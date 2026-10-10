---
description: Light spectral, gesture, proximity: TCS3200 color, APDS-9960 gesture/proximity, VL53L0X ToF, TSL2561 lux. Applications: ambient control, gesture interface, distance.
title: Light Spectral Gesture
tags: [esp32, sensor, light, color, gesture, proximity, tof, lux]
category: Sensori
lang: en
original: 10-Sensors/18-Light-Spectral-Gesture.md
date-created: 2026-09-27
date: 2026-10-08
---

# Light Spectral Gesture

## Purpose

Ambient and interaction sensors: TCS3200 color (R-G-B clear, I2C/SPI), APDS-9960 gesture/proximity (I2C), VL53L0X ToF (I2C, 50-1200 mm), TSL2561 lux (I2C). Applications: ambient light adaptation, gesture control, distance measurement.

## Characteristics

| Sensor | Range / Feature | Interface | Note |
| --- | --- | --- | --- |
| TCS3200 | RGB + clear | I2C / SPI | Filter selection |
| APDS-9960 | Proximity 20-100 mm, gesture | I2C 0x39 | 4-direction gesture |
| VL53L0X | 50-1200 mm | I2C 0x29 | ToF, ±1 mm |
| TSL2561 | 0.1-40,000 lux | I2C 0x39 / 0x29 | Photodiode |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | APDS gesture false | Wrong direction | Calibrate with library; avoid strong light |
| 2 | VL53L0X no reading | Out of range or black surface | Use within 50-1200 mm; avoid pure black |

## Official sources

- TCS3200 Datasheet - `check manually`.
- VL53L0X Guide (ST) - see manufacturer.

## See also

- [[EN/10-Sensors/26-Light-UV-IRArray-ToF.en]]
