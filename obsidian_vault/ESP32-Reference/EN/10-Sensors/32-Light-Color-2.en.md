---
description: Light color 2: TCS3200 RGB, APDS-9960, TSL2561 lux, ML8511 UV, color temperature. Applications: ambient, color control.
title: Light Color 2
tags: [esp32, sensor, light, color, tcs3200, tsl2561, ml8511]
category: Sensori
lang: en
original: 10-Sensors/32-Light-Color-2.md
date-created: 2026-09-27
date: 2026-10-08
---

# Light Color 2

## Purpose

Light and color sensors: TCS3200 (RGB + clear), TSL2561 lux, ML8511 UV, APDS-9960 gesture/proximity. Applications: ambient adaptation, color control, gesture.

## Characteristics

| Sensor | Feature | Interface | Note |
| --- | --- | --- | --- |
| TCS3200 | RGB + clear | I2C / SPI | Filter selection |
| TSL2561 | Lux 0.1-40k | I2C 0x39 | Photodiode |
| ML8511 | UV index | Analog / I2C | 280-390 nm |

## See also

- [[EN/10-Sensors/18-Light-Spectral-Gesture.en]]
- [[EN/10-Sensors/10-VL53L0X-TCS34725-TSL2561.en]]
