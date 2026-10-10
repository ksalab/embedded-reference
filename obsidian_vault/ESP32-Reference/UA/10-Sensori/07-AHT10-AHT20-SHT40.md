---
description: AHT10, AHT20 та SHT40 - компактні цифрові I2C-сенсори відносної вологості та температури. Наступне покоління після DHT11/DHT22: немає часозалежного однопровідного протоколу, працюють...
title: AHT10 / AHT20 / SHT40 - I2C датчики вологості та температури
tags: [esp32, sensor, aht10, aht20, sht40, humidity, temperature, i2c]
category: Sensori
date-created: 2026-09-27
---

# AHT10 / AHT20 / SHT40 - I2C датчики вологості та температури

![[assets/img/aht10-scheme.png|500]]
*Рис. 1. Підключення модуля AHT10/AHT20/SHT40 до ESP32 по I2C.*

## Призначення

AHT10, AHT20 та SHT40 - компактні цифрові I2C-сенсори відносної вологості та температури. Наступне покоління після DHT11/DHT22: немає часозалежного однопровідного протоколу, працюють на стандартній шині I2C, стабільно уживаються з FreeRTOS та Wi-Fi. Застосування: кімнатні метеостанції, теплиці, інкубатори, HVAC-контроль, вуличні IoT-вузли з deep-sleep, калібрування дешевших датчиків.

AHT10 - найдешевший (~$1), AHT20 - покращена версія з кращою стабільністю, SHT40 (Sensirion) - прецизійний наступник SHT31 з точністю ±1.8 %RH.

> На відміну від DHT, ці сенсори не блокують планувальник очікуванням мікросекундних імпульсів - їх можна безпечно опитувати з будь-якого завдання ESP-IDF.

## Характеристики

| Параметр | AHT10 | AHT20 | SHT40-AD1B |
| --- | --- | --- | --- |
| Діапазон температури | −40…+85 °C | −40…+85 °C | −40…+125 °C |
| Точність температури | ±0.3 °C | ±0.3 °C | ±0.2 °C |
| Діапазон вологості | 0…100 %RH | 0…100 %RH | 0…100 %RH |
| Точність вологості | ±2 %RH | ±2 %RH | ±1.8 %RH |
| Роздільна здатність | 0.01 °C / 0.024 %RH | 0.01 °C / 0.024 %RH | 0.01 °C / 0.01 %RH |
| Інтерфейс | I2C, 100 кГц | I2C, до 400 кГц | I2C, до 1 МГц |
| I2C-адреса | 0x38 (фіксована) | 0x38 (фіксована) | 0x44 (0x45 для варіанта BD1B) |
| Живлення | 1.8-3.6 В (модулі з LDO: 3.3-5 В) | 2.2-5.5 В | 1.08-3.6 В (модулі: 3.3-5 В) |
| Струм (вимір / сон) | 23 мкА / 0.25 мкА | 23 мкА / 0.25 мкА | 0.4 мА / 0.15 мкА |
| Час вимірювання | ~75 мс | ~75 мс | ~4-9 мс |
| Калібрування | Біт калібрування 0x08 + ініціалізація 0xBE | Автокалібрування після 0xBE | Заводське, не потребує |
| Ціна (орієнтовно) | ~$1 | ~$1.5-2 | ~$4-5 |

### Порівняння з DHT та BME280

| Критерій | DHT22 | AHT20 | SHT40 | BME280 |
| --- | --- | --- | --- | --- |
| Протокол | 1-Wire власний | I2C | I2C | I2C/SPI |
| Стабільність під RTOS | Низька (таймінги) | Висока | Висока | Висока |
| Тиск | Немає | Немає | Немає | Є |
| Швидкість | 0.5 Гц | ~10 Гц | ~100 Гц | ~50 Гц |
| Для вулиці | Середньо | Добре + кожух | Добре + фільтр PTFE | Добре |
| Висновок | Бюджетний варіант | Оптимум ціна/якість | Еталон вологості | Все-в-одному з тиском |

## Легенда пінів модуля

| Пін | Тип | Куди | Примітка |
| --- | --- | --- | --- |
| VCC (VIN) | Живлення | 3V3 ESP32 | 3.3 В; модулі GY-AHT з LDO терплять 5 В, але ліпше 3.3 В |
| GND | Земля | GND ESP32 | Спільна земля, короткий провід |
| SCL | Вхід, I2C clock | GPIO22 | Pull-up 4.7-10 кОм (зазвичай вже на модулі) |
| SDA | Двонапрямлений, I2C data | GPIO21 | Pull-up 4.7-10 кОм (зазвичай вже на модулі) |
| ADDR (тільки SHT40) | Вхід вибору адреси | GND / VCC / NC | GND → 0x44, VCC → 0x45; на дешевих модулях виведена не завжди |
| NC | - | Не підключати | Залишити вільним |

> AHT10/AHT20 мають фіксовану адресу 0x38 - два такі датчики на одній шині неможливі без I2C-мультиплексора TCA9548A.

## Схема підключення

| ESP32 | Модуль | Примітка |
| --- | --- | --- |
| 3V3 | VCC | Живлення 3.3 В, струм < 1 мА |
| GND | GND | Спільна земля |
| GPIO22 | SCL | Апаратний I2C0 SCL |
| GPIO21 | SDA | Апаратний I2C0 SDA |
| - | VCC-GND | Кераміка 100 нФ біля модуля при довгих лініях |

### ASCII-схема

```text
         ESP32 DevKit              GY-AHT / SHT40
     +----------------+          +--------------+
     |             3V3|----------|VCC           |
     |                |          |              |
     |            GND |----------|GND           |
     |                |          |              |
     |     GPIO22 SCL |----------|SCL  (pull-up)|
     |     GPIO21 SDA |----------|SDA  (pull-up)|
     +----------------+          +--------------+
         I2C0, 100 kHz          addr: 0x38 / 0x44
```

### Mermaid

```mermaid
graph LR
    ESP32[ESP32 DevKit] -->|3V3| VCC[VCC модуля]
    ESP32 -->|GND| GND[GND модуля]
    ESP32 -->|GPIO22 SCL| SCL[SCL]
    ESP32 -->|GPIO21 SDA| SDA[SDA]
    SCL -. pull-up 4.7k .-> VCC
    SDA -. pull-up 4.7k .-> VCC
```

## Код ESP-IDF

```c
#include "driver/i2c.h"
#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define I2C_PORT I2C_NUM_0
#define AHT_ADDR 0x38
static const char *TAG = "aht";

static esp_err_t aht_init(void)
{
    // Ініціалізація калібрування: 0xBE 0x08 0x00
    uint8_t cmd[3] = {0xBE, 0x08, 0x00};
    return i2c_master_write_to_device(I2C_PORT, AHT_ADDR, cmd, 3, 100);
}

static esp_err_t aht_read(float *t, float *h)
{
    uint8_t trig[3] = {0xAC, 0x33, 0x00};
    ESP_ERROR_CHECK(i2c_master_write_to_device(I2C_PORT, AHT_ADDR, trig, 3, 100));
    vTaskDelay(pdMS_TO_TICKS(80)); // очікування вимірювання
    uint8_t d[6] = {0};
    ESP_ERROR_CHECK(i2c_master_read_from_device(I2C_PORT, AHT_ADDR, d, 6, 100));
    if (d[0] & 0x80) return ESP_ERR_TIMEOUT; // біт зайнятості
    uint32_t raw_h = ((uint32_t)(d[1] << 12)) | (d[2] << 4) | (d[3] >> 4);
    uint32_t raw_t = ((uint32_t)((d[3] & 0x0F) << 16)) | (d[4] << 8) | d[5];
    *h = raw_h * 100.0f / 1048576.0f;
    *t = raw_t * 200.0f / 1048576.0f - 50.0f;
    return ESP_OK;
}

void app_main(void)
{
    i2c_config_t cfg = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = GPIO_NUM_21,
        .scl_io_num = GPIO_NUM_22,
        .sda_pullup_en = GPIO_PULLUP_ENABLE,
        .scl_pullup_en = GPIO_PULLUP_ENABLE,
        .master.clk_speed = 100000,
    };
    i2c_param_config(I2C_PORT, &cfg);
    i2c_driver_install(I2C_PORT, cfg.mode, 0, 0, 0);
    vTaskDelay(pdMS_TO_TICKS(50));
    aht_init();
    vTaskDelay(pdMS_TO_TICKS(50));
    for (;;) {
        float t = 0, h = 0;
        if (aht_read(&t, &h) == ESP_OK)
            ESP_LOGI(TAG, "T=%.2f C  H=%.2f %%", t, h);
        else
            ESP_LOGW(TAG, "AHT зайнятий, повтор");
        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}
```

## Код Arduino

```cpp
#include <Wire.h>
#include <Adafruit_AHTX0.h>
#include <Adafruit_SHT4x.h>

Adafruit_AHTX0 aht;
Adafruit_SHT4x sht4 = Adafruit_SHT4x();

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  if (aht.begin()) {
    Serial.println("AHT10/AHT20 знайдено (0x38)");
  } else {
    Serial.println("AHT не знайдено!");
  }
  if (sht4.begin()) {
    Serial.println("SHT40 знайдено (0x44)");
    sht4.setPrecision(SHT4X_HIGH_PRECISION);
    sht4.setHeater(SHT4X_NO_HEATER);
  }
}

void loop() {
  sensors_event_t h, t;
  if (aht.getStatus() != 0xFF) {
    aht.getEvent(&h, &t);
    Serial.printf("AHT: T=%.2f C H=%.2f %%\n", t.temperature, h.relative_humidity);
  }
  if (sht4.getEvent(&h, &t)) {
    Serial.printf("SHT40: T=%.2f C H=%.2f %%\n", t.temperature, h.relative_humidity);
  }
  delay(2000);
}
```

## Код MicroPython

```python
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
print("I2C:", [hex(a) for a in i2c.scan()])  # чекаємо 0x38 або 0x44

# --- AHT10/AHT20 без бібліотеки ---
ADDR = 0x38
i2c.writeto(ADDR, bytes([0xBE, 0x08, 0x00]))  # калібрування
time.sleep_ms(50)

while True:
    i2c.writeto(ADDR, bytes([0xAC, 0x33, 0x00]))
    time.sleep_ms(80)
    d = i2c.readfrom(ADDR, 6)
    raw_h = (d[1] << 12) | (d[2] << 4) | (d[3] >> 4)
    raw_t = ((d[3] & 0x0F) << 16) | (d[4] << 8) | d[5]
    print("T={:.2f} H={:.2f}".format(raw_t * 200 / 1048576 - 50, raw_h * 100 / 1048576))
    time.sleep(2)

# --- SHT40 (драйвер sht4x.py) ---
# import sht4x
# s = sht4x.SHT4X(i2c)
# print(s.measurements)
```

### Споріднені моделі: SHT20 / Si7021 / DHT12

| Параметр | SHT20 | Si7021 | DHT12 |
| --- | --- | --- | --- |
| Виробник | Sensirion (попередник SHT3x) | Silicon Labs | Aosong (I2C-версія DHT11) |
| Діапазон / точність RH | 0…100 %RH / ±3 %RH | 0…100 %RH / ±3 %RH | 20…95 %RH / ±5 %RH |
| Температура | −40…+125 °C / ±0.3 °C | −40…+85 °C / ±0.4 °C | −20…+60 °C / ±0.5 °C |
| Інтерфейс | I2C 0x40 | I2C 0x40 (+ нагрівач) | I2C 0x5C (4-піновий модуль) |
| Живлення | 2.1-3.6 В | 1.9-3.6 В | 3.3-5 В |
| Коли брати | Дешевий I2C без таймінгів DHT | Є вбудований нагрівач проти конденсату | Перехід з DHT11 на шину без зміни коду логіки |

```text
ESP32 GPIO21 (SDA) ──► SDA SHT20/Si7021/DHT12 (pull-up 4.7к до 3V3)
ESP32 GPIO22 (SCL) ──► SCL (pull-up 4.7к до 3V3)
3V3 ──► VCC, GND ──► GND (DHT12-модуль може мати 5V LDO — перевірити перемичку!)
```

> SHT20 vs SHT40: той же драйвер, гірша точність - для теплиць вистачає, для лабораторії беріть SHT40.

## Типові помилки

| № | Помилка | Симптом | Рішення |
| --- | --- | --- | --- |
| 1 | Не відправлена команда калібрування 0xBE | AHT10 повертає 0x00 або «залиплі» значення | Після power-on завжди слати 0xBE 0x08 0x00 і чекати 50 мс |
| 2 | Читання раніше 75 мс | Біт busy (0x80) встановлений, дані старі | Затримка 80 мс між тригером 0xAC і читанням |
| 3 | Конфлікт адрес 0x38 | Два AHT на шині, видно лише один | Один сенсор на шину або мультиплексор TCA9548A |
| 4 | Швидкість I2C 400 кГц для AHT10 | NACK, зависання шини | AHT10 - лише 100 кГц; AHT20/SHT40 - до 400 кГц / 1 МГц |
| 5 | Живлення 5 В без LDO на голому сенсорі | Перегрів, дрейф показань | Голі AHT10 - максимум 3.6 В; модулі GY - можна 5 В |
| 6 | Конденсат після вулиці | Вологість 100 % «залипає» | Просушити, у SHT40 увімкнути heater на 1 с (SHT4X_HIGH_HEATER_1S) |
| 7 | Плутанина SHT40 0x44 vs 0x45 | `i2c.scan()` порожній на 0x44 | Перевірити варіант чипа (AD1B → 0x44, BD1B → 0x45), сканувати шину |
| 8 | DHT12 замість SHT20 в коді | Невірна адреса/формат даних | DHT12 - 0x5C і свій формат, SHT20/Si7021 - 0x40; перевірити маркування чипа |

## Офіційні джерела

- [SHT40 - каталог і даташит (Sensirion)](https://sensirion.com/products/catalog/SHT40) - офіційні характеристики та документація.
- [SHT40 - живе фото (Adafruit)](https://www.adafruit.com/product/4885) - сторінка товару з фото.
- [Гайд SHT40/SHT41/SHT45 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor) - підключення, приклади.
- AHT10/AHT20 Datasheet (ASAIR) - `перевірити вручну`.

## Див. також

- [[10-Sensori/01-DHT11-DHT22]]
- [[10-Sensori/03-BME280-BMP280-SHT31]]
- [[04-Shini/03-I2C|I2C]]
- [[10-Sensori/02-DS18B20|DS18B20]]
- [[10-Sensori/04-MPU6050|MPU6050]]
- [[10-Sensori/06-INA219-HX711-BH1750]]
- [[06-Analog/01-ADC|ADC]]
