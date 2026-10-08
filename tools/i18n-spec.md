# i18n spec: UA → EN translation rules (strict)

## File layout
- Translation lives next to the original: `NN-Tema.md` → `NN-Tema.en.md`.
- NEVER edit/create anything except the assigned `*.en.md` files.
  UA originals, `Home.md`, `CHANGELOG.md`, scripts are maintained separately.

## Frontmatter (mandatory, first lines)
```yaml
---
title: <translated title>
description: <one translated sentence, ends with "; shows schematics, code and tables.">
tags: [same tags, translated where meaningful]
category: <same>
lang: en
original: <folder>/<NN-Tema.md>
date-created: <same as original>
date: <today YYYY-MM-DD>
---
```

## Content rules
- Faithful full translation, same section order and numbering. Do not shorten,
  do not add new facts, do not drop warnings.
- Code blocks (``` … ```): byte-identical copy, including comments.
- Mermaid blocks: translate node label texts only, keep all syntax (`-->`, `[]`, `{}`).
- Images: keep embeds byte-identical (`![[assets/img/….png|600]]` + caption
  translated to `*Fig. …*`). PNGs are shared between languages.
- Tables: `| A | B |`, delimiter `| --- | --- |`, empty cells `| |`,
  exactly 1 space around content (markdownlint + MD060 gate).
- No em/en dashes (`—`/`–`); hyphen `-` only. No AI-marker phrases
  (“Key rule”, “Rule #1”, “Let's not forget”, “check manually”).

## Links (strict purity: EN links only to EN)
- `[[folder/X | Аліас]]` → `[[folder/X.en | Translated alias]]`
  (alias must differ from the prettified stem).
- `[[folder/X]]` → `[[folder/X.en]]`. Keep `#fragment` suffixes as-is.
- `[[Home]]` → `[[Home.en]]`. Never link `CHANGELOG`/`TODO` from EN notes.
- Map EVERY wikilink, even if the target twin is translated by another batch.
- Length: keep ≥150 lines per note (same as original).

## Glossary (use these, do not invent)
дріт→wire, піни→pins, живлення→power supply, земля→ground (GND),
струм→current, напруга→voltage, опір/резистор→resistor, конденсатор→capacitor,
плата→board, датчик→sensor, прошивка→firmware, завантажувач→bootloader,
переривання→interrupt, таймер→timer, шина→bus, рівень→level (logic),
джерело→source, помилка→issue, причина→cause, лікування→fix,
див. також→see also, офіційні джерела→official sources,
типові помилки→common issues, шпаргалка→cheat sheet,
гребінка→pin header, макетна плата→breadboard, БЖ→PSU,
підтяжка→pull-up, дільник→divider, строби/такти→clock,
сон/deep-sleep→sleep/deep-sleep, сторожовий таймер→watchdog,
залізо→hardware, нота→note, довідник→reference,
маршрут→path, гребінка→header, корпус→package/case (context),
напівпровідник→semiconductor, світлодіод→LED, кнопка→button.
