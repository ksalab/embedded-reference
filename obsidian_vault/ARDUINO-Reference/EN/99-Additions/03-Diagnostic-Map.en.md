---
title: Arduino Diagnostic Card - Symptom, Tool, Signal
description: Explains the Arduino troubleshooting route from symptom through instrument to signal with log and tool index.; shows schematics, code and tables.
tags: [arduino, diagnostics, instruments, map]
category: Dodatki
lang: en
original: ARDUINO-Reference/99-Additions/03-Diagnostic-Map.md
date-created: 2026-10-05
date: 2026-10-08
---

# Arduino Diagnostic Map - Symptom, Tool, Signal
![[assets/img/arduino-diagmap-scheme.png|600]]
*Rice. From a symptom to a signal: what device to use and what to look for.*

> [!tip] Note assignment
> Give a table-route: symptom - device - signal. An addition to the FAQ, not a duplicate.

## 1. How to use the card Find the symptom, take the device, check the signal. There is no signal - the reason has been found. Analysis of the reasons - in [[99-Additions/01-Troubleshooting-FAQ | answers to questions]], here only the route of measurements.
## 2. Filling and port

| Symptom | Device | Signal |
| --- | --- | --- |
| There is no port Manager + other cable | COM appears when connecting |
| The filling breaks Verbose-log IDE | At what percentage is the cliff |
| Port busy | Close all | The monitor and the plotter are closed |
| The clone is silent | Bridge driver | CH340/CP2102 visible in system |

## 3. Start and stability

| Symptom | Device | Signal |
| --- | --- | --- |
| Does not start | Blink test | LED blinks or not |
| Rebut | Monitor + finger on LDO | Reason and heating
| Will hang by chance | Free RAM in the vine | Remaining SRAM in bytes |
| Warming | Current multimeter | Who eats more than the norm |

## 4. Tires and sensors

| Symptom | Device | Signal |
| --- | --- | --- |
| I2C is silent | Sketch scanner | Address on line |
| SPI garbage | Speed ​​reduction | Purely at a minimum or not |
| UART kriokazabry | Monitor baud rate | Coincidence with the sketch |
| ADC floats | Resistance multimeter | 5V or 1.1V stable |

## 5. Food

| Symptom | Device | Signal |
| --- | --- | --- |
| Draft | Multimeter under load | 5B holds or not |
| Hot LDO | Current and voltage VIN | Scattering power |
| The battery is worse Bank voltage | Internal resistance |

## Mermaid: diagnostic route```mermaid
flowchart TB
S[Symptom] --> T{What class?}T -->|Not sewn| PORT[Cable, driver, BOOT]T -->|Does not start| BLINK[Naked Blink]T -->|Bugs| MON[Monitor and RAM]T -->|Tyres| SCAN[Scanner and speed]T -->|Food| MM[Multimeter under load]PORT --> SIG [There is a signal - continue]    BLINK --> SIG
    MON --> SIG
    SCAN --> SIG
    MM --> SIG
SIG --> LOC[Localized to one node]```
## 6. Index of tools

| I have | I can I can't
| --- | --- | --- |
| Only USB | Port, log, fill | Analog and currents
| Plus a multimeter Power, short, current | Timings |
| Plus analyzer | Buses with decoders | Analog noise |
| Plus an oscilloscope PWM, ripples, fronts | Radio |

## 7. Journal: what to write down

| Field | Why |
| --- | --- |
| Board and clone or not | Clones behave differently! |
| Symptom literally | Repeat in a month
| Minimal sketch | A bare example with a bug |
| What has already been checked | Do not walk in circles

## 8. War stories map: three more

#
## K1. The plotter holds the port

| Field | Record |
| --- | --- |
| Symptom | The fill drops, the monitor is closed |
| Dimension | The plotter is open in the adjacent tab! |
| The reason | The same COM is busy |
| Fix | Close everything except IDE when filling |

#
## K2. 12 V on VIN and smoke

| Field | Record |
| --- | --- |
| Symptom | The smell, the board is dead |
| Dimension | The BZ stood at 12 V over the limit from the relay |
| The reason | LDO overheating + relay current |
| Fix | New board, VIN 7-9 V, relay separately |

#
## K3. The scanner found two sensors

| Field | Record |
| --- | --- |
| Symptom | One sensor is responsible for two |
| Dimension | Both at address 0x76 from box |
| The reason | Same addresses, SDO not resoldered |
| Fix | Re-solder the SDO one at 0x77 |

## 9. Quick index: symptom - where

| Symptom | Map section |
| --- | --- |
| There is no port 2. Filling and port |
| Does not start | 3. Start and stability |
| I2C is silent | 4. Tires and sensors |
| Warming | 5. Food |
| Only USB in hands 6. Index of tools |

## Typical errors

| # | Error | Why bad | How correct |
| --- | --- | --- | --- |
| 1 | Measure without the ground of the device | Phantom values ​​| Common ground always! |
| 2 | Search difficult first | Hours past the reason | From simple to complex |
| 3 | Without magazine | The same circles Record every step |
| 4 | One measure is a verdict Coincidence | Three times and the average |
| 5 | Ignore heating | Thermal glitches Finger and current |

## Official sources

- [Arduino Troubleshooting (Arduino)](https://support.arduino.cc/hc/en-us/sections/360003198300-Upload-issues) - fill, ports, drivers.
- [Arduino Language Reference (Arduino)](https://docs.arduino.cc/language-reference/) - functions and behavior.

## See also- [[Home | Home]]
- [[99-Additions/01-Troubleshooting-FAQ | answers to questions]]
- [[99-Additions/02-Cheklisti-Datasheet | lists and datasheets]]
- [[17-Lab/01-Priladi | measuring devices]]
- [[09-Firmware/01-IDE-CLI | environment and CLI]]


## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.
