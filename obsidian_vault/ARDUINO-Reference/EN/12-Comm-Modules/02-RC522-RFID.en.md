---
title: RC522 RFID - Card Reader over SPI
description: Explains RC522 RFID module for reading 13.56 MHz cards through SPI bus with correct power, UID and libraries; shows schematics, code and tables.
tags: [arduino, rfid, rc522, spi, card]
category: Zvyazok
lang: en
original: 12-Comm-Modules/02-RC522-RFID.md
date-created: 2026-10-05
date: 2026-10-09
---

# RC522 RFID - Card Reader over SPI

![[assets/img/arduino-rc522-scheme.png|600]]
*Fig. RC522 module with antenna, power through 3.3 V, card near coil, UID read by SPI.*

> [!tip] Purpose of this note
> Read RFID cards near the board: connect module on SPI, choose 3.3 V power, read UID with library.

## 1. Purpose

RC522 reads 13.56 MHz proximity cards; outputs UID over SPI.

Used for access control, identification, counters.

## 2. Module characteristics

| Parameter | Value | Note |
| --- | --- | --- |
| Frequency | 13.56 MHz | NFC/RFID |
| Interface | SPI | CS, MOSI, MISO, SCK |
| Power | 3.3 V | Never 5 V |
| Card type | MIFARE 1K/4K, UID 4 bytes | Most common |

## 3. Connection

| RC522 | Board |
| --- | --- |
| 3.3V | 3.3V |
| RST | Any digital |
| CS | Any digital |
| MOSI | MOSI |
| MISO | MISO |
| SCK | SCK |
| GND | GND |

## 4. Library MFRC522

Install by GitHub or library manager.

```cpp
#include <SPI.h>
#include <MFRC522.h>
MFRC522 mfrc522(10, 9); // CS, RST
void setup() { SPI.begin(); mfrc522.PCD_Init(); }
void loop() { if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) { Serial.print("UID:"); for (byte i=0; i<mfrc522.uid.size; i++) Serial.print(mfrc522.uid.uidByte[i], HEX); } }
```

## 5. UID and access

UID is unique; compare with allowed list; open only on match.

## 6. Common issues

| # | Issue | Fix |
| --- | --- | --- |
| 1 | No read | Check 3.3 V, antenna orientation |
| 2 | Wrong UID | Check card type |
| 3 | SPI error | Verify CS and RST pins |

## See also

- [[Home.en]]
- [[EN/04-Interfaces/02-SPI.en|Fast bus]]
