---
description: Прошивка без тестів ламається мовчки: сенсорний драйвер повертає сміття, OTA цеглить партію, а `ESP_LOG` тоне в спамі. Ця нотатка показує повний контур якості: Unity-тести в ESP-IDF...
title: Тестування та CI для ESP32
tags: [esp32, testing, unity, ci, github-actions, hil, ota, logging, semver]
category: Proshivka
date-created: 2026-09-28
---

# Тестування та CI для ESP32

## Призначення

Прошивка без тестів ламається мовчки: сенсорний драйвер повертає сміття, OTA цеглить партію, а `ESP_LOG` тоне в спамі. Ця нотатка показує повний контур якості: Unity-тести в ESP-IDF через `test`-компонент, емуляція чистої логіки на хості (без плати), GitHub Actions workflow з матрицею (build + tests), HIL-стенд де друга плата виступає тестером, версіонування semver + build-metadata, стратегія OTA-гілок `stable/beta`, логування `ESP_LOG` з рівнями, і техніка golden-файлів для сенсорних драйверів. Стартове середовище - [[09-Proshivka/01-ESP-IDF-setup]], альтернативи - [[09-Proshivka/02-Arduino-PlatformIO]] та [[09-Proshivka/03-MicroPython|MicroPython]], оновлення - [[08-Pamyat/03-OTA|OTA]], нагляд - [[07-Timeri-Son/02-WDT|WDT]].

> [!NOTE]
> Піраміда тестів для ESP32: 70% - хост-тести логіки (швидко, безкоштовно), 20% - Unity на платі (драйвери, flash), 10% - HIL/ручні (OTA, радіо, живлення).

![[assets/img/testing-ci-scheme.png|600]]

## 1. Unity-тести в IDF: test-компонент

| Елемент | Де лежить | Призначення |
| --- | --- | --- |
| `components/sensor/test/CMakeLists.txt` | Поруч з компонентом | Реєстрація тестів |
| `TEST_CASE("name", "[tag]")` | `test_*.c` | Один кейс (Unity під капотом) |
| `idf.py build flash monitor` + `test` | UART-меню | Запуск на платі |
| `unity` компонент | Автоматично в `test/` | `TEST_ASSERT_EQUAL`, `TEST_ASSERT_FLOAT_WITHIN` |
| Теги `[sensor][i2c]` | Фільтр запуску | `test sensor` / `test "[i2c]"` |
| `setUp/tearDown` | Опційно | Скидання I2C-шина/мок перед кейсом |

Структура каталогу:

```text
components/bme280/
  CMakeLists.txt
  bme280.c
  include/bme280.h
  test/
    CMakeLists.txt        # idf_component_register(SRCS "test_bme280.c" REQUIRES unity bme280)
    test_bme280.c
    golden/
      bme280_temp_25C.bin # golden-файл (див. розд. 8)
```

Код ESP-IDF - `test/test_bme280.c`:

```c
#include "unity.h"
#include "bme280.h"

TEST_CASE("bme280: convert raw to celsius", "[sensor][convert]") {
    // чиста функція — можна ганяти і на хості, і на платі
    TEST_ASSERT_FLOAT_WITHIN(0.01, 25.0, bme280_compensate_temp(519888));
    TEST_ASSERT_FLOAT_WITHIN(0.01, -40.0, bme280_compensate_temp(0));
}

TEST_CASE("bme280: probe on I2C", "[sensor][i2c]") {
    TEST_ASSERT_TRUE(bme280_probe(0x76)); // потрібне залізо!
}
```

Код ESP-IDF - `test/CMakeLists.txt` мінімум:

```cmake
idf_component_register(SRCS "test_bme280.c"
                       INCLUDE_DIRS "."
                       REQUIRES unity bme280)
```

Запуск:

```bash
idf.py -p /dev/ttyUSB0 flash monitor
# в моніторі:
# > test sensor        # всі кейси компонента
# > test "[convert]"   # тільки чиста логіка
# > test --list        # список кейсів
```

> [!TIP]
> Розділяйте теги: `[convert]` (без заліза, стабільно) vs `[i2c]` (потрібна плата/стенд). CI на хості ганяє тільки `[convert]`.

Код Arduino - тести через PlatformIO + Unity:

```cpp
// test/test_sensor/test_main.cpp  (PlatformIO Unity)
#include <unity.h>
#include "bme280_convert.h"
void test_convert(void) {
  TEST_ASSERT_FLOAT_WITHIN(0.01, 25.0, bme280_compensate_temp(519888));
}
void setup() {
  UNITY_BEGIN();
  RUN_TEST(test_convert);
  UNITY_END();
}
void loop() {}
```

```ini
; platformio.ini — окреме env для тестів
[env:test_native]
platform = native
test_framework = unity
lib_deps = throwtheswitch/Unity @ ^2.5.2
```

Код MicroPython - тести без Unity, `unittest`-стиль:

```python
# tests/test_convert.py (ганяється на хості CPython!)
import sys; sys.path.insert(0, "lib")
from bme280_convert import compensate_temp
def test_temp():
    assert abs(compensate_temp(519888) - 25.0) < 0.01
    assert abs(compensate_temp(0) - (-40.0)) < 0.5
if __name__ == "__main__":
    test_temp(); print("OK")
```

## 2. Емуляція логіки на хості: відокремте чисте від залізного

| Шар | Приклад | Тест на хості? |
| --- | --- | --- |
| Чиста логіка | `compensate_temp()`, CRC, NMEA-парсер, MQTT-state machine | Так, `gcc + unity`, без плати |
| HAL-адаптер | `i2c_read_reg()` обгортка | Мок (`fake_i2c.c`), так |
| Драйвер | `bme280_probe()` → реальний I2C | Ні, тільки плата/HIL |
| Мережа | Wi-Fi/MQTT-клієнт | Мок сокетів або HIL |
| Файли/NVS | `nvs_get_u32` | Мок або `Running ESP-IDF on Host` |

> [!NOTE]
> Золоте правило: файл `*_convert.c` не інклудить `driver/i2c.h`. Тільки математика + `#include <stdint.h>`. Тоді він компілюється і на ESP32, і на ноутбуці.

Код ESP-IDF - розділення:

```c
// bme280_convert.h — чисте, без IDF-залежностей
#pragma once
#include <stdint.h>
float bme280_compensate_temp(int32_t adc_T);
// bme280_io.c — залізне, тільки для плати
#include "driver/i2c.h"
#include "bme280_convert.h"
esp_err_t bme280_read_raw(int *adc_T);
```

Хост-збірка тесту (`CMakeLists.txt` для Linux):

```cmake
cmake_minimum_required(VERSION 3.16)
project(host_tests C)
add_executable(host_tests test_host_main.c ../main/bme280_convert.c unity/unity.c)
target_include_directories(host_tests PRIVATE ../main unity)
```

```bash
gcc test_host_main.c bme280_convert.c unity/unity.c -o host_tests && ./host_tests
```

## 3. GitHub Actions: build + tests матрицею (готовий YAML)

| Джоба | Що робить | Раннер |
| --- | --- | --- |
| `host-tests` | `gcc` + Unity, golden-порівняння | `ubuntu-latest` |
| `build` (матриця) | `idf.py build` для esp32/esp32s3/esp32c3 × stable/beta | `ubuntu-latest` + docker `espressif/idf` |
| `pio-build` | Збірка Arduino-варіанта | `ubuntu-latest` |
| `mpy-check` | `mpy-cross` компіляція + `ruff`/smoke на хості | `ubuntu-latest` |
| `hil` | Тільки `workflow_dispatch` або nightly, self-hosted з платою | `self-hosted` |

```yaml
# .github/workflows/fw-ci.yml
name: fw-ci
on:
  push:
    branches: [main, beta]
  pull_request:
  workflow_dispatch:

jobs:
  host-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { submodules: recursive }
      - name: Host unit tests (gcc + Unity)
        run: |
          gcc tests/host/test_host_main.c lib/bme280_convert.c tests/unity/unity.c \
            -Ilib -Itests/unity -o /tmp/host_tests -Wall -Wextra
          /tmp/host_tests
      - name: Golden check (сенсорні вектори)
        run: python3 tests/golden/check_golden.py tests/golden/vectors.csv

  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        target: [esp32, esp32s3, esp32c3]
        branch: [stable, beta]
    container: espressif/idf:v5.3
    steps:
      - uses: actions/checkout@v4
        with: { submodules: recursive }
      - name: Select config by branch
        run: |
          if [ "${{ matrix.branch }}" = "stable" ]; then
            cp sdkconfig.defaults.stable sdkconfig.defaults
          else
            cp sdkconfig.defaults.beta sdkconfig.defaults
          fi
      - run: idf.py set-target ${{ matrix.target }}
      - run: idf.py build
      - name: Size report
        run: idf.py size
      - uses: actions/upload-artifact@v4
        with:
          name: fw-${{ matrix.target }}-${{ matrix.branch }}
          path: |
            build/*.bin
            build/*.elf
            build/flasher_args.json

  pio-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: ~/.platformio
          key: pio-${{ hashFiles('platformio.ini') }}
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install platformio
      - run: pio run -e esp32dev -e esp32s3

  mpy-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install mpy-cross ruff
      - run: mpy-cross -o /tmp/app.mpy src/app.py && ls -la /tmp/app.mpy
      - run: ruff check src/ || true
```

> [!TIP]
> Кешуйте `~/.platformio` і `~/.espressif` (або беріть docker `espressif/idf`) - інакше кожен CI проганятиме 10-хвилинну установку тулчейну.

## 4. HIL-стенд: друга плата як тестер

| Роль | Плата A (DUT) | Плата B (Tester) |
| --- | --- | --- |
| Прошивка | Кандидат-реліз | Фіксований `hil-tester` (ніколи не чіпаємо без ревью) |
| Зв'язок | UART0 → USB (логи), UART1 → Tester (команди) | Керує живленням DUT через MOSFET/реле |
| Датчики | I2C-сенсор на шині | Емулює сенсор (віддає golden-вектори по I2C-slave) |
| OTA-тест | Приймає OTA | Віддає HTTP з бінарником + рве з'єднання на 50% |
| Вердикт | - | `PASS/FAIL` по UART + GPIO `TEST_OK` |

Схема стенду:

```text
[Tester ESP32] ---UART1 115200---> [DUT ESP32]
     | TX/RX                       | UART1 (команди)
     | GPIO4 (PWR_EN) -> MOSFET -> | 3V3 живлення DUT
     | I2C-slave (addr 0x76) ----> | I2C-master (сенсор-емуляція)
     | USB (логи тестера)           | USB (логи DUT)
```

Код тестера (псевдо-ESP-IDF):

```c
// hil_tester: віддати golden-вектор замість справжнього BME280
void hil_task(void *arg) {
    hil_power_cycle_dut();          // MOSFET OFF 500мс -> ON
    hil_expect_boot_log("I (", 5000);
    hil_i2c_slave_serve(golden_vectors, N); // емуляція сенсора
    hil_send_cmd("RUN_SELFTEST");
    TEST_ASSERT(hil_expect("SELFTEST PASS", 10000));
    hil_report_pass();
}
```

> [!WARNING]
> HIL - `workflow_dispatch` + `nightly`, не на кожен push: плати глючать, USB відвалюється. Тримайте стенд за `screen`/self-hosted runner з авторебутом.

Код MicroPython для дешевого HIL-тестера:

```python
# tester.py на другій платі
from machine import Pin, UART
import time
pwr = Pin(4, Pin.OUT)
u = UART(1, baudrate=115200, tx=17, rx=16)
pwr.value(0); time.sleep(0.5); pwr.value(1)  # power-cycle DUT
time.sleep(3)
u.write(b"RUN_SELFTEST\n")
resp = u.read(128)
print("PASS" if resp and b"PASS" in resp else "FAIL")
```

## 5. Semver + build-metadata: версія прошивки як контракт OTA

| Поле | Формат | Приклад |
| --- | --- | --- |
| `MAJOR.MINOR.PATCH` | semver | `2.4.1` |
| Пре-реліз | `-beta.N` | `2.5.0-beta.2` |
| Build-metadata | `+g<sha>.<timestamp>` | `2.4.1+g a1b2c3d.20260928` |
| Джерело версії | `version.txt` / `git describe` / `PROJECT_VER` | Один файл-правда |
| Перевірка OTA | Сервер віддає `version` + `sha256` | Плата відхиляє downgrade (див. розд. 6) |

Таблиця правил:

| Зміна | Бамп | OTA-канал |
| --- | --- | --- |
| Фікс багу сенсора | PATCH `2.4.1` → `2.4.2` | `stable` |
| Новий сенсор/команда | MINOR `2.4.x` → `2.5.0-beta.1` | `beta` |
| Зміна partition table / NVS-схеми | MAJOR `2.x` → `3.0.0-beta.1` + міграція | `beta`, потім `stable` |
| Тільки логи/документація | Не бампати, build-metadata росте | Будь-який |

Код ESP-IDF - версія в `CMakeLists.txt` + `app_desc`:

```cmake
# version.txt містить "2.4.1"
file(READ "${CMAKE_SOURCE_DIR}/version.txt" PROJECT_VER)
string(STRIP "${PROJECT_VER}" PROJECT_VER)
project(my-sensor VERSION ${PROJECT_VER})
```

```c
#include "esp_app_desc.h"
#include "esp_log.h"
static const char *TAG = "ver";
void print_ver(void) {
    const esp_app_desc_t *d = esp_app_get_description();
    ESP_LOGI(TAG, "fw=%s date=%s %s idf=%s", d->version, d->date, d->time, d->idf_ver);
}
```

## 6. Стратегія OTA-гілок: stable / beta

| Гілка | Канал OTA | Хто отримує | Rollback |
| --- | --- | --- | --- |
| `main` → `stable` | `https://ota.example.com/stable/` | Усі польові пристрої | Обов'язковий `esp_ota_mark_app_valid` після самодіагностики |
| `beta` | `https://ota.example.com/beta/` | Стенди + добровольці | Дозволений downgrade до stable |
| `feature/*` | Немає OTA | Тільки USB-флеш | - |
| Тег `vX.Y.Z` | Заморожений артефакт `fw-X.Y.Z.bin` + `.sha256` | Реліз-архів | Не перезаписується ніколи |

Потік:

```text
feature/i2c-fix -> PR -> CI (host+build) -> merge beta
  -> beta OTA на стенд -> HIL PASS 24г -> тег v2.5.0
  -> merge main -> stable OTA хвилями 10% -> 50% -> 100%
```

Код ESP-IDF - вибір каналу за `sdkconfig.defaults.*`:

```ini
# sdkconfig.defaults.stable
CONFIG_OTA_URL="https://ota.example.com/stable/"
CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE=y
# sdkconfig.defaults.beta
CONFIG_OTA_URL="https://ota.example.com/beta/"
CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE=y
CONFIG_LOG_DEFAULT_LEVEL_DEBUG=y
```

> [!CAUTION]
> Ніколи не лийте `beta` на всіх: одна бита partition table без rollback = виїзд до кожного пристрою. Деталі - [[08-Pamyat/03-OTA|OTA]].

## 7. Логування ESP_LOG + рівні: логи як тестовий інтерфейс

| Рівень | Коли | Приклад |
| --- | --- | --- |
| `ESP_LOGE` | Необоротна помилка, буде reboot/rollback | `E (123) mqtt: connect failed, reboot` |
| `ESP_LOGW` | Деградація, ретрай | `W (456) i2c: NACK addr=0x76, retry 2/5` |
| `ESP_LOGI` | Життєвий цикл: boot, OTA, версія | `I (789) ota: updated to 2.5.0, reboot` |
| `ESP_LOGD` | Діагностика стенду | `D (...) sens: raw=519888 comp=25.01` |
| `ESP_LOGV` | Дамп байтів, тільки HIL | `V (...) i2c: >> 88 01 ...` |
| Керування | `esp_log_level_set("sens", ESP_LOG_DEBUG)` | `beta`=DEBUG, `stable`=INFO |

Код ESP-IDF:

```c
#include "esp_log.h"
static const char *TAG = "sens";
void sensor_poll(void) {
    int raw = 0;
    if (bme280_read_raw(&raw) != ESP_OK) {
        ESP_LOGW(TAG, "read failed raw=%d", raw);
        return;
    }
    ESP_LOGD(TAG, "raw=%d", raw);
    ESP_LOGI(TAG, "temp=%.2f", bme280_compensate_temp(raw));
}
void app_main(void) {
#ifdef CONFIG_BETA_BUILD
    esp_log_level_set("sens", ESP_LOG_DEBUG);
#else
    esp_log_level_set("*", ESP_LOG_INFO);
#endif
}
```

HIL-асерти по логах (стабільні рядки - контракт!):

```python
# tests/hil/expect.py — ганяється на хості, читає UART DUT
import re
def expect_boot(log: str):
    assert re.search(r"fw=\d+\.\d+\.\d+", log), "no version line"
    assert "SELFTEST PASS" in log, "selftest failed"
```

## 8. Techniques: golden-файли для сенсорних драйверів

| Крок | Що зробити |
| --- | --- |
| 1. Записати | Зняти 50-200 сирих семплів з реального сенсора (`raw,...`) в `vectors.csv` |
| 2. Заморозити | Покласти файл у `tests/golden/`, закомітити - це еталон |
| 3. Порівняти | CI проганяє `compensate()` і диффає з `expected` з допуском |
| 4. Оновлювати | Тільки свідомо (`UPDATE_GOLDEN=1`), з ревью дифу |
| 5. Версіонувати | `golden/v1/`, `golden/v2/` при зміні калібрування |

Формат `vectors.csv`:

```csv
# raw_temp, expected_celsius, tolerance
519888, 25.04, 0.05
434500, 12.30, 0.05
0, -40.00, 0.50
```

Код перевірки (`tests/golden/check_golden.py`):

```python
import csv, sys
sys.path.insert(0, "lib")
from bme280_convert import compensate_temp
fails = 0
with open("tests/golden/vectors.csv") as f:
    for row in csv.reader(f):
        if not row or row[0].startswith("#"): continue
        raw, exp, tol = int(row[0]), float(row[1]), float(row[2])
        got = compensate_temp(raw)
        ok = abs(got - exp) <= tol
        print(("PASS" if ok else "FAIL"), raw, got, exp)
        fails += not ok
sys.exit(1 if fails else 0)
```

Код ESP-IDF - той же golden на платі (читаємо з `spiffs`/embed):

```c
TEST_CASE("bme280: golden vectors", "[sensor][golden]") {
    extern const uint8_t golden_bin_start[] asm("_binary_golden_bin_start");
    // розпарсити і прогнати compensate, TEST_ASSERT_FLOAT_WITHIN
}
```

> [!TIP]
> Golden-файли ловлять «тиху деградацію»: зміна округлення, інший порядок операцій з `float`, новий даташит з іншими коефіцієнтами.

## 9. Типові помилки

| Симптом | Причина | Рішення |
| --- | --- | --- |
| `No tests found` в моніторі | `test/` не в `REQUIRES`, забули `idf.py reconfigure` | Додати `REQUIRES unity`, переконфігурувати |
| Тести падають тільки на платі | `float`/`double` різняться з хостом, порядок байтів | Допуски `FLOAT_WITHIN`, golden з толерантністю |
| CI зелений, плата цеглиться | Тестували тільки логіку, не драйвери/OTA | Додати HIL + rollback-тест |
| HIL флапає (то PASS, то FAIL) | Живлення DUT просідає, USB-хаб | Окремий БЖ 5В/2А, конденсатор 470 мкФ, прямий USB-порт |
| OTA downgrade до старої бити | Немає перевірки версії | Порівнювати semver + `secure_version`, відхиляти downgrade на stable |
| Логи забивають UART, тести таймаутять | `ESP_LOGV` у `stable` | `stable`=INFO, `beta`=DEBUG, дампи тільки в HIL |
| Golden оновили «щоб позеленіло» | Приховали регресію | Оновлення golden тільки з ревью + причина в коміті |
| Артефакти CI перезаписались | Немає тегів, `latest.bin` мутує | Іменувати `fw-<target>-<ver>-g<sha>.bin` + `.sha256`, `latest` - симлінк |

## Офіційні джерела

- [ESP-IDF - Build System (компоненти, test, CMake)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/build-system.html)
- [ESP-IDF - Logging library (ESP_LOG, рівні)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/log.html)
- [ESP-IDF - OTA Updates (rollback, канали)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html)
- [GitHub Actions - документація (workflows, матриці, артефакти)](https://docs.github.com/en/actions)
- [ThrowTheSwitch Unity - фреймворк юніт-тестів для C](https://github.com/ThrowTheSwitch/Unity)

### Mermaid: конвеєр тестів

```mermaid
flowchart LR
    PUSH[Push] --> BUILD2[Build matrix: чипи × IDF]
    BUILD2 --> UNIT[Unity-тести на хості]
    UNIT --> HIL[HIL: прошивка на залізо + self-test]
    HIL --> OTA2[OTA-канал beta → stable]
```

## Див. також

- [[Home]]
- [[09-Proshivka/01-ESP-IDF-setup]]
- [[09-Proshivka/02-Arduino-PlatformIO]]
- [[09-Proshivka/03-MicroPython|MicroPython]]
- [[09-Proshivka/06-FreeRTOS-Patterns]]
- [[09-Proshivka/08-Tooling-Deep]]
- [[07-Timeri-Son/02-WDT]]
- [[08-Pamyat/03-OTA|OTA]]
