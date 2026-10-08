---
title: Matter, Thread і Zigbee на ESP32 - esp-matter, OpenThread, esp-zigbee-SDK
description: Три різні відповіді на питання «як розумному дому спілкуватись без хмари»: Matter, Thread і Zigbee.
tags: [esp32, matter, thread, openthread, zigbee, esp-matter, esp32-c6, esp32-h2, border-router, protokoli]
category: Protokoli
date-created: 2026-09-28
date: 2026-09-28
---

# Matter, Thread і Zigbee на ESP32 - esp-matter, OpenThread, esp-zigbee-SDK

> [!warning] Matter/Thread/Zigbee потребують радіо 802.15.4 - це C6/H2, а НЕ C3!
> ESP32-C3 не має 802.15.4 і не підтримує ані Thread, ані Zigbee. Для Matter-over-WiFi підійде будь-який ESP32 з WiFi, але для Matter-over-Thread або Zigbee беріть C6/H2. Див. [C3/C6/H2](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md).

Огляд радіо: [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md), живлення [живлення](../../../ESP32-Reference/02-Zhivlennya/01-Lancjugi-zhivlennya.md), старт [Home](../../../ESP32-Reference/Home.md).

## Призначення

Три різні відповіді на питання «як розумному дому спілкуватись без хмари»:

- **Matter** - прикладний IP-протокол верхнього рівня (застосунок). Працює поверх WiFi, Thread або Ethernet. Єдина «мова» для Apple Home, Google Home, Alexa, SmartThings: один пристрій видно в кількох екосистемах одразу (multi-admin). Комісіонування - через BLE + QR-код/числовий код.
- **Thread** - мережевий транспорт (IPv6 поверх 802.15.4, mesh). Це «дороги», якими їздять Matter-пакети, коли WiFi недоступний або невигідний (батарейні датчики). Thread сам по собі застосунку не дає - поверх нього йде Matter (або plain UDP/CoAP).
- **Zigbee** - зрілий не-IP стек (802.15.4 + власний мережевий/прикладний рівень). Своя екосистема: координатор + роутери + кінцеві пристрої, інтеграція з Home Assistant через ZHA або Zigbee2MQTT. З Matter несумісний безпосередньо - міст через Border Router/хаб.

Коли брати що:

- лампа/розетка в Apple/Google Home без власної хмари - Matter-over-WiFi на будь-якому ESP32;
- батарейний датчик з роками роботи і mesh - Matter-over-Thread на C6/H2;
- велика наявна Zigbee-мережа (десятки пристроїв Aqara/IKEA) - Zigbee-координатор/кінцевий на C6/H2;
- один сенсор до телефону поруч - звичайний BLE, див. [02-BLE-Bluetooth](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md).

## Що обрати - Matter vs Zigbee vs BLE vs WiFi

| Критерій | Matter-over-WiFi | Matter-over-Thread | Zigbee 3.0 | BLE (GATT) | Plain WiFi (MQTT/HTTP) |
| --- | --- | --- | --- | --- | --- |
| Чіпи ESP | будь-який з WiFi | C6/H2 (+Border Router) | C6/H2 | всі | будь-який з WiFi |
| Транспорт | IP/WiFi | 802.15.4 mesh + IP | 802.15.4 mesh, не IP | BLE-з'єднання | IP/WiFi |
| Екосистеми | Apple/Google/Alexa одночасно | ті ж | ZHA/Zigbee2MQTT, хаби | телефон/додаток | своя хмара, Node-RED |
| Комісіонування | BLE + QR/код | BLE + QR/код | pairing (permit join) | connect | provisioning, див. [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) |
| Живлення батарей | погане (WiFi) | відмінне (SED сплять роками) | відмінне | добре | погане без deep-sleep |
| Дальність/топологія | зірка до роутера | mesh, саморемонт | mesh, саморемонт | точка-точка ~10-50 м | зірка до роутера |
| Сертифікація | потрібна для логотипа | потрібна для логотипа | потрібна для логотипа | не потрібна | не потрібна |
| Складність коду | висока (esp-matter) | найвища (matter+thread) | середня (esp-zigbee-SDK) | низька | низька |
| Коли | розетка в HomeKit | датчик на батареї в HomeKit | наявний Zigbee-дім | пульт/маяк поруч | свій дашборд/MQTT |

Правило: **немає екосистем Apple/Google - не платіть ціну Matter**. Для свого дому достатньо Zigbee або MQTT, див. [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md).

## Вимоги до чіпів і пам'яті

| Чіп | WiFi | 802.15.4 | Matter-over-WiFi | Matter-over-Thread / Zigbee | Роль у Thread/Zigbee |
| --- | --- | --- | --- | --- | --- |
| ESP32 Classic | так | ні | так | ні | - |
| ESP32-S3 | так | ні | так | ні | - |
| ESP32-C3 | так | ні | так | ні | - |
| ESP32-C6 | WiFi 6 | так | так | так | вузол, RCP-радіо, Border Router |
| ESP32-H2 | ні | так | ні (немає WiFi) | так | вузол, RCP-радіо |
| ESP32-C2 | так | ні | обмежено (мало RAM) | ні | - |
| ESP32-P4 | ні (треба зовнішнє радіо) | ні | як хост по Ethernet | як хост + C6/H2-радіо по UART/SPI | хост Border Router |

Пам'ять: esp-matter тягне ~1 МБ flash (сертифікати DAC, кластери, BLE-комісіонування) - закладайте flash від 4 МБ і партиції під factory + OTA, див. [Partitions](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md). Thread-вузол на H2 живе в ~320 КБ flash. Деталі заліза: [C3/C6/H2](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md), [C2/P4](../../../ESP32-Reference/01-Hardware/09-ESP32-C2-P4.md).

![](../../../ESP32-Reference/assets/img/matter-thread-zigbee-scheme.png)
*Рис. Matter поверх WiFi і Thread: комісіонування BLE+QR, fabric кількох екосистем, Border Router між Thread-mesh і домашнім LAN.*

### ASCII-схема

```text
ЕКOSИСТЕМИ (multi-admin, одна fabric або кілька):
  Apple Home ─┐
  Google Home ─┼──► WiFi/Ethernet ──► Matter-вузол (ESP32-S3, on-off light)
  Alexa ──────┘                              │
                                             │ Thread-радіо (802.15.4)
                                             ▼
  Thread-mesh: H2-датчик (SED, спить) ──► C6-роутер ──► Border Router (C6+RCP / RPi+OTBR)
                                                    ──► LAN ──► ті самі екосистеми

Zigbee-гілка (окрема мережа, не IP):
  Zigbee-координатор (C6, esp-zigbee-SDK) ──► роутер (лампа) ──► end-device (кнопка, спить)
        │ USB/UART
        ▼
  Home Assistant (ZHA / Zigbee2MQTT) ──► MQTT ──► Node-RED (див. 05-Cloud-Pipeline)

Комісіонування Matter: BLE-advertise + QR (passcode/discriminator) ──► fabric-credentials ──► operational
```

### Mermaid

```mermaid
graph LR
    subgraph ECO[Екосистеми]
        A[Apple Home]
        G[Google Home]
        X[Alexa]
    end
    subgraph IP[Домашній LAN]
        W[Matter-вузол<br/>WiFi S3/C6]
        BR[Border Router<br/>C6/P4 + OTBR]
    end
    subgraph THR[Thread-mesh]
        SED[Датчик H2<br/>sleepy]
        RT[Роутер C6]
    end
    subgraph ZB[Zigbee]
        ZC[Координатор C6]
        ZE[End-device]
    end
    A --> W
    G --> W
    X --> W
    SED --> RT
    RT --> BR
    BR --> W
    ZC --> ZE
    ZC -.->|USB/MQTT| W
```

## esp-matter SDK: комісіонування, кластери, fabric, OTA

**Комісіонування (BLE + QR).** Новий пристрій рекламується по BLE. Комісіонер (телефон з Home) зчитує QR: там passcode, discriminator і дані для PASE-сесії. Далі по BLE йдуть operational-credentials (NOC - node operational certificate), пристрій входить у **fabric** і переходить на робочий транспорт (WiFi/Thread). Практика: QR друкуйте на корпусі + тримайте копію; без заводського QR перекомісіонування - через ручне введення коду з консолі.

**Модель даних: endpoints → clusters → attributes/commands.**

| Рівень | Приклад (розумна лампа) | Примітка |
| --- | --- | --- |
| Endpoint 0 | Root Node (Descriptor, Basic Information, OTA) | службовий, є завжди |
| Endpoint 1 | On/Off Light (0x0100): OnOff-сервер, LevelControl-сервер | твій пристрій |
| Cluster-сервер | OnOff (0x0006): атрибут `OnOff`, команди `On/Off/Toggle` | стан + керування |
| Cluster-клієнт | OnOff-клієнт на вимикачі - шле команди лампі | binding |
| Атрибут | `OnOff = true`, reporting при зміні | підписки екосистем |

**Fabric і multi-admin.** Fabric - домен безпеки (один дім = одна fabric; пристрій може бути в кількох - multi-admin: Apple + Google одночасно). Кожна fabric має свій NOC і своїх адмінів. Видалення fabric = «прибрати з дому» без скидання інших.

**Matter OTA.** Прошивка тягнеться через BDX-протокол від OTA-провайдера (хаб/телефон), образ перевіряється за VID/PID/версією. Закладайте два OTA-слоти, див. [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md).

Приклади esp-matter: `examples/light` (on-off + level), `examples/light_switch` (клієнт), `examples/thermostat`. Збірка - тільки ESP-IDF (esp-matter як компонент, CMake).

## Thread, OpenThread і Border Router

**Ролі вузлів Thread:**

| Роль | Живлення | Що робить | Приклад |
| --- | --- | --- | --- |
| Leader | мережа | керує mesh, один на мережу | C6-роутер |
| Router | мережа | ретранслює, до 32 на мережу | C6-лампа |
| Child (FTD/MTD) | мережа/батарея | говорить через батька | H2-вимикач |
| SED (Sleepy End Device) | батарея, роки | спить, опитує батька | H2-датчик дверей |

**OpenThread на ESP:** стек OpenThread в ESP-IDF (`CONFIG_OPENTHREAD_*`), транспорт 802.15.4 на C6/H2. Два дизайни: SoC (все на одному C6) або **RCP** (C6/H2 - тільки радіо по Spinel/UART, а стек і застосунок - на хості: P4 або Linux).

**Border Router (OTBR):** міст Thread-mesh ↔ WiFi/Ethernet. Варіанти: готовий OTBR на Raspberry Pi + C6/H2-RCP, або ESP32-Border-Router (C6-радіо + WiFi-аплінк). Без Border Router Thread-пристрої ізольовані від LAN і екосистем - це помилка №1 новачків.

> [!tip] C6 як радіо + P4 як хост
> Зв'язка з ТЗ: P4 (потужний хост без радіо) + C6/H2 як RCP по UART/SPI. Використовуйте офіційний образ `esp-border-router` і транспорт Spinel - не винаходьте свій протокол між хостом і радіо.

## esp-zigbee-SDK: ролі, pairing, touchlink

**Ролі:**

| Роль | Живлення | Приклад | Примітка |
| --- | --- | --- | --- |
| Coordinator | мережа, 1 на мережу | C6-стік на Home Assistant | формує мережу, зберігає таблиці |
| Router | мережа | лампа/розетка | ретранслює, діти до нього чіпляються |
| End Device | батарея | кнопка/датчик | спить, опитує батька |

**Pairing з ZHA/Zigbee2MQTT:** у координатора/ХАБа вмикається `permit join` (60-120 с), пристрій переводиться в pairing (кнопка/ресет), далі interview (кластери) і поява в HA. Канали 11-26 (2.4 ГГц); канали 25-26 перетинаються з WiFi 11-м - при глухому ефірі змініть канал координатора. Приклади SDK: `examples/esp_zigbee_HA_sample` (HA on-off light/switch), `HA_on_off_light`, `HA_on_off_switch`.

**Touchlink (оглядово).** Пряме спарювання «лампа↔пульт» зблизька (кілька метрів, знижена потужність), без координатора: пульт «краде» лампу в свою міні-мережу. Корисно для демо, у продакшені - обережно: touchlink може відв'язати чужу лампу через стіну, тому тримайте його вимкненим за замовчуванням.

> [!warning] Zigbee і Matter - різні мережі
> Zigbee-пристрій не з'явиться в Apple Home безпосередньо. Міст - через Home Assistant (ZHA/Z2M → HomeKit-bridge) або Matter-bridge-пристрій. Закладайте це в архітектуру одразу.

## Код - комісіонування і кластер on-off

**ESP-IDF, esp-matter: on-off light (скорочено, приклад `examples/light`):**

```c
// idf.py menuconfig: ESP_MATTER_ENABLE_DATA_MODEL_SERVER, WiFi/Thread транспорт,
// BLE-комісіонування увімкнено. QR-код друкується в лог при старті.
// Ключові кроки light-прикладу:
#include <esp_matter.h>
#include <esp_matter_console.h>

static void *s_onoff_handle; // дескриптор кластера OnOff (endpoint 1)

static esp_err_t onoff_cb(esp_matter::attribute::callback_type_t type, uint16_t ep,
                          uint32_t cluster, uint32_t attr, esp_matter_attr_val_t *val,
                          void *priv)
{
    if (type == esp_matter::attribute::callback_type_t::PRE_UPDATE) {
        bool on = val->val.b;                 // новий стан OnOff
        gpio_set_level(GPIO_NUM_2, on);       // фізична лампа/світлодіод
    }
    return ESP_OK;
}

void app_main(void)
{
    nvs_flash_init();                         // fabric-дані і QR живуть у NVS!
    esp_matter::node_t *node = esp_matter::node::create_raw();
    esp_matter::endpoint_t *ep =
        esp_matter::endpoint::on_off_light::create(node, NULL, NULL, NULL);
    s_onoff_handle = esp_matter::cluster::get_first(ep); // OnOff-кластер
    esp_matter::attribute::set_callback(onoff_cb);       // колбек PRE_UPDATE
    esp_matter::start();                        // старт + BLE-advertise для комісіонування
    // QR/passcode шукайте в логу: "QR Code URL: ...", "Manual pairing code: ..."
}
```

**ESP-IDF, esp-zigbee-SDK: HA on-off light (скорочено, `HA_on_off_light`):**

```c
// menuconfig: Zigbee channel/mode (Coordinator/Router/End Device), install code.
// Кнопка BOOT — toggle локально + report; pairing — довге утримання.
#include "esp_zigbee_core.h"

static void bdb_start_top_level_commissioning_cb(uint8_t mode_mask)
{
    ESP_ERROR_CHECK(esp_zb_bdb_start_top_level_commissioning(mode_mask));
}

void esp_zb_app_signal_handler(esp_zb_app_signal_t *sig)
{
    if (sig->p_app_signal == ESP_ZB_BDB_SIGNAL_STEERING) {
        // пристрій у мережі (coordinator відкрив permit join)
    }
}

static esp_err_t zb_onoff_handler(const esp_zb_zcl_set_attr_value_message_t *m)
{
    if (m->info.cluster == ESP_ZB_ZCL_CLUSTER_ID_ON_OFF &&
        m->attribute.id == ESP_ZB_ZCL_ATTR_ON_OFF_ON_OFF_ID) {
        gpio_set_level(GPIO_NUM_2, m->attribute.data.value.__u8);
    }
    return ESP_OK;
}

void app_main(void)
{
    esp_zb_cfg_t cfg = { .esp_zb_role = ESP_ZB_DEVICE_TYPE_ED, // або ROUTER/COORDINATOR
                         .install_code_policy = false };
    esp_zb_init(&cfg);
    esp_zb_on_off_light_cfg_t light = ESP_ZB_DEFAULT_ON_OFF_LIGHT_CONFIG();
    esp_zb_ep_list_t *ep = esp_zb_on_off_light_ep_create(10, &light);
    esp_zb_device_register(ep);
    esp_zb_core_action_handler_register(zb_onoff_handler);
    ESP_ERROR_CHECK(esp_zb_start(false)); // false = не factory-reset при старті
    esp_zb_main_loop_iteration();         // головний цикл стеку
}
```

**Arduino:** офіційної Arduino-обгортки esp-matter/esp-zigbee-SDK немає - ці стеки збираються тільки під ESP-IDF (CMake, партиції, NVS-фабричні дані). Практика: Matter/Zigbee-вузол пишіть на ESP-IDF, а Arduino-логіку тримайте на другому контролері або спілкуйтесь через UART/MQTT-міст. Не намагайтесь «залити Matter скетчем» - це глухий кут.

**MicroPython:** підтримки Matter/Thread/Zigbee у MicroPython немає (немає 802.15.4-драйвера і місця під сертифікати). Практика: MicroPython-вузол говорить з шлюзом по MQTT/UART (див. [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md)), а Matter/Zigbee-частину тримає окремий C6/H2 на ESP-IDF.

## Типові помилки

| Симптом | Причина | Рішення |
| --- | --- | --- |
| Thread/Zigbee не збирається на C3 | немає радіо 802.15.4 на C3 | перейти на C6/H2, див. [C3/C6/H2](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md) |
| Телефон не бачить QR / комісіонування висить | BLE зайнято іншим стеком; фабричні дані стерті | чистий приклад `light`, перевірити лог QR; не стирати NVS після комісіонування |
| Пристрій у fabric, але «не відповідає» | немає маршруту: Thread без Border Router; WiFi в іншому VLAN | підняти OTBR; тримати IoT і телефон в одному L2 |
| Після `erase_flash` пристрій «привид» у Home | fabric-дані лишились у хабі | видалити вузол з усіх fabric (усіх екосистем) до перепрошивки |
| Zigbee-інтерв'ю падає в ZHA/Z2M | сівший акумулятор end-device; канал з перешкодами | свіжа батарея; змінити канал координатора; роутер ближче |
| Touchlink «вкрав» чужу лампу | touchlink увімкнено скрізь | вимикати touchlink за замовчуванням, вмикати на хвилину |
| OTA Matter не стартує | не збігаються VID/PID/версія; малий OTA-слот | вирівняти версії в дескрипторі; партиції під два слоти |
| NVS переповнено після десятків комісіонувань | старі fabric не чистяться | factory-reset через довгу кнопку + `nvs_flash_erase()` |

## Офіційні джерела

- [ESP-Matter - Programming Guide](https://docs.espressif.com/projects/esp-matter/en/latest/) - комісіонування, data model, Matter OTA, приклади light/switch.
- [ESP Zigbee SDK - Programming Guide](https://docs.espressif.com/projects/esp-zigbee-sdk/en/latest/) - ролі, HA-приклади, API reference.
- [OpenThread](https://openthread.io/guides/border-router) - Border Router, Commissioner, RCP-дизайн.
- [Matter - Connectivity Standards Alliance](https://csa-iot.org/all-solutions/matter/) - специфікація, сертифікація, multi-admin.

## Див. також

- [Home](../../../ESP32-Reference/Home.md)
- [BLE/Bluetooth](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) - BLE-комісіонування Matter, GATT-база
- [BLE Mesh / A2DP / HID](../../../ESP32-Reference/05-Radio/05-BLE-Mesh-A2DP-HID.md) - інший BLE-стек Espressif, A2DP тільки на Classic
- [ESP32-C3/C6/H2](../../../ESP32-Reference/01-Hardware/04-ESP32-C3-C6-H2.md) - яке радіо де є
- [ESP32-C2/P4](../../../ESP32-Reference/01-Hardware/09-ESP32-C2-P4.md) - P4 як хост Border Router
- [Аудіо-кодеки](../../../ESP32-Reference/11-Vivid/13-Audio-Codecs.md) - I2S-звук для голосових Matter-пристроїв
- [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) - міст Zigbee2MQTT → хмара
- [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) - введення WiFi без перепрошивки
- [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md) - слоти під Matter OTA
- [NVS](../../../ESP32-Reference/08-Pamyat/01-Partitions-NVS.md) - fabric-дані живуть у NVS
