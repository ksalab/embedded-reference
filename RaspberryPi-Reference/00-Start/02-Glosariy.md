---
title: Глосарій Raspberry Pi - SoC, GPIO, HAT, CSI, PIO і всі терміни бази
description: Збирає всі терміни довідника в одному місці - SoC і моделі, GPIO і HAT, камери, живлення та скорочення.
tags: [raspberrypi, start, glossary, terms, soc, gpio, hat]
category: Start
date: 2026-10-06
---

# Глосарій Raspberry Pi - SoC, GPIO, HAT, CSI, PIO і всі терміни бази

EN version: `00-Start/02-Glosariy.en.md`

![[assets/img/rpi-glossary-scheme.png|600]]
*Рис. Карта термінів: залізо (SoC→плата→HAT), інтерфейси (GPIO→шини→CSI/DSI), софт (OS→бібліотеки→хмара).*

> [!tip] Що це за нота
> Словник бази: кожен термін - одним абзацом з прив'язкою до ноти. Читати при першій зустрічі з незнайомим словом. Вхід: [[00-Start/01-Yak-koristuvatis-dovidnikom|як користуватись]], далі: [[00-Start/03-Porivnyannya-plate|порівняння моделей]].

## 1. Мета

Дати єдині визначення, щоб ноти не розходились у термінології:

- залізо: SoC, моделі, пам'ять, живлення;
- контакти: GPIO, гребінка, HAT, шини;
- камери і дисплеї: CSI, DSI, Picamera2;
- софт: OS, Imager, EEPROM, Device Tree.

```mermaid
flowchart TB
  SOC[SoC: BCM/RP2040] --> BRD[Плата: Pi5/Zero/Pico]
  BRD --> HDR[Гребінка 40 пінів]
  HDR --> HAT[HAT-плата]
  HDR --> BUS[Шини: I2C/SPI/UART]
  BRD --> CSI[CSI-камера / DSI-дисплей]
  BRD --> OS[Raspberry Pi OS]
  OS --> LIB[gpiozero / libcamera]
  LIB --> NET[MQTT / HTTP]
```

## 2. Залізо: чипи і плати

| Термін | Значення | Нота |
| --- | --- | --- |
| SoC | кристал з CPU+GPU+пам'яттю (BCM2712, RP2040) | [[01-Hardware/01-SoC-Oglyad | огляд SoC]] |
| BCM2712 | чип Pi 5: 4×A76 2.4 ГГц, VideoCore VII | [[01-Hardware/02-BCM2712-Pi5 | BCM2712 і Pi 5]] |
| RP2040/RP2350 | мікроконтролери Pico: M0+/M33, PIO | [[01-Hardware/03-RP2040-RP2350 | RP2040 і RP2350]] |
| Pi 5/4/Zero/Pico | моделі плат різних класів | [[14-Devboards/01-Pi5-Flagman | флагман Pi 5]] |
| CM4/CM5 | Compute Module для вбудовування | [[14-Devboards/05-CM4-CM5 | модулі CM]] |
| HAT | плата на гребінку 40 пінів з EEPROM | [[12-Moduli-zvyazku/01-Sense-HAT | сенсорна Sense-плата]] |
| PoE HAT | живлення по Ethernet-кабелю | [[02-Zhivlennya/02-PoE-HAT | живлення PoE]] |

## 3. Контакти і шини

| Термін | Значення | Нота |
| --- | --- | --- |
| GPIO | пін загального призначення, 3.3V логіка | [[03-GPIO/01-Header-Gpiozero | гребінка і gpiozero]] |
| 3.3V логіка | HIGH=3.3V, 5V на вхід - смерть | [[03-GPIO/01-Header-Gpiozero | гребінка і gpiozero]] |
| I2C | двопровідна шина датчиків, 100/400 кГц | [[04-Shini/01-I2C-SPI-UART | шини I2C/SPI/UART]] |
| SPI | швидка шина дисплеїв і АЦП | [[04-Shini/01-I2C-SPI-UART | шини I2C/SPI/UART]] |
| UART | послідовний порт, консоль і модеми | шини I2C/SPI/UART |
| USB-CDC | віртуальний COM-порт Pico і програматорів | шини і USB |
| PWM | ШІМ: яскравість, серво, звук | [[03-GPIO/02-PWM-Pererivannya | ШІМ і переривання]] |
| PIO | програмовані автомати RP2040 (апаратний bit-bang) | [[01-Hardware/03-RP2040-RP2350 | RP2040 і RP2350]] |

## 4. Камери, дисплеї, звук

| Термін | Значення | Нота |
| --- | --- | --- |
| CSI | шлейф камери (не USB!) | [[10-Sensori/06-Kamera-CSI | камера CSI]] |
| DSI | шлейф дисплея | [[11-Vivid/01-DSI-HDMI-Displeyi | дисплеї DSI/HDMI]] |
| Picamera2 | бібліотека камер нового стека | [[10-Sensori/06-Kamera-CSI | камера CSI]] |
| HDMI | монітор/телевізор, звук теж | [[11-Vivid/01-DSI-HDMI-Displeyi | дисплеї DSI/HDMI]] |
| I2S | цифровий звук на ЦАП/мікрофони | [[11-Vivid/03-Audio-HAT | аудіо і HAT]] |

## 5. Живлення і пам'ять

| Термін | Значення | Нота |
| --- | --- | --- |
| USB-C PD | живлення Pi 4/5: 5V 3A/5A | [[02-Zhivlennya/01-USB-C-PD | живлення USB-C]] |
| Undervoltage | блискавка на екрані = слабкий БЖ | [[02-Zhivlennya/01-USB-C-PD | живлення USB-C]] |
| UPS HAT | безперебійник на 18650 | [[02-Zhivlennya/03-UPS-18650 | UPS-плати]] |
| SD/eMMC/NVMe | носії системи за швидкістю | [[08-Pamyat/01-SD-eMMC-NVMe | носії пам'яті]] |
| EEPROM | завантажувач Pi 4/5 на платі | [[09-Proshivka/02-EEPROM-Boot | завантаження EEPROM]] |

## 6. Софт і мережа

| Термін | Значення | Нота |
| --- | --- | --- |
| Raspberry Pi OS | офіційна ОС (Bookworm) | [[09-Proshivka/03-OS-Nalashtuvannya | налаштування ОС]] |
| Imager | прошивальник SD з коробки | [[09-Proshivka/01-Imager-Headless | прошивка Imager]] |
| Headless | без монітора, через SSH | [[09-Proshivka/01-Imager-Headless | прошивка Imager]] |
| Device Tree | опис заліза для ядра (config.txt) | [[09-Proshivka/03-OS-Nalashtuvannya | налаштування ОС]] |
| gpiozero | Python-бібліотека GPIO | [[03-GPIO/01-Header-Gpiozero | гребінка і gpiozero]] |
| MQTT | протокол телеметрії | [[15-Protokoli/01-MQTT | протокол MQTT]] |
| HAT EEPROM | мікросхема ID плати розширення | [[03-GPIO/03-HAT-EEPROM | HAT і EEPROM]] |

## 6.1 Мережеві терміни

| Термін | Значення |
| --- | --- |
| SSH | безпечна консоль по мережі, порт 22 |
| VNC/RDP | графічний стіл віддалено |
| AP/STA | точка доступу / клієнт WiFi |
| DHCP | автоматична видача IP роутером |
| mDNS | ім'я `raspberrypi.local` без запам'ятовування IP |
| I2C-адреса | 7-бітний номер пристрою на шині (сканер `i2cdetect`) |
| Baud | швидкість UART в бодах (115200 - стандарт консолі) |
| Pull-up/down | підтяжка входу до живлення/землі проти «плавання» |
| Debounce | придушення брязкоту кнопки (20-50 мс) |
| Duty cycle | шпаруватість ШІМ у відсотках |

## 7. Як читати скорочення на схемах

- `SDA/SCL` - дані/такт I2C;
- `MOSI/MISO/SCK/CS` - SPI-сигнали;
- `TXD/RXD` - UART (перехресно!);
- `5V/3V3/GND` - живлення і земля гребінки;
- `RUN` - пін скидання/запуску плати;
- `PoE` - живлення по витій парі (тільки з HAT!).

## 7.1 Одиниці і позначки на платах

- `5V`, `3V3`, `GND` - шини живлення гребінки;
- `RUN` - вхід запуску/скидання (коротнути на землю = ребут);
- `PoE` - контакти живлення по витій парі (працюють лише з PoE HAT);
- `ACT` - зелений світлодіод активності SD-карти;
- `PWR` - червоний світлодіод живлення (моргає при просадці);
- `HDMI0/HDMI1` - основний і другий виходи (перший ближче до USB-C);
- `CAM/DISP` - шлейфи камери і дисплея (ідентичні роз'єми, не плутати);
- `J2/J8` - номер гребінки на схемі (J8 - основна 40-пінова);
- `TP1/TP2` - тест-поїнти живлення для мультиметра;
- `EEPROM` - мікросхема завантажувача (Pi 4/5, оновлюється утилітою).

## 8. Типові помилки

| Симптом | Причина | Лікування |
| --- | --- | --- |
| Термін незрозумілий | пропустили глосарій | шукати слово тут, далі - в ноту з третьої колонки |
| CSI плутають з USB | обидва - «камера» | CSI - шлейф до роз'єму CAMERA, USB - в порт |
| HAT не стає | гребінка 26 пінів (старі Pi) | HAT треба 40 пінів (B+ і новіші) |
| 5V на GPIO | «а на Arduino можна» | не можна: рівень 3.3V, перетворювач рівнів обов'язковий |
| PIO плутають з PWM | обидва «апаратні» | PIO - автомати Pico, PWM - модулятор ширини |
| EEPROM Pi плутають з BIOS | інша архітектура | завантажувач у SPI-flash, оновлюється утилітою |

## 9. Суміжні ноти

- [[00-Start/01-Yak-koristuvatis-dovidnikom|як користуватись]] - маршрути читання.
- [[00-Start/03-Porivnyannya-plate|порівняння моделей]] - вибір заліза.
- [[00-Start/05-Vibir-seredovischa|вибір середовища]] - вибір софту.
- [[Home|головна карта]] - повна навігація.

## Офіційні джерела

- [Getting Started (Raspberry Pi docs)](https://www.raspberrypi.com/documentation/computers/getting-started.html) - терміни першого запуску.
- [Raspberry Pi OS (Raspberry Pi)](https://www.raspberrypi.com/software/) - редакції системи.
- [gpiozero docs (Read the Docs)](https://gpiozero.readthedocs.io/en/stable/) - словник GPIO-об'єктів.
