"""Dos planos complejos, imagen de una cuadrícula y geometría local de z²."""
from pathlib import Path
import json
import numpy as np
from manim import *

BG, FG, MUTED = '#0F1117', '#F5F7FA', '#A7B0BE'
BLUE, ORANGE, GREEN, VIOLET = '#4EA1FF', '#FFB454', '#63D471', '#B794F4'
config.background_color = BG
TEX = TexTemplate(tex_compiler='xelatex', output_format='.xdv')


def square(z):
    return z*z


class MAComplejoCuadrado(Scene):
    def math(self, value, size=36, color=FG):
        return MathTex(value, font_size=size, color=color, tex_template=TEX)

    def text(self, value, size=30, color=FG):
        return Tex(value, font_size=size, color=color, tex_template=TEX)

    def cue(self, key, offset=0):
        target = self.cues[key]['inicio'] + offset
        delta = target-self.time
        if delta < -1/config.frame_rate-1e-5:
            raise ValueError(f'SYNC WARN {key}: {self.time:.3f} > {target:.3f}')
        if delta > 1e-5:
            self.wait(delta)

    def footer(self, obj):
        obj.move_to([0,-2.45,0])
        if obj.width > 11.5:
            obj.scale_to_fit_width(11.5)
        if getattr(self,'current_footer',None) is not None:
            self.play(FadeOut(self.current_footer),run_time=.18)
        self.play(Write(obj),run_time=.65)
        self.current_footer=obj

    def path(self, plane, values, color, width=2.2):
        return VMobject(stroke_color=color,stroke_width=width,fill_opacity=0).set_points_as_corners(
            [plane.c2p(z.real,z.imag) for z in values])

    def lattice(self, plane, mapped=False):
        t=np.linspace(-1.2,1.2,97)
        group=VGroup()
        for c in np.linspace(-1.2,1.2,7):
            for vals,col in ((c+1j*t,BLUE),(t+1j*c,ORANGE)):
                group.add(self.path(plane,vals**2 if mapped else vals,col))
        return group

    def construct(self):
        timeline=json.loads((Path(__file__).parent/'generados/timing_produccion.json').read_text(encoding='utf8'))
        self.cues={c['id']:c for c in timeline['cues']+timeline['marcadores_visuales']}
        self.current_footer=None
        title=self.text(r'El plano complejo bajo $z^2$',38).move_to([0,3.4,0])
        divider=Line([-5.5,3.02,0],[5.5,3.02,0],color=MUTED,stroke_width=1.2)
        self.play(FadeIn(title),Create(divider),run_time=.8)
        # Cada panel es isotrópico; las escalas numéricas difieren y se indican.
        left=Axes(x_range=[-2,2,1],y_range=[-2,2,1],x_length=4.3,y_length=4.3,
                  tips=False,axis_config={'color':MUTED,'stroke_width':1.5}).move_to([-3.35,.3,0])
        right=Axes(x_range=[-3,3,1],y_range=[-3,3,1],x_length=4.3,y_length=4.3,
                   tips=False,axis_config={'color':MUTED,'stroke_width':1.5}).move_to([3.35,.3,0])
        headers=VGroup(self.text(r'Entrada: $z=x+iy$',28).move_to([-3.35,2.7,0]),
                       self.text(r'Salida: $w=u+iv$',28).move_to([3.35,2.7,0]))
        labels=VGroup()
        for p,real,imag in ((left,r'\operatorname{Re}z',r'\operatorname{Im}z'),
                            (right,r'\operatorname{Re}w',r'\operatorname{Im}w')):
            origin=p.c2p(0,0)
            labels.add(self.math(real,23,MUTED).next_to(p.x_axis.get_end(),DOWN,buff=.12).shift(LEFT*.25),
                       self.math(imag,23,MUTED).next_to(p.y_axis.get_end(),LEFT,buff=.12).shift(DOWN*.1))
            for val in (1,):
                labels.add(self.math(str(val),21,MUTED).next_to(p.c2p(val,0),DOWN,buff=.08))
        arrow=Arrow(LEFT*.5,RIGHT*.5,buff=0,color=FG,stroke_width=2).shift(UP*.3)
        self.cue('intro')
        self.play(Create(left),Create(right),FadeIn(headers),FadeIn(labels),GrowArrow(arrow),run_time=1.2)
        self.cue('funcion')
        self.cue('formula_funcion')
        self.footer(self.math(r'w=z^2',49,BLUE))
        self.cue('cuadricula')
        grid_left=self.lattice(left)
        grid_right=self.lattice(right)
        self.play(Create(grid_left),run_time=1.5)
        self.cue('deformacion')
        self.footer(self.math(r'z\longmapsto z^2',42))
        transition=self.text('Transición hacia la imagen',22,MUTED).move_to([3.35,-2.02,0])
        self.play(FadeIn(transition),FadeIn(grid_right),run_time=.2)
        self.play(Transform(grid_right,self.lattice(right,True)),run_time=3.0,rate_func=smooth)
        self.play(FadeOut(transition),run_time=.2)
        self.cue('parabolas')
        self.play(grid_left.animate.set_stroke(opacity=.3),grid_right.animate.set_stroke(opacity=.3),run_time=.35)
        t=np.linspace(-1.2,1.2,97)
        highlighted_left=VGroup(self.path(left,t+.8j,ORANGE,4),self.path(left,.8+1j*t,BLUE,4))
        highlighted_right=VGroup(self.path(right,(t+.8j)**2,ORANGE,4),self.path(right,(.8+1j*t)**2,BLUE,4))
        self.play(Create(highlighted_left),Create(highlighted_right),run_time=1.2)
        self.cue('ejes')
        self.play(FadeOut(highlighted_left),FadeOut(highlighted_right),run_time=.25)
        axes_left=VGroup(self.path(left,t+0j,ORANGE,4),self.path(left,1j*t,BLUE,4))
        axes_right=VGroup(self.path(right,(t+0j)**2,ORANGE,4),self.path(right,(1j*t)**2,BLUE,4))
        self.play(Create(axes_left),Create(axes_right),run_time=1.2)
        self.cue('ejemplo')
        self.play(FadeOut(grid_left),FadeOut(grid_right),FadeOut(axes_left),FadeOut(axes_right),run_time=.35)
        theta=ValueTracker(PI/4)
        radius=np.sqrt(2)
        def zval(): return radius*np.exp(1j*theta.get_value())
        def point(plane,val,col): return Dot(plane.c2p(val.real,val.imag),radius=.075,color=col).set_z_index(5)
        z_dot=always_redraw(lambda:point(left,zval(),BLUE))
        w_dot=always_redraw(lambda:point(right,square(zval()),GREEN))
        radial_left=always_redraw(lambda:Line(left.c2p(0,0),z_dot.get_center(),color=BLUE,stroke_width=2))
        radial_right=always_redraw(lambda:Line(right.c2p(0,0),w_dot.get_center(),color=GREEN,stroke_width=2))
        z_label=self.math('1+i',30,BLUE).next_to(left.c2p(1,1),UR,buff=.13)
        w_label=self.math('2i',30,GREEN).next_to(right.c2p(0,2),RIGHT,buff=.15)
        self.play(FadeIn(z_dot),FadeIn(w_dot),Create(radial_left),Create(radial_right),run_time=.25)
        self.cue('entrada_ejemplo')
        self.play(Write(z_label),run_time=.3)
        self.cue('resultado_ejemplo')
        self.add(w_label)
        self.footer(self.math(r'(1+i)^2=2i',44,GREEN))
        self.cue('modulo')
        circ_left=Circle(radius=radius*4.3/4,color=BLUE,stroke_width=1.5).move_to(left.c2p(0,0))
        circ_right=Circle(radius=2*4.3/6,color=GREEN,stroke_width=1.5).move_to(right.c2p(0,0))
        self.play(Create(circ_left),Create(circ_right),run_time=.9)
        self.footer(self.math(r'|w|=|z|^2\qquad (\sqrt{2})^2=2',40))
        self.cue('argumento')
        angle_left=Arc(radius=.4,start_angle=0,angle=PI/4,color=ORANGE).move_arc_center_to(left.c2p(0,0))
        angle_right=Arc(radius=.4,start_angle=0,angle=PI/2,color=ORANGE).move_arc_center_to(right.c2p(0,0))
        angle_labels=VGroup(self.math(r'45^\circ',26,ORANGE).move_to(left.c2p(0,0)+RIGHT*.8+UP*.22),
                            self.math(r'90^\circ',26,ORANGE).move_to(right.c2p(0,0)+RIGHT*.65+UP*.5))
        self.play(Create(angle_left),Create(angle_right),Write(angle_labels),run_time=.65)
        self.footer(self.math(r'z=re^{i\theta}\ \Longrightarrow\ w=r^2e^{2i\theta}\qquad r>0',36))
        self.cue('giro')
        self.play(FadeOut(z_label),FadeOut(w_label),FadeOut(angle_left),FadeOut(angle_right),FadeOut(angle_labels),run_time=.2)
        self.footer(self.math(r'\Delta\theta=\pi\qquad\Delta\arg w=2\pi',37))
        available=self.cues['opuestos']['inicio']-self.time-.15
        self.play(theta.animate.set_value(5*PI/4),run_time=available,rate_func=linear)
        self.cue('opuestos')
        neg_dot=always_redraw(lambda:point(left,-zval(),VIOLET))
        z_tag=self.math('z',30,BLUE).next_to(z_dot,DL,buff=.1)
        neg_tag=self.math('-z',30,VIOLET).next_to(left.c2p(1,1),UR,buff=.1)
        self.play(FadeIn(neg_dot),Write(z_tag),Write(neg_tag),run_time=.6)
        self.footer(self.math(r'(-z)^2=z^2',44))
        self.cue('preimagenes')
        self.play(Indicate(z_dot,scale_factor=1.1),Indicate(neg_dot,scale_factor=1.1),run_time=.65)
        self.play(Indicate(w_dot,scale_factor=1.1),run_time=.65)
        self.cue('condicion_preimagenes')
        self.footer(self.math(r'w\ne0:\quad z\ \text{y}\ -z',40))
        self.cue('local')
        orbit=VGroup(z_dot,w_dot,neg_dot,radial_left,radial_right,circ_left,circ_right,z_tag,neg_tag)
        self.play(FadeOut(orbit),run_time=.3)
        for m in (z_dot,w_dot,neg_dot,radial_left,radial_right):m.clear_updaters()
        self.footer(self.math(r'z\ne0:\quad\text{ángulos entre curvas}',37,GREEN))
        local=self.local_pair(left,right)
        self.play(Create(local[0]),run_time=.8)
        self.cue('angulos_locales')
        self.play(Create(local[1]),run_time=.65)
        self.cue('critico')
        self.play(FadeOut(local),run_time=.25)
        self.cue('derivada_cero')
        self.footer(self.math(r"f'(0)=0",44,ORANGE))
        rays=VGroup()
        for plane,angle in ((left,PI/4),(right,PI/2)):
            base=plane.c2p(0,0)
            for a in (0,angle):
                rays.add(Line(base,base+1.1*np.array([np.cos(a),np.sin(a),0]),color=ORANGE,stroke_width=3))
            rays.add(Arc(radius=.42,start_angle=0,angle=angle,color=ORANGE).move_arc_center_to(base))
        rays.add(self.math(r'45^\circ',28,ORANGE).move_to(left.c2p(0,0)+RIGHT*.85+UP*.28),
                 self.math(r'90^\circ',28,ORANGE).move_to(right.c2p(0,0)+RIGHT*.7+UP*.6))
        self.cue('falla_angular')
        self.play(Create(rays),run_time=.8)
        self.cue('cierre_local')
        self.play(FadeOut(rays),run_time=.25)
        local=self.local_pair(left,right)
        self.play(Create(local),run_time=.9)
        self.footer(self.math(r'\text{Conserva los ángulos si }z\ne0',37,GREEN))
        self.cue('cierre_global')
        self.play(FadeOut(local),run_time=.25)
        pair=VGroup(point(left,1+1j,BLUE),point(left,-1-1j,VIOLET),point(right,2j,GREEN),
                    self.math('1+i',30,BLUE).next_to(left.c2p(1,1),UR,buff=.12),
                    self.math('-1-i',30,VIOLET).next_to(left.c2p(-1,-1),DL,buff=.12),
                    self.math('2i',30,GREEN).next_to(right.c2p(0,2),RIGHT,buff=.12))
        self.play(FadeIn(pair),run_time=.6)
        self.footer(self.math(r'(1+i)^2=(-1-i)^2=2i',43))
        self.wait(max(0,timeline['duracion_total']-self.time))

    def local_pair(self,left,right):
        t=np.linspace(-.4,.4,65)
        z0=.8+.8j
        lines=VGroup(self.path(left,z0+t,BLUE,4),self.path(left,z0+1j*t,ORANGE,4),
                     self.path(right,(z0+t)**2,BLUE,4),self.path(right,(z0+1j*t)**2,ORANGE,4))
        angles=VGroup()
        for plane,z,start in ((left,z0,0),(right,z0*z0,PI/4)):
            base=plane.c2p(z.real,z.imag)
            lines.add(Dot(base,radius=.065,color=GREEN))
            angles.add(Arc(radius=.25,start_angle=start,angle=PI/2,color=GREEN).move_arc_center_to(base),
                       self.math(r'90^\circ',26,GREEN).move_to(base+RIGHT*.65+UP*.65))
        return VGroup(lines,angles)
