"""Revisión explícita de variantes de notación del ASR; conserva el bruto."""
from pathlib import Path
import json,re,unicodedata
from difflib import SequenceMatcher
from motor_voz import ROOT,EXPORTS,GENERADOS,sha256_file

def tokens(s):
    s=s.lower().replace('asiguen','a siguen')
    s=''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn')
    return [{'n':'ene','b':'be','0':'cero','1':'uno','2':'dos','3':'tres'}.get(w,w) for w in re.findall(r'[a-z0-9]+',s)]

def main():
    raw=json.loads((EXPORTS/'qa-final/transcripcion-asr.json').read_text(encoding='utf8'))
    assert raw['master_sha256']==sha256_file(ROOT/'EXP003_FINAL.mp4')
    a,b=tokens(raw['texto_esperado']),tokens(raw['texto_reconocido'])
    diff=[dict(op=op,esperado=a[i:j],reconocido=b[k:l]) for op,i,j,k,l in SequenceMatcher(None,a,b,autojunk=False).get_opcodes() if op!='equal']
    result={'master_sha256':raw['master_sha256'],'variantes_brutas':raw['diferencias_normalizadas'],'reglas_explicitas':['tildes qué/que','n/ene y b/be','dígitos0–3','asiguen/a siguen (segmentación)'],'diferencias_tras_revision':diff,'escucha_humana':False}
    (GENERADOS/'revision_asr_final.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    print('Variaciones brutas',len(raw['diferencias_normalizadas']),'diferencias tras revisión',diff)
    assert not diff
if __name__=='__main__':main()
