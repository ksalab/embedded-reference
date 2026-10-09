---
description: Bio/IR temperature sensors: MLX90614 (IR 32x32, I2C), MLX90640 (32x24, I2C), body temperature, fever detection. Applications: health, non-contact temp.
title: Bio-IR Temperature
tags: [esp32, sensor, mlx90614, mlx90640, ir, temperature, bio]
category: Sensori
lang: en
original: 10-Sensors/20-Bio-IR-Temp.md
date-created: 2026-09-27
date: 2026-10-08
---

# Bio-IR Temperature

## Purpose

Non-contact infrared temperature sensors for body/industrial measurement: MLX90614 (I2C, 32x32 pixels or single point, medical version ±0.2 °C), MLX90640 (32x24 array, I2C, 32x32 possible with interpolation). Applications: fever screening, non-contact thermometry.

## Characteristics

| Sensor | Array | Range | Accuracy | Note |
| --- | --- | --- | --- |
| MLX90614 | 1-32x32 | −70…382 °C | ±0.2 °C (medical) | I2C 0x5A |
| MLX90640 | 32x24 | −40…300 °C | ±1.5 °C | I2C 0x33 |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | No ambient compensation | Wrong reading | Use ambient sensor or library compensation |
| 2 | Emissivity wrong | Low/high value | Set emissivity 0.95 for skin |

## Official sources

- MLX90614 Datasheet (Melexis) - `check manually`.
- MLX90640 Datasheet (Melexis) - `check manually`.

## See also

- [[EN/10-Sensors/30-Temp-Precision.en]]
