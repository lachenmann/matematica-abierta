#!/usr/bin/env python3
"""Copyright-safe Quarto stress test; never reads or ships the real manuscript.

Only structural counts derived from an internal audit are used. No book text,
real problem statements, solutions or actual chapter mathematical expressions.
"""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path

EXPECTED = {'h1': 1, 'h2': 25, 'h3': 202, 'table': 10,
            'math': 3124, 'math_inline': 2818, 'math_display': 306}
TABLE_SHAPES = [(2, 14), (5, 4), (2, 14), (2, 4), (3, 4),
                (2, 8), (2, 8), (2, 4), (3, 2), (3, 2)]
TABLE_EXERCISES = [4, 4, 4, 10, 10, 11, 11, 16, 25, 25]
TABLES_BY_EXERCISE = {4: (0, 1, 2), 10: (3, 4), 11: (5, 6),
                      16: (7,), 25: (8, 9)}
MARKER = 'QA-SINTETICA-NO-ES-EL-MANUSCRITO-SPIVAK'


class CountHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.counts = {key: 0 for key in EXPECTED}
        self.tables = []
        self.exercise_tables = []
        self.exercise = 0
        self.table = None
        self.in_head = False
        self.in_body = False
        self.row_cells = None

    def handle_starttag(self, tag, attrs):
        if tag in self.counts:
            self.counts[tag] += 1
        if tag == 'h2':
            self.exercise += 1
        if tag == 'span':
            classes = dict(attrs).get('class', '').split()
            if 'math' in classes:
                self.counts['math'] += 1
                for form in ('inline', 'display'):
                    if form in classes:
                        self.counts[f'math_{form}'] += 1
        if tag == 'table':
            assert self.table is None, 'Unexpected nested HTML table'
            self.table = {'columns': None, 'rows': 0}
            self.exercise_tables.append(self.exercise)
        if self.table is None:
            return
        if tag == 'thead':
            self.in_head = True
        elif tag == 'tbody':
            self.in_body = True
        elif tag == 'tr':
            self.row_cells = 0
        elif tag in ('td', 'th') and self.row_cells is not None:
            self.row_cells += 1

    def handle_endtag(self, tag):
        if self.table is None:
            return
        if tag == 'tr' and self.row_cells is not None:
            if self.in_head:
                self.table['columns'] = self.row_cells
            elif self.in_body:
                self.table['rows'] += 1
                assert self.row_cells == self.table['columns'], (
                    f'Ragged table row in exercise {self.exercise}: '
                    f'{self.row_cells} != {self.table["columns"]}')
            self.row_cells = None
        elif tag == 'thead':
            self.in_head = False
        elif tag == 'tbody':
            self.in_body = False
        elif tag == 'table':
            self.tables.append((self.table['columns'], self.table['rows']))
            self.table = None


def table_markdown(index: int) -> list[str]:
    cols, rows = TABLE_SHAPES[index]
    headings = [f'Campo sintético {index + 1}.{c + 1}' for c in range(cols)]
    # Final two operation-like tables stress small, compact, 3-column layout.
    if index >= 8:
        headings = ['◇' if index == 8 else '⊙', 'A', 'B']
    lines = [f'| {" | ".join(headings)} |',
             f'| {" | ".join([":---"] * cols)} |']
    for row in range(rows):
        cells = [f'C{row + 1}.{col + 1}' for col in range(cols)]
        if index >= 8:
            cells = [chr(ord('A') + row), 'A', 'B']
        lines.append(f'| {" | ".join(cells)} |')
    return lines + ['']


def generate(path: Path):
    lines = ['---', 'title: "Ensayo sintético de Quarto (sin manuscrito)"',
             'lang: es', 'toc: false', '---', '', f'**{MARKER}**', '',
             'Las variables y tablas de esta prueba son ficticias.', '']
    inline = display = global_section = 0
    for exercise in range(1, 26):
        lines += [f'## Ejercicio sintético {exercise}', '']
        sections = 9 if exercise <= 2 else 8  # 2*9 + 23*8 = 202.
        for section in range(sections):
            lines += [f'### Sección técnica {exercise}.{section + 1}', '']
            tokens = 16 if global_section < 94 else 15
            display_here = 2 if global_section < 104 else 1
            for token in range(tokens):
                if token < display_here:
                    if display == 0:
                        formula = r'$$\begin{aligned} u+v&=v+u\\ u+(v+w)&=(u+v)+w\end{aligned}$$'
                    elif display == 1:
                        formula = r'$$g(t)=\begin{cases}t,&t\ge0,\\-t,&t<0.\end{cases}$$'
                    elif display == 2:
                        formula = r'$$\boxed{\sum_{j=1}^{m}j=\frac{m(m+1)}2}\tag{QA}$$'
                    else:
                        formula = f'$$a_{{{display}}}+b_{{{display}}}=c_{{{display}}}$$'
                    display += 1
                else:
                    formula = f'$x_{{{inline}}}^2+y_{{{inline}}}^2=z_{{{inline}}}^2$'
                    inline += 1
                lines += [formula, '']
            if section == 0:
                for index in TABLES_BY_EXERCISE.get(exercise, ()):
                    lines += table_markdown(index)
            global_section += 1
    assert global_section == 202 and inline == 2818 and display == 306, (
        global_section, inline, display)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'CREATED synthetic-only fixture: {path} | math inline={inline} '
          f'display={display}; tables={len(TABLE_SHAPES)}')


def verify(path: Path):
    data = path.read_text(encoding='utf-8')
    assert MARKER in data, 'Synthetic identifier missing; do not substitute another document.'
    parser = CountHTML()
    parser.feed(data)
    assert parser.counts == EXPECTED, (
        f'HTML counts differ: {parser.counts} != {EXPECTED}')
    assert parser.tables == TABLE_SHAPES, (
        f'Table shapes differ: {parser.tables} != {TABLE_SHAPES}')
    assert parser.exercise_tables == TABLE_EXERCISES, (
        f'Tables moved to wrong exercises: {parser.exercise_tables} != {TABLE_EXERCISES}')
    assert 'mathjax' in data.lower(), 'HTML does not appear to load MathJax'
    print(f'PASS synthetic Quarto HTML: {parser.counts}; '
          f'table shapes={parser.tables}; table positions={parser.exercise_tables}')
    print('SCOPE: synthetic surrogate only; actual chapter and browser layout NOT checked.')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('action', choices=['generate', 'verify'])
    p.add_argument('path', type=Path)
    args = p.parse_args()
    (generate if args.action == 'generate' else verify)(args.path)
