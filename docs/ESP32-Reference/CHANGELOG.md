# Changelog - ESP32-Reference

## [v0.32] - 2026-10-06 - закриття дір: Matter-deep, P4-нативно, Ethernet, UVC, LVGL, AI-зір

### Додано

- `15-Protokoli/16-Matter-Thread-Deep.md` (175 рядків): Fabric, кластери, commissioning, border router, C + MicroPython.
- `01-Hardware/12-ESP32-P4-Native.md` (163 рядки): MIPI, H.264, USB-HS, зв'язка з C6.
- `12-Moduli-zvyazku/31-Ethernet-PoE-Deep.md` (172 рядки): W5500, PoE, резервування каналів.
- `12-Moduli-zvyazku/32-USB-UVC-Host-Deep.md` (168 рядків): UVC-захват, стрім, запис.
- `11-Vivid/20-LVGL-Widgets-Deep.md` (181 рядок): віджети, стилі, кирилиця, пам'ять.
- `16-Proekti/07-Edge-AI-Vision.md` (181 рядок): детекція, IoU-трекінг, сонце.
- 6 PNG-схем + лінки і лічильники в `Home.md`.

- Перевірка: style 0 / links 0 (221 файл / 3958 посилань) / home 0, PNG 213/213, реєстр 895/895.

## [v0.31] - 2026-10-06 - добивки: P4/C5-плати, тепловізор, USB-хост

### Додано

- `14-Devboards/16-P4-DevKit.md` (154 рядки): P4 Function EV Board - MIPI, H.264, зв'язка з C6, LVGL, Ethernet.
- `14-Devboards/17-C5-DevKit.md` (152 рядки): C5 DevKitC - dual-band WiFi 6, 802.15.4, Matter, антена.
- `10-Sensori/40-Thermal-MLX90640.md` (157 рядків): тепловізор 32x24, компенсація, детекція людей, пожежка.
- `12-Moduli-zvyazku/30-USB-Host.md` (153 рядки): TinyUSB-хост - MSC/HID/CDC, VBUS-живлення, приклади IDF.
- 4 PNG-схеми + лінки і лічильники в `Home.md` (сенсори 40, зв'язок 30, плати 17).

- Перевірка: style 0 / links 0 (215 файлів / 3910 посилань) / home 0, PNG 207/207, реєстр 892/892.

## [v0.30] - 2026-10-05 - глибина: TinyML-deep + C5/C61-робот

### Додано

- `16-Proekti/05-TinyML-Deep-Practice.md` (193 рядки): TFLite-Micro конвеєр, голос на C3 + INMP441, усмішка на S3 + OV2640, квантизація int8, робочий код, пам'ять і профілювання.
- `16-Proekti/06-C5-C61-Robotics.md` (177 рядків): двовузловий робот - C5 (мотори DRV8833, ПІД на енкодерах, керування) + C61 (VL53L0X + BME280 → MQTT), розпіновка, Arduino-core код.
- 2 PNG-схеми (`tinym-deep-scheme.png`, `c5c61-robot-scheme.png`) + лінки і лічильник папки в `Home.md`.

- Перевірка: style 0 / links 0 (211 файлів / 3869 посилань) / home 0, PNG 203/203.

## [v0.29] - 2026-10-05 - Nano ESP32 окремо

### Додано

- `14-Devboards/15-Nano-ESP32.md` (154 рядки): NORA-W106, три середовища, Cloud, шилди, клас + PNG-схема.

- Перевірка: style 0 / links 0 (209 файлів / 3844 посилання) / home 0.

## [v0.28] - 2026-10-05 - C6/H2 mesh максимально докладно

### Додано

- `01-Hardware/11-ESP32-C6-H2-Mesh.md` (221 рядок): Zigbee/Thread/Matter вибір, dataset, binding, fabric, SED, співіснування + перехрестя з оглядом.

- Перевірка: style 0 / links 0 (208 файлів / 3834 посилання) / home 0.

## [v0.27] - 2026-10-05 - C5/C61 глибина

### Додано

- `01-Hardware/10-ESP32-C5-C61.md` (424→469 рядків): практика 5 ГГц (DFS, співіснування) + карта міграції C3/C6.

- Перевірка: style 0 / links 0 (207 файлів / 3824 посилання) / home 0.

## [v0.26] - 2026-10-05 - карта діагностики ESP32

### Додано

- `99-Dodatki/08-Diagnostic-Map.md` (174 рядки): маршрут симптом-прилад-сигнал, покажчик інструментів, журнал, війністорії В6-В10. Доповнення до FAQ, не дубль.

- Перевірка: style 0 / links 0 (207 файлів / 3824 посилання) / home 0.

## [v0.25] - 2026-10-05 - макетка без дублювання STM32

### Додано

- `17-Lab/05-Breadboard-Mezhi.md` (237 рядків): ESP32-специфіка - стрепінг, USB-UART мости, WiFi-просадки, струми сну, паразити в цифрах. Перетин зі STM32-версією лише у фізиці макетки.

- Перевірка: style 0 / links 0 (206 файлів / 3814 посилань) / home 0.

Формат спрощений за Keep a Changelog: `Додано / Змінено / Виправлено` по чергах робіт.

## [v0.24] - 2026-10-02 - глибина до стандарту STM32

### Додано

- FAQ: рівні L1/L2/L3, дерева рішень (завантаження, WiFi), Panic-декодер, блок по платах (70-77), 5 війністорій. FAQ 156→274 рядки.
- `09-Proshivka/08-Tooling-Deep.md`: вимір тактів CCOUNT + шаблон драйвера esp_err_t (520→581 рядок).

- Перевірка: style 0 / links 0 (205 файлів / 3806 посилань) / home 0.

## [v0.23] - 2026-10-01 - покриття Призначення 100%

### Виправлено

- Заголовки ## Призначення + дедуп у RC522/RTC-GPIO/DHT11; рядки ILI9340, MPU9250(NRND), WS2811/WS2801, OV5640.
- Метрики: A 95.9% (решта - мета), B 100% контентних, C 79.2% явних, компоненти 888/888.

## [v0.22] - 2026-10-01 - ремонт вікілінків

### Виправлено

- Учетверені дужки вікілінків (1291), транслітеровані аліаси → голі/українські (1093+36), перевірка bad-alias у валідаторі. Валідатори: style 0 / links 0 / home 0.

## [v0.21] - 2026-09-30 - інвентаризація компонентів (доповнено)

### Додано (доповнення)

- `COMPONENTS.md`: реєстр 835 позначень (категорії, ноти, ✅/❌ datasheet); 786 з виробничими + розділ «Де шукати даташити» (9 сайтів); добір лінків SP3232/LAN8720A/LAN8710A/AS5048A/IS31FL3731/HT1621/ADNS-5050/XC6206/SE050/MPR121.
- `comp_inventory.py`: режими `--json`/`--registry`, фільтри пінів/периферії/протоколів.

## [v0.21] - 2026-09-30 - інвентаризація компонентів

### Додано

- `scripts/comp_inventory.py`: підрахунок моделей + класифікація даташитів (методологія з P4-звіту).
- Даташити: ASAIR DHT11/DHT22, OmniVision OV2640/OV5640, Eastron SDM (закриття 100% легітимного покриття).
- Підсумок інвентаризації: 874 унікальних позначень (~700 справжніх компонентів), 143 ноти з виробничими посиланнями, ~470+ посилань на 35+ хостів. Доповнення: розділ «Де шукати даташити» (9 сайтів), добір ~40 лінків у 20 нот → 835/835 ✅, 177 нот з виробничими.

## [v0.20] - 2026-09-30 - валідатори + типографічний рейд

### Додано

- `scripts/check_home.py`: лічильники `(N нот)` vs файли + повнота Home-навігації.
- `check_style.py`: bad-h1-title, bad-script (CJK), bad-pipe, bad-homoglyph (з allowlist ROMів/Vвх/дефісних композитів).
- `TODO.md`: розділ P4 - 10 залишкових прогалин покриття (MiCS-6814, VESC, EtherCAT/PROFINET, HB100, ACR122U, RTL-SDR, SNMP, Helium, TPS63020, зовн. WDT).
- Перевірка: style 0 / links 0 broken / home 0 (204 файли, 3658 лінків, 183 PNG).

### Виправлено

- ~70 типографічних: CJK-вставки у 6 файлах, гомогліфи (ekerан, тu, пH, RAЕON, Matriс…), title 25-Secure-Elements і 02-Level-Shifters.

## [v0.19] - 2026-09-30 - UNIFY: єдиний формат + максимальне покриття

### Додано

- `scripts/check_style.py`: 6 автоперевірок формату (frontmatter/рисунок/mermaid/помилки/джерела/≥150); задокументовано.
- 7 нових нот: `15-Cloud-Platforms`, `13-09-USB-PD`, `02-05-Fuel-Gauge`, `07-04-TPL5110`, `12-27-LPWAN-Alt`, `12-28-UWB-2`, `12-29-LoRaWAN-Gateway`; PNG 137-143 + GPIO 144-148.
- E8: SDM630/ATM90E32, ICM42688, WS2815, ASR6501, RS232/MAX3232, AMC1301 - у існуючі ноти.
- Перевірка: 204 файли / 3658 лінків / 0 broken / PNG 183 (missing NONE); style 0 порушень.

### Змінено

- Frontmatter добито: title +20, category +57, description +120 (генератор H1+теги), date +13; теги нормалізовано (5 виправлень).
- Mermaid додано у 58 нот; ASCII - у контентні; помилки - у 29; джерела - у 26; тонкі 19→0.
- `Home.md`: лічильники і лінки нових нот; `assets/README.md`: рядки 112-148.

### Виправлено

- Битий `\|` у 4 вікілінках (03-GPIO/01); CJK-одрук у Fuel-Gauge; польське «zwykle» в RTC-GPIO; 9 каліцтв спадщини (P3 минулого TODO).

## [v0.18] - 2026-09-30

### Додано

- P3: 9 схем PNG 128-136 для `09-Proshivka/01-05` і `08-Pamyat/01-04` (IDF/Arduino-MP/esptool/JTAG/partitions-UFS/OTA/secure-boot); вставки в уніфікованій точці.
- `scripts/README.md`: інструкція додавання схеми (8 кроків), стандарт AT-шпаргалок.
- Перевірка: 196 файлів / 3555 лінків / 0 broken / PNG 171 (missing NONE).

### Виправлено

- AT-шпаргалки уніфіковано (4 колонки; зведена в 03, базова в 07, повна в 18, перехресні посилання).
- Українська: 9 каліцтв спадщини черги 16 (`Netz`, `subject to`, `[CJK-хвіст]`, `схемотажка`, `зbezpeченosti` та ін.).
- README-приклад сам ламав чекер (буквальні посилання/PNG у бектиках).

## [v0.17] - 2026-09-30

### Додано

- P1 (GSM/GPS/SIM): нова `12-Moduli-zvyazku/26-SIM-Power` (341→401: SIM/eSIM/PIN/PUK/DET/ESD + VBAT/TX-бурсти/buck/суперкап/шунт + антени розд. 8); PNG 117-118.
- P1: `03-SIM800L-GPS` 256→595 (SMS/дзвінки/USSD/APN/GPRS/HTTPS/сон + NEO-порівняння/AssistNow/PPS/V_BCKP).
- P1: `18-Cellular-LoRa-2` 932→1034 (TinyGSM vs стеки, TLS/час, keepalive, офлайн-буфер).
- P1: `[GPS Tracker](../../ESP32-Reference/16-Proekti/02-GPS-Tracker.md)` 234→355 (бюджет батареї, локальний geofence, буфер, OTA, АКБ 12V, IP65).
- P2: 9 нових нот - `[Industrial Sensors](../../ESP32-Reference/10-Sensori/38-Industrial-Sensors.md)`, `39-Wireless-Sensors`; `[ESP32C6 Boards](../../ESP32-Reference/14-Devboards/13-ESP32C6-Boards.md)`, `14-ESP32H2-Boards`; `[AWS IoT](../../ESP32-Reference/15-Protokoli/12-AWS-IoT.md)`, `13-Azure-IoT`, `14-MQTT-SN`; `13-Moduli-zhivlennya-rivniv/07-Stencil-Reflow`, `08-Conformal-Coating`; PNG 119-127.
- `Home.md`: навігація доповнена (10→39, 12→26, 13→7, 14→14, 15→14 нот).
- Перевірка: 196 файлів / 3537 лінків / 0 broken / PNG 162 (missing NONE).

### Змінено

- `27-Cellular-Data` і `28-GNSS-Practice` НЕ створювались окремо (свідомо): покриття розкладено по нотах 03/18/26 + існуючій 17-RTK - зафіксовано в TODO.

## [v0.16] - 2026-09-30

### Додано

- Схеми PNG 112-116 (`agro-soil-weather`, `bio-2-ecg-emg`, `diy-instruments-ad9833`, `secure-elements-atecc`, `mqtt-client-3stack`); таблиця `assets/README.md` доповнена, список зайнятих імен оновлено.
- `TODO.md` - реєстр недоробленого і план розширення (P0/P1/P2/P3).
- Рис. 2 у `[Cloud 2](../../ESP32-Reference/15-Protokoli/11-Cloud-2.md).md` (три MQTT-стеки поруч).

### Виправлено

- `scripts/generate_schemes.py`: 5 записів черги 16 перенесено всередину `C = {...}` (були поза словником → SyntaxError); скрипт знову генерує 134 PNG.
- Битий лінк на `[BLE Bluetooth](../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md)` (залишок старого імені).
- Вставки зображень: `[Agro](../../ESP32-Reference/10-Sensori/36-Agro.md).md` (2× формат `![][`, рис. 1-2), `[Bio 2](../../ESP32-Reference/10-Sensori/37-Bio-2.md).md` (ембед у бектиках не рендерився), `12-Moduli-zvyazku/25-Secure-Elements.md` (формат `![][`).
- Розсинхрон змісту: `mqtt-client-3stack-scheme.png` замість невідповідного `cloud-2-firebase-shelly` (нота 11-Cloud-2 - про MQTT-клієнт, не Firebase/Shelly).
- Перевірка: 186 файлів / 3357 лінків / 0 broken / PNG 151 (missing NONE).

## [v0.15] - 2026-09-29

### Додано

- Черга 15: `12-Moduli-zvyazku/21-Motion-Control` (852: FluidNC/micro-ROS/CRSF), `22-Automotive` (855: OBD/LIN/TPMS), `23-Marine-Time` (652: NMEA2000/DCF77/GPSDO).
- Схеми PNG 109-111; рядок Home оновлено.

## [v0.14] - 2026-09-29

### Змінено

- Поглиблено чергу 14 до «дуже докладно»: `[PCB Design](../../ESP32-Reference/17-Lab/04-PCB-Design.md)` 491→846 (розрахунки з числами), `[Tails](../../ESP32-Reference/10-Sensori/35-Tails.md)` 261→559 (ENS210/SGP41/TGS8100, ZMOD4510→«не брати»), `[Versions](../../ESP32-Reference/99-Dodatki/07-Versions.md)` 125→318 (міграції IDF/Arduino/MP, deprecated-таблиця), Strapping/UART/SPI/SD/WDT/Sleep - всі 400+.

### Виправлено

- Прибрано сміттєвий рядок `uint16т dummy` з CRC-прикладa в `[UART](../../ESP32-Reference/04-Shini/01-UART.md).md`.

## [v0.13] - 2026-09-29

### Змінено

- Поглиблено чергу 13 до «дуже докладно»: `17-GNSS-RTK` 522→1004 (NMEA/UBX/RTCM3, survey-in, moving-base, NTRIP-кастер), `18-Cellular-LoRa-2` 499→932 (AT-шпаргалка 35 команд, APN UA, SX1280-ranging), `19-Wired-2` 518→1073 (MBAP-парсер, UDS/J1939, SDO, SLCAN, CAN-логер), `20-NFC-Biometry-2` 557→922 (PN5180 bring-up, DESFire-APDU, NTAG-ритуал).

## [v0.12] - 2026-09-29

### Змінено

- Поглиблено чергу 12 до стандарту «дуже докладно»: `10-Mini-Boards` 201→622 (8 карток плат, PIO-ini, монітор батареї), `11-HMI-Boards` 186→490 (7 карток, LovyanGFX, тачі), `12-Retro-Wearable` 182→573 (VGA-таблиці, T-Watch-сон, T-Deck-Meshtastic, розрахунок батарей).

## [v0.11] - 2026-09-29

### Додано

- Черга 12: `14-Devboards/10-12` (міні/HMI/ретро), `[ESP32 C5 C61](../../ESP32-Reference/01-Hardware/10-ESP32-C5-C61.md)`, Porivnyannya 88→191.
- Черга 13: `12-Moduli-zvyazku/17-20` (RTK, Cat-1/LoRa-2, дротові-2, NFC-2).
- Черга 14: `[PCB Design](../../ESP32-Reference/17-Lab/04-PCB-Design.md)`, `[Tails](../../ESP32-Reference/10-Sensori/35-Tails.md)`, `[Versions](../../ESP32-Reference/99-Dodatki/07-Versions.md)`, поглиблено Strapping/UART/SPI/SD/WDT/Sleep (+70-166).
- Схеми PNG 98-108; рядки Home оновлено.

## [v0.10] - 2026-09-29

### Додано

- Черга 11 (звук/голос): I2S 76→520 рядків (DMA/TDM/PDM), `[MP3 TTS Amps](../../ESP32-Reference/11-Vivid/18-MP3-TTS-Amps.md)`, `19-WebRadio-Streaming`, `12-Moduli-zvyazku/16-Offline-Voice`, `[Voice Assistant](../../ESP32-Reference/15-Protokoli/10-Voice-Assistant.md)`.
- Схеми PNG 93-97; рядки Home оновлено.

## [v0.9] - 2026-09-29

### Додано

- Черга 10: `12-Moduli-zvyazku/15-RFID-Advanced` (977 рядків: Mifare-deep, T5577, UHF, Wiegand/OSDP), `[BLE Gateway Tracker](../../ESP32-Reference/05-Radio/06-BLE-Gateway-Tracker.md)` (ESPresense, pvvx), `[BLE5 LongRange Audio](../../ESP32-Reference/05-Radio/07-BLE5-LongRange-Audio.md)` (Coded, LE Audio).
- Схеми PNG 90-92; рядки Home оновлено.

## [v0.8] - 2026-09-29

### Додано

- Черга 8: `10-Sensori/28-33` (клімат-newgen, радар/лідар 60ГГц, термопари, IMU-3, світло-2, ввід/IO-2), `[Displays 3](../../ESP32-Reference/11-Vivid/14-Displays-3.md)`.
- Черга 9: `[EInk](../../ESP32-Reference/11-Vivid/15-EInk.md)` (SSD1680, partial refresh), `16-LCD-Char` (HD44780 вглиб), `17-Touchscreens` (CST816/GT911/XPT2046), `[Buttons Switches Pots](../../ESP32-Reference/10-Sensori/34-Buttons-Switches-Pots.md)` (NO-NC, дебаунс ×3), `12-Moduli-zvyazku/14-Proximity-Inputs` (LJ12A3, NPN/PNP, PC817).
- Схеми PNG 78-89 у `scripts/generate_schemes.py` + `assets/README.md`; рядки Home оновлено.

### Виправлено

- `scripts/generate_schemes.py`: видалено дубльований блок записів, виправлено неекрановану лапку `3.5" TFT` і зайву кому - генератор знову працює (107 PNG зі скрипта).

## [v0.6] - 2026-09-28

### Додано

- Розділ `16-Proekti`: 4 cookbook-ноти (Метеостанція, GPS-трекер, Контроль доступу, Енергомонітор).
- Схеми `cookbook-*.png` (4 шт) у `scripts/generate_schemes.py` + генерація в `assets/img/`.
- Рядок `16-Proekti` у `Home.md`, позиції 49-52 у `assets/README.md`.

## [v0.7] - 2026-09-28

### Додано

- Розділ `17-Lab`: 3 ноти про інструменти, soldering та сертифікацію.
- Сенсори хвиля-4: `[Env NewGen](../../ESP32-Reference/10-Sensori/28-Env-NewGen.md)`, `29-Range-Lidar-60GHz`, `30-Temp-Precision`, `31-IMU-Mag-3`.
- Ноти виводу `[Displays 3](../../ESP32-Reference/11-Vivid/14-Displays-3.md)`: SSD1322/1351/ST7796/GC9A01/RA8875/FT81x.
- Ноти протоколу `[Matter Thread Zigbee](../../ESP32-Reference/15-Protokoli/09-Matter-Thread-Zigbee.md)`, `[BLE Mesh A2DP HID](../../ESP32-Reference/05-Radio/05-BLE-Mesh-A2DP-HID.md)`, `[Audio Codecs](../../ESP32-Reference/11-Vivid/13-Audio-Codecs.md)`.
- Ноти зв'язку `12-Moduli-zvyazku/12-RC-Protocols`, `13-Camera-Streaming`.
- Оновлено `scripts/generate_schemes.py` (95 PNG) та `assets/README.md` (позиції 53-77).
- Змінено `[Official Sources Modules](../../ESP32-Reference/99-Dodatki/06-Official-Sources-Modules.md).md` та `05-Official-Sources-Sensors`.

### Змінено

- `Home.md`: додавання нових розділів у навігацію та індекс сторінок.
- `[Porivnyannya chipiv](../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md).md`: оновлена таблиця чипів з C2/P4.

### Виправлено

- Виправлено помилки з escaped pipes у деяких нотаток.
- Виправлено синтаксичні помилки у `scripts/generate_schemes.py`.

## [v0.5] - 2026-09-28

### Додано

- Розділ `15-Protokoli` (5 нот): MQTT, HTTP/WebSocket, mDNS/NTP/TLS, Provisioning, Cloud-Pipeline.
- Схеми `mqtt-broker-lwt-scheme.png`, `http-websocket-rest-scheme.png`, `mdns-ntp-tls-scheme.png`, `provisioning-blufi-rainmaker-scheme.png`, `cloud-pipeline-nodered-scheme.png`.

## [v0.4] - 2026-09-28

### Додано

- Сенсорні ноти другої черги `10-Sensori/17-21`: гази/CO2, світло/спектр, IMU 6/9-DOF, біо/ІЧ, лічильники енергії.
- Ноти виводу `11-Vivid/10-11`: дисплеї-2, потужність/рух (FOC, TMC5160).
- Нота зв'язку `12-Moduli-zvyazku/09`: Cellular/NB-IoT/LoRa-UART; нота `01-Hardware/09`: C2/P4.

## [v0.3] - 2026-09-27

### Додано

- Ноти `10-Sensori/07-16`: AHT/SHT40, повітря/CO2/пил, ADS/експандери, ToF/колір, темп-аналог, гази, охорона/рідини, RTC/HMI, струм/сила, компас/9-DOF.
- Ноти `11-Vivid/05-09`: індикація, приводи, силові ключі, звук/HMI, стрічки/живлення.
- Ноти `12-Moduli-zvyazku/05-08`, `13-Moduli-zhivlennya-rivniv`, `14-Devboards`.

## [v0.2] - 2026-09-27

### Додано

- Базові розділи `00-Start`-`09-Proshivka`: глосарій, чипи, живлення, GPIO, шини, радіо, аналог, сон, пам'ять, прошивка.
- Додатки `99-Dodatki`: pinout-таблиці, FAQ 28 проблем, чек-листи, datasheet-посилання.
- Скрипти `scripts/generate_schemes.py`, `scripts/check_links.py`; `assets/README.md`.

## [v0.1] - 2026-09-27

### Додано

- Каркас vault: `Home.md` (MOC), `_templates/Component-Template.md`, структура папок `00-Start`-`99-Dodatki`.
- Плейсхолдер `assets/img/placeholder.png`, перші ноти старту та живлення.
