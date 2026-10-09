---
date-created: 2026-09-27
date: 2026-10-08
description: Covers Li-Ion batteries, TP4056 charging, NTC control and solar power for ESP32; shows schematics, code and tables.
category: Zhivlennya
title: Batteries and TP4056 for ESP32
tags: [batteries, tp4056, 18650, lipo, solar, dw01, power]
aliases: [Batteries TP4056, ESP32 Battery]
lang: en
original: 02-Power-Supply/04-Akumulyatori-TP4056.md
---

# Batteries and TP4056

![[assets/img/placeholder.png]]

> [!warning] ESP32 takes only 3.3V, not 4.2V!
> A fully charged LiPo is 4.2V, too much for ESP32 (**3.3V**, 3.6V max). Always put an LDO or buck between the battery and the ESP32.

## Purpose

Batteries and TP4056 - chain; ESP32+TP4056+buck schematic; ESP32-to-module wiring table. A fully charged LiPo is 4.2V, too much for ESP32 (3.3V, 3.6V max). Always put an LDO or buck between the battery and the ESP32. TP4056 without NTC does not know the battery temperature. Add monitoring yourself - otherwise charging at low/high temperature kills the battery.

## Chain

| Node | Voltage | Note |
| --- | --- | --- |
| 18650 / LiPo | 3.0-4.2V | 3.7V nominal |
| TP4056 OUT | 3.0-4.2V | Charge + DW01 protection |
| Buck/LDO | **3.3V** | Only then to ESP32 |
| ESP32 3V3 | **3.3V** | 500 mA WiFi peak |

> [!danger] Why not power from the TP4056 5V pin without an LDO
> On TP4056 boards the OUT pin is NOT stable 5V and NOT **3.3V**, it is the raw battery voltage 3.0-4.2V plus droops. Without a regulator you get reboots and flash death. A buck/LDO to **3.3V** is mandatory. See [[EN/02-Power-Supply/01-Power-Rails.en]], [[EN/02-LDO-DC-DC.en]].

## ESP32+TP4056+buck schematic

| Connection | Where |
| --- | --- |
| B+ / B- TP4056 | 18650 battery |
| OUT+ TP4056 | Buck IN+ |
| OUT- TP4056 | Buck GND + ESP32 GND |
| Buck OUT 3.3V | ESP32 3V3 (exactly **3.3V**) |
| Solar 5-6V | TP4056 IN+ (via diode) |

> [!tip] Solar
> A 5V 1-2 W panel via a Schottky diode to TP4056 IN. Set the charge current with the Rprog resistor (1.2 kOhm = 1A, 0.5A is better for 18650). Compute node consumption per [[EN/03-Power-Consumption.en]]. The battery-monitor divider goes to ADC at 0-3.3V only, see [[EN/03-GPIO/01-GPIO-oglyad.en]].

## ESP32 to module wiring table

| ESP32 | Module | Description |
| --- | --- | --- |
| 3V3 | Module buck OUT | Stable **3.3V** from the battery |
| GND | Module TP4056 OUT- | Common ground |
| GPIO34 | Module battery divider | 100k/100k, 3.3V max at ADC |
| EN | Module RC | 10 kOhm to 3.3V |
| GPIO22/21 | Module INA219 | 3.3V current monitoring |

## Capacity vs reality (the 0.2C rule)

The "3000 mAh" label on a battery holds at a 0.2C discharge (600 mA for 3000 mAh) down to 3.0V at 25C. ESP32 with WiFi-TX gives 500 mA pulses + cold + an old battery = minus 30-50%.

| Condition | Real yield of nominal | Explanation |
| --- | --- | --- |
| 0.2C discharge, 25C, new | 95-100% | Datasheet reference |
| 0.5-1C pulses (WiFi-TX) | 80-90% | Internal resistance eats voltage |
| Cold +5C | 80% | Chemistry slows down |
| Cold -10C | 50-60% | + copper dendrite risk when charging! |
| Heat +45C | 95%, but aging x2 | Calendar aging accelerates |
| 300 cycles / 2 years | 70-80% | Capacity melts away even on the shelf |
| NoName "9900 mAh" 18650 | 800-1200 mAh real | Physics: more than 3500 mAh in an 18650 is impossible! |
| 21700 (18650 successor) | 4000-5000 mAh, same Li-ion | Higher current and lifespan; holder fits 21700 only, will not fit an 18650 bay |

Runtime calculation with derating:

```text
T = Cном × k_реаль × k_темп × k_вік / Iсер

Приклад: 18650 2600 мАг, Iсер 50 мА (сенсор + modem-sleep), вулиця +5°C, акуму 1 рік:
T = 2600 × 0.85 × 0.8 × 0.9 / 50 ≈ 32 год.
Той самий вузол в кімнаті з новим акумом: 2600 × 1.0 / 50 = 52 год.
Різниця ×1.6 — закладай у ТЗ одразу!
```

> [!warning] Pulsing load and DW01 protection
> The protection board cuts the battery at ~2.4-3.0V (depending on the DW01 clone). A 500 mA TX pulse on a low battery briefly sags voltage below the threshold, so protection cuts power - an eternal "boot-reboot" loop. Cure: a fresh battery + 470 uF on 3.3V + a higher deep-sleep threshold (sleep at 3.4V, not 3.1V).

## Self-discharge

| Chemistry | Self-discharge | Consequence for an ESP node |
| --- | --- | --- |
| Li-ion 18650 (protected) | 2-5% / month + protection board ~10 uA | After half a year on the shelf -30%. Recharge before the season! |
| LiPo pack | 3-8% / month | Soft pack + self-discharge = check swelling every season |
| LiFePO4 | 1-3% / month | Best for outdoors, but 3.2V nominal - check LDO dropout! |
| NiMH | 15-30% / month | Not for ESP at all |

## NTC thermal control (10 kOhm B=3950)

TP4056 without NTC does not know the battery temperature. Add monitoring yourself - otherwise charging at low/high temperature kills the battery.

| Schematic | Connection | Thresholds |
| --- | --- | --- |
| NTC 10k to the battery (thermal paste/tape) + 10k divider to 3.3V | Divider middle to GPIO34 (ADC, 0-3.3V!) | R/R25 to temperature via the B-equation |
| Fail threshold | ADC < 0.3V or > 3.0V | Sensor open/short - forbid charging! |

```cpp
// NTC-контроль перед дозволом заряду (Arduino)
#define NTC_PIN 34
float ntc_temp() {
  int raw = analogRead(NTC_PIN);                 // 0–4095
  float v = raw * 3.3 / 4095.0;
  float r = 10000.0 * v / (3.3 - v);             // верхнє плече 10к до 3.3V
  float t = 1.0 / (1.0/298.15 + log(r/10000.0)/3950.0) - 273.15;
  return t;
}
bool charge_allowed() {
  float t = ntc_temp();
  return (t > 0.5 && t < 45.0);  // вікно заряду, див. нижче
}
void loop() {
  if (!charge_allowed()) {
    // Вимкни key заряду (MOSFET на IN+ TP4056) + спи до потепління
    Serial.printf("T=%.1f C — заряд ЗАБОРОНЕНО\n", ntc_temp());
  }
  delay(5000);
}
```

ADC and levels: [[06-Analog/01-ADC.en | ADC]], [[EN/03-GPIO/03-Pidtyaguvannya-rivni.en]].

## Charging in frost is FORBIDDEN + heat

| Battery temperature | Charge | Discharge | Why |
| --- | --- | --- | --- |
| < 0C | FORBIDDEN (lithium plates as metal, dendrites, short) | Allowed, but capacity -20 to -50% | Bring into warmth or heat the box |
| 0 to +5C | Only 0.1C and supervised | Allowed | Better to wait for warmth |
| +5 to +45C | Normal (0.5C for 18650, 1C max) | Normal | Standard window |
| > +45C | Stop (degradation x2-4) | Reduce load | Shade/ventilation |
| > +60C | Emergency (unsealing risk) | Switch off | Move to shade, do not pour cold water on it! |

> [!danger] Outdoor solar node in winter
> A panel in winter gives current, so TP4056 charges an icy battery, and by spring the battery is swollen/dead. Fix: an NTC switch breaks TP4056 IN+ at T<+2C (hysteresis 2-5C), the node lives off the battery and waits for warmth. Solar details: [[EN/13-Power-Modules/01-Buck-Boost-Solar.en]], [[EN/13-Power-Modules/03-TP4056-IP5306-BMS-UPS.en]].

## Parallel connection: conditions

| Rule | Value | Why |
| --- | --- | --- |
| Only identical cells (model, age, capacity ±5%) | E.g. 2x new Samsung 26H | Different ones - the strong charges the weak with high current |
| Before connecting - equalize voltage to ±0.05V | Charge both to 4.15V separately | Otherwise sparks and 5-10 A current at soldering time! |
| Each battery with its own DW01 protection | Or a shared 2S/2P BMS | One bare battery in parallel = fire risk |
| Wires of equal length/gauge | < 5% resistance difference | Otherwise one works for both |
| Thermal control on each pack | NTC on each | One hot - switch the whole block off |
| Series (2S 7.4V) - only with balancing BMS | Never without BMS! | Without balancing one overcharges to 4.5V and ignites |

```text
Правильна паралель 2×18650 для ESP-вузла:
[18650 #1 + DW01] ─┬─► OUT+ ──► buck/LDO ──► 3V3 ESP32
[18650 #2 + DW01] ─┘      (зʼєднання ПІСЛЯ плат захисту, не до банок!)
                   └─► OUT- ──► GND (зірка!)
Ємність подвоюється (5200 мАг), струм ділиться навпіл → менше просадок TX.
```

Battery-monitor divider (0-3.3V to ADC!): two 100k R, middle to GPIO34, 100nF in parallel with the lower one. Switch via MOSFET, otherwise +16 uA around the clock. Sleep modes to save power: [[EN/07-Timers/03-Sleep-ULP.en]], current measurement: [[EN/03-Power-Consumption.en]].

### Mermaid: battery choice

```mermaid
flowchart TB
    Q[Autonomy] --> CAP{How many mAh/day?}
    CAP -->|Up to 500| S1[1x18650 2600 + TP4056]
    CAP -->|Up to 2000| S2[2P 18650 + BMS 1S]
    CAP -->|Solar| SOL[18650 + CN3791 MPPT + 5V panel]
    S1 --> PROT{Protection present?}
    PROT -->|No (bare cell)| DW[DW01+FS8205 mandatory!]
```

## Common issues

| # | Mistake | Why it is bad | Correct |
| --- | --- | --- | --- |
| 1 | Charging Li-Ion in frost | Lithium plating, degradation/fire | Charge only at 0 to +45C (NTC!) |
| 2 | Bare cell without BMS | Overdischarge/short | DW01 + MOSFETs or a protected cell |
| 3 | Parallel different cells | Cross-currents, fire | Same capacity/age/charge |
| 4 | TP4056 without current tuning | 1A into a small cell | Rprog for the capacity (0.2-0.5C) |

## Official sources

- [TP4056 datasheet](https://dlnmh9ip6v2uc.cloudfront.net/datasheets/Prototyping/TP4056.pdf) - current, NTC, cycles.
- [Battery University - Li-Ion charging](https://batteryuniversity.com/article/bu-409-charging-lithium-ion) - CC/CV, temperatures.

## See also

- [[EN/Home.en]]
- [[EN/00-Start/03-Chip-Comparison.en]]
- [[EN/03-GPIO/01-GPIO-oglyad.en]]
- [[EN/03-GPIO/02-Strapping-pini.en]]
- [[EN/02-Power-Supply/01-Power-Rails.en]]
- [[EN/02-LDO-DC-DC.en]]
- [[EN/03-Power-Consumption.en]]
- [[EN/01-Hardware/01-ESP32-Classic.en]]
