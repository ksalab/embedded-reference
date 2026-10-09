---
title: C5/C61 Robotics - DRV8833, Encoders, PID, ToF, IR Sensors
description: ESP32-C5/C61 robot with dual H-bridge, encoders, PID tuning, obstacle sensors; shows pinout, code and tables.
tags: [esp32, proekti, robotics, c5, c61, drv8833, pid, encoder, tof]
category: Proekti
lang: en
original: 16-Projects/06-C5-C61-Robotics.md
date-created: 2026-09-28
date: 2026-10-08
---

# Project 6 - C5/C61 Robotics: DRV8833 + Encoders + PID + ToF + IR

![[assets/img/cookbook-robotics-scheme.png|600]]
*Fig. Robot: ESP32-C5 brain + DRV8833 dual H-bridge + encoders + VL53L0X + IR sensors; C61 observer with BME280 + ToF.*

> [!tip] What we are building
> Two-node robot: C5 is brain (motors, PID, sensors); C61 is observer (BME280 + VL53L0X + ToF) and sends data to C5 over I2C/UART. Base: [[01-Hardware/10-ESP32-C5-C61 | C5/C61]], [[11-Vivid/04-L298N-TB6612-A4988-Buzzer.en | Drivers]].

## 1. Architecture

C5 = motor control + local decision; C61 = environment observer + telemetry.

## 2. BOM - components

| Component | Note | Note |
| --- | --- | --- |
| ESP32-C5 DevKit / SuperMini | [[01-Hardware/10-ESP32-C5-C61 | C5/C61]] | brain |
| ESP32-C61 MINI-1 | [[01-Hardware/10-ESP32-C5-C61 | C5/C61]] | observer |
| DRV8833 dual H-bridge | Official sources | 2× to 1.5 A, 3.3 V logic |
| 2 × DC motor 4.8-6 V with encoder | [[11-Vivid/04-L298N-TB6612-A4988-Buzzer.en | Drivers]] | ~300 rpm |
| 4×AA 6 V or 2S Li-ion 7.4 V | [[02-Power-Supply/01-Lancjugi-zhivlennya | Rails]] | motors only |
| 3.3 V LDO (ME6211, better than AMS1117) | [[02-Power-Supply/02-LDO-DC-DC | LDO]] | 6 V → 3.3 V |
| VL53L0X (I2C 0x29) | [[10-Sensors/10-VL53L0X-TCS34725-TSL2561 | ToF/Color]] | on C61 |
| BME280 (I2C 0x76) | [[10-Sensors/03-BME280-BMP280-SHT31.en | BME280]] | on C61 |
| 3 × IR line reflect sensor | [[06-Analog/01-ADC.en | ADC]] | line |
| Schottky diode + caps near VMOT | [[13-Power-Modules/04-LDO-Buck-XL4015-Protect.en | Protection]] | reverse current |

## 3. C5 Pinout

| C5 Pin | To | Note |
| --- | --- | --- |
| GPIO0 / GPIO1 | DRV8833 IN1 / IN2 | LEDC CH0 (motor A) |
| GPIO2 / GPIO3 | DRV8833 IN3 / IN4 | LEDC CH1 (motor B) |
| GPIO4 | ENA + ENB (together) | HIGH else bridges off |
| GPIO5…GPIO8 | encoder A/B, A/B | interrupt, quadrature ×4 |
| GPIO9…GPIO11 | IR ×3 | ADC1, 12 bit |
| GPIO12 | battery voltage /10 | ADC1, divider 100k/100k |
| 3V3 / GND | LDO output | ME6211 from 6 V battery |

## 4. C5 Working Code (Arduino core 3.3.x)

```cpp
#include <Arduino.h>
#include <ESP32Encoder.h>
#include <DRV8833.h>

ESPCounter encA(5, 6); ESPCounter encB(7, 8);
DRV8833 drv(0, 1, 2, 3, 4); // IN1..4 + EN
void setup() { drv.init(); encA.init(); encB.init(); }
void loop() { /* PID, read encoders, adjust PWM */ }
```

## 5. C61 Working Code

Observer sends `temp/pressure/dist` over I2C/UART to C5; C5 uses for obstacle avoidance and speed adjustment.

```cpp
#include <Wire.h>
#include <Adafruit_VL53L0X.h>
#include <Adafruit_BME280.h>

void loop() {
  float d = vl53.readRange();
  if (d < 10) sendObst();
}
```

## 6. PID: acceleration and tuning

| Step | What we do | Expected |
| --- | --- | --- |
| 1 | Wheel lifted, set 50 rpm | motor rotates ~50 rpm no load |
| 2 | Set Kp = 2, Ki = 0.5, Kd = 0.1 | stable within 5-10 s |
| 3 | Add load (battery or edge) | adjust Kp +20 %; Ki unchanged |
| 4 | Test full circle 1 m | deviation < 10 cm |

## 7. Troubleshooting

| Symptom | Where to look |
| --- | --- |
| Motor heats > 60 °C | DRV8833 current limit, Schottky diode missing | 
| Encoder counts wrong | quadrature wiring jitter, pull-ups 10k | 
| Robot circles, not straight | encoder calibration different, adjust Kp per side | 
| ToF returns 0 | I2C address 0x29, object < 10 mm | 

## 8. Official sources

- [DRV8833 - TI](https://www.ti.com/product/DRV8833) - dual H-bridge, 3.3 V logic.
- [ESP32-C5 - Espressif](https://www.espressif.com/en/products/socs/esp32-c5) - 160 MHz, RISC-V.
- [VL53L0X - ST](https://www.st.com/en/imaging-and-photonics-solutions/proximity-sensors/vl53l0x.html) - ToF I2C.

## See also

- [[EN/Home.en]]
- [[01-Hardware/10-ESP32-C5-C61.en | C5/C61]]
- [[16-Projects/01-Weather-Station.en | Weather Station]]
- [[16-Projects/03-Access-Control.en | Access Control]]

## Appendix: Energy budget (6 V battery, 2 motors, 30 min run)

| Mode | Current | Time | Charge |
| --- | --- | --- | --- |
| Idle (C5 + C61) | ~40 mA | 30 min | 20 mAh |
| Motors 50% PWM | ~800 mA | 10 min | 133 mAh |
| Total per session | - | 30 min | ~153 mAh |
| 4×AA (2000 mAh) | - | - | ~13 sessions |

## Extended notes

PID tuning guidelines: start with Kp = 2, Ki = 0.5, Kd = 0.1; increase Kp until oscillation begins then back off 30 %; Ki removes steady-state error for constant speed; Kd dampens overshoot but amplifies noise - keep low if encoder resolution is 4× quadrature; use filter on encoder input to avoid jitter.

Encoder wiring: twist pairs; pull-ups 10k to 3.3 V; do not run encoder wires parallel to motor power wires to avoid EMI; shield with aluminum tape if needed.

Motor selection: 300 rpm no-load, 4.8-6 V, stall current ~2 A; DRV8833 handles 1.5 A per bridge continuously; if stall > 2 A, add current limit via DRV8833 internal sense or external 0.1 Ω resistor; always include 100 nF + 10 µF near VMOT.

Safety: add physical kill switch; 6 V battery should have fuse 2 A; never leave robot running unattended without low-battery cutoff (GPIO12 ADC check); use Schottky SS34 for reverse protection on motor supply.

## More code details

```cpp
#include <Arduino.h>
#include <ESP32Encoder.h>

ESP32Encoder encA(5, 6);
void setup() { encA.clear(); encA.attachHalfQuad(5, 6); }
void loop() {
  int32_t pos = encA.getFullQuadCount();
  float rpm = pos * 60.0 / 400.0 / 0.1; // 400 ticks/rev, 0.1 s
}
```

## Calibration table

| Mode | PWM % | Speed rpm | Current mA | Battery V | Note |
| --- | --- | --- | --- | --- | --- |
| Slow | 30 | 90 | 120 | 6.0 | indoor floor |
| Normal | 50 | 150 | 300 | 5.8 | carpet / tile |
| Fast | 70 | 210 | 500 | 5.5 | open ground |
| Stall | 100 | 0 | 2000 | 5.2 | fatigue test |

## Hardware protection table

| Component | Value | Placement | Purpose |
| --- | --- | --- | --- |
| Schottky SS34 | 3 A | VMOT rail | reverse current from motor inductive spike |
| Cap 100 nF | 50 V | DRV8833 VMOT pin | high-frequency decoupling |
| Cap 10 µF | 25 V | motor terminals | bulk storage for PWM peaks |
| Fuse 2 A | 250 V | battery + | overcurrent protection |
| LDO ME6211 | 3.3 V 500 mA | C5 VCC | clean logic supply |

## Communication between nodes

C5 and C61 connect via UART (GPIO17/18) at 115200 baud; protocol: JSON line with `{"t":"env","temp":22,"dist":120,"rssi":-65}"; C61 sends every 200 ms; C5 parses in non-blocking loop; if UART error > 3 in 1 s, drop observer for 5 s.
