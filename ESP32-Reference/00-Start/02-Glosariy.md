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

EN version: `00-Start/02-Glosariy.en.md`

> [!tip] Як користуватись
> Таблиця відсортована за темами. Колонка «Посилання» веде до розділів довідника: старт - [[00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись]], чипи - [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]], плати - [[00-Start/04-Devkit-plati|DevKit плати]], SDK - [[00-Start/05-Vibir-seredovischa|Вибір середовища]], структура датчика - [[_templates/Component-Template|Шаблон компонента]], огляд - [[Home|Home]].
>
> [!warning] Напруги в термінах
> Де б не зустрічались TTL, VCC, HIGH - для ESP32 HIGH = 3.3V. 5V TTL (як в Arduino Uno) **несумісний** з GPIO без узгодження. Vin 5V - це лише вхід LDO, не рівень логіки.

## Базові поняття та живлення

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| GPIO | Лінія вводу-виводу загального призначення | Програмований цифровий пін, 3.3V, max ~12 мА (реком. ≤6 мА) | [[00-Start/01-Yak-koristuvatis-dovidnikom | Старт]] |
| VCC / VDD | Живлення | Для кристала - 3.3V; 5V - лише на VIN/USB до LDO | [[00-Start/04-Devkit-plati | DevKit]] |
| GND | Земля | Спільна точка, обов'язкова між усіма модулями | [[_templates/Component-Template | Шаблон]] |
| LDO | Лінійний стабілізатор | AMS1117/ME6211: 5V→3.3V, гріється, ~500 мА max | [[00-Start/04-Devkit-plati | DevKit]] |
| Level-shifter | Узгоджувач рівнів | TXS0108E, BSS138, дільник 1k/2k для 5V↔3.3V | [[_templates/Component-Template | Шаблон]] |
| Strapping pins | Піни конфігурації завантаження | GPIO0/2/5/12/15: рівні при reset визначають boot/flash | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| EN (CHIP_PU) | Увімкнення кристала | HIGH=робота, кнопка EN = reset | [[00-Start/04-Devkit-plati | DevKit]] |
| BOOT (GPIO0) | Режим завантаження | Утримувати при reset для download-режиму | [[00-Start/04-Devkit-plati | DevKit]] |
| eFuse | Одноразово програмована пам'ять | Калібрування ADC, ключі flash-шифрування, USB VID | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| Deep-sleep | Глибокий сон | 5-10 мкА, працює ULP/RTC, пробудження по таймеру/touch | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| ULP | Ультра-низькоспоживчий співпроцесор | RISC-V/FSM для опитування датчиків у сні | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |

## Аналогова периферія

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| ADC | Аналого-цифровий перетворювач | 12-біт, 0-3.3V (через атенюацію), нелінійний по краях | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| ADC attenuation | Атенюація АЦП | 0/2.5/6/11 дБ: діапазони до ~1.1/1.5/2.2/3.3V | [[Home | Home]] |
| DAC | Цифро-аналоговий перетворювач | 8-біт, GPIO25/26, тільки класичний ESP32 | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| PWM / LEDC | ШІМ | LEDC до 40 МГц (теоретичний максимум; практично - герци/кілогерци), 1-16 біт; для LED, серво (50 Гц) | [[00-Start/02-Glosariy | Глосарій (цей файл)]] |
| MCPWM | ШІМ для двигунів | Апаратний ШІМ з dead-time для BLDC/H-мостів | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| Touch sensor | Ємнісний сенсор | T0-T9, пробудження з deep-sleep дотиком | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| Hall sensor | Датчик Холла | Вбудований в ESP32-Classic, грубий, для демо | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| Vref | Опорна напруга АЦП | ~1.1V внутр., розкид між чипами, потрібна калібрування | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| SAR-ADC | АЦП послідовного наближення | Тип АЦП ESP32: 12-біт, швидкий, нелінійний по краях шкали | [[06-Analog/01-ADC | ADC]] |
| FOC | Векторне керування мотором | Field-Oriented Control: 3-фазний міст + енкодер кута, тихий момент | [[11-Vivid/11-PowerMotion-2 | Потужність/Рух]] |
| Deadtime | Мертвий час ключів | Пауза між HIGH/LOW одного плеча моста проти наскрізного струму | [[11-Vivid/11-PowerMotion-2 | Потужність/Рух]] |
| StallGuard | Детектор заклинювання | Фішка TMC2209/5160: зупинка без кінцевика по зворотній ЕРС | [[11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209 | Приводи]] |
| RVC | Робот-пилосос (режим BNO08x) | Robot Vacuum Cleaner UART-режим BNO08x: кватерніони готовим потоком | [[10-Sensori/19-IMU-6-9DOF | IMU]] |

## Цифрові шини

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| I2C | Двопровідна шина | SDA/SCL, 100/400 кГц, pull-up 4.7к до 3.3V | [[_templates/Component-Template | Шаблон]] |
| SPI | Швидка послідовна шина | MOSI/MISO/SCK/CS, до 80 МГц, для дисплеїв/Flash | [[_templates/Component-Template | Шаблон]] |
| UART | Асинхронний приймач-передавач | TX/RX, 3.3V, UART0 - консоль; не плутати з RS232 ±12V! | [[00-Start/01-Yak-koristuvatis-dovidnikom | Старт]] |
| JTAG | Налагоджувальний інтерфейс | TDI/TDO/TCK/TMS, OpenOCD, для ESP-IDF | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| RMT | Модулятор імпульсів | Точні імпульси для WS2812, ІЧ, DHT | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| TWAI | CAN-контролер (Two-Wire Auto Interface) | CAN 2.0, потрібен трансивер 3.3V (TJA1050) | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| I2S | Аудіошина | Мікрофони INMP441, ЦАП MAX98357A | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| 1-Wire | Однопровідний інтерфейс | DS18B20, pull-up 4.7к до 3.3V, не 5V! | [[_templates/Component-Template | Шаблон]] |
| USB-OTG / CDC | USB | S3/C3/H2: native USB; Classic - тільки через CP2102/CH340 | [[00-Start/04-Devkit-plati | DevKit]] |
| CP2102 / CH340 | USB-UART міст | Перетворює USB в UART 3.3V для прошивки | [[00-Start/04-Devkit-plati | DevKit]] |

## Радіо та мережа

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| STA | Wi-Fi клієнт | Підключення до роутера | [[Home | Home]] |
| AP | Точка доступу | ESP32 роздає Wi-Fi ( captive portal) | [[Home | Home]] |
| BLE | Bluetooth Low Energy | 4.2/5.0, датчики, provision | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| BT Classic | Класичний Bluetooth | Тільки ESP32-Classic (SPP/A2DP) | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| Zigbee / Thread | Mesh-радіо | ESP32-H2/C6, 802.15.4 | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| ESP-NOW | Безпосередній радіопротокол | P2P без роутера, низька затримка | [[Home | Home]] |
| OTA | Оновлення по повітрю | Два OTA-слоти, відкат при збої | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Provisioning | Первинне налаштування Wi-Fi | BLE / SoftAP + HTTP | [[Home | Home]] |
| RSSI | Рівень сигналу | дБм, -30 відмінно, -90 межа | [[Home | Home]] |
| LWT | Заповіт останньої волі | MQTT-повідомлення `offline`, що брокер шле при обриві вузла | [[15-Protokoli/01-MQTT | MQTT]] |
| QoS | Рівень гарантії доставки | MQTT 0 (без гарантій) / 1 (хоча б раз) / 2 (рівно раз) | [[15-Protokoli/01-MQTT | MQTT]] |
| Retain | Збережене повідомлення | Брокер тримає останнє для нових підписників; тільки state/config | [[15-Protokoli/01-MQTT | MQTT]] |
| Keepalive | Інтервал живості | MQTT PINGREQ кожні 15-60 с, ловить обрив | [[15-Protokoli/01-MQTT | MQTT]] |
| GATT | Профіль атрибутів BLE | Сервіси/характеристики/дескриптори, операції read/write/notify | [[05-Radio/02-BLE-Bluetooth | BLE]] |
| MTU | Розмір пакета BLE | 23 байти за замовчуванням, до 517 після exchange | [[05-Radio/02-BLE-Bluetooth | BLE]] |
| Bonding | Зв'язування BLE | Збереження ключів шифрування, passkey JustWorks | [[05-Radio/02-BLE-Bluetooth | BLE]] |
| RainMaker | Хмара Espressif | Provisioning + MQTT + OTA + голосові асистенти з коробки | [[15-Protokoli/04-Provisioning | Provisioning]] |
| BluFi | Налаштування по BLE | Протокол Espressif: SSID/пароль через BLE-канал protocomm | [[15-Protokoli/04-Provisioning | Provisioning]] |
| Matter | Стандарт розумного дому | IP-протокол поверх Thread/WiFi, комісія через BLE | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| Thread | Mesh 802.15.4 | IPv6-сітка для H2/C6, border-router на WiFi | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| mDNS | Локальні імена | `esp32.local` в одній підмережі, сервіси _http._tcp | [[15-Protokoli/03-mDNS-NTP-TLS | mDNS/NTP/TLS]] |
| SNTP | Синхронізація часу | UDP 123, UTC + TZ Europe/Kyiv, обов'язково перед TLS | [[15-Protokoli/03-mDNS-NTP-TLS | mDNS/NTP/TLS]] |
| SSE | Події сервера | Односторонній текстовий потік `/events` для телеметрії в браузер | [[15-Protokoli/02-HTTP-WebSocket | HTTP]] |
| Backoff | Експоненційна пауза | Перепідключення 1/2/4/8 с проти шторму реконектів | [[15-Protokoli/01-MQTT | MQTT]] |
| Broker | Сервер повідомлень | Mosquitto: приймає PUBLISH, роздає SUB за топіками | [[15-Protokoli/01-MQTT | MQTT]] |
| Gateway | Шлюз протоколів | Міст LoRa↔MQTT, Modbus↔WiFi, BLE↔хмара | [[15-Protokoli/05-Cloud-Pipeline | Cloud]] |

## Пам'ять та прошивка

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| Flash | Флеш-пам'ять програми | 4-16 МБ зовн. SPI-Flash | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| PSRAM | Зовнішня ОЗП | 2-8 МБ (WROVER), для камер/дисплеїв | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| SRAM | Внутрішня ОЗП | 320-512 КБ залежно від чипа | [[00-Start/03-Porivnyannya-chipiv | Чипи]] |
| NVS | Енергонезалежна пам'ять | Ключ-значення у Flash (Wi-Fi, калібрування) | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Partitions | Таблиця розділів | NVS/OTA/app/SPIFFS/LittleFS | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Bootloader | Завантажувач | 2nd-stage, вибір app, download-режим | [[00-Start/04-Devkit-plati | DevKit]] |
| esptool | Утиліта прошивки | `esptool.py --chip esp32 write_flash` | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Download mode | Режим прошивки | GPIO0=LOW + reset, швидкість 921600/460800 | [[00-Start/04-Devkit-plati | DevKit]] |
| LittleFS / SPIFFS | Файлові системи | LittleFS - сучасна, SPIFFS - застаріла | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Core dump | Знімок аварії | Для аналізу panic через ESP-IDF | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| OTA-rollback | Відкат прошивки | Повернення на минулий OTA-слот, якщо новий не mark_valid | [[08-Pamyat/03-OTA | OTA]] |
| Octal PSRAM | Швидка зовнішня ОЗП | 8-бітна шина OPI 120 МГц для LVGL/камер на S3 | [[01-Hardware/06-Flash-PSRAM | Flash/PSRAM]] |

## Середовища та інструменти

| Термін | Переклад | Пояснення | Посилання |
| --- | --- | --- | --- |
| ESP-IDF | Офіційний фреймворк Espressif | C/C++, FreeRTOS, повний контроль | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Arduino-core | Ядро Arduino для ESP32 | `setup()/loop()`, швидкий старт | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| MicroPython | Python для мікроконтролерів | REPL, швидкі прототипи, повільніше | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| PlatformIO | Система збірки | VS Code, зручні бібліотеки, CI | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| FreeRTOS | ОС реального часу | Задачі, черги, семафори; dual-core | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| OpenOCD | Налагоджувач | GDB + JTAG | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Dataview | Плагін Obsidian | SQL-подібні запити по нотах | [[00-Start/01-Yak-koristuvatis-dovidnikom | Старт]] |
| MOC | Карта контенту | [[Home | Home]] - центральний MOC | [[Home | Home]] |
| WROOM / WROVER | Модулі Espressif | WROOM - без PSRAM, WROVER - з PSRAM | [[00-Start/04-Devkit-plati | DevKit]] |
| DevKit | Налагоджувальна плата | Модуль + USB-UART + LDO + кнопки | [[00-Start/04-Devkit-plati | DevKit]] |
| HMI | Людино-машинний інтерфейс | Nextion/DWIN-дисплеї, кнопки, енкодери для керування | [[11-Vivid/08-DFPlayer-MAX98357-Nextion-LCD2004 | Звук/HMI]] |
| InfluxDB | База часових рядів | Зберігає телеметрію MQTT для Grafana-графіків | [[15-Protokoli/05-Cloud-Pipeline | Cloud]] |
| Pull-up/down | Підтяжка | Внутрішні ~45к слабкі; для I2C - зовн. 4.7к | [[_templates/Component-Template | Шаблон]] |
| Watchdog (WDT) | Сторожовий таймер | Reset при зависанні; годувати в `loop()` | [[00-Start/05-Vibir-seredovischa | Середовища]] |
| Brownout | Просідання живлення | Reset при VDD < 2.43V; конденсатор 470 мкФ | [[00-Start/04-Devkit-plati | DevKit]] |
| Dropout (LDO) | Падіння на стабілізаторі | Різниця Vin−Vout для стабілізації: AMS1117 ~1.1V, ME6211 ~0.3V | [[13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect | Захист]] |
| MPPT | Відбір максимуму потужності сонця | CN3791 тримає панель у точці Pmax, заряд CC/CV | [[13-Moduli-zhivlennya-rivniv/01-Buck-Boost-Solar | Buck/Solar]] |
| BMS | Плата захисту батареї | DW01+FS8205: відсікання по перезаряду/перерозряду/струму | [[13-Moduli-zhivlennya-rivniv/03-TP4056-IP5306-BMS-UPS | Заряд/BMS]] |
| PTC | Самовідновлюваний запобіжник | Полімерний: росте опір при перегріві струмом | [[13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect | Захист]] |
| TVS | Супресор перенапруги | SMBJ5.0A гасить ESD/сплески наносекунди | [[13-Moduli-zhivlennya-rivniv/04-LDO-Buck-XL4015-Protect | Захист]] |

> [!example] Фото/схема: ![[assets/img/placeholder.png]]
> Опорна схема рівнів для глосарію:

| ESP32 | Модуль 3.3V | Модуль 5V |
| --- | --- | --- |
| 3V3 | VCC | - (не підключати сигнали!) |
| GND | GND | GND (спільна) |
| GPIO (3.3V) | SDA/SCL/TX/RX безпосередньо | Тільки через level-shifter |
| 5V (VIN) | - | VCC живлення 5V |
| EN/BOOT | - | Кнопки для прошивки |

## Див. також

- [[Home|Головна карта]]
- [[00-Start/01-Yak-koristuvatis-dovidnikom|Як користуватись]]
- [[00-Start/03-Porivnyannya-chipiv|Порівняння чипів]]
- [[00-Start/04-Devkit-plati|DevKit плати]]
- [[00-Start/05-Vibir-seredovischa|Вибір середовища]]
- [[_templates/Component-Template|Шаблон компонента]]
