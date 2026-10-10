---
description: Light UV IR array ToF: TCS3200 RGB, ML8511 UV, TSOP/TSL series IR, VL53L0X ToF, APDS-9960 gesture. Applications: ambient sensing, gesture control.
title: Light UV IR Array ToF
tags: [esp32, sensor, uv, ir, light, tof, gesture, tsl]
category: Sensori
lang: en
original: 10-Sensors/26-Light-UV-IRArray-ToF.md
date-created: 2026-09-27
date: 2026-10-08
---

# Light UV IR Array ToF

## Purpose

Multi-spectrum light and distance sensors: ML8511 UV (I2C/analog), TCS3200 RGB, APDS-9960 gesture/proximity, VL53L0X ToF. Applications: ambient adaptation, gesture interface, distance.

## Characteristics

| Sensor | Feature | Interface | Note |
| --- | --- | --- | --- |
| ML8511 | UV index | Analog / I2C | 280-390 nm |
| APDS-9960 | Proximity + gesture | I2C 0x39 | 4-direction |
| VL53L0X | ToF 50-1200 mm | I2C 0x29 | ±1 mm |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | UV sensor near window | High UV | Shield or use indoor |

## See also

- [[EN/10-Sensors/18-Light-Spectral-Gesture.en]]
- [[EN/10-Sensors/10-VL53L0X-TCS34725-TSL2561.en]]
