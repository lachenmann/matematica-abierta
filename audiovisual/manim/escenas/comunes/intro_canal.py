from manim import *
from pathlib import Path
import numpy as np

from marca import BG, BLUE, FG, MUTED, a_squared

config.background_color = BG

MANIM_ROOT = Path(__file__).resolve().parents[2]
INTRO_DURATION_SECONDS = 7.0
INTRO_MUSIC_FILE = (
    MANIM_ROOT
    / "assets"
    / "audio"
    / "intro"
    / "CPM-intro-music.wav"
)
INTRO_MUSIC_GAIN_DB = -18.0


def add_intro_music(scene: Scene) -> None:
    """Añade la cortina oficial sólo al tramo de 7 s de IntroCanal."""
    if not INTRO_MUSIC_FILE.exists():
        raise FileNotFoundError(
            "No existe la cortina musical canónica. Ejecuta "
            "prepare-intro-music.ps1. Ruta esperada: "
            + str(INTRO_MUSIC_FILE)
        )
    scene.add_sound(
        str(INTRO_MUSIC_FILE),
        gain=INTRO_MUSIC_GAIN_DB,
    )


class IntroCanal(Scene):
    """Intro canónica de Matemática Abierta, retimizada a 7,00 s."""

    def construct(self):
        self.camera.background_color = BG

        background = self.math_background()
        self.add_background_motion(background)
        self.play(
            LaggedStart(
                *[FadeIn(obj, shift=0.06 * UP) for obj in background],
                lag_ratio=0.08,
            ),
            run_time=0.55,
        )

        ring = Circle(radius=1.38, color=BLUE, stroke_width=4.0)
        mark = a_squared(scale=1.15)
        a, two = mark

        self.play(Create(ring), run_time=0.55)
        self.play(Write(a), run_time=0.45)
        self.play(FadeIn(two, shift=0.22 * UP), run_time=0.30)
        self.wait(0.20)

        self.play(
            FadeOut(ring),
            mark.animate.scale(0.70).move_to(ORIGIN),
            run_time=0.45,
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
            run_time=0.85,
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

        self.play(FadeIn(tag, shift=0.10 * UP), run_time=0.40)
        self.play(Create(line_l), FadeIn(inf), Create(line_r), run_time=0.40)

        # El lockup permanece el tiempo suficiente para que la frase musical
        # complete su arco antes del fade-out final.
        self.wait(1.35)

        lockup = VGroup(left_start, target_mark, right_start, tag, rule)
        self.play(
            background.animate.set_opacity(0.0),
            lockup.animate.scale(0.92),
            run_time=0.55,
        )
        self.wait(0.35)

        for obj in background:
            obj.clear_updaters()

        self.play(FadeOut(lockup), run_time=0.60)


    def add_background_motion(self, background: VGroup):
        """Movimiento tenue y continuo del fondo matemático."""
        for i, obj in enumerate(background):
            base = np.array(obj.get_center())
            phase = 0.70 * i
            speed = 0.38 + 0.05 * i
            amp_x = 0.05 + 0.01 * (i % 3)
            amp_y = 0.035 + 0.008 * (i % 4)

            def drift(
                m,
                dt,
                base=base,
                phase=phase,
                speed=speed,
                amp_x=amp_x,
                amp_y=amp_y,
            ):
                t = getattr(m, "_drift_t", 0.0) + dt
                m._drift_t = t
                x = base[0] + amp_x * np.sin(speed * t + phase)
                y = base[1] + amp_y * np.cos(
                    0.82 * speed * t + phase
                )
                m.move_to([x, y, base[2]])

            obj.add_updater(drift)

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


class IntroCanalConMusica(IntroCanal):
    """Wrapper para render aislado: intro visual + cortina oficial."""

    def construct(self):
        add_intro_music(self)
        super().construct()
