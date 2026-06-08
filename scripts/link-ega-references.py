#!/usr/bin/env python3
"""Turn plain-text EGA citations in the SGA translation into links to the EGA book.

The SGA source cites Grothendieck-Dieudonne's *Elements de geometrie algebrique*
~1,650 times as plain text (e.g. ``EGA IV, 17.3.2``, ``EGA 0_III 9.2.2``,
``*EGA* III 2.1.12``). This script rewrites each *first* occurrence of a distinct
citation on a page into a Markdown link pointing at the corresponding section page
(and, where possible, the ``x.y`` subsection anchor) of the published EGA book at
https://jcreinhold.github.io/ega/ .

The citation -> file map is derived from EGA's source filenames (which encode the
chapter and section). Subsection anchors are read from EGA's *built* HTML
(``--ega-root/book/**.html``) so they are verified, never guessed. Run ``mdbook
build`` in the EGA repo first.

The transform is idempotent and self-maintaining. Each run does two things:
  1. *Refresh* -- every link already pointing at the EGA site is re-resolved from
     the citation in its label, so if the EGA book moves a file or retitles a
     heading, re-running this script repairs the URL/anchor automatically. (Note:
     re-nesting a chapter in EGA's SUMMARY.md does NOT change its URL -- mdBook
     URLs follow the source file path, not the table-of-contents hierarchy -- so
     only file renames/moves and heading edits need a refresh.)
  2. *Link* -- the first occurrence of each new plain-text citation per page.
The citation label is the source of truth; the URL is always derived. So link
maintenance is never by hand: re-run after rebuilding the EGA book.

Citations with no resolvable section number (bare ``EGA IV``) and references to the
unpublished volumes V and VI are left as plain text by design; a citation that has
disappeared from EGA is unwrapped back to plain text rather than left dead.

Usage:
    python3 scripts/link-ega-references.py --dry-run      # report only
    python3 scripts/link-ega-references.py                # rewrite in place
    python3 scripts/link-ega-references.py --ega-root ../ega
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

BASE_URL = "https://jcreinhold.github.io/ega/"

# SGA volume directories to process (SGA 1, 2, 3).
SGA_DIRS = ("i", "ii", "iii")

# ---------------------------------------------------------------------------
# Step 1 -- citation -> file map, from EGA source filenames.
# ---------------------------------------------------------------------------

# Chapter-class keys: "0", "I", "II", "III", "IV", "V". A citation resolves on
# (class, section); for chapter 0 the section number alone selects the volume
# (0_I = secs 1-7, 0_III = 8-13, 0_IV = 14-23), so the class need not encode it.

_FLAT_PREFIX_TO_CLASS = {"00": "0", "01": "I", "02": "II"}
_CH_DIGIT_TO_CLASS = {"0": "0", "3": "III", "4": "IV", "5": "V"}


def build_file_map(ega_root: Path) -> dict[tuple[str, int], str]:
    """Map (chapter-class, section) -> EGA *.html path, e.g. 'iv/30-...html'."""
    file_map: dict[tuple[str, int], str] = {}
    for vol_dir in ("i", "ii", "iii", "iv", "v"):
        d = ega_root / vol_dir
        if not d.is_dir():
            continue
        for md in sorted(d.glob("*.md")):
            name = md.name
            m = re.search(r"ch(\d)-(\d+)-", name)  # iii/iv/v: NN-chK-MM-...
            if m:
                cls = _CH_DIGIT_TO_CLASS.get(m.group(1))
                section = int(m.group(2))
            else:
                m = re.match(r"(\d\d)-(\d\d)-", name)  # i/ii: flat NN-MM-...
                if not m:
                    continue
                cls = _FLAT_PREFIX_TO_CLASS.get(m.group(1))
                section = int(m.group(2))
            if cls is None:
                continue
            html = f"{vol_dir}/{md.stem}.html"
            key = (cls, section)
            # First file wins; sorted glob keeps deterministic order.
            file_map.setdefault(key, html)
    return file_map


# ---------------------------------------------------------------------------
# Step 2 -- anchor index, from EGA built HTML (authoritative).
# ---------------------------------------------------------------------------

_HEADING_ID_RE = re.compile(r"<h[1-6][^>]*\sid=\"([^\"]+)\"")


def build_anchor_index(ega_root: Path, file_map: dict[tuple[str, int], str]) -> dict[str, dict[str, str]]:
    """For each target HTML file, map leading-digit-run -> anchor id.

    mdBook strips dots from heading numbers, so ``### 17.3.`` becomes
    ``id="173-..."``. Keying by the leading digit run lets ``17`` (sec 17 / 1.7),
    ``173`` (17.3), ``1910`` (19.10) resolve within a file unambiguously.
    """
    index: dict[str, dict[str, str]] = {}
    book = ega_root / "book"
    for html in set(file_map.values()):
        if html in index:
            continue
        path = book / html
        anchors: dict[str, str] = {}
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for anchor_id in _HEADING_ID_RE.findall(text):
                run = re.match(r"(\d+)", anchor_id)
                if run:
                    anchors.setdefault(run.group(1), anchor_id)
        else:
            print(f"  warning: built HTML missing: {path}", file=sys.stderr)
        index[html] = anchors
    return index


# ---------------------------------------------------------------------------
# Step 3 -- citation matching and rewriting.
# ---------------------------------------------------------------------------

# Volume token, longest/most-specific alternatives first. The chapter-0 form
# also covers the escaped/braced variants 0\_{IV} and 0_{III}.
_VOL = (
    r"0\\?_\{?(?:IV|III|II|I)\}?"
    r"|IV(?:_[1-4]|[₁₂₃₄]|[1-4])?"
    r"|III(?:_[12]|[₁₂])?"
    r"|II"
    r"|VI"
    r"|V"
    r"|I"
    r"|0"
)

CITATION_RE = re.compile(
    r"(?P<pre>\*)?EGA(?P<post>\*)?\s+"
    r"(?P<vol>" + _VOL + r")(?![A-Za-z])"
    r"(?:\s*,)?\s*(?:§{1,2}\s*)?"
    r"(?P<num>\d+(?:\.\d+)*(?:\s*[–—-]\s*\d+(?:\.\d+)*)?)?"
)

# Spans whose contents must never be rewritten.
_PROTECT_RES = [
    re.compile(r"(?ms)^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1"),  # fenced code
    re.compile(r"(?s)\$\$.*?\$\$"),  # block math
    re.compile(r"`+[^`]*`+"),  # inline code
    re.compile(r"\$(?:\\.|[^$\\\n])*\$"),  # inline math
    re.compile(r"\[[^\]]*\]\([^)]*\)"),  # existing md links
]

_ROMAN_RE = re.compile(r"IV|III|II|VI|V|I")

# Existing Markdown links, used to seed the per-page dedup on a re-run.
_EXISTING_EGA_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")


def classify(vol: str) -> str:
    """Reduce a matched volume token to its chapter class."""
    if vol[0] == "0":
        return "0"
    m = _ROMAN_RE.match(vol)
    return m.group(0) if m else vol


def parse_num(num: str) -> tuple[int, int | None]:
    """First range endpoint -> (section, subsection|None)."""
    first = re.split(r"\s*[–—-]\s*", num, maxsplit=1)[0]
    parts = first.split(".")
    section = int(parts[0])
    subsection = int(parts[1]) if len(parts) > 1 else None
    return section, subsection


def protected_intervals(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for pat in _PROTECT_RES:
        for m in pat.finditer(text):
            spans.append((m.start(), m.end()))
    spans.sort()
    merged: list[tuple[int, int]] = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return merged


class Linker:
    def __init__(self, file_map, anchor_index, stats: Counter):
        self.file_map = file_map
        self.anchor_index = anchor_index
        self.stats = stats

    def resolve_url(self, cls: str, num: str) -> str | None:
        if cls in ("V", "VI"):
            return None  # unpublished volumes: leave plain text (by decision)
        section, subsection = parse_num(num)
        html = self.file_map.get((cls, section))
        if html is None:
            return None
        anchors = self.anchor_index.get(html, {})
        anchor = None
        if subsection is not None:
            anchor = anchors.get(f"{section}{subsection}")
        if anchor is None:
            anchor = anchors.get(f"{section}")  # section-level fallback
        return BASE_URL + html + (f"#{anchor}" if anchor else "")

    def refresh_existing_links(self, text: str) -> str:
        """Re-resolve every link pointing at the EGA site, recomputing its URL from the citation in the link label.

        This is what makes the transform a one-command *refresh* after the EGA book moves a file or retitles a heading:
        the label is the source of truth, the URL is derived. A citation that no longer resolves is unwrapped back to
        plain text so no dead links survive.
        """

        def repl(m: re.Match) -> str:
            label, url = m.group(1), m.group(2)
            if BASE_URL not in url:
                return m.group(0)  # not an EGA link; leave alone
            cm = CITATION_RE.search(label)
            if not cm or not cm.group("num"):
                return m.group(0)
            new_url = self.resolve_url(classify(cm.group("vol")), cm.group("num"))
            if new_url is None:
                self.stats["unwrapped"] += 1
                return label  # citation gone from EGA: drop the dead link
            if new_url != url:
                self.stats["url_updated"] += 1
            return f"[{label}]({new_url})"

        return _EXISTING_EGA_LINK_RE.sub(repl, text)

    def rewrite_segment(self, segment: str, seen: set) -> str:
        def repl(m: re.Match) -> str:
            full = m.group(0)
            pre, post, vol, num = (
                m.group("pre"),
                m.group("post"),
                m.group("vol"),
                m.group("num"),
            )
            # Unbalanced italic marker around EGA -> too risky, leave as-is.
            if bool(pre) != bool(post):
                return full
            if not num:
                self.stats["bare_volume"] += 1
                return full
            cls = classify(vol)
            url = self.resolve_url(cls, num)
            if url is None:
                self.stats["unresolved"] += 1
                if len(self._unresolved_samples) < 25:
                    self._unresolved_samples.append(full.strip())
                return full
            key = (cls, re.sub(r"\s+", "", num))
            if key in seen:
                self.stats["repeat_skipped"] += 1
                return full
            seen.add(key)
            self.stats["linked"] += 1
            return f"[{full}]({url})"

        return CITATION_RE.sub(repl, segment)

    _unresolved_samples: list[str] = []

    def _seed_seen(self, text: str, seen: set) -> None:
        """Register citations linked to EGA site, so re-run does not promote a repeat into a new 'first' occurrence."""
        for label, url in _EXISTING_EGA_LINK_RE.findall(text):
            if BASE_URL not in url:
                continue
            m = CITATION_RE.search(label)
            if m and m.group("num"):
                seen.add((classify(m.group("vol")), re.sub(r"\s+", "", m.group("num"))))

    def rewrite_text(self, text: str) -> str:
        seen: set = set()
        self._seed_seen(text, seen)
        out: list[str] = []
        pos = 0
        for s, e in protected_intervals(text) + [(len(text), len(text))]:
            out.append(self.rewrite_segment(text[pos:s], seen))
            out.append(text[s:e])
            pos = e
        return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ega-root", default="../ega", help="path to the EGA repo")
    ap.add_argument("--sga-root", default=".", help="path to the SGA repo")
    ap.add_argument("--dry-run", action="store_true", help="report without writing")
    args = ap.parse_args()

    ega_root = Path(args.ega_root).resolve()
    sga_root = Path(args.sga_root).resolve()

    file_map = build_file_map(ega_root)
    anchor_index = build_anchor_index(ega_root, file_map)
    print(f"file_map: {len(file_map)} (class, section) entries")
    print(f"anchor index: {sum(len(a) for a in anchor_index.values())} anchors across {len(anchor_index)} files")

    stats: Counter = Counter()
    linker = Linker(file_map, anchor_index, stats)

    changed_files = 0
    per_file: list[tuple[str, int]] = []
    for vol in SGA_DIRS:
        for md in sorted((sga_root / vol).glob("*.md")):
            original = md.read_text(encoding="utf-8")
            before = stats["linked"]
            new = linker.rewrite_text(linker.refresh_existing_links(original))
            added = stats["linked"] - before
            if added:
                per_file.append((f"{vol}/{md.name}", added))
            if new != original:
                changed_files += 1
                if not args.dry_run:
                    md.write_text(new, encoding="utf-8")

    print("\n=== summary ===")
    print(f"links {'to add' if args.dry_run else 'added'}: {stats['linked']}")
    print(f"existing links re-pointed (stale URL refreshed): {stats['url_updated']}")
    print(f"existing links unwrapped (citation gone from EGA): {stats['unwrapped']}")
    print(f"repeats skipped (same citation, same page): {stats['repeat_skipped']}")
    print(f"bare-volume mentions left plain (no section #): {stats['bare_volume']}")
    print(f"unresolved (had a number but no EGA target): {stats['unresolved']}")
    print(f"files {'to change' if args.dry_run else 'changed'}: {changed_files}")

    print("\ntop files by links added:")
    for name, n in sorted(per_file, key=lambda x: -x[1])[:12]:
        print(f"  {n:4d}  {name}")

    if linker._unresolved_samples:
        print("\nunresolved samples (left as plain text):")
        for s in linker._unresolved_samples:
            print(f"  - {s}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
