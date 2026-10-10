---
title: Weather Station - Sensors and Display
description: Builds weather station with temperature, humidity, pressure sensors and display; shows schematics, code and tables.
tags: [arduino, weather, station, sensor, display]
category: Proekti
lang: en
original: 16-Projects/01-Meteostantsiya.md
date-created: 2026-10-05
date: 2026-10-09
---

# Weather Station - Sensors and Display

![[assets/img/arduino-weather-station-scheme.png|600]]
*Fig. Weather station: sensors outside, board inside, display with pressure, temperature, humidity.*

> [!tip] Purpose
> Build station from sensors to display with data and history.

## 1. Goal

Measure temperature, humidity, pressure; show on display; save to SD.

## 2. Sensors

| Sensor | Parameter | Interface |
| --- | --- | --- |
| DHT22 | Temp, humidity | Digital |
| BMP280 | Pressure, temp | I2C |

## 3. Display

LCD or OLED shows current and trends.

## 4. Sketch fragment

```cpp
#include <Wire.h>
void setup() {}
void loop() {}
```

## 5. Sensor details

| Sensor | Measurement range | Accuracy | Notes |
| --- | --- | --- | --- |
| DHT22 | -40 to 80 C, 0-100% | +/- 0.5 C, +/- 2% | Slow response |
| BMP280 | -40 to 85 C, 300-1100 hPa | +/- 1 hPa | I2C address 0x76 or 0x77 |

Calibration allows offset correction for individual units.

## 6. Display formats

| Mode | Content | Update rate |
| --- | --- | --- |
| Current | Numbers and icons | Every second |
| History | Last 24 hours | Every minute |
| Alarm | Threshold alert | Immediate |

## 7. Power and enclosure

Use 5 V power supply with stable voltage; enclosure protects from rain and dust; antenna outside if IoT.

## 8. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | Wrong reading | Check wiring and calibration |
| 2 | No display | Verify library and pin connections |
| 3 | No data save | Check storage format and capacity |

## 9. Official sources

- [DHT22 docs](https://www.dht22.com/)
- [BMP280 datasheet](https://www.bosch-sensortec.com/)
- [Arduino sensors guide](https://docs.arduino.cc/learn/electronics/sensors/)

## See also

- [[Home.en]]
- [[EN/11-Vivid/01-LCD1602.en|Character screen]]
