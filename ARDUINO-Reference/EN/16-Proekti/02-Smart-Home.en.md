---
title: Smart Home - Automation and Sensors
description: Explains smart home with auto controls, sensors, relays and communication; shows schematics, code and tables.
tags: [arduino, smart, home, automation, relay, sensor]
category: Proekti
lang: en
original: 16-Projects/02-Rozumniy-dim.md
date-created: 2026-10-05
date: 2026-10-09
---

# Smart Home - Automation and Sensors

![[assets/img/arduino-smart-home-scheme.png|600]]
*Fig. Smart home: sensors, board, relays, network link, display.*

> [!tip] Purpose
> Build automation: temperature control, lighting, security with remote access.

## 1. Goal

Control devices from board; read environment; send alerts.

## 2. Components

| Component | Function | Interface |
| --- | --- | --- |
| DHT | Temperature | Digital |
| Relay | Load switch | Digital |
| WiFi | Remote | UART/ESP |

## 3. Sketch fragment

```cpp
void setup() {}
void loop() {}
```

## 4. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | Relay not switching | Check power |
| 2 | No remote | Check WiFi settings |

## See also

- [[Home.en]]

## 5. Sensor tables

| Sensor | Function | Interface |
| --- | --- | --- |
| DHT22 | Temperature, humidity | Digital |
| LDR | Light | Analog |
| PIR | Motion | Digital |

## 6. Automation logic

If temperature > 25 C, turn on fan; if light low, turn on LED.

## 7. Power

Use 5 V supply; relays take separate 5-12 V if needed.

## 8. Security

Door sensor triggers alarm; send notification through WiFi.
