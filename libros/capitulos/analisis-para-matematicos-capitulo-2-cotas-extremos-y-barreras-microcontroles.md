---
title: "Soluciones de microcontroles — Capítulo 2"
content-id: MA-BCH-0092
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-002-MICROCONTROLES
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

# Soluciones de microcontroles — Capítulo 2

## §2.1. Controlar un conjunto desde arriba y desde abajo

[]{#MA-MSOL-ANM-01-002-001}

### 1. Para $A=(-2,4)$, decide si $4$, $5$ y $3$ son cotas superiores

Los números $4$ y $5$ sí son cotas superiores de $A$.

En efecto, todo $a\in(-2,4)$ satisface $a<4$, y por tanto $a\le4$. Así,

$$
4\in U(A).
$$

Como además $5>4$, también se cumple $a<4<5$ para todo $a\in A$, de modo que

$$
5\in U(A).
$$

En cambio, $3$ no es cota superior. Por ejemplo,

$$
\frac{7}{2}\in(-2,4)
\qquad\text{y}\qquad
\frac{7}{2}>3.
$$

Por tanto,

$$
\boxed{4,5\in U(A),\qquad 3\notin U(A).}
$$

[]{#MA-MSOL-ANM-01-002-002}

### 2. Para $A=(-2,4)$, decide si $-2$, $-3$ y $0$ son cotas inferiores

Los números $-2$ y $-3$ son cotas inferiores de $A$.

Para todo $a\in(-2,4)$ tenemos $-2<a$, luego también $-2\le a$. Por tanto,

$$
-2\in L(A).
$$

Como $-3<-2<a$ para todo $a\in A$, también

$$
-3\in L(A).
$$

En cambio, $0$ no es cota inferior, porque existen elementos de $A$ menores que $0$; por ejemplo,

$$
-1\in A
\qquad\text{y}\qquad
-1<0.
$$

Así,

$$
\boxed{-2,-3\in L(A),\qquad 0\notin L(A).}
$$

[]{#MA-MSOL-ANM-01-002-003}

### 3. ¿Puede una cota superior pertenecer al conjunto? ¿Puede no pertenecer?

Sí en ambos casos. La definición de cota superior exige únicamente que el número domine a todos los elementos del conjunto; no decide su pertenencia.

Por ejemplo, para

$$
A=[0,1],
$$

el número $1$ es cota superior y pertenece a $A$.

En cambio, para

$$
B=(0,1),
$$

el mismo número $1$ es cota superior pero no pertenece a $B$.

Por tanto, ser cota superior y pertenecer al conjunto son propiedades independientes.

[]{#MA-MSOL-ANM-01-002-004}

### 4. Si $u\in U(A)$ y $v>u$, ¿qué puedes afirmar sobre $v$?

Podemos afirmar que

$$
v\in U(A).
$$

En efecto, como $u$ es cota superior,

$$
a\le u
\qquad\text{para todo }a\in A.
$$

Y como $v>u$, tenemos $u<v$, luego

$$
a\le u<v
$$

para todo $a\in A$. En particular, $a\le v$ para todo $a\in A$, que es exactamente la condición para que $v$ sea cota superior.

La familia $U(A)$ es, por tanto, estable al desplazar una cota hacia la derecha.

[]{#MA-MSOL-ANM-01-002-005}

### 5. Da un ejemplo de un conjunto infinito pero acotado

Un ejemplo es

$$
A=(0,1).
$$

El conjunto contiene infinitos números reales, pero está acotado inferiormente por $0$ y superiormente por $1$:

$$
0\le a\le1
\qquad\text{para todo }a\in A.
$$

Así, la acotación controla la posición de los elementos, no su cantidad.

[]{#MA-MSOL-ANM-01-002-006}

### 6. Da un ejemplo de un conjunto acotado superiormente pero no inferiormente

Un ejemplo es

$$
A=(-\infty,5).
$$

El número $5$ es una cota superior, porque todo $a\in A$ satisface $a<5$ y, por tanto, $a\le5$.

En cambio, $A$ no tiene cota inferior. Dado cualquier candidato $l\in\mathbb R$, el número

$$
a=l-1
$$

pertenece a $A$ siempre que $l-1<5$; si $l-1\ge5$, basta tomar $a=4$, que también satisface $a<l$. En ambos casos podemos encontrar un elemento de $A$ menor que $l$.

De forma más uniforme, puede elegirse

$$
a=\min\{4,l-1\},
$$

que cumple $a\in A$ y $a<l$. Por tanto ningún real es cota inferior de $A$.

Así,

$$
\boxed{A=(-\infty,5)\text{ está acotado superiormente, pero no inferiormente}.}
$$

## §2.2. Extremos alcanzados: máximo y mínimo

[]{#MA-MSOL-ANM-01-002-007}

### 7. Para $A=\{-3,-1,2,7\}$, determina $\max A$ y $\min A$

El número $7$ pertenece a $A$ y todo elemento de $A$ es menor o igual que $7$. Por tanto,

$$
\boxed{\max A=7}.
$$

Análogamente, $-3\in A$ y todo elemento de $A$ es mayor o igual que $-3$. Así,

$$
\boxed{\min A=-3}.
$$

[]{#MA-MSOL-ANM-01-002-008}

### 8. En $B=[-2,5)$, ¿existe máximo? ¿existe mínimo? Justifica usando las definiciones

El conjunto sí tiene mínimo. El número $-2$ pertenece a $B$ y satisface

$$
-2\le b
\qquad
\text{para todo }b\in B.
$$

Por tanto,

$$
\boxed{\min B=-2}.
$$

En cambio, $B$ no tiene máximo. Si $x\in B$, entonces $x<5$ y

$$
y=\frac{x+5}{2}
$$

satisface

$$
x<y<5.
$$

Así, $y\in B$ y $y>x$. Ningún elemento de $B$ domina a todos los demás, de modo que

$$
\boxed{B\text{ no tiene máximo}.}
$$

[]{#MA-MSOL-ANM-01-002-009}

### 9. Si $u\in U(A)$ y además $u\in A$, ¿qué puedes concluir?

Podemos concluir que $u$ es el máximo de $A$.

La condición $u\in U(A)$ significa que

$$
a\le u
\qquad
\text{para todo }a\in A.
$$

Como además $u\in A$, se cumplen exactamente las dos condiciones de la definición de máximo. Por tanto,

$$
\boxed{u=\max A}.
$$

[]{#MA-MSOL-ANM-01-002-010}

### 10. ¿Es correcta la afirmación «toda cota superior de un conjunto acotado es su máximo»? Explica el error

No. Una cota superior sólo debe dominar a todos los elementos del conjunto; para ser máximo debe, además, pertenecer al conjunto.

Por ejemplo, si

$$
A=[0,1],
$$

entonces $2$ es una cota superior, porque todo $a\in A$ cumple $a\le1<2$. Sin embargo,

$$
2\notin A,
$$

de modo que $2$ no es el máximo. En realidad,

$$
\max A=1.
$$

El error consiste en omitir la condición de pertenencia.

[]{#MA-MSOL-ANM-01-002-011}

### 11. Demuestra directamente que $(2,4)$ no tiene máximo

Sea $x\in(2,4)$ cualquier elemento. Como $x<4$, el número

$$
y=\frac{x+4}{2}
$$

satisface

$$
x<y<4.
$$

Por tanto $y\in(2,4)$ y $y>x$. Así, cualquiera que sea el elemento $x$ elegido, existe otro elemento del conjunto estrictamente mayor.

En consecuencia, ningún elemento puede ser máximo y

$$
\boxed{(2,4)\text{ no tiene máximo}.}
$$

[]{#MA-MSOL-ANM-01-002-012}

### 12. ¿Puede un conjunto tener dos máximos distintos? ¿Qué parte de la prueba de unicidad lo impide?

No. Supongamos que $M$ y $N$ fueran ambos máximos de $A$.

Como $M$ es máximo, es cota superior de $A$; y como $N\in A$, se sigue que

$$
N\le M.
$$

Del mismo modo, como $N$ es máximo y $M\in A$,

$$
M\le N.
$$

Por antisimetría del orden,

$$
\boxed{M=N}.
$$

La prueba depende de combinar las dos partes de la definición: **cada máximo es una cota superior y, al mismo tiempo, pertenece al conjunto**. Esa combinación produce las dos desigualdades opuestas; la antisimetría impide que los máximos sean distintos.

## §2.3. La mejor barrera: supremo e ínfimo

[]{#MA-MSOL-ANM-01-002-013}

### 13. Para $A=(2,5)$, determina $U(A)$ y $L(A)$ y, a partir de ellos, identifica $\sup A$ e $\inf A$

Las cotas superiores son exactamente los números mayores o iguales que $5$:

$$
U(A)=[5,\infty).
$$

En efecto, todo $u\ge5$ satisface $a<5\le u$ para todo $a\in A$, mientras que si $u<5$ existe un punto de $(2,5)$ mayor que $u$.

Dualmente,

$$
L(A)=(-\infty,2].
$$

Por tanto,

$$
\boxed{\sup A=5,\qquad \inf A=2}.
$$

Ni $2$ ni $5$ pertenecen a $A$; eso no afecta a su papel como barreras extremales.

[]{#MA-MSOL-ANM-01-002-014}

### 14. Para $B=\{-4,1,7\}$, escribe $U(B)$ y $L(B)$ y localiza sus extremos

El elemento mayor de $B$ es $7$, así que las cotas superiores son exactamente

$$
U(B)=[7,\infty).
$$

El elemento menor es $-4$, por lo que

$$
L(B)=(-\infty,-4].
$$

Los extremos de estas familias son, respectivamente,

$$
\min U(B)=7,
\qquad
\max L(B)=-4.
$$

En consecuencia,

$$
\boxed{\sup B=7,\qquad \inf B=-4}.
$$

[]{#MA-MSOL-ANM-01-002-015}

### 15. Si $s=\sup A$, ¿por qué ningún número menor que $s$ puede pertenecer a $U(A)$?

Porque $s$ es, por definición, la **menor** cota superior de $A$.

Si existiera $u<s$ con $u\in U(A)$, entonces $u$ sería una cota superior estrictamente menor que $s$, contradiciendo la minimalidad de $s$.

Por tanto,

$$
\boxed{u<s\Longrightarrow u\notin U(A)}.
$$

[]{#MA-MSOL-ANM-01-002-016}

### 16. Demuestra directamente que, si $s=\sup A$, entonces $U(A)=[s,\infty)$

Como $s=\sup A$, el número $s$ es cota superior. Si $u\ge s$, entonces para todo $a\in A$,

$$
a\le s\le u,
$$

de modo que $u\in U(A)$. Así,

$$
[s,\infty)\subseteq U(A).
$$

Recíprocamente, si $u\in U(A)$, la minimalidad del supremo obliga a

$$
s\le u.
$$

Por tanto $u\in[s,\infty)$ y

$$
U(A)\subseteq[s,\infty).
$$

Concluimos

$$
\boxed{U(A)=[s,\infty)}.
$$

[]{#MA-MSOL-ANM-01-002-017}

### 17. Formula y demuestra la afirmación dual para el ínfimo

La afirmación dual es:

> si $i=\inf A$, entonces
> $$
> L(A)=(-\infty,i].
> $$

Como $i$ es cota inferior, todo $l\le i$ satisface, para cada $a\in A$,

$$
l\le i\le a,
$$

de modo que $l\in L(A)$. Por tanto,

$$
(-\infty,i]\subseteq L(A).
$$

Si $l\in L(A)$, como $i$ es la **mayor** cota inferior, necesariamente

$$
l\le i.
$$

Luego $l\in(-\infty,i]$, y obtenemos la inclusión contraria. Así,

$$
\boxed{L(A)=(-\infty,i]}.
$$

[]{#MA-MSOL-ANM-01-002-018}

### 18. Explica por qué la definición de supremo no incluye la condición $s\in A$

Porque el supremo responde a una pregunta sobre las **cotas superiores** de $A$, no sobre la pertenencia al conjunto original.

La definición exige que $s$ sea una cota superior y que sea la menor entre todas ellas. Es decir,

$$
s\in U(A)
$$

y

$$
s\le u
\qquad\text{para todo }u\in U(A).
$$

Ninguna de estas condiciones obliga a que $s\in A$.

Por ejemplo,

$$
A=(0,1)
$$

tiene

$$
\sup A=1,
$$

aunque

$$
1\notin A.
$$

La pertenencia de la barrera extremal es una cuestión distinta, que se estudia separadamente.

## §2.4. Alcanzado frente a no alcanzado

[]{#MA-MSOL-ANM-01-002-019}

### 19. Para $A=[-1,3)$, determina $\inf A$, $\sup A$, $\min A$ y decide si existe $\max A$

La barrera inferior es $-1$, y además pertenece al conjunto. Por tanto,

$$
\inf A=-1
\qquad\text{y}\qquad
\min A=-1.
$$

La barrera superior extremal es $3$: todo elemento de $A$ es menor que $3$, y ningún número menor que $3$ puede ser cota superior porque siempre hay puntos de $[-1,3)$ situados entre ese número y $3$. Así,

$$
\sup A=3.
$$

Pero

$$
3\notin A,
$$

de modo que esa barrera no está alcanzada. Por tanto, $A$ no tiene máximo.

En resumen,

$$
\boxed{\inf A=\min A=-1,\qquad \sup A=3,\qquad \max A\text{ no existe}.}
$$

[]{#MA-MSOL-ANM-01-002-020}

### 20. Para $B=(-2,4]$, identifica qué barrera extremal está alcanzada y cuál no

Tenemos

$$
\inf B=-2
\qquad\text{y}\qquad
\sup B=4.
$$

La barrera superior está alcanzada porque

$$
4\in B.
$$

Por ello,

$$
\boxed{\max B=4=\sup B}.
$$

En cambio,

$$
-2\notin B,
$$

así que la barrera inferior extremal no está alcanzada y $B$ no tiene mínimo.

Por tanto, la barrera superior está alcanzada y la inferior no.

[]{#MA-MSOL-ANM-01-002-021}

### 21. Supón que $\sup A$ existe. Demuestra que, si $\sup A\in A$, entonces $\sup A=\max A$

Sea

$$
s=\sup A.
$$

Por definición de supremo, $s$ es una cota superior de $A$, así que

$$
a\le s
\qquad
\text{para todo }a\in A.
$$

La hipótesis adicional dice que

$$
s\in A.
$$

Se cumplen entonces exactamente las dos condiciones que definen al máximo: pertenencia y dominio de todos los elementos. Por tanto,

$$
\boxed{\max A=s=\sup A}.
$$

[]{#MA-MSOL-ANM-01-002-022}

### 22. Demuestra directamente que, si $\max A$ existe, entonces también existe $\sup A$ y ambos coinciden

Sea

$$
M=\max A.
$$

Como $M$ domina a todos los elementos de $A$, es una cota superior:

$$
M\in U(A).
$$

Ahora sea $u\in U(A)$ una cota superior cualquiera. Puesto que

$$
M\in A,
$$

la definición de cota superior aplicada a $u$ obliga a que

$$
M\le u.
$$

Así, $M$ es una cota superior menor o igual que cualquier otra cota superior. Es, por tanto, la menor cota superior de $A$.

Concluimos que el supremo existe y

$$
\boxed{\sup A=M=\max A}.
$$

[]{#MA-MSOL-ANM-01-002-023}

### 23. Da un ejemplo de una cota superior que no sea el supremo

Tomemos

$$
A=(0,1).
$$

El número $2$ es cota superior, pues todo $a\in A$ satisface

$$
a<1<2.
$$

Sin embargo,

$$
\sup A=1,
$$

de modo que $2$ no es el supremo.

Por tanto, una cota superior puede controlar al conjunto sin ser la barrera superior extremal.

[]{#MA-MSOL-ANM-01-002-024}

### 24. Da un ejemplo de un conjunto con supremo pero sin máximo, y otro con máximo

Para un conjunto con supremo pero sin máximo podemos tomar

$$
A=(0,1).
$$

Se cumple

$$
\sup A=1,
$$

pero $1\notin A$, así que $A$ no tiene máximo.

Para un conjunto con máximo podemos tomar

$$
B=(0,1].
$$

Aquí

$$
1\in B
$$

y todo $b\in B$ satisface $b\le1$. Por tanto,

$$
\boxed{\max B=1}.
$$

Además, como todo máximo es también la menor cota superior,

$$
\sup B=1.
$$

Los dos conjuntos tienen la misma barrera superior extremal; lo que cambia es si esa barrera pertenece al conjunto.

## §2.5. Acercarse a una barrera sin tocarla

[]{#MA-MSOL-ANM-01-002-025}

### 25. Para $A=(2,5)$ y $s=5$, verifica directamente la condición con $\varepsilon$

Sea $\varepsilon>0$. Debemos encontrar un elemento $a\in(2,5)$ tal que

$$
5-\varepsilon<a\le5.
$$

Tomemos

$$
\delta=\min\left\{\frac{\varepsilon}{2},1\right\}
\qquad\text{y}\qquad
a=5-\delta.
$$

Como $0<\delta\le1$, se tiene

$$
4\le a<5,
$$

por lo que $a\in(2,5)$. Además, $\delta<\varepsilon$, así que

$$
5-\varepsilon<5-\delta=a<5.
$$

Por tanto, para todo $\varepsilon>0$ existe $a\in A$ con

$$
\boxed{5-\varepsilon<a\le5}.
$$

[]{#MA-MSOL-ANM-01-002-026}

### 26. Explica por qué, si existe $\varepsilon_0>0$ tal que ningún elemento de $A$ pertenece a $(s-\varepsilon_0,s]$, entonces $s$ no puede ser el supremo

Si $s$ fuera el supremo de $A$, la caracterización $\varepsilon$ exigiría que para **todo** $\varepsilon>0$ existiera algún $a\in A$ con

$$
s-\varepsilon<a\le s.
$$

Al tomar precisamente $\varepsilon=\varepsilon_0$, la hipótesis dice que no existe ningún elemento de $A$ en esa franja. Esto contradice la condición necesaria para ser supremo.

Equivalentemente, si además recordamos que un supremo es cota superior, la ausencia de puntos en $(s-\varepsilon_0,s]$ implica que todo $a\in A$ satisface

$$
a\le s-\varepsilon_0,
$$

de modo que $s-\varepsilon_0$ sería una cota superior estrictamente menor que $s$.

Por tanto,

$$
\boxed{s\text{ no puede ser }\sup A}.
$$

[]{#MA-MSOL-ANM-01-002-027}

### 27. Supón que $A\ne\varnothing$, que $s$ es cota superior y que para todo $\varepsilon>0$ existe $a\in A$ con $s-\varepsilon<a\le s$. Demuestra que $s=\sup A$

Ya sabemos que $s$ es cota superior. Sólo falta demostrar que es la menor.

Sea $u$ cualquier cota superior de $A$. Si ocurriera que

$$
u<s,
$$

tendríamos

$$
\varepsilon=s-u>0.
$$

Por hipótesis, existe $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Pero

$$
s-\varepsilon=s-(s-u)=u,
$$

de modo que $u<a$. Esto contradice que $u$ sea cota superior.

Por tanto ninguna cota superior es menor que $s$, es decir,

$$
s\le u
\qquad\text{para toda }u\in U(A).
$$

Concluimos que

$$
\boxed{s=\sup A}.
$$

[]{#MA-MSOL-ANM-01-002-028}

### 28. Formula y demuestra la versión dual para el ínfimo

La versión dual dice: si $A\ne\varnothing$, $i$ es una cota inferior de $A$ y

$$
\forall\varepsilon>0\;\exists a\in A
\quad\text{tal que}\quad
i\le a<i+\varepsilon,
$$

entonces

$$
\boxed{i=\inf A}.
$$

En efecto, sea $l$ una cota inferior cualquiera. Si $l>i$, entonces

$$
\varepsilon=l-i>0.
$$

Por la condición dada existe $a\in A$ con

$$
i\le a<i+\varepsilon=l.
$$

Así, $a<l$, contradiciendo que $l$ sea cota inferior. Por tanto toda cota inferior satisface

$$
l\le i.
$$

Como $i$ ya era cota inferior, resulta ser la mayor de todas ellas. Luego $i=\inf A$.

[]{#MA-MSOL-ANM-01-002-029}

### 29. ¿Qué cambia en la condición cuando el supremo pertenece a $A$?

La condición cuantificada no cambia:

$$
\forall\varepsilon>0\;\exists a\in A
\quad\text{tal que}\quad
s-\varepsilon<a\le s.
$$

Lo que cambia es que, si $s\in A$, podemos escoger siempre el mismo testigo,

$$
a=s,
$$

porque para todo $\varepsilon>0$ se cumple

$$
s-\varepsilon<s=s.
$$

Si $s\notin A$, en cambio, el testigo debe estar estrictamente por debajo de $s$ y puede depender del valor de $\varepsilon$.

Así, la caracterización cubre tanto el supremo alcanzado como el no alcanzado.

[]{#MA-MSOL-ANM-01-002-030}

### 30. Explica por qué la expresión “hay puntos arbitrariamente cerca del supremo” no obliga todavía a introducir una sucesión

La afirmación que hemos probado tiene la forma

$$
\forall\varepsilon>0\;\exists a\in A
\quad\text{tal que}\quad
s-\varepsilon<a\le s.
$$

Esto sólo dice que, **después de elegir un margen positivo cualquiera**, existe algún elemento de $A$ dentro de la franja correspondiente. No hemos elegido una lista numerada de márgenes ni una familia de puntos $a_1,a_2,\dots$, y tampoco hemos formulado una afirmación de convergencia.

Cada elección de $\varepsilon$ plantea un problema independiente de existencia. Por tanto, “arbitrariamente cerca” expresa aquí una propiedad cuantificada de las franjas alrededor de $s$, no la existencia de una sucesión previamente construida.

## §2.6. Comparar conjuntos por sus barreras

[]{#MA-MSOL-ANM-01-002-031}

### 31. Si $A\subseteq B$, demuestra directamente que $U(B)\subseteq U(A)$

Sea $u\in U(B)$. Entonces

$$
b\le u
\qquad\text{para todo }b\in B.
$$

Como $A\subseteq B$, cada $a\in A$ pertenece también a $B$. Por tanto,

$$
a\le u
\qquad\text{para todo }a\in A.
$$

Esto significa que $u\in U(A)$. Como $u$ era una cota superior cualquiera de $B$, concluimos

$$
\boxed{U(B)\subseteq U(A)}.
$$

[]{#MA-MSOL-ANM-01-002-032}

### 32. Formula y demuestra la inclusión correspondiente para $L(A)$ y $L(B)$

La inclusión dual es

$$
\boxed{L(B)\subseteq L(A)}.
$$

En efecto, sea $l\in L(B)$. Entonces

$$
l\le b
\qquad\text{para todo }b\in B.
$$

Como todo $a\in A$ pertenece a $B$, también

$$
l\le a
\qquad\text{para todo }a\in A.
$$

Por tanto $l\in L(A)$, lo que prueba la inclusión.

[]{#MA-MSOL-ANM-01-002-033}

### 33. Supón que $A\subseteq B$ y que existen $\sup A$ y $\sup B$. Demuestra que $\sup A\le\sup B$

Como $\sup B$ es una cota superior de $B$, pertenece a $U(B)$. Por la inclusión recién demostrada,

$$
U(B)\subseteq U(A),
$$

de modo que $\sup B$ también es una cota superior de $A$.

Pero $\sup A$ es la menor cota superior de $A$. Luego

$$
\boxed{\sup A\le\sup B}.
$$

La desigualdad puede ser igualdad: la inclusión de conjuntos no obliga a que la barrera superior se desplace estrictamente.

[]{#MA-MSOL-ANM-01-002-034}

### 34. Da un ejemplo con $A\subsetneq B$ pero $\sup A=\sup B$

Tomemos

$$
A=(0,1)
\qquad\text{y}\qquad
B=[0,1].
$$

La inclusión es estricta porque, por ejemplo, $0\in B$ pero $0\notin A$.

Sin embargo, ambos conjuntos tienen la misma menor cota superior:

$$
\boxed{\sup A=\sup B=1}.
$$

Por tanto, de $A\subsetneq B$ no se puede deducir $\sup A<\sup B$.

[]{#MA-MSOL-ANM-01-002-035}

### 35. Si existen $\inf A$ y $\sup(-A)$, explica por qué la reflexión obliga a que $\sup(-A)=-\inf A$

Sea

$$
i=\inf A.
$$

Entonces $i$ es la mayor cota inferior de $A$. Al multiplicar las desigualdades por $-1$, toda cota inferior $l$ de $A$ se transforma en la cota superior $-l$ de $-A$. En particular,

$$
U(-A)=-L(A).
$$

Como $i$ es el mayor elemento de $L(A)$, el número $-i$ es el menor elemento de $-L(A)=U(-A)$. Por tanto,

$$
\boxed{\sup(-A)=-i=-\inf A}.
$$

La identidad expresa exactamente la inversión del orden bajo la reflexión $x\mapsto -x$.

[]{#MA-MSOL-ANM-01-002-036}

### 36. Para $A=[-1,4)$, determina $-A$ y compara sus extremos con los de $A$

Al reflejar $A$ respecto del origen obtenemos

$$
-A=(-4,1].
$$

Para el conjunto original,

$$
\inf A=-1,
\qquad
\sup A=4.
$$

Para el reflejado,

$$
\inf(-A)=-4,
\qquad
\sup(-A)=1.
$$

Estas igualdades verifican las relaciones de reflexión:

$$
\boxed{\sup(-A)=1=-\inf A}
$$

y

$$
\boxed{\inf(-A)=-4=-\sup A}.
$$

Además, $1\in -A$, por lo que $\max(-A)=1$, mientras que $-4\notin -A$, de modo que $-A$ no tiene mínimo.

## §2.7. Definir una barrera no garantiza que exista

[]{#MA-MSOL-ANM-01-002-037}

### 37. Explica por qué la definición de $\sup A$ no demuestra por sí sola que $\sup A$ exista

Una definición establece **qué condiciones tendría que satisfacer** un número para recibir el nombre de supremo, pero no asegura que haya algún número que efectivamente las cumpla.

Decir que $s=\sup A$ significa que $s$ es una cota superior y que es la menor entre todas las cotas superiores. En términos de $U(A)$,

$$
\sup A=\min U(A)
$$

cuando ese mínimo existe.

Por tanto, antes de poder escribir $\sup A$ debemos saber que $U(A)$ tiene un mínimo. Esa existencia es una cuestión adicional a la definición.

[]{#MA-MSOL-ANM-01-002-038}

### 38. Para $A=(0,\infty)$, identifica cuál de los dos obstáculos para la existencia del supremo falla primero

Falla el primer obstáculo: el conjunto no tiene cotas superiores reales.

En efecto, dado cualquier $u\in\mathbb R$, podemos elegir, por ejemplo,

$$
a=\max\{1,u+1\}.
$$

Entonces $a\in(0,\infty)$ y $a>u$, de modo que $u$ no es cota superior. Por tanto,

$$
\boxed{U(A)=\varnothing}.
$$

Ni siquiera llegamos a preguntar si $U(A)$ tiene mínimo, porque no hay cotas superiores entre las cuales buscar una barrera extremal.

[]{#MA-MSOL-ANM-01-002-039}

### 39. Demuestra que $U(\varnothing)=L(\varnothing)=\mathbb R$

Sea $u\in\mathbb R$. Para que $u$ sea cota superior de $\varnothing$ debe cumplirse

$$
\forall a\in\varnothing,\qquad a\le u.
$$

Como no existe ningún elemento $a\in\varnothing$ que pueda violar esta desigualdad, la afirmación universal es verdadera. Así, **todo** real es cota superior de $\varnothing$ y

$$
U(\varnothing)=\mathbb R.
$$

Del mismo modo, para cualquier $l\in\mathbb R$ la afirmación

$$
\forall a\in\varnothing,\qquad l\le a
$$

es verdadera por la misma razón. Por tanto,

$$
L(\varnothing)=\mathbb R.
$$

En conjunto,

$$
\boxed{U(\varnothing)=L(\varnothing)=\mathbb R}.
$$

[]{#MA-MSOL-ANM-01-002-040}

### 40. Explica por qué de la igualdad anterior no se obtiene un supremo o un ínfimo real del conjunto vacío

Para obtener un supremo real necesitaríamos

$$
\sup\varnothing=\min U(\varnothing).
$$

Pero

$$
U(\varnothing)=\mathbb R,
$$

y $\mathbb R$ no tiene mínimo: dado cualquier $x\in\mathbb R$, el número $x-1$ es menor.

Análogamente, un ínfimo real requeriría

$$
\inf\varnothing=\max L(\varnothing),
$$

pero $L(\varnothing)=\mathbb R$ y $\mathbb R$ no tiene máximo, porque $x+1>x$ para todo $x\in\mathbb R$.

Así, con las convenciones de C02,

$$
\boxed{\sup\varnothing\text{ e }\inf\varnothing\text{ no existen como números reales}.}
$$

[]{#MA-MSOL-ANM-01-002-041}

### 41. ¿Qué muestra conceptualmente el contraste con $\mathbb Q$ respecto del papel del orden?

Muestra que **tener un orden y disponer de cotas superiores no basta, por sí solo, para garantizar una menor cota superior dentro del mismo sistema numérico**.

El conjunto racional considerado en el manuscrito,

$$
S=\{q\in\mathbb Q:q>0\text{ y }q^2<2\},
$$

tiene cotas superiores en $\mathbb Q$, pero el contraste está precisamente diseñado para mostrar que de ese hecho no se sigue automáticamente la existencia de una menor cota superior racional.

La función del ejemplo en C02 es conceptual: separar las propiedades del **orden** de la propiedad adicional que hará falta para garantizar extremos. No usamos aquí ese contraste para demostrar la completitud de $\mathbb R$.

[]{#MA-MSOL-ANM-01-002-042}

### 42. Distingue entre “verificar un supremo en un ejemplo” y “garantizar la existencia del supremo para toda una clase de conjuntos”

**Verificar un supremo en un ejemplo** significa tomar un conjunto concreto $A$ y un candidato concreto $s$, y demostrar directamente que:

1. $s$ es cota superior de $A$;
2. ninguna cota superior de $A$ es menor que $s$.

Por ejemplo, para $A=(0,1)$ puede verificarse directamente que $1=\sup A$.

En cambio, **garantizar la existencia para toda una clase de conjuntos** significa demostrar un enunciado universal del tipo:

> todo conjunto que satisfaga ciertas hipótesis posee un supremo.

Ese segundo nivel no se obtiene repitiendo la definición: requiere una propiedad general que asegure la existencia del extremo. C02 formula esta necesidad, pero no demuestra todavía esa garantía general.

## §2.8. De las barreras a la completitud

[]{#MA-MSOL-ANM-01-002-043}

### 43. ¿Por qué $\sup A$ puede existir sin pertenecer a $A$?

Porque la definición de supremo no exige pertenencia al conjunto original. Exige que $\sup A$ sea una cota superior de $A$ y que sea la menor entre todas las cotas superiores.

Por ejemplo, para

$$
A=(0,1)
$$

tenemos

$$
\sup A=1,
$$

pero

$$
1\notin A.
$$

No hay contradicción: $1$ es la barrera superior extremal aunque el conjunto no la alcance. La pertenencia es la condición adicional que distingue al máximo.

[]{#MA-MSOL-ANM-01-002-044}

### 44. ¿Por qué, si $\max A$ existe, entonces coincide necesariamente con $\sup A$?

Sea

$$
M=\max A.
$$

Como $M$ es máximo, pertenece a $A$ y domina a todos sus elementos. Por tanto, $M$ es una cota superior.

Ahora sea $u$ cualquier otra cota superior de $A$. Como $M\in A$ y $u$ domina a todo elemento de $A$, necesariamente

$$
M\le u.
$$

Así, $M$ es menor o igual que toda cota superior: es la menor cota superior. En consecuencia,

$$
\boxed{\max A=\sup A}.
$$

[]{#MA-MSOL-ANM-01-002-045}

### 45. ¿Qué niega exactamente la condición

$$
\forall\varepsilon>0\;\exists a\in A:
\quad
\sup A-\varepsilon<a\le\sup A?
$$

Niega que exista un margen positivo fijo por debajo del supremo que deje a todo el conjunto separado de la barrera.

En efecto, si existiera algún $\varepsilon_0>0$ sin elementos de $A$ en

$$
(\sup A-\varepsilon_0,\sup A],
$$

entonces $\sup A-\varepsilon_0$ seguiría siendo una cota superior de $A$. Pero sería estrictamente menor que $\sup A$, contradiciendo que éste sea la menor cota superior.

Por tanto, la condición expresa que **ninguna disminución positiva del supremo sigue controlando al conjunto completo**.

[]{#MA-MSOL-ANM-01-002-046}

### 46. ¿Qué nueva afirmación necesita C03 para convertir la teoría condicional de C02 en una garantía general de existencia dentro de $\mathbb R$?

C03 necesita introducir y justificar la afirmación:

> **Todo subconjunto no vacío de $\mathbb R$ que esté acotado superiormente posee un supremo en $\mathbb R$.**

Ésta es una afirmación de **existencia general**. No redefine qué es un supremo: garantiza que, bajo las hipótesis adecuadas, el objeto definido existe.

C02 sólo identifica esta pieza faltante y no la usa como teorema. La demostración o adopción de esa propiedad pertenece al capítulo siguiente.
