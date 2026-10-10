---
category: Moduli
lang: en
title: SIM800L GSM та NEO-6M GPS
description: SIM800L GSM + NEO-6M GPS - SIM800L - живлення (найважливіше); Легенда пінів модуля SIM800L; ASCII-схема (SIM800L); shows schematics, code and tables.
tags: [esp32, sim800l, gsm, gps, neo-6m, uart, at]
date: 2026-10-08
---

# SIM800L GSM + NEO-6M GPS

> [!danger] SIM800L not живити from 5V and not from 3.3V ESP32! Норма: 3.7-4.2V, пік 2A in TX-бурсті. without потужного живлення - вічні перезавантаження and мережа not реєструється.

Контекст: UART див. [[04-Interfaces/01-UART|UART]], живлення [[02-Power-Supply/01-Lancjugi-zhivlennya]] та [[13-Power-Modules/01-Buck-Boost-Solar]], рівні [[13-Power-Modules/02-Level-Shifters]], піни [[99-Additions/01-Pinout-tablici]], diagnostics [[99-Additions/02-Troubleshooting-FAQ]], start [[EN/Home.en]].

## Purpose

SIM800L GSM + NEO-6M GPS - SIM800L - живлення (найважливіше); Легенда пінів модуля SIM800L; ASCII-схема (SIM800L). SIM800L not живити from 5V and not from 3.3V ESP32! Норма: 3.7-4.2V, пік 2A in TX-бурсті. without потужного живлення - вічні перезавантаження and мережа not реєструється. Середній струм 200-500 мА, пік TX до 2A (577 мкс слот).

## 1. SIM800L - живлення (найважливіше)

- Чіп SIM800L: 3.4-4.4V (номінал 4.0V). 5V - смерть. 3.3V - нестабільність.
- Середній струм 200-500 мА, пік TX до 2A (577 мкс слот).
- Рекомендована схема: 5V 2A адаптер -> buck LM2596 виставлений on 4.0V -> електроліт 1000 мкФ low-ESR + кераміка 100 нФ біля SIM800L. Діод Шотткі проти переполюсовки.
- Дроти живлення товсті й короткі (<10 см). Земля спільна with ESP32.
- Світлодіод NET: блимає 1 раз/сек - немає мережі, 1 раз/3 сек - зареєстровано.

![[assets/img/sim800l-power-4v.png|500]]
*Fig. SIM800L - живлення 4.0V 2A via buck LM2596 + 1000 мкФ, UART перехресно до ESP32.*

### Module pin legend SIM800L

Синя маленька плата SIM800L має гребінку: VCC, RST, RXD, TXD, GND + окремо виводи NET (індикація), MIC/ SPK (аудіо), ANT (U.FL for GSM-антени).

| Пін | Позначення | Тип | Куди on ESP32 / живлення | Примітка |
| --- | --- | --- | --- | --- |
| 1 | VCC | Живлення 3.4-4.4V, пік 2A | Вихід buck LM2596 виставлений on 4.0V | not 5V (пробій!) and not 3.3V ESP32 (просадки, ребути); + електроліт 1000 мкФ low-ESR + 100 нФ біля піна |
| 2 | RST | Вхід reset, active low | GPIO4 або кнопка до GND | Імпульс LOW >100 мс = перезапуск; in роботі підтягнутий до HIGH |
| 3 | RXD | Вхід UART | GPIO17 (TX2 ESP32) via дільник | ESP32 TX → SIM800L RX: дільник 1к/2к або 2к/3.3к, або level-shifter, див. [[13-Power-Modules/02-Level-Shifters]] |
| 4 | TXD | Вихід UART | GPIO16 (RX2 ESP32) безпосередньо | SIM800L TX → ESP32 RX перехресно; рівень ~2.8V - ESP32 читає how HIGH without проблем |
| 5 | GND | Земля | GND ESP32 + GND buck | Спільна товста земля, дроти <10 см, зірка заземлення |
| 6 | NET | Вихід індикація | LED on платі / GPIO-вхід (опційно) | Блимання: 1 Гц = пошук мережі, 1 раз/3 с = зареєстровано |
| 7 | MIC_P / MIC_N | Аналоговий вхід | Електретний мікрофон | for дзвінків, in IoT зазвичай NC |
| 8 | SPK_P / SPK_N | Аналоговий вихід | Динамік 8 Ом | for дзвінків, in IoT зазвичай NC |
| 9 | ANT | ВЧ | GSM-антена (U.FL або клема) | without антени not реєструється, TX on повну потужність гріється |

Чому not 5V and not 3.3V:

1. **not 5V:** абсолютний максимум чипа 4.4V. Подача 5V пробиває RF-підсилювач - module гріється and вмирає for секунди. Виняток - лише червона плата EVB with власним стабілізатором and micro-USB: їй можна 5V, because on платі стоїть buck. Перевіряй свою версію візуально!
2. **not 3.3V ESP32:** нижня межа чипа 3.4V, but in TX-бурсті 2A просадка on тонких доріжках DevKit сягає 0.3-0.5V → 2.8V on чипі → brownout and перезапуск саме in момент реєстрації in мережі. Symptom класичний: «AT OK, but AT+CREG ніколи not 0,1».
3. **Правильно:** окремий buck LM2596 (або MP1584) with 5V 2A адаптера, on виході рівно 4.0V під навантаженням, електроліт 1000 мкФ low-ESR + кераміка 100 нФ біля SIM800L, товсті короткі дроти, див. [[02-Power-Supply/01-Lancjugi-zhivlennya]] and [[13-Power-Modules/01-Buck-Boost-Solar]].
4. **UART перехресно:** TX модуля → RX ESP32, RX модуля → TX ESP32. Швидкість for замовчуванням 115200, див. [[04-Interfaces/01-UART|UART]]. RX SIM800L not 5V-толерантний - дільник обов'язковий.
5. **AT-повідомлення:** після `AT+CMGF=1` and `AT+CMGS` module відповідає `>` and чекає текст + Ctrl+Z (0x1A). Довгі AT-сесії вести via міст Serial↔Serial2 for відладки.

| ESP32 | SIM800L | Примітка |
| --- | --- | --- |
| - (LM2596 4.0V) | VCC | 4.0V 2A + 1000 мкФ, not 5V/3.3V |
| GND | GND | спільна товста земля |
| GPIO16 (RX2) | TX | SIM800L TX -> ESP32 RX, дільник/level-shift якщо 5V-версія плати |
| GPIO17 (TX2) | RX | ESP32 TX -> SIM800L RX via дільник 2к/3.3к або 1к/2к |
| GPIO4 | RST | опційно, active low |
| - | ANT | GSM-антена, without неї not реєструється |

> Червона плата SIM800L EVB with micro-USB - має свій стабілізатор, їй можна 5V. Синя маленька плата without стабілізатора - тільки 4V! Перевіряй свою версію.

### ASCII schematic (SIM800L)

```text
Живлення SIM800L (обов'язково окремо!):
  5V 2A адаптер ──► [buck LM2596] ──(4.0V)──► VCC SIM800L
                                          ├─► 1000мкФ low-ESR (+) до VCC, (-) до GND
                                          └── 100нФ кераміка прямо на пінах

ESP32 DevKit          SIM800L (синя плата)
────────────          ───────────────────
GND ────────────────  GND (товстий провід <10 см, спільна з buck!)
GPIO16 (RX2) ◄──────  TXD (безпосередньо)
GPIO17 (TX2) ──[1к]──► RXD
                      [2к] від RXD до GND (дільник 5V→3.3V)
GPIO4 ─────────────►  RST (опційно)
                      ANT ──► GSM-антена (обов'язково!)
                      NET ──► LED блимає 1/3с = OK

Serial2.begin(115200, SERIAL_8N1, 16, 17);
```

### Mermaid (SIM800L)

```mermaid
graph LR
    AD[5V 2A адаптер] --> BUCK[buck LM2596<br/>4.0V]
    BUCK -->|4.0V 2A пік + 1000мкФ| VCC[VCC SIM800L]
    BUCK -->|GND товста| GNDM[GND SIM800L]
    ESP32[ESP32] -->|GND спільна| GNDM
    TXD[TXD SIM800L] -->|GPIO16 RX2| ESP32
    ESP32 -->|GPIO17 TX2 через дільник| RXD[RXD SIM800L]
    ESP32 -->|GPIO4 опційно| RST[RST]
    ANT[GSM антена] --- VCC
```

## 2. AT-команди базові

```text
AT                  -> OK (зв'язок)
AT+CPIN?            -> READY (SIM-карта)
AT+CSQ              -> рівень сигналу 0-31 (норма >10)
AT+CREG?            -> 0,1 зареєстровано home; 0,5 роумінг
AT+COPS?            -> оператор
AT+CBC              -> напруга живлення SIM800L
AT+CMGF=1           -> текстовий режим SMS
AT+CMGS="+380..."   -> відправка SMS (далі текст + Ctrl+Z)
AT+SAPBR=3,1,"APN","internet" -> налаштування GPRS
AT+HTTPINIT / AT+HTTPPARA / AT+HTTPACTION=0 -> HTTP GET
```

### Зведена шпаргалка (єдиний формат бази: команда → відповідь → зміст → error)

Деталі кожної групи - in розділах 4-9; повна шпаргалка on 35 команд (EC200U/A7670) - in [[EN/12-Comm-Modules/18-Cellular-LoRa-2.en]], базова 4G-table - in [[EN/12-Comm-Modules/07-SIM7600-W5500-MCP2515.en]].

| Команда | Відповідь OK | that означає | typical error |
| --- | --- | --- | --- |
| `AT` | `OK` | Зв'язок per UART | Тиша: baud 115200? RX/TX перехресно? |
| `AT+CPIN?` | `+CPIN: READY` | SIM готова | `SIM PIN`: `AT+CPIN="1234"`; IoT - зняти CLCK (розд. 1 ноти 26) |
| `AT+CSQ` | `+CSQ: 18,0` | Рівень, норма >10 | 99,99: антена/екран/підвал |
| `AT+CREG?` | `+CREG: 0,1` | Реєстрація home | 0,2: живлення/антена/PIN; блимання NET 1/с |
| `AT+CBC` | `+CBC: 0,95,4100` | VBAT ~4100 мВ | <3600: дроти/buck/конденсатор (розд. 5 ноти 26) |
| `AT+CMGF=1` | `OK` | Text-режим SMS | without нього `CMGS` → ERROR (розд. 4) |
| `AT+CMGS="..."` + текст + `0x1A` | `+CMGS: id` | SMS надіслано | `+CMS ERROR 305`: пам'ять/мережа; кирилиця - PDU (розд. 4) |
| `ATD+380...;` | `OK` | Voice дзвінок | without `;` - data-дзвінок/тиша (розд. 5) |
| `AT+CUSD=1,"*101#"` | URC `+CUSD` for 2-10 с | USSD-баланс | Порожньо: повторити; кирилиця - UCS2-hex (розд. 6) |
| `AT+SAPBR=1,1` | `OK` | Bearer відкрито | ERROR: APN буквально with табл. 6.2; спочатку `CGATT=1` (розд. 7) |
| `AT+HTTPACTION=0` | `+HTTPACTION: 0,200,N` | HTTP OK, N байт | 601: URL/SSL/час `CCLK` (розд. 7) |
| `AT+CSCLK=2` | `OK` | Автосон | not будиться: смикнути DTR (розд. 9) |

## 3. NEO-6M GPS

Specifications: u-blox NEO-6M, UART 9600 NMEA, холодний start ~30 с, гарячий ~5 с, антена керамічна + опційно активна. Живлення 3.3-5V (on платі є LDO), логіка 3.3V толерантна до ESP32 безпосередньо.

![[assets/img/neo6m-uart.png|500]]
*Fig. NEO-6M - UART до ESP32 перехресно (TX модуля → RX контролера), PPS опційно.*

### Module pin legend NEO-6M GPS

| Pin | Label | Type | To ESP32 | Note |
| --- | --- | --- | --- | --- |
| 1 | VCC | Живлення 3.3-5V | 3V3 або 5V for маркуванням плати | on платі GY-GPS6MV2 стоїть LDO - їй можна 5V; логіка все одно 3.3V |
| 2 | GND | Земля | GND | Спільна земля with ESP32 |
| 3 | TX | Вихід UART 9600 NMEA | GPIO26 (RX1 ESP32) | TX модуля → RX ESP32 перехресно! Потік NMEA $GPGGA/$GPRMC |
| 4 | RX | Вхід UART | GPIO27 (TX1 ESP32) або NC | ESP32 TX → GPS RX; потрібен лише for конфігурації u-blox (можна not підключати) |
| 5 | PPS | Вихід цифра 1 Гц | Будь-which GPIO with перериванням (опційно) | Точний імпульс секунди for синхронізації часу, ширина ~100 мс |

Пояснення:

- **TX модуля → RX ESP32:** головне правило UART, див. [[04-Interfaces/01-UART|UART]]. GPS лише передає NMEA, therefore мінімальна схема - 4 дроти: VCC, GND, TX→RX. RX GPS можна залишити вільним.
- **PPS:** імпульс точної секунди from супутників (джиттер ~десятки нс). Використовується for RTC-синхронізації або міток часу. without PPS час беруть with NMEA-речення `$GPRMC`.
- **Антена:** керамічний квадрат on платі працює лише with видом неба; in приміщенні - зовнішня активна антена with живленням 3.3V via коаксіал. Холодний start with видом неба 30 с - 15 хв.
- **Два UART одночасно:** SIM800L on Serial2 (16/17), GPS on Serial1 (26/27). not вішати обидва on один UART - NMEA потопить AT-відповіді.

| ESP32 | NEO-6M | Примітка |
| --- | --- | --- |
| 3V3 або 5V | VCC | for маркуванням плати (зазвичай 3.3-5V) |
| GND | GND | common ground |
| GPIO16 (RX2) | TX | GPS TX -> ESP32 RX |
| GPIO17 (TX2) | RX | for конфігурації u-blox, можна not підключати |
| - | PPS | опційно, точний імпульс 1 Гц |

> Два UART-пристрої одночасно: SIM800L on Serial2 (16/17), GPS on Serial1 (напр. RX=26 TX=27) або програмний. not вішати обидва on один UART.

### ASCII schematic (NEO-6M)

```text
ESP32 DevKit          NEO-6M GPS
────────────          ──────────
3V3 (або 5V) ──────►  VCC (за маркуванням плати)
GND ────────────────  GND
GPIO26 (RX1) ◄──────  TX (9600 NMEA, перехресно!)
GPIO27 (TX1) ──────►  RX (опційно, для конфігу u-blox)
GPIO33 ────────────◄  PPS (опційно, 1 Гц)

gpsSer.begin(9600, SERIAL_8N1, 26, 27);
Вид неба обов'язковий! У приміщенні — активна антена.
```

### Mermaid (NEO-6M)

```mermaid
graph LR
    ESP32[ESP32] -->|3V3/5V| VCC[VCC NEO-6M]
    ESP32 -->|GND| GNDM[GND NEO-6M]
    TX[TX GPS<br/>9600 NMEA] -->|GPIO26 RX1| ESP32
    ESP32 -->|GPIO27 TX1 опційно| RX[RX GPS]
    PPS[PPS 1Гц] -.->|GPIO33 опційно| ESP32
```

### Порівняння NEO-6M vs 7/8/M10: that брати in 2026

| module | Супутники | Холодний start | Струм | Ціна (орієнтир) | Вердикт |
| --- | --- | --- | --- | --- | --- |
| NEO-6M | GPS+SBAS (72 канали) | ~30 с (with небом) | ~40 мА | $5-8 | Класика for навчання; for виробу - застарів |
| NEO-7M | GPS+GLONASS | ~25 с | ~35 мА | $7-10 | GLONASS in місті допомагає, але рідкісний |
| NEO-8M (M8N) | GPS+GLONASS+BeiDou+Galileo | ~20 с | ~30 мА | $10-15 | **Золота середина**: 3 сузір'я, PPS, той же footprint |
| NEO-M10 (M10Q) | 4 сузір'я, L1 | ~15 с + низьке споживання | ~20 мА | $15-25 | Батарейні трекери; I2C+UART, крихітний 9.7×10.1 мм |
| ZED-F9P | L1+L2, RTK | сантиметри with поправками | ~70 мА | $150+ | Геодезія, див. [[EN/12-Comm-Modules/17-GNSS-RTK.en]] |

> Піни NEO-6M/7M/8M on платах GY-GPSxx сумісні (VCC/GND/TX/RX/PPS) - апгрейд перепайкою without зміни firmwares. M10Q - інший footprint (Qwiic), зате їсть удвічі менше.

### Холодний / теплий / гарячий start + батарейка V_BCKP

| Старт | that збережено | Час до Fix | Коли |
| --- | --- | --- | --- |
| Холодний | Нічого (перше ввімкнення, переїзд >500 км) | 30 с - 15 хв | with коробки, після місяця without живлення |
| Теплий | Альманах + приблизний час | 5-30 с | V_BCKP живий, доба without неба |
| Гарячий | Ефемериди + час + позиція | 1-5 с | Короткий сон, тунель 5 хв |

```text
V_BCKP (резервне живлення RTC+SRAM приймача):
  NEO-6M плата GY-GPS6MV2 ──► пін V_BCKP (якщо виведений) ──► CR1220/ML414 через діод
  або суперкап 0.22 Ф: тримає теплий start ~2–7 діб без основного живлення.
  Без V_BCKP кожне ввімкнення = холодний start = 30+ с очікування в полі!
```

### AssistNow (AGPS): ефемериди via інтернет

Замість чекати ефемериди with неба (12.5 хв повний альманах!) - залити via UART:

```text
1. Скачати AssistNow Online (u-blox сервер) або Offline (3–14 діб прогнозу).
2. Залити бінарник у приймач UBX-пакетом (115200 бод, RX GPS підключений!).
3. Холодний start стискається до 3–10 с.
Для ESP32-практики: ESP32 качає файл по WiFi/GPRS (розділи 7–8) і переливає в GPS.
Окупність: трекер, що прокидається раз на годину — тільки з AssistNow або M10.
```

### PPS-синхронізація часу (точність without NTP)

PPS - імпульс секунди with джиттером десятки нс (проти мілісекунд in NTP via WiFi!):

```cpp
// Arduino: мітка точної секунди за PPS + добивка часу з RMC
volatile unsigned long ppsMicros = 0;
void IRAM_ATTR onPPS() { ppsMicros = micros(); }
void setup() {
  pinMode(33, INPUT);
  attachInterrupt(33, onPPS, RISING);  // PPS від NEO-6M/M8N
}
// У loop: коли TinyGPS++ розпарсив RMC (година:хв:сек) — прив'язати до ppsMicros.
// Точність міток: ±1 мс без зусиль (обмеження — джиттер loop, не PPS).
// Для TLS/HTTPS через модем цього досить; для науки — input capture таймера.
```

## 4. SMS докладно: Text vs PDU, читання, видалення, URC

### 4.1. Два режими: Text (латиниця) vs PDU (кирилиця)

| Режим | Команда | that вміє | Обмеження |
| --- | --- | --- | --- |
| Text | `AT+CMGF=1` | Прості ASCII-SMS, читабельні команди | Тільки GSM 7-bit (латиниця, цифри); кирилиця - кракозябри |
| PDU | `AT+CMGF=0` | Будь-which алфавіт via UCS2-hex, довгі/конкатеновані | Треба кодувати/декодувати PDU (онлайн-кодувальники або бібліотека) |
| Кодування | `AT+CSCS?` | `"GSM"` for замовчуванням; `"UCS2"` for hex-тексту in Text-режимі | Після `AT+CSCS="UCS2"` номер теж hex: `AT+CMGS="002B0033..."` |

Практичне правило: сповіщення латиницею/транслітом - Text-режим; кирилиця клієнту - PDU або UCS2-hex. Трансліт in аварійних SMS - нормальна інженерна практика (доставка важливіша for красу).

### 4.2. Відправка SMS покроково (Text-режим)

```text
AT+CMGF=1            -> OK (текстовий режим)
AT+CSCS="GSM"        -> OK (кодування)
AT+CMGS="+380971234567"
>                    <- module чекає текст (запрошення ">")
ALARM: temp 85C!     <- текст, БЕЗ Enter зайвого
<Ctrl+Z 0x1A>        -> +CMGS: 12 / OK (надіслано, номер в архіві)
<Esc 0x1B>           -> скасувати набір (якщо передумав після ">")
```

> Після `>` чекати not більше 10-15 с: module сам повернеться in командний режим. Довгі паузи між символами тексту - module вирішить, that this кінець, and відправить обрізане.

### 4.3. Читання, видалення, пам'ять, нові повідомлення

```text
AT+CPMS?             -> +CPMS: "SM",3,50,"SM",3,50,"SM",3,50 (зайнято/всього)
AT+CPMS="SM","SM","SM" -> OK (сховище: SIM; альтернатива "ME" — пам'ять модуля)
AT+CMGL="ALL"        -> список усіх (повільно при 50 шт — краще "REC UNREAD")
AT+CMGR=2            -> прочитати №2 з індексом
AT+CMGD=2            -> видалити №2
AT+CMGD=1,4          -> видалити ВСІ (індекс ігнорується, прапор 4)
AT+CNMI=2,1,0,0,0    -> URC +CMTI при новій SMS (індекс одразу в події!)
```

> SIM-карта тримає зазвичай 30-50 SMS. Переповнення = нові not доходять МОВЧКИ. in автономному пристрої: після обробки кожної вхідної - `AT+CMGD`, плюс раз on добу `AT+CMGD=1,4` how страховка.

### 4.4. Mermaid: життєвий цикл SMS

```mermaid
flowchart TB
    CFG[AT+CMGF=1 + CNMI=2,1] --> WAIT{URC +CMTI?}
    WAIT -->|індекс N| READ[AT+CMGR=N — читати]
    READ --> PARSE{Команда валідна?}
    PARSE -->|Так: RELE ON| ACT[Виконати + SMS-відповідь]
    PARSE -->|Ні| IGN[Ігнор + SMS 'ERR']
    ACT --> DEL[AT+CMGD=N — видалити]
    IGN --> DEL
    DEL --> WAIT
    SEND[Тригога датчика] --> OUT[AT+CMGS — відправка]
    OUT -->|Ctrl+Z| OKC[+CMGS: id]
```

## 5. Голосові дзвінки: ATD/ATA/ATH, АОН, автовідповідь, аудіо

### 5.1. Команди дзвінка

```text
ATD+380971234567;    -> OK → дзвінок (крапка з комою ОБОВ'ЯЗКОВА = Voice режим!)
ATD+380971234567     -> без ";" = DATA-дзвінок (не те, буде помилка/тиша)
ATA                  -> підняти вхідний (після URC RING)
ATH                  -> покласти трубку (свою або чужу)
AT+CLIP=1            -> АОН: вхідний RING йде з +CLIP: "+380...",145
ATS0=2               -> автовідповідь після 2 гудків (0 = вимкнено)
AT+CHUP              -> альтернатива ATH (покласти)
```

Розбір вхідного with АОН:

```text
RING                          <- гудок 1
+CLIP: "+380971234567",145    <- хто дзвонить (при AT+CLIP=1)
RING                          <- гудок 2 …
```

> Білий список номерів - in прошивці: порівнювати `+CLIP`-номер with NVS-списком, чужих - `ATH` одразу. Дзвінок how безкоштовний канал керування: «дзвінок with номера господаря = відкрити ворота, передзвонювати not треба» (визначаємо per 1-2 RING and кладемо самі - 0 грн).

### 5.2. Аудіо: мікрофон/динамік синьої плати

| Пін/команда | Призначення | Налаштування |
| --- | --- | --- |
| MIC_P / MIC_N | Електретний мікрофон | Безпосередньо капсуль, живлення дає сам module |
| SPK_P / SPK_N | Динамік 8 Ом | Диференційно, not садити один кінець on GND! |
| `AT+CMIC=0,10` | Чутливість мікрофона (канал 0, рівень 0-15) | Підбирати: фон/луна |
| `AT+CLVL=60` | Гучність динаміка 0-100 | 60 - startова |
| `AT+CHFA=1` | Перемикання аудіоканалу (гарнітура/гучномовець on EVB) | on синій платі зазвичай один канал |

## 6. USSD and APN українських операторів

### 6.1. USSD-запити

```text
AT+CUSD=1,"*101#"     -> OK, відповідь приходить URC:
+CUSD: 0,"Balans 45.20 UAH",15   <- текст (може бути UCS2-hex при AT+CSCS="UCS2")
AT+CUSD=1,"*101#",15  -> той самий запит з явним кодуванням GSM 7-bit (15)
AT+CUSD=2             -> скасувати активну USSD-сесію
```

> USSD-відповідь - not синхронна: приходить окремим `+CUSD` via 2-10 с. Парсер AT має вміти URC посеред будь-якого очікування. Кирилична відповідь in UCS2-hex - декодувати hex→UTF-16.

### 6.2. Оператори України: USSD-портали та APN

| Оператор | Баланс/меню (USSD) | APN (GPRS) | Логін/пароль | Примітка |
| --- | --- | --- | --- | --- |
| Kyivstar | `*111#` (меню «Мій Київстар», там and баланс) | `kyivstar` | порожні | Старий `www.kyivstar.net` - legacy, not використовувати |
| Vodafone UA | `*101#` (баланс одразу) | `internet` | порожні | - |
| Lifecell | `*111#` (баланс/меню) | `internet` | порожні | - |

> APN чутливий до регістру and пробілів: `"Internet"` ≠ `"internet"` - мережа відхилить PDP-контекст with `AT+SAPBR=1,1` помилкою. Копіювати with таблиці буквально.

## 7. GPRS → HTTP/HTTPS: SAPBR-послідовність and SSL

### 7.1. Підняття GPRS-сесії (порядок суворий!)

```text
AT+CGATT=1                              -> OK (attach до GPRS-мережі)
AT+SAPBR=3,1,"Contype","GPRS"            -> OK
AT+SAPBR=3,1,"APN","kyivstar"            -> OK (свій APN з таблиці 6.2!)
AT+SAPBR=1,1                             -> OK (відкрити bearer; чекати до 30 с)
AT+SAPBR=2,1                             -> +SAPBR: 1,1,"10.20.30.40" (IP видано!)
```

### 7.2. HTTP GET / POST вбудованим стеком

```text
AT+HTTPINIT                              -> OK
AT+HTTPPARA="CID",1                      -> OK (прив'язка до bearer 1)
AT+HTTPPARA="URL","http://api.example.com/data?id=esp32_01" -> OK
AT+HTTPACTION=0                          -> OK, далі URC: +HTTPACTION: 0,200,142
AT+HTTPREAD                              -> +HTTPREAD: 142 <тіло відповіді>
AT+HTTPTERM                              -> OK (закрити HTTP)
AT+SAPBR=0,1                             -> OK (закрити bearer — економить трафік!)
```

POST with JSON:

```text
AT+HTTPPARA="URL","http://api.example.com/post" -> OK
AT+HTTPPARA="CONTENT","application/json"        -> OK
AT+HTTPDATA=48,10000                             -> DOWNLOAD (запрошення "DOWNLOAD")
{"id":"esp32_01","t":23.5}                       -> OK (48 байт тіла)
AT+HTTPACTION=1                                  -> +HTTPACTION: 1,200,16
```

### 7.3. HTTPS (SSL) - чесно про межі

```text
AT+HTTPSSL=1                             -> OK (увімкнути TLS для наступних HTTPACTION)
AT+HTTPPARA="URL","https://api.example.com/data" -> OK
AT+HTTPACTION=0                          -> +HTTPACTION: 0,200,...
```

| Питання | Відповідь |
| --- | --- |
| Чи вміє SIM800 HTTPS? | Так, `AT+HTTPSSL=1`. TLS 1.0-1.2, набір шифрів старий - частина сучасних серверів відмовить in handshake |
| Свій CA-сертифікат | Завантажити in файлову систему модуля (`AT+FSWRITE`), прив'язати via SSL-команди; процедура громіздка |
| check hostname | Слабка/відсутня - for критичних даних краще свій шлюз: ESP32→HTTP→свій сервер→HTTPS далі |
| Час for TLS | Сертифікати валідуються for часом: спочатку `AT+CCLK?` має показувати реальний час (NITZ from мережі або `AT+CCLK="26/09/30,08:00:00+12"`) |

### 7.4. Mermaid: GPRS-сесія

```mermaid
flowchart TB
    ATT[AT+CGATT=1] --> CFG[AT+SAPBR=3,1 Contype/APN]
    CFG --> OPEN[AT+SAPBR=1,1]
    OPEN --> IP{AT+SAPBR=2,1<br/>IP видано?}
    IP -->|Ні: APN/покриття| FIX[Перевірити APN табл. 6.2<br/>+CSQ, +CREG]
    FIX --> OPEN
    IP -->|Так| HTTP[HTTPINIT → HTTPPARA → HTTPACTION]
    HTTP --> SSL{HTTPS?}
    SSL -->|Так| TLS[AT+HTTPSSL=1 + CCLK-час!]
    SSL -->|Ні| READ[AT+HTTPREAD]
    TLS --> READ
    READ --> TERM[HTTPTERM → SAPBR=0,1]
```

## 8. E-mail via GPRS (оглядово - краще шлюзом)

SIM800 має вбудований SMTP-клієнт (`AT+EMAILCID`, `AT+EMAILTO`, `AT+SMTPSRV`, `AT+SMTPAUTH`, `AT+SMTPSEND`). Послідовність робоча, але:

1. Авторизація сучасних поштовиків (OAuth2, app-passwords) - via AT-термінал біль and сльози.
2. Кирилиця in темі/тілі - кодування вручну.
3. Будь-which зміна політики Gmail - and прошивка in полі ламається.

> Інженерне рішення: ESP32 шле HTTP POST on СВІЙ сервер (розділ 7.2), but листи відправляє сервер звичайною бібліотекою (Python `smtplib`, Node `nodemailer`). Модем лишається дурним транспортом - так надійніше on порядок.

## 9. Енергоспоживання та сон: CSCLK, DTR, PWRKEY

### 9.1. Режими SIM800L

| Режим | Струм (орієнтир) | how увійти | how вийти | Коли |
| --- | --- | --- | --- | --- |
| Активний (TX-бурст) | до 2000 мА пік | Дзвінок/GPRS-трафік | Кінець трафіку | Передача |
| Idle зареєстрований | ~20 мА | Просто чекати | - | Чергування |
| Сон `AT+CSCLK=1` | ~1-2 мА | DTR HIGH + 5 с тиші | DTR LOW | Батарейні датчики |
| Сон `AT+CSCLK=2` | ~1-2 мА | Автоматично після 5 с тиші | Дзвінок/SMS/дані per UART | Те саме without дроту DTR |
| Вимкнений | ~0 (десятки мкА) | PWRKEY LOW 1-2 с | PWRKEY LOW 1-2 с | Глибоке чергування |

```text
AT+CSCLK=0     -> OK (сон заборонено, за замовчуванням)
AT+CSCLK=1     -> OK (сон за рівнем DTR: HIGH = спати)
AT+CSCLK=2     -> OK (автосон: засне сам, прокинеться сам)
```

### 9.2. Схема сну with DTR and RI

```text
ESP32 DevKit          SIM800L
───────────          ───────
GPIO18 ────────────►  DTR (HIGH = "можна спати" при CSCLK=1)
GPIO19 ◄────────────  RI (прокидається LOW на 120 мс при дзвінку/SMS!)
GND ────────────────  GND
```

> PSM how in NB-IoT in SIM800 НЕМАЄ - not шукати. Економія будується так: `CSCLK=2` між сеансами + повне вимкнення PWRKEY on години (with MOSFET-ключем живлення, див. [[13-Power-Modules/04-LDO-Buck-XL4015-Protect]]). RI-пін - будильник ESP32: прокинувся → читай `+CLIP`/`+CMTI`.

### 9.3. Mermaid: сон and пробудження

```mermaid
flowchart TB
    IDLE[Idle, CSCLK=2] -->|5 с тиші| SLEEP[Сон ~1.5 мА]
    SLEEP -->|RING/SMS| RI[RI падає — будить ESP32]
    SLEEP -->|Дані в UART| WAKE[Прокинувся сам]
    SLEEP -->|DTR LOW при CSCLK=1| WAKE
    RI --> READ[ESP32 читає CLIP/CMTI]
    WAKE --> WORK[AT-сесія]
    WORK --> IDLE
    NIGHT[Ніч, 8 год] --> OFF[PWRKEY — вимкнути в нуль]
    OFF -->|Таймер/кнопка| PWR[PWRKEY — увімкнути]
    PWR --> REG[CREG + SAPBR заново]
```

![[assets/img/sim800l-sms-call-scheme.png|600]]
*Fig. SIM800L how термінал сповіщень: SMS (Text/PDU), голос with білим списком, USSD-баланс, GPRS-сесія SAPBR, сон via DTR/RI.*

## Code (3 фреймворки)

### Arduino - SIM800L AT + NEO-6M TinyGPS++

```cpp
#include <TinyGPS++.h>
TinyGPSPlus gps;
HardwareSerial sim(2); // RX=16 TX=17
HardwareSerial gpsSer(1); // RX=26 TX=27
void sendAT(const char* cmd, int wait=1000){
  sim.println(cmd); delay(wait);
  while(sim.available()) Serial.write(sim.read());
}
// Відправка SMS (Text-режим, латиниця/трансліт), розділ 4.2
bool smsSend(const char* num, const char* text){
  sim.println("AT+CMGF=1"); delay(300);
  sim.print("AT+CMGS=\""); sim.print(num); sim.println("\"");
  delay(500);
  if(!sim.find(">")) return false;   // немає запрошення — вихід
  sim.print(text); delay(300);
  sim.write(0x1A);                    // Ctrl+Z = відправити
  return sim.find("+CMGS:");          // чекаємо підтвердження
}
// Дзвінок-тривога з білим списком (розділ 5.1): дзвонимо самі
void alarmCall(const char* num){
  sim.print("ATD"); sim.print(num); sim.println(";"); // ";" = голос!
  delay(25000);                       // 25 с гудків
  sim.println("ATH");                 // покласти
}
void setup(){
  Serial.begin(115200); sim.begin(115200, SERIAL_8N1, 16, 17); gpsSer.begin(9600, SERIAL_8N1, 26, 27);
  delay(3000); sendAT("AT"); sendAT("AT+CSQ"); sendAT("AT+CREG?");
  sendAT("AT+CLIP=1");                // АОН для білого списку
  sendAT("AT+CNMI=2,1,0,0,0");        // URC нових SMS
}
void setup(){
  Serial.begin(115200); sim.begin(115200, SERIAL_8N1, 16, 17); gpsSer.begin(9600, SERIAL_8N1, 26, 27);
  delay(3000); sendAT("AT"); sendAT("AT+CSQ"); sendAT("AT+CREG?");
}
void loop(){
  while(gpsSer.available()) if(gps.encode(gpsSer.read())){
    if(gps.location.isValid()){ Serial.printf("LAT %.6f LON %.6f SAT %d\n", gps.location.lat(), gps.location.lng(), gps.satellites.value()); }
  }
  if(Serial.available()) sim.write(Serial.read()); // AT-міст з монітора
  if(sim.available()) Serial.write(sim.read());
}
```

### MicroPython - AT via UART + micropyGPS

```python
from machine import UART
import time
sim = UART(2, baudrate=115200, rx=16, tx=17)
gps = UART(1, baudrate=9600, rx=26, tx=27)
def at(cmd, wait=1):
    sim.write(cmd + "\r\n")
    time.sleep(wait)
    print(sim.read())
def sms_send(num, text):
    sim.write('AT+CMGF=1\r\n'); time.sleep(0.3)
    sim.write('AT+CMGS="%s"\r\n' % num); time.sleep(0.5)
    sim.write(text); time.sleep(0.3)
    sim.write(bytes([0x1A]))  # Ctrl+Z
    time.sleep(3)
    print(sim.read())
def ussd(code="*101#"):
    sim.write('AT+CUSD=1,"%s"\r\n' % code)
    time.sleep(8)  # відповідь приходить URC +CUSD із затримкою!
    print(sim.read())
at("AT"); at("AT+CSQ"); at("AT+CREG?")
at('AT+CLIP=1'); at('AT+CNMI=2,1,0,0,0')
while True:
    if gps.any(): print(gps.readline())
```

### ESP-IDF

```c
// uart_driver_install(UART_NUM_2, 2048, 2048, 0, NULL, 0);
// uart_set_pin(UART_NUM_2, 17, 16, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
// AT через uart_write_bytes + парсинг OK/CSQ/CREG; GPS NMEA через minmea lib на UART_NUM_1 (26/27)
```

### Живлення SIM800L - покрокова check

1. Виставити buck LM2596 on 4.0V without навантаження, потім підключити SIM800L via 1000 мкФ.
2. `AT+CBC` має показати 3900-4200 мВ; якщо менше - товстіші дроти, коротші, зірка GND.
3. `AT+CSQ` > 10, інакше винести GSM-антену до вікна.
4. `AT+CREG?` чекати `0,1` до 60 с; блимання NET 1 раз/3 с = успіх.
5. GPRS: `AT+SAPBR`, HTTP або MQTT - лише після стабільної реєстрації, див. [[05-Radio/01-WiFi-STA-AP]] for порівняння with WiFi.

| Symptom | Cause | Solution |
| --- | --- | --- |
| SIM800L перезавантажується, NET блимає | power sag, пік 2A | LM2596 on 4.0V + 1000 мкФ, товсті дроти |
| AT+CREG 0,2 довго | немає антени / слабкий сигнал / SIM without PIN знято | антена, AT+CPIN, винести до вікна |
| GPS нулі 00.0000 | холодний start in приміщенні | чекати 5-15 хв with видом неба, активна антена |
| Сміття in UART | різні baud / спільний UART on два модулі | SIM 115200 on Serial2, GPS 9600 on Serial1 |
| SIM800L гріється | подано 5V on синю плату | негайно вимкнути, verify 4.0V |
| `AT+CMGS` → `ERROR` / `+CMS ERROR: 305` | not Text-режим або немає пам'яті/мережі | `AT+CMGF=1` перед відправкою; `AT+CPMS?` - чистити; `AT+CREG?` має бути 0,1 |
| SMS кирилицею - кракозябри | Text-режим тільки GSM 7-bit | PDU-режим або `AT+CSCS="UCS2"` with hex, або трансліт (розділ 4.1) |
| Після `>` нічого not відправляється | забутий Ctrl+Z / пауза >15 с | `sim.write(0x1A)` одразу після тексту; Esc скасовує |
| Нові SMS not доходять | переповнена SIM (30-50 шт) | `AT+CMGD=1,4` раз on добу + видаляти після читання |
| USSD порожня відповідь / `+CUSD: 2` | сесія обірвана оператором | повторити via 10 с; `AT+CUSD=2` перед новим запитом |
| `AT+SAPBR=1,1` → ERROR | неправильний APN / немає GPRS-покриття | APN буквально with таблиці 6.2; `AT+CGATT=1` перед SAPBR |
| HTTPS `+HTTPACTION: 0,601` | немає маршруту/сертифікат відхилено (601 = network error) | verify URL, `AT+HTTPSSL=1`, `AT+CCLK?` - реальний час! |
| not прокидається with `CSCLK=2` | дані шлються in сплячий UART | смикнути DTR LOW або слати символ-пробудження and чекати 100 мс |
| `ATD` without `;` - тиша | пішов DATA-дзвінок замість голосового | завжди `ATD+380...;` with крапкою with комою |

## Official sources

- [SIM800 - даташити й AT Manual (SIMCom)](https://www.simcom.com/product/SIM800.html) - Hardware Design, живлення 3.4-4.4V.
- [NEO-6 - даташит (u-blox)](https://www.u-blox.com/en/product/neo-6-series) - NMEA, антени, фото.
- [ESP32 SIM800L SMS - туторіал with кодом (RNT)](https://randomnerdtutorials.com/esp32-sim800l-send-text-messages-sms/) - TinyGSM, пороги.
- [ESP32 + NEO-6M - туторіал with кодом (RNT)](https://randomnerdtutorials.com/esp32-neo-6m-gps-module-arduino/) - TinyGPS++, широта/довгота.
- [SIM800 Series AT Command Manual (SIMCom)](https://www.simcom.com/product/SIM800.html) - повний довідник: CMGF/CMGS/CUSD/SAPBR/HTTP/CSCLK/CSCS.
- [u-blox NEO-6M Hardware Integration Manual](https://www.u-blox.com/en/product/neo-6-series) - PPS, V_BCKP, активні антени.

## See also

- [[EN/Home.en]]
- [[04-Interfaces/01-UART|UART]]
- [[04-Interfaces/02-SPI|SPI]]
- [[02-Power-Supply/01-Lancjugi-zhivlennya]]
- [[03-GPIO/01-GPIO-oglyad]]
- [[13-Power-Modules/01-Buck-Boost-Solar]]
- [[13-Power-Modules/02-Level-Shifters]]
- [[EN/12-Comm-Modules/01-RC522-RFID.en]]
- [[EN/12-Comm-Modules/02-NRF24-LoRa.en]]
- [[EN/12-Comm-Modules/03-SIM800L-GPS.en]]
- [[EN/12-Comm-Modules/04-RS485-CAN-Ethernet-Kamera.en]]
- [[99-Additions/01-Pinout-tablici]]
- [[99-Additions/02-Troubleshooting-FAQ]]
