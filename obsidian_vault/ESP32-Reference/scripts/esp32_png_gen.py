#!/usr/bin/env python3
"""Генерація wiring/pinout PNG для ESP32-Reference. Оригінальні схеми, без копійованих картинок."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/ksalab/projects/.memories/ESP32-Reference/assets/img"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

def fonts():
    return (ImageFont.truetype(FB, 40), ImageFont.truetype(FB, 24),
            ImageFont.truetype(FM, 22), ImageFont.truetype(FR, 20))

# name: (заголовок, [рядки схеми])
C = {
"rc522-scheme.png": ("RC522 RFID — SPI, ТІЛЬКИ 3.3V",
 ["ESP32 3V3 ──► VCC (НЕ 5V! вб'є модуль)", "GND ─── GND (спільна)",
  "GPIO18 ──► SCK (VSPI clock)", "GPIO23 ──► MOSI", "GPIO19 ──► MISO",
  "GPIO5 ──► SDA/SS (Chip Select)", "GPIO22 ──► RST (тримати HIGH)",
  "IRQ ──► (можна не підключати, open-drain)"]),
"nrf24-wiring.png": ("NRF24L01 — SPI + конденсатор!",
 ["3V3 ──► VCC через конд. 10–100мкФ (біля модуля!)", "GND ─── GND",
  "GPIO18 SCK / GPIO23 MOSI / GPIO19 MISO", "GPIO5 ──► CSN   GPIO21 ──► CE",
  "IRQ ──► (опційно)   PA+LNA: струм до 250мА!", "Дроти < 20см, окреме живлення для PA"]),
"lora-ra02-scheme.png": ("LoRa Ra-02 SX1276 — АНТЕНА ОБОВ'ЯЗКОВА",
 ["3V3 ──► VCC   GND ─── GND", "SCK/MOSI/MISO ──► GPIO18/23/19",
  "GPIO5 ──► NSS   GPIO25 ──► RST   GPIO26 ──► DIO0",
  "!!! Без антени НЕ вмикати — згорить вихід !!!", "Частота: 433 або 868 МГц (одна!)", "Антена подалі від металу"]),
"sim800l-power-4v.png": ("SIM800L — 4.0V / 2A пік!",
 ["LM2596 виставити 4.0V БЕЗ модуля", "LM2596+ ──► VCC через конд. 1000мкФ",
  "Товсті короткі дроти (пік 2A!)", "GPIO16 ──► SIM RXD (через 1к)",
  "GPIO17 ──► SIM TXD (перехресно)", "GND спільна. НЕ 5V і НЕ 3.3V!"]),
"neo6m-uart.png": ("NEO-6M GPS — UART",
 ["3V3/5V ──► VCC (модуль з LDO)", "GND ─── GND", "GPS TX ──► GPIO16 (RX2)",
  "GPS RX ──► GPIO17 (TX2)", "PPS ──► GPIO (1Гц мітка)", "Антена — вид неба!"]),
"max485-de-re.png": ("MAX485 RS485 — напівдуплекс",
 ["3V3/5V ──► VCC   GND ─── GND", "GPIO17 ──► DI (TX)", "GPIO16 ──► RO (RX)",
  "GPIO4 ──► DE + RE (з'єднати! HIGH=TX)", "A/B ──► вита пара до A/B вузлів",
  "Термінатор 120 Ом на кінцях шини"]),
"can-hvd230-bus.png": ("SN65HVD230 CAN — шина",
 ["3V3 ──► VCC   GND ─── GND", "GPIO21 ──► CTX   GPIO22 ──► CRX",
  "CANH/CANL ──► CANH/CANL шини", "2×120 Ом на кінцях", "Rs: 10к на GND (швидкість)"]),
"lan8720-rmii.png": ("LAN8720 Ethernet — ТІЛЬКИ classic ESP32",
 ["RMII: TX0/TX1/TX_EN/RX0/RX1/CRS_DV", "MDC/MDIO ──► керування PHY",
  "nRST ──► GPIO, кварц 50МГц на платі", "Живлення 3.3V 200мА+", "Не працює на S2/S3/C3!"]),
"ov2640-s3-dvp.png": ("OV2640 камера — S3 + PSRAM",
 ["D0–D7 ──► GPIO камери S3", "VSYNC/HREF/PCLK ──► sync", "SIOC/SIOD ──► SCCB (I2C)",
  "XCLK ──► тактування   PWDN/RESET ──► GPIO", "Без PSRAM тільки QVGA!"]),
"dht22-scheme.png": ("DHT22 — 1-Wire + pull-up",
 ["3V3 ──► VCC   GND ─── GND", "GPIO4 ──► DATA через pull-up 5–10к до VCC",
  "Модулі 3-pin: pull-up вже є", "Опитування раз на 2с (DHT22)"]),
"ds18b20-1wire.png": ("DS18B20 — шина 1-Wire",
 ["3V3 ──► VDD (НЕ паразитне!)", "GND ─── GND", "GPIO15 ──► DQ + pull-up 4.7к",
  "Кілька датчиків на одній лінії DQ", "Довжина: вита пара, 100нФ біля датчика"]),
"bme280-i2c.png": ("BME280 — I2C 0x76/0x77",
 ["3V3 ──► VIN   GND ─── GND", "GPIO22 ──► SCL + pull-up 4.7к",
  "GPIO21 ──► SDA + pull-up 4.7к", "SDO→GND = 0x76, SDO→VCC = 0x77",
  "CSB→VCC в I2C-режимі"]),
"mpu6050-i2c.png": ("MPU6050 — акселерометр+гіроскоп",
 ["3V3 ──► VCC   GND ─── GND", "SCL/SDA ──► GPIO22/21 + pull-up",
  "AD0→GND = 0x68, AD0→VCC = 0x69", "INT ──► GPIO (пробудження)",
  "Жироскоп дрейфує — потрібен фильтр"]),
"hcsr04-divider.png": ("HC-SR04 — Echo 5V через дільник!",
 ["5V ──► VCC   GND ─── GND", "GPIO5 ──► Trig (10мкс імпульс)",
  "Echo (5V!) ──► дільник 1к/2к ──► GPIO18", "distance = t_мкс / 58 (см)",
  "PIR: VCC/GND/OUT→GPIO, 5–7м"]),
"ina219-hx711.png": ("INA219 струм + HX711 ваги",
 ["INA219: VIN+/VIN− в розрив +провода, I2C", "HX711: DT→GPIO, SCK→GPIO",
  "Тензодатчик E+/E−/A+/A−, калібрування вагою", "BH1750: I2C люксометр 0x23"]),
"oled-ssd1306-i2c.png": ("OLED SSD1306 128×64 — I2C",
 ["3V3 ──► VCC   GND ─── GND", "SCL→GPIO22  SDA→GPIO21 (0x3C)",
  "U8g2 / Adafruit_SSD1306", "Яскравість нижче — довше живе"]),
"tft-st7789-spi.png": ("TFT ST7789 240×240 — SPI",
 ["3V3 ──► VCC   GND ─── GND", "SCL→GPIO18 SDA→GPIO23 (MOSI)",
  "RES→GPIO  DC→GPIO  CS→GPIO5  BLK→3V3/PWM", "TFT_eSPI: налаштувати User_Setup",
  "E-paper: BUSY довге оновлення"]),
"neopixel-5v.png": ("NeoPixel WS2812 — 5V + RMT",
 ["5V 60мА/LED ──► 5V стрічки (окремий БЖ!)", "GND спільна + конд. 1000мкФ",
  "GPIO ──► DATA через 330 Ом", "3.3V→5V: 74AHCT125 для довгих ліній",
  "Серво SG90: 50Гц, VCC 5V окремо"]),
"l298n-tb6612.png": ("L298N vs TB6612 + A4988",
 ["L298N: втрата 2V + радіатор, VM 5–35V", "TB6612: MOSFET, ККД високий",
  "A4988: Vref = I×8×Rs, MS1-3 мікрокрок", "NEMA17: VM 12–24V, sleep при простої"]),
"buck-mp1584-trim.png": ("Buck MP1584/LM2596 — порядок!",
 ["1. Без навантаження виставити Vout!", "2. Мультиметр на вихід, крутити trim",
  "3. Вимкнути, підключити ESP32", "MP1584: до 3A   LM2596: до 3A + гріється",
  "MT3608 boost: з 18650 → 5V"]),
"txs0108-i2c.png": ("TXS0108 level-shifter",
 ["VCCA=3.3V  VCCB=5V  OE→VCCA", "A-сторона → ESP32, B-сторона → 5V модуль",
  "I2C: pull-up з ОБОХ сторін", "Дільник 1к/2к — для повільних ліній"]),
"aht10-scheme.png": ("AHT10/AHT20/SHT40 — вологість I2C",
 ["3V3 ──► VCC   GND ─── GND", "SCL/SDA → 22/21 (0x38 / 0x44)",
  "AHT: калібрувальна команда при старті", "SHT40: точність ±1.8%"]),
"air-quality-scheme.png": ("BME680/CCS811/MH-Z19/PMS5003",
 ["BME680: I2C VOC+тиск", "CCS811: прогрів 48г! eCO2",
  "MH-Z19B: UART CO2, ABC-калібрування", "PMS5003: UART + вентилятор, 5V"]),
"expander-scheme.png": ("ADS1115/MCP3008/PCF8574",
 ["ADS1115: 16біт I2C PGA, ADDR", "MCP3008: SPI 10біт, 8 каналів",
  "PCF8574: 8 GPIO I2C 0x20–0x27", "MCP23017: 16 GPIO + INT"]),
"light-tof-scheme.png": ("VL53L0X/TCS34725/TSL2561",
 ["VL53L0X: ToF лазер, XSHUT для адрес", "TCS34725: RGB + clear, INT",
  "TSL2561: люкси 0x29/0x39", "Уникати прямого сонця на ToF"]),
"temp-analog-scheme.png": ("NTC/PT100/MAX6675/LM35",
 ["NTC 10к + 10к дільник → ADC (Steinhart-Hart)", "PT100 → MAX31865 SPI",
  "K-термопара → MAX6675 SPI", "LM35: 10мВ/°C → ADC1 (не ADC2+WiFi!)"]),
"mq-gas-flame-sound-scheme.png": ("MQ-гази/полум'я/звук",
 ["MQ: нагрів 150мА, прогрів 24–48г!", "AO→ADC + DO→GPIO (поріг)",
  "Полум'я KY-026: чутливий до сонця", "KY-038: MIC + регулювання"]),
"security-flow-scheme.png": ("RCWL-0516/геркон/YF-S201/pH",
 ["RCWL: OUT 3.3V, VIN 4–28V, крізь стіни!", "YF-S201: імпульси ~450/л → PCNT",
  "pH-4502C: калібрування буферами", "TDS: залежність від температури"]),
"rtc-hmi-scheme.png": ("DS3231/енкодер/клавіатура",
 ["DS3231: I2C + CR2032, SQW/INT", "KY-040: CLK/DT + SW, переривання",
  "4×4: рядки→OUT, стовпці→IN_PULLUP", "Джойстик: VRX/VRY→ADC + SW"]),
"current-magnet-force-scheme.png": ("ACS712/ZMPT/PZEM/AS5600/FSR",
 ["ACS712: offset VCC/2, мВ/А за версією", "ZMPT101B: 220V! калібрування trim",
  "PZEM-004T: UART Modbus", "AS5600: магніт над чипом, I2C"]),
"orientation-id-scheme.png": ("QMC5883/BNO055/IR/GM65",
 ["QMC5883: компас, hard-iron калібрування", "BNO055: 9-DOF + fusion",
  "VS1838: 38кГц → RMT", "GM65: UART сканер кодів"]),
"max7219-tm1637-74hc595-scheme.png": ("MAX7219/TM1637/74HC595",
 ["MAX7219: DIN→MOSI CLK→SCK CS→GPIO, каскад", "TM1637: CLK/DIO, 5V живлення",
  "74HC595: DS/SHCP/STCP, OE→GND MR→VCC", "Конд. 10мкФ біля MAX7219"]),
"pca9685-mg996r-stepper-scheme.png": ("PCA9685/MG996R/28BYJ/TMC2209",
 ["PCA9685: VCC 3.3V + V+ 5–6V серво", "MG996R: пік 2.5A — окремий БЖ!",
  "28BYJ+ULN2003: IN1–4 послідовність", "TMC2209: UART + Vref + DIAG"]),
"bts7960-ssr-solenoid-scheme.png": ("BTS7960/L9110/SSR/соленоїд",
 ["BTS7960: RPWM/LPWM + EN, VM 6–27V", "L9110S: 2 канали 800мА",
  "SSR: DC 3.3V керує AC (нуль-перехід)", "Соленоїд: MOSFET + 1N4007!"]),
"dfplayer-max98357-nextion-lcd-scheme.png": ("DFPlayer/MAX98357/Nextion/2004",
 ["DFPlayer: RX через 1к, BUSY→GPIO, microSD", "MAX98357: BCLK/LRCK/DIN I2S",
  "Nextion: 5V, UART перехресно", "2004+PCF8574: 0x27/0x3F, контраст"]),
"led-strip-power-shifter-scheme.png": ("Стрічки: живлення+рівні",
 ["60мА/LED: 300 LED = 18A пік!", "Інжекція 5V кожні 2–3м", "1000мкФ + 330 Ом на DATA",
  "74AHCT125: 3.3V→5V для довгих ліній"]),
"nfc-rfid-biometry-scheme.png": ("PN532/RDM6300/R307/GM65",
 ["PN532: SEL0/SEL1 режим, IRQ/RST", "RDM6300: 5V + TX 9600 + котушка",
  "R307: UART відбитки, TOUCH", "GM65: UART, TRIG"]),
"bt-subghz-scheme.png": ("HC-05/HM-10/CC1101/HC-12",
 ["HC-05: EN для AT, RX через дільник!", "HM-10: 3.3V BLE", "CC1101: SPI + GDO0",
  "HC-12: SET для AT, антена 433МГц"]),
"lte-eth-can-scheme.png": ("SIM7600/W5500/MCP2515",
 ["SIM7600: VBAT 3.8V 3A! + PWRKEY", "W5500: SPI + RST/INT, 3.3V",
  "MCP2515: 8МГц кварц + J1 120 Ом"]),
"radar-uwb-ir-voice-scheme.png": ("LD2410/UWB/IR/голос",
 ["LD2410: OUT + UART 256000, гейти", "DWM1000: SPI + TWR", "VS1838: OUT → RMT",
  "SU-03T: UART голосові команди"]),
"tp4056-ip5306-bms-ups-scheme.png": ("TP4056/BMS/UPS",
 ["TP4056: PROG 1.2к=1A, LED R/G", "OUT відключається при 2.4V (DW01)",
  "BMS: B+/B−/P+/P−, балансування", "UPS: MOSFET+Schottky без ресету"]),
"ldo-buck-xl4015-protect-scheme.png": ("LDO/buck/захист",
 ["AMS1117: 1A, dropout 1.1V, гріється", "ME6211: 500мА для ESP32",
  "XL4015: CC/CV, V без навантаження!", "PTC + TVS + MOSFET від переполюсовки"]),
"usb-uart-autoreset-scheme.png": ("USB-UART + auto-reset",
 ["CH340/CP2102: TX/RX перехресно", "DTR→EN + RTS→BOOT (2×NPN + 100нФ)",
  "460800 робоча, 115200 для довгих кабелів", "S2/S3: вбудований USB"]),
"hc05-scheme.png": ("HC-05 детально", ["Див. bt-subghz-scheme", "EN=HIGH → AT 38400",
  "RXD через дільник 1к/2к", "STATE → GPIO"]),
"hm10-scheme.png": ("HM-10 BLE детально", ["Див. bt-subghz-scheme", "3.3V VCC",
  "BRK для розриву", "AT+ROLE0/1"]),
"pn532-scheme.png": ("PN532 детально", ["Див. nfc-rfid-biometry-scheme",
  "I2C 0x24 / SPI / HSU", "SEL0/SEL1 перемички"]),
"rdm6300-scheme.png": ("RDM6300 125кГц", ["5V VCC, TX 9600", "Зовнішня котушка",
  "Тільки читання EM4100"]),
"sim7600-scheme.png": ("SIM7600 4G детально", ["Див. lte-eth-can-scheme",
  "PWRKEY 1с імпульс", "AT+CMQTT"]),
"w5500-scheme.png": ("W5500 Ethernet SPI", ["Див. lte-eth-can-scheme",
  "SPI 33МГц макс", "Ethernet.h бібліотека"]),
"ld2410-scheme.png": ("LD2410 радар детально", ["Див. radar-uwb-ir-voice-scheme",
  "Гейти 0–8 чутливість", "BT-конфіг HLKRadarTool"]),
"devkit-usb-power.png": ("DevKit живлення від USB",
 ["USB 5V ──► VIN ──► LDO ──► 3.3V", "GND спільна", "TX0/RX0 ──► USB-UART",
  "EN+BOOT для download-режиму"]),
"brownout-scope.png": ("Brownout при WiFi TX",
 ["Пік 500мА при TX → просадка", "Слабкий LDO/тонкі дроти = 2.9V",
  "Ліки: 470мкФ + короткий USB + 5V/2A", "Brownout detector → reboot"]),
}

def draw(name, title, lines):
    Ft, Fs, Fm, Ff = fonts()
    W, H = 1000, 200 + len(lines) * 44 + 120
    H = max(H, 520)
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 130], fill=(17, 42, 67))
    d.text((30, 22), "ESP32-Reference", font=Fs, fill=(125, 211, 252))
    d.text((30, 55), title, font=Ft, fill="white")
    y = 150
    d.rectangle([0, y - 34, W, y + 2], fill=(255, 251, 235))
    d.text((30, y - 30), "3.3V логіка!  5V на GPIO — смерть кристала.", font=Ff, fill=(146, 64, 14))
    y += 30
    for ln in lines:
        d.text((30, y), "•  " + ln, font=Fm, fill=(17, 24, 39))
        y += 44
    d.rectangle([0, H - 56, W, H], fill=(241, 245, 249))
    d.text((30, H - 42), "ESP32-Reference  •  згенеровано локально (без копійованих картинок)",
           font=Ff, fill=(100, 116, 139))
    img.save(os.path.join(OUT, name))

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, (t, ls) in C.items():
        draw(n, t, ls)
    print(f"generated {len(C)} png")
