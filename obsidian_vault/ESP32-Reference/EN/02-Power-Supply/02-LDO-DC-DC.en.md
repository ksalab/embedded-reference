---
date-created: 2026-09-27
date: 2026-10-08
description: Compares LDO and buck regulators for ESP32, thermal design and LC ripple filters; shows schematics, code and tables.
category: Zhivlennya
title: LDO vs DC-DC for ESP32
tags: [ldo, dc-dc, ams1117, me6211, buck, power]
aliases: [LDO DC-DC, ESP32 Regulators]
lang: en
original: 02-Power-Supply/02-LDO-DC-DC.md
---

# LDO vs DC-DC for ESP32

![[assets/img/placeholder.png]]

> [!warning] Output is always 3.3V!
> Regardless of the input (5V, 12V, 4.2V LiPo) the regulator output for ESP32 is **3.3V**. Anything above 3.6V kills the chip.

## Purpose

LDO vs DC-DC for ESP32 - comparison; LDO-to-buck replacement schematic; ESP32-to-module wiring table. A typical buck (MP1584, LM2596) at 1 MHz gives 30-100 mV sawtooth at the output. Fine for digital, dirt for ADC/RF. MCP1700 Datasheet (Microchip): <https://www.microchip.com/en-us/product/MCP1700> - 250 mA LDO.

## Comparison

| Chip | Type | Current | Dropout / Efficiency | Heating |
| --- | --- | --- | --- | --- |
| AMS1117-3.3 | LDO | 800 mA | Dropout 1.1V, low efficiency | Heats up from 5V |
| ME6211-3.3 | LDO | 500 mA | Dropout 0.1V, small Iq | Cool, good for batteries |
| MP1584 / buck | Buck | 3 A | Efficiency 85-92% | Barely warm |
| HT7333 | LDO | 250 mA | Not enough for WiFi | Only for C3 without WiFi TX |

> [!danger] AMS1117 + 12V = an iron
> At (12V-3.3V)*0.3A = 2.6 W the AMS1117 overheats and hits thermal shutdown - the ESP32 hangs. From 12V use only a buck set to **3.3V**. See [[EN/02-Power-Supply/01-Power-Rails.en]].

## LDO-to-buck replacement schematic

| Step | Action |
| --- | --- |
| 1 | Desolder/bypass the AMS1117 |
| 2 | Buck input - to VIN 5-12V |
| 3 | Buck output - set **3.3V** with a multimeter WITHOUT the ESP32 |
| 4 | Buck output - to the board 3.3V rail + 100 nF + 10 uF |
| 5 | Common GND is mandatory |

> [!tip] Check without the module
> Always turn the buck trimmer with the ESP32 disconnected, set exactly **3.3V**, only then connect it. Otherwise 5V kills the GPIO. Monitor consumption: [[EN/03-Power-Consumption.en]].

## ESP32 to module wiring table

| ESP32 | Module | Description |
| --- | --- | --- |
| VIN | Module buck IN+ | 5-12V input |
| 3V3 | Module buck OUT+ | **3.3V** output to ESP32 |
| GND | Module buck GND | Common ground |
| GPIO34 | Module divider | Battery monitoring 0-3.3V |
| EN | Module RC | Pull-up to 3.3V |

## Thermal calculation: P = (Vin - Vout) x I

All voltage difference on an LDO turns into heat. One formula - different consequences depending on the package.

```text
P = (Vin − Vout) × I + Vin × Iq   (≈ другим доданком нехтують, Iq ~ мкА–мА)

Приклад 1 (DevKit від USB): (5.0 − 3.3) × 0.25 А = 0.43 Вт → теплий, житиме.
Приклад 2 (від 12V):        (12 − 3.3) × 0.30 А = 2.61 Вт → ПРАСКА, піде в protection!
Приклад 3 (LiPo 4.2V):      (4.2 − 3.3) × 0.20 А = 0.18 Вт → холодний.

Перегрів: Tj = Ta + P × RθJA. protection спрацьовує при Tj ≈ 150–165°C.
```

### Package limits (no heatsink, Ta=25C)

| Package | RthJA typ. | Max P without heatsink* | Verdict for ESP32 |
| --- | --- | --- | --- |
| SOT-23 (ME6211, HT7333) | ~220 C/W | ~0.4 W | From 5V: 0.43 W - borderline! Only C3/H2 or light TX |
| SOT-89 | ~150 C/W | ~0.6 W | From 5V average WiFi - ok, 500 mA peak - hot |
| SOT-223 (AMS1117) | ~90 C/W | ~1.0 W | From 5V - ok; from 12V (2.6 W) - death |
| TO-220 (AMS1117) no heatsink | ~60 C/W | ~1.5 W | From 12V - still hot, needs a heatsink |
| TO-220 + 10 C/W heatsink | ~12 C/W | ~8 W | From 12V it survives, but a buck is cheaper and cooler |

`*` Up to Tj approx 125C with margin to shutdown. In an enclosure +20C to Ta - halve the limit!

```text
Швидка перевірка пальцем (грубо, але працює):
- Холодний/ледь теплий (<40°C) — ок.
- Гарячий, але тримаєш 5 с (~60°C) — межа, міряй мультиметром з термопарою.
- Не втримати (>70°C) — або знижуй Vin (buck перед LDO), або став buck замість LDO.
Падіння 3.3V на осцилографі синхронно з нагрівом = термозахист LDO клацає!
```

## LDO dropout table (minimum Vin - Vout headroom)

| LDO | Dropout at 300-500 mA | Min Vin for 3.3V | Iq (own draw) | Max I | Verdict for ESP32 |
| --- | --- | --- | --- | --- | --- |
| AMS1117-3.3 | 1.1V | 4.4V+ | ~5 mA (kills the battery!) | 800 mA | DevKit from USB - ok; batteries - NO |
| ME6211C33 | 0.1-0.25V | 3.5V | ~40 uA | 500 mA | King of battery nodes |
| HT7333 | 0.09V | 3.4V | ~4 uA | 250 mA | Only C3/H2 without WiFi-TX! |
| MCP1700-3.3 | 0.18V | 3.5V | ~1.6 uA | 250 mA | Beacons, deep-sleep nodes |
| AP2112-3.3 | 0.25V | 3.6V | ~55 uA | 600 mA | Good compromise, DevKit-grade |
| XC6206-3.3 | 0.2V | 3.5V | ~1 uA | 250 mA | Sleepy nodes only |

> [!danger] HT7333 + WiFi-TX = reboot
> The 250 mA limit, while the TX peak is 500 mA. It will work "now and then" and torment you for months. Guideline: LDO of at least 500 mA for Classic/S3, 300 mA for C3. Mode consumption: [[EN/03-Power-Consumption.en]].

```cpp
// Перевірка dropout наживо: міряй Vin LDO при пія TX
// Якщо (Vin − 3.3V) < dropout з таблиці → LDO виходить з регулювання → просадка!
// Лікування: підніми вхід (заряджена батарея) або міняй LDO на low-dropout.
```

## Buck ripple and the LC filter

A typical buck (MP1584, LM2596) at 1 MHz gives 30-100 mV sawtooth at the output. Fine for digital, dirt for ADC/RF.

| Ripple source | Frequency | Typical amplitude | Suppressed by |
| --- | --- | --- | --- |
| Buck switching | 300 kHz-1.5 MHz | 30-100 mV | LC filter + ceramic |
| Diode/inductor ringing | 10-50 MHz | 10-30 mV | 100nF near the load + short GND |
| WiFi-TX load | 100 Hz-10 kHz envelope | Up to 300 mV without C | 470 uF (see [[EN/02-Power-Supply/01-Power-Rails.en]]) |
| USB 50 Hz hum | 50/100 Hz | 5-20 mV | Bigger input electrolytic |

LC filter after the buck (cuts the switching noise):

```text
buck OUT ──[L 2.2–10uH]──┬──► 3V3 чисті ──► ESP32
                         │
                        [C 22uF кераміка X7R]
                         │
                        GND (коротко, широким полігоном!)

Розрахунок зрізу: fc = 1 / (2π√(LC))
L=4.7uH, C=22uF → fc ≈ 15.6 кГц (комутація 1 МГц давиться у ~40 дБ ≈ ×100).
Струм індуктивності: Isat ≥ 1.5 × Iпік (для 500 мА бери ≥1 А, DCR < 0.1 Ом).
Феритовий намистин (альтернатива): 600 Ом @100 МГц послідовно + 10uF на землю.
```

| Buck module | Ripple out of the box | After LC | ADC noise | Verdict |
| --- | --- | --- | --- | --- |
| MP1584 Chinese | ~80 mV | ~5 mV | Clean | Add LC for analog nodes |
| LM2596 (150 kHz) | ~120 mV | ~10 mV | Tolerable | Old, heats up, MP1584 is better |
| XL4015 (180 kHz) | ~100 mV | ~8 mV | Tolerable | For P4 with camera - ok with LC |
| No-name "3A" | up to 200 mV + ringing | Measure! | Dirt | Check with oscilloscope before connecting ESP |

> [!tip] Two stages for perfection
> A dirty trick for precise measurements: buck 5V to 4.0V, then a low-noise LDO (ME6211/AP2112) 4.0 to 3.3V. The buck gives efficiency, the LDO eats the ripple. LDO losses are small: (4.0-3.3)x0.2 A = 0.14 W. Power modules: [[EN/13-Power-Modules/04-LDO-Buck-XL4015-Protect.en]], [[EN/13-Power-Modules/01-Buck-Boost-Solar.en]].

### Mermaid: LDO or buck

```mermaid
flowchart TB
    Q[3.3V supply] --> DROP{Vin-Vout headroom?}
    DROP -->|Small (<0.5V), current <500 mA| LDO[ME6211/LDO: quiet, simple]
    DROP -->|Large or current >500 mA| BUCK[Buck: efficient, cool]
    LDO --> HEAT{Heating up?}
    HEAT -->|P=(Vin-Vout)*I > 0.5 W| TOBUCK[Switch to buck!]
    BUCK --> RIPPLE{Ripple in ADC?}
    RIPPLE -->|Yes| LC[LC filter + ferrite]
```

### Buck-boost TPS63020 / SEPIC: 1S to 3.3V across the whole discharge

| Option | Input range | Efficiency | When |
| --- | --- | --- | --- |
| Buck + LDO cascade | 4.2 to 3.0V useful (below - dropout!) | ~80% | Cheap, simple |
| TPS63020 (buck-boost) | 1.8-5.5V to stable 3.3V | ~90% | 1S Li-Ion to the end (down to 2.8V!) |
| SEPIC (2 coils) | Wide, with input/output DC isolation | ~85% | Unstable sources (wind/solar without battery) |

```text
Коли треба: вузол має жити до 2.8V банки (а не до 3.5V dropout звичайного LDO) —
виграш +20–30% ємності. Ціна: котушка + розводка ВЧ (див. 17-Lab/04!).
```

## Common issues

| # | Mistake | Why it is bad | Correct |
| --- | --- | --- | --- |
| 1 | AMS1117 from 12V at 1A | 9 W of heat - smoke | Buck from 12V |
| 2 | LDO without dropout headroom | Droop on peaks | 0.3-0.5V margin above dropout |
| 3 | Buck without LC on an ADC board | Noise in measurements | Ferrite + LC, analog separate |
| 4 | Trim set without load | Drift under current | Set at 50% current |

## Official sources

- [ME6211 / AMS1117 datasheets](https://github.com/Edragon/Datasheet/blob/master/Microne/ME6211.pdf) - dropout, thermal.
- [MP1584 / SY8113 datasheets](https://www.monolithicpower.com/en/mp1584.html) - buck calculation.

- TPS63020 Datasheet (TI): <https://www.ti.com/product/TPS63020> - buck-boost 1.8-5.5V.
- TPS3823 Datasheet (TI): <https://www.ti.com/product/TPS3823> - voltage supervisor + WDT.
- MCP1700 Datasheet (Microchip): <https://www.microchip.com/en-us/product/MCP1700> - 250 mA LDO.

## See also

- [[EN/Home.en]]
- [[EN/00-Start/03-Chip-Comparison.en]]
- [[EN/03-GPIO/01-GPIO-oglyad.en]]
- [[EN/03-GPIO/02-Strapping-pini.en]]
- [[EN/02-Power-Supply/01-Power-Rails.en]]
- [[EN/03-Power-Consumption.en]]
- [[EN/04-Batteries-TP4056.en]]
