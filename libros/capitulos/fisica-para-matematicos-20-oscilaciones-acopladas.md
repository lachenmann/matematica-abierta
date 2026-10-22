---
title: "Oscilaciones acopladas"
subtitle: "Física para matemáticos · Tomo I · Capítulo 20"
author: "A. Peña"
description: "Capítulo 20 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0364
source-id: FISPM-r20261021-C20
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0361"]
related: [MA-BOK-0005]
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
include-in-header:
  - ../../assets/includes/ma-math-font-ready.html
  - ../../assets/books/fispm/fispm-lightbox-focus.html
format:
  html:
    css: ../../assets/books/fispm/fispm-reader.css
    lightbox: true
number-sections: false
---

[← 19. Cuerpo rígido en tres dimensiones](fisica-para-matematicos-19-cuerpo-rigido-en-tres-dimensiones.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [21. Trabajo virtual, coordenadas generalizadas y acción →](fisica-para-matematicos-21-trabajo-virtual-coordenadas-generalizadas-y-accion.md)

Desplazamos un carro sobre un riel y lo soltamos. Un segundo carro, inicialmente en reposo, comienza a moverse porque un resorte une ambos cuerpos. Durante un tiempo, la oscilación del primero pierde amplitud mientras crece la del segundo. Después el intercambio se invierte. Para predecirlo necesitamos conservar dos posiciones y dos velocidades iniciales: la fuerza sobre cada carro depende también de dónde está el otro.

El oscilador del capítulo 10 ofrecía una frecuencia y una preparación inicial. Aquí un mismo aparato admite varios movimientos especialmente sencillos. Podemos soltar los carros de manera que avancen juntos o que se aproximen y se separen simétricamente. Cada preparación conserva una proporción entre sus desplazamientos. Encontrar esas proporciones permitirá construir también el movimiento producido al soltar un solo carro.

Trabajaremos primero con resortes ideales, masas constantes y rozamiento despreciable, en un laboratorio inercial. Las fuerzas elásticas actuarán dentro de su intervalo lineal. Después examinaremos cómo esa descripción aparece al aproximar un potencial cerca del equilibrio. Las frecuencias calculadas pertenecerán al modelo elegido; medirlas permitirá contrastar sus masas, sus rigideces y sus condiciones de apoyo.

## Dos posiciones para un solo aparato

Dos carros de igual masa $m>0$ se mueven horizontalmente. Cada uno está unido a una pared fija mediante un resorte de rigidez $k>0$ y ambos están conectados mediante otro de rigidez $\kappa>0$. Llamaremos $x_1,x_2$ a sus desplazamientos respecto de un equilibrio en que los tres resortes tienen su longitud natural. Ambos ejes apuntan hacia la derecha. Al desplazar los carros, la extensión adicional del resorte central es $x_2-x_1$.

El resorte central tira del primer carro hacia la derecha si $x_2-x_1>0$, y ejerce sobre el segundo la fuerza opuesta. Newton da

$$
m\ddot x_1=-(k+\kappa)x_1+\kappa x_2,
\qquad
m\ddot x_2=\kappa x_1-(k+\kappa)x_2.
$$

El peso y la normal se compensan en vertical. Cada ecuación horizontal conserva las dos interacciones elásticas del carro correspondiente. Si sujetáramos el segundo carro, el primero oscilaría con rigidez $k+\kappa$. Al liberarlo cambia la situación física: su desplazamiento modifica continuamente la extensión central.

![Dos carros y tres resortes con desplazamientos orientados hacia la derecha.](/assets/books/fispm/r20261021/acoplados_aparato.svg){.fpm-v04-figure}
*Figura 20.1.* La extensión del resorte central depende de la diferencia de desplazamientos. Las paredes fijan el laboratorio y proporcionan las fuerzas externas sobre el conjunto.

Sumemos las ecuaciones y después restémoslas. Las combinaciones

$$
Q_+=\frac{x_1+x_2}{2},\qquad Q_-=\frac{x_1-x_2}{2}
$$

satisfacen

$$
\ddot Q_++\omega_+^2Q_+=0,
\qquad
\ddot Q_-+\omega_-^2Q_-=0,
\qquad
\omega_+^2=\frac{k}{m},\quad
\omega_-^2=\frac{k+2\kappa}{m}.
$$

Los signos de los subíndices indican suma y diferencia; en este aparato $\omega_- >\omega_+$. La suma elimina la fuerza interna del resorte central. La diferencia conserva su contribución dos veces, porque los extremos se desplazan en sentidos opuestos.

**Definición.** Un modo normal oscilatorio de un sistema lineal es un movimiento de perfil fijo $x(t)=\phi a(t)$, con un vector real constante $\phi\ne0$ y una función $a$ de amplitud positiva que satisface $\ddot a+\omega^2a=0$, para una frecuencia angular $\omega>0$. Las componentes del perfil determinan las proporciones y los signos relativos de los desplazamientos.

Para $\phi_+=(1,1)^{\mathsf T}$ ambos carros se desplazan igual y el resorte central conserva su extensión. Para $\phi_-=(1,-1)^{\mathsf T}$ se desplazan en sentidos opuestos y el resorte central añade restauración. Una componente nula del perfil mantiene ese carro en equilibrio durante el modo. Multiplicar el perfil por una constante y dividir la amplitud por la misma constante describe idéntico movimiento.

![Perfiles de movimiento conjunto y de movimiento opuesto.](/assets/books/fispm/r20261021/acoplados_modos.svg){.fpm-v04-figure}
*Figura 20.2.* Las flechas representan desplazamientos simultáneos. El perfil conserva sus proporciones durante cada oscilación; su escala depende de la preparación.

## Preparar los modos y recuperar los datos

La transformación tiene inversa: $x_1=Q_++Q_-$ y $x_2=Q_+-Q_-$. Podemos resolver las dos ecuaciones escalares mediante las funciones del capítulo 10 y reconstruir ambos carros.

**Proposición.** Para cualquier posición inicial $x(0)$ y velocidad inicial $v(0)$ del aparato simétrico, la solución única es

$$
Q_\pm(t)=Q_\pm(0)\cos\omega_\pm t+
\frac{\dot Q_\pm(0)}{\omega_\pm}\sin\omega_\pm t,
\qquad x_1=Q_++Q_-,\quad x_2=Q_+-Q_-.
$$

**Demostración.** La suma y la diferencia transforman las ecuaciones de Newton en las dos ecuaciones escalares obtenidas. Cada expresión satisface su ecuación y recupera su posición y derivada iniciales. La inversa reconstruye los cuatro datos originales. La unicidad del oscilador escalar aplicada a cada combinación garantiza la unicidad de la pareja reconstruida. $\square$

Soltemos sólo el primer carro desde $x_1(0)=A$, con $x_2(0)=0$ y velocidades nulas. Las coordenadas iniciales son $Q_+(0)=Q_-(0)=A/2$, y resulta

$$
x_1(t)=\frac A2(\cos\omega_+t+\cos\omega_-t),\qquad
x_2(t)=\frac A2(\cos\omega_+t-\cos\omega_-t).
$$

Definiendo $\bar\omega=(\omega_-+\omega_+)/2$ y $\delta=\omega_--\omega_+>0$, las identidades trigonométricas dan

$$
x_1=A\cos(\delta t/2)\cos\bar\omega t,
\qquad x_2=A\sin(\delta t/2)\sin\bar\omega t.
$$

Si $\kappa/k$ es pequeño, la frecuencia $\bar\omega$ marca la oscilación rápida y $\delta/2$ describe una modulación lenta. Los módulos de las envolventes vuelven a su situación inicial después de $2\pi/\delta$. La primera anulación de la envolvente del carro 1 ocurre en $t=\pi/\delta$. Su velocidad en ese instante es $-A\delta\cos(\bar\omega\pi/\delta)/2$ y puede conservar un valor distinto de cero. El registro de posición y el de velocidad deben leerse conjuntamente para decidir qué estado alcanzó el carro.

![Dos registros temporales con sus envolventes en acoplamiento débil.](/assets/books/fispm/r20261021/acoplados_batimientos.svg){.fpm-v04-figure}
*Figura 20.3.* Con $m=1\,\mathrm{kg}$, $k=4\,\mathrm{N/m}$ y $\kappa=0{,}245\,\mathrm{N/m}$, las frecuencias son $2$ y $\sqrt{4{,}49}$ radianes por segundo. Las líneas discontinuas muestran los límites de amplitud de las expresiones exactas del modelo lineal.

La energía de los carros y los tres resortes es

$$
E=\frac m2(\dot x_1^2+\dot x_2^2)
+\frac k2(x_1^2+x_2^2)+\frac\kappa2(x_2-x_1)^2
=m(\dot Q_+^2+\omega_+^2Q_+^2)
+m(\dot Q_-^2+\omega_-^2Q_-^2).
$$

Las dos energías modales se conservan por separado. El intercambio entre carros puede coexistir con esas constantes porque cada carro participa en ambos modos. El resorte central conserva además una energía propia. Para atribuir energías a subsistemas hay que declarar cómo se contabiliza esa contribución. En acoplamiento débil resulta útil hablar de intercambio lento entre osciladores, comprobando la aproximación con el balance completo.

## La masa decide cómo proyectar

Al cambiar una masa desaparece la igualdad de aceleraciones asociada a fuerzas iguales. Conservemos las dos posiciones cartesianas, permitamos masas $m_1,m_2>0$ y rigideces de pared $k_1,k_2$. Las ecuaciones toman la forma

$$
M\ddot x+Kx=0,\qquad
M=\begin{pmatrix}m_1&0\\0&m_2\end{pmatrix},\quad
K=\begin{pmatrix}k_1+\kappa&-\kappa\\-\kappa&k_2+\kappa\end{pmatrix}.
$$

La energía es $E=\dot x^{\mathsf T}M\dot x/2+x^{\mathsf T}Kx/2$. La simetría de $K$ procede aquí de las fuerzas derivadas del potencial elástico. Buscando un perfil fijo obtenemos $K\phi=\omega^2M\phi$. Para encontrarlo calculamos primero los valores $\lambda=\omega^2$ que satisfacen $\det(K-\lambda M)=0$ y después resolvemos la ecuación vectorial correspondiente. El determinante permite hallar candidatos; la ecuación vectorial decide sus perfiles.

**Definición.** Para una matriz real simétrica definida positiva $M$, el producto escalar de masas es $\langle u,v\rangle_M=u^{\mathsf T}Mv$. Una base de perfiles $\phi_1,\ldots,\phi_n$ es ortonormal respecto de las masas cuando $\phi_i^{\mathsf T}M\phi_j=\delta_{ij}$, con una elección coherente de unidades para sus componentes y sus coeficientes.

La forma $\dot x^{\mathsf T}M\dot x$ mide dos veces la energía cinética. Esta es la razón física para usarla al separar movimientos. Una matriz de masas constante también puede tener términos cruzados cuando las coordenadas combinan posiciones de varias partículas. En coordenadas de longitudes, $M$ lleva unidades de masa y los perfiles normalizados pueden llevar unidades de masa elevada a $-1/2$; sus coordenadas modales llevan entonces unidades de longitud por raíz de masa. Si intervienen ángulos, se fijan escalas de coordenadas antes de efectuar operaciones matriciales numéricas. Los productos energéticos conservan sus unidades en cualquier representación coherente.

**Proposición.** Sean $M$ real simétrica definida positiva y $K$ real simétrica, constantes, en un sistema de $n$ coordenadas. Existe una base real de perfiles que satisface

$$
K\phi_j=\lambda_jM\phi_j,\qquad
\phi_i^{\mathsf T}M\phi_j=\delta_{ij}.
$$

Si $K$ es definida positiva, todos los $\lambda_j$ son positivos. Perfiles correspondientes a valores distintos son ortogonales respecto de $M$.

**Demostración.** El resultado espectral para matrices simétricas se obtiene como en el capítulo 19: minimizar la forma cuadrática sobre la esfera produce un autovector unitario; su complemento perpendicular es invariante, y la repetición en ese complemento construye una base ortonormal. Aplicado a $M$, proporciona $M=ODO^{\mathsf T}$ con $O$ ortogonal y $D$ diagonal de entradas positivas. Por tanto existen las matrices simétricas $M^{1/2}=OD^{1/2}O^{\mathsf T}$ y $M^{-1/2}=OD^{-1/2}O^{\mathsf T}$.

La matriz $A=M^{-1/2}KM^{-1/2}$ es simétrica. El mismo resultado espectral da una base ortonormal $u_j$ con $Au_j=\lambda_ju_j$. Tomando $\phi_j=M^{-1/2}u_j$, obtenemos $K\phi_j=\lambda_jM\phi_j$ y $\phi_i^{\mathsf T}M\phi_j=u_i^{\mathsf T}u_j=\delta_{ij}$. Si $K$ es definida positiva, $\lambda_j=\phi_j^{\mathsf T}K\phi_j>0$. Finalmente, la simetría implica

$$
\lambda_j\phi_i^{\mathsf T}M\phi_j
=\phi_i^{\mathsf T}K\phi_j
=\lambda_i\phi_i^{\mathsf T}M\phi_j.
$$

Para $\lambda_i\ne\lambda_j$, esta identidad obliga a que el producto de masas sea cero. Dentro de un espacio de valor repetido se escoge una base ortonormal para ese producto. $\square$

Para ver qué cambia en la práctica, tomemos valores numéricos SI

$$
M=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
K=\begin{pmatrix}4&-2\\-2&6\end{pmatrix}.
$$

El polinomio es $2(\lambda-2)(\lambda-5)$. Podemos elegir los perfiles sin normalizar $(1,1)^{\mathsf T}$ y $(-2,1)^{\mathsf T}$. Su producto euclídeo es $-1$, mientras que su producto de masas es $-2+2=0$. Los perfiles normalizados son $\phi_1=(1,1)^{\mathsf T}/\sqrt3$ y $\phi_2=(-2,1)^{\mathsf T}/\sqrt6$, con las unidades implícitas de esa normalización. Dividir cada ecuación por su masa produce una matriz $M^{-1}K$ cuyas entradas cruzadas son $-2$ y $-1$. La simetría relevante se conserva en la pareja $(K,M)$.

![Comparación de dos perfiles de masas diferentes y su ortogonalidad ponderada.](/assets/books/fispm/r20261021/acoplados_masas.svg){.fpm-v04-figure}
*Figura 20.4.* Para masas de uno y dos kilogramos, el perfil rápido desplaza el primer carro con el doble de amplitud y signo opuesto. Las masas intervienen tanto en la frecuencia como en la proyección de una preparación.

## Separar las ecuaciones y la energía

Reunamos los perfiles normalizados en las columnas de $S$. Las identidades anteriores son $S^{\mathsf T}MS=I$ y $S^{\mathsf T}KS=\Lambda$, donde $\Lambda$ tiene entradas diagonales $\lambda_j$. Escribir $x=S\eta$ permite usar cada columna como una dirección de movimiento.

**Definición.** Las coordenadas normales asociadas a esa base son los coeficientes $\eta=S^{\mathsf T}Mx$ de la expansión $x=S\eta$. Sus velocidades son $\dot\eta=S^{\mathsf T}M\dot x$.

**Proposición.** La transformación anterior convierte $M\ddot x+Kx=0$ en las ecuaciones independientes $\ddot\eta_j+\lambda_j\eta_j=0$ y descompone la energía como

$$
E=\frac12\sum_j(\dot\eta_j^2+\lambda_j\eta_j^2).
$$

Para $\lambda_j=\omega_j^2>0$, cada coordenada queda determinada por sus datos mediante $\eta_j(t)=\eta_j(0)\cos\omega_jt+\dot\eta_j(0)\sin\omega_jt/\omega_j$.

**Demostración.** Como $S$ es una base, es invertible. La igualdad $S^{\mathsf T}MS=I$ muestra que su inversa es $S^{\mathsf T}M$. Sustituimos $x=S\eta$ en las ecuaciones y multiplicamos por $S^{\mathsf T}$. Las identidades de las matrices producen $\ddot\eta+\Lambda\eta=0$. La misma sustitución en las dos formas cuadráticas de la energía da la suma anunciada. Cada término tiene derivada $\dot\eta_j(\ddot\eta_j+\lambda_j\eta_j)=0$. La solución escalar recupera directamente sus dos datos iniciales. $\square$

En el ejemplo de masas diferentes, una preparación $x(0)=(A,0)^{\mathsf T}$ en reposo tiene coeficientes $\eta_1(0)=A/\sqrt3$ y $\eta_2(0)=-2A/\sqrt6$ en las unidades escogidas. De ahí,

$$
x_1=\frac A3\cos(\sqrt2\,t)+\frac{2A}3\cos(\sqrt5\,t),
\qquad
x_2=\frac A3[\cos(\sqrt2\,t)-\cos(\sqrt5\,t)].
$$

En estas fórmulas numéricas $t$ se expresa en segundos y las frecuencias en radianes por segundo. En $t=0$ se recupera la preparación; las derivadas iniciales son cero. La segunda masa recibe una superposición cuya amplitud está determinada por los dos perfiles. La proyección ponderada conserva esa información aun cuando los vectores de desplazamiento se dibujen sobre los mismos ejes cartesianos.

## Frecuencias nulas, crecimiento y periodicidad

Retiremos los resortes de pared y conservemos el resorte central. Trasladar ambos carros por igual deja intacta su extensión. La matriz $K$ tiene entonces un núcleo que contiene $(1,1)^{\mathsf T}$ y el valor correspondiente es $\lambda=0$. La coordenada modal satisface $\ddot\eta=0$: permite una posición constante y una traslación uniforme. Sus dos datos iniciales siguen siendo necesarios.

**Proposición.** Para las matrices simétricas $K$ y definida positiva $M$ anteriores, cada dirección modal evoluciona según el signo de su valor $\lambda$. Si $\lambda=0$, $\eta=a+bt$. Si $\lambda=-\sigma^2<0$, $\eta=a\cosh\sigma t+(b/\sigma)\sinh\sigma t$, con $a=\eta(0)$ y $b=\dot\eta(0)$. Un valor negativo permite perturbaciones arbitrariamente pequeñas que crecen exponencialmente en el sistema lineal.

**Demostración.** Integramos dos veces cuando $\lambda=0$. Para $\lambda=-\sigma^2$, derivar las funciones hiperbólicas verifica la ecuación $\ddot\eta-\sigma^2\eta=0$ y sus datos. La preparación $b=\sigma a$ produce $\eta=ae^{\sigma t}$. Para cualquier $a\ne0$, su módulo supera una tolerancia fija a tiempo suficientemente grande, aunque el módulo inicial se escoja tan pequeño como se quiera. $\square$

En un equilibrio de un sistema elástico, una dirección de curvatura negativa del potencial produce precisamente esa salida lineal. Una curvatura nula exige examinar también los términos superiores del potencial: puede describir una traslación libre, pero también una fuerza restauradora que comienza en orden cúbico. El problema 14 compara esas posibilidades.

Dos frecuencias positivas tampoco aseguran que toda la trayectoria se repita. Cuando ambas participaciones son distintas de cero, un período común $T$ exige $\omega_1T$ y $\omega_2T$ múltiplos enteros de $2\pi$. Por tanto, exige una razón racional $\omega_1/\omega_2$. La descomposición modal permite sumar movimientos periódicos cuyas fases relativas siguen cambiando sin un período común exacto.

![Una dirección libre, una oscilatoria y una de crecimiento.](/assets/books/fispm/r20261021/acoplados_regimenes.svg){.fpm-v04-figure}
*Figura 20.5.* Los valores cero, positivo y negativo de $\lambda$ producen evoluciones distintas de la coordenada modal. Cada curva corresponde a una ecuación lineal y a los datos iniciales indicados.

## La aproximación cerca de un equilibrio

Consideremos posiciones cartesianas independientes $x$ y un potencial $U$ de clase $C^3$ cerca de un equilibrio $x=0$, con $\nabla U(0)=0$. La expansión local de su gradiente es

$$
\nabla U(x)=Kx+r(x),\qquad K=D^2U(0),\qquad
\|r(x)\|\le C\|x\|^2
$$

en una vecindad suficientemente pequeña y con una elección fija de escalas. La cota procede de aplicar Taylor a las componentes del gradiente y acotar las derivadas terceras en una vecindad cerrada contenida en el dominio. Con masas constantes, Newton queda $M\ddot x+Kx=-r(x)$. Suprimir el resto define la aproximación lineal. La simetría del Hessiano y la positividad de la energía cinética permiten el análisis modal construido.

La cota compara fuerzas a medida que disminuye el desplazamiento. En direcciones donde la restauración lineal se anula, el resto puede aportar la fuerza dominante. Incluso con frecuencias positivas, una diferencia pequeña de frecuencia puede acumular un desfase tras muchas oscilaciones. Para contrastar el modelo se registran amplitud, duración, condiciones iniciales y precisión temporal. Una predicción de corto alcance y otra de largo alcance requieren controles distintos.

El capítulo 21 extenderá la energía cinética a una matriz que depende de coordenadas y de la geometría del vínculo. Cerca de un equilibrio fijo reaparecerá una pareja de formas cuadráticas como $(K,M)$. El presente capítulo construye las proyecciones y la ortogonalidad que ese uso necesita.

![Potencial cuadrático y corrección cuártica para amplitudes crecientes.](/assets/books/fispm/r20261021/acoplados_aproximacion.svg){.fpm-v04-figure}
*Figura 20.6.* Para $U(q)=kq^2/2+\alpha q^4/4$ con $k,\alpha>0$, la razón entre la fuerza cúbica y la lineal es $\alpha q^2/k$ cuando $q\ne0$. Esa comparación permite declarar una escala de amplitud.

## Lo que una medición de modos permite inferir

En el aparato simétrico, si se conocen la masa y las dos frecuencias, se obtiene $k=m\omega_+^2$ y $\kappa=m(\omega_-^2-\omega_+^2)/2$. Las frecuencias estiman parámetros dentro de una familia de modelos. Los perfiles aportan una prueba adicional: con la preparación de movimiento conjunto debe conservarse $x_1=x_2$, y con la opuesta debe conservarse $x_1=-x_2$. Una desigualdad de masas o apoyos puede cambiar ambas proporciones.

Para estudiar el acoplamiento débil hay que registrar un intervalo suficientemente largo para ver la modulación. Las lecturas repetidas, la calibración de los sensores y la elección de la frecuencia de muestreo conservan el papel que tenían en el capítulo 0. Una serie muy precisa puede seguir siendo compatible con varias frecuencias si sus instantes de registro pierden información. Los problemas finales separan el ajuste de parámetros del contraste de un modelo y del diseño de observaciones nuevas.

![Frecuencias medidas y regiones admisibles de rigideces.](/assets/books/fispm/r20261021/acoplados_inferencia.svg){.fpm-v04-figure}
*Figura 20.7.* Con masa conocida, las cotas de ambas frecuencias delimitan rigideces admisibles. Las proyecciones sobre los ejes dan cotas individuales; conservar la pareja de frecuencias preserva también la relación entre los parámetros.

## Elegir qué combinación registrar

El primer carro se había soltado solo y su movimiento reunía dos modos. Si el sensor publica únicamente el promedio $y=(x_1+x_2)/2$, entrega $Q_+$ en cada instante. Podemos cambiar por completo $Q_-$ y conservar esa serie temporal. La duración del registro y la precisión de sus lecturas actúan sobre la combinación elegida; la elección de esa combinación determina qué movimientos llegan hasta el registro.

Para precisar la recuperación, supongamos conocidos los parámetros del aparato simétrico y las dos frecuencias positivas distintas. Un registro lineal tiene la forma $y=g_+Q_++g_-Q_-$, donde $g_+,g_-$ son coeficientes conocidos y constantes.

**Proposición (recuperar dos modos desde un registro).** Si $g_+g_-\ne0$, un registro exacto de $y$ en un intervalo abierto permite recuperar ambos modos mediante

$$
Q_+=\frac{\ddot y+\omega_-^2y}{g_+(\omega_-^2-\omega_+^2)},
\qquad
Q_-=\frac{\ddot y+\omega_+^2y}{g_-(\omega_+^2-\omega_-^2)}.
$$

Si uno de los coeficientes es cero, el registro conserva la contribución del otro modo y admite cualquier preparación del modo cuyo coeficiente se anula.

**Demostración.** Para aislar $Q_+$ aplicamos la operación $d^2/dt^2+\omega_-^2$ a $y$. La ecuación de $Q_-$ anula su contribución; la ecuación de $Q_+$ deja $g_+(\omega_-^2-\omega_+^2)Q_+$. Las hipótesis permiten dividir. Intercambiar los índices prueba la segunda fórmula. Cuando un coeficiente es cero, la propia expresión de $y$ es independiente del modo correspondiente; sus dos datos iniciales pueden variarse libremente. $\square$

Al medir sólo $x_1$ los dos coeficientes valen uno y el registro temporal exacto contiene ambos modos. Al medir el promedio, el coeficiente del modo opuesto vale cero. Esta diferencia se decide antes de muestrear. Las fórmulas de recuperación con derivadas describen información ideal: al aplicarlas a datos experimentales hay que estimar derivadas y controlar sus errores. Una separación pequeña entre frecuencias o un coeficiente pequeño amplifica esos errores a través de los denominadores. El problema 21 retoma la liberación inicial para comparar dos movimientos que un promedio vuelve indistinguibles.

## Ejercicios

En los problemas del aparato simétrico se usan los dos resortes de pared de rigidez $k$, el central de rigidez $\kappa$ y masas iguales $m$. Los desplazamientos se miden desde el equilibrio y en el mismo sentido. Salvo indicación contraria se omite el rozamiento, se permanece en el régimen lineal y se utilizan unidades SI.

### 1. La fuerza del resorte compartido {#ejercicio-20-1}

Para $m=1\,\mathrm{kg}$, $k=4\,\mathrm{N/m}$ y $\kappa=2\,\mathrm{N/m}$, se observa $x_1=0{,}03\,\mathrm m$, $x_2=0{,}01\,\mathrm m$. Obtenga las dos aceleraciones mediante fuerzas individuales. Un cálculo asigna $-\kappa x_1$ al resorte central del primer carro. Determine qué condición adicional describiría esa expresión.

### 2. Preparar una sola frecuencia {#ejercicio-20-2}

Con los parámetros del problema 1, encuentre las trayectorias si se sueltan en reposo desde $(x_1,x_2)=(A,A)$ y desde $(A,-A)$. Calcule las energías para $A=0{,}02\,\mathrm m$. Explique qué registro permitiría reconocer cada preparación.

### 3. Cuatro datos iniciales {#ejercicio-20-3}

Para el mismo aparato, $x(0)=(0{,}06,-0{,}02)\,\mathrm m$ y $\dot x(0)=(0{,}10,0{,}30)\,\mathrm{m/s}$. Obtenga $Q_\pm(t)$ y reconstruya las posiciones. Compruebe las velocidades iniciales.

### 4. Energías que pertenecen a los modos {#ejercicio-20-4}

Calcule la energía inicial del problema 3, primero en carros y resortes y después en coordenadas $Q_\pm$. Explique qué energías conservan individualmente un valor constante.

### 5. Leer una envolvente {#ejercicio-20-5}

Un aparato simétrico tiene frecuencias angulares $\omega_+=2\,\mathrm{s^{-1}}$ y $\omega_-=2{,}12\,\mathrm{s^{-1}}$. Se prepara $x(0)=(A,0)$, $\dot x(0)=0$. Obtenga el primer cero de la envolvente de $x_1$ y el tiempo de retorno de los módulos de las dos envolventes. Para $A=0{,}05\,\mathrm m$, calcule $x_1$ y $\dot x_1$ en aquel primer cero. Decida si el carro está en reposo.

### 6. Inferir los tres resortes {#ejercicio-20-6}

Se conoce $m=0{,}5\,\mathrm{kg}$ y se miden frecuencias $2$ y $3\,\mathrm{s^{-1}}$, con perfiles proporcionales a $(1,1)$ y $(1,-1)$. Infiera $k$ y $\kappa$. Prediga la frecuencia del primer carro si el segundo se sujeta en el equilibrio.

### 7. La ortogonalidad que usan las masas {#ejercicio-20-7}

Para $M=\operatorname{diag}(1,2)\,\mathrm{kg}$ y $K=\begin{pmatrix}4&-2\\-2&6\end{pmatrix}\,\mathrm{N/m}$, encuentre valores modales, perfiles y normalizaciones. Compare sus productos euclídeo y de masas. Identifique resortes positivos que realicen esta matriz $K$.

### 8. Soltar la masa ligera {#ejercicio-20-8}

En el problema 7 se prepara $x(0)=(A,0)$ y $\dot x(0)=0$. Obtenga las dos posiciones y las energías modales. Determine la razón entre estas últimas. Utilice los valores numéricos SI y mantenga la unidad de energía al expresar el resultado.

### 9. Coordenadas que mezclan posiciones {#ejercicio-20-9}

Para el aparato del problema 1, defina $y_1=x_1$, $y_2=x_2-x_1$. Obtenga las matrices de energía cinética y potencial en $y$, sus valores modales y los dos perfiles. Verifique la ortogonalidad mediante la nueva matriz de masas.

### 10. Una traslación que sigue libre {#ejercicio-20-10}

Dos masas de $2$ y $3\,\mathrm{kg}$ están unidas por un resorte de rigidez $6\,\mathrm{N/m}$ sobre un riel libre de fuerzas horizontales externas. Los desplazamientos desde un equilibrio cumplen $x(0)=(0{,}1,-0{,}1)\,\mathrm m$ y $\dot x(0)=(0{,}4,0{,}4)\,\mathrm{m/s}$. Use el centro de masa y la extensión adicional para resolver ambas posiciones. Identifique el modo nulo.

### 11. Tres masas y dos resortes {#ejercicio-20-11}

Tres masas de un kilogramo forman una cadena libre con dos resortes iguales de un newton por metro, sin resortes de pared. Construya $K$ y encuentre sus tres valores modales y perfiles. Explique el significado del perfil de frecuencia nula y del que mantiene quieta la masa central.

### 12. Dos modos con igual frecuencia {#ejercicio-20-12}

Un sistema tiene $M=mI$ y $K=4m\,\mathrm{s^{-2}}I$ en dos coordenadas de longitud. Estudie $x(t)=A(\cos(2t),\sin(2t))$, con $t$ numérico en segundos. Descompóngalo en modos de perfiles fijos. Describa la trayectoria y la libertad para escoger una base modal.

### 13. Una curvatura que permite salir {#ejercicio-20-13}

En unidades SI, $M=I$ y $K=\begin{pmatrix}1&-2\\-2&1\end{pmatrix}$. Halle las dos direcciones modales. Resuelva el movimiento desde $x(0)=\varepsilon(1,1)$ y velocidad nula. Relacione la curvatura del potencial con el crecimiento de esa preparación.

### 14. Cuando desaparece la restauración lineal {#ejercicio-20-14}

Dos coordenadas cartesianas de masa $m>0$ tienen potencial $U=\alpha(x_1^4+x_2^4)/4$, con $\alpha>0$. Calcule el Hessiano en cero y la aproximación lineal. Utilizando la energía exacta, demuestre que preparaciones suficientemente pequeñas en posición y velocidad permanecen pequeñas para todo tiempo futuro. Compare esa conclusión con lo que permite decidir el Hessiano.

### 15. Amortiguamiento proporcional a la masa {#ejercicio-20-15}

Añada al problema 7 una fuerza viscosa $-C\dot x$ con $C=\gamma M$, $\gamma=1\,\mathrm{s^{-1}}$. Obtenga las ecuaciones modales y sus exponentes temporales. Si se instala un único amortiguador sobre la primera masa, $C=\operatorname{diag}(c,0)$, calcule el término cruzado de $S^{\mathsf T}CS$ y explique cómo cambia la separación.

### 16. Forzar un carro y observar el otro {#ejercicio-20-16}

En el aparato del problema 1 actúa $(F\cos\Omega t,0)$, con $F=0{,}1\,\mathrm N$. Busque una solución particular periódica para $\Omega$ distinta de las frecuencias normales. Determine la frecuencia a la que la respuesta particular de $x_1$ se anula y calcule $x_2$ en ella. Declare qué preparación permite observar sólo esa respuesta en el modelo sin disipación.

### 17. Un reloj que confunde frecuencias {#ejercicio-20-17}

Un sensor registra $x(n\Delta t)=A\cos(\omega n\Delta t)$ para enteros $n\ge0$, con $\Delta t=0{,}1\,\mathrm s$. Construya otra frecuencia positiva que produzca exactamente todos esos registros. Explique qué información adicional o cambio de observación permitiría distinguirlas.

### 18. El paso temporal y el modo más rápido {#ejercicio-20-18}

En coordenadas normales de frecuencia $\omega>0$, se usa la actualización $v_{n+1}=v_n-h\omega^2\eta_n$, $\eta_{n+1}=\eta_n+hv_{n+1}$. Obtenga su matriz, traza y determinante. Halle el intervalo positivo de pasos para el cual todas sus iteradas permanecen acotadas para cualquier dato inicial. Aplíquelo al problema 7 y examine la frontera superior.

### 19. Una prueba con producto ordinario {#ejercicio-20-19}

Un argumento aplica el teorema espectral euclídeo directamente a $M^{-1}K$ del problema 7 y concluye que sus dos perfiles son perpendiculares en el dibujo cartesiano. Localice el paso que necesita revisión. Pruebe directamente la simetría de $M^{-1}K$ respecto del producto de masas y use esa identidad para obtener la ortogonalidad correcta.

### 20. Cotas y contraste de una identificación {#ejercicio-20-20}

En el aparato simétrico se conoce exactamente $m=0{,}5\,\mathrm{kg}$ dentro del modelo. Las frecuencias angulares pertenecen a $[1{,}99,2{,}01]$ y $[2{,}99,3{,}01]\,\mathrm{s^{-1}}$. Se admiten todas las combinaciones de esas bandas. Obtenga cotas para $k$ y $\kappa$. Diseñe un ensayo de perfiles que contraste la hipótesis de simetría con información distinta de las dos frecuencias empleadas en el ajuste.

### 21. Dos movimientos detrás de un mismo registro {#ejercicio-20-21}

En el aparato simétrico tome $m=1\,\mathrm{kg}$, $k=4\,\mathrm{N/m}$, $\kappa=2\,\mathrm{N/m}$ y $A=0{,}02\,\mathrm m$. Compare las preparaciones en reposo $x(0)=(A,0)$ y $x(0)=(A/2,A/2)$. Un sensor registra de manera continua e ideal $y=(x_1+x_2)/2$. Obtenga las trayectorias, compare sus registros y sus energías. Describa qué familia de preparaciones queda compatible con el mismo registro en el modelo lineal. Si se añade la lectura de $x_1$, reconstruya ambos carros. Examine también si un registro exacto de $x_1$ por sí solo bastaría con parámetros conocidos. Distinga esa recuperación ideal de la estimación de derivadas con ruido.

## Soluciones

### 1. La fuerza del resorte compartido {#solucion-20-1}

La extensión adicional central es $0{,}01-0{,}03=-0{,}02\,\mathrm m$. El resorte está comprimido respecto de su equilibrio y empuja el primer carro hacia la izquierda con $0{,}04\,\mathrm N$. Su resorte de pared añade $-0{,}12\,\mathrm N$. Por tanto $\ddot x_1=-0{,}16\,\mathrm{m/s^2}$.

El segundo recibe $+0{,}04\,\mathrm N$ del resorte central y $-0{,}04\,\mathrm N$ de su pared, de modo que su aceleración instantánea es cero. Puede tener velocidad distinta de cero en ese instante. La expresión $-\kappa x_1$ para la fuerza central del primer carro corresponde a mantener $x_2=0$. Esa condición describe un extremo central sujeto o un instante en que el segundo carro pasa por su equilibrio. En el registro dado $x_2$ tiene otro valor y debe conservarse en la extensión.

### 2. Preparar una sola frecuencia {#solucion-20-2}

La preparación conjunta tiene $Q_+(0)=A$, $Q_-(0)=0$ y ambas velocidades modales nulas. Resulta $x_1=x_2=A\cos(2t)$. La preparación opuesta da $Q_+=0$, $Q_-=A\cos(\sqrt8\,t)$ y, por tanto, $x_1=A\cos(\sqrt8\,t)$, $x_2=-A\cos(\sqrt8\,t)$. Las igualdades entre posiciones permanecen durante todo el movimiento.

Para $A=0{,}02\,\mathrm m$, las energías iniciales son $E_+=kA^2=0{,}0016\,\mathrm J$ y $E_-=(k+2\kappa)A^2=0{,}0032\,\mathrm J$. En el segundo caso el resorte central tiene extensión de módulo $2A$ y aporta $2\kappa A^2$. Dos sensores permiten comparar simultáneamente signos y proporciones; un sensor aislado reconoce una frecuencia, pero pierde la comprobación del perfil.

### 3. Cuatro datos iniciales {#solucion-20-3}

La transformación se aplica tanto a posiciones como a velocidades. Produce $Q_+(0)=0{,}02\,\mathrm m$, $Q_-(0)=0{,}04\,\mathrm m$, $\dot Q_+(0)=0{,}20\,\mathrm{m/s}$ y $\dot Q_-(0)=-0{,}10\,\mathrm{m/s}$. En valores numéricos SI,

$$
Q_+=0{,}02\cos(2t)+0{,}10\sin(2t),\qquad
Q_-=0{,}04\cos(\sqrt8\,t)-\frac{0{,}10}{\sqrt8}\sin(\sqrt8\,t).
$$

Sumar y restar estas expresiones da $x_1$ y $x_2$. En el origen las posiciones son $0{,}02+0{,}04=0{,}06$ y $0{,}02-0{,}04=-0{,}02$. Las derivadas son $0{,}20-0{,}10=0{,}10$ y $0{,}20+0{,}10=0{,}30$, como exigía la preparación. Dividir cada velocidad modal por su frecuencia fue necesario para que el coeficiente del seno tuviera unidades de longitud.

### 4. Energías que pertenecen a los modos {#solucion-20-4}

La energía cinética inicial es $(0{,}10^2+0{,}30^2)/2=0{,}05\,\mathrm J$. Los resortes de pared aportan $4(0{,}06^2+0{,}02^2)/2=0{,}008\,\mathrm J$ y el central aporta $2(-0{,}08)^2/2=0{,}0064\,\mathrm J$. El total es $0{,}0644\,\mathrm J$.

Las contribuciones modales son $E_+=1(0{,}20^2+4\cdot0{,}02^2)=0{,}0416\,\mathrm J$ y $E_-=1(0{,}10^2+8\cdot0{,}04^2)=0{,}0228\,\mathrm J$. Su suma recupera el mismo total. Cada una es constante porque su coordenada satisface una ecuación escalar independiente. La energía cinética de cada carro y la potencial de cada resorte cambian durante la evolución; esos intercambios componen las constantes modales.

### 5. Leer una envolvente {#solucion-20-5}

Aquí $\delta=0{,}12\,\mathrm{s^{-1}}$ y $\bar\omega=2{,}06\,\mathrm{s^{-1}}$. El primer cero de la envolvente de $x_1$ ocurre en $\tau=\pi/\delta=25\pi/3\,\mathrm s$, aproximadamente $26{,}18\,\mathrm s$. El retorno de los módulos ocurre a $2\pi/\delta=50\pi/3\,\mathrm s$, aproximadamente $52{,}36\,\mathrm s$.

En $\tau$, $x_1=0$, pero al derivar el producto queda $\dot x_1=-A\delta\cos(\bar\omega\tau)/2$. El ángulo rápido es $103\pi/6$, cuyo coseno vale $-\sqrt3/2$. Así, $\dot x_1=0{,}0015\sqrt3\,\mathrm{m/s}$, aproximadamente $0{,}00260\,\mathrm{m/s}$. El carro cruza el equilibrio con velocidad positiva. El cero de la envolvente determina un evento del registro de posición; la velocidad calculada completa su interpretación física.

### 6. Inferir los tres resortes {#solucion-20-6}

El perfil conjunto identifica $\omega_+=2$ y el opuesto identifica $\omega_-=3$. Por tanto, $k=m\omega_+^2=2\,\mathrm{N/m}$ y $\kappa=m(\omega_-^2-\omega_+^2)/2=1{,}25\,\mathrm{N/m}$. Ambos parámetros son positivos y corresponden al aparato supuesto.

Sujetar el segundo carro fija un extremo del resorte central: el primero recibe una fuerza $-(k+\kappa)x_1$. Su frecuencia es $\sqrt{(k+\kappa)/m}=\sqrt{6{,}5}\,\mathrm{s^{-1}}$, aproximadamente $2{,}55\,\mathrm{s^{-1}}$. Esa tercera medición utiliza una condición de apoyo nueva y contrasta la predicción obtenida con los parámetros ajustados.

### 7. La ortogonalidad que usan las masas {#solucion-20-7}

El determinante es $(4-\lambda)(6-2\lambda)-4=2(\lambda-2)(\lambda-5)$. Para $\lambda_1=2$, la primera fila da $\phi_1^{(1)}=\phi_1^{(2)}$; para $\lambda_2=5$, da $\phi_2^{(1)}=-2\phi_2^{(2)}$. Tomamos los perfiles $(1,1)$ y $(-2,1)$. Sus normas de masas al cuadrado son tres y seis en valores numéricos SI. La normalización divide por $\sqrt3$ y $\sqrt6$.

El producto euclídeo de los perfiles elegidos es $-1$ y el de masas es cero. Las frecuencias son $\sqrt2$ y $\sqrt5\,\mathrm{s^{-1}}$. Los resortes se reconstruyen leyendo el término cruzado: $\kappa=2\,\mathrm{N/m}$, $k_1=4-2=2\,\mathrm{N/m}$ y $k_2=6-2=4\,\mathrm{N/m}$. La asimetría de las masas y las paredes explica que el perfil opuesto tenga amplitudes diferentes.

### 8. Soltar la masa ligera {#solucion-20-8}

La proyección de masas da $\eta_1(0)=A/\sqrt3$, $\eta_2(0)=-2A/\sqrt6$ y derivadas nulas. Multiplicar cada coseno por su perfil reconstruye

$$
x_1=\frac A3\cos\sqrt2t+\frac{2A}3\cos\sqrt5t,
\qquad x_2=\frac A3(\cos\sqrt2t-\cos\sqrt5t).
$$

Las energías son $E_1=\lambda_1\eta_1(0)^2/2=(1\,\mathrm{N/m})A^2/3$ y $E_2=\lambda_2\eta_2(0)^2/2=5(1\,\mathrm{N/m})A^2/3$. Su razón es $E_2/E_1=5$. La suma es $2(1\,\mathrm{N/m})A^2$, igual a $K_{11}A^2/2$. Las unidades de los coeficientes modales normalizados incorporan la raíz de masa; conservarlas convierte cada producto en joules cuando $A$ se expresa en metros.

### 9. Coordenadas que mezclan posiciones {#solucion-20-9}

La relación es $x=By$, con $B=\begin{pmatrix}1&0\\1&1\end{pmatrix}$. Sustituir en las energías, antes de escribir ecuaciones, da

$$
M_y=B^{\mathsf T}MB=\begin{pmatrix}2&1\\1&1\end{pmatrix}\,\mathrm{kg},\qquad
K_y=B^{\mathsf T}KB=\begin{pmatrix}8&4\\4&6\end{pmatrix}\,\mathrm{N/m}.
$$

Los términos cruzados conservan la participación de $\dot y_1$ en ambas velocidades cartesianas. El determinante numérico es $\lambda^2-12\lambda+32=(\lambda-4)(\lambda-8)$, de modo que se recuperan las frecuencias originales. El perfil conjunto se transforma en $(1,0)$ y el opuesto en $(1,-2)$. Su producto de masas es $(1,0)M_y(1,-2)^{\mathsf T}=0$. Cambiar coordenadas conserva la dinámica y cambia la forma en que la energía registra las direcciones.

### 10. Una traslación que sigue libre {#solucion-20-10}

Sean $R=(2x_1+3x_2)/5$ y $r=x_2-x_1$, la extensión adicional del resorte. La cancelación de fuerzas internas da $\ddot R=0$. Restar aceleraciones da $\ddot r+6(1/2+1/3)r=0$, es decir, $\ddot r+5r=0$. Los datos son $R(0)=-0{,}02\,\mathrm m$, $\dot R(0)=0{,}4\,\mathrm{m/s}$, $r(0)=-0{,}2\,\mathrm m$, $\dot r(0)=0$.

Por tanto, en valores SI, $R=-0{,}02+0{,}4t$ y $r=-0{,}2\cos\sqrt5t$. La reconstrucción es $x_1=R-3r/5=-0{,}02+0{,}4t+0{,}12\cos\sqrt5t$ y $x_2=R+2r/5=-0{,}02+0{,}4t-0{,}08\cos\sqrt5t$. Se recuperan las dos posiciones y velocidades iniciales. El perfil nulo $(1,1)$ transporta el centro de masa uniformemente y mantiene la extensión del resorte. La oscilación relativa tiene frecuencia $\sqrt5\,\mathrm{s^{-1}}$ y masa reducida $6/5\,\mathrm{kg}$.

### 11. Tres masas y dos resortes {#solucion-20-11}

El potencial es $[(x_2-x_1)^2+(x_3-x_2)^2]/2$ en unidades SI. Sus derivadas proporcionan

$$
K=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}\,\mathrm{N/m}.
$$

Multiplicar por $(1,1,1)^{\mathsf T}$ da cero; multiplicar por $(1,0,-1)^{\mathsf T}$ devuelve ese mismo vector; multiplicar por $(1,-2,1)^{\mathsf T}$ devuelve tres veces el vector. Son tres direcciones independientes, con valores $0$, $1$ y $3\,\mathrm{s^{-2}}$ y frecuencias oscilatorias $1$ y $\sqrt3\,\mathrm{s^{-1}}$. Las normas euclídeas son $\sqrt3$, $\sqrt2$ y $\sqrt6$, respectivamente, y el factor de masa completa su normalización física.

El primer perfil representa traslación de la cadena. En el segundo, las masas extremas se desplazan en sentidos opuestos y los dos resortes ejercen sobre la central fuerzas iguales y opuestas. La masa central puede permanecer quieta durante todo ese modo. El tercero desplaza conjuntamente los extremos y la central en sentido contrario, con el doble de amplitud.

### 12. Dos modos con igual frecuencia {#solucion-20-12}

Cada coordenada satisface $\ddot x_i+4x_i=0$ en valores SI. La expresión propuesta suma el modo de perfil $(1,0)$ con amplitud $A\cos2t$ y el de perfil $(0,1)$ con amplitud $A\sin2t$. Su trayectoria cumple $x_1^2+x_2^2=A^2$: recorre una circunferencia con rapidez constante $2A$ por segundo.

Todo vector del plano es autovector del mismo valor $4\,\mathrm{s^{-2}}$, de modo que cualquier base ortonormal de masas sirve para descomponerlo. La trayectoria circular necesita dos coeficientes temporales con diferencia de fase. Un solo perfil real fijo describiría una recta de movimiento. La degeneración de frecuencias conserva la separación en una base elegida y permite varias elecciones igualmente válidas de esa base.

### 13. Una curvatura que permite salir {#solucion-20-13}

Las direcciones $(1,1)$ y $(1,-1)$ tienen valores $-1$ y $3\,\mathrm{s^{-2}}$. La preparación dada participa sólo en la primera. Su solución es $x(t)=\varepsilon\cosh t\,(1,1)$, tomando $t$ numérico en segundos. Satisface los datos y crece en módulo como $|\varepsilon|e^t/2$ a tiempos grandes.

Sobre $x=a(1,1)$, el potencial cuadrático vale $U=-a^2$ en las unidades elegidas. Alejarse en esa dirección disminuye el potencial y la fuerza acelera la salida. Cualquier tolerancia fija de posición se supera para datos iniciales suficientemente pequeños pero distintos de cero, si se espera el tiempo correspondiente. La conclusión se refiere al modelo lineal; en un aparato real debe respetarse el intervalo en que la fuerza utilizada representa el mecanismo.

### 14. Cuando desaparece la restauración lineal {#solucion-20-14}

Las fuerzas son $-\alpha x_i^3$ y el Hessiano en el origen es cero. La aproximación lineal satisface $\ddot x=0$, que permite derivas para velocidades iniciales distintas de cero. El sistema exacto conserva

$$
E=\frac m2\|\dot x\|^2+\frac\alpha4(x_1^4+x_2^4).
$$

De $x_1^4+x_2^4\ge(x_1^2+x_2^2)^2/2$ se sigue $\|x\|\le(8E/\alpha)^{1/4}$ y $\|\dot x\|\le(2E/m)^{1/2}$. Para tolerancias de posición $a>0$ y velocidad $b>0$, basta elegir la energía inicial estrictamente menor que $\min(\alpha a^4/8,mb^2/2)$. Por continuidad de $E$ y por $E(0,0)=0$, una vecindad inicial suficientemente pequeña cumple esa condición. Las dos cotas se mantienen para toda la trayectoria.

Las ecuaciones son suaves y los subniveles de energía son acotados y cerrados; las soluciones permanecen en un conjunto compacto de estados y se prolongan para todo tiempo futuro. Hemos demostrado estabilidad del equilibrio exacto mediante sus términos cuárticos. El Hessiano registra la ausencia de restauración de primer orden; el potencial completo suministra la barrera que controla el movimiento.

### 15. Amortiguamiento proporcional a la masa {#solucion-20-15}

Al multiplicar por $S^{\mathsf T}$, el término viscoso se transforma en $S^{\mathsf T}CS\dot\eta=\gamma\dot\eta$. Las ecuaciones son $\ddot\eta_1+\dot\eta_1+2\eta_1=0$ y $\ddot\eta_2+\dot\eta_2+5\eta_2=0$ en las unidades fijadas. Sus exponentes son $(-1\pm i\sqrt7)/2$ y $(-1\pm i\sqrt{19})/2$ por segundo. Ambos modos oscilan con envolvente $e^{-t/2}$, y la energía total satisface $\dot E=-\dot x^{\mathsf T}C\dot x\le0$.

Con un solo amortiguador, los perfiles del problema 7 dan un coeficiente cruzado numérico $-2c/\sqrt{18}$ en $S^{\mathsf T}CS$, con las unidades correspondientes a la normalización. Esa entrada multiplica la velocidad del otro coeficiente modal. La base que separaba masa y rigidez sigue representando el estado, pero las ecuaciones viscosas conservan un acoplamiento. La proporcionalidad a $M$ era la hipótesis que eliminaba precisamente esa mezcla.

### 16. Forzar un carro y observar el otro {#solucion-20-16}

Sumar y restar las fuerzas produce $\ddot Q_\pm+\omega_\pm^2Q_\pm=F\cos\Omega t/(2m)$. Una respuesta particular es

$$
Q_\pm^{\mathrm p}=\frac{F}{2m(\omega_\pm^2-\Omega^2)}\cos\Omega t.
$$

La suma de coeficientes que determina $x_1^{\mathrm p}$ se anula cuando $\Omega^2=(\omega_+^2+\omega_-^2)/2=6\,\mathrm{s^{-2}}$. La diferencia da $x_2^{\mathrm p}=-(F/\kappa)\cos\Omega t=-0{,}05\cos(\sqrt6t)\,\mathrm m$. Aunque el primer carro permanece en su equilibrio, el resorte central transmite una fuerza que compensa instantáneamente la excitación.

En el modelo sin disipación, la solución general añade los dos modos libres. Para observar exclusivamente esta respuesta se prepara $x_1(0)=0$, $x_2(0)=-0{,}05\,\mathrm m$ y velocidades nulas, tomando la fuerza con la fase de coseno indicada. Otros datos conservan oscilaciones libres. En $\Omega=2$ o $\sqrt8\,\mathrm{s^{-1}}$ el denominador respectivo se anula y hay que resolver una respuesta resonante con término secular.

### 17. Un reloj que confunde frecuencias {#solucion-20-17}

La frecuencia $\omega'=\omega+2\pi/\Delta t=\omega+20\pi\,\mathrm{s^{-1}}$ produce $\cos(\omega'n\Delta t)=\cos(\omega n\Delta t+2\pi n)=\cos(\omega n\Delta t)$ para todo entero $n$. Todas las lecturas coinciden, aun con precisión ideal y una serie arbitrariamente larga en esos instantes.

Puede distinguirse esa pareja mediante registros en tiempos intermedios elegidos para que la diferencia de fase deje de ser un múltiplo de vuelta completa. Para identificar una frecuencia entre todas las alternativas se necesita además un rango previo justificado y una pauta temporal adecuada a ese rango, o mediciones adicionales de velocidad y del movimiento entre muestras. La repetición exacta de registros preserva su precisión; el diseño temporal decide qué frecuencias permiten inferir.

### 18. El paso temporal y el modo más rápido {#solucion-20-18}

Con el estado ordenado como $(\eta,v)$, la matriz es

$$
B_h=\begin{pmatrix}1-h^2\omega^2&h\\-h\omega^2&1\end{pmatrix},
\qquad \det B_h=1,\quad \operatorname{tr}B_h=2-h^2\omega^2.
$$

Para $0<h\omega<2$, sus autovalores son distintos, conjugados y de módulo uno: el polinomio es $z^2-(2-h^2\omega^2)z+1$ y su discriminante es negativo. La diagonalización compleja conserva una cota para todas las potencias y, por tanto, para todos los datos iniciales. Si $h\omega>2$, los autovalores son reales recíprocos y uno tiene módulo mayor que uno. En $h\omega=2$ ambos son $-1$, pero $B_h\ne-I$; el bloque doble produce crecimiento lineal de algunas iteradas.

Para que todos los modos positivos queden acotados se impone $0<h<2/\omega_{\max}$. En el problema 7 resulta $0<h<2/\sqrt5\,\mathrm s$, aproximadamente $0<h<0{,}8944\,\mathrm s$. El extremo superior es un supremo excluido. Esta condición controla acotación del algoritmo; la precisión de fase y amplitud requiere comparar pasos menores y el estado exacto cuando se conoce.

### 19. Una prueba con producto ordinario {#solucion-20-19}

En los valores SI, $M^{-1}K=\begin{pmatrix}4&-2\\-1&3\end{pmatrix}$ es una matriz con entradas cruzadas distintas. La aplicación directa del teorema espectral euclídeo exige una simetría que esa matriz carece en esas coordenadas. Los perfiles del problema 7 confirman el resultado geométrico: su producto euclídeo es $-1$.

Sea $A=M^{-1}K$. Para cualesquiera $u,v$,

$$
\langle u,Av\rangle_M=u^{\mathsf T}Kv
=\langle Au,v\rangle_M,
$$

pues $K$ y $M$ son simétricas. Si $Au=\lambda u$ y $Av=\mu v$, la identidad da $(\mu-\lambda)\langle u,v\rangle_M=0$. Para valores distintos se obtiene ortogonalidad de masas. La conjugación $M^{1/2}AM^{-1/2}=M^{-1/2}KM^{-1/2}$ produce la matriz simétrica euclídea que utiliza la prueba general del capítulo.

### 20. Cotas y contraste de una identificación {#solucion-20-20}

Las frecuencias son positivas, por lo que elevarlas al cuadrado conserva el orden. Para el resorte de pared,

$$
k\in[0{,}5(1{,}99)^2,0{,}5(2{,}01)^2]
=[1{,}98005,2{,}02005]\,\mathrm{N/m}.
$$

El acoplamiento aumenta con la frecuencia rápida y disminuye con la lenta. Admitiendo todas las combinaciones,

$$
\kappa\in\frac14[(2{,}99)^2-(2{,}01)^2,
(3{,}01)^2-(1{,}99)^2]
=[1{,}225,1{,}275]\,\mathrm{N/m}.
$$

Estas bandas son envolventes individuales válidas. Una frecuencia lenta mayor aumenta $k$ y, para una misma rápida, disminuye $\kappa$; conservar las dos frecuencias mantiene esa dependencia entre parámetros. Una región rectangular de cotas individuales admite combinaciones adicionales.

Para contrastar los perfiles, se desplazan ambos carros por igual y se sueltan con velocidades nulas, registrando $x_1-x_2$ durante varios ciclos. Después se prepara la disposición opuesta y se registra $x_1+x_2$. El aparato simétrico predice cero para esas combinaciones en los respectivos ensayos. Las tolerancias deben incluir la preparación, las calibraciones y el muestreo de ambos sensores. Una discrepancia persistente motiva revisar masas, apoyos, rozamiento y linealidad. Esos ensayos aportan información sobre el modelo mediante proporciones que las dos frecuencias usadas para ajustar sus rigideces dejaban abiertas.

### 21. Dos movimientos detrás de un mismo registro {#solucion-20-21}

Las frecuencias son $\omega_+=2\,\mathrm{s^{-1}}$ y $\omega_-=2\sqrt2\,\mathrm{s^{-1}}$. La primera preparación tiene $Q_+(0)=Q_-(0)=A/2$; la segunda tiene $Q_+(0)=A/2$, $Q_-(0)=0$. En ambas las velocidades iniciales son cero. Por tanto, expresando $t$ en segundos,

$$
\begin{aligned}
x_1^{(a)}&=\frac A2[\cos(2t)+\cos(2\sqrt2\,t)],&
x_2^{(a)}&=\frac A2[\cos(2t)-\cos(2\sqrt2\,t)],\\
x_1^{(b)}&=\frac A2\cos(2t),&
x_2^{(b)}&=\frac A2\cos(2t).
\end{aligned}
$$

El promedio de ambas parejas es exactamente $y=(A/2)\cos(2t)$. El sensor conserva el movimiento conjunto y elimina la participación opuesta. Podemos añadir a $Q_-$ cualquier solución $B\cos(\omega_-t)+C\sin(\omega_-t)$ manteniendo $Q_+=(A/2)\cos(\omega_+t)$, y obtenemos el mismo registro. Las preparaciones compatibles tienen $x(0)=(A/2+B,A/2-B)$ y $\dot x(0)=(\omega_-C,-\omega_-C)$.

La energía modal vale

$$
E=\frac{kA^2}{4}+m\omega_-^2(B^2+C^2).
$$

Para las dos preparaciones concretas, $E_a=1{,}2\times10^{-3}\,\mathrm J$ y $E_b=4\times10^{-4}\,\mathrm J$. En el modelo lineal ideal, el registro permite energías sin cota superior al variar $B,C$. En un aparato físico, las amplitudes admisibles siguen sujetas al intervalo lineal de los resortes y a las distancias disponibles. La pérdida de información subsiste dentro de cualquier intervalo que admita más de una de estas preparaciones.

Añadir $z=x_1$ permite reconstruir $x_1=z$ y $x_2=2y-z$ en cada instante. Si ambas lecturas tienen errores absolutos acotados por $\varepsilon$, la cota directa para el segundo carro es $3\varepsilon$. Mantener la relación entre ambas lecturas permite afinarla cuando se conocen dependencias de calibración, como en el capítulo 0.

Con parámetros exactos, el registro de $z=x_1$ solo también permite recuperar los dos modos mediante la proposición, pues ambos coeficientes valen uno. En este caso $\omega_-^2-\omega_+^2=4\,\mathrm{s^{-2}}$, y las fórmulas son $Q_+=(\ddot z+\omega_-^2z)/(\omega_-^2-\omega_+^2)$ y $Q_-=z-Q_+$. Las velocidades iniciales se obtienen derivando, lo que introduce la tercera derivada de $z$. La información temporal exacta contiene los cuatro datos; estimar esas derivadas a partir de lecturas perturbadas exige un control de ruido y de muestreo que la identidad algebraica deja abierto.

![Dos preparaciones con promedio idéntico y diferentes trayectorias del primer carro.](/assets/books/fispm/r20261021/acoplados_sensor_modos.svg){.fpm-v04-figure}

*Figura 20.8.* En el panel izquierdo coinciden los promedios de las dos preparaciones, aunque sus energías son distintas. El derecho conserva la lectura del primer carro y distingue los movimientos. Las curvas son soluciones exactas del modelo lineal; se muestran diez segundos del registro continuo.

## Lecturas y relaciones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 8, pp. 302–307, desarrolla el paso desde dos osciladores a sus perfiles y a la modulación; el capítulo 14, pp. 476–481, sitúa la separación en la aproximación de pequeñas oscilaciones y el problema generalizado de masas y rigideces. Aquí las ecuaciones se construyen primero desde Newton y las formas de energía; la formulación lagrangiana se desarrolla en los capítulos siguientes.

Sears–Zemansky, Young y Freedman, *Física universitaria*, volumen 1, §14.3, pp. 445–447, permite cotejar la contabilidad energética del oscilador; §15.8, pp. 495–496, amplía la idea de perfil a una cuerda. Serway–Jewett, *Física para ciencias e ingeniería*, volumen 1, §17.7, pp. 469–471, desarrolla la lectura temporal de los batimientos. La identidad trigonométrica compartida sirve aquí para interpretar las posiciones de dos carros cuyas fuerzas están acopladas.

El apunte *MEC Resumen Oscilaciones Acopladas con Lagrangeano*, conservado en la biblioteca de problemas, ofrece una familia de dos masas libres y un resorte con modo de traslación. Esa familia se retoma con masas distintas y reconstrucción desde datos iniciales. Los problemas, datos, demostraciones y figuras de este capítulo se desarrollaron para esta redacción.

---

[← 19. Cuerpo rígido en tres dimensiones](fisica-para-matematicos-19-cuerpo-rigido-en-tres-dimensiones.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [21. Trabajo virtual, coordenadas generalizadas y acción →](fisica-para-matematicos-21-trabajo-virtual-coordenadas-generalizadas-y-accion.md)
