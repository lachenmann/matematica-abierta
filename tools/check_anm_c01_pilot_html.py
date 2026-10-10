#!/usr/bin/env python3
"""Read-only C01 editorial pilot: rendered F01/F12, solution links, canonical SVG hashes.

No images are created, edited, converted or exported by this script.
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

STEM = "analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica"
CHAPTER = "libros/capitulos/" + STEM + ".md"
SOLUTIONS = "libros/capitulos/" + STEM + "-soluciones.md"
REGISTRY = "data/ma-fig-anm-c01-pilot-qa.json"
MAIN_ID, SOL_ID = "C01-F01", "C01-F12"


def norm(text: str) -> str:
    return " ".join(text.split()).casefold()


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.append(dict(attrs).get("href", ""))


def source_figure(source: str, fid: str):
    label = "fig-anm-c01-f" + fid[-2:].lower()
    pat = re.compile(
        r'!\[([^\]\n]+)\]'
        r'\(\.\./\.\./assets/books/anm/C01/' + fid + r'\.svg\)'
        r'\{#' + label + r' fig-alt="([^"\n]+)"\}'
    )
    matches = list(pat.finditer(source))
    return label, matches


def check(root: Path, site: Path) -> tuple[dict, list[str]]:
    errors = []
    meta = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    hashes = meta.get("all_existing_svg_sha256", {})
    expected = {"C01-F01", "C01-F02", "C01-F03", "C01-F05",
                "C01-F06", "C01-F07", "C01-F08", "C01-F09",
                "C01-F11", "C01-F12", "C01-F13", "C01-F14"}
    if set(hashes) != expected:
        errors.append("C01-PILOT: canonical register must contain exactly the 12 approved SVGs")
    for fid in expected:
        src = root / "assets/books/anm/C01" / (fid + ".svg")
        rendered = site / "assets/books/anm/C01" / (fid + ".svg")
        if not src.is_file() or not rendered.is_file():
            errors.append(f"C01-PILOT: {fid} source/rendered asset missing")
            continue
        checksum = hashes.get(fid)
        if (hashlib.sha256(src.read_bytes()).hexdigest() != checksum or
                hashlib.sha256(rendered.read_bytes()).hexdigest() != checksum):
            errors.append(f"C01-PILOT: {fid} SVG diverges from canonical SHA-256")
    pages = {
        MAIN_ID: (root / CHAPTER, site / Path(CHAPTER).with_suffix(".html")),
        SOL_ID: (root / SOLUTIONS, site / Path(SOLUTIONS).with_suffix(".html")),
    }
    for fid, (source_path, html_page) in pages.items():
        if not source_path.is_file() or not html_page.is_file():
            errors.append(f"C01-PILOT: {fid} source/rendered document unavailable")
            continue
        src_text = source_path.read_text(encoding="utf-8")
        label, matches = source_figure(src_text, fid)
        if len(matches) != 1:
            errors.append(f"C01-PILOT: {fid} must have exactly one semantic Markdown figure")
            continue
        caption, alt = matches[0].groups()
        if len(alt.strip()) < 50 or not caption.strip():
            errors.append(f"C01-PILOT: {fid} missing substantial caption/alt")
        parse = FigureIndex()
        parse.feed(html_page.read_text(encoding="utf-8"))
        figures = []
        for item in parse.figures:
            if label not in item["anchors"]:
                continue
            for img in item["images"]:
                try:
                    resolved = rendered_target(site, html_page, img.get("src", ""))
                except ValueError:
                    continue
                if resolved == (site / "assets/books/anm/C01" / (fid + ".svg")).resolve():
                    figures.append((item, img))
        if len(figures) != 1:
            errors.append(f"C01-PILOT: {fid} expected 1 HTML figure with image/anchor, found {len(figures)}")
            continue
        fig, img = figures[0]
        if norm(img.get("alt") or "") != norm(alt):
            errors.append(f"C01-PILOT: {fid} HTML img alt differs from source fig-alt")
        rendered_caption = norm("".join(fig["caption"]))
        if norm(caption) not in rendered_caption:
            errors.append(f"C01-PILOT: {fid} figcaption missing or changed")
        if fid.casefold() in rendered_caption:
            errors.append(f"C01-PILOT: {fid} duplicate visible editorial ID in caption")
    solutions_source = (root / SOLUTIONS).read_text(encoding="utf-8")
    source_refs = re.findall(r'\[C01-F12\]\(#fig-anm-c01-f12\)', solutions_source)
    if len(source_refs) != 3:
        errors.append(f"C01-PILOT: 3 contextual links expected in source, found {len(source_refs)}")
    if (site / Path(SOLUTIONS).with_suffix(".html")).is_file():
        collector = LinkCollector()
        collector.feed((site / Path(SOLUTIONS).with_suffix(".html")).read_text(encoding="utf-8"))
        refs = [x for x in collector.hrefs if urlsplit(x).fragment == "fig-anm-c01-f12"]
        if len(refs) != 3:
            errors.append(f"C01-PILOT: expected 3 rendered links into F12, found {len(refs)}")
        for ref in refs:
            if urlsplit(ref).path not in {"", STEM + "-soluciones.html"}:
                errors.append(f"C01-PILOT: F12 link points outside the solution: {ref}")
    return {"pilot_figures": 2, "svg_hashes": 12, "solution_links": len(source_refs)}, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    site = args.site_dir.resolve()
    if not site.is_dir():
        print(f"C01-PILOT FAIL: render directory missing: {site}", file=sys.stderr)
        return 1
    try:
        summary, errors = check(ROOT, site)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"C01-PILOT FAIL: {exc}", file=sys.stderr)
        return 1
    if errors:
        for issue in errors:
            print(issue, file=sys.stderr)
        return 1
    print(f"C01-PILOT PASS: {summary}; no images generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
