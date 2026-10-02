from manim import *

# Marca audiovisual de Matemática Abierta.
# Reconstrucción canónica v2 a partir de la intro aprobada en Mac.

BG = "#0F1117"
FG = "#F5F7FA"
BLUE = "#22AFF5"
MUTED = "#A7B0BE"


def a_squared(scale: float = 1.0) -> VGroup:
    """Símbolo A² reutilizable, con A y 2 como objetos independientes."""
    a = MathTex("A", color=BLUE).scale(2.25 * scale)
    two = MathTex("2", color=BLUE).scale(0.72 * scale)
    two.next_to(a, UR, buff=0.03)
    two.shift(0.10 * DOWN + 0.03 * LEFT)
    return VGroup(a, two)


def wordmark(scale: float = 1.0) -> VGroup:
    """Wordmark Matemátic + A² + biertA."""
    left = Tex(r"Matemátic", color=FG).scale(1.25 * scale)
    mark = a_squared(scale=0.72 * scale)
    right = Tex(r"biertA", color=FG).scale(1.25 * scale)
    group = VGroup(left, mark, right).arrange(RIGHT, buff=0.10)
    mark.shift(0.02 * DOWN)
    return group


def tagline(scale: float = 1.0) -> Tex:
    return Tex(
        r"CONOCIMIENTO PARA TODOS",
        color=MUTED,
    ).scale(0.44 * scale)


def infinity_rule(scale: float = 1.0) -> VGroup:
    inf = MathTex(r"\infty", color=MUTED).scale(0.70 * scale)
    left = Line(LEFT * 2.20, LEFT * 0.60, color=MUTED, stroke_width=1.5)
    right = Line(RIGHT * 0.60, RIGHT * 2.20, color=MUTED, stroke_width=1.5)
    return VGroup(left, inf, right).arrange(RIGHT, buff=0.18)
