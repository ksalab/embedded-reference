---
description: RCWL-0516 microwave motion, reed switch, vibration SW-420, tilt sensor, water flow YF-S201: digital and analog outputs, interrupt-friendly, low power. Applications: presence, door, vibration alarm, tilt, flow.
title: RCWL-0516, Reed, Vibration, Tilt, Flow
tags: [esp32, sensor, rcwl, reed, vibration, tilt, flow, motion]
category: Sensori
lang: en
original: 10-Sensors/13-RCWL0516-Reed-Vibration-Tilt-Flow.md
date-created: 2026-09-27
date: 2026-10-08
---

# RCWL-0516, Reed, Vibration, Tilt, Flow

## Purpose

Low-power presence and event sensors: RCWL-0516 (microwave Doppler 3.2 GHz, digital DO), reed switch (magnetic contact, digital), vibration SW-420 (digital + analog from LM393), tilt ball switch / digital, water flow YF-S201 (Hall pulse per rotation). All use digital outputs for interrupts and analog for level. Applications: room presence, door open/close, vibration alarm, tilt detection, water flow measurement.

> RCWL-0516 can trigger false positives near moving metal or moisture; set sensitivity via potentiometer and use software debounce.

## Characteristics

| Sensor | Type | Output | Range / Notes |
| --- | --- | --- | --- |
| RCWL-0516 | Microwave Doppler | DO LOW = motion | ~3-7 m, 120° cone, 3.2 GHz |
| Reed | Magnetic contact | DO LOW = open | 2-20 mm gap, 0.5 A max |
| Vibration SW-420 | Spring / piezo + LM393 | DO + AO | Sensitivity via pot |
| Tilt | Ball / mercury | DO LOW = tilt | Digital only |
| Flow YF-S201 | Hall pulse | Pulse / AO | 1-30 L/min, 450 pulses/L |

## Module pin legend

| Pin | Function | Note |
| --- | --- | --- |
| VCC | Power | 3.3-5 V; RCWL 5 V better |
| GND | Ground | Common |
| DO | Digital output | LOW = event; pull-up if open-drain |
| AO | Analog output | For vibration / flow level |

## Wiring diagram

| ESP32 | Sensor | Note |
| --- | --- | --- |
| 3V3 | VCC | 3.3 V for digital sensors |
| GND | GND | Star ground |
| GPIO25 | RCWL DO | Interrupt |
| GPIO26 | Reed DO | Interrupt |
| GPIO27 | Vibration DO | Interrupt + AO on GPIO35 |
| GPIO14 | Tilt DO | Interrupt |
| GPIO13 | Flow signal | Pulse input |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | RCWL too sensitive / near metal | False motion | Reduce pot; add software filter 2-3 s |
| 2 | Reed without pull-up | Unreliable open | Internal pull-up or 10k to 3V3 |
| 3 | Vibration AO noisy | Random values | Average 10-20 samples; set threshold |
| 4 | Flow without pulse counter | No flow reading | Count pulses with interrupt; 450 pulses/L |

## Official sources

- RCWL-0516 Datasheet (manufacturer) - `check manually`.
- SW-420 Datasheet (van der?) - `check manually`.
- YF-S201 Datasheet - `check manually`.

## See also

- [[EN/03-GPIO/01-GPIO-Overview.en]]
- [[EN/10-Sensors/01-DHT11-DHT22.en]]
