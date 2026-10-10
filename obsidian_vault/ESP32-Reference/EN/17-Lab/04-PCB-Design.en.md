---
title: PCB Design - Schematic, Layout, Ground, Power and Manufacturing
description: Full PCB design guide for ESP32 from schematic to Gerber: ground planes, power routing, antenna clearance, manufacturing notes; shows schematics, code and tables.
tags: [esp32, pcb, design, schematic, layout, gerber]
category: Lab
lang: en
original: ESP32-Reference/17-Lab/04-PCB-Design.md
date-created: 2026-09-28
date: 2026-10-08
---

# Lab 4 - PCB Design

![[assets/img/pcb-design-ground-scheme.png|600]]
*Fig. Ground and power routing for ESP32 PCB.*

## 1. Schematic Basics

- Use ESP32 symbol with all pins labeled.
- Add pull-ups (10k), decoupling caps (100 nF per pin, 10 µF bulk).
- Include USB-UART bridge (CH340/CP2102) or native USB if S3.

## 2. Layout Rules

| Rule | Value | Reason |
| --- | --- | --- |
| Trace width power | 0.3 mm / 1 mm for 5V | Current capacity |
| Ground plane | Continuous | Low impedance |
| Antenna keep-out | 15 mm from metal | RF performance |
| Crystal near chip | <5 mm | Clock stability |

## 3. Ground Planes

- Use single-point ground near LDO; avoid ground loops.
- Star ground for analog and digital sections.

## 4. Power Routing

- Route 5V and 3.3V separately; use wide traces.
- Place bulk cap 47 µF near module; 100 nF near each pin.
- LDO thermal: add copper pour for heat sinking.

## 5. Manufacturing Notes

- Use 2-layer for simple boards; 4-layer for complex RF.
- Order from JLCPCB / PCBWay; check DRU for 5/5 rules.
- Include test points for power and UART.

## See Also

- [[EN/Home.en]]
- [[01-Hardware/05-Moduli-WROOM-WROVER-MINI]]
- [[EN/99-Additions/03-Cheklisti-montazhu.en]]

> UA original twin: [[17-Lab/04-PCB-Design.md | UA]]
