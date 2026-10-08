---
title: STM32CubeProgrammer - flash, Option Bytes і масове шиття
description: Як використовувати CubeProgrammer (GUI/CLI) для прошивки STM32, читання RDP/OB, масового розгортання, оновлення ST-Link.
tags: [stm32, cubeprogrammer, option-bytes, rdp, flash, cli]
category: Proshivka
date-created: 2026-10-07
date: 2026-10-07
---

# STM32CubeProgrammer - flash, Option Bytes і масове шиття

![[assets/img/stm32-cubeprogrammer-scheme.png|600]]
*Рис. CubeProgrammer: підключення ST-Link → читання OB → програмування → верифікація → масове шиття через CLI.*

> [!tip] Призначення ноти
> Навчити інженера не лише прошивати, але й захищати чип (RDP) та масштабувати виробництво без ручних кліків.

## 1. Підключення

- **ST-Link V2 / V3 / V4** — USB → SWD (SWCLK + SWDIO) + GND + 3.3V;
- **UART-BOOT (DFU)** — на F1/F4 через USART1 + BOOT0 = 1; на G0/G4 — USB-DFU;
- **USB-OTG / DFU** — на H5/U5 з вбудованим USB;
- Перевіряйте `Target` → `Connection` → `Read Memory` — має бути `OK`.

## 2. Читання / запис

- `Erasing & Programming` → вибір `.hex` / `.bin` → `Programming -> Verify`;
- `External Loaders` — якщо зовнішня флеш (QSPI / SPI-NOR);
- Кількість байтів для `Flash` = розмір сектора × кількість; не переповнюйте.

## 3. Option Bytes (OB)

| Біт / група | Значення 0 | Значення 1 | Небезпека |
| --- | --- | --- | --- |
| RDP Level 0 | Читання/запис відкриті | Читання/запис відкриті | Нема (за замовч.) |
| RDP Level 1 | Читання заблоковано, дебаг доступний | Читання заблоковано, дебаг доступний | Повернення до 0 потребує стирання |
| RDP Level 2 | **НЕОБОРОТНІСТЬ** | не підтримується | **Після встановлення — чип безповоротно захищено** |
| nBOOT0 | Boot з Flash | Boot з System Memory | Без пінів BOOT0 може не стартувати |
| nBOOT1 | Boot з Flash | Boot з SRAM | Використовуйте з обережністю |
| WRP (Write Protection) | Сектори відкриті | Сектори захищені від запису | Безповоротно без стирання |

- `STM32CubeProgrammer` → `OB` → `Read`, потім `Modify` тільки після резервної копії `Read`;
- **Ніколи не ставте RDP2 до фінального тестування** — це фінальна печатка.

## 4. Масове шиття (CLI)

```bash
# Один чип через ST-Link
STM32_Programmer_CLI -c port=SWD -p file.hex 0x08000000 -v -rst

# Багато через скрипт + log
for dev in /dev/ttyACM{0..3}; do
  STM32_Programmer_CLI -c port=SWD -p fw.hex 0x08000000 -v >> deploy.log 2>&1
done
```

- `-rst` — перезапуск після програмирования;
- `-v` — верифікація (обов'язково!);
- Під час виробництва: `-no-progress` + `-log` для аудиту.

## 5. Оновлення ST-Link

- `ST-LINK Firmware Update` в GUI або `ST_Programmer_CLI -c port=USB -update`;
- Не обновлюйте під час прошивки — ризик зупинки.

## 6. Типові помилки

| Симптом | Причина | Лікування |
| --- | --- | --- |
| Target not found | Неправильний порт / живлення / кабель | Перевірте 3.3В, GND, SWDIO/SWCLK; спробуйте інший ST-Link |
| Readout protection error | RDP1/2 встановлено | Якщо RDP1 — стирайте + перепрошивйте; якщо RDP2 — чип безповоротно захищено |
| OB не зберігаються | MIT-тест: не натиснута кнопка Apply | Натисніть `Modify` → `Apply`; перевірте `Read` після |
| Flash не відповідає | Зовнішня QSPI — не вибрано External Loader | Додайте loader у `External Loaders`; перевірте `Memory` → `Add` |
| CLI код 1 | Файл не знайдено / адреса поза діапазоном | Перевірте `0x08000000`; перевірте розмір `.hex`; перевірте `ls` |

## Див. також

- [[01-Hardware/01-F0-F1-Classic | F0/F1-класика]] - де починати;
- [[09-Proshivka/01-CubeIDE-CubeMX | CubeIDE/CubeMX]] - середовище до CubeProgrammer;
- [[09-Proshivka/03-ST-Link-Proshivka | ST-Link]] - підключення та прошивка.

## Офіційні джерела

- [STM32CubeProgrammer (ST)](https://www.st.com/content/st_com/en/stm32cubeprogrammer.html) - GUI + CLI + документація.
- [Option bytes (ST docs)](https://dev.st.com/stm32cube-docs/prog/2.23.0/en/docs/markup/CubeProg_UserManual/Option_bytes.html) - RDP/BOR/WRP детально.
- [ST-Link firmware update (ST docs)](https://dev.st.com/stm32cube-docs/prog/2.23.0/en/_pdf/STM32CubeProgrammer_en.pdf) - оновлення, CLI-довідник.
- [RM0316 для STM32F3 (ST)](https://www.st.com/resource/en/reference_manual/rm0316-stm32f303xbcde-stm32f303x68-stm32f328x8-stm32f358xc-stm32f398xe-advanced-armbased-mcus-stmicroelectronics.pdf) - Option Byte регістри (FLASH_OPTR/WRPRA).
