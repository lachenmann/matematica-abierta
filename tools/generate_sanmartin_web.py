#!/usr/bin/env python3
"""Reproduce/verify the Quarto chapter files from the frozen IC2021 Markdown master.

No network access, dependencies beyond the Python standard library, or changes
outside of the book's destination directory are needed.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
import json
from pathlib import Path
from sanmartin_archive import ensure_archive

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'assets/books/san-martin/IC2021_master_y_figuras.zip'
DEST = ROOT / 'libros/otros/introduccion-al-calculo'
PART = re.compile(r'^# (Parte [IVX]+\. .+)$', re.M)
CHAPTER = re.compile(r'^## (.+)$', re.M)
DASH = '—'


def yaml_quote(v: str) -> str:
    # JSON double quotes are a YAML subset, and handle accents and math safely.
    import json
    return json.dumps(v, ensure_ascii=False)


def split_master(src: str):
    if not src.startswith('---\n'):
        raise ValueError('El maestro carece de front matter')
    p = src.find('\n---\n', 4)
    if p < 0:
        raise ValueError('Front matter no terminado')
    body = src[p + 5:]
    begin = PART.search(body)
    appendix = re.search(r'^# Apéndices y registro de procedencia\s*$', body, re.M)
    if not begin or not appendix or begin.start() >= appendix.start():
        raise ValueError('Partes y apéndices esperados ausentes')
    intro = body[:begin.start()].strip()
    middle = body[begin.start():appendix.start()]
    appendix_text = body[appendix.end():].strip()
    parts = []
    chapters = []
    current_part = None
    spans = list(re.finditer(r'^(# Parte [IVX]+\. [^\n]+|## [^\n]+)$', middle, re.M))
    for i, match in enumerate(spans):
        start = match.end()
        end = spans[i+1].start() if i+1 < len(spans) else len(middle)
        value = match.group(1)
        content = middle[start:end].strip()
        if value.startswith('# Parte'):
            if content:
                raise ValueError(f'Párrafo suelto tras parte: {value}')
            current_part = value[2:]
            parts.append({'name':current_part,'chapter_numbers':[]})
        else:
            if current_part is None:
                raise ValueError('Capítulo antes de la primera parte')
            number = len(chapters)+1
            title = value[3:].strip()
            chapters.append({'number':number, 'title':title, 'part':current_part, 'body':content})
            parts[-1]['chapter_numbers'].append(number)
    if len(parts) != 5 or len(chapters) != 18:
        raise ValueError(f'Se esperaban 5 partes y 18 capítulos; son {len(parts)} y {len(chapters)}')
    return intro, parts, chapters, appendix_text


def lower_headers(text: str) -> str:
    # The master has chapter titles at ## and their subjects at ###/####.
    # A Quarto page obtains its document title from YAML. Keep a local H2+ TOC.
    return re.sub(r'(?m)^(#{3,6})(?=\s)', lambda m: m.group(1)[1:], text)


def accessible_figures(text: str, chapter: int) -> str:
    """Keep original caption and bytes; add explicit alt and stable HTML anchors."""
    counter = 0
    def replace(match):
        nonlocal counter
        counter += 1
        caption, path, attributes = match.groups()
        alt = caption.replace('$', '')
        if len(alt) < 30:
            alt = 'Esquema matemático: ' + alt
        label = f'fig-ic2021-c{chapter:02d}-f{counter:02d}'
        retained = attributes.strip()[1:-1].strip() if attributes else ''
        return f'![{caption}]({path})' + '{#' + label + ' fig-alt=' + json.dumps(alt, ensure_ascii=False) + (' '+retained if retained else '') + '}'
    return re.sub(r'!\[([^\n]*)\]\((figuras/[^)]+)\)([ \t]*\{[^}\n]*\})?', replace, text)


def front(title, description, **extra):
    d = {
        'title':title,
        'description':description,
        'lang':'es-CL',
        'number-sections':False,
        'toc':True,
        'toc-depth':2,
        'status':'published',
        'draft':False,
        'source-id':'IC2021',
    }
    d.update(extra)
    lines=['---']
    for k,v in d.items():
        lines.append(f'{k}: {yaml_quote(v) if isinstance(v,str) else str(v).lower()}')
    lines.append('---')
    return '\n'.join(lines)+'\n\n'


def expected_files(master: str):
    introduction, parts, chapters, appendices = split_master(master)
    files = {}
    index = front('Introducción al cálculo', 'Del número real a la derivada; edición temática de las clases de Jorge San Martín (2021)',subtitle='Del número real a la derivada')
    index += '> **Edición no oficial de estudio.** Reconstrucción temática a partir de las cátedras públicas de Jorge San Martín (2021). La organización, las notas y las ampliaciones editoriales pertenecen a esta edición; las grabaciones conservan sus propios derechos y procedencia.\n\n'
    # The introductory original text is retained verbatim, except for changing H2 to H2.
    index += introduction+'\n\n'
    index += '## Índice temático\n\n'
    for part in parts:
        index += f'### {part["name"]}\n\n'
        for n in part['chapter_numbers']:
            c=chapters[n-1]
            index += f'{n}. [**{c["title"]}**](capitulo-{n:02d}.qmd)\n'
        index+='\n'
    index += '## Material complementario\n\n'
    index += '[Apéndices, concordancia y fuentes audiovisuales](apendices.qmd).\n\n'
    index += 'La edición web conserva el **maestro Markdown corregido**, las **177 figuras referenciadas** y la trazabilidad de las grabaciones. La auditoría audiovisual íntegra de las pizarras continúa pendiente, como señala el propio maestro.\n\n'
    index += '[Obtener el paquete reproducible completo (maestro y 177 figuras)](../../../assets/books/san-martin/IC2021_fuentes_web_completas.zip).\n\n'
    index += '## Créditos editoriales y derechos\n\nEdición temática no oficial de apuntes elaborados a partir de las clases de Jorge San Martín (2021), diferenciada del curso y de sus materiales oficiales. El maestro conserva las atribuciones docentes y las marcas de ampliación editorial. Las figuras proceden de los paquetes de elaboración editorial de estos apuntes; no se incorporan capturas de las grabaciones ni materiales oficiales adicionales. Los materiales externos enlazados conservan sus derechos: la atribución no otorga una nueva licencia. El docente no figura como revisor de esta edición.\n\nLa edición PDF definitiva no se enlaza: su archivo publicable no forma parte del paquete fuente recuperado.\n'
    files['index.qmd'] = index
    for c in chapters:
        n=c['number']
        chapter = front(c['title'], f'Capítulo {n} de Introducción al cálculo: {c["title"]}. Edición temática del curso IC2021.',subtitle=f'Capítulo {n} · {c["part"]}')
        chapter += accessible_figures(lower_headers(c['body']), n)+'\n\n'
        chapter += f'---\n\n*Este capítulo pertenece a la edición temática no oficial del curso IC2021. [Índice del libro](index.qmd) · [Fuentes y concordancia](apendices.qmd).*\n'
        files[f'capitulo-{n:02d}.qmd'] = chapter
    files['apendices.qmd'] = front('Apéndices y registro de procedencia','Concordancia de las 28 cátedras y bibliografía audiovisual del curso IC2021.') + appendices+'\n'
    return files, parts, chapters


def run():
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',action='store_true')
    g.add_argument('--check',action='store_true')
    p.add_argument('--master',type=Path,help='Maestro actualizado; omitir para usar la copia canónica congelada')
    opt=p.parse_args()
    if opt.master:
        master=opt.master.read_text(encoding='utf-8')
    else:
        with zipfile.ZipFile(ensure_archive()) as z:
            master=z.read('master/Introduccion_al_calculo_2021_master.md').decode('utf-8')
    files,parts,chapters=expected_files(master)
    differences=[]
    for name,content in files.items():
        target=DEST/name
        if opt.write:
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(content,encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8')!=content:
            differences.append(name)
    actual={f.name for f in DEST.glob('capitulo-*.qmd')}
    expected={f'capitulo-{i:02d}.qmd' for i in range(1,19)}
    if actual-expected:
        differences.extend(sorted(actual-expected))
    if differences:
        print('Desfase con el maestro: '+', '.join(differences),file=sys.stderr)
        sys.exit(1)
    print(f'IC2021 Quarto: {"GENERADO" if opt.write else "PASS"} — 5 partes, 18 capítulos, portada y apéndice')


if __name__ == '__main__':
    run()
