---
title: Testing and CI for ESP32
description: Testing and CI for ESP32 - Unity tests, host emulation, GitHub Actions, HIL rig and OTA strategy; shows schematics, code and tables.
tags: [esp32, testing, unity, ci, github-actions, hil, ota, logging, semver]
category: Proshivka
lang: en
original: 09-Firmware/07-Testing-CI.md
date-created: 2026-09-28
date: 2026-10-09
---

# Testing and CI for ESP32

## Purpose

Firmware with no tests breaks silently: a sensor driver returns garbage, OTA bricks a batch, and `ESP_LOG` drowns in spam. This note shows the full quality loop: Unity tests in ESP-IDF via a `test` component, emulation of pure logic on the host (no board), GitHub Actions workflow with a matrix (build + tests), HIL rig where a second board acts as tester, semver versioning + build-metadata, OTA branch strategy `stable/beta`, `ESP_LOG` logging with levels, and the golden-file technique for sensor drivers. The starter environment is [[EN/09-Firmware/01-ESP-IDF-Setup.en]], alternatives are [[EN/09-Firmware/02-Arduino-PlatformIO.en]] and [[09-Firmware/03-MicroPython.en | MicroPython]], updates are [[08-Memory/03-OTA.en | OTA]], supervision is [[07-Timers/02-WDT.en | WDT]].

> [!NOTE]
> Test pyramid for ESP32: 70% - host tests of logic (fast, free), 20% - Unity on board (drivers, flash), 10% - HIL/manual (OTA, radio, power).

![[assets/img/testing-ci-scheme.png|600]]
*Fig. Testing pyramid: host unit tests, on-board Unity, HIL rig, OTA channels.*

## 1. Unity tests in IDF: test component

| Item | Where it lives | Purpose |
| --- | --- | --- |
| `components/sensor/test/CMakeLists.txt` | Next to the component | Test registration |
| `TEST_CASE("name", "[tag]")` | `test_*.c` | One case (Unity under the hood) |
| `idf.py build flash monitor` + `test` | UART menu | Run on board |
| `unity` component | Auto in `test/` | `TEST_ASSERT_EQUAL`, `TEST_ASSERT_FLOAT_WITHIN` |
| Tags `[sensor][i2c]` | Run filter | `test sensor` / `test "[i2c]"` |
| `setUp/tearDown` | Optional | Reset I2C bus/mock before a case |

Directory layout:

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

ESP-IDF code - `test/test_bme280.c`:

```c
#include "unity.h"
#include "bme280.h"

TEST_CASE("bme280: convert raw to celsius", "[sensor][convert]") {
    // чиста функція - можна ганяти і на хості, і на платі
    TEST_ASSERT_FLOAT_WITHIN(0.01, 25.0, bme280_compensate_temp(519888));
    TEST_ASSERT_FLOAT_WITHIN(0.01, -40.0, bme280_compensate_temp(0));
}

TEST_CASE("bme280: probe on I2C", "[sensor][i2c]") {
    TEST_ASSERT_TRUE(bme280_probe(0x76)); // потрібне залізо!
}
```

ESP-IDF code - minimal `test/CMakeLists.txt`:

```cmake
idf_component_register(SRCS "test_bme280.c"
                       INCLUDE_DIRS "."
                       REQUIRES unity bme280)
```

Run:

```bash
idf.py -p /dev/ttyUSB0 flash monitor
# в моніторі:
# > test sensor        # всі кейси компонента
# > test "[convert]"   # тільки чиста логіка
# > test --list        # список кейсів
```

> [!TIP]
> Split tags: `[convert]` (no hardware, stable) vs `[i2c]` (board/rig needed). Host CI runs only `[convert]`.

Arduino code - tests via PlatformIO + Unity:

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
; platformio.ini - окреме env для тестів
[env:test_native]
platform = native
test_framework = unity
lib_deps = throwtheswitch/Unity @ ^2.5.2
```

MicroPython code - tests with no Unity, `unittest` style:

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

## 2. Host emulation of logic: separate pure from hardware

| Layer | Example | Host test? |
| --- | --- | --- |
| Pure logic | `compensate_temp()`, CRC, NMEA parser, MQTT-state machine | Yes, `gcc + unity`, no board |
| HAL adapter | `i2c_read_reg()` wrapper | Mock (`fake_i2c.c`), yes |
| Driver | `bme280_probe()` to real I2C | No, board/HIL only |
| Network | Wi-Fi/MQTT client | Socket mock or HIL |
| Files/NVS | `nvs_get_u32` | Mock or `Running ESP-IDF on Host` |

> [!NOTE]
> Golden rule: a `*_convert.c` file does not include `driver/i2c.h`. Only math + `#include <stdint.h>`. Then it compiles both on ESP32 and on a laptop.

ESP-IDF code - split:

```c
// bme280_convert.h - чисте, без IDF-залежностей
#pragma once
#include <stdint.h>
float bme280_compensate_temp(int32_t adc_T);
// bme280_io.c - залізне, тільки для плати
#include "driver/i2c.h"
#include "bme280_convert.h"
esp_err_t bme280_read_raw(int *adc_T);
```

Host test build (`CMakeLists.txt` for Linux):

```cmake
cmake_minimum_required(VERSION 3.16)
project(host_tests C)
add_executable(host_tests test_host_main.c ../main/bme280_convert.c unity/unity.c)
target_include_directories(host_tests PRIVATE ../main unity)
```

```bash
gcc test_host_main.c bme280_convert.c unity/unity.c -o host_tests && ./host_tests
```

## 3. GitHub Actions: build + tests as a matrix (ready YAML)

| Job | What it does | Runner |
| --- | --- | --- |
| `host-tests` | `gcc` + Unity, golden compare | `ubuntu-latest` |
| `build` (matrix) | `idf.py build` for esp32/esp32s3/esp32c3 x stable/beta | `ubuntu-latest` + docker `espressif/idf` |
| `pio-build` | Arduino variant build | `ubuntu-latest` |
| `mpy-check` | `mpy-cross` compile + `ruff`/smoke on host | `ubuntu-latest` |
| `hil` | Only `workflow_dispatch` or nightly, self-hosted with board | `self-hosted` |

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
> Cache `~/.platformio` and `~/.espressif` (or take the docker `espressif/idf`) - else every CI run repeats a 10-minute toolchain install.

## 4. HIL rig: second board as tester

| Role | Board A (DUT) | Board B (Tester) |
| --- | --- | --- |
| Firmware | Candidate release | Fixed `hil-tester` (never touched without review) |
| Link | UART0 to USB (logs), UART1 to Tester (commands) | Controls DUT power via MOSFET/relay |
| Sensors | I2C sensor on bus | Emulates sensor (serves golden vectors over I2C-slave) |
| OTA test | Accepts OTA | Serves HTTP with binary + breaks link at 50% |
| Verdict | - | `PASS/FAIL` over UART + GPIO `TEST_OK` |

Rig diagram:

```text
[Tester ESP32] ---UART1 115200---> [DUT ESP32]
     | TX/RX                       | UART1 (команди)
     | GPIO4 (PWR_EN) -> MOSFET -> | 3V3 живлення DUT
     | I2C-slave (addr 0x76) ----> | I2C-master (сенсор-емуляція)
     | USB (логи тестера)           | USB (логи DUT)
```

Tester code (pseudo-ESP-IDF):

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
> HIL is `workflow_dispatch` + `nightly`, not on every push: boards glitch, USB drops. Keep the rig behind `screen`/self-hosted runner with auto-reboot.

MicroPython code for a cheap HIL tester:

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

## 5. Semver + build-metadata: firmware version as OTA contract

| Field | Format | Example |
| --- | --- | --- |
| `MAJOR.MINOR.PATCH` | semver | `2.4.1` |
| Pre-release | `-beta.N` | `2.5.0-beta.2` |
| Build-metadata | `+g<sha>.<timestamp>` | `2.4.1+g a1b2c3d.20260928` |
| Version source | `version.txt` / `git describe` / `PROJECT_VER` | One true file |
| OTA check | Server serves `version` + `sha256` | Board rejects downgrade (see sec. 6) |

Rule table:

| Change | Bump | OTA channel |
| --- | --- | --- |
| Sensor bug fix | PATCH `2.4.1` to `2.4.2` | `stable` |
| New sensor/command | MINOR `2.4.x` to `2.5.0-beta.1` | `beta` |
| Partition table / NVS schema change | MAJOR `2.x` to `3.0.0-beta.1` + migration | `beta`, then `stable` |
| Logs/docs only | No bump, build-metadata grows | Any |

ESP-IDF code - version in `CMakeLists.txt` + `app_desc`:

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

## 6. OTA branch strategy: stable / beta

| Branch | OTA channel | Who receives | Rollback |
| --- | --- | --- | --- |
| `main` to `stable` | `https://ota.example.com/stable/` | All field devices | Mandatory `esp_ota_mark_app_valid` after self-check |
| `beta` | `https://ota.example.com/beta/` | Rigs + volunteers | Downgrade to stable allowed |
| `feature/*` | No OTA | USB flash only | - |
| Tag `vX.Y.Z` | Frozen artifact `fw-X.Y.Z.bin` + `.sha256` | Release archive | Never overwritten |

Flow:

```text
feature/i2c-fix -> PR -> CI (host+build) -> merge beta
  -> beta OTA на стенд -> HIL PASS 24г -> тег v2.5.0
  -> merge main -> stable OTA хвилями 10% -> 50% -> 100%
```

ESP-IDF code - channel select via `sdkconfig.defaults.*`:

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
> Never pour `beta` on everyone: one broken partition table with no rollback means a visit to every device. Details - [[08-Memory/03-OTA.en | OTA]].

## 7. ESP_LOG logging + levels: logs as test interface

| Level | When | Example |
| --- | --- | --- |
| `ESP_LOGE` | Fatal issue, reboot/rollback follows | `E (123) mqtt: connect failed, reboot` |
| `ESP_LOGW` | Degradation, retry | `W (456) i2c: NACK addr=0x76, retry 2/5` |
| `ESP_LOGI` | Lifecycle: boot, OTA, version | `I (789) ota: updated to 2.5.0, reboot` |
| `ESP_LOGD` | Rig diagnostics | `D (...) sens: raw=519888 comp=25.01` |
| `ESP_LOGV` | Byte dumps, HIL only | `V (...) i2c: >> 88 01 ...` |
| Control | `esp_log_level_set("sens", ESP_LOG_DEBUG)` | `beta`=DEBUG, `stable`=INFO |

ESP-IDF code:

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

HIL asserts on logs (stable lines are a contract!):

```python
# tests/hil/expect.py - ганяється на хості, читає UART DUT
import re
def expect_boot(log: str):
    assert re.search(r"fw=\d+\.\d+\.\d+", log), "no version line"
    assert "SELFTEST PASS" in log, "selftest failed"
```

## 8. Techniques: golden files for sensor drivers

| Step | What to do |
| --- | --- |
| 1. Record | Capture 50-200 raw samples from a real sensor (`raw,...`) into `vectors.csv` |
| 2. Freeze | Put the file in `tests/golden/`, commit - this is the reference |
| 3. Compare | CI runs `compensate()` and diffs against `expected` with tolerance |
| 4. Update | Only deliberately (`UPDATE_GOLDEN=1`), with diff review |
| 5. Version | `golden/v1/`, `golden/v2/` on calibration change |

`vectors.csv` format:

```csv
# raw_temp, expected_celsius, tolerance
519888, 25.04, 0.05
434500, 12.30, 0.05
0, -40.00, 0.50
```

Check code (`tests/golden/check_golden.py`):

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

ESP-IDF code - the same golden on board (read from `spiffs`/embed):

```c
TEST_CASE("bme280: golden vectors", "[sensor][golden]") {
    extern const uint8_t golden_bin_start[] asm("_binary_golden_bin_start");
    // розпарсити і прогнати compensate, TEST_ASSERT_FLOAT_WITHIN
}
```

> [!TIP]
> Golden files catch "silent degradation": rounding changes, different `float` op order, new datasheet with new coefficients.

## 9. Common issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| `No tests found` in monitor | `test/` not in `REQUIRES`, forgot `idf.py reconfigure` | Add `REQUIRES unity`, reconfigure |
| Tests fail only on board | `float`/`double` differ from host, byte order | `FLOAT_WITHIN` tolerances, golden with tolerance |
| CI green, board bricks | Tested logic only, not drivers/OTA | Add HIL + rollback test |
| HIL flaps (PASS, then FAIL) | DUT supply sags, USB hub | Separate 5V/2A PSU, 470 uF capacitor, direct USB port |
| OTA downgrade to old beta | No version check | Compare semver + `secure_version`, reject downgrade on stable |
| Logs flood UART, tests time out | `ESP_LOGV` in `stable` | `stable`=INFO, `beta`=DEBUG, dumps in HIL only |
| Golden updated "to turn green" | Hid a regression | Golden updates only with review + reason in commit |
| CI artifacts overwritten | No tags, mutating `latest.bin` | Name `fw-<target>-<ver>-g<sha>.bin` + `.sha256`, `latest` as symlink |

## Official sources

- [ESP-IDF - Build System (components, test, CMake)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/build-system.html)
- [ESP-IDF - Logging library (ESP_LOG, levels)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/log.html)
- [ESP-IDF - OTA Updates (rollback, channels)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html)
- [GitHub Actions - docs (workflows, matrices, artifacts)](https://docs.github.com/en/actions)
- [ThrowTheSwitch Unity - C unit test framework](https://github.com/ThrowTheSwitch/Unity)

### Mermaid: test pipeline

```mermaid
flowchart LR
    PUSH[Push] --> BUILD2[Build matrix: chips x IDF]
    BUILD2 --> UNIT[Unity tests on host]
    UNIT --> HIL[HIL: flash to hardware + self-test]
    HIL --> OTA2[OTA channel beta to stable]
```

## See also

- [[EN/Home.en]]
- [[EN/09-Firmware/01-ESP-IDF-Setup.en]]
- [[EN/09-Firmware/02-Arduino-PlatformIO.en]]
- [[09-Firmware/03-MicroPython.en | MicroPython]]
- [[EN/09-Firmware/06-FreeRTOS-Patterns.en]]
- [[EN/09-Firmware/08-Tooling-Deep.en]]
- [[EN/07-Timers/02-WDT.en]]
- [[08-Memory/03-OTA.en | OTA]]
