---
title: "El método de Diofanto y la parametrización racional de las ternas pitagóricas"
description: "Del problema II.8 de la Aritmética de Diofanto a los puntos racionales de la circunferencia y las ternas pitagóricas."
content-id: MA-ART-0005
content-type: article
status: published
draft: false
date-created: 2026-09-15
date-modified: 2026-09-17
areas:
  - algebra
  - geometria
  - teoria-de-numeros
level: introductorio
topics:
  - diofanto
  - ternas-pitagoricas
  - parametrizacion-racional
  - circunferencia-unidad
  - historia-de-las-matematicas
prerequisites: []
related: []
provenance:
  type: synthesis
license: GFDL-1.3-or-later
---

**¿Cómo dividir un cuadrado en dos cuadrados?** En el problema II.8 de la *Arithmetica*, Diofanto de Alejandría propone dividir el número $16=4^2$ en dos números que sean, a su vez, cuadrados. Su elección algebraica permite encontrar una solución racional. Vamos a reproducir primero ese cálculo y, después, a **generalizarlo con notación moderna**. Así aparecerán las ternas pitagóricas, los puntos racionales de una circunferencia y una fórmula clásica asociada con Euclides.

::: {.callout-important}
## Dos niveles de lectura
La resolución particular de $16$ pertenece a Diofanto. La pendiente variable $m$, la interpretación mediante rectas y la parametrización general que desarrollamos a continuación son una **reconstrucción matemática moderna** de su procedimiento, no una transcripción literal de su texto.
:::

## 1. El problema original: dividir $16$ en dos cuadrados

Buscamos números racionales positivos $x$ e $y$ tales que

$$
x^2+y^2=16.
$$

Diofanto elige como raíz del segundo cuadrado una expresión que, en nuestra notación, se escribe

$$
y=2x-4.
$$

Sustituimos esta elección en la condición del problema:

$$
\begin{aligned}
x^2+(2x-4)^2&=16,\\
x^2+4x^2-16x+16&=16,\\
5x^2-16x&=0,\\
x(5x-16)&=0.
\end{aligned}
$$

La raíz $x=0$ no sirve para la descomposición buscada en **dos cuadrados positivos**. La otra raíz proporciona

$$
x=\frac{16}{5},\qquad y=2\cdot\frac{16}{5}-4=\frac{12}{5}.
$$

Por tanto,

$$
\boxed{16=\left(\frac{16}{5}\right)^2+\left(\frac{12}{5}\right)^2}
$$

porque $256/25+144/25=400/25=16$.

**Pregunta para pensar.** ¿Por qué la elección $2x-4$, que parece complicar el problema, hace desaparecer el término constante después de sustituir?

## 2. El truco: partir de una solución conocida

La ecuación $x^2+y^2=16$ ya tiene una solución sencilla:

$$
(0,-4).
$$

La recta $y=2x-4$ pasa precisamente por ese punto. Al sustituirla en la ecuación de la circunferencia, encontramos dos intersecciones: la conocida, asociada con $x=0$, y la nueva, asociada con $x=16/5$.

::: {.callout-tip}
## Idea clave
Conocer un punto racional de una circunferencia permite buscar otro trazando por él una recta de pendiente racional. Como una de las intersecciones ya es conocida, la ecuación cuadrática se factoriza y deja una ecuación lineal para la segunda. La representación mediante una recta es nuestra lectura geométrica moderna del cálculo.
:::

## 3. Generalización: sustituir el $2$ por una pendiente racional

Sea $c>0$ un número racional. Buscamos soluciones racionales de

$$
x^2+y^2=c^2.
$$

Ahora reemplazamos la elección particular de Diofanto por la familia de rectas

$$
y=mx-c,\qquad m\in\mathbb{Q}.
$$

Todas pasan por el punto conocido $(0,-c)$. Sustituyendo,

$$
\begin{aligned}
x^2+(mx-c)^2&=c^2,\\
(1+m^2)x^2-2mcx&=0,\\
x\bigl((1+m^2)x-2mc\bigr)&=0.
\end{aligned}
$$

La solución $x=0$ representa el punto desde el que empezamos. Para hallar la segunda intersección, si $m\ne0$, tomamos el otro factor y obtenemos

$$
\boxed{x=\frac{2mc}{1+m^2}}.
$$

Sustituyendo en $y=mx-c$,

$$
\boxed{y=\frac{c(m^2-1)}{1+m^2}}.
$$

El denominador $1+m^2$ nunca se anula para $m$ racional. Por ello, **cada pendiente racional** produce un punto racional de la circunferencia. Para $m=0$, ambas intersecciones coinciden en $(0,-c)$; si buscamos dos raíces positivas, basta elegir $m>1$.

**Comprobación.** Para $c=4$ y $m=2$ reaparecen exactamente $x=16/5$ e $y=12/5$, los valores encontrados en el problema de Diofanto.

## 4. La circunferencia unidad y sus puntos racionales

Dividamos las coordenadas por $c$:

$$
X=\frac{x}{c},\qquad Y=\frac{y}{c},\qquad X^2+Y^2=1.
$$

Obtenemos la **parametrización racional**

$$
\boxed{(X,Y)=\left(\frac{2m}{1+m^2},\frac{m^2-1}{1+m^2}\right)},\qquad m\in\mathbb{Q}.
$$

No se trata solo de un método para construir ejemplos. Si $(X,Y)$ es un punto racional de la circunferencia y $X\ne0$, la recta que une $(0,-1)$ con ese punto tiene pendiente racional

$$
m=\frac{Y+1}{X}.
$$

Por tanto, la fórmula recupera **todos los puntos racionales de la circunferencia con $X\ne0$**. El punto $(0,-1)$ también aparece al tomar $m=0$; el único punto no representado por una pendiente finita es $(0,1)$, al que corresponde la recta vertical $X=0$. En el primer cuadrante, $m>1$ produce $X,Y>0$.

::: {.callout-note}
## Del ejemplo al resultado general
¿Qué se conserva al pasar del caso concreto $16$ a un cuadrado racional cualquiera? ¿Qué papel cumple el punto inicial $(0,-c)$ y por qué necesitamos que $m$ sea racional?
:::

## 5. De puntos racionales a ternas enteras

Escribamos una pendiente racional positiva mayor que $1$ como

$$
m=\frac pq,\qquad p,q\in\mathbb Z_{>0},\quad p>q.
$$

En la circunferencia unidad, las coordenadas son

$$
X=\frac{2pq}{p^2+q^2},\qquad
Y=\frac{p^2-q^2}{p^2+q^2}.
$$

Si ahora **elegimos el radio** $c=p^2+q^2$ —equivalentemente, multiplicamos las coordenadas anteriores por su denominador común—, obtenemos tres enteros positivos:

$$
\boxed{A=2pq,\qquad B=p^2-q^2,\qquad C=p^2+q^2.}
$$

Son una terna pitagórica porque

$$
\begin{aligned}
A^2+B^2
&=(2pq)^2+(p^2-q^2)^2\\
&=4p^2q^2+p^4-2p^2q^2+q^4\\
&=(p^2+q^2)^2=C^2.
\end{aligned}
$$

Esta es la forma habitual de la **fórmula de Euclides**. El lema 1 que acompaña a *Elementos* X.29 documenta una construcción antigua de cuadrados cuya suma también es un cuadrado; la fórmula que usamos aquí está escrita en notación algebraica moderna.

**Ejemplo.** Si $p=2$ y $q=1$, entonces

$$
(A,B,C)=(4,3,5),\qquad 4^2+3^2=5^2.
$$

**Precisión importante.** Cuando partimos de un cuadrado fijo $c^2$, no podemos cambiar su radio sin modificar el problema. Para generar ternas enteras hemos pasado deliberadamente a la circunferencia unidad y después la hemos escalado al radio $C=p^2+q^2$.

## 6. ¿Cuándo es primitiva una terna?

Una terna pitagórica $(A,B,C)$ es **primitiva** cuando $\gcd(A,B,C)=1$; es decir, sus tres términos no comparten un divisor entero mayor que $1$.

**Proposición.** Sean $p>q>0$ enteros. La terna

$$
(2pq,\ p^2-q^2,\ p^2+q^2)
$$

es primitiva **si y solo si**

$$
\boxed{\gcd(p,q)=1\quad\text{y}\quad p,q\text{ tienen distinta paridad}.}
$$

**Demostración.** Si $d=\gcd(p,q)>1$, entonces $d^2$ divide las tres entradas de la terna. Si $p$ y $q$ son impares, los tres términos son pares. En cualquiera de estos dos casos la terna no es primitiva.

Recíprocamente, supongamos que $p,q$ son coprimos y de distinta paridad. Entonces $C=p^2+q^2$ es impar. Si un primo impar $r$ dividiera los tres términos, en particular dividiría $2pq$ y $C$; como $r$ es impar, dividiría $p$ o $q$. Si $r\mid p$, de $r\mid p^2+q^2$ se deduce $r\mid q$, contradicción; el otro caso es simétrico. Tampoco $2$ puede dividir a los tres términos, pues $C$ es impar. No existe ningún divisor primo común: la terna es primitiva. $\square$

**No-ejemplo.** $p=3,q=1$ genera $(6,8,10)$, que satisface Pitágoras pero no es primitiva: su máximo común divisor es $2$. En cambio, $p=2,q=1$ genera $(4,3,5)$, que sí lo es.

### ¿Se obtienen todas las ternas primitivas?

Sí, salvo el orden de los catetos. Consideremos una terna primitiva positiva $(A,B,C)$ y llamemos $A$ a su cateto par. El otro cateto $B$ y la hipotenusa $C$ son impares. Definamos

$$
u=\frac{C+B}{2},\qquad v=\frac{C-B}{2}.
$$

Como $0<B<C$, ambos son enteros positivos. Además,

$$
uv=\frac{C^2-B^2}{4}=\left(\frac A2\right)^2.
$$

Los enteros $u$ y $v$ son coprimos: un divisor común dividiría tanto $u+v=C$ como $u-v=B$, y $\gcd(B,C)=1$: si un primo dividiera $B$ y $C$, dividiría $A^2=C^2-B^2$ y, por tanto, también $A$, contradiciendo la primitividad de la terna. Puesto que el producto de dos enteros positivos coprimos es un cuadrado, **cada factor es un cuadrado**. Existen, pues, enteros $p>q>0$ tales que $u=p^2$ y $v=q^2$. De aquí,

$$
C=p^2+q^2,\qquad B=p^2-q^2,\qquad A=2pq.
$$

La primitividad exige, según la proposición anterior, que $p,q$ sean coprimos y de distinta paridad. Queda demostrada la afirmación. $\square$

**Y las ternas no primitivas:** toda terna pitagórica positiva es un múltiplo entero $k\ge1$ de una primitiva. Por tanto, la descripción completa es

$$
\boxed{(A,B,C)=k\bigl(2pq,\ p^2-q^2,\ p^2+q^2\bigr)},
$$

con $k\in\mathbb Z_{>0}$, $p>q>0$, $\gcd(p,q)=1$ y paridades distintas, salvo intercambio de los catetos.

## 7. Exploración interactiva

Modifica $p$ y $q$. El generador garantiza $p>q$ y muestra la identidad pitagórica, la pendiente racional, el punto correspondiente de la circunferencia unidad y la condición de primitividad. **Intenta encontrar una terna no primitiva con $p,q$ coprimos:** ¿qué sucede si ambos son impares?

<!-- Publicación: cargar diofanto-triples.js una sola vez desde la plantilla de la web.
     Este Markdown no ejecuta scripts en línea: el HTML de abajo ofrece una vista
     estática matemáticamente correcta si el JS no está disponible. -->
<div class="diofanto-widget" data-diofanto-widget style="border:1px solid #c5cbd3; padding:1.25rem; border-radius:12px; margin:1.5rem 0; background:var(--background-secondary,#f8fafc); color:var(--text-normal,#17202a);">
  <h3 style="margin:0 0 1rem;">Generador de ternas pitagóricas</h3>
  <label style="display:block;">Parámetro p: <strong data-p-value>2</strong>
    <input data-p type="range" min="2" max="20" value="2" step="1" style="display:block; width:100%; margin:0.25rem 0 1rem;" />
  </label>
  <label style="display:block;">Parámetro q: <strong data-q-value>1</strong>
    <input data-q type="range" min="1" max="1" value="1" step="1" style="display:block; width:100%; margin:0.25rem 0 1rem;" />
  </label>
  <div style="line-height:1.8;">
    <div><strong data-identity>4² + 3² = 5²</strong></div>
    <div>Pendiente: <span data-slope>m = 2/1</span></div>
    <div>Punto racional (circunferencia unidad): <span data-point>(4/5, 3/5)</span></div>
    <div>mcd(p,q): <span data-gcd>1</span></div>
    <div><strong data-status>Terna primitiva</strong></div>
  </div>
  <svg data-triangle viewBox="0 0 260 250" width="260" height="250" role="img" aria-label="Triángulo rectángulo de catetos 4 y 3 e hipotenusa 5" style="display:block; max-width:100%; margin:1rem auto; overflow:visible;">
    <polygon data-polygon points="55,210 205,210 55,97.5" fill="#dbeafe" stroke="#2563eb" stroke-width="2" />
    <polyline data-right-angle points="55,198 67,198 67,210" fill="none" stroke="#2563eb" stroke-width="1.5" />
    <text data-label-a x="130" y="231" fill="currentColor" font-size="14" text-anchor="middle">4</text>
    <text data-label-b x="38" y="153.75" fill="currentColor" font-size="14" text-anchor="middle">3</text>
    <text data-label-c x="143" y="144.75" fill="currentColor" font-size="14" text-anchor="middle">5</text>
  </svg>
  <p data-fallback style="font-size:0.9em; margin:0.4rem 0;">Vista estática: el generador interactivo requiere que la web cargue su archivo JavaScript.</p>
  <p data-announcement role="status" aria-live="polite" aria-atomic="true" style="position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0;">Parámetros 2 y 1. Terna 4, 3, 5. Primitiva.</p>
  <p style="font-size:0.85em; margin:0; opacity:0.85;">El dibujo respeta las proporciones de los catetos. El máximo de q se ajusta a p − 1; se muestran también la pendiente reducida y las coordenadas racionales simplificadas.</p>
  <noscript><p>Para modificar los parámetros, habilita JavaScript en la versión web.</p></noscript>
</div>

## 8. De Diofanto a Fermat

Este problema tiene una historia posterior singular. Pierre de Fermat anotó en el margen de su ejemplar de la traducción latina de la *Arithmetica* publicada por **Claude-Gaspard Bachet en 1621** que, a diferencia de lo que sucede con los cuadrados, una potencia de exponente entero mayor que $2$ no puede descomponerse en la suma de dos potencias positivas del mismo exponente. Afirmó haber hallado una demostración que no cabía en el margen.

La observación está asociada precisamente al **problema II.8**. El ejemplar anotado por Fermat no se conserva; el texto de su observación fue publicado póstumamente por su hijo Samuel en la edición de **1670**. Hoy conocemos la afirmación como el *Último Teorema de Fermat*.

El contraste matemático es elocuente: la ecuación cuadrática $x^2+y^2=z^2$ tiene infinitas soluciones enteras positivas, mientras que el Último Teorema de Fermat afirma que $x^n+y^n=z^n$ no tiene ninguna solución en enteros positivos cuando $n>2$. La identidad pitagórica demostrada arriba **no constituye una demostración de ese teorema**.

## 9. Para investigar y demostrar

1. Repite el problema de Diofanto con $c=5$ y $m=3/2$. Comprueba por sustitución los dos valores obtenidos.
2. Explica por qué el factor $x=0$ aparece al intersectar la circunferencia con $y=mx-c$. ¿Qué pasa si $m=0$?
3. Prueba directamente que la parametrización de la circunferencia satisface $X^2+Y^2=1$ para todo $m\in\mathbb Q$.
4. Determina las ternas que resultan de $(p,q)=(3,2)$ y $(3,1)$. Comprueba qué condición de primitividad falla en el segundo caso.
5. Investiga si la terna $(9,12,15)$ puede obtenerse **sin** factor $k$ utilizando la fórmula $2pq,p^2-q^2,p^2+q^2$ con parámetros enteros. ¿Qué aporta $k$ a la descripción completa?

## 10. Qué hemos aprendido

La decisión de Diofanto de expresar una incógnita mediante la otra transforma un problema cuadrático en uno lineal. Al reconstruir esa idea con pendientes racionales, obtenemos puntos racionales de una circunferencia; al escalar convenientemente, aparecen las ternas pitagóricas. La relación entre **un punto conocido, una recta racional y un segundo punto racional** ofrece una puerta de entrada a métodos más generales de la teoría de números y la geometría algebraica, aunque esos desarrollos requieren herramientas adicionales.

## Fuentes y lecturas

- Diofanto, *Arithmetica*, II.8: traducción y comentario de Henry Mendell, California State University, Los Angeles, a partir de la edición de Tannery (1893). [Consultar II.8–10](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Diophantus/Arithmetica/Diophantus.II.8-10.html).
- Euclides, *Elementos*, libro X, proposición 29, lema 1; edición digital y comentario de David E. Joyce. [Consultar el texto y el lema](https://mathcs.clarku.edu/~djoyce/elements/bookX/propX29.html).
- Frank J. Swetz, «Mathematical Treasure: Bachet's Arithmetic of Diophantus», *Convergence*, Mathematical Association of America. [Consultar el estudio y la edición de 1670](https://old.maa.org/press/periodicals/convergence/mathematical-treasure-bachets-arithmetic-of-diophantus).

<script src="../assets/js/diofanto-triples.js" defer></script>
