---
title: DFSDM - Sigma-Delta ADC and Microphones
description: Explains sigma-delta stream filter operation from digital microphones to isolated current measurement; shows schematics, code and tables.
tags: [stm32, dfsdm, sigma-delta, pdm, current]
category: Analog
lang: en
original: 06-Analog/04-DFSDM.md
date-created: 2026-10-01
date: 2026-10-09
---

# DFSDM - Sigma-Delta ADC and Microphones

![[assets/img/stm32-dfsdm-scheme.png|600]]
*Fig. Path diagram: modulator, digital filter, decimation and ready code into memory over DMA.*

> [!tip] Purpose of this note
> Explain when a plain successive approximation converter is not enough and a sigma-delta path is needed: direct digital microphone connection, precise current measurement over a shunt with galvanic isolation and a fast short-circuit detector.
> This note gives a choice map between fast rough measurement and slow precise one, plus a minimal filter setup order.

## 1. Purpose

The digital filter module for sigma-delta modulators takes a fast one-bit stream and turns it into precise multi-bit codes. Instead of one bit weighting, a pair works here: an external or internal modulator outputs pulse density, while the internal filter averages it into a code.

This note serves those who connect pulse-density modulation microphones, measure current through an isolated modulator or want twenty bits where a plain converter gives twelve. It explains where to find this module in the catalog, how to pick filter order and decimation ratio, how not to lose data over direct access and when staying on a plain converter is cheaper.

The main trade here is time against accuracy: the longer the filter accumulates the stream, the cleaner the result, but the slower the update. Sound takes fast update, current and temperature take deep averaging.

## 2. Where to Find the Module in Families

Not every chip has the module. It went into measurement and audio families where microphones and precise slow measurements are needed. Before board layout check module presence and channel count for the exact package.

| Family | Module presence | Typical tasks |
| --- | --- | --- |
| Measurement line with precise inputs | Present, several channels | Energy meters, scales, pressure sensors |
| Senior general-purpose with large memory | Present, many filters | Microphone arrays, active noise cancel |
| Low-power with small memory | Present in select models | Battery voice remotes |
| Basic small packages | Missing | Plain converter remains |

```text
Module presence in a project:
  Chip choice --> [filter present] --> microphones direct, precise current, fault detector
  Chip choice --> [no filter] --> plain ADC plus external codec on bus
  Check not the family in general but the exact part number and package.
  Small packages may not expose all channels.
```

Without the module a digital microphone connects over an external codec on the audio serial bus. This adds a chip but frees the core from filtering.

## 3. Pulse-Density Modulation in Simple Words

A digital microphone outputs not a code but a stream of ones and zeros at a megahertz clock. The louder the sound at the moment, the more ones in the stream. The filter counts one-density over a window and outputs an amplitude code.

| Term | Meaning | Example |
| --- | --- | --- |
| Density stream | Fast one bit at megahertz clock | Two megahertz from microphone |
| Modulator clock | Bit output rate | Set by microphone or timer |
| Averaging window | Bit count per code | Sixty four or one hundred twenty eight |
| Decimation | Stream thinning into codes | Sixteen kilohertz sound from megahertz |
| Output code | Multi-bit amplitude | Sixteen or twenty four bits |

```text
Density as loudness:
  Silence:     0101010101010101 (half ones)
  Quiet sound: 0110011001100110 (slightly more ones)
  Loud sound:  1110111011101110 (clearly more ones)
  The filter counts the one share over a window and outputs a code.
  A longer window gives a cleaner code but slower updates.
```

Two microphones can share one data line on clock edges: one outputs a bit on the rising edge, the other on the falling edge. This is a stereo pair on three wires: clock, data and power.

## 4. Filters and Decimation

The digital filter has an order and a decimation ratio. Order defines quantization noise rejection steepness, ratio defines how many input bits fold into one output code. Larger order gives a cleaner signal but longer delay.

| Filter parameter | Small | Large |
| --- | --- | --- |
| Third order | Short delay, moderate purity | Enough for voice and control |
| Fifth order | Long delay, high purity | For measurements and quality sound |
| Window of thirty two | Fast update, more noise | Tracking fast changes |
| Window of two hundred fifty six | Slow update, little noise | Precise current and temperature |

| Task | Order | Window | Code rate |
| --- | --- | --- | --- |
| Voice command | Third | Sixty four | Sixteen kilohertz |
| Sound record | Fifth | One hundred twenty eight | Sixteen kilohertz clean |
| Slow motor current | Fifth | Two hundred fifty six | Units of kilohertz precise |
| Temperature | Maximum | Maximum | Units of hertz very clean |

Reference formula: code rate equals stream rate divided by decimation ratio. At a two megahertz stream and a one hundred twenty eight window, codes run about fifteen point six kilohertz. Further thinning can be done in software.

## 5. Microphones Direct With No Codec

A digital microphone connects with two signals: clock and data. The clock comes from a timer or the module itself, data goes into the filter input. Microphone power comes from a low-noise regulator, otherwise supply noise becomes record noise.

```text
Stereo pair on three wires:
  Module --CLK--> [left microphone] --+
         --CLK--> [right microphone] -+--> DATA --> [filter 0] --> left code
                                     +--> [filter 1] --> right code
  Left outputs a bit on the rising edge, right on the falling edge.
  Supply capacitors go near every microphone.
  Keep the clock trace away from analog inputs.
```

| Element | Recommendation |
| --- | --- |
| Microphone clock | One or two megahertz per capsule datasheet |
| Data line | Short, terminated, with no stubs |
| Capsule supply | Separate resistor plus capacitor filter |
| Case | Hole exactly at acoustic port, no gaps |

Record check starts with silence: in a quiet room codes must show small RMS deviation. On large noise look at supply, flex length and clock. A long breadboard flex rings, which no filter removes.

## 6. Current Over Shunt With Isolation

An isolated current modulator places a galvanic barrier between power and logic. The power side runs from its own source, the bit stream crosses the barrier, the logic-side filter outputs the current code. A power stage breakdown does not burn control.

| Measurement element | Role | Choice |
| --- | --- | --- |
| Shunt in power loop | Millivolts proportional to current | Small value, small inductance |
| Isolated modulator | Bit stream over barrier | Isolation voltage with margin |
| Modulator clock | Stream sync | Ten or twenty megahertz |
| Filter | Current code for regulator | Order and window for loop speed |

```text
Isolated phase current measurement:
  Motor phase --[shunt]--> [modulator |barrier| stream] --> [filter] --> code --> regulator
  The left side is at high voltage, the right side at three volt logic.
  Board clearance and a slot under the isolation package are mandatory.
  A fast loop takes a short window, precise metering takes a long one.
```

Such measurement is cleaner than a direct divider because power interference does not cross the barrier. The price is filter delay: fast short protection uses a separate detector instead of waiting for a ready code.

## 7. Short-Circuit Detector

A separate stream comparator watches density without waiting for a full code. If the stream stays near the scale rail too long, current passed the safe limit. The detector signal can feed the timer emergency stop just like an analog comparator output.

| Setting | Meaning | Example |
| --- | --- | --- |
| Upper stream threshold | One-density as upward fault | Current surge on switch breakdown |
| Lower stream threshold | Zero-density as downward fault | Break or short to ground |
| Confirm time | How long to hold for trip | Cuts short switching spikes |
| Reaction | Interrupt or PWM stop | Mute switches with no core |

The detector is tuned so motor start surges do not touch it, while a true short mutes the switches. Start from a rough threshold and time, then narrow it down on the current scope.

## 8. Link With Direct Access

The filter outputs codes continuously, so a circular direct access buffer collects them. Half the buffer is processed while the other fills. Overflow means the program is too slow: lower the code rate or raise the channel priority.

```c
#define DFSDM_BUF_LEN 128U
static int32_t dfsdm_buf[DFSDM_BUF_LEN];

void dfsdm_start_stream(DFSDM_Filter_HandleTypeDef *hflt)
{
    /* Безперервний потік кодів у кільцевий буфер */
    HAL_DFSDM_FilterRegularStart_DMA(hflt, dfsdm_buf, DFSDM_BUF_LEN);
}

void HAL_DFSDM_FilterRegConvHalfCpltCallback(DFSDM_Filter_HandleTypeDef *hflt)
{
    (void)hflt;
    /* Перша половина готова: фільтрувати або писати у кільце звуку */
}

void HAL_DFSDM_FilterRegConvCpltCallback(DFSDM_Filter_HandleTypeDef *hflt)
{
    (void)hflt;
    /* Друга половина готова: обробити і повернутися */
}
```

| Access setting | Value | Why so |
| --- | --- | --- |
| Mode | Circular | Stream with no restarts |
| Word size | Thirty two bits | Filter code is wide |
| Alignment | Signed shift right | Sound sign preserved |
| Priority | High for sound | A miss gives a click |

For sound the codes go straight into a ring audio buffer with read and write indexes. For current the codes run straight through the regulator moving average. The main rule matches the plain converter: never read the half that the controller writes.

## 9. Setup Order Step by Step

First the clock starts and is checked with a scope: frequency and duty must match the microphone or modulator datasheet. Then the filter channel turns on with small order and small window to see at least some codes. Then order and window grow to the needed purity.

```c
void dfsdm_bringup_order(void)
{
    /* Порядок дій при першому старті: */
    /* 1. Перевірити такт потоку осцилографом. */
    /* 2. Увімкнути канал і фільтр з малим вікном. */
    /* 3. Подивитися коди у паузі: тиша дає середину шкали. */
    /* 4. Збільшити вікно до потрібної чистоти. */
    /* 5. Увімкнути кільцевий доступ і детектор аварії. */
}
```

Silence for a microphone must give a code near zero after DC removal. On drifting middle look at capsule supply and clock-to-data crosstalk. DC is removed with a digital high-pass filter, not by trimming hardware.

## 10. When a Plain Converter Suffices

A sigma-delta path is more complex and slower per code than successive approximation. For a simple task it is not needed.

| Task | Plain one suffices | Filter needed |
| --- | --- | --- |
| Volume knob, battery | Yes, twelve bits suffice | No |
| Current with no isolation | Yes, with shunt amplifier | No, if speed matters |
| Digital microphone | No, stream cannot be processed | Yes, direct connection |
| Isolated current | No, barrier needed | Yes, modulator with isolation |
| Scales and slow sensors | May suffice with averaging | Yes, if twenty bits needed |

| Criterion | Reference |
| --- | --- |
| Accuracy to twelve bits plus speed | Plain converter with trigger |
| Accuracy above sixteen bits or microphone | Filter with decimation |
| Power stage isolation | Only barrier modulator |
| Battery supply and simplicity | Plain converter with sleep between measurements |

Selection rule: start from the plain converter, move to the filter for only one of three reasons: a digital stream at the input, isolation needed or accuracy beyond its limits needed.

## 11. Mermaid: Path Choice

```mermaid
flowchart TB
    Start[Measurement or sound needed] --> Qmic[Input is a density stream]
    Qmic -- Yes -- Filt[Filter on]
    Qmic -- No -- Qiso[Isolation needed]
    Qiso -- Yes -- Filt
    Qiso -- No -- Qbit[Need more than sixteen bits]
    Qbit -- Yes -- Filt
    Qbit -- No -- Sar[Plain converter]
    Filt -- Order and window picked --> Dma[Circular access for codes]
    Dma -- Stream even --> Protect[Fault detector to PWM stop]
    Protect --> Done[Silence and start surge check]
    Sar --> DoneSar[Timer trigger and averaging]
```

## Common Issues

| # | Issue | Why bad | Fix |
| --- | --- | --- | --- |
| 1 | Wrong clock for microphone | Capsule silent or noisy | Set datasheet frequency and check with scope |
| 2 | Too long a window for a fast loop | Phase delay shakes the regulator | Short window for control, long one only for metering |
| 3 | Buffer read without half split | Torn data and clicks in sound | Process the ready half on interrupt |
| 4 | Shared dirty microphone supply | Supply noise becomes record noise | Separate supply filter near every capsule |
| 5 | Waiting for code to guard a short | Code arrives late, switches burn | Separate stream detector straight to timer stop |
| 6 | Filter picked for a plain knob | Complexity with no gain, slow response | Keep the plain converter for batteries and knobs |

## Official Sources

- [Sigma-delta filter application guide (ST)](https://www.st.com/resource/en/application_note/an4990-digital-filter-for-sigma-delta-modulators-dfsdm--stmicroelectronics.pdf) - filters, decimation, detector and access link.
- [Module description in STM32L4 reference guide (ST)](https://www.st.com/en/microcontrollers-microprocessors/stm32l476rg.html) - channels, order, interrupts and registers.
- [Density-modulation digital microphones (ST)](https://www.st.com/en/mems-and-sensors/digital-microphones.html) - clock, stereo pair, board layout.

## See Also

- [[Home.en]]
- [[EN/01-Hardware/02-F3-F4.en|analog F3 and F4]]
- [[09-Firmware/01-CubeIDE-CubeMX|CubeMX setup]]
- [[EN/04-Interfaces/02-SPI.en|SPI bus]]
- [[EN/04-Interfaces/03-I2C.en|I2C bus]]
- [[EN/06-Analog/01-ADC.en|measurement over ADC]]
- [[EN/06-Analog/02-DAC.en|generation over DAC]]
- [[EN/06-Analog/03-COMP-OPAMP.en|comparators and op-amps]]
