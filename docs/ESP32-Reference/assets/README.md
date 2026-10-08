---
title: Assets README як додавати картинки
description: куди класти іменування формат wikilink список схем для домалювання
tags: [esp32, assets, obsidian, images]
date: 2026-09-27
---

# Assets - як додавати картинки

![](../../../ESP32-Reference/assets/img/placeholder.png)

Загальні правила бази: [Home](../../../ESP32-Reference/Home.md), приклад оформлення [01-Pinout-tablici](../../../ESP32-Reference/99-Dodatki/01-Pinout-tablici.md), діагностика [02-Troubleshooting-FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md), чек-листи [03-Cheklisti-montazhu](../../../ESP32-Reference/99-Dodatki/03-Cheklisti-montazhu.md), джерела [04-Datasheet-Links](../../../ESP32-Reference/99-Dodatki/04-Datasheet-Links.md), живлення [01-Lancjugi-zhivlennya](../../../ESP32-Reference/02-Zhivlennya/01-Lancjugi-zhivlennya.md).

## 1. Куди класти

| Що | Куди | Приклад |
| --- | --- | --- |
| ESP32-модулі схеми | assets/img/ | assets/img/rc522-scheme.png |
| ESP32 живі фото | assets/img/ | assets/img/nrf24-wiring.jpg |
| ESP32 осцилограми | assets/img/ | assets/img/brownout-scope.png |
| ESP32 загальні | assets/img/ | assets/img/placeholder.png |

- Папка фізично: `/home/ksalab/projects/.memories/ESP32-Reference/assets/img/`
- Не класти в корінь розділів 12/13/99 - тільки в assets/img, щоб не ламати відносні лінки.
- Оригінали у високій роздільності зберігати як `xxx-raw.png`, в нотатку вставляти стиснуту копію до 1200px.

## 2. Іменування `img/<modul>-scheme.png`

- Формат: малі літери, дефіс, без пробілів і кирилиці: `rc522-scheme.png`, `nrf24-pa-lna-wiring.jpg`, `lora-ra02-433-antenna.png`.
- Суфікси: `-scheme` схема, `-wiring` монтаж, `-pinout` розпіновка, `-scope` осцилограма, `-photo` фото плати.
- Список зайнятих/запланованих імен (не дублювати):
  - `rc522-scheme.png`, `nrf24-wiring.png`, `lora-ra02-scheme.png`, `sim800l-power-4v.png`, `neo6m-uart.png`, `max485-de-re.png`, `can-hvd230-bus.png`, `lan8720-rmii.png`, `ov2640-s3-dvp.png`, `buck-mp1584-trim.png`, `boost-mt3608.png`, `tp4056-solar-cn3791.png`, `txs0108-i2c.png`, `pc817-isolation.png`.
  - `dht22-scheme.png`, `ds18b20-1wire.png`, `bme280-i2c.png`, `mpu6050-i2c.png`, `hcsr04-divider.png`, `ina219-hx711.png`, `oled-ssd1306-i2c.png`, `tft-st7789-spi.png`, `neopixel-5v.png`, `l298n-tb6612.png`.
  - `aht20-i2c.png`, `sht40-i2c.png`, `mh-z19-uart.png`, `pms5003-uart.png`, `ads1115-i2c.png`, `vl53l0x-i2c.png`, `ntc-divider.png`, `mq2-analog.png`, `rcwl-0516-doppler.png`, `ds3231-rtc-i2c.png`, `acs712-analog.png`, `pzem-004t-uart.png`.
  - `agro-soil-weather-scheme.png`, `bio-2-ecg-emg-scheme.png`, `diy-instruments-ad9833-scheme.png`, `secure-elements-atecc-scheme.png`, `mqtt-client-3stack-scheme.png`, `sim800l-sms-call-scheme.png`, `sim-powerholder-scheme.png`, `industrial-sensors-iolink-hart-scheme.png`, `wireless-sensors-ble-thread-scheme.png`, `devboard-c6-boards-scheme.png`, `devboard-h2-boards-scheme.png`, `cloud-aws-iot-scheme.png`, `cloud-azure-iot-scheme.png`, `mqtt-sn-gateway-scheme.png`, `stencil-reflow-profile-scheme.png`, `conformal-coating-ip65-scheme.png`,
  `idf-setup-build-scheme.png`, `arduino-pio-flow-scheme.png`, `micropython-flash-tools-scheme.png`,
  `esptool-flash-verify-scheme.png`, `jtag-openocd-gdb-scheme.png`, `partitions-nvs-layout-scheme.png`,
  `filesystem-littlefs-fat-scheme.png`, `ota-dualbank-rollback-scheme.png`, `secureboot-flashenc-scheme.png`,
  `cloud-platforms-firebase-shelly-scheme.png`, `usb-pd-trigger-profiles-scheme.png`, `fuel-gauge-soc-scheme.png`,
  `tpl5110-nanotimer-power-scheme.png`, `lpwan-alt-compare-scheme.png`, `uwb-dw3000-ranging-scheme.png`,
  `lorawan-gateway-sx1302-scheme.png`, `gpio-overview-matrix-scheme.png`, `gpio-strapping-boot-scheme.png`,
  `gpio-pullup-levels-scheme.png`, `gpio-interrupt-pwm-scheme.png`, `gpio-rtc-sleep-scheme.png`.

## 3. Формат вставки `![](../../../ESP32-Reference/assets/img/xxx.png)`

- Базовий плейсхолдер у кожній нотатці: `![](../../../ESP32-Reference/assets/img/placeholder.png)` - замінити на реальну схему коли зявиться.
- З розміром: `![](../../../ESP32-Reference/assets/img/rc522-scheme.png)` (400-600 для схем, 300 для фото плат).
- З підписом: під картинкою курсивом `*Рис. RC522 - живлення 3.3V, SPI VSPI.*`
- Галерея: дві картинки поруч через таблицю 2 колонки або просто підряд з підписами.
- НЕ використовувати markdown `![](...)` з відносними шляхами - тільки wikilink-формат Obsidian для переносимості бази.

## 4. Список рекомендованих схем для домалювання (пріоритет)

| # | Схема | Для нотатки | Що має бути видно |
| --- | --- | --- | --- |
| 1 | rc522-scheme.png | [01-RC522-RFID](../../../ESP32-Reference/12-Moduli-zvyazku/01-RC522-RFID.md) | 3.3V (червоний хрест на 5V), VSPI 18/19/23/5, RST 22, конд. 100нФ |
| 2 | nrf24-wiring.png | [02-NRF24-LoRa](../../../ESP32-Reference/12-Moduli-zvyazku/02-NRF24-LoRa.md) | конд. 10 мкФ на VCC, CE 21 CSN 5, PA+LNA антена |
| 3 | lora-ra02-scheme.png | [02-NRF24-LoRa](../../../ESP32-Reference/12-Moduli-zvyazku/02-NRF24-LoRa.md) | NSS 5 RST 25 DIO0 26, антена 433/868, знак оклику без антени |
| 4 | sim800l-power-4v.png | [03-SIM800L-GPS](../../../ESP32-Reference/12-Moduli-zvyazku/03-SIM800L-GPS.md) | LM2596 4.0V + 1000 мкФ, товсті дроти, UART 16/17 |
| 5 | neo6m-uart.png | [03-SIM800L-GPS](../../../ESP32-Reference/12-Moduli-zvyazku/03-SIM800L-GPS.md) | TX->RX 16, PPS, вид неба |
| 6 | max485-de-re.png | [04-RS485-CAN-Ethernet-Kamera](../../../ESP32-Reference/12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera.md) | DE+RE на GPIO4, A/B вита пара, 120 Ом |
| 7 | can-hvd230-bus.png | [04-RS485-CAN-Ethernet-Kamera](../../../ESP32-Reference/12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera.md) | CTX/CRX, CANH/CANL, 2x120 Ом |
| 8 | buck-mp1584-trim.png | [01-Buck-Boost-Solar](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md) | підстроєчник, мультиметр 5.0V, порядок налаштування |
| 9 | solar-cn3791-full.png | [01-Buck-Boost-Solar](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md) | Solar->CN3791->18650->MT3608->ESP32 + дільники ADC |
| 10 | txs0108-i2c.png | [02-Level-Shifters](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/02-Level-Shifters.md) | VCCA 3.3V VCCB 5V, OE, A/B сторони |
| 11 | pinout-devkit-s3-c3.png (3 шт) | [01-Pinout-tablici](../../../ESP32-Reference/99-Dodatki/01-Pinout-tablici.md) | кольорові strapping/ADC/SPI/I2C |
| 12 | brownout-scope.png | [02-Troubleshooting-FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md) | просадка при WiFi TX до 2.9V |
| 13 | dht22-scheme.png | [01-DHT11-DHT22](../../../ESP32-Reference/10-Sensori/01-DHT11-DHT22.md) | 3V3, GPIO4 DATA, pull-up 4.7-10к, 100 нФ на довгих лініях |
| 14 | ds18b20-1wire.png | [DS18B20](../../../ESP32-Reference/10-Sensori/02-DS18B20.md) | VDD 3V3, DQ GPIO4, pull-up 4.7к, вита пара, шина до 10 датчиків |
| 15 | bme280-i2c.png | [03-BME280-BMP280-SHT31](../../../ESP32-Reference/10-Sensori/03-BME280-BMP280-SHT31.md) | VIN 3V3, SDA 21 SCL 22, SDO→GND 0x76, CSB→VCC |
| 16 | mpu6050-i2c.png | [MPU6050](../../../ESP32-Reference/10-Sensori/04-MPU6050.md) | VCC 3V3, SDA/SCL, AD0→GND 0x68, INT→GPIO15 |
| 17 | hcsr04-divider.png | [05-HC-SR04-PIR](../../../ESP32-Reference/10-Sensori/05-HC-SR04-PIR.md) | VCC 5V, Trig GPIO5, Echo через дільник 1к/2к на GPIO18 |
| 18 | ina219-hx711.png | [06-INA219-HX711-BH1750](../../../ESP32-Reference/10-Sensori/06-INA219-HX711-BH1750.md) | INA219 Vin+/Vin− розрив плюса, HX711 DT/SCK 16/17, BH1750 та сама I2C |
| 19 | oled-ssd1306-i2c.png | [01-OLED-SSD1306](../../../ESP32-Reference/11-Vivid/01-OLED-SSD1306.md) | VCC 3V3, SDA 21 SCL 22 400 кГц, адреса 0x3C |
| 20 | tft-st7789-spi.png | [02-TFT-LCD-Epaper](../../../ESP32-Reference/11-Vivid/02-TFT-LCD-Epaper.md) | VSPI 18/23/5, DC 2 RES 4, BLK PWM 15, 100 нФ |
| 21 | neopixel-5v.png | [03-NeoPixel-Servo-Rele-MOSFET](../../../ESP32-Reference/11-Vivid/03-NeoPixel-Servo-Rele-MOSFET.md) | DIN через 330 Ом GPIO13, БЖ 5V 60мА×N, 1000 мкФ, спільний GND |
| 22 | l298n-tb6612.png | [04-L298N-TB6612-A4988-Buzzer](../../../ESP32-Reference/11-Vivid/04-L298N-TB6612-A4988-Buzzer.md) | IN1/IN2 26/27, ENA PWM 14, окремий БЖ моторів, спільний GND |
| 23 | aht20-i2c.png | [03-BME280-BMP280-SHT31](../../../ESP32-Reference/10-Sensori/03-BME280-BMP280-SHT31.md) | AHT20 I2C 0x38, 3V3, калібрування після ввімкнення |
| 24 | sht40-i2c.png | [03-BME280-BMP280-SHT31](../../../ESP32-Reference/10-Sensori/03-BME280-BMP280-SHT31.md) | SHT40 I2C 0x44, heater проти конденсату, точність ±1.8 %RH |
| 25 | mh-z19-uart.png | [06-INA219-HX711-BH1750](../../../ESP32-Reference/10-Sensori/06-INA219-HX711-BH1750.md) | MH-Z19 NDIR CO2, 5V + прогрів 3 хв, UART 9600 TX→RX16, PWM-вихід |
| 26 | pms5003-uart.png | [06-INA219-HX711-BH1750](../../../ESP32-Reference/10-Sensori/06-INA219-HX711-BH1750.md) | PMS5003 пил, 5V вентилятор, UART 9600, рівень 3.3V через shift |
| 27 | ads1115-i2c.png | [06-INA219-HX711-BH1750](../../../ESP32-Reference/10-Sensori/06-INA219-HX711-BH1750.md) | ADS1115 16-біт АЦП, I2C 0x48-0x4B (ADDR), PGA, диференційні входи |
| 28 | vl53l0x-i2c.png | [05-HC-SR04-PIR](../../../ESP32-Reference/10-Sensori/05-HC-SR04-PIR.md) | VL53L0X ToF-лазер, I2C 0x29, XSHUT→GPIO, 2.8V через LDO модуля |
| 29 | ntc-divider.png | [DS18B20](../../../ESP32-Reference/10-Sensori/02-DS18B20.md) | NTC 10к + 10к дільник на 3V3, середина→ADC GPIO34, бета-коефіцієнт |
| 30 | mq2-analog.png | [06-INA219-HX711-BH1750](../../../ESP32-Reference/10-Sensori/06-INA219-HX711-BH1750.md) | MQ-2 газ, нагрівач 5V ~150 мА, AOUT→GPIO34, DOUT-поріг на GPIO35 |
| 31 | rcwl-0516-doppler.png | [05-HC-SR04-PIR](../../../ESP32-Reference/10-Sensori/05-HC-SR04-PIR.md) | RCWL-0516 доплер, 4-28V, OUT 3.3V→GPIO13, чутливість крізь пластик |
| 32 | ds3231-rtc-i2c.png | [I2C](../../../ESP32-Reference/04-Shini/03-I2C.md) | DS3231 RTC, I2C 0x68, батарейка CR2032, SQW/INT будильник на RTC-GPIO |
| 33 | acs712-analog.png | [06-INA219-HX711-BH1750](../../../ESP32-Reference/10-Sensori/06-INA219-HX711-BH1750.md) | ACS712 хол, 5V, нуль 2.5V через дільник в ADC, 66-185 мВ/А |
| 34 | pzem-004t-uart.png | [06-INA219-HX711-BH1750](../../../ESP32-Reference/10-Sensori/06-INA219-HX711-BH1750.md) | PZEM-004T лічильник 220V, CT-кліщі, UART/Modbus через опторозвʼязку |
| 35 | mqtt-broker-lwt-scheme.png | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) | вузли→брокер 1883/8883, LWT offline retained, keepalive + backoff |
| 36 | http-websocket-rest-scheme.png | [02-HTTP-WebSocket](../../../ESP32-Reference/15-Protokoli/02-HTTP-WebSocket.md) | REST POST/GET, SSE /events, WS /ws дуплекс, CA-bundle |
| 37 | mdns-ntp-tls-scheme.png | [03-mDNS-NTP-TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) | esp32.local одна підмережа, SNTP+TZ Київ, CA-bundle/TLS |
| 38 | provisioning-blufi-rainmaker-scheme.png | [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) | AP-портал/BLE protocomm→NVS→STA, таймаут, кнопка erase |
| 39 | cloud-pipeline-nodered-scheme.png | [05-Cloud-Pipeline](../../../ESP32-Reference/15-Protokoli/05-Cloud-Pipeline.md) | MQTT→Node-RED→InfluxDB→Grafana, офлайн-буфер 50, NTP |
| 40 | gas-co2-precision-scheme.png | [17-Gas-CO2-Precision](../../../ESP32-Reference/10-Sensori/17-Gas-CO2-Precision.md) | SGP30/SCD30/SEN5x, прогрів 12-48г, baseline, ABC |
| 41 | light-spectral-gesture-scheme.png | [18-Light-Spectral-Gesture](../../../ESP32-Reference/10-Sensori/18-Light-Spectral-Gesture.md) | TSL2591/AS7341/VL53L1X/APDS9960, ROI, жести |
| 42 | imu-6-9dof-scheme.png | [19-IMU-6-9DOF](../../../ESP32-Reference/10-Sensori/19-IMU-6-9DOF.md) | ADXL345/LSM6DS/ICM-20948/BNO08x, fusion, калібрування |
| 43 | bio-ir-temp-scheme.png | [20-Bio-IR-Temp](../../../ESP32-Reference/10-Sensori/20-Bio-IR-Temp.md) | MAX30102 SpO2, MLX90614 FOV, емісивність |
| 44 | energy-meters-scheme.png | [21-Energy-Meters](../../../ESP32-Reference/10-Sensori/21-Energy-Meters.md) | INA226/HLW/SDM120, НЕІЗОЛЬОВАНА мережа, запобіжник |
| 45 | displays-2-tft-smart-scheme.png | [10-Displays-2](../../../ESP32-Reference/11-Vivid/10-Displays-2.md) | ST7735/SH1106/DWIN-UART, сторінкова адресація |
| 46 | powermotion-bldc-foc-scheme.png | [11-PowerMotion-2](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md) | DRV8825/TB6600/TMC5160/FOC, 24-48V |
| 47 | cellular-nbiot-uartlora-scheme.png | [09-Cellular-NBIoT-UARTLoRa](../../../ESP32-Reference/12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa.md) | SIM7080/A7670/E32/SX1262, антени різні |
| 48 | esp32-c2-p4-scheme.png | [09-ESP32-C2-P4](../../../ESP32-Reference/01-Hardware/09-ESP32-C2-P4.md) | C2 вузол, P4 без радіо + C6 компаньйон |
| 53 | firmwares-wled-tasmota-scheme.png | [Прошивки](../../../ESP32-Reference/15-Protokoli/06-Firmwares.md) | WLED/Tasmota/Blynk/Homie, струм стрічок |
| 54 | notify-voice-telegram-scheme.png | [07-Notify-Voice](../../../ESP32-Reference/15-Protokoli/07-Notify-Voice.md) | Telegram-бот, CallMeBot, fauxmoESP |
| 55 | security-hardening-scheme.png | [08-Security-Hardening](../../../ESP32-Reference/15-Protokoli/08-Security-Hardening.md) | ланцюг довіри, чек-лист продакшену |
| 56 | usb-host-msc-hid-scheme.png | [06-USB-OTG-JTAG](../../../ESP32-Reference/04-Shini/06-USB-OTG-JTAG.md) | MSC/HID/UAC, VBUS 500мА |
| 57 | gas-2-voc-industrial-scheme.png | [22-Gas-2-VOC-Industrial](../../../ESP32-Reference/10-Sensori/22-Gas-2-VOC-Industrial.md) | ENS160/SGP40/TGS/MQ/ZE08, прогрів |
| 58 | dust-co2-2-scheme.png | [23-Dust-CO2-2](../../../ESP32-Reference/10-Sensori/23-Dust-CO2-2.md) | SPS30/K30/SCD41, ABC-калібрування |
| 59 | pressure-level-scheme.png | [24-Pressure-Level-Flow](../../../ESP32-Reference/10-Sensori/24-Pressure-Level-Flow.md) | MS5611/MS5837/Піто/XKC-Y25 |
| 60 | mag-imu-2-scheme.png | [25-Mag-IMU-2](../../../ESP32-Reference/10-Sensori/25-Mag-IMU-2.md) | компас/холл/BMI270/BMA400 |
| 61 | light-uv-irarray-scheme.png | [26-Light-UV-IRArray-ToF](../../../ESP32-Reference/10-Sensori/26-Light-UV-IRArray-ToF.md) | УФ/тепловізор/VL53L5CX/лідар |
| 62 | time-mem-io-scheme.png | [27-Time-Mem-IO-DAC](../../../ESP32-Reference/10-Sensori/27-Time-Mem-IO-DAC.md) | RTC/FRAM/TCA9548/ЦАП-24біт |
| 63 | industrial-fieldbus-scheme.png | [10-Industrial](../../../ESP32-Reference/12-Moduli-zvyazku/10-Industrial.md) | CANopen/DMX/4-20мА/TRIAC, 220V |
| 64 | lab-instruments-scheme.png | [Прилади](../../../ESP32-Reference/17-Lab/01-Instruments.md) | burden voltage, ×10 щуп, PulseView |
| 65 | soldering-connectors-scheme.png | [02-Soldering-Connectors](../../../ESP32-Reference/17-Lab/02-Soldering-Connectors.md) | SN-28B, JST/WAGO, AWG |
| 66 | enclosure-cert-factory-scheme.png | [03-Enclosure-Cert-Factory](../../../ESP32-Reference/17-Lab/03-Enclosure-Cert-Factory.md) | IP65, CE/FCC, mfg-NVS, фейки |
| 67 | freertos-patterns-scheme.png | [06-FreeRTOS-Patterns](../../../ESP32-Reference/09-Proshivka/06-FreeRTOS-Patterns.md) | pinning, mutex, автомат |
| 68 | testing-ci-scheme.png | [07-Testing-CI](../../../ESP32-Reference/09-Proshivka/07-Testing-CI.md) | Unity, Actions, HIL, semver |
| 69 | tooling-deep-scheme.png | [08-Tooling-Deep](../../../ESP32-Reference/09-Proshivka/08-Tooling-Deep.md) | Manager, PIO envs, ulab |
| 70 | tinyml-voice-scheme.png | [11-TinyML-Voice](../../../ESP32-Reference/12-Moduli-zvyazku/11-TinyML-Voice.md) | Edge Impulse, wake word |
| 71 | pid-filters-scheme.png | [03-PID-Filters](../../../ESP32-Reference/06-Analog/03-PID-Filters.md) | anti-windup, Kalman, гістерезис |
| 72 | matter-thread-zigbee-scheme.png | [09-Matter-Thread-Zigbee](../../../ESP32-Reference/15-Protokoli/09-Matter-Thread-Zigbee.md) | fabric, BR, ZHA/Z2M |
| 73 | ble-mesh-a2dp-hid-scheme.png | [05-BLE-Mesh-A2DP-HID](../../../ESP32-Reference/05-Radio/05-BLE-Mesh-A2DP-HID.md) | моделі, A2DP-sink, HID |
| 74 | audio-codecs-es8388-scheme.png | [13-Audio-Codecs](../../../ESP32-Reference/11-Vivid/13-Audio-Codecs.md) | I2S, MCLK, AudioKit |
| 75 | rc-protocols-sbus-mavlink-scheme.png | [12-RC-Protocols](../../../ESP32-Reference/12-Moduli-zvyazku/12-RC-Protocols.md) | інвертор, failsafe |
| 76 | camera-streaming-mjpeg-scheme.png | [13-Camera-Streaming](../../../ESP32-Reference/12-Moduli-zvyazku/13-Camera-Streaming.md) | PSRAM, GRAYSCALE |
| 77 | lvgl-squareline-scheme.png | [12-LVGL-SquareLine](../../../ESP32-Reference/11-Vivid/12-LVGL-SquareLine.md) | flush_cb, FPS від SPI |
| 78 | env-newgen-scheme.png | [28-Env-NewGen](../../../ESP32-Reference/10-Sensori/28-Env-NewGen.md) | BMP585/SEN66/AHT21 |
| 79 | range-lidar-60ghz-scheme.png | [29-Range-Lidar-60GHz](../../../ESP32-Reference/10-Sensori/29-Range-Lidar-60GHz.md) | VL53L7CX/LD19/BGT60 |
| 80 | temp-precision-scheme.png | [30-Temp-Precision](../../../ESP32-Reference/10-Sensori/30-Temp-Precision.md) | MAX31856/PT1000 |
| 81 | imu-mag-3-scheme.png | [31-IMU-Mag-3](../../../ESP32-Reference/10-Sensori/31-IMU-Mag-3.md) | BMI088/RM3100 |
| 82 | light-color-2-scheme.png | [32-Light-Color-2](../../../ESP32-Reference/10-Sensori/32-Light-Color-2.md) | AS7262/OPT4001 |
| 83 | input-io-2-scheme.png | [33-Input-IO-2](../../../ESP32-Reference/10-Sensori/33-Input-IO-2.md) | TTP/MPR/AS5048 |
| 84 | displays-3-oled-tft-eve-scheme.png | [14-Displays-3](../../../ESP32-Reference/11-Vivid/14-Displays-3.md) | SSD1322/GC9A01/FT81x |
| 85 | eink-controllers-scheme.png | [EInk](../../../ESP32-Reference/11-Vivid/15-EInk.md) | SSD1680, partial |
| 86 | lcd-char-hd44780-scheme.png | [16-LCD-Char](../../../ESP32-Reference/11-Vivid/16-LCD-Char.md) | CGRAM, PCF8574 |
| 87 | touchscreens-cap-res-scheme.png | [Тачскріни](../../../ESP32-Reference/11-Vivid/17-Touchscreens.md) | CST816/XPT2046 |
| 88 | buttons-switches-pots-scheme.png | [34-Buttons-Switches-Pots](../../../ESP32-Reference/10-Sensori/34-Buttons-Switches-Pots.md) | NO-NC, дебаунс |
| 89 | proximity-industrial-inputs-scheme.png | [14-Proximity-Inputs](../../../ESP32-Reference/12-Moduli-zvyazku/14-Proximity-Inputs.md) | LJ12A3, PC817 |
| 90 | rfid-advanced-mifare-scheme.png | [15-RFID-Advanced](../../../ESP32-Reference/12-Moduli-zvyazku/15-RFID-Advanced.md) | trailer, UHF, Wiegand |
| 91 | ble-gateway-tracker-scheme.png | [06-BLE-Gateway-Tracker](../../../ESP32-Reference/05-Radio/06-BLE-Gateway-Tracker.md) | ESPresense, pvvx |
| 92 | ble5-longrange-audio-scheme.png | [07-BLE5-LongRange-Audio](../../../ESP32-Reference/05-Radio/07-BLE5-LongRange-Audio.md) | Coded, LE Audio |
| 93 | i2s-deep-tdm-pdm-scheme.png | [I2S](../../../ESP32-Reference/04-Shini/04-I2S.md) | APLL, DMA, PDM |
| 94 | mp3-tts-amps-scheme.png | [18-MP3-TTS-Amps](../../../ESP32-Reference/11-Vivid/18-MP3-TTS-Amps.md) | JQ6500, SYN6288 |
| 95 | webradio-streaming-scheme.png | [19-WebRadio-Streaming](../../../ESP32-Reference/11-Vivid/19-WebRadio-Streaming.md) | Icecast, helix |
| 96 | offline-voice-uart-scheme.png | [16-Offline-Voice](../../../ESP32-Reference/12-Moduli-zvyazku/16-Offline-Voice.md) | LD3320, CRC16 |
| 97 | voice-assistant-pipeline-scheme.png | [10-Voice-Assistant](../../../ESP32-Reference/15-Protokoli/10-Voice-Assistant.md) | mWW, Wyoming |
| 98 | devboard-mini-s2s3-scheme.png | [10-Mini-Boards](../../../ESP32-Reference/14-Devboards/10-Mini-Boards.md) | STEMMA, LiPo |
| 99 | devboard-hmi-guition-scheme.png | [11-HMI-Boards](../../../ESP32-Reference/14-Devboards/11-HMI-Boards.md) | LVGL, живлення |
| 100 | devboard-retro-wearable-scheme.png | [12-Retro-Wearable](../../../ESP32-Reference/14-Devboards/12-Retro-Wearable.md) | VGA, Meshtastic |
| 101 | esp32-c5-c61-scheme.png | [10-ESP32-C5-C61](../../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md) | WiFi6, міграція |
| 102 | gnss-rtk-zedf9p-scheme.png | [17-GNSS-RTK](../../../ESP32-Reference/12-Moduli-zvyazku/17-GNSS-RTK.md) | база+ровер, NTRIP |
| 103 | cellular-lora-2-scheme.png | [18-Cellular-LoRa-2](../../../ESP32-Reference/12-Moduli-zvyazku/18-Cellular-LoRa-2.md) | Cat-1, SX1280 |
| 104 | wired-2-eth-can-tools-scheme.png | [19-Wired-2](../../../ESP32-Reference/12-Moduli-zvyazku/19-Wired-2.md) | ModbusTCP, SLCAN |
| 105 | nfc-biometry-2-scheme.png | [20-NFC-Biometry-2](../../../ESP32-Reference/12-Moduli-zvyazku/20-NFC-Biometry-2.md) | DESFire, PWD |
| 106 | pcb-design-ground-scheme.png | [04-PCB-Design](../../../ESP32-Reference/17-Lab/04-PCB-Design.md) | plane, ферит, TVS |
| 107 | sensor-tails-scheme.png | [Хвости](../../../ESP32-Reference/10-Sensori/35-Tails.md) | DPS368, TSOP |
| 108 | versions-matrix-scheme.png | [Версії](../../../ESP32-Reference/99-Dodatki/07-Versions.md) | гілки, штампи |
| 109 | motion-control-fluidnc-scheme.png | [21-Motion-Control](../../../ESP32-Reference/12-Moduli-zvyazku/21-Motion-Control.md) | YAML, micro-ROS |
| 110 | automotive-obd-lin-scheme.png | [22-Automotive](../../../ESP32-Reference/12-Moduli-zvyazku/22-Automotive.md) | PIDs, LIN |
| 111 | marine-time-nmea-scheme.png | [23-Marine-Time](../../../ESP32-Reference/12-Moduli-zvyazku/23-Marine-Time.md) | PGN, DCF77 |
| 112 | agro-soil-weather-scheme.png | [Агро](../../../ESP32-Reference/10-Sensori/36-Agro.md) | NPK/7-в-1 Modbus, анемометр, опадомір, Atlas EZO, клапани 24VAC |
| 113 | bio-2-ecg-emg-scheme.png | [37-Bio-2](../../../ESP32-Reference/10-Sensori/37-Bio-2.md) | AD8232/MAX30003/ADS1299/MyoWare, RLD, фільтр 0.5-40 Гц |
| 114 | diy-instruments-ad9833-scheme.png | [24-DIY-Instruments](../../../ESP32-Reference/12-Moduli-zvyazku/24-DIY-Instruments.md) | AD9833/GM328/CD74HC4067/DS2482/SC16IS750/W25Q32 |
| 115 | secure-elements-atecc-scheme.png | [25-Secure-Elements](../../../ESP32-Reference/12-Moduli-zvyazku/25-Secure-Elements.md) | ATECC608/SE050, mfg-NVS, espefuse, Secure Boot |
| 116 | mqtt-client-3stack-scheme.png | [11-Cloud-2](../../../ESP32-Reference/15-Protokoli/11-Cloud-2.md) | esp-mqtt/PubSubClient/umqtt, QoS, TLS ~40 КБ |
| 117 | sim800l-sms-call-scheme.png | [03-SIM800L-GPS](../../../ESP32-Reference/12-Moduli-zvyazku/03-SIM800L-GPS.md) | SMS Text/PDU, ATD з ';', USSD, SAPBR, CSCLK |
| 118 | sim-powerholder-scheme.png | [26-SIM-Power](../../../ESP32-Reference/12-Moduli-zvyazku/26-SIM-Power.md) | nano/eSIM, DET, buck 4V/3A, суперкап, шунт |
| 119 | industrial-sensors-iolink-hart-scheme.png | [38-Industrial-Sensors](../../../ESP32-Reference/10-Sensori/38-Industrial-Sensors.md) | 4-20 мА шунт, HART FSK, IO-Link C/Q |
| 120 | wireless-sensors-ble-thread-scheme.png | [39-Wireless-Sensors](../../../ESP32-Reference/10-Sensori/39-Wireless-Sensors.md) | BLE-маяки, Zigbee binding, Thread SED |
| 121 | devboard-c6-boards-scheme.png | [13-ESP32C6-Boards](../../../ESP32-Reference/14-Devboards/13-ESP32C6-Boards.md) | WiFi6+15.4, GPIO8, native USB |
| 122 | devboard-h2-boards-scheme.png | [14-ESP32H2-Boards](../../../ESP32-Reference/14-Devboards/14-ESP32H2-Boards.md) | Без WiFi!, SED, GPIO25-цегла |
| 123 | cloud-aws-iot-scheme.png | [12-AWS-IoT](../../../ESP32-Reference/15-Protokoli/12-AWS-IoT.md) | X.509, Shadow, Jobs, Fleet |
| 124 | cloud-azure-iot-scheme.png | [13-Azure-IoT](../../../ESP32-Reference/15-Protokoli/13-Azure-IoT.md) | SAS, DPS, Twins, Methods |
| 125 | mqtt-sn-gateway-scheme.png | [14-MQTT-SN](../../../ESP32-Reference/15-Protokoli/14-MQTT-SN.md) | UDP, topic-id, шлюз |
| 126 | stencil-reflow-profile-scheme.png | [07-Stencil-Reflow](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/07-Stencil-Reflow.md) | Апертури, профіль SAC305 |
| 127 | conformal-coating-ip65-scheme.png | [08-Conformal-Coating](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/08-Conformal-Coating.md) | Лак, маскування, компаунд |
| 128 | idf-setup-build-scheme.png | [01-ESP-IDF-setup](../../../ESP32-Reference/09-Proshivka/01-ESP-IDF-setup.md) | install/export, set-target, build/flash/monitor |
| 129 | arduino-pio-flow-scheme.png | [02-Arduino-PlatformIO](../../../ESP32-Reference/09-Proshivka/02-Arduino-PlatformIO.md) | Ядро/ini, lib_deps, Upload, JTAG-кнопка |
| 130 | micropython-flash-tools-scheme.png | [MicroPython](../../../ESP32-Reference/09-Proshivka/03-MicroPython.md) | erase/bin, Thonny/mpremote, boot/main, REPL |
| 131 | esptool-flash-verify-scheme.png | [04-Esptool-Flash](../../../ESP32-Reference/09-Proshivka/04-Esptool-Flash.md) | BOOT+EN, офсети, verify, charge-only кабель |
| 132 | jtag-openocd-gdb-scheme.png | [05-JTAG-Debug](../../../ESP32-Reference/09-Proshivka/05-JTAG-Debug.md) | TDI/TDO/TCK/TMS, OpenOCD, GDB |
| 133 | partitions-nvs-layout-scheme.png | [01-Partitions-NVS](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md) | 0x8000, ota_0/1, NVS wear-leveling |
| 134 | filesystem-littlefs-fat-scheme.png | [Файлові системи](../../../ESP32-Reference/08-Pamyat/02-Filesystem.md) | LittleFS vs FATFS, знос кільцем |
| 135 | ota-dualbank-rollback-scheme.png | [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md) | Два слоти, self-test, rollback |
| 136 | secureboot-flashenc-scheme.png | [04-Secure-Boot-Encrypt](../../../ESP32-Reference/08-Pamyat/04-Secure-Boot-Encrypt.md) | eFuse, підпис, XTS-AES, anti-rollback |
| 137 | cloud-platforms-firebase-shelly-scheme.png | [15-Cloud-Platforms](../../../ESP32-Reference/15-Protokoli/15-Cloud-Platforms.md) | Firebase/Shelly/Frigate/Supabase/Domoticz/Prometheus |
| 138 | usb-pd-trigger-profiles-scheme.png | [09-USB-PD](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/09-USB-PD.md) | Rd/Rp, CH224K, C-C, FUSB302 |
| 139 | fuel-gauge-soc-scheme.png | [05-Fuel-Gauge](../../../ESP32-Reference/02-Zhivlennya/05-Fuel-Gauge.md) | MAX17048/LC709203/BQ27441, ALRT |
| 140 | tpl5110-nanotimer-power-scheme.png | [04-TPL5110](../../../ESP32-Reference/07-Timeri-Son/04-TPL5110.md) | 35 нА, DONE, MOSFET, NVS-лічильник |
| 141 | lpwan-alt-compare-scheme.png | [27-LPWAN-Alt](../../../ESP32-Reference/12-Moduli-zvyazku/27-LPWAN-Alt.md) | Sigfox/Weightless/MIOTY/Wize, TCO |
| 142 | uwb-dw3000-ranging-scheme.png | [28-UWB-2](../../../ESP32-Reference/12-Moduli-zvyazku/28-UWB-2.md) | DW3000, канали 5/9, TDoA/PDOA |
| 143 | lorawan-gateway-sx1302-scheme.png | [29-LoRaWAN-Gateway](../../../ESP32-Reference/12-Moduli-zvyazku/29-LoRaWAN-Gateway.md) | SX1302, EU868, висота, ChirpStack |
| 144 | gpio-overview-matrix-scheme.png | [01-GPIO-oglyad](../../../ESP32-Reference/03-GPIO/01-GPIO-oglyad.md) | Матриця, струми, LED через резистор |
| 145 | gpio-strapping-boot-scheme.png | [02-Strapping-pini](../../../ESP32-Reference/03-GPIO/02-Strapping-pini.md) | GPIO0/2/5/12/15, download vs boot |
| 146 | gpio-pullup-levels-scheme.png | [03-Pidtyaguvannya-rivni](../../../ESP32-Reference/03-GPIO/03-Pidtyaguvannya-rivni.md) | Pull 45к/4.7к, дільник, TXS0108 |
| 147 | gpio-interrupt-pwm-scheme.png | [04-Pererivannya-PWM](../../../ESP32-Reference/03-GPIO/04-Pererivannya-PWM.md) | ISR-правила, LEDC, серво 50 Гц |
| 148 | gpio-rtc-sleep-scheme.png | [05-RTC-GPIO](../../../ESP32-Reference/03-GPIO/05-RTC-GPIO.md) | Hold, ULP, EXT0/EXT1 |
| 49 | cookbook-weather-scheme.png | [01-Weather-Station](../../../ESP32-Reference/16-Proekti/01-Weather-Station.md) | BME280+SHT40 I2C, deep-sleep 600с, solar TP4056+18650, MQTT JSON |
| 50 | cookbook-tracker-scheme.png | [02-GPS-Tracker](../../../ESP32-Reference/16-Proekti/02-GPS-Tracker.md) | NEO-M8N UART2 + A7670 UART1 3.8V, MPU-wake, MQTT geofence |
| 51 | cookbook-access-scheme.png | [03-Access-Control](../../../ESP32-Reference/16-Proekti/03-Access-Control.md) | RC522 SPI 3.3V, реле GPIO27 + 1N4007, NVS allow/deny, OTA |
| 52 | cookbook-energy-scheme.png | [04-Energy-Monitor](../../../ESP32-Reference/16-Proekti/04-Energy-Monitor.md) | PZEM-004T CT + 220V через запобіжник, UART-дільник, DIN-бокс |

## Див. також

- [Home](../../../ESP32-Reference/Home.md)
- [01-Pinout-tablici](../../../ESP32-Reference/99-Dodatki/01-Pinout-tablici.md)
- [02-Troubleshooting-FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md)
- [03-Cheklisti-montazhu](../../../ESP32-Reference/99-Dodatki/03-Cheklisti-montazhu.md)
- [04-Datasheet-Links](../../../ESP32-Reference/99-Dodatki/04-Datasheet-Links.md)
- [01-RC522-RFID](../../../ESP32-Reference/12-Moduli-zvyazku/01-RC522-RFID.md)
- [01-Buck-Boost-Solar](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md)

![](../../../ESP32-Reference/assets/img/placeholder.png)
| esp32-usb-host-deep-scheme.png | ESP32 USB-Host глибоко | OTG / UVC / HID / MSC / FS/HS |
