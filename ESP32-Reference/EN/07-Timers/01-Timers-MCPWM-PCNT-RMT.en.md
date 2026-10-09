---
description: Explains ESP32 hardware timers, MCPWM, PCNT and RMT with WS2812 timings and motor bridges; shows schematics, code and tables.
category: Timeri
title: Timers MCPWM PCNT RMT
tags: [esp32, timer, mcpwm, pcnt, rmt, neopixel, encoder]
date-created: 2026-09-27
date: 2026-10-09
lang: en
original: 07-Timers/01-Timeri-MCPWM-PCNT-RMT.md
---

# Timers / MCPWM / PCNT / RMT

![[assets/img/placeholder.png]]

Four hardware blocks: **hw-timer** (precise intervals), **MCPWM** (motors), **PCNT** (encoder), **RMT** (NeoPixel/IR).

> [!info] Do not confuse with LEDC
> [[03-GPIO/04-Interrupts-PWM.en | LEDC]] - simple PWM (LED, servo). MCPWM - dead-time, fault, 3 phases for BLDC/bridge.

## Purpose

Timers / MCPWM / PCNT / RMT - Block overview; Connection table; RMT-coding WS2812: timings + code. Four hardware blocks: hw-timer (precise intervals), MCPWM (motors), PCNT (encoder), RMT (NeoPixel/IR). [[EN/03-GPIO/04-Interrupts-PWM.en]] - simple PWM (LED, servo). MCPWM - dead-time, fault, 3 phases for BLDC/bridge.

## Block overview

| Block | Channels | Frequency | Application |
| --- | --- | --- | --- |
| HW Timer | 4x 64-bit | 80 MHz / divider | precise poll, timeout |
| MCPWM | 2 modules x 3 PWM | up to 40 MHz | DC motor, servo bridge, BLDC |
| PCNT | 8 counters | up to 40 MHz | quadrature encoder with no CPU |
| RMT | 8 TX/RX channels | 1 ns resolution | WS2812 NeoPixel, IR NEC |

## Connection table

| ESP32 | Device | Block |
| --- | --- | --- |
| GPIO18/19 | L298N IN1/IN2 + ENA | MCPWM 20 kHz |
| GPIO34/35 | encoder A/B | PCNT |
| GPIO23 | WS2812 DIN (through 330 Ohm) | RMT |
| 5V/GND | motor/strip power supply | common GND! |

**Arduino (hw-timer + RMT NeoPixel):**

```cpp
#include <Adafruit_NeoPixel.h>
Adafruit_NeoPixel px(8, 23, NEO_GRB + NEO_KHZ800);
volatile bool tick = false;
hw_timer_t *t = NULL;
void IRAM_ATTR onT() { tick = true; }
void setup() {
  px.begin();
  t = timerBegin(0, 80, true);  // 1 мкс тік
  timerAttachInterrupt(t, &onT, true);
  timerAlarmWrite(t, 1000000, true); timerAlarmEnable(t);
}
void loop() {
  if (tick) { tick = false; px.fill(px.Color(0, 50, 0)); px.show(); }
}
```

**ESP-IDF (MCPWM + PCNT):**

```c
// MCPWM: mcpwm_new_timer + mcpwm_new_operator + comparator + generator
// PCNT: pcnt_new_unit + pcnt_unit_add_watch_points, приклад pulse_count_event
// RMT TX: rmt_new_tx_channel + rmt_new_bytes_encoder (ws2812 example)
```

**MicroPython:**

```python
from machine import Timer, Pin
from neopixel import NeoPixel
np = NeoPixel(Pin(23), 8)
tim = Timer(0)
tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: print("tick"))
np[0] = (0, 50, 0); np.write()
# енкодер: esp32.PCNT у IDF-білдах
```

## RMT-coding WS2812: timings + code

WS2812 (NeoPixel) - 800 kHz, 1 wire, a bit is coded by **high-level duration**. RMT generates these pulses in hardware - the CPU is free.

| Symbol | T0H / T1H (high) | T0L / T1L (low) | Period | Tolerance |
| --- | --- | --- | --- | --- |
| `0` | 0.35 us (220-380 ns) | 0.90 us | 1.25 us | ±150 ns |
| `1` | 0.90 us (580-1000 ns) | 0.35 us | 1.25 us | ±150 ns |
| RESET | low > 50 us (new chips - > 280 us) | - | - | hold 80+ us |

Bit order: **GRB**, most significant bit first. Strip power is 5 V, DIN through **330 Ohm**, first pixel close (<30 cm) or through a 3.3 to 5 V level-shifter. A **1000 uF** electrolytic at the strip start is mandatory (see [[02-Power-Supply/01-Power-Rails.en | Power supply rails]]).

**ESP-IDF (RMT bytes-encoder, IDF 5.x):**

```c
#include "driver/rmt_tx.h"
// Таймінги 800 кГц, роздільність 10 МГц (тік 100 нс):
// T0: high=3 (0.3 мкс), low=9 (0.9 мкс); T1: high=9, low=3; reset=800 (80 мкс)
rmt_channel_handle_t led_ch;
rmt_bytes_encoder_handle_t enc;
void ws_init(gpio_num_t pin, int n) {
    rmt_tx_channel_config_t cc = {.gpio_num = pin, .clk_src = RMT_CLK_SRC_DEFAULT,
        .resolution_hz = 10*1000*1000, .mem_block_symbols = 64, .trans_queue_depth = 4};
    rmt_new_tx_channel(&cc, &led_ch);
    rmt_bytes_encoder_config_t ec = {
        .bit0 = {.level0 = 1, .duration0 = 3, .level1 = 0, .duration1 = 9},
        .bit1 = {.level0 = 1, .duration0 = 9, .level1 = 0, .duration1 = 3},
        .flags.msb_first = 1};
    rmt_new_bytes_encoder(&ec, &enc);
    rmt_enable(led_ch);
}
void ws_show(uint8_t *grb, int n) {
    rmt_transmit_config_t tc = {.loop_count = 0};
    rmt_transmit(led_ch, enc, grb, n * 3, &tc);
    rmt_tx_wait_all_done(led_ch, 1000);  // + reset-пауза окремо 100 мкс
}
```

**Arduino (no library, through the IDF RMT driver):**

```cpp
#include "driver/rmt.h"
#define WS_PIN 23
// Канал 0, дільник 8: тік 100 нс при 80 МГц APB
void wsRaw(const uint8_t *grb, int n) {
  rmt_config_t c = {};
  c.rmt_mode = RMT_MODE_TX; c.channel = RMT_CHANNEL_0;
  c.gpio_num = (gpio_num_t)WS_PIN; c.clk_div = 8; c.mem_block_num = 1;
  c.tx_config.loop_en = false; c.tx_config.idle_level = RMT_IDLE_LEVEL_LOW;
  c.tx_config.idle_output_en = true;
  rmt_config(&c); rmt_driver_install(c.channel, 0, 0);
  // далі: розкласти кожен біт у rmt_item32_t {3,1,9,0} / {9,1,3,0}, rmt_write_items + reset 80 мкс
}
```

**MicroPython (NeoPixel - the same RMT inside):**

```python
from machine import Pin
from neopixel import NeoPixel
np = NeoPixel(Pin(23), 8)
np[0] = (0, 50, 0)   # GRB всередині бібліотеки!
np.write()
# Увага: WiFi + довга стрічка (>200 пікселів) = просадка 5В -> перший піксель "червонить".
# Лікування: інжекція живлення кожні 50-100 пікселів, спільний GND.
```

> [!warning] WS2812 vs SK6812 vs WS2815
> SK6812 - same timings, has RGBW. WS2815 - 12 V (long lines, lower brightness). NeoPixel/FastLED libraries fit all three, but the RESET duration for new revisions became 280 us - old code with 50 us may flicker.

## PCNT + quadrature encoder (with direction)

An encoder gives 2 signals A/B shifted by 90 degrees. PCNT counts pulses **with no CPU involved** and records direction.

| Event | A | B | Direction |
| --- | --- | --- | --- |
| A rises with B=0 | up | 0 | forward (+1) |
| A rises with B=1 | up | 1 | backward (-1) |
| B broken | - | floating | counts one way - check the cable! |

Pull-ups: enable built-in pull-ups, 10-100nF capacitors on A/B near the ESP32 cut ringing (see [[03-GPIO/03-Pull-Ups-Levels.en | Pull-ups]]).

**ESP-IDF (PCNT, IDF 5.x):**

```c
#include "driver/pulse_cnt.h"
pcnt_unit_handle_t pcnt;
void enc_init(gpio_num_t a, gpio_num_t b) {
    pcnt_unit_config_t u = {.low_limit = -10000, .high_limit = 10000};
    pcnt_new_unit(&u, &pcnt);
    pcnt_chan_config_t ca = {.edge_gpio_num = a, .level_gpio_num = b};
    pcnt_channel_handle_t chA; pcnt_new_channel(pcnt, &ca, &chA);
    // A: на зростанні +1 якщо B низький, -1 якщо B високий
    pcnt_channel_set_edge_action(chA, PCNT_CHANNEL_EDGE_ACTION_INCREASE,
                                       PCNT_CHANNEL_EDGE_ACTION_DECREASE);
    pcnt_channel_set_level_action(chA, PCNT_CHANNEL_LEVEL_ACTION_KEEP,
                                        PCNT_CHANNEL_LEVEL_ACTION_INVERSE);
    pcnt_unit_add_watch_points(pcnt, (int[]){-1000, 0, 1000}, 3, 0);
    pcnt_unit_enable(pcnt); pcnt_unit_start(pcnt);
}
int pos = 0;
void enc_poll(void) { pcnt_unit_get_count(pcnt, &pos); }
```

**Arduino (PCNT through interrupts - simple option with no driver):**

```cpp
#define EA 34
#define EB 35
volatile long pos = 0;
void IRAM_ATTR onA() { pos += digitalRead(EB) ? -1 : 1; }
void setup() {
  pinMode(EA, INPUT_PULLUP); pinMode(EB, INPUT_PULLUP);
  attachInterrupt(EA, onA, RISING);
  Serial.begin(115200);
}
void loop() { Serial.println(pos); delay(200); }
```

**MicroPython:**

```python
from machine import Pin
pos = 0
pa, pb = Pin(34, Pin.IN, Pin.PULL_UP), Pin(35, Pin.IN, Pin.PULL_UP)
def onA(p):
    global pos
    pos += -1 if pb.value() else 1
pa.irq(onA, Pin.IRQ_RISING)
```

More about encoder mechanics - [[10-Sensors/14-DS3231-Encoder-Keypad-Joystick.en | Encoder Keypad]].

## MCPWM complementary + deadtime for a bridge

A half-bridge (H-bridge leg): the high and low transistors are driven by **complementary** signals. Without a pause (dead-time) both are open at once for ~50-200 ns = **shoot-through current** = smoke. MCPWM inserts dead-time in hardware.

| Parameter | Recommendation |
| --- | --- |
| Bridge frequency | 20 kHz (above hearing, moderate losses) |
| Dead-time MOSFET (IRFZ44N + driver) | 500-1000 ns |
| Dead-time IGBT | 1-3 us |
| Output | GPIO18 (PWMH) + GPIO19 (PWML) through a driver (IR2104 / TB6612) - not directly to gates! |

```text
PWMH  __--__--__              (верхній key)
           ^^ dead-time: обидва закриті
PWML  --__--__--__            (нижній key, інверсія + зсув)
```

**ESP-IDF (MCPWM + dead-time, IDF 5.x):**

```c
#include "driver/mcpwm_timer.h"
#include "driver/mcpwm_operator.h"
#include "driver/mcpwm_cmpr.h"
#include "driver/mcpwm_gen.h"
mcpwm_timer_handle_t t; mcpwm_oper_handle_t op;
mcpwm_cmpr_handle_t cmp; mcpwm_gen_handle_t h, l;
void bridge_init(void) {
    mcpwm_timer_config_t tc = {.group_id = 0, .clk_src = MCPWM_TIMER_CLK_SRC_DEFAULT,
        .resolution_hz = 10000000, .period_ticks = 500, .count_mode = MCPWM_TIMER_COUNT_MODE_UP};
    mcpwm_new_timer(&tc, &t);                       // 10 МГц / 500 = 20 кГц
    mcpwm_operator_config_t oc = {.group_id = 0};
    mcpwm_new_operator(&oc, &op);
    mcpwm_operator_connect_timer(op, t);
    mcpwm_comparator_config_t cc = {.flags.update_cmp_on_tez = true};
    mcpwm_new_comparator(op, &cc, &cmp);
    mcpwm_comparator_set_compare_value(cmp, 250);   // 50%
    mcpwm_generator_config_t gh = {.gen_gpio_num = 18}, gl = {.gen_gpio_num = 19};
    mcpwm_new_generator(op, &gh, &h); mcpwm_new_generator(op, &gl, &l);
    // H: високий при TEZ, низький при CMP; L: інверсія
    mcpwm_generator_set_action_on_timer_event(h, MCPWM_GEN_TIMER_EVENT_ACTION(MCPWM_TIMER_DIRECTION_UP, MCPWM_TIMER_EVENT_EMPTY, MCPWM_GEN_ACTION_HIGH));
    mcpwm_generator_set_action_on_compare_event(h, MCPWM_GEN_COMPARE_EVENT_ACTION(MCPWM_TIMER_DIRECTION_UP, cmp, MCPWM_GEN_ACTION_LOW));
    mcpwm_generator_set_action_on_timer_event(l, MCPWM_GEN_TIMER_EVENT_ACTION(MCPWM_TIMER_DIRECTION_UP, MCPWM_TIMER_EVENT_EMPTY, MCPWM_GEN_ACTION_LOW));
    mcpwm_generator_set_action_on_compare_event(l, MCPWM_GEN_COMPARE_EVENT_ACTION(MCPWM_TIMER_DIRECTION_UP, cmp, MCPWM_GEN_ACTION_HIGH));
    // DEAD-TIME 800 нс обом фронтам:
    mcpwm_dead_time_config_t dt = {.posedge_delay_ticks = 8, .negedge_delay_ticks = 8};
    mcpwm_generator_set_dead_time(h, h, &dt);  // тік 100 нс при 10 МГц
    mcpwm_generator_set_dead_time(l, l, &dt);
    mcpwm_timer_enable(t); mcpwm_timer_start_stop(t, MCPWM_TIMER_START_NO_STOP);
}
```

**Arduino:** use the same IDF API right in the sketch (available through `driver/mcpwm_*`), or the `ESP32Servo`/LEDC library for simple bridges like [[11-Vivid/04-L298N-TB6612-A4988-Buzzer.en | Motor drivers]] - but there do dead-time manually with a pause, which is less reliable.

**MicroPython:** there is no MCPWM module - for a bridge take a ready driver TB6612/L298N (two direction GPIOs + one PWM), the driver provides dead-time itself.

> [!danger] Bridge with no driver = burnt switches
> ESP32 GPIO gives neither the current/voltage for MOSFET gates nor guarantees software dead-time under WiFi interrupts. Always: driver (IR2104/FAN7388/TB6612) + dead-time in MCPWM + capacitors on the bridge power supply.

### Mermaid: what to take for the task

```mermaid
flowchart TB
    Q[Need timing] --> WHAT2{What exactly?}
    WHAT2 -->|Precise period/interrupt| GPT[General timer]
    WHAT2 -->|Motor/BLDC| MCPWM[Operators + dead-time!]
    WHAT2 -->|Count pulses| PCNT[PCNT + glitch filter]
    WHAT2 -->|WS2812/IR protocol| RMT[TX clock strip]
    MCPWM --> DT{Shoot-through current?}
    DT -->|Risk| DEAD[Dead-time 1-2 us mandatory!]
```

## Common issues

| # | Issue | Why it is bad | How to do it right |
| --- | --- | --- | --- |
| 1 | MCPWM with no dead-time | Shoot-through current, smoke | 1-2 us pause |
| 2 | PCNT with no filter | Counts ringing | Enable glitch filter |
| 3 | RMT as GPIO bit-bang | Jitter | Hardware RMT channel |
| 4 | Heavy timer ISR | Period breakdown | Flag + task |
| 5 | Prescaler "by eye" | Wrong frequency | Calculate: 80MHz / div / ticks |

## Official sources

- [GPTimer / MCPWM / PCNT / RMT (ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gptimer.html) - timer drivers.
- [MCPWM Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/mcpwm.html) - operators, dead-time.

## See also

- [[EN/Home.en]]
- [[EN/01-Hardware/01-ESP32-Classic.en]]
- [[03-GPIO/04-Interrupts-PWM.en | Interrupts and PWM]]
- [[11-Vivid/03-NeoPixel-Servo-Rele-MOSFET.en | LED NeoPixel]]
- [[03-GPIO/04-Interrupts-PWM.en | Buttons and encoders]]
- [[11-Vivid/04-L298N-TB6612-A4988-Buzzer.en | Motor drivers]]
- [[07-Timers/02-WDT.en | WDT]]
