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
> The table is sorted by topic. The link column points into reference sections: start - [How to use it](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md), chips - [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md), boards - [DevKit boards](../../../ESP32-Reference/00-Start/04-Devkit-plati.md), SDK - [Environment choice](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md), sensor structure - [Component template](../../../ESP32-Reference/_templates/Component-Template.md), overview - [Home map](../../../ESP32-Reference/Home.md).
>
> [!warning] Voltages in terms
> Wherever TTL, VCC, HIGH appear - for the ESP32 HIGH = 3.3V. 5V TTL (as on Arduino Uno) is **incompatible** with GPIO without level matching. Vin 5V is only an LDO input, not a logic level.

## Core concepts and power

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| GPIO | General-purpose input/output line | Programmable digital pin, 3.3V, max about 12 mA (6 mA or less recommended) | [Start](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md) |
| VCC / VDD | Power supply | For silicon - 3.3V; 5V only on VIN/USB ahead of the LDO | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| GND | Ground | Common point, mandatory between all modules | [Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| LDO | Linear regulator | AMS1117/ME6211: 5V to 3.3V, runs hot, about 500 mA max | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| Level-shifter | Level matcher | TXS0108E, BSS138, 1k/2k divider for 5V to 3.3V | [Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| Strapping pins | Boot-configuration pins | GPIO0/2/5/12/15: levels at reset define boot/flash | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| EN (CHIP_PU) | Silicon enable | HIGH = run, EN button = reset | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| BOOT (GPIO0) | Boot mode | Hold at reset for download mode | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| eFuse | One-time programmable memory | ADC calibration, flash-encryption keys, USB VID | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Deep-sleep | Deep sleep | 5-10 µA, ULP/RTC keep running, wake on timer/touch | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| ULP | Ultra-low-power coprocessor | RISC-V/FSM for polling sensors in sleep | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |

## Analog peripherals

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| ADC | Analog-to-digital converter | 12-bit, 0-3.3V (via attenuation), nonlinear near the edges | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| ADC attenuation | ADC attenuation | 0/2.5/6/11 dB: ranges up to about 1.1/1.5/2.2/3.3V | [Home map](../../../ESP32-Reference/Home.md) |
| DAC | Digital-to-analog converter | 8-bit, GPIO25/26, classic ESP32 only | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| PWM / LEDC | PWM | LEDC up to 40 MHz (theoretical ceiling; in practice hertz/kilohertz), 1-16 bit; for LEDs, servos (50 Hz) | [Glossary (this file)](../../../ESP32-Reference/00-Start/02-Glosariy.md) |
| MCPWM | Motor PWM | Hardware PWM with dead-time for BLDC/H-bridges | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Touch sensor | Capacitive sensor | T0-T9, deep-sleep wake on touch | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Hall sensor | Hall sensor | Built into ESP32-Classic, coarse, for demos | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Vref | ADC reference voltage | About 1.1V internal, varies between chips, calibration needed | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| SAR-ADC | Successive-approximation ADC | ESP32 ADC type: 12-bit, fast, nonlinear near scale edges | [ADC](../../../ESP32-Reference/06-Analog/01-ADC.md) |
| FOC | Vector motor control | Field-Oriented Control: 3-phase bridge + angle encoder, quiet torque | [Power/Motion](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md) |
| Deadtime | Switch dead time | Pause between HIGH/LOW of one bridge leg against shoot-through current | [Power/Motion](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md) |
| StallGuard | Stall detector | TMC2209/5160 feature: stop without an endstop via back-EMF | [Actuators](../../../ESP32-Reference/11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.md) |
| RVC | Robot vacuum (BNO08x mode) | Robot Vacuum Cleaner UART mode of BNO08x: quaternions as a ready stream | [IMU](../../../ESP32-Reference/10-Sensori/19-IMU-6-9DOF.md) |

## Digital buses

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| I2C | Two-wire bus | SDA/SCL, 100/400 kHz, 4.7k pull-ups to 3.3V | [Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| SPI | Fast serial bus | MOSI/MISO/SCK/CS, up to 80 MHz, for displays/Flash | [Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| UART | Asynchronous receiver-transmitter | TX/RX, 3.3V, UART0 is the console; do not mix up with RS232 ±12V! | [Start](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md) |
| JTAG | Debug interface | TDI/TDO/TCK/TMS, OpenOCD, for ESP-IDF | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| RMT | Pulse modulator | Precise pulses for WS2812, IR, DHT | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| TWAI | CAN controller (Two-Wire Auto Interface) | CAN 2.0, needs a 3.3V transceiver (TJA1050) | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| I2S | Audio bus | INMP441 microphones, MAX98357A DAC | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| 1-Wire | One-wire interface | DS18B20, 4.7k pull-up to 3.3V, not 5V! | [Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| USB-OTG / CDC | USB | S3/C3/H2: native USB; Classic only via CP2102/CH340 | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| CP2102 / CH340 | USB-UART bridge | Converts USB to 3.3V UART for flashing | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |

## Radio and networking

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| STA | Wi-Fi client | Connection to a router | [Home map](../../../ESP32-Reference/Home.md) |
| AP | Access point | ESP32 serves Wi-Fi (captive portal) | [Home map](../../../ESP32-Reference/Home.md) |
| BLE | Bluetooth Low Energy | 4.2/5.0, sensors, provision | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| BT Classic | Classic Bluetooth | ESP32-Classic only (SPP/A2DP) | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Zigbee / Thread | Mesh radio | ESP32-H2/C6, 802.15.4 | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| ESP-NOW | Direct radio protocol | P2P without a router, low latency | [Home map](../../../ESP32-Reference/Home.md) |
| OTA | Over-the-air update | Two OTA slots, rollback on failure | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Provisioning | First-time Wi-Fi setup | BLE / SoftAP + HTTP | [Home map](../../../ESP32-Reference/Home.md) |
| RSSI | Signal level | dBm, -30 excellent, -90 edge | [Home map](../../../ESP32-Reference/Home.md) |
| LWT | Last will message | MQTT `offline` message the broker sends when a node drops | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| QoS | Delivery guarantee level | MQTT 0 (no guarantees) / 1 (at least once) / 2 (exactly once) | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Retain | Retained message | Broker holds the latest one for new subscribers; state/config only | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Keepalive | Liveness interval | MQTT PINGREQ every 15-60 s, catches drops | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| GATT | BLE attribute profile | Services/characteristics/descriptors, read/write/notify ops | [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| MTU | BLE packet size | 23 bytes by default, up to 517 after exchange | [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| Bonding | BLE bonding | Storing encryption keys, passkey JustWorks | [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| RainMaker | Espressif cloud | Provisioning + MQTT + OTA + voice assistants out of the box | [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) |
| BluFi | Setup over BLE | Espressif protocol: SSID/password over a BLE protocomm channel | [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) |
| Matter | Smart-home standard | IP protocol over Thread/WiFi, commissioning over BLE | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Thread | 802.15.4 mesh | IPv6 grid for H2/C6, border router on WiFi | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| mDNS | Local names | `esp32.local` in one subnet, _http._tcp services | [mDNS/NTP/TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) |
| SNTP | Time sync | UDP 123, UTC + TZ Europe/Kyiv, mandatory before TLS | [mDNS/NTP/TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) |
| SSE | Server events | One-way text stream at `/events` for browser telemetry | [HTTP](../../../ESP32-Reference/15-Protokoli/02-HTTP-WebSocket.md) |
| Backoff | Exponential pause | Reconnects at 1/2/4/8 s against reconnect storms | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Broker | Message server | Mosquitto: takes PUBLISH, fans out SUB by topic | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Gateway | Protocol gateway | LoRa to MQTT, Modbus to WiFi, BLE to cloud bridge | [Cloud](../../../ESP32-Reference/15-Protokoli/05-Cloud-Pipeline.md) |

## Memory and firmware

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| Flash | Program flash memory | 4-16 MB external SPI-Flash | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| PSRAM | External RAM | 2-8 MB (WROVER), for cameras/displays | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| SRAM | Internal RAM | 320-512 KB depending on chip | [Chips](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| NVS | Non-volatile storage | Key-value in Flash (Wi-Fi, calibration) | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Partitions | Partition table | NVS/OTA/app/SPIFFS/LittleFS | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Bootloader | Bootloader | 2nd-stage, app choice, download mode | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| esptool | Flashing utility | `esptool.py --chip esp32 write_flash` | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Download mode | Flashing mode | GPIO0=LOW + reset, 921600/460800 baud | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| LittleFS / SPIFFS | Filesystems | LittleFS is modern, SPIFFS is legacy | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Core dump | Crash snapshot | For panic analysis via ESP-IDF | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| OTA-rollback | Firmware rollback | Return to the previous OTA slot if the new one never marks valid | [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md) |
| Octal PSRAM | Fast external RAM | 8-bit OPI bus at 120 MHz for LVGL/cameras on S3 | [Flash/PSRAM](../../../ESP32-Reference/01-Hardware/06-Flash-PSRAM.md) |

## Toolchains and tools

| Term | Translation | Explanation | Link |
| --- | --- | --- | --- |
| ESP-IDF | Official Espressif framework | C/C++, FreeRTOS, full control | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Arduino-core | Arduino core for ESP32 | `setup()/loop()`, fast start | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| MicroPython | Python for microcontrollers | REPL, fast prototypes, slower | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| PlatformIO | Build system | VS Code, handy libraries, CI | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| FreeRTOS | Real-time OS | Tasks, queues, semaphores; dual-core | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| OpenOCD | Debugger | GDB + JTAG | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Dataview | Obsidian plugin | SQL-like queries over notes | [Start](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md) |
| MOC | Content map | [Home map](../../../ESP32-Reference/Home.md) - the central MOC | [Home map](../../../ESP32-Reference/Home.md) |
| WROOM / WROVER | Espressif modules | WROOM without PSRAM, WROVER with PSRAM | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| DevKit | Dev board | Module + USB-UART + LDO + buttons | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| HMI | Human-machine interface | Nextion/DWIN displays, buttons, encoders for control | [Audio/HMI](../../../ESP32-Reference/11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.md) |
| InfluxDB | Time-series database | Stores MQTT telemetry for Grafana charts | [Cloud](../../../ESP32-Reference/15-Protokoli/05-Cloud-Pipeline.md) |
| Pull-up/down | Pull resistors | Internal about 45k are weak; I2C needs external 4.7k | [Template](../../../ESP32-Reference/_templates/Component-Template.md) |
| Watchdog (WDT) | Watchdog timer | Reset on hang; feed it in `loop()` | [Environments](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Brownout | Power dip | Reset at VDD below 2.43V; 470 µF capacitor | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| Dropout (LDO) | Regulator dropout | Vin minus Vout headroom for regulation: AMS1117 about 1.1V, ME6211 about 0.3V | [Protection](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect.md) |
| MPPT | Solar peak-power tracking | CN3791 holds the panel at the Pmax point, CC/CV charge | [Buck/Solar](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md) |
| BMS | Battery protection board | DW01+FS8205: cut-off on overcharge/overdischarge/current | [Charging/BMS](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/03-TP4056-IP5306-BMS-UPS.md) |
| PTC | Self-healing fuse | Polymer type: resistance grows on current overheat | [Protection](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect.md) |
| TVS | Surge suppressor | SMBJ5.0A quenches ESD/spikes in nanoseconds | [Protection](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect.md) |

> [!example] Photo/schematic: ![](../../../ESP32-Reference/assets/img/placeholder.png)
> Reference level schematic for the glossary:

| ESP32 | 3.3V module | 5V module |
| --- | --- | --- |
| 3V3 | VCC | - (no signals!) |
| GND | GND | GND (common) |
| GPIO (3.3V) | SDA/SCL/TX/RX directly | Only via level-shifter |
| 5V (VIN) | - | 5V power VCC |
| EN/BOOT | - | Buttons for flashing |

## See also

- [Home map](../../../ESP32-Reference/Home.md)
- [How to use it](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md)
- [Chip comparison](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md)
- [DevKit boards](../../../ESP32-Reference/00-Start/04-Devkit-plati.md)
- [Environment choice](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md)
- [Component template](../../../ESP32-Reference/_templates/Component-Template.md)
