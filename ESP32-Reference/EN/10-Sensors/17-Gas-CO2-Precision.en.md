---
description: Precision CO2 sensors MH-Z19, Sensirion SPS30, TE Connectivity: UART/I2C, 400-5000 ppm, NDIR principle. Applications: air quality, ventilation.
title: Gas CO2 Precision
tags: [esp32, sensor, co2, mh-z19, sps30, ndir]
category: Sensori
lang: en
original: 10-Sensors/17-Gas-CO2-Precision.md
date-created: 2026-09-27
date: 2026-10-08
---

# Gas CO2 Precision

## Purpose

High-precision CO2 sensors using NDIR (non-dispersive infrared): MH-Z19 (UART, 400-5000 ppm, ±50 ppm), Sensirion SPS30 (UART/I2C, PM1/2.5/10 + CO2, ±10% or ±40 ppm), TE Connectivity (industrial). Applications: indoor air quality, demand-controlled ventilation.

## Characteristics

| Model | Range | Interface | Accuracy | Note |
| --- | --- | --- | --- |
| MH-Z19 | 400-5000 ppm | UART 9600 | ±50 ppm + 3% | 3.3-5 V, warm-up 3 min |
| SPS30 | 400-10000 ppm | UART/I2C | ±10% or ±40 ppm | Also PM |
| TE | 0-50000 ppm | UART/I2C | ±3% | Industrial |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | No warm-up | Wrong initial reading | Wait 3-5 min after power-on |
| 2 | Direct sunlight / draft | Drift | Shield, avoid direct airflow |
| 3 | Incorrect UART baud | No data | Default 9600; check address |

## Official sources

- MH-Z19 Datasheet (Winsen) - `check manually`.
- SPS30 Datasheet (Sensirion) - `check manually`.

## See also

- [[EN/10-Sensors/22-Gas-2-VOC-Industrial.en]]
