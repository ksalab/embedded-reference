---
description: Agro sensors: soil moisture, temperature, humidity for agriculture, greenhouse, irrigation control. Applications: smart agriculture, auto-irrigation.
title: Agro
tags: [esp32, sensor, agro, soil, moisture, irrigation, greenhouse]
category: Sensori
lang: en
original: 10-Sensors/36-Agro.md
date-created: 2026-09-27
date: 2026-10-08
---

# Agro

## Purpose

Agricultural sensors: soil moisture (capacitive / resistive), temperature, humidity, light for greenhouse / irrigation. Applications: smart farming, auto-irrigation.

## Characteristics

| Sensor | Range | Interface | Note |
| --- | --- | --- | --- |
| Soil moisture | 0-100% | Analog | Capacitive preferred |
| Temp/Humidity | −40…85 °C / 0-100% RH | I2C / analog | BME280 / DHT |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | Resistive soil sensor | Corrosion | Use capacitive; calibrate |
| 2 | Direct sun on sensor | Drift | Shade / enclosure |

## See also

- [[EN/10-Sensors/03-BME280-BMP280-SHT31.en]]
- [[EN/10-Sensors/07-AHT10-AHT20-SHT40.en]]
