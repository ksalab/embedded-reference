---
title: HTTP REST and WebSocket Client on ESP32
description: HTTP - when a classic REST to your backend is needed: GET /api/state, POST /api/sensors with JSON. WebSocket - when duplex in real time is needed: dashboard, relay control without polling; shows schematics, code and tables.
tags: [esp32, http, https, websocket, rest, sse, protocols]
category: Protokoli
lang: en
original: 15-Protocols/02-HTTP-WebSocket.md
date-created: 2026-09-28
date: 2026-10-08
---

# HTTP REST and WebSocket on ESP32

> [!warning] Long HTTPS requests in `loop()` feed the WDT reset, while TLS eats about 40 KB of heap!
> Heavy requests go to a separate FreeRTOS task with stack margin, read responses in chunks.

Network overview: [[05-Radio/01-WiFi-STA-AP.en | WiFi STA and AP]], MQTT alternative [[15-Protocols/01-MQTT.en | MQTT]], time and TLS [[15-Protocols/03-mDNS-NTP-TLS.en | mDNS, NTP and TLS]], start [[Home.en | Home]].

## Purpose

HTTP - when a classic REST to your own backend is needed: `GET /api/state`, `POST /api/sensors` with JSON. WebSocket - when real-time duplex is needed: dashboard, relay control without polling.

When to use HTTP:

- sending telemetry to your own server once a minute;
- OTA firmware from a URL (`update.start(url)`), see [[08-Memory/03-OTA.en | OTA]];
- config from the backend with one GET at start.

When to use WebSocket / SSE:

- live dashboard: AsyncWebServer + SSE pushes data to the browser;
- commands from the browser without page reload;
- full duplex - WebSocket client to its own server.

When NOT to use: dozens of nodes with frequent messages - MQTT is cheaper, see [[15-Protocols/01-MQTT.en|MQTT]].

## Parameters

| Parameter | Value | Note |
| --- | --- | --- |
| IDF client | `esp_http_client` (GET/POST/PUT, keep-alive, chunked) | blocking `perform()` |
| IDF server | `esp_http_server` | for local pages |
| Arduino client | `HTTPClient` (wrapper over WiFiClient) | simple, synchronous |
| Arduino server | ESPAsyncWebServer + SSE | non-blocking, events to the browser |
| MP client | `urequests` (GET/POST JSON) | close the response! |
| MP server | picoweb / micropython-async webserver | simple pages only |
| WebSocket IDF | `esp_websocket_client` | separate registry component |
| WebSocket Arduino | WebSocketsClient (Links2004) | text and binary frames |
| HTTPS | CA bundle or single CA PEM | time via NTP is mandatory |
| RAM for TLS | about 40 KB heap per session | do not hold 2 TLS sessions on C3 |
| WDT | requests over 2-3 s in loop = reboot | separate task or async |

![[assets/img/http-websocket-rest-scheme.png | 600]]
*Fig. REST (request to response) and WebSocket/SSE (persistent channel) between ESP32, backend and browser.*

### ASCII diagram

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
    ESP[ESP32<br/>HTTP client] -->|POST JSON| API[Backend API<br/>:8000]
    API -->|GET config| ESP
    ESP -->|HTTPS CA-bundle| API
    BR[Browser] -->|GET /| WEB[ESP32 AsyncWebServer]
    WEB -->|SSE /events| BR
    WEB <-->|WS /ws| BR
```

## REST GET/POST JSON to your own backend

Application API contract (invent your own, but pin the version):

```text
POST /api/v1/sensors   body: {"id":"esp32-01","t":24.5,"h":55} → 200 {"ok":true}
GET  /api/v1/config?id=esp32-01 → 200 {"period":60,"relay":"auto"}
```

Rules: `Content-Type: application/json`, 5-10 s timeout, 3 tries with backoff, parse the response as a stream (ArduinoJson with a filter), log status codes. Store the send period in NVS, see [[08-Memory/01-Partitions-NVS.en | Partitions and NVS]].

## HTTPS with CA bundle

Server verification options (from secure to test):

1. Mozilla CA bundle in firmware (IDF: `crt_bundle_attach`, Arduino: embedded PEM) - production.
2. One root CA for your own server - your VPS with Let's Encrypt.
3. SHA-1/SHA-256 fingerprint - fragile (breaks on reissue), temporary only.
4. `setInsecure()` - local bench only, never in production.

Without synced time (NTP) the certificate check always FAILs - see [[15-Protocols/03-mDNS-NTP-TLS.en | mDNS, NTP and TLS]].

## WebSocket duplex and AsyncWebServer + SSE

- SSE (`/events`): server pushes telemetry to the browser, auto reconnect. Cheap, enough for a dashboard.
- WebSocket (`/ws`): duplex - a slider or button in the browser drives ESP32 without reload.
- On IDF - `esp_websocket_client` component for the client; server - `esp_http_server` with a WS handler.
- On Arduino - WebSocketsClient for the client, ESPAsyncWebServer for the server with SSE.
- Do not hold a WS server with 4+ clients and an HTTPS client at once on C3 without PSRAM - heap will run out.

## Code ESP-IDF (esp_http_client + WebSocket)

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

## Code Arduino (HTTPClient + WebSocketsClient + SSE)

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

## Code MicroPython (urequests + server)

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

## Common issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| WDT reboot during POST | blocking request in `loop()` without yield | separate FreeRTOS task or AsyncWebServer |
| `-1` from HTTPClient | WiFi drop or DNS not resolving | check `WL_CONNECTED`, IP instead of hostname |
| `-11` on read | server hangs, timeout too small | `setTimeout(8000)`, retries with backoff |
| `ENOMEM` on MP after an hour | `urequests` without `r.close()` | close every response in `finally` |
| HTTPS `verify failed` | no NTP (time 1970) or wrong CA | SNTP first, see [[15-Protocols/03-mDNS-NTP-TLS.en | mDNS, NTP and TLS]] |
| Truncated large body | whole JSON in RAM | chunked reading in parts / ArduinoJson filter |
| SSE never arrive | proxy buffers the stream | `Cache-Control: no-cache`, direct IP |
| WS drops behind NAT | idle over 60 s | ping/pong every 25 s, `setReconnectInterval` |
| 4 WS clients + HTTPS = crash | heap exhausted (about 40 KB per TLS) | limit clients, PSRAM, close sessions |

## Official sources

- [ESP HTTP Client - API reference (ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/protocols/esp_http_client.html) - perform, stream, auth, bundle.
- [esp_websocket_client - ESP Component Registry](https://components.espressif.com/components/espressif/esp_websocket_client) - duplex WS client, events.
- [ESPAsyncWebServer - GitHub](https://github.com/me-no-dev/ESPAsyncWebServer) - AsyncWebServer, SSE `AsyncEventSource`.
- [arduinoWebSockets - GitHub](https://github.com/Links2004/arduinoWebSockets) - WebSocketsClient, frames, reconnect.

## See also

- [[Home.en|Home]]
- [[05-Radio/01-WiFi-STA-AP.en|WiFi STA and AP]] - transport for HTTP and WS
- [[08-Memory/03-OTA.en|OTA]] - firmware update from URL
- [[08-Memory/01-Partitions-NVS.en|NVS]] - backend URL and polling period
- [[EN/99-Additions/02-Troubleshooting-FAQ.en|FAQ]] - WDT, ENOMEM, heap
- [[15-Protocols/01-MQTT.en|MQTT]] - light alternative for telemetry
- [[15-Protocols/03-mDNS-NTP-TLS.en|mDNS, NTP and TLS]] - time and certificates for HTTPS
- [[15-Protocols/04-Provisioning.en|Provisioning]] - initial configuration
- [[15-Protocols/05-Cloud-Pipeline.en|Cloud pipeline]] - where to store data next
