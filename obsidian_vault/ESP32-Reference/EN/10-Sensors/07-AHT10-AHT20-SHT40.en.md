---
description: AHT10, AHT20 and SHT40 - compact digital I2C humidity and temperature sensors. Next generation after DHT11/DHT22: no time-dependent single-wire protocol, work on standard I2C bus, stable with FreeRTOS and Wi-Fi. Applications: room weather stations, greenhouses, incubators, HVAC control, outdoor IoT nodes with deep-sleep, calibration of cheaper sensors.
title: AHT10 / AHT20 / SHT40 - I2C humidity and temperature sensors
tags: [esp32, sensor, aht10, aht20, sht40, humidity, temperature, i2c]
category: Sensori
lang: en
original: 10-Sensors/07-AHT10-AHT20-SHT40.md
date-created: 2026-09-27
date: 2026-10-08
---

# AHT10 / AHT20 / SHT40 - I2C humidity and temperature sensors

![[assets/img/aht10-scheme.png|500]]
*Fig. 1. AHT10/AHT20/SHT40 module connection to ESP32 via I2C.*

## Purpose

AHT10, AHT20 and SHT40 - compact digital I2C humidity and temperature sensors. Next generation after DHT11/DHT22: no time-dependent single-wire protocol, work on standard I2C bus, stable with FreeRTOS and Wi-Fi. Applications: room weather stations, greenhouses, incubators, HVAC control, outdoor IoT nodes with deep-sleep, calibration of cheaper sensors.

AHT10 - cheapest (~$1), AHT20 - improved version with better stability, SHT40 (Sensirion) - precision successor to SHT31 with ±1.8 %RH accuracy.

> Unlike DHT, these sensors do not block the scheduler waiting for microsecond pulses - they can be polled safely from any ESP-IDF task.

## Characteristics

| Parameter | AHT10 | AHT20 | SHT40-AD1B |
| --- | --- | --- | --- |
| Temperature range | −40…+85 °C | −40…+85 °C | −40…+125 °C |
| Temperature accuracy | ±0.3 °C | ±0.3 °C | ±0.2 °C |
| Humidity range | 0…100 %RH | 0…100 %RH | 0…100 %RH |
| Humidity accuracy | ±2 %RH | ±2 %RH | ±1.8 %RH |
| Resolution | 0.01 °C / 0.024 %RH | 0.01 °C / 0.024 %RH | 0.01 °C / 0.01 %RH |
| Interface | I2C, 100 kHz | I2C, up to 400 kHz | I2C, up to 1 MHz |
| I2C address | 0x38 (fixed) | 0x38 (fixed) | 0x44 (0x45 for BD1B variant) |
| Supply | 1.8-3.6 V (modules with LDO: 3.3-5 V) | 2.2-5.5 V | 1.08-3.6 V (modules: 3.3-5 V) |
| Current (measure / sleep) | 23 µA / 0.25 µA | 23 µA / 0.25 µA | 0.4 mA / 0.15 µA |
| Measurement time | ~75 ms | ~75 ms | ~4-9 ms |
| Calibration | Calibration bit 0x08 + init 0xBE | Auto-calibration after 0xBE | Factory, not required |
| Price (approx.) | ~$1 | ~$1.5-2 | ~$4-5 |

### Comparison with DHT and BME280

| Criterion | DHT22 | AHT20 | SHT40 | BME280 |
| --- | --- | --- | --- | --- |
| Protocol | 1-Wire custom | I2C | I2C | I2C/SPI |
| Stability under RTOS | Low (timing) | High | High | High |
| Pressure | No | No | No | Yes |
| Speed | 0.5 Hz | ~10 Hz | ~100 Hz | ~50 Hz |
| Outdoor | Medium | Good + enclosure | Good + PTFE filter | Good |
| Verdict | Budget option | Price/quality optimum | Humidity reference | All-in-one with pressure |

## Module pin legend

| Pin | Type | To | Note |
| --- | --- | --- | --- |
| VCC (VIN) | Power | ESP32 3V3 | 3.3 V; GY-AHT modules with LDO tolerate 5 V, but 3.3 V is better |
| GND | Ground | ESP32 GND | Common ground, short cable |
| SCL | Input, I2C clock | GPIO22 | Pull-up 4.7-10 kΩ (usually already on module) |
| SDA | Bidirectional, I2C data | GPIO21 | Pull-up 4.7-10 kΩ (usually already on module) |
| ADDR (SHT40 only) | Address select input | GND / VCC / NC | GND → 0x44, VCC → 0x45; not always present on cheap modules |
| NC | - | Do not connect | Leave floating |

> AHT10/AHT20 have fixed address 0x38 - two such sensors on one bus are impossible without I2C multiplexer TCA9548A.

## Wiring diagram

| ESP32 | Module | Note |
| --- | --- | --- |
| 3V3 | VCC | 3.3 V supply, current < 1 mA |
| GND | GND | Common ground |
| GPIO22 | SCL | Hardware I2C0 SCL |
| GPIO21 | SDA | Hardware I2C0 SDA |
| - | VCC-GND | Ceramic 100 nF near module for long lines |

### ASCII schema

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
    ESP32[ESP32 DevKit] -->|3V3| VCC[VCC module]
    ESP32 -->|GND| GND[GND module]
    ESP32 -->|GPIO22 SCL| SCL[SCL]
    ESP32 -->|GPIO21 SDA| SDA[SDA]
    SCL -. pull-up 4.7k .-> VCC
    SDA -. pull-up 4.7k .-> VCC
```

## ESP-IDF code

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
    // Calibration init: 0xBE 0x08 0x00
    uint8_t cmd[3] = {0xBE, 0x08, 0x00};
    return i2c_master_write_to_device(I2C_PORT, AHT_ADDR, cmd, 3, 100);
}

static esp_err_t aht_read(float *t, float *h)
{
    uint8_t trig[3] = {0xAC, 0x33, 0x00};
    ESP_ERROR_CHECK(i2c_master_write_to_device(I2C_PORT, AHT_ADDR, trig, 3, 100));
    vTaskDelay(pdMS_TO_TICKS(80)); // wait for measurement
    uint8_t d[6] = {0};
    ESP_ERROR_CHECK(i2c_master_read_from_device(I2C_PORT, AHT_ADDR, d, 6, 100));
    if (d[0] & 0x80) return ESP_ERR_TIMEOUT; // busy bit
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
            ESP_LOGW(TAG, "AHT busy, retry");
        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}
```

## Arduino code

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
    Serial.println("AHT10/AHT20 found (0x38)");
  } else {
    Serial.println("AHT not found!");
  }
  if (sht4.begin()) {
    Serial.println("SHT40 found (0x44)");
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

## MicroPython code

```python
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
print("I2C:", [hex(a) for a in i2c.scan()])  # expect 0x38 or 0x44

# --- AHT10/AHT20 without library ---
ADDR = 0x38
i2c.writeto(ADDR, bytes([0xBE, 0x08, 0x00]))  # calibration
 time.sleep_ms(50)

while True:
    i2c.writeto(ADDR, bytes([0xAC, 0x33, 0x00]))
    time.sleep_ms(80)
    d = i2c.readfrom(ADDR, 6)
    raw_h = (d[1] << 12) | (d[2] << 4) | (d[3] >> 4)
    raw_t = ((d[3] & 0x0F) << 16) | (d[4] << 8) | d[5]
    print("T={:.2f} H={:.2f}".format(raw_t * 200 / 1048576 - 50, raw_h * 100 / 1048576))
    time.sleep(2)

# --- SHT40 (driver sht4x.py) ---
# import sht4x
# s = sht4x.SHT4X(i2c)
# print(s.measurements)
```

### Related models: SHT20 / Si7021 / DHT12

| Parameter | SHT20 | Si7021 | DHT12 |
| --- | --- | --- | --- |
| Manufacturer | Sensirion (predecessor to SHT3x) | Silicon Labs | Aosong (I2C version of DHT11) |
| Range / accuracy RH | 0…100 %RH / ±3 %RH | 0…100 %RH / ±3 %RH | 20…95 %RH / ±5 %RH |
| Temperature | −40…+125 °C / ±0.3 °C | −40…+85 °C / ±0.4 °C | −20…+60 °C / ±0.5 °C |
| Interface | I2C 0x40 | I2C 0x40 (+ heater) | I2C 0x5C (4-pin module) |
| Supply | 2.1-3.6 V | 1.9-3.6 V | 3.3-5 V |
| When to choose | Cheap I2C without DHT timing | Built-in heater against condensation | Transition from DHT11 to bus without changing logic code |

```text
ESP32 GPIO21 (SDA) ──► SDA SHT20/Si7021/DHT12 (pull-up 4.7k to 3V3)
ESP32 GPIO22 (SCL) ──► SCL (pull-up 4.7k to 3V3)
3V3 ──► VCC, GND ──► GND (DHT12 module may have 5V LDO — check jumper!)
```

> SHT20 vs SHT40: same driver, worse accuracy - enough for greenhouses, for lab choose SHT40.

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | Calibration command 0xBE not sent | AHT10 returns 0x00 or "stuck" values | After power-on always send 0xBE 0x08 0x00 and wait 50 ms |
| 2 | Reading before 75 ms | Busy bit (0x80) set, data stale | Delay 80 ms between trigger 0xAC and read |
| 3 | Address conflict 0x38 | Two AHT on bus, only one visible | One sensor per bus or multiplexer TCA9548A |
| 4 | I2C speed 400 kHz for AHT10 | NACK, bus hang | AHT10 - only 100 kHz; AHT20/SHT40 - up to 400 kHz / 1 MHz |
| 5 | 5 V supply on bare sensor without LDO | Overheating, reading drift | Bare AHT10 - max 3.6 V; GY modules - 5 V allowed |
| 6 | Condensation after outdoor use | Humidity 100 % "stuck" | Dry out, on SHT40 turn heater on 1 s (SHT4X_HIGH_HEATER_1S) |
| 7 | Confusing SHT40 0x44 vs 0x45 | `i2c.scan()` empty at 0x44 | Check chip variant (AD1B → 0x44, BD1B → 0x45), scan bus |
| 8 | DHT12 instead of SHT20 in code | Wrong address/data format | DHT12 - 0x5C and its own format, SHT20/Si7021 - 0x40; check chip marking |

## Official sources

- [SHT40 - catalog and datasheet (Sensirion)](https://sensirion.com/products/catalog/SHT40) - official specifications and documentation.
- [SHT40 - live photo (Adafruit)](https://www.adafruit.com/product/4885) - product page with photo.
- [SHT40/SHT41/SHT45 guide with code (Adafruit Learn)](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor) - connection, examples.
- AHT10/AHT20 Datasheet (ASAIR) - `check manually`.

## See also

- [[EN/10-Sensors/01-DHT11-DHT22.en]]
- [[EN/10-Sensors/03-BME280-BMP280-SHT31.en]]
- [[EN/04-Interfaces/03-I2C.en|I2C]]
- [[EN/10-Sensors/02-DS18B20.en|DS18B20]]
- [[EN/10-Sensors/04-MPU6050.en|MPU6050]]
- [[EN/10-Sensors/06-INA219-HX711-BH1750.en]]
- [[06-Analog/01-ADC|ADC]]
