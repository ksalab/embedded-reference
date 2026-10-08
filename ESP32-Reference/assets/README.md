---
title: Assets README як додавати картинки
description: куди класти іменування формат wikilink список схем для домалювання
tags: [esp32, assets, obsidian, images]
date: 2026-09-27
---

# Assets - як додавати картинки

![[assets/img/placeholder.png]]

Загальні правила бази: [[Home]], приклад оформлення [[99-Dodatki/01-Pinout-tablici]], діагностика [[99-Dodatki/02-Troubleshooting-FAQ]], чек-листи [[99-Dodatki/03-Cheklisti-montazhu]], джерела [[99-Dodatki/04-Datasheet-Links]], живлення [[02-Zhivlennya/01-Lancjugi-zhivlennya]].

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

## 3. Формат вставки `![[assets/img/xxx.png|400]]`

- Базовий плейсхолдер у кожній нотатці: `![[assets/img/placeholder.png]]` - замінити на реальну схему коли зявиться.
- З розміром: `![[assets/img/rc522-scheme.png|500]]` (400-600 для схем, 300 для фото плат).
- З підписом: під картинкою курсивом `*Рис. RC522 - живлення 3.3V, SPI VSPI.*`
- Галерея: дві картинки поруч через таблицю 2 колонки або просто підряд з підписами.
- НЕ використовувати markdown `![](...)` з відносними шляхами - тільки wikilink-формат Obsidian для переносимості бази.

## 4. Список рекомендованих схем для домалювання (пріоритет)

| # | Схема | Для нотатки | Що має бути видно |
| --- | --- | --- | --- |
| 1 | rc522-scheme.png | [[12-Moduli-zvyazku/01-RC522-RFID]] | 3.3V (червоний хрест на 5V), VSPI 18/19/23/5, RST 22, конд. 100нФ |
| 2 | nrf24-wiring.png | [[12-Moduli-zvyazku/02-NRF24-LoRa]] | конд. 10 мкФ на VCC, CE 21 CSN 5, PA+LNA антена |
| 3 | lora-ra02-scheme.png | [[12-Moduli-zvyazku/02-NRF24-LoRa]] | NSS 5 RST 25 DIO0 26, антена 433/868, знак оклику без антени |
| 4 | sim800l-power-4v.png | [[12-Moduli-zvyazku/03-SIM800L-GPS]] | LM2596 4.0V + 1000 мкФ, товсті дроти, UART 16/17 |
| 5 | neo6m-uart.png | [[12-Moduli-zvyazku/03-SIM800L-GPS]] | TX->RX 16, PPS, вид неба |
| 6 | max485-de-re.png | [[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera]] | DE+RE на GPIO4, A/B вита пара, 120 Ом |
| 7 | can-hvd230-bus.png | [[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera]] | CTX/CRX, CANH/CANL, 2x120 Ом |
| 8 | buck-mp1584-trim.png | [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar]] | підстроєчник, мультиметр 5.0V, порядок налаштування |
| 9 | solar-cn3791-full.png | [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar]] | Solar->CN3791->18650->MT3608->ESP32 + дільники ADC |
| 10 | txs0108-i2c.png | [[13-Moduli-zhivlennya-rivniv/02-Level-Shifters]] | VCCA 3.3V VCCB 5V, OE, A/B сторони |
| 11 | pinout-devkit-s3-c3.png (3 шт) | [[99-Dodatki/01-Pinout-tablici]] | кольорові strapping/ADC/SPI/I2C |
| 12 | brownout-scope.png | [[99-Dodatki/02-Troubleshooting-FAQ]] | просадка при WiFi TX до 2.9V |
| 13 | dht22-scheme.png | [[10-Sensori/01-DHT11-DHT22]] | 3V3, GPIO4 DATA, pull-up 4.7-10к, 100 нФ на довгих лініях |
| 14 | ds18b20-1wire.png | [[10-Sensori/02-DS18B20 | DS18B20]] | VDD 3V3, DQ GPIO4, pull-up 4.7к, вита пара, шина до 10 датчиків |
| 15 | bme280-i2c.png | [[10-Sensori/03-BME280-BMP280-SHT31]] | VIN 3V3, SDA 21 SCL 22, SDO→GND 0x76, CSB→VCC |
| 16 | mpu6050-i2c.png | [[10-Sensori/04-MPU6050 | MPU6050]] | VCC 3V3, SDA/SCL, AD0→GND 0x68, INT→GPIO15 |
| 17 | hcsr04-divider.png | [[10-Sensori/05-HC-SR04-PIR]] | VCC 5V, Trig GPIO5, Echo через дільник 1к/2к на GPIO18 |
| 18 | ina219-hx711.png | [[10-Sensori/06-INA219-HX711-BH1750]] | INA219 Vin+/Vin− розрив плюса, HX711 DT/SCK 16/17, BH1750 та сама I2C |
| 19 | oled-ssd1306-i2c.png | [[11-Vivid/01-OLED-SSD1306]] | VCC 3V3, SDA 21 SCL 22 400 кГц, адреса 0x3C |
| 20 | tft-st7789-spi.png | [[11-Vivid/02-TFT-LCD-Epaper]] | VSPI 18/23/5, DC 2 RES 4, BLK PWM 15, 100 нФ |
| 21 | neopixel-5v.png | [[11-Vivid/03-NeoPixel-Servo-Rele-MOSFET]] | DIN через 330 Ом GPIO13, БЖ 5V 60мА×N, 1000 мкФ, спільний GND |
| 22 | l298n-tb6612.png | [[11-Vivid/04-L298N-TB6612-A4988-Buzzer]] | IN1/IN2 26/27, ENA PWM 14, окремий БЖ моторів, спільний GND |
| 23 | aht20-i2c.png | [[10-Sensori/03-BME280-BMP280-SHT31]] | AHT20 I2C 0x38, 3V3, калібрування після ввімкнення |
| 24 | sht40-i2c.png | [[10-Sensori/03-BME280-BMP280-SHT31]] | SHT40 I2C 0x44, heater проти конденсату, точність ±1.8 %RH |
| 25 | mh-z19-uart.png | [[10-Sensori/06-INA219-HX711-BH1750]] | MH-Z19 NDIR CO2, 5V + прогрів 3 хв, UART 9600 TX→RX16, PWM-вихід |
| 26 | pms5003-uart.png | [[10-Sensori/06-INA219-HX711-BH1750]] | PMS5003 пил, 5V вентилятор, UART 9600, рівень 3.3V через shift |
| 27 | ads1115-i2c.png | [[10-Sensori/06-INA219-HX711-BH1750]] | ADS1115 16-біт АЦП, I2C 0x48-0x4B (ADDR), PGA, диференційні входи |
| 28 | vl53l0x-i2c.png | [[10-Sensori/05-HC-SR04-PIR]] | VL53L0X ToF-лазер, I2C 0x29, XSHUT→GPIO, 2.8V через LDO модуля |
| 29 | ntc-divider.png | [[10-Sensori/02-DS18B20 | DS18B20]] | NTC 10к + 10к дільник на 3V3, середина→ADC GPIO34, бета-коефіцієнт |
| 30 | mq2-analog.png | [[10-Sensori/06-INA219-HX711-BH1750]] | MQ-2 газ, нагрівач 5V ~150 мА, AOUT→GPIO34, DOUT-поріг на GPIO35 |
| 31 | rcwl-0516-doppler.png | [[10-Sensori/05-HC-SR04-PIR]] | RCWL-0516 доплер, 4-28V, OUT 3.3V→GPIO13, чутливість крізь пластик |
| 32 | ds3231-rtc-i2c.png | [[04-Shini/03-I2C | I2C]] | DS3231 RTC, I2C 0x68, батарейка CR2032, SQW/INT будильник на RTC-GPIO |
| 33 | acs712-analog.png | [[10-Sensori/06-INA219-HX711-BH1750]] | ACS712 хол, 5V, нуль 2.5V через дільник в ADC, 66-185 мВ/А |
| 34 | pzem-004t-uart.png | [[10-Sensori/06-INA219-HX711-BH1750]] | PZEM-004T лічильник 220V, CT-кліщі, UART/Modbus через опторозвʼязку |
| 35 | mqtt-broker-lwt-scheme.png | [[15-Protokoli/01-MQTT | MQTT]] | вузли→брокер 1883/8883, LWT offline retained, keepalive + backoff |
| 36 | http-websocket-rest-scheme.png | [[15-Protokoli/02-HTTP-WebSocket]] | REST POST/GET, SSE /events, WS /ws дуплекс, CA-bundle |
| 37 | mdns-ntp-tls-scheme.png | [[15-Protokoli/03-mDNS-NTP-TLS]] | esp32.local одна підмережа, SNTP+TZ Київ, CA-bundle/TLS |
| 38 | provisioning-blufi-rainmaker-scheme.png | [[15-Protokoli/04-Provisioning | Provisioning]] | AP-портал/BLE protocomm→NVS→STA, таймаут, кнопка erase |
| 39 | cloud-pipeline-nodered-scheme.png | [[15-Protokoli/05-Cloud-Pipeline]] | MQTT→Node-RED→InfluxDB→Grafana, офлайн-буфер 50, NTP |
| 40 | gas-co2-precision-scheme.png | [[10-Sensori/17-Gas-CO2-Precision]] | SGP30/SCD30/SEN5x, прогрів 12-48г, baseline, ABC |
| 41 | light-spectral-gesture-scheme.png | [[10-Sensori/18-Light-Spectral-Gesture]] | TSL2591/AS7341/VL53L1X/APDS9960, ROI, жести |
| 42 | imu-6-9dof-scheme.png | [[10-Sensori/19-IMU-6-9DOF]] | ADXL345/LSM6DS/ICM-20948/BNO08x, fusion, калібрування |
| 43 | bio-ir-temp-scheme.png | [[10-Sensori/20-Bio-IR-Temp]] | MAX30102 SpO2, MLX90614 FOV, емісивність |
| 44 | energy-meters-scheme.png | [[10-Sensori/21-Energy-Meters]] | INA226/HLW/SDM120, НЕІЗОЛЬОВАНА мережа, запобіжник |
| 45 | displays-2-tft-smart-scheme.png | [[11-Vivid/10-Displays-2]] | ST7735/SH1106/DWIN-UART, сторінкова адресація |
| 46 | powermotion-bldc-foc-scheme.png | [[11-Vivid/11-PowerMotion-2]] | DRV8825/TB6600/TMC5160/FOC, 24-48V |
| 47 | cellular-nbiot-uartlora-scheme.png | [[12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa]] | SIM7080/A7670/E32/SX1262, антени різні |
| 48 | esp32-c2-p4-scheme.png | [[01-Hardware/09-ESP32-C2-P4]] | C2 вузол, P4 без радіо + C6 компаньйон |
| 53 | firmwares-wled-tasmota-scheme.png | [[15-Protokoli/06-Firmwares | Прошивки]] | WLED/Tasmota/Blynk/Homie, струм стрічок |
| 54 | notify-voice-telegram-scheme.png | [[15-Protokoli/07-Notify-Voice]] | Telegram-бот, CallMeBot, fauxmoESP |
| 55 | security-hardening-scheme.png | [[15-Protokoli/08-Security-Hardening]] | ланцюг довіри, чек-лист продакшену |
| 56 | usb-host-msc-hid-scheme.png | [[04-Shini/06-USB-OTG-JTAG]] | MSC/HID/UAC, VBUS 500мА |
| 57 | gas-2-voc-industrial-scheme.png | [[10-Sensori/22-Gas-2-VOC-Industrial]] | ENS160/SGP40/TGS/MQ/ZE08, прогрів |
| 58 | dust-co2-2-scheme.png | [[10-Sensori/23-Dust-CO2-2]] | SPS30/K30/SCD41, ABC-калібрування |
| 59 | pressure-level-scheme.png | [[10-Sensori/24-Pressure-Level-Flow]] | MS5611/MS5837/Піто/XKC-Y25 |
| 60 | mag-imu-2-scheme.png | [[10-Sensori/25-Mag-IMU-2]] | компас/холл/BMI270/BMA400 |
| 61 | light-uv-irarray-scheme.png | [[10-Sensori/26-Light-UV-IRArray-ToF]] | УФ/тепловізор/VL53L5CX/лідар |
| 62 | time-mem-io-scheme.png | [[10-Sensori/27-Time-Mem-IO-DAC]] | RTC/FRAM/TCA9548/ЦАП-24біт |
| 63 | industrial-fieldbus-scheme.png | [[12-Moduli-zvyazku/10-Industrial]] | CANopen/DMX/4-20мА/TRIAC, 220V |
| 64 | lab-instruments-scheme.png | [[17-Lab/01-Instruments | Прилади]] | burden voltage, ×10 щуп, PulseView |
| 65 | soldering-connectors-scheme.png | [[17-Lab/02-Soldering-Connectors]] | SN-28B, JST/WAGO, AWG |
| 66 | enclosure-cert-factory-scheme.png | [[17-Lab/03-Enclosure-Cert-Factory]] | IP65, CE/FCC, mfg-NVS, фейки |
| 67 | freertos-patterns-scheme.png | [[09-Proshivka/06-FreeRTOS-Patterns]] | pinning, mutex, автомат |
| 68 | testing-ci-scheme.png | [[09-Proshivka/07-Testing-CI]] | Unity, Actions, HIL, semver |
| 69 | tooling-deep-scheme.png | [[09-Proshivka/08-Tooling-Deep]] | Manager, PIO envs, ulab |
| 70 | tinyml-voice-scheme.png | [[12-Moduli-zvyazku/11-TinyML-Voice]] | Edge Impulse, wake word |
| 71 | pid-filters-scheme.png | [[06-Analog/03-PID-Filters]] | anti-windup, Kalman, гістерезис |
| 72 | matter-thread-zigbee-scheme.png | [[15-Protokoli/09-Matter-Thread-Zigbee]] | fabric, BR, ZHA/Z2M |
| 73 | ble-mesh-a2dp-hid-scheme.png | [[05-Radio/05-BLE-Mesh-A2DP-HID]] | моделі, A2DP-sink, HID |
| 74 | audio-codecs-es8388-scheme.png | [[11-Vivid/13-Audio-Codecs]] | I2S, MCLK, AudioKit |
| 75 | rc-protocols-sbus-mavlink-scheme.png | [[12-Moduli-zvyazku/12-RC-Protocols]] | інвертор, failsafe |
| 76 | camera-streaming-mjpeg-scheme.png | [[12-Moduli-zvyazku/13-Camera-Streaming]] | PSRAM, GRAYSCALE |
| 77 | lvgl-squareline-scheme.png | [[11-Vivid/12-LVGL-SquareLine]] | flush_cb, FPS від SPI |
| 78 | env-newgen-scheme.png | [[10-Sensori/28-Env-NewGen]] | BMP585/SEN66/AHT21 |
| 79 | range-lidar-60ghz-scheme.png | [[10-Sensori/29-Range-Lidar-60GHz]] | VL53L7CX/LD19/BGT60 |
| 80 | temp-precision-scheme.png | [[10-Sensori/30-Temp-Precision]] | MAX31856/PT1000 |
| 81 | imu-mag-3-scheme.png | [[10-Sensori/31-IMU-Mag-3]] | BMI088/RM3100 |
| 82 | light-color-2-scheme.png | [[10-Sensori/32-Light-Color-2]] | AS7262/OPT4001 |
| 83 | input-io-2-scheme.png | [[10-Sensori/33-Input-IO-2]] | TTP/MPR/AS5048 |
| 84 | displays-3-oled-tft-eve-scheme.png | [[11-Vivid/14-Displays-3]] | SSD1322/GC9A01/FT81x |
| 85 | eink-controllers-scheme.png | [[11-Vivid/15-EInk | EInk]] | SSD1680, partial |
| 86 | lcd-char-hd44780-scheme.png | [[11-Vivid/16-LCD-Char]] | CGRAM, PCF8574 |
| 87 | touchscreens-cap-res-scheme.png | [[11-Vivid/17-Touchscreens | Тачскріни]] | CST816/XPT2046 |
| 88 | buttons-switches-pots-scheme.png | [[10-Sensori/34-Buttons-Switches-Pots]] | NO-NC, дебаунс |
| 89 | proximity-industrial-inputs-scheme.png | [[12-Moduli-zvyazku/14-Proximity-Inputs]] | LJ12A3, PC817 |
| 90 | rfid-advanced-mifare-scheme.png | [[12-Moduli-zvyazku/15-RFID-Advanced]] | trailer, UHF, Wiegand |
| 91 | ble-gateway-tracker-scheme.png | [[05-Radio/06-BLE-Gateway-Tracker]] | ESPresense, pvvx |
| 92 | ble5-longrange-audio-scheme.png | [[05-Radio/07-BLE5-LongRange-Audio]] | Coded, LE Audio |
| 93 | i2s-deep-tdm-pdm-scheme.png | [[04-Shini/04-I2S | I2S]] | APLL, DMA, PDM |
| 94 | mp3-tts-amps-scheme.png | [[11-Vivid/18-MP3-TTS-Amps]] | JQ6500, SYN6288 |
| 95 | webradio-streaming-scheme.png | [[11-Vivid/19-WebRadio-Streaming]] | Icecast, helix |
| 96 | offline-voice-uart-scheme.png | [[12-Moduli-zvyazku/16-Offline-Voice]] | LD3320, CRC16 |
| 97 | voice-assistant-pipeline-scheme.png | [[15-Protokoli/10-Voice-Assistant]] | mWW, Wyoming |
| 98 | devboard-mini-s2s3-scheme.png | [[14-Devboards/10-Mini-Boards]] | STEMMA, LiPo |
| 99 | devboard-hmi-guition-scheme.png | [[14-Devboards/11-HMI-Boards]] | LVGL, живлення |
| 100 | devboard-retro-wearable-scheme.png | [[14-Devboards/12-Retro-Wearable]] | VGA, Meshtastic |
| 101 | esp32-c5-c61-scheme.png | [[01-Hardware/10-ESP32-C5-C61]] | WiFi6, міграція |
| 102 | gnss-rtk-zedf9p-scheme.png | [[12-Moduli-zvyazku/17-GNSS-RTK]] | база+ровер, NTRIP |
| 103 | cellular-lora-2-scheme.png | [[12-Moduli-zvyazku/18-Cellular-LoRa-2]] | Cat-1, SX1280 |
| 104 | wired-2-eth-can-tools-scheme.png | [[12-Moduli-zvyazku/19-Wired-2]] | ModbusTCP, SLCAN |
| 105 | nfc-biometry-2-scheme.png | [[12-Moduli-zvyazku/20-NFC-Biometry-2]] | DESFire, PWD |
| 106 | pcb-design-ground-scheme.png | [[17-Lab/04-PCB-Design]] | plane, ферит, TVS |
| 107 | sensor-tails-scheme.png | [[10-Sensori/35-Tails | Хвости]] | DPS368, TSOP |
| 108 | versions-matrix-scheme.png | [[99-Dodatki/07-Versions | Версії]] | гілки, штампи |
| 109 | motion-control-fluidnc-scheme.png | [[12-Moduli-zvyazku/21-Motion-Control]] | YAML, micro-ROS |
| 110 | automotive-obd-lin-scheme.png | [[12-Moduli-zvyazku/22-Automotive]] | PIDs, LIN |
| 111 | marine-time-nmea-scheme.png | [[12-Moduli-zvyazku/23-Marine-Time]] | PGN, DCF77 |
| 112 | agro-soil-weather-scheme.png | [[10-Sensori/36-Agro | Агро]] | NPK/7-в-1 Modbus, анемометр, опадомір, Atlas EZO, клапани 24VAC |
| 113 | bio-2-ecg-emg-scheme.png | [[10-Sensori/37-Bio-2]] | AD8232/MAX30003/ADS1299/MyoWare, RLD, фільтр 0.5-40 Гц |
| 114 | diy-instruments-ad9833-scheme.png | [[12-Moduli-zvyazku/24-DIY-Instruments]] | AD9833/GM328/CD74HC4067/DS2482/SC16IS750/W25Q32 |
| 115 | secure-elements-atecc-scheme.png | [[12-Moduli-zvyazku/25-Secure-Elements]] | ATECC608/SE050, mfg-NVS, espefuse, Secure Boot |
| 116 | mqtt-client-3stack-scheme.png | [[15-Protokoli/11-Cloud-2]] | esp-mqtt/PubSubClient/umqtt, QoS, TLS ~40 КБ |
| 117 | sim800l-sms-call-scheme.png | [[12-Moduli-zvyazku/03-SIM800L-GPS]] | SMS Text/PDU, ATD з ';', USSD, SAPBR, CSCLK |
| 118 | sim-powerholder-scheme.png | [[12-Moduli-zvyazku/26-SIM-Power]] | nano/eSIM, DET, buck 4V/3A, суперкап, шунт |
| 119 | industrial-sensors-iolink-hart-scheme.png | [[10-Sensori/38-Industrial-Sensors]] | 4-20 мА шунт, HART FSK, IO-Link C/Q |
| 120 | wireless-sensors-ble-thread-scheme.png | [[10-Sensori/39-Wireless-Sensors]] | BLE-маяки, Zigbee binding, Thread SED |
| 121 | devboard-c6-boards-scheme.png | [[14-Devboards/13-ESP32C6-Boards]] | WiFi6+15.4, GPIO8, native USB |
| 122 | devboard-h2-boards-scheme.png | [[14-Devboards/14-ESP32H2-Boards]] | Без WiFi!, SED, GPIO25-цегла |
| 123 | cloud-aws-iot-scheme.png | [[15-Protokoli/12-AWS-IoT]] | X.509, Shadow, Jobs, Fleet |
| 124 | cloud-azure-iot-scheme.png | [[15-Protokoli/13-Azure-IoT]] | SAS, DPS, Twins, Methods |
| 125 | mqtt-sn-gateway-scheme.png | [[15-Protokoli/14-MQTT-SN]] | UDP, topic-id, шлюз |
| 126 | stencil-reflow-profile-scheme.png | [[13-Moduli-zhivlennya-rivniv/07-Stencil-Reflow]] | Апертури, профіль SAC305 |
| 127 | conformal-coating-ip65-scheme.png | [[13-Moduli-zhivlennya-rivniv/08-Conformal-Coating]] | Лак, маскування, компаунд |
| 128 | idf-setup-build-scheme.png | [[09-Proshivka/01-ESP-IDF-setup]] | install/export, set-target, build/flash/monitor |
| 129 | arduino-pio-flow-scheme.png | [[09-Proshivka/02-Arduino-PlatformIO]] | Ядро/ini, lib_deps, Upload, JTAG-кнопка |
| 130 | micropython-flash-tools-scheme.png | [[09-Proshivka/03-MicroPython | MicroPython]] | erase/bin, Thonny/mpremote, boot/main, REPL |
| 131 | esptool-flash-verify-scheme.png | [[09-Proshivka/04-Esptool-Flash]] | BOOT+EN, офсети, verify, charge-only кабель |
| 132 | jtag-openocd-gdb-scheme.png | [[09-Proshivka/05-JTAG-Debug]] | TDI/TDO/TCK/TMS, OpenOCD, GDB |
| 133 | partitions-nvs-layout-scheme.png | [[08-Pamyat/01-Partitions-NVS]] | 0x8000, ota_0/1, NVS wear-leveling |
| 134 | filesystem-littlefs-fat-scheme.png | [[08-Pamyat/02-Filesystem | Файлові системи]] | LittleFS vs FATFS, знос кільцем |
| 135 | ota-dualbank-rollback-scheme.png | [[08-Pamyat/03-OTA | OTA]] | Два слоти, self-test, rollback |
| 136 | secureboot-flashenc-scheme.png | [[08-Pamyat/04-Secure-Boot-Encrypt]] | eFuse, підпис, XTS-AES, anti-rollback |
| 137 | cloud-platforms-firebase-shelly-scheme.png | [[15-Protokoli/15-Cloud-Platforms]] | Firebase/Shelly/Frigate/Supabase/Domoticz/Prometheus |
| 138 | usb-pd-trigger-profiles-scheme.png | [[13-Moduli-zhivlennya-rivniv/09-USB-PD]] | Rd/Rp, CH224K, C-C, FUSB302 |
| 139 | fuel-gauge-soc-scheme.png | [[02-Zhivlennya/05-Fuel-Gauge]] | MAX17048/LC709203/BQ27441, ALRT |
| 140 | tpl5110-nanotimer-power-scheme.png | [[07-Timeri-Son/04-TPL5110]] | 35 нА, DONE, MOSFET, NVS-лічильник |
| 141 | lpwan-alt-compare-scheme.png | [[12-Moduli-zvyazku/27-LPWAN-Alt]] | Sigfox/Weightless/MIOTY/Wize, TCO |
| 142 | uwb-dw3000-ranging-scheme.png | [[12-Moduli-zvyazku/28-UWB-2]] | DW3000, канали 5/9, TDoA/PDOA |
| 143 | lorawan-gateway-sx1302-scheme.png | [[12-Moduli-zvyazku/29-LoRaWAN-Gateway]] | SX1302, EU868, висота, ChirpStack |
| 144 | gpio-overview-matrix-scheme.png | [[03-GPIO/01-GPIO-oglyad]] | Матриця, струми, LED через резистор |
| 145 | gpio-strapping-boot-scheme.png | [[03-GPIO/02-Strapping-pini]] | GPIO0/2/5/12/15, download vs boot |
| 146 | gpio-pullup-levels-scheme.png | [[03-GPIO/03-Pidtyaguvannya-rivni]] | Pull 45к/4.7к, дільник, TXS0108 |
| 147 | gpio-interrupt-pwm-scheme.png | [[03-GPIO/04-Pererivannya-PWM]] | ISR-правила, LEDC, серво 50 Гц |
| 148 | gpio-rtc-sleep-scheme.png | [[03-GPIO/05-RTC-GPIO]] | Hold, ULP, EXT0/EXT1 |
| 49 | cookbook-weather-scheme.png | [[16-Proekti/01-Weather-Station]] | BME280+SHT40 I2C, deep-sleep 600с, solar TP4056+18650, MQTT JSON |
| 50 | cookbook-tracker-scheme.png | [[16-Proekti/02-GPS-Tracker]] | NEO-M8N UART2 + A7670 UART1 3.8V, MPU-wake, MQTT geofence |
| 51 | cookbook-access-scheme.png | [[16-Proekti/03-Access-Control]] | RC522 SPI 3.3V, реле GPIO27 + 1N4007, NVS allow/deny, OTA |
| 52 | cookbook-energy-scheme.png | [[16-Proekti/04-Energy-Monitor]] | PZEM-004T CT + 220V через запобіжник, UART-дільник, DIN-бокс |

## Див. також

- [[Home]]
- [[99-Dodatki/01-Pinout-tablici]]
- [[99-Dodatki/02-Troubleshooting-FAQ]]
- [[99-Dodatki/03-Cheklisti-montazhu]]
- [[99-Dodatki/04-Datasheet-Links]]
- [[12-Moduli-zvyazku/01-RC522-RFID]]
- [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar]]

![[assets/img/placeholder.png]]
| esp32-usb-host-deep-scheme.png | ESP32 USB-Host глибоко | OTG / UVC / HID / MSC / FS/HS |
