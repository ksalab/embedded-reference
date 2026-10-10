---
title: Ready firmwares ESP32 - WLED, Tasmota, Blynk, Homie
description: Своя прошивка (ESP-IDF / Arduino / MicroPython) дає повний контроль, але with'їдає тижні on WiFi-реконект, вебінтерфейс, OTA and дашборди. Ready firmwares закривають 80% типових задач for...
tags: [esp32, wled, tasmota, blynk, homie, mqtt, led, protokoli]
category: Protokoli
date-created: 2026-09-28
date: 2026-09-28
lang: en
original: 15-Protocols/06-Firmwares.md
date: 2026-10-08
---

# Ready firmwares ESP32 - WLED, Tasmota, Blynk, Homie

> [!warning] Готова прошивка ≠ відсутність ризиків: чужий бінарник бачить твій WiFi-пароль and MQTT-логін!
> Прошивай тільки with офіційних релізів (WLED/Tasmota GitHub), одразу міняй дефолтні паролі, закривай відкритий AP. Струм LED-стрічки рахуй ОКРЕМО - прошивка not врятує тонкі дроти!

Огляд мережі: [[05-Radio/01-WiFi-STA-AP]], телеметрія [[15-Protocols/01-MQTT|MQTT]], живлення стрічок [[11-Vivid/09-LED-Strip-Power-SK6812-APA102]], старт [[Home]].

## Призначення

Своя прошивка (ESP-IDF / Arduino / MicroPython) дає повний контроль, але with'їдає тижні on WiFi-реконект, вебінтерфейс, OTA and дашборди. Ready firmwares закривають 80% типових задач for вечір: налив світлодіодну стрічку - WLED, треба клацати реле with MQTT and кнопок - Tasmota, треба мобільний застосунок without бекенда - Blynk, треба самодокументовані MQTT-топіки - Homie-конвенція поверх своєї firmwares.

Коли брати готову прошивку:

- LED-інсталяція, гірлянда, підсвітка: WLED with коробки дає 200+ ефектів, сегменти, пресети, UDP-синхронізацію.
- Розумна розетка / вимикач / датчик with WebUI and MQTT: Tasmota with Template-конфігом without жодного рядка коду.
- Пілотний IoT-продукт with мобільним застосунком: Blynk (Console + Apps + Edgent-provisioning).
- Свій firmware, але стандартні топіки for Home Assistant / openHAB: Homie-конвенція.

Коли not брати:

- батарейний вузол with deep-sleep мікроамперами - Ready firmwares тримають WiFi and їдять десятки мА (див. сон [[07-Timers/03-Sleep-ULP]]);
- сертифікований комерційний виріб with власним брендом застосунку - Blynk Enterprise коштує грошей, WLED/Tasmota тягнуть GPL/EUPL-зобов'язання;
- екзотична периферія without готового драйвера - швидше написати своє, ніж пиляти usermod with нуля.

## Параметри

| Параметр | WLED | Tasmota (tasmota32) | Blynk (Edgent) | Homie (конвенція) |
| --- | --- | --- | --- | --- |
| Призначення | адресні LED: WS2812B, SK6812, APA102 | реле, датчики, димери, мости | хмара + мобільний UI | стандарт MQTT-топіків |
| Бінарник | `WLED_*.bin` / install.wled.me | `tasmota32.bin` (+ варіанти sensors/display) | свій скетч + Blynk-бібліотека | свій code + homie-lib |
| Перший launch | AP `WLED-AP`, портал 4.3.2.1 | AP `tasmota-XXXX`, портал 192.168.4.1 | BlynkEdgent provisioning (AP + claiming) | залежить from firmwares |
| Керування | WebUI, JSON/HTTP API, MQTT | WebUI, MQTT, HTTP `cm?`, Console | Blynk.Console / Apps, віртуальні піни | будь-which Homie-контролер |
| Автовиявлення | mDNS `wled.local`, HA discovery | MQTT discovery for HA | хмарний claiming | `$state` + self-description |
| OTA | HTTP OTA with WebUI | OTA URL (`OtaUrl`, `Upgrade 1`) | Blynk.Air OTA | свій механізм OTA |
| Струм LED | ліміт ABL in UI, але дроти рахуй сам! | PWM/DALI-мости, without ABL | without LED-рушія | without LED-рушія |
| Живлення ESP | 5 in / 500 мА пік WiFi | 5 in / 500 мА пік WiFi | 5 in / 500 мА пік WiFi | залежить from вузла |
| Ліцензія | EUPL-1.2 | GPL-3.0 | комерційна (free-ліміти) | MIT-подібна конвенція |

![[assets/img/firmwares-wled-tasmota-scheme.png|600]]
*Рис. Ready firmwares: WLED крутить стрічку and слухає JSON/MQTT, Tasmota клацає реле for Rules, Blynk возить дані in хмару on V-пінах, Homie описує себе топіками `$state`.*

### ASCII-схема

```text
                    WiFi-роутер 192.168.1.1
                            │
        ┌───────────────────┼────────────────────┐
        │                   │                    │
  WLED-вузол           Tasmota-вузол        Телефон Blynk.App
  192.168.1.50         192.168.1.51         (хмара blynk.cloud)
  GPIO16 → 300×WS2812B  GPIO23 → реле
        │                   │
        │ JSON http://.50   │ cmnd/tasmota_01/POWER
        │ /json/state       │ stat/tasmota_01/RESULT
        │                   │ tele/tasmota_01/SENSOR
        │                   │
        ├─ UDP-sync ────────┤ (WLED→WLED порт 21324)
        │                   │
        └─► MQTT-broker 192.168.1.10 ──► Home Assistant
              │  wled/+/g  (WLED)
              │  homie/5/device123/$state (Homie-вузол)
              └─► Blynk-хмара (TLS, auth-token) ──► дашборд

Перший launch: WLED-AP / tasmota-XXXX / BlynkEdgent-AP → портал → STA
```

### Mermaid

```mermaid
graph LR
    W[WLED<br/>192.168.1.50<br/>GPIO16 strip] -->|JSON/MQTT| B[Mosquitto<br/>broker]
    T[Tasmota32<br/>192.168.1.51<br/>реле Rules] -->|tele/stat/cmnd| B
    H[Homie-вузол<br/>homie/5/..] -->|self-describing| B
    B -->|discovery| HA[Home Assistant]
    BL[ESP32 Blynk.Edgent<br/>V0..Vn] -->|TLS auth-token| BC[Blynk.Cloud]
    BC -->|push| APP[Blynk.App]
    W -.->|UDP sync 21324| W2[WLED-2<br/>дзеркало]
```

## WLED - адресні стрічки without коду

WLED - прошивка-король for WS2812B / WS2811 / SK6812 / APA102 / WS2801. Прошивається готовим бінарником via [веб-інсталер](https://kno.wled.ge/basics/install-binary/) або `esptool.py`, далі все мишкою in WebUI.

Прошивка бінарником:

```bash
# Варіант 1: браузерний інсталер (рекомендовано) — https://install.wled.me/
# Варіант 2: вручну
pip install esptool
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash 0x0 WLED_0.15.0_ESP32.bin
```

Перший launch:

1. ESP піднімає відкритий AP `WLED-AP` (пароль `wled1234` in нових версіях).
2. Підключитись → портал або перейти on `4.3.2.1` → ввести домашній SSID/пароль.
3. Після конекту вузол доступний how `wled.local` (mDNS) + for DHCP-IP; AP лишається how failsafe.
4. `Config → LED Preferences`: тип стрічки (WS281x / SK6812 / APA102), GPIO, кількість LED, порядок кольорів (GRB!), вольтаж.

Сегменти, ефекти, пресети:

- **Сегменти (Segments):** ріжуть одну фізичну стрічку on віртуальні зони (0-99, 100-199…), кожна зі своїм ефектом/кольором/палітрою. До 10 виходів on ESP32 (паралельний I2S + RMT).
- **Ефекти:** 200+ вбудованих (бігучий вогонь, метеори, аудіореактивні with мікрофоном INMP441). Швидкість (Speed) й інтенсивність (Intensity) - окремі слайдери.
- **Пресети:** до 250 слотів - знімок кольори+ефекти+сегменти. Пресет 1 можна призначити on кнопку download. Плейлисти циклять пресети for таймером.
- **Нічник (Nightlight):** плавне згасання for N хвилин. **Ліміт струму ABL (Auto Brightness Limiter):** задаєш мА блока живлення - WLED придушить яскравість, але this not замінює товсті дроти!

Sync UDP між WLED-вузлами:

- `Settings → Sync Interfaces → WLED Broadcast`: усі вузли in одній WiFi-мережі шлють UDP-пакети on порт 21324 (ефект, колір, яскравість).
- Режими: Send + Receive (дзеркало), тільки Send (ведучий), тільки Receive (ведений).
- for сцени/театру - DDP / E1.31 / Art-Net вхід with Jinx/Resolume замість UDP-sync.

Інтеграція Home Assistant:

- Нативна інтеграція `WLED` (Settings → Devices → Add → WLED → IP): кожен сегмент стає окремим `light.*`, плюс сенсори струму/пам'яті/RSSI, селекти пресетів/плейлистів, кнопки рестарту.
- Мінімум WLED 0.14.0. WebSocket дає push-оновлення; кастомні збірки without JSON API not підтримуються.
- Автоматизація YAML - увімкнути пресет «My Preset»:

```yaml
action: light.turn_on
target:
  entity_id: light.wled
data:
  effect: "Fire 2012"
```

```yaml
action: select.select_option
target:
  entity_id: select.wled_preset
data:
  option: "My Preset"
```

Струм стрічок - ОБОВ'ЯЗКОВО прочитати [[11-Vivid/09-LED-Strip-Power-SK6812-APA102]]:

- 300× WS2812B on білому 100% = ~18 but @ 5 in. Один USB-блок on 2 but згорить або просадить напругу - кінець стрічки почервоніє.
- Живити стрічку with ОБОХ кінців (and кожні 2-3 м), спільна земля with ESP, data via резистор 33-100 Ом, конденсатор 1000 мкФ for живленням.
- ABL in WLED - софт-запобіжник, but not заміна міді: став 80% from номіналу блока.

JSON API example (HTTP):

```bash
# Статус
curl http://192.168.1.50/json/state
# Увімкнути червоний + ефект
curl -X POST http://192.168.1.50/json/state \
  -d '{"on":true,"bri":128,"seg":[{"col": [ [255,0,0] ],"fx":5,"sx":200}]}'
# MQTT ті самі поля: топік wled/wled-01/api → той самий JSON
```

## Tasmota - реле, датчики, автоматика without коду

Tasmota (гілка `tasmota32.bin` for ESP32) перетворює голий module on керований WebUI/MQTT/HTTP пристрій: реле, кнопки, DS18B20, BME280, WS2812-стрічки (прості), димери, IR/RF-мости.

Прошивка:

```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
# Взяти tasmota32.bin з https://github.com/arendst/Tasmota/releases
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash 0x0 tasmota32.bin
# Після старту: AP tasmota-XXXX → 192.168.4.1 → домашній WiFi → WebUI
```

Template / GPIO-конфіг (`Configure → Configure Template`):

- Кожен GPIO призначається on роль: `Relay1`, `Button1`, `Led1`, `DS18x20`, `I2C SDA/SCL`, `PWM1`, `WS2812`.
- Ready шаблони for сотень пристроїв - on [templates.blakadder.com](https://tasmota.github.io/docs/Templates/), вставляєш JSON in поле Template and тиснеш Activate.
- example: Sonoff Basic - GPIO12 Relay1, GPIO0 Button1. Своя плата: реле on GPIO23, кнопка on GPIO0 (with підтяжкою).

```text
{"NAME":"MyBoard","GPIO":[0,0,0,0,0,0,0,0,0,2304,0,320,0,0,0,0,0,0,0,0,0,0,224,0,0,0,0,0,0,0,0,0,0,0,0,0],"FLAG":0,"BASE":1}
; 224 = Relay1, 320 = Button1, 2304 = Led1 (індекси компонентів Tasmota)
```

MQTT-топіки `tele / stat / cmnd` (база [[15-Protocols/01-MQTT|MQTT]]):

```text
cmnd/tasmota_01/POWER1 ON        → команда (QoS 1, без retain)
stat/tasmota_01/RESULT {"POWER1":"ON"}   ← відповідь на команду
stat/tasmota_01/POWER1 ON        ← стан реле
tele/tasmota_01/SENSOR {"DS18B20":{"Temperature":23.4}}  ← телеметрія кожні TelePeriod
tele/tasmota_01/LWT Online       ← LWT online/offline
```

Налаштування via Console або Backlog однією пачкою:

```text
Backlog MqttHost 192.168.1.10; MqttUser esp; MqttPassword SECRET;
Topic tasmota_01; TelePeriod 60; PowerRetain on; SetOption53 1
; SetOption53=1 → CBC... (див. довідник SetOption нижче)
```

SetOption - ключові (повний список in `Commands`):

- `SetOption26 1` - форсувати індекси `POWER1` навіть with одним реле.
- `SetOption53 1` - показувати hostname+MAC in MQTT.
- `PowerRetain on` - retain on стан реле (HA бачить стан після рестарту).
- `TelePeriod 60` - період телеметрії, секунд (10-300).
- `BlinkCount / BlinkTime` - миготіння реле for дзвінків/сирен.
- `Emulation 1` - Belkin WeMo for Alexa (див. нотатку 07), `2` - Hue Bridge.

Правила Rules (автоматика without хмари):

```text
Rule1 ON DS18B20#Temperature>28 DO Power1 ON ENDON ON DS18B20#Temperature<25 DO Power1 OFF ENDON
Rule1 1
; Вентилятор за температурою: гістерезис 25/28 °C, всередині пристрою
Rule2 ON Switch1#State=2 DO Backlog Power1 TOGGLE; Publish stat/tasmota_01/EVT {"btn":"double"} ENDON
Rule2 1
```

Timer'и (`Timers` in WebUI) - 16 розкладів сходу/заходу сонця with офсетами, without коду.

## Blynk - хмара and застосунок for вечір

Blynk - платформа: Blynk.Cloud (broker+БД) + Blynk.Console (веб) + Blynk.Apps (iOS/Android) + Blynk Library / Edgent-прошивка. Платиш або терпиш free-ліміти (кількість девайсів/повідомлень), зате мобільний UI збирається drag-and-drop.

Auth-token and віртуальні піни:

- in Console: Template → Datastreams → створити `V0` (температура, double, °C), `V1` (реле, integer 0/1). Кожен пристрій отримує `BLYNK_AUTH_TOKEN`.
- Прошивка not використовує GPIO-номери безпосередньо in хмарі - пишеш in `Blynk.virtualWrite(V0, t)`, читаєш with `BLYNK_WRITE(V1)`.

```cpp
#define BLYNK_TEMPLATE_ID "TMPLxxxx"
#define BLYNK_TEMPLATE_NAME "ESP32 Climate"
#define BLYNK_AUTH_TOKEN "AbCdEfGhIjKlMnOpQrStUvWx"
#include <WiFi.h>
#include <BlynkSimpleEsp32.h>

char ssid[] = "SSID", pass[] = "PASS";

BLYNK_WRITE(V1) {  // віджет кнопки у застосунку
  digitalWrite(27, param.asInt());
}

void setup() {
  pinMode(27, OUTPUT);
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop() {
  Blynk.run();           // тримати зв'язок з хмарою!
  static uint32_t t0 = 0;
  if (millis() - t0 > 5000) {
    t0 = millis();
    Blynk.virtualWrite(V0, 24.5);  // температура → дашборд
  }
}
```

BlynkEdgent provisioning:

- example `Edgent_ESP32` with бібліотеки: перший старт - AP `Blynk Device-XXXX` → портал → домашній WiFi → claiming in твій акаунт (кнопка + LED-індикація статусу).
- OTA with хмари (Blynk.Air): заливаєш новий бінарник in Console → пристрої оновлюються партіями.
- Таймаут реконекту and `Blynk.config()` замість блокуючого `begin()` - якщо хмара недоступна, пристрій має працювати локально!

Тарифи (орієнтир, перевіряти on blynk.io/pricing):

- Free: 2 пристрої, базова історія даних, Blynk branding.
- Plus/Pro: більше пристроїв, white-label застосунок, організації, sub-tenant'и.
- Хобі-датчик погоди - Free вистачає; серія on 500 корпусів - рахуй $/пристрій/рік and читай Terms!

## Homie-конвенція - порядок in MQTT-топіках

Homie - not прошивка, but конвенція іменування MQTT-топіків: пристрій сам описує себе retained-повідомленнями, контролер (openHAB, Home Assistant, Node-RED) підхоплює without ручного мапінгу. Версія актуальна - Homie 5.0 (`homie/5/...`).

Каркас топіків:

```text
homie/5/device123/$state       → ready | sleeping | lost | alert
homie/5/device123/$description → JSON: ім'я, вузли, властивості, одиниці, формат
homie/5/device123/mythermostat/temperature → 22
homie/5/device123/mythermostat/temperature/set → 23  (команда: .../set)
homie/5/device123/$extensions/...  (OTA, статистика, firmware)
```

Мінімальний життєвий цикл `$state`: `init → ready → sleeping → ready → lost` (LWT = `lost`).

example опису (retained):

```json
{
  "id": "device123",
  "homie": "5.0",
  "version": "12",
  "name": "My device",
  "nodes": {
    "mythermostat": {
      "name": "My thermostat",
      "type": "thermostat",
      "properties": {
        "temperature": {
          "name": "Temperature",
          "unit": "°C",
          "datatype": "integer",
          "settable": true
        }
      }
    }
  }
}
```

OTA-розширення: властивість `firmware/checksum` + топік `.../firmware/update/set` with URL бінарника; пристрій качає, перевіряє SHA and перезавантажується.

Свій Homie-вузол on MicroPython (ескіз):

```python
import json
from umqtt.robust import MQTTClient
BASE = b"homie/5/esp32-01"
c = MQTTClient("esp32-01", "192.168.1.10")
c.set_last_will(BASE + b"/$state", b"lost", retain=True)
c.connect()
c.publish(BASE + b"/$state", b"init", retain=True)
desc = {"id": "esp32-01", "homie": "5.0", "version": "1",
        "name": "ESP32 climate",
        "nodes": {"env": {"name": "Env", "type": "sensor",
        "properties": {"t": {"name": "T", "unit": "°C",
        "datatype": "float", "settable": False}}}}}
c.publish(BASE + b"/$description", json.dumps(desc), retain=True)
c.publish(BASE + b"/env/t", b"24.5", retain=True)
c.publish(BASE + b"/$state", b"ready", retain=True)
```

## Коли своя прошивка, but коли готова

| Критерій | Своя прошивка (IDF/Arduino/MP) | WLED | Tasmota | Blynk | Homie поверх своєї |
| --- | --- | --- | --- | --- | --- |
| Час до демо | дні-тижні | 1 вечір | 1 вечір | 1 вечір + UI | дні (але топіки стандартні) |
| LED-стрічка 100+ | писати рушій/RMT самому | бери одразу | тільки прості | ні | пиши сам |
| Реле+кнопки+датчики | GPIO+MQTT вручну | ні | бери одразу | можливо | можливо |
| Мобільний застосунок | свій бекенд/Flutter | застосунок WLED | WebUI, not застосунок | бери одразу | свій |
| Офлайн-робота | повна | повна (LAN) | повна (LAN) | потрібна хмара | повна |
| Deep-sleep мкА | так | ні | ні | ні | так |
| Масштаб 100+ вузлів | свій fleet-менеджмент | MQTT+HA | MQTT+HA | Blynk Orgs/Air | свій + discovery |

Правило: прототип on готовій прошивці → якщо виріб «полетів» and впираєшся in стелю (сон, брендинг, екзотика) - переписуєш on свою, зберігаючи топіки (Homie або `device/<id>/...` with [[15-Protocols/01-MQTT|MQTT]]).

## typical errors

| Симптом | Причина | Рішення |
| --- | --- | --- |
| Кінець LED-стрічки жовтить/червонить | просадка 5 in on тонких/довгих дротах | живлення with обох кінців, провід ≥ 1.5 мм², спільна земля; див. [[11-Vivid/09-LED-Strip-Power-SK6812-APA102]] |
| WLED-AP not зникає після налаштування | failsafe AP лишено увімкненим | `WiFi Setup → Disable AP`, поставити пароль |
| Плутаються кольори R/B | not той порядок каналів | `LED Preferences → Color Order`: GRB for WS2812B, RGB for SK6812 |
| UDP-sync смикається | різні версії WLED / WiFi-лаги | одна версія on всіх, ведучий 1, multicast доступний |
| Tasmota not бачить датчик | not той GPIO/роль in Template | `Configure Template`, звіритись with blakadder-шаблоном плати |
| `cmnd/...` without відповіді | not той `Topic` / `FullTopic` | `Topic tasmota_01`, підписка `stat/#` for діагностики |
| Rules not спрацьовують | правило not ввімкнено | `Rule1 1`, check `Rule1` without параметра показує текст |
| Blynk `Invalid auth token` | токен from іншого Template | скопіювати `BLYNK_AUTH_TOKEN` with Device Info саме цього девайса |
| Blynk-дані not оновлюються | `Blynk.run()` кличеться рідко / `delay()` | without блокуючих `delay`, `run()` щонайменше кожні ~50 мс |
| Homie-контролер not бачить вузол | `$description` without retain | публікувати опис and `$state` with `retain=True` |

## official джерела

- [WLED - документація (kno.wled.ge)](https://kno.wled.ge/basics/install-binary/) - прошивка, сегменти, пресети, UDP-sync, JSON/MQTT API.
- [WLED - GitHub (wled/WLED)](https://github.com/wled/WLED) - релізи бінарників, install.wled.me, usermods.
- [Tasmota - документація](https://tasmota.github.io/docs/) - Template, компоненти, MQTT, Rules, Timers.
- [Tasmota Commands](https://tasmota.github.io/docs/Commands/) - Backlog, Power, SetOption, TelePeriod, Rules-синтаксис.
- [Homie-конвенція - огляд](https://homieiot.github.io/homie-esp8266/) - топіки, `$state`, self-description, розширення OTA.

- WS2801 Datasheet (WorldSemi, пошук PDF): [WS2801 search](https://www.alldatasheet.com/view.jsp?Searchword=WS2801) - LED-драйвер.
- WS2811 Datasheet (WorldSemi, пошук PDF): [WS2811 search](https://www.alldatasheet.com/view.jsp?Searchword=WS2811) - LED-драйвер 12V-стрічок.

## Див. також

- [[Home]]
- [[15-Protocols/01-MQTT|MQTT]] - broker, QoS, LWT for Tasmota/Homie
- [[15-Protocols/07-Notify-Voice|Notify/Voice]] - сповіщення and голосове керування готовими прошивками
- [[05-Radio/01-WiFi-STA-AP|WiFi STA/AP]] - режими радіо, AP-портали першого запуску
- [[11-Vivid/09-LED-Strip-Power-SK6812-APA102|LED Strip Power]] - струм, дроти, ABL for WLED - читати ДО стрічки!
- [[99-Additions/02-Troubleshooting-FAQ|FAQ]] - діагностика обривів and живлення
- [[15-Protocols/04-Provisioning|Provisioning]] - BlynkEdgent vs WiFiManager vs wifi_provisioning


## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| Connection/timeout | Network / broker settings | Verify URL, firewall, credentials |

## Official sources

- [Espressif Protocol Docs](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/index.html)
