---
title: 5V-3.3V level shifting (Level Shifters)
description: 5V to 3.3V level shifting - dividers, TXS0108 and TXB0104, BSS138, pull-ups on both I2C sides; shows schematics, code and tables.
tags: [esp32, level-shifter, txs0108, optocoupler, esd, i2c]
category: Power
lang: en
original: 13-Power-Modules/02-Level-Shifters.md
date-created: 2026-09-27
date: 2026-10-09
---

# Level shifting: 5V to 3.3V (Level Shifters)

> [!danger] ESP32 GPIOs are NOT 5V-tolerant! Long-term 5V on an input degrades the chip. Exception: open-drain with a pull-up to 3.3V. Every 5V sensor goes through shifting.

Related: power [[EN/02-Power-Supply/01-Power-Rails.en|Power supply]], buck [[EN/13-Power-Modules/01-Buck-Boost-Solar.en]], I2C [[EN/04-Interfaces/03-I2C.en|I2C]], UART [[EN/04-Interfaces/01-UART.en|UART]], SPI [[EN/04-Interfaces/02-SPI.en|SPI]], start [[EN/Home.en]], diagnostics [[EN/99-Additions/02-Troubleshooting-FAQ.en]].

## Purpose

5V to 3.3V level shifting - dividers; TXS0108/TXB0104; BSS138; pull-ups on both I2C sides. ESP32 GPIOs are NOT 5V-tolerant! Long-term 5V on an input degrades the chip. Exception: open-drain with a pull-up to 3.3V. Every 5V sensor goes through shifting. Related: power [[EN/02-Power-Supply/01-Power-Rails.en|Power supply]], buck [[EN/13-Power-Modules/01-Buck-Boost-Solar.en]], I2C [[EN/04-Interfaces/03-I2C.en|I2C]], UART [[EN/04-Interfaces/01-UART.en|UART]], SPI [[EN/04-Interfaces/02-SPI.en|SPI]], start [[EN/Home.en]], diagnostics [[EN/99-Additions/02-Troubleshooting-FAQ.en]].

## Comparison table: what to pick when

| Method | Speed | Direction | Use when | Avoid when |
| --- | --- | --- | --- | --- |
| Divider 1k/2k (or 2k/3.3k) | up to ~1 MHz | one way 5V->3.3V | UART RX, simple digital inputs, cheap and cheerful | I2C (open bus!), fast SPI, 3.3V->5V |
| TXS0108E / TXB0108 | TXS ~110 MHz, TXB ~100 MHz | bidirectional auto | I2C + SPI + UART, universal 8-channel module | long lines, large capacitance, I2C with strong pull-ups |
| MOSFET BSS138 (single channel) | ~1-2 MHz | bidirectional | I2C level-shift classic, 4-channel modules | 8+ signals, high-speed SPI |
| PC817 optocoupler | ~4-20 kHz (no speed-up) | one way + galvanic | isolation for 220V/industrial 24V inputs, RS485 isolation | fast I2C/SPI/UART, bidirectionality |
| Diode + pull-up | ~100 kHz | 5V->3.3V | open-drain buses, WS2812 control | push-pull outputs |
| 74LVC245 / 74AHCT125 | ~50-100 MHz | one way (switchable) | SPI, parallel buses, 5V peripherals | I2C without extra tricks |

## Details

### 1. Voltage divider

5V -> 1k (top) + 2k (bottom) = 3.33V. For UART: 1k in series + a 3.3V Zener as an alternative. Drawback: slows edges (RC with input capacitance), draws current all the time. Do NOT put it on ESP32 outputs toward 5V inputs - that side needs a boost (see below).

| ESP32 | Divider | 5V device |
| --- | --- | --- |
| GPIO16 RX | 1k/2k node | TX 5V |
| GPIO17 TX | direct or through 74AHCT125 | RX 5V (if the 5V input tolerates 3.3V HIGH - often works direct) |

### 2. TXS0108E vs TXB0108

- TXB: for push-pull (SPI, UART). Dislikes pull-ups and open collector.
- TXS: for open-drain + push-pull (I2C + UART + slow SPI). Has internal 10k pull-ups.
- Both: pull OE to VCCA (3.3V) through 10k, VCCA=3.3V, VCCB=5V, common ground. 100 nF capacitors near both supplies. Keep traces as short as possible.

| ESP32 | TXS0108E | 5V side |
| --- | --- | --- |
| 3V3 | VCCA | - |
| GND | GND | GND |
| GPIO21 SDA | A1 | B1 -> SDA 5V |
| GPIO22 SCL | A2 | B2 -> SCL 5V |
| 3V3 through 10k | OE | - |

### 3. I2C level-shift specifics

- I2C is open-drain, it needs a bidirectional shift (MOSFET BSS138 or TXS0108E). Dividers are FORBIDDEN.
- Pull-ups on one side only, or weak ones on both: total equivalent of 2-4.7k to each side's own voltage. Pull-ups that are too strong (1k on both) - the bus never reaches LOW.
- Bus capacitance below 400 pF (up to ~50 cm of wire at 100 kHz). Longer runs - drop the rate to 50 kHz or use an I2C extender P82B715.
- See [[EN/04-Interfaces/03-I2C.en|I2C]].

### 4. PC817 opto-isolation (when galvanics are needed)

```text
24V датчик -> 2.2к -> LED PC817 (анод), катод -> GND24
Фототранзистор: колектор -> 3.3V через 10к (або GPIO з pull-up), емітер -> GND ESP32
GPIO читає інверсію: LED горить = GPIO LOW. Для швидкості додати 1к + прискорюючий конденсатор 100пФ паралельно вхідному резистору.
```

Fast option: 6N137 / PC900 (10 Mbit) for isolated UART/SPI.

### 5. ESD and TVS protection

- Human hands + long wires = ESD. On every outdoor line (buttons, outdoor I2C, RS485): TVS diodes PESD3V3 / PRTR5V0U2X + 47-100 Ohm series resistor + 100 pF capacitor to ground.
- RS485/CAN: TVS SM712 (special for RS485) between A-B-GND. Ethernet: built-in transformers + TVS.
- Power: TVS SMBJ5.0A on the 5V input + a 1-2A self-recovery fuse.

| Symptom | Cause | Fix |
| --- | --- | --- |
| I2C NACK through shift | TXB instead of TXS / strong pull-ups | TXS0108E or BSS138, check pull-ups |
| 5V on GPIO, ESP32 heats up | direct 5V input | divider/shift, check whether it is broken |
| Optocoupler misses pulses | slow PC817 at 115200 | 6N137 or direct shift with no isolation |

## Wiring

| ESP32 | TXS0108E | 5V side |
| --- | --- | --- |
| 3V3 | VCCA | - |
| GND | GND | GND (common!) |
| GPIO21 SDA | A1 | B1 → SDA 5V |
| GPIO22 SCL | A2 | B2 → SCL 5V |
| 3V3 through 10k | OE | - |

### ASCII schematic

```text
ESP32 (3.3 В)           TXS0108E (8 каналів)          5 В сенсор/шина
-------------           ------------------          ----------------
3V3 ──────────────────► VCCA (= 3.3 В)
5V ────────────────────────────────────────────────► VCCB (= 5 В)
GND ──────────────────► GND ◄────────────────────── GND (спільна!)
GPIO21 SDA ───────────► A1 ──► B1 ─────────────────► SDA 5V
GPIO22 SCL ───────────► A2 ──► B2 ─────────────────► SCL 5V
3V3 ──[10 кОм]────────► OE (HIGH = робота)
VCCA ◄──[100 нФ]──► GND; VCCB ◄──[100 нФ]──► GND (біля мікросхеми)
I2C — тільки TXS (не TXB!); дільник на I2C ЗАБОРОНЕНО
```

### Mermaid

```mermaid
graph LR
  ESP32["ESP32<br/>3V3 / SDA / SCL"] -->|A1/A2| TXS["TXS0108E<br/>VCCA=3.3V VCCB=5V"]
  TXS -->|B1/B2| DEV["5V I2C device<br/>SDA / SCL"]
  ESP32 -->|GND| TXS
  TXS -->|GND| DEV
```

![[assets/img/txs0108-i2c.png|500]]
*Fig. TXS0108E - bidirectional I2C shift, OE to VCCA, 100 nF capacitors. Photo placeholder - see [[assets/README]].*

### NT0104 / SN74LVC2T45 - when TXS is not enough

| Option | What it is | Nuance |
| --- | --- | --- |
| NT0104 (Nexperia) | 4-bit translator with per-pin DIR direction | Predictable direction (unlike auto-TXS) - for UART RTS/CTS and SPI CS |
| SN74LVC2T45 | 2-bit, up to 420 Mbit/s | Fast buses where TXS chokes on edges |

```text
ESP32 GPIO ──► A-сторона ──[DIR=HIGH]──► B-сторона 5V-пристрій (і назад при DIR=LOW)
VCCA=3.3V, VCCB=5V, OE до VCCA через 10к (не залишати висячим!)
```

> Selection guideline: I2C/open-drain → TXS0108; UART/SPI with known direction → NT0104/SN74LVC2T45; single line → BSS138/resistor divider.

## Official sources

- [TXS0108E - datasheet (TI)](https://www.ti.com/product/TXS0108E) - auto-direction, do's and don'ts for I2C/SPI.
- [TXB0108 - datasheet (TI)](https://www.ti.com/product/TXB0108) - push-pull variant, differences from TXS.
- [ESP32 Pinout (RNT)](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) - which pins are strictly 3.3V, strapping.
- BSS138 / PC817 / 74LVC245 / 74AHCT125 - *verify by hand* against the marking.

### Single line on BSS138 (when TXS0108 is overkill)

```text
3.3V ──[10к]──┬── 3.3V-сторона (ESP32)
              │
            [BSS138: Gate→3.3V, Source→3.3V-сторона, Drain→5V-сторона]
              │
5V ───[10к]───┴── 5V-сторона (сенсор)
Двобічно для open-drain (I2C!) і повільних ліній; для SPI>10 МГц — TXB0104.
```

### TXS vs TXB vs divider - quick table

| Option | Speed | Direction | Use when |
| --- | --- | --- | --- |
| Divider 1k/2k | up to ~1 MHz | Down (5 to 3.3) | UART-TX, slow signals |
| BSS138 channel | up to ~2 MHz | Both ways (open-drain) | I2C, 1-Wire |
| TXS0108 | up to 24 MHz push-pull | Auto | SPI, fast buses |
| TXB0104 | up to 100 MHz | Auto (no pulls!) | With no pull-ups on lines |

## See also

- [[EN/Home.en]]
- [[EN/04-Interfaces/03-I2C.en|I2C]]
- [[EN/04-Interfaces/01-UART.en|UART]]
- [[EN/04-Interfaces/02-SPI.en|SPI]]
- [[EN/02-Power-Supply/01-Power-Rails.en|Power supply]]
- [[EN/13-Power-Modules/01-Buck-Boost-Solar.en]]
- [[EN/99-Additions/02-Troubleshooting-FAQ.en]]

![[assets/img/level-shifters-scheme.png|500]]
*Fig. Level shifting: divider, TXS0108/BSS138, fast NT0104, pull-ups on both I2C sides.*
