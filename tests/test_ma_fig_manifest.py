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


class TestManifestValidation(unittest.TestCase):
    def setUp(self):
        import hashlib
        import json
        import tempfile
        self._temp = tempfile.TemporaryDirectory()
        self.addCleanup(self._temp.cleanup)
        self.root = Path(self._temp.name)
        (self.root / "data/ma-fig-manifests").mkdir(parents=True)
        self.scope = {"schema_version": 1, "formal_treatise_prefixes": ["libros/otros/tratado-funciones/"], "formal_treatise_exact": [], "non_treatise_landing_exceptions": []}
        (self.root / "data/ma-fig-scope-v1.json").write_text(json.dumps(self.scope))
        consumer = self.root / "libros/para-matematicos/leccion.qmd"
        consumer.parent.mkdir(parents=True)
        consumer.write_text("# Lección")
        source = self.root / "tools/figures/contract.txt"
        source.parent.mkdir(parents=True)
        source.write_text("x maps to y")
        graphic = self.root / "assets/books/contract.svg"
        graphic.parent.mkdir(parents=True)
        data = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"/>'
        graphic.write_bytes(data)
        self.manifest = {
            "schema_version":1, "figure_id":"MA_FIG_TEST_2026",
            "document_class":"PEDAGOGICAL_BOOK",
            "consumer_source":"libros/para-matematicos/leccion.qmd",
            "status":"READY_FOR_PUBLICATION",
            "source_canonical":"Obsidian/Vault/Matematica/figura.md",
            "source_repository":"tools/figures/contract.txt",
            "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
            "build_toolchain_digest":"locked-test-environment",
            "build_command":"python3 tools/build_figures.py",
            "outputs":{"web_svg":"assets/books/contract.svg"},
            "output_sha256":{"web_svg":hashlib.sha256(data).hexdigest()},
            "author_generation_authorization":"GRANTED_WITH_EVIDENCE",
            "authorization_evidence":"synthetic test approval",
            "rights":"CLEARED",
            "caption":"Representación conceptual de una relación entre conjuntos.",
            "alt":"Dos conjuntos relacionados mediante una única asignación por elemento.",
            "qa": {x:"PASS" for x in ("math","visual","technical","accessibility","rights","integration")}
        }

    def issues(self, **changes):
        from tools.check_ma_fig_manifest import validate_manifest
        return validate_manifest({**self.manifest, **changes},self.root,self.scope,"fixture")

    def test_complete_contract(self):
        self.assertEqual(self.issues(), [])

    def test_draft_does_not_authorize_generation(self):
        self.assertEqual(self.issues(status="REFERENCE_ONLY",source_repository=None,author_generation_authorization="NOT_GRANTED"), [])

    def test_denied_authorization_rejected(self):
        self.assertIn("C2-AUTH"," ".join(self.issues(author_generation_authorization="NOT_GRANTED")))

    def test_missing_approval_evidence_rejected(self):
        self.assertIn("C2-AUTH"," ".join(self.issues(authorization_evidence="")))

    def test_uncleared_rights_rejected(self):
        self.assertIn("QA-RIGHTS"," ".join(self.issues(rights="PENDING")))

    def test_missing_source_rejected(self):
        self.assertIn("source missing"," ".join(self.issues(source_repository="tools/figures/absent.txt")))

    def test_changed_source_checksum_rejected(self):
        self.assertIn("mismatch"," ".join(self.issues(source_sha256="0"*64)))

    def test_changed_output_checksum_rejected(self):
        self.assertIn("mismatch"," ".join(self.issues(output_sha256={"web_svg":"0"*64})))

    def test_short_alt_text_rejected(self):
        self.assertIn("QA-A11Y"," ".join(self.issues(alt="diagrama")))

    def test_unapproved_quality_gates_rejected(self):
        qa={x:"PASS" for x in ("math","visual","technical","accessibility","rights","integration")}
        qa["math"]="PENDING"
        self.assertIn("QA:"," ".join(self.issues(qa=qa)))

    def test_formal_consumer_masquerading_as_book_rejected(self):
        self.assertIn("C0-SCOPE"," ".join(self.issues(consumer_source="libros/otros/tratado-funciones/capitulo-01.qmd")))

    def test_formal_class_rejected(self):
        self.assertIn("cannot use"," ".join(self.issues(document_class="FORMAL_TREATISE")))

    def test_duplicate_identifiers_rejected(self):
        import json
        from tools.check_ma_fig_manifest import check
        directory=self.root / "data/ma-fig-manifests"
        for name in ("one.json","two.json"):
            (directory/name).write_text(json.dumps(self.manifest))
        self.assertIn("duplicate figure_id"," ".join(check(self.root)))


class TestFormalSourceDiff(unittest.TestCase):
    def _exercise_diff(self, extra):
        import subprocess
        import tempfile
        from tools.check_ma_fig_manifest import diff_formal_additions
        with tempfile.TemporaryDirectory() as place:
            root=Path(place)
            file=root / "libros/otros/tratado-funciones/capitulo-01.qmd"
            file.parent.mkdir(parents=True)
            file.write_text("# Capítulo\n")
            def git(*args):
                return subprocess.run(("git",*args),cwd=root,check=True,
                    capture_output=True,text=True).stdout.strip()
            git("init","-q")
            git("config","user.name","QA")
            git("config","user.email","qa@example.invalid")
            git("add",".")
            git("commit","-qm","base")
            base=git("rev-parse","HEAD")
            file.write_text("# Capítulo\n"+extra)
            git("add",".")
            git("commit","-qm","change")
            scope={"formal_treatise_prefixes":["libros/otros/tratado-funciones/"],
                "formal_treatise_exact":[],"non_treatise_landing_exceptions":[]}
            return diff_formal_additions(root,base,scope)

    def test_formal_diagram_is_rejected_in_git_diff(self):
        self.assertIn("C0-SCOPE"," ".join(self._exercise_diff("![Ejemplo](archivo.svg)\n")))

    def test_equation_is_not_a_diagram_in_git_diff(self):
        self.assertEqual(self._exercise_diff("$ x^2+y^2=1 $\n"), [])

if __name__ == "__main__":
    unittest.main()
