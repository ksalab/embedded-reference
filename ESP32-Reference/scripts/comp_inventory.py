#!/usr/bin/env python3
"""Інвентаризація компонентів Obsidian-бази ESP32-Reference.

Що робить:
  1. Збирає позначення компонентів (токени LETTERS+DIGITS) з тіл нот (без коду).
  2. Фільтрує шум: піни (AD0, RXD3), периферія (GPIO12, MWDT1), AT-команди,
     appnotes (AN11740), роки/версії.
  3. Класифікує посилання секцій «Офіційні джерела»: виробники vs інші.
  4. Друкує зведені числа + JSON для ручної валідації вибірки.

Методологія зафіксована в звіті (TODO P4): токени ^[A-Z]{2,}[0-9]…,
поріг валідності — ручна вибірка n=40 (~80% справжніх → ≈700 компонентів).

Запуск (з кореня vault ESP32-Reference):
    python3 scripts/comp_inventory.py [--json out.json] [--registry COMPONENTS.md]

Код виходу: завжди 0 (інформаційний скрипт, не валідатор).

Режим --registry генерує COMPONENTS.md (НЕ редагувати вручну!):
позначення | розділи | ноти-згадки | datasheet ✅/❌.
✅ означає: хоча б в одній ноті-згадці є посилання виробника —
НЕ гарантує, що лінк саме на цей компонент! Звіряти вручну.
COMPONENTS.md свідомо поза валідаторами (автогенерація, див. SKIP/META).
"""
import json
import os
import pathlib
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import urlparse

VAULT = pathlib.Path(__file__).resolve().parent.parent

SKIP_NAMES = {"TODO.md", "TODO-UNIFY.md", "CHANGELOG.md", "Home.md",
              "COMPONENTS.md"}  # + автогенерований реєстр!
SKIP_DIRS = {".obsidian", "_templates", "scripts", "assets"}

PERIPH = re.compile(
    r"^(GPIO|RTC|MCLK|ADC|AIN|DAC|BOOT|CPU|BUTTON|BLK|CONFIG|TIM|GPT|MCPWM|PCNT"
    r"|RMT|TWAI|EFUSE|QEMU|WIFI|BLE|USB|OTG|JTAG|PSRAM|FLASH|CH|LED|PWM|I2C|SPI"
    r"|UART|SDIO|EMAC|RMII|SMI|RGB|RV32|ROLE|STORE|SF)([0-9]+[A-Z]?)?$")
PIN = re.compile(
    r"^(AD|AO|DO|DI|AI|INT|RST|TX|RX|CS|CK|DA|CL|STB|SEG|COM|DG|BD|BO|BS|AR"
    r"|SR|D|Q|T|U|J|P|R|Y|SCK|SCL|SDA|MOSI|MISO)[0-9]+[A-Z]?$")
IOREG = re.compile(
    r"^(BAUD|DAT|DIN|DOUT|DB|BCK|DIO|AIO|CHT|CRC|BCC|BLK|MWDT|PIO|POWER"
    r"|IPX|GDO|GPSPI|LRCK|BW|BK|VSPI|HSPI|FSPI)[0-9]+[A-Z]?$")
ATCMD = re.compile(r"^(ATE|ATH|ATL|ATI|A0|ATD|ATA|ATZ)[0-9]*$")
TOKEN = re.compile(r"\b([A-Z]{2,}[0-9][A-Z0-9]*)(-[A-Z]{2,}[0-9][A-Z0-9]*)*\b")

MFR = ['espressif', 'ti.com', 'analog.com', 'bosch-sensortec', 'sensirion.com',
 'st.com', 'infineon.com', 'microchip.com', 'nxp.com', 'onsemi.com', 'semtech.com',
 'nordicsemi', 'u-blox.com', 'ublox', 'simcom.com', 'quectel.com', 'winbond.com',
 'wch.cn', 'adafruit.com/learn', 'learn.adafruit', 'sparkfun.com/learn',
 'dfrobot.com/wiki', 'seeedstudio.com', 'wiki.seeedstudio', 'docs.arduino.com',
 'arduino.cc', 'docs.micropython.org', 'micropython.org', 'amazonaws.com',
 'aws.amazon.com', 'docs.aws.amazon.com', 'learn.microsoft.com', 'azure.microsoft.com',
 'platformio.org', 'ovt.com', 'omnivision', 'eastron', 'asaair', 'adafruit.com/datasheets',
 'firebase.google', 'shelly-api-docs', 'supabase.com', 'prometheus.io', 'qorvo',
 'oasis-open', 'mqtt.org', 'chirpstack.io', 'thethingsnetwork.org', 'modbus.org',
 'wch-ic', 'alldatasheet.com', 'alldatasheet', 'datasheets.com', 'octopart.com', 'findchips.com',
 'olimex.com', 'waveshare.com', 'waveshare.net', 'docs.m5stack.com', 'm5stack.com',
 'docs.heltec.org', 'heltec.cn', 'adafruit.com/product', 'lilygo', 'wemos.cc',
 'sigfox.com', 'lora-alliance.org', 'bluetooth.com', 'wi-fi.org',
 'usb.org', 'ipc.org', 'jlcpcb.com', 'pcbway.com', 'eclipse.org', 'apache.org',
 'freeRTOS.org', 'freertos.org', 'kernel.org', 'python.org', 'micropython.org',
 'raspberrypi.com', 'stm32', 'st.com', 'renesas.com', 'rohm.com', 'vishay.com',
 'murata.com', 'tdk.com', 'abracon.com', 'ecsxtal', 'taiyo-yuden', 'avx.com',
 'bourns.com', 'te.com', 'molex.com', 'jst-mfg', 'hirose.com', 'amphenol',
 'allegro', 'melexis.com', 'honeywell.com', 'ams-osram', 'osram', 'luminus.com',
 'cree.com', 'nichia.co', 'everlight.com', 'lite-on', 'liteon.com', 'kingbright',
 'vishay.com', 'on.com', 'diodes.com', 'nexperia.com', 'infineon.com', 'st.com',
 'toshiba', 'fujitsu', 'panasonic', 'omron', 'idec', 'phoenixcontact', 'wago.com',
 'weidmueller', 'rockwellautomation', 'siemens.com', 'schneider-electric',
 'abb.com', 'eaton.com', 'honeywell.com', 'emerson.com', 'yokogawa', 'keysight.com',
 'tek.com', 'rigol', 'siglent', 'fluke.com', 'keithley', 'ni.com', 'pickering',
 'saleae.com', 'dslogic', 'dreamource', 'sigrok.org', 'openocd.org', 'gcc.gnu.org',
 'cmake.org', 'ninja-build.org', 'espressif.com', 'components.espressif.com']


def iter_md():
    for root, dirs, files in os.walk(VAULT):
        if ".obsidian" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                yield pathlib.Path(root) / f


def body_of(p: pathlib.Path) -> str:
    c = p.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r"^---\n(.*?)\n---\n(.*)", c, re.S)
    b = m.group(2) if m else c
    return re.sub(r"```.*?```", "", b, flags=re.S)


def main() -> int:
    out_json = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None
    out_reg = sys.argv[sys.argv.index("--registry") + 1] if "--registry" in sys.argv else None
    cnt: Counter = Counter()
    comp_files: dict[str, set] = defaultdict(set)
    note_hosts: dict[str, set] = defaultdict(set)
    mfr_notes: set[str] = set()
    src_notes = 0
    for p in iter_md():
        rel = str(p.relative_to(VAULT))
        if p.name in SKIP_NAMES or rel.split("/")[0] in SKIP_DIRS:
            continue
        body = body_of(p)
        for m in TOKEN.finditer(body):
            for t in m.group(0).split("-"):
                t = t.strip()
                if len(t) < 4:
                    continue
                if PIN.match(t) or PERIPH.match(t) or ATCMD.match(t) or IOREG.match(t):
                    continue
                if re.match(r"^AN\d+$", t):
                    continue
                if re.search(r"20[12]\d", t):
                    continue
                cnt[t] += 1
                comp_files[t].add(rel)
        prosa = re.sub(r"```.*?```", "", body, flags=re.S)
        idx = body.find("Офіційні джерела")
        if idx >= 0:
            src_notes += 1
        if True:
            for um in re.finditer(r"https?://([A-Za-z0-9.\-]+)", prosa):
                host = um.group(1).lower()
                if any(k in host for k in MFR):
                    note_hosts[rel].add(host)
                    mfr_notes.add(rel)
    print(f"components-unique={len(cnt)} notes-with-mfr-link={len(mfr_notes)}/{src_notes}")
    if out_json:
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump({"freq": dict(cnt),
                       "files": {k: sorted(v) for k, v in comp_files.items()},
                       "mfr_notes": sorted(mfr_notes)},
                      f, ensure_ascii=False)
        print(f"wrote {out_json}")
    if out_reg:
        write_registry(out_reg, cnt, comp_files, note_hosts)
    return 0


SECTIONS = {
    "10-Sensori": "сенсори", "11-Vivid": "вивід/актуатори",
    "12-Moduli-zvyazku": "модулі зв'язку", "13-Moduli-zhivlennya-rivniv": "живлення/рівні",
    "14-Devboards": "плати", "01-Hardware": "чипи/модулі", "16-Proekti": "проєкти",
    "15-Protokoli": "протоколи", "17-Lab": "лабораторія", "02-Zhivlennya": "живлення",
    "06-Analog": "аналог", "00-Start": "старт", "03-GPIO": "gpio",
    "04-Shini": "шини", "05-Radio": "радіо", "07-Timeri-Son": "таймери",
    "08-Pamyat": "пам'ять", "09-Proshivka": "прошивка", "99-Dodatki": "додатки",
}


def write_registry(path: str, cnt: Counter, comp_files: dict, note_hosts: dict) -> None:
    import datetime
    rows = []
    with_ds = 0
    for t in sorted(cnt):
        files = sorted(comp_files[t])
        secs = sorted({f.split("/")[0] for f in files})
        hosts: set[str] = set()
        for f in files:
            hosts |= note_hosts.get(f, set())
        sec_names = ", ".join(SECTIONS.get(s, s) for s in secs)
        notes = ", ".join(f.split("/")[-1].replace(".md", "") for f in files[:4])
        if len(files) > 4:
            notes += f" +{len(files) - 4}"
        if hosts:
            with_ds += 1
            ds = "✅ " + ", ".join("`" + h + "`" for h in sorted(hosts)[:3])
        else:
            ds = "❌"
        rows.append((t, sec_names, notes, ds))
    stamp = datetime.date.today().isoformat()
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Реєстр компонентів ESP32-Reference\n\n")
        f.write(f"> Згенеровано {stamp}: `python3 scripts/comp_inventory.py --registry COMPONENTS.md`. "
                "НЕ редагувати вручну — перегенерувати!\n>\n")
        f.write("> ✅ = хоча б в одній ноті-згадці є посилання виробника. "
                "Це НЕ гарантує, що лінк саме на цей компонент — звіряти вручну!\n>\n")
        f.write("> ❌ = у жодній ноті-згадці нема виробничих посилань. "
                "Пріоритетні кандидати на додавання даташитів.\n\n")
        f.write(f"**Позначень:** {len(rows)}; **з datasheet:** {with_ds}; **без:** {len(rows) - with_ds}.\n\n")
        f.write("## Де шукати даташити (перевірено 2026-09-30)\n\n")
        f.write("| Сайт | Доступ ботом | Профіль |\n")
        f.write("| --- | --- | --- |\n")
        f.write("| alldatasheet.com (`view.jsp?Searchword=XXX`) | ❌ напряму (403), ✅ через проксі/браузер; є дзеркала `alldatasheetru.com` та ін. | Найбільший архів; китайські/хобі-мікросхеми (GalaxyCore, Tontek, Holtek) |\n")
        f.write("| datasheets.com (`/search?q=XXX`) | ✅ | Західні каталогові + ціни/залишки (Microchip, TI, NXP); китайських дисплеїв/сенсорів нема |\n")
        f.write("| octopart.com (`/search?q=XXX`) | ✅ | Метапошук дистриб'юторів; тільки авторизовані канали — хобі-Китаю нема |\n")
        f.write("| findchips.com (`/search/XXX`) | ✅ | Те саме, що Octopart, швидший |\n")
        f.write("| lcsc.com (пошук на сайті) | ❌ JS — тільки вручну | Китайські компоненти: картка + PDF одразу |\n")
        f.write("| tme.eu / mouser.com / digikey.com | ❌ боти ріжуться — вручну | Параметричний пошук + гарантовано свіжий PDF виробника |\n")
        f.write("| alltransistors.com | ❌ боти ріжуться — вручну | Біполярники/MOSFET/діоди (BC547, SS14) |\n")
        f.write("| datasheetspdf.com | ❌ нестабільний — вручну | Дзеркало архіву |\n")
        f.write("| Сайти виробників (першоджерело!) | ✅ | `ti.com/lit`, `analog.com`, `nxp.com`, `st.com`, `microchip.com/en-us/product/XXX` — завжди свіжіше за агрегатори |\n\n")
        f.write("| Компонент | Категорії | Ноти-згадки | Datasheet |\n")
        f.write("| --- | --- | --- | --- |\n")
        for t, sec_names, notes, ds in rows:
            f.write(f"| {t} | {sec_names} | {notes} | {ds} |\n")
    print(f"wrote {path}: {len(rows)} rows, with-ds={with_ds}")


if __name__ == "__main__":
    sys.exit(main())
