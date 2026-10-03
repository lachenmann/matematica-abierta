"""Publication checks for the complete HTML edition of the algebra treatise."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import argparse, json, re, shutil, subprocess

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = sorted((ROOT / "libros/capitulos").glob("tratado-de-algebra*.md"))
BOOK = ROOT / "libros/otros/tratado-de-algebra.md"
REGISTRY = (ROOT / "_project/ID_REGISTRY.md").read_text(encoding="utf-8")
ANCHOR = re.compile(r"\{#([\w:-]+)\}")
def metadata(source, key):
    m = re.search(r"^" + re.escape(key) + r": (.+)$", source, re.M)
    assert m, (key, source[:120])
    return m[1].strip("'\"")
def formulas(source):
    # Pandoc handles multiline math and Markdown blockquote markers.
    command = ["quarto", "pandoc"] if shutil.which("quarto") else ["pandoc"]
    result = subprocess.run(command + ["--from", "markdown", "--to", "json"],
                            input=source, text=True, capture_output=True, check=True)
    expressions = []
    def visit(node):
        if isinstance(node, dict):
            if node.get("t") == "Math":
                expressions.append(" ".join(node["c"][1].split()))
            else:
                for value in node.values():
                    visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)
    visit(json.loads(result.stdout)["blocks"])
    return expressions
def tex(source):
    source = source.strip()
    if source.startswith((r"\(", r"\[")):
        source = source[2:-2]
    return " ".join(source.split())
def source_target(origin, href):
    u = urlsplit(href)
    if u.scheme or u.netloc:
        return None, None
    path = unquote(u.path)
    target = ROOT / path.lstrip("/") if path.startswith("/") else origin.parent / path if path else origin
    if target.suffix == ".html":
        candidates = [target.with_suffix(".md"), target.with_suffix(".qmd")]
        target = next((p for p in candidates if p.is_file()), target)
    return target, unquote(u.fragment)

def source_anchors(path, seen=None):
    seen = set() if seen is None else seen
    assert path not in seen, ("recursive include", path)
    seen.add(path)
    source = path.read_text(encoding="utf-8")
    ids = set(ANCHOR.findall(source))
    ids.update(re.findall(r"""\bid=["']([^"']+)["']""", source))
    for include in re.findall(r"\{\{<\s*include\s+(.+?)\s*>\}\}", source):
        included = path.parent / include.strip().strip("'\\\"")
        assert included.is_file(), ("missing include", path, included)
        ids.update(source_anchors(included, seen.copy()))
    return ids

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids, self.main_ids, self.links, self.math, self.h1 = [], [], [], [], 0
        self.in_main = False
        self.math_depth = 0
        self.chunks = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "main":
            self.in_main = True
        if self.in_main:
            if attrs.get("id"):
                self.main_ids.append(attrs["id"])
            if tag == "a" and attrs.get("href"):
                self.links.append(attrs["href"])
            if tag == "h1":
                self.h1 += 1
            if self.math_depth:
                if tag not in {"br", "img", "input", "meta", "link", "hr", "wbr"}:
                    self.math_depth += 1
            elif tag == "span" and "math" in attrs.get("class", "").split():
                self.math_depth, self.chunks = 1, []
    def handle_endtag(self, tag):
        if self.math_depth:
            self.math_depth -= 1
            if self.math_depth == 0:
                self.math.append(tex("".join(self.chunks)))
        if tag == "main":
            self.in_main = False
    def handle_data(self, data):
        if self.math_depth:
            self.chunks.append(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", type=Path)
    parser.add_argument("--skip-links", action="store_true")
    args = parser.parse_args()
    assert len(CHAPTERS) == 43, len(CHAPTERS)
    sources = {path: path.read_text(encoding="utf-8") for path in CHAPTERS}
    sources[BOOK] = BOOK.read_text(encoding="utf-8")
    chapter_ids, anchors = [], []
    for path in CHAPTERS:
        s = sources[path]
        chapter_ids.append(metadata(s, "content-id"))
        assert metadata(s, "book-id") == "MA-BOK-0007", path
        assert metadata(s, "content-type") == "book-chapter", path
        assert metadata(s, "status") == "published", path
        assert metadata(s, "license") == "GFDL-1.3-or-later", path
        assert not re.search(r"^# ", s, re.M), ("duplicate title", path)
        assert not re.search(r"^#+ .*ejercicios", s, re.M | re.I), path
        assert not re.search(r"Auditoría local|Siguiente reserva|Progreso general|canonical-path:|proof-id:|result-id:|status: closed", s), path
        ids = [a for a in ANCHOR.findall(s) if a.startswith("talg-")]
        assert len(ids) == len(set(ids)), path
        anchors += ids
        assert re.search(r"^\| " + re.escape(chapter_ids[-1]) + r" \|", REGISTRY, re.M), path
    assert len(chapter_ids) == len(set(chapter_ids)) == 43
    assert len(anchors) == len(set(anchors)) == 507, len(anchors)
    proofs = {a for a in anchors if a.startswith("talg-prf-")}
    assert proofs == {f"talg-prf-{i:05d}" for i in range(1, 199)}
    book = sources[BOOK]
    front = book.split("---", 2)[1]
    related = set(re.findall(r"^\s+- (MA-BCH-\d+)\s*$", front, re.M))
    assert related == set(chapter_ids), (related ^ set(chapter_ids))
    listing = set(re.findall(r"\]\((\.\./capitulos/tratado-de-algebra[^)]+\.md)\)", book))
    assert len(listing) == 43, len(listing)
    assert "40 capítulos" in book and "43 unidades" in book
    assert "Ruta prevista" not in book and "permanece en elaboración" not in book
    for path in sources:
        if args.skip_links:
            continue
        for href in re.findall(r"\]\(([^)]+)\)", sources[path]):
            target, fragment = source_target(path, href)
            if target is None:
                continue
            assert target.is_file(), (path, href, target)
            if fragment.startswith(("talg-", "ta-", "parte-")) and target.suffix in {".md", ".qmd"}:
                assert fragment in source_anchors(target), (path, href, fragment)
    rendered = 0
    if args.html:
        out = ROOT / args.html
        pages = {}
        for path, source in sources.items():
            target = out / path.relative_to(ROOT).with_suffix(".html")
            assert target.is_file(), target
            p = Page(target.read_text(encoding="utf-8"))
            pages[target] = p
            duplicates = [i for i, n in Counter(p.main_ids).items() if n > 1]
            assert not duplicates, (target, duplicates)
            assert p.h1 == 1, (target, p.h1)
            expected = {a for a in ANCHOR.findall(source) if a.startswith("talg-")}
            actual = {a for a in p.main_ids if a.startswith("talg-")}
            assert expected == actual, (target, expected ^ actual)
            assert p.math == formulas(source), (target, len(p.math), len(formulas(source)))
            for href in p.links:
                u = urlsplit(href)
                if u.scheme or u.netloc:
                    continue
                linked = (target.parent / unquote(u.path)).resolve() if u.path else target.resolve()
                if linked.is_file() and linked.suffix == ".html" and u.fragment:
                    linked_page = pages.get(linked) or Page(linked.read_text(encoding="utf-8"))
                    assert unquote(u.fragment) in linked_page.ids, (target, href)
            rendered += 1
        assert len(pages) == 44
    print(json.dumps({"status": "PASS", "chapters": 43, "anchors": 507, "proofs": 198, "rendered_pages": rendered, "math_exact": bool(args.html)}, ensure_ascii=False))
if __name__ == "__main__":
    main()
