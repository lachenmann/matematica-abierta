"""Comprobaciones de los defectos encontrados en la auditoría audiovisual.

Ejecutar desde audiovisual/manim: uv run python cpm_yt_c01_v01/verify_production_layout.py
No genera ni modifica el audio o los marcadores.
"""

from pathlib import Path
import sys
import unittest

import numpy as np
from manim import MoveAlongPath

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "clases"))
from cpm_yt_c01_v01_production import (
    CPMYTC01V01Production, BLUE, ORANGE, GREEN, FG,
)


class CaptureScene(CPMYTC01V01Production):
    def __init__(self):
        super().__init__()
        self.paths = []

    def play(self, *animations, **kwargs):
        self.paths.extend(a for a in animations if isinstance(a, MoveAlongPath))

    def wait(self, *args, **kwargs):
        pass


class ProductionLayoutChecks(unittest.TestCase):
    def test_commuting_symbols_take_opposite_lanes(self):
        scene = CaptureScene()
        for demo in (scene.commutativity_sum, scene.commutativity_product):
            scene.paths.clear()
            demo()
            self.assertEqual(len(scene.paths), 2)
            a, b = scene.paths
            # Comprueba las trayectorias que realmente entrega cada demostración.
            for t in np.linspace(0.1, 0.9, 49):
                pa = a.path.point_from_proportion(t)
                pb = b.path.point_from_proportion(t)
                self.assertGreater(pa[1], 0)
                self.assertLess(pb[1], 0)
                overlap_x = abs(pa[0] - pb[0]) < (a.mobject.width + b.mobject.width) / 2
                overlap_y = abs(pa[1] - pb[1]) < (a.mobject.height + b.mobject.height) / 2
                self.assertFalse(overlap_x and overlap_y, f"Colisión en t={t}")

    def test_integer_cards_contain_their_text(self):
        for box, title, body in CPMYTC01V01Production().integer_field_audit_cards():
            for text in (title, body):
                self.assertGreater(text.get_left()[0], box.get_left()[0])
                self.assertLess(text.get_right()[0], box.get_right()[0])
                self.assertGreater(text.get_bottom()[1], box.get_bottom()[1])
                self.assertLess(text.get_top()[1], box.get_top()[1])
            self.assertGreater(title.get_bottom()[1], body.get_top()[1])

    def test_equalities_keep_variable_colors_and_neutral_operators(self):
        expr = CPMYTC01V01Production().colored_formula(r"a\cdot(b+c)=a\cdot b+a\cdot c")
        palette = {"a": BLUE, "b": ORANGE, "c": GREEN}
        for part in expr:
            expected = palette.get(part.tex_string, FG)
            for glyph in part.family_members_with_points():
                self.assertEqual(glyph.get_color().to_hex().upper(), expected.upper())


if __name__ == "__main__":
    unittest.main()
