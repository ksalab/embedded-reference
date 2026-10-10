---
title: Provisioning WiFi on ESP32 without reflashing
description: Provisioning - entry SSID/password (and MQTT-settings) in готовий пристрій without reflashing. Користувач підключається до тимчасової точки пристрою, вводить домашній WiFi - пристрій...
tags: [esp32, wifi, provisioning, captive, ble, rainmaker, protokoli]
category: Protokoli
date-created: 2026-09-28
date: 2026-09-28
lang: en
original: 15-Protocols/04-Provisioning.md
date: 2026-10-08
---

# Provisioning WiFi on ESP32 without reflashing

> [!warning] Відкритий портал provisioning without password and таймауту - дірка: будь-хто поруч перехопить пристрій!
> Пароль on SoftAP, таймаут порталу 3-5 хв, після успіху - гасити AP and чистити NVS at потребі.

База WiFi: [[05-Radio/01-WiFi-STA-AP]], зберігання облікових [[08-Memory/01-Partitions-NVS]], далі MQTT [[15-Protocols/01-MQTT|MQTT]], старт [[Home]].

## Призначення

Provisioning - entry SSID/password (and MQTT-settings) in готовий пристрій without reflashing. Користувач підключається до тимчасової точки пристрою, вводить домашній WiFi - пристрій перезапускається вже клієнтом.

Варіанти:

- **WiFiManager (Arduino)** - captive-портал, найпростіше for хобі.
- **wifi_provisioning + protocomm (IDF)** - BLE або SoftAP-транспорт, security1/2, продакшен-підхід.
- **Ручний AP-портал (MicroPython)** - сокет-сервер on 192.168.4.1, мінімум залежностей.
- **ESP RainMaker** - коли потрібні хмара, застосунок and claiming with коробки.
- **SmartConfig / BluFi** - застереження: крихко, лише legacy.

## Параметри

| Параметр | Значення | Примітка |
| --- | --- | --- |
| WiFiManager AP | SSID `ESP32-Setup`, IP 192.168.4.1 | captive-портал + DNS-перехоплення |
| IDF BLE-provisioning | GATT-сервіс protocomm, security1 (PoP) / security2 | телефон поруч, without відкритого AP |
| IDF SoftAP-provisioning | AP + HTTP-endpoints protocomm | how WiFiManager, але with шифруванням |
| MP-портал | свій `socket` + форма HTML | ~60 рядків, повний контроль |
| RainMaker | claiming + MQTT до хмари Espressif | застосунки iOS/Android Ready |
| SmartConfig | ESP-Touch per довжині пакетів | ламається on 5 ГГц/mesh, not радити |
| BluFi | BLE-канал закритого протоколу | лише Espressif-додаток, legacy |
| Безпека | пароль AP ≥ 8 символів, таймаут 180-300 с | після provision - стоп AP |
| Сховище | NVS (SSID/пасс), стирати at зміні власника | `nvs_flash_erase` / `WiFi.disconnect(true)` |
| Кнопка скидання | утримання GPIO 10 с → erase + reboot in портал | обов'язково for корпусного виробу |

![[assets/img/provisioning-blufi-rainmaker-scheme.png|600]]
*Рис. Provisioning-транспорта: BLE/SoftAP-портал віддає облікові, пристрій стає STA-клієнтом домашнього WiFi.*

### ASCII-схема

```text
ПЕРВИННИЙ СТАН (нема NVS-облікових / кнопка утримана)
────────────────────────────────────────────────────
 ESP32-AP "ESP32-Setup" (пароль! таймаут 180с)
   │
   ├─► Телефон підключається ──► captive-портал 192.168.4.1
   │     форма: SSID + пароль (+ MQTT-хост за потреби)
   │
   ├─► [IDF] BLE GATT protocomm security1 (PoP з наліпки) ──► ті самі поля
   │
   └─► Зберегти в NVS ──► стоп AP/BLE ──► reboot ──► STA до домашнього WiFi
                                                   │
ПІСЛЯ УСПІХУ: портал ЗАЧИНЕНО, пристрій ──► MQTT/HTTPS (див. 01/02)
НЕВДАЧА: лічильник 3 спроби ──► назад у портал (не висіти вічно!)
```

### Mermaid

```mermaid
graph LR
    P[Телефон<br/>браузер/BLE] -->|SSID+пароль| AP[ESP32-AP портал<br/>192.168.4.1]
    AP -->|зберегти NVS| STA[ESP32 STA<br/>домашній WiFi]
    STA -->|MQTT/HTTPS| NET[broker/бекенд]
    STA -.->|3 невдачі| AP
    BT[BLE protocomm<br/>security1] -->|альтернатива| STA
```

## WiFiManager (Arduino): captive-портал

Поведінка: стартує STA, немає збереженої мережі або конект провалився - піднімає AP + DNS + вебсервер. Captive-портал сам відкривається on телефоні.

Безпека мінімум: `autoConnect("ESP32-Setup", "SetupPass123")` (пароль!), `setConfigPortalTimeout(180)`, після успіху - звичайний `loop()`. Кастомні поля (MQTT-хост/порт) via `WiFiManagerParameter`, зберігати in NVS/Preferences.

Підводні: портал, that not закрився після provision (завис in AP+STA) - явно `stopConfigPortal()` / перезавантаження; старі облікові in NVS після зміни роутера - довге утримання кнопки → `WiFi.disconnect(true)` + reboot.

## wifi_provisioning + protocomm (IDF): BLE / SoftAP

Продакшен-шлях: транспорт BLE (телефон поруч, ефір чистий) або SoftAP + HTTP, поверх - protocomm-сесія with security:

- security0 - without шифрування, тільки розробка;
- security1 - Curve25519 + PoP (proof-of-possession with наліпки on корпусі);
- security2 - SRP6a, рекомендовано for серії.

Сценарій: `wifi_prov_mgr_init()` → `wifi_prov_mgr_start_provisioning(security, pop, service_name)` → застосунок/додаток передає SSID → подія `WIFI_PROV_END` → `wifi_prov_mgr_deinit()` (звільнити BLE-пам'ять!) → STA-конект. Після успіху BLE вимикати (`esp_bt_mem_release`) - інакше RAM тече.

## Ручний AP-портал (MicroPython)

Коли бібліотек немає: підняти AP `esp32-setup`, сокет on 80, віддати форму, прийняти POST, записати `wifi.json`, reboot. Плюс - нуль залежностей and повний контроль; мінус - самому робити валідацію, таймаут and dnS-перехоплення (without нього користувач іде on 192.168.4.1 вручну).

## ESP RainMaker - оглядово

Коли брати: потрібні віддалене керування with інтернету, Ready мобільні застосунки, claiming пристроїв, OTA with хмари - and немає своєї бекенд-команди. RainMaker дає агент on пристрої + хмару + застосунки; параметри (реле, температура) описуються моделлю and самі малюються in UI.

Коли not брати: локальний пристрій without інтернету, свій бекенд уже є (тоді MQTT/HTTP with розділів 01-02), жорсткі вимоги до приватності даних.

## SmartConfig / BluFi: застереження

- **SmartConfig (ESP-Touch):** кодує SSID довжинами пакетів. Ламається on 5 ГГц, mesh-роумінгу, ізольованих AP. Тільки legacy-підтримка старих партій.
- **BluFi:** закритий BLE-протокол під додаток Espressif. Працює, але прив'язує до чужого застосунку.
- Новим виробам - WiFiManager (хобі) або wifi_provisioning security1/2 (серія).

## code Arduino (WiFiManager, безпечний)

```cpp
#include <WiFi.h>
#include <WiFiManager.h>

#define RESET_PIN 0  // BOOT: утримати 10 с → забути WiFi

WiFiManagerParameter p_mqtt("mqtt", "MQTT host", "192.168.1.10", 40);

void setup() {
  Serial.begin(115200);
  pinMode(RESET_PIN, INPUT_PULLUP);
  WiFiManager wm;
  wm.addParameter(&p_mqtt);
  wm.setConfigPortalTimeout(180);          // не висіти вічно!
  wm.setConnectTimeout(20);
  // Скидання за кнопкою:
  if (digitalRead(RESET_PIN) == LOW) {
    delay(10000);
    if (digitalRead(RESET_PIN) == LOW) { wm.resetSettings(); ESP.restart(); }
  }
  // Пароль на AP — ОБОВ'ЯЗКОВО:
  if (!wm.autoConnect("ESP32-Setup", "SetupPass123")) {
    Serial.println("provision fail → reboot");
    ESP.restart();
  }
  Serial.println(WiFi.localIP());
  Serial.println(p_mqtt.getValue()); // → зберегти в Preferences/NVS
}

void loop() { /* робочий код: MQTT/HTTP */ }
```

## code ESP-IDF (wifi_provisioning via BLE)

```c
#include "wifi_provisioning/manager.h"

void prov_start(const char *pop) {
    wifi_prov_mgr_config_t cfg = {
        .scheme = wifi_prov_scheme_ble,
        .scheme_event_handler = WIFI_PROV_SCHEME_BLE_EVENT_HANDLER_FREE_BTDM,
    };
    wifi_prov_mgr_init(cfg);
    // service_name видно в ефірі; PoP — з наліпки на корпусі
    wifi_prov_mgr_start_provisioning(WIFI_PROV_SECURITY_1, pop,
                                     "ESP32_ABC123", NULL);
    // Чекати подію WIFI_PROV_END, далі:
    // wifi_prov_mgr_deinit(); → esp_bt_mem_release(ESP_BT_MODE_BTDM);
}

// Події: WIFI_PROV_CRED_RECV (облікові отримано),
// WIFI_PROV_CRED_SUCCESS / FAIL (3 FAIL → лишити портал, не reboot-цикл),
// WIFI_PROV_END → deinit + робочий режим STA.
```

## code MicroPython (ручний AP-портал)

```python
import network, socket, json, time, machine

CONF = "wifi.json"

def start_portal():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid="ESP32-Setup", password="SetupPass123")  # пароль!
    ap.ifconfig(("192.168.4.1", "255.255.255.0", "192.168.4.1", "8.8.8.8"))
    s = socket.socket(); s.bind(("0.0.0.0", 80)); s.listen(1)
    s.settimeout(1.0)
    t0 = time.time()
    while time.time() - t0 < 180:  # таймаут порталу!
        try: cl, _ = s.accept()
        except OSError: continue
        req = cl.recv(1024).decode()
        if "POST /save" in req:
            body = req.split("\r\n\r\n")[-1]  # ssid=..&pass=..&mqtt=..
            kv = dict(p.split("=") for p in body.split("&") if "=" in p)
            open(CONF, "w").write(json.dumps(kv))
            cl.send("HTTP/1.0 200 OK\r\n\r\nSaved. Rebooting...")
            cl.close(); time.sleep(1); machine.reset()
        else:
            html = ("<form method=POST action=/save>SSID:<input name=ssid><br>"
                    "PASS:<input name=pass type=password><br>"
                    "MQTT:<input name=mqtt value=192.168.1.10><br>"
                    "<input type=submit value=Save></form>")
            cl.send("HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n" + html)
        cl.close()
    machine.reset()  # таймаут вийшов — reboot у робочий режим

try:
    kv = json.load(open(CONF))
    sta = network.WLAN(network.STA_IF); sta.active(True)
    sta.connect(kv["ssid"], kv["pass"])
    for _ in range(40):
        if sta.isconnected(): break
        time.sleep(0.5)
    if not sta.isconnected(): start_portal()
except OSError:
    start_portal()  # конфіга нема → портал
```

## typical errors

| Симптом | Причина | Рішення |
| --- | --- | --- |
| Портал висить після provision | немає `deinit`/reboot, AP+STA одночасно | `wifi_prov_mgr_deinit()` / `ESP.restart()` після успіху |
| Пристрій not бачить нову мережу | старі облікові in NVS | кнопка 10 с → `resetSettings()` / `nvs_flash_erase` |
| Captive-портал not спливає | немає DNS-перехоплення (ручний портал) | йти вручну on 192.168.4.1; in WiFiManager увімкнено |
| Цикл reboot ↔ портал | FAIL without лічильника | 3 спроби → лишити портал, not ребутитись |
| BLE-provisioning with'їв RAM | BTDM not звільнено після deinit | `esp_bt_mem_release(ESP_BT_MODE_BTDM)` |
| Чужі підключаються до Setup-AP | відкритий AP without таймауту | пароль ≥ 8 символів + timeout 180 с |
| SmartConfig not ловить | 5 ГГц / mesh / ізоляція AP | тільки 2.4 ГГц або перейти on BLE/SoftAP |
| PoP-наліпка одна on партію | клонування доступу | унікальний PoP on пристрій (MAC-based) |

## official джерела

- [Protocomm - ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/provisioning/protocomm.html) - security0/1/2, BLE and SoftAP-транспорт.
- [WiFiManager - GitHub](https://github.com/tzapu/WiFiManager) - captive-портал, таймаути, кастомні параметри.
- [ESP RainMaker - Programming Guide](https://docs.espressif.com/projects/esp-rainmaker/en/latest/) - claiming, модель пристрою, OTA.
- [esp-rainmaker - GitHub](https://github.com/espressif/esp-rainmaker) - агент, приклади, застосунки.

## Див. також

- [[Home]]
- [[05-Radio/01-WiFi-STA-AP|WiFi STA/AP]] - режими, that перемикає provisioning
- [[08-Memory/03-OTA|OTA]] - оновлення вже provisioned-пристроїв
- [[08-Memory/01-Partitions-NVS|NVS]] - де лежать облікові, стирання
- [[99-Additions/02-Troubleshooting-FAQ|FAQ]] - портал not стартує, цикли
- [[15-Protocols/01-MQTT|MQTT]] - наступний крок після WiFi
- [[15-Protocols/02-HTTP-WebSocket|HTTP/WebSocket]] - наступний крок після WiFi
- [[15-Protocols/03-mDNS-NTP-TLS|mDNS/NTP/TLS]] - знахідка пристрою після provision
- [[15-Protocols/05-Cloud-Pipeline|Cloud-Pipeline]] - куди течуть дані

## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| Connection refused | Wrong broker/port or TLS cert missing | Verify URL, CA cert, firewall rules |
| Timeout / no response | Network unreachable / DNS failure | Check WiFi, mDNS/NTP server reachability |
| TLS handshake failed | Clock not set / wrong CA | Set time via NTP before TLS connect |

## Official sources

- [Espressif ESP-IDF Protocol Docs](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/index.html) - official protocol APIs.
- [Micropython umqtt / network docs](https://docs.micropython.org/en/latest/index.html) - MQTT and socket references.
