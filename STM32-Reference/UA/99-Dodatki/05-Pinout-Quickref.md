---
title: Швидка шпаргалка розпіновок STM32 - LQFP/Pin-mapping

description: Швидкий довідник розпіновок для STM32 - зведення ключових пінів (ADC, UART, SPI, CAN, I2C, PWM, DMA) з посиланнями на джерела.
tags: [stm32, pinout, quick-reference, lqfp, gpio, adc, pwm, dma]
category: Hardware
date: 2026-10-06
---

# Швидка шпаргалка розпіновок STM32

| Пін | Назва | Функція | Приклад використання |
| --- | --- | --- | --- |
| PA0 | ADC_IN0 | Аналог вхід | АЦП з датчиком |
| PA1 | ADC_IN1 | Аналог вхід | Аналоговий сигнал |
| PA2 | USART2_TX | UART | Консоль / модем |
| PA3 | USART2_RX | UART | Прийом даних |
| PA4 | ADC_IN4 / DAC | Аналог/ЦАП | Датчик / Аудіо |
| PA5 | SPI1_SCK | SPI такт | Дисплей |
| PA6 | SPI1_MISO | SPI прийом | Датчик |
| PA7 | SPI1_MOSI | SPI передача | Камера |
| PA9 | USART1_TX | UART | Консоль |
| PA10 | USART1_RX | UART | Прийом |
| PA13 | SWDIO | Налагодження | JTAG/SWD |
| PA14 | SWCLK | Налагодження | Такт вибірки |
| PB6 | I2C1_SCL | I2C такт | Датчики |
| PB7 | I2C1_SDA | I2C дані | Датчики |
| PB8 | CAN_RX | CAN прийом | Промислова шина |
| PB9 | CAN_TX | CAN передача | Промислова шина |
| PC6 | I2C3_SCL | I2C такт | Альтернатива |
| PC7 | I2C3_SDA | I2C дані | Альтернатива |
| PC8 | TIM3_CH0 | ШІМ | Серво / LED |
| PC9 | UART3_RX | UART | Консоль |
| PD6 | UART2_RX | UART | Альтернатива |
| PD7 | UART2_TX | UART | Альтернатива |

## Короткі правила

- Аналог: PA0-PA7 | PC0-PC3 (залежить від серії)
- UART: PA9/PA10 або PB10/PB11 - перевірити AF
- SPI: PA5-PA7 або PB3-PB5 - стандарт з MYF для F4
- CAN: PB8/PB9 (F4/F7/H7) - перевірити AF
- I2C: PB6/PB7 (стандарт) або PC14/PC15 (низьке споживання)
- ШІМ: TIM2-TIM5 на різних АФ
- ADC + DMA: PA0 з TIM3 trigger для синхронізації

## Примітка

Кожна серія STM32 (F0, F3, F4, F7, H7, U5, L4) має різні AF-множники на різних пінах. Завжди перевіряйте таблицю кожного чипа з офіційного даташита (STM32CubeMX також генерує).

## 9.1 Швидка шпаргалка розпіновок F4/H7

| Сигнал | Пін (LQFP) | Примітка |
| --- | --- | --- |
| DCMI D0 | PA4 | Камера 8-біт |
| SWDIO | PA13 | Налагодження |
| I2C SDA | PB7 | Датчики 400 кГц |
| CAN_RX | PB8 | Промислова шина |
| SPI MOSI | PB5 | Швидкість 40 МГц |

## Офіційні джерела

- [[01-Hardware/01-F0-F1-Classic|F0/F1-класика]] - місце в лінійці.
- [[01-Hardware/01-F0-F1-Classic | F0/F1-класика]] - місце в лінійці.
- <https://www.st.com/resource/en/reference_manual/rm0091-stm32f0x1-stm32f0x2-stm32f0x8-reference-manual-stmicroelectronics.pdf> (F0/F1)
- <https://www.st.com/resource/en/reference_manual/rm0432-stm32f4-reference-manual-stmicroelectronics.pdf> (F3/F4)
