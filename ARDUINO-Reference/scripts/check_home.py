#!/usr/bin/env python3
"""Перевірка Home-навігації Obsidian-бази ARDUINO-Reference.

Що перевіряє:
  1. Лічильники `(N нот)` у рядках Home збігаються з реальною кількістю .md у папці.
  2. Кожна контентна нота згадана в Home хоча б раз (сиріт навігації нема).

Мета-файли (не мусять бути в навігації): CHANGELOG.md, TODO.md, TODO-UNIFY.md,
сам Home.md, _templates/*, scripts/*, assets/*.

Запуск (з кореня vault ARDUINO-Reference):
    python3 scripts/check_home.py

Код виходу: 0 — чисто, 1 — розбіжності (список друкується).
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
META = {"CHANGELOG.md", "TODO.md", "TODO-UNIFY.md", "Home.md", "COMPONENTS.md"}
META_DIRS = {"_templates", "scripts", "assets"}


def main() -> int:
    home = (VAULT / "Home.md").read_text(encoding="utf-8")
    errors: list[str] = []

    # 1. Лічильники `(N нот)` vs файли в папці
    for m in re.finditer(r"\|\s*`([^`]+)`\s*\|[^\n]*?\((\d+) нот\)", home):
        d, claimed = m.group(1), int(m.group(2))
        p = VAULT / d
        if not p.is_dir():
            errors.append(f"нема папки: {d}")
            continue
        actual = len(list(p.glob("*.md")))
        if actual != claimed:
            errors.append(f"{d}: на Home {claimed}, файлів {actual}")

    # 2. Кожна контентна нота — в навігації
    linked: set[str] = set()
    for m in re.finditer(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", home):
        t = m.group(1).strip()
        if t.startswith("assets/") or t.endswith(".png"):
            continue
        linked.add(pathlib.Path(t).stem)
    for p in sorted(VAULT.rglob("*.md")):
        if ".obsidian" in str(p):
            continue
        rel = p.relative_to(VAULT)
        if p.name in META or rel.parts[0] in META_DIRS:
            continue
        if p.stem not in linked:
            errors.append(f"поза Home: {rel}")


    # 3. Форма рядків-навігації: у рядка папки рівно 3 комірки,
    #    лінки 3-ї колонки належать папці рядка (без чужих хвостів)
    for i, ln in enumerate(home.splitlines(), 1):
        s = ln.strip()
        if not s.startswith("|"):
            continue
        masked = re.sub(r"\[\[[^\]]*\]\]", "\x00", s)
        cells = [c.strip() for c in masked.strip("|").split("|")]
        if not cells:
            continue
        fm = re.match(r"`([^`]+)`$", cells[0])
        if not fm:
            continue
        folder = fm.group(1)
        if not (VAULT / folder).is_dir():
            continue
        if len(cells) != 3:
            errors.append(f"рядок {i} ({folder}): комірок {len(cells)}, треба 3")
            continue
        for lm in re.finditer(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", cells[2]):
            tgt = lm.group(1).strip()
            if tgt.startswith("assets/") or tgt.endswith(".png"):
                continue
            if "/" in tgt and not tgt.startswith(folder + "/"):
                errors.append(f"рядок {i} ({folder}): чужий лінк [[{tgt}]]")

    if errors:
        for e in errors:
            print(" ", e)
    print(f"home-errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
