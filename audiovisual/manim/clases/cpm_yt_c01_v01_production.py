from manim import *
from pathlib import Path
import json
import sys

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

MANIM_ROOT = Path(__file__).resolve().parents[1]
COMMON_ROOT = MANIM_ROOT / "escenas" / "comunes"
if str(COMMON_ROOT) not in sys.path:
    sys.path.insert(0, str(COMMON_ROOT))

from intro_canal import IntroCanal, INTRO_DURATION_SECONDS, add_intro_music
from marca import play_bouncy_a_squared

VOICE_ROOT = MANIM_ROOT / "cpm_yt_c01_v01" / "voice-reference"
TIMING_FILE = VOICE_ROOT / "voice-reference-timing.json"
AUDIO_FILE = VOICE_ROOT / "audio" / "CPM-YT-C01-V01-reference.wav"
VOICE_OFFSET_SECONDS = INTRO_DURATION_SECONDS

class CPMYTC01V01Production(IntroCanal):
    """Render de producción sincronizado con la toma continua de Reaper."""

    def construct(self):
        self.camera.background_color = BG
        self.load_voice_reference()
        add_intro_music(self)

        # 00 — Intro canónica autónoma: música, sin voz.
        IntroCanal.construct(self)

        # La voz comienza exactamente al terminar IntroCanal.
        self.sync_to("c01v01-00-start")

        # El logomark a² ocupa el resto de la introducción hablada.
        opening_mark = play_bouncy_a_squared(
            self,
            scale=1.0,
            center=ORIGIN,
        )

        # 01 — El título temático aparece sólo cuando comienza el contenido.
        self.sync_to("c01v01-01-aritmetica")
        for obj in opening_mark:
            obj.clear_updaters()
        self.play(FadeOut(opening_mark), run_time=0.30)
        self.section_title("Aritmética conocida")

        arithmetic = MathTex(
            r"2+3=5", r"\qquad", r"2\cdot3=6", r"\qquad",
            r"2\cdot x=1\Longrightarrow x=\frac12",
            color=FG,
        ).scale(0.95)
        arithmetic[0].set_color(BLUE)
        arithmetic[2].set_color(ORANGE)
        arithmetic[4].set_color(GREEN)
        self.play(LaggedStart(
            *[FadeIn(m, shift=0.15 * UP) for m in arithmetic],
            lag_ratio=0.12,
        ))

        # 02 — Cadena de sistemas numéricos
        self.sync_to("c01v01-02-cadena")
        self.clear_stage(arithmetic)
        self.section_title("Cadena de sistemas numéricos")
        chain = MathTex(
            r"\mathbb N", r"\subset", r"\mathbb Z", r"\subset",
            r"\mathbb Q", r"\subset", r"\mathbb R",
            color=FG,
        ).scale(1.35)
        chain[0].set_color(BLUE)
        chain[2].set_color(ORANGE)
        chain[4].set_color(GREEN)
        chain[6].set_color(VIOLET)
        self.play(LaggedStart(
            *[FadeIn(m, shift=0.18 * RIGHT) for m in chain],
            lag_ratio=0.10,
        ))

        self.sync_to("c01v01-03-naturales-suma")
        expr = MathTex(r"3", r"+", r"5", r"=", r"8", color=FG).scale(1.5)
        expr.move_to([0, -1.45, 0])
        expr[4].set_color(BLUE)
        marker = SurroundingRectangle(chain[0], color=BLUE, buff=0.12)
        self.play(Create(marker), FadeIn(expr))

        self.sync_to("c01v01-04-naturales-resta")
        minus = MathTex(r"-", color=RED).scale(1.5).move_to(expr[1].get_center())
        negative_two = MathTex(r"-2", color=RED).scale(1.5).move_to(expr[4].get_center())
        self.play(
            Transform(expr[1], minus),
            Transform(expr[4], negative_two),
            run_time=0.75,
            rate_func=smooth,
        )
        not_natural = MathTex(r"-2\notin\mathbb N", color=RED).scale(1.0)
        not_natural.next_to(expr, DOWN, buff=0.30)
        self.play(FadeIn(not_natural, shift=0.10 * UP))

        self.sync_to("c01v01-05-enteros")
        in_integers = MathTex(r"-2\in\mathbb Z", color=ORANGE).scale(1.0)
        in_integers.next_to(expr, DOWN, buff=0.30)
        self.play(
            marker.animate.move_to(chain[2]).set_color(ORANGE),
            FadeOut(not_natural),
            FadeIn(in_integers, shift=0.10 * UP),
            run_time=0.8,
        )

        self.sync_to("c01v01-06-racionales")
        self.play(FadeOut(expr), FadeOut(in_integers), run_time=0.35)
        eq = MathTex(r"2\cdot x=1", color=FG).scale(1.35).move_to([0, -1.45, 0])
        self.play(FadeIn(eq))
        half = MathTex(r"x=\frac12", color=GREEN).scale(1.35).move_to(eq)
        self.play(TransformMatchingTex(eq, half))
        half_not_z = MathTex(r"\frac12\notin\mathbb Z", color=RED).scale(1.0)
        half_not_z.next_to(half, DOWN, buff=0.30)
        self.play(FadeIn(half_not_z, shift=0.10 * UP))
        half_in_q = MathTex(r"\frac12\in\mathbb Q", color=GREEN).scale(1.0)
        half_in_q.next_to(half, DOWN, buff=0.30)
        self.play(
            marker.animate.move_to(chain[4]).set_color(GREEN),
            FadeOut(half_not_z),
            FadeIn(half_in_q, shift=0.10 * UP),
            run_time=0.8,
        )

        # 03 — Spoiler tenue
        self.sync_to("c01v01-07-spoiler-supremo")
        spoiler = Tex(r"Spoiler: supremo", color=MUTED).scale(0.78).move_to([0, 1.55, 0])
        self.play(FadeIn(spoiler, run_time=0.8))
        self.wait(1.0)
        self.play(FadeOut(spoiler, run_time=0.8))

        self.sync_to("c01v01-08-cuerpo")
        self.clear_stage(chain, half, half_in_q, marker)
        body_answer = Tex(r"Un cuerpo", color=BLUE).scale(1.45)
        self.play(FadeIn(body_answer, shift=0.12 * UP))

        # 04 — Conjunto y clausura
        self.sync_to("c01v01-09-conjunto-f")
        self.play(FadeOut(body_answer), run_time=0.35)
        self.section_title("Operaciones internas")
        f_nonempty = MathTex(r"F\neq\varnothing", color=FG).scale(1.35)
        self.play(FadeIn(f_nonempty))

        self.sync_to("c01v01-10-clausura")
        closure = MathTex(
            r"a,b\in F",
            r"\Longrightarrow",
            r"a+b\in F,\qquad a\cdot b\in F",
            color=FG,
        ).scale(1.05).next_to(f_nonempty, DOWN, buff=0.65)
        closure[2].set_color(BLUE)
        self.play(LaggedStart(*[FadeIn(m) for m in closure], lag_ratio=0.10))

        # 05 — Dos operaciones primitivas
        self.sync_to("c01v01-11-operaciones-primitivas")
        self.clear_stage(f_nonempty, closure)
        self.section_title("Dos operaciones primitivas")
        plus = MathTex(r"+", color=BLUE).scale(3)
        times = MathTex(r"\cdot", color=ORANGE).scale(3)
        ops = VGroup(plus, times).arrange(RIGHT, buff=2.4)
        self.play(GrowFromCenter(plus), GrowFromCenter(times))

        # 06–09 — Axiomas aditivos
        self.sync_to("c01v01-12-asoc-suma")
        self.clear_stage(ops)
        self.section_title("Axioma 1 — Asociatividad de la suma")
        state = self.associativity_sum()

        self.sync_to("c01v01-13-neutro-suma")
        self.play(FadeOut(state), run_time=0.35)
        self.replace_section_title("Axioma 2 — Neutro aditivo")
        state = self.additive_identity()

        self.sync_to("c01v01-14-inverso-suma")
        self.play(FadeOut(state), run_time=0.35)
        self.replace_section_title("Axioma 3 — Inverso aditivo")
        state = self.additive_inverse()

        self.sync_to("c01v01-15-conmut-suma")
        self.play(FadeOut(state), run_time=0.35)
        self.replace_section_title("Axioma 4 — Conmutatividad de la suma")
        state = self.commutativity_sum()

        # 10–13 — Axiomas multiplicativos
        self.sync_to("c01v01-16-asoc-producto")
        self.play(FadeOut(state), run_time=0.35)
        self.clear_stage()
        self.section_title("Axioma 5 — Asociatividad del producto")
        state = self.associativity_product()

        self.sync_to("c01v01-17-neutro-producto")
        self.play(FadeOut(state), run_time=0.35)
        self.replace_section_title("Axioma 6 — Neutro multiplicativo")
        state = self.multiplicative_identity()

        self.sync_to("c01v01-18-inverso-producto")
        self.play(FadeOut(state), run_time=0.35)
        self.replace_section_title("Axioma 7 — Inverso multiplicativo")
        state = self.multiplicative_inverse()

        self.sync_to("c01v01-19-cero-sin-inverso")
        state[0].set_color(ORANGE)
        self.play(Indicate(state[0], color=ORANGE), run_time=0.8)

        self.sync_to("c01v01-20-conmut-producto")
        self.play(FadeOut(state), run_time=0.35)
        self.replace_section_title("Axioma 8 — Conmutatividad del producto")
        state = self.commutativity_product()

        # 14 — Distributividad y lectura inversa
        self.sync_to("c01v01-21-distributividad")
        self.play(FadeOut(state), run_time=0.35)
        self.clear_stage()
        self.section_title("Axioma 9 — Distributividad")
        state = self.distributivity_demo()

        # 15 — Definición y cuerpo trivial
        self.sync_to("c01v01-23-def-cuerpo")
        self.play(FadeOut(state), run_time=0.35)
        self.clear_stage()
        self.section_title("Definición formal de cuerpo")
        definition = VGroup(
            MathTex(
                r"(F,+,\cdot,0,1)",
                color=FG,
            ).scale(1.32),
            MathTex(
                r"F\neq\varnothing,\qquad 0,1\in F,\qquad 0\neq1",
                color=FG,
            ).scale(0.98),
            MathTex(
                r"+\colon F\times F\longrightarrow F",
                color=BLUE,
            ).scale(0.98),
            MathTex(
                r"\cdot\colon F\times F\longrightarrow F",
                color=ORANGE,
            ).scale(0.98),
            MathTex(
                r"\forall a,b,c\in F:\quad \text{se satisfacen los axiomas }1\text{--}9",
                color=MUTED,
            ).scale(0.72),
        ).arrange(DOWN, buff=0.34)
        definition[1].set_color_by_tex(r"0\neq1", GREEN)
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=0.08 * UP) for row in definition],
                lag_ratio=0.14,
            ),
            run_time=1.4,
        )

        self.sync_to("c01v01-24-cuerpo-trivial")
        self.clear_stage(definition)
        self.section_title("Cuerpo trivial")
        trivial = MathTex(r"F=\{0\},\qquad", r"1=0", color=FG).scale(1.25)
        trivial[1].set_color(RED)
        self.play(Write(trivial))

        self.sync_to("c01v01-25-trivial-operaciones")
        ops_trivial = MathTex(r"0+0=0,\qquad", r"0\cdot0=0", color=FG).scale(1.1)
        ops_trivial.next_to(trivial, DOWN, buff=0.65)
        self.play(LaggedStart(
            Write(ops_trivial[0]), Write(ops_trivial[1]), lag_ratio=0.45
        ))

        self.sync_to("c01v01-26-excluir-trivial")
        exclusion = MathTex(r"0\neq1", color=GREEN).scale(1.45)
        exclusion.next_to(ops_trivial, DOWN, buff=0.65)
        self.play(FadeIn(exclusion, shift=0.15 * UP))
        box = SurroundingRectangle(exclusion, color=GREEN, buff=0.16)
        self.play(Create(box))

        # La voz recapitula ahora, uno por uno, los grupos de axiomas.
        # Tiempos QA fijados por el autor: 7:16 / 7:29 / 7:40.
        self.sync_between(
            "c01v01-26-excluir-trivial",
            "c01v01-27-tabla-axiomas",
            0.236398,
        )
        self.clear_stage(trivial, ops_trivial, exclusion, box)
        self.section_title("Axiomas 1–4 — Estructura aditiva")
        recap = self.axiom_recap_panel("additive")
        self.play(FadeIn(recap, shift=0.08 * UP), run_time=0.65)

        self.sync_between(
            "c01v01-26-excluir-trivial",
            "c01v01-27-tabla-axiomas",
            0.573739,
        )
        self.play(FadeOut(recap), run_time=0.35)
        self.replace_section_title("Axiomas 5–8 — Estructura multiplicativa")
        recap = self.axiom_recap_panel("multiplicative")
        self.play(FadeIn(recap, shift=0.08 * UP), run_time=0.65)

        self.sync_between(
            "c01v01-26-excluir-trivial",
            "c01v01-27-tabla-axiomas",
            0.859181,
        )
        self.play(FadeOut(recap), run_time=0.35)
        self.replace_section_title("Axioma 9 — Distributividad")
        recap = self.axiom_recap_panel("distributive")
        self.play(FadeIn(recap, shift=0.08 * UP), run_time=0.65)

        # 16 — Tabla de síntesis
        self.sync_to("c01v01-27-tabla-axiomas")
        self.play(FadeOut(recap), run_time=0.35)
        self.clear_stage()
        self.section_title("Condición estructural y nueve axiomas")
        state = self.axiom_summary()

        # 17 — F_2 de Spivak
        self.sync_to("c01v01-28-f2")
        self.play(FadeOut(state), run_time=0.35)
        self.clear_stage()
        self.section_title("Cuerpo de dos elementos")
        state = self.f2_demo()

        # 18 — Lo que todavía no hemos supuesto
        self.sync_to("c01v01-32-consecuencias-pendientes")
        self.play(FadeOut(state), run_time=0.35)
        self.clear_stage()
        self.section_title("Propiedades todavía no demostradas")
        pending = self.pending_consequences_panel()

        # El inventario se construye en el mismo orden en que lo enumera la voz.
        reveal_fractions = [0.05, 0.14, 0.23, 0.34, 0.44, 0.55, 0.66]
        for row, fraction in zip(pending, reveal_fractions):
            self.sync_between(
                "c01v01-32-consecuencias-pendientes",
                "c01v01-33-enteros-ejemplo",
                fraction,
            )
            self.play(FadeIn(row, shift=0.10 * RIGHT), run_time=0.45)

        # 19 — Los enteros no forman un cuerpo
        self.sync_to("c01v01-33-enteros-ejemplo")
        self.clear_stage(pending)
        self.section_title("¿Los enteros forman un cuerpo?")

        # La Z deja de ser una imagen estática: funciona como referencia mientras
        # se auditan, en el orden de la voz, las propiedades que sí se cumplen.
        integers = MathTex(r"\mathbb Z", color=ORANGE).scale(2.2)
        circle = Circle(radius=1.5, color=ORANGE).move_to(integers)
        integer_set = VGroup(circle, integers).move_to([-4.35, -0.25, 0])
        self.play(Create(circle), FadeIn(integers), run_time=0.75)

        integer_audit = self.integer_field_audit_cards()

        self.sync_between(
            "c01v01-33-enteros-ejemplo",
            "c01v01-34-enteros-inverso",
            0.12,
        )
        self.play(FadeIn(integer_audit[0], shift=0.10 * RIGHT), run_time=0.65)

        self.sync_between(
            "c01v01-33-enteros-ejemplo",
            "c01v01-34-enteros-inverso",
            0.50,
        )
        self.play(FadeIn(integer_audit[1], shift=0.10 * RIGHT), run_time=0.65)

        self.sync_between(
            "c01v01-33-enteros-ejemplo",
            "c01v01-34-enteros-inverso",
            0.70,
        )
        self.play(FadeIn(integer_audit[2], shift=0.10 * RIGHT), run_time=0.55)

        self.sync_between(
            "c01v01-33-enteros-ejemplo",
            "c01v01-34-enteros-inverso",
            0.86,
        )
        self.play(FadeIn(integer_audit[3], shift=0.10 * RIGHT), run_time=0.55)
        self.play(Indicate(integer_audit[3], color=ORANGE), run_time=0.75)

        self.sync_to("c01v01-34-enteros-inverso")
        self.play(
            FadeOut(integer_audit),
            circle.animate.move_to(ORIGIN),
            integers.animate.move_to(ORIGIN),
            run_time=0.55,
        )
        self.replace_section_title("Falla el inverso multiplicativo")

        eq2 = MathTex(r"2\cdot x=1", color=FG).scale(1.25).to_edge(DOWN, buff=1.2)
        half2 = MathTex(r"x=\frac12", color=GREEN).scale(1.25).move_to(eq2)
        half_floating = MathTex(r"\frac12", color=GREEN).scale(1.6).move_to(integers)
        self.play(Write(eq2))
        self.play(TransformMatchingTex(eq2, half2))
        self.play(FadeIn(half_floating))

        self.sync_to("c01v01-35-medio-no-entero")
        self.play(
            half_floating.animate.shift(3.0 * RIGHT).set_color(RED),
            circle.animate.set_color(RED),
            integers.animate.set_color(RED),
        )
        not_in = MathTex(r"\frac12\notin\mathbb Z", color=RED).scale(1.2)
        not_in.to_edge(DOWN, buff=1.0)
        self.play(FadeOut(half2), FadeIn(not_in, shift=0.14 * UP))

        # 20 — Q y R sí
        self.sync_to("c01v01-36-racionales-reales")
        self.clear_stage(circle, integers, half_floating, not_in)
        self.section_title("Dos cuerpos familiares")
        qr = MathTex(r"\mathbb Q", r"\qquad", r"\mathbb R", color=FG).scale(1.8)
        qr[0].set_color(GREEN)
        qr[2].set_color(VIOLET)
        self.play(FadeIn(qr, scale=0.92))

        # La narración pasa de los cuerpos familiares a la estructura que
        # todavía NO se ha añadido: orden, intervalos, cotas y completitud.
        self.sync_between(
            "c01v01-36-racionales-reales",
            "c01v01-37-cierre-siguiente-clase",
            0.20,
        )
        self.play(FadeOut(qr), run_time=0.35)
        self.replace_section_title("Lo que todavía no hemos supuesto")
        not_yet = self.not_yet_order_panel()
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=0.08 * RIGHT) for row in not_yet],
                lag_ratio=0.14,
            ),
            run_time=1.25,
        )

        # Consecuencia: todo teorema obtenido aquí vale en cualquier cuerpo.
        self.sync_between(
            "c01v01-36-racionales-reales",
            "c01v01-37-cierre-siguiente-clase",
            0.68,
        )
        self.play(FadeOut(not_yet), run_time=0.35)
        self.replace_section_title("Consecuencias puramente algebraicas")
        universality = self.field_universality_panel()
        self.play(FadeIn(universality, shift=0.08 * UP), run_time=0.75)

        # 21 — Enlace con el siguiente video
        self.sync_to("c01v01-37-cierre-siguiente-clase")
        self.clear_stage(universality)
        self.section_title("Siguiente clase: teoremas derivados de los axiomas")

        source_box = RoundedRectangle(
            width=6.2, height=1.65, corner_radius=0.16,
            color=BLUE, stroke_width=2.0,
        ).move_to([0, 1.45, 0])
        source_title = Tex(r"Axiomas de cuerpo", color=BLUE).scale(0.82)
        source_formula = MathTex(
            r"0\neq1", r"\qquad", r"+", r"\qquad", r"\cdot",
            color=FG,
        ).scale(0.86)
        source_distributivity = MathTex(
            r"a\cdot(b+c)=a\cdot b+a\cdot c",
            color=FG,
        ).scale(0.62)
        source_group = VGroup(
            source_box, source_title, source_formula, source_distributivity
        )
        source_title.move_to(source_box.get_center() + 0.47 * UP)
        source_formula.move_to(source_box.get_center() + 0.02 * UP)
        source_distributivity.move_to(source_box.get_center() + 0.45 * DOWN)

        self.play(Create(source_box))
        self.play(FadeIn(source_title), FadeIn(source_formula))
        self.play(FadeIn(source_distributivity, shift=0.08 * UP))

        cards = VGroup(
            self.theorem_card("Unicidad del cero", r"0=0'", BLUE),
            self.theorem_card(
                "Unicidad del inverso",
                r"b+c=0=b+d\Longrightarrow c=d",
                ORANGE,
            ),
            self.theorem_card("Producto por cero", r"a\cdot0=0", GREEN),
            self.theorem_card(
                "Cancelación",
                r"a\cdot b=a\cdot c,\ a\neq0\Longrightarrow b=c",
                VIOLET,
            ),
        ).arrange_in_grid(rows=2, cols=2, buff=(0.90, 0.70))
        cards.scale(0.74).move_to([0, -1.00, 0])
        self.play(
            LaggedStart(
                *[FadeIn(card, shift=0.10 * UP) for card in cards],
                lag_ratio=0.14,
            ),
            run_time=1.2,
        )

        top_left_arrow = Arrow(
            source_box.get_bottom() + 1.55 * LEFT,
            cards[0].get_top(),
            buff=0.10,
            stroke_width=1.8,
            max_tip_length_to_length_ratio=0.10,
            color=MUTED,
        )
        top_right_arrow = Arrow(
            source_box.get_bottom() + 1.55 * RIGHT,
            cards[1].get_top(),
            buff=0.10,
            stroke_width=1.8,
            max_tip_length_to_length_ratio=0.10,
            color=MUTED,
        )
        junction_y = 0.5 * (cards[0].get_bottom()[1] + cards[2].get_top()[1])
        junction = [0, junction_y, 0]
        trunk = Line(source_box.get_bottom(), junction, stroke_width=1.8, color=MUTED)
        bottom_left_arrow = Arrow(
            junction, cards[2].get_top(),
            buff=0.10, stroke_width=1.8,
            max_tip_length_to_length_ratio=0.10, color=MUTED,
        )
        bottom_right_arrow = Arrow(
            junction, cards[3].get_top(),
            buff=0.10, stroke_width=1.8,
            max_tip_length_to_length_ratio=0.10, color=MUTED,
        )
        arrows = VGroup(
            top_left_arrow, top_right_arrow, trunk,
            bottom_left_arrow, bottom_right_arrow,
        )
        self.play(
            GrowArrow(top_left_arrow),
            GrowArrow(top_right_arrow),
            Create(trunk),
            run_time=0.70,
        )
        self.play(
            GrowArrow(bottom_left_arrow),
            GrowArrow(bottom_right_arrow),
            run_time=0.60,
        )

        self.sync_to("c01v01-38-end")
        tail = VOICE_OFFSET_SECONDS + self.audio_duration - float(self.renderer.time)
        if tail > 0:
            self.wait(tail)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def load_voice_reference(self):
        if not TIMING_FILE.exists():
            raise FileNotFoundError(f"No existe el timing canónico: {TIMING_FILE}")
        if not AUDIO_FILE.exists():
            raise FileNotFoundError(
                "No existe el WAV local. Se espera en: "
                + str(AUDIO_FILE)
            )
        data = json.loads(TIMING_FILE.read_text(encoding="utf-8"))
        self.marker_times = {
            row["name"]: float(row["time_seconds"])
            for row in data["markers"]
        }
        self.audio_duration = float(data["audio_duration_seconds"])
        self.add_sound(
            str(AUDIO_FILE),
            time_offset=VOICE_OFFSET_SECONDS,
        )

    def sync_to(self, marker_name: str):
        target = VOICE_OFFSET_SECONDS + self.marker_times[marker_name]
        current = float(self.renderer.time)
        delta = target - current
        if delta > 0.001:
            self.wait(delta)
        elif delta < -0.25:
            print(
                f"[SYNC WARN] {marker_name}: visual timeline "
                f"{-delta:.3f}s late"
            )

    def sync_between(self, start_marker: str, end_marker: str, fraction: float):
        """Sincroniza a una fracción estable del intervalo entre dos marcadores."""
        start = self.marker_times[start_marker]
        end = self.marker_times[end_marker]
        voice_target = start + fraction * (end - start)
        target = VOICE_OFFSET_SECONDS + voice_target
        current = float(self.renderer.time)
        delta = target - current
        if delta > 0.001:
            self.wait(delta)
        elif delta < -0.25:
            print(
                f"[SYNC WARN] {start_marker}->{end_marker} "
                f"@{fraction:.2f}: visual timeline {-delta:.3f}s late"
            )

    def replace_section_title(self, text: str):
        """Sustituye el encabezado superior sin tocar el contenido central."""
        old = getattr(self, "_current_header", None)
        title = Tex(text, color=FG).scale(0.82).to_edge(UP, buff=0.35)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=MUTED, stroke_width=1.2)
        rule.next_to(title, DOWN, buff=0.18)
        new_header = VGroup(title, rule)

        animations = [FadeIn(title), Create(rule)]
        if old is not None:
            animations.insert(0, FadeOut(old))
        self.play(*animations, run_time=0.45)
        self._current_header = new_header

    def axiom_recap_panel(self, group: str) -> VGroup:
        """Paneles que acompañan la recapitulación verbal previa a la tabla final."""
        data = {
            "additive": [
                ("1", "Asociatividad", r"a+(b+c)=(a+b)+c"),
                ("2", "Neutro aditivo", r"a+0=a"),
                ("3", "Inverso aditivo", r"a+(-a)=0"),
                ("4", "Conmutatividad", r"a+b=b+a"),
            ],
            "multiplicative": [
                ("5", "Asociatividad", r"a\cdot(b\cdot c)=(a\cdot b)\cdot c"),
                ("6", "Neutro multiplicativo", r"a\cdot1=a"),
                ("7", "Inverso multiplicativo", r"a\cdot a^{-1}=1\quad(a\neq0)"),
                ("8", "Conmutatividad", r"a\cdot b=b\cdot a"),
            ],
            "distributive": [
                ("9", "Distributividad", r"a\cdot(b+c)=a\cdot b+a\cdot c"),
            ],
        }

        rows = VGroup()
        for number, name, formula in data[group]:
            badge = MathTex(number, color=MUTED).scale(0.72)
            label = Tex(name, color=FG).scale(0.62)
            expr = MathTex(formula, color=FG).scale(
                0.72 if group != "distributive" else 0.92
            )
            row = VGroup(badge, label, expr).arrange(
                RIGHT,
                buff=0.42,
                aligned_edge=DOWN,
            )
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.48)
        if group == "distributive":
            rows.move_to([0, -0.25, 0])
        else:
            rows.move_to([0, -0.35, 0])
        return rows

    def integer_field_audit_cards(self) -> VGroup:
        """Auditoría visual de los axiomas que sí satisfacen los enteros."""
        def card(title_text, formulas, accent):
            box = RoundedRectangle(
                width=6.2,
                height=1.25,
                corner_radius=0.12,
                color=accent,
                stroke_width=1.5,
            )
            title = Tex(title_text, color=accent).scale(0.56)
            body = VGroup(
                *[MathTex(formula, color=FG).scale(0.56) for formula in formulas]
            ).arrange(RIGHT, buff=0.42)
            title.move_to(box.get_center() + 0.34 * UP)
            body.move_to(box.get_center() + 0.22 * DOWN)
            return VGroup(box, title, body)

        additive = card(
            "Suma — cumple",
            [
                r"a+(b+c)=(a+b)+c",
                r"a+b=b+a",
                r"a+0=a",
                r"a+(-a)=0",
            ],
            GREEN,
        )

        multiplicative = card(
            "Producto — cumple parcialmente",
            [
                r"a\cdot(b\cdot c)=(a\cdot b)\cdot c",
                r"a\cdot b=b\cdot a",
                r"a\cdot1=a",
            ],
            BLUE,
        )

        distributive = card(
            "Distributividad — cumple",
            [r"a\cdot(b+c)=a\cdot b+a\cdot c"],
            VIOLET,
        )

        inverse = card(
            "Inverso multiplicativo — falta comprobar",
            [r"a\neq0\Longrightarrow a^{-1}\in\mathbb Z\ ?"],
            ORANGE,
        )

        cards = VGroup(
            additive,
            multiplicative,
            distributive,
            inverse,
        ).arrange(DOWN, buff=0.20)
        cards.scale(0.82).move_to([2.25, -0.30, 0])
        return cards

    def pending_consequences_panel(self) -> VGroup:
        """Inventario completo de reglas mencionadas pero aún no disponibles."""
        specs = [
            (r"a\cdot0=0", 0.82),
            (r"-(-a)=a", 0.82),
            (r"(-a)\cdot(-b)=a\cdot b", 0.82),
            (r"a+c=b+c\Longrightarrow a=b", 0.76),
            (r"a\cdot c=b\cdot c,\ c\neq0\Longrightarrow a=b", 0.70),
            (r"a\cdot b=0\Longrightarrow a=0\ \text{o}\ b=0", 0.70),
            (r"a-b\ ?\qquad \frac{a}{b}\ ?", 0.82),
        ]

        rows = VGroup()
        for formula, scale in specs:
            expr = MathTex(formula, color=FG).scale(scale)
            q = MathTex(r"?", color=ORANGE).scale(0.92)
            if formula.endswith(r"\ ?"):
                # La propia fórmula ya expresa que resta/división siguen sin definir.
                row = VGroup(expr)
            else:
                q.next_to(expr, RIGHT, buff=0.28)
                row = VGroup(expr, q)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        rows.move_to([0, -0.38, 0])
        return rows

    def not_yet_order_panel(self) -> VGroup:
        """Conceptos que aún no forman parte de la estructura de cuerpo."""
        rows = VGroup(
            VGroup(
                Tex("Orden", color=FG).scale(0.66),
                MathTex(r"2<3", color=ORANGE).scale(0.96),
            ),
            VGroup(
                Tex("Positividad", color=FG).scale(0.66),
                MathTex(r"x>0,\qquad x<0", color=MUTED).scale(0.82),
            ),
            VGroup(
                Tex("Intervalos", color=FG).scale(0.66),
                MathTex(r"(a,b),\qquad [a,b]", color=MUTED).scale(0.82),
            ),
            VGroup(
                Tex("Cotas, máximos y supremos", color=FG).scale(0.66),
                MathTex(r"\sup A,\qquad \max A", color=MUTED).scale(0.82),
            ),
            VGroup(
                Tex("Completitud", color=FG).scale(0.66),
                MathTex(r"?", color=ORANGE).scale(0.96),
            ),
        )
        for row in rows:
            row.arrange(RIGHT, buff=0.55)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.move_to([0, -0.35, 0])
        return rows

    def field_universality_panel(self) -> VGroup:
        """Lo demostrado sólo desde los axiomas vale en todo cuerpo."""
        source = RoundedRectangle(
            width=5.4,
            height=1.3,
            corner_radius=0.14,
            color=BLUE,
            stroke_width=2.0,
        ).move_to([0, 1.25, 0])
        source_text = VGroup(
            Tex("Axiomas de cuerpo", color=BLUE).scale(0.72),
            MathTex(r"(F,+,\cdot,0,1)", color=FG).scale(0.72),
        ).arrange(DOWN, buff=0.16).move_to(source)

        theorem = Tex(
            "Teorema demostrado sólo con estos axiomas",
            color=FG,
        ).scale(0.64).move_to([0, -0.10, 0])

        examples = VGroup(
            MathTex(r"F_2", color=ORANGE).scale(1.05),
            MathTex(r"\mathbb Q", color=GREEN).scale(1.05),
            MathTex(r"\mathbb R", color=VIOLET).scale(1.05),
        ).arrange(RIGHT, buff=1.55).move_to([0, -1.45, 0])

        arrows = VGroup(
            Arrow(
                theorem.get_bottom(),
                examples[0].get_top(),
                buff=0.12,
                stroke_width=1.6,
                color=MUTED,
            ),
            Arrow(
                theorem.get_bottom(),
                examples[1].get_top(),
                buff=0.12,
                stroke_width=1.6,
                color=MUTED,
            ),
            Arrow(
                theorem.get_bottom(),
                examples[2].get_top(),
                buff=0.12,
                stroke_width=1.6,
                color=MUTED,
            ),
        )
        return VGroup(source, source_text, theorem, examples, arrows)

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
        self.hold(1.80)
        proposition = MathTex(
            r"a+(b+c)=(a+b)+c",
            color=FG,
        ).scale(1.35)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        proposition.set_color_by_tex("c", GREEN)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        return proposition

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
        return expr

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
        return expr

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
        self.hold(1.80)
        proposition = MathTex(r"a+b=b+a", color=FG).scale(1.45)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        return proposition

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
        self.hold(1.80)
        proposition = MathTex(
            r"a\cdot(b\cdot c)=(a\cdot b)\cdot c",
            color=FG,
        ).scale(1.28)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        proposition.set_color_by_tex("c", GREEN)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        return proposition

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
        return expr

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
        return VGroup(hypothesis, expr)

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
        self.hold(1.80)
        proposition = MathTex(r"a\cdot b=b\cdot a", color=FG).scale(1.4)
        proposition.set_color_by_tex("a", BLUE)
        proposition.set_color_by_tex("b", ORANGE)
        self.play(FadeOut(source), FadeIn(proposition))
        self.hold(0.55)
        return proposition

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
        self.hold(1.80)

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
        self.sync_to("c01v01-22-factor-comun")
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
        self.hold(1.80)
        proposition_back = MathTex(
            r"a\cdot b+a\cdot c=a\cdot(b+c)",
            color=FG,
        ).scale(1.28)
        proposition_back.set_color_by_tex("a", BLUE)
        proposition_back.set_color_by_tex("b", ORANGE)
        proposition_back.set_color_by_tex("c", GREEN)
        self.play(FadeOut(source), FadeIn(proposition_back))
        self.hold(0.55)
        return proposition_back

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
        return VGroup(condition, rows)

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

        self.sync_to("c01v01-29-f2-tablas")
        self.play(Create(add_table), Create(mul_table), run_time=1.5)

        self.sync_to("c01v01-30-f2-suma")
        add_highlight = SurroundingRectangle(
            add_table.get_entries((3, 3)),
            color=ORANGE,
            buff=0.10,
        )
        sum_result = MathTex(r"1+1=0", color=ORANGE).scale(1.05)
        sum_result.to_edge(DOWN, buff=0.75)
        self.play(Create(add_highlight), FadeIn(sum_result))

        self.sync_to("c01v01-31-f2-producto")
        self.play(FadeOut(add_highlight), FadeOut(sum_result), run_time=0.35)
        mul_highlight = SurroundingRectangle(
            mul_table.get_entries((3, 3)),
            color=GREEN,
            buff=0.10,
        )
        mul_result = MathTex(
            r"1\cdot1=1", r"\qquad", r"1^{-1}=1",
            color=GREEN,
        ).scale(0.98).to_edge(DOWN, buff=0.75)
        self.play(Create(mul_highlight), FadeIn(mul_result))

        return VGroup(f2, add_table, mul_table, mul_highlight, mul_result)

