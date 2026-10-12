---
title: FAQ RaspberryPi-Reference - frequently asked questions and quick answers
description: RaspberryPi base FAQ - power, boot, GPIO, network and typical rake with short answers.; shows schematics, code and tables.
tags: [raspberrypi, faq, troubleshooting, dodatok]
category: Dodatki
lang: en
original: RaspberryPi-Reference/99-Additions/01-Troubleshooting-FAQ.md
date-created: 2026-10-01
date: 2026-10-08
---

# FAQ RaspberryPi-Reference - frequently asked questions and quick answers

## Food

**Lightning on the screen - what to do?**Change the BJ to an official one for the model and a short, thick cable. Check `vcgencmd get_throttled` - should be `0x0`. Details: [[02-Power-Supply/01-USB-C-PD | USB-C power supply].**Which BJ for Pi 5?**
Official PD 27W (5V 5A). It works with BZ 3A, but USB is cut to 600 mA.

**Is it possible to power through a 5V comb?**
Yes, but without reverse polarity protection and with a quality source. USB-C is safer.

## Loading

**ACT flashes 4 times - what is this?**No `start.elf` - broken image or map. Reflash Code table - [loading EEPROM](../../../../RaspberryPi-Reference/UA/09-Proshivka/02-EEPROM-Boot.md).**Not booting from USB/NVMe?**
Order in EEPROM (`BOOT_ORDER`), fresh bootloader firmware, `dtparam=pciex1` for NVMe.

**Forgot your password/don't have SSH?**
Flash from Imager with a new user, data from the backup. Or monitor+keyboard locally.

## GPIO and iron

**Burned the pin with 5 volts - what to do?** Nothing, the pin is dead. Move to a free GPIO and install a level converter. Details: [comb and gpiozero](../../../../RaspberryPi-Reference/UA/03-GPIO/01-Header-Gpiozero.md).**I2C not seeing sensor?**`i2cdetect -y 1`, check SDA/SCL places, braces, SDO address. Details: [tires](../../../../RaspberryPi-Reference/UA/04-Shini/01-I2C-SPI-UART.md).**HAT not detected?**Either it is a shield without EEPROM (manual dtoverlay) or ID pin conflict. Details: [HAT and EEPROM](../../../../RaspberryPi-Reference/UA/03-GPIO/03-HAT-EEPROM.md).
## Network

**WiFi not seeing 5GHz?**The country is not displayed. `raspi-config` → WiFi-country. Details: [ onboard radio].**Network drops every hour?**
WiFi power management. Disable PM, add a watchdog script.

**How to enter from outside without a white IP?**
Tailscale or WireGuard. Port forwarding is a last resort with fail2ban.

## Soft

**`pip install` refuses?**Bookworm protects system Python (PEP 668). Work at venv. Details: [ OS settings].**Service does not start after reboot?**
`enable` was forgotten or the paths are relative. `systemctl status`, absolute paths, `journalctl -u`.

**Old code from raspistill not working?**Stack removed. Rewrite on Picamera2. Details: [ CSI camera].
## Where to search next- Base map: [main map](../../../../RaspberryPi-Reference/Home.md).- Diagnosis by symptoms: [diagnostic card](../../../../RaspberryPi-Reference/UA/99-Dodatki/03-Diagnostic-Map.md) - queue note 4.- Datasheets: [links to datasheets](../../../../RaspberryPi-Reference/UA/99-Dodatki/02-Datasheet-Links.md).

## Common issues

Common issues are documented in the tables above. Verify power supply, clock, and firmware before changing code.


## Official sources

- STMicroelectronics reference manuals and datasheets
- Official ST-Link documentation
- Arduino / Raspberry Pi official guides
