#!/usr/bin/env python3
"""Content conservation, original figures and rendered internal links for IC2021."""
import argparse, hashlib, json, re, subprocess, zipfile
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from generate_sanmartin_web import DEST, expected_files, split_master, ROOT
from sanmartin_archive import ensure_archive

class HTML(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.links=[]; self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='a' and a.get('href'):self.links.append(a['href'])
        if tag=='img':self.images.append(a)

def ast(text):
    return json.loads(subprocess.check_output(['quarto','pandoc','--from=markdown','--to=json'],input=text.encode()))
def nodes(tree,kind):
    result=[]
    def visit(x):
        if isinstance(x,dict):
            if kind == 'Math' and x.get('t') == 'Image': return  # alt is plain text; caption mathematics remains in Figure
            if x.get('t')==kind:result.append(x['c'])
            for v in x.values():visit(v)
        elif isinstance(x,list):
            for v in x:visit(v)
    visit(tree);return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--site-dir',type=Path);p.add_argument('--report',type=Path);args=p.parse_args()
    with zipfile.ZipFile(ensure_archive()) as z: raw=z.read('master/Introduccion_al_calculo_2021_master.md')
    master=raw.decode();files,parts,chapters=expected_files(master)
    for name,text in files.items():assert (DEST/name).read_text()==text,name
    original=ast(master);derived=ast('\n\n'.join(re.sub(r'\A---\n.*?\n---\n','',files[name],flags=re.S) for name in ['index.qmd',*[f'capitulo-{n:02d}.qmd' for n in range(1,19)],'apendices.qmd']))
    original_math=nodes(original['blocks'],'Math');web_math=nodes(derived['blocks'],'Math')
    assert original_math==web_math,'Formula loss/change/order mismatch'
    original_images=nodes(original['blocks'],'Image'); assert len(original_images)==177
    inventory=[];headers=[]
    for c in chapters:
        name=f'capitulo-{c["number"]:02d}.qmd'
        headings=re.findall(r'(?m)^#{3,6} (.+)$',c['body']);headers.extend(headings)
        for i,(caption,path) in enumerate(re.findall(r'!\[([^\n]*)\]\((figuras/[^)]+)\)',c['body']),1):
            payload=(DEST/path).read_bytes()
            inventory.append({'chapter':c['number'],'section_source':name,'figure_id':f'fig-ic2021-c{c["number"]:02d}-f{i:02d}','path':path,'caption':caption,'sha256':hashlib.sha256(payload).hexdigest(),'bytes':len(payload)})
    assert len(inventory)==177 and len({i['path'] for i in inventory})==177
    report={'master_sha256':hashlib.sha256(raw).hexdigest(),'parts':parts,'chapters':[{'number':c['number'],'title':c['title'],'headings':re.findall(r'(?m)^#{3,6} (.+)$',c['body'])} for c in chapters], 'math_nodes_preserved':len(original_math),'math_sha256':hashlib.sha256(json.dumps(original_math).encode()).hexdigest(),'chapter_sections_preserved':len(headers),'source_markers':{word:len(re.findall(r'\*\*'+word,master)) for word in ['Definición','Teorema','Proposición','Demostración','Ejercicio','Solución']},'figures':inventory,'source_equivalence':'PASS'}
    if args.site_dir:
        site=args.site_dir.resolve();book=site/DEST.relative_to(ROOT);parsed={}
        for name in files:
            page=book/Path(name).with_suffix('.html');html=HTML();html.feed(page.read_text());parsed[page]=html
        for page,html in parsed.items():
            for href in html.links:
                u=urlsplit(href)
                if u.scheme or u.netloc or not u.path and not u.fragment:continue
                target=(site/u.path.lstrip('/') if u.path.startswith('/') else page.parent/unquote(u.path)).resolve() if u.path else page
                if target.is_dir():target=target/'index.html'
                # Global navigation is outside the book-only render. Book links must exist.
                if target.is_relative_to(book) or 'san-martin' in u.path:
                    assert target.is_file(),(page,href)
                    if u.fragment and target.suffix=='.html':
                        other=parsed.get(target)
                        if other is None:other=HTML();other.feed(target.read_text())
                        assert unquote(u.fragment) in other.ids,(page,href)
            for img in html.images:
                if not img.get('src','').startswith('figuras/'):continue
                assert img.get('alt'),(page,img)
                assert (page.parent/unquote(img['src'])).is_file(),(page,img)
        report['rendered_pages']=len(parsed);report['internal_links_and_images']='PASS'
    if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'IC2021 PASS: 5 parts, 18 chapters, 177 figures, {len(original_math)} mathematical expressions preserved, {len(headers)} sections')
if __name__=='__main__':main()
