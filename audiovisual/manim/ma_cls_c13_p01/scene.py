from manim import *

# Matemática Abierta — prototipo audiovisual, versión oscura v2.
# Capítulo visible 13 / fuente interna T1-C14.

MA_BG = "#0F1117"
MA_PANEL = "#161A23"
MA_PANEL_EDGE = "#2A3340"
MA_TEXT = "#E8EDF2"
MA_MUTED = "#A9B4BF"
MA_BLUE = "#4DA3D9"
MA_ORANGE = "#F29D62"
MA_GREEN = "#58C4A3"

config.background_color = MA_BG

MA_TEX = TexTemplate(tex_compiler="xelatex", output_format=".xdv")


def MAMathTex(*tex_strings, **kwargs):
    kwargs.setdefault("tex_template", MA_TEX)
    return MathTex(*tex_strings, **kwargs)


def f(x: float) -> float:
    return x * x


def make_axes():
    axes = Axes(
        x_range=[0, 1.05, 0.25],
        y_range=[0, 1.15, 0.25],
        x_length=7.0,
        y_length=4.6,
        axis_config={"color": MA_MUTED, "stroke_width": 2},
        tips=False,
    ).shift(LEFT * 2.25 + DOWN * 0.45)

    labels = axes.get_axis_labels(
        x_label=MAMathTex("x", color=MA_TEXT, font_size=30),
        y_label=MAMathTex("y", color=MA_TEXT, font_size=30),
    )
    curve = axes.plot(f, x_range=[0, 1], color=MA_TEXT, stroke_width=4)
    curve_label = MAMathTex("f(x)=x^2", color=MA_TEXT, font_size=32)
    curve_label.next_to(axes.c2p(0.67, 0.77), LEFT, buff=0.12)
    return axes, labels, curve, curve_label


def make_header(title: str, subtitle: str):
    title_mob = Text(
        title,
        font_size=34,
        color=MA_TEXT,
        weight=BOLD,
    ).to_corner(UL, buff=0.34)

    subtitle_mob = Text(
        subtitle,
        font_size=20,
        color=MA_MUTED,
    ).next_to(title_mob, DOWN, aligned_edge=LEFT, buff=0.10)

    return VGroup(title_mob, subtitle_mob)


def make_panel():
    return RoundedRectangle(
        width=4.55,
        height=4.95,
        corner_radius=0.18,
        stroke_color=MA_PANEL_EDGE,
        stroke_width=1.4,
        fill_color=MA_PANEL,
        fill_opacity=1,
    ).to_edge(RIGHT, buff=0.38).shift(DOWN * 0.34)


def panel_paragraph(*lines, font_size=17, color=MA_MUTED):
    """Texto auxiliar centrado y contenido dentro del panel lateral."""
    return Paragraph(
        *lines,
        alignment="center",
        font_size=font_size,
        color=color,
        line_spacing=0.85,
    )


def graph_rect(axes: Axes, a: float, b: float, h: float, color: str, opacity: float):
    return Polygon(
        axes.c2p(a, 0),
        axes.c2p(b, 0),
        axes.c2p(b, h),
        axes.c2p(a, h),
        stroke_color=color,
        stroke_width=1.15,
        fill_color=color,
        fill_opacity=opacity,
    )


def bound_rectangles(axes: Axes, n: int):
    dx = 1 / n
    lower = VGroup()
    upper = VGroup()

    for k in range(n):
        a = k * dx
        b = (k + 1) * dx
        h_low = f(a)
        h_up = f(b)

        upper.add(graph_rect(axes, a, b, h_up, MA_ORANGE, 0.14))
        if h_low > 0:
            lower.add(graph_rect(axes, a, b, h_low, MA_BLUE, 0.28))

    return lower, upper


def tagged_rectangles(axes: Axes, n: int):
    dx = 1 / n
    rects = VGroup()
    xis = []

    for k in range(n):
        a = k * dx
        b = (k + 1) * dx
        xi = (a + b) / 2
        xis.append(xi)
        rects.add(graph_rect(axes, a, b, f(xi), MA_BLUE, 0.20))

    return rects, xis


class MAVizC13RiemannRefinement(Scene):
    """MA-VIZ-C13-002 v2 — Encierro y refinamiento, sin residuos conceptuales."""

    def construct(self):
        self.camera.background_color = MA_BG

        header = make_header(
            "Del área a las sumas",
            "refinar la partición estrecha el encierro",
        )
        axes, labels, curve, curve_label = make_axes()
        panel = make_panel()

        self.play(FadeIn(header), FadeIn(panel), run_time=0.8)
        self.play(
            Create(axes),
            FadeIn(labels),
            Create(curve),
            FadeIn(curve_label),
            run_time=1.3,
        )

        lower_dot = Dot(radius=0.07, color=MA_BLUE)
        upper_dot = Dot(radius=0.07, color=MA_ORANGE)
        lower_text = Text("suma inferior", font_size=21, color=MA_BLUE)
        upper_text = Text("suma superior", font_size=21, color=MA_ORANGE)
        lower_row = VGroup(lower_dot, lower_text).arrange(RIGHT, buff=0.16)
        upper_row = VGroup(upper_dot, upper_text).arrange(RIGHT, buff=0.16)
        legend = VGroup(lower_row, upper_row).arrange(
            DOWN, aligned_edge=LEFT, buff=0.16
        )
        legend.move_to(panel.get_top() + DOWN * 0.65).align_to(panel, LEFT).shift(RIGHT * 0.42)

        lower_rects, upper_rects = bound_rectangles(axes, 4)
        inequality = MAMathTex(
            r"L(f,P)\le A\le U(f,P)",
            color=MA_TEXT,
            font_size=37,
        ).move_to(panel.get_center() + DOWN * 0.10)

        motivation = Text(
            "dos sumas finitas encierran el problema",
            font_size=18,
            color=MA_MUTED,
        ).next_to(inequality, DOWN, buff=0.34)

        self.play(
            FadeIn(legend),
            FadeIn(upper_rects),
            FadeIn(lower_rects),
            run_time=1.0,
        )
        self.bring_to_front(curve)
        self.play(Write(inequality), FadeIn(motivation), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(inequality), FadeOut(motivation), run_time=0.45)

        gap_formula = MAMathTex(
            r"U_n-L_n=\frac{1}{n}",
            color=MA_GREEN,
            font_size=40,
        ).move_to(panel.get_center() + UP * 0.05)

        exact_note = panel_paragraph(
            "brecha exacta para estas",
            "particiones uniformes",
            font_size=16,
        ).next_to(gap_formula, DOWN, buff=0.30)
        exact_note.set_x(panel.get_center()[0])

        n_label = MAMathTex(
            r"n=4",
            color=MA_TEXT,
            font_size=34,
        ).next_to(gap_formula, UP, buff=0.48)

        self.play(FadeIn(n_label), Write(gap_formula), FadeIn(exact_note), run_time=0.8)
        self.wait(0.65)

        for n in (8, 16, 32):
            new_lower, new_upper = bound_rectangles(axes, n)
            new_n = MAMathTex(
                rf"n={n}",
                color=MA_TEXT,
                font_size=34,
            ).move_to(n_label)

            # Fase cerrada antes de introducir la siguiente: no quedan residuos.
            self.play(
                FadeOut(lower_rects),
                FadeOut(upper_rects),
                FadeOut(n_label),
                run_time=0.24,
            )
            self.play(
                FadeIn(new_upper),
                FadeIn(new_lower),
                FadeIn(new_n),
                run_time=0.48,
            )
            self.bring_to_front(curve)

            lower_rects, upper_rects, n_label = new_lower, new_upper, new_n
            self.wait(0.55)

        self.play(
            FadeOut(n_label),
            FadeOut(gap_formula),
            FadeOut(exact_note),
            run_time=0.45,
        )

        limit_formula = MAMathTex(
            r"U_n-L_n\longrightarrow 0",
            color=MA_GREEN,
            font_size=44,
        ).move_to(panel.get_center() + UP * 0.18)

        conclusion = panel_paragraph(
            "la incertidumbre entre las cotas",
            "puede hacerse arbitrariamente pequeña",
            font_size=18,
            color=MA_TEXT,
        ).next_to(limit_formula, DOWN, buff=0.36)
        conclusion.set_x(panel.get_center()[0])

        self.play(Write(limit_formula), FadeIn(conclusion), run_time=0.9)
        self.wait(1.5)


class MAVizC13RiemannTermToSum(Scene):
    """MA-VIZ-C13-003 — De una franja a la estructura de una suma de Riemann."""

    def construct(self):
        self.camera.background_color = MA_BG

        header = make_header(
            "De una franja a una suma",
            "la fórmula emerge de la construcción geométrica",
        )
        axes, labels, curve, curve_label = make_axes()
        panel = make_panel()

        self.play(FadeIn(header), FadeIn(panel), run_time=0.8)
        self.play(
            Create(axes),
            FadeIn(labels),
            Create(curve),
            FadeIn(curve_label),
            run_time=1.3,
        )

        n = 8
        rects, xis = tagged_rectangles(axes, n)
        dx = 1 / n

        panel_title = Text(
            "una partición etiquetada",
            font_size=21,
            color=MA_MUTED,
        ).move_to(panel.get_top() + DOWN * 0.55)

        self.play(FadeIn(panel_title), FadeIn(rects), run_time=0.9)
        self.bring_to_front(curve)
        self.wait(0.65)

        idx = 5
        a = idx * dx
        b = (idx + 1) * dx
        xi = xis[idx]

        highlight = graph_rect(axes, a, b, f(xi), MA_GREEN, 0.42)
        height_line = DashedLine(
            axes.c2p(xi, 0),
            axes.c2p(xi, f(xi)),
            color=MA_GREEN,
            stroke_width=2.6,
            dash_length=0.09,
        )
        width_brace = BraceBetweenPoints(
            axes.c2p(a, 0),
            axes.c2p(b, 0),
            direction=DOWN,
            color=MA_GREEN,
        )

        width_label = MAMathTex(
            r"\Delta x_i",
            color=MA_GREEN,
            font_size=28,
        ).next_to(width_brace, DOWN, buff=0.08)

        height_label = MAMathTex(
            r"f(\xi_i)",
            color=MA_GREEN,
            font_size=28,
        ).next_to(height_line, RIGHT, buff=0.10)

        self.play(
            FadeIn(highlight),
            Create(height_line),
            GrowFromCenter(width_brace),
            FadeIn(width_label),
            FadeIn(height_label),
            run_time=0.95,
        )
        self.wait(0.65)

        dimensions = VGroup(
            Text("altura", font_size=18, color=MA_MUTED),
            MAMathTex(r"f(\xi_i)", color=MA_GREEN, font_size=34),
            Text("anchura", font_size=18, color=MA_MUTED),
            MAMathTex(r"\Delta x_i", color=MA_GREEN, font_size=34),
        ).arrange(DOWN, buff=0.13)
        dimensions.move_to(panel.get_center() + UP * 0.10)

        self.play(FadeIn(dimensions), run_time=0.65)
        self.wait(0.65)

        product = VGroup(
            Text("contribución de esta franja", font_size=18, color=MA_MUTED),
            MAMathTex(
                r"f(\xi_i)\,\Delta x_i",
                color=MA_GREEN,
                font_size=40,
            ),
        ).arrange(DOWN, buff=0.20)
        product.move_to(dimensions)

        self.play(FadeOut(dimensions), FadeIn(product), run_time=0.65)
        self.wait(0.8)

        sum_block = VGroup(
            Text("todas las franjas", font_size=18, color=MA_MUTED),
            MAMathTex(
                r"\sum_{i=1}^{n} f(\xi_i)\,\Delta x_i",
                color=MA_TEXT,
                font_size=41,
            ),
            Text(
                "suma de Riemann",
                font_size=20,
                color=MA_BLUE,
            ),
        ).arrange(DOWN, buff=0.22)
        sum_block.move_to(panel.get_center())

        self.play(
            FadeOut(product),
            FadeOut(highlight),
            FadeOut(height_line),
            FadeOut(width_brace),
            FadeOut(width_label),
            FadeOut(height_label),
            FadeIn(sum_block),
            run_time=0.85,
        )
        self.wait(0.75)

        caution = panel_paragraph(
            "todavía no es la definición general",
            "de integral",
            font_size=16,
        ).next_to(sum_block, DOWN, buff=0.36)
        caution.set_x(panel.get_center()[0])

        self.play(FadeIn(caution), run_time=0.55)
        self.wait(1.3)
