"""Referencia visual autónoma — NO es un render Manim ni contiene voz Kokoro.
Requiere Pillow, NumPy y FFmpeg. Uso: python render_vista_referencia.py
"""
from __future__ import annotations
from pathlib import Path
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'vista_42s_silenciosa.mp4'
W,H,FPS,DURATION=1280,720,24,42
BG='#0F1117';WHITE='#F5F7FA';MUTED='#A7B0BE';BLUE='#4EA1FF';ORANGE='#FFB454';GREEN='#63D471'
def pick_font(candidates):
    return next((p for p in candidates if Path(p).is_file()), None)
FONT=pick_font(['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', r'C:\Windows\Fonts\arial.ttf'])
BOLD=pick_font(['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', r'C:\Windows\Fonts\arialbd.ttf'])
if FONT is None or BOLD is None:
    raise RuntimeError('Faltan fuentes Sans compatibles para el renderizador auxiliar.')
FONTS={}
for key,sz in [('title',38),('brand',17),('section',15),('m',21),('body',24),('math',36),('small',19),('ticks',17),('bigmath',44)]:
    FONTS[key]=ImageFont.truetype(BOLD if key in ('title','section','math','bigmath') else FONT,sz)

def sat(t):return min(max(t,0.0),1.0)
def ease(t):
    p=sat(t);return p*p*(3-2*p)
def lerp(a,b,t):return a+(b-a)*t
def mixhex(a,b,t):
    u=ease(t);aa=tuple(int(a[i:i+2],16) for i in (1,3,5));bb=tuple(int(b[i:i+2],16) for i in (1,3,5))
    return tuple(round(lerp(v,w,u)) for v,w in zip(aa,bb))
def rgba_draw(draw,points,fill,opacity,width):
    if opacity<=0:return
    bg=mixhex(BG,fill,sat(opacity))
    draw.line(points,fill=bg,width=width,joint='curve')
def circle(draw,x,y,r,color,a=1.0):
    if a<=0:return
    draw.ellipse((x-r,y-r,x+r,y+r),fill=mixhex(BG,color,a),outline=None)
def pos(x,y):return 142+244*x,584-64*y

def fade_txt(draw,xy,text,font,fill,alpha=1,anchor=None):
    if alpha>0:draw.text(xy,text,font=font,fill=mixhex(BG,fill,alpha),anchor=anchor)

SEGMENTS=[
('01','PARÁBOLA','Una función, una curva y todos sus puntos.'),
('02','SECANTE','Dos puntos de la parábola determinan una secante.'),
('03','APROXIMACIÓN','Al acercar los puntos, la pendiente se acerca a dos.'),
('04','TANGENTE','La posición límite de las secantes es la tangente.')]

# Base background, static grid and title
base=Image.new('RGB',(W,H),BG)
d=ImageDraw.Draw(base)
d.rounded_rectangle((872,142,1205,584),radius=18,fill='#161d29',outline='#273141',width=2)
d.line((74,131,1205,131),fill='#354153',width=2)
d.line((142,584,822,584),fill='#9AA6B4',width=2)
d.line((142,584,142,152),fill='#9AA6B4',width=2)
for x in (1,2):
    px,_=pos(x,0)
    d.line((px,153,px,584),fill='#253244',width=1)
    fade_txt(d,(px,601),str(x),FONTS['ticks'],MUTED,0.9,anchor='mt')
for y in (1,2,4,6):
    _,py=pos(0,y)
    d.line((142,py,822,py),fill='#253244',width=1)
    fade_txt(d,(114,py),str(y),FONTS['ticks'],MUTED,0.75,anchor='rm')
fade_txt(d,(835,582),'x',FONTS['m'],MUTED)
fade_txt(d,(116,151),'y',FONTS['m'],MUTED)
fade_txt(d,(79,73),'CÁLCULO  /  MA-VIZ-001',FONTS['section'],MUTED)
fade_txt(d,(79,94),'DE LA SECANTE A LA TANGENTE',FONTS['title'],WHITE)
fade_txt(d,(1206,76),'MATEMÁTICA ABIERTA',FONTS['brand'],MUTED,anchor='ra')

# Stable plot coordinates
curve=[pos(v/180*2.58,(v/180*2.58)**2) for v in range(181)]
a_pt=pos(1,1)


def render(t):
    img=base.copy();draw=ImageDraw.Draw(img)
    # Subtle header progress indicator
    draw.line((79,133,79+1126*(t/DURATION),133),fill=BLUE,width=3)
    # Parabola stroke appears progressively
    k=round(ease((t-1.75)/3.7)*(len(curve)-1))
    if k>0:
        draw.line(curve[:k+1],fill=BLUE,width=5,joint='curve')
    fade_txt(draw,(913,167),'f(x) = x²',FONTS['math'],BLUE,ease((t-4.0)/1.0))
    # Segment labels are chosen only when the content has begun
    idx=0 if t<8 else 1 if t<18 else 2 if t<30 else 3
    n,caption,subtitle=SEGMENTS[idx]
    fade_txt(draw,(911,260),f'{n}  {caption}',FONTS['section'],MUTED,ease(min(t%12,1.0)*3))
    draw.line((909,291,1173,291),fill='#334252',width=1)
    # Anchor point
    if t>=8:
        a=ease((t-8)/0.8)
        circle(draw,*a_pt,7,GREEN,a)
        fade_txt(draw,(a_pt[0]-13,a_pt[1]+21),'A',FONTS['m'],GREEN,a,anchor='mm')
    # B point, secant and h
    if 8.85<=t<33:
        sec_entrance=ease((t-8.85)/1.6)
        sec_fade=1-ease((t-30.0)/2.5)
        a=sec_entrance*sec_fade
        if t<18:h=1.12
        elif t<29.8:
            # Gradual yet accelerating reduction; approaches a small positive h
            h=lerp(1.12,0.04,ease((t-18)/11.8))
        else:h=0.04
        b_pt=pos(1+h,(1+h)**2)
        slope=2+h
        xlo,xhi=max(.63,(1+h)/(2+h)+.01),2.60
        p1=pos(xlo,1+slope*(xlo-1));p2=pos(xhi,1+slope*(xhi-1))
        rgba_draw(draw,[p1,p2],ORANGE,a,5)
        circle(draw,*b_pt,7,ORANGE,a)
        fade_txt(draw,(b_pt[0]+14,b_pt[1]-13),'B',FONTS['small'],ORANGE,a)
        if t>=12:
            # horizontal distance at y=0.50
            x1,yhelper=pos(1,.5); x2,_=pos(1+h,.5)
            if x2-x1>9:
                draw.line((x1,yhelper,x2,yhelper),fill=mixhex(BG,ORANGE,a*0.6),width=2)
                for xx in (x1,x2):draw.line((xx,yhelper-4,xx,yhelper+4),fill=mixhex(BG,ORANGE,a*.6),width=2)
            if h>.20:
                fade_txt(draw,((x1+x2)/2,yhelper-23),'h',FONTS['small'],ORANGE,a,anchor='mm')
        fade_txt(draw,(911,339),'Recta secante',FONTS['body'],ORANGE,a)
        if t>=18:
            f=ease((t-18)/.7)*a
            fade_txt(draw,(911,391),'m(h) = 2 + h',FONTS['math'],ORANGE,f)
            fade_txt(draw,(911,456),f'h = {h:.2f}',FONTS['body'],WHITE,f)
            fade_txt(draw,(911,498),f'm = {2+h:.2f}',FONTS['body'],ORANGE,f)
    if t>=30:
        f=ease((t-30.6)/1.4)
        xlo,xhi=.58,2.72
        tang1=pos(xlo,2*xlo-1);tang2=pos(xhi,2*xhi-1)
        # Tangent is only shown when slope limit established
        rgba_draw(draw,[tang1,tang2],GREEN,f,5)
        fade_txt(draw,(911,339),'Recta tangente',FONTS['body'],GREEN,f)
        fade_txt(draw,(911,393),'m = 2',FONTS['math'],GREEN,ease((t-32.4)/1.3))
        fade_txt(draw,(910,483),"f′(1) = 2",FONTS['bigmath'],GREEN,ease((t-35.6)/1.2))
    # Bottom information changes at the start of each scene
    draw.line((79,633,1204,633),fill='#354153',width=1)
    fade_txt(draw,(79,656),subtitle,FONTS['small'],WHITE,1.0)
    fade_txt(draw,(1205,690),'VISTA CONCEPTUAL SILENCIOSA · NO MANIM',FONTS['section'],MUTED,0.9,anchor='ra')
    return img


def main():
    cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo',
         '-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
         '-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p',
         '-movflags','+faststart','-an',str(OUT)]
    p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for idx in range(DURATION*FPS):
            img=render(idx/FPS)
            p.stdin.write(img.tobytes())
            if idx and idx%240==0: print(f'[VISTA] {idx/FPS:.1f}s / {DURATION}s',flush=True)
    except BrokenPipeError as e:
        raise RuntimeError('FFmpeg interrumpió el video de referencia.') from e
    finally:
        p.stdin.close()
    if p.wait()!=0:raise RuntimeError('Falló FFmpeg al producir la vista de referencia')
    print('[OK]',OUT,OUT.stat().st_size,flush=True)

if __name__=='__main__': main()
