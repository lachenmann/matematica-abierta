---
title: Capítulo 6 — Soluciones desarrolladas
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
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
    note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra
      independiente.'
source-id: EDC-C06-SOLUCIONES
source-sha256: 9f949f1581247bb84a9bbb2abd61ea695764b6b935dd73b74644a58a66a615e0
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-06.md) · [Ejercicios](capitulo-06-ejercicios.md) · [Soluciones](capitulo-06-soluciones.md) · [Notas históricas](capitulo-06-notas.md)

Se emplean exclusivamente las construcciones de C00–C06; los teoremas de integral ya demostrados en C05 y el Teorema Fundamental de C06 se invocan con sus condiciones de continuidad, integrabilidad, orientación y dominio. El identificador `EDC-C06-SOL-nnn` corresponde exactamente al problema `EDC-C06-EXR-nnn`.

## A. Interpretación y control de hipótesis

### Solución 6.1 (`EDC-C06-SOL-001`)

La **primera parte** supone $f:[a,b]\to\mathbb R$ continua y construye $F(x)=\int_a^x f(t)\,dt$. C05 garantiza que las subintegrales existen, y C05 también aporta orden y aditividad. La continuidad de $f$ permite demostrar mediante el encaje de los incrementos que $F'(x)=f(x)$ para cada $x\in(a,b)$, con versiones laterales en los extremos. La **segunda parte** supone, además, una función $G$ continua en $[a,b]$, derivable en $(a,b)$, con $G'=f$ allí; afirma $\int_a^b f=G(b)-G(a)$. Se deduce de la primera parte y del valor medio de C03, porque $G-F$ tiene derivada nula. Así, la existencia de la integral no procede de la fórmula con primitiva, sino de la construcción autónoma de C05.

### Solución 6.2 (`EDC-C06-SOL-002`)

La función $f(t)=t^2$ es continua en $[0,2]$. El Teorema 6.2 da $F'_+(0)=f(0)=0$ y $F'_-(2)=f(2)=4$. En ambos casos la razón de cambio usa incrementos para los cuales el argumento sigue perteneciendo a $[0,2]$. Como $F$ no está definida para $x<0$ ni $x>2$ en el enunciado, carece de sentido exigir en esos extremos el cociente incremental bilateral propio de un punto interior de dominio.

### Solución 6.3 (`EDC-C06-SOL-003`)

Para $a\le x<y\le b$ la aditividad proporciona $F(y)-F(x)=\int_x^y f(t)\,dt\ge0$ porque $f\ge0$ y el orden de C05 compara con la función cero. Si $f$ es continua y positiva en **todo** $[a,b]$, entonces sobre cualquier $[x,y]$ alcanza un mínimo $m_{x,y}>0$ (C00). De ahí

$$
F(y)-F(x)=\int_x^y f(t)\,dt\ge m_{x,y}(y-x)>0.
$$

Queda probada la estricta monotonía. Si se conociera únicamente $f\ge0$, sin positividad estricta, $f\equiv0$ muestra que la conclusión estricta no es válida.

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

En $[-1,0]$, $|t|=-t$, de modo que

$$
F(x)=\int_{-1}^x(-t)\,dt=\frac{1-x^2}{2}.
$$

Para $x\in[0,2]$, por aditividad,

$$
F(x)=\int_{-1}^0(-t)\,dt+\int_0^x t\,dt
=\frac12+\frac{x^2}{2}.
$$

Las ramas coinciden en $x=0$, donde ambas valen $1/2$. Sus derivadas laterales son $-0=0$ y $+0=0$; por el criterio de C01, $F'(0)=0=|0|$. Finalmente $F(2)=1/2+4/2=5/2$.

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

La función $s$ es monótona, acotada y por C05 integrable, incluso si la definimos con $s(0)=1$. Para $x\le0$, la integral de $s$ vale cero porque $s=0$ salvo, a lo sumo, el punto $0$, cuya modificación no afecta la integral. Para $x\ge0$, queda un tramo de longitud $x$ en el que $s=1$. Así,

$$
S(x)=\begin{cases}0,&-1\le x\le0,\\x,&0\le x\le1.\end{cases}
$$

Las derivadas laterales en $0$ son $S'_-(0)=0$ y $S'_+(0)=1$, por lo que no existe derivada bilateral. Sin embargo, $S$ es continua y $S(1)=1$. La integrabilidad del integrando **no** es la continuidad necesaria para la identidad puntual $S'(0)=s(0)$.

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

La función $G(t)=t^4/4$ es una primitiva de $t^3$ en toda la recta. Por tanto,

$$
\int_{-2}^{2}t^3\,dt=\frac{2^4}{4}-\frac{(-2)^4}{4}=0.
$$

La prueba por simetría no requiere anticipar una fórmula general de cambio de variable. Reflejamos las particiones de $[-2,0]$ en particiones de $[0,2]$ y las muestras $\xi$ en $-\xi$. Como la función es impar, las sumas etiquetadas reflejadas son las opuestas. El criterio de convergencia de sumas de Riemann de C05 implica $\int_{-2}^0t^3\,dt=-\int_0^2t^3\,dt$. Su suma por aditividad vale cero.

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

Sea $A(u)=\int_0^u e^{t^2}\,dt$ para $0\le u\le1$. Por la primera parte, $A'(u)=e^{u^2}$ en el interior y la extensión lateral sirve en el extremo $u=0$. Como $x^2$ toma valores en $[0,1]$, la Proposición 6.2 con límite inferior constante produce

$$
H'(x)=e^{(x^2)^2}(2x)=2x e^{x^4}.
$$

La fórmula vale también en $x=0$ porque allí el extremo interior $x^2$ tiene derivada cero. No se ha hallado ni requerido una primitiva elemental de $e^{t^2}$.

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

Sea $h=r-1$. La función $h$ vale $-1$ sólo en $t=0$ y cero en el resto; el Lema 5.3 muestra que es integrable y su integral sobre cualquier subintervalo es cero. Por linealidad,

$$
R(x)=\int_{-1}^x r(t)\,dt=\int_{-1}^x1\,dt=x+1.
$$

Por tanto $R'(0)=1$ mientras $r(0)=0$. La primera parte requiere **continuidad del integrando en el punto** para garantizar igualdad puntual; $r$ no es continua en $0$. Su integrabilidad sola basta para la continuidad de $R$ pero no para la igualdad $R'(0)=r(0)$.

### Solución 6.26 (`EDC-C06-SOL-026`)

La derivada $G'(x)=1/(2\sqrt{x})$ existe para $x\in(0,1)$, pero crece sin cota cuando $x\downarrow0$. No existe una extensión de esa fórmula que sea **acotada en $[0,1]$**, condición necesaria para la integral propia de Riemann–Darboux definida en C05. Por tanto la hipótesis «$f$ integrable» del Teorema 6.6 no se cumple. Es verdad que $G(1)-G(0)=1$, pero no se puede reinterpretar ese número como $\int_0^1 G'$ **en el sentido propio definido aquí**. Haría falta construir una integral impropia mediante un límite adicional, teoría que este capítulo no ha desarrollado.

### Solución 6.27 (`EDC-C06-SOL-027`)

La función $f(x)=x$ es continua e integrable en $[0,1]$, con $\int_0^1x\,dx=1/2$. En cambio,

$$
G(1)-G(0)=\frac12-100\ne\frac12.
$$

La igualdad $G'(x)=x$ para $0<x<1$ no basta para aplicar el Teorema 6.5, porque $G$ **no es continua en $x=0$**: su límite desde la derecha vale $0$, mientras $G(0)=100$. Esta hipótesis impide modificar arbitrariamente los valores terminales de una primitiva.

## F. Pruebas y síntesis

### Solución 6.28 (`EDC-C06-SOL-028`)

La diferencia $K=G-H$ es continua en $[a,b]$ y derivable en $(a,b)$, con $K'=0$. Para cada $a\le u<v\le b$, el teorema del valor medio da $c\in(u,v)$ tal que

$$
K(v)-K(u)=K'(c)(v-u)=0.
$$

Por tanto $K$ toma un valor constante en todo el intervalo. Sobre un dominio disconexo, por ejemplo $(0,1)\cup(2,3)$, podemos tomar $H\equiv0$, y $G(x)=0$ en el primer componente y $G(x)=1$ en el segundo: las derivadas coinciden, pero $G-H$ no es una sola constante en todo el dominio. La conexión por un intervalo es esencial.

### Solución 6.29 (`EDC-C06-SOL-029`)

Tomemos una partición cualquiera $a=x_0<\cdots<x_n=b$. La función $G$ satisface las hipótesis del teorema del valor medio en cada $[x_{i-1},x_i]$, incluso cuando esos extremos coinciden con $a$ o $b$, porque sólo se exige derivabilidad interior. Por tanto existen $\xi_i\in(x_{i-1},x_i)$ con

$$
G(x_i)-G(x_{i-1})=G'(\xi_i)\Delta_i=f(\xi_i)\Delta_i.
$$

Sumando, los términos del lado izquierdo telescopan:

$$
G(b)-G(a)=\sum_{i=1}^n f(\xi_i)\Delta_i.
$$

El **valor medio** produjo los puntos $\xi_i$ que realizan cada cociente de incrementos; la **equivalencia Riemann–Darboux** de C05 asegura que, porque $f$ es integrable, estas sumas convergen a $\int_a^b f$ siempre que la finura de las particiones tienda a cero, independientemente de las muestras. Como todas las sumas de la fórmula valen ya $G(b)-G(a)$, ese número debe ser la integral. No se ha invocado la primera parte del Teorema Fundamental ni se ha exigido continuidad de $f$.

### Solución 6.30 (`EDC-C06-SOL-030`)

Sea $V(s;P)=\sum_{i=1}^n|s(t_i)-s(t_{i-1})|$ para una partición $P$. Como $s'$ es continua, $|s'|$ es integrable por C05. La segunda parte del Teorema Fundamental aplicada en cada subintervalo a la primitiva $s$ da

$$
|s(t_i)-s(t_{i-1})|=\left|\int_{t_{i-1}}^{t_i}s'(t)\,dt\right|
\le\int_{t_{i-1}}^{t_i}|s'(t)|\,dt.
$$

Sumando por aditividad,

$$
V(s;P)\le\int_a^b|s'(t)|\,dt
$$

para **toda** partición. Luego el supremo $V(s)=\sup_PV(s;P)$ existe y es a lo sumo esa integral.

Para la desigualdad opuesta, escojamos las particiones uniformes $P_n$ con finura $(b-a)/n\to0$. El teorema del valor medio, en cada $[t_{i-1},t_i]$, proporciona un $\xi_i$ con

$$
|s(t_i)-s(t_{i-1})|=|s'(\xi_i)|\Delta_i.
$$

Así, $V(s;P_n)$ es una suma de Riemann de la función continua $|s'|$. Por el Teorema 5.3, sus valores convergen a $\int_a^b|s'|$. Como $V(s;P_n)\le V(s)$ para todo $n$, obtenemos $\int_a^b|s'|\le V(s)$. Las dos cotas prueban

$$
\boxed{V(s)=\int_a^b|s'(t)|\,dt.}
$$

En una trayectoria unidimensional con posición $s(t)$, la variación total representa la **distancia recorrida**, mientras $\int_a^b s'(t)dt=s(b)-s(a)$ es el desplazamiento neto. La igualdad ha sido demostrada aquí, bajo regularidad $C^1$, y no se extrapola a movimientos sin esas hipótesis.

---

**Control de cobertura:** `EDC-C06-SOL-001--030` corresponde uno a uno a `EDC-C06-EXR-001--030`. Los desarrollos comprueban dominios, orientación, límites del intervalo e hipótesis de continuidad/integrabilidad, sin usar sustitución o integración por partes de C07.
