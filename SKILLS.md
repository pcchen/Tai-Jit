# SKILLS.md

Skills and knowledge needed to work on this project.

## Content Transcription

- Reading historical Japanese/Taiwanese dictionary entries
- Understanding Taiwanese romanization systems (POJ / Pe̍h-ōe-jī)
- Taiwanese Kana (台湾語仮名) — extended katakana for Taiwanese phonetics
- Circled ideograph numbering: ㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉ (maps to 1-10)

## MkDocs & Material Theme

- MkDocs configuration (`mkdocs.yml`) — nav, plugins, theme settings
- Material theme customization — `font: false` for custom CJK fonts, `language: ja`
- mkdocs-ruby-plugin — `{base(annotation)}` syntax for furigana
- PyMdown Extensions — superfences, caret, mark, tilde

## CSS / Vertical Text

- `writing-mode: vertical-rl` — right-to-left vertical flow
- `text-orientation: mixed` — CJK upright, Latin sideways
- CSS multi-column layout (`column-width`, `column-gap`, `column-fill`)
- `scroll-snap-type` / `scroll-snap-align` for page-like scrolling
- `@font-face` with `unicode-range` for selective font loading
- `break-inside: avoid` to prevent splitting entries across columns
- Responsive design for vertical text layouts

## Font Engineering

- fonttools / brotli for font subsetting and WOFF2 conversion
- Unicode ranges for Taiwanese Kana: U+31F0-31FF, U+1B130-1B16F, U+1ABFE-1AC0F
- CJK serif font stack for cross-platform rendering

## Python / uv

- uv for dependency management (`pyproject.toml`, `uv sync`, `uv run`)
- Python >=3.10
