---
description: Сантиметрова навігація для ESP32: RTK-приймачі u-blox ZED-F9P та Unicore UM980
title: GNSS RTK - ZED-F9P, UM980, LC29H, бюджетні модулі, NTRIP на ESP32
tags: [esp32, gnss, rtk, zed-f9p, um980, lc29h, ntrip, rtcm, nmea, ubx, atgm336h, u-center, rtklib]
category: Moduli
date-created: 2026-09-29
---

# GNSS RTK - ZED-F9P / UM980, база + ровер, NTRIP-клієнт на ESP32

## Призначення

Сантиметрова навігація для ESP32: RTK-приймачі u-blox ZED-F9P та Unicore UM980
даються точність `0.01 м + 1 ppm CEP` у режимі RTK Fix замість `1.5-2.5 м` у звичайного
NEO-6M / NEO-M8N. Нота покриває повний ланцюжок: дводіапазонна антена → ровер на ESP32 →
NTRIP-клієнт через WiFi / Cat-1 → RTCM3-поправки від бази або NTRIP-кастера →
парсинг NMEA / UBX на ESP32.

База - це другий RTK-приймач у режимі `TIME` / `SURVEY-IN` з відомими координатами,
що віддає RTCM3 (1005/1077/1087/1097/1127/1230). Ровер - рухомий приймач, що приймає
ці поправки через UART, I2C, USB або NTRIP через інтернет. Результат: `Fix` (сантиметри),
`Float` (дециметри), `DGPS` (метр), `Single` (без поправок).

Зв'язок з базою знань: старт - [Home](../../../ESP32-Reference/Home.md), бюджетний GNSS - [03-SIM800L-GPS](../../../ESP32-Reference/12-Moduli-zvyazku/03-SIM800L-GPS.md),
радіоканал для поправок - [02-NRF24-LoRa](../../../ESP32-Reference/12-Moduli-zvyazku/02-NRF24-LoRa.md) та [09-Cellular-NBIoT-UARTLoRa](../../../ESP32-Reference/12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa.md),
UART - [UART](../../../ESP32-Reference/04-Shini/01-UART.md), живлення - [01-Lancjugi-zhivlennya](../../../ESP32-Reference/02-Zhivlennya/01-Lancjugi-zhivlennya.md),
продовження стільникової теми - [18-Cellular-LoRa-2](../../../ESP32-Reference/12-Moduli-zvyazku/18-Cellular-LoRa-2.md).

> САНТИМЕТРИ - ТІЛЬКИ З ДВОМА ДІАПАЗОНАМИ! Один L1-приймач (NEO-6M, ATGM336H)
> ніколи не дасть RTK Fix. Потрібні L1+L2 (ZED-F9P-00B/02B) або L1+L5 (ZED-F9P-15B,
> LC29H-BA/DA/EA, UM980). І друге: без поправок RTCM3 RTK-приймач = звичайний
> точний GNSS з точністю ~1 м. Поправки обов'язкові!

![](../../../ESP32-Reference/assets/img/gnss-rtk-zedf9p-scheme.png)
*Рис. RTK-система: база (нерухома антена + ZED-F9P) → NTRIP-кастер → ESP32 NTRIP-клієнт → ровер ZED-F9P/UM980. UART перехресно, антени з видом на небо.*

## Характеристики

| Модуль | Діапазони / сузір'я | Точність | Інтерфейс | Живлення | Ціна / ніша |
| --- | --- | --- | --- | --- | --- |
| u-blox ZED-F9P-02B | L1/L2: GPS L1C/A+L2C, GLO L1+L2, GAL E1+E5b, BDS B1+B2 | RTK 0.01 м + 1 ppm, сходимість <10 с, до 20 Гц | UART×2, USB, SPI, I2C (DDC), PPS | 2.7-3.6 В, ~70 мА | ~180-220 $, еталон для бази і ровера |
| u-blox ZED-F9P-15B | L1/L5: GPS L1+L5, GAL E1+E5a, BDS B1+B2a | RTK 0.01 м + 1 ppm, OSNMA, до 20 Гц | UART×2, USB, SPI, I2C, PPS | 2.7-3.6 В, ~70 мА | ~200 $, майбутнє (L5 чистіший) |
| Unicore UM980 | Всесузір'я всі частоти: GPS L1/L2/L5, BDS B1/B2/B3, GLO, GAL, QZSS, NavIC | RTK <5 с ініціалізація, 50 Гц, 1408 каналів | UART×3, I2C*, SPI*, PPS, EVENT, CAN* | 3.0-3.6 В, ~150 мА | ~60-90 $, дешевше F9P, 50 Гц! |
| Quectel LC29H-BA | L1+L5 GPS+GLO+GAL+BDS+QZSS, RTK + dead reckoning (IMU) | RTK сантиметри, автономно 1 м CEP | UART, I2C, SPI*, USB* | 3.1-3.6 В, ~40 мА | ~25-35 $, найдешевший RTK! |
| Quectel LC29H-DA | L1+L5, RTK 1 Гц | RTK сантиметри 1 Гц | UART, I2C | 3.1-3.6 В, ~40 мА | ~18-25 $, трекер з RTK |
| Quectel LC29H-EA | L1+L5, RTK 10 Гц + dual-antenna heading | RTK + курс 0.4° з двох антен | UART, I2C | 3.1-3.6 В | ~35-45 $, курс без компаса |
| Quectel LC29H-AA | L1+L5, стандартна точність (без RTK) | ~1 м CEP | UART, I2C | 3.1-3.6 В, low-power | ~10-15 $, апгрейд NEO-6M |
| ATGM336H (слон) | GPS+BDS L1, NMEA | 1.5-2 м | UART 9600 | 3.3 В, ~30 мА | ~3-5 $, бюджетний logger |
| u-blox NEO-M8N | GPS+GLO+GAL+BDS L1 | 2 м | UART, USB, I2C, PPS | 3.3 В | ~8-15 $, база для порівняння |
| u-blox M10 (M10050) | L1 всі сузір'я, low-power | 1.5 м, −160 дБм | UART, I2C | 3.3 В, ~15 мА | ~10 $, трекер на батареї |
| L76 / L86 Quectel | GPS+GLO L1, вбудована patch-антена | 2 м | UART | 3.3 В | ~8 $, прототип без антени |

Деталі вибору:

1. **База + ровер з нуля:** 2× ZED-F9P (або 2× UM980). Однакові антени на базі і ровері!
2. **Тільки ровер + публічний NTRIP:** 1× LC29H-BA або ZED-F9P + WiFi ESP32. Дешевше, бази не треба.
3. **Дрон / 50 Гц:** UM980 (ZED-F9P дає максимум 20 Гц RTK).
4. **Курс без магнітометра:** LC29H-EA з двома антенами (moving base) або 2× ZED-F9P у moving base.
5. **Бюджетний трекер без сантиметрів:** ATGM336H / NEO-M8N / LC29H-AA - див. [03-SIM800L-GPS](../../../ESP32-Reference/12-Moduli-zvyazku/03-SIM800L-GPS.md).
6. **Тунелі / паркінги:** тільки LC29H-BA/CA з dead reckoning (IMU) тримає трек без супутників.
7. **L2 чи L5?** L2 (F9P-02B) - сумісність зі старими базами; L5 (F9P-15B, LC29H) - чистіший сигнал, майбутнє, але база теж має видавати L5 (MSM7 1077/1097/1127).

## Легенда пінів модуля

### ZED-F9P (модуль LGA 17×22 мм / плата simpleRTK2B)

| Пін | Позначення | Тип | Куди на ESP32 | Примітка |
| --- | --- | --- | --- | --- |
| 1 | VCC 3V3 | Живлення вхід | 3V3 (окремий LDO, 200 мА запас!) | 2.7-3.6 В! НЕ 5V! Пульсації <50 мВ |
| 2 | GND | Земля | GND | Спільна земля + екран антени |
| 3 | TX1 (UART1 TX) | Вихід UART | GPIO16 (RX2 ESP32) | Перехресно TX→RX, 38400-115200 для NMEA, 115200+ для RTCM |
| 4 | RX1 (UART1 RX) | Вхід UART | GPIO17 (TX2 ESP32) | Сюди ллємо RTCM3 з NTRIP-клієнта! |
| 5 | TX2 / D_SEL | Вихід UART2 | GPIO4 (RX, опційно) | Другий порт: RTCM-вихід бази або UBX-лог |
| 6 | RX2 | Вхід UART2 | GPIO5 (TX, опційно) | Вхід поправок для бази |
| 7 | SDA (DDC/I2C) | Вхід/вихід OD | GPIO21 + pull-up 4.7к | u-center через I2C, адреса 0x42 |
| 8 | SCL (DDC/I2C) | Вхід OD | GPIO22 + pull-up 4.7к | 400 кГц максимум |
| 9 | USB_DP / USB_DM | USB | USB-UART / ПК безпосередньо | u-center + прошивка, 5V-толерантні через захист |
| 10 | TIMEPULSE (PPS) | Вихід цифровий | GPIO34 (тільки вхід!) | 1 Гц імпульс ±30 нс, для синхронізації |
| 11 | RESET_N | Вхід, active low | GPIO14 або кнопка | LOW ≥10 мс = перезапуск |
| 12 | SAFEBOOT_N | Вхід | NC (HIGH) | LOW при старті = safeboot для відновлення прошивки |
| 13 | V_BCKP | Живлення RTC | Батарейка CR1220 / 3V3 | Гарячий старт <5 с замість 30 с! |
| 14 | RF_IN | ВЧ-вхід | Активна дводіапазонна антена SMA | 50 Ом! DC-feed 3.3-5 В для LNA антени |
| 15 | ANT_DETECT | Вхід АЦП | Дільник з RF-тракту | Детект обриву / КЗ антени |
| 16 | ANT_OFF | Вихід | Ключ живлення антени | Вимикає feed при КЗ |

> Живлення антени: ZED-F9P плати (Ardusimple simpleRTK2B, SparkFun) мають перемичку
> `3V3 / 5V ANT POWER`. Активна антена ANN-MB потребує 3.3-5 В на RF_IN. Пасивна
> patch без LNA на RTK не працює стабільно - тільки активна!

### Unicore UM980 (LGA 22×17 мм / плата UM980 EVK)

| Пін | Позначення | Тип | Куди на ESP32 | Примітка |
| --- | --- | --- | --- | --- |
| 1 | VCC | Живлення вхід | 3V3 500 мА | 3.0-3.6 В, пік при старті! |
| 2 | GND | Земля | GND | Спільна земля |
| 3 | UART1_TX | Вихід UART | GPIO16 (RX2) | NMEA 115200 за замовчуванням |
| 4 | UART1_RX | Вхід UART | GPIO17 (TX2) | RTCM3 вхід сюди |
| 5 | UART2_TX | Вихід UART | GPIO4 (опційно) | Raw / debug |
| 6 | UART2_RX | Вхід UART | GPIO5 (опційно) | Конфігурація |
| 7 | UART3_TX/RX | UART | NC або логер | Третій порт для бази |
| 8 | PPS | Вихід | GPIO34 | 1PPS, ширина/полярність настроювані |
| 9 | EVENT | Вхід | GPIO35 (опційно) | Мітка події для фотограмметрії |
| 10 | RESET_N | Вхід, active low | GPIO14 | LOW ≥5 мс = скид |
| 11 | RF_IN | ВЧ-вхід | Активна антена | Зовнішнє живлення антени! UM980 сам НЕ живить LNA - потрібен bias-tee! |
| 12 | V_BCKP | RTC | Батарейка | Гарячий старт |

> UM980 НЕ видає живлення на антену зсередини (на відміну від ZED-F9P плат)!
> Став bias-tee або активну антену з окремим інжектором 3.3 В. Інакше - тиша в ефірі.

### Quectel LC29H (LCC 16×12.2 мм)

| Пін | Позначення | Тип | Куди на ESP32 | Примітка |
| --- | --- | --- | --- | --- |
| 1 | VCC | Живлення вхід | 3V3 | 3.1-3.6 В, типово 3.3 В |
| 2 | GND | Земля | GND | Земля |
| 3 | TXD (UART) | Вихід UART | GPIO16 (RX2) | NMEA 115200, протоколи NMEA/PAIR/PQTM |
| 4 | RXD (UART) | Вхід UART | GPIO17 (TX2) | Команди `$PQTM*`, RTCM вхід (BA/DA/EA) |
| 5 | SDA / SPI_MOSI* | I2C/SPI | GPIO21 | Залежить від прошивки |
| 6 | SCL / SPI_CLK* | I2C/SPI | GPIO22 | 1.8 В домен на деяких пінах - читати Hardware Design! |
| 7 | PPS | Вихід | GPIO34 | 1PPS <100 нс |
| 8 | RESET_N | Вхід | GPIO14 або NC | Скид |
| 9 | ANT | ВЧ-вхід | Активна L1+L5 антена | Зовнішній LNA; short/open детект є |
| 10 | D_SEL1/D_SEL2 | Вхід конфіг | GND/VCC перемички | Вибір UART/I2C/SPI при старті |

### Бюджетні ATGM336H / NEO-M8N (UART 9600/115200)

| Пін | Позначення | Тип | Куди на ESP32 | Примітка |
| --- | --- | --- | --- | --- |
| 1 | VCC | Живлення | 3V3 (ATGM336H) / 3.3-5V (NEO плата з LDO) | Перевірити LDO на платі! |
| 2 | GND | Земля | GND | Спільна |
| 3 | TX | Вихід UART | GPIO16 (RX2) | NMEA 9600 (ATGM336H) або 9600/115200 (NEO) |
| 4 | RX | Вхід UART | GPIO17 (TX2) | Конфігурація |
| 5 | PPS | Вихід | GPIO34 (опційно) | Є на NEO, немає на ATGM336H |
| 6 | ANT | ВЧ | Керамічна patch / IPEX | ATGM336H має вбудовану антену - тримати до неба! |

## Схема

### ASCII-схема

```text
ЖИВЛЕННЯ (зірка заземлення!):
  5V 2A ──► [buck 5→3.3V / LDO AMS1117] ──► VCC ESP32 DevKit
                                        ──► VCC ZED-F9P (3.3V, пульсації <50мВ!)
                                        ──► bias-tee 3.3V ──► активна антена (якщо UM980/LC29H)
  GND спільна, товсті дроти, екран антени на GND біля RF_IN!

РОВЕР (NTRIP через WiFi ESP32):
  Небо ──► [активна L1/L2 антена ANN-MB + ground plane 10см] ──► RF_IN ZED-F9P
  ZED-F9P UART1:
    TX1 ──────────────► GPIO16 (RX2 ESP32)   NMEA+UBX 115200
    RX1 ◄────────────── GPIO17 (TX2 ESP32)   RTCM3 від NTRIP-клієнта
    PPS ──────────────► GPIO34 (опційно)     мітка часу
    USB ──────────────► ПК (u-center, конфіг)
  ESP32 ──WiFi──► NTRIP-кастер (rtk2go.com:2101 / власний) ──► RTCM3 ──► RX1 ровера

БАЗА (власний кастер через ESP32 або ПК):
  Небо ──► [активна антена на даху, ground plane!] ──► RF_IN ZED-F9P №2
  ZED-F9P №2 UART2 (база, режим SURVEY-IN/TIME):
    TX2 ──► GPIO4 ESP32 / ПК ──► str2str ──► NTRIP-кастер (mountpoint /BASE)
  Координати бази: survey-in 60с / 2м АБО точні ECEF з геодезії!

ВАРІАНТ БЕЗ ІНТЕРНЕТУ (радіоміст поправок):
  База TX2 (RTCM 1005+1077+1087+1097+1127) ──► LoRa E22 868МГц ──повітря──► LoRa E22 ──► RX1 ровера
  Див. [[12-Moduli-zvyazku/02-NRF24-LoRa]] та [[12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa]]

I2C-Варіант (u-center без USB):
  ZED-F9P SDA ──[4.7к]──► GPIO21, SCL ──[4.7к]──► GPIO22, адреса 0x42
```

### Mermaid

```mermaid
graph LR
    SKY((Супутники<br/>GPS+GLO+GAL+BDS)) -->|L1/L2 або L1/L5| ANT_B[Активна антена бази<br/>+ ground plane]
    SKY -->|L1/L2 або L1/L5| ANT_R[Активна антена ровера<br/>+ ground plane]
    ANT_B -->|RF 50 Ом| BASE[ZED-F9P База<br/>SURVEY-IN/TIME]
    BASE -->|UART2 RTCM3<br/>1005/1077/1087/1097| ESPB[ESP32 бази / ПК str2str]
    ESPB -->|TCP/IP| CASTER[NTRIP-кастер<br/>rtk2go / власний]
    CASTER -->|WiFi/Cat-1<br/>NTRIP-клієнт| ESPR[ESP32 ровер<br/>NTRIP-клієнт]
    ESPR -->|UART RTCM3<br/>GPIO17→RX1| ROVER[ZED-F9P/UM980 Ровер]
    ANT_R -->|RF 50 Ом| ROVER
    ROVER -->|UART NMEA/UBX<br/>TX1→GPIO16| ESPR
    ROVER -->|PPS| ESPR
    ESPR -->|USB-лог| PC[ПК RTKLIB/u-center]
    BASE -->|USB| PC
```

## NMEA vs UBX vs RTCM3 - три мови GNSS

| Протокол | Напрям | Приклад | Призначення |
| --- | --- | --- | --- |
| NMEA-0183 ASCII | Модуль → ESP32 | `$GNGGA,123519,4807.038,N,01131.000,E,4,12,0.9,545.4,M,,*47` | Позиція для людини/карти. Поле fix: 1=Single, 2=DGPS, 4=RTK Fix, 5=RTK Float! |
| UBX бінарний (u-blox) | Обидва | `B5 62 01 3C ...` NAV-RELPOSNED | Конфігурація, carrier-phase, точний статус RTK. Тільки u-blox! |
| Unicore binary | Обидва | `$GPTXT...` / binary | Конфігурація UM980, аналог UBX |
| PQTM (Quectel) | Обидва | `$PQTMCFG...` | Конфігурація LC29H |
| RTCM3 бінарний | База/кастер → ровер | `D3 00 13 3E ...` type 1077 | Поправки! 1005=координати бази, 1077/1087/1097/1127=MSM спостереження, 1230=GLONASS bias |

NMEA читаємо, RTCM3 пишемо всліпу в RX ровера, UBX - для конфігурації.
RTCM3 не парсимо на ESP32 - просто пересилаємо байти з NTRIP-с blom сокета в UART!

Приклад NMEA GGA з RTK Fix:

```text
$GNGGA,101230.00,5041.1234567,N,03030.7654321,E,4,21,0.6,183.42,M,0.0,M,,*5A
         час      широта           довгота            ^ ^  ^   висота
                                              fix=4=RTK Fix (сантиметри!)
                                              супутників=21, HDOP=0.6
fix: 0=нема, 1=Single(метри), 2=DGPS(субметр), 4=Fix(см!), 5=Float(дм), 6=dead reckoning
```

## RTK база + ровер - режими

1. **Survey-in (для старту):** база усереднює свою позицію 60-300 с з точністю 1-2 м.
   Команда UBX `CFG-TMODE3`: `survey-in, minDur=60s, accLimit=2000мм`. Просто, але абсолютна
   точність ровера = точність бази. Для автопілота/агро - достатньо.
2. **Fixed TIME (для роботи):** вводимо точні ECEF-координати бази (з геодезії або PPP).
   Тоді ровер дає абсолютні сантиметри. Формат: `UBX-CFG-TMODE3, mode=FIXED, ecefX/Y/Z`.
3. **Moving base (курс):** два приймачі на одній платформі, база шле RTCM3 роверу безпосередньо
   по UART. Ровер видає `UBX-NAV-RELPOSNED` - вектор між антенами (курс 0.4° при базі 1 м).
4. **NTRIP (через інтернет):** база шле в кастер (`str2str -in serial -out ntrips`),
   ровер забирає (`ntrip://user:pass@caster:2101/MOUNT`). ESP32 робить те саме кодом нижче.
5. **Радіоміст (без інтернету):** RTCM3 з TX2 бази → LoRa E22 → RX1 ровера. Швидкість повітря
   ≥9600 бод, RTCM ~1-3 кБ/с. Див. [02-NRF24-LoRa](../../../ESP32-Reference/12-Moduli-zvyazku/02-NRF24-LoRa.md).

Мінімальний набір RTCM3 для ZED-F9P/UM980: `1005 (1с) + 1077 (1с) + 1087 (1с) + 1097 (1с) + 1127 (1с) + 1230 (5с)`.
Без 1230 GLONASS не зафіксується! Перевірка в u-center: View → Messages → RXM-RTCM.

## Антени - половина RTK

1. **Тільки активна дводіапазонна:** ANN-MB (L1/L2), ANN-MB1 (L1/L5), Harxon HX-CH3602,
   ArduSimple AS-ANT2B-HEL-42-SMA. Пасивна patch з AliExpress вбиває Fix.
2. **Ground plane обов'язковий:** металевий диск/квадрат 10×10 см під антеною.
   Без нього багатопроменевість (multipath) зриває Fix у Float. На даху - сам дах працює.
3. **Вид на небо 360°:** мінімум 15° над горизонтом чисто. Балкон/вікно = Float назавжди.
4. **Кабель короткий:** втрати 1 дБ/м на RG174. Довше 3 м - тільки з активним LNA 28 дБ.
5. **База і ровер - однакові антени:** різні фазові центри дають зсув у сантиметри.
6. **Живлення LNA:** ZED-F9P плати дають 3.3/5 В на RF (перемичка); UM980/LC29H - тільки
   зовнішній bias-tee! Перевірити струм ~10-20 мА.
7. **НЕ поряд з LTE-антеною:** рознести ≥20 см, інакше десенс (забивання LNA).

## Інтерфейси: UART vs I2C vs USB

| Інтерфейс | Швидкість | Коли використовувати |
| --- | --- | --- |
| UART1 (NMEA+RTCM) | 115200-460800 | Основний канал ESP32. RTCM в RX, NMEA з TX одночасно! |
| UART2 (RTCM out, база) | 115200 | Вихід поправок з бази на ESP32/радіо |
| USB | 12 Мбіт | u-center, прошивка, лог UBX на ПК |
| I2C (DDC) 0x42 | 400 кГц | Два пристрої на шині, економія UART ESP32 |
| SPI | 5 МГц | Лог raw-даних на SD на високій швидкості |
| PPS | 1 Гц | Синхронізація камери / лідара / другого MCU |

> ESP32 має 3 UART: UART0=USB-лог, UART1=вільний (але піни конфліктують з flash!),
> UART2=основний для GNSS. Використовуй UART2 (GPIO16/17) для ровера.

## RTKLIB та u-center - оглядово

- **u-center (Windows, безкоштовно):** конфігурація ZED-F9P, вид супутників, survey-in,
  запис UBX-логів, оновлення прошивки HPG. Вкладки: UBX-CFG-TMODE3 (база), UBX-CFG-MSG
  (увімкнути RXM-RTCM + NAV-RELPOSNED), UBX-CFG-PRT (бод UART). Для M10/LC29H - u-center 2.
- **RTKLIB (Takasu, open source):** `RTKNAVI` (RTK у реальному часі з NTRIP),
  `STRSVR` (міст COM→NTRIP-кастер), `RTKPOST` (постобробка RINEX), `STREN`/`STR2STR`
  (консольний міст для бази на Linux). Якщо приймач без вбудованого RTK (NEO-M8T) -
  RTKLIB рахує Fix на ПК. З F9P/UM980 - RTKLIB потрібен тільки для логів і бази.
- **Типові команди str2str для бази:**
  `str2str -in serial://COM5:115200 -out ntrips://user:pass@rtk2go.com:2101/MOUNT -msg "1005(1),1077(1),1087(1),1097(1),1127(1),1230(5)"`

## Код ESP-IDF (UART + NTRIP-клієнт + пересилка RTCM)

```c
// ESP-IDF v5.x: NTRIP-клієнт на ESP32, RTCM з сокета -> UART2 (RX1 ровера), NMEA з UART2 -> лог
// Піни: GPIO16=RX2 (TX1 модуля), GPIO17=TX2 (RX1 модуля). WiFi -> rtk2go.com:2101
#include <string.h>
#include <sys/socket.h>
#include <netdb.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "esp_wifi.h"
#include "nvs_flash.h"
#include "driver/uart.h"
#include "mbedtls/base64.h"

#define TAG "rtk_ntrip"
#define UART_NUM UART_NUM_2
#define PIN_TX 17
#define PIN_RX 16
#define NTRIP_HOST "rtk2go.com"
#define NTRIP_PORT "2101"
#define NTRIP_MOUNT "/KYIV-MOUNT"
#define NTRIP_USER "user"
#define NTRIP_PASS "pass"
#define GGA_FIX " $GNGGA,101230.00,5041.1234,N,03030.7654,E,1,08,1.0,180.0,M,0,M,,*00\r\n"

static int ntrip_sock = -1;

static void uart_init_gnss(void) {
    uart_config_t cfg = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
        .source_clk = UART_SCLK_DEFAULT,
    };
    ESP_ERROR_CHECK(uart_driver_install(UART_NUM, 4096, 4096, 0, NULL, 0));
    ESP_ERROR_CHECK(uart_param_config(UART_NUM, &cfg));
    ESP_ERROR_CHECK(uart_set_pin(UART_NUM, PIN_TX, PIN_RX, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE));
}

// GGA потрібна кастеру для VRS / найближчої бази — шлемо раз на 10 с
static void send_gga(void) {
    if (ntrip_sock >= 0) send(ntrip_sock, GGA_FIX, strlen(GGA_FIX), 0);
}

static bool ntrip_connect(void) {
    struct addrinfo hints = { .ai_family = AF_INET, .ai_socktype = SOCK_STREAM };
    struct addrinfo *res = NULL;
    if (getaddrinfo(NTRIP_HOST, NTRIP_PORT, &hints, &res) != 0) return false;
    ntrip_sock = socket(res->ai_family, res->ai_socktype, 0);
    if (ntrip_sock < 0) { freeaddrinfo(res); return false; }
    if (connect(ntrip_sock, res->ai_addr, res->ai_addrlen) != 0) {
        close(ntrip_sock); ntrip_sock = -1; freeaddrinfo(res); return false;
    }
    freeaddrinfo(res);
    char creds[128], b64[192]; size_t olen = 0;
    snprintf(creds, sizeof(creds), "%s:%s", NTRIP_USER, NTRIP_PASS);
    mbedtls_base64_encode((unsigned char*)b64, sizeof(b64), &olen,
                          (unsigned char*)creds, strlen(creds));
    char req[512];
    snprintf(req, sizeof(req),
        "GET %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: ESP32-NTRIP/1.0\r\n"
        "Authorization: Basic %s\r\nNtrip-Version: Ntrip/2.0\r\nConnection: close\r\n\r\n",
        NTRIP_MOUNT, NTRIP_HOST, b64);
    send(ntrip_sock, req, strlen(req), 0);
    char hdr[512]; int n = recv(ntrip_sock, hdr, sizeof(hdr) - 1, 0);
    if (n <= 0) return false;
    hdr[n] = 0;
    ESP_LOGI(TAG, "NTRIP hdr: %.60s", hdr);
    return (strstr(hdr, "200") != NULL || strstr(hdr, "ICY 200") != NULL);
}

// RTCM з мережі -> UART ровера; NMEA з UART -> лог (шукаємо fix=4)
static void ntrip_task(void *arg) {
    uint8_t net[1024], u[512];
    TickType_t last_gga = 0;
    while (1) {
        if (ntrip_sock < 0) {
            ESP_LOGI(TAG, "NTRIP reconnect...");
            if (!ntrip_connect()) { vTaskDelay(pdMS_TO_TICKS(5000)); continue; }
            ESP_LOGI(TAG, "NTRIP connected, streaming RTCM");
        }
        if ((xTaskGetTickCount() - last_gga) > pdMS_TO_TICKS(10000)) {
            send_gga(); last_gga = xTaskGetTickCount();
        }
        struct timeval tv = { .tv_sec = 0, .tv_usec = 200000 };
        setsockopt(ntrip_sock, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
        int n = recv(ntrip_sock, net, sizeof(net), 0);
        if (n > 0) uart_write_bytes(UART_NUM, (char*)net, n);  // RTCM -> ровер всліпу!
        else if (n == 0) { close(ntrip_sock); ntrip_sock = -1; continue; }
        int m = uart_read_bytes(UART_NUM, u, sizeof(u) - 1, pdMS_TO_TICKS(20));
        if (m > 0) {
            u[m] = 0;
            if (strstr((char*)u, "$GNGGA")) ESP_LOGI(TAG, "NMEA: %.100s", (char*)u);
        }
    }
}

void app_main(void) {
    nvs_flash_init();
    // TODO: підключити WiFi (див. приклад wifi/station), потім:
    uart_init_gnss();
    xTaskCreate(ntrip_task, "ntrip", 8192, NULL, 5, NULL);
}
```

## Код Arduino (ровер: читання GGA + детект Fix/Float)

```cpp
// Arduino-ESP32: ровер ZED-F9P/UM980/LC29H через Serial2, детект RTK Fix з GGA
// Піни: RX2=GPIO16 (TX модуля), TX2=GPIO17 (RX модуля)
#include <Arduino.h>
#define GNSS_RX 16
#define GNSS_TX 17

String uartBuf;

void setup() {
  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, GNSS_RX, GNSS_TX);
  Serial.println("RTK rover: чекаю GGA...");
  // LC29H: увімкнути RTK (приклад PQTM-команди, деталі в Protocol Spec)
  // Serial2.println("$PQTMCFGOUTPUT,W,1,1,GGA,1*xx");
  delay(1000);
}

// Парсинг GGA: $GNGGA,час,шир,N/S,дов,E/W,fix,сат,hdop,вис,...
void parseGGA(const String &line) {
  // Розбиваємо по комах
  int idx[15]; int n = 0;
  for (int i = 0; i < (int)line.length() && n < 15; i++)
    if (line[i] == ',') idx[n++] = i;
  if (n < 10) return;
  int fix = line.substring(idx[5] + 1, idx[6]).toInt();
  String sats = line.substring(idx[6] + 1, idx[7]);
  String hdop = line.substring(idx[7] + 1, idx[8]);
  String lat = line.substring(idx[1] + 1, idx[2]);
  String lon = line.substring(idx[3] + 1, idx[4]);
  const char *st = "?";
  if (fix == 4) st = "FIX (см!)";
  else if (fix == 5) st = "FLOAT (дм)";
  else if (fix == 2) st = "DGPS (м)";
  else if (fix == 1) st = "SINGLE (метри)";
  else if (fix == 6) st = "DEAD RECKONING";
  Serial.printf("GGA fix=%d [%s] sat=%s hdop=%s lat=%s lon=%s\n",
                fix, st, sats.c_str(), hdop.c_str(), lat.c_str(), lon.c_str());
  if (fix == 4) Serial.println(">>> RTK FIX — можна їхати/міряти!");
}

void loop() {
  while (Serial2.available()) {
    char c = Serial2.read();
    if (c == '\n') {
      uartBuf.trim();
      if (uartBuf.startsWith("$GNGGA") || uartBuf.startsWith("$GPGGA"))
        parseGGA(uartBuf);
      uartBuf = "";
    } else if (c != '\r') {
      uartBuf += c;
      if (uartBuf.length() > 200) uartBuf = "";  // захист від сміття
    }
  }
  // Міст USB<->GNSS для u-center: все з Serial в Serial2
  while (Serial.available()) Serial2.write(Serial.read());
}
```

## Код MicroPython (парсинг NMEA + запит поправок)

```python
"""MicroPython ESP32: читання GGA з ZED-F9P/UM980, оцінка Fix, LED-індикація."""
from machine import UART, Pin
import time

uart = UART(2, baudrate=115200, tx=17, rx=16, timeout=100)
led_fix = Pin(2, Pin.OUT)  # синій LED: горить = FIX

def parse_gga(line):
    try:
        p = line.split(",")
        if len(p) < 10 or p[0][-3:] != "GGA":
            return None
        fix = int(p[6]) if p[6] else 0
        sats = p[7]
        lat = p[2] + p[3]
        lon = p[4] + p[5]
        return fix, sats, lat, lon
    except Exception:
        return None

names = {0: "NO FIX", 1: "SINGLE", 2: "DGPS", 4: "FIX см!", 5: "FLOAT дм", 6: "DR"}

print("RTK rover MicroPython: чекаю GGA...")
buf = b""
while True:
    if uart.any():
        buf += uart.read(uart.any())
        while b"\n" in buf:
            line, buf = buf.split(b"\n", 1)
            try:
                s = line.decode().strip()
            except Exception:
                continue
            if "GGA" in s:
                r = parse_gga(s)
                if r:
                    fix, sats, lat, lon = r
                    print("{} sat={} lat={} lon={} [{}]".format(
                        s[:20], sats, lat, lon, names.get(fix, fix)))
                    led_fix.value(1 if fix == 4 else 0)
    time.sleep_ms(20)
```

## Типові помилки

| № | Симптом | Причина | Виправлення |
| --- | --- | --- | --- |
| 1 | Ніколи немає Fix, тільки Float/Single | Пасивна або однодіапазонна антена | Тільки активна L1/L2 або L1/L5 + перевірити струм LNA |
| 2 | Fix є на столі, в полі зривається | Немає ground plane, multipath | Підкласти метал 10×10 см під антену |
| 3 | RTCM йде, але ровер мовчить | RTCM ллється не в той UART (UART2 замість UART1 RX) | Поправки строго в RX1 (той же порт, що й NMEA-вихід) |
| 4 | NTRIP 401 Unauthorized | Невірний логін/паря mountpoint | Перевірити `user:pass`, mountpoint з малої літери, sourcetable |
| 5 | NTRIP рветься кожні 30 с | Не шлемо GGA кастеру (VRS вимагає позицію) | Шлити GGA раз на 5-10 с (див. ESP-IDF код) |
| 6 | Бод 9600 і RTCM не влазить | UART ровера 9600 - RTCM потік 2-3 кБ/с губиться | Підняти UART до 115200+ з обох боків |
| 7 | UM980 взагалі не бачить супутників | Немає живлення антени (UM980 не дає bias!) | Додати bias-tee 3.3 В або активну антену з інжектором |
| 8 | ZED-F9P гріється / не стартує | Подали 5V на VCC (максимум 3.6 В!) | Тільки 3.3 В, перевірити перемичку ANT POWER ≠ VCC |
| 9 | База в survey-in роками | Поганий вид неба / accLimit занадто строгий | minDur=60 с, accLimit=2000 мм, антену на дах |
| 10 | GLONASS не фіксується | Немає RTCM 1230 (GLONASS bias) | Додати 1230 з періодом 5 с у str2str / кастер |
| 11 | L5-ровер + стара база = немає Fix | База не видає MSM для L5 (тільки 1004/1012!) | База має видавати MSM7: 1077+1087+1097+1127 |
| 12 | I2C мовчить (NACK 0x42) | Немає pull-up або D_SEL у SPI-режимі | Pull-up 4.7к на SDA/SCL, перевірити D_SEL перемички |
| 13 | PPS джитер / немає імпульсу | PPS не увімкнено в CFG-TP5 або пін не підтягнуто | Увімкнути TIMEPULSE в u-center, rate=1 Гц |
| 14 | ESP32 ребутиться при старті GNSS | Просадка 3.3 В (UM980 бере пік!) | Окремий LDO 500 мА + 100 мкФ біля модуля |

## Офіційні джерела

> Усі URL нижче перевірені через webfetch 2026-09-29. Вгадані посилання заборонені.

1. u-blox ZED-F9P - сторінка продукту, варіанти 02B/04B/05B/15B, L1/L2 vs L1/L5, інтерфейси - <https://www.u-blox.com/en/product/zed-f9p-module>
2. Unicore UM980 - all-constellation multi-frequency RTK-модуль, NebulasIV, 1408 каналів - <https://en.unicore.com/products/um980>
3. Quectel LC29H series - варіанти AA/BA/CA/DA/EA, L1+L5, RTK + dead reckoning - <https://www.quectel.com/product/gnss-lc29h/>
4. RTKLIB (Tomoji Takasu) - open source пакет RTK: RTKNAVI/STRSVR/RTKPOST/STR2STR, GitHub - <https://github.com/tomojitakasu/RTKLIB>
5. u-blox u-center - ПЗ оцінки GNSS для M8/M9/F9, конфігурація і логи - <https://www.u-blox.com/en/product/u-center>
6. BKG NTRIP - документація протоколу Networked Transport of RTCM via Internet Protocol, кастери, RTCM3 MSM - <https://igs.bkg.bund.de/ntrip>
7. ESP-IDF UART - драйвер UART ESP32: uart_param_config, uart_set_pin, події, приклади включно з nmea0183_parser - <https://docs.espressif.com/projects/esp-idf/en/v5.5/esp32/api-reference/peripherals/uart.html>
8. Unicore UM980 - all-constellation multi-frequency RTK-модуль NebulasIV, 1408 каналів, L1/L2/L5 - <https://en.unicore.com/products/um980>
9. Quectel LC29H series - варіанти AA/BA/CA/DA/EA/BS, L1+L5, RTK + dead reckoning, moving base - <https://www.quectel.com/product/gnss-lc29h/>
10. Semtech SX1280 - LoRa 2.4 ГГц трансивер з ranging time-of-flight, документи AN1200.29/AN1200.50 - <https://www.semtech.com/products/wireless-rf/lora-connect/sx1280>
11. Semtech LR1121 - sub-GHz + 2.4 ГГц + S-band/L-band супутник, LR-FHSS, LoRaWAN - <https://www.semtech.com/products/wireless-rf/lora-connect/lr1121>
12. RAK3172 WisDuo datasheet - STM32WLE5, LoRaWAN 1.0.3, AT RUI3, P2P, 1.69 мкА сон - <https://docs.rakwireless.com/product-categories/wisduo/rak3172-module/datasheet>

## NMEA-речення повна шпаргалка (GGA/RMC/GSV/GSA/VTG/ZDA)

NMEA-0183 v4.11 - ASCII-рядки `$...*CHK CRLF`, бод 9600-115200. Контрольна сума:
XOR усіх байтів між `$` і `*`. ESP32 перевіряє її перед парсингом, інакше сміття
з UART дасть стрибок позиції на кілометри.

Розрахунок контрольної суми (Arduino):

```cpp
bool nmeaCheck(const String &line) {
  int a = line.indexOf('*');
  if (line[0] != '$' || a < 0) return false;
  uint8_t cs = 0;
  for (int i = 1; i < a; i++) cs ^= line[i];
  uint8_t ref = strtoul(line.substring(a + 1, a + 3).c_str(), NULL, 16);
  return cs == ref;
}
```

### GGA - Global Positioning System Fix Data (головне!)

Період 1-10 Гц, приклад:

```text
$GNGGA,101230.00,5041.1234567,N,03030.7654321,E,4,21,0.6,183.42,M,0.0,M,,*5A
```

| Поле | Приклад | Розшифровка |
| --- | --- | --- |
| 0 префікс | `$GNGGA` | GN=всесузір'я, GP=GPS, GL=GLO, GA=GAL, GB=BDS |
| 1 UTC | `101230.00` | 10:12:30.00 UTC |
| 2 широта | `5041.1234567` | 50° + 41.1234567′ = 50.68539° |
| 3 півкуля | `N` | N/S |
| 4 довгота | `03030.7654321` | 030° + 30.7654321′ = 30.51275° |
| 5 півкуля | `E` | E/W |
| 6 fix | `4` | 0=немає, 1=Single, 2=DGPS, 4=RTK Fix!, 5=Float, 6=DR |
| 7 супутники | `21` | використано в рішенні; <8 = погано, >15 = добре |
| 8 HDOP | `0.6` | <0.8=відмінно, 1-2=норма, >5=місто/ліс |
| 9 висота | `183.42,M` | над еліпсоїдом WGS84, метри |
| 10 геоїд | `0.0,M` | різниця геоїд-еліпсоїд (в Україні ~+15…+25 м!) |
| 11 вік DGPS | `` | секунд з останньої RTCM (порожньо в RTK) |
| 12 ID станції | `` | ID бази |
| 13 checksum | `*5A` | XOR |

Переведення NMEA-координат у градуси:

```cpp
double nmeaToDeg(const String &dm) {
  double v = dm.toDouble();
  int d = (int)(v / 100);
  return d + (v - d * 100) / 60.0;
}
// 5041.1234567 -> 50 + 41.1234567/60 = 50.6853909
```

### RMC - Recommended Minimum (швидкість + дата)

```text
$GNRMC,101230.00,A,5041.1234,N,03030.7654,E,0.45,183.2,290926,,,A,V*12
```

| Поле | Значення |
| --- | --- |
| 1 UTC | час фікса |
| 2 статус | A=active (є фікс), V=void |
| 3-6 шир/дов | як у GGA |
| 7 швидкість | вузли (1 вузол=1.852 км/г); 0.45=0.83 км/г пішохід |
| 8 курс | градуси 0-360 |
| 9 дата | 29.09.26 |
| 10 магн. відм. | звичайно порожньо |
| 11 режим | A=autonomous, D=DGPS, F=RTK Float, R=RTK Fix, N=none |
| 12 статус | A/V навігаційний статус |

RMC - єдине речення з датою! Для логера треку обов'язкові GGA+RMC.

### GSV - Satellites in View (вид неба)

```text
$GPGSV,3,1,11,02,45,123,42,05,30,045,40,07,60,200,45,08,15,300,38*7A
$GPGSV,3,2,11,...
$GPGSV,3,3,11,...
```

| Поле | Значення |
| --- | --- |
| 1 всього повідомлень | 3 рядки на епоху |
| 2 номер рядка | 1..3 |
| 3 всього супутників | 11 видно |
| 4×(PRN, elev, azim, CN0) | PRN=номер, elev=висота° над горизонтом, azim=азимут°, CN0=дБ-Гц |

CN0-орієнтир: `>45`=чисте небо, `35-45`=норма, `25-35`=місто/вікно, `<25`=відбиття.
Для RTK треба ≥12 супутників з CN0>38 на L1+L2/L5. GSV шлють пачками по 4 сузір'ях:
GPGSV (GPS), GLGSV (GLO), GAGSV (GAL), GBGSV (BDS) - на ESP32 рахуй суму!

### GSA - DOP and Active Satellites

```text
$GNGSA,A,3,02,05,07,08,10,13,15,20,,,,,,1.2,0.6,1.0*33
```

| Поле | Значення |
| --- | --- |
| 1 режим | M=ручний, A=авто 2D/3D |
| 2 фікс | 1=немає, 2=2D, 3=3D |
| 3-14 PRN | до 12 номерів активних супутників |
| 15 PDOP | 3D-точність; <2 добре, >6 погано |
| 16 HDOP | горизонтальна; дублює GGA |
| 17 VDOP | вертикальна; завжди гірша за HDOP у 1.5 раза |

### VTG - Track and Ground Speed

```text
$GNVTG,183.2,T,,M,0.45,N,0.83,K,A*23
```

| Поле | Значення |
| --- | --- |
| 1 курс | 183.2° true |
| 2 T | true north |
| 3-4 магн. курс | звичайно порожньо |
| 5-6 швидкість вузли | 0.45 N |
| 7-8 швидкість км/г | 0.83 K - бери це для спідометра! |
| 9 режим | A/D/F/R як у RMC |

### ZDA + GLL + TXT (допоміжні)

```text
$GNZDA,101230.00,29,09,2026,00,00*4F
$GNGLL,5041.1234,N,03030.7654,E,101230.00,A,A*6B
$GPTXT,01,01,02,ANTSTATUS=OK*3B
```

| Речення | Поля |
| --- | --- |
| ZDA | UTC + день/місяць/рік + зона; точний час для RTC ESP32! |
| GLL | шир/дов + UTC + статус; коротший за GGA, без висоти |
| TXT | текстові повідомлення приймача (ANTSTATUS,ujian) |
| GST | статистика помилок lat/lon/alt RMS - для геодезії! |
| HDT | істинний курс від moving-base (дві антени) |

Практика на ESP32: увімкни тільки `GGA+RMC+GSV+GSA+VTG 1 Гц`, решту вимкни -
заощадиш 60% трафіку UART. У u-center UBX-CFG-MSG вимикає непотрібні NMEA.

## UBX-CFG ключові повідомлення (u-blox бінарний протокол)

Структура: `B5 62 CLASS ID LEN(LE) PAYLOAD CK_A CK_B`, де CK - 8-біт Fletcher.
Швидкість вища за NMEA, плюс carrier-phase. Класи: `0x06=CFG, 0x01=NAV, 0x02=RXM, 0x0B=AID`.

| Повідомлення | CLASS/ID | Призначення |
| --- | --- | --- |
| CFG-PRT | 06 00 | бод/протокол UART1/UART2/USB/I2C; напр. UART1 115200 NMEA+UBX+RTCM3 |
| CFG-MSG | 06 01 | періодичність кожного NMEA/UBX на кожному порту |
| CFG-RATE | 06 08 | частота навігації 1-20 Гц (measRate мс + navRate циклів) |
| CFG-TP5 | 06 31 | PPS: частота, ширина, полярність, прив'язка до UTC/GPS |
| CFG-TMODE3 | 06 71 | режим бази: 0=off, 1=survey-in, 2=fixed ECEF! |
| CFG-VALSET | 06 8A | нова система конфігурації (F9P FW≥1.0): ключ+значення, RAM/BBR/flash шари |
| CFG-VALGET | 06 8B | читання ключа конфігурації |
| CFG-VALDEL | 06 8C | скид до дефолту |
| CFG-CFG | 06 09 | зберегти в flash/BBR, заводський скид |
| NAV-PVT | 01 07 | все в одному: lat/lon/hMSL/fix/спутники/швидкість - парси це замість NMEA! |
| NAV-RELPOSNED | 01 3C | вектор moving-base: relPosN/E/D см + heading° - курс без компаса! |
| NAV-SVIN | 01 3B | статус survey-in: meanX/Y/Z, cAcc мм, valid flag |
| RXM-RTCM | 02 32 | лічильник прийнятих RTCM3: який тип дійшов, CRC-ok/fail |
| MON-HW | 0A 09 | шум, AGC, детект антени (open/short/ok) |
| MON-RF | 0A 38 | CN0 по діапазонах, jamming-індикатор |
| NAV-SAT | 01 35 | детально по кожному супутнику: PRN, elev, azim, CN0, used/fix |
| TIM-TOS | 0D 12 | синхронізація часу для PPS |

Приклад CFG-VALSET (вимкнути NMEA GLL на UART1, ключ `0x209100CA`):

```text
B5 62 06 8A 09 00 00 01 00 00 CA 00 91 20 00 5F 9B
версія=0 шари=RAM+BBR ключі=1 [ключ LE][значення 0] CK_A CK_B
```

Порада: не пиши байти вручну - використай `pyubx2` на ПК (`pip install pyubx2`),
сформуй повідомлення скриптом і скопіюй hex у прошивку ESP32. Для UM980 аналог -
команди `$CFG` ASCII, для LC29H - `$PQTMCFG*` (див. Protocol Specification).

NAV-PVT розбір на ESP32 (скорочено, little-endian з 0):

```c
// ubx 01 07 len 92: iTOW U4, year U2..., fixType U1[20], numSV U1[23],
// lon I4[24]/1e-7, lat I4[28]/1e-7, hMSL I4[36] мм, gSpeed I4[60] мм/с
int32_t lon = (int32_t)(p[24]|p[25]<<8|p[26]<<16|p[27]<<24);
double lat = (int32_t)(p[28]|p[29]<<8|p[30]<<16|p[31]<<24) / 1e7;
uint8_t fix = p[20]; // 0 none, 2 2D, 3 3D, 4 GNSS+DR, 5 time only
```

## RTCM3 типи докладно (що ллється з бази в ровер)

Кадр: `D3 [len 10біт] payload [CRC-24Q]`. ESP32 не парсить - пересилає всліпу,
але знати склад зобов'язаний, інакше Float назавжди.

| Тип | Назва | Період | Зміст |
| --- | --- | --- | --- |
| 1005 | Station coordinates | 1-5 с | ECEF XYZ бази мм + ID; без нього ровер не стартує! |
| 1006/1008 | Station + antenna | 5-10 с | те саме + висота антени + дескриптор ( rover ігнорує, але кастери вимагають) |
| 1033 | Receiver descriptor | 10 с | тип приймача/антени; для sourcetable |
| 1074 | GPS MSM4 | 1 с | compact: псевдодальність + фаза L1/L2 (старий мінімум) |
| 1077 | GPS MSM7 | 1 с | full: фаза + CNR + доплер, всі сигнали - БЕРИ ЦЕ! |
| 1084/1087 | GLONASS MSM4/MSM7 | 1 с | те саме для GLO; без пари з 1230 не зафіксується |
| 1094/1097 | Galileo MSM4/MSM7 | 1 с | E1+E5b; для F9P-02B обов'язково |
| 1114/1117 | QZSS MSM | 1 с | Японія; в Україні ігнор |
| 1124/1127 | BeiDou MSM4/MSM7 | 1 с | B1+B2; в місті дає +4 супутники |
| 1230 | GLONASS bias | 5 с | міжчастотні зсуви GLO; БЕЗ НЬОГО GLO FLOAT! |
| 4072.0/4072.1 | u-blox proprietary | 1 с | додаткові дані F9P (внутрішнє) |
| 4065 | Text | 10 с | довільний текст бази |

Мінімальні набори:

```text
L1/L2 база (F9P-02B): 1005(1)+1077(1)+1087(1)+1097(1)+1127(1)+1230(5)+1033(10)
L1/L5 база (F9P-15B/LC29H/UM980): той самий MSM7! MSM4 для L5 не беруть.
Економ-режим (повільний радіоканал 9600): 1005(5)+1077(2)+1087(2)+1230(10)
```

Перевірка в u-center: `View → Messages → UBX-RXM-RTCM` - лічильник по кожному
типу, `CRC failed >0` = битий радіоканал. На ровері `UBX-NAV-PVT fixType` має
стати `3` + `carrSoln=2` (2=Fix, 1=Float).

## Survey-in процедура покроково з командами

Survey-in - усереднення позиції нерухомої антени. Точність бази = стеля точності
ровера. Для агро/дрона достатньо survey-in; для кадастру - тільки FIXED з PPP.

Крок 0 - місце: дах, щогла 2 м, ground plane, 360° неба, далі від парапетів 1 м.
Крок 1 - u-center підключи USB бази, `Receiver → Action → Survey-in`: minDur 60-300 с,
accLimit 2000 мм (старт) або 500 мм (фінально).
Крок 2 - ті ж команди вручну (UBX CFG-TMODE3 survey-in 120 с / 1500 мм):

```text
B5 62 06 71 28 00 01 78 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 78 00 00 00 DC 05 00 00 0F 27 00 00
пояснення: mode=1 survey-in, minDur=120с (0x78), accLimit=1500мм (0x05DC)
```

Або через VALSET-ключі (FW HPG 1.30+): `CFG-TMODE-MODE=1, CFG-TMODE-SVIN_MIN_DUR=120,
CFG-TMODE-SVIN_ACC_LIMIT=1500`, потім`CFG-CFG save`.
Крок 3 - UM980 еквівалент (ASCII, 115200):

```text
CONFIG SIGNALGROUP 3 6       ; GPS+GLO+GAL+BDS всі частоти
MODE BASE TIME 60 2.0 0      ; survey 60с, 2.0м, без збереження
SAVECONFIG
```

Крок 4 - LC29H-BA еквівалент:

```text
$PQTMCFGSVIN,W,1,60,2000,0*xx   ; увімкнути, 60с, 2м
$PQTMSAVEPAR*5A                 ; зберегти
```

Крок 5 - контроль: `UBX-NAV-SVIN` раз на секунду показує `cAcc` (мм) і `valid`.
Чекаєш `valid=1`. Типовий час: відкрите небо 60-120 с, дах у місті 180-600 с.
Крок 6 - зафіксуй координати: скопіюй `meanX/meanY/meanZ` з NAV-SVIN у блокнот,
переведи базу в FIXED (див. нижче) - інакше після перезавантаження survey піде заново!

Перехід survey → fixed (точні ECEF, приклад Київ):

```text
; u-center CFG-TMODE3: mode=2 Fixed, ecefX=3491342.12 ecefY=2066889.45 ecefZ=4888034.20
; АБО VALSET: CFG-TMODE-POS_TYPE=0, CFG-TMODE-ECEF_X/Y/Z, CFG-TMODE-FIXED_POS_ACC=50мм
```

Точні координати без геодезиста: лог RINEX 24 год → сервіс CSRS-PPP / NRCan →
FIXED з точністю 2 см. Для агро достатньо survey-in 300 с.

## Moving-base схема (два F9P - курс без компаса!)

Ідея: дві антени на даху трактора/дрона на відстані `baseline` 0.5-2 м.
Задня F9P = база (шле RTCM3 безпосередньо по UART!), передня = ровер (рахує вектор).
Вихід - `NAV-RELPOSNED`: північ/схід/вниз у см + `relPosHeading` у градусах.

```text
Небо ──► [ANT задня] ──► RF F9P#BASE (TIME fixed, координати умовні!)
Небо ──► [ANT передня] ──► RF F9P#ROVER
F9P#BASE UART2 TX (RTCM 1077+1087+1097+1127+1230 1Гц) ──► F9P#ROVER UART2 RX (прямий дріт 115200!)
F9P#ROVER UART1 TX (NMEA+UBX NAV-RELPOSNED) ──► ESP32 GPIO16
ESP32 рахує heading і шле в AgOpenGPS / автопілот
Живлення: обидва 3.3В, спільна земля! Боди UART2 з обох боків однакові!
```

Конфігурація бази moving-base (u-center):

```text
CFG-TMODE3 mode=0 OFF (moving base НЕ використовує TIME! вона рухома!)
CFG-MSG RTCM3-1077/1087/1097/1127 на UART2 1 Гц, 1230 0.2 Гц, 1005 ВИМКНУТИ!
CFG-PRT UART2 115200
```

Конфігурація ровера:

```text
CFG-MSG UBX-NAV-RELPOSNED на UART1 1–10 Гц
CFG-MSG UBX-NAV-PVT на UART1 5 Гц
```

Парсинг RELPOSNED на ESP32 (скорочено):

```cpp
// UBX 01 3C len 64: refStationId U2, iTOW U4, relPosN/E/D I4 см[8/12/16],
// relPosLength I4[20] см, relPosHeading I4[24] 1e-5°, flags U4[60]
bool relposned(const uint8_t *p, float &hdg, float &len) {
  uint32_t fl = p[60] | (p[61]<<8) | (p[62]<<16) | (p[63]<<24);
  bool fix = fl & (1<<8);       // relPosValid
  bool hdgOk = fl & (1<<9);     // isHeadingValid
  int32_t h = (int32_t)(p[24]|p[25]<<8|p[26]<<16|p[27]<<24);
  int32_t l = (int32_t)(p[20]|p[21]<<8|p[22]<<16|p[23]<<24);
  hdg = h / 1e5; len = l / 100.0;
  return fix && hdgOk;
}
// baseline 1м -> точність курсу ~0.4°, 2м -> ~0.2° (чим довше, тим краще!)
```

LC29H-EA вміє те саме одним чіпом з двома антенами: `$PQTMCFGHEADING,W,1*` +
дві L1+L5 антени на 0.5-1 м. Дешевше за два F9P! Деталі - Quectel LC29H(EA)
Moving Base Application Note. Зв'язок з радіо - [02-NRF24-LoRa](../../../ESP32-Reference/12-Moduli-zvyazku/02-NRF24-LoRa.md).

## Свій NTRIP-кастер (RTKLIB str2str - без чужого rtk2go!)

Навіщо свій: rtk2go.com інколи лежить, а поле без інтернету взагалі вимагає
локального кастера в тракторі (Raspberry Pi + 4G). Схема:

```text
[База F9P UART2 USB] ──► [RPi/ПК str2str] ──TCP:2101──► [ровер ESP32 NTRIP-клієнт]
                                              └─► [другий ровер / AgOpenGPS]
```

Рецепт 1 - база в кастер (Linux, RTKLIB зібрано з `app/str2str/gcc/makefile`):

```bash
# Зібрати
cd RTKLIB/app/str2str/gcc && make
# База serial -> NTRIP-кастер (тип NTRIPS!), порт 2101, mountpoint /BASE1
./str2str -in serial://ttyACM0:115200 -out ntrips://:pass@:2101/BASE1 \
  -msg "1005(1),1077(1),1087(1),1097(1),1127(1),1230(5),1033(10)" \
  -t 1 -fl /tmp/str2str.log &
# Перевірка sourcetable браузером: http://localhost:2101/
```

Рецепт 2 - готовий rtk2go (без свого сервера, для старту):

```bash
./str2str -in serial://ttyACM0:115200 \
  -out ntrips://user:pass@rtk2go.com:2101/KYIV-BASE1 \
  -msg "1005(1),1077(1),1087(1),1097(1),1127(1),1230(5)" -t 1
# mountpoint унікальний! пароль з листа rtk2go. GGA від ровера обов'язкова.
```

Рецепт 3 - міст UART→TCP без NTRIP (поле, один ровер, мінімум накладних):

```bash
./str2str -in serial://ttyACM0:115200 -out tcpsvr://:25000 -b 1
# ESP32 ровер: TCP-клієнт на 192.168.4.1:25000, байти в UART1 RX всліпу
```

Рецепт 4 - Windows STRSVR (GUI): Input=COM5 115200, Output=NTRIP Caster
Port 2101, Conversion=None, Msg як вище. Кнопка Start. Логи в `strsvr.log`.

Поради кастера: порт 2101 відкрити в роутері (port forward), mountpoint ВЕЛИКИМИ
без пробілів, пароль ≥12 символів, sourcetable-таблицю перевіряти через
`curl http://caster:2101/`. ESP32-код NTRIP-клієнта вже є вище в ноті -
міняєш тільки HOST/PORT/MOUNT. Канал NTRIP - через [18-Cellular-LoRa-2](../../../ESP32-Reference/12-Moduli-zvyazku/18-Cellular-LoRa-2.md).

## Антени докладно: patch vs helix vs choke-ring + ground plane розміри

| Тип | Конструкція | Посилення | Ціна | Вердикт RTK |
| --- | --- | --- | --- | --- |
| Керамічна patch 25×25 | квадрат на платі ATGM336H | 2-3 дБі, тільки L1 | ~1 $ | НЕ RTK! Тільки logger |
| Активна patch L1/L2 40×40 | ANN-MB, AS-ANT2B, TW3882 + LNA 28 дБ + SAW | 4-5 дБі | ~40-80 $ | СТАНДАРТ ровера/бази |
| Helix (квадрифіляр) | Harxon HX-CH3602, AS-ANT2B-HEL | 3-5 дБі, широка ДС | ~60-120 $ | КРАЩЕ в місті (multipath!) |
| Choke-ring | кільця-екрани 20 см, геодезія | 5-7 дБі, відсікає землю | ~800-2000 $ | База CORS, не ровер |
| Стрижень/антени 868 МГц | LoRa-шнурки | −20 дБ на 1.5 ГГц | - | ЗАБОРОНЕНО! |

Ground plane - металева пластина під антеною, що відсікає відбиття від землі:

```text
Мінімум ровер: квадрат 100×100×1 мм алюміній/сталь, антена по центру на магніті
Норма база: диск Ø 200 мм або квадрат 200×200 мм, заземлений на щоглу
Ідеал CORS: диск Ø 400 мм + choke-кільця, антена на висоті 2 м над дахом
Матеріал: будь-який метал ≥0.5 мм (кришка каструлі працює!). Неметал (картон) = 0 ефекту.
Отвір під кабель по центру, контакт по колу! Фарбу зачистити!
Кабель: RG174 до 2 м, LMR200/CFD200 до 5 м, далі — тільки винос бази ближче.
```

Живлення LNA: виміряй мультиметром струм у розрив bias: норма 8-25 мА.
0 мА = обрив/пасивна антена, >50 мА = КЗ (перевір ANT_OFF!). ZED-F9P плати мають
джампер ANT 3V3/5V - став 3.3 В для ANN-MB. UM980/LC29H - зовнішній bias-tee
(індуктивність 100 нГ + конденсатор 100 пФ схема з Hardware Design).
Рознесення: GNSS-антена ≥20 см від LTE (див. [18-Cellular-LoRa-2](../../../ESP32-Reference/12-Moduli-zvyazku/18-Cellular-LoRa-2.md)),
≥50 см від LoRa 868 МГц штиря, ≥1 м від WiFi-роутера.

## Багатопроменевість у місті (чому Float між будинками)

Multipath - сигнал приходить двічі: безпосередньо + відбитий від фасаду/асфальту.
Відбитий довший на 10-100 м → фаза бреше → Fix зривається у Float/DGPS.
Ознаки: CN0 стрибає 30↔45, HDOP>2, супутників 18 але Fix немає, висота ±5 м.

| Захист | Як | Ефект |
| --- | --- | --- |
| Elevation mask 15° | відсікти низькі супутники (CFG-NAV5 minElev) | −50% multipath, −2 супутники |
| Тільки L5/E5a | L5 чистіший, chipping rate ×10 | Fix там, де L2 мовчить |
| Helix-антена | кругова поляризація давить відбиття | +20% Fix у місті |
| Ground plane 200 мм | відсікає відбиття від землі | стабільна висота |
| Довга ініціалізація | стояти 60 с нерухомо після старту | Fix тримається в русі |
| Винести антену | щогла 2 м / дах авто замість салону | інколи єдиний вихід |
| Маска CN0 35 | ігнорувати слабкі (RTKLIB `snrmask`) | менше хибних фаз |

Тест: увімкни `UBX-NAV-SAT`, запиши 5 хв у місті і вдома. Порівняй середній CN0
і кількість `used=1`. Різниця >6 дБ = місце погане, шукай інше. Тунелі/паркінги -
тільки LC29H-BA з dead reckoning тримає трек (див. початок ноти).

## Геодезія на ESP32: ECEF→LLA→ENU + точність vs час

База віддає ECEF (метри від центру Землі), роверу потрібні локальні ENU
(схід/північ/вгору від бази) для автопілота. Формули WGS84: `a=6378137, f=1/298.257223563`.

```c
// ECEF -> LLA (ітеративний, 3 ітерації достатньо для см)
void ecef2lla(double x,double y,double z,double *lat,double *lon,double *h){
  const double a=6378137.0, f=1/298.257223563, e2=f*(2-f), b=a*(1-f);
  *lon=atan2(y,x);
  double p=sqrt(x*x+y*y), th=atan2(z*a,p*b), s=sin(th), c=cos(th);
  *lat=atan2(z+e2/(1-e2)*b*s*s*s, p-e2*a*c*c*c);
  double N=a/sqrt(1-e2*sin(*lat)*sin(*lat));
  *h=p/cos(*lat)-N;
}
// LLA -> ENU відносно бази (радіани+метри)
void lla2enu(double lat,double lon,double h, double lat0,double lon0,double h0,
             double *e,double *n,double *u){
  const double a=6378137.0, f=1/298.257223563, e2=f*(2-f);
  double N=a/sqrt(1-e2*sin(lat0)*sin(lat0));
  double x=(N+h0)*cos(lat0)*cos(lon0), y=(N+h0)*cos(lat0)*sin(lon0), z=((1-e2)*N+h0)*sin(lat0);
  double N1=a/sqrt(1-e2*sin(lat)*sin(lat));
  double x1=(N1+h)*cos(lat)*cos(lon), y1=(N1+h)*cos(lat)*sin(lon), z1=((1-e2)*N1+h)*sin(lat);
  double dx=x1-x, dy=y1-y, dz=z1-z, sl=sin(lat0), cl=cos(lat0), so=sin(lon0), co=cos(lon0);
  *e=-so*dx+co*dy; *n=-sl*co*dx-sl*so*dy+cl*dz; *u=cl*co*dx+cl*so*dy+sl*dz;
}
```

Точність vs час (відкрите небо, база 5 км, L1/L2):

| Режим | 10 с | 60 с | 10 хв | 1 год | Типово |
| --- | --- | --- | --- | --- | --- |
| Single (без поправок) | 2.5 м | 2.0 м | 1.5 м | 1.2 м | дрейф іоносфери |
| DGPS (1005+1230) | 1.0 м | 0.8 м | 0.6 м | 0.5 м | кода, без фази |
| Float (MSM є, ambiguity пливе) | 0.5 м | 0.3 м | 0.2 м | 0.15 м | дециметри |
| Fix (ambiguity зафіксовано!) | 0.05 м | 0.02 м | 0.014 м | 0.01 м + 1ppm | сантиметри! |
| Fix + 24г PPP (база) | - | - | - | 0.005 м | геодезія |

Правило 1 ppm: +1 мм помилки на кожен км бази. База 20 км = +2 см до Fix.
Тому NTRIP-ровер далі 30 км від бази - Float. Своя база в радіусі 10 км - ідеал.
Висота завжди гірша за план у 1.5-2 рази! Геоїд EGM2008 для України +15…+25 м -
віднімай перед порівнянням з картою. Живлення геодезії - [01-Lancjugi-zhivlennya](../../../ESP32-Reference/02-Zhivlennya/01-Lancjugi-zhivlennya.md).

## AgOpenGPS оглядово (автоприлад для трактора)

AgOpenGPS (AOG) - відкритий автопілот агро: Windows-планшет + F9P ровер +
WAS-датчик кута + мотор керма + ESP32-секції. AOG бере NMEA GGA+VTG 10 Гц і
RELPOSNED-курс, веде трактор по AB-лінії з точністю 2 см!

| Компонент AOG | Що | Зв'язок з цією нотою |
| --- | --- | --- |
| GPS-ровер | ZED-F9P 10 Гц + NTRIP (ця нота!) | UART1 у планшет через USB; боди 115200 |
| IMU/курс | BNO085 + dual-F9P moving-base | heading з RELPOSNED (див. вище) |
| WAS | потенціометр кута коліс → ADS1115 | ESP32 читає і шле в AOG UDP |
| Автокермо | Cytron MD13S + мотор 12 В | ESP32/Panda-плата, PID у AOG |
| Секції | 8 реле обприскувача | ESP32 по UDP, код як NTRIP-клієнт вище |
| База | своя F9P + str2str (див. кастер вище) | rtk2go або локальний кастер у полі |

Конфіг F9P для AOG: 10 Гц, GGA+VTG 10 Гц, PVT 10 Гц, боди 115200, RTCM в RX1.
AOG-NTRIP можна лити прямо з планшета (вбудований клієнт) - тоді ESP32 не потрібен,
але для автономного ровера (дрон/робот) ESP32-клієнт з цієї ноти - те що треба.
Старт: плата Ardusimple + планшет + безкоштовний AOG з GitHub, поле з відкритим небом.

## Див. також

- [Home](../../../ESP32-Reference/Home.md) - старт бази знань
- [03-SIM800L-GPS](../../../ESP32-Reference/12-Moduli-zvyazku/03-SIM800L-GPS.md) - бюджетний GNSS NEO-6M + SIM800L (з чого починати)
- [02-NRF24-LoRa](../../../ESP32-Reference/12-Moduli-zvyazku/02-NRF24-LoRa.md) - радіоміст для RTCM3 без інтернету (E22/E32, SX1262)
- [09-Cellular-NBIoT-UARTLoRa](../../../ESP32-Reference/12-Moduli-zvyazku/09-Cellular-NBIoT-UARTLoRa.md) - SIM7080G/A7670/E32/SX1262 (NTRIP через Cat-1)
- [18-Cellular-LoRa-2](../../../ESP32-Reference/12-Moduli-zvyazku/18-Cellular-LoRa-2.md) - Cat-1 EC200U/Air724 + LoRa E78/RAK3172/SX1280/LR1121 (NTRIP-канал для ровера)
- [17-GNSS-RTK](../../../ESP32-Reference/12-Moduli-zvyazku/17-GNSS-RTK.md) - ця нота (якір RTK)
- [UART](../../../ESP32-Reference/04-Shini/01-UART.md) - UART ESP32: бод, перехрестя TX/RX, буфери
- [01-Lancjugi-zhivlennya](../../../ESP32-Reference/02-Zhivlennya/01-Lancjugi-zhivlennya.md) - живлення 3.3 В без просадок, LDO, bias-tee антени
