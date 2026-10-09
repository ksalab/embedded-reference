---
title: Arduino TFT with Touch Deep - ILI9341, Calibration and Menu
description: Builds a graphical interface on Arduino - TFT ILI9341 with touch XPT2046, calibration, menu and memory optimization; shows schematics, code and tables.
tags: [arduino, tft, ili9341, touch, xpt2046, display, gui, menu, spi]
category: Vivid
lang: en
original: 11-Vivid/07-TFT-Touch-Deep.md
date-created: 2026-10-06
date: 2026-10-09
---

# Arduino TFT with Touch Deep - ILI9341, Calibration and Menu

![[assets/img/ard-tft-touch-deep-scheme.png|600]]
*Fig. TFT screen: display over SPI, touch with separate CS, menu as states, fonts in PROGMEM.*

> [!tip] What this note is about
> Deep TFT theme: not just output text, but menu with buttons, calibrated touch and life in 2 KB SRAM. Base: [[EN/11-Vivid/04-TFT-ST7735.en|TFT ST7735]], [[EN/04-Interfaces/02-SPI.en|Fast bus]].

## 1. Goal

Build a device with screen:

- ILI9341 320x240: init and speeds;
- Touch XPT2046: calibration with matrix;
- Auto menu: screens, buttons, return;
- Memory: frame buffer does not fit - draw in parts.

## 2. ILI9341 and touch

| Module | Resolution | Touch chip | Interface |
| --- | --- | --- | --- |
| ILI9341 | 320x240 | XPT2046 | SPI |

Calibration uses 4-point or 5-point matrix; store constants in EEPROM.

## 3. Library and init

Use Adafruit ILI9341 and Adafruit GFX; touch library XPT2046_TouchScreen.

## 4. Menu states

| State | Screen | Buttons |
| --- | --- | --- |
| Main | Title and options | Select |
| Settings | Sliders and values | Back |
| Info | Text and values | Back |

Draw only changed areas; full redraw is slow.

## 5. Memory optimization

Fonts stored in PROGMEM; buffers small; avoid large arrays.

## 6. Sketch fragment

```cpp
#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <XPT2046_Touchscreen.h>
// Init and draw menu
void setup() {}
void loop() {}
```

## 7. Calibration

Measure min/max X and Y; compute scale; save to EEPROM.

## 8. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | Touch inaccurate | Recalibrate |
| 2 | Menu slow | Draw partial |

## See also

- [[Home.en]]
- [[EN/11-Vivid/04-TFT-ST7735.en|TFT ST7735]]
