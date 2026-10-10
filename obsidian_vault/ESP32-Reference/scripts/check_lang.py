#!/usr/bin/env python3
"""Мовна чистота двомовної бази (UA + *.en.md).

Перевіряє:
  1. Кожен *.en.md має frontmatter `lang: en` + `original: X.md`, і X.md існує.
  2. UA-ноти (не .en) не посилаються на .en-цілі взагалі.
  3. EN-ноти посилаються тільки на .en-цілі (assets/png — можна).
     Виняток міграції: EN→UA лінк, чий .en-двійник ЩЕ НЕ створено,
     рахується як `pending` (беклог, не помилка). EN→UA лінк, чий двійник
     вже існує, — помилка `cross` (забули перемапити).

Вихід: 0 — чисто (pending не валить); 1 — є cross/UA2EN/frontmatter помилки.

Запуск (з кореня vault):
    python3 scripts/check_lang.py
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
META_DIRS = {"_templates", "scripts", "assets"}
META_FILES = {"CHANGELOG.md", "TODO.md", "TODO-UNIFY.md", "COMPONENTS.md"}

LINK = re.compile(r"\[\[([^\]]+)\]\]")


def body_lines(text: str):
    """Рядки поза fenced-блоками (звичайними і цитатними)."""
    out, plain, qinf = [], False, False
    for ln in text.splitlines():
        if re.match(r"^\s*```", ln) and not re.match(r"^\s*>+\s*```", ln):
            plain = not plain
            continue
        if plain:
            continue
        if re.match(r"^\s*>+\s*```", ln):
            qinf = not qinf
            continue
        if qinf:
            continue
        out.append(ln)
    return out


def split_target(inner: str) -> str:
    t = inner.split("|", 1)[0].strip()
    return t.split("#", 1)[0].strip()


def main() -> int:
    errors: list[str] = []
    pending: list[str] = []
    en_files = sorted(VAULT.rglob("*.en.md"))
    en_stems = {p.stem for p in en_files}  # "X.en"
    all_stems = {p.stem for p in VAULT.rglob("*.md") if ".obsidian" not in str(p)}

    for p in en_files:
        rel = p.relative_to(VAULT)
        text = p.read_text(encoding="utf-8", errors="ignore")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        fm = m.group(1) if m else ""
        if not re.search(r"^lang:\s*en\s*$", fm, re.M):
            errors.append(f"{rel}: нема frontmatter lang: en")
        mo = re.search(r"^original:\s*(\S+\.md)\s*$", fm, re.M)
        if not mo:
            errors.append(f"{rel}: нема frontmatter original: X.md")
        elif not (VAULT / mo.group(1)).exists() and (VAULT / mo.group(1)).name not in all_stems:
            # original може лежати в підпапці: шукаємо за stem
            stem = pathlib.Path(mo.group(1)).stem
            if stem not in all_stems:
                errors.append(f"{rel}: original {mo.group(1)} не існує")
        for ln in body_lines(text):
            for lm in LINK.finditer(ln):
                tgt = split_target(lm.group(1))
                if not tgt or tgt.startswith("assets/") or tgt.startswith("scripts/") or tgt.endswith(".png"):
                    continue
                pp = pathlib.PurePosixPath(tgt)
                stem = pp.stem
                if pp.suffix == ".en" and (stem + ".en") in all_stems:
                    continue
                if stem + ".en" in all_stems or (stem + ".en") in en_stems:
                    errors.append(f"{rel}: UA-ціль [[{tgt}]] має .en-двійника — перемапити")
                else:
                    pending.append(f"{rel}: [[{tgt}]] (двійник ще не створений)")

    for p in sorted(VAULT.rglob("*.md")):
        if ".obsidian" in str(p) or p.name.endswith(".en.md"):
            continue
        rel = p.relative_to(VAULT)
        if p.name in META_FILES or (len(rel.parts) > 1 and rel.parts[0] in META_DIRS):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for ln in body_lines(text):
            for lm in LINK.finditer(ln):
                tgt = split_target(lm.group(1))
                if re.search(r"\.en(\||#|$)", lm.group(1)):
                    errors.append(f"{rel}: UA→EN лінк [[{tgt}]]")

    for e in errors:
        print(" ", e)
    print(f"lang-errors={len(errors)} pending-en-twins={len(pending)}")
    if pending and "--verbose" in sys.argv:
        for x in pending:
            print("  ~", x)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
