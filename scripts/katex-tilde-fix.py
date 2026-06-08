#!/usr/bin/env python3
"""mdBook preprocessor: stop KaTeX tilde accents from becoming strikethrough.

mdbook-katex renders math to HTML at *preprocess* time, and KaTeX draws the
`\\tilde{...}` accent as a literal `~` (U+007E) glyph: `<span class="mord">~</span>`.
mdBook then runs that HTML back through pulldown-cmark, whose GFM strikethrough
extension treats a lone `~` as a delimiter. Two `\\tilde` accents in one text run
therefore pair into a spurious `<del>`, striking through the prose between them and
*consuming the accent glyphs* (so `\\tilde{E}` can lose its tilde). In the SGA corpus
this produced 159 spurious `<del>` spans before this fix.

This preprocessor runs immediately after `katex` (see `after` in book.toml) and
HTML-encodes those accent tildes (`>~<` -> `>&#126;<`) before the markdown renderer
sees them. Crucially, pulldown-cmark sees `&#126;` as an entity token (NOT a `~`
strikethrough delimiter) during parsing, so it never pairs; it then decodes the
entity to a plain `~` in the output, so the accent renders correctly. The pattern
`>~<` (a tilde alone between tags) is emitted only by KaTeX; prose/path tildes are
`~word` / `` `~/path` `` and are left untouched.

Stdlib only, no third-party deps, so it runs under the plain `python3` already used
by scripts/generate-summary.py — no uv/venv needed.
"""

import json
import sys


def fix(content: str) -> str:
    return content.replace(">~<", ">&#126;<")


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
