---
title: DIY instruments for ESP32 - AD9833, GM328, multiplexers, Flash (DIY Instruments)
description: This module covers a number of powerful but economical digital and analog modules that can be used to create professional measuring instruments, signal generators,...; shows schematics, code and tables.
tags: [esp32, diy, instruments, ad9833, gm328, cd74hc4067, ds2482, sc16is750, w25q32, qi]
category: Moduli
lang: en
date-created: 2026-09-29
date: 2026-10-10
original: 12-Moduli-zvyazku/24-DIY-Instruments.md
---

# DIY instruments for ESP32 (AD9833, GM328, multiplexers, Flash)

![[assets/img/diy-instruments-ad9833-scheme.png|600]]

> [!info]
> This document covers popular modules for creating external instruments with ESP32. Each module is described from the point of view of connection, characteristics and common errors.

## Purpose

This module covers a number of powerful but economical digital and analog modules that can be used to create professional measuring instruments, signal generators, monitoring and other DIY projects on ESP32. All modules are chosen per the "size/price/functionality" principle and have good support in ESP-IDF, Arduino and MicroPython.

Modules covered:

- **AD9833** - DDS sine/triangle/square generator up to 12.5 MHz over SPI
- **GM328** - transistor tester with beta, HFE, continuity and other parameter measurement
- **CD74HC4067** - 16-channel analog multiplexer for input expansion
- **DS2482** - 1-Wire master that converts the protocol to I2C
- **SC16IS750** - UART expander over SPI/I2C (solves the UART shortage problem)
- **W25Q32** - external SPI-flash memory 32 Mb for logging/datalogging
- **Qi charging** - inductive charging receiver/transmitter for devices

## Characteristics

| Module | Interface | Main parameters | Purpose |
| --- | --- | --- | --- |
| **AD9833** | SPI | Frequency: 0.01-12.5 MHz; outputs: sine, triangle, square; accuracy: 14 bit | DDS signal generator for testing, audio, radio |
| **GM328** | Analog (GPIO) | Measurements: beta (DC current gain), HFE, Vces(sat), Ic, Ie; SMD/DIP transistor test | Transistor testing and categorization |
| **CD74HC4067** | 16-ch Analog MUX | Power: 0.6-5.5 V; logic: 3.3 V / 5 V; capacitance: ~15 pF | ESP32 ADC analog input expansion |
| **DS2482** | 1-Wire to I2C | I2C address: 0x18; speed: up to 100 kHz (stronger mods) | Links to 1-Wire sensors (DS18B20, DS1822 etc) via I2C port |
| **DS2408 / DS2413 / DS2450** | 1-Wire GPIO/ADC | 8xGPIO (2408), 2xGPIO (2413), 4xADC (2450) | Discrete inputs/outputs over one 1-Wire line: reed switches, relays, buttons of remote nodes |
| **SC16IS750** | SPI / I2C | 4 independent UARTs; baud up to 460800; UART FIFO: 16 bytes | UART port expansion for GPS, sensors, modules with serial interface |
| **W25Q32** | SPI | Capacity: 32 Mb (4 MB); SPI speed: up to 104 MHz (adrv); package: SOIC-8, WSON-8 | external storage for logs, firmware, configuration |
| **Qi charging** | Resonant inductive coupling | Frequency: 110-205 kHz; power: up to 5 V/1 A (degree depends on coil); protocol: controlled via GPIO and analog warner | Contact and wireless charging of mobile devices |

## Module pin legends

### AD9833 SPI pins

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| 1 | VDD | Power supply | 2.85-3.63 V |
| 2 | FSELECT | Input | Waveform select (0=sine, 1=triangle) |
| 3 | CLK | SPI Clock output | SPI clocking |
| 4 | FUDATA | Serial data output | Serial data, waveform |
| 5 | GND | Ground | Common ground |
| 6 | FSCTRL1 | Input | Frequency control bit |
| 7 | FSCTRL0 | Input | Frequency control bit |
| 8 | SDO | SPI Data Out output | SPI data (may be left unconnected) |

### GM328 transistor tester pins

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| Base (B) | Base input | Input | Connects to the transistor base |
| Emitter (E) | Emitter input | Input | Connects to the transistor emitter |
| Collector (C) | Collector input | Input | Connects to the transistor collector |
| VCC | Power supply | Input | 3.3V or 5V (depends on module) |
| GND | Ground | Ground | Common ground |
| Test pin | Test output | Output | LED/Buzzer indicator |

### CD74HC4067 16-ch mux pins

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| S0-S3 | Channel select | Input | 4 bits to select one of 16 channels |
| COM | Common contact | Output/Input | Output signal of the selected channel |
| NC1-NC16 | not used | - | Closed (usually unconnected) |
| VCC | Power supply | Input | 2.0-5.5 V |
| GND | Ground | Ground | Common ground |

### DS2482 1-Wire master pins

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| GND | Ground | Ground | Common ground |
| I/O | 1-Wire input/output | Output/Input | 1-Wire protocol data |
| VCC | Power supply | Input | 3.0-5.5 V |
| A0 | Address input | Input | Defines the I2C address (usually pulled) |

### SC16IS750 UART expander pins

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| SCL / SDA | I2C clock / data | Input/Input | I2C control interface |
| SDO / SDI | SPI data out / in | Output/Input | SPI data interface |
| CS | Chip Select | Input | Active-low chip select |
| RST | Reset | Input | Active-high reset |
| VCC | Power supply | Input | 2.7-3.6 V |
| GND | Ground | Ground | Common ground |

### W25Q32 SPI flash pins

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| VCC | Power supply | Input | 2.7-3.6 V |
| GND | Ground | Ground | Common ground |
| CS | Chip Select | Input | Active-low chip select |
| CLK | SPI Clock | Clocking | SPI clocking |
| IO0 / IO1 | SPI Data lines | Output/Input | Bidirectional SPI data (IO0 for data, IO1 for extended commands) |
| WP | Write Protect | Input | Write protection (pull to VCC or GND) |
| HOLD | Hold | Input | SPI operation pause (pull to VCC or GND) |

### Qi charging module (receiver) pins

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| Coil+ | Coil + (anode) | Output | Connection to primary coil |
| Coil- | Coil - (cathode) | Output | Connection to primary coil |
| D+ / D- | Data lines | Analog | Control PWM/parator data |
| GND | Ground | Ground | Common ground with ESP32 |

## ## Schematic

### ASCII schematic (example for AD9833 + ESP32)

```text
           +-------------------+       +-----------------+
           |      AD9833       |       |     ESP32       |
           +-------------------+       +-----------------+
                 ↑                   ↑           ↑
          FSELECT            CLK           MISO MOSI SCK
                 │                   │           │
    +------------+-----------+-----------+-----------+
    |            VDD (3.3V)         GND         |
    +---------------------------------------------+
                       │
                 +-----+-----+
                 |  SPIbus     |
                 +-----+-----+
                        │
               +---------+---------+
               |   ESP32 SPI       |
               | GPIO18=SCK, GPIO19=MISO, GPIO23=MOSI, GPIO5=SS   |
               +-----------------------+
```

### Mermaid graph LR (connecting modules with ESP32)

```mermaid
graph LR
    %% AD9833 section
    esp32[ESP32 DevKit]
    ad9833[AD9833 DDS Generator]
    ad9833 -->|VDD 3.3V| vcc[Power 3.3V]
    ad9833 -->|GND| gnd[GND]
    esp32 -->|GPIO18 SCK| clk[CLK]
    esp32 -->|GPIO19 MISO| miso[MISO]
    esp32 -->|GPIO23 MOSI| mosi[MOSI]
    esp32 -->|GPIO5 SS| ss[CS/FSELECT]

    %% GM328 section
    gm328[GM328 Transistor Tester]
    gm328 -->|VCC 3.3V| vcc2[Power]
    gm328 -->|GND| gnd2[GND]
    gm328 -->|Base| base_gpio[GPIO26]
    gm328 -->|Emitter| emit_gpio[GPIO27]
    gm328 -->|Collector| coll_gpio[GPIO25]

    %% CD74HC4067 section
    mux[CD74HC4067 Mux 16-ch]
    mux -->|VCC 3.3V| vcc3[Power]
    mux -->|GND| gnd3[GND]
    esp32 -->|GPIO14 S0| s0[S0]
    esp32 -->|GPIO15 S1| s1[S1]
    esp32 -->|GPIO16 S2| s2[S2]
    esp32 -->|GPIO17 S3| s3[S3]
    esp32 -->|ADC1_0| adc_in[ADC Channel]
    mux -->|COM| com_out[Common Out]

    %% DS2482 section
    ds2482[DS2482 1-Wire Master]
    ds2482 -->|VCC 3.3V| vcc4[Power]
    ds2482 -->|GND| gnd4[GND]
    ds2482 -->|I/O| ow_iom[1-Wire Bus]
    esp32 -->|GPIO4 SCL| i2c_scl[I2C SCL]
    esp32 -->|GPIO5 SDA| i2c_sda[I2C SDA]

    %% SC16IS750 section
    sc16is750[SC16IS750 UART Expander]
    sc16is750 -->|VCC 3.3V| vcc5[Power]
    sc16is750 -->|GND| gnd5[GND]
    esp32 -->|GPIO6 SCLK| spi_sclk[SPI CLK]
    esp32 -->|GPIO7 SDO| spi_sdo[SPI SDO]
    esp32 -->|GPIO8 SDI| spi_sdi[SPI SDI]
    esp32 -->|GPIO9 CS| cs[Chip Select]
    sc16is750 -->|UART TX| uart_tx[GPS/Sensors RX]
    sc16is750 -->|UART RX| uart_rx[GPS/Sensors TX]

    %% W25Q32 section
    w25q32[W25Q32 Flash 32Mbit]
    w25q32 -->|VCC 3.3V| vcc6[Power]
    w25q32 -->|GND| gnd6[GND]
    w25q32 -->|CLK| flash_clk[SPI CLK]
    w25q32 -->|IO0| flash_io0[SPI IO0]
    w25q32 -->|IO1| flash_io1[SPI IO1]
    esp32 -->|GPIO10 CS| flash_cs[Chip Select]

    %% Qi section
    qi[Qi Charging Module]
    qi -->|Coil+| coil_plus[Coil +
    qi -->|Coil–| coil_minus[Coil –]
    esp32 -->|GPIO12| charge_en[Charge Enable]
    esp32 -->|GPIO13| led_status[LED Status]
```

## ## Code

### Arduino - AD9833 signal generator

```cpp
#include <SPI.h>
#include <MF_AD9833.h> // custom lib or Adafruit_AD9833

#define AD9833_RESET 23
#define AD9833_SPI_CS 5

AD9833 ad9833;

void setup() {
  Serial.begin(115200);
  SPI.begin(18, 19, 23, AD9833_SPI_CS); // SCK=18, MISO=19, MOSI=23, CS=5

  // Ініціалізація AD9833
  ad9833.reset();
  ad9833.setFrequency(440.0);      // 440 Hz
  ad9833.setWaveform(AD9833_WAVE_SINE); // синус, AD9833_WAVE_TRIANGLE, AD9833_WAVE_SQUARE
  ad9833.enableOutput(true);

  Serial.println("AD9833 ready - generating 440Hz sine wave");
}

void loop() {
  // Можна змінювати частоту та форму сигналу тут
  delay(1000);
}
```

### Arduino - CD74HC4067 multiplexer (reading 16 ADC channels)

```cpp
const int s0 = 14;
const int s1 = 15;
const int s2 = 16;
const int s3 = 17;
const int adc_pin = ADC1_CHANNEL_0; // GPIO36 або аналогово

void setup() {
  Serial.begin(115200);
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);

  // Тестування кожного чату
  for (int ch = 0; ch < 16; ch++) {
    setMuxChannel(ch);
    int val = analogRead(adc_pin);
    Serial.print("Channel ");
    Serial.print(ch);
    Serial.print(": ");
    Serial.println(val);
  }
}

void setMuxChannel(int channel) {
  digitalWrite(s0, channel & 0x01);
  digitalWrite(s1, (channel >> 1) & 0x01);
  digitalWrite(s2, (channel >> 2) & 0x01);
  digitalWrite(s3, (channel >> 3) & 0x01);
}

void loop() {
  // Основна програма
}
```

### MicroPython - SC16IS750 UART expander

```python
from machine import Pin, SoftI2C, UART
import time

# I2C налаштування для SC16IS750
i2c = SoftI2C(scl=Pin(22), sda=Pin(23))

# Перевірка адреси чіпа
devices = i2c.scan()
if 0x60 in devices:
    print("SC16IS750 found at address 0x60")
else:
    print("SC16IS750 not found")
    while True:
        pass  # Halt

# Ініціалізація UART чіпа через SC16IS750
uart = UART(0, baudrate=9600, bits=8, parity=None, stop=1)
# Регістри SC16IS750 керуються через I2C, див. даташит

# Тест передачі
uart.write("Hello from SC16IS750 UART expander!\n")
time.sleep(1)

# Читання даних
if uart.any():
    data = uart.read()
    print("Received:", data)
```

### ESP-IDF - W25Q32 Flash operations (Arduino style for ESP-IDF)

```c
#include "driver/spi_master.h"
#include "driver/gpio.h"
#include "sdkconfig.h"

// W25Q32 pin definitions
#define W25Q32_CS_GPIO    GPIO_NUM_5
#define W25Q32_CLK_GPIO   GPIO_NUM_18
#define W25Q32_IO0_GPIO   GPIO_NUM_19
#define W25Q32_IO1_GPIO   GPIO_NUM_23

static spi_device_handle_t spi_handle;

static esp_err_t w25q32_init(void) {
    spi_device_interface_config_t devcfg = {
        .clock_speed_hz = 20 * 1000 * 1000, // 20 MHz
        .mode = 0,                           // SPI mode 0
        .spics_io_num = W25Q32_CS_GPIO,
        .flags = 0,
    };
    ESP_ERROR_CHECK(spi_bus_initialize(SPI2_HOST, HSPI_HOST_LINES, DMA_CHAN));
    ESP_ERROR_CHECK(spi_bus_add_device(SPI2_HOST, &devcfg, &spi_handle));
    return ESP_OK;
}

static uint8_t w25q32_read_id(void) {
    uint8_t cmd[] = {0x9F, 0x00, 0x00, 0x00}; // Read ID command
    uint8_t resp[4];

    spi_transaction_t t = {
        .length = 32, // 4 bytes * 8
        .tx_buffer = cmd,
        .rx_buffer = resp,
    };
    ESP_ERROR_CHECK(spi_device_transact(spi_handle, &t));

    // Manufacturer ID typically in resp[1]
    return resp[1];
}

void app_main(void) {
    ESP_ERROR_CHECK(w25q32_init());

    uint8_t man_id = w25q32_read_id();
    printf("W25Q32 Manufacturer ID: 0x%02X\n", man_id);

    // Далі: читати сектори, записувати дані, etc.
}
```

### DS2484 / W25Q128 / AD9850 - older relatives

| Item | What it is | Difference |
| --- | --- | --- |
| DS2484 | 1-Wire master like DS2482, but with adjustable timing | More flexible slew-rate for long lines; same I2C addressing |
| W25Q128 | SPI-flash 128 Mbit (16 MB) | Twice bigger than W25Q32; same SOIC-8 footprint, compatible commands |
| AD9850 | DDS up to 40 MHz (older brother of AD9833) | Higher frequency and parallel/serial interface, but bigger package and appetite |

> DS2484 vs DS2482: DS2482 is enough for buses up to 30 m; longer/noisy lines - DS2484 with tuned timing.

## ## Common errors 12+ as a table

| # | Symptom | Cause | Solution |
| --- | --- | --- | --- |
| 1 | AD9833 outputs 0V or noise | Wrong power (not 3.3V) | verify voltage on VDD, add 100nF + 10uF capacitors near the chip |
| 2 | Unreadable signal on scope | Error in FSCTRL1/FSCTRL0 setting | Use the frequency calculator from the datasheet, verify bits |
| 3 | GM328 does not identify the transistor | Wrong Base/Emitter/Collector connection | Straighten the connection, verify the transistor datasheet |
| 4 | GM328 shows beta = 0 or very high | Transistor burnt-out | verify on a current tester or replace the transistor |
| 5 | CD74HC4067 outputs "grabs" all channels | Error in S0-S3 bit settings | verify bit order (LSB first), verify multiplexer power |
| 6 | ADC reading floats/drifts | Electromagnetic interference (EMI) | Add a ceramic filter on COM output, increase capacitors |
| 7 | DS2482 does not see 1-Wire devices | Parasitic power from the 1-Wire line does not work | Add an external capacitor (100 uF) between DS2482 VCC and GND |
| 8 | DS2482 I2C address 0x18 does not answer | A0 pin setting error | verify A0 pull to VCC/GND per the datasheet |
| 9 | SC16IS750 UART outputs garbage | Baud rate mismatch between ESP and peripheral | verify common speed, use exact baud settings |
| 10 | W25Q32 does not answer on SPI | Wrong CS pin or CLK setting | verify SPI connections, verify WP/HOLD pins (pull-ups) |
| 11 | Qi charging does not start | Wrong driver generator frequency | Check GPIO management code, check coils and matching resistors |
| 12 | Qi charging overheats | Short in winding or power > 1A | Replace the coil with a lower-power one, extra thermal safety |

| # | Symptom | Cause | Solution |
| --- | --- | --- | --- |
| 13 | Common SPI interaction (AD9833 + W25Q32 + DS2482) | Shared SPI bus without separate CS | Add separate CS pins for each device, call `spi.begin()` once |
| 14 | Switching between modules reboots ESP32 | Reverse current between power modules | Install isolated LDOs for each module or use a common 3.3V bus with diode isolation |
| 15 | MicroPython AD9833 import error | wrong library or MicroPython version | Use `from machine import SPI, Pin` with manual registration, see the AD9833 datasheet |
| 16 | CD74HC4067 damaged signal at high frequencies | Multiplexing degradation at HF | Lower the channel switching frequency, add a Schmitt trigger on output to clean the signal |
| 17 | DS2482 sporadically resets ESP32 | Pull-up resistor on the 1-Wire line too small | Use a 4.7k-10k pull-up to 3.3V, verify wire length |
| 18 | SC16IS750 not detected in MicroPython | Missing pull-up on SDA/SCL | Add 10k pull-up resistors on the I2C bus |
| 19 | W25Q32 write protection error | WP pin hard-grounded to GND | Pull WP to VCC or join with GND only when writing is needed |
| 20 | Qi charger intermittent operation | Magnetic field flight strength | Move the coil angle, verify resonance pattern, use a shell design |
| 21 | W25Q128 as a W25Q32 replacement without attention to addressing | Old libraries do not know 4-byte addresses | Update the driver; AD9850 requires separate 30-125 MHz clocking, not the ESP32 SPI clock |

## ## Official sources

1. [AD9833 DDS Generator Datasheet (PDF, Analog Devices)](https://www.analog.com/en/products/ad9833.html) - official datasheet with registers, frequency formulas and App Note
2. [GM328 Transistor Tester Guide (Blog, Greatest-Tech)](https://greatest-tech.com/gm328-transistor-tester-guide/) - pin breakdown, functions and tests
3. [CD74HC4067 16-Channel Multiplexer Datasheet (PDF, TI)](https://www.ti.com/lit/ds/symlink/cd74hc4067.pdf) - full channel table and characteristics
4. [DS2482 1-Wire to I2C Master Datasheet (PDF, Maxim Integrated/Dallas)](https://datasheets.maximintegrated.com/en/ds/DS2482A.pdf) - protocol details and I2C addressing
5. [SC16IS750 UART Expander Datasheet (PDF, NXP/Silicon Labs)](https://www.nxp.com/docs/en/data-sheet/SC16IS750.pdf) - UART registers and SPI/I2C settings
6. [W25Q32 Flash Memory Datasheet (PDF, Winbond)](https://www.winbond.com/products/spi-nor-flash/w25q32) - page sizes, SPI modes, endurance tests
7. [Qi Wireless Charging Specification (PDF, WPC)](https://www.wirelesspowerconsortium.com/specifications/) - standard frequencies, powers, control protocol

> [!warning]
> Guessed URL addresses without webfetch verification are forbidden. Check each link before use in production code.

## ## See also

- [[EN/Home.en]]
- [[EN/04-Interfaces/02-SPI.en|SPI]]
- [[EN/04-Interfaces/03-I2C.en|I2C]]
- [[EN/06-Analog/01-ADC.en|ADC]]
- [[EN/12-Comm-Modules/24-DIY-Instruments.en]]

24→(Home, [[EN/04-Interfaces/02-SPI.en|SPI]], [[EN/04-Interfaces/03-I2C.en|I2C]], [[EN/06-Analog/01-ADC.en|ADC]])
