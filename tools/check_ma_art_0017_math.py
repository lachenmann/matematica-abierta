#!/usr/bin/env python3
"""MA-ART-0017: prevent malformed display-math delimiters and unrendered evaluations.

Check the Quarto source before rendering; check the generated HTML afterward.
Standard-library only, with no modification of files or figures.
"""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("blog/como-leer-una-integral.qmd")
HTML = Path("blog/como-leer-una-integral.html")
FIRST_INTEGRAL = r"\int_{-1}^{1}x\,dx"
FIRST_EVALUATION = r"\left.\frac{x^2}{2}\right|_{-1}^{1}"
PARTS_EVALUATION = r"\left.-\frac{\cos x}{x}\right|_1^R"


def validate_source(source: str) -> list[str]:
    lines = source.splitlines()
    errors: list[str] = []
    malformed = [i for i, line in enumerate(lines, 1) if line.strip() == "$"]
    if malformed:
        errors.append(f"single-$ display delimiter at line(s) {malformed}")
    fences = sum(line.strip() == "$$" for line in lines)
    if fences < 2 or fences % 2:
        errors.append(f"unbalanced standalone display-math delimiters: {fences}")
    if not (FIRST_INTEGRAL in source and FIRST_EVALUATION in source):
        errors.append("first integral/evaluation not present in source")
    if PARTS_EVALUATION not in source:
        errors.append("integration-by-parts evaluation missing")
    return errors


class DisplayMathParser(HTMLParser):
    """Collect TeX payloads in spans emitted by Quarto/Pandoc for MathJax."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_math = False
        self.contents = []
        self.current = []

    def handle_starttag(self, tag, attrs):
        if tag != "span" or self.in_math:
            return
        classes = dict(attrs).get("class", "").split()
        if "math" in classes and "display" in classes:
            self.in_math = True
            self.current = []

    def handle_data(self, data):
        if self.in_math:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == "span" and self.in_math:
            self.contents.append("".join(self.current))
            self.current = []
            self.in_math = False


def validate_rendered(html_text: str) -> list[str]:
    parser = DisplayMathParser()
    parser.feed(html_text)
    errors = []
    if not any(FIRST_INTEGRAL in block and FIRST_EVALUATION in block
               for block in parser.contents):
        errors.append("first integral not inside MathJax display span")
    if not any(PARTS_EVALUATION in block for block in parser.contents):
        errors.append("integration-by-parts evaluation not inside MathJax display span")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=None)
    parser.add_argument("--source", type=Path, default=ROOT / SOURCE)
    args = parser.parse_args()
    errors = []
    try:
        errors.extend(validate_source(args.source.read_text(encoding="utf-8")))
    except OSError as exc:
        errors.append(f"source unavailable: {exc}")
    if args.site_dir is not None:
        html_path = args.site_dir / HTML
        try:
            errors.extend(validate_rendered(html_path.read_text(encoding="utf-8")))
        except OSError as exc:
            errors.append(f"rendered page unavailable: {exc}")
    if errors:
        for error in errors:
            print(f"MA-ART-0017-MATH: FAIL — {error}")
        return 1
    print("MA-ART-0017-MATH: PASS — display math correctly delimited"
          + (" and compiled" if args.site_dir is not None else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
