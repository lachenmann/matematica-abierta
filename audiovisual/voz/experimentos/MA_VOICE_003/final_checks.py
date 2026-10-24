import pathlib,json,hashlib,difflib
from html.parser import HTMLParser
R=pathlib.Path(__file__).resolve().parent
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
    return h.hexdigest()
profile=json.loads((R/'VOICE_PROFILE.json').read_text(encoding='utf8'));levels=json.loads((R/'evidencia/sonoridad.json').read_text())
checks={'reference_unchanged':sha(R/profile['reference_audio'])==profile['reference_sha256'],'prompt_unchanged':sha(R/profile['prompt_cache'])==profile['prompt_cache_sha256']}
for mode,x in levels.items():checks['narration_'+mode+'_unchanged']=sha(R/'escucha'/f'NARRACION_{mode}.wav')==x['sha256']
for name in ['eventos','anclajes']:
    before=R/'evidencia'/f'{name}_antes_correccion_0.json';after=R/'demo/generados'/('eventos_visuales.json' if name=='eventos' else 'anclajes_resueltos.json')
    checks[name+'_timing_unchanged']=json.loads(before.read_text(encoding='utf8'))==json.loads(after.read_text(encoding='utf8'))
for x in json.loads((R/'evidencia/proteccion.json').read_text()):checks['original_'+pathlib.Path(x['source']).parent.name+'_'+pathlib.Path(x['source']).name]=sha(pathlib.Path(x['source']))==x['sha256']
class Links(HTMLParser):
    def __init__(self):super().__init__();self.sources=[]
    def handle_starttag(self,tag,attrs):
        if tag in ['audio','video']:self.sources.append(dict(attrs)['src'])
parser=Links();parser.feed((R/'ESCUCHA.html').read_text(encoding='utf8'))
checks['all_media_links_exist']=len(parser.sources)==40 and all((R/s).is_file() and (R/s).stat().st_size>0 for s in parser.sources)
manifest=R/'evidencia/integracion_fuentes.json';m=json.loads(manifest.read_text())
m['copy_sha256']=sha(R/'demo/escena.py');m['animations']='original animation sequence and composition; one index label position corrected'
m['spatial_adaptations']=[{'object':'zero label','from':[-5,-.3,0],'to':[-5,-.7,0],'reason':'separate label from inherited green rectangle border'}]
m['caption_adaptations']=[{'asr':'Asubn','canonical_start':'a','reason':'anchor caption at the actual compound-word onset'}]
manifest.write_text(json.dumps(m,indent=2),encoding='utf8')
original=pathlib.Path(m['source_scene']);copy=R/'demo/escena.py'
diff=''.join(difflib.unified_diff(original.read_text(encoding='utf8').splitlines(True),copy.read_text(encoding='utf8').splitlines(True),fromfile='EXP003 original',tofile='MA-VOICE-003 copy'))
(R/'evidencia/cambios_escena.diff').write_text(diff,encoding='utf8')
(R/'evidencia/final_checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
assert all(checks.values()),checks
print(json.dumps(checks),flush=True)
