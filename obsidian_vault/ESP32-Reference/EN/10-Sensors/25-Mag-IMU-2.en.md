---
description: Magnetic IMU 2: HMC5883 magnetometer, BNO055 absolute orientation, LSM303. Applications: navigation, position tracking.
title: Mag IMU 2
tags: [esp32, sensor, mag, imu, hmc5883, bno055, lsm303]
category: Sensori
lang: en
original: 10-Sensors/25-Mag-IMU-2.md
date-created: 2026-09-27
date: 2026-10-08
---

# Mag IMU 2

## Purpose

Magnetometer and IMU for navigation and orientation: HMC5883 (I2C magnetometer), BNO055 (9 DOF absolute), LSM303 (accel+mag). Applications: compass, heading, motion tracking.

## Characteristics

| Sensor | Type | Interface | Note |
| --- | --- | --- | --- |
| HMC5883 | Magnetometer | I2C 0x1E | ±8 Gauss |
| BNO055 | 9 DOF | I2C 0x28 | Fusion, absolute |
| LSM303 | Accel+Mag | I2C 0x19 | Low power |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | Magnetometer near ferrous metal | Offset | Hard-iron calibration; keep away |

## See also

- [[EN/10-Sensors/19-IMU-6-9DOF.en]]
- [[EN/10-Sensors/16-HMC5883-BNO055-RFID-RC522-Barcode.en]]
