"""Standard-library-only adapter, safe to import inside canonical Manim."""
import hashlib
import json
from pathlib import Path


class VoiceTimeline:
    def __init__(self, timing_path, narration_path, markers_path=None):
        self.data = json.loads(Path(timing_path).read_text(encoding='utf8'))
        self.sha = hashlib.sha256(Path(narration_path).read_bytes()).hexdigest()
        if self.sha != self.data['sha256']:
            raise ValueError('Timing no corresponde al WAV')
        self.cues = {}
        last = 0
        for cue in self.data['cues']:
            if cue['id'] in self.cues or not last <= cue['inicio'] <= cue['fin_voz'] <= cue['fin']:
                raise ValueError('Cues duplicados, solapados o inválidos')
            self.cues[cue['id']] = cue
            last = cue['fin']
        self.markers = {}
        if markers_path:
            data = json.loads(Path(markers_path).read_text(encoding='utf8'))
            if data['audio_sha256'] != self.sha:
                raise ValueError('Marcadores de otro audio')
            for marker in data['markers']:
                cid, t = marker['cue_id'], float(marker['voice_seconds'])
                cue = self.cues[cid]
                if marker['id'] in self.markers or not cue['inicio'] <= t <= cue['fin_voz']:
                    raise ValueError('Marcador duplicado o fuera del tramo de voz')
                if marker.get('basis') not in ('author', 'reviewed_word_alignment'):
                    raise ValueError('Marcador semántico requiere fuente explícita y revisada')
                self.markers[marker['id']] = t

    def cue_start(self, cue_id):
        return self.cues[cue_id]['inicio'] + self.data['offset_video']

    def semantic_time(self, marker_id):
        # No percentage or guessed fallback: important reveals must use verified markers.
        return self.markers[marker_id] + self.data['offset_video']

    def wait_until(self, scene, absolute_time):
        remaining = absolute_time - float(scene.time)
        if remaining < -1 / self.data['fps']:
            raise ValueError(f'SYNC WARN: cue pasado {remaining:.3f}s')
        if remaining > 0:
            scene.wait(remaining)
