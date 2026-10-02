---
title: 'Tratado moderno de Álgebra — Capítulo 28: Propiedades arquimedianas'
description: Capítulo del Tratado moderno de Álgebra dedicado a numerales internos, arquimedianidad, cambios de escala y recíprocos pequeños.
author: Gustav A. Tachek
content-id: MA-BCH-0136
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-10-02'
date-modified: '2026-10-02'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-ordenadas
- propiedad-arquimediana
- numerales
prerequisites:
- MA-BCH-0135
related:
- MA-BOK-0007
- MA-BCH-0135
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 28 — Propiedades arquimedianas

## 28.0. El problema: comparar escalas finitas sin introducir completitud

Los capítulos 25–27 han construido el orden compatible con las operaciones hasta llegar a los cuerpos ordenados. Falta aislar una propiedad de **escala** que no forma parte de la definición de cuerpo ordenado: la posibilidad de sobrepasar cualquier elemento mediante un número finito de copias de una unidad positiva, o, en formulaciones equivalentes, de hacer suficientemente grande un múltiplo natural de un elemento positivo.

Este capítulo tratará esa cuestión como una propiedad **algebraico-ordenada**. No introducirá supremos, ínfimos, completitud, convergencia, topología, métrica ni continuidad. La completitud pertenece al *Tratado de análisis*; aquí sólo se construirá la infraestructura algebraica que Análisis podrá reutilizar.

La dificultad fundacional previa es tipológica. Un natural $n\in\mathbb N$ no es literalmente un elemento de un anillo $R$. Antes de escribir expresiones como “$n1_R$” debemos construir una aplicación canónica de numerales mediante recursión sobre $\mathbb N$ y demostrar las leyes que autorizan esa lectura.

```text
naturales + recursión
        │
        ▼
numerales internos ν_R(n)
        │
        ├── aritmética de los numerales
        └── orden de los numerales cuando 0 < 1_R
                 │
                 ▼
        propiedad arquimediana
                 │
        ┌────────┴────────┐
        │                 │
  forma de escala    cuerpos ordenados
  x < ν_R(n)y        recíprocos pequeños
```

> **Frontera metodológica.** No se importarán desde Análisis la aplicación abstracta de numerales de un cuerpo ordenado ni su definición de cuerpo arquimediano. Álgebra reconstruirá esta capa desde la infraestructura previa de naturales, para conservar la dirección canónica «resultado abstracto en Álgebra → instanciación en Análisis».

## 28.1. Infraestructura natural: inducción y recursión

Antes de construir numerales internos necesitamos una interfaz mínima de naturales, inducción y recursión. Esta infraestructura procede del tratamiento fundacional previo y no incorpora resultados sobre cuerpos ordenados ni arquimedianidad.

### Interfaz 28.1.1 — Naturales, inducción y recursión para numerales internos {#talg-imp-00006}
Para construir los numerales internos de un anillo necesitamos una cantidad muy pequeña, pero precisa, de aritmética natural. Esta interfaz importa exclusivamente infraestructura anterior del *Tratado de análisis* y la expone a Álgebra sin importar ningún resultado sobre cuerpos ordenados abstractos.

Las interfaces fundacionales previas garantizan que las nociones de función, producto cartesiano y orden ya tengan significado dentro del tratado antes de utilizar las correspondientes fuentes naturales. La interfaz natural emplea las siguientes piezas:

| fuente | contenido importado |
|---|---|
| `TA-NOT-00007` | $\mathbb N=\omega$ |
| `TA-DEF-00030` | sucesor $S(x)=x\cup\{x\}$ |
| `TA-NOT-00008` | unidad natural $1=S(0)$ |
| `TA-THM-00008` | principio de inducción sobre $\mathbb N$ |
| `TA-THM-00011` | todo natural es $0$ o un sucesor, con predecesor único |
| `TA-COR-00002` | recursión con parámetros y unicidad de la función recursiva |
| `TA-DEF-00036` | adición natural |
| `TA-DEF-00037` | multiplicación natural |
| `TA-DEF-00038` | orden aritmético $m\le n\iff\exists k\in\mathbb N\;(n=m+k)$ |
| `TA-THM-00020` | totalidad del orden natural |

En particular, la recursión con parámetros afirma que, dados conjuntos $P,X$ y funciones $b:P\to X$ y $r:P\times X\to X$, existe una única función

$$
F:P\times\mathbb N\to X
$$

con

$$
F(p,0)=b(p),\qquad F(p,S(n))=r(p,F(p,n)).
$$

La suma y el producto importados son las funciones únicas sobre $\mathbb N\times\mathbb N$ determinadas por

$$
m+0=m,\qquad m+S(n)=S(m+n),
$$

$$
m\cdot0=0,\qquad m\cdot S(n)=m\cdot n+m.
$$

No se importan aquí las leyes abstractas de numerales dentro de un cuerpo, porque serán demostradas internamente en este capítulo a partir de estas ecuaciones y de la estructura algebraica de destino.

La construcción de los naturales utilizada aquí depende del axioma de Infinito y no utiliza el axioma de elección. Tampoco presupone un algoritmo de comparación ni decidibilidad de la igualdad en las estructuras algebraicas posteriores.

Quedan deliberadamente fuera los resultados de Análisis que ya formulen numerales o arquimedianidad en cuerpos ordenados: esa teoría se reconstruye aquí desde la infraestructura natural mínima.

La interfaz previa de aritmética entera y racional conserva su función para los modelos concretos y no sustituye esta interfaz abstracta.

### 28.1.2. Alcance incluido

El capítulo desarrolla, en este orden lógico:

1. numerales naturales internos de un anillo unital mediante una función $\nu_R:\mathbb N\to R$;
2. preservación de $0$, $1$, suma y producto por $\nu_R$;
3. positividad, estricta monotonía e inyectividad de los numerales cuando la estructura ordenada y la no trivialidad proporcionen $0<1_R$;
4. definición de propiedad arquimediana en el nivel algebraico-ordenado adecuado y equivalencia con su formulación de dos escalas positivas;
5. especialización a cuerpos ordenados y caracterización mediante recíprocos positivos arbitrariamente pequeños;
6. compatibilidad con el modelo racional desde la infraestructura aritmética ya admitida.

La formulación primaria de arquimedianidad se elegirá **positiva/existencial**. Formulaciones negativas del tipo «los numerales no están acotados superiormente» se tratarán, si se incorporan, como equivalencias clásicas explícitas y no como definiciones constructivamente idénticas.

### 28.1.3. Alcance excluido

Quedan expresamente fuera de este capítulo:

- propiedad del supremo, ínfimo o completitud de orden;
- completitud métrica o secuencial;
- convergencia, límites, continuidad o topología;
- construcción de $\mathbb R$;
- densidad del subcuerpo primo como requisito de cierre de esta unidad;
- algoritmos para decidir comparaciones en un cuerpo ordenado abstracto;
- identificación literal de $n\in\mathbb N$ con $\nu_R(n)\in R$.

La densidad del subcuerpo primo puede ser recuperada posteriormente en Análisis a partir de la infraestructura algebraica apropiada. No será necesaria para cerrar la Parte V.

## 28.5. Numerales naturales internos de un anillo

Un natural $n\in\mathbb N$ y un elemento de un anillo $R$ pertenecen, en general, a conjuntos distintos. Por tanto, antes de escribir expresiones heurísticas como «$n$ copias de $1$» debemos construir la función que transporta la aritmética recursiva de $\mathbb N$ al anillo.

La construcción necesita sólo dos datos del anillo: su cero aditivo, como valor inicial, y la operación «sumar una vez la unidad multiplicativa», como paso sucesor. No requiere orden, conmutatividad multiplicativa ni no trivialidad.

### Definición 28.5.1 — Aplicación canónica de numerales naturales en un anillo unital {#talg-def-00063}
Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo en el sentido de la Definición 14.1.1. La regla

$$
x\longmapsto x+1_{\mathcal R}
$$

define una función $R\to R$: en efecto, $1_{\mathcal R}\in R$ y $+$ es una operación binaria $R\times R\to R$.

**Existencia.** Para obtener rigurosamente la recursión sin identificar todavía ninguna notación, tomemos un conjunto unitario de parámetros $P=\{p\}$. Definamos

$$
b:P\to R,
\qquad
b(p)=0_{\mathcal R},
$$

y

$$
r:P\times R\to R,
\qquad
r(p,x)=x+1_{\mathcal R}.
$$

Ambas son funciones bien tipadas. La recursión con parámetros de la Interfaz 28.1.1 proporciona entonces una única función

$$
F:P\times\mathbb N\to R
$$

tal que

$$
F(p,0)=0_{\mathcal R},
\qquad
F(p,S(n))=F(p,n)+1_{\mathcal R}.
$$

Definamos provisionalmente $f:\mathbb N\to R$ por $f(n)=F(p,n)$. Entonces

$$
f(0)=0_{\mathcal R},
\qquad
f(S(n))=f(n)+1_{\mathcal R}.
$$

**Unicidad.** Si $g:\mathbb N\to R$ satisface esas mismas dos ecuaciones, la función $G:P\times\mathbb N\to R$ dada por $G(p,n)=g(n)$ satisface las mismas ecuaciones parametrizadas que $F$. La unicidad importada en la Interfaz 28.1.1 da $G=F$; evaluando en $(p,n)$ obtenemos $g(n)=f(n)$ para todo $n\in\mathbb N$. Por tanto $g=f$.

Hemos probado así que existe una única función $\mathbb N\to R$ con esas ecuaciones. **Sólo ahora** introducimos la notación

$$
\boxed{
\nu_{\mathcal R}:\mathbb N\to R
}
$$

para esa función. En consecuencia, para todo $n\in\mathbb N$,

$$
\boxed{
\nu_{\mathcal R}(0)=0_{\mathcal R},
\qquad
\nu_{\mathcal R}(S(n))=\nu_{\mathcal R}(n)+1_{\mathcal R}.
}
$$

La llamaremos **aplicación canónica de numerales naturales** de $\mathcal R$. Cuando la estructura de anillo sobre $R$ esté fijada sin ambigüedad, escribiremos también $\nu_R$.

> **Lectura tipológica.** La expresión $\nu_{\mathcal R}(n)$ pertenece a $R$; el natural $n$ sigue perteneciendo a $\mathbb N$. La definición construye un puente entre ambos conjuntos, no una identificación literal $\mathbb N\subseteq R$.

Nada en la definición afirma todavía que $\nu_{\mathcal R}$ sea inyectiva, que preserve suma o producto, ni que preserve o refleje un orden. Tampoco se supone $0_{\mathcal R}\ne1_{\mathcal R}$. En particular, la definición vale para todo anillo del tratado, incluido el anillo trivial. Esas distinciones son esenciales: la existencia de los numerales internos es anterior a las leyes que luego puedan satisfacer.

## 28.7. Aritmética de la aplicación canónica de numerales

La Definición 28.5.1 construyó la función $\nu_{\mathcal R}$, pero todavía no autorizó a trasladar a $R$ las operaciones de $\mathbb N$. Ése es el objetivo de este subtramo. En las fórmulas siguientes, las operaciones que aparecen **dentro** del argumento de $\nu_{\mathcal R}$ son las operaciones naturales importadas por la Interfaz 28.1.1; las operaciones que aparecen **fuera** son las del anillo $\mathcal R$.

### Proposición 28.7.1 — Aritmética de la aplicación canónica de numerales {#talg-pro-00093}
Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo y sea $\nu_{\mathcal R}:\mathbb N\to R$ su aplicación canónica de numerales. Entonces:

1. $\nu_{\mathcal R}(0)=0_{\mathcal R}$;
2. $\nu_{\mathcal R}(1)=1_{\mathcal R}$;
3. para todos $m,n\in\mathbb N$,

$$
\nu_{\mathcal R}(m+n)
=
\nu_{\mathcal R}(m)+\nu_{\mathcal R}(n);
$$

4. para todos $m,n\in\mathbb N$,

$$
\nu_{\mathcal R}(m\cdot n)
=
\nu_{\mathcal R}(m)\cdot\nu_{\mathcal R}(n).
$$

#### Demostración {#talg-prf-00138}
La primera identidad es una de las ecuaciones que definen $\nu_{\mathcal R}$. Para la segunda, la Interfaz 28.1.1 fija $1=S(0)$ en $\mathbb N$. Por tanto

$$
\begin{aligned}
\nu_{\mathcal R}(1)
&=\nu_{\mathcal R}(S(0))\\
&=\nu_{\mathcal R}(0)+1_{\mathcal R}\\
&=0_{\mathcal R}+1_{\mathcal R}\\
&=1_{\mathcal R}.
\end{aligned}
$$

Quedan la suma y el producto. Las probaremos por separado para que sea visible qué ecuación recursiva se usa en cada paso.

**Preservación de la suma.** Fijemos $m\in\mathbb N$ e induzcamos sobre $n$. Para $n=0$, la ecuación natural $m+0=m$, la definición de $\nu_{\mathcal R}(0)$ y el neutro aditivo dan

$$
\nu_{\mathcal R}(m+0)
=\nu_{\mathcal R}(m)
=\nu_{\mathcal R}(m)+0_{\mathcal R}
=\nu_{\mathcal R}(m)+\nu_{\mathcal R}(0).
$$

Supongamos ahora

$$
\nu_{\mathcal R}(m+n)
=\nu_{\mathcal R}(m)+\nu_{\mathcal R}(n).
$$

La recursión natural satisface $m+S(n)=S(m+n)$. Entonces

$$
\begin{aligned}
\nu_{\mathcal R}(m+S(n))
&=\nu_{\mathcal R}(S(m+n))\\
&=\nu_{\mathcal R}(m+n)+1_{\mathcal R}\\
&=(\nu_{\mathcal R}(m)+\nu_{\mathcal R}(n))+1_{\mathcal R}\\
&=\nu_{\mathcal R}(m)+(\nu_{\mathcal R}(n)+1_{\mathcal R})\\
&=\nu_{\mathcal R}(m)+\nu_{\mathcal R}(S(n)).
\end{aligned}
$$

La cuarta igualdad usa asociatividad de la suma en el grupo aditivo del anillo. Por inducción, la fórmula aditiva vale para todo $n$, y como $m$ era arbitrario, vale para todos $m,n\in\mathbb N$.

**Preservación del producto.** Fijemos nuevamente $m\in\mathbb N$ e induzcamos sobre $n$. Para $n=0$, como $m\cdot0=0$ en $\mathbb N$,

$$
\nu_{\mathcal R}(m\cdot0)=\nu_{\mathcal R}(0)=0_{\mathcal R}.
$$

Por otra parte, la absorción del cero demostrada en la Proposición 14.3.1 da

$$
\nu_{\mathcal R}(m)\cdot\nu_{\mathcal R}(0)
=\nu_{\mathcal R}(m)\cdot0_{\mathcal R}
=0_{\mathcal R}.
$$

Luego la fórmula multiplicativa vale en el caso base. Supongamos ahora

$$
\nu_{\mathcal R}(m\cdot n)
=\nu_{\mathcal R}(m)\cdot\nu_{\mathcal R}(n).
$$

La recursión natural satisface $m\cdot S(n)=m\cdot n+m$. Usando primero la preservación de la suma ya demostrada, después la hipótesis inductiva, la unidad multiplicativa y la distributividad, obtenemos

$$
\begin{aligned}
\nu_{\mathcal R}(m\cdot S(n))
&=\nu_{\mathcal R}(m\cdot n+m)\\
&=\nu_{\mathcal R}(m\cdot n)+\nu_{\mathcal R}(m)\\
&=\nu_{\mathcal R}(m)\cdot\nu_{\mathcal R}(n)+\nu_{\mathcal R}(m)\\
&=\nu_{\mathcal R}(m)\cdot\nu_{\mathcal R}(n)+\nu_{\mathcal R}(m)\cdot1_{\mathcal R}\\
&=\nu_{\mathcal R}(m)\cdot(\nu_{\mathcal R}(n)+1_{\mathcal R})\\
&=\nu_{\mathcal R}(m)\cdot\nu_{\mathcal R}(S(n)).
\end{aligned}
$$

Así la fórmula multiplicativa vale para todo $n$, y por arbitrariedad de $m$, para todos $m,n\in\mathbb N$. ∎

> **Lectura de la prueba.** La suma se demuestra antes que el producto porque la propia recursión de la multiplicación natural contiene una suma: $m\cdot S(n)=m\cdot n+m$. El paso multiplicativo usa, por tanto, la ley aditiva ya cerrada unas líneas antes; no hay circularidad.

> **Prueba de estrés: el anillo trivial.** Si $0_{\mathcal R}=1_{\mathcal R}$, entonces la recursión fuerza que todos los numerales tengan el mismo valor. Las cuatro identidades anteriores siguen siendo verdaderas. Esto muestra por qué «preservar la aritmética» no implica todavía inyectividad de $\nu_{\mathcal R}$.

La proposición no requiere orden ni conmutatividad multiplicativa. En particular, no se ha usado todavía ninguna comparación entre naturales internos.

## 28.9. Orden de la aplicación canónica de numerales

La aritmética de los numerales ya está cerrada. Ahora añadimos exactamente las hipótesis que faltaban para impedir colapsos: una estructura de anillo totalmente ordenado y la no trivialidad $0_{\mathcal R}\ne1_{\mathcal R}$. Por la Proposición 26.16.1 estas hipótesis implican

$$
0_{\mathcal R}<1_{\mathcal R}.
$$

En $\mathbb N$ escribiremos $m<n$ para el orden estricto asociado al orden natural importado en la Interfaz 28.1.1, conforme a la interfaz general de orden de §25.1. Esta escritura no introduce un algoritmo de comparación.

### Proposición 28.9.1 — Orden estricto e inyectividad de los numerales en anillos totalmente ordenados no triviales {#talg-pro-00094}
Sea $\mathcal R$ un anillo totalmente ordenado no trivial y sea $\nu_{\mathcal R}:\mathbb N\to R$ su aplicación canónica de numerales. Entonces:

1. para todo $n\in\mathbb N$,
   $$
   0_{\mathcal R}\le\nu_{\mathcal R}(n);
   $$
2. si $n\ne0$, entonces
   $$
   0_{\mathcal R}<\nu_{\mathcal R}(n);
   $$
3. para todos $m,n\in\mathbb N$,
   $$
   m\le n
   \iff
   \nu_{\mathcal R}(m)\le\nu_{\mathcal R}(n);
   $$
4. para todos $m,n\in\mathbb N$,
   $$
   m<n
   \iff
   \nu_{\mathcal R}(m)<\nu_{\mathcal R}(n);
   $$
5. $\nu_{\mathcal R}$ es inyectiva.

En particular, $\nu_{\mathcal R}$ identifica a $\mathbb N$ con una copia ordenada de los naturales dentro de $R$, pero no con un subconjunto literalmente igual a $\mathbb N$.

#### Demostración {#talg-prf-00139}
Como $\mathcal R$ es totalmente ordenado y no trivial, la Proposición 26.16.1 da

$$
0_{\mathcal R}<1_{\mathcal R}.
$$

**Paso 1: todos los numerales son no negativos.** Demostraremos por inducción que

$$
0_{\mathcal R}\le\nu_{\mathcal R}(r)
$$

para todo $r\in\mathbb N$.

Para $r=0$,

$$
\nu_{\mathcal R}(0)=0_{\mathcal R},
$$

y la reflexividad del orden da $0_{\mathcal R}\le0_{\mathcal R}$.

Supongamos ahora

$$
0_{\mathcal R}\le\nu_{\mathcal R}(r).
$$

De $0_{\mathcal R}<1_{\mathcal R}$ y la invariancia estricta por traslaciones de §25.5, al sumar $\nu_{\mathcal R}(r)$ a ambos miembros obtenemos

$$
\nu_{\mathcal R}(r)
<
\nu_{\mathcal R}(r)+1_{\mathcal R}
=
\nu_{\mathcal R}(S(r)).
$$

Por definición del orden estricto asociado,

$$
\nu_{\mathcal R}(r)\le\nu_{\mathcal R}(S(r)).
$$

La transitividad de $\le$ con la hipótesis inductiva da

$$
0_{\mathcal R}\le\nu_{\mathcal R}(S(r)).
$$

La inducción queda cerrada.

**Paso 2: todo numeral natural no nulo es estrictamente positivo.** Sea $n\ne0$. La Interfaz 28.1.1, mediante el teorema de predecesor natural, proporciona $r\in\mathbb N$ con

$$
n=S(r).
$$

Por el Paso 1,

$$
0_{\mathcal R}\le\nu_{\mathcal R}(r).
$$

Como antes, $0_{\mathcal R}<1_{\mathcal R}$ y la traslación estricta dan

$$
\nu_{\mathcal R}(r)
<
\nu_{\mathcal R}(r)+1_{\mathcal R}
=
\nu_{\mathcal R}(n).
$$

En particular, $\nu_{\mathcal R}(r)\le\nu_{\mathcal R}(n)$. Junto con $0_{\mathcal R}\le\nu_{\mathcal R}(r)$, la transitividad da

$$
0_{\mathcal R}\le\nu_{\mathcal R}(n).
$$

Falta excluir la igualdad con cero. Supongamos, para obtener una contradicción, que

$$
\nu_{\mathcal R}(n)=0_{\mathcal R}.
$$

Entonces $\nu_{\mathcal R}(r)\le0_{\mathcal R}$; combinado con $0_{\mathcal R}\le\nu_{\mathcal R}(r)$, la antisimetría da $\nu_{\mathcal R}(r)=0_{\mathcal R}=\nu_{\mathcal R}(n)$, contradiciendo la desigualdad estricta anterior. Por tanto

$$
\nu_{\mathcal R}(n)\ne0_{\mathcal R}.
$$

Como ya sabemos que $0_{\mathcal R}\le\nu_{\mathcal R}(n)$, la definición del orden estricto asociado concluye

$$
0_{\mathcal R}<\nu_{\mathcal R}(n).
$$

**Paso 3: preservación del orden no estricto.** Supongamos $m\le n$. Por la definición del orden natural existe $k\in\mathbb N$ tal que

$$
n=m+k.
$$

La aritmética de §28.7 da

$$
\nu_{\mathcal R}(n)
=
\nu_{\mathcal R}(m+k)
=
\nu_{\mathcal R}(m)+\nu_{\mathcal R}(k).
$$

Por el Paso 1, $0_{\mathcal R}\le\nu_{\mathcal R}(k)$. La invariancia exacta del orden por traslaciones de §25.3 permite sumar $\nu_{\mathcal R}(m)$ y obtener

$$
\nu_{\mathcal R}(m)
\le
\nu_{\mathcal R}(m)+\nu_{\mathcal R}(k)
=
\nu_{\mathcal R}(n).
$$

**Paso 4: preservación del orden estricto.** Supongamos $m<n$. Como $<$ es el orden estricto asociado,

$$
m\le n
\qquad\text{y}\qquad
m\ne n.
$$

El primer hecho proporciona $k\in\mathbb N$ con $n=m+k$. Si $k=0$, entonces $n=m+0=m$, contradicción. Por tanto $k\ne0$, y el Paso 2 da

$$
0_{\mathcal R}<\nu_{\mathcal R}(k).
$$

Trasladando estrictamente por $\nu_{\mathcal R}(m)$,

$$
\nu_{\mathcal R}(m)
<
\nu_{\mathcal R}(m)+\nu_{\mathcal R}(k)
=
\nu_{\mathcal R}(n).
$$

**Paso 5: inyectividad.** Supongamos

$$
\nu_{\mathcal R}(m)=\nu_{\mathcal R}(n).
$$

La totalidad del orden natural importada en la Interfaz 28.1.1 da

$$
m\le n
\qquad\text{o}\qquad
n\le m.
$$

Consideremos primero $m\le n$. Existe $k\in\mathbb N$ con $n=m+k$. La misma interfaz natural expone que todo natural es $0$ o un sucesor.

- Si $k=0$, entonces $n=m$.
- Si $k=S(r)$ para algún $r\in\mathbb N$, el argumento del Paso 2 aplicado directamente al sucesor $S(r)$ da
  $$
  0_{\mathcal R}<\nu_{\mathcal R}(k).
  $$
  Trasladando por $\nu_{\mathcal R}(m)$ y usando §28.7,
  $$
  \nu_{\mathcal R}(m)
  <
  \nu_{\mathcal R}(m)+\nu_{\mathcal R}(k)
  =
  \nu_{\mathcal R}(n),
  $$
  contradicción con la igualdad de las imágenes.

Por tanto, en el caso $m\le n$ necesariamente $m=n$. El caso $n\le m$ es simétrico. Así

$$
\nu_{\mathcal R}(m)=\nu_{\mathcal R}(n)
\Longrightarrow
m=n,
$$

y $\nu_{\mathcal R}$ es inyectiva.

**Paso 6: reflexión del orden no estricto.** Supongamos

$$
\nu_{\mathcal R}(m)\le\nu_{\mathcal R}(n).
$$

Por totalidad del orden natural, $m\le n$ o $n\le m$. En el primer caso ya tenemos la conclusión. En el segundo, el Paso 3 da

$$
\nu_{\mathcal R}(n)\le\nu_{\mathcal R}(m).
$$

La antisimetría en $R$ produce

$$
\nu_{\mathcal R}(m)=\nu_{\mathcal R}(n),
$$

y la inyectividad recién demostrada da $m=n$. Por reflexividad, $m\le n$.

Hemos probado así

$$
m\le n
\iff
\nu_{\mathcal R}(m)\le\nu_{\mathcal R}(n).
$$

**Paso 7: reflexión del orden estricto.** Supongamos

$$
\nu_{\mathcal R}(m)<\nu_{\mathcal R}(n).
$$

Por definición del orden estricto asociado,

$$
\nu_{\mathcal R}(m)\le\nu_{\mathcal R}(n)
$$

y

$$
\nu_{\mathcal R}(m)\ne\nu_{\mathcal R}(n).
$$

El Paso 6 refleja la primera relación y da $m\le n$. Si $m=n$, la funcionalidad de $\nu_{\mathcal R}$ daría igualdad de las imágenes, contradicción. Luego $m\ne n$, y por la definición del orden estricto asociado,

$$
m<n.
$$

Combinando con el Paso 4,

$$
m<n
\iff
\nu_{\mathcal R}(m)<\nu_{\mathcal R}(n).
$$

Quedan demostradas todas las afirmaciones. ∎

> **Lectura de la prueba.** El orden no se «hereda» de la aritmética por notación. Primero se demuestra que los numerales no nulos son positivos; esa positividad convierte el testigo natural $n=m+k$ en una desigualdad interna. Sólo después se prueba inyectividad y, finalmente, la reflexión del orden.

> **Por qué no aparece tricotomía decidible.** La prueba usa la totalidad de $\le$ en $\mathbb N$ como una disyunción matemática y la descomposición natural «cero o sucesor» ya expuesta por la Interfaz 28.1.1. No importa `TA-PRO-00170`, no postula un algoritmo de comparación y no añade un principio clásico sustantivo.

## 28.11. Propiedad arquimediana

La expresión «arquimediano» puede formularse en estructuras ordenadas de distinta generalidad, pero esas formulaciones dejan de ser automáticamente equivalentes cuando faltan inversos multiplicativos. En particular, la condición de que los numerales internos sean cofinales por arriba tiene sentido en un anillo totalmente ordenado no trivial, pero de ella no se puede pasar en general a una comparación con una **escala positiva arbitraria** $y$ sin poder dividir por $y$.

Por esa razón, y para que la definición tenga un único alcance matemático estable, el tratado reserva aquí la propiedad arquimediana a los **cuerpos ordenados**. La formulación primaria será la cofinalidad positiva de los numerales; la equivalencia con la forma de dos escalas se demostrará después y no se incorpora a la definición.

### Definición 28.11.1 — Propiedad arquimediana {#talg-def-00064}
Sea $\mathcal F$ un cuerpo ordenado y sea

$$
\nu_{\mathcal F}:\mathbb N\to F
$$

su aplicación canónica de numerales. Diremos que $\mathcal F$ es **arquimediano** si

$$
\boxed{
\forall x\in F\;\exists n\in\mathbb N
\quad
x<\nu_{\mathcal F}(n).
}
$$

Ésta será la **formulación primaria** de la propiedad arquimediana en el tratado.

> **Lectura de cuantificadores.** El testigo $n$ puede depender de $x$. La definición no afirma la existencia de un único natural que domine simultáneamente a todos los elementos de $F$.

> **Por qué no exigimos $n\ne0$.** Para elementos negativos, $n=0$ puede ser un testigo legítimo porque $\nu_{\mathcal F}(0)=0_F$. Cuando $x\ge0$, cualquier testigo de la desigualdad estricta es necesariamente no nulo por el encaje de orden demostrado en §28.9. Exigir positividad del natural en la definición sólo añadiría una condición redundante que conviene derivar cuando haga falta.

La definición es deliberadamente **positiva y existencial**. No se define arquimedianidad mediante la frase «$\nu_{\mathcal F}[\mathbb N]$ no está acotado superiormente». En la lógica clásica esa formulación negativa puede relacionarse con la anterior, pero la conversión involucra negación de cuantificadores y no se toma aquí como identidad definicional.

Tampoco aparece ninguna forma de completitud. La propiedad arquimediana controla una comparación de **escalas finitas** mediante numerales internos; no afirma existencia de supremos, ínfimos, límites ni puntos de acumulación.

### Por qué el nivel estructural es un cuerpo ordenado

La fórmula de la Definición 28.11.1 sólo menciona orden y numerales, de modo que podría escribirse sintácticamente para un anillo totalmente ordenado no trivial. Sin embargo, para comparar después una escala positiva arbitraria $y$ mediante expresiones de la forma

$$
x<\nu_{\mathcal F}(n)y.
$$

Para reducir esa comparación a la formulación primaria hay que poder transformar la escala $y$ usando su inverso positivo. Ésa es precisamente la infraestructura que ya está disponible en un cuerpo ordenado por el capítulo 27. El tratado no identificará, por tanto, la mera cofinalidad de los numerales en un anillo general con la propiedad de dos escalas sin una prueba válida que lo autorice.

## 28.13. Formulación de dos escalas positivas

La definición primaria mide todos los elementos con respecto a la unidad $1_F$. La forma realmente útil para reutilizar la propiedad consiste en permitir una **unidad de escala positiva arbitraria** $y$: el tamaño de $x$ se compara entonces con múltiplos naturales de $y$.

Conviene distinguir dos formulaciones. La primera admite un objetivo $x$ arbitrario y una escala $y>0$; la segunda restringe también $x$ a ser positivo y exige explícitamente un numeral no nulo. Demostraremos que ambas son equivalentes a la Definición 28.11.1.

### Proposición 28.13.1 — Equivalencia con la formulación de dos escalas positivas {#talg-pro-00095}
Sea $\mathcal F$ un cuerpo ordenado, con aplicación canónica de numerales $\nu_{\mathcal F}:\mathbb N\to F$. Son equivalentes las siguientes afirmaciones:

1. $\mathcal F$ es arquimediano;
2. para todos $x,y\in F$, si $0<y$, existe $n\in\mathbb N$ tal que
   $$
   \boxed{x<\nu_{\mathcal F}(n)y};
   $$
3. para todos $x,y\in F$, si $0<x$ y $0<y$, existe $n\in\mathbb N$, $n\ne0$, tal que
   $$
   \boxed{x<\nu_{\mathcal F}(n)y}.
   $$

La condición 3 será llamada **formulación de dos escalas positivas**: una escala positiva $y$ puede multiplicarse por un numeral natural suficientemente grande para sobrepasar cualquier otra escala positiva $x$.

#### Demostración {#talg-prf-00140}
**1 $\Rightarrow$ 2.** Supongamos que $\mathcal F$ es arquimediano. Sean $x,y\in F$ y supongamos $0<y$. Por la definición del orden estricto asociado, $y\ne0$, de modo que $y^{-1}$ está definido. El elemento

$$
z:=xy^{-1}
$$

pertenece a $F$. Por arquimedianidad existe $n\in\mathbb N$ tal que

$$
xy^{-1}<\nu_{\mathcal F}(n). \tag{1}
$$

Aplicaremos ahora la equivalencia estricta de la Proposición 27.14.1 con factor positivo $c=y$. Para

$$
a=x,
\qquad
b=\nu_{\mathcal F}(n)y,
$$

dicha proposición da

$$
x<\nu_{\mathcal F}(n)y
\iff
xy^{-1}<\bigl(\nu_{\mathcal F}(n)y\bigr)y^{-1}. \tag{2}
$$

Por asociatividad de la multiplicación, la identidad $yy^{-1}=1$ y la ley de la unidad,

$$
\bigl(\nu_{\mathcal F}(n)y\bigr)y^{-1}
=
\nu_{\mathcal F}(n)(yy^{-1})
=
\nu_{\mathcal F}(n).
$$

La desigualdad (1) es, por tanto, exactamente el miembro derecho de (2). Concluimos

$$
x<\nu_{\mathcal F}(n)y.
$$

Esto prueba 2.

**2 $\Rightarrow$ 3.** Supongamos 2 y sean ahora $x,y>0$. Existe $n\in\mathbb N$ con

$$
x<\nu_{\mathcal F}(n)y. \tag{3}
$$

Falta verificar que el testigo no puede ser $0$. Si $n=0$, la Proposición 28.7.1 y la absorción del cero darían

$$
\nu_{\mathcal F}(n)y
=
\nu_{\mathcal F}(0)y
=
0_Fy
=
0_F.
$$

Entonces (3) implicaría $x<0_F$, contradiciendo $0_F<x$. Por tanto $n\ne0$, y queda demostrada 3.

**3 $\Rightarrow$ 1.** Supongamos la formulación de dos escalas positivas y fijemos un elemento arbitrario $z\in F$. Como el orden es total,

$$
z\le0_F
\qquad\text{o}\qquad
0_F\le z.
$$

Consideremos los dos casos.

- Si $z\le0_F$, la Proposición 26.16.1 da $0_F<1_F$, mientras que la Proposición 28.7.1 da $\nu_{\mathcal F}(1)=1_F$. Por transitividad,
  $$
  z<1_F=\nu_{\mathcal F}(1).
  $$
  Así la condición arquimediana se satisface con el testigo $1$.

- Supongamos $0_F\le z$. De $0_F<1_F$ y la invariancia del orden estricto por traslaciones (§25.5) obtenemos
  $$
  z<z+1_F.
  $$
  Combinando con $0_F\le z$, resulta
  $$
  0_F<z+1_F.
  $$
  Además $0_F<1_F$. Aplicamos 3 a las dos escalas positivas
  $$
  x:=z+1_F,
  \qquad
  y:=1_F.
  $$
  Existe $n\in\mathbb N$, $n\ne0$, tal que
  $$
  z+1_F
  <
  \nu_{\mathcal F}(n)1_F
  =
  \nu_{\mathcal F}(n).
  $$
  Como $z<z+1_F$, la transitividad del orden estricto da
  $$
  z<\nu_{\mathcal F}(n).
  $$

En ambos casos existe un natural cuyo numeral supera estrictamente a $z$. Como $z$ era arbitrario, $\mathcal F$ es arquimediano por la Definición 28.11.1. $\square$

> **Lectura de la prueba.** El único paso que necesita inversos es $1\Rightarrow2$: para medir $x$ en unidades de $y$ se considera $xy^{-1}$. La vuelta $3\Rightarrow1$ no usa división; sólo reduce un elemento arbitrario al caso positivo mediante $z+1_F$.

> **Orden de los cuantificadores.** Ni 2 ni 3 afirman la existencia de un mismo $n$ para todos los pares $(x,y)$. El testigo puede depender simultáneamente del objetivo y de la unidad de escala.

> **Frontera estructural.** Esta prueba explica por qué §28.11 fijó la arquimedianidad al nivel de cuerpo ordenado: el paso $1\Rightarrow2$ utiliza el inverso de una escala positiva arbitraria. No se extiende automáticamente a anillos totalmente ordenados donde dicho inverso puede no existir.

## 28.15. Recíprocos positivos arbitrariamente pequeños

La formulación arquimediana dice que los numerales internos pueden hacerse tan grandes como sea necesario. En un cuerpo ordenado, la inversión transforma esa afirmación en una descripción dual: los inversos de numerales positivos pueden hacerse tan pequeños como se quiera **sin llegar a cero**.

Esta equivalencia no introduce una sucesión, un límite ni una noción de convergencia. La frase «arbitrariamente pequeños» abrevia únicamente una afirmación cuantificada: dada de antemano una cota positiva $\varepsilon$, existe un numeral natural no nulo cuyo inverso queda estrictamente entre $0$ y $\varepsilon$.

### Proposición 28.15.1 — Caracterización por recíprocos positivos arbitrariamente pequeños {#talg-pro-00096}
Sea $\mathcal F$ un cuerpo ordenado y sea $\nu_{\mathcal F}:\mathbb N\to F$ su aplicación canónica de numerales. Son equivalentes:

1. $\mathcal F$ es arquimediano;
2. para todo $\varepsilon\in F$ con $0<\varepsilon$, existe $n\in\mathbb N$ tal que
   $$
   n\ne0
   \qquad\text{y}\qquad
   \boxed{0<\nu_{\mathcal F}(n)^{-1}<\varepsilon}.
   $$

En la condición 2, la escritura $\nu_{\mathcal F}(n)^{-1}$ se interpreta **después** de verificar $n\ne0$: por la Proposición 28.9.1, ese hecho implica $0<\nu_{\mathcal F}(n)$ y, por tanto, $\nu_{\mathcal F}(n)\ne0$.

#### Demostración {#talg-prf-00141}
**1 $\Rightarrow$ 2.** Supongamos que $\mathcal F$ es arquimediano y fijemos $\varepsilon\in F$ con

$$
0<\varepsilon.
$$

La desigualdad estricta implica $\varepsilon\ne0$, por lo que $\varepsilon^{-1}$ está definido. La Proposición 27.4.1 da

$$
0<\varepsilon^{-1}. \tag{1}
$$

Aplicamos ahora la Definición 28.11.1 al elemento $\varepsilon^{-1}$. Existe $n\in\mathbb N$ tal que

$$
\varepsilon^{-1}<\nu_{\mathcal F}(n). \tag{2}
$$

De (1), (2) y la transitividad del orden estricto obtenemos

$$
0<\nu_{\mathcal F}(n). \tag{3}
$$

Debemos justificar que el numeral puede invertirse. Si $n=0$, la Proposición 28.7.1 daría

$$
\nu_{\mathcal F}(n)=\nu_{\mathcal F}(0)=0_F,
$$

contradiciendo (3). Por tanto

$$
n\ne0.
$$

La Proposición 28.9.1 confirma además que todo numeral correspondiente a un natural no nulo es estrictamente positivo; en particular, $\nu_{\mathcal F}(n)\ne0$ y su inverso está definido. La Proposición 27.4.1 aplicada a $\nu_{\mathcal F}(n)>0$ proporciona

$$
0<\nu_{\mathcal F}(n)^{-1}. \tag{4}
$$

Ahora (1) y (3) permiten aplicar la antitonicidad de la inversión entre positivos, Proposición 27.8.1, a la desigualdad (2). Resulta

$$
\nu_{\mathcal F}(n)^{-1}
<
(\varepsilon^{-1})^{-1}. \tag{5}
$$

Falta identificar el miembro derecho. Como $\varepsilon\ne0$, por definición de inverso

$$
\varepsilon\varepsilon^{-1}=1
\qquad\text{y}\qquad
\varepsilon^{-1}\varepsilon=1.
$$

Por (1), $\varepsilon^{-1}\ne0$, de modo que $(\varepsilon^{-1})^{-1}$ existe. Las dos igualdades anteriores muestran que $\varepsilon$ es un inverso bilateral de $\varepsilon^{-1}$; por la unicidad del inverso multiplicativo, Proposición 15.2.1,

$$
(\varepsilon^{-1})^{-1}=\varepsilon. \tag{6}
$$

Sustituyendo (6) en (5) y combinando con (4), obtenemos

$$
0<\nu_{\mathcal F}(n)^{-1}<\varepsilon.
$$

Queda demostrada la condición 2.

**2 $\Rightarrow$ 1.** Supongamos ahora la condición de los recíprocos pequeños y fijemos un elemento arbitrario $x\in F$. La totalidad del orden da

$$
x\le0_F
\qquad\text{o}\qquad
0_F\le x. \tag{7}
$$

Consideremos ambas posibilidades.

- Si $x\le0_F$, la Proposición 26.16.1 da $0_F<1_F$ y la Proposición 28.7.1 da $\nu_{\mathcal F}(1)=1_F$. Por transitividad,
  $$
  x<1_F=\nu_{\mathcal F}(1).
  $$
  Por tanto la condición arquimediana se satisface para $x$ con el testigo $1$.

- Supongamos $0_F\le x$. Como $0_F<1_F$, la invariancia estricta por traslaciones de la Proposición 25.5.1 permite sumar $x$ a ambos miembros y obtener
  $$
  x<x+1_F. \tag{8}
  $$
  Junto con $0_F\le x$, esto implica
  $$
  0_F<x+1_F. \tag{9}
  $$
  Por la Proposición 27.4.1,
  $$
  0_F<(x+1_F)^{-1}. \tag{10}
  $$
  Aplicamos la condición 2 a la cantidad positiva
  $$
  \varepsilon:=(x+1_F)^{-1}.
  $$
  Existe $n\in\mathbb N$, $n\ne0$, tal que
  $$
  0_F<\nu_{\mathcal F}(n)^{-1}
  <
  (x+1_F)^{-1}. \tag{11}
  $$
  Como $n\ne0$, la Proposición 28.9.1 da
  $$
  0_F<\nu_{\mathcal F}(n). \tag{12}
  $$
  Las cantidades $x+1_F$ y $\nu_{\mathcal F}(n)$ son, por (9) y (12), ambas positivas. La equivalencia de la Proposición 27.8.1 dice entonces
  $$
  x+1_F<\nu_{\mathcal F}(n)
  \iff
  \nu_{\mathcal F}(n)^{-1}<(x+1_F)^{-1}. \tag{13}
  $$
  El miembro derecho de (13) es precisamente la segunda desigualdad de (11); por tanto
  $$
  x+1_F<\nu_{\mathcal F}(n).
  $$
  Finalmente, (8) y la transitividad del orden estricto dan
  $$
  x<\nu_{\mathcal F}(n).
  $$

En los dos casos existe $n\in\mathbb N$ cuyo numeral supera estrictamente a $x$. Como $x$ era arbitrario, $\mathcal F$ es arquimediano por la Definición 28.11.1. $\square$

> **Lectura de la prueba.** En el sentido directo, «numerales grandes» se convierte en «recíprocos pequeños» invirtiendo una desigualdad entre dos elementos cuya positividad ya está establecida. En el sentido recíproco, la tolerancia $(x+1)^{-1}$ fabrica un numeral cuyo inverso es todavía menor; la antitonicidad de la inversión vuelve a invertir la comparación y produce un numeral mayor que $x+1$.

> **Por qué $n\ne0$ aparece antes del inverso.** El símbolo $\nu(n)^{-1}$ no es una operación total sobre todos los elementos del cuerpo: $0_F$ no tiene inverso. El testigo natural debe ser no nulo, y §28.9 transforma esa no nulidad natural en positividad —y por tanto no nulidad— del numeral interno.

> **No hay convergencia escondida.** El resultado no afirma que la familia $\nu(n)^{-1}$ «converja a cero». Sólo establece el patrón cuantificado $\forall\varepsilon>0\;\exists n\ne0$ con $0<\nu(n)^{-1}<\varepsilon$. Cualquier lectura secuencial o topológica queda fuera de este capítulo.

## 28.19. Compatibilidad de los numerales con el modelo racional

Queda una última cuestión matemática: comprobar que la aplicación abstracta de numerales reconstruida en este capítulo coincide, cuando el anillo destino es el cuerpo racional ya construido, con el camino concreto que primero interpreta un natural como entero y después ese entero como racional.

La clave no será una nueva inducción. Las dos construcciones quedarán identificadas porque satisfacen el mismo problema de recursión con la misma condición inicial y el mismo paso sucesor.

### Proposición 28.19.1 — Compatibilidad de la aplicación canónica de numerales con el modelo racional {#talg-pro-00097}
Sea $\mathbb Q$ el cuerpo racional expuesto por la Interfaz 24.0.1. Denotemos por

$$
\iota_{\mathbb N}^{\mathbb Z}:\mathbb N\to\mathbb Z
$$

la incrustación natural en los enteros y por

$$
\jmath_{\mathbb Z}^{\mathbb Q}:\mathbb Z\to\mathbb Q
$$

la incrustación entera en los racionales, ambas disponibles mediante la Interfaz 24.0.1. Sea además

$$
\nu_{\mathbb Q}:\mathbb N\to\mathbb Q
$$

la aplicación canónica de numerales de la Definición 28.5.1, aplicada al anillo subyacente del cuerpo racional. Entonces, para todo $n\in\mathbb N$,

$$
\boxed{
\nu_{\mathbb Q}(n)
=
\jmath_{\mathbb Z}^{\mathbb Q}
\bigl(\iota_{\mathbb N}^{\mathbb Z}(n)\bigr).
}
$$

Equivalentemente, como funciones $\mathbb N\to\mathbb Q$,

$$
\boxed{
\nu_{\mathbb Q}
=
\jmath_{\mathbb Z}^{\mathbb Q}
\circ
\iota_{\mathbb N}^{\mathbb Z}.
}
$$

#### Demostración {#talg-prf-00142}
Definamos la composición

$$
h
:=
\jmath_{\mathbb Z}^{\mathbb Q}
\circ
\iota_{\mathbb N}^{\mathbb Z}
:
\mathbb N\to\mathbb Q.
$$

La función está bien tipada: la primera incrustación tiene codominio $\mathbb Z$ y la segunda dominio $\mathbb Z$. Verificaremos que $h$ satisface exactamente las dos ecuaciones recursivas que caracterizan a $\nu_{\mathbb Q}$.

**Paso 1: valor inicial.** La Interfaz 24.0.1 expone que ambas incrustaciones preservan el cero. Por tanto

$$
\begin{aligned}
h(0)
&=\jmath_{\mathbb Z}^{\mathbb Q}
   \bigl(\iota_{\mathbb N}^{\mathbb Z}(0)\bigr)\\
&=\jmath_{\mathbb Z}^{\mathbb Q}(0_{\mathbb Z})\\
&=0_{\mathbb Q}.
\end{aligned}
$$

**Paso 2: relación entre sucesor y suma con $1$.** La Interfaz 28.1.1 fija $1=S(0)$ y las ecuaciones recursivas de la suma natural. Para todo $n\in\mathbb N$,

$$
\begin{aligned}
n+1
&=n+S(0)\\
&=S(n+0)\\
&=S(n).
\end{aligned}
$$

Así,

$$
\boxed{S(n)=n+1.}
$$

**Paso 3: paso sucesor para $h$.** Las dos incrustaciones preservan la suma y la unidad. Utilizando el Paso 2,

$$
\begin{aligned}
h(S(n))
&=\jmath_{\mathbb Z}^{\mathbb Q}
  \bigl(\iota_{\mathbb N}^{\mathbb Z}(S(n))\bigr)\\
&=\jmath_{\mathbb Z}^{\mathbb Q}
  \bigl(\iota_{\mathbb N}^{\mathbb Z}(n+1)\bigr)\\
&=\jmath_{\mathbb Z}^{\mathbb Q}
  \bigl(\iota_{\mathbb N}^{\mathbb Z}(n)
  +\iota_{\mathbb N}^{\mathbb Z}(1)\bigr)\\
&=\jmath_{\mathbb Z}^{\mathbb Q}
  \bigl(\iota_{\mathbb N}^{\mathbb Z}(n)+1_{\mathbb Z}\bigr)\\
&=\jmath_{\mathbb Z}^{\mathbb Q}
  \bigl(\iota_{\mathbb N}^{\mathbb Z}(n)\bigr)
  +\jmath_{\mathbb Z}^{\mathbb Q}(1_{\mathbb Z})\\
&=h(n)+1_{\mathbb Q}.
\end{aligned}
$$

Hemos demostrado, por tanto,

$$
h(0)=0_{\mathbb Q},
\qquad
h(S(n))=h(n)+1_{\mathbb Q}.
$$

La Definición 28.5.1 caracteriza a $\nu_{\mathbb Q}$ como la **única** función $\mathbb N\to\mathbb Q$ que satisface esas dos ecuaciones. Como $h$ satisface las mismas ecuaciones, la unicidad obliga a

$$
h=\nu_{\mathbb Q}.
$$

Evaluando ambas funciones en un $n\in\mathbb N$ arbitrario obtenemos

$$
\nu_{\mathbb Q}(n)
=
\jmath_{\mathbb Z}^{\mathbb Q}
\bigl(\iota_{\mathbb N}^{\mathbb Z}(n)\bigr).
$$

Queda demostrada la compatibilidad. $\square$

> **Lectura de la prueba.** No se demuestra otra vez por inducción que las dos copias de los naturales coinciden. Se verifica que ambas resuelven el mismo problema recursivo y se usa la unicidad ya construida. La igualdad procede de una propiedad universal local de la recursión, no de una convención notacional.

> **Frontera tipológica.** La conclusión no afirma $\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q$ como inclusiones literales. Afirma que dos funciones con dominio $\mathbb N$ y codominio $\mathbb Q$ son iguales.

> **Prueba de estrés.** Ni el orden racional, ni la arquimedianidad de $\mathbb Q$, ni la densidad racional intervienen. Sólo se usan el cuerpo racional como destino algebraico, las dos incrustaciones aritméticas y la unicidad de la recursión de numerales.

## 28.21. Síntesis deductiva del capítulo

El problema planteado en §28.0 era aislar la propiedad arquimediana como una propiedad **algebraico-ordenada de escala finita**, sin identificar naturales con elementos del cuerpo y sin importar completitud desde Análisis. La cadena cerrada del capítulo puede resumirse así:

```text
naturales + inducción + recursión
        │
        ▼
aplicación canónica de numerales ν_R : N → R
        │
        ├── aritmética: 0, 1, suma y producto (§28.7)
        │
        └── orden + no trivialidad (§28.9)
            ├── numerales no negativos
            ├── numerales no nulos positivos
            └── ν_R preserva y refleja ≤ y <
        │
        ▼
cuerpo ordenado + cofinalidad de numerales
        │
        ├── propiedad arquimediana (§28.11)
        ├── formulación de escala positiva arbitraria (§28.13)
        └── recíprocos positivos arbitrariamente pequeños (§28.15)
        │
        ▼
compatibilidad con el modelo racional (§28.19)
        └── ν_Q = j_Z^Q ∘ i_N^Z por unicidad de la recursión
```

La primera separación conceptual del capítulo es **tipológica**. Un natural $n\in\mathbb N$ no se identifica literalmente con un elemento de un anillo $R$: la Definición 28.5.1 construye una función $\nu_{\mathcal R}:\mathbb N\to R$, y sólo después se demuestran las leyes que permiten tratar sus valores como numerales internos. En el anillo trivial la función existe y preserva las operaciones, pero no es inyectiva; por eso la inyectividad aparece sólo después de añadir orden total y no trivialidad.

La segunda separación es entre **cofinalidad de numerales** y **cambio de escala**. La Definición 28.11.1 fija la arquimedianidad en cuerpos ordenados mediante la formulación positiva
$$
\forall x\in F\;\exists n\in\mathbb N\quad x<\nu_{\mathcal F}(n).
$$
La Proposición 28.13.1 demuestra después —y no presupone— que esta condición equivale a sobrepasar un objetivo mediante múltiplos naturales de cualquier escala positiva. El paso de una escala arbitraria a la unidad utiliza el inverso positivo de esa escala; ésa es la razón estructural para trabajar al nivel de cuerpos ordenados.

La tercera separación es entre una **afirmación cuantificada de pequeñez** y una afirmación analítica de convergencia. La Proposición 28.15.1 establece
$$
\forall\varepsilon>0\;\exists n\ne0
\quad
0<\nu_{\mathcal F}(n)^{-1}<\varepsilon,
$$
como caracterización equivalente de la arquimedianidad. Esto no introduce sucesiones, límites, topología ni completitud. El testigo $n\ne0$ se obtiene antes de formar el inverso del numeral.

Finalmente, la compatibilidad racional de §28.19 no identifica literalmente $\mathbb N$, $\mathbb Z$ y $\mathbb Q$. La composición
$$
\mathbb N\longrightarrow\mathbb Z\longrightarrow\mathbb Q
$$
coincide con $\nu_{\mathbb Q}$ porque satisface las mismas ecuaciones recursivas de cero y sucesor y la aplicación de numerales es única. No se usa la arquimedianidad de $\mathbb Q$ ya demostrada en Análisis.

El capítulo hereda el axioma de Infinito a través de la construcción de $\mathbb N$ y no utiliza el axioma de elección. No aparece un principio clásico sustantivo nuevo en las pruebas propias: las disyunciones empleadas proceden de totalidades ya asumidas o importadas como estructura. La propiedad del supremo, la completitud, la densidad del subcuerpo primo, la convergencia y cualquier lectura topológica permanecen fuera de este capítulo.

---

[← **Capítulo 27 — Cuerpos ordenados**](tratado-de-algebra-capitulo-27-cuerpos-ordenados.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
