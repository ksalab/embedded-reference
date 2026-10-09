---
description: Energy meters: ACE712, PZEM-017, INA219 + shunt, CT clamp, wattmeter modules. Applications: power monitoring, energy tracking.
title: Energy Meters
tags: [esp32, sensor, energy, meter, pzem, ina219, acs712]
category: Sensori
lang: en
original: 10-Sensors/21-Energy-Meters.md
date-created: 2026-09-27
date: 2026-10-08
---

# Energy Meters

## Purpose

Energy and power measurement modules: PZEM-017 (UART, 0-100A/400V, energy), INA219 with shunt (I2C, 26V 2A), ACE712, CT clamp, wattmeter modules. Applications: home energy monitoring, solar tracking.

## Characteristics

| Module | Interface | Range | Accuracy |
| --- | --- | --- | --- |
| PZEM-017 | UART | 0-100A / 0-400V | ±1% |
| INA219 | I2C | 26V / 2A | ±0.5% |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | Shunt wrong value | Wrong current | Use exact shunt resistance |
| 2 | PZEM wrong baud/address | No data | Default 9600 / address 1 |

## Official sources

- PZEM manual - see manufacturer.
- INA219 Datasheet (TI) - `check manually`.

## See also

- [[EN/10-Sensors/15-ACS712-ZMPT101B-PZEM-AS5600-FSR.en]]
- [[06-Analog/01-ADC|ADC]]
