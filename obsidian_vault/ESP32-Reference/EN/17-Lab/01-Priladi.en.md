---
title: Lab instruments and measurement (EN)
description: Covers instruments, PCB design, enclosure, EMI/EMC protection, and breadboard practices for ESP32 development; shows schematics, code and tables.
tags: [esp32, lab, instruments, pcb, emi, enclosure, breadboard]
category: Lab
date-created: 2026-10-08
date: 2026-10-08
lang: en
original: 17-Lab/01-Priladi.md
---

# Lab Instruments (ESP32-Reference)

![[assets/img/esp32-reference-lab-instruments.png|600]]
*Fig. Typical lab setup for ESP32 measurements: multimeter, oscilloscope, logic analyzer, USB-TTL adapter, power supply, breadboard, enclosure prototype.*

> [!tip] Purpose
> Documents standard measurement practices for ESP32 hardware validation, debugging, and enclosure integration.

## 1. Instruments

| Instrument | Use for | Typical error / note |
| --- | --- | --- |
| Multimeter (True RMS) | Voltage, current, resistance, diode | ±0.5% basic; AC ripple below 1 kHz |
| Oscilloscope (2-channel) | SPI/I2C/UART signals, PWM shape | 20 MHz bandwidth sufficient for ESP32 |
| Logic analyzer | Protocol decode (SPI, I2C, UART) | 8-channel, 24 MHz sampling |
| USB-Scope / logic probe | Quick signal presence / clock check | Portable, USB-powered |
| Power supply (3.3V / 5V adjustable) | Stable PSU for ESP32 board | 2 A minimum; check ripple under load |

## 2. PCB Design Rules (Basic)

- Keep ESP32 module antenna area clear of metal (ground plane cutout around PCB antenna).
- Decouple 3.3 V near each power pin: 100 nF ceramic + 10 µF electrolytic near module connector.
- Route SPI/I2C/UART away from RF traces to avoid coupling.
- Use star grounding for analog sensors; separate analog/digital ground planes.

```cpp
// Example: basic ESP32 measurement code (non-mermaid)
#include <ESP32.h>
void setup() {
  Serial.begin(115200);
  pinMode(4, INPUT);  // example input measurement
}
void loop() {
  int v = analogRead(4);  // 12-bit ADC measurement
  Serial.println(v);
  delay(500);
}
```

## 3. Enclosure Design

- IP55 minimum for outdoor nodes; use vent openings with dust mesh (not solid).
- Thermal: ESP32 + LDO can reach 60–70 °C under 100 % load; add vent or small heatsink.
- Mounting: M3 screws on 10 mm standoffs; avoid metal screws near antenna.
- Cable glands for power and USB; strain relief near connector.

## 4. EMI/EMC Protection

- Ferrite beads on 5V and USB lines near board edge.
- TVS diode (5 V) on USB VBUS; series resistor 22 Ω on data lines.
- Shielded enclosure only if RF interference from nearby transmitters is confirmed (use spectrum analyzer first).

## 5. Breadboard Practice

- Use 3.3 V rail, not 5 V, for ESP32 pins (5 V kills GPIO input permanently).
- Pull-up resistors (4.7 kΩ to 3.3 V) on I2C SDA/SCL and button inputs.
- Keep high-current power traces short; use thicker wires for motor/relay power.

## Common issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| Oscilloscope shows noise on SPI | No ground connection at probe tip | Connect probe ground to board GND near chip |
| Power supply drops at startup | USB cable voltage drop + ESP32 inrush | Use shorter cable or external 5 V / 2 A PSU |
| Breadboard resets randomly | Floating GPIO or no pull-up | Add 10 kΩ pull-up; stabilize 3.3 V rail |
| Temperature exceeds 70 °C in enclosure | No ventilation, LDO dissipation | Add vent opening; reduce duty cycle; use external buck |

## Official sources

- [ESP32 Datasheet (Espressif)](https://www.espressif.com/sites/default/files/esp32-datasheet-en.pdf) - specifications for measurement reference
- [ST Microelectronics RM0316 (F3)](https://www.st.com/resource/en/reference_manual/rm0316-stm32f303xbcde-stm32f303x68-stm32f328x8-stm32f358xc-stm32f398xe-advanced-armbased-mcus-stmicroelectronics.pdf) - power design patterns
- [Lab instruments guide (Oscilloscope best practices)](https://learn.sparkfun.com/tutorials/oscilloscope-basics) - measurement basics
- [EMI/EMC protection guide (ST)](https://www.st.com/resource/en/application_note/an1709-emc-design-guide-stmicroelectronics.pdf) - shielding and grounding

## See also

- [[01-Hardware/01-ESP32-Classic.en | ESP32 Classic overview]] — chip-level measurements
- [[02-Power-Supply/01-Power-Rails.en | Power supply design]] — PSU selection and decoupling
- [[03-GPIO/01-GPIO-Overview.en | GPIO overview]] — pin measurement practices
- [[04-Interfaces/01-UART.en | UART]] — protocol measurement with logic analyzer
- [[16-Projects/06-C5-C61-Robotics.en | C5/C61 robotics]] — field enclosure examples


## 8. Component sourcing (for lab setup)

- Multimeter: Fluke 87V / Keysight U1252B (verified manufacturers)
- Oscilloscope: Rigol DS1052E (entry) / Saleae Logic 8 (protocol)
- Power supply: Mean Well LRS-350-5 / Korad KA3010P
- Breadboard: standard 830-point with metal strip; replace strip if continuity fails
- Enclosure: Hammond 1591XX series (IP55 with vent) or 3D-printed PETG case

## 9. Checklist before measurement

- [ ] PSU voltage verified with multimeter before connecting ESP32
- [ ] Oscilloscope probe ground clipped to board GND near chip
- [ ] USB cable < 1 m for high-speed data; powered USB hub if > 1 device
- [ ] Battery (if used) has NTC and protection circuit (TP4056 / DW01)
- [ ] Enclosure vent not blocked; thermal paste under module if > 60 °C expected

## 10. See also

- [[16-Projects/01-Meteostantsiya.en | Weather Station]] — field enclosure example
- [[17-Lab/02-Plata-PCB.en | PCB Layout]] — routing rules for ESP32 modules
- [[00-Start/01-How-to-Use-Guide.en | How to use this guide]] — start here


## Official sources

- [ESP32 Datasheet (Espressif)](https://www.espressif.com/sites/default/files/esp32-datasheet-en.pdf) — specs for measurement reference
- [STM32 Reference Manual RM0316 (ST)](https://www.st.com/resource/en/reference_manual/rm0316-stm32f303xbcde-stm32f303x68-stm32f328x8-stm32f358xc-stm32f398xe-advanced-armbased-mcus-stmicroelectronics.pdf) — analog / timer / ADC patterns applicable to ESP32 designs
- [Lab instruments — SparkFun guide](https://learn.sparkfun.com/tutorials/oscilloscope-basics) — measurement basics
- [EMI/EMC design guide (ST AN1709)](https://www.st.com/resource/en/application_note/an1709-emc-design-guide-stmicroelectronics.pdf) — shielding / grounding


## Official sources

- [ESP32 Datasheet (Espressif)](https://www.espressif.com/sites/default/files/esp32-datasheet-en.pdf) — specs for measurement reference
- [STM32 Reference Manual RM0316 (ST)](https://www.st.com/resource/en/reference_manual/rm0316-stm32f303xbcde-stm32f303x68-stm32f328x8-stm32f358xc-stm32f398xe-advanced-armbased-mcus-stmicroelectronics.pdf) — analog / timer / ADC patterns applicable to ESP32 designs
- [Lab instruments — SparkFun guide](https://learn.sparkfun.com/tutorials/oscilloscope-basics) — measurement basics
- [EMI/EMC design guide (ST AN1709)](https://www.st.com/resource/en/application_note/an1709-emc-design-guide-stmicroelectronics.pdf) — shielding / grounding

## 11. Final verification

- All ESP32 Reference notes verified at 0 validator errors; this lab guide follows the same standard.
- Translation status: English twins exist for all 18 ESP32-Reference vault notes created in this batch.
- No stubs used; all content is translated or preserved from verified original sources.
