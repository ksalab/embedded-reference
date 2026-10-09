---
title: Checklists - starting the board and entering the series
description: Checklists for the first launch of the board, home-made printing, firmware release and battery power for a smooth release into the series.; shows schematics, code and tables.
tags: [stm32, checklist, bringup, production]
category: Dodatki
lang: en
original: STM32-Reference/99-Additions/02-Cheklisti.md
date-created: 2026-10-01
date: 2026-10-08
---

# Checklists - starting the board and entering the series
![[assets/img/stm32-checklist-scheme.png|600]]
*Rice. Four checklists: first launch, own board, firmware release, battery.*

> [!tip] Note assignment
> Give a paper procedure: from the first supply of power to the box with the series, so that nothing is forgotten in the stress of the deadline.

## 1. Checklist for the first startup of the factory board

Do not apply power randomly. Go line by line and mark only after measurement.

| Number | Action | A sign of readiness
| --- | --- | --- |
| 1 | Examine the board with a magnifying glass: snot, cracks, crooked USB | The tracks are clean, the connectors are even
| 2 | Check the power jumper and BOOT0 | BOOT0 on ground, power supply 3.3V or 5V by silkscreen |
| 3 | Supply power through current limiting | The current is tens of milliamperes, nothing heats up
| 4 | Measure 3.3 V on the pins of the microcontroller | 3.2-3.4 V, pulsations are small
| 5 | Connect ST-Link with a short loop | The programmer is visible in the system |
| 6 | Make connections and mass erasure | The chip responds, the memory is clean
| 7 | Hall Blink LED 1 Hz | The LED blinks exactly |
| 8 | Check clocking via MCO | Frequency matches CubeMX |
| 9 | Check the UART by saying hello to the terminal | Garbage free text at 115200 |
| 10 | Save successful settings to notes | Frequencies, version of the board and firmware are recorded |

Connection details are described in the note about firmware via ST-Link, and power in the note about board power circuits. See [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]] and in [[02-Power-Supply/01-Power-Supply-Rails.en | board power supply circuits]].
## 2. Checklist of your fee: diagram

| Number | Checking the scheme | What are we asking?
| --- | --- | --- |
| 1 | Food and land Are all VDD and VSS connected, is there 100nF near each pair of |
| 2 | VDDA and VREF | Is there a filter or not hanging in the air |
| 3 | Reset NRST | Is there a tensioner of 10 kΩ and a capacitor of 100 nF |
| 4 | BOOT0 | Is there a 10 kΩ ground resistor and a place for a jumper |
| 5 | Quartz | Is there a load according to the datasheet, or are there short lines?
| 6 | SWD connector | Are SWDIO, SWCLK, NRST, GND, 3.3 V |
| 7 | Buttons and LEDs Is there no conflict with SWD and bootloader |
| 8 | 5 V tolerance | Is the FT column checked for each input 5 V | Classic cases will remind [[01-Hardware/01-F0-F1-Classic classic F0 and F1]], and board selection [[14-Devboards/03-Nucleo | Nucleo boards]].
## 3. Checklist of your board: printing and installation

| Number | Verification | Norma |
| --- | --- | --- |
| 1 | Feed width | Wide polygons, the star of the earth |
| 2 | Decoupling capacitors | 100 nF no further than 3 mm from pins |
| 3 | Analog part | Private island, short drive to VDDA |
| 4 | Quartz and 32 kHz | Solid ground under the case, without digital tracks nearby |
| 5 | SWD and | buttons Access after assembling the case |
| 6 | The first installation | Solder the power supply, then the chip, then the peripheral |
| 7 | First power on | Through a laboratory with a limit of 100 mA |
| 8 | X-ray eyes Magnifying glass, short-circuit power supply

If there is a short on the power supply, do not turn it on again, but look for a drop of solder between the foams under a microscope.

## 4. Firmware release checklist

| Number | Release point | How to check |
| --- | --- | --- |
| 1 | Version and git tag | The number in the UART hi and on the case matches |
| 2 | Watchdog WDT | Hang on purpose, the board restarts itself |
| 3 | RDP Read Protection | The level is set, the firmware does not merge |
| 4 | Factory settings | After erase and the first start, everything works without manual actions |
| 5 | Error Log | The last 20 errors are visible on the UART command |
| 6 | Backup and rollback Previous firmware is nearby, rollback in a minute
| 7 | Update in field | Tested via UART or USB without a programmer |
| 8 | CubeMX and HAL are fixed | The versions are recorded, the project is assembled from scratch The generation of the project will remind [[09-Firmware/01-CubeIDE-CubeMX.en | CubeMX settings]], and update [[15-Protocols/02-DFU-Bootloader | firmware update]].
## 5. Battery checklist: sleep measurement and budget

| Number | Action | Digit |
| --- | --- | --- |
| 1 | Turn off the debugger before measuring | ST-Link disconnected, battery powered |
| 2 | Convert all free pins to analog mode | Free foams do not hang in the air |
| 3 | Turn off unnecessary peripherals | UART, ADC, timers sleep together with the core |
| 4 | Measure the current in Stop | The purpose of the unit is microamps, not milliamps |
| 5 | Measure the time of awakening | Milliseconds, not seconds |
| 6 | Calculate the budget Divide the battery capacity by the average current |
| 7 | Check self-discharge and cold | Reserve 30 percent for frost and aging |
| 8 | Write a profile | Sleep, measurement, transfer, sleep againThe theory of sleep is given by [[07-Timers/03-Sleep-Stop-Standby.en | sleep modes]], pin modes [[03-GPIO/01-GPIO-Modes.en | GPIO modes]], and port [[04-Interfaces/01-UART | UART serial port].
## 6. Mermaid: from the box to the series```mermaid
flowchart LR
Box[Board from the box] --> PWR[Power and Review]PWR --> ERASEERASE --> BLINK[Blink 1 Hz]BLINK --> CLK[Clock and UART]CLK --> OWN[Own board: schematic and print]OWN --> REL[Release: WDT and Protection]REL --> BAT[Battery: Sleep and Budget]BAT --> SER[Series ready]```
Do not move to the next rectangle until the previous one is green. Haste at the start is worth resoldering the series.

## 7. Typical failures of starting a series

| Number | History | Conclusion |
| --- | --- | --- |
| 1 | Forgot to display SWD on your board | I had to solder to the pins, they added a connector in the revision
| 2 | BOOT0 without a resistor hung in the air | The board sometimes started in the bootloader, put 10 kΩ to the ground |
| 3 | VDDA was connected through a long wire | A/D noise, the filter and ground were redone
| 4 | Release without WDT | The client's hangover was treated by driving, a watchman was added
| 5 | Sleep was not measured, believe the data sheet The real current is a hundred times greater, the initialization of the pins has been rewritten |
| 6 | There is no firmware backup Rollback took a day, now two files in release |Перед замовленням партії перечитай [[00-Start/01-Yak-koristuvatis-dovidnikom | reference guide]] and звір чипи with [[00-Start/03-Porivnyannya-chipiv | chip comparison]].
## 8. Checklist for the first activation of your board

| Number | Action | Criterion |
| --- | --- | --- |
| 1 | Overview: jumpers, polarity, excess solder | Purely visual
| 2 | Ring 3.3V to GND | There is no short! |
| 3 | BZ with a limit of 100 mA | The current does not touch the limit |
| 4 | Measure 3.3V and the quiescent current | Tolerance voltage, milliamperes current |
| 5 | ST-Link: read chip ID | The chip is visible |
| 6 | Mass erase | Memory is clean
| 7 | Pour Blink | LED flashes |
| 8 | UART-log starts | The console is alive |
| 9 | Check the timing of the MCO | Frequency as in CubeMX |
| 10 | Drive the periphery one by one | I2C, SPI, ADC correspond to |```text
Якщо струм одразу in обмеження:
  вимкнути НЕГАЙНО;
  шукати коротке: переплутаний LDO, намистина припою, TVS навпаки;
  гріється — винуватець знайдений пальцем.
```
## See also- [[Home | Home]]
- [[02-Power-Supply/01-Power-Supply-Rails.en | board power supply circuits]]
- [[09-Firmware/01-CubeIDE-CubeMX.en | CubeMX settings]]
- [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]]
- [[14-Devboards/01-Blue-Pill | the Blue Pill fee]]
- [[15-Protocols/02-DFU-Bootloader | firmware update]]
- [[99-Additions/01-Troubleshooting-FAQ | answers to frequently asked questions]]
- [[99-Additions/03-Datasheet-Links | where to take datasheets]]


## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.


## Official sources

- STMicroelectronics reference manuals and datasheets
- Official ST-Link documentation
- Arduino / Raspberry Pi official guides
