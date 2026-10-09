---
title: LoRaWAN-шлюз на ESP32 - single vs 8-канальний, ChirpStack, TTN, backhaul Cat-1
description: Вузли LoRa говорять - хтось має слухати. Варіанти: одноканальний «шлюз» на ESP32 ($15, але профанація), повноцінний 8-канальний на SX1302 ($80+, справжній), або чужий TTN/ChirpStack....
tags: [esp32, lorawan, gateway, sx1302, chirpstack, ttn, packet-forwarder, backhaul, moduli]
category: Moduli
date-created: 2026-09-30
date: 2026-09-30
---

# LoRaWAN-шлюз: single-channel пастка, SX1302, ChirpStack, TTN

## Призначення

Вузли LoRa говорять - хтось має слухати. Варіанти: одноканальний «шлюз» на ESP32 ($15, але профанація), повноцінний 8-канальний на SX1302 ($80+, справжній), або чужий TTN/ChirpStack. Нота - щоб не купити не те.

База: старт - [[Home]], LoRa-база - [[12-Moduli-zvyazku/02-NRF24-LoRa|LoRa]], Cat-1 - [[12-Moduli-zvyazku/18-Cellular-LoRa-2|Cat-1]] (backhaul!), MQTT-SN - [[15-Protokoli/14-MQTT-SN]].

> [!danger] Single-channel «шлюз» - НЕ шлюз!
> Одноканальний приймач (ESP32+SX1276) чує 1 комбінацію (частота+SF) з ~50 можливих і не шле downlink вчасно. Вузли поруч «працюють», решта - ні, діагностика - пекло. Для 1-2 датчиків поруч - ок; називати це LoRaWAN-мережею - ні.

![[assets/img/lorawan-gateway-sx1302-scheme.png|600]]
*Рис. Вузли → 8-канальний шлюз (SX1302) → backhaul (Ethernet/Cat-1) → ChirpStack/TTN → MQTT.*

## Порівняння шлюзів

| Варіант | Залізо | Канали | Downlink | Ціна | Коли |
| --- | --- | --- | --- | --- | --- |
| Single-channel (ESP32+SX1276) | 1 demodulator | 1 | Кривий | $15 | 1-2 вузли поруч, тести |
| 8-канальний (SX1302+ESP32/RPi) | 8×SF паралельно | 8 | Повноцінний | $80-150 | Справжня мережа |
| Готовий (RAK7268, Milesight) | Все всередині | 8 | + PoE/IP65 | $150-300 | Вулиця без мороки |
| Milesight UG65/UG67 | IP65 готовий, вбудований NS | 8 | Повноцінний | $200-350 | Вуличний стовп: повісив і забув (живлення PoE/сонце) |
| TTN community | Чужий | - | - | $0 | Місто з покриттям (перевірити карту!) |

```text
SX1302-шлюз на ESP32 (схема):
  SX1302-плата (SPI: SCK/MOSI/MISO/CS + RST) ──► ESP32 (хост packet-forwarder!)
  Backhaul: Ethernet (W5500 — стабільно!) або Cat-1 (див. 18-Cellular-LoRa-2).
  Антена 868 МГц скловолокно 3–5 дБм ЯКОМОГА ВИЩЕ (висота = покриття!).
  GPS PPS на шлюзі — для Class-B маяків (без PPS тільки Class-A/C!).
```

### Mermaid: вибір

```mermaid
flowchart TB
    Q[Треба приймати LoRa] --> N{Скільки вузлів?}
    N -->|1–2 поруч| SINGLE[Single-channel тестовий]
    N -->|Парк/вулиця| COV{Є TTN-покриття?}
    COV -->|Так| TTN[Чужий TTN + свої вузли]
    COV -->|Ні| GW8[Свій SX1302 + ChirpStack]
    GW8 --> BH{Backhaul?}
    BH -->|Є Ethernet| W5500[W5500 — найстабільніше]
    BH -->|Тільки поле| CAT1[Cat-1 EC200U/A7670]
```

## 1. ChirpStack vs TTN

| Параметр | ChirpStack (свій) | TTN (спільнотний) |
| --- | --- | --- |
| Де живе | Свій сервер (RPi/VPS) | Хмара TTN |
| Ліміти | Немає | Fair use (30с ефіру/добу/вузол!) |
| Приватність | Дані свої | Дані через чужу хмару |
| MQTT-інтеграція | Вбудована | Вбудована |
| Ціна | Сервер свій | $0 (або TTI Cloud платно) |

## 2. ABP vs OTAA (вузли!)

| Режим | Join | Плюс | Мінус |
| --- | --- | --- | --- |
| OTAA | По ефіру, ключі сесійні | Безпечно, ротація | Треба downlink-вікна (single-channel кульгає!) |
| ABP | Ключі зашиті | Працює навіть з кривим шлюзом | Ключі вічні; frame-counter скидання = відмова! |

## Типові помилки

| # | Помилка | Чому погано | Як правильно |
| --- | --- | --- | --- |
| 1 | Single-channel як «мережа» | Чує 2% ефіру | Чесно називати тестом; мережа - SX1302 |
| 2 | Шлюз у квартирі на столі | Покриття 200 м | Якомога вище + зовнішня антена |
| 3 | ABP з скиданням лічильника | Мережа відкидає кадри | Зберігати frame-counter в NVS! |
| 4 | Backhaul по WiFi без резерву | Падіння = сліпа мережа | Ethernet або Cat-1 |
| 5 | Class-B без GPS PPS | Маяки не працюють | PPS на шлюзі або тільки A/C |
| 6 | TTN fair use перевищено | Бан пристрою | Рахувати ефір: SF12 - рідко! |

## Офіційні джерела

- [SX1302 datasheet (Semtech)](https://www.semtech.com/products/wireless-rf/lora-core/sx1302) - канали, чутливість.
- [ChirpStack docs](https://www.chirpstack.io/docs/) - шлюз-міст, інтеграції.
- [The Things Network docs](https://www.thethingsnetwork.org/docs/) - fair use, OTAA/ABP.

## Packet-forwarder: мінімальний конфіг

```json
{
  "gateway_conf": {"gateway_ID": "AA555A0000000000", "server_address": "chirpstack.local", "serv_port_up": 1700, "serv_port_down": 1700},
  "SX130x_conf": {"lorawan_public": true, "clksrc": 0, "antenna_gain": 3},
  "station_conf": {"log_file": "stderr"}
}
```

## План частот EU868 (що слухати!)

| Канал | Частота | SF | Призначення |
| --- | --- | --- | --- |
| 0-2 | 868.1 / 868.3 / 868.5 МГц | 7-12 | Дефолтні uplink (мусять бути!) |
| 3-7 | 867.1-867.9 | 7-12 | Додаткові (CFList від сервера) |
| RX2 | 869.525 МГц | SF9 | Дефолтний downlink! |
| 868.0 | FSK 50 кбіт | - | Рідко використовується |

### Висота антени = покриття (формула горизонту!)

```text
Радіогоризонт: d ≈ 4.12 × (√h1 + √h2) км, h у метрах.
Шлюз 15 м + вузол 2 м: 4.12 × (3.87 + 1.41) ≈ 21 км (ідеал!).
Шлюз на столі 1.5 м + вузол 1.5 м: ≈ 10 км теорії, 0.2–2 км міста (будинки!).
Кожні +6 м висоти ≈ подвоєння площі покриття. Щогла окупається першою.
```

### ChirpStack за 5 кроків

```text
1. ChirpStack Gateway Bridge на хості шлюзу (MQTT-міст до сервера!).
2. Network Server + Application Server (Docker-compose з офіційного репо!).
3. Додати gateway (EUI з packet-forwarder!), профіль EU868.
4. Створити application + device (OTAA: AppEUI/AppKey згенерувати!).
5. Інтеграція MQTT/HTTP → свої топіки (див. 15-01!) → Node-RED/Grafana.
```

## Діагностика шлюзу: що дивитись

| Симптом | Куди дивитись |
| --- | --- |
| Пакети в ефірі є, на сервері немає | Backhaul (ping!), firewall 1700/UDP |
| RSSI −120, SNR −15 | Межа чутливості: SF вище / антену вище |
| Join-request без accept | Ключі AppKey / CFList / час сервера! |
| Дубльовані аплінки | Два шлюзи чують - норма, дедуплікація на сервері |

## Резервування шлюзів (щоб мережа не лягла!)

```text
Два SX1302 з перекриттям зон: вузли чують обидва → сервер дедуплікує.
Backhaul різний: один Ethernet, другий Cat-1 (різні оператори!).
Живлення: UPS/PoE з батареєю на 4+ год (відключення світла ≠ зупинка мережі).
Моніторинг: heartbeat шлюзу в ChirpStack + алерт «мовчить 10 хв» у Telegram.
```

## Див. також

- [[Home|Головна]]
- [[12-Moduli-zvyazku/02-NRF24-LoRa|NRF24/LoRa]]
- [[12-Moduli-zvyazku/18-Cellular-LoRa-2|Cat-1/LoRa-2]]
- [[12-Moduli-zvyazku/27-LPWAN-Alt|LPWAN-альтернативи]]
- [[15-Protokoli/14-MQTT-SN|MQTT-SN]]
- [[12-Moduli-zvyazku/07-SIM7600-W5500-MCP2515|W5500]]
