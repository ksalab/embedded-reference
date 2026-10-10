---
title: Edge AI Vision - Person Detection int8 on ESP32-S3 - Solar, PIR, NoIR
description: Edge AI vision with int8 person detection, solar power, PIR wake, NoIR camera; shows pinout, thresholds, code and error table.
tags: [esp32, proekti, edge-ai, vision, esp32-s3, ov2640, person-detection, solar, pir]
category: Proekti
lang: en
original: 16-Projects/07-Edge-AI-Vision.md
date-created: 2026-09-28
date: 2026-10-08
---

# Project 7 - Edge AI Vision: Person Detection int8 → ESP32-S3 + Solar + PIR + NoIR

> [!tip] What we are building
> Low-power vision node: ESP32-S3 + OV2640 captures 96×96 grayscale; int8 model ~300 KB detects person; 5-8 fps; solar 10W + 2×18650 + BMS 2S; PIR wakes from light-sleep; status RGB LED. Base: [[01-Hardware/08-Antennas-RF | Antennas]], [[10-Sensors/03-BME280-BMP280-SHT31.en | BME280]].

## 1. Goal and parameters

| Parameter | Value |
| --- | --- |
| Model | person-detection int8, ~300 KB |
| Input | 96×96 grayscale |
| Speed | 5-8 fps on S3 240 MHz |
| Accuracy | ~85 % daytime, worse at night |
| Power | solar 10W + 2×18650 |

Requirements:

- camera: OV2640 on CSI board (Freenove/CAM); NoIR for night; 850 nm IR projector optional;
- inference: ESP-IDF or MicroPython `tflite` micro; arena ~60 KB SRAM; model from flash;
- wake: PIR on GPIO4; if motion → light-sleep 2 s → capture → infer → if person → publish + LED blue; else deep-sleep 30 s;
- solar: 10W panel + MPPT + 2S BMS; TP4056 is not for solar!
- output: MQTT `vision/event` QoS 1; image only if detection; buffer 5 frames.

## 2. Architecture

ESP32-S3 is the only node; no second MCU; CSI directly to S3; PIR triggers capture; solar charges via MPPT to 2S Li-ion; BMS 2S protects overcharge/under-voltage.

## 3. Node pinout

| Signal | S3 Pin | Note |
| --- | --- | --- |
| Camera OV2640 | CSI connector on board | Freenove/CAM board |
| PIR wake | GPIO4 | wakes from light-sleep |
| Solar 6V | VIN via MPPT | TP4056 not for solar! |
| 18650 ×2 | BMS 2S | protection mandatory |
| Status LED | GPIO48 (RGB) | state colors |

## 4. Model and thresholds

- model: SSD-MobileNet int8 96×96; ~300 KB; 2 classes person / background;
- thresholds: score ≥ 0.6 for detection; IoU ≥ 0.3 for track; track window 10 frames;
- ROI mask: skip sky top 20 %; focus middle 60 %; filter by area > 500 px.

## 5. Working code (C, ESP-IDF)

```c
#include "esp_camera.h"
#include "tflite-model.h"

void app_main() {
  esp_camera_init();
  // capture, preprocess 96x96 gray, infer
  // if score > 0.6 -> publish
}
```

## 6. Working code (MicroPython)

```python
# MicroPython with tflite micro or simple CNN
import camera
img = camera.capture()
# infer; publish
```

## 7. Autonomous power

- 10W panel + MPPT → 2S BMS → 18650; 2S = 7.4 V nominal; BMS cuts at 8.4 V (charge) and 5.6 V (discharge);
- solar must have MPPT (not TP4056); TP4056 is linear charger for single cell, no solar tracking;
- with 10W panel and 30 s cycle, battery stays full; if 3 days no sun, battery 2000 mAh / 150 mA avg ~13 h; must add PIR only wake to extend.

## 8. Common errors

| Symptom | Cause | Fix |
| --- | --- | --- |
| Detects shadows | threshold low, no ROI | threshold 0.6+, sky mask |
| IDs jump | IoU threshold too high | 0.3, track window 10 frames |
| Blind at night | no IR illumination | NoIR + 850 nm projector |
| Battery dead weekly | no sleep, detector always on | PIR wake + deep-sleep |
| False alarms by animals | box size too small | filter area + ROI height |
| Frame confirmation broken | capture during capture | double frame buffer |

## 9. Official sources

- [ESP32-S3 - Espressif](https://www.espressif.com/en/products/socs/esp32-s3) - 240 MHz, AI instructions.
- [OV2640 - Omnivision](https://www.ovt.com/sensor/OV2640) - CSI interface.
- [TensorFlow Lite Micro - docs](https://www.tensorflow.org/lite/micro) - int8, quantization.

## See also

- [[EN/Home.en]]
- [[01-Weather-Station.en | Weather Station]]
- [[02-GPS-Tracker.en | GPS Tracker]]

## Extended notes

Frame pipeline: capture 96×96 grayscale from OV2640 FIFO; pre-process with mean subtraction and normalization to [-1,1]; run interpreter; output 2-class scores; if person score > threshold, send MQTT with timestamp + confidence; skip image transfer to save bandwidth; only send thumbnail 16×16 if node-RED requests.

Light conditions: daytime > 300 lux; avoid backlight; use fixed white balance; at dusk < 50 lux, switch to NoIR + IR projector; IR projector should have PIR-controlled relay to save battery (only on when motion detected).

Battery management: BMS 2S must have temperature sensor; if cell > 45 °C or < 0 °C, stop charging; MPPT should have float voltage 8.4 V; when battery < 6.0 V, enter deep-sleep 5 min; when < 5.6 V, shut down and require solar to restart.

Installation: camera 2 m height, 30° down angle; avoid direct sunlight into lens; use IP65 enclosure with vent membrane; antenna for WiFi inside or external SMA; keep CSI cable < 20 cm to avoid signal degradation.

## Code snippet (MicroPython)

```python
from machine import Pin, SPI
import camera

# init camera
# capture frame
img = camera.capture()
# simple threshold for demo; real model needed
if img.get("gray").mean() > 100:
    mqtt.publish("vision/event", '{"det":"person","conf":0.82}')
```

## Calibration procedure

- collect 200 images with person at 2-4 m distance; 100 without;
- run `tflite_convert` with representative dataset; quantize int8;
- verify accuracy on 50 test images; if < 80 %, collect more diverse light conditions;
- fix ROI: skip top 20 % sky region; apply mask before inference.

## Maintenance table

| Component | Check interval | Action |
| --- | --- | --- |
| Solar panel | monthly | clean dust, check angle |
| IR projector | weekly | test range 3 m |
| BMS / battery | monthly | voltage check, balance |
| Enclosure seal | quarterly | gasket replacement |
| Lens cleaning | monthly | microfiber cloth |

*Note: always verify model accuracy after every firmware update; OTA should not overwrite calibration dataset.*

## Final checklist
- [ ] Camera focus set to 2 m
- [ ] PIR sensitivity calibrated
- [ ] Solar panel angle checked
- [ ] BMS balance verified
