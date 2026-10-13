#!/usr/bin/env python3
"""MA-ART-0018 M03: SVG exactos y reproducibles (solo biblioteca estándar).

Uso: python3 generar_figuras_enteros.py --output-dir .
Convenio: N={0,1,...}; (a,b)~(c,d) ssi a+d=b+c.
"""
from __future__ import annotations
import argparse
from pathlib import Path
from html import escape
from hashlib import sha256

BG='#FFFFFF'; INK='#17263B'; MUTED='#46536A'; LINE='#DCE3EB'; BLUE='#16649E'; ORANGE='#A54A12'; GREEN='#176C51'; SOFTBLUE='#EAF4FC'; SOFTORANGE='#FFF2E8'; SOFTGREEN='#EAF8F1'; GRAY='#56647A'
FONT='DejaVu Sans, sans-serif'

def t(x,y,s,size=23,color=INK,weight=400,anchor=None):
    at=f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{color}"{at}>{escape(s)}</text>'

def rect(x,y,w,h,fill='#FFF',stroke=LINE,r=15,sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def line(x1,y1,x2,y2,color=LINE,sw=2,dash=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'

def circ(x,y,r,color,stroke='#FFFFFF',sw=2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="{stroke}" stroke-width="{sw}"/>'

def chip(x,y,color):return circ(x,y,10,color,INK,1)

def shell(w,h,title,desc,body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="svgtitle svgdesc">'
            f'<title id="svgtitle">{escape(title)}</title><desc id="svgdesc">{escape(desc)}</desc>'
            +rect(1,1,w-2,h-2,BG,BG,0,0)+body+'</svg>\n')

def f01():
    """Mobile-first single-column layout: counts and two cross-comparisons."""
    p=[t(31,49,'Fichas y sumas cruzadas',31,INK,700),
       t(31,79,'Dos cuentas distintas pueden ser equivalentes.',19,MUTED)]
    for x,y,a,b,name in [(32,112,5,2,'A = (5,2)'),(32,323,4,1,'B = (4,1)')]:
        p += [rect(x,y,586,181,'#FBFCFD','#BACDDD'),t(x+20,y+37,name,27,INK,700),
              t(x+24,y+82,'a favor',22,BLUE,700),t(x+310,y+82,'en contra',22,ORANGE,700),
              t(x+22,y+158,str(a)+' fichas',18,INK),t(x+308,y+158,str(b)+(' ficha' if b==1 else ' fichas'),18,INK)]
        for i in range(a):p.append(chip(x+31+31*i,y+110,BLUE))
        for i in range(b):p.append(chip(x+317+31*i,y+110,ORANGE))
    p += [t(32,548,'Compara columnas opuestas:',24,INK,700),
          rect(31,571,587,102,SOFTBLUE,'#B7D7EC'),
          t(54,606,'1.ª de A  +  2.ª de B',23,BLUE,700),
          t(54,645,'5 + 1 = 6',29,INK,700),
          rect(31,685,587,102,SOFTORANGE,'#E6C1A7'),
          t(54,721,'2.ª de A  +  1.ª de B',23,ORANGE,700),
          t(54,761,'2 + 4 = 6',29,INK,700),
          rect(31,805,587,121,SOFTGREEN,'#97C7AF'),
          t(53,846,'Se cumple la igualdad cruzada:',21,GREEN,700),
          t(53,884,'5 + 1 = 2 + 4',26,INK,700),
          t(53,914,'(5,2) ~ (4,1), pero no son el mismo par.',17,INK)]
    return shell(650,953,'F01: fichas y sumas cruzadas','La cuenta A=(5,2) tiene cinco fichas a favor y dos en contra; B=(4,1) tiene cuatro a favor y una en contra. Los totales cruzados son 5+1=6 y 2+4=6. Los dos pares distintos son equivalentes.',''.join(p))

def f02():
    """Mobile-first 7x7 exact grid; colored shapes also distinguish families."""
    x0,y0,step=88,637,71
    p=[t(30,48,'Clases de equivalencia',31,INK,700),
       t(30,78,'Cada punto es un par (a,b) de naturales.',19,MUTED),
       t(30,105,'Se muestra solo la ventana de 0 a 6.',19,MUTED)]
    for b in range(7):p.append(line(x0,y0-step*b,x0+6*step,y0-step*b,LINE,1))
    for a in range(7):p.append(line(x0+a*step,y0,x0+a*step,y0-step*6,LINE,1))
    for a in range(7):
        for b in range(7):p.append(circ(x0+step*a,y0-step*b,3.7,'#C3D0DB','#C3D0DB',0))
    p += [line(x0,y0,x0+6*step+23,y0,INK,2),line(x0,y0,x0,y0-6*step-23,INK,2)]
    for n in range(7):
        p += [t(x0+step*n,y0+27,str(n),18,INK,anchor='middle'),
              t(x0-27,y0-step*n+6,str(n),18,INK,anchor='middle')]
    p += [t(547,y0+6,'a',24,INK,700),t(x0-5,175,'b',24,INK,700)]
    families=[('P',[(a,b) for a in range(7) for b in range(7) if a==b+3],BLUE,'square'),
              ('C',[(a,b) for a in range(7) for b in range(7) if a==b],GRAY,'circle'),
              ('N',[(a,b) for a in range(7) for b in range(7) if b==a+3],ORANGE,'diamond')]
    assert [len(pts) for _,pts,_,_ in families]==[4,7,4]
    for label,pts,col,shape in families:
        a0,b0=pts[0]; a1,b1=pts[-1]
        p.append(line(x0+a0*step,y0-b0*step,x0+a1*step,y0-b1*step,col,3,'8 7'))
        for a,b in pts:
            x,y=x0+a*step,y0-b*step
            if shape=='square':p.append(f'<rect x="{x-8}" y="{y-8}" width="16" height="16" rx="2" fill="{col}"/>')
            elif shape=='diamond':p.append(f'<polygon points="{x},{y-10} {x+10},{y} {x},{y+10} {x-10},{y}" fill="{col}"/>')
            else:p.append(circ(x,y,8,col,BG,1))
            if a==0 or b==0:p.append(f'<circle cx="{x}" cy="{y}" r="17" fill="none" stroke="{INK}" stroke-width="2.6"/>')
    assert (6,6) in families[1][1]
    p += [t(31,707,'P  ■   [(3,0)]   :   a = b + 3',23,BLUE,700),
          t(31,758,'C  ●   [(0,0)]   :   a = b',23,GRAY,700),
          t(31,809,'N  ◆   [(0,3)]   :   b = a + 3',23,ORANGE,700),
          rect(30,848,586,157,SOFTBLUE,'#B6CFDF'),
          t(51,891,'Los aros indican representantes',21,INK),
          t(51,924,'canónicos sobre los ejes.',21,INK),
          t(51,959,'Las líneas solo guían la vista.',19,MUTED),
          t(51,987,'Las clases continúan fuera del recorte.',18,MUTED)]
    return shell(650,1031,'F02: retícula de clases','Retícula de los 49 pares de naturales entre cero y seis. Cuatro cuadrados P representan (3,0),(4,1),(5,2),(6,3). Siete círculos C representan todos los (n,n) de 0 a 6, incluido (6,6). Cuatro rombos N representan (0,3),(1,4),(2,5),(3,6). Aros señalan (3,0),(0,0),(0,3); las clases tienen infinitos elementos y los trazos son solo guías.', ''.join(p))

def f03():
    parts=[t(40,53,'Operar no es normalizar',33,INK,700),t(40,84,'El entero es una clase; el par es uno de sus representantes.',19,MUTED)]
    panels=[(108,SOFTBLUE,BLUE,'1  Elegir representantes', '[(3,0)] y [(0,2)]'),
            (305,SOFTORANGE,ORANGE,'2  Sumar por coordenadas','[(3,0)] + [(0,2)] = [(3,2)]'),
            (502,SOFTGREEN,GREEN,'3  Normalizar el par','(3,2) ~ (2,1) ~ (1,0)')]
    for y,fill,col,head,equation in panels:
        parts += [rect(38,y,704,174,fill,'#BCCCD8',12,2), t(64,y+41,head,27,col,700), t(66,y+96,equation,29,INK,700)]
    parts += [t(65,255,'Ambos pares elegidos tienen una coordenada igual a cero.',18,MUTED),
              t(65,450,'El par (3,2) obtenido no es normalizado.',18,MUTED),
              t(65,648,'Cada par está en la retícula: a y b son naturales.',18,MUTED),
              t(40,716,'(3,2) y (1,0) son pares diferentes,',24,INK),
              t(40,748,'pero sus clases son iguales:',24,INK),
              rect(36,775,708,94,'#F4F7FA','#ABC3D3'),
              t(65,816,'[(3,2)] = [(1,0)] = 1',30,GREEN,700),
              t(65,850,'Por tanto, 3 + (−2) = 1.',22,INK,700)]
    return shell(780,900,'F03: sumar y normalizar','Secuencia de tres pasos: elegir pares normalizados (3,0) y (0,2); sumar coordenadas para obtener (3,2); sustituir ese representante por (1,0) de su misma clase, pues (3,2), (2,1) y (1,0) son pares naturales equivalentes. Resultado: 3 más menos dos es uno.', ''.join(parts))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='.');args=ap.parse_args();out=Path(args.output_dir);out.mkdir(parents=True,exist_ok=True)
    files={'MA-ART-0018-F01.svg':f01(),'MA-ART-0018-F02.svg':f02(),'MA-ART-0018-F03.svg':f03()}
    for fn,content in files.items():
        dest=out/fn;dest.write_text(content,encoding='utf-8');print(fn,dest.stat().st_size,sha256(dest.read_bytes()).hexdigest())

if __name__=='__main__':main()
