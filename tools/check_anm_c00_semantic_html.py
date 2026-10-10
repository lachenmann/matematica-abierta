#!/usr/bin/env python3
"""ANM C00: read-only post-render QA for the 12 canonical legacy figures.

This is NOT permission to generate, edit, or rasterize SVG assets.
The register under data/ma-fig-anm-c00-legacy-qa.json is not a C8/C9
publication manifest; C00 already completed its original V1-V4 QA.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.check_ma_fig_html import FigureIndex, rendered_target

STEM = "analisis-para-matematicos-capitulo-0-construir-los-numeros-reales"
CHAPTER = "libros/capitulos/" + STEM + ".md"
SOLUTIONS = "libros/capitulos/" + STEM + "-soluciones.md"
REGISTRY = "data/ma-fig-anm-c00-legacy-qa.json"
FIG_RE = re.compile(
    r'^!\[([^\]\n]+)\]\(\.\./\.\./assets/books/anm/(C00-F\d{2})\.svg\)'
    r'\{#(fig-anm-c00-f\d{2}) fig-alt="([^"\n]+)"\}$', re.M
)
SOURCE_LINK_RE = re.compile(
    r'\[C00-F(\d{2})(?: \(\*\*[^)\n]+\*\*\))?\]'
    r'\(' + re.escape(STEM) + r'\.md#fig-anm-c00-f\d{2}\)'
)


class SolutionLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            if "#fig-anm-c00-f" in href:
                self.hrefs.append(href)


def normalize(text: str) -> str:
    return " ".join(text.split()).casefold()


def audit(root: Path, site: Path) -> tuple[dict, list[str]]:
    errors = []
    source = (root / CHAPTER).read_text(encoding="utf-8")
    solutions = (root / SOLUTIONS).read_text(encoding="utf-8")
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    ids = registry["figure_order"]
    canon = registry["current_svg_sha256"]
    candidates = [
        dict(caption=m[1], id=m[2], anchor=m[3], alt=m[4])
        for m in FIG_RE.finditer(source)
    ]
    seen = [f["id"] for f in candidates]
    if len(seen) != 12 or seen != ids or len(set(seen)) != 12:
        errors.append("C00-QA: sources must contain 12 ordered, uniquely anchored figures")
    if len(canon) != 12 or any(id not in canon for id in ids):
        errors.append("C00-QA: canonical SHA-256 register is incomplete")
    html_page = (site / Path(CHAPTER).with_suffix(".html")).resolve()
    sol_page = (site / Path(SOLUTIONS).with_suffix(".html")).resolve()
    if not html_page.is_file() or not sol_page.is_file():
        return dict(figures=len(candidates), links=0), errors + [
            "C00-QA: rendered chapter/solutions HTML unavailable"
        ]
    figs = FigureIndex()
    figs.feed(html_page.read_text(encoding="utf-8"))
    links = SolutionLinks()
    links.feed(sol_page.read_text(encoding="utf-8"))
    count_links = 0

    for fig in candidates:
        fid = fig["id"]
        anchor = fig["anchor"]
        if anchor != "fig-anm-c00-f" + fid[-2:].lower():
            errors.append(f"{fid}: wrong stable anchor {anchor}")
        source_asset = (root / "assets/books/anm" / (fid + ".svg"))
        built_asset = (site / "assets/books/anm" / (fid + ".svg"))
        if not source_asset.is_file() or not built_asset.is_file():
            errors.append(f"{fid}: canonical/rendered SVG missing")
        else:
            expected = canon.get(fid, "")
            source_hash = hashlib.sha256(source_asset.read_bytes()).hexdigest()
            built_hash = hashlib.sha256(built_asset.read_bytes()).hexdigest()
            if source_hash != expected or built_hash != expected:
                errors.append(f"{fid}: source/rendered SHA-256 differs from Obsidian canon")
        matches = []
        for rendered in figs.figures:
            if anchor not in rendered["anchors"]:
                continue
            for img in rendered["images"]:
                try:
                    target = rendered_target(site, html_page, img.get("src", ""))
                except ValueError:
                    continue
                if target == built_asset.resolve():
                    matches.append((rendered, img))
        if len(matches) != 1:
            errors.append(f"{fid}: expected exactly one <figure> with matching image and anchor, got {len(matches)}")
            continue
        rendered, img = matches[0]
        if normalize(img.get("alt") or "") != normalize(fig["alt"]):
            errors.append(f"{fid}: img alt does not match canonical descriptive source")
        visible = normalize("".join(rendered["caption"]))
        expected_caption = normalize(fig["caption"])
        if not visible or expected_caption[:22] not in visible:
            errors.append(f"{fid}: figcaption missing/inconsistent with chapter source")
        if fid.casefold() in visible:
            errors.append(f"{fid}: canonical ID duplicated in visible Quarto caption")
        if not re.search(r"\bfigura\s+\d+", visible):
            errors.append(f"{fid}: expected Quarto's single visible numeric caption")

    direct = list(SOURCE_LINK_RE.finditer(solutions))
    # Every archived reference to a figure remains linked; 35 references
    # comprise 30 single-figure links, 1 deferred-note link and 4 pair links.
    if len(direct) != 35:
        errors.append(f"C00-QA: expected 35 source figure links, found {len(direct)}")
    for href in links.hrefs:
        parsed = urlsplit(href)
        if not parsed.fragment.startswith("fig-anm-c00-f"):
            errors.append("C00-QA: invalid figure link fragment")
            continue
        if not parsed.path.endswith(STEM + ".html"):
            errors.append(f"C00-QA: figure link resolves to unexpected page: {href}")
        if parsed.fragment not in {"fig-anm-c00-f" + id[-2:].lower() for id in ids}:
            errors.append(f"C00-QA: figure link points to unknown anchor: {href}")
        count_links += 1
    if count_links != 35:
        errors.append(f"C00-QA: expected 35 rendered deep links, found {count_links}")
    return dict(figures=len(candidates), rendered_links=count_links,
                canonical_svg_hashes_checked=12), errors


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--site-dir", type=Path, default=ROOT / "_site")
    args = p.parse_args()
    site = args.site_dir.resolve()
    if not site.is_dir():
        print("ANM C00 semantic QA FAIL: rendered site does not exist", file=sys.stderr)
        return 1
    try:
        counts, errors = audit(ROOT, site)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"ANM C00 semantic QA FAIL: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"ANM C00 semantic QA PASS: {counts} (no images generated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
