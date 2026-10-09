---
description: New generation environmental sensors: BME680 (gas, pressure, temp, humidity), CCS811 (TVOC/eCO2, I2C), MH-Z19 (CO2), PMS5003 (dust). Applications: smart environment.
title: Env NewGen
tags: [esp32, sensor, bme680, ccs811, mh-z19, pms, env]
category: Sensori
lang: en
original: 10-Sensors/28-Env-NewGen.md
date-created: 2026-09-27
date: 2026-10-08
---

# Env NewGen

## Purpose

Next-gen combined environmental sensors: BME680 (pressure, temp, humidity, gas resistance, I2C/SPI), CCS811 (TVOC/eCO2 I2C 0x5B), MH-Z19 CO2 UART, PMS5003 dust UART. Applications: smart home, indoor air quality.

## Characteristics

| Sensor | Measures | Interface | Note |
| --- | --- | --- | --- |
| BME680 | P,T,H,gas | I2C/SPI 0x76 | Gas resistance |
| CCS811 | TVOC, eCO2 | I2C 0x5B | Requires burn-in |
| MH-Z19 | CO2 | UART 9600 | NDIR |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | CCS811 no data | Not initialized | Run startup sequence |
| 2 | BME680 gas not calibrated | Wrong gas | Calibrate with clean air |

## See also

- [[EN/10-Sensors/03-BME280-BMP280-SHT31.en]]
- [[EN/10-Sensors/08-BME680-CCS811-MHZ19-PMS5003.en]]
