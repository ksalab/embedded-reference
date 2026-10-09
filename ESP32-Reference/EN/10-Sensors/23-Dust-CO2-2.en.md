---
description: Dust and CO2 2: PMS5003/7003 (PM2.5, UART), SDS011, MH-Z19B (CO2 UART). Applications: air quality monitors.
title: Dust CO2 2
tags: [esp32, sensor, dust, pms, sds, mh-z19, pm25]
category: Sensori
lang: en
original: 10-Sensors/23-Dust-CO2-2.md
date-created: 2026-09-27
date: 2026-10-08
---

# Dust CO2 2

## Purpose

Dust and CO2 sensors for air quality: PMS5003/7003 (PM1/2.5/10 UART 9600). MH-Z19B (CO2 UART). SDS011 (dust laser). Applications: indoor monitors, weather stations.

## Characteristics

| Sensor | Range | Interface | Note |
| --- | --- | --- | --- |
| PMS5003 | 0-500 µg/m³ PM2.5 | UART 9600 | Passive / laser |
| SDS011 | 0-1000 µg/m³ | UART 9600 | Laser |
| MH-Z19B | 400-5000 ppm CO2 | UART 9600 | NDIR |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | PMS no data | Wrong baud | 9600 default |
| 2 | CO2 drift | No warm-up | Warm 3 min |

## Official sources

- PMS5003 Datasheet (Plantower) - `check manually`.
- MH-Z19B Datasheet (Winsen) - `check manually`.

## See also

- [[EN/10-Sensors/17-Gas-CO2-Precision.en]]
