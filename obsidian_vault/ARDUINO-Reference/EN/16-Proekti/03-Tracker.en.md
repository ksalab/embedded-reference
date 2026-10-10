---
title: Tracker - GPS and Data Logger
description: Builds GPS tracker with position, speed, SD logging and display; shows schematics, code and tables.
tags: [arduino, tracker, gps, logger, sd, display]
category: Proekti
lang: en
original: 16-Projects/03-Treker.md
date-created: 2026-10-05
date: 2026-10-09
---

# Tracker - GPS and Data Logger

![[assets/img/arduino-tracker-scheme.png|600]]
*Fig. Tracker: GPS module, board, SD card, battery, display with position.*

> [!tip] Purpose
> Log position over time; show current speed and direction.

## 1. Goal

Get GPS fix; save to SD; show on display.

## 2. Components

| Component | Function |
| --- | --- |
| GPS NEO | Position |
| SD module | Storage |
| Display | LCD/OLED |

## 3. Sketch fragment

```cpp
#include <SoftwareSerial.h>
void setup() {}
void loop() {}
```

## 4. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No fix | Place antenna outside |
| 2 | No save | Check SD format |

## See also

- [[Home.en]]

## 5. Logging format

CSV: time, lat, lon, speed, status.

## 6. Battery

Use Li-ion with charger module; low voltage alarm stops logging.

## 7. Display modes

Current, history graph, alarm.

## 8. Antenna

Place GPS antenna outside; shield board from interference.
