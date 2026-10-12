---
title: Troubleshooting FAQ - 69 Problems in Table Form
description: Troubleshooting FAQ - 69 problems table: Power and brownout (1-8); Boot and flash (9-12); WiFi and BLE drops (13-20); MQTT/HTTP breaks (21-28); LoRa and 4G (29-33); I2C, SPI and sensors (34-40); displays and LVGL (41-48); RSSI, antennas, cases (49-55); OTA and partitioning (56-63); WDT, deep-sleep, battery (64-69); shows schematics, code and tables.
tags: [esp32, troubleshooting, faq, brownout, wdt, wifi, mqtt, ota, adc, i2c, lora, lvgl]
category: Meta
lang: en
original: ESP32-Reference/99-Additions/02-Troubleshooting-FAQ.md
date-created: 2026-09-27
date: 2026-10-08
---

# Troubleshooting FAQ - 69 Problems in Table Form

![](../../../../ESP32-Reference/assets/img/placeholder.png)

How to use: find symptom in table, check cause, apply fix. Base: power [EN/02-Power-Supply/01-Power-Rails.en], GPIO [EN/03-GPIO/01-GPIO-Overview.en], I2C [I2C](../../../../ESP32-Reference/UA/04-Shini/03-I2C.md), SPI [SPI](../../../../ESP32-Reference/UA/04-Shini/02-SPI.md), UART [UART](../../../../ESP32-Reference/UA/04-Shini/01-UART.md), WiFi [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md), MQTT [MQTT](../../../../ESP32-Reference/UA/15-Protokoli/01-MQTT.md), sleep [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md), OTA [OTA](../../../../ESP32-Reference/UA/08-Pamyat/03-OTA.md), start [Home](../../../../ESP32-Reference/Home.md).

## Power and Brownout (1-8)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 1 | Brownout detector triggered, reboot | 3.3V sag during WiFi TX (500 mA peak), thin USB wires | short thick USB, cap 470-1000 µF on 5V + 100 nF on 3.3V, separate 5V 2A block | [EN/02-Power-Supply/01-Power-Rails.en] [02-LDO-DC-DC](../../../../ESP32-Reference/UA/02-Zhivlennya/02-LDO-DC-DC.md) |
| 2 | Boot loop: rst:0x8 TG1WDT_SYS_RESET | strapping GPIO pulled / power / bad flash | remove load from strapping 0/2/5/12/15, erase flash `esptool erase_flash` | [07-Boot-Strapping-Reset](../../../../ESP32-Reference/UA/01-Hardware/07-Boot-Strapping-Reset.md) [04-Esptool-Flash](../../../../ESP32-Reference/UA/09-Proshivka/04-Esptool-Flash.md) |
| 3 | Guru Meditation Error: LoadProhibited / IntegerDivideByZero | null pointer, divide by 0, stack overflow 8 KB | decode backtrace with EspExceptionDecoder, increase task stack to 4-8k, check malloc | [05-JTAG-Debug](../../../../ESP32-Reference/UA/09-Proshivka/05-JTAG-Debug.md) [EN/09-Firmware/01-ESP-IDF-Setup.en] |
| 4 | Task watchdog triggered, abort | loop() blocked >5 s, delay without yield, long I2C | break into chunks, vTaskDelay(1), esp_task_wdt_reset(), move to separate task | [02-WDT](../../../../ESP32-Reference/UA/07-Timeri-Son/02-WDT.md) |
| 5 | Upload failed: no serial data received | wrong COM, GPIO0 not in boot, CH340 driver | hold BOOT then press EN, check CH340/CP2102 driver, DATA cable (not charge-only) | [04-Esptool-Flash](../../../../ESP32-Reference/UA/09-Proshivka/04-Esptool-Flash.md) [05-USB-UART-AutoReset](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/05-USB-UART-AutoReset.md) |
| 6 | Timed out waiting for packet header | weak power during flash, speed 921600 | use 115200, cap 10 µF on EN, different USB port without hub | [04-Esptool-Flash](../../../../ESP32-Reference/UA/09-Proshivka/04-Esptool-Flash.md) |
| 7 | Flash read err 1000 / invalid header | bad firmware, wrong flash mode (QIO vs DIO) | erase_flash + flash with DIO 40M, check partition scheme | [06-Flash-PSRAM](../../../../ESP32-Reference/UA/01-Hardware/06-Flash-PSRAM.md) [01-Partitions-NVS](../../../../ESP32-Reference/UA/08-Pamyat/01-Partitions-NVS.md) |
| 8 | EN pin floats, board does not start without button | no RC on EN, sag at boot | 10 µF cap EN-GND + 10k resistor EN-3.3V | [07-Boot-Strapping-Reset](../../../../ESP32-Reference/UA/01-Hardware/07-Boot-Strapping-Reset.md) [EN/00-Start/04-Dev-Boards.en] |

## Boot and Flash (9-12)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 9 | rst:0x10 RTCWDT_RTC_RESET after flash | strapping GPIO12 pulled HIGH (VDD_SDIO 1.8V) | remove pull-up from GPIO12, check [EN/03-GPIO/02-Strapping-Pins.en] | [EN/03-GPIO/02-Strapping-Pins.en] [07-Boot-Strapping-Reset](../../../../ESP32-Reference/UA/01-Hardware/07-Boot-Strapping-Reset.md) |
| 10 | invalid magic byte / reboot without log | firmware not written at 0x10000 / wrong chip-target | `esptool write_flash 0x1000 bootloader + 0x8000 partitions + 0x10000 firmware`, check `--chip esp32-s3` | [04-Esptool-Flash](../../../../ESP32-Reference/UA/09-Proshivka/04-Esptool-Flash.md) [01-Partitions-NVS](../../../../ESP32-Reference/UA/08-Pamyat/01-Partitions-NVS.md) |
| 11 | Download mode not entered, BOOT does not help | broken auto-reset (DTR/RTS), CH340 without DTR | manual switch: BOOT LOW + EN LOW-HIGH, check [05-USB-UART-AutoReset](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/05-USB-UART-AutoReset.md) | [05-USB-UART-AutoReset](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/05-USB-UART-AutoReset.md) [04-Esptool-Flash](../../../../ESP32-Reference/UA/09-Proshivka/04-Esptool-Flash.md) |
| 12 | After erase_flash board silent | everything erased including bootloader | flash full set: bootloader + partitions + app + `esptool --chip auto` | [04-Esptool-Flash](../../../../ESP32-Reference/UA/09-Proshivka/04-Esptool-Flash.md) [01-Partitions-NVS](../../../../ESP32-Reference/UA/08-Pamyat/01-Partitions-NVS.md) |

## WiFi and BLE Drops (13-20)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 13 | WiFi disconnect reason 201 / 202 (NO_AP_FOUND) | weak signal, wrong channel, router 5 GHz only | move closer, fix channel 1/6/11 2.4 GHz, WiFi.setAutoReconnect(true) | [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md) |
| 14 | reason 15 (4WAY_HANDSHAKE_TIMEOUT) | wrong password / WPA3 incompatible | check password, router WPA2, esp_wifi_set_ps(WIFI_PS_NONE) for tests | [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md) |
| 15 | WiFi works, but MQTT breaks | heap exhausted, keepalive 60 s too long | keepalive 15-30 s, MQTT buffer 1024+, check freeHeap | [MQTT](../../../../ESP32-Reference/UA/15-Protokoli/01-MQTT.md) [03-mDNS-NTP-TLS](../../../../ESP32-Reference/UA/15-Protokoli/03-mDNS-NTP-TLS.md) |
| 16 | BLE + WiFi together - reboots | RAM/current shortage, antenna near metal | WiFi modem-sleep, BLE MTU smaller, separate power, move antenna | [02-BLE-Bluetooth](../../../../ESP32-Reference/UA/05-Radio/02-BLE-Bluetooth.md) [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md) |
| 17 | WiFi reason 8 (ASSOC_LEAVE) every minute | router drops due to power-save / short DHCP lease | WIFI_PS_NONE, static IP or long DHCP lease, reconnect with backoff | [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md) [Glossary] |
| 18 | BLE GATT disconnect 0x08 / MTU exchange fail | phone cuts MTU to 23, bonding without IO-capability | MTU 23 default, bonding only with passkey, NimBLE instead of Bluedroid on small heap | [02-BLE-Bluetooth](../../../../ESP32-Reference/UA/05-Radio/02-BLE-Bluetooth.md) [Glossary] |
| 19 | ESP-NOW delivery fail / peer not found | different channels / different MAC / WiFi not started | fix channel on both, add peer via esp_now_add_peer(), antenna away from metal | [03-ESP-NOW](../../../../ESP32-Reference/UA/05-Radio/03-ESP-NOW.md) [EN/01-Hardware/08-Antennas-RF.en] |
| 20 | WiFi works only near router | PCB antenna covered by metal / IPEX without antenna | move antenna out, for WROOM with IPEX screw 2.4 GHz antenna, RSSI > -75 dBm | [EN/01-Hardware/08-Antennas-RF.en] [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md) |

## MQTT and HTTP Breaks (21-28)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 21 | MQTT `rc=-2` conn lost right after WiFi | MQTT reconnect before WL_CONNECTED | reconnect only after WiFi status, backoff 1/2/4/8 s | [MQTT](../../../../ESP32-Reference/UA/15-Protokoli/01-MQTT.md) [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md) |
| 22 | MQTT `rc=5` not authorized / CONNACK 0x05 | wrong login or ACL blocks topic | mosquitto_passwd + `topic readwrite device/<id>/#`, allow_anonymous false with user | [MQTT](../../../../ESP32-Reference/UA/15-Protokoli/01-MQTT.md) [05-Cloud-Pipeline](../../../../ESP32-Reference/UA/15-Protokoli/05-Cloud-Pipeline.md) |
| 23 | Retain storm: old commands arrive after reconnect | retain set on telemetry stream | retain only on state/status/config, telemetry QoS 0 without retain | [MQTT](../../../../ESP32-Reference/UA/15-Protokoli/01-MQTT.md) [Glossary] |
| 24 | JSON truncated, broker drops connection | PubSubClient buffer 256 bytes too small | setBufferSize(1024) before connect(), check JSON length | [MQTT](../../../../ESP32-Reference/UA/15-Protokoli/01-MQTT.md) [05-Cloud-Pipeline](../../../../ESP32-Reference/UA/15-Protokoli/05-Cloud-Pipeline.md) |
| 25 | HTTPS `handshake failed` / mbedTLS -0x2700 | time 1970 (no NTP) or wrong CA bundle | SNTP sync first, then TLS; CA in LittleFS, setInsecure only for bench | [03-mDNS-NTP-TLS](../../../../ESP32-Reference/UA/15-Protokoli/03-mDNS-NTP-TLS.md) [EN/15-Protocols/03-HTTP-Client.en] |
| 26 | WebSocket breaks every ~60 s | ping/pong not set, proxy cuts idle | ping every 20-30 s, reconnect with backoff, separate task for WS | [EN/15-Protocols/03-HTTP-Client.en] [02-WDT](../../../../ESP32-Reference/UA/07-Timeri-Son/02-WDT.md) |
| 27 | SSE `/events` do not reach browser | proxy buffering / wrong Content-Type | Content-Type text/event-stream, flush after each event, heartbeat comment `:ping` | [EN/15-Protocols/03-HTTP-Client.en] |
| 28 | Node-RED does not see topics `device/#` | confusion `+` vs `#`, Cyrillic/spaces in topic | subscribe `device/+/sensors` for one level, `#` only at end; ID without spaces | [05-Cloud-Pipeline](../../../../ESP32-Reference/UA/15-Protokoli/05-Cloud-Pipeline.md) [MQTT](../../../../ESP32-Reference/UA/15-Protokoli/01-MQTT.md) |

## LoRa and 4G (29-33)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 29 | LoRa/NRF24 TX fail | 3.3V power sag, wrong antenna | 10-47 µF cap on module, PA_LOW first, antenna at correct frequency [02-NRF24-LoRa](../../../../ESP32-Reference/UA/12-Moduli-zvyazku/02-NRF24-LoRa.md) | [02-NRF24-LoRa](../../../../ESP32-Reference/UA/12-Moduli-zvyazku/02-NRF24-LoRa.md) |
| 30 | LoRa range meters instead of km | antenna 433 on module 868 (or vice versa), SF7 + BW500 | antenna strictly on frequency, SF10-12 + BW125 for range, antenna vertical up | [02-NRF24-LoRa](../../../../ESP32-Reference/UA/12-Moduli-zvyazku/02-NRF24-LoRa.md) [EN/01-Hardware/08-Antennas-RF.en] |
| 31 | E32/E22 LoRa-UART silent | M0/M1 both HIGH (sleep/config mode) instead of 00 | M0=LOW M1=LOW for operation, AT/config only in mode 11, AUX wait HIGH | [09-Cellular-NBIoT-UARTLoRa](../../../../ESP32-Reference/UA/12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa.md) [UART](../../../../ESP32-Reference/UA/04-Shini/01-UART.md) |
| 32 | SIM800L/A7670 `+CREG: 0,0` not registered | no 4V/2A, SIM without PIN unlock, GSM antenna wrong | LM2596 4.0V + 1000 µF, AT+CPIN?, AT+CBAND, move antenna to window | [03-SIM800L-GPS](../../../../ESP32-Reference/UA/12-Moduli-zvyazku/03-SIM800L-GPS.md) [07-SIM7600-W5500-MCP2515](../../../../ESP32-Reference/UA/12-Moduli-zvyazku/07-SIM7600-W5500-MCP2515.md) |
| 33 | GPS NEO-M8N cold start 15 min / no fix | antenna indoors, no backup RTC power | open sky 180°, active antenna 3.3V, battery on V_BCKP, check NMEA GGA | [03-SIM800L-GPS](../../../../ESP32-Reference/UA/12-Moduli-zvyazku/03-SIM800L-GPS.md) [03-LILYGO-TDisplay-TBeam](../../../../ESP32-Reference/UA/14-Devboards/03-LILYGO-TDisplay-TBeam.md) |

## I2C, SPI and Sensors (34-40)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 34 | ADC noise +-100 units, floating | WiFi noise + no averaging + long wires | average 32-64 samples, 100 nF cap on input, ADC1 only, atten 11 dB [ADC](../../../../ESP32-Reference/UA/06-Analog/01-ADC.md) | [ADC](../../../../ESP32-Reference/UA/06-Analog/01-ADC.md) |
| 35 | ADC2 shows zeros with WiFi | hardware conflict ADC2/WiFi | move to ADC1 (GPIO32-39) | [ADC](../../../../ESP32-Reference/UA/06-Analog/01-ADC.md) |
| 36 | DS18B20 -127 / 85 degrees | no pull-up 4.7k, parasitic power too weak | pull-up 4.7k to 3.3V, separate power, res 12 bit with 750 ms delay | [DS18B20](../../../../ESP32-Reference/UA/10-Sensori/02-DS18B20.md) |
| 37 | BME280 not found 0x76/0x77 | SDO address swapped, long wires | I2C scanner, SDO to GND=0x76 to VCC=0x77, wires <30 cm | [03-BME280-BMP280-SHT31](../../../../ESP32-Reference/UA/10-Sensori/03-BME280-BMP280-SHT31.md) [I2C](../../../../ESP32-Reference/UA/04-Shini/03-I2C.md) |
| 38 | MPU6050 drift / noise | vibration + no calibration + 5V instead of 3.3V | calibrate offset, DLPF 42 Hz, power 3.3V stable | [MPU6050](../../../../ESP32-Reference/UA/10-Sensori/04-MPU6050.md) [19-IMU-6-9DOF](../../../../ESP32-Reference/UA/10-Sensori/19-IMU-6-9DOF.md) |

## Displays and LVGL (41-48)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 41 | SPI LCD white / lines / no image | wrong SPI mode or voltage 5V | check SPI mode 0/3, LCD 3.3V, CS pull-up 10k | [02-TFT-LCD-Epaper](../../../../ESP32-Reference/UA/11-Vivid/02-TFT-LCD-Epaper.md) |
| 42 | LVGL screen freezes / buttons not work | heap too small (<60 KB), task priority wrong | heap >= 60 KB, task priority above LVGL timer, double buffer 1/2 screen | [08-DFPlayer-MAX98357-Nextion-LCD2004](../../../../ESP32-Reference/UA/11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.md) |
| 43 | OLED SSD1306 only top half | display height configured 32 instead of 64 | set height 64, check I2C address 0x3C/0x3D | [01-OLED-SSD1306](../../../../ESP32-Reference/UA/11-Vivid/01-OLED-SSD1306.md) |
| 44 | TFT 1.8/2.4 / MIPI LCD black after start | reset not pulsed / backlight not turned | pulse RESET 10 ms, backlight PWM or GPIO HIGH | [02-TFT-LCD-Epaper](../../../../ESP32-Reference/UA/11-Vivid/02-TFT-LCD-Epaper.md) |
| 45 | Touch X/Y swapped / wrong calibration | rotated panel / no calibration | rotate in LVGL, calibrate 5-point, save to NVS | [02-TFT-LCD-Epaper](../../../../ESP32-Reference/UA/11-Vivid/02-TFT-LCD-Epaper.md) |
| 46 | E-Paper only updates every 10 s | full refresh takes time, partial refresh not used | use partial refresh, reduce color depth, check temperature range | [02-TFT-LCD-Epaper](../../../../ESP32-Reference/UA/11-Vivid/02-TFT-LCD-Epaper.md) |
| 47 | Keyboard / encoder not detected | wrong GPIO / C/D swapped | check GPIO mapping, C/D to correct pins, debounce 10 ms | [13-Audio-Codecs](../../../../ESP32-Reference/UA/11-Vivid/13-Audio-Codecs.md) |
| 48 | Display flickers at WiFi TX | power sag / ground loop / long SPI wires | separate 3.3V for display, shorten SPI <20 cm, ground at one point | [02-TFT-LCD-Epaper](../../../../ESP32-Reference/UA/11-Vivid/02-TFT-LCD-Epaper.md) |

## Antenna, Case, Power (49-55)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 49 | RSSI drops >10 dB near wall / metal | antenna in case / IPEX loose / ground near antenna | external antenna, check IPEX connection, keep ground away | [EN/01-Hardware/08-Antennas-RF.en] [01-WiFi-STA-AP](../../../../ESP32-Reference/UA/05-Radio/01-WiFi-STA-AP.md) |
| 50 | Board reboots when motor / relay starts | inductive spike / ground bounce / voltage dip | diode on relay, separate 5V for motor, cap 470 µF, star ground | [EN/02-Power-Supply/01-Power-Rails.en] [02-Level-Shifters](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/02-Level-Shifters.md) |
| 51 | USB-UART disconnect when USB unplugs | CH340/CP2102 power from USB, no RC on EN | 10 µF EN cap so EN stays high briefly, or external 3.3V | [07-Boot-Strapping-Reset](../../../../ESP32-Reference/UA/01-Hardware/07-Boot-Strapping-Reset.md) |
| 52 | Deep-sleep current 5 mA instead of 10 µA | USB-UART powered / LED on / RTC memory not saved | cut USB power, LED desoldered, save RTC data, disable peripherals | [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md) |
| 53 | Battery voltage drops overnight | self-discharge / wakeup timer too frequent / no solar | check battery type, increase sleep interval, add MPPT / TP4056 | [EN/02-Power-Supply/04-Batteries-TP4056.en] [01-Buck-Boost-Solar](../../../../ESP32-Reference/UA/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md) |
| 54 | Temperature reading wrong / drifting | sensor near heat source / no calibration / wrong table | calibrate at 25 C, place away from LDO, use correct BME280 table | [03-BME280-BMP280-SHT31](../../../../ESP32-Reference/UA/10-Sensori/03-BME280-BMP280-SHT31.md) |
| 55 | Case condensation / moisture inside | sealed case / temperature swings / no ventilation | add silicone gasket, ventilation holes, silica gel, IP65 only if needed | [03-Enclosure-Cert-Factory](../../../../ESP32-Reference/UA/17-Lab/03-Enclosure-Cert-Factory.md) |

## OTA, Partition, WDT (56-63)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 56 | OTA fails at 90% / checksum error | partition too small / network drop / wrong URL | check partition size for app, retry 3 times with backoff, verify URL HTTPS | [03-OTA](../../../../ESP32-Reference/UA/08-Pamyat/03-OTA.md) [05-Cloud-Pipeline](../../../../ESP32-Reference/UA/15-Protokoli/05-Cloud-Pipeline.md) |
| 57 | After OTA board does not boot | partition not switched / bootloader old | check partition table, use `esp_ota_set_boot_partition()`, update bootloader | [03-OTA](../../../../ESP32-Reference/UA/08-Pamyat/03-OTA.md) [01-Partitions-NVS](../../../../ESP32-Reference/UA/08-Pamyat/01-Partitions-NVS.md) |
| 58 | WDT resets during long calculation | task >5 s / no yield / blocking I/O | split calculation, vTaskDelay(1), esp_task_wdt_reset(), move to lower priority | [02-WDT](../../../../ESP32-Reference/UA/07-Timeri-Son/02-WDT.md) |
| 59 | WDT does not reset after sleep | timer not restarted after wakeup | restart WDT after wakeup, check timer source | [02-WDT](../../../../ESP32-Reference/UA/07-Timeri-Son/02-WDT.md) |
| 60 | Brownout after OTA / flash due to low 3.3V | power sag during write / USB thin cable | 470 µF on 5V, 100 nF on 3.3V, 2A supply during update | [EN/02-Power-Supply/01-Power-Rails.en] |
| 61 | NVS corruption after reboot | power loss during write / wrong key / overflow | check NVS size, use `nvs_set_str` safely, check return codes | [01-Partitions-NVS](../../../../ESP32-Reference/UA/08-Pamyat/01-Partitions-NVS.md) |
| 62 | Log missing after reboot | Serial not started / file not opened / no flush | open file in `setup()`, flush every line, use `Serial` for debug | [EN/09-Firmware/01-ESP-IDF-Setup.en] |
| 63 | Firmware version mismatch between units | different builds / no version check / no serial | version in EEPROM/NVS, self-test PASS, log batch SHA | [03-Cheklisti-montazhu](../../../../ESP32-Reference/UA/99-Dodatki/03-Cheklisti-montazhu.md) |

## Deep-Sleep, Battery, WDT (64-69)

| # | Symptom | Cause | Fix | See |
| --- | --- | --- | --- | --- |
| 64 | Wakeup timer not firing / wrong interval | timer source wrong / RTC not initialized / deep-sleep not entered | use `esp_sleep_enable_timer_wakeup()`, check RTC, verify `esp_deep_sleep_start()` | [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md) |
| 65 | External wakeup not working | GPIO not configured / pull wrong / interrupt not enabled | set GPIO EXT0/EXT1, correct pull, `gpio_install_isr_service()`, test with button | [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md) |
| 66 | Touch wakeup false / misses | capacitive noise / wrong threshold / pad near metal | calibrate threshold, keep pad away from metal, test with dry finger | [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md) |
| 67 | Battery dies faster than calculated | average current underestimated / temperature cold / self-discharge | measure with INA219, add 50% reserve, use LiFePO4 or 18650 | [EN/02-Power-Supply/04-Batteries-TP4056.en] [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md) |
| 68 | Deep-sleep 150 µA instead of 10 µA | USB-UART chip powered / LED / regulator quiescent | disconnect USB-UART power, desolder LED, use low-Iq LDO | [03-Sleep-ULP](../../../../ESP32-Reference/UA/07-Timeri-Son/03-Sleep-ULP.md) [02-LDO-DC-DC](../../../../ESP32-Reference/UA/02-Zhivlennya/02-LDO-DC-DC.md) |
| 69 | Temperature sensor drift after sleep | self-heating / no calibration after wake / wrong table | calibrate after wake, wait 100 ms before read, use correct BME280 table | [03-BME280-BMP280-SHT31](../../../../ESP32-Reference/UA/10-Sensori/03-BME280-BMP280-SHT31.md) |

## See Also

- [Home](../../../../ESP32-Reference/Home.md)
- [01-Pinout-tablici](../../../../ESP32-Reference/UA/99-Dodatki/01-Pinout-tablici.md)
- [03-Cheklisti-montazhu](../../../../ESP32-Reference/UA/99-Dodatki/03-Cheklisti-montazhu.md)
- [04-Datasheet-Links](../../../../ESP32-Reference/UA/99-Dodatki/04-Datasheet-Links.md)
- [EN/02-Power-Supply/01-Power-Rails.en]

![](../../../../ESP32-Reference/assets/img/placeholder.png)

> UA original twin: [UA](../../../../ESP32-Reference/UA/99-Dodatki/02-Troubleshooting-FAQ.md)
