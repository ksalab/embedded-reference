#!/usr/bin/env python3
"""Перевірка цілісності Obsidian-бази ARDUINO-Reference.

Що перевіряє:
  1. Всі [[wikilink]]-посилання ведуть на існуючі .md нотатки (за stem імені файла).
  2. Всі вбудовані `assets/img/*.png` реально існують (крім xxx.png — приклад в документації).

Запуск (з кореня vault ARDUINO-Reference):
    python3 scripts/check_links.py

Код виходу: 0 — все чисто, 1 — є биті посилання або відсутні картинки.
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    files = list(VAULT.rglob("*.md"))
    basenames = {p.stem for p in files}
    broken: dict[str, int] = {}
    total = 0
    for p in files:
        text = p.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", text):
            target = m.group(1).strip()
            if target.startswith("assets/") or target.endswith(".png"):
                continue
            total += 1
            if pathlib.Path(target).stem not in basenames:
                broken[target] = broken.get(target, 0) + 1

    have = {p.name for p in (VAULT / "assets" / "img").glob("*.png")}
    missing: set[str] = set()
    for p in files:
        for m in re.finditer(r"assets/img/([A-Za-z0-9_.\-]+\.png)",
                             p.read_text(encoding="utf-8", errors="ignore")):
            name = m.group(1)
            if name not in have and name != "xxx.png":
                missing.add(name)

    print(f"files={len(files)} links={total} broken={len(broken)}")
    for k, v in sorted(broken.items(), key=lambda x: -x[1])[:20]:
        print(f"  {v}x BROKEN [[{k}]]")
    print(f"png: have={len(have)} missing={sorted(missing) if missing else 'NONE'}")
    return 1 if (broken or missing) else 0


if __name__ == "__main__":
    sys.exit(main())
