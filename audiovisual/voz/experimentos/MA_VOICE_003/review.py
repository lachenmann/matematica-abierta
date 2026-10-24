import pathlib,json,re,unicodedata,difflib
R=pathlib.Path(__file__).resolve().parent
script=json.loads((R/'guion.json').read_text(encoding='utf8'))['segmentos']
def tokens(text):
    for a,b in [('1.000.000','un millón'),('1,000,000','un millón'),('1000000','un millón'),('1.000.001','un millón más uno'),('1000001','un millón más uno'),('1.000.002','un millón más dos'),('1000002','un millón más dos')]: text=text.replace(a,b)
    text=''.join(c for c in unicodedata.normalize('NFD',text.lower()) if unicodedata.category(c)!='Mn')
    return [{'n':'ene','b':'be','0':'cero','1':'uno','2':'dos','3':'tres','4':'cuatro'}.get(w,w) for w in re.findall(r'[a-z0-9]+',text)]
out=[]
for mode in ['clone','direct']:
    a=json.loads((R/'evidencia'/f'alineacion_{mode}.json').read_text(encoding='utf8'))
    for cue,actual in zip(script,a['clips']):
        assert cue['id']==actual['id']; expected=tokens(cue['texto']); recognized=tokens(actual['text']); matcher=difflib.SequenceMatcher(None,expected,recognized,autojunk=False)
        differences=[{'op':tag,'expected':' '.join(expected[a:b]),'asr':' '.join(recognized[c:d])} for tag,a,b,c,d in matcher.get_opcodes() if tag!='equal']
        out.append({'mode':mode,'id':cue['id'],'expected':cue['texto'],'recognized':actual['text'],'token_ratio':matcher.ratio(),'differences':differences,'status':'ASR evidence only; perceptual review pending'})
(R/'evidencia/revision_lectura.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps([{'mode':x['mode'],'id':x['id'],'ratio':x['token_ratio'],'differences':x['differences']} for x in out],ensure_ascii=True),flush=True)
