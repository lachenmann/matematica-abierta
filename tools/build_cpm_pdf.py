"""Build CPM's amsbook derivatives from an identified raw Markdown snapshot."""
from pathlib import Path
import argparse,hashlib,json,re,shutil,subprocess
p=argparse.ArgumentParser();p.add_argument('canonical',type=Path);p.add_argument('--template',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--figures',type=Path,required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[1];a.output.mkdir(parents=True,exist_ok=True)
(a.output/'chapters').mkdir(exist_ok=True);(a.output/'markdown').mkdir(exist_ok=True)
shutil.copytree(a.figures,a.output/'figures',dirs_exist_ok=True)
shutil.copy(a.template/'references.bib',a.output/'references.bib')
labels=json.loads((root/'data/cpm-tome-i-reference-labels.json').read_text())
manifest={'title':'Cálculo para matemáticos — Tomo I','edition_date':'2026-10-16','author':'A. Peña','protocol':'MA-PDF v1.0','review':'R05','chapters':[]}
mathcatalog={}
for n in range(2,22):
    source=a.canonical/f'T1-C{n:02}.md';s=source.read_text();k=n-1
    title=re.search(r'^# (.*?) \{#',s,re.M).group(1)
    manifest['chapters'].append({'chapter':source.stem,'visible':k,'title':title,'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'exercises':len(re.findall(r'\{#exr-',s)),'solutions':len(re.findall(r'\{#sol-',s))})
    s=re.sub(r'\A---\n.*?\n---\n','',s,count=1,flags=re.S)
    def reference(m):
        ident=m[1];label=labels[ident].replace('[',r'\[').replace(']',r'\]')
        return f'[{label}](#{ident})'
    s=re.sub(r'(?<!\w)@((?:sec|def|thm|lem|prp|cor|exm|exr|sol|fig|eq|tbl)-[\w-]+)',reference,s)
    s=s.replace('@jacob-evans-analysis-v1',r'\cite{jacob-evans-analysis-v1}')
    s=s.replace('../90 - Assets/figures/','figures/')
    md=a.output/'markdown'/f'c{k:02}.md';md.write_text(s)
    mathcatalog[str(k)]=re.findall(r'\$\$\s*([\s\S]*?)\s*\$\$',s)
    command=['pandoc',str(md),'-f','markdown+fenced_divs+tex_math_dollars','-t','latex','--top-level-division=chapter','--lua-filter',str(root/'tools/cpm-pdf.lua'),'-o',str(a.output/'chapters'/f'c{k:02}.tex')]
    subprocess.run(command,check=True)
for name in ['main.tex','main-carta.tex']:
    s=(a.template/name).read_text().replace('6 de octubre de 2026','16 de octubre de 2026')
    old=r'\NewEnviron{cpmath}{\sbox{\cpmmathbox}{$\displaystyle\BODY$}\[\ifdim\wd\cpmmathbox>\linewidth\resizebox{\linewidth}{!}{\usebox{\cpmmathbox}}\else\BODY\fi\]}'
    new=r'''\NewEnviron{cpmath}[1]{\sbox{\cpmmathbox}{$\displaystyle\BODY$}%
\ifdim\wd\cpmmathbox>1.11111\linewidth\typeout{CPMWIDE:\thechapter:#1:\the\wd\cpmmathbox:\the\linewidth}\fi
\[\ifdim\wd\cpmmathbox>\linewidth\resizebox{\linewidth}{!}{\usebox{\cpmmathbox}}\else\BODY\fi\]}'''
    if old in s:s=s.replace(old,new)
    else:assert new in s
    if r'\usepackage{upquote}' not in s:s=s.replace(r'\begin{document}',r'\usepackage{upquote}'+'\n'+r'\begin{document}')
    (a.output/name).write_text(s)
(a.output/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(a.output/'math-catalog.json').write_text(json.dumps(mathcatalog,ensure_ascii=False,indent=2))
print('Generated 20 chapters; 800 exercises and 800 solutions.')
