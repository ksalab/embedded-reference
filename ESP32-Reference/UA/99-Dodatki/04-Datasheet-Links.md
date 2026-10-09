---
title: Даташити посилання ціни
description: Datasheet Links, ціни, де купити, література - Офіційні даташити Espressif (шукати за назвою на espressif.com); Таблиця модулів - орієнтовні ціни (2026, роздріб Україна/Китай); Де купити (Україна +...
tags: [esp32, datasheet, buy, price, books]
date: 2026-09-27
---

# Datasheet Links, ціни, де купити, література

![[assets/img/placeholder.png]]

Навігація: [[Home]], піни [[99-Dodatki/01-Pinout-tablici]], ремонт [[99-Dodatki/02-Troubleshooting-FAQ]], чек-листи [[99-Dodatki/03-Cheklisti-montazhu]], живлення [[02-Zhivlennya/01-Lancjugi-zhivlennya]], радіо [[05-Radio/01-WiFi-STA-AP]].

## 1. Офіційні даташити Espressif (шукати за назвою на espressif.com)

| Документ | Що всередині | Коли відкривати |
| --- | --- | --- |
| ESP32 Datasheet (D0WD) | електричні параметри, strapping, ADC, touch | перший запуск, strapping, межі напруг |
| ESP32-S3 Datasheet + TRM | GPIO-матриця, USB-OTG, камера DVP, PSRAM octal | камера/дисплей/USB проекти |
| ESP32-C3 Datasheet | RISC-V, ADC1, strapping, sleep-струми | SuperMini батарейні проекти |
| ESP32 Hardware Design Guidelines | розводка антени, живлення, EMC | своя плата, винесена антена |
| ESP-IDF Programming Guide | API всіх периферій, TWAI/Ethernet/Camera | ESP-IDF розробка |
| ESP-AT Command Set | AT для WiFi/BLE-модемів | AT-прошивки |
| MFRC522 (NXP) | регістри RFID, антена 13.56 МГц | [[12-Moduli-zvyazku/01-RC522-RFID]] глибоко |
| SX1276/78 (Semtech) | LoRa-модем, link budget | [[12-Moduli-zvyazku/02-NRF24-LoRa]] дальність |
| SIM800 Series AT Manual (Simcom) | всі AT-команди GSM/GPRS | [[12-Moduli-zvyazku/03-SIM800L-GPS]] SMS/HTTP |
| NEO-6M Hardware Integration (u-blox) | NMEA, PPS, антени | GPS-точність |
| SN65HVD230 / TJA1050 | CAN-трансивери | [[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera]] |
| LAN8720A | RMII, REF_CLK 50 МГц | Ethernet тільки classic |
| OV2640 | DVP, SCCB, роздільна здатність | камера S3 |

## 2. Таблиця модулів - орієнтовні ціни (2026, роздріб Україна/Китай)

| ESP32-Модуль | Орієнтовна ціна | Коментар |
| --- | --- | --- |
| ESP32 DevKit V1 (CH340, 30p) | 180-260 грн / $5-7 | робоча конячка, брати з широкими пінами |
| ESP32-S3 DevKitC-1 N8R8 | 350-500 грн / $9-13 | камера+дисплей+USB-OTG, тільки з PSRAM |
| ESP32-C3 SuperMini | 120-180 грн / $3-5 | батарейні BLE/WiFi, слабша антена |
| RC522 RFID | 80-130 грн / $2-3 | тільки 3.3V версія |
| NRF24L01+PA+LNA + адаптер | 120-200 грн / $3-5 | адаптер з AMS1117 обов'язково |
| LoRa Ra-02 SX1276 + антена | 250-380 грн / $6-10 | антена на 433/868 окремо +50-100 грн |
| SIM800L синя (без стаб.) | 250-350 грн | + buck LM2596 + 1000 мкФ |
| SIM800L EVB червона (зі стаб.) | 350-500 грн | можна 5V, простіше новачкам |
| NEO-6M з антеною | 250-400 грн | активна антена +100 грн для приміщень |
| MAX485 модуль | 40-70 грн | брати з TVS-версією для вулиці |
| SN65HVD230 модуль | 90-140 грн | 3.3V, кращий за TJA1050 для ESP32 |
| LAN8720 модуль | 200-300 грн | тільки classic ESP32! |
| OV2640 під S3 / ESP32-S3-CAM | 400-700 грн у зборі | окремий сенсор 150-250 грн |
| MP1584 / LM2596 модуль | 60-110 грн | MP1584 кращий ККД |
| MT3608 boost | 50-90 грн | для 1x18650 |
| TP4056 з захистом | 30-60 грн | тільки версія з DW01 OUT+- |
| CN3791 MPPT solar | 120-200 грн | для сонця, не TP4056 |
| TXS0108E 8ch | 60-110 грн | універсальний shift |
| BSS138 4ch I2C shift | 40-70 грн | для I2C класика |

> Ціни орієнтовні, коливаються з курсом. Китай (AliExpress) дешевше на 20-40%, але 2-4 тижні доставка і ризик клонів (CP2102 клон, RC522 брак).

## 3. Де купити (Україна + світ)

- Україна: Arduino.ua, Microchip.com.ua (Київ), RadioMarket, Prom.ua продавці з рейтингом, OLX тільки з перевіркою.
- Китай: AliExpress (офіційні: Espressif store, Heltec, Lilygo), LCSC для компонентів, JLCPCB для своїх плат.
- Поради: CH340-драйвер качати з wch.cn; USB-кабелі DATA перевіряти одразу; SIM-карти для SIM800L - 2G! (Lifecell/Vodafone 2G ще живі, перевіряти покриття; SIM800L НЕ вміє 4G - для 4G брати SIM7600).

## 4. Література та ресурси

- Espressif Docs (docs.espressif.com) - першоджерело, завжди актуальніше за блоги.
- RandomNerdTutorials.com - практичні ESP32-проекти з кодом.
- LastMinuteEngineers.com - розбір модулів RC522/NRF24/SIM800L по регістрах.
- Книга: Kolban ESP32 (безкоштовно PDF) - повний огляд classic.
- Книга: John H. Davies, ESP32-C3/S3 глибокі теми (2024-2025).
- YouTube: Andreas Spiess (сонце/батареї/LoRa заміри), Espressif Developers.

## 5. Нові чипи/плати (доповнення 2026)

| Компонент | Шукати | Нота бази |
| --- | --- | --- |
| ESP32-C6 / H2 | datasheet + TRM + errata | [[01-Hardware/04-ESP32-C3-C6-H2]] |
| ESP32-C5 / C61 / P4 | product brief + migration guide | [[01-Hardware/10-ESP32-C5-C61]] |
| ZED-F9P / UM980 (RTK) | integration manual + interface description | [[12-Moduli-zvyazku/17-GNSS-RTK]] |
| A7670 / EC200U (Cat-1) | AT manual + hardware design | [[12-Moduli-zvyazku/18-Cellular-LoRa-2]] |
| ATECC608 / SE050 | datasheet + appnotes ([ATECC608 Microchip](https://www.microchip.com/en-us/product/ATECC608)) | [[12-Moduli-zvyazku/25-Secure-Elements]] |

## Див. також

- [[Home]]
- [[99-Dodatki/01-Pinout-tablici]]
- [[99-Dodatki/02-Troubleshooting-FAQ]]
- [[99-Dodatki/03-Cheklisti-montazhu]]
- [[12-Moduli-zvyazku/01-RC522-RFID]]
- [[12-Moduli-zvyazku/02-NRF24-LoRa]]
- [[12-Moduli-zvyazku/03-SIM800L-GPS]]

![[assets/img/placeholder.png]]

> English twin: [[99-Dodatki/04-Datasheet-Links.en.md | EN]]
