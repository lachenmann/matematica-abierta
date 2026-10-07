---
title: "Ejercicios — Capítulo 0"
content-id: MA-BCH-0176
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-000-EJERCICIOS
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-10-07
date-modified: 2026-10-07
areas: [analisis]
level: universitario
topics: [analisis-real, numeros-reales, completitud]
prerequisites: []
related: [MA-BOK-0010]
provenance:
  type: original
  sources:
    - "ANM-C00_EJERCICIOS.md, fuente canónica ANM; paquete C00 cerrado."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 0](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md) · [Ejercicios](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.md)

## §0.1. ¿Existen los números reales?

[]{#MA-EX-ANM-01-000-001}

[]{#MA-SEC-ANM-01-000-001}

[]{#MA-SOL-ANM-01-000-001}

### 1. Auditar una especificación antes de usarla

Sea $F$ un candidato desconocido equipado con dos operaciones y una relación de orden. Considera las cuatro expresiones siguientes, donde $A\subseteq F$:

1. $A\le u$.
2. Para todo $x\in F$ existe $y\in F$ tal que $xy=1$.
3. Si $A\ne\varnothing$ y existe $u\in F$ tal que $a\le u$ para todo $a\in A$, entonces existe $s\in F$ que es menor o igual que toda cota superior de $A$ y que, a la vez, satisface $a\le s$ para todo $a\in A$.
4. $\sup A\in A$.

Para cada expresión, decide cuál de las siguientes descripciones es la más adecuada:

- está mal tipada o mal cuantificada y necesita reparación;
- está bien formada, pero afirma más de lo que exige la especificación de un cuerpo ordenado completo;
- expresa correctamente una parte de la especificación.

Reescribe correctamente las expresiones 1 y 2. En la expresión 4 no supongas que el supremo deba pertenecer al conjunto sólo porque exista.

[]{#MA-EX-ANM-01-000-002}

[]{#MA-SOL-ANM-01-000-002}

### 2. Una existencia demostrada suponiendo que ya existe

Un estudiante propone la siguiente demostración:

> «Definimos los números reales como los elementos de un cuerpo ordenado completo. Sea entonces $F$ un cuerpo ordenado completo. Por definición, $F$ es un cuerpo, su orden es compatible con las operaciones y todo subconjunto no vacío acotado superiormente tiene supremo en $F$. Por tanto, $F$ cumple exactamente las propiedades pedidas. Luego existe al menos un cuerpo ordenado completo.»

Audita el argumento.

1. Localiza la primera presuposición que impide que esto sea una prueba de existencia.
2. Explica qué afirmación condicional sí sería legítimo deducir si se permitiera comenzar con «sea $F$ un cuerpo ordenado completo».
3. Explica qué clase de trabajo matemático faltaría para convertir la especificación en una auténtica prueba de existencia.

No construyas todavía ningún modelo concreto.

[]{#MA-EX-ANM-01-000-003}

[]{#MA-SOL-ANM-01-000-003}

### 3. Qué tendría que certificar un modelo

Supón que una construcción futura entrega un objeto concreto $M$ junto con operaciones $+$, $\cdot$ y una relación $\le$. Un informe de verificación se divide en cuatro etapas:

- **I. Construcción:** $M$ y sus operaciones están definidos como objetos matemáticos concretos.
- **II. Álgebra:** con esas operaciones, $M$ satisface los axiomas de cuerpo.
- **III. Orden:** $\le$ es un orden lineal compatible con la suma y el producto.
- **IV. Completitud:** todo subconjunto no vacío de $M$ acotado superiormente posee un supremo en $M$.

Responde:

1. ¿Por qué la etapa I, por sí sola, no resuelve la pregunta de existencia planteada en §0.1?
2. ¿Por qué las etapas I–III todavía no bastan?
3. Explica por qué completar I–IV sí permite concluir que existe al menos un cuerpo ordenado completo.
4. Si otra construcción produjera después un objeto $N$ que también superara I–IV, ¿qué nueva pregunta quedaría abierta sin volver a poner en duda la existencia?

Tu respuesta debe separar con claridad **construir**, **verificar** y **comparar estructuras**.

## §0.2. Extender sin perder estructura: de $\mathbb N$ a $\mathbb Q$

[]{#MA-EX-ANM-01-000-004}

[]{#MA-SEC-ANM-01-000-002}

[]{#MA-SOL-ANM-01-000-004}

### 4. Qué significa realmente cada flecha

Considera la cadena

$$
\mathbb N
\xhookrightarrow{\ \iota_{\mathbb N\mathbb Z}\ }
\mathbb Z
\xhookrightarrow{\ \iota_{\mathbb Z\mathbb Q}\ }
\mathbb Q.
$$

Un informe preliminar describe ambas flechas diciendo simplemente:

> «Son inclusiones de cuerpos que conservan toda la estructura».

Repara esa descripción.

1. Para la flecha $\mathbb N\to\mathbb Z$, enumera qué datos de la estructura disponible en $\mathbb N$ deben preservarse según §0.2.
2. Para la flecha $\mathbb Z\to\mathbb Q$, enumera qué datos adicionales están disponibles en el dominio y deben preservarse.
3. Explica por qué no está autorizado llamar «inclusión literal» a ninguna de las dos flechas antes de identificar el dominio con su imagen.
4. Explica por qué la expresión «inclusiones de cuerpos» está mal tipada para la cadena completa.

El objetivo es producir una descripción estructuralmente correcta, no sólo corregir vocabulario.

[]{#MA-EX-ANM-01-000-005}

[]{#MA-SOL-ANM-01-000-005}

### 5. Construir la flecha directa de $\mathbb N$ a $\mathbb Q$

Usa únicamente las dos incrustaciones canónicas de §0.2 para construir una aplicación

$$
\iota_{\mathbb N\mathbb Q}:\mathbb N\longrightarrow\mathbb Q.
$$

1. Defínela como composición de las dos flechas conocidas.
2. Escribe explícitamente las imágenes de $0,1,2,3$.
3. Muestra que, para $m,n\in\mathbb N$,

$$
\iota_{\mathbb N\mathbb Q}(m+n)
=
\iota_{\mathbb N\mathbb Q}(m)
+
\iota_{\mathbb N\mathbb Q}(n),
$$

y

$$
\iota_{\mathbb N\mathbb Q}(mn)
=
\iota_{\mathbb N\mathbb Q}(m)\,
\iota_{\mathbb N\mathbb Q}(n).
$$

4. Explica por qué la aplicación es inyectiva y por qué conserva el orden.
5. Indica qué identificación notacional permite, después de estas verificaciones, escribir cómodamente $\mathbb N\subseteq\mathbb Q$.

No uses inclusión literal como punto de partida: debe aparecer sólo al final como convención sustentada por la construcción.

[]{#MA-EX-ANM-01-000-006}

[]{#MA-SOL-ANM-01-000-006}

### 6. La composición de incrustaciones vuelve a ser una incrustación

Sean $A,B,C$ sistemas ordenados con suma y producto, y supón que

$$
\iota:A\hookrightarrow B,
\qquad
\kappa:B\hookrightarrow C
$$

son aplicaciones inyectivas que conservan suma, producto y orden en el sentido de

$$
a<a'
\iff
\iota(a)<\iota(a'),
$$

y análogamente para $\kappa$.

Demuestra que la composición

$$
\kappa\circ\iota:A\longrightarrow C
$$

también es una incrustación al mismo nivel estructural.

Tu prueba debe verificar por separado:

1. inyectividad;
2. preservación de la suma;
3. preservación del producto;
4. preservación y reflexión del orden.

Concluye explicando por qué este resultado justifica leer la cadena

$$
\mathbb N\hookrightarrow\mathbb Z\hookrightarrow\mathbb Q
$$

también como una vía estructural directa de $\mathbb N$ hacia $\mathbb Q$.

[]{#MA-EX-ANM-01-000-007}

[]{#MA-SOL-ANM-01-000-007}

### 7. Una aplicación inyectiva no basta

Un estudiante propone

$$
f:\mathbb Z\longrightarrow\mathbb Q,
\qquad
f(n)=2n,
$$

y afirma:

> «Como $f$ es inyectiva y conserva el orden, podemos usarla para identificar $\mathbb Z$ con una copia de sí misma dentro de $\mathbb Q$ exactamente del mismo modo que con la incrustación canónica».

Audita la afirmación.

1. Comprueba que $f$ es inyectiva.
2. Determina si conserva el orden.
3. Determina si conserva la suma.
4. Comprueba qué ocurre con $1$ y con el producto.
5. Decide con precisión qué parte de la estructura de $\mathbb Z$ sí transporta fielmente $f$ y por qué no sirve como la incrustación de anillos ordenados requerida en §0.2.
6. Explica qué error conceptual cometeríamos si, a partir de la mera inyectividad, escribiéramos sin más $\mathbb Z\subseteq\mathbb Q$ identificando $n$ con $2n$.

## §0.3. El obstáculo: $\mathbb Q$ no está completo

[]{#MA-EX-ANM-01-000-008}

[]{#MA-SEC-ANM-01-000-003}

[]{#MA-SOL-ANM-01-000-008}

### 8. Construir un racional que escape por la derecha

Trabaja únicamente en $\mathbb Q$ y considera

$$
S_2=\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

1. Verifica que $S_2$ es no vacío y que $2$ es una cota superior racional.
2. Sea $s\in\mathbb Q$ tal que $1\le s$ y $s^2<2$. Define

$$
\delta=\frac{2-s^2}{4s+4}.
$$

Demuestra que $\delta\in\mathbb Q$, que $0<\delta<1$ y que

$$
u=s+\delta
$$

satisface $u>s$ y $u\in S_2$.
3. Explica qué propiedad impediría que un racional $s$ con $s^2<2$ fuera una cota superior de $S_2$.

La construcción debe justificarse mediante desigualdades racionales; no introduzcas $\sqrt2$ ni ningún modelo de $\mathbb R$.

[]{#MA-EX-ANM-01-000-009}

[]{#MA-SOL-ANM-01-000-009}

### 9. Mejorar una cota que queda demasiado a la derecha

Sea $s\in\mathbb Q$ con $s>0$ y $s^2>2$. Define

$$
\delta=\frac{s^2-2}{4s},
\qquad
t=s-\delta.
$$

Demuestra, en este orden, que:

1. $\delta>0$ y $0<t<s$;
2. $t^2>2$;
3. todo $q\in S_2$ satisface $q<t$;
4. por tanto $t$ es una cota superior racional de $S_2$ estrictamente menor que $s$.

Concluye qué propiedad del supremo viola cualquier candidato racional $s$ con $s^2>2$.

[]{#MA-EX-ANM-01-000-010}

[]{#MA-SOL-ANM-01-000-010}

### 10. Ningún candidato racional sobrevive

Demuestra que $S_2$ no posee supremo en $\mathbb Q$.

Tu demostración debe organizarse como una prueba por contradicción:

1. supón que existe $s=\sup_{\mathbb Q}S_2$;
2. deduce de manera explícita que $1\le s\le2$;
3. separa los tres casos

$$
s^2<2,
\qquad
s^2=2,
\qquad
s^2>2;
$$

4. usa las construcciones de los ejercicios 8 y 9 para descartar los casos estrictos;
5. descarta $s^2=2$ mediante un argumento enteramente racional basado en una fracción $m/n$ escrita en términos mínimos;
6. concluye con precisión qué propiedad de $\mathbb Q$ falla.

No está permitido invocar la existencia previa de un número real cuyo cuadrado sea $2$.

[]{#MA-EX-ANM-01-000-011}

[]{#MA-SOL-ANM-01-000-011}

### 11. Una prueba que introduce demasiado pronto la frontera

Un estudiante escribe:

> «En $\mathbb R$ existe $\sqrt2$. Todo $q\in S_2$ cumple $q<\sqrt2$, y como los racionales son densos podemos aproximarnos racionalmente a $\sqrt2$ tanto como queramos desde abajo. Por tanto $\sqrt2$ es el supremo de $S_2$. Como $\sqrt2\notin\mathbb Q$, el conjunto $S_2$ no tiene supremo racional.»

Audita el argumento dentro del punto del capítulo en que nos encontramos.

1. Identifica la primera afirmación que no está disponible todavía.
2. Explica por qué la apelación a «aproximarse racionalmente a $\sqrt2$» también presupone un marco que aún no hemos construido.
3. Distingue qué conclusión matemática sería válida si ya dispusiéramos de $\mathbb R$ de la cuestión fundacional que §0.3 está intentando resolver sin circularidad.
4. Repara la estrategia indicando cómo reemplazar la referencia a $\sqrt2$ por un análisis puramente racional de un supuesto $s=\sup_{\mathbb Q}S_2$.

No basta con decir «es circular»: localiza exactamente qué objeto y qué propiedad se han usado antes de estar disponibles.

[]{#MA-EX-ANM-01-000-012}

[]{#MA-SOL-ANM-01-000-012}

### 12. Denso, pero no completo

Refuta la afirmación:

> «Todo cuerpo ordenado denso es completo para la propiedad del supremo.»

Tu contraejemplo debe ser $\mathbb Q$ y debe incluir tres piezas.

1. Demuestra directamente que $\mathbb Q$ es denso: dados $p<q$ racionales, construye un racional estrictamente entre ambos.
2. Usa $S_2$ y el resultado del ejercicio 10 para demostrar que $\mathbb Q$ no satisface la propiedad del supremo.
3. Considera además

$$
A=\{q\in\mathbb Q:q<1\}.
$$

Demuestra que $A$ no tiene máximo, pero sí tiene supremo racional, y explica por qué este contraste impide confundir «no tener máximo» con «no tener supremo».

Cierra distinguiendo en una frase qué controla la densidad y qué controla la completitud.

## §0.4. Construir una frontera sin tener el punto

[]{#MA-EX-ANM-01-000-013}

[]{#MA-SEC-ANM-01-000-004}

[]{#MA-SOL-ANM-01-000-013}

### 13. Auditar las cuatro condiciones de una cortadura

Para un subconjunto $A\subseteq\mathbb Q$, considera por separado estas cuatro exigencias:

1. $A\ne\varnothing$;
2. $A\subsetneq\mathbb Q$;
3. si $q\in A$ y $r<q$, entonces $r\in A$;
4. $A$ no tiene máximo.

Analiza los siguientes subconjuntos de $\mathbb Q$:

$$
\begin{aligned}
B_1&=\{q\in\mathbb Q:q<3\},\\
B_2&=\{q\in\mathbb Q:q\le3\},\\
B_3&=\mathbb Q,\\
B_4&=\varnothing,\\
B_5&=\{q\in\mathbb Q:q<0\ \text{o}\ 1<q<2\}.
\end{aligned}
$$

Para cada $A_i$:

1. determina cuáles de las cuatro condiciones satisface;
2. cuando una condición falle, exhibe un testigo concreto del fallo;
3. decide cuáles son cortaduras de Dedekind.

Cierra escribiendo correctamente los tipos de los objetos involucrados cuando $A\in\mathcal D$ y $q\in A$: distingue entre $A\in\mathcal D$, $A\subseteq\mathbb Q$, $q\in A$ y $q\in\mathbb Q$.

[]{#MA-EX-ANM-01-000-014}

[]{#MA-SOL-ANM-01-000-014}

### 14. Construir la cortadura determinada por un racional

Sea $c\in\mathbb Q$. Define

$$
c^*=\{q\in\mathbb Q:q<c\}.
$$

Demuestra directamente que $c^*$ es una cortadura de Dedekind.

Tu prueba debe verificar por separado:

1. no vaciedad;
2. que $c^*\subsetneq\mathbb Q$;
3. clausura hacia abajo;
4. ausencia de máximo.

Para la última condición, construye a partir de un $q\in c^*$ un racional $r$ tal que

$$
q<r<c.
$$

Explica finalmente por qué

$$
\{q\in\mathbb Q:q\le c\}
$$

no puede usarse como segundo código admisible para la misma frontera racional.

No demuestres todavía que $c\mapsto c^*$ preserva el orden; eso corresponde a la sección siguiente.

[]{#MA-EX-ANM-01-000-015}

[]{#MA-SOL-ANM-01-000-015}

### 15. Reparar $S_2$ hasta obtener una cortadura

Recuerda el conjunto de §0.3

$$
S_2=\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

1. Demuestra que $S_2$ **no** es una cortadura de Dedekind localizando una condición concreta que falla.
2. Define

$$
A_2=\{q\in\mathbb Q:q<0\ \text{o}\ q^2<2\}.
$$

Demuestra que $A_2$ sí es una cortadura.
3. En la prueba de ausencia de máximo, trata separadamente:
   - $q<0$;
   - $q\ge0$.

En el segundo caso puedes usar

$$
\delta=\frac{2-q^2}{2q+3}.
$$

Debes justificar que $q+\delta\in A_2$ y $q+\delta>q$.

4. Explica por qué esta construcción sigue usando únicamente objetos racionales y no introduce de manera encubierta una frontera real preexistente.

[]{#MA-EX-ANM-01-000-016}

[]{#MA-SOL-ANM-01-000-016}

### 16. La inclusión ordena linealmente todas las cortaduras

Sean $A,B\in\mathcal D$. Demuestra que

$$
A\subseteq B
\qquad\text{o}\qquad
B\subseteq A.
$$

Organiza la prueba a partir del caso no trivial $A\not\subseteq B$:

1. elige $a\in A\setminus B$;
2. toma un $b\in B$ arbitrario;
3. demuestra que no pueden ocurrir $a<b$ ni $a=b$;
4. usa la tricotomía de $\mathbb Q$ para concluir $b<a$;
5. usa la clausura hacia abajo de $A$ para obtener $b\in A$.

Concluye que la relación

$$
A\le_{\mathcal D}B
\iff
A\subseteq B
$$

es un orden lineal sobre $\mathcal D$, indicando además por qué reflexividad, antisimetría y transitividad provienen de la inclusión de conjuntos.

[]{#MA-EX-ANM-01-000-017}

[]{#MA-SOL-ANM-01-000-017}

### 17. Situar $A_2$ entre dos cortaduras racionales

Usa la notación

$$
c^*=\{q\in\mathbb Q:q<c\}
$$

y la cortadura

$$
A_2=\{q\in\mathbb Q:q<0\ \text{o}\ q^2<2\}.
$$

1. Demuestra las inclusiones estrictas

$$
1^*\subsetneq A_2\subsetneq 2^*.
$$

Debes exhibir un racional que pruebe la estricta inclusión en cada caso.
2. Supón, para obtener una contradicción, que existe $c\in\mathbb Q$ tal que

$$
A_2=c^*.
$$

Demuestra primero que $c>0$. Después separa los tres casos

$$
c^2<2,\qquad c^2=2,\qquad c^2>2,
$$

y usa sólo resultados disponibles hasta §0.4 para descartar cada uno.
3. Concluye que $A_2$ es una cortadura situada estrictamente entre dos cortaduras racionales, pero no coincide con $c^*$ para ningún racional $c$.

No interpretes todavía esta conclusión como una identificación con un número real previamente existente.

## §0.5. Una copia de $\mathbb Q$ dentro del nuevo sistema

[]{#MA-EX-ANM-01-000-018}

[]{#MA-SEC-ANM-01-000-005}

[]{#MA-SOL-ANM-01-000-018}

### 18. Construir la aplicación racional hacia $\mathcal D$

Para cada $q\in\mathbb Q$, recuerda la cortadura racional

$$
q^*=\{r\in\mathbb Q:r<q\}.
$$

Usa el resultado de §0.4 según el cual $q^*\in\mathcal D$ para construir formalmente

$$
\iota_{\mathbb Q}:\mathbb Q\longrightarrow\mathcal D,
\qquad
\iota_{\mathbb Q}(q)=q^*.
$$

1. Explica por qué la fórmula define realmente una aplicación con codominio $\mathcal D$.
2. Escribe explícitamente como subconjuntos de $\mathbb Q$ las imágenes de $-\frac32$, $0$ y $\frac74$.
3. Para un $q\in\mathbb Q$, distingue con tipos correctos los cuatro objetos o relaciones
   $q$, $q^*$, $q\in\mathbb Q$ y $q^*\in\mathcal D$.
4. Define la imagen

$$
\mathcal Q^*=\iota_{\mathbb Q}(\mathbb Q)
$$

y expresa correctamente su relación conjuntista con $\mathcal D$.

En este ejercicio no afirmes todavía que $\mathbb Q$ sea literalmente un subconjunto de $\mathcal D$: construye primero la aplicación y su imagen.

[]{#MA-EX-ANM-01-000-019}

[]{#MA-SOL-ANM-01-000-019}

### 19. Recuperar exactamente el orden racional

Sean $p,q\in\mathbb Q$. Demuestra la equivalencia

$$
p<q
\quad\Longleftrightarrow\quad
p^*\subsetneq q^*.
$$

Tu prueba debe incluir ambos sentidos.

1. Si $p<q$, demuestra primero $p^*\subseteq q^*$ y exhibe un testigo concreto de que la inclusión es estricta.
2. Si $p^*\subsetneq q^*$, elige un racional $r\in q^*\setminus p^*$ y usa únicamente el orden de $\mathbb Q$ para concluir $p<q$.
3. Deduce como corolario que

$$
p\le q
\quad\Longleftrightarrow\quad
p^*\subseteq q^*.
$$

4. Usa la equivalencia estricta para demostrar que $\iota_{\mathbb Q}$ es inyectiva.

La conclusión debe dejar claro que la aplicación no sólo preserva el orden: también permite recuperarlo desde las imágenes.

[]{#MA-EX-ANM-01-000-020}

[]{#MA-SOL-ANM-01-000-020}

### 20. Una certificación algebraica demasiado temprana

Un informe afirma:

> «Como $q\mapsto q^*$ es inyectiva y preserva el orden, ya hemos demostrado que $\mathbb Q$ está incrustado en $\mathcal D$ como cuerpo ordenado. Por tanto, para todos $p,q\in\mathbb Q$ podemos usar desde ahora
> $p^*+q^*=(p+q)^*$ y $p^*q^*=(pq)^*$. En consecuencia, escribiremos sin más $\mathbb Q\subseteq\mathcal D$.»

Audita el informe en el punto exacto del capítulo en que estamos.

1. Separa las afirmaciones que ya están demostradas de las que todavía no están disponibles.
2. Explica por qué la inyectividad y la preservación/reflexión del orden sólo certifican una **incrustación de órdenes lineales**.
3. Identifica qué operaciones sobre $\mathcal D$ tendrían que estar definidas antes de que las dos identidades algebraicas del informe tengan siquiera sentido dentro de la construcción.
4. Explica qué verificaciones adicionales serían necesarias para elevar el certificado a una incrustación de cuerpos ordenados.
5. Formula la certificación en dos tiempos que debe respetar el capítulo.

No refutes las identidades futuras: diagnostica por qué todavía no pueden usarse como resultados.

[]{#MA-EX-ANM-01-000-021}

[]{#MA-SOL-ANM-01-000-021}

### 21. La copia racional como orden, no todavía como cuerpo

Sea

$$
\mathcal Q^*=\{q^*:q\in\mathbb Q\}\subseteq\mathcal D.
$$

Define una aplicación

$$
\rho:\mathcal Q^*\longrightarrow\mathbb Q,
\qquad
\rho(q^*)=q.
$$

Demuestra que $\rho$ es el inverso de $\iota_{\mathbb Q}$ cuando restringimos el codominio de esta última a $\mathcal Q^*$.

Tu prueba debe mostrar:

1. que $\rho$ está bien definida;
2. que

$$
\rho\circ\iota_{\mathbb Q}
=
\operatorname{id}_{\mathbb Q};
$$

3. que

$$
\iota_{\mathbb Q}\circ\rho
=
\operatorname{id}_{\mathcal Q^*};
$$

4. que para $p,q\in\mathbb Q$,

$$
p<q
\quad\Longleftrightarrow\quad
p^*<_{\mathcal D}q^*;
$$

5. que, si $p^*<_{\mathcal D}q^*$, existe una cortadura racional $r^*\in\mathcal Q^*$ tal que

$$
p^*<_{\mathcal D}r^*<_{\mathcal D}q^*.
$$

Concluye exactamente en qué sentido $\mathcal Q^*$ es una copia de $\mathbb Q$ dentro de $\mathcal D$ y qué estructura sigue todavía sin certificar.

## §0.6. Dar aritmética a las cortaduras I: suma y opuesto

[]{#MA-EX-ANM-01-000-022}

[]{#MA-SEC-ANM-01-000-006}

[]{#MA-SOL-ANM-01-000-022}

### 22. Construir una suma que permanezca dentro de $\mathcal D$

Sean $A,B\in\mathcal D$. Define

$$
A+B=\{a+b:a\in A,\ b\in B\}.
$$

Demuestra que esta fórmula determina una operación interna

$$
+:\mathcal D\times\mathcal D\longrightarrow\mathcal D.
$$

Tu demostración debe verificar por separado las cuatro condiciones de cortadura para $A+B$.

1. Prueba que $A+B\ne\varnothing$.
2. Para demostrar que $A+B\ne\mathbb Q$, elige $u\notin A$ y $v\notin B$ y demuestra primero el hecho auxiliar
   $a<u$ para todo $a\in A$ y $b<v$ para todo $b\in B$.
3. Demuestra la clausura hacia abajo de $A+B$ sin apelar a ninguna noción geométrica de frontera.
4. Demuestra que $A+B$ no tiene máximo.

Cierra explicando por qué escribir una fórmula para $A+B$ no habría bastado, por sí solo, para definir una operación en $\mathcal D$.

[]{#MA-EX-ANM-01-000-023}

[]{#MA-SOL-ANM-01-000-023}

### 23. Recuperar la suma racional y localizar el cero

Sean $p,q\in\mathbb Q$.

1. Demuestra, por doble inclusión, que

$$
p^*+q^*=(p+q)^*.
$$

En la inclusión difícil, si $x<p+q$, construye explícitamente $a<p$ y $b<q$ tales que $x=a+b$.
2. Deduce que

$$
\iota_{\mathbb Q}(p+q)
=
\iota_{\mathbb Q}(p)+\iota_{\mathbb Q}(q).
$$

3. Demuestra directamente que

$$
A+0^*=A
$$

para toda $A\in\mathcal D$.
4. Usando la definición de la suma y la aritmética racional, demuestra que la suma de cortaduras es conmutativa y asociativa.

Concluye qué parte de la estructura aditiva racional está ya certificada y qué parte de la estructura de cuerpo sigue pendiente.

[]{#MA-EX-ANM-01-000-024}

[]{#MA-SOL-ANM-01-000-024}

### 24. Construir el opuesto sin introducir un punto final

Sea $A\in\mathcal D$.

Considera primero el conjunto ingenuo

$$
N(A)=\{-s:s\notin A\}.
$$

1. Examina el caso $A=q^*$ y demuestra que $N(q^*)$ no es una cortadura.
2. Define entonces

$$
-A
=
\{x\in\mathbb Q:
\exists s\notin A\text{ tal que }x<-s\}.
$$

Demuestra que $-A\in\mathcal D$ verificando las cuatro condiciones de cortadura.
3. Demuestra que, para todo $q\in\mathbb Q$,

$$
-(q^*)=(-q)^*.
$$

Explica por qué la desigualdad estricta en la definición de $-A$ es estructuralmente necesaria y no un detalle notacional.

[]{#MA-EX-ANM-01-000-025}

[]{#MA-SOL-ANM-01-000-025}

### 25. Trazar la prueba de que el opuesto es un inverso aditivo

Sea $A\in\mathcal D$.

Primero demuestra el lema siguiente:

> Si $h\in\mathbb Q$ y $h>0$, existe $a\in A$ tal que $a+h\notin A$.

Tu prueba debe señalar exactamente dónde se usa la propiedad arquimediana de $\mathbb Q$.

Después usa ese lema para demostrar

$$
A+(-A)=0^*.
$$

Organiza la prueba por doble inclusión y, en la inclusión

$$
0^*\subseteq A+(-A),
$$

explica por qué para $x<0$ conviene introducir

$$
h=-\frac{x}{2}.
$$

Finalmente demuestra la equivalencia de traslación

$$
A\subseteq B
\quad\Longleftrightarrow\quad
A+C\subseteq B+C
$$

para $A,B,C\in\mathcal D$, y deduce la versión estricta.

Cierra con una lista breve de dependencias: qué parte usa clausura hacia abajo, qué parte usa existencia de racionales exteriores, qué parte usa arquimedianidad y qué parte usa ya la existencia del opuesto.

[]{#MA-EX-ANM-01-000-026}

[]{#MA-SOL-ANM-01-000-026}

### 26. Auditar un cierre aditivo demasiado rápido

Un informe afirma:

> «Definimos $A+B=\{a+b:a\in A,\ b\in B\}$ y $-A=\{-a:a\in A\}$. Como ambas fórmulas usan sólo racionales, sus resultados pertenecen automáticamente a $\mathcal D$. Además, como $A+(-A)$ representa intuitivamente cero, ya tenemos un grupo ordenado. Por tanto podemos cancelar $C$ en $A+C\subseteq B+C$ y concluir $A\subseteq B$.»

Audita el informe.

1. Localiza la primera inferencia inválida.
2. Explica por qué una fórmula con valores racionales no garantiza que el resultado sea una cortadura.
3. Demuestra con un ejemplo racional que $\{-a:a\in A\}$ no puede ser la definición correcta del opuesto.
4. Explica qué verificaciones deben preceder a la afirmación $A+(-A)=0^*$.
5. Explica por qué la cancelación usada al final sólo queda justificada después de construir y verificar el inverso aditivo.
6. Reordena el argumento en una cadena lógica correcta que termine exactamente en

$$
(\mathcal D,+,\le_{\mathcal D})
\text{ es un grupo abeliano linealmente ordenado}.
$$

No uses producto, unidad multiplicativa ni inversos multiplicativos.

## §0.7. Dar aritmética a las cortaduras II: producto e inverso

[]{#MA-EX-ANM-01-000-027}

[]{#MA-SEC-ANM-01-000-007}

[]{#MA-SOL-ANM-01-000-027}

### 27. Construir el núcleo positivo del producto

La receta aditiva sugiere primero el conjunto ingenuo

$$
P(A,B)=\{ab:a\in A,\ b\in B\}.
$$

1. Toma $A=B=1^*$ y demuestra que $P(1^*,1^*)$ contiene racionales positivos arbitrariamente grandes. Explica por qué eso impide que esta receta sea, en general, un producto de cortaduras.
2. Para $A\in\mathcal D$, demuestra las equivalencias

$$
0^*\subsetneq A
\quad\Longleftrightarrow\quad
0\in A
\quad\Longleftrightarrow\quad
\exists a\in A\text{ con }a>0.
$$

3. Si $A,B>0^*$, define

$$
A_{>0}=\{a\in A:a>0\},
$$

y construye el candidato

$$
A\cdot_+B
=
\{x\in\mathbb Q:\exists a\in A_{>0}\ \exists b\in B_{>0}\text{ con }x<ab\}.
$$

4. Demuestra ya, a partir de la definición, que $A\cdot_+B$ es no vacío, contiene $0$ y es cerrado hacia abajo.

No declares todavía que $A\cdot_+B\in\mathcal D$: las dos condiciones restantes deben demostrarse en el ejercicio siguiente.

[]{#MA-EX-ANM-01-000-028}

[]{#MA-SOL-ANM-01-000-028}

### 28. Cerrar el producto positivo y recuperar el producto racional

Sean $A,B>0^*$ y usa la operación $A\cdot_+B$ construida en el ejercicio 27.

1. Demuestra que $A\cdot_+B$ es propio. Tu prueba debe elegir racionales exteriores $u\notin A$ y $v\notin B$ y justificar por qué necesariamente $u,v>0$.
2. Demuestra que $A\cdot_+B$ no tiene máximo.
3. Concluye que

$$
A\cdot_+B\in\mathcal D
\qquad\text{y}\qquad
A\cdot_+B>0^*.
$$

4. Sean ahora $p,q\in\mathbb Q$ con $p,q>0$. Demuestra por doble inclusión que

$$
p^*\cdot_+q^*=(pq)^*.
$$

En la inclusión difícil, separa los casos $x\le0$ y $0<x<pq$, y localiza exactamente dónde interviene la densidad de $\mathbb Q$.

[]{#MA-EX-ANM-01-000-029}

[]{#MA-SOL-ANM-01-000-029}

### 29. Trazar el paso del producto positivo a todos los signos

Usa la estructura aditiva de §0.6 y el producto positivo de los ejercicios 27–28.

1. Explica por qué

$$
-(-A)=A
$$

y por qué $A<0^*$ implica $-A>0^*$.
2. Define un producto $A\cdot B$ para $A,B\in\mathcal D$ mediante los cinco casos: cero, dos positivos, dos negativos y los dos órdenes posibles de signos opuestos. Debes escribir explícitamente la definición por casos y verificar que cada aparición de $\cdot_+$ recibe argumentos estrictamente positivos.
3. Demuestra que, para todos $p,q\in\mathbb Q$,

$$
p^*\cdot q^*=(pq)^*.
$$

No omitas los casos de signos negativos ni los casos con cero.
4. Demuestra primero para $A>0^*$ que

$$
A\cdot_+1^*=A,
$$

y extiende después el resultado a todo $A\in\mathcal D$ para obtener

$$
A\cdot1^*=A=1^*\cdot A.
$$

Cierra con un mapa de dependencias que indique qué parte usa el opuesto de §0.6, qué parte usa la identidad racional positiva del ejercicio 28 y qué parte usa ausencia de máximo.

[]{#MA-EX-ANM-01-000-030}

[]{#MA-SOL-ANM-01-000-030}

### 30. Construir y verificar el inverso multiplicativo

Sea $A>0^*$. Define

$$
A^{-1,+}
=
\left\{
q\in\mathbb Q:
q\le0
\text{ o }
\exists s>0\;\bigl(s\notin A\text{ y }q<s^{-1}\bigr)
\right\}.
$$

1. Demuestra que $A^{-1,+}$ es una cortadura estrictamente positiva.
2. Demuestra por doble inclusión que

$$
A\cdot_+A^{-1,+}=1^*.
$$

3. Para la inclusión $1^*\subseteq A\cdot_+A^{-1,+}$, trata por separado $x\le0$ y $0<x<1$. En el segundo caso debes usar el lema de aproximación racional de §0.6 para obtener un par

$$
a\in A,
\qquad
s=a+h\notin A
$$

suficientemente próximo.
4. Si $A\ne0^*$, define $A^{-1}$ para ambos signos y demuestra

$$
A\cdot A^{-1}=1^*=A^{-1}\cdot A.
$$

> **Pista conceptual.** Para $0<x<1$, busca primero un $c\in A$ positivo y elige $h$ tan pequeño que $h<(1-x)c$. El objetivo es forzar $x/a<1/s$ para poder insertar un racional entre ambos.

[]{#MA-EX-ANM-01-000-031}

[]{#MA-SOL-ANM-01-000-031}

### 31. Un producto correcto para positivos que no forma un cuerpo

Para mostrar que el sector positivo no determina por sí solo toda la estructura de cuerpo, define una operación $\star$ sobre $\mathcal D$ así:

$$
A\star B=
\begin{cases}
0^*,&A=0^*\text{ o }B=0^*,\\
A\cdot_+B,&A>0^*,\ B>0^*,\\
-\bigl((-A)\cdot_+(-B)\bigr),&A<0^*,\ B<0^*,\\
-\bigl(A\cdot_+(-B)\bigr),&A>0^*>B,\\
-\bigl((-A)\cdot_+B\bigr),&B>0^*>A.
\end{cases}
$$

La única rama deliberadamente alterada respecto del producto correcto es la de dos factores negativos.

1. Explica por qué $\star$ sigue siendo una operación interna en $\mathcal D$ y coincide con $\cdot_+$ cuando ambos factores son positivos.
2. Calcula

$$
(-1)^*\star(-1)^*.
$$

3. Usa los tres elementos $(-1)^*,(-1)^*,1^*$ para demostrar directamente que $\star$ no es distributiva respecto de la suma ya construida.
4. Explica por qué este ejemplo refuta la inferencia «si el producto funciona para positivos, el resto de las leyes de cuerpo queda automáticamente determinado».

> **Pista conceptual.** Compara $(-1)^*\star\bigl((-1)^*+1^*\bigr)$ con $\bigl((-1)^*\star(-1)^*\bigr)+\bigl((-1)^*\star1^*\bigr)$.

[]{#MA-EX-ANM-01-000-032}

[]{#MA-SOL-ANM-01-000-032}

### 32. Cerrar el cuerpo ordenado sin confundirlo con completitud

Trabaja con el producto correcto $\cdot$ y los inversos construidos en los ejercicios anteriores. Organiza el cierre multiplicativo mediante una estrategia de **núcleo positivo + regla de signos**.

1. Demuestra la conmutatividad y la asociatividad de $\cdot_+$ para cortaduras positivas. En la asociatividad, construye explícitamente el testigo intermedio que permite pasar de una agrupación a la otra.
2. Extiende conmutatividad y asociatividad a todos los signos explicando por qué ambos lados tienen el mismo signo y el mismo núcleo positivo.
3. Demuestra la distributividad positiva

$$
A\cdot_+(B+C)
=
(A\cdot_+B)+(A\cdot_+C)
$$

para $A,B,C>0^*$.
4. Extiende la distributividad a signos arbitrarios. En el caso $B>0^*>C$, explica por qué hay que comparar $B$ con $-C$ y cómo la cancelación en el grupo aditivo reduce el problema al caso positivo.
5. Demuestra la compatibilidad multiplicativa del orden:

$$
0^*\le A,\ 0^*\le B
\quad\Longrightarrow\quad
0^*\le A\cdot B.
$$

6. Reúne todo lo demostrado en §§0.6–0.7 y justifica que

$$
(\mathcal D,+,\cdot,\le_{\mathcal D})
$$

es un cuerpo ordenado.
7. Demuestra que

$$
\iota_{\mathbb Q}:\mathbb Q\hookrightarrow\mathcal D,
\qquad q\mapsto q^*,
$$

queda ahora certificada como incrustación de cuerpos ordenados.
8. Explica con precisión por qué **todavía no** puede concluirse que la pregunta de existencia de §0.1 está cerrada.

> **Pista conceptual.** Para evitar una explosión de casos, separa cada cortadura no nula en un signo y una parte positiva. Para la distributividad con signos opuestos, compara primero $B$ y $-C$ dentro del orden lineal de $\mathcal D$.

## §0.8. Sí existen: el supremo como unión

[]{#MA-EX-ANM-01-000-033}

[]{#MA-SEC-ANM-01-000-008}

[]{#MA-SOL-ANM-01-000-033}

### 33. Demostrar que la unión vuelve a ser una cortadura

Sea $\mathscr A\subseteq\mathcal D$ una familia no vacía y acotada superiormente. Define

$$
S=\bigcup_{A\in\mathscr A}A.
$$

Demuestra que $S\in\mathcal D$ verificando por separado las cuatro condiciones de una cortadura.

1. Para la no vaciedad, usa únicamente que $\mathscr A\ne\varnothing$ y que cada miembro de $\mathscr A$ es no vacío.
2. Para demostrar que $S\ne\mathbb Q$, toma una cota superior $U\in\mathcal D$ de $\mathscr A$ y prueba primero

$$
S\subseteq U.
$$

3. Demuestra la clausura hacia abajo de $S$ siguiendo un elemento $q\in S$ hasta alguna cortadura $A\in\mathscr A$ que lo contenga.
4. Demuestra que $S$ no tiene máximo usando la ausencia de máximo del mismo miembro $A$.
5. Cierra indicando con precisión en cuál de las cuatro verificaciones se usa la hipótesis de acotación superior y en cuál se usa que la familia sea no vacía.

No llames todavía a $S$ «supremo»: en este ejercicio sólo debes probar que el candidato pertenece al dominio $\mathcal D$.

[]{#MA-EX-ANM-01-000-034}

[]{#MA-SOL-ANM-01-000-034}

### 34. Separar «ser cortadura» de «ser supremo»

Mantén las hipótesis del ejercicio 33 y supón ya demostrado que

$$
S=\bigcup_{A\in\mathscr A}A\in\mathcal D.
$$

Traza ahora, como una segunda prueba independiente, que

$$
S=\sup_{\mathcal D}\mathscr A.
$$

Tu argumento debe distinguir explícitamente las dos obligaciones de un supremo.

1. Demuestra que $S$ es cota superior de $\mathscr A$.
2. Sea $V\in\mathcal D$ una cota superior arbitraria de $\mathscr A$. Demuestra que $S\subseteq V$.
3. Traduce ambas inclusiones al orden $\le_{\mathcal D}$.
4. Explica por qué la prueba de que $S$ es la menor cota superior no reemplaza la prueba previa de que $S\in\mathcal D$.
5. Haz un inventario de hipótesis: señala cuáles se gastaron para garantizar que $S$ fuera un elemento de $\mathcal D$ y cuáles se usan directamente en la caracterización de menor cota superior.

El cierre debe ser la identidad

$$
\boxed{
\sup_{\mathcal D}\mathscr A
=
\bigcup_{A\in\mathscr A}A.
}
$$

[]{#MA-EX-ANM-01-000-035}

[]{#MA-SOL-ANM-01-000-035}

### 35. Localizar exactamente por qué hace falta una cota superior

Para cada $n\in\mathbb N$, considera la cortadura racional

$$
n^*=\{q\in\mathbb Q:q<n\},
$$

y la familia

$$
\mathscr N=\{n^*:n\in\mathbb N\}\subseteq\mathcal D.
$$

1. Demuestra que $\mathscr N$ es no vacía.
2. Usa la propiedad arquimediana de $\mathbb Q$ para demostrar

$$
\bigcup_{n\in\mathbb N}n^*=\mathbb Q.
$$

3. Concluye que esa unión no es una cortadura.
4. Demuestra que $\mathscr N$ no puede estar acotada superiormente en $\mathcal D$.
5. Vuelve a la demostración del ejercicio 33 y localiza el paso exacto que se rompe para $\mathscr N$.

Concluye por qué la afirmación

> «la unión de cualquier familia no vacía de cortaduras es otra cortadura»

es falsa, aunque la unión siga siendo no vacía, cerrada hacia abajo y sin máximo en este ejemplo.

[]{#MA-EX-ANM-01-000-036}

[]{#MA-SOL-ANM-01-000-036}

### 36. Cerrar la pregunta de existencia sin confundir modelo con esencia

Reúne los dos certificados obtenidos hasta ahora:

$$
\text{ORDERED FIELD = VERIFIED}
$$

en §§0.6–0.7, y la propiedad del supremo demostrada en los ejercicios 33–34.

1. Demuestra que

$$
(\mathcal D,+,\cdot,\le_{\mathcal D})
$$

es un cuerpo ordenado completo.
2. Explica por qué esto constituye una prueba de existencia de al menos un sistema de números reales en el sentido fijado en §0.1.
3. Incorpora la incrustación

$$
\iota_{\mathbb Q}:\mathbb Q\hookrightarrow\mathcal D,
\qquad q\mapsto q^*,
$$

y precisa qué estructura conserva.
4. Explica en qué sentido está autorizado decir que $\mathcal D$ es **un modelo de los números reales** y por qué de ello no se sigue que «un número real sea por esencia una cortadura».
5. Retoma

$$
A_2=\{q\in\mathbb Q:q<0\text{ o }q^2<2\}.
$$

Explica qué afirmación nueva queda autorizada acerca de $A_2$ después del cierre de completitud y qué afirmación sobre unicidad de modelos sigue todavía sin demostrarse.

> **Pista conceptual.** La prueba de existencia no requiere identificar una ontología única: basta exhibir una estructura concreta que satisfaga toda la especificación.

[]{#MA-EX-ANM-01-000-037}

[]{#MA-SOL-ANM-01-000-037}

### 37. Auditar un cierre de existencia que mezcla cuatro niveles

Un informe propone:

> «En §0.7 demostramos que $\mathcal D$ es un cuerpo ordenado; por tanto ya es completo. Además, la unión de cualquier familia de cortaduras es una cortadura, así que toda familia tiene supremo. En consecuencia $\mathcal D$ es literalmente $\mathbb R$. Como ya encontramos un modelo, cualquier otro cuerpo ordenado completo debe ser igual a $\mathcal D$.»

Audita el informe sin usar resultados de §§0.9–0.10.

1. Localiza la primera inferencia inválida y refútala usando un resultado ya disponible del capítulo.
2. Refuta la segunda inferencia mediante la familia $\mathscr N=\{n^*:n\in\mathbb N\}$ del ejercicio 35.
3. Formula correctamente el teorema de unión, incluyendo todas sus hipótesis.
4. Explica la diferencia entre las afirmaciones

$$
\mathcal D\text{ es un modelo de los números reales}
$$

y

$$
\mathcal D\text{ es literalmente el único conjunto posible de números reales}.
$$

5. Repara el informe hasta obtener exactamente la conclusión disponible al terminar §0.8: existencia de un cuerpo ordenado completo con una copia ordenada de $\mathbb Q$, sin afirmar todavía unicidad estructural.

> **Pista conceptual.** Distingue cuatro puertas: cuerpo ordenado, propiedad del supremo, existencia de un modelo y unicidad del modelo. Ninguna debe sustituirse por la siguiente sin prueba.

## §0.9. ¿Podría haber otros reales?

[]{#MA-EX-ANM-01-000-038}

[]{#MA-SEC-ANM-01-000-009}

[]{#MA-SOL-ANM-01-000-038}

### 38. Separar universos y construir la copia racional canónica

Sea

$$
F=(F,+,\cdot,0_F,1_F,\le_F)
$$

un cuerpo ordenado arbitrario. No supongas todavía que sea completo.

1. Define los numerales de $F$ mediante

$$
\nu_F(0)=0_F,\qquad \nu_F(n+1)=\nu_F(n)+1_F,
$$

y demuestra que $m<n$ implica $\nu_F(m)<\nu_F(n)$. Deduce que $F$ tiene característica cero.
2. Escribe correctamente los tipos de las aplicaciones

$$
\nu_F,\qquad \jmath_{\mathbb Z}^F,\qquad \iota_F,
$$

donde la segunda debe representar enteros y la tercera racionales dentro de $F$.
3. Para $m,n\in\mathbb N$, define

$$
\jmath_{\mathbb Z}^F(m-n)=\nu_F(m)-\nu_F(n)
$$

y explica qué debe verificarse para que la definición no dependa de la representación del entero.
4. Para $a,b\in\mathbb Z$ con $b\ne0$, define

$$
\iota_F\!\left(\frac ab\right)
=
\jmath_{\mathbb Z}^F(a)
\bigl(\jmath_{\mathbb Z}^F(b)\bigr)^{-1}.
$$

Justifica por qué el inverso existe y qué igualdad debe usarse para comprobar que el valor no depende del representante $a/b$.
5. Explica por qué, aun después de estas verificaciones, la escritura $\mathbb Q\subseteq F$ es una identificación notacional con la imagen de $\iota_F$ y no una igualdad literal impuesta entre conjuntos.

Cierra indicando qué parte de esta construcción requiere completitud de $F$.

[]{#MA-EX-ANM-01-000-039}

[]{#MA-SOL-ANM-01-000-039}

### 39. La completitud obliga a la arquimedianidad

Supón ahora que $F$ es un cuerpo ordenado completo y considera

$$
N_F=\{\nu_F(n):n\in\mathbb N\}.
$$

Demuestra que $F$ es arquimediano. Organiza la prueba por contradicción.

1. Supón que $N_F$ está acotado superiormente y usa completitud para definir

$$
s=\sup_F N_F.
$$

2. Explica por qué $s-1_F$ no puede ser una cota superior de $N_F$.
3. Deduce que existe $n\in\mathbb N$ con

$$
s-1_F<\nu_F(n),
$$

y obtiene una contradicción sumando $1_F$.
4. Concluye que para todo $x\in F$ existe $n\in\mathbb N$ tal que

$$
x<\nu_F(n).
$$

5. Señala el único paso de la demostración en el que se gasta la completitud y explica por qué el argumento no demuestra que **todo** cuerpo ordenado sea arquimediano.

[]{#MA-EX-ANM-01-000-040}

[]{#MA-SOL-ANM-01-000-040}

### 40. Trazar el camino desde la arquimedianidad hasta la densidad racional

Sea $F$ un cuerpo ordenado completo y usa su incrustación racional canónica

$$
\iota_F:\mathbb Q\hookrightarrow F.
$$

Reconstruye sin saltos la cadena

$$
\text{arquimedianidad}
\Longrightarrow
\text{localización entera}
\Longrightarrow
\text{localización racional}
\Longrightarrow
\text{densidad de }\iota_F(\mathbb Q).
$$

1. Para $x\in F$, demuestra que existe $m\in\mathbb Z$ tal que

$$
\iota_F(m-1)\le x<\iota_F(m).
$$

Debes construir un conjunto $K\subseteq\mathbb N$, tomar su mínimo y explicar por qué la minimalidad produce simultáneamente las dos desigualdades.
2. Sean $x<y$ en $F$. Usa la arquimedianidad aplicada a $(y-x)^{-1}$ para elegir $n\in\mathbb N$, $n>0$, de modo que

$$
0<\iota_F\!\left(\frac1n\right)<y-x.
$$

3. Aplica la localización entera a $x\,\iota_F(n)$ y construye un entero $m$ para el cual

$$
\iota_F\!\left(\frac{m-1}{n}\right)\le x<\iota_F\!\left(\frac mn\right).
$$

4. Demuestra que el mismo $q=m/n$ satisface

$$
\boxed{x<\iota_F(q)<y}.
$$

5. Cierra con un mapa de dependencias que indique dónde se usa: orden de $F$, arquimedianidad, buen orden de $\mathbb N$, estructura de cuerpo e incrustación racional. No invoques una intuición geométrica de «racionales muy juntos».

> **Pista conceptual.** La arquimedianidad da escala; el mínimo de $K$ convierte esa escala en una celda entera; dividir una celda suficientemente fina produce la posición racional intermedia.

[]{#MA-EX-ANM-01-000-041}

[]{#MA-SOL-ANM-01-000-041}

### 41. Convertir una posición abstracta en una cortadura racional

Para $x\in F$, define

$$
A_x=\{q\in\mathbb Q:\iota_F(q)<x\}.
$$

1. Escribe los tipos correctos de $x$, $q$, $\iota_F(q)$ y $A_x$. Explica por qué $A_x$ es un subconjunto de $\mathbb Q$ y no un subconjunto de $F$.
2. Demuestra que $A_x$ es una cortadura de Dedekind verificando las cuatro condiciones: no vaciedad, propiedad de ser subconjunto propio, clausura hacia abajo y ausencia de máximo.
3. En cada una de las cuatro verificaciones, identifica si interviene la densidad racional demostrada en el ejercicio 40 o sólo la preservación del orden por $\iota_F$.
4. Como variación, toma $c\in\mathbb Q$ y $x=\iota_F(c)$. Demuestra que

$$
\boxed{A_{\iota_F(c)}=c^*}.
$$

Explica qué muestra esta identidad acerca de la compatibilidad entre la traza racional de un modelo abstracto y las cortaduras racionales construidas antes.

> **Pista conceptual.** Para probar que $A_x$ es no vacío y propio, busca racionales entre $x-1_F$ y $x$, y entre $x$ y $x+1_F$.

[]{#MA-EX-ANM-01-000-042}

[]{#MA-SOL-ANM-01-000-042}

### 42. Reconstruir un elemento desde su traza y recuperar el orden

Sea $F$ un cuerpo ordenado completo y, para cada $x\in F$, usa la cortadura

$$
A_x=\{q\in\mathbb Q:\iota_F(q)<x\}.
$$

1. Demuestra que

$$
\iota_F(A_x)=\{\iota_F(q):q\in A_x\}
$$

es no vacío y está acotado superiormente por $x$.
2. Usa completitud para definir

$$
s=\sup_F\iota_F(A_x)
$$

y demuestra que

$$
\boxed{x=\sup_F\iota_F(A_x)}.
$$

En el paso decisivo, si supones $s<x$, debes producir mediante densidad racional un elemento de $\iota_F(A_x)$ estrictamente mayor que $s$.
3. Deduce que

$$
A_x=A_y\Longrightarrow x=y.
$$

4. Demuestra la equivalencia

$$
\boxed{x\le y\quad\Longleftrightarrow\quad A_x\subseteq A_y}
$$

y deduce también

$$
\boxed{x<y\quad\Longleftrightarrow\quad A_x\subsetneq A_y}.
$$

5. Explica por qué estos resultados convierten a $\mathbb Q$ en un lenguaje común para registrar posiciones dentro de cualquier cuerpo ordenado completo, pero **no** construyas todavía una aplicación entre dos modelos distintos.

> **Pista conceptual.** La traza determina a $x$ porque cualquier hueco entre su supremo y $x$ contendría una imagen racional que la propia traza habría tenido que registrar.

## §0.10. Únicos hasta isomorfismo

[]{#MA-EX-ANM-01-000-043}

[]{#MA-SEC-ANM-01-000-010}

[]{#MA-SOL-ANM-01-000-043}

### 43. Antes del transporte: demostrar que el supremo existe

Sean $F$ y $G$ cuerpos ordenados completos, con incrustaciones racionales canónicas

$$
\iota_F:\mathbb Q\hookrightarrow F,
\qquad
\iota_G:\mathbb Q\hookrightarrow G.
$$

Para $x\in F$, sea

$$
A_x^F=\{q\in\mathbb Q:\iota_F(q)<x\}.
$$

Queremos definir

$$
\phi(x)=\sup_G\iota_G(A_x^F).
$$

No uses esa fórmula hasta haber verificado que el supremo está autorizado.

1. Escribe los tipos correctos de $x$, $A_x^F$, $\iota_G(A_x^F)$ y del eventual valor $\phi(x)$.
2. Demuestra que $\iota_G(A_x^F)$ es no vacío.
3. Como $A_x^F$ es una cortadura, elige $u\in\mathbb Q\setminus A_x^F$ y demuestra que

$$
q<u
\qquad(q\in A_x^F).
$$

4. Deduce que $\iota_G(u)$ es una cota superior de $\iota_G(A_x^F)$.
5. Señala exactamente dónde se usa la completitud de $G$ y, sólo entonces, define

$$
\boxed{\phi:F\longrightarrow G,
\qquad
\phi(x)=\sup_G\{\iota_G(q):q\in A_x^F\}.}
$$

6. Explica por qué la definición no contiene una elección arbitraria de representante ni de cota superior.

[]{#MA-EX-ANM-01-000-044}

[]{#MA-SOL-ANM-01-000-044}

### 44. El transporte conserva exactamente la traza racional

Mantén la definición de $\phi$ del ejercicio 43. Para distinguir universos escribe

$$
A_x^F=\{q\in\mathbb Q:\iota_F(q)<x\},
$$

y, para $y\in G$,

$$
A_y^G=\{q\in\mathbb Q:\iota_G(q)<y\}.
$$

1. Demuestra la identidad central

$$
\boxed{A_{\phi(x)}^G=A_x^F}
$$

por doble inclusión. En la inclusión $A_x^F\subseteq A_{\phi(x)}^G$ debes usar que $A_x^F$ no tiene máximo.
2. Usa la caracterización del orden por inclusión de trazas obtenida en §0.9 para demostrar

$$
\boxed{x\le y\iff\phi(x)\le\phi(y)}
$$

y

$$
\boxed{x<y\iff\phi(x)<\phi(y)}.
$$

3. Deduce que $\phi$ es inyectiva.
4. Explica por qué el argumento demuestra más que monotonicidad: la posición racional de cada elemento queda transportada sin alteración.

> **Pista conceptual.** Para la inclusión inversa, si $q<\phi(x)$ pero $q\notin A_x^F$, muestra que $\iota_G(q)$ sería una cota superior de $\iota_G(A_x^F)$ menor que su supremo.

[]{#MA-EX-ANM-01-000-045}

[]{#MA-SOL-ANM-01-000-045}

### 45. Construir la inversa sin cardinalidad ni elección de preimágenes

Intercambia ahora los papeles de $F$ y $G$ y define, cuando esté justificado,

$$
\psi:G\longrightarrow F,
\qquad
\psi(y)=\sup_F\{\iota_F(q):q\in A_y^G\}.
$$

1. Traza la buena definición de $\psi$ y señala el gasto de completitud de $F$.
2. Demuestra

$$
A_{\psi(y)}^F=A_y^G.
$$

3. Para $x\in F$, calcula la traza de $\psi(\phi(x))$ y usa la reconstrucción desde trazas para demostrar

$$
\boxed{\psi(\phi(x))=x}.
$$

4. Demuestra simétricamente

$$
\boxed{\phi(\psi(y))=y}
$$

para todo $y\in G$.
5. Concluye que $\psi=\phi^{-1}$ y que $\phi$ es biyectiva.
6. Resume en un mapa de dependencias por qué la sobreyectividad obtenida aquí no usa cardinalidad de $F$ y $G$, ni una elección arbitraria de preimágenes.

> **Pista conceptual.** No busques un preimagen de $y$ por tanteo: reconstruye en $F$ el elemento que tenga exactamente la misma traza racional que $y$.

[]{#MA-EX-ANM-01-000-046}

[]{#MA-SOL-ANM-01-000-046}

### 46. Tres atajos que no producen un isomorfismo de cuerpos ordenados

Refuta cada uno de los siguientes atajos.

1. **«Biyectiva y ordenada basta».** En un cuerpo ordenado completo $F$, considera

$$
\tau:F\longrightarrow F,
\qquad
\tau(x)=x+1_F.
$$

Demuestra que $\tau$ es biyectiva y preserva y refleja el orden, pero no es un homomorfismo de cuerpos.
2. **«Misma cardinalidad da sobreyectividad».** Explica por qué, aun si dos conjuntos tienen la misma cardinalidad, una aplicación inyectiva concreta entre ellos no tiene por qué ser sobreyectiva. Exhibe un ejemplo elemental explícito.
3. **«Multiplicatividad para no negativos basta».** Explica por qué demostrar

$$
\phi(xy)=\phi(x)\phi(y)
\qquad(x,y\ge0)
$$

no cubre los casos con uno o dos factores negativos.
4. Para cada atajo, indica cuál es la obligación correcta que debe reemplazarlo dentro de la prueba de unicidad de §0.10.

> **Pista conceptual.** Un isomorfismo de cuerpos ordenados debe conservar simultáneamente estructura algebraica, orden y elementos distinguidos; ninguna de esas capas se recupera automáticamente de las otras.

[]{#MA-EX-ANM-01-000-047}

[]{#MA-SOL-ANM-01-000-047}

### 47. Recuperar toda la aritmética desde las trazas

Trabaja con el transporte canónico biyectivo $\phi:F\to G$ de los ejercicios 43–45.

1. Demuestra primero que, para todo $q\in\mathbb Q$,

$$
\boxed{\phi(\iota_F(q))=\iota_G(q)}.
$$

Deduce

$$
\phi(0_F)=0_G,
\qquad
\phi(1_F)=1_G.
$$

2. Demuestra la caracterización racional de la suma:

$$
\boxed{
q\in A_{x+y}^F
\iff
\exists r\in A_x^F\;\exists s\in A_y^F:
q<r+s.
}
$$

Usa densidad racional en los dos pasos necesarios de la implicación directa.
3. Como $\phi$ conserva trazas, deduce de esa caracterización

$$
\boxed{\phi(x+y)=\phi(x)+\phi(y)}
$$

y luego

$$
\phi(-x)=-\phi(x).
$$

4. Para $x,y\ge0$, demuestra la caracterización

$$
\boxed{
q\in A_{xy}^F
\iff
q<0
\ \text{o}\
\exists r,s>0:
\bigl(r\in A_x^F,
\ s\in A_y^F,
\ q<rs\bigr).
}
$$

5. Deduce

$$
\phi(xy)=\phi(x)\phi(y)
\qquad(x,y\ge0).
$$

6. Cierra **todos** los casos de signo y demuestra

$$
\boxed{\phi(xy)=\phi(x)\phi(y)}
$$

para $x,y\in F$ arbitrarios.
7. Deduce finalmente la preservación de inversos para $x\ne0_F$.

> **Pista conceptual.** No calcules directamente los supremos de $A_{x+y}$ o $A_{xy}$. Caracteriza primero esas trazas por racionales; después usa que igualdad de trazas implica igualdad de elementos.

[]{#MA-EX-ANM-01-000-048}

[]{#MA-SOL-ANM-01-000-048}

### 48. Cerrar la unicidad estructural de los números reales

Sean $F$ y $G$ cuerpos ordenados completos y sea

$$
\phi:F\longrightarrow G
$$

el transporte canónico construido en esta sección.

1. Reúne los resultados anteriores para demostrar que $\phi$ es un isomorfismo de cuerpos ordenados.
2. Sea ahora

$$
T:F\longrightarrow G
$$

un isomorfismo de cuerpos ordenados arbitrario. Demuestra que

$$
T\circ\iota_F=\iota_G.
$$

3. Para $x\in F$, prueba que

$$
A_{T(x)}^G=A_x^F.
$$

4. Compara esa identidad con $A_{\phi(x)}^G=A_x^F$ y demuestra que

$$
\boxed{T(x)=\phi(x)}
$$

para todo $x\in F$. Concluye

$$
\boxed{T=\phi}.
$$

5. Formula el teorema final: entre cualesquiera dos cuerpos ordenados completos existe un **único** isomorfismo de cuerpos ordenados. Deduce que todo automorfismo de cuerpo ordenado de un cuerpo ordenado completo es la identidad.
6. Distingue con precisión:
   - igualdad literal $F=G$;
   - existencia de algún isomorfismo $F\cong G$;
   - existencia de un único isomorfismo de cuerpos ordenados.
7. Explica por qué «canónico por unicidad» no significa automáticamente «computable».
8. Cierra el arco del capítulo explicando cómo

$$
\boxed{
\text{EXISTENCIA}
+
\text{UNICIDAD HASTA ÚNICO ISOMORFISMO}
}
$$

justifica estructuralmente hablar de **los números reales** sin imponer una codificación conjuntista particular.

> **Pista conceptual.** Todo isomorfismo ordenado debe fijar la copia racional canónica; una vez fijados los racionales, las trazas racionales fuerzan punto por punto la imagen de cada elemento.

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 0](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md) · [Ejercicios](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.md)
