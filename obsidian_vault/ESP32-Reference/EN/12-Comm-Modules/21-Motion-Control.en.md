---
description: ESP32 is a full motion controller: it counts steps at up to 120 kHz,; shows schematics, code and tables.
title: Motion Control on ESP32 - FluidNC, grbl_ESP32, Klipper, micro-ROS, ESP-Drone, CRSF telemetry
tags: [esp32, motion, fluidnc, grbl-esp32, klipper, micro-ros, esp-drone, cnc, tmc2209, crsf, telemetry, yaml, step-dir]
category: Moduli
lang: en
date-created: 2026-09-29
date: 2026-10-10
original: 12-Moduli-zvyazku/21-Motion-Control.md
---

# Motion Control on ESP32 - FluidNC / grbl_ESP32 / Klipper / micro-ROS / ESP-Drone

## Purpose

ESP32 is a full motion controller: it counts steps at up to 120 kHz,
holds a CNC-machine WebUI, works as a 3D-printer secondary MCU under Klipper,
spins a ROS 2 node via micro-ROS, flies as a mini-quadcopter under ESP-Drone
or sits as a second board next to a Betaflight/INAV flight controller as a GPS logger
and CRSF telemetry bridge. Note brings all six ecosystems into one map:
where ESP32 is primary (FluidNC, grbl_ESP32, ESP-Drone), where subordinate
(Klipper secondary MCU, micro-ROS node), and where an honest "second pilot"
next to an STM32F4/F7/H7 flight controller that it never replaces.

Note covers: FluidNC `config.yaml` from zero, WebUI + SD card,
TMC drivers over UART/SPI, grbl_ESP32 step/dir pins and `$` settings,
Klipper on ESP32 how secondary MCU (menuconfig + printer.cfg),
micro-ROS (agent, publisher/subscriber, UART/WiFi transport, executor),
ESP-Drone (stabilize/height-hold/position-hold modes, flow-deck),
the honest INAV/Betaflight on ESP32 limit, three ready codes
(FluidNC-config, micro-ROS publisher, CRSF telemetry) and 14 common issues.

![[assets/img/motion-control-fluidnc-scheme.png|600]]
*Fig. ESP32 as a FluidNC motion controller: step/dir to TMC2209, limit switches, spindle, SD card, WebUI over WiFi.*

## Ecosystem overview - who is primary, who is subordinate

| Firmware | ESP32 role | Hardware | Config | Transport | When to take |
| --- | --- | --- | --- | --- | --- |
| FluidNC | primary CNC/laser controller | ESP32 + outdoor drivers (TMC2209/DM542) | `config.yaml` on flash/SD, without recompilation | WiFi WebUI, Telnet, USB-Serial, SD | new machine, mill, laser, plotter |
| grbl_ESP32 | primary CNC controller (legacy) | ESP32 + drivers | recompilation + `$` commands in EEPROM | USB-Serial, BT-Serial, WiFi | old project that already lives on grbl_ESP32 |
| grblHAL | grbl_ESP32 successor (active branch) | ESP32 + drivers, WebUI | `$` commands compatible, config via WebUI | USB-Serial, WiFi, Ethernet (with expansion boards) | new CNC projects instead of frozen grbl_ESP32 |
| Klipper | secondary MCU | RPi host + ESP32 as executive node | `printer.cfg` on host + `make menuconfig` for ESP32 | USB-UART to host | 3D printer: ESP32 reads ADXL345, drives fan/LED |
| micro-ROS | ROS 2 node on microcontroller | ESP32 + agent on PC/RPi | `colcon.meta` + `idf.py menuconfig` | UDP/WiFi or UART-serial to agent | mobile robot, manipulator, swarm |
| ESP-Drone | mini-drone primary flight controller | ESP32 + motor-driver board + IMU | `sdkconfig`, Crazyflie parameters | WiFi-APP, ESP-NOW joystick, cfclient | STEAM education, room flights |
| Betaflight / INAV | ESP32 is not a flight controller! | STM32 flight controller + ESP32 as second board | Betaflight Configurator / INAV Configurator | CRSF/SBUS/MAVLink bridge | GPS logger, CRSF telemetry, WiFi gateway to GCS |

> Honest rule: Betaflight and INAV do not work on ESP32 as flight controllers -
> the 8 kHz stabilization loop + DShot + gyro-DMA is sharpened for STM32F4/F7/H7/AT32.
> ESP32 next to them is a telemetry bridge, logger and ground gateway,
> see the section below and [[EN/12-Comm-Modules/12-RC-Protocols.en]].

## FluidNC - primary CNC controller

FluidNC is the grbl_ESP32 successor from the same author (bdring). Architecture
Object-oriented: the machine is described by a text `config.yaml`, one firmware for all -
no recompilation needed. Supports up to 6 coordinated axes, dual
motors per axis with portal auto-squaring, PWM spindle /
RS485 Modbus / DAC 0-10 V / relay, laser with power compensation from speed,
tool change, SD card with G-code launch over WiFi, WebUI in browser,
Telnet G-code feed, OTA updates and push notifications.

### What FluidNC can do out of the box

| Subsystem | Features | Where in YAML |
| --- | --- | --- |
| Axes | up to 6 XYZABC axes, up to 12 motors, dual-motor Y with two limit switches | `axes:` |
| Drivers | Step/Dir, TMC2209/TMC5160 over UART/SPI (StealthChop, CoolStep, StallGuard) | `axes: to motor0: to tmc_2209:` |
| Limit switches | limit/homing with debounce, sensorless-homing via StallGuard | `axes: to homing:` |
| Probes | Z-probe on any axis, safety-door, hold/resume/reset buttons | `probe:`, `control:` |
| Spindle | PWM, laser, RS485-VFD (Huanyang), 10V-DAC, BESC for brushless | `spindle:` |
| Cooling | Mist, Flood | `coolant:` |
| Link | USB-Serial, WiFi AP/STA, WebUI, Telnet, BT-Serial | `wifi:`, `telnet:` |
| Files | SD card, launch from WebUI, several `*.yaml` + `$Config/Filename=` | `sdcard:` |
| Macros | script buttons, job start/end, tool-change sequences | `macros:`, `start:` |

### Pin legend of a typical FluidNC board (6-pack / generic DevKit)

| ESP32 pin | FluidNC function | Where | Note |
| --- | --- | --- | --- |
| GPIO14 | X.step | Driver X STEP | 50% duty step, up to 120 kHz |
| GPIO25 | X.dir | Driver X DIR | direction, set >= 1 us before step edge |
| GPIO26 | Y.step | Driver Y STEP | twisted pair with ground, < 30 cm |
| GPIO33 | Y.dir | Driver Y DIR | - |
| GPIO17 | Z.step | Driver Z STEP | - |
| GPIO16 | Z.dir | Driver Z DIR | - |
| GPIO4 | UART TX to TMC2209 | Driver RX (chain) | one TX for all: addresses 0/1/2 by MS1/MS2 jumpers |
| GPIO15 | UART RX from TMC2209 | Driver TX via 1 kOhm | summing resistor mandatory in a chain! |
| GPIO34 | X.limit | X limit switch, NO to GND | input-only pin, pull-up only, without output! |
| GPIO35 | Y.limit | Y limit switch | input-only, see [[EN/03-GPIO/01-GPIO-Overview.en]] |
| GPIO32 | Z.probe | Z probe | pull-up to 3V3, shield from spindle |
| GPIO27 | spindle PWM | MOSFET/laser TTL | via [[EN/11-Vivid/11-PowerMotion-2.en]] |
| GPIO13, GPIO5, GPIO23, GPIO19, GPIO18 | SD SPI | SD card | SCK/MOSI/MISO/CS like in [[EN/04-Interfaces/07-SD-SDIO.en]] |
| EN, GPIO0 | reset/feed-hold buttons | buttons to GND | - |

Explanation:

- **Step/dir - separate GPIOs per motor:** each driver wants its own
  step+dir pair; run step ground next to the signal, not along 24 V power.
- **TMC UART - one wire bus:** controller TX fan-out to RX of all drivers,
  back - via 1 kOhm resistors from each TX to the common controller RX point,
  otherwise drivers "argue" on the line.
- **GPIO34/35 - inputs only:** they have no internal pull-up that can be
  correctly enabled by software for a limit switch - put an outdoor 4.7-10 kOhm to 3V3.
- **Spindle - never directly:** GPIO27 gives 3.3 V logic, then a MOSFET module,
  relay or laser TTL driver with optoisolation.

### ASCII schematic

```text
                    FLUIDNC — ESP32 DevKit + 3x TMC2209 + SD + шпиндель
                    ───────────────────────────────────────────────────
   Живлення логіки                 ESP32                        Силова частина
   ───────────────                 ─────                        ──────────────
   5V USB ──► AMS1117 ──► 3V3 ──► [3V3]                    24V ──► VM драйверів
                             ┌── [EN] ──► кнопки Hold/Resume до GND
                             │
   TMC-UART bus (один TX!)   │   GPIO4 (TX) ──┬──► RX TMC-X (addr 0)
                             │                ├──► RX TMC-Y (addr 1)
                             │                └──► RX TMC-Z (addr 2)
                             │   GPIO15 (RX) ◄──┬── 1кОм ── TX TMC-X
                             │                  ├── 1кОм ── TX TMC-Y
                             │                  └── 1кОм ── TX TMC-Z
                             │
   Кроки/напрями              │   GPIO14 ──► STEP X    GPIO25 ──► DIR X
                             │   GPIO26 ──► STEP Y    GPIO33 ──► DIR Y
                             │   GPIO17 ──► STEP Z    GPIO16 ──► DIR Z
                             │
   Кінцевики (NO до GND)      │   GPIO34 ◄── кінцевик X (pull-up 10к до 3V3)
                             │   GPIO35 ◄── кінцевик Y (pull-up 10к до 3V3)
                             │   GPIO32 ◄── Z-щуп    (екран, подалі від 24В)
                             │
   Шпиндель/лазер             │   GPIO27 ──► MOSFET-module ──► шпиндель/лазер TTL
                             │              (див. [[11-Vivid/11-PowerMotion-2]])
                             │
   SD-карта (SPI)             │   GPIO23 ──► MOSI SD    GPIO19 ◄── MISO SD
                             │   GPIO18 ──► SCK SD     GPIO13 ──► CS SD
                             │   GPIO5  ──► (другий CS / резерв)
                             │
   Зв'язок                    │   USB ──► G-code sender / FluidTerm
                             └── WiFi ──► WebUI в браузері (192.168.0.1 або STA-IP)

 Notes:
 - GND спільна: ESP32 GND ── драйвери GND ── 24V GND ── корпус верстата (одна точка!).
 - Сигнальні step-джгути < 30 см, кручена пара signal+GND, не поруч із 24В/шпинделем.
 - VM драйверів 12–24 В + електроліт 470–1000 мкФ біля кожного драйвера.
 - TMC2209 без адреси = конфлікт: MS1/MS2 перемички дають addr 0/1/2!
```

### Mermaid

```mermaid
graph LR
    subgraph ESP32_FluidNC[ESP32 FluidNC]
        CPU[Motion planner<br/>+ WebUI + Telnet]
        STEP[Step/dir generator<br/>up to 120 kHz]
        TMC[TMC-UART<br/>GPIO4/GPIO15]
        SD[SD SPI<br/>G-code files]
        SP[Spindle PWM<br/>GPIO27]
    end
        DRIVERS[Drivers]
        DX[TMC2209 X<br/>addr 0]
        DY[TMC2209 Y<br/>addr 1]
        DZ[TMC2209 Z<br/>addr 2]
    end
        MECH[Mechanics]
        MX[X axis<br/>screw/belt]
        MY[Y axis<br/>dual / portal]
        MZ[Z axis<br/>+ probe]
        LIM[Limit switches<br/>X/Y/Z]
    end
        USER[User]
        PC[Browser WebUI<br/>+ Telnet + USB]
    end
    CPU --> STEP
    CPU --> TMC
    CPU --> SD
    CPU --> SP
    STEP --> DX & DY & DZ
    TMC --> DX & DY & DZ
    DX --> MX
    DY --> MY
    DZ --> MZ
    LIM --> CPU
    SP --> MZ
    PC <-->|WiFi / USB| CPU
```

### FluidNC: WebUI, SD, TMC drivers in detail

- **WebUI:** built-in Esp32_WebUI - after firmware the board raises the
  `FluidNC` AP or hooks to home WiFi (STA, set in YAML).
  In browser: jog buttons, DRO coordinates, `.nc/.gcode` download to SD,
  launch/pause, `$` command console, `config.yaml` editor right in WebUI.
- **SD card:** G-code pours over WiFi in WebUI to be written to SD to run
  from SD without PC tie (USB jitter does not tear the laser arc). Two CS pins for a second
  card or backup, SD SPI frequency up to 20 MHz, short traces.
- **TMC2209 over UART:** StealthChop (quiet), CoolStep (heats less),
  StallGuard (sensorless homing). Current `run_current`, microstep
`microsteps`, address `uart_num` set in YAML per motor, not by current
  jumpers Vref - the Vref pot on the UART version is ignored!
- **Several configs:** `config.yaml` by default lands on flash;
  `$Config/Filename=/mine.yaml` switches to another file - handy to keep
  "mill.yaml" and "laser.yaml" on one board.
- **Diagnostics:** `$SS` (system status), `$LD` (list SD directories),
  `$Config/Dump` - print of active YAML, `$Motors/Disable` - drop current.

## grbl_ESP32 - predecessor (legacy but alive)

grbl_ESP32 is a classic grbl port for ESP32, frozen in favor of FluidNC
(the author directly advises new projects on FluidNC). Differences:

| Feature | grbl_ESP32 | FluidNC |
| --- | --- | --- |
| Machine description | pin `#define` + recompilation | `config.yaml`, without recompilation |
| Settings | `$0..$132` in EEPROM | YAML items + some `$` on the fly |
| Axes/motors | up to 6 axes, up to 12 motors | same but more flexible mapping |
| TMC | SPI versions, StealthChop/StallGuard | UART + SPI, fuller set |
| WebUI | exists (same Esp32_WebUI) | newer, YAML editor |
| Status | maintenance only | active development |

### grbl_ESP32 step/dir pins (example `machine.h`)

Typical 3-axis mill mapping: step pins nearby, dir pins nearby,
enable shared. In machine code:

```cpp
// Grbl_ESP32: CPU_MAP, приклад кастомної машини
#define X_STEP_PIN       GPIO_NUM_14
#define X_DIRECTION_PIN  GPIO_NUM_25
#define Y_STEP_PIN       GPIO_NUM_26
#define Y_DIRECTION_PIN  GPIO_NUM_33
#define Z_STEP_PIN       GPIO_NUM_17
#define Z_DIRECTION_PIN  GPIO_NUM_16
#define STEPPERS_DISABLE_PIN GPIO_NUM_13
#define X_LIMIT_PIN      GPIO_NUM_34
#define Y_LIMIT_PIN      GPIO_NUM_35
#define SPINDLE_PWM_PIN  GPIO_NUM_27
```

### grbl_ESP32 `$` settings (what to turn first)

| Command | Content | Typical |
| --- | --- | --- |
| `$100`, `$101`, `$102` | steps/mm X/Y/Z | 80 (GT2-20T), 400 (8 mm screw + 1/8) |
| `$110`, `$111`, `$112` | max speed mm/min | 3000 / 3000 / 1000 |
| `$120`, `$121`, `$122` | acceleration mm/s2 | 200 / 200 / 100 |
| `$130`-`$132` | axis travel mm (soft limits) | 300 / 300 / 80 |
| `$20`, `$21`, `$22` | soft/hard limits, homing enable | 1 / 1 / 1 |
| `$23` | homing direction inversion | bit mask |
| `$3` | dir inversion | mask, if an axis goes the wrong way |
| `$5` | limit-probe inversion | 0 = NO, 1 = NC |
| `$32` | laser mode | 1 for laser, 0 for spindle |
| `$$` | print of all | check before first start |
| `$H` | homing of all axes | only after limit switches! |
| `$X` | drop alarm-lock | after an accident, with cause check |

> grbl_ESP32 to FluidNC migration: `$100` becomes
> `axes: → x: → motor0: → steps_per_mm:`, `$110` - `max_rate_mm_per_min:`,
> `$120` is `acceleration_mm_per_sec2:`. Pins from `machine.h` move
> to `step_pin:` / `direction_pin:` / `limit_all_pin:` of matching YAML sections.

## Klipper - ESP32 how secondary MCU

Klipper splits work: Raspberry Pi counts the trajectory (Python), while microcontrollers
do steps on schedule (C). ESP32 here is an ideal second/third MCU:
native WiFi is not needed (link is wired USB-UART with the host!), but many
GPIOs, ADC, RMT for NeoPixel, I2C for ADXL345 resonance measurement.

### Architecture with ESP32 add-on

| Node | Role | What on it |
| --- | --- | --- |
| RPi host | Klipper host + Moonraker + Fluidd/Mainsail | `printer.cfg`, kinematics, pressure advance, input shaping |
| Main MCU (SKR/Manta) | primary `[mcu]` | XYZ/E steps, heating, fans |
| ESP32 | secondary `[mcu esp32]` | ADXL345 over SPI, NeoPixel, extra fan, button, thermocouple |

### Flashing ESP32 for Klipper (menuconfig)

```text
cd ~/klipper && make menuconfig
  Micro-controller Architecture = Espressif ESP32
  Processor model = ESP32 (або ESP32-S2/S3 за платою)
  Communication interface = USB-serial (через CP2102/CH340 плати)
  # або Serial на UART0, якщо шити безпосередньо через USB-UART міст
make
make flash FLASH_DEVICE=/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0
ls /dev/serial/by-id/*   # <- цей ID піде в printer.cfg
```

### `printer.cfg` - ESP32 as second MCU

```ini
[mcu esp32]
serial: /dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0
restart_method: command

# ADXL345 на ESP32 для виміру резонансів (input shaper)
[adxl345]
cs_pin: esp32:gpio5
spi_bus: spi2a
axes_map: x,y,z

# NeoPixel-стрічка через RMT ESP32
[neopixel sb_leds]
pin: esp32:gpio21
chain_count: 12
color_order: GRB
initial_RED: 0.1
initial_GREEN: 0.1
initial_BLUE: 0.1

# Додатковий вентилятор корпуса
[fan_generic chamber_fan]
pin: esp32:gpio22
max_power: 1.0

# Кнопка filament-runout на ESP32
[filament_switch_sensor runout]
pause_on_runout: True
switch_pin: ^!esp32:gpio34
```

Explanation:

- **`esp32:` prefix** in each pin tells Klipper which MCU owns the pin.
  Without prefix the pin is looked up on the primary `[mcu]` and errors.
- **`^` and `!`** are pull-up and inversion: `^!esp32:gpio34` = pull-up + NC sensor.
- **ADXL345 - only over ESP32 SPI:** Klipper does not calibrate resonances correctly in
  ADXL345 I2C mode; SPI 5 MHz, wires < 15 cm, see resonances in Klipper docs.
- **USB-serial, not WiFi:** Klipper does not talk to an MCU over WiFi-TCP in stable
  mode - only wired serial. ESP32 WiFi in Klipper mode is not used.
- **Multi-MCU homing:** a limit switch must hang on the same MCU as its motor,
  otherwise a `multi-mcu homing` error during `$H`/G28.

## micro-ROS - ESP32 as a ROS 2 node

micro-ROS plants the ROS 2 client API (rclc + Micro XRCE-DDS) straight on ESP32.
ESP32 talks to a micro-ROS agent (program on PC/RPi), while the agent already talks
to the rest of the ROS 2 graph over DDS. Two transports: UDP over WiFi (handy) or UART-serial
(reliable, without WiFi jitter). Execution model is executor: one thread spins
timers, subscribers and services in a loop.

### Architecture

| Layer | Where it lives | What it does |
| --- | --- | --- |
| ROS 2 graph (Humble/Jazzy) | PC / RPi | `rviz`, `ros2 topic echo`, Nav2 navigation |
| micro-ROS Agent | PC / RPi, Docker `microros/micro-ros-agent` | XRCE-DDS to DDS bridge: `udp4 --port 8888` or `serial --dev /dev/ttyUSB0` |
| micro-ROS node | ESP32 (ESP-IDF + component) | publishes odometry, listens to `cmd_vel`, spins motors |
| Transport | WiFi-UDP or UART | UDP for mobility, UART for determinism |

### ESP-IDF component setup

```text
. $IDF_PATH/export.sh
pip3 install catkin_pkg colcon-common-extensions lark
cd my_robot/components
git clone -b rolling https://github.com/micro-ROS/micro_ros_espidf_component.git
cd ../..
idf.py set-target esp32
idf.py menuconfig
  # micro-ROS Settings -> middleware = Micro XRCE-DDS
  # micro-ROS Settings -> transport = UDP (WiFi SSID/pass) або UART
  # WiFi credentials вписати тут же, якщо транспорт UDP
idf.py build && idf.py flash && idf.py monitor
```

Agent on host:

```bash
# UDP-агент (ESP32 по WiFi стукає на порт 8888):
docker run -it --rm --net=host microros/micro-ros-agent:rolling udp4 --port 8888 -v6
# Serial-агент (ESP32 по USB-UART):
docker run -it --rm -v /dev:/dev --privileged --net=host \
  microros/micro-ros-agent:rolling serial --dev /dev/ttyUSB0 -v6
```

### Executor - the node heart (patterns)

| Pattern | When | Example |
| --- | --- | --- |
| One timer + one publisher | 20 Hz odometry beacon | `rclc_timer_init_default` + `rclc_executor_spin` |
| `cmd_vel` subscriber + PWM | differential robot | Twist callback to MCPWM on two motors |
| Service + action | calibration / grip | `rclc_service_init_default`, states in callback |
| Static executor + `10 ms sleep` | battery node | fewer wake-ups, charge economy |

> Memory: keep `rmw` buffers small (`colcon.meta` - MTU 512 on UART),
> otherwise ESP32 eats a pile of PSRAM for XRCE fragmentation.

## ESP-Drone - mini-quadcopter on ESP32

ESP-Drone (Espressif, Crazyflie port) is a full flight controller for a room
quad on ESP32/S2/S3 under ESP-IDF v5. Stabilization code is from Crazyflie (GPL-3.0),
board is simple: ESP32 + brushed-motor driver + MPU9250/BMI088 IMU.

### Modes and expansion boards

| Mode | What it stabilizes | What is needed |
| --- | --- | --- |
| Stabilize (attitude) | roll/pitch angles, yaw-rate | base board + IMU |
| Height-hold (flapper/altitude) | + pressure height | altimeter board (BMP388/LPS22) |
| Position-hold (positioning) | + XY by optic flow | flow-deck: PMW3901 (optic-flow) + VL53L1x (ToF rangefinder) |
| APP control | smartphone control | drone WiFi AP + ESP-Drone APP (iOS/Android) |
| Joystick / cfclient | PC control | `crazyflie-clients-python`, ESP-NOW joystick via ESP-BOX3 |

### Control link

| Channel | Transport | Delay | When |
| --- | --- | --- | --- |
| WiFi APP | UDP to drone AP | ~20-50 ms | learning, STEAM demo |
| ESP-NOW joystick | ESP-NOW 2.4 GHz | ~5-10 ms | more exact flights without router |
| cfclient (Crazyradio-compatible) | USB dongle to Crazyflie protocol | ~10 ms | logs, PID parameters, telemetry |

> Flow-deck is the key to room position-hold without GPS: PMW3901 looks down
> and measures optic flow (floor-picture shift), VL53L1x gives ToF height.
> Without flow-deck a room drone holds only angles and height - XY drifts with wind.

## INAV / Betaflight on ESP32 - honest limit

Neither INAV nor Betaflight builds for ESP32 as a flight-controller target:
targets are STM32F4/F7/H7 and AT32, an 8 kHz PID loop, DMA gyro reads, DShot with exact
timing. ESP32 lacks the needed DMA chains for their scheduler and
passes no CI target of these projects. So the correct topology is two boards:

```text
STM32-польотник (Betaflight/INAV)  <──CRS F/SBUS/MAVLink──>  ESP32 (другий борт)
  gyro + PID 8 кГц, DShot до ESC                                GPS-логер (SD)
  OSD, failsafe, RTH                                            WiFi-шлюз до GCS
  CRSF-приймач ELRS ──TX/RX── ESP32-перехоплювач ──TX/RX── FC   CRSF-міст + LTM-ретранслятор
```

| ESP32 role next to FC | Protocol | UART | Why |
| --- | --- | --- | --- |
| CRSF bridge / sniffer | CRSF 420000 8N1 | UART2 | channel logs, telemetry relay to ground |
| GPS logger | NMEA/UBX 115200 | UART1 | write track to SD independently of FC blackbox |
| MAVLink gateway | MAVLink 57600 | UART1 + WiFi | FC to ESP32 to QGroundControl over WiFi |
| S.Port/F.Port node | 57600/115200 inv. | UART + inversion | give voltage/current to a FrSky receiver |
| DShot bench (without flight!) | DShot via RMT | RMT TX | spin a motor on the bench, see MCPWM/RMT note |

CRSF-parsing details, SBUS inversion and MAVLink-heartbeat are in the
[[EN/12-Comm-Modules/12-RC-Protocols.en]], RMT DShot timing is in section 4 of file
in [[EN/07-Timers/01-Timers-MCPWM-PCNT-RMT.en]].

## Code 1 - FluidNC `config.yaml` (3 axes + TMC2209 + laser/spindle)

```yaml
# FluidNC config.yaml — 3-осьовий фрезер/лазер на ESP32 DevKit + 3x TMC2209
# Залити через WebUI (Config) або по USB: fluidterm / `pio run -t uploadfs`
name: "ESP32 3-axis TMC2209"
board: "ESP32 DevKit"

stepping:
  engine: RMT
  idle_ms: 255
  pulse_us: 2
  dir_delay_us: 1

uart1:
  txd_pin: gpio.4
  rxd_pin: gpio.15
  rts_pin: NO_PIN
  cts_pin: NO_PIN
  baud: 115200
  mode: 8N1

axes:
  x:
    steps_per_mm: 80.0
    max_rate_mm_per_min: 3000
    acceleration_mm_per_sec2: 200
    max_travel_mm: 300
    homing:
      cycle: 2
      mpos_mm: 0.0
      feed_mm_per_min: 300.0
      seek_mm_per_min: 1500.0
      settle_ms: 250
    motor0:
      limit_all_pin: gpio.34:low:pu
      step_pin: gpio.14
      direction_pin: gpio.25
      disable_pin: NO_PIN
      tmc_2209:
        uart_num: 1
        addr: 0
        r_sense_ohms: 0.110
        run_current: 1.2
        hold_current: 0.6
        microsteps: 8
        stallguard: 0
        stealthchop: true
    motor1: null
  y:
    steps_per_mm: 80.0
    max_rate_mm_per_min: 3000
    acceleration_mm_per_sec2: 200
    max_travel_mm: 300
    homing:
      cycle: 2
      mpos_mm: 0.0
      feed_mm_per_min: 300.0
      seek_mm_per_min: 1500.0
      settle_ms: 250
    motor0:
      limit_all_pin: gpio.35:low:pu
      step_pin: gpio.26
      direction_pin: gpio.33
      disable_pin: NO_PIN
      tmc_2209:
        uart_num: 1
        addr: 1
        r_sense_ohms: 0.110
        run_current: 1.2
        hold_current: 0.6
        microsteps: 8
        stallguard: 0
        stealthchop: true
  z:
    steps_per_mm: 400.0
    max_rate_mm_per_min: 1000
    acceleration_mm_per_sec2: 100
    max_travel_mm: 80
    homing:
      cycle: 1
      mpos_mm: 0.0
      feed_mm_per_min: 200.0
      seek_mm_per_min: 800.0
      settle_ms: 250
    motor0:
      limit_all_pin: gpio.32:low:pu
      step_pin: gpio.17
      direction_pin: gpio.16
      disable_pin: NO_PIN
      tmc_2209:
        uart_num: 1
        addr: 2
        r_sense_ohms: 0.110
        run_current: 1.0
        hold_current: 0.5
        microsteps: 8
        stallguard: 0
        stealthchop: true

probe:
  pin: gpio.32:low:pu
  toolsetter_pin: NO_PIN
  check_mode_start: true

spindle:
  pwm:
    pwm_hz: 5000
    output_pin: gpio.27
    enable_pin: NO_PIN
    direction_pin: NO_PIN
    disable_with_zero_speed: false
    s_off_with_disable: true
    spinup_ms: 0
    spindown_ms: 0
    tool_num: 0
    speed_map: 0=0% 1000=0% 24000=100%

coolant:
  mist_pin: NO_PIN
  flood_pin: NO_PIN
  delay_ms: 0

control:
  safety_door_pin: NO_PIN
  reset_pin: NO_PIN
  feed_hold_pin: NO_PIN
  cycle_start_pin: NO_PIN
  macro0_pin: NO_PIN

sdcard:
  cs_pin: gpio.13
  card_detect_pin: NO_PIN
  frequency_hz: 20000000

wifi:
  ap:
    ssid: "FluidNC"
  sta:
    ssid: ""
    password: ""
  hostname: fluidnc
  access_point: true

telnet:
  enable: true
  port: 23

start:
  must_home: true
  deactivate_parking: false
  check_limits: true
```

Config comments:

- `engine: RMT` - steps via ESP32 RMT peripheral, most stable timing;
  `pulse_us: 2` keeps compatibility with TMC2209 and outdoor DM542.
- `uart1 to 115200` - TMC bus; all three drivers on one UART with different
  `addr` (MS1/MS2 jumpers on the driver board set 0/1/2).
- `r_sense_ohms: 0.110` - check against the Rsense marking on the specific module
  (may be 0.110 or 0.220!); wrong value = twice-wrong current.
- `limit_all_pin: gpio.34:low:pu` - NO limit switch to ground with pull-up;
  for NC sensors - `:high`, see GPIO note.
- `must_home: true` - the machine will not go without `$H` after power-on; safety first.
- Laser mode separately: `$32=1` in console or a `laser:` section in newer
  FluidNC builds - verify `$I` (build info) before engraving.

## Code 2 - micro-ROS publisher on ESP-IDF (odometry + cmd_vel)

```c
// micro-ROS ESP32: паблішер одометрії 20 Гц + сабскрайбер cmd_vel -> MCPWM
// ESP-IDF + micro_ros_espidf_component. Транспорт: UDP/WiFi або UART (menuconfig).
#include <stdio.h>
#include <unistd.h>
#include <rcl/rcl.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <std_msgs/msg/int32.h>
#include <geometry_msgs/msg/twist.h>

#define RCCHECK(fn) { rcl_ret_t rc = fn; if (rc != RCL_RET_OK) printf("RCL err %d @%d\n", rc, __LINE__); }
#define RCSOFTCHECK(fn) { rcl_ret_t rc = fn; (void)rc; }

static int32_t odom_ticks = 0;

// cmd_vel -> сюди прийде швидкість від Nav2 / teleop
static void cmd_vel_cb(const void * msgin) {
    const geometry_msgs__msg__Twist * twist = (const geometry_msgs__msg__Twist *)msgin;
    float lin = twist->linear.x;    // м/с
    float ang = twist->angular.z;   // рад/с
    // TODO: lin/ang -> PWM лівого/правого мотора через MCPWM,
    // див. [[11-Vivid/11-PowerMotion-2]] і [[07-Timers/01-Timeri-MCPWM-PCNT-RMT]]
    printf("cmd_vel: lin=%.2f ang=%.2f\n", lin, ang);
}

// Таймер 50 мс: наростити "одометрію" і опублікувати
static void timer_cb(rcl_timer_t * timer, int64_t last_call_time) {
    (void)timer; (void)last_call_time;
    static std_msgs__msg__Int32 msg;
    // TODO: прочитати енкодери через PCNT (див. MCPWM-PCNT-RMT ноту)
    odom_ticks += 10;
    msg.data = odom_ticks;
    RCSOFTCHECK(rcl_publish(timer, NULL, NULL)); // заглушка-ніц: див. нижче
    (void)msg;
}

void app_main(void) {
    rcl_allocator_t allocator = rcl_get_default_allocator();
    rclc_support_t support;
    RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

    rcl_node_t node;
    RCCHECK(rclc_node_init_default(&node, "esp32_odom", "", &support));

    rcl_publisher_t pub;
    RCCHECK(rclc_publisher_init_default(
        &pub, &node,
        ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int32),
        "wheel_ticks"));

    rcl_subscription_t sub;
    RCCHECK(rclc_subscription_init_default(
        &sub, &node,
        ROSIDL_GET_MSG_TYPE_SUPPORT(geometry_msgs, msg, Twist),
        "cmd_vel"));

    rcl_timer_t timer;
    RCCHECK(rclc_timer_init_default(&timer, &support, RCL_MS_FROM_SEC(1) / 20, timer_cb));

    rclc_executor_t executor;
    RCCHECK(rclc_executor_init(&executor, &support.context, 2, &allocator));
    RCCHECK(rclc_executor_add_timer(&executor, &timer));
    RCCHECK(rclc_executor_add_subscription(
        &executor, &sub, &(geometry_msgs__msg__Twist){0},
        &cmd_vel_cb, ON_NEW_DATA));

    // Правильна публікація з таймера: тримаємо publisher глобально.
    // У мінімальному прикладі int32_publisher з репозиторію компонента:
    //   rcl_publish(&pub, &msg, NULL);
    // Повний робочий приклад: examples/int32_publisher компонента.
    rclc_executor_spin(&executor);

    RCCHECK(rcl_publisher_fini(&pub, &node));
    RCCHECK(rcl_node_fini(&node));
}
```

> Working minimum without cuts is in the component repo:
> `examples/int32_publisher` (publisher) and `examples/int32_subscriber`.
> Code above is a frame for your robot: substitute a real `rcl_publish(&pub, ...)`
> in the timer, PCNT encoders and MCPWM bridges from [[EN/11-Vivid/11-PowerMotion-2.en]].

Launch steps of the link:

```bash
# 1. Агент на хості (RPi/ПК), ROS 2 Humble/Jazzy:
docker run -it --rm --net=host microros/micro-ros-agent:rolling udp4 --port 8888 -v6
# 2. ESP32 вже прошитий з WiFi-транспортом і IP агента -> стукає сам.
# 3. Перевірка графа:
ros2 topic list            # мають бути /wheel_ticks /cmd_vel
ros2 topic echo /wheel_ticks
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 0.2}, angular: {z: 0.0}}" --once
```

## Code 3 - ESP32 CRSF telemetry to ELRS receiver (battery + GPS)

```cpp
// ESP32 -> ELRS-приймач: CRSF-телеметрія (Battery 0x08 + GPS 0x02), 420000 8N1
// Без інверсії! UART2: RX=GPIO16 (від TX приймача), TX=GPIO17 (до RX приймача).
// CRC8-DVB-S2, big-endian у payload. Деталі кадру: див. RC-Protocols ноту.
#include <Arduino.h>

#define CRSF_BAUD 420000
#define CRSF_ADDR_FC 0xC8
#define CRSF_TYPE_BATTERY 0x08
#define CRSF_TYPE_GPS 0x02

uint8_t crc8_dvb_s2(uint8_t crc, uint8_t b) {
    crc ^= b;
    for (int i = 0; i < 8; i++)
        crc = (crc & 0x80) ? (crc << 1) ^ 0xD5 : (crc << 1);
    return crc;
}

// voltage: В*10 (126 = 12.6 В), current: А*10, fuel: 0..100%, remaining: мАг
void crsfSendBattery(uint16_t mv_x10, uint16_t ma_x10, uint8_t fuel_pct) {
    uint8_t f[2 + 8 + 1];
    f[0] = CRSF_ADDR_FC;
    f[1] = 10; // len = type(1) + payload(8) + crc(1)
    f[2] = CRSF_TYPE_BATTERY;
    f[3] = (mv_x10 >> 8) & 0xFF; f[4] = mv_x10 & 0xFF;
    f[5] = (ma_x10 >> 8) & 0xFF; f[6] = ma_x10 & 0xFF;
    f[7] = 0; f[8] = 0; f[9] = 0; // capacity used, мАг (3 байти)
    f[10] = fuel_pct;
    uint8_t crc = 0;
    for (int i = 2; i < 11; i++) crc = crc8_dvb_s2(crc, f[i]);
    f[11] = crc;
    Serial2.write(f, sizeof(f));
}

// lat/lon: градуси*1e7 (int32), alt: метри+1000 (напр. 1123 = 123 м)
void crsfSendGps(int32_t lat_e7, int32_t lon_e7, uint16_t gspd_kmh_x10,
                 uint16_t hdg_deg_x100, uint16_t alt_m_plus1000, uint8_t sats) {
    uint8_t f[2 + 15 + 1];
    f[0] = CRSF_ADDR_FC;
    f[1] = 17;
    f[2] = CRSF_TYPE_GPS;
    f[3] = (lat_e7 >> 24) & 0xFF; f[4] = (lat_e7 >> 16) & 0xFF;
    f[5] = (lat_e7 >> 8) & 0xFF;  f[6] = lat_e7 & 0xFF;
    f[7] = (lon_e7 >> 24) & 0xFF; f[8] = (lon_e7 >> 16) & 0xFF;
    f[9] = (lon_e7 >> 8) & 0xFF;  f[10] = lon_e7 & 0xFF;
    f[11] = (gspd_kmh_x10 >> 8) & 0xFF; f[12] = gspd_kmh_x10 & 0xFF;
    f[13] = (hdg_deg_x100 >> 8) & 0xFF; f[14] = hdg_deg_x100 & 0xFF;
    f[15] = (alt_m_plus1000 >> 8) & 0xFF; f[16] = alt_m_plus1000 & 0xFF;
    f[17] = sats;
    uint8_t crc = 0;
    for (int i = 2; i < 18; i++) crc = crc8_dvb_s2(crc, f[i]);
    f[18] = crc;
    Serial2.write(f, sizeof(f));
}

void setup() {
    Serial.begin(115200);
    // CRSF: 420000 8N1, пряма логіка, БЕЗ інверсії!
    Serial2.begin(CRSF_BAUD, SERIAL_8N1, 16, 17);
}

void loop() {
    // Приклад: 16.7 В, 8.4 А, 72% + Київ, 0 км/г, 123 м, 12 супутників
    crsfSendBattery(167, 84, 72);
    crsfSendGps(504378000, 304567000, 0, 0, 1123, 12);
    delay(250); // ~4 Гц: батарея+Gps по черзі, не частіше 10 Гц сумарно
    // TODO: читати справжні INA219 (див. 10-Sensori) і GPS (див. 17-GNSS-RTK)
    // замість констант вище.
}
```

Code explanation:

- **`0xC8` address** is "flight controller": the ELRS receiver takes telemetry only
  from this address; `0xEE` is the transmitter address itself, do not use it.
- **Big-endian:** multi-byte CRSF fields go senior byte first
  (unlike MAVLink/SBUS LSB), mix up and 1123 m height becomes 253 m.
- **4 Hz rate:** send battery and GPS in turn no more often than 10 Hz total,
  otherwise you clog the uplink and channels start lagging.
- **Cross:** receiver TX to GPIO16, receiver RX to GPIO17 (like a plain UART).

## Machine/dryer power, grounds and safety

| Node | Requirement | Why |
| --- | --- | --- |
| ESP32 logic | 3.3 V, separate LDO with 500 mA margin | sag = step tearing and WebUI restart |
| Step drivers | 12-24 V, 470+ uF electrolytic near each | damping motor back-kicks |
| Common ground | one star: ESP32 - drivers - PSU - enclosure | ground loops = false limit switches and "dancing" coordinates |
| Signal harnesses | step/dir < 30 cm, twisted pair with GND | cross pickup from 24 V and spindle |
| Spindle/heating | only via MOSFET/relay module | GPIO gives 12 mA - a MOSFET without driver will not open |
| E-stop | physical button tears 24 V/220 V, not GPIO! | software stop does not save on hang |
| Limit switches | shield, NC chain in series on long axes | NC-chain break = accident, not a frame crash |
| USB + 24 V at once | ground first, then USB; or isolated USB-UART | potential difference burns CP2102 |

> Never bring E-stop only into ESP32: the red mushroom must tear the power
> line with a contactor. GPIO stop is the second frontier, not the first.

## typical errors

| No. | Symptom | Cause | Fix |
| --- | --- | --- | --- |
| 1 | FluidNC: `config.yaml not found` after flashing | file flashed not to that FS or with BOM/tabs | reflash via WebUI to Config; YAML - spaces only, UTF-8 without BOM, verify `$Config/Filename=` |
| 2 | FluidNC silent, no WebUI | STA SSID/password wrong, board not on network | temporarily `access_point: true`, enter AP `FluidNC`, fix STA credentials |
| 3 | Motors tremble in place / go half distance | `r_sense_ohms` wrong (0.110 vs 0.220) or wrong `microsteps` | check Rsense on module, recount `steps_per_mm = microsteps x motor_steps / mm_per_rev` |
| 4 | TMC2209 does not answer over UART | all `addr` identical or no 1 kOhm resistors on return line | give addr 0/1/2 with MS1/MS2 jumpers, solder 1 kOhm from each driver TX to ESP32 RX |
| 5 | Limit switch triggers by itself | spindle/24 V pickup, no debounce | twisted pair + shield, 10-100 nF capacitor near input, NC logic, away from power |
| 6 | GPIO34/35 "do not hold" pull-up | these are input-only pins without a correct internal pull-up | outdoor 4.7-10 kOhm resistor to 3V3, see GPIO note |
| 7 | Axis goes the wrong way / homing into wall | `direction_pin` inversion or `homing:mpos_mm` from the wrong edge | invert pin (`gpio.25:low` to `:high`) or `$3` in grbl_ESP32, verify `$H` at low feed |
| 8 | grbl_ESP32: `$H` hits the frame | `$23` (homing mask) or `$5` (probe inversion) wrong | set `$23` per limit-switch placement, `$5` per NO/NC, test with hand on E-stop |
| 9 | Klipper: `Unable to connect to MCU esp32` | wrong `/dev/serial/by-id/*` or board in download mode | `ls /dev/serial/by-id/*` after reflash, write fresh ID into `[mcu esp32]`, `restart` |
| 10 | Klipper: `multi-mcu homing` / pins of wrong board | limit switch and motor on different MCUs or forgotten `esp32:` prefix | move limit switch to the same MCU as its motor; write each ESP32 pin as `esp32:gpioN` |
| 11 | micro-ROS: topics not seen in `ros2 topic list` | agent not started or ESP32 knocks on wrong IP/port | raise `micro-ros-agent udp4 --port 8888`, check agent IP and WiFi credentials in `menuconfig`, `-v6` agent logs |
| 12 | micro-ROS: `fragmentation` / memory falls | XRCE MTU too big for UDP/WiFi or too many publishers | lower MTU in `colcon.meta` (512 for UART), cut queues, static executor instead of dynamics |
| 13 | ESP-Drone does not hold room position | no flow-deck or glossy textureless floor | put PMW3901+VL53L1x deck, fly over carpet/newspaper, calibrate IMU before takeoff |
| 14 | CRSF telemetry silent on radio | inversion on, TX/RX swapped or address not `0xC8` | turn inversion off (CRSF is straight logic!), cross TX to RX, `0xC8` address, 420000 8N1 baud, rate <= 10 Hz |

## Official sources

- [FluidNC - GitHub (firmware, config.yaml examples, WebUI)](https://github.com/bdring/FluidNC) - YAML machines, RMT stepper, TMC drivers, SD/Telnet/WebUI, migration from grbl_ESP32.
- [Grbl_ESP32 - GitHub (FluidNC predecessor, machine.h, $settings)](https://github.com/bdring/Grbl_Esp32) - step/dir mapping, 6 axes, TMC-SPI, BT/WiFi connectivity, transition-to-FluidNC statement.
- [Klipper overview](https://www.klipper3d.org/Overview.html) - host+MCU architecture, `make menuconfig`, `printer.cfg`, secondary-MCU approach.
- [Klipper - Installation (menuconfig, flash, serial by-id)](https://www.klipper3d.org/Installation.html) - step-by-step MCU flashing, serial-port detection, `printer.cfg` structure.
- [micro-ROS overview docs](https://micro.vulcanexus.org/docs/overview/) - XRCE-DDS bridge, UDP/serial transports, executor model, supported-hardware list.
- [micro_ros_espidf_component - GitHub (ESP-IDF component, examples)](https://github.com/micro-ROS/micro_ros_espidf_component) - `int32_publisher`, `menuconfig`, UDP/UART transports, Docker agent.
- [ESP-Drone - GitHub (mini-drone firmware, flow-deck)](https://github.com/espressif/esp-drone) - stabilize/height-hold/position-hold, PMW3901+ToF deck, WiFi APP, ESP-IDF v5.
- [Betaflight setup guide](https://betaflight.com/docs/wiki/getting-started/setup-guide) - why the flight controller is STM32, while ESP32 nearby is only a bridge/logger.
- [INAV - GitHub (navigation flight controller, telemetry)](https://github.com/iNavFlight/inav) - position-hold/RTH/waypoints on F4/F7/H7, CRSF/MAVLink/LTM telemetry for the ESP32 bridge.
- [ESP-IDF Programming Guide - ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/index.html) - RMT/MCPWM/PCNT/UART base for all motion codes of this note.

## See also

- [[EN/Home.en]]
- [[EN/11-Vivid/11-PowerMotion-2.en]]
- [[EN/11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.en]]
- [[EN/07-Timers/01-Timers-MCPWM-PCNT-RMT.en]]
- [[EN/04-Interfaces/01-UART.en|UART]]
- [[EN/12-Comm-Modules/12-RC-Protocols.en]]
- [[EN/04-Interfaces/07-SD-SDIO.en]]
- [[EN/03-GPIO/01-GPIO-Overview.en]]
- [[EN/05-Radio/01-WiFi-STA-AP.en]]
- [[EN/09-Firmware/06-FreeRTOS-Patterns.en]]
- [[EN/10-Sensors/19-IMU-6-9DOF.en]]
- [[EN/12-Comm-Modules/17-GNSS-RTK.en]]
- [[EN/99-Additions/02-Troubleshooting-FAQ.en]]
- [[EN/99-Additions/06-Official-Sources-Modules.en]]
