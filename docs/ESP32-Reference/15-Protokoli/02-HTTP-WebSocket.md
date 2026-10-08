---
title: HTTP REST та WebSocket на ESP32
description: HTTP - коли потрібен класичний REST до свого бекенда: `GET /api/state`, `POST /api/sensors` з JSON. WebSocket - коли потрібен дуплекс у реальному часі: дашборд, керування реле без...
tags: [esp32, http, https, websocket, rest, sse, protokoli]
category: Protokoli
date-created: 2026-09-28
date: 2026-09-28
---

# HTTP REST та WebSocket на ESP32

> [!warning] Довгі HTTPS-запити в `loop()` годують WDT-ресет, а TLS з'їдає ~40 КБ heap!
> Важкі запити - в окрему задачу FreeRTOS з запасом стеку, відповіді читати порціями.

Огляд мережі: [01-WiFi-STA-AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md), MQTT-альтернатива [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md), час/TLS [03-mDNS-NTP-TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md), старт [Home](../../../ESP32-Reference/Home.md).

## Призначення

HTTP - коли потрібен класичний REST до свого бекенда: `GET /api/state`, `POST /api/sensors` з JSON. WebSocket - коли потрібен дуплекс у реальному часі: дашборд, керування реле без опитування.

Коли брати HTTP:

- відправка телеметрії на свій сервер раз на хвилину;
- OTA-прошивка з URL (`update.start(url)`), див. [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md);
- конфіг з бекенда одним GET при старті.

Коли брати WebSocket / SSE:

- живий дашборд: AsyncWebServer + SSE штовхає дані в браузер;
- команди з браузера без перезавантаження сторінки;
- повний дуплекс - WebSocket-клієнт до свого сервера.

Коли НЕ брати: десятки вузлів з частими повідомленнями - дешевше MQTT, див. [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md).

## Параметри

| Параметр | Значення | Примітка |
| --- | --- | --- |
| IDF-клієнт | `esp_http_client` (GET/POST/PUT, keep-alive, chunked) | блокуючий `perform()` |
| IDF-сервер | `esp_http_server` | для локальних сторінок |
| Arduino-клієнт | `HTTPClient` (обгортка над WiFiClient) | простий, синхронний |
| Arduino-сервер | ESPAsyncWebServer + SSE | неблокуючий, події в браузер |
| MP-клієнт | `urequests` (GET/POST JSON) | відповідь закривати! |
| MP-сервер | picoweb / micropython-async вебсервер | тільки прості сторінки |
| WebSocket IDF | `esp_websocket_client` | окремий компонент реєстру |
| WebSocket Arduino | WebSocketsClient (Links2004) | текст/бінарні кадри |
| HTTPS | CA-bundle або один CA PEM | час через NTP обов'язково |
| RAM під TLS | ~40 КБ heap на сесію | не тримати 2 TLS-сесії на C3 |
| WDT | довгі запити > 2-3 с в loop = ребут | окрема задача / async |

![](../../../ESP32-Reference/assets/img/http-websocket-rest-scheme.png)
*Рис. REST (запит→відповідь) і WebSocket/SSE (постійний канал) між ESP32, бекендом і браузером.*

### ASCII-схема

```text
ESP32 (клієнт)                    Свій бекенд (192.168.1.20:8000)
──────────────                    ─────────────────────────────
 POST /api/sensors {"t":24.5} ──► 200 OK {"cmd":"relay_off"}
 GET  /api/config?v=3 ────────► 200 OK {"period":60}
 HTTPS ──► CA-bundle перевірка ──► TLS handshake (час NTP!)
 chunked ──► читати порціями, не чекати весь body в RAM

ESP32 (сервер AsyncWebServer:80)      Браузер дашборда
────────────────────────────────      ────────────────
 GET / ──► index.html (SPIFFS/LittleFS)
 GET /events (SSE) ──► text/event-stream: data: {"t":24.5}
 WS /ws ◄──► дуплекс: {"relay":"ON"} ◄──► {"state":"ON"}
```

### Mermaid

```mermaid
graph LR
    ESP[ESP32<br/>HTTP-клієнт] -->|POST JSON| API[Бекенд API<br/>:8000]
    API -->|GET config| ESP
    ESP -->|HTTPS CA-bundle| API
    BR[Браузер] -->|GET /| WEB[ESP32 AsyncWebServer]
    WEB -->|SSE /events| BR
    WEB <-->|WS /ws| BR
```

## REST GET/POST JSON до свого бекенда

Контракт прикладного API (вигадати свій, але зафіксувати версію):

```text
POST /api/v1/sensors   body: {"id":"esp32-01","t":24.5,"h":55} → 200 {"ok":true}
GET  /api/v1/config?id=esp32-01 → 200 {"period":60,"relay":"auto"}
```

Правила: `Content-Type: application/json`, таймаут 5-10 с, 3 спроби з backoff, відповідь парсити потоково (ArduinoJson з фільтром), код стану логувати. Період відправки зберігати в NVS, див. [01-Partitions-NVS](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md).

## HTTPS з CA-бандлом

Варіанти перевірки сервера (від безпечного до тестового):

1. CA-bundle Mozilla в прошивці (IDF: `crt_bundle_attach`, Arduino: вшитий PEM) - продакшен.
2. Один кореневий CA свого сервера - свій VPS з Let's Encrypt.
3. Fingerprint SHA-1/SHA-256 - крихко (ламається при перевипуску), тільки тимчасово.
4. `setInsecure()` - тільки стенд у локалці, ніколи в прод.

Без синхронізованого часу (NTP) перевірка сертифіката завжди FAIL - див. [03-mDNS-NTP-TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md).

## WebSocket-дуплекс і AsyncWebServer + SSE

- SSE (`/events`): сервер штовхає телеметрію в браузер, перепідключення автоматичне. Дешево, вистачає для дашборда.
- WebSocket (`/ws`): дуплекс - слайдер/кнопка в браузері керує ESP32 без перезавантаження.
- На IDF - компонент `esp_websocket_client` для клієнта; сервер - `esp_http_server` з WS-хендлером.
- На Arduino - WebSocketsClient для клієнта, ESPAsyncWebServer для сервера+S biomarkerSSE.
- Не тримати одночасно WS-сервер на 4+ клієнтів і HTTPS-клієнт на C3 без PSRAM - не вистачить heap.

## Код ESP-IDF (esp_http_client + WebSocket)

```c
#include "esp_http_client.h"
#include "esp_websocket_client.h"

// --- REST POST JSON ---
void post_sensors(const char *json) {
    esp_http_client_config_t cfg = {
        .url = "http://192.168.1.20:8000/api/v1/sensors",
        .timeout_ms = 8000,
        // .crt_bundle_attach = esp_crt_bundle_attach, // для https
    };
    esp_http_client_handle_t c = esp_http_client_init(&cfg);
    esp_http_client_set_method(c, HTTP_METHOD_POST);
    esp_http_client_set_header(c, "Content-Type", "application/json");
    esp_http_client_set_post_field(c, json, strlen(json));
    esp_err_t err = esp_http_client_perform(c);
    if (err == ESP_OK)
        ESP_LOGI("HTTP", "status=%d", esp_http_client_get_status_code(c));
    esp_http_client_cleanup(c); // обов'язково, інакше витік сокетів
}

// --- WebSocket-клієнт (дуплекс) ---
static void ws_event(void *a, esp_event_base_t b, int32_t id, void *d) {
    esp_websocket_event_data_t *e = d;
    if (id == WEBSOCKET_EVENT_DATA)
        ESP_LOGI("WS", "rx: %.*s", e->data_len, (char*)e->data_ptr);
}

void ws_start(void) {
    esp_websocket_client_config_t cfg = { .uri = "ws://192.168.1.20:8000/ws" };
    esp_websocket_client_handle_t ws = esp_websocket_client_init(&cfg);
    esp_websocket_register_events(ws, WEBSOCKET_EVENT_ANY, ws_event, NULL);
    esp_websocket_client_start(ws);
    // esp_websocket_client_send_text(ws, "{\"relay\":\"ON\"}", 14, portMAX_DELAY);
}
```

## Код Arduino (HTTPClient + WebSocketsClient + SSE)

```cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include <WebSocketsClient.h>
#include <ESPAsyncWebServer.h>

AsyncWebServer server(80);
AsyncEventSource events("/events");
WebSocketsClient ws;

void onWs(WStype_t t, uint8_t* p, size_t n) {
  if (t == WStype_TEXT) { // команда з сервера: {"relay":"ON"}
    digitalWrite(27, String((char*)p).indexOf("ON") >= 0);
  }
}

void postSensors(const String& json) {
  HTTPClient http;
  http.begin("http://192.168.1.20:8000/api/v1/sensors");
  http.addHeader("Content-Type", "application/json");
  http.setTimeout(8000);
  int code = http.POST(json);
  Serial.println(code); // 200, -1 = обрив, -11 = таймаут читання
  http.end(); // обов'язково звільнити з'єднання
}

void setup() {
  WiFi.begin("SSID", "PASS");
  while (WiFi.status() != WL_CONNECTED) delay(300);
  // SSE-дашборд:
  server.addHandler(&events);
  server.on("/", HTTP_GET, [](AsyncWebServerRequest* r){
    r->send(200, "text/html", "<meta http-equiv=refresh content=2><h1>ESP32</h1>");
  });
  server.begin();
  // WS-клієнт:
  ws.begin("192.168.1.20", 8000, "/ws");
  ws.onEvent(onWs);
  ws.setReconnectInterval(5000);
}

void loop() {
  ws.loop();
  static uint32_t t = 0;
  if (millis() - t > 5000) { // раз на 5 с
    t = millis();
    events.send("{\"t\":24.5}", "sensors", millis());
    // postSensors(...) — НЕ в кожному циклі: важкий, краще раз на 60 с
  }
}
```

## Код MicroPython (urequests + сервер)

```python
import network, urequests, json, time

sta = network.WLAN(network.STA_IF)
sta.active(True); sta.connect("SSID", "PASS")
while not sta.isconnected(): time.sleep(0.3)

# --- REST POST ---
try:
    r = urequests.post("http://192.168.1.20:8000/api/v1/sensors",
                       data=json.dumps({"id": "esp32-01", "t": 24.5}),
                       headers={"Content-Type": "application/json"})
    print(r.status_code, r.text[:100])
    r.close()  # ОБОВ'ЯЗКОВО, інакше витік сокетів → ENOMEM
except OSError as e:
    print("http fail:", e)

# --- REST GET конфігу ---
try:
    r = urequests.get("http://192.168.1.20:8000/api/v1/config?id=esp32-01")
    cfg = r.json()
    r.close()
    print("period:", cfg.get("period", 60))
except OSError as e:
    print("cfg fail:", e)

# --- Міні-сервер статусу (замість AsyncWebServer; для SSE/WS на MP
# потрібні picoweb або micropython-async — тільки прості сторінки!) ---
import socket
s = socket.socket(); s.bind(("0.0.0.0", 80)); s.listen(1)
s.settimeout(0.5)
while True:
    try:
        cl, _ = s.accept()
        cl.recv(512)
        body = json.dumps({"t": 24.5})
        cl.send("HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n" + body)
        cl.close()
    except OSError:
        pass
```

## Типові помилки

| Симптом | Причина | Рішення |
| --- | --- | --- |
| WDT-ребут під час POST | блокуючий запит у `loop()` без yield | окрема задача FreeRTOS / AsyncWebServer |
| `-1` від HTTPClient | WiFi обрив або DNS не резолвить | перевірити `WL_CONNECTED`, IP замість hostname |
| `-11` читання | сервер висне, таймаут малий | `setTimeout(8000)`, ретраї з backoff |
| `ENOMEM` на MP через годину | `urequests` без `r.close()` | закривати кожну відповідь у `finally` |
| HTTPS `verify failed` | немає NTP (час 1970) або не той CA | спочатку SNTP, див. [03-mDNS-NTP-TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) |
| Обірваний великий body | весь JSON в RAM | chunked-читання порціями / фільтр ArduinoJson |
| SSE не доходять | проксі буферизує потік | `Cache-Control: no-cache`, прямий IP |
| WS рветься за NAT | idle > 60 с | ping/pong кожні 25 с, `setReconnectInterval` |
| 4 WS-клієнти + HTTPS = крах | heap скінчився (~40 КБ/TLS) | ліміт клієнтів, PSRAM, закривати сесії |

## Офіційні джерела

- [ESP HTTP Client - API reference (ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/protocols/esp_http_client.html) - perform, stream, auth, bundle.
- [esp_websocket_client - ESP Component Registry](https://components.espressif.com/components/espressif/esp_websocket_client) - дуплексний WS-клієнт, події.
- [ESPAsyncWebServer - GitHub](https://github.com/me-no-dev/ESPAsyncWebServer) - AsyncWebServer, SSE `AsyncEventSource`.
- [arduinoWebSockets - GitHub](https://github.com/Links2004/arduinoWebSockets) - WebSocketsClient, кадри, реконект.

## Див. також

- [Home](../../../ESP32-Reference/Home.md)
- [WiFi STA/AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md) - транспорт для HTTP/WS
- [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md) - оновлення прошивкою з URL
- [NVS](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md) - URL бекенда і період опитування
- [FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md) - WDT, ENOMEM, heap
- [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) - легка альтернатива для телеметрії
- [mDNS/NTP/TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) - час і сертифікати для HTTPS
- [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) - первинне налаштування
- [Cloud-Pipeline](../../../ESP32-Reference/15-Protokoli/05-Cloud-Pipeline.md) - куди складати дані далі
