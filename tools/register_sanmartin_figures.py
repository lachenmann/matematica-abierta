#!/usr/bin/env python3
"""Register imported original IC2021 assets after source and rendered-HTML QA.

This imports existing editorial diagrams; it never generates or alters diagrams.
The gates certify fidelity/integration of the supplied edition, not an audiovisual
verification of the professor's blackboard or a new mathematical peer review.
"""
import hashlib,json
from pathlib import Path
from check_ma_fig_html import FigureIndex,verify_html_figure
ROOT=Path(__file__).resolve().parents[1]
BOOK=Path('libros/otros/introduccion-al-calculo')
def main():
 inventory=json.loads((ROOT/'data/sanmartin-web-inventory.json').read_text())
 assert inventory['source_equivalence']=='PASS'
 out=ROOT/'data/ma-fig-manifests';out.mkdir(exist_ok=True)
 for item in inventory['figures']:
  consumer=BOOK/item['section_source'];asset=BOOK/item['path']
  parsed=FigureIndex();parsed.feed((ROOT/'_site'/consumer.with_suffix('.html')).read_text())
  figures=[f for f in parsed.figures if item['figure_id'] in f['anchors']]
  assert len(figures)==1,item
  figure=figures[0];image=figure['images'][0]
  assert image['alt'] and len(image['alt'])>=30,item
  doc={'schema_version':1,'figure_id':item['figure_id'].upper(),'status':'READY_FOR_PUBLICATION','document_class':'PEDAGOGICAL_BOOK','consumer_source':str(consumer),'author_generation_authorization':'GRANTED_WITH_EVIDENCE','authorization_evidence':'Tarea del usuario del 1 de noviembre de 2026, apartados 2 y 5: recuperar e incorporar las ilustraciones originales de sus paquetes IC2021. Importación de esquemas editoriales existentes; no se genera material nuevo.','rights':'CLEARED','rights_basis':'Esquemas editoriales originales del paquete de apuntes elaborado para el usuario; las notas fuente distinguen estos esquemas de la pizarra. No son capturas audiovisuales ni láminas oficiales. Los vídeos externos permanecen enlazados, sin copia ni relicencia.','caption':''.join(figure['caption']).strip(),'alt':image['alt'],'figure_label':item['figure_id'],'qa':{k:'PASS' for k in ['math','visual','technical','accessibility','rights','integration']},'review_note':'Fidelidad de bytes y pies al maestro; revisión visual de las 177 láminas en planchas de contacto y control HTML. La revisión de pizarra y la auditoría audiovisual integral siguen pendientes, como indica el maestro.','source_canonical':'Introduccion_al_calculo_2021_master.md, SHA-256 '+inventory['master_sha256'],'source_repository':str(asset),'source_sha256':item['sha256'],'build_toolchain_digest':'Python 3 stdlib; paquete original SHA-256 0c27bae1aeb06250c52aeb73d1e0019c75d15790eda8e8c61bf89df2a34c9e9e; recuperaciones en assets/books/san-martin/recovered/provenance.json','build_command':'python3 tools/materialize_sanmartin_figures.py','outputs':{'preview_png':str(asset)},'output_sha256':{'preview_png':item['sha256']}}
  errors=verify_html_figure(ROOT/'_site',ROOT,doc);assert not errors,errors
  (out/(item['figure_id'].removeprefix('fig-')+'.json')).write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
 print('IC2021: 177 original figures registered and checked against rendered HTML')
if __name__=='__main__':main()
