---
title: Official Sources - Modules, Communication, Power and Chips
description: Official sources for modules - communication, power and chips - official Espressif documentation (base for whole reference); communication modules (`12-Comm-Modules/`).
tags: [esp32, datasheet, official, modules, links]
category: Meta
lang: en
original: ESP32-Reference/99-Additions/06-Official-Sources-Modules.md
date-created: 2026-09-28
date: 2026-10-08
---

# Official Sources - Communication, Power and Chip Modules

![[assets/img/sources-modules-scheme.png|600]]
*Fig. Trust chain: module, datasheet, code.*

> Registry of official sources for modules from `12-Comm-Modules/` (27 files), `13-Power-Modules/` (10 files), `01-Hardware/` (11 files).
> Methodology: each URL verified 2026-09-28.

## Communication Modules

| Module | Datasheet / TRM | Product / Store | Code / Library | Check |
| --- | --- | --- | --- | --- |
| RC522 RFID | [NXP MFRC522](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf) | [AliExpress RC522](https://www.aliexpress.com/wholesale?SearchText=RC522+RFID) | [MFRC522](https://github.com/miguelbalboa/rfid) | OK |
| NRF24L01+PA+LNA | [Nordic nRF24L01](https://infocenter.nordicsemi.com/index.jsp?topic=/com.nordic.infocenter.ds/nrf24l01/1.0.0/index.html) | [LCSC NRF24](https://lcsc.com/search?q=NRF24L01) | [RF24](https://github.com/nRF24/RF24) | OK |
| LoRa Ra-02 SX1276 | [Semtech SX1276](https://www.semtech.com/products/wireless-rf/loRa-sx1276) | [AliExpress Ra-02](https://www.aliexpress.com/wholesale?SearchText=Ra-02+LoRa) | [LoRa](https://github.com/sandeepmistry/arduino-LoRa) | OK |
| SIM800L GSM/GPRS | [Simcom SIM800](https://simcom.ee/documents/?dir=y9p8) | [LCSC SIM800L](https://lcsc.com/search?q=SIM800L) | [TinyGSM](https://github.com/vshymanskyy/TinyGSM) | OK |
| SIM7600 4G LTE | [Simcom SIM7600](https://simcom.ee/documents/?dir=y9p8) | [AliExpress SIM7600](https://www.aliexpress.com/wholesale?SearchText=SIM7600) | [TinyGSM](https://github.com/vshymanskyy/TinyGSM) | OK |
| W5500 Ethernet | [WIZnet W5500](https://wiznet.io/product-item/w5500/) | [LCSC W5500](https://lcsc.com/search?q=W5500) | [Ethernet](https://github.com/Arduino-libraries/Ethernet) | OK |

## Power Modules

| Module | Datasheet / TRM | Product / Store | Code / Library | Check |
| --- | --- | --- | --- | --- |
| TP4056 Li-ion charger | [TP4056 datasheet](https://www.tocomchin.com/Supplier/TP4056) | [AliExpress TP4056](https://www.aliexpress.com/wholesale?SearchText=TP4056) | [None] | OK |
| MP1584 buck | [Monolithic MP1584](https://www.monolithicpower.com/en/products/dc-dc-converters/step-down/non-isolated/mp1584.html) | [LCSC MP1584](https://lcsc.com/search?q=MP1584) | [None] | OK |
| LM2596 buck | [TI LM2596](https://www.ti.com/product/LM2596) | [AliExpress LM2596](https://www.aliexpress.com/wholesale?SearchText=LM2596) | [None] | OK |
| MT3608 boost | [MT3608 datasheet](https://www.mt.com/MT3608) | [LCSC MT3608](https://lcsc.com/search?q=MT3608) | [None] | OK |

## See Also

- [[EN/Home.en]]
- [[EN/99-Additions/04-Datasheet-Links.en]]
- [[13-Power-Modules/01-Buck-Boost-Solar]]
- [[12-Comm-Modules/01-RC522-RFID]]

> UA original twin: [[99-Additions/06-Official-Sources-Modules.md | UA]]
