---
description: ESP32 - повноцінний контролер руху: він рахує кроки з частотою до 120 кГц,
title: Motion Control на ESP32 - FluidNC, grbl_ESP32, Klipper, micro-ROS, ESP-Drone, CRSF-телеметрія
tags: [esp32, motion, fluidnc, grbl-esp32, klipper, micro-ros, esp-drone, cnc, tmc2209, crsf, telemetry, yaml, step-dir]
category: Moduli
date-created: 2026-09-29
---

# Motion Control на ESP32 - FluidNC / grbl_ESP32 / Klipper / micro-ROS / ESP-Drone

## Призначення

ESP32 - повноцінний контролер руху: він рахує кроки з частотою до 120 кГц,
тримає WebUI ЧПК-верстата, працює вторинним MCU 3D-принтера під Klipper,
крутить вузол ROS 2 через micro-ROS, літає як міні-квадрокоптер під ESP-Drone
або сидить другим бортом поруч із польотником Betaflight/INAV як GPS-логер
і CRSF-міст телеметрії. Нота зводить усі шість екосистем в одну карту:
де ESP32 - головний (FluidNC, grbl_ESP32, ESP-Drone), де - підлеглий
(Klipper secondary MCU, micro-ROS node), а де - чесний «другий пілот»
поряд із STM32F4/F7/H7-польотником, який він ніколи не замінює.

Нота покриває: конфіг FluidNC `config.yaml` з нуля, WebUI + SD-карту,
TMC-драйвери по UART/SPI, піни step/dir grbl_ESP32 і `$`-налаштування,
Klipper на ESP32 як secondary MCU (menuconfig + printer.cfg),
micro-ROS (agent, publisher/subscriber, транспорт UART/WiFi, executor),
ESP-Drone (режими stabilize/height-hold/position-hold, flow-deck),
чесну межу INAV/Betaflight на ESP32, три готові коди
(FluidNC-config, micro-ROS publisher, CRSF-телеметрія) і 14 типових помилок.

![](../../../ESP32-Reference/assets/img/motion-control-fluidnc-scheme.png)
*Рис. ESP32 як контролер руху FluidNC: step/dir до TMC2209, кінцевики, шпиндель, SD-карта, WebUI по WiFi.*

## Огляд екосистем - хто головний, хто підлеглий

| Прошивка | Роль ESP32 | Залізо | Конфіг | Транспорт | Коли брати |
| --- | --- | --- | --- | --- | --- |
| FluidNC | головний контролер ЧПК/лазера | ESP32 + зовнішні драйвери (TMC2209/DM542) | `config.yaml` на флеш/SD, без перекомпіляції | WiFi WebUI, Telnet, USB-Serial, SD | новий верстат, фрезер, лазер, plotter |
| grbl_ESP32 | головний контролер ЧПК (legacy) | ESP32 + драйвери | перекомпіляція + `$`-команди в EEPROM | USB-Serial, BT-Serial, WiFi | старий проєкт, який вже живе на grbl_ESP32 |
| grblHAL | наступник grbl_ESP32 (активна гілка) | ESP32 + драйвери, WebUI | `$`-команди сумісні, конфіг через WebUI | USB-Serial, WiFi, Ethernet (з платами розширення) | нові ЧПК-проєкти замість замороженого grbl_ESP32 |
| Klipper | вторинний MCU (secondary) | RPi-хост + ESP32 як виконавчий вузол | `printer.cfg` на хості + `make menuconfig` для ESP32 | USB-UART до хоста | 3D-принтер: ESP32 читає ADXL345, керує вентилятором/світлодіодом |
| micro-ROS | ROS 2-вузол на мікроконтролері | ESP32 + агент на ПК/RPi | `colcon.meta` + `idf.py menuconfig` | UDP/WiFi або UART-serial до агента | мобільний робот, маніпулятор, рій |
| ESP-Drone | головний польотник міні-дрона | ESP32 + плата керування моторами + IMU | `sdkconfig`, параметри Crazyflie | WiFi-APP, ESP-NOW-джойстик, cfclient | STEAM-освіта, кімнатні польоти |
| Betaflight / INAV | ESP32 - НЕ польотник! | STM32-польотник + ESP32 другим бортом | Betaflight Configurator / INAV Configurator | CRSF/SBUS/MAVLink міст | GPS-логер, CRSF-телеметрія, WiFi-шлюз до GCS |

> Чесне правило: Betaflight і INAV не працюють на ESP32 як польотники -
> цикл стабілізації 8 кГц + DShot + gyro-DMA заточений під STM32F4/F7/H7/AT32.
> ESP32 поруч із ними - це телеметрійний міст, логер і наземний шлюз,
> див. розділ нижче і [12-RC-Protocols](../../../ESP32-Reference/12-Moduli-zvyazku/12-RC-Protocols.md).

## FluidNC - головний контролер ЧПК

FluidNC - наступник grbl_ESP32 від того ж автора (bdring). Архітектура
об'єктна: машина описується текстовим `config.yaml`, прошивка одна на всіх -
перекомпіляція не потрібна. Підтримує до 6 координованих осей, подвійні
мотори на вісь з авто-вирівнюванням порталу (auto-squaring), шпиндель PWM /
RS485 Modbus / DAC 0-10 В / реле, лазер з компенсацією потужності від швидкості,
зміну інструменту, SD-карту з запуском G-коду по WiFi, WebUI в браузері,
Telnet-подачу G-коду, OTA-оновлення і push-сповіщення.

### Що вміє FluidNC з коробки

| Підсистема | Можливості | Де лежить у YAML |
| --- | --- | --- |
| Осі | до 6 осей XYZABC, до 12 моторів, dual-motor Y з двома кінцевиками | `axes:` |
| Драйвери | Step/Dir, TMC2209/TMC5160 по UART/SPI (StealthChop, CoolStep, StallGuard) | `axes: → motor0: → tmc_2209:` |
| Кінцевики | limit/homing з дебаунсом, sensorless-homing через StallGuard | `axes: → homing:` |
| Зонди | Z-probe на будь-яку вісь, safety-door, hold/resume/reset кнопки | `probe:`, `control:` |
| Шпиндель | PWM, лазер, RS485-VFD (Huanyang), 10V-DAC, BESC для безколекторників | `spindle:` |
| Охолодження | Mist, Flood | `coolant:` |
| Зв'язок | USB-Serial, WiFi AP/STA, WebUI, Telnet, BT-Serial | `wifi:`, `telnet:` |
| Файли | SD-карта, запуск з WebUI, кілька `*.yaml` + `$Config/Filename=` | `sdcard:` |
| Макроси | кнопки-скрипти, старт/кінець завдання, tool-change послідовності | `macros:`, `start:` |

### Легенда пінів типової плати FluidNC (6-pack / generic DevKit)

| Пін ESP32 | Функція FluidNC | Куди | Примітка |
| --- | --- | --- | --- |
| GPIO14 | X.step | STEP драйвера X | крок 50% шпаруватість, частота до 120 кГц |
| GPIO25 | X.dir | DIR драйвера X | напрям, встановити до фронту step ≥ 1 мкс |
| GPIO26 | Y.step | STEP драйвера Y | кручена пара зі землею, < 30 см |
| GPIO33 | Y.dir | DIR драйвера Y | - |
| GPIO17 | Z.step | STEP драйвера Z | - |
| GPIO16 | Z.dir | DIR драйвера Z | - |
| GPIO4 | UART TX до TMC2209 | RX драйверів (ланцюжок) | один TX на всіх: адреси 0/1/2 перемичками MS1/MS2 |
| GPIO15 | UART RX від TMC2209 | TX драйверів через 1 кОм | резистор-суматор обов'язковий при ланцюжку! |
| GPIO34 | X.limit | кінцевик X, NO до GND | вхід only-input, тільки pull-up, без виходу! |
| GPIO35 | Y.limit | кінцевик Y | only-input, див. [01-GPIO-oglyad](../../../ESP32-Reference/03-GPIO/01-GPIO-oglyad.md) |
| GPIO32 | Z.probe | щуп Z | підтяжка до 3V3, екран від шпинделя |
| GPIO27 | spindle PWM | MOSFET/лазер TTL | через [11-PowerMotion-2](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md) |
| GPIO13, GPIO5, GPIO23, GPIO19, GPIO18 | SD SPI | SD-карта | SCK/MOSI/MISO/CS як у [07-SD-SDIO](../../../ESP32-Reference/04-Shini/07-SD-SDIO.md) |
| EN, GPIO0 | reset/feed-hold кнопки | кнопки до GND | - |

Пояснення:

- **Step/dir - окремі GPIO на мотор:** кожен драйвер хоче свою пару
  step+dir; землю кроку вести поруч із сигналом, не уздовж силових 24 В.
- **TMC UART - один провід-шина:** TX контролера віялом на RX усіх драйверів,
  назад - через резистори 1 кОм з кожного TX у спільну точку RX контролера,
  інакше драйвери «сперечаються» на лінії.
- **GPIO34/35 - тільки входи:** на них немає внутрішнього pull-up, який можна
  ввімкнути програмно коректно для кінцевика - став зовнішній 4.7-10 кОм до 3V3.
- **Шпиндель - ніколи безпосередньо:** GPIO27 дає 3.3 В логіку, а далі MOSFET-модуль,
  реле або TTL-драйвер лазера з опторозв'язкою.

### ASCII-схема

```text
                    FLUIDNC — ESP32 DevKit + 3x TMC2209 + SD + шпиндель
                    ───────────────────────────────────────────────────
   Живлення логіки                 ESP32                        Силова частина
   ───────────────                 ─────                        ──────────────
   5V USB ──► AMS1117 ──► 3V3 ──► [3V3]                    24V ──► VM драйверів
                             ┌── [EN] ──► кнопки Hold/Resume до GND
                             │
   TMC-UART шина (один TX!)   │   GPIO4 (TX) ──┬──► RX TMC-X (addr 0)
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
   Шпиндель/лазер             │   GPIO27 ──► MOSFET-модуль ──► шпиндель/лазер TTL
                             │              (див. [[11-Vivid/11-PowerMotion-2]])
                             │
   SD-карта (SPI)             │   GPIO23 ──► MOSI SD    GPIO19 ◄── MISO SD
                             │   GPIO18 ──► SCK SD     GPIO13 ──► CS SD
                             │   GPIO5  ──► (другий CS / резерв)
                             │
   Зв'язок                    │   USB ──► G-code sender / FluidTerm
                             └── WiFi ──► WebUI в браузері (192.168.0.1 або STA-IP)

 Примітки:
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
        STEP[Step/dir генератор<br/>до 120 кГц]
        TMC[TMC-UART<br/>GPIO4/GPIO15]
        SD[SD SPI<br/>G-code файли]
        SP[Spindle PWM<br/>GPIO27]
    end
    subgraph DRIVERS[Драйвери]
        DX[TMC2209 X<br/>addr 0]
        DY[TMC2209 Y<br/>addr 1]
        DZ[TMC2209 Z<br/>addr 2]
    end
    subgraph MECH[Механіка]
        MX[Вісь X<br/>гвинт/ремінь]
        MY[Вісь Y<br/>dual / портал]
        MZ[Вісь Z<br/>+ щуп]
        LIM[Кінцевики<br/>X/Y/Z]
    end
    subgraph USER[Користувач]
        PC[Браузер WebUI<br/>+ Telnet + USB]
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

### FluidNC: WebUI, SD, TMC-драйвери детально

- **WebUI:** вбудований Esp32_WebUI - після прошивки плата піднімає AP
  `FluidNC` або чіпляється до домашнього WiFi (STA, задається в YAML).
  У браузері: jog-кнопки, DRO-координати, завантаження `.nc/.gcode` на SD,
  запуск/пауза, консоль `$`-команд, редактор `config.yaml` прямо в WebUI.
- **SD-карта:** G-код ллється по WiFi у WebUI → пишеться на SD → виконується
  з SD без прив'язі до ПК (джиттер USB не рве дугу лазера). Два CS - під другу
  карту або резерв, частота SPI SD до 20 МГц, доріжки короткі.
- **TMC2209 по UART:** StealthChop (тихо), CoolStep (менше гріється),
  StallGuard (бездатчикове homing). Струм `run_current`, мікрокрок
  `microsteps`, адреса `uart_num` задаються в YAML на мотор, а не перемичками
  струму Vref - Vref-потенціометр на UART-версії ігнорується!
- **Кілька конфігів:** на флеш лягає `config.yaml` за замовчуванням;
  `$Config/Filename=/моя.yaml` перемикає на інший файл - зручно тримати
  «фрезер.yaml» і «лазер.yaml» на одній платі.
- **Діагностика:** `$SS` (system status), `$LD` (list directories SD),
  `$Config/Dump` - роздрук активного YAML, `$Motors/Disable` - зняти струм.

## grbl_ESP32 - попередник (legacy, але живий)

grbl_ESP32 - порт класичного grbl під ESP32, заморожений на користь FluidNC
(автор прямо радить нові проєкти робити на FluidNC). Відмінності:

| Риса | grbl_ESP32 | FluidNC |
| --- | --- | --- |
| Опис машини | `#define` пінів + перекомпіляція | `config.yaml`, без перекомпіляції |
| Налаштування | `$0..$132` у EEPROM | пункти YAML + частина `$` на льоту |
| Осей/моторів | до 6 осей, до 12 моторів | так само, але гнучкіше маплення |
| TMC | SPI-версії, StealthChop/StallGuard | UART + SPI, повніший набір |
| WebUI | є (той же Esp32_WebUI) | новіший, редактор YAML |
| Статус | maintenance only | активна розробка |

### Піни step/dir у grbl_ESP32 (приклад `machine.h`)

Типовий мапінг 3-осьового фрезера: step-пини поруч, dir-пини поруч,
enable - спільний. У коді машини:

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

### `$`-налаштування grbl_ESP32 (що крутити першим)

| Команда | Зміст | Типове |
| --- | --- | --- |
| `$100`, `$101`, `$102` | кроків/мм X/Y/Z | 80 (GT2-20T), 400 (гвинт 8 мм + 1/8) |
| `$110`, `$111`, `$112` | макс. швидкість мм/хв | 3000 / 3000 / 1000 |
| `$120`, `$121`, `$122` | прискорення мм/с² | 200 / 200 / 100 |
| `$130`-`$132` | хід осей мм (soft limits) | 300 / 300 / 80 |
| `$20`, `$21`, `$22` | soft/hard limits, homing enable | 1 / 1 / 1 |
| `$23` | інверсія безпосередньо homing | маска бітів |
| `$3` | інверсія dir | маска, якщо вісь їде не туди |
| `$5` | інверсія limit-щупів | 0 = NO, 1 = NC |
| `$32` | режим лазера | 1 для лазера, 0 для шпинделя |
| `$$` | роздрук усіх | перевірка перед першим пуском |
| `$H` | homing усіх осей | тільки після кінцевиків! |
| `$X` | зняти alarm-lock | після аварії, з перевіркою причини |

> Міграція grbl_ESP32 → FluidNC: `$100` стає
> `axes: → x: → motor0: → steps_per_mm:`, `$110` - `max_rate_mm_per_min:`,
> `$120` - `acceleration_mm_per_sec2:`. Піни з `machine.h` переїжджають
> у `step_pin:` / `direction_pin:` / `limit_all_pin:` відповідних секцій YAML.

## Klipper - ESP32 як secondary MCU

Klipper ділить роботу: Raspberry Pi рахує траєкторію (Python), а мікроконтролери
виконують кроки за розкладом (C). ESP32 тут - ідеальний другий/третій MCU:
рідний WiFi не потрібен (зв'язок - дротовий USB-UART з хостом!), зате багато
GPIO, АЦП, RMT для NeoPixel, I2C для ADXL345-виміру резонансів.

### Архітектура з ESP32-довеском

| Вузол | Роль | Що на ньому |
| --- | --- | --- |
| RPi-хост | Klipper host + Moonraker + Fluidd/Mainsail | `printer.cfg`, кінематика, pressure advance, input shaping |
| Main MCU (SKR/Manta) | primary `[mcu]` | кроки XYZ/E, нагрів, вентилятори |
| ESP32 | secondary `[mcu esp32]` | ADXL345 по SPI, NeoPixel, додатковий вентилятор, кнопка, термопара |

### Прошивка ESP32 під Klipper (menuconfig)

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

### `printer.cfg` - ESP32 як другий MCU

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

Пояснення:

- **Префікс `esp32:`** у кожному піні каже Klipper, якому MCU належить пін.
  Без префікса - пін шукається на primary `[mcu]` і буде помилка.
- **`^` і `!`** - pull-up та інверсія: `^!esp32:gpio34` = підтяжка + NC-датчик.
- **ADXL345 - тільки по SPI ESP32:** I2C-режим ADXL345 Klipper не калібрує
  резонанси коректно; SPI 5 МГц, дроти < 15 см, див. резонанси в Klipper-доках.
- **USB-serial, не WiFi:** Klipper не говорить з MCU по WiFi-TCP у стабільному
  режимі - тільки дротовий serial. WiFi ESP32 у Klipper-режимі не використовується.
- **Multi-MCU homing:** кінцевик має висіти на тому ж MCU, що й відповідний мотор,
  інакше - помилка `multi-mcu homing` під час `$H`/G28.

## micro-ROS - ESP32 як ROS 2-вузол

micro-ROS садить клієнтський API ROS 2 (rclc + Micro XRCE-DDS) прямо на ESP32.
ESP32 говорить з micro-ROS-агентом (програма на ПК/RPi), а агент вже розмовляє
з рештою ROS 2-графа по DDS. Транспортів два: UDP по WiFi (зручно) або UART-serial
(надійно, без джиттера WiFi). Виконавча модель - executor: один потік крутить
таймери, сабскрайбери і сервіси по колу.

### Архітектура

| Шар | Де живе | Що робить |
| --- | --- | --- |
| ROS 2-граф (Humble/Jazzy) | ПК / RPi | `rviz`, `ros2 topic echo`, навігація Nav2 |
| micro-ROS Agent | ПК / RPi, Docker `microros/micro-ros-agent` | міст XRCE-DDS ↔ DDS: `udp4 --port 8888` або `serial --dev /dev/ttyUSB0` |
| micro-ROS node | ESP32 (ESP-IDF + компонент) | паблішить одометрію, слухає `cmd_vel`, крутить мотори |
| Транспорт | WiFi-UDP або UART | UDP - мобільність, UART - детермінізм |

### Налаштування ESP-IDF компонента

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

Агент на хості:

```bash
# UDP-агент (ESP32 по WiFi стукає на порт 8888):
docker run -it --rm --net=host microros/micro-ros-agent:rolling udp4 --port 8888 -v6
# Serial-агент (ESP32 по USB-UART):
docker run -it --rm -v /dev:/dev --privileged --net=host \
  microros/micro-ros-agent:rolling serial --dev /dev/ttyUSB0 -v6
```

### Executor - серце вузла (патерни)

| Патерн | Коли | Приклад |
| --- | --- | --- |
| Один таймер + один паблішер | маяк одометрії 20 Гц | `rclc_timer_init_default` + `rclc_executor_spin` |
| Сабскрайбер `cmd_vel` + PWM | диференціальний робот | колбек Twist → MCPWM на два мотори |
| Сервіс + екшен | калібрування / захват | `rclc_service_init_default`, стани в колбеку |
| Static executor + `sleep 10 мс` | батарейний вузол | менше прокидань, економія заряду |

> Пам'ять: тримай `rmw` буфери маленькими (`colcon.meta` - MTU 512 при UART),
> інакше ESP32 з'їсть купу PSRAM під фрагментацію XRCE.

## ESP-Drone - міні-квадрокоптер на ESP32

ESP-Drone (Espressif, порт Crazyflie) - повноцінний польотник для кімнатного
квадрика на ESP32/S2/S3 під ESP-IDF v5. Код стабілізації - з Crazyflie (GPL-3.0),
плата - проста: ESP32 + драйвер колекторних моторів + IMU MPU9250/BMI088.

### Режими і плати розширення

| Режим | Що стабілізує | Що треба |
| --- | --- | --- |
| Stabilize (attitude) | кути roll/pitch, yaw-rate | базова плата + IMU |
| Height-hold (flapper/altitude) | + висота за тиском | плата висотоміра (BMP388/LPS22) |
| Position-hold (positioning) | + XY за оптичним потоком | flow-deck: PMW3901 (optic-flow) + VL53L1x (ToF-далекомір) |
| APP control | керування зі смартфона | WiFi AP дрона + ESP-Drone APP (iOS/Android) |
| Joystick / cfclient | керування з ПК | `crazyflie-clients-python`, ESP-NOW-джойстик через ESP-BOX3 |

### Зв'язок керування

| Канал | Транспорт | Затримка | Коли |
| --- | --- | --- | --- |
| WiFi APP | UDP до AP дрона | ~20-50 мс | навчання, STEAM-демо |
| ESP-NOW джойстик | ESP-NOW 2.4 ГГц | ~5-10 мс | точніші польоти без роутера |
| cfclient (Crazyradio-сумісний) | USB-dongle → Crazyflie-протокол | ~10 мс | логи, параметри PID, телеметрія |

> Flow-deck - ключ до position-hold у кімнаті без GPS: PMW3901 дивиться вниз
> і міряє оптичний потік (зсув картинки підлоги), VL53L1x дає висоту ToF.
> Без flow-deck кімнатний дрон тримає тільки кути й висоту - XY пливе за вітром.

## INAV / Betaflight на ESP32 - чесна межа

Ні INAV, ні Betaflight не збираються під ESP32 як ціль польотника:
цілі - STM32F4/F7/H7 і AT32, цикл ПІД 8 кГц, DMA-читання gyro, DShot з точним
таймінгом. ESP32 не має потрібних DMA-ланцюжків під їхній scheduler і не
пройде жоден CI-таргет цих проєктів. Тому правильна топологія - два борти:

```text
STM32-польотник (Betaflight/INAV)  <──CRS F/SBUS/MAVLink──>  ESP32 (другий борт)
  gyro + PID 8 кГц, DShot до ESC                                GPS-логер (SD)
  OSD, failsafe, RTH                                            WiFi-шлюз до GCS
  CRSF-приймач ELRS ──TX/RX── ESP32-перехоплювач ──TX/RX── FC   CRSF-міст + LTM-ретранслятор
```

| Роль ESP32 поруч із FC | Протокол | UART | Навіщо |
| --- | --- | --- | --- |
| CRSF-міст / сніфер | CRSF 420000 8N1 | UART2 | логи каналів, ретрансляція телеметрії на землю |
| GPS-логер | NMEA/UBX 115200 | UART1 | писати трек на SD незалежно від blackbox FC |
| MAVLink-шлюз | MAVLink 57600 | UART1 + WiFi | FC → ESP32 → QGroundControl по WiFi |
| S.Port/F.Port вузол | 57600/115200 інв. | UART + інверсія | віддати напругу/струм у FrSky-приймач |
| DShot-стенд (без польоту!) | DShot через RMT | RMT TX | покрутити мотор на столі, див. MCPWM/RMT-ноту |

Деталі CRSF-парсингу, інверсії SBUS і MAVLink-heartbeat - у ноті
[12-RC-Protocols](../../../ESP32-Reference/12-Moduli-zvyazku/12-RC-Protocols.md), таймінг DShot через RMT -
у [01-Timeri-MCPWM-PCNT-RMT](../../../ESP32-Reference/07-Timeri-Son/01-Timeri-MCPWM-PCNT-RMT.md).

## Код 1 - FluidNC `config.yaml` (3 осі + TMC2209 + лазер/шпиндель)

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

Коментарі до конфігу:

- `engine: RMT` - кроки через RMT-периферію ESP32, найстабільніший таймінг;
  `pulse_us: 2` тримає сумісність із TMC2209 і зовнішніми DM542.
- `uart1 → 115200` - шина TMC; усі три драйвери на одному UART з різними
  `addr` (перемички MS1/MS2 на платі драйвера задають 0/1/2).
- `r_sense_ohms: 0.110` - звірити з написом Rsense на конкретному модулі
  (буває 0.110 або 0.220!); неправильне значення = вдвічі хибний струм.
- `limit_all_pin: gpio.34:low:pu` - кінцевик NO до землі з підтяжкою;
  для NC-датчиків - `:high`, див. GPIO-ноту.
- `must_home: true` - верстат не поїде без `$H` після вмикання; безпека перша.
- Лазерний режим окремо: `$32=1` в консолі або `laser:`-секція у новіших
  збірках FluidNC - перевірити `$I` (build info) перед гравіюванням.

## Код 2 - micro-ROS publisher на ESP-IDF (одометрія + cmd_vel)

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
    // див. [[11-Vivid/11-PowerMotion-2]] і [[07-Timeri-Son/01-Timeri-MCPWM-PCNT-RMT]]
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

> Робочий мінімум без скорочень - у репозиторії компонента:
> `examples/int32_publisher` (паблішер) і `examples/int32_subscriber`.
> Код вище - каркас під твій робот: підстав реальний `rcl_publish(&pub, …)`
> у таймері, PCNT-енкодери і MCPWM-мости з [11-PowerMotion-2](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md).

Кроки запуску зв'язки:

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

## Код 3 - CRSF-телеметрія з ESP32 до ELRS-приймача (батарея + GPS)

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

Пояснення до коду:

- **Адреса `0xC8`** - «польотник»: приймач ELRS приймає телеметрію тільки
  з цієї адреси; `0xEE` - адреса самого передавача, її не використовувати.
- **Big-endian:** багатобайтові поля CRSF - старший байт першим
  (на відміну від MAVLink/SBUS LSB), переплутаєш - висота 1123 м стане 253 м.
- **Темп 4 Гц:** батарею і GPS слати по черзі не частіше 10 Гц сумарно,
  інакше заб'єш аплінк і канали почнуть лагати.
- **Перехрест:** TX приймача → GPIO16, RX приймача → GPIO17 (як звичайний UART).

## Живлення, землі і безпека верстата/друкарки

| Вузол | Вимога | Чому |
| --- | --- | --- |
| Логіка ESP32 | 3.3 В, окремий LDO з запасом 500 мА | просідання = зрив кроків і перезапуск WebUI |
| Драйвери кроку | 12-24 В, електроліт 470+ мкФ біля кожного | гасіння зворотних викидів мотора |
| Спільна земля | одна зірка: ESP32 − драйвери − БЖ − корпус | петлі землі = хибні кінцевики і «танцюючі» координати |
| Сигнальні джгути | step/dir < 30 см, кручена пара з GND | перехресні наведення від 24 В і шпинделя |
| Шпиндель/нагрів | тільки через MOSFET/реле-модуль | GPIO дає 12 мА - мосфет без драйвера не відкриється |
| E-stop | фізична кнопка рве 24 В/220 В, не GPIO! | софтовий стоп не рятує при зависанні |
| Кінцевики | екран, NC-ланцюжок послідовно на довгих осях | обрив NC-ланцюга = аварія, а не в'їзд у раму |
| USB + 24 В одночасно | спочатку земля, потім USB; або ізольований USB-UART | різниця потенціалів палить CP2102 |

> E-stop ніколи не заводити тільки в ESP32: червоний гриб має рвати силову
> лінію контактором. GPIO-стоп - другий рубіж, не перший.

## Типові помилки

| № | Симптом | Причина | Виправлення |
| --- | --- | --- | --- |
| 1 | FluidNC: `config.yaml not found` після заливки | файл залили не в ту ФС або з BOM/табами | перезалити через WebUI → Config; YAML - тільки пробіли, UTF-8 без BOM, перевірити `$Config/Filename=` |
| 2 | FluidNC мовчить, WebUI немає | STA SSID/пароль хибні, плата не в мережі | тимчасово `access_point: true`, зайти на AP `FluidNC`, виправити STA-креденшали |
| 3 | Мотори тремтять на місці / їдуть вдвічі менше | `r_sense_ohms` не той (0.110 vs 0.220) або `microsteps` не ті | звірити Rsense на модулі, перерахувати `steps_per_mm = microsteps × кроків_мотора / мм_оберта` |
| 4 | TMC2209 не відповідає по UART | усі `addr` однакові або немає резисторів 1 кОм на зворотній лінії | роздати addr 0/1/2 перемичками MS1/MS2, впаяти 1 кОм з кожного TX драйвера в RX ESP32 |
| 5 | Кінцевик спрацьовує сам | наведення від шпинделя/24 В, немає дебаунсу | кручена пара + екран, конденсатор 10-100 нФ біля входу, NC-логіка, подалі від силових |
| 6 | GPIO34/35 «не тримають» pull-up | це only-input піни без коректного внутрішнього pull-up | зовнішній резистор 4.7-10 кОм до 3V3, див. GPIO-ноту |
| 7 | Вісь їде не туди / homing у стіну | інверсія `direction_pin` або `homing:mpos_mm` не з того краю | інвертувати пін (`gpio.25:low` ↔ `:high`) або `$3` у grbl_ESP32, перевірити `$H` на малій подачі |
| 8 | grbl_ESP32: `$H` б'ється в раму | `$23` (маска homing) або `$5` (інверсія щупів) хибні | виставити `$23` під розташування кінцевиків, `$5` під NO/NC, тестити з рукою на E-stop |
| 9 | Klipper: `Unable to connect to MCU esp32` | не той `/dev/serial/by-id/*` або плата в download-режимі | `ls /dev/serial/by-id/*` після перепрошивки, вписати свіжий ID у `[mcu esp32]`, `restart` |
| 10 | Klipper: `multi-mcu homing` / піни не тієї плати | кінцевик і мотор на різних MCU або забутий префікс `esp32:` | кінцевик пересадити на той же MCU, що й мотор; кожен пін ESP32 писати як `esp32:gpioN` |
| 11 | micro-ROS: топики не видно в `ros2 topic list` | агент не запущений або ESP32 стукає не на той IP/порт | підняти `micro-ros-agent udp4 --port 8888`, звірити IP агента і WiFi-креденшали в `menuconfig`, `-v6` логи агента |
| 12 | micro-ROS: `fragmentation` / падіння по пам'яті | MTU XRCE завеликий під UDP/WiFi або забагато паблішерів | зменшити MTU в `colcon.meta` (512 для UART), скоротити черги, static executor замість динаміки |
| 13 | ESP-Drone не тримає позицію в кімнаті | немає flow-deck або глянцева підлога без текстури | поставити PMW3901+VL53L1x deck, літати над килимом/газетою, калібрувати IMU перед вильотом |
| 14 | CRSF-телеметрія мовчить на пульті | інверсія увімкнена, переплутані TX/RX або адреса не `0xC8` | вимкнути інверсію (CRSF - пряма логіка!), перехрестити TX→RX, адреса `0xC8`, бод 420000 8N1, темп ≤ 10 Гц |

## Офіційні джерела

- [FluidNC - GitHub (прошивка, приклади config.yaml, WebUI)](https://github.com/bdring/FluidNC) - YAML-машини, RMT-степпер, TMC-драйвери, SD/Telnet/WebUI, міграція з grbl_ESP32.
- [Grbl_ESP32 - GitHub (попередник FluidNC, machine.h, $settings)](https://github.com/bdring/Grbl_Esp32) - step/dir-мапінг, 6 осей, TMC-SPI, BT/WiFi-конективіті, заява про перехід на FluidNC.
- [Klipper overview](https://www.klipper3d.org/Overview.html) - хост+MCU архітектура, `make menuconfig`, `printer.cfg`, secondary-MCU підхід.
- [Klipper - Installation (menuconfig, flash, serial by-id)](https://www.klipper3d.org/Installation.html) - покрокова прошивка MCU, визначення serial-порту, структура `printer.cfg`.
- [micro-ROS overview docs](https://micro.vulcanexus.org/docs/overview/) - XRCE-DDS міст, UDP/serial-транспорти, executor-модель, список підтриманого заліза.
- [micro_ros_espidf_component - GitHub (ESP-IDF компонент, приклади)](https://github.com/micro-ROS/micro_ros_espidf_component) - `int32_publisher`, `menuconfig`, UDP/UART-транспорти, Docker-агент.
- [ESP-Drone - GitHub (прошивка міні-дрона, flow-deck)](https://github.com/espressif/esp-drone) - stabilize/height-hold/position-hold, PMW3901+ToF deck, WiFi APP, ESP-IDF v5.
- [Betaflight setup guide](https://betaflight.com/docs/wiki/getting-started/setup-guide) - чому польотник - STM32, а ESP32 поруч - тільки міст/логер.
- [INAV - GitHub (навігаційний польотник, телеметрія)](https://github.com/iNavFlight/inav) - position-hold/RTH/waypoints на F4/F7/H7, CRSF/MAVLink/LTM-телеметрія для ESP32-моста.
- [ESP-IDF Programming Guide - ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/index.html) - RMT/MCPWM/PCNT/UART-база під усі motion-коди цієї ноти.

## Див. також

- [Home](../../../ESP32-Reference/Home.md)
- [11-PowerMotion-2](../../../ESP32-Reference/11-Vivid/11-PowerMotion-2.md)
- [06-PCA9685-MG996R-28BYJ48-TMC2209](../../../ESP32-Reference/11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.md)
- [01-Timeri-MCPWM-PCNT-RMT](../../../ESP32-Reference/07-Timeri-Son/01-Timeri-MCPWM-PCNT-RMT.md)
- [UART](../../../ESP32-Reference/04-Shini/01-UART.md)
- [12-RC-Protocols](../../../ESP32-Reference/12-Moduli-zvyazku/12-RC-Protocols.md)
- [07-SD-SDIO](../../../ESP32-Reference/04-Shini/07-SD-SDIO.md)
- [01-GPIO-oglyad](../../../ESP32-Reference/03-GPIO/01-GPIO-oglyad.md)
- [01-WiFi-STA-AP](../../../ESP32-Reference/05-Radio/01-WiFi-STA-AP.md)
- [06-FreeRTOS-Patterns](../../../ESP32-Reference/09-Proshivka/06-FreeRTOS-Patterns.md)
- [19-IMU-6-9DOF](../../../ESP32-Reference/10-Sensori/19-IMU-6-9DOF.md)
- [17-GNSS-RTK](../../../ESP32-Reference/12-Moduli-zvyazku/17-GNSS-RTK.md)
- [02-Troubleshooting-FAQ](../../../ESP32-Reference/99-Dodatki/02-Troubleshooting-FAQ.md)
- [06-Official-Sources-Modules](../../../ESP32-Reference/99-Dodatki/06-Official-Sources-Modules.md)
