import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, MagicMock

import numpy as np
import soundfile as sf
from ma_voice.core import (ROOT, PROFILE_DIR, profile, prepare_script, cache_payload, signature,
                           cached, publish_clip, assemble, digest, write_json)
from ma_voice.pronunciation import load, normalize
from ma_voice.manim_timing import VoiceTimeline
from ma_voice.backends import QwenBase


class VoiceTests(unittest.TestCase):
    def setUp(self):
        self.dictionary = load()
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        # Windows indexing/antivirus can briefly retain newly written media.
        import time
        for attempt in range(3):
            try:
                self.temp.cleanup()
                return
            except OSError:
                if attempt == 2:
                    raise
                time.sleep(.1)

    def cue(self, text='Hola.', **kwargs):
        return {'id': 'a', 'texto': text, 'pausa': 1, **kwargs}

    def audio(self):
        path = self.root/'test.wav'
        sf.write(path, np.sin(np.arange(2400)*.1)*.1, 24000, subtype='FLOAT')
        return path

    def test_approved_profile_and_assets(self):
        p = profile()
        self.assertEqual(p['approval'], 'approved_by_author')
        self.assertEqual(p['approved_narration_sha256'], '87acdafe6e5ef954017af57b9c6c246b2a7db34edcf1623d4ba4692c979a0586')

    def test_reference_tamper_blocks(self):
        from ma_voice.core import digest as real_digest
        def changed(path):
            return 'wrong' if Path(path).name == 'referencia.wav' else real_digest(path)
        with patch('ma_voice.core.digest', side_effect=changed), self.assertRaises(ValueError):
            profile()

    def test_index(self):
        self.assertEqual(normalize('$a_n$ y $b_{n+1}$.', self.dictionary), 'a sub ene y be sub ene más uno.')

    def test_exponents(self):
        self.assertEqual(normalize('$x^2$, $z^{3}$ y $x^n$.', self.dictionary), 'equis al cuadrado, zeta al cubo y equis elevado a ene.')

    def test_symbols_algebra_names(self):
        self.assertEqual(normalize('Euler: $x+y$ $≠$ $∞$.', self.dictionary, ['Euler']), 'Óiler: equis más ye es distinto de infinito.')

    def test_ambiguous_math_blocks(self):
        for text in ('$a_{n+2}$', '$x^{2$', 'x^2', '$q_n$', '1/2', r'\frac{1}{2}', 'x²', '$x+y+z$'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                normalize(text, self.dictionary)

    def test_unknown_required_name(self):
        with self.assertRaises(ValueError):
            normalize('Gauss.', self.dictionary, ['Gauss'])

    def test_custom_dictionary(self):
        d = copy.deepcopy(self.dictionary)
        d['expresiones']['a_{n+2}'] = 'a sub ene más dos'
        self.assertEqual(normalize('$a_{n+2}$', d), 'a sub ene más dos')

    def test_duplicate_ids(self):
        with self.assertRaises(ValueError):
            prepare_script({'segmentos': [self.cue(), self.cue()]}, self.dictionary)

    def test_paths_and_negative_pause_rejected(self):
        for cue in (self.cue(id='../escape'), self.cue(pausa=-1), self.cue(pausa=float('nan'))):
            with self.assertRaises(ValueError):
                prepare_script({'segmentos': [cue]}, self.dictionary)

    def test_canonical_text_preserved(self):
        cue = self.cue('$x^2$')
        result = prepare_script({'segmentos': [cue]}, self.dictionary)[0]
        self.assertEqual(result['texto'], '$x^2$')
        self.assertEqual(result['hablado'], 'equis al cuadrado')

    def test_cache_key_tracks_identity_and_parameters(self):
        p = profile()
        a = cache_payload('Hola', 'qwen-base', p, self.dictionary, {'v': 1})
        for field in ('text', 'engine', 'profile', 'dictionary', 'backend', 'reference_sha256', 'seed', 'batch_size'):
            b = copy.deepcopy(a)
            b[field] = 'changed'
            self.assertNotEqual(signature(a), signature(b))

    def test_corrupted_cache_blocks(self):
        payload = {'text': 'hola'}
        path = publish_clip(self.root/'cache', payload, self.audio(), {'test': True})
        self.assertEqual(path, cached(path.parent, signature(payload)))
        path.write_bytes(b'corrupt')
        with self.assertRaises(ValueError):
            cached(path.parent, signature(payload))

    def test_assembly_and_manim_markers(self):
        cues = prepare_script({'segmentos': [self.cue()]}, self.dictionary)
        path = self.audio()
        out = self.root/'output'
        result = assemble(cues, [path], out, offset=7)
        self.assertAlmostEqual(result['duracion_total'], 1.1)
        markers = self.root/'markers.json'
        write_json(markers, {'audio_sha256': result['sha256'], 'markers': [
            {'id': 'reveal', 'cue_id': 'a', 'voice_seconds': .05, 'basis': 'author'}]})
        timeline = VoiceTimeline(out/'timing.json', out/'narracion.wav', markers)
        self.assertEqual(timeline.cue_start('a'), 7)
        self.assertEqual(timeline.semantic_time('reveal'), 7.05)
        with self.assertRaises(KeyError):
            timeline.semantic_time('missing')
        scene = MagicMock(time=7.06)
        timeline.wait_until(scene, 7.08)
        scene.wait.assert_called_once()
        with self.assertRaises(ValueError):
            timeline.wait_until(scene, 6)

    def test_output_not_overwritten(self):
        with self.assertRaises(FileExistsError):
            assemble([], [], self.root)

    def test_nan_audio_rejected(self):
        path = self.root/'nan.wav'
        sf.write(path, np.array([np.nan]), 24000, subtype='FLOAT')
        with self.assertRaises(ValueError):
            assemble([self.cue(hablado='Hola.')], [path], self.root/'out')

    def test_clipping_rejected(self):
        path = self.root/'clipped.wav'
        sf.write(path, np.array([1.0]), 24000, subtype='FLOAT')
        with self.assertRaises(ValueError):
            assemble([self.cue(hablado='Hola.')], [path], self.root/'out')

    def test_markers_must_match_wav(self):
        cues = prepare_script({'segmentos': [self.cue()]}, self.dictionary)
        out = self.root/'out'
        assemble(cues, [self.audio()], out)
        marker = self.root/'marker.json'
        write_json(marker, {'audio_sha256': 'wrong', 'markers': []})
        with self.assertRaises(ValueError):
            VoiceTimeline(out/'timing.json', out/'narracion.wav', marker)

    def test_duplicate_unreviewed_out_of_bounds_markers(self):
        cues = prepare_script({'segmentos': [self.cue()]}, self.dictionary)
        out = self.root/'out'
        result = assemble(cues, [self.audio()], out)
        marker = self.root/'marker.json'
        m = {'id': 'a', 'cue_id': 'a', 'voice_seconds': .05, 'basis': 'author'}
        for markers in ([m, m], [{**m, 'basis': 'automatic_unreviewed'}], [{**m, 'voice_seconds': .5}]):
            write_json(marker, {'audio_sha256': result['sha256'], 'markers': markers})
            with self.assertRaises(ValueError):
                VoiceTimeline(out/'timing.json', out/'narracion.wav', marker)

    def test_worker_uses_only_fixed_prompt_base_api(self):
        worker = object.__new__(QwenBase)
        worker.profile, worker.torch, worker.model = profile(), MagicMock(), MagicMock()
        worker.prompt = ['protected-prompt']
        worker.model.generate_voice_clone.return_value = ([np.array([.1])], 24000)
        worker.generate('Hola.')
        worker.model.generate_voice_clone.assert_called_once_with(text=['Hola.'], language='Spanish', voice_clone_prompt=['protected-prompt'], max_new_tokens=768)
        worker.model.generate_voice_design.assert_not_called()
        worker.torch.manual_seed.assert_called_once_with(20261023)

    def test_alternative_exact_sample_limits(self):
        alt, sr = sf.read(PROFILE_DIR/'alternativa_inicial_direct_exact.wav', dtype='int32')
        direct, rate = sf.read(ROOT/'experimentos/MA_VOICE_003/escucha/NARRACION_direct.wav', dtype='int32', frames=552960)
        self.assertEqual(sr, 48000)
        self.assertEqual(rate, sr)
        self.assertEqual(len(alt), 552960)
        np.testing.assert_array_equal(alt, direct)


if __name__ == '__main__':
    unittest.main()
