---
description: 6-axis / 9-axis IMU: MPU6050 (I2C 6 DOF), BNO055 (9 DOF absolute), LSM6DS3, ADXL345, MMA8452. Applications: motion, orientation, gesture.
title: IMU 6-9 DOF
tags: [esp32, sensor, imu, mpu6050, bno055, 6dof, 9dof]
category: Sensori
lang: en
original: 10-Sensors/19-IMU-6-9DOF.md
date-created: 2026-09-27
date: 2026-10-08
---

# IMU 6-9 DOF

## Purpose

Inertial measurement units for motion tracking: MPU6050 (I2C 6 DOF accel+gyro, DMP), BNO055 (I2C 9 DOF with fusion, absolute), LSM6DS3, ADXL345, MMA8452. Applications: motion detection, orientation, gesture, stabilization.

## Characteristics

| IMU | DOF | Interface | Features |
| --- | --- | --- | --- |
| MPU6050 | 6 | I2C 0x68 | DMP, 6-axis |
| BNO055 | 9 | I2C 0x28 | Fusion, absolute |
| LSM6DS3 | 6 | I2C/SPI | Low power |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | MPU6050 no DMP | No quaternion | Use library with DMP support |
| 2 | BNO055 wrong mode | No orientation | Enable NDOF mode |

## Official sources

- MPU6050 Datasheet (InvenSense) - `check manually`.
- BNO055 Datasheet (Bosch) - `check manually`.

## See also

- [[EN/10-Sensors/04-MPU6050.en]]
- [[EN/10-Sensors/16-HMC5883-BNO055-RFID-RC522-Barcode.en]]
