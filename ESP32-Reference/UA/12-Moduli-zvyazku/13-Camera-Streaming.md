---
description: ESP32-S3 з PSRAM + OV2640 - найдешевша WiFi-камера: MJPEG-стрим у браузері,; показує схеми, код і таблиці.
title: Камера OV2640 - MJPEG-стрим, RTSP, QR-AprilTag, Timelapse, Telegram
tags: [esp32, camera, ov2640, mjpeg, rtsp, qr, apriltag, telegram, timelapse, psram]
category: Moduli
date-created: 2026-09-28
---

# Камера OV2640 - MJPEG-стрим, RTSP, QR/AprilTag, Timelapse, Telegram

## Призначення

ESP32-S3 з PSRAM + OV2640 - найдешевша WiFi-камера: MJPEG-стрим у браузері,
одиночні кадри `/capture`, RTSP для відеореєстраторів, розпізнавання QR і AprilTag
прямо на борту, timelapse на SD-карту та відправка фото в Telegram. Нота покриває
налаштування `esp32-camera`, різницю `/capture` vs `/stream`, вимоги до світла
і фокуса та готові коди стримера трьома мовами.

## Характеристики

| Режим | Шлях | Формат | PSRAM | Кадр/с | Застосування |
| --- | --- | --- | --- | --- | --- |
| Фото | `/capture` | JPEG | бажано | за запитом | Telegram, timelapse, детекція |
| Стрим | `/stream` | MJPEG multipart | обов'язково | 5-25 | перегляд у браузері |
| RTSP | `:8554/mjpeg/1` | RTP/JPEG | обов'язково | 5-15 | VLC, реєстратор, Home Assistant |
| QR-скан | кадр у пам'яті | GRAYSCALE | бажано | 2-5 | коди доступу, маркування |
| AprilTag | кадр у пам'яті | GRAYSCALE | бажано | 1-5 | навігація роботів |
| Timelapse | JPEG на SD | JPEG | обов'язково | 1 / N с | будівництво, рослини |

Залізо-мінімум: плата ESP32-S3 з PSRAM (S3R8 і більше), OV2640 (2 Мп, 1600×1200),
живлення 5 В / 1 А (стрим + WiFi їдять 300-500 мА піками), конденсатор 47-100 мкФ
за живленням камери. Без PSRAM - лише QQVGA і ніякого стримінгу, деталі пінів -
див. [[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera]].

> OV2640 має фіксований фокус з заводу: різкість на ~50 см-нескінченність.
> Для QR зблизька об'єктив треба ВИКРУТИТИ (проти годинникової на 1/4-1/2 оберта)
> і зафіксувати краплею лаку. Без цього коди з 10 см не читаються взагалі.
> OV5640 (5 Мп, автофокусні версії) - апгрейд OV2640 на тому самому DVP-сокеті,
> але вимагає більше PSRAM і дає більший кадр (менший FPS на тому самому WiFi).

## MJPEG-стрим з OV2640

Архітектура `esp32-camera` + `esp_httpd`:

- **part-асинхрон:** HTTP-сервер віддає `multipart/x-mixed-replace;boundary=...`,
  кожен part - JPEG-кадр із заголовком `Content-Length`. Браузер малює кадри
  по мірі надходження, окремий потік не потрібен.
- **Буфер PSRAM:** `fb_count = 2` (подвійна буферизація: поки один кадр летить
  у WiFi, сенсор пише наступний). `jpeg_quality = 10-12` (менше число = краща
  якість = більший кадр = менше FPS). Роздільність стріму SVGA (800×600) -
  золота середина між деталізацією і FPS; UXGA душить WiFi.
- **`/capture` vs `/stream`:** `/capture` = один `esp_camera_fb_get()` + відповідь
  `image/jpeg` (для Telegram/timelapse/детекції); `/stream` = нескінченний цикл
  у хендлері (для очей). Не смикати `/capture` під час активного `/stream` на
  одному fb - буде `fb alloc failed`, беріть `fb_count = 2`.
- **PSRAM DMA (S3):** `CONFIG_CAMERA_PSRAM_DMA` - прискорює запис кадрів у PSRAM;
  без нього JPEG SVGA все одно працює, але RGB/GRAYSCALE великих розмірів рветься.

### Легенда пінів камерної плати (ESP32-S3 + OV2640, типово Freenove)

| Пін плати | Призначення | Тип | Куди / примітка |
| --- | --- | --- | --- |
| 5V / 3V3 | Живлення камери | Силове | 5 В від USB/BEC + конденсатор 47-100 мкФ; 3V3-пін плати не тягне стрим |
| GND | Земля | Земля | Коротка земля, спільна з WiFi-антеною (не різати полігон!) |
| GPIO38/39 | SCCB SCL/SDA | I2C конфігурації | Регістри сенсора; швидкість 100 кГц достатньо |
| GPIO40/41/42 | VSYNC/HREF/PCLK | Синхронізація DVP | Короткі доріжки, не вести поруч з антеною |
| GPIO8-GPIO20 | D0-D7 дані DVP | Паралельна шина | Мапа залежить від плати - звіряти з `camera_pins.h`! |
| GPIO45 | XCLK 20 МГц | Мастер-клок | Генерує S3; тремтіння = плаваючі кольори |
| BOOT/USB | Прошивка | USB-Serial | Утримати BOOT при заливці, якщо немає auto-reset |
| SD (SPI/SDIO) | Карта пам'яті | SD 1-біт/4-біт | Timelapse і буфер фото; див. [[08-Pamyat/02-Filesystem | Файлові системи]] |

Пояснення:

- **Конденсатор за живленням:** пік струму сенсора + WiFi TX просаджує шину -
  коричневий `brownout` і ребут саме в момент `/capture`. 100 мкФ біля роз'єму камери.
- **Мапа DVP:** у різних вендорів (Freenove/Waveshare/Espressif) D0-D7 сидять на
  різних GPIO - брати `CAMERA_MODEL_...` з прикладу CameraWebServer під СВОЮ плату.
- **Антенна зона:** не класти камеру/дроти поверх керамічної антени S3 -
  падає RSSI і рветься стрим.

## RTSP оглядово (Micro-RTSP)

MJPEG у браузері - для людей; для машин (VLC, motionEye, реєстратор) - RTSP.
Бібліотека Micro-RTSP (geeksville) - RTSP-сервер для ESP32: слухає TCP 8554,
на `broadcastCurrentFrame()` віддає JPEG-кадр як RTP-пак.wav потік.

- Один клієнт одночасно (обмеження бібліотеки) - для одного реєстратора ок.
- Затримка VLC за замовчуванням ~1 с (буфер `--network-caching`); для «живого»
  зменшити кеш клієнта, а не ганяти FPS.
- RTSP і HTTP-стрим одночасно - тільки з `fb_count = 2` і SVGA або нижче,
  інакше сторожа (`task watchdog`) вбиває цикл.
- URL типово `rtsp://<ip>:8554/mjpeg/1`.

## QR / qrcode + AprilTag - кадри в GRAYSCALE

Детекція працює НЕ з JPEG, а з розпакованим кадром у відтінках сірого:

1. `esp_camera_fb_get()` з `pixel_format = PIXFORMAT_GRAYSCALE`, роздільність
   QVGA (320×240) - швидко і вистачає для кодів до 1-2 м.
2. QR-декодер (quirc-порт / Nayuki-генератор для ПЕЧАТКИ кодів, декодер - quirc)
   їсть буфер безпосередньо; JPEG-кадр спочатку `frame2jpg`→jpg2gray - повільно, уникати.
3. AprilTag (бібліотека AprilTag, сімейство `tag36h11`): точне 3D-положення мітки
   відносно камери - навігація роботів, посадка дрона. Працює на S3 ~1-5 FPS
   у QVGA; більше роздільність = квадратичне зростання часу.
4. Світло: детекторам потрібна рівномірна освітленість без відблисків;
   у темряві вмикати підсвітний LED плати (GPIO, PWM-диммінг) або ІЧ-підсвітку.

> НЕ ганяйте детекцію на кожному кадрі стріму: окремий FreeRTOS-таск з періодом
> 200-500 мс + останній доступний fb (`CAMERA_GRAB_LATEST`). Інакше стрим
> перетвориться на слайд-шоу.

## Timelapse на SD

Цикл: глибокий сон (або `delay`) N секунд → пробудження → `/capture` →
запис `/timelapse/IMG_xxxx.jpg` на SD → назад у сон. Нюанси:

- Імена файлів з інкрементом у NVS/EEPROM, щоб не перезаписувати після ребута.
- SD у режимі 1-біт вистачає (JPEG ~50-150 кБ), живлення карти - стабільні 3.3 В.
- Довгий timelapse (доба+) - живлення від павербанка через 5V-пін, USB-порт
  комп'ютера не потягне піки WiFi (хоча timelapse зазвичай без WiFi).
- Збірка відео: `ffmpeg -framerate 30 -i IMG_%04d.jpg out.mp4` вже на ПК.
- Файлова система і знос карти - див. [[08-Pamyat/02-Filesystem|Файлові системи]].

## Telegram-фото

ESP32 шле фото через Bot API `sendPhoto` (multipart/form-data, ліміт ~10 МБ,
наші JPEG - сотні кБ): тригер (PIR/кнопка/команда `/photo` через `getUpdates`)
→ `/capture` → HTTPS POST на `https://api.telegram.org/bot<token>/sendPhoto`.
Нюанси: потрібен коректний час (NTP, інакше TLS рветься), токен зберігати в NVS,
а не в коді; для відео - `sendVideo` не тягне MJPEG, тільки MP4 (ESP32 не кодує -
не використовувати). Сповіщення/голосові - див. [[15-Protokoli/07-Notify-Voice]].

## Вимоги освітлення і фокуса

- **Світло:** OV2640 без ІЧ-фільтра «бачить» в темряві погано; мінімум для кольору -
  звичайне кімнатне освітлення. На вулиці вночі - ІЧ-прожектор 850 нм + зняти
  ІЧ-фільтр (незворотно!) або чутливіший OV5640.
- **Експозиція:** `sensor->set_exposure_ctrl(1)`, нічний режим `set_night_mode(1)`;
  автоекспозиція «дихає» при timelapse - для рівних кадрів зафіксувати
  `set_aec_value()` після прогріву 2 с.
- **Фокус:** заводський - дальній; QR/макро - викрутити об'єктив і зафіксувати.
  Перевірка: роздрукувати QR 5×5 см, дистанція 20 см, має читатися миттєво.
- **Баланс білого:** авто (+сонячно/хмарно пресети) - для timelapse зафіксувати
  `set_whitebal(1)` + `set_wb_mode()`, інакше кадри «стрибають» за кольором.

## Схема

![[assets/img/camera-streaming-mjpeg-scheme.png|600]]
*Рис. S3-камера: MJPEG-стрим у браузер, RTSP у реєстратор, фото в Telegram і на SD.
Місце під схему - див. [[assets/README]].*

### ASCII-схема

```text
ESP32-S3-CAM (PSRAM!)          Периферія / мережа
─────────────────────          ─────────────────
5V ──────────────────►  живлення (+100мкФ до GND біля камери!)
GND ──────────────────  GND
OV2640 DVP ──► GPIO8-20/38-42/45 (VSYNC/HREF/PCLK/D0-D7/XCLK 20МГц)
SD-карта ──► SPI/SDIO (timelapse IMG_xxxx.jpg, 1-біт вистачає)
PIR/кнопка ──► GPIO (тригер Telegram-фото)
Підсвітний LED ──► GPIO (PWM-диммінг для нічного QR)

WiFi STA ──► /capture (JPEG, один кадр)
         ──► /stream (MJPEG multipart, браузер)
         ──► :8554/mjpeg/1 (RTSP, VLC/реєстратор)
         ──► HTTPS api.telegram.org (sendPhoto, NTP обов'язково!)
```

### Mermaid

```mermaid
graph LR
    OV[OV2640 DVP<br/>XCLK 20МГц] -->|GPIO DVP| S3[ESP32-S3<br/>PSRAM fb×2]
    S3 -->|/stream MJPEG| BR((Браузер))
    S3 -->|RTSP 8554| VLC((VLC/реєстратор))
    S3 -->|sendPhoto HTTPS| TG((Telegram Bot API))
    S3 -->|JPEG| SD[(SD-карта<br/>timelapse)]
    PIR[PIR/кнопка] -->|тригер| S3
    S3 -->|GRAYSCALE QVGA| DET{QR/AprilTag<br/>таск 2-5 Гц}
```

## Код ESP-IDF - MJPEG-стример

```c
#include "esp_camera.h"
#include "esp_http_server.h"

#define PART_BOUNDARY "123456789000000000000987654321"
static const char *_CT = "multipart/x-mixed-replace;boundary=" PART_BOUNDARY;
static const char *_BDR = "\r\n--" PART_BOUNDARY "\r\n";
static const char *_PART = "Content-Type: image/jpeg\r\nContent-Length: %u\r\n\r\n";

// Плата Freenove S3: звірити D0-D7 з camera_pins.h СВОЄЇ плати!
#define CAM_D0 11
#define CAM_D1 9
// ... (повна мапа — див. приклад camera_example esp32-camera)

static camera_config_t cam_cfg = {
    .pin_xclk = 45, .pin_sccb_sda = 39, .pin_sccb_scl = 38,
    .pin_vsync = 40, .pin_href = 41, .pin_pclk = 42,
    .xclk_freq_hz = 20000000,
    .ledc_timer = LEDC_TIMER_0, .ledc_channel = LEDC_CHANNEL_0,
    .pixel_format = PIXFORMAT_JPEG,
    .frame_size = FRAMESIZE_SVGA, // 800x600 — баланс FPS/деталізація
    .jpeg_quality = 11,
    .fb_count = 2,                // подвійна буферизація для стріму
    .grab_mode = CAMERA_GRAB_LATEST,
};

static esp_err_t stream_handler(httpd_req_t *req) {
    httpd_resp_set_type(req, _CT);
    char part[64];
    while (true) {
        camera_fb_t *fb = esp_camera_fb_get();
        if (!fb) break;
        int hlen = snprintf(part, sizeof(part), _PART, fb->len);
        if (httpd_resp_send_chunk(req, _BDR, strlen(_BDR)) != ESP_OK ||
            httpd_resp_send_chunk(req, part, hlen) != ESP_OK ||
            httpd_resp_send_chunk(req, (char*)fb->buf, fb->len) != ESP_OK) {
            esp_camera_fb_return(fb);
            break; // клієнт відключився
        }
        esp_camera_fb_return(fb);
    }
    return ESP_OK;
}

static esp_err_t capture_handler(httpd_req_t *req) {
    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb) { httpd_resp_send_500(req); return ESP_FAIL; }
    httpd_resp_set_type(req, "image/jpeg");
    esp_err_t r = httpd_resp_send(req, (char*)fb->buf, fb->len);
    esp_camera_fb_return(fb);
    return r;
}

void app_main(void) {
    ESP_ERROR_CHECK(esp_camera_init(&cam_cfg));
    httpd_handle_t srv = NULL;
    httpd_config_t hcfg = HTTPD_DEFAULT_CONFIG();
    httpd_start(&srv, &hcfg);
    httpd_uri_t u_cap = {.uri="/capture", .method=HTTP_GET,
                         .handler=capture_handler};
    httpd_uri_t u_stm = {.uri="/stream", .method=HTTP_GET,
                         .handler=stream_handler};
    httpd_register_uri_handler(srv, &u_cap);
    httpd_register_uri_handler(srv, &u_stm);
}
```

## Код Arduino - стример + Telegram-фото

```cpp
#include "esp_camera.h"
#include <WiFi.h>
#include <WiFiClientSecure.h>
// Мапа пінів Freenove S3 — ВЗЯТИ З ПРИКЛАДУ ПІД СВОЮ ПЛАТУ!
#define PWDN -1
#include "camera_pins.h" // CAMERA_MODEL_... з CameraWebServer

void camInit() {
  camera_config_t c;
  c.pin_pwdn = CAM_PIN_PWDN; c.pin_reset = CAM_PIN_RESET;
  c.pin_xclk = CAM_PIN_XCLK; c.pin_sccb_sda = CAM_PIN_SIOD;
  c.pin_sccb_scl = CAM_PIN_SIOC;
  c.pin_d7 = CAM_PIN_D7; c.pin_d6 = CAM_PIN_D6; c.pin_d5 = CAM_PIN_D5;
  c.pin_d4 = CAM_PIN_D4; c.pin_d3 = CAM_PIN_D3; c.pin_d2 = CAM_PIN_D2;
  c.pin_d1 = CAM_PIN_D1; c.pin_d0 = CAM_PIN_D0;
  c.pin_vsync = CAM_PIN_VSYNC; c.pin_href = CAM_PIN_HREF;
  c.pin_pclk = CAM_PIN_PCLK;
  c.xclk_freq_hz = 20000000;
  c.ledc_timer = LEDC_TIMER_0; c.ledc_channel = LEDC_CHANNEL_0;
  c.pixel_format = PIXFORMAT_JPEG;
  c.frame_size = FRAMESIZE_SVGA;
  c.jpeg_quality = 11; c.fb_count = 2;
  c.grab_mode = CAMERA_GRAB_LATEST;
  esp_camera_init(&c);
  sensor_t *s = esp_camera_sensor_get();
  s->set_brightness(s, 0); s->set_saturation(s, 0);
}

// Відправка кадру в Telegram sendPhoto (токен — з NVS, не в код!)
void sendPhoto(const char *token, const char *chatId) {
  camera_fb_t *fb = esp_camera_fb_get();
  if (!fb) return;
  WiFiClientSecure cli; cli.setInsecure(); // для продакшн — setCACert!
  if (!cli.connect("api.telegram.org", 443)) {
    esp_camera_fb_return(fb); return;
  }
  String head = "--p\r\nContent-Disposition: form-data; name=\"chat_id\"\r\n\r\n"
                + String(chatId) + "\r\n--p\r\nContent-Disposition: form-data;"
                + " name=\"photo\"; filename=\"esp.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n";
  String tail = "\r\n--p--\r\n";
  uint32_t len = head.length() + fb->len + tail.length();
  cli.print("POST /bot" + String(token) + "/sendPhoto HTTP/1.1\r\nHost: api.telegram.org\r\n"
            "Content-Type: multipart/form-data; boundary=p\r\nContent-Length: "
            + String(len) + "\r\nConnection: close\r\n\r\n");
  cli.print(head);
  cli.write(fb->buf, fb->len);
  cli.print(tail);
  esp_camera_fb_return(fb);
  while (cli.available()) Serial.write(cli.read());
}
void setup() { Serial.begin(115200); camInit(); /* + WiFi + NTP! */ }
void loop() { /* /capture /stream хендлери як у CameraWebServer */ }
```

## Код MicroPython - capture + timelapse

```python
# MicroPython: драйвер камери обмежений — для стріму краще Arduino/IDF.
# Тут: одиночні кадри + timelapse на SD + тригер Telegram (через urequests).
import camera, machine, time, os, urequests

# Ініціалізація OV2640 (піни — ПІД СВОЮ S3-ПЛАТУ!)
camera.init(0, d0=11, d1=9, d2=8, d3=10, d4=12, d5=18, d6=17, d7=16,
            format=camera.JPEG, framesize=camera.FRAME_SVGA,
            xclk_freq=camera.XCLK_20MHz, href=41, vsync=40,
            reset=-1, pwdn=-1, sioc=38, siod=39, xclk=45, pclk=42)
camera.quality(11)

pir = machine.Pin(13, machine.Pin.IN)

def capture(path):
    buf = camera.capture()  # JPEG-байтстрінг
    with open(path, "wb") as f:
        f.write(buf)
    print("saved", path, len(buf))

# Timelapse: кадр кожні 30 с з інкрементом імені
n = 0
try:
    n = max([int(f[4:8]) for f in os.listdir("/sd/tl")]) + 1
except Exception:
    pass
while True:
    if pir.value():  # рух — позаплановий кадр + Telegram
        capture("/sd/tl/evt_%04d.jpg" % n)
        # urequests.post("https://api.telegram.org/bot<token>/sendPhoto", ...)
    capture("/sd/tl/img_%04d.jpg" % n)
    n += 1
    time.sleep(30)
```

### GC0328 - бюджетна VGA-камера

| Параметр | GC0328 |
| --- | --- |
| Сенсор | GalaxyCore, 640×480 VGA, rolling shutter |
| Інтерфейс | DVP (як OV2640, ті ж піни ESP32-CAM) |
| Живлення | 2.8 В ядро (на платі свій LDO), I/O 1.8/2.8 В |
| Коли брати | Заміна OV2640 там, де ціна важливіша за якість картинки; перед покупкою перевірити підтримку сенсора у поточній версії драйвера esp32-camera |

> GC0328 vs OV2640: дешевша, гірша чутливість у темряві, той же роз'єм - перепайка 1-в-1 на платах ESP32-CAM клонів.

## Типові помилки

1. **`fb alloc failed` / ребут на UXGA** → немає PSRAM або він вимкнений у menuconfig.
   Тільки плата S3R8+, PSRAM 80 МГц + конденсатор живлення.
2. **Коричневий brownout при `/capture`** → пік WiFi+сенсор. Конденсатор 100 мкФ,
   живлення 5 В / 1 А, короткі дроти.
3. **Білий/рожевий кадр, смуги** → неправильна мапа D0-D7 (чужа плата в `CAMERA_MODEL`)
   або довгі «соплі» DVP. Взяти мапу вендора плати.
4. **GC0328 замість OV2640 без зміни драйвера** → чорний кадр. Сенсори не взаємозамінні прошивкою: SCCB-профіль і мапа пінів під конкретний сенсор.
5. **Стрим 1 FPS** → UXGA + quality 5 + один fb. SVGA, quality 10-12, `fb_count = 2`.
6. **`/capture` під час `/stream` вішає** → один fb на двох споживачів. `fb_count = 2`
   - `CAMERA_GRAB_LATEST`.
7. **QR не читається зблизька** → заводський фокус на даль. Викрутити об'єктив,
   зафіксувати лаком; кадри для детекції - GRAYSCALE QVGA, не JPEG!
8. **Telegram: TLS handshake failed** → не виставлений час. Спочатку NTP-синхронізація,
   потім HTTPS.
9. **RTSP затримка секунди** → буфер VLC, не ESP32. Зменшити network-caching клієнта.
10. **Timelapse «стрибає» за кольором** → авто-WB/експозиція. Зафіксувати WB і AEC
   після прогріву.
11. **Сторожевой task watchdog у стрим-циклі** → немає поступок планувальнику при RTSP +
    детекція в одному ядрі. Детекцію - окремим таском з паузою, див. приклад вище.

## Офіційні джерела

- [OV2640 - OmniVision](https://www.ovt.com/sensors/OV2640) - 2 Мп, DVP, формати виводу.
- [OV5640 - OmniVision](https://www.ovt.com/sensors/OV5640) - 5 Мп, автофокус-версії.
- [esp32-camera - драйвер і приклади (Espressif)](https://github.com/espressif/esp32-camera) - init, fb_count, PSRAM DMA, MJPEG-хендлери.
- [Micro-RTSP - RTSP-сервер для ESP32](https://github.com/geeksville/Micro-RTSP) - OV2640Streamer, broadcastCurrentFrame.
- [Telegram Bot API - sendPhoto](https://core.telegram.org/bots/api) - multipart-відправка фото, ліміти.
- [AprilTag - візуальні мітки (UMich)](https://april.eecs.umich.edu/software/apriltag) - сімейства тегів, 3D-поза.
- [QR-Code-generator - генерація QR (Nayuki)](https://github.com/nayuki/QR-Code-generator) - друк власних кодів (C/C++, MIT).

## Див. також

- [[Home]]
- [[12-Moduli-zvyazku/04-RS485-CAN-Ethernet-Kamera]]
- [[08-Pamyat/02-Filesystem|Файлові системи]]
- [[15-Protokoli/07-Notify-Voice]]
- [[12-Moduli-zvyazku/12-RC-Protocols]]
- [[11-Vivid/12-LVGL-SquareLine]]
- [[05-Radio/01-WiFi-STA-AP]]
- [[04-Shini/07-SD-SDIO]]
- [[99-Dodatki/02-Troubleshooting-FAQ]]
