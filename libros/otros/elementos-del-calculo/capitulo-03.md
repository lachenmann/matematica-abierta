---
title: Capítulo 3. Extremos, crecimiento y aproximación local
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
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C03
source-sha256: 7abd9b8b07f0232e86ce2c8949d67bd69d7bf351bded3d73814eebaf6aa80237
content-id: MA-BCH-0334
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-03.html) · [Ejercicios](capitulo-03-ejercicios.html) · [Soluciones](capitulo-03-soluciones.html) · [Notas históricas](capitulo-03-notas.html)

[← Capítulo 2](capitulo-02.html) · [Capítulo 4 →](capitulo-04.html)

> **Pregunta generadora.** Si una derivada describe lo que ocurre muy cerca de un punto, ¿con qué derecho podemos utilizarla para decidir cómo se comporta una función en un intervalo entero, dónde alcanza sus extremos y cuánto nos equivocamos al sustituirla por una recta?

Los capítulos anteriores dieron significado a la derivada y permitieron calcularla en funciones construidas mediante operaciones algebraicas, composición, exponenciales y trigonometría. Falta un paso lógico crucial. Saber que $f'(a)>0$ describe el comportamiento de cocientes incrementales próximos a $a$, pero no demuestra que $f$ crezca en todo su dominio. Tampoco basta resolver $f'(x)=0$ para encontrar los máximos y mínimos de un problema: la ecuación puede tener soluciones que no sean extremos, y los extremos pueden aparecer donde no exista derivada o en los bordes del dominio.

El problema de este capítulo consiste en pasar de un resultado **local** a una conclusión **sobre un intervalo**. Utilizaremos las consecuencias de la continuidad sobre intervalos cerrados demostradas en C00, la definición de derivada y su aproximación afín de C01 y las reglas operativas de C02. De esa combinación surgirán el principio de Fermat, el teorema de Rolle y el teorema del valor medio. A partir de ellos organizaremos la monotonía, las desigualdades de incremento, la convexidad y una primera teoría de optimización rigurosa. No utilizaremos la integral ni la fórmula de Taylor, reservadas para capítulos posteriores.

## 3.1. Un problema sencillo con una dificultad escondida

Sea $f(x)=x^3-3x$ en el intervalo $[-2,2]$. El cálculo algebraico de C02 da

$$
f'(x)=3x^2-3=3(x-1)(x+1).
$$

Los puntos $-1$ y $1$ son candidatos a extremos. Sin embargo, ¿por qué deberíamos mirar precisamente los ceros de la derivada? ¿Y por qué no olvidar los extremos del intervalo $-2$ y $2$? Los valores son

$$
\begin{array}{c|rrrr}
x&-2&-1&1&2\\ \hline
f(x)&-2&2&-2&2.
\end{array}
$$

Este ejemplo tiene extremos absolutos que se alcanzan tanto dentro del intervalo como en sus bordes. Más adelante podremos justificar por el signo de $f'$ qué ocurre entre esos cuatro puntos. Primero debemos formular exactamente la relación entre un extremo interior y una derivada.

## 3.2. Extremos locales y el principio de Fermat

**Definición 3.1 (`EDC-C03-DEF-001`).** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $c\in D$. Decimos que $f$ tiene un **máximo local** en $c$ si existe $\delta>0$ tal que

$$
f(x)\le f(c)\qquad(x\in D,\ |x-c|<\delta).
$$

Se define análogamente un **mínimo local** invirtiendo la desigualdad. Si la desigualdad es estricta para $x\ne c$, el extremo local es estricto. Un **máximo absoluto** exige $f(x)\le f(c)$ para **todo** $x\in D$; un mínimo absoluto se define de modo dual. Un extremo local se entiende siempre *relativo al dominio especificado*.

Los extremos absolutos existen para toda función continua en $[a,b]$, $a<b$, por el teorema de los valores extremos de C00 (`EDC-C00-THM-007`). Pero nada en dicho teorema asegura que los puntos que los realizan sean interiores.

**Teorema 3.1 (principio de Fermat; `EDC-C03-THM-001`).** Sea $f:D\to\mathbb R$ y sea $c$ un punto interior de $D$. Si $f$ tiene un extremo local en $c$ y es derivable allí, entonces

$$
f'(c)=0.
$$

**Demostración.** Supongamos primero que $c$ es un máximo local. Para $h>0$ suficientemente pequeño,

$$
\frac{f(c+h)-f(c)}{h}\le0,
$$

mientras que para $h<0$ suficientemente pequeño la misma fracción es mayor o igual que cero, pues el numerador no es positivo y el denominador es negativo. La existencia de la derivada bilateral obliga a que los dos límites laterales coincidan: uno no puede ser positivo y el otro no puede ser negativo. Por tanto $f'(c)=0$. Para un mínimo basta aplicar la demostración a $-f$. $\square$

La conclusión es **necesaria, no suficiente**. Para $f(x)=x^3$, se cumple $f'(0)=0$, pero $0$ no es máximo ni mínimo local: a ambos lados toma valores de signos opuestos. Para $f(x)=|x|$, $0$ sí es un mínimo local, pero $f'(0)$ no existe. Para $f(x)=x$ en $[0,1]$, el mínimo absoluto se alcanza en $0$, punto de borde; la derivada unilateral derecha vale $1$, no cero. Ninguno de estos hechos contradice el teorema, porque en cada ejemplo falta una hipótesis distinta.

**Definición 3.2 (`EDC-C03-DEF-002`).** Para una función definida sobre un intervalo, un punto **estacionario** interior es un punto donde existe $f'(c)=0$. Llamaremos **candidato crítico interior** a un punto interior donde $f'(c)=0$ o donde la función no es derivable. Usaremos esta expresión como instrumento para buscar extremos, sin afirmar que cada candidato sea uno.

La terminología está deliberadamente fijada: no confundiremos punto estacionario con todo punto de posible extremo. El método correcto exige **comprobar** qué ocurre en los candidatos y en los extremos del dominio.

## 3.3. Rolle: dos valores iguales fuerzan una pendiente nula

Imaginemos una curva que comienza y termina a la misma altura. ¿Necesariamente tiene entre ambos extremos una tangente horizontal? La afirmación no es cierta para una curva con un ángulo agudo, pero sí cuando la continuidad y la derivabilidad se distribuyen correctamente.

**Teorema 3.2 (Rolle; `EDC-C03-THM-002`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$. Supongamos que:

1. $f$ es continua en $[a,b]$;
2. $f$ es derivable en $(a,b)$;
3. $f(a)=f(b)$.

Entonces existe $c\in(a,b)$ tal que $f'(c)=0$.

**Demostración.** Por el teorema de los valores extremos de C00, $f$ alcanza su máximo $M$ y su mínimo $m$ en $[a,b]$. Si $M=m$, es constante y $f'(x)=0$ en cada punto interior. Si $M>m$, al menos uno de esos valores es distinto del valor común $f(a)=f(b)$. Ese extremo no puede realizarse únicamente en los bordes, cuyos valores son iguales: existe un punto $c\in(a,b)$ donde se alcanza. En $c$ se aplica el principio de Fermat y se obtiene $f'(c)=0$. $\square$

El ejemplo $f(x)=|x|$ en $[-1,1]$ enseña por qué la derivabilidad interior importa: los valores extremos son iguales, $f(-1)=f(1)=1$, pero la derivada vale $-1$ para $x<0$, $1$ para $x>0$ y no existe en $0$. No hay ningún punto interior de derivada nula. El ejemplo $f(x)=x$ en $[0,1]$ muestra por qué hace falta la igualdad de extremos. Y la discontinuidad puede destruir la conclusión aunque exista derivada en todo punto interior donde la función está definida: por ejemplo, $f(0)=f(1)=0$ y $f(x)=x$ para $0<x<1$ no es continua en $1$ y tiene derivada interior $1$.

## 3.4. El teorema del valor medio

En un intervalo $[a,b]$, el cambio total $f(b)-f(a)$ determina la pendiente de la secante

$$
m=\frac{f(b)-f(a)}{b-a}.
$$

La pregunta decisiva es si esa pendiente global aparece como derivada en algún punto intermedio. La respuesta reduce una comparación entre extremos a una propiedad local.

**Teorema 3.3 (valor medio de Lagrange; `EDC-C03-THM-003`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en $[a,b]$ y derivable en $(a,b)$. Existe un punto $c\in(a,b)$ tal que

$$
f'(c)=\frac{f(b)-f(a)}{b-a},
\qquad\text{equivalentemente}\qquad
f(b)-f(a)=f'(c)(b-a).
$$

**Demostración.** Construimos la función auxiliar

$$
g(x)=f(x)-\left[f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\right].
$$

La cantidad entre corchetes es la ecuación de la recta secante. Por las hipótesis y las reglas de derivación ya demostradas, $g$ es continua en $[a,b]$ y derivable en $(a,b)$. Además $g(a)=g(b)=0$. Por Rolle existe $c\in(a,b)$ con $g'(c)=0$, es decir,

$$
f'(c)-\frac{f(b)-f(a)}{b-a}=0.
$$

$\square$

Para $f(x)=x^2$ entre $a=-1$ y $b=2$, la pendiente media es $(4-1)/(2-(-1))=1$. Como $f'(x)=2x$, el punto garantizado es $c=1/2$. En general, el teorema asegura la **existencia** de algún $c$; no identifica un único punto ni afirma que $c$ sea el punto medio de $[a,b]$.

El valor medio enlaza dos niveles que los capítulos anteriores habían mantenido separados: no toda información local se convierte automáticamente en conclusión global, pero las hipótesis de continuidad y derivabilidad sí permiten transportar la derivada hacia la diferencia finita de los valores de una función.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — De una cumbre al teorema del valor medio"}

*Lectura opcional.*

Quien sube una colina y después baja suele pasar por un lugar donde la pendiente se aplana. Esta imagen nos ayuda a recordar la pregunta de Fermat por los máximos y mínimos: ¿qué tiene de especial el punto donde una cantidad deja de crecer y empieza a disminuir?

Ahora pensemos en una curva que comienza y termina a la misma altura. Entre ambos extremos puede subir y bajar; el teorema de Rolle encuentra un punto con tangente horizontal. Si las alturas finales son distintas, el teorema del valor medio encuentra una tangente paralela a la secante que une los extremos.

Las preguntas históricas sobre extremos, raíces y tangentes se encuentran aquí en un mismo paisaje. Los nombres de Fermat y Rolle nos ayudan a recorrerlo: primero una cumbre, luego dos alturas iguales y finalmente una comparación entre el cambio de todo el camino y el cambio en uno de sus puntos.

**Para seguir leyendo:** [Notas históricas del capítulo 3, apartados H1–H3](capitulo-03-notas.html).

:::

## 3.5. Monotonía, constancia y unicidad

**Definición 3.3 (`EDC-C03-DEF-003`).** Una función $f:I\to\mathbb R$ es **no decreciente** cuando $x<y$ implica $f(x)\le f(y)$; es **estrictamente creciente** si la conclusión es $f(x)<f(y)$. Las definiciones de no creciente y estrictamente decreciente invierten esas comparaciones.

**Teorema 3.4 (criterios de monotonía; `EDC-C03-THM-004`).** Sea $I\subseteq\mathbb R$ un intervalo abierto y sea $f:I\to\mathbb R$ derivable. Entonces:

1. $f$ es no decreciente en $I$ **si y sólo si** $f'(x)\ge0$ para todo $x\in I$.
2. Si $f'(x)>0$ para todo $x\in I$, entonces $f$ es estrictamente creciente. Si $f'(x)<0$ en todo $I$, es estrictamente decreciente.
3. $f$ es constante en $I$ **si y sólo si** $f'(x)=0$ para todo $x\in I$.

Para intervalos de cualquier tipo que posean extremos de borde, las conclusiones entre puntos del intervalo se conservan si $f$ es continua en esos extremos y derivable en el interior.

**Demostración.** Sean $x<y$ en $I$. El valor medio, aplicado en $[x,y]$, da $f(y)-f(x)=f'(c)(y-x)$ para algún $c\in(x,y)$. Como $y-x>0$, las condiciones sobre el signo de la derivada producen las implicaciones directas de 1, 2 y 3. Recíprocamente, si $f$ es no decreciente, para $h>0$ suficientemente pequeño el cociente $(f(x+h)-f(x))/h$ es no negativo; para $h<0$ sucede lo mismo, pues numerador y denominador son no positivos. El límite existe y es $f'(x)\ge0$. Si $f$ es constante, los cocientes son cero. Si $f'=0$ en todos los puntos, el valor medio da $f(y)=f(x)$ para cada par. $\square$

El recíproco estricto **no** exige $f'(x)>0$ en todos los puntos: la función $x\mapsto x^3$ es estrictamente creciente en $\mathbb R$ y tiene $f'(0)=0$. A su vez, $f'(x)\ge0$ sólo fuerza crecimiento no estricto: puede haber tramos donde la función sea constante.

**Corolario 3.1 (unicidad de primitivas potenciales; `EDC-C03-COR-001`).** Sea $I\subseteq\mathbb R$ un intervalo no vacío, abierto, cerrado, semiabierto o no acotado. Sean $f,g:I\to\mathbb R$ **continuas en todo $I$ según la definición de continuidad relativa de C00** (también en cualquier extremo incluido) y derivables en su interior $I^{\circ}$. Si $f'(x)=g'(x)$ para todo $x\in I^{\circ}$, entonces $f-g$ es constante en **todo $I$**. Para un intervalo de un solo punto, la conclusión es trivial. Por tanto, una función cuya derivada se conoce queda determinada **salvo una constante aditiva**, siempre que ya exista alguna función con esa derivada y se controlen sus valores de borde.

**Demostración.** Sea $h=f-g$. Para cualesquiera $u<v$ en $I$, el segmento $[u,v]$ está contenido en $I$ por ser intervalo. La función $h$ es continua en $[u,v]$, incluidos sus extremos, y derivable en $(u,v)$, con $h'=0$. El teorema del valor medio proporciona $c\in(u,v)$ con $h(v)-h(u)=h'(c)(v-u)=0$. Como $u,v$ son arbitrarios, $h$ es constante en todo $I$. $\square$

Esta observación será decisiva en la teoría integral. Por ahora no hemos probado que *toda* función dada sea derivada de otra, ni hemos definido una integral.

## 3.6. Estimar una variación sin calcularla exactamente

**Teorema 3.5 (cotas de incremento; `EDC-C03-THM-005`).** Sea $f:[a,b]\to\mathbb R$ continua en $[a,b]$ y derivable en $(a,b)$, donde $a<b$. Si $m,M\in\mathbb R$ satisfacen

$$
m\le f'(x)\le M\qquad(x\in(a,b)),
$$

entonces

$$
m(b-a)\le f(b)-f(a)\le M(b-a).
$$

En particular, si $|f'(x)|\le K$ para todo $x\in(a,b)$ y $K\ge0$, entonces

$$
|f(b)-f(a)|\le K|b-a|.
$$

**Demostración.** El teorema del valor medio proporciona un $c\in(a,b)$ con $f(b)-f(a)=f'(c)(b-a)$. Como $b-a>0$, multiplicar las desigualdades que acotan a $f'(c)$ produce el resultado. La cota absoluta surge tomando $m=-K$ y $M=K$. $\square$

**Aplicación: una desigualdad trigonométrica.** Como $|\cos x|\le1$ para todo real y $\sin'=\cos$ se demostró en C02, para cualesquiera $a,b\in\mathbb R$ tenemos

$$
|\sin b-\sin a|\le|b-a|.
$$

Esto no se deduce de una mera observación gráfica: es un control cuantitativo válido para todos los pares de argumentos reales.

**Proposición 3.1 (inversas y control de sensibilidad; `EDC-C03-PRP-001`).** Sea $I$ un intervalo abierto y $f:I\to\mathbb R$ derivable, con $f'(x)\ge m>0$ en todo $I$. Entonces $f$ es estrictamente creciente, admite una inversa $F:f(I)\to I$ y

$$
|F(v)-F(u)|\le\frac{|v-u|}{m}\qquad(u,v\in f(I)).
$$

**Demostración.** La monotonía estricta sigue del Teorema 3.4. Si $u=f(x)$ y $v=f(y)$, con $x<y$, el valor medio da $v-u=f'(c)(y-x)\ge m(y-x)$. Reordenamos y obtenemos la desigualdad, que es simétrica en $u,v$. $\square$

En este capítulo las cotas de derivadas son herramientas de prueba. No sustituimos las hipótesis por un dibujo ni usamos reglas globales sobre funciones que sólo sabemos derivables en un punto.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — L’Hôpital y Bernoulli: de las lecciones al libro"}

*Lectura opcional.*

Antes de escribir su tratado, el marqués de L’Hôpital fue alumno del nuevo cálculo. En 1691 y 1692 recibió lecciones de Johann Bernoulli. Aquellas enseñanzas formaron parte del camino que llevó a su Analyse des infiniment petits, publicado en 1696.

El libro iba desde las reglas de cálculo hasta tangentes, máximos, mínimos y puntos de inflexión. En el prefacio, L’Hôpital agradecía el trabajo de Leibniz y de los Bernoulli, especialmente el de Johann. Detrás del tratado había lecciones, preguntas y correspondencia: aprender y enseñar también hicieron avanzar el cálculo.

En sus páginas aparece el problema que hoy asociamos a la regla de L’Hôpital: ¿qué hacer cuando el numerador y el denominador de un cociente se acercan ambos a cero? Es una pregunta natural después de estudiar razones de cambio. Las derivadas ofrecen una pista, y los teoremas sobre variación ayudan a comprender por qué puede funcionar.

**Para seguir leyendo:** [L’Hôpital, Analyse des infiniment petits (1696); Bradley, Petrilli y Sandifer, edición anotada (2015), introducción](https://link.springer.com/book/10.1007/978-3-319-17115-9).

:::

## 3.7. Aproximación lineal y control del error

En C01 probamos que la derivabilidad en $a$ equivale a

$$
f(a+h)=f(a)+f'(a)h+r_a(h),\qquad\frac{r_a(h)}{|h|}\longrightarrow0
\quad(h\to0,\ h\ne0).
$$

Esta es una afirmación **local**: no ofrece por sí sola una tolerancia común para intervalos grandes. El teorema del valor medio permite convertirla en una estimación comprobable cuando conocemos cómo varía la derivada.

**Proposición 3.2 (error de linealización; `EDC-C03-PRP-002`).** Sea $I$ un intervalo abierto, $a\in I$, y supongamos que $f$ es derivable en $I$. Para $a+h\in I$, $h\ne0$, existe un punto $c$ estrictamente entre $a$ y $a+h$ tal que

$$
f(a+h)-f(a)-f'(a)h=[f'(c)-f'(a)]h.
$$

Si además $f'$ es continua en $a$, el error es $o(|h|)$, de acuerdo con C01. Si $f'$ es derivable en el intervalo entre $a$ y $a+h$ y $|f''|\le K$ allí, entonces

$$
|f(a+h)-f(a)-f'(a)h|\le K|h|^2.
$$

**Demostración.** El valor medio aplicado entre $a$ y $a+h$ da la primera igualdad; su orientación no altera el resultado. Si $f'$ es continua en $a$, $c\to a$ cuando $h\to0$, por lo que $f'(c)-f'(a)\to0$. Para la cota cuadrática, el teorema del valor medio aplicado a $f'$ entre $a$ y $c$ da $|f'(c)-f'(a)|\le K|c-a|\le K|h|$, y concluimos. $\square$

La estimación cuadrática tiene una constante deliberadamente no óptima: su fuerza aquí radica en que necesita sólo resultados ya demostrados. Una fórmula precisa con resto de orden superior —incluida su constante— será objeto del capítulo 9. Tampoco debe confundirse una aproximación lineal con una igualdad polinómica exacta en todo un intervalo.

## 3.8. Convexidad: de las pendientes a la forma de la gráfica

Hay funciones cuya inclinación no permanece constante pero aumenta sistemáticamente. Ese fenómeno se formaliza sin hablar de curvatura de superficies ni de espacios abstractos.

**Definición 3.4 (`EDC-C03-DEF-004`).** Una función $f:I\to\mathbb R$, sobre un intervalo $I$, es **convexa** si para cualesquiera $x,y\in I$ y $t\in[0,1]$ se cumple

$$
f((1-t)x+ty)\le(1-t)f(x)+tf(y).
$$

Si la desigualdad es estricta cuando $x\ne y$ y $0<t<1$, se dice que $f$ es **estrictamente convexa**. La **concavidad** se define por convexidad de $-f$.

**Teorema 3.6 (pendientes y convexidad; `EDC-C03-THM-006`).** Sea $I$ un intervalo abierto y $f:I\to\mathbb R$ derivable. Son equivalentes:

1. $f$ es convexa;
2. $f'$ es no decreciente;
3. para todo $x,y\in I$,

$$
f(y)\ge f(x)+f'(x)(y-x).
$$

Si $f'$ es estrictamente creciente, entonces $f$ es estrictamente convexa.

**Demostración.** Supongamos primero que $f$ es convexa. Para $x<y<z$, la desigualdad convexa con $y=(1-t)x+tz$ implica

$$
\frac{f(y)-f(x)}{y-x}\le\frac{f(z)-f(x)}{z-x}\le\frac{f(z)-f(y)}{z-y}.
$$

Fijando $x<z$ y haciendo $y\to x^+$ en la primera comparación obtenemos $f'(x)\le(f(z)-f(x))/(z-x)$. Haciendo $y\to z^-$ en la segunda obtenemos $(f(z)-f(x))/(z-x)\le f'(z)$. Por tanto $f'(x)\le f'(z)$.

Si $f'$ es no decreciente, para $y>x$ el valor medio da $f(y)-f(x)=f'(c)(y-x)\ge f'(x)(y-x)$, pues $c\in(x,y)$. Si $y<x$, el mismo teorema da $f(y)-f(x)=f'(c)(y-x)$ con $c\in(y,x)$, y como $f'(c)\le f'(x)$ la multiplicación por $y-x<0$ vuelve a producir la desigualdad de 3.

Finalmente, si vale 3 y $z=(1-t)x+ty$, aplicamos la desigualdad de soporte con base $z$ a $x$ y a $y$ y multiplicamos por $1-t$ y $t$, respectivamente. Al sumar, los términos que contienen $f'(z)$ se cancelan y resulta $f(z)\le(1-t)f(x)+tf(y)$. Si $f'$ es estrictamente creciente, en el paso del valor medio para $x\ne y$ la desigualdad de soporte es estricta; de ello se deduce convexidad estricta para $0<t<1$. $\square$

La desigualdad de soporte dice que **la recta tangente queda por debajo de la gráfica** de una función convexa derivable. Esta afirmación ya no es una mera descripción gráfica: procede de un teorema con hipótesis y prueba.

**Corolario 3.2 (criterio por la segunda derivada; `EDC-C03-COR-002`).** Si $f$ es dos veces derivable sobre un intervalo abierto $I$ y $f''(x)\ge0$ para todo $x\in I$, entonces $f$ es convexa. Si $f''(x)>0$ en todo $I$, es estrictamente convexa. Las afirmaciones duales valen cuando $f''\le0$ o $f''<0$.

**Demostración.** Apliquemos el criterio de monotonía del Teorema 3.4 a $f'$, que es derivable y tiene derivada $f''$. Después aplicamos el Teorema 3.6. $\square$

**Ejemplo.** Como $(\ln x)''=-1/x^2<0$ para $x>0$, el logaritmo es estrictamente cóncavo en $(0,\infty)$. La desigualdad de soporte para una función cóncava, con base $x=1$, produce

$$
\ln y\le\ln1+(\ln1)'(y-1)=y-1,\qquad y>0.
$$

Hay igualdad si $y=1$, y es estricta en los demás puntos. La propiedad no depende de haber definido todavía la integral del logaritmo.

## 3.9. Qué decide la segunda derivada en un punto

El principio de Fermat reduce la búsqueda de extremos interiores derivables a puntos donde $f'=0$. La segunda derivada puede ayudar a **clasificarlos**, pero sólo bajo sus hipótesis.

**Teorema 3.7 (criterio local de segunda derivada; `EDC-C03-THM-007`).** Sea $c$ interior de un intervalo abierto $I$, y supongamos que $f$ es derivable en una vecindad de $c$, que $f'(c)=0$ y que $f'$ es derivable en $c$. Si $f''(c)>0$, entonces $f$ tiene un mínimo local estricto en $c$. Si $f''(c)<0$, tiene un máximo local estricto allí.

**Demostración.** Si $f''(c)>0$, por definición de la derivada de $f'$ existe $\delta>0$ tal que

$$
\frac{f'(c+h)-f'(c)}h>0\qquad(0<|h|<\delta).
$$

Como $f'(c)=0$, esto implica $f'(c+h)<0$ para $h<0$ y $f'(c+h)>0$ para $h>0$. Por el criterio de monotonía, $f$ decrece estrictamente en el tramo izquierdo y crece estrictamente en el derecho (reduciendo $\delta$ si fuera necesario). Se alcanza un mínimo estricto en $c$. El caso negativo se aplica a $-f$. $\square$

Cuando $f''(c)=0$, el criterio no resuelve nada. Las funciones $x^4$, $-x^4$ y $x^3$ tienen en $0$ primera y segunda derivadas nulas; la primera tiene mínimo, la segunda máximo y la tercera ningún extremo. No hay una regla correcta que convierta automáticamente la igualdad $f''(c)=0$ en una clasificación.

## 3.10. Las derivadas tienen una propiedad intermedia

En C02 vimos una función derivable cuya derivada no es continua. No obstante, una derivada no puede saltar arbitrariamente de un valor a otro dejando todos los valores intermedios sin alcanzar.

**Teorema 3.8 (propiedad de Darboux de la derivada; `EDC-C03-THM-008`).** Sea $f:I\to\mathbb R$ derivable en un intervalo abierto $I$, y sean $a<b$ dos puntos de $I$. Si un número $\lambda$ está estrictamente entre $f'(a)$ y $f'(b)$, existe $c\in(a,b)$ tal que $f'(c)=\lambda$.

**Demostración.** Consideremos $g(x)=f(x)-\lambda x$. Supongamos primero que $f'(a)<\lambda<f'(b)$, de modo que $g'(a)<0<g'(b)$. Como $g'(a)<0$, para incrementos positivos suficientemente pequeños tenemos $g(a+h)<g(a)$; por tanto $a$ no realiza el mínimo absoluto de $g$ en $[a,b]$. Análogamente, $g'(b)>0$ implica que para ciertos $h<0$ pequeños se cumple $g(b+h)<g(b)$: tampoco $b$ realiza el mínimo. Por continuidad y valores extremos, $g$ tiene un mínimo absoluto en algún punto interior $c$, y por Fermat $g'(c)=0$. Así $f'(c)=\lambda$. Si el orden de las derivadas extremas es el inverso, aplicamos lo anterior a $-f$ y $-\lambda$. $\square$

Este resultado no dice que toda derivada sea continua. Dice algo más preciso y compatible con el ejemplo de C02: **si toma dos valores, también toma los intermedios en algún punto entre ellos**.

## 3.11. Un método de optimización con hipótesis comprobables

La estrategia para maximizar o minimizar una función $f$ continua en un intervalo compacto $[a,b]$ se apoya ahora en una cadena de razones, no sólo en un procedimiento formal:

1. el teorema de valores extremos garantiza la existencia de máximo y mínimo;
2. cualquier extremo absoluto **interior donde exista derivada** tiene derivada cero, por Fermat;
3. los puntos interiores de no derivabilidad y los extremos de borde también deben examinarse;
4. los valores de los candidatos se comparan, o se estudian intervalos de signo de la derivada mediante el valor medio.

No se exige que el dominio original sea compacto: cuando se trata de un intervalo abierto o ilimitado habrá que investigar si el extremo existe y qué pasa al acercarse a sus bordes. Escribir $f'(x)=0$ no garantiza por sí solo que el máximo exista.

**Proposición 3.3 (optimización en intervalos cerrados; `EDC-C03-PRP-003`).** Sea $f:[a,b]\to\mathbb R$ continua y derivable salvo quizás en un conjunto $S\subset(a,b)$. Todo punto donde $f$ alcanza un máximo o mínimo absoluto pertenece a $\{a,b\}\cup S\cup\{c\in(a,b)\setminus S:f'(c)=0\}$. Si este conjunto de candidatos es finito, comparar sus valores identifica los extremos absolutos.

**Demostración.** La existencia es el teorema de valores extremos. Si un extremo ocurre en $c\in(a,b)\setminus S$, existe derivada y Fermat impone $f'(c)=0$. Todo caso restante está entre los bordes o en $S$. Para un conjunto finito de candidatos, cada extremo absoluto tiene que estar en él y basta comparar los valores. $\square$

**Ejemplo 1: el rectángulo de perímetro fijo.** Si el perímetro es $P>0$, sus lados positivos $x,y$ satisfacen $x+y=P/2$ y el área es

$$
A(x)=x\left(\frac P2-x\right),\qquad0<x<\frac P2.
$$

El polinomio se extiende continuamente a $[0,P/2]$ con valores nulos en los extremos. Como $A'(x)=P/2-2x$, es positivo para $x<P/4$ y negativo para $x>P/4$. El valor máximo entre rectángulos no degenerados corresponde a $x=y=P/4$ y es $P^2/16$. La restricción geométrica importa: un lado negativo no pertenece al problema.

**Ejemplo 2: una familia con decaimiento.** Sean $\alpha,\lambda>0$ y

$$
F(x)=x^{\alpha}e^{-\lambda x},\qquad x>0.
$$

Por las reglas de C02,

$$
F'(x)=x^{\alpha-1}e^{-\lambda x}(\alpha-\lambda x).
$$

Los dos primeros factores son positivos, de modo que $F$ crece para $0<x<\alpha/\lambda$ y decrece después. El máximo global en el semieje positivo se realiza en $x=\alpha/\lambda$, con valor $(\alpha/\lambda)^{\alpha}e^{-\alpha}$. No hemos necesitado afirmar sin prueba que la derivada negativa en un solo punto fuerza decrecimiento en todo el semieje: la desigualdad de signos está verificada en intervalos completos.

## 3.12. Historia, alcance y tránsito a las cuadraturas

La búsqueda de extremos es históricamente anterior a la formulación moderna de la derivada. Fermat utilizó métodos algebraicos para abordar máximos, mínimos y tangentes; no corresponde atribuirle automáticamente la prueba con límites laterales que acabamos de dar. El resultado asociado al nombre de Michel Rolle apareció en un contexto de álgebra y teoría de ecuaciones, no como una proposición escrita con nuestro vocabulario de función continua y derivable. Las elaboraciones rigurosas posteriores del valor medio forman parte de una historia más extensa y no de un instante único de descubrimiento. Los documentos historiográficos consultados, sus localizadores y sus límites se registran en [notas históricas](capitulo-03-notas.html); este capítulo utiliza pruebas modernas propias.

Hemos establecido un nuevo puente fundamental:

$$
\text{derivada local}\xrightarrow[\text{continuidad y derivabilidad}]{\text{Rolle y valor medio}}
\text{crecimiento, cotas y extremos en intervalos}.
$$

Ahora poseemos un repertorio suficiente para abordar problemas de variación y justificar métodos de optimización. Pero no hemos definido el área bajo una curva ni la acumulación de una magnitud variable. En C04 comenzaremos por cuadraturas y procedimientos históricos de aproximación; C05 convertirá esos métodos en la teoría rigurosa de la integral. Sólo en C06 estableceremos su relación con la derivación.

### Mapa de dependencias

- **De C00:** orden y completitud de $\mathbb R$, continuidad, valores extremos, criterio secuencial y teorema del valor intermedio.
- **De C01:** derivada bilateral en un punto interior, límites laterales, aproximación afín y derivabilidad implica continuidad.
- **De C02:** suma, producto, composición, inversas y derivadas de potencias, exponencial, logaritmo y trigonometría, todas en sus dominios.
- **Nuevos:** `EDC-C03-THM-001--008`, `EDC-C03-PRP-001--003`, `EDC-C03-COR-001--002`, y las definiciones locales; no se invoca un resultado de C04–C11.
- **Reservado:** integrales, teorema fundamental, Taylor con resto e hipótesis de convergencia de series generales.

### Trabajo del lector

El banco [Ejercicios del capítulo 3](capitulo-03-ejercicios.html) propone problemas de lectura de hipótesis, cálculo aplicado, demostración, contraejemplos, optimización y una síntesis final. Las [soluciones desarrolladas](capitulo-03-soluciones.html) se conservan en archivo independiente: resolver antes de consultarlas forma parte del método del libro.
