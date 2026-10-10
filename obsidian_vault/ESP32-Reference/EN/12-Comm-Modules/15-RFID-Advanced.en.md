---
title: RFID Advanced - Mifare Classic Deep, NTAG/DESFire, T5577, HID, UHF EPC Gen2, Wiegand/OSDP, Upgrade Readers
description: RFID Advanced - Mifare Classic deep, LF rewritable, HID, UHF, Wiegand/OSDP, upgrade readers - Mifare Classic deep; 1. Mifare Classic geometry / keys / nested attacks / cloning; 2. Anticollision / cascade; 3. Ultralight/NTAG vs DESFire vs FeliCa; 4. Rewritable LF 125 kHz: T5577 / EM4305; 5. HID Prox / Indala / FDX-B / HDX; 6. UHF EPC Gen2: R2000 / YRM100; 7. Wiegand deep / OSDP; 8. Upgrade readers: PN5180 / ST25R3911 / TRF7970A / CLRC663; 9. ESP32 connection; 10. Code; 11. Common errors; 12. Official sources; 13. See also; shows schematics, code and tables.
tags: [esp32, rfid, mifare, mifare-classic, ntag, ultralight, desfire, felica, t5577, em4100, hid, wiegand, osdp, uhf, epc-gen2, r2000, yrm100, pn5180, st25r3911, trf7970a, clrc663, upgrade, wiegand, oosdp]
category: Moduli
lang: en
original: /home/ksalab/projects/embedded-reference/ESP32-Reference/UA/12-Moduli-zvyazku/15-RFID-Advanced.md
date: 2026-10-09
date-created: 2026-09-29
---

# RFID Advanced - Mifare Classic Deep, LF Rewritable, HID, UHF, Wiegand/OSDP, Upgrade Readers

> [!warning] Law and Ethics
> All information about keys, Crypto-1, nested attacks, T5577 cloning — **only for your own cards / key fobs and your own systems**. Do not use for third-party access control or payment cards.

This note is an in-depth continuation of [[EN/12-Comm-Modules/01-RC522-RFID.en]] and [[EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en]] and [[EN/12-Comm-Modules/20-NFC-Biometry-2.en]]: Mifare Classic deep (geometry, keys, nested attack, Clone / RLF / darkside), anticollision / cascade, Ultralight / NTAG vs DESFire vs FeliCa, rewritable LF 125 kHz (T5577 / EM4305 vs EM4100), HID Prox / Indala, animal FDX-B / HDX (134 kHz), UHF EPC Gen2 (R2000 / YRM100), Wiegand deep / OSDP, upgrade readers (PN5180 / ST25R3911 / TRF7970A / CLRC663), ESP32 connection, code examples, common errors, references.

![[assets/img/rfid-advanced-mifare-scheme.png|600]]
*Fig. Mifare Classic memory map: sectors -> blocks -> sector trailer (KeyA / AccessBits / KeyB), value blocks, linked sectors, Anti-collision / cascade flow.*

Links to [[EN/Home.en]], [[EN/12-Comm-Modules/01-RC522-RFID.en]], [[EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en]], [[03-Projects/01-Smart-Home]], [[EN/12-Comm-Modules/20-NFC-Biometry-2.en]], [[04-Interfaces/02-SPI|SPI]], [[04-Interfaces/01-UART|UART]], [[02-Power-Supply/01-Lancjugi-zhivlennya]].

## Purpose

RFID Advanced - Mifare Classic deep, LF rewritable, HID, UHF, Wiegand/OSDP, upgrade readers - Mifare Classic deep; 1. Geometry / keys / nested attacks / cloning; 2. Anticollision / cascade; 3. Ultralight/NTAG vs DESFire vs FeliCa; 4. Rewritable LF 125 kHz: T5577/EM4305; 5. HID Prox/Indala and animal FDX-B/HDX; 6. UHF EPC Gen2: R2000/YRM100; 7. Wiegand deep / OSDP; 8. Upgrade readers; 9. ESP32 connection; 10. Code; 11. Common errors; 12. Official sources; 13. See also; shows schematics, code and tables.

## Contents

1. [Mifare Classic deep](#1-mifare-classic-deep)
2. [Anticollision and cascade](#2-anticollision--cascade-select)
3. [Ultralight/NTAG vs DESFire vs FeliCa](#3-mifare-ultralightntag-vs-desfire-vs-felica)
4. [Rewritable LF 125 kHz: T5577 / EM4305](#4-rewritable-lf-125-khz-t5577em4305-vs-em4100)
5. [HID Prox / Indala and animal FDX-B / HDX](#5-hid-proxindala-and-animal-fdx-bhdx-134-khz)
6. [UHF EPC Gen2: R2000 / YRM100](#6-uhf-epc-gen2-r2000yrm100)
7. [Wiegand deep and OSDP](#7-wiegand-deep-and-osdp)
8. [Upgrade readers: PN5180 / ST25R3911 / TRF7970A / CLRC663](#8-upgrade-readers-pn5180st25r3911trf7970aclrc663)
9. [Connection to ESP32](#9-connection-to-esp32)
10. [Code](#10-code)
11. [Common errors](#common-errors)
12. [Official sources](#official-sources)
13. [See also](#see-also)

## 1. Mifare Classic Deep

### 1.1. Geometry 1K / 4K / Mini

| Card | Sectors | Blocks | Total bytes | Data blocks | Useful bytes* |
| --- | --- | --- | --- | --- | --- |
| Mifare Mini (320 B) | 5 (sectors 0-4, 4 blocks each) | 20 | 320 | 14 | 224 |
| Mifare Classic 1K (S50) | 16 (sectors 0-15, 4 blocks) | 64 (0-63) | 1024 | 48 | 752 |
| Mifare Classic 4K (S70) | 40: sectors 0-31 (4 blocks) + 32-39 (16 blocks) | 256 (0-255) | 4096 | 216 | 3440 |
| Classic EV1 1K/4K | like S50 / S70 + 7-byte UID option + counters | same | same | same | same |

*Useful bytes exclude sector trailers (6 bytes per sector for 1K / 4 bytes for 4K after sector 31) and manufacturer block 0.

### 1.2. Key Structure and Access Bits

```
Sector trailer (block 3 of each sector for 1K; block 15 / 31 / 47 / ... for 4K):
  Bytes 0-5: Key A (6 bytes) — default FF FF FF FF FF FF
  Bytes 6-9: Access bits (4 bytes) — e.g. FF 07 80 69 for open read/write
  Bytes 10-15: Key B (6 bytes) — can be used as data (if access bits allow)
```

Access bits determine: read Key A (always needed for selection), write Key A, read / write data, read / write Key B, transport config. The 3-byte access structure is: C1-x / C2-x / C3-x per segment (data / trailer / key), giving 8 conditions per block.

> [!warning] Default Keys Are Public
> Key A = FF FF FF FF FF FF, Key B = FF FF FF FF FF FF on factory cards. Change immediately after first read. Never leave Key B as data if access bits allow public access — attackers can rewrite sector trailers.

### 1.3. Value Blocks (Value / Backup / Nested)

```
Value block format (4 bytes):
  Byte 0-3: value (little-endian signed 32-bit) — e.g. 00 00 04 D2 = 1234
  Byte 4-7: inverted value (bitwise NOT of bytes 0-3) — for integrity
  Byte 8-11: value again (for triple-check)
  Byte 12-15: address / block number — for linking to master value
```

Nested attack (darkside / nested authentication): attacker selects a card, performs authentication with known key on one sector, then uses the same key stream (nonce + encrypted nonce) to recover Key A / B of other sectors. Defense: use different keys per sector, rotate keys, disable nested authentication (if reader allows), or migrate to DESFire / NTAG.

### 1.4. Clone / RLF / Darkside Tools

| Tool / Method | What It Does | Defense |
| --- | --- | --- |
| Proxmark3 (RDV 4 / PM3) | Full Mifare Classic analysis, nested attack, clone to T5577 | Change keys, use DESFire |
| MCT (Mifare Classic Tool) | Read / write / dump cards, change keys | Rotate keys, disable default |
| RLF (radio frequency analysis) | Capture RF, replay, clone to T5577 / EM4305 | Use rolling code / DESFire |
| Darkside attack | Passive nested auth without card selection | Different keys per sector |
| Gen3 / Gen1 clone cards | Write Mifare Classic data to T5577 / EM4305 | Monitor card logs, use AES |

## 2. Anticollision and Cascade Select

```
1. Reader sends REQA / WUPA (7 bits, 0x26 / 0x52) — all cards answer
2. Anticollision: cards send UID bit by bit; cards with 0 at first collision drop out
3. Cascade Level 1: select UID first 4 bytes; for 7-byte UID (EV1) -> cascade level 2
4. Select (SEL + UID) -> card selected; now ready for authentication
5. Authentication (Auth A / Auth B): nonce + encrypted nonce -> session key
6. Read / Write blocks via READ (0x30) / WRITE (0xA0)
```

```c
// ESP32 (Arduino): basic anticollision + read sector 0 block 0 via MFRC522
#include <MFRC522.h>
MFRC522 mfrc522(5, 22); // NSS=5, RST=22

void setup() {
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop() {
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    if (mfrc522.MIFARE_Read(0, buffer, 18)) {
      Serial.println("UID: ");
      for (byte i = 0; i < 4; i++) Serial.print(buffer[i], HEX);
    }
    mfrc522.PICC_HaltA();
  }
}
```

## 3. Mifare Ultralight / NTAG vs DESFire vs FeliCa

| Feature | Mifare Ultralight C / EV1 | NTAG213 / 215 / 216 | DESFire EV2 / EV3 | FeliCa Lite / Standard |
| --- | --- | --- | --- | --- |
| Standard | ISO/IEC 14443 Type A | NFC Type 2 (ISO 14443A) | ISO/IEC 14443 Type A / B / FeliCa | FeliCa (212 / 424 kbps) |
| Storage | 192 / 768 B | 144 / 504 / 888 B | 2 - 8 KB files | 1 - 9 KB |
| Crypto | None (password 32-bit on NTAG) | PWD + lock bits | AES-128 / 3DES / file keys | AES / common key / service key |
| UID | 7 bytes (EV1 option) | 7 bytes | 7 bytes | 8 / 16 bytes |
| Anti-clone | Low | Low | Very high (key diversity) | High (common / service key) |
| Cost | € | € | €€€ + SAM | €€ (Japan / Asia) |
| Use | Tags, URLs, Wi-Fi pairing | Business cards, URL, NDEF | Pay, access, transport | Japan transit, ID |

> [!tip] For access control in 2026: prefer DESFire EV2 with SAM module for master keys. For cheap tags: NTAG216 with PWD + lock bits. Avoid Mifare Classic for new systems.

## 4. Rewritable LF 125 kHz: T5577 / EM4305 vs EM4100

T5577 (RFID 125 kHz, rewritable) and EM4305 (rewritable with password) allow writing UID / data to low-frequency cards. EM4100 is fixed UID, not rewritable.

```
T5577 block format (2 bytes per block):
  Block 0: 0x01 0x0A (config: RF/32, etc.) or 0x01 0x0E (RF/64)
  Block 1: UID first 4 bytes (little-endian)
  Block 2: UID last 2 bytes + 2 bytes data (optional)
  Block 3: data / password (optional)
```

```cpp
// Arduino: T5577 write UID (simplified; full protocol via Proxmark3 / RFIdeas)
#include <SoftwareSerial.h>
// ... T5577 library or Proxmark3 command line: lf t55xx write -b 1 --uid 00112233
```

> [!warning] LF Cloning Is Illegal in Many Jurisdictions
> Rewriting T5577 / EM4305 to clone access cards is illegal in EU / US / UK. Only use for your own systems (e.g. personal RFID key fob replacement). Use DESFire / UHF for secure systems.

## 5. HID Prox / Indala and Animal FDX-B / HDX (134 kHz)

HID Prox (125 kHz, 26-bit facility / card number) and HID Indala (37-bit) use ASK / FSK modulation. FDX-B (134.2 kHz, ISO 11784 / 11785) for animal identification; HDX (half-duplex) also 134 kHz.

| Standard | Frequency | Modulation | Data | Range | Use |
| --- | --- | --- | --- | --- | --- |
| HID Prox 26-bit | 125 kHz | ASK | 26 bits (8 facility + 16 card) | 5-15 cm | Access cards |
| HID Indala 37-bit | 125 kHz | FSK | 37 bits | 5-15 cm | Parking / access |
| FDX-B | 134.2 kHz | FDX / HDX | 15 digits (ISO) | 30-60 cm | Animal IDs |
| HDX | 134.2 kHz | HDX | Variable | 30-60 cm | Livestock tracking |

```c
// ESP32: HID Prox reader (e.g. RFID-RC522 with 125 kHz module or dedicated HID reader on UART)
// Most HID readers output Wiegand 26-bit or UART data; connect to ESP32 UART or use Wiegand-to-TTL adapter
```

## 6. UHF EPC Gen2: R2000 / YRM100

UHF RFID (860-960 MHz) uses EPC Gen2 (ISO/IEC 18000-63). R2000 (Impinj) and YRM100 (YARONG) are chip modules; readers (Impinj Indy, Zebra, etc.) use UART / Ethernet / USB-HID.

```
EPC Gen2 protocol flow:
  1. Inventory: reader sends Query -> tags respond with EPC + RN (random number)
  2. Select: filter by EPC or bank
  3. Read / Write bank 0 (EPC), bank 1 (TID / serial), bank 2 (user)
  4. Kill / Lock: permanent disable or password protect
```

```python
# MicroPython (ESP32): UHF reader over UART (simplified; actual API depends on reader model)
from machine import UART
uhf = UART(2, baudrate=115200, rx=16, tx=17)
# Send inventory command (depends on reader firmware); read EPC response
```

> [!tip] UHF Range: 3-12 m depending on antenna, tag orientation, environment (metal / water). For indoor access: use fixed antennas; for warehouse: handheld or portal.

## 7. Wiegand Deep and OSDP

Wiegand interface (26-bit, 34-bit, 37-bit, 40-bit) is de facto standard for access control. OSDP (Open Supervised Device Protocol, IEC 60839-11-5 / SIA OSDP) is modern, secure, encrypted over RS-485.

| Feature | Wiegand 26-bit | Wiegand 37-bit (Indala) | OSDP (secure) |
| --- | --- | --- | --- |
| Lines | D0 / D1 + GND | D0 / D1 + GND | RS-485 (A / B / GND) |
| Data | 8-bit facility + 16-bit card | 17-bit facility + 19-bit card | Variable, encrypted |
| Security | None | None | AES-128, mutual auth |
| Range | 5-15 cm (reader) | 5-15 cm | 100-1200 m (RS-485) |
| Use | Basic access | Parking / extended | Modern building / smart |

```c
// ESP32: Wiegand 26-bit to UART (using Wiegand-reader module with UART output)
// If using raw Wiegand (D0/D1): read pulse lengths (100 µs low = 0, 100 µs high = 1)
// For OSDP: use RS-485 adapter (MAX485) and implement OSDP state machine (complex; use library)
```

> [!warning] Wiegand Is Not Secure
> Wiegand 26-bit can be replayed with a cheap sniffer / replay device. For new installations use OSDP with AES-128 or at least DESFire with AES authentication.

## 8. Upgrade Readers: PN5180 / ST25R3911 / TRF7970A / CLRC663

See [[EN/12-Comm-Modules/20-NFC-Biometry-2.en]] for PN5180 / ST25R3911 / TRF7970A details. CLRC663 (NXP) is a legacy but stable NFC frontend with ISO/IEC 14443 / ISO/IEC 15693 / FeliCa support.

| Reader | Protocols | Power | Interface | When |
| --- | --- | --- | --- | --- |
| PN5180 | 14443A/B / 15693 / NFC-IP / FeliCa | 3.3V, TX 100+ mW | SPI + IRQ / BUSY | POS / metal / DPC |
| ST25R3911B | 14443A/B / 15693 / NFC-IP | 2.4-5.5V, low power | SPI + IRQ | Battery / antenna auto-tune |
| TRF7970A | 14443A/B / 15693 / 18000-3 / FeliCa | 2.7-5.5V, I/O 1.8-5.5V | SPI / Parallel + IRQ | R&D / universal |
| CLRC663 | 14443A/B / 15693 / FeliCa | 3.3V | SPI / I2C | Legacy / stable |

> [!tip] Migration Path: RC522 -> PN5180 / ST25R3911 (mainstream) -> TRF7970A (R&D / universal) -> CLRC663 (legacy stable). Always test antenna design with VNA.

## 9. Connection to ESP32

See [[EN/12-Comm-Modules/20-NFC-Biometry-2.en]] section 6 for VSPI / UART mapping. Key differences: Wiegand uses 2 GPIO (D0 / D1) with interrupt or polling; OSDP uses UART / RS-485; HID / UHF use UART / USB.

```text
ESP32 VSPI -> NFC frontend (PN5180 / TRF7970A / CLRC663)
ESP32 UART1 -> Wiegand-to-UART adapter or RS-485 (OSDP)
ESP32 UART2 -> HID reader (UART out) or UHF reader (UART 115200)
ESP32 UART3 -> 2D scanner / fingerprint (see 20-NFC-Biometry-2)
```

## 10. Code

```c
// ESP32 (Arduino): Mifare Classic sector 0 block 3 read (sector trailer) via MFRC522
#include <MFRC522.h>
MFRC522 mfrc522(5, 22);

void setup() { SPI.begin(); mfrc522.PCD_Init(); }
void loop() {
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    if (mfrc522.MIFARE_Read(3, trailer, 18)) {
      Serial.print("KeyA: ");
      for (byte i = 0; i < 6; i++) Serial.print(trailer[i], HEX);
    }
    mfrc522.PICC_HaltA();
  }
}
```

```python
# MicroPython: simple Wiegand 26-bit pulse parser (D0=GPIO4, D1=GPIO5)
from machine import Pin
import time

d0 = Pin(4, Pin.IN, Pin.PULL_UP)
d1 = Pin(5, Pin.IN, Pin.PULL_UP)

def parse_wiegand():
    data = 0
    for _ in range(26):
        while d0.value() == 1 and d1.value() == 1:
            time.sleep_us(10)
        if d0.value() == 0:
            data = (data << 1) | 0
        else:
            data = (data << 1) | 1
    return data
```

## 11. Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| No card detected | Antenna mismatch / metal nearby / wrong frequency | Use VNA / check antenna / add ferrite shield |
| SPI errors / phantom reads | Shared 3.3V rail / no ferrite / long wires | Separate LDO / ferrite + 10 µF + 100 nF near chip |
| Nested attack possible | Default keys / same key per sector / no rotation | Change keys / different per sector / migrate to DESFire |
| Cloned card works | T5577 / EM4305 clone / no rolling code | Use DESFire / monitor / replace with AES |
| Wiegand replay | No encryption / fixed data / cheap sniffer | Use OSDP / AES / DESFire with auth |
| UHF range low | Tag orientation / metal / water / low power | Use directional antenna / mount above door / check EIRP |

## 12. Official Sources

- Mifare Classic datasheet (NXP) — geometry, keys, access bits
- DESFire EV2/EV3 datasheet — AES, file system, key diversification
- PN5180 / ST25R3911 / TRF7970A / CLRC663 datasheets — frontend, antenna design
- ISO/IEC 14443-2 / -3 / -4 — types A / B / FeliCa / anticollision
- ISO/IEC 15693 — vicinity cards (NTAG, DESFire)
- ISO/IEC 18000-63 — UHF EPC Gen2
- OSDP IEC 60839-11-5 / SIA OSDP spec — secure RS-485
- HID Prox / Indala datasheets — 125 kHz access
- T5577 / EM4305 datasheets — LF rewritable
- FDX-B / HDX ISO 11784 / 11785 — animal identification

## 13. See Also

- [[EN/12-Comm-Modules/01-RC522-RFID.en]] - RC522 basics
- [[EN/12-Comm-Modules/20-NFC-Biometry-2.en]] - PN5180 / ST25R3911 / TRF7970A / DESFire / NTAG / fingerprint
- [[EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en]] - PN532 + fingerprint basics
- [[EN/16-Projects/03-Access-Control.en]] - Access control with DESFire + SAM
- [[04-Interfaces/02-SPI|SPI]] - SPI details
- [[04-Interfaces/01-UART|UART]] - UART details
- [[02-Power-Supply/01-Lancjugi-zhivlennya]] - Power branches
