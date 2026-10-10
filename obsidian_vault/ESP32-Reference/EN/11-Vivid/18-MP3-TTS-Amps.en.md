---
title: MP3 Modules, TTS Speech Synthesis and Amplifiers - JQ6500/KT403A/BY8301/DY-SV5W/SOMO-14D, SYN6288/XFS5152, PAM8403/TPA3116/LM386, MAX4466/MAX9814, MSGEQ7, PT2399
description: This note is "big sound" on ESP32 without I2S codecs: autonomous MP3 playback from SD (entrance, museum, toy, alarm), text-to-speech (station announcements, voice assistant in English via pinyin/translit), boosting sound to speaker (0.5 W buzzer to 50 W sub), microphone amplification (intercom, noise meter, voice control), spectrum visualization (color music, VU meter 7 bands), and echo/reverb (karaoke, intercom, effects).
tags: [esp32, vivid, mp3, jq6500, kt403a, by8301, dy-sv5w, somo-14d, tts, syn6288, xfs5152, pam8403, tpa3116, lm386, max4466, max9814, msgeq7, pt2399, uart, audio, amplifier]
category: Vivid
date-created: 2026-09-29
lang: en
original: 11-Vivid/18-MP3-TTS-Amps.md
date: 2026-10-08
---

# MP3 Modules, TTS Speech Synthesis and Amplifiers - JQ6500/KT403A/BY8301/DY-SV5W/SOMO-14D, SYN6288/XFS5152, PAM8403/TPA3116/LM386, MAX4466/MAX9814, MSGEQ7, PT2399

> [!info] Where this is in the reference
> Sound base: [[04-Interfaces/04-I2S.en.md|I2S]], simpler solution [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.en.md|DFPlayer/MAX98357A]], codecs [[11-Vivid/13-Audio-Codecs.en.md|Audio-Codecs]], start [[Home.en.md|Home]].
> Network audio - parallel note: [[11-Vivid/19-WebRadio-Streaming.en.md|WebRadio-Streaming]].

## Purpose

This note is "big sound" on ESP32 without I2S codecs: when you need **autonomous MP3 playback from SD** (entrance, museum, toy, alarm), **speak from text** (TTS: station announcements, voice assistant in English via pinyin/translit or English phrases), **boost to speaker** (0.5 W buzzer to 50 W sub), **boost microphone** (intercom, noise meter, voice control), **see spectrum** (color music, 7-band VU meter), and **add echo / reverb** (karaoke, intercom, effects).

When to choose what:

- just play files from microSD over UART - **KT403A** (DFPlayer-compatible one-to-one) or **JQ6500** (cheaper, but own protocol);
- loud without external amp - **DY-SV5W** (5 W on board) or MP3 module + **PAM8403**;
- announce text, not files - **SYN6288 / XFS5152** (send string over UART - module speaks);
- room stereo volume - **PAM8403** (3 W, 5 V);
- outdoor column / subwoofer - **TPA3116** (up to 50 W, 12-24 V, heatsink!);
- mic to ESP32 ADC - **MAX4466** (manual gain) or **MAX9814** (AGC for voice);
- color music - **MSGEQ7** (7 bands on one analog pin);
- echo - **PT2399** (analog delay 30-340 ms).

When NOT to choose: need HiFi stereo from network - see [[11-Vivid/19-WebRadio-Streaming.en.md]]; need record + headphones + I2S - see [[11-Vivid/13-Audio-Codecs.en.md]].

## Characteristics

| Module | Interface | Power | Output / power | Key rule |
| --- | --- | --- | --- | --- |
| JQ6500-28P | UART 9600 + BUSY + ADKEY/IO | 5 V (3.3 V - glitches!) | DAC stereo + SPK mono ~2 W | Own protocol `7E … EF`; USB re-flash possible |
| KT403A | UART 9600, DFPlayer protocol | 3.3-5 V (better 5 V) | DAC + SPK ~2 W | DFPlayer commands 1:1; easiest DFPlayer replacement |
| BY8301-16P | UART 9600 + IO/ADKEY | 5 V | SPK 2-3 W | Frame `7E … EF` with own command table - verify revision! |
| DY-SV5W | UART + IO buttons, USB | 5 V (up to 2 A peak!) | Built-in amp 5 W mono | SD + USB flash + SPI-flash; BUSY pin for track queue |
| SOMO-14D | UART 9600 (3.3 V!) + BUSY | 3.3 V | Linear stereo out (needs amp!) | 4D Systems; 3.3 V logic tolerant to ESP32 |
| DFPlayer Mini (reference) | UART 9600 + BUSY + ADKEY | 5 V | SPK 3 W diff. | See [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.en.md|note 08]] |
| SYN6288 | UART 9600 (TX/RX) + BUSY | 3.3-5 V | Linear out (to amp!) | GB2312 encoding! Cyrillic - pinyin/translit or English phrases |
| XFS5152 (XF-S5152CE) | UART 9600/115200 + BUSY | 3.3-5 V | Linear out | GBK/UTF-8/Unicode modes; volume/tone/speed by commands |
| PAM8403 | Analog input (stereo) | 5 V (2.5-5.5 V) | 3 W × 2, class-D | Noise from 5 V supply! LC filter or separate DC-DC; input not above 1 V |
| TPA3116 (XH-M543 board etc.) | Analog input (stereo) | 12-24 V (4.5-26 V) | 2 × 50 W (4 Ω, 21 V) | Heatsink mandatory! LC filter on output; gain resistors |
| LM386 (module) | Analog input | 5-9 V | 0.5 W | Gain 20 (default) / 200 (10 µF cap between 1-8) |
| NS4150 (module) | Analog input | 5 V | 3 W mono, class-D | Small, for buzzers / door bells |
| LM4871 (module) | Analog input | 5 V | 3 W mono BTL | Differential output - not to ground! |
| MAX4466 (preamp) | Analog out to ADC | 2.4-5 V (better 3.3 V!) | Gain 25×-125× (trimmer) | Output offset VCC/2; quiet 3.3 V supply |
| MAX9814 (preamp AGC) | Analog out to ADC | 2.7-5.5 V | Gain 40/50/60 dB + AGC | AGC keeps voice level; attack/release per datasheet |
| MSGEQ7 | STROBE + RESET (digital) + OUT (analog) | 5 V | 7 bands: 63/160/400/1k/2.5k/6.25k/16k Hz | Strobe clock ~36 µs; read OUT after each strobe |
| PT2399 (echo module) | Analog in/out | 5 V | Delay 30-340 ms | Resistor sets delay; long delay = dirty/noise |

## MP3 module comparison with DFPlayer Mini

| Parameter | DFPlayer Mini | JQ6500-28P | KT403A | BY8301-16P | DY-SV5W | SOMO-14D |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UART protocol | `7E FF 06 … EF` | Own `7E len cmd … EF` | **Like DFPlayer** | Own `7E … EF` | Own + IO | Own ASCII/UART |
| Rate | 9600 | 9600 | 9600 | 9600 | 9600 | 9600 |
| Power | 3.3-5 V (5 V best) | 5 V (3.3 unstable) | 3.3-5 V (5 V best) | 5 V | 5 V (up to 2 A peak) | 3.3 V |
| Volume command | `0x06` + 0-30 | `0x06` (verify!) | `0x06` | `0x06` | `0x06` | via ASCII |
| Track play | `0x12` + track | `0x12` (verify!) | `0x12` | `0x12` | `0x12` | `PLAY` + number |
| SD card | microSD (FAT32) | microSD (FAT32) | microSD (FAT32) | microSD (FAT32) | microSD / USB | none (SPI-flash / USB) |
| File name format | `001.mp3` | `001.mp3` (verify!) | `001.mp3` | `001.mp3` | `001.mp3` | none |
| Key replacement | - | different protocol | 1:1 | different protocol | different protocol | different protocol |

> [!tip] Protocol verification
> JQ6500/BY8301 commands vary by board revision; always verify with logic analyzer / serial. KT403A is closest to DFPlayer; easiest migration.

## UART commands for MP3 modules: play / stop / volume / track

### KT403A (and DFPlayer - same frame)

```cpp
// UART 9600, frame: 0x7E 0xFF 0x06 [COMMAND] [FEEDBACK] [VALUE] [CHECKSUM] 0xEF
// Play track 3, volume 20
Serial.write(0x7E); Serial.write(0xFF); Serial.write(0x06); Serial.write(0x03); // play
Serial.write(0x01); Serial.write(0x03); Serial.write(0xB9); Serial.write(0xEF); // checksum
```

### JQ6500 (typical set; verify board revision!)

```cpp
// Frame: 7E len cmd [args] checksum EF
Serial.write(0x7E); Serial.write(0x03); Serial.write(0x12); // play
Serial.write(0x01); Serial.write(0xb8); Serial.write(0xEF); // checksum (verify!)
```

### BY8301 / DY-SV5W (typical set)

```cpp
// Similar to JQ6500 but different command table; consult module datasheet.
Serial.write(0x7E); Serial.write(0x03); Serial.write(0x12); Serial.write(0x01);
Serial.write(0xB8); Serial.write(0xEF);
```

## SD card and FAT32 for MP3 modules

- Format microSD as FAT32 (not exFAT); cluster size 4096-8192.
- File names: 3-digit number with leading zeros (`001.mp3` ... `999.mp3`).
- Bitrate: 128-320 kbps MP3; 44.1 kHz; stereo/mono both work.
- BY8301 / DY-SV5W may support USB flash instead of SD.
- Do not use long file names or folders; put in root.

## TTS modules: SYN6288 / XFS5152 - text to speech via UART

```cpp
// SYN6288 (GB2312): send text as GB2312 bytes, then play command
String text = "Hello"; // encode to GB2312 / pinyin for Cyrillic
Serial.write(0xAA); Serial.write(0x01); // play after text
```

```cpp
// XFS5152: GBK / UTF-8 / Unicode modes selectable by command
Serial.write(0xFD); Serial.write(0x00); Serial.write(0x01); Serial.write(0x01); // set UTF-8
Serial.print("Hello"); Serial.write(0xA5); // play command
```

> [!tip] Cyrillic
> SYN6288 requires GB2312; Cyrillic needs pinyin/translit or English phrases. XFS5152 supports more encodings; verify mode.

## Amplifiers: PAM8403, TPA3116, LM386/NS4150/LM4871

### PAM8403 - 3 W stereo (room, desk, toy)

- Supply: 5 V (2.5-5.5 V); current up to 2 A at max; separate DC-DC if noisy.
- Input: analog stereo; do not exceed 1 V (use divider if needed).
- Output: direct to 4 Ω speaker; no output capacitor needed (class-D).
- LC filter near power; keep traces short.

### TPA3116 - 50 W (outdoor, sub, garage)

- Supply: 12-24 V; current high; heatsink mandatory; 4 Ω / 8 Ω load.
- Gain resistors set gain; adjust for voltage supply.
- LC output filter required; do not omit.
- Use 12 V supply for 2× 30 W; 24 V for 2× 50 W.

### Small: LM386 / NS4150 / LM4871

- LM386: 5-9 V; gain 20 default, 200 with 10 µF cap; 0.5 W.
- NS4150: 5 V; 3 W mono class-D; small; for buzzers.
- LM4871: 5 V; 3 W mono BTL; differential - do not ground one side.

## Microphone preamps: MAX4466 / MAX9814 (gain, AGC!)

```cpp
// MAX4466 to ESP32 ADC (2.4-5 V supply, better 3.3 V!)
// Gain 25-125× via trimmer; output offset VCC/2
int val = analogRead(A0); // 0-4095 at 3.3 V
```

```cpp
// MAX9814 (AGC) to ESP32 ADC
// Gain 40/50/60 dB selectable; AGC holds voice level
int val = analogRead(A0);
```

> [!warning] MAX4466 output offset
> At 3.3 V supply, output sits at 1.65 V; AC-couple to ADC or subtract offset in software.

## MSGEQ7 - 7-band spectrum analyzer

```cpp
// Strobe -> OUT -> read A0 after each strobe ~36 µs
const int STROBE = 4, RESET = 5, OUT = A0;
void readSpectrum() {
  digitalWrite(RESET, HIGH); delay(1); digitalWrite(RESET, LOW);
  for (int b=0; b<7; b++) {
    digitalWrite(STROBE, LOW); delayMicroseconds(36);
    int v = analogRead(OUT); // 63 Hz ... 16 kHz
    digitalWrite(STROBE, HIGH);
  }
}
```

## PT2399 - echo / reverb

```cpp
// Analog: input -> PT2399 -> output; delay set by resistor (30-340 ms)
// Long delay increases noise; use clean supply; keep analog paths short
```

## Star ground for audio (no ground loops)

- Use single ground point near ESP32; do not daisy-chain audio ground.
- Separate analog and digital ground; connect at one point (star).
- Use shielded cable for mic and line; ground shield at ESP32 only.
- Separate power supply for amplifiers (5 V / 12 V) from ESP32 3.3 V.

## Common issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| No sound from MP3 | wrong protocol / baud; FAT32 not formatted; file names not 3-digit | verify with analyzer; format FAT32; rename to `001.mp3` |
| MP3 plays but distorted | bitrate > 320 kbps; stereo vs mono mismatch | use 128-320 kbps; check module specs |
| TTS silent / garbled | GB2312 vs ASCII encoding; wrong UART rate | encode correctly; verify rate 9600 |
| Amplifier hum (50 Hz) | ground loop; shared supply | star ground; separate supply; LC filter |
| Mic noisy / low | gain too low / too high; AGC not set | adjust trimmer / AGC pin; keep wires short |
| Spectrum read wrong | strobe timing off; ADC read before settle | 36 µs strobe; read after delay |
| Echo dirty / noisy | long delay; dirty supply; long analog paths | keep delay moderate; clean supply; short traces |

## Official sources

- [DFPlayer Mini datasheet / Wiki](https://wiki.dfrobot.com/DFPlayer_Mini_MKII) - protocol reference.
- [JQ6500 / BY8301 datasheets](https://www.google.com/search?q=JQ6500+datasheet) - command tables by revision.
- [PAM8403 / TPA3116 datasheets (TI / others)](https://www.ti.com) - amplifier specs, gains, filters.
- [MSGEQ7 datasheet](https://www.sparkfun.com/products/110) - spectrum analyzer timing.
- [PT2399 datasheet](https://www.datasheetarchive.com) - analog delay specs.

## See also

- [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.en.md|DFPlayer / MAX98357A]] - simpler MP3 + amp.
- [[11-Vivid/13-Audio-Codecs.en.md|Audio Codecs]] - I2S / codec sound.
- [[11-Vivid/19-WebRadio-Streaming.en.md|WebRadio / Streaming]] - network audio.
- [[04-Interfaces/04-I2S.en.md|I2S]] - digital sound signals.
