#!/usr/bin/env python3
"""mdBook preprocessor: stop KaTeX glyphs from colliding with markdown inline syntax.

mdbook-katex renders math to HTML at *preprocess* time, then mdBook runs that HTML
back through pulldown-cmark. Two KaTeX glyphs are literal characters that the
markdown parser then mis-reads, corrupting the surrounding HTML:

  ~  (the `\\tilde` / `\\widetilde` accent, `<span class="mord">~</span>`)
     A lone `~` is a GFM strikethrough delimiter; two accents in one text run pair
     into a spurious `<del>`, striking through the prose between them and *consuming
     the accent glyphs*. In the SGA corpus this produced 159 stray `<del>` spans.

  \\  (`\\backslash`, `<span class="mord">\\</span>`)
     A `\\` immediately before the span's closing `<` is read as a markdown
     backslash-escape of that `<`, so the `</span>` is turned into escaped text
     (`&lt;/span&gt;`) and the `<span>` is left unclosed — mdBook then warns
     "unclosed HTML tag `<span>`" and the math renders broken. In the SGA corpus
     `\\backslash` appears 100+ times (quotient notation `F\\backslash G`).

Both are fixed the same way: HTML-encode the offending glyph as a numeric character
reference (`~` -> `&#126;`, `\\` -> `&#92;`). pulldown-cmark sees the entity as a
single token during parsing — NOT a strikethrough delimiter, NOT an escape — so it
never mis-pairs or eats the tag; it then decodes the entity back to the literal glyph
in the output, so the math still renders correctly.

This runs immediately after `katex` (see `after` in book.toml). The patterns `>~<`
and `>\\<` (a glyph alone between tags) are emitted only by KaTeX; prose/path tildes
and backslashes are `~word` / `` `\\foo` `` and never match.

Stdlib only, no third-party deps, so it runs under the plain `python3` already used
by scripts/generate-summary.py — no uv/venv needed.
"""

import json
import sys

# (KaTeX-emitted glyph between tags) -> (numeric character reference).
REPLACEMENTS = (
    (">~<", ">&#126;<"),  # \tilde accent vs GFM strikethrough
    (">\\<", ">&#92;<"),  # \backslash vs markdown backslash-escape
)


def fix(content: str) -> str:
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)
    return content


def walk(items) -> None:
    for item in items:
        chapter = item.get("Chapter") if isinstance(item, dict) else None
        if not chapter:
            continue
        if chapter.get("content"):
            chapter["content"] = fix(chapter["content"])
        if chapter.get("sub_items"):
            walk(chapter["sub_items"])


def main() -> int:
    # `mdbook` asks `<cmd> supports <renderer>`; exit 0 to claim support.
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        return 0
    _context, book = json.load(sys.stdin)
    # mdBook 0.5 names the top-level list "items" (0.4 used "sections").
    walk(book.get("items", book.get("sections", [])))
    json.dump(book, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
