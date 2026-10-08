---
title: Як користуватись довідником ESP32-Reference
tags:

  - esp32
  - esp32/start
  - esp32/guide

aliases:

  - 01-Yak-koristuvatis
  - Як користуватись довідником

type: guide
---

# Як користуватись довідником

EN version: `00-Start/01-Yak-koristuvatis-dovidnikom.en.md`

> [!tip] Правило 30 секунд
> Будь-яку відповідь можна знайти за 30 секунд: `Ctrl+P` для файлів, `Ctrl+Shift+F` для тексту, клік по тегу `#esp32/*` або перехід з [Головної карти](../../../ESP32-Reference/Home.md).

Довідник організовано за принципом MOC: [Home](../../../ESP32-Reference/Home.md) зв'язує все. Глибока теорія - у [Глосарії](../../../ESP32-Reference/00-Start/02-Glosariy.md), вибір заліза - [Порівняння чипів](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) та [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md), вибір SDK - [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md), нові датчики - за [Шаблоном компонента](../../../ESP32-Reference/_templates/Component-Template.md).

> [!warning] Базове правило живлення
> Увесь довідник виходить з того, що логіка ESP32 - **3.3V**. Приклади з 5V Arduino (Uno/Nano) не переносяться буквально: дільники, level-shifter обов'язкові. Подача 5V на будь-який GPIO - незворотне пошкодження.

## Структура папок

| Папка | Зміст | Приклад |
| --- | --- | --- |
| `00-Start/` | Вхід, глосарій, вибір | Ця нота, [Глосарій](../../../ESP32-Reference/00-Start/02-Glosariy.md), [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| `01-Hardware/` | Чипи і відмінності | [Чипи C3/C6/H2](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md), [C5/C61](../../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md) |
| `02-Zhivlennya/` | Живлення, батареї | [Акумулятори](../../../ESP32-Reference/02-Zhivlennya/04-Akumulyatori-TP4056.md), [Споживання](../../../ESP32-Reference/02-Zhivlennya/03-Spozhivannya.md) |
| `03-GPIO/` | Піни, strapping | [GPIO-огляд](../../../ESP32-Reference/03-GPIO/01-GPIO-oglyad.md), [Strapping](../../../ESP32-Reference/03-GPIO/02-Strapping-pini.md) |
| `04-Shini/` | UART, SPI, I2C | [UART](../../../ESP32-Reference/04-Shini/01-UART.md), [I2C](../../../ESP32-Reference/04-Shini/03-I2C.md) |
| `05-Radio/` | WiFi STA/AP, BLE | [WiFi-STA/AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md), [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| `06-Analog/` | АЦП, ЦАП | [ADC](../../../ESP32-Reference/06-Analog/01-ADC.md) |
| `09-Proshivka/` | Середовища, esptool | [Esptool-Flash](../../../ESP32-Reference/09-Proshivka/04-Esptool-Flash.md) |
| `10-Sensori/` | Датчики за шаблоном | [DHT11/DHT22](../../../ESP32-Reference/10-Sensori/01-DHT11-DHT22.md) |
| `99-Dodatki/` | FAQ, версії | [FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md), [Версії](../../../ESP32-Reference/99-Dodatki/07-Versions.md) |
| `_templates/` | Шаблони нот | [Component-Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| `assets/img/` | Схеми, фото | `placeholder.png` |

## Теги

| Тег | Коли використовувати |
| --- | --- |
| `#esp32/gpio` | Піни, strapping, переривання |
| `#esp32/adc` | АЦП, калібрування, дільники |
| `#esp32/i2c`, `#esp32/spi`, `#esp32/uart` | Шини |
| `#esp32/wifi`, `#esp32/ble` | Радіо |
| `#esp32/ota`, `#esp32/nvs` | Прошивка та пам'ять |
| `#esp32/power` | Живлення, сон, LDO |
| `#esp32/sensor` | Датчики |
| `#esp32/beginner`, `#esp32/advanced` | Рівень складності |

## Пошук та Dataview

Пошук Obsidian:

- `tag:#esp32/adc` - усі ноти про АЦП
- `path:01-Hardware UART` - UART у залізі
- `"level-shifter"` - де згадується узгодження рівнів

> [!example] Dataview-запит: усі датчики I2C
>
> ```dataview
> TABLE tags, type
> FROM "ESP32-Reference"
> WHERE contains(tags, "esp32/sensor")
> SORT file.name ASC
> ```
>
> [!example] Dataview-запит: таблиця чипів
>
> ```dataview
> TABLE cores, wifi
> FROM "ESP32-Reference/00-Start"
> WHERE type = "reference"
> ```

## Умовні позначення схем

| Позначення | Значення |
| --- | --- |
| `3V3` | 3.3V з LDO плати, максимум ~500 мА |
| `5V / VIN` | 5V з USB, тільки живлення модулів |
| `GND` | Спільна земля, завжди з'єднувати |
| `→ TXS / ⇅` | Потрібен level-shifter |
| `⚠ 5V!` | Лінія 5V, не підключати до GPIO |
| `4k7 ↑3V3` | Pull-up 4.7 кОм до 3.3V |

## Рівні складності

| Рівень | Мітки | Приклад |
| --- | --- | --- |
| 🟢 Початківець | `#esp32/beginner` | Блимання LED, [підключення DevKit по USB](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| 🟡 Середній | - | I2C-датчик, [PlatformIO](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md), Wi-Fi STA |
| 🔴 Просунутий | `#esp32/advanced` | OTA, ULP, TWAI, eFuse |

> [!tip] Рекомендований маршрут
>
> 1. [Глосарій](../../../ESP32-Reference/00-Start/02-Glosariy.md) - 10 хв на терміни. 2. [Порівняння чипів](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) - вибір кристала. 3. [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) - яку плату купити. 4. [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) - ESP-IDF чи Arduino. 5. [Home](../../../ESP32-Reference/Home.md) - повернутись до карти.
>
> [!example] Фото/схема: ![](../../../ESP32-Reference/assets/img/placeholder.png)
> Еталонне підключення для всіх прикладів довідника:

| ESP32 DevKit | Модуль / ПК | Примітка |
| --- | --- | --- |
| 3V3 | VCC датчика 3.3V | До 500 мА |
| GND | GND | Спільна земля |
| GPIO21 / GPIO22 | I2C SDA / SCL | Pull-up 4.7к до 3V3 |
| GPIO1 / GPIO3 | USB-UART RX / TX | 3.3V, без 5V! |

## Див. також

- [Головна карта](../../../ESP32-Reference/Home.md)
- [Глосарій](../../../ESP32-Reference/00-Start/02-Glosariy.md)
- [Порівняння чипів](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md)
- [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md)
- [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md)
- [Шаблон компонента](../../../ESP32-Reference/_templates/Component-Template.md)
