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
> Будь-яку відповідь можна знайти за 30 секунд: `Ctrl+P` для файлів, `Ctrl+Shift+F` для тексту, клік по тегу `#esp32/*` або перехід з [[Home|Головної карти]].

Довідник організовано за принципом MOC: [[Home|Home]] зв'язує все. Глибока теорія - у [[00-Start/02-Glosariy|Глосарії]], вибір заліза - [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]] та [[00-Start/04-Devkit-plati|DevKit плати]], вибір SDK - [[00-Start/05-Vibir-seredovischa|Вибір середовища]], нові датчики - за [[_templates/Component-Template|Шаблоном компонента]].

> [!warning] Базове правило живлення
> Увесь довідник виходить з того, що логіка ESP32 - **3.3V**. Приклади з 5V Arduino (Uno/Nano) не переносяться буквально: дільники, level-shifter обов'язкові. Подача 5V на будь-який GPIO - незворотне пошкодження.

## Структура папок

| Папка | Зміст | Приклад |
| --- | --- | --- |
| `00-Start/` | Вхід, глосарій, вибір | Ця нота, [[00-Start/02-Glosariy | Глосарій]], [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| `01-Hardware/` | Чипи і відмінності | [[01-Hardware/04-ESP32-C3-C6-H2 | Чипи C3/C6/H2]], [[01-Hardware/10-ESP32-C5-C61 | C5/C61]] |
| `02-Zhivlennya/` | Живлення, батареї | [[02-Zhivlennya/04-Akumulyatori-TP4056 | Акумулятори]], [[02-Zhivlennya/03-Spozhivannya | Споживання]] |
| `03-GPIO/` | Піни, strapping | [[03-GPIO/01-GPIO-oglyad | GPIO-огляд]], [[03-GPIO/02-Strapping-pini | Strapping]] |
| `04-Shini/` | UART, SPI, I2C | [[04-Shini/01-UART | UART]], [[04-Shini/03-I2C | I2C]] |
| `05-Radio/` | WiFi STA/AP, BLE | [[05-Radio/01-WiFi-STA-AP | WiFi-STA/AP]], [[05-Radio/02-BLE-Bluetooth | BLE]] |
| `06-Analog/` | АЦП, ЦАП | [[06-Analog/01-ADC | ADC]] |
| `09-Proshivka/` | Середовища, esptool | [[09-Proshivka/04-Esptool-Flash | Esptool-Flash]] |
| `10-Sensori/` | Датчики за шаблоном | [[10-Sensori/01-DHT11-DHT22 | DHT11/DHT22]] |
| `99-Dodatki/` | FAQ, версії | [[99-Dodatki/02-Troubleshooting-FAQ | FAQ]], [[99-Dodatki/07-Versions | Версії]] |
| `_templates/` | Шаблони нот | [[_templates/Component-Template | Component-Template]] |
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
| 🟢 Початківець | `#esp32/beginner` | Блимання LED, [[00-Start/04-Devkit-plati | підключення DevKit по USB]] |
| 🟡 Середній | - | I2C-датчик, [[00-Start/05-Vibir-seredovischa | PlatformIO]], Wi-Fi STA |
| 🔴 Просунутий | `#esp32/advanced` | OTA, ULP, TWAI, eFuse |

> [!tip] Рекомендований маршрут
>
> 1. [[00-Start/02-Glosariy|Глосарій]] - 10 хв на терміни. 2. [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]] - вибір кристала. 3. [[00-Start/04-Devkit-plati|DevKit плати]] - яку плату купити. 4. [[00-Start/05-Vibir-seredovischa|Вибір середовища]] - ESP-IDF чи Arduino. 5. [[Home|Home]] - повернутись до карти.
>
> [!example] Фото/схема: ![[assets/img/placeholder.png]]
> Еталонне підключення для всіх прикладів довідника:

| ESP32 DevKit | Модуль / ПК | Примітка |
| --- | --- | --- |
| 3V3 | VCC датчика 3.3V | До 500 мА |
| GND | GND | Спільна земля |
| GPIO21 / GPIO22 | I2C SDA / SCL | Pull-up 4.7к до 3V3 |
| GPIO1 / GPIO3 | USB-UART RX / TX | 3.3V, без 5V! |

## Див. також

- [[Home|Головна карта]]
- [[00-Start/02-Glosariy|Глосарій]]
- [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]]
- [[00-Start/04-Devkit-plati|DevKit плати]]
- [[00-Start/05-Vibir-seredovischa|Вибір середовища]]
- [[_templates/Component-Template|Шаблон компонента]]
