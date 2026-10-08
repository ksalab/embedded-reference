---
description: ESP-NOW - P2P без роутера - Схема gateway ESP-NOW → MQTT; Таблиця з'єднань (сенсорний вузол); Код - send / recv
category: Radio
title: ESP-NOW - P2P без роутера
tags: [esp32, esp-now, mac, mqtt, gateway, p2p]
date: 2026-09-27
---

# ESP-NOW - P2P без роутера

![[assets/img/placeholder.png]]

ESP-NOW - фірмовий P2P-протокол Espressif: до **250 байт** на пакет, без роутера, затримка ~1-10 мс. Ідеально для сенсорної мережі + один gateway у WiFi/MQTT.

> [!info] Як працює pairing
> Кожен вузол знає **MAC** піра (6 байт). Канал WiFi має збігатися на всіх (1-13). Шифрування PMK/LMK - опційно.

## Призначення

ESP-NOW - P2P без роутера - Схема gateway ESP-NOW → MQTT; Таблиця з'єднань (сенсорний вузол); Код - send / recv. ESP-NOW - фірмовий P2P-протокол Espressif: до 250 байт на пакет, без роутера, затримка ~1-10 мс. Ідеально для сенсорної мережі + один gateway у WiFi/MQTT. Кожен вузол знає MAC піра (6 байт). Канал WiFi має збігатися на всіх (1-13). Шифрування PMK/LMK - опційно.

## Характеристики

| Параметр | Значення |
| --- | --- |
| Розмір пакета | ≤250 байт |
| Пірів | до 20 (шифр.) / більше відкритих |
| Канал | 1-13, спільний для всіх |
| Дальність | ~100-200 м (open), з антеною більше |
| Струм | TX ~200 мА пік, сон між пакетами |

## Схема gateway ESP-NOW → MQTT

```text
[Sensors ×N --ESP-NOW--> Gateway ESP32 --WiFi/MQTT--> Broker]
   MAC:pair, ch=1            STA+AP, ch=1
```

| Вузол | Роль | Налаштування |
| --- | --- | --- |
| Sensor 1..N | ESP-NOW TX | channel 1, peer = MAC gateway, deep-sleep між відправками |
| Gateway | ESP-NOW RX + WiFi STA | фіксований канал 1, форвардить у [[05-Radio/03-ESP-NOW | MQTT]] |

> [!warning] Канал роутера vs ESP-NOW
> Якщо gateway в STA на каналі 6, а сенсори шлють на 1 - пакети губляться. Фіксуй канал роутера або канал ESP-NOW однаковим.

## Таблиця з'єднань (сенсорний вузол)

| ESP32 сенсора | Периферія | Примітка |
| --- | --- | --- |
| GPIO21/22 | BME280 I2C | дані для пакета |
| GPIO33 | LED | blink при send OK |
| 3V3 | Li-ion + LDO | deep-sleep 10 мкА |

## Код - send / recv

**Arduino (TX):**

```cpp
#include <esp_now.h>
#include <WiFi.h>
uint8_t peer[] = {0x24,0x6F,0x28,0xAA,0xBB,0xCC};
typedef struct { float t; float h; } Msg;
void setup() {
  WiFi.mode(WIFI_STA); WiFi.disconnect();
  esp_now_init();
  esp_now_peer_info_t p = {}; memcpy(p.peer_addr, peer, 6); p.channel = 1; p.encrypt = false;
  esp_now_add_peer(&p);
  Msg m = {23.5, 55.0};
  esp_now_send(peer, (uint8_t*)&m, sizeof(m));
}
void loop() {}
```

**Arduino (RX gateway):**

```cpp
#include <esp_now.h>
#include <WiFi.h>
void onRecv(const uint8_t *mac, const uint8_t *data, int len) { Serial.printf("got %d bytes\n", len); }
void setup() { WiFi.mode(WIFI_STA); esp_now_init(); esp_now_register_recv_cb(onRecv); }
void loop() {}
```

**ESP-IDF:** `esp_now_init + esp_now_add_peer + esp_now_send`, колбек `esp_now_register_recv_cb`.

**MicroPython (espnow):**

```python
import network, espnow
w = network.WLAN(network.STA_IF); w.active(True); w.disconnect()
e = espnow.ESPNow(); e.active(True)
e.add_peer(b"\x24\x6f\x28\xaa\xbb\xcc")
e.send(b"hello")
print(e.recv())
```

### Mermaid: пакети не доходять

```mermaid
flowchart TB
    ND[Не доходять] --> CH2{Один канал у всіх?}
    CH2 -->|Ні| FIX[Зафіксувати канал (1–11), без стрибків!]
    CH2 -->|Так| PEER{Peer додано з MAC?}
    PEER -->|Ні| ADD[esp_now_add_peer + той самий PMK]
    PEER -->|Так| ENC{Шифрування збігається?}
    ENC -->|Ні| PMK[Однаковий PMK/LMK або без шифру]
    ENC -->|Так| PWR3[Потужність TX + антени]
```

## Шифровані піри + колбеки прийому

```cpp
// ESP-NOW: прийом з розбором + автовідповідь (Arduino-ESP32)
#include <esp_now.h>
#include <WiFi.h>
typedef struct { uint8_t id; float t; float h; } Packet;
void onRecv(const esp_now_recv_info_t *info, const uint8_t *data, int len) {
  if (len != sizeof(Packet)) return;  // чужий формат — ігнор!
  Packet p; memcpy(&p, data, len);
  Serial.printf("від %02X:%02X t=%.1f h=%.0f
", info->src_addr[4], info->src_addr[5], p.t, p.h);
}
void setup() {
  WiFi.mode(WIFI_STA);
  WiFi.channel(6);  // ФІКСОВАНИЙ канал — як у відправника!
  esp_now_init();
  esp_now_register_recv_cb(onRecv);
}
```

### Ліміти, про які мовчать приклади

| Ліміт | Значення | Наслідок |
| --- | --- | --- |
| Пейлоад | 250 байт | Більше - різати вручну |
| Шифрованих пірів | 6 (LMK) | Сьомий - тільки відкритий |
| Пірів всього | 20 | Зірка, не mesh! |
| Канал | Спільний з WiFi | WiFi-скан = розрив ESP-NOW |
| Дальність | ~100-200 м прямої видимості | Стіни ріжуть як WiFi |

## Типові помилки

| # | Помилка | Чому погано | Як правильно |
| --- | --- | --- | --- |
| 1 | Різні канали | Фізично не чують одне одного | Один канал скрізь |
| 2 | Немає peer | ESP-NOW шле тільки знайомим | add_peer з MAC |
| 3 | PMK різні | Дешифрування падає мовчки | Один PMK або без шифру |
| 4 | WiFi-сканування паралельно | Канал стрибає | Не сканувати під час ESP-NOW |
| 5 | Довгі пакети >250 байт | Обрізаються | Фрагментація вручну |

## Офіційні джерела

- [ESP-NOW Guide (ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html) - peer, PMK, колбеки.
- [ESP-NOW + WiFi coexistence](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/coexist.html) - спільний канал.

## Див. також

- [[Home]]
- [[01-Hardware/01-ESP32-Classic]]
- [[05-Radio/01-WiFi-STA-AP|WiFi]]
- [[05-Radio/04-ESP-MESH|ESP-MESH]]
- [[05-Radio/03-ESP-NOW|MQTT]]
- [[07-Timeri-Son/03-Sleep-ULP|Sleep]]
- [[10-Sensori/03-BME280-BMP280-SHT31|I2C сенсори]]
