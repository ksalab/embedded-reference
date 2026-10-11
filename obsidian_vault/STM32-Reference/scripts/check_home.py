#!/usr/bin/env python3
"""Перевірка Home-навігації (EN/UA-розкол).

Home.md -> дерево UA/, EN/Home.en.md -> дерево EN/.
  1. Лічильники `(N нот)` / `(N notes)` у рядках збігаються з .md у папці.
  2. Кожна контентна нота згадана у відповідному Home (сиріт нема).
  3. Форма рядків-навігації: рівно 3 комірки, лінки 3-ї колонки належать папці.

Запуск (з кореня vault):  python3 scripts/check_home.py
Код виходу: 0 — чисто, 1 — розбіжності.
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
META = {"CHANGELOG.md", "TODO.md", "TODO-UNIFY.md", "Home.md", "Home.en.md",
        "COMPONENTS.md"}
META_DIRS = {"_templates", "scripts", "assets"}
HOMES = (("Home.md", "UA", re.compile(r"\((\d+) нот[а-я]*\)")),
         ("EN/Home.en.md", "EN", re.compile(r"\((\d+) notes?\)")))


def stem_of(target: str) -> str:
    t = target.split("|", 1)[0].strip().split("#", 1)[0].strip()
    stem = pathlib.PurePosixPath(t).stem
    if stem.endswith(".en"):
        stem = stem[:-3]
    return stem


def main() -> int:
    errors: list[str] = []
    for home_rel, langdir, counter_re in HOMES:
        home_p = VAULT / home_rel
        if not home_p.exists():
            errors.append(f"нема {home_rel}")
            continue
        home = home_p.read_text(encoding="utf-8")

        # 1. Лічильники
        for m in re.finditer(r"\|\s*`([^`]+)`\s*\|[^\n]*?" + counter_re.pattern,
                             home):
            cell, claimed = m.group(1), int(m.group(2))
            cand = VAULT / cell if (VAULT / cell).is_dir() \
                else VAULT / langdir / cell
            if not cand.is_dir():
                errors.append(f"{home_rel}: нема папки: {cell}")
                continue
            actual = len([x for x in cand.glob("*.md")
                          if not x.name.endswith(".en.md")]) \
                if langdir == "UA" else \
                len([x for x in cand.glob("*.en.md")])
            if actual != claimed:
                errors.append(f"{home_rel}: {cell}: на Home {claimed}, "
                              f"файлів {actual}")

        # 2. Сироти навігації
        linked: set[str] = set()
        for m in re.finditer(r"\[\[([^\]]+)\]\]", home):
            t = m.group(1).split("|", 1)[0].strip()
            if t.startswith("assets/") or t.endswith(".png"):
                continue
            if "/" not in t and pathlib.Path(t).suffix in (
                    ".md", "") and t.split("#")[0].strip() in META:
                continue
            linked.add(stem_of(m.group(1)))
        tree = VAULT / langdir
        want: set[str] = set()
        for p in sorted(tree.rglob("*.md")):
            if ".obsidian" in str(p):
                continue
            if p.name in ("Home.md", "Home.en.md"):
                continue
            if p.name in META:
                continue
            rel = p.relative_to(tree)
            if rel.parts[0] in META_DIRS:
                continue
            if langdir == "UA" and p.name.endswith(".en.md"):
                continue
            if langdir == "EN" and not p.name.endswith(".en.md"):
                continue
            stem = p.stem[:-3] if p.stem.endswith(".en") else p.stem
            want.add(stem)
        for stem in sorted(want - linked):
            errors.append(f"{home_rel}: поза Home: {stem}")

        # 3. Форма рядків
        for i, ln in enumerate(home.splitlines(), 1):
            s = ln.strip()
            if not s.startswith("|"):
                continue
            masked = re.sub(r"\[\[[^\]]*\]\]", "\x00", s)
            cells = [c.strip() for c in masked.strip("|").split("|")]
            if not cells:
                continue
            fm = re.match(r"`([^`]+)$", cells[0].rstrip())
            fm = re.match(r"`([^`]+)`$", cells[0])
            if not fm:
                continue
            folder = fm.group(1)
            base = VAULT / folder if (VAULT / folder).is_dir() \
                else VAULT / langdir / folder
            if not base.is_dir():
                continue
            if len(cells) != 3:
                errors.append(f"{home_rel} рядок {i} ({folder}): комірок "
                              f"{len(cells)}, треба 3")
                continue
            for lm in re.finditer(r"\[\[([^\]]+)\]\]", cells[2]):
                tgt = lm.group(1).split("|", 1)[0].strip()
                if tgt.startswith("assets/") or tgt.endswith(".png"):
                    continue
                if "/" in tgt and not (
                        tgt.startswith(folder + "/") or tgt == folder):
                    errors.append(f"{home_rel} рядок {i} ({folder}): чужий "
                                  f"лінк [[{tgt}]]")
    if errors:
        for e in errors:
            print(" ", e)
    print(f"home-errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
