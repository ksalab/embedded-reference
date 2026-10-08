# Contributing

This base lives on precision: every note passes three automatic checkers.
Follow the order below and the checks stay green.

## 0. Languages (i18n)

Ukrainian is the first language, not the only one. Rules for translations:

- A translation lives next to the original: `NN-Tema.md` → `NN-Tema.en.md`
  (later `.de.md`, `.pl.md`, …). Same folder, same number.
- Frontmatter gains `lang: en` and `original: NN-Tema.md`; the original gains
  a one-line pointer under its H1: `EN version: [[NN-Tema.en | English]]`.
- Translated note follows the same skeleton (§2) and the same checks (§5).
- `Home.md` stays canonical until a full translated MOC exists; do not
  renumber folders for a translation.

## 1. New note: full cycle (7 steps)

1. Файл — у правильну папку, ім'я `NN-Tema.md` (наступний вільний номер, без дублів).
2. Запис у `scripts/generate_schemes.py`, словник `C`:
   `"імʼя-scheme.png": ("Заголовок", ["булет1", …])` — українською,
   тільки дефіс `-`, без бектиків і `[[ ]]`.
3. `python3 scripts/generate_schemes.py` з кореня сховища → з'являється PNG.
4. Вставка в ноту: `![[assets/img/імʼя-scheme.png|600]]` + підпис курсивом
   `*Рис. …*`. Жодних `placeholder.png` у контентних нотах.
5. Рядок у `assets/README.md` (наступний номер + нота + що видно).
6. `Home.md`: лінк `[[папка/файл | Аліас]]` у рядок свого розділу
   (аліас відрізняється від імені) + оновити лічильник `(N нот)`.
   Лінкувати тільки на існуючі файли.
7. `CHANGELOG.md` — запис нової версії; потім
   `python3 scripts/comp_inventory.py --registry COMPONENTS.md`
   (файл генерується, руками не правити).

## 2. Обов'язковий скелет ноти

frontmatter → H1 → рисунок → «Призначення» → 6–9 нумерованих розділів →
mermaid → код → таблиця `| Симптом | Причина | Лікування |` (6+ рядків) →
`## Офіційні джерела` (4+ лінки) → `## Див. також` (`[[…]]`).

- Таблиці: `| A | B |`, деліметр `| --- | --- |`, порожні комірки `| |`,
  рівно 1 пробіл навколо вмісту.
- Код поза перевірками тексту не чіпати ніякими масовими замінами.

## 3. Джерела: політика URL

- URL не вигадувати. Кожен лінк — або `curl` з HTTP 200, або підтвердження
  вебпошуком (для сайтів, що ріжуть ботів: st.com, analog.com тощо).
- Пріоритет: сторінка конкретної моделі/документація виробника >
  офіційні docs > агрегатори. Заглушки на кшталт «перевірити вручну» заборонені.

## 4. Мова

- Тільки дефіс `-` у прозі (довгі тире `—`/`–` заборонені).
- Апостроф обов'язковий: `пам'ять`, `ім'я`, `обов'язково`.
- Термінологія за таблицею відповідностей (`04-START-Quality-Report-table.md`):
  `дроти` (не провода), `піни` (не ноги), `HAT-плата` (не шапка),
  `перетворювач рівнів` (не шифтер), `безпосередньо` (не напряму).
- Без AI-маркерів: «Ключове правило», «Правило №1», «Давайте не забути».

## 5. Перед комітом

```bash
python3 scripts/check_style.py && python3 scripts/check_links.py && python3 scripts/check_home.py
markdownlint "<Vault>/**/*.md"   # з кореня репо, діє .markdownlint.yaml
python3 tools/export_github.py   # оновити docs/ після зміни vaults
```

Усі три чеки — в нуль, лінт — чистий, `docs/` — перегенеровано.
Інакше PR не приймається.
