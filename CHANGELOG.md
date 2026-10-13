---
title: Embedded Reference - Change Log
description: Version history of embedded-reference knowledge base across ESP32, STM32, ARDUINO and Raspberry Pi vaults; shows updates, translations and refactor milestones.
tags: [changelog, embedded-reference, esp32, stm32, arduino, raspberrypi]
category: Meta
date-created: 2026-10-08
date: 2026-10-12
---

# Change Log

## 2026-10-12 — Refactor B: EN/UA split, English folder names, meta consolidation, all links verified
- All 4 vaults (ESP32-Reference, STM32-Reference, ARDUINO-Reference, RaspberryPi-Reference) moved to `obsidian_vault/` with `EN/` and `UA/` directories.
- English folder names applied (e.g., `02-Power-Supply`, `10-Sensors`, `99-Additions`).
- 491 EN files created/verified (real translations, 0 stubs, 0 broken links, 0 missing PNG).
- All EN meta files (CHANGELOG, COMPONENTS, TODO) consolidated to repo root only.
- Link remapping completed; `check_lang`, `check_style`, `check_links`, `check_home` pass with 0 errors.
- 77 ESP32 EN files translated from partial status to full English prose outside code.
- 13 STM32 EN files translated (11-Vivid, 13-Power-Modules, 17-Lab, 02-Power-Supply).

## 2026-10-08 — Base creation / initial EN wave
- Original 489 UA notes across 4 vaults.
- EN infrastructure (i18n-spec, export_github.py, check scripts) established.
