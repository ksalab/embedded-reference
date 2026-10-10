---
title: Soldering and Connectors - Techniques and Common Mistakes
description: Soldering techniques for ESP32 modules, pin headers, connectors and wires; common soldering errors and fixes; shows schematics, code and tables.
tags: [esp32, soldering, connectors, header, wire]
category: Lab
lang: en
original: ESP32-Reference/17-Lab/02-Soldering-Connectors.md
date-created: 2026-09-28
date: 2026-10-08
---

# Lab 2 - Soldering and Connectors

![](../../../../ESP32-Reference/assets/img/soldering-connectors-scheme.png)
*Fig. Soldering stages: header, wire, connector, inspection.*

## 1. Tools and Settings

| Tool | Setting | Note |
| --- | --- | --- |
| Iron | 300-320 C | Lead-free solder needs higher temp |
| Tip | Conical 1 mm | Fine work on module pins |
| Flux | No-clean | Easier cleanup |
| Solder | 0.5-0.8 mm | Not too thick |

## 2. Header Soldering

- Insert header into breadboard or PCB; solder one pin, check alignment; solder rest.
- Use solder wick to remove excess; avoid bridging adjacent pins.
- Check with multimeter for shorts between neighboring pins.

## 3. Wire Connections

- Strip 2-3 mm; twist if needed; solder to pin; cover with heat shrink.
- Use different colors: red VCC, black GND, yellow/green signal.
- Keep I2C under 30 cm; SPI under 20 cm; UART under 100 cm.

## 4. Common Mistakes

| Mistake | Cause | Fix |
| --- | --- | --- |
| Cold joint | Not enough heat | Reheat with flux |
| Bridge | Too much solder | Wick or desolder pump |
| Lifted pad | Overheating / force | Repair with wire bridge |

## See Also

- [Home](../../../../ESP32-Reference/Home.md)
- [01-Instruments](../../../../ESP32-Reference/UA/17-Lab/01-Instruments.md)
- [03-Cheklisti-montazhu](../../../../ESP32-Reference/UA/99-Dodatki/03-Cheklisti-montazhu.md)

> UA original twin: [UA](../../../../ESP32-Reference/UA/17-Lab/02-Soldering-Connectors.md)
