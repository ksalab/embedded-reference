---
description: Wireless sensors: LoRa, Zigbee, Wi-Fi sensor nodes, BLE sensors, sub-GHz, wireless temperature/humidity/motion nodes. Applications: wireless monitoring, IoT.
title: Wireless Sensors
tags: [esp32, sensor, wireless, lora, zigbee, wifi, ble, sub-ghz]
category: Sensori
lang: en
original: 10-Sensors/39-Wireless-Sensors.md
date-created: 2026-09-27
date: 2026-10-08
---

# Wireless Sensors

## Purpose

Wireless sensor nodes using ESP32 + radio: LoRa (SX1276, 868/915 MHz), Zigbee (CC2530/ESP32-ZB), Wi-Fi access points, BLE peripherals, sub-GHz. Applications: remote monitoring, wireless IoT.

## Characteristics

| Radio | Range | Power | Note |
| --- | --- | --- | --- |
| LoRa | 1-10 km | Low | SX1276 / RFM95 |
| Zigbee | 10-100 m | Low | Mesh, 2.4 GHz |
| BLE | 10-50 m | Very low | 2.4 GHz |
| Wi-Fi | 10-100 m | Medium | STA/AP |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | LoRa wrong frequency | No packet | Match region 868/915 MHz |
| 2 | Zigbee not paired | No network | Check PAN ID; power cycle |

## See also

- [[EN/05-Radio/01-WiFi-STA-AP.en]]
- [[EN/05-Radio/02-BLE-Bluetooth.en]]
