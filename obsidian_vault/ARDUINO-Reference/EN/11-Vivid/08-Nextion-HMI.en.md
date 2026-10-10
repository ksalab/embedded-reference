---
title: Arduino Nextion HMI - Smart Display with Editor
description: Builds interface on Nextion display - editor, pages and components, UART protocol and link with Arduino; shows schematics, code and tables.
tags: [arduino, nextion, hmi, display, uart, touchscreen, editor]
category: Vivid
lang: en
original: 11-Vivid/08-Nextion-HMI.md
date-created: 2026-10-06
date: 2026-10-09
---

# Arduino Nextion HMI - Smart Display with Editor

![[assets/img/ard-nextion-hmi-scheme.png|600]]
*Fig. Smart display: interface lives in Nextion, Arduino sends data and catches presses - UART bridge.*

> [!tip] What this note is about
> Display-computer: draw interface with mouse in editor, Arduino only supplies data. Opposite of TFT where controller draws. Base: [[EN/11-Vivid/07-TFT-Touch-Deep.en|TFT with touch deep]], [[EN/04-Interfaces/01-UART.en|UART bus]].

## 1. Goal

Give interface to display:

- Nextion editor: pages, buttons, graphics, keyboards;
- Protocol: text commands to it, events back;
- Link with Arduino: data up, presses down;
- SD card on display: interface firmware.

## 2. Editor and pages

Pages are screens; components have IDs; commands set text and colors.

## 3. UART protocol

Arduino sends commands like `t0.txt="Hello"`; display sends touch events as `65 01 01 FF FF 01`.

## 4. Sketch fragment

```cpp
#include <SoftwareSerial.h>
SoftwareSerial nextSerial(10, 11);
void setup() { nextSerial.begin(9600); nextSerial.print("t0.txt=\"Hello\""); }
void loop() {}
```

## 5. Connection

UART at 9600; common ground; data to RX, from TX.

## 6. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No response | Check baud and wiring |
| 2 | Wrong IDs | Match editor IDs |

## See also

- [[Home.en]]
- [[EN/11-Vivid/07-TFT-Touch-Deep.en|TFT with touch deep]]
