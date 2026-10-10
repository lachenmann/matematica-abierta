"""ANM C00 editorial figure contract tests; no images are created."""
import hashlib
import json
import re
import unittest
from pathlib import Path

from tools.check_anm_c00_semantic_html import CHAPTER, SOLUTIONS, REGISTRY, FIG_RE, SOURCE_LINK_RE
from tools.check_ma_fig_html import FigureIndex

ROOT = Path(__file__).resolve().parents[1]


class ANMC00SemanticContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapter = (ROOT / CHAPTER).read_text(encoding="utf-8")
        cls.solutions = (ROOT / SOLUTIONS).read_text(encoding="utf-8")
        cls.registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
        cls.figures = list(FIG_RE.finditer(cls.chapter))

    def test_twelve_distinct_approved_figures_in_reading_order(self):
        ids = [m[2] for m in self.figures]
        self.assertEqual(ids, self.registry["figure_order"])
        self.assertEqual(len(set(ids)), 12)

    def test_exactly_one_caption_and_alt_for_each_figure(self):
        for m in self.figures:
            id, anchor = m[2], m[3]
            self.assertEqual(anchor, "fig-anm-c00-f" + id[-2:].lower())
            self.assertTrue(m[1].strip())
            self.assertGreater(len(m[4].strip()), 50)
            self.assertFalse(m[1].startswith(id + "."))
        self.assertNotRegex(self.chapter, r"(?m)^\*Figura C00-F\d\d\.")

    def test_approved_graphics_match_current_canonical_bytes(self):
        self.assertEqual(len(self.registry["original_svg_sha256"]), 12)
        for id, sha in self.registry["current_svg_sha256"].items():
            resource = ROOT / "assets/books/anm" / (id + ".svg")
            self.assertTrue(resource.is_file(), id)
            self.assertEqual(hashlib.sha256(resource.read_bytes()).hexdigest(), sha)

    def test_all_35_solution_references_are_deep_links(self):
        links = list(SOURCE_LINK_RE.finditer(self.solutions))
        self.assertEqual(len(links), 35)
        all_ids = [m.group(0) for m in re.finditer(r"C00-F\d\d", self.solutions)]
        self.assertEqual(len(all_ids), 35)
        expected = set(self.registry["figure_order"])
        self.assertTrue(all("C00-F" + m[1] in expected for m in links))

    def test_each_figure_is_referenced_by_internal_anchor_in_chapter(self):
        for id in self.registry["figure_order"]:
            fragment = "#fig-anm-c00-f" + id[-2:].lower()
            self.assertIn(fragment, self.chapter)

    def test_html_parser_handles_quarto_wrapper(self):
        html = ('<div id="fig-anm-c00-f01"><figure>'
                '<img src="../../assets/books/anm/C00-F01.svg" alt="Texto descriptivo">'
                '<figcaption>Figura 1: La especificación abre la pregunta de existencia.</figcaption>'
                '</figure></div>')
        parsed = FigureIndex()
        parsed.feed(html)
        self.assertEqual(len(parsed.figures), 1)
        self.assertEqual(parsed.figures[0]["anchors"], ["fig-anm-c00-f01"])
        self.assertEqual(parsed.figures[0]["images"][0]["alt"], "Texto descriptivo")


if __name__ == "__main__":
    unittest.main()
