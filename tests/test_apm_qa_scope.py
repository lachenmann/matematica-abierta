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
 def test_tomo_ii_and_index_have_their_own_browser_battery(self):
  changed=['libros/capitulos/algebra-para-matematicos-tomo-ii-capitulo-01.md',
           'libros/para-matematicos/algebra-para-matematicos-tomo-ii.md',
           'libros/para-matematicos/algebra-para-matematicos.md']
  self.assertFalse(required(changed,set(),'',''))
  self.assertTrue(required(changed+['assets/books/reader.css'],set(),'',''))
 def test_tomo_i_prefixed_chapters_still_require_full_battery(self):
  self.assertTrue(required(['libros/capitulos/algebra-para-matematicos-capitulo-26.md'],set(),'',''))
 def test_licence_resource_keeps_general_config_checks(self):
  old='project:\n  resources:\n    - "assets/books/cdr/**"\n'
  new=old.replace('  resources:\n','  resources:\n    - "COPYING.FDL"\n')
  self.assertFalse(required(['_quarto.yml'],set(),old,new))
  self.assertTrue(required(['_quarto.yml'],set(),old,new+'format: pdf\n'))

 def test_other_book_resources_preserve_existing_composition(self):
  old='project:\n  type: website\n  resources:\n    - "assets/books/cdr/**"\n\nformat:\n  html: default\n'
  for added in ['    - assets/books/mp/**\n','    - "assets/books/fp/**"\n']:
   new=old.replace('  resources:\n','  resources:\n'+added)
   self.assertFalse(required(['_quarto.yml'],set(),old,new))
   self.assertTrue(required(['_quarto.yml','assets/books/reader.css'],set(),old,new))
   self.assertTrue(required(['_quarto.yml'],set(),old,new.replace('html: default','html: dark')))
 def test_existing_resources_cannot_be_removed_or_reordered(self):
  old='project:\n  resources:\n    - "assets/books/cdr/**"\n    - "COPYING.FDL"\n'
  removed=old.replace('    - "assets/books/cdr/**"\n','')
  reordered='project:\n  resources:\n    - "COPYING.FDL"\n    - "assets/books/cdr/**"\n'
  self.assertTrue(required(['_quarto.yml'],set(),old,removed))
  self.assertTrue(required(['_quarto.yml'],set(),old,reordered))
 def test_tomo_i_resource_additions_require_browser_battery(self):
  old='project:\n  resources:\n    - "COPYING.FDL"\n'
  for resource in ['assets/books/apm-tomo-i/**','assets/books/apm/**','assets/includes/**']:
   new=old+'    - "'+resource+'"\n'
   self.assertTrue(required(['_quarto.yml'],set(),old,new))
 def test_resources_outside_project_cannot_hide_presentation_changes(self):
  old='website:\n  resources:\n    - "COPYING.FDL"\n'
  new=old+'    - assets/books/mp/**\n'
  self.assertTrue(required(['_quarto.yml'],set(),old,new))

if __name__=='__main__':unittest.main()
