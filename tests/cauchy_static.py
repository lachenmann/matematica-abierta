"""Control editorial estático para la publicación MA-ART-0004 / MA-APP-0002."""
from pathlib import Path
import re

repo = Path(__file__).resolve().parents[1]
r = repo / 'teoria' / 'resultados'
article = (r / 'desigualdad-cauchy-schwarz.qmd').read_text(encoding='utf-8')
lab_page = (r / 'laboratorio-cauchy-schwarz.qmd').read_text(encoding='utf-8')
lab_html = (r / 'interactive/cauchy-schwarz.html').read_text(encoding='utf-8')
resizer = (r / 'interactive/cauchy-schwarz-embed.js').read_text(encoding='utf-8')


def verify(ok, reason):
    if not ok:
        raise AssertionError(reason)

verify(article.count('content-id: MA-ART-0004') == 1, 'identidad del artículo')
verify(lab_page.count('content-id: MA-APP-0002') == 1, 'identidad del laboratorio')
verify(len(re.findall(r'^### ¿[^\n]+ \{#cs-faq-', article, re.M)) == 14, '14 preguntas frecuentes')
verify('[[ ' not in article and '[[' not in article and '> [!' not in article, 'sin enlaces o callouts Obsidian')
verify(article.count('```') % 2 == 0, 'bloques de código emparejados')
verify(article.count('$$') % 2 == 0, 'bloques matemáticos emparejados')
verify(article.count('::: {.callout-') == len(re.findall(r'^:::$', article, re.M)), 'callouts equilibrados')
verify(article.find('## 7. Ahora sí:') < article.find('## 9. La identidad'), 'progresión pedagógica')
verify(article.find('## 2. Dos términos:') < article.find('## 7. Ahora sí:'), 'notación no anticipada')
for fragment in re.findall(r'\]\(#([\w-]+)\)', article):
    verify(f'{{#{fragment}}}' in article, f'fragmento sin destino: {fragment}')
for fragment in re.findall(r'desigualdad-cauchy-schwarz\.qmd#([\w-]+)', lab_page):
    verify(f'{{#{fragment}}}' in article, f'enlace laboratorio-artículo: {fragment}')
for name in ['desigualdad-cauchy-schwarz.qmd', 'laboratorio-cauchy-schwarz.qmd']:
    verify((r / name).is_file(), f'QMD ausente: {name}')
for page in (article, lab_page):
    verify('src="interactive/cauchy-schwarz.html"' in page, 'HTML único incrustado')
    verify('src="interactive/cauchy-schwarz-embed.js"' in page, 'ajuste de altura compartido')
verify(len(re.findall(r'id="[ab][12]range" aria-label="Deslizador', lab_html)) == 4, 'deslizadores etiquetados')
verify('ResizeObserver' in lab_html and 'document.body.scrollHeight' in lab_html, 'altura natural')
verify("event.origin !== window.location.origin" in resizer, 'validación de origen iframe')
verify('Prototipo autónomo de evaluación' not in lab_html, 'metadatos de prototipo retirados de web')
verify('https://' not in resizer, 'recurso local sin llamadas remotas')
verify('## Correspondencia editorial y control de revisión' not in article, 'notas editoriales fuera del artículo')
print('QA estático OK: IDs, 14 FAQ, matemáticas, enlaces, recursos, accesibilidad, progresión y fuente original preservada.')

if (r / 'index.qmd').is_file():
    index = (r / 'index.qmd').read_text(encoding='utf-8')
    verify('desigualdad-cauchy-schwarz.qmd' in index, 'índice sin artículo')
    verify('laboratorio-cauchy-schwarz.qmd' in index, 'índice sin laboratorio')
    print('QA índice OK.')
if (r / 'desigualdad-triangular.qmd').is_file():
    triangle = (r / 'desigualdad-triangular.qmd').read_text(encoding='utf-8')
    verify('desigualdad-cauchy-schwarz.qmd#cs-enunciado' in triangle, 'sin enlace desde desigualdad triangular')
    print('QA reciprocidad triangular OK.')
