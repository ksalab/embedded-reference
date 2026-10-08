#!/usr/bin/env python3
"""PNG devboard-плат у стилі scripts/generate_schemes.py (PIL, DejaVu, шапка + смуга 3.3V)."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/ksalab/projects/.memories/ESP32-Reference/assets/img"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

def fonts():
    return (ImageFont.truetype(FB, 40), ImageFont.truetype(FB, 24),
            ImageFont.truetype(FM, 22), ImageFont.truetype(FR, 20))

C = {
"devboard-doit-v1.png": ("DOIT DevKitV1 — 30pin, AMS1117, CP2102/CH340",
 ["USB 5V -> VIN -> AMS1117-3.3 -> 3.3V (ESP32 + пін 3V3)",
  "Лівий ряд: EN/VP/VN/34/35/32/33/25/26/27/14/12/GND/13",
  "Правий ряд: 23/22/21/19/18/5/17/16/1/3/4/2/15/GND/5V",
  "CP2102 (кварц) або CH340G/C — драйвер SiLabs/WCH",
  "DTR->EN + RTS->GPIO0 (авторесет), кнопки BOOT+EN",
  "GPIO6-11 НЕ чіпати (Flash), 34-39 тільки входи"]),
"devboard-wemos-d1r32.png": ("Wemos D1 R32 — форм-фактор UNO, увага 5V!",
 ["DC 7.5V/USB -> стаб.5V -> AMS1117 -> 3.3V (два каскади!)",
  "D0/D1=GPIO3/1 (UART0) D11-D13=GPIO23/19/18 (SPI)",
  "A0-A5=GPIO2/4/35/34/36/39 — АЦП 0-3.3V, НЕ 0-5V!",
  "5V на шилд можна, СИГНАЛИ 5V->GPIO — ЗАБОРОНЕНО",
  "CH340G міст, кнопки IO0+EN, шилд зняти на час прошивки",
  "Strapping GPIO0/2/5/12/15 — шилд не тягне при boot"]),
"devboard-ttgo-tdisplay-tbeam.png": ("TTGO T-Display (ST7789) / T-Beam (LoRa+GPS+18650)",
 ["T-Display: TFT MOSI19/SCK18/CS5/DC16/RST23/BLK4(PWM!)",
  "Кнопки: B1=GPIO35(вхід!) B2=GPIO0(BOOT), I2C 21/22 вільні",
  "T-Beam: LoRa NSS18/RST14/DIO26 + SPI 5/27/19, антена 868!",
  "GPS TX->GPIO34 @9600, живлення GPS через PMU AXP2101",
  "JST полярність перевірити! PWR тримати 2с (старт від 18650)",
  "CP2104/CH9102 міст, прошивка 921600/460800"]),
"devboard-heltec-lora32.png": ("Heltec WiFi LoRa32 — OLED + LoRa + LiPo",
 ["V2: Classic+SX1276 / V3: S3+SX1262 — код несумісний!",
  "OLED SSD1306 0x3C: V2 RST16/SCL15/SDA4, V3 RST21/SCL18/SDA17",
  "LoRa: V2 NSS18/RST14/DIO26+SPI | V3 NSS8/RST12/DIO14+SPI",
  "USB-C/Micro 5V -> зарядка -> LiPo JST/SH1.25 -> 3.3V",
  "CP2102 міст, кнопки PRG/BOOT+RST, монітор 115200",
  "Антена IPEX своєї частоти ОБОВ'ЯЗКОВА до TX!"]),
"devboard-esp32cam.png": ("ESP32-CAM — OV2640, БЕЗ USB, FTDI 3.3V!",
 ["БЖ 5V 2A -> пін 5V + 470-1000мкФ (піки 300мА!)",
  "Камера: D0-D7 + PCLK/HREF/VSYNC + SCCB 26/27, PSRAM потрірібна",
  "FTDI TX->U0R(3) RX->U0T(1) GND->GND, логіка 3.3V!",
  "GPIO0->GND перемичка + RST -> шити 460800 -> зняти -> RST",
  "Вільні: 13/14/15/2 (без SD), 1/3 після прошивки",
  "GPIO16 (PSRAM CS) НЕ ЧІПАТИ! Спалах=GPIO4, LED=GPIO33"]),
"devboard-m5stack.png": ("M5Stack Core/Stick — дисплей+батарея+Grove",
 ["USB-C 5V -> PMU IP5306/AXP192 -> батарея + шини 5V/3.3V",
  "Core: LCD 23/19/18/14/27/33/32 + кнопки 39/38/37 (входи!)",
  "Grove A (21/22 I2C) — датчики без паяння! B/C — ADC/UART",
  "StickC Plus: TFT + IMU/PMU на 21/22, G36/G25 ділять порт!",
  "Швидкість ТІЛЬКИ 1500000/750000/500000/250000/115200",
  "UIFlow: M5Burner+блоки / Arduino: M5Unified + M5.begin()"]),
"devboard-feather-huzzah32.png": ("Feather HUZZAH32 / Thing — LiPo зарядка",
 ["USB 5V -> AP2112 -> 3.3V + MCP73831 -> LiPo JST-PH 3.7V",
  "Feather: CP2104; Thing: FT231X — авторесет, шити 921600",
  "Feather-піни: A0=26 SCK/MOSI/MISO=5/19/18 SDA/SCL=23/22",
  "Thing: GPIO-підписи + LED GPIO5 + кнопка 0 (BOOT)",
  "Полярність JST перевірити! Зарядка Feather 200мА",
  "Qwiic/STEMMA: 3V3/GND/SDA/SCL кабелем, VBAT — моніторинг"]),
"devboard-s3-c3-xiao.png": ("S3-DevKitC / C3-SuperMini / XIAO — native USB",
 ["S3-DevKitC: 2xUSB-C (UART CP2102N + native), RGB=GPIO48",
  "S3: OPI PSRAM у меню! JTAG через native USB, BOOT+RESET",
  "C3-SuperMini native USB: BOOT при вмиканні для 1-ї прошивки",
  "SuperMini BAT-пади БЕЗ зарядки — LiPo тільки через TP4056!",
  "XIAO: native + charging-IC 100мА, charging-LED гасне=100%",
  "Strapping C3: GPIO2/8/9 не тягнути при boot"]),
"devboard-wt32-eth01.png": ("WT32-ETH01 / Olimex — Ethernet+WiFi, PoE увага!",
 ["WT32-ETH01: FTDI TX->GPIO3 RX->GPIO1, GPIO0->GND + ресет",
  "ETH.begin(1,16,23,18,LAN8720,GPIO0_IN); RMII-піни НЕ чіпати",
  "Живлення 5V (LDO) або 3V3. PoE в WT32 — ЗАБОРОНЕНО!",
  "Olimex: CH340 вбудовано (460800), delay(500) перед ETH!",
  "EVB: реле 32/33 + CAN + IR + SD + UEXT; -EA антена для шаф",
  "PoE ТІЛЬКИ на PoE/PoE-ISO платах через 802.3af!"]),
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
