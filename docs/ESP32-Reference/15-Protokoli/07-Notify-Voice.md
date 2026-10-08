---
title: Сповіщення і голосове керування ESP32 - Telegram, CallMeBot, Alexa
description: ESP32 вміє не тільки мигати, а й кричати: «протікання!», «двері відчинено!», «полив завершено». Два напрями: сповіщення (пристрій → людина: Telegram / WhatsApp / push) і голос (людина...
tags: [esp32, telegram, callmebot, ifttt, pushover, alexa, fauxmoesp, sinric, protokoli]
category: Protokoli
date-created: 2026-09-28
date: 2026-09-28
---

# Сповіщення і голосове керування ESP32 - Telegram, CallMeBot, Alexa

> [!warning] Токен бота в коді = пароль: хто його прочитав - пише від твого імені!
> Тримай токен у NVS/`secrets.h` (не в git!), увімкни whitelist chat-ID - інакше будь-хто в Telegram клацатиме твоїм реле. Фото з камери не шли у публічні групи!

Огляд мережі: [01-WiFi-STA-AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md), брокер подій [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md), готові прошивки [Прошивки](../../../ESP32-Reference/15-Protokoli/06-Firmwares.md), старт [Home](../../../ESP32-Reference/Home.md).

## Призначення

ESP32 вміє не тільки мигати, а й кричати: «протікання!», «двері відчинено!», «полив завершено». Два напрями: **сповіщення** (пристрій → людина: Telegram / WhatsApp / push) і **голос** (людина → пристрій: «Alexa, turn on…»).

Коли що брати:

- Кнопка / датчик → повідомлення тобі в телефон: **Telegram-бот** (свій, безкоштовно, з фото) або **CallMeBot** (WhatsApp/Telegram без свого бота, 1 GET-запит).
- Критичний аларм з підтвердженням прочитання: **Pushover** (emergency-priority з retry) замість/разом з Telegram.
- Голос у локалці без хмари: **fauxmoESP** («Alexa, turn on…», емуляція ламп).
- Голос + застосунок + віддалено через інтернет: **Sinric Pro** (Alexa / Google Home / SmartThings), у Tasmota - `Emulation`.
- Автоматизації між сервісами («якщо ESP → то Google Sheet»): **IFTTT Webhooks**.

Коли НЕ брати:

- батарейний датчик з deep-sleep - long-poll Telegram тримає WiFi і з'їсть батарею за добу (див. розділ про сон);
- комерційний продукт на чужому безкоштовному шлюзі (CallMeBot/IFTTT free) - ліміти, черги, жодних SLA;
- приватні дані (відео няні, сигналізація) через публічні боти без whitelist - тільки свій сервер/webhook.

## Параметри

| Параметр | Telegram-бот (свій) | CallMeBot | IFTTT Webhooks + Pushover | fauxmoESP (Alexa LAN) | Sinric Pro |
| --- | --- | --- | --- | --- | --- |
| Реєстрація | @BotFather → токен | номер у контактах CallMeBot, apikey | ключ maker.ifttt.com + APP/USER keys | без реєстрації | акаунт + APP_KEY/SECRET |
| Протокол | HTTPS `api.telegram.org` | HTTPS GET 1 запитом | HTTPS POST JSON | UDP discovery + HTTP (LAN) | WebSocket/MQTT TLS до хмари |
| Прийом команд | long-poll `getUpdates` | тільки відправка | через IFTTT-аплети | голос «turn on/off/set %» | голос + застосунок |
| Фото/файли | `sendPhoto` з камери! | текст (медіа - платно) | Pushover attachment 5 МБ | ні | камера (окремі приклади) |
| Вартість | безкоштовно | free personal / TextMeBot платно | IFTTT free-ліміти, Pushover разовий платіж | безкоштовно | 3 девайси free, далі $/рік |
| Затримка | 1-3 с | 5-30 с (черга) | 2-15 с | < 1 с (LAN) | 1-3 с |
| Офлайн-робота | потрібен інтернет | потрібен інтернет | потрібен інтернет | працює без інтернету! | потрібен інтернет |
| Безпека | токен + whitelist chat-ID | apikey у URL (не світити!) | ключі в NVS | тільки LAN, без auth | підписані команди + local control |

![](../../../ESP32-Reference/assets/img/notify-voice-telegram-scheme.png)
*Рис. Подія з ESP32 розходиться трьома шляхами: Telegram-бот (long-poll + фото), CallMeBot/IFTTT/Pushover (HTTPS-хуки), голос назад через Alexa (fauxmoESP локально або Sinric Pro хмарою).*

### ASCII-схема

```text
ESP32 (кнопка GPIO0 / PIR / ESP32-CAM)
   │
   ├─ 1) Telegram-бот (свій, long-poll) ──HTTPS──► api.telegram.org
   │      getUpdates offset=N ──► нові msg ──► whitelist chat-ID?
   │      sendMessage / sendPhoto ──► твій чат (токен BotFather)
   │
   ├─ 2) CallMeBot (без свого бота) ──HTTPS GET──► api.callmebot.com
   │      /whatsapp.php?phone=..&text=..&apikey=..
   │      /telegram.php /telegram/call (дзвінок голосом!)
   │
   ├─ 3) IFTTT Webhooks ──POST──► maker.ifttt.com/trigger/{event}/with/key/KEY
   │      ──► аплет: Pushover / Pushbullet / Google Sheets / Mail
   │      Pushover: api.pushover.net/1/messages.json (priority 2 = будитиме!)
   │
   └─ 4) Голос назад:
        Alexa ──LAN──► fauxmoESP (порт 80, "Alexa, turn on pump")
        Alexa/Google ──хмара──► Sinric Pro ──WebSocket──► ESP32

 Deep-sleep несумісний з long-poll! (див. розділ Сон): будильник → швидкий POST → спати.
```

### Mermaid

```mermaid
graph LR
    E[ESP32<br/>кнопка/PIR/CAM] -->|long-poll getUpdates| TG[Telegram Bot API<br/>BotFather token]
    TG -->|sendMessage/Photo| PHONE[Телефон<br/>whitelist chat-ID]
    E -->|HTTPS GET| CMB[CallMeBot<br/>WhatsApp/Telegram]
    CMB -->|push| PHONE
    E -->|POST trigger| IFTTT[IFTTT Webhooks]
    IFTTT -->|аплет| PO[Pushover/Pushbullet]
    PO -->|priority 2| PHONE
    ALEXA[Alexa<br/>turn on pump] -->|LAN Hue-емуляція| F[fauxmoESP<br/>порт 80]
    F -->|callback| E
    ALEXA2[Alexa/Google<br/>хмара] -->|WebSocket| SIN[Sinric Pro]
    SIN -->|команда| E
```

## Telegram-бот: BotFather, long-poll, фото, whitelist

Свій бот - найгнучкіший шлях: безкоштовно, з двостороннім зв'язком (і команди приймає, і фото з камери шле), працює з бібліотекою UniversalTelegramBot.

Крок 1 - BotFather (у застосунку Telegram):

1. Знайти `@BotFather` → `/newbot` → ім'я (`My ESP32`) + username (`myesp32bot`).
2. Зберегти токен `123456:ABC-DEF...` - це ПАРОЛЬ, у код безпосередньо не комітити!
3. `/setprivacy` → Disable (щоб бот бачив команди в групах), `/setcommands` - список (`led_on`, `status`).
4. Написати боту будь-що з особистого акаунта, дізнатись свій chat-ID: `https://api.telegram.org/bot<TOKEN>/getUpdates` → поле `message.chat.id`.

Крок 2 - long-poll на ESP32 (бібліотека [UniversalTelegramBot](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot)):

```cpp
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

#define BOT_TOKEN "123456:ABC-DEF..."   // ← у secrets.h / NVS, НЕ в git!
#define CHAT_ID "123456789"             // свій ID (whitelist!)
#define ALLOWED_CHAT_ID "123456789"

WiFiClientSecure secured;
UniversalTelegramBot bot(BOT_TOKEN, secured);
uint32_t lastCheck = 0;

void handleMsg(const telegramMessage &m) {
  if (String(m.chat_id) != ALLOWED_CHAT_ID) {
    bot.sendMessage(m.chat_id, "⛔ No access", "");  // чужим — відмова
    return;
  }
  if (m.text == "/led_on")  { digitalWrite(27, HIGH); bot.sendMessage(CHAT_ID, "LED ON", ""); }
  if (m.text == "/led_off") { digitalWrite(27, LOW);  bot.sendMessage(CHAT_ID, "LED OFF", ""); }
  if (m.text == "/status")  { bot.sendMessage(CHAT_ID, "T=24.5 IP=" + WiFi.localIP().toString(), ""); }
}

void setup() {
  Serial.begin(115200);
  pinMode(27, OUTPUT);
  WiFi.begin("SSID", "PASS");
  while (WiFi.status() != WL_CONNECTED) delay(300);
  secured.setCACert(TELEGRAM_CERTIFICATE_ROOT);  // з прикладів бібліотеки!
  bot.longPoll = 10;  // довгі запити — менше трафіку
}

void loop() {
  if (millis() - lastCheck > 2000) {
    lastCheck = millis();
    int n = bot.getUpdates(bot.last_message_received + 1);
    for (int i = 0; i < n; i++) handleMsg(bot.messages[i]);
  }
}
```

sendMessage з фото (ESP32-CAM → Telegram):

```cpp
// Варіант A: фото за URL (камера вже віддає JPEG по HTTP):
bot.sendPhoto(CHAT_ID, "http://192.168.1.60/capture", "Рух біля дверей!");
// Варіант B: прямий POST multipart (див. приклад SendPhoto/PhotoFromSD у бібліотеці):
// bot.sendPhotoByBinary(CHAT_ID, "image/jpeg", size, bufferReader, ...);
// Важливо: бот пише ПЕРШІМ тільки тому, хто вже написав йому (обмеження Bot API)!
```

Чат-ID whitelist - обов'язково:

```cpp
const char* ALLOWED[] = {"123456789", "987654321"};  // сім'я
bool allowed(const String& id) {
  for (auto a : ALLOWED) if (id == a) return true;
  return false;
}
// У handleMsg: if (!allowed(m.chat_id)) return;  // мовчки ігнорувати чужих
```

Ліміти Bot API: ~30 повідомлень/с у чат, 20 МБ на фото через bot API (50 МБ download), текст 4096 символів. Флуд - бан на хвилини.

MicroPython-варіант (без бібліотеки, чистий HTTPS):

```python
import urequests, json
TOKEN = "123456:ABC-DEF..."  # з файлу secrets, не з коду!
CHAT = "123456789"
def tg_send(text):
    url = "https://api.telegram.org/bot%s/sendMessage" % TOKEN
    urequests.post(url, json={"chat_id": CHAT, "text": text}).close()
tg_send("ESP32 прокинувся, T=24.5")
```

## CallMeBot - WhatsApp/Telegram без свого бота

Коли свого бота заводити лінь, а треба «1 GET - і повідомлення в WhatsApp»: [CallMeBot API](https://api.callmebot.com/) - безкоштовний шлюз (personal use). Реєстрація: додати номер CallMeBot у контакти, написати йому «I allow callmebot to send me messages», отримати apikey.

WhatsApp з ESP32 (приклад з [блогу ESP8266/ESP32](https://www.callmebot.com/blog/whatsapp-messages-from-esp8266-esp32/)):

```cpp
#include <WiFi.h>
#include <HTTPClient.h>

String phone = "380501234567";   // БЕЗ + !
String apikey = "123456";        // від CallMeBot
String text = "Door OPEN! T=24.5";

void callmebot_whatsapp(const String& msg) {
  HTTPClient http;
  String url = "https://api.callmebot.com/whatsapp.php?phone=" + phone
             + "&text=" + msg + "&apikey=" + apikey;
  url.replace(" ", "%20");
  http.begin(url);
  int code = http.GET();
  Serial.println(code);  // 200 = прийнято (не = доставлено!)
  http.end();
}
```

Telegram-текст і дзвінок через CallMeBot:

```bash
# Telegram-текст (після активації за інструкцією callmebot-бота):
curl "https://api.callmebot.com/text.php?user=@myuser&text=Alarm!&apikey=KEY"
# Голосовий дзвінок у Telegram (читає текст уголос!):
curl "https://api.callmebot.com/telegram/call.php?user=@myuser&text=Water+leak!&lang=en-US-Standard-A&apikey=KEY"
```

Обмеження: черги 5-30 с, ліміт повідомлень/добу, текст латиницею надійніший за кирилицю (URL-encode!), жодних фото/файлів на free. Для бізнесу - платний TextMeBot. Apikey у URL світиться в логах проксі - окремий акаунт, не основний!

## IFTTT Webhooks + Pushover / Pushbullet

IFTTT - клей між ESP32 і сотнями сервісів: один POST з плати → аплет розсилає куди завгодно.

Webhook-тригер:

```cpp
#include <HTTPClient.h>
void ifttt(const char* event, const char* v1) {
  HTTPClient http;
  String url = String("https://maker.ifttt.com/trigger/") + event
             + "/with/key/cdxxxxxxxxxxxxxxxxxxxxxxxxxx";
  http.begin(url);
  http.addHeader("Content-Type", "application/json");
  http.POST(String("{\"value1\":\"") + v1 + "\"}");
  http.end();
}
// Виклик: ifttt("door_open", "kitchen 21:30");
```

Аплет у ifttt.com: `If Webhooks (door_open) → Then Pushover / Gmail / Sheets / Philips Hue`. Ім'я події - латиницею, без пробілів.

Pushover ([API](https://pushover.net/api)) - push з пріоритетами, працює з ESP32 безпосередньо без IFTTT:

```cpp
// POST https://api.pushover.net/1/messages.json
// token=APP_TOKEN&user=USER_KEY&message=Leak!&priority=2&retry=60&expire=1800
// priority: -2 silent, 0 normal, 1 bypass quiet, 2 EMERGENCY (будить поки не підтвердиш!)
```

```bash
curl -s -F "token=APP_TOKEN" -F "user=USER_KEY" \
  -F "priority=2" -F "retry=60" -F "expire=1800" \
  -F "message=Water leak, kitchen!" https://api.pushover.net/1/messages.json
# Вкладення: -F "attachment=@/capture.jpg" (до 5 МБ!)
```

Pushbullet - простіше (1 токен, канали), але без emergency-повторів. Для «пожежа/потоп» - Pushover priority 2, для «полив завершено» - Telegram/IFTTT.

## Alexa через fauxmoESP + Sinric Pro, Google Home

fauxmoESP - локальна емуляція ламп для Alexa, інтернет НЕ потрібен. Працює так: ESP32 прикидається Philips Hue (v3+, раніше - Belkin WeMo), колонка Echo знаходить її в LAN і шле `turn on/off/set %`.

> [!note] Історична деталь: до v3.0 fauxmoESP емулював Belkin WeMo, з v3.0 - Philips Hue (дає димування «set to 50%»). У старих гайдах ще пишуть «WeMo» - суть та сама: локальний discovery без хмари.

```cpp
#include <WiFi.h>
#include <fauxmoESP.h>  // https://github.com/vintlabs/fauxmoESP

fauxmoESP fauxmo;

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "PASS");
  while (WiFi.status() != WL_CONNECTED) delay(300);
  fauxmo.createServer(true);
  fauxmo.setPort(80);  // gen3-колонки вимагають порт 80!
  fauxmo.enable(true);
  fauxmo.addDevice("pump");    // "Alexa, turn on pump"
  fauxmo.addDevice("kitchen light");
  fauxmo.onSetState([](unsigned char id, const char* name, bool state, unsigned char value) {
    Serial.printf("%s → %s (%d)\n", name, state ? "ON" : "OFF", value);
    digitalWrite(27, state ? HIGH : LOW);  // value 0..255 = яскравість!
  });
}

void loop() {
  fauxmo.handle();  // викликати ЧАСТО, без delay()!
}
```

Умови: Echo і ESP32 в ОДНІЙ підмережі (без guest-ізоляції!), порт 80 вільний, LwIP «Higher Bandwidth» на ESP8266-ядрі. «Alexa, discover devices» → «turn on pump» / «set kitchen light to fifty percent». З 2.4/5 ГГц-розносом на роутері discovery часто ламається - саджати обох на 2.4 ГГц.

Sinric Pro ([SinricPro ESP SDK](https://github.com/sinricpro/esp8266-esp32-sdk)) - хмарний міст до Alexa/Google/SmartThings/Homebridge, коли треба керування ЧЕРЕЗ ІНТЕРНЕТ + застосунок + OTA:

1. Реєстрація → Add Device (Switch/Dimmer/Thermostat) → APP_KEY + APP_SECRET + DEVICE_ID.
2. Прошивка з SDK (`SinricPro` lib): WebSocket TLS до хмари, колбеки `onPowerState`.
3. Free: 3 пристрої; далі ~$3/пристрій/рік. Працює і local control (підписані LAN-команди, коли інтернет ліг).
4. У Tasmota є вбудоване: `Emulation 1` (WeMo) / `2` (Hue) - Alexa знаходить розетку без коду взагалі.

Google Home безпосередньо (без посередників) ESP32 не вміє - тільки через хмару: Sinric Pro (Google Action), Home Assistant (emulated_hue / Google Assistant integration) або Tasmota Hue-емуляція + HA-міст. Окремої «бібліотеки Google Home для ESP32» не існує - всі гайди ведуть через один із цих мостів.

## Приклад «кнопка → сповіщення + фото з камери»

Сценарій: кнопка дверей (GPIO0) → ESP32-CAM робить знімок → Telegram-бот шле фото + текст → паралельно Pushover priority 1.

```cpp
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include "esp_camera.h"  // ESP32-CAM конфіг опущено

#define BOT_TOKEN "123456:ABC-DEF..."
#define CHAT_ID "123456789"
#define BTN 0

WiFiClientSecure secured;
UniversalTelegramBot bot(BOT_TOKEN, secured);
volatile bool pressed = false;

void IRAM_ATTR onBtn() { pressed = true; }  // тільки прапорець!

void sendAlert() {
  camera_fb_t* fb = esp_camera_fb_get();
  if (!fb) { bot.sendMessage(CHAT_ID, "🚪 Двері! (камера недоступна)", ""); return; }
  // Шлях 1: фото через Telegram (див. SendPhoto-приклади бібліотеки)
  // bot.sendPhotoByBinary(CHAT_ID, "image/jpeg", fb->len, ...);
  esp_camera_fb_return(fb);
  bot.sendMessage(CHAT_ID, "🚪 Двері відчинено 21:30", "");
  // Шлях 2: паралельно Pushover (HTTPClient POST) — якщо Telegram ліг
}

void setup() {
  WiFi.begin("SSID", "PASS");
  while (WiFi.status() != WL_CONNECTED) delay(300);
  secured.setCACert(TELEGRAM_CERTIFICATE_ROOT);
  pinMode(BTN, INPUT_PULLUP);
  attachInterrupt(BTN, onBtn, FALLING);
}

void loop() {
  bot.getUpdates(bot.last_message_received + 1);  // + обробка команд /led_on...
  if (pressed) {
    pressed = false;
    delay(50);  // антибрязкіт
    if (digitalRead(BTN) == LOW) sendAlert();
  }
}
```

Живлення камери: спалах підсвітки + WiFi-TX = пік 600+ мА, окремий стабілізатор 5 В/2 А, інакше brownout у момент фото.

## Сон: long-poll + deep-sleep несумісні

Проблема: `getUpdates` вимагає ПОСТІЙНОГО WiFi (десятки мА), а deep-sleep вимикає радіо повністю (10 мкА). Разом не живуть: або спиш, або слухаєш команди.

Рішення 1 - polling будильником (датчик спить, прокидається, ШЛЕ, знову спить):

```cpp
// Прокинувся за таймером / EXT0 (PIR) → WiFi → tg_send("T=...") → спати
esp_sleep_enable_timer_wakeup(10 * 60 * 1000000ULL);  // кожні 10 хв
// ... WiFi + sendMessage ...
esp_deep_sleep_start();  // команд НЕ чекаємо — тільки відправка!
```

Рішення 2 - webhook-сервер замість long-poll (для завжди-ввімкнених вузлів):

- Свій сервер (VPS/RPi) тримає `setWebhook https://...`, приймає команди Telegram і кладе їх у чергу/MQTT (`device/esp32-01/cmd`).
- ESP32 прокидається, забирає чергу по MQTT (QoS 1, retained команда), виконує, звітує, спить.
- Бонус: сервер ховає токен бота - на пристрої тільки MQTT-логін.

Правило: батарейка → тільки ВІДПРАВКА по пробудженню (Telegram/CallMeBot/Pushover POST); прийом команд у сні - через retained-MQTT чергу, не long-poll.

## Типові помилки

| Симптом | Причина | Рішення |
| --- | --- | --- |
| `410 Gone` / бот мовчить | токен відкликано через BotFather | згенерувати новий `/token`, оновити NVS, не комітити в git |
| Бот не відповідає в групі | privacy mode ріже чужі повідомлення | @BotFather `/setprivacy` → Disable, додати бота адміном |
| Команди виконує будь-хто | немає whitelist chat-ID | порівнювати `m.chat_id` з ALLOWED, чужим - ігнор/відмова |
| `sendPhoto` падає на ESP32-CAM | мало heap під JPEG + TLS (~40 КБ) | QVGA замість UXGA, PSRAM увімкнено, фото окремо від long-poll |
| CallMeBot відповідає 200, але нічого немає | не завершена активація / ліміт | повторно «I allow…», пауза 24 год, латиниця в тексті |
| Кирилиця в CallMeBot - «???» | не закодовано URL | `url.encode()` / `%20` для пробілів, краще латиниця |
| IFTTT спрацьовує через хвилини | free-черга IFTTT | критичне - безпосередньо Pushover/Telegram, не через аплет |
| «Alexa, turn on…» - «device not found» | різні підмережі / порт не 80 | одна LAN 2.4 ГГц, `fauxmo.setPort(80)`, rediscover |
| fauxmoESP не компілюється з WebServer | конфлікт порту 80 | приклад `fauxmoESP_External_Server` або інший порт + gen1-колонка |
| Long-poll їсть батарею за добу | WiFi+TLS постійно в ефірі | deep-sleep + відправка по будильнику, див. розділ Сон |
| Pushover emergency не замовкає | немає `retry/expire`, юзер не підтвердив | `retry≥30, expire≤10800`, підтвердження в застосунку |

## Офіційні джерела

- [Telegram Bot API](https://core.telegram.org/bots/api) - `getUpdates`, `sendMessage`, `sendPhoto`, ліміти.
- [UniversalTelegramBot - GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot) - long-poll, клавіатури, приклади ESP32/CAM.
- [CallMeBot API](https://api.callmebot.com/) - WhatsApp/Telegram/Signal API, активація, apikey.
- [Pushover API](https://pushover.net/api) - пріоритети, retry/expire, вкладення 5 МБ.
- [fauxmoESP - GitHub](https://github.com/vintlabs/fauxmoESP) - Hue-емуляція, порт 80, `onSetState`.

## Див. також

- [Home](../../../ESP32-Reference/Home.md)
- [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) - черга команд для сплячих вузлів, LWT
- [Прошивки](../../../ESP32-Reference/15-Protokoli/06-Firmwares.md) - Tasmota Emulation, Blynk-сповіщення з коробки
- [WiFi STA/AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md) - STA-конект перед будь-яким HTTPS
- [LED Strip Power](../../../ESP32-Reference/11-Vivid/09-LED-Strip-Power-SK6812-APA102.md) - живлення ESP32-CAM у момент фото
- [FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md) - TLS handshake, NTP-час для HTTPS, brownout
