---
title: ESP32 chip comparison - Classic/S2/S3/C3/C6/H2/P4/C5
description: Comparison of ESP32 Classic, S2, S3, C3, C6, H2, P4, C5 and C61 with choice matrices, prices and toolchain support; shows schematics, code and tables.
tags:

  - esp32
  - esp32/start
  - esp32/hardware
  - esp32/chips

aliases:

  - Chip comparison
  - Chip comparison EN
  - ESP32 vs S2 vs S3 vs C3 vs C6 vs H2

type: reference
lang: en
original: 00-Start/03-Porivnyannya-chipiv.md
date-created: 2026-10-08
date: 2026-10-08
---

# ESP32 chip comparison

> [!tip] Quick pick
> Universal - **ESP32-Classic** or **S3**. Cheap Wi-Fi sensor - **C3**. Camera/ML/USB - **S3**. Zigbee/Thread - **C6/H2**. Look terms up in the [[00-Start/02-Glosariy| Glossary]], boards in [[00-Start/04-Devkit-plati| DevKit boards]], SDK in [[00-Start/05-Vibir-seredovischa| Environment choice]]. Reference structure - [[00-Start/01-Yak-koristuvatis-dovidnikom| How to use it]], map - [[Home.en | Home map]].
>
> [!warning] All chips are 3.3V!
> No ESP32 (Classic/S2/S3/C3/C6/H2) has 5V-tolerant GPIO. They differ only in pin count and peripherals, but the setup is one: HIGH = 3.3V max. 5V sensors only via [[_templates/Component-Template.en | template level matching]].

## Detail table

| Parameter | ESP32 Classic | ESP32-S2 | ESP32-S3 | ESP32-C3 | ESP32-C6 | ESP32-H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Cores | 2x Xtensa LX6 | 1x LX7 | 2x LX7 | 1x RISC-V | 1x RISC-V HP + LP | 1x RISC-V |
| Frequency | 160/240 MHz | 240 MHz | 240 MHz | 160 MHz | 160 MHz | 96 MHz |
| SRAM | 520 KB | 320 KB | 512 KB | 400 KB | 512 KB | 320 KB |
| PSRAM option | Yes (WROVER) | Yes | Yes (Octal) | No | No | No |
| External Flash | 4-16 MB | 4-16 MB | 8-32 MB (Octal) | 4-8 MB | 8 MB | 4-8 MB |
| Wi-Fi | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 6 (ax) | No |
| Bluetooth | Classic + BLE 4.2 | No (USB only) | BLE 5.0 Mesh | BLE 5.0 Mesh | BLE 5.3 + 15.4 | BLE 5.2 + 15.4 |
| Zigbee/Thread | No | No | No | No | Yes | Yes |
| USB | UART bridge only | OTG Full-Speed | OTG Full-Speed | CDC serial | CDC + JTAG | CDC |
| ADC | 2x 12-bit (18 ch.) | 2x 13-bit (20 ch.) | 2x 12-bit (20 ch.) | 2x 12-bit (6 ch.) | 1x 12-bit (7 ch.) | No (temp sensor) |
| DAC | 2x 8-bit | 2x 8-bit | No | No | No | No |
| Touch | 10 ch. | 14 ch. | 14 ch. | No | No | No |
| RMT / MCPWM / TWAI | Yes | Yes / No / Yes | Yes | RMT, MCPWM lite | RMT, MCPWM | - |
| ULP | FSM | FSM + RISC-V | FSM + RISC-V | No | LP-Core | LP |
| Module price, $ | 3-5 | 3-5 | 5-8 | 2-4 | 4-6 | 3-5 |
| Use | Universal, BT Classic | USB HID, no BLE | Camera, ML, displays | Sensors, ESP-NOW | Matter, gateways | Zigbee end nodes |

## Choice advice

| Task | Take | Why |
| --- | --- | --- |
| Learning, legacy projects, A2DP | ESP32 Classic (WROOM-32) | Most examples, DAC, BT Classic |
| USB keyboard, device | S2 (Saola) | Native USB, cheap, but no BLE |
| OV2640 camera, TinyML, LCD | S3 (DevKitC-1) | Octal PSRAM, AI vector instructions, USB |
| Cheap Wi-Fi/MQTT sensor | C3 SuperMini | $2-3, BLE 5, low draw |
| Matter / Thread / Zigbee | C6 or H2 | 802.15.4, Wi-Fi 6 (C6) |
| Battery sensor for years | C3 / H2 + deep-sleep | 5 µA sleep, see [[00-Start/04-Devkit-plati| DevKit power]] |

> [!tip] PSRAM
> For cameras (OV2640 2 MP) and LVGL displays take a **WROVER** or an **S3 with 8 MB Octal PSRAM**. Without PSRAM a JPEG frame will not fit in SRAM. Power details - [[00-Start/04-Devkit-plati| DevKit boards]].
>
> [!warning] ADC2 + Wi-Fi
> On Classic/S3 the ADC2 channel clashes with the Wi-Fi driver. For analog readings with Wi-Fi on, use ADC1 only. This is a common cause of jumping readings.

## Toolchain compatibility

| Toolchain | Classic | S2/S3 | C3/C6/H2 |
| --- | --- | --- | --- |
| ESP-IDF 5.x | Yes | Yes | Yes (RISC-V stable since 5.0) |
| Arduino-core 2.x/3.x | Yes | Yes | Yes, C6/H2 on 3.x only |
| MicroPython | Yes | S2/S3 partly | C3 yes, C6/H2 experimental |
| PlatformIO | Yes | Yes | Yes |

Details - [[00-Start/05-Vibir-seredovischa| Environment choice]].

> [!example] Photo/schematic: ![[assets/img/placeholder.png]]
> Comparison bench: three DevKits on one desk:

| ESP32 DevKit | USB | Note |
| --- | --- | --- |
| Classic DOIT | Micro-USB | CP2102, 5V to 3.3V AMS1117 |
| S3 DevKitC-1 | USB-C native | Two ports: UART + USB-OTG |
| C3 SuperMini | USB-C native | CDC, BOOT button for flashing |
| GND between boards | - | Tie together for shared 3.3V sensors |

## New chips: C5 / C61 / P4 / C2 (2025-2026)

> [!tip] Newcomers in detail
> Full notes: C5/C61 - [[01-Hardware/10-ESP32-C5-C61.en]], C2/P4 - [[01-Hardware/09-ESP32-C2-P4.en]],
> C3/C6/H2 - [[01-Hardware/04-ESP32-C3-C6-H2.en]]. Below - a short cut to pick in 2 minutes.

| Chip | What it is | Headline feature | Limit |
| --- | --- | --- | --- |
| ESP32-C5 | C-line flagship, RISC-V 240 MHz + LP 40 MHz | **Dual-band Wi-Fi 6 (2.4 + 5 GHz)** + BLE + **802.15.4** on one die | Pricier, fewer examples than C3/C6; no MIPI/USB HS |
| ESP32-C61 | Cut-price C6 follower, RISC-V 160 MHz | Cheap **Wi-Fi 6 2.4 GHz** + BLE 5, in-package PSRAM, ETM | **No 802.15.4!** No hardware Zigbee/Thread |
| ESP32-P4 | Strong host, dual RISC-V 400 MHz | MIPI-CSI/DSI up to 1080p, USB HS, Ethernet - **no radio!** | Wi-Fi/BLE only via a companion (C6/C61 over SPI/SDIO/UART) |
| ESP32-C2 (ESP8684/85 SiP) | Cheapest node, RISC-V 120 MHz | $1.5-2.5 price, Wi-Fi 4 + BLE 5, SiP-flash 2-4 MB | About 14 GPIO, 272 KB SRAM, no 15.4, modest sleep |

> [!warning] C61 is not C6 for Zigbee!
> Common mistake: taking a C61 for Thread/Zigbee because it is the C6 follower. On the C61 the 802.15.4 radio is
> **cut for price** - Thread/Zigbee will never run there. Need 15.4 → C6, H2 or C5.
> Need only cheap Wi-Fi 6 → C61. Details - [[01-Hardware/10-ESP32-C5-C61.en]].

## Extended table (all 10 chips)

| Parameter | Classic | S2 | S3 | C3 | C6 | C5 | C61 | H2 | C2 | P4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cores | 2x Xtensa LX6 | 1x LX7 | 2x LX7 | 1x RISC-V | RISC-V HP + LP | RISC-V 240 MHz + LP 40 MHz | 1x RISC-V | 1x RISC-V | 1x RISC-V | 2x RISC-V HP + LP |
| Frequency | 160/240 MHz | 240 MHz | 240 MHz | 160 MHz | 160 MHz | 240 MHz | 160 MHz | 96 MHz | 120 MHz | 400 MHz |
| SRAM | 520 KB | 320 KB | 512 KB | 400 KB | 512 KB | 384 KB | 320 KB | 320 KB | 272 KB | 768 KB HP |
| PSRAM option | Yes (WROVER) | Yes | Yes (Octal) | No | No | Yes (external) | Yes (in-package!) | No | No (SiP-flash) | Yes (external, a must for cameras) |
| Flash | 4-16 MB | 4-16 MB | 8-32 MB (Octal) | 4-8 MB | 8 MB | External (QSPI) | Quad SPI + SiP variants | 4-8 MB | Ext. / SiP 2-4 MB (H2/H4) | External |
| Wi-Fi | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 4 (b/g/n) | 6 (ax, 2.4) | **6 (ax, 2.4 + 5!)** | 6 (ax, 2.4) | No | 4 (b/g/n) | No (via C6!) |
| Bluetooth | Classic + BLE 4.2 | No | BLE 5.0 Mesh | BLE 5.0 Mesh | BLE 5.3 + 15.4 | BLE 5 + 15.4 | BLE 5 + Mesh 1.1 | BLE 5.2 + 15.4 | BLE 5 | No (via C6!) |
| Zigbee/Thread | No | No | No | No | Yes | Yes | **No** | Yes | No | No |
| USB | UART bridge | OTG FS | OTG FS | CDC serial | CDC + JTAG | CDC + JTAG | CDC + JTAG | CDC | Serial-JTAG | **OTG HS** |
| GPIO (approx.) | about 34 | about 43 | about 45 | 22 | 30 | up to 29 | 20+ (per module) | 19 | about 14 | 55 |
| Module price 2026, $ | 3-5 | 3-5 | 5-8 | 2-4 | 4-6 | 5-8 | 2.5-4 | 3-5 | 1.5-2.5 | 8-12 |
| Use | Legacy, BT Classic | USB HID, no BLE | Camera, ML, displays | Sensors, ESP-NOW | Matter/Thread gateway | Dual-band gateway, 5 GHz | Cheap Wi-Fi 6 | Zigbee end nodes | Outlet, AT slave | 1080p HMI, USB host |

## Choice matrix (task to chip)

| Task | Take | Why |
| --- | --- | --- |
| Battery sensor (years on a cell) | **C3** (or H2 for Zigbee) | 5 µA sleep, enough RAM, most low-power examples |
| OV2640 camera / TinyML / LCD | **S3** | Octal PSRAM, AI instructions, USB; C5/C6 cannot drive a camera! |
| Zigbee / Thread / Matter-over-Thread | **C6** (gateway) or H2 (end node) | 802.15.4 on die; C61/C2 do not fit - it is missing there |
| Cheapest: outlet, lamp, AT slave | **C2** / ESP8684 | $1.5-2.5, Wi-Fi 4 + BLE is enough, SiP-flash saves space |
| HMI panel / 1080p camera / USB host | **P4 + C6** (radio companion) | MIPI + USB HS on P4, Wi-Fi 6 from C6 over SPI/SDIO (ESP-Hosted) |
| Wi-Fi 6, crowded air, low latency | **C5** | The only one with **5 GHz**: TWT, OFDMA, BSS coloring; Thread included |
| Cheap Wi-Fi 6 without Thread | **C61** | C3-level price, Wi-Fi 6 features (TWT/OFDMA), Matter-over-WiFi |
| USB keyboard, device without BLE | S2 | Native USB, cheap; but look at S3 for new projects |
| Learning, legacy, A2DP / BT Classic | Classic (WROOM-32) | Most examples, DAC, BT Classic - but read the EOL note below! |

## 2026 prices (guide, modules/DevKits)

| Chip | Module, $ | DevKit, $ | Comment |
| --- | --- | --- | --- |
| C2 / ESP8684 | 1.5-2.5 | 4-6 | Cheapest entry; MINI boards cost less than a DevKit |
| C3 | 2-4 | 5-7 | SuperMini clones are the price floor, but inspect the LDO and USB bridge |
| C61 | 2.5-4 | 6-9 | MINI-1 available; price will fall as stock fills |
| H2 | 3-5 | 7-10 | Niche, keep spares: needs a border router (C6/S3) |
| Classic | 3-5 | 6-9 | Price holds on volume, but it is legacy |
| S2 | 3-5 | 7-10 | Demand is low - hunt sales, or take S3 |
| C6 | 4-6 | 8-12 | Matter-segment hit, price stable |
| C5 | 5-8 | 10-15 | Premium for dual-band and novelty; DevKitC-1 in official stores |
| S3 | 5-8 | 10-16 | Depends on PSRAM (8 MB Octal costs more) |
| P4 | 8-12 | 15-25 | Plus the C6 companion and PSRAM price; cost HMI projects whole |

> Prices are AliExpress/distributor retail, autumn 2026. Volume lots of 100+ units run 20-40% lower.
> Before buying, verify the exact module in stock (WROOM/WROVER/MINI), not just the chip.

## EOL note: Classic is legacy

> [!danger] New projects - not on Classic!
> ESP32 Classic (LX6, Wi-Fi 4, 2016) is mature but a dead end: no Wi-Fi 6,
> no 802.15.4, higher draw, 40-nm process versus modern ones. Espressif has long pushed
> migration: ESP8266 → C2, while Classic is being pushed out of new designs by S3 (power),
> C6/C5 (Wi-Fi 6 + Matter) and C61/C3 (price). Keep Classic for: supporting old boards,
> BT Classic/A2DP (no C-chip has it!), DAC and ready examples.
> Verify long-term availability of a given chip in
> [Longevity Commitment (Espressif)](https://www.espressif.com/en/products/longevity-commitment)
> and PCN notices - do not lock Classic into a 5+ year product without checking.

| Take instead of Classic | When |
| --- | --- |
| S3 | Camera, displays, ML, USB - direct power follower |
| C6 / C5 | Wi-Fi 6, Matter, gateways; C5 if you need 5 GHz |
| C3 / C61 | Cheap sensors; C61 if you want Wi-Fi 6 at C3 price |
| C2 | Ultra-cheap nodes instead of ESP8266/simple Classic tasks |

## New-chip toolchain support

| Toolchain | C5 | C61 | P4 | C2 |
| --- | --- | --- | --- | --- |
| ESP-IDF | **5.5+** (`set-target esp32c5`) | **5.5+** (`esp32c61`) + Matter SDK | 5.3+ (`esp32p4`) | 5.0+ (`esp32c2`) |
| Arduino-core | **3.3.x+** (C5 Dev Module board) | **3.3.x+** (PR #12019) | 3.x, partly | 2.x/3.x |
| MicroPython | Experiment (no stable build) | Experiment | Experiment | Yes (compact build) |
| PlatformIO | Via pioarduino/community | Same path | Yes | Yes |

Details - [[00-Start/05-Vibir-seredovischa| Environment choice]],
IDF setup - [[09-Proshivka/01-ESP-IDF-setup.en | ESP-IDF setup]],
Arduino/PIO - [[09-Proshivka/02-Arduino-PlatformIO.en | Arduino/PlatformIO]],
full notes - [[01-Hardware/10-ESP32-C5-C61.en]] and [[01-Hardware/09-ESP32-C2-P4.en]].

## See also

- [[Home.en | Home map]]
- [[00-Start/01-Yak-koristuvatis-dovidnikom| How to use it]]
- [[00-Start/02-Glosariy| Glossary]]
- [[00-Start/04-Devkit-plati| DevKit boards]]
- [[00-Start/05-Vibir-seredovischa| Environment choice]]
- [[01-Hardware/10-ESP32-C5-C61.en | C5/C61]]
- [[01-Hardware/09-ESP32-C2-P4.en | C2/P4]]
- [[01-Hardware/04-ESP32-C3-C6-H2.en | C3/C6/H2]]
- [[_templates/Component-Template.en | Component template]]
