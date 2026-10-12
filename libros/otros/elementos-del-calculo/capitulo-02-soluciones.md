---
title: Capítulo 2 — Soluciones desarrolladas
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
source-id: EDC-C02-SOLUCIONES
source-sha256: ea2091e9334b9c4e5aac0611c44c0d87b76169b21d218691f2a71134c168eda4
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-02.md) · [Ejercicios](capitulo-02-ejercicios.md) · [Soluciones](capitulo-02-soluciones.md) · [Notas históricas](capitulo-02-notas.md)

Estas soluciones son elaboraciones matemáticas propias. La referencia `EDC-C02-SOL-nnn` corresponde exactamente al enunciado `EDC-C02-EXR-nnn`; todos los argumentos se apoyan en C00–C02. Cada hipótesis de dominio se conserva a lo largo del cálculo.

## A. Reconocimiento y lenguaje

### Solución 2.1 (`EDC-C02-SOL-001`)

La función $f(x)=(x^2+1)/(x-1)$ está definida para $x\in\mathbb R\setminus\{1\}$. Numerador y denominador son polinomios derivables y el denominador no se anula en ese conjunto; el Teorema 2.1 garantiza derivabilidad en cada punto del dominio. Como

$$
f'(x)=\frac{2x(x-1)-(x^2+1)}{(x-1)^2}
=\frac{x^2-2x-1}{(x-1)^2},
$$

obtenemos $f'(0)=-1$. No existe $f'(1)$: ni siquiera existe $f(1)$.

### Solución 2.2 (`EDC-C02-SOL-002`)

Son válidas $(f+g)'=f'+g'$ y $(cf)'=cf'$ cuando $f,g$ sean derivables en el punto y $c$ sea constante. Para $f(x)=g(x)=x$, la derivada del producto es $(x^2)'=2x$, mientras $f'g'=1$; falla la segunda fórmula. Para $f(x)=x$ y $g(x)=x+1$, con $x\ne-1$, la derivada de $f/g$ es $1/(x+1)^2$, mientras $f'/g'=1$. Por ejemplo, en $x=1$ son $1/4$ y $1$. Además $f'/g'$ podría carecer de sentido aunque el cociente original fuera derivable.

### Solución 2.3 (`EDC-C02-SOL-003`)

Por linealidad y la fórmula de potencias, $p'(a)=3a^2-2$. Para el control directo en $a=1$,

$$
\frac{p(1+h)-p(1)}h
=\frac{(1+h)^3-2(1+h)+5-(1-2+5)}h
=1+3h+h^2\longrightarrow1.
$$

Coincide con $3(1)^2-2=1$.

### Solución 2.4 (`EDC-C02-SOL-004`)

Continuidad y monotonía estricta en el intervalo hacen que exista una inversa sobre $f(I)$, y garantizan su continuidad. La condición puntual $f'(a)\ne0$ hace que sea legítimo tomar el recíproco del cociente incremental al pasar al límite; sin ella no se obtiene el valor finito del teorema. Para $f(x)=x^3$, la inversa es $F(y)=\sqrt[3]y$; en $0$, $f'(0)=0$, mientras

$$
\frac{F(h)-F(0)}h=|h|^{-2/3}\longrightarrow+\infty.
$$

Así, $F'(0)$ no existe como derivada real finita, aunque la función inversa sí existe y es continua.

## B. Derivación algebraica y composición

### Solución 2.5 (`EDC-C02-SOL-005`)

La regla del producto da

$$
p'(x)=(6x-2)(x^3+4)+(3x^2-2x+1)(3x^2).
$$

Expandiendo la función original obtenemos $p(x)=3x^5-2x^4+x^3+12x^2-8x+4$, de donde

$$
p'(x)=15x^4-8x^3+3x^2+24x-8.
$$

Las expresiones coinciden al desarrollar la primera; las dos rutas comprueban la misma regla sin presuponerla en la expansión.

### Solución 2.6 (`EDC-C02-SOL-006`)

El dominio es $\mathbb R\setminus\{2\}$. Por el cociente,

$$
q'(x)=\frac{2x(x-2)-(x^2+1)}{(x-2)^2}
=\frac{x^2-4x-1}{(x-2)^2}.
$$

En $x=3$ obtenemos $q'(3)=9-12-1=-4$.

### Solución 2.7 (`EDC-C02-SOL-007`)

Tomamos $g(x)=x^2+1$ y $f(t)=t^5$. La regla de la cadena produce

$$
u'(x)=f'(g(x))g'(x)=5(x^2+1)^4(2x)=10x(x^2+1)^4.
$$

El dominio es todo $\mathbb R$.

### Solución 2.8 (`EDC-C02-SOL-008`)

La función interior $1+3x^2$ es estrictamente positiva para todo $x\in\mathbb R$. La función raíz es derivable sobre $(0,\infty)$, por el teorema de la inversa; por cadena,

$$
v'(x)=\frac{6x}{2\sqrt{1+3x^2}}
=\frac{3x}{\sqrt{1+3x^2}},\qquad x\in\mathbb R.
$$

Nunca se anula su denominador.

### Solución 2.9 (`EDC-C02-SOL-009`)

Si $x\ne0$, $x^{-3}=1/x^3$, y la regla del cociente da

$$
w'(x)=-\frac{3x^2}{x^6}=-3x^{-4}.
$$

En $x=0$ no hay valor de $w$ y, por tanto, tampoco cociente incremental de $w$.

### Solución 2.10 (`EDC-C02-SOL-010`)

Como $1+x^2>0$ para todo real,

$$
r'(x)=\frac{e^x(1+x^2)-e^x(2x)}{(1+x^2)^2}
=\frac{e^x(x-1)^2}{(1+x^2)^2}.
$$

La expresión es no negativa en toda la recta; sin utilizar todavía el valor medio, esta observación no es en sí una demostración de monotonía global.

## C. Exponenciales, logaritmos y trigonometría

### Solución 2.11 (`EDC-C02-SOL-011`)

Para $f$, el exponente es un polinomio, luego

$$
f'(x)=e^{2x-x^2}(2-2x),\qquad x\in\mathbb R.
$$

Para $g$, $3+x^2>0$ para todo $x$, y la cadena con $(\ln u)'=1/u$ da

$$
g'(x)=\frac{2x}{3+x^2},\qquad x\in\mathbb R.
$$

### Solución 2.12 (`EDC-C02-SOL-012`)

Para $0<x<\pi$, $\sin x>0$; por ello $\ln(\sin x)$ es una función real derivable. La cadena da

$$
h'(x)=\frac{\cos x}{\sin x}=\cot x.
$$

En $0$ y $\pi$ el seno es cero y el logaritmo no está definido; fuera del intervalo el signo del seno requiere revisar el dominio.

### Solución 2.13 (`EDC-C02-SOL-013`)

Las fórmulas son

$$
\frac d{dx}2^x=2^x\ln2,\qquad
\frac d{dx}\log_2x=\frac1{x\ln2},\quad x>0.
$$

La función $\log_2$ es **inversa funcional** de $2^x$: $2^{\log_2x}=x$ para $x>0$. La recíproca numérica de $2^x$ es en cambio $2^{-x}$, definida en todo $\mathbb R$; no debe confundirse la inversión de una correspondencia con la inversión de sus valores.

### Solución 2.14 (`EDC-C02-SOL-014`)

La derivada de $\arctan u$ es $1/(1+u^2)$ y la interior $u=3x$ tiene derivada $3$. Por tanto,

$$
a'(x)=\frac3{1+9x^2},\qquad x\in\mathbb R.
$$

### Solución 2.15 (`EDC-C02-SOL-015`)

Como $x^2\in[0,1]$ precisamente cuando $-1\le x\le1$, ése es el dominio real. En $-1<x<1$ se puede aplicar la cadena y

$$
b'(x)=\frac{2x}{\sqrt{1-x^4}}.
$$

En $x=\pm1$ la función existe pero el dominio no contiene un entorno bilateral, y el denominador de la fórmula se anula. No existe allí derivada bilateral según la definición de C01; cualquier discusión de derivadas laterales debe formularse expresamente.

### Solución 2.16 (`EDC-C02-SOL-016`)

La base $1+x^2$ es siempre positiva, de modo que

$$
k(x)=\exp\bigl(\sin x\,\ln(1+x^2)\bigr)
$$

está definida para todo real. Producto y cadena dan

$$
k'(x)=(1+x^2)^{\sin x}
\left[\cos x\,\ln(1+x^2)+\sin x\,\frac{2x}{1+x^2}\right].
$$

No hemos supuesto una regla informal para derivar una base y un exponente variables: la reducción a $E\circ(\sin\cdot\ln)$ la justifica.

## D. Diagnóstico de inferencias inválidas

### Solución 2.17 (`EDC-C02-SOL-017`)

Con $f(x)=x$, $g(x)=x^2$, el producto es $x^3$ y su derivada $3x^2$, mientras $f'(x)g'(x)=1\cdot2x=2x$. Son funciones diferentes. La igualdad correcta es $(fg)'=f'g+fg'$, que aquí da $x^2+2x^2=3x^2$.

### Solución 2.18 (`EDC-C02-SOL-018`)

La función $f(t)=|t|$ no tiene derivada en $t=0$, por diferencia entre los cocientes laterales. Sin embargo,

$$
(f\circ g)(x)=|x^2|=x^2
$$

es derivable en $x=0$, con derivada cero. El recíproco de la regla de la cadena no vale: la composición puede suavizar una singularidad porque la función interior sólo recorre una parte del dominio exterior.

### Solución 2.19 (`EDC-C02-SOL-019`)

Para $x\ne0$, $f'(x)=2x\sin(1/x)-\cos(1/x)$ y $f'(0)=0$ por $|f(h)/h|\le|h|$. Tomando

$$
x_n=\frac1{2\pi n},\qquad y_n=\frac1{(2n+1)\pi},
$$

obtenemos $f'(x_n)=-1$ y $f'(y_n)=1$. Ambas sucesiones tienden a cero; por el criterio secuencial de C00, $f'$ carece de límite en el origen y no es continua allí.

### Solución 2.20 (`EDC-C02-SOL-020`)

La función es continua en $0$ porque ambas expresiones tienden a $0=f(0)$. Para $h>0$,

$$
\frac{f(h)-f(0)}h=h\longrightarrow0;
$$

para $h<0$ el cociente vale $2$. Así $f'_+(0)=0$ y $f'_-(0)=2$. Como difieren, $f'(0)$ no existe, por el Teorema 1.4. Continuidad no implica derivabilidad.

## E. Demostraciones

### Solución 2.21 (`EDC-C02-SOL-021`)

La continuidad de $f$ en $a$ permite elegir $\delta>0$ tal que $|f(a+h)-f(a)|<|f(a)|/2$ cuando $|h|<\delta$; por ello $|f(a+h)|>|f(a)|/2>0$. Para $h\ne0$ suficientemente pequeño,

$$
\frac{1/f(a+h)-1/f(a)}h
=-\frac{f(a+h)-f(a)}h\frac1{f(a+h)f(a)}.
$$

El primer factor tiende a $f'(a)$ y el segundo a $1/f(a)^2$, de donde $(1/f)'(a)=-f'(a)/f(a)^2$.

### Solución 2.22 (`EDC-C02-SOL-022`)

Para $n=1$ la afirmación $(f^1)'=f'$ es inmediata. Supuesta $(f^n)'=nf^{n-1}f'$, usamos $f^{n+1}=f^nf$ y la regla del producto:

$$
(f^{n+1})'=nf^{n-1}f'\,f+f^n f'
=(n+1)f^nf'.
$$

La inducción vale punto por punto en $I$; no se requiere que $f$ sea positiva, pues son potencias enteras.

### Solución 2.23 (`EDC-C02-SOL-023`)

Si $g(x)>0$, la expresión es $\ln g(x)$ y su derivada vale $g'(x)/g(x)$ por cadena. Si $g(x)<0$, tenemos $\ln|g(x)|=\ln(-g(x))$, cuya derivada es $(-g'(x))/(-g(x))=g'(x)/g(x)$. Por continuidad y ausencia de ceros, el signo de $g$ no cambia en un entorno suficientemente pequeño de cada punto, así que las dos fórmulas locales prueban el resultado en todo $I$.

### Solución 2.24 (`EDC-C02-SOL-024`)

Al poner $y=-x$ en $E(x+y)=E(x)E(y)$, queda $E(0)=E(x)E(-x)=1$. Como $E(x)>0$, $E(-x)=1/E(x)$. Si $u<v$, entonces $E(v)=E(u)E(v-u)>E(u)$ porque $v-u>0$; por tanto, $E$ es estrictamente creciente, sin usar derivadas ni valor medio. De la serie para $x>0$ obtenemos $E(x)\ge1+x\to\infty$ al crecer $x$, y $E(-x)=1/E(x)\to0$. Por continuidad y valor intermedio, se alcanzan todos y sólo los valores positivos.

## F. Descubrimiento guiado

### Solución 2.25 (`EDC-C02-SOL-025`)

Para $x\ne0$ se tiene $\sqrt{x^2}=|x|$, y la cadena da

$$
F'(x)=\frac{2x}{2\sqrt{x^2}}=\frac{x}{|x|}
=\begin{cases}1,&x>0,\\-1,&x<0.\end{cases}
$$

En $0$, la función raíz exterior se evalúa en $0$, punto donde su derivada finita no existe, de modo que la cadena invocada no cumple sus hipótesis. Además, el cociente directo $|h|/h$ tiene límites laterales distintos. Por ambas vías, $F'(0)$ no existe.

### Solución 2.26 (`EDC-C02-SOL-026`)

Por definición de potencia real de base positiva y Teorema 2.5, $p(x)=x^r=E(r\ln x)$ es derivable en $x=1$ y $p'(1)=r\cdot1^{r-1}=r$. El cociente incremental de $p$ en $1$ es precisamente

$$
\frac{(1+h)^r-1}{h},\qquad h\ne0,\quad1+h>0.
$$

Por definición de derivada, el límite es $r$. No hemos supuesto previamente un binomio infinito ni un desarrollo de Taylor.

### Solución 2.27 (`EDC-C02-SOL-027`)

Para $-a<x<a$, la rama superior es

$$
y(x)=b\sqrt{1-\frac{x^2}{a^2}}>0,
$$

composición de funciones derivables, pues el argumento de la raíz es positivo. Derivando $x^2/a^2+y(x)^2/b^2=1$,

$$
\frac{2x}{a^2}+\frac{2y(x)y'(x)}{b^2}=0,
\qquad
 y'(x)=-\frac{b^2x}{a^2y(x)}.
$$

En el punto indicado, la pendiente es $-b/a$. El método no permite dividir por $y$ en los puntos extremos $(\pm a,0)$, donde la rama ya no es una función derivable en un entorno abierto con esa expresión.

## G. Desafío de síntesis

### Solución 2.28 (`EDC-C02-SOL-028`)

Por producto y cadena,

$$
y'(x)=e^{\alpha x}\bigl(\alpha\cos(\beta x)-\beta\sin(\beta x)\bigr).
$$

Derivando una segunda vez con las mismas reglas,

$$
y''(x)=e^{\alpha x}\bigl((\alpha^2-\beta^2)\cos(\beta x)-2\alpha\beta\sin(\beta x)\bigr).
$$

El coeficiente total de $\cos(\beta x)$ en $y''-2\alpha y'+(\alpha^2+\beta^2)y$ es

$$
(\alpha^2-\beta^2)-2\alpha^2+(\alpha^2+\beta^2)=0.
$$

El coeficiente total de $\sin(\beta x)$ es $-2\alpha\beta+2\alpha\beta=0$. Por lo tanto, la identidad se cumple para todo $x\in\mathbb R$, también en los casos $\alpha=0$ o $\beta=0$. No se ha demostrado que sean éstas todas las soluciones de tal ecuación.

---

**Control de cobertura:** se han resuelto los 28 ejercicios `EDC-C02-EXR-001--028` mediante entradas `EDC-C02-SOL-001--028`, sin incisos omitidos ni uso de capítulos futuros como premisas.
