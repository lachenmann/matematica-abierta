---
title: "Ejercicios — Capítulo 2"
content-id: MA-BCH-0090
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-002-EJERCICIOS
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-09-30
date-modified: 2026-09-30
areas: [analisis]
level: universitario
topics: [analisis-real, orden, topologia]
prerequisites: [MA-BCH-0083]
related: [MA-BOK-0010]
provenance:
  type: original
  sources:
    - "Manuscrito ANM C02; referencias de contraste en la portada del libro."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Capítulo 2](analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras.md) · [Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Ejercicios](analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras-microcontroles.md)

# Ejercicios — Capítulo 2

## §2.1. Controlar un conjunto desde arriba y desde abajo

[]{#MA-EX-ANM-01-002-001}

### 1. Barreras válidas e inválidas

Sea

$$
A=(-2,3).
$$

Para cada uno de los números

$$
-2,\qquad 3,\qquad 0,\qquad 4,
$$

decide si es:

- cota superior de $A$;
- cota inferior de $A$;
- ambas cosas;
- ninguna de las dos.

Justifica cada respuesta directamente desde las definiciones. En particular, explica por qué la pertenencia o no pertenencia del número a $A$ no decide por sí sola si es cota.

[]{#MA-EX-ANM-01-002-002}

### 2. Cuatro formas de estar acotado

Considera los conjuntos

$$
A=(-1,2),
$$

$$
B=[3,\infty),
$$

$$
C=(-\infty,5),
$$

y

$$
D=\mathbb R.
$$

Para cada conjunto:

1. decide si está acotado superiormente;
2. decide si está acotado inferiormente;
3. decide si está acotado;
4. cuando exista una cota en una dirección, exhibe una concreta;
5. cuando no exista, explica cómo producir un elemento del conjunto que destruya cualquier candidato propuesto.

No uses máximo, mínimo, supremo ni ínfimo.

[]{#MA-EX-ANM-01-002-003}

### 3. Del conjunto a todas sus cotas

Sea

$$
A=\{x\in\mathbb R:-4<x\le7\}.
$$

Determina exactamente los conjuntos

$$
U(A)
$$

y

$$
L(A).
$$

Tu respuesta debe justificar las dos inclusiones en cada caso. Es decir, no basta con proponer una semirrecta: debes explicar por qué todos sus elementos son cotas y por qué ningún número exterior a ella puede serlo.

[]{#MA-EX-ANM-01-002-004}

### 4. Mover una barrera en la dirección equivocada

Un estudiante afirma:

> Si $u$ es una cota superior de $A$ y $v<u$, entonces $v$ ya no puede ser una cota superior de $A$.

1. Decide si la afirmación es correcta.
2. Si es falsa, construye un contraejemplo explícito.
3. Formula la afirmación correcta sobre lo que ocurre cuando una cota superior se desplaza hacia la derecha.
4. Escribe y justifica la versión dual para cotas inferiores.

El diagnóstico debe distinguir cuidadosamente lo que se deduce de que $u$ sea **una** cota superior de lo que no se deduce.

[]{#MA-EX-ANM-01-002-005}

### 5. Trasladar un conjunto traslada sus barreras

Sea $A\subseteq\mathbb R$ y sea $c\in\mathbb R$. Define

$$
A+c=\{a+c:a\in A\}.
$$

Para cualquier conjunto $S\subseteq\mathbb R$, usa también la notación

$$
S+c=\{s+c:s\in S\}.
$$

1. Demuestra, usando sólo la definición de cota, que

   $$
   U(A+c)=U(A)+c.
   $$

2. Demuestra de manera dual que

   $$
   L(A+c)=L(A)+c.
   $$

3. Aplica ambas identidades a

   $$
   A=(-2,5]
   $$

   y $c=3$, determinando explícitamente $U(A)$, $L(A)$, $U(A+3)$ y $L(A+3)$.

El objetivo es identificar qué parte del lenguaje de cotas cambia y qué parte conserva su estructura cuando trasladamos todo el conjunto.

## §2.2. Extremos alcanzados: máximo y mínimo

[]{#MA-EX-ANM-01-002-006}

### 6. Cota, pertenencia y extremo

Sea

$$
A=(-3,2]\cup\{5\}.
$$

Para cada uno de los números

$$
-3,\qquad 2,\qquad 5,\qquad 6,
$$

decide:

1. si pertenece a $A$;
2. si es cota superior de $A$;
3. si es cota inferior de $A$;
4. si es máximo o mínimo de $A$, cuando corresponda.

Justifica cada clasificación usando las dos condiciones de las definiciones de máximo y mínimo. Al final, indica si $A$ posee máximo y si posee mínimo.

[]{#MA-EX-ANM-01-002-007}

### 7. Quitar un extremo cambia la respuesta

Parte del intervalo

$$
A=[-2,3].
$$

Define

$$
B=A\setminus\{3\},\qquad
C=A\setminus\{-2\},\qquad
D=A\setminus\{-2,3\}.
$$

Para cada uno de los cuatro conjuntos $A,B,C,D$:

1. decide si existe máximo;
2. decide si existe mínimo;
3. cuando exista, identifícalo;
4. cuando no exista, demuestra directamente que ningún elemento del conjunto puede desempeñar ese papel.

No uses supremo ni ínfimo. El objetivo es aislar exactamente qué efecto tiene eliminar uno o ambos extremos alcanzados.

[]{#MA-EX-ANM-01-002-008}

### 8. La intersección que contiene al máximo

Sea $A\subseteq\mathbb R$.

1. Demuestra que, si
   $$
   A\cap U(A)\ne\varnothing,
   $$
   entonces todo elemento de $A\cap U(A)$ es un máximo de $A$.
2. Demuestra que $A\cap U(A)$ no puede contener dos elementos distintos.
3. Concluye que, si $A\cap U(A)\ne\varnothing$, entonces existe un único número $M$ tal que
   $$
   A\cap U(A)=\{M\},
   $$
   y ese número es $\max A$.
4. Formula y demuestra el resultado dual usando $A\cap L(A)$ y el mínimo.

La prueba debe salir exclusivamente de pertenencia, definición de cota y antisimetría del orden.

[]{#MA-EX-ANM-01-002-009}

### 9. Dos conjuntos no vacíos no tienen por qué encontrarse

Un estudiante argumenta:

> Si $A$ es no vacío y está acotado superiormente, entonces $A\ne\varnothing$ y $U(A)\ne\varnothing$. Por tanto, $A\cap U(A)\ne\varnothing$, así que $A$ tiene máximo.

Diagnostica el razonamiento.

1. Identifica con precisión el paso lógico inválido.
2. Usa
   $$
   A=(-\infty,0)
   $$
   para calcular $U(A)$ directamente.
3. Determina $A\cap U(A)$.
4. Explica por qué este ejemplo destruye la conclusión del estudiante sin negar que $A$ esté acotado superiormente.

No uses supremo para el diagnóstico.

[]{#MA-EX-ANM-01-002-010}

### 10. Qué hacen las transformaciones afines con máximo y mínimo

Sea $A\subseteq\mathbb R$ un conjunto que posee máximo $M$ y mínimo $m$. Para $\alpha,\beta\in\mathbb R$, define

$$
T(A)=\{\alpha a+\beta:a\in A\}.
$$

Determina y demuestra, usando las definiciones de máximo y mínimo, cuáles son $\max T(A)$ y $\min T(A)$ en los tres casos:

1. $\alpha>0$;
2. $\alpha<0$;
3. $\alpha=0$.

Tu demostración debe explicar por qué el signo de $\alpha$ decide si los papeles de máximo y mínimo se conservan o se intercambian. No uses supremo ni ínfimo.

## §2.3. La mejor barrera: supremo e ínfimo

[]{#MA-EX-ANM-01-002-011}

### 11. Cota no significa barrera extremal

Sea

$$
A=(-2,3)\cup\{6\}.
$$

Analiza los seis números

$$
8,\qquad 6,\qquad 5,\qquad -4,\qquad -2,\qquad -1.
$$

1. Decide cuáles son cotas superiores de $A$.
2. Entre las cotas superiores propuestas, determina si alguna es $\sup A$.
3. Decide cuáles son cotas inferiores de $A$.
4. Entre las cotas inferiores propuestas, determina si alguna es $\inf A$.
5. Para cada candidato rechazado como supremo o ínfimo, indica exactamente qué condición de la definición falla.

No basta con identificar una cota: debes distinguir entre **controlar** al conjunto y ser la **barrera extremal**.

[]{#MA-EX-ANM-01-002-012}

### 12. Distintos conjuntos, las mismas familias de cotas

Supón que un conjunto no vacío $A\subseteq\mathbb R$ satisface

$$
U(A)=[4,\infty)
$$

y

$$
L(A)=(-\infty,-2].
$$

1. Determina $\sup A$ e $\inf A$ directamente a partir de estas dos familias de cotas.
2. Construye al menos tres conjuntos distintos $A_1,A_2,A_3\subseteq\mathbb R$ que tengan exactamente esas mismas familias $U(A_k)$ y $L(A_k)$.
3. Haz que, entre tus ejemplos, aparezcan distintas decisiones de pertenencia de $-2$ y $4$.
4. Explica qué información queda determinada por $U(A)$ y $L(A)$ y qué información sobre la pertenencia de las barreras no queda determinada.

No uses todavía la relación entre supremo y máximo.

[]{#MA-EX-ANM-01-002-013}

### 13. Por qué no puede haber dos supremos

Sea $A\subseteq\mathbb R$.

1. Supón que $s$ y $t$ satisfacen ambos la definición de supremo de $A$. Demuestra, sin citar un teorema de unicidad ya establecido, que
   $$
   s=t.
   $$
2. Identifica con precisión dónde utilizas que cada candidato es una **cota superior** y dónde utilizas que es la **menor** de las cotas superiores.
3. Repite el argumento para dos candidatos $i$ y $j$ que satisfagan ambos la definición de ínfimo.

La prueba debe reducir la unicidad a dos desigualdades opuestas y a la antisimetría del orden.

[]{#MA-EX-ANM-01-002-014}

### 14. Una condición necesaria no basta

Un estudiante afirma:

> Sea $A=(0,1)$. Como $2$ es una cota superior de $A$ y el supremo no tiene por qué pertenecer al conjunto, entonces $2=\sup A$.

Diagnostica el razonamiento.

1. Señala qué parte de la definición de supremo sí verifica el estudiante.
2. Identifica la condición que falta.
3. Determina directamente $U(A)$.
4. Usa esa descripción para explicar por qué $2$ no puede ser el supremo.
5. Formula una versión corregida del argumento que sí permita identificar $\sup A$.

Tu respuesta debe distinguir entre «ser una cota superior» y «ser la menor cota superior».

[]{#MA-EX-ANM-01-002-015}

### 15. El intervalo de control más ajustado

Sea $A\subseteq\mathbb R$ no vacío. Supón que existen

$$
i=\inf A
\qquad\text{y}\qquad
s=\sup A.
$$

Demuestra que:

1. $A\subseteq[i,s]$;
2. si $l,u\in\mathbb R$ satisfacen
   $$
   A\subseteq[l,u],
   $$
   entonces
   $$
   l\le i\le s\le u;
   $$
3. en consecuencia,
   $$
   [i,s]\subseteq[l,u].
   $$

Interpreta el resultado: entre todos los intervalos de la forma $[l,u]$ que contienen a $A$, el intervalo $[i,s]$ es el más ajustado por inclusión.

No supongas que $i$ o $s$ pertenecen a $A$.

[]{#MA-EX-ANM-01-002-016}

### 16. Trasladar y escalar una barrera extremal

Sea $A\subseteq\mathbb R$ no vacío y supón que existen

$$
s=\sup A,
\qquad
i=\inf A.
$$

Fija $\alpha>0$ y $\beta\in\mathbb R$, y define

$$
T(A)=\{\alpha a+\beta:a\in A\}.
$$

Demuestra directamente desde las definiciones que

$$
\sup T(A)=\alpha s+\beta
$$

y

$$
\inf T(A)=\alpha i+\beta.
$$

Tu prueba debe verificar por separado:

1. que $\alpha s+\beta$ es cota superior de $T(A)$;
2. que ninguna cota superior de $T(A)$ puede ser menor que $\alpha s+\beta$;
3. las dos afirmaciones duales para $\alpha i+\beta$.

No uses caracterizaciones con $\varepsilon$, sucesiones ni completitud.

## §2.4. Alcanzado frente a no alcanzado

[]{#MA-EX-ANM-01-002-017}

### 17. Cinco afirmaciones sobre alcanzar la barrera

Para cada una de las afirmaciones siguientes, decide si es siempre verdadera o falsa. Cuando sea verdadera, justifica desde las definiciones; cuando sea falsa, da un contraejemplo explícito.

1. Si $s=\sup A$ y $s\in A$, entonces $A$ tiene máximo.
2. Si $s=\sup A$ y $s\notin A$, entonces $A$ no tiene máximo.
3. Si $A$ tiene máximo $M$, entonces existe $\sup A$ y vale $M$.
4. Si $A$ no tiene máximo, entonces $A$ no tiene supremo.
5. Si $A$ tiene supremo, entonces tiene máximo.

En cada caso distingue con precisión la **existencia de la barrera extremal** de su **pertenencia al conjunto**.

[]{#MA-EX-ANM-01-002-018}

### 18. El criterio de alcanzamiento

Demuestra directamente desde las definiciones las dos equivalencias siguientes.

1. En el lado superior:
   - si $s=\sup A$ y $s\in A$, entonces $\max A=s$;
   - si $M=\max A$, entonces $M=\sup A$.

2. En el lado inferior:
   - si $i=\inf A$ y $i\in A$, entonces $\min A=i$;
   - si $m=\min A$, entonces $m=\inf A$.

Concluye que, siempre que el supremo exista,

$$
\max A\text{ existe}\quad\Longleftrightarrow\quad \sup A\in A,
$$

y formula la equivalencia dual para el mínimo.

No cites el resultado como teorema ya conocido: reconstruye cada dirección a partir de **cota + pertenencia + extremalidad**.

[]{#MA-EX-ANM-01-002-019}

### 19. Misma barrera no significa mismo máximo

Un estudiante afirma:

> Si dos conjuntos tienen el mismo supremo, entonces o bien ambos tienen máximo o bien ninguno lo tiene.

1. Diagnostica la afirmación usando
   $$
   A=[0,1],
   \qquad
   B=[0,1).
   $$
2. Determina $\sup A$, $\sup B$, $\max A$ y decide si $\max B$ existe.
3. Explica qué dato permanece igual entre $A$ y $B$ y qué dato cambia.
4. Formula una versión verdadera que relacione «tener el mismo máximo» con «tener el mismo supremo».

El objetivo es separar **posición de la barrera extremal** de **pertenencia de esa barrera**.

[]{#MA-EX-ANM-01-002-020}

### 20. Añadir la barrera o rebasarla

Sea $A\subseteq\mathbb R$ no vacío y supón que existe

$$
s=\sup A
$$

con

$$
s\notin A.
$$

Define

$$
B=A\cup\{s\}
$$

y, para un número fijo $c>s$,

$$
C=A\cup\{c\}.
$$

Demuestra que:

1. $\sup B=s$ y $\max B=s$;
2. $\sup C=c$ y $\max C=c$;
3. $U(B)=U(A)$;
4. $U(C)=[c,\infty)$.

Interpreta la diferencia: **añadir la barrera extremal** cambia el alcanzamiento sin mover la barrera, mientras que **añadir un punto más allá de ella** obliga a desplazarla.

[]{#MA-EX-ANM-01-002-021}

### 21. Intersecar el conjunto con sus propias cotas

Sea $A\subseteq\mathbb R$ no vacío y supón que existen

$$
i=\inf A,
\qquad
s=\sup A.
$$

1. Demuestra que
   $$
   A\cap U(A)
   $$
   sólo puede ser $\varnothing$ o $\{s\}$, y determina exactamente cuándo ocurre cada caso.
2. Demuestra de manera dual que
   $$
   A\cap L(A)
   $$
   sólo puede ser $\varnothing$ o $\{i\}$.
3. Deduce de estas dos identidades los criterios de existencia de máximo y mínimo.
4. Construye cuatro conjuntos con
   $$
   \inf A=0,
   \qquad
   \sup A=1,
   $$
   que realicen respectivamente las cuatro posibilidades:
   - máximo y mínimo;
   - máximo pero no mínimo;
   - mínimo pero no máximo;
   - ni máximo ni mínimo.

Este ejercicio debe conectar las tres capas ya construidas: **conjunto original, conjuntos de cotas y barreras extremales**.

## §2.5. Acercarse a una barrera sin tocarla

[]{#MA-EX-ANM-01-002-022}

### 22. Franjas pegadas a la barrera

Considera los conjuntos

$$
A=(0,1)
\qquad\text{y}\qquad
B=(0,1].
$$

En ambos casos la barrera superior extremal es $s=1$.

Para cada uno de los valores

$$
\varepsilon=1,\qquad
\varepsilon=\frac12,\qquad
\varepsilon=\frac1{10},
$$

haz lo siguiente por separado para $A$ y para $B$:

1. escribe explícitamente la franja
   $$
   (1-\varepsilon,1];
   $$
2. exhibe un elemento del conjunto que pertenezca a esa franja;
3. indica si puedes usar el mismo punto $a=1$ como testigo;
4. explica qué parte de la representación cambia entre $A$ y $B$ y qué parte permanece igual.

No organices los testigos como una sucesión. Cada valor de $\varepsilon$ representa una verificación independiente de la condición

$$
1-\varepsilon<a\le1.
$$

[]{#MA-EX-ANM-01-002-023}

### 23. Del supremo a la condición $\varepsilon$

Sea $A\subseteq\mathbb R$ no vacío y supón que

$$
s=\sup A.
$$

Demuestra directamente desde la definición de supremo que

$$
\forall\varepsilon>0\;\exists a\in A
\quad\text{tal que}\quad
s-\varepsilon<a\le s.
$$

Tu demostración debe hacer explícitos estos tres pasos:

1. por qué $s-\varepsilon<s$;
2. por qué $s-\varepsilon$ no puede ser cota superior;
3. cómo la negación de «ser cota superior» produce el elemento $a$.

No uses sucesiones, límites ni completitud.

[]{#MA-EX-ANM-01-002-024}

### 24. De la condición $\varepsilon$ al supremo

Sea $A\subseteq\mathbb R$ no vacío. Supón que $s$ es una cota superior de $A$ y que

$$
\forall\varepsilon>0\;\exists a\in A
\quad\text{tal que}\quad
s-\varepsilon<a\le s.
$$

Demuestra que

$$
s=\sup A.
$$

La prueba debe partir de una cota superior arbitraria $u$ y mostrar que $u<s$ lleva a contradicción mediante la elección

$$
\varepsilon=s-u.
$$

Indica con precisión dónde utilizas que $s$ ya es una cota superior.

[]{#MA-EX-ANM-01-002-025}

### 25. Cambiar el orden de los cuantificadores cambia la afirmación

Para $A=(0,1)$ y $s=1$, compara las dos afirmaciones:

$$
\text{(I)}\qquad
\forall\varepsilon>0\;\exists a\in A:
1-\varepsilon<a\le1,
$$

y

$$
\text{(II)}\qquad
\exists a\in A\;\forall\varepsilon>0:
1-\varepsilon<a\le1.
$$

1. Decide cuál de las dos es verdadera.
2. Explica por qué la otra falla.
3. Identifica el error conceptual de interpretar (I) como si exigiera un único punto fijo de $A$ que funcionara para todos los $\varepsilon$.
4. Da un ejemplo de un conjunto para el cual ambas afirmaciones sean verdaderas con la misma barrera $s$.

El objetivo es controlar el orden lógico

$$
\forall\varepsilon\;\exists a
$$

sin convertirlo en

$$
\exists a\;\forall\varepsilon.
$$

[]{#MA-EX-ANM-01-002-026}

### 26. La caracterización dual del ínfimo

Sea $A\subseteq\mathbb R$ no vacío.

Demuestra la equivalencia

$$
i=\inf A
\quad\Longleftrightarrow\quad
\begin{cases}
i\text{ es cota inferior de }A,\\[1mm]
\forall\varepsilon>0\;\exists a\in A:
i\le a<i+\varepsilon.
\end{cases}
$$

Debes probar las dos direcciones.

Después demuestra que esta formulación es equivalente a la siguiente:

> para todo $r>i$ existe $a\in A$ tal que
> $$
> i\le a<r.
> $$

No cites la versión superior como una «regla automática»: reconstruye el argumento dual.

[]{#MA-EX-ANM-01-002-027}

### 27. Sumar conjuntos suma sus barreras extremales

Sean $A,B\subseteq\mathbb R$ no vacíos y supón que existen

$$
s_A=\sup A,\qquad s_B=\sup B,
$$

así como

$$
i_A=\inf A,\qquad i_B=\inf B.
$$

Define la suma de conjuntos

$$
A+B=\{a+b:a\in A,\ b\in B\}.
$$

Demuestra, usando la caracterización $\varepsilon$ y sin invocar completitud, que

$$
\boxed{\sup(A+B)=s_A+s_B}
$$

y

$$
\boxed{\inf(A+B)=i_A+i_B}.
$$

Para la igualdad de supremos, organiza la prueba en dos partes:

1. demostrar que $s_A+s_B$ es cota superior de $A+B$;
2. para un $\varepsilon>0$ arbitrario, elegir separadamente $a\in A$ y $b\in B$ a una distancia menor que $\varepsilon/2$ de sus respectivas barreras superiores y combinar ambas desigualdades.

Haz el argumento dual para los ínfimos.

No introduzcas sucesiones.

## §2.6. Comparar conjuntos por sus barreras

[]{#MA-EX-ANM-01-002-028}

### 28. Dos conjuntos, cuatro familias de cotas

Considera

$$
A=(-1,1)
\qquad\text{y}\qquad
B=[-2,3).
$$

1. Verifica que $A\subseteq B$.
2. Determina exactamente $U(A)$, $L(A)$, $U(B)$ y $L(B)$.
3. Representa las cuatro familias como semirrectas sobre una misma escala.
4. Comprueba visual y algebraicamente que
   $$
   U(B)\subseteq U(A)
   \qquad\text{y}\qquad
   L(B)\subseteq L(A).
   $$
5. Identifica $\sup A$, $\sup B$, $\inf A$ e $\inf B$ y relaciona sus posiciones con las inclusiones anteriores.

El objetivo es hacer visible que **agrandar el conjunto original reduce las familias de cotas admisibles**.

[]{#MA-EX-ANM-01-002-029}

### 29. De la inclusión de conjuntos a la monotonía de sus barreras

Sean $A,B\subseteq\mathbb R$ con

$$
A\subseteq B.
$$

1. Demuestra directamente desde la definición de cota que
   $$
   U(B)\subseteq U(A).
   $$
2. Demuestra de manera dual que
   $$
   L(B)\subseteq L(A).
   $$
3. Suponiendo que existen $\sup A$ y $\sup B$, deduce que
   $$
   \sup A\le\sup B.
   $$
4. Suponiendo que existen $\inf A$ y $\inf B$, deduce que
   $$
   \inf B\le\inf A.
   $$

La prueba debe mostrar la secuencia lógica completa: **primero se comparan las familias de cotas; después sus extremos**.

[]{#MA-EX-ANM-01-002-030}

### 30. Reflejar un conjunto intercambia arriba y abajo

Sea $A\subseteq\mathbb R$ y define

$$
-A=\{-a:a\in A\}.
$$

Demuestra que

$$
U(-A)=-L(A)
$$

y

$$
L(-A)=-U(A),
$$

donde, para cualquier conjunto $S\subseteq\mathbb R$,

$$
-S=\{-s:s\in S\}.
$$

A partir de estas identidades, prueba que:

1. si $\inf A$ existe, entonces $\sup(-A)$ existe y
   $$
   \sup(-A)=-\inf A;
   $$
2. si $\sup A$ existe, entonces $\inf(-A)$ existe y
   $$
   \inf(-A)=-\sup A.
   $$

No trates estas fórmulas como reglas memorizadas: la prueba debe pasar por la inversión del orden al multiplicar por $-1$.

[]{#MA-EX-ANM-01-002-031}

### 31. Inclusión estricta no obliga a desigualdad estricta

Un estudiante afirma:

> Si $A\subsetneq B$, entonces necesariamente $\sup A<\sup B$ y $\inf B<\inf A$.

1. Diagnostica la afirmación usando
   $$
   A=(0,1),
   \qquad
   B=[0,1].
   $$
2. Calcula los cuatro extremos y explica por qué la inclusión es estricta aunque ambas desigualdades entre barreras sean igualdades.
3. Da un segundo ejemplo $C\subsetneq D$ en el que sí sean estrictas simultáneamente
   $$
   \sup C<\sup D
   \qquad\text{y}\qquad
   \inf D<\inf C.
   $$
4. Formula la conclusión general correcta que puede deducirse de $A\subseteq B$.

El diagnóstico debe distinguir **inclusión estricta de conjuntos** de **desplazamiento estricto de barreras**.

[]{#MA-EX-ANM-01-002-032}

### 32. Dónde añadir un punto determina qué barrera se mueve

Sea $A\subseteq\mathbb R$ no vacío y supón que existen

$$
i=\inf A,
\qquad
s=\sup A.
$$

Para $c\in\mathbb R$, define

$$
B_c=A\cup\{c\}.
$$

Determina y demuestra $\inf B_c$ y $\sup B_c$ en los tres casos:

1. $i\le c\le s$;
2. $c>s$;
3. $c<i$.

Tu respuesta debe explicar por qué un punto añadido **dentro del intervalo de control** $[i,s]$ no mueve ninguna barrera extremal, mientras que un punto añadido fuera de él desplaza exactamente la barrera correspondiente.

No uses ninguna garantía general de existencia: trabaja sólo con los extremos ya dados para $A$ y con el punto añadido.

[]{#MA-EX-ANM-01-002-033}

### 33. Cuándo la inclusión deja intactas todas las cotas

Sean $A,B\subseteq\mathbb R$ no vacíos con

$$
A\subseteq B,
$$

y supón que existen $\sup A$, $\sup B$, $\inf A$ e $\inf B$.

Demuestra las equivalencias

$$
\sup A=\sup B
\quad\Longleftrightarrow\quad
U(A)=U(B)
$$

y

$$
\inf A=\inf B
\quad\Longleftrightarrow\quad
L(A)=L(B).
$$

Deduce que

$$
\sup A=\sup B
\quad\text{e}\quad
\inf A=\inf B
$$

si y sólo si

$$
U(A)=U(B)
\quad\text{y}\quad
L(A)=L(B).
$$

Finalmente, construye un ejemplo con $A\subsetneq B$ para el cual se cumplan simultáneamente estas igualdades, y explica qué información sobre los conjuntos **no** queda determinada por sus familias de cotas.

El ejercicio conecta tres niveles: **inclusión de conjuntos, familias completas de cotas y barreras extremales**.

## §2.7. Definir una barrera no garantiza que exista

[]{#MA-EX-ANM-01-002-034}

### 34. Definir no es garantizar

Decide cuáles de las afirmaciones siguientes se deducen **sólo de las definiciones** desarrolladas en C02 y cuáles requieren una hipótesis o un resultado adicional. Justifica cada respuesta.

1. Si $s=\sup A$, entonces $s\in U(A)$.
2. Si $s=\sup A$, entonces $s=\min U(A)$.
3. Si $U(A)=\varnothing$, entonces $A$ no posee supremo real.
4. Si $U(A)\ne\varnothing$, entonces $\min U(A)$ existe automáticamente.
5. Haber definido $\sup A$ como la menor cota superior demuestra que todo conjunto acotado superiormente posee supremo.
6. Si $A=\varnothing$, entonces $U(A)=\mathbb R$.

En las afirmaciones 4 y 5 no debes invocar completitud. El objetivo es separar **significado de una definición** de **garantía de existencia**.

[]{#MA-EX-ANM-01-002-035}

### 35. Un mapa de los dos obstáculos

Para cada uno de los conjuntos

$$
A=(0,\infty),
\qquad
B=(0,1),
\qquad
C=\varnothing,
$$

completa una tabla con las columnas siguientes:

1. $U(X)$;
2. ¿$U(X)$ es vacío?;
3. si $U(X)\ne\varnothing$, ¿posee mínimo?;
4. ¿existe un supremo real de $X$ en el marco de C02?;
5. si falla la existencia, indica si falla el **primer obstáculo** ($U(X)=\varnothing$) o el **segundo** (no existe $\min U(X)$).

Después representa el proceso mediante el esquema lógico

$$
X
\longrightarrow
U(X)
\longrightarrow
\text{¿}U(X)\ne\varnothing\text{?}
\longrightarrow
\text{¿}\min U(X)\text{ existe?}
$$

y ubica $A,B,C$ en las ramas correspondientes.

No uses $+\infty$ como valor del supremo.

[]{#MA-EX-ANM-01-002-036}

### 36. Una conclusión correcta con una prueba incompleta

Un estudiante razona así:

> Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente. Entonces $U(A)\ne\varnothing$. Como $U(A)$ es un conjunto no vacío de números reales, debe tener mínimo. Por tanto $\sup A=\min U(A)$ existe.

Analiza el argumento.

1. Identifica el paso que no se deduce de las definiciones ni del orden por sí solo.
2. Explica por qué la no vaciedad de un subconjunto de $\mathbb R$ no basta, en general, para garantizar que tenga mínimo.
3. Aclara por qué el diagnóstico no consiste en afirmar que la conclusión final sea falsa para $\mathbb R$, sino en señalar que todavía falta una **garantía general de existencia**.
4. Indica qué tipo de resultado tendría que incorporarse para convertir el argumento en una demostración válida.

No enuncies ni demuestres todavía el teorema de completitud de C03.

[]{#MA-EX-ANM-01-002-037}

### 37. El vacío tiene todas las cotas, pero ningún extremo real

Un estudiante afirma:

> Como todo número real es cota superior e inferior de $\varnothing$, cualquier real puede elegirse como $\sup\varnothing$ y como $\inf\varnothing$.

Diagnostica la afirmación desde las definiciones.

1. Demuestra que
   $$
   U(\varnothing)=L(\varnothing)=\mathbb R.
   $$
2. Explica por qué la verdad vacía de las desigualdades universales produce todas esas cotas.
3. Demuestra que $\mathbb R$ no tiene mínimo ni máximo.
4. Concluye por qué, bajo las convenciones de C02, no definimos $\sup\varnothing$ ni $\inf\varnothing$ como números reales.
5. Compara esta falla con la de $A=(0,\infty)$, donde $U(A)=\varnothing$.

El diagnóstico debe distinguir **tener muchas cotas** de **tener una cota extremal**.

[]{#MA-EX-ANM-01-002-038}

### 38. El hueco racional: cotas sin supremo en $\mathbb Q$

Trabaja ahora en el sistema ordenado $\mathbb Q$ y considera

$$
S=\{q\in\mathbb Q:q>0\text{ y }q^2<2\}.
$$

Demuestra que $S$ posee cotas superiores racionales pero no posee supremo **dentro de $\mathbb Q$**.

Organiza la prueba así:

1. verifica que $S$ es no vacío y que $2$ es una cota superior racional;
2. demuestra que no existe $r\in\mathbb Q$ con $r^2=2$;
3. muestra que, si $r\in\mathbb Q$ y $r>0$ satisface $r^2<2$, entonces existe un racional $r'>r$ con $(r')^2<2$;
4. muestra que, si $r\in\mathbb Q$ y $r^2>2$, entonces existe una cota superior racional $u<r$ de $S$;
5. concluye que ningún racional puede ser la menor cota superior de $S$.

Puedes usar, en los pasos 3 y 4, perturbaciones racionales construidas explícitamente a partir de $r$.

Explica al final qué muestra este ejemplo sobre la diferencia entre **orden**, **existencia de cotas** y **completitud**, sin atribuir todavía a $\mathbb R$ ningún teorema no demostrado en C02.

## §2.8. De las barreras a la completitud

[]{#MA-EX-ANM-01-002-039}

### 39. Un mapa de equivalencias alrededor de una barrera

Sea $A\subseteq\mathbb R$ no vacío y sea $s\in\mathbb R$.

Compara las tres descripciones siguientes:

$$
\text{(I)}\qquad s=\min U(A),
$$

$$
\text{(II)}\qquad s=\sup A,
$$

y

$$
\text{(III)}\qquad
\begin{cases}
s\in U(A),\\[1mm]
\forall\varepsilon>0\;\exists a\in A:\ s-\varepsilon<a\le s.
\end{cases}
$$

1. Explica por qué (I) y (II) expresan exactamente la misma situación.
2. Demuestra que (II) y (III) son equivalentes usando únicamente los resultados ya establecidos en C02.
3. Añade ahora la condición $s\in A$. Demuestra que, bajo cualquiera de las tres descripciones anteriores,
   $$
   s\in A
   \quad\Longleftrightarrow\quad
   s=\max A.
   $$
4. Dibuja un mapa lógico que conecte las cuatro ideas: **conjunto de cotas**, **supremo**, **caracterización $\varepsilon$** y **máximo**.
5. Explica por qué todas estas equivalencias sirven para **reconocer** una barrera extremal pero no demuestran que, para un conjunto arbitrario acotado superiormente, exista necesariamente algún $s$ que las satisfaga.

No uses completitud ni ningún resultado de C03.

[]{#MA-EX-ANM-01-002-040}

### 40. Diseñar con precisión la pieza que falta

Considera la siguiente afirmación, que **no debes demostrar** en este ejercicio:

> **(S)** Si $A\subseteq\mathbb R$ es no vacío y está acotado superiormente, entonces existe un número real $s$ tal que $s=\sup A$.

Trabaja con (S) únicamente como una proposición hipotética cuya función es cerrar el hueco lógico detectado en C02.

1. Reescribe (S) usando $U(A)$ y la operación $\min$.
2. Explica por qué la hipótesis de acotación superior no puede simplemente eliminarse dentro de las convenciones de C02. Usa un contraejemplo explícito.
3. Explica por qué la hipótesis de no vaciedad tampoco puede eliminarse dentro de esas mismas convenciones. Usa el conjunto vacío y describe $U(\varnothing)$.
4. Formula la afirmación dual que correspondería a subconjuntos no vacíos y acotados inferiormente, **sin demostrarla ni derivarla de (S)**.
5. Supón, sólo para esta parte, que (S) estuviera disponible como una caja negra. Explica cuáles de las siguientes frases pasarían de ser condicionales a quedar automáticamente habilitadas bajo las hipótesis adecuadas y cuáles seguirían necesitando información adicional:
   - «$\sup A$ existe»;
   - «$\sup A=\max A$»;
   - «$\sup A$ satisface la caracterización $\varepsilon$»;
   - «si $A\subseteq B$, entonces $\sup A\le\sup B$».
6. Explica por qué el ejemplo racional
   $$
   S_{\mathbb Q}=\{q\in\mathbb Q:q>0\text{ y }q^2<2\}
   $$
   impide atribuir una afirmación análoga a **todo** sistema numérico ordenado sólo por poseer orden y cotas.
7. Cierra con una frase que distinga, sin ambigüedad, las dos funciones siguientes:
   - **definir** qué es un supremo;
   - **garantizar** que un supremo exista.

El objetivo no es probar completitud, sino formular exactamente qué debe aportar C03 y por qué esa aportación es lógicamente independiente de las definiciones de C02.
