---
title: RaspberryPi Reference - головна карта довідника
description: RaspberryPi головна карта навігація MOC плати моделі сенсори HAT OS
tags: [raspberrypi, home, moc, navigation]
category: Meta
date-created: 2026-10-06
date: 2026-10-06
---

# RaspberryPi Reference - головна карта довідника

> MOC всього довідника. Стандарт ноти: frontmatter, рисунок, mermaid, ASCII, код, помилки, джерела. Валідатори: `check_style` / `check_links` / `check_home` - усі в нуль.

| Маршрут | Ланцюжок |
| --- | --- |
| Новачок | [[00-Start/01-Yak-koristuvatis-dovidnikom | Як користуватись]] → [[00-Start/03-Porivnyannya-plate | Порівняння плат]] → [[00-Start/04-Devkit-plati | Плати і аксесуари]] → [[00-Start/05-Vibir-seredovischa | Вибір середовища]] → [[09-Proshivka/01-Imager-Headless | Перший boot]] → [[03-GPIO/01-Header-Gpiozero | Перший LED]] |

| Розділ | Тема | Ноти |
| --- | --- | --- |
| `00-Start` | Старт (5 нот) | [[00-Start/01-Yak-koristuvatis-dovidnikom | Як користуватись]], [[00-Start/02-Glosariy | Глосарій]], [[00-Start/03-Porivnyannya-plate | Порівняння]], [[00-Start/04-Devkit-plati | Плати]], [[00-Start/05-Vibir-seredovischa | Середовище]] |
| `01-Hardware` | Чипи і SoC (3 ноти) | [[01-Hardware/01-SoC-Oglyad | Огляд SoC]], [[01-Hardware/02-BCM2712-Pi5 | BCM2712]], [[01-Hardware/03-RP2040-RP2350 | RP2040/50]] |
| `02-Zhivlennya` | Живлення (3 ноти) | [[02-Zhivlennya/01-USB-C-PD | USB-C PD]], [[02-Zhivlennya/02-PoE-HAT | PoE HAT]], [[02-Zhivlennya/03-UPS-18650 | UPS-резерв]] |
| `03-GPIO` | Піни (3 ноти) | [[03-GPIO/01-Header-Gpiozero | Гребінка]], [[03-GPIO/02-PWM-Pererivannya | ШІМ]], [[03-GPIO/03-HAT-EEPROM | HAT-EEPROM]] |
| `04-Shini` | Шини (2 ноти) | [[04-Shini/01-I2C-SPI-UART | Шини]], [[04-Shini/02-Logic-Analyzer | Аналізатор]] |
| `05-Radio` | Радіо (1 нота) | [[05-Radio/01-WiFi-BT-Bort | Бортове радіо]] |
| `06-Analog` | Аналог (1 нота) | [[06-Analog/01-ADC-Zovnishnye | Зовнішні АЦП]] |
| `07-Timeri-Son` | Таймери і сон (1 нота) | [[07-Timeri-Son/01-Taimeri-Son | Час і сон]] |
| `08-Pamyat` | Пам'ять (2 ноти) | [[08-Pamyat/01-SD-eMMC-NVMe | Носії]], [[08-Pamyat/02-Backup-Clone | Бекапи]] |
| `09-Proshivka` | ОС і прошивка (4 ноти) | [[09-Proshivka/01-Imager-Headless | Imager]], [[09-Proshivka/02-EEPROM-Boot | EEPROM-boot]], [[09-Proshivka/03-OS-Nalashtuvannya | Налаштування ОС]], [[09-Proshivka/04-Docker-Pi | Docker]] |
| `10-Sensori` | Датчики (6 нот) | [[10-Sensori/01-BME280-Klimat | Клімат]], [[10-Sensori/02-MPU6050-Rukh | Рух]], [[10-Sensori/03-DS18B20-Temp | Температура]], [[10-Sensori/04-INA219-Strum | Струм]], [[10-Sensori/05-GPS-NEO | GPS]], [[10-Sensori/06-Kamera-CSI | Камера]] |
| `11-Vivid` | Вивід (3 ноти) | [[11-Vivid/01-DSI-HDMI-Displeyi | Дисплеї]], [[11-Vivid/02-NeoPixel-Servo-Rele | Сила]], [[11-Vivid/03-Audio-HAT | Аудіо]] |
| `12-Moduli-zvyazku` | Зв'язок (3 ноти) | [[12-Moduli-zvyazku/01-Sense-HAT | Sense HAT]], [[12-Moduli-zvyazku/02-GPS-LoRa-HAT | LoRa/GPS]], [[12-Moduli-zvyazku/03-CAN-RS485-HAT | CAN/RS485]] |
| `13-Moduli-zhivlennya-rivniv` | Живлення-модулі (2 ноти) | [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-DC-DC | DC-DC]], [[13-Moduli-zhivlennya-rivniv/02-Level-Shift-3V3 | Рівні]] |
| `14-Devboards` | Плати (6 нот) | [[14-Devboards/01-Pi5-Flagman | Pi 5]], [[14-Devboards/02-Pi4-Robocha | Pi 4]], [[14-Devboards/03-Pico-W-Family | Pico-родина]], [[14-Devboards/04-Zero-2W | Zero 2 W]], [[14-Devboards/05-CM4-CM5 | CM-модулі]], [[14-Devboards/06-400-500 | 400/500]] |
| `15-Protokoli` | Протоколи (2 ноти) | [[15-Protokoli/01-MQTT | MQTT]], [[15-Protokoli/02-HTTP-Webhook | HTTP]] |
| `16-Proekti` | Проєкти (3 ноти) | [[16-Proekti/01-Meteostantsiya | Метео]], [[16-Proekti/02-GPS-Treker | Трекер]], [[16-Proekti/03-Robot-Vizok | Робот]] |
| `17-Lab` | Лабораторія (2 ноти) | [[17-Lab/01-Priladi | Прилади]], [[17-Lab/02-Plata-PCB-HAT | Плата]] |
| `99-Dodatki` | Додатки (3 ноти) | [[99-Dodatki/01-Troubleshooting-FAQ | FAQ]], [[99-Dodatki/02-Datasheet-Links | Даташити]], [[99-Dodatki/03-Diagnostic-Map | Карта]] |
