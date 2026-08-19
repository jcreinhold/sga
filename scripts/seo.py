#!/usr/bin/env python3
"""Post-build SEO pass for the SGA mdBook site.

Runs after `mdbook build` and, purely by editing the generated HTML in book/:

- rewrites every <title> to a descriptive, page-specific value
  (homepage, volume landing pages, exposés, front/back matter);
- adds a self-referential <link rel="canonical"> to every indexable page
  (canonical root: https://jcreinhold.github.io/sga/);
- replaces the global mdBook meta description with a per-page one;
- writes book/sitemap.xml (all useful canonical HTML URLs) and book/robots.txt.

The page inventory and exposé metadata are derived from SUMMARY.md, so the
script stays in sync with the table of contents automatically. It fails the
build (non-zero exit) if a chapter file in SUMMARY.md has no generated HTML
page, which also guards against broken/orphaned exposé pages.
"""

from __future__ import annotations

import html
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARY = ROOT / "SUMMARY.md"
BUILD = ROOT / "book"
BASE = "https://jcreinhold.github.io/sga/"

SITE_TAGLINE = "English Translation"
SITE_DESC = (
    "A complete English translation of Grothendieck's Séminaire de Géométrie "
    "Algébrique du Bois-Marie (SGA): SGA 1 on étale coverings and the "
    "fundamental group, SGA 2 on local cohomology and Lefschetz theorems, "
    "SGA 3 on group schemes, and SGA 4 on topoi — browser-readable, fully "
    "linked, preserving the original exposé numbering."
)

# Volume landing page -> (volume label, volume title, volume description).
VOLUME_LANDING = {
    "i/00-title-preface.html": (
        "SGA 1",
        "Étale Coverings and the Fundamental Group",
        "English translation of SGA 1 (Revêtements étales et groupe "
        "fondamental), Grothendieck's 1960–61 seminar on étale coverings, "
        "descent, and the fundamental group of schemes, with exposés by "
        "M. Raynaud.",
    ),
    "ii/00-title-preface.html": (
        "SGA 2",
        "Local Cohomology and Lefschetz Theorems",
        "English translation of SGA 2 (Cohomologie locale des faisceaux "
        "cohérents et théorèmes de Lefschetz locaux et globaux), "
        "Grothendieck's 1961–62 seminar on local cohomology, depth, duality, "
        "and Lefschetz-type theorems.",
    ),
    "iii/00-ii-preface.html": (
        "SGA 3",
        "Group Schemes",
        "English translation of SGA 3 (Schémas en groupes), the 1962–64 "
        "Demazure–Grothendieck seminar on group schemes, groups of "
        "multiplicative type, and reductive groups.",
    ),
    "iv/00-front-matter.html": (
        "SGA 4",
        "Topoi and Sites",
        "English translation of SGA 4 (Théorie des topos et cohomologie "
        "étale des schémas), the Artin–Grothendieck–Verdier seminar on "
        "presheaves, sites, and topoi.",
    ),
}

# SUMMARY.md section header -> volume label used in titles.
VOLUME_HEADERS = {
    "SGA 1": "SGA 1",
    "SGA 2": "SGA 2",
    "SGA 3": "SGA 3",
    "SGA IV": "SGA 4",
}

HOME_TITLE = "SGA — Séminaire de Géométrie Algébrique du Bois-Marie | English Translation"

# Volume label -> (landing-page basename, volume title) for breadcrumbs.
VOLUME_INFO = {
    label: (landing.rsplit("/", 1)[1], vol_title)
    for landing, (label, vol_title, _desc) in VOLUME_LANDING.items()
}

# HTML files that must never be indexed or listed in the sitemap.
# 404.html is the error page; toc.html is mdBook's no-JS sidebar iframe
# (already noindex) and has no standalone content.
EXCLUDE = {"404.html", "toc.html"}


def roman_volume(header: str) -> str | None:
    for key, label in VOLUME_HEADERS.items():
        if header.startswith(f"# {key} ") or header.strip() == f"# {key}":
            return label
    return None


def parse_summary() -> list[tuple[str, str, str | None]]:
    """Return [(md_path, chapter_title, volume_label)] from SUMMARY.md."""
    entries: list[tuple[str, str, str | None]] = []
    volume: str | None = None
    for line in SUMMARY.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            volume = roman_volume(line) or volume
            continue
        m = re.match(r"(?:- )?\[(.+?)\]\((.+?\.md)\)", line.strip())
        if m:
            entries.append((m.group(2), m.group(1), volume))
    return entries


def expose_title(volume: str, chapter: str) -> str:
    """'Exposé V. The Fundamental Group: Generalities' ->
    'SGA 1, Exposé V — The Fundamental Group: Generalities | English Translation'"""
    m = re.match(r"Exposé\s+(.+?)\.\s*(.*)", chapter)
    if m:
        num, subject = m.group(1), m.group(2).strip()
        title = f"{volume}, Exposé {num}"
        if subject:
            title += f" — {subject}"
    else:
        title = f"{chapter} — {volume}"
    return f"{title} | {SITE_TAGLINE}"


def expose_desc(volume: str, chapter: str) -> str:
    m = re.match(r"Exposé\s+(.+?)\.\s*(.*)", chapter)
    if m and m.group(2).strip():
        subject = m.group(2).strip()
        return (
            f"English translation of {volume}, Exposé {m.group(1)} — "
            f"{subject} — from Grothendieck's Séminaire de Géométrie "
            f"Algébrique du Bois-Marie."
        )
    return (
        f"English translation of the {chapter.lower()} of {volume}, from "
        f"Grothendieck's Séminaire de Géométrie Algébrique du Bois-Marie."
    )


def canonical_url(rel: str) -> str:
    return BASE if rel == "index.html" else BASE + rel


def patch_html(path: Path, rel: str, title: str, desc: str) -> None:
    text = path.read_text(encoding="utf-8")
    esc_title = html.escape(title, quote=True)
    esc_desc = html.escape(desc, quote=True)
    canon = canonical_url(rel)
    breadcrumb = make_breadcrumb(rel)

    text, n_title = re.subn(r"<title>.*?</title>", f"<title>{esc_title}</title>", text, count=1)
    if re.search(r'<meta\s+name="description"', text):
        text = re.sub(
            r'<meta\s+name="description"\s+content="[^"]*"\s*/?>',
            f'<meta name="description" content="{esc_desc}">',
            text,
            count=1,
        )
    else:
        text = text.replace("</title>", f'</title>\n        <meta name="description" content="{esc_desc}">', 1)
    # Insert the canonical link right after the charset meta, first in head.
    if 'rel="canonical"' not in text:
        text = text.replace(
            '<meta charset="UTF-8">',
            f'<meta charset="UTF-8">\n        <link rel="canonical" href="{canon}">',
            1,
        )
    if n_title != 1 or 'rel="canonical"' not in text:
        raise SystemExit(f"error: failed to patch <head> of {rel}")
    if breadcrumb and 'sga-breadcrumb' not in text:
        if "<main>" not in text:
            raise SystemExit(f"error: no <main> found in {rel}")
        text = text.replace("<main>", "<main>\n" + breadcrumb, 1)
    path.write_text(text, encoding="utf-8")


def make_breadcrumb(rel: str) -> str:
    """Static breadcrumb linking each chapter to the homepage and its parent
    volume landing page (the sidebar ToC is JS-injected, so crawlers without
    rendering otherwise only see prev/next links)."""
    if rel == "index.html" or "/" not in rel:
        return ""
    volume_dir = rel.split("/", 1)[0]
    for landing, (label, vol_title, _desc) in VOLUME_LANDING.items():
        if landing.startswith(volume_dir + "/"):
            depth = rel.count("/")
            home = "../" * depth + "index.html"
            home_a = f'<a href="{home}">SGA — English Translation</a>'
            if rel == landing:
                inner = home_a
            else:
                # All chapter pages live directly inside the volume directory.
                inner = f'{home_a} › <a href="{landing.split("/", 1)[1]}">{html.escape(label)} — {html.escape(vol_title)}</a>'
            return f'<p class="sga-breadcrumb">{inner}</p>'
    return ""


def main() -> int:
    entries = parse_summary()
    html_pages = {
        str(p.relative_to(BUILD)) for p in BUILD.rglob("*.html") if p.name not in EXCLUDE
    }

    patched: list[str] = []
    missing: list[str] = []
    for md_path, chapter, volume in entries:
        rel = md_path[:-3] + ".html"  # .md -> .html
        page = BUILD / rel
        if rel not in html_pages:
            missing.append(rel)
            continue
        if rel == "index.html":
            title, desc = HOME_TITLE, SITE_DESC
        elif rel in VOLUME_LANDING:
            vol, vol_title, desc = VOLUME_LANDING[rel]
            title = f"{vol} — {vol_title} | {SITE_TAGLINE}"
        elif volume:
            title, desc = expose_title(volume, chapter), expose_desc(volume, chapter)
        else:
            title = f"{chapter} | Séminaire de Géométrie Algébrique — English Translation"
            desc = SITE_DESC
        patch_html(page, rel, title, desc)
        patched.append(rel)

    if missing:
        for rel in missing:
            print(f"error: SUMMARY.md chapter has no generated page: {rel}", file=sys.stderr)
        return 1

    # Every other generated HTML page (none expected beyond SUMMARY entries)
    # still gets a canonical + sane title fallback so nothing ships unpatched.
    for rel in sorted(html_pages - set(patched)):
        page = BUILD / rel
        m = re.search(r"<title>(.*?)</title>", page.read_text(encoding="utf-8"))
        fallback = m.group(1) if m else rel
        patch_html(page, rel, fallback, SITE_DESC)
        patched.append(rel)

    today = date.today().isoformat()
    urls = sorted(canonical_url(rel) for rel in patched)
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
        + "</urlset>\n"
    )
    (BUILD / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (BUILD / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: " + BASE + "sitemap.xml\n",
        encoding="utf-8",
    )
    print(f"seo: patched {len(patched)} pages; wrote sitemap.xml ({len(urls)} URLs) and robots.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
