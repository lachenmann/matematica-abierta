"""Regression tests for C01 figures, including the preserved F01/F12 pilot."""
import hashlib
import json
import unittest
from pathlib import Path

from tools.check_anm_c01_pilot_html import (
    ROOT, CHAPTER, SOLUTIONS, REGISTRY, MAIN_ID, SOL_ID, source_figure,
)
from tools.check_ma_fig_html import FigureIndex


class C01PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapter = (ROOT / CHAPTER).read_text(encoding="utf-8")
        cls.solutions = (ROOT / SOLUTIONS).read_text(encoding="utf-8")
        cls.registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))

    def test_main_figure_has_single_caption_and_alt(self):
        _, matches = source_figure(self.chapter, MAIN_ID)
        self.assertEqual(len(matches), 1)
        self.assertGreater(len(matches[0][2]), 50)
        self.assertFalse(matches[0][1].startswith("C01-F01."))
        self.assertNotIn("*Figura C01-F01.", self.chapter)

    def test_solution_figure_has_single_caption_and_alt(self):
        _, matches = source_figure(self.solutions, SOL_ID)
        self.assertEqual(len(matches), 1)
        self.assertGreater(len(matches[0][2]), 50)
        self.assertNotIn("*Figura C01-F12.", self.solutions)

    def test_full_chapter_rollout_retains_pilot_and_12_figures(self):
        self.assertEqual(self.chapter.count('svg){#fig-anm-c01-'), 8)
        self.assertEqual(self.solutions.count('svg){#fig-anm-c01-'), 4)
        self.assertEqual(self.chapter.count('svg){fig-alt="'), 0)
        self.assertEqual(self.solutions.count('svg){fig-alt="'), 0)

    def test_all_twelve_approved_svgs_remain_byte_identical(self):
        hashes = self.registry["all_existing_svg_sha256"]
        self.assertEqual(len(hashes), 12)
        for fid, canonical in hashes.items():
            target = ROOT / "assets/books/anm/C01" / (fid + ".svg")
            self.assertTrue(target.is_file(), fid)
            self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(), canonical, fid)

    def test_solution_reference_links_remain_after_explanations(self):
        self.assertEqual(self.solutions.count("[C01-F12](#fig-anm-c01-f12)"), 3)
        self.assertIn("### 32. Cuándo una bola cabe dentro de otra", self.solutions)
        self.assertIn("### 37.", self.solutions)
        self.assertEqual(self.solutions.count("C01-F12.svg"), 1)

    def test_quarto_figure_index_parses_wrapper_without_svg(self):
        parser = FigureIndex()
        parser.feed(
            '<div id="fig-anm-c01-f12"><figure><img src="existing.svg" '
            'alt="Descripción matemática"/><figcaption>Figura 1: Leyenda.</figcaption>'
            '</figure></div>'
        )
        self.assertEqual(len(parser.figures), 1)
        self.assertEqual(parser.figures[0]["anchors"], ["fig-anm-c01-f12"])


if __name__ == "__main__":
    unittest.main()
