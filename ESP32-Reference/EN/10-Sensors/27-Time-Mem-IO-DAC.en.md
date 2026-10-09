---
description: Time, memory, IO, DAC: DS3231 RTC, EEPROM/FRAM, GPIO expander MCP23017, DAC MCP4725. Applications: timekeeping, storage, analog output.
title: Time Mem IO DAC
tags: [esp32, sensor, ds3231, eeprom, mcp23017, dac, mcp4725]
category: Sensori
lang: en
original: 10-Sensors/27-Time-Mem-IO-DAC.md
date-created: 2026-09-27
date: 2026-10-08
---

# Time Mem IO DAC

## Purpose

Supporting modules: DS3231 RTC (I2C 0x68), EEPROM/FRAM (I2C), GPIO expander MCP23017 (I2C 0x20/0x21), DAC MCP4725 (I2C 0x60). Applications: clock, storage, extra IO, analog output.

## Characteristics

| Module | Interface | Features |
| --- | --- | --- |
| DS3231 | I2C 0x68 | ±2 ppm, alarm |
| EEPROM | I2C 0x50 | 1-32 KB |
| MCP23017 | I2C 0x20 | 16 GPIO |
| MCP4725 | I2C 0x60 | 12-bit DAC |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | DS3231 no battery | Time lost | CR2032 backup |
| 2 | MCP23017 wrong address | Not found | Check address jumpers |

## See also

- [[EN/04-Interfaces/03-I2C.en|I2C]]
- [[EN/10-Sensors/14-DS3231-Encoder-Keypad-Joystick.en]]
