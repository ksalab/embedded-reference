---
title: NFC-Biometry-2 - Powerful Frontends PN5180/ST25R3911/TRF7970A, DESFire, NTAG21x, GT-521F32/DE2120/YHD-M200
description: NFC-Biometry-2 - powerful frontends, DESFire, NTAG21x, fingerprints and scanners - powerful NFC frontends: PN5180 / ST25R3911 / TRF7970A; 1. Comparison with RC522; 2. DPC - why this is the key word of the note; shows schematics, code and tables.
tags: [esp32, nfc, pn5180, st25r3911, trf7970a, desfire, aes, ntag213, ntag215, ntag216, gt-521f32, fingerprint, de2120, yhd-m200, barcode, biometry]
category: Moduli
lang: en
original: /home/ksalab/projects/embedded-reference/ESP32-Reference/UA/12-Moduli-zvyazku/20-NFC-Biometry-2.md
date: 2026-10-09
date-created: 2026-09-29
---

# NFC-Biometry-2 - Strong Frontends, DESFire, NTAG21x, Fingerprints and Scanners

> [!info] Purpose
> This note is the second part of NFC / biometrics (continuation of [[EN/12-Comm-Modules/01-RC522-RFID.en]], [[EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en]] and [[EN/12-Comm-Modules/15-RFID-Advanced.en]]): powerful NFC frontends **PN5180 / ST25R3911 / TRF7970A** with DPC and comparison with RC522, secured cards **DESFire** (AES, file system, balance reading), mass tags **NTAG21x** (password, lock bits), fingerprint scanners **GT-521F32** and 2D scanners **DE2120 / YHD-M200**, plus a summary table "reader -> task".

![[assets/img/nfc-biometry-2-scheme.png|600]]
*Fig. ESP32 with a powerful NFC frontend (SPI) reads DESFire / NTAG; fingerprint scanner and 2D scanner hang on UART — all three provide an "ID" for access control.*

Links to [[EN/Home.en]], [[EN/12-Comm-Modules/01-RC522-RFID.en]], [[EN/12-Comm-Modules/15-RFID-Advanced.en]], [[EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en]], [[EN/12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera.en]], [[EN/12-Comm-Modules/19-Wired-2.en]], [[04-Interfaces/02-SPI|SPI]], [[04-Interfaces/01-UART|UART]], [[02-Power-Supply/01-Lancjugi-zhivlennya]].

Characteristics (comparison table):

| Node | Type | Interface to ESP32 | Power | Range / Capacity | When to use |
| --- | --- | --- | --- | --- | --- |
| PN5180 | NFC frontend, all modes | SPI to 7 MHz + IRQ / BUSY | 3.3V, TX up to 100+ mW | up to 10 cm, EMVCo L1 | POS / turnstile, metal nearby, power needed |
| ST25R3911B | NFC frontend, auto-tune antenna | SPI + IRQ | 2.4 - 5.5V | up to 8 cm, low consumption | Battery readers, complex antenna |
| TRF7970A | Multi-protocol transceiver | SPI / Parallel + IRQ | 2.7 - 5.5V, I/O 1.8 - 5.5V | 106 - 848 kbps, all tags 1 - 5 | Universal R&D reader, card emulation |
| RC522 (base) | MFRC522, only 14443A | SPI to 10 MHz | 3.3V | 3 - 5 cm | Cheap and simple; see [[EN/12-Comm-Modules/01-RC522-RFID.en]] |
| DESFire EV2 / EV3 | Secured smart card | via frontend 13.56 MHz | passive (field) | 2 - 8 KB files, AES / DES / 3DES | Money / access / transport - balance in file |
| NTAG213 / 215 / 216 | NFC Type 2 tag | via frontend 13.56 MHz | passive (field) | 144 / 504 / 888 bytes, 32-bit password | Business cards, Wi-Fi pairing, seals, posters |
| GT-521F32 | Optical fingerprint scanner | UART 9600 (3.3V TTL!) | 3.3 - 6V, <130 mA | 200 templates in module | Doors / safe without PC, 1:N in module |
| DE2120 / YHD-M200 | 2D barcode / QR scanner | UART 9600 / USB-HID | 5V (backlight ~200 mA) | 5 - 30 cm | Tickets, warehouse, QR payment |

## Purpose

NFC-Biometry-2 - strong frontends, DESFire, NTAG21x, fingerprints and scanners - strong NFC frontends: PN5180 / ST25R3911 / TRF7970A; 1. Comparison with RC522; 2. DPC - why this is the key word of the note. NFC-Biometry-2 - strong frontends, DESFire, NTAG21x, fingerprints and scanners. Links to Home, EN/12-Comm-Modules/01-RC522-RFID.en, EN/12-Comm-Modules/15-RFID-Advanced.en, EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en, EN/12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera.en, EN/12-Comm-Modules/19-Wired-2.en, [[04-Interfaces/02-SPI|SPI]], [[04-Interfaces/01-UART|UART]], [[02-Power-Supply/01-Lancjugi-zhivlennya]].

## 1. Strong NFC Frontends: PN5180 / ST25R3911 / TRF7970A

RC522 (MFRC522) is a 14443A-only chip from the 2000s with fixed power and sensitivity "whatever the antenna gives". Strong frontends solve three pains: **range / stability in metal**, **all protocols** (B, FeliCa, V / 15693), **auto-tuning** (DPC / AWC / antenna calibration).

### 1.1. Comparison with RC522

| Criterion | RC522 (MFRC522) | PN5180 (NXP) | ST25R3911B (ST) | TRF7970A (TI) |
| --- | --- | --- | --- | --- |
| Protocols | 14443A | A / B, FeliCa, 15693, 18000-3m3, NFC-IP | A / B, F, V, NFC-IP | A / B, 15693, 18000-3, FeliCa |
| TX Power | fixed, weak | programmable + **DPC** | programmable + auto-tune | +20 / +23 dBm programmable |
| DPC / AWC | none | **DPC** (dynamic power) + AWC (waveform) | automatic antenna tuning | RSSI + dual receiver |
| Speed | up to 848 kbps (A) | up to 848 kbps | up to 848 kbps | 106 - 848 kbps |
| Host I/F | SPI / I2C / UART | SPI to 7 MHz + IRQ + BUSY | SPI + IRQ | SPI / Parallel + IRQ, FIFO 127 B |
| Power | 3.3V | 3.3V | 2.4 - 5.5V | 2.7 - 5.5V, I/O 1.8 - 5.5V |
| Price / complexity | $1, library everywhere | €€, NFC Reader Library | €, ST Cockpit / library | €, detailed TI appnotes |
| When | toys, prototypes | POS, EMVCo L1, metal | battery, complex antenna | R&D, card emulation, all tags |

### 1.2. DPC - Why This Is the Key Word of the Note

**DPC (Dynamic Power Control)** in PN5180: the frontend firmware measures antenna detuning in real time (card in field / metal nearby changes impedance) and adjusts output power and waveform (AWC) so the field stays within EMVCo tolerances. Without DPC: card on a metal turnstile "sometimes reads, sometimes not". With DPC: stable transactions on a detuned antenna. For ESP32 this means: heavy RF work is done by PN5180 itself; the host only sends commands over SPI — no real-time from our side.

ST25R3911B hits the other side: **automatic antenna calibration** (capacitive DACs for tuning), amplitude / phase measurement, ultra-low-power card-detection mode (negligibly small current in sleep — ideal for a battery reader that wakes on a card).

TRF7970A is the most universal for development: direct modes (raw subcarrier), built-in codecs for all protocols, RSSI from two receivers (no "dead zones"), I/O voltage 1.8 - 5.5V (friendly with any ESP32 without level shifters), detailed TI appnotes including a DESFire-AES example.

### 1.3. Connecting the Frontend to ESP32 (SPI)

All three are SPI-slave + IRQ (DIO). Mapping on VSPI classic: SCK = GPIO18, MISO = GPIO19, MOSI = GPIO23, NSS = GPIO5, IRQ = GPIO21, RST = GPIO22. PN5180 additionally has a **BUSY** line (module busy — do not send SPI!). Frontend power is a separate 3.3V branch with ferrite + 10 µF + 100 nF near the chip: TX current spikes bring down the shared bus and cause "phantom" SPI errors.

> [!warning] Antenna Is Half the Device
> Frontend without a matched 13.56 MHz antenna = expensive RC522. Follow manufacturer guides (PN5180 Antenna Design Guide, TRF79xxA Antenna Guide): target impedance, Q-factor, distance to metal >= 5 mm or ferrite shield. Check with VNA or at least range measurement with a reference card.

### PN7150 / PN7120 - NCI Controllers for Linux-Like Hosts

| Parameter | PN7150 / PN7120 |
| --- | --- |
| Protocols | Reader / Writer + P2P + card emulation (NCI stack) |
| Interface | I2C + IRQ + VEN (power control) |
| Power | 3.3 V (OM5578 board with antenna out of the box) |
| When to use | Card emulation / P2P with phone needed - something RC522 / PN532 do not do comfortably |

```text
ESP32 GPIO21 (SDA) ──► SDA PN7150 (pull-up 4.7k)
ESP32 GPIO22 (SCL) ──► SCL (pull-up 4.7k)
ESP32 GPIO5 ──► VEN (HIGH = working, LOW = power-down)
ESP32 GPIO4 ◄── IRQ (card in field!)
```

> PN7150 vs PN532: PN532 is cheaper for UID / NDEF reading; PN7150 — when card emulation or a stable NCI driver is needed (Linux example `nfcpy` ports almost 1-to-1).

![[assets/img/pn7150-i2c-scheme.png|500]]
*Fig. PN7150: I2C with pull-up, VEN for power on, IRQ for card detection.*

## 2. DESFire - AES, Files, Balance Reading

**Mifare DESFire** (EV2 / EV3) is no longer "memory blocks" but a **file OS on the card**: Applications (AID 3 bytes) → Files (File ID) → AES-128 / DES / 3DES keys at each level (Master Key of card, Master Key of application, read / write file keys). Without key authentication the data is not given — cloning without a key is impossible (unlike Classic / Ultralight without a password).

### 2.1. File Types

| Type | ID | Purpose | Balance Example |
| --- | --- | --- | --- |
| Standard Data File | 0x00 | Arbitrary bytes R / W | JSON profile, ticket |
| Backup Data File | 0x01 | Like standard + transactional | Critical writes |
| **Value File** | 0x02 | **Money counter**: Credit / Debit / LimitedCredit, GetValue | **Wallet balance** |
| Linear Record File | 0x03 | Fixed circular log | Trip history (last N) |
| Cyclic Record File | 0x04 | Circular log | Access journal |

### 2.2. Balance Reading Session (Step Diagram)

```text
1. REQA / WUPA + Anticollision + Select        -> UID (ISO14443-3)
2. RATS / PPS                                -> ATS, speed selection (ISO14443-4)
3. SelectApplication(AID of wallet, e.g. 0x112233)
4. AuthenticateAES(KeyNo=1, Key=diversified read key)
     card <-> host: challenge-response AES-128 -> Session Key
5. ReadData / GetValue(FileNo=0x01)
     response ENCRYPTED with session key (CommMode ENC)
6. Decrypt -> balance (least significant byte first, e.g. 0x000004D2 = 1234 kopecks)
```

> [!warning] Keys Do Not Live in ESP32 in Open Form
> Master keys from the issuer — only in SAM module / secure storage. In ESP32 — only **diversified** keys (K = AES_MK(UID)), unique per card: compromise of one device does not collapse the whole system. For production — see [[EN/16-Projects/03-Access-Control.en]].

### 2.3. DESFire vs NTAG vs Classic - When What

| Feature | DESFire EV2/EV3 | NTAG213/215/216 | MIFARE Classic 1K/4K |
| --- | --- | --- | --- |
| Crypto | AES-128 / 3DES, file-level keys | 32-bit PWD, lock bits (no crypto) | 48-bit key per sector (weak) |
| Storage | 2 - 8 KB files, structured | 144 / 504 / 888 bytes | 1 / 4 KB |
| Reading balance | Yes (Value File + AES session) | No (only UID / URL / text) | No |
| Clone resistance | Very high (key diversification) | Low (PWD replay possible) | Low (key recovery known) |
| Cost / complexity | €€€ / SAM needed | € / simple | € / simple |
| When | Payments, access, transport | Business cards, Wi-Fi pairing, tags | Legacy, cheap prototypes |

## 3. NTAG21x - Password, Lock Bits, NDEF

NTAG213 (144 B), NTAG215 (504 B), NTAG216 (888 B) are Type 2 tags with a simple memory layout: 4-byte UID + 2 B OTP / internal + 16 B Capability Container + (N - 16) B user memory + 2 B lock / mirror + 2 B dynamic lock bytes. The security model is minimal but sufficient for tags: **32-bit password (PWD)** and **lock bits (LB)** that permanently block writes to selected pages.

### 3.1. Password Authentication Flow

```text
1. Send PWD_AUTH (0x1B) + PWD[4 bytes] -> card responds with PACK[2 bytes]
2. Verify PACK == CRC16(PWD) -> session open for 30 s (default)
3. Read pages 4..39 via READ (0x30) or FAST_READ
4. Lock pages via WRITE to Lock/Page (0x00 / 0x01 / ... depending on tag)
```

> [!tip] Lock Bits Are Permanent
> Once a lock bit is set to 1, that page becomes read-only forever (even with PWD). Plan the tag layout before writing: write static data (URL, URI) to locked pages, keep dynamic data to unlockable pages.

### 3.2. NDEF URI Record Example

```text
Record Type Name: "U" (URI)
Payload: 0x01 (http://) + "example.com/access?card=1234"
Total: 1 (type) + 1 (payload len) + 23 (payload) = 25 bytes on page 4
```

```c
// ESP32 (Arduino): NTAG PWD_AUTH and page read via PN5180 / compatible frontend
#include <MFRC522.h>  // transport example; for PN5180 use NXP library
MFRC522 mf(5, 22);

bool ntag_pwd_auth(const uint8_t pwd[4], uint8_t *pack) {
    byte cmd[] = { 0x1B, pwd[0], pwd[1], pwd[2], pwd[3] };
    mf.PCD_WriteRegister(0x00, 0x01);
    // ... crypto and response parsing omitted for brevity
    return true;
}
```

> For production with many tags: do not hard-code PWD in ESP32 firmware. Derive from a device secret + tag UID (K = AES_MK(UID)), same principle as DESFire.

## 4. GT-521F32 - Fingerprint Scanner by UART

GT-521F32 is an optical fingerprint module with an internal template storage (200 fingerprints) and 1:N identification directly on the module. Communication: UART 9600 baud, 3.3V TTL (not RS-232!). Power: 3.3 - 6V, peak <130 mA during LED / scan. Interface is packet-based: 55 AA | DEV (2) | PARAM (4 LE) | CMD (2 LE) | SUM (2 LE).

### 4.1. Packet Structure

```text
Header: 55 AA
Device ID: 2 bytes (01 00 for GT-521F32)
Parameter length: 4 bytes LE (e.g. 00 00 00 03 = 3 params)
Parameters: variable (e.g. 01 00 03 00 = ID 3)
Command: 2 bytes LE (e.g. 01 00 = Open)
Checksum: SUM of all previous bytes (mod 256)
```

```cpp
// Arduino (ESP32): GT-521F32 over UART2 9600. Open -> LED on -> Identify.
// Packet: 55 AA | DEV(2) | PARAM(4 LE) | CMD(2 LE) | SUM(2 LE).
#include <HardwareSerial.h>
HardwareSerial fps(2);  // RX=16 TX=17

static uint16_t fps_sum(const uint8_t *b, int n) {
  uint16_t s = 0;
  for (int i = 0; i < n; i++) s += b[i];
  return s & 0xFFFF;
}
```

> [!warning] 3.3V TTL — Not 5V RS-232
> GT-521F32 uses 3.3V logic levels. If powering from 5V, use a voltage divider on ESP32 RX, or a level shifter module. UART 9600 is fixed; do not change baud without factory reset.

### 4.2. Identification Flow (1:N)

```text
1. Open -> LED on -> capture fingerprint (finger on glass)
2. Identify (CMD 0x02, Param 0x0001) -> module compares with stored 200 templates
3. Response: 55 AA | DEV | PARAM | CMD | RESULT (0 = success) + Template ID (2 bytes LE)
4. If success -> ESP32 decides access; if fail -> retry or alarm
```

## 5. DE2120 / YHD-M200 - 2D Barcode Scanners

DE2120 (USB-HID / UART) and YHD-M200 (UART / USB-HID) are 2D scanners for barcodes and QR codes. Interface: UART 9600 or USB-HID (appears as keyboard). Power: 5V, backlight ~200 mA. Range: 5 - 30 cm depending on code size. For ESP32: connect UART to any UART pin (e.g. UART1: RX=25, TX=26) or use USB-HID via USB-OTG (complex).

### 5.1. UART Mode Configuration

```c
// ESP-IDF / Arduino: 2D scanner UART init, 9600 8N1, trigger line to signal new scan
#include <HardwareSerial.h>
HardwareSerial scan(1);  // RX=25, TX=26 on ESP32

void setup() {
  scan.begin(9600, SERIAL_8N1, 25, 26);
  pinMode(4, OUTPUT); digitalWrite(4, HIGH); // trigger / buzzer
}

void loop() {
  if (scan.available()) {
    String s = scan.readStringUntil('\r'); // most scanners end with CR
    if (s.length() > 3) process_code(s);
  }
}
```

> [!tip] USB-HID Is Easier for No-Code Projects
> If the ESP32 board has USB-OTG (e.g. ESP32-S2 / S3 / C3 with USB), connect scanner via USB and use `USBHost` or `tusb` library — scanner appears as keyboard, no UART wiring needed. For UART mode: check scanner manual for factory reset to 9600 if it came with different settings.

## 6. Integration Diagram (ESP32 + All Modules)

```mermaid
graph LR
    ESP32[ESP32<br/>VSPI + 2×UART] -->|SPI + IRQ / BUSY| FE[PN5180 / ST25R3911<br/>TRF7970A frontend]
    FE -->|13.56 MHz field| CARD1((DESFire<br/>AES wallet))
    FE -->|13.56 MHz field| CARD2((NTAG21x<br/>PWD + lock))
    ESP32 -->|UART2 9600| FPS[GT-521F32<br/>200 templates]
    ESP32 -->|UART1 9600| SCAN[DE2120 / YHD-M200<br/>2D scanner]
    ESP32 -->|UART3 9600 / USB-HID| CELL[Cellular / LoRa<br/>(if remote access needed)]
```

### 6.1. VSPI Pin Mapping (Classic)

```text
ESP32 DevKit           NFC / Biometry Modules
─────────────           ────────────────────
VSPI:
  GPIO18 SCK  ─────────►  SCK
  GPIO23 MOSI ─────────►  MOSI
  GPIO19 MISO ◄─────────  MISO
  GPIO5 NSS  ─────────►  NSS (PN5180 / TRF7970A)
  GPIO21 IRQ  ◄─────────  IRQ (card detected / busy / ready)
  GPIO22 BUSY ◄─────────  BUSY (PN5180 only — do not send SPI when HIGH)
  GPIO22 RST  ─────────►  RST (optional, or shared with BUSY via jumper)
  GPIO15     ─────────►  ANT / DPC tuning (if antenna board supports)

UART2 (fingerprint):
  GPIO16  ◄──────────── RX (GT-521F32 TX)
  GPIO17  ────────────► TX (GT-521F32 RX)

UART1 (scanner):
  GPIO25  ◄──────────── RX (DE2120 TX)
  GPIO26  ────────────► TX (DE2120 RX)

UART3 (cellular / LoRa):
  GPIO27  ◄──────────── RX
  GPIO14  ────────────► TX
```

### 6.2. Power Branches (Separate!)

```text
3.3V Main (ESP32)  ──┬──► ESP32 board (max ~500 mA with Wi-Fi)
                     ├──► PN5180 / TRF7970A frontend (separate 3.3V, ferrite + 10 µF + 100 nF)
                     └──► GT-521F32 (3.3V when powered from ESP32 rail, but peak ~130 mA — check rail)

5V External (USB / adapter)  ──┬──► DE2120 / YHD-M200 (5V, backlight ~200 mA)
                                └──► GT-521F32 (5V input, internal LDO to 3.3V for logic)

GND Common  ──► All modules must share GND (star topology from ESP32 GND pin, not through long thin traces)
```

> [!warning] Power Separation Is Critical
> TX spikes from PN5180 (up to 100 mW, ~30 mA peak) bring down a weak 3.3V rail and cause SPI errors or RFID read failures. Always use a separate LDO or at least a ferrite + 10 µF + 100 nF filter right at the frontend VCC pin. Measure with oscilloscope during TX: rail should stay within 3.3 ± 0.15 V.

## 7. MicroPython Example (Fingerprint + NFC + Scanner)

```python
"""MicroPython (ESP32): fingerprint on UART2 + 2D scanner on UART1."""
from machine import UART, Pin
import struct, time

fps = UART(2, baudrate=9600, rx=16, tx=17)
scan = UART(1, baudrate=9600, rx=25, tx=26)
trig = Pin(4, Pin.OUT, value=1)

def fps_packet(cmd, param=0):
    dev = struct.pack("<H", 0x01)
    param_bytes = struct.pack("<I", param)
    cmd_bytes = struct.pack("<H", cmd)
    payload = dev + param_bytes + cmd_bytes
    s = sum(payload) & 0xFFFF
    return bytes([0x55, 0xAA]) + payload + struct.pack("<H", s)

def read_scan():
    if scan.any():
        s = scan.read().decode("ascii", "ignore")
        return s.strip()
    return None

# Main loop: identify fingerprint, if OK read scanner code, if OK open access
while True:
    fps.write(fps_packet(0x01, 0x01))  # Open
    time.sleep(0.5)
    # ... fingerprint identification parsing omitted for brevity
    code = read_scan()
    if code:
        print("Access granted with code:", code)
    time.sleep(0.1)
```

### 7.1. NTAG Page Read (MicroPython)

```python
"""MicroPython: read NDEF from NTAG via compatible driver (pseudo-API).
READ pages 4..39, search TLV 0x03 (NDEF), length, URI record."""
def read_ntag_pages(ntag, start=4, end=39):
    raw = b""
    for page in range(start, end + 1, 4):
        raw += ntag.read_page(page)   # 16 B: 4 pages
    # Search TLV 0x03 at offset after Capability Container
    offs = raw.find(b"\x03")
    if offs >= 0:
        length = raw[offs + 1]
        uri = raw[offs + 2 : offs + 2 + length]
        return uri
    return b""
```

## 8. Summary Table (Reader -> Task)

| Task | Best Module | Why | Notes |
| --- | --- | --- | --- |
| POS / turnstile with metal | PN5180 + DPC | Dynamic power / auto-tune | Needs matched antenna |
| Battery reader, complex antenna | ST25R3911B | Ultra-low sleep current | Auto-tune capacitive |
| Universal R&D / card emulation | TRF7970A | All protocols / raw modes / 1.8V I/O | Detailed appnotes |
| Cheap prototype / UID only | RC522 | $1, library everywhere | No DPC, weak in metal |
| Balance / wallet / access card | DESFire EV2/EV3 + SAM | AES, file system, key diversification | Master keys in SAM only |
| Business card / Wi-Fi pairing | NTAG215 / 216 | Large storage, PWD + lock | Lock bits permanent |
| Door / safe fingerprint | GT-521F32 | 200 templates, 1:N on module | 3.3V TTL UART 9600 |
| Ticket / warehouse QR scan | DE2120 / YHD-M200 | 2D, 5-30 cm range | 5V USB-HID or UART |
| Remote access / logging | ESP32 + Cellular / LoRa | Send ID + event to cloud | Use [[EN/12-Comm-Modules/18-Cellular-LoRa-2.en]] for module choice |

## References

- [[EN/12-Comm-Modules/01-RC522-RFID.en]] - RC522 base comparison
- [[EN/12-Comm-Modules/15-RFID-Advanced.en]] - Advanced RFID (DESFire, NTAG, security)
- [[EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en]] - PN532 + fingerprint + barcode basics
- [[EN/12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera.en]] - Camera / Ethernet for remote access
- [[EN/12-Comm-Modules/19-Wired-2.en]] - Wired interfaces (SPI / UART / I2C mapping)
- [[04-Interfaces/02-SPI|SPI]] - SPI interface details
- [[04-Interfaces/01-UART|UART]] - UART interface details
- [[02-Power-Supply/01-Lancjugi-zhivlennya]] - Power supply branches
- [[EN/16-Projects/03-Access-Control.en]] - Access control project with DESFire + SAM
