---
title: STM32 Reference - головна карта довідника
description: STM32 головна карта навігація MOC чипи плати сенсори CubeIDE HAL LL
tags: [stm32, home, moc, navigation]
category: Meta
date-created: 2026-10-01
date: 2026-10-01
---

# STM32 Reference - головна карта довідника

EN version: `Home.en.md`

> MOC всього довідника. Стандарт ноти: frontmatter, рисунок, mermaid, ASCII, код, помилки, джерела. Валідатори: `check_style` / `check_links` / `check_home` - усі в нуль.

| Маршрут | Ланцюжок |
| --- | --- |
| Новачок | [[UA/00-Start/01-Yak-koristuvatis-dovidnikom| Як користуватись]] → [[UA/00-Start/02-Glosariy| Глосарій]] → [[UA/00-Start/03-Porivnyannya-chipiv| Порівняння чипів]] → [[UA/00-Start/04-Devkit-plati| DevKit плати]] → [[UA/00-Start/05-Vibir-seredovischa| Вибір середовища]] |

| Розділ | Тема | Ноти |
| --- | --- | --- |
| `UA/00-Start` | Старт (5 нот) | [[UA/00-Start/01-Yak-koristuvatis-dovidnikom| Як користуватись]], [[UA/00-Start/02-Glosariy| Глосарій]], [[UA/00-Start/03-Porivnyannya-chipiv| Порівняння чипів]], [[UA/00-Start/04-Devkit-plati| DevKit плати]], [[UA/00-Start/05-Vibir-seredovischa| Вибір середовища]] |
| `UA/01-Hardware` | Чипи (11 нот) | [[UA/01-Hardware/01-F0-F1-Classic| F0/F1]], [[UA/01-Hardware/02-F3-F4| F3/F4]], [[UA/01-Hardware/03-G0-G4| G0/G4]], [[UA/01-Hardware/04-H5-H7| H5/H7]], [[UA/01-Hardware/05-L0-L4-U5| L0/L4/U5]], [[UA/01-Hardware/06-WB-WL| WB/WL]], [[UA/01-Hardware/07-Errata-Migratsiya| Errata]], [[UA/01-Hardware/08-F7-Bridge| F7]], [[UA/01-Hardware/09-H7-Deep| H7-deep]], [[UA/01-Hardware/10-U5-Deep| U5-deep]], [[UA/01-Hardware/11-STM32C0-Start| C0-старт]] |
| `UA/02-Zhivlennya` | Живлення (4 нот) | [[UA/02-Zhivlennya/01-Lancjugi-zhivlennya| Ланцюги]], [[UA/02-Zhivlennya/02-Batareyne-zhivlennya| Батареї]], [[UA/02-Zhivlennya/03-Power-Design| Живлення-дизайн]], [[UA/02-Zhivlennya/04-USB-C-PD| USB-C PD]] |
| `UA/03-GPIO` | Піни (4 нот) | [[UA/03-GPIO/01-GPIO-rezhimi| Режими]], [[UA/03-GPIO/02-AF-maping| AF-мапінг]], [[UA/03-GPIO/03-EXTI-NVIC| EXTI]], [[UA/03-GPIO/04-NVIC-Priority-DeepDive| NVIC]] |
| `UA/04-Shini` | Шини (8 нот) | [[UA/04-Shini/01-UART| UART]], [[UA/04-Shini/02-SPI| SPI]], [[UA/04-Shini/03-I2C| I2C]], [[UA/04-Shini/04-FDCAN| FDCAN]], [[UA/04-Shini/05-USB| USB]], [[UA/04-Shini/06-SDMMC-QUADSPI| SDMMC/QSPI]], [[UA/04-Shini/07-DMA-DeepDive| DMA]], [[UA/04-Shini/08-LIN-SMBus-I3C| LIN/SMBus]] |
| `UA/05-Radio` | Радіо (4 нот) | [[UA/05-Radio/01-BLE-WB| BLE]], [[UA/05-Radio/02-LoRaWAN-WL| LoRaWAN]], [[UA/05-Radio/03-Antena-50ohm| Антена]], [[UA/05-Radio/04-LoRa-P2P| P2P]] |
| `UA/06-Analog` | Аналог (5 нот) | [[UA/06-Analog/01-ADC| АЦП]], [[UA/06-Analog/02-DAC| ЦАП]], [[UA/06-Analog/03-COMP-OPAMP| COMP/OPAMP]], [[UA/06-Analog/04-DFSDM| DFSDM]], [[UA/06-Analog/05-Shunt-OPAMP| Шунт]] |
| `UA/07-Timeri-Son` | Таймери і сон (3 нот) | [[UA/07-Timeri-Son/01-GPTIM-ADTIM| Таймери]], [[UA/07-Timeri-Son/02-LPTIM-RTC-WDT| LPTIM/RTC/WDT]], [[UA/07-Timeri-Son/03-Sleep-Stop-Standby| Сон]] |
| `UA/08-Pamyat` | Пам'ять (3 нот) | [[UA/08-Pamyat/01-Flash-OTP-EEPROM| Flash і OTP]], [[UA/08-Pamyat/02-Zovnishni-Loadery| Лоадери]], [[UA/08-Pamyat/03-Filesystem-LittleFS| Файли]] |
| `UA/09-Proshivka` | Прошивка (8 нот) | [[UA/09-Proshivka/01-CubeIDE-CubeMX| CubeIDE]], [[UA/09-Proshivka/02-HAL-LL| HAL/LL]], [[UA/09-Proshivka/03-ST-Link-Proshivka| ST-Link]], [[UA/09-Proshivka/04-Bez-CubeIDE| Без CubeIDE]], [[UA/09-Proshivka/05-Shablon-Drayvera| Драйвер]], [[UA/09-Proshivka/06-FreeRTOS| RTOS]], [[UA/09-Proshivka/07-Performance-Optimization| Швидкодія]], [[UA/09-Proshivka/08-CubeProgrammer-OB| CubeProgrammer]] |
| `UA/10-Sensori` | Датчики (14 нот) | [[UA/10-Sensori/01-DHT11-DS18B20| DHT11/DS18B20]], [[UA/10-Sensori/02-BME280-SHT3x| BME280/SHT]], [[UA/10-Sensori/03-MPU6050-IMU| MPU6050]], [[UA/10-Sensori/04-INA219-HX711| INA219/HX711]], [[UA/10-Sensori/05-HC-SR04-VL53L0X| HC-SR04/VL53L0X]], [[UA/10-Sensori/06-Pressure-BMP-MS| Тиск]], [[UA/10-Sensori/07-CO2-SCD-MHZ| CO2]], [[UA/10-Sensori/08-Light-BH-TSL| Світло]], [[UA/10-Sensori/09-RFID-RC522| RFID]], [[UA/10-Sensori/10-MQ-Gas| Гази]], [[UA/10-Sensori/11-Encoder| Енкодер]], [[UA/10-Sensori/12-Strum-Potuzhnist| Струм]], [[UA/10-Sensori/13-Yakist-Povitrya| Повітря]], [[UA/10-Sensori/14-Mag-Gesture-RTC| Компас/Жести]] |
| `UA/11-Vivid` | Вивід (9 нот) | [[UA/11-Vivid/01-OLED-SSD1306| OLED]], [[UA/11-Vivid/02-TFT-LCD| TFT]], [[UA/11-Vivid/03-Servo-Rele-MOSFET-WS2812| Сила]], [[UA/11-Vivid/04-Epaper| Чорнила]], [[UA/11-Vivid/05-LVGL| LVGL]], [[UA/11-Vivid/06-Stepper-TMC| Крок]], [[UA/11-Vivid/07-Indikatsiya-MAX7219| Індикація]], [[UA/11-Vivid/08-Audio-DFPlayer| Аудіо]], [[UA/11-Vivid/09-FOC-BLDC| FOC-мотор]] |
| `UA/12-Moduli-zvyazku` | Зв'язок (9 нот) | [[UA/12-Moduli-zvyazku/01-NRF24-LoRa| NRF24/LoRa]], [[UA/12-Moduli-zvyazku/02-RS485-CAN-Ethernet| RS485/CAN/ETH]], [[UA/12-Moduli-zvyazku/03-GPS-GSM| GPS/GSM]], [[UA/12-Moduli-zvyazku/04-W5500| W5500]], [[UA/12-Moduli-zvyazku/05-SIM7600| SIM7600]], [[UA/12-Moduli-zvyazku/06-WiFi-ESP-AT| WiFi-AT]], [[UA/12-Moduli-zvyazku/07-BLE-HC05-HM10| BT-модулі]], [[UA/12-Moduli-zvyazku/08-DCMI-Camera| DCMI-камера]], [[UA/12-Moduli-zvyazku/09-LWIP-Ethernet| LWIP]] |
| `UA/13-Moduli-zhivlennya-rivniv` | Живлення-модулі (3 нот) | [[UA/13-Moduli-zhivlennya-rivniv/01-Buck-Boost| Buck/Boost]], [[UA/13-Moduli-zhivlennya-rivniv/02-Level-Shift| Рівні]], [[UA/13-Moduli-zhivlennya-rivniv/03-Charger-Protect| Заряд]] |
| `UA/14-Devboards` | Плати (6 нот) | [[UA/14-Devboards/01-Blue-Pill| Blue Pill]], [[UA/14-Devboards/02-Black-Pill| Black Pill]], [[UA/14-Devboards/03-Nucleo| Nucleo]], [[UA/14-Devboards/04-Discovery| Discovery]], [[UA/14-Devboards/05-WeAct| WeAct]], [[UA/14-Devboards/06-IoT-Discovery| IoT-Discovery]] |
| `UA/15-Protokoli` | Протоколи (6 нот) | [[UA/15-Protokoli/01-Modbus| Modbus]], [[UA/15-Protokoli/02-DFU-Bootloader| DFU]], [[UA/15-Protokoli/03-Bezpeka| Безпека]], [[UA/15-Protokoli/04-MQTT| MQTT]], [[UA/15-Protokoli/05-CANopen| CANopen]], [[UA/15-Protokoli/06-Secure-Boot| SecureBoot]] |
| `UA/16-Proekti` | Проєкти (6 нот) | [[UA/16-Proekti/01-Meteostantsiya| Метео]], [[UA/16-Proekti/02-GPS-treker| Трекер]], [[UA/16-Proekti/03-Energomonitor| Енергія]], [[UA/16-Proekti/04-Modbus-Gateway| Шлюз]], [[UA/16-Proekti/05-USB-Logger| Логер]], [[UA/16-Proekti/06-Drone-FC| Дрон]] |
| `UA/17-Lab` | Лабораторія (5 нот) | [[UA/17-Lab/01-Priladi| Прилади]], [[UA/17-Lab/02-Plata-PCB| Плата]], [[UA/17-Lab/03-Hardware-Design-Guidelines| Схемотехніка]], [[UA/17-Lab/04-EMI-EMC-Protection| EMI]], [[UA/17-Lab/05-Maketka| Макетка]] |
| `UA/99-Dodatki` | Додатки (5 нот) | [[UA/99-Dodatki/01-Troubleshooting-FAQ| FAQ]], [[UA/99-Dodatki/02-Cheklisti| Чеклісти]], [[UA/99-Dodatki/03-Datasheet-Links| Даташити]], [[UA/99-Dodatki/04-Diagnostic-Map| Карта]], [[UA/99-Dodatki/05-Pinout-Quickref| Піни]] |

## Див. також

- [[CHANGELOG]]
- [[TODO]]
