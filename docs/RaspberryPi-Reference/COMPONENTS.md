# Реєстр компонентів RaspberryPi-Reference

> Згенеровано 2026-10-07: `python3 scripts/comp_inventory.py --registry COMPONENTS.md`. НЕ редагувати вручну — перегенерувати!
>
> ✅ = хоча б в одній ноті-згадці є посилання виробника. Це НЕ гарантує, що лінк саме на цей компонент — звіряти вручну!
>
> ❌ = у жодній ноті-згадці немає виробничих посилань. Пріоритетні кандидати на додавання даташитів.

**Позначень:** 74; **з datasheet:** 74; **без:** 0.

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
| ADS1115 | аналог, проєкти, додатки | 01-ADC-Zovnishnye, 01-Meteostantsiya, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| ARM1176 | чипи/модулі | 01-SoC-Oglyad | ✅ `www.raspberrypi.com` |
| BCM17 | чипи/модулі | 01-SoC-Oglyad | ✅ `www.raspberrypi.com` |
| BCM2711 | старт, чипи/модулі, плати | 03-Porivnyannya-plate, 01-SoC-Oglyad, 02-Pi4-Robocha | ✅ `datasheets.raspberrypi.com`, `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| BCM2712 | старт, чипи/модулі, живлення, плати | 02-Glosariy, 03-Porivnyannya-plate, 01-SoC-Oglyad, 02-BCM2712-Pi5 +2 | ✅ `datasheets.raspberrypi.com`, `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| BCM2835 | чипи/модулі | 01-SoC-Oglyad | ✅ `www.raspberrypi.com` |
| BCM2836 | чипи/модулі | 01-SoC-Oglyad | ✅ `www.raspberrypi.com` |
| BH1750FVI | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| BME280 | старт, шини, сенсори, модулі зв'язку, плати, протоколи, проєкти, додатки | 01-Yak-koristuvatis-dovidnikom, 01-I2C-SPI-UART, 01-BME280-Klimat, 02-MPU6050-Rukh +7 | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| BSS138 | живлення/рівні | 02-Level-Shift-3V3 | ✅ `gpiozero.readthedocs.io`, `www.ti.com`, `www.waveshare.com` |
| CAM0 | сенсори | 06-Kamera-CSI | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| CAM1 | сенсори | 06-Kamera-CSI | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| CYW43 | чипи/модулі, плати | 03-RP2040-RP2350, 03-Pico-W-Family | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| CYW43439 | чипи/модулі, плати | 03-RP2040-RP2350, 03-Pico-W-Family | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| DF40 | плати | 05-CM4-CM5 | ✅ `www.raspberrypi.com` |
| DHT22 | живлення/рівні | 02-Level-Shift-3V3 | ✅ `gpiozero.readthedocs.io`, `www.ti.com`, `www.waveshare.com` |
| DS18B20 | сенсори, модулі зв'язку, проєкти, додатки | 03-DS18B20-Temp, 01-Sense-HAT, 01-Meteostantsiya, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| DS3231 | чипи/модулі, таймери, додатки | 01-SoC-Oglyad, 01-Taimeri-Son, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| DSO138 | шини | 02-Logic-Analyzer | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| ESP32 | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| FAT32 | пам'ять | 01-SD-eMMC-NVMe | ✅ `www.raspberrypi.com` |
| HDMI0 | старт, вивід/актуатори, плати | 02-Glosariy, 01-DSI-HDMI-Displeyi, 01-Pi5-Flagman, 02-Pi4-Robocha | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| HDMI1 | старт | 02-Glosariy | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| HTS221 | модулі зв'язку | 01-Sense-HAT | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| IMX477 | сенсори | 06-Kamera-CSI | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| IMX500 | старт, сенсори | 04-Devkit-plati, 06-Kamera-CSI | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| IMX708 | сенсори | 06-Kamera-CSI | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| INA219 | аналог, сенсори, живлення/рівні, додатки | 01-ADC-Zovnishnye, 04-INA219-Strum, 01-Buck-Boost-DC-DC, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| INA226 | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| IP65 | проєкти | 01-Meteostantsiya | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| LM2596 | живлення/рівні, додатки | 01-Buck-Boost-DC-DC, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| LPDDR2 | чипи/модулі, плати | 01-SoC-Oglyad, 04-Zero-2W | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| LPDDR4 | чипи/модулі, плати | 01-SoC-Oglyad, 02-Pi4-Robocha | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| LPDDR4X | чипи/модулі | 01-SoC-Oglyad, 02-BCM2712-Pi5 | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| LPS25H | модулі зв'язку | 01-Sense-HAT | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| LSM9DS1 | модулі зв'язку | 01-Sense-HAT | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| MAX3485 | модулі зв'язку | 03-CAN-RS485-HAT | ✅ `www.microchip.com`, `www.u-blox.com`, `www.waveshare.com` |
| MAX7219 | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| MAX98357A | вивід/актуатори, додатки | 03-Audio-HAT, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| MCP2515 | модулі зв'язку | 03-CAN-RS485-HAT | ✅ `www.microchip.com`, `www.u-blox.com`, `www.waveshare.com` |
| MCP3008 | аналог | 01-ADC-Zovnishnye | ✅ `www.raspberrypi.com`, `www.ti.com` |
| MG996R | вивід/актуатори | 02-NeoPixel-Servo-Rele | ✅ `gpiozero.readthedocs.io`, `learn.adafruit.com`, `www.raspberrypi.com` |
| MLX90640 | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| MPU6050 | сенсори, модулі зв'язку | 02-MPU6050-Rukh, 05-GPS-NEO, 01-Sense-HAT | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com`, `www.u-blox.com` |
| MT3608 | живлення/рівні | 01-Buck-Boost-DC-DC | ✅ `www.raspberrypi.com`, `www.ti.com`, `www.waveshare.com` |
| PCA9685 | gpio, вивід/актуатори | 02-PWM-Pererivannya, 02-NeoPixel-Servo-Rele | ✅ `gpiozero.readthedocs.io`, `learn.adafruit.com`, `www.raspberrypi.com` |
| PCF8523 | таймери | 01-Taimeri-Son | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| PCM5102 | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| QMC5883L | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| RP2040 | старт, чипи/модулі, аналог, плати, додатки | 02-Glosariy, 03-Porivnyannya-plate, 05-Vibir-seredovischa, 01-SoC-Oglyad +4 | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| RP2350 | старт, чипи/модулі, аналог, плати, додатки | 02-Glosariy, 03-Porivnyannya-plate, 04-Devkit-plati, 01-SoC-Oglyad +4 | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| RP3A0 | старт, плати | 03-Porivnyannya-plate, 04-Zero-2W | ✅ `datasheets.raspberrypi.com`, `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| RS485 | чипи/модулі, шини, модулі зв'язку | 02-BCM2712-Pi5, 01-I2C-SPI-UART, 03-CAN-RS485-HAT | ✅ `gpiozero.readthedocs.io`, `www.microchip.com`, `www.raspberrypi.com` |
| SG90 | вивід/актуатори | 02-NeoPixel-Servo-Rele | ✅ `gpiozero.readthedocs.io`, `learn.adafruit.com`, `www.raspberrypi.com` |
| SIM800L | проєкти | 02-GPS-Treker | ✅ `www.raspberrypi.com`, `www.u-blox.com`, `www.waveshare.com` |
| SPS30 | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| SX1262 | модулі зв'язку | 02-GPS-LoRa-HAT | ✅ `www.raspberrypi.com`, `www.u-blox.com`, `www.waveshare.com` |
| SX1268 | модулі зв'язку, проєкти | 02-GPS-LoRa-HAT, 02-GPS-Treker | ✅ `www.raspberrypi.com`, `www.u-blox.com`, `www.waveshare.com` |
| SX1276 | модулі зв'язку | 02-GPS-LoRa-HAT | ✅ `www.raspberrypi.com`, `www.u-blox.com`, `www.waveshare.com` |
| SX1302 | модулі зв'язку | 02-GPS-LoRa-HAT | ✅ `www.raspberrypi.com`, `www.u-blox.com`, `www.waveshare.com` |
| TB6612 | проєкти | 03-Robot-Vizok | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| TB6612FNG | проєкти, додатки | 03-Robot-Vizok, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| TCA9548A | сенсори | 01-BME280-Klimat | ✅ `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
| TJA1050 | модулі зв'язку | 03-CAN-RS485-HAT | ✅ `www.microchip.com`, `www.u-blox.com`, `www.waveshare.com` |
| TL431 | чипи/модулі, аналог | 03-RP2040-RP2350, 01-ADC-Zovnishnye | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com`, `www.ti.com` |
| TM1637 | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| TP4056 | чипи/модулі, плати | 03-RP2040-RP2350, 03-Pico-W-Family | ✅ `datasheets.raspberrypi.com`, `www.raspberrypi.com` |
| TXS0108E | живлення/рівні, додатки | 02-Level-Shift-3V3, 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| UAC1 | вивід/актуатори | 03-Audio-HAT | ✅ `www.raspberrypi.com` |
| UAC2 | вивід/актуатори | 03-Audio-HAT | ✅ `www.raspberrypi.com` |
| VL53L0X | додатки | 02-Datasheet-Links | ✅ `datasheets.raspberrypi.com`, `docs.arduino.cc`, `docs.espressif.com` |
| WPA2 | радіо | 01-WiFi-BT-Bort | ✅ `www.raspberrypi.com` |
| WPA3 | радіо | 01-WiFi-BT-Bort | ✅ `www.raspberrypi.com` |
| WS2812 | чипи/модулі, живлення/рівні, плати | 03-RP2040-RP2350, 02-Level-Shift-3V3, 03-Pico-W-Family | ✅ `datasheets.raspberrypi.com`, `gpiozero.readthedocs.io`, `www.raspberrypi.com` |
