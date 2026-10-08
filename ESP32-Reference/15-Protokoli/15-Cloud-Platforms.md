---
title: Хмарні платформи з ESP32 - Firebase, Shelly, Frigate, Supabase, Domoticz, Prometheus
description: Свій Mosquitto - не завжди відповідь: інколи треба готові дашборди (Domoticz), мобільні пуші з коробки (Firebase), міст до готових реле (Shelly), відеоаналітику (Frigate), SQL-сховище...
tags: [esp32, cloud, firebase, shelly, frigate, supabase, domoticz, prometheus, mqtt, rest, protokoli]
category: Protokoli
date-created: 2026-09-30
date: 2026-09-30
---

# Хмарні платформи з ESP32: Firebase, Shelly, Frigate, Supabase, Domoticz, Prometheus

## Призначення

Свій Mosquitto - не завжди відповідь: інколи треба готові дашборди (Domoticz), мобільні пуші з коробки (Firebase), міст до готових реле (Shelly), відеоаналітику (Frigate), SQL-сховище (Supabase) або збір метрик (Prometheus). Нота - карта «що вміє кожен + як підключити ESP32 + ціна питання».

База: старт - [[Home]], MQTT - [[15-Protokoli/01-MQTT|MQTT]], пайплайн - [[15-Protokoli/05-Cloud-Pipeline]], AWS - [[15-Protokoli/12-AWS-IoT]], Azure - [[15-Protokoli/13-Azure-IoT]], TLS - [[15-Protokoli/03-mDNS-NTP-TLS]].

![[assets/img/cloud-platforms-firebase-shelly-scheme.png|600]]
*Рис. ESP32 в центрі: стрілки до Firebase/Supabase (HTTPS), Shelly (RPC/MQTT), Frigate (MQTT-кадр), Domoticz (MQTT), Prometheus (scrape /metrics).*

## Порівняльна таблиця

| Платформа | Протокол з ESP32 | Auth | Безкоштовно | Коли брати |
| --- | --- | --- | --- | --- |
| Firebase RTDB + FCM | HTTPS REST / SSE | OAuth2 / database secret | Spark-план (ліміти!) | Мобільний застосунок + пуші |
| Shelly (пристрої) | HTTP-RPC / MQTT | Digest / MQTT-логін | Купуєш реле | Готові актуатори без паяння |
| Frigate (NVR) | MQTT-кадр подій | Без / MQTT-логін | Open-source | Камера + «хтось у дворі» |
| Supabase | HTTPS REST (PostgREST) | anon/service key (JWT) | 500 МБ БД | Треба SQL, а не топіки |
| Domoticz | MQTT `domoticz/in` | Без / пароль | Open-source | Дашборд за 15 хв |
| Prometheus | HTTP GET `/metrics` (scrape!) | Без / bearer | Open-source | Моніторинг парку, алерти |

### Mermaid: вибір платформи

```mermaid
flowchart TB
    Q[Куди слати дані?] --> APP{Треба мобільний застосунок?}
    APP -->|Так| FB[Firebase: RTDB + FCM-пуші]
    APP -->|Ні| DASH{Треба дашборд?}
    DASH -->|Швидко| DOM[Domoticz: MQTT domoticz/in]
    DASH -->|SQL-запити| SUP[Supabase: REST-таблиця]
    DASH -->|Моніторинг парку| PROM[Prometheus: /metrics + Grafana]
    Q --> ACT{Готові реле?}
    ACT -->|Так| SH[Shelly: HTTP-RPC або MQTT-режим]
    Q --> CAM{Камера + детекція?}
    CAM -->|Так| FR[Frigate: події по MQTT]
```

## 1. Firebase: RTDB + FCM-пуші

```text
RTDB REST: PUT https://<proj>.firebaseio.com/device/<id>/sensors.json?auth=<DB_SECRET>
  тіло {"t":23.5} → відповідь 200. ПРАВИЛА RTDB: за замовчуванням ЗАКРИТО —
  відкрити читання/запис для шляху пристрою (не root!).
FCM-пуш з ESP32 безпосередньо НЕ шлють (потрібен server key!) — схема:
  ESP32 → RTDB → Cloud Function → FCM на телефон.
ESP32-сторона: HTTPS POST (див. 15-02), CA-сертифікат + NTP-час обов'язково!
```

## 2. Shelly: HTTP-RPC і MQTT-режим

```text
HTTP-RPC (без хмари взагалі!): GET http://shelly-84/status → JSON;
  GET http://shelly-84/rpc/Switch.Set?id=0&on=true → клац!
MQTT-режим: shelly вмикається в Settings → MQTT prefix shelly-kitchen-1 →
  топіки shellies/.../relay/0/command (accept) і .../announce.
ESP32 керує Shelly реле безпосередньо по LAN: затримка мс, інтернет не потрібен.
```

## 3. Frigate: події з камери по MQTT

```text
Frigate (на сервері/міні-ПК) дивиться RTSP з камери → детекція (person/car/dog) →
  MQTT: frigate/events → {"before":{...},"after":{"label":"person","camera":"yard"}}.
ESP32 підписаний на frigate/events → сирена/світло/LINE-сповіщення.
Зворотний бік: ESP32-CAM як джерело для Frigate — RTSP-прошивка камери + стабільний WiFi!
```

## 4. Supabase: SQL замість топіків

```cpp
// Arduino: POST рядка в таблицю telemetry через PostgREST
// POST https://<proj>.supabase.co/rest/v1/telemetry
// Headers: apikey: <ANON_KEY>, Authorization: Bearer <ANON_KEY>, Content-Type: application/json
// Body: {"device_id":"esp32-01","t":23.5}
// Відповідь 201. RLS-політики: дозволити INSERT тільки в свою таблицю!
```

## 5. Domoticz: MQTT-вхід за 15 хв

```text
Domoticz → Налаштування → MQTT (mosquitto той самий!) → топік domoticz/in.
ESP32 шле: {"idx":12,"nvalue":0,"svalue":"23.5"} → пристрій-сенсор з'являється сам!
idx дізнатись: вкладка Пристрої (невикористані) → додати.
```

## 6. Prometheus: scrape `/metrics` з ESP32

```text
ESP32 віддає текст на :80/metrics:
  # HELP esp32_temp_c Температура
  # TYPE esp32_temp_c gauge
  esp32_temp_c{device="esp32-01"} 23.5
  esp32_heap_free 180000
Prometheus scrape_interval 60s → Grafana → алерти (t>30 5 хв).
Плюс: нуль коду на пристрої крім формату; мінус: pull-модель (пристрій має бути доступний!).
```

## Код (ESP-IDF/Arduino - універсальні фрагменти)

```cpp
// Arduino: Domoticz-публікація через PubSubClient (розділ 5)
mqtt.publish("domoticz/in", "{\"idx\":12,\"nvalue\":0,\"svalue\":\"23.5\"}");
// Arduino: Prometheus-метрики через WebServer (розділ 6)
server.on("/metrics", []() {
  char b[160];
  snprintf(b, sizeof(b),
    "# TYPE esp32_temp_c gauge\nesp32_temp_c{device=\"esp32-01\"} %.1f\n", readTemp());
  server.send(200, "text/plain", b);
});
```

## Типові помилки

| # | Помилка | Чому погано | Як правильно |
| --- | --- | --- | --- |
| 1 | RTDB rules відкриті на root | Читає/пише хто завгодно | Правила на шлях пристрою |
| 2 | FCM з ESP32 безпосередньо | Потрібен server key (секрет на пристрої!) | Через Cloud Function |
| 3 | Shelly в хмарі, а треба LAN | Затримки + залежність від інтернету | HTTP-RPC по локалці |
| 4 | Supabase без RLS | Будь-хто пише в таблицю | RLS: INSERT тільки своє |
| 5 | Prometheus scrape 5s | DDoS власного вузла | 30-60s достатньо |
| 6 | Domoticz без idx | Повідомлення в нікуди | idx з вкладки Пристрої |
| 7 | HTTPS без NTP | TLS падає | SNTP до запитів (див. 15-03) |
| 8 | Один ключ на парк | Компрометація = всі | Ключ/токен на пристрій |

## Офіційні джерела

- [Firebase RTDB REST](https://firebase.google.com/docs/database/rest/start) - auth, правила.
- [Shelly API Docs](https://shelly-api-docs.shelly.cloud/gen2/) - RPC, MQTT.
- [Frigate MQTT](https://docs.frigate.video/integrations/mqtt) - топіки подій.
- [Supabase PostgREST](https://supabase.com/docs/guides/api) - таблиці, RLS.
- [Prometheus exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/) - формат метрик.

## Див. також

- [[Home|Головна]]
- [[15-Protokoli/01-MQTT|MQTT]]
- [[15-Protokoli/02-HTTP-WebSocket|HTTP/WebSocket]]
- [[15-Protokoli/03-mDNS-NTP-TLS|TLS/NTP]]
- [[15-Protokoli/05-Cloud-Pipeline|Cloud-Pipeline]]
- [[15-Protokoli/12-AWS-IoT]]
- [[15-Protokoli/13-Azure-IoT]]
- [[12-Moduli-zvyazku/13-Camera-Streaming|Камера-стримінг]]
