---
title: Capítulo 6 — Soluciones desarrolladas
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
source-id: EDC-C06-SOLUCIONES
source-sha256: 448566ff69cf960643439832b4c7c86e453df32b7adf48e5b0f248ead3588d66
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-06.html) · [Ejercicios](capitulo-06-ejercicios.html) · [Soluciones](capitulo-06-soluciones.html) · [Notas históricas](capitulo-06-notas.html)

Se emplean exclusivamente las construcciones de C00–C06; los teoremas de integral ya demostrados en C05 y el Teorema Fundamental de C06 se invocan con sus condiciones de continuidad, integrabilidad, orientación y dominio. El identificador `EDC-C06-SOL-nnn` corresponde exactamente al problema `EDC-C06-EXR-nnn`.

## A. Interpretación y control de hipótesis

### Solución 6.1 (`EDC-C06-SOL-001`)

La primera parte construye la acumulación $F(x)=\int_a^x f(t)\,dt$ de una función continua $f:[a,b]\to\mathbb R$. La integrabilidad de continuas y de sus restricciones, demostrada en C05, asegura cada valor de $F$. Su incremento entre $x$ y $x+h$ es la integral sobre ese tramo, por aditividad. El orden coloca el cociente incremental entre las alturas locales de $f$, y la continuidad las acerca a $f(x)$ cuando la anchura tiende a cero. Así se obtiene $F'=f$ en el interior, con versiones relativas en los extremos.

La segunda parte parte de una primitiva $G$: continua en $[a,b]$, derivable en $(a,b)$ y con $G'=f$ allí. Afirma que $\int_a^b f=G(b)-G(a)$. La primera parte proporciona otra primitiva, $F$, y el valor medio de C03 demuestra que $G-F$ es constante. Esa constante desaparece al restar los valores en los extremos. La construcción de la integral precede a ambas afirmaciones; la primera identifica una derivada y la segunda permite evaluar un valor integral ya definido.

### Solución 6.2 (`EDC-C06-SOL-002`)

La función $f(t)=t^2$ es continua en $[0,2]$. El Teorema 6.2 da $F'_+(0)=f(0)=0$ y $F'_-(2)=f(2)=4$. En ambos casos la razón de cambio usa incrementos para los cuales el argumento sigue perteneciendo a $[0,2]$. Como $F$ no está definida para $x<0$ ni $x>2$ en el enunciado, carece de sentido exigir en esos extremos el cociente incremental bilateral propio de un punto interior de dominio.

### Solución 6.3 (`EDC-C06-SOL-003`)

Fijamos $a\le x<y\le b$. Por aditividad, $F(y)-F(x)=\int_x^y f(t)\,dt$. La restricción es integrable y no negativa, así que el orden de C05 compara su integral con la de la función cero. Resulta $F(y)\ge F(x)$ para cualquier par, que demuestra monotonía no decreciente sin derivar $F$.

Si $f$ es además continua y positiva en cada punto, el teorema de extremos de C00 proporciona un mínimo en el tramo cerrado $[x,y]$. Ese mínimo $m_{x,y}$ es un valor de la función y, por positividad, es estrictamente mayor que cero. La comparación con esa constante da

$$
F(y)-F(x)=\int_x^y f(t)\,dt\ge m_{x,y}(y-x)>0.
$$

La longitud $y-x$ también es positiva. Por tanto cada par ordenado produce una diferencia estricta y $F$ es estrictamente creciente. La mera condición $f\ge0$ permitiría, por ejemplo, $f\equiv0$ y una acumulación constante.

### Solución 6.4 (`EDC-C06-SOL-004`)

Una primitiva de $v(t)=3t^2$ es $s(t)=t^3$; por la segunda parte,

$$
\int_0^2 3t^2\,dt=[t^3]_0^2=8\ \mathrm{m}.
$$

Si $t$ tiene unidad segundo y $v$ metro por segundo, el coeficiente de $t^2$ debe tener unidades $(\mathrm{m}/\mathrm{s})/\mathrm{s}^2=\mathrm{m}/\mathrm{s}^3$. El símbolo numérico $3$ representa aquí un coeficiente dimensional, no una cantidad pura. Como $v\ge0$ durante el intervalo, desplazamiento y distancia recorrida coinciden en este modelo.

### Solución 6.5 (`EDC-C06-SOL-005`)

Por aditividad y orientación (C05), para todo $x\in[a,b]$,

$$
F_a(x)=\int_a^c f(t)\,dt+\int_c^x f(t)\,dt
=\left(\int_a^c f(t)\,dt\right)+F_c(x).
$$

La diferencia es la constante $\int_a^c f$, independiente de $x$. Las letras $t,u$ nombran el argumento de integración dentro de una suma o integral definida; sustituir una por otra no cambia la función integranda evaluada ni los extremos. En cambio, cambiar el **extremo** de integración sí altera la acumulación.

## B. Acumulaciones construidas desde la integral

### Solución 6.6 (`EDC-C06-SOL-006`)

Como $G(x)=x^3/3$ es una primitiva de $t^2$ por la regla de potencias, la segunda parte da

$$
F(x)=\int_0^x t^2\,dt=\frac{x^3}{3}-\frac{0^3}{3}=\frac{x^3}{3}.
$$

La derivada interior es $F'(x)=x^2$, de acuerdo con la primera parte, y $F(0)=0$. La igualdad en los extremos se interpreta por la continuidad de la expresión polinómica.

### Solución 6.7 (`EDC-C06-SOL-007`)

Tomamos $G(t)=t^2/2-3t$. Entonces

$$
F(x)=G(x)-G(1)=\frac{x^2}{2}-3x+\frac52.
$$

Su derivada es $F'(x)=x-3$. Por el criterio de monotonía de C03, $F$ decrece en $[-1,3]$ y crece en $[3,4]$; la acumulación no es necesariamente creciente porque el integrando puede ser negativo. Se obtiene $F(1)=0$ y $F(4)=8-12+5/2=-3/2$. El mínimo está en $x=3$, donde $F(3)=-2$.

### Solución 6.8 (`EDC-C06-SOL-008`)

El módulo tiene una expresión distinta a cada lado del origen. Para $x\in[-1,0]$, todo el tramo de integración está donde $|t|=-t$, y la segunda parte, aplicada a esa función continua, da

$$
F(x)=\int_{-1}^x(-t)\,dt=\frac{1-x^2}{2}.
$$

Si $x\in[0,2]$, cortamos en cero por aditividad. Conservamos la acumulación hasta el corte y añadimos el tramo donde $|t|=t$:

$$
F(x)=\int_{-1}^0(-t)\,dt+\int_0^x t\,dt
=\frac12+\frac{x^2}{2}.
$$

Las ramas valen $1/2$ en el corte. Para comprobar derivabilidad allí usamos ese valor en el cociente: si $h<0$, $[F(h)-F(0)]/h=-h/2$; si $h>0$, el cociente vale $h/2$. Ambos tienden a cero, de modo que $F'(0)=0=|0|$, tal como garantiza la continuidad del integrando. Finalmente $F(2)=1/2+4/2=5/2$.

### Solución 6.9 (`EDC-C06-SOL-009`)

La función $t\mapsto1/(1+t^2)$ es continua en $[0,1]$; como $(\arctan t)'=1/(1+t^2)$ por C02,

$$
F(x)=\arctan x-\arctan0=\arctan x.
$$

La primera parte da $F'(x)=1/(1+x^2)>0$ en el interior, y la continuidad con el criterio de C03 asegura que $F$ es estrictamente creciente. Además $F(1)=\arctan1=\pi/4$.

### Solución 6.10 (`EDC-C06-SOL-010`)

La función $e^{-t^2}$ es continua y estrictamente positiva en $[0,1]$, pues es una composición de funciones continuas ya construidas en C02. Por el Teorema 6.2,

$$
F'(x)=e^{-x^2}\quad(0<x<1).
$$

La positividad implica crecimiento estricto. Puesto que $0<e^{-t^2}\le1$ cuando $t\in[0,1]$, la monotonía de la integral proporciona, para $x\ge0$,

$$
0\le F(x)=\int_0^x e^{-t^2}\,dt\le\int_0^x1\,dt=x.
$$

No hemos necesitado expresar $F$ mediante un repertorio cerrado de funciones elementales.

### Solución 6.11 (`EDC-C06-SOL-011`)

La función $s$ es monótona y acotada, por lo que es integrable. Para $x<0$ vale cero en todo el tramo $[-1,x]$. En $x=0$ puede tomar el valor uno en el extremo, pero el Lema 5.3 garantiza que una contribución concentrada en un solo punto tiene integral cero. Para $x>0$, la aditividad separa ese tramo de integral nula y la función constante uno en $[0,x]$. Obtenemos

$$
S(x)=\begin{cases}0,&-1\le x\le0,\\x,&0\le x\le1.\end{cases}
$$

Como $S(0)=0$, su cociente incremental es cero para $h<0$ y uno para $h>0$. Por tanto $S'_-(0)=0$ y $S'_+(0)=1$: el límite bilateral no existe. Las dos ramas sí se unen continuamente y $S(1)=1$. El salto del integrando conserva continuidad de la acumulación, pero hace que las franjas de cada lado produzcan pendientes diferentes.

## C. Evaluación de integrales definidas

### Solución 6.12 (`EDC-C06-SOL-012`)

Una primitiva válida en toda la recta es $G(t)=t^3-t^2+t$, porque $G'=3t^2-2t+1$. Por tanto,

$$
\int_{-1}^2(3t^2-2t+1)\,dt=G(2)-G(-1)
=(8-4+2)-(-1-1-1)=6-(-3)=9.
$$

### Solución 6.13 (`EDC-C06-SOL-013`)

Como $(-\cos t)'=\sin t$ para todo real,

$$
\int_0^\pi\sin t\,dt=(-\cos\pi)-(-\cos0)=1+1=2.
$$

En $[0,\pi]$ el seno es no negativo; no hay cancelación entre aportes positivos y negativos y el valor coincide con el área ordinaria bajo la gráfica.

### Solución 6.14 (`EDC-C06-SOL-014`)

Todo punto de $[1,e]$ es estrictamente positivo. Por ello $\ln t$ está definida y es una primitiva de $1/t$ sobre un intervalo abierto que contiene $[1,e]$. Entonces

$$
\int_1^e\frac{dt}{t}=\ln e-\ln1=1-0=1.
$$

### Solución 6.15 (`EDC-C06-SOL-015`)

La cadena de C02 da

$$
\frac{d}{dt}\left(\frac12e^{2t}\right)=\frac12\,e^{2t}\cdot2=e^{2t}.
$$

El integrando es continuo en $[0,1]$, por lo que

$$
\int_0^1 e^{2t}\,dt=\left[\frac12e^{2t}\right]_0^1=\frac{e^2-1}{2}.
$$

### Solución 6.16 (`EDC-C06-SOL-016`)

Para $0\le t\le\pi/4$ se cumple $\cos t>0$. Por C02, $(\tan t)'=1/\cos^2t$ sobre ese intervalo. La fórmula de evaluación produce

$$
\int_0^{\pi/4}\frac{dt}{\cos^2t}=\tan(\pi/4)-\tan0=1.
$$

### Solución 6.17 (`EDC-C06-SOL-017`)

Por la regla de potencias, $G(t)=t^4/4$ es una primitiva de $t^3$. El integrando es continuo en todo el intervalo y la segunda parte da

$$
\int_{-2}^{2}t^3\,dt=\frac{2^4}{4}-\frac{(-2)^4}{4}=0.
$$

Para probarlo por simetría, tomamos una partición $-2=t_0<\cdots<t_n=0$ de la mitad izquierda, con cualquier etiqueta en cada pieza. Reflejamos sus cortes y los ordenamos desde cero hasta dos. La pieza $[t_{i-1},t_i]$ se convierte en $[-t_i,-t_{i-1}]$ con la misma anchura; si su etiqueta era $\xi_i$, la reflejada es $-\xi_i$. La imparidad da $(-\xi_i)^3=-\xi_i^3$, por lo que las dos sumas son opuestas.

Al tomar particiones de finura tendente a cero, las reflejadas tienen la misma finura. La continuidad asegura integrabilidad en ambas mitades y el Teorema 5.3 identifica sus límites. Así $\int_{-2}^0t^3\,dt=-\int_0^2t^3\,dt$. La aditividad reúne ambas contribuciones y da cero. La reflexión se efectuó en sumas finitas, sin usar una regla general de sustitución.

### Solución 6.18 (`EDC-C06-SOL-018`)

Definamos $G(t)=t|t|/2$, esto es, $G(t)=t^2/2$ para $t\ge0$ y $G(t)=-t^2/2$ para $t\le0$. Fuera del origen, la derivada de ambas ramas vale $|t|$. En $0$,

$$
\frac{G(h)-G(0)}h=\frac{|h|}{2}\longrightarrow0=|0|.
$$

Así, $G$ es derivable incluso en $0$ y es una primitiva de $|t|$. La segunda parte da

$$
\int_{-1}^1|t|\,dt=G(1)-G(-1)=\frac12-\left(-\frac12\right)=1.
$$

El hecho de que $|t|$ no sea derivable en $0$ no impide que sea un **integrando continuo** con primitiva.

### Solución 6.19 (`EDC-C06-SOL-019`)

Por convención de orientación,

$$
\int_2^0(2t+1)\,dt=-\int_0^2(2t+1)\,dt
=-[t^2+t]_0^2=-(4+2)=-6.
$$

El integrando es positivo sobre $[0,2]$; el signo negativo procede exclusivamente del orden invertido de los extremos.

## D. Extremos variables

### Solución 6.20 (`EDC-C06-SOL-020`)

Definimos $A(u)=\int_0^u e^{t^2}\,dt$ para $u\in[0,1]$. El integrando es continuo y la primera parte da $A'(u)=e^{u^2}$ en el interior. Como $H(x)=A(x^2)$ y $x^2\in[0,1)$ para $-1<x<1$, la Proposición 6.2 con extremo inferior constante proporciona

$$
H'(x)=e^{(x^2)^2}(2x)=2x e^{x^4}.
$$

En $x=0$ el argumento de $A$ toca el borde de su dominio. Podemos comprobar directamente la derivada: para $0\le t\le1$, $e^{t^2}\le e$, luego el orden de la integral da $|H(h)-H(0)|\le e h^2$. Al dividir por $|h|$ obtenemos una cota $e|h|$ que tiende a cero. Así $H'(0)=0$, en acuerdo con la fórmula. La estimación justifica el punto de borde sin extender artificialmente el dominio de $A$ ni buscar una primitiva elemental.

### Solución 6.21 (`EDC-C06-SOL-021`)

Para $-1<x<1$, tenemos $\sin x\in[-1,1]$ y $x^2+1\in[1,2]$. El integrando $f(t)=\ln(1+t^2)$ es continuo en el compacto $[-1,2]$, pues $1+t^2>0$. Aplicando la fórmula de extremos variables,

$$
K'(x)=2x\ln\!\left(1+(x^2+1)^2\right)
-\cos x\,\ln\!\left(1+\sin^2x\right).
$$

La primera contribución procede del extremo superior y la segunda se resta por el extremo inferior.

### Solución 6.22 (`EDC-C06-SOL-022`)

El integrando $t^2+1$ es continuo en $[-1,2]$; al derivar un extremo inferior variable con extremo superior constante obtenemos

$$
L'(x)=-(x^2+1),\qquad -1<x<2.
$$

La definición integral da $L(2)=\int_2^2(t^2+1)dt=0$, y la expresión explícita de una primitiva es $L(x)=\frac{14}{3}-(x^3/3+x)$, continua hasta $x=2$.

### Solución 6.23 (`EDC-C06-SOL-023`)

El integrando $f(t)=\cos(t^2)$ es continuo en $[-1,1]$ y $x^3\in(-1,1)$ para $x\in(-1,1)$. Aplicamos la primera parte a la acumulación $A(u)=\int_0^u f(t)dt$ y luego la cadena a $A(x^3)$:

$$
M'(x)=\cos((x^3)^2)\cdot3x^2=3x^2\cos(x^6).
$$

No se ha transformado el integrando dentro de la integral: sólo se ha derivado **la composición con su extremo**. Una regla general de sustitución para evaluar integrales será objeto de C07.

### Solución 6.24 (`EDC-C06-SOL-024`)

La aditividad de C05 asegura, para cada $x\in[-1,1]$,

$$
N(x)=\int_{-1}^1(t^2+1)\,dt.
$$

Por la segunda parte con $G(t)=t^3/3+t$,

$$
N(x)=G(1)-G(-1)=\left(\frac13+1\right)-\left(-\frac13-1\right)=\frac83.
$$

Es constante, luego $N'(x)=0$. Directamente desde la regla de extremos variables, su derivada es $(x^2+1)-(x^2+1)=0$.

## E. Diagnóstico de afirmaciones inválidas

### Solución 6.25 (`EDC-C06-SOL-025`)

Escribimos $r=1+h$, donde $h$ vale $-1$ en cero y se anula en el resto. Por el Lema 5.3, $h$ es integrable y su integral sobre cualquier subintervalo no degenerado es cero; en un intervalo degenerado la convención da también cero. La función constante uno es integrable, así que la linealidad asegura integrabilidad de $r$ y

$$
R(x)=\int_{-1}^x r(t)\,dt=\int_{-1}^x1\,dt=x+1.
$$

La acumulación es afín y $R'(0)=1$, mientras el valor aislado del integrando es $r(0)=0$. Para puntos no nulos cercanos a cero, $r(t)=1$, de modo que no converge a $r(0)$. Falla exactamente la continuidad del integrando en el punto donde se quiere aplicar la primera parte. La integral conserva la acumulación al cambiar una sola altura, y por eso su derivada no puede registrar esa modificación puntual.

### Solución 6.26 (`EDC-C06-SOL-026`)

La derivada $G'(x)=1/(2\sqrt{x})$ existe para $x\in(0,1)$, pero crece sin cota cuando $x\downarrow0$. No existe una extensión de esa fórmula que sea **acotada en $[0,1]$**, condición necesaria para la integral propia de Riemann–Darboux definida en C05. Por tanto la hipótesis «$f$ integrable» del Teorema 6.6 no se cumple. Es verdad que $G(1)-G(0)=1$, pero no se puede reinterpretar ese número como $\int_0^1 G'$ **en el sentido propio definido aquí**. Haría falta construir una integral impropia mediante un límite adicional, teoría que este capítulo no ha desarrollado.

### Solución 6.27 (`EDC-C06-SOL-027`)

La función $f(x)=x$ es continua y su integral en $[0,1]$ vale $1/2$, por C05 o por la primitiva continua $x^2/2$. En cambio, la función propuesta tiene $G(0)=100$, y

$$
G(1)-G(0)=\frac12-100\ne\frac12.
$$

Aunque $G'=f$ en el interior, $G$ no cumple la definición de primitiva sobre el intervalo cerrado: su límite derecho en cero es cero y difiere de $G(0)$. La continuidad terminal es una hipótesis del Teorema 6.5. También aparece en sus pruebas: sin ella no podemos aplicar el valor medio en una pieza que empiece en cero, ni concluir que la diferencia de primitivas mantiene su constante en el borde. El ejemplo cambia el valor terminal sin cambiar ninguna derivada interior y muestra por qué esa continuidad es necesaria para la fórmula declarada.

## F. Pruebas y síntesis

### Solución 6.28 (`EDC-C06-SOL-028`)

La diferencia $K=G-H$ es continua en $[a,b]$ y derivable en $(a,b)$, con $K'=0$. Para cada $a\le u<v\le b$, el teorema del valor medio da $c\in(u,v)$ tal que

$$
K(v)-K(u)=K'(c)(v-u)=0.
$$

Por tanto $K$ toma un valor constante en todo el intervalo. Sobre un dominio disconexo, por ejemplo $(0,1)\cup(2,3)$, podemos tomar $H\equiv0$, y $G(x)=0$ en el primer componente y $G(x)=1$ en el segundo: las derivadas coinciden, pero $G-H$ no es una sola constante en todo el dominio. La conexión por un intervalo es esencial.

### Solución 6.29 (`EDC-C06-SOL-029`)

Elegimos una partición $a=x_0<\cdots<x_n=b$. En cada pieza, $G$ es continua hasta los extremos y derivable en el interior, incluso si la pieza toca $a$ o $b$. El teorema del valor medio proporciona una etiqueta estrictamente interior $\xi_i$ con

$$
G(x_i)-G(x_{i-1})=G'(\xi_i)\Delta_i=f(\xi_i)\Delta_i.
$$

La igualdad con $f$ es válida en esas etiquetas porque todas pertenecen a $(a,b)$. Al sumar, cada valor de $G$ en un corte interior se cancela con el de la pieza vecina:

$$
G(b)-G(a)=\sum_{i=1}^n f(\xi_i)\Delta_i.
$$

Hasta aquí el valor medio ha producido una suma etiquetada exacta, para cualquier partición. Para identificarla con la integral usamos ahora la integrabilidad de $f$. Dado $\varepsilon>0$, el Teorema 5.3 da un umbral que controla todas las sumas de finura menor que él. Elegimos una partición así y sus etiquetas del valor medio: la suma vale $G(b)-G(a)$ y difiere de la integral en menos que $\varepsilon$. Esos dos números son fijos y quedan separados por menos que cualquier tolerancia, luego coinciden.

El valor medio elige las alturas y la equivalencia Riemann–Darboux determina el valor límite. No se requiere continuidad de $f$, pues su integrabilidad es hipótesis, ni se utiliza la primera parte del Teorema Fundamental. Los valores de $f$ en los extremos tampoco intervienen en la elección de etiquetas interiores.

### Solución 6.30 (`EDC-C06-SOL-030`)

Sea $V(s;P)=\sum_{i=1}^n|s(t_i)-s(t_{i-1})|$. Usamos la prolongación continua de $s'$ a $[a,b]$ que exige el enunciado; sus valores en los bordes no necesitan ser derivadas bilaterales de $s$. La función $|s'|$ es continua e integrable. Para comparar una variación finita con su integral, la segunda parte aplicada a $s$ en cada pieza da

$$
|s(t_i)-s(t_{i-1})|=\left|\int_{t_{i-1}}^{t_i}s'(t)\,dt\right|
\le\int_{t_{i-1}}^{t_i}|s'(t)|\,dt.
$$

La desigualdad triangular integral elimina las cancelaciones dentro de cada pieza. Sumamos por aditividad:

$$
V(s;P)\le\int_a^b|s'(t)|\,dt
$$

para cualquier partición. El conjunto de esas variaciones es no vacío, no negativo y acotado superiormente por una integral finita. La completitud de C00 proporciona su supremo $V(s)$, y la misma cota da $V(s)\le\int_a^b|s'|$.

Falta mostrar que las variaciones finitas se acercan a esa cota tanto como queramos. Elegimos particiones uniformes $P_n$ con finura $(b-a)/n\to0$. En cada pieza, el valor medio proporciona un punto interior $\xi_i$ tal que

$$
|s(t_i)-s(t_{i-1})|=|s'(\xi_i)|\Delta_i.
$$

Por tanto $V(s;P_n)$ es una suma etiquetada de $|s'|$. La continuidad hace integrable esta función, y el Teorema 5.3 obliga a que esas sumas converjan a su integral, aunque las etiquetas cambien con $n$. Cada suma está acotada por $V(s)$; el límite también lo está. Si la integral fuera mayor, una tolerancia menor que su separación respecto del supremo haría que alguna suma superase $V(s)$, contradicción. Obtenemos $\int_a^b|s'|\le V(s)$ y, junto con la primera cota,

$$
\boxed{V(s)=\int_a^b|s'(t)|\,dt.}
$$

Para una posición unidimensional $s(t)$, cada diferencia absoluta mide el desplazamiento entre dos cortes sin conservar su signo. Una partición puede ocultar cambios de sentido dentro de sus piezas; al refinarla, la desigualdad triangular asegura que la suma no disminuye. El supremo recoge la variación total y representa la distancia recorrida en este modelo de regularidad $C^1$. El desplazamiento $s(b)-s(a)=\int_a^b s'$ conserva las cancelaciones entre sentidos opuestos. La prueba da la interpretación de ambas integrales bajo las hipótesis declaradas.

---

**Control de cobertura:** `EDC-C06-SOL-001--030` corresponde uno a uno a `EDC-C06-EXR-001--030`. Los desarrollos comprueban dominios, orientación, límites del intervalo e hipótesis de continuidad/integrabilidad, sin usar sustitución o integración por partes de C07.
