---
title: Офіційні джерела модулів
description: Офіційні джерела модулів зв'язку, живлення і чипів - Офіційна документація Espressif (база для всього довідника); Модулі зв'язку (`12-Moduli-zvyazku/`); 1. RC522 RFID (12-Moduli-zvyazku/01-RC522-RFID)
tags: [esp32, datasheet, official, modules, links]
date: 2026-09-28
---

# Офіційні джерела модулів зв'язку, живлення і чипів

![[assets/img/sources-modules-scheme.png|600]]
*Рис. Ланцюжок довіри: компонент, фото, код.*

> [!info] Як користуватись
> Реєстр **офіційних** джерел для кожного компонента з [[12-Moduli-zvyazku/01-RC522-RFID|12-Moduli-zvyazku]] (8 нотаток), [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar|13-Moduli-zhivlennya-rivniv]] (5 нотаток) і [[01-Hardware/01-ESP32-Classic|01-Hardware]] (8 нотаток) + окремий блок документації Espressif.
> Формат: **Компонент → даташит виробника → сторінка продукту з живим фото → туторіал з кодом**.
> Позначки: ✅ - URL перевірено через webfetch (200, станом на 2026-09-28); ⚠️ *перевірити вручну* - сторінка існує, але автоперевірка заблокована (бот-захист) або точний URL не підтверджено, вгадувати заборонено.
> Живі зображення - лише зовнішні посилання на сторінки з фото; чужі картинки в репозиторій НЕ копіювати.

Навігація: [[Home]], ціни та література [[99-Dodatki/04-Datasheet-Links]], піни [[99-Dodatki/01-Pinout-tablici]], ремонт [[99-Dodatki/02-Troubleshooting-FAQ]].

## 0. Офіційна документація Espressif (база для всього довідника)

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| ESP32-D0WD-V3 (Classic) | База: електрика, strapping, ADC | ✅ [ESP32 Datasheet (PDF)](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) - повний даташит | ✅ [ESP32 - сторінка продукту](https://www.espressif.com/en/products/socs/esp32) - опис, фото, ресурси | ✅ [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/) - API всіх периферій |
| ESP32-S2 / S3 / C3 / C6 / H2 | Даташити по чипах, TRM | ✅ [Техдокументація Espressif (хаб)](https://www.espressif.com/en/support/download/documents) - datasheets, TRM, пошук за назвою чипа | ✅ [ESP32-S2](https://www.espressif.com/en/products/socs/esp32-s2) ✅ [ESP32-S3](https://www.espressif.com/en/products/socs/esp32-s3) ✅ [ESP32-C3](https://www.espressif.com/en/products/socs/esp32-c3) ✅ [ESP32-C6](https://www.espressif.com/en/products/socs/esp32-c6) ✅ [ESP32-H2](https://www.espressif.com/en/products/socs/esp32-h2) - фото і характеристики | ✅ [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/) - вибір target у дропдауні |
| Модулі WROOM / WROVER / MINI | Сертифіковані модулі, розміри, антени | ✅ [Техдокументація Espressif (хаб)](https://www.espressif.com/en/support/download/documents) - шукати WROOM-32 / WROVER / MINI-1 | ✅ [ESP Modules](https://www.espressif.com/en/products/modules) - каталог модулів з фото | ✅ [ESP32 Pinout Reference (RNT)](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) - які GPIO можна використовувати, з фото |
| Hardware Design Guidelines | Своя плата, антена, живлення, EMC | ✅ [Техдокументація Espressif (хаб)](https://www.espressif.com/en/support/download/documents) - шукати «Hardware Design Guidelines» | ✅ [ESP32 - сторінка продукту](https://www.espressif.com/en/products/socs/esp32) - розділ Hardware Design Guidelines | ✅ [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/) - Hardware Reference |
| ESP-AT (AT-прошивки) | WiFi/BLE-модем, AT-команди | ✅ [ESP-AT User Guide](https://docs.espressif.com/projects/esp-at/en/latest/) - бінарники, AT-команди, приклади | ✅ [Техдокументація Espressif (хаб)](https://www.espressif.com/en/support/download/documents) - ESP-AT releases | ✅ [ESP-AT User Guide - AT Command Examples](https://docs.espressif.com/projects/esp-at/en/latest/) - готові приклади з кодом |

## 1. Модулі зв'язку (`12-Moduli-zvyazku/`)

### 1.1. RC522 RFID ([[12-Moduli-zvyazku/01-RC522-RFID]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| MFRC522 (RC522) | RFID 13.56 МГц, SPI, 3.3V | ✅ [MFRC522 Datasheet (PDF, NXP)](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf) - регістри, антена | ✅ [MFRC522 - сторінка NXP](https://www.nxp.com/products/rfid-nfc/nfc-hf/nfc-readers/standard-performance-mifare-and-ntag-frontend:MFRC52202HN1) - фото, доки, EOL-статус | ✅ [ESP32 + MFRC522 (RNT)](https://randomnerdtutorials.com/esp32-mfrc522-rfid-reader-arduino/) - UID, читання/запис, код |
| RC522 (модуль) | Дешева синя плата, ті ж піни | ✅ той же [MFRC522 PDF](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf) | ✅ [MFRC522 - сторінка NXP](https://www.nxp.com/products/rfid-nfc/nfc-hf/nfc-readers/standard-performance-mifare-and-ntag-frontend:MFRC52202HN1) - фото чипа | ✅ [RC522 + Arduino (LME)](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/) - піни, пам'ять Mifare 1K, фото підключення |

### 1.2. NRF24 + LoRa ([[12-Moduli-zvyazku/02-NRF24-LoRa]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| nRF24L01+ (+PA+LNA) | 2.4 ГГц, SPI, тільки 3.3V, 250 мА пік | ⚠️ *перевірити вручну* - nordicsemi.com блокує автозапити (403); шукати «nRF24L01 Product Specification» на nordicsemi.com | ⚠️ *перевірити вручну* - сторінка продукту nordicsemi.com (блокує ботів) | ✅ [nRF24L01 + Arduino (LME)](https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/) - Multiceiver, ShockBurst, конденсатор, код TX/RX |
| LoRa SX1276 (Ra-02) | 433/868 МГц, антена обов'язково | ✅ [SX1276 - Semtech](https://www.semtech.com/products/wireless-rf/lora-connect/sx1276) - даташит, link budget, PDF | ✅ та сама [сторінка SX1276 Semtech](https://www.semtech.com/products/wireless-rf/lora-connect/sx1276) - фото, dev-кити | ✅ [ESP32 + LoRa RFM95 (RNT)](https://randomnerdtutorials.com/esp32-lora-rfm95-transceiver-arduino-ide/) - Sender/Receiver, код |

### 1.3. SIM800L + GPS ([[12-Moduli-zvyazku/03-SIM800L-GPS]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| SIM800L | GSM 2G, 3.4-4.4V, пік 2A, AT-команди | ✅ [SIM800 - SIMCom](https://www.simcom.com/product/SIM800.html) - AT Manual, Hardware Design, файли | ✅ та сама [сторінка SIM800 SIMCom](https://www.simcom.com/product/SIM800.html) - фото, специфікація | ✅ [SIM800L SMS + ESP32 (RNT)](https://randomnerdtutorials.com/esp32-sim800l-send-text-messages-sms/) - TinyGSM, код ✅ [SIM800L + Arduino (LME)](https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/) - живлення 4V, AT, фото |
| NEO-6M GPS (u-blox NEO-6) | UART 9600, NMEA, антена | ✅ [NEO-6 series - u-blox](https://www.u-blox.com/en/product/neo-6-series) - Data Sheet, інтеграція | ✅ та сама [сторінка NEO-6 u-blox](https://www.u-blox.com/en/product/neo-6-series) - фото, варіанти | ✅ [ESP32 + NEO-6M (RNT)](https://randomnerdtutorials.com/esp32-neo-6m-gps-module-arduino/) - TinyGPS++, код |

### 1.4. RS485 / CAN / Ethernet / Камера ([[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| MAX485 / MAX3485 (RS485) | DE/RE, 120 Ом, напівдуплекс | ⚠️ *перевірити вручну* - шукати «MAX485» на analog.com (Maxim/ADI) | ⚠️ *перевірити вручну* - сторінка продукту analog.com з фото | ✅ [ESP32-CAM / загальні UART-практики (RNT)](https://randomnerdtutorials.com/esp32-cam-video-streaming-face-recognition-arduino-ide/) - суміжний приклад UART-периферії; RS485-код - у нотатці |
| SN65HVD230 (CAN 3.3V) | Кращий за TJA1050 для ESP32 | ✅ [SN65HVD230 - TI](https://www.ti.com/product/SN65HVD230) - даташит, standby, фото | ✅ та сама [сторінка TI](https://www.ti.com/product/SN65HVD230) - корпуси, EVM | ✅ код TWAI/CAN - у нотатці + [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/) (TWAI) |
| TJA1050 (CAN 5V) | Старий стандарт, потрібен shift | ⚠️ *перевірити вручну* - шукати «TJA1050» на nxp.com | ⚠️ *перевірити вручну* - сторінка NXP | ✅ орієнтир - [SN65HVD230 TI](https://www.ti.com/product/SN65HVD230) (3.3V заміна) |
| W5500 (Ethernet SPI) | Апаратний TCP/IP, 8 сокетів | ✅ [W5500 Datasheet - WIZnet Docs](https://docs.wiznet.io/Product/Chip/Ethernet/W5500) - регістри, SPI до 80 МГц | ✅ [W5500 - wiznet.io](https://wiznet.io/products/ethernet-chips/w5500) - фото, модулі | ✅ [W5500 Docs - приклади ioLibrary](https://docs.wiznet.io/Product/Chip/Ethernet/W5500) - TCP/UDP/MQTT приклади з кодом |
| LAN8720 (Ethernet RMII) | Тільки classic ESP32, REF_CLK 50 МГц | ⚠️ *перевірити вручну* - шукати «LAN8720» на microchip.com (SMSC) | ⚠️ *перевірити вручну* - сторінка Microchip | ✅ [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/) - Ethernet RMII приклади |
| OV2640 (камера) | DVP + SCCB, для S3 з PSRAM | ⚠️ *перевірити вручну* - шукати «OV2640» на omnivision-group.com | ⚠️ *перевірити вручну* - сторінка OmniVision | ✅ [ESP32-CAM відеострім (RNT)](https://randomnerdtutorials.com/esp32-cam-video-streaming-face-recognition-arduino-ide/) - CameraWebServer, код |

### 1.5. PN532 / RDM6300 / R307 / GM65 ([[12-Moduli-zvyazku/05-PN532-RDM6300-Fingerprint-GM65]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| PN532 NFC | I2C/SPI/UART, SEL0/SEL1 | ✅ [PN532 Datasheet (PDF, NXP)](https://www.nxp.com/docs/en/nxp/data-sheets/PN532_C1.pdf) - режими, емуляція | ✅ [PN532 - сторінка NXP](https://www.nxp.com/products/rfid-nfc/nfc-hf/nfc-readers/nfc-integrated-solution:PN5321A3HN) - фото, доки | ✅ [ESP32 + MFRC522 (RNT)](https://randomnerdtutorials.com/esp32-mfrc522-rfid-reader-arduino/) - суміжний RFID-код; PN532-бібліотека - у нотатці |
| RDM6300 125 кГц | UART 9600, тільки читання UID | ⚠️ *перевірити вручну* - виробник не публікує єдиний даташит; шукати «RDM6300 datasheet» | ⚠️ *перевірити вручну* - фото на сторінках продавців (LCSC та ін.) | ✅ [RC522 RFID (LME)](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/) - RFID-база, структура UID |
| R307 / AS608 (відбитки) | UART, шаблони 1:N на модулі | ⚠️ *перевірити вручну* - шукати «R307 fingerprint» / AS608 у виробника | ⚠️ *перевірити вручну* - фото модулів у продавців | ✅ код Adafruit-Fingerprint - у нотатці |
| GM65 (штрих/QR) | UART/USB-HID, автоскан | ⚠️ *перевірити вручну* - виробник не публікує єдину сторінку; шукати «GM65 barcode» | ⚠️ *перевірити вручну* - фото у продавців | ✅ код читання штрих-кодів - у нотатці |

### 1.6. HC-05 / HM-10 / CC1101 / HC-12 ([[12-Moduli-zvyazku/06-HC05-HM10-CC1101-HC12]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| HC-05 (BT Classic SPP) | UART-міст, AT 38400, логіка 3.3V | ⚠️ *перевірити вручну* - CSR BC417 EOL; шукати даташит HC-05 у продавців модулів | ⚠️ *перевірити вручну* - фото плат HC-05 у продавців | ✅ [HC-05 + Arduino (LME)](https://lastminuteengineers.com/hc05-bluetooth-arduino-tutorial/) - AT-режим, master/slave, код |
| HM-10 BLE (CC2541) | BLE 4.0, VCC 3.3V | ⚠️ *перевірити вручну* - CC2541 на ti.com (пошук «CC2541») | ⚠️ *перевірити вручну* - фото HM-10 у продавців | ✅ [ESP32 BLE Server/Scanner (RNT)](https://randomnerdtutorials.com/esp32-bluetooth-low-energy-ble-arduino-ide/) - GATT, код (BLE-база для HM-10) |
| CC1101 Sub-GHz | SPI + GDO0/GDO2, 433 МГц | ⚠️ *перевірити вручну* - шукати «CC1101» на ti.com | ⚠️ *перевірити вручну* - сторінка TI з фото | ✅ [nRF24L01 радіопрактики (LME)](https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/) - SPI-радіо, антени, живлення |
| HC-12 (SI4463, 433 МГц) | UART-міст до 1 км, AT+SET | ⚠️ *перевірити вручну* - Si4463 на silabs.com; HC-12 - модуль без єдиного вендора | ⚠️ *перевірити вручну* - фото HC-12 у продавців | ✅ [HC-05 UART-міст (LME)](https://lastminuteengineers.com/hc05-bluetooth-arduino-tutorial/) - той же патерн прозорого UART-моста |

### 1.7. SIM7600 / W5500 / MCP2515 ([[12-Moduli-zvyazku/07-SIM7600-W5500-MCP2515]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| SIM7600E-H (4G LTE) | VBAT 3.4-4.2V, піки 3A, PWRKEY | ✅ [SIM7600X-H - SIMCom](https://www.simcom.com/product/SIM7600X-H.html) - AT Manual, Hardware Design | ✅ та сама [сторінка SIM7600 SIMCom](https://www.simcom.com/product/SIM7600X-H.html) - фото, бенди | ✅ [SIM800L SMS (RNT)](https://randomnerdtutorials.com/esp32-sim800l-send-text-messages-sms/) - той же патерн TinyGSM/AT, код (піни й живлення - у нотатці) |
| W5500 | Див. 1.4 | ✅ [W5500 Docs](https://docs.wiznet.io/Product/Chip/Ethernet/W5500) | ✅ [W5500 wiznet.io](https://wiznet.io/products/ethernet-chips/w5500) | ✅ приклади ioLibrary - там само |
| MCP2515 (CAN SPI) | Кварц 8 МГц, INT, термінатор 120 Ом | ✅ [MCP2515 Datasheet (PDF, Microchip)](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf) - регістри, маски/фільтри | ⚠️ *перевірити вручну* - сторінка продукту microchip.com блокує автозапити (403) | ✅ код mcp_can - у нотатці + [SN65HVD230 TI](https://www.ti.com/product/SN65HVD230) (трансивер до пари) |

### 1.8. LD2410 / UWB / IR / Voice ([[12-Moduli-zvyazku/08-LD2410-UWB-IR-Voice]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| LD2410 (HLK, 24 ГГц) | UART 256000 + OUT, гейти 0-8 | ✅ [HLK-LD2410 - Hi-Link](https://www.hlktech.net/index.php?id=988) - мануал, фото, параметри | ✅ та сама [сторінка Hi-Link](https://www.hlktech.net/index.php?id=988) - фото, ціна, файли | ✅ [LD2410 + ESP32 з кодом](https://how2electronics.com/ld2410-sensor-with-esp32-human-presence-detection/) - ld2410.h, гейти ✅ [LD2410 - ESPHome](https://esphome.io/components/sensor/ld2410.html) - YAML, калібрування |
| DWM1000 UWB (Decawave) | SPI, TWR, ±10 см | ⚠️ *перевірити вручну* - Decawave поглинуто Qorvo; шукати «DWM1000» на qorvo.com | ⚠️ *перевірити вручну* - сторінка Qorvo з фото | ✅ код TWR - у нотатці |
| VS1838B IR 38 кГц | RMT-декодер NEC/RC5 | ⚠️ *перевірити вручну* - виробники клонів без єдиного даташита | ⚠️ *перевірити вручну* - фото у продавців | ✅ код RMT - у нотатці |
| SU-03T (голос, офлайн) | UART 115200, прошивка WiseLight | ⚠️ *перевірити вручну* - шукати виробника голосового модуля | ⚠️ *перевірити вручну* - фото у продавців | ✅ код команд - у нотатці |

## 2. Живлення та рівні (`13-Moduli-zhivlennya-rivniv/`)

### 2.1. Buck / Boost / Solar ([[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| LM2596 (buck 3A) | 150 кГц, гріється, для 12V→5V | ✅ [LM2596 - TI](https://www.ti.com/product/LM2596) - даташит, WEBENCH-розрахунок | ✅ та сама [сторінка TI](https://www.ti.com/product/LM2596) - корпуси, EVM | ✅ налаштування підстроєчником - у нотатці |
| MP1584 (Mini360 buck) | Синхронний, 1.5 МГц, кращий ККД | ⚠️ *перевірити вручну* - сайт monolithicpower.com блокує автозапити; шукати «MP1584» на monolithicpower.com | ⚠️ *перевірити вручну* - сторінка MPS з фото | ✅ порівняння MP1584 vs LM2596 - у нотатці |
| MT3608 (boost) | Батарейка → 5V | ⚠️ *перевірити вручну* - шукати «MT3608» у виробника (Aerosemi) | ⚠️ *перевірити вручну* - фото модулів у продавців | ✅ схема boost-вузла - у нотатці |
| CN3791 (solar MPPT) | Сонце → Li-Ion, не TP4056 | ⚠️ *перевірити вручну* - шукати «CN3791» у виробника (Consonance) | ⚠️ *перевірити вручну* - фото модулів у продавців | ✅ сонячний вузол - у нотатці |

### 2.2. Level Shifters ([[13-Moduli-zhivlennya-rivniv/02-Level-Shifters]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| TXS0108E (8ch, I2C+SPI+UART) | Авто-напрям, 110 МГц | ✅ [TXS0108E - TI](https://www.ti.com/product/TXS0108E) - даташит, do's and don'ts | ✅ та сама [сторінка TI](https://www.ti.com/product/TXS0108E) - корпуси, EVM | ✅ [ESP32 Pinout (RNT)](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) - які піни 3.3V і чому потрібен shift |
| TXB0108 (8ch, push-pull) | Для SPI/UART, не для I2C з сильними pull-up | ✅ [TXB0108 - TI](https://www.ti.com/product/TXB0108) - даташит, відмінності від TXS | ✅ та сама [сторінка TI](https://www.ti.com/product/TXB0108) - корпуси | ✅ порівняльна таблиця - у нотатці |
| BSS138 (MOSFET, I2C) | Класика для I2C, 4ch модулі | ⚠️ *перевірити вручну* - шукати BSS138 у виробника MOSFET | ⚠️ *перевірити вручну* - фото 4-канальних модулів у продавців | ✅ схема I2C shift - у нотатці |
| PC817 (оптопара) | Гальваніка 220V/24V, повільна | ⚠️ *перевірити вручну* - шукати «PC817» у виробника (Sharp) | ⚠️ *перевірити вручну* - фото у продавців | ✅ схема розв'язки - у нотатці |

### 2.3. TP4056 / BMS / UPS ([[13-Moduli-zhivlennya-rivniv/03-TP4056-IP5306-BMS-UPS]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| TP4056 (+DW01+FS8205A) | Лінійний CC/CV 1A, тільки версія з OUT+- | ⚠️ *перевірити вручну* - єдиного вендора немає; шукати «TP4056 datasheet» | ⚠️ *перевірити вручну* - фото версій з/без захисту у продавців | ✅ [BQ24074 charger - TI](https://www.ti.com/product/BQ24074) - еталонний лінійний charger 1-cell з Power Path: фази CC/CV, termination (орієнтир для TP4056-вузла) |
| IP5306 (powerbank boost) | 5V 2.1A, KEY+LED | ⚠️ *перевірити вручну* - шукати «IP5306» у виробника (Injoinic) | ⚠️ *перевірити вручну* - фото плат у продавців | ✅ процедури - у нотатці |
| BMS 1S/2S/3S | 4.25V/2.5V, балансування для 2S+ | ⚠️ *перевірити вручну* - плати без єдиного вендора; шукати за маркуванням (HX-1S-01 тощо) | ⚠️ *перевірити вручну* - фото у продавців | ✅ схеми підключення - у нотатці |

### 2.4. LDO / Buck / Захист ([[13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| AMS1117-3.3 (LDO 1A) | Dropout 1.1V, гріється | ⚠️ *перевірити вручну* - шукати «AMS1117» у виробника (Advanced Monolithic) | ⚠️ *перевірити вручну* - фото у продавців | ✅ орієнтир-заміна: [TLV1117 - TI](https://www.ti.com/product/TLV1117) - pin-to-pin LDO 800 мА з даташитом |
| TLV1117 (LDO-референс) | 800 мА, для порівняння розрахунків | ✅ [TLV1117 - TI](https://www.ti.com/product/TLV1117) - даташит, теплові розрахунки | ✅ та сама [сторінка TI](https://www.ti.com/product/TLV1117) - корпуси | ✅ тепловий розрахунок - у нотатці |
| XL4015 (buck 5A CC/CV) | Для LED/свинцевих АКБ | ⚠️ *перевірити вручну* - шукати «XL4015» у виробника (XLSEMI) | ⚠️ *перевірити вручну* - фото модулів у продавців | ✅ налаштування CC/CV - у нотатці |
| LM2596 (buck 3A) | Див. 2.1 | ✅ [LM2596 - TI](https://www.ti.com/product/LM2596) | ✅ [сторінка TI](https://www.ti.com/product/LM2596) | ✅ у нотатці |
| Захист: PTC + TVS + MOSFET | Переполюсовка, перенапруга, КЗ | ✅ [TXS0108E ESD-розділ - TI](https://www.ti.com/product/TXS0108E) - орієнтир по ESD-захисту | ⚠️ *перевірити вручну* - TVS-діоди за місцем купівлі | ✅ схеми захисту - у нотатці |

### 2.5. USB-UART ([[13-Moduli-zhivlennya-rivniv/05-USB-UART-AutoReset]])

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| CH340C / CH340G | Дешевий міст, потрібен драйвер, G - кварц 12 МГц | ✅ [CH340 - WCH (оригінал)](https://www.wch.cn/products/CH340.html) - даташит, драйвери | ✅ [CH340 - WCH english](https://www.wch-ic.com/products/CH340.html) - фото, версії | ✅ auto-reset на 2 NPN - у нотатці |
| CP2102 / CP2104 | Стабільний, драйвер в ОС | ✅ [CP2102 - Silicon Labs](https://www.silabs.com/interface/usb-bridges/classic/device.cp2102) - даташит, VCP-драйвери | ✅ та сама [сторінка Silabs](https://www.silabs.com/interface/usb-bridges/classic/device.cp2102) - фото, EK | ✅ швидкості esptool - у нотатці |
| FT232RL | Дорогий, CBUS, клони цегляться | ⚠️ *перевірити вручну* - сайт ftdichip.com блокує автозапити (403); шукати «FT232RL» на ftdichip.com | ⚠️ *перевірити вручну* - сторінка FTDI з фото | ✅ порівняння мостів - у нотатці |

## 3. Залізо ESP32 (`01-Hardware/`)

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| ESP32 Classic D0WD-V3 ([[01-Hardware/01-ESP32-Classic]]) | LX6 240 МГц, BT 4.2, ADC2+WiFi конфлікт | ✅ [ESP32 Datasheet (PDF)](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) | ✅ [ESP32 - продукт](https://www.espressif.com/en/products/socs/esp32) | ✅ [ESP32 Pinout (RNT)](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) - ADC1/ADC2, strapping |
| ESP32-S2 ([[01-Hardware/02-ESP32-S2]]) | LX7 single, USB-OTG, без BT | ✅ [Техдокументація Espressif](https://www.espressif.com/en/support/download/documents) - S2 Datasheet+TRM | ✅ [ESP32-S2 - продукт](https://www.espressif.com/en/products/socs/esp32-s2) | ✅ [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/) - USB-OTG API |
| ESP32-S3 ([[01-Hardware/03-ESP32-S3]]) | LX7 dual, AI, USB-JTAG, Octal PSRAM | ✅ [Техдокументація Espressif](https://www.espressif.com/en/support/download/documents) - S3 Datasheet+TRM | ✅ [ESP32-S3 - продукт](https://www.espressif.com/en/products/socs/esp32-s3) | ✅ [ESP32-CAM відеострім (RNT)](https://randomnerdtutorials.com/esp32-cam-video-streaming-face-recognition-arduino-ide/) - камера DVP на S3 |
| ESP32-C3/C6/H2 ([[01-Hardware/04-ESP32-C3-C6-H2]]) | RISC-V, BLE 5, 802.15.4 (C6/H2) | ✅ [Техдокументація Espressif](https://www.espressif.com/en/support/download/documents) - C3/C6/H2 Datasheet | ✅ [C3](https://www.espressif.com/en/products/socs/esp32-c3) ✅ [C6](https://www.espressif.com/en/products/socs/esp32-c6) ✅ [H2](https://www.espressif.com/en/products/socs/esp32-h2) | ✅ [ESP32 BLE (RNT)](https://randomnerdtutorials.com/esp32-bluetooth-low-energy-ble-arduino-ide/) - BLE-база для C3/C6/H2 |
| WROOM / WROVER / MINI-1 ([[01-Hardware/05-Moduli-WROOM-WROVER-MINI]]) | Розміри, PSRAM, PCB/IPEX | ✅ [Техдокументація Espressif](https://www.espressif.com/en/support/download/documents) - даташити модулів | ✅ [ESP Modules](https://www.espressif.com/en/products/modules) - каталог з фото | ✅ [ESP32 Pinout (RNT)](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) - DevKit-піни |
| Flash / PSRAM ([[01-Hardware/06-Flash-PSRAM]]) | QD/QIO, 40/80 МГц, partitions | ✅ [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/) - SPI Flash API, partitions | ✅ [ESP32 - продукт](https://www.espressif.com/en/products/socs/esp32) - пам'ять | ⚠️ *перевірити вручну* - Winbond/GigaDevice/XMC даташити за маркуванням чипа |
| Boot / Strapping / Reset ([[01-Hardware/07-Boot-Strapping-Reset]]) | GPIO0/2/5/12/15, EN, download | ✅ [ESP32 Datasheet (PDF)](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) - розділ strapping | ✅ [Техдокументація Espressif](https://www.espressif.com/en/support/download/documents) - TRM (boot modes) | ✅ [ESP32 Pinout (RNT)](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) - strapping-таблиця з поясненнями |
| Антени / RF ([[01-Hardware/08-Anteni-RF]]) | PCB vs IPEX, keepout 15 мм | ✅ [Техдокументація Espressif](https://www.espressif.com/en/support/download/documents) - Hardware Design Guidelines (антени, EMC) | ✅ [ESP Modules](https://www.espressif.com/en/products/modules) - фото PCB/IPEX виконань | ✅ [nRF24L01 антени/дальність (LME)](https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/) - практики дальності, живлення RF |

## Див. також

- [[Home]]
- [[99-Dodatki/04-Datasheet-Links]] - ціни, де купити, література
- [[99-Dodatki/01-Pinout-tablici]]
- [[99-Dodatki/02-Troubleshooting-FAQ]]
- [[12-Moduli-zvyazku/01-RC522-RFID]]
- [[12-Moduli-zvyazku/02-NRF24-LoRa]]
- [[12-Moduli-zvyazku/03-SIM800L-GPS]]

> English twin: [[99-Dodatki/06-Official-Sources-Modules.en.md | EN]]
