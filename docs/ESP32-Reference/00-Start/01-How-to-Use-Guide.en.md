---
title: How to use the ESP32-Reference guide
description: Guide to the ESP32 reference layout covering folders, tags, search, schematic symbols and difficulty levels; shows schematics, code and tables.
tags:

  - esp32
  - esp32/start
  - esp32/guide

aliases:

  - How-to-use-guide
  - How to use the reference

type: guide
lang: en
original: 00-Start/01-Yak-koristuvatis-dovidnikom.md
date-created: 2026-10-08
date: 2026-10-08
---

# How to use the reference

> [!tip] 30-second finder
> Any answer can be found in 30 seconds: `Ctrl+P` for files, `Ctrl+Shift+F` for text, click a `#esp32/*` tag or hop from [Home map](../../../ESP32-Reference/Home.md).

The reference follows the MOC principle: [Home map](../../../ESP32-Reference/Home.md) links everything. Deep theory lives in the [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md), hardware choice in [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) and [DevKit boards](../../../ESP32-Reference/00-Start/04-Devkit-plati.md), SDK choice in [Environment choice](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md), new sensors follow the [Component template](../../../ESP32-Reference/_templates/Component-Template.md).

> [!warning] Core power setup
> The whole reference assumes ESP32 logic is **3.3V**. Examples from 5V Arduino boards (Uno/Nano) do not transfer literally: dividers and level-shifters are mandatory. Feeding 5V into any GPIO causes irreversible damage.

## Folder structure

| Folder | Contents | Example |
| --- | --- | --- |
| `00-Start/` | Entry, glossary, choice | This note, [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md), [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| `01-Hardware/` | Chips and differences | [C3/C6/H2 chips](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md), [C5/C61](../../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md) |
| `02-Zhivlennya/` | Power, batteries | [Batteries](../../../ESP32-Reference/02-Zhivlennya/04-Akumulyatori-TP4056.md), [Power consumption](../../../ESP32-Reference/02-Zhivlennya/03-Spozhivannya.md) |
| `03-GPIO/` | Pins, strapping | [GPIO overview](../../../ESP32-Reference/03-GPIO/01-GPIO-oglyad.md), [Strapping](../../../ESP32-Reference/03-GPIO/02-Strapping-pini.md) |
| `04-Shini/` | UART, SPI, I2C | [UART](../../../ESP32-Reference/04-Shini/01-UART.md), [I2C](../../../ESP32-Reference/04-Shini/03-I2C.md) |
| `05-Radio/` | WiFi STA/AP, BLE | [WiFi STA/AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md), [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| `06-Analog/` | ADC, DAC | [ADC](../../../ESP32-Reference/06-Analog/01-ADC.md) |
| `09-Proshivka/` | Toolchains, esptool | [Esptool-Flash](../../../ESP32-Reference/09-Proshivka/04-Esptool-Flash.md) |
| `10-Sensori/` | Sensors by template | [DHT11/DHT22](../../../ESP32-Reference/10-Sensori/01-DHT11-DHT22.md) |
| `99-Dodatki/` | FAQ, versions | [FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md), [Versions](../../../ESP32-Reference/99-Dodatki/07-Versions.md) |
| `_templates/` | Note templates | [Component-Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| `assets/img/` | Schematics, photos | `placeholder.png` |

## Tags

| Tag | When to use it |
| --- | --- |
| `#esp32/gpio` | Pins, strapping, interrupts |
| `#esp32/adc` | ADC, calibration, dividers |
| `#esp32/i2c`, `#esp32/spi`, `#esp32/uart` | Buses |
| `#esp32/wifi`, `#esp32/ble` | Radio |
| `#esp32/ota`, `#esp32/nvs` | Firmware and memory |
| `#esp32/power` | Power, sleep, LDO |
| `#esp32/sensor` | Sensors |
| `#esp32/beginner`, `#esp32/advanced` | Difficulty level |

## Search and Dataview

Obsidian search:

- `tag:#esp32/adc` - all notes about the ADC
- `path:01-Hardware UART` - UART in hardware
- `"level-shifter"` - where level matching is mentioned

> [!example] Dataview query: all I2C sensors
>
> ```dataview
> TABLE tags, type
> FROM "ESP32-Reference"
> WHERE contains(tags, "esp32/sensor")
> SORT file.name ASC
> ```
>
> [!example] Dataview query: chip table
>
> ```dataview
> TABLE cores, wifi
> FROM "ESP32-Reference/00-Start"
> WHERE type = "reference"
> ```

## Schematic symbols

| Symbol | Meaning |
| --- | --- |
| `3V3` | 3.3V from the board LDO, about 500 mA max |
| `5V / VIN` | 5V from USB, module power only |
| `GND` | Common ground, always connect |
| `→ TXS / ⇅` | Needs a level-shifter |
| `⚠ 5V!` | 5V line, do not connect to GPIO |
| `4k7 ↑3V3` | 4.7k pull-up to 3.3V |

## Difficulty levels

| Level | Labels | Example |
| --- | --- | --- |
| 🟢 Beginner | `#esp32/beginner` | Blinking an LED, [connecting a DevKit over USB](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| 🟡 Intermediate | - | I2C sensor, [PlatformIO](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md), Wi-Fi STA |
| 🔴 Advanced | `#esp32/advanced` | OTA, ULP, TWAI, eFuse |

> [!tip] Suggested path
>
> 1. [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md) - 10 min on terms. 2. [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) - picking silicon. 3. [DevKit boards](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) - which board to buy. 4. [Environment choice](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) - ESP-IDF or Arduino. 5. [Home map](../../../ESP32-Reference/Home.md) - back to the map.
>
> [!example] Photo/schematic: ![](../../../ESP32-Reference/assets/img/placeholder.png)
> Reference wiring for all guide examples:

| ESP32 DevKit | Module / PC | Note |
| --- | --- | --- |
| 3V3 | 3.3V sensor VCC | Up to 500 mA |
| GND | GND | Common ground |
| GPIO21 / GPIO22 | I2C SDA / SCL | 4.7k pull-ups to 3V3 |
| GPIO1 / GPIO3 | USB-UART RX / TX | 3.3V, no 5V! |

## See also

- [Home map](../../../ESP32-Reference/Home.md)
- [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md)
- [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md)
- [DevKit boards](../../../ESP32-Reference/00-Start/04-Devkit-plati.md)
- [Environment choice](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md)
- [Component template](../../../ESP32-Reference/_templates/Component-Template.md)
