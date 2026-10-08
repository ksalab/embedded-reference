---
title: ESP32 DevKit boards - choice and power
description: Guide to ESP32 DevKit boards covering USB-UART bridges, BOOT/EN buttons, clones and power wiring; shows schematics, code and tables.
tags:

  - esp32
  - esp32/start
  - esp32/hardware
  - esp32/devkit
  - esp32/power

aliases:

  - DevKit boards
  - DOIT WROOM WROVER
  - Devkit boards EN

type: guide
lang: en
original: 00-Start/04-Devkit-plati.md
date-created: 2026-10-08
date: 2026-10-08
---

# DevKit boards - choice and power

> [!tip] What to buy in 2026
> First board - **ESP32-DevKitC V4 / DOIT V1 (WROOM-32)** for compatibility. Second - **ESP32-S3-DevKitC-1** for camera/displays. Third - **C3 SuperMini** for tiny sensors. Crystal comparison - [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md), terms - [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md), flashing - [Environment choice](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md).
>
> [!warning] 5V on VIN/USB only!
> On a DevKit the `5V/VIN` pin is a power input. All GPIO, TX/RX, SDA/SCL are **3.3V**. Wiring a 5V sensor signal into GPIO kills the pin or the chip. Use the [level-matching template](../../../ESP32-Reference/_templates/Component-Template.md).

## Popular boards overview

| Board | Module / chip | USB-UART | USB port | PSRAM | Notes |
| --- | --- | --- | --- | --- | --- |
| DOIT DevKit V1 | WROOM-32 (Classic) | CP2102 | Micro-USB | No | 30 pins, wide, example baseline |
| DevKitC V4 | WROOM-32E | CP2102N | Micro-USB | No | Narrow, quality LDO |
| WROVER-Kit | WROVER-B | FTDI | Micro-USB | 8 MB | LCD + camera, pricey |
| ESP32-S3-DevKitC-1 | S3-WROOM-1 | CP2102N + native | 2x USB-C | 8 MB Octal | BOOT/RESET buttons, RGB |
| ESP32-C3 SuperMini | C3FN4 | Native CDC | USB-C | No | 22x18 mm, 4 mA deep-sleep |
| Generic C3 DevKitM | C3-MINI-1 | Native CDC | Micro-USB | No | Cheap, weaker LDO |

Reference map - [Home map](../../../ESP32-Reference/Home.md), how to search - [How to use it](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md).

## Power and USB-UART

| Part | CP2102/CP2102N | CH340C/G | Native USB (S3/C3) |
| --- | --- | --- | --- |
| Driver | Needed (SiLabs) | Needed (WCH) | Not needed (CDC) |
| Stability | High | Medium, clones | High |
| Flash speed | 921600 baud | 460800 baud | 921600 baud |
| 3.3V output | 100 mA max | Weak | - |

> [!tip] Project power
> USB gives 500 mA. The AMS1117 LDO on DOIT already runs hot at 400 mA. For relays/servos/motors use a separate 5V 2A unit with common GND. A 470-1000 µF electrolytic cap on VIN+GND removes brownout on Wi-Fi peaks (up to 500 mA).
>
> [!warning] Clones
> Clone signs: CH340 instead of the claimed CP2102, WROOM print without the Espressif logo, AMS1117 without marking, floating MAC, unstable flashing at 921600. Fix by dropping speed to 115200 and using a quality cable (data, not charge-only).

## BOOT/EN buttons

| Action | BOOT (GPIO0) | EN | Result |
| --- | --- | --- | --- |
| Run | Released | Press and release | Reset |
| Download mode by hand | Hold | Press and release, then release BOOT | `waiting for download` |
| Auto-flash | DTR/RTS circuit | DTR/RTS circuit | esptool enters the mode itself |

If auto-reset fails (cheap boards), enter the mode by hand using the table above.

## How to spot a clone

| Sign | Genuine | Clone |
| --- | --- | --- |
| Silkscreen | Sharp, `ESP32 DEVKITV1` | Blurry, errors |
| Module shield | Laser engraving, FCC | Sticker, no logo |
| LDO | AMS1117-3.3 with marking | No marking, runs hot |
| USB-UART | CP2102 with crystal | CH340 without crystal, CP2102 print |
| Capacitors | Tantalum near antenna | Ceramic, less capacitance |

## Typical power wiring

> [!example] Photo/schematic: ![](../../../ESP32-Reference/assets/img/devkit-boards-compare.png)
> Baseline: DevKit power from USB + external 5V sensor:

| ESP32 DevKit | External module | Note |
| --- | --- | --- |
| 5V (VIN) | 5V relay VCC / HC-SR04 VCC | Power for 5V modules |
| 3V3 | 3.3V I2C sensor VCC | Up to 400 mA total |
| GND | GND of all modules | Common ground is mandatory |
| GPIO (3.3V) | SDA/SCL, RX/TX via level-shifter if the module is 5V | Never 5V direct! |
| EN / GPIO0 | Buttons on board | For download mode |

## See also

- [Home map](../../../ESP32-Reference/Home.md)
- [How to use it](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md)
- [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md)
- [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md)
- [Environment choice](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md)
- [Component template](../../../ESP32-Reference/_templates/Component-Template.md)
- [DOIT DevKitV1 / NodeMCU-32S](../../../ESP32-Reference/14-Devboards/01-DOIT-DevKitV1-NodeMCU32S.md)
- [02-Wemos-D1-R32](../../../ESP32-Reference/14-Devboards/02-Wemos-D1-R32.md)
- [LILYGO T-Display / T-Beam](../../../ESP32-Reference/14-Devboards/03-LILYGO-TDisplay-TBeam.md)
- [04-Heltec-WiFi-LoRa32](../../../ESP32-Reference/14-Devboards/04-Heltec-WiFi-LoRa32.md)
- [ESP32-CAM](../../../ESP32-Reference/14-Devboards/05-ESP32-CAM.md)
- [M5Stack Core / Stick](../../../ESP32-Reference/14-Devboards/06-M5Stack-Core-Stick.md)
- [Feather HUZZAH32 / Thing](../../../ESP32-Reference/14-Devboards/07-Feather-Huzzah32-Thing.md)
- [S3-DevKitC / C3-SuperMini / XIAO](../../../ESP32-Reference/14-Devboards/08-S3-DevKitC-C3-SuperMini-XIAO.md)
- [WT32-ETH01 / Olimex](../../../ESP32-Reference/14-Devboards/09-WT32-ETH01-Olimex.md)
