---
title: Arduino Reference - home map of the reference
description: Home MOC with reader paths and a section map that guides newcomers and makers; shows schematics, code and tables.
tags: [arduino, home, moc, navigation]
category: Meta
lang: en
original: Home.md
date-created: 2026-10-05
date: 2026-10-08
---

# Arduino Reference - home map of the reference

> MOC of the whole reference. Note standard: frontmatter, figure, mermaid, ASCII, code, issues, sources. Validators: `check_style` / `check_links` / `check_home` - all zero.

| Path | Chain |
| --- | --- |
| Newcomer | [[00-Start/01-Yak-koristuvatis-dovidnikom.en | How to use]] → [[00-Start/02-Glosariy.en | Glossary]] → [[00-Start/03-Porivnyannya-plat.en | Board comparison]] → [[00-Start/04-Devkit-plati.en | DevKit boards]] → [[00-Start/05-Vibir-seredovischa.en | Environment choice]] |

| Section | Topic | Notes |
| --- | --- | --- |
| `00-Start` | Start (5 notes) | [[00-Start/01-Yak-koristuvatis-dovidnikom.en | How to use]], [[00-Start/02-Glosariy.en | Glossary]], [[00-Start/03-Porivnyannya-plat.en | Board comparison]], [[00-Start/04-Devkit-plati.en | DevKit boards]], [[00-Start/05-Vibir-seredovischa.en | Environment choice]] |
| `01-Hardware` | Chips (5 notes) | [[01-Hardware/01-AVR-Uno.en | AVR-Uno]], [[01-Hardware/02-Nano-Mega.en | Nano-Mega]], [[01-Hardware/03-Due-Zero-ARM.en | Due-Zero]], [[01-Hardware/04-Uno-R4.en | Uno R4]], [[01-Hardware/05-Nano33-BLE-ARM.en | Nano 33 BLE]] |
| `02-Zhivlennya` | Power supply (2 notes) | [[02-Power-Supply/01-Zhivlennya-VIN.en | VIN]], [[02-Power-Supply/02-Batareyki.en | Batteries]] |
| `03-GPIO` | Pins (3 notes) | [[03-GPIO/01-Digital-pini.en | Digital]], [[03-GPIO/02-PWM-analogWrite.en | PWM]], [[03-GPIO/03-Pererivannya.en | Interrupts]] |
| `04-Shini` | Buses (4 notes) | [[04-Interfaces/01-UART.en | UART]], [[04-Interfaces/02-SPI.en | SPI]], [[04-Interfaces/03-I2C-Wire.en | I2C]], [[04-Interfaces/04-USB-AVR.en | USB]] |
| `05-Radio` | Radio (3 notes) | [[05-Radio/01-LoRa-moduli.en | LoRa]], [[05-Radio/02-GSM-SIM800.en | GSM]], [[05-Radio/03-GSM-Deep-HTTP.en | GSM deep]] |
| `06-Analog` | Analog (2 notes) | [[06-Analog/01-ADC.en | ADC]], [[06-Analog/02-DAC-nema.en | DAC workaround]] |
| `07-Timeri-Son` | Timers and sleep (3 notes) | [[07-Timers/01-Timeri-millis.en | Timers]], [[07-Timers/02-Son-WDT.en | Sleep]], [[07-Timers/03-Timeri-16bit-Deep.en | 16-bit]] |
| `08-Pamyat` | Memory (2 notes) | [[08-Memory/01-Pamyat-EEPROM.en | Memory]], [[08-Memory/02-SD-FatFS-Deep.en | SD-FatFS]] |
| `09-Proshivka` | Firmware (3 notes) | [[09-Firmware/01-IDE-CLI.en | IDE-CLI]], [[09-Firmware/02-Bootloader-AVRDUDE.en | Bootloader]], [[09-Firmware/03-PlatformIO.en | PlatformIO]] |
| `10-Sensori` | Sensors (12 notes) | [[10-Sensors/01-DHT-DS18B20.en | DHT/DS18B20]], [[10-Sensors/02-BME280.en | BME280]], [[10-Sensors/03-HC-SR04-PIR.en | HC-SR04/PIR]], [[10-Sensors/04-LM35-NTC.en | LM35/NTC]], [[10-Sensors/05-MPU6050.en | MPU6050]], [[10-Sensors/06-MQ-Gas.en | Gas sensors]], [[10-Sensors/07-RFID-RC522.en | RFID]], [[10-Sensors/08-Encoder.en | Encoder]], [[10-Sensors/09-Svitlo-Tisk-ToF.en | Light/Pressure]], [[10-Sensors/10-Strum-INA219.en | Current]], [[10-Sensors/11-CO2-Povitrya.en | CO2]], [[10-Sensors/12-Mag-Gesture-RTC.en | Compass/Gestures]] |
| `11-Vivid` | Output (8 notes) | [[11-Vivid/01-LCD1602.en | LCD1602]], [[11-Vivid/02-OLED-SSD1306.en | OLED]], [[11-Vivid/03-NeoPixel-Servo-Rele.en | Power outputs]], [[11-Vivid/04-TFT-ST7735.en | TFT]], [[11-Vivid/05-Servo-Motor-L298N.en | Motor]], [[11-Vivid/06-Indikatsiya-Audio.en | Indication]], [[11-Vivid/07-TFT-Touch-Deep.en | TFT deep]], [[11-Vivid/08-Nextion-HMI.en | Nextion]] |
| `12-Moduli-zvyazku` | Comms (6 notes) | [[12-Comm-Modules/01-NRF24.en | NRF24]], [[12-Comm-Modules/02-RC522-RFID.en | RC522]], [[12-Comm-Modules/03-ESP8266-WiFi.en | ESP WiFi]], [[12-Comm-Modules/04-GPS-NEO.en | GPS]], [[12-Comm-Modules/05-BT-Ethernet.en | BT/Ethernet]], [[12-Comm-Modules/06-Ethernet-W5500-Deep.en | Ethernet deep]] |
| `13-Moduli-zhivlennya-rivniv` | Power modules (2 notes) | [[13-Power-Modules/01-Buck-peretvoryuvach.en | Buck]], [[13-Power-Modules/02-Level-Shift-TP4056.en | Levels]] |
| `14-Devboards` | Boards (4 notes) | [[14-Devboards/01-Shildi.en | Shields]], [[14-Devboards/02-Kloni-CH340.en | Clones]], [[14-Devboards/03-Nano-ESP32-GIGA.en | Flagships]], [[14-Devboards/04-RP2040.en | RP2040]] |
| `15-Protokoli` | Protocols (3 notes) | [[15-Protocols/01-Modbus.en | Modbus]], [[15-Protocols/02-MQTT-ESP.en | MQTT]], [[15-Protocols/03-HTTP-Web.en | HTTP client]] |
| `16-Proekti` | Projects (4 notes) | [[16-Projects/01-Meteostantsiya.en | Weather station]], [[16-Projects/02-Rozumniy-dim.en | Smart home]], [[16-Projects/03-Treker.en | Tracker]], [[16-Projects/04-Loger-SD.en | Logger]] |
| `17-Lab` | Lab (2 notes) | [[17-Lab/01-Priladi.en | Instruments]], [[17-Lab/02-Maketka-PCB.en | Breadboard]] |
| `99-Dodatki` | Appendices (3 notes) | [[99-Additions/01-Troubleshooting-FAQ.en | FAQ]], [[99-Additions/02-Cheklisti-Datasheet.en | Checklists]], [[99-Additions/03-Diagnostic-Map.en | Map]] |
