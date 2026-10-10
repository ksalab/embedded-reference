---
description: HMC5883 magnetometer, BNO055 IMU, RFID RC522, barcode scanner: I2C/SPI, position, orientation, identification. Applications: navigation, tracking, access.
title: HMC5883, BNO055, RFID RC522, Barcode
tags: [esp32, sensor, hmc5883, bno055, rfid, rc522, barcode]
category: Sensori
lang: en
original: 10-Sensors/16-HMC5883-BNO055-RFID-RC522-Barcode.md
date-created: 2026-09-27
date: 2026-10-08
---

# HMC5883, BNO055, RFID RC522, Barcode

## Purpose

Sensors for positioning and identification: HMC5883 (I2C magnetometer, 1-8 Gauss), BNO055 (I2C 9-axis absolute orientation with fusion), RFID RC522 (SPI 13.56 MHz MIFARE), barcode scanner (USB/serial or module). Applications: navigation, tracking, access control.

## Characteristics

| Sensor | Interface | Features |
| --- | --- | --- |
| HMC5883 | I2C 0x1E | ±8 Gauss, 160 Hz |
| BNO055 | I2C 0x28 | 9 DOF, absolute orientation |
| RC522 | SPI / I2C optional | 13.56 MHz, MIFARE |
| Barcode | USB / UART | Serial output |

## Wiring diagram

| ESP32 | Sensor | Note |
| --- | --- | --- |
| 3V3 | VCC | 3.3 V |
| GND | GND | Common |
| GPIO21 | SDA / I2C data | Pull-up |
| GPIO22 | SCL / I2C clock | Pull-up |
| GPIO18/19/23/5 | SPI RC522 | VSPI |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | HMC5883 near metal | Offset error | Calibrate with circle; keep away from magnets |
| 2 | BNO055 no fusion | No orientation | Use library with fusion enabled |
| 3 | RC522 not detected | SPI CS wrong | Check CS pin; 3.3 V only |

## Official sources

- BNO055 Datasheet (Bosch) - `check manually`.
- RC522 Datasheet (NXP) - `check manually`.

## See also

- [[EN/04-Interfaces/03-I2C.en|I2C]]
- [[EN/04-Interfaces/02-SPI.en|SPI]]
