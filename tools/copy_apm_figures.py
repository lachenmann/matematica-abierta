from pathlib import Path
import shutil
for source in Path('data/apm-figure-sources').glob('*.svg'):
    target=Path('assets/books/apm-tomo-i')/source.name
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(source,target)
