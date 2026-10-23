"""EXP003: datos finitos y reglas de continuación; animación original discreta."""
from pathlib import Path
import json
import re
import unicodedata
import sys
import numpy as np
from manim import *

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'recursos'))
from intro_canal import IntroCanal

BG, FG, MUTED = '#0F1117', '#F5F7FA', '#A7B0BE'
BLUE, VIOLET, GREEN, ORANGE = '#4EA1FF', '#B794F4', '#63D471', '#FFB454'
TEX = TexTemplate(tex_compiler='xelatex', output_format='.xdv')
config.background_color = BG
config.tex_template = TEX


class EXP003(IntroCanal):
    def tx(self, text, size=30, color=FG):
        return Tex(text, font_size=size, color=color, tex_template=TEX)

    def mx(self, text, size=42, color=FG):
        return MathTex(text, font_size=size, color=color, tex_template=TEX)

    def cue(self, name, offset=0):
        target = self.cues[name]['inicio'] + offset
        if self.time > target + 1/config.frame_rate + 1e-4:
            raise ValueError(f'SYNC WARN {name}: {self.time:.4f} > {target:.4f}')
        if target-self.time > 1e-5:
            self.wait(target-self.time)

    WORD_ANCHORS = {
        ('pregunta', .4): ('Cada dato', 0),
        ('pregunta', .73): ('Qué podemos', 0),
        ('regla_a', .3): ('a sub', 0),
        ('primeros', .16): ('obtenemos uno', 1),
        ('primeros', .265): ('un medio', 0),
        ('primeros', .37): ('un tercio', 0),
        ('primeros', .475): ('un cuarto', 0),
        ('primeros', .66): ('Cada paso', 0),
        ('regla_b', .14): ('sub n', 1),
        ('regla_b', .26): ('Hasta el índice', 0),
        ('regla_b', .62): ('uno dividido', 0),
        ('segunda_rama', .65): ('su valor es uno', 0),
        ('comunes', .24): ('En cada índice', 0),
        ('comunes', .5): ('las dos alturas', 0),
        ('cuenta', .35): ('más el término de índice cero', 0),
        ('frontera', .25): ('En n', 0),
        ('frontera', .54): ('ambas sucesiones valen', 0),
        ('siguiente', .22): ('Ahora', 0),
        ('siguiente', .53): ('La primera sucesión', 0),
        ('salto', .12): ('toma el valor uno', 0),
        ('salto', .43): ('Aquí aparece', 0),
        ('respuesta_muestra', .44): ('Para conocer', 0),
        ('generalizacion', .21): ('cualquier longitud finita', 0),
        ('generalizacion', .46): ('Después de su último índice', 0),
        ('generalizacion', .72): ('mantenemos la primera regla', 0),
        ('alcance', .08): ('una muestra finita', 0),
        ('alcance', .38): ('deja abiertas continuaciones', 0),
        ('alcance', .66): ('La información decisiva', 0),
        ('final', .24): ('qué ocurre', 0),
        ('final', .42): ('todos los términos', 0),
        ('final', .76): ('Aprenderemos', 0),
    }

    @staticmethod
    def normalized(word):
        word=''.join(c for c in unicodedata.normalize('NFD',word.lower()) if unicodedata.category(c)!='Mn')
        word=re.sub(r'[^a-z0-9]', '', word)
        return {'0':'cero','1':'uno','2':'dos','3':'tres','n':'ene'}.get(word,word)

    def word(self, name, phrase, selected=0, fallback=.25, last=False):
        words=self.alignments.get(name, {}).get('words', [])
        expected=[self.normalized(w) for w in phrase.split()]
        actual=[self.normalized(w['word']) for w in words]
        matches=[i for i in range(len(words)-len(expected)+1) if actual[i:i+len(expected)]==expected]
        if matches:
            i=matches[-1] if last else matches[0]
            offset=words[i+selected]['start']
            mode='palabra_ASR'
        else:
            c=self.cues[name]
            offset=fallback*(c['fin_voz']-c['inicio'])
            mode='fraccion_preliminar'
        self.anchor_log.append(dict(cue=name,phrase=phrase,offset=offset,metodo=mode))
        self.cue(name,offset)

    def at(self, name, fraction):
        key=(name,round(fraction,3))
        if key in self.WORD_ANCHORS:
            phrase, selected=self.WORD_ANCHORS[key]
            self.word(name,phrase,selected,fallback=fraction)
        else:
            c=self.cues[name]
            self.cue(name, fraction*(c['fin_voz']-c['inicio']))

    def event(self, name, anchor):
        self.events.append({'id': name, 'inicio': round(self.time, 6), 'anclaje': anchor})

    def body_clear(self, keep=()):
        objects = [m for m in self.mobjects if m not in [self.title, self.rule, *keep]]
        if objects:
            self.play(*[FadeOut(m) for m in objects], run_time=.25)

    def heading(self, title):
        new = self.tx(title, 36).move_to([0,3.45,0])
        if hasattr(self,'title'):
            self.play(FadeOut(self.title),run_time=.18)
        self.title=new
        self.play(Write(new),run_time=.5)

    def construct(self):
        timeline = json.loads((ROOT/'generados/timing_produccion.json').read_text(encoding='utf8'))
        self.cues={c['id']:c for c in timeline['cues']}
        self.events=[]
        self.anchor_log=[]
        alignment=ROOT/'generados/alineacion_clips.json'
        self.alignments={c['id']:c for c in json.loads(alignment.read_text(encoding='utf8'))['clips']} if alignment.exists() else {}
        IntroCanal.construct(self)
        # La intro institucional existente suma exactamente siete segundos.
        assert abs(self.time-7)<1/config.frame_rate+1e-4
        self.clear()
        self.rule=Line([-5.5,3.08,0],[5.5,3.08,0],color=MUTED,stroke_width=1)
        self.cue('pregunta')
        self.heading('¿Hasta dónde llegan los datos?')
        self.play(Create(self.rule),run_time=.25)
        initial=VGroup(*[Dot([-4.2+i*1.4,.8,0],radius=.065,color=BLUE) for i in range(7)])
        rings=VGroup(*[Circle(radius=.11,color=VIOLET,stroke_width=2.3).move_to(d) for d in initial])
        self.play(LaggedStart(*[FadeIn(d) for d in initial],lag_ratio=.15),run_time=1.2)
        self.at('pregunta',.4)
        self.play(LaggedStart(*[Create(r) for r in rings],lag_ratio=.13),run_time=1)
        self.at('pregunta',.73)
        question=self.mx('?',70,ORANGE).move_to([0,-.8,0])
        self.event('pregunta_inicial','¿Qué podemos afirmar?')
        self.play(Write(question),run_time=.5)

        self.cue('regla_a')
        self.body_clear()
        self.heading('Una regla, término a término')
        self.at('regla_a',.3)
        formula=self.mx(r'a_n=\frac{1}{n+1}',50,BLUE).move_to([0,2.1,0])
        self.event('formula_a','a sub ene es uno dividido por la suma de ene y uno')
        self.play(Write(formula),run_time=1.1)
        self.cue('naturales')
        nzero=self.mx('n=0',36,ORANGE).move_to([0,.7,0])
        self.word('naturales','empieza en cero',fallback=.16)
        self.play(Write(nzero),run_time=.5)
        natural_domain=self.mx(r'n\in\mathbb N',34,MUTED).move_to([0,1.0,0])
        self.word('naturales','números naturales',fallback=.42)
        self.play(FadeOut(nzero),run_time=.15)
        self.play(Write(natural_domain),run_time=.4)
        naturals=VGroup(*[self.mx(v,34,MUTED).move_to([-2+i,-.1,0]) for i,v in enumerate(['0','1','2','3',r'\ldots'])])
        for i,(phrase,position) in enumerate([('naturales cero',1),('uno dos',0),('dos tres',0),('tres y',0),('así sucesivamente',0)]):
            self.word('naturales',phrase,position,fallback=.57+i*.065)
            self.play(Write(naturals[i]),run_time=.23)
        natural=VGroup(natural_domain,naturals)
        self.cue('primeros')
        self.play(FadeOut(natural),run_time=.25)
        xs=[-4.5,-1.5,1.5,4.5]
        indices=VGroup(*[self.mx(f'n={i}',30,MUTED).move_to([x,.75,0]) for i,x in enumerate(xs)])
        values=VGroup(*[self.mx(v,46,BLUE).move_to([x,-.3,0]) for x,v in zip(xs,['1',r'\frac12',r'\frac13',r'\frac14'])])
        self.play(FadeIn(indices),run_time=.35)
        for i in range(4):
            self.at('primeros',.16+i*.105)
            self.event(f'termino_{i}',f'valor a_{i}')
            self.play(Write(values[i]),run_time=.4)
        denominator=self.mx(r'1<2<3<4',34,ORANGE).move_to([0,-1.65,0])
        self.at('primeros',.66)
        self.play(Write(denominator),run_time=.6)
        self.cue('discretos')
        self.play(FadeOut(indices),FadeOut(values),FadeOut(denominator),run_time=.25)
        axes=Axes(x_range=[0,8,1],y_range=[0,1.2,.5],x_length=9,y_length=2.7,tips=False,
                  axis_config={'color':MUTED,'stroke_width':1.2,'include_ticks':True}).move_to([0,-.35,0])
        labels=VGroup(*[self.mx(str(i),25,MUTED).next_to(axes.c2p(i,0),DOWN,buff=.14) for i in [0,2,4,6,8]])
        labs=VGroup(self.mx('n',28,MUTED).next_to(axes,RIGHT,buff=.15),self.mx('a_n',28,BLUE).next_to(axes,UL,buff=.1))
        ylabels=VGroup(*[self.mx(v,24,MUTED).next_to(axes.c2p(0,y),LEFT,buff=.13) for y,v in [(1,'1'),(.5,r'\frac12')]])
        self.play(Create(axes),FadeIn(labels),FadeIn(labs),FadeIn(ylabels),run_time=.7)
        points=VGroup(*[Dot(axes.c2p(i,1/(i+1)),radius=.055,color=BLUE) for i in range(9)])
        self.at('discretos',.2)
        selector=Circle(radius=.12,color=ORANGE,stroke_width=2).move_to(points[0])
        self.play(FadeIn(points[0]),Create(selector),run_time=.35)
        for i in range(1,9):
            self.at('discretos',.25+i*.065)
            self.play(FadeIn(points[i]),selector.animate.move_to(points[i]),run_time=.3)
        self.event('grafico_discreto','puntos se acercan a la altura cero')

        self.cue('regla_b')
        self.body_clear()
        self.heading('Dos reglas de continuación')
        a_ref=self.mx(r'a_n=\frac{1}{n+1}',34,BLUE).move_to([-3.8,2.15,0])
        self.play(Write(a_ref),run_time=.25)
        self.at('regla_b',.14)
        bhead=self.mx('b_n=',46,VIOLET).move_to([-3.3,.25,0])
        brace=self.mx(r'\left\{\vphantom{\begin{matrix}\dfrac11\\\dfrac11\end{matrix}}\right.',48,VIOLET).move_to([-2.2,-.1,0])
        self.play(Write(bhead),Write(brace),run_time=.4)
        condition1=self.mx(r'0\leq n\leq10^6',35,GREEN).move_to([2.45,.45,0])
        self.at('regla_b',.26)
        self.event('condicion_comun','hasta el índice un millón incluido')
        self.play(Write(condition1),run_time=.8)
        val1=self.mx(r'\dfrac1{n+1}',42,VIOLET).move_to([-.7,.45,0])
        self.at('regla_b',.62)
        self.play(Write(val1),run_time=.9)
        self.cue('segunda_rama')
        condition2=self.mx(r'n>10^6',35,ORANGE).move_to([2.45,-.9,0])
        self.event('condicion_posterior','índices mayores que un millón')
        self.play(Write(condition2),run_time=.8)
        self.at('segunda_rama',.65)
        val2=self.mx('1',44,VIOLET).move_to([-.7,-.9,0])
        self.event('segunda_rama_valor','su valor es uno')
        self.play(Write(val2),run_time=.5)

        self.cue('comunes')
        self.body_clear()
        self.heading('Un tramo común muy largo')
        domain=self.mx(r'0\le n\le10^6',38,GREEN).move_to([0,2.2,0])
        self.play(Write(domain),run_time=.65)
        viewlabel=self.tx('Esquema de índices',26,MUTED).move_to([0,1.2,0])
        self.play(Write(viewlabel),run_time=.4)
        stripxs=[-4.8,-3.2,-1.6,1.1,4.6]
        indtexts=['0','1','2',r'\cdots','10^6']
        striplabels=VGroup(*[self.mx(v,34,MUTED).move_to([x,-.25,0]) for x,v in zip(stripxs,indtexts)])
        paired=VGroup(*[VGroup(Dot([x,.35,0],radius=.065,color=BLUE),Circle(radius=.115,color=VIOLET,stroke_width=2).move_to([x,.35,0])) for x in [-4.8,-3.2,-1.6,4.6]])
        self.play(FadeIn(striplabels),run_time=.45)
        self.at('comunes',.24)
        self.play(LaggedStart(*[FadeIn(m) for m in paired],lag_ratio=.25),run_time=.65)
        equality=self.mx('a_n=b_n',44,GREEN).move_to([0,-1.5,0])
        omitted=self.tx('Tramo intermedio omitido',24,MUTED).move_to([.6,.55,0])
        self.at('comunes',.5)
        self.event('igualdad_comun','en cada índice las dos alturas coinciden')
        self.play(Write(equality),Write(omitted),run_time=.8)
        self.at('comunes',.75)
        self.play(Indicate(domain,color=GREEN,scale_factor=1.025),run_time=.55)
        self.cue('cuenta')
        under=BraceBetweenPoints([-5,-.75,0],[5,-.75,0],direction=DOWN,color=GREEN)
        self.play(Create(under),run_time=.7)
        self.at('cuenta',.35)
        self.play(FadeOut(equality),run_time=.2)
        count=self.mx(r'10^6+1=1\,000\,001\quad\text{términos}',40,GREEN).move_to([0,-1.8,0])
        self.event('conteo_inclusivo','un millón de términos más el término de índice cero')
        self.play(Write(count),run_time=1.1)

        self.cue('frontera')
        self.body_clear()
        self.heading('La frontera exacta')
        tablabel=self.tx('Tabla de valores',28,MUTED).move_to([0,2.25,0])
        self.play(Write(tablabel),run_time=.5)
        ar=self.mx('a_n',40,BLUE).move_to([-5.25,.3,0]);br=self.mx('b_n',40,VIOLET).move_to([-5.25,-1.1,0])
        self.play(Write(ar),Write(br),run_time=.45)
        self.at('frontera',.25)
        oldn=self.mx(r'n=10^6',39,ORANGE).move_to([-2.35,1.4,0])
        self.event('indice_frontera','ene igual a un millón')
        self.play(Write(oldn),run_time=.6)
        olda=self.mx(r'\frac1{10^6+1}',44,BLUE).move_to([-2.35,.3,0])
        oldb=self.mx(r'\frac1{10^6+1}',44,VIOLET).move_to([-2.35,-1.1,0])
        self.at('frontera',.54)
        self.play(Write(olda),Write(oldb),run_time=1)
        oldbox=SurroundingRectangle(VGroup(oldn,olda,oldb),buff=.25,color=GREEN,stroke_width=1.5)
        self.at('frontera',.83)
        self.play(Create(oldbox),run_time=.5)
        self.cue('siguiente')
        arrow=Arrow([-.75,1.4,0],[.65,1.4,0],buff=.12,color=ORANGE)
        self.play(GrowArrow(arrow),run_time=.5)
        self.at('siguiente',.22)
        nextn=self.mx(r'n=10^6+1',39,ORANGE).move_to([2.75,1.4,0])
        self.event('indice_siguiente','ene vale un millón más uno')
        self.play(Write(nextn),run_time=.75)
        nexta=self.mx(r'\frac1{10^6+2}',44,BLUE).move_to([2.75,.3,0])
        self.at('siguiente',.53)
        self.event('valor_a_siguiente','primera sucesión uno dividido por la suma de un millón y dos')
        self.play(Write(nexta),run_time=.9)
        self.cue('salto')
        nextb=self.mx('1',48,VIOLET).move_to([2.75,-1.1,0])
        self.at('salto',.12)
        self.event('valor_b_salto','segunda toma el valor uno')
        self.play(Write(nextb),run_time=.6)
        self.at('salto',.43)
        separated=SurroundingRectangle(VGroup(nexta,nextb),buff=.3,color=ORANGE,stroke_width=2)
        self.play(Create(separated),run_time=.65)
        self.cue('despues')
        self.play(FadeOut(oldbox),FadeOut(separated),run_time=.25)
        for k,frac in [(2,.2),(3,.5),(4,.73)]:
            self.at('despues',frac)
            nn=self.mx(fr'n=10^6+{k}',39,ORANGE).move_to(nextn)
            aa=self.mx(fr'\frac1{{10^6+{k+1}}}',44,BLUE).move_to(nexta)
            self.play(FadeOut(nextn),FadeOut(nexta),run_time=.15)
            self.play(Write(nn),Write(aa),Indicate(nextb,color=VIOLET,scale_factor=1.035),run_time=.5)
            nextn,nexta=nn,aa
            self.event(f'continuacion_{k}','a disminuye; b permanece en uno')

        self.cue('pregunta_muestra')
        self.body_clear()
        self.heading('¿Qué aporta una muestra finita?')
        question=self.mx('?',72,ORANGE).move_to([0,.1,0])
        self.event('pregunta_muestra_visual','¿qué nos enseñó aquella larga coincidencia?')
        self.play(Write(question),run_time=.65)
        self.cue('respuesta_muestra')
        self.play(FadeOut(question),run_time=.2)
        observed=self.tx('Términos inspeccionados',36).move_to([0,1.55,0])
        eq=self.mx(r'a_n=b_n\qquad(0\le n\le10^6)',42,GREEN).move_to([0,.35,0])
        self.play(Write(observed),Write(eq),run_time=1)
        self.at('respuesta_muestra',.44)
        continuation=self.tx('Reglas de continuación',36,ORANGE).move_to([0,-1.35,0])
        self.play(Write(continuation),run_time=.8)

        self.cue('generalizacion')
        self.body_clear()
        self.heading('Cualquier tramo finito')
        scheme=self.tx('Esquema de índices',27,MUTED).move_to([0,2.25,0])
        self.play(Write(scheme),run_time=.5)
        # El espacio es esquemático: N es un corte finito, no una escala variable.
        line=Line([-5.3,.25,0],[5.3,.25,0],color=MUTED,stroke_width=1.2)
        axis_arrow=Arrow([4.9,.25,0],[5.6,.25,0],buff=0,color=MUTED,stroke_width=1.2)
        dots=VGroup(*[Dot([x,.25,0],radius=.04,color=MUTED) for x in np.linspace(-5,5,21)])
        first=self.mx('0',30,MUTED).move_to([-5,-.3,0])
        self.play(Create(line),GrowArrow(axis_arrow),FadeIn(dots),Write(first),run_time=.75)
        cutx=-.5
        window=Rectangle(width=cutx+5.35,height=1.1,color=GREEN,stroke_width=2,fill_opacity=.045).move_to([(-5.35+cutx)/2,.25,0])
        cut=self.mx('N',34,ORANGE).move_to([cutx,-.7,0])
        leftlabel=self.mx(r'a_n=b_n\quad(0\le n\le N)',34,GREEN).move_to([-2.4,1.2,0])
        self.at('generalizacion',.21)
        explanation=self.tx(r'$N$: último índice del tramo',28,ORANGE).move_to([0,-1.8,0])
        self.event('definicion_N','N es el último índice del tramo común')
        self.play(Write(explanation),run_time=.4)
        self.event('prefijo_finito','tramo común de cualquier longitud finita')
        self.play(Create(window),Write(cut),Write(leftlabel),run_time=.6)
        self.at('generalizacion',.46)
        for newx in [.5,2.0]:
            newwindow=Rectangle(width=newx+5.35,height=1.1,color=GREEN,stroke_width=2,fill_opacity=.045).move_to([(-5.35+newx)/2,.25,0])
            self.play(Transform(window,newwindow),cut.animate.move_to([newx,-.7,0]),run_time=.65)
        self.at('generalizacion',.72)
        tail=self.mx(r'n>N',34,ORANGE).move_to([4,1.2,0])
        rules=VGroup(self.mx(r'a_n=\frac1{n+1}',38,BLUE),self.mx(r'b_n=1',38,VIOLET)).arrange(RIGHT,buff=1.2).move_to([0,-1.9,0])
        self.event('reglas_despues_de_N','después del último índice mantenemos primera regla y cambiamos segunda')
        self.play(FadeOut(explanation),run_time=.2)
        self.play(Write(tail),Write(rules[0]),run_time=.6)
        self.word('generalizacion','cambiamos la segunda',fallback=.89)
        self.play(Write(rules[1]),run_time=.6)
        self.cue('alcance')
        self.at('alcance',.08)
        self.play(Indicate(window,color=GREEN,scale_factor=1.015),run_time=.65)
        self.at('alcance',.38)
        highlight=SurroundingRectangle(VGroup(tail),buff=.18,color=ORANGE,stroke_width=1.6)
        self.play(Create(highlight),run_time=.45)
        self.at('alcance',.66)
        self.play(Indicate(rules,color=ORANGE,scale_factor=1.025),run_time=.7)
        self.cue('final')
        self.heading('La pregunta que abre el límite')
        self.play(FadeOut(rules),FadeOut(leftlabel),FadeOut(highlight),run_time=.3)
        self.at('final',.24)
        q=self.mx('?',58,ORANGE).move_to([0,-1.35,0])
        prefix_dots=VGroup(*[d for d in dots if d.get_center()[0]<=2.00001])
        late_dots=VGroup(*[d for d in dots if d.get_center()[0]>2.00001])
        # Atenuar el trazo y el relleno por separado: set_opacity elevaría el
        # relleno de .045 a .18 e invertiría el foco pedagógico del cierre.
        self.play(window.animate.set_stroke(opacity=.18).set_fill(opacity=.01),
                  prefix_dots.animate.set_opacity(.25),first.animate.set_opacity(.3),
                  Write(q),run_time=.45)
        self.at('final',.42)
        conclusion=self.tx(r'Todos los términos\\suficientemente tardíos',37).move_to([0,-2.15,0])
        self.event('pregunta_final','todos los términos suficientemente tardíos')
        tailfocus=Line([2.3,-.65,0],[5.45,-.65,0],color=ORANGE,stroke_width=3)
        self.event('foco_cola','todos los términos suficientemente tardíos: puntos posteriores a N')
        self.play(Write(conclusion),Create(tailfocus),
                  *[d.animate.set_color(ORANGE).set_opacity(1).scale(1.7) for d in late_dots],
                  axis_arrow.animate.set_color(ORANGE).set_stroke(width=3),run_time=1)
        self.at('final',.76)
        end=timeline['duracion_total']
        if self.time>end+1/config.frame_rate:
            raise ValueError(f'SYNC WARN final {self.time} > {end}')
        self.wait(max(0,end-self.time))
        (ROOT/'generados/anclajes_resueltos.json').write_text(json.dumps(self.anchor_log,ensure_ascii=False,indent=2),encoding='utf8')
        (ROOT/'generados/eventos_visuales.json').write_text(json.dumps(self.events,ensure_ascii=False,indent=2),encoding='utf8')
