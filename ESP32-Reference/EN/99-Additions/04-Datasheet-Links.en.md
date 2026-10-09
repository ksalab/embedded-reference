---
title: Datasheet Links, Prices, Where to Buy, Literature
description: Official Espressif datasheets, module price estimates (2026, retail Ukraine/China), where to purchase, and reference literature; shows schematics, code and tables.
tags: [esp32, datasheet, buy, price, books]
category: Meta
lang: en
original: ESP32-Reference/99-Additions/04-Datasheet-Links.md
date-created: 2026-09-27
date: 2026-10-08
---

# Datasheet Links, Prices, Where to Buy, Literature

![[assets/img/placeholder.png]]

Navigation: [[EN/Home.en]], pins [[EN/99-Additions/01-Pinout-tablici.en]], repair [[EN/99-Additions/02-Troubleshooting-FAQ.en]], checklists [[EN/99-Additions/03-Cheklisti-montazhu.en]], power [[02-Power-Supply/01-Lancjugi-zhivlennya]], radio [[05-Radio/01-WiFi-STA-AP]].

## 1. Official Espressif Datasheets (search by name on espressif.com)

| Document | Contents | When to open |
| --- | --- | --- |
| ESP32 Datasheet (D0WD) | electrical params, strapping, ADC, touch | first boot, strapping, voltage limits |
| ESP32-S3 Datasheet + TRM | GPIO matrix, USB-OTG, DVP camera, PSRAM octal | camera/display/USB projects |
| ESP32-C3 Datasheet | RISC-V, ADC1, strapping, sleep currents | SuperMini battery projects |
| ESP32 Hardware Design Guidelines | antenna layout, power, EMC | own board, external antenna |
| ESP-IDF Programming Guide | API for all peripherals, TWAI/Ethernet/Camera | ESP-IDF development |
| ESP-AT Command Set | AT for WiFi/BLE modems | AT firmware |
| MFRC522 (NXP) | RFID registers, 13.56 MHz antenna | [[12-Comm-Modules/01-RC522-RFID]] deep dive |
| SX1276/78 (Semtech) | LoRa modem, link budget | [[12-Comm-Modules/02-NRF24-LoRa]] range |
| SIM800 Series AT Manual (Simcom) | all AT commands GSM/GPRS | [[12-Comm-Modules/03-SIM800L-GPS]] SMS/HTTP |
| NEO-6M Hardware Integration (u-blox) | NMEA, PPS, antennas | GPS accuracy |
| SN65HVD230 / TJA1050 | CAN transceivers | [[12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera]] |
| LAN8720A | RMII, REF_CLK 50 MHz | Ethernet classic only |
| OV2640 | DVP, SCCB, resolution | camera S3 |

## 2. Module Price Estimates (2026, retail Ukraine/China)

| ESP32 Module | Approx. price | Note |
| --- | --- | --- |
| ESP32 DevKit V1 (CH340, 30p) | 180-260 UAH / $5-7 | workhorse, buy with wide pins |
| ESP32-S3 DevKitC-1 N8R8 | 350-500 UAH / $9-13 | camera + display + USB-OTG, only with PSRAM |
| ESP32-C3 SuperMini | 120-180 UAH / $3-5 | battery BLE/WiFi, weaker antenna |
| RC522 RFID | 80-130 UAH / $2-3 | only 3.3V version |
| NRF24L01+PA+LNA + adapter | 120-200 UAH / $3-5 | adapter with AMS1117 required |
| LoRa Ra-02 SX1276 + antenna | 250-380 UAH / $6-10 | antenna 433/868 separate +50-100 UAH |
| SIM800L blue (no reg) | 250-350 UAH | + buck LM2596 + 1000 µF |
| SIM800L EVB red (with reg) | 350-500 UAH | can use 5V, easier for beginners |
| NEO-6M with antenna | 250-400 UAH | active antenna +100 UAH indoors |
| MAX485 module | 40-70 UAH | buy TVS version for outdoor |
| SN65HVD230 module | 90-140 UAH | 3.3V, better than TJA1050 for ESP32 |
| LAN8720 module | 200-300 UAH | classic ESP32 only! |
| OV2640 for S3 / ESP32-S3-CAM | 400-700 UAH assembled | standalone sensor 150-250 UAH |
| MP1584 / LM2596 module | 60-110 UAH | MP1584 better efficiency |
| MT3608 boost | 50-90 UAH | for 1x18650 |
| TP4056 with protection | 30-60 UAH | only DW01 OUT+- version |
| CN3791 MPPT solar | 120-200 UAH | for solar, not TP4056 |
| TXS0108E 8ch | 60-110 UAH | universal shift |
| BSS138 4ch I2C shift | 40-70 UAH | for I2C classic |

> Prices approximate, fluctuate with exchange rate. China (AliExpress) 20-40% cheaper but 2-4 weeks delivery and clone risk (CP2102 clone, RC522 defect).

## 3. Where to Buy (Ukraine + Worldwide)

- Ukraine: Arduino.ua, Microchip.com.ua (Kyiv), RadioMarket, Prom.ua sellers with rating; OLX only with verification.
- China: AliExpress (official: Espressif store, Heltec, Lilygo), LCSC for components, JLCPCB for custom boards.
- Tips: CH340 driver download from wch.cn; USB DATA cables check immediately; SIM cards for SIM800L - 2G! (Lifecell/Vodafone 2G still alive, check coverage; SIM800L does NOT support 4G - for 4G use SIM7600).

## 4. Literature and Resources

- Espressif Docs (docs.espressif.com) - primary source, always more current than blogs.
- RandomNerdTutorials.com - practical ESP32 projects with code.
- LastMinuteEngineers.com - module breakdown RC522/NRF24/SIM800L by registers.
- Book: Kolban ESP32 (free PDF) - full classic overview.
- Book: John H. Davies, ESP32-C3/S3 deep topics (2024-2025).
- YouTube: Andreas Spiess (solar/battery/LoRa measurements), Espressif Developers.

## 5. New Chips/Boards (update 2026)

| Component | Search | Base note |
| --- | --- | --- |
| ESP32-C6 / H2 | datasheet + TRM + errata | [[01-Hardware/04-ESP32-C3-C6-H2]] |
| ESP32-C5 / C61 / P4 | product brief + migration guide | [[01-Hardware/10-ESP32-C5-C61]] |
| ZED-F9P / UM980 (RTK) | integration manual + interface description | [[12-Comm-Modules/17-GNSS-RTK]] |
| A7670 / EC200U (Cat-1) | AT manual + hardware design | [[12-Comm-Modules/18-Cellular-LoRa-2]] |
| ATECC608 / SE050 | datasheet + appnotes ([ATECC608 Microchip](https://www.microchip.com/en-us/product/ATECC608)) | [[12-Comm-Modules/25-Secure-Elements]] |

## See Also

- [[EN/Home.en]]
- [[EN/99-Additions/01-Pinout-tablici.en]]
- [[EN/99-Additions/02-Troubleshooting-FAQ.en]]
- [[EN/99-Additions/03-Cheklisti-montazhu.en]]
- [[12-Comm-Modules/01-RC522-RFID]]
- [[12-Comm-Modules/02-NRF24-LoRa]]
- [[12-Comm-Modules/03-SIM800L-GPS]]

![[assets/img/placeholder.png]]

> UA original twin: [[99-Additions/04-Datasheet-Links.md | UA]]
