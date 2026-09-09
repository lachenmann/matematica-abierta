## 0.4. Relaciones {#sec-ta-0-4}

El producto cartesiano reúne todos los pares posibles entre dos conjuntos. Una **relación** selecciona algunos de esos pares. Esta observación convierte una noción aparentemente nueva en una construcción conjuntista ya controlada: relacionar elementos de $A$ con elementos de $B$ será simplemente especificar un subconjunto de $A\times B$.

Esta perspectiva es la que permitirá tratar, con un mismo lenguaje, equivalencias, órdenes y grafos funcionales.

### Definición 0.4.1 — Relación binaria {#ta-relacion-binaria}

*Glosario: [relación binaria](../otros/tratado-de-analisis-glosario.md#gl-relacion-binaria)*

Una **relación binaria de $A$ en $B$** es un conjunto

$$
R\subseteq A\times B.
$$

Cuando $A=B$, diremos simplemente que $R$ es una relación sobre $A$.

Escribiremos

$$
aRb
$$

como abreviatura de

$$
\langle a,b\rangle\in R.
$$

---

### Definición 0.4.2 — Dominio y recorrido de una relación {#ta-dominio-recorrido-relacion}

*Glosario: [dominio de una relación](../otros/tratado-de-analisis-glosario.md#gl-dominio-relacion) · [recorrido de una relación](../otros/tratado-de-analisis-glosario.md#gl-recorrido-relacion)*

Si $R\subseteq A\times B$, definimos

$$
\operatorname{dom}R
:=
\{a\in A:\exists b\in B\;(aRb)\},
$$

y

$$
\operatorname{ran}R
:=
\{b\in B:\exists a\in A\;(aRb)\}.
$$

Usaremos `ran` para recorrido de una relación y reservaremos `im` para la imagen de un subconjunto bajo una función.

---

### Definición 0.4.3 — Relación inversa {#ta-relacion-inversa}

*Glosario: [relación inversa](../otros/tratado-de-analisis-glosario.md#gl-relacion-inversa)*

Si $R\subseteq A\times B$, definimos

$$
R^{-1}
:=
\{\langle b,a\rangle\in B\times A:aRb\}.
$$

---

### Definición 0.4.4 — Composición de relaciones {#ta-composicion-relaciones}

*Glosario: [composición de relaciones](../otros/tratado-de-analisis-glosario.md#gl-composicion-relaciones)*

Sean

$$
R\subseteq A\times B,
\qquad
S\subseteq B\times C.
$$

Definimos la composición **$S$ después de $R$** por

$$
S\circ R
:=
\{
\langle a,c\rangle\in A\times C:
\exists b\in B\;(aRb\land bSc)
\}.
$$

La dirección de la composición se leerá de derecha a izquierda, igual que para funciones.

---

### Proposición 0.4.5 — Tipo de la inversa y de la composición
Si $R\subseteq A\times B$ y $S\subseteq B\times C$, entonces

$$
R^{-1}\subseteq B\times A
$$

y

$$
S\circ R\subseteq A\times C.
$$

**Demostración.**  
Ambas inclusiones forman parte de las condiciones definitorias de las Definiciones 0.4.3 y 0.4.4: cada construcción se obtiene por separación dentro del producto cartesiano correspondiente. ∎

---

### Definición 0.4.6 — Propiedades de una relación {#ta-propiedades-relacion}

*Glosario: [reflexividad](../otros/tratado-de-analisis-glosario.md#gl-reflexividad) · [simetría](../otros/tratado-de-analisis-glosario.md#gl-simetria) · [antisimetría](../otros/tratado-de-analisis-glosario.md#gl-antisimetria) · [transitividad](../otros/tratado-de-analisis-glosario.md#gl-transitividad) · [totalidad](../otros/tratado-de-analisis-glosario.md#gl-totalidad)*

Sea $R$ una relación sobre $A$.

- $R$ es **reflexiva** si $\forall a\in A,\ aRa$.
- $R$ es **simétrica** si $aRb\Rightarrow bRa$.
- $R$ es **antisimétrica** si $(aRb\land bRa)\Rightarrow a=b$.
- $R$ es **transitiva** si $(aRb\land bRc)\Rightarrow aRc$.
- $R$ es **total** o **conexa** si para cualesquiera $a,b\in A$, $aRb$ o $bRa$.

---

### Definición 0.4.7 — Relación de equivalencia {#ta-relacion-equivalencia}

*Glosario: [relación de equivalencia](../otros/tratado-de-analisis-glosario.md#gl-relacion-equivalencia)*

Una relación $\sim$ sobre $A$ es una **relación de equivalencia** si es reflexiva, simétrica y transitiva.

---

::: {.callout-note title="Publicación progresiva"}
Esta entrega del capítulo comprende ya §§0.0–0.4. La siguiente incorporará **0.5 — Clases de equivalencia, particiones y cocientes** y continuará en el orden del manuscrito maestro.

El [**Glosario matemático del Tratado**](../otros/tratado-de-analisis-glosario.md) se actualiza en paralelo: esta incorporación añade **relación binaria**, **dominio**, **recorrido**, **relación inversa**, **composición**, **reflexividad**, **simetría**, **antisimetría**, **transitividad**, **totalidad** y **relación de equivalencia**.
:::
