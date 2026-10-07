import json
import re
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from generate_offline_manifests import (
    build_manifest,
    load_catalog,
    resolve_source_path,
    select_book,
    validate_self_contained_html,
    write_book_package,
)
from canonical_offline import CanonicalAssets


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
    def test_runtime_distribution_integrity_is_checked_before_extraction(self):
        with tempfile.TemporaryDirectory() as tmp, patch('canonical_offline.download', return_value=b'corrupt archive'):
            with self.assertRaisesRegex(ValueError, 'integrity failed'):
                CanonicalAssets(Path(tmp)).mathjax()

    def test_canonical_resource_cannot_escape_site_or_fetch_unknown_origin(self):
        with tempfile.TemporaryDirectory() as tmp:
            assets = CanonicalAssets(Path(tmp))
            for url in ['../../outside.css', 'https://unapproved.example/style.css', 'file://host/private/style.css']:
                with self.subTest(url=url), self.assertRaises(ValueError):
                    assets.resource(url, (Path(tmp) / 'chapter.html').as_uri())

    def test_package_derives_canonical_html_without_rendering_markdown(self):
        catalog = sample_catalog()
        main = '<main class="content" id="quarto-document-content"><p id="p">Texto <span class="math inline">\\(x^2\\)</span></p></main>'
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / 'libros/capitulos').mkdir(parents=True)
            (site / 'theme.css').write_text('body{color:white}')
            for number in [1, 2]:
                (site / f'libros/capitulos/capitulo-{number}.html').write_text(
                    '<html lang="es"><head><link rel="stylesheet" href="../../theme.css">'
                    '<script id="ma-math-font-ready">window.MathJax={startup:{}};</script>'
                    '<script src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js"></script>'
                    '</head><body class="quarto-dark"><script id="quarto-html-before-body">window.theme=true;</script>'
                    '<nav>chrome</nav><div id="quarto-content" class="canonical-shell">' + main + '</div></body></html>')
            def runtime(assets):
                assets.assets['assets/mathjax/tex-chtml.js'] = b'window.MathJax={};'
                assets.assets['assets/mathjax-offline-speech.js'] = b'window.__maCreateSpeechWorker=null;'
            with patch.object(CanonicalAssets, 'mathjax', runtime), patch('subprocess.run', side_effect=AssertionError('must not render')):
                manifest_path = write_book_package(site, site, catalog, 'MA-BOK-0005')
            manifest = json.loads(manifest_path.read_text())
            self.assertEqual(len(manifest['assets']), 3)
            package = manifest_path.parent
            for item in manifest['contents']:
                html = (package / item['localPath']).read_text()
                self.assertIn(main, html)
                self.assertIn('class="canonical-shell"', html)
                self.assertIn('window.theme=true;', html)
                self.assertNotIn('<nav>', html)
                self.assertNotIn('cdn.jsdelivr.net', html)
            self.assertEqual(manifest['totalSize'], sum((package / i['localPath']).stat().st_size
                             for i in manifest['contents'] + manifest['assets']))

    def test_declared_relative_resources_and_css_dependencies(self):
        assets = {"assets/theme.css": b"body{color:red}"}
        html = b'<html><body><link rel="stylesheet" href="../assets/theme.css"></body></html>'
        validate_self_contained_html(html, label="ok", assets=assets)
        with self.assertRaises(ValueError):
            validate_self_contained_html(html, label="undeclared")
        validate_self_contained_html(
            b'<html><body><script>const sample="<img src=https://example.com/x>";</script></body></html>',
            label="script literal")

    def test_unsafe_resource_urls_fail_closed(self):
        for url in ["https://host/x", "http://host/x", "//host/x", "/assets/x.css",
                    "../../assets/x.css", "file:///assets/x.css", "javascript:alert(1)",
                    "../assets/missing.css", "../assets/%2e%2e/x.css", "..\\assets/x.css"]:
            for tag in ['<link rel="stylesheet" href="{}">', '<img src="{}">',
                        '<script src="{}"></script>', '<object data="{}"></object>']:
                with self.subTest(url=url, tag=tag), self.assertRaises(ValueError):
                    validate_self_contained_html(
                        ('<html><body>' + tag.format(url) + '</body></html>').encode(),
                        label="unsafe", assets={"assets/x.css": b""})

    def test_css_escape_import_and_embedded_styles_are_checked(self):
        from urllib.parse import quote
        css_cases = [r'@import "https://host/x";',
                     r'@\69mport "//host/x";',
                     r'body{background:u\72l(https://host/x)}',
                     'body{background:url(../outside.png)}',
                     'body{background:image-set("https://host/x" 1x)}']
        for css in css_cases:
            for markup in [f'<style>{css}</style>',
                           f'<link rel="stylesheet" href="data:text/css,{quote(css)}">']:
                with self.subTest(css=css), self.assertRaises(ValueError):
                    validate_self_contained_html(
                        f'<html><body>{markup}</body></html>'.encode(), label="css")

    def test_asset_paths_and_transitive_css_are_validated_before_manifest(self):
        book, chapters = select_book(sample_catalog(), "MA-BOK-0005")
        artifacts = {c["id"]: b"<html><body>x</body></html>" for c in chapters}
        for assets in [{"assets/../../escape.css": b""},
                       {"assets/a.css": b'@import "missing.css";'},
                       {"assets/a.css": b'body{background:url(https://host/x)}'}]:
            with self.subTest(assets=assets), self.assertRaises(ValueError):
                build_manifest(book, chapters, artifacts, generated_at="now", assets=assets)

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

        with_assets = build_manifest(
            book,
            chapters,
            artifacts,
            generated_at="2026-10-05T18:00:00Z",
            assets={
                "assets/quarto-bootstrap-light.css": b"body{font-family:test}",
                "assets/quarto-bootstrap-dark.css": b"body{font-family:test-dark}",
            },
        )
        self.assertEqual(len(with_assets["assets"]), 2)
        self.assertEqual(
            with_assets["totalSize"],
            first["totalSize"]
            + sum(item["size"] for item in with_assets["assets"]),
        )
        self.assertTrue(
            all(item["mediaType"] == "text/css" for item in with_assets["assets"])
        )
        self.assertNotEqual(first["version"], with_assets["version"])


if __name__ == "__main__":
    unittest.main()
