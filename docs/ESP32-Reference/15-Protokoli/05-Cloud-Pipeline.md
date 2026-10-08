---
title: Cloud-пайплайн ESP32 - MQTT, Node-RED, InfluxDB, Grafana
description: Наскрізний приклад прикладного IoT: вузол ESP32 з DHT22/BME280 шле телеметрію по MQTT, Mosquitto приймає, Node-RED нормалізує, InfluxDB зберігає часові ряди, Grafana малює дашборд....
tags: [esp32, mqtt, nodered, influxdb, grafana, cloud, iot, protokoli]
category: Protokoli
date-created: 2026-09-28
date: 2026-09-28
---

# Cloud-пайплайн: ESP32 → MQTT → Node-RED → InfluxDB → Grafana

> [!warning] Без NTP-часу на вузлі InfluxDB запише точки з міткою 1970 - графіки «порожні»!
> NTP-синк до першої публікації обов'язковий, див. [03-mDNS-NTP-TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md).

База: MQTT [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md), час [03-mDNS-NTP-TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md), сон [03-Sleep-ULP](../../../ESP32-Reference/07-Timeri-Son/03-Sleep-ULP.md), WiFi [01-WiFi-STA-AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md), старт [Home](../../../ESP32-Reference/Home.md).

## Призначення

Наскрізний приклад прикладного IoT: вузол ESP32 з DHT22/BME280 шле телеметрію по MQTT, Mosquitto приймає, Node-RED нормалізує, InfluxDB зберігає часові ряди, Grafana малює дашборд. Кожну ланку можна замінити, контракт між ними - JSON і MQTT-топіки з розділу [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md).

Коли брати такий стек:

- свій сервер (RPi 4 / VPS), дані нікуди не віддаємо;
- десятки вузлів, потрібні графіки, алерти, історія за рік;
- правила («якщо t > 30 - увімкнути вентилятор») пише нетехнар у Node-RED.

Альтернативи (оглядово, нижче): ThingsBoard замість Node-RED+InfluxDB+Grafana разом; AWS IoT Core замість свого Mosquitto - коли парку тисяч пристроїв замало одного брокера.

## Параметри

| Параметр | Значення | Примітка |
| --- | --- | --- |
| Вузол | ESP32 + DHT22/BME280, період 60 с | deep-sleep між вимірами |
| Транспорт | MQTT QoS 0, топік `device/<id>/sensors` | без retain на потоці! |
| Брокер | Mosquitto 2.x на RPi/VPS | 1883 локально, див. [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Потік | Node-RED: mqtt-in → function → influxdb-out | JSON потоку нижче |
| Сховище | InfluxDB 2.x bucket `iot`, measurement `climate` | retention 365 днів |
| Дашборд | Grafana: Flux/SQL-запит, панель Time series | алерт у Telegram |
| Batch | 1 точка = 1 запис; офлайн-буфер - пачками до 50 | більше - різати |
| Час | NTP на вузлі + серверний timestamp як fallback | без часу - сміття в БД |
| Альтернатива 1 | ThingsBoard (MQTT + свій UI) | швидкий старт, менше гнучкості |
| Альтернатива 2 | AWS IoT Core (MQTT + rules → Timestream) | гроші за повідомлення |

![](../../../ESP32-Reference/assets/img/cloud-pipeline-nodered-scheme.png)
*Рис. Пайплайн: сонний вузол прокидається, шле MQTT, Node-RED пише в InfluxDB, Grafana малює.*

### ASCII-схема

```text
ESP32-вузол (deep-sleep 60с)        Сервер RPi (192.168.1.10)
────────────────────────────        ────────────────────────
 wake → BME280 read → connect WiFi
   │ NTP sync (раз на добу/wake)     Mosquitto :1883
   └─► PUBLISH device/esp32-01/sensors {"t":24.5,"h":55,"vbat":4.0} ──►│
                                                                      ▼
                                                              Node-RED :1880
                                                               mqtt-in (device/#)
                                                                 │
                                                              function: нормалізація
                                                               + timestamp fallback
                                                                 │
                                                              influxdb-out ──► InfluxDB :8086
                                                                                bucket iot
                                                                                  │
                                                                               Grafana :3000
                                                                                 дашборд + алерти
Офлайн: нема WiFi → кільцевий буфер у RTC/NVS (до 50 точок) → злив пачкою.
```

### Mermaid

```mermaid
graph LR
    ESP[ESP32 deep-sleep<br/>BME280] -->|MQTT sensors| MQ[Mosquitto<br/>:1883]
    MQ -->|mqtt-in device/#| NR[Node-RED<br/>function]
    NR -->|line protocol| DB[(InfluxDB<br/>bucket iot)]
    DB -->|Flux| GF[Grafana<br/>дашборд]
    ESP -.->|офлайн-буфер 50| ESP
    GF -.->|алерт t>30| TG[Telegram]
```

## Ланка 1: вузол (коротко, деталі - 01-MQTT)

Вузол робить мінімум: прокинувся → виміряв → підключився → опублікував → заснув. Повний MQTT-код з реконектом - у [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md), тут лише каркас трьох стеків (нижче). Формат корисного навантаження фіксований:

```json
{"id": "esp32-01", "t": 24.5, "h": 55.1, "vbat": 4.02, "rssi": -67}
```

Поле `ts` вузол НЕ ставить (годинник може брехати) - timestamp проставляє Node-RED/InfluxDB при записі, а NTP на вузлі потрібен для TLS і порядку точок.

## Ланка 2: Mosquitto

Брокер з розділу [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md): користувач на вузол, ACL `device/<id>/#`, користувач `nodered` з `device/#` на читання. Жодної логіки в брокері - він тільки шина.

## Ланка 3: Node-RED flow (JSON потоку)

Встановити: `sudo apt install -y nodejs npm`, далі Node-RED офіційним скриптом, палітра `node-red-contrib-influxdb`. Імпортувати потік (Menu → Import):

```json
[
  {
    "id": "mqtt-in-climate",
    "type": "mqtt in",
    "topic": "device/+/sensors",
    "qos": "0",
    "broker": "mosquitto-local",
    "nl": false
  },
  {
    "id": "fn-normalize",
    "type": "function",
    "func": "const m = JSON.parse(msg.payload);\nmsg.measurement = 'climate';\nmsg.payload = [{\n  t: Number(m.t), h: Number(m.h),\n  vbat: Number(m.vbat), rssi: Number(m.rssi)\n}, {id: m.id}];\nreturn msg;"
  },
  {
    "id": "influx-out",
    "type": "influxdb out",
    "influxdb": "influx-local",
    "measurement": "climate",
    "precision": "s"
  },
  {
    "id": "fn-alert",
    "type": "function",
    "func": "const m = JSON.parse(msg.payload);\nif (m.t > 30) { msg.payload = 'ALERT ' + m.id + ' t=' + m.t; return msg; }\nreturn null;"
  }
]
```

Зв'язки: `mqtt-in-climate` → `fn-normalize` → `influx-out`; `mqtt-in-climate` → `fn-alert` → (telegram-sender). Функція нормалізації відкидає сміття (`NaN` від DHT22 - не писати в БД, лічильник бракованих по BME280 - окрема метрика).

## Ланка 4: InfluxDB (bucket, retention, запит)

```bash
influx setup -b iot -o home -u admin -p '***' -r 365d --force
influx bucket list
```

Line protocol, що пише Node-RED:

```text
climate,id=esp32-01 t=24.5,h=55.1,vbat=4.02,rssi=-67 1727486400
```

Перевірка даних (Flux):

```flux
from(bucket: "iot")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "climate" and r.id == "esp32-01")
```

Batch-правило: пачка з офлайн-буфера - до 50 точок за запис; більше ріже пам'ять Node-RED і таймаути InfluxDB.

## Ланка 5: Grafana-дашборд

Джерело: InfluxDB (Flux, URL `http://localhost:8086`, токен з правами read на `iot`). Панелі: Time series `t`/`h` за 24 год, Stat `vbat` (червоний < 3.3 В), Bar gauge `rssi`. Алерт: `t > 30` протягом 5 хв → контакт Telegram. Дашборд експортувати JSON у git - відновлення за хвилину.

## Deep-sleep вузол + буферизація при офлайні

Цикл: `wake → sensors → WiFi → NTP (рідко) → MQTT → sleep(60 с)`. Якщо WiFi/MQTT недоступні - точку складати в кільцевий буфер (RTC-пам'ять до ребуту, NVS - переживе ребут, до 50 записів). При наступному успіху - злити буфер пачкою QoS 1 і почистити. Ніколи не крутити реконект довше 20 с від батареї - краще заснути і спробувати наступного циклу.

## Код вузла: ESP-IDF (каркас, деталі - 01-MQTT)

```c
// wake → read BME280 → publish → sleep. MQTT-клієнт як у 01-MQTT.
void app_main(void) {
    wifi_connect(); sntp_start(); mqtt_start();
    float t, h; bme280_read(&t, &h);
    char j[128];
    snprintf(j, sizeof j, "{\"id\":\"esp32-01\",\"t\":%.1f,\"h\":%.1f}", t, h);
    mqtt_await_connected(5000);
    esp_mqtt_client_publish(s_client, "device/esp32-01/sensors", j, 0, 0, 0);
    vTaskDelay(pdMS_TO_TICKS(500)); // дати TCP стекти
    esp_sleep_enable_timer_wakeup(60 * 1000000ULL);
    esp_deep_sleep_start();
}
```

## Код вузла: Arduino (каркас)

```cpp
#include <WiFi.h>
#include <PubSubClient.h>
WiFiClient net; PubSubClient mqtt(net);
void setup() {
  WiFi.begin("SSID", "PASS");
  for (int i = 0; i < 60 && WiFi.status() != WL_CONNECTED; i++) delay(500);
  mqtt.setServer("192.168.1.10", 1883);
  if (mqtt.connect("esp32-01", "esp32-01", "SECRET")) {
    float t = 24.5, h = 55.0; // dht.readTemperature/Humidity()
    if (!isnan(t)) mqtt.publish("device/esp32-01/sensors",
      ("{\"id\":\"esp32-01\",\"t\":" + String(t) + "}").c_str());
    delay(500);
  }
  esp_sleep_enable_timer_wakeup(60 * 1000000ULL);
  esp_deep_sleep_start(); // реконект — у 01-MQTT, тут сон важливіший
}
void loop() {}
```

## Код вузла: MicroPython (каркас)

```python
import network, time, json, machine
from umqtt.simple import MQTTClient
import dht
from machine import Pin

sta = network.WLAN(network.STA_IF); sta.active(True)
sta.connect("SSID", "PASS")
for _ in range(40):
    if sta.isconnected(): break
    time.sleep(0.5)
if sta.isconnected():
    s = dht.DHT22(Pin(4)); s.measure()
    c = MQTTClient("esp32-01", "192.168.1.10", user="esp32-01", password="SECRET")
    c.connect()
    c.publish(b"device/esp32-01/sensors",
              json.dumps({"id": "esp32-01", "t": s.temperature(), "h": s.humidity()}))
    time.sleep(0.5)
# else: записати точку в буфер (файл) і спати
machine.deepsleep(60_000)
```

## Альтернативи: ThingsBoard, AWS IoT Core (оглядово)

- **ThingsBoard:** вузол шле MQTT на `v1/devices/me/telemetry` з токеном пристрою - і одразу має дашборди, rule engine, алерти без Node-RED/InfluxDB/Grafana. Швидкий старт, ціна - менша гнучкість запитів і прив'язка до однієї платформи.
- **AWS IoT Core:** брокер + rules (SQL) → Timestream/DynamoDB/S3, тінь пристрою (shadow), fleet provisioning для тисяч вузлів. Ціна - гроші за мільйон повідомлень і складніший IAM/TLS з клієнтськими сертифікатами. Виправдано від сотень пристроїв або коли замовник уже в AWS.

## Типові помилки

| Симптом | Причина | Рішення |
| --- | --- | --- |
| Графіки порожні, точки з 1970 | немає NTP на вузлі | SNTP до першої публікації; fallback - серверний timestamp |
| Дублі точок після реконекту | retained `sensors` + перепідписка | retain ТІЛЬКИ state/status, ніколи потік (див. 01-MQTT) |
| `NaN` у БД, ламані графіки | DHT22 не встиг / CRC fail | відкидати `isnan` у Node-RED function |
| Пачка 500 точок вішає запис | batch без ліміту | різати по 50, таймаут InfluxDB-клієнта |
| retain-шторм: 1000 старих точок | вузол щоразу публікує retain | QoS 0 без retain на `sensors` |
| Час стрибає після deep-sleep | RTC-дрейф, NTP раз на добу мало | синк кожного N-го wake або при дрейфі > 2 с |
| Grafana `401` до InfluxDB | протух токен / не той bucket | токен read на `iot`, перевірити Organization |

## Офіційні джерела

- [Node-RED - документація](https://nodered.org/docs/) - потоки, mqtt-in, function-вузли.
- [InfluxDB OSS v2 - документація](https://docs.influxdata.com/influxdb/v2/) - buckets, line protocol, Flux.
- [Grafana - документація](https://grafana.com/docs/grafana/latest/) - джерела, панелі, алерти.
- [ThingsBoard - документація](https://thingsboard.io/docs/) - MQTT telemetry API, rule engine.
- [AWS IoT - What is AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) - Core, rules, протоколи.

## Див. також

- [Home](../../../ESP32-Reference/Home.md)
- [WiFi STA/AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md) - транспорт вузла
- [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md) - оновлення вузлів пайплайна
- [NVS](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md) - офлайн-буфер, ID вузла
- [FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md) - діагностика ланок
- [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) - повний код вузла з реконектом
- [HTTP/WebSocket](../../../ESP32-Reference/15-Protokoli/02-HTTP-WebSocket.md) - REST-альтернатива вузлу
- [mDNS/NTP/TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) - час для InfluxDB
- [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) - введення WiFi на вузлах
