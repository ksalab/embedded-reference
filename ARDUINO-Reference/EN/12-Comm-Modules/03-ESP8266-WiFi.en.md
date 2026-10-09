---
title: ESP8266 WiFi Module - Serial AT Commands
description: Explains ESP8266 WiFi module for wireless connection through UART with AT commands, power, baud and libraries; shows schematics, code and tables.
tags: [arduino, esp8266, wifi, uart, at, module]
category: Zvyazok
lang: en
original: 12-Comm-Modules/03-ESP8266-WiFi.md
date-created: 2026-10-05
date: 2026-10-09
---

# ESP8266 WiFi Module - Serial AT Commands

![[assets/img/arduino-esp8266-scheme.png|600]]
*Fig. ESP8266 module on board, UART link, 3.3 V power, WiFi antenna, AT commands.*

> [!tip] Purpose of this note
> Add WiFi to Arduino through ESP8266 module: connect UART, set baud, send AT commands, connect to network.

## 1. Purpose

ESP8266 is a WiFi chip with UART interface; AT commands control it.

Used for IoT, remote control, data upload.

## 2. Module characteristics

| Parameter | Value | Note |
| --- | --- | --- |
| Chip | ESP8266 | 2.4 GHz WiFi |
| Interface | UART | TX/RX |
| Power | 3.3 V | 5 V through level shifter if needed |
| Baud | 115200 default | Can change |

## 3. Connection

| ESP8266 | Board |
| --- | --- |
| VCC | 3.3 V |
| GND | GND |
| TX | RX (with divider if 5 V) |
| RX | TX (with divider if 5 V) |

Use voltage divider on RX from board to module to protect 3.3 V input.

## 4. AT commands

| Command | Function |
| --- | --- |
| AT | Check |
| AT+CWMODE=1 | Station mode |
| AT+CWJAP="SSID","PASS" | Connect to AP |
| AT+CIFSR | Get IP |

## 5. Sketch fragment

```cpp
#include <SoftwareSerial.h>
SoftwareSerial esp(10, 11);
void setup() { esp.begin(115200); esp.println("AT"); }
void loop() {}
```

## 6. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No response | Check baud, power 3.3 V |
| 2 | No WiFi | Check SSID and password |
| 3 | Garbage | Match baud rate |

## See also

- [[Home.en]]
- [[EN/04-Interfaces/01-UART.en|UART bus]]
