"""Figuras fuente, reproducibles, del MA-ART-0017 M04.
Obra original: figuras analíticas con datos matemáticos verificables.
Se producen SVG accesibles y PNG de respaldo en desktop/mobile.
Requisitos: matplotlib, numpy. No se utiliza IA generativa ni material ajeno.
"""
from pathlib import Path
import re
import textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
from matplotlib import rcParams

HERE=Path(__file__).resolve().parent
OUT=HERE if HERE.name=='MA-ART-0017 - Integrales - assets' else HERE/'MA-ART-0017 - Integrales - assets'
OUT.mkdir(parents=True,exist_ok=True)
BG='#f7f7f5'; INK='#202124'; MUTE='#5f6368'; AX='#4b5563'
BLUE='#4c78a8'; GREEN='#08783f'; RED='#b3261e'; ORANGE='#be650a'; PURPLE='#75499c'
rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','font.size':12,'axes.edgecolor':AX,
                 'axes.labelcolor':INK,'xtick.color':AX,'ytick.color':AX,'text.color':INK,
                 'savefig.facecolor':BG,'figure.facecolor':BG})
records=[]

def figbase(num, mobile, caption):
    if mobile:
        fig=plt.figure(figsize=(6.1,10.0),dpi=110,facecolor=BG)
        fig.text(.05,.976,f'MA-ART-0017 · FIGURA {num:02}',fontsize=10,color=MUTE,ha='left',va='top',weight='bold')
        fig.text(.05,.948,textwrap.fill(caption,width=34,break_long_words=False),fontsize=16,color=INK,ha='left',va='top',weight='bold',linespacing=1.18)
    else:
        fig=plt.figure(figsize=(12.0,5.5),dpi=110,facecolor=BG)
        fig.text(.04,.965,f'MA-ART-0017 · FIGURA {num:02}',fontsize=11,color=MUTE,ha='left',va='top',weight='bold')
        fig.text(.04,.914,caption,fontsize=22,color=INK,ha='left',va='top',weight='bold')
    return fig

def axes_style(ax, xlim, ylim, xticks=None, yticks=None):
    ax.set_facecolor(BG);ax.set_xlim(*xlim);ax.set_ylim(*ylim)
    for edge in ['top','right']:ax.spines[edge].set_visible(False)
    for edge in ['left','bottom']:ax.spines[edge].set_color('#94a3b8')
    ax.axhline(0,color=AX,lw=1.2,alpha=.9,zorder=1)
    if xticks is not None:ax.set_xticks(xticks)
    if yticks is not None:ax.set_yticks(yticks)
    ax.tick_params(labelsize=10,length=3)
    ax.grid(alpha=.1,ls=':',zorder=0)

def add_caption(fig, text, mobile):
    y=.025 if mobile else .037
    fig.text(.05 if mobile else .04,y,text,fontsize=10.8 if mobile else 10.6,color=MUTE,va='bottom',ha='left')

def write(fig,num,slug,mobile,title,desc):
    fname=f'MA-ART-0017-F{num:02}_{slug}' + ('-mobile' if mobile else '')
    svg=OUT/(fname+'.svg');png=OUT/(fname+'.png')
    fig.savefig(svg,facecolor=BG,format='svg',dpi=110)
    fig.savefig(png,facecolor=BG,format='png',dpi=140)
    plt.close(fig)
    s=svg.read_text()
    k=re.search(r'<svg\s[^>]*>',s,re.S)
    assert k is not None
    old=k.group();new=old[:-1]+' role="img" aria-labelledby="title-ma-'+str(num)+('-mobile' if mobile else '')+' desc-ma-'+str(num)+('-mobile' if mobile else '')+'">'
    def esc(x):return x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    suf='-mobile' if mobile else ''
    a=(f'<title id="title-ma-{num}{suf}">{esc(title)}</title>\n'
       f'<desc id="desc-ma-{num}{suf}">{esc(desc)}</desc>\n')
    s=s.replace(old,new+a,1);svg.write_text(s)
    records.append((fname+'.svg',fname+'.png'))

# F01: 1 signed net vs unsigned area
for mobile in (False,True):
    fig=figbase(1,mobile,'Balance con signo y área geométrica')
    if mobile:pos=[(0.14,.555,.72,.29),(0.14,.16,.72,.29)];fs=14
    else:pos=[(.075,.25,.375,.52),(.565,.25,.375,.52)];fs=14
    x=np.linspace(-1,1,301)
    for j,p in enumerate(pos):
        ax=fig.add_axes(p)
        y=x if j==0 else np.abs(x)
        axes_style(ax,(-1.12,1.12),(-1.15,1.27),[-1,0,1],[-1,0,1])
        if j==0:
            ax.fill_between(x,x,0,where=x<0,facecolor=BLUE,alpha=.33,hatch='///',edgecolor=BLUE,zorder=2)
            ax.fill_between(x,x,0,where=x>0,facecolor=ORANGE,alpha=.28,hatch='\\\\',edgecolor=ORANGE,zorder=2)
            ax.text(-.58,-.37,'−1/2',fontsize=fs,color=BLUE,ha='center',weight='bold')
            ax.text(.58,.34,'+1/2',fontsize=fs,color=ORANGE,ha='center',weight='bold')
            ax.set_title('Integral de x: −1/2 + 1/2 = 0',fontsize=13.2,pad=12,weight='bold')
        else:
            ax.fill_between(x,y,0,facecolor=GREEN,alpha=.22,hatch='...',edgecolor=GREEN,zorder=2)
            ax.text(0,.37,'1/2 + 1/2 = 1',fontsize=fs,color=GREEN,ha='center',weight='bold')
            ax.set_title('Integral de |x|: área total = 1',fontsize=13.2,pad=12,weight='bold')
        ax.plot(x,y,color=INK,lw=2.6,zorder=4)
        ax.text(1.03,-.12,'x',fontsize=11,color=MUTE)
    add_caption(fig,'Misma gráfica de partida; distinta operación de lectura.',mobile)
    write(fig,1,'balance-y-area',mobile,'Integral con signo frente al área geométrica','En el intervalo de -1 a 1, f(x)=x produce dos triángulos de áreas 1/2. La integral con signo suma -1/2 y +1/2 y vale cero. El integral de |x| suma ambas áreas y vale 1.')

# F02: sumas de Riemann (extremo derecho) y límite
for mobile in (False,True):
    fig=figbase(2,mobile,'La integral de Riemann pesa cada contribución')
    if mobile:pp=(.14,.49,.75,.30);tx=.08;ty=.36;fs=13.5
    else:pp=(.08,.23,.56,.55);tx=.695;ty=.705;fs=13.5
    ax=fig.add_axes(pp)
    x=np.linspace(0,1,301);y=1+x*x
    axes_style(ax,(-.03,1.12),(0,2.2),[0,.25,.5,.75,1],[0,1,2])
    for i in range(8):
        L=i/8;R=(i+1)/8;v=1+R*R
        is_focus=(i==4)
        ax.add_patch(Rectangle((L,0),1/8,v,edgecolor=ORANGE if is_focus else BLUE,
                               facecolor='#f5d7aa' if is_focus else '#cbdff0',lw=1.6,alpha=.88,zorder=2))
    ax.plot(x,y,color=INK,lw=2.6,zorder=4)
    ax.set_xlabel('posición x',fontsize=11)
    ax.set_ylabel('f(x) = 1 + x²',fontsize=11)
    fig.text(tx,ty,'Cada rectángulo:',fontsize=fs,weight='bold',color=INK)
    fig.text(tx,ty-.095 if not mobile else ty-.05,'valor f(ξᵢ) × anchura Δxᵢ',fontsize=fs-1,color=MUTE)
    fig.text(tx,ty-.195 if not mobile else ty-.10,'Δxᵢ = 1/8  (ocho partes)',fontsize=fs-1,color=BLUE)
    fig.text(tx,ty-.30 if not mobile else ty-.15,'S₈ = 179/128 ≈ 1,3984',fontsize=fs-1,weight='bold',color=INK)
    fig.text(tx,ty-.395 if not mobile else ty-.20,'Límite: ∫₀¹ (1+x²)dx = 4/3',fontsize=fs-1,color=GREEN)
    add_caption(fig,'La suma dibujada es una aproximación, no la integral exacta.',mobile)
    write(fig,2,'riemann-pesos',mobile,'Riemann: producto de valor por anchura','Ocho rectángulos de extremo derecho para f(x)=1+x al cuadrado en el intervalo de cero a uno. Cada área es el valor de f en el extremo derecho multiplicado por 1/8. La suma vale 179/128 y aproxima la integral 4/3.')

# F04: integrando idéntico, medidas diferentes
for mobile in (False,True):
    fig=figbase(4,mobile,'Misma función, distinta medida')
    if mobile:poss=[(.16,.60,.7,.22),(.16,.22,.7,.22)];fs=12
    else:poss=[(.075,.24,.38,.51),(.565,.24,.38,.51)];fs=12
    x=np.linspace(0,1,301);y=1+x*x
    for j,p in enumerate(poss):
        ax=fig.add_axes(p)
        axes_style(ax,(-.08,1.12),(0,2.25),[0,.5,1],[0,1,2]);ax.plot(x,y,color=INK,lw=2.5,zorder=4)
        if j==0:
            ax.fill_between(x,0,y,facecolor=BLUE,edgecolor=BLUE,alpha=.24,zorder=2)
            ax.set_title('Lebesgue: dλ (o dx)',fontsize=14,pad=10,weight='bold')
            ax.text(.56,.43,'4/3',fontsize=18,color=BLUE,ha='center',weight='bold')
        else:
            ax.vlines([0,1],[0,0],[1,2],lw=4,color=ORANGE,zorder=3)
            ax.scatter([0,1],[1,2],s=[110,110],color=ORANGE,zorder=6)
            ax.text(.05,1.19,'f(0) = 1',fontsize=fs,color=ORANGE)
            ax.text(.56,1.78,'f(1) = 2',fontsize=fs,color=ORANGE)
            ax.set_title('Átomos: μ = δ₀ + δ₁',fontsize=14,pad=10,weight='bold')
            ax.text(.38,.40,'1 + 2 = 3',fontsize=15,color=ORANGE,ha='center',weight='bold')
    add_caption(fig,'No cambiamos f; cambiamos cómo se pesa el dominio.',mobile)
    write(fig,4,'medida-longitud-dirac',mobile,'Integral de la misma función con medidas distintas','f(x)=1+x al cuadrado en [0,1]. Respecto a Lebesgue, el área bajo la curva es 4/3. Respecto a la medida δ en 0 más δ en 1, sólo contribuyen los valores f(0)=1 y f(1)=2; la integral es 3.')

# F03: functional vs accumulation operator
for mobile in (False,True):
    fig=figbase(3,mobile,'Una integral puede devolver un número o una función')
    if mobile:
        pos1=(.18,.66,.65,.17);pos2=(.18,.32,.65,.19);headx=.08
    else:
        pos1=(.055,.27,.28,.48);pos2=(.66,.27,.28,.48);headx=.39
    x=np.linspace(0,1,150)
    a=fig.add_axes(pos1);axes_style(a,(-.08,1.12),(-.05,1.16),[0,.5,1],[0,.5,1]);a.plot(x,x,color=BLUE,lw=3);a.fill_between(x,0,x,alpha=.12,color=BLUE);a.set_title('Entrada: f(s) = s',fontsize=13,weight='bold',pad=10)
    b=fig.add_axes(pos2);axes_style(b,(-.08,1.12),(-.05,.64),[0,.5,1],[0,.25,.5]);b.plot(x,.5*x*x,color=GREEN,lw=3);b.set_title('Salida: (Tf)(t) = t²/2',fontsize=13,weight='bold',pad=10)
    if mobile:
        fig.text(.14,.61,'I(f) = ∫₀¹f(s)ds = 1/2',fontsize=14,weight='bold',color=ORANGE)
        fig.text(.14,.56,'Funcional → número',fontsize=12,color=MUTE)
        fig.text(.14,.275,'T(f)(t) = ∫₀ᵗf(s)ds',fontsize=13,weight='bold',color=GREEN)
        fig.text(.14,.235,'Operador → función de t',fontsize=12,color=MUTE)
    else:
        fig.text(headx,.676,'I(f) = 1/2',fontsize=19,color=ORANGE,weight='bold')
        fig.text(headx,.57,'funcional: escalar',fontsize=12,color=MUTE)
        fig.text(headx,.431,'T(f)(t) = ∫₀ᵗs ds',fontsize=14,color=GREEN,weight='bold')
        fig.text(headx,.337,'operador: función',fontsize=12,color=MUTE)
        fig.text(.35,.5,'→',fontsize=24,color=MUTE)
        fig.text(.60,.5,'→',fontsize=24,color=MUTE)
    add_caption(fig,'La variable s está ligada; t permanece libre en Tf(t).',mobile)
    write(fig,3,'funcional-operador',mobile,'Un funcional devuelve un escalar y un operador de acumulación devuelve una función','Para f(s)=s en [0,1], I(f) igual a la integral de cero a uno es un medio. El operador T con Tf(t)=integral de cero a t de s ds produce la función t al cuadrado dividido por dos.')

# F05: circle orientation and length
for mobile in (False,True):
    fig=figbase(5,mobile,'La orientación cambia el trabajo, no la longitud')
    if mobile:poss=[(.18,.55,.64,.24),(.18,.18,.64,.24)]
    else:poss=[(.15,.185,.30,.535),(.59,.185,.30,.535)]
    th=np.linspace(0,2*np.pi,400)
    for j,p in enumerate(poss):
        ax=fig.add_axes(p);ax.set_aspect('equal');ax.set_xlim(-1.31,1.31);ax.set_ylim(-1.3,1.3)
        ax.set_facecolor(BG);ax.axis('off')
        ax.axhline(0,color='#a7b2be',lw=.8);ax.axvline(0,color='#a7b2be',lw=.8)
        ax.plot(np.cos(th),np.sin(th),color=INK,lw=2.8)
        c=GREEN if j==0 else RED
        for angle in [.35,2.2,4.2]:
            v=1 if j==0 else -1
            t0=angle;dt=.26*v
            ax.annotate('',xy=(np.cos(t0+dt),np.sin(t0+dt)),xytext=(np.cos(t0),np.sin(t0)),
                        arrowprops={'arrowstyle':'-|>','mutation_scale':18,'lw':2.5,'color':c})
        ax.text(0,0.17,'∫ 1 ds = 2π',ha='center',fontsize=13,color=INK,weight='bold')
        ax.text(0,-.18,'∫ F·dr = '+('+2π' if j==0 else '−2π'),ha='center',fontsize=13,color=c,weight='bold')
        ax.set_title('Antihorario' if j==0 else 'Horario',fontsize=14,weight='bold',color=c,pad=13)
    add_caption(fig,'Campo tangencial F(x,y)=(-y,x); una vuelta de la circunferencia unitaria.',mobile)
    write(fig,5,'curva-orientacion',mobile,'Trabajo de campo tangencial cambia con sentido de recorrido','En la circunferencia unitaria y para el campo F(x,y)=(-y,x), una vuelta antihoraria produce integral de trabajo +2 pi y una vuelta horaria -2 pi. La integral escalar de 1 respecto de longitud vale 2 pi en ambos recorridos.')

# F06: x squared map traversed twice
for mobile in (False,True):
    fig=figbase(6,mobile,'Cambio de variable: signo frente a multiplicidad')
    pp=(.13,.43,.75,.42) if mobile else (.08,.22,.56,.57)
    ax=fig.add_axes(pp)
    xs=np.linspace(-1,1,401);ax.set_xlim(-1.16,1.15);ax.set_ylim(-.08,1.21)
    ax.set_facecolor(BG);ax.axhline(0,color=AX,lw=1);ax.axvline(0,color=AX,lw=1)
    ax.set_xticks([-1,0,1]);ax.set_yticks([0,1]);ax.tick_params(labelsize=12)
    for ed in ['right','top']:ax.spines[ed].set_visible(False)
    L=np.linspace(-1,0,210);R=np.linspace(0,1,210)
    ax.plot(L,L*L,color=BLUE,lw=4,label='1 → 0 (baja)');ax.plot(R,R*R,color=ORANGE,lw=4,label='0 → 1 (sube)')
    for t,c in [(-.68,BLUE),(.68,ORANGE)]:
        d=.10
        ax.annotate('',xy=(t+d,(t+d)**2),xytext=(t,t*t),arrowprops={'arrowstyle':'-|>','color':c,'lw':3,'mutation_scale':18})
    ax.scatter([-1,0,1],[1,0,1],color=[BLUE,INK,ORANGE],s=55,zorder=6)
    ax.text(-.91,1.045,'1',color=BLUE,fontsize=13,weight='bold');ax.text(.9,1.045,'1',color=ORANGE,fontsize=13,weight='bold')
    ax.set_xlabel('x',fontsize=13);ax.set_ylabel('u = x²',fontsize=13)
    if mobile:
        fig.text(.08,.345,'Integral orientada:  ∫ 2x dx = 0',fontsize=13.5,color=BLUE,weight='bold')
        fig.text(.08,.282,'Variación total:  ∫ 2|x| dx = 2',fontsize=13.5,color=ORANGE,weight='bold')
        fig.text(.08,.222,'Longitud de la imagen [0,1]: 1',fontsize=12.5,color=INK)
    else:
        fig.text(.68,.65,'Partida: u = 1',fontsize=15,color=INK,weight='bold')
        fig.text(.68,.56,'Mínimo: u = 0',fontsize=14,color=MUTE)
        fig.text(.68,.47,'Llegada: u = 1',fontsize=14,color=INK,weight='bold')
        fig.text(.68,.34,'∫ 2x dx = 0',fontsize=14,color=BLUE,weight='bold')
        fig.text(.68,.255,'∫ 2|x| dx = 2',fontsize=14,color=ORANGE,weight='bold')
        fig.text(.68,.17,'Imagen [0,1]: longitud 1',fontsize=12,color=INK)
    add_caption(fig,'Las integrales indicadas van de −1 a 1; la curva baja y vuelve a subir.',mobile)
    write(fig,6,'sustitucion-multiplicidad',mobile,'Mapa x al cuadrado con signos y multiplicidad','Para u=x al cuadrado en [-1,1], el recorrido desde u=1 baja a cero y vuelve a u=1. La integral orientada de la derivada 2x vale cero. La integral de |2x| vale 2, porque cuenta dos recorridos de longitud 1; el conjunto imagen [0,1] tiene longitud 1.')

# F07: area recovered as Tonelli
for mobile in (False,True):
    fig=figbase(7,mobile,'El área vuelve a aparecer como un teorema')
    pp=(.14,.43,.72,.40) if mobile else (.08,.20,.56,.62)
    ax=fig.add_axes(pp)
    x=np.linspace(0,1,501);y=x*x
    ax.set_facecolor(BG);ax.set_xlim(0,1.12);ax.set_ylim(0,1.13)
    ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
    ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1]);ax.tick_params(labelsize=12)
    ax.plot(x,y,color=INK,lw=3)
    ax.fill_between(x,0,y,color=GREEN,alpha=.24,hatch='///',edgecolor=GREEN)
    for xx in [.18,.35,.53,.7,.86]:ax.vlines(xx,0,xx*xx,color=GREEN,lw=2,alpha=.65)
    ax.set_xlabel('x',fontsize=13);ax.set_ylabel('y',fontsize=13)
    ax.text(.74,.40,'E',color=GREEN,fontsize=20,weight='bold')
    if mobile:
        fig.text(.08,.33,'E = {(x,y): 0 ≤ x ≤ 1; 0 ≤ y ≤ x²}',fontsize=11.4,weight='bold')
        fig.text(.08,.275,'∬ 1_E dλ₂ = λ₂(E) = 1/3',fontsize=12.5,color=GREEN,weight='bold')
        fig.text(.08,.216,'∫₀¹ x²dx = 1/3',fontsize=13.5,color=BLUE,weight='bold')
    else:
        fig.text(.68,.63,'E: subgráfico de x²',fontsize=14,weight='bold')
        fig.text(.68,.52,'∬ 1_E dλ₂ = λ₂(E)',fontsize=12.3,color=GREEN,weight='bold')
        fig.text(.68,.39,'∫₀¹ x²dx = 1/3',fontsize=15,color=BLUE,weight='bold')
        fig.text(.68,.27,'Dos integrales para una',fontsize=12,color=MUTE)
        fig.text(.68,.22,'misma medida geométrica.',fontsize=12,color=MUTE)
    add_caption(fig,'Tonelli relaciona las secciones verticales con la medida bidimensional.',mobile)
    write(fig,7,'area-por-tonelli',mobile,'Área del subgráfico como integral en dos dimensiones','La región E debajo de y=x al cuadrado para 0 menor o igual que x menor o igual que 1 se sombrea. Su medida bidimensional es 1/3 y coincide con la integral de x al cuadrado respecto de x, por Tonelli.')

print('Produced',len(records),'pairs SVG/PNG')
for a,b in records:print(a,b)
