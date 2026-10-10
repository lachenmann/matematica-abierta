## 11.4. Preservación de suma y producto {#sec-ta-11-4}

La aplicación $\Phi$ ya está definida sobre todo $\mathbb R_C$, pero hasta aquí sólo sabemos cómo leer su valor a partir de un representante. Antes de comparar operaciones conviene eliminar también esa dependencia expositiva: la cortadura $\Phi(x)$ puede reconocerse directamente a partir de la posición de $x$ respecto de la copia racional en $\mathbb R_C$.

Este criterio será el puente entre las dos aritméticas. Para la suma permitirá traducir la pertenencia a una suma de cortaduras en una desigualdad en $\mathbb R_C$ y volver de ella mediante densidad racional. Para el producto habrá que respetar una dificultad adicional ya presente en el Capítulo 6: la multiplicación de Dedekind se construyó primero sobre cortaduras estrictamente positivas y sólo después se extendió por signos. Seguiremos exactamente ese orden.

### Lema 11.4.1 — Traza racional de $\Phi(x)$

Para todo $x\in\mathbb R_C$ y todo $q\in\mathbb Q$,

$$
\boxed{
q\in\Phi(x)
\iff
\iota_C(q)<_C x.
}
$$

**Demostración.**

Fijemos $x\in\mathbb R_C$. Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy existe una sucesión $a\in\mathcal C_{\mathbb Q}$ tal que

$$
x=[a]_C.
$$

Para este representante local, Definición 11.3.1 — Aplicación canónica de Cauchy a Dedekind da

$$
\Phi(x)=\Phi([a]_C)=\mathcal L_C(a).
$$

Por Proposición 11.1.2 — Caracterización mediante el orden de $\mathbb R_C$, para todo $q\in\mathbb Q$,

$$
q\in\mathcal L_C(a)
\iff
\iota_C(q)<_C[a]_C.
$$

Sustituyendo las dos igualdades anteriores obtenemos

$$
q\in\Phi(x)
\iff
\iota_C(q)<_C x.
$$

∎

El lema muestra que $\Phi(x)$ es exactamente la traza racional inferior de $x$ dentro del cuerpo de Cauchy. Esta descripción no identifica los modelos: el miembro izquierdo es pertenencia a una cortadura de $\mathbb R_D$ y el derecho es una desigualdad en $\mathbb R_C$.

### Proposición 11.4.2 — Preservación de la suma

Para todos $x,y\in\mathbb R_C$,

$$
\boxed{
\Phi(x+y)=\Phi(x)+_D\Phi(y).
}
$$

**Demostración.**

Demostraremos igualdad de cortaduras por extensionalidad. Fijemos $r\in\mathbb Q$.

Supongamos primero

$$
r\in\Phi(x)+_D\Phi(y).
$$

Por Definición 6.1.4 — Adición de Dedekind y Definición 6.1.2 — Conjunto suma de dos cortaduras, existen $p,q\in\mathbb Q$ tales que

$$
p\in\Phi(x),
\qquad
q\in\Phi(y),
\qquad
r=p+q.
$$

El lema anterior da

$$
\iota_C(p)<_C x,
\qquad
\iota_C(q)<_C y.
$$

Como $\mathbb R_C$ es un cuerpo ordenado (Teorema 9.10.3 — $\mathbb R_C$ es un cuerpo ordenado), la invariancia estricta por traslación permite sumar las desigualdades y obtener

$$
\iota_C(p)+\iota_C(q)<_C x+y.
$$

Por Proposición 9.9.3 — Preservación de la aritmética racional, $\iota_C$ preserva la suma racional, de modo que

$$
\iota_C(r)
=
\iota_C(p+q)
=
\iota_C(p)+\iota_C(q)
<_C x+y.
$$

Aplicando Lema 11.4.1 — Traza racional de $\Phi(x)$ a $x+y$,

$$
r\in\Phi(x+y).
$$

Así

$$
\Phi(x)+_D\Phi(y)\subseteq\Phi(x+y).
$$

Recíprocamente, supongamos

$$
r\in\Phi(x+y).
$$

Entonces

$$
\iota_C(r)<_C x+y.
$$

Trasladando por $-y$ en el cuerpo ordenado $\mathbb R_C$,

$$
\iota_C(r)-y<_C x.
$$

La densidad de la copia racional, Corolario 10.6.2 — Densidad de la copia racional en $\mathbb R_C$, proporciona un racional $p\in\mathbb Q$ tal que

$$
\iota_C(r)-y
<_C
\iota_C(p)
<_C
x.
$$

Definimos en $\mathbb Q$

$$
q:=r-p.
$$

De la primera desigualdad, trasladando términos en $\mathbb R_C$ y usando la preservación de la aritmética racional por $\iota_C$, se obtiene

$$
\iota_C(q)
=
\iota_C(r-p)
=
\iota_C(r)-\iota_C(p)
<_C y.
$$

Por Lema 11.4.1 — Traza racional de $\Phi(x)$,

$$
p\in\Phi(x),
\qquad
q\in\Phi(y).
$$

Además, por construcción,

$$
r=p+q.
$$

Por la definición de la suma de Dedekind,

$$
r\in\Phi(x)+_D\Phi(y).
$$

Hemos probado ambas inclusiones; Teorema 0.2.4 — Criterio extensional por doble inclusión da la igualdad de cortaduras.

∎

### Corolario 11.4.3 — Preservación del cero y del opuesto

Para todo $x\in\mathbb R_C$,

$$
\boxed{
\Phi(0_C)=0_D
}
$$

y

$$
\boxed{
\Phi(-x)=-_D\Phi(x).
}
$$

**Demostración.**

Para la primera igualdad, sea $q\in\mathbb Q$. Por Lema 11.4.1 — Traza racional de $\Phi(x)$,

$$
q\in\Phi(0_C)
\iff
\iota_C(q)<_C0_C.
$$

Como $\iota_C(0_{\mathbb Q})=0_C$ por Proposición 9.9.3 — Preservación de la aritmética racional y $\iota_C$ refleja el orden estricto por Proposición 9.9.5 — Preservación y reflexión del orden racional,

$$
\iota_C(q)<_C0_C
\iff
q<0_{\mathbb Q}.
$$

La última condición equivale a $q\in0_D$ por Definición 6.2.1 — Cero de Dedekind. Por extensionalidad,

$$
\Phi(0_C)=0_D.
$$

Para el opuesto, la preservación de la suma da

$$
\Phi(x)+_D\Phi(-x)
=
\Phi(x+(-x))
=
\Phi(0_C)
=
0_D.
$$

Por otra parte, la definición del opuesto de Dedekind y su ley aditiva dan

$$
\Phi(x)+_D(-_D\Phi(x))=0_D.
$$

La cancelación aditiva en $\mathbb R_D$, Proposición 6.3.11 — Cancelación aditiva en $\mathbb R_D$, implica

$$
\Phi(-x)=-_D\Phi(x).
$$

∎

Este corolario no introduce una comparación general de órdenes entre los dos modelos. Registra únicamente las dos identidades algebraicas que serán necesarias para extender el producto desde el cono positivo a todos los signos.

### Lema 11.4.4 — Preservación del producto en el cono positivo

Sean $x,y\in\mathbb R_C$ tales que

$$
0_C<_C x,
\qquad
0_C<_C y.
$$

Entonces

$$
\Phi(x),\Phi(y)\in\mathbb R_D^{>0}
$$

y

$$
\boxed{
\Phi(xy)=\Phi(x)\cdot_D^+\Phi(y).
}
$$

**Demostración.**

Como $\iota_C(0_{\mathbb Q})=0_C<_Cx$, Lema 11.4.1 — Traza racional de $\Phi(x)$ da

$$
0_{\mathbb Q}\in\Phi(x).
$$

Por Lema 6.4.2 — Caracterizaciones de la positividad, esto equivale a

$$
0_D<_D\Phi(x).
$$

Análogamente,

$$
0_D<_D\Phi(y).
$$

Por tanto ambos factores pertenecen a $\mathbb R_D^{>0}$ y el producto $\cdot_D^+$ está legítimamente definido.

Probemos ahora la igualdad por extensionalidad. Fijemos $r\in\mathbb Q$.

Supongamos primero

$$
r\in\Phi(x)\cdot_D^+\Phi(y).
$$

Por Definición 6.4.4 — Candidato a producto positivo, existen racionales $p,q$ tales que

$$
0<p,
\qquad
0<q,
\qquad
p\in\Phi(x),
\qquad
q\in\Phi(y),
\qquad
r<pq.
$$

Por Lema 11.4.1 — Traza racional de $\Phi(x)$,

$$
\iota_C(p)<_Cx,
\qquad
\iota_C(q)<_Cy.
$$

Como $p,q>0$ y $\iota_C$ preserva el orden, ambos $\iota_C(p)$ y $\iota_C(q)$ son positivos. En el cuerpo ordenado $\mathbb R_C$ podemos multiplicar sucesivamente por factores positivos:

$$
\iota_C(p)\iota_C(q)
<_C
x\iota_C(q)
<_C
xy.
$$

Además, de $r<pq$ y Proposición 9.9.3 — Preservación de la aritmética racional–Proposición 9.9.5 — Preservación y reflexión del orden racional se obtiene

$$
\iota_C(r)
<_C
\iota_C(pq)
=
\iota_C(p)\iota_C(q).
$$

Por transitividad,

$$
\iota_C(r)<_Cxy,
$$

y Lema 11.4.1 — Traza racional de $\Phi(x)$ da

$$
r\in\Phi(xy).
$$

Así

$$
\Phi(x)\cdot_D^+\Phi(y)
\subseteq
\Phi(xy).
$$

Para la inclusión recíproca, sea

$$
r\in\Phi(xy).
$$

Entonces

$$
\iota_C(r)<_Cxy.
$$

Distinguimos dos casos racionales.

**Caso 1: $r\leq0$.** Por densidad de $\iota_C[\mathbb Q]$ entre $0_C$ y $x$, existe $p\in\mathbb Q$ tal que

$$
0_C<_C\iota_C(p)<_Cx.
$$

De modo análogo existe $q\in\mathbb Q$ con

$$
0_C<_C\iota_C(q)<_Cy.
$$

La reflexión del orden por $\iota_C$ da $p,q>0$. Entonces $pq>0$, y de $r\leq0<pq$ se sigue

$$
r<pq.
$$

El lema de traza racional da $p\in\Phi(x)$ y $q\in\Phi(y)$; por Definición 6.4.4 — Candidato a producto positivo,

$$
r\in\Phi(x)\cdot_D^+\Phi(y).
$$

**Caso 2: $0<r$.** Como $y>0_C$, su inverso es positivo por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado. Multiplicando

$$
\iota_C(r)<_Cxy
$$

por $y^{-1}>0_C$, obtenemos

$$
\iota_C(r)y^{-1}<_Cx.
$$

El miembro izquierdo es positivo. Por densidad racional existe $p\in\mathbb Q$ tal que

$$
\iota_C(r)y^{-1}
<_C
\iota_C(p)
<_C
x.
$$

En particular $0_C<_C\iota_C(p)$, luego $p>0$ por reflexión del orden. Multiplicando la primera desigualdad por $y>0_C$ y reordenando,

$$
\iota_C(r)<_C\iota_C(p)y.
$$

Como $\iota_C(p)>0_C$, su inverso es positivo, y por tanto

$$
\iota_C(r)\,\iota_C(p)^{-1}<_Cy.
$$

El miembro izquierdo vuelve a ser positivo. Una segunda aplicación de la densidad racional proporciona $q\in\mathbb Q$ con

$$
\iota_C(r)\,\iota_C(p)^{-1}
<_C
\iota_C(q)
<_C
y.
$$

Así $q>0$. Multiplicando la primera desigualdad por $\iota_C(p)>0_C$ obtenemos

$$
\iota_C(r)
<_C
\iota_C(p)\iota_C(q)
=
\iota_C(pq).
$$

Como $\iota_C$ refleja el orden,

$$
r<pq.
$$

Además, las desigualdades $\iota_C(p)<_Cx$ y $\iota_C(q)<_Cy$ implican, por Lema 11.4.1 — Traza racional de $\Phi(x)$,

$$
p\in\Phi(x),
\qquad
q\in\Phi(y).
$$

Por Definición 6.4.4 — Candidato a producto positivo, nuevamente

$$
r\in\Phi(x)\cdot_D^+\Phi(y).
$$

Ambos casos establecen la inclusión recíproca. Por extensionalidad,

$$
\Phi(xy)=\Phi(x)\cdot_D^+\Phi(y).
$$

∎

La demostración anterior es la única parte realmente analítica de la compatibilidad multiplicativa: expresa que todo racional situado bajo $xy$ queda por debajo de algún producto $pq$ con $0<p<x$ y $0<q<y$, donde las comparaciones se entienden a través de $\iota_C$.

### Proposición 11.4.5 — Preservación del producto

Para todos $x,y\in\mathbb R_C$,

$$
\boxed{
\Phi(xy)=\Phi(x)\cdot_D\Phi(y).
}
$$

**Demostración.**

Como $\mathbb R_C$ es un cuerpo ordenado, cada factor es negativo, nulo o positivo. Distinguimos los casos exigidos por la propia definición signada del producto de Dedekind.

**1. Algún factor es nulo.** Si, por ejemplo, $x=0_C$, entonces $xy=0_C$ y, por Corolario 11.4.3 — Preservación del cero y del opuesto,

$$
\Phi(xy)=0_D=\Phi(x).
$$

Como $\Phi(x)=0_D$, la rama nula de Definición 6.5.4 — Producto signado candidato–Definición 6.5.6 — Multiplicación de Dedekind da

$$
\Phi(x)\cdot_D\Phi(y)=0_D.
$$

El caso $y=0_C$ es idéntico.

**2. Ambos factores son positivos.** Si $0_C<_Cx$ y $0_C<_Cy$, Lema 11.4.4 — Preservación del producto en el cono positivo da

$$
\Phi(xy)=\Phi(x)\cdot_D^+\Phi(y),
$$

con $\Phi(x),\Phi(y)>_D0_D$. En esta rama, Definición 6.5.6 — Multiplicación de Dedekind coincide con el producto positivo, por lo que

$$
\Phi(xy)=\Phi(x)\cdot_D\Phi(y).
$$

**3. Ambos factores son negativos.** Supongamos

$$
x<_C0_C,
\qquad
y<_C0_C.
$$

Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado, $-x$ y $-y$ son positivos, y Lema 4.1.2 — Identidades algebraicas elementales en un cuerpo da

$$
xy=(-x)(-y).
$$

Aplicando el caso positivo y después Corolario 11.4.3 — Preservación del cero y del opuesto,

$$
\begin{aligned}
\Phi(xy)
&=\Phi((-x)(-y))\\
&=\Phi(-x)\cdot_D^+\Phi(-y)\\
&=(-_D\Phi(x))\cdot_D^+(-_D\Phi(y)).
\end{aligned}
$$

Además, $\Phi(-x)$ y $\Phi(-y)$ son positivas por Lema 11.4.4 — Preservación del producto en el cono positivo; como

$$
\Phi(-x)=-_D\Phi(x),
\qquad
\Phi(-y)=-_D\Phi(y),
$$

Lema 6.5.3 — El opuesto intercambia los signos implica que $\Phi(x)$ y $\Phi(y)$ son negativas. La rama «negativo por negativo» de Definición 6.5.4 — Producto signado candidato es precisamente

$$
\Phi(x)\cdot_D\Phi(y)
=
(-_D\Phi(x))\cdot_D^+(-_D\Phi(y)),
$$

por lo que se obtiene la igualdad buscada.

**4. Signos opuestos.** Supongamos primero

$$
0_C<_Cx,
\qquad
y<_C0_C.
$$

Entonces $-y>_C0_C$ y

$$
xy=-\bigl(x(-y)\bigr)
$$

por Lema 4.1.2 — Identidades algebraicas elementales en un cuerpo. Utilizando sucesivamente la preservación del opuesto y el caso positivo,

$$
\begin{aligned}
\Phi(xy)
&=\Phi\bigl(-(x(-y))\bigr)\\
&=-_D\Phi\bigl(x(-y)\bigr)\\
&=-_D\bigl(\Phi(x)\cdot_D^+\Phi(-y)\bigr)\\
&=-_D\bigl(\Phi(x)\cdot_D^+(-_D\Phi(y))\bigr).
\end{aligned}
$$

Aquí $\Phi(x)>_D0_D$ y $\Phi(-y)=-_D\Phi(y)>_D0_D$, de donde Lema 6.5.3 — El opuesto intercambia los signos da $\Phi(y)<_D0_D$. La expresión final es exactamente la rama «positivo por negativo» de Definición 6.5.4 — Producto signado candidato, y por tanto

$$
\Phi(xy)=\Phi(x)\cdot_D\Phi(y).
$$

Supongamos finalmente

$$
x<_C0_C,
\qquad
0_C<_Cy.
$$

Entonces $-x>_C0_C$ y

$$
xy=-\bigl((-x)y\bigr).
$$

Por Corolario 11.4.3 — Preservación del cero y del opuesto y el caso positivo,

$$
\begin{aligned}
\Phi(xy)
&=\Phi\bigl(-((-x)y)\bigr)\\
&=-_D\Phi\bigl((-x)y\bigr)\\
&=-_D\bigl(\Phi(-x)\cdot_D^+\Phi(y)\bigr)\\
&=-_D\bigl((-_D\Phi(x))\cdot_D^+\Phi(y)\bigr).
\end{aligned}
$$

Aquí $-_D\Phi(x)=\Phi(-x)>_D0_D$ y $\Phi(y)>_D0_D$; por Lema 6.5.3 — El opuesto intercambia los signos, $\Phi(x)<_D0_D$. La última expresión es exactamente la rama «negativo por positivo» de Definición 6.5.4 — Producto signado candidato. Por consiguiente,

$$
\Phi(xy)=\Phi(x)\cdot_D\Phi(y).
$$

Los casos son exhaustivos por la totalidad del orden de $\mathbb R_C$. Queda demostrada la preservación del producto para todos $x,y$.

∎
