---
title: RaspberryPi Reference - головна карта довідника
description: RaspberryPi головна карта навігація MOC плати моделі сенсори HAT OS
tags: [raspberrypi, home, moc, navigation]
category: Meta
date-created: 2026-10-06
date: 2026-10-06
---

# RaspberryPi Reference - головна карта довідника

EN version: `Home.en.md`

> MOC всього довідника. Стандарт ноти: frontmatter, рисунок, mermaid, ASCII, код, помилки, джерела. Валідатори: `check_style` / `check_links` / `check_home` - усі в нуль.

| Маршрут | Ланцюжок |
| --- | --- |
| Новачок | [[UA/00-Start/01-Yak-koristuvatis-dovidnikom| Як користуватись]] → [[UA/00-Start/03-Porivnyannya-plate| Порівняння плат]] → [[UA/00-Start/04-Devkit-plati| Плати і аксесуари]] → [[UA/00-Start/05-Vibir-seredovischa| Вибір середовища]] → [[UA/09-Proshivka/01-Imager-Headless| Перший boot]] → [[UA/03-GPIO/01-Header-Gpiozero| Перший LED]] |

| Розділ | Тема | Ноти |
| --- | --- | --- |
| `UA/00-Start` | Старт (5 нот) | [[UA/00-Start/01-Yak-koristuvatis-dovidnikom| Як користуватись]], [[UA/00-Start/02-Glosariy| Глосарій]], [[UA/00-Start/03-Porivnyannya-plate| Порівняння]], [[UA/00-Start/04-Devkit-plati| Плати]], [[UA/00-Start/05-Vibir-seredovischa| Середовище]] |
| `UA/01-Hardware` | Чипи і SoC (3 нот) | [[UA/01-Hardware/01-SoC-Oglyad| Огляд SoC]], [[UA/01-Hardware/02-BCM2712-Pi5| BCM2712]], [[UA/01-Hardware/03-RP2040-RP2350| RP2040/50]] |
| `UA/02-Zhivlennya` | Живлення (3 нот) | [[UA/02-Zhivlennya/01-USB-C-PD| USB-C PD]], [[UA/02-Zhivlennya/02-PoE-HAT| PoE HAT]], [[UA/02-Zhivlennya/03-UPS-18650| UPS-резерв]] |
| `UA/03-GPIO` | Піни (3 нот) | [[UA/03-GPIO/01-Header-Gpiozero| Гребінка]], [[UA/03-GPIO/02-PWM-Pererivannya| ШІМ]], [[UA/03-GPIO/03-HAT-EEPROM| HAT-EEPROM]] |
| `UA/04-Shini` | Шини (2 нот) | [[UA/04-Shini/01-I2C-SPI-UART| Шини]], [[UA/04-Shini/02-Logic-Analyzer| Аналізатор]] |
| `UA/05-Radio` | Радіо (1 нот) | [[UA/05-Radio/01-WiFi-BT-Bort| Бортове радіо]] |
| `UA/06-Analog` | Аналог (1 нот) | [[UA/06-Analog/01-ADC-Zovnishnye| Зовнішні АЦП]] |
| `UA/07-Timeri-Son` | Таймери і сон (1 нот) | [[UA/07-Timeri-Son/01-Taimeri-Son| Час і сон]] |
| `UA/08-Pamyat` | Пам'ять (2 нот) | [[UA/08-Pamyat/01-SD-eMMC-NVMe| Носії]], [[UA/08-Pamyat/02-Backup-Clone| Бекапи]] |
| `UA/09-Proshivka` | ОС і прошивка (4 нот) | [[UA/09-Proshivka/01-Imager-Headless| Imager]], [[UA/09-Proshivka/02-EEPROM-Boot| EEPROM-boot]], [[UA/09-Proshivka/03-OS-Nalashtuvannya| Налаштування ОС]], [[UA/09-Proshivka/04-Docker-Pi| Docker]] |
| `UA/10-Sensori` | Датчики (6 нот) | [[UA/10-Sensori/01-BME280-Klimat| Клімат]], [[UA/10-Sensori/02-MPU6050-Rukh| Рух]], [[UA/10-Sensori/03-DS18B20-Temp| Температура]], [[UA/10-Sensori/04-INA219-Strum| Струм]], [[UA/10-Sensori/05-GPS-NEO| GPS]], [[UA/10-Sensori/06-Kamera-CSI| Камера]] |
| `UA/11-Vivid` | Вивід (3 нот) | [[UA/11-Vivid/01-DSI-HDMI-Displeyi| Дисплеї]], [[UA/11-Vivid/02-NeoPixel-Servo-Rele| Сила]], [[UA/11-Vivid/03-Audio-HAT| Аудіо]] |
| `UA/12-Moduli-zvyazku` | Зв'язок (3 нот) | [[UA/12-Moduli-zvyazku/01-Sense-HAT| Sense HAT]], [[UA/12-Moduli-zvyazku/02-GPS-LoRa-HAT| LoRa/GPS]], [[UA/12-Moduli-zvyazku/03-CAN-RS485-HAT| CAN/RS485]] |
| `UA/13-Moduli-zhivlennya-rivniv` | Живлення-модулі (2 нот) | [[UA/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-DC-DC| DC-DC]], [[UA/13-Moduli-zhivlennya-rivniv/02-Level-Shift-3V3| Рівні]] |
| `UA/14-Devboards` | Плати (6 нот) | [[UA/14-Devboards/01-Pi5-Flagman| Pi 5]], [[UA/14-Devboards/02-Pi4-Robocha| Pi 4]], [[UA/14-Devboards/03-Pico-W-Family| Pico-родина]], [[UA/14-Devboards/04-Zero-2W| Zero 2 W]], [[UA/14-Devboards/05-CM4-CM5| CM-модулі]], [[UA/14-Devboards/06-400-500| 400/500]] |
| `UA/15-Protokoli` | Протоколи (2 нот) | [[UA/15-Protokoli/01-MQTT| MQTT]], [[UA/15-Protokoli/02-HTTP-Webhook| HTTP]] |
| `UA/16-Proekti` | Проєкти (3 нот) | [[UA/16-Proekti/01-Meteostantsiya| Метео]], [[UA/16-Proekti/02-GPS-Treker| Трекер]], [[UA/16-Proekti/03-Robot-Vizok| Робот]] |
| `UA/17-Lab` | Лабораторія (2 нот) | [[UA/17-Lab/01-Priladi| Прилади]], [[UA/17-Lab/02-Plata-PCB-HAT| Плата]] |
| `UA/99-Dodatki` | Додатки (3 нот) | [[UA/99-Dodatki/01-Troubleshooting-FAQ| FAQ]], [[UA/99-Dodatki/02-Datasheet-Links| Даташити]], [[UA/99-Dodatki/03-Diagnostic-Map| Карта]] |
