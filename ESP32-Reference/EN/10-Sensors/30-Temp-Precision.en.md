---
description: Precision temperature sensors: PT100/PT1000 4-wire, MAX31865, LM35, TMP36, DS18B20 precision mode, thermocouple K/N type, calibration. Applications: precise temperature measurement.
title: Temp Precision
tags: [esp32, sensor, pt100, pt1000, max31865, lm35, tmp36, thermocouple]
category: Sensori
lang: en
original: 10-Sensors/30-Temp-Precision.md
date-created: 2026-09-27
date: 2026-10-08
---

# Temp Precision

## Purpose

High-precision temperature measurement: PT100/PT1000 4-wire (MAX31865 SPI), LM35/TMP36 analog 10 mV/°C, DS18B20 12-bit, K/N thermocouple with cold-junction compensation. Applications: calibration, lab, industrial.

## Characteristics

| Sensor | Accuracy | Interface | Range |
| --- | --- | --- | --- |
| PT100 class A | ±0.15 °C | SPI MAX31865 | −200…+850 °C |
| LM35 | ±0.5 °C | ADC | −55…+150 °C |
| TMP36 | ±1 °C | ADC | −40…+125 °C |
| K thermocouple | ±2 °C | SPI MAX6675 | 0…1024 °C |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | PT100 2-wire | +1-2 °C error | Use 3/4-wire |
| 2 | No cold-junction comp | Wrong thermocouple | Use MAX6675 / MAX31865 |

## See also

- [[EN/10-Sensors/11-NTC-PT100-MAX6675-LM35.en]]
