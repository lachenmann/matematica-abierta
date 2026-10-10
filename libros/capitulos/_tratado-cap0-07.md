## 0.7. Órdenes {#sec-ta-0-7}

El análisis no sólo necesita saber cuándo dos objetos son iguales; necesita compararlos. Más adelante hablaremos de intervalos, cotas, monotonía, supremos y completitud. Todas esas nociones descansan sobre una estructura de orden.

Introducimos aquí únicamente el vocabulario abstracto indispensable. Todavía no afirmamos que los sistemas numéricos posean estos órdenes: en cada construcción posterior habrá que definir la relación correspondiente y demostrar que satisface las propiedades exigidas.

### Definición 0.7.1 — Preorden, orden parcial y orden total {#ta-preorden-orden-parcial-total}

*Glosario: [preorden](../otros/tratado-de-analisis-glosario.md#gl-preorden) · [orden parcial](../otros/tratado-de-analisis-glosario.md#gl-orden-parcial) · [orden total](../otros/tratado-de-analisis-glosario.md#gl-orden-total)*

Sea $\leq$ una relación sobre un conjunto $A$.

- $\leq$ es un preorden si es reflexiva y transitiva.
- $\leq$ es un orden parcial si es reflexiva, antisimétrica y transitiva.
- $\leq$ es un orden total si es un orden parcial y, además, para cualesquiera $a,b\in A$,

$$
a\leq b
\quad\text{o}\quad
b\leq a.
$$

El par $(A,\leq)$ se llamará, respectivamente, conjunto preordenado, parcialmente ordenado o totalmente ordenado.

---

### Definición 0.7.2 — Orden estricto asociado {#ta-orden-estricto}

*Glosario: [orden estricto](../otros/tratado-de-analisis-glosario.md#gl-orden-estricto)*

Si $\leq$ es un orden parcial sobre $A$, definimos

$$
a<b
\quad\Longleftrightarrow\quad
(a\leq b\ \text{y}\ a\neq b).
$$

La relación $<$ se denomina orden estricto asociado a $\leq$.

---

### Proposición 0.7.3 — Propiedades del orden estricto asociado {#ta-propiedades-orden-estricto}
Si $\leq$ es un orden parcial sobre $A$, entonces $<$ es irreflexiva y transitiva.

Si $\leq$ es total, entonces para cualesquiera $a,b\in A$ exactamente una de las siguientes proposiciones es verdadera:

$$
a<b,
\qquad
a=b,
\qquad
b<a.
$$

**Demostración.**  
Irreflexividad: $a<a$ exigiría simultáneamente $a\leq a$ y $a\neq a$, imposible.

Transitividad: si $a<b$ y $b<c$, entonces $a\leq b$ y $b\leq c$, por lo que $a\leq c$. Si $a=c$, de $a\leq b$ y $b\leq a$ se seguiría $a=b$ por antisimetría, contradiciendo $a<b$. Luego $a\neq c$ y, por tanto, $a<c$.

Supongamos ahora que $\leq$ es total. Dados $a,b$, por totalidad $a\leq b$ o $b\leq a$. Si $a=b$, se cumple la alternativa central. Si $a\neq b$, la primera relación produce $a<b$ y la segunda produce $b<a$. No pueden darse simultáneamente $a<b$ y $b<a$, pues implicarían $a\leq b$ y $b\leq a$, y la antisimetría daría $a=b$. ∎

---

### Definición 0.7.4 — Cotas superiores e inferiores {#ta-cotas}

*Glosario: [cota superior](../otros/tratado-de-analisis-glosario.md#gl-cota-superior) · [cota inferior](../otros/tratado-de-analisis-glosario.md#gl-cota-inferior) · [acotado superiormente](../otros/tratado-de-analisis-glosario.md#gl-acotado-superiormente) · [acotado inferiormente](../otros/tratado-de-analisis-glosario.md#gl-acotado-inferiormente)*

Sea $(A,\leq)$ un conjunto parcialmente ordenado y sea $S\subseteq A$.

Un elemento $u\in A$ es una cota superior de $S$ si

$$
\forall s\in S,\quad s\leq u.
$$

Un elemento $\ell\in A$ es una cota inferior de $S$ si

$$
\forall s\in S,\quad \ell\leq s.
$$

Diremos que $S$ está acotado superiormente si posee alguna cota superior y acotado inferiormente si posee alguna cota inferior.

---

### Definición 0.7.5 — Máximo y mínimo {#ta-maximo-minimo}

*Glosario: [máximo](../otros/tratado-de-analisis-glosario.md#gl-maximo) · [mínimo](../otros/tratado-de-analisis-glosario.md#gl-minimo)*

Sea $S\subseteq A$.

Un elemento $m\in S$ es el máximo de $S$ si

$$
\forall s\in S,\quad s\leq m.
$$

Un elemento $n\in S$ es el mínimo de $S$ si

$$
\forall s\in S,\quad n\leq s.
$$

La pertenencia $m,n\in S$ forma parte de la definición y distingue máximo/mínimo de una cota exterior.

---

### Proposición 0.7.6 — Unicidad de máximo y mínimo {#ta-unicidad-maximo-minimo}
Un subconjunto de un conjunto parcialmente ordenado tiene a lo sumo un máximo y a lo sumo un mínimo.

**Demostración.**  
Sean $m,m'$ dos máximos de $S$. Como $m'\in S$ y $m$ es máximo, $m'\leq m$. Como $m\in S$ y $m'$ es máximo, $m\leq m'$. Por antisimetría, $m=m'$.

La prueba para mínimos es dual. ∎

---

### Definición 0.7.7 — Supremo e ínfimo {#ta-supremo-infimo}

*Glosario: [supremo](../otros/tratado-de-analisis-glosario.md#gl-supremo) · [ínfimo](../otros/tratado-de-analisis-glosario.md#gl-infimo)*

Sea $S\subseteq A$.

Un elemento $u\in A$ es el supremo de $S$ si:

1. $u$ es cota superior de $S$;
2. para toda cota superior $v$ de $S$,

$$
u\leq v.
$$

Un elemento $\ell\in A$ es el ínfimo de $S$ si:

1. $\ell$ es cota inferior de $S$;
2. para toda cota inferior $v$ de $S$,

$$
v\leq \ell.
$$

Obsérvese que la definición no afirma que supremo o ínfimo existan.

---

### Proposición 0.7.8 — Unicidad de supremo e ínfimo {#ta-unicidad-supremo-infimo}
Si $S$ posee supremo, éste es único. Si $S$ posee ínfimo, éste es único.

**Demostración.**  
Sean $u$ y $u'$ dos supremos de $S$. Como $u'$ es una cota superior y $u$ es la menor cota superior,

$$
u\leq u'.
$$

Simétricamente,

$$
u'\leq u.
$$

Por antisimetría, $u=u'$. La prueba para el ínfimo es dual. ∎

---

### Corolario 0.7.9 — Notación legítima para supremo e ínfimo {#ta-notacion-sup-inf}
Cuando se haya demostrado que $S$ posee supremo, escribiremos

$$
\sup S
$$

para ese único elemento. Cuando se haya demostrado que posee ínfimo, escribiremos

$$
\inf S.
$$

Las expresiones $\sup S$ e $\inf S$ no se considerarán definidas bajo hipótesis que no garanticen existencia.

---

::: {.callout-tip title="Capítulo 0 completo"}
Con §§0.8–0.10 queda completo el Capítulo 0 — Fundamento lógico y conjuntista. La publicación progresiva continuará con el Capítulo 1 — Los números naturales.
:::
