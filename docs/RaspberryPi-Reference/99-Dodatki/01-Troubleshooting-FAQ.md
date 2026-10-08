---
title: FAQ RaspberryPi-Reference - часті питання і швидкі відповіді
description: FAQ бази RaspberryPi - живлення, завантаження, GPIO, мережа і типові граблі з короткими відповідями.
tags: [raspberrypi, faq, troubleshooting, dodatok]
category: Dodatki
date: 2026-10-06
---

# FAQ RaspberryPi-Reference - часті питання і швидкі відповіді

## Живлення

**Блискавка на екрані - що робити?**
Міняти БЖ на офіційний під модель і короткий товстий кабель. Перевірити `vcgencmd get_throttled` - має бути `0x0`. Деталі: [живлення USB-C](../../../RaspberryPi-Reference/02-Zhivlennya/01-USB-C-PD.md).

**Який БЖ для Pi 5?**
Офіційний PD 27W (5V 5A). З БЖ 3A працює, але USB порізані до 600 мА.

**Чи можна живити через гребінку 5V?**
Так, але без захисту від переполюсовки і з якісним джерелом. USB-C - безпечніше.

## Завантаження

**ACT блимає 4 рази - що це?**
Немає `start.elf` - битий образ або карта. Перепрошити. Таблиця кодів - [завантаження EEPROM](../../../RaspberryPi-Reference/09-Proshivka/02-EEPROM-Boot.md).

**Не bootається з USB/NVMe?**
Порядок в EEPROM (`BOOT_ORDER`), свіжа прошивка завантажувача, `dtparam=pciex1` для NVMe.

**Забув пароль/немає SSH?**
Перепрошити з Imager з новим користувачем, дані з бекапу. Або монітор+клавіатура локально.

## GPIO і залізо

**Спалив пін 5 вольтами - що робити?**
Нічого, пін мертвий. Переїхати на вільний GPIO і поставити перетворювач рівнів. Деталі: [гребінка і gpiozero](../../../RaspberryPi-Reference/03-GPIO/01-Header-Gpiozero.md).

**I2C не бачить датчик?**
`i2cdetect -y 1`, перевірити SDA/SCL місцями, підтяжки, адресу SDO. Деталі: [шини](../../../RaspberryPi-Reference/04-Shini/01-I2C-SPI-UART.md).

**HAT не визначається?**
Або це шилд без EEPROM (ручний dtoverlay), або конфлікт ID-пінів. Деталі: [HAT і EEPROM](../../../RaspberryPi-Reference/03-GPIO/03-HAT-EEPROM.md).

## Мережа

**WiFi не бачить 5 ГГц?**
Не виставлена країна. `raspi-config` → WiFi-country. Деталі: [бортове радіо](../../../RaspberryPi-Reference/05-Radio/01-WiFi-BT-Bort.md).

**Пропадає мережа щогодини?**
Power management WiFi. Вимкнути PM, додати watchdog-скрипт.

**Як зайти ззовні без білого IP?**
Tailscale або WireGuard. Проброс портів - крайній захід з fail2ban.

## Софт

**`pip install` відмовляє?**
Bookworm захищає системний Python (PEP 668). Працювати у venv. Деталі: [налаштування ОС](../../../RaspberryPi-Reference/09-Proshivka/03-OS-Nalashtuvannya.md).

**Сервіс не стартує після ребута?**
`enable` забули або шляхи відносні. `systemctl status`, абсолютні шляхи, `journalctl -u`.

**Старий код з raspistill не працює?**
Стек видалено. Переписувати на Picamera2. Деталі: [камера CSI](../../../RaspberryPi-Reference/10-Sensori/06-Kamera-CSI.md).

## Де шукати далі

- Карта бази: [головна карта](../../../RaspberryPi-Reference/Home.md).
- Діагностика по симптомах: [діагностична карта](../../../RaspberryPi-Reference/99-Dodatki/03-Diagnostic-Map.md) - нота черги 4.
- Даташити: [посилання на даташити](../../../RaspberryPi-Reference/99-Dodatki/02-Datasheet-Links.md).
