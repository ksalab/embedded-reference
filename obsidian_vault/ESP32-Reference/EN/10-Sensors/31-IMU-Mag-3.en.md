---
description: IMU Mag 3: LSM6DS3 (I2C/SPI accel+gyro), LSM303 (mag+accel), HMC5883, BNO055. Applications: motion, navigation, orientation.
title: IMU Mag 3
tags: [esp32, sensor, imu, mag, lsm6ds3, lsm303, hmc5883, bno055]
category: Sensori
lang: en
original: 10-Sensors/31-IMU-Mag-3.md
date-created: 2026-09-27
date: 2026-10-08
---

# IMU Mag 3

## Purpose

IMU and magnetometer combinations: LSM6DS3 (6 DOF, low power), LSM303 (accel+mag), HMC5883, BNO055 (9 DOF). Applications: motion tracking, compass, stabilization.

## Characteristics

| IMU | DOF / Type | Interface | Note |
| --- | --- | --- | --- |
| LSM6DS3 | 6 DOF accel+gyro | I2C/SPI | Low power |
| LSM303 | Accel + Mag | I2C 0x19 | Low power |
| BNO055 | 9 DOF | I2C 0x28 | Fusion |

## See also

- [[EN/10-Sensors/19-IMU-6-9DOF.en]]
- [[EN/10-Sensors/25-Mag-IMU-2.en]]
