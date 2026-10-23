"""Controles geométricos independientes del render de z²."""
import json
import numpy as np
from manim import Axes
from escena import MAComplejoCuadrado


def main():
    t=np.linspace(-1.2,1.2,501)
    c=.8
    vertical=(c+1j*t)**2
    horizontal=(t+1j*c)**2
    assert np.max(abs(vertical.real-(c*c-vertical.imag**2/(4*c*c))))<1e-12
    assert np.max(abs(horizontal.real-(horizontal.imag**2/(4*c*c)-c*c)))<1e-12
    z0=.8+.8j
    eps=1e-5
    dx=((z0+eps)**2-(z0-eps)**2)/(2*eps)
    dy=((z0+1j*eps)**2-(z0-1j*eps)**2)/(2*eps)
    angle=np.angle(dy/dx)
    assert abs(angle-np.pi/2)<1e-9
    theta=np.linspace(np.pi/4,5*np.pi/4,501)
    image=(np.sqrt(2)*np.exp(1j*theta))**2
    winding=np.unwrap(np.angle(image))[-1]-np.unwrap(np.angle(image))[0]
    assert abs(winding-2*np.pi)<1e-12
    assert abs((1+1j)**2-2j)<1e-12 and abs((-1-1j)**2-2j)<1e-12
    assert abs(np.angle(np.exp(1j*np.pi/4)**2)-np.pi/2)<1e-12
    corners=np.array([x+1j*y for x in (-1.2,1.2) for y in (-1.2,1.2)])**2
    assert np.max(abs(corners.imag))<3
    scene=MAComplejoCuadrado()
    plane=Axes(x_range=[-3,3,1],y_range=[-3,3,1],x_length=4.3,y_length=4.3)
    assert abs(np.linalg.norm(plane.c2p(1,0)-plane.c2p(0,0))-np.linalg.norm(plane.c2p(0,1)-plane.c2p(0,0)))<1e-12
    grid=scene.lattice(plane,True)
    grid.set_stroke(opacity=.3)
    assert all(float(p.get_fill_opacity())==0 for p in grid)
    # Al interpolar la cuadrícula no se afirma que cada estado sea conforme.
    result={'parabolas':'OK','ejemplo_1_mas_i':'OK','dos_preimagenes':'OK',
            'angulo_local_grados':float(np.degrees(angle)),
            'giro_imagen_radianes':float(winding),'origen_45_a_90':'OK',
            'escala_isotropica':'OK','curvas_sin_relleno':'OK','limites_imagen':'OK'}
    from pathlib import Path
    Path('generados/validacion_matematica.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
