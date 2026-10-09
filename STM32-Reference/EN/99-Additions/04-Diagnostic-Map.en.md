---
title: Diagnostic card - symptom, tool, signal
description: Explains the choice of measuring tool for each STM32 board fault symptom.; shows schematics, code and tables.
tags: [stm32, diagnostics, instruments, mapping]
category: Dodatki
lang: en
original: STM32-Reference/99-Additions/04-Diagnostic-Map.md
date-created: 2026-10-02
date: 2026-10-08
---

# Diagnostic map - symptom, tool, signal
![[assets/img/stm32-diag-map-scheme.png|600]]
*Rice. From a symptom to a signal: what device to use and what to look for.*

> [!tip] Note assignment
> Give a table-route: symptom - what device to measure - what signal to look for.

## 1. How to use the card

Find your symptom in the table, take the specified device, check the signal. If there is no signal, the cause has been found. If there is - go further in the chain.

## 2. Power and start

| Symptom | Device | Signal |
| --- | --- | --- |
| The board is dead | Multimeter | 3.3 V on the VDD leg of the chip |
| The stabilizer is heating up Finger and ammeter | Quiescent current: milliamps, not amperes |
| Reset under load | Oscilloscope on VDD | Subsidence below the BOR threshold |
| Does not start with quartz | Oscilloscope on OSC | A sine wave of the correct frequency |
| Floating start | NRST logic | Pure treble without ringing |

## 3. Firmware and debugging

| Symptom | Device | Signal |
| --- | --- | --- |
| ST-Link does not see | CubeProgrammer + Wires | SWDIO and SWCLK go to the | pins
| A break in the middle of the record | Shorter plume | Reduce the frequency of SWD |
| Starts only with the debugger | Scheme BOOT0 | Lifting BOOT0 to the ground |
| HardFault immediately | Debugger, HFSR register | Fault address in the disassembler |

## 4. Digital buses

| Symptom | Device | Signal |
| --- | --- | --- |
| UART emits garbage | Logic analyzer | Baud rate and start bit on line |
| UART is silent | Analyzer on TX | Is there any forwarding at all |
| I2C hangs | Oscilloscope on SCL | Line at zero - the slave holds |
| I2C NACK | Address analyzer | The address on the line matches the datasheet |
| SPI bit shift | Analyzer with decoder | CPOL and CPHA are the same on both sides |
| CAN is silent | Oscilloscope differential | Dominant and recessive levels |

## 5. Analog and time

| Symptom | Device | Signal |
| --- | --- | --- |
| ADC noise | Oscilloscope on VDDA | Pulsations of the digital part |
| Floating dimension | Multimeter on VREF | The support is stable under load
| Awake in Stop | Ammeter in the gap | Which peripherals are not turned off - turn them off one by one |
| Floating RTC | Frequency meter on LSE | 32768 Hz exactly, capacitors according to the datasheet |

## 6. Mermaid: diagnostic route```mermaid
flowchart TB
S[Symptom] --> T{Which device?}T -->|No start| MM[Multimeter: Power and Short]T -->|Not sewn| PRG[Programmer: connect and erase]T -->|Tyres| LA[Analyzer: Protocol Decoder]T -->|Noise and Reset| OSC[Oscilloscope: Power and Signals]MM --> SIG [There is a signal - continue]    PRG --> SIG
    LA --> SIG
    OSC --> SIG
SIG --> LOC[Localized to one node]```
## 7. Minimum laboratory set

| Device | Minimum | Why |
| --- | --- | --- |
| Multimeter | True-RMS | Voltages, currents, ringing |
| BZ with the restriction | 0-30 V, current regulation | Secure First Power On |
| Logic analyzer | 8 channels, 24 MHz | UART, I2C, SPI decoders |
| Oscilloscope | 2 channels, 100 MHz | Power, quartz, signals |
| ST-Link | Original or clone | Firmware and debugging

## 8. Radio and power circuits

| Symptom | Device | Signal |
| --- | --- | --- |
| LoRa is not audible | Checking FUS and stack | Stack and firmware versions are compatible
| Short range | Overview of the antenna | 50 ohms, keepout zone, pi circuit |
| Servo jerks | PWM oscilloscope Period 20 ms, pulse 1-2 ms stable |
| The relay clicks exactly | Oscilloscope on a coil | Discharge without a diode - false positives
| The MOSFET heats | Shutter measurement | The front is steep, the Miller plateau is short

## 9. Diagnostic log: what to write down

| Field | Why |
| --- | --- |
| Symptom literally | To repeat in a month |
| Conditions: power, temperature, cables | The bug lives in the conditions, not in the code
| What has already been checked | Do not walk in circles
| Minimal example | A bare project where the bug is visible |
| Photo of the board and oscillogram | Memory is better than words```text
Шаблон запису:
  плата: ревізія, чип, живлення;
  симптом: that and коли;
  виміри: прилад, точка, значення;
  висновок: вузол-винуватець;
  фікс: that змінено, результат.
```
## 10. When to stop and ask for help

| Sign | Action |
| --- | --- |
| You walk in circles for the third time A break, then a minimal example from scratch |
| Suspicion of missing chip | Re-solder on a consciously working board |
| Suspicion of wiretapping Compare with Nucleo: Does the same code work there? |
| There is no device for signal | Ask for a measurement, not guess |```text
Package for a question on the forum:minimal code repeating the bug;connection diagram of the problem node;oscillogram or log from the device;which has already been checked against this map.Without a package, you will receive the same questions in response.```
## 11. War stories: how it was in the field

#
## Case 1. Silent UART after moving to G0

| Field | Record |
| --- | --- |
| Symptom | Console throws garbage after moving from F1 |
| Dimension | The analyzer showed a baud rate 12 percent higher |
| The reason | The APB bus is different, the BRR is calculated from the old frequency |
| Fix | BRR recalculation from actual tire, MCO check |

#
## Case 2. I2C dies once a day

| Field | Record |
| --- | --- |
| Symptom | The sensor disappears, it is treated with a reset |
| Dimension | Oscilloscope: SCL at zero after thunderstorm near |
| The reason | The slave hung in the middle of the byte, interference from the | contactor
| Fix | TVS on the line + software 9 clocks recovery |

#
## Case 3. The battery died in a month instead of years

| Field | Record |
| --- | --- |
| Symptom | The node is silent after a month |
| Dimension | Ammeter: 2 mA in sleep instead of 2 μA |
| The reason | UART transmitter is not turned off before sleeping |
| Fix | Turn off the periphery clearly, measure sleep in the checklist

#
## Case 4. ADC sees steps

| Field | Record |
| --- | --- |
| Symptom | The value jumps short to the least significant bits |
| Dimension | VDDA pulses synchronously with PWM |
| The reason | Joint decoupling of the digit and analog |
| Fix | Ferrite and individual capacitors on VDDA |

#
## Case 5. The radio hears every other time

| Field | Record |
| --- | --- |
| Symptom | Packets are lost in half the distance |
| Dimension | RSSI is 15 dB worse than the reference board |
| The reason | Copper under the chip antenna in this revision |
| Fix | Keepout in the next revision, temporarily - external antenna |

## 12. War stories 6-10: the second five

#
## Case 6. HardFault from stack overflow

| Field | Record |
| --- | --- |
| Symptom | Drops in random places |
| Dimension | Map file: stack almost next to heap |
| The reason | Recursion in the parser plus deep ISR |
| Fix | More stack in the linker, remove recursion |

#
## Case 7. Brick board after RDP

| Field | Record |
| --- | --- |
| Symptom | ST-Link does not see, erase does not go |
| Dimension | Option bytes: RDP level 2 |
| The reason | Click in CubeProgrammer on the debugging board |
| Fix | Chip in the trash; rule - RDP 2 only in series |

#
## Case 8. Burnt pin from 5 V

| Field | Record |
| --- | --- |
| Symptom | The input always reads one, the chip heats |
| Dimension | The FT column in the datasheet is empty for this pin |
| The reason | 5 V on the non-FT input directly |
| Fix | Chip replacement, divider or MOSFET-bridge |

#
## Case 9. Slow I2C over wires

| Field | Record |
| --- | --- |
| Symptom | NACK on half of the transactions |
| Dimension | The SCL fronts are stretched - loop capacity |
| The reason | 30 cm of mock wires at 400 kHz |
| Fix | Shorter, lower speed, stronger lifts |

#
## Case 10. Sleep eats the battery through the debugger

| Field | Record |
| --- | --- |
| Symptom | In a dream milliamperes instead of microamperes
| Dimension | Without ST-Link - normal, with it - no |
| The reason | The debugger holds power domains |
| Fix | Measure sleep only without connected debugger |

## 13. Index of tools: what I can do with what I have

| I have | I can check | I can't
| --- | --- | --- |
| Only a multimeter | Power supply, short, quiescent current, buttons, dividers | Timings, protocols, pulsations |
| Multimeter + ST-Link | Plus chip ID, registers, memory, HardFault address | Fast signals |
| Plus a logic analyzer | UART, I2C, SPI, PWM periods, protocol timings | Analog noise |
| Plus an oscilloscope Everything above plus pulsations, quartz, fronts, KXH landmarks | Radio spectrum
| All + VNA | Matching antennas, S11, accurate 50 Ohm | Certification measurements of the field |```text
Пріоритет покупок для лабораторії:
  мультиметр -> ST-Link -> аналізатор -> осцилограф -> БЖ з обмеженням.
  Кожен наступний відкриває новий клас багів.
```
## See also- [[Home | Home]]
- [[99-Additions/01-Troubleshooting-FAQ | answers to questions]]
- [[99-Additions/02-Cheklisti | checklists]]
- [[17-Lab/01-Priladi | measuring devices]]
- [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]]


## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.


## Official sources

- STMicroelectronics reference manuals and datasheets
- Official ST-Link documentation
- Arduino / Raspberry Pi official guides
