---
title: Вибір середовища - ESP-IDF vs Arduino vs MicroPython vs PlatformIO
tags:

  - esp32
  - esp32/start
  - esp32/firmware
  - esp32/esp-idf
  - esp32/arduino
  - esp32/micropython
  - esp32/platformio

aliases:

  - Вибір середовища
  - 05-Vibir-seredovischa
  - ESP-IDF vs Arduino

type: guide
---

# Вибір середовища - ESP-IDF vs Arduino vs MicroPython vs PlatformIO

EN version: `00-Start/05-Environment-Choice.en.md`

> [!tip] Правило вибору за 10 секунд
> Продакшн/робота - **ESP-IDF**. Швидкий прототип/Arduino-бекграунд - **Arduino-core**. Навчання/тест датчика за 5 хв - **MicroPython**. Багато бібліотек/команда - **PlatformIO**. Деталі заліза - [Порівняння чипів](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) та [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md), терміни - [Глосарій](../../../ESP32-Reference/00-Start/02-Glosariy.md), структура - [Як користуватись](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md), карта - [Home](../../../ESP32-Reference/Home.md).
>
> [!warning] Незалежно від середовища - 3.3V!
> Жодне SDK не врятує GPIO від 5V. `digitalWrite()`/`gpio_set_level()`/`Pin.value()` керують піном 3.3V. Датчики описуйте за [Шаблоном компонента](../../../ESP32-Reference/_templates/Component-Template.md) з узгодженням рівнів.

## Порівняльна таблиця

| Критерій | ESP-IDF 5.x | Arduino-core 3.x | MicroPython 1.22+ | PlatformIO |
| --- | --- | --- | --- | --- |
| Мова | C/C++ | C++ (`setup/loop`) | Python (REPL) | C++ / IDF / MicroPython |
| Поріг входу | Високий | Низький | Дуже низький | Середній |
| Контроль заліза | Повний (FreeRTOS, ULP, eFuse) | Середній | Обмежений | Як у базового фреймворку |
| Wi-Fi/OTA/NVS | `esp_wifi`, `esp_ota`, `nvs_flash` | `WiFi.h`, `ArduinoOTA` | `network`, `ota` (обмеж.) | Ті ж бібліотеки |
| Налагодження | GDB+JTAG, coredump | Serial | REPL + Serial | GDB + Serial |
| Швидкість роботи | Максимальна | Висока | У 10-50 разів повільніша | Як база |
| Розмір flash | ~200 КБ hello-world | ~250 КБ | ~1.5 МБ прошивка + скрипти | Як база |
| Бібліотеки | Компоненти IDF | 10000+ Arduino | Обмежені модулі | Registry PIO |
| CI/прод | Менюконфіг, SBOM, підпис | Простіше, але грубіше | Рідко прод | Ідеально для CI |
| Коли брати | Прод, BLE-Mesh, ULP, Matter | Прототип за вечір, уроки | Тест датчика, навчання | Команда, багато плат |

## Коли що брати

| Задача | Рекомендація |
| --- | --- |
| Серійний пристрій, deep-sleep мкА, OTA з відкатом | ESP-IDF, див. [вибір чипа C3/S3](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Швидкий MQTT-датчик, WS2812, серво | Arduino-core |
| Перевірити I2C-адресу за 2 хвилини | MicroPython `i2c.scan()` |
| Один код на ESP32 + STM32 + AVR | PlatformIO |
| Камера + LVGL + PSRAM | ESP-IDF або Arduino на S3 |

## Установка коротко

| Середовище | Команди |
| --- | --- |
| ESP-IDF | `git clone esp-idf; ./install.sh esp32s3; . export.sh; idf.py create-project demo; idf.py -p /dev/ttyUSB0 flash monitor` |
| Arduino IDE | Boards Manager → `esp32 by Espressif` → плата `DOIT ESP32 DEVKIT V1` → порт → Upload |
| MicroPython | `esptool --chip esp32 write_flash -z 0x1000 firmware.bin` → `mpremote connect /dev/ttyUSB0 repl` → `import machine` |
| PlatformIO | `pio project init -b esp32dev -o demo; pio run -t upload -t monitor` |

> [!tip] esptool - спільний знаменник
> Усі середовища внизу викликають esptool. Базові команди: `esptool.py --port /dev/ttyUSB0 chip_id`, `read_mac`, `write_flash -z 0x1000 fw.bin`, `erase_flash`. Швидкість знижуйте до 460800/115200 на підробках [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md).
>
> [!example] Той же Blink у 3 SDK
>
> ```cpp
> // Arduino
> void setup(){pinMode(2,OUTPUT);} void loop(){digitalWrite(2,HIGH);delay(500);digitalWrite(2,LOW);delay(500);}
> ```
>
> ```c
> // ESP-IDF
> gpio_set_direction(2,GPIO_MODE_OUTPUT);
> while(1){gpio_set_level(2,1);vTaskDelay(pdMS_TO_TICKS(500));gpio_set_level(2,0);vTaskDelay(pdMS_TO_TICKS(500));}
> ```
>
> ```python
> # MicroPython
> from machine import Pin; import time
> led=Pin(2,Pin.OUT)
> while True: led.on(); time.sleep(0.5); led.off(); time.sleep(0.5)
> ```

## Таблиця переходу між SDK

| Дія | ESP-IDF | Arduino | MicroPython |
| --- | --- | --- | --- |
| GPIO вихід | `gpio_set_direction/level` | `pinMode/digitalWrite` | `Pin(n, Pin.OUT).on()` |
| ADC | `adc_oneshot_read()` | `analogRead(34)` | `ADC(Pin(34)).read()` |
| I2C скан | `i2c_master_probe()` | `Wire.beginTransmission()` | `I2C(0).scan()` |
| Wi-Fi STA | `esp_wifi_set_mode(WIFI_MODE_STA)` | `WiFi.begin(ssid,pass)` | `WLAN(STA_IF).connect()` |
| NVS | `nvs_set_i32()` | `Preferences.putInt()` | файл `config.json` |

> [!example] Фото/схема: ![](../../../ESP32-Reference/assets/img/placeholder.png)
> Стенд для перевірки всіх SDK (один LED + кнопка):

| ESP32 DevKit | Компонент | Примітка |
| --- | --- | --- |
| GPIO2 | LED вбудований / зовн. через 220 Ом до GND | 3.3V, ~6 мА |
| GPIO0 (BOOT) | Кнопка на платі | Тест входу в усіх SDK |
| 3V3 | VCC макету | - |
| GND | GND макету | Спільна земля |
| TX0/RX0 | USB-UART | Монітор 115200 бод, 3.3V |

## Див. також

- [Головна карта](../../../ESP32-Reference/Home.md)
- [Як користуватись](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md)
- [Глосарій](../../../ESP32-Reference/00-Start/02-Glosariy.md)
- [Порівняння чипів](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md)
- [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md)
- [Шаблон компонента](../../../ESP32-Reference/_templates/Component-Template.md)
