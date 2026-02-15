# CLAUDE.md

## Project Overview

Digital edition of 臺日大辭典 (Taiwan-Japan Grand Dictionary) — a vertical-text (tategaki), right-to-left paged e-book website built with MkDocs.

## Tech Stack

- **Package manager**: uv (`pyproject.toml`)
- **Site generator**: MkDocs 1.6 with Material theme (`mkdocs.yml`)
- **Ruby plugin**: mkdocs-ruby-plugin — converts `{漢字(かな)}` to `<ruby>` HTML
- **CSS**: Vertical writing mode (`writing-mode: vertical-rl`) with column-based paging
- **Language**: Python >=3.10 for utilities

## Project Structure

```
├── pyproject.toml                  # uv project & dependencies
├── mkdocs.yml                      # MkDocs configuration
├── docs/
│   ├── index.md                    # Landing page (dictionary index)
│   ├── hong.md                     # Dictionary entry: 風 (ホン)
│   ├── stylesheets/
│   │   └── tategaki-paged.css      # Vertical text & paging layout
│   └── fonts/                      # Web fonts (WOFF2) — served to browser
│       └── .gitkeep
└── fonts/                          # Source font files (OTF, SFD) — build inputs
    └── .gitkeep
```

## Commands

```bash
# Install dependencies
uv sync

# Preview site locally (http://127.0.0.1:8000)
uv run mkdocs serve

# Build static site to site/
uv run mkdocs build
```

## Key Conventions

### Ruby (furigana) Notation

The site uses mkdocs-ruby-plugin with default delimiters:
```
{漢字(かな)}  →  <ruby>漢字<rt>かな</rt></ruby>
```

### Dictionary Entry Format

- **Headword**: Bold with kana reading, e.g. `**バァ𚿲** {肉(bah)}`
- **Definitions**: Numbered with circled ideographs `㊀㊁㊂...` (not Arabic numerals)
- Mixed Japanese and Taiwanese (Taiwanese Kana) content

### Content Language

Content is historical Taiwanese-Japanese. UI and documentation use a mix of Taiwanese, Japanese, and English.

### Adding a New Dictionary Entry

1. Create `docs/<romanization>.md` with the entry content
2. Add to `nav:` in `mkdocs.yml`
3. Add a link in `docs/index.md`

## Working with Content

- When editing dictionary entries, preserve the original text faithfully — this is historical document transcription
- Use `{漢字(かな)}` syntax for all ruby annotations
- Use circled ideographs `㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉` for definition numbering (1-10)

## CSS Architecture (`docs/stylesheets/tategaki-paged.css`)

- **Font**: TaiwaneseKana (WOFF2, unicode-range restricted) + CJK serif fallback stack
- **Layout**: `writing-mode: vertical-rl` on `.md-content__inner`, column-based paging with scroll-snap
- **Navigation/header/footer**: forced `writing-mode: horizontal-tb` (stays horizontal)
- **Responsive**: breakpoints at 76.25em and 600px
- **Print**: columns removed, full vertical flow
