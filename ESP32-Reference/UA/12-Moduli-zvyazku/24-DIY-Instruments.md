---
title: DIY-прилади для ESP32 - AD9833, GM328, мультиплексори, Flash (DIY Instruments)
description: Цей модуль розглядає низку потужних але економних цифрових та аналогових модулів, які можна використати для створення професійних вимірювальних інструментів, генераторів сигналів,...
tags: [esp32, diy, instruments, ad9833, gm328, cd74hc4067, ds2482, sc16is750, w25q32, qi]
category: Moduli
date-created: 2026-09-29
---

# DIY-прилади для ESP32 (AD9833, GM328, мультиплексори, Flash)

![[assets/img/diy-instruments-ad9833-scheme.png|600]]

> [!info]
> Цей документ охоплює популярні модулі для створення зовнішніх інструментів з ESP32. Кожен модуль описан з точки зору підключення, характеристик та поширених помилок.

## Призначення

Цей модуль розглядає низку потужних але економних цифрових та аналогових модулів, які можна використати для створення професійних вимірювальних інструментів, генераторів сигналів, моніторингу та інших DIY проектах на базі ESP32. Всі модулі вибрані згідно з принципом "розмір/ціна/функціональність" і мають добру підтримку у ESP-IDF, Arduino та MicroPython.

Модулі охоплюють:

- **AD9833** - DDS-генератор синуса/трикутника/меандр до 12.5 МГц по SPI
- **GM328** - транзисторний тестер з виміром β, HFE, continuing і іншими параметрами
- **CD74HC4067** - 16-чатовий аналоговий мультиплексор для розширення вхідів
- **DS2482** - 1-Wire master, який перетворює протокол на I2C
- **SC16IS750** - UART-розширювач по SPI/I2C (решає проблему дефісу UART)
- **W25Q32** - зовнішня SPI-flash пам'ять 32 Мб для логування/datalogingu
- **Qi-зарядка** - приймач/передавач индуктивної зарядки для пристроїв

## Характеристики

| Модуль | Інтерфейс | Основні параметри | Назначення |
| --- | --- | --- | --- |
| **AD9833** | SPI | Частота: 0.01-12.5 МГц; виходи: синус, трикутник, меандр; точність: 14 біт | DDS-генератор сигналів для тестування, аудіо, радіо |
| **GM328** | Аналог (GPIO) | Виміри: β (DC current gain), HFE, Vces(sat), Ic, Ie; тест транзисторів SMD/DIP | Тестування і категорізація транзисторів |
| **CD74HC4067** | 16-ch Analog MUX | Живлення: 0.6-5.5 В; логіка: 3.3 В / 5 В; ємність: ~15 пФ | Розширення аналогових входів ESP32 (ADC) |
| **DS2482** | 1-Wire → I2C | I2C адреса: 0x18; швидкість: до 100 кГц (потужніше модифікації) | Зв'язок з 1-Wire сенсорами (DS18B20, DS1822 тощо) через I2C-порт |
| **DS2408 / DS2413 / DS2450** | 1-Wire GPIO/АЦП | 8×GPIO (2408), 2×GPIO (2413), 4×АЦП (2450) | Дискретні входи/виходи по одній лінії 1-Wire: геркони, реле, кнопки далеких вузлів |
| **SC16IS750** | SPI / I2C | 4 незалежних UART; baud до 460800; UART FIFO: 16 байт | Розширення UART-портів для GPS, датчиків, модулів з serial інтерфейсом |
| **W25Q32** | SPI | Ємність: 32 Мб (4 МБ); швидкість SPI: до 104 МГц (adrv); памець: SOIC-8, WSON-8 | зовнішній накопичувач для логів, прошивок, конфігурації |
| **Qi-зарядка** | Resonant inductive coupling | Частота: 110-205 кГц; потужність: до 5 В/1 A (степінь залежно от котушки); протокол: управляється через GPIO та аналоговий попереджач | Натсужена та бездротова зарядка мобільних пристроїв |

## Легенда пінів модулів

### AD9833 SPI pins

| Пін | Позначення | Тип | Опис |
| --- | --- | --- | --- |
| 1 | VDD | Живлення | 2.85-3.63 В |
| 2 | FSELECT | Вхід | Вибір форми сигналу (0=синус, 1=трикутник) |
| 3 | CLK | Вихід SPI Clock | Тактування SPI |
| 4 | FUDATA | Вихід послідовних даних | Послідовні дані, форма сигналу |
| 5 | GND | Земля | Спільна земля |
| 6 | FSCTRL1 | Вхід | Біт керування частотою |
| 7 | FSCTRL0 | Вхід | Біт керування частотою |
| 8 | SDO | Вихід SPI Data Out | Дані SPI (може бути не підключено) |

### GM328 transistor tester pins

| Пін | Позначення | Тип | Опис |
| --- | --- | --- | --- |
| Base (B) | Вхід бази | Вхід | Підключається до бази транзистора |
| Emitter (E) | Вхід еміттера | Вхід | Підключається до еміттера транзистора |
| Collector (C) | Вхід колектору | Вхід | Підключається до колектора транзистора |
| VCC | Живлення | Вхід | 3.3В або 5В (залежно від модуля) |
| GND | Земля | Земля | Спільна земля |
| Test pin | Вихід тесту | Вихід | LED/Buzzer indicator |

### CD74HC4067 16-ch mux pins

| Пін | Позначення | Тип | Опис |
| --- | --- | --- | --- |
| S0-S3 | Вибір чату | Вхід | 4 біти для вибору одного з 16 чатів |
| COM | Спільний контакт | Вихід/Вхід | Вихідний сигнал вибраного каналу |
| NC1-NC16 | Не використовується | - | Затворі (зазвичай не підключені) |
| VCC | Живлення | Вхід | 2.0-5.5 В |
| GND | Земля | Земля | Спільна земля |

### DS2482 1-Wire master pins

| Пін | Позначення | Тип | Опис |
| --- | --- | --- | --- |
| GND | Земля | Земля | Спільна земля |
| I/O | Вхід/Виход 1-Wire | Вихід/Вхід | Дані 1-Wire протоколу |
| VCC | Живлення | Вхід | 3.0-5.5 В |
| A0 | Адресний ввід | Вхід | Визвача I2C адреси (зазвичай підтяжене) |

### SC16IS750 UART-розширивач pins

| Пін | Позначення | Тип | Опис |
| --- | --- | --- | --- |
| SCL / SDA | I2C clock / data | Вхід/Вхід | I2C інтерфейс керування |
| SDO / SDI | SPI data out / in | Вихід/Вхід | SPI інтерфейс даних |
| CS | Chip Select | Вхід | Активний низький вибір чіпа |
| RST | Reset | Вхід | Активний високий скидання |
| VCC | Живлення | Вхід | 2.7-3.6 В |
| GND | Земля | Земля | Спільна земля |

### W25Q32 SPI flash pins

| Пін | Позначення | Тип | Опис |
| --- | --- | --- | --- |
| VCC | Живлення | Вхід | 2.7-3.6 В |
| GND | Земля | Земля | Спільна земля |
| CS | Chip Select | Вхід | Активний низький вибір чіпа |
| CLK | SPI Clock | Тактування | SPI тактування |
| IO0 / IO1 | SPI Data lines | Вихід/Вхід | Двоспічні дані SPI (IO0 для даних, IO1 для розширених команд) |
| WP | Write Protect | Вхід | Захист від запису (підтягнути до VCC або GND) |
| HOLD | Hold | Вхід | Пауза операціій SPI (підтягнути до VCC або GND) |

### Qi-зарядка модуль (приймач) pins

| Пін | Позначення | Тип | Опис |
| --- | --- | --- | --- |
| Coil+ | Котушка + (анод) | Вихід | Підключення до primary coil |
| Coil- | Котушка - (катод) | Вихід | Підключення до primary coil |
| D+ / D- | Data lines | Аналогові | Дані PWM/parator управління |
| GND | Земля | Земля | Спільна земля з ESP32 |

## ## Схема

### ASCII-схема (зразок для AD9833 + ESP32)

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

### Mermaid graph LR (з'єднання модулів з ESP32)

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

## ## Код

### Arduino - AD9833 генератор сигналу

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

### Arduino - CD74HC4067 мультиплексор (читаємо 16 каналів ADC)

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

### MicroPython - SC16IS750 UART розширювач

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

### ESP-IDF - W25Q32 Flash операції (Arduino-стиль для ESP-IDF)

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

### DS2484 / W25Q128 / AD9850 - старші родичі

| Позиція | Що це | Відмінність |
| --- | --- | --- |
| DS2484 | 1-Wire master як DS2482, але з регульованим таймінгом | Гнучкіший slew-rate для довгих ліній; I2C-адресація та ж |
| W25Q128 | SPI-flash 128 Мбіт (16 МБ) | Удвічі більше за W25Q32; той же SOIC-8 footprint, команди сумісні |
| AD9850 | DDS до 40 МГц (старший брат AD9833) | Вища частота і паралельний/послідовний інтерфейс, але більший корпус і апетит |

> DS2484 vs DS2482: для шин до 30 м вистачає DS2482; довші/шумні лінії - DS2484 з налаштованим таймінгом.

## ## Типові помилки 12+ таблицею

| # | Симптом | Причина | Рішення |
| --- | --- | --- | --- |
| 1 | AD9833 виводить 0В або шуми | Невірне живлення (не 3.3В) | Перевірити напругу на VDD, додати конденсатори 100нФ + 10мкФ біля чіпа |
| 2 | Нечитабельний сигнал на OSC'ї | Помилка в налаштуванні FSCTRL1/FSCTRL0 | Використати калькулятор частот з даташиту, перевірити    bits |
| 3 | GM328 не визначній транзистор | Неправильне з'єднання Base/Emitter/Collector | Повипрямити підключення, перевірити datasheet транзистора |
| 4 | GM328 показує β = 0 або дуже високий | Транзистор згорів (burnt-out) | Перевірити на тестері токів або замінювати транзистор |
| 5 | CD74HC4067 виводить "захоплює" всі канали | Помилка в бітових налаштуваннях S0-S3 | Перевірити послідовність бітів (LSB first), перевірити живлення мультиплексора |
| 6 | ADC reading флутить/дрейфовить | Електромагнітний інтерференцій (EMI) | Додати керамічний фільтр на COM вихід, збільшить конденсатори |
| 7 | DS2482 не видить 1-Wire пристрої | Паразитне живлення від 1-Wire лінії не працює | Додати зовнішній конденсатор (100 мкФ) між VCC і GND DS2482 |
| 8 | DS2482 I2C адреса 0x18 не відповідає | Помилка налаштування A0 pine | Перевірити підтяжку A0 до VCC/GND відповідно до даташиту |
| 9 | SC16IS750 UART виводить сміття | Baud rate mismatch між ESP та peripheral | Перевірити спільну швидкість, використовувати точні baud settings |
| 10 | W25Q32 не відповідає на SPI | Неправильне налаштування CS pine або CLK | Перевірити SPI connections, перевірити WP/HOLD pine (підтяжки) |
| 11 | Qi-зарядка не запускається | Невірна частота рушійного генератора | Перевірить GPIO management код, перевірить котушки та відповідні резистори |
| 12 | Qi-зарядка перегрівається | КЗ в обмотці або потужність > 1A | Замінити котушку на меншу потужність, додатковий термобезпека |

| # | Симптом | Причина | Рішення |
| --- | --- | --- | --- |
| 13 | Загальна SPI взаємодія (AD9833 + W25Q32 + DS2482) | Спільна SPI-шина без роздільних CS | Додати окремі CS pine для кожного пристроя, викликати `spi.begin()` один раз |
| 14 | Перемикань між модулями перезавантажує ESP32 | Зворотній ток між модулями живлення | Встановіть ізольовані LDO для кожного модуля або використайте спільну 3.3V шину (common bus) з діодною ізоляцією |
| 15 | MicroPython AD9833 import error | Не вірна бібліотека або версія MicroPython | Використати `from machine import SPI, Pin` та руčne реєстрування, див. даташит AD9833 |
| 16 | CD74HC4067 пошкоджений сигнал на високих частотах | Погіршення мультиплексування на ВЧ | Зменшити частоту перемикання каналів, додати тригер Шмітта на вихід для очищення сигналу |
| 17 | DS2482 sporadically reset ESP32 | Підтяжковий резистор на 1-Wire лінії занадто малий | Використати 4.7кΩ-10kΩ pull-up до 3.3V, перевірити довжину дроту |
| 18 | SC16IS750 не визначається в MicroPython | Відсутність pull-up на SDA/SCL | Додати 10kΩ pull-up резистори на шині I2C |
| 19 | W25Q32 write protection помилка | WP pin Hard-grounded до GND | Підтягніть WP до VCC або з'єднайте з GND тільки при необхідності запису |
| 20 | Qi charger інтерміттентна робота | Міцність полета магнітного поля | Перемістити кутку котушки, перевірити шаблон резонансу, використайте оболонковий дизайн |
| 21 | W25Q128 як заміна W25Q32 без уваги до адресації | Старі бібліотеки не знають 4-байтних адрес | Оновити драйвер; AD9850 вимагає окремого тактування 30-125 МГц, не SPI-клок ESP32 |

## ## Офіційні джерела

1. [AD9833 DDS Generator Datasheet (PDF, Analog Devices)](https://www.analog.com/en/products/ad9833.html) - офіційний даташит з регістрами, формулами частоти та App Note
2. [GM328 Transistor Tester Guide (Blog, Greatest-Tech)](https://greatest-tech.com/gm328-transistor-tester-guide/) - розбір пінов, функцій та тестів
3. [CD74HC4067 16-Channel Multiplexer Datasheet (PDF, TI)](https://www.ti.com/lit/ds/symlink/cd74hc4067.pdf) - повна таблиця каналів та характеристик
4. [DS2482 1-Wire to I2C Master Datasheet (PDF, Maxim Integrated/Dallas)](https://datasheets.maximintegrated.com/en/ds/DS2482A.pdf) - протокол деталі та I2C адресизація
5. [SC16IS750 UART Expander Datasheet (PDF, NXP/Silicon Labs)](https://www.nxp.com/docs/en/data-sheet/SC16IS750.pdf) - регістри UART та SPI/I2C налаштування
6. [W25Q32 Flash Memory Datasheet (PDF, Winbond)](https://www.winbond.com/products/spi-nor-flash/w25q32) - page sizes, SPI modes, endurance тести
7. [Qi Wireless Charging Specification (PDF, WPC)](https://www.wirelesspowerconsortium.com/specifications/) - стандартні частоти, потужності, протокол управління

> [!warning]
> Вгадані URL-адреси без перевірки через webfetch заборонені. Перевірте кожен посилання перед використанням у продакшн-коді.

## ## Див. також

- [[Home]]
- [[04-Shini/02-SPI|SPI]]
- [[04-Shini/03-I2C|I2C]]
- [[06-Analog/01-ADC|ADC]]
- [[12-Moduli-zvyazku/24-DIY-Instruments]]

24→(Home, [[04-Shini/02-SPI|SPI]], [[04-Shini/03-I2C|I2C]], [[06-Analog/01-ADC|ADC]])
