## 3.2. Equivalencia y cociente racional {#sec-ta-3-2}

### Definición 3.2.1 — Relación de equivalencia racional {#ta-relacion-equivalencia-racional}

*Glosario: [relación de equivalencia racional](../otros/tratado-de-analisis-glosario.md#gl-relacion-equivalencia-racional)*

Sobre $D_{\mathbb Q}$ definimos

$$
\boxed{
(a,b)\sim_{\mathbb Q}(c,d)
\iff
ad=bc.
}
$$

La condición utiliza únicamente el producto entero.

### Proposición 3.2.2 — $\sim_{\mathbb Q}$ es una relación de equivalencia {#ta-equivalencia-racional-es-equivalencia}

La relación $\sim_{\mathbb Q}$ es reflexiva, simétrica y transitiva sobre $D_{\mathbb Q}$.

**Demostración.**  
**Reflexividad.** Para $(a,b)\in D_{\mathbb Q}$,

$$
ab=ba
$$

por conmutatividad del producto entero. Luego $(a,b)\sim_{\mathbb Q}(a,b)$.

**Simetría.** Si $ad=bc$, entonces $cb=da$ por simetría de la igualdad y conmutatividad del producto; por tanto $(c,d)\sim_{\mathbb Q}(a,b)$.

**Transitividad.** Supongamos

$$
(a,b)\sim_{\mathbb Q}(c,d)
\qquad\text{y}\qquad
(c,d)\sim_{\mathbb Q}(e,f).
$$

Entonces

$$
ad=bc,
\qquad
cf=de.
$$

Multiplicando la primera igualdad por $f$ y la segunda por $b$,

$$
adf=bcf
\qquad\text{y}\qquad
bcf=bde.
$$

Por transitividad de la igualdad,

$$
adf=bde.
$$

Reordenando factores,

$$
d(af)=d(be).
$$

Como $(c,d)\in D_{\mathbb Q}$, tenemos $d\neq0_{\mathbb Z}$. Por el [Lema 3.1.1 — Cancelación multiplicativa en $\mathbb Z$](#ta-cancelacion-multiplicativa-enteros),

$$
af=be.
$$

Por definición, $(a,b)\sim_{\mathbb Q}(e,f)$. ∎

### Proposición 3.2.3 — Existencia del cociente racional {#ta-existencia-cociente-racional}

Existe el conjunto

$$
D_{\mathbb Q}/{\sim_{\mathbb Q}}.
$$

**Demostración.**  
$D_{\mathbb Q}$ es un conjunto por la [Definición 3.1.6 — Conjunto de representantes racionales](#ta-conjunto-representantes-racionales), y $\sim_{\mathbb Q}$ es una relación de equivalencia por la Proposición 3.2.2. La existencia del cociente es una instancia de la construcción general desarrollada en [§0.5 — Clases de equivalencia, particiones y cocientes](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#sec-ta-0-5). ∎

### Definición 3.2.4 — Conjunto de los números racionales {#ta-conjunto-numeros-racionales}

*Glosario: [número racional](../otros/tratado-de-analisis-glosario.md#gl-numero-racional)*

Definimos

$$
\boxed{
\mathbb Q
:=
D_{\mathbb Q}/{\sim_{\mathbb Q}}.
}
$$

Un **número racional** es un elemento de $\mathbb Q$.

### Notación 3.2.5 — Clases racionales y notación fraccionaria {#ta-clases-racionales-notacion-fraccionaria}

*Glosario: [clase racional](../otros/tratado-de-analisis-glosario.md#gl-clase-racional) · [notación fraccionaria](../otros/tratado-de-analisis-glosario.md#gl-notacion-fraccionaria)*

Para $(a,b)\in D_{\mathbb Q}$ escribiremos

$$
[(a,b)]_{\mathbb Q}
$$

para su clase de equivalencia. A partir de este punto introducimos además la abreviatura

$$
\boxed{
\frac ab
:=
[(a,b)]_{\mathbb Q}.
}
$$

La barra fraccionaria designa, por tanto, **una clase**, no el par representante. La expresión $\frac ab$ sólo está definida cuando $b\neq0_{\mathbb Z}$.

La forma $[a,b]$ continúa reservada para intervalos y no se utilizará para clases racionales.

### Proposición 3.2.6 — Criterio de igualdad de racionales {#ta-criterio-igualdad-racionales}

Para $(a,b),(c,d)\in D_{\mathbb Q}$,

$$
\boxed{
\frac ab=\frac cd
\iff
ad=bc.
}
$$

**Demostración.**  
Por el [Lema 0.5.3 — Igualdad de clases](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-igualdad-clases), dos clases de equivalencia coinciden si y sólo si sus representantes son equivalentes. La definición de $\sim_{\mathbb Q}$ transforma esa condición exactamente en $ad=bc$. ∎

---

::: {.callout-note title="Publicación progresiva"}
Con §3.2 queda construido formalmente el conjunto de los números racionales,

$$
\mathbb Q=D_{\mathbb Q}/{\sim_{\mathbb Q}},
$$

y la escritura $\frac ab$ pasa a designar una clase racional, no un par. La siguiente entrega será **§3.3 — Suma, cero, opuesto y sustracción**.
:::
