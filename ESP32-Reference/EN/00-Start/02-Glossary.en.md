---
title: ESP32 glossary - 90+ terms
description: Glossary of 90+ ESP32 terms covering power, analog, buses, radio, memory and toolchains with links into the reference; shows schematics, code and tables.
tags:

  - esp32
  - esp32/start
  - esp32/glossary

aliases:

  - Glossary
  - Glossary EN
  - Term dictionary

type: reference
lang: en
original: 00-Start/02-Glosariy.md
date-created: 2026-10-08
date: 2026-10-08
---

# ESP32 glossary - 90+ terms

> [!tip] How to use it
> The table is sorted by topic. The link column points into reference sections: start - [[00-Start/01-Yak-koristuvatis-dovidnikom| How to use it]], chips - [[00-Start/03-Porivnyannya-chipiv| Chip comparison]], boards - [[00-Start/04-Devkit-plati| DevKit boards]], SDK - [[00-Start/05-Vibir-seredovischa| Environment choice]], sensor structure - [[_templates/Component-Template.en | Component template]], overview - [[Home.en | Home map]].
>
> [!warning] Voltages in terms
> Wherever TTL, VCC, HIGH appear - for the ESP32 HIGH = 3.3V. 5V TTL (as on Arduino Uno) is **incompatible** with GPIO without level matching. Vin 5V is only an LDO input, not a logic level.

## Core concepts and power

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| GPIO | General-purpose input/output line | Programmable digital pin, 3.3V, max about 12 mA (6 mA or less recommended) | [[00-Start/01-Yak-koristuvatis-dovidnikom| Start]] |
| VCC / VDD | Power supply | For silicon - 3.3V; 5V only on VIN/USB ahead of the LDO | [[00-Start/04-Devkit-plati| DevKit]] |
| GND | Ground | Common point, mandatory between all modules | [[_templates/Component-Template.en | Template]] |
| LDO | Linear regulator | AMS1117/ME6211: 5V to 3.3V, runs hot, about 500 mA max | [[00-Start/04-Devkit-plati| DevKit]] |
| Level-shifter | Level matcher | TXS0108E, BSS138, 1k/2k divider for 5V to 3.3V | [[_templates/Component-Template.en | Template]] |
| Strapping pins | Boot-configuration pins | GPIO0/2/5/12/15: levels at reset define boot/flash | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| EN (CHIP_PU) | Silicon enable | HIGH = run, EN button = reset | [[00-Start/04-Devkit-plati| DevKit]] |
| BOOT (GPIO0) | Boot mode | Hold at reset for download mode | [[00-Start/04-Devkit-plati| DevKit]] |
| eFuse | One-time programmable memory | ADC calibration, flash-encryption keys, USB VID | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| Deep-sleep | Deep sleep | 5-10 µA, ULP/RTC keep running, wake on timer/touch | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| ULP | Ultra-low-power coprocessor | RISC-V/FSM for polling sensors in sleep | [[00-Start/03-Porivnyannya-chipiv| Chips]] |

## Analog peripherals

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| ADC | Analog-to-digital converter | 12-bit, 0-3.3V (via attenuation), nonlinear near the edges | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| ADC attenuation | ADC attenuation | 0/2.5/6/11 dB: ranges up to about 1.1/1.5/2.2/3.3V | [[Home.en | Home map]] |
| DAC | Digital-to-analog converter | 8-bit, GPIO25/26, classic ESP32 only | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| PWM / LEDC | PWM | LEDC up to 40 MHz (theoretical ceiling; in practice hertz/kilohertz), 1-16 bit; for LEDs, servos (50 Hz) | [[00-Start/02-Glosariy| Glossary (this file)]] |
| MCPWM | Motor PWM | Hardware PWM with dead-time for BLDC/H-bridges | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| Touch sensor | Capacitive sensor | T0-T9, deep-sleep wake on touch | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| Hall sensor | Hall sensor | Built into ESP32-Classic, coarse, for demos | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| Vref | ADC reference voltage | About 1.1V internal, varies between chips, calibration needed | [[00-Start/05-Vibir-seredovischa| Environments]] |
| SAR-ADC | Successive-approximation ADC | ESP32 ADC type: 12-bit, fast, nonlinear near scale edges | [[06-Analog/01-ADC.en | ADC]] |
| FOC | Vector motor control | Field-Oriented Control: 3-phase bridge + angle encoder, quiet torque | [[11-Vivid/11-PowerMotion-2.en | Power/Motion]] |
| Deadtime | Switch dead time | Pause between HIGH/LOW of one bridge leg against shoot-through current | [[11-Vivid/11-PowerMotion-2.en | Power/Motion]] |
| StallGuard | Stall detector | TMC2209/5160 feature: stop without an endstop via back-EMF | [[11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.en | Actuators]] |
| RVC | Robot vacuum (BNO08x mode) | Robot Vacuum Cleaner UART mode of BNO08x: quaternions as a ready stream | [[10-Sensors/19-IMU-6-9DOF.en | IMU]] |

## Digital buses

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| I2C | Two-wire bus | SDA/SCL, 100/400 kHz, 4.7k pull-ups to 3.3V | [[_templates/Component-Template.en | Template]] |
| SPI | Fast serial bus | MOSI/MISO/SCK/CS, up to 80 MHz, for displays/Flash | [[_templates/Component-Template.en | Template]] |
| UART | Asynchronous receiver-transmitter | TX/RX, 3.3V, UART0 is the console; do not mix up with RS232 ±12V! | [[00-Start/01-Yak-koristuvatis-dovidnikom| Start]] |
| JTAG | Debug interface | TDI/TDO/TCK/TMS, OpenOCD, for ESP-IDF | [[00-Start/05-Vibir-seredovischa| Environments]] |
| RMT | Pulse modulator | Precise pulses for WS2812, IR, DHT | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| TWAI | CAN controller (Two-Wire Auto Interface) | CAN 2.0, needs a 3.3V transceiver (TJA1050) | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| I2S | Audio bus | INMP441 microphones, MAX98357A DAC | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| 1-Wire | One-wire interface | DS18B20, 4.7k pull-up to 3.3V, not 5V! | [[_templates/Component-Template.en | Template]] |
| USB-OTG / CDC | USB | S3/C3/H2: native USB; Classic only via CP2102/CH340 | [[00-Start/04-Devkit-plati| DevKit]] |
| CP2102 / CH340 | USB-UART bridge | Converts USB to 3.3V UART for flashing | [[00-Start/04-Devkit-plati| DevKit]] |

## Radio and networking

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| STA | Wi-Fi client | Connection to a router | [[Home.en | Home map]] |
| AP | Access point | ESP32 serves Wi-Fi (captive portal) | [[Home.en | Home map]] |
| BLE | Bluetooth Low Energy | 4.2/5.0, sensors, provision | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| BT Classic | Classic Bluetooth | ESP32-Classic only (SPP/A2DP) | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| Zigbee / Thread | Mesh radio | ESP32-H2/C6, 802.15.4 | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| ESP-NOW | Direct radio protocol | P2P without a router, low latency | [[Home.en | Home map]] |
| OTA | Over-the-air update | Two OTA slots, rollback on failure | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Provisioning | First-time Wi-Fi setup | BLE / SoftAP + HTTP | [[Home.en | Home map]] |
| RSSI | Signal level | dBm, -30 excellent, -90 edge | [[Home.en | Home map]] |
| LWT | Last will message | MQTT `offline` message the broker sends when a node drops | [[15-Protocols/01-MQTT.en | MQTT]] |
| QoS | Delivery guarantee level | MQTT 0 (no guarantees) / 1 (at least once) / 2 (exactly once) | [[15-Protocols/01-MQTT.en | MQTT]] |
| Retain | Retained message | Broker holds the latest one for new subscribers; state/config only | [[15-Protocols/01-MQTT.en | MQTT]] |
| Keepalive | Liveness interval | MQTT PINGREQ every 15-60 s, catches drops | [[15-Protocols/01-MQTT.en | MQTT]] |
| GATT | BLE attribute profile | Services/characteristics/descriptors, read/write/notify ops | [[05-Radio/02-BLE-Bluetooth.en | BLE]] |
| MTU | BLE packet size | 23 bytes by default, up to 517 after exchange | [[05-Radio/02-BLE-Bluetooth.en | BLE]] |
| Bonding | BLE bonding | Storing encryption keys, passkey JustWorks | [[05-Radio/02-BLE-Bluetooth.en | BLE]] |
| RainMaker | Espressif cloud | Provisioning + MQTT + OTA + voice assistants out of the box | [[15-Protocols/04-Provisioning.en | Provisioning]] |
| BluFi | Setup over BLE | Espressif protocol: SSID/password over a BLE protocomm channel | [[15-Protocols/04-Provisioning.en | Provisioning]] |
| Matter | Smart-home standard | IP protocol over Thread/WiFi, commissioning over BLE | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| Thread | 802.15.4 mesh | IPv6 grid for H2/C6, border router on WiFi | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| mDNS | Local names | `esp32.local` in one subnet, _http._tcp services | [[15-Protocols/03-mDNS-NTP-TLS.en | mDNS/NTP/TLS]] |
| SNTP | Time sync | UDP 123, UTC + TZ Europe/Kyiv, mandatory before TLS | [[15-Protocols/03-mDNS-NTP-TLS.en | mDNS/NTP/TLS]] |
| SSE | Server events | One-way text stream at `/events` for browser telemetry | [[15-Protocols/02-HTTP-WebSocket.en | HTTP]] |
| Backoff | Exponential pause | Reconnects at 1/2/4/8 s against reconnect storms | [[15-Protocols/01-MQTT.en | MQTT]] |
| Broker | Message server | Mosquitto: takes PUBLISH, fans out SUB by topic | [[15-Protocols/01-MQTT.en | MQTT]] |
| Gateway | Protocol gateway | LoRa to MQTT, Modbus to WiFi, BLE to cloud bridge | [[15-Protocols/05-Cloud-Pipeline.en | Cloud]] |

## Memory and firmware

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| Flash | Program flash memory | 4-16 MB external SPI-Flash | [[00-Start/05-Vibir-seredovischa| Environments]] |
| PSRAM | External RAM | 2-8 MB (WROVER), for cameras/displays | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| SRAM | Internal RAM | 320-512 KB depending on chip | [[00-Start/03-Porivnyannya-chipiv| Chips]] |
| NVS | Non-volatile storage | Key-value in Flash (Wi-Fi, calibration) | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Partitions | Partition table | NVS/OTA/app/SPIFFS/LittleFS | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Bootloader | Bootloader | 2nd-stage, app choice, download mode | [[00-Start/04-Devkit-plati| DevKit]] |
| esptool | Flashing utility | `esptool.py --chip esp32 write_flash` | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Download mode | Flashing mode | GPIO0=LOW + reset, 921600/460800 baud | [[00-Start/04-Devkit-plati| DevKit]] |
| LittleFS / SPIFFS | Filesystems | LittleFS is modern, SPIFFS is legacy | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Core dump | Crash snapshot | For panic analysis via ESP-IDF | [[00-Start/05-Vibir-seredovischa| Environments]] |
| OTA-rollback | Firmware rollback | Return to the previous OTA slot if the new one never marks valid | [[08-Memory/03-OTA.en | OTA]] |
| Octal PSRAM | Fast external RAM | 8-bit OPI bus at 120 MHz for LVGL/cameras on S3 | [[01-Hardware/06-Flash-PSRAM.en | Flash/PSRAM]] |

## Toolchains and tools

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| ESP-IDF | Official Espressif framework | C/C++, FreeRTOS, full control | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Arduino-core | Arduino core for ESP32 | `setup()/loop()`, fast start | [[00-Start/05-Vibir-seredovischa| Environments]] |
| MicroPython | Python for microcontrollers | REPL, fast prototypes, slower | [[00-Start/05-Vibir-seredovischa| Environments]] |
| PlatformIO | Build system | VS Code, handy libraries, CI | [[00-Start/05-Vibir-seredovischa| Environments]] |
| FreeRTOS | Real-time OS | Tasks, queues, semaphores; dual-core | [[00-Start/05-Vibir-seredovischa| Environments]] |
| OpenOCD | Debugger | GDB + JTAG | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Dataview | Obsidian plugin | SQL-like queries over notes | [[00-Start/01-Yak-koristuvatis-dovidnikom| Start]] |
| MOC | Content map | [[Home.en | Home map]] - the central MOC | [[Home.en | Home map]] |
| WROOM / WROVER | Espressif modules | WROOM without PSRAM, WROVER with PSRAM | [[00-Start/04-Devkit-plati| DevKit]] |
| DevKit | Dev board | Module + USB-UART + LDO + buttons | [[00-Start/04-Devkit-plati| DevKit]] |
| HMI | Human-machine interface | Nextion/DWIN displays, buttons, encoders for control | [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.en | Audio/HMI]] |
| InfluxDB | Time-series database | Stores MQTT telemetry for Grafana charts | [[15-Protocols/05-Cloud-Pipeline.en | Cloud]] |
| Pull-up/down | Pull resistors | Internal about 45k are weak; I2C needs external 4.7k | [[_templates/Component-Template.en | Template]] |
| Watchdog (WDT) | Watchdog timer | Reset on hang; feed it in `loop()` | [[00-Start/05-Vibir-seredovischa| Environments]] |
| Brownout | Power dip | Reset at VDD below 2.43V; 470 µF capacitor | [[00-Start/04-Devkit-plati| DevKit]] |
| Dropout (LDO) | Regulator dropout | Vin minus Vout headroom for regulation: AMS1117 about 1.1V, ME6211 about 0.3V | [[13-Power-Modules/04-LDO-Buck-XL4015-Protect.en | Protection]] |
| MPPT | Solar peak-power tracking | CN3791 holds the panel at the Pmax point, CC/CV charge | [[13-Power-Modules/01-Buck-Boost-Solar.en | Buck/Solar]] |
| BMS | Battery protection board | DW01+FS8205: cut-off on overcharge/overdischarge/current | [[13-Power-Modules/03-TP4056-IP5306-BMS-UPS.en | Charging/BMS]] |
| PTC | Self-healing fuse | Polymer type: resistance grows on current overheat | [[13-Power-Modules/04-LDO-Buck-XL4015-Protect.en | Protection]] |
| TVS | Surge suppressor | SMBJ5.0A quenches ESD/spikes in nanoseconds | [[13-Power-Modules/04-LDO-Buck-XL4015-Protect.en | Protection]] |

> [!example] Photo/schematic: ![[assets/img/placeholder.png]]
> Reference level schematic for the glossary:

| ESP32 | 3.3V module | 5V module |
| --- | --- | --- |
| 3V3 | VCC | - (no signals!) |
| GND | GND | GND (common) |
| GPIO (3.3V) | SDA/SCL/TX/RX directly | Only via level-shifter |
| 5V (VIN) | - | 5V power VCC |
| EN/BOOT | - | Buttons for flashing |

## See also

- [[Home.en | Home map]]
- [[00-Start/01-Yak-koristuvatis-dovidnikom| How to use it]]
- [[00-Start/03-Porivnyannya-chipiv| Chip comparison]]
- [[00-Start/04-Devkit-plati| DevKit boards]]
- [[00-Start/05-Vibir-seredovischa| Environment choice]]
- [[_templates/Component-Template.en | Component template]]
