#!/usr/bin/env python3
"""Експорт Obsidian-сховищ у GitHub-сумісний Markdown (docs/).

Що конвертує:
  [[папка/нота | Аліас]] -> [Аліас](../../Vault/папка/нота.md)
  [[Нота]]               -> [Нота](../../Vault/Нота.md)
  ![[assets/img/x.png|600]] -> ![](відносний шлях до PNG сховища)
Callout'и (> [!tip]), mermaid, frontmatter — GitHub рендерить нативно,
тому лишаються як є. PNG не копіюються, docs/ посилається на оригінали.

Запуск з кореня репо:  python3 tools/export_github.py
"""
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
VAULTS = ["ESP32-Reference", "STM32-Reference", "ARDUINO-Reference", "RaspberryPi-Reference"]
OUT = ROOT / "docs"

WIKILINK = re.compile(r"(!?)\[\[([^\]]+)\]\]")
MDLINK = re.compile(r"!?\[[^\]]*\]\([^)]*\)")


def build_stem_map(vault: pathlib.Path) -> dict:
    """stem файлу -> відносний шлях від кореня сховища (перший збіг)."""
    m: dict = {}
    for p in sorted(vault.rglob("*.md")):
        if ".obsidian" in str(p):
            continue
        m.setdefault(p.stem, p.relative_to(vault).as_posix())
    return m


def convert_link(target: str, alias: str | None, src_dir: pathlib.PurePosixPath,
                 vault: str, stems: dict) -> str:
    target = target.strip()
    if target.startswith("assets/") or target.endswith(".png"):
        return "![](%s)" % target  # не wikilink, лишити (обробиться окремо)
    frag = ""
    if "#" in target:
        target, frag = target.split("#", 1)
        frag = "#" + frag
    rel = stems.get(pathlib.PurePosixPath(target).stem)
    if rel is None:
        return "[%s]" % (alias or target)  # нерозв'язаний: звичайний текст
    text = alias.strip() if alias else pathlib.PurePosixPath(target).stem
    href = os.path.relpath(f"{vault}/{rel}", str(src_dir)) + frag
    return "[%s](%s)" % (text, href)


def convert_line(ln: str, doc_path: pathlib.PurePosixPath, vault: str, stems: dict) -> str:
    src_dir = doc_path.parent

    def _img(m: re.Match) -> str:
        inner = m.group(1)
        parts = inner.split("|", 1)
        path = parts[0].strip()
        href = os.path.relpath(f"{vault}/{path}", str(src_dir))
        return "![](%s)" % href

    ln = re.sub(r"!\[\[([^\]]+)\]\]", _img, ln)

    def _link(m: re.Match) -> str:
        inner = m.group(2)
        if "|" in inner:
            t, a = inner.split("|", 1)
        else:
            t, a = inner, None
        return convert_link(t, a, src_dir, vault, stems)

    return WIKILINK.sub(_link, ln)


def main() -> None:
    n = 0
    for vault in VAULTS:
        vp = ROOT / vault
        stems = build_stem_map(vp)
        for src in sorted(vp.rglob("*.md")):
            if ".obsidian" in str(src):
                continue
            rel = src.relative_to(vp)
            dst = OUT / vault / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            lines = src.read_text(encoding="utf-8", errors="ignore").splitlines()
            out, in_fence = [], False
            for ln in lines:
                if re.match(r"^\s*```", ln):
                    in_fence = not in_fence
                    out.append(ln)
                    continue
                if in_fence:
                    out.append(ln)
                    continue
                doc_path = pathlib.PurePosixPath("docs", vault, rel.as_posix())
                out.append(convert_line(ln, doc_path, vault, stems))
            dst.write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8")
            n += 1
    print(f"exported {n} files -> docs/")


if __name__ == "__main__":
    main()
