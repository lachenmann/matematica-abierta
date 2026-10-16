"""C01 full semantic rollout regression tests (read-only, no image generation)."""
import hashlib
import json
import unittest

from tools.check_anm_c01_semantic_html import (
    ROOT, CHAPTER, SOLUTIONS, REGISTRY, MAIN_IDS, SOLUTION_IDS,
    SRC_FIG, SOURCE_LINK, substantive_caption_fragments,
)
from tools.check_ma_fig_html import FigureIndex


class C01FullSemantics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.main = (ROOT / CHAPTER).read_text(encoding="utf-8")
        cls.solutions = (ROOT / SOLUTIONS).read_text(encoding="utf-8")
        cls.registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))

    def test_twelve_figures_in_integrated_chapter(self):
        matches = list(SRC_FIG.finditer(self.main))
        self.assertEqual(tuple(m.group(2) for m in matches), ("C01-F01", "C01-F02", "C01-F03", "C01-F05", "C01-F11", "C01-F06", "C01-F07", "C01-F12", "C01-F08", "C01-F13", "C01-F09", "C01-F14"))

    def test_four_figures_in_worked_solutions(self):
        matches = list(SRC_FIG.finditer(self.solutions))
        self.assertEqual(tuple(m.group(2) for m in matches), SOLUTION_IDS)

    def test_all_figures_have_unique_stable_anchors_and_descriptive_alts(self):
        matches = list(SRC_FIG.finditer(self.main + "\n" + self.solutions))
        self.assertEqual(len(matches), 16)
        self.assertEqual(len({m.group(3) for m in matches}), 12)
        for src in (self.main, self.solutions):
            anchors = [m.group(3) for m in SRC_FIG.finditer(src)]
            self.assertEqual(len(anchors), len(set(anchors)))
        for m in matches:
            self.assertEqual(m.group(3), "fig-anm-c01-f" + m.group(2)[-2:])
            self.assertGreaterEqual(len(m.group(4)), 50)
            self.assertFalse(m.group(1).startswith(m.group(2) + "."))

    def test_legacy_duplicate_caption_paragraphs_are_gone(self):
        for src in (self.main, self.solutions):
            self.assertNotIn("svg){fig-alt=", src)
            self.assertNotRegex(src, r"(?m)^\*Figura C01-F\d\d\.")

    def test_fifteen_prose_references_are_stable_links(self):
        self.assertEqual(len(SOURCE_LINK.findall(self.main)), 6)
        self.assertEqual(len(SOURCE_LINK.findall(self.solutions)), 6)
        for key, anchor_key in SOURCE_LINK.findall(self.main + self.solutions):
            self.assertEqual(key, anchor_key)

    def test_f04_f10_remain_absent_as_graphical_assets(self):
        for obsolete in ("C01-F04.svg", "C01-F10.svg"):
            self.assertNotIn(obsolete, self.main)
            self.assertNotIn(obsolete, self.solutions)

    def test_existing_twelve_svg_files_still_match_obisidian_hashes(self):
        expected = self.registry["all_existing_svg_sha256"]
        self.assertEqual(set(expected), set(MAIN_IDS + SOLUTION_IDS))
        for fid, sha in expected.items():
            p = ROOT / "assets/books/anm/C01" / (fid + ".svg")
            self.assertTrue(p.is_file(), fid)
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), sha)

    def test_brackets_inside_math_caption_are_not_truncated(self):
        source = list(SRC_FIG.finditer(self.solutions))
        figure_f11 = next(m for m in source if m.group(2) == "C01-F11")
        self.assertIn("$[x,z]$", figure_f11.group(1))
        self.assertTrue(substantive_caption_fragments(figure_f11.group(1)))

    def test_synthetic_html_figure_has_caption_alt_and_anchor(self):
        index = FigureIndex()
        index.feed('<div id="fig-anm-c01-f11"><figure>'
                   '<img src="old.svg" alt="Descripción accesible">'
                   '<figcaption>Figura 1: El exceso de recorrido crece.</figcaption>'
                   '</figure></div>')
        self.assertEqual(index.figures[0]["anchors"], ["fig-anm-c01-f11"])
        self.assertEqual(index.figures[0]["images"][0]["alt"], "Descripción accesible")


if __name__ == "__main__":
    unittest.main()
