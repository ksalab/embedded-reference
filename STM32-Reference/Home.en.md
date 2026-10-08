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
| Newcomer | [[00-Start/01-Yak-koristuvatis-dovidnikom.en | How to use]] → [[00-Start/02-Glosariy.en | Glossary]] → [[00-Start/03-Porivnyannya-chipiv.en | Chip comparison]] → [[00-Start/04-Devkit-plati.en | DevKit boards]] → [[00-Start/05-Vibir-seredovischa.en | Environment choice]] |

| Section | Topic | Notes |
| --- | --- | --- |
| `00-Start` | Start (5 notes) | [[00-Start/01-Yak-koristuvatis-dovidnikom.en | How to use]], [[00-Start/02-Glosariy.en | Glossary]], [[00-Start/03-Porivnyannya-chipiv.en | Chip comparison]], [[00-Start/04-Devkit-plati.en | DevKit boards]], [[00-Start/05-Vibir-seredovischa.en | Environment choice]] |
| `01-Hardware` | Chips (11 notes) | [[01-Hardware/01-F0-F1-Classic.en | F0/F1]], [[01-Hardware/02-F3-F4.en | F3/F4]], [[01-Hardware/03-G0-G4.en | G0/G4]], [[01-Hardware/04-H5-H7.en | H5/H7]], [[01-Hardware/05-L0-L4-U5.en | L0/L4/U5]], [[01-Hardware/06-WB-WL.en | WB/WL]], [[01-Hardware/07-Errata-Migratsiya.en | Errata]], [[01-Hardware/08-F7-Bridge.en | F7]], [[01-Hardware/09-H7-Deep.en | H7-deep]], [[01-Hardware/10-U5-Deep.en | U5-deep]], [[01-Hardware/11-STM32C0-Start.en | C0 start]] |
| `02-Zhivlennya` | Power supply (4 notes) | [[02-Zhivlennya/01-Lancjugi-zhivlennya.en | Power rails]], [[02-Zhivlennya/02-Batareyne-zhivlennya.en | Batteries]], [[02-Zhivlennya/03-Power-Design.en | Power design]], [[02-Zhivlennya/04-USB-C-PD.en | USB-C PD]] |
| `03-GPIO` | Pins (4 notes) | [[03-GPIO/01-GPIO-rezhimi.en | Modes]], [[03-GPIO/02-AF-maping.en | AF mapping]], [[03-GPIO/03-EXTI-NVIC.en | EXTI]], [[03-GPIO/04-NVIC-Priority-DeepDive.en | NVIC]] |
| `04-Shini` | Buses (8 notes) | [[04-Shini/01-UART.en | UART]], [[04-Shini/02-SPI.en | SPI]], [[04-Shini/03-I2C.en | I2C]], [[04-Shini/04-FDCAN.en | FDCAN]], [[04-Shini/05-USB.en | USB]], [[04-Shini/06-SDMMC-QUADSPI.en | SDMMC/QSPI]], [[04-Shini/07-DMA-DeepDive.en | DMA]], [[04-Shini/08-LIN-SMBus-I3C.en | LIN/SMBus]] |
| `05-Radio` | Radio (4 notes) | [[05-Radio/01-BLE-WB.en | BLE]], [[05-Radio/02-LoRaWAN-WL.en | LoRaWAN]], [[05-Radio/03-Antena-50ohm.en | Antenna]], [[05-Radio/04-LoRa-P2P.en | P2P]] |
| `06-Analog` | Analog (5 notes) | [[06-Analog/01-ADC.en | ADC]], [[06-Analog/02-DAC.en | DAC]], [[06-Analog/03-COMP-OPAMP.en | COMP/OPAMP]], [[06-Analog/04-DFSDM.en | DFSDM]], [[06-Analog/05-Shunt-OPAMP.en | Shunt]] |
| `07-Timeri-Son` | Timers and sleep (3 notes) | [[07-Timeri-Son/01-GPTIM-ADTIM.en | Timers]], [[07-Timeri-Son/02-LPTIM-RTC-WDT.en | LPTIM/RTC/WDT]], [[07-Timeri-Son/03-Sleep-Stop-Standby.en | Sleep]] |
| `08-Pamyat` | Memory (3 notes) | [[08-Pamyat/01-Flash-OTP-EEPROM.en | Flash and OTP]], [[08-Pamyat/02-Zovnishni-Loadery.en | Loaders]], [[08-Pamyat/03-Filesystem-LittleFS.en | Files]] |
| `09-Proshivka` | Firmware (8 notes) | [[09-Proshivka/01-CubeIDE-CubeMX.en | CubeIDE]], [[09-Proshivka/02-HAL-LL.en | HAL/LL]], [[09-Proshivka/03-ST-Link-Proshivka.en | ST-Link]], [[09-Proshivka/04-Bez-CubeIDE.en | Without CubeIDE]], [[09-Proshivka/05-Shablon-Drayvera.en | Driver]], [[09-Proshivka/06-FreeRTOS.en | RTOS]], [[09-Proshivka/07-Performance-Optimization.en | Performance]], [[09-Proshivka/08-CubeProgrammer-OB.en | CubeProgrammer]] |
| `10-Sensori` | Sensors (14 notes) | [[10-Sensori/01-DHT11-DS18B20.en | DHT11/DS18B20]], [[10-Sensori/02-BME280-SHT3x.en | BME280/SHT]], [[10-Sensori/03-MPU6050-IMU.en | MPU6050]], [[10-Sensori/04-INA219-HX711.en | INA219/HX711]], [[10-Sensori/05-HC-SR04-VL53L0X.en | HC-SR04/VL53L0X]], [[10-Sensori/06-Pressure-BMP-MS.en | Pressure]], [[10-Sensori/07-CO2-SCD-MHZ.en | CO2]], [[10-Sensori/08-Light-BH-TSL.en | Light]], [[10-Sensori/09-RFID-RC522.en | RFID]], [[10-Sensori/10-MQ-Gas.en | Gases]], [[10-Sensori/11-Encoder.en | Encoder]], [[10-Sensori/12-Strum-Potuzhnist.en | Current]], [[10-Sensori/13-Yakist-Povitrya.en | Air]], [[10-Sensori/14-Mag-Gesture-RTC.en | Compass/Gestures]] |
| `11-Vivid` | Outputs (9 notes) | [[11-Vivid/01-OLED-SSD1306.en | OLED]], [[11-Vivid/02-TFT-LCD.en | TFT]], [[11-Vivid/03-Servo-Rele-MOSFET-WS2812.en | Power]], [[11-Vivid/04-Epaper.en | E-paper]], [[11-Vivid/05-LVGL.en | LVGL]], [[11-Vivid/06-Stepper-TMC.en | Step]], [[11-Vivid/07-Indikatsiya-MAX7219.en | Indication]], [[11-Vivid/08-Audio-DFPlayer.en | Audio]], [[11-Vivid/09-FOC-BLDC.en | FOC motor]] |
| `12-Moduli-zvyazku` | Comms (9 notes) | [[12-Moduli-zvyazku/01-NRF24-LoRa.en | NRF24/LoRa]], [[12-Moduli-zvyazku/02-RS485-CAN-Ethernet.en | RS485/CAN/ETH]], [[12-Moduli-zvyazku/03-GPS-GSM.en | GPS/GSM]], [[12-Moduli-zvyazku/04-W5500.en | W5500]], [[12-Moduli-zvyazku/05-SIM7600.en | SIM7600]], [[12-Moduli-zvyazku/06-WiFi-ESP-AT.en | WiFi-AT]], [[12-Moduli-zvyazku/07-BLE-HC05-HM10.en | BT modules]], [[12-Moduli-zvyazku/08-DCMI-Camera.en | DCMI camera]], [[12-Moduli-zvyazku/09-LWIP-Ethernet.en | LWIP]] |
| `13-Moduli-zhivlennya-rivniv` | Power modules (3 notes) | [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost.en | Buck/Boost]], [[13-Moduli-zhivlennya-rivniv/02-Level-Shift.en | Levels]], [[13-Moduli-zhivlennya-rivniv/03-Charger-Protect.en | Charging]] |
| `14-Devboards` | Boards (6 notes) | [[14-Devboards/01-Blue-Pill.en | Blue Pill]], [[14-Devboards/02-Black-Pill.en | Black Pill]], [[14-Devboards/03-Nucleo.en | Nucleo]], [[14-Devboards/04-Discovery.en | Discovery]], [[14-Devboards/05-WeAct.en | WeAct]], [[14-Devboards/06-IoT-Discovery.en | IoT-Discovery]] |
| `15-Protokoli` | Protocols (6 notes) | [[15-Protokoli/01-Modbus.en | Modbus]], [[15-Protokoli/02-DFU-Bootloader.en | DFU]], [[15-Protokoli/03-Bezpeka.en | Security]], [[15-Protokoli/04-MQTT.en | MQTT]], [[15-Protokoli/05-CANopen.en | CANopen]], [[15-Protokoli/06-Secure-Boot.en | SecureBoot]] |
| `16-Proekti` | Projects (6 notes) | [[16-Proekti/01-Meteostantsiya.en | Weather]], [[16-Proekti/02-GPS-treker.en | Tracker]], [[16-Proekti/03-Energomonitor.en | Energy]], [[16-Proekti/04-Modbus-Gateway.en | Gateway]], [[16-Proekti/05-USB-Logger.en | Logger]], [[16-Proekti/06-Drone-FC.en | Drone]] |
| `17-Lab` | Lab (5 notes) | [[17-Lab/01-Priladi.en | Instruments]], [[17-Lab/02-Plata-PCB.en | Board]], [[17-Lab/03-Hardware-Design-Guidelines.en | Schematics]], [[17-Lab/04-EMI-EMC-Protection.en | EMI]], [[17-Lab/05-Maketka.en | Breadboard]] |
| `99-Dodatki` | Appendices (5 notes) | [[99-Dodatki/01-Troubleshooting-FAQ.en | FAQ]], [[99-Dodatki/02-Cheklisti.en | Checklists]], [[99-Dodatki/03-Datasheet-Links.en | Datasheets]], [[99-Dodatki/04-Diagnostic-Map.en | Map]], [[99-Dodatki/05-Pinout-Quickref.en | Pins]] |

## See also

- CHANGELOG
- TODO
