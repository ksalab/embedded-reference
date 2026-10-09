---
title: Quick STM32 pinout cheat sheet - LQFP/Pin-mapping
description: STM32 Pinout Quick Reference - Summary of key pins (ADC, UART, SPI, CAN, I2C, PWM, DMA) with source references.; shows schematics, code and tables.
tags: [stm32, pinout, quick-reference, lqfp, gpio, adc, pwm, dma]
category: Hardware
lang: en
original: STM32-Reference/99-Additions/05-Pinout-Quickref.md
date-created: 2026-10-01
date: 2026-10-08
---

# Quick STM32 pinout cheat sheet

| Pin | Name | Function | An example of using |
| --- | --- | --- | --- |
| PA0 | ADC_IN0 | Analog input | ADC with sensor |
| PA1 | ADC_IN1 | Analog input | Analog signal |
| PA2 | USART2_TX | UART | Console / Modem |
| PA3 | USART2_RX | UART | Data reception |
| PA4 | ADC_IN4 / DAC | Analog/DAC | Sensor / Audio |
| PA5 | SPI1_SCK | SPI clock | Display |
| PA6 | SPI1_MISO | SPI reception | Sensor |
| PA7 | SPI1_MOSI | SPI transfer | Camera |
| PA9 | USART1_TX | UART | Console |
| PA10 | USART1_RX | UART | Reception |
| PA13 | SWDIO | Debugging | JTAG/SWD |
| PA14 | SWCLK | Debugging | Sampling rate |
| PB6 | I2C1_SCL | I2C clock | Sensors |
| PB7 | I2C1_SDA | I2C data | Sensors |
| PB8 | CAN_RX | CAN reception | Industrial tire |
| PB9 | CAN_TX | CAN transmission | Industrial tire |
| PC6 | I2C3_SCL | I2C clock | Alternative |
| PC7 | I2C3_SDA | I2C data | Alternative |
| PC8 | TIM3_CH0 | PWM | Servo / LED |
| PC9 | UART3_RX | UART | Console |
| PD6 | UART2_RX | UART | Alternative |
| PD7 | UART2_TX | UART | Alternative |

## Short rules

- Analogue: PA0-PA7 | PC0-PC3 (depends on the series)
- UART: PA9/PA10 or PB10/PB11 - check AF
- SPI: PA5-PA7 or PB3-PB5 - standard with MYF for F4
- CAN: PB8/PB9 (F4/F7/H7) - check AF
- I2C: PB6/PB7 (standard) or PC14/PC15 (low consumption)
- PWM: TIM2-TIM5 on different AFs
- ADC + DMA: PA0 with TIM3 trigger for synchronization

## Note

Each STM32 series (F0, F3, F4, F7, H7, U5, L4) has different AF multipliers on different pins. Always check the table of each chip from the official datasheet (STM32CubeMX also generates one).

## 9.1 Quick F4/H7 expansion cheat sheet

| Signal | Pin (LQFP) | Note |
| --- | --- | --- |
| DCMI D0 | PA4 | Camera 8-bit |
| SWDIO | PA13 | Debugging |
| I2C SDA | PB7 | Sensors 400 kHz |
| CAN_RX | PB8 | Industrial tire |
| SPI MOSI | PB5 | Speed ​​40 MHz |

## Official sources- [[01-Hardware/01-F0-F1-Classic | F0/F1-classic]] - a place in the lineup.- [[01-Hardware/01-F0-F1-Classic | F0/F1-classic]] - a place in the lineup.- <https://www.st.com/resource/en/reference_manual/rm0091-stm32f0x1-stm32f0x2-stm32f0x8-reference-manual-stmicroelectronics.pdf> (F0/F1)
- <https://www.st.com/resource/en/reference_manual/rm0432-stm32f4-reference-manual-stmicroelectronics.pdf> (F3/F4)

## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.

## Supplement: Full pin mapping by port

| Port | Key pins | Function | Notes |
| --- | --- | --- | --- |
| PA0 | PA0 | ADC / WKUP | Analog start |
| PA1 | PA1 | ADC | Analog channel 1 |
| PA2 | PA2 | ADC | Analog channel 2 |
| PA3 | PA3 | ADC | Analog channel 3 |
| PA4 | PA4 | ADC / DAC | Analog with DAC |
| PA5 | PA5 | ADC / DAC | Analog with DAC |
| PA6 | PA6 | ADC | Analog channel 6 |
| PA7 | PA7 | ADC | Analog channel 7 |
| PA8 | PA8 | I2C SDA / USB FS | Dual use |
| PA9 | PA9 | USART1 TX | Serial TX |
| PA10 | PA10 | USART1 RX | Serial RX |
| PA13 | PA13 | SWDIO | Debug data |
| PA14 | PA14 | SWCLK | Debug clock |
| PA15 | PA15 | JTDI | JTAG data |
| PB0 | PB0 | ADC | Analog input |
| PB1 | PB1 | ADC | Analog input |

## Notes on quick reference use

- Always confirm pin functions against the datasheet for your specific STM32 variant; some pins have alternate functions.
- Use the reference table to plan connections before soldering; reserve PA13/PA14 for debugger access.
- Power pins (VDD, VSS) must be connected for every port group; do not leave any VDD floating.
- Analog pins near high-speed digital outputs may need filtering; keep traces short.
- For USB operation, PA11 (DM) and PA12 (DP) require precise 90-ohm differential routing.

*Quick reference completes pin identification; see official sources for full electrical specs.*
## Additional notes: power, ground and clock pins

| Pin group | Pins | Purpose | Check before use |
| --- | --- | --- | --- |
| VDD | 3V3 pins | Main supply | Verify voltage level |
| VSS | GND pins | Ground | Connect to common ground |
| NRST | Reset pin | System reset | Pull-up resistor recommended |
| BOOT | BOOT0 | Boot mode | Tie low for normal run |
| OSC | OSC_IN / OUT | Crystal | Match frequency to spec |

## Troubleshooting quick checks

- If LED does not blink: verify PA13/PA14 debugger connection and BOOT0 state.
- If UART is silent: check baud rate, TX/RX swap, and ground continuity.
- If ADC reads wrong: confirm reference voltage and pin mapping.
- If board resets unexpectedly: check power supply stability and decoupling capacitors.
- For clock issues: verify crystal load capacitance matches datasheet; replace crystal if unstable.

## Reference links (official sources)
- STMicroelectronics STM32 datasheets: https://www.st.com/en/microcontrollers-microprocessors/stm32-mainstream-microcontrollers.html
- STM32CubeMX pinout view: use for full alternate-function mapping.
- Community quick-reference: compare with official datasheet before final design.

## Extended pin table for common STM32 families

| Family | Main GPIO | Special pins | Typical use |
| --- | --- | --- | --- |
| F1 | PA, PB, PC | PA13/14 debug | Learning / basic |
| F3 | PA, PB, PC | 5V tolerant inputs | Industrial |
| F4 | PA, PB, PC | Full-speed USB | Communication |
| L4 | PA, PB | Low power | Battery / IoT |
| G0 | PA, PB, PC | Small footprint | Cost-sensitive |

## Final reminder

Keep this quick reference beside the board during development. Cross-check every connection with the official datasheet. Do not assume pin functions; verify with multimeter and oscilloscope when debugging. Refer to official ST documentation for updates and errata.
