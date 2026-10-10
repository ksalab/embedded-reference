---
title: ESP-NOW - P2P without a router
description: Explains ESP-NOW peer-to-peer radio, sensor-to-MQTT gateway scheme, pairing and callbacks; shows schematics, code and tables.
tags: [esp32, esp-now, mac, mqtt, gateway, p2p]
category: Radio
lang: en
original: 05-Radio/03-ESP-NOW.md
date: 2026-10-08
---

# ESP-NOW - P2P without a router

![[assets/img/placeholder.png]]

ESP-NOW is the proprietary Espressif P2P protocol: up to **250 bytes** per packet, no router, latency ~1-10 ms. Ideal for a sensor network + one gateway into WiFi/MQTT.

> [!info] How pairing works
> Each node knows the peer **MAC** (6 bytes). The WiFi channel must match on all nodes (1-13). PMK/LMK encryption is optional.

## Purpose

ESP-NOW - P2P without a router - Gateway scheme ESP-NOW → MQTT; Connection table (sensor node); Code - send / recv. ESP-NOW is the proprietary Espressif P2P protocol: up to 250 bytes per packet, no router, latency ~1-10 ms. Ideal for a sensor network + one gateway into WiFi/MQTT. Each node knows the peer MAC (6 bytes). The WiFi channel must match on all nodes (1-13). PMK/LMK encryption is optional.

## Characteristics

| Parameter | Value |
| --- | --- |
| Packet size | up to 250 bytes |
| Peers | up to 20 (encrypted) / more open |
| Channel | 1-13, shared by all |
| Range | ~100-200 m (open), more with an antenna |
| Current | TX ~200 mA peak, sleep between packets |

## Gateway scheme ESP-NOW → MQTT

```text
[Sensors ×N --ESP-NOW--> Gateway ESP32 --WiFi/MQTT--> Broker]
   MAC:pair, ch=1            STA+AP, ch=1
```

| Node | Role | Settings |
| --- | --- | --- |
| Sensor 1..N | ESP-NOW TX | channel 1, peer = gateway MAC, deep-sleep between sends |
| Gateway | ESP-NOW RX + WiFi STA | fixed channel 1, forwards to [[05-Radio/03-ESP-NOW.en | MQTT]] |

> [!warning] Router channel vs ESP-NOW
> If the gateway sits in STA on channel 6 while sensors send on 1 - packets are lost. Fix the router channel and the ESP-NOW channel to the same value.

## Sensor node connection table

| Sensor ESP32 | Peripheral | Note |
| --- | --- | --- |
| GPIO21/22 | BME280 I2C | packet data |
| GPIO33 | LED | blinks on send OK |
| 3V3 | Li-ion + LDO | 10 µA deep-sleep |

## Code - send / recv

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

**ESP-IDF:** `esp_now_init + esp_now_add_peer + esp_now_send`, callback `esp_now_register_recv_cb`.

**MicroPython (espnow):**

```python
import network, espnow
w = network.WLAN(network.STA_IF); w.active(True); w.disconnect()
e = espnow.ESPNow(); e.active(True)
e.add_peer(b"\x24\x6f\x28\xaa\xbb\xcc")
e.send(b"hello")
print(e.recv())
```

### Mermaid: packets do not arrive

```mermaid
flowchart TB
    ND[Packets lost] --> CH2{Same channel everywhere?}
    CH2 -->|No| FIX[Fix the channel (1-11), no hopping!]
    CH2 -->|Yes| PEER{Peer added with MAC?}
    PEER -->|No| ADD[esp_now_add_peer + same PMK]
    PEER -->|Yes| ENC{Encryption matches?}
    ENC -->|No| PMK[Same PMK/LMK or no encryption]
    ENC -->|Yes| PWR3[TX power + antennas]
```

## Encrypted peers + receive callbacks

```cpp
// ESP-NOW: прийом з розбором + автовідповідь (Arduino-ESP32)
#include <esp_now.h>
#include <WiFi.h>
typedef struct { uint8_t id; float t; float h; } Packet;
void onRecv(const esp_now_recv_info_t *info, const uint8_t *data, int len) {
  if (len != sizeof(Packet)) return;  // чужий формат - ігнор!
  Packet p; memcpy(&p, data, len);
  Serial.printf("від %02X:%02X t=%.1f h=%.0f
", info->src_addr[4], info->src_addr[5], p.t, p.h);
}
void setup() {
  WiFi.mode(WIFI_STA);
  WiFi.channel(6);  // ФІКСОВАНИЙ канал - як у відправника!
  esp_now_init();
  esp_now_register_recv_cb(onRecv);
}
```

### Limits the examples stay silent about

| Limit | Value | Consequence |
| --- | --- | --- |
| Payload | 250 bytes | More - slice manually |
| Encrypted peers | 6 (LMK) | Seventh - open only |
| Peers total | 20 | Star, not mesh! |
| Channel | Shared with WiFi | WiFi scan = ESP-NOW drop |
| Range | ~100-200 m line of sight | Walls cut like WiFi |

## Common issues

| # | Issue | Why it is bad | Correct way |
| --- | --- | --- | --- |
| 1 | Different channels | Physically cannot hear each other | One channel everywhere |
| 2 | No peer | ESP-NOW sends only to acquaintances | add_peer with MAC |
| 3 | Different PMKs | Decryption fails silently | One PMK or no encryption |
| 4 | WiFi scanning in parallel | Channel hops | Do not scan during ESP-NOW |
| 5 | Long packets over 250 bytes | Truncated | Manual fragmentation |

## Official sources

- [ESP-NOW Guide (ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html) - peers, PMK, callbacks.
- [ESP-NOW + WiFi coexistence](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/coexist.html) - shared channel.

## See also

- [[EN/Home.en]]
- [[EN/01-Hardware/01-ESP32-Classic.en]]
- [[EN/05-Radio/01-WiFi-STA-AP.en|WiFi]]
- [[EN/05-Radio/04-ESP-MESH.en|ESP-MESH]]
- [[EN/05-Radio/03-ESP-NOW.en|MQTT]]
- [[07-Timers/03-Sleep-ULP|Sleep]]
- [[EN/10-Sensors/03-BME280-BMP280-SHT31.en|I2C sensors]]
