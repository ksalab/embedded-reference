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
| Newcomer | [[EN/00-Start/01-How-to-Use-Guide.en| How to use]] → [[EN/00-Start/02-Glossary.en| Glossary]] → [[EN/00-Start/03-Board-Comparison.en| Board comparison]] → [[EN/00-Start/04-Dev-Boards.en| DevKit boards]] → [[EN/00-Start/05-Environment-Choice.en| Environment choice]] |

| Section | Topic | Notes |
| --- | --- | --- |
| `EN/00-Start` | Start (5 notes) | [[EN/00-Start/01-How-to-Use-Guide.en| How to use]], [[EN/00-Start/02-Glossary.en| Glossary]], [[EN/00-Start/03-Board-Comparison.en| Board comparison]], [[EN/00-Start/04-Dev-Boards.en| DevKit boards]], [[EN/00-Start/05-Environment-Choice.en| Environment choice]] |
| `EN/01-Hardware` | Chips (5 notes) | [[EN/01-Hardware/01-AVR-Uno.en| AVR-Uno]], [[EN/01-Hardware/02-Nano-Mega.en| Nano-Mega]], [[EN/01-Hardware/03-Due-Zero-ARM.en| Due-Zero]], [[EN/01-Hardware/04-Uno-R4.en| Uno R4]], [[EN/01-Hardware/05-Nano33-BLE-ARM.en| Nano 33 BLE]] |
| `EN/02-Power-Supply` | Power supply (2 notes) | [[EN/02-Power-Supply/01-VIN-Power-Supply.en| VIN]], [[EN/02-Power-Supply/02-Battery-Power.en| Batteries]] |
| `EN/03-GPIO` | Pins (3 notes) | [[EN/03-GPIO/01-Digital-Pins.en| Digital]], [[EN/03-GPIO/02-PWM-analogWrite.en| PWM]], [[EN/03-GPIO/03-Interrupts.en| Interrupts]] |
| `EN/04-Interfaces` | Buses (4 notes) | [[EN/04-Interfaces/01-UART.en| UART]], [[EN/04-Interfaces/02-SPI.en| SPI]], [[EN/04-Interfaces/03-I2C-Wire.en| I2C]], [[EN/04-Interfaces/04-USB-AVR.en| USB]] |
| `EN/05-Radio` | Radio (3 notes) | [[EN/05-Radio/01-LoRa-Modules.en| LoRa]], [[EN/05-Radio/02-GSM-SIM800.en| GSM]], [[EN/05-Radio/03-GSM-Deep-HTTP.en| GSM deep]] |
| `EN/06-Analog` | Analog (2 notes) | [[EN/06-Analog/01-ADC.en| ADC]], [[EN/06-Analog/02-No-DAC.en| DAC workaround]] |
| `EN/07-Timers` | Timers and sleep (3 notes) | [[EN/07-Timers/01-Timers-millis.en| Timers]], [[EN/07-Timers/02-Sleep-WDT.en| Sleep]], [[EN/07-Timers/03-16bit-Timers-Deep.en| 16-bit]] |
| `EN/08-Memory` | Memory (2 notes) | [[EN/08-Memory/01-Memory-EEPROM.en| Memory]], [[EN/08-Memory/02-SD-FatFS-Deep.en| SD-FatFS]] |
| `EN/09-Firmware` | Firmware (3 notes) | [[EN/09-Firmware/01-IDE-CLI.en| IDE-CLI]], [[EN/09-Firmware/02-Bootloader-AVRDUDE.en| Bootloader]], [[EN/09-Firmware/03-PlatformIO.en| PlatformIO]] |
| `EN/10-Sensors` | Sensors (12 notes) | [[EN/10-Sensors/01-DHT-DS18B20.en| DHT/DS18B20]], [[EN/10-Sensors/02-BME280.en| BME280]], [[EN/10-Sensors/03-HC-SR04-PIR.en| HC-SR04/PIR]], [[EN/10-Sensors/04-LM35-NTC.en| LM35/NTC]], [[EN/10-Sensors/05-MPU6050.en| MPU6050]], [[EN/10-Sensors/06-MQ-Gas.en| Gas sensors]], [[EN/10-Sensors/07-RFID-RC522.en| RFID]], [[EN/10-Sensors/08-Encoder.en| Encoder]], [[EN/10-Sensors/09-Light-Pressure-ToF.en| Light/Pressure]], [[EN/10-Sensors/10-Current-INA219.en| Current]], [[EN/10-Sensors/11-CO2-Air.en| CO2]], [[EN/10-Sensors/12-Mag-Gesture-RTC.en| Compass/Gestures]] |
| `EN/11-Vivid` | Output (8 notes) | [[EN/11-Vivid/01-LCD1602.en| LCD1602]], [[EN/11-Vivid/02-OLED-SSD1306.en| OLED]], [[EN/11-Vivid/03-NeoPixel-Servo-Relay.en| Power outputs]], [[EN/11-Vivid/04-TFT-ST7735.en| TFT]], [[EN/11-Vivid/05-Servo-Motor-L298N.en| Motor]], [[EN/11-Vivid/06-Indicator-Audio.en| Indication]], [[EN/11-Vivid/07-TFT-Touch-Deep.en| TFT deep]], [[EN/11-Vivid/08-Nextion-HMI.en| Nextion]] |
| `EN/12-Comm-Modules` | Comms (6 notes) | [[EN/12-Comm-Modules/01-NRF24.en| NRF24]], [[EN/12-Comm-Modules/02-RC522-RFID.en| RC522]], [[EN/12-Comm-Modules/03-ESP8266-WiFi.en| ESP WiFi]], [[EN/12-Comm-Modules/04-GPS-NEO.en| GPS]], [[EN/12-Comm-Modules/05-BT-Ethernet.en| BT/Ethernet]], [[EN/12-Comm-Modules/06-Ethernet-W5500-Deep.en| Ethernet deep]] |
| `EN/13-Power-Modules` | Power modules (2 notes) | [[EN/13-Power-Modules/01-Buck-Converter.en| Buck]], [[EN/13-Power-Modules/02-Level-Shift-TP4056.en| Levels]] |
| `EN/14-Devboards` | Boards (4 notes) | [[EN/14-Devboards/01-Shields.en| Shields]], [[EN/14-Devboards/02-Clones-CH340.en| Clones]], [[EN/14-Devboards/03-Nano-ESP32-GIGA.en| Flagships]], [[EN/14-Devboards/04-RP2040.en| RP2040]] |
| `EN/15-Protocols` | Protocols (3 notes) | [[EN/15-Protocols/01-Modbus.en| Modbus]], [[EN/15-Protocols/02-MQTT-ESP.en| MQTT]], [[EN/15-Protocols/03-HTTP-Web.en| HTTP client]] |
| `EN/16-Proekti` | Projects (4 notes) | [[EN/16-Proekti/01-Weather-Station.en| Weather station]], [[EN/16-Proekti/02-Smart-Home.en| Smart home]], [[EN/16-Proekti/03-Tracker.en| Tracker]], [[EN/16-Proekti/04-SD-Logger.en| Logger]] |
| `EN/17-Lab` | Lab (2 notes) | [[EN/17-Lab/01-Instruments.en| Instruments]], [[EN/17-Lab/02-Breadboard-PCB.en| Breadboard]] |
| `EN/99-Additions` | Appendices (3 notes) | [[EN/99-Additions/01-Troubleshooting-FAQ.en| FAQ]], [[EN/99-Additions/02-Cheklisti-Datasheet.en| Checklists]], [[EN/99-Additions/03-Diagnostic-Map.en| Map]] |
