# Реєстр компонентів ARDUINO-Reference

> Згенеровано 2026-10-07: `python3 scripts/comp_inventory.py --registry COMPONENTS.md`. НЕ редагувати вручну — перегенерувати!
>
> ✅ = хоча б в одній ноті-згадці є посилання виробника. Це НЕ гарантує, що лінк саме на цей компонент — звіряти вручну!
>
> ❌ = у жодній ноті-згадці немає виробничих посилань. Пріоритетні кандидати на додавання даташитів.

**Позначень:** 96; **з datasheet:** 96; **без:** 0.

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
| ACS712 | сенсори | 10-Strum-INA219 | ✅ `docs.arduino.cc`, `www.ti.com` |
| AMS1117 | живлення | 01-Zhivlennya-VIN | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| BH1750 | сенсори | 09-Svitlo-Tisk-ToF | ✅ `www.st.com` |
| BH1750FVI | сенсори | 09-Svitlo-Tisk-ToF | ✅ `www.st.com` |
| BME280 | сенсори, живлення/рівні, проєкти | 01-DHT-DS18B20, 02-BME280, 03-HC-SR04-PIR, 04-LM35-NTC +6 | ✅ `docs.arduino.cc`, `invensense.tdk.com`, `www.analog.com` |
| BME680 | сенсори | 11-CO2-Povitrya | ✅ `docs.arduino.cc`, `www.winsen-sensor.com` |
| BMP280 | сенсори | 09-Svitlo-Tisk-ToF | ✅ `www.st.com` |
| COMF10 | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| COMF11 | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| CP2102 | старт, чипи/модулі, шини, додатки | 04-Devkit-plati, 05-Nano33-BLE-ARM, 04-USB-AVR, 03-Diagnostic-Map | ✅ `docs.arduino.cc`, `docs.nordicsemi.com`, `playground.arduino.cc` |
| CR2032 | сенсори | 12-Mag-Gesture-RTC | ✅ `www.u-blox.com` |
| DFR0299 | вивід/актуатори | 06-Indikatsiya-Audio | ✅ `www.analog.com`, `www.seeedstudio.com` |
| DHT11 | сенсори | 01-DHT-DS18B20 | ✅ `docs.arduino.cc`, `www.analog.com`, `www.arduino.cc` |
| DS18B20 | сенсори, проєкти | 01-DHT-DS18B20, 02-BME280, 03-HC-SR04-PIR, 04-LM35-NTC +1 | ✅ `docs.arduino.cc`, `www.analog.com`, `www.arduino.cc` |
| DS3231 | сенсори | 12-Mag-Gesture-RTC | ✅ `www.u-blox.com` |
| DW01 | живлення, живлення/рівні | 02-Batareyki, 02-Level-Shift-TP4056 | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| ESP32 | чипи/модулі, плати, протоколи | 04-Uno-R4, 05-Nano33-BLE-ARM, 03-Nano-ESP32-GIGA, 03-HTTP-Web | ✅ `docs.arduino.cc`, `docs.nordicsemi.com`, `mqtt.org` |
| ESP8266 | модулі зв'язку, протоколи | 03-ESP8266-WiFi, 04-GPS-NEO, 05-BT-Ethernet, 03-HTTP-Web | ✅ `docs.arduino.cc`, `docs.espressif.com`, `mqtt.org` |
| FAT32 | вивід/актуатори | 06-Indikatsiya-Audio, 08-Nextion-HMI | ✅ `docs.arduino.cc`, `www.analog.com`, `www.seeedstudio.com` |
| HD44780 | вивід/актуатори | 01-LCD1602 | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| ICNT1 | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| ICP1 | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| ICR1 | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| ILI9341 | вивід/актуатори | 07-TFT-Touch-Deep | ✅ `docs.arduino.cc` |
| ILI9488 | вивід/актуатори | 07-TFT-Touch-Deep | ✅ `docs.arduino.cc` |
| INA219 | сенсори | 10-Strum-INA219 | ✅ `docs.arduino.cc`, `www.ti.com` |
| LCD1602 | вивід/актуатори | 01-LCD1602, 02-OLED-SSD1306, 03-NeoPixel-Servo-Rele, 06-Indikatsiya-Audio | ✅ `docs.arduino.cc`, `www.analog.com`, `www.arduino.cc` |
| LM2596 | живлення/рівні | 01-Buck-peretvoryuvach | ✅ `docs.arduino.cc`, `www.ti.com` |
| LM35 | сенсори, вивід/актуатори | 01-DHT-DS18B20, 02-BME280, 03-HC-SR04-PIR, 04-LM35-NTC +2 | ✅ `docs.arduino.cc`, `www.analog.com`, `www.arduino.cc` |
| LOG00001 | пам'ять | 02-SD-FatFS-Deep | ✅ `docs.arduino.cc` |
| MAX7219 | вивід/актуатори | 06-Indikatsiya-Audio | ✅ `www.analog.com`, `www.seeedstudio.com` |
| MCP4725 | аналог | 02-DAC-nema | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| MCP4728 | аналог | 02-DAC-nema | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| MFRC522 | сенсори, модулі зв'язку | 07-RFID-RC522, 02-RC522-RFID | ✅ `docs.arduino.cc`, `www.arduino.cc`, `www.nxp.com` |
| MKR1000 | чипи/модулі | 05-Nano33-BLE-ARM | ✅ `docs.arduino.cc`, `docs.nordicsemi.com` |
| MP1584 | живлення/рівні | 01-Buck-peretvoryuvach | ✅ `docs.arduino.cc`, `www.ti.com` |
| MPU6050 | сенсори | 05-MPU6050, 06-MQ-Gas, 07-RFID-RC522, 08-Encoder +1 | ✅ `docs.arduino.cc`, `invensense.tdk.com`, `www.arduino.cc` |
| MQ135 | сенсори | 06-MQ-Gas | ✅ `docs.arduino.cc`, `www.arduino.cc`, `www.renesas.com` |
| MQ136 | сенсори | 06-MQ-Gas | ✅ `docs.arduino.cc`, `www.arduino.cc`, `www.renesas.com` |
| NRF24 | радіо, модулі зв'язку, живлення/рівні, плати | 01-LoRa-moduli, 02-RC522-RFID, 03-ESP8266-WiFi, 04-GPS-NEO +3 | ✅ `docs.arduino.cc`, `docs.espressif.com`, `www.arduino.cc` |
| NRF24L01 | модулі зв'язку | 01-NRF24 | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| NX8048T070 | вивід/актуатори | 08-Nextion-HMI | ✅ `docs.arduino.cc` |
| OC0A | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OC0B | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OC1A | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OC1B | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OC2A | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OC2B | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OCR1A | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OCR1B | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| OUT1 | вивід/актуатори | 05-Servo-Motor-L298N | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| OUT2 | вивід/актуатори | 05-Servo-Motor-L298N | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| OUT3 | вивід/актуатори | 05-Servo-Motor-L298N | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| OUT4 | вивід/актуатори | 05-Servo-Motor-L298N | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| PCF8574 | вивід/актуатори | 01-LCD1602 | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| PCF8591 | аналог | 02-DAC-nema | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| PT8211 | аналог | 02-DAC-nema | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| QMC5883L | сенсори | 12-Mag-Gesture-RTC | ✅ `www.u-blox.com` |
| RC522 | сенсори, модулі зв'язку | 07-RFID-RC522, 08-Encoder, 01-NRF24, 02-RC522-RFID | ✅ `docs.arduino.cc`, `www.arduino.cc`, `www.nxp.com` |
| RELAY1 | радіо | 03-GSM-Deep-HTTP | ✅ `docs.arduino.cc`, `www.simcom.com` |
| RF24 | модулі зв'язку | 01-NRF24 | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| RF95 | радіо | 01-LoRa-moduli | ✅ `www.semtech.com` |
| RFM95 | радіо | 01-LoRa-moduli | ✅ `www.semtech.com` |
| RFM96 | радіо | 01-LoRa-moduli | ✅ `www.semtech.com` |
| RS485 | шини | 01-UART | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| SAM3X8E | чипи/модулі | 03-Due-Zero-ARM | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| SAM3X8X | чипи/модулі | 05-Nano33-BLE-ARM | ✅ `docs.arduino.cc`, `docs.nordicsemi.com` |
| SAMD21 | чипи/модулі | 03-Due-Zero-ARM, 05-Nano33-BLE-ARM | ✅ `docs.arduino.cc`, `docs.nordicsemi.com`, `www.arduino.cc` |
| SAMW25 | чипи/модулі | 05-Nano33-BLE-ARM | ✅ `docs.arduino.cc`, `docs.nordicsemi.com` |
| SHA1 | протоколи | 03-HTTP-Web | ✅ `docs.arduino.cc`, `mqtt.org` |
| SIM7600 | радіо | 03-GSM-Deep-HTTP | ✅ `docs.arduino.cc`, `www.simcom.com` |
| SIM800 | чипи/модулі, радіо, проєкти | 05-Nano33-BLE-ARM, 01-LoRa-moduli, 02-GSM-SIM800, 03-GSM-Deep-HTTP +1 | ✅ `docs.arduino.cc`, `docs.nordicsemi.com`, `www.arduino.cc` |
| SIM800C | радіо | 02-GSM-SIM800, 03-GSM-Deep-HTTP | ✅ `docs.arduino.cc`, `www.simcom.com` |
| SIM800L | радіо | 02-GSM-SIM800 | ✅ `docs.arduino.cc` |
| SSD1306 | вивід/актуатори | 01-LCD1602, 02-OLED-SSD1306, 03-NeoPixel-Servo-Rele, 04-TFT-ST7735 +2 | ✅ `docs.arduino.cc`, `www.analog.com`, `www.arduino.cc` |
| ST7735 | вивід/актуатори | 04-TFT-ST7735, 05-Servo-Motor-L298N, 07-TFT-Touch-Deep, 08-Nextion-HMI | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| STM32 | модулі зв'язку, плати | 05-BT-Ethernet, 03-Nano-ESP32-GIGA | ✅ `docs.arduino.cc` |
| STM32H7 | плати | 03-Nano-ESP32-GIGA | ✅ `docs.arduino.cc` |
| STM32H743 | чипи/модулі | 05-Nano33-BLE-ARM | ✅ `docs.arduino.cc`, `docs.nordicsemi.com` |
| STM32H747 | плати | 03-Nano-ESP32-GIGA | ✅ `docs.arduino.cc` |
| SX1276 | радіо | 01-LoRa-moduli | ✅ `www.semtech.com` |
| SX1278 | радіо | 01-LoRa-moduli | ✅ `www.semtech.com` |
| TCCR1A | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| TCCR1B | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| TM1637 | вивід/актуатори | 06-Indikatsiya-Audio | ✅ `www.analog.com`, `www.seeedstudio.com` |
| TOV1F | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| TP4056 | пам'ять, живлення/рівні | 01-Pamyat-EEPROM, 01-Buck-peretvoryuvach, 02-Level-Shift-TP4056 | ✅ `docs.arduino.cc`, `www.ti.com` |
| TXB0108 | живлення/рівні | 02-Level-Shift-TP4056 | ✅ `docs.arduino.cc` |
| TXS0108 | живлення/рівні | 02-Level-Shift-TP4056 | ✅ `docs.arduino.cc` |
| UCS2 | радіо | 02-GSM-SIM800 | ✅ `docs.arduino.cc` |
| VL53L0X | сенсори | 09-Svitlo-Tisk-ToF | ✅ `www.st.com` |
| WGM12 | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| WGM13 | таймери | 03-Timeri-16bit-Deep | ✅ `docs.arduino.cc`, `ww1.microchip.com` |
| WS2812 | вивід/актуатори | 03-NeoPixel-Servo-Rele | ✅ `docs.arduino.cc`, `www.arduino.cc` |
| XL4015 | живлення/рівні | 01-Buck-peretvoryuvach | ✅ `docs.arduino.cc`, `www.ti.com` |
| XPT2046 | вивід/актуатори | 07-TFT-Touch-Deep | ✅ `docs.arduino.cc` |
