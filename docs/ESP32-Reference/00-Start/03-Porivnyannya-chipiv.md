---
title: Порівняння чипів ESP32 - Classic/S2/S3/C3/C6/H2/P4/C5
tags:

  - esp32
  - esp32/start
  - esp32/hardware
  - esp32/chips

aliases:

  - 03-Porivnyannya-chipiv
  - Порівняння чипів
  - ESP32 vs S2 vs S3 vs C3 vs C6 vs H2

type: reference
---

# Порівняння чипів ESP32

EN version: `00-Start/03-Chip-Comparison.en.md`

> [!tip] Короткий вибір
> Універсальний - **ESP32-Classic** або **S3**. Дешевий Wi-Fi датчик - **C3**. Камера/ML/USB - **S3**. Zigbee/Thread - **C6/H2**. Терміни дивіться у [Глосарії](../../../ESP32-Reference/00-Start/02-Glosariy.md), плати - [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md), SDK - [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md). Структура довідника - [Як користуватись](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md), карта - [Home](../../../ESP32-Reference/Home.md).
>
> [!warning] Усі чипи - 3.3V!
> Жоден ESP32 (Classic/S2/S3/C3/C6/H2) не має 5V-толерантних GPIO. Різниця лише в кількості пінів та периферії, але правило одне: HIGH = 3.3V max. Датчики 5V - тільки через [узгодження рівнів за шаблоном](../../../ESP32-Reference/_templates/Component-Template.md).

## Детальна таблиця

| Параметр | ESP32 Classic | ESP32-S2 | ESP32-S3 | ESP32-C3 | ESP32-C6 | ESP32-H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Ядра | 2× Xtensa LX6 | 1× LX7 | 2× LX7 | 1× RISC-V | 1× RISC-V HP + LP | 1× RISC-V |
| Частота | 160/240 МГц | 240 МГц | 240 МГц | 160 МГц | 160 МГц | 96 МГц |
| SRAM | 520 КБ | 320 КБ | 512 КБ | 400 КБ | 512 КБ | 320 КБ |
| PSRAM опція | Так (WROVER) | Так | Так (Octal) | Ні | Ні | Ні |
| Flash зовн. | 4-16 МБ | 4-16 МБ | 8-32 МБ (Octal) | 4-8 МБ | 8 МБ | 4-8 МБ |
| Wi-Fi | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 6 (ax) | Ні |
| Bluetooth | Classic + BLE 4.2 | Ні (тільки USB) | BLE 5.0 Mesh | BLE 5.0 Mesh | BLE 5.3 + 15.4 | BLE 5.2 + 15.4 |
| Zigbee/Thread | Ні | Ні | Ні | Ні | Так | Так |
| USB | Тільки UART-міст | OTG Full-Speed | OTG Full-Speed | CDC serial | CDC + JTAG | CDC |
| ADC | 2× 12-біт (18 кан.) | 2× 13-біт (20 кан.) | 2× 12-біт (20 кан.) | 2× 12-біт (6 кан.) | 1× 12-біт (7 кан.) | Ні (темп. сенсор) |
| DAC | 2× 8-біт | 2× 8-біт | Ні | Ні | Ні | Ні |
| Touch | 10 кан. | 14 кан. | 14 кан. | Ні | Ні | Ні |
| RMT / MCPWM / TWAI | Так | Так / Ні / Так | Так | RMT, MCPWM лайт | RMT, MCPWM | - |
| ULP | FSM | FSM + RISC-V | FSM + RISC-V | Ні | LP-Core | LP |
| Ціна модуля, $ | 3-5 | 3-5 | 5-8 | 2-4 | 4-6 | 3-5 |
| Застосування | Універсальний, BT Classic | USB HID, без BLE | Камера, ML, дисплеї | Датчики, ESP-NOW | Matter, шлюзи | Zigbee-кінцеві |

## Рекомендації вибору

| Задача | Беріть | Чому |
| --- | --- | --- |
| Навчання, legacy-проєкти, A2DP | ESP32 Classic (WROOM-32) | Максимум прикладів, DAC, BT Classic |
| USB-клавіатура, девайс | S2 (Saola) | Native USB, дешевий, але без BLE |
| Камера OV2640, TinyML, LCD | S3 (DevKitC-1) | Octal PSRAM, AI-векторні інструкції, USB |
| Дешевий датчик Wi-Fi/MQTT | C3 SuperMini | $2-3, BLE 5, низьке споживання |
| Matter / Thread / Zigbee | C6 або H2 | 802.15.4, Wi-Fi 6 (C6) |
| Батарейний датчик на роки | C3 / H2 + deep-sleep | 5 мкА сон, див. [живлення DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |

> [!tip] PSRAM
> Для камер (OV2640 2 МП) та LVGL-дисплеїв беріть **WROVER** або **S3 з Octal PSRAM 8 МБ**. Без PSRAM JPEG-кадр не влізе в SRAM. Деталі живлення - [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md).
>
> [!warning] ADC2 + Wi-Fi
> На Classic/S3 канал ADC2 конфліктує з Wi-Fi драйвером. Для аналогових вимірювань при увімкненому Wi-Fi використовуйте тільки ADC1. Це часта причина «стрибаючих» показань.

## Сумісність зі середовищами

| Середовище | Classic | S2/S3 | C3/C6/H2 |
| --- | --- | --- | --- |
| ESP-IDF 5.x | Так | Так | Так (RISC-V стабільно з 5.0) |
| Arduino-core 2.x/3.x | Так | Так | Так, C6/H2 - тільки 3.x |
| MicroPython | Так | S2/S3 частково | C3 - так, C6/H2 - експеримент. |
| PlatformIO | Так | Так | Так |

Деталі - [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md).

> [!example] Фото/схема: ![](../../../ESP32-Reference/assets/img/placeholder.png)
> Порівняльний стенд: три DevKit на одному столі:

| ESP32 DevKit | USB | Примітка |
| --- | --- | --- |
| Classic DOIT | Micro-USB | CP2102, 5V→3.3V AMS1117 |
| S3 DevKitC-1 | USB-C native | Два порти: UART + USB-OTG |
| C3 SuperMini | USB-C native | CDC, кнопка BOOT для прошивки |
| GND між платами | - | З'єднати при спільних датчиках 3.3V |

## Нові чипи: C5 / C61 / P4 / C2 (2025-2026)

> [!tip] Детально про новачків
> Повні ноти: C5/C61 - [10-ESP32-C5-C61](../../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md), C2/P4 - [09-ESP32-C2-P4](../../../ESP32-Reference/01-Hardware/09-ESP32-C2-P4.md),
> C3/C6/H2 - [04-ESP32-C3-C6-H2](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md). Нижче - короткий зріз, щоб вибрати за 2 хвилини.

| Чип | Що це | Головна фішка | Обмеження |
| --- | --- | --- | --- |
| ESP32-C5 | Флагман C-лінійки, RISC-V 240 МГц + LP 40 МГц | **Dual-band Wi-Fi 6 (2.4 + 5 ГГц)** + BLE + **802.15.4** в одному кристалі | Дорожчий, прикладів менше, ніж під C3/C6; без MIPI/USB HS |
| ESP32-C61 | Здешевлений наступник C6, RISC-V 160 МГц | Дешевий **Wi-Fi 6 2.4 ГГц** + BLE 5, in-package PSRAM, ETM | **Немає 802.15.4!** Zigbee/Thread не вміє апаратно |
| ESP32-P4 | Потужний хост, dual RISC-V 400 МГц | MIPI-CSI/DSI до 1080p, USB HS, Ethernet - **без радіо!** | Wi-Fi/BLE тільки через компаньйона (C6/C61 по SPI/SDIO/UART) |
| ESP32-C2 (ESP8684/85 SiP) | Найдешевший вузол, RISC-V 120 МГц | Ціна $1.5-2.5, Wi-Fi 4 + BLE 5, SiP-flash 2-4 МБ | ~14 GPIO, 272 КБ SRAM, немає 15.4, скромний сон |

> [!warning] C61 ≠ C6 для Zigbee!
> Часта помилка: беруть C61 під Thread/Zigbee, бо «це ж наступник C6». У C61 радіо 802.15.4
> **вирізано заради ціни** - Thread/Zigbee там не буде ніколи. Треба 15.4 → C6, H2 або C5.
> Треба тільки дешевий Wi-Fi 6 → C61. Деталі - [10-ESP32-C5-C61](../../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md).

## Розширена таблиця (усі 10 чипів)

| Параметр | Classic | S2 | S3 | C3 | C6 | C5 | C61 | H2 | C2 | P4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ядра | 2× Xtensa LX6 | 1× LX7 | 2× LX7 | 1× RISC-V | RISC-V HP + LP | RISC-V 240 МГц + LP 40 МГц | 1× RISC-V | 1× RISC-V | 1× RISC-V | 2× RISC-V HP + LP |
| Частота | 160/240 МГц | 240 МГц | 240 МГц | 160 МГц | 160 МГц | 240 МГц | 160 МГц | 96 МГц | 120 МГц | 400 МГц |
| SRAM | 520 КБ | 320 КБ | 512 КБ | 400 КБ | 512 КБ | 384 КБ | 320 КБ | 320 КБ | 272 КБ | 768 КБ HP |
| PSRAM опція | Так (WROVER) | Так | Так (Octal) | Ні | Ні | Так (зовнішня) | Так (in-package!) | Ні | Ні (SiP-flash) | Так (зовнішня, обов'язкова під камеру) |
| Flash | 4-16 МБ | 4-16 МБ | 8-32 МБ (Octal) | 4-8 МБ | 8 МБ | Зовнішня (QSPI) | Quad SPI + SiP-варіанти | 4-8 МБ | Зовн. / SiP 2-4 МБ (H2/H4) | Зовнішня |
| Wi-Fi | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 6 (ax, 2.4) | **6 (ax, 2.4 + 5!)** | 6 (ax, 2.4) | Ні | 4 (b/g/n) | Ні (через C6!) |
| Bluetooth | Classic + BLE 4.2 | Ні | BLE 5.0 Mesh | BLE 5.0 Mesh | BLE 5.3 + 15.4 | BLE 5 + 15.4 | BLE 5 + Mesh 1.1 | BLE 5.2 + 15.4 | BLE 5 | Ні (через C6!) |
| Zigbee/Thread | Ні | Ні | Ні | Ні | Так | Так | **Ні** | Так | Ні | Ні |
| USB | UART-міст | OTG FS | OTG FS | CDC serial | CDC + JTAG | CDC + JTAG | CDC + JTAG | CDC | Serial-JTAG | **OTG HS** |
| GPIO (орієнтовно) | ~34 | ~43 | ~45 | 22 | 30 | до 29 | 20+ (за модулем) | 19 | ~14 | 55 |
| Ціна модуля 2026, $ | 3-5 | 3-5 | 5-8 | 2-4 | 4-6 | 5-8 | 2.5-4 | 3-5 | 1.5-2.5 | 8-12 |
| Застосування | Legacy, BT Classic | USB HID без BLE | Камера, ML, дисплеї | Датчики, ESP-NOW | Matter/Thread-шлюз | Dual-band шлюз, 5 ГГц | Дешевий Wi-Fi 6 | Zigbee-кінцеві | Розетка, AT-слейв | HMI 1080p, USB-хост |

## Матриця вибору «задача → чип»

| Задача | Беріть | Чому |
| --- | --- | --- |
| Батарейний датчик (роки на акумі) | **C3** (або H2 для Zigbee) | 5 мкА сон, достатньо RAM, максимум прикладів low-power |
| Камера OV2640 / TinyML / LCD | **S3** | Octal PSRAM, AI-інструкції, USB; C5/C6 камеру не тягнуть! |
| Zigbee / Thread / Matter-over-Thread | **C6** (шлюз) або H2 (кінцевий) | 802.15.4 на кристалі; C61/C2 не підійдуть - там його немає |
| Найдешевше: розетка, лампа, AT-слейв | **C2** / ESP8684 | $1.5-2.5, Wi-Fi 4 + BLE вистачає, SiP-flash економить місце |
| HMI-панель / камера 1080p / USB-хост | **P4 + C6** (радіо-компаньйон) | MIPI + USB HS у P4, Wi-Fi 6 бере C6 по SPI/SDIO (ESP-Hosted) |
| Wi-Fi 6, забитий ефір, низька затримка | **C5** | Єдиний з **5 ГГц**: TWT, OFDMA, BSS coloring; Thread у комплекті |
| Дешевий Wi-Fi 6 без Thread | **C61** | Ціна рівня C3, фічі Wi-Fi 6 (TWT/OFDMA), Matter-over-WiFi |
| USB-клавіатура, девайс без BLE | S2 | Native USB, дешевий; але для нових проєктів глянь S3 |
| Навчання, legacy, A2DP / BT Classic | Classic (WROOM-32) | Максимум прикладів, DAC, BT Classic - але читай EOL нижче! |

## Ціни 2026 (орієнтовні, модулі/DevKit)

| Чип | Модуль, $ | DevKit, $ | Коментар |
| --- | --- | --- | --- |
| C2 / ESP8684 | 1.5-2.5 | 4-6 | Найдешевший вхід; MINI-плати дешевші за DevKit |
| C3 | 2-4 | 5-7 | SuperMini-клони - дно ціни, але перевіряй LDO і USB-міст |
| C61 | 2.5-4 | 6-9 | MINI-1 доступний; ціна впаде мірою насичення складів |
| H2 | 3-5 | 7-10 | Нішевий, тримай запас: потрібен border router (C6/S3) |
| Classic | 3-5 | 6-9 | Ціна стоїть через масовість, але це legacy |
| S2 | 3-5 | 7-10 | Попит низький - шукай розпродажі, або бери S3 |
| C6 | 4-6 | 8-12 | Хіт Matter-сегмента, ціна стабільна |
| C5 | 5-8 | 10-15 | Премія за dual-band і новизну; DevKitC-1 у офіційних сторах |
| S3 | 5-8 | 10-16 | Залежить від PSRAM (Octal 8 МБ дорожча) |
| P4 | 8-12 | 15-25 | Плюс ціна C6-компаньйона і PSRAM; HMI-проєкти рахувати цілком |

> Ціни - роздріб AliExpress/дистриб'ютори, осінь 2026. Гурт від 100 шт −20-40%.
> Перед закупівлею звір наявність саме потрібного модуля (WROOM/WROVER/MINI), а не тільки чипа.

## EOL-застереження: Classic - legacy

> [!danger] Нові проєкти - не на Classic!
> ESP32 Classic (LX6, Wi-Fi 4, 2016 рік) - зрілий, але глухий кут: немає Wi-Fi 6,
> немає 802.15.4, вище споживання, 40-нм процес проти сучасних. Espressif давно просуває
> міграцію: ESP8266 → C2, а Classic для нових розробок витісняють S3 (потужність),
> C6/C5 (Wi-Fi 6 + Matter) і C61/C3 (ціна). Classic лишай для: підтримки старих плат,
> BT Classic/A2DP (його немає в жодному C-чипі!), DAC і готових прикладів.
> Довгострокову доступність конкретного чипа перевіряй у
> [Longevity Commitment (Espressif)](https://www.espressif.com/en/products/longevity-commitment)
> і PCN-повідомленнях - не закладай Classic у продукт на 5+ років без перевірки.

| Замість Classic бери | Коли |
| --- | --- |
| S3 | Камера, дисплеї, ML, USB - прямий наступник за потужністю |
| C6 / C5 | Wi-Fi 6, Matter, шлюзи; C5 - якщо треба 5 ГГц |
| C3 / C61 | Дешеві датчики; C61 - якщо хочеш Wi-Fi 6 за ціною C3 |
| C2 | Ультрадешеві вузли замість ESP8266/Classic-простих задач |

## Сумісність нових чипів із середовищами

| Середовище | C5 | C61 | P4 | C2 |
| --- | --- | --- | --- | --- |
| ESP-IDF | **5.5+** (`set-target esp32c5`) | **5.5+** (`esp32c61`) + Matter SDK | 5.3+ (`esp32p4`) | 5.0+ (`esp32c2`) |
| Arduino-core | **3.3.x+** (плата C5 Dev Module) | **3.3.x+** (PR #12019) | 3.x, частково | 2.x/3.x |
| MicroPython | Експеримент (немає стабільної) | Експеримент | Експеримент | Так (компактна збірка) |
| PlatformIO | Через pioarduino/community | Аналогічно | Так | Так |

Деталі - [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md),
налаштування IDF - [ESP-IDF setup](../../../ESP32-Reference/09-Proshivka/01-ESP-IDF-setup.md),
Arduino/PIO - [Arduino/PlatformIO](../../../ESP32-Reference/09-Proshivka/02-Arduino-PlatformIO.md),
повні ноти - [10-ESP32-C5-C61](../../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md) і [09-ESP32-C2-P4](../../../ESP32-Reference/01-Hardware/09-ESP32-C2-P4.md).

## Див. також

- [Головна карта](../../../ESP32-Reference/Home.md)
- [Як користуватись](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md)
- [Глосарій](../../../ESP32-Reference/00-Start/02-Glosariy.md)
- [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md)
- [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md)
- [C5/C61](../../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md)
- [C2/P4](../../../ESP32-Reference/01-Hardware/09-ESP32-C2-P4.md)
- [C3/C6/H2](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md)
- [Шаблон компонента](../../../ESP32-Reference/_templates/Component-Template.md)
