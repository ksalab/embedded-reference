---
title: Arduino Nextion HMI - розумний дисплей з редактором
description: Будує інтерфейс на Nextion-дисплеї - редактор, сторінки і компоненти, протокол UART і зв'язка з Arduino.
tags: [arduino, nextion, hmi, display, uart, touchscreen, editor]
category: Vivid
date-created: 2026-10-06
date: 2026-10-06
---

# Arduino Nextion HMI - розумний дисплей з редактором

![[assets/img/ard-nextion-hmi-scheme.png|600]]
*Рис. Розумний дисплей: інтерфейс живе в Nextion, Arduino шле дані і ловить натискання - UART міст.*

> [!tip] Що це за нота
> Дисплей-комп'ютер: малюємо інтерфейс мишею в редакторі, Arduino лише постачає дані. Протилежність TFT, де малює контролер. База: [[11-Vivid/07-TFT-Touch-Deep|TFT з тачем]], [[04-Shini/01-UART|шина UART]].

## 1. Мета

Віддати інтерфейс дисплею:

- редактор Nextion: сторінки, кнопки, графіки, клавіатури;
- протокол: текстові команди туди, події сюди;
- зв'язка з Arduino: дані вгору, натискання вниз;
- SD-картка дисплея: прошивка інтерфейсу;
- коли Nextion, а коли TFT.

| Підхід | Де логіка | Плюси |
| --- | --- | --- |
| Nextion | у дисплеї | Arduino вільний, краса мишею |
| TFT+LVGL | у контролері | гнучкість, дешевше |

## 2. Архітектура

```mermaid
flowchart TB
  ARD[Uno/Mega] <-->|UART 9600| NXT[Nextion 3.5"/7"]
  NXT --> SCR[Сторінки: головна/графік/налаштування]
  SCR --> TOUCH[Кнопки/повзунки]
  TOUCH -->|події| ARD
  ARD -->|t0.txt="23.5"| NXT
  SENS[Датчики] --> ARD
  NXT --> SDCARD[SD: прошивка .tft]
```

Протокол текстовий з термінатором `FF FF FF`. Arduino шле `t0.txt="23.5"`, дисплей відповідає подіями кнопок.

## 3. Розпіновка дисплея

| Сигнал Nextion | Пін Uno | Примітка |
| --- | --- | --- |
| TX | D2 (RX софтверний) | перехресно! |
| RX | D3 (TX софтверний) | 5V логіка ок |
| 5V/GND | живлення | 500 мА+ для 7"! |
| SD-слот | прошивка .tft | FAT32, файл `fw.tft` |

Великі діагоналі їдять струм підсвітки: окреме живлення 5V 2A, не з USB.

## 4. Редактор: перший проєкт

- сторінка `page0`: фон, текст `t0`, кнопка `b0`, графік `s0`;
- системні змінні: `bkcmd`, `baud`, `thup` (тач-прокидання);
- подія кнопки: `Touch Press → print "B0"`;
- компіляція → `.tft` на SD → вставити → перезавантажити;
- налагодження: вкладка Debug шле команди вживу.

## 5. Робочий код (C, Arduino)

```cpp
#include <SoftwareSerial.h>
SoftwareSerial nxt(2, 3);

void nxt_cmd(const char *cmd) {
  nxt.print(cmd);
  nxt.write(0xFF);
  nxt.write(0xFF);
  nxt.write(0xFF);
}

void setup() {
  Serial.begin(115200);
  nxt.begin(9600);
  nxt_cmd("page 0");
}

void loop() {
  static unsigned long t0 = 0;
  if (millis() - t0 > 2000) {
    t0 = millis();
    char buf[32];
    snprintf(buf, sizeof(buf), "t0.txt=\"%.1f\"", analogRead(A0) * 0.488);
    nxt_cmd(buf);
    snprintf(buf, sizeof(buf), "s0.add %d,%d", 0, (int)(analogRead(A0) / 4));
    nxt_cmd(buf);
  }
  static String ev;
  while (nxt.available()) {
    char c = nxt.read();
    if (c == '\n' || ev.length() > 20) {
      if (ev == "B0") digitalWrite(5, !digitalRead(5));
      if (ev == "B1") digitalWrite(6, HIGH);
      ev = "";
    } else if (c >= 32) {
      ev += c;
    }
  }
}
```

Події кнопок - текстом з дисплея (`print` у редакторі). Парсимо рядки, виконуємо. Затримки відповіді - мілісекунди.

## 6. Робочий код (MicroPython)

```python
# MicroPython: Nextion-міст (UART + події)
import time
from machine import UART, Pin, ADC

nxt = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
adc = ADC(Pin(26))

def cmd(s):
    nxt.write(s.encode() + b'\xff\xff\xff')

def read_event(timeout=0.2):
    t0 = time.ticks_ms()
    buf = b''
    while time.ticks_diff(time.ticks_ms(), t0) < int(timeout * 1000):
        if nxt.any():
            buf += nxt.read(1)
            if buf.endswith(b'\xff\xff\xff'):
                return buf[:-3]
    return None

cmd('page 0')
while True:
    v = adc.read_u16() * 3.3 / 65535
    cmd('t0.txt="%0.1f"' % (v * 100))
    ev = read_event()
    if ev == b'B0':
        print('button B0')
    time.sleep(2)
```

Термінатор `FF FF FF` - межа пакетів. Читаємо до термінатора, не фіксовану довжину.

## 7. Компоненти редактора

- текст/числа: `t0`, `x0` (плаваюча точка!);
- кнопки dual-state: стан видно без Arduino;
- повзунок `h0`: значення їде в контролер;
- графік `s0`: канали, кольори, сітка;
- клавіатура: ввід WiFi-пароля на місці;
- таймер `tm0`: періодичні дії без контролера.

## 8. Типові помилки

| Симптом | Причина | Лікування |
| --- | --- | --- |
| Мовчить після прошивки | швидкість не та | baud дисплея = baud порту |
| Сміття замість тексту | немає термінатора | три байти FF в кінці кожної команди |
| SD не прошиває | не FAT32 / не той файл | FAT32, файл у корені |
| Кнопки не шлють | немає print у події | додати `print "B0"` в редакторі |
| Гасне підсвітлення | слабке живлення 7" | окремий БЖ 5V 2A |
| Лагає відгук | SoftwareSerial на 115200 | 9600 для Nextion достатньо |

## 9. Швидка шпаргалка Nextion

- команди текстом + `FF FF FF`;
- baud однаковий з обох боків;
- прошивка .tft з FAT32-картки;
- події - print-рядками;
- логіка в дисплеї, дані - з Arduino.

## 10. Суміжні ноти

- [[11-Vivid/07-TFT-Touch-Deep|TFT з тачем]] - дурний дисплей-альтернатива.
- [[11-Vivid/04-TFT-ST7735|дисплей TFT]] - стартова нота.
- [[04-Shini/01-UART|шина UART]] - транспорт дисплея.
- [[02-Zhivlennya/01-Zhivlennya-VIN|живлення VIN]] - струм підсвітки.
- [[Home|головна карта]] - повна навігація.

## Офіційні джерела

- [NX8048T070 Datasheet (Nextion)](https://nextion.tech/datasheets/nx8048t070/) - команди, компоненти, живлення.
- [Language Reference (Arduino docs)](https://docs.arduino.cc/language-reference/) - SoftwareSerial, рядки.
- [Ethernet Shield Rev2 (Arduino docs)](https://docs.arduino.cc/hardware/ethernet-shield-rev2/) - приклад конфлікту UART/SPI пінів.
