"""Preserve the canonical force diagram and move its overlapping T label."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
name='FPM-I-10_DCL_03_v01.svg'
source=ROOT/'data/fispm-figure-sources/C10'/name
output=ROOT/'assets/books/fispm/C10'/name
raw=source.read_text(encoding='utf-8')
before='<text x="438" y="184"'
assert raw.count(before)==1
output.write_text(raw.replace(before,'<text x="460" y="160"'),encoding='utf-8',newline='\n')
