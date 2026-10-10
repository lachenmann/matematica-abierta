"""Generate lightweight C01 reading pages from its complete public source."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def paginate():
    manifest_path = ROOT/'data/cpm-tome-i-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    row = manifest['chapters'][0]
    landing = ROOT/row['path']
    full = landing.parent/'_cpm-c01-full.md'
    text = full.read_text()
    front, body = re.match(r'(---\n.*?\n---\n)(.*)', text, re.S).groups()
    nav = '[Índice del Tomo I](../para-matematicos/calculo-para-matematicos.md) · [Capítulo 2 →](funciones-reales-estructura-composicion-inversas-y-graficas.md)'
    body = body.replace('\n\n'+nav, '')
    body = re.sub(r'\n\n---\s*$', '', body)
    sections = list(re.finditer(r'^## (.+?) \{#([^}]+)\}\s*$', body, re.M))
    assert len(sections) == 11
    intro = body[:sections[0].start()].strip()
    chunks = []
    for i, section in enumerate(sections):
        end = sections[i+1].start() if i+1 < len(sections) else len(body)
        chunk = body[section.start():end].strip()
        if i == 10:
            cut = chunk.index('\n### Soluciones\n')
            chunks.append((i+1, 'Ejercicios', chunk[:cut]))
            chunks.append((i+1, 'Soluciones', '## Soluciones de los ejercicios {#cpm-c01-soluciones}\n'+chunk[cut:]))
        else:
            chunks.append((i+1, section[1], chunk))
    pages = []
    owners = {}
    for i, (number, title, chunk) in enumerate(chunks):
        filename = 'cpm-c01-'+(f'{number:02d}' if i < 11 else 'soluciones')+'.md'
        path = landing.parent/filename
        pages.append({'path':str(path.relative_to(ROOT)), 'title':title, 'section':number})
        for anchor in re.findall(r'\{#([\w-]+)', chunk):
            assert anchor not in owners
            owners[anchor] = filename
    def links(chunk, filename):
        def replace(m):
            file, anchor = m.groups()
            if anchor in owners and (not file or Path(file).name == landing.name):
                destination = '' if owners[anchor] == filename else owners[anchor]
                return ']('+destination+'#'+anchor+')'
            return m[0]
        return re.sub(r'\]\(([^)#]*)#([\w-]+)\)', replace, chunk)
    for i, ((number, title, chunk), page) in enumerate(zip(chunks, pages)):
        filename = Path(page['path']).name
        metadata = re.sub(r'^content-id: .*\n', '', front, flags=re.M)
        metadata = metadata.replace('content-type: book-chapter', 'content-type: book-section')
        metadata = metadata.replace('number-offset: [0]', f'number-offset: [0, {number-1}]')
        metadata = metadata.replace('date-modified: 2026-10-01', 'date-modified: 2026-10-06')
        metadata = re.sub(r'^title: .*$', lambda _: 'title: '+json.dumps(f'1.{number} — {title}', ensure_ascii=False), metadata, flags=re.M)
        metadata = re.sub(r'^description: .*$', 'description: "Capítulo 1 de Cálculo para matemáticos: lectura por secciones."', metadata, flags=re.M)
        previous = Path(pages[i-1]['path']).name if i else landing.name
        following = Path(pages[i+1]['path']).name if i+1 < len(pages) else 'funciones-reales-estructura-composicion-inversas-y-graficas.md'
        local_nav = f'[← Anterior]({previous}) · [Índice del capítulo]({landing.name}) · [Siguiente →]({following})'
        chapter_heading = '# Los números reales: axiomas de cuerpo, orden y completitud\n\n'
        (ROOT/page['path']).write_text(metadata+'\n'+chapter_heading+local_nav+'\n\n'+links(chunk, filename)+'\n\n---\n\n'+local_nav+'\n')
    index = '\n\n## Lectura por secciones {.unnumbered}\n\nCada sección se carga en una página independiente. Los ejercicios y sus soluciones se pueden abrir por separado.\n\n'
    for i, page in enumerate(pages):
        label = ('1.'+str(page['section'])+' — ' if i < 11 else '')+page['title']
        index += '- ['+label+']('+Path(page['path']).name+')\n'
    # Old bookmarks and incoming chapter references keep their public route.
    redirects = {anchor:filename.replace('.md', '.html') for anchor,filename in owners.items()}
    compatibility = '\n```{=html}\n<script id="cpm-c01-anchor-routes" type="application/json">'+json.dumps(redirects, ensure_ascii=False)+'</script>\n<script>\n(function () {\n  function followAnchor() {\n    const anchor = decodeURIComponent(location.hash.slice(1));\n    const routes = JSON.parse(document.getElementById("cpm-c01-anchor-routes").textContent);\n    if (Object.hasOwn(routes, anchor)) location.replace(routes[anchor] + location.hash);\n  }\n  followAnchor();\n  window.addEventListener("hashchange", followAnchor);\n})();\n</script>\n```\n'
    landing.write_text(front.replace('content-type: book-chapter', 'content-id: MA-BCH-0003\ncontent-type: book-chapter').replace('date-modified: 2026-10-01', 'date-modified: 2026-10-06')+'\n'+intro+'\n\n'+nav+index+compatibility+'\n'+nav+'\n')
    row['pages'] = pages
    row['web_source'] = str(full.relative_to(ROOT))
    row['anchor_routes'] = redirects
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    return pages

if __name__ == '__main__':
    print('Generated', len(paginate()), 'reading pages')
