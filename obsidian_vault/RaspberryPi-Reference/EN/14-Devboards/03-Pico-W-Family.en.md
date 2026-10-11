---
title: Pico Family - Pico, Pico W, Pico 2 and Pico 2 W on the Desk
description: Takes apart Raspberry Pi microcontroller boards - Pico versions, W-model radio, UF2 firmware and board choice; shows schematics, code and tables.
tags: [raspberrypi, pico, pico-w, pico-2, rp2040, rp2350, devboard, uf2]
category: Devboards
lang: en
original: 14-Devboards/03-Pico-W-Family.md
date-created: 2026-10-06
date: 2026-10-10
---

# Pico Family - Pico, Pico W, Pico 2 and Pico 2 W on the Desk

![[assets/img/rpi-pico-family-scheme.png|600]]
*Fig. Pico line: a bare board for soldering, W versions with an antenna, firmware by dragging UF2.*

> [!tip] What this note is
> All four boards side by side: how they differ, what the radio can do, how to flash and debug. Chips: [[EN/01-Hardware/03-RP2040-RP2350.en|RP2040 and RP2350]], environment: [[EN/00-Start/05-Environment-Choice.en|environment choice]].

## 1. Goal

Pick and start a Pico in one evening:

- a table of four models without confusion;
- W versions: what CYW43439 can do and what it cannot;
- UF2 firmware, Thonny, Picoprobe-SWD;
- castellated edge: soldering and carrier boards.

| Board | Chip | Flash | Radio | USB |
| --- | --- | --- | --- | --- |
| Pico | RP2040 | 2 MB | none | micro-USB device |
| Pico W | RP2040 | 2 MB | WiFi + BT (CYW43439) | micro-USB |
| Pico 2 | RP2350 | 4 MB | none | micro-USB device + host |
| Pico 2 W | RP2350 | 4 MB | WiFi + BT | micro-USB |

## 2. Board architecture

```mermaid
flowchart TB
  USB[micro-USB] --> PICO[Pico: RP2040/50]
  PICO --> GPIO[26 GPIO + 3 ADC]
  PICO --> DBG[3-pin SWD connector]
  PICO --> ANT[Antenna (W only)]
  PICO --> LED[LED + WL-LED (W)]
  BOOT[BOOTSEL] --> PICO
```

BOOTSEL button: hold at power-up - the board becomes a flash drive, drag UF2 over. The WL-LED on W versions hangs on the WiFi chip, controlled separately!

## 3. W versions in detail

- CYW43439: WiFi 4 + BT 5.2 (classic + BLE) - BT only through C SDK/BTstack, none in MicroPython;
- MicroPython: `network.WLAN`, examples everywhere;
- C SDK: `pico_cyw43_arch` (threadsafe or poll);
- built-in LED - through `cyw43_arch_gpio_put`, not GPIO25!;
- BT stack in the C SDK (BTstack), limited in MicroPython;
- WiFi TX current up to 300 mA - USB is enough, count the battery.

## 4. Firmware three ways

- UF2 by dragging: BOOTSEL + file into the disk window;
- Thonny: the Run button sends the script, Stop halts it;
- `picotool load/verify/reboot` from the console - for CI;
- Picoprobe (a second Pico): SWD debugging and console;
- bulk: one UF2 for all boards of the batch.

## 5. Working code (MicroPython)

```python
import network
import time
from machine import Pin, ADC
import umqtt.simple as mqtt

led = Pin("LED", Pin.OUT)
adc = ADC(26)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("ssid", "pass")
while not wlan.isconnected():
    time.sleep(0.5)

cl = mqtt.MQTTClient("pico-node", "broker.local")
cl.connect()

while True:
    volt = adc.read_u16() * 3.3 / 65535
    cl.publish(b"pico/adc", str(volt).encode())
    led.toggle()
    time.sleep(10)
```

The `"LED"` string instead of a number works on all Picos, including W (through the CYW43 driver). ADC26 is the first external channel.

## 6. Pico node power

- VSYS 1.8-5.5V: Li-ion battery directly without a converter;
- ADC3 measures VSYS/4 - battery monitoring out of the box;
- sleep: `machine.deepsleep()` - microamperes, wake on GPIO/RTC;
- solar panel + TP4056 - a field-node classic;
- USB 5V for development, battery for the field.

## 7. Carrier boards and cases

- the castellated edge solders onto a carrier board as a module;
- ready carriers: relays, displays, motors (Pimoroni, Waveshare);
- breadboard: the Pico fits a 40-pin DIP row;
- print cases or take acrylic sandwiches.

## 7.1 PIO examples out of the box

- WS2812 strip: the `pio/ws2812` example lights without CPU;
- software UART-TX: any pin becomes a port;
- I2S output: the SDK example drives sound into a DAC;
- DVI terminal: PicoDVI shows a console on a monitor;
- logic analyzer: PIO writes the capture to RAM;
- each example is a file pair: `.pio` + `.c`, built together.

## 8. Common issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| Not seen as a disk | BOOTSEL not held | hold the button at USB plug-in |
| LED does not blink on W | pin 25 instead of "LED" | `Pin("LED")` - goes through CYW43 |
| WiFi does not connect | 5 GHz network | 2.4 GHz only |
| Thonny does not see the board | old MicroPython | fresh UF2 for your model |
| ADC drifts | reference from USB | calibration or LDO |
| C SDK does not build | no toolchain | `arm-none-eabi-gcc` per guide |

## 9. Related notes

- [[EN/01-Hardware/03-RP2040-RP2350.en|RP2040 and RP2350]] - chips in detail.
- [[EN/00-Start/05-Environment-Choice.en|environment choice]] - MicroPython versus C SDK.
- [[EN/06-Analog/01-External-ADC.en|external ADCs]] - when built-in is not enough.
- [[EN/15-Protocols/01-MQTT.en|MQTT protocol]] - node telemetry.
- [[EN/02-Power-Supply/03-UPS-18650.en|UPS boards]] - battery power.

## 9.1 Pico quick cheat sheet

- BOOTSEL at power-up equals a UF2 disk;
- W versions: `Pin("LED")`, 2.4 GHz only;
- VSYS 1.8-5.5V, ADC3 measures the battery;
- Picoprobe equals SWD for 4 dollars;
- Thonny to start, C SDK for speed.

## 9.2 A spare Pico in the bag

- flashed blink-UF2 - power and USB check in a minute;
- jumpers and a data USB cable (not charge-only!);
- a pinout card - do not guess ADC numbers;
- a second Pico as Picoprobe - SWD and console;
- a clean MicroPython UF2 of the latest version.

## Official sources

- [RP2040 Datasheet (Raspberry Pi)](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf) - PIO, ADC, USB.
- [RP2350 Datasheet (Raspberry Pi)](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf) - M33, host, security.
- [Getting Started (Raspberry Pi docs)](https://www.raspberrypi.com/documentation/computers/getting-started.html) - UF2 and Thonny.
