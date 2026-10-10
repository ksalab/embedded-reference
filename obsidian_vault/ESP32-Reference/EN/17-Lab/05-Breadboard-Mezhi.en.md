---
title: ESP32 Breadboard - Build Without Soldering and Its Limits
description: Full guide to ESP32 on breadboard from strapping pins and USB-UART to WiFi sags and transition to soldered board.
tags: [esp32, breadboard, strapping, usb-uart, wifi-noise]
category: Lab
lang: en
original: ESP32-Reference/17-Lab/05-Breadboard-Mezhi.md
date-created: 2026-10-05
date: 2026-10-08
---

# ESP32 Breadboard - Build Without Soldering and Its Limits

![[assets/img/breadboard-limits-scheme.png|600]]
*Fig. Breadboard as first project hour: what you can do, where the walls are.*

> [!tip] Purpose
> Give full breadboard map for ESP32: power, strapping pins, USB-UART bridges, bus limits and radio - so glitches come from code, not wires.

## 1. Purpose

ESP32 lives better on breadboard than most chips: DevKit already has USB-UART bridge, regulator and BOOT/EN buttons. Plug into breadboard - first sketch in a minute. But WiFi peaks eat half an amp, strapping pins decide boot fate, and every wire is an antenna. This note breaks down all layers: from power rails to the moment when breadboard should be thrown away.

## 2. Breadboard Power Rails: Red and Blue

| Rule | Explanation |
| --- | --- |
| Power strips at edges | Plus and ground along full board length |
| Break in middle | Most breadboards break strips in center - check! |
| Jumpers across break | Jumpers edge-to-edge if power must continue |
| Bulk near module | 10-47 µF electrolytic + 100 nF ceramic in adjacent holes |
| Thick power wires | Thin Dupont sags at WiFi TX peaks |

```text
Check before first power-on:
  1. Continuity of 5V and GND strips edge-to-edge;
  2. Find center break BEFORE debugging hour;
  3. Measure 3.3V at module pins under load.
```

## 3. ESP32 Power: WiFi Peaks Kill Weak PSUs

| Source | Current | Conclusion |
| --- | --- | --- |
| PC USB port | 500 mA by standard | Enough, but tight with peripherals |
| 1 A charger | Really enough | Minimum for CAM and displays |
| 2 A+ charger | Reserve for everything | Get one immediately |
| LDO on DevKit | AMS1117 gets hot | Over half amp - hot! |

| Symptom | Cause | Fix |
| --- | --- | --- |
| Brownout when WiFi connects | TX peak sags line | Short thick wires, bulk 47 µF |
| Reboot on ESP32-CAM at photo | PSRAM + camera together | PSU 5V 2A, bulk near board |
| Works from USB, silent from battery | Battery internal resistance | Fresh battery, short wires |

## 4. Strapping Pins: Do Not Touch at Boot

| Pin | Role at boot | What NOT to do on breadboard |
| --- | --- | --- |
| GPIO0 | BOOT mode | Do not pull down constantly - button only! |
| GPIO2 | Level + strapping | Do not hang peripheral that pulls down |
| GPIO12 | Flash voltage (MTDI) | Critical: low = flash problems! |

## 5. USB-UART Bridge and Auto-Reset

- DevKit includes CH340/CP2102 with DTR/RTS to EN/BOOT.
- On breadboard: keep bridge module separate; do not mix USB-UART ground with breadboard ground unless star ground.
- Auto-reset needs 100 nF cap EN-GND for clean reset.

## 6. Signal Quality and Noise

- Keep SPI/I2C <30 cm; UART can be longer with twisted pair.
- Use 10k pull-ups on I2C; 10k CS pull-up on SPI.
- WiFi antenna: keep away from breadboard metal rails and USB cables.
- If ADC noisy: average 32-64 samples; 100 nF cap on analog input.

## 7. When to Move to Soldered Board

- More than 15 wires; power sag >0.2V; dry joints; intermittent I2C.
- Replace breadboard with custom PCB or perfboard when design is frozen.

## See Also

- [[EN/Home.en]]
- [[EN/17-Lab/01-Instruments.en]]
- [[03-GPIO/01-GPIO-oglyad]]

> UA original twin: [[17-Lab/05-Breadboard-Mezhi.md | UA]]
