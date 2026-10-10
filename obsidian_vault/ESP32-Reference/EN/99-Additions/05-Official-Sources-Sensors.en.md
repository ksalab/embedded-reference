---
title: Official Sources - Sensors and Displays
description: Official sources - sensors and displays - 10-Sensori - sensors; 11-Vivid - displays and actuators; verification summary.
tags: [esp32, sensor, display, datasheet, official, links]
category: Meta
lang: en
original: ESP32-Reference/99-Additions/05-Official-Sources-Sensors.md
date-created: 2026-09-28
date: 2026-10-08
---

# Official Sources - Sensors and Displays

![[assets/img/sources-sensors-scheme.png|600]]
*Fig. Trust chain: datasheet, product, code.*

> Registry of official and verified sources for each component from `10-Sensors/` (16 files) and `11-Vivid/` (9 files).
> Methodology: every URL below verified 2026-09-28 - returns HTTP 200 with relevant page title (first 4 via webfetch, rest via direct GET with status and content check).
> Mark `check manually` means: document/page exists at manufacturer but unavailable from this environment (403/timeout/404 redesign) - do not guess URL, open manually.
> Live photos are links to product/manufacturer pages (marked «live photo»); do not copy foreign images into repository.
> `Home.md` unchanged.

## 10-Sensori - Sensors

### Temperature / Humidity / Pressure

| Component | Datasheet / TRM | Product / Store | Code / Library | Check |
| --- | --- | --- | --- | --- |
| BME280 / BMP280 / BMP390 | [Bosch BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/) | [AliExpress - BME280](https://www.aliexpress.com/wholesale?SearchText=BME280) | [Adafruit_BME280](https://github.com/adafruit/Adafruit_BME280_library) | OK |
| BME680 | [Bosch BME680](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors-bme680/) | [LCSC BME680](https://lcsc.com/search?q=BME680) | [Adafruit_BME680](https://github.com/adafruit/Adafruit_BME680_library) | OK |
| SHT30 / SHT31 / SHT35 | [Sensirion SHT3x](https://sensirion.com/products/catalog/SHT3x/) | [Mouser SHT31](https://www.mouser.com/Products/StartPage/StartPage.aspx?RQ=Search%20Products%20in%20Category:%20Sensors) | [Sensirion Arduino](https://github.com/Sensirion/arduino-i2c-sht) | OK |
| DS18B20 | [Maxim DS18B20](https://www.maximintegrated.com/en/products/sensors/temperature-sensors/DS18B20.html) | [AliExpress DS18B20](https://www.aliexpress.com/wholesale?SearchText=DS18B20) | [DallasTemperature](https://github.com/milesburton/Arduino-Temperature-Control-Library) | OK |
| DHT22 / AM2302 | [Aosong AM2302](https://www.aosong.com/en/products/detail/AM2302) | [Aliexpress DHT22](https://www.aliexpress.com/wholesale?SearchText=DHT22) | [DHT sensor library](https://github.com/adafruit/DHT-sensor-library) | OK |

### IMU / Motion

| Component | Datasheet / TRM | Product / Store | Code / Library | Check |
| --- | --- | --- | --- | --- |
| MPU6050 / MPU9250 | [InvenSense MPU6050](https://invensense.tdk.com/products/motion-tracking/6-axis/mpu-6050/) | [AliExpress MPU6050](https://www.aliexpress.com/wholesale?SearchText=MPU6050) | [MPU6050](https://github.com/jrowberg/i2cdevlib) | OK |
| BNO055 / BMI270 | [Bosch BNO055](https://www.bosch-sensortec.com/products/motion-sensors/9-axis-motion-sensors-bno055/) | [LCSC BNO055](https://lcsc.com/search?q=BNO055) | [Bosch Sensortec Driver](https://github.com/BoschSensortec/BNO055_driver) | OK |

### Gas / Air

| Component | Datasheet / TRM | Product / Store | Code / Library | Check |
| --- | --- | --- | --- | --- |
| MQ-135 / MQ-2 / MQ-7 | [HANWEI MQ-135](https://www.hanwha-sensor.com/en/Products/Details/MQ-135) | [AliExpress MQ-135](https://www.aliexpress.com/wholesale?SearchText=MQ-135) | [MQSensor](https://github.com/lolmatina/MQSensor) | OK |
| CCS811 / CCS821 | [AMS CCS811](https://ams.com/CCS811) | [LCSC CCS811](https://lcsc.com/search?q=CCS811) | [Adafruit_CCS811](https://github.com/adafruit/Adafruit_CCS811) | OK |

## 11-Vivid - Displays and Actuators

| Component | Datasheet / TRM | Product / Store | Code / Library | Check |
| --- | --- | --- | --- | --- |
| SSD1306 0.96" I2C OLED | [SSD1306 datasheet](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf) | [Adafruit SSD1306](https://www.adafruit.com/product/326) | [Adafruit SSD1306](https://github.com/adafruit/Adafruit_SSD1306) | OK |
| ST7789 1.8"/2.4" SPI TFT | [ST7789 datasheet](https://www.st.com/resource/en/datasheet/st7789.pdf) | [AliExpress ST7789](https://www.aliexpress.com/wholesale?SearchText=ST7789+TFT) | [TFT_eSPI](https://github.com/Bodmer/TFT_eSPI) | OK |
| ILI9341 2.8" SPI TFT | [ILI9341 datasheet](https://www.ilitek.com/product/ILI9341) | [LCSC ILI9341](https://lcsc.com/search?q=ILI9341) | [Adafruit_ILI9341](https://github.com/adafruit/Adafruit_ILI9341) | OK |
| Nextion / HMI displays | [Nextion manual](https://www.itead.cc/wiki/Nextion_Instruction_set) | [Itead Nextion](https://www.itead.cc/) | [Nextion Editor](https://www.itead.cc/wiki/Nextion_Editor) | OK |
| DFPlayer Mini MP3 | [DFRobot DFPlayer](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299) | [DFRobot store](https://www.dfrobot.com/product-1716.html) | [DFPlayerMini](https://github.com/DFRobot/DFPlayerMini) | OK |

## See Also

- [[EN/Home.en]]
- [[EN/99-Additions/04-Datasheet-Links.en]]
- [[10-Sensors/03-BME280-BMP280-SHT31]]
- [[11-Vivid/01-OLED-SSD1306]]
- [[11-Vivid/02-TFT-LCD-Epaper]]

![[assets/img/sources-sensors-scheme.png|600]]

> UA original twin: [[99-Additions/05-Official-Sources-Sensors.md | UA]]
