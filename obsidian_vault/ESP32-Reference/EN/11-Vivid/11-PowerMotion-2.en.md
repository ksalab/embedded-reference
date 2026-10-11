---
description: Power Motion 2; shows schematics, code and tables.
title: Power Motion 2 - DRV8825, TB6600/DM542, TMC5160, SimpleFOC/BLDC/ESC
tags: [esp32, stepper, bldc, foc, drv8825, tb6600, dm542, tmc5160, esc, mcpwm]
category: Vivid
date-created: 2026-09-28
lang: en
original: 11-Vivid/11-PowerMotion-2.md
date: 2026-10-08
---


# Power Motion 2 - DRV8825, TB6600/DM542, TMC5160, SimpleFOC/BLDC/ESC

## Purpose

Second-level power drivers for ESP32: compact stepper driver DRV8825 (microstep up to 1/32, Vref),
industrial TB6600/DM542 drivers with current DIP switches for 24-48 V,
smart TMC5160 driver with SPI configuration and StallGuard,
plus BLDC/FOC/ESC overview: 3-phase bridge + encoder and why L298N does not fit BLDC.
Base: L298N/TB6612/A4988 - see [[11-Vivid/04-L298N-TB6612-A4988-Buzzer.en | L298N TB6612 A4988 Buzzer]],
servo/stepper 28BYJ48/TMC2209 - [[11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.en | PCA9685 MG996R 28BYJ48 TMC2209]],
power switches BTS7960 - [[11-Vivid/07-BTS7960-L9110S-SSR-Solenoid.en | BTS7960 L9110S SSR Solenoid]].

## Characteristics

| Driver | Motor | voltage / current | Control | Feature |
| --- | --- | --- | --- | --- |
| DRV8825 (Pololu carrier) | Bipolar stepper (NEMA14/17) | 8.2-45 V, up to 1.5 A without heatsink (2.2 A with cooling) | STEP/DIR + M0/M1/M2 | Microstep up to 1/32, Vref = I_lim/2, drop-in for A4988 |
| TB6600 | Stepper NEMA17/23/34 | 9-42 V, 0.5-4 A (DIP SW1-SW3) | STEP/DIR + ENA, DIP SW4-SW6 microstep | Opto-isolated inputs, big heatsink |
| DM542 | Stepper NEMA23/34 | 20-50 V (typically 24-48 V!), up to 4.2 A | STEP/DIR + ENA, current/microstep DIP | Industrial case, quieter than TB6600 clones |
| TMC5160 | Stepper + BLDC support | 8-60 V, up to 3 A RMS (external MOSFET optional) | SPI config + STEP/DIR | StallGuard2, StealthChop2, DcStep, CoolStep |
| SimpleFOC + 3-phase bridge | BLDC/gimbal/stepper in FOC | 8-35 V (SimpleFOCShield on DRV8313, up to 2 A/phase) | 3xPWM (6PWM) + encoder | Vector control, smoothness and torque at low RPM |
| BLDC ESC (SimonK/BLHeli) | Brushless star/delta | 2-6S LiPo, tens of amps | PPM 1-2 ms (servo signal) | Sensorless, for props; no positioning |

> Why not L298N for steppers/BLDC: bipolar L298N is a stone age (2-4 V drop, heats,
> no microstep or current limit), and BLDC generally needs a 3-phase bridge with 20+ kHz PWM and reverse feedback.

## Легенда pinandin модуля

### DRV8825 (кар'єр Pololu, 16 pin)

| Pin | Value | Type | To ESP32 | Note |
| --- | --- | --- | --- | --- |
| 1 | ENBL (ENABLE) | input, active low | GPIO26 or NC | LOW = driver on; pull-up on board |
| 2 | M0 | digital input | GPIO27 / jumper | LSB of microstep (see table) |
| 3 | M1 | digital input | GPIO14 / jumper | Middle bit of microstep |
| 4 | M2 | digital input | GPIO12 / jumper | MSB of microstep |
| 5 | RESET | input, active low | to SLEEP (jumper) | Pull HIGH, else driver sleeps |
| 6 | SLEEP | input, active low | at RESET (jumper) | HIGH = робота; LOW = sleep (current мкА) |
| 7 | STEP | edge input | GPIO25 | One pulse >=1.9 us = one microstep |
| 8 | DIR | digital input | GPIO33 | HIGH/LOW = direction |
| 9 | FAULT | output, active low | GPIO32 or NC | Overheat/overcurrent; 1.5 k resistor on board |
| 10-11 | A1/A2 (1B/1A) | power output | Motor winding A | do not switch on the fly! |
| 12-13 | B1/B2 (2A/2B) | power output | Motor winding B | Pair rings with multimeter |
| 14 | GND (logic) | ground | GND | common logic ground |
| 15 | VDD | power supply input | 3V3 | 3.3 V logic from ESP32 |
| 16 | VMOT + GND | power supply | 8.2-45 V PSU + >=47 uF electrolytic | Separate PSU, ground common with ESP32 |

table M0/M1/M2 (DRV8825):

| M0 | M1 | M2 | Microstep |
| --- | --- | --- | --- |
| LOW | LOW | LOW | Full step |
| HIGH | LOW | LOW | 1/2 |
| LOW | HIGH | LOW | 1/4 |
| HIGH | HIGH | LOW | 1/8 |
| LOW | LOW | HIGH | 1/16 |
| HIGH | LOW | HIGH | 1/32 |
| LOW | HIGH | HIGH | 1/32 |
| HIGH | HIGH | HIGH | 1/32 |

Vref: `I_lim = Vref x 2` (Rsense 0.1 Ohm). 1 A motor → Vref = 0.5 V. Turn pot with VMOT off!

### TB6600 (industrial module with DIP)

| Pin / group | Value | Type | To ESP32 | Note |
| --- | --- | --- | --- | --- |
| PUL+ / PUL- | Step pulses | opto input | PUL+ → 3V3, PUL- → GPIO25 | Can swap via GND; opto current ~10 mA |
| DIR+ / DIR- | Direction | opto input | DIR+ → 3V3, DIR- → GPIO33 | HIGH/LOW = direction |
| ENA+ / ENA- | Enable | opto input | ENA+ → 3V3, ENA- → GPIO26 | Disconnected = on (depends on revision!) |
| VCC / GND | Power supply | input | 9-42 V PSU | Electrolytic already on board; common ground |
| A+ / A-, B+ / B- | Windings | power output | Stepper motor | do not switch under voltage |
| SW1-SW3 | Current | DIP switches | 0.5-4 A per case table | Set ≤ motor rating |
| SW4-SW6 | Microstep | DIP switches | 1/1 … 1/32 | Bigger microstep = quieter and smoother |
| SW (half-current) | Half-current | DIP | ON = standstill current 50% | Less heat at idle |

### DM542 (like TB6600, enclosed)

| Pin / group | Value | Type | To ESP32 | Note |
| --- | --- | --- | --- | --- |
| PUL+/PUL-, DIR+/DIR-, ENA+/ENA- | Signals | Opto inputs | as in TB6600 | 5 V logic via resistors; 3.3 V works |
| VCC/GND | Power | input | 24-48 V PSU! | Note: 12 V gives weak torque at speed |
| A+/A−, B+/B− | Обмотки | output | Мотор | current дипами SW1-SW3 up to 4.2 but |
| SW5-SW8 | Microstep | DIP | up to 1/256 (depends on revision) | check table of your own revision |

### TMC5160 (module/BOB with SPI)

| Pin | Value | Type | To ESP32 | Note |
| --- | --- | --- | --- | --- |
| VM / GND | Power | input | 8-60 V PSU | Separate PSU + electrolytic |
| VIO | Logic | input | 3V3 | 3.3 V from ESP32 |
| STEP / DIR | Step/dir | input | GPIO25 / GPIO33 | Classic mode after SPI config |
| SCK / SDI / SDO | SPI | SPI bus | GPIO18 / GPIO23 / GPIO19 | Register configuration |
| CSN | Chip Select SPI | input CS | GPIO5 | Окремий CS at кожен TMC5160 |
| ENN | Enable, active low | input | GPIO26 | LOW = bridge on |
| DIAG0/DIAG1 | Diagnostics | output | GPIO32 or NC | StallGuard stop flag without limit switches! |
| CLK | Clocking | input | NC (internal) or GPIO | Internal 12 MHz is enough |
| OA1/OA2, OB1/OB2 | Windings | output | Motor | up to 3 A RMS without external FETs |

### SimpleFOC node: 3-phase bridge + encoder (ex. SimpleFOCShield)

| Pin / node | Value | Type | To ESP32 | Note |
| --- | --- | --- | --- | --- |
| Bridge VM / GND | Power | input | 8-35 V PSU | Gimbal motor R > 10 Ohm for Shield |
| U / V / W | 3 phases | output | BLDC windings | Phase order affects direction |
| INH_U/V/W (6PWM) | High-side switches | PWM input | GPIO25/26/27 | PWM frequency 20-30 kHz |
| INL_U/V/W (6PWM) | Low-side switches | PWM input | GPIO32/33/14 | Dead time in hardware |
| AS5600 SDA/SCL | I2C encoder | I2C | GPIO21 / GPIO22 | address 0x36, magnet over chip! |
| SPI encoder (AS5048) | CS/SCK/MOSI/MISO | SPI | GPIO5/18/23/19 | More precise and faster than I2C |
| ACS712/INA | Phase current | Analog | GPIO34/35 (ADC) | for FOC current loop |

> L298N has no place in this circuit: 2 bridges instead of 3 phases, 2-4 V drop, no fast PWM or current sense.
> Sensorless BLDC is open loop only (spinner/gimbal demo), no positioning.

## Wiring diagram

| ESP32 | DRV8825 | TB6600/DM542 | TMC5160 | BLDC bridge (FOC) |
| --- | --- | --- | --- | --- |
| 3V3 | VDD | PUL+/DIR+/ENA+ | VIO | - (bridge logic from own regulator) |
| GND | Logic GND + VMOT GND | Signal GND | GND | GND (common with bridge PSU!) |
| GPIO25 | STEP | PUL− | STEP | INH_U (PWM) |
| GPIO33 | DIR | DIR− | DIR | INH_V (PWM) |
| GPIO26 | ENBL | ENA− | ENN | INH_W (PWM) |
| GPIO27/14/12 | M0/M1/M2 | - (DIP on case) | - (SPI registers) | - |
| GPIO18/23/19/5 | - | - | SCK/SDI/SDO/CSN | - (SPI for AS5048 encoder) |
| GPIO21/22 | - | - | - | AS5600 SDA/SCL |
| PSU 8-45 in | VMOT (+47 мкФ!) | - | - | - |
| PSU 24-48 in | - | VCC TB6600/DM542 | - | - |
| PSU 8-60 in | - | - | VM | - |
| PSU 8-35 in | - | - | - | VM моста |

Common grounds everywhere mandatory; power ground as star to PSU, see [[02-Power-Supply/01-Power-Rails.en | Power Supply Rails]].
ШІМ/таймери - [[EN/07-Timers/01-Timers-MCPWM-PCNT-RMT.en]], UART for setup - [[04-Interfaces/01-UART.en | UART]].

### ASCII-schem

```text
ESP32 DevKit              DRV8825 (NEMA17, 12В)
------------              ---------------------
3V3 ────────────────────► VDD (логіка)
GND ────────────────────► GND (логіка) + GND VMOT (зірка!)
GPIO25 ─────────────────► STEP (імпульс ≥1.9 мкс)
GPIO33 ─────────────────► DIR
GPIO26 ─────────────────► ENBL (або NC)
GPIO27/14/12 ───────────► M0/M1/M2 (мікрокрок, див. таблицю)
GPIO32 ◄───────────────── FAULT (опційно)
RESET ◄──перемичка──► SLEEP (обидва HIGH!)
[БЖ 12В] ───────────────► VMOT + GND, електроліт ≥47 мкФ біля плати!
A1/A2, B1/B2 ───────────► обмотки мотора (НЕ чіпати під напругою!)
Vref = I_lim/2 (мотор 1А → 0.5В, крутити при ВИМКНЕНОМУ VMOT)

ESP32 DevKit              TB6600 / DM542 (NEMA23, 24-48В!)
------------              -------------------------------
3V3 ────────────────────► PUL+, DIR+, ENA+ (спільний + оптопар)
GPIO25 ─────────────────► PUL- (крок)
GPIO33 ─────────────────► DIR- (напрям)
GPIO26 ─────────────────► ENA- (дозвіл; на частині ревізій NC=ON)
[БЖ 24-48В] ────────────► VCC + GND (земля спільна з ESP32!)
A+/A-, B+/B- ───────────► обмотки мотора
SW1-SW3: струм ≤ номіналу мотора; SW4-SW6: мікрокрок (1/8..1/32)
УВАГА: 12В на швидкості дасть провал моменту - беріть 24-48В!

ESP32 DevKit              TMC5160 (SPI-конфіг + StallGuard)
------------              -------------------------------
3V3 ────────────────────► VIO
GND ────────────────────► GND
GPIO18 ─────────────────► SCK
GPIO23 ─────────────────► SDI
GPIO19 ◄───────────────── SDO
GPIO5 ──────────────────► CSN (окремий на кожен драйвер!)
GPIO25 ─────────────────► STEP
GPIO33 ─────────────────► DIR
GPIO26 ─────────────────► ENN (LOW=ON)
GPIO32 ◄───────────────── DIAG0 (StallGuard-флаг)
[БЖ 12-48В] ────────────► VM + GND
Спочатку SPI-конфіг (струм, StealthChop), потім STEP/DIR!

ESP32 DevKit              SimpleFOC: міст + енкодер (BLDC)
------------              -------------------------------
GND ═════════════════════ GND моста (товстий провід, зірка!)
GPIO25/26/27 ───────────► INH_U/V/W (верхні ключі, 20-30 кГц)
GPIO32/33/14 ───────────► INL_U/V/W (нижні ключі)
GPIO21 ─────────────────► AS5600 SDA (0x36) / або SPI-енкодер
GPIO22 ─────────────────► AS5600 SCL
[БЖ 12-24В] ────────────► VM моста
U/V/W ──────────────────► 3 фази BLDC (порядок=напрям)
L298N сюди НЕ ставити: 2 мости ≠ 3 фази, падіння 2-4В, немає струму!
```

### Mermaid

```mermaid
graph LR
  ESP32["ESP32<br/>STEP/DIR + SPI + PWM"]
  ESP32 -->|GPIO25 STEP| DRV["DRV8825<br/>Vref=I/2"]
  ESP32 -->|GPIO33 DIR| DRV
  ESP32 -->|M0/M1/M2| DRV
  ESP32 -->|PUL-/DIR-/ENA-| TB["TB6600/DM542<br/>24-48V, дипи"]
  ESP32 -->|SPI GPIO18/23/19/5| TMC["TMC5160<br/>StallGuard"]
  TMC -->|DIAG0| ESP32
  ESP32 -->|6×PWM 20-30кГц| BR["3-фазний міст<br/>U/V/W"]
  ENC["Енкодер<br/>AS5600/AS5048"] -->|I2C/SPI| ESP32
  BR -->|U/V/W| BLDC((BLDC мотор))
  PSU1(["БЖ 12В"]) --> DRV
  PSU2(["БЖ 24-48В"]) --> TB
  PSU3(["БЖ 8-35В"]) --> BR
```

![[assets/img/powermotion-bldc-foc-scheme.png]]
*Fig. DRV8825/TB6600/TMC5160 and FOC BLDC node with encoder. Space below schematic - see [[assets/README]].*

## Code ESP-IDF

```c
#include "driver/gpio.h"
#include "driver/mcpwm_prelude.h"
#include "driver/spi_master.h"
#include "esp_rom_sys.h"

// --- STEP/DIR для DRV8825 / TB6600 / DM542 (MCPWM-оператор як генератор кроків) ---
#define PIN_STEP 25
#define PIN_DIR  33
#define PIN_ENA  26

void stepper_step(gpio_num_t dir, int steps, int step_us)
{
    gpio_set_level(PIN_DIR, dir);
    esp_rom_delay_us(5);
    for (int i = 0; i < steps; i++) {
        gpio_set_level(PIN_STEP, 1);
        esp_rom_delay_us(step_us);   // DRV8825: ≥1.9 мкс
        gpio_set_level(PIN_STEP, 0);
        esp_rom_delay_us(step_us);
    }
}

// --- TMC5160: запис регістра по SPI (приклад: IHOLD_IRUN) ---
#define TMC_HOST SPI2_HOST
static spi_device_handle_t tmc;

void tmc5160_write(uint8_t addr, uint32_t val)
{
    uint8_t tx[5] = {(uint8_t)(addr | 0x80),
                     (val >> 24) & 0xFF, (val >> 16) & 0xFF,
                     (val >> 8) & 0xFF, val & 0xFF};
    spi_transaction_t t = {.length = 40, .tx_buffer = tx};
    spi_device_transmit(tmc, &t);
}

void app_main(void)
{
    gpio_config_t o = {.pin_bit_mask = (1ULL << PIN_STEP) | (1ULL << PIN_DIR) | (1ULL << PIN_ENA),
                       .mode = GPIO_MODE_OUTPUT};
    gpio_config(&o);
    gpio_set_level(PIN_ENA, 0);  // DRV8825 ENBL active low; TB6600 ENA- до GND-логіки
    stepper_step(1, 1600, 500);  // 1/8 мікрокрок: 1600 імп/об для 200-крокового мотора

    // SPI для TMC5160: SCK=18, MOSI=23, MISO=19, CS=5, 1 МГц, mode 3
    spi_bus_config_t bus = {.mosi_io_num = 23, .miso_io_num = 19, .sclk_io_num = 18,
                            .quadwp_io_num = -1, .quadhd_io_num = -1};
    spi_bus_initialize(TMC_HOST, &bus, SPI_DMA_DISABLED);
    spi_device_interface_config_t dev = {.clock_speed_hz = 1000000, .mode = 3,
                                         .spics_io_num = 5, .queue_size = 1};
    spi_bus_add_device(TMC_HOST, &dev, &tmc);
    tmc5160_write(0x10, 0x00071F02);  // IHOLD_IRUN: приклад, біти за даташитом!
    // Далі: GCONF (StealthChop), TPOWERDOWN, COOLCONF, StallGuard-поріг SGT.
}
```

## Code Arduino

```cpp
// Один скетч для DRV8825 / TB6600 / DM542 (STEP/DIR однакові!)
const int PIN_STEP = 25, PIN_DIR = 33, PIN_ENA = 26;

void step_move(bool dir, int steps, int us) {
  digitalWrite(PIN_DIR, dir);
  delayMicroseconds(5);
  for (int i = 0; i < steps; i++) {
    digitalWrite(PIN_STEP, HIGH);
    delayMicroseconds(us);   // DRV8825 ≥2 мкс; TB6600 ≥2.5 мкс
    digitalWrite(PIN_STEP, LOW);
    delayMicroseconds(us);
  }
}

void setup() {
  pinMode(PIN_STEP, OUTPUT); pinMode(PIN_DIR, OUTPUT); pinMode(PIN_ENA, OUTPUT);
  digitalWrite(PIN_ENA, LOW);  // увімкнути міст (перевірити полярність ENA своєї плати!)
  step_move(1, 1600, 500);     // оберт при 1/8 для 200-крокового
}

// --- TMC5160 через бібліотеку TMCStepper ---
#include <TMCStepper.h>
#include <SPI.h>
#define CS_PIN 5
TMC5160Stepper tmc(CS_PIN, 0.075f);  // Rsense 0.075 Ом на конкретній платі!
void setup_tmc() {
  SPI.begin(18, 19, 23, CS_PIN);
  tmc.begin();
  tmc.toff(4); tmc.blank_time(24);
  tmc.rms_current(1200);       // 1.2 А RMS
  tmc.microsteps(16);
  tmc.en_spreadCycle(false);   // StealthChop
  tmc.sgthrs(100);             // StallGuard-поріг (підібрати!)
  // DIAG0 → кінцевик: attachInterrupt(32, on_stall, RISING)
}

// --- SimpleFOC BLDC (відкритий контур мінімум) ---
#include <SimpleFOC.h>
BLDCDriver3PWM driver(25, 26, 27, 12);  // INH_U/V/W + enable
void setup_foc() {
  driver.voltage_power_supply = 12;
  driver.voltage_limit = 6;             // гімбал-мотор! не 12!
  driver.init();
  // Закритий контур: MagneticSensorI2C sensor = MagneticSensorI2C(0x36);
  // BLDCMotor motor(11); motor.linkDriver(&driver); motor.linkSensor(&sensor);
}
```

## Code MicroPython

```python
from machine import Pin, SPI
import time

STEP, DIR, ENA = Pin(25, Pin.OUT), Pin(33, Pin.OUT), Pin(26, Pin.OUT)
ENA.value(0)  # увімкнути міст (перевірити полярність плати!)

def move(steps, us=500, direction=1):
    DIR.value(direction)
    time.sleep_us(5)
    for _ in range(steps):
        STEP.value(1); time.sleep_us(us)
        STEP.value(0); time.sleep_us(us)

move(1600)  # оберт при 1/8

# --- TMC5160: читання регістра по SPI (адреса без бітів запису) ---
spi = SPI(2, baudrate=1000000, polarity=1, phase=1,  # mode 3!
          sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(5, Pin.OUT); cs.value(1)

def tmc_read(addr):
    cs.value(0)
    spi.write(bytes([addr & 0x7F, 0, 0, 0, 0]))  # перший запит - холостий
    cs.value(1); cs.value(0)
    spi.write(bytes([addr & 0x7F])); resp = spi.read(4)
    cs.value(1)
    return int.from_bytes(resp, "big")

print("GCONF:", hex(tmc_read(0x00)))
# StallGuard-результат - регістр SG_RESULT, поріг SGT підбирається під механіку!

# --- BLDC ESC (PPM 1-2 мс, як серво 50 Гц) ---
from machine import PWM
esc = PWM(Pin(25), freq=50)
esc.duty_ns(1000000)  # 1 мс = мінімум/арм; ЗНЯТИ ПРОПЕЛЕР!
time.sleep(2)
esc.duty_ns(1500000)  # середній газ для тесту без навантаження
```

### VESC vs SimpleFOC: ready controller or own bridge

| Parameter | VESC (ready controller) | SimpleFOC + own bridge |
| --- | --- | --- |
| What it is | firmware+hardware (4-12S, 50-100A) | library + DRV8313/8301 bridge |
| Setup | VESC Tool (GUI, motor auto-detect!) | code + manual calibration |
| Price | $50-150 per channel | $10-20 per channel |
| Telemetry | CAN/USB out of box | whatever you code (UART/CAN) |
| When | Eskate/bike/robot - ride tomorrow | Gimbal/drone/arm - own form factor |

```text
Зв'язка з ESP32: VESC ←→ UART/PPM/CAN (команди газу + телеметрія струму/обертів);
ESP32 тут - верхній рівень (пульт/автопілот), FOC рахує сам VESC.
```

### TMC2226 - тихий driver with UART

| Parameter | TMC2226 |
| --- | --- |
| Current | up to 2 A RMS, low RDS(on) MOSFET |
| Режими | StealthChop (тихо) + SpreadCycle (момент) |
| Control | STEP/DIR + UART (current, microstep up to 1/256 with interpolation) |
| power supply | VM 4.75-29 in, VIO 3.3 in |
| When to use | Instead of TMC2209 where it overheats: same StepStick footprint, cooler key |

> TMC2226 vs TMC2209: pin-compatible upgrade; UART address and StealthChop configure the same, no Vref trim needed with UART current control.

![[assets/img/tmc2226-uart-scheme.png]]
*Fig. TMC2226: VM with capacitor, mandatory 3.3 V VIO, STEP/DIR + UART.*

## Common issues

1. **Vref trimmed with VMOT off** → current spike, driver death. Enable VMOT, set Vref, then enable.
2. **DRV8825 RESET/SLEEP floating** → driver silent. Join RESET↔SLEEP (both HIGH), else sleeps by default.
3. **Motor switched on the fly** → key explosion. Any A/B wires only with VMOT off.
4. **No electrolytic on VMOT** → resets on LC spikes, esp. on long wires. ≥47 uF near board, short pins.
5. **TB6600/DM542 on 12 V at speed** → torque collapse. Steppers need 24-48 V: torque at RPM grows with voltage.
6. **DIP current above motor rating** → 100°C+ hot motor. SW1-SW3 ≤ rating; standstill half-current ON.
7. **TMC5160 stepped at once without SPI config** → jerks/overheat. First current, StealthChop, SGT threshold, then motion.
8. **StallGuard without calibration** → false trips. SGT tuned to speed/voltage/mechanics of each node.
9. **L298N on BLDC/NEMA23 stepper** → heater instead of driver. L298N: 2-4 V drop, no microstep, only 2 bridges.
10. **Expecting positioning from sensorless BLDC** → open loop holds no angle. Positioning needs AS5600/AS5048 + FOC loop.
11. **ESC armed with prop** → injury. First arm without prop, 1 ms minimum, check direction with marker.
12. **TMC2226 logic from VM without VIO** → silent on UART. 3.3 V VIO from ESP32 mandatory, even if VM is 24 V.

## Official sources

- [DRV8825 - carrier with photo and M0-M2 table (Pololu)](https://www.pololu.com/product/2133) - Vref = I/2, 8.2-45 V, 47 uF LC guard.
- [TB6612 - guide with code (Adafruit Learn)](https://learn.adafruit.com/adafruit-tb6612-h-bridge-dc-stepper-motor-driver-breakout) - bridges, PWM, how it differs from L298N.
- [L298N + ESP32 - tutorial with code (RNT)](https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/) - speed/direction, why it is base but not final.
- [SimpleFOC - documentation with code (SimpleFOC)](https://docs.simplefoc.com/bldcmotor) - BLDCDriver, encoders, FOC loops.
- [ESP-IDF SPI Master - documentation with code (Espressif)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html) - bus for TMC5160 configuration.

## See also

- [[Home.en | Home]]
- [[11-Vivid/04-L298N-TB6612-A4988-Buzzer.en | L298N TB6612 A4988 Buzzer]]
- [[11-Vivid/06-PCA9685-MG996R-28BYJ48-TMC2209.en | PCA9685 MG996R 28BYJ48 TMC2209]]
- [[11-Vivid/07-BTS7960-L9110S-SSR-Solenoid.en | BTS7960 L9110S SSR Solenoid]]
- [[03-GPIO/01-GPIO-Overview.en | GPIO Overview]]
- [[03-GPIO/04-Interrupts-PWM.en | Interrupts / PWM]]
- [[EN/07-Timers/01-Timers-MCPWM-PCNT-RMT.en]]
- [[04-Interfaces/01-UART.en | UART]]
- [[04-Interfaces/02-SPI.en | SPI]]
- [[04-Interfaces/03-I2C.en | I2C]]
- [[02-Power-Supply/01-Power-Rails.en | Power Supply Rails]]
- [[99-Additions/02-Troubleshooting-FAQ.en | Troubleshooting FAQ]]
