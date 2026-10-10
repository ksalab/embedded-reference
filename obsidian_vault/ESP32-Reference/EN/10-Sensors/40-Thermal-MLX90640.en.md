---
description: Thermal MLX90640 infrared array 32x24, I2C, 768 pixels, 16 Hz, 0-300 °C, medical/industrial thermal imaging. Applications: thermal imaging, fever screening.
title: Thermal MLX90640
tags: [esp32, sensor, mlx90640, thermal, ir-array, temperature]
category: Sensori
lang: en
original: 10-Sensors/40-Thermal-MLX90640.md
date-created: 2026-09-27
date: 2026-10-08
---

# Thermal MLX90640

## Purpose

Thermal imaging sensor MLX90640 (32x24 IR array, 768 pixels, I2C 0x33, 16 Hz, 0-300 °C). Applications: thermal imaging, fever screening, industrial monitoring.

## Characteristics

| Parameter | Value |
| --- | --- |
| Array | 32 x 24 (768 pixels) |
| Frame rate | 16 Hz |
| Temperature range | −40…300 °C |
| Interface | I2C 0x33 |
| Accuracy | ±1.5 °C (typical) |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | No image | Wrong I2C address | Check 0x33; check wiring |
| 2 | Hot spots | Calibration needed | Use library calibration; check emissivity |

## Official sources

- MLX90640 Datasheet (Melexis) - `check manually`.

## See also

- [[EN/10-Sensors/20-Bio-IR-Temp.en]]
