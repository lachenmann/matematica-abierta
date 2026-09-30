---
title: "Ejercicios — Capítulo 4"
content-id: MA-BCH-0096
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-004-EJERCICIOS
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
    - "Manuscrito ANM C04; referencias de contraste en la portada del libro."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Capítulo 4](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto.md) · [Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Ejercicios](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-microcontroles.md)

# Ejercicios — Capítulo 4

## §4.1. Ventanas alrededor de un punto: vecindades

[]{#MA-EX-ANM-01-004-001}

### 1. Una definición, varias formas lógicas

Sean $V\subseteq\mathbb R$ y $x\in\mathbb R$. Considera las afirmaciones:

1. existe $r>0$ tal que
   $$
   B(x,r)\subseteq V;
   $$
2. existe $r>0$ tal que, para todo $y\in\mathbb R$,
   $$
   |y-x|<r
   \Longrightarrow
   y\in V;
   $$
3. existe $r>0$ tal que
   $$
   (x-r,x+r)\subseteq V;
   $$
4. para todo $r>0$ existe $y\in V$ tal que
   $$
   |y-x|<r.
   $$

a) Demuestra que las afirmaciones 1, 2 y 3 son equivalentes.

b) Explica por qué la afirmación 4 tiene una estructura lógica distinta. Identifica con precisión el orden de los cuantificadores en 2 y en 4.

c) Da un ejemplo de $V$ y $x$ para el cual 4 sea verdadera pero 1 sea falsa.

d) Formula con palabras qué información adicional exige una vecindad respecto de la mera afirmación de que siempre aparecen puntos de $V$ cerca de $x$.

No uses ninguna terminología de secciones posteriores.

[]{#MA-EX-ANM-01-004-002}

### 2. El conjunto de radios que realmente sirven

Sea

$$
V=(-4,3)\cup\{100\}.
$$

Para un punto $x\in V$, define el conjunto de radios admisibles

$$
R_V(x)
=
\{r>0:B(x,r)\subseteq V\}.
$$

a) Determina exactamente $R_V(-1)$.

b) Determina exactamente $R_V(2)$.

c) Decide si $R_V(100)$ es vacío o no vacío y justifica tu respuesta.

d) Explica por qué el punto aislado $\{100\}$ no ayuda a aumentar los radios admisibles alrededor de $-1$ ni alrededor de $2$.

e) Compara $R_V(-1)$ y $R_V(2)$ y explica qué muestra el ejemplo acerca de la dependencia del radio respecto del centro.

Tu respuesta debe distinguir entre «pertenecer a $V$» y «disponer de un radio positivo cuya bola completa quede dentro de $V$».

[]{#MA-EX-ANM-01-004-003}

### 3. Intersecciones finitas sí; intersecciones arbitrarias, no

Sea $x\in\mathbb R$ y sean

$$
V_1,\dots,V_n
$$

vecindades de $x$.

a) Demuestra que

$$
\bigcap_{k=1}^nV_k
$$

también es una vecindad de $x$.

Tu prueba debe:

1. elegir, para cada $k$, un radio $r_k>0$ con
   $$
   B(x,r_k)\subseteq V_k;
   $$
2. construir un único radio positivo que funcione simultáneamente para todos los conjuntos;
3. indicar exactamente por qué la finitud de la familia permite hacer esa elección.

b) Considera ahora, para cada $r>0$,

$$
V_r=(-r,r).
$$

Demuestra que cada $V_r$ es una vecindad de $0$, pero que

$$
\bigcap_{r>0}V_r=\{0\}.
$$

c) Concluye que una intersección arbitraria de vecindades de un mismo punto no tiene por qué ser una vecindad de ese punto.

No uses teoría de conjuntos abiertos ni resultados de §4.7.

[]{#MA-EX-ANM-01-004-004}

### 4. Cuando «tocar» una ventana se confunde con «llenarla»

Un estudiante quiere demostrar que

$$
V=[0,\infty)
$$

es una vecindad de $0$ y escribe:

> Sea $r>0$. El número $r/2$ pertenece a $V$ y además $|r/2|<r$. Por tanto
> $$
> B(0,r)\cap V\ne\varnothing.
> $$
> Como esto ocurre para todo $r>0$, $V$ contiene puntos arbitrariamente cercanos a $0$. Luego $V$ es una vecindad de $0$.

Audita el argumento.

a) Identifica exactamente qué afirmación cuantificada ha demostrado el estudiante.

b) Escribe la afirmación cuantificada que realmente tendría que demostrar para concluir que $V$ es vecindad de $0$.

c) Localiza el cambio ilegítimo entre ambas afirmaciones.

d) Demuestra directamente que $V$ no es una vecindad de $0$: para un radio arbitrario $r>0$, construye un punto de $B(0,r)$ que no pertenezca a $V$.

e) Repara la conclusión del estudiante sin introducir aún nombres de conceptos posteriores: expresa sólo qué propiedad local de $V$ alrededor de $0$ sí quedó demostrada.

## §4.2. Interior y exterior: tener margen

[]{#MA-EX-ANM-01-004-005}

### 5. Negar correctamente el margen

Sean $A\subseteq\mathbb R$ y $x\in\mathbb R$. Considera

$$
I(x,A):
\exists r>0:\ B(x,r)\subseteq A
$$

y

$$
E(x,A):
\exists r>0:\ B(x,r)\subseteq A^c.
$$

a) Escribe la negación de $I(x,A)$ sin usar la expresión «no es interior». La fórmula final debe comenzar con $\forall r>0$.

b) Escribe de la misma manera la negación de $E(x,A)$.

c) Demuestra que $I(x,A)$ y $E(x,A)$ no pueden ser verdaderas simultáneamente.

d) Muestra que sus negaciones sí pueden ser verdaderas simultáneamente. Usa

$$
A=[0,1],
\qquad
x=0,
$$

y verifica directamente las dos condiciones cuantificadas.

e) Explica por qué la alternativa «interior o exterior» no agota necesariamente todos los puntos de $\mathbb R$.

No nombres todavía la tercera clase local que aparecerá más adelante.

[]{#MA-EX-ANM-01-004-006}

### 6. Dos familias de radios alrededor del mismo conjunto

Sea

$$
A=(-3,-1]\cup(1,4).
$$

Para $x\in\mathbb R$, define

$$
R_{\mathrm{in}}(x)
=
\{r>0:B(x,r)\subseteq A\}
$$

y

$$
R_{\mathrm{out}}(x)
=
\{r>0:B(x,r)\subseteq A^c\}.
$$

Determina exactamente ambas familias de radios para

$$
x=-2,\qquad x=0,\qquad x=-1,\qquad x=4.
$$

Después:

a) identifica qué puntos son interiores, cuáles son exteriores y cuáles no pertenecen a ninguna de esas dos clases;

b) explica qué información aporta conocer el conjunto completo de radios admisibles, en lugar de limitarse a saber si existe alguno;

c) compara los casos $x=-1$ y $x=4$: uno pertenece a $A$ y el otro no, pero ambos producen el mismo patrón de radios admisibles. Explica por qué esto confirma que pertenencia y margen local son datos distintos.

[]{#MA-EX-ANM-01-004-007}

### 7. Clasificar todo un conjunto por margen local

Considera

$$
A=[-2,-1)\cup\{0\}\cup(1,3].
$$

Determina exactamente

$$
\operatorname{int}(A)
$$

y

$$
\operatorname{ext}(A).
$$

Tu respuesta debe ser una demostración por casos, no una inspección gráfica.

En particular:

a) construye radios explícitos para los puntos que afirmes interiores;

b) construye radios explícitos para los puntos que afirmes exteriores;

c) demuestra que ninguno de los puntos

$$
-2,\qquad -1,\qquad 0,\qquad 1,\qquad 3
$$

es interior ni exterior;

d) verifica al final que cada punto real ha quedado clasificado como interior, exterior o dentro del conjunto excepcional anterior.

No uses todavía ninguna noción posterior a §4.2.

[]{#MA-EX-ANM-01-004-008}

### 8. Cómo se comporta el interior bajo operaciones de conjuntos

Sean $A,B\subseteq\mathbb R$.

a) Demuestra directamente que

$$
\operatorname{int}(A\cap B)
=
\operatorname{int}(A)\cap\operatorname{int}(B).
$$

En la inclusión no inmediata deberás sincronizar dos radios.

b) Usa

$$
\operatorname{ext}(C)=\operatorname{int}(C^c)
$$

y una ley de De Morgan para deducir

$$
\operatorname{ext}(A\cup B)
=
\operatorname{ext}(A)\cap\operatorname{ext}(B).
$$

c) Demuestra que siempre

$$
\operatorname{int}(A)\cup\operatorname{int}(B)
\subseteq
\operatorname{int}(A\cup B).
$$

d) Muestra que la inclusión del apartado c) puede ser estricta usando

$$
A=[-1,0],
\qquad
B=[0,1].
$$

Identifica el punto que pertenece al interior de $A\cup B$ pero no a $\operatorname{int}(A)\cup\operatorname{int}(B)$.

[]{#MA-EX-ANM-01-004-009}

### 9. Añadir puntos sin crear margen

Sea $t>1$ y considera

$$
A_t=(0,1)\cup\{t\},
$$

y

$$
B_t=[0,1)\cup\{t\}.
$$

a) Demuestra que, para todo $t>1$,

$$
\operatorname{int}(A_t)
=
\operatorname{int}(B_t)
=
(0,1).
$$

b) Demuestra que

$$
\operatorname{ext}(A_t)
=
\operatorname{ext}(B_t)
=
(-\infty,0)\cup(1,t)\cup(t,\infty).
$$

c) Compara $A_t$ con $(0,1)$. ¿Qué efecto tiene añadir el punto $t$ sobre el interior? ¿Qué efecto tiene sobre el exterior?

d) Compara $A_t$ con $B_t$. El punto $0$ cambia de pertenencia, pero el interior y el exterior no cambian. Justifica por qué.

e) Formula con tus propias palabras una conclusión general: ¿qué muestra esta familia acerca de la diferencia entre modificar la pertenencia de algunos puntos y modificar el margen local?

## §4.3. Clausura: puntos que no pueden evitar al conjunto

[]{#MA-EX-ANM-01-004-010}

### 10. Una clausura con intervalos y un punto separado

Sea

$$
A=(-2,-1)\cup\{0\}\cup(1,2).
$$

Determina exactamente $\overline A$.

Tu demostración debe separar tres tipos de puntos:

1. puntos que ya pertenecen a $A$;
2. puntos que no pertenecen a $A$ pero que toda bola positiva alrededor de ellos obliga a tocar $A$;
3. puntos para los cuales puedes construir una bola positiva disjunta de $A$.

No basta escribir la respuesta por analogía con intervalos. Debes justificar explícitamente qué ocurre en

$$
-2,\quad -1,\quad 0,\quad 1,\quad 2
$$

y explicar por qué no hay otros puntos adherentes.

[]{#MA-EX-ANM-01-004-011}

### 11. La clausura de una unión finita

Sean $A,B\subseteq\mathbb R$.

Demuestra que

$$
\boxed{
\overline{A\cup B}
=
\overline A\cup\overline B.
}
$$

Organiza la prueba como una igualdad de conjuntos.

Para una de las inclusiones puedes usar la monotonicidad de la clausura ya demostrada en §4.3. Para la otra, si decides argumentar por contradicción, deberás:

1. suponer que un punto no pertenece ni a $\overline A$ ni a $\overline B$;
2. obtener dos radios positivos que eviten respectivamente a $A$ y a $B$;
3. sincronizar esos radios;
4. explicar por qué la bola resultante evita a $A\cup B$.

Al final, identifica dónde se usa que sólo hay **dos** conjuntos.

[]{#MA-EX-ANM-01-004-012}

### 12. La intersección se comporta de otra manera

Sean $A,B\subseteq\mathbb R$.

a) Demuestra que siempre

$$
\boxed{
\overline{A\cap B}
\subseteq
\overline A\cap\overline B.
}
$$

b) Decide si la igualdad tiene que cumplirse siempre.

c) Si no es así, usa

$$
A=(-1,0),
\qquad
B=(0,1)
$$

para demostrar que la inclusión puede ser estricta.

d) Explica por qué el fracaso de la igualdad no contradice la identidad del ejercicio anterior.

Tu solución no debe invocar conjuntos cerrados ni resultados de §4.7.

[]{#MA-EX-ANM-01-004-013}

### 13. Reparar una prueba de idempotencia

Un estudiante intenta demostrar

$$
\overline{\overline A}\subseteq\overline A
$$

de la siguiente manera:

> Sea $x\in\overline{\overline A}$ y sea $r>0$. Como $x$ es adherente a $\overline A$, existe
> $$
> y\in B(x,r)\cap\overline A.
> $$
> Como $y\in\overline A$, existe
> $$
> a\in B(y,r)\cap A.
> $$
> Por la desigualdad triangular,
> $$
> |a-x|
> \le |a-y|+|y-x|
> <r+r.
> $$
> Luego $a\in B(x,r)$, y por tanto $x\in\overline A$.

Audita el argumento.

a) Identifica la línea exacta que no está justificada.

b) Explica qué conclusión sí permite obtener la estimación

$$
|a-x|<2r.
$$

c) Repara la prueba cambiando únicamente la elección de los radios de las dos bolas auxiliares.

d) Explica por qué la elección corregida permite cerrar el argumento para un radio **arbitrario** $r>0$.

e) Resume en una frase el mecanismo reutilizable de la reparación.

[]{#MA-EX-ANM-01-004-014}

### 14. Perforar, rellenar y añadir un punto separado

Sea $t\in(0,1)$ y define

$$
A_t=(0,1)\setminus\{t\},
$$

$$
B_t=A_t\cup\{t\}=(0,1),
$$

y

$$
C_t=A_t\cup\{2\}.
$$

a) Demuestra directamente, sin sucesiones, que

$$
\overline{A_t}=[0,1].
$$

Tu argumento debe tratar por separado:

- los puntos de $A_t$;
- el punto perforado $t$;
- los extremos $0$ y $1$;
- los puntos exteriores a $[0,1]$.

b) Deduce que

$$
\overline{B_t}=[0,1].
$$

c) Demuestra que

$$
\overline{C_t}=[0,1]\cup\{2\}.
$$

Puedes usar el resultado del ejercicio 11.

d) Compara las tres operaciones:

1. quitar el punto interior $t$;
2. volver a añadirlo;
3. añadir el punto separado $2$.

Explica por qué las dos primeras no cambian la clausura, mientras que la tercera sí.

e) Formula una conclusión conceptual: ¿qué información local detecta la clausura que la simple pertenencia de un punto no registra?

## §4.4. Frontera: toda ventana ve ambos lados

[]{#MA-EX-ANM-01-004-015}

### 15. El espacio lógico de tres estados locales

Sean $A\subseteq\mathbb R$ y $x\in\mathbb R$. Considera las dos preguntas:

$$
P_A(x):
\exists r>0:\ B(x,r)\subseteq A,
$$

y

$$
Q_A(x):
\exists r>0:\ B(x,r)\subseteq A^c.
$$

Representa el estado local de $x$ mediante el par de respuestas

$$
\bigl(P_A(x),Q_A(x)\bigr).
$$

a) Explica por qué el estado

$$
(\text{sí},\text{sí})
$$

es imposible.

b) Interpreta matemáticamente los estados

$$
(\text{sí},\text{no}),
\qquad
(\text{no},\text{sí}),
\qquad
(\text{no},\text{no}).
$$

c) Demuestra que el estado $(\text{no},\text{no})$ equivale a

$$
\forall r>0:
\bigl(B(x,r)\cap A\ne\varnothing\bigr)
\ \text{y}\
\bigl(B(x,r)\cap A^c\ne\varnothing\bigr).
$$

d) Resume el resultado en una tabla con tres filas: interior, exterior y frontera. La tabla debe mostrar qué cambia en el cuantificador y en el lado del conjunto que ocupa la ventana.

[]{#MA-EX-ANM-01-004-016}

### 16. Clasificar una configuración completa

Sea

$$
A=[-2,-1)\cup\{0\}\cup(1,2].
$$

Determina exactamente

$$
\operatorname{int}(A),
\qquad
\operatorname{ext}(A),
\qquad
\partial A.
$$

Tu solución debe justificar explícitamente:

1. qué radios sirven para puntos interiores;
2. qué radios sirven para puntos exteriores;
3. por qué
   $$
   -2,\ -1,\ 0,\ 1,\ 2
   $$
   son puntos de frontera;
4. por qué no hay otros puntos fronterizos.

Al final, verifica directamente la partición

$$
\mathbb R
=
\operatorname{int}(A)
\,\dot\cup\,
\partial A
\,\dot\cup\,
\operatorname{ext}(A).
$$

[]{#MA-EX-ANM-01-004-017}

### 17. La frontera de una unión no puede aparecer de la nada

Sean $A,B\subseteq\mathbb R$.

a) Demuestra que

$$
\boxed{
\partial(A\cup B)
\subseteq
\partial A\cup\partial B.
}
$$

Puedes organizar la prueba por contraposición usando la partición local interior–frontera–exterior.

b) Usa la identidad

$$
\partial(C^c)=\partial C
$$

y una ley de De Morgan para deducir

$$
\boxed{
\partial(A\cap B)
\subseteq
\partial A\cup\partial B.
}
$$

c) Muestra que la inclusión del apartado a) puede ser estricta con

$$
A=[-1,0],
\qquad
B=[0,1].
$$

d) Explica geométricamente por qué el punto $0$ desaparece de la frontera cuando pasamos de los dos conjuntos separados a su unión.

[]{#MA-EX-ANM-01-004-018}

### 18. Dos radios que no están sincronizados

Un estudiante quiere probar que $x\in\partial A$ y dispone de la siguiente información:

- para todo $r>0$, existe
  $$
  a_r\in A
  $$
  con
  $$
  |a_r-x|<r;
  $$
- para todo $r>0$, existe
  $$
  b_r\in A^c
  $$
  con
  $$
  |b_r-x|<2r.
  $$

Entonces escribe:

> Para un radio arbitrario $r>0$, los puntos $a_r$ y $b_r$ están ambos suficientemente cerca de $x$. Por tanto
> $$
> B(x,r)
> $$
> intersecta a $A$ y a $A^c$, así que $x\in\partial A$.

a) Identifica el paso no justificado.

b) Explica qué sí garantiza la desigualdad $|b_r-x|<2r$.

c) Decide si las hipótesis del estudiante son suficientes para demostrar que $x\in\partial A$.

d) Si lo son, repara la demostración mediante una reparametrización adecuada del segundo radio.

e) Explica qué enseña este ejemplo sobre la necesidad de sincronizar escalas cuando una definición exige dos condiciones dentro de la **misma** bola.

[]{#MA-EX-ANM-01-004-019}

### 19. La frontera no es monótona

Una primera intuición podría sugerir que, si

$$
A\subseteq B,
$$

entonces debería cumplirse

$$
\partial A\subseteq\partial B.
$$

Construye una familia paramétrica que destruya esa intuición.

Sea $c\in\mathbb R$ y $R>0$. Define

$$
A=\{c\},
\qquad
B=(c-R,c+R).
$$

a) Demuestra que $A\subseteq B$.

b) Calcula directamente

$$
\partial A
$$

y

$$
\partial B.
$$

c) Concluye que

$$
\partial A\not\subseteq\partial B.
$$

d) Observa además que

$$
\partial B\not\subseteq\partial A.
$$

e) Demuestra que, de hecho,

$$
\partial A\cap\partial B=\varnothing.
$$

f) Explica por qué agrandar un conjunto puede hacer desaparecer una frontera antigua y crear otra en una región diferente.

Tu argumento debe usar únicamente las definiciones locales disponibles hasta §4.4.

## §4.5. Acumulación: el conjunto reaparece alrededor del punto

[]{#MA-EX-ANM-01-004-020}

### 20. Negar una bola perforada

Sean $A\subseteq\mathbb R$ y $x\in\mathbb R$.

a) Escribe con cuantificadores la afirmación
$$
x\in\operatorname{Acc}(A).
$$

b) Niega correctamente esa afirmación y demuestra que
$$
x\notin\operatorname{Acc}(A)
\iff
\exists r>0:
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A=\varnothing.
$$

c) Compara esta negación con $x\notin\overline A$. Explica con precisión qué papel desempeña el centro $x$ en cada caso.

d) Usa $A=\{0\}$ y $x=0$ para mostrar que puede ocurrir
$$
x\in\overline A
\qquad\text{y}\qquad
x\notin\operatorname{Acc}(A).
$$

e) Usa $A=(0,1)$ y $x=0$ para mostrar que un punto puede pertenecer a $\operatorname{Acc}(A)$ sin pertenecer a $A$.

[]{#MA-EX-ANM-01-004-021}

### 21. Calcular todos los puntos de acumulación

Sea
$$
A=(-2,-1)\cup\{0\}\cup(1,2].
$$

Determina exactamente $\operatorname{Acc}(A)$.

Tu demostración debe tratar por separado los puntos interiores de los dos intervalos, los cuatro extremos $-2,-1,1,2$, el punto $0$, los puntos de los huecos $(-1,0)$ y $(0,1)$ y los puntos exteriores a $[-2,2]$.

Para cada punto que afirmes de acumulación, comienza con un radio arbitrario $r>0$ y construye un punto de $A$ distinto del centro dentro de la bola perforada. Para cada punto que excluyas, exhibe un radio positivo que destruya la condición universal.

[]{#MA-EX-ANM-01-004-022}

### 22. La acumulación de una unión finita

Sean $A,B\subseteq\mathbb R$. Demuestra que
$$
\operatorname{Acc}(A\cup B)
=
\operatorname{Acc}(A)\cup\operatorname{Acc}(B).
$$

La prueba debe incluir la inclusión obtenida por monotonicidad y la inclusión contraria por contraposición, usando la negación correcta del test de acumulación y un único radio que haga fallar dicho test para $A\cup B$.

Explica al final por qué el argumento depende de que la unión sea finita. No uses sucesiones.

[]{#MA-EX-ANM-01-004-023}

### 23. Dos testigos distintos no producen un testigo común

Un estudiante afirma que
$$
\operatorname{Acc}(A\cap B)
=
\operatorname{Acc}(A)\cap\operatorname{Acc}(B)
$$
porque toda bola perforada que toca a $A$ y a $B$ debería tocar a $A\cap B$.

a) Identifica el salto lógico.

b) Usa
$$
A=(-1,0),\qquad B=(0,1),\qquad x=0
$$
para refutar la igualdad.

c) Demuestra la inclusión correcta
$$
\operatorname{Acc}(A\cap B)
\subseteq
\operatorname{Acc}(A)\cap\operatorname{Acc}(B).
$$

d) Explica por qué «existe un punto de $A$ y existe un punto de $B$» no equivale a «existe un mismo punto de $A\cap B$».

[]{#MA-EX-ANM-01-004-024}

### 24. Quitar un punto, añadirlo y colocar otro lejos

Sean $s\in(0,1)$ y $t>1$, y define
$$
A=(0,1),\qquad
B=(0,1)\setminus\{s\},\qquad
C=(0,1)\cup\{t\}.
$$

Demuestra, sin sucesiones, que
$$
\operatorname{Acc}(A)
=
\operatorname{Acc}(B)
=
\operatorname{Acc}(C)
=
[0,1].
$$

Justifica específicamente por qué quitar $s$ no destruye la acumulación en $s$, por qué los demás puntos de $[0,1]$ siguen siendo de acumulación, por qué $t$ no se convierte en punto de acumulación y por qué no aparecen nuevos puntos de acumulación fuera de $[0,1]$.

Concluye explicando qué diferencia conceptual existe entre modificar la pertenencia de algunos puntos y modificar el conjunto de puntos de acumulación.

## §4.6. Puntos aislados y descomposición local

[]{#MA-EX-ANM-01-004-025}

### 25. Dos comportamientos dentro del mismo conjunto

Sea

$$
A=(-2,-1)\cup\{0,2\}.
$$

Clasifica **cada punto de $A$** como punto de acumulación de $A$ o como punto aislado de $A$.

Tu solución debe:

a) demostrar que todo

$$
x\in(-2,-1)
$$

es punto de acumulación mediante una bola perforada arbitraria;

b) exhibir un radio que aísle al punto $0$;

c) exhibir un radio que aísle al punto $2$;

d) escribir al final la descomposición

$$
A
=
\bigl(A\cap\operatorname{Acc}(A)\bigr)
\,\dot\cup\,
\bigl(A\setminus\operatorname{Acc}(A)\bigr)
$$

para este conjunto concreto;

e) explicar qué información adicional aporta esta descomposición respecto de la mera afirmación $A\subseteq\overline A$.

[]{#MA-EX-ANM-01-004-026}

### 26. Aislamiento expresado mediante vecindades

Sean $A\subseteq\mathbb R$ y $x\in A$.

Demuestra la equivalencia

$$
\boxed{
x\text{ es aislado en }A
\iff
\exists V\text{ vecindad de }x:
V\cap A=\{x\}.
}
$$

La demostración debe cubrir ambos sentidos.

En la dirección de izquierda a derecha, explica por qué una bola que aísla al centro es ya una vecindad adecuada.

En la dirección de derecha a izquierda, parte de una vecindad general $V$ y vuelve explícitamente a una bola

$$
B(x,r)\subseteq V.
$$

Concluye explicando por qué la palabra «vecindad» no cambia el contenido matemático de la definición, sino sólo comprime la existencia de una bola suficientemente pequeña.

[]{#MA-EX-ANM-01-004-027}

### 27. No ser de acumulación no basta para ser aislado

Refuta la afirmación

> Si $x\notin\operatorname{Acc}(A)$, entonces $x$ es aislado en $A$.

Tu respuesta debe:

a) dar un contraejemplo con un conjunto elemental de la recta real;

b) verificar directamente que

$$
x\notin\operatorname{Acc}(A);
$$

c) explicar por qué $x$ no puede ser aislado en $A$;

d) identificar la hipótesis exacta que falta para convertir la afirmación falsa en la equivalencia correcta;

e) escribir esa equivalencia correcta.

[]{#MA-EX-ANM-01-004-028}

### 28. El aislamiento no se conserva al agrandar el conjunto

Refuta la afirmación

> Si $A\subseteq B$ y $x$ es aislado en $A$, entonces $x$ es aislado en $B$.

Usa

$$
A=\{0\},
\qquad
B=(-1,1).
$$

a) Demuestra que $0$ es aislado en $A$.

b) Demuestra que $0$ no es aislado en $B$.

c) Prueba además que

$$
0\in\operatorname{Acc}(B).
$$

d) Formula y demuestra la propiedad que sí es válida en la dirección opuesta:

> si $C\subseteq A$, $x\in C$ y $x$ es aislado en $A$, entonces $x$ es aislado en $C$.

e) Explica por qué añadir puntos cerca del centro puede destruir aislamiento, mientras que retirar puntos conservando el centro no puede hacerlo.

[]{#MA-EX-ANM-01-004-029}

### 29. Qué modificaciones puede ignorar un punto aislado

Sea $A\subseteq\mathbb R$ y supón que $x$ es aislado en $A$. Fija un radio $r_0>0$ tal que

$$
B(x,r_0)\cap A=\{x\}.
$$

a) Sea $C\subseteq\mathbb R$ un conjunto tal que

$$
C\cap B(x,r_0)=\varnothing.
$$

Demuestra que $x$ sigue siendo aislado en

$$
A\cup C.
$$

b) Sea $D\subseteq A\setminus\{x\}$. Demuestra que $x$ sigue siendo aislado en

$$
A\setminus D.
$$

c) Combina ambos apartados: si primero quitas puntos de $A$ distintos de $x$ y luego añades un conjunto completamente exterior a $B(x,r_0)$, demuestra que el mismo radio $r_0$ sigue certificando aislamiento.

d) Muestra que la condición del apartado a) no puede suprimirse. Usa

$$
A=\{0\},
\qquad
x=0,
\qquad
C=(0,1).
$$

e) Extrae una conclusión local: explica por qué el aislamiento depende únicamente de lo que ocurre en alguna ventana suficientemente pequeña alrededor de $x$, y no del comportamiento global del conjunto lejos del centro.

## §4.7. Abiertos y cerrados: de lo local a lo global

[]{#MA-EX-ANM-01-004-030}

### 30. Un radio por punto no es un radio para todos

Considera el intervalo

$$
A=(0,1).
$$

a) Demuestra directamente que

$$
\forall x\in A\ \exists r_x>0:
B(x,r_x)\subseteq A.
$$

b) Demuestra que es falsa la afirmación más fuerte

$$
\exists r>0\ \forall x\in A:
B(x,r)\subseteq A.
$$

Tu argumento debe comenzar con un radio arbitrario $r>0$ y construir un punto $x\in(0,1)$ para el cual ese radio no sirve.

c) Explica con palabras por qué intercambiar el orden de

$$
\forall x
\qquad\text{y}\qquad
\exists r_x
$$

cambia la afirmación matemática.

d) Da un ejemplo de conjunto para el cual la afirmación fuerte sí sea verdadera.

[]{#MA-EX-ANM-01-004-031}

### 31. Del margen local al complemento cerrado

Sea

$$
U=(-2,0)\cup(1,\infty)
$$

y define

$$
F=U^c.
$$

a) Escribe explícitamente $F$.

b) Demuestra que $U$ es abierto construyendo, para cada tipo de punto $x\in U$, un radio $r_x>0$ con

$$
B(x,r_x)\subseteq U.
$$

c) Usa únicamente la definición por complemento para concluir que $F$ es cerrado.

d) Reinterpreta la misma situación desde $F$: para cada $x\notin F$, exhibe una bola centrada en $x$ que no intersecte $F$.

e) Explica por qué los radios deben depender de $x$ y por qué una figura que dibuje sólo unas pocas ventanas no sustituye la condición

$$
\forall x\in U\ \exists r_x>0.
$$

[]{#MA-EX-ANM-01-004-032}

### 32. Interior e intersecciones: qué sobrevive para familias arbitrarias

Sea $\{A_i\}_{i\in I}$ una familia no vacía de subconjuntos de $\mathbb R$.

a) Demuestra que siempre

$$
\boxed{
\operatorname{int}\left(\bigcap_{i\in I}A_i\right)
\subseteq
\bigcap_{i\in I}\operatorname{int}(A_i).
}
$$

b) Demuestra que, si $I$ es finito, entonces la inclusión es una igualdad.

c) Muestra que para una familia arbitraria la igualdad puede fallar. Usa

$$
A_r=(-r,r),
\qquad
r>0.
$$

Calcula

$$
\operatorname{int}\left(\bigcap_{r>0}A_r\right)
$$

y

$$
\bigcap_{r>0}\operatorname{int}(A_r).
$$

d) Identifica exactamente qué paso de la demostración finita deja de estar disponible en la familia arbitraria.

[]{#MA-EX-ANM-01-004-033}

### 33. La frontera siempre es cerrada

Sea $A\subseteq\mathbb R$.

Demuestra que

$$
\boxed{
\partial A
\text{ es un conjunto cerrado.}
}
$$

Puedes usar los resultados ya demostrados:

$$
\partial A
=
\overline A\cap\overline{A^c},
$$

la idempotencia de la clausura y la caracterización

$$
F\text{ cerrado}
\iff
F=\overline F.
$$

Tu prueba debe dejar explícito:

a) por qué $\overline A$ es cerrado;

b) por qué $\overline{A^c}$ es cerrado;

c) por qué la intersección de esos dos conjuntos es cerrada.

Concluye explicando por qué este resultado no afirma que la frontera deba ser finita ni que deba estar contenida en $A$.

[]{#MA-EX-ANM-01-004-034}

### 34. El mínimo de infinitos radios puede desaparecer

Un estudiante intenta demostrar que una intersección arbitraria de abiertos es abierta:

> Sea $\{U_i\}_{i\in I}$ una familia de abiertos y sea
> $$
> x\in\bigcap_{i\in I}U_i.
> $$
> Para cada $i$ existe $r_i>0$ tal que
> $$
> B(x,r_i)\subseteq U_i.
> $$
> Tomamos
> $$
> r=\min_{i\in I}r_i>0.
> $$
> Entonces
> $$
> B(x,r)\subseteq\bigcap_{i\in I}U_i.
> $$
> Por tanto la intersección es abierta.

a) Identifica la afirmación no justificada.

b) Explica por qué el hecho de que cada $r_i$ sea positivo no garantiza un mínimo positivo para una familia arbitraria.

c) Usa la familia

$$
U_t=(-t,t),
\qquad
t>0,
$$

para mostrar concretamente el fallo.

d) Calcula

$$
\bigcap_{t>0}U_t
$$

y demuestra que ese conjunto no es abierto.

e) Repara el enunciado del estudiante sustituyendo «arbitraria» por la hipótesis exacta que sí permite la prueba con un mínimo de radios.

[]{#MA-EX-ANM-01-004-035}

### 35. Una unión arbitraria de cerrados puede dejar de ser cerrada

Para cada $r>0$, define

$$
F_r=[r,\infty).
$$

a) Demuestra que cada $F_r$ es cerrado.

b) Calcula exactamente

$$
\bigcup_{r>0}F_r.
$$

c) Demuestra que la unión obtenida no es cerrada.

d) Explica por qué esto no contradice el teorema de que las uniones **finitas** de cerrados son cerradas.

e) Pasa al complemento y explica cómo este mismo ejemplo refleja el fallo de estabilidad de los abiertos bajo intersecciones arbitrarias.

[]{#MA-EX-ANM-01-004-036}

### 36. Dos envolventes extremales de un conjunto

Sea $A\subseteq\mathbb R$.

a) Demuestra directamente que $\operatorname{int}(A)$ es abierto.

b) Demuestra que, si $G$ es abierto y

$$
G\subseteq A,
$$

entonces

$$
G\subseteq\operatorname{int}(A).
$$

Concluye que $\operatorname{int}(A)$ es el **mayor conjunto abierto contenido en $A$**.

c) Demuestra que $\overline A$ es cerrado.

d) Sea $F$ cerrado y supón

$$
A\subseteq F.
$$

Demuestra que

$$
\overline A\subseteq F.
$$

Concluye que $\overline A$ es el **menor conjunto cerrado que contiene a $A$**.

e) Organiza los dos resultados en un esquema dual:

$$
\operatorname{int}(A)
\subseteq
A
\subseteq
\overline A.
$$

Explica qué significa que las dos operaciones actúen como envolventes extremales desde lados opuestos.

f) Aplica el esquema a

$$
A=[0,1)
$$

y determina las dos envolventes.

## §4.8. Un diccionario local para leer conjuntos

[]{#MA-EX-ANM-01-004-037}

### 37. Reconstruir el diccionario desde tres decisiones

Sea $A\subseteq\mathbb R$ y fija $x\in\mathbb R$.

Sin consultar una tabla previa, reconstruye las seis nociones locales del capítulo a partir de estas tres decisiones:

1. cuantificador sobre el radio:
   $$
   \exists r>0
   \qquad\text{o}\qquad
   \forall r>0;
   $$
2. lado observado:
   $$
   A,\qquad A^c,\qquad\text{o ambos};
   $$
3. centro permitido o perforado.

Tu reconstrucción debe producir las condiciones para:

- interior;
- exterior;
- adherencia;
- frontera;
- acumulación;
- aislamiento.

Después demuestra las relaciones

$$
\operatorname{int}(A)\subseteq A\subseteq\overline A,
$$

$$
\operatorname{ext}(A)=\operatorname{int}(A^c),
$$

$$
\partial A=\overline A\cap\overline{A^c},
$$

y

$$
x\text{ aislado en }A
\iff
x\in A\setminus\operatorname{Acc}(A).
$$

Finalmente, explica cuál de las seis nociones no puede decidirse sólo con información sobre bolas completas porque exige perforar explícitamente el centro.

[]{#MA-EX-ANM-01-004-038}

### 38. Radiografía completa de un conjunto mixto

Sea

$$
A=(-2,-1]\cup
\left((0,1)\setminus\left\{\frac12\right\}\right)
\cup\{2\}.
$$

Determina exactamente:

$$
\operatorname{int}(A),
\qquad
\overline A,
\qquad
\partial A,
\qquad
\operatorname{Acc}(A),
$$

y el conjunto de puntos aislados de $A$.

Después determina:

1. $\operatorname{ext}(A)$;
2. si $A$ es abierto;
3. si $A$ es cerrado.

Tu solución debe usar las identidades del capítulo para reducir trabajo cuando sea legítimo, pero debe justificar directamente al menos:

- por qué $1/2$ pertenece a $\operatorname{Acc}(A)$;
- por qué $2$ es aislado;
- por qué $-1$ pertenece a la frontera aunque pertenezca a $A$.

[]{#MA-EX-ANM-01-004-039}

### 39. Cinco formas de reconocer que un conjunto es cerrado

Sea $A\subseteq\mathbb R$.

Demuestra la equivalencia entre las cinco afirmaciones siguientes:

1. $A$ es cerrado;
2. $A^c$ es abierto;
3. $A=\overline A$;
4. $\operatorname{Acc}(A)\subseteq A$;
5. $\partial A\subseteq A$.

No repitas cinco pruebas independientes. Organiza el argumento como una red eficiente de implicaciones, indicando qué resultados previos utilizas en cada paso.

Como parte de la prueba de $5\Rightarrow3$, puedes usar

$$
\overline A
=
\operatorname{int}(A)
\cup
\partial A,
$$

pero debes justificar esa identidad a partir de

$$
\partial A
=
\overline A\setminus\operatorname{int}(A)
$$

y

$$
\operatorname{int}(A)\subseteq A\subseteq\overline A.
$$

Al final, explica qué aporta la quinta caracterización respecto de las otras cuatro: ¿qué dice de los puntos donde toda ventana ve ambos lados?

[]{#MA-EX-ANM-01-004-040}

### 40. Reconstrucción inversa a partir de datos locales

Se sabe que un conjunto $A\subseteq\mathbb R$ satisface simultáneamente:

$$
\operatorname{int}(A)
=
(-3,-1)\cup(0,1),
$$

$$
\operatorname{Acc}(A)
=
[-3,-1]\cup[0,1],
$$

el conjunto de puntos aislados de $A$ es

$$
\{2\},
$$

y además

$$
-3\in A,
\qquad
-1\notin A,
\qquad
0\notin A,
\qquad
1\notin A.
$$

a) Reconstruye $A$.

b) Demuestra que tu respuesta satisface todos los datos dados.

c) Calcula después

$$
\overline A,
\qquad
\partial A,
\qquad
\operatorname{ext}(A).
$$

d) Decide si $A$ es abierto o cerrado.

e) Demuestra que los datos determinan $A$ de manera única.

La prueba de unicidad debe usar la descomposición

$$
A
=
\bigl(A\cap\operatorname{Acc}(A)\bigr)
\,\dot\cup\,
\{\text{puntos aislados de }A\}
$$

y no una mera inspección de la respuesta propuesta.
