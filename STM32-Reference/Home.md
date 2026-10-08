---
title: STM32 Reference - головна карта довідника
description: STM32 головна карта навігація MOC чипи плати сенсори CubeIDE HAL LL
tags: [stm32, home, moc, navigation]
category: Meta
date-created: 2026-10-01
date: 2026-10-01
---

# STM32 Reference - головна карта довідника

> MOC всього довідника. Стандарт ноти: frontmatter, рисунок, mermaid, ASCII, код, помилки, джерела. Валідатори: `check_style` / `check_links` / `check_home` - усі в нуль.

| Маршрут | Ланцюжок |
| --- | --- |
| Новачок | [[00-Start/01-Yak-koristuvatis-dovidnikom | Як користуватись]] → [[00-Start/02-Glosariy | Глосарій]] → [[00-Start/03-Porivnyannya-chipiv | Порівняння чипів]] → [[00-Start/04-Devkit-plati | DevKit плати]] → [[00-Start/05-Vibir-seredovischa | Вибір середовища]] |

| Розділ | Тема | Ноти |
| --- | --- | --- |
| `00-Start` | Старт (5 нот) | [[00-Start/01-Yak-koristuvatis-dovidnikom | Як користуватись]], [[00-Start/02-Glosariy | Глосарій]], [[00-Start/03-Porivnyannya-chipiv | Порівняння чипів]], [[00-Start/04-Devkit-plati | DevKit плати]], [[00-Start/05-Vibir-seredovischa | Вибір середовища]] |
| `01-Hardware` | Чипи (11 нот) | [[01-Hardware/01-F0-F1-Classic | F0/F1]], [[01-Hardware/02-F3-F4 | F3/F4]], [[01-Hardware/03-G0-G4 | G0/G4]], [[01-Hardware/04-H5-H7 | H5/H7]], [[01-Hardware/05-L0-L4-U5 | L0/L4/U5]], [[01-Hardware/06-WB-WL | WB/WL]], [[01-Hardware/07-Errata-Migratsiya | Errata]], [[01-Hardware/08-F7-Bridge | F7]], [[01-Hardware/09-H7-Deep | H7-deep]], [[01-Hardware/10-U5-Deep | U5-deep]], [[01-Hardware/11-STM32C0-Start | C0-старт]] |
| `02-Zhivlennya` | Живлення (4 ноти) | [[02-Zhivlennya/01-Lancjugi-zhivlennya | Ланцюги]], [[02-Zhivlennya/02-Batareyne-zhivlennya | Батареї]], [[02-Zhivlennya/03-Power-Design | Живлення-дизайн]], [[02-Zhivlennya/04-USB-C-PD | USB-C PD]] |
| `03-GPIO` | Піни (4 ноти) | [[03-GPIO/01-GPIO-rezhimi | Режими]], [[03-GPIO/02-AF-maping | AF-мапінг]], [[03-GPIO/03-EXTI-NVIC | EXTI]], [[03-GPIO/04-NVIC-Priority-DeepDive | NVIC]] |
| `04-Shini` | Шини (8 нот) | [[04-Shini/01-UART | UART]], [[04-Shini/02-SPI | SPI]], [[04-Shini/03-I2C | I2C]], [[04-Shini/04-FDCAN | FDCAN]], [[04-Shini/05-USB | USB]], [[04-Shini/06-SDMMC-QUADSPI | SDMMC/QSPI]], [[04-Shini/07-DMA-DeepDive | DMA]], [[04-Shini/08-LIN-SMBus-I3C | LIN/SMBus]] |
| `05-Radio` | Радіо (4 ноти) | [[05-Radio/01-BLE-WB | BLE]], [[05-Radio/02-LoRaWAN-WL | LoRaWAN]], [[05-Radio/03-Antena-50ohm | Антена]], [[05-Radio/04-LoRa-P2P | P2P]] |
| `06-Analog` | Аналог (5 нот) | [[06-Analog/01-ADC | АЦП]], [[06-Analog/02-DAC | ЦАП]], [[06-Analog/03-COMP-OPAMP | COMP/OPAMP]], [[06-Analog/04-DFSDM | DFSDM]], [[06-Analog/05-Shunt-OPAMP | Шунт]] |
| `07-Timeri-Son` | Таймери і сон (3 ноти) | [[07-Timeri-Son/01-GPTIM-ADTIM | Таймери]], [[07-Timeri-Son/02-LPTIM-RTC-WDT | LPTIM/RTC/WDT]], [[07-Timeri-Son/03-Sleep-Stop-Standby | Сон]] |
| `08-Pamyat` | Пам'ять (3 ноти) | [[08-Pamyat/01-Flash-OTP-EEPROM | Flash і OTP]], [[08-Pamyat/02-Zovnishni-Loadery | Лоадери]], [[08-Pamyat/03-Filesystem-LittleFS | Файли]] |
| `09-Proshivka` | Прошивка (8 нот) | [[09-Proshivka/01-CubeIDE-CubeMX | CubeIDE]], [[09-Proshivka/02-HAL-LL | HAL/LL]], [[09-Proshivka/03-ST-Link-Proshivka | ST-Link]], [[09-Proshivka/04-Bez-CubeIDE | Без CubeIDE]], [[09-Proshivka/05-Shablon-Drayvera | Драйвер]], [[09-Proshivka/06-FreeRTOS | RTOS]], [[09-Proshivka/07-Performance-Optimization | Швидкодія]], [[09-Proshivka/08-CubeProgrammer-OB | CubeProgrammer]] |
| `10-Sensori` | Датчики (14 нот) | [[10-Sensori/01-DHT11-DS18B20 | DHT11/DS18B20]], [[10-Sensori/02-BME280-SHT3x | BME280/SHT]], [[10-Sensori/03-MPU6050-IMU | MPU6050]], [[10-Sensori/04-INA219-HX711 | INA219/HX711]], [[10-Sensori/05-HC-SR04-VL53L0X | HC-SR04/VL53L0X]], [[10-Sensori/06-Pressure-BMP-MS | Тиск]], [[10-Sensori/07-CO2-SCD-MHZ | CO2]], [[10-Sensori/08-Light-BH-TSL | Світло]], [[10-Sensori/09-RFID-RC522 | RFID]], [[10-Sensori/10-MQ-Gas | Гази]], [[10-Sensori/11-Encoder | Енкодер]], [[10-Sensori/12-Strum-Potuzhnist | Струм]], [[10-Sensori/13-Yakist-Povitrya | Повітря]], [[10-Sensori/14-Mag-Gesture-RTC | Компас/Жести]] |
| `11-Vivid` | Вивід (9 нот) | [[11-Vivid/01-OLED-SSD1306 | OLED]], [[11-Vivid/02-TFT-LCD | TFT]], [[11-Vivid/03-Servo-Rele-MOSFET-WS2812 | Сила]], [[11-Vivid/04-Epaper | Чорнила]], [[11-Vivid/05-LVGL | LVGL]], [[11-Vivid/06-Stepper-TMC | Крок]], [[11-Vivid/07-Indikatsiya-MAX7219 | Індикація]], [[11-Vivid/08-Audio-DFPlayer | Аудіо]], [[11-Vivid/09-FOC-BLDC | FOC-мотор]] |
| `12-Moduli-zvyazku` | Зв'язок (9 нот) | [[12-Moduli-zvyazku/01-NRF24-LoRa | NRF24/LoRa]], [[12-Moduli-zvyazku/02-RS485-CAN-Ethernet | RS485/CAN/ETH]], [[12-Moduli-zvyazku/03-GPS-GSM | GPS/GSM]], [[12-Moduli-zvyazku/04-W5500 | W5500]], [[12-Moduli-zvyazku/05-SIM7600 | SIM7600]], [[12-Moduli-zvyazku/06-WiFi-ESP-AT | WiFi-AT]], [[12-Moduli-zvyazku/07-BLE-HC05-HM10 | BT-модулі]], [[12-Moduli-zvyazku/08-DCMI-Camera | DCMI-камера]], [[12-Moduli-zvyazku/09-LWIP-Ethernet | LWIP]] |
| `13-Moduli-zhivlennya-rivniv` | Живлення-модулі (3 ноти) | [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost | Buck/Boost]], [[13-Moduli-zhivlennya-rivniv/02-Level-Shift | Рівні]], [[13-Moduli-zhivlennya-rivniv/03-Charger-Protect | Заряд]] |
| `14-Devboards` | Плати (6 нот) | [[14-Devboards/01-Blue-Pill | Blue Pill]], [[14-Devboards/02-Black-Pill | Black Pill]], [[14-Devboards/03-Nucleo | Nucleo]], [[14-Devboards/04-Discovery | Discovery]], [[14-Devboards/05-WeAct | WeAct]], [[14-Devboards/06-IoT-Discovery | IoT-Discovery]] |
| `15-Protokoli` | Протоколи (6 нот) | [[15-Protokoli/01-Modbus | Modbus]], [[15-Protokoli/02-DFU-Bootloader | DFU]], [[15-Protokoli/03-Bezpeka | Безпека]], [[15-Protokoli/04-MQTT | MQTT]], [[15-Protokoli/05-CANopen | CANopen]], [[15-Protokoli/06-Secure-Boot | SecureBoot]] |
| `16-Proekti` | Проєкти (6 нот) | [[16-Proekti/01-Meteostantsiya | Метео]], [[16-Proekti/02-GPS-treker | Трекер]], [[16-Proekti/03-Energomonitor | Енергія]], [[16-Proekti/04-Modbus-Gateway | Шлюз]], [[16-Proekti/05-USB-Logger | Логер]], [[16-Proekti/06-Drone-FC | Дрон]] |
| `17-Lab` | Лабораторія (5 нот) | [[17-Lab/01-Priladi | Прилади]], [[17-Lab/02-Plata-PCB | Плата]], [[17-Lab/03-Hardware-Design-Guidelines | Схемотехніка]], [[17-Lab/04-EMI-EMC-Protection | EMI]], [[17-Lab/05-Maketka | Макетка]] |
| `99-Dodatki` | Додатки (5 нот) | [[99-Dodatki/01-Troubleshooting-FAQ | FAQ]], [[99-Dodatki/02-Cheklisti | Чеклісти]], [[99-Dodatki/03-Datasheet-Links | Даташити]], [[99-Dodatki/04-Diagnostic-Map | Карта]], [[99-Dodatki/05-Pinout-Quickref | Піни]] |


## Див. також

- [[CHANGELOG]]
- [[TODO]]
