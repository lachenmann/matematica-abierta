#!/usr/bin/env python3
"""Check inheritance and rendered CSS for all Quarto book pages."""
from argparse import ArgumentParser
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "assets/books/reader.css"

class BookPage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_quarto = False
        self.styles = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "main" and attrs.get("id") == "quarto-document-content":
            self.is_quarto = True
        if tag == "link" and "stylesheet" in attrs.get("rel", "").split():
            self.styles.append(attrs.get("href", ""))

def check(site_dir):
    metadata = (ROOT / "libros/_metadata.yml").read_text()
    if not re.search(r"(?m)^      - \.\./assets/books/reader\.css$", metadata):
        raise ValueError("book directory must inherit the canonical CSS")
    if not (ROOT / CANONICAL).is_file():
        raise ValueError("canonical CSS is missing")
    # Avoid reintroducing dependencies between book-specific stylesheets.
    for name in ["assets/books/anm/reader.css",
                 "libros/capitulos/calculo-para-matematicos.css"]:
        if "@import" in (ROOT / name).read_text():
            raise ValueError(f"book CSS must contain exceptions only: {name}")
    if site_dir is None:
        print("Book layout inheritance: PASS")
        return
    site = site_dir.resolve()
    canonical = (site / CANONICAL).resolve()
    if not canonical.is_file():
        raise ValueError("canonical CSS was not copied to the site")
    checked = 0
    for page in sorted((site / "libros").rglob("*.html")):
        parsed = BookPage()
        parsed.feed(page.read_text(encoding="utf-8"))
        if not parsed.is_quarto:
            continue  # PDFs, labs and standalone documents have their own format.
        targets = []
        for href in parsed.styles:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            target = (site / path.lstrip("/") if path.startswith("/")
                      else page.parent / path).resolve()
            if not target.is_file():
                raise ValueError(f"missing stylesheet: {page.relative_to(site)}: {href}")
            targets.append(target)
        if targets.count(canonical) != 1:
            raise ValueError(f"canonical CSS must occur once: {page.relative_to(site)}")
        checked += 1
    if not checked:
        raise ValueError("no rendered Quarto book pages found")
    print(f"Canonical book layout: PASS — {checked} rendered pages")

if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path)
    check(parser.parse_args().site_dir)
