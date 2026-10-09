---
title: Troubleshooting - frequently asked questions and answers
description: Compilation of common STM32 faults from firmware to sleep and ADC, symptom table and quick troubleshooting technique.; shows schematics, code and tables.
tags: [stm32, faq, debug, troubleshooting]
category: Dodatki
lang: en
original: STM32-Reference/99-Additions/01-Troubleshooting-FAQ.md
date-created: 2026-10-01
date: 2026-10-08
---

# Troubleshooting - frequently asked questions and answers
![[assets/img/stm32-faq-faq-scheme.png|600]]
*Rice. Fault finding logic: power, timing, firmware, peripherals, sleep.*

> [!tip] Note assignment
> Collect nine out of ten requests from newbies in one table: what we see, what is most often at fault and which reference note to open next.

## 1. The rule is measure, don't guess

The main mistake of a beginner is to change the code at random. The correct order is always the same: power, clock, reset, firmware, peripherals, program.

| Step | What do we measure | What | Norma |
| --- | --- | --- | --- |
| 1 | Supply voltage on the foam of the microcontroller | Multimeter | 3.3 V plus minus 0.1 V |
| 2 | Pulsations and subsidence under load | Oscilloscope | Tens of millivolts, without dips
| 3 | Level on NRST in work | Multimeter | High level, short reset pulses |
| 4 | Quartz frequency and PLL output | Oscilloscope, output MCO | Matches the setting in CubeMX |
| 5 | The flow of consumption in work and in sleep Multimeter, shunt | Milliamps in work, microamps in sleep
| 6 | Logic levels on the tires | Logic analyzer | Clear fronts without steps

No guess is counted without a number on the device screen. Record the measurements in the debugging notebook immediately.

For power details, see the note about board power circuits, and for pin modes, see the note about GPIO modes.

## 2. Symptom, cause, where to look

| Symptom | The most frequent reason | Where to look |
| --- | --- | --- |
| The board is not sewn, the programmer does not see the chip No power, SWDIO and SWCLK mixed up, chip in deep sleep | A note about ST-Link, Power Section |
| The board sews, but does not start | BOOT0 in high level, forgotten SystemClock, hang in HardFault | Note on CubeMX, Blue Pill Map |
| Silent UART, in the terminal garbage | Incorrect clock frequency, confused reception and transmission, different speed | A note on UART, GPIO modes |
| The ADC makes noise, the codes jump Dirty analog ground, unfiltered VDDA, long sensor wires | A note about ADC, board power |
| Awake, the current is milliamperes instead of microamperes Foam in the air, the peripherals are not turned off, the debugger holds the core | A note about sleep modes |
| Brake, the cycle is executed slowly | Wait in interrupts, float on non-FPU core, high polling rate | Comparison of chips, classic F0 and F1 |
| HardFault crashes after changing the code | Null pointer access, stack overflow, unaligned access | Note on CubeMX Reference Guide |
| Does not find the I2C device on the scanner | Missing braces, wrong address, stuck tire after reset | A note about the I2C bus |
| Time flies, the clock rushes or falls behind Internal RC instead of quartz, incorrect prescaler, timer overflow | A note about sleep modes, timers |
| The stabilizer or chip is heating up Short circuit, 5 V on non-tolerant input, output overload | Board power circuits |Deciphering the lines: the firmware is described in the note [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]], start of the project in [[09-Firmware/01-CubeIDE-CubeMX.en | CubeMX settings]], serial port in [[04-Interfaces/01-UART | UART serial port]], sensor bus in [[04-Interfaces/03-I2C | I2C bus]], measurement in [[06-Analog/01-ADC.en | measurement via ADC]], sleep in [[07-Timers/03-Sleep-Stop-Standby.en | sleep modes]].
## 3. Does not sew and does not start

| Verification | How to do | A sign of success
| --- | --- | --- |
| Power has reached the foam | Measure between VDD and VSS directly on the case | 3.3 V, stable |
| Connection of the programmer | SWDIO, SWCLK, GND, NRST, if necessary 3.3 V | Short wires up to 20 cm |
| Boot Mode | BOOT0 on the ground to work from flash | After the firmware, the board starts itself
| Read Protection | Try the connection under reset, then erase | Memory is cleared without errors |
| Driver and software ST-Link Upgrade, CubeProgrammer latest | The programmer is visible in the system |
| Clone board | Check the marking and soldering of the quartz | Even soldering without cold spots

If the chip went to sleep in Stop with SWD off, hold reset while pressing Connect, then immediately do a mass erase. See the clone map in [[14-Devboards/01-Blue-Pill | the Blue Pill fee]], power in [[02-Power-Supply/01-Power-Supply-Rails.en | board power supply circuits]], and classic chips in [[01-Hardware/01-F0-F1-Classic | classic F0 and F1]].
## 4. UART is silent and I2C is not visible

| Symptom | The reason | Action |
| --- | --- | --- |
| In the terminal the hieroglyphs | Baud is calculated from another frequency HCLK | Check timing, output frequency on MCO |
| Silence in response Mixed TX and RX, no common ground | Switch places, connect GND |
| Only works at low speed | Long wires, line capacity, weak braces | Shorten the train, reduce the speed
| I2C scanner finds nothing | No pull-ups 4.7 kΩ to 3.3 V | Add resistors, check the power supply of the sensor |
| The tire hangs after the error | The driven keeps SDA at zero | Nine pulses on SCL, then bus reset |
| The address is not the | Shift on the read bit of the record | Run the scanner from 0x08 to 0x77 |Detailed pin modes are described in [[03-GPIO/01-GPIO-Modes.en | GPIO modes]], and the start navigation in [[00-Start/01-Yak-koristuvatis-dovidnikom | reference guide]].
## 5. The ADC makes noise and time passes

| The problem | What to check | Norma |
| --- | --- | --- |
| The lower bits of the ADC jump | VDDA filter, capacitors near pins | 100 nF plus 1 µF right next to the case |
| Systematic displacement | Calibration, support, divider | Calibrate after each gain change |
| Hints from the number | Analog ground tracing, pause survey | Measurement at the moment of silence, averaging of 16 samples |
| The timer is in a hurry | Source HSI instead of HSE | 8 MHz quartz for precise intervals |
| Periodic freezing | 16-bit counter overflow | Go to 32 bit or count overflow |
| Real Time Clock Drift | Quartz load 32 kHz | Capacities according to the data sheet |The basic theory of measurements is revealed by [[06-Analog/01-ADC.en | measurement via ADC]], and the power supply of the sensor [[02-Power-Supply/01-Power-Supply-Rails.en | board power supply circuits]].
## 6. A minimal example to reproduce the bug

Do not send the entire project. Cut ten lines where the bug is visible without your iron.```text
Minimum repetition:1. New CubeMX project, only HSE 8 MHz, UART1 115200.2. In main, only Blink LED 1 Hz.3. You add ONE suspicious line: driver call, interrupt, DMA.4. If it breaks: this is a repeat. If not: add the next line.5. Fix: HCLK frequency, HAL version, what is on the oscilloscope, what is in the logs.```
| Report field | Example of filling |
| --- | --- |
| Board and chip | Self-made on F103C8, power supply 3.3 V |
| Timing | HSE 8 MHz, PLL at 72 MHz, MCO tested |
| What did you expect? UART responds every second |
| What got | Silence, on TX constant unit |
| What has already been measured | TX oscilloscope, ground, speed 115200 |
| Minimum code | Archive with three files or insert below |

Such a report is analyzed in ten minutes instead of three days of correspondence.Порівняння чипів for вибору швидкості дивись у [[00-Start/03-Porivnyannya-chipiv | chip comparison]].
## 7. Mermaid: fault finding algorithm```mermaid
flowchart TB
    Start[Щось not працює] --> PWR{Живлення 3.3 in on ніжках?}
    PWR -->|Ні| PSU[Перевір стабілізатор, діоди, перемички]
    PWR -->|Так| CLK{Тактування how у CubeMX?}
    CLK -->|Ні| OSC[Перевір HSE, PLL, MCO осцилографом]
    CLK -->|Так| SWD{Програматор бачить чип?}
    SWD -->|Ні| BOOT[BOOT0 on землю, скидання, erase]
    SWD -->|Так| RUN{Старт після прошивки?}
    RUN -->|Ні| FAULT[Дивись HardFault, стек, Watchdog]
    RUN -->|Так| PER[Перевір UART, I2C, АЦП по черзі]
    PER --> OK[Локалізуй до одного драйвера]
```
Go from top to bottom and don't jump over. Ninety percent of bugs are closed on the first three diamonds.

## 8. Typical mistakes of beginners

| Number | Error | What ends | How correct |
| --- | --- | --- | --- |
| 1 | Long SWD wires through the breadboard | Random disconnections | Short plume, land nearby |
| 2 | 5 V on the non-tolerant pin | Input failure, heating | See the FT column in the datasheet |
| 3 | Delays in interruptions | Package skips, brakes | Only the flag |
| 4 | Foam in the air before sleep | Milliamps instead of microamps | All free in analog mode |
| 5 | Belief in Clone Marking | Less memory, different quartz | Check with the programmer |
| 6 | Capacitor treatment at random | Masking subsidence | First, measure the current and pulsationsFor the first start of the factory board, open [[14-Devboards/03-Nucleo | Nucleo boards]] and [[14-Devboards/01-Blue-Pill | the Blue Pill fee]], and for classic chips [[01-Hardware/01-F0-F1-Classic | classic F0 and F1]].
## 9. Diagnostic levels: L1, L2, L3

| Level | What are we doing? Tool | Time |
| --- | --- | --- | --- |
| L1 Quick fix | Power supply, wires, BOOT0, jumpers | Eyes and a multimeter 5 minutes
| L2 Software and config | Clocking, NVIC, DMA channels, init bugs | Debugger and log | Hour |
| L3 Depth | Quartz, wiring, interference, lack | Oscilloscope and analyzer | Day |```text
Escalation rule:L1 failed twice - go to L2, don't twist wires for an hour;L2 did not give a result - do a minimal example and measure iron (L3).```
## 10. Decision tree: not stitched```mermaid
flowchart TB
    S[Не шиється] --> LED{LED живлення горить?}
    LED -->|Ні| VDD[Заміряй 3.3 В: БЖ, діод, LDO, коротке]
    LED -->|Так| DET{ST-Link бачить чип?}
    DET -->|Ні| WIRE[Дроти SWDIO SWCLK GND коротші, частота нижче]
    WIRE -->|Не допомогло| URESET[Connect Under Reset + mass erase]
    DET -->|Так| ERASE[Full chip erase, потім ший знову]
    URESET --> RDP{RDP рівень 2?}
    RDP -->|Так| DEAD[Чип закритий назавжди]
    RDP -->|Ні| UARTB[BOOT0 в 1, ший через UART bootloader]
```
## 11. Decision Tree: Works unstable```mermaid
flowchart TB
U[Reset and freeze] --> WDG{Is there a pattern?}WDG -->|Periodically| PWR2[Power sag: bulk, BZ, radio peaks]WDG -->|Random| EMI[Interference: ground, TVS, relay nearby]WDG -->|After firmware| STK[Stack: Overflow, HardFault, MPU]PWR2 --> BOR[Enable BOR and PVD, see flags]EMI --> SHD[Ferrites, shields, decoupling]STK --> MAP[Map file: stack size, no recursion?]```

Повну карту симптомів дивись in [[99-Additions/04-Diagnostic-Map | diagnostic card]].
## 12. Power FAQ: drops and pulsations

| Symptom | The reason | What to do |
| --- | --- | --- |
| Reset when starting the radio | The current peak plants the line | Bulk 10 μF+ near the radio, BJ with a reserve |
| Ripples on the ADC synchronously with PWM | Joint decoupling | Ferrite and individual capacitors on VDDA |
| Does not start on battery, works from USB | Internal resistance of the bank | Fresh can, short thick wires |
| The LDO is heated | Big drop and current | Count dispersion, or buck |
| Failure at the first millisecond | The charge of the output containers | Soft-start, more bulk at the entrance |
| Works only with the debugger | Power comes from ST-Link | Test your power without a debugger |```mermaid
flowchart TB
    P[issue живлення] --> V{Напруга стабільна?}
    V -->|Ні| SRC[БЖ, діод, LDO, коротке]
    V -->|Так| RIP{Пульсації під навантаженням?}
    RIP -->|Так| CAP[Декуплінг, bulk, земля]
    RIP -->|Ні| CUR{Струм у нормі?}
    CUR -->|Ні| LEAK[Хто їсть: периферія, піни, сон]
    CUR -->|Так| SEQ[Порядок живлень and BOR]
```
## 13. Radio FAQ: non-join and bad RSSI

| Symptom | The reason | What to do |
| --- | --- | --- |
| BLE does not advertise | Stack not filled or FUS old | FUS and stack in one package! |
| Does not connect | UUID is not in the ad | Add services to the package |
| LoRa does not join | Keys or frequency | OTAA keys, region range |
| Packets are lost | Weak signal | Antenna, SF above, gateway above |
| Ban on the server | Duty-cycle exceeded | Less frequent packets, lower SF |
| Works on the table, not in the field Body and arm | Test in real conditions |

## 14. FAQ on boards: Blue Pill, Black Pill, Nucleo

| Fee | Symptom | Reason and fix |
| --- | --- | --- |
| Blue Pill | Does not sew via USB There is only power! ST-Link or UART |
| Blue Pill | BOOT0 back forgotten | The board hangs in the bootloader - switch |
| Blue Pill | The LDO is heated | The load is large - separate power |
| Blue Pill | Less Flash than writing | Clone: ​​check st-info |
| Black Pill | DFU is not visible | BOOT0 button when connecting USB! |
| Black Pill | The CDC is silent | Descriptors and drivers VCP |
| Nucleo | Does not see the external board | Remove the ST-Link jumpers! |
| Nucleo | Power supply JP5 is not | U5V, E5V, VIN - choose your |
| Nucleo | Current measurement is zero | Is the IDD jumper in place? |
| Discovery | The display is white BSP init sequence, backlight power |
| Discovery | No sound | I2S and amplifier in shutdown |

## 15. HardFault decoder: we read the cause of the crash

| Register | Bit | Value |
| --- | --- | --- |
| HFSR | FORCED | Another fault escalated - see below
| HFSR | VECTTBL | Error reading vector table |
| CFSR.BFSR | PRECISERR | Exact bus error - address in BFAR! |
| CFSR.BFSR | IMPRECISERR | Inaccurate - look for the culprit by code |
| CFSR.UFSR | UNDEFINSTR | Unknown instruction - broken code or jump |
| CFSR.UFSR | INVSTATE | Attempting ARM mode on Cortex-M |
| CFSR.UFSR | DIVBYZERO | Division by zero (if trap is on) |
| CFSR.MMSR | IACCVIOL | Execution from forbidden area (MPU!) |
| CFSR.MMSR | DACCVIOL | Access to restricted area |```c
// A minimal catcher with a dump to the console:void HardFault_Handler(void)
{
  print_hex("HFSR", SCB->HFSR);
  print_hex("CFSR", SCB->CFSR);
  print_hex("BFAR", SCB->BFAR);
  print_hex("MMFAR", SCB->MMFAR);
  while (1) { blink_sos(); }
}
```

```text
Deciphering the drop address:1. Take the address from BFAR or from the stack (PC at the time of fault);2. arm-none-eabi-addr2line -e firmware.elf <address>;3. Get the culprit file and string.Typical culprits: NULL pointer, stack overflow, reading from a disabled peripheral.```
## 16. Symptom Index: Fast Entry

| Symptom | Where to look |
| --- | --- |
| ADC makes noise | Section 5 of this note, VDDA filter |
| The battery drains quickly Sleep modes, sleep current with an ammeter |
| The chip is warming up In short, LDO on the contrary, firmware with a conflict of pins |
| Hangs randomly | Stack, interference, power sag |
| Does not see the I2C device | Address, braces, flat tire |
| Does not start after firmware | Clocking, WDG, vector table |
| Not sewn Tree 10 of this note |
| Works unstable | Wood 11 of this note |
| RTC Time Flow | LSE-quartz, VBAT, capacitors |
| The radio is silent FUS and stack, antenna, power PA |
| Resets under load | Bulk, BOR, current peaks |
| Garbage in UART | Baudrate, earth, inversion |
| SPI bit shift | CPOL and CPHA on both sides |

## See also- [[Home | Home]]
- [[00-Start/01-Yak-koristuvatis-dovidnikom | reference guide]]
- [[02-Power-Supply/01-Power-Supply-Rails.en | board power supply circuits]]
- [[04-Interfaces/01-UART | UART serial port]]
- [[04-Interfaces/03-I2C | I2C bus]]
- [[06-Analog/01-ADC.en | measurement via ADC]]
- [[07-Timers/03-Sleep-Stop-Standby.en | sleep modes]]
- [[09-Firmware/03-ST-Link-Flashing.en | firmware via ST-Link]]
- [[99-Additions/02-Cheklisti | checklists]]
- [[99-Additions/03-Datasheet-Links | where to take datasheets]]


## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.


## Official sources

- STMicroelectronics reference manuals and datasheets
- Official ST-Link documentation
- Arduino / Raspberry Pi official guides
