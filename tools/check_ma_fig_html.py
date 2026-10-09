#!/usr/bin/env python3
"""MA-FIG C9: verify manifest-backed figures in rendered Quarto HTML.

Read-only: this validator does not build, edit, export, or generate images.
Legacy images without a registered manifest are intentionally not recertified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.check_ma_fig_manifest import MANIFESTS, checked_path, load_scope, is_formal_treatise

QA_STATES = {"READY_FOR_PUBLICATION", "PUBLISHED"}
GENERIC_ALT = {"image", "imagen", "figura", "grafico", "gráfico", "diagram", "diagrama"}
VOID = {"img", "link", "meta", "input", "br", "hr", "source", "wbr", "area", "embed"}


def norm(text: str) -> str:
    return " ".join(text.split()).casefold()


class FigureIndex(HTMLParser):
    """Collect img, figcaption and anchors within the same figure element."""
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, dict, int | None]] = []
        self.figures: list[dict] = []

    def _inside_figure(self) -> int | None:
        for tag, attrs, uid in reversed(self.stack):
            if tag == "figure":
                return uid
        return None

    def handle_starttag(self, tag: str, attrlist: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrlist)
        fid = None
        if tag == "figure":
            fid = len(self.figures)
            anchors = [nodeattrs.get("id") for _, nodeattrs, _ in self.stack
                       if nodeattrs.get("id")]
            if attrs.get("id"):
                anchors.append(attrs["id"])
            self.figures.append({"anchors": anchors, "images": [], "caption": []})
        if tag == "img":
            parent = self._inside_figure()
            if parent is not None:
                self.figures[parent]["images"].append(attrs)
        if tag not in VOID:
            self.stack.append((tag, attrs, fid))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data: str) -> None:
        parent = self._inside_figure()
        if parent is not None and any(tag == "figcaption" for tag, _, _ in self.stack):
            self.figures[parent]["caption"].append(data)


def rendered_target(site: Path, page: Path, src: str) -> Path:
    """Resolve HTML image URLs, rejecting traversal and external resources."""
    if not isinstance(src, str) or not src or src.startswith("//"):
        raise ValueError("missing or protocol-relative image URL")
    url = urlsplit(src)
    if url.scheme or url.netloc or not url.path:
        raise ValueError("external/empty image URL")
    path = unquote(url.path)
    if chr(0) in path or "\\" in path:
        raise ValueError("unsafe encoded image path")
    target = ((site / path.lstrip("/")) if path.startswith("/")
              else page.parent / path).resolve()
    if not target.is_relative_to(site.resolve()):
        raise ValueError("image resolves outside rendered site")
    return target


def verify_html_figure(site: Path, root: Path, manifest: dict) -> list[str]:
    errors: list[str] = []
    figure_id = manifest.get("figure_id", "<missing>")
    consumer = manifest.get("consumer_source", "")
    label = f"C9-HTML {figure_id} ({consumer})"
    if not isinstance(consumer, str) or not consumer.endswith((".md", ".qmd")):
        return [f"{label}: invalid consumer_source"]
    if is_formal_treatise(consumer, load_scope(root)):
        return [f"{label}: figure on formal treatise is forbidden"]
    source_page = checked_path(root, consumer, "consumer_source")
    if not source_page.is_file():
        return [f"{label}: source page missing"]
    html_page = (site / Path(consumer).with_suffix(".html")).resolve()
    if not html_page.is_relative_to(site.resolve()) or not html_page.is_file():
        return [f"{label}: rendered consumer HTML missing: {html_page}"]
    outputs = manifest.get("outputs")
    if not isinstance(outputs, dict):
        return [f"{label}: outputs must be an object"]
    output = outputs.get("web_svg") or outputs.get("preview_png")
    if not isinstance(output, str) or not output:
        return [f"{label}: web_svg or preview_png required for HTML"]
    output_path = checked_path(root, output, "output")
    if not output_path.is_file():
        return [f"{label}: approved source asset missing: {output}"]
    payload = output_path.read_bytes()
    expected_digest = manifest.get("output_sha256", {}).get(
        "web_svg" if outputs.get("web_svg") else "preview_png"
    )
    if hashlib.sha256(payload).hexdigest() != expected_digest:
        errors.append(f"{label}: approved asset checksum mismatch")
    parser = FigureIndex()
    parser.feed(html_page.read_text(encoding="utf-8"))
    parser.close()
    matches: list[dict] = []
    for figure in parser.figures:
        for img in figure["images"]:
            try:
                target = rendered_target(site, html_page, img.get("src", ""))
            except ValueError:
                continue
            if target == (site / output).resolve():
                matches.append({"figure": figure, "image": img, "target": target})
    if len(matches) != 1:
        return errors + [f"{label}: expected one rendered <figure>/<img> for {output}; found {len(matches)}"]
    found = matches[0]
    if not found["target"].is_file():
        errors.append(f"{label}: image is absent in rendered site")
    elif found["target"].read_bytes() != payload:
        errors.append(f"{label}: rendered asset differs from approved bytes")
    alt = found["image"].get("alt") or ""
    expected_alt = manifest.get("alt")
    if (not alt.strip() or norm(alt) in GENERIC_ALT or
            not isinstance(expected_alt, str) or norm(alt) != norm(expected_alt)):
        errors.append(f"{label}: img alt missing, generic, or inconsistent with manifest")
    caption = norm("".join(found["figure"]["caption"]))
    expected_caption = manifest.get("caption")
    if (not isinstance(expected_caption, str) or
            not expected_caption.strip() or norm(expected_caption) not in caption):
        errors.append(f"{label}: figure caption missing/inconsistent")
    figure_label = manifest.get("figure_label")
    if (not isinstance(figure_label, str) or
            not re.fullmatch(r"fig-[a-zA-Z0-9_-]+", figure_label)):
        errors.append(f"{label}: valid figure_label starting with fig- required")
    elif figure_label not in found["figure"]["anchors"]:
        errors.append(f"{label}: figure_label anchor not present in HTML")
    return errors


def check(root: Path, site: Path) -> tuple[int, list[str]]:
    manifests = root / MANIFESTS
    errors = []
    verified = 0
    for item in sorted(manifests.glob("*.json")) if manifests.exists() else []:
        try:
            data = json.loads(item.read_text(encoding="utf-8"))
            if isinstance(data, dict) and data.get("status") in QA_STATES:
                verified += 1
                errors.extend(verify_html_figure(site, root, data))
        except (ValueError, OSError, json.JSONDecodeError) as exc:
            errors.append(f"C9-HTML {item.name}: {exc}")
    return verified, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    site = args.site_dir.resolve()
    if not site.is_dir():
        print(f"C9-HTML: FAIL — rendered site not found: {site}", file=sys.stderr)
        return 1
    verified, errors = check(ROOT, site)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"C9-HTML: FAIL — {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(f"C9-HTML: PASS — {verified} registered figure(s) checked (no images generated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
