---
title: Зведені pinout-таблиці
description: Pinout-таблиці: DevKit V1 / S3 DevKitC / C3 SuperMini: ADC/CAN/DAC
tags: [esp32, pinout, devkit, s3, c3, gpio, strapping]
date: 2026-09-27
---

# Pinout-таблиці: DevKit V1 / S3 DevKitC / C3 SuperMini

![[assets/img/esp32-classic-pinout.png|600]]

![[assets/img/esp32-s3-pinout.png|600]]

![[assets/img/esp32-c3-supermini-pinout.png|600]]

База GPIO: [[03-GPIO/01-GPIO-oglyad]], шини [[04-Shini/02-SPI|SPI]] [[04-Shini/03-I2C|I2C]] [[04-Shini/01-UART|UART]], сон [[07-Timeri-Son/03-Sleep-ULP]], аналог [[06-Analog/01-ADC|ADC]], старт [[Home]], ремонт [[99-Dodatki/02-Troubleshooting-FAQ]].

## 1. ESP32 DevKit V1 (classic D0WD, 30 пінів)

| GPIO | ADC | Touch | SPI | I2C | UART | Strapping | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ADC2_CH1 | T1 | - | - | - | BOOT (LOW=flash) | кнопка BOOT, pull-up 10к |
| 1 | - | - | - | - | TX0 | - | USB-UART TX, не займати |
| 2 | ADC2_CH2 | T2 | - | - | - | STRAP | вбудований LED, має бути LOW на старті для норм. boot |
| 3 | - | - | - | - | RX0 | - | USB-UART RX |
| 4 | ADC2_CH0 | T0 | HSPI HD | - | TX2* | - | добрий загальний GPIO |
| 5 | - | - | VSPI SS | - | - | STRAP | VSPI CS за замовч., HIGH на старті |
| 12 | ADC2_CH5 | T5 | HSPI MISO | - | - | STRAP (MTDI) | HIGH=flash 3.3V, не тягнути HIGH сильно |
| 13 | ADC2_CH4 | T4 | HSPI MOSI | - | - | - | добрий GPIO |
| 14 | ADC2_CH6 | T6 | HSPI SCK | - | - | - | добрий GPIO |
| 15 | ADC2_CH3 | T3 | HSPI SS | - | - | STRAP (MTDO) | HIGH=ROM-лог silent |
| 16 | - | - | - | - | RX2 | - | добрий для UART/GPS |
| 17 | - | - | - | - | TX2 | - | добрий для UART/GPS |
| 18 | - | - | VSPI SCK | - | - | STRAP | VSPI SCK |
| 19 | - | - | VSPI MISO | - | - | - | VSPI MISO |
| 21 | - | - | - | SDA* | - | - | I2C за замовч. |
| 22 | - | - | - | SCL* | - | - | I2C за замовч. |
| 23 | - | - | VSPI MOSI | - | - | - | VSPI MOSI |
| 25 | ADC2_CH8 | - | - | - | - | - | DAC1, добрий аналог |
| 26 | ADC2_CH9 | - | - | - | - | - | DAC2 |
| 27 | ADC2_CH7 | T7 | - | - | - | - | добрий GPIO |
| 32 | ADC1_CH4 | T9 | - | - | - | - | RTC, ULP, добрий |
| 33 | ADC1_CH5 | T8 | - | - | - | - | RTC, ULP |
| 34 | ADC1_CH6 | - | - | - | - | - | тільки вхід, без pull-up/down |
| 35 | ADC1_CH7 | - | - | - | - | - | тільки вхід |
| 36 VP | ADC1_CH0 | - | - | - | - | - | тільки вхід |
| 39 VN | ADC1_CH3 | - | - | - | - | - | тільки вхід |
| 6-11 | - | - | SPI-flash | - | - | - | НЕ використовувати! flash |

*UART/I2C/SPI можна мапити на майже будь-які GPIO через матрицю, вказані - типові.
ADC2 конфліктує з WiFi - при увімкненому WiFi ADC2 недоступний! Аналог тільки ADC1. Див. [[06-Analog/01-ADC|ADC]].

## 2. ESP32-S3 DevKitC-1 (44 піни, USB-OTG, PSRAM опційно)

| GPIO | ADC | Touch | SPI | I2C | UART | Strapping | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | - | - | - | - | - | BOOT (LOW=download) | кнопка BOOT |
| 1-2 | - | T1-T2 | - | - | - | - | добрі GPIO |
| 3 | - | T3 | - | - | - | STRAP (JTAG) | - |
| 4-10 | ADC1 | T4-T10 | SPI2/3 | - | - | - | шина камери/дисплея, 8-20 = DVP |
| 11-14 | ADC1/2 | T11-T14 | SPI2 | - | - | SPI-flash/PSRAM (не чіпати на платах з octal) | обережно! |
| 15-20 | ADC2 | - | - | - | UHCI | - | DVP дані камери |
| 21 | - | - | - | - | - | - | добрий GPIO |
| 33-37 | - | T | - | - | - | OCTAL-flash strap | на S3R8 не використовувати як GPIO |
| 38-42 | - | - | - | - | TX0/RX0* | STRAP | USB-UART, 19/20 = USB-D-/D+ native |
| 43-44 | - | T | - | - | TX0/RX0 | - | USB-UART за замовч. |
| 45 | - | - | - | - | - | STRAP (VDD_SPI) | LOW=3.3V flash |
| 46 | - | - | - | - | - | STRAP | pull-down для норм. boot |
| 47-48 | - | - | - | - | - | - | LED RGB (48), 47 = PSRAM safe |

S3 native USB (GPIO19/20) дозволяє USB-CDC + JTAG без моста. Камера OV2640 тільки з PSRAM-платою (S3R8/R16). Див. [[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera]].

## 3. ESP32-C3 SuperMini (RISC-V, 22 піни)

| GPIO | ADC | Touch | SPI | I2C | UART | Strapping | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0-5 | ADC1 | - | SPI2 | - | - | - | добрі GPIO, 2-5 = strapping SPI-flash уважно |
| 2-5 | - | - | SPI-flash | - | - | STRAP | не тягнути при старті |
| 6-7 | - | - | - | - | - | - | вільні GPIO |
| 8 | - | - | - | SDA* | - | STRAP (BOOT) | RGB-LED, BOOT-режим при LOW |
| 9 | - | - | - | - | - | STRAP | BOOT, pull-up |
| 10 | - | - | - | SCL* | - | - | I2C за замовч. |
| 20-21 | - | - | - | - | TX0/RX0 | - | USB-Serial-JTAG |

C3: один ADC (ADC1, 6 каналів), немає DAC, немає touch, WiFi 4 + BLE5. Маленька антена SuperMini - слабший WiFi (~-3 дБ). Живлення 5V пін -> LDO 3.3V 500 мА.

| Симптом | Причина | Рішення |
| --- | --- | --- |
| GPIO34-39 не виставляються OUT | тільки входи classic | перенести вихід на 25-27/32-33 |
| ADC2 нулі при WiFi | конфлікт WiFi/ADC2 | тільки ADC1 для аналогу |
| S3 не бутиться, LED тьмяно | GPIO0/45/46 притягнуті | прибрати pull на strapping, див. [[99-Dodatki/02-Troubleshooting-FAQ]] |

## 4. ESP32-C6 / H2 (RISC-V + 802.15.4, коротко)

| Плата | USB | Strapping при boot | Особливе |
| --- | --- | --- | --- |
| C6-DevKitC-1 | 2× USB-C (міст + native) | GPIO8/9 вільні! | RGB на GPIO8 |
| XIAO/Beetle C6 | native | GPIO8/9 вільні! | Пади BAT + зарядка (XIAO/Beetle) |
| H2-DevKitM-1 | native | GPIO8/9/25 вільні! | WiFi НЕМАЄ; цегла → GPIO25+BOOT |
| C3-DevKitC-02 | міст + native | GPIO2/8/9 вільні! | Класика C3 повнорозмірна |

Деталі: [[14-Devboards/13-ESP32C6-Boards|C6-плати]], [[14-Devboards/14-ESP32H2-Boards|H2-плати]].

## Див. також

- [[Home]]
- [[03-GPIO/01-GPIO-oglyad]]
- [[04-Shini/02-SPI|SPI]]
- [[04-Shini/03-I2C|I2C]]
- [[04-Shini/01-UART|UART]]
- [[06-Analog/01-ADC|ADC]]
- [[99-Dodatki/02-Troubleshooting-FAQ]]

![[assets/img/placeholder.png]]
