---
description: Range lidar and 60 GHz radar: VL53L1X (ToF 400-4000 mm), 60 GHz mmWave radar (XIAO? see module). Applications: presence, distance, motion.
title: Range Lidar 60GHz
tags: [esp32, sensor, vl53l1x, lidar, 60ghz, radar, range]
category: Sensori
lang: en
original: 10-Sensors/29-Range-Lidar-60GHz.md
date-created: 2026-09-27
date: 2026-10-08
---

# Range Lidar 60GHz

## Purpose

Range sensors: VL53L1X ToF 400-4000 mm (I2C 0x29), 60 GHz mmWave radar modules (motion + distance). Applications: presence detection, distance measurement, people counting.

## Characteristics

| Sensor | Range | Interface | Note |
| --- | --- | --- | --- |
| VL53L1X | 40-400 cm | I2C 0x29 | ToF |
| 60 GHz radar | 0-8 m / motion | UART / I2C | mmWave |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | VL53L1X black surface | No reading | Use within range; avoid pure black |

## See also

- [[EN/10-Sensors/10-VL53L0X-TCS34725-TSL2561.en]]
