---
title: TinyML Deep Practice - Voice + Smile on ESP32-C3/S3 - TFLite Micro
description: Deploy int8 models for voice commands and smile detection with quantization notes; shows code, memory tables and schematics.
tags: [esp32, proekti, tinyml, tflite, voice, smile, esp32-c3, esp32-s3, inmp441, ov2640]
category: Proekti
lang: en
original: 16-Projects/05-TinyML-Deep-Practice.md
date-created: 2026-09-28
date: 2026-10-08
---

# Project 5 - TinyML Deep Practice: Voice Commands + Smile → ESP32-C3/S3 + TFLite-Micro

> [!tip] What we are building
> Small int8 neural networks on ESP32: voice command "go / stop" on ESP32-C3 + INMP441; smile / no-smile on ESP32-S3 + OV2640 + PSRAM; quantization int8 vs int16 notes; inference < 100 ms; memory budget shown. Base: [[10-Sensors/02-DS18B20 | Sensors]], [[09-Firmware/01-ESP-IDF-setup | IDF]].

## 1. Goal and what we build

| Target | Chip | Model | Accuracy | Inference budget |
| --- | --- | --- | --- |
| Voice commands "go / stop" | ESP32-C3, 160 MHz | ~150 KB int8, 10 labels | ≥90 % in quiet room | < 30 ms per frame, 15 ms window |
| Smile / no-smile | ESP32-S3, 240 MHz + PSRAM | ~350 KB int8, 96×96 | ≥85 % in light 300-1500 lux | < 100 ms per frame |

Requirements:

- TFLite-Micro (TensorFlow Lite Micro) with `micro_speech` or custom CNN;
- quantization int8 with calibration (100-300 samples); accuracy drop ≤3 %;
- memory: weights in DROM (flash), tensors in SRAM, arena 16-32 KB;
- audio: INMP441 I2S 16 kHz; camera: OV2640 FIFO via SPI/I2C; no USB stream.

## 2. Why TFLite-Micro

- 150-350 KB fits ESP32-C3 (4 MB flash) and ESP32-S3 (8 MB + PSRAM);
- int8 quantization uses `tvmicro` with `TFLITE_ENABLE_XNNPACK` disabled (XNNPACK not on ESP32);
- Arduino library + ESP-IDF both supported; `micro_speech` pretrained model 20 KB baseline.

## 3. Model 1 - Voice command on ESP32-C3 + INMP441

### 3.1 Hardware

| C3 Pin | Function | Note |
| --- | --- | --- |
| GPIO4 | I2S DIN (mic SD) | data |
| GPIO5 | I2S WS (LRC) | channel 16 kHz |
| GPIO6 | I2S BCLK | clock |
| 3V3 / GND | INMP441 power | only 3.3 V + 100 nF |

### 3.2 Data and model

- dataset: 1 s "go" / "stop" / silence / noise; 300 samples per class; 16 kHz mono;
- preprocess: 30 ms window, 10 ms step, MFCC 10 coefficients; 20×10 input;
- model: 2 conv + 1 dense; ~150 KB int8; 10 output labels.

### 3.3 Working code (Arduino core)

```cpp
#include <Arduino.h>
#include <Audio.h>
#include <TensorFlowLite.h>

const int PB = 4; // button
// INMP441 I2S init
void setup() {
  // init I2S, load model from flash
}
void loop() {
  // record 1 s, infer, if "go" -> relay
}
```

### 3.4 Memory and time

| Operand | Place | Size |
| --- | --- | --- |
| Weights | DROM-flash | 150 KB |
| Input/output tensors | SRAM | 12 KB |
| Arena | SRAM | 16 KB |
| Audio buffer | SRAM | 1 KB |
| Total SRAM | - | ~30 KB (C3 has 320 KB) |

## 4. Model 2 - Smile on ESP32-S3 + OV2640

- camera: OV2640 FIFO + SPI; 96×96 grayscale; 30 fps; capture on button;
- model: simple CNN 3 conv + 2 dense; ~350 KB int8; 2 classes smile / none;
- light: 300-1500 lux; avoid face shadow; white balance fixed.

Code: `esp_camera` + `TensorFlowLite` with `MicroInterpreter`; arena 32 KB in PSRAM or SRAM.

## 5. Quantization: int8 vs int16

| Step | int16 | int8 |
| --- | --- | --- |
| Model size | ×2 | 1× |
| Speed on P6 | 1× | 1.5-2× |
| Accuracy | higher | −0.5…−3 % with proper calibration |

Calibration: 100-300 representative samples; `tf.lite.TFLiteConverter` with `representative_dataset`; avoid overfit to training light.

## 6. Troubleshooting

| Symptom | Where to look |
| --- | --- |
| Inference > 100 ms | arena too small, PSRAM not used, reduce model | 
| Audio not captured | I2S WS/BCLK swapped, 3.3 V missing cap | 
| Accuracy < 85 % | calibration samples too few, light variance | 
| Camera black frame | SPI CS wrong, FIFO not flushed | 
| Flash full (4 MB) | model > 200 KB; use ESP32-S3 8 MB | 

## 7. Memory budget table (ESP32-C3 + S3)

| Component | ESP32-C3 (320 KB SRAM) | ESP32-S3 (512 KB SRAM + 8 MB PSRAM) |
| --- | --- | --- |
| Model weights (flash) | 150 KB int8 | 350 KB int8 |
| Arena (SRAM) | 16-32 KB | 32-64 KB |
| Audio / image buffer | 1 KB / 4 KB | 4 KB / 16 KB |
| Stack + heap | 50 KB | 80 KB |
| Free after load | ~220 KB | ~350 KB |

## 8. Deployment checklist

- [ ] Calibrate int8 with 100+ samples per class
- [ ] Check inference time with `micros()` in loop
- [ ] Verify SRAM usage with `esp_get_free_heap_size()`
- [ ] Lock model to DROM; do not load to SRAM
- [ ] Test with battery at 3.3 V; voltage drop affects ADC / mic
- [ ] Set `CONFIG_TINYML_ENABLE` in sdkconfig if using ESP-IDF

## 9. Official sources

- [TensorFlow Lite Micro - docs](https://www.tensorflow.org/lite/micro) - int8, quantization.
- [ESP32-C3 - Espressif](https://www.espressif.com/en/products/socs/esp32-c3) - 160 MHz, 4 MB flash.
- [INMP441 - datasheet](https://invensense.tdk.com/en/products/video/part-number/INMP441/) - I2S mic, 3.3 V.
- [OV2640 - Omnivision](https://www.ovt.com/sensor/OV2640) - 1/4" CMOS, FIFO.

## See also

- [[EN/Home.en]]
- [[09-Firmware/01-ESP-IDF-setup.en | IDF]]
- [[16-Projects/01-Weather-Station.en | Weather Station]]
- [[16-Projects/02-GPS-Tracker.en | GPS Tracker]]
- [[09-Firmware/03-MicroPython | MicroPython]]

## Appendix: Sample JSON output

```json
{"label":"go","conf":0.94,"t_ms":28,"vbat":3.31}
```

*Note: always log inference time and confidence for calibration tracking.*

