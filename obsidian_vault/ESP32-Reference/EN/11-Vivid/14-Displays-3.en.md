---
description: Displays 3: SSD1322, SSD1351, ST7796, GC9A01, RA8875, FT81x; shows schematics, code and tables.
title: Displays 3: SSD1322, SSD1351, ST7796, GC9A01, RA8875, FT81x
tags: [esp32, display, tft, ssd1322, ssd1351, gc9a01, ra8875, ft81x, lvgl, squareline]
category: Vivid
date-created: 2026-09-28
lang: en
original: 11-Vivid/14-Displays-3.md
date: 2026-10-08
---


# Displays 3: SSD1322, SSD1351, ST7796, GC9A01, RA8875, FT81x

![[assets/img/displays-3-oled-tft-eve-scheme.png|600]]
*Fig. 1. Display choice for ESP32: from miniature grey OLED (SSD1322) to graphic TFT (ST7796) and FT81x electronics with built-in GPU.*

## Purpose

This section covers advanced displays for professional attachments, UI/HMI and premium projects. SSD1322 is a grey OLED (not colour), SSD1351 - colour OLED 128x128, ST7796 - classic TFT 480x320, GC9A01 - round OLED/colour TFT 240x240, RA8875 - large TFT controller (3.5"/5"), FT81x - electronics with built-in GPU for fast UI creation.

## Characteristics

| Module | Resolution | Interface | controller | power supply | Feature |
| --- | --- | --- | --- | --- | --- |
| SSD1322 | 128x128 (grey) | I2C / SPI | SSD1322 | 3.3 V | Grey palette, low consumption (≈15 mA) |
| SSD1351 | 128x128 (Colour) | SPI | SSD1351 | 3.3 V | 65K colours, built-in RAM animation |
| ILI9340 / ILI9341 | 240x320 (TFT) | SPI / 8080 | ILI9340 (predecessor) / ILI9341 | 3.3 V (I/O), 5V (Backlight) | Popular 2.4-2.8″ TFT; ILI9340 - old revision, ILI9341 - current (TFT_eSPI out of box) |
| ST7796 | 480x320 (TFT) | 8080-bus / SPI | ST7796 | 3.3 V (I/O), 5V (Backlight) | Wide viewing angle, LVGL support, compatible with FT81x |
| GC9A01 | 240x240 (Colour) | SPI / 8080 | SSD2805 / ST7789 | 3.3 V (I/O), 5V (Backlight) | Round format, touch support |
| RA8875 | 320x240 / 3.5" TFT | 8080-cat / SPI | RA8875 | 3.3 V (I/O), 5V (Backlight) | Large display, SPI speed up to 40 MHz |
| FT81x (EVE) | 3.5" / 4.3" / 7" TFT | SPI / 8080 / RGB | FT81x (EVE) | 3.3 V (I/O), 5V (Backlight) | 'Elektor Graphics Engine' - hardwired GUI, command lists |

## Module pin legend (universal for SPI / 8080)

| Pin | Type | To on ESP32 | Note |
| --- | --- | --- | --- |
| VCC | power supply | 3.3 V (logic) / 5 V (Backlight) | SSDO VCC, Backlight - separate sources |
| GND | ground | Common GND | Common minus |
| D0-D7 (DB0-DB7) | DBUS data | GPIO18-GPIO23 (SPI) | Bidirectional data bus |
| RS / RSX | Register / Command | GPIO5 (or other) | 0 = command, 1 = data |
| WRX / WR | Write strobe | GPIO18 (SPI) | Latch command/data to device |
| RDX / RD | Read strobe | GPIO19 (SPI) | Read from display memory |
| CS / XCS | Chip Select | GPIO5 (or other) | Active LOW level |
| RESX / RST | Reset | GPIO4 (or other) | Hard reset at start |
| SCK / SCK | Clocking | GPIO18 (SPI) | SPI clock (if 8080 - use WRX) |
| SDI / SDA | SPI data | GPIO23 (VSPI) | write data |
| SDO | SPI MISO | GPIO19 (VSPI) | Read data |

## Wiring diagram (SPI 4-wire)

```text
ESP32 DevKit        SSD1322 / SSD1351 / ST7796 / GC9A01 / RA8875 / FT81x
  3V3 ──────► VCC
  GND    ──────► GND
  GPIO18 ──────► SCK (CLK)
  GPIO19 ──────► SDO (MISO)
  GPIO23 ──────► SDI (MOSI)
      GPIO5   ──────► CS (LOW = активний)
      GPIO4   ──────► RES (Reset)
```

### ASCII-schem (SPI)

```text
ESP32 DevKit                        Дисплей (SPI)
  ┌────────────┐                         ┌─────────────┐
  │        3V3 ├─────────────────────────┤ VCC         │
  │        GND ├─────────────────────────┤ GND         │
  │     GPIO18 ├─────────────────────────┤ SCK / CLK   │
  │     GPIO19 ├─────────────────────────┤ SDO / MISO  │
  │     GPIO23 ├─────────────────────────┤ SDI / MOSI  │
  │      GPIO5 ├─────────────────────────┤ CS          │
  │      GPIO4 ├─────────────────────────┤ RES         │
  └────────────┘                         └─────────────┘
```

### Mermaid

```mermaid
graph LR
    ESP[ESP32 DevKit] -->|3V3/GND| DISP[Дисплей]
    ESP -->|GPIO18 SCK| DISP
    ESP -->|GPIO19 SDO MISO| DISP
    ESP -->|GPIO23 SDI MOSI| DISP
    ESP -->|GPIO5 CS| DISP
    ESP -->|GPIO4 RES| DISP
```

## Code ESP-IDF (LVGL + SSD1351)

```c
#include "lvgl.h"
#include "driver/spi_master.h"
#include "display_driver.h"

static lv_disp_draw_buf_t draw_buf;

void app_main(void) {
    esp_err_t ret;
    spi_bus_config_t buscfg = {
        .miso_io_num = GPIO_NUM_19,
        .mosi_io_num = GPIO_NUM_23,
        .sclk_io_num = GPIO_NUM_18,
        .quadwp_io_num = -1,
        .quadhd_io_num = -1,
    };
    ret = spi_bus_initialize(SPI2_HOST, &buscfg, SPI_DMA_CH_AUTO);
    assert(ret == ESP_OK);

    spi_device_interface_config_t devcfg = {
        .clock_speed_hz = 20000000,
        .mode = 0,
        .spics_io_num = GPIO_NUM_5,
        .queue_size = 7,
    };
    ret = spi_bus_add_device(SPI2_HOST, &devcfg, &spi_dev);
    assert(ret == ESP_OK);

    // LVGL initialisation
    lv_init();
    lv_disp_draw_buf_init(&draw_buf, buf1, buf2, LV_HOR_RES_MAX * LV_VER_RES_MAX / 10);

    // Register display handler
    lv_disp_drv_t disp_drv = {
        .hor_res = 128,
        .ver_res = 128,
        .flush_cb = my_disp_flush,
        .draw_buf = &draw_buf,
        .lv_disp_drv_init = true,
    };
    lv_disp_drv_register(&disp_drv);
}
```

## Code Arduino (FT81x EVE)

```cpp
#include <SPI.h>
#include <FT81.h>

#define TFT_CS   5
#define TFT_RST  4
#define TFT_DC   17

void setup() {
  Serial.begin(115200);
  SPI.begin(18, 19, 23, 5);
  EVE.begin(FT81_CLK, FT81_MISO, FT81_MOSI, FT81_CS, FT81_RST);
  EVE_cmd_DlStart();
  // Окремі команди FT81x для кнопок, слайдерів, списків
}

void loop() {
  EVE_cmd_Display();
  EVE_cmd_number(100, 100, 10, 13, "Score:");
}
```

## Code MicroPython (SSD1322 / SPI)

```python
from machine import Pin, SPI
import ssd1322

spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
dc = Pin(4)
rst = Pin(5)
display = ssd1322.SSD1322(spi, dc, rst, width=128, height=128)
display.fill(0)
display.text("Hello", 0, 0, 1)
display.show()
```

## Common issues

| No | error | Symptom | Fix |
| --- | --- | --- | --- |
| 1 | SSDO loses sync | Stripes on screen, glitches | Check SPI speed (lower to 8-10 MHz); check pull-up resistors on bus |
| 2 | SSD1322 shows grey screen | Missing colour data | Check correct driver: SSD1322 is grey-scale IC, SSD1351 - colour |
| 3 | FT81x does not init | `EVE not responding` | Check SPI / 8080 mode; check VCC (3.3 V logic, 5 V backlight); check RESET line |
| 4 | Garbage on screen on frame swap | Phantom images, ghosting | use `double buffering` in LVGL; tune `partial refresh` |

## Official sources

- FTDI FT81x (EVE): `ftdichip.com` (Programming Guide), `github.com/FTDI-EVE`
- GC9A01A Datasheet (GalaxyCore, via alldatasheet): [GC9A01A PDF](https://www.alldatasheet.com/datasheet-pdf/pdf/2267469/GALAXYCORE/GC9A01A.html) - 240×240 TFT, Rev 1.0.
- SSD1322/SSD1351: `seeedstudio.com` (OLED display), `waveshare.com`
- ST7796: `lcdwiki.com` (ST7796 breakdown), `waveshare.com`
- RA8875: `rapidonline.com` (RA8875 datasheet)

- RA8875 Datasheet (Raio, PDF search): [RA8875 search](https://www.alldatasheet.com/view.jsp?Searchword=RA8875) - TFT-controller with GPU.
- ST7796 Datasheet (Sitronix, PDF search): [ST7796 search](https://www.alldatasheet.com/view.jsp?Searchword=ST7796) - TFT 480x320.
- ILI9340 Datasheet (Ilitek, PDF search): [ILI9340 search](https://www.alldatasheet.com/view.jsp?Searchword=ILI9340) - TFT 240x320.
- SSD1322/SSD1351 Datasheet (Solomon, PDF search): [SSD1322 search](https://www.alldatasheet.com/view.jsp?Searchword=SSD1322) - OLED controllers.
- SSD2805 Datasheet (Solomon, PDF search): [SSD2805 search](https://www.alldatasheet.com/view.jsp?Searchword=SSD2805) - MIPI bridge.

## See also

- [[Home.en | Home]]
- [[11-Vivid/12-LVGL-SquareLine.en | LVGL SquareLine]]
- [[11-Vivid/13-Audio-Codecs.en | Audio Codecs]]
- [[EN/10-Sensors/32-Light-Color-2.en]]
- [[04-Interfaces/02-SPI.en | SPI]]
