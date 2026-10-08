# Реєстр компонентів STM32-Reference

> Згенеровано 2026-10-07: `python3 scripts/comp_inventory.py --registry COMPONENTS.md`. НЕ редагувати вручну — перегенерувати!
>
> ✅ = хоча б в одній ноті-згадці є посилання виробника. Це НЕ гарантує, що лінк саме на цей компонент — звіряти вручну!
>
> ❌ = у жодній ноті-згадці немає виробничих посилань. Пріоритетні кандидати на додавання даташитів.

**Позначень:** 246; **з datasheet:** 246; **без:** 0.

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
| ACS712 | сенсори | 12-Strum-Potuzhnist | ✅ `www.ti.com` |
| AF15 | старт, gpio | 02-Glosariy, 02-AF-maping | ✅ `www.st.com` |
| AMS1117 | живлення, модулі зв'язку, лабораторія | 03-Power-Design, 06-WiFi-ESP-AT, 05-Maketka | ✅ `docs.espressif.com`, `mqtt.org`, `www.espressif.com` |
| APDS9960 | сенсори | 14-Mag-Gesture-RTC | ✅ `www.u-blox.com` |
| AS5600 | сенсори | 11-Encoder | ✅ `ams-osram.com`, `www.st.com` |
| BC417 | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| BH1750 | сенсори | 08-Light-BH-TSL | ✅ `ams-osram.com`, `www.rohm.com` |
| BLPS0003 | сенсори | 06-Pressure-BMP-MS | ✅ `www.bosch-sensortec.com`, `www.te.com` |
| BME280 | прошивка, сенсори, проєкти | 05-Shablon-Drayvera, 01-DHT11-DS18B20, 02-BME280-SHT3x, 04-INA219-HX711 +5 | ✅ `ams-osram.com`, `sensirion.com`, `www.analog.com` |
| BMP280 | шини, сенсори | 03-I2C, 02-BME280-SHT3x | ✅ `sensirion.com`, `www.bosch-sensortec.com`, `www.nxp.com` |
| BMP390 | сенсори | 06-Pressure-BMP-MS | ✅ `www.bosch-sensortec.com`, `www.te.com` |
| BOR1 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| BOR4 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| CC2541 | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| CR2032 | старт, чипи/модулі, живлення, сенсори | 02-Glosariy, 05-L0-L4-U5, 02-Batareyne-zhivlennya, 14-Mag-Gesture-RTC | ✅ `www.st.com`, `www.u-blox.com` |
| CR2450 | чипи/модулі, живлення, вивід/актуатори | 05-L0-L4-U5, 06-WB-WL, 02-Batareyne-zhivlennya, 04-Epaper | ✅ `www.st.com`, `www.waveshare.com` |
| CS32F103 | старт | 03-Porivnyannya-chipiv | ✅ `www.st.com` |
| DFR0299 | вивід/актуатори | 08-Audio-DFPlayer | ✅ `www.ti.com` |
| DHT11 | сенсори | 01-DHT11-DS18B20, 02-BME280-SHT3x, 03-MPU6050-IMU | ✅ `invensense.tdk.com`, `sensirion.com`, `www.analog.com` |
| DHT22 | сенсори | 01-DHT11-DS18B20 | ✅ `www.analog.com` |
| DMA2D | вивід/актуатори | 05-LVGL | ✅ `www.st.com` |
| DS18B20 | сенсори | 01-DHT11-DS18B20, 02-BME280-SHT3x, 03-MPU6050-IMU | ✅ `invensense.tdk.com`, `sensirion.com`, `www.analog.com` |
| DS3231 | сенсори | 14-Mag-Gesture-RTC | ✅ `www.u-blox.com` |
| DW01 | живлення, живлення/рівні | 02-Batareyne-zhivlennya, 03-Charger-Protect | ✅ `www.ic-fortune.com`, `www.st.com` |
| ER14505 | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| ESP32 | модулі зв'язку, проєкти | 06-WiFi-ESP-AT, 08-DCMI-Camera, 06-Drone-FC | ✅ `docs.espressif.com`, `mqtt.org`, `www.espressif.com` |
| ESP8266 | модулі зв'язку | 06-WiFi-ESP-AT | ✅ `docs.espressif.com`, `mqtt.org`, `www.espressif.com` |
| EXTI0 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI1 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI11 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI12 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI15 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI16 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI2 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI3 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI4 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI7 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTI8 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTICR1 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTICR2 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTICR3 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| EXTICR4 | gpio | 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| FAT16 | вивід/актуатори | 08-Audio-DFPlayer | ✅ `www.ti.com` |
| FAT32 | шини, вивід/актуатори | 06-SDMMC-QUADSPI, 08-Audio-DFPlayer | ✅ `www.st.com`, `www.ti.com` |
| FDCAN1 | шини | 04-FDCAN | ✅ `www.st.com` |
| FFE0 | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| FFE1 | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| FS8205 | живлення/рівні | 03-Charger-Protect | ✅ `www.ic-fortune.com` |
| GD32 | старт | 03-Porivnyannya-chipiv | ✅ `www.st.com` |
| HTS221 | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| HX711 | живлення, аналог, сенсори, проєкти | 03-Power-Design, 05-Shunt-OPAMP, 03-MPU6050-IMU, 04-INA219-HX711 +2 | ✅ `invensense.tdk.com`, `www.olimex.com`, `www.st.com` |
| ILI9341 | вивід/актуатори | 02-TFT-LCD | ✅ `www.st.com` |
| INA219 | живлення, шини, аналог, сенсори, проєкти | 03-Power-Design, 03-I2C, 05-Shunt-OPAMP, 03-MPU6050-IMU +3 | ✅ `invensense.tdk.com`, `www.nxp.com`, `www.olimex.com` |
| INA226 | сенсори | 12-Strum-Potuzhnist | ✅ `www.ti.com` |
| INCR4 | шини | 07-DMA-DeepDive | ✅ `www.st.com` |
| IOT01A | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| IRFB7199 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| ISM43362 | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| LIS3MDL | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| LPS22HB | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| LQFP100 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| LQFP144 | чипи/модулі | 09-H7-Deep | ✅ `mqtt.org`, `www.st.com` |
| LQFP48 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| LQFP64 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| LSM6DSL | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| MAX7219 | вивід/актуатори | 07-Indikatsiya-MAX7219 | ✅ `www.analog.com`, `www.seeedstudio.com` |
| MAX98357 | вивід/актуатори | 08-Audio-DFPlayer | ✅ `www.ti.com` |
| MC60 | модулі зв'язку | 03-GPS-GSM | ✅ `www.quectel.com`, `www.simcom.com`, `www.u-blox.com` |
| MCP3208 | шини | 02-SPI | ✅ `www.st.com`, `www.winbond.com` |
| MCP4725 | чипи/модулі, аналог | 02-F3-F4, 02-DAC | ✅ `www.st.com` |
| ME6211 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| ME6211A18 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| MFRC522 | сенсори | 09-RFID-RC522 | ✅ `www.nxp.com` |
| MODE0 | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| MODE1 | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| MP1584 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| MP34DT01 | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| MPU6050 | шини, сенсори, проєкти | 03-I2C, 01-DHT11-DS18B20, 02-BME280-SHT3x, 03-MPU6050-IMU +7 | ✅ `ams-osram.com`, `invensense.tdk.com`, `learn.adafruit.com` |
| MQ135 | сенсори | 10-MQ-Gas | ✅ `www.winsen-sensor.com` |
| MS5611 | сенсори | 06-Pressure-BMP-MS | ✅ `www.bosch-sensortec.com`, `www.te.com` |
| NAMESTM32BLE | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| NRF24 | шини, радіо, модулі зв'язку, проєкти | 02-SPI, 02-LoRaWAN-WL, 04-LoRa-P2P, 01-NRF24-LoRa +4 | ✅ `lora-alliance.org`, `www.bluetooth.com`, `www.bosch-sensortec.com` |
| OV7670 | модулі зв'язку | 08-DCMI-Camera | ✅ `www.st.com`, `www.waveshare.com` |
| OVER16 | шини | 01-UART | ✅ `www.st.com` |
| OVER8 | шини | 01-UART | ✅ `www.st.com` |
| PA10 | чипи/модулі, gpio, вивід/актуатори, модулі зв'язку, додатки | 01-F0-F1-Classic, 02-AF-maping, 08-Audio-DFPlayer, 09-FOC-BLDC +2 | ✅ `docs.espressif.com`, `mqtt.org`, `www.espressif.com` |
| PA11 | протоколи | 05-CANopen | ✅ `www.st.com` |
| PA12 | протоколи | 05-CANopen | ✅ `www.st.com` |
| PA13 | gpio, прошивка, додатки | 02-AF-maping, 03-ST-Link-Proshivka, 05-Pinout-Quickref | ✅ `www.st.com` |
| PA14 | gpio, прошивка, додатки | 02-AF-maping, 03-ST-Link-Proshivka, 05-Pinout-Quickref | ✅ `www.st.com` |
| PA15 | gpio, вивід/актуатори | 02-AF-maping, 09-FOC-BLDC | ✅ `www.st.com` |
| PB10 | gpio, додатки | 02-AF-maping, 05-Pinout-Quickref | ✅ `www.st.com` |
| PB11 | gpio, модулі зв'язку, додатки | 02-AF-maping, 09-LWIP-Ethernet, 05-Pinout-Quickref | ✅ `docs.wiznet.io`, `www.st.com` |
| PB12 | модулі зв'язку | 07-BLE-HC05-HM10, 09-LWIP-Ethernet | ✅ `docs.wiznet.io`, `www.bluetooth.com` |
| PB13 | вивід/актуатори, модулі зв'язку | 09-FOC-BLDC, 07-BLE-HC05-HM10, 09-LWIP-Ethernet | ✅ `docs.wiznet.io`, `www.bluetooth.com`, `www.st.com` |
| PB15 | вивід/актуатори | 09-FOC-BLDC | ✅ `www.st.com` |
| PC13 | старт, чипи/модулі, плати, протоколи, лабораторія | 04-Devkit-plati, 01-F0-F1-Classic, 01-Blue-Pill, 03-Nucleo +2 | ✅ `mqtt.org`, `www.st.com` |
| PC14 | додатки | 05-Pinout-Quickref | ✅ `www.st.com` |
| PC15 | чипи/модулі, додатки | 01-F0-F1-Classic, 05-Pinout-Quickref | ✅ `www.st.com` |
| PCM5102 | вивід/актуатори | 08-Audio-DFPlayer | ✅ `www.ti.com` |
| PM0214 | gpio | 04-NVIC-Priority-DeepDive | ✅ `www.st.com` |
| PM0223 | пам'ять | 01-Flash-OTP-EEPROM | ✅ `www.st.com` |
| PM10 | сенсори | 13-Yakist-Povitrya | ✅ `sensirion.com` |
| PMS5003 | сенсори | 13-Yakist-Povitrya | ✅ `sensirion.com` |
| QFN32 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| QMC5883L | сенсори | 14-Mag-Gesture-RTC | ✅ `www.u-blox.com` |
| RC522 | сенсори, вивід/актуатори | 09-RFID-RC522, 08-Audio-DFPlayer | ✅ `www.nxp.com`, `www.ti.com` |
| RJ45 | модулі зв'язку | 04-W5500 | ✅ `docs.wiznet.io` |
| RM0008 | gpio, шини | 01-GPIO-rezhimi, 02-AF-maping, 01-UART, 02-SPI | ✅ `community.st.com`, `www.st.com`, `www.winbond.com` |
| RM0368 | gpio | 01-GPIO-rezhimi, 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| RM0444 | шини | 01-UART, 03-I2C | ✅ `www.nxp.com`, `www.st.com` |
| RPDO1 | протоколи | 05-CANopen | ✅ `www.st.com` |
| RS485 | старт, шини, модулі зв'язку, живлення/рівні, протоколи, проєкти, лабораторія | 02-Glosariy, 01-UART, 01-NRF24-LoRa, 02-RS485-CAN-Ethernet +8 | ✅ `docs.wiznet.io`, `mqtt.org`, `www.modbus.org` |
| RT9193 | старт | 04-Devkit-plati | ✅ `www.st.com` |
| SCD40 | сенсори | 07-CO2-SCD-MHZ, 10-MQ-Gas | ✅ `sensirion.com`, `www.winsen-sensor.com` |
| SGP40 | сенсори | 13-Yakist-Povitrya | ✅ `sensirion.com` |
| SHA256 | протоколи | 02-DFU-Bootloader | ✅ `www.st.com` |
| SHT30 | сенсори | 02-BME280-SHT3x | ✅ `sensirion.com`, `www.bosch-sensortec.com` |
| SIM7600 | модулі зв'язку, протоколи | 05-SIM7600, 04-MQTT | ✅ `mqtt.org`, `www.simcom.com` |
| SIM7600X | модулі зв'язку | 05-SIM7600 | ✅ `www.simcom.com` |
| SIM800 | модулі зв'язку | 03-GPS-GSM | ✅ `www.quectel.com`, `www.simcom.com`, `www.u-blox.com` |
| SMBJ5 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| SPS30 | сенсори | 13-Yakist-Povitrya | ✅ `sensirion.com` |
| SRAM4 | чипи/модулі | 09-H7-Deep | ✅ `mqtt.org`, `www.st.com` |
| SSD1306 | шини, вивід/актуатори | 03-I2C, 01-OLED-SSD1306, 02-TFT-LCD, 03-Servo-Rele-MOSFET-WS2812 +2 | ✅ `www.analog.com`, `www.nxp.com`, `www.seeedstudio.com` |
| SSD1675 | вивід/актуатори | 04-Epaper | ✅ `www.waveshare.com` |
| ST7735 | шини, вивід/актуатори | 02-SPI, 02-TFT-LCD | ✅ `www.st.com`, `www.winbond.com` |
| STBC02 | живлення | 02-Batareyne-zhivlennya | ✅ `www.st.com` |
| STM32 | старт, чипи/модулі, живлення, gpio, шини, аналог, таймери, прошивка, сенсори, вивід/актуатори, модулі зв'язку, живлення/рівні, плати, протоколи, проєкти, лабораторія, додатки | 01-Yak-koristuvatis-dovidnikom, 02-Glosariy, 03-Porivnyannya-chipiv, 05-Vibir-seredovischa +73 | ✅ `ams-osram.com`, `community.st.com`, `docs.espressif.com` |
| STM32BLE | модулі зв'язку | 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com` |
| STM32F0 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F030F4P6 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F051K8U6 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F072C8 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F072CBT6 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F1 | чипи/модулі, шини | 01-F0-F1-Classic, 01-UART, 02-SPI | ✅ `www.st.com`, `www.winbond.com` |
| STM32F103 | gpio, модулі зв'язку | 01-GPIO-rezhimi, 02-AF-maping, 06-WiFi-ESP-AT | ✅ `community.st.com`, `docs.espressif.com`, `mqtt.org` |
| STM32F103C8T6 | старт, чипи/модулі | 03-Porivnyannya-chipiv, 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F103RCT6 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F107VCT6 | чипи/модулі | 01-F0-F1-Classic | ✅ `www.st.com` |
| STM32F3 | чипи/модулі, аналог | 02-F3-F4, 01-ADC | ✅ `www.st.com` |
| STM32F303CCT6 | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F303K8T6 | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F303VC | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F373VCT6 | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F4 | чипи/модулі, живлення, gpio, вивід/актуатори, модулі зв'язку, протоколи, проєкти | 02-F3-F4, 09-H7-Deep, 10-U5-Deep, 03-Power-Design +9 | ✅ `mqtt.org`, `www.analog.com`, `www.olimex.com` |
| STM32F401 | gpio | 01-GPIO-rezhimi, 02-AF-maping, 03-EXTI-NVIC | ✅ `community.st.com`, `www.st.com` |
| STM32F401CCU6 | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F407 | чипи/модулі | 09-H7-Deep | ✅ `mqtt.org`, `www.st.com` |
| STM32F407VG | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F407VGT6 | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F411 | проєкти | 06-Drone-FC | ✅ `www.st.com`, `www.tdk.com` |
| STM32F429NIH6 | чипи/модулі | 02-F3-F4 | ✅ `www.st.com` |
| STM32F7 | чипи/модулі | 08-F7-Bridge | ✅ `www.st.com` |
| STM32F722ZET6 | чипи/модулі | 08-F7-Bridge | ✅ `www.st.com` |
| STM32F732VET6 | чипи/модулі | 08-F7-Bridge | ✅ `www.st.com` |
| STM32F746NG | чипи/модулі | 08-F7-Bridge | ✅ `www.st.com` |
| STM32F746NGH6 | чипи/модулі | 08-F7-Bridge | ✅ `www.st.com` |
| STM32F769NIH6 | чипи/модулі | 08-F7-Bridge | ✅ `www.st.com` |
| STM32G0 | чипи/модулі, gpio, шини | 03-G0-G4, 03-EXTI-NVIC, 01-UART, 03-I2C | ✅ `community.st.com`, `www.nxp.com`, `www.st.com` |
| STM32G030F6 | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32G030F6P6 | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32G070 | gpio | 02-AF-maping | ✅ `www.st.com` |
| STM32G070KBT6 | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32G0B1CET6 | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32G4 | чипи/модулі, шини, аналог, сенсори | 03-G0-G4, 04-FDCAN, 01-ADC, 02-DAC +2 | ✅ `www.st.com`, `www.ti.com` |
| STM32G431KB | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32G431KBT6 | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32G474RET6 | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32G491KCT6 | чипи/модулі | 03-G0-G4 | ✅ `www.st.com` |
| STM32H5 | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32H563ZI | чипи/модулі, протоколи | 04-H5-H7, 03-Bezpeka | ✅ `www.st.com` |
| STM32H563ZIT6 | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32H573RIT6 | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32H7 | чипи/модулі | 04-H5-H7, 09-H7-Deep | ✅ `mqtt.org`, `www.st.com` |
| STM32H743 | чипи/модулі | 09-H7-Deep | ✅ `mqtt.org`, `www.st.com` |
| STM32H743ZI | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32H743ZIT6 | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32H745BIT6 | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32H750VBT6 | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32H7A3VIT6 | чипи/модулі | 04-H5-H7 | ✅ `www.st.com` |
| STM32L0 | живлення, проєкти | 02-Batareyne-zhivlennya, 01-Meteostantsiya | ✅ `www.bosch-sensortec.com`, `www.st.com` |
| STM32L031K6T6 | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| STM32L072CZT6 | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| STM32L4 | аналог, проєкти | 04-DFSDM, 01-Meteostantsiya, 02-GPS-treker | ✅ `www.bosch-sensortec.com`, `www.st.com` |
| STM32L431RCT6 | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| STM32L452RE | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| STM32L452RET6 | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| STM32L475VG | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| STM32L552ZET6 | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| STM32U5 | чипи/модулі | 10-U5-Deep | ✅ `mqtt.org`, `www.st.com` |
| STM32U585AI | чипи/модулі, протоколи | 05-L0-L4-U5, 03-Bezpeka | ✅ `www.st.com` |
| STM32U585AIT6 | чипи/модулі | 05-L0-L4-U5 | ✅ `www.st.com` |
| STM32WB | радіо, модулі зв'язку | 01-BLE-WB, 07-BLE-HC05-HM10 | ✅ `www.bluetooth.com`, `www.st.com` |
| STM32WB55 | чипи/модулі, радіо | 06-WB-WL, 01-BLE-WB | ✅ `www.bluetooth.com`, `www.st.com` |
| STM32WB55CEU5 | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| STM32WB55CG | чипи/модулі, протоколи | 06-WB-WL, 02-DFU-Bootloader | ✅ `www.st.com` |
| STM32WB55CGU6 | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| STM32WB5MMGH6 | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| STM32WL | радіо | 02-LoRaWAN-WL | ✅ `lora-alliance.org`, `www.st.com` |
| STM32WL55 | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| STM32WL55JC | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| STM32WL55JC56 | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| STM32WLE5CCU6 | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| SX1276 | модулі зв'язку | 01-NRF24-LoRa | ✅ `www.nordicsemi.com`, `www.semtech.com` |
| SY8113 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| TJA1021 | шини | 08-LIN-SMBus-I3C | ✅ `findchips.com` |
| TJA1050 | протоколи | 05-CANopen | ✅ `www.st.com` |
| TJA1051 | шини | 04-FDCAN | ✅ `www.st.com` |
| TJA1441 | шини | 04-FDCAN | ✅ `www.st.com` |
| TM1637 | вивід/актуатори | 07-Indikatsiya-MAX7219 | ✅ `www.analog.com`, `www.seeedstudio.com` |
| TMC2209 | вивід/актуатори | 06-Stepper-TMC | ✅ `www.analog.com`, `www.st.com` |
| TMC2209STEPPERTN | вивід/актуатори | 06-Stepper-TMC | ✅ `www.analog.com`, `www.st.com` |
| TMC2300 | вивід/актуатори | 06-Stepper-TMC | ✅ `www.analog.com`, `www.st.com` |
| TMC2300STEPPERTN | вивід/актуатори | 06-Stepper-TMC | ✅ `www.analog.com`, `www.st.com` |
| TP4056 | живлення, живлення/рівні | 02-Batareyne-zhivlennya, 03-Charger-Protect | ✅ `www.ic-fortune.com`, `www.st.com` |
| TPDO1 | протоколи | 05-CANopen | ✅ `www.st.com` |
| TPS25750 | живлення | 04-USB-C-PD | ✅ `mqtt.org`, `www.st.com`, `www.ti.com` |
| TSL2591 | сенсори | 08-Light-BH-TSL | ✅ `ams-osram.com`, `www.rohm.com` |
| TSSOP20 | чипи/модулі | 01-F0-F1-Classic, 03-G0-G4 | ✅ `www.st.com` |
| TXB0104 | живлення/рівні | 02-Level-Shift | ✅ `www.nxp.com`, `www.ti.com` |
| TXB0108 | живлення/рівні | 02-Level-Shift | ✅ `www.nxp.com`, `www.ti.com` |
| TXS0108 | живлення/рівні | 02-Level-Shift | ✅ `www.nxp.com`, `www.ti.com` |
| UM10204 | шини | 03-I2C | ✅ `www.nxp.com`, `www.st.com` |
| UM1075 | прошивка | 03-ST-Link-Proshivka | ✅ `www.st.com` |
| UM1718 | прошивка | 01-CubeIDE-CubeMX | ✅ `www.st.com` |
| UM1905 | прошивка | 02-HAL-LL, 05-Shablon-Drayvera | ✅ `www.st.com` |
| UM2237 | пам'ять, прошивка | 02-Zovnishni-Loadery, 03-ST-Link-Proshivka | ✅ `www.st.com` |
| UM2305 | живлення | 02-Batareyne-zhivlennya | ✅ `www.st.com` |
| USART1 | gpio | 02-AF-maping | ✅ `www.st.com` |
| USART2 | gpio | 02-AF-maping | ✅ `www.st.com` |
| USBLC6 | живлення | 03-Power-Design | ✅ `www.olimex.com`, `www.st.com` |
| VDD11 | старт | 02-Glosariy, 03-Porivnyannya-chipiv | ✅ `www.st.com` |
| VL53L0X | сенсори, плати | 05-HC-SR04-VL53L0X, 06-IoT-Discovery | ✅ `learn.adafruit.com`, `www.st.com` |
| VOS0 | чипи/модулі | 09-H7-Deep | ✅ `mqtt.org`, `www.st.com` |
| VOS3 | чипи/модулі | 09-H7-Deep | ✅ `mqtt.org`, `www.st.com` |
| WB55 | старт, чипи/модулі, радіо | 03-Porivnyannya-chipiv, 06-WB-WL, 01-BLE-WB | ✅ `www.bluetooth.com`, `www.st.com` |
| WB55CG | протоколи | 02-DFU-Bootloader | ✅ `www.st.com` |
| WIZNET5K | модулі зв'язку | 09-LWIP-Ethernet | ✅ `docs.wiznet.io` |
| WL55 | чипи/модулі | 06-WB-WL | ✅ `www.st.com` |
| WPA2 | плати | 06-IoT-Discovery | ✅ `www.st.com` |
| WS2812 | сенсори, вивід/актуатори | 11-Encoder, 01-OLED-SSD1306, 02-TFT-LCD, 03-Servo-Rele-MOSFET-WS2812 +1 | ✅ `ams-osram.com`, `www.st.com`, `www.ti.com` |
| WS2812B | вивід/актуатори | 03-Servo-Rele-MOSFET-WS2812 | ✅ `www.st.com` |
| XPT2046 | вивід/актуатори | 02-TFT-LCD, 05-LVGL | ✅ `www.st.com` |
| XT30 | проєкти | 06-Drone-FC | ✅ `www.st.com`, `www.tdk.com` |
| XT60 | проєкти | 06-Drone-FC | ✅ `www.st.com`, `www.tdk.com` |
