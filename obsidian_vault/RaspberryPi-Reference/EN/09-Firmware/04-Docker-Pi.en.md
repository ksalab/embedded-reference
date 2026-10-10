---
title: Docker on Raspberry Pi - Containers, Volumes, Systemd
description: Explains Docker on Raspberry Pi: installation, volumes, systemd autostart with compose; shows schematics, code and tables.
tags: [raspberrypi, docker, container, systemd, compose, raspberrypi-os, gpio, deployment]
category: Proshivka
lang: en
original: 09-Firmware/04-Docker-Pi.md
date-created: 2026-10-07
date: 2026-10-09
---

# Docker on Raspberry Pi - Containers, Volumes, Systemd

![[assets/img/rpi-docker-systemd-scheme.png|600]]
*Fig. Container with a volume on the Pi host, control through systemd - a standalone service without cron.*

> [!tip] What this note is
> After flashing and OS setup a container stack is needed: Docker Engine installs from the official repo, containers get volumes from the host FS, and systemd starts them as services. Next: [[EN/09-Firmware/03-OS-Setup.en|OS setup]], related: [[EN/08-Memory/01-SD-eMMC-NVMe.en|storage media]].

## 1. Goal

Run Docker on Raspberry Pi OS (Bookworm / Lite):

- Docker Engine install from the official Docker repository;
- container run with volume binding (bind mount / named volume);
- autostart through systemd (docker-compose + systemd unit or docker service);
- resource check (RAM, CPU, disk) and typical issues.

## 2. Process architecture

```mermaid
flowchart LR
  C[Container] -->|mounts| V[Volume / host bind]
  V --> PI[Pi OS rootfs /]
  PI --> SD[Systemd service / docker-compose]
  SD --> A[App autostart]
```

A container keeps no data inside itself: the volume lives on host SD/NVMe, systemd starts the service after boot, not through cron.

## 3. Docker Engine install

```bash
# Оновлення пакунків
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker
# Перевірка
sudo docker version
sudo docker info | grep -i architecture
```

For Raspberry Pi OS the official repo is `download.docker.com/linux/debian` (Bookworm). Avoid the outdated `snap` or a manual `.deb` of another architecture.

## 4. Docker Compose (yaml)

```yaml
# compose.yml
services:
  app:
    image: nginx:alpine
    container_name: rpi_nginx
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
      - rpi_log:/var/log/nginx
    environment:
      - NGINX_HOST=localhost
volumes:
  rpi_log:
```

Run: `docker compose up -d`. The `rpi_log` volumes live in `/var/lib/docker/volumes` on the host.

## 5. Systemd integration

```bash
# /etc/systemd/system/docker-app.service
[Unit]
Description=Docker Compose App
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/pi/project
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down

[Install]
WantedBy=multi-user.target
```

Activate: `sudo systemctl enable --now docker-app`.

## 6. Docker run with a volume (bash)

```bash
# Named volume
sudo docker run -d --name rpi_redis \
  -v rpi_redis_data:/data \
  -p 6379:6379 \
  --restart unless-stopped \
  redis:7-alpine

# Bind mount з хост FS
sudo docker run -d --name rpi_sensor \
  -v /home/pi/gpio:/app/gpio:ro \
  -e PYTHONUNBUFFERED=1 \
  --restart unless-stopped \
  python:3.11-slim
```

A volume with `-v` lives on the host and survives container removal.

## 7. Typical issues (7)

| Symptom | Cause | Fix |
| --- | --- | --- |
| `Cannot connect to Docker daemon` | user not in docker group / daemon down | `sudo usermod -aG docker` + `sudo systemctl restart docker` |
| `no space left on device` | SD full / large volumes | `docker system prune -a`, move volumes to NVMe |
| `Permission denied` on volume | container UID differs from host | `--user $(id -u):$(id -g)` or `chmod 777` for test |
| Container dead after reboot | no `restart: unless-stopped` / systemd | add policy in compose or unit |
| `manifest for ... not found` | image for arm/v7 instead of arm64 | `docker pull --platform linux/arm/v7` or use `arm32v7` |
| GPIO not visible from container | `/dev/gpiochip0` not passed | `--device /dev/gpiochip0 --device /dev/gpiochip1` |
| `error during connect` Docker after update | old docker-ce version | `apt upgrade docker-ce` from Docker repo, not Debian |

## 8. Resource advice

- RAM: Pi 4/5 with 4-8 GB - enough for 3-5 light containers; heavy ML loads fit Pi 5 with 8 GB or an external GPU better.
- CPU: a container does not speed the core; for real time use Pi OS Lite + CPU isolation through `systemd` settings, not Docker.
- Disk: `docker system df`; keep images on external NVMe through a `/var/lib/docker` symlink.
- Journal: `journalctl -u docker -n 50`; `docker logs --tail 100 rpi_nginx`.

## 9. Related notes (See also)

- [[EN/09-Firmware/03-OS-Setup.en|OS setup]] - base services and users.
- [[EN/08-Memory/01-SD-eMMC-NVMe.en|storage media]] - how to move `/var/lib/docker` to NVMe.
- [[EN/02-Power-Supply/01-USB-C-PD.en|USB-C power supply]] - stability under heavy load.
- [[EN/09-Firmware/01-Imager-Headless.en|Imager and headless]] - SD preparation before Docker install.

## 10. Quick cheat sheet

- `curl -fsSL https://get.docker.com | sh` - install.
- `docker compose up -d` + `systemctl enable docker-app` - run + autostart.
- `docker system prune -a` - cleanup.
- `--device /dev/gpiochip0` - GPIO into the container.
- Volumes on the host, not in the container - data live after `docker rm`.

## Official sources

- [Install Docker Engine on Raspberry Pi OS](https://docs.docker.com/engine/install/raspberry-pi-os/) - official Docker guide for Pi OS.
- [Raspberry Pi Documentation (Getting Started)](https://www.raspberrypi.com/documentation/computers/getting-started.html) - Pi base docs, services, boot.
- [Raspberry Pi Software](https://www.raspberrypi.com/software/) - Imager, OS, repo for Pi OS.
- [GPIO Zero docs](https://gpiozero.readthedocs.io/) - GPIO library, container fit (access to `/dev/gpiochip*`).
- [Docker Compose specification](https://docs.docker.com/compose/compose-file/05-services/) - `compose.yml` format, volumes, restart.
