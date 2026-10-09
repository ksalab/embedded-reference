---
title: Lab Instruments - Multimeter, Oscilloscope, Logic Analyzer, PSU, Load, USB Tester
description: Without instruments ESP32 development is guesswork from logs; instruments answer questions; shows schematics, code and tables.
tags: [esp32, lab, instruments, multimeter, oscilloscope, logic-analyzer, psu, power, debug]
category: Lab
lang: en
original: ESP32-Reference/17-Lab/01-Instruments.md
date-created: 2026-09-28
date: 2026-10-08
---

# Lab 1 - Measurement Instruments: Multimeter, Oscilloscope, Analyzer, PSU, Load, USB Tester

![[assets/img/lab-instruments-scheme.png|600]]
*Fig. ESP32 lab stand: lab PSU -> USB tester -> DevKit, multimeter in power gap, oscilloscope on VIN, logic analyzer on buses.*

> [!warning] Safety first
> Lab PSU always starts with current limit (CC). First power-on of new board - through CC 100-200 mA. Short on ESP32 board smells hot AMS1117 - turn off in time.
>
> [!tip] Purpose
> This note is a map of lab instruments for ESP32 development and debugging: what to measure with what, how not to burn board with probe, and how to catch power sag during WiFi transmission.

## 1. Purpose

Without instruments ESP32 development is guesswork from logs. Instruments answer:

- how much the board really consumes in deep-sleep (microamps or milliamps?);
- why board reboots at WiFi start (VIN sag below brownout?);
- what really flows over I2C/SPI/UART (address, ACK, baud rate?);
- can LDO/buck handle peak 500 mA WiFi TX;
- does USB cable have data wires or only charge.

## 2. Multimeter Basics

| Measurement | Range / Mode | What it answers |
| --- | --- | --- |
| DC Voltage | 3.3V / 5V | LDO output, VIN sag |
| DC Current | 10 mA - 10 A | Sleep, active, peak |
| Resistance | Continuity | Short, open, pull-up |
| Diode | 0.3-0.7V | Protection diode direction |

```text
Safety rules:
  - Always turn off power before moving probes to resistance/continuity;
  - Use 10A fuse for current; never measure voltage in current mode;
  - Use thin sharp probes to reach module pins.
```

## 3. Oscilloscope: Catching Peaks

| Channel | What to measure | Trigger | Note |
| --- | --- | --- | --- |
| CH1 | VIN / 3.3V | Falling edge at 3.0V | Brownout detection |
| CH2 | USB-UART TX | Rising edge | Start bit, baud rate |
| CH3 | I2C SDA / SCL | I2C trigger | Address, ACK, clock |

- Use 10x probe to reduce loading.
- Set time base 1 ms/div for WiFi peaks.
- Capture mode to see peak current at TX.

## 4. Logic Analyzer

| Protocol | Rate | What to check | Software |
| --- | --- | --- | --- |
| I2C | 100-400 kHz | Address ACK, data | PulseView / Saleae |
| SPI | 1-10 MHz | CS toggle, MISO, clock | PulseView |
| UART | 115200 | Start/stop, data | PulseView / Arduino IDE |

- Always use 3.3V logic levels; 5V can damage ESP32.

## 5. Power Supply (PSU)

| Type | Volts / Amps | Use | Safety |
| --- | --- | --- | --- |
| Lab PSU | 5V / 2A CC | Main power | Always CC first |
| Buck module (LM2596) | 5V -> 3.3V | Remote load | Heat check |
| Battery (18650 / LiPo) | 3.7V / 2000 mAh | Portable | Protection circuit |

```text
First power-on procedure:
  1. Set PSU to 3.3V, CC 100 mA;
  2. Connect board, check current (should be <50 mA at idle);
  3. If >200 mA - disconnect, check shorts;
  4. Only then increase current limit to 1-2 A.
```

## 6. USB Tester and Current Measurement

- USB tester shows voltage, current, power in real time.
- Use multimeter in series to measure sleep current (cut USB-UART power for real sleep).
- INA219 module can log current over time.

## See Also

- [[EN/Home.en]]
- [[EN/17-Lab/02-Soldering-Connectors.en]]
- [[02-Power-Supply/01-Lancjugi-zhivlennya]]
- [[EN/99-Additions/01-Pinout-tablici.en]]

> UA original twin: [[17-Lab/01-Instruments.md | UA]]
