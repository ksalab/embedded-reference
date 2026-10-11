---
title: STM32 Reference - reference home map
description: Entry map of the STM32 reference covering chip choice, boards, power, GPIO, buses, sensors and firmware; shows schematics, code and tables.
tags: [stm32, home, moc, navigation]
category: Meta
lang: en
original: Home.md
date-created: 2026-10-01
date: 2026-10-08
---

# STM32 Reference - reference home map

> MOC of the whole reference. Note standard: frontmatter, figure, mermaid, ASCII, code, issues, sources. Validators: `check_style` / `check_links` / `check_home` - all report zero.

| Path | Chain |
| --- | --- |
| Newcomer | [[EN/00-Start/01-How-to-Use-Guide.en| How to use]] → [[EN/00-Start/02-Glossary.en| Glossary]] → [[EN/00-Start/03-Chip-Comparison.en| Chip comparison]] → [[EN/00-Start/04-Dev-Boards.en| DevKit boards]] → [[EN/00-Start/05-Environment-Choice.en| Environment choice]] |

| Section | Topic | Notes |
| --- | --- | --- |
| `EN/00-Start` | Start (5 notes) | [[EN/00-Start/01-How-to-Use-Guide.en| How to use]], [[EN/00-Start/02-Glossary.en| Glossary]], [[EN/00-Start/03-Chip-Comparison.en| Chip comparison]], [[EN/00-Start/04-Dev-Boards.en| DevKit boards]], [[EN/00-Start/05-Environment-Choice.en| Environment choice]] |
| `EN/01-Hardware` | Chips (11 notes) | [[EN/01-Hardware/01-F0-F1-Classic.en| F0/F1]], [[EN/01-Hardware/02-F3-F4.en| F3/F4]], [[EN/01-Hardware/03-G0-G4.en| G0/G4]], [[EN/01-Hardware/04-H5-H7.en| H5/H7]], [[EN/01-Hardware/05-L0-L4-U5.en| L0/L4/U5]], [[EN/01-Hardware/06-WB-WL.en| WB/WL]], [[EN/01-Hardware/07-Errata-Migration.en| Errata]], [[EN/01-Hardware/08-F7-Bridge.en| F7]], [[EN/01-Hardware/09-H7-Deep.en| H7-deep]], [[EN/01-Hardware/10-U5-Deep.en| U5-deep]], [[EN/01-Hardware/11-STM32C0-Start.en| C0 start]] |
| `EN/02-Power-Supply` | Power supply (4 notes) | [[EN/02-Power-Supply/01-Power-Supply-Rails.en| Power rails]], [[EN/02-Power-Supply/02-Battery-Power.en| Batteries]], [[EN/02-Power-Supply/03-Power-Design.en| Power design]], [[EN/02-Power-Supply/04-USB-C-PD.en| USB-C PD]] |
| `EN/03-GPIO` | Pins (4 notes) | [[EN/03-GPIO/01-GPIO-Modes.en| Modes]], [[EN/03-GPIO/02-AF-Mapping.en| AF mapping]], [[EN/03-GPIO/03-EXTI-NVIC.en| EXTI]], [[EN/03-GPIO/04-NVIC-Priority-DeepDive.en| NVIC]] |
| `EN/04-Interfaces` | Buses (8 notes) | [[EN/04-Interfaces/01-UART.en| UART]], [[EN/04-Interfaces/02-SPI.en| SPI]], [[EN/04-Interfaces/03-I2C.en| I2C]], [[EN/04-Interfaces/04-FDCAN.en| FDCAN]], [[EN/04-Interfaces/05-USB.en| USB]], [[EN/04-Interfaces/06-SDMMC-QUADSPI.en| SDMMC/QSPI]], [[EN/04-Interfaces/07-DMA-DeepDive.en| DMA]], [[EN/04-Interfaces/08-LIN-SMBus-I3C.en| LIN/SMBus]] |
| `EN/05-Radio` | Radio (4 notes) | [[EN/05-Radio/01-BLE-WB.en| BLE]], [[EN/05-Radio/02-LoRaWAN-WL.en| LoRaWAN]], [[EN/05-Radio/03-Antenna-50ohm.en| Antenna]], [[EN/05-Radio/04-LoRa-P2P.en| P2P]] |
| `EN/06-Analog` | Analog (5 notes) | [[EN/06-Analog/01-ADC.en| ADC]], [[EN/06-Analog/02-DAC.en| DAC]], [[EN/06-Analog/03-COMP-OPAMP.en| COMP/OPAMP]], [[EN/06-Analog/04-DFSDM.en| DFSDM]], [[EN/06-Analog/05-Shunt-OPAMP.en| Shunt]] |
| `EN/07-Timers` | Timers and sleep (3 notes) | [[EN/07-Timers/01-GPTIM-ADTIM.en| Timers]], [[EN/07-Timers/02-LPTIM-RTC-WDT.en| LPTIM/RTC/WDT]], [[EN/07-Timers/03-Sleep-Stop-Standby.en| Sleep]] |
| `EN/08-Memory` | Memory (3 notes) | [[EN/08-Memory/01-Flash-OTP-EEPROM.en| Flash and OTP]], [[EN/08-Memory/02-External-Loaders.en| Loaders]], [[EN/08-Memory/03-Filesystem-LittleFS.en| Files]] |
| `EN/09-Firmware` | Firmware (8 notes) | [[EN/09-Firmware/01-CubeIDE-CubeMX.en| CubeIDE]], [[EN/09-Firmware/02-HAL-LL.en| HAL/LL]], [[EN/09-Firmware/03-ST-Link-Flashing.en| ST-Link]], [[EN/09-Firmware/04-Without-CubeIDE.en| Without CubeIDE]], [[EN/09-Firmware/05-Driver-Template.en| Driver]], [[EN/09-Firmware/06-FreeRTOS.en| RTOS]], [[EN/09-Firmware/07-Performance-Optimization.en| Performance]], [[EN/09-Firmware/08-CubeProgrammer-OB.en| CubeProgrammer]] |
| `EN/10-Sensors` | Sensors (14 notes) | [[EN/10-Sensors/01-DHT11-DS18B20.en| DHT11/DS18B20]], [[EN/10-Sensors/02-BME280-SHT3x.en| BME280/SHT]], [[EN/10-Sensors/03-MPU6050-IMU.en| MPU6050]], [[EN/10-Sensors/04-INA219-HX711.en| INA219/HX711]], [[EN/10-Sensors/05-HC-SR04-VL53L0X.en| HC-SR04/VL53L0X]], [[EN/10-Sensors/06-Pressure-BMP390-MS5611.en| Pressure]], [[EN/10-Sensors/07-CO2-SCD40-MH-Z19.en| CO2]], [[EN/10-Sensors/08-Light-BH1750-TSL2591.en| Light]], [[EN/10-Sensors/09-RFID-RC522.en| RFID]], [[EN/10-Sensors/10-MQ-Gas.en| Gases]], [[EN/10-Sensors/11-Encoder.en| Encoder]], [[EN/10-Sensors/12-Current-Power.en| Current]], [[EN/10-Sensors/13-Air-Quality.en| Air]], [[EN/10-Sensors/14-Mag-Gesture-RTC.en| Compass/Gestures]] |
| `EN/11-Vivid` | Outputs (9 notes) | [[EN/11-Vivid/01-OLED-SSD1306.en| OLED]], [[EN/11-Vivid/02-TFT-LCD.en| TFT]], [[EN/11-Vivid/03-Servo-Relay-MOSFET-WS2812.en| Power]], [[EN/11-Vivid/04-Epaper.en| E-paper]], [[EN/11-Vivid/05-LVGL.en| LVGL]], [[EN/11-Vivid/06-Stepper-TMC.en| Step]], [[EN/11-Vivid/07-LED-Indication-MAX7219.en| Indication]], [[EN/11-Vivid/08-Audio-DFPlayer.en| Audio]], [[EN/11-Vivid/09-FOC-BLDC.en| FOC motor]] |
| `EN/12-Comm-Modules` | Comms (9 notes) | [[EN/12-Comm-Modules/01-NRF24-LoRa.en| NRF24/LoRa]], [[EN/12-Comm-Modules/02-RS485-CAN-Ethernet.en| RS485/CAN/ETH]], [[EN/12-Comm-Modules/03-GPS-GSM.en| GPS/GSM]], [[EN/12-Comm-Modules/04-W5500.en| W5500]], [[EN/12-Comm-Modules/05-SIM7600.en| SIM7600]], [[EN/12-Comm-Modules/06-WiFi-ESP-AT.en| WiFi-AT]], [[EN/12-Comm-Modules/07-BLE-HC05-HM10.en| BT modules]], [[EN/12-Comm-Modules/08-DCMI-Camera.en| DCMI camera]], [[EN/12-Comm-Modules/09-LWIP-Ethernet.en| LWIP]] |
| `EN/13-Power-Modules` | Power modules (3 notes) | [[EN/13-Power-Modules/01-Buck-Boost.en| Buck/Boost]], [[EN/13-Power-Modules/02-Level-Shift.en| Levels]], [[EN/13-Power-Modules/03-Charger-Protection.en| Charging]] |
| `EN/14-Devboards` | Boards (6 notes) | [[EN/14-Devboards/01-Blue-Pill.en| Blue Pill]], [[EN/14-Devboards/02-Black-Pill.en| Black Pill]], [[EN/14-Devboards/03-Nucleo.en| Nucleo]], [[EN/14-Devboards/04-Discovery.en| Discovery]], [[EN/14-Devboards/05-WeAct.en| WeAct]], [[EN/14-Devboards/06-IoT-Discovery.en| IoT-Discovery]] |
| `EN/15-Protocols` | Protocols (6 notes) | [[EN/15-Protocols/01-Modbus.en| Modbus]], [[EN/15-Protocols/02-DFU-Bootloader.en| DFU]], [[EN/15-Protocols/03-Security.en| Security]], [[EN/15-Protocols/04-MQTT.en| MQTT]], [[EN/15-Protocols/05-CANopen.en| CANopen]], [[EN/15-Protocols/06-Secure-Boot.en| SecureBoot]] |
| `EN/16-Projects` | Projects (6 notes) | [[EN/16-Projects/01-Weather-Station.en| Weather]], [[EN/16-Projects/02-GPS-Tracker.en| Tracker]], [[EN/16-Projects/03-Energy-Monitor.en| Energy]], [[EN/16-Projects/04-Modbus-Gateway.en| Gateway]], [[EN/16-Projects/05-USB-Logger.en| Logger]], [[EN/16-Projects/06-Drone-FC.en| Drone]] |
| `EN/17-Lab` | Lab (5 notes) | [[EN/17-Lab/01-Instruments.en| Instruments]], [[EN/17-Lab/02-PCB-Board.en| Board]], [[EN/17-Lab/03-Hardware-Design-Guidelines.en| Schematics]], [[EN/17-Lab/04-EMI-EMC-Protection.en| EMI]], [[EN/17-Lab/05-Breadboard.en| Breadboard]] |
| `EN/99-Additions` | Appendices (5 notes) | [[EN/99-Additions/01-Troubleshooting-FAQ.en| FAQ]], [[EN/99-Additions/02-Cheklisti.en| Checklists]], [[EN/99-Additions/03-Datasheet-Links.en| Datasheets]], [[EN/99-Additions/04-Diagnostic-Map.en| Map]], [[EN/99-Additions/05-Pinout-Quickref.en| Pins]] |

## See also

- CHANGELOG
- TODO
