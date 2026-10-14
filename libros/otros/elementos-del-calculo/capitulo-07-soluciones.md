---
title: Capítulo 7 — Soluciones desarrolladas
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
license: GFDL-1.3-or-later
areas:
  - calculo
  - analisis
  - fundamentos
level: intermedio
topics:
  - calculo-de-una-variable
  - historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
    - role: idea
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C07-SOLUCIONES
source-sha256: 005cb3834c69d4308ed234c4ed3056a3a3f935a43cb320728e2641185707e1bd
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-07.html) · [Ejercicios](capitulo-07-ejercicios.html) · [Soluciones](capitulo-07-soluciones.html)

Las siguientes soluciones corresponden, una por una, a [los treinta ejercicios del capítulo](capitulo-07-ejercicios.html). Se han utilizado únicamente resultados demostrados en C00–C07. Los cálculos no se separan de sus hipótesis: las funciones racionales se integran sobre intervalos que evitan sus polos, las fórmulas de sustitución conservan extremos orientados y las integrales definidas son propias.

## A. Hipótesis, lenguaje y elecciones de método

### Solución 7.1 (`EDC-C07-SOL-001`)

(a) Si $f:[a,b]\to\mathbb R$ es continua, la integrabilidad se sigue del Teorema 5.4: las sumas de Darboux pueden aproximarse arbitrariamente. Esto **establece la existencia de un número**, sin exigir una fórmula para encontrarlo. (b) Hallar una primitiva es construir $F$ continua en $[a,b]$, derivable en $(a,b)$, tal que $F'=f$ allí. La primera parte del Teorema Fundamental (C06) garantiza existencia cuando $f$ es continua, aunque $F$ pueda quedar expresada como acumulación. (c) La segunda parte (`EDC-C06-THM-005`) demuestra que el valor de la integral es $F(b)-F(a)$. No debemos usar esta última igualdad para definir la integral y luego anunciarla como teorema: en EDC la integral ya se definió mediante Darboux.

### Solución 7.2 (`EDC-C07-SOL-002`)

El Teorema 7.1 se demuestra componiendo una primitiva $F$ de $f$ con $\phi$ y usando la cadena. No se necesita resolver $t$ a partir de $\phi(t)$; por eso el cambio puede invertir la orientación o recorrer varias veces un valor. La derivada conserva el signo de cada recorrido.

Para $\phi(t)=1-t$ y $f(u)=u$, el cambio lleva el extremo cero a uno y el extremo uno a cero, con derivada $-1$. Resulta

$$
\int_0^1 f(1-t)(-1)\,dt
=\int_1^0u\,du=-\frac12.
$$

La comprobación directa integra $t-1$ y da $[t^2/2-t]_0^1=-1/2$. El signo negativo aparece tanto en la derivada del cambio como en el orden de los extremos de la integral transformada, dos maneras compatibles de registrar el mismo retroceso.

### Solución 7.3 (`EDC-C07-SOL-003`)

Para aplicar la sustitución evaluamos $\phi(t)=t^2$ en los extremos originales. Tanto $-1$ como $1$ se convierten en uno; cero es un valor interior del recorrido, que se alcanza cuando $t=0$. Con $\phi'(t)=2t$, el teorema da

$$
\int_{-1}^1 2te^{t^2}\,dt
=\int_{\phi(-1)}^{\phi(1)}e^u\,du
=\int_1^1e^u\,du=0.
$$

Podemos separar en cero para ver la cancelación: en $[-1,0]$ el nuevo argumento va de uno a cero y aporta $1-e$; en $[0,1]$ va de cero a uno y aporta $e-1$. La integral propuesta por el estudiante conserva sólo ese segundo recorrido. La imparidad de $2te^{t^2}$ ofrece también un control del valor cero.

### Solución 7.4 (`EDC-C07-SOL-004`)

El integrando $1/x$ **no está definido en $0$**, que pertenece a $[-1,1]$. No es una función real acotada sobre todo ese intervalo y no se le puede aplicar la definición propia de Darboux de C05. Una cancelación informal de los intervalos a ambos lados de cero no crea una integral propia. En cambio $1/x$ es continua en $[1,2]$, allí sí es integrable, y

$$
\int_1^2\frac{dx}{x}=[\ln x]_1^2=\ln2.
$$

La primitiva $\ln|x|$ existe separadamente en $(-\infty,0)$ y $(0,\infty)$; no cruza el origen.

## B. Sustitución y extremos

### Solución 7.5 (`EDC-C07-SOL-005`)

La función $1+x^3$ es positiva en $[0,2]$. Elegimos $u=1+x^3$ y $du=3x^2\,dx$ como abreviatura de $du/dx=3x^2$. Los extremos se transforman en $u(0)=1$ y $u(2)=9$. Luego

$$
\int_0^2 3x^2(1+x^3)^4\,dx
=\int_1^9u^4\,du
=\left[\frac{u^5}5\right]_1^9
=\frac{9^5-1}{5}=11809.6.
$$

El valor exacto preferible es $(9^5-1)/5=59048/5$; la igualdad decimal sólo representa ese racional.

### Solución 7.6 (`EDC-C07-SOL-006`)

Puesto que $1+x^2\ge1$ en $[0,1]$, el integrando es continuo. Poniendo $u=1+x^2$ y $du/dx=2x$,

$$
\int_0^1\frac{2x}{1+x^2}\,dx
=\int_1^2\frac{du}{u}=[\ln u]_1^2=\ln2.
$$

La positividad de $u$ autoriza usar el logaritmo natural sin valor absoluto.

### Solución 7.7 (`EDC-C07-SOL-007`)

Con $u=\sin x$, $du/dx=\cos x$, y extremos $0,1$,

$$
\int_0^{\pi/2}\sin x\cos x\,dx
=\int_0^1u\,du=\frac12.
$$

Como $2\sin x\cos x=\sin2x$, otra prueba es $\frac12\int_0^{\pi/2}\sin2x\,dx=[-\cos2x/4]_0^{\pi/2}=1/2$. Los senos y cosenos son continuos en el intervalo.

### Solución 7.8 (`EDC-C07-SOL-008`)

La función $x^2$ es continuamente derivable en todo $[-1,1]$, y la exponencial es continua sobre un intervalo abierto que contiene su recorrido. El Teorema 7.1 no exige monotonía del cambio. Como los extremos se convierten ambos en uno,

$$
\int_{-1}^1 2xe^{x^2}\,dx=\int_1^1e^u\,du=0.
$$

En la mitad izquierda la derivada $2x$ es negativa y en la derecha positiva; los dos recorridos del argumento producen contribuciones opuestas. Si la reemplazamos por $|2x|$, quitamos el signo de la primera contribución. El nuevo integrando es par y no negativo, y su integral vale $2\int_0^1 2xe^{x^2}\,dx=2(e-1)>0$. Esta última suma las magnitudes de los aportes; no evalúa la expresión pedida.

### Solución 7.9 (`EDC-C07-SOL-009`)

Sea $u=3x+1$, de modo que $du/dx=3$ y $dx=du/3$ en la notación abreviada. $x=0$ da $u=1$ y $x=1$ da $u=4$. Por tanto,

$$
\int_0^1e^{3x+1}\,dx
=\frac13\int_1^4e^u\,du
=\frac{e^4-e}{3}.
$$

La función es continua en todo $\mathbb R$ y la fórmula es una aplicación del Teorema 7.1 con cambio afín.

### Solución 7.10 (`EDC-C07-SOL-010`)

En $[0,1]$ tenemos $1+x^2\in[1,2]$, de modo que la raíz es real y continua. Escribiendo $u=1+x^2$,

$$
\begin{aligned}
\int_0^1x\sqrt{1+x^2}\,dx
&=\frac12\int_1^2u^{1/2}\,du\\
&=\frac13\left[u^{3/2}\right]_1^2
=\frac{2\sqrt2-1}{3}.
\end{aligned}
$$

La comprobación por derivación de $(1+x^2)^{3/2}/3$ produce $x\sqrt{1+x^2}$.

### Solución 7.11 (`EDC-C07-SOL-011`)

El denominador cumple $2+\sin x\ge1$ para todo $x$, por lo que el integrando es continuo en $[0,\pi]$. Tomamos $\phi(x)=2+\sin x$, cuya derivada es $\cos x$, y la función exterior $f(u)=1/u$ sobre el intervalo abierto positivo. Sus extremos son $\phi(0)=\phi(\pi)=2$ y la sustitución da

$$
\int_0^\pi\frac{\cos x}{2+\sin x}\,dx
=\int_2^2\frac{du}{u}=0.
$$

El argumento sube de dos a tres y vuelve a dos. La derivada cambia de signo en el regreso y conserva la orientación de ese segundo aporte. También podemos evaluar la primitiva $\ln(2+\sin x)$: tiene el mismo valor en ambos extremos. Ninguna de las dos justificaciones necesita una inversa global del cambio.

### Solución 7.12 (`EDC-C07-SOL-012`)

El intervalo $[1,e]$ está contenido en $(0,\infty)$; $\ln x/x$ es continuo. La sustitución $u=\ln x$, con $du/dx=1/x$, transforma los extremos en $0,1$:

$$
\int_1^e\frac{\ln x}{x}\,dx=\int_0^1u\,du=\frac12.
$$

Una primitiva sobre $(0,\infty)$ es $(\ln x)^2/2$; al derivarla se obtiene $(\ln x)/x$.

## C. Integración por partes

### Solución 7.13 (`EDC-C07-SOL-013`)

Con $u=x$, $u'=1$, $v'=e^x$, $v=e^x$, el Teorema 7.2 da

$$
\int_0^1 xe^x\,dx=[xe^x]_0^1-\int_0^1e^x\,dx=e-(e-1)=1.
$$

La función $(x-1)e^x$ tiene derivada $e^x+(x-1)e^x=xe^x$, y sus valores terminales son $0$ y $-1$, cuya diferencia es $1$.

### Solución 7.14 (`EDC-C07-SOL-014`)

Elegimos $u=x$, $u'=1$, $v'=\sin x$, $v=-\cos x$. Entonces

$$
\int_0^\pi x\sin x\,dx
=[-x\cos x]_0^\pi+\int_0^\pi\cos x\,dx
=\pi+\sin\pi-\sin0=\pi.
$$

El resultado es positivo, compatible con $x\ge0$ y $\sin x\ge0$ en el intervalo.

### Solución 7.15 (`EDC-C07-SOL-015`)

Escribimos $\ln x=(\ln x)\cdot1$. En $[1,e]$ elegimos $u=\ln x$, $u'=1/x$, $v'=1$, $v=x$, todos continuos en su dominio. Por tanto

$$
\int_1^e\ln x\,dx=[x\ln x]_1^e-\int_1^e1\,dx=e-(e-1)=1.
$$

El candidato $x\ln x-x$ es primitiva de $\ln x$ sobre el semieje positivo, pues su derivada es $\ln x+1-1=\ln x$.

### Solución 7.16 (`EDC-C07-SOL-016`)

Elegimos derivar el factor polinómico, porque cada derivación disminuye su grado, e integrar la exponencial, que permanece igual. La primera aplicación, con $u=x^2$ y $v'=e^x$, produce

$$
\int x^2e^x\,dx=x^2e^x-2\int xe^x\,dx.
$$

En la integral restante usamos $u=x$ y $v'=e^x$, que da $\int xe^x\,dx=xe^x-e^x+C$. Sustituimos y reunimos los términos exponenciales:

$$
\int x^2e^x\,dx=e^x(x^2-2x+2)+C.
$$

Para comprobarla derivamos por el producto. La derivada es $e^x[(x^2-2x+2)+(2x-2)]=x^2e^x$; los términos lineales y constantes se cancelan. El integrando es continuo en $[0,1]$, así que la segunda parte del Teorema Fundamental evalúa

$$
\int_0^1x^2e^x\,dx=e\,(1-2+2)-2=e-2.
$$

La constante elegida en la primitiva no interviene en esa diferencia terminal.

### Solución 7.17 (`EDC-C07-SOL-017`)

Usamos acumulaciones con un origen fijo para que cada igualdad determine funciones concretas. Sea $I(x)=\int_0^xe^t\cos t\,dt$. Por partes, derivando el coseno e integrando la exponencial,

$$
I(x)=e^x\cos x-1+J(x),\qquad J(x)=\int_0^xe^t\sin t\,dt.
$$

El término $-1$ viene del producto en cero. Una segunda aplicación, ahora derivando el seno, da $J(x)=e^x\sin x-I(x)$; el producto terminal en cero se anula. Ambas identidades valen para $x$ positivo o negativo por orientación. Al sustituir $J$ en la primera igualdad, aparece $I$ a ambos lados con signos opuestos. Lo reunimos en el izquierdo:

$$
2I(x)=e^x(\sin x+\cos x)-1.
$$

Dividir por dos explica el factor buscado. La acumulación y la candidata difieren en una constante, de modo que todas las primitivas tienen la forma

$$
G(x)=\frac12e^x(\sin x+\cos x)+C.
$$

Por el producto, $G'=\frac12e^x[(\sin x+\cos x)+(\cos x-\sin x)]=e^x\cos x$. La repetición cerró el sistema de dos integrales y el factor $1/2$ procede de las dos apariciones de la misma $I$, reunidas en un único despeje.

### Solución 7.18 (`EDC-C07-SOL-018`)

Con $u=x$, $v'=\cos(2x)$ tenemos $u'=1$ y $v=\sin(2x)/2$. Entonces

$$
\begin{aligned}
\int_0^1x\cos(2x)\,dx
&=\left[\frac{x\sin(2x)}2\right]_0^1
-\frac12\int_0^1\sin(2x)\,dx\\
&=\frac{\sin2}{2}+\left[\frac{\cos(2x)}4\right]_0^1
=\frac{\sin2}{2}+\frac{\cos2-1}{4}.
\end{aligned}
$$

La derivada de $x\sin(2x)/2+\cos(2x)/4$ es $x\cos2x$.

### Solución 7.19 (`EDC-C07-SOL-019`)

Con $u(x)=v(x)=x$ para $0\le x\le1$,

$$
\int_0^1uv\,dx=\int_0^1x^2\,dx=\frac13,
\qquad
\left(\int_0^1u\,dx\right)\left(\int_0^1v\,dx\right)=\frac14.
$$

Son distintos. La linealidad de la integral vale para sumas y múltiplos constantes, **no** convierte el producto de funciones en producto de integrales. La identidad correcta relevante es $(uv)'=u'v+uv'$, que conduce a integración por partes cuando se conocen primitivas y regularidad apropiadas.

## D. Fracciones racionales y controles de dominio

### Solución 7.20 (`EDC-C07-SOL-020`)

Buscamos $A/x+B/(x-1)$ en el dominio $x\notin\{0,1\}$. Multiplicar por el denominador transforma la igualdad racional propuesta en la identidad polinómica

$$
1=A(x-1)+Bx.
$$

Esta identidad se puede evaluar en los puntos excluidos de la fracción original: ya no estamos evaluando el cociente, sino los polinomios. En cero queda $A=-1$ y en uno $B=1$. Al sustituir, el numerador resultante es $-(x-1)+x=1$, que verifica la igualdad para todo $x$ donde el denominador no sea cero.

Cada logaritmo se deriva dentro de un intervalo que evita su raíz. Por tanto, en $(-\infty,0)$, $(0,1)$ y $(1,\infty)$,

$$
\int\frac{dx}{x(x-1)}=-\ln|x|+\ln|x-1|+C.
$$

La derivada recupera $-1/x+1/(x-1)=1/[x(x-1)]$. La constante es única para cada componente y puede elegirse de manera independiente entre los tres.

### Solución 7.21 (`EDC-C07-SOL-021`)

Verificamos la identidad

$$
\frac1{x(x-1)^2}=\frac1x-\frac1{x-1}+\frac1{(x-1)^2}
$$

llevando el lado derecho al denominador común: su numerador es $(x-1)^2-x(x-1)+x=x^2-2x+1-x^2+x+x=1$. La primitiva, para $x\ne0,1$ y en cada intervalo conexo del dominio, es

$$
\ln|x|-\ln|x-1|-\frac1{x-1}+C.
$$

La última derivada vale $(x-1)^{-2}$, porque $( - (x-1)^{-1})'=(x-1)^{-2}$. No se integran a través de los polos.

### Solución 7.22 (`EDC-C07-SOL-022`)

Completamos el cuadrado: $x^2+2x+2=(x+1)^2+1>0$ para todo $x$. El numerador se divide como $(2x+2)+1$. Entonces

$$
\begin{aligned}
\int\frac{2x+3}{x^2+2x+2}\,dx
&=\int\frac{2x+2}{(x+1)^2+1}\,dx
+\int\frac{dx}{(x+1)^2+1}\\
&=\ln((x+1)^2+1)+\arctan(x+1)+C.
\end{aligned}
$$

La primera derivada es $(2x+2)/Q(x)$ y la segunda $1/Q(x)$; suman el integrando. No hay restricciones de dominio adicionales.

### Solución 7.23 (`EDC-C07-SOL-023`)

La división euclídea separa la parte polinómica: $x^3+1=x(x^2-1)+(x+1)$. Para $x\ne-1,1$ podemos factorizar el denominador y cancelar el factor $x+1$:

$$
\frac{x^3+1}{x^2-1}=x+\frac{x+1}{(x-1)(x+1)}=x+\frac1{x-1}.
$$

En $[2,3]$ el cociente original es continuo y $x-1$ es positivo. Una primitiva válida en todo el tramo es $x^2/2+\ln(x-1)$, por lo que

$$
\int_2^3\frac{x^3+1}{x^2-1}\,dx
=\left[\frac{x^2}{2}+\ln(x-1)\right]_2^3
=\frac52+\ln2.
$$

La cancelación utilizó que $x+1$ no era cero. La expresión simplificada admite un valor en $x=-1$, pero el cociente original sigue sin estar definido allí. Rellenar ese punto daría una extensión de la función; no forma parte de la simplificación ni del dominio pedido.

### Solución 7.24 (`EDC-C07-SOL-024`)

El denominador $Q(x)=(x-1)(x-2)(x-3)$ tiene tres raíces reales distintas y el numerador constante tiene grado menor que tres. El Teorema 7.3 da $A_i=1/Q'(r_i)$; cada derivada en una raíz es el producto de sus diferencias con las otras:

$$
Q'(1)=(1-2)(1-3)=2,\quad
Q'(2)=(2-1)(2-3)=-1,\quad
Q'(3)=(3-1)(3-2)=2.
$$

Los coeficientes son $1/2,-1,1/2$, y obtenemos

$$
\frac1{(x-1)(x-2)(x-3)}
=\frac{1/2}{x-1}-\frac1{x-2}+\frac{1/2}{x-3}.
$$

Para controlar la identidad multiplicamos por $Q$. El numerador derecho es $(x-2)(x-3)/2-(x-1)(x-3)+(x-1)(x-2)/2$. Su coeficiente cuadrático es $1/2-1+1/2=0$, el lineal es $-5/2+4-3/2=0$ y el constante es $3-3+1=1$. Coincide con el numerador izquierdo.

En cada uno de los intervalos $(-\infty,1)$, $(1,2)$, $(2,3)$ y $(3,\infty)$, el Corolario 7.3 proporciona

$$
\frac12\ln|x-1|-\ln|x-2|+\frac12\ln|x-3|+C.
$$

Los módulos mantienen los logaritmos reales a ambos lados de las raíces; las constantes pueden variar entre componentes.

## E. Aplicaciones y significado de la integral

### Solución 7.25 (`EDC-C07-SOL-025`)

En $0\le x\le2$, $2x-x^2=x(2-x)\ge0$, por lo que $y=2x$ está encima de $y=x^2$. El área es

$$
A=\int_0^2(2x-x^2)\,dx
=\left[x^2-\frac{x^3}{3}\right]_0^2
=4-\frac83=\frac43.
$$

La continuidad de la diferencia garantiza la existencia de la integral; su no negatividad justifica leerla como área geométrica.

### Solución 7.26 (`EDC-C07-SOL-026`)

El área total integra la altura $|x-x^2|$. Los cruces están en cero y uno, porque $x-x^2=x(1-x)$. La diferencia es negativa en $[-1,0]$, positiva en $[0,1]$ y negativa en $[1,2]$. En cada tramo usamos la curva superior menos la inferior:

$$
\begin{aligned}
A&=\int_{-1}^0(x^2-x)\,dx
+\int_0^1(x-x^2)\,dx
+\int_1^2(x^2-x)\,dx\\
&=\frac56+\frac16+\frac56=\boxed{\frac{11}{6}}.
\end{aligned}
$$

Las dos contribuciones exteriores se evalúan con $x^3/3-x^2/2$ y la central con su opuesta. En cambio, la integral orientada conserva el signo de la diferencia:

$$
\int_{-1}^{2}(x-x^2)\,dx
=\left[\frac{x^2}2-\frac{x^3}3\right]_{-1}^{2}
=-\frac32,
$$

cuyo módulo es $3/2$, distinto de $11/6$. Las contribuciones negativas suman $-5/3$ y la positiva $1/6$; cancelarlas antes de tomar el módulo pierde parte del área que queremos medir.

### Solución 7.27 (`EDC-C07-SOL-027`)

El trabajo de la fuerza externa en el desplazamiento positivo es

$$
W_{\mathrm{ext}}=\int_0^L kx\,dx=\frac{kL^2}{2}.
$$

Para la fuerza de restitución, que se opone al desplazamiento, obtenemos

$$
W_{\mathrm{res}}=\int_0^L(-kx)\,dx=-\frac{kL^2}{2}.
$$

Si $k$ se mide en $\mathrm{N}/\mathrm m$ y $L$ en $\mathrm m$, $kL^2$ tiene unidades $\mathrm{N\,m}=\mathrm J$. No se deben intercambiar los signos de fuerzas físicamente opuestas.

### Solución 7.28 (`EDC-C07-SOL-028`)

Por el Teorema Fundamental aplicado a $Q'=r$,

$$
Q(4)-Q(1)=\int_1^4(2t+3)\,dt
=\left[t^2+3t\right]_1^4
=(16+12)-(1+3)=24.
$$

Para hallar $Q(4)$ como número absoluto necesitamos una condición inicial, por ejemplo el valor $Q(1)$. La derivada sólo determina $Q$ hasta una constante; en el modelo habría que especificar además las unidades de $t$ y $Q$ para atribuir unidades coherentes a los coeficientes $2$ y $3$.

## F. Demostraciones y desafío de síntesis

### Solución 7.29 (`EDC-C07-SOL-029`)

Usamos $\phi(t)=-t$ sobre $[-b,-a]$, cuyos extremos están ordenados porque $a<b$. Para ajustar literalmente la hipótesis de intervalo abierto del Teorema 7.1, basta disponer de $f$ sobre uno que contenga $[a,b]$. Si el intervalo del enunciado sólo da continuidad hasta los bordes, prolongamos la restricción de $f$ con el valor constante $f(a)$ a la izquierda y $f(b)$ a la derecha. La prolongación es continua y coincide con $f$ en todo el recorrido del cambio, por lo que ninguna integral pedida se altera.

Tenemos $\phi(-b)=b$, $\phi(-a)=a$ y $\phi'=-1$. La sustitución orientada da

$$
-\int_{-b}^{-a}f(-t)\,dt
=\int_b^a f(u)\,du
=-\int_a^b f(u)\,du.
$$

Multiplicamos los dos lados por $-1$ y obtenemos

$$
\boxed{\int_{-b}^{-a}f(-t)\,dt=\int_a^b f(u)\,du.}
$$

Un signo negativo procede de la derivada del cambio y el otro del orden invertido de las imágenes terminales; se compensan. La continuidad asegura que las integrales son propias y que la prolongación usada para aplicar el teorema no introduce una dificultad nueva.

### Solución 7.30 (`EDC-C07-SOL-030`)

Los tres sumandos son continuos en $[0,1]$: los argumentos logarítmicos y los factores del denominador son positivos allí. La linealidad permite calcular cada contribución con el procedimiento que su estructura sugiere.

**Primer sumando.** El factor $2x$ es la derivada del argumento $x^2$. Con $u=x^2$, las imágenes de los extremos son cero y uno, y

$$
\int_0^12xe^{x^2}\,dx=\int_0^1e^u\,du=e-1.
$$

**Segundo sumando.** El cambio $u=1+x^2$ proporciona $du/dx=2x$, por lo que el factor $x$ deja un coeficiente $1/2$. Los extremos se convierten en uno y dos. La integral transformada de $\ln u$ se calcula por partes, escribiéndolo como $(\ln u)\cdot1$:

$$
\begin{aligned}
\int_0^1x\ln(1+x^2)\,dx
&=\frac12\int_1^2\ln u\,du\\
&=\frac12[\,u\ln u-u\,]_1^2
=\ln2-\frac12,
\end{aligned}
$$

donde la elección de factores produce la primitiva $u\ln u-u$ sobre el semieje positivo.

**Tercer sumando.** Buscamos $A/(x+1)+B/(x+2)$. Multiplicar por el denominador exige $1=A(x+2)+B(x+1)$; evaluar en $-1$ y $-2$ da $A=1$ y $B=-1$. Así,

$$
\frac1{(x+1)(x+2)}=\frac1{x+1}-\frac1{x+2}
$$

y los argumentos positivos permiten usar los logaritmos sin módulos en $[0,1]$:

$$
\begin{aligned}
\int_0^1\frac{dx}{(x+1)(x+2)}
&=[\ln(x+1)-\ln(x+2)]_0^1\\
&=\ln\left(\frac23\right)-\ln\left(\frac12\right)
=\ln\frac43.
\end{aligned}
$$

Las partes constantes suman $e-3/2$ y los logaritmos se reúnen como $\ln2+\ln(4/3)=\ln(8/3)$. El resultado es

$$
\boxed{\int_0^1\left(2xe^{x^2}+x\ln(1+x^2)+\frac1{(x+1)(x+2)}\right)dx
=e-\frac32+\ln\frac83.}
$$

Para comprobarlo con una primitiva explícita, tomamos

$$
G(x)=e^{x^2}+\frac12\bigl[(1+x^2)\ln(1+x^2)-(1+x^2)\bigr]
+\ln(x+1)-\ln(x+2).
$$

La cadena da $2xe^{x^2}$ en el primer término. Si $u=1+x^2$, derivar $[u\ln u-u]/2$ deja $u'\ln u/2=x\ln(1+x^2)$: los términos $u'/2$ se cancelan. Los logaritmos finales aportan $1/(x+1)-1/(x+2)$, que es la fracción original. Así $G'$ coincide con todo el integrando sobre un intervalo abierto que contiene $[0,1]$, y $G(1)-G(0)$ confirma la evaluación anterior.
