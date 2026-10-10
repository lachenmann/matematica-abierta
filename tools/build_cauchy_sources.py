from pathlib import Path
import re, os
ROOT=Path.cwd(); R=ROOT/'teoria/resultados'; LAB=R/'interactive'
src=Path(os.environ['MA_CS_ARTICLE']).read_text(encoding='utf8')
front,body=src.split('---',2)[1:]
front=front.replace('status: working-draft','status: review').replace('publication-state: "not-published; awaiting editorial and mathematical review"','publication-state: "web-source"')
front=front.replace('"Manuscrito canónico de trabajo; progresión de sumas elementales a productos internos, basada en lectura crítica de Labbé y Steele, bajo MA-PED v1.0."','"Derivado web de MA-ART-0004; el manuscrito canónico permanece en Obsidian."')
front+='description: "Demostraciones completas de Cauchy–Schwarz: sumas de cuadrados, inducción, Labbé, Steele, identidad de Lagrange, igualdad, espacios con producto interno e integrales."\n'
body=re.split(r'\n---\n\n## Correspondencia editorial y control de revisión \{#cs-editorial\}',body,maxsplit=1)[0]
linkmap={'MA-APP-0002 - Laboratorio de Cauchy-Schwarz':'laboratorio-cauchy-schwarz.qmd','MA-ART-0003 - La desigualdad triangular':'desigualdad-triangular.qmd'}
def wiki(m):
    destination,title=m.group(1).split('|',1) if '|' in m.group(1) else (m.group(1),m.group(1))
    if destination not in linkmap: raise ValueError('Wiki link no resuelto: '+destination)
    return f'[{title}]({linkmap[destination]})'
body=re.sub(r'\[\[([^\]]+)\]\]',wiki,body)
callout={'abstract':'note','question':'tip','example':'important','tip':'tip'}
def convert_callouts(text):
    lines=text.splitlines(keepends=True); result=[]; i=0
    while i<len(lines):
        match=re.match(r'^> \[!(abstract|question|example|tip)\]([^\n]*)',lines[i])
        if not match: result.append(lines[i]); i+=1; continue
        typ,title=match.groups(); result.append(f'::: {{.callout-{callout[typ]} title="{title.strip()}"}}\n'); i+=1
        while i<len(lines) and lines[i].startswith('>'):
            line=lines[i]; result.append(line[2:] if line.startswith('> ') else line[1:]); i+=1
        result.append(':::\n')
    return ''.join(result)
body=convert_callouts(body)
assert not re.search(r'\[\[|^> \[!',body,re.M)
assert '## 17. Preguntas frecuentes {#cs-faq}' in body
start=body.index('::: {.callout-tip title="Laboratorio de Cauchy–Schwarz (complemento opcional)"}')
end=body.index(':::',start+4)+3
replacement='''::: {.callout-tip title="Laboratorio interactivo · MA-APP-0002"}
Contrasta el cuadrado de §2 con la identidad de Lagrange, explora el parámetro de Labbé y, después de introducir la notación de §7, interpreta los vectores. El laboratorio permite investigar ejemplos; **no sustituye las demostraciones universales**.
:::

<iframe src="interactive/cauchy-schwarz.html" class="cs-lab-frame" data-cs-lab title="Laboratorio de Cauchy–Schwarz: sumas, parámetro de Labbé y geometría" loading="lazy" referrerpolicy="no-referrer" style="display:block;width:100%;height:1650px;border:1px solid #8097ac;border-radius:8px"></iframe>

[**Abrir el laboratorio en una página independiente**](laboratorio-cauchy-schwarz.qmd).

<script src="interactive/cauchy-schwarz-embed.js" defer></script>'''
body=body[:start]+replacement+'\n\n'+body[end:].lstrip('\n')
faqstart=body.index('## 17. Preguntas frecuentes {#cs-faq}')
faqs=re.findall(r'^### (¿[^\n]*\?) \{#(cs-faq-[^}]+)\}',body[faqstart:],flags=re.M)
assert len(faqs)==14,faqs
faqnav='\n\n**Ir a una pregunta:** '+ ' · '.join(f'[{title}](#{anchor})' for title,anchor in faqs)+'.\n'
pos=body.index('\n\n',faqstart)+2; pos=body.index('\n\n',pos)+2
body=body[:pos]+faqnav+body[pos:]
article='---'+front+'---'+body.rstrip()+'\n'
(R/'desigualdad-cauchy-schwarz.qmd').write_text(article,encoding='utf8')
html=Path(os.environ['MA_CS_HTML']).read_text(encoding='utf8')
html=html.replace('Matemática Abierta · MA-APP-0002 · Prototipo','Matemática Abierta · MA-APP-0002 · Laboratorio interactivo')
html=html.replace('Prototipo autónomo de evaluación · Fuente matemática:', 'Laboratorio interactivo · Fuente matemática:')
html=html.replace('La prueba para todas las sumas finitas está en las secciones 2–5 y 9 del artículo MA-ART-0004.', 'La prueba para todas las sumas finitas está en las <a href="../desigualdad-cauchy-schwarz.html#cs-enunciado">secciones 2–5 y 9 del artículo MA-ART-0004</a>.')
html=html.replace('25*x,190-25*y','15*x,190-15*y').replace('250+i*25,y=190-i*25','250+i*15,y=190-i*15')
for k,name in [('a1','a uno'),('a2','a dos'),('b1','b uno'),('b2','b dos')]: html=html.replace(f'id="{k}range" min=',f'id="{k}range" aria-label="Deslizador {name}" min=')
html=html.replace('update();\n})();\n</script>', '''update();
if(window.parent!==window && typeof ResizeObserver!=='undefined'){
 const sendHeight=()=>window.parent.postMessage({type:'ma-cs-resize',height:Math.ceil(document.body.scrollHeight)},window.location.origin==='null'?'*':window.location.origin);
 new ResizeObserver(sendHeight).observe(document.body);
 window.addEventListener('load',sendHeight);
 sendHeight();
}
})();
</script>''')
(LAB/'cauchy-schwarz.html').write_text(html,encoding='utf8')
print('Generados', (R/'desigualdad-cauchy-schwarz.qmd').stat().st_size, (LAB/'cauchy-schwarz.html').stat().st_size, 'FAQ',len(faqs))
