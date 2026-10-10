---
description: Industrial sensors: vibration, temperature, pressure, gas, flow for industrial automation and predictive maintenance. Applications: predictive maintenance, process control.
title: Industrial Sensors
tags: [esp32, sensor, industrial, vibration, predictive, maintenance]
category: Sensori
lang: en
original: 10-Sensors/38-Industrial-Sensors.md
date-created: 2026-09-27
date: 2026-10-08
---

# Industrial Sensors

## Purpose

Industrial monitoring sensors: vibration (accelerometer), temperature (PT100, thermocouple), pressure (4-20 mA), gas (electrochemical), flow (Hall / ultrasonic). Applications: predictive maintenance, process control.

## Characteristics

| Sensor | Type | Interface | Note |
| --- | --- | --- | --- |
| Vibration | Accel / piezo | I2C / analog | High frequency |
| Temperature PT100 | Resistance | SPI MAX31865 | 4-wire |
| Pressure | 4-20 mA / 0-10V | ADC / I2C | Calibrate |
| Gas | Electrochemical | UART / analog | Calibrate with standard |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | 4-20 mA wrong resistor | Wrong pressure | Use 250 Ω resistor; 1V = 4 mA, 5V = 20 mA |
| 2 | Industrial noise | Unstable values | Shielded cables; filter; average 10-20 samples |

## See also

- [[EN/10-Sensors/30-Temp-Precision.en]]
- [[EN/10-Sensors/15-ACS712-ZMPT101B-PZEM-AS5600-FSR.en]]
