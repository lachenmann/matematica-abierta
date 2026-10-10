---
title: "1.11 — Soluciones"
description: "Capítulo 1 de Cálculo para matemáticos: lectura por secciones."
content-type: book-section
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas: [calculo, analisis]
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: 2026-09-09
date-modified: 2026-10-06
prerequisites:
  []
number-sections: true
number-depth: 2
number-offset: [0, 10]
crossref:
  chapters: true
format:
  html:
    css: calculo-para-matematicos.css
    html-math-method:
      method: mathjax
      url: https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js
---

# Los números reales: axiomas de cuerpo, orden y completitud

[← Anterior](cpm-c01-11.md) · [Índice del capítulo](los-numeros-reales-orden-valor-absoluto-desigualdades-y-completitud.md) · [Siguiente →](funciones-reales-estructura-composicion-inversas-y-graficas.md)

## Soluciones de los ejercicios {#cpm-c01-soluciones}

### Soluciones

Las soluciones siguen el mismo orden. En los ejercicios técnicos se incluyen los controles de dominio y de signos; en los problemas de síntesis se explicita la estrategia y la dependencia estructural decisiva.

#### Soluciones del nivel A

::: {#sol-t1-0036}
<!-- CPM-T1-SOL-0036 -->
**Solución A1.**

Las dos condiciones equivalen a

$$
-1<x<5
$$

y

$$
-3\le x\le1.
$$

Debemos tomar la intersección. Por tanto,

$$
-1<x\le1,
$$

y

$$
\boxed{S=(-1,1]}.
$$

El extremo $-1$ queda excluido por la primera desigualdad estricta; el extremo $1$ satisface ambas condiciones.
:::
::: {#sol-t1-0037}
<!-- CPM-T1-SOL-0037 -->
**Solución A2.**

Como $c<0$, multiplicar $a<b$ por $c$ invierte el orden; además, los dos productos son negativos:

$$
\boxed{bc<ac<0}.
$$

Dividir por $c<0$ también invierte el orden, y ambos cocientes son negativos:

$$
\boxed{\frac bc<\frac ac<0}.
$$

Finalmente, para recíprocos positivos se invierte el orden:

$$
\boxed{0<\frac1b<\frac1a}.
$$

Las tres cadenas usan el mismo dato $a<b$, pero cada transformación exige controlar el signo del factor o divisor.
:::
::: {#sol-t1-0038}
<!-- CPM-T1-SOL-0038 -->
**Solución A3.**

Todo elemento de $A$ es menor que $5$, y en el componente $[3,5)$ hay elementos arbitrariamente próximos a $5$ por la izquierda. Por tanto,

$$
\sup A=5,
$$

pero $5\notin A$, así que no hay máximo.

Del mismo modo, $-2$ es cota inferior y el componente $(-2,1]$ contiene puntos arbitrariamente próximos a $-2$ por la derecha. Luego

$$
\inf A=-2,
$$

y como $-2\notin A$, tampoco hay mínimo.
:::
::: {#sol-t1-0039}
<!-- CPM-T1-SOL-0039 -->
**Solución A4.**

La clasificación es la siguiente.

1. **Axioma.**
   $$
   a(b+c)=ab+ac
   $$
   es exactamente `C9`, la distributividad.

2. **Definición.**
   $$
   a-b:=a+(-b)
   $$
   es la definición de resta como operación derivada de la suma y el inverso aditivo.

3. **Resultado demostrado.**
   $$
   a0=0
   $$
   no figura entre `C1--C9`. Se demuestra a partir de los axiomas; en §1.1 aparece como la prueba auditada [Ejemplo 1.1](cpm-c01-01.md#exm-t1-0040).

4. **Resultado demostrado.** La implicación
   $$
   a\ne0,\quad ab=ac\Longrightarrow b=c
   $$
   es la cancelación multiplicativa de [Proposición 1.3](cpm-c01-01.md#prp-t1-0027). La hipótesis $a\ne0$ no es decorativa: permite usar el inverso multiplicativo de $a$.

5. **Definición.** El orden se introduce mediante la positividad:
   $$
   a<b
   \iff
   b-a>0.
   $$
   Por tanto esta equivalencia fija el significado de $<$ dentro de la estructura ordenada.

La distinción importa porque un axioma puede usarse como punto de partida, una definición fija significado y un resultado demostrado solo puede reutilizarse después de haber sido establecido. Si tratamos una consecuencia como si fuese axioma, podemos ocultar precisamente la dependencia que una auditoría de prueba debe hacer visible.
:::
::: {#sol-t1-0040}
<!-- CPM-T1-SOL-0040 -->
**Solución A5.**

1. Sí. El conjunto es no vacío —por ejemplo, contiene a $2$— y está acotado superiormente, por ejemplo por $3$.
2. No. Es no vacío, pero no está acotado superiormente.
3. No. Falla la hipótesis de no vacuidad.
4. Sí. Contiene a $1$ y está acotado superiormente por $1$.
5. Sí. Es no vacío y $0$ es una cota superior.

La quinta parte subraya que el axioma solo exige acotación **superior**; el conjunto puede ser ilimitado hacia abajo.
:::
::: {#sol-t1-0041}
<!-- CPM-T1-SOL-0041 -->
**Solución A6.**

1. La desigualdad triangular se obtiene de **cuerpo ordenado** y las propiedades del valor absoluto; no necesita completitud.
2. La existencia general de supremos para conjuntos no vacíos y acotados superiormente es **completitud directamente**.
3. $1/n<\varepsilon$ se deduce de la **propiedad arquimediana**, que en nuestro desarrollo es una **consecuencia previa de completitud**.
4. La densidad racional se deduce de arquimedianidad y encajonamiento entero; por tanto depende **indirectamente de completitud** en la cadena adoptada por este capítulo.

La clasificación depende de nuestra arquitectura de pruebas, no solo de que un resultado sea verdadero en $\mathbb R$.
:::

::: {#sol-t1-0042}
<!-- CPM-T1-SOL-0042 -->
**Solución A7.**

Tenemos

$$
\frac1{n+2}<\frac1{n+1}.
$$

Por tanto,

$$
1-\frac1{n+1}<1-\frac1{n+2}
$$

y

$$
1+\frac1{n+2}<1+\frac1{n+1}.
$$

Así, los extremos del intervalo siguiente quedan dentro del anterior y

$$
I_{n+1}\subseteq I_n.
$$

Además,

$$
1-\frac1{n+1}\le1\le1+\frac1{n+1},
$$

de modo que $1\in I_n$ para todo $n$.

Como todos los $I_n$ son cerrados, no vacíos, acotados y encajados, el principio de intervalos encajados garantiza

$$
\bigcap_nI_n\neq\varnothing.
$$

Ese teorema por sí solo garantiza existencia, no unicidad. La unicidad requeriría además explotar que las longitudes se hacen arbitrariamente pequeñas.
:::

#### Soluciones del nivel B

::: {#sol-t1-0043}
<!-- CPM-T1-SOL-0043 -->
**Solución B1.**

La desigualdad equivale a

$$
1\le|x-1|\le3.
$$

La cota superior da

$$
-2\le x\le4,
$$

mientras que $|x-1|\ge1$ equivale a

$$
x\le0
\quad\text{o}\quad
x\ge2.
$$

Intersectando ambas condiciones,

$$
\boxed{x\in[-2,0]\cup[2,4]}.
$$
:::
::: {#sol-t1-0044}
<!-- CPM-T1-SOL-0044 -->
**Solución B2.**

Factorizamos:

$$
|x^2-4|=|x-2|\,|x+2|.
$$

Para controlar el segundo factor escribimos

$$
x+2=(x-2)+4.
$$

Por desigualdad triangular,

$$
|x+2|\le |x-2|+4<\frac1{10}+4=\frac{41}{10}.
$$

Luego

$$
|x^2-4|
<
\frac1{10}\cdot\frac{41}{10}
=
\frac{41}{100}.
$$

La idea es típica de las estimaciones futuras: el dato controla $|x-2|$ y fabricamos a partir de él un control del factor restante.
:::

::: {#sol-t1-0045}
<!-- CPM-T1-SOL-0045 -->
**Solución B3.**

Por las reglas de cocientes,

$$
a^{-1}-b^{-1}
=
\frac1a-\frac1b
=
\frac{b-a}{ab}.
$$

Si $0<a<b$, entonces $b-a>0$ y $ab>0$. Dividir un positivo por un positivo produce un número positivo, de modo que

$$
\frac1a-\frac1b>0.
$$

Por definición del orden,

$$
\boxed{\frac1b<\frac1a}.
$$
:::
::: {#sol-t1-0046}
<!-- CPM-T1-SOL-0046 -->
**Solución B4.**

La elección más sencilla es

$$
\boxed{n=201}.
$$

Claramente $201>200$. Además, como $201>137>0$, al tomar recíprocos se invierte el orden:

$$
\frac1{201}<\frac1{137}.
$$

Por tanto satisface simultáneamente ambas exigencias.
:::

::: {#sol-t1-0047}
<!-- CPM-T1-SOL-0047 -->
**Solución B5.**

Partimos de

$$
I_0=[3,4],
$$

porque $3^2=9<10<16=4^2$.

Primer punto medio:

$$
m_1=\frac72,
\qquad
\left(\frac72\right)^2=\frac{49}{4}>10.
$$

Conservamos

$$
I_1=\left[3,\frac72\right].
$$

Segundo punto medio:

$$
m_2=\frac{13}{4},
\qquad
\left(\frac{13}{4}\right)^2=\frac{169}{16}>10
$$

porque $169>160$. Luego

$$
I_2=\left[3,\frac{13}{4}\right].
$$

Tercer punto medio:

$$
m_3=\frac{25}{8},
\qquad
\left(\frac{25}{8}\right)^2=\frac{625}{64}<10
$$

porque $625<640$. Por tanto,

$$
I_3=\left[\frac{25}{8},\frac{13}{4}\right].
$$

Así,

$$
\boxed{\frac{25}{8}<\sqrt{10}<\frac{13}{4}.}
$$
:::

::: {#sol-t1-0048}
<!-- CPM-T1-SOL-0048 -->
**Solución B6.**

Por definición,

$$
\frac ab=ab^{-1}.
$$

La parte 5 de [Proposición 1.5](cpm-c01-01.md#prp-t1-0007) dice que $b^{-1}$ tiene el mismo signo que $b$. La parte 8 caracteriza el signo de un producto: es positivo cuando los factores tienen el mismo signo y negativo cuando tienen signos opuestos. Sustituyendo el signo de $b^{-1}$ por el de $b$ obtenemos exactamente

$$
\boxed{\frac ab>0
\iff
(a>0,b>0)\text{ o }(a<0,b<0)}
$$

y

$$
\boxed{\frac ab<0
\iff
(a>0,b<0)\text{ o }(a<0,b>0)}.
$$
:::
::: {#sol-t1-0049}
<!-- CPM-T1-SOL-0049 -->
**Solución B7.**

Queremos resolver

$$
\left|\frac{x-1}{x+2}\right|
\le
\frac{|x-3|}{2}.
$$

**1. Dominio y puntos críticos.** El denominador exige

$$
x\ne-2.
$$

Los argumentos de los valores absolutos se anulan en $x=1$ y $x=3$. Estos puntos, junto con el polo $-2$, deben registrarse aunque una transformación posterior produzca fronteras adicionales.

**2. Eliminación segura de denominadores y valores absolutos.** Para $x\ne-2$, $2|x+2|>0$. Multiplicamos sin cambiar el sentido:

$$
2|x-1|\le |x-3|\,|x+2|.
$$

Ambos lados son no negativos, así que elevar al cuadrado es una equivalencia:

$$
4(x-1)^2\le (x-3)^2(x+2)^2.
$$

Llevando todo a un lado y factorizando,

$$
(x-3)^2(x+2)^2-4(x-1)^2
=(x-4)(x+1)(x^2+x-8).
$$

Las raíces del factor cuadrático son

$$
r_- =\frac{-1-\sqrt{33}}2,
\qquad
r_+ =\frac{-1+\sqrt{33}}2.
$$

El orden relevante es

$$
r_-<-2<-1<r_+<3<4.
$$

**3. Análisis de signos.** Debemos resolver

$$
(x-4)(x+1)(x-r_-)(x-r_+)\ge0.
$$

Todos los ceros son simples, por lo que el signo alterna al atravesarlos. Como el polinomio es positivo para $x$ grande y positivo, resulta no negativo en

$$
(-\infty,r_-]\cup[-1,r_+]\cup[4,\infty).
$$

El punto excluido $x=-2$ se encuentra en una región que ya no pertenece a la solución, pero debe mantenerse fuera del dominio en todo momento.

**4. Extremos.** En $r_-$, $-1$, $r_+$ y $4$ se obtiene igualdad, y ninguno es un polo; por eso se incluyen.

Por consiguiente,

$$
\boxed{
(-\infty,\tfrac{-1-\sqrt{33}}2]
\cup
[-1,\tfrac{-1+\sqrt{33}}2]
\cup
[4,\infty)
}.
$$

La comprobación final respeta el dominio original y todos los extremos proceden de equivalencias algebraicas reversibles.
:::

#### Soluciones del nivel C

::: {#sol-t1-0050}
<!-- CPM-T1-SOL-0050 -->
**Solución C1.**

Sea

$$
s=\sup A.
$$

Como $a\le s$ para todo $a\in A$ y $c>0$,

$$
ca\le cs.
$$

Así, $cs$ es cota superior de $cA$.

Para demostrar que es la menor, sea $\varepsilon>0$. Como $s=\sup A$, existe $a\in A$ tal que

$$
s-\frac{\varepsilon}{c}<a\le s.
$$

Multiplicando por $c>0$,

$$
cs-\varepsilon<ca\le cs.
$$

Por la caracterización aproximativa del supremo,

$$
\boxed{\sup(cA)=c\sup A.}
$$
:::

::: {#sol-t1-0051}
<!-- CPM-T1-SOL-0051 -->
**Solución C2.**

Sea

$$
t=\sup(-A).
$$

Para todo $a\in A$, el número $-a$ pertenece a $-A$, luego

$$
-a\le t.
$$

Multiplicando por $-1$,

$$
a\ge -t.
$$

Así, $-t$ es cota inferior de $A$.

Si $\ell$ es cualquier cota inferior de $A$, entonces

$$
\ell\le a
$$

para todo $a\in A$, por lo que

$$
-a\le-\ell
$$

para todo $-a\in-A$. Así, $-\ell$ es cota superior de $-A$. Como $t$ es la menor de ellas,

$$
t\le-\ell,
$$

y, al multiplicar por $-1$,

$$
-t\ge\ell.
$$

Por tanto, $-t$ es la mayor cota inferior de $A$:

$$
\boxed{\inf A=-\sup(-A).}
$$
:::

::: {#sol-t1-0052}
<!-- CPM-T1-SOL-0052 -->
**Solución C3.**

Sea

$$
h=\frac{b-a}{2N+1}>0.
$$

Para cada $j=1,\dots,N$, por densidad de $\mathbb Q$ elegimos

$$
q_j\in\mathbb Q\cap
\bigl(a+(2j-2)h,\,a+(2j-1)h\bigr),
$$

y por densidad de los irracionales elegimos

$$
\xi_j\in(\mathbb R\setminus\mathbb Q)\cap
\bigl(a+(2j-1)h,\,a+2jh\bigr).
$$

Los subintervalos fueron escogidos en orden y son disjuntos. Por tanto,

$$
a<q_1<\xi_1<q_2<\xi_2<\cdots<q_N<\xi_N<a+2Nh<b.
$$

Esto demuestra la afirmación.
:::
::: {#sol-t1-0053}
<!-- CPM-T1-SOL-0053 -->
**Solución C4.**

La ecuación equivale primero a

$$
ax=c-b.
$$

Como $a\ne0$, el candidato natural es

$$
x_0=a^{-1}(c-b).
$$

En efecto,

$$
ax_0+b
=(aa^{-1})(c-b)+b
=c.
$$

Si $y$ es otra solución, entonces

$$
ay+b=c=ax_0+b.
$$

La cancelación aditiva da $ay=ax_0$, y la cancelación multiplicativa —válida porque $a\ne0$— da $y=x_0$. Por tanto,

$$
\boxed{x=a^{-1}(c-b)}
$$

es la solución única.
:::
::: {#sol-t1-0054}
<!-- CPM-T1-SOL-0054 -->
**Solución C5.**

Como $a,b\ge0$, también

$$
\sqrt a\ge0,
\qquad
\sqrt b\ge0,
$$

de modo que

$$
\sqrt a\,\sqrt b\ge0.
$$

Además,

$$
(\sqrt a\,\sqrt b)^2
=(\sqrt a)^2(\sqrt b)^2
=ab.
$$

El teorema de raíces cuadradas afirma que existe un **único** número no negativo cuyo cuadrado es $ab$. Como $\sqrt a\,\sqrt b$ tiene esas dos propiedades, debe coincidir con él:

$$
\boxed{\sqrt{ab}=\sqrt a\,\sqrt b.}
$$

La unicidad es el paso que legitima la identificación final.
:::

::: {#sol-t1-0055}
<!-- CPM-T1-SOL-0055 -->
**Solución C6.**

Resolvemos

$$
\frac{|x-2|}{|x+1|}\ge\frac{|x|}{2}.
$$

**1. Dominio.** Debe cumplirse

$$
x\ne-1.
$$

Los argumentos de los valores absolutos se anulan en $x=-1,0,2$; el primero es además un polo.

**2. Transformación equivalente.** Para $x\ne-1$, multiplicamos por $2|x+1|>0$:

$$
2|x-2|\ge |x|\,|x+1|.
$$

Ambos miembros son no negativos, por lo que podemos elevar al cuadrado sin introducir soluciones espurias:

$$
4(x-2)^2\ge x^2(x+1)^2.
$$

La diferencia factoriza como

$$
4(x-2)^2-x^2(x+1)^2
=-(x-1)(x+4)(x^2-x+4).
$$

El cuadrático satisface

$$
\Delta=(-1)^2-16=-15<0
$$

y tiene coeficiente principal positivo, así que

$$
x^2-x+4>0
$$

para todo real $x$.

Por tanto, la inecuación equivale a

$$
-(x-1)(x+4)\ge0,
$$

o

$$
(x-1)(x+4)\le0.
$$

Esto ocurre para

$$
-4\le x\le1.
$$

**3. Reincorporación del dominio.** Debemos eliminar $x=-1$.

Los extremos $-4$ y $1$ producen igualdad y son admisibles. En consecuencia,

$$
\boxed{[-4,-1)\cup(-1,1].}
$$

Los puntos $0$ y $2$ eran críticos para la forma original de los valores absolutos; la transformación mediante cuadrados los absorbió en una equivalencia global válida, pero registrarlos evita perder de vista la estructura original.
:::

::: {#sol-t1-0056}
<!-- CPM-T1-SOL-0056 -->
**Solución C7.**

Por el principio de intervalos encajados y el criterio de longitudes arbitrariamente pequeñas, cada familia tiene un único punto común. Llamémoslos $x$ para $(I_n)$ e $y$ para $(J_n)$.

Supongamos $x\ne y$ y sea

$$
\varepsilon=\frac{|x-y|}{3}>0.
$$

Elige una etapa $N$ en la que las longitudes de $I_N$ y $J_N$ sean menores que $\varepsilon$; podemos tomar el máximo de dos etapas si fuera necesario. Por hipótesis existe

$$
z\in I_N\cap J_N.
$$

Como $x,z\in I_N$ y $y,z\in J_N$,

$$
|x-z|<\varepsilon,
\qquad
|y-z|<\varepsilon.
$$

La desigualdad triangular produce

$$
|x-y|
\le |x-z|+|z-y|
<2\varepsilon
=\frac23|x-y|,
$$

contradicción. Luego $x=y$.
:::

#### Soluciones del nivel D

::: {#sol-t1-0057}
<!-- CPM-T1-SOL-0057 -->
**Solución D1.**

Tomemos $A=B=(0,1)$. Entonces

$$
\sup(A\cup B)=1,
\qquad
\sup A+\sup B=2,
$$

así que la fórmula propuesta es falsa.

La identidad correcta es

$$
\boxed{\sup(A\cup B)=\max\{\sup A,\sup B\}}.
$$

Sea $s$ el máximo del miembro derecho. Todo elemento de $A\cup B$ pertenece a uno de los dos conjuntos y, por tanto, es menor o igual que $s$; luego $s$ es cota superior de la unión.

Si $u$ es cualquier cota superior de $A\cup B$, entonces también es cota superior de $A$ y de $B$. Por ello

$$
\sup A\le u,
\qquad
\sup B\le u,
$$

y en consecuencia $s\le u$. Así $s$ es la menor cota superior.
:::
::: {#sol-t1-0058}
<!-- CPM-T1-SOL-0058 -->
**Solución D2.**

La cancelación de $x-1$ solo es válida bajo la hipótesis

$$
x-1\ne0.
$$

Si $x=1$, ambos miembros de la ecuación original son $0$, de modo que $x=1$ es una solución y se perdería al cancelar.

En el caso $x\ne1$ sí podemos cancelar y obtenemos

$$
x+2=3x-4,
$$

de donde $x=3$.

Por tanto,

$$
\boxed{x\in\{1,3\}}.
$$

Equivalentemente, restando los miembros y factorizando se llega a

$$
(x-1)(6-2x)=0,
$$

y la ley del producto nulo produce los mismos dos casos.
:::
::: {#sol-t1-0059}
<!-- CPM-T1-SOL-0059 -->
**Solución D3.**

La afirmación sin hipótesis adicional es falsa. Si

$$
A=\{0,1\},
\qquad
F=\{1\},
$$

entonces $\sup A=1$, pero $\sup(A\setminus F)=0$.

Ahora sea $s=\sup A$ y supongamos $s\notin F$. Como $A\setminus F\subseteq A$, el número $s$ es cota superior de $A\setminus F$.

Si $F=\varnothing$, no hay nada que probar. Supongamos $F\ne\varnothing$ y sea $m=\max F$. Como todos los elementos de $F$ son menores o iguales que $s$ y $s\notin F$, tenemos $m<s$.

Dado $\varepsilon>0$, toma

$$
\delta=\frac12\min\{\varepsilon,s-m\}>0.
$$

Por la caracterización aproximativa del supremo existe $a\in A$ tal que

$$
s-\delta<a\le s.
$$

Además $s-\delta>m$, por lo que $a\notin F$. Así $a\in A\setminus F$ y

$$
s-\varepsilon<a\le s.
$$

La caracterización aproximativa concluye

$$
\boxed{\sup(A\setminus F)=s=\sup A}.
$$
:::
::: {#sol-t1-0060}
<!-- CPM-T1-SOL-0060 -->
**Solución D4.**

El intervalo inicial tiene extremos racionales. El punto medio de dos racionales es racional, de modo que cada bisección vuelve a producir extremos racionales.

Cada paso divide la longitud por $2$; como $|I_0|=1$,

$$
|I_n|=2^{-n}.
$$

Los intervalos son cerrados, no vacíos y encajados, así que tienen un punto común en $\mathbb R$. Como sus longitudes pueden hacerse menores que cualquier número positivo, ese punto es único. La regla de elección mantiene a $\sqrt2$ dentro de todos ellos, luego

$$
\bigcap_n I_n=\{\sqrt2\}.
$$

Pero $\sqrt2\notin\mathbb Q$. Por tanto,

$$
\bigcap_n(I_n\cap\mathbb Q)=\varnothing.
$$

Los racionales siguen siendo densos —cada intervalo contiene racionales—, pero el punto común exigido por completitud puede faltar dentro de $\mathbb Q$.
:::
::: {#sol-t1-0061}
<!-- CPM-T1-SOL-0061 -->
**Solución D5.**

Resolvemos

$$
\frac{|x-2|+|x+1|}{|x-1|}\le3.
$$

**1. Dominio y puntos críticos.** El denominador exige

$$
x\ne1.
$$

Los argumentos cambian de signo en

$$
-1,\quad1,\quad2.
$$

Estos tres puntos dividen la recta en cuatro regiones.

**Caso 1: $x<-1$.**

$$
|x-2|=2-x,
\quad
|x+1|=-x-1,
\quad
|x-1|=1-x.
$$

Entonces

$$
\frac{1-2x}{1-x}\le3.
$$

Como $1-x>0$,

$$
1-2x\le3-3x
\iff
x\le2,
$$

lo cual es verdadero en todo el caso. Obtenemos $(-\infty,-1)$.

**Caso 2: $-1\le x<1$.**

El numerador vale

$$
(2-x)+(x+1)=3,
$$

y el denominador $1-x>0$. Así,

$$
\frac3{1-x}\le3
\iff
1\le1-x
\iff
x\le0.
$$

Dentro del caso obtenemos $[-1,0]$.

**Caso 3: $1<x<2$.**

El numerador sigue siendo $3$, pero ahora $|x-1|=x-1$:

$$
\frac3{x-1}\le3
\iff
1\le x-1
\iff
x\ge2.
$$

No hay soluciones en $(1,2)$.

**Caso 4: $x\ge2$.**

$$
|x-2|=x-2,
\quad
|x+1|=x+1,
\quad
|x-1|=x-1.
$$

Por tanto,

$$
\frac{2x-1}{x-1}\le3.
$$

Como $x-1>0$,

$$
2x-1\le3x-3
\iff
x\ge2,
$$

válido en todo el caso. Obtenemos $[2,\infty)$.

**Recomposición.**

$$
(-\infty,-1)\cup[-1,0]
=
(-\infty,0].
$$

El punto $x=1$ permanece excluido y no aparece en la solución. Finalmente,

$$
\boxed{(-\infty,0]\cup[2,\infty).}
$$

Los extremos $0$ y $2$ satisfacen la igualdad original, por lo que se incluyen.
:::

::: {#sol-t1-0062}
<!-- CPM-T1-SOL-0062 -->
**Solución D6.**

El argumento será válido una vez que dispongamos de continuidad y del teorema del valor intermedio. El problema es su **posición lógica** dentro de este libro.

En este capítulo todavía no hemos demostrado continuidad de $x^2$ ni el teorema del valor intermedio. Más aún, esos resultados posteriores se apoyarán en propiedades estructurales de $\mathbb R$ cuya raíz está precisamente en la completitud.

Usarlos ahora para justificar una consecuencia que estamos extrayendo de completitud invertiría la dirección de dependencia comprometida por el proyecto.

La vía autorizada en este capítulo es:

$$
\boxed{
\text{completitud}
\to
\alpha=\sup\{x\ge0:x^2<3\}
\to
\alpha^2=3.
}
$$

No afirmamos que la prueba con IVT sea matemáticamente falsa; afirmamos que es **prematura y circular respecto de nuestra arquitectura**.
:::

#### Soluciones del nivel E

::: {#sol-t1-0063}
<!-- CPM-T1-SOL-0063 -->
**Solución E1.**

Una elección elemental es

$$
A_1=[0,1],
\qquad
A_2=[0,1),
\qquad
A_3=(0,1],
\qquad
A_4=(0,1).
$$

Todos tienen supremo $1$. Además:

- $A_1$ tiene máximo $1$ y mínimo $0$;
- $A_2$ no tiene máximo y tiene mínimo $0$;
- $A_3$ tiene máximo $1$ y no tiene mínimo;
- $A_4$ no tiene máximo ni mínimo.

La pertenencia de los puntos frontera, no el valor del supremo o del ínfimo, decide la existencia de extremos alcanzados.
:::
::: {#sol-t1-0064}
<!-- CPM-T1-SOL-0064 -->
**Solución E2.**

Podemos tomar

$$
A=(-1,0),
\qquad
B=(-\infty,0).
$$

En ambos casos $0$ es la menor cota superior, así que

$$
\sup A=\sup B=0.
$$

El conjunto $A$ está acotado inferiormente y

$$
\inf A=-1.
$$

En cambio, $B$ no está acotado inferiormente: dado cualquier $m\in\mathbb R$, existe un elemento de $B$ menor que $m$. Por ello no puede existir un ínfimo real de $B$.

El ejemplo muestra que la existencia de un supremo es una propiedad unilateral: no implica acotación por abajo.
:::
::: {#sol-t1-0065}
<!-- CPM-T1-SOL-0065 -->
**Solución E3.**

La ecuación

$$
0x=0
$$

no determina un valor particular de $x$. Por el resultado $0x=0$, válido para todo $x\in F$, **cada elemento del cuerpo es una solución**.

Así, si el cuerpo contiene al menos dos elementos —y por definición $0\ne1$—, la ecuación tiene al menos las dos soluciones distintas

$$
x=0
\qquad\text{y}\qquad
x=1.
$$

Esto ya refuta la conclusión $x=1$ como solución única.

Ahora examinemos la notación $0/0$. La división fue definida por

$$
\frac ab:=ab^{-1}
$$

solo cuando

$$
b\ne0.
$$

Para formar $0/0$ necesitaríamos un inverso multiplicativo $0^{-1}$, es decir, un elemento $y$ tal que

$$
0y=1.
$$

Pero $0y=0$ para todo $y$, mientras que $0\ne1$. Tal inverso no existe. Por eso

$$
\boxed{\frac00\text{ no está definido}.}
$$

La identidad

$$
\frac aa=1
$$

solo fue demostrada bajo la hipótesis $a\ne0$. Sustituir $a=0$ borra precisamente la condición que hace legal la división.

El **primer paso ilegítimo** de la cadena es, por tanto,

$$
0x=0
\quad\Longrightarrow\quad
x=\frac00,
$$

porque intenta dividir ambos miembros por un elemento que no posee inverso multiplicativo.
:::
::: {#sol-t1-0066}
<!-- CPM-T1-SOL-0066 -->
**Solución E4.**

Para $k\in\mathbb N_{>0}$ definamos

$$
I_{2k}=
\left[0,\frac1k\right],
\qquad
I_{2k-1}=
\left[1,1+\frac1k\right].
$$

Todos son intervalos cerrados y no vacíos, y sus longitudes son $1/k$, que pueden hacerse menores que cualquier $\varepsilon>0$.

Sin embargo, un punto que perteneciera a todos los intervalos debería pertenecer simultáneamente a $I_2=[0,1]$ y a todos los intervalos impares que se concentran junto a $1$, y también a $I_4=[0,1/2]$; de hecho, para $k\ge2$, los intervalos pares están contenidos en $[0,1/2]$ mientras los impares están contenidos en $[1,2]$. Por tanto,

$$
\bigcap_n I_n=\varnothing.
$$

La familia no es encajada: por ejemplo, $I_1=[1,2]$ e $I_2=[0,1]$ no satisfacen $I_2\subseteq I_1$. No se viola ninguna hipótesis del teorema porque precisamente falta el encajamiento.
:::
::: {#sol-t1-0067}
<!-- CPM-T1-SOL-0067 -->
**Solución E5.**

Como $1\in S_{\mathbb Q}$, tenemos $3\in T$, así que $T$ es no vacío. Además $2$ es cota superior de $S_{\mathbb Q}$, por lo que

$$
2q+1\le5
$$

para todo $q\in S_{\mathbb Q}$; así, $5$ es una cota superior racional de $T$.

Supongamos ahora que $t\in\mathbb Q$ fuese

$$
t=\sup_{\mathbb Q}T.
$$

Definamos

$$
s=\frac{t-1}{2}\in\mathbb Q.
$$

Para todo $q\in S_{\mathbb Q}$, de $2q+1\le t$ se sigue $q\le s$, así que $s$ es cota superior racional de $S_{\mathbb Q}$.

Si $u$ es cualquier cota superior racional de $S_{\mathbb Q}$, entonces $2u+1$ es cota superior racional de $T$. Como $t$ es la menor de estas cotas,

$$
t\le2u+1,
$$

y por tanto $s\le u$. Así $s$ sería el supremo racional de $S_{\mathbb Q}$, contradiciendo el resultado del capítulo.

Luego $T$ no tiene supremo en $\mathbb Q$.
:::

#### Soluciones del nivel F

::: {#sol-t1-0068}
<!-- CPM-T1-SOL-0068 -->
**Solución F1.**

Como $a\le s$ para todo $a\in A$,

$$
a+c\le s+c,
$$

de modo que $s+c$ es cota superior de $A+c$.

Sea ahora $\varepsilon>0$. Como $s=\sup A$, existe $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Sumando $c$,

$$
(s+c)-\varepsilon<a+c\le s+c.
$$

El punto $a+c$ pertenece a $A+c$, así que la caracterización aproximativa del supremo da

$$
\boxed{\sup(A+c)=s+c}.
$$
:::
::: {#sol-t1-0069}
<!-- CPM-T1-SOL-0069 -->
**Solución F2.**

Define

$$
R=
\max\left\{
M_1,\dots,M_r,
\frac1{\varepsilon_1},\dots,\frac1{\varepsilon_s}
\right\}.
$$

Por la propiedad arquimediana existe $n\in\mathbb N_{>0}$ con $n>R$. Entonces $n>M_i$ para todo $i$ y

$$
n>\frac1{\varepsilon_j}
$$

para todo $j$. Como $n,\varepsilon_j>0$, esto último equivale a $1/n<\varepsilon_j$. Una sola elección satisface todas las restricciones.
:::
::: {#sol-t1-0070}
<!-- CPM-T1-SOL-0070 -->
**Solución F3.**

Como $b-a>0$, por la propiedad arquimediana podemos elegir $n\in\mathbb N_{>0}$ tal que

$$
n>\max\left\{N,\frac1{b-a}\right\}.
$$

Entonces $n>N$ y

$$
na+1<nb.
$$

Por el lema de encajonamiento entero existe $k\in\mathbb Z$ con

$$
k\le na<k+1.
$$

Tomando $m=k+1$ obtenemos

$$
na<m\le na+1<nb.
$$

Dividiendo por $n>0$,

$$
\boxed{a<\frac mn<b},
$$

con el denominador además sujeto a $n>N$.
:::
::: {#sol-t1-0071}
<!-- CPM-T1-SOL-0071 -->
**Solución F4.**

Cada bisección divide la longitud por $2$. Si $L_0=1$, entonces

$$
L_n=2^{-n};
$$

esto puede formalizarse por inducción.

Queremos

$$
2^{-n}<\frac1{100},
$$

equivalentemente $2^n>100$. Como

$$
2^6=64\le100<128=2^7,
$$

el menor valor es

$$
\boxed{n=7}.
$$

En esa etapa obtenemos un intervalo racional cerrado $[a_7,b_7]$ tal que

$$
\sqrt7\in[a_7,b_7]
$$

y

$$
b_7-a_7=\frac1{128}<\frac1{100}.
$$

Ese es un certificado exacto de incertidumbre, independientemente de que hayamos escrito los extremos.
:::
::: {#sol-t1-0072}
<!-- CPM-T1-SOL-0072 -->
**Solución F5.**

Por conmutatividad del producto, $1a=a$. Entonces

$$
\begin{aligned}
a+(-1)a
&=1a+(-1)a\\
&=(1+(-1))a && \text{(distributividad)}\\
&=0a && \text{(inverso aditivo de }1\text{)}\\
&=0.
\end{aligned}
$$

Así, $(-1)a$ es un inverso aditivo de $a$. Por unicidad,

$$
\boxed{(-1)a=-a}.
$$

Tomando $a=-1$ obtenemos

$$
(-1)(-1)=-(-1)=1,
$$

donde la última igualdad usa que el inverso aditivo del inverso de $1$ vuelve a ser $1$.
:::

#### Soluciones del nivel G

::: {#sol-t1-0073}
<!-- CPM-T1-SOL-0073 -->
**Solución G1.**

Sea

$$
\alpha=\sup A,
\qquad
\beta=\sup B.
$$

Primero comprobamos que $\alpha+\beta$ es cota superior de $A+B$. Si $a\in A$ y $b\in B$, entonces

$$
a\le\alpha,
\qquad
b\le\beta,
$$

y sumando,

$$
a+b\le\alpha+\beta.
$$

Ahora debemos demostrar que ninguna cota menor funciona. Sea $\varepsilon>0$. Por la caracterización aproximativa del supremo existen $a\in A$ y $b\in B$ tales que

$$
\alpha-\frac\varepsilon2<a\le\alpha,
$$

$$
\beta-\frac\varepsilon2<b\le\beta.
$$

Sumando,

$$
\alpha+\beta-\varepsilon<a+b\le\alpha+\beta.
$$

Como $a+b\in A+B$, la caracterización aproximativa vuelve a decir que

$$
\boxed{\sup(A+B)=\alpha+\beta=\sup A+\sup B.}
$$

La completitud interviene para garantizar la existencia de $\alpha$ y $\beta$; el resto es orden y la caracterización del supremo.
:::

::: {#sol-t1-0074}
<!-- CPM-T1-SOL-0074 -->
**Solución G2.**

La condición de separación es

$$
\ell<u
\qquad
\text{para todo }\ell\in L\text{ y todo }u\in U.
$$

Como $U\ne\varnothing$, elegimos $u_0\in U$. Para todo $\ell\in L$,

$$
\ell<u_0,
$$

de modo que $u_0$ es cota superior de $L$. Como $L\ne\varnothing$, completitud garantiza

$$
c=\sup L.
$$

Por definición de supremo,

$$
\ell\le c
$$

para todo $\ell\in L$.

Por otro lado, cada $u\in U$ es cota superior de $L$, porque todo $\ell\in L$ satisface $\ell<u$. Como $c$ es la menor cota superior,

$$
c\le u
$$

para todo $u\in U$.

Así,

$$
\boxed{\ell\le c\le u}
$$

para todos $\ell\in L$, $u\in U$.

Como $L\cup U=\mathbb R$, el real $c$ pertenece a uno de los dos conjuntos. Son disjuntos, así que pertenece exactamente a uno.

- Si $c\in L$, como $c$ domina a todo elemento de $L$, tenemos $c=\max L$.
- Si $c\in U$, como $c\le u$ para todo $u\in U$, tenemos $c=\min U$.

Por tanto ocurre exactamente una de las dos posibilidades:

$$
\boxed{c=\max L\quad\text{o}\quad c=\min U.}
$$

Esta propiedad traduce completitud en lenguaje de cortes: una separación ordenada de la recta posee un punto frontera real.
:::

::: {#sol-t1-0075}
<!-- CPM-T1-SOL-0075 -->
**Solución G3.**

Sea $a>0$ y

$$
S=\{x\ge0:x^3<a\}.
$$

La estrategia replica, con un grado algebraico mayor, la construcción de raíces cuadradas: completitud produce un candidato frontera y dos perturbaciones descartan que su cubo quede por debajo o por encima de $a$.

**1. No vacuidad y acotación.**

El número

$$
t=\frac{a}{1+a}
$$

es positivo y pertenece a $S$. En efecto, si $a\ge1$, entonces $0<t<1$ y $t^3<1\le a$; si $0<a<1$, entonces $0<t<a<1$, por lo que $t^3<a^3<a$.

Además, $a+1$ es cota superior de $S$. Si $x\ge a+1$, entonces $x>1$ y $x>a$ cuando $a<1$, o $x>a\ge1$ cuando $a\ge1$; en ambos casos $x^3>a$, de modo que tal $x$ no pertenece a $S$.

Por completitud existe

$$
\alpha=\sup S.
$$

Como $t\in S$ y $t>0$, tenemos $\alpha>0$.

**2. No puede ocurrir $\alpha^3<a$.**

Supongamos

$$
\alpha^3<a
$$

y definamos

$$
\delta=a-\alpha^3>0.
$$

Elegimos

$$
h=\frac12\min\left\{1,\frac{\delta}{3\alpha^2+3\alpha+1}\right\}>0.
$$

Entonces $h<1$ y

$$
h(3\alpha^2+3\alpha+1)<\delta.
$$

Como $h<1$,

$$
3\alpha h\le3\alpha,
\qquad
h^2<1,
$$

y por tanto

$$
\begin{aligned}
(\alpha+h)^3
&=\alpha^3+h(3\alpha^2+3\alpha h+h^2)\\
&<\alpha^3+h(3\alpha^2+3\alpha+1)\\
&<\alpha^3+\delta\\
&=a.
\end{aligned}
$$

Así $\alpha+h\in S$, pero $\alpha+h>\alpha$, contradiciendo que $\alpha$ sea cota superior.

**3. No puede ocurrir $\alpha^3>a$.**

Supongamos ahora

$$
\alpha^3>a
$$

y pongamos

$$
\delta=\alpha^3-a>0.
$$

Elegimos

$$
h=\frac12\min\left\{\alpha,\frac{\delta}{3\alpha^2}\right\}>0
$$

y definimos

$$
c=\alpha-h.
$$

Como $h<\alpha$, $c>0$. Además,

$$
\alpha^3-c^3
=3\alpha^2h-3\alpha h^2+h^3.
$$

Como $0<h<\alpha$, el término

$$
-3\alpha h^2+h^3=h^2(h-3\alpha)<0,
$$

de modo que

$$
\alpha^3-c^3<3\alpha^2h<\delta.
$$

Por tanto,

$$
c^3>\alpha^3-\delta=a.
$$

Si $x\in S$ y $x\ge c$, como $x,c\ge0$, la identidad

$$
x^3-c^3=(x-c)(x^2+xc+c^2)\ge0
$$

justifica directamente que $x^3\ge c^3>a$. Esto contradice la condición $x^3<a$ que define a $S$. Así todo $x\in S$ satisface $x<c$. Por tanto $c$ es una cota superior de $S$, pero

$$
c<\alpha,
$$

contradiciendo que $\alpha$ sea la menor cota superior.

Los dos casos estrictos son imposibles. Por tricotomía,

$$
\boxed{\alpha^3=a.}
$$

**4. Unicidad.**

Sean $0<u<v$. Entonces

$$
v^3-u^3=(v-u)(v^2+uv+u^2)>0.
$$

Así el cubo es estrictamente creciente sobre los reales no negativos. Por consiguiente, no pueden existir dos números no negativos distintos con cubo $a$.

Hemos demostrado, sin continuidad, que para todo $a>0$ existe un único $\alpha>0$ tal que

$$
\boxed{\alpha^3=a.}
$$

La prueba muestra de nuevo la arquitectura central del capítulo:

$$
\boxed{
\text{conjunto de aproximantes}
\to
\text{supremo}
\to
\text{perturbaciones}
\to
\text{identificación de la frontera}.
}
$$
:::

### Auditoría del banco

Antes de cerrar el capítulo, conviene verificar el contrato de esta sección.

- Ejercicios publicados: **40**.
- Soluciones publicadas: **40**.
- Correspondencia `EXR-0036--0075` / `SOL-0036--0075`: **completa**.
- Distribución A–G: $7+7+7+6+5+5+3=40$.
- Tipologías `CONCEPTUAL`, `PROOF`, `COUNTEREXAMPLE`, `DISCOVERY`, `SYNTHESIS` y `GEOMETRY`: presentes.
- Inecuaciones racionales con valor absoluto de alta complejidad: **3**, en B7, C6 y D5.
- Reproducciones literales de demostraciones ya resueltas en el desarrollo: **eliminadas del banco**. Cuando una idea reaparece, exige transferencia, generalización, diagnóstico o combinación de herramientas.
- Capa axiomática: clasificación axioma/definición/resultado (A4), identidad y orden de recíprocos (B3), signo de cocientes (B6), ecuación afín con existencia y unicidad (C4), cancelación con solución perdida (D2), división por cero (E3) y reconstrucción estructural de $(-1)a=-a$ (F5).
- Transferencias de completitud: supremos bajo unión y traslación, eliminación finita de puntos, transporte del hueco racional, intervalos racionales encajados y propiedad de corte.
- Problemas F: traslación del supremo, elección arquimediana simultánea, densidad con control de denominador, presupuesto de bisección y reconstrucción axiomática: **5/5**.
- Problemas G de síntesis: suma de conjuntos, propiedad de corte y construcción de una raíz cúbica mediante supremo: **3/3**.
- Dependencias de `T1-C03` o posteriores: **ninguna**.

La política pedagógica del banco queda así alineada con la progresión del capítulo: **primero modelar la justificación, después retirar el andamiaje y exigir transferencia**.

---

[← Anterior](cpm-c01-11.md) · [Índice del capítulo](los-numeros-reales-orden-valor-absoluto-desigualdades-y-completitud.md) · [Siguiente →](funciones-reales-estructura-composicion-inversas-y-graficas.md)
