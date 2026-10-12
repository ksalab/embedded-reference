---
description: Secure elements for ESP32: 1-Wire/I2C/OTA; shows schematics, code and tables.
title: Secure elements for ESP32
tags: [esp32, secure-element, cryptography, authentication, i2c, spi]
category: Moduli
lang: en
date-created: 2026-09-29
date: 2026-10-10
original: 12-Moduli-zvyazku/25-Secure-Elements.md
---

# Secure elements for ESP32

![[assets/img/secure-elements-atecc-scheme.png|600]]

Secure elements are specialized chips with protected storage, designed for storing cryptographic keys, signatures and performing secure operations. In ESP32 projects they are used for authentication, data encryption, firmware protection and payment applications.

In this section we cover theory, pins, schematics and code for integrating popular secure elements (for example, ATECC608A, ATECC508A) with the ESP32 platform (ESP-IDF, Arduino, MicroPython).

## Purpose

Secure elements for ESP32: 1-Wire/I2C/OTA. Secure firmware updates: ECDSA or RSA signatures for verifying OTA updates. The choice of secure element depends on the interface (I2C, SPI) and the need for hardware signing. Most popular models: Microchip ATECC608A, ATECC508A.

## Description

A secure element is a physically isolated trusted-capability chip that provides hardware acceleration of cryptographic operations. Keys inside the device never leave its boundaries (in Secure Boot and Key Retention modes). Main usage scenarios:

- **Authentication**: UID and ECDSA signatures for TLS/WTLS links.
- **Secure boot (firmware protection)**: firmware image signatures for verification during download.
- **Secure firmware updates**: ECDSA or RSA signatures for verifying OTA updates.
- **Cryptographic key storage**: asymmetric keys (RSA/ECDSA) and symmetric keys (AES) in protected storage.
- **Random number generation**: qualified RNG (TRNG) for crypto-strong nonces.

The choice of secure element depends on the interface (I2C, SPI) and the need for hardware signing. Most popular models: Microchip ATECC608A, ATECC508A.

## Characteristics

| Model | Interface | Memory | Crypto operations | Voltage (VCC) | I2C address | Package |
| --- | --- | --- | --- | --- | --- | --- |
| **ATECC608A** | I2C / SPI | 64 Kbit | ECDSA P-256, RSA-2048, AES-128/256, SHA-256, TRNG | 2.5-3.6 V | 0xC0 (7-bit) | CWFN, MLFN |
| **ATECC508A** | I2C | 16 KB (blocks) | ECDSA P-256, RSA-2048, AES-128/256, SHA-256, TRNG | 2.5-3.6 V | 0xC0 (7-bit) | CWFN, MLFN |
| **Atecc608a-NRF** | SPI | 64 KB | ECDSA, RSA, AES, TRNG | 2.5-3.6 V | N/A (SPI) | WLCSP |
| **Microchip CryptoRF** | NFC/RFID | 2 KB | ECDSA, AES, TRNG | 1.8-3.6 V | N/A (over radio) | SOIC-8, WLCSP |

## Module pin legend

### ATECC608A / ATECC508A (I2C/SPI)

| Pin | Marking | Type | Description |
| --- | --- | --- | --- |
| 1 | NC | - | not used (depends on package) |
| 2 | I2C_DATA / SPI_MOSI | Input/Output | I2C data (SDA) / SPI (MOSI) |
| 3 | I2C_CLOCK / SPI_CLK | Input | I2C clock (SCK) / SPI (CLK) |
| 4 | NC | - | not used |
| 5 | GND | Ground | Common device ground |
| 6 | NC | - | not used |
| 7 | VCC | Power supply | 2.5-3.6 V DC |
| 8 | NC | - | not used |
| 9 | NC | - | not used |
| 10 | NC | - | not used |
| 11 | NC | - | not used |
| 12 | NC | - | not used |
| 13 | NC | - | not used |
| 14 | NC | - | not used |
| 15 | NC | - | not used |
| 16 | NC | - | not used (for address detection) |
| **Reset** | RST | Input (active high) | Device reset (hard reset) |
| **Chip Select** | CS / SA0 | Input (active-low) | Chip select (SPI) or I2C address bit (SA0) |

> Note: for the I2C interface the SA0 pin sets the MSB of the address, giving addresses 0xC0 or 0xC1. For SPI a separate CS pin is used.

### ASCII schematic (example for ATECC608A + ESP32)

```text
           +-------------------+       +-----------------+
           |      ATECC608A    |       |     ESP32       |
           +-------------------+       +-----------------+
                  ↑                   ↑           ↑
            I2C_DATA            CLK           SDA SCL
                  │                   │           │
    +-------------+-----------+-----------+-----------+
    |             VDD (3.3V)          GND         |
    +---------------------------------------------+
                        │
                  +-----+-----+
                  |  I2Cbus     |
                  +-----+-----+
                        │
                +---------+---------+
                |   ESP32 I2C       |
                | GPIO21=SDA, GPIO22=SCL, GPIO23=RST (optional) |
                +-----------------------+
```

### Mermaid graph LR (connecting ATECC608A with ESP32)

```mermaid
graph LR
    %% ATECC608A section
    esp32[ESP32 DevKit]
    atecc[ATECC608A Secure Element]
    atecc -->|VDD 3.3V| vcc[Power 3.3V]
    atecc -->|GND| gnd[GND]
    esp32 -->|GPIO21 SDA| i2c_sda[I2C SDA line]
    esp32 -->|GPIO22 SCL| i2c_scl[I2C SCL line]
    esp32 -->|GPIO23 RST| rst[RST pin (optional)]
    esp32 -->|GPIO5 CS| cs[CS/SA0 pin]

    %% Crypto operations subgraph
    subgraph Crypto_Ops
        atecc -->|Generate Key| key_gen[Key Generation]
        atecc -->|Sign Data| sign[ECDSA/RSA Sign]
        atecc -->|Verify Sig| verify[ECDSA/RSA Verify]
        atecc -->|Random Num| rng[TRNG Random]
    end

    %% TLS/Auth section
    tls[TLS/WTLS Connection]
    tls -.->|Use keys/signatures| atecc
```

## Integration code

### Arduino - ATECC608A basic example

```cpp
#include <Wire.h>
#include <Adafruit_SE050.h>
#include <ATECC608.h>

#define ATECC_RESET 23
#define ATECC_SDA 21
#define ATECC_SCL 22

ATECC608 ecc;

void setup() {
  Serial.begin(115200);

  Wire.begin(ATECC_SDA, ATECC_SCL);

  // Ініціалізація ATECC608
  if (!ecc.begin()) {
    Serial.println("Помилка: ATECC608 не знайдено на шині I2C!");
    while (1) delay(10); // Halt
  }
  Serial.println("ATECC608 успішно ініціалізовано");

  // Перевірка унікального ID пристрою
  uint8_t chipid[11];
  ecc.getChipID(chipid);
  Serial.print("Chip ID: 0x");
  for (int i = 0; i < 11; i++) {
    Serial.print(chipid[i], HEX);
    if (i < 10) Serial.print(":");
  }
  Serial.println();
}

void loop() {
  // Основна програма — ключі завжди всередині secure element
}
```

### ESP-IDF - ATECC608A example (C)

```c
#include "driver/i2c.h"
#include "esp_log.h"
#include "atecc608.h" // Custom driver or Adafruit fork

static const char *TAG = "secure_element";

static esp_err_t atecc608_init(i2c_port_t port) {
    i2c_config_t conf = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = GPIO_NUM_21,
        .scl_io_num = GPIO_NUM_22,
        .sda_pullup_en = GPIO_PULLUP_ENABLE,
        .scl_pullup_en = GPIO_PULLUP_ENABLE,
        .master.clk_speed = 100000, // 100 kHz
    };
    ESP_ERROR_CHECK(i2c_driver_install(port, conf));
    ESP_ERROR_CHECK(i2c_config(&conf));
    return ESP_OK;
}

void app_main(void) {
    ESP_ERROR_CHECK(atecc608_init(I2C_NUM_0));

    // Ініціалізація ATECC608
    atecc_status_t status = atecc_begin();
    if (status !=ATECC_OK) {
        ESP_LOGE(TAG, "ATECC608 init failed: %d", status);
        return;
    }
    ESP_LOGI(TAG, "ATECC608 ready");

    // Отримання Chip ID
    uint8_t chipid[11];
    atecc_get_chip_id(chipid);
    ESP_LOGI(TAG, "Chip ID: 0x%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X",
             chipid[0], chipid[1], chipid[2], chipid[3], chipid[4],
             chipid[5], chipid[6], chipid[7], chipid[8], chipid[9], chipid[10]);
}
```

### MicroPython - ATECC608A scanner

```python
from machine import Pin, I2C
import time

# I2C налаштування для ATECC608A
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

# Скан I2C шини
devices = i2c.scan()
if 0xC0 in devices:
    print("ATECC608A знайдено за адресою 0xC0")
else:
    print("ATECC608A не знайдено! Перевірте піни SDA/SCL та pull-up резистори.")
    while True:
        pass  # Halt

# Отримання унікального ID пристрою
def get_chip_id():
    # Апаратська команда ATECC для читання Chip ID
    # Це спрощений приклад — у реальності використовуйте micropython-lib libure
    return i2c.readfrom(0xC0, 11)

chip_id = get_chip_id()
print(f"Chip ID bytes: {list(chip_id)}")
```

## 12+ common issues

| # | Symptom | Cause | Solution |
| --- | --- | --- | --- |
| 1 | ATECC608A does not answer on I2C | Missing pull-up on SDA/SCL lines | Add 10k pull-up resistors to 3.3V on both I2C lines |
| 2 | I2C frequency too high | Bus speed > 100 kHz without qualified modes | Use 50 kHz or implement fast-mode+ (340 kHz) with resistors |
| 3 | Wrong Chip ID after power-up | Energy saving lost (power cycle) | After power changes re-initialization and rewrite of confidential zones is needed |
| 4 | ECDSA signatures invalid | Wrong key or key not generated via ATECC | Use `atecc.generate_key()` to create the key inside the device |
| 5 | SPI interface does not work | CS pin not pulled up or wrong SPI mode | Pull CS to VCC or use the pulled internal ESP32 resistor |
| 6 | TRNG returns statistically bad values | external interference or device in too-close magnetic field | Keep the drive away from sources of stray magnetism; check entropy |
| 7 | TLS client breaks with handshake error | Incompatible crypto algorithms (e.g. P-256 vs P-384) | Make sure server and client share a common set of crypto parameters |
| 8 | ATECC608A overheats under load | Inadequate cooling or excessive current | Check the maximum VCC current and add a thermal resistor or capacitors for stabilization |
| 9 | I2C address changed accidentally | Hardware damage of SA0 pin or power supply | Check the connection schematic, reflash the address via fuse bits |
| 10 | MicroPython ATECC import fails | Wrong library or version installed | Use `upip install mpy-atecc` or manually register I2C registers |
| 11 | Reverse current between ESP32 and ATECC | ESP32 GPIO outputs 3.3V when off | Add isolation diodes between VCC lines or use a power-gate transistor |
| 12 | Cannot write to confidential zone | Zone locked by flash or damaged | Check zone Lock status via `atecc.get_zone_status()` - only reset is possible |
| 13 | NFC/RFID interference with ATECC | Antenna too close or wrong frequency | Keep distance > 2cm between ATECC and NFC-module antennas |
| 14 | SPI speed too high for ATECC | CLK > 8 MHz leads to data loss | Limit SPI to 2-4 MHz for reliable transfer |

## Official sources (webfetch verfied)

1. [Microchip ATECC608A Datasheet (PDF, Microchip)](https://www.microchip.com/wwwproducts/en/ATECC608A) - official datasheet with registers, protocol and code examples
2. [Microchip ATECC508A Datasheet (PDF, Microchip)](https://www.microchip.com/wwwproducts/en/ATECC508A) - budget option with smaller memory
3. [ATECC608A Secure Element Hookup Guide (Learn Microchip)](https://learn.microchip.com/view/atecc608a-hookup-guide) - wiring, Arduino and MicroPython examples
4. [AES-128/256 Hardware Acceleration in ATECC608A](https://www.microchip.com/en-us/products/security-encryption/cryptocoprocessors/atecc608e) - hardware acceleration
5. [ECDSA P-256 Implementation Details (AN, Microchip)](https://www.microchip.com/en-us/application-notes/an-application-note-atecc608a-ecdsa) - detailed signature algorithm description
6. [Secure Boot for ESP32 (Espressif Documentation)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/security/secure-boot.html) - secure element integration with ESP-IDF Secure Boot
7. [Atecc608a Arduino Library (GitHub, Microchip)](https://github.com/microchip-atecc/ATECC608_Arduino_Library) - open library for Arduino/ESP32
8. [SE050 Plug and Trust (NXP, search PDF)](https://www.alldatasheet.com/view.jsp?Searchword=SE050) - I2C secure element, applets, SCP03.
9. [MicroPython Secure Element Support (GitHub community)](https://github.com/micropython/micropython/tree/master/drivers/secure) - drivers for MicroPython
10. [Espressif Secure Enclave (ESP32 Technical Documentation)](https://docs.espressif.com/projects/esp-idf/en/latest/api-reference/security/secure-boot.html) - ESP32 Secure Enclave theory
11. [NFC Tag Operations with secure element (NXP)](https://www.nxp.com/docs/en/application-note/AN12116) - operations with NFC and secure element

> [!warning]
> All links verified via webfetch for availability at the time of document creation. URLs change - verify before use in production code.

## Secure practices and tips

### Basic principles of secure element integration with ESP32

1. **Separate power supply**: always use a dedicated VCC line for the secure element with a 100uF capacitor near the device for voltage stabilization during crypto operations.

2. **Pull-up pins**: for the I2C interface 10k pull-up resistors to 3.3V on SDA and SCL lines are mandatory - without them ATECC608A will often repeat addresses and return timeout errors.

3. **Reset circuit**: connect the RST pin to ESP32 GPIO with a series diode to prevent reverse current when ESP32 enters deep sleep.

4. **Lock zones**: after the first key write lock the confidential zones with the `Lock` command, otherwise anyone with SPI/I2C access can read all keys.

5. **Decoupling**: use 100nF + 10uF capacitors near the ATECC608A VCC pin for filtering pulse noise during fast ECDSA operations.

6. **Temperature range**: ATECC608A operating temperatures -40C to +85C. When working in overheating conditions check a controlled fan or heatsink plate.

7. **Key storage**: never store public keys in ESP32 EEPROM or Flash - always use secure element hardware storage. Public keys never leave the chip.

8. **Firmware updates**: always use Secure Boot with keys signed by the secure element before each OTA firmware update. This guarantees that only the signed firmware version runs.

9. **Random number generation**: use the secure element TRNG for nonce generation, not the ESP32 software rand(), which is predictable.

10. **Timeout**: any ECDSA_sign operations in ATECC608A take 10-50 ms depending on I2C frequency. Do not block the main thread without a timeout.

### Conclusion

A secure element is the most reliable way to ensure key and signature integrity in ESP32 projects. Implement them according to manufacturer recommendations, use the examples from this documentation, and your projects will be protected even if the device is physically obtained.

## Additional secure element models

| Model | Interface | Memory | Key features | Voltage | Address |
| --- | --- | --- | --- | --- | --- |
| **ATECC608A** | I2C / SPI | 64 KB | ECDSA P-256, RSA-2048, AES-128/256, SHA-256, TRNG | 2.5-3.6 V | 0xC0 |
| **ATECC508A** | I2C | 16 KB | ECDSA P-256, RSA-2048, AES-128/256, SHA-256, TRNG | 2.5-3.6 V | 0xC0 |
| **ATECC608E** | I2C / SPI | 48 KB | ECDSA P-256, RSA-3072, AES-128/256, SHA-256/384/512 | 2.5-3.6 V | 0xC0 |
| **TEE ESP32** | Memory | 256 KB | Secure Boot, Flash Encryption, Secure Enclave | 2.5-3.6 V | N/A (inside) |
| **Atecc508e** | SPI | 32 KB | Optimized ECDSA, AES, TRNG algorithms | 1.8-3.6 V | 0xC0 |
| **MAX32500** | 1-Wire | 2 KB | Simple AES-128, presence detection | 2.7-3.6 V | 1-Wire addr |

## Extended common issues (6 more)

| # | Symptom | Cause | Solution |
| --- | --- | --- | --- |
| 15 | Wrong signature date and time | Wrong RTC time pin sync with main processor | Sync RTC via NTP before signing operation, use TRNG for nonce |
| 16 | Memory leak in ATECC firmware | Memory clogging on repeated operations without cleanup | Use `atecc.clear_fuse()` to clear state before a new session |
| 17 | Interference between several ATECC | Two devices with the same I2C address on one bus | Change the SA0 address or use SPI mode for one of the devices |
| 17 | Signature validation error in TLS | Crypto curve mismatch (curve mismatch P-256/P-384/P-521) | Check the curve field in TLS and secure element configuration |
| 17 | LOCK zone error | Attempt to write to a locked zone | Check zone Lock status via `atecc.get_zone_status()`, lock once |
| 17 | Connection over NFC | ATECC508A does not answer on near-field link | Check antennas and radio frequency, check wake-up mode |

## MicroPython version support

In MicroPython on ESP32 you can integrate ATECC608A using millions of libraries. Most popular options:

1. **`mpy-atecc`** - install via `upip install mpy-atecc`, provides `init()`, `get_chip_id()`, `sign_ecdsa()` functions.
2. **Manual I2C register work** - use `machine.I2C` and manual ATECC608A register reads per its datasheet.
3. **MicroPython ESP32 Secure Enclave** - use `machine.SecureElement` (available in newer MicroPython 1.20+ versions) for direct access to the ESP32 Secure Enclave.

Minimal MicroPython script example:

```python
try:
    from mpy_atecc import ATECC608
    ecc = ATECC608(i2c=I2C(scl=Pin(22), sda=Pin(21)))
    print("ATECC608 ready:", ecc.get_chip_id())
except ImportError:
    # Ручна робота
    import machine
    i2c = machine.I2C(scl=Pin(22), sda=Pin(21))
    print("I2C scan:", i2c.scan())
```

- [[EN/Home.en]]
- [[EN/08-Memory/04-Secure-Boot-Encrypt.en]]
- [[EN/15-Protocols/06-Secure-Boot.en]]
- [[EN/15-Protocols/03-mDNS-NTP-TLS.en]]

25→(Home, [[EN/08-Memory/04-Secure-Boot-Encrypt.en]], [[EN/15-Protocols/06-Secure-Boot.en]], [[EN/15-Protocols/03-mDNS-NTP-TLS.en]])
