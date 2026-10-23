"""Refinamiento de la maqueta original, gobernado por los WAV de Kokoro."""
from __future__ import annotations
import json
from pathlib import Path
from manim import *

BG, FG, MUTED = "#0F1117", "#F5F7FA", "#A7B0BE"
BLUE, ORANGE, GREEN = "#4EA1FF", "#FFB454", "#63D471"
config.background_color = BG
TEX = TexTemplate(tex_compiler="xelatex", output_format=".xdv")


class MAVIZSecanteTangente(Scene):
    def math(self, text, size=42, color=FG):
        return MathTex(text, font_size=size, color=color, tex_template=TEX)

    def text(self, text, size=32, color=FG):
        return Tex(text, font_size=size, color=color, tex_template=TEX)

    def cue(self, name):
        target = self.cues[name]["inicio"]
        remaining = target - self.time
        if remaining < -1 / config.frame_rate - 1e-5:
            raise ValueError(f"SYNC WARN {name}: {self.time:.3f} > {target:.3f}")
        if remaining > 1e-5:
            self.wait(remaining)

    def construct(self):
        timeline = json.loads((Path(__file__).parent / "generados/timing_produccion.json").read_text(encoding="utf-8"))
        self.cues = {c["id"]: c for c in timeline["cues"] + timeline["marcadores_visuales"]}
        title = self.text("De la secante a la tangente", 38).move_to([0, 3.37, 0])
        divider = Line([-5.5, 2.94, 0], [5.5, 2.94, 0], color=MUTED, stroke_width=1.2)
        self.play(FadeIn(title), Create(divider), run_time=0.8)
        axes = Axes(x_range=[0, 3.2, 1], y_range=[0, 7.2, 1], x_length=7.5,
                    y_length=4.0, tips=False,
                    axis_config={"color": MUTED, "stroke_width": 2}).shift(LEFT * 1.8 + UP * 0.15)
        labels = VGroup(self.math("x", 27, MUTED).next_to(axes.x_axis, RIGHT, buff=.13),
                        self.math("y", 27, MUTED).next_to(axes.y_axis, UP, buff=.13),
                        self.math("1", 25, MUTED).next_to(axes.c2p(1, 0), DOWN, buff=.1))
        curve = axes.plot(lambda x: x*x, x_range=[0, 2.62], color=BLUE, stroke_width=5)
        formula = self.math("f(x)=x^2", 50, BLUE).move_to([4.15, 1.75, 0])
        self.cue("curva")
        self.play(Create(axes), FadeIn(labels), run_time=.7)
        self.play(Create(curve), run_time=.95)
        self.cue("formula_funcion")
        self.play(Write(formula), run_time=1.2)
        self.cue("funcion")
        tracer = Dot(axes.c2p(.4, .16), radius=.07, color=FG)
        path = axes.plot(lambda x: x*x, x_range=[.4, 2.4])
        self.play(FadeIn(tracer), run_time=.25)
        self.play(MoveAlongPath(tracer, path), run_time=2.3, rate_func=smooth)
        self.play(FadeOut(tracer), run_time=.25)

        h = ValueTracker(1.15)
        point_a = Dot(axes.c2p(1, 1), radius=.085, color=GREEN).set_z_index(5)
        a_label = self.math("A", 30, GREEN).next_to(point_a, UL, buff=.14)
        a_coord = self.math("A=(1,1)", 34, GREEN).move_to([4.15, .78, 0])
        self.cue("punto_a")
        self.play(FadeIn(point_a), Write(a_label), run_time=.7)
        self.cue("coordenada_a")
        self.play(Write(a_coord), run_time=.75)
        self.cue("punto_b")
        point_b = always_redraw(lambda: Dot(axes.c2p(1+h.get_value(), (1+h.get_value())**2),
                                           radius=.085, color=ORANGE).set_z_index(5))
        b_label = always_redraw(lambda: self.math("B", 30, ORANGE).next_to(point_b, UL, buff=.14))
        self.play(FadeIn(point_b), FadeIn(b_label), run_time=.7)
        self.cue("secante")
        def secant_line():
            m = 2+h.get_value()
            return Line(axes.c2p(.68, 1+m*(.68-1)), axes.c2p(2.52, 1+m*(2.52-1)),
                        color=ORANGE, stroke_width=4)
        secant = always_redraw(secant_line)
        caption = self.text("Recta secante", 31, ORANGE).move_to([4.15, -.2, 0])
        self.play(Create(secant), run_time=1.0)
        self.cue("nombre_secante")
        self.play(Write(caption), run_time=.65)

        self.cue("h")
        self.cue("nombre_h")
        def span():
            left = axes.c2p(1, 0)+DOWN*.37
            right = axes.c2p(1+h.get_value(), 0)+DOWN*.37
            return VGroup(Line(left, right, color=ORANGE, stroke_width=3),
                          Line(left+UP*.055, left+DOWN*.055, color=ORANGE, stroke_width=2),
                          Line(right+UP*.055, right+DOWN*.055, color=ORANGE, stroke_width=2))
        h_span = always_redraw(span)
        h_label = self.math("h", 29, ORANGE)
        h_label.add_updater(lambda m: m.next_to(h_span, DOWN, buff=.08))
        project = always_redraw(lambda: DashedLine(point_b.get_center(), axes.c2p(1+h.get_value(), 0),
                                                  color=MUTED, stroke_width=1.5, dash_length=.08))
        h_condition = self.math("h>0", 28, GREEN).move_to([4.15, -2.4, 0])
        self.play(FadeIn(project), Create(h_span), Write(h_label), Write(h_condition), run_time=.9)
        self.cue("pendiente")
        self.cue("nombre_pendiente")
        slope = MathTex("m(h)=", "2+h", font_size=43, color=ORANGE, tex_template=TEX).move_to([4.15, -1.28, 0])
        self.play(Write(slope[0]), run_time=.7)
        self.cue("valor_pendiente")
        self.play(Write(slope[1]), run_time=.9)

        self.cue("limite_h")
        self.cue("h_cero")
        approach = self.math(r"h\longrightarrow 0^+", 34, ORANGE).move_to([4.15, -2.4, 0])
        self.play(FadeOut(h_condition), FadeOut(b_label), run_time=.2)
        b_label.clear_updaters()
        self.play(Write(approach), run_time=.55)
        left = self.cues["limite_m"]["inicio"] - self.time
        self.play(h.animate.set_value(.38), run_time=left, rate_func=smooth)
        self.cue("limite_m")
        limit_m = self.math(r"m(h)\longrightarrow 2", 37, ORANGE).move_to([4.15, -1.28, 0])
        self.play(FadeOut(slope), run_time=.2)
        self.cue("m_dos")
        self.play(Write(limit_m), h.animate.set_value(.08), run_time=.75)

        self.cue("tangente")
        self.play(h.animate.set_value(.001), FadeOut(point_b), FadeOut(project),
                  FadeOut(h_span), FadeOut(h_label), run_time=1.3)
        for mob in (point_b, project, h_span, h_label):
            mob.clear_updaters()
        tangent = Line(axes.c2p(.68, .36), axes.c2p(2.52, 4.04), color=GREEN, stroke_width=4)
        secant.clear_updaters()
        self.cue("nombre_tangente")
        self.play(FadeOut(secant), FadeOut(caption), FadeOut(approach), FadeOut(limit_m), run_time=.2)
        tangent_caption = self.text("Recta tangente", 31, GREEN).move_to(caption)
        self.play(Create(tangent), Write(tangent_caption), run_time=1.0)
        self.cue("dos")
        m_two = self.math("m=2", 48, GREEN).move_to([4.15, -1.28, 0])
        self.cue("pendiente_dos")
        self.play(Write(m_two), run_time=.8)
        self.cue("derivada")
        self.cue("nombre_derivada")
        self.play(FadeOut(m_two), run_time=.2)
        derivative = self.math("f'(1)=2", 53, GREEN).move_to([4.15, -1.28, 0])
        self.play(Write(derivative), run_time=1.0)
        box = SurroundingRectangle(derivative, color=GREEN, buff=.2, stroke_width=1.5)
        self.play(Create(box), run_time=.45)
        self.wait(max(0, timeline["duracion_total"] - self.time))
