---
title: GPS NEO-6M - Position from UART
description: Explains GPS NEO-6M module for position over UART with fix, baud and NMEA sentences; shows schematics, code and tables.
tags: [arduino, gps, neo-6m, uart, nmea, position]
category: Zvyazok
lang: en
original: 12-Comm-Modules/04-GPS-NEO.md
date-created: 2026-10-05
date: 2026-10-09
---

# GPS NEO-6M - Position from UART

![[assets/img/arduino-gps-neo-scheme.png|600]]
*Fig. GPS module with antenna, UART to board, 3.3 or 5 V, NMEA sentences.*

> [!tip] Purpose of this note
> Get position from satellite: connect UART, read NMEA sentences, extract latitude and longitude.

## 1. Purpose

GPS module gives time, position, speed over UART; used for trackers, navigation.

## 2. Characteristics

| Parameter | Value | Note |
| --- | --- | --- |
| Chip | NEO-6M | 50 channels |
| Interface | UART | 9600 baud |
| Power | 3.3-5 V | Most modules accept 5 V |
| Antenna | External active | Place outdoors for fix |

## 3. Connection

| GPS | Board |
| --- | --- |
| VCC | 5 V or 3.3 V |
| GND | GND |
| TX | RX |
| RX | TX (optional for config) |

## 4. NMEA sentences

$GPGGA gives fix, $GPRMC gives position and time.

## 5. Sketch fragment

```cpp
#include <SoftwareSerial.h>
SoftwareSerial gps(10, 11);
void setup() { gps.begin(9600); Serial.begin(9600); }
void loop() { while (gps.available()) Serial.write(gps.read()); }
```

## 6. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No fix | Place antenna outside, wait 30-60 s |
| 2 | No data | Check baud 9600 |

## See also

- [[Home.en]]
- [[EN/04-Interfaces/01-UART.en|UART bus]]
