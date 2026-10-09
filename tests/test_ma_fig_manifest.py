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

if __name__ == "__main__":
    unittest.main()
