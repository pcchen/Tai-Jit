# Plan 001: MkDocs Project Setup

**Status**: Completed
**Date**: 2025-02-15

## Goal

Set up the 臺日大辭典 digital edition as a functional vertical-text MkDocs site with column-based paging, ruby annotations, and CJK font support.

## Prerequisites

- uv installed
- Git repository initialized
- Sample content file `docs/hong.md` exists

## Files Created (in order)

### 1. `pyproject.toml`

uv-managed Python project:
- `name = "tai-jit"`, `version = "0.1.0"`
- `requires-python = ">=3.10"`
- Dependencies: mkdocs, mkdocs-material, mkdocs-ruby-plugin, pymdown-extensions, fonttools, brotli

### 2. `mkdocs.yml`

MkDocs configuration:
- `site_name: 臺日大辭典`
- Material theme: `language: ja`, `font: false` (custom CJK fonts)
- Plugins: search (with separator), ruby (default delimiters `{` `}` `(` `)`)
- Markdown extensions: pymdownx.superfences, caret, mark, tilde
- Extra CSS: `stylesheets/tategaki-paged.css`
- Nav: index.md + content pages

**Note**: mkdocs-ruby-plugin uses `outer_begin`/`outer_end`/`inter_begin`/`inter_end` config keys (not `outer_start`/`inner_start`). The defaults already use `{` `}` `(` `)`, so no overrides needed.

### 3. `docs/stylesheets/tategaki-paged.css`

Vertical text stylesheet:
- `@font-face` for TaiwaneseKana WOFF2, unicode-range restricted to Taiwanese Kana codepoints
- CSS custom properties: `--cjk-serif` font stack, `--page-gap`, `--column-width`
- `.md-content__inner`: `writing-mode: vertical-rl`, column-based paging, scroll-snap
- Ruby/furigana: `ruby-align: center`, `rt` at 0.5em
- Nav/header/footer/search forced to `writing-mode: horizontal-tb`
- Responsive breakpoints: 76.25em, 600px
- Print: columns removed, full flow, UI hidden

### 4. `docs/index.md`

Landing page:
- Front matter: `hide: [navigation, toc]`
- Title: `# 臺日大辭典`
- Links to dictionary entries using ruby syntax

### 5. Directory Placeholders

- `docs/fonts/.gitkeep` — web fonts (WOFF2)
- `fonts/.gitkeep` — source font files (OTF, SFD)

## Post-Creation Steps

```bash
# Install dependencies
uv sync

# Build and verify
uv run mkdocs build
```

## Verification Checklist

- [x] `uv sync` installs all dependencies
- [x] `uv run mkdocs build` succeeds with no warnings
- [x] Ruby annotations render as `<ruby>漢字<rt>かな</rt></ruby>`
- [x] Circled ideographs (㊀-㊆) display correctly
- [ ] Vertical text flows right-to-left in browser (visual check)
- [ ] Column-based paging with scroll-snap works (visual check)
- [ ] TaiwaneseKana font loads when WOFF2 file is present

## Adding a New Dictionary Entry (reusable steps)

1. Create `docs/<romanization>.md` with entry content
2. Add `- <漢字>: <romanization>.md` to `nav:` in `mkdocs.yml`
3. Add `- [{漢字(reading)}](<romanization>.md)` to `docs/index.md`
4. Run `uv run mkdocs build` to verify

## Lessons Learned

- mkdocs-ruby-plugin config keys are `outer_begin`/`inter_begin` (not `outer_start`/`inner_start`)
- The default delimiters `{` `}` `(` `)` match the project convention, so no config overrides needed
- Material theme `font: false` is required to prevent Google Fonts from overriding custom CJK fonts
