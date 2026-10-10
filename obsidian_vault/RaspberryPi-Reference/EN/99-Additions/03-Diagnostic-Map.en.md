---
title: RaspberryPi-Reference diagnostic card - symptom, device, action
description: Quick diagnosis card - a symptom, which device to look at and what to do, for all subsystems of the board.; shows schematics, code and tables.
tags: [raspberrypi, diagnostics, troubleshooting, map, dodatok]
category: Dodatki
lang: en
original: RaspberryPi-Reference/99-Additions/03-Diagnostic-Map.md
date-created: 2026-10-01
date: 2026-10-08
---

# RaspberryPi-Reference diagnostic card - symptom, device, action

## Food

| Symptom | Device | Action |
| --- | --- | --- |
| Lightning / rebut | USB tester, `get_throttled` | BJ + cable |
| BZ is warming up hand / pyrometer | current reserve 30% |
| USB falls off | USB tester in a gap | powered hub |

## Loading

| Symptom | Device | Action |
| --- | --- | --- |
| ACT 4/7/8 flashes | eyes + code table | flash media |
| A rainbow hangs monitor | edit config.txt on PC |
| Everything is silent UART console | see boot log |

## GPIO and buses

| Symptom | Device | Action |
| --- | --- | --- |
| The sensor is silent | `i2cdetect` → analyzer | bus, address, power |
| The button jumps | event log | bounce_time |
| Pin is dead | multimeter | move, put a level converter |

## Network

| Symptom | The reason | Action |
| --- | --- | --- |
| No 5 GHz | country | raspi-config |
| Tears every hour | PM | disable, watchdog |
| Slowly | channel/signal | scanner, wire |

## See also- [[99-Additions/01-Troubleshooting-FAQ | FAQ]] - detailed answers.- [[99-Additions/02-Datasheet-Links | links to datasheets]] - documents.- [[17-Lab/01-Priladi | laboratory devices]] - arsenal.- [[Home | main map]] - full navigation.

## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.


## Official sources

- STMicroelectronics reference manuals and datasheets
- Official ST-Link documentation
- Arduino / Raspberry Pi official guides
