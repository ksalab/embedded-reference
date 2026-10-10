---
title: WebRadio and Streaming on ESP32 - Icecast/Shoutcast, AAC, Buffers, Squeezelite, Snapcast, AirPlay, DLNA, VS1053, PSRAM
description: This note - network audio on ESP32: internet radio (MP3/AAC stream from Icecast/Shoutcast servers), multi-room sync (multiple speakers play same), receiving sound from phone / laptop (AirPlay, DLNA), decoding with VS1053, buffering with PSRAM.
tags: [esp32, vivid, webradio, icecast, shoutcast, streaming, mp3, aac, helix, psram, squeezelite, lms, snapcast, airplay, shairport, dlna, vs1053, i2s, audio, buffer]
category: Vivid
date-created: 2026-09-29
lang: en
original: 11-Vivid/19-WebRadio-Streaming.md
date: 2026-10-08
---

# WebRadio and Streaming on ESP32 - Icecast/Shoutcast, AAC, Buffers, Squeezelite, Snapcast, AirPlay, DLNA, VS1053, PSRAM

> [!info] Where this is
> Sound base: [[04-Interfaces/04-I2S.en.md|I2S]], simpler solution [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.en.md|DFPlayer/MAX98357A]], codecs [[11-Vivid/13-Audio-Codecs.en.md|Audio-Codecs]], MP3/TTS [[11-Vivid/18-MP3-TTS-Amps.en.md|MP3/TTS/Amps]], start [[Home.en.md|Home]].

## Purpose

Network audio on ESP32: play internet radio streams (MP3/AAC from public Icecast/Shoutcast servers), multi-room sync (several ESP32 speakers play the same stream synchronized), receive audio from phone / laptop (AirPlay, DLNA), decode MP3 with VS1053, and manage buffers in PSRAM for smooth playback.

When to choose:
- internet radio station - ESP32 + WiFi + VS1053 or software decoder;
- multi-room sync - Snapcast or Squeezelite + ESP32 clients;
- receive from Apple/Android - AirPlay (Shairport) or DLNA renderer;
- high-quality decode - VS1053 (hardware MP3 decoder);
- large buffer for high-bitrate streams - PSRAM (8/16 MB).

When NOT: just play local files - see [[11-Vivid/18-MP3-TTS-Amps.en.md]]; need codec/I2S sound - see [[11-Vivid/13-Audio-Codecs.en.md]].

## Key parameters

| Parameter | Typical value | Note |
| --- | --- | --- |
| Stream format | MP3 / AAC / OGG | AAC needs decoder (ESP32 can software-decode, or use VS1053) |
| Bitrate | 32-320 kbps | Higher = larger buffer; 128 kbps ~1 MB/min |
| Buffer | 2-10 KB (SMALL) / 100-500 KB (MEDIUM) / 2-8 MB (LARGE, PSRAM) | Large buffers prevent dropout on WiFi jitter |
| Network | WiFi 2.4 GHz | Use static IP or mDNS; keep signal > -70 dBm |
| Sync protocol | Snapcast / Squeezelite + Logitech Media Server (LMS) | Snapcast uses TCP stream; Squeezelite uses Logitech protocol |
| AirPlay | Shairport-on-ESP32 or AirPlay receiver software | Timing-sensitive; use dedicated library |
| DLNA | DLNA renderer library (ESP32) | Discoverable via SSDP; play from server |
| VS1053 | Hardware MP3 decoder (SPI) | Decodes MP3 in real-time; outputs I2S to ESP32 or amplifier |

## Icecast / Shoutcast streams

```cpp
// Simple HTTP stream read (ESP-IDF / Arduino)
#include <WiFi.h>
#include <HTTPClient.h>

String url = "http://icecast.radiofrance.fr/franceinter-hifi.mp3";
HTTPClient http;
http.begin(url);
int code = http.GET();
// Read chunks into buffer; feed to VS1053 or software decoder
```

> [!tip] Public streams
> Icecast directory (icecast.org) lists stations with URL and bitrate. Shoutcast (shoutcast.com) also provides streams. Use `http://` not `https://` for simplicity; some require `User-Agent` header.

## AAC streams

AAC (Advanced Audio Coding) is more efficient than MP3; ESP32 can decode AAC in software (libfaad / AAC decoder in ESP-ADF), but CPU usage is high. For reliable play, use VS1053 (hardware MP3/AAC?) or software decode with sufficient buffer and CPU headroom.

```cpp
// Buffer management for AAC
#define BUFFER_SIZE 4096
uint8_t buffer[BUFFER_SIZE];
// Read from stream; fill buffer; feed decoder; clear when played
```

## Buffering and PSRAM

- Small buffer (2-10 KB): enough for stable WiFi; dropout on jitter.
- Medium (100-500 KB): handles 30-60 s WiFi interruption; needs more RAM.
- Large (2-8 MB): best for high-bitrate / unstable networks; requires PSRAM (ESP32-WROVER / ESP32-S3 with PSRAM).

```cpp
// PSRAM usage (ESP32 with 8 MB PSRAM)
#include <esp_heap_caps.h>
void* buf = heap_caps_malloc(2*1024*1024, MALLOC_CAP_SPIRAM); // 2 MB in PSRAM
```

## Squeezelite / LMS multi-room

Squeezelite runs on ESP32 as a Logitech Media Server client; LMS manages library and sync. ESP32 runs Squeezelite + I2S output to amplifier/codec.

```cpp
// Conceptual setup: ESP32 connects to LMS server; plays synchronized
// Use squeezelite-esp32 port or build with ESP-IDF + LMS protocol
```

> [!tip] Sync precision
> Snapcast uses TCP audio stream + timing packets; clients adjust delay so all speakers play in sync (within ~10 ms). Requires network latency measurement.

## Snapcast

Snapcast server (on PC / Raspberry Pi) reads stream and distributes to clients (ESP32). ESP32 connects via TCP, receives PCM / WAV, outputs via I2S.

## AirPlay / DLNA

- AirPlay: ESP32 runs Shairport or AirPlay receiver; iPhone / Mac detects; sends audio.
- DLNA: ESP32 exposes renderer; phone / PC discovers; plays to ESP32.

```cpp
// DLNA renderer concept
// Start SSDP; advertise device; listen for play commands; stream from server URL
```

## VS1053 hardware decoder

```cpp
// VS1053 via SPI to ESP32
#include <SPI.h>
#include <VS1053.h>

VS1053 player(VS1053_CS, VS1053_DCS, VS1053_DREQ);
player.begin();
// Feed MP3 bytes to VS1053 via SPI; output I2S from VS1053 to EP32 or amp
```

> [!tip] VS1053 outputs I2S
> VS1053 can output I2S directly to ESP32 I2S input or to external I2S amplifier; reduces ESP32 CPU load.

## Common issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| Stream stops after 10-30 s | WiFi dropout; buffer empty; server timeout | increase buffer; check WiFi signal; use reliable server |
| Audio dropout / crackle | buffer too small; network jitter; high bitrate | increase buffer (PSRAM); lower bitrate; use wired if possible |
| Not synchronized with other speakers | different network latency; no time sync | use Snapcast / Squeezelite with timing; ensure same network |
| AirPlay not discovered | mDNS / Bonjour issue; firewall | enable mDNS; check firewall / router settings |
| DLNA not found | SSDP blocked; wrong interface | ensure WiFi interface; open UDP 1900 |
| VS1053 no output | SPI miswired; missing clock; wrong mode | verify SPI pins; set to MP3 mode; check DREQ |

## Official sources

- [Icecast directory](https://icecast.org) - station directory with URLs.
- [Shoutcast directory](https://www.shoutcast.com) - station directory.
- [Snapcast documentation](https://github.com/badaix/snapcast) - multi-room sync.
- [Squeezelite / Logitech Media Server](https://github.com/ralphirving/squeezelite) - LMS client.
- [VS1053 datasheet (VLSI)](https://www.vlsi.fi/en/products/vs1053.html) - hardware MP3 decoder.
- [AirPlay / Shairport](https://github.com/mikebrady/shairport-sync) - AirPlay receiver.
- [ESP-ADF Streaming examples](https://docs.espressif.com/projects/esp-adf/en/latest/) - network audio pipeline.

## See also

- [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.en.md|DFPlayer / MAX98357A]] - simpler audio.
- [[11-Vivid/13-Audio-Codecs.en.md|Audio Codecs]] - I2S codec sound.
- [[11-Vivid/18-MP3-TTS-Amps.en.md|MP3 / TTS / Amps]] - local MP3 and amplifiers.
- [[04-Interfaces/04-I2S.en.md|I2S]] - digital sound interface.
