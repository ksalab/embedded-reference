---
title: MQTT-SN - MQTT для сенсорних мереж (UDP, сплячі вузли, шлюз)
description: Класичний MQTT - це TCP + довгі імена топіків: важко для LoRa/Zigbee (маленькі MTU, сплячі вузли, немає TCP). MQTT-SN (Sensor Networks) - той же pub/sub, але поверх UDP, з короткими...
tags: [esp32, mqtt-sn, udp, gateway, sleepy, qos, lora, zigbee, sensor-network]
category: Protokoli
date-created: 2026-09-30
date: 2026-09-30
---

# MQTT-SN: MQTT для сенсорних мереж

## Призначення

Класичний MQTT - це TCP + довгі імена топіків: важко для LoRa/Zigbee (маленькі MTU, сплячі вузли, немає TCP). MQTT-SN (Sensor Networks) - той же pub/sub, але поверх UDP, з короткими topic-id і процедурою сну. ESP32 виступає шлюзом: з одного боку LoRa/Zigbee-вузли, з іншого - звичайний брокер.

База: старт - [[Home]], MQTT - [[15-Protokoli/01-MQTT|MQTT]], LoRa - [[12-Moduli-zvyazku/02-NRF24-LoRa|LoRa]], Zigbee - [[15-Protokoli/09-Matter-Thread-Zigbee]], офлайн-буфер - [[12-Moduli-zvyazku/18-Cellular-LoRa-2|Cat-1]].

> MQTT-SN ≠ MQTT: різні дроти! Безпосередньо до Mosquitto не підключитись - потрібен SN-шлюз (прозорий або агрегуючий). Шлюз - це і є робота ESP32 тут.

![[assets/img/mqtt-sn-gateway-scheme.png|600]]
*Рис. LoRa/Zigbee-вузли говорять MQTT-SN/UDP зі шлюзом ESP32, шлюз - класичним MQTT/TCP з брокером.*

## Характеристики

| Параметр | MQTT-SN | Класичний MQTT |
| --- | --- | --- |
| Транспорт | UDP (TCP - опційно) | TCP |
| Топіки | 2-байтні topic-id / predefined / short-name (2 символи!) | Довгі рядки |
| CONNECT | Короткий, з `.../sleep` процедурою | Довгий + will |
| QoS | −1 (fire-and-forget!), 0, 1, 2 | 0, 1, 2 |
| Сплячі | PINGREQ з `...` + буфер шлюзу | Тільки LWT |
| MTU-дружність | Пакети ~10-30 байт | CONNECT ~100+ байт |
| Шлюз | Обов'язковий (transparent/aggregating) | Не потрібен |

## 1. Топіки: id замість рядків

```text
Реєстрація: PUBLISH з довгим ім'ям → шлюз повертає REGISTER + topic-id (2 байти).
Далі: PUBLISH тільки з topic-id — економія кожного байта ефіру!
Predefined topic-id: зашиті в прошивку обох сторін (0x0001 = temp) — реєстрація не потрібна.
Short topic name: рівно 2 ASCII-символи ("t1") — для найбідніших.
```

## 2. Сплячий вузол: процедура SLEEP

```text
Вузол: CONNECT (clean, duration=600) → REGISTER/SUB → ... → PINGREQ з полем Sleep!
Шлюз: бачить Sleep → БУФЕРИЗУЄ вхідні QoS1/2 для вузла.
Вузол спить (радіо вимкнене!) → прокидається → PINGREQ (будить) → забирає буфер → знову Sleep.
DISCONNECT з duration: «спатиму N с, тримай буфер» — офіційний механізм, не хак!
```

### Mermaid: сон з буфером шлюзу

```mermaid
flowchart TB
    C[CONNECT duration=600] --> REG[REGISTER topic-id]
    REG --> SUB[SUBSCRIBE cmd/#]
    SUB --> SLP[PINGREQ Sleep → радіо OFF]
    SLP -->|Хмара шле команду| GBUF[Шлюз буферизує QoS1]
    SLP -->|Таймер/датчик| WAKE[PINGREQ — прокинувся]
    WAKE --> GET[Забрати буфер + PUBLISH дані]
    GET --> SLP
```

## 3. Шлюз на ESP32: прозорий vs агрегуючий

| Тип | Як працює | Плюс | Мінус |
| --- | --- | --- | --- |
| Transparent | 1 SN-з'єднання = 1 MQTT-з'єднання з брокером | Простота, LWT наскрізний | 100 вузлів = 100 TCP-сесій (RAM!) |
| Aggregating | ОДНЕ MQTT-з'єднання на всіх, префікси топіків | Масштаб: сотні вузлів | Складніший код, LWT емулювати |

```text
Архітектура шлюзу (ESP32-S3 з PSRAM!):
  LoRa (SX1262/SPI) або Zigbee (C6 UART) ──► SN-парсер ──► буфер ──► esp-mqtt ──► брокер
  Мапінг: SN topic-id 0x0001 вузла A → MQTT device/node-A/sensors/temp
  Реалізації: Eclipse Paho MQTT-SN Gateway (Java/C), RSMB (старий, але робочий),
  або свій міні-шлюз під 10–20 вузлів (простіше, ніж здається!).
```

## 4. QoS −1: publish без з'єднання (для маяків!)

```text
QoS −1 = вузол шле PUBLISH з predefined topic-id БЕЗ CONNECT взагалі.
Шлюз налаштований приймати — ідеально для односторонніх датчиків (температура раз на 10 хв).
Ціна: без підтверджень і без шифрування на цьому рівні — для критичного додати лічильник + HMAC у payload!
```

## Типові помилки

| # | Помилка | Чому погано | Як правильно |
| --- | --- | --- | --- |
| 1 | MQTT-SN безпосередньо в Mosquitto | Різні протоколи! | Тільки через SN-шлюз |
| 2 | Довгі топіки в ефірі | Їсть MTU LoRa | topic-id / predefined |
| 3 | TCP замість UDP на LoRa | Handshake не пролізе | UDP за замовчуванням |
| 4 | Без duration у CONNECT | Шлюз викидає буфер | Duration = період сну + запас |
| 5 | 100 TCP-сесій на ESP32 | Немає RAM | Агрегуючий шлюз |
| 6 | QoS −1 для команд | Команди губляться мовчки | −1 тільки для телеметрії |
| 7 | Без лічильника в payload | Replay-атаки | seq + HMAC |
| 8 | Один topic-id на всіх | Колізії | Реєстрація на вузол |

## Офіційні джерела

- [MQTT-SN specification (OASIS)](https://www.oasis-open.org/committees/mqtt-sn/) - пакети, процедури, шлюзи.
- [Eclipse Paho MQTT-SN Gateway](https://github.com/eclipse-paho/paho.mqtt-sn.embedded-c) - embedded-C клієнт + шлюз.
- [RSMB (Really Small Message Broker)](https://github.com/eclipse-mosquitto/mosquitto.rsmb) - брокер з SN-підтримкою.

### Мінімальний SN-клієнт (псевдокод вузла)

```text
LOOP (прокинувся раз на 10 хв):
  CONNECT(clean, duration=700) → чекати CONNACK
  REGISTER "sensors/temp" → запам'ятати topic-id (або predefined 0x0001!)
  PUBLISH topic-id, QoS1, "23.5" → чекати PUBACK (3 ретраї)
  PINGREQ зі Sleep → радіо OFF, спати 600 с
Перший цикл: duration з запасом +20% (дрейф годинника вузла!).
```

### SN + LoRa: розрахунок ефіру

```text
Пакет PUBLISH QoS1: ~15–25 байт (замість 60+ у класичного MQTT!).
SF7/125 кГц: ефір ~50–100 мс → 1% duty-cycle = ~14 пакетів/годину МАКСИМУМ.
Висновок: період 10 хв — комфортно; раз на хвилину — тільки SF7 + короткий payload.
Sleep duration: період + 20% запас (дрейф RC-генератора вузла!).
Шлюз на ESP32-S3: SN-UDP-сокет + esp-mqtt + LittleFS-буфер (див. 18-Cellular-LoRa-2).
```

### RSMB-шлюз на сервері (коли ESP32-шлюз замалий)

```text
Eclipse RSMB (Really Small Message Broker): приймає MQTT-SN/UDP :1883
і класичний MQTT/TCP одночасно — шлюз не потрібен взагалі!
  - Вузли LoRa → свій UDP-міст (LoRa-приймач + forwarder) → RSMB :1883/UDP
  - Дашборди → класичний MQTT :1883/TCP до того самого RSMB
  - Retained/LWT працюють наскрізно (transparent-режим)
Мінус: RSMB застарілий (останні коміти давні) — для продакшену брати
Paho Gateway або ChirpStack + MQTT-інтеграцію.
```

## Див. також

- [[Home|Головна]]
- [[15-Protokoli/01-MQTT|MQTT]]
- [[15-Protokoli/11-Cloud-2|MQTT-клієнт]]
- [[15-Protokoli/09-Matter-Thread-Zigbee|Matter/Thread/Zigbee]]
- [[12-Moduli-zvyazku/02-NRF24-LoRa|LoRa]]
- [[12-Moduli-zvyazku/18-Cellular-LoRa-2|Cat-1 (буфер)]]
- [[10-Sensori/39-Wireless-Sensors|Бездротові сенсори]]

> English twin: [[15-Protokoli/14-MQTT-SN.en.md | EN]]
