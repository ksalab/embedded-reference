#!/usr/bin/env python3
"""Перевірка ЄДИНОГО ФОРМАТУ нот Obsidian-бази STM32-Reference.

Що перевіряє (стандарт ноти):
  1. frontmatter містить title + description + tags + category + date-created
  2. Є вставка рисунка ![[assets/img/*.png]]
  3. Є ```mermaid-блок
  4. Є секція помилок: "Типові помилки"/"Типові проблеми" або таблиця "| Симптом |"
  5. Є секція "Офіційні джерела"
  6. Довжина ≥150 рядків
  7. title і H1 про одну тему (є спільний токен довжиною 3+)
  8. Чистота скриптів: нема CJK-ієрогліфів/складів (µΩ° — легітимні одиниці!),
     нема зламаного `\\|` всередині [[вікілінків]]
  9. Нема гомогліфів: латинські двійники всередині кириличних слів
     (ekerан, тu, RMOX виправляти; ROMів, Vвх, Tсимволу — легітимні винятки!)

Винятки (не контентні ноти, стандарт не застосовується):
  CHANGELOG.md, TODO.md, TODO-UNIFY.md, Home.md,
  _templates/*, scripts/README.md, assets/README.md,
  99-Dodatki/* (навігація/списки — інший жанр),
  00-Start/* (навігація — інший жанр)

Запуск (з кореня vault STM32-Reference):
    python3 scripts/check_style.py

Код виходу: 0 — нуль порушень, 1 — є порушення (список друкується).
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent

SKIP = {
    "CHANGELOG.md", "TODO.md", "TODO-UNIFY.md", "Home.md",
    "Component-Template.md", "README.md", "COMPONENTS.md",
}
SKIP_DIRS = {"_templates", "99-Dodatki"}

CHECKS = ("frontmatter", "image", "mermaid", "errors", "sources", "length")

# Латинські літери-двійники кириличних (візуальні гомогліфи)
HOMO_LAT = set("aceijkmnoprstuvwyxACEHKMNOPRTX")

# Легітимні винятки: [повний збіг слова] — акронім+відмінок, формули
HOMO_ALLOW = re.compile(
    r"^(?:"
    r"[A-Z]{2,}[а-яіїєґ]{1,3}"      # ROMів, PIN-код основа, MOSI — ні (дефіс), RMOX — ні
    r"|[VRIPUTQFSCL][а-яіїєґ]+"      # Vвх, Rниз, Tсимволу, Pпотужність
    r"|[VRIPUTQFSCL]\d"              # V2, R1 — позначення на схемі
    r")$"
)

# CJK: ієрогліфи + кана + хангиль. Легітимні µΩ° сюди НЕ входять.
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")


def strip_code(text: str) -> str:
    """Прибрати фіксовані блоки коду (перевірки тексту — тільки проза!)."""
    return re.sub(r"```.*?```", "", text, flags=re.S)


def word_homoglyphs(word: str) -> bool:
    """Латинський двійник усередині кириличного СЕГМЕНТА слова?

    Слово ріжеться по дефісах/слешах: MQTT-топологія, TLS-сесія,
    CA-сертифікат — легітимні композити (сегменти чисті).
    Працює всередині сегмента: ekerан, тu, пH, RAЕON, Matriс.
    """
    for seg in re.split(r"[-/–—]", word):
        core = seg.strip("0123456789_+.%,:;()[]\"'")
        if not core or HOMO_ALLOW.match(core):
            continue
        has_cyr = any("\u0400" <= ch <= "\u04ff" for ch in core)
        has_homo = any(ch in HOMO_LAT for ch in core)
        if has_cyr and has_homo:
            return True
    return False


def check_file(p: pathlib.Path) -> list[str]:
    bad: list[str] = []
    text = p.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ["no-frontmatter"]
    fm = m.group(1)
    for field in ("title:", "description:", "tags:", "category:", "date"):
        if field == "date":
            if not re.search(r"^date", fm, re.M):
                bad.append("no-date")
        elif field not in fm:
            bad.append("no-" + field.rstrip(":"))
    # 10. description: ≥8 слів І (дієслово-присудок АБО карта змісту ≥2 ';')
    dm = re.search(r"^description:\s*(.+)$", fm, re.M)
    if dm:
        d = dm.group(1).strip()
        is_en = bool(re.search(r"^lang:\s*en\s*$", fm, re.M))
        if is_en:
            verb = re.search(
                r"(\bis\b|\bare\b|explains|shows|covers|provides|describes|helps|"
                r"compares|lists|teaches|guides|gives|offers|contains|includes|"
                r"\bfor\b|\bto\b|\bwith\b|\band\b|how\b)", d, re.I)
        else:
            verb = re.search(
            r"(є |є,|дає|має|працює|використовується|призначений|забезпечує|дозволяє|"
            r"вимірює|керує|читає|містить|підтримує|вміє|служить|опис|огляд|гайд|розбір|"
            r"йдеться|потрібно|треба|можна|показує|пояснює|будує|збирає|закриває|"
            r"відповідає|будуємо|охоплює|за допомогою|\bдля\b|щоб|[а-яіїєґ](ти|тись|тися|ться)\b)", d, re.I)
        content_map = d.count(";") >= 2
        enum_list = bool(re.search(r":\s*\S.{5,}?,\s*\S", d))
        definition = " — " in d or " – " in d
        if not (len(d.split()) >= 8 and (verb or content_map or definition or enum_list)):
            bad.append("bad-description")
    if not re.search(r"!\[\[assets/img/", text):
        bad.append("no-image")
        bad.append("no-image")
    if "```mermaid" not in text:
        bad.append("no-mermaid")
    is_en_doc = bool(re.search(r"^lang:\s*en\s*$", fm, re.M))
    if is_en_doc:
        err_ok = bool(re.search(r"Common (issues|problems)|\| Symptom \|", text))
    else:
        err_ok = bool(re.search(r"Типові (помилки|проблеми)|\| Симптом \|", text))
    if not err_ok:
        bad.append("no-errors")
    src_ok = ("Official sources" in text) if is_en_doc else ("Офіційні джерела" in text)
    if not src_ok:
        bad.append("no-sources")
    if text.count("\n") + 1 < 150:
        bad.append("thin")
    # 7. title vs H1: спільний токен 3+
    tm = re.search(r"^title:\s*(.+)$", fm, re.M)
    h1 = re.search(r"^# (.+)$", text[m.end():], re.M)
    if tm and h1:
        toks = lambda s: {w for w in re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ0-9]+", s.lower()) if len(w) >= 3}
        if not (toks(tm.group(1)) & toks(h1.group(1))):
            bad.append("bad-h1-title")
    # 8. биті пайпи у вікілінках
    if re.search(r"\[\[[^\]]*\\\|", text):
        bad.append("bad-pipe")
    # 8б. транслітеровані аліаси (наслідки автогенерації): аліас == префікс стема
    for m in re.finditer(r"\[\[([^\]|#]+?)\|([^\]]+?)\]\]", text):
        tgt, alias = m.group(1).strip(), m.group(2).strip()
        if "/" not in tgt:
            continue
        stem = tgt.split("/")[-1]
        pretty = re.sub(r"^\d+-", "", stem).replace("-", " ")
        if alias == pretty and len(alias.split()) >= 2:
            bad.append("bad-alias")
            break
    # 8-9. скрипти — тільки поза кодом!
    prose = strip_code(text[m.end():])
    if CJK.search(prose):
        bad.append("bad-script")
    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ0-9][A-Za-zА-Яа-яІіЇїЄєҐґ0-9\-/]*", prose)
    if any(word_homoglyphs(w) for w in words):
        bad.append("bad-homoglyph")
    return bad


def main() -> int:
    files = [p for p in VAULT.rglob("*.md") if ".obsidian" not in str(p)]
    total_viol = 0
    by_check: dict[str, int] = {c: 0 for c in CHECKS}
    by_check["no-frontmatter"] = 0
    for p in sorted(files):
        rel = str(p.relative_to(VAULT))
        base_name = p.name[:-len(".en.md")] + ".md" if p.name.endswith(".en.md") else p.name
        if base_name in SKIP or p.name in SKIP or rel.split("/")[0] in SKIP_DIRS:
            continue
        bad = check_file(p)
        if bad:
            total_viol += len(bad)
            for b in bad:
                by_check[b] = by_check.get(b, 0) + 1
            print(f"{rel}: {', '.join(bad)}")
    def _counted(p):
        base_name = p.name[:-len(".en.md")] + ".md" if p.name.endswith(".en.md") else p.name
        return base_name not in SKIP and p.name not in SKIP and str(p.relative_to(VAULT)).split("/")[0] not in SKIP_DIRS
    checked = len([p for p in files if _counted(p)])
    print(f"checked={checked} violations={total_viol} {by_check}")
    return 1 if total_viol else 0


if __name__ == "__main__":
    sys.exit(main())
