---
description: Підтягування та рівні 3.3V - Internal pull-up / pull-down; Дільник 5V → 3.3V - розрахунок; TXS0108 vs резистивний дільник
category: GPIO
title: Підтягування та рівні 3.3V
tags: [esp32, gpio, pullup, level-shifter, 5v]
date: 2026-09-27
---

# Підтягування та рівні 3.3V

EN version: `03-GPIO/03-Pull-Ups-Levels.en.md`

![[assets/img/gpio-pullup-levels-scheme.png|600]]
*Рис. Підтяжки і рівні: внутрішні/зовнішні pull, дільник 5V→3.3V, TXS0108.*

ESP32 - **строго 3.3V логіка**. 5V на пін = деградація/пробій. Внутрішні підтяжки слабкі (~45 кОм) - для довгих ліній і [[04-Shini/03-I2C|I2C]] став зовнішні.

> [!danger] 5V НЕ толерується
> На відміну від STM32 (5V-tolerant піни), ESP32 **не має** 5V-tolerant GPIO. Датчик 5V → тільки через дільник або level-shifter.

## Призначення

Підтягування та рівні 3.3V - Internal pull-up / pull-down; Дільник 5V → 3.3V - розрахунок; TXS0108 vs резистивний дільник. ESP32 - строго 3.3V логіка. 5V на пін = деградація/пробій. Внутрішні підтяжки слабкі (~45 кОм) - для довгих ліній і [[04-Shini/03-I2C|I2C]] став зовнішні. На відміну від STM32 (5V-tolerant піни), ESP32 не має 5V-tolerant GPIO. Датчик 5V → тільки через дільник або level-shifter.

## Internal pull-up / pull-down

| Параметр | Значення |
| --- | --- |
| R pull-up/down | ~45 кОм (30-80 кОм розкид) |
| Вмикання | програмно + зовнішньо |
| Струм | ~70 мкА при 3.3В |
| Коли не вистачає | I2C, довгі шлейфи, кнопки з шумами |

```cpp
// Arduino
pinMode(13, INPUT_PULLUP);
pinMode(14, INPUT_PULLDOWN);
```

```c
// ESP-IDF
gpio_set_pull_mode(13, GPIO_PULLUP_ONLY);
gpio_set_pull_mode(14, GPIO_PULLDOWN_ONLY);
```

```python
# MicroPython
from machine import Pin
b = Pin(13, Pin.IN, Pin.PULL_UP)
```

## Дільник 5V → 3.3V - розрахунок

Формула: `Vout = Vin × R2 / (R1 + R2)`

| Vin | R1 | R2 | Vout | Струм |
| --- | --- | --- | --- | --- |
| 5.0В | 2 кОм | 3.3 кОм | ~3.11В | ~0.94 мА |
| 5.0В | 1.8 кОм | 3.3 кОм | ~3.23В | ~0.98 мА |
| 5.0В | 10 кОм | 20 кОм | ~3.33В | ~0.17 мА (для повільних сигналів) |

> [!tip] Для UART 115200 бери R1=2к, R2=3.3к. 10к+20к - тільки для кнопок/повільних сигналів, бо RC-фронт завалює бодрейт.

## TXS0108 vs резистивний дільник

| Критерій | Резистивний дільник | TXS0108 / TXB0108 |
| --- | --- | --- |
| Напрям | тільки 5V→3.3V | bidirectional |
| Швидкість | до ~1 МГц | до 24+ МГц (TXS) |
| I2C | погано (open-drain конфлікт) | TXS0108 - так, TXB - ні |
| Ціна | копійки | дорожче, потребує OE + живлення обох сторін |
| Коли брати | UART RX, дільник сенсора | [[04-Shini/03-I2C | I2C]], [[04-Shini/02-SPI | SPI]], NeoPixel 5V |

> [!info] Для I2C 5V сенсорів класика - TXS0108E або MOSFET-перетворювач рівнів (BSS138). Дільник на SDA/SCL не став.

## Схема кнопки з debounce

| ESP32 | Компонент | Значення |
| --- | --- | --- |
| GPIO13 | кнопка → GND | вхід |
| GPIO13 | резистор → 3V3 | 10 кОм pull-up (або internal) |
| GPIO13 | конденсатор → GND | 100 нФ (апаратний debounce) |

**Arduino (програмний debounce):**

```cpp
const int BTN = 13;
int last = HIGH; unsigned long t = 0;
void setup() { pinMode(BTN, INPUT_PULLUP); Serial.begin(115200); }
void loop() {
  int v = digitalRead(BTN);
  if (v != last && millis() - t > 50) { t = millis(); last = v;
    if (v == LOW) Serial.println("press"); }
}
```

**ESP-IDF:**

```c
gpio_set_direction(13, GPIO_MODE_INPUT);
gpio_set_pull_mode(13, GPIO_PULLUP_ONLY);
// далі опитування + vTaskDelay(20 / portTICK_PERIOD_MS) або interrupt + timer
```

**MicroPython:**

```python
from machine import Pin
import time
b = Pin(13, Pin.IN, Pin.PULL_UP)
last = 1
while True:
    v = b.value()
    if v != last:
        time.sleep_ms(50)
        v = b.value()
        if v != last:
            last = v
            if v == 0: print("press")
    time.sleep_ms(10)
```

## Див. також

- [[Home]]
- [[01-Hardware/01-ESP32-Classic]]
- [[03-GPIO/01-GPIO-oglyad|GPIO огляд]]
- [[03-GPIO/02-Strapping-pini|Strapping-піни]]
- [[04-Shini/03-I2C|I2C]]
- [[13-Moduli-zhivlennya-rivniv/02-Level-Shifters|Level-shifteri]]
- [[03-GPIO/04-Pererivannya-PWM|Кнопки та енкодери]]

### Mermaid: вибір підтяжки

```mermaid
flowchart TB
    Q[Лінія висить?] --> LEN{Довжина / швидкість?}
    LEN -->|Кнопка на платі| INT[Внутрішній pull-up ~45к]
    LEN -->|I2C до 400 кГц| EXT47[Зовнішній 4.7к до 3.3V]
    LEN -->|Шлейф > 20 см| EXT22[Зовнішній 2.2к + 100нФ]
    Q --> V5{Сигнал 5V?}
    V5 -->|Повільно| DIV[Дільник (напр. 1к/2к)]
    V5 -->|Швидко/двобічно| TXS[TXS0108 / TXB0104]
    V5 -->|Тільки вхід| OD[Open-drain + pull-up до 3.3V]
```

### RC-дебаунс кнопки (коли софта мало)

```text
GPIO ──[10к pull-up до 3.3V]──┬──[1к]──┬──► вхід
                              │        │
                           кнопка   [100нФ до GND]
                              │        │
                             GND      GND
```

## Типові помилки

| # | Помилка | Чому погано | Як правильно |
| --- | --- | --- | --- |
| 1 | I2C тільки на внутрішніх pull | ~45к за слабкі → NACK на 400 кГц | Зовнішні 4.7к до 3.3V |
| 2 | Pull-up до 5V на SDA/SCL | 5V на GPIO через pull! | Pull ТІЛЬКИ до 3.3V |
| 3 | Дільник без запасу на 5V-логіку | 5.5V замість 5V → 3.6V на піні | Рахувати на 5.5V + TVS |
| 4 | TXS0108 на I2C без pull з обох боків | Не стартує | Pull з ОБОХ сторін (див. 13-02) |
| 5 | Кнопка без debounce | Дзвін контактів = 5 «натискань» | RC + 20-50 мс софтверно |
| 6 | Довга лінія без фільтра | Наведення, хибні фронти | 2.2к + 100нФ біля входу |

## Офіційні джерела

- [ESP32 Datasheet - DC Characteristics](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) - VIH/VIL, pull-струми.
- [TXS0108E datasheet (TI)](https://www.ti.com/product/TXS0108E) - автонапрямний shifter, вимоги до pull.
