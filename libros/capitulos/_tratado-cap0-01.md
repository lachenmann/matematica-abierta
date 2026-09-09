## 0.1. Lenguaje lógico y axiomas conjuntistas disponibles

Antes de construir objetos matemáticos conviene precisar qué parte de la maquinaria se **admite** y qué parte deberá **demostrarse**. La distinción es esencial en un tratado que pretende construir los sistemas numéricos desde fundamentos explícitos: si una propiedad se apoya en un axioma de ZF, queremos poder decir cuál; si se obtiene de definiciones anteriores, queremos verla aparecer como resultado interno.

Esta sección no pretende convertir el tratado en un curso de lógica o teoría de conjuntos. Su función es más austera: fijar el suelo sobre el que caminaremos. A partir de ese suelo, las construcciones posteriores deberán justificarse dentro del propio desarrollo.

### Convención 0.1.1 — Metanivel y nivel objeto {#ta-metanivel-nivel-objeto}

*Glosario: [metanivel](../otros/tratado-de-analisis-glosario.md#gl-metanivel) · [nivel objeto](../otros/tratado-de-analisis-glosario.md#gl-nivel-objeto)*

Distinguiremos permanentemente:

1. el **metanivel**, en el que hablamos de fórmulas, demostraciones, variables, definiciones y dependencias;
2. el **nivel objeto**, en el que las variables recorren conjuntos.

Los numerales usados para numerar capítulos, secciones o resultados pertenecen al metanivel editorial hasta que los números naturales hayan sido construidos.

---

### Convención 0.1.2 — Lógica ambiente {#ta-logica-ambiente}

*Glosario: [lógica clásica](../otros/tratado-de-analisis-glosario.md#gl-logica-clasica)*

Se trabaja en lógica clásica de primer orden con igualdad. Se permiten, entre otros, modus ponens, introducción y eliminación usual de cuantificadores, sustitución de iguales, contrapositiva, reducción al absurdo y tercero excluido.

La igualdad `=` es lógica y primitiva. La pertenencia $\in$ es el único símbolo no lógico primitivo del lenguaje conjuntista.

No registraremos como resultados del tratado las tautologías puramente lógicas.

---

### 0.1.1. Inventario axiomático {#ta-zf}

*Glosario: [ZF](../otros/tratado-de-analisis-glosario.md#gl-zf)*

Los axiomas siguientes son **fundamento admitido**, no teoremas del tratado. Se los reproduce aquí para que las dependencias de las construcciones posteriores sean visibles.

#### Extensionalidad {#ta-axioma-extensionalidad}

*Glosario: [extensionalidad](../otros/tratado-de-analisis-glosario.md#gl-extensionalidad)*

$$
\forall A\,\forall B\,
\Bigl[
\forall x\,(x\in A\leftrightarrow x\in B)
\;\Longrightarrow\;
A=B
\Bigr].
$$

#### Par

Para cualesquiera conjuntos $a,b$ existe un conjunto $P$ cuyos elementos son exactamente $a$ y $b$:

$$
\forall a\,\forall b\,\exists P\,\forall x
\bigl(x\in P\leftrightarrow(x=a\lor x=b)\bigr).
$$

#### Unión

Para todo conjunto $A$ existe un conjunto $U$ tal que

$$
x\in U
\iff
\exists B\,(B\in A\land x\in B).
$$

#### Conjunto potencia

Para todo conjunto $A$ existe un conjunto $P$ tal que

$$
X\in P
\iff
\forall x\,(x\in X\rightarrow x\in A).
$$

#### Esquema de separación

Dado un conjunto $A$ y una fórmula $\varphi(x)$, existe un conjunto $B$ tal que

$$
x\in B
\iff
(x\in A\land\varphi(x)).
$$

#### Esquema de reemplazo

Si una fórmula $\varphi(x,y)$ determina para cada $x\in A$ un único $y$, entonces la colección de esos valores $y$ es un conjunto.

#### Infinito

Usaremos en el capítulo 1 el axioma de infinito. Para evitar utilizar anticipadamente el símbolo $\varnothing$, puede expresarse en una forma equivalente adecuada a este tratado:

$$
\exists I\Bigl[
\exists e\bigl(e\in I\land\forall z\,(z\notin e)\bigr)
\land
\forall x\Bigl(
x\in I\rightarrow
\exists y\bigl(
y\in I\land
\forall z\,(z\in y\leftrightarrow(z\in x\lor z=x))
\bigr)
\Bigr)
\Bigr].
$$

En este capítulo utilizaremos de este axioma únicamente su consecuencia inmediata de que **existe al menos un conjunto**.

#### Fundación

El axioma de fundación está disponible por pertenecer a ZF, pero ningún resultado de este capítulo dependerá de él.

---

### Notación 0.1.3 — Separación restringida {#ta-separacion-restringida}

*Glosario: [separación restringida](../otros/tratado-de-analisis-glosario.md#gl-separacion-restringida)*

Cuando $A$ es un conjunto y $P(x)$ una propiedad, escribiremos

$$
\{x\in A:P(x)\}
$$

para el subconjunto de $A$ cuya existencia garantiza separación.

Esta notación **no** autoriza expresiones irrestrictas de la forma $\{x:P(x)\}$ sin un conjunto ambiente previamente disponible.

---

