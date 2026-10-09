---
title: BLE and Bluetooth Classic
description: Compares BLE and Bluetooth Classic, wiring, GATT server, MTU negotiation and bonding; shows schematics, code and tables.
tags: [esp32, ble, nimble, bluetooth, beacon]
category: Radio
lang: en
original: 05-Radio/02-BLE-Bluetooth.md
date: 2026-10-08
---

# BLE and Bluetooth Classic

![[assets/img/placeholder.png]]

**BLE** - on all ESP32 (sensors, beacons). **BT Classic (SPP/A2DP)** - only on ESP32 Classic, S3/C3/C6 do not have it!

> [!warning] BT Classic only on ESP32
> If you need an SPP terminal or A2DP audio - take exactly the Classic. On S3/C3 - only BLE (+NIMBLE).

## Purpose

BLE and Bluetooth Classic - Comparison; Connection table; Code - BLE beacon / server. BLE - on all ESP32 (sensors, beacons). BT Classic (SPP/A2DP) - only on ESP32 Classic, S3/C3/C6 do not have it! If you need an SPP terminal or A2DP audio - take exactly the Classic. On S3/C3 - only BLE (+NIMBLE).

## Comparison

| Parameter | BLE | BT Classic |
| --- | --- | --- |
| Chips | all ESP32 | only Classic |
| Profiles | GATT server/client, beacon | SPP, A2DP |
| Current | ~10-30 mA (advertising) | ~50-100 mA |
| Stack | Bluedroid / NIMBLE (lighter) | Bluedroid |
| Range | up to 50-100 m (coded PHY on C3) | ~10 m |

| BLE role | Description |
| --- | --- |
| Server (peripheral) | sensor serves data, phone reads |
| Client (central) | ESP32 collects data from sensor beacons |
| Beacon | advertising only, no connection |

## Connection table

| ESP32 | Peripheral | Note |
| --- | --- | --- |
| 3V3/GND | power supply | BLE peaks are smaller than WiFi, but keep the capacitor |
| GPIO21/22 | I2C sensor (BME280) | data for the GATT characteristic |
| GPIO2 | LED | blinks on connect |

## Code - BLE beacon / server

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

**ESP-IDF:** BT component Bluedroid/NIMBLE, example `ble/gatt_server`; init `esp_bt_controller_mem_release(ESP_BT_MODE_CLASSIC_BT)` to keep BLE only.

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

## GATT server step by step

A GATT server is a tree: **Profile → Service → Characteristic → Descriptor**. The client (phone) reads/writes characteristics and subscribes to updates.

```text
Profile (твій пристрій "ESP32_Sensor")
└── Service 0x181A (Environmental Sensing)
    ├── Characteristic 0x2A6E (Temperature), props: READ | NOTIFY
    │   └── Descriptor 0x2902 (CCCD) - клієнт пише 0x0001 щоб увімкнути notify
    └── Characteristic 0x2A6F (Humidity), props: READ
```

Steps to create a server:

1. **Init the stack** (`NimBLEDevice::init("NAME")` / `ble.active(True)`).
2. **Create the server** (peripheral role).
3. **Create a service** with a 16-bit UUID (standard: 0x1800 Generic Access, 0x180F Battery, 0x181A Environmental) or a 128-bit custom one.
4. **Add characteristics**: UUID + properties (READ / WRITE / NOTIFY / INDICATE) + access rights + initial value.
5. **CCCD descriptor 0x2902** - mandatory for NOTIFY/INDICATE. Without it iOS/Android will not subscribe (see issues below).
6. **`svc->start()`** - activate the service.
7. **Advertising**: add the Service UUID to the adv packet + `start()` (interval 100-1000 ms; smaller = found faster, more current).
8. **Update loop**: `setValue()` + `notify()` on new sensor data.

> [!tip] 16-bit vs 128-bit UUID
> Take standard services as 16-bit (`"181A"`, `"2A6E"`). For a custom service (e.g. UART bridge) - generate a 128-bit UUID so it does not conflict: `"6E400001-B5A3-F393-E0A9-E50E24DCCA9E"` (Nordic UART).

## NimBLE vs Bluedroid - memory-based choice

| Parameter | NimBLE | Bluedroid |
| --- | --- | --- |
| Flash | ~60-80 KB | ~250-300 KB |
| RAM (heap) | ~20-30 KB | ~80-100+ KB |
| BT Classic | no (BLE only) | yes (SPP/A2DP) - ESP32 Classic only |
| Roles | peripheral + central | peripheral + central |
| Simultaneous connections | up to ~3-5 stable | up to 7 (costs RAM) |
| MTU / DLE | yes | yes |
| Arduino support | `NimBLEDevice.h` (recommended) | `BLEDevice.h` (heavier) |
| When to take | sensors, beacons, battery, S3/C3 | need SPP/A2DP on Classic, or an old example |

Rule: **NimBLE by default**. Bluedroid - only if you need BT Classic or you port old code. On projects with WiFi + BLE at once NimBLE saves ~200 KB of flash - that is the difference between "OTA fits" and "does not fit" (see [[08-Memory/01-Partitions-NVS|Partitions]]).

In ESP-IDF the choice is via menuconfig `Component config → Bluetooth → NimBLE` vs `Bluedroid`, example: `examples/bluetooth/nimble/gatt_server`.

## MTU: negotiation, 185 / 517

By default ATT MTU is **23 bytes** (useful payload ~20 bytes). After `MTU Exchange` both sides agree on more:

| Scenario | MTU | Useful bytes | Comment |
| --- | --- | --- | --- |
| Default (no exchange) | 23 | 20 | slow but compatible with everything |
| NimBLE + Android (typical) | 185 | 182 | real typical result |
| ESP-IDF max (BLE 4.2 DLE) | 517 | 514 | standard maximum, not all phones grant it |
| iOS (typical) | 185 | 182 | iOS cuts to 185 |

What to do in code:

- Server: `NimBLEDevice::setMTU(517)` - ask for the maximum; the stack negotiates down by itself.
- Do not slice packets into 20 bytes manually - check `conn->getMTU()` and fragment sensor data (e.g. JSON) accordingly.
- Big MTU + notify = fast log/firmware transfer over BLE, but buffer memory grows - on S3 with PSRAM fine, on C3 without PSRAM be careful.

## Bonding, passkey, security

| Level | What it gives | When |
| --- | --- | --- |
| Just Works (no MITM) | encryption without PIN | home sensors, beacons |
| Passkey (6 digits) | MITM protection | lock, medical sensor |
| OOB / Numeric Comparison | maximum | payment/critical (rare on ESP32) |
| Bonding (key storage) | reconnect without PIN | everything with a passkey |

Minimal pattern: enable bonding + passkey on the server, keys are stored in NVS (see [[08-Memory/01-Partitions-NVS|NVS]]). After a `factory reset` - delete the bond on both sides, otherwise encryption error `0x05 / 0x06`.

> [!warning] Do not pass "secret" data via open READ
> A BLE sniffer (nRF Sniffer) sees everything unencrypted. Calibration constants are fine, but WiFi tokens via GATT without bonding are not.

## Notify vs Indicate

| Parameter | Notify (0x0001 in CCCD) | Indicate (0x0002 in CCCD) |
| --- | --- | --- |
| Acknowledge | none (fire-and-forget) | yes (ATT Handle Value Confirmation) |
| Speed | high (temperature stream 10 Hz) | low (~2-5x slower) |
| Reliability | may drop under load | guaranteed in-order delivery |
| Consumption | less | more (radio active longer) |
| When | sensors, streams | alarms, "open the lock" commands |

Rule: **sensor → notify; command/alarm → indicate or write-with-response**.

Notify period for temperature/humidity - 1 s is enough; a 50 Hz accelerometer over notify with MTU 185 is already the limit, better to aggregate.

## Code - beacon + UART service in 3 frameworks

Nordic UART service (NUS): RX characteristic (WRITE, phone → ESP32), TX characteristic (NOTIFY, ESP32 → phone). 128-bit UUIDs `6E40000X-B5A3-F393-E0A9-E50E24DCCA9E`.

**Arduino (NimBLE, UART service + beacon):**

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

**ESP-IDF (NimBLE GATT server, shortened):**

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

**MicroPython (iBeacon beacon + UART service):**

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

Check with a phone: **nRF Connect** → Advertise tab → find `ESP32_UART` → Connect → enable the "up arrow" (CCCD notify) → read TX.

## Common issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| `GATT error 133 (0x85)` on Android | phone/ESP32 stacks desynced, queue overflow, simultaneous connect+scan | `disconnect()` + `close()` on the phone, restart advertising on ESP32; lower notify rate; do not scan during a connection |
| iOS does not see / will not subscribe | no CCCD 0x2902; notify without subscription; cached service with old UUID | add descriptor 0x2902; wait for subscription before `notify()`; change MAC/name or "Forget device" on iOS |
| `notify()` is silent although connected | client did not write 0x0001 to CCCD | check the `onSubscribe()` callback / read CCCD before notify |
| Truncated 20-byte packets | MTU not negotiated (stayed 23) | run MTU exchange, read `getMTU()`, fragment |
| `ESP_GATT_NO_RESOURCES` / crash | too many connections on Bluedroid without RAM | switch to NimBLE, lower `max_connections` to 2-3 |
| Will not connect after bonding | NVS keys diverged (firmware wiped one side) | "Forget" on the phone + `nvs_flash_erase()` or a new passkey |
| Beacon visible, GATT not | advertise packet without Service UUID (name only) | `addServiceUUID()` + scan response with the name |

> [!tip] "BLE does not work" checklist
>
> 1. Does the phone see advertising? (nRF Connect). 2. Does Connect pass? 3. Are services visible? 4. Is CCCD written? 5. What is the MTU? 6. NimBLE logs (`CONFIG_BT_NIMBLE_LOG_LEVEL_DEBUG`). Points 1-4 close 90% of cases.

### Mermaid: BLE not visible / will not connect

```mermaid
flowchart TB
    NB[Device not visible] --> ADV{Advertising running?}
    ADV -->|No| START[Start advertising + correct UUIDs]
    ADV -->|Yes| PHONE{Phone sees it?}
    PHONE -->|No| CACHE[Reset the phone BLE cache!]
    PHONE -->|Yes| MTU{Drop on read?}
    MTU -->|Yes| SMALL[Smaller MTU (23-185), slower]
```

## Official sources

- [NimBLE + Bluedroid (ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/index.html) - stacks, GATT, GAP.
- [Bluetooth GAP/GATT overview](https://www.bluetooth.com/specifications/specs/) - services, characteristics.

## See also

- [[EN/Home.en]]
- [[EN/01-Hardware/01-ESP32-Classic.en]]
- [[EN/05-Radio/01-WiFi-STA-AP.en|WiFi]]
- [[EN/05-Radio/03-ESP-NOW.en|ESP-NOW]]
- [[EN/10-Sensors/03-BME280-BMP280-SHT31.en|I2C sensors]]
- [[EN/05-Radio/03-ESP-NOW.en|MQTT]]
- [[07-Timers/03-Sleep-ULP|Sleep]]
