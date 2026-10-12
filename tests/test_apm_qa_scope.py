import unittest
from tools.apm_qa_scope import required

class Scope(unittest.TestCase):
 def test_legacy_chapter_still_runs_full_battery(self):
  self.assertTrue(required(['libros/capitulos/el-algebra-como-lenguaje-de-relaciones-y-estructuras.md'],{'libros/capitulos/el-algebra-como-lenguaje-de-relaciones-y-estructuras.md'},'',''))
 def test_shared_style_and_general_config_require_battery(self):
  self.assertTrue(required(['assets/books/reader.css'],set(),'',''))
  self.assertTrue(required(['_quarto.yml'],set(),'theme: light\n','theme: dark\n'))
 def test_unrelated_book_and_scoped_css_do_not_retest_apm(self):
  self.assertFalse(required(['libros/otros/elementos-del-calculo/index.qmd','libros/otros/tratado-funciones/tratado.css'],set(),'',''))
 def test_only_verbatim_licence_resource_is_exempt(self):
  old='project:\n  resources:\n    - "assets/books/cdr/**"\n'
  new=old.replace('  resources:\n','  resources:\n    - "COPYING.FDL"\n')
  self.assertFalse(required(['_quarto.yml'],set(),old,new))
  self.assertTrue(required(['_quarto.yml'],set(),old,new+'format: pdf\n'))

if __name__=='__main__':unittest.main()
