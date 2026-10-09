---
title: SD Logger - Data Logging to Card
description: Explains SD card logger with timestamps, sensors and file format; shows schematics, code and tables.
tags: [arduino, logger, sd, data, card, storage]
category: Proekti
lang: en
original: 16-Projects/04-Loger-SD.md
date-created: 2026-10-05
date: 2026-10-09
---

# SD Logger - Data Logging to Card

![[assets/img/arduino-sd-logger-scheme.png|600]]
*Fig. Logger: board, SD module, sensors, file with time and values.*

> [!tip] Purpose
> Save sensor data over time to SD with timestamp.

## 1. Goal

Read sensors; write to file; format CSV.

## 2. Components

| Component | Function |
| --- | --- |
| SD module | Storage |
| Sensor | Data source |

## 3. Sketch fragment

```cpp
#include <SD.h>
void setup() {}
void loop() {}
```

## 4. File format

CSV with time, value, unit.

## 5. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No write | Check CS pin |
| 2 | Corrupt file | Format FAT32 |

## See also

- [[Home.en]]

## 6. File naming

Use date prefix: 2026-10-09.csv.

## 7. Storage capacity

4 GB card holds months of data at 1 minute interval.

## 8. Data export

Copy file to PC; open in spreadsheet.
