"""C9 HTML-only contract tests. All assets are inert byte stubs; no image created."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.check_ma_fig_html import check, rendered_target, verify_html_figure, FigureIndex


class C9RenderedHtmlTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"
        self.site = self.root / "_site"
        self.root.mkdir()
        self.site.mkdir()
        (self.root / "data/ma-fig-manifests").mkdir(parents=True)
        (self.root / "data/ma-fig-scope-v1.json").write_text(json.dumps({
            "schema_version": 1,
            "formal_treatise_prefixes": ["libros/otros/tratado-funciones/"],
            "formal_treatise_exact": [],
            "non_treatise_landing_exceptions": []
        }))
        self.consumer = "libros/para-matematicos/leccion.qmd"
        self.asset = "assets/books/math/diag.svg"
        source = self.root / self.consumer
        source.parent.mkdir(parents=True)
        source.write_text("# Lección\n", encoding="utf-8")
        self.approved = self.root / self.asset
        self.approved.parent.mkdir(parents=True)
        # Deliberately NOT an SVG illustration: non-graphic sentinel bytes only.
        self.payload = b"TEST-ONLY-NOT-A-GRAPHIC"
        self.approved.write_bytes(self.payload)
        self.rendered = self.site / self.asset
        self.rendered.parent.mkdir(parents=True)
        self.rendered.write_bytes(self.payload)
        self.html_page = self.site / Path(self.consumer).with_suffix(".html")
        self.html_page.parent.mkdir(parents=True)
        self.doc = {
            "schema_version": 1,
            "figure_id": "MA_FIG_FAKE_HTML_01",
            "figure_label": "fig-mapping-01",
            "consumer_source": self.consumer,
            "document_class": "PEDAGOGICAL_BOOK",
            "status": "READY_FOR_PUBLICATION",
            "outputs": {"web_svg": self.asset},
            "output_sha256": {"web_svg": hashlib.sha256(self.payload).hexdigest()},
            "alt": "La relación entre dos conjuntos finitos, indicando imágenes y preimágenes.",
            "caption": "Diagrama de correspondencias entre dos conjuntos finitos.",
        }
        self.write_html()

    def write_html(self, alt=None, caption=None, figure_label=None, image=None, wrap=True):
        alt = self.doc["alt"] if alt is None else alt
        caption = self.doc["caption"] if caption is None else caption
        figure_label = self.doc["figure_label"] if figure_label is None else figure_label
        src = "../../" + self.asset if image is None else image
        fragment = (
            '<figure class="quarto-float quarto-float-fig">'
            '<img src="' + src + '" alt="' + alt + '">'
            '<figcaption>Figura 1: ' + caption + '</figcaption></figure>'
        )
        if wrap:
            fragment = '<div id="' + figure_label + '" class="quarto-figure">' + fragment + '</div>'
        self.html_page.write_text('<html><body><main>' + fragment + '</main></body></html>',
                                  encoding="utf-8")

    def problems(self, doc=None):
        return verify_html_figure(self.site, self.root,
                                  self.doc if doc is None else doc)

    def test_valid_quarto_markup(self):
        self.assertEqual(self.problems(), [])

    def test_manifest_backed_check(self):
        entry = self.root / "data/ma-fig-manifests/figure.json"
        entry.write_text(json.dumps(self.doc))
        self.assertEqual(check(self.root, self.site), (1, []))

    def test_empty_registry_reports_zero_not_full_audit(self):
        self.assertEqual(check(self.root, self.site), (0, []))

    def test_missing_rendered_page_rejected(self):
        self.html_page.unlink()
        self.assertIn("HTML missing", " ".join(self.problems()))

    def test_missing_rendered_asset_rejected(self):
        self.rendered.unlink()
        self.assertIn("absent", " ".join(self.problems()))

    def test_modified_rendered_asset_rejected(self):
        self.rendered.write_bytes(b"CORRUPTED-STUB")
        self.assertIn("differs", " ".join(self.problems()))

    def test_modified_approved_asset_rejected(self):
        changed = dict(self.doc, output_sha256={"web_svg": "0" * 64})
        self.assertIn("checksum mismatch", " ".join(self.problems(changed)))

    def test_missing_image_reference_rejected(self):
        self.write_html(image="../../assets/another.svg")
        self.assertIn("expected one", " ".join(self.problems()))

    def test_external_html_asset_rejected(self):
        self.write_html(image="https://example.invalid/asset.svg")
        self.assertIn("expected one", " ".join(self.problems()))

    def test_generic_alt_rejected(self):
        self.write_html(alt="gráfico")
        self.assertIn("alt", " ".join(self.problems()))

    def test_wrong_alt_rejected(self):
        self.write_html(alt="Esquema diferente.")
        self.assertIn("alt", " ".join(self.problems()))

    def test_caption_absent_rejected(self):
        self.write_html(caption="Texto diferente.")
        self.assertIn("caption", " ".join(self.problems()))

    def test_quarto_numbered_caption_passes(self):
        self.assertEqual(self.problems(), [])

    def test_missing_figure_anchor_rejected(self):
        self.write_html(wrap=False)
        self.assertIn("anchor", " ".join(self.problems()))

    def test_wrong_figure_anchor_rejected(self):
        self.write_html(figure_label="fig-other-01")
        self.assertIn("anchor", " ".join(self.problems()))

    def test_wrong_figure_label_rejected(self):
        changed = dict(self.doc, figure_label="missing-prefix")
        self.assertIn("figure_label", " ".join(self.problems(changed)))

    def test_duplicate_images_rejected(self):
        text = self.html_page.read_text()
        text = text.replace("<figcaption>", '<img src="../../' + self.asset + '" alt="' +
                            self.doc["alt"] + '"><figcaption>')
        self.html_page.write_text(text)
        self.assertIn("found 2", " ".join(self.problems()))

    def test_not_an_html_figure_rejected(self):
        self.html_page.write_text('<main><img src="../../' + self.asset + '"></main>')
        self.assertIn("expected one", " ".join(self.problems()))

    def test_formal_consumer_rejected(self):
        changed = dict(self.doc, consumer_source="libros/otros/tratado-funciones/capitulo.qmd")
        self.assertIn("formal treatise", " ".join(self.problems(changed)))

    def test_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            rendered_target(self.site, self.html_page, "../../../../outside.svg")

    def test_external_resource_rejected(self):
        with self.assertRaises(ValueError):
            rendered_target(self.site, self.html_page, "https://example.invalid/a.svg")

    def test_root_absolute_site_resource(self):
        self.write_html(image="/" + self.asset)
        self.assertEqual(self.problems(), [])

    def test_html_parser_single_figure(self):
        f = FigureIndex()
        f.feed(self.html_page.read_text())
        self.assertEqual(len(f.figures), 1)
        self.assertEqual(len(f.figures[0]["images"]), 1)


if __name__ == "__main__":
    unittest.main()
