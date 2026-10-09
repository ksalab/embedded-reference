---
title: ESP32 Ethernet глибоко - W5500, PoE and провідний шлюз
description: Будує провідний вузол on ESP32 - W5500 per SPI, PoE-живлення, Ethernet+WiFi резервування and MQTT-шлюз with кодом.; shows schematics, code and tables.
tags: [esp32, ethernet, w5500, poe, spi, gateway, mqtt, wired]
category: Moduli-zvyazku
date: 2026-10-06
---

# ESP32 Ethernet глибоко - W5500, PoE and провідний шлюз

![[assets/img/esp32-ethernet-poe-deep-scheme.png|600]]
*Fig. Провідний вузол: W5500 per SPI дає TCP/IP, PoE-спліттер - вати, WiFi лишається резервом.*

> [!tip] that this for нота
> Коли радіо not варіант: цех, підвал, серверна. Апаратний TCP/IP in W5500 розвантажує кристал, PoE прибирає БЖ. База: [[04-Interfaces/02-SPI|bus SPI]], [[12-Comm-Modules/07-SIM7600-W5500-MCP2515|модулі SIM/W5500]].

## 1. Мета

Побудувати вузол, якому not потрібен ефір:

- W5500 per SPI: сокети, швидкості, ліміти;
- PoE: спліттер vs PoE-HAT for ESP32;
- резервування Ethernet+WiFi with автоперемиканням;
- шлюз RS485→Ethernet→MQTT.

| Варіант | Швидкість | Коли |
| --- | --- | --- |
| W5500 module | 10/100, SPI 80 МГц | універсально |
| Вбудований MAC+PHY (рідкісні плати) | 10/100 | якщо є on платі |
| PoE-спліттер 5V | + вати per кабелю | стеля/шафа |
| WiFi-бекап | - | резерв каналу |

## 2. Архітектура

```mermaid
flowchart TB
  ESP[ESP32] <-->|SPI 40 МГц| W5[W5500]
  W5 <-->|RJ45| LAN[Мережа]
  POE[PoE-інжектор] -->|вати| SPL[Спліттер 5V]
  SPL --> ESP
  ESP <-->|UART| RS[RS485-пристрої]
  ESP -->|MQTT| BRK[broker]
  ESP -.->|резерв| WIFI[WiFi]
```

W5500 тримає 8 сокетів апаратно: TCP/IP not їсть CPU. SPI on 40 МГц - межа стабільності on довгих дротах.

## 3. Розпіновка модуля W5500

| Пін ESP32 | Пін W5500 | Примітка |
| --- | --- | --- |
| GPIO18 | SCK | такт до 80 МГц |
| GPIO23 | MOSI | дані in module |
| GPIO19 | MISO | дані with модуля |
| GPIO5 | CS | вибір кристала |
| GPIO4 | INT | переривання сокетів |
| GPIO2 | RST | апаратний ресет |
| 3V3/GND | VCC/GND | 200 мА запас |

Довжина SPI-шлейфа до 10 см on 40 МГц. Довше - опускати до 20 МГц або буфери.

## 4. PoE-практика

- спліттер 5V 2A: стандартний 802.3af вхід, USB-C/гребінка вихід;
- гальванічна розв'язка всередині - земля мережі not йде in плату;
- бюджет: плата + датчики + запас 30 %;
- грозозахист on вуличних прольотах;
- тестер PoE показує клас пристрою до вмикання.

## 5. Робочий code (C, Arduino)

```cpp
#include <SPI.h>
#include <Ethernet.h>

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x01};
EthernetClient client;

void setup() {
  Serial.begin(115200);
  SPI.begin(18, 19, 23, 5);
  Ethernet.init(5);
  if (Ethernet.begin(mac) == 0) {
    Ethernet.begin(mac, IPAddress(192, 168, 1, 177));
  }
  Serial.println(Ethernet.localIP());
}

void loop() {
  if (!client.connected()) {
    client.stop();
    client.connect("broker.local", 1883);
  }
  static unsigned long t0 = 0;
  if (millis() - t0 > 5000) {
    t0 = millis();
    client.println("PUB sensors/temp 23.5");
  }
  Ethernet.maintain();
}
```

`Ethernet.maintain()` - продовження DHCP-оренди. Статика надійніша for 24/7: менше точок відмови.

## 6. Робочий code (MicroPython)

```python
# MicroPython + W5500 (драйвер wiznet5k)
import network
import time
from machine import Pin, SPI

spi = SPI(1, baudrate=40000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
nic = network.WIZNET5K(spi, Pin(5), Pin(4))
nic.active(True)
nic.ifconfig(('192.168.1.177', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
print(nic.ifconfig())

import usocket
while True:
    try:
        s = usocket.socket()
        s.connect(('broker.local', 1883))
        s.send(b'PUB sensors/temp 23.5\n')
        s.close()
    except OSError as e:
        print('net error', e)
    time.sleep(5)
```

WIZNET5K-драйвер є in прошивках with мережевою підтримкою. Немає - збираємо свою with модулем `wiznet5k`.

## 7. Резервування каналів

- основний Ethernet, WiFi - `reconnect` at втраті лінка;
- check: ping шлюзу кожні 30 с;
- MQTT-брокерів два (локальний + хмара) - клієнт перебирає;
- статичні IP обом інтерфейсам - without DHCP-залежності;
- журнал перемикань - for розбору нестабільності.

## 8. typical errors

| Symptom | Cause | Лікування |
| --- | --- | --- |
| DHCP 0.0.0.0 | лінка немає/кабель | verify LED Link/Act, інший кабель |
| Рветься on 40 МГц SPI | довгий шлейф | 20 МГц або коротше 10 см |
| Працює хвилину and висне | немає `maintain()` | викликати in циклі або статика |
| PoE not живить | пасивний інжектор | тільки 802.3af/at активний |
| Сокети закінчились | not закриваємо with'єднання | `stop()` + таймаути |
| Повільно після WiFi | обидва стеки активні | пріоритет Ethernet, WiFi in сон |

## 9. Швидка шпаргалка Ethernet

- SPI 40 МГц, шлейф до 10 см;
- статика замість DHCP for 24/7;
- PoE - тільки активний стандарт;
- сокети закривати with таймаутом;
- WiFi - резерв, not основа.

## 10. Суміжні ноти

- [[12-Comm-Modules/07-SIM7600-W5500-MCP2515|модулі SIM/W5500]] - огляд модуля.
- [[04-Interfaces/02-SPI|bus SPI]] - швидкості and CS.
- [[15-Protocols/01-MQTT|протокол MQTT]] - телеметрія.
- [[02-Power-Supply/02-LDO-DC-DC|живлення]] - стабільні 3.3V.
- [[Home|головна карта]] - повна навігація.

## Official sources

- [W5500 (WIZnet Docs)](https://docs.wiznet.io/Product/Chip/Ethernet/W5500) - регістри, сокети, SPI.
- [Ethernet examples (Espressif, GitHub)](https://github.com/espressif/esp-idf/tree/master/examples/ethernet) - драйвери and події.
- [MQTT Specification (OASIS)](https://mqtt.org/mqtt-specification/) - протокол поверх TCP.
