---
title: STM32 DevKit boards - Blue Pill, Black Pill, Nucleo, Discovery
description: Compares Blue Pill, Black Pill, Nucleo and Discovery boards and teaches the first launch; shows schematics, code and tables.
tags: [stm32, start, devkit, bluepill, blackpill, nucleo, discovery, stlink]
category: Start
lang: en
original: 00-Start/04-Devkit-plati.md
date-created: 2026-10-01
date: 2026-10-08
---

# DevKit boards - Blue Pill, Black Pill, Nucleo, Discovery

![[assets/img/stm32-devkit-boards-scheme.png|600]]
*Fig. From the $2 Blue Pill (with nothing) to Nucleo (ST-Link + Morpho on board).*

> [!tip] Purpose of this note
> Pick a board for the stage: learning, prototype, production unit. Plus clone traps.

## 1. Purpose

A board is a chip + power supply + programmer + handy pins. Blue Pill is cheap but has no ST-Link and a regulator lottery. Nucleo costs more but carries a built-in ST-Link and a Morpho connector for shields. Mixing them up costs days.

## Board specs

| Board | Typical chip | Programmer | Power supply | When to take |
| --- | --- | --- | --- | --- |
| Blue Pill | F103C8 (often remarked!) | None (external ST-Link!) | USB 5V → weak LDO | Learning for $2; verify chip authenticity! |
| Black Pill | F401/F411 | None / USB-CDC (depends) | USB-C, better LDO | Compact nodes, USB serial |
| Nucleo-64/144 | Depends on board | Built-in ST-Link! | ST-Link USB / VIN / 5V | Development: debug out of the box |
| Discovery | F4/H7 + display/sensors | Built-in ST-Link | USB | Peripheral demo (audio, LCD, MEMS) |
| WeAct MiniF4 | F401 | USB-CDC | USB-C | Modern minimalism |

```text
Швидкий вибір:
  Перша плата в житті .......... Nucleo (дебаг з коробки рятує тижні)
  Дешевий вузол у корпус ........ Black Pill / WeAct
  Вчитися на помилках за $2 ..... Blue Pill (+ зовнішній ST-Link!)
```

## Mermaid: original vs clone

```mermaid
flowchart TB
    BUY[Buying a Blue Pill] --> MARK{Chip marking?}
    MARK -->|Laser, sharp| T1[Likely original: CubeMX test + flash size]
    MARK -->|Printed/crooked| CLONE[Clone (CS32/GD32): check peripherals one by one!]
    CLONE --> USBS{Does USB work?}
    USB -->|No| EXT[External ST-Link mandatory]
```

## Common issues

| # | Issue | Cause | Fix |
| --- | --- | --- | --- |
| 1 | Clone with remarking | Different flash size, USB glitches | `st-info --probe` + peripheral test |
| 2 | 5V supply on a 3.3V pin | Chip death | 3.3V on GPIO only (5V-tolerant ones are the exception, not the rule!) |
| 3 | Flashing Blue Pill over USB | There is no USB-UART there! | ST-Link (SWDIO/SWCLK) or UART bootloader |
| 4 | BOOT0 not returned to 0 | Board always in bootloader | Jumper back after flashing over UART |

## Official sources

- [Nucleo Boards (ST)](https://www.st.com/en/evaluation-tools/stm32-nucleo-boards.html) - lineup and docs.
- [STM32CubeProgrammer (ST)](https://www.st.com/en/development-tools/stm32cubeprog.html) - flashing/erasing/OB.

## First launch step by step (any board)

1. **Inspect the board**: supply jumpers (JP5 on Nucleo!), BOOT0 at 0, a USB cable with data.
2. **Plug in and listen**: a new COM port / ST-Link in Device Manager = alive.
3. **Read the chip**: STM32CubeProgrammer → Connect → chip ID + flash size. No connect - check BOOT0, NRST, power supply.
4. **Load Blink**: GPIO_Toggle example, Start Debugging button (green bug!). LED blinks = toolchain is whole.
5. **Then**: move the LED pin to yours, add a button with interrupt, enable UART logging.

## Power supply in detail

| Source | Where it goes | Limit |
| --- | --- | --- |
| USB ST-Link (Nucleo) | 5V board rail → LDO → 3.3V | Current from PC USB port (~500 mA) |
| USB device (Blue Pill) | 5V → LDO RT9193 | Weak LDO: WiFi modules/motors - separately! |
| VIN / 5V pin | Straight to the 5V rail | Do not exceed 5.5V, Schottky diode against reversal |
| 3.3V pin | Straight into the domain (bypassing LDO!) | Stable 3.3V only, otherwise - death |
| Battery + LDO | Via VIN | Count dropout: 3.0V Li-Ion will not pull a 3.3V LDO! |

## Boards in detail: what sits where

### Blue Pill (F103C8)

| Element | Where | Note |
| --- | --- | --- |
| USB | Micro-USB, power only (no data!) | Flashing - ST-Link or UART1 |
| Buttons | RESET + BOOT0 jumper | BOOT0: 0 = run, 1 = bootload |
| LED | PC13 (active low!) | First Blink goes right here |
| LDO | Weak, heats up | External modules get separate power |

### Nucleo-64 (F401RE example)

| Element | Where | Note |
| --- | --- | --- |
| ST-Link | Top part, USB Mini-B | Flashing + debug + VCP log |
| Supply jumpers | JP5 (U5V/E5V/VIN) | Wrong one - board stays silent |
| Buttons | RESET (black) + USER (blue, PC13) | USER - first interrupt |
| Arduino connector | Morpho + Arduino Uno V3 | Shields fit at once |
| JP6 (IDD) | Current measurement | Ammeter instead of jumper - measure sleep! |

### Discovery (F407 example)

| Element | Where | Note |
| --- | --- | --- |
| Display/audio/sensors | On board | ST demo firmware as a start |
| ST-Link | Built-in | Like Nucleo |
| Power supply | USB + external 5V | Display eats - a USB hub may not be enough |

## Clones in detail: what to check

| Check | How | Expected |
| --- | --- | --- |
| Chip ID | `st-info --probe` | Matches the marking |
| Flash size | CubeProgrammer → read | As in datasheet |
| USB/UART | Echo test at 115200 and 921600 | No garbage at high speed |
| ADC | Short input to GND/3V3 | 0 and 4095 without hundred-code noise |
| Reset button | Press during run | Clean restart, no lockup |

> A clone with honest parameters for $1 is a working learning option. A clone with a remarked smaller Flash goes back to the seller.

## Board upgrade as the project grows

| Was | Became | What changes |
| --- | --- | --- |
| Blue Pill | Black Pill / WeAct | USB-CDC, more Flash, same code |
| Black Pill | Nucleo-64 | ST-Link and pin margin appear |
| Nucleo-64 | Nucleo-144 / Discovery | Ethernet, displays, more memory |
| Any DevKit | Own board | Only what is needed: chip + crystal + LDO + SWD connector |

> Pins and HAL code carry over almost 1-to-1 inside one family. Swap the board, do not rewrite the project.

## Where to buy and what to watch

| Channel | Plus | Minus |
| --- | --- | --- |
| Official distributors | Original guarantee, full docs | Price and lead times |
| Marketplaces | Cheap, fast | Clone lottery - check against the table above |
| Fleamarkets/used | Sometimes rarities | No guarantees at all |

> For learning, one Nucleo + one Blue Pill is enough. An "everything in a row" kit collects dust.

## How to tell a clone

- Price below $2 is almost surely a clone with smaller Flash; verify with a programmer.
- Blurry silkscreen, wobbly USB connector are signs of cheap assembly.
- A clone works, but errata and documentation are luck of the draw.

## See also

- [[Home.en]]
- [[00-Start/03-Porivnyannya-chipiv| Chip comparison]]
- [[00-Start/05-Vibir-seredovischa| Environment choice]]
