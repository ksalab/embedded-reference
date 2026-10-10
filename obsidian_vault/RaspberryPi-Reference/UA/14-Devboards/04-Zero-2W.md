---
title: Raspberry Pi Zero 2 W - малюк з Linux для IoT-вузлів
description: Розбирає найменшу Linux-плату - Zero 2 W: живлення, OTG-хаби, камери, безголовний режим і межі застосування.
tags: [raspberrypi, zero-2w, iot, otg, headless, wifi, devboard]
category: Devboards
date: 2026-10-06
---

# Raspberry Pi Zero 2 W - малюк з Linux для IoT-вузлів

![[assets/img/rpi-zero2w-board-scheme.png|600]]
*Рис. Zero 2 W: micro-USB живлення+OTG, mini-HDMI, CSI - повноцінний Linux на марці.*

> [!tip] Що це за нота
> Кишеньковий Linux за ціною піци: 4 ядра, WiFi, камера - для датчиків, камер-пасток і USB-гаджетів. Вибір: [[00-Start/03-Porivnyannya-plate|порівняння моделей]], покупка: [[00-Start/04-Devkit-plati|плати і аксесуари]].

## 1. Мета

Вичавити максимум з 65×30 мм:

- живлення і OTG-режими без сюрпризів;
- headless-налаштування з першого boot;
- камера і датчики на малій платі;
- чесні межі: що Zero не тягне.

| Параметр | Значення |
| --- | --- |
| SoC | RP3A0: 4×A53 1 ГГц (SiP з RAM) |
| RAM | 512 МБ LPDDR2 |
| Радіо | WiFi + BT 4.2 |
| USB | 1×micro-USB OTG (дані+живлення роздільно!) |
| Відео | mini-HDMI, CSI-камера |
| Живлення | micro-USB 5V 2.5A |

Два micro-USB: PWR (тільки живлення) і USB (OTG-дані). Плутанина портів - класика першого запуску.

## 2. Архітектура плати

```mermaid
flowchart TB
  PWR[micro-USB PWR] --> Z[Zero 2 W]
  OTG[micro-USB OTG] --> Z
  Z --> HDMI[mini-HDMI]
  Z --> CSI[CSI-камера]
  Z --> GPIO[Гребінка 40 (є версія WH)]
  OTG --> HUB[OTG-хаб: клавіатура+миша]
  Z -->|WiFi| NET[Мережа]
```

Версія WH - з розпаяною гребінкою (+пара доларів, економить паяння). Без H - паяємо самі або беремо hammer-header без паяльника.

## 3. Headless-запуск

- Imager: ОС Lite 64-bit, SSH, WiFi, користувач - усе в майстрі;
- перший boot 1-2 хвилини (розгортання);
- `ssh user@raspberrypi.local` або IP з роутера;
- hostname міняємо одразу (`raspi-config`) - в мережі буде кілька Zero;
- годинник - тільки NTP, RTC немає.

## 4. OTG-режими

- хост: хаб → клавіатура/миша/FM-донгл;
- гаджет: Zero як Ethernet/USB-серійник для ПК (`dtoverlay=dwc2`);
- Pi-KVM-подібні сценарії: клавіатура/миша для іншого ПК;
- живлення через OTG-кабель не йде - PWR окремо!

## 5. Робочий код: IoT-вузол

```python
import time
import board
import busio
import adafruit_bme280
from gpiozero import LED
import paho.mqtt.client as mqtt

i2c = busio.I2C(board.SCL, board.SDA)
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
led = LED(17)
cl = mqtt.Client()
cl.connect("broker.local", 1883, 60)
cl.loop_start()

while True:
    t = bme.temperature
    h = bme.humidity
    cl.publish("zero2w/climate", f"{t:.1f},{h:.0f}")
    led.toggle()
    time.sleep(60)
```

Blinka-бібліотеки (`board`, `busio`) - міст CircuitPython на Pi. Працюють на всіх Linux-платах однаково.

## 6. Камера на Zero

- CSI-роз'єм: Camera Module 3 або AI Camera;
- libcamera + Picamera2 - той же код, що на Pi 4/5 (деталі - в ноті камери);
- пастка-кадр раз на хвилину + MQTT - класика;
- відео 1080p декодує, стрім тягне, але з натугою.

## 7. Межі застосування

- десктоп - ні: 512 МБ і один USB вбивають ідею;
- компіляція великого - ні: своп на SD повільний, збираємо на Pi 4/5;
- USB-аудіо/диски - через хаб з живленням;
- 24/7 - так, споживання ~1W, гріється слабо;
- кластер з Zero - навчальний, не бойовий.

## 7.1 USB-гаджети Zero: режими

- Ethernet-гаджет: Zero як мережева карта для ПК;
- Serial-гаджет: консоль по USB без мережі;
- Mass-storage: шматок SD як флешка для ПК;
- MIDI-гаджет: кнопки в музичний софт;
- комбо: Ethernet + Serial одночасно;
- увімкнення - `dtoverlay=dwc2` + модулі `g_ether`/`g_serial`.

## 8. Типові помилки

| Симптом | Причина | Лікування |
| --- | --- | --- |
| Не стартує | кабель у OTG замість PWR | живлення - в порт PWR |
| WiFi не бачить 5 ГГц | його немає (тільки 2.4) | точка 2.4 ГГц |
| Клавіатура не працює | OTG без хаба/живлення | хаб з живленням |
| Гальмує Desktop | 512 МБ + своп | тільки Lite |
| Камера чорна | шлейф/несумісний модуль | перевірити шлейф, libcamera-стек |
| Губиться в мережі | однаковий hostname | унікальне ім'я кожному Zero |

## 9. Суміжні ноти

- [[00-Start/03-Porivnyannya-plate|порівняння моделей]] - місце Zero в лінійці.
- [[09-Proshivka/01-Imager-Headless|прошивка Imager]] - headless-установка.
- Клімат BME280 як перший датчик - нота черги 3 (розділ сенсорів).
- Камера CSI детально - нота черги 3 (розділ сенсорів).
- [[15-Protokoli/01-MQTT|протокол MQTT]] - телеметрія вузла.

## 9.1 Швидка шпаргалка Zero 2 W

- живлення в PWR, дані в OTG;
- тільки Lite, тільки 2.4 ГГц;
- хаб з живленням для периферії;
- унікальний hostname кожному;
- гаджет-режими через `dwc2`.

## Офіційні джерела

- [Raspberry Pi Zero 2 W (Raspberry Pi)](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) - характеристики і живлення.
- [Getting Started (Raspberry Pi docs)](https://www.raspberrypi.com/documentation/computers/getting-started.html) - OTG і headless.
- [gpiozero docs (Read the Docs)](https://gpiozero.readthedocs.io/en/stable/) - піни і LED.
