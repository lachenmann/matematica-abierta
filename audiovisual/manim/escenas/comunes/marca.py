from manim import *
import numpy as np

# Marca audiovisual de Matemática Abierta.
# Reconstrucción canónica v2 a partir de la intro aprobada en Mac.

BG = "#0F1117"
FG = "#F5F7FA"
BLUE = "#22AFF5"
MUTED = "#A7B0BE"


def a_squared(scale: float = 1.0) -> VGroup:
    """Símbolo a² reutilizable, con a y 2 como objetos independientes."""
    a = MathTex("a", color=BLUE).scale(2.25 * scale)
    two = MathTex("2", color=BLUE).scale(0.72 * scale)
    two.next_to(a, UR, buff=0.03)
    two.shift(0.10 * DOWN + 0.03 * LEFT)
    return VGroup(a, two)


def wordmark(scale: float = 1.0) -> VGroup:
    """Wordmark Matemátic + a² + biertA."""
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


def ease_out_bounce(t: float) -> float:
    """Curva de rebote determinista, sin depender de rate functions externas."""
    n1 = 7.5625
    d1 = 2.75
    if t < 1 / d1:
        return n1 * t * t
    if t < 2 / d1:
        t -= 1.5 / d1
        return n1 * t * t + 0.75
    if t < 2.5 / d1:
        t -= 2.25 / d1
        return n1 * t * t + 0.9375
    t -= 2.625 / d1
    return n1 * t * t + 0.984375


def play_bouncy_a_squared(
    scene: Scene,
    scale: float = 1.0,
    center=ORIGIN,
) -> VGroup:
    """Hace entrar a² saltando y deja un movimiento secundario suave."""
    mark = a_squared(scale=scale)
    a, two = mark

    mark.move_to(center)
    a_target = a.get_center().copy()
    two_target = two.get_center().copy()

    a.move_to(a_target + 3.6 * UP)
    two.move_to(two_target + 4.3 * UP + 0.18 * RIGHT)

    scene.add(a)
    scene.play(
        a.animate.move_to(a_target),
        run_time=1.10,
        rate_func=ease_out_bounce,
    )

    # Squash / stretch breve al aterrizar.
    scene.play(
        a.animate.stretch(1.08, 0).stretch(0.84, 1),
        run_time=0.11,
        rate_func=smooth,
    )
    scene.play(
        a.animate.stretch(1 / 1.08, 0).stretch(1 / 0.84, 1),
        run_time=0.16,
        rate_func=smooth,
    )

    scene.add(two)
    scene.play(
        two.animate.move_to(two_target),
        run_time=0.85,
        rate_func=ease_out_bounce,
    )
    scene.play(
        two.animate.shift(0.12 * UP),
        run_time=0.22,
        rate_func=there_and_back,
    )

    # Idle independiente: la a respira y el exponente flota un poco más.
    bases = [a.get_center().copy(), two.get_center().copy()]
    amplitudes = [0.035, 0.070]
    speeds = [1.25, 1.55]
    phases = [0.0, 0.55]

    for obj, base, amp, speed, phase in zip(
        mark, bases, amplitudes, speeds, phases
    ):
        obj._idle_t = 0.0

        def idle(
            m,
            dt,
            base=base,
            amp=amp,
            speed=speed,
            phase=phase,
        ):
            m._idle_t += dt
            y = base[1] + amp * np.sin(speed * m._idle_t + phase)
            m.move_to([base[0], y, base[2]])

        obj.add_updater(idle)

    return mark
