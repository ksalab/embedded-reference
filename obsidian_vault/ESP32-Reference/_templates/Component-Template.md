---
title: Шаблон компонента (службовий)
tags:

  - esp32/template
  - esp32/component

aliases:

  - Component Template
  - Шаблон компонента

type: template
---

# Шаблон компонента

> [!tip] Як використовувати
> Скопіюйте цей файл для кожного нового датчика/модуля в `05-Sensors/` або `06-Actuators/`. Заповніть усі таблиці. Приклади структури дивіться у [[00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись]] та термінологію у [[00-Start/02-Glosariy|Глосарії]]. Вибір чипа звіряйте з [[00-Start/03-Porivnyannya-chipiv|Порівнянням чипів]], плату - з [[00-Start/04-Devkit-plati|DevKit]], середовище - з [[00-Start/05-Vibir-seredovischa|Вибором середовища]].
>
> [!warning] 3.3V логіка!
> Усі GPIO ESP32 - 3.3V, **не 5V-толерантні**. Якщо модуль має 5V живлення (наприклад HC-SR04, реле 5V), сигнальні лінії до ESP32 узгоджуйте через дільник або TXS0108E. Інакше - пошкодження кристала.

## Призначення

Коротко: що робить модуль, інтерфейс (I2C/SPI/UART/1-Wire/аналог), напруга живлення, типові задачі.

| Параметр | Значення |
| --- | --- |
| Інтерфейс | I2C / SPI / UART (зазначити) |
| Живлення модуля | 3.3V / 5V (зазначити) |
| Рівень сигналів | 3.3V (обов'язково для ESP32) |
| Сумісність | ESP32 / S3 / C3 ([[00-Start/03-Porivnyannya-chipiv | таблиця чипів]]) |

## Характеристики

| Характеристика | Значення | Примітка |
| --- | --- | --- |
| Напруга живлення | 3.3-5.0 V | LDO на модулі? |
| Споживання | __ mA | Пік / сон |
| Діапазон вимірювання | __ | Точність |
| Інтерфейс | I2C 0x__ | Pull-up потрібні? |
| Робоча температура | -40…+85 °C | - |

> [!tip] Живлення
> Живіть ESP32 DevKit через USB 5V або VIN 5V (далі AMS1117 → 3.3V), див. [[00-Start/04-Devkit-plati|DevKit плати]]. Сам кристал і GPIO - тільки 3.3V.

## Розпіновка модуля

| Пін модуля | Призначення | Куди на ESP32 |
| --- | --- | --- |
| VCC | Живлення | 3V3 або 5V (за даташитом) |
| GND | Земля | GND |
| SDA / MOSI / TX | Дані | GPIO21 / GPIO23 / GPIO17 |
| SCL / SCK / RX | Такт / дані | GPIO22 / GPIO18 / GPIO16 |

## Схема підключення

> [!example] Фото/схема: ![[assets/img/placeholder.png]]
> Замініть на реальне фото макету та схему Fritzing/KiCad.

| ESP32 DevKit | Модуль | Примітка |
| --- | --- | --- |
| 3V3 | VCC (якщо 3.3V модуль) | Не перевищувати 500 мА з LDO |
| 5V (VIN) | VCC (якщо 5V модуль) | Тільки живлення, не сигнали! |
| GND | GND | Спільна земля |
| GPIO21 | SDA | Pull-up 4.7 кОм до 3.3V |
| GPIO22 | SCL | Pull-up 4.7 кОм до 3.3V |
| GPIO__ | ALERT/INT | Через дільник якщо 5V |

> [!warning] 5V модулі
> Реле, HC-SR04 Echo (5V), WS2812 DIN через 5V-логіку - не підключати безпосередньо. Використовуйте дільник 1k/2k або level-shifter. Перевірте мультиметром рівень HIGH перед підключенням до GPIO.

## Код ESP-IDF

```c
#include "driver/i2c.h"
#define I2C_PORT I2C_NUM_0
#define SDA_PIN 21
#define SCL_PIN 22
void app_main(void) {
    i2c_config_t cfg = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = SDA_PIN,
        .scl_io_num = SCL_PIN,
        .sda_pullup_en = GPIO_PULLUP_ENABLE,
        .scl_pullup_en = GPIO_PULLUP_ENABLE,
        .master.clk_speed = 100000,
    };
    i2c_param_config(I2C_PORT, &cfg);  // IDF 4.x legacy; у 5.x - i2c_new_master_bus() (див. 99-Dodatki/07-Versions)
    i2c_driver_install(I2C_PORT, cfg.mode, 0, 0, 0);
}
```

## Код Arduino

```cpp
#include <Wire.h>
void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22); // SDA, SCL
}
void loop() {
  Wire.beginTransmission(0x48);
  Wire.endTransmission();
  delay(1000);
}
```

## Код MicroPython

```python
from machine import I2C, Pin
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=100000)
print(i2c.scan())
```

Детальніше про середовища: [[00-Start/05-Vibir-seredovischa|Вибір середовища]].

## Типові помилки

| Симптом | Причина | Рішення |
| --- | --- | --- |
| `ENOMEM` / NACK на I2C | Немає pull-up, 5V на шині | Pull-up 4.7к до 3.3V, прибрати 5V pull-up з модуля |
| Сміття в UART | Різний baud, 5V TX | Зрівняти baud, level-shift |
| ESP32 гріється / згорів | 5V на GPIO | Заміна чипа; надалі тільки 3.3V |
| Не сканується I2C | Не той адрес, поганий GND | `i2c.scan()`, перевірити GND |

## Див. також

- [[00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись довідником]]
- [[00-Start/02-Glosariy|Глосарій]]
- [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]]
- [[00-Start/04-Devkit-plati|DevKit плати]]
- [[00-Start/05-Vibir-seredovischa|Вибір середовища]]
- [[Home|Головна карта довідника]]
