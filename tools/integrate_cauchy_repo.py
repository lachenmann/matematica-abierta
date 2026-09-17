from pathlib import Path
repo=Path.cwd(); r=repo/'teoria/resultados'; idx=r/'index.qmd'; triangle=r/'desigualdad-triangular.qmd'; ci=repo/'.github/workflows/quarto-check.yml'
assert idx.is_file() and triangle.is_file() and ci.is_file()
assert (r/'desigualdad-cauchy-schwarz.qmd').is_file() and (r/'laboratorio-cauchy-schwarz.qmd').is_file()
src=idx.read_text(encoding='utf-8')
if 'desigualdad-cauchy-schwarz.qmd' not in src:
    marker='\n## Sumas finitas y cálculo discreto\n'; assert src.count(marker)==1
    add='''- [**La desigualdad de Cauchy–Schwarz: demostraciones y variantes**](desigualdad-cauchy-schwarz.qmd) (`MA-ART-0004`) — del caso elemental y la inducción a Labbé, Steele, la identidad de Lagrange, las condiciones de igualdad y las versiones compleja e integral.
- [**Laboratorio interactivo de Cauchy–Schwarz**](laboratorio-cauchy-schwarz.qmd) (`MA-APP-0002`) — explora sumas de cuadrados, el parámetro de Labbé y la interpretación geométrica; incluye casos nulos y de igualdad.
'''
    idx.write_text(src.replace(marker,'\n'+add+marker),encoding='utf-8')
src=triangle.read_text(encoding='utf-8')
if 'desigualdad-cauchy-schwarz.qmd#cs-enunciado' not in src:
    marker='**Lema (Cauchy–Schwarz finito).**'; assert src.count(marker)==1
    addition=('Para profundizar, consulta [la demostración completa de Cauchy–Schwarz]'
              '(desigualdad-cauchy-schwarz.qmd#cs-enunciado), que desarrolla la inducción, '
              'las pruebas cuadráticas, la igualdad y la identidad de Lagrange. '
              'Conservamos aquí una demostración breve para que el argumento sea autónomo.\n\n')
    triangle.write_text(src.replace(marker,addition+marker),encoding='utf-8')
src=ci.read_text(encoding='utf-8')
if 'Validate Cauchy' not in src:
    before='      - name: Set up Quarto\n'; assert src.count(before)==1
    step='''      - name: Validate Cauchy–Schwarz source and laboratory
        run: |
          python3 tests/cauchy_static.py
          node --check teoria/resultados/interactive/cauchy-schwarz-embed.js
          python3 -c "from pathlib import Path; import re; h=Path('teoria/resultados/interactive/cauchy-schwarz.html').read_text(); Path('/tmp/cauchy-lab-inline.js').write_text(re.search(r'<script>([\\s\\S]*?)</script>', h).group(1))"
          node --check /tmp/cauchy-lab-inline.js

'''
    src=src.replace(before,step+before)
    before='      - name: Preserve rendered site for visual and link QA\n'; assert src.count(before)==1
    step='''      - name: Verify Cauchy–Schwarz rendered pages and assets
        run: |
          test -s _site/teoria/resultados/desigualdad-cauchy-schwarz.html
          test -s _site/teoria/resultados/laboratorio-cauchy-schwarz.html
          test -s _site/teoria/resultados/interactive/cauchy-schwarz.html
          test -s _site/teoria/resultados/interactive/cauchy-schwarz-embed.js
          grep -q 'interactive/cauchy-schwarz.html' _site/teoria/resultados/desigualdad-cauchy-schwarz.html
          grep -q 'interactive/cauchy-schwarz.html' _site/teoria/resultados/laboratorio-cauchy-schwarz.html
          grep -q 'MA-APP-0002' _site/teoria/resultados/laboratorio-cauchy-schwarz.html
          grep -q 'desigualdad-cauchy-schwarz.html' _site/teoria/resultados/index.html

'''
    ci.write_text(src.replace(before,step+before),encoding='utf-8')
print('Integración lista.')
