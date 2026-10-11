---
title: ESP32 Reference - reference home map
description: Entry map of the ESP32 reference covering chip choice, power, GPIO, buses, radio, sleep, memory, firmware, sensors, outputs and comms modules; shows schematics, code and tables.
tags:

  - esp32
  - esp32/moc
  - esp32/start

aliases:

  - Home
  - ESP32 Reference
  - ESP32 MOC

type: MOC
lang: en
original: Home.md
date-created: 2026-10-08
date: 2026-10-08
---

# ESP32 Reference - reference home map

> [!tip] Navigation
> This is the MOC of the whole reference. Start: [[EN/00-Start/01-How-to-Use-Guide.en| How to use it]] → [[EN/00-Start/03-Chip-Comparison.en| Chip comparison]] → [[EN/00-Start/04-Dev-Boards.en| DevKit boards]] → [[EN/00-Start/05-Environment-Choice.en| Environment choice]].

The reference covers ESP32 / S2 / S3 / C3 / C6 / H2: chip choice, power, GPIO, buses, radio, sleep, memory, firmware, sensors, outputs, comms modules. Examples everywhere use 3 stacks: ESP-IDF + Arduino + MicroPython. All logic is **3.3V**.

> [!warning] 3.3V power!
> The ESP32 is **not 5V tolerant** on GPIO. See [[EN/03-GPIO/03-Pull-Ups-Levels.en| 3.3V/5V levels]] and [[EN/13-Power-Modules/02-Level-Shifters.en| Level-shifters]].

## Reading paths

| Who | Path |
| --- | --- |
| Newcomer | [[EN/00-Start/01-How-to-Use-Guide.en]] → [[EN/00-Start/02-Glossary.en| Glossary]] → [[EN/00-Start/03-Chip-Comparison.en]] → [[EN/00-Start/04-Dev-Boards.en]] → [[EN/09-Firmware/02-Arduino-PlatformIO.en]] → [[EN/03-GPIO/01-GPIO-Overview.en]] → [[EN/04-Interfaces/03-I2C.en| I2C]] → [[EN/99-Additions/02-Troubleshooting-FAQ.en]] |
| Radio / IoT | [[EN/05-Radio/01-WiFi-STA-AP.en]] → [[EN/05-Radio/02-BLE-Bluetooth.en]] → [[EN/05-Radio/03-ESP-NOW.en]] → [[EN/08-Memory/03-OTA.en| OTA]] → [[EN/07-Timers/03-Sleep-ULP.en| Sleep]] |
| Battery device | [[EN/02-Power-Supply/01-Power-Rails.en]] → [[EN/02-Power-Supply/03-Power-Consumption.en| Power consumption]] → [[EN/07-Timers/03-Sleep-ULP.en| Sleep]] → [[EN/02-Power-Supply/04-Batteries-TP4056.en]] |
| Sensors / outputs | [[EN/10-Sensors/01-DHT11-DHT22.en| DHT11/DHT22]] → [[EN/10-Sensors/03-BME280-BMP280-SHT31.en]] → [[EN/11-Vivid/01-OLED-SSD1306.en]] → [[EN/11-Vivid/03-NeoPixel-Servo-Rele-MOSFET.en]] |

## Section map

| Folder | Topic | Key notes |
| --- | --- | --- |
| `EN/00-Start` | Getting started | [[EN/00-Start/01-How-to-Use-Guide.en]], [[EN/00-Start/02-Glossary.en| Glossary]], [[EN/00-Start/03-Chip-Comparison.en]], [[EN/00-Start/04-Dev-Boards.en]], [[EN/00-Start/05-Environment-Choice.en]] |
| `EN/01-Hardware` | Chips, flash, boot, RF | [[EN/01-Hardware/01-ESP32-Classic.en]], [[EN/01-Hardware/02-ESP32-S2.en]], [[EN/01-Hardware/03-ESP32-S3.en]], [[EN/01-Hardware/04-ESP32-C3-C6-H2.en]], [[EN/01-Hardware/05-WROOM-WROVER-MINI-Modules.en]], [[EN/01-Hardware/06-Flash-PSRAM.en]], [[EN/01-Hardware/07-Boot-Strapping-Reset.en]], [[EN/01-Hardware/08-Antennas-RF.en]], [[EN/01-Hardware/09-ESP32-C2-P4.en| C2/P4]], [[EN/01-Hardware/10-ESP32-C5-C61.en| C5/C61]], [[EN/01-Hardware/11-ESP32-C6-H2-Mesh.en| C6/H2 mesh]], [[EN/01-Hardware/12-ESP32-P4-Native.en| Native P4]] |
| `EN/02-Power-Supply` | Power supply | [[EN/02-Power-Supply/01-Power-Rails.en]], [[EN/02-Power-Supply/02-LDO-DC-DC.en]], [[EN/02-Power-Supply/03-Power-Consumption.en| Power consumption]], [[EN/02-Power-Supply/04-Batteries-TP4056.en]], [[EN/02-Power-Supply/05-Fuel-Gauge.en]] |
| `EN/03-GPIO` | Pins | [[EN/03-GPIO/01-GPIO-Overview.en]], [[EN/03-GPIO/02-Strapping-Pins.en]], [[EN/03-GPIO/03-Pull-Ups-Levels.en]], [[EN/03-GPIO/04-Interrupts-PWM.en]], [[EN/03-GPIO/05-RTC-GPIO.en]] |
| `EN/04-Interfaces` | Buses | [[EN/04-Interfaces/01-UART.en| UART]], [[EN/04-Interfaces/02-SPI.en| SPI]], [[EN/04-Interfaces/03-I2C.en| I2C]], [[EN/04-Interfaces/04-I2S.en| I2S]], [[EN/04-Interfaces/05-CAN-TWAI-RS485.en]], [[EN/04-Interfaces/06-USB-OTG-JTAG.en]], [[EN/04-Interfaces/07-SD-SDIO.en]] |
| `EN/05-Radio` | Radio (7 notes) | [[EN/05-Radio/01-WiFi-STA-AP.en]], [[EN/05-Radio/02-BLE-Bluetooth.en]], [[EN/05-Radio/03-ESP-NOW.en]], [[EN/05-Radio/04-ESP-MESH.en]], [[EN/05-Radio/05-BLE-Mesh-A2DP-HID.en| Mesh/A2DP]], [[EN/05-Radio/06-BLE-Gateway-Tracker.en| BLE gateway]], [[EN/05-Radio/07-BLE5-LongRange-Audio.en| BLE5]] |
| `EN/06-Analog` | Analog | [[EN/06-Analog/01-ADC.en| ADC]], [[EN/06-Analog/02-DAC-Touch-Hall.en]], [[EN/06-Analog/03-PID-Filters.en| PID/Filters]] |
| `EN/07-Timers` | Timers, sleep | [[EN/07-Timers/01-Timers-MCPWM-PCNT-RMT.en| Timers/MCPWM/RMT]], [[EN/07-Timers/02-WDT.en| WDT]], [[EN/07-Timers/03-Sleep-ULP.en| Sleep/ULP]], [[EN/07-Timers/04-TPL5110.en| TPL5110]] |
| `EN/08-Memory` | Memory | [[EN/08-Memory/01-Partitions-NVS.en]], [[EN/08-Memory/02-Filesystem.en| Filesystems]], [[EN/08-Memory/03-OTA.en| OTA]], [[EN/08-Memory/04-Secure-Boot-Encrypt.en]] |
| `EN/09-Firmware` | Firmware (8 notes) | [[EN/09-Firmware/01-ESP-IDF-Setup.en]], [[EN/09-Firmware/02-Arduino-PlatformIO.en]], [[EN/09-Firmware/03-MicroPython.en| MicroPython]], [[EN/09-Firmware/04-Esptool-Flash.en]], [[EN/09-Firmware/05-JTAG-Debug.en]], [[EN/09-Firmware/06-FreeRTOS-Patterns.en| FreeRTOS]], [[EN/09-Firmware/07-Testing-CI.en| Tests/CI]], [[EN/09-Firmware/08-Tooling-Deep.en| Tooling]] |
| `EN/10-Sensors` | Sensors (40 notes) | [[EN/10-Sensors/01-DHT11-DHT22.en| DHT]], [[EN/10-Sensors/02-DS18B20.en| DS18B20]], [[EN/10-Sensors/03-BME280-BMP280-SHT31.en| BME280]], [[EN/10-Sensors/04-MPU6050.en| MPU6050]], [[EN/10-Sensors/05-HC-SR04-PIR.en| HC-SR04/PIR]], [[EN/10-Sensors/06-INA219-HX711-BH1750.en| INA219/HX711]], [[EN/10-Sensors/07-AHT10-AHT20-SHT40.en| AHT/SHT40]], [[EN/10-Sensors/08-BME680-CCS811-MHZ19-PMS5003.en| Air/CO2/Dust]], [[EN/10-Sensors/09-ADS1115-MCP3008-PCF8574-MCP23017.en| ADS/Expander]], [[EN/10-Sensors/10-VL53L0X-TCS34725-TSL2561.en| ToF/Color]], [[EN/10-Sensors/11-NTC-PT100-MAX6675-LM35.en| Analog temp]], [[EN/10-Sensors/12-MQ2-MQ7-MQ135-Flame-Sound.en| Gases]], [[EN/10-Sensors/13-RCWL0516-Reed-Vibration-Tilt-Flow.en| Security/Fluids]], [[EN/10-Sensors/14-DS3231-Encoder-Keypad-Joystick.en| RTC/HMI]], [[EN/10-Sensors/15-ACS712-ZMPT101B-PZEM-AS5600-FSR.en| Current/Force]], [[EN/10-Sensors/16-HMC5883-BNO055-RFID-RC522-Barcode.en| Compass/9-DOF]], [[EN/10-Sensors/17-Gas-CO2-Precision.en| Gases/CO2]], [[EN/10-Sensors/18-Light-Spectral-Gesture.en| Light/Spectrum]], [[EN/10-Sensors/19-IMU-6-9DOF.en| IMU]], [[EN/10-Sensors/20-Bio-IR-Temp.en| Bio/IR]], [[EN/10-Sensors/21-Energy-Meters.en| Meters]], [[EN/10-Sensors/22-Gas-2-VOC-Industrial.en| Gases-2]], [[EN/10-Sensors/23-Dust-CO2-2.en| Dust/CO2-2]], [[EN/10-Sensors/24-Pressure-Level-Flow.en| Pressure/Level]], [[EN/10-Sensors/25-Mag-IMU-2.en| Mag/IMU-2]], [[EN/10-Sensors/26-Light-UV-IRArray-ToF.en| UV/Thermal/ToF]], [[EN/10-Sensors/27-Time-Mem-IO-DAC.en| Time/Memory/IO]], [[EN/10-Sensors/33-Input-IO-2.en| Input/IO-2]], [[EN/10-Sensors/28-Env-NewGen.en| Climate-new]], [[EN/10-Sensors/29-Range-Lidar-60GHz.en| Radar/Lidar]], [[EN/10-Sensors/30-Temp-Precision.en| Thermocouples]], [[EN/10-Sensors/31-IMU-Mag-3.en| IMU-3]], [[EN/10-Sensors/32-Light-Color-2.en| Light-2]], [[EN/10-Sensors/34-Buttons-Switches-Pots.en| Buttons]], [[EN/10-Sensors/35-Tails.en| Leftovers]], [[EN/10-Sensors/36-Agro.en| Agro]], [[EN/10-Sensors/37-Bio-2.en| Bio-2]], [[EN/10-Sensors/38-Industrial-Sensors.en| Industrial sensors]], [[EN/10-Sensors/39-Wireless-Sensors.en| Wireless]], [[EN/10-Sensors/40-Thermal-MLX90640.en| Thermal camera]] |
| `EN/11-Vivid` | Outputs (20 notes) | [[EN/11-Vivid/01-OLED-SSD1306.en| OLED]], [[EN/11-Vivid/02-TFT-LCD-Epaper.en| TFT/LCD]], [[EN/11-Vivid/03-NeoPixel-Servo-Rele-MOSFET.en| NeoPixel/Servo/Relay]], [[EN/11-Vivid/04-L298N-TB6612-A4988-Buzzer.en| Drivers]], [[EN/11-Vivid/05-MAX7219-TM1637-74HC595.en| MAX7219/7-seg]], [[EN/11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.en| PCA9685/Servos]], [[EN/11-Vivid/07-BTS7960-L9110S-SSR-Solenoid.en| BTS7960/SSR]], [[EN/11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.en| Audio/HMI]], [[EN/11-Vivid/09-LED-Strip-Power-SK6812-APA102.en| Strips/Power]], [[EN/11-Vivid/10-Displays-2.en| Displays-2]], [[EN/11-Vivid/11-PowerMotion-2.en| Power/Motion]], [[EN/11-Vivid/12-LVGL-SquareLine.en| LVGL]], [[EN/11-Vivid/13-Audio-Codecs.en| Audio]], [[EN/11-Vivid/14-Displays-3.en| Displays-3]], [[EN/11-Vivid/15-EInk.en| E-Ink]], [[EN/11-Vivid/16-LCD-Char.en| LCD]], [[EN/11-Vivid/17-Touchscreens.en| Touch]], [[EN/11-Vivid/18-MP3-TTS-Amps.en| MP3/TTS]], [[EN/11-Vivid/19-WebRadio-Streaming.en| Web radio]], [[EN/11-Vivid/20-LVGL-Widgets-Deep.en| LVGL widgets]] |
| `EN/12-Comm-Modules` | Comms (33 notes) | [[EN/12-Comm-Modules/01-RC522-RFID.en| RC522]], [[EN/12-Comm-Modules/02-NRF24-LoRa.en| NRF24/LoRa]], [[EN/12-Comm-Modules/03-SIM800L-GPS.en| SIM800L/GPS]], [[EN/12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera.en| RS485/CAN/Cam]], [[EN/12-Comm-Modules/05-PN532-RDM6300-Fingerprint-GM65.en| NFC/Biometrics]], [[EN/12-Comm-Modules/06-HC05-HM10-CC1101-HC12.en| BT/Sub-GHz]], [[EN/12-Comm-Modules/07-SIM7600-W5500-MCP2515.en| 4G/Ethernet/CAN]], [[EN/12-Comm-Modules/08-LD2410-UWB-IR-Voice.en| Radar/UWB]], [[EN/12-Comm-Modules/09-Cellular-NBIoT-UARTLoRa.en| Cellular/LoRa-UART]], [[EN/12-Comm-Modules/10-Industrial.en| Industrial]], [[EN/12-Comm-Modules/11-TinyML-Voice.en| TinyML/Voice]], [[EN/12-Comm-Modules/12-RC-Protocols.en| RC]], [[EN/12-Comm-Modules/13-Camera-Streaming.en| Streaming]], [[EN/12-Comm-Modules/14-Proximity-Inputs.en| Industrial inputs]], [[EN/12-Comm-Modules/15-RFID-Advanced.en| RFID deep-dive]], [[EN/12-Comm-Modules/16-Offline-Voice.en| Offline voice]], [[EN/12-Comm-Modules/17-GNSS-RTK.en| RTK]], [[EN/12-Comm-Modules/18-Cellular-LoRa-2.en| Cat-1/LoRa-2]], [[EN/12-Comm-Modules/19-Wired-2.en| Wired-2]], [[EN/12-Comm-Modules/20-NFC-Biometry-2.en| NFC-2]], [[EN/12-Comm-Modules/21-Motion-Control.en| Motion]], [[EN/12-Comm-Modules/22-Automotive.en| Automotive]], [[EN/12-Comm-Modules/23-Marine-Time.en| Marine/Time]], [[EN/12-Comm-Modules/24-DIY-Instruments.en| DIY instruments]], [[EN/12-Comm-Modules/25-Secure-Elements.en]], [[EN/12-Comm-Modules/26-SIM-Power.en| SIM+Power]], [[EN/12-Comm-Modules/27-LPWAN-Alt.en| LPWAN-Alt]], [[EN/12-Comm-Modules/28-UWB-2.en| UWB-2]], [[EN/12-Comm-Modules/29-LoRaWAN-Gateway.en| LoRaWAN gateway]], [[EN/12-Comm-Modules/30-USB-Host.en| USB host]], [[EN/12-Comm-Modules/31-Ethernet-PoE-Deep.en| Ethernet-PoE]], [[EN/12-Comm-Modules/32-USB-UVC-Host-Deep.en| USB-UVC]], [[EN/12-Comm-Modules/29-LoRaWAN-Gateway-Deep.en| Gateway deep-dive]] |
| `EN/13-Power-Modules` | Power modules (8 notes) | [[EN/13-Power-Modules/01-Buck-Boost-Solar.en| Buck/Solar]], [[EN/13-Power-Modules/02-Level-Shifters.en| Level-shifters]], [[EN/13-Power-Modules/03-TP4056-IP5306-BMS-UPS.en| Charging/BMS/UPS]], [[EN/13-Power-Modules/04-LDO-Buck-XL4015-Protect.en| XL4015/Protection]], [[EN/13-Power-Modules/05-USB-UART-AutoReset.en| USB-UART]], [[EN/13-Power-Modules/07-Stencil-Reflow.en| Stencil/Reflow]], [[EN/13-Power-Modules/08-Conformal-Coating.en| Coating/Compound]], [[EN/13-Power-Modules/09-USB-PD.en| USB-PD]] |
| `EN/14-Devboards` | Boards (17 notes) | [[EN/14-Devboards/01-DOIT-DevKitV1-NodeMCU32S.en| DOIT DevKitV1]], [[EN/14-Devboards/02-Wemos-D1-R32.en]], [[EN/14-Devboards/03-LILYGO-TDisplay-TBeam.en| LILYGO T-Display/T-Beam]], [[EN/14-Devboards/04-Heltec-WiFi-LoRa32.en| Heltec LoRa32]], [[EN/14-Devboards/05-ESP32-CAM.en| ESP32-CAM]], [[EN/14-Devboards/06-M5Stack-Core-Stick.en| M5Stack]], [[EN/14-Devboards/07-Feather-Huzzah32-Thing.en| Feather/Thing]], [[EN/14-Devboards/08-S3-DevKitC-C3-SuperMini-XIAO.en| S3/C3/XIAO]], [[EN/14-Devboards/09-WT32-ETH01-Olimex.en| WT32/Olimex]], [[EN/14-Devboards/10-Mini-Boards.en| Mini]], [[EN/14-Devboards/11-HMI-Boards.en| HMI]], [[EN/14-Devboards/12-Retro-Wearable.en| Retro]], [[EN/14-Devboards/13-ESP32C6-Boards.en| C6 boards]], [[EN/14-Devboards/14-ESP32H2-Boards.en| H2 boards]], [[EN/14-Devboards/15-Nano-ESP32.en| Nano]], [[EN/14-Devboards/16-P4-DevKit.en| P4 board]], [[EN/14-Devboards/17-C5-DevKit.en| C5 board]] |
| `EN/15-Protocols` | Protocols (16 notes) | [[EN/15-Protocols/01-MQTT.en| MQTT]], [[EN/15-Protocols/03-HTTP-Client.en| HTTP/WebSocket]], [[EN/15-Protocols/03-mDNS-NTP-TLS.en| mDNS/NTP/TLS]], [[EN/15-Protocols/04-Provisioning.en| Provisioning]], [[EN/15-Protocols/05-Cloud-Pipeline.en| Cloud]], [[EN/15-Protocols/06-Firmwares.en| WLED/Tasmota]], [[EN/15-Protocols/02-Notify-Voice.en| Notifications]], [[EN/15-Protocols/06-Secure-Boot.en| Security]], [[EN/15-Protocols/09-Matter-Thread-Zigbee.en| Matter]], [[EN/15-Protocols/10-Voice-Assistant.en| Voice]], [[EN/15-Protocols/05-Cloud-2.en| MQTT client]], [[EN/15-Protocols/12-AWS-IoT.en| AWS]], [[EN/15-Protocols/13-Azure-IoT.en| Azure]], [[EN/15-Protocols/14-MQTT-SN.en| MQTT-SN]], [[EN/15-Protocols/04-RTSP-Stream.en| Cloud platforms]], [[EN/15-Protocols/16-Matter-Thread-Deep.en| Matter deep-dive]] |
| `EN/16-Projects` | Projects (7 notes) | [[EN/16-Projects/01-Weather-Station.en| Weather station]], [[EN/16-Projects/02-GPS-Tracker.en| GPS tracker]], [[EN/16-Projects/03-Access-Control.en| Access control]], [[EN/16-Projects/04-Energy-Monitor.en| Energy monitor]], [[EN/16-Projects/05-TinyML-Deep-Practice.en| TinyML deep-dive]], [[EN/16-Projects/06-C5-C61-Robotics.en| C5/C61 robot]], [[EN/16-Projects/07-Edge-AI-Vision.en| AI vision]] |
| `EN/17-Lab` | Lab (5 notes) | [[EN/17-Lab/01-Instruments.en| Instruments]], [[EN/17-Lab/02-Soldering-Connectors.en| Soldering/Connectors]], [[EN/17-Lab/03-Enclosure-Cert-Factory.en| Enclosure/Factory]], [[EN/17-Lab/04-PCB-Design.en| PCB]], [[EN/17-Lab/05-Breadboard-Mezhi.en| Breadboard]] |
| `EN/99-Additions` | Appendices | [[EN/99-Additions/01-Pinout-tablici.en| Pinout]], [[EN/99-Additions/02-Troubleshooting-FAQ.en| FAQ]], [[EN/99-Additions/03-Cheklisti-montazhu.en| Checklists]], [[EN/99-Additions/04-Datasheet-Links.en| Datasheets]], [[EN/99-Additions/05-Official-Sources-Sensors.en| Sources: sensors]], [[EN/99-Additions/06-Official-Sources-Modules.en| Sources: modules]], [[EN/99-Additions/07-Versions.en| Versions]], [[EN/99-Additions/08-Diagnostic-Map.en| Map]] |

## Tags and graph

| Tag | Purpose |
| --- | --- |
| `#esp32/gpio` | Pins, modes, interrupts |
| `#esp32/adc` | Analog measurements |
| `#esp32/wifi` | STA/AP, scanning |
| `#esp32/ota` | Over-the-air updates |
| `#esp32/power` | Power, LDO, deep-sleep |
| `#esp32/sensor` | Sensors by template |

> [!tip] Graph
> Graph View → filter `path:ESP32-Reference`. The MOC links all sections, `## See also` in every note forms a dense grid.
>
> [!example] Schematic: powering a DevKit from USB
> Photo placeholder: `assets/img/devkit-usb-power.png` - see [[assets/README | How to add images]].

| ESP32 DevKit | PC / Module | Note |
| --- | --- | --- |
| 5V (VIN) | USB 5V | Board power, then LDO → 3.3V, see [[EN/02-Power-Supply/01-Power-Rails.en]] |
| GND | USB GND | Common ground is mandatory |
| TX0 (GPIO1) | RX USB-UART | 3.3V logic |
| RX0 (GPIO3) | TX USB-UART | No 5V! See [[EN/03-GPIO/03-Pull-Ups-Levels.en]] |
| EN + BOOT | Buttons | Download mode, see [[EN/01-Hardware/07-Boot-Strapping-Reset.en]] |

## See also

- [[EN/00-Start/01-How-to-Use-Guide.en| How to use it]]
- [[EN/00-Start/03-Chip-Comparison.en| Chip comparison]]
- [[EN/03-GPIO/01-GPIO-Overview.en| GPIO overview]]
- [[EN/04-Interfaces/01-UART.en| UART]]
- [[EN/05-Radio/01-WiFi-STA-AP.en| WiFi]]
- [[EN/06-Analog/01-ADC.en| ADC]]
- [[EN/08-Memory/03-OTA.en| OTA]]
- [[EN/09-Firmware/04-Esptool-Flash.en| Esptool]]
- [[EN/99-Additions/02-Troubleshooting-FAQ.en| FAQ]]
- [[EN/99-Additions/05-Official-Sources-Sensors.en| Official sources: sensors]]
- [[EN/99-Additions/06-Official-Sources-Modules.en| Official sources: modules]]
- [[scripts/README | Vault maintenance scripts]]
