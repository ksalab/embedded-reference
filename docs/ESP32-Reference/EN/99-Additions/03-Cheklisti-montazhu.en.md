---
title: Assembly Checklists
description: Assembly, soldering and first-run checklists for ESP32 DevKit, I2C/SPI/UART, power, WiFi/LoRa and deep-sleep verification; shows schematics, code and tables.
tags: [esp32-reference, checklist, assembly, soldering, release]
category: Meta
lang: en
original: ESP32-Reference/99-Additions/03-Cheklisti-montazhu.md
date-created: 2026-09-27
date: 2026-10-08
---

# Assembly and Launch Checklists

![](../../../../ESP32-Reference/assets/img/placeholder.png)

Process: start [Home](../../../../ESP32-Reference/Home.md), pins [01-Pinout-tablici](../../../../ESP32-Reference/UA/99-Dodatki/01-Pinout-tablici.md), power [01-Lancjugi-zhivlennya](../../../../ESP32-Reference/UA/02-Zhivlennya/01-Lancjugi-zhivlennya.md) + [01-Buck-Boost-Solar](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md), levels [02-Level-Shifters](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/02-Level-Shifters.md), diagnostics [02-Troubleshooting-FAQ](../../../../ESP32-Reference/UA/99-Dodatki/02-Troubleshooting-FAQ.md), datasheets [04-Datasheet-Links](../../../../ESP32-Reference/UA/99-Dodatki/04-Datasheet-Links.md).

## 1. First DevKit Launch (5 min)

- [ ] USB DATA cable (not charge-only), port without hub
- [ ] CH340/CP2102 driver installed, COM port visible
- [ ] Nothing connected to GPIO0/2/5/12/15 (strapping pins free)
- [ ] Flash Blink / Hello World at 115200, monitor 115200 8N1
- [ ] EN+BOOT buttons work: EN=reset, BOOT+EN=download
- [ ] 3.3V pin with multimeter: 3.20-3.40V, LDO not warm
- [ ] WiFi scan finds >3 networks (antenna alive)

## 2. Soldering and Assembly

- [ ] Flux + temperature 300-320 C, clean tip, shiny conical solder joint
- [ ] No bridges between neighboring pins (check with x10 loupe)
- [ ] Continuity: VCC-GND must not short (>1k in reverse), SDA/SCL must not short to ground
- [ ] Connectors: pin headers first, then wires; colors: red VCC, black GND, yellow/green signal
- [ ] I2C length <30 cm, SPI <20 cm, UART <100 cm (or twisted pair)
- [ ] I2C pull-up 4.7k, SPI CS 10k to 3.3V, EN 10k+10µF, BOOT 10k to 3.3V
- [ ] TVS + fuse on external lines (see [02-Level-Shifters](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/02-Level-Shifters.md))

## 3. Power (before first power-on!)

| ESP32 | Check | Norm |
| --- | --- | --- |
| 5V VIN | buck voltage without load | 5.00 +- 0.10V |
| 3.3V | LDO voltage without load | 3.30 +- 0.10V |
| GND | resistance to case/ground | 0 Ohm, no loops |
| Idle current | USB tester without WiFi | 40-80 mA classic, 20-40 mA S3/C3 |
| WiFi TX current | network scan | peak 350-500 mA, dip <0.15V |

- [ ] Buck set WITHOUT ESP32, sealed with lacquer (see [01-Buck-Boost-Solar](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md))
- [ ] SIM800L: 4.0V + 1000 µF, NRF24: 3.3V + 10 µF, camera: +100 µF
- [ ] RC522/LoRa only 3.3V, SIM800L only 4V - check twice!

## 4. I2C / SPI Launch

- [ ] I2C scanner finds address (0x76/0x77 BME280, 0x68 MPU, 0x27 LCD)
- [ ] Start frequency 50-100 kHz, then 400 kHz if stable
- [ ] Logic analyzer / oscilloscope: SDA/SCL edges clean, no steps
- [ ] SPI: start at 1 MHz, CS toggles, MISO does not hang (pull-up 10k)
- [ ] RC522 DumpVersion not 0x00/0xFF; NRF24 printDetails shows config

## 5. WiFi / Radio

- [ ] Scan: RSSI > -75 dBm at installation site
- [ ] Connection + router ping <50 ms, reconnect on drop implemented
- [ ] MQTT/HTTP: keepalive 15-30 s, timeouts, watchdog for hangs
- [ ] LoRa: frequency matches Ra-02 label (433 vs 868), antenna screwed on BEFORE power
- [ ] NRF24: PA_LOW on table, PA_MAX only with good power and distance

## 6. Deep-Sleep Measurement

- [ ] All extras off: USB-UART power interrupted, LEDs desoldered or accounted
- [ ] Multimeter/INA219 in 5V gap: active mode recorded, sleep mode recorded
- [ ] Norm classic: modem-sleep ~20 mA, light-sleep ~2 mA, deep-sleep 10-150 µA (depends on board)
- [ ] Wakeup sources verified: timer + ext0/ext1 + touch, after wakeup peripherals re-initialized
- [ ] Battery calculation: 3000 mAh / average current = hours; reserve x1.5 for cold

## 7. Release Check (before delivery/installation)

- [ ] Partition with OTA, firmware version in EEPROM/NVS, logging in Serial + file
- [ ] WDT enabled, brownout 2.7V, code survives reboot (state in RTC/NVS)
- [ ] Case: ventilation, antenna outside, wires secured, moisture protection if needed
- [ ] Documentation: schematic, pinout sheet, WiFi password, where .bin firmware is stored
- [ ] Spare ESP32 module + flashed .bin on flash drive next to product

## 8. Batch Check (batch 10+ pcs, before shipping!)

```text
[ ] Firmware identical: version + sha on all (read back and verify!)
[ ] NVS: serial numbers unique (mfg partition, not clone!)
[ ] eFuse: summary saved to batch log (see 17-Lab/03)
[ ] Self-test PASS on each (see 17-Lab/03 sec. 8)
[ ] RF: RSSI selective against reference (3 of 10)
[ ] Case: glands tightened, plugs in place, Gore in place
[ ] Kit: board + antennas + mounts + paper with QR to docs
```

## See Also

- [Home](../../../../ESP32-Reference/Home.md)
- [01-Pinout-tablici](../../../../ESP32-Reference/UA/99-Dodatki/01-Pinout-tablici.md)
- [02-Troubleshooting-FAQ](../../../../ESP32-Reference/UA/99-Dodatki/02-Troubleshooting-FAQ.md)
- [04-Datasheet-Links](../../../../ESP32-Reference/UA/99-Dodatki/04-Datasheet-Links.md)
- [01-Lancjugi-zhivlennya](../../../../ESP32-Reference/UA/02-Zhivlennya/01-Lancjugi-zhivlennya.md)
- [01-Buck-Boost-Solar](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md)
- [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md)

![](../../../../ESP32-Reference/assets/img/placeholder.png)

> UA original twin: [UA](../../../../ESP32-Reference/UA/99-Dodatki/03-Cheklisti-montazhu.md)
