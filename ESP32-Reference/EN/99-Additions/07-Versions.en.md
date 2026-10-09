---
title: ESP32 Versions and Revisions
description: ESP32 versions, revisions, modules and boards with key differences (classic / S3 / C3 / C6 / H2); migration notes; shows schematics, code and tables.
tags: [esp32, versions, revision, module, board]
category: Meta
lang: en
original: ESP32-Reference/99-Additions/07-Versions.md
date-created: 2026-09-27
date: 2026-10-08
---

# ESP32 Versions and Revisions

> Quick reference: classic ESP32 (D0WD / D2WD), ESP32-S3 (Xtensa LX7), ESP32-C3 (RISC-V), ESP32-C6 / H2 (RISC-V + 802.15.4). Migration notes below.

## Core Differences

| Feature | ESP32 Classic | ESP32-S3 | ESP32-C3 | ESP32-C6 / H2 |
| --- | --- | --- | --- | --- |
| Core | Xtensa LX6 dual | Xtensa LX7 dual | RISC-V 32-bit | RISC-V 32-bit |
| WiFi | 4 + BLE 4.2 | 4 + BLE 5 + USB-OTG | 4 + BLE 5 | 6 + 802.15.4 (C6); none WiFi (H2) |
| ADC | 2 channels (ADC1/ADC2) | 2 (ADC1/ADC2) | 1 (ADC1, 6 ch) | 1-2 |
| DAC | 2 (GPIO25/26) | None | None | None |
| Flash | External SPI | Octal PSRAM optional | SPI | SPI |
| Power | 5V -> LDO 3.3V 500 mA | 5V -> LDO 3.3V 500 mA | 5V -> LDO 500 mA | 5V -> LDO |
| Strapping | GPIO0/2/5/12/15 | GPIO0/45/46/8/9 | GPIO2/8/9 | GPIO8/9/25 |

## Module Versions

| Module | Chip | Flash / PSRAM | UART / USB | Use |
| --- | --- | --- | --- | --- |
| ESP32-WROOM-32 | D0WD / D2WD | 4 MB / none | UART bridge | Classic boards |
| ESP32-S3-WROOM-1 | S3 | 8 MB / none | USB-OTG native | Camera / display |
| ESP32-S3-WROOM-1-N8R8 | S3 | 8 MB / 8 MB PSRAM | USB-OTG native | Camera + RAM |
| ESP32-C3-WROOM-02 | C3 | 4 MB / none | USB-Serial-JTAG | Battery / small |
| ESP32-C6-WROOM-1 | C6 | 4 MB / none | USB-OTG native | Thread / Zigbee |

## Migration Notes

- From classic to S3: change strapping pins, ADC2 unavailable with WiFi, no DAC, use ULP or ESP-IDF sleep instead.
- From S3 to C3: RISC-V, different ABI, smaller flash, no USB-OTG native on some modules, use UART bridge.
- From C3 to C6: add 802.15.4 (Thread), no WiFi on H2, check strapping different.

## See Also

- [[EN/Home.en]]
- [[EN/01-Hardware/01-ESP32-Classic.en]]
- [[01-Hardware/04-ESP32-C3-C6-H2]]

> UA original twin: [[99-Additions/07-Versions.md | UA]]
