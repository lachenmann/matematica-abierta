"""Import this adapter only; synthesize beforehand with the isolated voice worker."""
import sys
from pathlib import Path
from manim import Scene, MathTex, Write

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ma_voice.manim_timing import VoiceTimeline


class EjemploVoz(Scene):
    def construct(self):
        out = Path(__file__).parent/'salida'
        voice = VoiceTimeline(out/'timing.json', out/'narracion.wav', out/'marcadores.json')
        self.add_sound(str(out/'narracion.wav'), time_offset=voice.data['offset_video'])
        # This marker must be measured in the generated WAV and reviewed first.
        voice.wait_until(self, voice.semantic_time('regla_pronunciada'))
        self.play(Write(MathTex(r'f(x)=x^2')))
