# Tai-Jit 臺日大辭典

Digital edition of 臺日大辭典 (Taiwan-Japan Grand Dictionary) — a vertical-text (tategaki), right-to-left paged e-book website.

**Live site**: https://pcchen.github.io/Tai-Jit/

## Quick Start

```bash
# Install dependencies
uv sync

# Preview locally at http://127.0.0.1:8000
uv run mkdocs serve

# Build static site
uv run mkdocs build

# Deploy to GitHub Pages
uv run mkdocs gh-deploy --force
```

## Tech Stack

- **uv** — Python package manager
- **MkDocs** + Material theme — static site generator
- **mkdocs-ruby-plugin** — `{漢字(かな)}` furigana syntax
- **CSS vertical writing** — `writing-mode: vertical-rl` with column-based paging

## Project Structure

```
docs/           Markdown content (one file per dictionary entry)
docs/stylesheets/  Vertical text & paging CSS
docs/fonts/     Web fonts (WOFF2)
fonts/          Source font files (OTF, SFD)
plans/          Implementation plans
```

## Content Format

Dictionary entries use ruby annotation syntax and circled ideograph numbering:

```markdown
**ホン** 風。

㊀（姓）{風(ふう)}。

㊁{風(かぜ)}。
{捲螺風(クン𚿸 レエ𚿳 ホン)}＝{旋風(せんぷう)}。
```
