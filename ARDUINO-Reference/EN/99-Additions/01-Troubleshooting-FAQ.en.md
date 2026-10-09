---
title: Troubleshooting Arduino - questions and answers
description: Explains system diagnostics of common Arduino faults: symptom table, solution tree, minimal examples of bug reproduction and order of checks.; shows schematics, code and tables.
tags: [arduino, faq, debug]
category: Dodatki
lang: en
original: ARDUINO-Reference/99-Additions/01-Troubleshooting-FAQ.md
date-created: 2026-10-05
date: 2026-10-08
---

# Troubleshooting Arduino - questions and answers

![[assets/img/arduino-faq-scheme.png|600]]
_Rice. Diagnostic map: from symptom through cause to solution in five steps._

> [!tip] Note assignment
> Give a quick self-help map: symptom, most likely cause, solution, and a minimal example that reproduces or disproves the bug.

## 1. Purpose

When the board does not work, it is tempting to change everything at once: code, wires, board, computer.
The right way is shorter: one symptom, one hypothesis, one check at a time.
The note collects frequently asked questions in the symptom-cause-solution table: the answer is in a minute.
The decision tree below leads from a dead board to a working setup without any unnecessary moves.
Minimal examples cut off half the suspicion: pure Blink is more honest than a thousand lines of project.
The order of checks goes from cheap to expensive: cable, port, power, code, iron.
Write down what you checked: the log saves hours when repeating the problem.

## 2. Big table: symptom, cause, solution

| Symptom                                                                                                                                                                                                                                                                                                                                                                                                                     | The most likely cause                                                              | Solution                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| The sketch does not load, access error                                                                                                                                                                                                                                                                                                                                                                                      | The port is occupied by a monitor or another program                               | Close the port monitor, select the correct port, repeat                 |
| The port disappeared from the list                                                                                                                                                                                                                                                                                                                                                                                          | Bad cable with no data lines or bridge driver                                      | Replace the cable with a tested one, install the converter driver       |
| Pouring begins and breaks                                                                                                                                                                                                                                                                                                                                                                                                   | Power sag or autoreboot failed                                                     | Short cable, press manual reset at the time of filling                  |
| The sketch remains, but does not start                                                                                                                                                                                                                                                                                                                                                                                      | Freezes while waiting for a port or at the start of a program                      | Remove port waiting without timeout, add flashing at start              |
| Garbage in port monitor                                                                                                                                                                                                                                                                                                                                                                                                     | The monitor speed does not match the sketch                                        | Put the same speed on both sides, start with 9600                       |
| The I2C sensor is silent                                                                                                                                                                                                                                                                                                                                                                                                    | Wrong address, no power or weak braces                                             | Run the bus scanner, check the power and ground of the module           |
| The stabilizer is heated Output overload or input voltage too high                                                                                                                                                                                                                                                                                                                                                          | Remove the load, reduce the input voltage, add a radiator                          |
| The sketch does not fit into the memory                                                                                                                                                                                                                                                                                                                                                                                     | Rows and buffers ate flash or RAM Transfer lines to program memory, reduce buffers |
| The board is rebooted in cycles                                                                                                                                                                                                                                                                                                                                                                                             | The start current exceeds the power supply                                         | Separate power supply for engines, electrolyte for the bus, thick wires |
| Works on USB, silent on battery                                                                                                                                                                                                                                                                                                                                                                                             | The battery is dead or does not draw current                                       | Measure the voltage under the load, take a fresh source```text          |
| A quick survey of the dead charge in one minute:Is the power on? ......... no -> USB cable, socket, fuseIs the port visible? ............... no -> data cable, bridge driverIs the filling going? .............. no -> the monitor is closed, the board is selected correctlyStart flashing? ........... no -> hangs at the start, simplify the setupData in the monitor? .......... no -> speed, terrain, signal levels``` |

## 3. Does not overflow: step-by-step analysis

| Step | Verification                                                                                    | How to understand that a step has been passed                         |
| ---- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1    | The board is chosen precisely and                                                               | The name of the board coincides with the inscription on the textolite |
| 2    | The port is selected correctly The port disappears from the list when the board is disconnected |
| 3    | Data cable                                                                                      | The port can be seen through it and the Blink                         |
| 4    | The port monitor is closed                                                                      | No window holds the port while pouring                                |
| 5    | The bridge driver is installed                                                                  | The chip near the USB is recognized by the system                     |
| 6    | Manual reset in the fill window                                                                 | The LED flashed, the filling started                                  |

An access error almost always means a busy port: a monitor, a plotter, or a second copy of the environment.
A synchronization error hints at someone else's bootloader: choose the appropriate item in the processor menu.
Clones with a cheap bridge need a driver: without it, the port will never appear.
A long cable through a hub without power is a classic of interruptions: stick the board directly into the computer.
If the fill breaks on a large sketch - try minimal Blink: it will cut off the code problem.

## 4. The port has disappeared: cable, driver, iron

| Sign | Diagnosis Action |
| --- | --- | --- |
| The port was there, disappeared after the new cable | Cable only for charging | Return the old cable or bundle with data lines |
| The port never appeared No USB bridge driver | Install the driver for your bridge chip
| The port disappears when you touch | Socket soldering crack | Solder the socket or replace the board |
| There is a port, but the filling is silent | Bootloader erased | Flash the bootloader through the programmer |
| The entire USB bus hangs | A short on the board puts a tire | Disconnect immediately, ring the power |```text
Тест кабелю за десять секунд:

1. Увімкни USB-тестер між кабелем and платою.
2. Струм росте at підключенні -> живлення йде.
3. Порт with'явився in системі -> лінії даних цілі.
4. Живлення є, порту нема -> кабель зарядний, у смітник.

````
## 5. The sketch does not start: the insidious start of the program

| Trap at the start | Why hang | Medicines
| --- | --- | --- |
| Waiting for port without timeout | There is never a port on battery power Wait no longer than two seconds or remove the wait |
| The sensor does not respond at the start | The waiting cycle of the sensor is infinite | Add a try counter and continue without the sensor |
| Long calibration with flashing | The board seems to be dead | One short flash at the start, details later
| Global buffers are out of memory | A stack meets a pile of | Reduce buffers, lines in program memory |

The golden rule of starting: the LED should flash in the first second after power is applied.
There is no flashing - there is a problem with the power supply or at the start of the program, do not read the code further.
It blinked and hung up - place the beacons: it blinks after each stage of the start.
Beacons show the exact stopping place better than any guess.

## 6. Garbage in the monitor and I2C silence

| Symptom on the tire | The reason | Verification |
| --- | --- | --- |
| Hieroglyphs instead of text | The speed of the monitor is different Set the same speed, start with 9600 |
| The text is torn to pieces The land is not shared or the levels are not the same Common land, levels agreed |
| I2C scanner sees nothing | Module without power | Measure the power directly on the pins of the module |
| The address is not the same as in the lesson | Revision of the module is different Trust the scanner, not the lesson |
| The data is there, but the values ​​are strange | The byte order is scrambled | Read passport: high byte first or not |

The bus scanner is the first sketch for any silent module: it answers the question about the address.
Check the tire tensioners with a multimeter without power: a short circuit gives infinity, a short circuit gives zero.
Two drivers on the same bus with different speeds - guaranteed garbage: only one.

## 7. The stabilizer and a large sketch are warming up

| The problem | Border | Output |
| --- | --- | --- |
| Heating of the linear stabilizer | The finger does not hold - already too much | Lower the input voltage or unload the output |
| The fall on the stabilizer is big | The input-output difference is multiplied by the current | Live logic directly from five volts
| Flash exhausted | The fill was rejected by the linker | Remove the monster libraries, simplify the lines |
| Operational exhausted | Strange falls at work | Smaller buffers, saving every byte |
| Rows eat up memory | Each line is duplicated in operational | Save the texts in the program memory |

Assessment of heating without a thermometer: warm - the norm, hot - a reason to count, scalding - turn off.
The heating power is equal to the voltage drop multiplied by the current: it is calculated on the knee in seconds.
Ten volts of difference at half an amp is five watts of heat: this is a sentence for a small body.

## 8. A minimal example to reproduce the bug```cpp
// Minimal bug report in the code: only the suspect node.// If the glitch is gone, the cleaned code is to blame, return it in pieces.// If it remains, this node or the iron is to blame.#include <Wire.h>

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
digitalWrite(LED_BUILTIN, HIGH);  // beacon: start passed  Wire.begin();
  Serial.println("Scan start");
}

void loop() {
  static unsigned long last = 0;
  if (millis() - last > 1000) {
    last = millis();
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
    Serial.print("tick free=");
    Serial.println(freeRam());
  }
}

int freeRam() {
  extern int __heap_start, *__brkval;
  int v;
  return (int)&v - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);
}
````

The rules of the minimal example: one file, no third-party libraries, with a start beacon.
The example must fit on the screen: more than fifty lines is no longer the minimum.
Three facts are added to the example: what I expected, what I received, what I already checked.
Without these facts, any question turns into a guess.

## 9. Mermaid: diagnostic decision tree```mermaid

flowchart TB
S[Плата not працює] --> P{Порт видно in системі}
P -->|Ні| C[Міняй кабель and став драйвер моста]
P -->|Так| U[Пробуй залити чистий Blink]
U --> UQ{Заливка пройшла}
UQ -->|Ні| M[Закрий монітор and тисни скидання вручну]
UQ -->|Так| B{Світлодіод блимає}
B -->|Ні| W[Шукай зависання on старті програми]
B -->|Так| App[Залізо живе, копай code проекту]
App --> Mem{Падіння випадкові}
Mem -->|Так| Pow[Перевір живлення and нагрів стабілізатора]
Mem -->|Ні| Bus[Скануй шини and звіряй швидкості]

````
## 10. Diagnostic levels: L1, L2, L3

| Level | What are we doing? Tool | Time |
| --- | --- | --- | --- |
| L1 Quick fix | Cable, port, reset button, example Blink | Eyes and IDE | 5 minutes
| L2 Software and config | Board in IDE, libraries, speed, SRAM | Monitor, verbose log | Hour |
| L3 Depth | Oscilloscope power supply, failure, revision | Multimeter, oscilloscope Day |```text
Escalation rule:L1 did not help twice - go to L2, do not change cables for an hour;L2 did not help - a minimal sketch and measure the iron (L3).```
## 11. Decision Tree: The port is gone```mermaid
flowchart TB
    S[Порту нема] --> CAB{Інший кабель з даними?}
    CAB -->|Ні| TRY[Спробуй свідомо data-кабель]
    CAB -->|Так| DRV{Драйвер моста стоїть?}
    DRV -->|Ні| INST[CH340/CP2102 з сайту виробника]
    DRV -->|Так| HUB{Через хаб?}
    HUB -->|Так| DIRECT[Безпосередньо в компютер!]
    HUB -->|Ні| BRD[Інша плата або порт — локалізуй]
````

## 12. The tree of decisions: warms and bounces```mermaid

flowchart TB
H[Hot LDO or rebuts] --> LOAD{What is powered by the board?}LOAD -->|Motors/Relays| SEP [Separate BZ immediately!]LOAD -->|Sensors only| CUR [Measure the current with a multimeter]CUR --> HIGH{More than half an amp?}HIGH -->|Yes| SEPHIGH -->|No| VINP[What is the voltage at VIN?]VINP --> HOT{Over 12 V?}HOT -->|Yes| DOWN [Reduce to 7-9 V]HOT -->|No| SHORT [Search short by dialing]```

## 13. War stories: how it was (B1-B5)

#

## B1. The charging cable ate up the evening

| Field      | Record                                    |
| ---------- | ----------------------------------------- |
| Symptom    | There is no port at all                   |
| Dimension  | The same port with a different cable - is |
| The reason | Thin cable without data lines             |
| Fix        | Mark data cables with insulating tape     |

#

## B2. The monitor holds the port

| Field      | Record                                       |
| ---------- | -------------------------------------------- |
| Symptom    | Pouring fails with a busy port               |
| Dimension  | Closed monitor - filling is in progress      |
| The reason | Two processes on one COM                     |
| Fix        | Close the monitor and plotter before pouring |

#

## B3. 9V on VIN and hot LDO

| Field      | Record                               |
| ---------- | ------------------------------------ |
| Symptom    | Rebut every minute                   |
| Dimension  | LDO burns, current 400 mA            |
| The reason | A drop of 9→5 V heats the stabilizer |
| Fix        | VIN 7.5 V or a separate buck         |

#

## B4. The I2C address is not the same

| Field      | Record                                       |
| ---------- | -------------------------------------------- |
| Symptom    | The sensor is silent from example            |
| Dimension  | Scanner showed 0x3F instead of 0x27          |
| The reason | The revision of the I2C adapter is different |
| Fix        | Scanner before each new module               |

#

## B5. SRAM ate the strings

| Field      | Record                                  |
| ---------- | --------------------------------------- |
| Symptom    | Accidental drops on long texts          |
| Dimension  | There are 200 bytes of free RAM         |
| The reason | Rows in SRAM instead of Flash           |
| Fix        | F() and PROGMEM everywhere in the texts |

## Typical errors

| #   | Error                                                                                           | Why bad                                                                           | How correct                                     |
| --- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------- |
| 1   | Change everything at once without a hypothesis It is not clear what helped, the bug will return | One check at a time, results log                                                  |
| 2   | Faith lesson instead of tire scanner                                                            | Module addresses differ by revision                                               | The scanner shows the actual address            |
| 3   | Waiting for port without timeout                                                                | The sketch hangs forever on the battery Timeout two seconds or start without port |
| 4   | Ignoring stabilizer heating                                                                     | Thermal protection gives cyclic restarts                                          | Calculate the power, unload the output          |
| 5   | Long cable through passive hub                                                                  | Pouring breaks and phantom bugs                                                   | Pay directly to the computer with a short cable |
| 6   | A question without a minimal example                                                            | No one will reproduce the bug and help One file, start beacon, three facts        |

## Official sources

- [Arduino - upload issues guide](https://support.arduino.cc/hc/en-us/sections/360003198300-Upload-issues) - ports, drivers, uploader.
- [Arduino - Language Help and Bus Scanner Example](https://docs.arduino.cc/learn/communication/wire/) - Exchange library and examples.
- [ATmega328P datasheet - watchdog and reset](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf) - causes of resets and freezes.

## See also- [[Home | Home]]

- [[09-Firmware/01-IDE-CLI | environment and CLI]]
- [[09-Firmware/02-Bootloader-AVRDUDE | bootloader and avrdude]]
- [[17-Lab/01-Priladi | measuring devices]]
- [[99-Additions/02-Cheklisti-Datasheet | lists and datasheets]]

## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.
