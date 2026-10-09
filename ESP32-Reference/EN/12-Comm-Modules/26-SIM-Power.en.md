---
title: SIM-карти та живлення стільникових модулів - холдери, PIN/PUK, eSIM, TX-бурсти 2-3A, суперкап
description: half «мертвих» GSM-проєктів - this not прошивка, but дві залізні теми: SIM-карта (формат, PIN, холдер, детект) and живлення (піки 2-3A in TX-бурсті, які not тримає жоден LDO DevKit-плати)....; shows schematics, code and tables.
tags: [esp32, sim, esim, pin, puk, ccid, holder, sim-detect, esd, power, sim800, a7670, ec200u, dc-dc, supercap, tx-burst]
category: Moduli
lang: en
date-created: 2026-09-30
date: 2026-10-08
---

# SIM-карти та живлення стільникових модулів - холдери, eSIM, TX-бурсти, суперкап

## Purpose

half «мертвих» GSM-проєктів - this not прошивка, but дві залізні теми: SIM-карта (формат, PIN, холдер, детект) and живлення (піки 2-3A in TX-бурсті, які not тримає жоден LDO DevKit-плати). Нота збирає обидві in одному місці how фундамент під практику.

База: перший GSM - [[EN/12-Comm-Modules/03-SIM800L-GPS.en]], 4G - [[EN/12-Comm-Modules/07-SIM7600-W5500-MCP2515.en]], Cat-1 - [[EN/12-Comm-Modules/18-Cellular-LoRa-2.en]], NB-IoT - [[EN/12-Comm-Modules/09-Cellular-NBIoT-UARTLoRa.en]], UART - [[04-Interfaces/01-UART|UART]], живлення - [[02-Power-Supply/01-Lancjugi-zhivlennya]], protection - [[13-Power-Modules/04-LDO-Buck-XL4015-Protect]], start - [[EN/Home.en]].

> [!danger] Два вбивці стільникових модулів
>
> 1. **5V on VBAT** синьої плати (SIM800/A7670/EC200U without свого стабілізатора) - пробій RF-підсилювача for секунди. 2. **Живлення from 3.3V DevKit** - TX-бурст 2A садить рейку, module перезавантажується саме in момент реєстрації (`AT+CREG` ніколи not `0,1`). Обидва симптоми лікуються ТІЛЬКИ окремим DC-DC + 1000 мкФ, розділ 5.

![[assets/img/sim-powerholder-scheme.png|600]]
*Fig. Вузол стільникового зв'язку: DC-DC 4.0V/3A + 1000 мкФ + TVS → VBAT, SIM-холдер with детектом and ESD, GSM-антена окремо from GNSS.*

## Характеристики

### Живлення популярних модулів (звести in одну таблицю!)

| module | Діапазон VBAT | Номінал | Пік TX | Наслідок неправильного живлення |
| --- | --- | --- | --- | --- |
| SIM800L (синя плата) | 3.4-4.4V | 4.0V | до 2A (слот 577 мкс) | 5V = смерть; 3.3V = ребути at реєстрації |
| SIM800L EVB (червона, micro-USB) | 5V on вхід плати | свій buck on платі | - | Їй МОЖНА 5V - стабілізатор свій; перевіряти візуально! |
| A7670E/SA/G | 3.4-4.2V | 3.8-4.0V | до 2A | Те саме, that SIM800; плюс PWRKEY-імпульс |
| SIM7600E-H | 3.4-4.2V | 3.8V | до 3A | 3A - товстіший провід, той же 1000 мкФ |
| SIM7080G | 2.7-4.8V | 4.0V | до 2A | Ширший діапазон, але пік той же |
| EC200U / Air724UG | 3.4-4.3V | 3.8V | до 2.5-3A | USB-режими ECM/RNDIS not знімають вимоги до VBAT! |

### SIM-карти: формати

| Формат | Розмір | Де зустрічається | Коментар for ESP32-проєктів |
| --- | --- | --- | --- |
| Mini-SIM (2FF) | 25×15 мм | Старі холдери, автотрекери | Рідко, але холдери дешеві and живучі |
| Micro-SIM (3FF) | 15×12 мм | SIM800 EVB, частина Cat-1 плат | Перехідний формат |
| Nano-SIM (4FF) | 12.3×8.8 мм | A7670, EC200U, SIM7600 - стандарт де-факто | **Проєктувати під nano**, адаптери - тільки for столу |
| eSIM (MFF2, паяна) | 6×5 мм | Серійні вироби | Профіль заливається per RSP; for України - уточнювати підтримку in оператора |
| SoftSIM / solderable | чип | Промислові batches | Той же eSIM-клас, інша назва in каталогах |

> Адаптери nano→micro/mini - ТІЛЬКИ for лабораторії: in вібрації/полі адаптер розхитується, контакт пропадає, модем мовчки відвалюється from мережі. in виріб - холдер рідного формату карти.

## Легенда пінів SIM-інтерфейсу

| Пін (сторона модуля) | Призначення | Куди / that | Примітка |
| --- | --- | --- | --- |
| SIM_VDD | Живлення карти 1.8V / 3.0V | Всередині модуля, автоматичний вибір | not підтягувати ззовні! module сам домовляється with картою |
| SIM_DATA (I/O) | Дані, open-drain | Всередині модуля + TVS-матриця for потреби | Підтяжка всередині; довжина доріжок мінімальна |
| SIM_CLK | Такт 1-5 МГц | Всередині модуля | Поруч - ніяких силових трас (наведення = errors ATR) |
| SIM_RST | Скидання карти | Всередині модуля | - |
| SIM_DET / SIM_PRESENCE | Детект карти in холдері | GPIO ESP32 (вхід with pull-up) або NC | Переривання «карту вийняли» → коректно закрити PDP/MQTT |
| GND | Земля SIM-блоку | Спільна GND | - |

### ASCII schematic: SIM-блок

```text
Модемний module              SIM-холдер (nano, push-push)
───────────────              ────────────────────────────
SIM_VDD ───────────────────►  VCC (1.8/3.0V авто)
SIM_DATA ──[TVS]────────────►  DATA (доріжка < 30 мм!)
SIM_CLK ───────────────────►  CLK (далі від VBAT-силової!)
SIM_RST ───────────────────►  RST
GND ────────────────────────  GND
                               DET ──► GPIO34 ESP32 (переривання FALLING)
                               корпус холдера ──► GND (екран!)
```

### Mermaid: SIM-блок

```mermaid
graph LR
    MOD[Модем<br/>SIM800/A7670/EC200U] -->|VDD/DATA/CLK/RST| HOLD[SIM-холдер nano]
    HOLD -->|DET| ESP[GPIO34 ESP32<br/>переривання]
    TVS[TVS-матриця<br/>на DATA/CLK/RST] --- HOLD
    PSU[DC-DC 4.0V + 1000мкФ] -->|VBAT| MOD
    ANT[GSM-антена] --- MOD
```

## 1. PIN/PUK: команди and ритуали

```text
AT+CPIN?              -> +CPIN: READY (карта без PIN — ідеал для IoT!)
AT+CPIN?              -> +CPIN: SIM PIN (просить PIN)
AT+CPIN="1234"        -> OK (ввести PIN; 3 спроби!)
AT+CPIN?              -> +CPIN: SIM PUK (PIN вичерпано — тільки PUK!)
AT+CPIN="87654321","0000" -> OK (PUK + новий PIN)
AT+CLCK="SC",0,"1234" -> OK (вимкнути запит PIN назавжди — ТАК для IoT)
AT+CCID               -> +CCID: 89380... (серійник карти — інвентаризація!)
AT+CIMI               -> 25501... (IMSI: MCC+MNC+абонент; 25501 = Vodafone UA)
AT+CNUM               -> +CNUM: ""," +380...",129 (свій номер, якщо записаний)
```

| Правило | Чому |
| --- | --- |
| Усі IoT-карти - with ВИМКНЕНИМ PIN (`AT+CLCK="SC",0`) | Після кожного ребута/просадки модем інакше висітиме on `SIM PIN` without мережі |
| PUK зберігати in реєстрі batches, not in прошивці | 10 невірних PUK = карта мертва назавжди, заміна in полі |
| `AT+CCID`/`AT+CIMI` - in self-test and in лог | Прив'язка «серійник пристрою ↔ SIM» ловить підміну карт |
| 3 спроби PIN - and стоп | Прошивка not має брутфорсити PIN: після 2 невдач - стоп and аварійний статус |

> [!warning] PUK - this останній рубіж
> 10 невірних введень PUK спалюють карту безповоротно. therefore PUK вводять тільки руками with папірця/сховища, ніколи - автоматичним перебором in коді.

## 2. Холдери: типи, детект, гаряча заміна

| Тип холдера | how працює | Де ставити | Пастка |
| --- | --- | --- | --- |
| Push-push (натисни-клац) | Натиснув - виїхала | Столова розробка, доступні корпуси | in вібрації карта може відійти - for авто/трактора брати with замком |
| Push-pull / tray (лоток with голкою) | how in телефоні | Герметичні корпуси (лоток + гумка = IP!) | Голка-скріпка in полі губиться - класти запасну in корпус |
| Hinged/lock (кришка with замком) | Відкидна кришка | Вібрація, промзона | Найнадійніший контакт, але більший |
| eSIM MFF2 (паяний) | Профіль per RSP | Серія 100+ | Немає «вийняти and verify» - потрібен стенд with тестовим профілем |

### SIM_DET - переривання «карту вийняли»

```cpp
// Arduino: детект карти → коректне завершення сесії
#define SIM_DET 34
volatile bool simGone = false;
void IRAM_ATTR onSimDet() { simGone = true; }
void setup() {
  pinMode(SIM_DET, INPUT_PULLUP);
  attachInterrupt(SIM_DET, onSimDet, FALLING); // холдер замикає DET на GND
}
void loop() {
  if (simGone) {
    simGone = false;
    sim.println("AT+SAPBR=0,1");   // закрити bearer
    delay(500);
    // MQTT LWT сам повідомить хмару про відвал
  }
}
```

Гаряча заміна (вийняти/вставити without ребута): можлива ТІЛЬКИ якщо модем її підтримує (`AT+QSIMDET` in Quectel-лінійки; in SIM800 - умовно). Безпечний ритуал without підтримки: `AT+CFUN=0` (радіо викл) → заміна → `AT+CFUN=1` → чекати `+CPIN: READY` → `AT+CREG?` → підняти SAPBR заново.

## 3. ESD on SIM-лініях

SIM-холдер - this отвір in корпусі, куди тицяють пальцями: статичний розряд 8 кВ прямо in `SIM_DATA`.

| Захід | how | Чому |
| --- | --- | --- |
| TVS-матриця (напр. PRTR5V0U2X) on DATA/CLK/RST | Біля холдера, земля - коротко in plane | Зрізає розряд до ~10V, далі вмирати нікуди |
| Послідовні 22-33 Ом on DATA/CLK | Між TVS and модулем | Обмежують струм розряду + давлять дзвін on 5 МГц CLK |
| Корпус холдера - on GND | Металева клітка холдера паяється in землю | Екран from пальців and наведень |
| Доріжки SIM < 30 мм, without силових сусідів | Розведення for главою RF-keepout | CLK 5 МГц ловить TX-бурсти VBAT поруч |

## 4. TX-бурсти: фізика просадки

GSM - TDMA: передавач вмикається слотом 577 мкс with піком 2A (2G) / 1-3A (Cat-1/LTE залежно from смуги and відстані до вишки). Середній струм смішний (200-500 мА), but от пік - ні.

```text
Струм VBAT у часі (реєстрація в мережі, слабкий сигнал):

 2.0A ─┤  ┌──┐    ┌──┐    ┌──┐
       │  │  │    │  │    │  │   слот 577 мкс
 0.3A ─┤──┘  └────┘  └────┘  └─── idle між слотами
       └──────────────────────────► t

 Конденсатор 1000 мкФ віддає заряд у слоті:
 ΔV = I × Δt / C = 2.0 × 577e-6 / 1000e-6 ≈ 1.15V  ← без DC-DC було б лихо!
 DC-DC з швидким transient-відгуком підхоплює — тому потрібен саме
 імпульсний buck (LM2596/MP1584/SY8113), а не лінійний LDO.
```

> Чому not LDO: лінійник with 5V on 4V at 2A розсіює (5−4)×2 = 2 Вт + not встигає for фронтом 577 мкс without величезного bulk. Buck - ККД 85-90%, гріється мало, transient тримає.

## 5. DC-DC for VBAT: вибір and обв'язка

| Варіант | Струм | Плюс | Мінус | Коли |
| --- | --- | --- | --- | --- |
| LM2596 (module) | до 3A | Дешевий, всюди є, гвинтовий trim | 150 кГц - велика котушка, гріється without радіатора | Стіл, перші прототипи |
| MP1584 (module/чіп) | до 3A | 1.5 МГц - компактний, холодніший | Trim дрібний, крутити обережно | Виріб середній |
| SY8113 / TPS5632xx (своя плата) | 3A+ | Сучасні, малий dropout обв'язки | Тільки своя розводка | Серія, див. [[17-Lab/04-PCB-Design]] |
| 2×18650 → buck | 3A+ | Автономність | BMS + заряд обов'язкові | Поле without мережі 220V |

### Еталонна обв'язка VBAT (збирати буквально!)

```text
Вхід 5V 2A+ (адаптер / USB-C PD-тригер / АКБ через boost)
  │
  ├─► TVS SMBJ5.0A на землю (кидки адаптера!)
  ├─► електроліт 470 мкФ на ВХОДІ buck
  │
[buck: LM2596/MP1584, виставлено 4.0V БЕЗ навантаження!]
  │
  ├─► електроліт 1000 мкФ low-ESR (ESR ≤ 100 мОм!)
  ├─► кераміка 100 нФ + 10 мкФ прямо біля VBAT-піна модуля
  └─► VBAT модуля (провід ≥0.5 мм², <10 см!)
        GND — товста зірка: buck GND = SIM GND = ESP32 GND в ОДНІЙ точці
```

Порядок entry in експлуатацію:

1. without модуля виставити 4.0V мультиметром, покрутити trim, почекати 5 хв (дрейф!).
2. Підключити module via 1000 мкФ, `AT+CBC` має показати 3900-4200.
3. `AT+CSQ` > 10, `AT+CREG?` → `0,1` (NET блимає 1 раз/3 с).
4. Прогнати 10 HTTP-сесій підряд - жодного ребута (лічильник `AT+CCLK?` not має стрибати).

## 6. Суперкап how буфер піків

Коли DC-DC слабкий, but переробляти плату ніколи: суперконденсатор 1-10 Ф on 5.5V паралельно VBAT-рейці via діод Шотткі.

```text
buck 4.0V ──►|діод Шотткі|──┬──► VBAT модуля
                            │
                       [суперкап 4–10 Ф, 5.5V]
                            │
                           GND

 Заряд: повільно через резистор 10 Ом (обмежити пусковий струм!)
 Розряд: у TX-слоті діод закритий — кап віддає пік сам.
```

| Параметр | Значення | Коментар |
| --- | --- | --- |
| Ємність | 4-10 Ф | 1 Ф тримає слот 577 мкс with просадкою ~0.5V - мінімум; 10 Ф - with запасом |
| Напруга | 5.5V | with запасом над 4.0V (деградація!) |
| ESR | < 100 мОм | Високий ESR = кап not встигає for слотом |
| Зарядний резистор | 10 Ом, 1W | without нього пусковий струм виб'є protection buck |
| Витік (leakage) | десятки мкА | for батарейних - рахувати in бюджеті сну! |

> Суперкап - костиль, not архітектура. in новій ревізії плати - нормальний buck on 3A замість капа.

## 7. Вимірювання піків осцилографом

without цього - гадання. Процедура with [[17-Lab/01-Instruments|Прилади]] стосовно до модема:

1. Шунт 0.05 Ом (2W!) in розрив VBAT + диференційний пробник, або кліщі improvized - НІ, тільки шунт.
2. Тригер - per GPIO-маркеру ESP32 перед `AT+HTTPACTION`.
3. Очікуване: пачки 577 мкс, амплітуда 1.5-2A (2G) / до 3A (LTE, слабкий сигнал).
4. Одночасно другим каналом - VBAT: просадка not глибше 3.4V (нижня межа SIM800). Глибше → більший bulk / коротші дроти / інший buck.
5. Слабкий сигнал = максимальні піки: вимірювати with прикритою антеною (рука поверх - чесний worst case).

```mermaid
flowchart TB
    M[Модем ребутиться при GPRS] --> SHUNT[Шунт 0.05 Ом + скоп]
    SHUNT --> AMP{Пік > 2A?}
    AMP -->|Ні, ~0.5A| PSU[DC-DC не віддає: trim/вхід/protection]
    AMP -->|Так, 2–3A| SAG{VBAT падає < 3.4V?}
    SAG -->|Так| CAP[+1000 мкФ / коротші дроти / суперкап]
    SAG -->|Ні| ANT[Софт: +CREG/+CSQ, прошивка модема]
```

## 8. Антени GSM/LTE/GNSS: роз'єми, розміщення, активні GPS, грозозахист

### 8.1. Типи антен and роз'єми

| Антена | Діапазон | Роз'єм | Де | Пастка |
| --- | --- | --- | --- | --- |
| Штирьова «палиця» GSM | 900/1800 МГц (2G), 700-2700 (LTE wideband) | SMA (on платі) | Стіл, тести | without ground plane під основою - КСХ > 3, гріється PA |
| PIFA/друкована on платі модема | Той же | - (розведена) | Компактні вироби | Поруч метал/АКБ - розстроювання, міряти `AT+CSQ` до/після корпусу |
| Зовнішня on кабелі | for маркуванням | U.FL (I-PEX) on модулі → SMA on корпусі | Вуличні корпуси | U.FL - 30 циклів макс! not смикати щотижня |
| GNSS patch кераміка 25×25 | 1575 МГц (L1) | Пін/коаксіал | NEO-6M плати | Працює тільки видом in небо + ground plane знизу |
| GNSS активна (with LNA) | L1 (+L2/L5 in F9P) | SMA + живлення 3.3V per коаксіалу (bias-tee!) | Дах, щогла | without bias-tee LNA мовчить - «антена є, супутників немає» |
| Комбінована LTE+GNSS «шайба» | Два кабелі всередині! | 2× SMA | Авто/трекери | not переплутати хвости: LTE in LTE-гніздо, GNSS in GNSS |

> LTE-антена (700-2700 МГц) and LoRa-антена (433/868 МГц) not взаємозамінні - чужа антена = КСХ 5+ = смерть вихідного каскаду for хвилини. Маркувати роз'єми on корпусі гравіюванням, див. [[EN/12-Comm-Modules/18-Cellular-LoRa-2.en]] (смуги B1/B3/B7/B20 + КСХ).

### 8.2. Розміщення: правила, які видно on `AT+CSQ`

1. GSM/LTE-антена - НАЙВИЩЕ in корпусі, далі from DC-DC (дроселі свистять in приймач).
2. Відстань до ESP32-WiFi-антени - ≥10 см (десенсибілізація: LTE TX глушить WiFi RX).
3. Металевий корпус = клітка Фарадея: антена ТІЛЬКИ зовні (SMA-перехід in стінці + гумка IP65).
4. GNSS patch - горизонтально небом вгору, під ним суцільний ground plane ≥70×70 мм (for F9P - 100×100, див. [[EN/12-Comm-Modules/17-GNSS-RTK.en]]).
5. Коаксіал not перегинати (радіус ≥5× діаметра), not класти паралельно силовим 220V.

### 8.3. Активна GNSS-антена and bias-tee

```text
NEO-6M / F9P module                Активна антена (3.3V LNA всередині)
───────────────────                ──────────────────────────────────
ANT/RF_IN ◄─── коаксіал 50 Ом ───►  RF (живлення LNA ЇДЕ ТИМ САМИМ кабелем!)
  └─► bias-tee: котушка до 3.3V + конденсатор у тракт (на платі приймача
      або окремим модулем, якщо приймач пасивний)
Перевірка: AT/NMEA показує супутники → LNA живиться; нулі → міряти 3.3V на кабелі!
Струм LNA 5–15 мА: закорочений кабель = перегрів bias-tee, ставити PTC.
```

### 8.4. Грозозахист зовнішньої антени

| Рівень | Захід | Коментар |
| --- | --- | --- |
| Обов'язково | Заземлена щогла + розрядник (coax lightning arrestor) перед вводом in будівлю | Розрядник - витратник: після близької грози перевіряти/міняти |
| Обов'язково | Заземлення корпусу вузла (bus 4 мм² до контуру) | Інакше різниця потенціалів піде via ESP32 |
| Бажано | TVS on коаксіал (спец. прохідні) | Другий рубіж після розрядника |
| Заборонено | «Авось пронесе» with антеною on даху without заземлення | Наведена перенапруга вбиває модем and все, that for ним per UART |

### 8.5. Mermaid: diagnostics «немає мережі / немає супутників»

```mermaid
flowchart TB
    S[AT+CSQ < 10 або 99,99] --> ANT{Антена підключена<br/>до СВОГО гнізда?}
    ANT -->|Ні| FIX[Підключити, перевірити U.FL до клацання]
    ANT -->|Так| CSQ2{CSQ росте якщо<br/>винести до вікна?}
    CSQ2 -->|Так| PLACE[Переставити антену вище/зовні, розд. 8.2]
    CSQ2 -->|Ні| BAND{AT+COPS=? бачить<br/>операторів?}
    BAND -->|Ні| SIMD[SIM: CPIN/CCID, інша карта, інший module]
    BAND -->|Так| REG[Чекати CREG; далі — APN/SAPBR, нота 03]
    G[GPS: нулі, нема GGA] --> SKY{Вид неба +<br/>активна антена живиться?}
    SKY -->|Ні| SKYF[На вулицю / bias-tee 3.3V, розд. 8.3]
    SKY -->|Так| COLD[Холодний start 5–15 хв; далі — RTK, нота 17]
```

## Code (3 фреймворки)

### Arduino - self-test SIM + живлення

```cpp
// Самоперевірка SIM і живлення перед роботою (розділи 1, 5)
HardwareSerial sim(2); // RX=16 TX=17
String atQuery(const char* cmd, int wait = 2000) {
  sim.println(cmd); delay(wait);
  String r; while (sim.available()) r += (char)sim.read();
  return r;
}
bool simCheck() {
  String cpin = atQuery("AT+CPIN?");
  if (cpin.indexOf("READY") < 0) { Serial.println("SIM не готова: " + cpin); return false; }
  Serial.println(atQuery("AT+CCID"));   // інвентаризація карти
  Serial.println(atQuery("AT+CIMI"));   // IMSI оператора
  String cbc = atQuery("AT+CBC");       // напруга VBAT
  Serial.println(cbc);                  // чекаємо ~4000 мВ
  String csq = atQuery("AT+CSQ");
  Serial.println(csq);                  // перше число > 10
  return atQuery("AT+CREG?").indexOf(",1") > 0 || atQuery("AT+CREG?").indexOf(",5") > 0;
}
void setup() {
  Serial.begin(115200); sim.begin(115200, SERIAL_8N1, 16, 17);
  delay(3000);
  if (!simCheck()) Serial.println("SELF-TEST FAIL: SIM/живлення/мережа");
  else Serial.println("SELF-TEST PASS");
}
```

### MicroPython - self-test SIM + живлення

```python
from machine import UART
import time
sim = UART(2, baudrate=115200, rx=16, tx=17)
def atq(cmd, wait=2):
    sim.write(cmd + "\r\n"); time.sleep(wait)
    return (sim.read() or b"").decode(errors="ignore")
print(atq("AT+CPIN?"))   # READY?
print(atq("AT+CCID"))    # серійник карти
print(atq("AT+CBC"))     # ~4000 мВ
print(atq("AT+CSQ"))     # > 10
print(atq("AT+CREG?"))   # 0,1 або 0,5
```

### ESP-IDF - self-test SIM + живлення

```c
// uart_write_bytes(UART_NUM_2, "AT+CPIN?\r\n", 9); → читати до "READY"/"SIM PIN"
// "AT+CBC" → парсити мВ, поріг 3600; "AT+CSQ" → поріг 10; "AT+CREG?" → ",1"/",5"
// Послідовність як в Arduino-прикладі; результат — в NVS selftest (див. 17-Lab/03).
```

## typical errors

| # | error | Чому погано | how правильно |
| --- | --- | --- | --- |
| 1 | Живлення модема from 3.3V DevKit | Пік 2A садить рейку, ребути at `CREG` | Окремий buck 4.0V + 1000 мкФ, розділ 5 |
| 2 | 5V on синю плату SIM800 | Пробій RF-підсилювача | 4.0V! Виняток - тільки червона EVB зі своїм стабілізатором |
| 3 | Адаптер nano→micro in полі | Розхитування, мовчазний відвал from мережі | Холдер рідного формату карти |
| 4 | PIN увімкнений on IoT-карті | Після ребута модем висить on `SIM PIN` | `AT+CLCK="SC",0` один раз at введенні in експлуатацію |
| 5 | Брутфорс PIN in коді | 3 спроби → PUK, 10 PUK → карта мертва | Після 2 невдач - стоп and аварійний статус |
| 6 | SIM_DATA довга, поруч VBAT | errors ATR, `SIM not inserted` | <30 мм, TVS біля холдера, without силових сусідів |
| 7 | Холдер without DET in корпусі with доступом | Вийняту карту помічають per таймаутах | DET on GPIO-переривання, розділ 2 |
| 8 | Немає TVS on SIM-лініях | ESD 8 кВ with пальців in `SIM_DATA` | PRTR5V0U2X + 22 Ом, розділ 3 |
| 9 | LDO замість buck on VBAT | 2 Вт тепла + not тримає transient 577 мкс | Buck LM2596/MP1584, розділ 5 |
| 10 | Суперкап without зарядного резистора | Пусковий струм вибиває protection buck | 10 Ом 1W послідовно, розділ 6 |
| 11 | APN with великої літери | Мережа відхиляє PDP-контекст | Буквально with таблиці 6.2 ноти 03 (`kyivstar`, `internet`) |
| 12 | Вимір піків кліщами/on око | not видно 577 мкс слотів | Шунт 0.05 Ом + скоп with тригером, розділ 7 |

## Official sources

- [SIM800 Hardware Design V1.09 (SIMCom)](https://www.simcom.com/product/SIM800.html) - VBAT 3.4-4.4V, піки 2A, SIM-інтерфейс, ESD.
- [A7670 Hardware Design (SIMCom)](https://www.simcom.com/product/A7670.html) - VBAT, PWRKEY, SIM-холдер.
- [EC200U Hardware Design (Quectel)](https://www.quectel.com/product/lte-ec200u-series) - VBAT 3.4-4.3V, SIM_DET (`AT+QSIMDET`), USB ECM/RNDIS.
- [Espressif - Hardware Design Guidelines](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/index.html) - розв'язка, TVS, розведення (застосовно до SIM-блоку).

## See also

- [[Home|Головна]]
- [[12-Comm-Modules/03-SIM800L-GPS|SIM800L + GPS]]
- [[12-Comm-Modules/07-SIM7600-W5500-MCP2515|SIM7600E 4G]]
- [[12-Comm-Modules/09-Cellular-NBIoT-UARTLoRa|SIM7080/A7670]]
- [[12-Comm-Modules/18-Cellular-LoRa-2|Cat-1 + LoRa-2]]
- [[12-Comm-Modules/17-GNSS-RTK|GNSS-RTK]]
- [[16-Projects/02-GPS-Tracker|GPS-трекер]]
- [[02-Power-Supply/01-Lancjugi-zhivlennya|Ланцюги живлення]]
- [[13-Power-Modules/04-LDO-Buck-XL4015-Protect|LDO/buck/protection]]
- [[13-Power-Modules/01-Buck-Boost-Solar|Buck/Boost/Solar]]
- [[17-Lab/01-Instruments|Прилади]]
- [[17-Lab/04-PCB-Design|PCB-Design]]
