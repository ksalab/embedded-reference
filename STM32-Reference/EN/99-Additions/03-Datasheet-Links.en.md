---
title: Datasheets - what to read and where to get them
description: Hierarchy of ST documents from datasheet to upnotes, verified AN numbers and rules for reading errata before ordering a board.; shows schematics, code and tables.
tags: [stm32, datasheet, reference-manual, errata]
category: Dodatki
lang: en
original: STM32-Reference/99-Additions/03-Datasheet-Links.md
date-created: 2026-10-01
date: 2026-10-08
---

# Datasheets - what to read and where to get them
![[assets/img/stm32-datasheet-links-scheme.png|600]]
*Rice. Pyramid of documents: datasheet, reference manual, programming manual, errata, upnotes.*

> [!tip] Note assignment
> To explain which document is responsible for what, where the original source is and which upnotes actually exist, so as not to Google garbage.

## 1. Hierarchy of ST documents

| Document | What is inside | When to open |
| --- | --- | --- |
| Data sheet | Foams, cases, memory, 5 V tolerance, currents, temperatures | Chip selection and pin check |
| Reference Manual | Registers, clocking, DMA, interrupts, sleep modes | Driver writing and debugging
| Programming Manual | Cortex core, interrupt system, instructions, MPU | HardFault, priorities, assembler |
| Errata Sheet | Errors of silicon specific revisions and bypasses | Before the order is paid and before the release
| Application Note AN | Ready-made recipes: bootloader, quartz, ADC, USB | When you make a knot for the first time |
| User Manual of the board | Nucleo circuit, jumpers, ST-Link on board | The first launch of the factory board |

One rule: doubt is decided by the original source on st.com, not a forum or repost.

## 2. Where to pump so as not to catch the old one

| Source | What to take | Why |
| --- | --- | --- |
| st.com, chip page | Datasheet, Reference Manual, Errata of the latest revisions | Always fresh, with date and revision |
| st.com, search by AN | Downloads in PDF with number and date | No overwritten copies |
| STM32CubeMX | Headers HAL and SVD register description | Matches your version of HAL |
| STM32CubeProgrammer | Latest firmware algorithms | Old software does not see new chips
| Project archive Saved PDFs with download date | In a year, you will prove what you bred for

Never pay for a datasheet from an unknown mirror. Beast revision number in the footer.

## 3. Key upnots: only real numbers

| Number | Topic | What to take |
| --- | --- | --- |
| AN2606 | System memory boot mode, factory bootloader | Table of bootloader interfaces for each chip |
| AN2586 | Getting started with hardware development | Minimum binding: power, reset, quartz |
| AN2867 | Oscillator design guide | Selection of quartz, loading, tracing |
| AN2834 | How to get the best ADC accuracy | VDDA, support, ground, averaging |
| AN2668 | Improving ADC resolution by oversampling | Oversampling and filtering for bits |
| AN4899 | GPIO hardware settings and low-power | Settings for sleep and current pins |
| AN3155 | USART protocol used in bootloader | Firmware protocol via UART |
| AN4879 | USB hardware and PCB guidelines | USB wiring, protection, power |
| AN2824 | I2C optimized examples | Examples of polling, interrupts and DMA for I2C |
| AN1709 | EMC design guide | Protection against interference and static discharge |

All numbers above exist on st.com. If you see a different number on the blog, check it by searching on the manufacturer's website. Reference reference: bootloader in [[15-Protocols/02-DFU-Bootloader | firmware update]], port in [[04-Interfaces/01-UART | UART serial port]], bus in [[04-Interfaces/03-I2C | I2C bus]], measurement in [[06-Analog/01-ADC.en | measurement via ADC]].
## 4. How to read a datasheet in twenty minutes

| Minute | Section | What do we write out |
| --- | --- | --- |
| 0-3 | Ordering information Exact part number, amount of memory, case |
| 3-7 | Pinout | Power, NRST, BOOT0, SWD, FT foam |
| 7-12 | Electrical characteristics | Power supply range, foam current, temperature |
| 12-16 | Clock and timing | HSE, LSE, requirements for capacitors |
| 16-20 | Package drawings Landing place and thermal requirements |Start with the classics [[01-Hardware/01-F0-F1-Classic | classic F0 and F1]] and the beast from [[00-Start/03-Porivnyannya-chipiv | chip comparison]].
## 5. How to read errata before ordering a fee

| Step | Action | Example |
| --- | --- | --- |
| 1 | Find your chip revision | Letters on the body and marking |
| 2 | Open the errata for this revision The date is fresher than your datasheet
| 3 | Walk around your periphery UART, I2C, ADC, sleep, USB |
| 4 | Write the detours in the code | Flag, Reset, Delay |
| 5 | Check the effect on the board | Other quartz, filter, brace |
| 6 | Save PDF to repository | The docs folder with the date |

The most expensive mistake is finding out about the I2C bug after printing. An hour with errata is cheaper than resoldering.

## 6. Mermaid: which document when```mermaid
flowchart TB
Q[Task] --> SEL{Chip Selection?}SEL -->|Yes| DS[Datasheet: memory, legs, FT]SEL -->|No| DRV{Are you writing a driver?}DRV -->|Yes| RM[Reference Manual: registers]DRV -->|No| ERR{Preparing the board?}ERR -->|Yes| ES[Errata plus AN2586 plus AN2867]ERR -->|No| BOOT{Firmware from the factory?}BOOT -->|Yes| AN2606[AN2606: bootloader modes]BOOT -->|No| ADC{Accurate Measurements?}ADC -->|Yes| AN2834[AN2834 plus AN2668: ADC]ADC -->|No| GPIO[AN4899: foam and sleep]```
Move from top to bottom. Do not get into the reference manual until you have covered the issue of the case and power supply.

## 7. Cheat sheet for contacts with the directory

| Guide topic | Document ST |
| --- | --- |
| Power board and VDDA | Datasheet plus AN2834 |
| Modes of foams and sleep | AN4899 plus Reference Manual GPIO |
| UART bootloader | AN2606 plus AN3155 |
| Bus of sensors | AN2824 plus Reference Manual I2C |
| ADC and noise | AN2834 plus AN2668 |
| The first launch of the board | User Manual board plus note Nucleo |
| Firmware by a programmer Note ST-Link plus CubeProg manual |Додатково тримай поруч [[03-GPIO/01-GPIO-Modes.en | GPIO modes]] and [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]] for швидкої звірки.

Перший запуск плати дивись у [[14-Devboards/03-Nucleo | Nucleo boards]], карту клонів у [[14-Devboards/01-Blue-Pill | the Blue Pill fee]], старт проєкту у [[09-Firmware/01-CubeIDE-CubeMX.en | CubeMX settings]].
## 8. Typical reading errors

| Number | Error | Consequence | How correct |
| --- | --- | --- | --- |
| 1 | Read old revision PDF | Pins do not match | Check the date and revision on st.com |
| 2 | Confuse maximum with typical | Overheating and subsidence Design according to maximum, battery according to typical |
| 3 | Ignore footnote FT | 5 V burns input | Check the FT column for each pin |
| 4 | Do not open errata | Bug catches silicon in series | Read errata to tracing |
| 5 | Believe copies from the forum | Legacy tables bootloader | Only AN2606 from the manufacturer's website |
| 6 | Do not save PDF | A year later, the solution cannot be proved | Dated docs folder in repository |for старту with нуля відкрий [[00-Start/01-Yak-koristuvatis-dovidnikom | reference guide]] and оновлення [[15-Protocols/02-DFU-Bootloader | firmware update]].
## See also- [[Home | Home]]
- [[00-Start/01-Yak-koristuvatis-dovidnikom | reference guide]]
- [[01-Hardware/01-F0-F1-Classic | classic F0 and F1]]
- [[04-Interfaces/03-I2C | I2C bus]]
- [[06-Analog/01-ADC.en | measurement via ADC]]
- [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]]
- [[14-Devboards/01-Blue-Pill | the Blue Pill fee]]
- [[99-Additions/01-Troubleshooting-FAQ | answers to frequently asked questions]]
- [[99-Additions/02-Cheklisti | checklists]]


## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.


## Official sources

- STMicroelectronics reference manuals and datasheets
- Official ST-Link documentation
- Arduino / Raspberry Pi official guides
