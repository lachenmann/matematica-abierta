#!/usr/bin/env python3
"""Synthetic Quarto stress test: never handles or distributes the manuscript."""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path

EXPECTED = {'h1': 1, 'h2': 25, 'h3': 202, 'table': 10, 'math': 3124}
MARKER = 'QA-SINTETICA-NO-ES-EL-MANUSCRITO-SPIVAK'


class CountHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.counts = {key: 0 for key in EXPECTED}

    def handle_starttag(self, tag, attrs):
        if tag in self.counts:
            self.counts[tag] += 1
        if tag == 'span' and 'math' in dict(attrs).get('class', '').split():
            self.counts['math'] += 1


def generate(path: Path):
    lines = [
        '---',
        'title: "Ensayo sintético de Quarto (sin manuscrito)"',
        'lang: es',
        'toc: false',
        '---',
        '',
        f'**{MARKER}**',
        '',
        'Esta prueba contiene símbolos inventados, no ejercicios ni soluciones del libro.',
        '',
    ]
    generated_math = 0
    for exercise in range(25):
        lines += [f'## Ejercicio sintético {exercise + 1}', '']
        sections = 9 if exercise < 2 else 8  # 2*9 + 23*8 = 202.
        for section in range(sections):
            lines += [f'### Sección técnica {exercise + 1}.{section + 1}', '']
            global_section = sum(9 if e < 2 else 8 for e in range(exercise)) + section
            tokens = 16 if global_section < 94 else 15  # 94*16+108*15 = 3124.
            for token in range(tokens):
                if generated_math == 0:
                    formula = r'$$\begin{aligned} a+b&=b+a\\ a+(b+c)&=(a+b)+c\end{aligned}$$'
                elif generated_math == 1:
                    formula = r'$$f(x)=\begin{cases}x,&x\ge0,\\-x,&x<0.\end{cases}$$'
                elif generated_math == 2:
                    formula = r'$$\boxed{\sum_{k=1}^{n}k=\frac{n(n+1)}2}\tag{QA}$$'
                else:
                    formula = f'$x_{{{generated_math}}}^2+y_{{{generated_math}}}^2=z_{{{generated_math}}}^2$'
                lines += [formula, '']
                generated_math += 1
            if global_section < 10:
                lines += ['| Variable | Valor | Prueba |', '|:---|---:|---|',
                          f'| Caso {global_section + 1} | {global_section + 1} | Dato ficticio |', '']
    assert generated_math == EXPECTED['math']
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'CREATED synthetic-only fixture: {path} | math={generated_math}')


def verify(path: Path):
    data = path.read_text(encoding='utf-8')
    assert MARKER in data, 'Synthetic identifier missing; do not substitute another document.'
    parser = CountHTML()
    parser.feed(data)
    assert parser.counts == EXPECTED, f'HTML counts differ: {parser.counts} != {EXPECTED}'
    assert 'mathjax' in data.lower(), 'HTML does not appear to load MathJax'
    print(f'PASS synthetic Quarto HTML: {parser.counts}; MathJax hook present')
    print('SCOPE: synthetic surrogate only; actual chapter and browser layout NOT checked.')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('action', choices=['generate', 'verify'])
    p.add_argument('path', type=Path)
    args = p.parse_args()
    (generate if args.action == 'generate' else verify)(args.path)
