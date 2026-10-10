"""Regression tests for the MA-ART-0017 MathJax display-math gate."""
import unittest

from tools.check_ma_art_0017_math import validate_source, validate_rendered

EQUATION = (
    "$$\n"
    "\\int_{-1}^{1}x\\,dx\n"
    "=\\left.\\frac{x^2}{2}\\right|_{-1}^{1}\n"
    "=0.\n"
    "$$\n"
)
PARTS = "$$\n\\left.-\\frac{\\cos x}{x}\\right|_1^R\n$$\n"
HTML_EQUATION = (
    '<span class="math display">\\[\n'
    '\\int_{-1}^{1}x\\,dx\n'
    '=\\left.\\frac{x^2}{2}\\right|_{-1}^{1}\n'
    '=0.\n\\]</span>'
)
HTML_PARTS = (
    '<span class="math display">'
    '\\[\\left.-\\frac{\\cos x}{x}\\right|_1^R\\]'
    '</span>'
)


class MathDelimiterRegression(unittest.TestCase):
    def test_well_formed_source(self):
        self.assertEqual(validate_source(EQUATION + PARTS), [])

    def test_lost_dollar_sign_is_detected(self):
        broken = EQUATION.replace("=0.\n$$", "=0.\n$")
        problems = validate_source(broken + PARTS)
        self.assertTrue(any("single-$" in e for e in problems))
        self.assertTrue(any("unbalanced" in e for e in problems))

    def test_correct_mathjax_render(self):
        self.assertEqual(validate_rendered(HTML_EQUATION + HTML_PARTS), [])

    def test_raw_tex_after_broken_fence_is_detected(self):
        broken = "<p>$$ <em>{-1}^{1}x,dx =.|</em>{-1}^{1}=0. $</p>"
        problems = validate_rendered(broken + HTML_PARTS)
        self.assertTrue(any("first integral not inside" in e for e in problems))


if __name__ == "__main__":
    unittest.main()
