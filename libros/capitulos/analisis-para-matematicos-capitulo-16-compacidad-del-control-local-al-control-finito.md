---
content-id: MA-BCH-0266
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-016
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: 'Capítulo 16 — Compacidad: del control local al control finito'
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C16.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-16)

Si una función continua nunca se anula, cada punto dispone de una vecindad donde sus valores permanecen separados de cero. Esos márgenes locales pueden reducirse al variar el punto y no dar una barrera positiva común. En un dominio compacto no vacío, la función alcanzará un mínimo positivo de su magnitud. El recurso que permite obtener esa conclusión consiste en reducir cualquier cubierta abierta dada a una subfamilia finita que todavía cubra todo el dominio.

La prueba comenzará con segmentos y el supremo de C00, usando los abiertos de C04 sin recurrir a una equivalencia secuencial. Heine–Borel permitirá después reconocer los compactos reales por cerradura y acotación. La extracción de sucesiones dadas de C08 y la continuidad de C14, con las herramientas de C06 y C12, tendrán funciones distintas en las consecuencias. La recíproca secuencial general mantendrá explícita CC(R), o una enumeración sobreyectiva dada cuando esté disponible; no se utilizarán continuidad uniforme ni derivadas.

## 16.1. Una cubierta dada y una reducción finita

[]{#MA-SEC-ANM-01-016-001}

En una cubierta, cada punto está en algún abierto de la familia. La dificultad es conservar esa cobertura de todos los puntos usando sólo finitos miembros originales. Para un conjunto fijo podemos encontrar una cubierta finita cómoda, pero la compacidad debe responder también a cualquier otra cubierta que se nos entregue.

**Definición.** Una cubierta abierta de $K\subseteq\mathbb R$ es una familia dada $U:I\to\mathcal P(\mathbb R)$, cuyos miembros $U_i$ son abiertos reales, tal que

$$K\subseteq\bigcup_{i\in I}U_i.$$

La inclusión significa $\forall x\in K\;\exists i\in I:\;x\in U_i$. Para un punto fijado podemos usar un índice que lo cubra, sin disponer por ello de una función que seleccione índices simultáneamente para todos los puntos. Una **subcubierta finita** restringe la misma familia a un conjunto finito $J\subseteq I$ y conserva cobertura de todo $K$. Sus abiertos deben proceder de la cubierta recibida; no se sustituyen por nuevos abiertos. También puede haber índices distintos asociados al mismo abierto.

**Compacidad.** $K$ es compacto si **toda** cubierta abierta dada de $K$ admite una subcubierta finita. Primero se recibe la familia arbitraria, después se obtiene un conjunto finito de sus índices y con ellos se debe cubrir cada punto. La familia $\{\mathbb R\}$ cubre finitamente cualquier conjunto real, pero eso sólo verifica una elección particular de cubierta. Para negar compacidad basta, en cambio, una cubierta concreta que ninguna subfamilia finita consiga reducir.

![Los abiertos U1=(−1/4,2/5), U2=(3/10,4/5), U3=(7/10,5/4) y U4=(1/5,3/5) cubren \[0,1\]. J={1,2,3} basta, incluidos los extremos. Esta verificación particular no demuestra por sí sola compacidad; la definición cuantifica sobre toda cubierta.](../../assets/books/anm/C16/C16-F01.svg){#fig-anm-c16-f01 fig-alt="Cuatro ventanas abiertas sobre un segmento cerrado. Las primeras tres se solapan y protegen los extremos cero y uno; la cuarta puede descartarse."}

**R1. Casos finitos y una primera fuga.** El vacío es compacto: de cualquier cubierta tomamos $J=\varnothing$, cuya unión cubre el vacío. Para un singleton $\{a\}$, la cobertura proporciona un índice $i$ con $a\in U_i$; $J=\{i\}$ basta. Una unión de dos compactos es compacta: una cubierta de la unión cubre por separado ambas piezas, que entregan conjuntos finitos $J_1,J_2$; la unión finita $J_1\cup J_2$ cubre todo. Inducción finita da compacidad de conjuntos finitos y de uniones finitas de compactos. No se está escogiendo una subcubierta por cada miembro de una familia infinita.

La recta admite una cubierta sin reducción finita. Los abiertos $U_n=(-(n+1),n+1)$, para $n\in\mathbb N$, cubren cada real por arquimedianidad. Si $J\subseteq\mathbb N$ es finito y no vacío, tiene máximo $m$, y cada $U_j$ seleccionado está contenido en $U_m$. El punto $m+2$ queda fuera de toda la unión seleccionada. La subfamilia vacía tampoco cubre la recta, así que hemos descartado todos los conjuntos finitos de índices para esta cubierta.

Un conjunto finito no vacío de reales tiene mínimo y máximo: basta recorrer una lista finita y conservar en cada comparación el menor y el mayor encontrados. El mínimo es uno de los valores de la lista, de modo que si todos son positivos, también lo es él. Para los infinitos radios $1/(n+1)$, cualquier candidato positivo deja de ser cota inferior al encontrar un recíproco menor; su ínfimo es cero. La reducción a finitos controles será la que permita conservar un margen positivo al reunirlos.

### Ejercicios de la sección 16.1

[]{#ejercicios-16}

#### Ejercicio 1. Una sola cubierta no basta

[]{#MA-EX-ANM-01-016-001}

Un argumento afirma que todo subconjunto real es compacto porque $\{\mathbb R\}$ es una cubierta finita. Explica el cambio ilegítimo de cuantificadores y refútalo con una cubierta de $\mathbb R$.

[]{#MA-SOL-ANM-01-016-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Compacidad exige que para toda cubierta abierta dada exista una subcubierta finita de esa misma familia. El argumento sólo presenta una cubierta conveniente. Para $\mathbb R$, la familia $U_n=(-(n+1),n+1)$ cubre por arquimedianidad. Toda lista finita no vacía de índices tiene máximo $m$ y su unión está en $U_m$, que no contiene $m+2$. La subfamilia vacía tampoco cubre la recta. Por tanto hay una cubierta sin ninguna subcubierta finita y la recta no es compacta.

La afirmación inválida sustituye «para toda cubierta» por «existe alguna cubierta». La familia creciente es una cubierta abierta concreta que refuta la afirmación universal para la recta. El máximo sólo se toma tras fijar una subfamilia finita no vacía. Tratar también la vacía completa la refutación de todas las reducciones posibles.

</details>

#### Ejercicio 2. Subcubierta concreta

[]{#MA-EX-ANM-01-016-002}

Considera $K=[0,1]$ y los abiertos $U_1=(-1/4,2/5)$, $U_2=(3/10,4/5)$, $U_3=(7/10,5/4)$, $U_4=(1/5,3/5)$. Identifica una subcubierta de tres miembros y muestra que quitar cualquiera de esos tres deja algún punto sin cubrir dentro de esa subfamilia.

[]{#MA-SOL-ANM-01-016-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Los índices $J=\{1,2,3\}$ sirven: $U_1$ cubre desde cero hasta antes de $2/5$, $U_2$ solapa desde $3/10$ y cubre hasta antes de $4/5$, y $U_3$ solapa desde $7/10$ y alcanza uno. Su unión contiene $[0,1]$. Al quitar $U_1$, cero queda fuera; al quitar $U_3$, uno queda fuera; al quitar $U_2$, $1/2$ no está en $U_1$ ni $U_3$. Es una subcubierta concreta, y su irredundancia dentro de esos tres no prueba por sí sola compacidad de $K$, que debe valer para cualquier cubierta.

**Retorno visual.** Véase [C16-F01](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las desigualdades $3/10<2/5$ y $7/10<4/5$ verifican los solapes, evitando huecos entre los tres abiertos. Los testigos cero, uno y medio muestran irredundancia respecto de esa lista elegida. Al retirar un miembro no se reincorpora $U_4$, pues la pregunta examina esa subfamilia de tres. Nada de ello sustituye la comprobación para cubiertas arbitrarias que exige compacidad.

</details>

#### Ejercicio 3. Uniones finitas desde la definición

[]{#MA-EX-ANM-01-016-003}

Prueba desde cubiertas que una unión finita de compactos reales es compacta, incluyendo la unión vacía. No invoques Heine–Borel.

[]{#MA-SOL-ANM-01-016-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

El vacío es compacto porque dentro de cualquier cubierta sirve la subfamilia vacía. Para dos compactos, una cubierta de la unión cubre cada uno; existen conjuntos finitos de índices $J_1,J_2$ que cubren las piezas. Su unión finita cubre la unión de las piezas. Por inducción sobre una lista finita de compactos, partiendo de la unión vacía y añadiendo una pieza por paso, se obtiene el resultado. Sólo se combinan testigos finitos de la cubierta fijada; no se escogen subcubiertas de infinitos compactos.

Para una cubierta fijada de la unión, sus miembros cubren cada compacto de la lista. La inducción combina una reducción de la unión anterior con una de la pieza añadida, manteniendo índices de esa cubierta. La finitud de las piezas asegura que el proceso termina con una lista finita. Una familia infinita podría requerir añadir índices indefinidamente y no cumple este argumento.

</details>

#### Ejercicio 4. El mínimo positivo tiene una hipótesis

[]{#MA-EX-ANM-01-016-004}

Demuestra que una familia finita no vacía de radios positivos tiene mínimo positivo. Refuta la conclusión análoga para una familia infinita.

[]{#MA-SOL-ANM-01-016-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Una lista finita no vacía $r_1,\ldots,r_k$ admite un mínimo: empezamos por $r_1$ y comparamos sucesivamente con el siguiente valor, conservando el menor. El resultado es uno de los $r_j$, luego es positivo. Para $r_n=1/(n+1)$, todos los radios son positivos y cero es cota inferior. Para cualquier $c>0$, arquimedianidad da $n$ con $1/(n+1)<c$, así ninguna cota inferior positiva es posible. El ínfimo es cero y no hay un radio positivo que sea menor o igual que todos.

La construcción del mínimo finito termina tras comparar todos los valores y devuelve uno de ellos. Por ello no sólo obtiene una cota, sino un valor positivo de la lista. En la familia infinita, cualquier barrera positiva deja de ser cota inferior al elegir un recíproco más pequeño. El paso finito que conserva una escala positiva no puede reemplazarse por un ínfimo sin comprobar su positividad.

</details>

#### Ejercicio 5. Una unión infinita que escapa

[]{#MA-EX-ANM-01-016-005}

Sabiendo que cada segmento $[-n,n]$ será compacto por R2, explica por qué la unión de esos segmentos para $n\in\mathbb N$ refuta que toda unión de compactos sea compacta. Exhibe la cubierta responsable.

[]{#MA-SOL-ANM-01-016-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Por arquimedianidad cada real está en algún $[-n,n]$, así la unión es $\mathbb R$. R2 prueba compacidad de cada segmento, incluido $n=0$. Pero la cubierta $U_n=(-(n+1),n+1)$ de la recta no tiene reducción finita: si $m$ es máximo de los índices seleccionados, $m+2$ queda fuera. La conclusión de unión finita no se extiende a uniones infinitas; las reducciones entregadas por cada pieza no se convierten automáticamente en una sola lista finita.

Cada real tiene magnitud menor o igual que algún natural y por eso pertenece a uno de los segmentos. Esta identidad de la unión sitúa el ejemplo exactamente en la recta, cuyo fallo de compacidad ya se muestra por una cubierta. No basta que cada pieza individual admita reducciones: sus listas pueden crecer sin una cota finita común al recorrer todas las piezas.

</details>

## 16.2. El supremo prolonga los segmentos cubiertos

[]{#MA-SEC-ANM-01-016-002}

**R2. Todo segmento $[a,b]$, con $a\le b$, es compacto.** No partiremos de Heine–Borel: debemos producir una reducción finita para una cubierta arbitraria. Fijamos $U:I\to\mathcal P(\mathbb R)$ que cubre $[a,b]$, y registramos hasta dónde hay cobertura finita:

$$S=\{x\in[a,b]:[a,x]\text{ admite una subcubierta finita de }U\}.$$

Pertenecer a $S$ significa que existe alguna reducción finita para ese segmento; no se ha definido una asignación $x\mapsto J_x$. Un abierto que contiene $a$ cubre $[a,a]$, así que $a\in S$. Además $S\subseteq[a,b]$ está acotado por $b$. La completitud de C00 proporciona $c=\sup S$, y las dos propiedades $a\in S$ y $b$ cota dan $a\le c\le b$. Podemos aplicar la cubierta a $c$ aunque todavía no sepamos que pertenece a $S$.

Fijemos un índice $i_c$ con $c\in U_{i_c}$. Su apertura da $r>0$ con $(c-r,c+r)\subseteq U_{i_c}$. Para aprovechar ese margen buscamos un segmento ya cubierto que llegue cerca de $c$. Como $c-r/2<c$ no es cota superior de $S$, existe $t\in S$ con $c-r/2<t\le c$. Este testigo puede ser el propio $c$ si pertenece a $S$; la prueba no necesita que la distancia sea positiva.

Para ese único $t$, la definición de $S$ entrega una subcubierta finita $J_t$ de $[a,t]$. Prolongamos hasta

$$d=\min(b,c+r/2).$$

La fórmula garantiza $c\le d\le b$, y para cualquier $z\in[t,d]$ tenemos $z\ge t>c-r/2>c-r$ y $z\le d\le c+r/2<c+r$. Por tanto el abierto $U_{i_c}$ contiene todo el tramo $[t,d]$. Los índices $J_t\cup\{i_c\}$ siguen siendo finitos y pertenecen a la familia original: cubren $[a,t]$ con la reducción anterior y $[t,d]$ con el nuevo abierto. Como ambos tramos forman $[a,d]$, obtenemos $d\in S$.

![Esquema del caso hipotético c<b. Con c−r/2<t≤c y d=min(b,c+r/2), el conjunto Jt más el índice que cubre c cubre \[a,d\]. Por tanto d∈S; si c<b, d>c contradice la cota. Cuando c=b, la misma construcción da d=b∈S. Las posiciones son ilustrativas.](../../assets/books/anm/C16/C16-F02.svg){#fig-anm-c16-f02 fig-alt="Segmento previamente cubierto hasta t y prolongación roja hasta d dentro del abierto que contiene c. Se distinguen c, d y el extremo final b."}

Si $c<b$, tanto $b$ como $c+r/2$ son mayores que $c$, y su mínimo $d$ también lo es. Esto contradice que $c$ acote a $S$, pues acabamos de probar $d\in S$. Luego $c=b$. La construcción conserva además la pertenencia de $d$: al sustituir $c=b$ resulta $d=b\in S$, cuya definición proporciona una subcubierta finita de todo $[a,b]$.

La igualdad $\sup S=b$ no habría bastado para terminar: cuando $a<b$, el conjunto $[a,b)$ tiene ese supremo y no lo contiene. La apertura en torno al extremo es lo que ha permitido probar pertenencia, además de identificar la cota. Para $a=b$ basta el abierto que cubre el único punto, aunque el argumento también lo incluye; con la convención $[a,b]=\varnothing$ si $a>b$, sirve directamente la subfamilia vacía.

Los testigos utilizados fueron un índice para $a$, otro para $c$, un radio de este último abierto y un punto aproximante $t$ con una reducción finita de su segmento. No se necesitó elegir un abierto por cada punto ni una reducción por cada miembro de $S$. La prolongación de un único segmento cercano a la frontera resolvió la cobertura completa.

### Ejercicios de la sección 16.2

#### Ejercicio 6. Registrar cobertura finita

[]{#MA-EX-ANM-01-016-006}

Para una cubierta arbitraria de $[a,b]$, $a\le b$, define $S$ como en R2 y justifica $a\in S$, existencia de su supremo y pertenencia del supremo al segmento.

[]{#MA-SOL-ANM-01-016-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

La cobertura da un índice con $a\in U_i$, y ese único miembro cubre $[a,a]$. Por tanto $a\in S$ y $S$ no es vacío. Como $S\subseteq[a,b]$, $b$ es cota superior. Completitud da $c=\sup S$; $a\le c$ porque $a\in S$ y $c\le b$ porque $b$ es cota. Así $c\in[a,b]$ y puede aplicarse la cobertura a ese punto. No se supone que $c\in S$.

La definición de $S$ usa existencia de una lista finita para cada segmento registrado. El primer testigo sólo se necesita para $a$, y permite demostrar no vacuidad. La localización del supremo usa simultáneamente que $a$ es miembro y que $b$ es cota. Quedar en el segmento habilita aplicar la cubierta a $c$, antes de saber si pertenece a $S$.

</details>

#### Ejercicio 7. Prolongar con un solo abierto

[]{#MA-EX-ANM-01-016-007}

Si $c=\sup S$, $(c-r,c+r)\subseteq U_{i_c}$ y $t\in S$ satisface $c-r/2<t\le c$, prueba que $d=\min(b,c+r/2)$ pertenece a $S$. Identifica qué índices cubren cada tramo.

[]{#MA-SOL-ANM-01-016-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

$c\le d\le b$ y $t\le c$, así $a\le t\le d\le b$. Para $z\in[t,d]$, $z\ge t>c-r/2>c-r$ y $z\le d\le c+r/2<c+r$, luego $z\in U_{i_c}$. Por $t\in S$ hay un conjunto finito $J_t$ que cubre $[a,t]$. La unión $J_t\cup\{i_c\}$ es finita y cubre $[a,t]\cup[t,d]=[a,d]$. Esto es exactamente la propiedad que define $d\in S$. Sólo se fijó una subcubierta asociada al $t$ concreto.

La estimación se realiza para cada punto $z$ del tramo nuevo, no únicamente para $d$. Así el mismo abierto $U_{i_c}$ cubre todo lo que falta después de $t$. La lista $J_t$ existe por la pertenencia del $t$ concreto a $S$. Unirla con el índice del abierto central produce una lista finita original y acredita el predicado que define $d\in S$.

</details>

#### Ejercicio 8. El extremo omitido de una prueba

[]{#MA-EX-ANM-01-016-008}

Una prueba concluye $\sup S=b$ y afirma «por tanto $b\in S$». Refuta ese paso lógico y completa el argumento correcto de R2 para obtener la subcubierta de todo el segmento.

[]{#MA-SOL-ANM-01-016-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Con $a<b$, $S=[a,b)$ tiene supremo $b$ y no lo contiene; la igualdad de supremo no implica pertenencia. En R2 se construye además $d=\min(b,c+r/2)\in S$, usando una cobertura de $[a,t]$ y un abierto que contiene a $c$. Si $c<b$, ese $d$ sería mayor que $c$, contradicción con la cota. Luego $c=b$, y la misma fórmula da $d=b$. Como ya se probó $d\in S$, ahora sí $b\in S$. Su definición suministra los índices finitos que cubren $[a,b]$.

**Retorno visual.** Véase [C16-F02](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Si $c<b$, tanto $b$ como $c+r/2$ son mayores que $c$, así su mínimo también lo es. Ese $d\in S$ contradiría que $c$ domina a $S$. Una vez excluido ese caso, se conserva la construcción ya verificada y se obtiene $d=b\in S$. La prueba de pertenencia es indispensable: completitud sola no convierte cualquier supremo en máximo.

</details>

#### Ejercicio 9. No elegir una subcubierta por segmento

[]{#MA-EX-ANM-01-016-009}

Explica por qué definir $S$ mediante «existe una subcubierta finita de $[a,x]$» no obliga a construir una función $x\mapsto J_x$. Enumera los testigos concretos necesarios en R2.

[]{#MA-SOL-ANM-01-016-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

El predicado existencial determina qué puntos están en $S$ sin asociarles un testigo elegido. Primero se usa un índice que cubre $a$ para probar $a\in S$. Después se fija un índice $i_c$ que cubre el supremo, un radio de apertura y un único $t\in S$ próximo al supremo. Sólo para ese $t$ se instancia la existencia de $J_t$. La lista finita $J_t\cup\{i_c\}$ concluye la prueba. No se forma una familia de elecciones sobre todos los $x\in S$.

Definir un conjunto mediante una existencia sólo decide qué elementos cumplen el predicado. Para la prolongación se fija un único punto aproximante y se instancia la existencia de su lista finita. El índice que cubre $c$ y su radio de apertura también se usan sólo en ese paso. No hay una asignación simultánea de subcubiertas o radios sobre todos los segmentos posibles.

</details>

#### Ejercicio 10. Cobertura del intervalo abierto frente al cerrado

[]{#MA-EX-ANM-01-016-010}

¿Puede la familia $U_n=(1/(n+2),2)$ cubrir $[0,1]$? Compara con su acción sobre $(0,1)$ y explica por qué no contradice R2.

[]{#MA-SOL-ANM-01-016-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

No cubre $[0,1]$ porque ningún miembro contiene cero. Sí cubre $(0,1)$: dado un punto positivo, algún recíproco $1/(n+2)$ es menor que él. Para una subfamilia finita no vacía con máximo índice $m$, $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de su unión $U_m$. Por eso el intervalo abierto no es compacto. R2 cuantifica sobre cubiertas que realmente cubren todo el segmento cerrado; esta familia no satisface esa premisa.

La ausencia de cero de todos los abiertos invalida cobertura del segmento cerrado, aunque cubran cada punto positivo. Para el intervalo abierto, el testigo fuera de cualquier reducción finita muestra un fallo real de compacidad. R2 se aplica a familias que cubren también los extremos del segmento. La misma familia puede ser una cubierta de un subconjunto y no serlo del conjunto mayor.

</details>

## 16.3. Heredar compacidad sin perder índices

[]{#MA-SEC-ANM-01-016-003}

Estar dentro de un compacto no garantiza heredar su compacidad: un subconjunto puede omitir una frontera a la que se acercan sus puntos. La cerradura relativa permitirá ampliar cualquier cubierta de ese subconjunto a una del compacto y después recuperar índices de la cubierta original.

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Para cada $x\in K$, si $x\in F$, entonces $x\in A$ y lo cubre algún $U_i$; si $x\notin F$, lo cubre $V$. La familia ampliada cubre así $K$. Para distinguir la procedencia de sus miembros usamos los índices $(i,0)$ para los antiguos y el índice $(\varnothing,1)$ para el añadido. Sus valores son respectivamente $U_i$ y $V$, y las etiquetas diferentes impiden colisiones aunque coincidan algunos abiertos como conjuntos. La compacidad de $K$ entrega un conjunto finito de estos índices ampliados.

Retenemos los índices de la forma $(i,0)$ y los proyectamos a sus $i$ originales, obteniendo un conjunto finito $J\subseteq I$. Si $x\in A$, entonces $x\in F$ y $x\notin V$: el índice excepcional no puede cubrirlo. Alguno de los originales seleccionados debe hacerlo, por lo que $J$ cubre todo $A$. Como la cubierta de $A$ era arbitraria, queda probada su compacidad.

El abierto añadido cubre todo $K\setminus A$. Un recorte cerca de un extremo de un segmento ambiente podría dejar parte de ese complemento sin cubrir e impedir la aplicación de compacidad. Al volver a la cubierta original se retira un índice etiquetado concreto, no todos los índices que tengan un mismo abierto como valor.

En particular, si $F$ es cerrado real y $K$ es compacto, $K\cap F$ es compacto. Para $K=[-2,2]$ y $F=(-\infty,-1]\cup[1,\infty)$ obtenemos $[-2,-1]\cup[1,2]$. En la prueba de herencia, el abierto añadido es $(-1,1)$ y cubre la zona central que falta. El argumento no necesita que el cerrado relativo sea un intervalo.

Para ver qué puede fallar sin cerradura relativa, consideremos $(0,1)\subseteq[0,1]$ y la familia

$$U_n=(1/(n+2),2),\qquad n\in\mathbb N.$$

Cada $x\in(0,1)$ supera algún $1/(n+2)$ por arquimedianidad, así que la familia cubre ese dominio. Los abiertos crecen con el índice. Para una subfamilia finita no vacía, su máximo índice $m$ da unión exactamente $U_m$, y el punto $1/(2(m+2))$ pertenece a $(0,1)$ pero queda por debajo del extremo izquierdo de $U_m$. No está cubierto. La subfamilia vacía tampoco cubre el intervalo. Este subconjunto no es compacto; la misma familia ni siquiera cubre el segmento cerrado, porque ninguno de sus abiertos contiene cero.

![Un=(1/(n+2),2), n≥0, cubre (0,1). Toda subfamilia finita no vacía tiene máximo m y omite x=1/\[2(m+2)\]. Arriba se ilustra m=3; abajo el acercamiento de umbrales a cero es esquemático. El caso de subfamilia vacía se descarta por no vacuidad de K.](../../assets/books/anm/C16/C16-F03.svg){#fig-anm-c16-f03 fig-alt="Un segmento con ambos extremos abiertos y un punto omitido por una ventana de índice máximo. Otra fila indica ventanas que se acercan a cero sin alcanzarlo."}

### Ejercicios de la sección 16.3

#### Ejercicio 11. Cubrir el complemento completo

[]{#MA-EX-ANM-01-016-011}

Para heredar compacidad de $A=K\cap F$, una prueba añade sólo $V=(M-1,M+1)\cap(\mathbb R\setminus F)$ cuando $K=[-M,M]$. Muestra con $M=2$, $F=\{0\}$ y una cubierta de $A$ que la familia ampliada puede no cubrir $K$. Repara el abierto añadido.

[]{#MA-SOL-ANM-01-016-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Aquí $A=\{0\}$. La familia con un solo miembro $U=(-1/4,1/4)$ cubre $A$, y el abierto propuesto es $(1,3)$. La unión de ambos no contiene, por ejemplo, $-1\in K$. No cubre $K$, así no puede aplicarse compacidad del segmento. La reparación es añadir todo $V=\mathbb R\setminus F$. Si un punto de $K$ no está en $F$, lo cubre $V$; si está en $F$, pertenece a $A$ y lo cubre la familia original. $V$ no toca $A$, por lo que sus índices se pueden retirar después de obtener una subcubierta finita ampliada.

La familia original elegida sólo necesita cubrir cero y por eso puede ser muy pequeña. El recorte del complemento añadido no alcanza la zona negativa de $K$, que tampoco cubre ese original. La reparación con el complemento entero verifica cobertura por los dos casos de pertenencia a $F$. Su disjunción con $A$ garantiza que después pueda retirarse el índice excepcional sin perder cobertura de $A$.

</details>

#### Ejercicio 12. Cerrar dos piezas dentro de un segmento

[]{#MA-EX-ANM-01-016-012}

Prueba compacidad de $A=[-2,-1]\cup[1,2]$ como cerrado relativo de $K=[-2,2]$, sin usar todavía Heine–Borel. Describe el abierto añadido en la prueba de herencia.

[]{#MA-SOL-ANM-01-016-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

$K$ es compacto por R2. Tomamos $F=(-\infty,-1]\cup[1,\infty)$, cerrado real porque su complemento $(-1,1)$ es abierto. Entonces $A=K\cap F$. R3 da compacidad. Para una cubierta de $A$, se añade $\mathbb R\setminus F=(-1,1)$, que cubre precisamente la zona de $K$ no cubierta por pertenencia a $A$; después una subcubierta finita de $K$ conserva suficientes índices originales para cubrir $A$, pues el abierto añadido no toca sus puntos.

El cerrado real $F$ conserva exactamente las dos piezas al recortar por $K$. El abierto añadido cubre el hueco central de ese segmento, mientras una cubierta dada de $A$ cubre sus otras entradas. La reducción finita ampliada puede usar ese abierto, pero ningún punto de $A$ depende de él. Esto permite volver a índices originales y demostrar herencia sin adelantar Heine–Borel.

</details>

#### Ejercicio 13. Etiquetas y abiertos repetidos

[]{#MA-EX-ANM-01-016-013}

Desarrolla el sistema de índices al añadir un abierto $V$ a una cubierta $(U_i)_{i\in I}$ y al retirar ese miembro tras aplicar compacidad. Permite que $V$ coincida como conjunto con algún $U_i$.

[]{#MA-SOL-ANM-01-016-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Usamos $I^*=(I\times\{0\})\cup\{(\varnothing,1)\}$ y definimos $W_{(i,0)}=U_i$, $W_{(\varnothing,1)}=V$. Las etiquetas $0\ne1$ garantizan índice excepcional distinto. Una subcubierta finita $J^*$ determina $J=\{i\in I:(i,0)\in J^*\}$, finito por proyección de una parte finita. Para $x\in A$ con $A\cap V=\varnothing$, un índice que lo cubre no es el excepcional; proviene de $J$ y $x\in U_i$. La coincidencia de valores abiertos no cambia la prueba: se retiran sólo índices etiquetados, no todos los miembros de igual valor.

Las etiquetas distinguen posiciones en la familia aunque sus valores como conjuntos sean iguales. El conjunto de índices originales conservados es la proyección de una parte de la lista finita ampliada y sigue siendo finito. Para cada entrada de $A$, el índice excepcional queda descartado por disjunción de su abierto con $A$. Se elimina ese índice concreto, conservando los originales que tengan el mismo valor si los hubiera.

</details>

#### Ejercicio 14. Un subconjunto que pierde compacidad

[]{#MA-EX-ANM-01-016-014}

Prueba mediante una cubierta que $(0,1)$ no es compacto, aunque esté dentro del compacto $[0,1]$. Trata las subfamilias vacías y no vacías.

[]{#MA-SOL-ANM-01-016-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

La cubierta $U_n=(1/(n+2),2)$ cubre $(0,1)$ por arquimedianidad. La subfamilia vacía no cubre su punto $1/2$. Si $J\subseteq\mathbb N$ es finito no vacío, su máximo $m$ da unión $U_m$, pues los miembros son crecientes. El punto $x=1/(2(m+2))$ es positivo y menor que uno pero está por debajo de $1/(m+2)$, luego no pertenece a ningún abierto seleccionado. No existe subcubierta finita. La hipótesis de cerrado relativo de R3 no puede omitirse.

**Retorno visual.** Véase [C16-F03](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La familia crece porque sus extremos izquierdos disminuyen al aumentar el índice. De ahí que cualquier reducción no vacía tenga unión exactamente igual al abierto de mayor índice. El testigo construido está en el dominio pero por debajo de ese extremo izquierdo. La inclusión en $[0,1]$ se mantiene verdadera; lo que falta para heredar compacidad es ser cerrado relativo allí.

</details>

#### Ejercicio 15. Intersección con un cerrado

[]{#MA-EX-ANM-01-016-015}

Prueba que $K\cap F$ es compacto cuando $K$ lo es y $F$ es cerrado real. Deduce que la intersección de toda familia no vacía de compactos reales es compacta, una vez disponible R4. Separa el caso de familia vacía.

[]{#MA-SOL-ANM-01-016-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

La intersección $K\cap F$ es cerrada relativa a $K$, y R3 la hace compacta. Para una familia de compactos con al menos un miembro, R4 hace a todos cerrados reales. Su intersección $A$ es cerrada, porque su complemento es unión de complementos abiertos, y está contenida en un miembro fijo $K_0$. Es $K_0\cap A$, por tanto compacta por la primera afirmación; esto vale incluso si el conjunto resultante es vacío. Para una familia sin miembros, la intersección ambiental es $\mathbb R$, que no es compacta. La no vacuidad requerida es la de la familia de índices, no la del conjunto intersección.

Después de Heine–Borel, cada miembro compacto es cerrado real, y una intersección arbitraria de cerrados sigue siendo cerrada. Fijar un único miembro de la familia no vacía aporta un ambiente compacto que contiene toda la intersección. No se requiere que haya una entrada común ni seleccionar un miembro por cada índice. La familia vacía no ofrece ese ambiente y su intersección convencional es la recta no compacta.

</details>

## 16.4. Heine–Borel: cerrar las dos direcciones

[]{#MA-SEC-ANM-01-016-004}

**R4. En la recta real, compacto equivale a cerrado y acotado.** Probaremos las dos necesidades desde cubiertas y la suficiencia desde R2/R3. No intervienen sucesiones ni una equivalencia secuencial anticipada.

Para probar acotación, supongamos primero $K\ne\varnothing$. La cubierta $U_n=(-(n+1),n+1)$ de la recta cubre también $K$, y la compacidad proporciona un conjunto finito de índices $J$. No puede ser vacío porque cubre un punto de $K$. Su máximo $m$ domina a los índices seleccionados y da $K\subseteq U_m\subseteq[-(m+1),m+1]$. Sólo después de la reducción finita hemos tomado ese máximo. El conjunto vacío se acota directamente, por ejemplo con cero.

Para demostrar cerradura, fijemos $p\notin K$ y supongamos $K\ne\varnothing$. Definimos los abiertos

$$V_n=\{x\in\mathbb R:|x-p|>1/(n+1)\},\qquad n\in\mathbb N,$$

Cada $V_n$ es la unión de los rayos $(-\infty,p-1/(n+1))$ y $(p+1/(n+1),\infty)$. Cubren $K$ porque, fijado $x\in K$, la distancia $|x-p|>0$ supera algún recíproco. La compacidad da una subcubierta finita no vacía y su máximo índice $m$ domina a los demás, ya que los $V_n$ aumentan. Así $K\subseteq V_m$, y la bola de $p$ de radio $1/(m+1)>0$ es disjunta de $K$. Cada punto exterior dispone de una bola dentro del complemento, que es por tanto abierto. El vacío también es cerrado, pues su complemento es toda la recta.

Para la suficiencia, si $K$ es cerrado y acotado, tomamos $M>0$ con $K\subseteq[-M,M]$. El segmento es compacto por R2 y $K=[-M,M]\cap K$ es cerrado relativo en él. R3 da compacidad de $K$, incluido el caso vacío. Las dos condiciones geométricas se han utilizado por separado: la acotación da el ambiente compacto y la cerradura permite heredar su propiedad.

![Heine–Borel real exige cerradura y acotación. El segmento cerrado cumple ambas; (0,1\] pierde cerradura y R pierde acotación. La unión de los dos segmentos cumple ambas aunque tiene un hueco. Las pruebas generales preceden a la clasificación.](../../assets/books/anm/C16/C16-F04.svg){#fig-anm-c16-f04 fig-alt="Cuatro dominios muestran extremos incluidos, un extremo omitido, una recta ilimitada y dos segmentos cerrados separados."}

Heine–Borel caracteriza mediante cerradura y acotación la propiedad de cubiertas definida al principio. Las pruebas anteriores han usado el orden completo y las bolas de la recta; el resultado no se está afirmando para espacios arbitrarios ni se ha obtenido de una recíproca secuencial.

La acotación sin cerradura falla en $(0,1)$ y la cerradura sin acotación falla en $\mathbb R$. También son distintas compacidad y conexidad: $[-2,-1]\cup[1,2]$ es cerrado y acotado, pero el corte cero lo separa; $(0,1)$ es un intervalo conexo por C15 y no es compacto. El conjunto

$$K=\{0\}\cup\{1/(n+1):n\in\mathbb N\}$$

es otro compacto. Está contenido en $[0,1]$; para demostrar su cerradura fijamos un punto exterior $p$. Si $p<0$ o $p>1$, la mitad de su distancia al segmento da una bola que evita $K$. En otro caso $0<p<1$, pues cero y uno pertenecen al conjunto. Elegimos $N\ge1$ con $1/(N+1)<p/2$. Toda la cola de recíprocos queda por debajo de $p/2$ y dista de $p$ más que $p/2$; cero dista $p$. Las distancias de $p$ a los términos del prefijo $n<N$ son finitas en número y positivas. La mitad del mínimo de esas distancias y de $p/2$ da un radio que evita prefijo, cola y cero. El complemento es abierto y Heine–Borel prueba compacidad. Quitar cero destruye cerradura, porque cada bola suya contiene un recíproco, y con ella destruye compacidad.

### Ejercicios de la sección 16.4

#### Ejercicio 16. Acotación desde una cubierta creciente

[]{#MA-EX-ANM-01-016-016}

Prueba que todo compacto real es acotado usando sólo la cubierta $U_n=(-(n+1),n+1)$. Incluye el vacío.

[]{#MA-SOL-ANM-01-016-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

El vacío está en $[0,0]$. Para $K\ne\varnothing$, la familia cubre toda la recta por arquimedianidad y en particular $K$. Compacidad entrega índices finitos $J$, que no pueden ser vacíos. Tienen máximo $m$. Cada $U_j$ seleccionado está contenido en $U_m$, así $K\subseteq(-(m+1),m+1)\subseteq[-(m+1),m+1]$. Los extremos son cotas reales. No se usó ninguna sucesión fabricada de puntos lejanos.

La arquimedianidad verifica cobertura sin construir una sucesión de entradas alejadas. La compacidad entrega una lista finita que cubre todo $K$ y su máximo permite dominar todos los abiertos seleccionados con uno. Esa contención aporta cotas inferior y superior uniformes de entradas. Para el vacío, cualquier cota es válida y no se necesita un máximo de índices.

</details>

#### Ejercicio 17. Un radio exterior por índices finitos

[]{#MA-EX-ANM-01-016-017}

Fija $p\notin K$, con $K$ compacto no vacío. Usando $V_n=\{x:|x-p|>1/(n+1)\}$, demuestra que alguna bola positiva alrededor de $p$ evita $K$.

[]{#MA-SOL-ANM-01-016-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Cada $V_n$ es unión de dos rayos abiertos. Para cualquier $x\in K$, la distancia $|x-p|$ es positiva y supera algún recíproco, así la familia cubre $K$. Compacidad entrega una subfamilia finita no vacía; con máximo índice $m$, su unión está en $V_m$ porque los miembros crecen. Por tanto todos los puntos de $K$ distan de $p$ más que $1/(m+1)$. La bola abierta de ese radio en $p$ no toca $K$. Como se puede hacer para cada punto exterior, el complemento de $K$ es abierto y $K$ cerrado.

Cada entrada de $K$ tiene distancia positiva a $p$, pero esas distancias podrían a priori ser arbitrariamente pequeñas. La reducción finita de la cubierta transforma los umbrales individuales en uno común mediante el mayor índice. El radio resultante separa toda la bola de $K$. Así se demuestra cerradura desde cubiertas sin seleccionar una ruta convergente hacia el punto exterior.

</details>

#### Ejercicio 18. Reconocer cinco dominios

[]{#MA-EX-ANM-01-016-018}

Usa Heine–Borel para decidir compacidad de $[0,1]$, $(0,1]$, $\mathbb R$, $\{-1,1\}$ y $\mathbb Q\cap[0,1]$. Justifica el fallo cuando corresponda.

[]{#MA-SOL-ANM-01-016-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

$[0,1]$ es cerrado y acotado, compacto. $(0,1]$ es acotado pero no cerrado, pues cero es adherente por los recíprocos y falta; no es compacto. $\mathbb R$ es cerrado pero no acotado, no compacto. El conjunto finito $\{-1,1\}$ es cerrado y acotado, compacto. Los racionales de $[0,1]$ son acotados pero no cerrados: el irracional $p=\sqrt2/2\in(0,1)$ no pertenece y toda bola suya suficientemente pequeña dentro de $(0,1)$ contiene racionales por densidad. Toda bola, por contener una más pequeña de ese tipo, toca el conjunto. No es compacto. La interfaz algebraica de raíz e irracionalidad viene de C04/C10.

Heine–Borel requiere comprobar cerradura y acotación por separado. Un solo fallo basta para negar compacidad. En los racionales del segmento, la densidad produce entradas próximas al irracional interior sin incluirlo en el dominio. Para una bola grande se recorta a otra menor dentro del segmento, lo que asegura adherencia para todas las escalas y no sólo para algunas.

</details>

#### Ejercicio 19. La cola y el prefijo

[]{#MA-EX-ANM-01-016-019}

Prueba cerradura y compacidad de $K=\{0\}\cup\{1/(n+1):n\in\mathbb N\}$ sin usar la recíproca secuencial. Para un exterior positivo, construye el radio desde una cola y un prefijo finito.

[]{#MA-SOL-ANM-01-016-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

$K\subseteq[0,1]$. Si $p\notin K$ y $p<0$ o $p>1$, la mitad de su distancia al segmento da una bola exterior. En el caso restante $0<p<1$ y $p$ no es ningún recíproco, elegimos $N\ge1$ con $1/(N+1)<p/2$. Para todo $n\ge N$, $t_n=1/(n+1)<p/2$, luego $|p-t_n|>p/2$; cero también dista $p$. Los valores $|p-t_n|$ para $n<N$ son una familia finita no vacía positiva. Sea $d$ el mínimo de ellos y $p/2$, positivo. La bola de radio $d/2$ no contiene cero, prefijo ni cola. El complemento es abierto, por tanto $K$ cerrado; al ser acotado, Heine–Borel lo hace compacto. No se eligió una sucesión de testigos arbitrarios de vecindades.

**Retorno visual.** Véase [C16-F04](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El exterior no puede ser cero ni uno porque ambos pertenecen a $K$. En el caso positivo interior, un único corte $N$ controla de una vez toda la cola. Las entradas restantes son finitas y tienen distancia no nula al exterior. El mínimo positivo combina ambos controles y su mitad evita todas las entradas, incluido cero, acreditando apertura del complemento.

</details>

#### Ejercicio 20. Dos propiedades distintas

[]{#MA-EX-ANM-01-016-020}

Da un compacto real no conexo y un conexo real no compacto. Justifica ambas propiedades con los resultados correspondientes.

[]{#MA-SOL-ANM-01-016-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

$[-2,-1]\cup[1,2]$ es cerrado y acotado, compacto por R4; se separa por los rayos a ambos lados de cero, o no es intervalo por el punto omitido cero entre $-1$ y $1$, así no conexo por C15. $(0,1)$ es intervalo, conexo por C15; no es cerrado porque cero es adherente y falta, así no compacto por Heine–Borel. Los ejemplos muestran que ninguna de las dos propiedades implica la otra.

El compacto con dos piezas obtiene sus propiedades de cerradura y acotación, pero el corte cero muestra su separación. El intervalo abierto obtiene conexidad de intervalaridad, mientras una frontera ausente le impide cerradura y compacidad. Los dos ejemplos son necesarios para descartar las dos implicaciones posibles. Las propiedades pueden coexistir en otros dominios sin que una caracterice a la otra.

</details>

## 16.5. Sucesiones: extraer y seleccionar son tareas distintas

[]{#MA-SEC-ANM-01-016-005}

**Compacidad secuencial.** $K$ es secuencialmente compacto si toda sucesión dada $(x_n)$ de puntos de $K$ tiene una subsucesión $(x_{\varphi(n)})$ que converge a un punto $\ell\in K$, con $\varphi:\mathbb N\to\mathbb N$ estrictamente creciente. El requisito de pertenencia del límite es decisivo. Si $K$ es vacío, no hay sucesión con todos sus términos en él y la condición universal es vacía.

**R5, dirección directa.** Todo compacto real es secuencialmente compacto. Por R4 es cerrado y acotado. Una sucesión dada de puntos de $K$ es acotada, y Bolzano–Weierstrass de C08 proporciona una subsucesión convergente en $\mathbb R$. Su límite está en $K$: si estuviera fuera, la apertura del complemento daría una bola exterior que la convergencia obligaría a ocupar a términos que pertenecen a $K$, contradicción. La extracción actúa sobre una sucesión ya dada mediante el mecanismo de C08, con bisección e índices naturales mínimos; no fabrica puntos de un conjunto arbitrario.

En $(0,1]$, la sucesión dada $x_n=1/(n+1)$ refuta compacidad secuencial. Para cualquier selector estrictamente creciente $\varphi$, se cumple $\varphi(k)\ge k$ por inducción y $0<x_{\varphi(k)}\le1/(k+1)\to0$. Toda extracción tiene límite cero; por unicidad, ninguna puede converger además a un miembro de $(0,1]$. Al añadir cero a los recíprocos obtenemos el compacto ya probado y R5 garantiza una extracción con límite perteneciente al conjunto para cualquier sucesión dada en él.

**Recíproca con alcance.** Para un conjunto arbitrario, probar «secuencialmente compacto implica compacto» requiere, en el argumento siguiente, la hipótesis adicional $\mathrm{CC}(\mathbb R)$: toda familia numerable dada de subconjuntos reales no vacíos admite una selección simultánea. Esta hipótesis es local al enunciado condicional; no se adopta globalmente.

Si $K$ no fuera acotado, los conjuntos

$$E_n=\{x\in K:|x|>n\}$$

serían no vacíos. Aplicamos aquí $\mathrm{CC}(\mathbb R)$ para definir simultáneamente $x_n\in E_n$. Si alguna subsucesión de índices crecientes $\varphi$ convergiera, sería acotada. Sin embargo, $|x_{\varphi(k)}|>\varphi(k)\ge k$ supera cualquier cota fija para un índice suficientemente grande. Ninguna extracción puede converger, contra compacidad secuencial. Así $K$ es acotado bajo la hipótesis declarada.

Si $K$ no fuera cerrado, habría un punto adherente $p\notin K$. Los conjuntos $F_n=K\cap(p-1/(n+1),p+1/(n+1))$ son no vacíos. Aplicando la misma hipótesis de selección obtenemos $z_n\in F_n$ y la cota $|z_n-p|<1/(n+1)$ prueba $z_n\to p$. La compacidad secuencial entrega una subsucesión con límite $\ell\in K$, que también converge a $p$ por ser extracción de una sucesión convergente. La unicidad da $\ell=p$, contradicción. Por tanto $K$ es cerrado y R4 lo hace compacto.

La selección adicional ha intervenido al fabricar las rutas $x_n$ y $z_n$; la extracción posterior trabaja sobre rutas ya definidas. Si $K\ne\varnothing$ viene con una sobreyección dada $e:\mathbb N\to K$, podemos definirlas sin CC(R): para cada $E_n$ o $F_n$, el conjunto de índices $j$ con $e(j)$ dentro es no vacío y tiene un menor elemento natural único. Evaluar $e$ en ese mínimo determina el término. Los índices de fabricación pueden repetirse; no son los índices crecientes de una extracción. La enumeración es un dato y no se infiere para un conjunto real arbitrario. Para el vacío, la compacidad se comprueba directamente.

![La ruta an=1/(n+1) y cada subsucesión convergen a cero. En (0,1\] ese límite queda fuera; al añadir cero al conjunto de recíprocos queda dentro de un compacto. Sólo se muestran los primeros términos. La recíproca secuencial general requiere CC(R), mientras una enumeración sobreyectiva dada permite mínimos de índices.](../../assets/books/anm/C16/C16-F05.svg){#fig-anm-c16-f05 fig-alt="Dos filas de puntos recíprocos que se acercan a cero. El límite aparece como círculo vacío en la primera y lleno en la segunda."}

Las pruebas por cubiertas establecieron compacto $\Longleftrightarrow$ cerrado y acotado, y la extracción de una sucesión dada estableció compacto $\Longrightarrow$ secuencialmente compacto. La vuelta secuencial que acabamos de demostrar conserva CC(R) para conjuntos reales arbitrarios, o utiliza la enumeración sobreyectiva dada de un conjunto no vacío. Este alcance no se extiende silenciosamente a una equivalencia universal sin premisa.

### Ejercicios de la sección 16.5

#### Ejercicio 21. Acotar la ruta y retener su límite

[]{#MA-EX-ANM-01-016-021}

Demuestra que un compacto real es secuencialmente compacto usando Bolzano–Weierstrass de C08. Identifica el paso que coloca el límite en el conjunto.

[]{#MA-SOL-ANM-01-016-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

R4 hace cerrado y acotado a $K$. Dada una sucesión de puntos de $K$, es acotada y C08 entrega una subsucesión convergente en la recta a $\ell$. Si $\ell\notin K$, cerradura da un radio $r>0$ cuya bola en $\ell$ no toca $K$. Convergencia obliga a que los términos de la subsucesión estén eventualmente dentro de esa bola, contradiciendo que todos están en $K$. Por tanto $\ell\in K$. Si $K$ es vacío, no existe tal sucesión y la condición universal se cumple. No se fabrica la sucesión inicial; era un dato.

El límite que proporciona C08 está inicialmente sólo en la recta. La cerradura del dominio lo retiene: una bola exterior sería incompatible con la visita eventual que exige convergencia. La sucesión inicial y sus valores ya son datos, así este paso no fabrica una selección de puntos de familias arbitrarias. En el vacío la afirmación secuencial universal no tiene sucesiones que examinar.

</details>

#### Ejercicio 22. Un límite exterior para todas las extracciones

[]{#MA-EX-ANM-01-016-022}

Prueba que $(0,1]$ no es secuencialmente compacto mediante una sucesión concreta. No basta decir que esa sucesión converge fuera: debes tratar todas sus subsucesiones.

[]{#MA-SOL-ANM-01-016-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Tomamos $x_n=1/(n+1)$, todos en $(0,1]$, con límite cero. Para un selector estrictamente creciente $\varphi$, $\varphi(k)\ge k$ por inducción; entonces $0<x_{\varphi(k)}\le1/(k+1)\to0$. Toda subsucesión converge a cero. Si alguna convergiera a $\ell\in(0,1]$, unicidad del límite daría $\ell=0$, imposible. No hay subsucesión con límite en el dominio, refutando su compacidad secuencial.

**Retorno visual.** Véase [C16-F05](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El selector de una subsucesión puede saltar índices, pero su crecimiento estricto obliga a $\varphi(k)\ge k$. La cota por recíprocos controla por ello cualquier extracción, sin importar sus saltos. La unicidad del límite impide que la misma extracción tenga también un destino interior positivo. Este argumento es más fuerte que comprobar únicamente el destino de la ruta original.

</details>

#### Ejercicio 23. Una fabricación que necesita permiso

[]{#MA-EX-ANM-01-016-023}

Un argumento dice: «Si $K$ no es acotado, para cada $n$ hay $x_n\in K$ con $|x_n|>n$; luego tenemos una sucesión». Distingue las afirmaciones y completa la contradicción bajo CC(R) explícita.

[]{#MA-SOL-ANM-01-016-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

No acotación da que cada $E_n=\{x\in K:|x|>n\}$ es no vacío. Eso es $\forall n\exists x$, no aún una sola función que elija todos los valores. Bajo CC(R) sí existe una sucesión $x_n\in E_n$. Si $K$ fuera secuencialmente compacto, alguna subsucesión $x_{\varphi(k)}$ convergería y por tanto sería acotada por un $M$. Pero $|x_{\varphi(k)}|>\varphi(k)\ge k$, que supera $M$ para algún natural por arquimedianidad. Contradicción. Se prueba acotación bajo la hipótesis indicada; no se adopta CC(R) globalmente.

El cambio que debe justificarse es pasar de existencias individuales a una sola función de términos. CC(R) respalda precisamente ese paso en la recíproca general. Después, una extracción convergente sería acotada, pero sus magnitudes superan índices que crecen sin cota. La contradicción utiliza la ruta seleccionada y deja visible de dónde procede su existencia.

</details>

#### Ejercicio 24. La ruta hacia un punto omitido

[]{#MA-EX-ANM-01-016-024}

Bajo CC(R), prueba que un secuencialmente compacto es cerrado. Declara la familia seleccionada y todos los límites utilizados.

[]{#MA-SOL-ANM-01-016-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Si $K$ no fuese cerrado, habría $p\notin K$ adherente. Los $F_n=K\cap(p-1/(n+1),p+1/(n+1))$ son no vacíos. CC(R) da una sucesión $z_n\in F_n$. La cota $|z_n-p|<1/(n+1)$ prueba $z_n\to p$. Compacidad secuencial da una subsucesión con límite $\ell\in K$. Toda subsucesión de la convergente también converge a $p$; unicidad da $\ell=p$, contradicción. La selección fue la fabricación de $z_n$, mientras la extracción posterior usa la propiedad secuencial. Por ello $K$ es cerrado bajo la premisa declarada.

La familia seleccionada contiene entradas de $K$ dentro de ventanas decrecientes alrededor del exterior. Las cotas de distancia acreditan convergencia de la ruta completa, y por tanto de todas sus extracciones, a $p$. La extracción que ofrece compacidad secuencial tiene además un destino en $K$. Unicidad identifica ambos destinos y contradice que el punto adherente haya sido exterior.

</details>

#### Ejercicio 25. Una enumeración dada determina testigos

[]{#MA-EX-ANM-01-016-025}

Sea $K\ne\varnothing$ secuencialmente compacto y sea $e:\mathbb N\to K$ una sobreyección dada. Prueba que $K$ es cerrado y acotado, y por ello compacto, sin invocar CC(R).

[]{#MA-SOL-ANM-01-016-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Si $K$ fuera no acotado, cada $E_n=\{x\in K:|x|>n\}$ sería no vacío. La sobreyectividad hace no vacío $\{j:e(j)\in E_n\}$. Tomamos su menor índice $j_n$, determinado por buen orden, y $x_n=e(j_n)$. Cualquier subsucesión tiene $|x_{\varphi(k)}|>\varphi(k)\ge k$, y no converge, contradicción. Si hubiera $p\notin K$ adherente, los $F_n=K\cap B_{1/(n+1)}(p)$ serían no vacíos. Tomamos el menor índice $k_n$ con $e(k_n)\in F_n$ y $z_n=e(k_n)\to p$. Compacidad secuencial daría una subsucesión convergente a $\ell\in K$, también a $p$, contradicción por unicidad. Ambas rutas están determinadas por fórmulas de mínimo de índices, sin elegir puntos arbitrariamente. Cerrado y acotado, R4 hace compacto a $K$. No se infiere la enumeración: estaba dada.

La enumeración sobreyectiva es un dato adicional: no se deduce de compacidad secuencial ni se construye sin justificación. El buen orden natural determina un índice mínimo para cada condición no vacía y con ello un término único. Los índices de fabricación pueden repetirse y no son los índices de extracción. Una vez fabricadas las rutas, las dos contradicciones prueban acotación y cerradura, suficientes por R4.

</details>

## 16.6. La continuidad lleva compactos a compactos

[]{#MA-SEC-ANM-01-016-006}

**R6. Imagen continua de un compacto.** Sea $f:D\to\mathbb R$ continua y $K\subseteq D$ compacto. Entonces $H=f[K]$ es compacto. Para vacío, la imagen es vacía. En general fijamos una cubierta abierta arbitraria $(V_i)_{i\in I}$ de $H$. La restricción $h=f\mathbin{\upharpoonright}K$ es continua por C14. Sus preimágenes

$$A_i=h^{-1}[V_i]=\{x\in K:f(x)\in V_i\}$$

son abiertas relativas a $K$ y cubren $K$. La definición que hemos adoptado aplica compacidad a abiertos de la recta, y una preimagen relativa puede no serlo: para la identidad en $[0,1]$, la preimagen de $(-1,1/2)$ es $[0,1/2)$, que contiene cero pero ninguna bola real alrededor de cero. Necesitamos una cubierta ambiental que conserve exactamente las mismas pertenencias dentro de $K$.

Como R4 ya demostró que $K$ es cerrado real, definimos para cada índice

$$W_i=(\mathbb R\setminus K)\cup A_i.$$

Cada $W_i$ es abierto real. Si un punto está fuera de $K$, el complemento abierto proporciona una bola dentro de $W_i$. Para un punto de $A_i$, fijado este índice, la apertura relativa da un abierto real $O$ con $A_i=K\cap O$. Cualquier punto de $O$ está fuera de $K$ o pertenece a $A_i$, de modo que $O\subseteq W_i$ y ofrece una vecindad real del punto. La familia $W$ está definida por una fórmula única: el representante $O$ sólo se usa para acreditar la apertura del índice considerado y no se reúne una familia escogida $(O_i)$. Además,

$$K\cap W_i=A_i.$$

La familia $W$ cubre $K$, porque para cada $x\in K$ la salida $f(x)$ está en algún $V_i$ y por tanto $x\in A_i\subseteq W_i$. La compacidad proporciona un conjunto finito $J\subseteq I$ que cubre $K$ con los $W_j$. Fijada cualquier salida $y\in H$, la pertenencia a la imagen entrega una entrada $x\in K$ con $f(x)=y$. Algún $j\in J$ cubre esa entrada y $x\in K\cap W_j=A_j$ implica $y\in V_j$. Los mismos índices finitos cubren así $H$ con los abiertos originales. No se necesita que la entrada de cada salida sea única ni elegir simultáneamente todas esas entradas.

![Para q(x)=x² sobre K=\[−2,−1\]∪\[1,2\], H=\[1,4\]. V1=(1/2,5/2) y V2=(2,9/2) cubren H; sus preimágenes relativas cubren K. Antes de aplicar compacidad se levantan mediante Wi=(R menos K)∪q⁻¹\[Vi\], una fórmula canónica de abiertos reales. No se requiere inyectividad ni elegir un ambiente por índice.](../../assets/books/anm/C16/C16-F06.svg){#fig-anm-c16-f06 fig-alt="Dos ramas de la parábola sobre un dominio de dos segmentos, con dos bandas de salida que se solapan; debajo aparecen las dos ventanas que cubren el segmento imagen."}

El paso a $W_i$ permitió aplicar compacidad en su ambiente real y la identidad al recortar devolvió los índices hacia las salidas. No se exigió inyectividad, una sucesión seleccionada ni compacidad de todo $D$, sino sólo del subconjunto $K$. Por Heine–Borel la imagen es cerrada y acotada; en particular, una continua tiene valores acotados sobre cada compacto de su dominio, aunque éste tenga varias piezas.

La conclusión no se invierte: una constante en $\mathbb R$ es continua y tiene imagen singleton compacta, mientras su dominio no es compacto. Tampoco hay preservación universal por preimagen: para la constante cero, $f^{-1}[\{0\}]=\mathbb R$. En cambio, la continua $r(x)=1/(1+x^2)$ en la recta tiene preimagen vacía de $\{0\}$ y preimagen $\{0\}$ de $\{1\}$, ambas compactas; conocer esas fibras particulares tampoco prueba compacidad del dominio. El resultado demostrado concierne a imágenes directas de compactos.

### Ejercicios de la sección 16.6

#### Ejercicio 26. Levantar un abierto relativo

[]{#MA-EX-ANM-01-016-026}

Sea $K$ cerrado real y $A$ abierto relativo a $K$. Prueba que $W=(\mathbb R\setminus K)\cup A$ es abierto real y que $K\cap W=A$. Explica por qué esta fórmula sirve para una familia sin elegir ambientes simultáneamente.

[]{#MA-SOL-ANM-01-016-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La identidad es distributividad, pues $K\cap(\mathbb R\setminus K)=\varnothing$ y $A\subseteq K$. Para un punto fuera de $K$, apertura del complemento da una bola dentro de $W$. Para un punto de $A$, representamos $A=K\cap O$ con $O$ abierto real. Todo punto de $O$ está fuera de $K$ o en $A$, así $O\subseteq W$ y da una vecindad del punto. Todos los puntos de $W$ tienen vecindad real dentro, luego $W$ abierto. Para una familia $A_i$, cada $W_i$ está determinado por la misma fórmula; se usa la existencia de un $O$ para probar cada caso, sin reunir una función elegida $i\mapsto O_i$.

Con un representante $O$ del abierto relativo se puede escribir también $W=(\mathbb R\setminus K)\cup O$. La igualdad se verifica separando las entradas de $O$ que están dentro y fuera de $K$. Ambas piezas de esta última unión son abiertas reales porque $K$ es cerrado. La fórmula inicial define $W$ sin depender de cuál representante se haya utilizado para probar su apertura.

</details>

#### Ejercicio 27. Devolver los mismos índices

[]{#MA-EX-ANM-01-016-027}

En R6, una subfamilia finita $W_j$ cubre $K$. Prueba que los mismos índices $j$ cubren $f[K]$ con los $V_j$ originales. No supongas que $f$ tenga inversa.

[]{#MA-SOL-ANM-01-016-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Para $y\in f[K]$ hay una entrada concreta $x\in K$ con $f(x)=y$, por definición de imagen. Algún índice seleccionado $j$ cumple $x\in W_j$. La identidad $K\cap W_j=A_j=f^{-1}[V_j]$ en el dominio restringido da $f(x)\in V_j$, esto es $y\in V_j$. Como $y$ era arbitrario, los mismos índices finitos cubren toda la imagen. Se fija sólo una entrada testigo para el valor considerado; ni unicidad ni una función inversa son necesarias.

La salida arbitraria se fija primero y luego se usa una entrada que la alcance. La cobertura finita de esa entrada proporciona un índice de la misma lista seleccionada. El levantamiento no altera su pertenencia a la preimagen dentro de $K$, así el abierto de salida correspondiente cubre el valor. No se ha supuesto unicidad de entrada ni un selector global de fibras.

</details>

#### Ejercicio 28. Imagen compacta con un hueco

[]{#MA-EX-ANM-01-016-028}

Para $K=[-2,-1]\cup[1,2]$ y $q(x)=x^2$, calcula $q[K]$ y una cubierta de esa imagen con dos miembros abiertos. Describe las preimágenes relativas y sus levantamientos canónicos.

[]{#MA-SOL-ANM-01-016-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Cada rama da valores entre $1$ y $4$, y para $y\in[1,4]$ la raíz positiva $\sqrt y\in[1,2]$ es preimagen; así $q[K]=[1,4]$. Sirven $V_1=(1/2,5/2)$ y $V_2=(2,9/2)$, que solapan y cubren $[1,4]$. Las preimágenes son $A_1=\{x\in K:x^2<5/2\}$ y $A_2=\{x\in K:x^2>2\}$. Son abiertas relativas por continuidad de $q$. $W_i=(\mathbb R\setminus K)\cup A_i$ son abiertos reales porque $K$ es cerrado, y conservan $K\cap W_i=A_i$. El hueco del dominio no impide compacidad ni el transporte de la cubierta.

**Retorno visual.** Véase [C16-F06](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La raíz positiva verifica que todo valor entre uno y cuatro se alcanza, incluso si hay también una entrada negativa que lo produzca. Los dos abiertos de salida solapan entre dos y cinco medios. En el dominio, esa cobertura se traduce en las condiciones $x^2<5/2$ o $x^2>2$, que juntas cubren todas las entradas. Los levantamientos conservan esas selecciones al recortar por $K$.

</details>

#### Ejercicio 29. Una preimagen demasiado grande

[]{#MA-EX-ANM-01-016-029}

Da una continua cuya imagen sea compacta y cuyo dominio no lo sea. Usa el mismo ejemplo para refutar compacidad universal de preimágenes de compactos.

[]{#MA-SOL-ANM-01-016-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

La constante $f:\mathbb R\to\mathbb R$, $f(x)=0$, es continua: el error de salida siempre es cero. Su imagen es el singleton $\{0\}$, compacto por R1, pero su dominio $\mathbb R$ no es compacto. Además $f^{-1}[\{0\}]=\mathbb R$, una preimagen no compacta de un conjunto compacto. R6 sólo preserva imágenes directas de dominios compactos; no afirma las dos recíprocas refutadas.

El mismo ejemplo refuta dos afirmaciones distintas: una recíproca sobre el dominio y una preservación universal por preimagen. La imagen constante es compacta, pero su fibra completa reproduce un dominio no acotado. Continuidad conserva imágenes de compactos; no limita el tamaño de todas las entradas que producen una salida particular.

</details>

#### Ejercicio 30. El ambiente importa antes de aplicar compacidad

[]{#MA-EX-ANM-01-016-030}

Una prueba afirma que las preimágenes $A_i\subseteq K$ de abiertos de salida son abiertos reales y aplica directamente la definición ambiental de compacidad. Da un ejemplo de preimagen no abierta real y repara la prueba.

[]{#MA-SOL-ANM-01-016-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Para la identidad $h:[0,1]\to\mathbb R$, la preimagen de $(-1,1/2)$ es $[0,1/2)$, abierta relativa a $K=[0,1]$ pero no abierta real: toda bola alrededor de cero contiene negativos ajenos al conjunto. Para un $K$ compacto, R4 lo hace cerrado real. Se reemplaza cada preimagen por $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real por el argumento de E026 y con $K\cap W_i=A_i$. La compacidad se aplica ahora a la cubierta ambiental $W$; por E027 los índices finitos vuelven a cubrir salidas con los abiertos originales. No se afirma que $A_i$ cambie de ambiente sin prueba.

El extremo cero pertenece a la preimagen y toda bola real suya incluye negativos, de modo que apertura relativa no puede reinterpretarse como real. El levantamiento añade las entradas exteriores a $K$ y sí proporciona abiertos ambientales. Su identidad al recortar garantiza que la reparación no cambia qué entradas del compacto corresponden a cada abierto de salida. Así los índices finitos aún vuelven a la cubierta original.

</details>

## 16.7. Por qué los extremos llegan a alcanzarse

[]{#MA-SEC-ANM-01-016-007}

Una imagen acotada y no vacía tiene supremo e ínfimo reales, pero todavía pueden faltar en ella. La cerradura que acabamos de obtener para las imágenes compactas impedirá esa ausencia y permitirá recuperar entradas que alcancen las cotas.

**Lema de extremos de un compacto.** Si $H\subseteq\mathbb R$ es compacto y no vacío, $M=\sup H$ y $m=\inf H$ existen por R4 y completitud. Si $M\notin H$, la cerradura da $r>0$ con $(M-r,M+r)\cap H=\varnothing$. Pero $M-r/2<M$ no es cota superior, así existe $y\in H$ con $M-r/2<y\le M$, que cae en la bola excluida. Contradicción: $M\in H$ y es máximo. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, mientras $m+s/2>m$ no es cota inferior; existe $z\in H$ con $m\le z<m+s/2$, de nuevo contradicción. Así $m\in H$ y es mínimo. No elegimos una sucesión que aproxime extremos.

**R7. Weierstrass.** Si $f:D\to\mathbb R$ es continua y $K\subseteq D$ compacto no vacío, hay $x_-,x_+\in K$ con

$$f(x_-)\le f(x)\le f(x_+)\qquad(x\in K).$$

Por R6, $H=f[K]$ es compacto. Como $K$ contiene una entrada, $H$ contiene su salida y es no vacío. El lema da $m,M\in H$ y, por definición de imagen, existen $x_-,x_+\in K$ con $f(x_-)=m$ y $f(x_+)=M$. Las cotas sobre todos los valores de $H$ producen las desigualdades de R7. Se han usado dos testigos concretos de valores alcanzados, sin definir una inversa ni un selector de todas las fibras. No se afirma que esos argumentos sean únicos, distintos o extremos del dominio.

![En \[0,3\], f(x)=(x−1)² alcanza mínimo cero en x=1 y máximo cuatro en x=3. La existencia general procede de la compacidad de la imagen y de su cerradura, que hacen miembros al ínfimo y al supremo. Un extremo de salida puede tener un argumento interior; no se afirma unicidad en general.](../../assets/books/anm/C16/C16-F07.svg){#fig-anm-c16-f07 fig-alt="Parábola restringida al segmento de cero a tres, con mínimo interior en uno y máximo en el extremo derecho."}

Para $f(x)=(x-1)^2$ en $[0,3]$, se cumple $-1\le x-1\le2$ y por tanto $0\le(x-1)^2\le4$. La igualdad inferior exige $x=1$, que es un punto interior. La superior exige $|x-1|=2$, con candidatos $3$ y $-1$; sólo $3$ pertenece al dominio. El mínimo es cero y el máximo cuatro, alcanzados donde indica la figura. En $\{-1,1\}$, en cambio, el cuadrado vale uno en ambas entradas y las dos minimizan y maximizan. La compacidad permite tanto un extremo interior como extremizadores no únicos.

Si el dominio es además un segmento, C15 hace intervalar a la imagen. Weierstrass aporta extremos globales alcanzados $m,M$, así toda salida está en $[m,M]$; la intervalaridad y la pertenencia de ambos extremos dan la inclusión contraria. Obtenemos $f[[a,b]]=[m,M]$, también cuando $a=b$. No podemos identificar sin más $m,M$ con $f(a),f(b)$, como muestra el mínimo interior anterior. En un compacto separado, la identidad de $[-2,-1]\cup[1,2]$ conserva una imagen compacta con hueco: la compacidad da los extremos y la conexidad es la que permite rellenar entre ellos.

La identidad en $(0,1)$ conserva continuidad y acotación, pero no alcanza el ínfimo cero ni el supremo uno porque su dominio no es compacto. Sobre el compacto $[0,1]$, la función $u(x)=x$ para $x<1$ y $u(1)=0$ tiene imagen $[0,1)$ y tampoco alcanza máximo: cada salida $y$ admite otra mayor, $(y+1)/2$, dentro de la imagen. Aquí falla continuidad en uno; para cualquier radio $\delta>0$, $x=1-\min(\delta/2,1/4)$ pertenece al dominio, dista menos que $\delta$ del centro y su salida difiere de $u(1)$ en al menos $3/4$, refutando la tolerancia $1/2$. El vacío sí es compacto, pero carece de entradas extremizadoras. Estas posibilidades explican por separado las hipótesis de R7.

### Ejercicios de la sección 16.7

#### Ejercicio 31. Un supremo que se alcanza

[]{#MA-EX-ANM-01-016-031}

Prueba que un compacto no vacío $H\subseteq\mathbb R$ contiene su supremo y su ínfimo. No construyas una sucesión de puntos próximos a esos valores.

[]{#MA-SOL-ANM-01-016-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Heine–Borel da acotación y cerradura, así completitud da $M=\sup H$ y $m=\inf H$. Si $M\notin H$, alguna bola de radio $r>0$ en $M$ no toca $H$. Como $M-r/2$ no es cota superior, existe $y\in H$ con $M-r/2<y\le M$, dentro de esa bola, contradicción. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, pero $m+s/2$ no es cota inferior; hay $z\in H$ con $m\le z<m+s/2$, también dentro, contradicción. Ambos valores pertenecen y son extremos. Sólo se usan testigos individuales para dos vecindades.

La acotación suministra cotas reales y la no vacuidad permite usar completitud. La cerradura aporta la bola exterior si el extremo no pertenece al conjunto. La propiedad aproximante del supremo o ínfimo encuentra una entrada dentro de esa bola y contradice la hipótesis exterior. Sólo después de ese paso se pueden llamar máximo y mínimo a las cotas óptimas.

</details>

#### Ejercicio 32. Extremos que no son ambos extremos de entrada

[]{#MA-EX-ANM-01-016-032}

Encuentra mínimo, máximo y todos los argumentos que los alcanzan para $f(x)=(x-1)^2$ en $[0,3]$. Justifica con desigualdades, sin derivadas.

[]{#MA-SOL-ANM-01-016-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

$-1\le x-1\le2$. Si $x\le1$, $|x-1|\le1$; si $x\ge1$, $|x-1|\le2$. En todo el dominio $0\le(x-1)^2\le4$. El mínimo cero requiere $x=1$ y se alcanza allí, punto interior. El máximo cuatro requiere $|x-1|=2$, es decir $x=3$ o $x=-1$; sólo $3$ pertenece al dominio. Así el máximo es $4$ único en $3$. No se evaluaron sólo los extremos del dominio para inferir el mínimo.

**Retorno visual.** Véase [C16-F07](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La no negatividad da la cota inferior y la igualdad exige anular $x-1$. La cota superior se obtiene controlando la magnitud de $x-1$ en las dos zonas del dominio. Para hallar todos los maximizadores hay que resolver también la igualdad y descartar el candidato menos uno que queda fuera. Así se acreditan valores extremos y sus fibras completas, sin derivadas.

</details>

#### Ejercicio 33. Un compacto sin continuidad suficiente

[]{#MA-EX-ANM-01-016-033}

En $[0,1]$, define $u(x)=x$ si $x<1$ y $u(1)=0$. Calcula su imagen, decide si alcanza máximo y refuta continuidad en $1$ con un testigo para cada radio.

[]{#MA-SOL-ANM-01-016-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

La imagen es $[0,1)$: los argumentos menores que uno producen todos esos valores y el extremo añade cero ya presente. No hay máximo, porque cada $y<1$ de la imagen tiene $(y+1)/2$ mayor dentro de ella. Para $\delta>0$, tomamos $h=\min(\delta/2,1/4)>0$ y $x=1-h\in[0,1)$. Dista menos que $\delta$ de $1$ y $|u(x)-u(1)|=1-h\ge3/4>1/2$. La tolerancia $1/2$ refuta continuidad. El dominio compacto no basta sin la hipótesis funcional de R7.

El extremo de entrada uno tiene una salida que ya estaba en la imagen y no cierra su frontera superior. La imagen permanece acotada pero sin máximo. El testigo para cada radio se mantiene dentro del dominio y compara con el valor central cero, como exige continuidad. Por ello el ejemplo conserva compacidad del dominio y muestra exactamente la necesidad de continuidad de la función.

</details>

#### Ejercicio 34. No vacuidad y no unicidad

[]{#MA-EX-ANM-01-016-034}

Explica por qué Weierstrass requiere dominio no vacío pero no garantiza unicidad de los extremizadores. Da un ejemplo compacto no vacío con varios mínimos y máximos.

[]{#MA-SOL-ANM-01-016-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

El vacío es compacto, pero no contiene ninguna entrada que sirva de $x_-$ o $x_+$. Su imagen es vacía y no tiene mínimo o máximo real alcanzado. Para no unicidad, $K=\{-1,1\}$ es compacto y $f(x)=x^2$ es continua en él y vale $1$ en ambos puntos. Los dos argumentos minimizan y maximizan; la desigualdad global de Weierstrass permite ese caso. No exige puntos distintos ni únicos.

La compacidad incluye el vacío, mientras existencia de extremizadores exige entradas reales del dominio. Esa diferencia explica la hipótesis de no vacuidad. En el ejemplo no vacío, dos entradas comparten ambas salidas extremas y satisfacen todas las desigualdades globales. Weierstrass permite empates y no impone que mínimo y máximo sean distintos.

</details>

#### Ejercicio 35. Dos teoremas para describir la imagen

[]{#MA-EX-ANM-01-016-035}

Sea $a\le b$ y $f:[a,b]\to\mathbb R$ continua. Prueba que su imagen es $[m,M]$, identificando qué aporta C15 y qué aporta C16. Refuta que se puedan tomar siempre $m=f(a)$ y $M=f(b)$.

[]{#MA-SOL-ANM-01-016-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

R2 hace compacto al segmento y R7 aporta extremos globales alcanzados $m\le M$ de la imagen. Toda salida está en $[m,M]$. C15 hace intervalar la imagen porque la función es continua en un intervalo. Como $m,M$ pertenecen a ella, incluye todo $[m,M]$. Ambas inclusiones dan igualdad. Para $f(x)=(x-1)^2$ en $[0,3]$, el mínimo es $0=f(1)$, mientras $f(0)=1$; la propuesta de usar siempre valores de entrada extremos es falsa. Compacidad da extremos alcanzados y conexidad rellena entre ellos, funciones distintas de las dos hipótesis.

La primera inclusión procede de las cotas globales alcanzadas de Weierstrass. La segunda procede de intervalaridad de la imagen y pertenencia de los dos valores extremos. Si $a=b$, la imagen es un singleton y ambas inclusiones siguen siendo válidas. El contraejemplo muestra que los valores globales deben identificarse por la función completa, no asignarse de antemano a los extremos de entrada.

</details>

## 16.8. Márgenes positivos e inversas sobre compactos

[]{#MA-SEC-ANM-01-016-008}

**R8, margen respecto de cero.** Sea $K$ compacto no vacío y $f:K\to\mathbb R$ continua sin ceros. La función $|f|$ es continua por C14. R7 entrega $x_0\in K$ donde alcanza su mínimo $m=|f(x_0)|$. Como no hay ceros, $m>0$, y

$$|f(x)|\ge m>0\qquad(x\in K).$$

El mínimo alcanzado de $|f|$ es una magnitud de la forma $|f(x_0)|$, y la ausencia de ceros la hace positiva. Esto da una barrera común, más fuerte que disponer de un valor no nulo en cada punto por separado. El recíproco está definido en todo $K$, es continuo por C14 y satisface $|1/f(x)|\le1/m$. Para otra continua $g:K\to\mathbb R$, R6 o R7 proporciona $B\ge0$ con $|g(x)|\le B$, y queda $|g(x)/f(x)|\le B/m$ en todo $K$. En $(0,1]$, la identidad es positiva pero algún recíproco $1/(n+1)$ es menor que cualquier margen propuesto; sin compacidad no se obtiene esa conclusión global.

![La función x² en K=\[−2,−1\]∪\[1,2\] tiene mínimo alcanzado m=1. Ningún valor de |f| entra en \[0,1); por tanto |1/f|≤1. El margen requiere compacidad, continuidad y ausencia de ceros. En (0,1\], la identidad es positiva pero carece de margen positivo global.](../../assets/books/anm/C16/C16-F08.svg){#fig-anm-c16-f08 fig-alt="Dos ramas del cuadrado con mínimo uno; una franja bajo ese nivel separa toda la imagen del cero y controla el recíproco."}

Para un real $p$ fijado, la función distancia $d_p(x)=|x-p|$ es continua por C14 y alcanza su mínimo en el compacto no vacío $K$. Si $p\notin K$, el minimizador $x_0$ es distinto de $p$ y la distancia mínima $|x_0-p|$ es positiva. Si $p\in K$, se alcanza cero en la entrada $p$. Puede haber varios puntos más próximos: para $K=\{-1,1\}$ y $p=0$, ambos dan distancia uno. La prueba produce un minimizador para este $p$; no una selección única o simultánea para todos los puntos exteriores.

**Fibras compactas.** Para una continua $f:K\to\mathbb R$ con dominio compacto y un cerrado real $F$, C14 hace $f^{-1}[F]$ cerrado relativo a $K$ y R3 lo hace compacto. En particular, cada fibra $f^{-1}[\{y\}]$ es compacta, incluso cuando el valor no se alcanza y la fibra es vacía. Aquí el dominio compacto y la condición cerrada de salida aportan las hipótesis que faltaban en el contraejemplo de la constante en la recta. El cerrado $F$ ni siquiera necesita ser acotado: la acotación relevante está en el dominio.

**Inversa en un compacto.** Una inyección continua $f:K\to\mathbb R$ con $K$ compacto es un homeomorfismo $K\to H=f[K]$. Al declarar codominio $H$ se conserva el control de distancias de $f$. Cada salida de $H$ tiene una entrada única por definición de imagen e inyectividad, así que existe $h:H\to K$. Sea $A$ cerrado relativo a $K$. Por R3 es compacto y por R6 su imagen $f[A]$ también lo es; R4 la hace cerrada real y, en particular, cerrada relativa a $H$. La biyectividad hacia la imagen da

$$h^{-1}[A]=f[A].$$

El miembro izquierdo es la preimagen por $h$ de un cerrado relativo de su codominio $K$, y el derecho acaba de probarse cerrado relativo en su dominio $H$. Como vale para todo $A$, el criterio de C14 concluye continuidad de $h$. La prueba incluye el vacío, donde tanto la inversa como sus controles son vacíos, y no necesita que el compacto sea intervalo ni que exista monotonía global.

En C15 la intervalaridad permitió construir barreras de orden para la inversa. La compacidad permite otra prueba mediante cerrados, aplicable también a dominios separados. La biyección de C14/C15 sobre $[0,1)\cup[2,3]$, con ramas $x$ y $x-1$, queda fuera de esta hipótesis: el punto uno es adherente al dominio y falta en él, así que no es cerrado ni compacto. La falla de continuidad inversa de aquel ejemplo no contradice el resultado presente.

La positividad en cada entrada adquirió un margen común al convertirse el ínfimo de $|f|$ en un valor alcanzado. La misma pertenencia de los extremos a la imagen permitió minimizar distancias, mientras el transporte de compactos convirtió imágenes de cerrados en preimágenes cerradas de la inversa. Todos esos pasos se apoyan en la reducción finita de cubiertas, sin haber exigido todavía un radio de continuidad común para todos los centros.

### Ejercicios de la sección 16.8

#### Ejercicio 36. Positividad con margen

[]{#MA-EX-ANM-01-016-036}

En $K=[-2,-1]\cup[1,2]$, considera $f(x)=x^2$ y $g(x)=x+1$. Encuentra un margen positivo de $|f|$ y cotas de $|1/f|$ y $|g/f|$ válidas en todo $K$.

[]{#MA-SOL-ANM-01-016-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Para todo $x\in K$, $1\le x^2\le4$, así $m=1$ es un margen positivo, alcanzado en $\pm1$. El recíproco está definido y $|1/f(x)|=1/x^2\le1$. Además $|g(x)|=|x+1|\le|x|+1\le3$, y $|g(x)/f(x)|\le3$. Las funciones son continuas por C14; las cotas explícitas verifican la consecuencia de R8 sin exigir conectividad del dominio. La cota $3$ es válida aunque no se afirme que sea óptima.

**Retorno visual.** Véase [C16-F08](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El margen uno se alcanza en ambos puntos de magnitud uno y es válido en las dos piezas del dominio. Invertirlo controla el recíproco. La triangular y $|x|\le2$ dan una cota del numerador; dividir por un denominador de magnitud al menos uno conserva esa cota. Estos controles son globales y no necesitan conectar las dos piezas por un intervalo.

</details>

#### Ejercicio 37. Punto más cercano y dos candidatos

[]{#MA-EX-ANM-01-016-037}

Prueba que cualquier compacto no vacío tiene un punto más próximo a un real fijado $p$. Para $K=\{-1,1\}$ y $p=0$, calcula todos los minimizadores y el margen.

[]{#MA-SOL-ANM-01-016-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

$d_p(x)=|x-p|$ es continua por C14; R7 da un $x_0\in K$ donde alcanza mínimo $m$. Así $|x-p|\ge m$ para todo $x\in K$. Si $p\notin K$, $m=|x_0-p|>0$; si $p\in K$, la entrada $p$ da mínimo cero. En $\{-1,1\}$ con $p=0$ ambas distancias valen $1$, luego ambos puntos son minimizadores y el margen es $1$. No se garantiza unicidad ni se construye una elección para todos los $p$ simultáneamente.

El mínimo de distancia pertenece a la imagen de la función continua y por eso hay una entrada que lo alcanza. Si el punto fijado es exterior, esa entrada no coincide con él y el valor mínimo es positivo. Los dos candidatos del ejemplo tienen la misma distancia y ninguno mejora al otro. Existencia de un minimizador no equivale a una regla única de elección para todos los puntos exteriores.

</details>

#### Ejercicio 38. Una fibra compacta que se divide

[]{#MA-EX-ANM-01-016-038}

Para $q(x)=x^2$ en $K=[-2,2]$, calcula la fibra de $1$ y prueba su compacidad y su desconexión. Generaliza la compacidad a la preimagen de cualquier cerrado real por una continua en compacto.

[]{#MA-SOL-ANM-01-016-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

La ecuación $x^2=1$ da $\{-1,1\}$, finito y compacto. No es intervalo porque omite cero entre sus puntos, así no conexo por C15. En general, si $f:K\to\mathbb R$ es continua y $F$ cerrado real, C14 da $f^{-1}[F]$ cerrado relativo a $K$, y R3 lo hace compacto. Se incluyen fibras vacías. No hay contradicción entre compacidad y desconexión ni una afirmación de preimágenes compactas para dominios arbitrarios.

La fibra concreta tiene dos entradas y su compacidad proviene de finitud, pero su desconexión proviene del hueco entre ellas. En la generalización, cerrado de salida se convierte por continuidad en cerrado relativo de entradas, y R3 utiliza el dominio compacto. La conclusión no exige que el cerrado de salida sea acotado, pues la acotación relevante ya está en el dominio.

</details>

#### Ejercicio 39. Inversa por transporte de cerrados

[]{#MA-EX-ANM-01-016-039}

Sea $K$ compacto y $f:K\to\mathbb R$ continua e inyectiva. Demuestra que la inversa $h:f[K]\to K$ es continua mediante preimágenes de cerrados relativos. Trata el vacío.

[]{#MA-SOL-ANM-01-016-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Inyectividad y pertenencia a la imagen dan una entrada única para cada salida, por lo que $h$ existe. Si $A\subseteq K$ es cerrado relativo, R3 lo hace compacto. Su imagen $f[A]$ es compacta por R6, cerrada real por R4 y por ello cerrada relativa a $H=f[K]$. La identidad de la biyección $h^{-1}[A]=f[A]$ prueba que todas esas preimágenes son cerradas relativas. El criterio de C14 para funciones entre dominios y codominios reales relativos da continuidad de $h$. Re-tipar la función directa hacia $H$ conserva el mismo control de distancias y su continuidad. Si $K$ es vacío, también lo es $H$, y las funciones vacías son continuas por la condición universal sin entradas.

La inversa tiene dominio exactamente la imagen y codominio $K$. Cada cerrado relativo de ese codominio debe tener preimagen cerrada relativa en la imagen. La identidad con $f[A]$ traduce esa obligación en transporte de compactos y Heine–Borel. El vacío satisface el criterio sin entradas; no hay necesidad de excluirlo ni de añadir monotonía o continuidad uniforme.

</details>

#### Ejercicio 40. Homeomorfismo compacto sin monotonía global

[]{#MA-EX-ANM-01-016-040}

Sea $K=[0,1]\cup[2,3]$ y define $f(x)=x$ en la primera pieza, $f(x)=x-4$ en la segunda. Calcula la imagen, prueba inyectividad y continuidad, decide si es monótona en todo $K$ y justifica continuidad de su inversa.

[]{#MA-SOL-ANM-01-016-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La imagen es $H=[0,1]\cup[-2,-1]$. Las imágenes de ramas son disjuntas y cada rama es inyectiva; por tanto la función es inyectiva y sobreyectiva sobre $H$. Para un centro de $K$ y $\varepsilon>0$, $\delta=\min(1/2,\varepsilon)$ evita la otra pieza y en la misma rama el error de salida es la distancia de entradas, menor que $\varepsilon$. Es continua relativa. No es creciente porque $f(1)=1>f(2)=-2$ aunque $1<2$; no es decreciente porque $f(0)=0<f(1)=1$. $K$ es cerrado y acotado, compacto, así la prueba de E039 da inversa continua sin monotonía global. Explícitamente vale $h(y)=y$ en $[0,1]$ y $h(y)=y+4$ en $[-2,-1]$. La hipótesis compacta sirve aunque el dominio esté roto.

Las imágenes de las dos piezas son disjuntas, por lo que la inyectividad local de cada rama se convierte en inyectividad global. La separación de las piezas permite un radio común auxiliar que mantiene una entrada próxima en la misma rama. Las comparaciones dadas refutan tanto crecimiento como decrecimiento globales. Aun así compacidad e inyectividad permiten aplicar E039 y obtener continuidad de la inversa sobre la imagen separada.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-16)

[← Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Capítulo 17 →](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html)
