#!/usr/bin/env python3
"""ANM C01: read-only audit of 12 legacy SVGs and their semantic Quarto HTML.

The Obsidian-approved figures are never created, edited, rendered or exported.
This file checks existing source and already-rendered _site outputs only.
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
MAIN_IDS = ("C01-F01", "C01-F02", "C01-F03", "C01-F05",
            "C01-F06", "C01-F07", "C01-F08", "C01-F09")
SOLUTION_IDS = ("C01-F11", "C01-F12", "C01-F13", "C01-F14")
SRC_FIG = re.compile(
    r'^!\[(.+)\]\(\.\./\.\./assets/books/anm/C01/(C01-F\d\d)\.svg\)'
    r'\{#(fig-anm-c01-f\d\d) fig-alt="([^"\n]+)"\}$', re.M
)
SOURCE_LINK = re.compile(r'\[C01-F(\d\d)\]\(#fig-anm-c01-f(\d\d)\)')


def norm(value: str) -> str:
    return " ".join(value.split()).casefold()


def substantive_caption_fragments(markdown: str) -> list[str]:
    """Keep meaningful prose spans; inline LaTeX may be transformed by Quarto."""
    parts = re.split(r"\$[^$]*\$", markdown)
    return [norm(part) for part in parts if len(norm(part)) >= 22]


class AnchorLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.append(dict(attrs).get("href", ""))


def audit(root: Path, site: Path) -> tuple[dict, list[str]]:
    errors = []
    data = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    expected = MAIN_IDS + SOLUTION_IDS
    hashes = data.get("all_existing_svg_sha256", {})
    if set(hashes) != set(expected):
        errors.append("C01-SEM: canonical SVG registry must have exactly 12 identifiers")

    for fid in expected:
        original = root / "assets/books/anm/C01" / (fid + ".svg")
        rendered = site / "assets/books/anm/C01" / (fid + ".svg")
        if not original.is_file() or not rendered.is_file():
            errors.append(f"C01-SEM: {fid} source/rendered SVG missing")
            continue
        hash_expected = hashes.get(fid, "")
        if (hashlib.sha256(original.read_bytes()).hexdigest() != hash_expected
                or hashlib.sha256(rendered.read_bytes()).hexdigest() != hash_expected):
            errors.append(f"C01-SEM: {fid} bytes differ from canonical SHA-256")

    links_total = 0
    figures_total = 0
    for path, wanted, wanted_links in (
        (CHAPTER, MAIN_IDS, 9),
        (SOLUTIONS, SOLUTION_IDS, 6),
    ):
        src = (root / path).read_text(encoding="utf-8")
        html_path = site / Path(path).with_suffix(".html")
        if not html_path.is_file():
            errors.append(f"C01-SEM: rendered page missing: {path}")
            continue
        html = html_path.read_text(encoding="utf-8")
        parser = FigureIndex()
        parser.feed(html)
        parser.close()
        links = AnchorLinks()
        links.feed(html)
        source_figs = list(SRC_FIG.finditer(src))
        found = [m.group(2) for m in source_figs]
        if found != list(wanted):
            errors.append(f"C01-SEM: {path} wrong figure count/order: {found}")

        if re.search(r"(?m)^\*Figura C01-F\d\d\.", src):
            errors.append(f"C01-SEM: {path} contains an old detached caption")
        for m in source_figs:
            caption, fid, anchor, alt = m.groups()
            figures_total += 1
            if anchor != "fig-anm-c01-f" + fid[-2:]:
                errors.append(f"C01-SEM: {fid} incorrect stable anchor")
            if not caption.strip() or len(alt.strip()) < 40:
                errors.append(f"C01-SEM: {fid} insufficient caption or alt")
            matches = []
            for fg in parser.figures:
                if anchor not in fg["anchors"]:
                    continue
                for img in fg["images"]:
                    try:
                        target = rendered_target(site, html_path, img.get("src", ""))
                    except ValueError:
                        continue
                    if target == (site / "assets/books/anm/C01" / (fid + ".svg")).resolve():
                        matches.append((fg, img))
            if len(matches) != 1:
                errors.append(f"C01-SEM: {fid} expected one figure/image/anchor; got {len(matches)}")
                continue
            figure, img = matches[0]
            if norm(img.get("alt") or "") != norm(alt):
                errors.append(f"C01-SEM: {fid} HTML alt mismatches fig-alt")
            actual_caption = norm("".join(figure["caption"]))
            fragments = substantive_caption_fragments(caption)
            if not fragments or not any(fragment in actual_caption for fragment in fragments):
                errors.append(f"C01-SEM: {fid} figcaption lost mathematical prose")
            if fid.casefold() in actual_caption:
                errors.append(f"C01-SEM: {fid} duplicated visible internal identifier")
            if not re.search(r"\bfigura\s+\d+\b", actual_caption):
                errors.append(f"C01-SEM: {fid} lacks a single Quarto figure number")

        src_links = SOURCE_LINK.findall(src)
        if len(src_links) != wanted_links:
            errors.append(f"C01-SEM: {path} expected {wanted_links} Markdown deep links, got {len(src_links)}")
        for key, anchor_key in src_links:
            if key != anchor_key or "C01-F" + key not in wanted:
                errors.append(f"C01-SEM: {path} invalid Markdown figure reference {key}/{anchor_key}")
        expected_fragments = ["fig-anm-c01-f" + key for key, _ in src_links]
        rendered_targets = []
        for href in links.hrefs:
            target = urlsplit(href)
            if target.fragment.startswith("fig-anm-c01-f"):
                rendered_targets.append((target.fragment, target.path))
        if len(rendered_targets) != wanted_links:
            errors.append(f"C01-SEM: {path} expected {wanted_links} HTML links, got {len(rendered_targets)}")
        for frag, target_path in rendered_targets:
            if frag not in expected_fragments or target_path not in {"", Path(path).with_suffix(".html").name}:
                errors.append(f"C01-SEM: {path} bad figure link target {frag} / {target_path}")
            elif frag in expected_fragments:
                expected_fragments.remove(frag)
        if expected_fragments:
            errors.append(f"C01-SEM: {path} missing rendered anchor links {expected_fragments}")
        links_total += len(rendered_targets)

    return {"figures": figures_total, "svg_sha256": len(expected),
            "navigable_references": links_total}, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    site = args.site_dir.resolve()
    if not site.is_dir():
        print("C01-SEM FAIL: rendered site missing", file=sys.stderr)
        return 1
    try:
        outcome, errors = audit(ROOT, site)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"C01-SEM FAIL: {exc}", file=sys.stderr)
        return 1
    if errors:
        for issue in errors:
            print(issue, file=sys.stderr)
        return 1
    print(f"C01-SEM PASS: {outcome} (no images created or modified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
