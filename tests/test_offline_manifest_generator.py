import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from generate_offline_manifests import (
    build_manifest,
    build_offline_render_command,
    load_catalog,
    optimize_offline_html,
    resolve_source_path,
    select_book,
    validate_self_contained_html,
)


def sample_catalog():
    return {
        "schemaVersion": 1,
        "generatedAt": "2026-10-05T17:00:00Z",
        "siteBaseUrl": "https://matematicaabierta.cl",
        "items": [
            {
                "id": "MA-BOK-0005",
                "type": "book",
                "title": "Física para matemáticos",
                "path": "/libros/para-matematicos/fisica-para-matematicos.html",
                "status": "published",
                "related": ["MA-BCH-0009", "MA-BCH-0031"],
            },
            {
                "id": "MA-BCH-0009",
                "type": "book-chapter",
                "title": "Capítulo 1",
                "path": "/libros/capitulos/capitulo-1.html",
                "parentId": "MA-BOK-0005",
                "dateModified": "2026-09-10",
                "status": "published",
            },
            {
                "id": "MA-BCH-0031",
                "type": "book-chapter",
                "title": "Capítulo 2",
                "path": "/libros/capitulos/capitulo-2.html",
                "parentId": "MA-BOK-0005",
                "dateModified": "2026-09-15",
                "status": "published",
            },
        ],
    }


class OfflineManifestGeneratorTests(unittest.TestCase):
    def test_catalog_and_book_selection_are_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "catalog.json"
            path.write_text(json.dumps(sample_catalog()), encoding="utf-8")
            catalog = load_catalog(path)

        book, chapters = select_book(catalog, "MA-BOK-0005")
        self.assertEqual(book["id"], "MA-BOK-0005")
        self.assertEqual(
            [item["id"] for item in chapters],
            ["MA-BCH-0009", "MA-BCH-0031"],
        )

        with self.assertRaisesRegex(ValueError, "bookId inválido"):
            select_book(catalog, "../bad")

    def test_book_related_defines_reading_order(self):
        catalog = sample_catalog()
        book = next(
            item for item in catalog["items"] if item["id"] == "MA-BOK-0005"
        )
        book["related"] = ["MA-BCH-0031", "MA-BCH-0009"]

        _, chapters = select_book(catalog, "MA-BOK-0005")
        self.assertEqual(
            [item["id"] for item in chapters],
            ["MA-BCH-0031", "MA-BCH-0009"],
        )

    def test_book_without_complete_reading_order_fails_closed(self):
        catalog = sample_catalog()
        book = next(
            item for item in catalog["items"] if item["id"] == "MA-BOK-0005"
        )
        book["related"] = ["MA-BCH-0009"]

        with self.assertRaisesRegex(ValueError, "orden de todos sus capítulos"):
            select_book(catalog, "MA-BOK-0005")

    def test_offline_render_uses_minimal_self_contained_html(self):
        root = Path("/repo")
        source = root / "libros" / "capitulos" / "capitulo-1.md"
        output_dir = Path("/tmp/offline")

        command = build_offline_render_command(
            root,
            source,
            output_dir,
            quarto="quarto",
        )

        self.assertIn("minimal:true", command)
        self.assertIn("toc:false", command)
        self.assertIn("anchor-sections:false", command)
        self.assertIn("code-copy:false", command)
        self.assertIn("fig-responsive:true", command)
        self.assertIn("embed-resources:true", command)
        self.assertIn("self-contained-math:true", command)
        self.assertEqual(
            command[:4],
            ["quarto", "render", "libros/capitulos/capitulo-1.md", "--to"],
        )

    def test_source_resolution_uses_canonical_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "libros" / "capitulos" / "capitulo-1.md"
            source.parent.mkdir(parents=True)
            source.write_text("---\ntitle: X\n---\n", encoding="utf-8")

            self.assertEqual(
                resolve_source_path(root, "/libros/capitulos/capitulo-1.html"),
                source,
            )

    def test_offline_optimizer_keeps_main_math_and_static_css(self):
        from urllib.parse import quote

        theme_css = (
            "@font-face {font-family: 'Source Sans Pro';"
            "src:url(data:font/ttf;base64,AAAA);}"
            "body{font-family:'Source Sans Pro',sans-serif}"
        )
        encoded_theme = "data:text/css," + quote(
            theme_css,
            safe="!()*+,/:;=?@-._~",
        )
        html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<link href="{encoded_theme}" rel="stylesheet">
<style>@font-face {{font-family: "bootstrap-icons";src:url(data:font/woff;base64,BBBB);}} .bi{{display:inline-block}}</style>
<script>/*! @algolia/autocomplete-js 1.19.1 */ window.SEARCH = true;</script>
<script type="text/javascript">window.MathJax = {{startup: {{}}}};</script>
<script>window.CONTENT_SPECIFIC = true;</script>
</head>
<body class="fullcontent">
<header id="quarto-header"><nav>chrome</nav></header>
<main class="content" id="quarto-document-content">
<h1 id="x">Capítulo</h1>
<p><span class="math inline">\\(x^2\\)</span></p>
<table><tr><td>1</td></tr></table>
</main>
<footer>chrome</footer>
</body>
</html>""".encode("utf-8")

        optimized = optimize_offline_html(html, label="sample").decode("utf-8")

        self.assertIn('id="quarto-document-content"', optimized)
        self.assertIn('class="math inline"', optimized)
        self.assertIn("<table>", optimized)
        self.assertIn("window.MathJax", optimized)
        self.assertIn("window.CONTENT_SPECIFIC", optimized)
        self.assertIn("Source%20Sans%20Pro", optimized)

        self.assertNotIn("quarto-header", optimized)
        self.assertNotIn("<footer>", optimized)
        self.assertNotIn("@algolia/autocomplete-js", optimized)
        self.assertNotIn("data:font/ttf;base64,AAAA", optimized)
        self.assertNotIn("bootstrap-icons", optimized)
        self.assertLess(len(optimized), len(html))

    def test_offline_optimizer_ignores_html_literals_inside_mathjax(self):
        html = b"""<!DOCTYPE html>
<html lang="es">
<head>
<script type="text/javascript">
window.MathJax = {};
const template = "<html><head></head><body><main>fake</main></body></html>";
</script>
<style>main{max-width:70ch}</style>
</head>
<body class="fullcontent">
<header id="quarto-header">chrome</header>
<main id="quarto-document-content">
<figure><img src="data:image/png;base64,AA=="><figcaption>Figura</figcaption></figure>
<table><tr><td>dato</td></tr></table>
<p><a href="https://example.com">fuente</a></p>
</main>
<footer>chrome</footer>
</body>
</html>"""

        optimized = optimize_offline_html(html, label="mathjax-template").decode(
            "utf-8"
        )

        self.assertTrue(optimized.startswith("<!DOCTYPE html>\n<html"))
        self.assertIn("window.MathJax", optimized)
        self.assertIn(
            'const template = "<html><head></head><body><main>fake</main></body></html>";',
            optimized,
        )
        self.assertIn('id="quarto-document-content"', optimized)
        self.assertEqual(optimized.count('id="quarto-document-content"'), 1)
        self.assertIn('src="data:image/png;base64,AA=="', optimized)
        self.assertIn("<table>", optimized)
        self.assertIn('<a href="https://example.com">fuente</a>', optimized)
        self.assertLess(
            optimized.index("</script>"),
            optimized.index('<main id="quarto-document-content">'),
        )
        self.assertNotIn("quarto-header", optimized)
        self.assertNotIn("<footer>", optimized)

    def test_offline_optimizer_preserves_content_icons_and_language(self):
        html = b"""<!DOCTYPE html>
<html lang="la">
<head>
<style>@font-face {font-family: "bootstrap-icons";src:url(data:font/woff;base64,BBBB);} .bi{display:inline-block}</style>
<script>window.MathJax = {};</script>
</head>
<body>
<header id="quarto-header">chrome</header>
<main id="quarto-document-content"><i class="bi bi-star"></i><p>Textus</p></main>
</body>
</html>"""

        optimized = optimize_offline_html(html, label="icons").decode("utf-8")

        self.assertIn('<html lang="la">', optimized)
        self.assertIn("bootstrap-icons", optimized)
        self.assertIn('class="bi bi-star"', optimized)

    def test_display_math_separates_vertical_overflow_from_horizontal_scroll(self):
        css = (ROOT / "styles.scss").read_text(encoding="utf-8")

        outer_match = re.search(
            r"\.math\.display\s*\{([^}]*)\}",
            css,
            re.S,
        )
        self.assertIsNotNone(outer_match)
        outer = outer_match.group(1)
        self.assertIn("overflow: visible", outer)
        self.assertNotIn("overflow-x: auto", outer)

        scroll_match = re.search(
            r'\.math\.display\s*>\s*mjx-container\[display="true"\]\s*\{([^}]*)\}',
            css,
            re.S,
        )
        self.assertIsNotNone(scroll_match)
        scroll = scroll_match.group(1)
        self.assertIn("overflow-x: auto", scroll)
        self.assertIn("padding-top: 0.55em !important", scroll)
        self.assertIn("padding-bottom: 0.65em !important", scroll)

    def test_self_contained_validation_allows_external_links_but_not_subresources(self):
        validate_self_contained_html(
            b'<html><body><a href="https://example.com">x</a>'
            b'<img src="data:image/png;base64,AA=="></body></html>',
            label="ok",
        )

        with self.assertRaisesRegex(ValueError, "subrecurso externo"):
            validate_self_contained_html(
                b'<html><body><script src="https://cdn.example/x.js"></script></body></html>',
                label="bad",
            )

    def test_manifest_hashes_real_bytes_and_version_is_deterministic(self):
        catalog = sample_catalog()
        book, chapters = select_book(catalog, "MA-BOK-0005")
        artifacts = {
            "MA-BCH-0009": b"<html><body>uno</body></html>",
            "MA-BCH-0031": b"<html><body>dos</body></html>",
        }

        first = build_manifest(
            book,
            chapters,
            artifacts,
            generated_at="2026-10-05T17:00:00Z",
        )
        second = build_manifest(
            book,
            chapters,
            artifacts,
            generated_at="2026-10-05T18:00:00Z",
        )

        self.assertEqual(first["schemaVersion"], 1)
        self.assertEqual(first["bookId"], "MA-BOK-0005")
        self.assertEqual(first["entryContentId"], "MA-BCH-0009")
        self.assertEqual(first["assets"], [])
        self.assertEqual(first["version"], second["version"])
        self.assertEqual(
            first["totalSize"],
            sum(item["size"] for item in first["contents"]),
        )
        self.assertEqual(len(first["contents"][0]["sha256"]), 64)

        changed = dict(artifacts)
        changed["MA-BCH-0031"] = b"<html><body>dos revisado</body></html>"
        third = build_manifest(
            book,
            chapters,
            changed,
            generated_at="2026-10-05T18:00:00Z",
        )
        self.assertNotEqual(first["version"], third["version"])


if __name__ == "__main__":
    unittest.main()
