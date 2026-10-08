---
title: Глосарій ESP32 - 90+ термінів
tags:

  - esp32
  - esp32/start
  - esp32/glossary

aliases:

  - Глосарій
  - Glossary
  - Словник термінів

type: reference
---

# Глосарій ESP32 - 90+ термінів

EN version: `00-Start/02-Glossary.en.md`

> [!tip] Як користуватись
> Таблиця відсортована за темами. Колонка «Посилання» веде до розділів довідника: старт - [Як користуватись](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md), чипи - [Порівняння чипів](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md), плати - [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md), SDK - [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md), структура датчика - [Шаблон компонента](../../../ESP32-Reference/_templates/Component-Template.md), огляд - [Home](../../../ESP32-Reference/Home.md).
>
> [!warning] Напруги в термінах
> Де б не зустрічались TTL, VCC, HIGH - для ESP32 HIGH = 3.3V. 5V TTL (як в Arduino Uno) **несумісний** з GPIO без узгодження. Vin 5V - це лише вхід LDO, не рівень логіки.

## Базові поняття та живлення

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| GPIO | Лінія вводу-виводу загального призначення | Програмований цифровий пін, 3.3V, max ~12 мА (реком. ≤6 мА) | [Старт](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md) |
| VCC / VDD | Живлення | Для кристала - 3.3V; 5V - лише на VIN/USB до LDO | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| GND | Земля | Спільна точка, обов'язкова між усіма модулями | [Шаблон](../../../ESP32-Reference/_templates/Component-Template.md) |
| LDO | Лінійний стабілізатор | AMS1117/ME6211: 5V→3.3V, гріється, ~500 мА max | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| Level-shifter | Узгоджувач рівнів | TXS0108E, BSS138, дільник 1k/2k для 5V↔3.3V | [Шаблон](../../../ESP32-Reference/_templates/Component-Template.md) |
| Strapping pins | Піни конфігурації завантаження | GPIO0/2/5/12/15: рівні при reset визначають boot/flash | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| EN (CHIP_PU) | Увімкнення кристала | HIGH=робота, кнопка EN = reset | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| BOOT (GPIO0) | Режим завантаження | Утримувати при reset для download-режиму | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| eFuse | Одноразово програмована пам'ять | Калібрування ADC, ключі flash-шифрування, USB VID | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Deep-sleep | Глибокий сон | 5-10 мкА, працює ULP/RTC, пробудження по таймеру/touch | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| ULP | Ультра-низькоспоживчий співпроцесор | RISC-V/FSM для опитування датчиків у сні | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |

## Аналогова периферія

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| ADC | Аналого-цифровий перетворювач | 12-біт, 0-3.3V (через атенюацію), нелінійний по краях | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| ADC attenuation | Атенюація АЦП | 0/2.5/6/11 дБ: діапазони до ~1.1/1.5/2.2/3.3V | [Home](../../../ESP32-Reference/Home.md) |
| DAC | Цифро-аналоговий перетворювач | 8-біт, GPIO25/26, тільки класичний ESP32 | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| PWM / LEDC | ШІМ | LEDC до 40 МГц (теоретичний максимум; практично - герци/кілогерци), 1-16 біт; для LED, серво (50 Гц) | [Глосарій (цей файл)](../../../ESP32-Reference/00-Start/02-Glosariy.md) |
| MCPWM | ШІМ для двигунів | Апаратний ШІМ з dead-time для BLDC/H-мостів | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Touch sensor | Ємнісний сенсор | T0-T9, пробудження з deep-sleep дотиком | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Hall sensor | Датчик Холла | Вбудований в ESP32-Classic, грубий, для демо | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Vref | Опорна напруга АЦП | ~1.1V внутр., розкид між чипами, потрібна калібрування | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| SAR-ADC | АЦП послідовного наближення | Тип АЦП ESP32: 12-біт, швидкий, нелінійний по краях шкали | [ADC](../../../ESP32-Reference/06-Analog/01-ADC.md) |
| FOC | Векторне керування мотором | Field-Oriented Control: 3-фазний міст + енкодер кута, тихий момент | [Потужність/Рух](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md) |
| Deadtime | Мертвий час ключів | Пауза між HIGH/LOW одного плеча моста проти наскрізного струму | [Потужність/Рух](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md) |
| StallGuard | Детектор заклинювання | Фішка TMC2209/5160: зупинка без кінцевика по зворотній ЕРС | [Приводи](../../../ESP32-Reference/11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.md) |
| RVC | Робот-пилосос (режим BNO08x) | Robot Vacuum Cleaner UART-режим BNO08x: кватерніони готовим потоком | [IMU](../../../ESP32-Reference/10-Sensori/19-IMU-6-9DOF.md) |

## Цифрові шини

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| I2C | Двопровідна шина | SDA/SCL, 100/400 кГц, pull-up 4.7к до 3.3V | [Шаблон](../../../ESP32-Reference/_templates/Component-Template.md) |
| SPI | Швидка послідовна шина | MOSI/MISO/SCK/CS, до 80 МГц, для дисплеїв/Flash | [Шаблон](../../../ESP32-Reference/_templates/Component-Template.md) |
| UART | Асинхронний приймач-передавач | TX/RX, 3.3V, UART0 - консоль; не плутати з RS232 ±12V! | [Старт](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md) |
| JTAG | Налагоджувальний інтерфейс | TDI/TDO/TCK/TMS, OpenOCD, для ESP-IDF | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| RMT | Модулятор імпульсів | Точні імпульси для WS2812, ІЧ, DHT | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| TWAI | CAN-контролер (Two-Wire Auto Interface) | CAN 2.0, потрібен трансивер 3.3V (TJA1050) | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| I2S | Аудіошина | Мікрофони INMP441, ЦАП MAX98357A | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| 1-Wire | Однопровідний інтерфейс | DS18B20, pull-up 4.7к до 3.3V, не 5V! | [Шаблон](../../../ESP32-Reference/_templates/Component-Template.md) |
| USB-OTG / CDC | USB | S3/C3/H2: native USB; Classic - тільки через CP2102/CH340 | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| CP2102 / CH340 | USB-UART міст | Перетворює USB в UART 3.3V для прошивки | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |

## Радіо та мережа

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| STA | Wi-Fi клієнт | Підключення до роутера | [Home](../../../ESP32-Reference/Home.md) |
| AP | Точка доступу | ESP32 роздає Wi-Fi ( captive portal) | [Home](../../../ESP32-Reference/Home.md) |
| BLE | Bluetooth Low Energy | 4.2/5.0, датчики, provision | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| BT Classic | Класичний Bluetooth | Тільки ESP32-Classic (SPP/A2DP) | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Zigbee / Thread | Mesh-радіо | ESP32-H2/C6, 802.15.4 | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| ESP-NOW | Безпосередній радіопротокол | P2P без роутера, низька затримка | [Home](../../../ESP32-Reference/Home.md) |
| OTA | Оновлення по повітрю | Два OTA-слоти, відкат при збої | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Provisioning | Первинне налаштування Wi-Fi | BLE / SoftAP + HTTP | [Home](../../../ESP32-Reference/Home.md) |
| RSSI | Рівень сигналу | дБм, -30 відмінно, -90 межа | [Home](../../../ESP32-Reference/Home.md) |
| LWT | Заповіт останньої волі | MQTT-повідомлення `offline`, що брокер шле при обриві вузла | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| QoS | Рівень гарантії доставки | MQTT 0 (без гарантій) / 1 (хоча б раз) / 2 (рівно раз) | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Retain | Збережене повідомлення | Брокер тримає останнє для нових підписників; тільки state/config | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Keepalive | Інтервал живості | MQTT PINGREQ кожні 15-60 с, ловить обрив | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| GATT | Профіль атрибутів BLE | Сервіси/характеристики/дескриптори, операції read/write/notify | [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| MTU | Розмір пакета BLE | 23 байти за замовчуванням, до 517 після exchange | [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| Bonding | Зв'язування BLE | Збереження ключів шифрування, passkey JustWorks | [BLE](../../../ESP32-Reference/05-Radio/02-BLE-Bluetooth.md) |
| RainMaker | Хмара Espressif | Provisioning + MQTT + OTA + голосові асистенти з коробки | [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) |
| BluFi | Налаштування по BLE | Протокол Espressif: SSID/пароль через BLE-канал protocomm | [Provisioning](../../../ESP32-Reference/15-Protokoli/04-Provisioning.md) |
| Matter | Стандарт розумного дому | IP-протокол поверх Thread/WiFi, комісія через BLE | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| Thread | Mesh 802.15.4 | IPv6-сітка для H2/C6, border-router на WiFi | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| mDNS | Локальні імена | `esp32.local` в одній підмережі, сервіси _http._tcp | [mDNS/NTP/TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) |
| SNTP | Синхронізація часу | UDP 123, UTC + TZ Europe/Kyiv, обов'язково перед TLS | [mDNS/NTP/TLS](../../../ESP32-Reference/15-Protokoli/03-mDNS-NTP-TLS.md) |
| SSE | Події сервера | Односторонній текстовий потік `/events` для телеметрії в браузер | [HTTP](../../../ESP32-Reference/15-Protokoli/02-HTTP-WebSocket.md) |
| Backoff | Експоненційна пауза | Перепідключення 1/2/4/8 с проти шторму реконектів | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Broker | Сервер повідомлень | Mosquitto: приймає PUBLISH, роздає SUB за топіками | [MQTT](../../../ESP32-Reference/15-Protokoli/01-MQTT.md) |
| Gateway | Шлюз протоколів | Міст LoRa↔MQTT, Modbus↔WiFi, BLE↔хмара | [Cloud](../../../ESP32-Reference/15-Protokoli/05-Cloud-Pipeline.md) |

## Пам'ять та прошивка

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| Flash | Флеш-пам'ять програми | 4-16 МБ зовн. SPI-Flash | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| PSRAM | Зовнішня ОЗП | 2-8 МБ (WROVER), для камер/дисплеїв | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| SRAM | Внутрішня ОЗП | 320-512 КБ залежно від чипа | [Чипи](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md) |
| NVS | Енергонезалежна пам'ять | Ключ-значення у Flash (Wi-Fi, калібрування) | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Partitions | Таблиця розділів | NVS/OTA/app/SPIFFS/LittleFS | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Bootloader | Завантажувач | 2nd-stage, вибір app, download-режим | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| esptool | Утиліта прошивки | `esptool.py --chip esp32 write_flash` | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Download mode | Режим прошивки | GPIO0=LOW + reset, швидкість 921600/460800 | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| LittleFS / SPIFFS | Файлові системи | LittleFS - сучасна, SPIFFS - застаріла | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Core dump | Знімок аварії | Для аналізу panic через ESP-IDF | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| OTA-rollback | Відкат прошивки | Повернення на минулий OTA-слот, якщо новий не mark_valid | [OTA](../../../ESP32-Reference/08-Pamyat/03-OTA.md) |
| Octal PSRAM | Швидка зовнішня ОЗП | 8-бітна шина OPI 120 МГц для LVGL/камер на S3 | [Flash/PSRAM](../../../ESP32-Reference/01-Hardware/06-Flash-PSRAM.md) |

## Середовища та інструменти

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| ESP-IDF | Офіційний фреймворк Espressif | C/C++, FreeRTOS, повний контроль | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Arduino-core | Ядро Arduino для ESP32 | `setup()/loop()`, швидкий старт | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| MicroPython | Python для мікроконтролерів | REPL, швидкі прототипи, повільніше | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| PlatformIO | Система збірки | VS Code, зручні бібліотеки, CI | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| FreeRTOS | ОС реального часу | Задачі, черги, семафори; dual-core | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| OpenOCD | Налагоджувач | GDB + JTAG | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Dataview | Плагін Obsidian | SQL-подібні запити по нотах | [Старт](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md) |
| MOC | Карта контенту | [Home](../../../ESP32-Reference/Home.md) - центральний MOC | [Home](../../../ESP32-Reference/Home.md) |
| WROOM / WROVER | Модулі Espressif | WROOM - без PSRAM, WROVER - з PSRAM | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| DevKit | Налагоджувальна плата | Модуль + USB-UART + LDO + кнопки | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| HMI | Людино-машинний інтерфейс | Nextion/DWIN-дисплеї, кнопки, енкодери для керування | [Звук/HMI](../../../ESP32-Reference/11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004.md) |
| InfluxDB | База часових рядів | Зберігає телеметрію MQTT для Grafana-графіків | [Cloud](../../../ESP32-Reference/15-Protokoli/05-Cloud-Pipeline.md) |
| Pull-up/down | Підтяжка | Внутрішні ~45к слабкі; для I2C - зовн. 4.7к | [Шаблон](../../../ESP32-Reference/_templates/Component-Template.md) |
| Watchdog (WDT) | Сторожовий таймер | Reset при зависанні; годувати в `loop()` | [Середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md) |
| Brownout | Просідання живлення | Reset при VDD < 2.43V; конденсатор 470 мкФ | [DevKit](../../../ESP32-Reference/00-Start/04-Devkit-plati.md) |
| Dropout (LDO) | Падіння на стабілізаторі | Різниця Vin−Vout для стабілізації: AMS1117 ~1.1V, ME6211 ~0.3V | [Захист](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect.md) |
| MPPT | Відбір максимуму потужності сонця | CN3791 тримає панель у точці Pmax, заряд CC/CV | [Buck/Solar](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar.md) |
| BMS | Плата захисту батареї | DW01+FS8205: відсікання по перезаряду/перерозряду/струму | [Заряд/BMS](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/03-TP4056-IP5306-BMS-UPS.md) |
| PTC | Самовідновлюваний запобіжник | Полімерний: росте опір при перегріві струмом | [Захист](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect.md) |
| TVS | Супресор перенапруги | SMBJ5.0A гасить ESD/сплески наносекунди | [Захист](../../../ESP32-Reference/13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect.md) |

> [!example] Фото/схема: ![](../../../ESP32-Reference/assets/img/placeholder.png)
> Опорна схема рівнів для глосарію:

| ESP32 | Модуль 3.3V | Модуль 5V |
| --- | --- | --- |
| 3V3 | VCC | - (не підключати сигнали!) |
| GND | GND | GND (спільна) |
| GPIO (3.3V) | SDA/SCL/TX/RX безпосередньо | Тільки через level-shifter |
| 5V (VIN) | - | VCC живлення 5V |
| EN/BOOT | - | Кнопки для прошивки |

## Див. також

- [Головна карта](../../../ESP32-Reference/Home.md)
- [Як користуватись](../../../ESP32-Reference/00-Start/01-Yak-koristuvatis-dovidnikom.md)
- [Порівняння чипів](../../../ESP32-Reference/00-Start/03-Porivnyannya-chipiv.md)
- [DevKit плати](../../../ESP32-Reference/00-Start/04-Devkit-plati.md)
- [Вибір середовища](../../../ESP32-Reference/00-Start/05-Vibir-seredovischa.md)
- [Шаблон компонента](../../../ESP32-Reference/_templates/Component-Template.md)
