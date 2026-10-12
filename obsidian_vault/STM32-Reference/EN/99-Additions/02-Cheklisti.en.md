---
title: Checklists - starting the board and entering the series
description: Checklists for the first launch of the board, own board layout, firmware release and battery power for a smooth release into the series; shows schematics, code and tables.
tags: [stm32, checklist, bringup, production]
category: Dodatki
lang: en
original: STM32-Reference/99-Additions/02-Cheklisti.md
date-created: 2026-10-01
date: 2026-10-08
---

# Checklists - starting the board and entering the series
![[assets/img/stm32-checklist-scheme.png|600]]
*Fig. Four checklists: first start, own board, firmware release, battery.*

> [!tip] Note purpose
> Give a paper procedure: from the first supply of power to the box with the series, so that nothing is forgotten in the stress of the deadline.

## 1. Checklist for the first startup of the factory board

Do not apply power randomly. Go line by line and mark only after measurement.

| Number | Action | Readiness sign |
| --- | --- | --- |
| 1 | Inspect the board with a magnifier: solder bridges, cracks, crooked USB | Tracks clean, connectors even |
| 2 | Check the power jumpers and BOOT0 | BOOT0 to ground, 3.3 V or 5 V power per silkscreen |
| 3 | Apply power through a current limit | Current is tens of milliamps, nothing heats up |
| 4 | Measure 3.3 V on the microcontroller pins | 3.2-3.4 V, small ripple |
| 5 | Connect ST-Link with a short cable | Programmer visible in the system |
| 6 | Connect and mass erase | Chip answers, memory clean |
| 7 | Flash Blink with 1 Hz LED | LED blinks evenly |
| 8 | Check clocking via MCO | Frequency matches CubeMX |
| 9 | Check UART with a greeting in the terminal | Clean text at 115200 |
| 10 | Save good settings into notes | Frequencies, board and firmware version recorded |

Connection details are described in the note about firmware via ST-Link, and power in the note about board power rails. See [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]] and [[02-Power-Supply/01-Power-Supply-Rails.en | board power rails]].

## 2. Own board checklist: schematic

| Number | Schematic check | What we ask |
| --- | --- | --- |
| 1 | Power and grounds | Are all VDD and VSS connected, is there 100 nF near each pair |
| 2 | VDDA and VREF | Is there a filter, not floating |
| 3 | NRST reset | Is there a 10 kOhm pull-up and a 100 nF capacitor |
| 4 | BOOT0 | Is there a 10 kOhm ground resistor and a jumper place |
| 5 | Crystals | Is there a load per datasheet, are the lines short |
| 6 | SWD connector | Are SWDIO, SWCLK, NRST, GND, 3.3 V routed |
| 7 | Buttons and LEDs | No conflict with SWD and bootloader |
| 8 | 5 V tolerance | Is the FT column checked for each 5 V input |

Classic packages are recalled by [[EN/01-Hardware/01-F0-F1-Classic.en | classic F0 and F1]], and board choice by [[EN/14-Devboards/03-Nucleo.en|Nucleo boards]].

## 3. Own board checklist: layout and assembly

| Number | Check | Norm |
| --- | --- | --- |
| 1 | Power width | Wide polygons, ground star |
| 2 | Decoupling capacitors | 100 nF no further than 3 mm from pins |
| 3 | Analog part | Separate island, short path to VDDA |
| 4 | Crystal and 32 kHz | Solid ground under the package, no digital tracks nearby |
| 5 | SWD and buttons | Access after case assembly |
| 6 | First assembly | Solder power, then the chip, then peripherals |
| 7 | First power-on | Through a lab PSU with a 100 mA limit |
| 8 | Eye X-ray | Magnifier, power short test |

If there is a short on power, do not turn it on again; look for a solder drop between pins under the microscope.

## 4. Firmware release checklist

| Number | Release point | How to check |
| --- | --- | --- |
| 1 | Version and git tag | Number in the UART greeting matches the package |
| 2 | Watchdog timer WDT | Hang on purpose, the board restarts by itself |
| 3 | Read protection RDP | Level set, firmware does not read out |
| 4 | Factory settings | After erase and first start all works without manual steps |
| 5 | Error log | Last 20 errors visible via a UART command |
| 6 | Backup and rollback | Previous firmware nearby, rollback in a minute |
| 7 | Field update | Verified over UART or USB without a programmer |
| 8 | CubeMX and HAL pinned | Versions recorded, project builds from scratch |

Project generation is recalled by [[09-Firmware/01-CubeIDE-CubeMX.en | CubeMX settings]], and update by [[EN/15-Protocols/02-DFU-Bootloader.en|firmware update]].

## 5. Battery checklist: sleep measurement and budget

| Number | Action | Figure |
| --- | --- | --- |
| 1 | Turn off the debugger before measuring | ST-Link disconnected, battery powered |
| 2 | Move all free pins to analog mode | Free pins do not float |
| 3 | Turn off unused peripherals | UART, ADC, timers sleep with the core |
| 4 | Measure current in Stop | Target single microamps, not milliamps |
| 5 | Measure wake-up time | Milliseconds, not seconds |
| 6 | Calculate the budget | Battery capacity divided by average current |
| 7 | Check self-discharge and cold | 30 percent reserve for frost and aging |
| 8 | Write a profile | Sleep, measure, transmit, sleep again |

Sleep theory is given by [[07-Timers/03-Sleep-Stop-Standby.en | sleep modes]], pin modes by [[03-GPIO/01-GPIO-Modes.en | GPIO modes]], and the port by [[EN/04-Interfaces/01-UART.en | UART serial port]].

## 6. Mermaid: from the box to the series

```mermaid
flowchart LR
    Box[Board from the box] --> PWR[Power and inspection]
    PWR --> ERASE[Connection and erase]
    ERASE --> BLINK[Blink 1 Hz]
    BLINK --> CLK[Clock and UART]
    CLK --> OWN[Own board: schematic and layout]
    OWN --> REL[Release: WDT and protection]
    REL --> BAT[Battery: sleep and budget]
    BAT --> SER[Series ready]
```

Do not move to the next box until the previous one is green. Hurry at the start costs a series rework.

## 7. Typical failures of starting a series

| Number | History | Conclusion |
| --- | --- | --- |
| 1 | Forgot SWD on your own board | Had to solder to pins, added a connector in the revision |
| 2 | BOOT0 without a resistor floated | Board sometimes started into the bootloader, put 10 kOhm to ground |
| 3 | VDDA connected over a long wire | ADC noisy, reworked filter and ground |
| 4 | Release without WDT | Customer hang fixed by driving over, added a watchdog |
| 5 | Sleep not measured, trusted the datasheet | Real current a hundred times larger, rewrote pin init |
| 6 | No firmware backup | Rollback took a day, now two files in the release |

Before ordering a batch reread [[EN/00-Start/01-How-to-Use-Guide.en|reference guide]] and check chips against [[EN/00-Start/03-Chip-Comparison.en|chip comparison]].

## 8. Checklist for the first power-on of your board

| Number | Action | Criterion |
| --- | --- | --- |
| 1 | Inspection: jumpers, polarity, excess solder | Purely visual |
| 2 | Ring 3.3V to GND | No short! |
| 3 | PSU with a 100 mA limit | Current does not hit the limit |
| 4 | Measure 3.3V and quiescent current | Voltage within tolerance, current in milliamps |
| 5 | ST-Link: read the chip ID | Chip visible |
| 6 | Mass erase | Memory clean |
| 7 | Flash Blink | LED blinks |
| 8 | UART log starts | Console alive |
| 9 | Check clocking with MCO | Frequency as in CubeMX |
| 10 | Run peripherals one by one | I2C, SPI, ADC answer |

```text
Якщо струм одразу в обмеження:
  вимкнути НЕГАЙНО;
  шукати коротке: переплутаний LDO, намистина припою, TVS навпаки;
  гріється — винуватець знайдений пальцем.
```

## See also

- [[Home.en | Home]]
- [[02-Power-Supply/01-Power-Supply-Rails.en | board power rails]]
- [[09-Firmware/01-CubeIDE-CubeMX.en | CubeMX settings]]
- [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]]
- [[EN/14-Devboards/01-Blue-Pill.en|Blue Pill board]]
- [[EN/15-Protocols/02-DFU-Bootloader.en|firmware update]]
- [[EN/99-Additions/01-Troubleshooting-FAQ.en|answers to frequently asked questions]]
- [[EN/99-Additions/03-Datasheet-Links.en|where to get datasheets]]


## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.


## Official sources

- STMicroelectronics reference manuals and datasheets
- Official ST-Link documentation
- Arduino / Raspberry Pi official guides
