from manim import *

from marca import BG, BLUE, FG, MUTED, a_squared

config.background_color = BG


class IntroCanal(Scene):
    """Reconstrucción v2 de la intro aprobada de Matemática Abierta."""

    def construct(self):
        self.camera.background_color = BG

        background = self.math_background()
        self.play(
            LaggedStart(
                *[FadeIn(obj, shift=0.06 * UP) for obj in background],
                lag_ratio=0.08,
            ),
            run_time=1.0,
        )

        ring = Circle(radius=1.38, color=BLUE, stroke_width=4.0)
        mark = a_squared(scale=1.15)
        a, two = mark

        self.play(Create(ring), run_time=1.0)
        self.play(Write(a), run_time=0.9)
        self.play(FadeIn(two, shift=0.22 * UP), run_time=0.55)
        self.wait(0.45)

        self.play(
            FadeOut(ring),
            mark.animate.scale(0.70).move_to(ORIGIN),
            run_time=0.75,
        )

        left = Tex(r"Matemátic", color=FG).scale(1.25)
        right = Tex(r"biertA", color=FG).scale(1.25)
        target_mark = a_squared(scale=0.72)
        full = VGroup(left, target_mark, right).arrange(RIGHT, buff=0.10)
        target_mark.shift(0.02 * DOWN)
        full.move_to([0, 0.25, 0])

        left_start = left.copy().move_to(full[0]).shift(5.8 * LEFT)
        right_start = right.copy().move_to(full[2]).shift(5.8 * RIGHT)
        self.add(left_start, right_start)

        self.play(
            left_start.animate.move_to(full[0]),
            right_start.animate.move_to(full[2]),
            mark.animate.move_to(full[1]).scale(0.72 / 0.805),
            run_time=1.35,
            rate_func=smooth,
        )

        self.remove(mark)
        self.add(target_mark)

        tag = Tex(r"CONOCIMIENTO PARA TODOS", color=MUTED).scale(0.44)
        tag.next_to(full, DOWN, buff=0.40)

        inf = MathTex(r"\infty", color=MUTED).scale(0.70)
        line_l = Line(LEFT * 2.20, LEFT * 0.60, color=MUTED, stroke_width=1.5)
        line_r = Line(RIGHT * 0.60, RIGHT * 2.20, color=MUTED, stroke_width=1.5)
        rule = VGroup(line_l, inf, line_r).arrange(RIGHT, buff=0.18)
        rule.next_to(tag, DOWN, buff=0.30)

        self.play(FadeIn(tag, shift=0.10 * UP), run_time=0.65)
        self.play(Create(line_l), FadeIn(inf), Create(line_r), run_time=0.70)
        self.wait(2.1)

        lockup = VGroup(left_start, target_mark, right_start, tag, rule)
        self.play(
            background.animate.set_opacity(0.0),
            lockup.animate.scale(0.92),
            run_time=0.80,
        )
        self.wait(0.45)
        self.play(FadeOut(lockup), run_time=0.65)

    def math_background(self) -> VGroup:
        """Motivos matemáticos recordados de la intro original."""
        opacity = 0.16

        summation = MathTex(
            r"\sum_{k=1}^{n} k = \frac{n(n+1)}{2}",
            color=MUTED,
        ).scale(0.65).move_to([-4.5, 2.55, 0])

        circle = Circle(radius=0.70, color=MUTED, stroke_width=1.2)
        radius = Line(circle.get_center(), circle.get_right(), color=MUTED, stroke_width=1.2)
        circle_group = VGroup(circle, radius).move_to([4.65, 2.45, 0])

        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[0, 3, 1],
            x_length=2.7,
            y_length=1.8,
            tips=False,
            axis_config={"color": MUTED, "stroke_width": 1.0},
        )
        parabola = axes.plot(lambda x: 0.55 * x * x, x_range=[-1.8, 1.8], color=MUTED)
        graph_group = VGroup(axes, parabola).scale(0.82).move_to([-4.45, -2.25, 0])

        limit = MathTex(
            r"\lim_{x\to0}\frac{\sin x}{x}=1",
            color=MUTED,
        ).scale(0.62).move_to([4.55, -2.35, 0])

        matrix = MathTex(
            r"\begin{pmatrix}a&b\\c&d\end{pmatrix}",
            color=MUTED,
        ).scale(0.68).move_to([5.00, 0.25, 0])

        derivative = MathTex(
            r"\frac{d}{dx}x^n=nx^{n-1}",
            color=MUTED,
        ).scale(0.62).move_to([-4.75, 0.10, 0])

        triangle = Polygon(
            [-0.55, -0.35, 0],
            [0.55, -0.35, 0],
            [0.05, 0.55, 0],
            color=MUTED,
            stroke_width=1.2,
        ).scale(0.95).move_to([0, -2.65, 0])

        group = VGroup(
            summation,
            circle_group,
            graph_group,
            limit,
            matrix,
            derivative,
            triangle,
        )
        group.set_opacity(opacity)
        return group
