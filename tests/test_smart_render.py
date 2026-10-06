import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("smart_render", Path(__file__).resolve().parents[1] / "tools/smart_render.py")
smart = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(smart)


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.call("init", "-q")
        self.call("config", "user.email", "probe@example.invalid")
        self.call("config", "user.name", "Probe")
        self.write("index.qmd", '---\ntitle: Inicio\n---\n\n# Inicio\n\nTexto inicial.\n')
        self.write("page.qmd", '---\ntitle: Página\n---\n\n# Página\n\n{{< include _fragment.md >}}\n')
        self.write("_fragment.md", '## Sección {#sec-prueba}\n\nUna explicación.\n\n$$x^2=2$$\n')
        self.write("list.qmd", '---\ntitle: Lista\nlisting: default\n---\n\nLista.\n')
        self.commit()
        self.base = {"commit": self.call("rev-parse", "HEAD"), "site": {"index.html": "a", "page.html": "b", "list.html": "c"}}

    def call(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True).strip()

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def commit(self):
        self.call("add", ".")
        self.call("commit", "-qm", "fixture")

    def edit(self, name, old, new):
        path = self.root / name
        path.write_text(path.read_text().replace(old, new))
        self.commit()

    def test_body_edit_and_listings(self):
        self.edit("index.qmd", "Texto inicial", "Texto corregido")
        result = smart.plan(self.root, self.base)
        self.assertEqual(result["mode"], "incremental")
        self.assertEqual(result["targets"], ["index.qmd", "list.qmd"])

    def test_nested_shared_include(self):
        self.edit("_fragment.md", "Una explicación", "Una explicación ampliada")
        result = smart.plan(self.root, self.base)
        self.assertEqual(result["targets"], ["list.qmd", "page.qmd"])

    def test_recursive_include_consumers(self):
        self.write("_deep.md", "Texto profundo")
        self.write("_fragment.md", "{{< include _deep.md >}}\n")
        self.commit()
        self.base["commit"] = self.call("rev-parse", "HEAD")
        self.edit("_deep.md", "Texto profundo", "Texto corregido")
        self.assertEqual(smart.plan(self.root, self.base)["targets"], ["list.qmd", "page.qmd"])

    def test_cumulative_changes_since_cached_commit(self):
        self.edit("_fragment.md", "Una explicación", "Otra explicación")
        self.edit("index.qmd", "Texto inicial", "Texto corregido")
        self.assertEqual(smart.plan(self.root, self.base)["targets"], ["index.qmd", "list.qmd", "page.qmd"])

    def test_formula_correction(self):
        self.edit("_fragment.md", "x^2=2", "x^2=3")
        self.assertEqual(smart.plan(self.root, self.base)["mode"], "incremental")

    def test_metadata_changes_force_full(self):
        self.edit("index.qmd", "title: Inicio", "title: Nuevo")
        self.assertEqual(smart.plan(self.root, self.base)["mode"], "full")

    def test_heading_changes_force_full(self):
        self.edit("_fragment.md", "## Sección", "## Nueva sección")
        self.assertEqual(smart.plan(self.root, self.base)["mode"], "full")

    def test_resource_changes_force_full(self):
        self.write("theme.scss", "body {}")
        self.commit()
        self.assertEqual(smart.plan(self.root, self.base)["mode"], "full")

    def test_deletion_forces_full(self):
        (self.root / "index.qmd").unlink()
        self.commit()
        self.assertEqual(smart.plan(self.root, self.base)["mode"], "full")

    def test_unmapped_fragment_forces_full(self):
        self.write("_orphan.md", "Original")
        self.commit()
        self.base["commit"] = self.call("rev-parse", "HEAD")
        self.edit("_orphan.md", "Original", "Corregido")
        self.assertEqual(smart.plan(self.root, self.base)["mode"], "full")

    def test_source_unchanged_reuses(self):
        self.assertEqual(smart.plan(self.root, self.base)["mode"], "reuse")

    def test_corrupt_cached_output_rejected(self):
        self.write("_site/index.html", "valid")
        self.write(".quarto/idx/page", "valid")
        data = {"schema": smart.SCHEMA, "quarto": "test", "offline_books": [], "commit": self.base["commit"],
                "site": smart.inventory(self.root / "_site"), "quarto_state": smart.inventory(self.root / ".quarto")}
        self.write(".ma-build/base.json", json.dumps(data))
        self.assertEqual(smart.verify_base(self.root, "test", [])["commit"], self.base["commit"])
        self.write("_site/index.html", "corrupt")
        with self.assertRaisesRegex(ValueError, "integrity"):
            smart.verify_base(self.root, "test", [])

    def test_partial_output_loss_detected(self):
        self.write("_site/index.html", "a")
        self.write("_site/page.html", "b")
        base = {"site": smart.inventory(self.root / "_site")}
        (self.root / "_site/page.html").unlink()
        with self.assertRaisesRegex(ValueError, "inventory"):
            smart.check_preservation(self.root, base, ["index.qmd"])

    def test_unexpected_asset_mutation_detected(self):
        self.write("_site/index.html", "a")
        self.write("_site/style.css", "b")
        base = {"site": smart.inventory(self.root / "_site")}
        self.write("_site/style.css", "changed")
        with self.assertRaisesRegex(ValueError, "outside affected"):
            smart.check_preservation(self.root, base, ["index.qmd"])

    def test_incremental_failure_retries_clean_full(self):
        self.write("_site/stale.html", "old")
        self.write(".quarto/stale", "old")
        base = {"commit": self.base["commit"]}
        decision = {"mode": "incremental", "reason": "test", "changed": ["index.qmd"], "targets": ["index.qmd"]}
        calls = []
        def fake_render(root, targets=None):
            calls.append(targets)
            if targets is not None:
                raise subprocess.CalledProcessError(1, "quarto")
            self.assertFalse((root / "_site/stale.html").exists())
            self.assertFalse((root / ".quarto/stale").exists())
            self.write("_site/index.html", "new")
        with patch.object(smart, "version", return_value="test"), patch.object(smart, "verify_base", return_value=base), patch.object(smart, "plan", return_value=decision), patch.object(smart, "render", side_effect=fake_render), patch.object(smart, "validate_site"), patch.object(smart, "offline", return_value={}):
            report = smart.build(self.root)
        self.assertEqual(calls, [["index.qmd"], None])
        self.assertEqual(report["mode"], "full")


class StructureTests(unittest.TestCase):
    def test_links_labels_citations_and_code_force_full(self):
        for old, new in [("[a](old.html)", "[a](new.html)"), ("{#thm-a}", "{#thm-b}"), ("@prp-a", "@prp-b"), ("```python\nprint(1)\n```", "```python\nprint(2)\n```"), ('<img src="a.png">', '<img src="b.png">')]:
            with self.subTest(old=old):
                self.assertFalse(smart.safe_edit(old, new))

    def test_unclosed_and_inline_code_changes_force_full(self):
        self.assertFalse(smart.safe_edit("```python\n1", "```python\n2"))
        self.assertFalse(smart.safe_edit("Resultado `{python} 1`", "Resultado `{python} 2`"))
        self.assertFalse(smart.safe_edit("<script>run(1)</script>", "<script>run(2)</script>"))

    def test_offline_package_reused_for_unrelated_page(self):
        manifest = {"contents": [{"canonicalPath": "/physics.html"}]}
        with patch.object(smart, "verify_package", return_value=manifest), patch.object(smart.subprocess, "run") as run:
            result = smart.offline(Path("/tmp"), ["MA-BOK-0005"], {"mode": "incremental", "targets": ["licencia.qmd"]})
        self.assertEqual(result, {"MA-BOK-0005": "reused"})
        run.assert_not_called()

    def test_offline_package_rebuilt_when_chapter_changed(self):
        manifest = {"contents": [{"canonicalPath": "/physics.html"}]}
        with patch.object(smart, "verify_package", return_value=manifest), patch.object(smart.subprocess, "run") as run:
            result = smart.offline(Path("/tmp"), ["MA-BOK-0005"], {"mode": "incremental", "targets": ["physics.md"]})
        self.assertEqual(result, {"MA-BOK-0005": "regenerated"})
        run.assert_called_once()

    def test_corrupt_offline_package_is_regenerated(self):
        with patch.object(smart, "verify_package", side_effect=[ValueError("corrupt"), {}]), patch.object(smart.subprocess, "run") as run:
            result = smart.offline(Path("/tmp"), ["MA-BOK-0005"], {"mode": "reuse", "targets": []})
        self.assertEqual(result, {"MA-BOK-0005": "regenerated"})
        run.assert_called_once()


if __name__ == "__main__":
    unittest.main()
