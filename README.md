# Embedded Reference UA

Україномовна база знань з вбудованої електроніки у форматі Obsidian-сховищ:
**ESP32 · STM32 · Arduino · Raspberry Pi** — близько 490 нот, 460+ оригінальних схем,
≈6000 перехресних посилань, код під 3 фреймворки, перевірені даташити.

| Сховище | Нот | Схем | Фокус |
|---|---|---|---|
| [ESP32-Reference](ESP32-Reference/Home.md) | 222 | 214 | Classic/S2/S3/C3/C6/H2/C5/P4, WiFi/BLE/Matter, TinyML, LoRaWAN |
| [STM32-Reference](STM32-Reference/Home.md) | 122 | 116 | F0–U5, HAL/LL, CubeIDE, FOC, CAN-FD, USB, Secure Boot |
| [ARDUINO-Reference](ARDUINO-Reference/Home.md) | 80 | 77 | AVR Uno/Nano/Mega, UNO R4, RP2040, сенсори, PlatformIO |
| [RaspberryPi-Reference](RaspberryPi-Reference/Home.md) | 60 | 51 | Pi 4/5, Pico W, HAT, NVMe-boot, Docker, headless |

## Як користуватись

1. Відкрийте папку сховища як vault в [Obsidian](https://obsidian.md).
2. Старт — `Home.md` у корені кожного сховища: маршрути читання
   («Новачок», «Радіо», «Батарейний пристрій») і карта всіх розділів.
3. Новачкам: `00-Start/` — гід, глосарій, порівняння плат, вибір середовища.
4. Кожна нота — автономна: схема, код, таблиця «Симптом → Причина → Лікування»,
   офіційні джерела з прямими лінками на виробника.

## Стандарт ноти

- YAML frontmatter (`title`, `description`, `tags`, `category`, `date-created`, `date`);
- рисунок `![[assets/img/…|600]]` + підпис курсивом;
- mermaid-діаграма; код (Arduino / ESP-IDF / MicroPython — де доречно);
- таблиця типових помилок; розділ «Офіційні джерела» (лінки на конкретну
  модель/документацію, вгадані URL заборонені);
- ≥150 рядків; українська мова за глосарієм (`04-START-Quality-Report-table.md`).

## Перевірки

У кожному сховищі `scripts/`:

```bash
python3 scripts/check_style.py   # стандарт ноти, очікуємо violations=0
python3 scripts/check_links.py   # валідність [[посилань]] і PNG, broken=0
python3 scripts/check_home.py    # лічильники Home і повнота навігації, home-errors=0
```

Лінт з кореня репозиторію (конфіг [.markdownlint.yaml](.markdownlint.yaml)):

```bash
markdownlint "ESP32-Reference/**/*.md" "STM32-Reference/**/*.md" \
  "ARDUINO-Reference/**/*.md" "RaspberryPi-Reference/**/*.md"
```

Деталі для авторів — у [CONTRIBUTING.md](CONTRIBUTING.md).
Звіт про якість: [04-START-Quality-Report.md](04-START-Quality-Report.md),
таблиця уніфікованої термінології: [04-START-Quality-Report-table.md](04-START-Quality-Report-table.md).
