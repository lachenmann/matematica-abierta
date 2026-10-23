"""Entrega verificable: fuentes, recursos institucionales y clips exactos."""
from pathlib import Path
import json,zipfile,subprocess,time
from motor_voz import ROOT,GENERADOS,EXPORTS,sha256_file

def main():
    t=json.loads((GENERADOS/'timing_produccion.json').read_text(encoding='utf8'))
    files=[f for f in ROOT.iterdir() if f.is_file() and f.suffix in ('.py','.ps1','.md','.json','.toml','.lock','.srt')]
    files += [ROOT/'.gitignore',ROOT/'.python-version']
    files += list((ROOT/'recursos').glob('*.py'))+list((ROOT/'recursos').glob('*.md'))+list((ROOT/'recursos').glob('*.wav'))
    files += list(GENERADOS.glob('*.json'))
    for c in t['cues']:
        clip=ROOT/c['audio'];assert sha256_file(clip)==c['sha256'];files += [clip,clip.with_suffix('.json')]
    files += list((EXPORTS/'qa-final').glob('*.json'))
    commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    inventory={f.relative_to(ROOT).as_posix():sha256_file(f) for f in sorted(set(files))}
    zpath=ROOT/'EXP003_FUENTES.zip'
    with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
        for name in inventory:z.write(ROOT/name,name)
        z.writestr('INVENTARIO_SHA256.json',json.dumps(inventory,indent=2))
        z.writestr('COMMIT.txt',commit+'\n')
    artifacts=[ROOT/n for n in ('EXP003_FINAL.mp4','EXP003_AUDIO.wav','EXP003_SUBTITULOS.srt','EXP003_FUENTES.zip')]
    data={'commit':commit,'archivos':[{'path':str(f),'bytes':f.stat().st_size,'sha256':sha256_file(f)} for f in artifacts]}
    data['segundos_hasta_empaquetado']=time.time()-json.loads((GENERADOS/'inicio.json').read_text())['unix']
    (EXPORTS/'ENTREGA.json').write_text(json.dumps(data,indent=2),encoding='utf8')
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
