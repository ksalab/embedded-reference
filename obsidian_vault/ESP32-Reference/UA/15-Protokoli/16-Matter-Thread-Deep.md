---
title: ESP32 Matter-over-Thread - глибокий розбір Fabric, кластерів і commissioning
description: Будує Matter-пристрої на ESP32-H2/C6 - Fabric і NodeID, кластери OnOff/Level, BLE-commissioning, border router з кодом.
tags: [esp32, matter, thread, openthread, c6, h2, ble, commissioning, iot]
category: Protokoli
date: 2026-10-06
---

# ESP32 Matter-over-Thread - глибокий розбір Fabric, кластерів і commissioning

![[assets/img/esp32-matter-thread-deep-scheme.png|600]]
*Рис. Matter-вузол: 802.15.4-радіо C6/H2, Thread-мережа, border router в IP, комісія через BLE.*

> [!tip] Що це за нота
> Глибина поверх оглядової Matter-ноти: тут Fabric, кластери і код, а не маркетинг. Потрібні C6 або H2 (є 802.15.4). База: [[01-Hardware/04-ESP32-C3-C6-H2|чипи C3/C6/H2]], [[15-Protokoli/09-Matter-Thread-Zigbee|Matter оглядово]].

## 1. Мета

Зібрати сертифіковно-сумісний Matter-вузол:

- Fabric: що це і чому один пристрій у кількох домах;
- кластери OnOff/LevelControl/Color: кінцевий вимикач і лампа;
- commissioning по BLE: QR, passcode, discriminator;
- border router: Thread↔WiFi на другому ESP32;
- пам'ять: скільки їсть Matter на C6.

| Елемент | Роль | Де живе |
| --- | --- | --- |
| Node | пристрій (лампа) | ESP32-C6/H2 |
| Fabric | домен довіри + ключі | комісіонер і вузол |
| Cluster | функція (OnOff) | endpoint вузла |
| Commissioner | вводить у Fabric | телефон/хаб |
| Border Router | Thread↔IP міст | ESP32 + WiFi |

## 2. Архітектура

```mermaid
flowchart TB
  LAMP[ESP32-C6: лампа Matter] <-->|802.15.4| THR[Thread-мережа]
  THR <--> BR[Border Router: ESP32]
  BR <-->|WiFi/IP| HOME[Apple/Google/Alexa дом]
  PHONE[Телефон-комісіонер] -->|BLE| LAMP
  LAMP --> LED[Relay + LED]
```

Commissioning йде по BLE (тимчасово), робота - по Thread. WiFi на вузлі не потрібен взагалі.

## 3. Розпіновка вузла (DevKitC-H2/C6)

| Пін плати | Призначення | Примітка |
| --- | --- | --- |
| GPIO8 | Реле/LED (OnOff-кластер) | через транзистор, не безпосередньо! |
| GPIO9 | Кнопка commissioning | на землю, pull-up |
| GPIO20/21 | UART-лог | 115200 для моніторингу |
| 3V3/GND | живлення | 500 мА запас |
| EN/BOOT | прошивка | кнопки плати |

Реле - тільки модулем з опторозв'язкою. Мережева частина - за електриком, не за цією нотою.

## 4. Commissioning покроково

- прошиваємо приклад `light` з esp-matter;
- QR на екрані монітора: `MT:XXXX-XXX-XXXX`;
- телефон (Apple Home/Google Home) → додати пристрій → сканувати QR;
- BLE-сесія обмінюється ключами Fabric (CASE/PASE);
- після комісії BLE можна вимкнути - далі Thread;
- другий дім - той же вузол, новий Fabric (multi-admin!).

## 5. Робочий код (C, ESP-IDF)

```c
#include "esp_matter.h"

static esp_err_t on_off_cb(esp_matter_cluster_t *cluster, uint32_t cmd) {
  bool on = (cmd == 1);
  gpio_set_level(GPIO_NUM_8, on);
  esp_matter_attr_val_t val = {.b = on};
  esp_matter_cluster_update(cluster, 0, &val);
  return ESP_OK;
}

void app_main(void) {
  esp_matter_node_t *node = esp_matter_node_create(NULL, 0, 0, 0);
  esp_matter_endpoint_t *ep = esp_matter_endpoint_create(node, 0);
  esp_matter_cluster_t *cl = esp_matter_cluster_create_on_off(ep, on_off_cb);
  (void)cl;
  esp_matter_start();
}
```

Кластер OnOff: команда 0/1, атрибут стану, підписка контролера. Колбеки - короткі, важке - в чергу.

## 6. Робочий код (MicroPython)

```python
# MicroPython: Matter-клієнт-емуляція через BLE-GATT (навчальний міст)
# Повний Matter-стек на MicroPython нема — керуємо вузлом HTTP-мостом
import network
import urequests
import time
from machine import Pin

relay = Pin(8, Pin.OUT)
btn = Pin(9, Pin.IN, Pin.PULL_UP)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ssid', 'pass')
while not wlan.isconnected():
    time.sleep(0.5)

BRIDGE = 'http://border-router.local:8080'

def set_lamp(on):
    urequests.post(BRIDGE + '/lamp', json={'on': on})
    relay.value(on)

while True:
    if not btn.value():
        set_lamp(not relay.value())
        time.sleep(0.5)
    time.sleep(0.05)
```

Чесно: Matter-commissioning на MicroPython не реалізувати розумно - міст через border router дає той же результат (керування лампою) малою кров'ю.

## 7. Border Router

- другий ESP32 (S3/C6) з RCP-прошивкою OpenThread + WiFi;
- `otbr-agent` або ESP Thread Border Router приклад;
- Thread-мережа отримує IPv6-префікс з LAN;
- mDNS/DNS-SD - виявлення вузлів контролерами;
- живлення 24/7, провідний uplink бажано.

## 8. Пам'ять і межі C6

| Ресурс | Витрата Matter | Залишок |
| --- | --- | --- |
| Flash | ~1.5 МБ (стек+кластери) | під OTA-запас |
| RAM | ~150 КБ runtime | обережно з буферами |
| NVS | ключі Fabric + лічильники | не прати без decommission! |

Фабричний ресет - кнопкою за процедурою (утримання 10 с), інакше ключі залишаться і комісія зависне.

## 9. Типові помилки

| Симптом | Причина | Лікування |
| --- | --- | --- |
| Комісія падає на 90 % | BLE розрив / далеко | телефон поруч, без металу між |
| Вузол не в Thread | немає лідера/border router | підняти BR першим |
| Працює, після ребута - ні | стерто NVS з ключами | не прати flash цілком, тільки app |
| Дві лампи плутаються | однакові discriminator | унікальний дискримінатор на вузол |
| Apple бачить, Google ні | лише один Fabric | multi-admin: додати другий дім |
| Пам'яті не вистачає | важкі кластери + лог | рівень логу Error, оптимізувати партиції |

## 10. Швидка шпаргалка Matter

- вузол: C6/H2, приклад light;
- комісія: QR + BLE поруч;
- робота: Thread, BR 24/7;
- NVS з ключами - святе;
- multi-admin - фішка, не баг.

## 11. Суміжні ноти

- [[15-Protokoli/09-Matter-Thread-Zigbee|Matter оглядово]] - стартова картина.
- [[01-Hardware/04-ESP32-C3-C6-H2|чипи C3/C6/H2]] - радіо 802.15.4.
- [[15-Protokoli/01-MQTT|протокол MQTT]] - альтернативний транспорт.
- [[14-Devboards/13-ESP32C6-Boards|плати C6]] - залізо вузла.
- [[Home|головна карта]] - повна навігація.

## Офіційні джерела

- [esp-matter (Espressif, GitHub)](https://github.com/espressif/esp-matter) - SDK, приклади, комісія.
- [ESP-Matter Docs (Espressif)](https://docs.espressif.com/projects/esp-matter/en/latest/) - Fabric, кластери, пам'ять.
- [esp-thread-br (Espressif, GitHub)](https://github.com/espressif/esp-thread-br) - border router, RCP, IPv6.

> English twin: [[15-Protokoli/16-Matter-Thread-Deep.en.md | EN]]
