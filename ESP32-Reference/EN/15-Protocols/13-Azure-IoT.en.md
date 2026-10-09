---
title: Azure IoT Hub with ESP32 - SAS-tokens, DPS, Direct Methods, Device Twins
description: Azure IoT Hub - MQTT-broker Microsoft with authorization for SAS-токенами (HMAC from device key, час життя - години!) або X.509. Плюс DPS (автопідключення пристроїв), Device Twins (двійники)...; показує схеми, code and таблиці.
tags: [esp32, azure, iot-hub, dps, sas-token, direct-methods, device-twins, mqtt, tls]
category: Protokoli
date-created: 2026-09-30
date: 2026-09-30
lang: en
original: 15-Protocols/13-Azure-IoT.md
date: 2026-10-08
---

# Azure IoT Hub with ESP32: SAS, DPS, Twins, Direct Methods

## Призначення

Azure IoT Hub - MQTT-broker Microsoft with authorization for SAS-токенами (HMAC from device key, час життя - години!) або X.509. Плюс DPS (автопідключення пристроїв), Device Twins (двійники) and Direct Methods (виклик функцій with хмари). ESP32 - via Azure SDK for Embedded C.

База: старт - [[Home]], MQTT - [[15-Protocols/01-MQTT|MQTT]], TLS - [[15-Protocols/03-mDNS-NTP-TLS]], AWS-близнюк - [[15-Protocols/12-AWS-IoT]], OTA - [[08-Memory/03-OTA|OTA]].

> [!warning] SAS-токен протухає!
> on відміну from AWS-сертифіката (безстроковий), SAS-токен живе години-добу (поле `se=` - expiry epoch). Прошивка МУСИТЬ перегенеровувати токен and перепідключатись ДО expiry, інакше парк мовчки відвалюється опівночі. Час (NTP!) - критичний двічі: for TLS and for `se`.

![[assets/img/cloud-azure-iot-scheme.png|600]]
*Рис. ESP32 with device key → SAS-токен → IoT Hub 8883 → Twins/Direct Methods + DPS for парку.*

## Характеристики підключення

| Параметр | Значення |
| --- | --- |
| Endpoint | `<hub>.azure-devices.net:8883` |
| Авторизація | SAS-токен (`SharedAccessSignature sr=...&sig=...&se=...`) або X.509 |
| Username | `<hub>.azure-devices.net/<device-id>/?api-version=2020-09-30` (так, username - цілий URL!) |
| ClientID | `<device-id>` |
| Протокол | MQTT 3.1.1, keepalive 120-300 с |
| Безкоштовний ліміт | 8000 повідомлень/добу (F1) - вистачає on ~5 вузлів per 1/хв |

## 1. SAS-токен: формула and генерація on ESP32

```text
Токен = "SharedAccessSignature sr={URL-encoded resourceURI}&sig={URL-encoded HMAC-SHA256}&se={expiry}"
  resourceURI = <hub>.azure-devices.net/devices/<device-id> (lowercase!)
  HMAC-SHA256 ключем = base64-декодований device primary key
  se = epoch + 3600 (година життя — мінімум для сну!)
Генерація — на пристрої (mbedTLS HMAC є в IDF) або сервером-посередником.
Пароль MQTT = весь токен цілком (довгий рядок 200+ символів — буфер PubSubClient збільшити!).
```

```c
// ESP-IDF: HMAC-SHA256 з mbedTLS (скорочено, повний код — в Azure SDK samples)
mbedtls_md_hmac(mbedtls_md_info_from_type(MBEDTLS_MD_SHA256),
  key, key_len, (uint8_t*)toSign, toSign_len, hmac);
// далі base64 + URL-encode + збірка токена; se = time(NULL) + 3600.
```

## 2. Топіки Hub (закодовані in MQTT!)

```text
Телеметрія:  devices/<id>/messages/events/              ← PUBLISH сюди
  + властивості: devices/<id>/messages/events/tempAlert=true
C2D (хмара→пристрій): devices/<id>/messages/devicebound/# ← SUB
Direct Method виклик (з хмари): $iothub/methods/POST/reboot/?$rid=1
  ← відповідь пристрою: $iothub/methods/res/200/?$rid=1 {"result":"ok"}
Twin desired: $iothub/twin/PATCH/properties/desired/#   ← SUB (команди!)
Twin reported: $iothub/twin/PATCH/properties/reported/  ← PUBLISH стан
```

## 3. Device Twins vs Direct Methods - коли that

| Механізм | Семантика | example | Обмеження |
| --- | --- | --- | --- |
| Twin desired | Стан, that ЧЕКАЄ (for сплячих!) | `{"period":300}` | Доставка at наступному connect |
| Twin reported | Стан пристрою in хмару | `{"t":23.5,"vbat":3.95}` | Останнє відоме |
| Direct Method | Синхронний виклик, 30 с таймаут | `reboot`, `relayOn` | Пристрій МУСИТЬ бути онлайн! |
| C2D | Повідомлення in чергу (48 год) | Конфіг-файл | Черга, not виклик |

> Сплячий датчик: тільки Twins. Живий актуатор: Direct Methods. Плутанина = «команда reboot not дійшла, because пристрій спав».

## 4. DPS: автопідключення парку

```text
Device Provisioning Service: один глобальний endpoint (global.azure-devices-provisioning.net),
пристрій приїжджає з ID Scope + реєстраційним ID → DPS віддає СВІЙ hub + hostname.
Типи: Symmetric Key (групові/індивідуальні), X.509 (сертифікати), TPM (рідко на ESP32).
Прошивка: DPS-реєстрація ОДИН раз → зберегти assigned hub в NVS → далі безпосередньо в Hub.
```

### Mermaid: життєвий цикл пристрою

```mermaid
flowchart TB
    SNTP[SNTP: час!] --> REG[DPS register: ID Scope + key]
    REG --> HUB[assignedHub в NVS]
    HUB --> SAS[Згенерувати SAS se=now+3600]
    SAS --> CONN[MQTT 8883 CONNECT]
    CONN --> TWIN[Twin reported + desired-SUB]
    TWIN --> WORK[Телеметрія / сон]
    WORK -->|se спливає за 10 хв| SAS
    WORK -->|Direct Method reboot| REBOOT[Виконати + res/200]
```

## typical errors

| # | error | Чому погано | how правильно |
| --- | --- | --- | --- |
| 1 | SAS протух - парк мовчить | `se` in минулому | Регенерація for 10 хв до expiry |
| 2 | Час 1970 | and TLS, and `se` ламаються | SNTP блокуюче до connect |
| 3 | Username короткий | Hub вимагає повний URL | Формат with таблиці вище |
| 4 | PubSubClient дефолтний буфер | Токен 200+ символів not влазить | `setBufferSize(512)` |
| 5 | Direct Method on сплячого | Таймаут 30 с | Сплячим - тільки Twins |
| 6 | Один key on парк | Компрометація = всі | DPS group + окремі derived keys |
| 7 | F1-ліміт перевищено | Hub ріже повідомлення | Рахувати: вузли × частота < 8000/добу |
| 8 | `sr` not lowercase | signature not зійдеться | resourceURI in нижньому регістрі! |
| 9 | Вільний `se=+86400×30` | Місячний токен = дірка | Максимум доба, краще година |
| 10 | DPS кожен раз | Зайві секунди and трафік | assignedHub кешувати in NVS |

## official джерела

- [Azure IoT SDK for Embedded C (GitHub)](https://github.com/Azure/azure-sdk-for-c) - приклади ESP32 (provisioning + telemetry + twin).
- [IoT Hub MQTT protocol](https://learn.microsoft.com/azure/iot-hub/iot-hub-mqtt-support) - топіки, SAS, ліміти.
- [DPS concepts](https://learn.microsoft.com/azure/iot-dps/concepts-service) - enrollment, ID Scope.

### Twin desired-обробник (концепція, ESP-IDF)

```c
// Підписка: $iothub/twin/PATCH/properties/desired/#
// Вхід: {"period":300} → зберегти в NVS → застосувати до таймера deep-sleep.
// Відповідь: PUBLISH reported {"period":300,"status":"applied"}.
// Direct Method reboot: $iothub/methods/POST/reboot → виконати esp_restart()
// ТІЛЬКИ якщо пристрій онлайн (таймаут хмари 30 с!); сплячим — ігнорувати,
// хмара повторить через twin при наступному пробудженні.
```

### Ціни and ліміти: that влізає in free tier

| Параметр | F1 (free) | S1 (платно) |
| --- | --- | --- |
| Повідомлень/добу | 8000 | мільйони |
| Пристроїв | 500 | необмежено |
| C2D + Direct Methods | Так | Так |
| SLA | Немає | 99.9% |

```text
Бюджет повідомлень (приклад): 5 вузлів × 1/хв × 1440 = 7200/добу — влазить у F1!
Правило: телеметрія раз на 1–5 хв + reported twin раз на годину = запас 20%+.
```

## Див. також

- [[Home|Головна]]
- [[15-Protocols/01-MQTT|MQTT]]
- [[15-Protocols/03-mDNS-NTP-TLS|TLS/NTP]]
- [[15-Protocols/12-AWS-IoT]]
- [[15-Protocols/05-Cloud-Pipeline|Cloud-Pipeline]]
- [[08-Memory/03-OTA|OTA]]
- [[08-Memory/01-Partitions-NVS|NVS]]


## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| Connection / auth failure | Credentials / cert / region | Verify keys, cert, region config |

## Official sources

- [AWS IoT Docs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-connect-devices.html)
- [Azure IoT Docs](https://learn.microsoft.com/en-us/azure/iot/develop/reference-iot-device-mqtt/)
