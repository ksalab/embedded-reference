---
title: Environment choice - STM32CubeIDE vs Arduino vs PlatformIO, HAL vs LL
description: Compares STM32CubeIDE, Arduino and PlatformIO and shows the HAL vs LL difference in code; shows schematics, code and tables.
tags: [stm32, start, ide, cubeide, cubemx, platformio, arduino, hal, ll]
category: Start
lang: en
original: 00-Start/05-Vibir-seredovischa.md
date-created: 2026-10-01
date: 2026-10-08
---

# Environment choice - STM32CubeIDE vs Arduino vs PlatformIO

![[assets/img/stm32-env-choose-scheme.png|600]]
*Fig. Three paths: CubeIDE (full control), Arduino (fast start), PlatformIO (deps + CI).*

> [!tip] Purpose of this note
> Pick a tool for the task, not from habit: comparison, choice rule, traps of each.

## 1. Purpose

The environment sets the start speed and the capability ceiling. Arduino is Blink in 10 minutes but has no CubeMX configurator and foreign cores. CubeIDE is full control (HAL/LL, debug, CubeMX) with a higher entry bar. PlatformIO is dependencies and CI on top of both worlds.

## Option specs

| Criterion | STM32CubeIDE | Arduino (STM32Duino core) | PlatformIO |
| --- | --- | --- | --- |
| Price/license | Free (ST) | Free | Free (core - PIO) |
| CubeMX generation | Built-in | None (by hand/DIV) | Via CubeMX + import |
| HAL vs LL | Both + direct register | Arduino wrappers (hidden HAL) | As configured |
| Debug | ST-Link + GDB out of the box | Limited (Serial + occasional ST-Link) | ST-Link via settings |
| Libraries | ST HAL examples | Thousands of Arduino libraries | PIO Registry + Arduino + HAL |
| CI/automation | headless builds are hard | CLI exists but crooked | `pio run/test/ci` - best |

```text
Швидкий вибір:
  Навчання / прототип за вечір .. Arduino (Blue Pill + USB-Serial)
  Серійний виріб / складна периферія  CubeIDE + HAL (далі LL у гарячих місцях)
  Команда / CI / кілька плат ........ PlatformIO
```

## Mermaid: HAL vs LL

```mermaid
flowchart TB
    Q[Writing a driver] --> HOT{Hot path?}
    HOT -->|No: init, slow| HAL[HAL: readable, portable]
    HOT -->|Yes: ISR, MHz| LL[LL: thin, fast, closer to registers]
    HOT -->|Extreme| REG[Direct registers (see Reference Manual!)]
```

## Common issues

| # | Issue | Cause | Fix |
| --- | --- | --- | --- |
| 1 | Arduino core not for your chip | Does not compile / wrong pins | Check board support in the STM32Duino core |
| 2 | HAL in a MHz interrupt | Misses deadlines, jitter | LL or registers in ISR |
| 3 | CubeMX regenerated over hand code | Code is gone | Your code ONLY between `USER CODE BEGIN/END`! |
| 4 | Debug over Serial instead of ST-Link | Blind on lockups | ST-Link + breakpoints from day 1 |

## Official sources

- [STM32CubeIDE (ST)](https://www.st.com/en/development-tools/stm32cubeide.html) - IDE + CubeMX.
- [Arduino core STM32 (GitHub)](https://github.com/stm32duino/Arduino_Core_STM32) - supported boards.

## First project step by step

**CubeIDE:** File → New → STM32 Project → pick your chip → name it → Yes initialize peripherals → in `.ioc` enable GPIO LED as Output → Ctrl+S (generate!) → write between USER CODE → Debug (green bug).

**Arduino:** Tools → Board → find your board → Blink example → Upload. First time is slow (core compile), then fast.

**PlatformIO:** New Project → board + Arduino/STM32Cube framework → `src/main.cpp` → Upload + Monitor. Libraries go through Library Manager in `platformio.ini` (`lib_deps`).

## HAL vs LL on an example (blink an LED)

```c
// HAL: читабельно
HAL_GPIO_TogglePin(LD2_GPIO_Port, LD2_Pin);
HAL_Delay(500);
// LL: те саме, швидше і тонше
LL_GPIO_TogglePin(LD2_GPIO_Port, LD2_Pin);
LL_mDelay(500);
```

## HAL vs LL deeper: where each hurts

| Situation | HAL | LL |
| --- | --- | --- |
| Peripheral init | One `HAL_UART_Init` call | Dozens of setup lines |
| 1 kHz interrupt | In time with margin | In time even more |
| 100 kHz+ interrupt | Jitter, misses | Only option |
| Datasheet reading | Rarely needed | Mandatory (what exactly you write to the register) |
| Port to another chip | Often compiles at once | Rewrite spots with different registers |
| Code size | Bigger (but who cares at 512K) | Smaller, matters for F0 with 16K |

## ST-Link setup in all three

| Environment | What to press | If not seen |
| --- | --- | --- |
| CubeIDE | Green bug → Debug Configurations → STM32 Cortex-M C/C++ Application | Update ST-Link firmware via STM32CubeProgrammer |
| Arduino | Tools → Programmer: ST-Link | Check the STLINK-VCP driver |
| PlatformIO | Debug button (bug) + `debug_tool = stlink` in ini | `platformio device list`, replug USB |

## Migration between environments

Arduino → CubeIDE: take the logic (`loop` → `while(1)` in main), rewrite HAL calls instead of Arduino functions, check pins against CubeMX. CubeIDE → PlatformIO: copy `Core/` + create `platformio.ini` with `framework = stm32cube`. PlatformIO → Arduino: pull the logic back into `.ino`, drop HAL dependencies.

## CI example for PlatformIO (GitHub Actions)

```yaml
# .github/workflows/build.yml — збірка при кожному push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with: { path: ~/.platformio, key: pio }
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install platformio
      - run: pio run -e nucleo_f401re -e bluepill_f103c8
```

## When to change environment mid-project

| Signal | Where to go |
| --- | --- | --- |
| Arduino got tight (no debug, odd crashes) | CubeIDE + ST-Link |
| CubeIDE project must build on a server | PlatformIO (same code, `platformio.ini`) |
| Need a foreign Arduino example in CubeIDE | Port by hand: logic - yes, libraries - look for HAL analogs |

## Command cheat sheet of the three environments

| Action | CubeIDE | Arduino IDE | PlatformIO |
| --- | --- | --- | --- |
| Build | Ctrl+B / Build | Verify (checkmark) | `pio run` |
| Flash | Debug (bug) | Upload (arrow) | `pio run -t upload` |
| Monitor | OpenOCD Console / SWO | Serial Monitor | `pio device monitor` |
| Clean build | Project → Clean | None (cache hides) | `pio run -t clean` |

## Project storage (backup!)

> A project lives in three places: code in git, CubeMX `.ioc` next to the code (no restoring the config without it!), generated files can be deleted and regenerated. Binaries and IDE `.settings` do not go into git.

## Toolchain versions in a team

- Pin CubeIDE/GCC versions in the project README, otherwise the build drifts.
- One Docker image with the toolchain for all developers.

## See also

- [[Home.en]]
- [[00-Start/03-Porivnyannya-chipiv| Chip comparison]]
- [[00-Start/04-Devkit-plati| DevKit boards]]
