# Реєстр компонентів ESP32-Reference

> Згенеровано 2026-10-07: `python3 scripts/comp_inventory.py --registry COMPONENTS.md`. НЕ редагувати вручну — перегенерувати!
>
> ✅ = хоча б в одній ноті-згадці є посилання виробника. Це НЕ гарантує, що лінк саме на цей компонент — звіряти вручну!
>
> ❌ = у жодній ноті-згадці немає виробничих посилань. Пріоритетні кандидати на додавання даташитів.

**Позначень:** 896; **з datasheet:** 896; **без:** 0.

## Де шукати даташити (перевірено 2026-09-30)

| Сайт | Доступ ботом | Профіль |
| --- | --- | --- |
| alldatasheet.com (`view.jsp?Searchword=XXX`) | ❌ безпосередньо (403), ✅ через проксі/браузер; є дзеркала `alldatasheetru.com` та ін. | Найбільший архів; китайські/хобі-мікросхеми (GalaxyCore, Tontek, Holtek) |
| datasheets.com (`/search?q=XXX`) | ✅ | Західні каталогові + ціни/залишки (Microchip, TI, NXP); китайських дисплеїв/сенсорів немає |
| octopart.com (`/search?q=XXX`) | ✅ | Метапошук дистриб'юторів; тільки авторизовані канали — хобі-Китаю немає |
| findchips.com (`/search/XXX`) | ✅ | Те саме, що Octopart, швидший |
| lcsc.com (пошук на сайті) | ❌ JS — тільки вручну | Китайські компоненти: картка + PDF одразу |
| tme.eu / mouser.com / digikey.com | ❌ боти ріжуться — вручну | Параметричний пошук + гарантовано свіжий PDF виробника |
| alltransistors.com | ❌ боти ріжуться — вручну | Біполярники/MOSFET/діоди (BC547, SS14) |
| datasheetspdf.com | ❌ нестабільний — вручну | Дзеркало архіву |
| Сайти виробників (першоджерело!) | ✅ | `ti.com/lit`, `analog.com`, `nxp.com`, `st.com`, `microchip.com/en-us/product/XXX` — завжди свіжіше за агрегатори |

| Компонент | Категорії | Ноти-згадки | Datasheet |
| --- | --- | --- | --- |
| AA55 | модулі зв'язку | 16-Offline-Voice | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| AC101 | вивід/актуатори | 13-Audio-Codecs | ✅ `docs.espressif.com` |
| ACR122U | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| ACR1252U | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| ACS712 | сенсори, вивід/актуатори, проєкти, додатки | 15-ACS712-ZMPT101B-PZEM-AS5600-FSR, 11-PowerMotion-2, 04-Energy-Monitor, 02-Troubleshooting-FAQ +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| ADE7758 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| ADM2483 | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera | ✅ `www.ti.com` |
| ADM2587E | шини, модулі зв'язку | 01-UART, 10-Industrial | ✅ `learn.adafruit.com`, `www.alldatasheet.com`, `www.ti.com` |
| ADM3057E | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera | ✅ `www.ti.com` |
| ADS1115 | аналог, сенсори, модулі зв'язку, додатки | 01-ADC, 09-ADS1115-MCP3008-PCF8574-MCP23017, 11-NTC-PT100-MAX6675-LM35, 21-Energy-Meters +4 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| ADS1256 | сенсори, модулі зв'язку | 27-Time-Mem-IO-DAC, 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| ADS1292 | сенсори | 37-Bio-2 | ✅ `www.analog.com`, `www.ti.com` |
| ADS1299 | сенсори | 37-Bio-2 | ✅ `www.analog.com`, `www.ti.com` |
| ADS7843 | вивід/актуатори | 17-Touchscreens | ✅ `www.alldatasheet.com`, `www.ti.com` |
| ADS7866 | шини | 02-SPI | ✅ `www.ti.com` |
| ADT7410 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| ADXL345 | сенсори, модулі зв'язку | 19-IMU-6-9DOF, 21-Motion-Control | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| ADXL355 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| ADXL375 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| AHT10 | сенсори, плати, проєкти, додатки | 07-AHT10-AHT20-SHT40, 08-BME680-CCS811-MHZ19-PMS5003, 10-VL53L0X-TCS34725-TSL2561, 17-Gas-CO2-Precision +7 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| AHT20 | сенсори, плати, проєкти, додатки | 07-AHT10-AHT20-SHT40, 08-BME680-CCS811-MHZ19-PMS5003, 10-VL53L0X-TCS34725-TSL2561, 35-Tails +5 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| AHT21 | сенсори | 28-Env-NewGen | ✅ `sensirion.com`, `www.bosch-sensortec.com` |
| AHT25 | сенсори | 17-Gas-CO2-Precision, 35-Tails | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| AHT30 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| AK8963 | сенсори | 16-HMC5883-BNO055-RFID-RC522-Barcode | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| AM2302 | сенсори, додатки | 01-DHT11-DHT22, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| AMC1301 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| AMG8833 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| AMS1117 | старт, чипи/модулі, живлення, шини, таймери, вивід/актуатори, модулі зв'язку, живлення/рівні, плати, проєкти, лабораторія, додатки | 02-Glosariy, 03-Porivnyannya-chipiv, 04-Devkit-plati, 05-Moduli-WROOM-WROVER-MINI +21 | ✅ `assets.bosch-sensortec.com`, `circuitpython.org`, `docs.espressif.com` |
| AMT22 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| ANT1 | модулі зв'язку | 05-PN532-RDM6300-Fingerprint-GM65 | ✅ `www.nxp.com` |
| ANT2 | модулі зв'язку | 05-PN532-RDM6300-Fingerprint-GM65 | ✅ `www.nxp.com` |
| ANT2B | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| AOD4184 | аналог | 03-PID-Filters | ✅ `docs.espressif.com` |
| AP2112 | живлення, плати | 02-LDO-DC-DC, 07-Feather-Huzzah32-Thing, 10-Mini-Boards | ✅ `docs.arduino.cc`, `learn.adafruit.com`, `www.diodes.com` |
| APA102 | вивід/актуатори, плати, протоколи, додатки | 09-LED-Strip-Power-SK6812-APA102, 11-HMI-Boards, 06-Firmwares, 07-Notify-Voice +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| APDS9960 | сенсори | 18-Light-Spectral-Gesture, 32-Light-Color-2 | ✅ `ams-osram.com`, `learn.adafruit.com`, `www.nxp.com` |
| AQY212S | вивід/актуатори | 07-BTS7960-L9110S-SSR-Solenoid | ✅ `www.alldatasheet.com` |
| AS5047P | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| AS5048 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| AS5048A | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| AS5600 | сенсори, вивід/актуатори, проєкти, додатки | 15-ACS712-ZMPT101B-PZEM-AS5600-FSR, 11-PowerMotion-2, 04-Energy-Monitor, 02-Troubleshooting-FAQ +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| AS608 | модулі зв'язку, додатки | 05-PN532-RDM6300-Fingerprint-GM65, 20-NFC-Biometry-2, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `learn.adafruit.com`, `ww1.microchip.com` |
| AS7262 | сенсори | 32-Light-Color-2 | ✅ `ams-osram.com`, `www.nxp.com`, `www.ti.com` |
| AS7341 | сенсори | 18-Light-Spectral-Gesture | ✅ `learn.adafruit.com` |
| AS923 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| ASR6501 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| ASR6601 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| AT24C256 | сенсори | 14-DS3231-Encoder-Keypad-Joystick | ✅ `www.microchip.com` |
| AT24C32 | сенсори | 14-DS3231-Encoder-Keypad-Joystick | ✅ `www.microchip.com` |
| AT32 | модулі зв'язку | 21-Motion-Control | ✅ `docs.espressif.com` |
| ATC1441 | радіо, сенсори | 06-BLE-Gateway-Tracker, 39-Wireless-Sensors | ✅ `docs.espressif.com` |
| ATECC508A | модулі зв'язку | 25-Secure-Elements | ✅ `docs.espressif.com`, `learn.microchip.com`, `www.alldatasheet.com` |
| ATECC608 | додатки | 04-Datasheet-Links | ✅ `www.microchip.com` |
| ATECC608A | модулі зв'язку | 25-Secure-Elements | ✅ `docs.espressif.com`, `learn.microchip.com`, `www.alldatasheet.com` |
| ATECC608E | модулі зв'язку | 25-Secure-Elements | ✅ `docs.espressif.com`, `learn.microchip.com`, `www.alldatasheet.com` |
| ATGM336H | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| ATM90E32 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| ATM90E32NBLA | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| ATSP0 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| ATSP3 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| ATSP6 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| AUTH0 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| AW9523 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| AXP192 | плати | 03-LILYGO-TDisplay-TBeam, 06-M5Stack-Core-Stick | ✅ `docs.m5stack.com`, `invensense.tdk.com`, `lilygo.cc` |
| AXP2101 | плати | 03-LILYGO-TDisplay-TBeam, 12-Retro-Wearable | ✅ `lilygo.cc`, `wiki.lilygo.cc`, `www.alldatasheet.com` |
| BC25 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| BC417 | модулі зв'язку, додатки | 06-HC05-HM10-CC1101-HC12, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| BC547 | модулі зв'язку | 12-RC-Protocols | ✅ `www.alldatasheet.com` |
| BGT60 | сенсори | 29-Range-Lidar-60GHz | ✅ `www.infineon.com`, `www.seeedstudio.com`, `www.st.com` |
| BGT60TR13C | сенсори | 29-Range-Lidar-60GHz | ✅ `www.infineon.com`, `www.seeedstudio.com`, `www.st.com` |
| BH1750 | живлення, сенсори, додатки | 01-Lancjugi-zhivlennya, 01-DHT11-DHT22, 02-DS18B20, 03-BME280-BMP280-SHT31 +17 | ✅ `ams-osram.com`, `docs.espressif.com`, `learn.adafruit.com` |
| BIN1 | вивід/актуатори | 04-L298N-TB6612-A4988-Buzzer | ✅ `learn.adafruit.com` |
| BIN2 | вивід/актуатори | 04-L298N-TB6612-A4988-Buzzer | ✅ `learn.adafruit.com` |
| BL0937 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| BLM18PG121 | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| BLM18PG601 | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| BLOCK1 | чипи/модулі | 01-ESP32-Classic | ✅ `docs.espressif.com`, `www.espressif.com` |
| BM8563 | плати | 06-M5Stack-Core-Stick | ✅ `docs.m5stack.com`, `invensense.tdk.com`, `m5stack.com` |
| BMA400 | сенсори | 25-Mag-IMU-2 | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| BMA423 | плати | 12-Retro-Wearable | ✅ `lilygo.cc`, `wiki.lilygo.cc`, `www.alldatasheet.com` |
| BME280 | чипи/модулі, живлення, шини, радіо, сенсори, модулі зв'язку, живлення/рівні, плати, протоколи, проєкти, лабораторія, додатки | 09-ESP32-C2-P4, 03-Spozhivannya, 03-I2C, 02-BLE-Bluetooth +35 | ✅ `amphenol-sensors.com`, `assets.bosch-sensortec.com`, `circuitpython.org` |
| BME680 | сенсори, додатки | 08-BME680-CCS811-MHZ19-PMS5003, 17-Gas-CO2-Precision, 22-Gas-2-VOC-Industrial, 23-Dust-CO2-2 +4 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| BME688 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| BME690 | сенсори | 28-Env-NewGen | ✅ `sensirion.com`, `www.bosch-sensortec.com` |
| BMI088 | сенсори, модулі зв'язку | 31-IMU-Mag-3, 21-Motion-Control | ✅ `docs.espressif.com`, `www.analog.com`, `www.bosch-sensortec.com` |
| BMI160 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| BMI270 | сенсори | 25-Mag-IMU-2 | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| BMP280 | шини, радіо, сенсори, плати, проєкти, лабораторія, додатки | 03-I2C, 02-BLE-Bluetooth, 03-ESP-NOW, 01-DHT11-DHT22 +28 | ✅ `amphenol-sensors.com`, `ams-osram.com`, `assets.bosch-sensortec.com` |
| BMP384 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| BMP388 | сенсори, модулі зв'язку | 35-Tails, 21-Motion-Control | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `sensirion.com` |
| BMP390 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| BMP581 | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| BMP585 | сенсори | 28-Env-NewGen | ✅ `sensirion.com`, `www.bosch-sensortec.com` |
| BNO055 | сенсори, додатки | 16-HMC5883-BNO055-RFID-RC522-Barcode, 25-Mag-IMU-2, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| BNO085 | сенсори, модулі зв'язку | 19-IMU-6-9DOF, 17-GNSS-RTK | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.quectel.com` |
| BOX3 | модулі зв'язку | 21-Motion-Control | ✅ `docs.espressif.com` |
| BQ24074 | живлення/рівні, додатки | 03-TP4056-IP5306-BMS-UPS, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| BQ25504 | живлення/рівні | 01-Buck-Boost-Solar | ✅ `www.alldatasheet.com`, `www.ti.com` |
| BQ25570 | живлення/рівні | 01-Buck-Boost-Solar | ✅ `www.alldatasheet.com`, `www.ti.com` |
| BQ274 | живлення | 05-Fuel-Gauge | ✅ `www.analog.com`, `www.onsemi.com`, `www.ti.com` |
| BQ27441 | живлення | 05-Fuel-Gauge | ✅ `www.analog.com`, `www.onsemi.com`, `www.ti.com` |
| BSEC2 | сенсори | 28-Env-NewGen | ✅ `sensirion.com`, `www.bosch-sensortec.com` |
| BSS138 | старт, gpio, модулі зв'язку, живлення/рівні, додатки | 02-Glosariy, 03-Pidtyaguvannya-rivni, 15-RFID-Advanced, 02-Level-Shifters +2 | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| BT136 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| BTA16 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| BTA24 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| BTS6143D | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| BTS7960 | вивід/актуатори, проєкти, лабораторія, додатки | 07-BTS7960-L9110S-SSR-Solenoid, 11-PowerMotion-2, 03-Access-Control, 04-PCB-Design +1 | ✅ `docs.espressif.com`, `jlcpcb.com`, `learn.adafruit.com` |
| BY8301 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| CAP1188 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| CAP2 | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| CAT24C32 | сенсори | 14-DS3231-Encoder-Keypad-Joystick | ✅ `www.microchip.com` |
| CC1101 | модулі зв'язку, плати, додатки | 06-HC05-HM10-CC1101-HC12, 09-Cellular-NBIoT-UARTLoRa, 22-Automotive, 11-HMI-Boards +1 | ✅ `docs.espressif.com`, `wiki.lilygo.cc`, `ww1.microchip.com` |
| CC1310 | модулі зв'язку | 09-Cellular-NBIoT-UARTLoRa | ✅ `docs.espressif.com`, `www.semtech.com`, `www.simcom.com` |
| CC2541 | модулі зв'язку, додатки | 06-HC05-HM10-CC1101-HC12, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| CC41 | модулі зв'язку | 06-HC05-HM10-CC1101-HC12 | ✅ `www.alldatasheet.com` |
| CCS811 | сенсори, додатки | 08-BME680-CCS811-MHZ19-PMS5003, 17-Gas-CO2-Precision, 22-Gas-2-VOC-Industrial, 23-Dust-CO2-2 +3 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| CD74HC4067 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| CGDK2 | радіо | 06-BLE-Gateway-Tracker | ✅ `docs.espressif.com` |
| CGG1 | радіо | 06-BLE-Gateway-Tracker | ✅ `docs.espressif.com` |
| CH341SER | живлення/рівні, плати | 05-USB-UART-AutoReset, 01-DOIT-DevKitV1-NodeMCU32S, 02-Wemos-D1-R32 | ✅ `docs.espressif.com`, `www.espressif.com`, `www.wch-ic.com` |
| CIC310 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| CLRC663 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| CM1106 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| CN3065 | живлення/рівні | 01-Buck-Boost-Solar | ✅ `www.alldatasheet.com`, `www.ti.com` |
| CN3791 | старт, живлення/рівні, додатки | 02-Glosariy, 01-Buck-Boost-Solar, 03-TP4056-IP5306-BMS-UPS, 04-Datasheet-Links +1 | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| CN470 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| CP2102 | старт, gpio, шини, таймери, прошивка, модулі зв'язку, живлення/рівні, плати, лабораторія, додатки | 02-Glosariy, 03-Porivnyannya-chipiv, 04-Devkit-plati, 02-Strapping-pini +17 | ✅ `circuitpython.org`, `docs.espressif.com`, `docs.heltec.org` |
| CP2102N | старт, прошивка, плати | 04-Devkit-plati, 05-JTAG-Debug, 08-S3-DevKitC-C3-SuperMini-XIAO, 13-ESP32C6-Boards | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| CP2104 | живлення/рівні, плати, лабораторія, додатки | 05-USB-UART-AutoReset, 03-LILYGO-TDisplay-TBeam, 06-M5Stack-Core-Stick, 07-Feather-Huzzah32-Thing +2 | ✅ `docs.espressif.com`, `docs.m5stack.com`, `invensense.tdk.com` |
| CR1220 | сенсори, модулі зв'язку, проєкти | 27-Time-Mem-IO-DAC, 17-GNSS-RTK, 02-GPS-Tracker | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.quectel.com` |
| CR2032 | живлення, радіо, сенсори | 05-Fuel-Gauge, 06-BLE-Gateway-Tracker, 07-BLE5-LongRange-Audio, 14-DS3231-Encoder-Keypad-Joystick +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.analog.com` |
| CR2450 | чипи/модулі, радіо, сенсори | 11-ESP32-C6-H2-Mesh, 06-BLE-Gateway-Tracker, 39-Wireless-Sensors | ✅ `docs.espressif.com` |
| CSE7766 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| CST816 | вивід/актуатори, плати | 17-Touchscreens, 11-HMI-Boards, 12-Retro-Wearable | ✅ `lilygo.cc`, `wiki.lilygo.cc`, `www.alldatasheet.com` |
| CST816S | вивід/актуатори | 17-Touchscreens | ✅ `www.alldatasheet.com`, `www.ti.com` |
| CTRL0 | сенсори | 25-Mag-IMU-2 | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| CTRL4 | сенсори | 25-Mag-IMU-2 | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| CY7C68013A | лабораторія | 01-Instruments | ✅ `docs.espressif.com`, `sigrok.org` |
| DATA1 | плати | 05-ESP32-CAM | ✅ `circuitpython.org` |
| DCF77 | модулі зв'язку | 23-Marine-Time | ✅ `docs.espressif.com`, `www.u-blox.com` |
| DE2120 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| DEPG0213BN | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| DEVKITV1 | старт, плати | 04-Devkit-plati, 01-DOIT-DevKitV1-NodeMCU32S | ✅ `docs.espressif.com`, `www.espressif.com` |
| DFN8 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| DHT11 | сенсори, додатки | 01-DHT11-DHT22, 02-DS18B20, 03-BME280-BMP280-SHT31, 06-INA219-HX711-BH1750 +4 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| DHT12 | сенсори | 07-AHT10-AHT20-SHT40 | ✅ `learn.adafruit.com`, `sensirion.com` |
| DHT20 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| DHT22 | сенсори, протоколи, додатки | 01-DHT11-DHT22, 02-DS18B20, 03-BME280-BMP280-SHT31, 06-INA219-HX711-BH1750 +5 | ✅ `docs.aws.amazon.com`, `docs.espressif.com`, `learn.adafruit.com` |
| DIAG0 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| DIAG1 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| DIS08070H | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| DM542 | вивід/актуатори, модулі зв'язку | 11-PowerMotion-2, 21-Motion-Control | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| DM9051 | модулі зв'язку, додатки | 19-Wired-2, 07-Versions | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| DMX512 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| DP83848 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| DP83848C | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| DP83TC811 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| DP83TC811S | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| DPS310 | сенсори | 17-Gas-CO2-Precision, 35-Tails | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| DPS368 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| DRV2605 | плати | 12-Retro-Wearable | ✅ `lilygo.cc`, `wiki.lilygo.cc`, `www.alldatasheet.com` |
| DRV8313 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| DRV8825 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| DRV8833 | проєкти | 06-C5-C61-Robotics | ✅ `assets.bosch-sensortec.com`, `www.espressif.com`, `www.st.com` |
| DS1307 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| DS13317 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| DS1804 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| DS1822 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| DS18B20 | старт, сенсори, модулі зв'язку, протоколи, проєкти, лабораторія, додатки | 02-Glosariy, 01-DHT11-DHT22, 02-DS18B20, 03-BME280-BMP280-SHT31 +12 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| DS2408 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| DS2413 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| DS2450 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| DS2482 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| DS2482A | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| DS2484 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| DS3218 | вивід/актуатори | 06-PCA9685-MG996R-28BYJ48-TMC2209 | ✅ `www.alldatasheet.com` |
| DS3231 | таймери, сенсори, додатки | 01-Timeri-MCPWM-PCNT-RMT, 03-Sleep-ULP, 14-DS3231-Encoder-Keypad-Joystick, 27-Time-Mem-IO-DAC +2 | ✅ `docs.espressif.com`, `docs.micropython.org`, `learn.adafruit.com` |
| DS3231M | сенсори | 14-DS3231-Encoder-Keypad-Joystick | ✅ `www.microchip.com` |
| DS3231MZ | сенсори | 14-DS3231-Encoder-Keypad-Joystick | ✅ `www.microchip.com` |
| DS3502 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| DS80064 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| DS8500 | сенсори | 38-Industrial-Sensors | ✅ `www.analog.com`, `www.ti.com` |
| DSM501 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| DSM501A | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| DUT1 | модулі зв'язку | 23-Marine-Time | ✅ `docs.espressif.com`, `www.u-blox.com` |
| DW01 | старт, живлення, живлення/рівні, плати, проєкти, лабораторія, додатки | 02-Glosariy, 04-Akumulyatori-TP4056, 01-Buck-Boost-Solar, 03-TP4056-IP5306-BMS-UPS +7 | ✅ `docs.arduino.cc`, `docs.espressif.com`, `jlcpcb.com` |
| DW1000 | модулі зв'язку | 08-LD2410-UWB-IR-Voice, 28-UWB-2 | ✅ `www.alldatasheet.com`, `www.qorvo.com` |
| DW3000 | модулі зв'язку | 28-UWB-2 | ✅ `www.qorvo.com` |
| DWM1000 | модулі зв'язку, додатки | 08-LD2410-UWB-IR-Voice, 28-UWB-2, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| DWM3000 | модулі зв'язку | 28-UWB-2 | ✅ `www.qorvo.com` |
| DWM3000EVB | модулі зв'язку | 28-UWB-2 | ✅ `www.qorvo.com` |
| EA60 | лабораторія | 03-Enclosure-Cert-Factory | ✅ `docs.espressif.com` |
| EAL3 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| EAL5 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| EC200U | модулі зв'язку, додатки | 03-SIM800L-GPS, 17-GNSS-RTK, 18-Cellular-LoRa-2, 26-SIM-Power +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| EC25 | сенсори | 13-RCWL0516-Reed-Vibration-Tilt-Flow | ✅ `www.alldatasheet.com` |
| ECON1 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| EEC1 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| EEC2 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| EGM2008 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| EK73002 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| EK73002ACGB | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| EK79655 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| EK9716 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| EK9716BD3 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| EL817 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| ELM327 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| EM18 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| EM4100 | модулі зв'язку | 05-PN532-RDM6300-Fingerprint-GM65, 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| EM4305 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| EN50543 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| ENC28J60 | модулі зв'язку | 07-SIM7600-W5500-MCP2515, 19-Wired-2, 20-NFC-Biometry-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| ENS160 | сенсори | 22-Gas-2-VOC-Industrial | ✅ `learn.adafruit.com`, `sensirion.com` |
| ENS161 | сенсори | 28-Env-NewGen | ✅ `sensirion.com`, `www.bosch-sensortec.com` |
| ENS210 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| ENS210A | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| ENS211 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| ENS212A | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| ENS215 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| ES1J | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| ES7210 | шини, вивід/актуатори, плати | 04-I2S, 13-Audio-Codecs, 12-Retro-Wearable | ✅ `docs.espressif.com`, `docs.micropython.org`, `lilygo.cc` |
| ES8311 | вивід/актуатори | 13-Audio-Codecs | ✅ `docs.espressif.com` |
| ES8388 | шини, радіо, вивід/актуатори | 04-I2S, 05-BLE-Mesh-A2DP-HID, 13-Audio-Codecs | ✅ `docs.espressif.com`, `docs.micropython.org` |
| ESD5Z3V3 | живлення | 01-Lancjugi-zhivlennya | ✅ `docs.espressif.com`, `www.espressif.com` |
| ESP32 | старт, чипи/модулі, живлення, gpio, шини, радіо, аналог, таймери, пам'ять, прошивка, сенсори, вивід/актуатори, модулі зв'язку, живлення/рівні, плати, протоколи, проєкти, лабораторія, додатки | 01-Yak-koristuvatis-dovidnikom, 02-Glosariy, 03-Porivnyannya-chipiv, 04-Devkit-plati +208 | ✅ `amphenol-sensors.com`, `ams-osram.com`, `assets.bosch-sensortec.com` |
| ESP32C3 | плати | 08-S3-DevKitC-C3-SuperMini-XIAO | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| ESP32C5 | плати | 17-C5-DevKit | ✅ `docs.espressif.com` |
| ESP32C6 | чипи/модулі, плати, протоколи, додатки | 11-ESP32-C6-H2-Mesh, 12-ESP32-P4-Native, 13-ESP32C6-Boards, 14-ESP32H2-Boards +4 | ✅ `docs.espressif.com`, `wiki.seeedstudio.com`, `www.espressif.com` |
| ESP32H2 | чипи/модулі, плати, додатки | 11-ESP32-C6-H2-Mesh, 14-ESP32H2-Boards, 01-Pinout-tablici | ✅ `docs.espressif.com` |
| ESP32S3 | плати | 08-S3-DevKitC-C3-SuperMini-XIAO, 11-HMI-Boards, 12-Retro-Wearable | ✅ `docs.espressif.com`, `lilygo.cc`, `wiki.lilygo.cc` |
| ESP8266 | старт, вивід/актуатори, протоколи | 03-Porivnyannya-chipiv, 19-WebRadio-Streaming, 03-mDNS-NTP-TLS, 07-Notify-Voice | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.espressif.com` |
| ESP8684 | старт, чипи/модулі | 03-Porivnyannya-chipiv, 06-Flash-PSRAM, 09-ESP32-C2-P4, 10-ESP32-C5-C61 | ✅ `docs.espressif.com`, `www.espressif.com` |
| ESP8684H2 | чипи/модулі | 06-Flash-PSRAM, 09-ESP32-C2-P4 | ✅ `docs.espressif.com`, `www.espressif.com` |
| ESP8685 | чипи/модулі | 09-ESP32-C2-P4 | ✅ `docs.espressif.com`, `www.espressif.com` |
| ESP8685H2 | чипи/модулі | 09-ESP32-C2-P4 | ✅ `docs.espressif.com`, `www.espressif.com` |
| ETC1 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| ETH01 | старт, модулі зв'язку, плати | 04-Devkit-plati, 04-RS485-CAN-Ethernet-Kamera, 09-WT32-ETH01-Olimex | ✅ `www.microchip.com`, `www.olimex.com`, `www.ti.com` |
| EU868 | модулі зв'язку | 18-Cellular-LoRa-2, 27-LPWAN-Alt, 29-LoRaWAN-Gateway | ✅ `docs.espressif.com`, `lora-alliance.org`, `www.chirpstack.io` |
| EXT0 | gpio, таймери, модулі зв'язку, лабораторія | 05-RTC-GPIO, 03-Sleep-ULP, 20-NFC-Biometry-2, 05-Breadboard-Mezhi | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.nordicsemi.com` |
| EXT1 | gpio, таймери | 05-RTC-GPIO, 03-Sleep-ULP | ✅ `docs.espressif.com`, `www.nordicsemi.com`, `www.ti.com` |
| FAN7388 | таймери | 01-Timeri-MCPWM-PCNT-RMT | ✅ `docs.espressif.com` |
| FAT16 | вивід/актуатори | 08-DFPlayer-MAX98357-Nextion-LCD2004, 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| FAT32 | шини, вивід/актуатори, модулі зв'язку, плати | 06-USB-OTG-JTAG, 07-SD-SDIO, 08-DFPlayer-MAX98357-Nextion-LCD2004, 18-MP3-TTS-Amps +5 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| FC01 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| FC03 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| FC05 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| FC06 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| FC0F | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| FC10 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| FM24C64 | сенсори | 14-DS3231-Encoder-Keypad-Joystick | ✅ `www.microchip.com` |
| FPC1020 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| FS8205 | старт, живлення/рівні | 02-Glosariy, 01-Buck-Boost-Solar, 03-TP4056-IP5306-BMS-UPS | ✅ `www.alldatasheet.com`, `www.ti.com` |
| FS8205A | живлення/рівні, лабораторія, додатки | 01-Buck-Boost-Solar, 03-TP4056-IP5306-BMS-UPS, 04-PCB-Design, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `jlcpcb.com`, `ww1.microchip.com` |
| FSCTRL0 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| FSCTRL1 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| FT2232 | шини, прошивка | 06-USB-OTG-JTAG, 05-JTAG-Debug | ✅ `docs.espressif.com` |
| FT2232H | прошивка | 05-JTAG-Debug | ✅ `docs.espressif.com` |
| FT231X | плати | 07-Feather-Huzzah32-Thing | ✅ `learn.adafruit.com` |
| FT232RL | живлення/рівні, плати, додатки | 05-USB-UART-AutoReset, 05-ESP32-CAM, 06-Official-Sources-Modules | ✅ `circuitpython.org`, `docs.espressif.com`, `ww1.microchip.com` |
| FT4232H | прошивка, живлення/рівні | 05-JTAG-Debug, 05-USB-UART-AutoReset | ✅ `docs.espressif.com`, `www.wch-ic.com`, `www.wch.cn` |
| FT6206 | вивід/актуатори | 17-Touchscreens | ✅ `www.alldatasheet.com`, `www.ti.com` |
| FT6236 | вивід/актуатори | 17-Touchscreens | ✅ `www.alldatasheet.com`, `www.ti.com` |
| FT6336 | плати | 06-M5Stack-Core-Stick, 12-Retro-Wearable | ✅ `docs.m5stack.com`, `invensense.tdk.com`, `lilygo.cc` |
| FT6336U | вивід/актуатори, плати | 17-Touchscreens, 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.alldatasheet.com`, `www.espressif.com` |
| FUSB302 | живлення/рівні, лабораторія | 09-USB-PD, 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| GB2312 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| GC0308 | модулі зв'язку | 11-TinyML-Voice | ✅ `www.alldatasheet.com` |
| GC0328 | модулі зв'язку | 13-Camera-Streaming | ✅ `www.ovt.com` |
| GC9A01 | вивід/актуатори | 14-Displays-3 | ✅ `www.alldatasheet.com` |
| GC9A01A | вивід/актуатори | 14-Displays-3 | ✅ `www.alldatasheet.com` |
| GD25Q32 | чипи/модулі | 06-Flash-PSRAM | ✅ `docs.espressif.com`, `www.espressif.com` |
| GD25Q64 | чипи/модулі | 06-Flash-PSRAM | ✅ `docs.espressif.com`, `www.espressif.com` |
| GDE0213B1 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEH0213B72 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEH0213B73 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEM0213B74 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEM029T94 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW0154T8 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW0154Z04 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW0213M21 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW0213T5D | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW0213Z19 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW042T2 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW042Z15 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW075T7 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEW075T8 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEY0154D67 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEY0213B74 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEY029T94 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GDEY075T7 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| GM328 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| GM65 | сенсори, модулі зв'язку, проєкти, додатки | 16-HMC5883-BNO055-RFID-RC522-Barcode, 05-PN532-RDM6300-Fingerprint-GM65, 15-RFID-Advanced, 19-Wired-2 +3 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| GND1 | модулі зв'язку | 19-Wired-2, 23-Marine-Time | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| GND2 | модулі зв'язку | 19-Wired-2, 23-Marine-Time | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| GP2Y | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| GP2Y1010 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| GP2Y1010AU0F | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| GPA0 | сенсори | 09-ADS1115-MCP3008-PCF8574-MCP23017 | ✅ `www.ti.com` |
| GPB0 | сенсори | 09-ADS1115-MCP3008-PCF8574-MCP23017 | ✅ `www.ti.com` |
| GPS6MV2 | модулі зв'язку | 03-SIM800L-GPS | ✅ `www.simcom.com`, `www.u-blox.com` |
| GT911 | вивід/актуатори, плати | 17-Touchscreens, 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.alldatasheet.com`, `www.espressif.com` |
| HB100 | модулі зв'язку | 08-LD2410-UWB-IR-Voice | ✅ `www.alldatasheet.com` |
| HC05 | модулі зв'язку, плати, додатки | 09-Cellular-NBIoT-UARTLoRa, 11-HMI-Boards, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `wiki.lilygo.cc`, `ww1.microchip.com` |
| HC12 | модулі зв'язку, плати, додатки | 09-Cellular-NBIoT-UARTLoRa, 11-HMI-Boards, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `wiki.lilygo.cc`, `ww1.microchip.com` |
| HCS301 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| HCS341 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| HD44780 | вивід/актуатори, додатки | 16-LCD-Char, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| HDC1080 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| HLW8012 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| HLW8032 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| HM10 | модулі зв'язку, плати, додатки | 09-Cellular-NBIoT-UARTLoRa, 11-HMI-Boards, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `wiki.lilygo.cc`, `ww1.microchip.com` |
| HMC5883 | сенсори | 25-Mag-IMU-2 | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| HMC5883L | сенсори, додатки | 04-MPU6050, 16-HMC5883-BNO055-RFID-RC522-Barcode, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| HPMA115 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| HPMA115S | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| HT1621 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| HT16K33 | вивід/актуатори | 10-Displays-2 | ✅ `learn.adafruit.com` |
| HT7333 | живлення, таймери, живлення/рівні | 02-LDO-DC-DC, 03-Sleep-ULP, 04-LDO-Buck-XL4015-Protect | ✅ `www.microchip.com`, `www.nordicsemi.com`, `www.ti.com` |
| HTU21D | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| HUZZAH32 | старт, плати | 04-Devkit-plati, 07-Feather-Huzzah32-Thing | ✅ `learn.adafruit.com` |
| HX710 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| HX711 | живлення, сенсори, додатки | 01-Lancjugi-zhivlennya, 01-DHT11-DHT22, 02-DS18B20, 03-BME280-BMP280-SHT31 +16 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| HX8357 | вивід/актуатори | 10-Displays-2 | ✅ `learn.adafruit.com` |
| ICL7660 | вивід/актуатори | 16-LCD-Char | ✅ `learn.adafruit.com` |
| ICM20948 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| ICM42688 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| IDF5 | додатки | 07-Versions | ✅ `docs.espressif.com` |
| IDLE0 | таймери, прошивка | 02-WDT, 06-FreeRTOS-Patterns | ✅ `docs.espressif.com`, `www.alldatasheet.com`, `www.freertos.org` |
| IDLE1 | таймери, прошивка | 02-WDT, 06-FreeRTOS-Patterns | ✅ `docs.espressif.com`, `www.alldatasheet.com`, `www.freertos.org` |
| IL0373 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| IL0398 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| IL3895 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| IL3897 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| ILI9340 | вивід/актуатори, плати | 14-Displays-3, 12-Retro-Wearable | ✅ `lilygo.cc`, `wiki.lilygo.cc`, `www.alldatasheet.com` |
| ILI9341 | вивід/актуатори, плати, додатки | 02-TFT-LCD-Epaper, 12-LVGL-SquareLine, 14-Displays-3, 17-Touchscreens +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| ILI9342C | плати | 06-M5Stack-Core-Stick | ✅ `docs.m5stack.com`, `invensense.tdk.com`, `m5stack.com` |
| IM69D130 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| IMX636 | чипи/модулі | 12-ESP32-P4-Native | ✅ `docs.espressif.com`, `www.espressif.com` |
| INA219 | живлення, сенсори, вивід/актуатори, додатки | 01-Lancjugi-zhivlennya, 03-Spozhivannya, 04-Akumulyatori-TP4056, 01-DHT11-DHT22 +20 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| INA226 | живлення, сенсори | 03-Spozhivannya, 21-Energy-Meters | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| INA3221 | сенсори | 06-INA219-HX711-BH1750 | ✅ `learn.adafruit.com`, `www.ti.com` |
| INMP441 | старт, шини, вивід/актуатори, модулі зв'язку, протоколи, проєкти | 02-Glosariy, 04-I2S, 13-Audio-Codecs, 11-TinyML-Voice +4 | ✅ `docs.espressif.com`, `docs.micropython.org`, `wiki.seeedstudio.com` |
| IO38 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| IO47 | плати | 10-Mini-Boards | ✅ `docs.arduino.cc`, `learn.adafruit.com`, `www.diodes.com` |
| IP20 | сенсори, лабораторія | 21-Energy-Meters, 03-Enclosure-Cert-Factory | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| IP44 | лабораторія | 03-Enclosure-Cert-Factory | ✅ `docs.espressif.com` |
| IP5306 | старт, живлення, живлення/рівні, плати, проєкти, додатки | 02-Glosariy, 04-Akumulyatori-TP4056, 03-TP4056-IP5306-BMS-UPS, 04-LDO-Buck-XL4015-Protect +7 | ✅ `docs.arduino.cc`, `docs.espressif.com`, `docs.m5stack.com` |
| IP5328P | живлення/рівні | 03-TP4056-IP5306-BMS-UPS | ✅ `www.ti.com` |
| IP54 | модулі зв'язку, проєкти, лабораторія | 10-Industrial, 02-GPS-Tracker, 03-Enclosure-Cert-Factory | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.simcom.com` |
| IP65 | модулі зв'язку, живлення/рівні, проєкти, лабораторія | 20-NFC-Biometry-2, 26-SIM-Power, 29-LoRaWAN-Gateway-Deep, 29-LoRaWAN-Gateway +4 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `lora-alliance.org` |
| IP66 | лабораторія | 03-Enclosure-Cert-Factory | ✅ `docs.espressif.com` |
| IP67 | сенсори, модулі зв'язку, лабораторія | 26-Light-UV-IRArray-ToF, 35-Tails, 23-Marine-Time, 03-Enclosure-Cert-Factory | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| IP68 | сенсори, плати | 24-Pressure-Level-Flow, 12-Retro-Wearable | ✅ `learn.adafruit.com`, `lilygo.cc`, `sensirion.com` |
| IR2104 | таймери | 01-Timeri-MCPWM-PCNT-RMT | ✅ `docs.espressif.com` |
| IR2110 | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| IRF540 | аналог, вивід/актуатори | 03-PID-Filters, 03-NeoPixel-Servo-Rele-MOSFET | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| IRFZ44N | таймери, вивід/актуатори, живлення/рівні | 01-Timeri-MCPWM-PCNT-RMT, 03-NeoPixel-Servo-Rele-MOSFET, 04-LDO-Buck-XL4015-Protect | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| IRL540 | вивід/актуатори | 03-NeoPixel-Servo-Rele-MOSFET | ✅ `learn.adafruit.com` |
| IRLZ44N | аналог, вивід/актуатори | 03-PID-Filters, 03-NeoPixel-Servo-Rele-MOSFET, 07-BTS7960-L9110S-SSR-Solenoid | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.alldatasheet.com` |
| IRS2110 | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| IRS2110S | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| IS31FL3731 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| ISD9160 | модулі зв'язку | 16-Offline-Voice | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| ISM330 | сенсори | 19-IMU-6-9DOF | ✅ `learn.adafruit.com` |
| ISO1042 | модулі зв'язку | 19-Wired-2, 23-Marine-Time | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| ISO1050 | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera, 19-Wired-2, 22-Automotive, 23-Marine-Time | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.nxp.com` |
| ISO11784 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ISO11898 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| ISO124 | модулі зв'язку | 10-Industrial, 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| ISO13239 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ISO1410 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| ISO14443 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ISO14443A | модулі зв'язку | 01-RC522-RFID, 05-PN532-RDM6300-Fingerprint-GM65, 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ISO1452 | шини | 01-UART | ✅ `www.alldatasheet.com`, `www.ti.com` |
| ISO15693 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ISO18000 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ISO7741 | сенсори, лабораторія | 38-Industrial-Sensors, 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| ISO7816 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| JC3248W535 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| JC8048W550 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| JQ6500 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| JTYJGD03MJ | радіо | 06-BLE-Gateway-Tracker | ✅ `docs.espressif.com` |
| KCD1 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| KCD3 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| KS0066 | вивід/актуатори | 16-LCD-Char | ✅ `learn.adafruit.com` |
| KSZ8081 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| KSZ8081MNX | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| KSZ8081RNA | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| KSZ80XX | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| KSZ8851 | додатки | 07-Versions | ✅ `docs.espressif.com` |
| KT403A | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| KW11 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| KWP2000 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| LAN8710A | плати | 09-WT32-ETH01-Olimex | ✅ `www.microchip.com`, `www.olimex.com` |
| LAN8720 | модулі зв'язку, плати, додатки | 04-RS485-CAN-Ethernet-Kamera, 19-Wired-2, 09-WT32-ETH01-Olimex, 04-Datasheet-Links +1 | ✅ `docs.espressif.com`, `docs.kernel.org`, `ww1.microchip.com` |
| LAN8720A | плати, додатки | 09-WT32-ETH01-Olimex, 04-Datasheet-Links | ✅ `www.microchip.com`, `www.olimex.com` |
| LAN9252 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| LC29H | модулі зв'язку | 17-GNSS-RTK, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| LC709203 | живлення | 05-Fuel-Gauge | ✅ `www.analog.com`, `www.onsemi.com`, `www.ti.com` |
| LC709203F | живлення | 05-Fuel-Gauge | ✅ `www.analog.com`, `www.onsemi.com`, `www.ti.com` |
| LCD1602 | сенсори, вивід/актуатори, додатки | 09-ADS1115-MCP3008-PCF8574-MCP23017, 02-TFT-LCD-Epaper, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| LCD2004 | старт, радіо, вивід/актуатори, модулі зв'язку, додатки | 02-Glosariy, 05-BLE-Mesh-A2DP-HID, 08-DFPlayer-MAX98357-Nextion-LCD2004, 10-Displays-2 +5 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| LD19 | сенсори | 29-Range-Lidar-60GHz | ✅ `www.infineon.com`, `www.seeedstudio.com`, `www.st.com` |
| LD2410 | сенсори, модулі зв'язку, додатки | 26-Light-UV-IRArray-ToF, 29-Range-Lidar-60GHz, 35-Tails, 08-LD2410-UWB-IR-Voice +4 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| LD2410B | модулі зв'язку | 08-LD2410-UWB-IR-Voice | ✅ `www.alldatasheet.com` |
| LD2410C | модулі зв'язку | 08-LD2410-UWB-IR-Voice | ✅ `www.alldatasheet.com` |
| LD2420 | сенсори, модулі зв'язку | 26-Light-UV-IRArray-ToF, 08-LD2410-UWB-IR-Voice | ✅ `learn.adafruit.com`, `www.alldatasheet.com` |
| LD2450 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| LD3320 | модулі зв'язку, протоколи | 16-Offline-Voice, 10-Voice-Assistant | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| LDO1 | плати | 10-Mini-Boards | ✅ `docs.arduino.cc`, `learn.adafruit.com`, `www.diodes.com` |
| LDO2 | плати | 10-Mini-Boards | ✅ `docs.arduino.cc`, `learn.adafruit.com`, `www.diodes.com` |
| LIR2032 | сенсори | 14-DS3231-Encoder-Keypad-Joystick | ✅ `www.microchip.com` |
| LIS2MDL | сенсори | 19-IMU-6-9DOF | ✅ `learn.adafruit.com` |
| LIS3DH | сенсори, проєкти | 25-Mag-IMU-2, 02-GPS-Tracker | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com`, `www.simcom.com` |
| LJ12A3 | модулі зв'язку | 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| LJC18 | модулі зв'язку | 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| LJC18A3 | модулі зв'язку | 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| LLCC68 | модулі зв'язку | 09-Cellular-NBIoT-UARTLoRa, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| LM2596 | живлення, модулі зв'язку, живлення/рівні, проєкти, додатки | 02-LDO-DC-DC, 03-SIM800L-GPS, 26-SIM-Power, 01-Buck-Boost-Solar +5 | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| LM2596HV | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| LM35 | аналог, сенсори, додатки | 03-PID-Filters, 09-ADS1115-MCP3008-PCF8574-MCP23017, 11-NTC-PT100-MAX6675-LM35, 27-Time-Mem-IO-DAC +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| LM358 | модулі зв'язку | 08-LD2410-UWB-IR-Voice, 10-Industrial | ✅ `learn.adafruit.com`, `www.alldatasheet.com`, `www.ti.com` |
| LM386 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| LM393 | сенсори | 12-MQ2-MQ7-MQ135-Flame-Sound, 13-RCWL0516-Reed-Vibration-Tilt-Flow | ✅ `www.alldatasheet.com`, `www.ti.com` |
| LM4871 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| LMP91000 | сенсори | 22-Gas-2-VOC-Industrial | ✅ `learn.adafruit.com`, `sensirion.com` |
| LMR240 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| LOCK0 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| LOCK1 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| LOUT1 | вивід/актуатори | 13-Audio-Codecs | ✅ `docs.espressif.com` |
| LPS22 | сенсори, модулі зв'язку | 17-Gas-CO2-Precision, 21-Motion-Control | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| LPS22HB | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| LPS28 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| LPS28DFW | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| LR1121 | модулі зв'язку | 17-GNSS-RTK, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| LT3652 | живлення/рівні | 01-Buck-Boost-Solar | ✅ `www.alldatasheet.com`, `www.ti.com` |
| LYWSD03MMC | радіо, сенсори | 06-BLE-Gateway-Tracker, 39-Wireless-Sensors | ✅ `docs.espressif.com` |
| MA730 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| MAX14827A | сенсори | 38-Industrial-Sensors | ✅ `www.analog.com`, `www.ti.com` |
| MAX14850 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| MAX17048 | живлення | 05-Fuel-Gauge | ✅ `www.analog.com`, `www.onsemi.com`, `www.ti.com` |
| MAX232 | шини, модулі зв'язку | 01-UART, 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.alldatasheet.com` |
| MAX30003 | сенсори | 37-Bio-2 | ✅ `www.analog.com`, `www.ti.com` |
| MAX30102 | сенсори | 20-Bio-IR-Temp, 37-Bio-2 | ✅ `learn.adafruit.com`, `sensirion.com`, `www.analog.com` |
| MAX30105 | сенсори | 20-Bio-IR-Temp | ✅ `learn.adafruit.com`, `sensirion.com` |
| MAX30208 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| MAX31855 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| MAX31856 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| MAX31865 | сенсори, додатки | 11-NTC-PT100-MAX6675-LM35, 30-Temp-Precision, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MAX3232 | шини, модулі зв'язку | 01-UART, 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.alldatasheet.com` |
| MAX32500 | модулі зв'язку | 25-Secure-Elements | ✅ `docs.espressif.com`, `learn.microchip.com`, `www.alldatasheet.com` |
| MAX3485 | сенсори, модулі зв'язку, додатки | 21-Energy-Meters, 04-RS485-CAN-Ethernet-Kamera, 10-Industrial, 15-RFID-Advanced +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `ww1.microchip.com` |
| MAX44009 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| MAX4466 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| MAX485 | шини, сенсори, модулі зв'язку, додатки | 01-UART, 05-CAN-TWAI-RS485, 36-Agro, 04-RS485-CAN-Ethernet-Kamera +5 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| MAX6369 | таймери | 02-WDT | ✅ `www.alldatasheet.com` |
| MAX6675 | аналог, сенсори, додатки | 03-PID-Filters, 09-ADS1115-MCP3008-PCF8574-MCP23017, 11-NTC-PT100-MAX6675-LM35, 30-Temp-Precision +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MAX7219 | шини, вивід/актуатори, додатки | 02-SPI, 05-MAX7219-TM1637-74HC595, 09-LED-Strip-Power-SK6812-APA102, 10-Displays-2 +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MAX9814 | вивід/актуатори, модулі зв'язку | 18-MP3-TTS-Amps, 11-TinyML-Voice, 16-Offline-Voice | ✅ `docs.espressif.com`, `learn.adafruit.com`, `wiki.seeedstudio.com` |
| MAX98357 | старт, шини, радіо, вивід/актуатори, модулі зв'язку, додатки | 02-Glosariy, 04-I2S, 05-BLE-Mesh-A2DP-HID, 08-DFPlayer-MAX98357-Nextion-LCD2004 +6 | ✅ `docs.espressif.com`, `docs.micropython.org`, `learn.adafruit.com` |
| MAX98357A | старт, шини, радіо, аналог, вивід/актуатори, плати, протоколи, додатки | 02-Glosariy, 04-I2S, 05-BLE-Mesh-A2DP-HID, 02-DAC-Touch-Hall +7 | ✅ `docs.espressif.com`, `docs.micropython.org`, `learn.adafruit.com` |
| MB85RC | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| MB85RC256 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| MCP1700 | живлення | 02-LDO-DC-DC | ✅ `www.microchip.com`, `www.ti.com` |
| MCP23017 | аналог, сенсори, додатки | 01-ADC, 09-ADS1115-MCP3008-PCF8574-MCP23017, 11-NTC-PT100-MAX6675-LM35, 02-Troubleshooting-FAQ +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MCP2515 | шини, радіо, модулі зв'язку, плати, проєкти, додатки | 05-CAN-TWAI-RS485, 06-USB-OTG-JTAG, 01-WiFi-STA-AP, 03-SIM800L-GPS +14 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| MCP2518FD | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| MCP3008 | шини, аналог, сенсори, додатки | 02-SPI, 01-ADC, 09-ADS1115-MCP3008-PCF8574-MCP23017, 11-NTC-PT100-MAX6675-LM35 +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MCP3421 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| MCP41010 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| MCP41100 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| MCP4131 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| MCP4725 | аналог, сенсори, модулі зв'язку | 02-DAC-Touch-Hall, 27-Time-Mem-IO-DAC, 10-Industrial | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| MCP73831 | плати, лабораторія | 07-Feather-Huzzah32-Thing, 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `learn.adafruit.com` |
| MCP9600 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| MCP9808 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| MD13S | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| ME6211 | старт, чипи/модулі, живлення, модулі зв'язку, живлення/рівні, плати, проєкти | 02-Glosariy, 05-Moduli-WROOM-WROVER-MINI, 02-LDO-DC-DC, 03-Spozhivannya +4 | ✅ `assets.bosch-sensortec.com`, `docs.espressif.com`, `wiki.seeedstudio.com` |
| ME6211C33 | живлення, живлення/рівні | 02-LDO-DC-DC, 04-LDO-Buck-XL4015-Protect | ✅ `www.microchip.com`, `www.ti.com` |
| MFF2 | модулі зв'язку | 26-SIM-Power | ✅ `docs.espressif.com`, `www.quectel.com`, `www.simcom.com` |
| MFRC522 | сенсори, модулі зв'язку, проєкти, додатки | 16-HMC5883-BNO055-RFID-RC522-Barcode, 01-RC522-RFID, 05-PN532-RDM6300-Fingerprint-GM65, 15-RFID-Advanced +5 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MFRC52202HN1 | модулі зв'язку, додатки | 01-RC522-RFID, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| MFRC663 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| MG996R | старт, вивід/актуатори, модулі зв'язку, додатки | 02-Glosariy, 06-PCA9685-MG996R-28BYJ48-TMC2209, 07-BTS7960-L9110S-SSR-Solenoid, 11-PowerMotion-2 +4 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MHZ19 | сенсори | 17-Gas-CO2-Precision, 22-Gas-2-VOC-Industrial, 23-Dust-CO2-2, 24-Pressure-Level-Flow +1 | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| MJWSD05MMC | радіо | 06-BLE-Gateway-Tracker | ✅ `docs.espressif.com` |
| ML302 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| ML8511 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| MLX90393 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| MLX90614 | сенсори | 20-Bio-IR-Temp, 40-Thermal-MLX90640 | ✅ `learn.adafruit.com`, `sensirion.com`, `www.melexis.com` |
| MLX90640 | сенсори, проєкти | 26-Light-UV-IRArray-ToF, 40-Thermal-MLX90640, 07-Edge-AI-Vision | ✅ `learn.adafruit.com`, `www.melexis.com` |
| MMC5603 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| MMC5603NJ | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| MMC5983MA | сенсори | 25-Mag-IMU-2 | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| MOC3021 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| MOC3041 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| MP1584 | живлення, модулі зв'язку, живлення/рівні, лабораторія, додатки | 02-LDO-DC-DC, 03-SIM800L-GPS, 26-SIM-Power, 01-Buck-Boost-Solar +4 | ✅ `docs.espressif.com`, `jlcpcb.com`, `ww1.microchip.com` |
| MP1584EN | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| MP2307 | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| MPL3115A2 | сенсори | 32-Light-Color-2 | ✅ `ams-osram.com`, `www.nxp.com`, `www.ti.com` |
| MPR121 | сенсори | 33-Input-IO-2, 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.alldatasheet.com` |
| MPU6050 | аналог, сенсори, проєкти, додатки | 03-PID-Filters, 04-MPU6050, 07-AHT10-AHT20-SHT40, 16-HMC5883-BNO055-RFID-RC522-Barcode +5 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| MPU6886 | плати | 06-M5Stack-Core-Stick | ✅ `docs.m5stack.com`, `invensense.tdk.com`, `m5stack.com` |
| MPU9250 | сенсори, модулі зв'язку | 19-IMU-6-9DOF, 21-Motion-Control | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| MPXV5010 | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| MPXV5010DP | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| MPXV7002DP | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| MQ135 | сенсори | 22-Gas-2-VOC-Industrial, 35-Tails | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| MR24HPC1 | сенсори | 29-Range-Lidar-60GHz | ✅ `www.infineon.com`, `www.seeedstudio.com`, `www.st.com` |
| MR60 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| MR60FDA | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| MS5611 | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| MS5837 | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| MSGEQ7 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| MSM4 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| MSM7 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| MT3608 | живлення/рівні, проєкти, додатки | 01-Buck-Boost-Solar, 03-TP4056-IP5306-BMS-UPS, 01-Weather-Station, 04-Datasheet-Links +1 | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| MT6701 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| NAU7802 | сенсори | 21-Energy-Meters | ✅ `learn.adafruit.com` |
| NAV5 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| NC16 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| NEMA14 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| NEMA17 | вивід/актуатори | 04-L298N-TB6612-A4988-Buzzer, 06-PCA9685-MG996R-28BYJ48-TMC2209, 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.alldatasheet.com` |
| NEMA23 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| NMEA0183 | модулі зв'язку | 23-Marine-Time | ✅ `docs.espressif.com`, `www.u-blox.com` |
| NMEA2000 | модулі зв'язку | 22-Automotive, 23-Marine-Time | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| NRF24 | чипи/модулі, шини, модулі зв'язку, плати, протоколи, додатки | 08-Anteni-RF, 02-SPI, 01-RC522-RFID, 02-NRF24-LoRa +18 | ✅ `docs.espressif.com`, `docs.heltec.org`, `lilygo.cc` |
| NRF24L01 | шини, модулі зв'язку, додатки | 02-SPI, 02-NRF24-LoRa, 04-Datasheet-Links | ✅ `www.microchip.com`, `www.semtech.com`, `www.ti.com` |
| NS4150 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| NT0104 | живлення/рівні | 02-Level-Shifters | ✅ `www.ti.com` |
| NTAG213 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| NTAG215 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| NTAG216 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| OM5578 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| OPT3001 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| OPT4001 | сенсори | 32-Light-Color-2 | ✅ `ams-osram.com`, `www.nxp.com`, `www.ti.com` |
| OUT1 | вивід/актуатори, модулі зв'язку | 04-L298N-TB6612-A4988-Buzzer, 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| OUT2 | вивід/актуатори | 04-L298N-TB6612-A4988-Buzzer | ✅ `learn.adafruit.com` |
| OUT3 | вивід/актуатори | 04-L298N-TB6612-A4988-Buzzer | ✅ `learn.adafruit.com` |
| OUT4 | вивід/актуатори | 04-L298N-TB6612-A4988-Buzzer | ✅ `learn.adafruit.com` |
| OUT8 | модулі зв'язку | 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| OV2640 | старт, чипи/модулі, модулі зв'язку, плати, проєкти, додатки | 03-Porivnyannya-chipiv, 03-ESP32-S3, 05-Moduli-WROOM-WROVER-MINI, 09-ESP32-C2-P4 +10 | ✅ `circuitpython.org`, `docs.espressif.com`, `wiki.seeedstudio.com` |
| OV3660 | плати | 08-S3-DevKitC-C3-SuperMini-XIAO | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| OV5640 | модулі зв'язку | 13-Camera-Streaming | ✅ `www.ovt.com` |
| OV5647 | чипи/модулі | 12-ESP32-P4-Native | ✅ `docs.espressif.com`, `www.espressif.com` |
| PAM3 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| PAM8403 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| PC814 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| PC817 | вивід/актуатори, модулі зв'язку, живлення/рівні, додатки | 03-NeoPixel-Servo-Rele-MOSFET, 10-Industrial, 14-Proximity-Inputs, 15-RFID-Advanced +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `ww1.microchip.com` |
| PC900 | живлення/рівні | 02-Level-Shifters | ✅ `www.ti.com` |
| PCA9555 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| PCA9557 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| PCA9685 | старт, вивід/актуатори, модулі зв'язку, додатки | 02-Glosariy, 06-PCA9685-MG996R-28BYJ48-TMC2209, 07-BTS7960-L9110S-SSR-Solenoid, 11-PowerMotion-2 +4 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| PCF8523 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| PCF8563 | плати | 12-Retro-Wearable | ✅ `lilygo.cc`, `wiki.lilygo.cc`, `www.alldatasheet.com` |
| PCF8574 | аналог, сенсори, вивід/актуатори, додатки | 01-ADC, 09-ADS1115-MCP3008-PCF8574-MCP23017, 11-NTC-PT100-MAX6675-LM35, 02-TFT-LCD-Epaper +5 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| PCF8574A | сенсори, вивід/актуатори | 09-ADS1115-MCP3008-PCF8574-MCP23017, 16-LCD-Char | ✅ `learn.adafruit.com`, `www.ti.com` |
| PCF8574AT | вивід/актуатори | 16-LCD-Char | ✅ `learn.adafruit.com` |
| PCF8574T | вивід/актуатори | 16-LCD-Char | ✅ `learn.adafruit.com` |
| PCM5102 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| PCM5102A | радіо, вивід/актуатори | 05-BLE-Mesh-A2DP-HID, 13-Audio-Codecs, 19-WebRadio-Streaming | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| PDF417 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| PDU1 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| PDU2 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| PESD3V3 | живлення/рівні, лабораторія | 02-Level-Shifters, 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| PHYAD0 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| PL2303 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| PM10 | сенсори | 08-BME680-CCS811-MHZ19-PMS5003, 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| PMS5003 | сенсори, додатки | 08-BME680-CCS811-MHZ19-PMS5003, 17-Gas-CO2-Precision, 22-Gas-2-VOC-Industrial, 23-Dust-CO2-2 +3 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| PMS5003T | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| PMS7003 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| PMW3360 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| PMW3901 | модулі зв'язку | 21-Motion-Control | ✅ `docs.espressif.com` |
| PN5180 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| PN5180A0XX | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| PN532 | модулі зв'язку, плати, проєкти, додатки | 05-PN532-RDM6300-Fingerprint-GM65, 15-RFID-Advanced, 19-Wired-2, 20-NFC-Biometry-2 +3 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| PN5321A3HN | модулі зв'язку, додатки | 05-PN532-RDM6300-Fingerprint-GM65, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| PN7120 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| PN7150 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| PPD42NS | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| PPK2 | таймери | 03-Sleep-ULP | ✅ `www.nordicsemi.com`, `www.ti.com` |
| PRTR5V0U2X | модулі зв'язку, живлення/рівні, лабораторія | 26-SIM-Power, 02-Level-Shifters, 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| PT100 | аналог, сенсори, додатки | 03-PID-Filters, 09-ADS1115-MCP3008-PCF8574-MCP23017, 11-NTC-PT100-MAX6675-LM35, 30-Temp-Precision +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| PT1000 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| PT2399 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| QFN24 | чипи/модулі | 09-ESP32-C2-P4 | ✅ `docs.espressif.com`, `www.espressif.com` |
| QFN32 | чипи/модулі | 09-ESP32-C2-P4 | ✅ `docs.espressif.com`, `www.espressif.com` |
| QFN4 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| QMC5883L | сенсори, додатки | 16-HMC5883-BNO055-RFID-RC522-Barcode, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| RA8875 | вивід/актуатори | 14-Displays-3 | ✅ `www.alldatasheet.com` |
| RAK3172 | модулі зв'язку | 17-GNSS-RTK, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| RAK7268 | модулі зв'язку | 29-LoRaWAN-Gateway | ✅ `www.chirpstack.io`, `www.semtech.com`, `www.thethingsnetwork.org` |
| RC522 | сенсори, модулі зв'язку, плати, проєкти, додатки | 16-HMC5883-BNO055-RFID-RC522-Barcode, 25-Mag-IMU-2, 01-RC522-RFID, 02-NRF24-LoRa +16 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| RDA8910 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| RDM630 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| RDM6300 | модулі зв'язку, проєкти, додатки | 05-PN532-RDM6300-Fingerprint-GM65, 15-RFID-Advanced, 19-Wired-2, 20-NFC-Biometry-2 +2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| RF24 | модулі зв'язку | 02-NRF24-LoRa | ✅ `www.semtech.com` |
| RFM95 | додатки | 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| RG174 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| RG178 | чипи/модулі | 08-Anteni-RF | ✅ `www.espressif.com` |
| RG58 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| RJ45 | модулі зв'язку, плати | 04-RS485-CAN-Ethernet-Kamera, 07-SIM7600-W5500-MCP2515, 19-Wired-2, 09-WT32-ETH01-Olimex | ✅ `docs.espressif.com`, `docs.kernel.org`, `ww1.microchip.com` |
| RM3100 | сенсори | 31-IMU-Mag-3 | ✅ `www.analog.com`, `www.bosch-sensortec.com` |
| RMD0999C | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| RN00280 | модулі зв'язку | 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| ROUT1 | вивід/актуатори | 13-Audio-Codecs | ✅ `docs.espressif.com` |
| RS232 | старт, шини, модулі зв'язку | 02-Glosariy, 01-UART, 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.alldatasheet.com` |
| RS485 | шини, радіо, сенсори, вивід/актуатори, модулі зв'язку, живлення/рівні, плати, проєкти, додатки | 01-UART, 02-SPI, 05-CAN-TWAI-RS485, 04-ESP-MESH +31 | ✅ `assets.bosch-sensortec.com`, `circuitpython.org`, `docs.arduino.cc` |
| RSA2048 | протоколи | 12-AWS-IoT | ✅ `docs.aws.amazon.com` |
| RT9080 | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| RTCM3 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| RUI3 | модулі зв'язку | 17-GNSS-RTK, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| RV32IMC | таймери | 03-Sleep-ULP | ✅ `www.nordicsemi.com`, `www.ti.com` |
| RW007 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| RXD0 | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera, 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| RXD1 | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera, 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| RXD2 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| RXD3 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| RYLR896 | модулі зв'язку | 09-Cellular-NBIoT-UARTLoRa | ✅ `docs.espressif.com`, `www.semtech.com`, `www.simcom.com` |
| RYLR998 | модулі зв'язку | 09-Cellular-NBIoT-UARTLoRa, 15-RFID-Advanced | ✅ `docs.espressif.com`, `www.nxp.com`, `www.semtech.com` |
| SAC305 | живлення/рівні, лабораторія | 07-Stencil-Reflow, 02-Soldering-Connectors, 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| SBUS2 | модулі зв'язку | 12-RC-Protocols | ✅ `www.alldatasheet.com` |
| SC01 | вивід/актуатори, плати | 17-Touchscreens, 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.alldatasheet.com`, `www.espressif.com` |
| SC16IS750 | модулі зв'язку | 24-DIY-Instruments | ✅ `www.analog.com`, `www.nxp.com`, `www.ti.com` |
| SCD30 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SCD40 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SCD41 | сенсори | 17-Gas-CO2-Precision, 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SCP03 | модулі зв'язку | 25-Secure-Elements | ✅ `docs.espressif.com`, `learn.microchip.com`, `www.alldatasheet.com` |
| SDM120 | сенсори, проєкти | 21-Energy-Meters, 04-Energy-Monitor | ✅ `learn.adafruit.com`, `www.eastronuk.com` |
| SDM630 | сенсори, проєкти | 21-Energy-Meters, 04-Energy-Monitor | ✅ `learn.adafruit.com`, `www.eastronuk.com` |
| SDS011 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| SDS021 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| SE050 | модулі зв'язку, додатки | 25-Secure-Elements, 04-Datasheet-Links | ✅ `docs.espressif.com`, `learn.microchip.com`, `www.alldatasheet.com` |
| SE3307 | модулі зв'язку | 05-PN532-RDM6300-Fingerprint-GM65 | ✅ `www.nxp.com` |
| SEL0 | модулі зв'язку, додатки | 05-PN532-RDM6300-Fingerprint-GM65, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| SEL1 | модулі зв'язку, додатки | 05-PN532-RDM6300-Fingerprint-GM65, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| SEN54 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SEN55 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SEN66 | сенсори | 28-Env-NewGen | ✅ `sensirion.com`, `www.bosch-sensortec.com` |
| SFM3000 | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SFM3019 | сенсори | 24-Pressure-Level-Flow | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SG90 | gpio, вивід/актуатори, додатки | 04-Pererivannya-PWM, 03-NeoPixel-Servo-Rele-MOSFET, 06-PCA9685-MG996R-28BYJ48-TMC2209, 02-Troubleshooting-FAQ +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| SGP30 | сенсори | 17-Gas-CO2-Precision, 22-Gas-2-VOC-Industrial, 35-Tails | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| SGP40 | сенсори | 22-Gas-2-VOC-Industrial, 35-Tails | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| SGP41 | сенсори, додатки | 22-Gas-2-VOC-Industrial, 35-Tails, 07-Versions | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| SGP43 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SGPC3 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SH1106 | вивід/актуатори | 01-OLED-SSD1306, 10-Displays-2 | ✅ `learn.adafruit.com` |
| SHT20 | сенсори | 07-AHT10-AHT20-SHT40 | ✅ `learn.adafruit.com`, `sensirion.com` |
| SHT31 | шини, радіо, сенсори, плати, проєкти, додатки | 03-I2C, 02-BLE-Bluetooth, 03-ESP-NOW, 01-DHT11-DHT22 +25 | ✅ `amphenol-sensors.com`, `assets.bosch-sensortec.com`, `docs.espressif.com` |
| SHT40 | сенсори, плати, проєкти, додатки | 07-AHT10-AHT20-SHT40, 08-BME680-CCS811-MHZ19-PMS5003, 10-VL53L0X-TCS34725-TSL2561, 11-NTC-PT100-MAX6675-LM35 +6 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| SHT41 | сенсори, додатки | 07-AHT10-AHT20-SHT40, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| SHT43 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| SHT45 | сенсори, додатки | 07-AHT10-AHT20-SHT40, 17-Gas-CO2-Precision, 20-Bio-IR-Temp, 35-Tails +1 | ✅ `amphenol-sensors.com`, `docs.espressif.com`, `learn.adafruit.com` |
| SHT85 | сенсори | 17-Gas-CO2-Precision | ✅ `learn.adafruit.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| SI1133 | сенсори | 32-Light-Color-2 | ✅ `ams-osram.com`, `www.nxp.com`, `www.ti.com` |
| SI2301 | таймери | 04-TPL5110 | ✅ `learn.adafruit.com`, `www.ti.com` |
| SI4463 | модулі зв'язку, додатки | 06-HC05-HM10-CC1101-HC12, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| SIM7080 | модулі зв'язку | 18-Cellular-LoRa-2, 26-SIM-Power | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| SIM7080G | модулі зв'язку | 09-Cellular-NBIoT-UARTLoRa, 17-GNSS-RTK, 18-Cellular-LoRa-2, 26-SIM-Power | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| SIM7600 | шини, радіо, модулі зв'язку, плати, проєкти, додатки | 06-USB-OTG-JTAG, 01-WiFi-STA-AP, 03-SIM800L-GPS, 07-SIM7600-W5500-MCP2515 +12 | ✅ `docs.espressif.com`, `docs.kernel.org`, `learn.adafruit.com` |
| SIM7600E | модулі зв'язку, додатки | 07-SIM7600-W5500-MCP2515, 26-SIM-Power, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| SIM7600G | проєкти | 02-GPS-Tracker | ✅ `www.simcom.com`, `www.u-blox.com` |
| SIM7600X | модулі зв'язку, додатки | 07-SIM7600-W5500-MCP2515, 09-Cellular-NBIoT-UARTLoRa, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| SIM800 | модулі зв'язку, додатки | 03-SIM800L-GPS, 09-Cellular-NBIoT-UARTLoRa, 18-Cellular-LoRa-2, 26-SIM-Power +2 | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| SIM800L | шини, радіо, модулі зв'язку, плати, проєкти, додатки | 01-UART, 04-ESP-MESH, 01-RC522-RFID, 02-NRF24-LoRa +15 | ✅ `docs.espressif.com`, `docs.heltec.org`, `lilygo.cc` |
| SJA1000 | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera | ✅ `www.ti.com` |
| SJA1124 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| SK6812 | таймери, вивід/актуатори, протоколи, додатки | 01-Timeri-MCPWM-PCNT-RMT, 09-LED-Strip-Power-SK6812-APA102, 06-Firmwares, 07-Notify-Voice +3 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| SLOT1 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| SM712 | живлення/рівні | 02-Level-Shifters | ✅ `www.ti.com` |
| SMBJ12A | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| SMBJ24A | модулі зв'язку | 22-Automotive, 23-Marine-Time | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| SMBJ28A | модулі зв'язку | 22-Automotive, 23-Marine-Time | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| SMBJ36A | модулі зв'язку | 23-Marine-Time | ✅ `docs.espressif.com`, `www.u-blox.com` |
| SMBJ5 | старт, живлення, живлення/рівні, лабораторія | 02-Glosariy, 01-Lancjugi-zhivlennya, 02-Level-Shifters, 04-LDO-Buck-XL4015-Protect +1 | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| SMD291AX | живлення/рівні | 07-Stencil-Reflow | ✅ `jlcpcb.com`, `www.ipc.org` |
| SN65HVD230 | шини, модулі зв'язку, додатки | 05-CAN-TWAI-RS485, 04-RS485-CAN-Ethernet-Kamera, 19-Wired-2, 22-Automotive +3 | ✅ `docs.espressif.com`, `docs.kernel.org`, `ww1.microchip.com` |
| SN74HC14 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| SN74LVC2T45 | живлення/рівні | 02-Level-Shifters | ✅ `www.ti.com` |
| SP3232 | шини | 01-UART | ✅ `www.alldatasheet.com`, `www.ti.com` |
| SP3485 | шини | 01-UART | ✅ `www.alldatasheet.com`, `www.ti.com` |
| SPH0645 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| SPH0645LM4H | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| SPM1423 | плати | 06-M5Stack-Core-Stick | ✅ `docs.m5stack.com`, `invensense.tdk.com`, `m5stack.com` |
| SPS30 | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| SPV1050 | живлення/рівні | 01-Buck-Boost-Solar | ✅ `www.alldatasheet.com`, `www.ti.com` |
| SQ110 | сенсори | 36-Agro | ✅ `www.modbus.org` |
| SRX882 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| SS12D00 | сенсори | 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.ti.com` |
| SS14 | проєкти | 01-Weather-Station | ✅ `docs.espressif.com` |
| SS34 | модулі зв'язку, живлення/рівні | 22-Automotive, 04-LDO-Buck-XL4015-Protect | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| SS54 | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| SSD1306 | шини, вивід/актуатори, плати, додатки | 03-I2C, 01-OLED-SSD1306, 02-TFT-LCD-Epaper, 03-NeoPixel-Servo-Rele-MOSFET +7 | ✅ `docs.espressif.com`, `docs.heltec.org`, `learn.adafruit.com` |
| SSD1309 | вивід/актуатори | 10-Displays-2 | ✅ `learn.adafruit.com` |
| SSD1322 | вивід/актуатори | 14-Displays-3 | ✅ `www.alldatasheet.com` |
| SSD1351 | вивід/актуатори | 14-Displays-3 | ✅ `www.alldatasheet.com` |
| SSD1675 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| SSD1675A | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| SSD1675B | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| SSD1680 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| SSD1681 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| SSD2805 | вивід/актуатори | 14-Displays-3 | ✅ `www.alldatasheet.com` |
| ST25R3911 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| ST25R3911B | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| ST25R3916 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ST4000 | модулі зв'язку | 23-Marine-Time | ✅ `docs.espressif.com`, `www.u-blox.com` |
| ST7066 | вивід/актуатори | 16-LCD-Char | ✅ `learn.adafruit.com` |
| ST7262 | вивід/актуатори, плати | 17-Touchscreens, 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.alldatasheet.com`, `www.espressif.com` |
| ST7265 | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| ST7735 | вивід/актуатори | 10-Displays-2 | ✅ `learn.adafruit.com` |
| ST7789 | вивід/актуатори, модулі зв'язку, плати, додатки | 02-TFT-LCD-Epaper, 17-Touchscreens, 11-TinyML-Voice, 03-LILYGO-TDisplay-TBeam +3 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `lilygo.cc` |
| ST7789V | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| ST7796 | вивід/актуатори | 14-Displays-3, 17-Touchscreens | ✅ `www.alldatasheet.com`, `www.ti.com` |
| ST7796S | плати | 11-HMI-Boards | ✅ `wiki.lilygo.cc`, `www.espressif.com`, `www.guition.com` |
| ST8002 | модулі зв'язку | 23-Marine-Time | ✅ `docs.espressif.com`, `www.u-blox.com` |
| STM32 | старт, gpio, вивід/актуатори, модулі зв'язку | 05-Vibir-seredovischa, 03-Pidtyaguvannya-rivni, 12-LVGL-SquareLine, 21-Motion-Control | ✅ `docs.espressif.com`, `www.espressif.com`, `www.ti.com` |
| STM32F042 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| STM32F4 | модулі зв'язку | 21-Motion-Control, 29-LoRaWAN-Gateway-Deep | ✅ `docs.espressif.com`, `lora-alliance.org`, `www.st.com` |
| STM32WLE | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| STM32WLE5 | модулі зв'язку | 17-GNSS-RTK, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| STM32WLE5CC | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| STR2STR | модулі зв'язку | 17-GNSS-RTK, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| STS35 | сенсори | 30-Temp-Precision | ✅ `sensirion.com`, `www.analog.com`, `www.microchip.com` |
| SV5W | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| SW2303 | живлення/рівні | 09-USB-PD | ✅ `www.onsemi.com`, `www.usb.org`, `www.wch.cn` |
| SX1262 | модулі зв'язку, плати | 09-Cellular-NBIoT-UARTLoRa, 17-GNSS-RTK, 18-Cellular-LoRa-2, 03-LILYGO-TDisplay-TBeam +2 | ✅ `docs.espressif.com`, `docs.heltec.org`, `lilygo.cc` |
| SX1268 | модулі зв'язку | 29-LoRaWAN-Gateway-Deep | ✅ `lora-alliance.org`, `www.st.com`, `www.waveshare.com` |
| SX1276 | модулі зв'язку, плати, додатки | 02-NRF24-LoRa, 09-Cellular-NBIoT-UARTLoRa, 18-Cellular-LoRa-2, 29-LoRaWAN-Gateway +4 | ✅ `docs.espressif.com`, `docs.heltec.org`, `lilygo.cc` |
| SX1278 | модулі зв'язку | 02-NRF24-LoRa | ✅ `www.semtech.com` |
| SX1280 | модулі зв'язку, плати | 17-GNSS-RTK, 18-Cellular-LoRa-2, 12-Retro-Wearable | ✅ `docs.espressif.com`, `lilygo.cc`, `wiki.lilygo.cc` |
| SX1302 | модулі зв'язку | 29-LoRaWAN-Gateway-Deep, 29-LoRaWAN-Gateway | ✅ `lora-alliance.org`, `www.chirpstack.io`, `www.semtech.com` |
| SX1509 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| SY8113 | живлення, модулі зв'язку, лабораторія | 02-LDO-DC-DC, 26-SIM-Power, 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| SYN6288 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| SYN7318 | модулі зв'язку, протоколи | 16-Offline-Voice, 10-Voice-Assistant | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| TB6600 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| TB6612 | аналог, таймери, сенсори, вивід/актуатори, проєкти, додатки | 03-PID-Filters, 01-Timeri-MCPWM-PCNT-RMT, 05-HC-SR04-PIR, 03-NeoPixel-Servo-Rele-MOSFET +7 | ✅ `assets.bosch-sensortec.com`, `docs.espressif.com`, `learn.adafruit.com` |
| TB6612FNG | вивід/актуатори, додатки | 04-L298N-TB6612-A4988-Buzzer, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| TC4056A | живлення/рівні | 03-TP4056-IP5306-BMS-UPS | ✅ `www.ti.com` |
| TCA8418 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| TCA9548 | шини, сенсори | 03-I2C, 25-Mag-IMU-2, 27-Time-Mem-IO-DAC | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.bosch-sensortec.com` |
| TCA9548A | сенсори | 07-AHT10-AHT20-SHT40, 10-VL53L0X-TCS34725-TSL2561, 17-Gas-CO2-Precision, 18-Light-Spectral-Gesture +3 | ✅ `ams-osram.com`, `learn.adafruit.com`, `sensirion.com` |
| TCAN1042 | модулі зв'язку | 19-Wired-2 | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| TCAN4550 | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| TCS3400 | сенсори | 18-Light-Spectral-Gesture | ✅ `learn.adafruit.com` |
| TCS34725 | сенсори, плати, проєкти, додатки | 10-VL53L0X-TCS34725-TSL2561, 26-Light-UV-IRArray-ToF, 29-Range-Lidar-60GHz, 32-Light-Color-2 +5 | ✅ `amphenol-sensors.com`, `ams-osram.com`, `assets.bosch-sensortec.com` |
| TCST2103 | модулі зв'язку | 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| TDA1085C | модулі зв'язку | 10-Industrial | ✅ `learn.adafruit.com`, `www.ti.com` |
| TDA1543 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| TDM4 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| TDM8 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| TG0WDT | живлення | 03-Spozhivannya | ✅ `docs.espressif.com` |
| TGS2600 | сенсори | 22-Gas-2-VOC-Industrial | ✅ `learn.adafruit.com`, `sensirion.com` |
| TGS8100 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| THVD1400 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| TIOL111 | сенсори | 38-Industrial-Sensors | ✅ `www.analog.com`, `www.ti.com` |
| TJA1020 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| TJA1050 | старт, шини, модулі зв'язку, плати, додатки | 02-Glosariy, 05-CAN-TWAI-RS485, 04-RS485-CAN-Ethernet-Kamera, 07-SIM7600-W5500-MCP2515 +5 | ✅ `docs.espressif.com`, `docs.kernel.org`, `ww1.microchip.com` |
| TJA1080 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| TK4100 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| TL431 | сенсори | 09-ADS1115-MCP3008-PCF8574-MCP23017 | ✅ `www.ti.com` |
| TLE5012 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| TLP2362 | модулі зв'язку | 14-Proximity-Inputs | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| TLSR8251 | радіо | 06-BLE-Gateway-Tracker | ✅ `docs.espressif.com` |
| TLV1117 | живлення/рівні, додатки | 04-LDO-Buck-XL4015-Protect, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| TLV493D | сенсори | 25-Mag-IMU-2 | ✅ `learn.adafruit.com`, `www.bosch-sensortec.com` |
| TM1637 | вивід/актуатори, додатки | 05-MAX7219-TM1637-74HC595, 09-LED-Strip-Power-SK6812-APA102, 10-Displays-2, 02-Troubleshooting-FAQ +1 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| TM1638 | вивід/актуатори | 10-Displays-2 | ✅ `learn.adafruit.com` |
| TM1650 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| TMC2209 | старт, вивід/актуатори, модулі зв'язку, додатки | 02-Glosariy, 06-PCA9685-MG996R-28BYJ48-TMC2209, 07-BTS7960-L9110S-SSR-Solenoid, 11-PowerMotion-2 +4 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| TMC2226 | вивід/актуатори | 11-PowerMotion-2 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| TMC5160 | вивід/актуатори, модулі зв'язку | 11-PowerMotion-2, 21-Motion-Control | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| TMD3725 | сенсори | 32-Light-Color-2 | ✅ `ams-osram.com`, `www.nxp.com`, `www.ti.com` |
| TMF8806 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| TMF8820 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| TMF8821 | сенсори | 29-Range-Lidar-60GHz | ✅ `www.infineon.com`, `www.seeedstudio.com`, `www.st.com` |
| TMODE3 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| TMP117 | сенсори | 27-Time-Mem-IO-DAC | ✅ `learn.adafruit.com` |
| TMP36 | сенсори | 11-NTC-PT100-MAX6675-LM35 | ✅ `www.ti.com` |
| TP4056 | старт, живлення, таймери, живлення/рівні, плати, проєкти, лабораторія, додатки | 02-Glosariy, 01-Lancjugi-zhivlennya, 02-LDO-DC-DC, 03-Spozhivannya +25 | ✅ `docs.arduino.cc`, `docs.espressif.com`, `docs.heltec.org` |
| TP5100 | живлення/рівні | 03-TP4056-IP5306-BMS-UPS | ✅ `www.ti.com` |
| TPA3116 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| TPA3116D2 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| TPIC6B595 | вивід/актуатори | 05-MAX7219-TM1637-74HC595 | ✅ `www.ti.com` |
| TPL5110 | таймери | 02-WDT, 04-TPL5110 | ✅ `learn.adafruit.com`, `www.alldatasheet.com`, `www.ti.com` |
| TPL5111 | таймери | 04-TPL5110 | ✅ `learn.adafruit.com`, `www.ti.com` |
| TPS2051 | модулі зв'язку | 30-USB-Host, 32-USB-UVC-Host-Deep | ✅ `docs.espressif.com` |
| TPS25921 | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| TPS3823 | живлення, таймери | 02-LDO-DC-DC, 02-WDT | ✅ `www.alldatasheet.com`, `www.microchip.com`, `www.ti.com` |
| TPS563201 | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| TPS63020 | живлення | 02-LDO-DC-DC | ✅ `www.microchip.com`, `www.ti.com` |
| TPS737 | таймери | 03-Sleep-ULP | ✅ `www.nordicsemi.com`, `www.ti.com` |
| TRF7970A | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| TSC2007 | вивід/актуатори | 17-Touchscreens | ✅ `www.alldatasheet.com`, `www.ti.com` |
| TSDP34138 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSL2561 | сенсори, плати, проєкти, додатки | 10-VL53L0X-TCS34725-TSL2561, 26-Light-UV-IRArray-ToF, 29-Range-Lidar-60GHz, 32-Light-Color-2 +5 | ✅ `amphenol-sensors.com`, `ams-osram.com`, `assets.bosch-sensortec.com` |
| TSL2581 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSL2583 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSL2591 | сенсори | 18-Light-Spectral-Gesture, 35-Tails | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| TSMP93 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSMP95 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP32338 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP34438 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP38238 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP48 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP4830 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP4833 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP4836 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP4838 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP4840 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP48438 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TSOP4856 | сенсори | 35-Tails | ✅ `amphenol-sensors.com`, `sensirion.com`, `www.bosch-sensortec.com` |
| TTP223 | сенсори | 33-Input-IO-2, 34-Buttons-Switches-Pots | ✅ `docs.espressif.com`, `docs.micropython.org`, `www.alldatasheet.com` |
| TTP229 | сенсори | 33-Input-IO-2 | ✅ `www.alldatasheet.com` |
| TW3882 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| TXB0104 | живлення/рівні | 02-Level-Shifters | ✅ `www.ti.com` |
| TXB0108 | gpio, живлення/рівні, додатки | 03-Pidtyaguvannya-rivni, 02-Level-Shifters, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.espressif.com` |
| TXD0 | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera | ✅ `www.ti.com` |
| TXD1 | модулі зв'язку | 04-RS485-CAN-Ethernet-Kamera | ✅ `www.ti.com` |
| TXS0102 | вивід/актуатори | 09-LED-Strip-Power-SK6812-APA102 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| TXS0108 | gpio, живлення/рівні | 01-GPIO-oglyad, 03-Pidtyaguvannya-rivni, 02-Level-Shifters | ✅ `docs.espressif.com`, `www.espressif.com`, `www.ti.com` |
| TXS0108E | старт, gpio, вивід/актуатори, модулі зв'язку, живлення/рівні, плати, додатки | 02-Glosariy, 03-Pidtyaguvannya-rivni, 05-MAX7219-TM1637-74HC595, 08-DFPlayer-MAX98357-Nextion-LCD2004 +6 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `wiki.seeedstudio.com` |
| UC8151 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| UC8151D | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| UC8176 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| UC8179 | вивід/актуатори | 15-EInk | ✅ `learn.adafruit.com`, `www.waveshare.com` |
| UCS2 | модулі зв'язку | 03-SIM800L-GPS, 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| UDA1334 | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| UDA1334A | шини | 04-I2S | ✅ `docs.espressif.com`, `docs.micropython.org` |
| UF4007 | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| UG65 | модулі зв'язку | 29-LoRaWAN-Gateway | ✅ `www.chirpstack.io`, `www.semtech.com`, `www.thethingsnetwork.org` |
| UG67 | модулі зв'язку | 29-LoRaWAN-Gateway | ✅ `www.chirpstack.io`, `www.semtech.com`, `www.thethingsnetwork.org` |
| UID0 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| UID1 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| UID2 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| UID3 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| UID5 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| UID6 | модулі зв'язку | 15-RFID-Advanced, 20-NFC-Biometry-2 | ✅ `learn.adafruit.com`, `www.nxp.com`, `www.ti.com` |
| UID9 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ULN2003 | сенсори, вивід/актуатори | 09-ADS1115-MCP3008-PCF8574-MCP23017, 05-MAX7219-TM1637-74HC595, 06-PCA9685-MG996R-28BYJ48-TMC2209 | ✅ `www.alldatasheet.com`, `www.ti.com` |
| UM10204 | шини | 03-I2C | ✅ `docs.espressif.com`, `www.nxp.com` |
| UM980 | модулі зв'язку, додатки | 17-GNSS-RTK, 18-Cellular-LoRa-2, 04-Datasheet-Links | ✅ `docs.espressif.com`, `www.microchip.com`, `www.quectel.com` |
| UNI3588 | модулі зв'язку | 16-Offline-Voice | ✅ `docs.espressif.com`, `wiki.seeedstudio.com` |
| US915 | модулі зв'язку | 18-Cellular-LoRa-2 | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| USBLC6 | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| UT61E | живлення | 03-Spozhivannya | ✅ `docs.espressif.com` |
| VCC1 | модулі зв'язку | 19-Wired-2, 23-Marine-Time | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| VCC2 | модулі зв'язку | 19-Wired-2, 23-Marine-Time | ✅ `docs.espressif.com`, `docs.kernel.org`, `www.ti.com` |
| VDD3P3 | лабораторія | 04-PCB-Design | ✅ `docs.espressif.com`, `jlcpcb.com`, `www.analog.com` |
| VEML6040 | сенсори | 32-Light-Color-2 | ✅ `ams-osram.com`, `www.nxp.com`, `www.ti.com` |
| VEML6070 | сенсори | 10-VL53L0X-TCS34725-TSL2561 | ✅ `learn.adafruit.com` |
| VEML6075 | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| VEML7700 | сенсори | 18-Light-Spectral-Gesture | ✅ `learn.adafruit.com` |
| VGA32 | плати | 12-Retro-Wearable | ✅ `lilygo.cc`, `wiki.lilygo.cc`, `www.alldatasheet.com` |
| VL53 | сенсори | 26-Light-UV-IRArray-ToF, 29-Range-Lidar-60GHz | ✅ `learn.adafruit.com`, `www.infineon.com`, `www.seeedstudio.com` |
| VL53L0X | сенсори, плати, проєкти, додатки | 05-HC-SR04-PIR, 10-VL53L0X-TCS34725-TSL2561, 18-Light-Spectral-Gesture, 26-Light-UV-IRArray-ToF +7 | ✅ `amphenol-sensors.com`, `ams-osram.com`, `assets.bosch-sensortec.com` |
| VL53L1X | сенсори | 18-Light-Spectral-Gesture | ✅ `learn.adafruit.com` |
| VL53L4CD | сенсори | 29-Range-Lidar-60GHz | ✅ `www.infineon.com`, `www.seeedstudio.com`, `www.st.com` |
| VL53L5CX | сенсори | 26-Light-UV-IRArray-ToF | ✅ `learn.adafruit.com` |
| VL53L7CX | сенсори | 29-Range-Lidar-60GHz | ✅ `www.infineon.com`, `www.seeedstudio.com`, `www.st.com` |
| VS1053 | вивід/актуатори | 18-MP3-TTS-Amps, 19-WebRadio-Streaming | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| VS1838 | сенсори, модулі зв'язку | 16-HMC5883-BNO055-RFID-RC522-Barcode, 08-LD2410-UWB-IR-Voice | ✅ `learn.adafruit.com`, `www.alldatasheet.com`, `www.bosch-sensortec.com` |
| VS1838B | модулі зв'язку, додатки | 08-LD2410-UWB-IR-Voice, 06-Official-Sources-Modules | ✅ `docs.espressif.com`, `ww1.microchip.com`, `www.alldatasheet.com` |
| WGS84 | модулі зв'язку | 17-GNSS-RTK | ✅ `docs.espressif.com`, `www.quectel.com`, `www.semtech.com` |
| WIZNET5K | модулі зв'язку | 31-Ethernet-PoE-Deep | ✅ `mqtt.org` |
| WM8978 | вивід/актуатори | 13-Audio-Codecs | ✅ `docs.espressif.com` |
| WPA2 | радіо, протоколи, додатки | 01-WiFi-STA-AP, 08-Security-Hardening, 02-Troubleshooting-FAQ | ✅ `docs.espressif.com` |
| WPA3 | радіо, протоколи, додатки | 01-WiFi-STA-AP, 08-Security-Hardening, 02-Troubleshooting-FAQ | ✅ `docs.espressif.com` |
| WS2801 | вивід/актуатори, протоколи | 09-LED-Strip-Power-SK6812-APA102, 06-Firmwares | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.alldatasheet.com` |
| WS2811 | вивід/актуатори, протоколи | 09-LED-Strip-Power-SK6812-APA102, 06-Firmwares | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.alldatasheet.com` |
| WS2812 | старт, чипи/модулі, gpio, шини, таймери, вивід/актуатори, живлення/рівні, протоколи, додатки | 02-Glosariy, 05-Vibir-seredovischa, 03-ESP32-S3, 04-ESP32-C3-C6-H2 +9 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| WS2812B | вивід/актуатори, протоколи | 03-NeoPixel-Servo-Rele-MOSFET, 09-LED-Strip-Power-SK6812-APA102, 06-Firmwares | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.alldatasheet.com` |
| WS2813 | вивід/актуатори | 09-LED-Strip-Power-SK6812-APA102 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| WS2815 | таймери, вивід/актуатори | 01-Timeri-MCPWM-PCNT-RMT, 09-LED-Strip-Power-SK6812-APA102 | ✅ `docs.espressif.com`, `learn.adafruit.com` |
| WT32 | старт, вивід/актуатори, модулі зв'язку, плати | 04-Devkit-plati, 17-Touchscreens, 04-RS485-CAN-Ethernet-Kamera, 09-WT32-ETH01-Olimex +1 | ✅ `wiki.lilygo.cc`, `www.alldatasheet.com`, `www.espressif.com` |
| XC6206 | живлення, таймери, живлення/рівні | 02-LDO-DC-DC, 03-Sleep-ULP, 01-Buck-Boost-Solar | ✅ `www.alldatasheet.com`, `www.microchip.com`, `www.nordicsemi.com` |
| XFS5152 | вивід/актуатори | 18-MP3-TTS-Amps | ✅ `docs.espressif.com`, `learn.adafruit.com`, `www.ti.com` |
| XL1509 | модулі зв'язку | 22-Automotive | ✅ `docs.espressif.com`, `www.nxp.com`, `www.ti.com` |
| XL4015 | старт, живлення, модулі зв'язку, живлення/рівні, плати, проєкти, лабораторія, додатки | 02-Glosariy, 02-LDO-DC-DC, 03-SIM800L-GPS, 26-SIM-Power +8 | ✅ `assets.bosch-sensortec.com`, `docs.espressif.com`, `jlcpcb.com` |
| XL6009 | живлення/рівні | 04-LDO-Buck-XL4015-Protect | ✅ `www.ti.com` |
| XPT2046 | вивід/актуатори, плати | 02-TFT-LCD-Epaper, 10-Displays-2, 12-LVGL-SquareLine, 17-Touchscreens +2 | ✅ `docs.espressif.com`, `learn.adafruit.com`, `wiki.lilygo.cc` |
| XTR115 | сенсори, модулі зв'язку, додатки | 38-Industrial-Sensors, 10-Industrial, 14-Proximity-Inputs, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| XTR116 | сенсори | 38-Industrial-Sensors | ✅ `www.analog.com`, `www.ti.com` |
| YOLO26 | модулі зв'язку | 11-TinyML-Voice | ✅ `www.alldatasheet.com` |
| YR9035 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| YRM100 | модулі зв'язку | 15-RFID-Advanced | ✅ `www.nxp.com`, `www.ti.com` |
| ZE07 | сенсори | 22-Gas-2-VOC-Industrial | ✅ `learn.adafruit.com`, `sensirion.com` |
| ZE08 | сенсори | 22-Gas-2-VOC-Industrial | ✅ `learn.adafruit.com`, `sensirion.com` |
| ZH03B | сенсори | 23-Dust-CO2-2 | ✅ `learn.adafruit.com`, `sensirion.com` |
| ZMOD4410 | сенсори | 22-Gas-2-VOC-Industrial | ✅ `learn.adafruit.com`, `sensirion.com` |
| ZMOD4510 | сенсори | 22-Gas-2-VOC-Industrial, 35-Tails | ✅ `amphenol-sensors.com`, `learn.adafruit.com`, `sensirion.com` |
| ZMPT101B | сенсори, проєкти, додатки | 15-ACS712-ZMPT101B-PZEM-AS5600-FSR, 04-Energy-Monitor, 02-Troubleshooting-FAQ, 05-Official-Sources-Sensors | ✅ `docs.espressif.com`, `learn.adafruit.com`, `sensirion.com` |
| ZP07 | сенсори | 22-Gas-2-VOC-Industrial | ✅ `learn.adafruit.com`, `sensirion.com` |
