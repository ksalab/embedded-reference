---
description: DS3231 RTC, rotary encoder, keypad matrix, joystick analog: time keep, rotation input, key matrix, analog direction. Applications: clocks, menus, control.
title: DS3231, Encoder, Keypad, Joystick
tags: [esp32, sensor, ds3231, encoder, keypad, joystick]
category: Sensori
lang: en
original: 10-Sensors/14-DS3231-Encoder-Keypad-Joystick.md
date-created: 2026-09-27
date: 2026-10-08
---

# DS3231, Encoder, Keypad, Joystick

## Purpose

Real-time clock DS3231 (I2C, temperature compensated, battery backup), rotary encoder (quadrature A/B, push), keypad matrix 4×4, analog joystick (X/Y/A + button). Applications: clocks, menu control, input devices.

## Characteristics

| Device | Interface | Features |
| --- | --- | --- |
| DS3231 | I2C 0x68 | ±2 ppm, temperature comp, alarm, 32kHz |
| Encoder | GPIO A/B + push | Quadrature, 360° or limited |
| Keypad 4×4 | GPIO row/col | Matrix scan |
| Joystick | ADC X/Y + button | Analog 0-3.3 V |

## Wiring diagram

| ESP32 | DS3231 / Encoder / Keypad / Joystick | Note |
| --- | --- | --- |
| 3V3 | VCC | 3.3 V |
| GND | GND | Common |
| GPIO21 | SDA / Encoder A / Joystick X | I2C / interrupt |
| GPIO22 | SCL / Encoder B / Joystick Y | I2C / ADC |
| GPIO4 | Encoder push / Keypad row | Pull-up |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | DS3231 without battery | Time lost on power off | CR2032 backup, 3V battery |
| 2 | Encoder bounce | Count jumps | Software debounce 1-2 ms |
| 3 | Keypad ghosting | Wrong key | Diodes in matrix or software scan |

## Official sources

- DS3231 Datasheet (Maxim) - `check manually`.
- Encoder guide - see libraries.

## See also

- [[EN/04-Interfaces/03-I2C.en|I2C]]
- [[EN/10-Sensors/01-DHT11-DHT22.en]]
