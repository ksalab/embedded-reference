---
description: Buttons, switches, pots: tactile buttons, rocker switches, potentiometers 10k/50k, rotary encoders, slide switches. Applications: user input, control.
title: Buttons Switches Pots
tags: [esp32, sensor, button, switch, potentiometer, encoder]
category: Sensori
lang: en
original: 10-Sensors/34-Buttons-Switches-Pots.md
date-created: 2026-09-27
date: 2026-10-08
---

# Buttons Switches Pots

## Purpose

Basic input devices: tactile buttons, rocker switches, potentiometers (10k, 50k, linear/log), rotary encoders, slide switches. Applications: user control, settings.

## Characteristics

| Component | Type | Note |
| --- | --- | --- |
| Tactile button | Digital | Pull-up, debounce 1-2 ms |
| Potentiometer | Analog 10k | 0-3.3 V, linear/log |
| Encoder | Quadrature A/B | Count direction |

## Common issues

| No. | Error | Symptom | Solution |
| --- | --- | --- | --- |
| 1 | Button bounce | Multiple presses | Software debounce 10-20 ms |
| 2 | Pot noisy | Jumping ADC | Average 10 samples; add 100 nF cap |

## See also

- [[EN/03-GPIO/01-GPIO-Overview.en]]
