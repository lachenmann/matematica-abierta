## 12.4. Construcción del transporte por cortes racionales {#sec-ta-12-4}

Sean

$$
(E,\iota_E)
\qquad\text{y}\qquad
(F,\iota_F)
$$

dos completaciones ordenadas de $\mathbb Q$. Por Corolario 12.2.9 — La copia racional de toda completación es la copia canónica, las incrustaciones que forman parte de esos datos coinciden necesariamente con las copias racionales canónicas:

$$
\iota_E=\jmath_{\mathbb Q}^{E},
\qquad
\iota_F=\jmath_{\mathbb Q}^{F}.
$$

No identificaremos por ello $\mathbb Q$ con un subconjunto literal de $E$ o de $F$. La comparación se realizará siempre a través de esas funciones.

La idea es asociar a cada elemento de un cuerpo ordenado la totalidad de los racionales que quedan estrictamente por debajo de él. En un cuerpo arquimediano, esa información forma una cortadura de Dedekind. Si después trasladamos la misma cortadura a otro cuerpo completo, su imagen racional tendrá un supremo. Ese supremo será el elemento correspondiente.

### Definición 12.4.1 — Traza racional inferior de un elemento

Sea $E$ un cuerpo ordenado. Para cada $x\in E$ definimos su traza racional inferior por

$$
\boxed{
L_E(x)
:=
\{q\in\mathbb Q:\jmath_{\mathbb Q}^{E}(q)<x\}.
}
$$

Así obtenemos una función

$$
\boxed{
L_E:E\longrightarrow\mathcal P(\mathbb Q).
}
$$

Para cada $x\in E$, el conjunto $L_E(x)$ existe por Separación dentro de $\mathbb Q$. Como ese subconjunto está determinado de manera única por la fórmula anterior, el grafo

$$
\{\langle x,\alpha\rangle\in E\times\mathcal P(\mathbb Q):
\alpha=L_E(x)\}
$$

define una función. No se selecciona ningún racional asociado a $x$.

La definición tiene sentido en cualquier cuerpo ordenado. Para que $L_E(x)$ sea una cortadura necesitaremos además que la copia racional sea densa.

> **Nota fundacional.** La traza es un subconjunto extensional perfectamente definido de $\mathbb Q$, pero eso no implica que su pertenencia sea decidible. En general,
> $$ \boxed{ \text{traza extensional} \neq \text{membresía decidible}. } $$
> Decidir $q\in L_E(x)$ equivale a decidir la comparación estricta $\jmath_{\mathbb Q}^{E}(q)<x$, algo que no está disponible uniformemente en un cuerpo ordenado completo arbitrario.

### Proposición 12.4.2 — La traza racional de un cuerpo arquimediano es una cortadura

Sea $E$ un cuerpo ordenado arquimediano y sea $x\in E$. Entonces

$$
\boxed{L_E(x)\in\mathbb R_D.}
$$

Es decir, $L_E(x)$ es una cortadura de Dedekind de $\mathbb Q$.

**Demostración.**

Verificamos las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind.

**No vaciedad.** En todo cuerpo ordenado,

$$
0_E<1_E,
$$

de modo que

$$
x-1_E<x.
$$

Por Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano, existe $q_-\in\mathbb Q$ tal que

$$
x-1_E
<
\jmath_{\mathbb Q}^{E}(q_-)
<
x.
$$

Por definición, $q_-\in L_E(x)$. Luego

$$
L_E(x)\neq\varnothing.
$$

**Propiedad.** De nuevo,

$$
x<x+1_E.
$$

La densidad racional proporciona $q_+\in\mathbb Q$ con

$$
x
<
\jmath_{\mathbb Q}^{E}(q_+)
<
x+1_E.
$$

Por tanto

$$
q_+\notin L_E(x),
$$

y así

$$
L_E(x)\neq\mathbb Q.
$$

**Clausura inferior.** Sean $r\in L_E(x)$ y $s\in\mathbb Q$ con $s<r$. Entonces

$$
\jmath_{\mathbb Q}^{E}(r)<x.
$$

Como Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados afirma que $\jmath_{\mathbb Q}^{E}$ preserva el orden estricto,

$$
\jmath_{\mathbb Q}^{E}(s)
<
\jmath_{\mathbb Q}^{E}(r)
<
x.
$$

Luego $s\in L_E(x)$.

**Ausencia de máximo.** Sea $r\in L_E(x)$. Entonces

$$
\jmath_{\mathbb Q}^{E}(r)<x.
$$

Aplicando otra vez Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano al intervalo abierto entre esos dos elementos, existe $s\in\mathbb Q$ tal que

$$
\jmath_{\mathbb Q}^{E}(r)
<
\jmath_{\mathbb Q}^{E}(s)
<
x.
$$

La segunda desigualdad da $s\in L_E(x)$, y la reflexión del orden estricto de Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados da

$$
r<s.
$$

Por tanto $L_E(x)$ no posee máximo.

Se cumplen las cuatro condiciones de cortadura y, por Definición 5.1.3 — Conjunto subyacente del modelo de Dedekind,

$$
L_E(x)\in\mathbb R_D.
$$

∎

### Lema 12.4.3 — La imagen transportada de una traza es no vacía y acotada

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$, y sea $x\in E$. Entonces el subconjunto de $F$

$$
\boxed{
\jmath_{\mathbb Q}^{F}[L_E(x)]
}
$$

es no vacío y está acotado superiormente en $F$.

**Demostración.**

Como $E$ es una completación ordenada, Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo proporciona densidad de la copia racional canónica en $E$.

Por los axiomas de cuerpo ordenado,

$$
x-1_E<x<x+1_E.
$$

Aplicando la densidad al intervalo $(x-1_E,x)$, existe $r\in\mathbb Q$ tal que

$$
x-1_E
<
\jmath_{\mathbb Q}^{E}(r)
<
x.
$$

Por Definición 12.4.1 — Traza racional inferior de un elemento,

$$
r\in L_E(x).
$$

Luego

$$
\jmath_{\mathbb Q}^{F}(r)
\in
\jmath_{\mathbb Q}^{F}[L_E(x)],
$$

y la imagen está habitada; en particular, es no vacía.

Para construir una cota superior, aplicamos de nuevo la densidad, ahora al intervalo $(x,x+1_E)$. Existe $u\in\mathbb Q$ con

$$
x
<
\jmath_{\mathbb Q}^{E}(u)
<
x+1_E.
$$

Sea $s\in L_E(x)$. Entonces

$$
\jmath_{\mathbb Q}^{E}(s)<x<\jmath_{\mathbb Q}^{E}(u).
$$

Como Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados refleja el orden estricto racional,

$$
s<u.
$$

Aplicando la preservación del orden por la copia racional de $F$,

$$
\jmath_{\mathbb Q}^{F}(s)
<
\jmath_{\mathbb Q}^{F}(u).
$$

Por tanto

$$
\boxed{
\jmath_{\mathbb Q}^{F}(u)
}
$$

es una cota superior de

$$
\jmath_{\mathbb Q}^{F}[L_E(x)].
$$

∎

> **Nota fundacional.** La prueba usa testigos positivos producidos directamente por densidad para el elemento fijo $x$; ya no convierte las afirmaciones negativas
> $$ L_E(x)\neq\varnothing, \qquad L_E(x)\neq\mathbb Q $$
> en testigos. La clasicidad permanece exactamente donde corresponde: en la densidad abstracta heredada de Corolario 12.3.2 — Densidad racional en todo cuerpo ordenado completo.
>

### Definición 12.4.4 — Transporte canónico determinado por cortes racionales

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Para cada $x\in E$, Lema 12.4.3 — La imagen transportada de una traza es no vacía y acotada demuestra que

$$
\jmath_{\mathbb Q}^{F}[L_E(x)]
$$

es no vacío y está acotado superiormente. Como $F$ es completo, posee un supremo en $F$.

Definimos

$$
\boxed{
\Psi_{E,F}:E\longrightarrow F
}
$$

por

$$
\boxed{
\Psi_{E,F}(x)
:=
\sup\bigl(\jmath_{\mathbb Q}^{F}[L_E(x)]\bigr).
}
$$

La notación $\sup$ es legítima por Corolario 0.7.9 — Notación legítima para supremo e ínfimo, y su valor es único por Proposición 0.7.8 — Unicidad de supremo e ínfimo. Por tanto, para cada $x\in E$ existe un único $y\in F$ que satisface la fórmula anterior. El grafo de $\Psi_{E,F}$ se obtiene entonces por Separación dentro de $E\times F$.

La definición no escoge un elemento de $F$ entre varios candidatos. El valor está determinado de manera única como un supremo.

> **Nota fundacional.** Aquí «canónico» significa únicamente determinado por la estructura. La propiedad del supremo garantiza existencia y unicidad extensional, pero no proporciona un procedimiento uniforme para calcular el supremo a partir de una presentación arbitraria de la traza. Por tanto,
> $$ \boxed{ \text{canónico por unicidad} \neq \text{computable}. } $$

### Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Entonces, para todo $x\in E$,

$$
\boxed{
L_F\bigl(\Psi_{E,F}(x)\bigr)
=
L_E(x).
}
$$

**Demostración.**

Fijemos $x\in E$ y escribamos, sólo dentro de esta demostración,

$$
A:=\jmath_{\mathbb Q}^{F}[L_E(x)].
$$

Por definición,

$$
\Psi_{E,F}(x)=\sup A.
$$

Demostraremos la igualdad de las dos trazas por doble inclusión.

Sea primero $q\in L_E(x)$. Como $L_E(x)$ es una cortadura, no posee máximo. Existe por tanto $r\in L_E(x)$ tal que

$$
q<r.
$$

La preservación estricta del orden por $\jmath_{\mathbb Q}^{F}$ da

$$
\jmath_{\mathbb Q}^{F}(q)
<
\jmath_{\mathbb Q}^{F}(r).
$$

Además,

$$
\jmath_{\mathbb Q}^{F}(r)\in A,
$$

y todo elemento de $A$ es menor o igual que su supremo. Luego

$$
\jmath_{\mathbb Q}^{F}(q)
<
\jmath_{\mathbb Q}^{F}(r)
\le
\sup A
=
\Psi_{E,F}(x).
$$

Por Definición 12.4.1 — Traza racional inferior de un elemento, esto significa

$$
q\in L_F\bigl(\Psi_{E,F}(x)\bigr).
$$

Así,

$$
L_E(x)
\subseteq
L_F\bigl(\Psi_{E,F}(x)\bigr).
$$

Para la inclusión inversa, sea $q\in\mathbb Q$ y supongamos

$$
q\notin L_E(x).
$$

Si $r\in L_E(x)$, entonces necesariamente $r<q$: de lo contrario la totalidad del orden racional daría $q\le r$, y la igualdad o la clausura inferior de la cortadura implicarían $q\in L_E(x)$, contradicción.

Por consiguiente,

$$
\jmath_{\mathbb Q}^{F}(r)
<
\jmath_{\mathbb Q}^{F}(q)
$$

para todo $r\in L_E(x)$. Así $\jmath_{\mathbb Q}^{F}(q)$ es una cota superior de $A$. Por la propiedad definitoria del supremo,

$$
\Psi_{E,F}(x)
=
\sup A
\le
\jmath_{\mathbb Q}^{F}(q).
$$

En particular no puede ocurrir

$$
\jmath_{\mathbb Q}^{F}(q)
<
\Psi_{E,F}(x).
$$

Por Definición 12.4.1 — Traza racional inferior de un elemento,

$$
q\notin L_F\bigl(\Psi_{E,F}(x)\bigr).
$$

Hemos demostrado

$$
q\notin L_E(x)
\Longrightarrow
q\notin L_F\bigl(\Psi_{E,F}(x)\bigr),
$$

y por contrapositiva,

$$
L_F\bigl(\Psi_{E,F}(x)\bigr)
\subseteq
L_E(x).
$$

Las dos inclusiones y Teorema 0.2.4 — Criterio extensional por doble inclusión dan

$$
L_F\bigl(\Psi_{E,F}(x)\bigr)
=
L_E(x).
$$

∎

> **Nota fundacional.** La segunda inclusión es una frontera clásica real, no sólo una elección estilística de prueba. Una demostración positiva a partir de
> $$ \jmath_{\mathbb Q}^{F}(q)<\sup A $$
> necesitaría producir algún $a\in A$ con $\jmath_{\mathbb Q}^{F}(q)<a$. La completitud clásica garantiza el supremo, pero no incorpora ese testigo de aproximación desde abajo. La prueba actual evita esa extracción trabajando por contrapositiva; obtener el testigo directamente requeriría información positiva adicional sobre la completitud o una negación clásica de cuantificadores.

El teorema expresa el núcleo de la construcción. El elemento $\Psi_{E,F}(x)$ no se ha obtenido intentando copiar la codificación conjuntista de $x$; se ha reconstruido exclusivamente a partir de su posición racional. La completitud del cuerpo de llegada interviene exactamente una vez: garantiza que esa posición racional tiene una frontera interna.

Todavía no hemos demostrado que $\Psi_{E,F}$ preserve el orden, sea biyectiva o respete las operaciones. El paso siguiente será mostrar que en un cuerpo completo la traza racional inferior determina completamente el orden de sus elementos. La identidad de trazas recién probada convertirá entonces a $\Psi_{E,F}$ en un isomorfismo de órdenes. Ése será el contenido de §12.5.
