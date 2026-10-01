from manim import *

# Matemática Abierta — prototipo audiovisual
# Capítulo visible 13 / fuente interna T1-C14.

MA_BLUE = "#176b91"
MA_ORANGE = "#b95418"
MA_GREEN = "#287c66"
MA_INK = "#243746"
MA_MUTED = "#6f7f89"

config.background_color = WHITE


def f(x: float) -> float:
    return x * x


class MAVizC13RiemannRefinement(Scene):
    """MA-VIZ-C13-002 — Refinamiento de sumas rectangulares.

    La escena respeta el alcance de T1-C14: motiva el mecanismo de encierro
    y refinamiento sin presentar todavía una definición general de integral
    de Riemann.
    """

    def construct(self):
        self.camera.background_color = WHITE

        title = Text(
            "Del área a las sumas",
            font_size=42,
            color=MA_INK,
            weight=BOLD,
        ).to_edge(UP, buff=0.35)

        subtitle = Text(
            "refinar la partición estrecha el encierro",
            font_size=24,
            color=MA_MUTED,
        ).next_to(title, DOWN, buff=0.12)

        axes = Axes(
            x_range=[0, 1.05, 0.25],
            y_range=[0, 1.15, 0.25],
            x_length=7.2,
            y_length=4.2,
            axis_config={"color": MA_INK, "stroke_width": 2},
            tips=False,
        ).shift(LEFT * 1.7 + DOWN * 0.35)

        labels = axes.get_axis_labels(
            x_label=MathTex("x", tex_template=MA_TEX, color=MA_INK),
            y_label=MathTex("y", tex_template=MA_TEX, color=MA_INK),
        )
        curve = axes.plot(f, x_range=[0, 1], color=MA_INK, stroke_width=4)
        curve_label = MathTex("f(x)=x^2", tex_template=MA_TEX, color=MA_INK, font_size=34)
        curve_label.next_to(axes.c2p(0.72, 0.78), LEFT, buff=0.08)

        self.play(FadeIn(title), FadeIn(subtitle), run_time=1.0)
        self.play(
            Create(axes),
            FadeIn(labels),
            Create(curve),
            FadeIn(curve_label),
            run_time=1.8,
        )

        lower_label = Text("suma inferior", font_size=24, color=MA_BLUE)
        upper_label = Text("suma superior", font_size=24, color=MA_ORANGE)
        lower_label.to_corner(UR).shift(DOWN * 1.35 + LEFT * 0.25)
        upper_label.next_to(lower_label, DOWN, buff=0.16).align_to(lower_label, LEFT)

        formula = MathTex(
            r"L(f,P)\;\le\; A\;\le\; U(f,P)",
            color=MA_INK,
            font_size=38,
        ).to_corner(DR).shift(UP * 0.4 + LEFT * 0.2)

        self.play(FadeIn(lower_label), FadeIn(upper_label), FadeIn(formula))
        self.wait(0.6)

        lower_rects = None
        upper_rects = None
        n_label = None
        gap_label = None

        for step, n in enumerate([4, 8, 16, 32]):
            new_lower, new_upper = self._bounds_rectangles(axes, n)
            new_n = MathTex(rf"n={n}", color=MA_INK, font_size=34)
            new_n.next_to(axes, DOWN, buff=0.25)

            # Para f(x)=x^2 en la partición uniforme de [0,1]:
            # U_n - L_n = 1/n exactamente.
            new_gap = MathTex(
                rf"U_n-L_n=\frac{{1}}{{{n}}}",
                color=MA_GREEN,
                font_size=34,
            )
            new_gap.next_to(formula, UP, buff=0.28).align_to(formula, LEFT)

            if step == 0:
                self.play(
                    LaggedStart(
                        FadeIn(new_lower),
                        FadeIn(new_upper),
                        FadeIn(new_n),
                        FadeIn(new_gap),
                        lag_ratio=0.12,
                    ),
                    run_time=2.0,
                )
            else:
                self.play(
                    ReplacementTransform(lower_rects, new_lower),
                    ReplacementTransform(upper_rects, new_upper),
                    Transform(n_label, new_n),
                    Transform(gap_label, new_gap),
                    run_time=1.7,
                )

            lower_rects, upper_rects = new_lower, new_upper
            n_label, gap_label = new_n, new_gap
            self.wait(0.7)

        limit_gap = MathTex(
            r"U_n-L_n\longrightarrow 0",
            color=MA_GREEN,
            font_size=46,
        ).move_to(gap_label)

        self.play(Transform(gap_label, limit_gap), run_time=1.2)
        self.wait(0.8)

        # Aislar una franja hace emerger la estructura altura × anchura.
        x0 = 0.75
        x1 = x0 + 1 / 32
        xi = (x0 + x1) / 2

        term_brace = BraceBetweenPoints(
            axes.c2p(x0, 0),
            axes.c2p(x1, 0),
            direction=DOWN,
            color=MA_GREEN,
        )
        width_label = MathTex(r"\Delta x_i", color=MA_GREEN, font_size=30)
        width_label.next_to(term_brace, DOWN, buff=0.08)

        sample_height = DashedLine(
            axes.c2p(xi, 0),
            axes.c2p(xi, f(xi)),
            color=MA_GREEN,
            stroke_width=2.5,
        )
        height_label = MathTex(r"f(\xi_i)", color=MA_GREEN, font_size=30)
        height_label.next_to(sample_height, RIGHT, buff=0.08)

        term = MathTex(
            r"f(\xi_i)\,\Delta x_i",
            color=MA_GREEN,
            font_size=38,
        ).to_corner(DR).shift(UP * 1.25 + LEFT * 0.15)

        riemann_sum = MathTex(
            r"\sum_{i=1}^{n} f(\xi_i)\,\Delta x_i",
            color=MA_INK,
            font_size=44,
        ).to_corner(DR).shift(UP * 0.35 + LEFT * 0.12)

        self.play(
            FadeOut(formula),
            FadeOut(gap_label),
            FadeOut(n_label),
            Create(term_brace),
            FadeIn(width_label),
            Create(sample_height),
            FadeIn(height_label),
            FadeIn(term),
            run_time=1.5,
        )
        self.wait(0.7)
        self.play(TransformFromCopy(term, riemann_sum), run_time=1.2)
        self.wait(0.8)

        conclusion = VGroup(
            Text("El dibujo motiva.", font_size=30, color=MA_MUTED),
            Text(
                "La teoría debe demostrar qué sobrevive al refinar.",
                font_size=30,
                color=MA_INK,
                weight=BOLD,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        conclusion.to_edge(DOWN, buff=0.28)

        self.play(FadeIn(conclusion, shift=UP * 0.12), run_time=1.0)
        self.wait(1.5)

    def _rect(self, axes: Axes, a: float, b: float, h: float, color: str, opacity: float):
        return Polygon(
            axes.c2p(a, 0),
            axes.c2p(b, 0),
            axes.c2p(b, h),
            axes.c2p(a, h),
            stroke_color=color,
            stroke_width=1.3,
            fill_color=color,
            fill_opacity=opacity,
        )

    def _bounds_rectangles(self, axes: Axes, n: int):
        dx = 1 / n
        lower = VGroup()
        upper = VGroup()

        for k in range(n):
            a = k * dx
            b = (k + 1) * dx
            h_low = f(a)
            h_up = f(b)

            if h_low > 0:
                lower.add(self._rect(axes, a, b, h_low, MA_BLUE, 0.23))

            upper.add(self._rect(axes, a, b, h_up, MA_ORANGE, 0.13))

        return lower, upper
