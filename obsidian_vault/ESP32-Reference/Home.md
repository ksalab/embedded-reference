---
title: ESP32 Reference - головна карта довідника
tags:

  - esp32
  - esp32/moc
  - esp32/start

aliases:

  - Home
  - ESP32 Довідник
  - MOC ESP32

type: MOC
date: 2026-10-08
---

# ESP32 Reference - головна карта довідника

EN version: `Home.en.md`

> [!tip] Навігація
> Це MOC всього довідника. Старт: [[UA/00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись]] → [[UA/00-Start/03-Porivnyannya-chipiv|Порівняння чипів]] → [[UA/00-Start/04-Devkit-plati|DevKit плати]] → [[UA/00-Start/05-Vibir-seredovischa|Вибір середовища]].

Довідник покриває ESP32 / S2 / S3 / C3 / C6 / H2: вибір чипа, живлення, GPIO, шини, радіо, сон, пам'ять, прошивка, сенсори, вивід, модулі зв'язку. Приклади скрізь у 3 стеках: ESP-IDF + Arduino + MicroPython. Вся логіка - **3.3V**.

> [!warning] Живлення 3.3V!
> ESP32 **не толерантний до 5V** на GPIO. Див. [[UA/03-GPIO/03-Pidtyaguvannya-rivni|Рівні 3.3V/5V]] та [[UA/13-Moduli-zhivlennya-rivniv/02-Level-Shifters|Level-shifters]].

## Маршрути читання

| Хто | Маршрут |
| --- | --- |
| Новачок | [[UA/00-Start/01-Yak-koristuvatis-dovidnikom]] → [[UA/00-Start/02-Glosariy| Глосарій]] → [[UA/00-Start/03-Porivnyannya-chipiv]] → [[UA/00-Start/04-Devkit-plati]] → [[UA/09-Proshivka/02-Arduino-PlatformIO]] → [[UA/03-GPIO/01-GPIO-oglyad]] → [[UA/04-Shini/03-I2C| I2C]] → [[UA/99-Dodatki/02-Troubleshooting-FAQ]] |
| Радіо / IoT | [[UA/05-Radio/01-WiFi-STA-AP]] → [[UA/05-Radio/02-BLE-Bluetooth]] → [[UA/05-Radio/03-ESP-NOW]] → [[UA/08-Pamyat/03-OTA| OTA]] → [[UA/07-Timeri-Son/03-Sleep-ULP| Sleep]] |
| Батарейний пристрій | [[UA/02-Zhivlennya/01-Lancjugi-zhivlennya]] → [[UA/02-Zhivlennya/03-Spozhivannya| Споживання]] → [[UA/07-Timeri-Son/03-Sleep-ULP| Sleep]] → [[UA/02-Zhivlennya/04-Akumulyatori-TP4056]] |
| Датчики / вивід | [[UA/10-Sensori/01-DHT11-DHT22| DHT11/DHT22]] → [[UA/10-Sensori/03-BME280-BMP280-SHT31]] → [[UA/11-Vivid/01-OLED-SSD1306]] → [[UA/11-Vivid/03-NeoPixel-Servo-Rele-MOSFET]] |

## Карта розділів

| Папка | Тема | Ключові ноти |
| --- | --- | --- |
| `UA/00-Start` | Старт | [[UA/00-Start/01-Yak-koristuvatis-dovidnikom]], [[UA/00-Start/02-Glosariy| Глосарій]], [[UA/00-Start/03-Porivnyannya-chipiv]], [[UA/00-Start/04-Devkit-plati]], [[UA/00-Start/05-Vibir-seredovischa]] |
| `UA/01-Hardware` | Чипи, флеш, boot, RF | [[UA/01-Hardware/01-ESP32-Classic]], [[UA/01-Hardware/02-ESP32-S2]], [[UA/01-Hardware/03-ESP32-S3]], [[UA/01-Hardware/04-ESP32-C3-C6-H2]], [[UA/01-Hardware/05-Moduli-WROOM-WROVER-MINI]], [[UA/01-Hardware/06-Flash-PSRAM]], [[UA/01-Hardware/07-Boot-Strapping-Reset]], [[UA/01-Hardware/08-Anteni-RF]], [[UA/01-Hardware/09-ESP32-C2-P4| C2/P4]], [[UA/01-Hardware/10-ESP32-C5-C61| C5/C61]], [[UA/01-Hardware/11-ESP32-C6-H2-Mesh| C6/H2-mesh]], [[UA/01-Hardware/12-ESP32-P4-Native| P4-нативно]] |
| `UA/02-Zhivlennya` | Живлення | [[UA/02-Zhivlennya/01-Lancjugi-zhivlennya]], [[UA/02-Zhivlennya/02-LDO-DC-DC]], [[UA/02-Zhivlennya/03-Spozhivannya| Споживання]], [[UA/02-Zhivlennya/04-Akumulyatori-TP4056]], [[UA/02-Zhivlennya/05-Fuel-Gauge]] |
| `UA/03-GPIO` | Піни | [[UA/03-GPIO/01-GPIO-oglyad]], [[UA/03-GPIO/02-Strapping-pini]], [[UA/03-GPIO/03-Pidtyaguvannya-rivni]], [[UA/03-GPIO/04-Pererivannya-PWM]], [[UA/03-GPIO/05-RTC-GPIO]] |
| `UA/04-Shini` | Шини | [[UA/04-Shini/01-UART| UART]], [[UA/04-Shini/02-SPI| SPI]], [[UA/04-Shini/03-I2C| I2C]], [[UA/04-Shini/04-I2S| I2S]], [[UA/04-Shini/05-CAN-TWAI-RS485]], [[UA/04-Shini/06-USB-OTG-JTAG]], [[UA/04-Shini/07-SD-SDIO]] |
| `UA/05-Radio` | Радіо (7 нот) | [[UA/05-Radio/01-WiFi-STA-AP]], [[UA/05-Radio/02-BLE-Bluetooth]], [[UA/05-Radio/03-ESP-NOW]], [[UA/05-Radio/04-ESP-MESH]], [[UA/05-Radio/05-BLE-Mesh-A2DP-HID| Mesh/A2DP]], [[UA/05-Radio/06-BLE-Gateway-Tracker| BLE-шлюз]], [[UA/05-Radio/07-BLE5-LongRange-Audio| BLE5]] |
| `UA/06-Analog` | Аналог | [[UA/06-Analog/01-ADC| ADC]], [[UA/06-Analog/02-DAC-Touch-Hall]], [[UA/06-Analog/03-PID-Filters| ПІД/Фільтри]] |
| `UA/07-Timeri-Son` | Таймери, сон | [[UA/07-Timeri-Son/01-Timeri-MCPWM-PCNT-RMT| Таймери/MCPWM/RMT]], [[UA/07-Timeri-Son/02-WDT| WDT]], [[UA/07-Timeri-Son/03-Sleep-ULP| Sleep/ULP]], [[UA/07-Timeri-Son/04-TPL5110| TPL5110]] |
| `UA/08-Pamyat` | Пам'ять | [[UA/08-Pamyat/01-Partitions-NVS]], [[UA/08-Pamyat/02-Filesystem| Файлові системи]], [[UA/08-Pamyat/03-OTA| OTA]], [[UA/08-Pamyat/04-Secure-Boot-Encrypt]] |
| `UA/09-Proshivka` | Прошивка (8 нот) | [[UA/09-Proshivka/01-ESP-IDF-setup]], [[UA/09-Proshivka/02-Arduino-PlatformIO]], [[UA/09-Proshivka/03-MicroPython| MicroPython]], [[UA/09-Proshivka/04-Esptool-Flash]], [[UA/09-Proshivka/05-JTAG-Debug]], [[UA/09-Proshivka/06-FreeRTOS-Patterns| FreeRTOS]], [[UA/09-Proshivka/07-Testing-CI| Тести/CI]], [[UA/09-Proshivka/08-Tooling-Deep| Туулінг]] |
| `UA/10-Sensori` | Сенсори (40 нот) | [[UA/10-Sensori/01-DHT11-DHT22| DHT]], [[UA/10-Sensori/02-DS18B20| DS18B20]], [[UA/10-Sensori/03-BME280-BMP280-SHT31| BME280]], [[UA/10-Sensori/04-MPU6050| MPU6050]], [[UA/10-Sensori/05-HC-SR04-PIR| HC-SR04/PIR]], [[UA/10-Sensori/06-INA219-HX711-BH1750| INA219/HX711]], [[UA/10-Sensori/07-AHT10-AHT20-SHT40| AHT/SHT40]], [[UA/10-Sensori/08-BME680-CCS811-MHZ19-PMS5003| Повітря/CO2/Пил]], [[UA/10-Sensori/09-ADS1115-MCP3008-PCF8574-MCP23017| ADS/Expander]], [[UA/10-Sensori/10-VL53L0X-TCS34725-TSL2561| ToF/Колір]], [[UA/10-Sensori/11-NTC-PT100-MAX6675-LM35| Темп-аналог]], [[UA/10-Sensori/12-MQ2-MQ7-MQ135-Flame-Sound| Гази]], [[UA/10-Sensori/13-RCWL0516-Reed-Vibration-Tilt-Flow| Охорона/Рідини]], [[UA/10-Sensori/14-DS3231-Encoder-Keypad-Joystick| RTC/HMI]], [[UA/10-Sensori/15-ACS712-ZMPT101B-PZEM-AS5600-FSR| Струм/Сила]], [[UA/10-Sensori/16-HMC5883-BNO055-RFID-RC522-Barcode| Компас/9-DOF]], [[UA/10-Sensori/17-Gas-CO2-Precision| Гази/CO2]], [[UA/10-Sensori/18-Light-Spectral-Gesture| Світло/Спектр]], [[UA/10-Sensori/19-IMU-6-9DOF| IMU]], [[UA/10-Sensori/20-Bio-IR-Temp| Біо/ІЧ]], [[UA/10-Sensori/21-Energy-Meters| Лічильники]], [[UA/10-Sensori/22-Gas-2-VOC-Industrial| Гази-2]], [[UA/10-Sensori/23-Dust-CO2-2| Пил/CO2-2]], [[UA/10-Sensori/24-Pressure-Level-Flow| Тиск/Рівень]], [[UA/10-Sensori/25-Mag-IMU-2| Магніт/IMU-2]], [[UA/10-Sensori/26-Light-UV-IRArray-ToF| УФ/Тепло/ToF]], [[UA/10-Sensori/27-Time-Mem-IO-DAC| Час/Пам'ять/IO]], [[UA/10-Sensori/33-Input-IO-2| Ввід/IO-2]], [[UA/10-Sensori/28-Env-NewGen| Клімат-new]], [[UA/10-Sensori/29-Range-Lidar-60GHz| Радар/Лідар]], [[UA/10-Sensori/30-Temp-Precision| Термопари]], [[UA/10-Sensori/31-IMU-Mag-3| IMU-3]], [[UA/10-Sensori/32-Light-Color-2| Світло-2]], [[UA/10-Sensori/34-Buttons-Switches-Pots| Кнопки]], [[UA/10-Sensori/35-Tails| Хвости]], [[UA/10-Sensori/36-Agro| Агро]], [[UA/10-Sensori/37-Bio-2| Біо-2]], [[UA/10-Sensori/38-Industrial-Sensors| Промсенсори]], [[UA/10-Sensori/39-Wireless-Sensors| Бездротові]], [[UA/10-Sensori/40-Thermal-MLX90640| Тепловізор]] |
| `UA/11-Vivid` | Вивід (20 нот) | [[UA/11-Vivid/01-OLED-SSD1306| OLED]], [[UA/11-Vivid/02-TFT-LCD-Epaper| TFT/LCD]], [[UA/11-Vivid/03-NeoPixel-Servo-Rele-MOSFET| NeoPixel/Серво/Реле]], [[UA/11-Vivid/04-L298N-TB6612-A4988-Buzzer| Драйвери]], [[UA/11-Vivid/05-MAX7219-TM1637-74HC595| MAX7219/7-seg]], [[UA/11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209| PCA9685/Сервоприводи]], [[UA/11-Vivid/07-BTS7960-L9110S-SSR-Solenoid| BTS7960/SSR]], [[UA/11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004| Звук/HMI]], [[UA/11-Vivid/09-LED-Strip-Power-SK6812-APA102| Стрічки/Живлення]], [[UA/11-Vivid/10-Displays-2| Дисплеї-2]], [[UA/11-Vivid/11-PowerMotion-2| Потужність/Рух]], [[UA/11-Vivid/12-LVGL-SquareLine| LVGL]], [[UA/11-Vivid/13-Audio-Codecs| Аудіо]], [[UA/11-Vivid/14-Displays-3| Дисплеї-3]], [[UA/11-Vivid/15-EInk| E-Ink]], [[UA/11-Vivid/16-LCD-Char| LCD]], [[UA/11-Vivid/17-Touchscreens| Тач]], [[UA/11-Vivid/18-MP3-TTS-Amps| MP3/TTS]], [[UA/11-Vivid/19-WebRadio-Streaming| Вебрадіо]], [[UA/11-Vivid/20-LVGL-Widgets-Deep| LVGL-віджети]] |
| `UA/12-Moduli-zvyazku` | Зв'язок (33 нот) | [[UA/12-Moduli-zvyazku/01-RC522-RFID| RC522]], [[UA/12-Moduli-zvyazku/02-NRF24-LoRa| NRF24/LoRa]], [[UA/12-Moduli-zvyazku/03-SIM800L-GPS| SIM800L/GPS]], [[UA/12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera| RS485/CAN/Cam]], [[UA/12-Moduli-zvyazku/05-PN532-RDM6300-Fingerprint-GM65| NFC/Біометрія]], [[UA/12-Moduli-zvyazku/06-HC05-HM10-CC1101-HC12| BT/Sub-GHz]], [[UA/12-Moduli-zvyazku/07-SIM7600-W5500-MCP2515| 4G/Ethernet/CAN]], [[UA/12-Moduli-zvyazku/08-LD2410-UWB-IR-Voice| Радар/UWB]], [[UA/12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa| Cellular/LoRa-UART]], [[UA/12-Moduli-zvyazku/10-Industrial| Промисловість]], [[UA/12-Moduli-zvyazku/11-TinyML-Voice| TinyML/Голос]], [[UA/12-Moduli-zvyazku/12-RC-Protocols| RC]], [[UA/12-Moduli-zvyazku/13-Camera-Streaming| Стримінг]], [[UA/12-Moduli-zvyazku/14-Proximity-Inputs| Промвходи]], [[UA/12-Moduli-zvyazku/15-RFID-Advanced| RFID-deep]], [[UA/12-Moduli-zvyazku/16-Offline-Voice| Офлайн-голос]], [[UA/12-Moduli-zvyazku/17-GNSS-RTK| RTK]], [[UA/12-Moduli-zvyazku/18-Cellular-LoRa-2| Cat-1/LoRa-2]], [[UA/12-Moduli-zvyazku/19-Wired-2| Дротові-2]], [[UA/12-Moduli-zvyazku/20-NFC-Biometry-2| NFC-2]], [[UA/12-Moduli-zvyazku/21-Motion-Control| Рух]], [[UA/12-Moduli-zvyazku/22-Automotive| Авто]], [[UA/12-Moduli-zvyazku/23-Marine-Time| Море/Час]], [[UA/12-Moduli-zvyazku/24-DIY-Instruments| DIY-прилади]], [[UA/12-Moduli-zvyazku/25-Secure-Elements]], [[UA/12-Moduli-zvyazku/26-SIM-Power| SIM+Живлення]], [[UA/12-Moduli-zvyazku/27-LPWAN-Alt| LPWAN-Alt]], [[UA/12-Moduli-zvyazku/28-UWB-2| UWB-2]], [[UA/12-Moduli-zvyazku/29-LoRaWAN-Gateway| LoRaWAN-шлюз]], [[UA/12-Moduli-zvyazku/30-USB-Host| USB-хост]], [[UA/12-Moduli-zvyazku/31-Ethernet-PoE-Deep| Ethernet-PoE]], [[UA/12-Moduli-zvyazku/32-USB-UVC-Host-Deep| USB-UVC]], [[UA/12-Moduli-zvyazku/29-LoRaWAN-Gateway-Deep| Шлюз-deep]] |
| `UA/13-Moduli-zhivlennya-rivniv` | Живлення модулі (8 нот) | [[UA/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar| Buck/Solar]], [[UA/13-Moduli-zhivlennya-rivniv/02-Level-Shifters| Level-shifters]], [[UA/13-Moduli-zhivlennya-rivniv/03-TP4056-IP5306-BMS-UPS| Заряд/BMS/UPS]], [[UA/13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect| XL4015/Захист]], [[UA/13-Moduli-zhivlennya-rivniv/05-USB-UART-AutoReset| USB-UART]], [[UA/13-Moduli-zhivlennya-rivniv/07-Stencil-Reflow| Stencil/Reflow]], [[UA/13-Moduli-zhivlennya-rivniv/08-Conformal-Coating| Лак/Компаунд]], [[UA/13-Moduli-zhivlennya-rivniv/09-USB-PD| USB-PD]] |
| `UA/14-Devboards` | Плати (17 нот) | [[UA/14-Devboards/01-DOIT-DevKitV1-NodeMCU32S| DOIT DevKitV1]], [[UA/14-Devboards/02-Wemos-D1-R32]], [[UA/14-Devboards/03-LILYGO-TDisplay-TBeam| LILYGO T-Display/T-Beam]], [[UA/14-Devboards/04-Heltec-WiFi-LoRa32| Heltec LoRa32]], [[UA/14-Devboards/05-ESP32-CAM| ESP32-CAM]], [[UA/14-Devboards/06-M5Stack-Core-Stick| M5Stack]], [[UA/14-Devboards/07-Feather-Huzzah32-Thing| Feather/Thing]], [[UA/14-Devboards/08-S3-DevKitC-C3-SuperMini-XIAO| S3/C3/XIAO]], [[UA/14-Devboards/09-WT32-ETH01-Olimex| WT32/Olimex]], [[UA/14-Devboards/10-Mini-Boards| Міні]], [[UA/14-Devboards/11-HMI-Boards| HMI]], [[UA/14-Devboards/12-Retro-Wearable| Ретро]], [[UA/14-Devboards/13-ESP32C6-Boards| C6-плати]], [[UA/14-Devboards/14-ESP32H2-Boards| H2-плати]], [[UA/14-Devboards/15-Nano-ESP32| Nano]], [[UA/14-Devboards/16-P4-DevKit| P4-плата]], [[UA/14-Devboards/17-C5-DevKit| C5-плата]] |
| `UA/15-Protokoli` | Протоколи (16 нот) | [[UA/15-Protokoli/01-MQTT| MQTT]], [[UA/15-Protokoli/02-HTTP-WebSocket| HTTP/WebSocket]], [[UA/15-Protokoli/03-mDNS-NTP-TLS| mDNS/NTP/TLS]], [[UA/15-Protokoli/04-Provisioning| Provisioning]], [[UA/15-Protokoli/05-Cloud-Pipeline| Cloud]], [[UA/15-Protokoli/06-Firmwares| WLED/Tasmota]], [[UA/15-Protokoli/07-Notify-Voice| Сповіщення]], [[UA/15-Protokoli/08-Security-Hardening| Безпека]], [[UA/15-Protokoli/09-Matter-Thread-Zigbee| Matter]], [[UA/15-Protokoli/10-Voice-Assistant| Голос]], [[UA/15-Protokoli/11-Cloud-2| MQTT-клієнт]], [[UA/15-Protokoli/12-AWS-IoT| AWS]], [[UA/15-Protokoli/13-Azure-IoT| Azure]], [[UA/15-Protokoli/14-MQTT-SN| MQTT-SN]], [[UA/15-Protokoli/15-Cloud-Platforms| Хмарні платформи]], [[UA/15-Protokoli/16-Matter-Thread-Deep| Matter-deep]] |
| `UA/16-Proekti` | Проєкти (7 нот) | [[UA/16-Proekti/01-Weather-Station| Метеостанція]], [[UA/16-Proekti/02-GPS-Tracker| GPS-трекер]], [[UA/16-Proekti/03-Access-Control| Контроль доступу]], [[UA/16-Proekti/04-Energy-Monitor| Енергомонітор]], [[UA/16-Proekti/05-TinyML-Deep-Practice| TinyML-deep]], [[UA/16-Proekti/06-C5-C61-Robotics| C5/C61-робот]], [[UA/16-Proekti/07-Edge-AI-Vision| AI-зір]] |
| `UA/17-Lab` | Лабораторія (5 нот) | [[UA/17-Lab/01-Instruments| Прилади]], [[UA/17-Lab/02-Soldering-Connectors| Пайка/Конектори]], [[UA/17-Lab/03-Enclosure-Cert-Factory| Корпус/Завод]], [[UA/17-Lab/04-PCB-Design| PCB]], [[UA/17-Lab/05-Breadboard-Mezhi| Макетка]] |
| `UA/99-Dodatki` | Додатки | [[UA/99-Dodatki/01-Pinout-tablici| Pinout]], [[UA/99-Dodatki/02-Troubleshooting-FAQ| FAQ]], [[UA/99-Dodatki/03-Cheklisti-montazhu| Чек-листи]], [[UA/99-Dodatki/04-Datasheet-Links| Datasheets]], [[UA/99-Dodatki/05-Official-Sources-Sensors| Джерела: сенсори]], [[UA/99-Dodatki/06-Official-Sources-Modules| Джерела: модулі]], [[UA/99-Dodatki/07-Versions| Версії]], [[UA/99-Dodatki/08-Diagnostic-Map| Карта]] |

## Теги та граф

| Тег | Призначення |
| --- | --- |
| `#esp32/gpio` | Піни, режими, переривання |
| `#esp32/adc` | Аналогові вимірювання |
| `#esp32/wifi` | STA/AP, сканування |
| `#esp32/ota` | Оновлення по повітрю |
| `#esp32/power` | Живлення, LDO, deep-sleep |
| `#esp32/sensor` | Датчики за шаблоном |

> [!tip] Граф
> Graph View → фільтр `path:ESP32-Reference`. MOC зв'язує всі розділи, `## Див. також` у кожній ноті утворює щільну сітку.
>
> [!example] Схема: живлення DevKit від USB
> Місце під фото: `assets/img/devkit-usb-power.png` - див. [[assets/README|Як додавати картинки]].

| ESP32 DevKit | ПК / Модуль | Примітка |
| --- | --- | --- |
| 5V (VIN) | USB 5V | Живлення плати, далі LDO → 3.3V, див. [[UA/02-Zhivlennya/01-Lancjugi-zhivlennya]] |
| GND | GND USB | Спільна земля обов'язкова |
| TX0 (GPIO1) | RX USB-UART | 3.3V логіка |
| RX0 (GPIO3) | TX USB-UART | Без 5V! Див. [[UA/03-GPIO/03-Pidtyaguvannya-rivni]] |
| EN + BOOT | Кнопки | Download-режим, див. [[UA/01-Hardware/07-Boot-Strapping-Reset]] |

## Див. також

- [[UA/00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись]]
- [[UA/00-Start/03-Porivnyannya-chipiv|Порівняння чипів]]
- [[UA/03-GPIO/01-GPIO-oglyad|GPIO огляд]]
- [[UA/04-Shini/01-UART|UART]]
- [[UA/05-Radio/01-WiFi-STA-AP|WiFi]]
- [[UA/06-Analog/01-ADC|ADC]]
- [[UA/08-Pamyat/03-OTA|OTA]]
- [[UA/09-Proshivka/04-Esptool-Flash|Esptool]]
- [[UA/99-Dodatki/02-Troubleshooting-FAQ|FAQ]]
- [[UA/99-Dodatki/05-Official-Sources-Sensors|Офіційні джерела: сенсори]]
- [[UA/99-Dodatki/06-Official-Sources-Modules|Офіційні джерела: модулі]]
- [[scripts/README|Скрипти обслуговування бази]]
