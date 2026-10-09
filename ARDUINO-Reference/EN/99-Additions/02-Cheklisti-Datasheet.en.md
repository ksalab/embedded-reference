---
title: Checklist and date Arduino
description: Explains startup and custom board checklists, official sources for datasheets, schematics, and key documents of the Arduino ecosystem.; shows schematics, code and tables.
tags: [arduino, checklist, datasheet]
category: Dodatki
lang: en
original: ARDUINO-Reference/99-Additions/02-Cheklisti-Datasheet.md
date-created: 2026-10-05
date: 2026-10-08
---

# Check and date the Arduino
![[assets/img/arduino-checklist-scheme.png|600]]
*Rice. Paper checklists for the first start-up and a set of key documents: data sheets, diagrams, output maps.*

> [!tip] Note assignment
> Collect pre-startup checklists and document maps in one place: where to get datasheets, circuit boards, and which sections to read first.

## 1. Purpose

A checklist is a memory on paper: it does not get tired, does not rush, and does not miss points.
The first launch without a checklist turns into a lottery: luck or smoke.
A datasheet is a passport of a component: all limits, all modes, all pitfalls in one file.
Newbies are afraid of datasheets because of the volume, but you don't have to read the whole thing: five key sections are enough.
The note gives two lists: the first launch of the finished board and the verification of the board of its own design.
Next - a map of sources: official site, manufacturers of microcircuits, manufacturers of modules.
Final - key documents of the ecosystem: what to download and put next to the workplace.

## 2. Checklist for the first launch of the finished board

| Number | Item | How to check |
| --- | --- | --- |
| 1 | Review of the board under a magnifying glass | There are no solder bridges, cracks, blown capacitors
| 2 | Completeness and version | The name and revision match the documentation |
| 3 | Cable with data lines | The port appears when the card is connected |
| 4 | The environment sees port | The list of ports responds to disconnect |
| 5 | Blink cast passes | The LED flashes with a period of one second |
| 6 | Bus five volts is normal | The multimeter shows from 4.75 to 5.25 |
| 7 | Bus three and three volts are normal | The multimeter shows from 3.2 to 3.4 |
| 8 | The quiescent current corresponds to the norm | The USB tester shows tens of milliamps |
| 9 | The reset button works | Pressing restarts the flashing from the beginning |
| 10 | The port monitor shows the text | The speeds match, there is no garbage |```text
Protocol for the first launch (fill in by hand):Date ............ Fee ............ Revision ....Cable: [ ] data is Port: ................5V = ...... 3V3 = ...... Quiescent current = ......Blink: [ ] yes Reset: [ ] yes Monitor: [ ] clearSignature ............ Next step ............```
Items go from cheap to expensive: visual inspection, then cable, then power, then code.
Not a single point is missed: they are crossed out only after the actual check, and not from memory.
Failure at an item stops the list: do not go further until the item turns green.
The completed protocol is kept: in the case of a repeated problem, it is clear what was already the norm.
The first launch is done on a table without modules: bare board, cable, multimeter - nothing else.

## 3. Checklist of your board before turning it on

| Number | Item | How to check |
| --- | --- | --- |
| 1 | The scheme is verified with the board | Each track starts and ends where it should |
| 2 | The power supply is not closed to the ground | The callout shows a gap between the tires |
| 3 | Polarity of electrolytes Strip minus to the ground, plus to the power bus |
| 4 | The first pin of each chip | The case key matches the key on the silkscreen |
| 5 | Ratings of resistors of braces | Marking corresponds to the scheme, there are no breaks |
| 6 | Junction near each chip | One hundred nanofarads close to the power pins
| 7 | Quartz and its capacitors Denominations according to the datasheet, tracks are short
| 8 | The programming connector is available | The probes or the adapter reach all contacts |
| 9 | The current limit on the unit is set | One hundred milliamps before the first switch |
| 10 | The fire extinguisher is metaphorical next to it Hand on the switch, eyes on the board for the first seconds```text
Обхід своєї плати перед першим вмиканням:
  1. Продзвони плюс on землю: писку бути not повинно.
  2. Продзвони землю on корпус роз'ємів: писк має бути.
  3. Перевір полярність кожного електроліта окремо.
  4. Приклади лінійку: висота деталей not заважає корпусу.
  5. Подай живлення via межу and дивися on струм.
  6. Струм нульовий -> шукай обрив, великий -> шукай коротке.
```
The board is turned on in two stages: first power without chips, then complete assembly.
Without microcircuits, the tires are checked: the voltage is normal, there is no heating, the current is negligible.
Panels for microcircuits on the first board are not a shame, but insurance against resoldering.
A photo of both sides before turning on is mandatory: after the repair, you will not be able to prove how it was.

## 4. Where to get datasheets: source map

| Source | What lies there | When to go there |
| --- | --- | --- |
| Official website of the project Circuit boards, output maps, characteristics | First stop for any branded board |
| The microcircuit manufacturer's website Data sheet, errata, application examples Exact boundaries, regimes, registers |
| Site of the manufacturer of the module | Scheme of the module, description of outputs, libraries | The module does not behave according to the lesson |
| Board Repository | Gerbera, specification, list of details | Repetition or repair of someone else's board |
| Forum and project tracker | Known rakes and fixes | The problem is similar to the mass |

Priority of sources: the manufacturer is more important than the lesson, the datasheet is more important than the forum.
Lessons become outdated in a year, a data sheet lives for decades: check the numbers with the original source.
Compare the revision of the document with the revision of the iron: the old scheme for the new board gives wrong advice.
Save the datasheet file locally with the version in the name: sites move, links rot.
A questionable PDF from a file exchange is the last hope: look for the same document from the manufacturer.

## 5. Key ecosystem documents

| Document | What is inside | Read first |
| --- | --- | --- |
| ATmega328P datasheet | Memory, power, timers, ADC, interfaces | Electrical characteristics and limits of conclusions |
| Circuit board Uno | Stabilizer, USB bridge, solution, reset | Power circuit and reset button |
| Circuit board Nano | USB converter, compact wiring | Power differences from a large board |
| Map of board outputs | Correspondence of pins to functions | PWM, interrupts, buses at a glance |
| Downloader Description | Filling protocol, fuses | When the filling does not work or the chip is bare
| Errata chips | Known errors of the crystal | When everything is according to the datasheet and does not work```text
The five sections of the datasheet that are read first:1. Features ............ features on one page2. Pinout .............. pin map and alternate functions3. Electrical ........... limits of voltages, currents, temperatures4. Clock ................ clock sources and start5. Typical application .. a sample of the binding from the manufacturerThe rest is read point by point, as needed by the project.```
You don't need to read the complete eight-hundred-page datasheet in a row: it's a reference book, not a novel.
Bookmarks in the browser save hours: register table, interrupt map, binding example.
Electrical characteristics are sacred: the absolute maximums are never exceeded, even for a short time.
The typical application section is copied into their scheme: the manufacturer has already stepped on this rake.

## 6. Self-check with a sketch after the checklists```cpp
// Фінальний Bills of health: живлення, пам'ять, шина.
// Проганяють після кожного чекліста, цифри записують у протокол.
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("Health check start");
  Serial.print("A0 ref = ");
  Serial.println(analogRead(A0));
  Serial.print("Free RAM = ");
  Serial.println(freeRam());
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("Health check done");
}

void loop() {
}

int freeRam() {
  extern int __heap_start, *__brkval;
  int v;
  return (int)&v - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);
}
```
The numbers of the run are recorded in the protocol next to the measurements of the multimeter.
Free memory of less than two hundred bytes is a reason to reduce buffers before connecting modules.
The readings of the ADC on the known divider are checked with a multimeter: the discrepancy is sought in the ground.

## 7. Mermaid: from a question to a document```mermaid
flowchart TB
S[Need number or fact] --> Q{What are you looking for}Q -->|Leg or function| Pin[Board Pin Map]Q -->|Power or limit| El [Electricity section in the datasheet]Q -->|Node diagram| Sch[Official fee scheme]Q -->|Crystal Bug| Err[Manufacturer's Errata]Q -->|Code example| Lib[Library repository and examples]Pin --> V[Bill revision of payment and document]    El --> V
    Sch --> V
    Err --> V
    Lib --> V
V --> OK[Save PDF locally with version in name]```
## Typical errors

| # | Error | Why bad | How correct |
| --- | --- | --- | --- |
| 1 | The first run without a checklist | Missed item price in fee | Go through the list from top to bottom, cross out the fact |
| 2 | Reading the datasheet from the middle at random | You destroy boundaries and burn conclusions Start with five sections: Functions, Foams, Electrics |
| 3 | Scheme of another fee revision | Tips are no match for iron | Make a revision on the text sheet and in the document |
| 4 | Trusting the lesson instead of the manufacturer | Lessons become obsolete, numbers float | Figures only from the manufacturer's data sheet
| 5 | Link without local copy | The site has moved, the document is lost Save PDF with version in filename |
| 6 | Turning on your board to full without limit | The first mistake becomes the last | One hundred milliampere limits and a hand on the switch

## Official sources

- [Arduino documentation - schematics, pin maps, characteristics](https://docs.arduino.cc/hardware/) - the first stop for board documents.
- [ATmega328P datasheet - chip manufacturer](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf) - a complete passport of a classic chip.
- [Arduino UNO R3 - schematic and board files](https://docs.arduino.cc/hardware/uno-rev3/) - sample circuit, solution and power supply.

## See also- [[Home | Home]]
- [[00-Start/01-Yak-koristuvatis-dovidnikom | reference guide]]
- [[01-Hardware/01-AVR-Uno | classic AVR]]
- [[17-Lab/02-Maketka-PCB | layout and board]]
- [[99-Additions/01-Troubleshooting-FAQ | answers to questions]]


## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.
