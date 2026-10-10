---
description: Industrial VOC and gas sensors 2: H2S, NO2, SO2, O3, VOC PID, electrochemical. Higher precision, industrial calibration required. Applications: industrial safety, air quality.
title: Gas 2 VOC Industrial
tags: [esp32, sensor, gas, voc, h2s, no2, industrial, electrochemical]
category: Sensori
lang: en
original: 10-Sensors/22-Gas-2-VOC-Industrial.md
date-created: 2026-09-27
date: 2026-10-08
---

# Gas 2 VOC Industrial

## Purpose

Industrial gas sensors: H2S (electrochemical), NO2, SO2, O3 (electrochemical / PID), VOC PID (photoionization, ppb-ppm). Applications: industrial safety, environmental monitoring, chemical plants.

## Characteristics

| Gas | Range | Response time | Note |
| --- | --- | --- | --- |
| H2S | 0-100 ppm | < 30 s | Electrochemical |
| NO2 | 0-5 ppm | < 60 s | Electrochemical |
| SO2 | 0-20 ppm | < 30 s | Electrochemical |
| VOC (PID) | 0-2000 ppm / ppb | < 5 s | PID lamp |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | No calibration | Wrong ppm | Calibrate with standard gas |
| 2 | Humidity too high | Drift | Use humidity compensation |

## Official sources

- Manufacturer datasheets - `check manually`.

## See also

- [[EN/10-Sensors/17-Gas-CO2-Precision.en]]
