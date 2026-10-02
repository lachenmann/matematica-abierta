from manim import *

# -----------------------------------------------------------------------------
# Cálculo para matemáticos — Video 1 — Preview local de animaciones
# Manim Community 0.21.0
# Render local previsto desde:
# D:\\MatematicaAbierta-Main\\audiovisual\\manim
# -----------------------------------------------------------------------------

BG = "#0F1117"
FG = "#F5F7FA"
MUTED = "#A7B0BE"
BLUE = "#4EA1FF"
ORANGE = "#FFB454"
GREEN = "#63D471"
RED = "#FF6B6B"
VIOLET = "#B794F4"

config.background_color = BG


class CPMYTC01V01Preview(Scene):
    """Preview local, sin audio, de las animaciones del Video 1."""

    def construct(self):
        self.camera.background_color = BG

        # 01 — Apertura algebraica
        self.section_title("Aritmética conocida")
        arithmetic = MathTex(
            r"2+3=5", r"\qquad", r"2\cdot3=6", r"\qquad", r"2\cdot x=1\Longrightarrow x=\frac12",
            color=FG,
        ).scale(0.95)
        arithmetic[0].set_color(BLUE)
        arithmetic[2].set_color(ORANGE)
        arithmetic[4].set_color(GREEN)
        self.play(LaggedStart(*[FadeIn(m, shift=0.15 * UP) for m in arithmetic], lag_ratio=0.12))
        self.hold()
        self.clear_stage(arithmetic)

        # 02 — Cadena de sistemas numéricos
        self.section_title("Cadena de sistemas numéricos")
        chain = MathTex(
            r"\mathbb N", r"\subset", r"\mathbb Z", r"\subset", r"\mathbb Q", r"\subset", r"\mathbb R",
            color=FG,
        ).scale(1.35)
        chain[0].set_color(BLUE)
        chain[2].set_color(ORANGE)
        chain[4].set_color(GREEN)
        chain[6].set_color(VIOLET)
        self.play(LaggedStart(*[FadeIn(m, shift=0.18 * RIGHT) for m in chain], lag_ratio=0.10))
        self.hold(0.6)

        # Una proposición verdadera en N.
        expr = MathTex(
            r"3", r"+", r"5", r"=", r"8",
            color=FG,
        ).scale(1.5).move_to([0, -1.45, 0])
        expr[4].set_color(BLUE)
        marker = SurroundingRectangle(chain[0], color=BLUE, buff=0.12)
        self.play(Create(marker), FadeIn(expr))
        self.hold(0.55)

        # Cambian la operación y el resultado, pero no los operandos.
        minus = MathTex(r"-", color=RED).scale(1.5).move_to(expr[1].get_center())
        negative_two = MathTex(r"-2", color=RED).scale(1.5).move_to(expr[4].get_center())
        self.play(
            Transform(expr[1], minus),
            Transform(expr[4], negative_two),
            run_time=0.75,
            rate_func=smooth,
        )
        self.hold(0.35)

        not_natural = MathTex(r"-2\notin\mathbb N", color=RED).scale(1.0)
        not_natural.next_to(expr, DOWN, buff=0.30)
        self.play(FadeIn(not_natural, shift=0.10 * UP))
        self.hold(0.55)

        # Z resuelve exactamente el problema anterior.
        in_integers = MathTex(r"-2\in\mathbb Z", color=ORANGE).scale(1.0)
        in_integers.next_to(expr, DOWN, buff=0.30)
        self.play(
            marker.animate.move_to(chain[2]).set_color(ORANGE),
            FadeOut(not_natural),
            FadeIn(in_integers, shift=0.10 * UP),
            run_time=0.8,
        )
        self.hold(0.55)
        self.play(FadeOut(expr), FadeOut(in_integers))

        # Ahora aparece un problema nuevo dentro de Z.
        eq = MathTex(r"2\cdot x=1", color=FG).scale(1.35).move_to([0, -1.45, 0])
        self.play(FadeIn(eq))
        self.hold(0.35)

        half = MathTex(r"x=\frac12", color=GREEN).scale(1.35).move_to(eq)
        self.play(TransformMatchingTex(eq, half))
        self.hold(0.35)

        half_not_z = MathTex(r"\frac12\notin\mathbb Z", color=RED).scale(1.0)
        half_not_z.next_to(half, DOWN, buff=0.30)
        self.play(FadeIn(half_not_z, shift=0.10 * UP))
        self.hold(0.55)

        half_in_q = MathTex(r"\frac12\in\mathbb Q", color=GREEN).scale(1.0)
        half_in_q.next_to(half, DOWN, buff=0.30)
        self.play(
            marker.animate.move_to(chain[4]).set_color(GREEN),
            FadeOut(half_not_z),
            FadeIn(half_in_q, shift=0.10 * UP),
            run_time=0.8,
        )
        self.hold(0.55)
        self.clear_stage(chain, half, half_in_q, marker)

        # 03 — Spoiler tenue
        spoiler = Tex(r"Spoiler: supremo", color=MUTED).scale(0.78)
        self.play(FadeIn(spoiler, run_time=0.8))
        self.hold(0.5)
        self.play(FadeOut(spoiler, run_time=0.8))

        # 04 — Conjunto y clausura
        self.section_title("Operaciones internas")
        f_nonempty = MathTex(r"F\neq\varnothing", color=FG).scale(1.35)
        closure = MathTex(
            r"a,b\in F",
            r"\Longrightarrow",
            r"a+b\in F,\qquad a\cdot b\in F",
            color=FG,
        ).scale(1.05).next_to(f_nonempty, DOWN, buff=0.65)
        closure[2].set_color(BLUE)
        self.play(FadeIn(f_nonempty))
        self.play(LaggedStart(*[FadeIn(m) for m in closure], lag_ratio=0.10))
        self.hold()
        self.clear_stage(f_nonempty, closure)

        # 05 — Dos operaciones primitivas
        self.section_title("Dos operaciones primitivas")
        plus = MathTex(r"+", color=BLUE).scale(3)
        times = MathTex(r"\cdot", color=ORANGE).scale(3)
        ops = VGroup(plus, times).arrange(RIGHT, buff=2.4)
        self.play(GrowFromCenter(plus), GrowFromCenter(times))
        self.hold(0.6)
        self.clear_stage(ops)

        # 06–09 — Axiomas aditivos
        self.section_title("Axiomas aditivos")
        self.associativity_sum()
        self.additive_identity()
        self.additive_inverse()
        self.commutativity_sum()

        # 10–13 — Axiomas multiplicativos
        self.section_title("Axiomas multiplicativos")
        self.associativity_product()
        self.multiplicative_identity()
        self.multiplicative_inverse()
        self.commutativity_product()

        # 14 — Distributividad y lectura inversa
        self.section_title("Distributividad")
        self.distributivity_demo()

        # 15 — Cuerpo trivial
        self.section_title("Cuerpo trivial")
        trivial = MathTex(r"F=\{0\},\qquad", r"1=0", color=FG).scale(1.25)
        trivial[1].set_color(RED)
        ops_trivial = MathTex(r"0+0=0,\qquad", r"0\cdot0=0", color=FG).scale(1.1)
        ops_trivial.next_to(trivial, DOWN, buff=0.65)
        exclusion = MathTex(r"0\neq1", color=GREEN).scale(1.45).next_to(ops_trivial, DOWN, buff=0.65)
        self.play(Write(trivial))
        self.play(LaggedStart(Write(ops_trivial[0]), Write(ops_trivial[1]), lag_ratio=0.45))
        self.play(FadeIn(exclusion, shift=0.15 * UP))
        box = SurroundingRectangle(exclusion, color=GREEN, buff=0.16)
        self.play(Create(box))
        self.hold(0.7)
        self.clear_stage(trivial, ops_trivial, exclusion, box)

        # 16 — Tabla de síntesis
        self.section_title("Condición estructural y nueve axiomas")
        self.axiom_summary()

        # 17 — F_2 de Spivak
        self.section_title("Cuerpo de dos elementos")
        self.f2_demo()

        # 18 — Lo que todavía no hemos supuesto
        self.section_title("Propiedades todavía no demostradas")
        pending = VGroup(
            MathTex(r"a\cdot0=0", color=FG),
            MathTex(r"-(-a)=a", color=FG),
            MathTex(r"(-a)\cdot(-b)=a\cdot b", color=FG),
            MathTex(r"a\cdot b=0\Longrightarrow a=0\ \text{o}\ b=0", color=FG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42).scale(0.92)
        for row in pending:
            q = MathTex(r"?", color=ORANGE).scale(1.15).next_to(row, RIGHT, buff=0.35)
            row.add(q)
        self.play(LaggedStart(*[FadeIn(row, shift=0.12 * RIGHT) for row in pending], lag_ratio=0.18))
        self.hold(0.8)
        self.clear_stage(pending)

        # 19 — Los enteros no forman un cuerpo
        self.section_title("Los enteros no forman un cuerpo")
        integers = MathTex(r"\mathbb Z", color=ORANGE).scale(2.2)
        circle = Circle(radius=1.5, color=ORANGE).move_to(integers)
        eq2 = MathTex(r"2\cdot x=1", color=FG).scale(1.25).to_edge(DOWN, buff=1.2)
        half2 = MathTex(r"x=\frac12", color=GREEN).scale(1.25).move_to(eq2)
        half_floating = MathTex(r"\frac12", color=GREEN).scale(1.6).move_to(integers)
        self.play(Create(circle), FadeIn(integers))
        self.play(Write(eq2))
        self.play(TransformMatchingTex(eq2, half2))
        self.play(FadeIn(half_floating))
        self.play(
            half_floating.animate.shift(3.0 * RIGHT).set_color(RED),
            circle.animate.set_color(RED),
            integers.animate.set_color(RED),
        )
        not_in = MathTex(r"\frac12\notin\mathbb Z", color=RED).scale(1.2).to_edge(DOWN, buff=1.0)
        self.play(FadeOut(half2), FadeIn(not_in, shift=0.14 * UP))
        self.hold(0.8)
        self.clear_stage(circle, integers, half_floating, not_in)

        # 20 — Q y R sí
        self.section_title("Dos cuerpos familiares")
        qr = MathTex(r"\mathbb Q", r"\qquad", r"\mathbb R", color=FG).scale(1.8)
        qr[0].set_color(GREEN)
        qr[2].set_color(VIOLET)
        self.play(FadeIn(qr, scale=0.92))
        self.hold(0.8)
        self.clear_stage(qr)

        # 21 — Enlace con el siguiente video
        self.section_title("Siguiente clase: teoremas derivados de los axiomas")

        source_box = RoundedRectangle(
            width=5.3, height=1.25, corner_radius=0.16,
            color=BLUE, stroke_width=2.0,
        ).move_to([0, 1.55, 0])
        source_title = Tex(r"Axiomas de cuerpo", color=BLUE).scale(0.82)
        source_formula = MathTex(
            r"0\neq1", r"\qquad", r"+", r"\qquad", r"\cdot",
            color=FG,
        ).scale(0.90)
        source_group = VGroup(source_box, source_title, source_formula)
        source_title.move_to(source_box.get_center() + 0.28 * UP)
        source_formula.move_to(source_box.get_center() + 0.28 * DOWN)

        self.play(Create(source_box))
        self.play(FadeIn(source_title), FadeIn(source_formula))
        self.hold(0.35)

        cards = VGroup(
            self.theorem_card("Unicidad del cero", r"0=0'", BLUE),
            self.theorem_card("Unicidad del inverso", r"b+c=0=b+d\Longrightarrow c=d", ORANGE),
            self.theorem_card("Producto por cero", r"a\cdot0=0", GREEN),
            self.theorem_card("Cancelación", r"a\cdot b=a\cdot c,\ a\neq0\Longrightarrow b=c", VIOLET),
        ).arrange_in_grid(rows=2, cols=2, buff=(0.45, 0.45))
        cards.scale(0.78).move_to([0, -0.75, 0])

        arrows = VGroup()
        for card in cards:
            arrows.add(
                Arrow(
                    source_box.get_bottom(),
                    card.get_top(),
                    buff=0.10,
                    stroke_width=1.8,
                    max_tip_length_to_length_ratio=0.10,
                    color=MUTED,
                )
            )

        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.12),
            run_time=0.8,
        )
        self.play(
            LaggedStart(*[FadeIn(card, shift=0.10 * UP) for card in cards], lag_ratio=0.14),
            run_time=1.2,
        )
        self.hold(1.0)

        self.clear_stage(source_group, arrows, cards)

        # 22 — Cierre
        closing = Tex(r"Fin del preview local", color=MUTED).scale(0.82)
        self.play(FadeIn(closing))
        self.hold(0.8)
        self.play(FadeOut(closing))

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def section_title(self, text: str):
        title = Tex(text, color=FG).scale(0.82).to_edge(UP, buff=0.35)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=MUTED, stroke_width=1.2)
        rule.next_to(title, DOWN, buff=0.18)
        self.play(FadeIn(title), Create(rule), run_time=0.45)
        self._current_header = VGroup(title, rule)

    def clear_stage(self, *objects):
        mobs = [m for m in objects if m is not None]
        if hasattr(self, "_current_header") and self._current_header is not None:
            mobs.append(self._current_header)
            self._current_header = None
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=0.45)

    def hold(self, t=0.75):
        self.wait(t)

    # ------------------------------------------------------------------
    # Axiomas aditivos
    # ------------------------------------------------------------------
    def associativity_sum(self):
        source = MathTex(
            r"a", r"+", r"(", r"b", r"+", r"c", r")",
            color=FG,
        ).scale(1.5)
        target = MathTex(
            r"(", r"a", r"+", r"b", r")", r"+", r"c",
            color=FG,
        ).scale(1.5)
        source[0].set_color(BLUE)
        source[3].set_color(ORANGE)
        source[5].set_color(GREEN)
        target[1].set_color(BLUE)
        target[3].set_color(ORANGE)
        target[6].set_color(GREEN)

        self.play(Write(source))
        self.hold(0.25)

        mapping = {
            0: 1,  # a
            1: 2,  # primer +
            2: 0,  # (
            3: 3,  # b
            4: 5,  # segundo +
            5: 6,  # c
            6: 4,  # )
        }
        self.play(
            *[
                source[i].animate.move_to(target[j].get_center())
                for i, j in mapping.items()
            ],
            run_time=1.15,
            rate_func=smooth,
        )
        self.hold(0.35)
        proposition = MathTex(
            r"a+(b+c)=(a+b)+c",
            color=FG,
        ).scale(1.35)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        proposition.set_color_by_tex("c", GREEN)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        self.play(FadeOut(proposition))

    def additive_identity(self):
        expr = MathTex(
            r"a", r"+", r"0", r"=", r"a",
            color=FG,
        ).scale(1.5)
        expr[0].set_color(BLUE)
        expr[2].set_color(MUTED)
        expr[4].set_color(BLUE)

        self.play(FadeIn(expr[0]))
        self.play(FadeIn(expr[1]), FadeIn(expr[2], shift=0.12 * LEFT))
        self.play(FadeIn(expr[3]), FadeIn(expr[4], shift=0.12 * LEFT))
        self.hold(0.5)
        self.play(FadeOut(expr))

    def additive_inverse(self):
        expr = MathTex(
            r"a", r"+", r"(", r"-a", r")", r"=", r"0",
            color=FG,
        ).scale(1.5)
        expr[0].set_color(BLUE)
        expr[3].set_color(ORANGE)
        expr[6].set_color(GREEN)

        # Primero queda visible la estructura completa a + (-a).
        self.play(
            FadeIn(expr[1]),
            FadeIn(expr[2]),
            FadeIn(expr[4]),
        )
        self.play(
            FadeIn(expr[0], shift=0.35 * RIGHT),
            FadeIn(expr[3], shift=0.35 * LEFT),
            run_time=0.75,
        )
        self.hold(0.35)

        # Sólo después aparece el resultado = 0.
        self.play(
            FadeIn(expr[5]),
            FadeIn(expr[6], shift=0.12 * UP),
            run_time=0.55,
        )
        self.hold(0.6)
        self.play(FadeOut(expr))

    def commutativity_sum(self):
        source = MathTex(r"a", r"+", r"b", color=FG).scale(1.6)
        target = MathTex(r"b", r"+", r"a", color=FG).scale(1.6)
        source[0].set_color(BLUE)
        source[2].set_color(ORANGE)
        target[0].set_color(ORANGE)
        target[2].set_color(BLUE)

        self.play(Write(source))
        a_start = source[0].get_center()
        b_start = source[2].get_center()
        a_end = target[2].get_center()
        b_end = target[0].get_center()

        path_a = ArcBetweenPoints(a_start, a_end, angle=-PI / 2)
        path_b = ArcBetweenPoints(b_start, b_end, angle=PI / 2)
        self.play(
            MoveAlongPath(source[0], path_a),
            MoveAlongPath(source[2], path_b),
            source[1].animate.move_to(target[1].get_center()),
            run_time=1.25,
            rate_func=smooth,
        )
        self.hold(0.35)
        proposition = MathTex(r"a+b=b+a", color=FG).scale(1.45)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        self.play(FadeOut(proposition))
        self.clear_stage()

    # ------------------------------------------------------------------
    # Axiomas multiplicativos
    # ------------------------------------------------------------------
    def associativity_product(self):
        source = MathTex(
            r"a", r"\cdot", r"(", r"b", r"\cdot", r"c", r")",
            color=FG,
        ).scale(1.5)
        target = MathTex(
            r"(", r"a", r"\cdot", r"b", r")", r"\cdot", r"c",
            color=FG,
        ).scale(1.5)
        source[0].set_color(BLUE)
        source[3].set_color(ORANGE)
        source[5].set_color(GREEN)
        target[1].set_color(BLUE)
        target[3].set_color(ORANGE)
        target[6].set_color(GREEN)

        self.play(Write(source))
        self.hold(0.25)

        mapping = {
            0: 1,  # a
            1: 2,  # primer punto
            2: 0,  # (
            3: 3,  # b
            4: 5,  # segundo punto
            5: 6,  # c
            6: 4,  # )
        }
        self.play(
            *[
                source[i].animate.move_to(target[j].get_center())
                for i, j in mapping.items()
            ],
            run_time=1.15,
            rate_func=smooth,
        )
        self.hold(0.35)
        proposition = MathTex(
            r"a\cdot(b\cdot c)=(a\cdot b)\cdot c",
            color=FG,
        ).scale(1.28)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        proposition.set_color_by_tex("c", GREEN)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        self.play(FadeOut(proposition))

    def multiplicative_identity(self):
        expr = MathTex(
            r"a", r"\cdot", r"1", r"=", r"a",
            color=FG,
        ).scale(1.5)
        expr[0].set_color(BLUE)
        expr[2].set_color(MUTED)
        expr[4].set_color(BLUE)

        self.play(FadeIn(expr[0]))
        self.play(FadeIn(expr[1]), FadeIn(expr[2], shift=0.12 * LEFT))
        self.play(FadeIn(expr[3]), FadeIn(expr[4], shift=0.12 * LEFT))
        self.hold(0.5)
        self.play(FadeOut(expr))

    def multiplicative_inverse(self):
        hypothesis = MathTex(r"a\neq0", color=ORANGE).scale(1.05).to_edge(UP, buff=1.55)
        expr = MathTex(
            r"a", r"\cdot", r"a^{-1}", r"=", r"1",
            color=FG,
        ).scale(1.5)
        expr[0].set_color(BLUE)
        expr[2].set_color(GREEN)
        expr[4].set_color(GREEN)

        self.play(FadeIn(hypothesis))
        self.play(FadeIn(expr[1]))
        self.play(
            FadeIn(expr[0], shift=0.35 * RIGHT),
            FadeIn(expr[2], shift=0.35 * LEFT),
            run_time=0.75,
        )
        self.hold(0.3)
        self.play(FadeIn(expr[3]), FadeIn(expr[4], shift=0.12 * UP))
        self.hold(0.5)
        self.play(FadeOut(hypothesis), FadeOut(expr))

    def commutativity_product(self):
        source = MathTex(r"a", r"\cdot", r"b", color=FG).scale(1.6)
        target = MathTex(r"b", r"\cdot", r"a", color=FG).scale(1.6)
        source[0].set_color(BLUE)
        source[2].set_color(ORANGE)
        target[0].set_color(ORANGE)
        target[2].set_color(BLUE)

        self.play(Write(source))
        a_start = source[0].get_center()
        b_start = source[2].get_center()
        a_end = target[2].get_center()
        b_end = target[0].get_center()

        path_a = ArcBetweenPoints(a_start, a_end, angle=-PI / 2)
        path_b = ArcBetweenPoints(b_start, b_end, angle=PI / 2)
        self.play(
            MoveAlongPath(source[0], path_a),
            MoveAlongPath(source[2], path_b),
            source[1].animate.move_to(target[1].get_center()),
            run_time=1.20,
            rate_func=smooth,
        )
        self.hold(0.35)
        proposition = MathTex(r"a\cdot b=b\cdot a", color=FG).scale(1.4)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        self.play(FadeOut(proposition))
        self.clear_stage()

    # ------------------------------------------------------------------
    # Distributividad
    # ------------------------------------------------------------------
    def distributivity_demo(self):
        source = MathTex(
            r"a", r"\cdot", r"(", r"b", r"+", r"c", r")",
            color=FG,
        ).scale(1.5)
        target = MathTex(
            r"a", r"\cdot", r"b", r"+", r"a", r"\cdot", r"c",
            color=FG,
        ).scale(1.5)

        source[0].set_color(BLUE)
        source[3].set_color(ORANGE)
        source[5].set_color(GREEN)
        target[0].set_color(BLUE)
        target[2].set_color(ORANGE)
        target[4].set_color(BLUE)
        target[6].set_color(GREEN)

        self.play(Write(source))
        self.hold(0.3)

        initial_positions = [part.get_center().copy() for part in source]

        # Duplicamos explícitamente el factor a y su signo de multiplicación.
        a_copy = source[0].copy()
        dot_copy = source[1].copy()
        self.add(a_copy, dot_copy)

        self.play(
            source[0].animate.move_to(target[0].get_center()),
            source[1].animate.move_to(target[1].get_center()),
            source[3].animate.move_to(target[2].get_center()),
            source[4].animate.move_to(target[3].get_center()),
            a_copy.animate.move_to(target[4].get_center()),
            dot_copy.animate.move_to(target[5].get_center()),
            source[5].animate.move_to(target[6].get_center()),
            FadeOut(source[2]),
            FadeOut(source[6]),
            run_time=1.15,
            rate_func=smooth,
        )
        self.hold(0.35)

        proposition = MathTex(
            r"a\cdot(b+c)=a\cdot b+a\cdot c",
            color=FG,
        ).scale(1.28)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        proposition.set_color_by_tex("c", GREEN)
        moving_state = VGroup(
            source[0], source[1], source[3], source[4], source[5],
            a_copy, dot_copy,
        )
        self.play(FadeOut(moving_state), FadeIn(proposition))
        self.hold(0.65)
        self.play(FadeOut(proposition), FadeIn(moving_state))

        # Factorización inversa: las dos copias de a se reúnen en la posición original.
        self.play(
            source[0].animate.move_to(initial_positions[0]),
            a_copy.animate.move_to(initial_positions[0]),
            source[1].animate.move_to(initial_positions[1]),
            dot_copy.animate.move_to(initial_positions[1]),
            source[3].animate.move_to(initial_positions[3]),
            source[4].animate.move_to(initial_positions[4]),
            source[5].animate.move_to(initial_positions[5]),
            FadeIn(source[2]),
            FadeIn(source[6]),
            run_time=1.0,
            rate_func=smooth,
        )
        self.play(FadeOut(a_copy), FadeOut(dot_copy), run_time=0.25)
        self.hold(0.3)
        proposition_back = MathTex(
            r"a\cdot b+a\cdot c=a\cdot(b+c)",
            color=FG,
        ).scale(1.28)
        proposition_back.set_color_by_tex("a", BLUE)
        proposition_back.set_color_by_tex("b", ORANGE)
        proposition_back.set_color_by_tex("c", GREEN)
        self.play(FadeOut(source), FadeIn(proposition_back))
        self.hold(0.55)
        self.play(FadeOut(proposition_back))
        self.clear_stage()

    def theorem_card(self, title_text, formula, color):
        box = RoundedRectangle(
            width=4.6, height=1.35, corner_radius=0.14,
            color=color, stroke_width=1.8,
        )
        title = Tex(title_text, color=color).scale(0.56)
        math = MathTex(formula, color=FG).scale(0.58)
        title.move_to(box.get_center() + 0.28 * UP)
        math.move_to(box.get_center() + 0.25 * DOWN)
        return VGroup(box, title, math)

    # ------------------------------------------------------------------
    # Tabla de síntesis
    # ------------------------------------------------------------------
    def axiom_summary(self):
        condition = VGroup(
            Tex(r"Condición estructural", color=MUTED).scale(0.68),
            MathTex(r"0\neq1", color=GREEN).scale(1.05),
        ).arrange(RIGHT, buff=0.38).move_to([0, 2.15, 0])

        labels = [
            ("1", "Asociatividad de la suma", r"a+(b+c)=(a+b)+c"),
            ("2", "Neutro aditivo", r"a+0=a"),
            ("3", "Inverso aditivo", r"a+(-a)=0"),
            ("4", "Conmutatividad de la suma", r"a+b=b+a"),
            ("5", "Asociatividad del producto", r"a\cdot(b\cdot c)=(a\cdot b)\cdot c"),
            ("6", "Neutro multiplicativo", r"a\cdot1=a"),
            ("7", "Inverso multiplicativo", r"a\cdot a^{-1}=1\quad(a\neq0)"),
            ("8", "Conmutatividad del producto", r"a\cdot b=b\cdot a"),
            ("9", "Distributividad", r"a\cdot(b+c)=a\cdot b+a\cdot c"),
        ]

        rows = VGroup()
        first_y = 1.32
        row_step = 0.47

        for i, (n, name, formula) in enumerate(labels):
            y = first_y - i * row_step

            n_obj = MathTex(n, color=MUTED).scale(0.64)
            name_obj = Tex(name, color=FG).scale(0.58)
            formula_obj = MathTex(formula, color=FG).scale(0.62)

            n_obj.move_to([-5.45, y, 0])
            name_obj.move_to([-2.75, y, 0])
            formula_obj.move_to([2.25, y, 0])

            rows.add(VGroup(n_obj, name_obj, formula_obj))

        self.play(FadeIn(condition))
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=0.06 * RIGHT) for row in rows],
                lag_ratio=0.07,
            ),
            run_time=2.0,
        )
        self.hold(1.0)
        self.play(FadeOut(condition), FadeOut(rows), run_time=0.55)
        self.clear_stage()

    # ------------------------------------------------------------------
    # Cuerpo finito F_2
    # ------------------------------------------------------------------
    def f2_demo(self):
        f2 = MathTex(r"F_2=\{0,1\}", color=FG).scale(1.2).to_edge(UP, buff=1.45)
        add_table = MathTable(
            [["0", "1"], ["1", "0"]],
            row_labels=[MathTex("0"), MathTex("1")],
            col_labels=[MathTex("0"), MathTex("1")],
            top_left_entry=MathTex("+"),
            include_outer_lines=True,
            line_config={"stroke_width": 1.2, "color": MUTED},
            element_to_mobject_config={"color": FG},
        ).scale(0.72).shift(3.0 * LEFT + 0.35 * DOWN)
        mul_table = MathTable(
            [["0", "0"], ["0", "1"]],
            row_labels=[MathTex("0"), MathTex("1")],
            col_labels=[MathTex("0"), MathTex("1")],
            top_left_entry=MathTex(r"\cdot"),
            include_outer_lines=True,
            line_config={"stroke_width": 1.2, "color": MUTED},
            element_to_mobject_config={"color": FG},
        ).scale(0.72).shift(3.0 * RIGHT + 0.35 * DOWN)

        self.play(FadeIn(f2))
        self.play(Create(add_table), Create(mul_table), run_time=1.5)

        add_highlight = SurroundingRectangle(add_table.get_entries((2, 2)), color=ORANGE, buff=0.10)
        sum_result = MathTex(r"1+1=0", color=ORANGE).scale(1.05).to_edge(DOWN, buff=0.75)
        self.play(Create(add_highlight), FadeIn(sum_result))
        self.hold(0.75)
        self.play(FadeOut(add_highlight), FadeOut(sum_result))

        mul_highlight = SurroundingRectangle(mul_table.get_entries((2, 2)), color=GREEN, buff=0.10)
        mul_result = MathTex(r"1\cdot1=1", r"\qquad", r"1^{-1}=1", color=GREEN).scale(0.98).to_edge(DOWN, buff=0.75)
        self.play(Create(mul_highlight), FadeIn(mul_result))
        self.hold(0.75)
        self.play(FadeOut(mul_highlight), FadeOut(mul_result))

        self.play(FadeOut(f2), FadeOut(add_table), FadeOut(mul_table), run_time=0.55)
        self.clear_stage()
