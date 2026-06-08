#!/usr/bin/env python3
"""Generate SUMMARY.md for mdBook from the SGA volume directories.

Walks ``i/``, ``ii/``, ``iii/`` in order and, for each exposé file, uses its
first-level (``# ``) heading as the human title — these headings are the
authoritative English titles (e.g. "Exposé I. Étale Morphisms"). Front- and
back-matter pages (and the two chapters whose heading carries LaTeX that would
render raw in the sidebar) get a short curated label from ``TITLE_OVERRIDES``.
Writes ``SUMMARY.md`` at the repo root. With ``--check`` the script exits
non-zero if the committed file is stale; this is the drift gate run in CI.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARY = ROOT / "SUMMARY.md"

VOLUMES: list[tuple[str, str]] = [
    ("i", "SGA 1 — Étale Coverings and the Fundamental Group"),
    ("ii", "SGA 2 — Local Cohomology and Lefschetz Theorems"),
    ("iii", "SGA 3 — Group Schemes"),
]

# Curated short labels, keyed by file stem. Front/back matter, plus the two
# chapters whose `# ` heading contains math ($...$) that would otherwise show
# raw in the sidebar. Everything else takes its title from the `# ` heading.
TITLE_OVERRIDES: dict[str, str] = {
    "00-title-preface": "Title and preface",
    "00-foreword": "Foreword",
    "00-introduction": "Introduction",
    "00-i-foreword-introduction": "Foreword and introduction (I)",
    "00-i-errata": "Errata (I)",
    "00-ii-preface": "Preface (II)",
    "00-iii-errata": "Errata (III)",
    "glossary": "Translation glossary",
    "zz-index-notations": "Index of notations",
    "zz-index-terminological": "Index of terminology",
    "zz-i-index": "Index (volume I)",
    "zz-iii-index": "Index (volume III)",
    "06-ext-functors": "Exposé VI. The functors Ext and ℰxt",
    "07A-infinitesimal-study-differential-operators": (
        "Exposé VII_A. Infinitesimal study: differential operators and restricted p-Lie algebras"
    ),
}

PREFIX_RE = re.compile(r"^\d+[A-Za-z]?-")


def first_heading(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def derive_title(path: Path) -> str:
    stem = path.stem
    if stem in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[stem]
    heading = first_heading(path)
    if heading:
        return heading
    # Fallback for an untitled file: prettify the (already English) stem.
    body = stem
    while PREFIX_RE.match(body):
        body = PREFIX_RE.sub("", body, count=1)
    return body.replace("-", " ").capitalize()


def sort_key(path: Path) -> tuple[int, str]:
    stem = path.stem
    if stem.startswith("00-") or "preface" in stem or stem == "00-introduction":
        bucket = 0
    elif stem.startswith("zz-") or stem == "glossary":
        bucket = 2
    else:
        bucket = 1
    return bucket, stem


def volume_entries(vol: str) -> list[tuple[str, Path]]:
    vol_dir = ROOT / vol
    skip = {"README.md"}
    paths = sorted(
        (p for p in vol_dir.glob("*.md") if p.name not in skip),
        key=sort_key,
    )
    return [(derive_title(p), p.relative_to(ROOT)) for p in paths]


def render() -> str:
    lines: list[str] = ["# Summary", "", "[Introduction](index.md)", ""]
    for vol, label in VOLUMES:
        lines.append(f"# {label}")
        lines.append("")
        for title, rel in volume_entries(vol):
            lines.append(f"- [{title}]({rel.as_posix()})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if SUMMARY.md does not match the generated output.",
    )
    args = parser.parse_args()

    new = render()
    if args.check:
        current = SUMMARY.read_text() if SUMMARY.exists() else ""
        if current != new:
            print(
                "SUMMARY.md is out of date. Run scripts/generate-summary.py.",
                file=sys.stderr,
            )
            return 1
        return 0
    SUMMARY.write_text(new)
    return 0


if __name__ == "__main__":
    sys.exit(main())
