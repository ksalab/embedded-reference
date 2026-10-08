---
title: Environment choice - ESP-IDF vs Arduino vs MicroPython vs PlatformIO
description: Comparison of ESP-IDF, Arduino-core, MicroPython and PlatformIO with install notes and an SDK transition table; shows schematics, code and tables.
tags:

  - esp32
  - esp32/start
  - esp32/firmware
  - esp32/esp-idf
  - esp32/arduino
  - esp32/micropython
  - esp32/platformio

aliases:

  - Environment choice
  - Environment choice EN
  - ESP-IDF vs Arduino

type: guide
lang: en
original: 00-Start/05-Vibir-seredovischa.md
date-created: 2026-10-08
date: 2026-10-08
---

# Environment choice - ESP-IDF vs Arduino vs MicroPython vs PlatformIO

> [!tip] 10-second chooser
> Production/work - **ESP-IDF**. Fast prototype/Arduino background - **Arduino-core**. Learning/5-min sensor test - **MicroPython**. Many libraries/team - **PlatformIO**. Hardware details - [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) and [DevKit boards](../../../ESP32-Reference/00-Start/04-Devkit-plati.md), terms - [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md), structure - [How to use it](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md), map - [Home map](../../../ESP32-Reference/Home.md).
>
> [!warning] 3.3V in every toolchain!
> No SDK saves GPIO from 5V. `digitalWrite()`/`gpio_set_level()`/`Pin.value()` drive a 3.3V pin. Describe sensors via the [Component template](../../../ESP32-Reference/_templates/Component-Template.md) with level matching.

## Comparison table

| Criterion | ESP-IDF 5.x | Arduino-core 3.x | MicroPython 1.22+ | PlatformIO |
| --- | --- | --- | --- | --- |
| Language | C/C++ | C++ (`setup/loop`) | Python (REPL) | C++ / IDF / MicroPython |
| Entry bar | High | Low | Very low | Medium |
| Hardware control | Full (FreeRTOS, ULP, eFuse) | Medium | Limited | Same as base framework |
| Wi-Fi/OTA/NVS | `esp_wifi`, `esp_ota`, `nvs_flash` | `WiFi.h`, `ArduinoOTA` | `network`, `ota` (limited) | Same libraries |
| Debugging | GDB+JTAG, coredump | Serial | REPL + Serial | GDB + Serial |
| Run speed | Top | High | 10-50x slower | Same as base |
| Flash size | About 200 KB hello-world | About 250 KB | About 1.5 MB firmware + scripts | Same as base |
| Libraries | IDF components | 10000+ Arduino | Limited modules | PIO Registry |
| CI/prod | Menuconfig, SBOM, signing | Simpler, but coarser | Rarely prod | Ideal for CI |
| When to take it | Prod, BLE-Mesh, ULP, Matter | Evening prototype, lessons | Sensor test, learning | Team, many boards |

## When to take what

| Task | Advice |
| --- | --- |
| Serial device, µA deep-sleep, OTA with rollback | ESP-IDF, see [C3/S3 chip choice](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Fast MQTT sensor, WS2812, servo | Arduino-core |
| Probe an I2C address in 2 minutes | MicroPython `i2c.scan()` |
| One code for ESP32 + STM32 + AVR | PlatformIO |
| Camera + LVGL + PSRAM | ESP-IDF or Arduino on S3 |

## Install in short

| Toolchain | Commands |
| --- | --- |
| ESP-IDF | `git clone esp-idf; ./install.sh esp32s3; . export.sh; idf.py create-project demo; idf.py -p /dev/ttyUSB0 flash monitor` |
| Arduino IDE | Boards Manager → `esp32 by Espressif` → board `DOIT ESP32 DEVKIT V1` → port → Upload |
| MicroPython | `esptool --chip esp32 write_flash -z 0x1000 firmware.bin` → `mpremote connect /dev/ttyUSB0 repl` → `import machine` |
| PlatformIO | `pio project init -b esp32dev -o demo; pio run -t upload -t monitor` |

> [!tip] esptool - the common base
> All toolchains call esptool underneath. Base commands: `esptool.py --port /dev/ttyUSB0 chip_id`, `read_mac`, `write_flash -z 0x1000 fw.bin`, `erase_flash`. Drop speed to 460800/115200 on clones [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md).
>
> [!example] Same Blink in 3 SDKs
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

## SDK transition table

| Action | ESP-IDF | Arduino | MicroPython |
| --- | --- | --- | --- |
| GPIO out | `gpio_set_direction/level` | `pinMode/digitalWrite` | `Pin(n, Pin.OUT).on()` |
| ADC | `adc_oneshot_read()` | `analogRead(34)` | `ADC(Pin(34)).read()` |
| I2C scan | `i2c_master_probe()` | `Wire.beginTransmission()` | `I2C(0).scan()` |
| Wi-Fi STA | `esp_wifi_set_mode(WIFI_MODE_STA)` | `WiFi.begin(ssid,pass)` | `WLAN(STA_IF).connect()` |
| NVS | `nvs_set_i32()` | `Preferences.putInt()` | `config.json` file |

> [!example] Photo/schematic: ![](../../../ESP32-Reference/assets/img/placeholder.png)
> Bench to verify all SDKs (one LED + button):

| ESP32 DevKit | Part | Note |
| --- | --- | --- |
| GPIO2 | Built-in LED / external via 220 Ohm to GND | 3.3V, about 6 mA |
| GPIO0 (BOOT) | Button on board | Input test in all SDKs |
| 3V3 | Breadboard VCC | - |
| GND | Breadboard GND | Common ground |
| TX0/RX0 | USB-UART | 115200 baud monitor, 3.3V |

## See also

- [Home map](../../../ESP32-Reference/Home.md)
- [How to use it](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md)
- [Glossary](../../../ESP32-Reference/00-Start/02-Glosariy.md)
- [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md)
- [DevKit boards](../../../ESP32-Reference/00-Start/04-Devkit-plati.md)
- [Component template](../../../ESP32-Reference/_templates/Component-Template.md)
