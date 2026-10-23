"""SRT legible por bloques de hasta dos líneas, a partir de las palabras reales."""
from difflib import SequenceMatcher
import json,re,textwrap,unicodedata
from motor_voz import ROOT,EXPORTS,GENERADOS,srt_time

def norm(w):
    w=''.join(c for c in unicodedata.normalize('NFD',w.lower()) if unicodedata.category(c)!='Mn')
    w=re.sub(r'[^a-z0-9]','',w)
    return {'0':'cero','1':'uno','2':'dos','3':'tres','n':'ene','b':'be'}.get(w,w)

def build(timeline):
    alignment=json.loads((GENERADOS/'alineacion_clips.json').read_text(encoding='utf8'))
    assert alignment['guion_sha256']==timeline['guion_sha256']
    aligned={c['id']:c for c in alignment['clips']}
    result=[]
    for cue in timeline['cues']:
        a=aligned[cue['id']];assert a['sha256']==cue['sha256']
        words=cue['texto'].split();actual=a['words'];times={}
        matcher=SequenceMatcher(None,[norm(w) for w in words],[norm(w['word']) for w in actual],autojunk=False)
        for block in matcher.get_matching_blocks():
            for k in range(block.size):times[block.a+k]=actual[block.b+k]['start']
        # Sólo se interpolan límites sin correspondencia ASR, no el contenido.
        times[0]=0.;times[len(words)]=cue['fin_voz']-cue['inicio']
        anchored=set(times)
        for i in range(len(words)):
            if i not in times:
                lo=max(k for k in times if k<i);hi=min(k for k in times if k>i)
                times[i]=times[lo]+(times[hi]-times[lo])*(i-lo)/(hi-lo)
        groups=[];start=0
        while start<len(words):
            end=start+1
            while end<len(words) and len(textwrap.wrap(' '.join(words[start:end+1]),width=42))<=2:end+=1
            # Preferir cerrar una frase si cabe con suficiente texto.
            candidates=[i+1 for i in range(start,end) if words[i].endswith(('.', '?', ':',';')) and len(' '.join(words[start:i+1]))>=30]
            if candidates:end=candidates[-1]
            groups.append((start,end));start=end
        for j,(start,end) in enumerate(groups):
            begin=cue['inicio']+times[start]
            finish=cue['inicio']+times[end]-.025 if end<len(words) else cue['fin_voz']
            assert finish>begin
            lines=textwrap.wrap(' '.join(words[start:end]),width=42);assert len(lines)<=2
            result.append(dict(id=cue['id']+f'-{j+1}',inicio=begin,fin=finish,texto=' '.join(words[start:end]),lineas=lines,metodo_inicio='inicio_cue' if start==0 else ('palabra_ASR' if start in anchored else 'interpolado_entre_palabras_ASR')))
    assert ' '.join(c['texto'] for c in result)==' '.join(c['texto'] for c in timeline['cues'])
    data='\n'.join(f"{i}\n{srt_time(c['inicio'])} --> {srt_time(c['fin'])}\n"+'\n'.join(c['lineas'])+'\n' for i,c in enumerate(result,1))
    for dest in [ROOT/'EXP003_SUBTITULOS.srt',EXPORTS/'EXP003_SUBTITULOS.srt']:dest.write_text(data,encoding='utf8')
    (GENERADOS/'timing_subtitulos.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    return result
if __name__=='__main__':
    t=json.loads((GENERADOS/'timing_produccion.json').read_text(encoding='utf8'));print(len(build(t)),'subtítulos')
