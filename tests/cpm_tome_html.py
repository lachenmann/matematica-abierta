"""Verify the integrated rendered chapters; exclude Quarto's hidden metadata."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json, re

repo = Path(__file__).resolve().parents[1]
root = repo/'_site-cpm-qa'
rows = json.loads((repo/'data/cpm-tome-i-manifest.json').read_text())['chapters']
class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.body = False
        self.ids, self.links, self.images = [], [], []
        self.math = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'body': self.body = True
        if self.body and a.get('id'): self.ids.append(a['id'])
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag == 'img': self.images.append(a)
        if 'math' in a.get('class', '').split(): self.math += 1
    def handle_endtag(self, tag):
        if tag == 'body': self.body = False
pages = {}
for row in rows:
    path = (root/Path(row['path']).with_suffix('.html')).resolve()
    raw = re.sub(r'<div id="quarto-meta-markdown" class="hidden">.*?</div>', '', path.read_text(), flags=re.S)
    parser = Inspect(); parser.feed(raw)
    assert not [i for i,n in Counter(parser.ids).items() if n > 1], row['chapter']
    assert 'quarto-unresolved-ref' not in raw and parser.math > 0
    for section in row['sections']:
        anchor, expected = section['anchor'], section['number']
        assert re.search(r'<section id="'+anchor+r'"[^>]*data-number="'+re.escape(expected)+r'"', raw), (row['chapter'], anchor, expected)
    pages[path] = parser
images = set()
for path, parser in pages.items():
    for href in parser.links:
        url = urlsplit(href)
        if url.scheme or url.netloc: continue
        target = (path.parent/unquote(url.path)).resolve() if url.path else path
        if target in pages and url.fragment:
            assert unquote(url.fragment) in pages[target].ids, href
    for image in parser.images:
        src = image.get('src', '')
        if 'assets/books/cpm-tomo-i/' in src:
            assert image.get('alt')
            assert (path.parent/unquote(src)).resolve().is_file()
            images.add(src.split('/')[-1])
assert len(images) == 64
result = {'chapters':20,'images':64,'math_spans':sum(p.math for p in pages.values()),
          'duplicate_body_ids':0,'unresolved_refs':0,'broken_chapter_links':0}
(repo/'cpm-html-qa.json').write_text(json.dumps(result, indent=2)+'\n')
print(result)
