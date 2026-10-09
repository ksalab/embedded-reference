---
title: BT Ethernet - Bluetooth and Wired Link
description: Explains module combining Bluetooth and Ethernet for wireless and wired connection through UART and SPI; shows schematics, code and tables.
tags: [arduino, bt, bluetooth, ethernet, uart, spi]
category: Zvyazok
lang: en
original: 12-Comm-Modules/05-BT-Ethernet.md
date-created: 2026-10-05
date: 2026-10-09
---

# BT Ethernet - Bluetooth and Wired Link

![[assets/img/arduino-bt-ethernet-scheme.png|600]]
*Fig. Dual module: Bluetooth for wireless, Ethernet for wired, UART to board.*

> [!tip] Purpose of this note
> Connect to devices by wireless or wire: set module through UART, choose protocol.

## 1. Purpose

Module provides both interfaces; useful for flexible systems.

## 2. Characteristics

| Interface | Protocol | Use |
| --- | --- | --- |
| Bluetooth | Serial profile | Phone, PC link |
| Ethernet | TCP/IP | Network, server |

## 3. Connection

UART to module; module to network or phone.

## 4. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No BT pair | Check pairing mode |
| 2 | No Ethernet | Check cables and IP |

## See also

- [[Home.en]]

## 5. Bluetooth pairing

Use default PIN 1234 or 0000; pair from phone settings.

## 6. Ethernet IP

Set static IP: 192.168.1.100; gateway 192.168.1.1.

## 7. Protocol selection

Bluetooth serial for short range; Ethernet TCP for network.

## 8. Security

Use passwords for Bluetooth; firewall rules for Ethernet.
