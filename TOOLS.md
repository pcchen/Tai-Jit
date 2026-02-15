# TOOLS.md

Tools and dependencies used in this project.

## Package Manager

| Tool | Purpose | Install |
|------|---------|---------|
| [uv](https://docs.astral.sh/uv/) | Python package & project manager | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

## Python Dependencies (`pyproject.toml`)

| Package | Version | Purpose |
|---------|---------|---------|
| mkdocs | 1.6.x | Static site generator |
| mkdocs-material | 9.x | Material Design theme |
| mkdocs-ruby-plugin | 0.0.3 | `{漢字(かな)}` → `<ruby>` conversion |
| pymdown-extensions | 10.x | Markdown extensions (superfences, caret, mark, tilde) |
| fonttools | 4.x | Font inspection, subsetting, conversion |
| brotli | 1.x | WOFF2 compression (used by fonttools) |

## MkDocs Plugins (configured in `mkdocs.yml`)

| Plugin | Configuration |
|--------|--------------|
| search | `separator: '[\s\-\.]+'` |
| ruby | Default delimiters: `{` `}` outer, `(` `)` inner |

## MkDocs Markdown Extensions

| Extension | Purpose |
|-----------|---------|
| pymdownx.superfences | Fenced code blocks with extras |
| pymdownx.caret | `^^insert^^` and `^superscript^` |
| pymdownx.mark | `==highlight==` |
| pymdownx.tilde | `~~delete~~` and `~subscript~` |

## Development Commands

```bash
# First-time setup
uv sync

# Local preview server
uv run mkdocs serve

# Production build
uv run mkdocs build

# Font subsetting example (future use)
uv run fonttools subset input.otf --output-file=output.woff2 --flavor=woff2 --unicodes="U+31F0-31FF,U+1B130-1B16F"
```

## Directory Conventions

| Directory | Contents | Served? |
|-----------|----------|---------|
| `docs/fonts/` | WOFF2 web fonts | Yes (via MkDocs) |
| `fonts/` | Source OTF/SFD files | No (build inputs only) |
| `site/` | Built output (gitignored) | Deployment target |
