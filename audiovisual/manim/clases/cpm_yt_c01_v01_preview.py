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
            r"2+3=5", r"\qquad", r"2\cdot3=6", r"\qquad", r"2x=1\Longrightarrow x=\frac12",
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

        expr = MathTex(r"3-5", color=FG).scale(1.5).to_edge(DOWN, buff=1.25)
        self.play(FadeIn(expr))
        marker = SurroundingRectangle(chain[0], color=BLUE, buff=0.12)
        self.play(Create(marker))
        self.play(marker.animate.move_to(chain[2]), expr.animate.set_color(ORANGE))
        self.hold(0.5)
        self.play(FadeOut(expr), FadeOut(marker))

        eq = MathTex(r"2x=1", color=FG).scale(1.35).to_edge(DOWN, buff=1.25)
        half = MathTex(r"x=\frac12", color=GREEN).scale(1.35).move_to(eq)
        marker2 = SurroundingRectangle(chain[2], color=ORANGE, buff=0.12)
        self.play(FadeIn(eq), Create(marker2))
        self.play(TransformMatchingTex(eq, half), marker2.animate.move_to(chain[4]))
        self.hold(0.6)
        self.clear_stage(chain, half, marker2)

        # 03 — Spoiler tenue
        spoiler = Tex(r"Spoiler: supremo", color=MUTED).scale(0.78)
        self.play(FadeIn(spoiler, run_time=0.8))
        self.hold(0.5)
        self.play(FadeOut(spoiler, run_time=0.8))

        # 04 — Conjunto y clausura
        self.section_title("Operaciones internas")
        f_nonempty = MathTex(r"F\neq\varnothing", color=FG).scale(1.35)
        closure = MathTex(
            r"a,b\in F", r"\Longrightarrow", r"a+b\in F", r",\qquad", r"ab\in F",
            color=FG,
        ).scale(1.05).next_to(f_nonempty, DOWN, buff=0.65)
        closure[2].set_color(BLUE)
        closure[4].set_color(ORANGE)
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
        lhs = MathTex(r"a(b+c)", color=FG).scale(1.45)
        rhs = MathTex(r"ab+ac", color=FG).scale(1.45)
        lhs[0][0].set_color(GREEN)
        self.play(Write(lhs))
        self.play(TransformMatchingTex(lhs, rhs))
        self.hold(0.6)
        factor = MathTex(r"a(b+c)", color=FG).scale(1.45)
        self.play(TransformMatchingTex(rhs, factor))
        self.hold(0.5)
        self.clear_stage(factor)

        # 15 — Cuerpo trivial
        self.section_title("Cuerpo trivial")
        trivial = MathTex(r"F=\{0\}", r",\qquad", r"1=0", color=FG).scale(1.25)
        trivial[2].set_color(RED)
        ops_trivial = MathTex(r"0+0=0", r",\qquad", r"0\cdot0=0", color=FG).scale(1.1)
        ops_trivial.next_to(trivial, DOWN, buff=0.65)
        exclusion = MathTex(r"0\neq1", color=GREEN).scale(1.45).next_to(ops_trivial, DOWN, buff=0.65)
        self.play(Write(trivial))
        self.play(LaggedStart(Write(ops_trivial[0]), Write(ops_trivial[2]), lag_ratio=0.45))
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
            MathTex(r"(-a)(-b)=ab", color=FG),
            MathTex(r"ab=0\Longrightarrow a=0\ \text{o}\ b=0", color=FG),
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
        eq2 = MathTex(r"2x=1", color=FG).scale(1.25).to_edge(DOWN, buff=1.2)
        half2 = MathTex(r"x=\frac12", color=GREEN).scale(1.25).move_to(eq2)
        half_floating = MathTex(r"\frac12", color=GREEN).scale(1.6).move_to(integers)
        self.play(Create(circle), FadeIn(integers))
        self.play(Write(eq2))
        self.play(TransformMatchingTex(eq2, half2))
        self.play(FadeIn(half_floating))
        self.play(half_floating.animate.shift(3.0 * RIGHT), circle.animate.set_color(RED), integers.animate.set_color(RED))
        self.hold(0.7)
        self.clear_stage(circle, integers, half2, half_floating)

        # 20 — Q y R sí
        self.section_title("Dos cuerpos familiares")
        qr = MathTex(r"\mathbb Q", r"\qquad", r"\mathbb R", color=FG).scale(1.8)
        qr[0].set_color(GREEN)
        qr[2].set_color(VIOLET)
        self.play(FadeIn(qr, scale=0.92))
        self.hold(0.8)
        self.clear_stage(qr)

        # 21 — Capa algebraica / capa de orden
        self.section_title("Siguiente capa: orden")
        algebra = Tex(r"Capa algebraica", color=BLUE).scale(0.95)
        order = Tex(r"Capa de orden", color=GREEN).scale(0.95)
        layers = VGroup(algebra, order).arrange(DOWN, buff=0.75)
        relation = MathTex(r"2<3", color=FG).scale(1.55).next_to(order, DOWN, buff=0.7)
        self.play(FadeIn(algebra, shift=0.15 * RIGHT))
        self.play(FadeIn(order, shift=0.15 * RIGHT))
        self.play(Write(relation))
        self.hold(0.8)
        self.clear_stage(layers, relation)

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
        a = MathTex(r"a+(b+c)", color=FG).scale(1.5)
        b = MathTex(r"(a+b)+c", color=FG).scale(1.5)
        self.play(Write(a))
        self.play(TransformMatchingTex(a, b))
        self.hold(0.45)
        self.play(FadeOut(b))

    def additive_identity(self):
        a = MathTex(r"a", color=BLUE).scale(1.55)
        zero = MathTex(r"+0", color=MUTED).scale(1.55).next_to(a, RIGHT, buff=0.12)
        result = MathTex(r"a+0=a", color=FG).scale(1.45)
        self.play(FadeIn(a))
        self.play(FadeIn(zero, shift=0.18 * LEFT))
        pair = VGroup(a, zero)
        self.play(ReplacementTransform(pair, result))
        self.hold(0.45)
        self.play(FadeOut(result))

    def additive_inverse(self):
        left = MathTex(r"a", color=BLUE).scale(1.55).shift(1.35 * LEFT)
        right = MathTex(r"-a", color=ORANGE).scale(1.55).shift(1.35 * RIGHT)
        zero = MathTex(r"0", color=GREEN).scale(1.65)
        self.play(FadeIn(left), FadeIn(right))
        self.play(left.animate.shift(0.75 * RIGHT), right.animate.shift(0.75 * LEFT))
        self.play(ReplacementTransform(VGroup(left, right), zero))
        self.hold(0.45)
        self.play(FadeOut(zero))

    def commutativity_sum(self):
        start = MathTex(r"a+b", color=FG).scale(1.5)
        end = MathTex(r"b+a", color=FG).scale(1.5)
        start[0][0].set_color(BLUE)
        start[0][2].set_color(ORANGE)
        end[0][0].set_color(ORANGE)
        end[0][2].set_color(BLUE)
        self.play(Write(start))
        self.play(TransformMatchingTex(start, end))
        self.hold(0.45)
        self.play(FadeOut(end))
        self.clear_stage()

    # ------------------------------------------------------------------
    # Axiomas multiplicativos
    # ------------------------------------------------------------------
    def associativity_product(self):
        a = MathTex(r"a(bc)", color=FG).scale(1.5)
        b = MathTex(r"(ab)c", color=FG).scale(1.5)
        self.play(Write(a))
        self.play(TransformMatchingTex(a, b))
        self.hold(0.45)
        self.play(FadeOut(b))

    def multiplicative_identity(self):
        a = MathTex(r"a", color=BLUE).scale(1.55)
        one = MathTex(r"\cdot1", color=MUTED).scale(1.55).next_to(a, RIGHT, buff=0.12)
        result = MathTex(r"a\cdot1=a", color=FG).scale(1.45)
        self.play(FadeIn(a))
        self.play(FadeIn(one, shift=0.18 * LEFT))
        self.play(ReplacementTransform(VGroup(a, one), result))
        self.hold(0.45)
        self.play(FadeOut(result))

    def multiplicative_inverse(self):
        hypothesis = MathTex(r"a\neq0", color=ORANGE).scale(1.05).to_edge(UP, buff=1.55)
        left = MathTex(r"a", color=BLUE).scale(1.55).shift(1.45 * LEFT)
        right = MathTex(r"a^{-1}", color=GREEN).scale(1.55).shift(1.45 * RIGHT)
        one = MathTex(r"1", color=GREEN).scale(1.65)
        self.play(FadeIn(hypothesis))
        self.play(FadeIn(left), FadeIn(right))
        self.play(left.animate.shift(0.78 * RIGHT), right.animate.shift(0.78 * LEFT))
        self.play(ReplacementTransform(VGroup(left, right), one))
        self.hold(0.45)
        self.play(FadeOut(hypothesis), FadeOut(one))

    def commutativity_product(self):
        start = MathTex(r"ab", color=FG).scale(1.5)
        end = MathTex(r"ba", color=FG).scale(1.5)
        start[0][0].set_color(BLUE)
        start[0][1].set_color(ORANGE)
        end[0][0].set_color(ORANGE)
        end[0][1].set_color(BLUE)
        self.play(Write(start))
        self.play(TransformMatchingTex(start, end))
        self.hold(0.45)
        self.play(FadeOut(end))
        self.clear_stage()

    # ------------------------------------------------------------------
    # Tabla de síntesis
    # ------------------------------------------------------------------
    def axiom_summary(self):
        condition = VGroup(
            Tex(r"Condición estructural", color=MUTED).scale(0.55),
            MathTex(r"0\neq1", color=GREEN).scale(0.9),
        ).arrange(RIGHT, buff=0.35).to_edge(UP, buff=1.35)

        labels = [
            ("1", "Asociatividad de la suma", r"a+(b+c)=(a+b)+c"),
            ("2", "Neutro aditivo", r"a+0=a"),
            ("3", "Inverso aditivo", r"a+(-a)=0"),
            ("4", "Conmutatividad de la suma", r"a+b=b+a"),
            ("5", "Asociatividad del producto", r"a(bc)=(ab)c"),
            ("6", "Neutro multiplicativo", r"a\cdot1=a"),
            ("7", "Inverso multiplicativo", r"aa^{-1}=1\quad(a\neq0)"),
            ("8", "Conmutatividad del producto", r"ab=ba"),
            ("9", "Distributividad", r"a(b+c)=ab+ac"),
        ]
        rows = VGroup()
        for n, name, formula in labels:
            n_obj = MathTex(n, color=MUTED).scale(0.52)
            name_obj = Tex(name, color=FG).scale(0.46)
            formula_obj = MathTex(formula, color=FG).scale(0.50)
            row = VGroup(n_obj, name_obj, formula_obj)
            n_obj.set_x(-5.35)
            name_obj.set_x(-2.95)
            formula_obj.set_x(2.35)
            rows.add(row)
        rows.arrange(DOWN, buff=0.17, center=False, aligned_edge=LEFT).shift(0.35 * DOWN)

        self.play(FadeIn(condition))
        self.play(LaggedStart(*[FadeIn(row, shift=0.08 * RIGHT) for row in rows], lag_ratio=0.08), run_time=2.1)
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
        mul_result = MathTex(r"1\cdot1=1", r",\qquad", r"1^{-1}=1", color=GREEN).scale(0.98).to_edge(DOWN, buff=0.75)
        self.play(Create(mul_highlight), FadeIn(mul_result))
        self.hold(0.75)
        self.play(FadeOut(mul_highlight), FadeOut(mul_result))

        self.play(FadeOut(f2), FadeOut(add_table), FadeOut(mul_table), run_time=0.55)
        self.clear_stage()
