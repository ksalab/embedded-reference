---
description: Pressure, level, flow: BMP280/BME280 pressure (I2C/SPI), liquid level ultrasonic/capacitive, YF-S201 flow pulse. Applications: weather, tank, water.
title: Pressure Level Flow
tags: [esp32, sensor, pressure, bmp280, bme280, level, flow, yfs201]
category: Sensori
lang: en
original: 10-Sensors/24-Pressure-Level-Flow.md
date-created: 2026-09-27
date: 2026-10-08
---

# Pressure Level Flow

## Purpose

Environmental sensors: BMP280/BME280 (I2C/SPI, pressure 300-1100 hPa, temperature, humidity with BME), liquid level ultrasonic / capacitive, flow YF-S201 (Hall pulse per rotation, 450 pulses/L). Applications: weather, tank level, water flow.

## Characteristics

| Sensor | Range | Interface | Note |
| --- | --- | --- | --- |
| BMP280 | 300-1100 hPa | I2C/SPI 0x76/77 | Pressure, temp |
| BME280 | 300-1100 hPa / 0-100% RH | I2C/SPI | + humidity |
| Level ultrasonic | 2-400 cm | GPIO trigger/echo | HC-SR04 style |
| Flow YF-S201 | 1-30 L/min | Pulse / ADC | 450 pulses/L |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | Pressure wrong | No calibration | Calibrate at known pressure |
| 2 | Flow pulse missed | Wrong volume | Use interrupt; debounce |

## Official sources

- BMP280 Datasheet (Bosch) - `check manually`.

## See also

- [[EN/10-Sensors/03-BME280-BMP280-SHT31.en]]
