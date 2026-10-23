import json
import tempfile
from pathlib import Path
import wave
import unittest
from unittest import mock
from demo import build_timeline, srt_time, voice_signature, audio_seconds

ROOT=Path(__file__).resolve().parent

class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.guion=json.loads((ROOT/'guion.json').read_text(encoding='utf-8'))
    def test_silent_plan(self):
        data=build_timeline(self.guion,[None]*4,'silencio')
        self.assertEqual(data['duracion_total'],42.0)
        self.assertEqual([x['inicio'] for x in data['segmentos']],[0,8,18,30])
        self.assertEqual(data['qa'],'PROTOTIPO_NO_AUDITADO')
    def test_reject_wrong_visual_order(self):
        self.guion['segmentos'][1]['visual']='incorrecto'
        with self.assertRaises(ValueError):
            build_timeline(self.guion,[None]*4,'silencio')
    def test_time_code(self):
        self.assertEqual(srt_time(62.345),'00:01:02,345')
    def test_real_wav_length(self):
        with tempfile.TemporaryDirectory() as d:
            wav=Path(d)/'test.wav'
            with wave.open(str(wav),'wb') as f:
                f.setnchannels(1);f.setsampwidth(2);f.setframerate(24000)
                f.writeframes(b'\0\0'*24000*3)
            self.assertAlmostEqual(audio_seconds(wav),3.0)
            data=build_timeline(self.guion,[wav]*4,'kokoro')
            self.assertEqual(data['duracion_total'],42.0)
    def test_audio_expands_stage(self):
        with mock.patch('demo.audio_seconds', return_value=17.0):
            plan=build_timeline(self.guion,[Path('fake.wav')]*4,'kokoro')
            self.assertAlmostEqual(plan['duracion_total'],72.8)
    def test_voice_cache_invalidation(self):
        with tempfile.TemporaryDirectory() as d:
            m=Path(d)/'model.onnx';m.write_bytes(b'ab')
            a=voice_signature('hola','em_alex',0.94,m)
            b=voice_signature('hola','em_alex',1.0,m)
            self.assertNotEqual(a,b)

if __name__=='__main__': unittest.main()
