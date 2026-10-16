"""Check that the three canonical ANM downloads match their release and compile inputs."""
from pathlib import Path
import hashlib,json,re,zipfile
root=Path(__file__).resolve().parents[1]
folder=root/'assets/books/anm/downloads'
release=json.loads((folder/'release.json').read_text())
expected={'ANM_A4_Digital_Con_Soluciones_v03.pdf','ANM_Carta_Impresion_Con_Soluciones_v03.pdf','ANM_Overleaf_MA_PDF_v03.zip'}
assert {r['file'] for r in release['files']}==expected
assert release['solutions']==release['exercise_pairs']+release['microcheck_pairs']==3338
for row in release['files']:
    data=(folder/row['file']).read_bytes()
    assert len(data)==row['bytes']
    assert hashlib.sha256(data).hexdigest()==row['sha256']
    if row['file'].endswith('.pdf'):
        assert data.startswith(b'%PDF-') and row['solutions']==3338
with zipfile.ZipFile(folder/'ANM_Overleaf_MA_PDF_v03.zip') as archive:
    assert archive.testzip() is None
    names=set(archive.namelist())
    assert not any(n.startswith('/') or '..' in Path(n).parts for n in names)
    for main,paper in [('main.tex','a4paper'),('main-carta.tex','letterpaper')]:
        text=archive.read(main).decode()
        assert r'\documentclass[11pt,'+paper+r',oneside]{amsbook}' in text
    manifest=json.loads(archive.read('source-manifest.json'))
    assert len(manifest['chapters'])==32
    solutions=0
    for row in manifest['chapters']:
        data=archive.read(row['tex'])
        assert hashlib.sha256(data).hexdigest()==row['tex_sha256']
        text=data.decode();solutions+=text.count(r'\begin{ANMSolution}')
        assert not re.search(r"\\chapter\{(?:\\texorpdfstring\{)?`Capítulo",text)
    assert solutions==3338
    for figure in manifest['figures']:
        assert hashlib.sha256(archive.read(figure['path'])).hexdigest()==figure['sha256']
print('ANM downloads PASS: two canonical PDFs, 3,338 solutions and self-contained AMS Book Overleaf archive')
