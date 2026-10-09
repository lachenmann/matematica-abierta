import unittest
from pathlib import Path
from tools.check_ma_fig_manifest import is_formal_treatise, checked_path

class TestMaFigureScope(unittest.TestCase):
    def test_formal_treatise_is_excluded(self):
        scope = {"formal_treatise_prefixes":["libros/otros/tratado-funciones/"], "formal_treatise_exact":[], "non_treatise_landing_exceptions":[]}
        self.assertTrue(is_formal_treatise("libros/otros/tratado-funciones/capitulo-05.qmd",scope))

    def test_pedagogical_book_is_eligible(self):
        scope = {"formal_treatise_prefixes":[], "formal_treatise_exact":[], "non_treatise_landing_exceptions":[]}
        self.assertFalse(is_formal_treatise("libros/para-matematicos/capitulo.md",scope))

    def test_paths_cannot_escape_root(self):
        with self.assertRaises(ValueError):
            checked_path(Path("/tmp"),"../outside.md","test")

    def test_formal_fallback(self):
        scope = {"formal_treatise_prefixes":[], "formal_treatise_exact":[], "non_treatise_landing_exceptions":[]}
        self.assertTrue(is_formal_treatise("libros/otros/tratado-futuro.qmd",scope))

    def test_treatise_landing_exception(self):
        scope = {"formal_treatise_prefixes":["libros/tratados/"], "formal_treatise_exact":[], "non_treatise_landing_exceptions":["libros/tratados/index.qmd"]}
        self.assertFalse(is_formal_treatise("libros/tratados/index.qmd",scope))


    def test_no_false_positive_for_math(self):
        from tools.check_ma_fig_manifest import FIGURE_MARKUP
        self.assertIsNone(FIGURE_MARKUP.search("$ f(x)=x^2 $"))

    def test_image_reference_is_detected(self):
        from tools.check_ma_fig_manifest import FIGURE_MARKUP
        self.assertIsNotNone(FIGURE_MARKUP.search("![Ejemplo](figura.svg)"))

    def test_landing_navigation_is_not_figure(self):
        from tools.check_ma_fig_manifest import FIGURE_MARKUP
        self.assertIsNone(FIGURE_MARKUP.search('<link rel="icon" href="logo.svg">'))

    def test_scope_main_registry_schema(self):
        from tools.check_ma_fig_manifest import load_scope, ROOT
        self.assertEqual(load_scope(ROOT)["schema_version"], 1)

    def test_svg_plain_xml_allowed(self):
        from tools.check_ma_fig_manifest import validate_svg
        sample = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1"/>'
        self.assertEqual(validate_svg(sample, "unit"), [])

    def test_svg_remote_dependency_denied(self):
        from tools.check_ma_fig_manifest import validate_svg
        sample = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1"><use href="external.svg"/></svg>'
        self.assertTrue(validate_svg(sample, "unit"))

if __name__ == "__main__":
    unittest.main()
