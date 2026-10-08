---
description: BLE та Bluetooth Classic - Порівняння; Таблиця з'єднань; Код - BLE beacon / server
category: Radio
title: BLE та Bluetooth Classic
tags: [esp32, ble, nimble, bluetooth, beacon]
date: 2026-09-27
---

# BLE та Bluetooth Classic

![](../../../ESP32-Reference/assets/img/placeholder.png)

**BLE** - на всіх ESP32 (датчики, beacon). **BT Classic (SPP/A2DP)** - тільки ESP32 Classic, на S3/C3/C6 його немає!

> [!warning] BT Classic тільки на ESP32
> Якщо треба SPP-термінал або A2DP-аудіо - бери саме Classic. На S3/C3 - тільки BLE (+NIMBLE).

## Призначення

BLE та Bluetooth Classic - Порівняння; Таблиця з'єднань; Код - BLE beacon / server. BLE - на всіх ESP32 (датчики, beacon). BT Classic (SPP/A2DP) - тільки ESP32 Classic, на S3/C3/C6 його немає! Якщо треба SPP-термінал або A2DP-аудіо - бери саме Classic. На S3/C3 - тільки BLE (+NIMBLE).

## Порівняння

| Параметр | BLE | BT Classic |
| --- | --- | --- |
| Чіпи | всі ESP32 | тільки Classic |
| Профілі | GATT server/client, beacon | SPP, A2DP |
| Струм | ~10-30 мА (advertising) | ~50-100 мА |
| Стек | Bluedroid / NIMBLE (легший) | Bluedroid |
| Дальність | до 50-100 м (coded PHY на C3) | ~10 м |

| Роль BLE | Опис |
| --- | --- |
| Server (peripheral) | сенсор віддає дані, телефон читає |
| Client (central) | ESP32 збирає дані з сенсорів-beacon |
| Beacon | тільки advertising, без з'єднання |

## Таблиця з'єднань

| ESP32 | Периферія | Примітка |
| --- | --- | --- |
| 3V3/GND | живлення | BLE піки менші за WiFi, але конденсатор лишити |
| GPIO21/22 | I2C сенсор (BME280) | дані для GATT-характеристики |
| GPIO2 | LED | blink при connect |

## Код - BLE beacon / server

**Arduino (NIMBLE server):**

```cpp
#include <NimBLEDevice.h>
void setup() {
  NimBLEDevice::init("ESP32_Sensor");
  NimBLEServer *s = NimBLEDevice::createServer();
  NimBLEService *svc = s->createService("181A");
  NimBLECharacteristic *c = svc->createCharacteristic("2A6E", NIMBLE_PROPERTY::READ | NIMBLE_PROPERTY::NOTIFY);
  c->setValue("23.5");
  svc->start();
  s->getAdvertising()->addServiceUUID("181A");
  s->getAdvertising()->start();
}
void loop() {}
```

**ESP-IDF:** компонент BT Bluedroid/NIMBLE, приклад `ble/gatt_server`; ініт `esp_bt_controller_mem_release(ESP_BT_MODE_CLASSIC_BT)` щоб лишити тільки BLE.

**MicroPython (beacon):**

```python
import bluetooth
from micropython import const
_IRQ_CENTRAL_CONNECT = const(1)
ble = bluetooth.BLE()
ble.active(True)
# advertising payload: flags + name
adv = bytes([0x02,0x01,0x06, 0x0B,0x09]) + b"ESP32_BEAC"
ble.gap_advertise(100000, adv)
print("beacon on")
```

## GATT-сервер покроково

GATT-сервер - це дерево: **Profile → Service → Characteristic → Descriptor**. Клієнт (телефон) читає/пише характеристики і підписується на оновлення.

```text
Profile (твій пристрій "ESP32_Sensor")
└── Service 0x181A (Environmental Sensing)
    ├── Characteristic 0x2A6E (Temperature), props: READ | NOTIFY
    │   └── Descriptor 0x2902 (CCCD) — клієнт пише 0x0001 щоб увімкнути notify
    └── Characteristic 0x2A6F (Humidity), props: READ
```

Кроки створення сервера:

1. **Ініт стека** (`NimBLEDevice::init("NAME")` / `ble.active(True)`).
2. **Створити сервер** (peripheral-роль).
3. **Створити сервіс** за 16-бітним UUID (стандартні: 0x1800 Generic Access, 0x180F Battery, 0x181A Environmental) або 128-бітним власним.
4. **Додати характеристики**: UUID + властивості (READ / WRITE / NOTIFY / INDICATE) + права доступу + початкове значення.
5. **CCCD-дескриптор 0x2902** - обов'язковий для NOTIFY/INDICATE. Без нього iOS/Android не підпишуться (див. помилки нижче).
6. **`svc->start()`** - активувати сервіс.
7. **Advertising**: додати Service UUID в adv-пакет + `start()` (інтервал 100-1000 мс; менше = швидше знаходять, більше струм).
8. **Цикл оновлення**: `setValue()` + `notify()` при нових даних сенсора.

> [!tip] 16-біт vs 128-біт UUID
> Стандартні сервіси бери 16-бітні (`"181A"`, `"2A6E"`). Власний сервіс (напр. UART-міст) - генеруй 128-бітний UUID, щоб не конфліктувати: `"6E400001-B5A3-F393-E0A9-E50E24DCCA9E"` (Nordic UART).

## NimBLE vs Bluedroid - вибір за пам'яттю

| Параметр | NimBLE | Bluedroid |
| --- | --- | --- |
| Flash | ~60-80 КБ | ~250-300 КБ |
| RAM (heap) | ~20-30 КБ | ~80-100+ КБ |
| BT Classic | немає (тільки BLE) | є (SPP/A2DP) - тільки ESP32 Classic |
| Ролі | peripheral + central | peripheral + central |
| З'єднань одночасно | до ~3-5 стабільно | до 7 (ціною RAM) |
| MTU / DLE | так | так |
| Підтримка в Arduino | `NimBLEDevice.h` (рекомендовано) | `BLEDevice.h` (важчий) |
| Коли брати | сенсори, beacon, батарея, S3/C3 | треба SPP/A2DP на Classic, або старий приклад |

Правило: **за замовчуванням - NimBLE**. Bluedroid - тільки якщо потрібен BT Classic або портіруєш старий код. На проєктах з WiFi + BLE одночасно NimBLE економить ~200 КБ flash - це різниця між «влізло OTA» і «не влізло» (див. [Partitions](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md)).

В ESP-IDF вибір - через menuconfig `Component config → Bluetooth → NimBLE` vs `Bluedroid`, приклад: `examples/bluetooth/nimble/gatt_server`.

## MTU: переговори, 185 / 517

За замовчуванням ATT MTU = **23 байти** (корисне навантаження ~20 байт). Після `MTU Exchange` сторони узгоджують більше:

| Сценарій | MTU | Корисних байт | Коментар |
| --- | --- | --- | --- |
| Default (без exchange) | 23 | 20 | повільно, але сумісно з усім |
| NimBLE + Android (типово) | 185 | 182 | реальний типовий результат |
| ESP-IDF max (BLE 4.2 DLE) | 517 | 514 | максимум стандарту, не всі телефони дають |
| iOS (типово) | 185 | 182 | iOS ріже до 185 |

Що робити в коді:

- Сервер: `NimBLEDevice::setMTU(517)` - запитати максимум; стек сам сторгується вниз.
- Не ріж пакети по 20 байт вручну - перевіряй `conn->getMTU()` і фрагментуй дані сенсора (напр. JSON) відповідно.
- Великий MTU + notify = швидка передача логів/прошивок по BLE, але пам'ять буферів росте - на S3 з PSRAM ок, на C3 без PSRAM обережно.

## Bonding, passkey, безпека

| Рівень | Що дає | Коли |
| --- | --- | --- |
| Just Works (без MITM) | шифрування без PIN | сенсори вдома, beacon |
| Passkey (6 цифр) | захист від MITM | замок, медичний датчик |
| OOB / Numeric Comparison | максимум | платіжні/критичні (рідко на ESP32) |
| Bonding (збереження ключів) | перепідключення без PIN | все, де є passkey |

Мінімальний патерн: увімкнути bonding + passkey на сервері, ключі зберігаються в NVS (див. [NVS](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md)). Після `Factory reset` - видалити bond з обох боків, інакше помилка шифрування `0x05 / 0x06`.

> [!warning] Не роби «секретні» дані через відкритий READ
> BLE-sniffer (nRF Sniffer) бачить усе незашифроване. Калібрувальні константи - ок, а токени WiFi через GATT без bonding - ні.

## Notify vs Indicate

| Параметр | Notify (0x0001 в CCCD) | Indicate (0x0002 в CCCD) |
| --- | --- | --- |
| Підтвердження | немає (fire-and-forget) | є (ATT Handle Value Confirmation) |
| Швидкість | висока (потік температури 10 Гц) | низька (~2-5× повільніше) |
| Надійність | може губити при перевантаженні | гарантована доставка по черзі |
| Споживання | менше | більше (радіо довше активне) |
| Коли | сенсори, стрім | аларми, команди «відкрий замок» |

Правило: **сенсор → notify; команда/аларм → indicate або write-with-response**.

Період notify для температури/вологості - 1 с достатньо; 50 Гц акселерометра по notify з MTU 185 - вже межа, краще агрегувати.

## Код - beacon + UART-сервіс у 3 фреймворках

Сервіс Nordic UART (NUS): RX-характеристика (WRITE, телефон → ESP32), TX-характеристика (NOTIFY, ESP32 → телефон). UUID 128-бітні `6E40000X-B5A3-F393-E0A9-E50E24DCCA9E`.

**Arduino (NimBLE, UART-сервіс + beacon):**

```cpp
#include <NimBLEDevice.h>
#define SVC_UUID "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
#define CHR_RX   "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"  // WRITE
#define CHR_TX   "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"  // NOTIFY
NimBLECharacteristic *txChr;

class RxCb : public NimBLECharacteristicCallbacks {
  void onWrite(NimBLECharacteristic *c) {
    String s = c->getValue();
    Serial.print("RX: "); Serial.println(s);
    txChr->setValue("echo:" + s);
    txChr->notify();  // спрацює лише якщо клієнт записав 0x0001 у 0x2902
  }
};

void setup() {
  Serial.begin(115200);
  NimBLEDevice::init("ESP32_UART");
  NimBLEDevice::setMTU(517);
  NimBLEDevice::setSecurityAuth(true, true, true);  // bonding для прикладу
  NimBLEServer *srv = NimBLEDevice::createServer();
  NimBLEService *svc = srv->createService(SVC_UUID);
  auto *rx = svc->createCharacteristic(CHR_RX, NIMBLE_PROPERTY::WRITE);
  rx->setCallbacks(new RxCb());
  txChr = svc->createCharacteristic(CHR_TX, NIMBLE_PROPERTY::READ | NIMBLE_PROPERTY::NOTIFY);
  // NimBLE створює дескриптор 0x2902 автоматично для NOTIFY-характеристики
  txChr->setValue("hello");
  svc->start();
  auto *adv = srv->getAdvertising();
  adv->addServiceUUID(SVC_UUID);
  adv->setScanResponse(true);
  adv->start();  // інтервал за замовч. ~100 мс
}
void loop() {
  static uint32_t t = 0;
  if (millis() - t > 2000) {  // періодичний notify сенсора
    t = millis();
    txChr->setValue("temp=23.5");
    txChr->notify();
  }
  delay(10);
}
```

**ESP-IDF (NimBLE GATT-сервер, скорочено):**

```c
// Приклад: examples/bluetooth/nimble/gatt_server (menuconfig: NimBLE, GATT Server)
// Ключові кроки:
// 1. nimble_port_init(); ble_hs_cfg.store_status_cb = ...;
// 2. Опис таблиці GATT:
//    struct ble_gatt_svc_def gatt_svcs[] = {
//      {.type = BLE_GATT_SVC_TYPE_PRIMARY,
//       .uuid = BLE_UUID128_DECLARE(0x9E,0xCA,...), // NUS 128-bit
//       .characteristics = (struct ble_gatt_chr_def[]) {
//         {.uuid = BLE_UUID128_DECLARE(...02...),
//          .access_cb = rx_access_cb,
//          .flags = BLE_GATT_CHR_F_WRITE},
//         {.uuid = BLE_UUID128_DECLARE(...03...),
//          .access_cb = tx_access_cb,
//          .flags = BLE_GATT_CHR_F_READ | BLE_GATT_CHR_F_NOTIFY,
//          .descriptors = (struct ble_gatt_dsc_def[]) {
//            {.uuid = BLE_UUID16_DECLARE(0x2902),  // CCCD вручну!
//             .att_flags = BLE_ATT_F_READ | BLE_ATT_F_WRITE,
//             .access_cb = cccd_access_cb},
//            {0}}},
//         {0}}},
//      {0}};
// 3. ble_gatts_count_cfg(...); ble_gatts_add_svcs(gatt_svcs);
// 4. Advertising: ble_gap_adv_start(... conn_mode=UND, disc_mode=GEN,
//    itvl 160 (=100 мс, одиниці 0.625 мс)).
// 5. MTU:GRAN ble_att_set_preferred_mtu(517); подія BLE_GAP_EVENT_MTU.
// 6. Bonding: ble_hs_cfg.sm_bonding = 1; sm_mitm = 1; sm_io_cap = BLE_SM_IO_CAP_DISP_ONLY (passkey на дисплеї).
```

**MicroPython (beacon iBeacon + UART-сервіс):**

```python
import bluetooth, struct, time
from micropython import const
_IRQ_CENTRAL_CONNECT, _IRQ_CENTRAL_DISCONNECT = const(1), const(2)
_IRQ_GATTS_WRITE = const(3)
ble = bluetooth.BLE()
ble.active(True)
ble.config(mtu=517)  # попросити максимум (сторгується сам)

# --- iBeacon payload: company(Apple 0x004C) + type + UUID + major/minor + tx ---
def ibeacon_adv(uuid16, major, minor, txp=-59):
    prefix = bytes([0x02,0x01,0x06, 0x1A,0xFF, 0x4C,0x00, 0x02,0x15])
    body = uuid16 + struct.pack(">HHb", major, minor, txp)
    return prefix + body

UUID = bytes.fromhex("6E400001B5A3F393E0A9E50E24DCCA9E")
ble.gap_advertise(100000, ibeacon_adv(UUID, 1, 7))
print("ibeacon on")

# --- UART-сервіс (NUS) ---
SVC = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
CHR_RX = (bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_WRITE,)
CHR_TX = (bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
SRV = (SVC, (CHR_RX, CHR_TX))
handles = ble.gatts_register_services((SRV,))
h_rx, h_tx = handles[0][0], handles[0][1]

def irq(ev, data):
    if ev == _IRQ_CENTRAL_CONNECT:
        print("central connected")
    elif ev == _IRQ_GATTS_WRITE:
        conn, attr = data
        print("RX:", ble.gatts_read(h_rx))
        ble.gatts_notify(conn, h_tx, b"echo-ok")  # треба підписка на CCCD з боку телефона
ble.irq(irq)
```

Перевірка телефоном: **nRF Connect** → вкладка Advertise → знайти `ESP32_UART` → Connect → увімкнути «стрілку вгору» (CCCD notify) → читати TX.

## Типові помилки

| Симптом | Причина | Лікування |
| --- | --- | --- |
| `GATT error 133 (0x85)` на Android | стек телефона/ESP32 розсинхронізувався, переповнення черги, одночасні connect+scan | `disconnect()` + `close()` на телефоні, перезапуск advertise на ESP32; зменшити частоту notify; не сканувати під час з'єднання |
| iOS не бачить / не підписується | немає CCCD 0x2902; notify без підписки; закешований сервіс зі старим UUID | додати дескриптор 0x2902; чекати підписки перед `notify()`; змінити MAC/name або «Forget device» на iOS |
| `notify()` мовчить, хоча connect є | клієнт не записав 0x0001 у CCCD | перевірити колбек `onSubscribe()` / читати CCCD перед notify |
| Обрізані пакети 20 байт | MTU не узгоджено (лишилось 23) | викликати MTU exchange, читати `getMTU()`, фрагментувати |
| `ESP_GATT_NO_RESOURCES` / падіння | забагато з'єднань на Bluedroid без RAM | перейти на NimBLE, зменшити `max_connections` до 2-3 |
| Не конектиться після bonding | ключі в NVS розійшлися (прошивка стерла одну сторону) | «Forget» на телефоні + `nvs_flash_erase()` або новий passkey |
| Beacon видно, GATT - ні | advertise-пакет без Service UUID (тільки name) | `addServiceUUID()` + scan-response з ім'ям |

> [!tip] Чек-лист «не працює BLE»
>
> 1. Телефон бачить advertise? (nRF Connect). 2. Connect проходить? 3. Сервіси видно? 4. CCCD записано? 5. MTU яке? 6. Логи NimBLE (`CONFIG_BT_NIMBLE_LOG_LEVEL_DEBUG`). 90% кейсів закриваються пунктами 1-4.

### Mermaid: не бачить / не конектиться BLE

```mermaid
flowchart TB
    NB[Не бачить пристрій] --> ADV{Реклама йде?}
    ADV -->|Ні| START[Запустити advertising + правильні UUID]
    ADV -->|Так| PHONE{Телефон бачить?}
    PHONE -->|Ні| CACHE[Скинути BLE-кеш телефону!]
    PHONE -->|Так| MTU{Обрив при читанні?}
    MTU -->|Так| SMALL[Менший MTU (23–185), повільніше]
```

## Офіційні джерела

- [NimBLE + Bluedroid (ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/index.html) - стеки, GATT, GAP.
- [Bluetooth GAP/GATT огляд](https://www.bluetooth.com/specifications/specs/) - сервіси, характеристики.

## Див. також

- [Home](../../../ESP32-Reference/Home.md)
- [01-ESP32-Classic](../../../ESP32-Reference/01-Hardware/01-ESP32-Classic.md)
- [WiFi](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md)
- [ESP-NOW](../../../ESP32-Reference/05-Radio/03-ESP-NOW.md)
- [I2C сенсори](../../../ESP32-Reference/10-Sensori/03-BME280-BMP280-SHT31.md)
- [MQTT](../../../ESP32-Reference/05-Radio/03-ESP-NOW.md)
- [Sleep](../../../ESP32-Reference/07-Timeri-Son/03-Sleep-ULP.md)
