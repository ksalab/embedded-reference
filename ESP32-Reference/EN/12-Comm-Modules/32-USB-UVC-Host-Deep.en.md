---
title: ESP32 USB-OTG and UVC-Host - глибока практика
description: how використати ESP32 how USB-host (UVC-камери, HID, MSC, CDC), розрізняючи FS/HS, OTG-режими та обмеження per чипу.; shows schematics, code and tables.
tags: [esp32, usb, otg, uvc, host, usb-c]
category: Moduli-zvyazku
date-created: 2026-10-07
date: 2026-10-07
---

# ESP32 USB-OTG and UVC-Host - глибока практика

![[assets/img/esp32-usb-host-deep-scheme.png|600]]
*Fig. ESP32 how USB-Host: OTG-ID пін визначає роль, UVC-камери via UVC-стек, HID-клавіатури via HID-клас.*

> [!tip] Призначення ноти
> Розібрати, which ESP32-чу може бути USB-host, якої швидкості (FS/HS), with якими класами (UVC/UAC/HID/MSC/CDC) and чому not всі чипи однаково.

## 1. which чип that вміє

| Чип | USB | Швидкість | Отримання | Host | Примітка |
| --- | --- | --- | --- | --- | --- |
| ESP32 | USB-OTG FS | Full-Speed (12 Мб/с) | Так | Так | Переривання + polling |
| ESP32-S2 | USB-OTG FS | Full-Speed | Так | Так | Видалено UVC with SDK 5.2 |
| ESP32-S3 | USB-OTG HS + FS | High-Speed (480 Мб/с) | Так | Так | UVC/VCP/MSC/HID |
| ESP32-C3 | USB-OTG FS | Full-Speed | Так | Так | Неможливий UVC-стек |
| ESP32-C6 | USB-OTG FS | Full-Speed | Так | Ні (device) | Host обмежений |
| ESP32-P4 | USB-OTG HS + FS | High-Speed | Так | Так | Native USB-Host, Ethernet |

- **Full-Speed (12 Мб/с)** — достатньо for HID, CDC, MSC (флешки); for UVC-камери — мінімум, але працює (720p @ 30 FPS via компресію).
- **High-Speed (480 Мб/с)** — for 1080p UVC, аудіо-інтерфейсів, швидких MSC.

```mermaid
graph LR
    ESP32-S3 -->|GPIO19 OTG-ID=GND| USB_HOST
    ESP32-S3 -->|GPIO19 float| USB_DEV
    USB_HOST -->|5V 500mA| CAM[UVC Camera]
    USB_HOST -->|FS/HS| HID[Keyboard/Mouse]
    USB_HOST -->|FS| MSC[Flash drive]
    USB_DEV -->|USB-C| PC
```

## 2. Роль via OTG-ID

- `GPIO19` (on ESP32-S3) — `OTG_ID`; якщо підключено `GND` → Host; якщо `VCC/плаває` → Device;
- `GPIO20` / `GPIO21` — `USB_D-` / `USB_D+` (HS via внутрішні PHY);
- for Host-режиму: пін живлення USB (`5V`) має давати `500 мА` (зовнішній БЖ або хаб); плата not живить with `3.3V` регулятора.

## 3. UVC-Host практика (ESP32-S3 / P4)

```c
#include "esp_camera.h"
#include <usb/usb_host.h>

void app_main(void) {
    usb_host_config_t config = { .skip_phy_setup = false, .intr_flags = ESP_INTR_FLAG_LOWMED };
    ESP_ERROR_CHECK(usb_host_install(&config));
    // UVC-стек підключається через usb_host_client_handle_t
    // камера розпізнається по PID/VID
    ESP_LOGI("UVC", "Host ready: %d devices found", usb_host_device_addr_list(0));
}
```

- **Обмеження**: UVC-потік вимагає `USB-Host` + `USB-Stream` (stack with SDK, not Base); on S2 видалено in 5.2 — перевіряйте версію SDK.
- **Пам'ять**: кожен UVC-камерний потік займає ~200-400 КБ буфера (720p @ MJPEG); on 512 КБ SRAM — лише 1 камера without іншого.
- **Живлення**: 5V 500 мА on порт; якщо камера with підсвічуванням — додавайте зовнішній БЖ.

## 4. HID-Host (клавіатура/миша)

```python
from machine import USB
from usb_hid import HIDServer
# MicroPython / CircuitPython для HID-Host обмежено;
# C SDK через usb_host_client для HID-report
```

- HID-Host працює on FS (ESP32, S2, S3, C3); not вимагає HS.
- Підключення via `USB-HID` клас; зчитування report via callback.

## 5. MSC / CDC-Host

- MSC — зчитування флешок via `FATFS` + `USB-Host` (ESP32-S3/P4);
- CDC — серійний порт via USB-кабель (PC ↔ ESP32) — this Device, not Host.

## 6. typical errors

| Symptom | Cause | Лікування |
| --- | --- | --- |
| `No device found` on Host | OTG-ID not підключений / пін wrong | Перевірте `GPIO19` on `GND`; перевірте `USB_D+/D-` |
| UVC not розпізнає камеру | SDK-версія або not UVC-клас | Оновіть до 5.2+; перевірте PID/VID (лог via `usb_host_printf`) |
| Перезавантаження at USB-ті | Недостатній БЖ (`5V < 4.8V`) | Окремий БЖ `5V 2A+`; not живити with `VIN` плати |
| MSC not бачить флешку | Формат NTFS / exFAT / більший розділ | Форматувати FAT32; розмір < 32 ГБ |
| `Task watchdog` після USB | Buffer overflow on UVC-потоці | Зменшіть роздільність (480p) / зменшіть FPS |

## 2.1 Частоти та протоколи

- Full-Speed USB 2.0 = 12 Мбіт/с; достатньо for HID (клавіатура 8 байт/запит, 125 Гц) та MSC (флешка до 32 ГБ FAT32).
- High-Speed USB 2.0 = 480 Мбіт/с; необхідний for UVC 720p MJPEG (~6 Мб/с потік) та аудіо 48 кГц stereo.
- ESP32-S3 має вбудований HS PHY; ESP32 (Classic) — лише FS.
- Device-режим (CDC/MSC) працює on всіх; Host — потребує 5V-source > 500 мА.

## 2.2 Живлення USB-Host

- Порт USB on ESP32-платі not дає 5V on вихід — зовнішній хаб/БЖ обов’язковий.
- for UVC-камери with підсвічуванням: рахувати 5V × 0.5 but (камера) + 0.2 but (стабілізатор PWM) = 3.5 Вт + запас = БЖ 5A.
- for HID (миша) — 500 мА достатньо; HID not вимагає HS.
- for MSC — флешка до 32 ГБ FAT32; NTFS/exFAT not підтримуються without додаткового стека.

## 2.3 code UVC-потоку (ESP-IDF 5.2+)

```cpp
#include "esp_camera.h"
#include <usb/usb_host.h>
void app_main() {
    usb_host_config_t cfg = { .skip_phy_setup = false, .intr_flags = ESP_INTR_FLAG_LOWMED };
    ESP_ERROR_CHECK(usb_host_install(&cfg));
    // UVC-class розпізнається автоматично за PID/VID
    ESP_LOGI("UVC", "Host active; FS/HS detected");
}
```

> [!warning] in SDK 5.2 UVC-стек видалено with базового бандла — перевіряйте `component.mk` on наявність `usb_stream`.

## See also

- [[12-Comm-Modules/32-USB-UVC-Host-Deep | USB-UVC-Host глибоко]] - глибша схема UVC-потоку;
- [[04-Interfaces/06-USB-OTG-JTAG | USB-OTG-JTAG]] - OTG + JTAG on ESP32;
- [[01-Hardware/09-ESP32-C2-P4 | C2/P4]] - P4 with HS + Ethernet.

## Official sources

- [ESP-IDF USB-Host (Espressif)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/usb/usb_host.html) - Host-стек, класів.
- [USB-OTG for ESP32-S3 (Espressif)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/usb/otg.html) - HS + FS, OTG-ID.
- [UVC specs (USB-IF)](https://www.usb.org/document-library/video-class-v11-specification) - клас UVC.
- [ESP32-S3 Datasheet (Espressif)](https://www.espressif.com/sites/default/files/esp32-s3_datasheet_en.pdf) - USB-OTG, DMA, UART.

## 7. Живлення USB-Host

- Розрахунок сумарного струму: 500 мА (камера) + 100 мА (PWM-кулер) + 50 мА (контролер) = 650 мА мінімум;
- БЖ with PD-протоколом (5 in / 5 but = 27 Вт) дає запас for піків at startі USB;
- якщо БЖ дає лише 3 but - обмежитись однією камерою + HID, without MSC;
- diagnostics: `usb_host_printf(USB_HOST_LOG_LEVEL_DEBUG)` показує енумерацію пристроїв.

> [!warning] USB-Host without зовнішнього БЖ on 2 but - гарантоване просідання 5V and скидання ESP32 під навантаженням.

## 10. Завершення

- USB-Host on ESP32-S3/P4: FS/HS, UVC/HID/MSC; OTG-ID керує роллю; 5V 500 мА мінімум; SDK 5.2+ перевіряти наявність UVC.
- BOOTSEL and прошивка not залежать from USB-ролі: UF2 заливається in обох режимах.
- Перший тест Host: HID-миша (дешево, FS, видно одразу in логах).
- UVC-камера: починати with 480p MJPEG, потім піднімати роздільність.
