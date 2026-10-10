---
title: STM32 Comparators and Op-Amps
description: Explains STM32 comparator and op-amp operation from thresholds and hysteresis to motor protection; shows schematics, code and tables.
tags: [stm32, comparator, opamp, pga, bkin]
category: Analog
lang: en
original: 06-Analog/03-COMP-OPAMP.md
date-created: 2026-10-01
date: 2026-10-09
---

# STM32 Comparators and Op-Amps

![[assets/img/stm32-comp-opamp-scheme.png|600]]
*Fig. Protection diagram: current shunt, amplifier, comparator and emergency PWM stop with no core involvement.*

> [!tip] Purpose of this note
> Show the analog blocks that work with no core and no program: how a comparator watches a threshold with hysteresis, how its output mutes PWM through the emergency stop input and how the built-in amplifier lifts shunt millivolts to converter level.
> This note covers fast motor protection and current measurement with no external chips.

## 1. Purpose

A comparator compares two voltages and outputs a digital level: above threshold one, below threshold zero. An operational amplifier amplifies the difference and prepares a small signal for measurement. Both blocks run in hardware, so reaction takes tens of nanoseconds instead of interrupt microseconds.

This note serves everyone who builds overload protection, watches a battery, measures current over a shunt or amplifies a sensor. It explains where internal threshold references come from, why hysteresis is needed against chatter, which modes the built-in amplifier has and how to link all this to a timer with no code line in the critical path.

The main idea is simple: the fast protection path must be hardware. Software configures thresholds once, then hardware alone turns off switches on fault. The software path over converter and interrupt stays for slow tasks such as indication.

## 2. What a Comparator Can Do

A comparator has direct and inverse inputs, programmable reference choice and programmable hysteresis. The output can go to a pin, to the timer emergency stop input or serve as a wake-up event.

| Parameter | Typical values | Meaning |
| --- | --- | --- |
| Reaction time | About fifty nanoseconds in fast mode | Switch current muted before destruction |
| Internal reference | Internal reference, supply fractions, external pin | Threshold with no board divider |
| Hysteresis | Off or several millivolts | No chatter near threshold |
| Consumption | Fast mode more, slow mode less | Balance of speed and battery |
| Output | To pin, to timer, to interrupt | Flexible reaction with no core |

```text
Comparator with hysteresis against chatter:
  Sawtooth input with noise:
    ----/--/--/---- upper threshold
    .............. lower threshold
  Output without hysteresis:  _-_-_-_-,,,, pulse burst
  Output with hysteresis:     ______,,,,, one clean edge
  The gap between thresholds eats noise and ringing.
```

Fast mode suits switch protection, slow mode suits battery supervision. Fast mode draws more, but on mains supply this does not matter. In a battery product the slow mode runs background supervision and wakes the fast one only for measurement time.

## 3. Reference and Thresholds With No External Parts

The internal multiplexer picks a reference from several sources: internal stable reference, analog supply fractions, external pin. This replaces a two-resistor divider on board and removes their tolerances.

| Reference source | When to take | Threshold example |
| --- | --- | --- |
| Internal reference | Precise battery threshold | Lithium cell discharge voltage |
| Supply quarter | Rough supervision | Supply drop below norm |
| Supply half | Scale middle | Zero detector for AC signal |
| External pin | Precise external divider | Threshold set by precision reference |
| Amplifier output | Complex chains | Threshold after shunt gain |

| Channel | How to set |
| --- | --- |
| Fixed battery threshold | Internal reference to one input, battery through divider to other |
| Adjustable threshold | External potentiometer to reference input |
| Two thresholds as window | Two comparators with different references on one signal |

The internal reference wins on temperature stability. A board resistor divider drifts with heat, while the internal reference stays in specified limits. For motor protection this means stable trip current in heat and cold.

## 4. Emergency PWM Stop With No Core

Comparator output can feed the timer emergency stop input. Then current excess instantly drives PWM outputs into a safe state: switches close with no interrupt, no bus delay, no program involvement.

| Protection element | Role | Setting |
| --- | --- | --- |
| Shunt in motor loop | Millivolts proportional to current | Small inductance, near switches |
| Amplifier | Lifts millivolts to volts | Gain of eight or sixteen |
| Comparator | Compares against current threshold | Hysteresis against false trips |
| Timer stop input | Mutes PWM outputs | Active level and ring filter |
| Program | Only logs the fault | Reads the flag and counts events |

```text
Hardware motor protection path:
  Current --> [shunt] --millivolts--> [OPAMP x16] --volts--> [COMP threshold] --stop--> [TIM BKIN]
  PWM outputs go out in tens of nanoseconds.
  The core learns about the fault later, when handy, through the flag.
  The software path over ADC is hundreds of times slower here.
```

The filter on the stop input removes short switching spikes. Without a filter every switch edge would cause a false stop. With too long a filter protection lags. Start from tens of nanoseconds and tune with a scope.

After a stop trip the outputs stay muted until software deliberately unlocks them. This is correct: automatic restart under overload leads to rhythmic current hits and overheating.

## 5. Op-Amp Modes

The built-in amplifier can run as follower, as programmable-gain amplifier or as a standalone block with external resistors. Mode choice defines input range and accuracy.

| Mode | Circuit | Application |
| --- | --- | --- |
| Follower | Output to inverse input inside | Buffer for high-impedance sensor |
| Programmable gain | Internal matrix resistors | Current shunt with no external parts |
| External resistors | Classic board wiring | Precise gain, filtering |
| Comparator stage | Amplifier plus comparator | Small signals with fast threshold |

| Gain | Shunt input | Converter output |
| --- | --- | --- |
| Two | One hundred millivolts | Two hundred millivolts, large margin |
| Eight | One hundred millivolts | Eight hundred millivolts, scale middle |
| Sixteen | One hundred millivolts | One point six volts, good sensitivity |
| Thirty two | Fifty millivolts | One point six volts, small currents visible |

Programmable gain saves space: no need for precise resistors around the package. The internal matrix is already matched and switches with configuration bits. For series boards this removes several BOM lines.

## 6. Motor Current With No External Chips

A typical current chain has a shunt, amplifier and converter. The shunt gives tens of millivolts, the amplifier multiplies them to volts, the converter digitizes on timer trigger in the quiet PWM pulse middle.

```text
Current measurement in the low-side switch:
  Ground --[5 mOhm shunt]--+--> bridge --> motor
                            |
                       Ushunt = I * R (at 10 A gives fifty millivolts)
                            |
                       [OPAMP x16] --> eight hundred millivolts --> ADC on PWM trigger
  Traces to the amplifier run as a close pair, loop minimal.
  The filter goes after the amplifier, not before it.
```

Gain is picked so maximum current gives about two thirds of converter scale. Headroom is needed for start-up surges that must not drive the path into saturation. A saturated amplifier leaves limiting slowly and lies in later measurements.

The shunt goes in with small inductance and wide current traces. A narrow trace adds an inductive spike on every edge that later needs filtering. Better to route wide and short at once.

## 7. Self-Calibration and Accuracy

Amplifier and comparator input offset is units of millivolts. For a shunt signal of tens of millivolts this is a visible error. Self-calibration measures offset internally and stores the correction.

```c
void opamp_selfcal_ll(void)
{
    /* Калібрування обох входів перед роботою */
    LL_OPAMP_Enable(OPAMP1);
    LL_OPAMP_StartCalibration(OPAMP1, LL_OPAMP_MODE_FUNCTIONAL,
                              LL_OPAMP_INPUT_INVERT);
    while (LL_OPAMP_IsCalibrationOnGoing(OPAMP1) != 0UL)
    {
        /* Чекаємо завершення, ядро нікуди не поспішає */
    }
}
```

Calibration runs after supply settling and die warm-up. In precise products it repeats on large temperature change. Offset drifts with heat, so one calibration on a cold chip errs on a hot one.

Extra accuracy comes from converter averaging: random noise falls, systematic offset stays. So the order is: first offset calibration, then clean supply, then averaging.

## 8. Input Range Limits

Amplifier and comparator inputs work not from supply rail to rail. Near ground and near supply there are blind zones of tens or hundreds of millivolts depending on mode. The signal must stay inside the allowed window.

| Input mode | Allowed window | Consequence of leaving it |
| --- | --- | --- |
| Normal input | With margin from both rails | Saturation and false level |
| Near-ground input | Special low-voltage mode | Without it a shunt near zero lies |
| Near-supply input | Margin mandatory | Threshold near supply goes through divider |

The check is simple: sweep the input slowly from zero to supply and watch where the output stops tracking. Write limits into board notes and never place working points in blind zones again.

For a ground-side shunt pick a mode working from zero or add a small upward bias. Bias lifts current zero above the blind zone, software subtracts it as a digital zero.

## 9. Start Examples

A comparator starts over the abstraction layer in several calls: configure inputs and hysteresis, pick the reference, enable and start. Below is a start with edge interrupt for battery supervision.

```c
void comp_battery_start(COMP_HandleTypeDef *hcomp)
{
    /* Поріг від внутрішньої опори, гістерезис проти брязкоту */
    HAL_COMP_Init(hcomp);
    HAL_COMP_Start(hcomp);
}

void HAL_COMP_TriggerCallback(COMP_HandleTypeDef *hcomp)
{
    (void)hcomp;
    /* Напруга перетнула поріг: засвітити попередження або піти у сон */
}
```

A programmable-gain amplifier configures over the low-level driver with no extra structures. Below is a follower as sensor buffer and a gain option for a shunt.

```c
void opamp_modes_ll(void)
{
    /* Буфер для високоомного датчика */
    LL_OPAMP_SetMode(OPAMP1, LL_OPAMP_MODE_FOLLOWER);
    LL_OPAMP_Enable(OPAMP1);

    /* Варіант для шунта: коефіцієнт шістнадцять */
    /* LL_OPAMP_SetMode(OPAMP1, LL_OPAMP_MODE_FUNCTIONAL); */
    /* LL_OPAMP_SetPGAGain(OPAMP1, LL_OPAMP_GAIN_16); */
}
```

Both fragments are checked with a voltmeter: on a buffer the output repeats the input, on an amplifier the output equals input times gain. On mismatch look at supply, input range and calibration.

## 10. Mermaid: Chain Choice

```mermaid
flowchart TB
    Start[Signal small or threshold needed] --> Qsig[Signal needs gain]
    Qsig -- Yes -- Amp[Built-in amplifier]
    Qsig -- No -- Comp[Direct to comparator]
    Amp -- Gain picked --> Comp
    Comp -- Threshold needed -- Ref[Internal reference choice]
    Ref -- Reference stable --> Hyst[Hysteresis on]
    Hyst -- Edge clean --> Qfast[Reaction must be instant]
    Qfast -- Yes -- Bkin[Output to PWM emergency stop]
    Qfast -- No -- Irq[Interrupt or wake-up]
    Bkin --> Done[Scope check on edges]
    Irq --> Done
```

## Common Issues

| # | Issue | Why bad | Fix |
| --- | --- | --- | --- |
| 1 | Comparator with no hysteresis on noisy signal | Burst of false edges near threshold | Turn on hysteresis of several millivolts plus input filter |
| 2 | Motor protection over program and converter | Microsecond delay burns switches | Comparator output straight to timer stop input |
| 3 | Skipped offset self-calibration | Millivolt error on small shunt | Calibrate after warm-up and repeat on heating |
| 4 | Signal in blind zone near ground | Amplifier saturates, current zero lies | Zero-capable mode or small upward bias |
| 5 | Long spread traces from shunt | Loop picks up switching spikes | Route as short close pair, filter after amplifier |
| 6 | Automatic PWM restart after fault | Rhythmic current hits and overheating | Hold outputs muted until deliberate program unlock |

## Official Sources

- [STM32 comparator application guide (ST)](https://www.st.com/resource/en/application_note/an4071-comparator-usage-in-stm32-microcontrollers--stmicroelectronics.pdf) - references, hysteresis, timer link.
- [Op-amp description in STM32G4 (ST)](https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html) - modes, programmable gain, calibration.
- [Motor control and emergency stop input (ST)](https://www.st.com/en/applications/motor-control.html) - hardware protection over stop input with no core.

## See Also

- [[Home.en]]
- [[EN/01-Hardware/02-F3-F4.en|analog F3 and F4]]
- [[EN/01-Hardware/03-G0-G4.en|G4 analog]]
- [[09-Firmware/01-CubeIDE-CubeMX|CubeMX setup]]
- [[09-Firmware/02-HAL-LL|HAL and LL layers]]
- [[EN/06-Analog/01-ADC.en|measurement over ADC]]
- [[EN/06-Analog/02-DAC.en|generation over DAC]]
- [[EN/06-Analog/04-DFSDM.en|sigma-delta filter]]
