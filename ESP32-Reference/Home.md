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
---

# ESP32 Reference - головна карта довідника

EN version: `Home.en.md`

> [!tip] Навігація
> Це MOC всього довідника. Старт: [[00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись]] → [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]] → [[00-Start/04-Devkit-plati|DevKit плати]] → [[00-Start/05-Vibir-seredovischa|Вибір середовища]].

Довідник покриває ESP32 / S2 / S3 / C3 / C6 / H2: вибір чипа, живлення, GPIO, шини, радіо, сон, пам'ять, прошивка, сенсори, вивід, модулі зв'язку. Приклади скрізь у 3 стеках: ESP-IDF + Arduino + MicroPython. Вся логіка - **3.3V**.

> [!warning] Живлення 3.3V!
> ESP32 **не толерантний до 5V** на GPIO. Див. [[03-GPIO/03-Pidtyaguvannya-rivni|Рівні 3.3V/5V]] та [[13-Moduli-zhivlennya-rivniv/02-Level-Shifters|Level-shifters]].

## Маршрути читання

| Хто | Маршрут |
| --- | --- |
| Новачок | [[00-Start/01-Yak-koristuvatis-dovidnikom]] → [[00-Start/02-Glosariy | Глосарій]] → [[00-Start/03-Porivnyannya-chipiv]] → [[00-Start/04-Devkit-plati]] → [[09-Proshivka/02-Arduino-PlatformIO]] → [[03-GPIO/01-GPIO-oglyad]] → [[04-Shini/03-I2C | I2C]] → [[99-Dodatki/02-Troubleshooting-FAQ]] |
| Радіо / IoT | [[05-Radio/01-WiFi-STA-AP]] → [[05-Radio/02-BLE-Bluetooth]] → [[05-Radio/03-ESP-NOW]] → [[08-Pamyat/03-OTA | OTA]] → [[07-Timeri-Son/03-Sleep-ULP | Sleep]] |
| Батарейний пристрій | [[02-Zhivlennya/01-Lancjugi-zhivlennya]] → [[02-Zhivlennya/03-Spozhivannya | Споживання]] → [[07-Timeri-Son/03-Sleep-ULP | Sleep]] → [[02-Zhivlennya/04-Akumulyatori-TP4056]] |
| Датчики / вивід | [[10-Sensori/01-DHT11-DHT22 | DHT11/DHT22]] → [[10-Sensori/03-BME280-BMP280-SHT31]] → [[11-Vivid/01-OLED-SSD1306]] → [[11-Vivid/03-NeoPixel-Servo-Rele-MOSFET]] |

## Карта розділів

| Папка | Тема | Ключові ноти |
| --- | --- | --- |
| `00-Start` | Старт | [[00-Start/01-Yak-koristuvatis-dovidnikom]], [[00-Start/02-Glosariy | Глосарій]], [[00-Start/03-Porivnyannya-chipiv]], [[00-Start/04-Devkit-plati]], [[00-Start/05-Vibir-seredovischa]] |
| `01-Hardware` | Чипи, флеш, boot, RF | [[01-Hardware/01-ESP32-Classic]], [[01-Hardware/02-ESP32-S2]], [[01-Hardware/03-ESP32-S3]], [[01-Hardware/04-ESP32-C3-C6-H2]], [[01-Hardware/05-Moduli-WROOM-WROVER-MINI]], [[01-Hardware/06-Flash-PSRAM]], [[01-Hardware/07-Boot-Strapping-Reset]], [[01-Hardware/08-Anteni-RF]], [[01-Hardware/09-ESP32-C2-P4 | C2/P4]], [[01-Hardware/10-ESP32-C5-C61 | C5/C61]], [[01-Hardware/11-ESP32-C6-H2-Mesh | C6/H2-mesh]], [[01-Hardware/12-ESP32-P4-Native | P4-нативно]] |
| `02-Zhivlennya` | Живлення | [[02-Zhivlennya/01-Lancjugi-zhivlennya]], [[02-Zhivlennya/02-LDO-DC-DC]], [[02-Zhivlennya/03-Spozhivannya | Споживання]], [[02-Zhivlennya/04-Akumulyatori-TP4056]], [[02-Zhivlennya/05-Fuel-Gauge]] |
| `03-GPIO` | Піни | [[03-GPIO/01-GPIO-oglyad]], [[03-GPIO/02-Strapping-pini]], [[03-GPIO/03-Pidtyaguvannya-rivni]], [[03-GPIO/04-Pererivannya-PWM]], [[03-GPIO/05-RTC-GPIO]] |
| `04-Shini` | Шини | [[04-Shini/01-UART | UART]], [[04-Shini/02-SPI | SPI]], [[04-Shini/03-I2C | I2C]], [[04-Shini/04-I2S | I2S]], [[04-Shini/05-CAN-TWAI-RS485]], [[04-Shini/06-USB-OTG-JTAG]], [[04-Shini/07-SD-SDIO]] |
| `05-Radio` | Радіо (7 нот) | [[05-Radio/01-WiFi-STA-AP]], [[05-Radio/02-BLE-Bluetooth]], [[05-Radio/03-ESP-NOW]], [[05-Radio/04-ESP-MESH]], [[05-Radio/05-BLE-Mesh-A2DP-HID | Mesh/A2DP]], [[05-Radio/06-BLE-Gateway-Tracker | BLE-шлюз]], [[05-Radio/07-BLE5-LongRange-Audio | BLE5]] |
| `06-Analog` | Аналог | [[06-Analog/01-ADC | ADC]], [[06-Analog/02-DAC-Touch-Hall]], [[06-Analog/03-PID-Filters | ПІД/Фільтри]] |
| `07-Timeri-Son` | Таймери, сон | [[07-Timeri-Son/01-Timeri-MCPWM-PCNT-RMT | Таймери/MCPWM/RMT]], [[07-Timeri-Son/02-WDT | WDT]], [[07-Timeri-Son/03-Sleep-ULP | Sleep/ULP]], [[07-Timeri-Son/04-TPL5110 | TPL5110]] |
| `08-Pamyat` | Пам'ять | [[08-Pamyat/01-Partitions-NVS]], [[08-Pamyat/02-Filesystem | Файлові системи]], [[08-Pamyat/03-OTA | OTA]], [[08-Pamyat/04-Secure-Boot-Encrypt]] |
| `09-Proshivka` | Прошивка (8 нот) | [[09-Proshivka/01-ESP-IDF-setup]], [[09-Proshivka/02-Arduino-PlatformIO]], [[09-Proshivka/03-MicroPython | MicroPython]], [[09-Proshivka/04-Esptool-Flash]], [[09-Proshivka/05-JTAG-Debug]], [[09-Proshivka/06-FreeRTOS-Patterns | FreeRTOS]], [[09-Proshivka/07-Testing-CI | Тести/CI]], [[09-Proshivka/08-Tooling-Deep | Туулінг]] |
| `10-Sensori` | Сенсори (40 нот) | [[10-Sensori/01-DHT11-DHT22 | DHT]], [[10-Sensori/02-DS18B20 | DS18B20]], [[10-Sensori/03-BME280-BMP280-SHT31 | BME280]], [[10-Sensori/04-MPU6050 | MPU6050]], [[10-Sensori/05-HC-SR04-PIR | HC-SR04/PIR]], [[10-Sensori/06-INA219-HX711-BH1750 | INA219/HX711]], [[10-Sensori/07-AHT10-AHT20-SHT40 | AHT/SHT40]], [[10-Sensori/08-BME680-CCS811-MHZ19-PMS5003 | Повітря/CO2/Пил]], [[10-Sensori/09-ADS1115-MCP3008-PCF8574-MCP23017 | ADS/Expander]], [[10-Sensori/10-VL53L0X-TCS34725-TSL2561 | ToF/Колір]], [[10-Sensori/11-NTC-PT100-MAX6675-LM35 | Темп-аналог]], [[10-Sensori/12-MQ2-MQ7-MQ135-Flame-Sound | Гази]], [[10-Sensori/13-RCWL0516-Reed-Vibration-Tilt-Flow | Охорона/Рідини]], [[10-Sensori/14-DS3231-Encoder-Keypad-Joystick | RTC/HMI]], [[10-Sensori/15-ACS712-ZMPT101B-PZEM-AS5600-FSR | Струм/Сила]], [[10-Sensori/16-HMC5883-BNO055-RFID-RC522-Barcode | Компас/9-DOF]], [[10-Sensori/17-Gas-CO2-Precision | Гази/CO2]], [[10-Sensori/18-Light-Spectral-Gesture | Світло/Спектр]], [[10-Sensori/19-IMU-6-9DOF | IMU]], [[10-Sensori/20-Bio-IR-Temp | Біо/ІЧ]], [[10-Sensori/21-Energy-Meters | Лічильники]], [[10-Sensori/22-Gas-2-VOC-Industrial | Гази-2]], [[10-Sensori/23-Dust-CO2-2 | Пил/CO2-2]], [[10-Sensori/24-Pressure-Level-Flow | Тиск/Рівень]], [[10-Sensori/25-Mag-IMU-2 | Магніт/IMU-2]], [[10-Sensori/26-Light-UV-IRArray-ToF | УФ/Тепло/ToF]], [[10-Sensori/27-Time-Mem-IO-DAC | Час/Пам'ять/IO]], [[10-Sensori/33-Input-IO-2 | Ввід/IO-2]], [[10-Sensori/28-Env-NewGen | Клімат-new]], [[10-Sensori/29-Range-Lidar-60GHz | Радар/Лідар]], [[10-Sensori/30-Temp-Precision | Термопари]], [[10-Sensori/31-IMU-Mag-3 | IMU-3]], [[10-Sensori/32-Light-Color-2 | Світло-2]], [[10-Sensori/34-Buttons-Switches-Pots | Кнопки]], [[10-Sensori/35-Tails | Хвости]], [[10-Sensori/36-Agro | Агро]], [[10-Sensori/37-Bio-2 | Біо-2]], [[10-Sensori/38-Industrial-Sensors | Промсенсори]], [[10-Sensori/39-Wireless-Sensors | Бездротові]], [[10-Sensori/40-Thermal-MLX90640 | Тепловізор]] |
| `11-Vivid` | Вивід (20 нот) | [[11-Vivid/01-OLED-SSD1306 | OLED]], [[11-Vivid/02-TFT-LCD-Epaper | TFT/LCD]], [[11-Vivid/03-NeoPixel-Servo-Rele-MOSFET | NeoPixel/Серво/Реле]], [[11-Vivid/04-L298N-TB6612-A4988-Buzzer | Драйвери]], [[11-Vivid/05-MAX7219-TM1637-74HC595 | MAX7219/7-seg]], [[11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209 | PCA9685/Сервоприводи]], [[11-Vivid/07-BTS7960-L9110S-SSR-Solenoid | BTS7960/SSR]], [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004 | Звук/HMI]], [[11-Vivid/09-LED-Strip-Power-SK6812-APA102 | Стрічки/Живлення]], [[11-Vivid/10-Displays-2 | Дисплеї-2]], [[11-Vivid/11-PowerMotion-2 | Потужність/Рух]], [[11-Vivid/12-LVGL-SquareLine | LVGL]], [[11-Vivid/13-Audio-Codecs | Аудіо]], [[11-Vivid/14-Displays-3 | Дисплеї-3]], [[11-Vivid/15-EInk | E-Ink]], [[11-Vivid/16-LCD-Char | LCD]], [[11-Vivid/17-Touchscreens | Тач]], [[11-Vivid/18-MP3-TTS-Amps | MP3/TTS]], [[11-Vivid/19-WebRadio-Streaming | Вебрадіо]], [[11-Vivid/20-LVGL-Widgets-Deep | LVGL-віджети]] |
| `12-Moduli-zvyazku` | Зв'язок (33 нот) | [[12-Moduli-zvyazku/01-RC522-RFID | RC522]], [[12-Moduli-zvyazku/02-NRF24-LoRa | NRF24/LoRa]], [[12-Moduli-zvyazku/03-SIM800L-GPS | SIM800L/GPS]], [[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera | RS485/CAN/Cam]], [[12-Moduli-zvyazku/05-PN532-RDM6300-Fingerprint-GM65 | NFC/Біометрія]], [[12-Moduli-zvyazku/06-HC05-HM10-CC1101-HC12 | BT/Sub-GHz]], [[12-Moduli-zvyazku/07-SIM7600-W5500-MCP2515 | 4G/Ethernet/CAN]], [[12-Moduli-zvyazku/08-LD2410-UWB-IR-Voice | Радар/UWB]], [[12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa | Cellular/LoRa-UART]], [[12-Moduli-zvyazku/10-Industrial | Промисловість]], [[12-Moduli-zvyazku/11-TinyML-Voice | TinyML/Голос]], [[12-Moduli-zvyazku/12-RC-Protocols | RC]], [[12-Moduli-zvyazku/13-Camera-Streaming | Стримінг]], [[12-Moduli-zvyazku/14-Proximity-Inputs | Промвходи]], [[12-Moduli-zvyazku/15-RFID-Advanced | RFID-deep]], [[12-Moduli-zvyazku/16-Offline-Voice | Офлайн-голос]], [[12-Moduli-zvyazku/17-GNSS-RTK | RTK]], [[12-Moduli-zvyazku/18-Cellular-LoRa-2 | Cat-1/LoRa-2]], [[12-Moduli-zvyazku/19-Wired-2 | Дротові-2]], [[12-Moduli-zvyazku/20-NFC-Biometry-2 | NFC-2]], [[12-Moduli-zvyazku/21-Motion-Control | Рух]], [[12-Moduli-zvyazku/22-Automotive | Авто]], [[12-Moduli-zvyazku/23-Marine-Time | Море/Час]], [[12-Moduli-zvyazku/24-DIY-Instruments | DIY-прилади]], [[12-Moduli-zvyazku/25-Secure-Elements]], [[12-Moduli-zvyazku/26-SIM-Power | SIM+Живлення]], [[12-Moduli-zvyazku/27-LPWAN-Alt | LPWAN-Alt]], [[12-Moduli-zvyazku/28-UWB-2 | UWB-2]], [[12-Moduli-zvyazku/29-LoRaWAN-Gateway | LoRaWAN-шлюз]], [[12-Moduli-zvyazku/30-USB-Host | USB-хост]], [[12-Moduli-zvyazku/31-Ethernet-PoE-Deep | Ethernet-PoE]], [[12-Moduli-zvyazku/32-USB-UVC-Host-Deep | USB-UVC]], [[12-Moduli-zvyazku/29-LoRaWAN-Gateway-Deep | Шлюз-deep]] |
| `13-Moduli-zhivlennya-rivniv` | Живлення модулі (8 нот) | [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar | Buck/Solar]], [[13-Moduli-zhivlennya-rivniv/02-Level-Shifters | Level-shifters]], [[13-Moduli-zhivlennya-rivniv/03-TP4056-IP5306-BMS-UPS | Заряд/BMS/UPS]], [[13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect | XL4015/Захист]], [[13-Moduli-zhivlennya-rivniv/05-USB-UART-AutoReset | USB-UART]], [[13-Moduli-zhivlennya-rivniv/07-Stencil-Reflow | Stencil/Reflow]], [[13-Moduli-zhivlennya-rivniv/08-Conformal-Coating | Лак/Компаунд]], [[13-Moduli-zhivlennya-rivniv/09-USB-PD | USB-PD]] |
| `14-Devboards` | Плати (17 нот) | [[14-Devboards/01-DOIT-DevKitV1-NodeMCU32S | DOIT DevKitV1]], [[14-Devboards/02-Wemos-D1-R32]], [[14-Devboards/03-LILYGO-TDisplay-TBeam | LILYGO T-Display/T-Beam]], [[14-Devboards/04-Heltec-WiFi-LoRa32 | Heltec LoRa32]], [[14-Devboards/05-ESP32-CAM | ESP32-CAM]], [[14-Devboards/06-M5Stack-Core-Stick | M5Stack]], [[14-Devboards/07-Feather-Huzzah32-Thing | Feather/Thing]], [[14-Devboards/08-S3-DevKitC-C3-SuperMini-XIAO | S3/C3/XIAO]], [[14-Devboards/09-WT32-ETH01-Olimex | WT32/Olimex]], [[14-Devboards/10-Mini-Boards | Міні]], [[14-Devboards/11-HMI-Boards | HMI]], [[14-Devboards/12-Retro-Wearable | Ретро]], [[14-Devboards/13-ESP32C6-Boards | C6-плати]], [[14-Devboards/14-ESP32H2-Boards | H2-плати]], [[14-Devboards/15-Nano-ESP32 | Nano]], [[14-Devboards/16-P4-DevKit | P4-плата]], [[14-Devboards/17-C5-DevKit | C5-плата]] |
| `15-Protokoli` | Протоколи (16 нот) | [[15-Protokoli/01-MQTT | MQTT]], [[15-Protokoli/02-HTTP-WebSocket | HTTP/WebSocket]], [[15-Protokoli/03-mDNS-NTP-TLS | mDNS/NTP/TLS]], [[15-Protokoli/04-Provisioning | Provisioning]], [[15-Protokoli/05-Cloud-Pipeline | Cloud]], [[15-Protokoli/06-Firmwares | WLED/Tasmota]], [[15-Protokoli/07-Notify-Voice | Сповіщення]], [[15-Protokoli/08-Security-Hardening | Безпека]], [[15-Protokoli/09-Matter-Thread-Zigbee | Matter]], [[15-Protokoli/10-Voice-Assistant | Голос]], [[15-Protokoli/11-Cloud-2 | MQTT-клієнт]], [[15-Protokoli/12-AWS-IoT | AWS]], [[15-Protokoli/13-Azure-IoT | Azure]], [[15-Protokoli/14-MQTT-SN | MQTT-SN]], [[15-Protokoli/15-Cloud-Platforms | Хмарні платформи]], [[15-Protokoli/16-Matter-Thread-Deep | Matter-deep]] |
| `16-Proekti` | Проєкти (7 нот) | [[16-Proekti/01-Weather-Station | Метеостанція]], [[16-Proekti/02-GPS-Tracker | GPS-трекер]], [[16-Proekti/03-Access-Control | Контроль доступу]], [[16-Proekti/04-Energy-Monitor | Енергомонітор]], [[16-Proekti/05-TinyML-Deep-Practice | TinyML-deep]], [[16-Proekti/06-C5-C61-Robotics | C5/C61-робот]], [[16-Proekti/07-Edge-AI-Vision | AI-зір]] |
| `17-Lab` | Лабораторія (5 нот) | [[17-Lab/01-Instruments | Прилади]], [[17-Lab/02-Soldering-Connectors | Пайка/Конектори]], [[17-Lab/03-Enclosure-Cert-Factory | Корпус/Завод]], [[17-Lab/04-PCB-Design | PCB]], [[17-Lab/05-Breadboard-Mezhi | Макетка]] |
| `99-Dodatki` | Додатки | [[99-Dodatki/01-Pinout-tablici | Pinout]], [[99-Dodatki/02-Troubleshooting-FAQ | FAQ]], [[99-Dodatki/03-Cheklisti-montazhu | Чек-листи]], [[99-Dodatki/04-Datasheet-Links | Datasheets]], [[99-Dodatki/05-Official-Sources-Sensors | Джерела: сенсори]], [[99-Dodatki/06-Official-Sources-Modules | Джерела: модулі]], [[99-Dodatki/07-Versions | Версії]], [[99-Dodatki/08-Diagnostic-Map | Карта]] |

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
| 5V (VIN) | USB 5V | Живлення плати, далі LDO → 3.3V, див. [[02-Zhivlennya/01-Lancjugi-zhivlennya]] |
| GND | GND USB | Спільна земля обов'язкова |
| TX0 (GPIO1) | RX USB-UART | 3.3V логіка |
| RX0 (GPIO3) | TX USB-UART | Без 5V! Див. [[03-GPIO/03-Pidtyaguvannya-rivni]] |
| EN + BOOT | Кнопки | Download-режим, див. [[01-Hardware/07-Boot-Strapping-Reset]] |

## Див. також

- [[00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись]]
- [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]]
- [[03-GPIO/01-GPIO-oglyad|GPIO огляд]]
- [[04-Shini/01-UART|UART]]
- [[05-Radio/01-WiFi-STA-AP|WiFi]]
- [[06-Analog/01-ADC|ADC]]
- [[08-Pamyat/03-OTA|OTA]]
- [[09-Proshivka/04-Esptool-Flash|Esptool]]
- [[99-Dodatki/02-Troubleshooting-FAQ|FAQ]]
- [[99-Dodatki/05-Official-Sources-Sensors|Офіційні джерела: сенсори]]
- [[99-Dodatki/06-Official-Sources-Modules|Офіційні джерела: модулі]]
- [[scripts/README|Скрипти обслуговування бази]]
