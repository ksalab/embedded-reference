---
title: Consolidated Pinout Tables
description: Pinout tables: DevKit V1 / S3 DevKitC / C3 SuperMini: ADC/CAN/DAC; shows schematics, code and tables.
tags: [esp32, pinout, devkit, s3, c3, gpio, strapping]
category: Meta
lang: en
original: ESP32-Reference/99-Additions/01-Pinout-tablici.md
date-created: 2026-09-27
date: 2026-10-08
---

# Pinout Tables: DevKit V1 / S3 DevKitC / C3 SuperMini

![[assets/img/esp32-classic-pinout.png|600]]

![[assets/img/esp32-s3-pinout.png|600]]

![[assets/img/esp32-c3-supermini-pinout.png|600]]

GPIO base: [[03-GPIO/01-GPIO-oglyad]], buses [[04-Interfaces/02-SPI|SPI]] [[04-Interfaces/03-I2C|I2C]] [[04-Interfaces/01-UART|UART]], sleep [[07-Timers/03-Sleep-ULP]], analog [[06-Analog/01-ADC|ADC]], start [[EN/Home.en]], repair [[EN/99-Additions/02-Troubleshooting-FAQ.en]].

## 1. ESP32 DevKit V1 (classic D0WD, 30 pins)

| GPIO | ADC | Touch | SPI | I2C | UART | Strapping | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ADC2_CH1 | T1 | - | - | - | BOOT (LOW=flash) | BOOT button, pull-up 10k |
| 1 | - | - | - | - | TX0 | - | USB-UART TX, do not use |
| 2 | ADC2_CH2 | T2 | - | - | - | STRAP | built-in LED, must be LOW at boot for normal boot |
| 3 | - | - | - | - | RX0 | - | USB-UART RX |
| 4 | ADC2_CH0 | T0 | HSPI HD | - | TX2* | - | good general GPIO |
| 5 | - | - | VSPI SS | - | - | STRAP | VSPI CS default, HIGH at boot |
| 12 | ADC2_CH5 | T5 | HSPI MISO | - | - | STRAP (MTDI) | HIGH=flash 3.3V, do not pull HIGH hard |
| 13 | ADC2_CH4 | T4 | HSPI MOSI | - | - | - | good GPIO |
| 14 | ADC2_CH6 | T6 | HSPI SCK | - | - | - | good GPIO |
| 15 | ADC2_CH3 | T3 | HSPI SS | - | - | STRAP (MTDO) | HIGH=ROM silent log |
| 16 | - | - | - | - | RX2 | - | good for UART/GPS |
| 17 | - | - | - | - | TX2 | - | good for UART/GPS |
| 18 | - | - | VSPI SCK | - | - | STRAP | VSPI SCK |
| 19 | - | - | VSPI MISO | - | - | - | VSPI MISO |
| 21 | - | - | - | SDA* | - | - | I2C default |
| 22 | - | - | - | SCL* | - | - | I2C default |
| 23 | - | - | VSPI MOSI | - | - | - | VSPI MOSI |
| 25 | ADC2_CH8 | - | - | - | - | - | DAC1, good analog |
| 26 | ADC2_CH9 | - | - | - | - | - | DAC2 |
| 27 | ADC2_CH7 | T7 | - | - | - | - | good GPIO |
| 32 | ADC1_CH4 | T9 | - | - | - | - | RTC, ULP, good |
| 33 | ADC1_CH5 | T8 | - | - | - | - | RTC, ULP |
| 34 | ADC1_CH6 | - | - | - | - | - | input only, no pull-up/down |
| 35 | ADC1_CH7 | - | - | - | - | - | input only |
| 36 VP | ADC1_CH0 | - | - | - | - | - | input only |
| 39 VN | ADC1_CH3 | - | - | - | - | - | input only |
| 6-11 | - | - | SPI-flash | - | - | - | DO NOT USE! flash |

*UART/I2C/SPI can be mapped to almost any GPIO via matrix; listed are typical.
ADC2 conflicts with WiFi - with WiFi on, ADC2 unavailable! Analog only via ADC1. See [[06-Analog/01-ADC|ADC]].

## 2. ESP32-S3 DevKitC-1 (44 pins, USB-OTG, PSRAM optional)

| GPIO | ADC | Touch | SPI | I2C | UART | Strapping | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | - | - | - | - | - | BOOT (LOW=download) | BOOT button |
| 1-2 | - | T1-T2 | - | - | - | - | good GPIO |
| 3 | - | T3 | - | - | - | STRAP (JTAG) | - |
| 4-10 | ADC1 | T4-T10 | SPI2/3 | - | - | - | camera/display bus, 8-20 = DVP |
| 11-14 | ADC1/2 | T11-T14 | SPI2 | - | - | SPI-flash/PSRAM (do not touch on octal boards) | careful! |
| 15-20 | ADC2 | - | - | - | UHCI | - | camera DVP data |
| 21 | - | - | - | - | - | - | good GPIO |
| 33-37 | - | T | - | - | - | OCTAL-flash strap | on S3R8 do not use as GPIO |
| 38-42 | - | - | - | - | TX0/RX0* | STRAP | USB-UART, 19/20 = USB-D-/D+ native |
| 43-44 | - | T | - | - | TX0/RX0 | - | USB-UART default |
| 45 | - | - | - | - | - | STRAP (VDD_SPI) | LOW=3.3V flash |
| 46 | - | - | - | - | - | STRAP | pull-down for normal boot |
| 47-48 | - | - | - | - | - | - | RGB LED (48), 47 = PSRAM safe |

S3 native USB (GPIO19/20) allows USB-CDC + JTAG without bridge. OV2640 camera only with PSRAM board (S3R8/R16). See [[12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera]].

## 3. ESP32-C3 SuperMini (RISC-V, 22 pins)

| GPIO | ADC | Touch | SPI | I2C | UART | Strapping | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0-5 | ADC1 | - | SPI2 | - | - | - | good GPIO, 2-5 = strapping SPI-flash careful |
| 2-5 | - | - | SPI-flash | - | - | STRAP | do not pull at boot |
| 6-7 | - | - | - | - | - | - | free GPIO |
| 8 | - | - | - | SDA* | - | STRAP (BOOT) | RGB-LED, BOOT mode at LOW |
| 9 | - | - | - | - | - | STRAP | BOOT, pull-up |
| 10 | - | - | - | SCL* | - | - | I2C default |
| 20-21 | - | - | - | - | TX0/RX0 | - | USB-Serial-JTAG |

C3: one ADC (ADC1, 6 channels), no DAC, no touch, WiFi 4 + BLE5. Small SuperMini antenna - weaker WiFi (~-3 dB). Power 5V pin -> LDO 3.3V 500 mA.

| Symptom | Cause | Fix |
| --- | --- | --- |
| GPIO34-39 do not set OUT | input only classic | move output to 25-27/32-33 |
| ADC2 zeros with WiFi | WiFi/ADC2 conflict | only ADC1 for analog |
| S3 does not boot, LED dim | GPIO0/45/46 pulled | remove pull on strapping, see [[EN/99-Additions/02-Troubleshooting-FAQ.en]] |

## 4. ESP32-C6 / H2 (RISC-V + 802.15.4, brief)

| Board | USB | Strapping at boot | Special |
| --- | --- | --- | --- |
| C6-DevKitC-1 | 2× USB-C (bridge + native) | GPIO8/9 free! | RGB on GPIO8 |
| XIAO/Beetle C6 | native | GPIO8/9 free! | BAT pads + charge (XIAO/Beetle) |
| H2-DevKitM-1 | native | GPIO8/9/25 free! | WiFi NONE; brick → GPIO25+BOOT |
| C3-DevKitC-02 | bridge + native | GPIO2/8/9 free! | Classic C3 full-size |

Details: [[14-Devboards/13-ESP32C6-Boards|C6 boards]], [[14-Devboards/14-ESP32H2-Boards|H2 boards]].

## See Also

- [[EN/Home.en]]
- [[03-GPIO/01-GPIO-oglyad]]
- [[04-Interfaces/02-SPI|SPI]]
- [[04-Interfaces/03-I2C|I2C]]
- [[04-Interfaces/01-UART|UART]]
- [[06-Analog/01-ADC|ADC]]
- [[EN/99-Additions/02-Troubleshooting-FAQ.en]]

![[assets/img/placeholder.png]]

> UA original twin: [[99-Additions/01-Pinout-tablici.md | UA]]
