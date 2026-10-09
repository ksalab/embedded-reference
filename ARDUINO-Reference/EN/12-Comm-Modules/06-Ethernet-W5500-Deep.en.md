---
title: Ethernet W5500 Deep - TCP/IP Stack over SPI
description: Explains W5500 Ethernet module with TCP/IP stack through SPI, IP setup, sockets and libraries; shows schematics, code and tables.
tags: [arduino, ethernet, w5500, tcp, spi, network]
category: Zvyazok
lang: en
original: 12-Comm-Modules/06-Ethernet-W5500-Deep.md
date-created: 2026-10-05
date: 2026-10-09
---

# Ethernet W5500 Deep - TCP/IP Stack over SPI

![[assets/img/arduino-ethernet-w5500-scheme.png|600]]
*Fig. W5500 module with SPI to board, RJ45 connector, IP setup, TCP sockets.*

> [!tip] Purpose of this note
> Add network to Arduino: connect W5500 on SPI, set IP, open socket, send data.

## 1. Purpose

W5500 is an Ethernet chip with TCP/IP stack; library handles sockets.

Used for servers, clients, remote control.

## 2. Module characteristics

| Parameter | Value | Note |
| --- | --- | --- |
| Chip | W5500 | Hardware TCP/IP |
| Interface | SPI | CS, MOSI, MISO, SCK |
| Power | 3.3 V | Module often has 3.3 V reg or needs it |
| Connector | RJ45 | Standard Ethernet |

## 3. Connection

| W5500 | Board |
| --- | --- |
| VCC | 3.3 V or 5 V if module accepts |
| GND | GND |
| MOSI | MOSI |
| MISO | MISO |
| SCK | SCK |
| CS | Any digital |
| INT | Any digital (optional) |

## 4. Library Ethernet3 or W5500

```cpp
#include <SPI.h>
#include <Ethernet3.h>
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
void setup() { Ethernet.begin(mac); }
void loop() {}
```

## 5. IP setup

Can use DHCP or static; static needs gateway and subnet.

## 6. Socket example

```cpp
EthernetServer server(80);
void setup() { server.begin(); }
void loop() { EthernetClient client = server.available(); if (client) { client.println("HTTP/1.1 200 OK"); client.println(); } }
```

## 7. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No connection | Check cable, IP, gateway |
| 2 | SPI error | Verify CS |
| 3 | No data | Check library and pins |

## See also

- [[Home.en]]
- [[EN/04-Interfaces/02-SPI.en|Fast bus]]

## 8. TCP client mode

Connect to remote server; send HTTP requests.

## 9. Performance

W5500 handles up to 4 sockets; divide connections.

## 10. Power

Use 3.3 V; module often includes regulator.

## 11. Enclosure

Protect RJ45 from moisture; mount near router.
