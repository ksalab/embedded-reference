---
title: GNSS RTK - ZED-F9P / UM980 / LC29H, Budget Modules, NTRIP on ESP32
description: GNSS RTK - centimeter navigation for ESP32: RTK receivers u-blox ZED-F9P and Unicore UM980 give 0.01 m + 1 ppm CEP accuracy in RTK Fix mode instead of 1.5-2.5 m for standard NEO-6M / NEO-M8N; covers full chain: dual-band antenna -> rover on ESP32 -> base station / NTRIP client / RTCM / NMEA / u-center / RTKLIB; shows schematics, code and tables.
tags: [esp32, gnss, rtk, zed-f9p, um980, lc29h, ntrip, rtcm, nmea, ubx, atgm336h, u-center, rtklib, base, rover, cm-level, dual-band]
category: Moduli
lang: en
original: /home/ksalab/projects/embedded-reference/ESP32-Reference/UA/12-Moduli-zvyazku/17-GNSS-RTK.md
date: 2026-10-09
date-created: 2026-09-29
---

# GNSS RTK - ZED-F9P / UM980 / LC29H, Budget Modules, NTRIP on ESP32

## Purpose

Centimeter navigation for ESP32: RTK receivers u-blox ZED-F9P and Unicore UM980 give `0.01 m + 1 ppm CEP` accuracy in RTK Fix mode instead of `1.5 - 2.5 m` for standard NEO-6M / NEO-M8N. Note covers full chain: dual-band antenna -> rover on ESP32 -> base station / NTRIP client / RTCM / NMEA / u-center / RTKLIB.

![[assets/img/gnss-rtk-rover-base.png|600]]
*Fig. RTK chain: base station (static, known position) -> RTCM corrections -> NTRIP server / local radio -> rover ESP32 + ZED-F9P -> NMEA / UBX outputs.*

Links to [[EN/Home.en]], [[EN/12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera.en]], [[EN/12-Comm-Modules/07-SIM7600-W5500-MCP2515.en]], [[04-Interfaces/02-SPI|SPI]], [[04-Interfaces/01-UART|UART]], [[02-Power-Supply/01-Lancjugi-zhivlennya]].

## Characteristics (Comparison Table)

| Module | Bands | RTK | Accuracy | Interface | When |
| --- | --- | --- | --- | --- | --- |
| u-blox ZED-F9P | L1/L2 (GPS/GLON/Gal/Bei) | Yes | 0.01 m + 1 ppm CEP | UART / SPI / USB | Rover / base, best accuracy |
| Unicore UM980 | L1/L2 / L5 (multi) | Yes | ~0.02 m | UART / USB / SPI | Budget RTK, multi-const |
| Quectel LC29H | L1/L2 / L5 | Yes | ~0.02 m | UART / USB | Low cost, good for demos |
| u-blox NEO-M8N | L1 only | No | 1.5 - 2.5 m | UART / USB | Basic navigation, no RTK |
| ATGM336H | L1 only | No | 2.5 - 3.5 m | UART | Very cheap, basic |
| NEO-6M | L1 only | No | 2.5 - 3 m | UART | Legacy, basic |

### Accuracy Modes

| Mode | Accuracy | Conditions |
| --- | --- | --- |
| Standard (autonomous) | 1.5 - 3 m CEP | No base / corrections |
| DGPS (SBAS / WAAS) | 0.5 - 1.5 m | SBAS corrections (free, via satellite) |
| RTK Float (not fixed) | 0.05 - 0.2 m | Base + rover, but not fully fixed |
| RTK Fix (full) | 0.01 - 0.02 m | High-quality base, good antenna, short baseline (<30 km) |

> [!tip] RTK Fix Requires Quality
> For 0.01 m accuracy: dual-band antenna (L1/L2), good sky view (>10 satellites, PDOP < 3), base station within 30 km, RTCM 3.2 corrections at 1 Hz, no multipath (metal / buildings nearby). In urban canyon: expect RTK Float (0.05-0.2 m) or standard.

## 1. Hardware Chain

```text
Base Station (static, known lat/lon/alt)
  -> RTK engine (ZED-F9P / UM980) -> RTCM 3.2 output ->
  => Option A: Local radio / Wi-Fi -> Rover ESP32
  => Option B: Internet / NTRIP server -> Rover ESP32 (4G / Wi-Fi)

Rover (ESP32 + ZED-F9P / UM980)
  -> UART / SPI -> NMEA / UBX -> ESP32 parses -> MQTT / LoRa / TCP -> Cloud / SCADA
```

### 1.1. Antenna Requirements

```text
Dual-band active antenna (L1 1575 MHz + L2 1227 MHz) with LNA (noise figure < 2 dB)
Cable: RG-174 / RG-58, length < 5 m (longer = signal loss)
Ground plane / choke: 100-150 mm diameter ground plane for L2; choke on cable near antenna
Mount: > 1 m above ground, clear sky view, away from metal / buildings / trees
```

> [!warning] Antenna Is 80% of Accuracy
> A cheap L1-only antenna with long cable can give 2-3 m error even with ZED-F9P. Invest in a quality dual-band antenna (e.g. u-blox ANN-MB / ANN-MB2) and short high-quality cable.

## 2. Base Station / Rover Settings

```text
Base (static, known coordinates):
  - Survey (static) -> measure coordinate with high accuracy -> save as base position
  - Output RTCM 3.2 (MSM4 / MSM7) at 1 Hz (or 5 Hz for fast movement)
  - UART / USB / Ethernet to server / radio

Rover (moving):
  - Receive RTCM 3.2 via UART / Wi-Fi / 4G / LoRa
  - Configure RTK mode (fix condition, base distance limit, elevation mask)
  - Output NMEA 0183 / UBX-RXM-RTK (fix status, lat/lon/alt, accuracy estimates)
```

```c
// ESP32 (Arduino): ZED-F9P UART init, receive NMEA, check RTK fix status
#include <HardwareSerial.h>
HardwareSerial gnss(2); // RX=16, TX=17 (or UART2 default)

void setup() {
  gnss.begin(9600, SERIAL_8N1, 16, 17);
  // Send UBX-CFG-RTCM to enable RTCM input (if using NTRIP / local radio)
}

void loop() {
  if (gnss.available()) {
    String s = gnss.readStringUntil('\n');
    if (s.indexOf("GNGGA") >= 0) {
      // Parse GGA for fix quality (0=none, 1=GPS, 2=DGPS, 4=RTK Fixed, 5=RTK Float)
    }
  }
}
```

### 2.1. NTRIP Client on ESP32

```python
# MicroPython: NTRIP client (simplified; use u-modbus / ntrip-client library for full)
import socket, time

def ntrip_connect(host, port, mountpoint, user, passwd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(f"GET /{mountpoint} HTTP/1.1\r\nHost: {host}\r\nNtrip-Version: Ntrip/2.0\r\nAuthorization: Basic {base64}\r\n\r\n")
    # Read RTCM stream -> send to ZED-F9P UART
    return s
```

> [!tip] NTRIP Servers (Free / Paid)
> Free: RTK2go (global, limited), EUREF (EU), state networks (US: NOAA / CORS). Paid: Trimble RTX, u-blox PointPerfect, local providers. For demo: RTK2go with base at known coordinate; for production: use local base / paid NTRIP.

## 3. RTCM 3.2 / NMEA / UBX

```text
RTCM 3.2 message types (key):
  1073 / 1074 / 1075 / 1076 / 1077: GPS / GLON / GAL / Bei / SBAS MSM4 observations
  1005 / 1006: Station coordinates / antenna info (base)
  1008 / 1033: Antenna description / station info
  1230: GLONASS code / phase biases

NMEA 0183 (key sentences):
  GNGGA: Fix quality, lat/lon, HDOP, sats, age
  GNGSA: Sat info / DOP
  GNRMC: Recommended minimum (speed, course, date/time, lat/lon)
  GNVTG: Track / speed over ground
```

## 4. u-center / RTKLIB / Post-Processing

- u-center (Windows): u-blox config tool for ZED-F9P settings, firmware update, survey
- RTKLIB / RTKPOST (Windows/Linux): post-process static / kinematic data with base RINEX
- Ubx-Cfg-Rst / Ubx-Cfg-Rate: configure message rates, output formats

> [!tip] Survey Before RTK
> For a static base: collect 24h of data, process with RTKLIB / OPUS / PPP service -> get accurate base coordinate -> use for all rover operations. Without accurate base: all rover data has systematic error.

## 5. ESP32 Integration (GPIO Mapping)

```text
ZED-F9P / UM980 UART to ESP32:
  GPS_TX  -> ESP32 UART2_RX (GPIO16)  [9600 / 115200 baud]
  GPS_RX  <- ESP32 UART2_TX (GPIO17)  [UBX commands / RTCM input]
  GPS_VCC -> 3.3V (separate LDO, ferrite + 10 µF)
  GPS_GND -> GND
  GPS_PPS (1 Hz) -> ESP32 GPIO18 (optional, for time sync)

NTRIP / Wi-Fi / 4G:
  ESP32 Wi-Fi -> Internet -> NTRIP server -> RTCM -> UART to GPS
  ESP32 4G (SIM7600) -> Internet -> NTRIP
```

## 6. Budget Options (2026)

| Module | Price (USD) | Notes |
| --- | --- | --- |
| Quectel LC29H | 30-50 | Multi-band, RTK, good for demo |
| Unicore UM980 | 60-100 | Good accuracy, low cost vs ZED-F9P |
| u-blox ZED-F9P | 150-250 | Best, industrial, dual-band |
| ATGM336H / NEO-M8N | 10-30 | Basic, no RTK |
| ESP32-S3 + ZED-F9P + ESP32-C3 (base) | 200 + 50 | Full chain, Wi-Fi / 4G |

## References

- u-blox ZED-F9P datasheet
- Unicore UM980 datasheet
- ISO / RTCM spec 3.2
- u-center user guide
- RTKLIB manual
- NTRIP spec / RTK2go
- ESP32 UART / SPI / Wi-Fi docs
