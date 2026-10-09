---
description: Input IO 2: GPIO expander MCP23017/MCP23008, shift register 74HC165, button matrix, potentiometer ADC, touch TTP223. Applications: extra IO, input devices.
tags: [esp32, sensor, io, mcp23017, button, potentiometer, touch]
category: Sensori
lang: en
original: 10-Sensors/33-Input-IO-2.md
date-created: 2026-09-27
date: 2026-10-08
---

# Input IO 2

## Purpose

Input expansion and control: MCP23017 (16 GPIO I2C), 74HC165 shift register, button matrix, potentiometer ADC, touch TTP223 (capacitive). Applications: extra IO, interfaces.

## Characteristics

| Module | Interface | Features |
| --- | --- | --- |
| MCP23017 | I2C 0x20/21 | 16 GPIO, interrupt |
| 74HC165 | SPI / parallel | 8-bit shift |
| TTP223 | Digital touch | Capacitive |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | MCP23017 wrong address | Not found | Check jumpers |

## See also

- [[EN/04-Interfaces/03-I2C.en|I2C]]
- [[EN/04-Interfaces/02-SPI.en|SPI]]
