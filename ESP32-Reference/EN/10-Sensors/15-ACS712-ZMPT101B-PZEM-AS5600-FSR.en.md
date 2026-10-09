---
description: ACS712 current sensor (5A/20A/30A), ZMPT101B voltage, PZEM-017 power meter, AS5600 magnetic encoder, FSR resistive force: analog/current/I2C/pulse outputs. Applications: power monitoring, position, force.
title: ACS712, ZMPT101B, PZEM, AS5600, FSR
tags: [esp32, sensor, acs712, zmpt, pzem, as5600, fsr, current, voltage, power]
category: Sensori
lang: en
original: 10-Sensors/15-ACS712-ZMPT101B-PZEM-AS5600-FSR.md
date-created: 2026-09-27
date: 2026-10-08
---

# ACS712, ZMPT101B, PZEM, AS5600, FSR

## Purpose

Current sensing ACS712 (Hall, analog 2.5V ±), voltage ZMPT101B (isolation, analog), power meter PZEM-017 (UART/Modbus), magnetic encoder AS5600 (I2C 12-bit), force sensor FSR (resistive analog). Applications: energy monitoring, position, force measurement.

## Characteristics

| Sensor | Range | Output | Note |
| --- | --- | --- | --- |
| ACS712 5A | ±5 A | Analog 2.5V ± | 185 mV/A |
| ACS712 20A | ±20 A | Analog | 100 mV/A |
| ZMPT101B | 100V AC | Analog | Isolation transformer |
| PZEM-017 | 0-100A / 0-400V | UART / Modbus | Power, energy |
| AS5600 | 0-360° | I2C 12-bit | Magnetic |
| FSR | 0-10 kg | Analog resistance | Non-linear |

## Wiring diagram

| ESP32 | Sensor | Note |
| --- | --- | --- |
| 3V3 | VCC / AS5600 SDA/SCL | 3.3 V |
| GND | GND | Star |
| GPIO32 | ACS712 AO | ADC1 |
| GPIO35 | ZMPT AO | ADC1 |
| UART RX/TX | PZEM | 9600 baud |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | ACS712 near AC line without isolation | Noise, risk | Use isolated module; keep distance |
| 2 | ZMPT without calibration | Wrong voltage | Calibrate with known source |
| 3 | PZEM wrong baud | No data | 9600 default; check address |

## Official sources

- ACS712 Datasheet (Allegro) - `check manually`.
- PZEM manual - see manufacturer.

## See also

- [[06-Analog/01-ADC|ADC]]
- [[EN/04-Interfaces/01-UART.en|UART]]
