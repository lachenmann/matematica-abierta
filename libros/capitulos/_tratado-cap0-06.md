## 0.6. Funciones {#sec-ta-0-6}

Una función puede describirse informalmente como una regla que asigna a cada entrada una única salida. Para el desarrollo posterior necesitamos una versión más precisa: una función debe ser un **objeto matemático identificable**, con dominio y codominio determinados y con un grafo que registre todas sus asignaciones.

Esta decisión tendrá consecuencias reales. Dos funciones con los mismos pares entrada–salida pero codominios distintos no serán idénticas en nuestro formalismo. A cambio obtenemos una noción de función cuyo tipo está siempre explícito y que puede manipularse enteramente dentro de ZF.

### Definición 0.6.1 — Función como dominio, codominio y grafo {#ta-funcion}

*Glosario: [función](../otros/tratado-de-analisis-glosario.md#gl-funcion) · [dominio de una función](../otros/tratado-de-analisis-glosario.md#gl-dominio-funcion) · [codominio](../otros/tratado-de-analisis-glosario.md#gl-codominio) · [grafo de una función](../otros/tratado-de-analisis-glosario.md#gl-grafo-funcion)*

Una **función** $f$ de $A$ en $B$ es el dato

$$
f=\langle A,B,G_f\rangle,
$$

donde

$$
G_f\subseteq A\times B
$$

y

$$
\forall a\in A\;\exists!b\in B
\quad
\langle a,b\rangle\in G_f.
$$

El conjunto $A$ es el **dominio**, $B$ el **codominio** y $G_f$ el **grafo**.

---

### Notación 0.6.2 — Flecha y evaluación {#ta-flecha-evaluacion}

Para una función con dominio $A$ y codominio $B$, escribiremos

$$
f:A\to B.
$$

Si $a\in A$, el único $b\in B$ tal que $\langle a,b\rangle\in G_f$ se denotará

$$
f(a).
$$

La expresión $f(a)$ es abreviatura de una relación de pertenencia al grafo; no es una operación primitiva.

> **Nota fundacional.** La definición anterior fija una función como objeto **extensional**: dominio, codominio y grafo determinan completamente la aplicación. Esto no proporciona, por sí solo, un procedimiento efectivo para obtener $f(a)$ a partir de una codificación de $a$. Mantendremos explícita la distinción
>
> $$
> \boxed{\text{función conjuntista}\neq\text{algoritmo de evaluación}.}
> $$

---

### Proposición 0.6.3 — Criterio de igualdad de funciones {#ta-igualdad-funciones}

Sean

$$
f=\langle A,B,G_f\rangle,
\qquad
g=\langle C,D,G_g\rangle
$$

funciones. Entonces

$$
f=g
$$

si y sólo si

$$
A=C,\qquad B=D,\qquad G_f=G_g.
$$

**Demostración.**  
La afirmación se sigue del criterio característico del par ordenado aplicado recursivamente a la codificación de triples fijada en el Capítulo 0. ∎

**Escolio.** El codominio forma parte de la identidad de una función. Dos aplicaciones con el mismo grafo y dominios iguales, pero codominios distintos, son formalmente funciones distintas.

---

### Definición 0.6.4 — Identidad y composición de funciones {#ta-identidad-composicion-funciones}

*Glosario: [función identidad](../otros/tratado-de-analisis-glosario.md#gl-funcion-identidad) · [composición de funciones](../otros/tratado-de-analisis-glosario.md#gl-composicion-funciones)*

Para un conjunto $A$, definimos la función identidad

$$
\operatorname{id}_A:A\to A,
\qquad
\operatorname{id}_A(a)=a.
$$

Si

$$
f:A\to B,
\qquad
g:B\to C,
$$

definimos

$$
g\circ f:A\to C
$$

por

$$
(g\circ f)(a):=g(f(a)).
$$

Su grafo coincide con la composición relacional de los grafos correspondientes.

---

### Proposición 0.6.5 — Asociatividad y leyes de identidad {#ta-asociatividad-identidad-funciones}

Si

$$
f:A\to B,\qquad
g:B\to C,\qquad
h:C\to D,
$$

entonces

$$
h\circ(g\circ f)=(h\circ g)\circ f,
$$

y

$$
\operatorname{id}_B\circ f=f,
\qquad
f\circ\operatorname{id}_A=f.
$$

**Demostración.**  
Las funciones comparadas tienen, en cada igualdad, el mismo dominio y codominio. Para cada $a\in A$,

$$
[h\circ(g\circ f)](a)
=
h(g(f(a)))
=
[(h\circ g)\circ f](a).
$$

Por unicidad de los valores, sus grafos coinciden; por la Proposición 0.6.3, las funciones son iguales. Las leyes de identidad se prueban del mismo modo. ∎

---

### Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad {#ta-inyectiva-sobreyectiva-biyectiva}

*Glosario: [inyectividad](../otros/tratado-de-analisis-glosario.md#gl-inyectividad) · [sobreyectividad](../otros/tratado-de-analisis-glosario.md#gl-sobreyectividad) · [biyectividad](../otros/tratado-de-analisis-glosario.md#gl-biyectividad)*

Sea $f:A\to B$.

- $f$ es **inyectiva** si $f(a)=f(a')\Rightarrow a=a'$.
- $f$ es **sobreyectiva** si para todo $b\in B$ existe $a\in A$ tal que $f(a)=b$.
- $f$ es **biyectiva** si es inyectiva y sobreyectiva.

---

### Teorema 0.6.7 — Caracterización de las funciones invertibles {#ta-funciones-invertibles}

Una función $f:A\to B$ es biyectiva si y sólo si existe una función $g:B\to A$ tal que

$$
g\circ f=\operatorname{id}_A
\qquad\text{y}\qquad
f\circ g=\operatorname{id}_B.
$$

En tal caso, $g$ es única.

**Demostración.**  
Supongamos primero que $f$ es biyectiva. Para cada $b\in B$, por sobreyectividad existe $a\in A$ con $f(a)=b$; por inyectividad, tal $a$ es único. Definimos

$$
G_g
:=
\{\langle b,a\rangle\in B\times A:f(a)=b\}.
$$

Este conjunto existe por separación y determina una función $g:B\to A$. Por construcción,

$$
g(f(a))=a
$$

para todo $a\in A$, y

$$
f(g(b))=b
$$

para todo $b\in B$. Luego las dos composiciones son las identidades correspondientes.

Recíprocamente, supongamos que existe $g$ con ambas identidades. Si $f(a)=f(a')$, aplicando $g$ obtenemos

$$
a=g(f(a))=g(f(a'))=a',
$$

por lo que $f$ es inyectiva. Para cada $b\in B$, tomando $a=g(b)$ obtenemos

$$
f(a)=f(g(b))=b,
$$

de modo que $f$ es sobreyectiva.

Finalmente, si $g$ y $g'$ satisfacen las dos identidades, entonces

$$
g
=
g\circ\operatorname{id}_B
=
g\circ(f\circ g')
=
(g\circ f)\circ g'
=
\operatorname{id}_A\circ g'
=
g',
$$

usando la Proposición 0.6.5. ∎

---

### Notación 0.6.8 — Función inversa {#ta-funcion-inversa}

*Glosario: [función inversa](../otros/tratado-de-analisis-glosario.md#gl-funcion-inversa)*

Si $f:A\to B$ es biyectiva, denotaremos por

$$
f^{-1}:B\to A
$$

la única función cuya existencia garantiza el Teorema 0.6.7.

El símbolo $f^{-1}$ **no** se utilizará para una función antes de demostrar que $f$ es biyectiva. Para relaciones, $R^{-1}$ conserva el significado fijado en la sección de relaciones binarias.

---

### Definición 0.6.9 — Imagen y preimagen {#ta-imagen-preimagen}

*Glosario: [imagen directa](../otros/tratado-de-analisis-glosario.md#gl-imagen-directa) · [preimagen](../otros/tratado-de-analisis-glosario.md#gl-preimagen)*

Sea $f:A\to B$.

Para $X\subseteq A$, definimos la **imagen directa**

$$
f[X]
:=
\{b\in B:\exists x\in X\;(f(x)=b)\}.
$$

Para $Y\subseteq B$, definimos la **preimagen**

$$
f^{-1}[Y]
:=
\{a\in A:f(a)\in Y\}.
$$

Los corchetes distinguen estas operaciones sobre subconjuntos de la evaluación $f(a)$ y, en el caso biyectivo, de la función inversa $f^{-1}$.

---

### Proposición 0.6.10 — Leyes elementales de preimagen {#ta-leyes-preimagen}

Si $f:A\to B$ y $Y,Z\subseteq B$, entonces

$$
f^{-1}[Y\cup Z]
=
f^{-1}[Y]\cup f^{-1}[Z],
$$

$$
f^{-1}[Y\cap Z]
=
f^{-1}[Y]\cap f^{-1}[Z],
$$

y

$$
f^{-1}[B\setminus Y]
=
A\setminus f^{-1}[Y].
$$

**Demostración.**  
Para la primera igualdad, sea $a\in A$. Entonces

$$
\begin{aligned}
a\in f^{-1}[Y\cup Z]
&\iff f(a)\in Y\cup Z\\
&\iff (f(a)\in Y\lor f(a)\in Z)\\
&\iff (a\in f^{-1}[Y]\lor a\in f^{-1}[Z])\\
&\iff a\in f^{-1}[Y]\cup f^{-1}[Z].
\end{aligned}
$$

Por extensionalidad, los conjuntos son iguales. Las otras dos identidades se prueban mediante la misma cadena de equivalencias. ∎

---

### Definición 0.6.11 — Conjunto de funciones {#ta-conjunto-funciones}

*Glosario: [conjunto de funciones](../otros/tratado-de-analisis-glosario.md#gl-conjunto-funciones)*

Para conjuntos $A,B$, denotaremos por

$$
B^A
$$

el conjunto de todas las funciones $f:A\to B$.

La notación recuerda la convención habitual de que el dominio aparece en el exponente.

---

### Proposición 0.6.12 — Existencia de $B^A$ {#ta-existencia-conjunto-funciones}

Para cualesquiera conjuntos $A,B$, $B^A$ existe como conjunto.

**Demostración.**  
Por la existencia del producto cartesiano, $A\times B$ es un conjunto y, por conjunto potencia,

$$
\mathcal P(A\times B)
$$

es un conjunto. Formemos

$$
U:=\{A,B\}\cup\mathcal P(A\times B)
$$

y después

$$
V:=U\cup\mathcal P(\mathcal P(U)).
$$

Ambos existen usando únicamente par, unión y conjunto potencia.

Sea ahora $G\in\mathcal P(A\times B)$. Entonces $A,B,G\in U$. Por la codificación de pares de Kuratowski, $\langle B,G\rangle\in\mathcal P(\mathcal P(U))$, y por tanto $A,\langle B,G\rangle\in V$. Aplicando una vez más la misma codificación,

$$
\langle A,B,G\rangle
=
\langle A,\langle B,G\rangle\rangle
\in
\mathcal P(\mathcal P(V)).
$$

Tenemos así un conjunto ambiente fijo que contiene todos los triples candidatos. Por separación existe

$$
T
:=
\left\{
 t\in\mathcal P(\mathcal P(V)):
 \exists G\in\mathcal P(A\times B)
 \;t=\langle A,B,G\rangle
\right\}.
$$

Separamos ahora dentro de $T$ aquellos triples $\langle A,B,G\rangle$ cuyo tercer componente satisface

$$
\forall a\in A\;\exists!b\in B\;
\langle a,b\rangle\in G.
$$

El subconjunto resultante existe por separación y, por la Definición 0.6.1, es exactamente $B^A$. ∎

> **Nota fundacional.** Esta construcción no necesita Reemplazo: conjunto potencia, par, unión y separación bastan para obtener un conjunto ambiente que contiene todas las funciones $A\to B$. Tampoco interviene Choice: no seleccionamos una función de una familia de conjuntos; formamos la totalidad extensional de los grafos que satisfacen una propiedad definible.

### Definición 0.6.13 — Proyección canónica de un cociente {#ta-proyeccion-canonica}

*Glosario: [proyección canónica](../otros/tratado-de-analisis-glosario.md#gl-proyeccion-canonica)*

Sea $\sim$ una relación de equivalencia sobre $A$. Definimos

$$
\pi_{\sim}:A\to A/{\sim},
\qquad
\pi_{\sim}(a):=[a].
$$

Cuando la relación sea inequívoca, escribiremos simplemente $\pi$.

---

### Proposición 0.6.14 — Sobreyectividad de la proyección canónica {#ta-sobreyectividad-proyeccion}

La proyección canónica

$$
\pi_{\sim}:A\to A/{\sim}
$$

es sobreyectiva.

**Demostración.**  
Sea $C\in A/{\sim}$. Por la definición del cociente existe $a\in A$ tal que $C=[a]$. Entonces

$$
\pi_{\sim}(a)=[a]=C.
$$

Por la definición de sobreyectividad, $\pi_{\sim}$ es sobreyectiva. ∎

---

La proyección es sobreyectiva: toda clase tiene al menos un representante. Esto plantea el problema que aparecerá repetidamente en los próximos capítulos. Supongamos que sabemos calcular una cantidad a partir de un representante $a$. ¿Cuándo ese cálculo define realmente una función de la clase $[a]$ y no depende de la representación elegida?

La respuesta es: exactamente cuando el cálculo toma el mismo valor sobre representantes equivalentes. El teorema siguiente formaliza esa idea y será nuestra herramienta básica de **buena definición** sobre cocientes.

### Teorema 0.6.15 — Principio de definición sobre clases {#ta-definicion-sobre-clases}

*Glosario: [principio de definición sobre clases](../otros/tratado-de-analisis-glosario.md#gl-definicion-sobre-clases)*

Sea $\sim$ una relación de equivalencia sobre $A$, sea $B$ un conjunto y sea

$$
\varphi:A\to B
$$

una función que satisface

$$
a\sim a'
\quad\Longrightarrow\quad
\varphi(a)=\varphi(a').
$$

Entonces existe una única función

$$
\overline{\varphi}:A/{\sim}\to B
$$

tal que

$$
\overline{\varphi}\circ\pi_{\sim}=\varphi.
$$

Equivalente y sugestivamente,

$$
\overline{\varphi}([a])=\varphi(a).
$$

**Demostración.**  
**Existencia.** Definamos una relación $G$ sobre $(A/{\sim})\times B$ por

$$
\langle C,b\rangle\in G
$$

si y sólo si existe $a\in A$ tal que

$$
C=[a]
\qquad\text{y}\qquad
b=\varphi(a).
$$

Debemos demostrar que $G$ es funcional y total sobre $A/{\sim}$.

Sea $C\in A/{\sim}$. Por definición del cociente, existe $a\in A$ con $C=[a]$; entonces $\langle C,\varphi(a)\rangle\in G$. Por tanto existe al menos un valor.

Supongamos ahora que

$$
C=[a]=[a']
$$

y que los valores propuestos son $\varphi(a)$ y $\varphi(a')$. Por el [Lema 0.5.3 — Igualdad de clases](#ta-igualdad-clases), $a\sim a'$. La hipótesis de constancia sobre clases da

$$
\varphi(a)=\varphi(a').
$$

Por tanto el valor es único. Así $G$ es el grafo de una función $\overline{\varphi}:A/{\sim}\to B$.

Para todo $a\in A$,

$$
(\overline{\varphi}\circ\pi_{\sim})(a)
=
\overline{\varphi}([a])
=
\varphi(a),
$$

de modo que las dos funciones son iguales.

**Unicidad.** Si $\psi:A/{\sim}\to B$ satisface $\psi\circ\pi_{\sim}=\varphi$, sea $C\in A/{\sim}$. Por sobreyectividad de $\pi_{\sim}$, existe $a\in A$ con $C=\pi_{\sim}(a)$. Entonces

$$
\psi(C)
=
\psi(\pi_{\sim}(a))
=
\varphi(a)
=
\overline{\varphi}(\pi_{\sim}(a))
=
\overline{\varphi}(C).
$$

Por el criterio de igualdad de funciones, $\psi=\overline{\varphi}$. ∎

> **Regla operativa.** Toda definición posterior sobre $\mathbb Z$, $\mathbb Q$ o $\mathbb R_C$ que use representantes será una aplicación concreta de este principio o contendrá una prueba equivalente de buena definición.

---

### Definición 0.6.16 — Familia indexada {#ta-familia-indexada}

*Glosario: [familia indexada](../otros/tratado-de-analisis-glosario.md#gl-familia-indexada)*

Una **familia indexada** de elementos de un conjunto $X$, con conjunto de índices $I$, es una función

$$
x:I\to X.
$$

Escribiremos

$$
(x_i)_{i\in I}
$$

en lugar de la función $x$, con $x_i:=x(i)$.

Si $U$ es un conjunto y la familia toma valores en $\mathcal P(U)$, escribiremos $(A_i)_{i\in I}$ y definiremos

$$
\bigcup_{i\in I}A_i
:=
\bigcup \operatorname{ran}(A),
$$

y

$$
\bigcap_{i\in I}A_i
:=
\{x\in U:\forall i\in I\;(x\in A_i)\}.
$$

Para $I=\varnothing$, esta última definición da $\bigcap_{i\in I}A_i=U$; por ello el conjunto ambiente $U$ forma parte de la convención.

---
