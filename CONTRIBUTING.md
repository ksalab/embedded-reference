# Contributing

This base lives on precision: every note passes three automatic checkers.
Follow the order below and the checks stay green.

## 0. Languages (i18n)

Ukrainian is the first language, not the only one. Rules for translations:

- A translation lives next to the original: `NN-Tema.md` → `NN-Tema.en.md`
  (later `.de.md`, `.pl.md`, …). Same folder, same number.
- Frontmatter gains `lang: en` and `original: NN-Tema.md`; the original gains
  a one-line pointer under its H1: `EN version: [[NN-Tema.en | English]]`.
- A translated note follows the same skeleton (§2) and the same checks (§5).
- `Home.md` stays canonical until a full translated MOC exists; do not
  renumber folders for a translation.

## 1. New note: full cycle (7 steps)

1. File goes into the right folder as `NN-Tema.md` (next free number, no duplicates).
2. Entry in `scripts/generate_schemes.py`, dictionary `C`:
   `"name-scheme.png": ("Title", ["bullet1", …])` — in the note's language,
   hyphen `-` only, no backticks, no `[[ ]]`.
3. Run `python3 scripts/generate_schemes.py` from the vault root → PNG appears.
4. Embed in the note: `![[assets/img/name-scheme.png|600]]` + italic caption
   `*Fig. …*`. No `placeholder.png` in content notes.
5. Row in `assets/README.md` (next number + note + what is shown).
6. `Home.md`: link `[[folder/file | Alias]]` in its section row
   (alias must differ from the file name) + update the `(N notes)` counter.
   Link only to existing files.
7. `CHANGELOG.md` entry for the new version; then
   `python3 scripts/comp_inventory.py --registry COMPONENTS.md`
   (generated file, never edit by hand).

## 2. Mandatory note skeleton

frontmatter → H1 → figure → purpose callout → 6–9 numbered sections →
mermaid → code → `| Symptom | Cause | Fix |` table (6+ rows) →
`## Official sources` (4+ links) → `## See also` (`[[…]]`).

- Tables: `| A | B |`, delimiter `| --- | --- |`, empty cells as `| |`,
  exactly 1 space around cell content.
- Never touch code blocks with bulk text replacements.

## 3. Sources: URL policy

- Never guess URLs. Every link is either `curl`-checked (HTTP 200) or
  websearch-verified (for bot-blocking sites: st.com, analog.com, …).
- Priority: exact model page / manufacturer documentation >
  official docs > aggregators. Placeholders like “check manually” are forbidden.

## 4. Language

- Hyphen `-` only in prose (em/en dashes `—`/`–` forbidden).
- Terminology follows the correspondence table
  (`04-START-Quality-Report-table.md` in the working copy):
  `wires` (not cables-as-prowoda calques), `pins`, `HAT board`, `level shifter`.
- No AI-marker phrases: “Key rule”, “Rule #1”, “Let's not forget”.

## 5. Before committing

```bash
python3 scripts/check_style.py && python3 scripts/check_links.py && python3 scripts/check_home.py
markdownlint "<Vault>/**/*.md"   # from repo root, .markdownlint.yaml applies
python3 tools/export_github.py   # refresh docs/ after changing vaults
```

All three checks at zero, lint clean, `docs/` regenerated.
Otherwise the PR is rejected.
