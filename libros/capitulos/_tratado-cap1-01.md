## 1.1. Conjuntos inductivos y construcción de $\omega$ {#sec-ta-1-1}

La intuición habitual presenta los naturales como una sucesión que comienza en cero y avanza, paso a paso, mediante la operación de tomar el siguiente número. Aquí esa sucesión todavía no existe: debemos producirla usando únicamente conjuntos.

La idea de von Neumann consiste en comenzar con el vacío y hacer que cada nuevo número contenga a todos sus predecesores. Para formalizar el paso de un estadio al siguiente introduciremos enseguida una operación de **sucesor**.

El [axioma de infinito](../otros/tratado-de-analisis-glosario.md#gl-axioma-infinito) nos garantizará que existe al menos un conjunto cerrado bajo este proceso. Sin embargo, no queremos declarar natural a cualquier elemento de cualquier conjunto semejante: un conjunto inductivo puede contener objetos adicionales que nada tienen que ver con la sucesión generada desde el cero. Por eso el verdadero problema será aislar la parte **forzada** por dos exigencias: contener el cero y permanecer cerrada al tomar sucesores.

### Notación 1.1.1 — Cero {#ta-cero}

*Glosario: [cero](../otros/tratado-de-analisis-glosario.md#gl-cero)*

Definimos

$$
\boxed{0:=\varnothing.}
$$

---

### Definición 1.1.2 — Sucesor {#ta-sucesor}

*Glosario: [sucesor](../otros/tratado-de-analisis-glosario.md#gl-sucesor)*

Para cualquier conjunto $x$,

$$
\boxed{S(x):=x\cup\{x\}.}
$$

En particular, $x\in S(x)$.

---

### Definición 1.1.3 — Conjunto inductivo {#ta-conjunto-inductivo}

*Glosario: [conjunto inductivo](../otros/tratado-de-analisis-glosario.md#gl-conjunto-inductivo)*

Un conjunto $I$ es **inductivo** si

1. $0\in I$;
2. $x\in I\Rightarrow S(x)\in I$.

---

### Proposición 1.1.4 — Existencia de un conjunto inductivo {#ta-existencia-conjunto-inductivo}

Existe al menos un conjunto inductivo.

**Demostración.**  
Es el contenido del axioma de infinito, en la forma admitida en el [inventario axiomático del Capítulo 0](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-zf), una vez introducidas las notaciones $0$ y $S$. ∎

La existencia de algún conjunto inductivo resuelve sólo la mitad del problema. Falta extraer de él el menor núcleo que no contenga nada salvo lo que todas las construcciones inductivas están obligadas a contener. La definición siguiente realiza precisamente esa intersección de manera interna, por separación, sin formar una colección ilegítima de «todos los conjuntos inductivos».

---

### Definición 1.1.5 — Núcleo inductivo {#ta-nucleo-inductivo}

*Glosario: [núcleo inductivo](../otros/tratado-de-analisis-glosario.md#gl-nucleo-inductivo)*

Sea $I$ inductivo. Definimos

$$
\omega_I:=\{x\in I:\forall J\,[(J\subseteq I\text{ y }J\text{ inductivo})\Rightarrow x\in J]\}.
$$

Su existencia se obtiene por separación sobre $I$; no se forma «el conjunto de todos los conjuntos inductivos».

---

### Proposición 1.1.6 — $\omega_I$ es inductivo {#ta-omega-i-inductivo}

**Demostración.**  
Todo subconjunto inductivo de $I$ contiene $0$, luego $0\in\omega_I$. Si $x\in\omega_I$, entonces $x\in I$ y por inductividad $S(x)\in I$; además, cada subconjunto inductivo $J\subseteq I$ que contiene $x$ contiene también $S(x)$. Por tanto $S(x)\in\omega_I$. ∎

---

### Teorema 1.1.7 — Minimalidad {#ta-minimalidad-omega}

Si $I$ es inductivo y $J$ es cualquier conjunto inductivo, entonces

$$
\omega_I\subseteq J.
$$

**Demostración.**  
$I\cap J$ es un subconjunto inductivo de $I$. Por definición de $\omega_I$, todo elemento de $\omega_I$ pertenece a $I\cap J$, y por tanto a $J$. ∎

---

### Teorema 1.1.8 — Independencia del conjunto inductivo inicial {#ta-independencia-omega}

Si $I$ y $J$ son inductivos, entonces

$$
\omega_I=\omega_J.
$$

**Demostración.**  
Como $\omega_J$ es inductivo, la minimalidad da $\omega_I\subseteq\omega_J$; intercambiando $I$ y $J$, $\omega_J\subseteq\omega_I$. Aplicamos doble inclusión. ∎

La minimalidad muestra que $\omega_I$ está contenido en todo conjunto inductivo; la independencia demuestra algo todavía más importante: el resultado no depende del conjunto $I$ que usamos como ambiente inicial. Hemos obtenido, por tanto, un objeto **canónico**. Ya podemos retirar el subíndice auxiliar y reconocer en este conjunto el sistema de los naturales.

---

### Notación 1.1.9 — $\omega$ y $\mathbb N$ {#ta-omega-naturales}

*Glosario: [$\omega$](../otros/tratado-de-analisis-glosario.md#gl-omega) · [números naturales](../otros/tratado-de-analisis-glosario.md#gl-numeros-naturales)*

Denotamos por $\omega$ el conjunto común $\omega_I$ y definimos

$$
\boxed{\mathbb N:=\omega.}
$$

Así $0\in\mathbb N$, $\mathbb N$ es inductivo y está contenido en todo conjunto inductivo.

---

### Teorema 1.1.10 — Principio de inducción {#ta-principio-induccion}

*Glosario: [principio de inducción](../otros/tratado-de-analisis-glosario.md#gl-principio-induccion)*

Sea $A\subseteq\mathbb N$. Si $0\in A$ y $n\in A\Rightarrow S(n)\in A$, entonces

$$
A=\mathbb N.
$$

Equivalentemente, si una propiedad $P$ satisface $P(0)$ y $P(n)\Rightarrow P(S(n))$, entonces vale para todo $n\in\mathbb N$.

**Demostración.**  
Las hipótesis hacen de $A$ un conjunto inductivo. Por minimalidad $\mathbb N\subseteq A$; junto con $A\subseteq\mathbb N$, obtenemos igualdad. La versión para $P$ se aplica a $\{n\in\mathbb N:P(n)\}$. ∎

---

::: {.callout-note title="Publicación progresiva"}
Con §1.1 queda construida canónicamente $\mathbb N=\omega$ y demostrado el principio de inducción. La siguiente entrega será **§1.2 — Estructura de los naturales y Peano**, donde las propiedades de Peano aparecerán como teoremas de esta construcción, no como axiomas adicionales.
:::
