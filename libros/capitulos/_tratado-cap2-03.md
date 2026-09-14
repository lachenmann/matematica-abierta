## 2.3. Suma de enteros {#sec-ta-2-3}

En los representantes, la suma natural de diferencias formales es la operación esperable:

$$
(a,b)+(c,d)\leadsto(a+c,b+d).
$$

La intuición proviene de la identidad informal

$$
(a-b)+(c-d)=(a+c)-(b+d),
$$

pero la definición real utilizará solamente suma de naturales.

Antes de descender la operación al cociente, necesitaremos una versión binaria del principio de definición sobre clases.

### Teorema 2.3.1 — Principio de definición binaria sobre clases {#ta-principio-definicion-binaria-clases}

*Glosario: [principio de definición binaria sobre clases](../otros/tratado-de-analisis-glosario.md#gl-definicion-binaria-clases)*

Sea $\sim$ una relación de equivalencia sobre un conjunto $A$, sea $B$ un conjunto y sea

$$
\psi:A\times A\to B
$$

una función tal que, siempre que

$$
a\sim a'
\qquad\text{y}\qquad
b\sim b',
$$

se tenga

$$
\psi(a,b)=\psi(a',b').
$$

Entonces existe una única función

$$
\overline{\psi}:
(A/{\sim})\times(A/{\sim})\to B
$$

tal que

$$
\boxed{
\overline{\psi}([a],[b])=\psi(a,b).
}
$$

**Demostración.**  
Sea

$$
Q:=A/{\sim}.
$$

Como $Q$ y $B$ son conjuntos, también existen $Q\times Q$ y $(Q\times Q)\times B$.

Definimos $G\subseteq(Q\times Q)\times B$ por

$$
\langle\langle C,D\rangle,y\rangle\in G
$$

si y sólo si existen $a,b\in A$ tales que

$$
C=[a],\qquad D=[b],\qquad y=\psi(a,b).
$$

La existencia de $G$ se obtiene por separación.

Debemos probar que $G$ es el grafo de una función con dominio $Q\times Q$.

Sea $\langle C,D\rangle\in Q\times Q$. Por definición de cociente existen $a,b\in A$ con

$$
C=[a],
\qquad
D=[b].
$$

Entonces

$$
\langle\langle C,D\rangle,\psi(a,b)\rangle\in G,
$$

así que existe al menos un valor.

Para la unicidad, supongamos

$$
C=[a]=[a'],
\qquad
D=[b]=[b'].
$$

Por el criterio general de igualdad de clases de equivalencia,

$$
a\sim a',
\qquad
b\sim b'.
$$

La hipótesis de invariancia da

$$
\psi(a,b)=\psi(a',b').
$$

Por tanto el valor asociado a $\langle C,D\rangle$ es único. Así $G$ es el grafo de una función

$$
\overline{\psi}:Q\times Q\to B.
$$

La fórmula

$$
\overline{\psi}([a],[b])=\psi(a,b)
$$

es inmediata de la definición de $G$.

Finalmente, cualquier otra función $F:Q\times Q\to B$ que satisfaga esa misma fórmula coincide con $\overline{\psi}$ en todo par de clases, y por el criterio de igualdad de funciones es igual a ella. ∎

Este teorema no crea ninguna elección de representantes. Precisamente evita tener que escoger uno de manera global.

### Definición 2.3.2 — Suma de diferencias formales {#ta-suma-diferencias-formales}

Definimos

$$
\sigma_{\mathbb Z}:
(\mathbb N\times\mathbb N)\times(\mathbb N\times\mathbb N)
\to
\mathbb N\times\mathbb N
$$

por

$$
\boxed{
\sigma_{\mathbb Z}\bigl((a,b),(c,d)\bigr)
:=
(a+c,b+d).
}
$$

### Proposición 2.3.3 — Compatibilidad de la suma con $\sim_{\mathbb Z}$ {#ta-compatibilidad-suma-enteros}

Si

$$
(a,b)\sim_{\mathbb Z}(a',b')
$$

y

$$
(c,d)\sim_{\mathbb Z}(c',d'),
$$

entonces

$$
(a+c,b+d)\sim_{\mathbb Z}(a'+c',b'+d').
$$

**Demostración.**  
Las hipótesis son

$$
a+b'=b+a',
$$

$$
c+d'=d+c'.
$$

Queremos demostrar

$$
(a+c)+(b'+d')=(b+d)+(a'+c').
$$

Por asociatividad y conmutatividad,

$$
(a+c)+(b'+d')
=
(a+b')+(c+d').
$$

Sustituyendo las igualdades anteriores,

$$
(a+b')+(c+d')
=
(b+a')+(d+c').
$$

Reordenando nuevamente,

$$
(b+a')+(d+c')
=
(b+d)+(a'+c').
$$

Ésta es exactamente la condición requerida. ∎

### Definición 2.3.4 — Suma en $\mathbb Z$ {#ta-suma-enteros}

*Glosario: [suma entera](../otros/tratado-de-analisis-glosario.md#gl-suma-entera)*

La composición de $\sigma_{\mathbb Z}$ con la proyección canónica

$$
\pi_{\mathbb Z}:
\mathbb N\times\mathbb N\to\mathbb Z
$$

es invariante bajo cambio de representantes en ambos argumentos. Por el Teorema 2.3.1 induce una única función

$$
+_{\mathbb Z}:\mathbb Z\times\mathbb Z\to\mathbb Z
$$

tal que

$$
\boxed{
[(a,b)]+_{\mathbb Z}[(c,d)]
=
[(a+c,b+d)].
}
$$

Cuando el tipo sea inequívoco escribiremos simplemente $x+y$.

La buena definición no está contenida en la fórmula: está contenida en la Proposición 2.3.3 y en el principio binario de descenso. Desde este punto la expresión $x+y$ para $x,y\in\mathbb Z$ es una operación genuina sobre clases.
