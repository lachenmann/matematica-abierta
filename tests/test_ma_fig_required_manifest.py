"""C8 figure manifest references: tests use source text, not generated images."""
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.check_ma_fig_manifest import (
    educational_source, image_references, normalize_illustration_ref,
    new_educational_image_references,
)


class NewIllustrationManifestTests(unittest.TestCase):
    CONSUMER = "libros/para-matematicos/leccion.qmd"
    ASSET = "assets/books/anm/new-diagram.svg"
    REF = "![Nueva figura](../../assets/books/anm/new-diagram.svg)"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.scope = {
            "formal_treatise_prefixes": ["libros/otros/tratado-funciones/"],
            "formal_treatise_exact": ["libros/otros/tratado-de-algebra.md"],
            "non_treatise_landing_exceptions": ["libros/tratados/index.qmd"],
        }
        self.path = self.root / self.CONSUMER
        self.path.parent.mkdir(parents=True)
        self.path.write_text("# Lección\n", encoding="utf-8")
        self.git("init", "-q")
        self.git("config", "user.name", "MA Figure QA")
        self.git("config", "user.email", "qa@example.invalid")
        self.git("add", ".")
        self.git("commit", "-qm", "baseline")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.run(("git", *args), cwd=self.root, check=True,
                              capture_output=True, text=True).stdout.strip()

    def modify(self, text, consumer=None):
        filename = self.root / (consumer or self.CONSUMER)
        filename.parent.mkdir(parents=True, exist_ok=True)
        filename.write_text(text, encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "update")

    def manifest(self, **update):
        record = {
            "figure_id": "MA_FIG_TEST_100",
            "consumer_source": self.CONSUMER,
            "document_class": "PEDAGOGICAL_BOOK",
            "status": "READY_FOR_PUBLICATION",
            "outputs": {"web_svg": self.ASSET},
        }
        record.update(update)
        return record

    def gate(self, records=()):
        return new_educational_image_references(
            self.root, self.base, self.scope, list(records)
        )

    def test_unregistered_new_figure_is_blocked(self):
        self.modify("# Lección\n" + self.REF + "\n")
        self.assertIn("C8-MANIFEST", " ".join(self.gate()))

    def test_matching_manifest_passes(self):
        self.modify("# Lección\n" + self.REF + "\n")
        self.assertEqual(self.gate([self.manifest()]), [])

    def test_wrong_consumer_does_not_approve(self):
        self.modify("# Lección\n" + self.REF + "\n")
        self.assertTrue(self.gate([
            self.manifest(consumer_source="libros/para-matematicos/otra.qmd")
        ]))

    def test_wrong_asset_does_not_approve(self):
        self.modify("# Lección\n" + self.REF + "\n")
        self.assertTrue(self.gate([
            self.manifest(outputs={"web_svg": "assets/books/anm/other.svg"})
        ]))

    def test_draft_manifest_does_not_approve_integration(self):
        self.modify("# Lección\n" + self.REF + "\n")
        self.assertTrue(self.gate([self.manifest(status="DRAFT")]))

    def test_duplicate_claimants_rejected(self):
        self.modify("# Lección\n" + self.REF + "\n")
        self.assertTrue(self.gate([self.manifest(), self.manifest(
            figure_id="MA_FIG_TEST_101"
        )]))

    def test_existing_reference_grandfathered(self):
        old = "# Lección\n" + self.REF + "\n"
        self.path.write_text(old, encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "preexisting figure")
        self.base = self.git("rev-parse", "HEAD")
        self.modify(old + "\nPárrafo corregido.\n")
        self.assertEqual(self.gate(), [])

    def test_relocated_old_reference_not_new(self):
        old = "# Lección\n" + self.REF + "\nTexto\n"
        self.path.write_text(old, encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "old illustration")
        self.base = self.git("rev-parse", "HEAD")
        self.modify("# Lección\nTexto\n" + self.REF + "\n")
        self.assertEqual(self.gate(), [])

    def test_new_duplicate_reference_requires_manifest(self):
        old = "# Lección\n" + self.REF + "\n"
        self.path.write_text(old, encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "original")
        self.base = self.git("rev-parse", "HEAD")
        self.modify(old + self.REF + "\n")
        self.assertTrue(self.gate())

    def test_html_image_reference_is_checked(self):
        self.modify('# Lección\n<img alt="diagrama" src="../../assets/books/anm/new-diagram.svg">\n')
        self.assertEqual(self.gate([self.manifest()]), [])

    def test_external_image_is_rejected(self):
        self.modify("# Lección\n![figura](https://example.invalid/figure.svg)\n")
        self.assertIn("external", " ".join(self.gate()))

    def test_reference_style_image_fails_closed(self):
        self.modify("# Lección\n![figura][f]\n\n[f]: ../../assets/books/anm/new-diagram.svg\n")
        self.assertIn("reference-style", " ".join(self.gate()))

    def test_code_fence_images_do_not_require_manifest(self):
        self.modify("# Lección\n~~~md\n" + self.REF + "\n~~~\n")
        self.assertEqual(self.gate(), [])

    def test_html_comment_images_do_not_require_manifest(self):
        self.modify("# Lección\n<!-- " + self.REF + " -->\n")
        self.assertEqual(self.gate(), [])

    def test_site_article_class_is_distinct(self):
        path = "teoria/resultados/explicacion.qmd"
        self.modify("# Artículo\n![figura](../../assets/books/anm/new-diagram.svg)\n", path)
        row = self.manifest(
            consumer_source=path, document_class="SITE_EDUCATIONAL"
        )
        self.assertEqual(self.gate([row]), [])

    def test_formal_treatise_is_outside_educational_gate(self):
        self.assertFalse(educational_source(
            "libros/otros/tratado-funciones/capitulo-01.qmd", self.scope
        ))

    def test_relative_and_root_paths_are_equivalent(self):
        self.assertEqual(
            normalize_illustration_ref("../../assets/books/anm/new-diagram.svg",
                                       self.CONSUMER), self.ASSET
        )
        self.assertEqual(
            normalize_illustration_ref("/assets/books/anm/new-diagram.svg",
                                       self.CONSUMER), self.ASSET
        )

    def test_reference_cannot_escape_checkout(self):
        with self.assertRaises(ValueError):
            normalize_illustration_ref("../../../../outside.svg", self.CONSUMER)

    def test_code_comment_parser(self):
        self.assertEqual(image_references("~~~md\n![no](x.svg)\n~~~"), [])
        self.assertEqual(image_references("<!-- ![no](x.svg) -->"), [])


if __name__ == "__main__":
    unittest.main()
