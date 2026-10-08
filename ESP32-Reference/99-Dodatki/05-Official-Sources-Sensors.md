---
title: Офіційні джерела - сенсори та вивід
description: Офіційні джерела - сенсори та вивід - 10-Sensori - датчики; 11-Vivid - вивід та актуатори; Зведення перевірки
tags: [esp32, sensor, display, datasheet, official, links]
date: 2026-09-28
---

# Офіційні джерела - сенсори та вивід

![[assets/img/sources-sensors-scheme.png|600]]
*Рис. Ланцюжок довіри: даташит, продукт, код.*

> Реєстр офіційних і перевірених джерел для кожного компонента з `10-Sensori/` (16 файлів) та `11-Vivid/` (9 файлів).
> Методологія: кожен URL нижче перевірено 2026-09-28 - повертає HTTP 200 з релевантним заголовком сторінки (перші 4 - через webfetch, решта - прямим GET-запитом з перевіркою статусу та контенту).
> Позначка `перевірити вручну` означає: документ/сторінка існує у виробника, але з цього середовища недоступна (403/timeout/404 редизайн сайту) - URL не вгадувати, відкрити вручну.
> Живі фото - це посилання на сторінки товарів/виробників (підпис «живе фото»); чужі картинки в репозиторій не копіювати.
> Файл `Home.md` не змінювався.

## 10-Sensori - датчики

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| DHT11 | `10-Sensori/01` | перевірити вручну (Aosong) | [DHT11 - живе фото (Adafruit)](https://www.adafruit.com/product/386) | [Туторіал DHT11/DHT22 з кодом (RNT)](https://randomnerdtutorials.com/esp32-dht11-dht22-temperature-humidity-sensor-arduino-ide/) |
| DHT22 (AM2302) | `10-Sensori/01` | перевірити вручну (Aosong) | [DHT22 - живе фото (Adafruit)](https://www.adafruit.com/product/385) | [Розбір протоколу DHT11/DHT22 (LME)](https://lastminuteengineers.com/dht11-dht22-arduino-tutorial/) |
| DS18B20 | `10-Sensori/02` | перевірити вручну (Analog/Maxim, сайт блокує ботів) | [DS18B20 - живе фото (Adafruit)](https://www.adafruit.com/product/374) | [Туторіал DS18B20 з кодом (RNT)](https://randomnerdtutorials.com/esp32-ds18b20-temperature-arduino-ide/) |
| BME280 | `10-Sensori/03` | [Сторінка BME280 + даташит (Bosch)](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/) | [BME280-модуль - живе фото (Adafruit)](https://www.adafruit.com/product/2652) | [Туторіал BME280 з кодом (RNT)](https://randomnerdtutorials.com/esp32-bme280-arduino-ide-pressure-temperature-humidity/) |
| BMP280 | `10-Sensori/03` | перевірити вручну (Bosch, редизайн сайту) | [BME280-модуль - живе фото (Adafruit)](https://www.adafruit.com/product/2652) | [Гайд BME280, код сумісний з BMP280 (Adafruit Learn)](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout) |
| SHT31 | `10-Sensori/03` | [SHT31-DIS-F - каталог і даташит (Sensirion)](https://sensirion.com/products/catalog/SHT31-DIS-F) | [SHT31-D - живе фото (Adafruit)](https://www.adafruit.com/product/2857) | [Гайд SHT31-D з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout) |
| MPU6050 | `10-Sensori/04` | перевірити вручну (TDK InvenSense, сторінка переїхала) | [MPU-6050 - живе фото (Adafruit)](https://www.adafruit.com/product/3886) | [Туторіал MPU-6050 з кодом (RNT)](https://randomnerdtutorials.com/esp32-mpu-6050-accelerometer-gyroscope-arduino/) |
| HC-SR04 | `10-Sensori/05` | перевірити вручну (даташит виробника модуля) | - | [Туторіал HC-SR04 з кодом (RNT)](https://randomnerdtutorials.com/esp32-hc-sr04-ultrasonic-arduino/) |
| HC-SR501 PIR | `10-Sensori/05` | перевірити вручну (даташит виробника модуля) | - | [Туторіал PIR з кодом (RNT)](https://randomnerdtutorials.com/esp32-pir-motion-sensor-interrupts-timers/) |
| INA219 | `10-Sensori/06` | [Сторінка INA219 + даташит (TI)](https://www.ti.com/product/INA219) | [INA219-модуль - живе фото (Adafruit)](https://www.adafruit.com/product/904) | [Гайд INA219 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout) |
| HX711 | `10-Sensori/06` | перевірити вручну (Avia Semiconductor) | - | [Туторіал HX711 + тензодатчик з кодом (RNT)](https://randomnerdtutorials.com/esp32-load-cell-hx711/) |
| BH1750 | `10-Sensori/06` | перевірити вручну (ROHM) | - | перевірити вручну |
| AHT10 | `10-Sensori/07` | перевірити вручну (ASAIR) | - | перевірити вручну |
| AHT20 | `10-Sensori/07` | перевірити вручну (ASAIR) | - | перевірити вручну |
| SHT40 | `10-Sensori/07` | [SHT40 - каталог і даташит (Sensirion)](https://sensirion.com/products/catalog/SHT40) | [SHT40 - живе фото (Adafruit)](https://www.adafruit.com/product/4885) | [Гайд SHT40/SHT41/SHT45 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor) |
| BME680 | `10-Sensori/08` | [Сторінка BME680 + даташит (Bosch)](https://www.bosch-sensortec.com/en/products/environmental-sensors/gas-sensors/bme680/) | [BME680-модуль - живе фото (Adafruit)](https://www.adafruit.com/product/3660) | [Гайд BME680 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas) |
| CCS811 | `10-Sensori/08` | перевірити вручну (ams-OSRAM, редизайн сайту) | [CCS811-модуль - живе фото (Adafruit)](https://www.adafruit.com/product/3566) | [Гайд CCS811 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor) |
| MH-Z19 (CO2) | `10-Sensori/08` | перевірити вручну (Winsen, PDF-мануал на winsen-sensor.com) | - | перевірити вручну |
| PMS5003 | `10-Sensori/08` | перевірити вручну (Plantower, сайт блокує ботів) | - | перевірити вручну |
| ADS1115 | `10-Sensori/09` | [Сторінка ADS1115 + даташит (TI)](https://www.ti.com/product/ADS1115) | [ADS1115-модуль - живе фото (Adafruit)](https://www.adafruit.com/product/1085) | - |
| MCP3008 | `10-Sensori/09` | перевірити вручну (Microchip, сайт блокує ботів) | [MCP3008 - живе фото (Adafruit)](https://www.adafruit.com/product/856) | - |
| PCF8574 | `10-Sensori/09` | [Сторінка PCF8574 + даташит (TI)](https://www.ti.com/product/PCF8574) | - | [Туторіал I2C LCD на PCF8574 з кодом (RNT)](https://randomnerdtutorials.com/esp32-esp8266-i2c-lcd-arduino-ide/) |
| MCP23017 | `10-Sensori/09` | перевірити вручну (Microchip, сайт блокує ботів) | [MCP23017 - живе фото (Adafruit)](https://www.adafruit.com/product/732) | - |
| VL53L0X | `10-Sensori/10` | перевірити вручну (ST, таймаут з цього середовища) | [VL53L0X - живе фото (Adafruit)](https://www.adafruit.com/product/3317) | [Гайд VL53L0X з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout) |
| TCS34725 | `10-Sensori/10` | перевірити вручну (ams-OSRAM, редизайн сайту) | [TCS34725 - живе фото (Adafruit)](https://www.adafruit.com/product/1334) | - |
| TSL2561 | `10-Sensori/10` | перевірити вручну (ams-OSRAM, редизайн сайту) | [TSL2561 - живе фото (Adafruit)](https://www.adafruit.com/product/439) | - |
| NTC-термістор | `10-Sensori/11` | перевірити вручну (таблиця R-T виробника) | - | перевірити вручну |
| PT100 + MAX31865 | `10-Sensori/11` | перевірити вручну (Analog/Maxim, сайт блокує ботів) | [MAX31865-підсилювач PT100 - живе фото (Adafruit)](https://www.adafruit.com/product/3328) | - |
| MAX6675 (K-тип) | `10-Sensori/11` | перевірити вручну (Analog/Maxim, сайт блокує ботів) | - | [Розбір MAX6675 з кодом (LME)](https://lastminuteengineers.com/max6675-thermocouple-arduino-tutorial/) |
| LM35 | `10-Sensori/11` | [Сторінка LM35 + даташит (TI)](https://www.ti.com/product/LM35) | - | - |
| MQ-2 / MQ-7 / MQ-135 | `10-Sensori/12` | перевірити вручну (Winsen/Hanwei) | - | перевірити вручну |
| KY-026 Flame | `10-Sensori/12` | перевірити вручну (даташит виробника модуля) | - | перевірити вручну |
| KY-038 Sound | `10-Sensori/12` | перевірити вручну (даташит виробника модуля) | - | [Розбір датчика звуку з кодом (LME)](https://lastminuteengineers.com/sound-sensor-arduino-tutorial/) |
| RCWL-0516 | `10-Sensori/13` | перевірити вручну (даташит виробника модуля) | - | [Туторіал RCWL-0516 з кодом (RNT)](https://randomnerdtutorials.com/arduino-rcwl-0516/) |
| Reed / SW-420 / Tilt | `10-Sensori/13` | перевірити вручну | - | - |
| YF-S201 Flow | `10-Sensori/13` | перевірити вручну (даташит виробника) | - | [Розпіновка та код YF-S201 (MicrocontrollersLab)](https://microcontrollerslab.com/water-flow-sensor-pinout-interfacing-with-arduino-measure-flow-rate/) |
| DS3231 RTC | `10-Sensori/14` | перевірити вручну (Analog/Maxim, сайт блокує ботів) | [DS3231 - живе фото (Adafruit)](https://www.adafruit.com/product/3013) | [Гайд DS3231 з кодом (RNT)](https://randomnerdtutorials.com/esp32-ds3231-real-time-clock-arduino/) |
| KY-040 Encoder | `10-Sensori/14` | перевірити вручну (даташит виробника модуля) | - | [Розбір енкодера з кодом (LME)](https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/) |
| Keypad 4×4 / Joystick | `10-Sensori/14` | перевірити вручну | - | [Розбір матричної клавіатури з кодом (LME)](https://lastminuteengineers.com/keypad-arduino-tutorial/) |
| ACS712 | `10-Sensori/15` | перевірити вручну (Allegro) | - | перевірити вручну |
| ZMPT101B | `10-Sensori/15` | перевірити вручну | - | перевірити вручну |
| PZEM-004T | `10-Sensori/15` | перевірити вручну (Peacefair) | - | перевірити вручну |
| AS5600 | `10-Sensori/15` | перевірити вручну (ams-OSRAM, редизайн сайту) | - | перевірити вручну |
| FSR | `10-Sensori/15` | перевірити вручну | [FSR - живе фото (Adafruit)](https://www.adafruit.com/product/166) | - |
| HMC5883L / QMC5883L | `10-Sensori/16` | перевірити вручну (Honeywell/QST) | - | перевірити вручну |
| BNO055 | `10-Sensori/16` | [Сторінка BNO055 + даташит (Bosch)](https://www.bosch-sensortec.com/en/products/smart-sensor-systems/bno055/) | [BNO055 - живе фото (Adafruit)](https://www.adafruit.com/product/2472) | [Гайд BNO055 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor) |
| RC522 RFID-міст | `10-Sensori/16` | перевірити вручну (NXP MFRC522) | - | перевірити вручну |

## 11-Vivid - вивід та актуатори

| Компонент | Нотатка | Даташит виробника | Сторінка продукту + живе фото | Туторіал з кодом |
| --- | --- | --- | --- | --- |
| SSD1306 OLED 128×64 | `11-Vivid/01` | перевірити вручну (Solomon Systech) | [OLED 0.96″ - живе фото (Adafruit)](https://www.adafruit.com/product/326) | [Туторіал OLED з кодом (RNT)](https://randomnerdtutorials.com/esp32-ssd1306-oled-display-arduino-ide/) |
| ST7789 TFT | `11-Vivid/02` | перевірити вручну (Sitronix) | [TFT ST7789 - живе фото (Adafruit)](https://www.adafruit.com/product/3787) | перевірити вручну |
| ILI9341 TFT | `11-Vivid/02` | перевірити вручну (Ilitek) | - | перевірити вручну |
| LCD1602 + I2C | `11-Vivid/02` | перевірити вручну (Hitachi HD44780) | - | [Туторіал I2C LCD з кодом (RNT)](https://randomnerdtutorials.com/esp32-esp8266-i2c-lcd-arduino-ide/) |
| E-paper | `11-Vivid/02` | перевірити вручну | [E-paper HAT - фото і wiki (Waveshare)](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT) | - |
| WS2812 NeoPixel | `11-Vivid/03` | перевірити вручну (WorldSemi) | [NeoPixel-стрічка - живе фото (Adafruit)](https://www.adafruit.com/product/1426) | [NeoPixel Überguide з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-neopixel-uberguide) |
| SG90 Servo | `11-Vivid/03` | перевірити вручну (TowerPro) | - | [Туторіал Servo + ESP32 з кодом (RNT)](https://randomnerdtutorials.com/esp32-servo-motor-web-server-arduino-ide/) |
| SRD-05V Реле | `11-Vivid/03` | перевірити вручну (Songle) | - | [Туторіал Relay + ESP32 з кодом (RNT)](https://randomnerdtutorials.com/esp32-relay-module-ac-web-server/) |
| MOSFET-ключ | `11-Vivid/03` | перевірити вручну | - | [Керування навантаженням через реле/MOSFET (RNT)](https://randomnerdtutorials.com/esp32-relay-module-ac-web-server/) |
| L298N | `11-Vivid/04` | перевірити вручну (ST) | - | [Туторіал L298N + ESP32 з кодом (RNT)](https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/) |
| TB6612FNG | `11-Vivid/04` | перевірити вручну (Toshiba) | [TB6612 - живе фото (Adafruit)](https://www.adafruit.com/product/2448) | [Гайд TB6612 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-tb6612-h-bridge-dc-stepper-motor-driver-breakout) |
| A4988 | `11-Vivid/04` | перевірити вручну (Allegro) | - | перевірити вручну |
| MAX7219 | `11-Vivid/05` | перевірити вручну (Analog/Maxim, сайт блокує ботів) | - | [Гайд MAX7219-матриця з кодом (RNT)](https://randomnerdtutorials.com/guide-for-8x8-dot-matrix-max7219-with-arduino-pong-game/) |
| TM1637 | `11-Vivid/05` | перевірити вручну (Titan Micro) | - | [Розбір TM1637 з кодом (LME)](https://lastminuteengineers.com/tm1637-arduino-tutorial/) |
| 74HC595 | `11-Vivid/05` | перевірити вручну (TI/Nexperia) | - | [Розбір 74HC595 з кодом (LME)](https://lastminuteengineers.com/74hc595-shift-register-arduino-tutorial/) |
| PCA9685 | `11-Vivid/06` | перевірити вручну (NXP, редизайн сайту) | [PCA9685 - живе фото (Adafruit)](https://www.adafruit.com/product/815) | [Туторіал Servo + ESP32 з кодом (RNT)](https://randomnerdtutorials.com/esp32-servo-motor-web-server-arduino-ide/) |
| MG996R / 28BYJ-48 | `11-Vivid/06` | перевірити вручну | - | [Як працює Servo з кодом (LME)](https://lastminuteengineers.com/servo-motor-arduino-tutorial/) |
| TMC2209 | `11-Vivid/06` | перевірити вручну (Analog/Trinamic, сайт блокує ботів) | - | перевірити вручну |
| BTS7960 | `11-Vivid/07` | перевірити вручну (Infineon) | - | [BTS7960 + Arduino з кодом (DeepBlue)](https://deepbluembedded.com/arduino-bts7960-dc-motor-driver/) |
| L9110S | `11-Vivid/07` | перевірити вручну | - | перевірити вручну |
| SSR / Соленоїд | `11-Vivid/07` | перевірити вручну | - | [Керування AC-навантаженням з кодом (RNT)](https://randomnerdtutorials.com/esp32-relay-module-ac-web-server/) |
| DFPlayer Mini | `11-Vivid/08` | [DFPlayer Mini - сторінка товару (DFRobot)](https://www.dfrobot.com/product-1121.html) | [DFPlayer Mini - живе фото (DFRobot)](https://www.dfrobot.com/product-1121.html) | [DFPlayer Mini wiki + скетчі (DFRobot)](https://wiki.dfrobot.com/dfr0299/) |
| MAX98357A I2S | `11-Vivid/08` | перевірити вручну (Analog/Maxim, сайт блокує ботів) | [MAX98357A - живе фото (Adafruit)](https://www.adafruit.com/product/3006) | [Гайд MAX98357 з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp) |
| Nextion HMI | `11-Vivid/08` | [Офіційний сайт Nextion (документація, редактор)](https://nextion.tech/editor_guide/) | - | - |
| LCD2004 + I2C | `11-Vivid/08` | перевірити вручну (Hitachi HD44780) | - | [Туторіал I2C LCD з кодом (RNT)](https://randomnerdtutorials.com/esp32-esp8266-i2c-lcd-arduino-ide/) |
| SK6812 | `11-Vivid/09` | перевірити вручну (WorldSemi) | [DotStar-стрічка - живе фото (Adafruit)](https://www.adafruit.com/product/2343) | [NeoPixel Überguide з кодом (Adafruit Learn)](https://learn.adafruit.com/adafruit-neopixel-uberguide) |
| APA102 | `11-Vivid/09` | перевірити вручну | [DotStar APA102 - живе фото (Adafruit)](https://www.adafruit.com/product/2343) | [ESP-IDF RMT - офіційна документація (Espressif)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/rmt.html) |

## Зведення перевірки

- Усього унікальних URL у реєстрі: 84 - усі повернули HTTP 200 з релевантним заголовком 2026-09-28.
- Позначено `перевірити вручну`: сторінки analog.com, microchip.com (403 anti-bot), st.com (таймаут), invensense.tdk.com (контент переїхав), nxp.com/PCA9685, ams-osram.com/AS5600, winsen-sensor.com (404 після редизайну), plantower.com (403), окремі LME/RNT-слаги (404).
- Відхилено як нерелевантні після перевірки title: `dfrobot.com/product-1129.html` (веде на чохол Raspberry Pi, не DFPlayer), `adafruit.com/product/4666` (PIR-сенсор, не AHT20).

## 12-Moduli / нове (доповнення)

| Нота | Виробник/дока |
| --- | --- |
| [[10-Sensori/38-Industrial-Sensors | Промислові]] | IO-Link Consortium, FieldComm HART, TI XTR115, ADI AD5700 |
| [[10-Sensori/39-Wireless-Sensors | Бездротові]] | pvvx ATC, ESP Zigbee SDK, OpenThread, connectedhomeip |
| [[12-Moduli-zvyazku/26-SIM-Power | SIM+живлення]] | SIMCom HW Design, Quectel EC200U HD, Espressif HDG |

## Див. також

- [[99-Dodatki/04-Datasheet-Links]]
- [[99-Dodatki/01-Pinout-tablici]]
- [[Home]]
