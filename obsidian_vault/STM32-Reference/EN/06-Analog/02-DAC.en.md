---
title: STM32 DAC - Waves Over DMA and Buffer
description: Explains STM32 DAC operation from output buffer to wave generation over DMA on timer trigger; shows schematics, code and tables.
tags: [stm32, dac, waveform, dma]
category: Analog
lang: en
original: 06-Analog/02-DAC.md
date-created: 2026-10-01
date: 2026-10-09
---

# STM32 DAC - Waves Over DMA and Buffer

![[assets/img/stm32-dac-scheme.png|600]]
*Fig. DAC diagram: code register, output buffer, timer trigger and sample stream over DMA.*

> [!tip] Purpose of this note
> Show how to get a true analog voltage without external chips: when to turn on the built-in buffer, how to push sine or saw over direct access on timer trigger, how to use built-in noise and triangle and what to do when the package has no converter.
> This note covers the path from a static level for sensor bias to continuous sound and test signal generation.

## 1. Purpose

A digital to analog converter turns a digital code into a voltage on a microcontroller pin. In classic families these are two twelve-bit channels with separate data registers and a shared trigger. One channel can hold a constant level while the second generates a wave at the same time.

This note serves where pulse-width modulation with a filter gives steps and delay: clean sine for sound, saw for sweep, arbitrary shape for path testing, precise bias for a sensor. It explains why voltage sags under load without a buffer, why steps are uneven without a trigger and how to compute the real wave frequency.

The case of a missing converter in the chip is covered separately. Many small packages lack it, so the choice between filtered modulation and an external chip on a serial bus depends on purity and speed demands.

## 2. Two Channels and Twelve Bits

Every channel has its own pin, register and enable. Data can be written as twelve bit right- or left-aligned, or as eight bit for fast tasks. Two channels can run independently or synchronously from one trigger.

| Parameter | Value in typical families | Consequence |
| --- | --- | --- |
| Channel count | Two independent | Static plus wave at once |
| Resolution | Twelve bit | Four thousand ninety six levels |
| Step at three volt reference | Under a millivolt | Smooth sound steps |
| Output range without buffer | From ground to reference | Full swing, but small current |
| Output range with buffer | With margin from rails | Smaller swing, but stability |
| Speed | About one million samples | Sound and fast sweeps are real |

```text
Two channels on one reference:
  Code A --> [DAC channel 1] --Uout1--> load or amplifier
  Code B --> [DAC channel 2] --Uout2--> sensor bias or second sound channel
  Reference is shared, so both channels depend on reference purity.
  Each channel buffer turns on separately.
```

Simultaneous start of two channels from one trigger gives a stereo pair with no time skew. Both channels switch to synchronous mode and a code pair is written in one access.

## 3. Output Buffer: When to Turn On

Output without a buffer is effectively a resistor matrix with large output impedance. It gives full swing from ground to reference but sags even under tens of kiloohms of load. Buffered output holds loads of several kiloohms and hundreds of picofarads, but loses tens of millivolts near scale rails.

| Output mode | Advantage | Limit |
| --- | --- | --- |
| No buffer, pin outside | Full rail-to-rail swing | Only for high-impedance load or follower |
| Buffered to pin | Holds current and capacitance | Offset from ground and reference, smaller swing |
| Internal with no pin | Bias for comparator and amplifier | Invisible outside, saves a pin |
| Through external follower | Best stability | Extra chip on board |

| Load | Recommendation |
| --- | --- |
| Op-amp input | Possible without buffer, impedance large |
| Ten kiloohm divider | Turn on buffer or add a follower |
| Headphones or speaker | Only through an external power amplifier |
| Long cable to instrument | Buffer plus series resistor of tens of ohms |

Practical rule: if pin voltage depends on the connected instrument, a buffer or external follower is missing. Measure with a voltmeter of large input impedance, otherwise the instrument itself becomes part of the divider.

## 4. Wave Over Direct Access on Trigger

A static level can be updated by software, but an even wave needs an even grid in time. A sample array in memory, circular direct access and a periodic timer trigger give exact frequency with no core jitter.

| Chain element | Role | Example |
| --- | --- | --- |
| Sample array | One wave period in codes | Sixty four sine points |
| Trigger timer | Even start pulses | Every ten microseconds |
| Direct access | Code move into register | Circular mode with no core |
| Converter trigger | Output update moment | Timer event or software |

```text
Sine generation chain:
  [array of 64 codes] --DMA--> [DAC register] --TIM6 trigger--> [output Uout] --> filter --> phones
  Wave frequency equals trigger frequency divided by point count.
  Example: one hundred kilohertz trigger and sixty four points give one and a half kilohertz.
```

Wave frequency is simple math: trigger frequency divided by array length. Frequency change without rewriting the array is done by changing the timer period. Amplitude change is done by scaling the array in memory.

| Wave | Array | Application |
| --- | --- | --- |
| Sine | Sine table per period | Sound, path test, modulation |
| Saw | Linear rise and reset | Sweep, linearity test |
| Square | Two levels per half period | Clocking, rough test |
| Arbitrary | Record from measurement or math | Sensor imitation, calibration |

## 5. Wave Start: Setup Step by Step

First the array in memory is prepared and checked statically: the middle code is written and half scale is measured with a voltmeter. Then the timer turns on with a slow period and steps are confirmed even. Only after that the working frequency is set.

```c
#define WAVE_LEN 64U
static uint16_t wave_sine[WAVE_LEN];

void dac_wave_fill(void)
{
    /* Заповнення одного періоду синуса на повну шкалу */
    for (uint32_t i = 0U; i < WAVE_LEN; i++)
    {
        /* Проста таблиця без бібліотеки: тут виклик обчислення синуса */
        wave_sine[i] = sine_table_12bit(i);
    }
}

void dac_wave_start(DAC_HandleTypeDef *hdac, TIM_HandleTypeDef *htim)
{
    HAL_DAC_Start_DMA(hdac, DAC_CHANNEL_1, (uint32_t *)wave_sine, WAVE_LEN, DAC_ALIGN_12B_R);
    HAL_TIM_Base_Start(htim);
}
```

The table fill function stands apart so it can be tested: minimum near zero, maximum near full scale, mean in the middle. If the table is wrong, no timer will fix it.

The beginner mistake is starting direct access without a running timer: the output hangs on the first sample and the converter looks broken. Always check both starts: first the channel with access, then the timer base.

## 6. Built-in Noise and Triangle

The hardware noise and triangle generator needs no array in memory. Pseudorandom noise suits filter checks and stability margin, while a programmable-amplitude triangle wave gives a sweep with no table.

| Built-in signal | Setting | Application |
| --- | --- | --- |
| Noise with bit mask | Mask defines amplitude | Filter check, spectrum spreading |
| Small triangle | Several least significant bits | Sensitivity test, dithering |
| Full-scale triangle | Whole twelve-bit scale | Scope sweep, linearity test |
| Constant level plus triangle | Offset by register | Comparator threshold check |

```text
Triangle with no array:
  Trigger --> [counter up] --> maximum --> [counter down] --> minimum --> repeat
  Amplitude is set by counter bit count.
  Core is free, memory is free, the wave runs by itself.
```

Noise does not repeat periodically in a short window, so it suits resonance hunting. Triangle is strictly periodic, so it suits path linearity measurement.

## 7. Offset Calibration

The output buffer has an initial offset of several millivolts. Calibration measures this offset internally and subtracts the correction. The procedure runs after power-up, before first output use.

```c
void dac_trim_once(DAC_HandleTypeDef *hdac, uint32_t channel)
{
    /* Калібрування зсуву буфера перед роботою */
    if (HAL_DACEx_SelfCalibrate(hdac, channel, 100000U) != HAL_OK)
    {
        Error_Handler();
    }
    HAL_DAC_Start(hdac, channel);
}
```

Without calibration a small signal near zero shows a step: first codes change no voltage because offset eats them. After calibration the curve starts smoother.

In precise products calibration repeats on die temperature change. Offset drifts with heat, so a periodic self-check pause pays off in zero stability.

## 8. Speed and Step Filtering

The converter updates the output about a million times per second. This means microsecond wave steps need smoothing with a plain resistor and capacitor, otherwise edges ring. Filter cutoff goes several times above wave frequency but below step frequency.

| Wave frequency | Step frequency at sixty four points | Output filter |
| --- | --- | --- |
| One kilohertz | Sixty four kilohertz | Cutoff near ten kilohertz |
| Ten kilohertz | Six hundred forty kilohertz | Cutoff near one hundred kilohertz |
| Static level | No steps | Only a capacitor against noise |

```text
Simple filter on output:
  DAC Uout --1k--+------------------> to load
                     |
                    10n
                     |
                   ground
  Cutoff near sixteen kilohertz: sine clean, steps smoothed.
  For a precise level take a film capacitor, not piezo ceramic.
```

A long trace from pin to filter picks up interference. The filter goes next to the microcontroller, and the smoothed signal travels further.

## 9. When the Package Has No Converter

Small packages often lack a built-in converter. Then two paths exist: filtered modulation or an external chip on a serial bus.

| Option | Advantage | Drawback |
| --- | --- | --- |
| Modulation with resistor and capacitor | Zero extra parts | Slow, noisy, loads the timer |
| External converter on bus | Precise, stable, multichannel | Needs a bus and driver |
| External follower on modulator | Faster than passive filter | Extra amplifier and supply |

```text
Built-in DAC replacement:
  Option A: TIM PWM --10k--+--100n-- ground --> Uout slow, cheap
  Option B: I2C bus --> [MCP4725] --> Uout precise, for bias and calibration
  Choice depends on speed: sound only through option B or a senior chip.
```

The bus link is described in serial interface notes. Eight bits of an external chip suffice for slow bias, sound takes twelve bits and a fast bus.

## 10. Low-Level Start Without Excess

The low-level driver gives direct access to trigger and register with no hidden states. Below is a minimal first-channel start with software trigger for a static level.

```c
void dac_static_ll(uint16_t code12)
{
    LL_DAC_Enable(DAC1, LL_DAC_CHANNEL_1);
    LL_DAC_SetTriggerSource(DAC1, LL_DAC_CHANNEL_1, LL_DAC_TRIG_SOFTWARE);
    LL_DAC_ConvertData12RightAligned(DAC1, LL_DAC_CHANNEL_1, code12);
    LL_DAC_TrigSWConversion(DAC1, LL_DAC_CHANNEL_1);
}
```

This fragment suits board check: write mid scale, measure half the reference with a voltmeter, write zero and maximum, check rails. If rails mismatch, look at buffer mode and load.

## 11. Mermaid: Solution Choice

```mermaid
flowchart TB
    Start[Analog voltage needed] --> Has[Converter present in chip]
    Has -- Present -- Static[Constant level needed]
    Has -- Missing -- Alt[Replacement choice]
    Static -- Yes -- Buf[Buffer setup for load]
    Static -- No -- Wave[Wave generation over DMA]
    Buf -- Load small --> Direct[Direct output with no buffer]
    Buf -- Load visible --> Buffered[Buffered output]
    Wave -- Table ready --> Trig[Timer trigger]
    Trig -- Grid even --> Filter[Step filter on output]
    Filter --> Done[Scope check]
    Alt -- Slow and cheap --> Pwm[Modulation with filter]
    Alt -- Precise and stable --> Ext[External chip on bus]
```

## Common Issues

| # | Issue | Why bad | Fix |
| --- | --- | --- | --- |
| 1 | Unbuffered output into several kiloohms of load | Voltage sags, scale compresses | Turn on buffer or add an external follower |
| 2 | Access start without timer start | Output hangs on first sample, no wave | Start the channel with access plus the timer base separately |
| 3 | Wrong wave frequency math | Wave sounds off pitch or tears | Divide trigger frequency by array length and check with scope |
| 4 | Skipped offset calibration | Step near zero, small codes dead | Run self-calibration before first start |
| 5 | No filter on fast wave | Steps and ringing on edges | Resistor with capacitor near pin, cutoff between wave and steps |
| 6 | Sound attempt over filtered modulation | Quantization noise and small range | Take a chip with converter or an external bus chip |

## Official Sources

- [STM32 DAC application guide (ST)](https://www.st.com/resource/en/application_note/an3126-audio-and-waveform-generation-using-the-dac-in-stm32-microcontrollers--stmicroelectronics.pdf) - wave generation, triggers, timer link.
- [DAC description in STM32G4 reference guide (ST)](https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html) - buffer, calibration, internal links.
- [External MCP4725 DAC for small chips (ST)](https://www.st.com/en/interfaces-and-transceivers/i2c.html) - when no built-in converter exists, bus choice.

## See Also

- [[Home.en]]
- [[EN/01-Hardware/02-F3-F4.en|analog F3 and F4]]
- [[09-Firmware/01-CubeIDE-CubeMX|CubeMX setup]]
- [[09-Firmware/02-HAL-LL|HAL and LL layers]]
- [[EN/04-Interfaces/03-I2C.en|I2C bus]]
- [[EN/06-Analog/01-ADC.en|measurement over ADC]]
- [[EN/06-Analog/03-COMP-OPAMP.en|comparators and op-amps]]
- [[EN/06-Analog/04-DFSDM.en|sigma-delta filter]]
