#!/usr/bin/env python3
"""Перепис Home.md -> UA/ дерево, EN/Home.en.md -> EN/ дерево.

- Комірки папок: `UA/<ua-folder>` / `EN/<en-folder>` (EN-мапа з original:).
- Лінки: префікс UA/ або EN/ + справжні EN-імена (мапа через original:).
- Лічильники (N нот)/(N notes) за фактом. [[Home]], CHANGELOG, scripts/,
  assets/, _templates/ не чіпає. UA-оригінали та контент не чіпає.
Запуск з кореня vault: python3 scripts/home_fix.py (потім check_home.py).
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent


def build_maps():
    """UA relpath -> EN relpath (через original:), UA folder -> EN folder."""
    ua_by_name: dict[str, str] = {}
    for p in sorted((VAULT / "UA").rglob("*.md")):
        if ".obsidian" in str(p):
            continue
        ua_by_name.setdefault(p.name, p.relative_to(VAULT).as_posix())
    en_by_stem: dict[str, str] = {}
    orig2en: dict[str, str] = {}
    for p in sorted((VAULT / "EN").rglob("*.en.md")):
        if ".obsidian" in str(p):
            continue
        rel = p.relative_to(VAULT).as_posix()
        en_by_stem.setdefault(p.stem, rel)
        t = p.read_text(encoding="utf-8", errors="ignore")
        m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
        if m:
            mo = re.search(r"^original:\s*(\S+\.md)\s*$", m.group(1), re.M)
            if mo:
                o = mo.group(1)
                parts = o.split("/")
                cands = [o, "UA/" + o] + (
                    ["UA/" + parts[-2] + "/" + parts[-1]]
                    if len(parts) >= 2 else [])
                hit = next((c for c in cands if (VAULT / c).exists()), None)
                if hit is None and o.split("/")[-1] in ua_by_name:
                    hit = ua_by_name[o.split("/")[-1]]
                if hit:
                    orig2en[hit] = rel
    folder_map: dict[str, str] = {}
    for ua_rel, en_rel in orig2en.items():
        up, ep = ua_rel.split("/"), en_rel.split("/")
        if len(up) >= 2 and len(ep) >= 2 and up[0] == "UA" and ep[0] == "EN":
            folder_map.setdefault(up[1], ep[1])
    return ua_by_name, en_by_stem, orig2en, folder_map


def resolve_en(target: str, ua_by_name, en_by_stem, orig2en):
    """UA-подібна ціль Home.en -> справжній EN-шлях або None."""
    t = target.strip()
    if t.startswith("EN/"):
        stem = t[3:]
        stem = stem[:-3] if stem.endswith(".en") else stem
        for cand in (f"EN/{stem}.en.md", f"EN/{stem}.md"):
            if (VAULT / cand).exists():
                return cand[:-3]
    if t.startswith(("assets/", "scripts/", "_templates/")) \
            or t in ("Home", "Home.en.md", "CHANGELOG", "CHANGELOG.md",
                     "TODO", "TODO.md", "COMPONENTS", "COMPONENTS.md") \
            or "/" not in t:
        return None
    base = t[:-3] if t.endswith(".en") else t
    if base.startswith("EN/"):
        base = base[3:]
    folder, _, stem = base.partition("/")
    # 1) точний EN-файл
    for cand in (f"EN/{folder}/{stem}.en.md", f"EN/{folder}/{stem}.md"):
        if (VAULT / cand).exists():
            return cand[:-3] if cand.endswith(".md") else cand
    # 2) через UA-оригінал
    ua_hit = None
    for cand in (f"UA/{folder}/{stem}.md", f"{folder}/{stem}.md"):
        if (VAULT / cand).exists():
            ua_hit = cand
            break
    if ua_hit is None and stem + ".md" in ua_by_name:
        ua_hit = ua_by_name[stem + ".md"]
    if ua_hit and ua_hit in orig2en:
        return orig2en[ua_hit][:-3]
    return None


def fix_home(home_rel: str, langdir: str, counter_word: str,
             ua_by_name, en_by_stem, orig2en, folder_map) -> list[str]:
    p = VAULT / home_rel
    lines = p.read_text(encoding="utf-8").splitlines()
    leftovers: list[str] = []
    out = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("|") and re.match(r"^\|\s*`[^`]+`", s):
            mcell = re.match(r"^(\|\s*`)([^`]+)(`\s*\|)(.*)$", ln)
            if mcell:
                pre, cell, mid, rest = mcell.groups()
                folder = cell.split("/")[-1]
                if langdir == "UA":
                    newcell = f"UA/{folder}" if (VAULT / "UA" / folder).is_dir() \
                        else cell
                    cnt = len([x for x in (VAULT / newcell).glob("*.md")]) \
                        if (VAULT / newcell).is_dir() else 0
                    rest = re.sub(r"\(\d+ нот[а-я]*\)",
                                  f"({cnt} нот)", rest)
                    ln = pre + newcell + mid + rest
                else:
                    enf = folder_map.get(folder, folder)
                    newcell = f"EN/{enf}" if (VAULT / "EN" / enf).is_dir() \
                        else cell
                    epath = VAULT / newcell
                    cnt = len(list(epath.glob("*.en.md"))) \
                        if epath.is_dir() else 0
                    rest = re.sub(r"\(\d+ notes?\)", f"({cnt} notes)", rest)
                    ln = pre + newcell + mid + rest
        def _link(m: re.Match) -> str:
            inner = m.group(1)
            t, _, alias = inner.partition("|")
            t = t.strip()
            if t.startswith(("assets/", "scripts/", "_templates/")) \
                    or "/" not in t or t.split("/")[0] in (
                        "Home", "CHANGELOG", "TODO", "COMPONENTS"):
                return m.group(0)
            if langdir == "UA":
                nt = t if t.startswith("UA/") else f"UA/{t}"
                if (VAULT / nt.split("#")[0]).exists() or \
                        nt.split("#")[0] + ".md" and any(
                        True for _ in [0]):
                    pass
                return "[[" + nt + ("|" + alias if alias else "") + "]]"
            resolved = resolve_en(t, ua_by_name, en_by_stem, orig2en)
            if resolved is None:
                leftovers.append(f"{home_rel}: {t}")
                return m.group(0)
            return "[[" + resolved + ("|" + alias if alias else "") + "]]"
        ln = re.sub(r"\[\[([^\]]+)\]\]", _link, ln)
        out.append(ln)
    p.write_text("\n".join(out) + "\n", encoding="utf-8")
    return leftovers


def main() -> int:
    ua_by_name, en_by_stem, orig2en, folder_map = build_maps()
    left: list[str] = []
    left += fix_home("Home.md", "UA", "нот", ua_by_name, en_by_stem,
                     orig2en, folder_map)
    left += fix_home("EN/Home.en.md", "EN", "notes", ua_by_name, en_by_stem,
                     orig2en, folder_map)
    print(f"leftovers={len(left)}")
    for x in left[:20]:
        print(" ", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
