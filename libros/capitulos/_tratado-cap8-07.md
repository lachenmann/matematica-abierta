## 8.7. Incompletitud secuencial de $\mathbb Q$ {#sec-ta-8-7}

La condición de Cauchy fue diseñada precisamente para describir procesos racionales que se estabilizan internamente sin mencionar de antemano un límite. Hasta ahora hemos probado una sola dirección:

$$
q_n\to_{\mathbb Q}\ell
\Longrightarrow
q\in\mathcal C_{\mathbb Q}.
$$

La pregunta decisiva es si la recíproca vale en $\mathbb Q$.

Si toda sucesión racional de Cauchy poseyera un límite racional, el sistema racional sería suficiente para absorber todos sus procesos de aproximación coherentes. Si, por el contrario, podemos construir una sucesión de Cauchy sin límite en $\mathbb Q$, aparecerá una nueva forma de incompletitud: no un hueco descrito directamente por un conjunto ordenado, sino un **proceso racional que exige un punto que $\mathbb Q$ no contiene**.

### Definición 8.7.1 — Completitud secuencial de $\mathbb Q$

Diremos que $\mathbb Q$ es **secuencialmente completo** si toda sucesión racional de Cauchy converge racionalmente a algún elemento de $\mathbb Q$; es decir, si

$$
\boxed{
\forall q\in\mathcal C_{\mathbb Q}\;
\exists \ell\in\mathbb Q
\quad
q_n\to_{\mathbb Q}\ell.
}
$$

La completitud secuencial es aquí una afirmación existencial sobre límites:
$$
\boxed{\text{completitud secuencial}\neq\text{algoritmo que calcule el límite}.}
$$
Para una lectura efectiva habrá que exigir nombres computables y módulos adecuados.

Negar esta propiedad significa exhibir una sucesión concreta

$$
q\in\mathcal C_{\mathbb Q}
$$

tal que

$$
\forall \ell\in\mathbb Q,
\qquad
q_n\not\to_{\mathbb Q}\ell.
$$

Construiremos una de ellas mediante una bisección enteramente racional asociada a la ecuación $x^2=2_{\mathbb Q}$.

---

### Definición 8.7.2 — Operador racional de bisección para $x^2=2$

Para $x,y\in\mathbb Q$ definimos su punto medio racional

$$
\mu(x,y)
:=
\frac{x+y}{2_{\mathbb Q}}.
$$

Como $2_{\mathbb Q}\neq0_{\mathbb Q}$, esta división está definida.

Definimos el **operador racional de bisección**

$$
\Phi_2:
\mathbb Q\times\mathbb Q
\longrightarrow
\mathbb Q\times\mathbb Q
$$

por

$$
\boxed{
\Phi_2(x,y)
=
\begin{cases}
(\mu(x,y),y),
&
\text{si }\mu(x,y)^2<2_{\mathbb Q},
\\[1mm]
(x,\mu(x,y)),
&
\text{si }\neg\bigl(\mu(x,y)^2<2_{\mathbb Q}\bigr).
\end{cases}
}
$$

La definición es total y efectiva sobre entradas racionales. La comparación

$$
\mu(x,y)^2<2_{\mathbb Q}
$$

es decidible por Proposición 3.7.6 — Tricotomía decidible de los racionales; por tanto podemos determinar cuál de las dos cláusulas corresponde
sin apelar a una instancia no efectiva del tercero excluido. Su grafo se obtiene por separación dentro de

$$
(\mathbb Q\times\mathbb Q)\times(\mathbb Q\times\mathbb Q),
$$

y cada entrada determina un único valor.

> **Nota fundacional.** La definición no efectúa una elección entre múltiples testigos: el nuevo par queda determinado por una condición decidida sobre un único punto medio racional. No interviene Choice.

> `classical-use: none`; `constructive-status: constructive-compatible`; `effective-status: effective`.

---

### Proposición 8.7.3 — Existencia y unicidad de las sucesiones de bisección

Existen únicas sucesiones racionales

$$
a=(a_n)_{n\in\mathbb N},
\qquad
b=(b_n)_{n\in\mathbb N}
$$

tales que

$$
a_0=1_{\mathbb Q},
\qquad
b_0=2_{\mathbb Q},
$$

y, si

$$
m_n:=\frac{a_n+b_n}{2_{\mathbb Q}},
$$

entonces para todo $n\in\mathbb N$,

$$
\boxed{
(a_{S(n)},b_{S(n)})
=
\begin{cases}
(m_n,b_n),
&
\text{si }m_n^2<2_{\mathbb Q},
\\[1mm]
(a_n,m_n),
&
\text{si }\neg(m_n^2<2_{\mathbb Q}).
\end{cases}
}
$$

**Demostración.**

Consideremos el conjunto de estados

$$
X:=\mathbb Q\times\mathbb Q
$$

y el estado inicial

$$
p_0:=(1_{\mathbb Q},2_{\mathbb Q})\in X.
$$

El operador $\Phi_2$ de Definición 8.7.2 — Operador racional de bisección para $x^2=2$ es una función $X\to X$. El teorema de recursión sobre $\mathbb N$, Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$, produce una única función

$$
p:\mathbb N\longrightarrow X
$$

tal que

$$
p(0)=p_0
$$

y

$$
p(S(n))=\Phi_2(p(n))
$$

para todo $n\in\mathbb N$.

Para cada $n$, como $p(n)\in\mathbb Q\times\mathbb Q$, existen $a_n,b_n\in\mathbb Q$ con

$$
p(n)=\langle a_n,b_n\rangle.
$$

La unicidad de las coordenadas se sigue del teorema característico del par ordenado Teorema 0.3.4 — Teorema característico del par ordenado. Los grafos

$$
G_a
=
\{\langle n,x\rangle\in\mathbb N\times\mathbb Q:
\exists y\in\mathbb Q,\ p(n)=\langle x,y\rangle\}
$$

y

$$
G_b
=
\{\langle n,y\rangle\in\mathbb N\times\mathbb Q:
\exists x\in\mathbb Q,\ p(n)=\langle x,y\rangle\}
$$

determinan por tanto funciones únicas

$$
a,b:\mathbb N\to\mathbb Q.
$$

La ecuación recursiva de $p$ se traduce exactamente en las fórmulas afirmadas para $a$ y $b$. La unicidad de $p$ implica la unicidad del par $(a,b)$. ∎

> **Auditoría de elección.** La función de estados $p$ viene dada por el teorema de recursión y cada coordenada está determinada de manera única. No se elige una sucesión de ramas ni una familia de representantes.

> **Contenido efectivo.** Como la rama de $\Phi_2$ se decide racionalmente en cada etapa, la recursión
> produce sucesiones computables $n\mapsto a_n$ y $n\mapsto b_n$.

---

### Lema 8.7.4 — Invariantes de la bisección racional

Para todo $n\in\mathbb N$ se cumplen:

1. 
   $$
   0_{\mathbb Q}<a_n<b_n;
   $$
2. 
   $$
   a_n^2<2_{\mathbb Q}<b_n^2;
   $$
3. 
   $$
   a_n\leq a_{S(n)}<b_{S(n)}\leq b_n;
   $$
4. 
   $$
   b_{S(n)}-a_{S(n)}
   =
   \frac{b_n-a_n}{2_{\mathbb Q}}.
   $$

Además, si $n,r\in\mathbb N$ y $n\leq r$, entonces

$$
\boxed{
a_n\leq a_r<b_r\leq b_n.
}
$$

**Demostración.**

Procedemos por inducción sobre $n$.

Para $n=0$,

$$
a_0=1_{\mathbb Q},
\qquad
b_0=2_{\mathbb Q}.
$$

Las propiedades de la incrustación natural Corolario 3.8.2 — Propiedades de la incrustación natural dan

$$
0_{\mathbb Q}<1_{\mathbb Q}<2_{\mathbb Q}.
$$

Además,

$$
1_{\mathbb Q}^2=1_{\mathbb Q}<2_{\mathbb Q}.
$$

Como $0_{\mathbb Q}<2_{\mathbb Q}$, la invariancia estricta por traslación da

$$
2_{\mathbb Q}
<
2_{\mathbb Q}+2_{\mathbb Q}
=
2_{\mathbb Q}^2.
$$

Por tanto,

$$
a_0^2<2_{\mathbb Q}<b_0^2,
$$

y las dos primeras propiedades valen en el estado inicial.

Supongamos ahora que

$$
0<a_n<b_n
$$

y

$$
a_n^2<2_{\mathbb Q}<b_n^2.
$$

Sea

$$
m_n=\frac{a_n+b_n}{2_{\mathbb Q}}.
$$

Como $0<2_{\mathbb Q}$, también $0<2_{\mathbb Q}^{-1}$. De $a_n<b_n$ obtenemos

$$
0<b_n-a_n.
$$

Multiplicando por el inverso positivo de $2_{\mathbb Q}$,

$$
0<
\frac{b_n-a_n}{2_{\mathbb Q}}.
$$

Las leyes del cuerpo reducen

$$
m_n-a_n
=
\frac{b_n-a_n}{2_{\mathbb Q}}
$$

y

$$
b_n-m_n
=
\frac{b_n-a_n}{2_{\mathbb Q}},
$$

por lo que

$$
a_n<m_n<b_n.
$$

Por Teorema 3.9.5 — No existe una raíz cuadrada racional de $2$, ningún racional tiene cuadrado igual a $2_{\mathbb Q}$; en particular,

$$
m_n^2\neq2_{\mathbb Q}.
$$

La totalidad del orden racional deja entonces exactamente dos posibilidades:

$$
m_n^2<2_{\mathbb Q}
\qquad\text{o}\qquad
2_{\mathbb Q}<m_n^2.
$$

Si $m_n^2<2_{\mathbb Q}$, la recurrencia da

$$
a_{S(n)}=m_n,
\qquad
b_{S(n)}=b_n.
$$

Entonces

$$
a_n<a_{S(n)}<b_{S(n)}=b_n
$$

y

$$
a_{S(n)}^2<2_{\mathbb Q}<b_{S(n)}^2.
$$

Si $2_{\mathbb Q}<m_n^2$, la recurrencia da

$$
a_{S(n)}=a_n,
\qquad
b_{S(n)}=m_n,
$$

por lo que

$$
a_n=a_{S(n)}<b_{S(n)}<b_n
$$

y nuevamente

$$
a_{S(n)}^2<2_{\mathbb Q}<b_{S(n)}^2.
$$

En ambos casos se preservan las propiedades $1$, $2$ y $3$.

Para la anchura, en la primera rama,

$$
b_{S(n)}-a_{S(n)}
=
b_n-m_n
=
\frac{b_n-a_n}{2_{\mathbb Q}},
$$

mientras que en la segunda,

$$
b_{S(n)}-a_{S(n)}
=
m_n-a_n
=
\frac{b_n-a_n}{2_{\mathbb Q}}.
$$

Así vale $4$ en todos los casos.

El principio de inducción Teorema 1.1.10 — Principio de inducción prueba las cuatro afirmaciones para todo $n$.

Queda la propiedad de anidamiento para índices arbitrarios. Si $n\leq r$, por la definición aritmética del orden natural existe $k\in\mathbb N$ tal que

$$
n+k=r.
$$

Induciendo sobre $k$ y aplicando en cada paso la propiedad $3$, obtenemos

$$
a_n\leq a_r
$$

y

$$
b_r\leq b_n.
$$

Junto con $a_r<b_r$, resulta

$$
a_n\leq a_r<b_r\leq b_n.
$$

Esto completa la demostración. ∎

> **Nota fundacional.** La dicotomía usada en cada etapa no es una apelación a LEM sobre una
> proposición arbitraria: $m_n^2<2_{\mathbb Q}$ es una comparación racional decidible por P0-B.

---

### Lema 8.7.5 — Las anchuras se hacen arbitrariamente pequeñas

Para todo $\varepsilon\in\mathbb Q$ con $0<\varepsilon$, existe $N\in\mathbb N$ tal que, para todo $n\in\mathbb N$,

$$
N\leq n
\Longrightarrow
0<b_n-a_n<\varepsilon.
$$

**Demostración.**

Escribamos

$$
\delta_n:=b_n-a_n.
$$

Por Lema 8.7.4 — Invariantes de la bisección racional,

$$
0<\delta_n
$$

y

$$
\delta_{S(n)}
=
\frac{\delta_n}{2_{\mathbb Q}}.
$$

Como $\delta_0=1_{\mathbb Q}$, una inducción inmediata da además la fórmula exacta

$$
\boxed{
\delta_n
=
\left(2_{\mathbb Q}^{-1}\right)^n
=
2_{\mathbb Q}^{-n}.
}
$$

Primero estableceremos la estimación

$$
\boxed{
n\neq0
\Longrightarrow
\nu(n)\delta_n\leq1_{\mathbb Q}.
}
$$

La probaremos por inducción, en la forma equivalente

$$
\nu(S(k))\delta_{S(k)}
\leq
1_{\mathbb Q}
\qquad(k\in\mathbb N).
$$

Para $k=0$, tenemos

$$
\delta_0=b_0-a_0
=
2_{\mathbb Q}-1_{\mathbb Q}
=
1_{\mathbb Q},
$$

y por la fórmula de reducción de la anchura,

$$
\delta_1
=
\frac{1_{\mathbb Q}}{2_{\mathbb Q}}.
$$

Como $\nu(1)=1_{\mathbb Q}$ y $1_{\mathbb Q}<2_{\mathbb Q}$, la inversión del orden para positivos (Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (7)) da

$$
0_{\mathbb Q}
<
2_{\mathbb Q}^{-1}
<
1_{\mathbb Q}^{-1}
=
1_{\mathbb Q}.
$$

Por consiguiente,

$$
\nu(1)\delta_1
=
\frac{1_{\mathbb Q}}{2_{\mathbb Q}}
\leq
1_{\mathbb Q}.
$$

Supongamos ahora

$$
\nu(S(k))\delta_{S(k)}
\leq
1_{\mathbb Q}.
$$

Pongamos $r:=S(k)$. En $\mathbb N$ se tiene $1\leq r$. La compatibilidad del orden natural con la suma implica

$$
S(r)=r+1\leq r+r.
$$

Aplicando la incrustación $\nu$ y sus propiedades,

$$
\nu(S(r))
\leq
\nu(r+r)
=
\nu(r)+\nu(r)
=
2_{\mathbb Q}\nu(r).
$$

Como $\delta_r>0$, la compatibilidad del orden con el producto da

$$
\nu(S(r))\delta_r
\leq
2_{\mathbb Q}\nu(r)\delta_r
\leq
2_{\mathbb Q}.
$$

Multiplicando por el inverso positivo de $2_{\mathbb Q}$,

$$
\nu(S(r))
\frac{\delta_r}{2_{\mathbb Q}}
\leq
1_{\mathbb Q}.
$$

Pero

$$
\delta_{S(r)}
=
\frac{\delta_r}{2_{\mathbb Q}},
$$

y por tanto

$$
\nu(S(r))\delta_{S(r)}
\leq1_{\mathbb Q}.
$$

La inducción queda cerrada. Como Teorema 1.2.7 — Predecesor de todo natural no nulo establece que todo natural no nulo es sucesor de algún natural, la estimación vale para todo $n\neq0$.

Sea ahora $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Por la positividad del inverso,

$$
0<\varepsilon^{-1}.
$$

La propiedad arquimediana de $\mathbb Q$, Teorema 3.8.5 — $\mathbb Q$ es arquimediano, proporciona $N\in\mathbb N$ tal que

$$
\varepsilon^{-1}<\nu(N).
$$

Como el miembro izquierdo es positivo,

$$
0<\nu(N),
$$

de modo que $N\neq0$. Por la estimación anterior,

$$
\nu(N)\delta_N\leq1_{\mathbb Q}.
$$

Multiplicando

$$
\varepsilon^{-1}<\nu(N)
$$

por el racional positivo $\varepsilon$ obtenemos

$$
1_{\mathbb Q}<\varepsilon\nu(N).
$$

Por tanto,

$$
\nu(N)\delta_N
<
\varepsilon\nu(N).
$$

Como $\nu(N)>0$, el escalamiento estricto por un factor positivo permite cancelar $\nu(N)$ y concluir

$$
\delta_N<\varepsilon.
$$

Finalmente, si $N\leq n$, el anidamiento de Lema 8.7.4 — Invariantes de la bisección racional da

$$
a_N\leq a_n<b_n\leq b_N,
$$

y por compatibilidad del orden con la suma y la sustracción,

$$
0<\delta_n=b_n-a_n\leq b_N-a_N=\delta_N<\varepsilon.
$$

Esto prueba la afirmación. ∎

> **Auditoría de elección.** Para una precisión $\varepsilon$ se usa una sola instancia de la propiedad arquimediana. No se construye una elección simultánea de índices para todas las precisiones.

> **Módulo efectivo de anchura.** Puesto que $N\mapsto2_{\mathbb Q}^{-N}$ es computable y la
> comparación racional es decidible, podemos buscar sucesivamente el primer $N$ con
> $$ 2_{\mathbb Q}^{-N}<\varepsilon. $$
> La prueba garantiza que la búsqueda termina. Así se obtiene un módulo computable de
> estrechamiento y, usando el anidamiento, un módulo computable de Cauchy para la sucesión inferior.

---

### Teorema 8.7.6 — Una sucesión de Cauchy racional sin límite racional

Sea $a=(a_n)_{n\in\mathbb N}$ la sucesión inferior de la bisección de Proposición 8.7.3 — Existencia y unicidad de las sucesiones de bisección. Entonces

$$
\boxed{
a\in\mathcal C_{\mathbb Q}
}
$$

pero

$$
\boxed{
\forall \ell\in\mathbb Q,
\qquad
a_n\not\to_{\mathbb Q}\ell.
}
$$

**Demostración.**

#### 1. La sucesión $a$ es de Cauchy

Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Por Lema 8.7.5 — Las anchuras se hacen arbitrariamente pequeñas, existe $N\in\mathbb N$ tal que

$$
b_N-a_N<\varepsilon.
$$

Si $m,n\geq N$, el anidamiento de Lema 8.7.4 — Invariantes de la bisección racional da

$$
a_N\leq a_m,a_n<b_m,b_n\leq b_N.
$$

La tricotomía decidible de $\mathbb Q$ permite comparar $a_m$ y $a_n$. En cualquiera de las dos orientaciones,

$$
|a_m-a_n|
\leq b_N-a_N
<\varepsilon.
$$

Luego $a$ es de Cauchy y

$$
a\in\mathcal C_{\mathbb Q}.
$$

#### 2. La sucesión $a$ no posee límite racional

Supongamos que existe $\ell\in\mathbb Q$ tal que

$$
a_n\to_{\mathbb Q}\ell.
$$

Por el anidamiento,

$$
1_{\mathbb Q}=a_0\leq a_n
$$

para todo $n$. Si $\ell<1_{\mathbb Q}$, tomando

$$
\eta:=\frac{1_{\mathbb Q}-\ell}{2_{\mathbb Q}}>0
$$

la convergencia daría, para $n$ suficientemente grande,

$$
a_n<\ell+\eta=\frac{\ell+1_{\mathbb Q}}{2_{\mathbb Q}}<1_{\mathbb Q},
$$

contradicción. Por la tricotomía racional,

$$
1_{\mathbb Q}\leq\ell,
$$

y en particular $0_{\mathbb Q}<\ell$.

Aplicamos ahora Proposición 3.7.6 — Tricotomía decidible de los racionales a $\ell^2$ y $2_{\mathbb Q}$.

**Caso 1: $\ell^2=2_{\mathbb Q}$.** Esto contradice Teorema 3.9.5 — No existe una raíz cuadrada racional de $2$.

**Caso 2: $\ell^2<2_{\mathbb Q}$.** Pongamos

$$
d:=2_{\mathbb Q}-\ell^2>0,
\qquad
h:=\frac{d}{2_{\mathbb Q}(2_{\mathbb Q}\ell+1_{\mathbb Q})}>0,
\qquad
r:=\ell+h.
$$

Como $\ell\geq1_{\mathbb Q}$ y $\ell^2<2_{\mathbb Q}$, tenemos
$0<d\leq1_{\mathbb Q}$ y $2(2\ell+1)\geq6$. En particular $0<h<1_{\mathbb Q}$, luego
$h^2<h$. Así

$$
2\ell h+h^2
<
(2\ell+1)h
=
\frac d2
<
d,
$$

y por tanto

$$
r^2=(\ell+h)^2<2_{\mathbb Q}.
$$

Aplicamos la convergencia con precisión $h/2_{\mathbb Q}$ y el estrechamiento de
Lema 8.7.5 — Las anchuras se hacen arbitrariamente pequeñas con la misma precisión. Para algún $N$,

$$
|a_N-\ell|<\frac h2,
\qquad
b_N-a_N<\frac h2.
$$

Entonces

$$
b_N
=a_N+(b_N-a_N)
<\ell+\frac h2+\frac h2
=r.
$$

Pero Lema 8.7.4 — Invariantes de la bisección racional da $0<b_N$ y $2_{\mathbb Q}<b_N^2$. Como $0<b_N<r$,
Lema 3.9.6 — Estricta monotonía del cuadrado en los racionales no negativos implica

$$
b_N^2<r^2<2_{\mathbb Q},
$$

contradicción.

**Caso 3: $2_{\mathbb Q}<\ell^2$.** Pongamos

$$
d:=\ell^2-2_{\mathbb Q}>0,
\qquad
h:=\frac{d}{2_{\mathbb Q}(2_{\mathbb Q}\ell+1_{\mathbb Q})}>0.
$$

Como $d=\ell^2-2_{\mathbb Q}<\ell^2$ y $\ell\geq1_{\mathbb Q}$,

$$
0<h
<
\frac{\ell^2}{2(2\ell+1)}
<
\ell.
$$

Además,

$$
2\ell h-h^2
<
2\ell h
<
(2\ell+1)h
=
\frac d2
<
d.
$$

Por tanto

$$
(\ell-h)^2
=\ell^2-(2\ell h-h^2)
>2_{\mathbb Q}.
$$

Por la convergencia, para algún $N$,

$$
|a_N-\ell|<h.
$$

La caracterización local de la distancia (Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional) da

$$
\ell-h<a_N.
$$

Como $0<\ell-h<a_N$, Lema 3.9.6 — Estricta monotonía del cuadrado en los racionales no negativos implica

$$
2_{\mathbb Q}
<(\ell-h)^2
<a_N^2,
$$

contradiciendo $a_N^2<2_{\mathbb Q}$ de Lema 8.7.4 — Invariantes de la bisección racional.

Las tres posibilidades de la tricotomía racional son imposibles. Por tanto no existe
$\ell\in\mathbb Q$ con $a_n\to_{\mathbb Q}\ell$. ∎

> **Nota conceptual.** No hemos construido ni utilizado la raíz real de $2$. La contradicción final es completamente local: si existiera un límite racional $\ell$, los intervalos encajados forzarían $\ell^2=2_{\mathbb Q}$, contra Teorema 3.9.5 — No existe una raíz cuadrada racional de $2$. La prueba ya no depende de reconstruir un supremo racional de $S_2$.

> **Auditoría de elección.** El proceso de bisección es recursivo y determinista. Los índices usados en la prueba de Cauchy y en la contradicción de convergencia son testigos locales para precisiones fijadas. No se forma ninguna función de elección.

---

### Corolario 8.7.7 — $\mathbb Q$ no es secuencialmente completo

El cuerpo ordenado $\mathbb Q$ no es secuencialmente completo.

**Demostración.**

Por Teorema 8.7.6 — Una sucesión de Cauchy racional sin límite racional existe una sucesión

$$
a\in\mathcal C_{\mathbb Q}
$$

que no converge racionalmente a ningún elemento de $\mathbb Q$. Esto niega exactamente la condición de Definición 8.7.1 — Completitud secuencial de $\mathbb Q$. ∎

---

### Cierre del capítulo

El capítulo comenzó con procesos racionales y terminó demostrando que algunos de esos procesos desbordan el propio sistema racional.

La cadena obtenida es ahora:

$$
\boxed{
\text{convergencia racional}
\Longrightarrow
\text{Cauchy}
\Longrightarrow
\text{acotación},
}
$$

pero la primera implicación no puede invertirse en $\mathbb Q$:

$$
\boxed{
\exists q\in\mathcal C_{\mathbb Q}
\quad
\forall\ell\in\mathbb Q,
\quad
q_n\not\to_{\mathbb Q}\ell.
}
$$

La insuficiencia que en el capítulo 3 apareció como ausencia de un supremo racional reaparece ahora como ausencia de un límite racional. Hemos conectado, sin recurrir a $\mathbb R_D$, dos manifestaciones de un mismo defecto estructural de $\mathbb Q$.

El siguiente paso no será asignar arbitrariamente un nuevo número a cada sucesión de Cauchy. Distintas sucesiones pueden describir la misma posición asintótica. Antes de formar un nuevo sistema numérico debemos determinar cuándo dos procesos de Cauchy deben considerarse equivalentes y demostrar que las operaciones término a término respetan esa identificación.

Ése será el problema del **Capítulo 9 — El cuerpo de Cauchy**.
