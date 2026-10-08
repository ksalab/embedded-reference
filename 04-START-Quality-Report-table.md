# Аналіз модулів/ревізій — що описано, що пропущено (2026-10-07)

## Методика
Перевірено 4 бази (ESP32/STM32/ARDUINO/RaspberryPi) по файлах `01-Hardware/*.md` + `14-Devboards/*.md` + `05-Moduli-*/`. Підтверджено `grep -oE` + `ls`. Без вигадок.

## ESP32 (01-Hardware/ + 05-Moduli/)

| Модуль / серія | Файл | Покриття | Ревізії виробника | Пропуск |
|---|---|---|---|---|
| C5 / C61 | 10-ESP32-C5-C61.md | Глибоко (469 рядків) | Так (5.5+, C5/C61) | Ревізія модуля WROOM-E — не розділено |
| C2 / P4 | 09-ESP32-C2-P4.md | Є | C2 + P4 native | P4 rev (PCIe Gen3) — не детально |
| S2 | 02-ESP32-S2.md | Є | S2 rev (USB-OTG) | S2 rev v1.3 vs v1.4 — не вказано |
| S3 | 03-ESP32-S3.md | Є | S3 rev | UVC-видалення 5.2 — загально |
| C3 / C6 / H2 | 04-ESP32-C3-C6-H2.md | Є | C3/C6/H2 | Mesh-rev — не розділено |
| Classic | 01-ESP32-Classic.md | Є (C3/C6/H2) | — | — |
| WROOM / WROVER / MINI | 05-Moduli-WROOM-WROVER-MINI.md | Таблиця порівняння | Ні (WROOM-32 / WROVER / MINI-1) | WROOM v1/v2/E, WROVER-B, MINI-1 rev |
| Flash/PSRAM | 06-Flash-PSRAM.md | Є | — | — |
| Strapping/Boot | 07-Boot-Strapping-Reset.md | Є | — | — |

**Пропуск**: WROOM/E rev, WROVER-B, MINI-1 rev — 1-2 рядки в існуючій ноті.

## STM32 (01-Hardware/ + 99-Dodatki/)

| Серія / модуль | Файл | Покриття | Ревізії | Пропуск |
|---|---|---|---|---|
| F0 / F1 | 01-F0-F1-Classic.md | Таблиця + код | Імпліцитно (errata) | Errata F0/F1 по ревізіям — не розділено |
| F3 / F4 | 02-F3-F4.md | Довге (F3 10 Msps interleaved) | Так (F3/F4) | F303 vs F303RE — не розділено |
| G0 / G4 | 03-G0-G4.md | Є | G0/G4 | G071 vs G071RB — не розділено |
| H5 / H7 | 04-H5-H7.md | Є | H5/H7 | H7-deep — окремо |
| L0 / L4 / U5 | 05-L0-L4-U5.md | Є | L0/L4/U5 | U5-deep — окремо |
| WB / WL | 06-WB-WL.md | Є | WB/WL | — |
| C0 | 11-STM32C0-Start.md (P4) | Новий | C011/C031 | RM+C0 ревізія — не розділено |
| Devboards | 01-Blue-Pill/02-Black-Pill/03-Nucleo... | 6 нот | Плати, не чипи | — |

**Пропуск**: Errata по конкретній ревізії (F3/F4/G0) — є `07-Errata-Migratsiya.md`, але не по кожному чипу.

## ARDUINO (01-Hardware/ + 14-Devboards/)

| Модуль / серія | Файл | Покриття | Ревізії | Пропуск |
|---|---|---|---|---|
| AVR-Uno | 01-AVR-Uno.md | Є (ATmega328P) | ATmega328P vs 328PB | 328PB з USB — не розділено |
| Nano-Mega | 02-Nano-Mega.md | Є | ATmega328P/2560 | — |
| Due / Zero / ARM | 03-Due-Zero-ARM.md | Є | SAM3X8E / RP2040 | — |
| Uno R4 | 04-Uno-R4.md | Minima vs WiFi — є | Rev1 vs Rev2 — не розділено | Потрібна 2 рядки |
| Nano33-BLE | 05-Nano33-BLE-ARM.md | Є | Nano 33 BLE Sense vs Sense rev 2 | Rev 2 — не розділено |
| RP2040 | 04-RP2040.md (P4) | Новий | RP2040 / RP2350 / PICO-W / PICO-2W | Rev (Pico W vs Pico 2 W) — не розділено |
| ESP32-GIGA | 03-Nano-ESP32-GIGA.md | Флагмани (P4) | ESP32-S3 / STM32H7 | — |

**Пропуск**: Nano33 Sense rev 2, Uno R4 Rev1/Rev2, RP2040 rev (W vs 2W) — 2-3 рядки в існуючих нотах.

## Raspberry Pi (01-Hardware/ + 03-RP2040-RP2350/)

| Модуль / серія | Файл | Покриття | Ревізії | Пропуск |
|---|---|---|---|---|
| BCM2711 (Pi 4) | 01-SoC-Oglyad.md | Так | Pi 4 rev (1.1 vs 1.2?) | Не розділено |
| BCM2712 (Pi 5) | 01-SoC-Oglyad.md + 01-Pi5-Flagman.md | Так + глибоко | Pi 5 rev (NVMe, PCIe) | Rev 1.0 vs 1.1 — не розділено |
| RP2040 | 03-RP2040-RP2350.md | Глибоко (PIO) | RP2040 / RP2350 (A/B?) | RP2350 rev — не розділено |
| RP2350 | 03-RP2040-RP2350.md | Так | M33 / A53 vs M0+ | — |
| Zero 2 W | 04-Zero-2W.md (P4) | Так | RP3A0 | — |

**Пропуск**: Pi 5 Rev (NVMe/PCIe Gen3), RP2040 rev (W vs 2W) — 2 рядки; HAT+ механіка — є джерело в `03-HAT-EEPROM.md`, але не в `01-SoC`.

## Висновок
- **Варіанти описані** для всіх ключових сімейств (ESP32 C3/S2/S3/C5/P4, STM32 F/G/H/L/U/C0, Arduino AVR/ARM/ESP32-GIGA/RP2040, RPi Pi4/Pi5/RP2040/RP2350).
- **Ревізії виробника**: загальні (C5/C61, F3/F4 errata) — в основному тексті; конкретні (WROOM rev, F3 rev, Nano33 rev, Pi 5 rev) — частково (заголовок/таблиця), не в кожній ноті.
- **Помилки/пошкодження**: 0; символика: чисто.
- **Рекомендація**: якщо потрібно виробниче покриття (один чип — один файл) — додати 2-3 рядки ревізій у існуючі `01-Hardware/*.md`; не створювати нові.
