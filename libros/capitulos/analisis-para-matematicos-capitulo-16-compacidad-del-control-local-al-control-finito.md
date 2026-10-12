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
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C16.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-16)

Una cubierta abierta puede contener infinitos controles locales. La compacidad exige que, para cada cubierta dada, baste un conjunto finito de sus índices para proteger todos los puntos. Ese paso de lo local a lo finito permitirá convertir continuidad en extremos alcanzados y márgenes positivos.

Partimos de abiertos y cerrados de C04, extracción de sucesiones dadas de C08 y continuidad de C14, con supremo de C00, límites de C06 y tipos de C12 como interfaces heredadas. Primero probaremos que un segmento es compacto usando supremo; después deduciremos Heine–Borel sin usar sucesiones. Distinguiremos extracción de una ruta dada y selección de una ruta nueva. Las imágenes continuas, los extremos y las inversas se tratarán por cubiertas y cerradura. No usamos continuidad uniforme ni derivadas. La recíproca secuencial general se declara condicional a CC(R); para una enumeración dada se construyen los testigos por mínimos de índices.

## 16.1. Una cubierta dada y una reducción finita

[]{#MA-SEC-ANM-01-016-001}

En C14 un punto recibía un radio de control; en C15 la ausencia de separaciones producía valores intermedios. Ahora buscamos otra forma de pasar de información local a una conclusión global: que una familia de vecindades pueda reducirse a un número finito de ellas, sin dejar puntos sin cubrir.

**Definición.** Una cubierta abierta de $K\subseteq\mathbb R$ es una familia dada $U:I\to\mathcal P(\mathbb R)$, cuyos miembros $U_i$ son abiertos reales, tal que

$$K\subseteq\bigcup_{i\in I}U_i.$$

La cobertura significa $\forall x\in K\;\exists i\in I:\;x\in U_i$. No presupone una función que elija un índice para cada punto. Una **subcubierta finita** es una restricción a un conjunto finito $J\subseteq I$ que todavía cubre $K$. Se conservan miembros de la familia original; no se reemplazan por nuevos abiertos. Índices diferentes pueden tener el mismo abierto asociado.

**Compacidad.** $K$ es compacto si **toda** cubierta abierta dada de $K$ admite una subcubierta finita. El orden de cuantificadores es: familia arbitraria completa, luego un conjunto finito de índices, luego cobertura de todos los puntos. Exhibir una única cubierta finita no prueba compacidad: $\{\mathbb R\}$ cubre finitamente cualquier conjunto real. Para refutarla, en cambio, basta una cubierta concreta sin ninguna reducción finita.

![Los abiertos U1=(−1/4,2/5), U2=(3/10,4/5), U3=(7/10,5/4) y U4=(1/5,3/5) cubren \[0,1\]. J={1,2,3} basta, incluidos los extremos. Esta verificación particular no demuestra por sí sola compacidad; la definición cuantifica sobre toda cubierta.](../../assets/books/anm/C16/C16-F01.svg){#fig-anm-c16-f01 fig-alt="Los abiertos U1=(−1/4,2/5), U2=(3/10,4/5), U3=(7/10,5/4) y U4=(1/5,3/5) cubren \[0,1\]. J={1,2,3} basta, incluidos los extremos. Esta verificación particular no demuestra por sí sola compacidad; la definición cuantifica sobre toda cubierta."}

**R1. Casos finitos y una primera fuga.** El vacío es compacto: de cualquier cubierta tomamos $J=\varnothing$, cuya unión cubre el vacío. Para un singleton $\{a\}$, la cobertura proporciona un índice $i$ con $a\in U_i$; $J=\{i\}$ basta. Una unión de dos compactos es compacta: una cubierta de la unión cubre por separado ambas piezas, que entregan conjuntos finitos $J_1,J_2$; la unión finita $J_1\cup J_2$ cubre todo. Inducción finita da compacidad de conjuntos finitos y de uniones finitas de compactos. No se está escogiendo una subcubierta por cada miembro de una familia infinita.

La recta no es compacta. Los abiertos $U_n=(-(n+1),n+1)$, $n\in\mathbb N$, la cubren por arquimedianidad. Para un conjunto finito no vacío de índices $J$, existe $m=\max J$; todos sus miembros están en $U_m$, y $m+2$ queda fuera. La subfamilia vacía tampoco cubre la recta. Se ha refutado la posibilidad de cualquier $J$ finito en esta cubierta.

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-016-001}

¿Qué distingue una cubierta finita particular de la compacidad?

[]{#MA-MSOL-ANM-01-016-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

**Respuesta.**

Una cubierta finita particular cubre el conjunto una sola vez; compacidad exige una subcubierta finita dentro de toda cubierta abierta dada. La familia $\{\mathbb R\}$ cubre finitamente cualquier conjunto, incluso los no compactos.

**Fundamento en la sección 16.1.**

La cobertura significa $\forall x\in K\;\exists i\in I:\;x\in U_i$. No presupone una función que elija un índice para cada punto. Una **subcubierta finita** es una restricción a un conjunto finito $J\subseteq I$ que todavía cubre $K$. Se conservan miembros de la familia original; no se reemplazan por nuevos abiertos. Índices diferentes pueden tener el mismo abierto asociado.

**Compacidad.** $K$ es compacto si **toda** cubierta abierta dada de $K$ admite una subcubierta finita. El orden de cuantificadores es: familia arbitraria completa, luego un conjunto finito de índices, luego cobertura de todos los puntos. Exhibir una única cubierta finita no prueba compacidad: $\{\mathbb R\}$ cubre finitamente cualquier conjunto real. Para refutarla, en cambio, basta una cubierta concreta sin ninguna reducción finita.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-016-002}

¿Qué debe conservar una subcubierta de $(U_i)_{i\in I}$?

[]{#MA-MSOL-ANM-01-016-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

**Respuesta.**

Miembros de la familia original y cobertura de todos los puntos de $K$. Se restringe a índices $J\subseteq I$ finitos; no se reemplazan abiertos por otros nuevos.

**Fundamento en la sección 16.1.**

La cobertura significa $\forall x\in K\;\exists i\in I:\;x\in U_i$. No presupone una función que elija un índice para cada punto. Una **subcubierta finita** es una restricción a un conjunto finito $J\subseteq I$ que todavía cubre $K$. Se conservan miembros de la familia original; no se reemplazan por nuevos abiertos. Índices diferentes pueden tener el mismo abierto asociado.

**Compacidad.** $K$ es compacto si **toda** cubierta abierta dada de $K$ admite una subcubierta finita. El orden de cuantificadores es: familia arbitraria completa, luego un conjunto finito de índices, luego cobertura de todos los puntos. Exhibir una única cubierta finita no prueba compacidad: $\{\mathbb R\}$ cubre finitamente cualquier conjunto real. Para refutarla, en cambio, basta una cubierta concreta sin ninguna reducción finita.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-016-003}

¿La cobertura $\forall x\in K\;\exists i:x\in U_i$ ya da una función de índices por punto?

[]{#MA-MSOL-ANM-01-016-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

**Respuesta.**

No. Asegura un testigo para cada punto considerado, pero no construye una selección simultánea $x\mapsto i_x$. Las pruebas usan sólo los testigos concretos que necesitan.

**Fundamento en la sección 16.1.**

La cobertura significa $\forall x\in K\;\exists i\in I:\;x\in U_i$. No presupone una función que elija un índice para cada punto. Una **subcubierta finita** es una restricción a un conjunto finito $J\subseteq I$ que todavía cubre $K$. Se conservan miembros de la familia original; no se reemplazan por nuevos abiertos. Índices diferentes pueden tener el mismo abierto asociado.

**Compacidad.** $K$ es compacto si **toda** cubierta abierta dada de $K$ admite una subcubierta finita. El orden de cuantificadores es: familia arbitraria completa, luego un conjunto finito de índices, luego cobertura de todos los puntos. Exhibir una única cubierta finita no prueba compacidad: $\{\mathbb R\}$ cubre finitamente cualquier conjunto real. Para refutarla, en cambio, basta una cubierta concreta sin ninguna reducción finita.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-016-004}

¿Cómo se cubre finitamente el vacío dentro de cualquier cubierta?

[]{#MA-MSOL-ANM-01-016-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

**Respuesta.**

Tomando el conjunto vacío de índices. Su unión es vacía y contiene al conjunto vacío, incluso si la cubierta original no tiene índices.

**Fundamento en la sección 16.1.**

La recta no es compacta. Los abiertos $U_n=(-(n+1),n+1)$, $n\in\mathbb N$, la cubren por arquimedianidad. Para un conjunto finito no vacío de índices $J$, existe $m=\max J$; todos sus miembros están en $U_m$, y $m+2$ queda fuera. La subfamilia vacía tampoco cubre la recta. Se ha refutado la posibilidad de cualquier $J$ finito en esta cubierta.

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-016-005}

¿Por qué una cubierta arbitraria de un singleton tiene subcubierta finita?

[]{#MA-MSOL-ANM-01-016-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

**Respuesta.**

La cobertura del único punto $a$ da un índice $i$ con $a\in U_i$. El singleton de índices $\{i\}$ cubre todo $\{a\}$.

**Fundamento en la sección 16.1.**

La cobertura significa $\forall x\in K\;\exists i\in I:\;x\in U_i$. No presupone una función que elija un índice para cada punto. Una **subcubierta finita** es una restricción a un conjunto finito $J\subseteq I$ que todavía cubre $K$. Se conservan miembros de la familia original; no se reemplazan por nuevos abiertos. Índices diferentes pueden tener el mismo abierto asociado.

**Compacidad.** $K$ es compacto si **toda** cubierta abierta dada de $K$ admite una subcubierta finita. El orden de cuantificadores es: familia arbitraria completa, luego un conjunto finito de índices, luego cobertura de todos los puntos. Exhibir una única cubierta finita no prueba compacidad: $\{\mathbb R\}$ cubre finitamente cualquier conjunto real. Para refutarla, en cambio, basta una cubierta concreta sin ninguna reducción finita.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-016-006}

¿Cómo se combinan dos subcubiertas finitas para cubrir una unión de compactos?

[]{#MA-MSOL-ANM-01-016-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

**Respuesta.**

La cubierta de la unión cubre cada pieza. Cada compacto da un conjunto finito de índices y su unión, también finita, cubre ambas piezas.

**Fundamento en la sección 16.1.**

**R1. Casos finitos y una primera fuga.** El vacío es compacto: de cualquier cubierta tomamos $J=\varnothing$, cuya unión cubre el vacío. Para un singleton $\{a\}$, la cobertura proporciona un índice $i$ con $a\in U_i$; $J=\{i\}$ basta. Una unión de dos compactos es compacta: una cubierta de la unión cubre por separado ambas piezas, que entregan conjuntos finitos $J_1,J_2$; la unión finita $J_1\cup J_2$ cubre todo. Inducción finita da compacidad de conjuntos finitos y de uniones finitas de compactos. No se está escogiendo una subcubierta por cada miembro de una familia infinita.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-016-007}

¿Por qué $U_n=(-(n+1),n+1)$ no tiene una subcubierta finita de la recta?

[]{#MA-MSOL-ANM-01-016-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

**Respuesta.**

Los índices de una subfamilia finita no vacía tienen máximo $m$, y todos los abiertos seleccionados están en $U_m$. El punto $m+2$ queda fuera. La familia vacía tampoco cubre la recta.

**Fundamento en la sección 16.1.**

La recta no es compacta. Los abiertos $U_n=(-(n+1),n+1)$, $n\in\mathbb N$, la cubren por arquimedianidad. Para un conjunto finito no vacío de índices $J$, existe $m=\max J$; todos sus miembros están en $U_m$, y $m+2$ queda fuera. La subfamilia vacía tampoco cubre la recta. Se ha refutado la posibilidad de cualquier $J$ finito en esta cubierta.

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-016-008}

¿El ínfimo de una familia infinita de radios positivos tiene que ser positivo?

[]{#MA-MSOL-ANM-01-016-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

**Respuesta.**

No. $r_n=1/(n+1)>0$ para todo $n$, pero $\inf_n r_n=0$. Un mínimo positivo se garantiza aquí sólo para una familia finita no vacía de valores positivos.

**Fundamento en la sección 16.1.**

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

</details>

### Ejercicios de la sección 16.1

[]{#ejercicios-16}

#### Ejercicio 1. Una sola cubierta no basta

[]{#MA-EX-ANM-01-016-001}

Un argumento afirma que todo subconjunto real es compacto porque $\{\mathbb R\}$ es una cubierta finita. Explica el cambio ilegítimo de cuantificadores y refútalo con una cubierta de $\mathbb R$.

[]{#MA-SOL-ANM-01-016-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

**Respuesta.**

Compacidad exige que para toda cubierta abierta dada exista una subcubierta finita de esa misma familia. El argumento sólo presenta una cubierta conveniente. Para $\mathbb R$, la familia $U_n=(-(n+1),n+1)$ cubre por arquimedianidad. Toda lista finita no vacía de índices tiene máximo $m$ y su unión está en $U_m$, que no contiene $m+2$. La subfamilia vacía tampoco cubre la recta. Por tanto hay una cubierta sin ninguna subcubierta finita y la recta no es compacta.

**Fundamento en la sección 16.1.**

La recta no es compacta. Los abiertos $U_n=(-(n+1),n+1)$, $n\in\mathbb N$, la cubren por arquimedianidad. Para un conjunto finito no vacío de índices $J$, existe $m=\max J$; todos sus miembros están en $U_m$, y $m+2$ queda fuera. La subfamilia vacía tampoco cubre la recta. Se ha refutado la posibilidad de cualquier $J$ finito en esta cubierta.

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

</details>

#### Ejercicio 2. Subcubierta concreta

[]{#MA-EX-ANM-01-016-002}

Considera $K=[0,1]$ y los abiertos $U_1=(-1/4,2/5)$, $U_2=(3/10,4/5)$, $U_3=(7/10,5/4)$, $U_4=(1/5,3/5)$. Identifica una subcubierta de tres miembros y muestra que quitar cualquiera de esos tres deja algún punto sin cubrir dentro de esa subfamilia.

[]{#MA-SOL-ANM-01-016-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Los índices $J=\{1,2,3\}$ sirven: $U_1$ cubre desde cero hasta antes de $2/5$, $U_2$ solapa desde $3/10$ y cubre hasta antes de $4/5$, y $U_3$ solapa desde $7/10$ y alcanza uno. Su unión contiene $[0,1]$. Al quitar $U_1$, cero queda fuera; al quitar $U_3$, uno queda fuera; al quitar $U_2$, $1/2$ no está en $U_1$ ni $U_3$. Es una subcubierta concreta, y su irredundancia dentro de esos tres no prueba por sí sola compacidad de $K$, que debe valer para cualquier cubierta.

**Retorno visual.** Véase [C16-F01](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 3. Uniones finitas desde la definición

[]{#MA-EX-ANM-01-016-003}

Prueba desde cubiertas que una unión finita de compactos reales es compacta, incluyendo la unión vacía. No invoques Heine–Borel.

[]{#MA-SOL-ANM-01-016-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

**Respuesta.**

El vacío es compacto porque dentro de cualquier cubierta sirve la subfamilia vacía. Para dos compactos, una cubierta de la unión cubre cada uno; existen conjuntos finitos de índices $J_1,J_2$ que cubren las piezas. Su unión finita cubre la unión de las piezas. Por inducción sobre una lista finita de compactos, partiendo de la unión vacía y añadiendo una pieza por paso, se obtiene el resultado. Sólo se combinan testigos finitos de la cubierta fijada; no se escogen subcubiertas de infinitos compactos.

**Fundamento en la sección 16.1.**

La recta no es compacta. Los abiertos $U_n=(-(n+1),n+1)$, $n\in\mathbb N$, la cubren por arquimedianidad. Para un conjunto finito no vacío de índices $J$, existe $m=\max J$; todos sus miembros están en $U_m$, y $m+2$ queda fuera. La subfamilia vacía tampoco cubre la recta. Se ha refutado la posibilidad de cualquier $J$ finito en esta cubierta.

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

</details>

#### Ejercicio 4. El mínimo positivo tiene una hipótesis

[]{#MA-EX-ANM-01-016-004}

Demuestra que una familia finita no vacía de radios positivos tiene mínimo positivo. Refuta la conclusión análoga para una familia infinita.

[]{#MA-SOL-ANM-01-016-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

**Respuesta.**

Una lista finita no vacía $r_1,\ldots,r_k$ admite un mínimo: empezamos por $r_1$ y comparamos sucesivamente con el siguiente valor, conservando el menor. El resultado es uno de los $r_j$, luego es positivo. Para $r_n=1/(n+1)$, todos los radios son positivos y cero es cota inferior. Para cualquier $c>0$, arquimedianidad da $n$ con $1/(n+1)<c$, así ninguna cota inferior positiva es posible. El ínfimo es cero y no hay un radio positivo que sea menor o igual que todos.

**Fundamento en la sección 16.1.**

La recta no es compacta. Los abiertos $U_n=(-(n+1),n+1)$, $n\in\mathbb N$, la cubren por arquimedianidad. Para un conjunto finito no vacío de índices $J$, existe $m=\max J$; todos sus miembros están en $U_m$, y $m+2$ queda fuera. La subfamilia vacía tampoco cubre la recta. Se ha refutado la posibilidad de cualquier $J$ finito en esta cubierta.

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

</details>

#### Ejercicio 5. Una unión infinita que escapa

[]{#MA-EX-ANM-01-016-005}

Sabiendo que cada segmento $[-n,n]$ será compacto por R2, explica por qué la unión de esos segmentos para $n\in\mathbb N$ refuta que toda unión de compactos sea compacta. Exhibe la cubierta responsable.

[]{#MA-SOL-ANM-01-016-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

**Respuesta.**

Por arquimedianidad cada real está en algún $[-n,n]$, así la unión es $\mathbb R$. R2 prueba compacidad de cada segmento, incluido $n=0$. Pero la cubierta $U_n=(-(n+1),n+1)$ de la recta no tiene reducción finita: si $m$ es máximo de los índices seleccionados, $m+2$ queda fuera. La conclusión de unión finita no se extiende a uniones infinitas; las reducciones entregadas por cada pieza no se convierten automáticamente en una sola lista finita.

**Fundamento en la sección 16.1.**

La recta no es compacta. Los abiertos $U_n=(-(n+1),n+1)$, $n\in\mathbb N$, la cubren por arquimedianidad. Para un conjunto finito no vacío de índices $J$, existe $m=\max J$; todos sus miembros están en $U_m$, y $m+2$ queda fuera. La subfamilia vacía tampoco cubre la recta. Se ha refutado la posibilidad de cualquier $J$ finito en esta cubierta.

**Herramienta finita.** Un conjunto finito no vacío de reales tiene mínimo y máximo: se ordena una lista finita comparando dos valores en cada paso. Si sus valores son todos positivos, el mínimo es positivo porque es uno de ellos. Para una familia infinita positiva esto no vale: $1/(n+1)>0$ para todo $n$, pero su ínfimo es cero. La compacidad será valiosa precisamente porque entrega un conjunto finito concreto antes de tomar un mínimo.

</details>
## 16.2. El supremo prolonga los segmentos cubiertos

[]{#MA-SEC-ANM-01-016-002}

**R2. Todo segmento $[a,b]$, con $a\le b$, es compacto.** No partiremos de Heine–Borel: debemos producir una reducción finita para una cubierta arbitraria. Fijamos $U:I\to\mathcal P(\mathbb R)$ que cubre $[a,b]$, y registramos hasta dónde hay cobertura finita:

$$S=\{x\in[a,b]:[a,x]\text{ admite una subcubierta finita de }U\}.$$

Este conjunto guarda una propiedad existencial, no una elección $x\mapsto J_x$. Contiene $a$, porque algún abierto de la cubierta contiene ese punto y cubre el segmento degenerado $[a,a]$. Está acotado por $b$. La completitud de C00 proporciona $c=\sup S$ con $a\le c\le b$.

La cobertura proporciona un índice $i_c$ con $c\in U_{i_c}$. La apertura da $r>0$ tal que $(c-r,c+r)\subseteq U_{i_c}$. La propiedad aproximante del supremo entrega $t\in S$ con $c-r/2<t\le c$: si no hubiera tal $t$, el real $c-r/2<c$ sería una cota superior de $S$, contradicción.

Fijamos una subcubierta finita $J_t$ de $[a,t]$, disponible para este único $t$. Definimos

$$d=\min(b,c+r/2).$$

Entonces $c\le d\le b$, y para todo $z\in[t,d]$ tenemos $c-r<z<c+r$, pues $t>c-r/2$ y $d\le c+r/2$. Así $[t,d]\subseteq U_{i_c}$. Los índices $J_t\cup\{i_c\}$ son finitos y cubren $[a,d]$: hasta $t$ actúa la cobertura anterior, y desde $t$ hasta $d$ el nuevo abierto. Por definición, $d\in S$.

![Esquema del caso hipotético c<b. Con c−r/2<t≤c y d=min(b,c+r/2), el conjunto Jt más el índice que cubre c cubre \[a,d\]. Por tanto d∈S; si c<b, d>c contradice la cota. Cuando c=b, la misma construcción da d=b∈S. Las posiciones son ilustrativas.](../../assets/books/anm/C16/C16-F02.svg){#fig-anm-c16-f02 fig-alt="Esquema del caso hipotético c&lt;b. Con c−r/2&lt;t≤c y d=min(b,c+r/2), el conjunto Jt más el índice que cubre c cubre \[a,d\]. Por tanto d∈S; si c&lt;b, d&gt;c contradice la cota. Cuando c=b, la misma construcción da d=b∈S. Las posiciones son ilustrativas."}

Como $c$ es cota superior, $d\le c$. Si $c<b$, la fórmula del mínimo da $d>c$, contradicción. Por tanto $c=b$. Pero la prueba aporta algo más que esa igualdad: el punto construido $d$ pertenece a $S$ y, al ser $c=b$, también $d=b$. Hemos demostrado $b\in S$, cuya definición entrega la subcubierta finita buscada de $[a,b]$.

El último paso es esencial. De $\sup S=b$ no se deduce por sí solo $b\in S$; $S=[a,b)$, cuando $a<b$, ilustra ese error lógico. Aquí la apertura de un abierto que contiene el extremo final cierra la cobertura. El mismo argumento incluye $a=b$, aunque R1 ya resuelve ese caso; si la notación $[a,b]$ se usa con $a>b$, denota el vacío y R1 vuelve a aplicarse.

No se eligió un abierto para cada punto ni una subcubierta para cada segmento. Se fijaron sólo los testigos asociados a $c$ y a un $t$ concreto. El intervalo y la completitud localizaron la frontera; la apertura impidió que la reducción finita se detuviera antes del final y permitió alcanzarlo.

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-016-009}

¿Qué registra el conjunto $S$ en la prueba de compacidad de $[a,b]$?

[]{#MA-MSOL-ANM-01-016-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

**Respuesta.**

Los $x\in[a,b]$ para los que el segmento $[a,x]$ admite alguna subcubierta finita de la cubierta dada. Registra existencia, sin elegir una subcubierta para cada $x$.

**Fundamento en la sección 16.2.**

**R2. Todo segmento $[a,b]$, con $a\le b$, es compacto.** No partiremos de Heine–Borel: debemos producir una reducción finita para una cubierta arbitraria. Fijamos $U:I\to\mathcal P(\mathbb R)$ que cubre $[a,b]$, y registramos hasta dónde hay cobertura finita:

$$S=\{x\in[a,b]:[a,x]\text{ admite una subcubierta finita de }U\}.$$

Este conjunto guarda una propiedad existencial, no una elección $x\mapsto J_x$. Contiene $a$, porque algún abierto de la cubierta contiene ese punto y cubre el segmento degenerado $[a,a]$. Está acotado por $b$. La completitud de C00 proporciona $c=\sup S$ con $a\le c\le b$.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-016-010}

¿Por qué $S$ es no vacío y acotado superiormente?

[]{#MA-MSOL-ANM-01-016-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

**Respuesta.**

$a\in S$ porque un solo abierto que cubre $a$ cubre $[a,a]$. Además $S\subseteq[a,b]$, así $b$ es cota superior.

**Fundamento en la sección 16.2.**

Este conjunto guarda una propiedad existencial, no una elección $x\mapsto J_x$. Contiene $a$, porque algún abierto de la cubierta contiene ese punto y cubre el segmento degenerado $[a,a]$. Está acotado por $b$. La completitud de C00 proporciona $c=\sup S$ con $a\le c\le b$.

La cobertura proporciona un índice $i_c$ con $c\in U_{i_c}$. La apertura da $r>0$ tal que $(c-r,c+r)\subseteq U_{i_c}$. La propiedad aproximante del supremo entrega $t\in S$ con $c-r/2<t\le c$: si no hubiera tal $t$, el real $c-r/2<c$ sería una cota superior de $S$, contradicción.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-016-011}

¿Qué proporciona la apertura de un miembro que contiene $c=\sup S$?

[]{#MA-MSOL-ANM-01-016-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

**Respuesta.**

Un radio $r>0$ con $(c-r,c+r)\subseteq U_{i_c}$. Ese margen permitirá ampliar una cobertura finita que llegue a un $t$ suficientemente próximo a $c$.

**Fundamento en la sección 16.2.**

Este conjunto guarda una propiedad existencial, no una elección $x\mapsto J_x$. Contiene $a$, porque algún abierto de la cubierta contiene ese punto y cubre el segmento degenerado $[a,a]$. Está acotado por $b$. La completitud de C00 proporciona $c=\sup S$ con $a\le c\le b$.

La cobertura proporciona un índice $i_c$ con $c\in U_{i_c}$. La apertura da $r>0$ tal que $(c-r,c+r)\subseteq U_{i_c}$. La propiedad aproximante del supremo entrega $t\in S$ con $c-r/2<t\le c$: si no hubiera tal $t$, el real $c-r/2<c$ sería una cota superior de $S$, contradicción.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-016-012}

¿Por qué existe $t\in S$ con $c-r/2<t\le c$?

[]{#MA-MSOL-ANM-01-016-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

**Respuesta.**

Porque $c-r/2<c$ no puede ser cota superior de $S$. La negación de ser cota produce un $t\in S$ mayor, y $t\le c$ por ser $c$ cota.

**Fundamento en la sección 16.2.**

Entonces $c\le d\le b$, y para todo $z\in[t,d]$ tenemos $c-r<z<c+r$, pues $t>c-r/2$ y $d\le c+r/2$. Así $[t,d]\subseteq U_{i_c}$. Los índices $J_t\cup\{i_c\}$ son finitos y cubren $[a,d]$: hasta $t$ actúa la cobertura anterior, y desde $t$ hasta $d$ el nuevo abierto. Por definición, $d\in S$.

Como $c$ es cota superior, $d\le c$. Si $c<b$, la fórmula del mínimo da $d>c$, contradicción. Por tanto $c=b$. Pero la prueba aporta algo más que esa igualdad: el punto construido $d$ pertenece a $S$ y, al ser $c=b$, también $d=b$. Hemos demostrado $b\in S$, cuya definición entrega la subcubierta finita buscada de $[a,b]$.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-016-013}

¿Qué impide que $d=\min(b,c+r/2)$ salga del segmento?

[]{#MA-MSOL-ANM-01-016-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

**Respuesta.**

La fórmula da $c\le d\le b$, y $c\ge a$. Así $d\in[a,b]$, a la vez que todo $[t,d]$ queda dentro de la bola de radio $r$ alrededor de $c$.

**Fundamento en la sección 16.2.**

Fijamos una subcubierta finita $J_t$ de $[a,t]$, disponible para este único $t$. Definimos

$$d=\min(b,c+r/2).$$

Entonces $c\le d\le b$, y para todo $z\in[t,d]$ tenemos $c-r<z<c+r$, pues $t>c-r/2$ y $d\le c+r/2$. Así $[t,d]\subseteq U_{i_c}$. Los índices $J_t\cup\{i_c\}$ son finitos y cubren $[a,d]$: hasta $t$ actúa la cobertura anterior, y desde $t$ hasta $d$ el nuevo abierto. Por definición, $d\in S$.

Como $c$ es cota superior, $d\le c$. Si $c<b$, la fórmula del mínimo da $d>c$, contradicción. Por tanto $c=b$. Pero la prueba aporta algo más que esa igualdad: el punto construido $d$ pertenece a $S$ y, al ser $c=b$, también $d=b$. Hemos demostrado $b\in S$, cuya definición entrega la subcubierta finita buscada de $[a,b]$.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-016-014}

¿Por qué $J_t\cup\{i_c\}$ cubre $[a,d]$?

[]{#MA-MSOL-ANM-01-016-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

**Respuesta.**

$J_t$ cubre $[a,t]$ y $U_{i_c}$ cubre $[t,d]$. Como $a\le t\le d$, la unión de esos dos segmentos es $[a,d]$; los índices siguen siendo finitos.

**Fundamento en la sección 16.2.**

La cobertura proporciona un índice $i_c$ con $c\in U_{i_c}$. La apertura da $r>0$ tal que $(c-r,c+r)\subseteq U_{i_c}$. La propiedad aproximante del supremo entrega $t\in S$ con $c-r/2<t\le c$: si no hubiera tal $t$, el real $c-r/2<c$ sería una cota superior de $S$, contradicción.

Fijamos una subcubierta finita $J_t$ de $[a,t]$, disponible para este único $t$. Definimos

$$d=\min(b,c+r/2).$$

Entonces $c\le d\le b$, y para todo $z\in[t,d]$ tenemos $c-r<z<c+r$, pues $t>c-r/2$ y $d\le c+r/2$. Así $[t,d]\subseteq U_{i_c}$. Los índices $J_t\cup\{i_c\}$ son finitos y cubren $[a,d]$: hasta $t$ actúa la cobertura anterior, y desde $t$ hasta $d$ el nuevo abierto. Por definición, $d\in S$.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-016-015}

¿De $\sup S=b$ se deduce siempre $b\in S$?

[]{#MA-MSOL-ANM-01-016-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

**Respuesta.**

No. $S=[a,b)$ con $a<b$ tiene supremo $b$ pero no lo contiene. En R2 se obtiene además $d\in S$ y, una vez $c=b$, $d=b$, lo que sí prueba pertenencia.

**Fundamento en la sección 16.2.**

Como $c$ es cota superior, $d\le c$. Si $c<b$, la fórmula del mínimo da $d>c$, contradicción. Por tanto $c=b$. Pero la prueba aporta algo más que esa igualdad: el punto construido $d$ pertenece a $S$ y, al ser $c=b$, también $d=b$. Hemos demostrado $b\in S$, cuya definición entrega la subcubierta finita buscada de $[a,b]$.

El último paso es esencial. De $\sup S=b$ no se deduce por sí solo $b\in S$; $S=[a,b)$, cuando $a<b$, ilustra ese error lógico. Aquí la apertura de un abierto que contiene el extremo final cierra la cobertura. El mismo argumento incluye $a=b$, aunque R1 ya resuelve ese caso; si la notación $[a,b]$ se usa con $a>b$, denota el vacío y R1 vuelve a aplicarse.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-016-016}

¿Qué cambia para $a=b$ o para $a>b$?

[]{#MA-MSOL-ANM-01-016-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

**Respuesta.**

Si $a=b$, el segmento es singleton y basta un abierto que cubra ese punto. Con $a>b$, la notación de intervalo describe el vacío, compacto por la subfamilia vacía.

**Fundamento en la sección 16.2.**

El último paso es esencial. De $\sup S=b$ no se deduce por sí solo $b\in S$; $S=[a,b)$, cuando $a<b$, ilustra ese error lógico. Aquí la apertura de un abierto que contiene el extremo final cierra la cobertura. El mismo argumento incluye $a=b$, aunque R1 ya resuelve ese caso; si la notación $[a,b]$ se usa con $a>b$, denota el vacío y R1 vuelve a aplicarse.

No se eligió un abierto para cada punto ni una subcubierta para cada segmento. Se fijaron sólo los testigos asociados a $c$ y a un $t$ concreto. El intervalo y la completitud localizaron la frontera; la apertura impidió que la reducción finita se detuviera antes del final y permitió alcanzarlo.

</details>

### Ejercicios de la sección 16.2

#### Ejercicio 6. Registrar cobertura finita

[]{#MA-EX-ANM-01-016-006}

Para una cubierta arbitraria de $[a,b]$, $a\le b$, define $S$ como en R2 y justifica $a\in S$, existencia de su supremo y pertenencia del supremo al segmento.

[]{#MA-SOL-ANM-01-016-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

**Respuesta.**

La cobertura da un índice con $a\in U_i$, y ese único miembro cubre $[a,a]$. Por tanto $a\in S$ y $S$ no es vacío. Como $S\subseteq[a,b]$, $b$ es cota superior. Completitud da $c=\sup S$; $a\le c$ porque $a\in S$ y $c\le b$ porque $b$ es cota. Así $c\in[a,b]$ y puede aplicarse la cobertura a ese punto. No se supone que $c\in S$.

**Fundamento en la sección 16.2.**

Este conjunto guarda una propiedad existencial, no una elección $x\mapsto J_x$. Contiene $a$, porque algún abierto de la cubierta contiene ese punto y cubre el segmento degenerado $[a,a]$. Está acotado por $b$. La completitud de C00 proporciona $c=\sup S$ con $a\le c\le b$.

La cobertura proporciona un índice $i_c$ con $c\in U_{i_c}$. La apertura da $r>0$ tal que $(c-r,c+r)\subseteq U_{i_c}$. La propiedad aproximante del supremo entrega $t\in S$ con $c-r/2<t\le c$: si no hubiera tal $t$, el real $c-r/2<c$ sería una cota superior de $S$, contradicción.

</details>

#### Ejercicio 7. Prolongar con un solo abierto

[]{#MA-EX-ANM-01-016-007}

Si $c=\sup S$, $(c-r,c+r)\subseteq U_{i_c}$ y $t\in S$ satisface $c-r/2<t\le c$, prueba que $d=\min(b,c+r/2)$ pertenece a $S$. Identifica qué índices cubren cada tramo.

[]{#MA-SOL-ANM-01-016-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

**Respuesta.**

$c\le d\le b$ y $t\le c$, así $a\le t\le d\le b$. Para $z\in[t,d]$, $z\ge t>c-r/2>c-r$ y $z\le d\le c+r/2<c+r$, luego $z\in U_{i_c}$. Por $t\in S$ hay un conjunto finito $J_t$ que cubre $[a,t]$. La unión $J_t\cup\{i_c\}$ es finita y cubre $[a,t]\cup[t,d]=[a,d]$. Esto es exactamente la propiedad que define $d\in S$. Sólo se fijó una subcubierta asociada al $t$ concreto.

**Fundamento en la sección 16.2.**

Fijamos una subcubierta finita $J_t$ de $[a,t]$, disponible para este único $t$. Definimos

$$d=\min(b,c+r/2).$$

Entonces $c\le d\le b$, y para todo $z\in[t,d]$ tenemos $c-r<z<c+r$, pues $t>c-r/2$ y $d\le c+r/2$. Así $[t,d]\subseteq U_{i_c}$. Los índices $J_t\cup\{i_c\}$ son finitos y cubren $[a,d]$: hasta $t$ actúa la cobertura anterior, y desde $t$ hasta $d$ el nuevo abierto. Por definición, $d\in S$.

Como $c$ es cota superior, $d\le c$. Si $c<b$, la fórmula del mínimo da $d>c$, contradicción. Por tanto $c=b$. Pero la prueba aporta algo más que esa igualdad: el punto construido $d$ pertenece a $S$ y, al ser $c=b$, también $d=b$. Hemos demostrado $b\in S$, cuya definición entrega la subcubierta finita buscada de $[a,b]$.

</details>

#### Ejercicio 8. El extremo omitido de una prueba

[]{#MA-EX-ANM-01-016-008}

Una prueba concluye $\sup S=b$ y afirma «por tanto $b\in S$». Refuta ese paso lógico y completa el argumento correcto de R2 para obtener la subcubierta de todo el segmento.

[]{#MA-SOL-ANM-01-016-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Con $a<b$, $S=[a,b)$ tiene supremo $b$ y no lo contiene; la igualdad de supremo no implica pertenencia. En R2 se construye además $d=\min(b,c+r/2)\in S$, usando una cobertura de $[a,t]$ y un abierto que contiene a $c$. Si $c<b$, ese $d$ sería mayor que $c$, contradicción con la cota. Luego $c=b$, y la misma fórmula da $d=b$. Como ya se probó $d\in S$, ahora sí $b\in S$. Su definición suministra los índices finitos que cubren $[a,b]$.

**Retorno visual.** Véase [C16-F02](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. No elegir una subcubierta por segmento

[]{#MA-EX-ANM-01-016-009}

Explica por qué definir $S$ mediante «existe una subcubierta finita de $[a,x]$» no obliga a construir una función $x\mapsto J_x$. Enumera los testigos concretos necesarios en R2.

[]{#MA-SOL-ANM-01-016-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

**Respuesta.**

El predicado existencial determina qué puntos están en $S$ sin asociarles un testigo elegido. Primero se usa un índice que cubre $a$ para probar $a\in S$. Después se fija un índice $i_c$ que cubre el supremo, un radio de apertura y un único $t\in S$ próximo al supremo. Sólo para ese $t$ se instancia la existencia de $J_t$. La lista finita $J_t\cup\{i_c\}$ concluye la prueba. No se forma una familia de elecciones sobre todos los $x\in S$.

**Fundamento en la sección 16.2.**

Este conjunto guarda una propiedad existencial, no una elección $x\mapsto J_x$. Contiene $a$, porque algún abierto de la cubierta contiene ese punto y cubre el segmento degenerado $[a,a]$. Está acotado por $b$. La completitud de C00 proporciona $c=\sup S$ con $a\le c\le b$.

La cobertura proporciona un índice $i_c$ con $c\in U_{i_c}$. La apertura da $r>0$ tal que $(c-r,c+r)\subseteq U_{i_c}$. La propiedad aproximante del supremo entrega $t\in S$ con $c-r/2<t\le c$: si no hubiera tal $t$, el real $c-r/2<c$ sería una cota superior de $S$, contradicción.

</details>

#### Ejercicio 10. Cobertura del intervalo abierto frente al cerrado

[]{#MA-EX-ANM-01-016-010}

¿Puede la familia $U_n=(1/(n+2),2)$ cubrir $[0,1]$? Compara con su acción sobre $(0,1)$ y explica por qué no contradice R2.

[]{#MA-SOL-ANM-01-016-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

**Respuesta.**

No cubre $[0,1]$ porque ningún miembro contiene cero. Sí cubre $(0,1)$: dado un punto positivo, algún recíproco $1/(n+2)$ es menor que él. Para una subfamilia finita no vacía con máximo índice $m$, $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de su unión $U_m$. Por eso el intervalo abierto no es compacto. R2 cuantifica sobre cubiertas que realmente cubren todo el segmento cerrado; esta familia no satisface esa premisa.

**Fundamento en la sección 16.2.**

Este conjunto guarda una propiedad existencial, no una elección $x\mapsto J_x$. Contiene $a$, porque algún abierto de la cubierta contiene ese punto y cubre el segmento degenerado $[a,a]$. Está acotado por $b$. La completitud de C00 proporciona $c=\sup S$ con $a\le c\le b$.

La cobertura proporciona un índice $i_c$ con $c\in U_{i_c}$. La apertura da $r>0$ tal que $(c-r,c+r)\subseteq U_{i_c}$. La propiedad aproximante del supremo entrega $t\in S$ con $c-r/2<t\le c$: si no hubiera tal $t$, el real $c-r/2<c$ sería una cota superior de $S$, contradicción.

</details>
## 16.3. Heredar compacidad sin perder índices

[]{#MA-SEC-ANM-01-016-003}

Una parte de un compacto puede dejar escapar puntos de adherencia. Antes de conocer Heine–Borel necesitamos identificar qué partes conservan la propiedad de cubiertas.

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

Retenemos los índices originales que aparecen allí; la proyección $(i,0)\mapsto i$ conserva finitud. Para un $x\in A$, ningún abierto adicional puede ser el único que lo cubra: $x\in F$ implica $x\notin V$. Por tanto un índice original de la lista finita cubre $x$. Los índices retenidos dan una subcubierta finita de la cubierta original de $A$. Puesto que ésta era arbitraria, $A$ es compacto.

El abierto añadido debe cubrir **todo** $K\setminus A$, no sólo la zona próxima a un extremo de un segmento ambiente. Y se retiran índices, no necesariamente un valor de abierto de una colección sin etiquetas: si un valor estaba repetido, las etiquetas mantienen qué miembros procedían de la cubierta original.

**Primera reutilización.** Si $F$ es cerrado real, $K\cap F$ es compacto por R3. Todo cerrado acotado contenido en un segmento será, por tanto, candidato para la dirección suficiente de Heine–Borel. Para $K=[-2,2]$ y $F=(-\infty,-1]\cup[1,\infty)$ obtenemos el compacto $[-2,-1]\cup[1,2]$, aunque tenga dos piezas.

La hipótesis de cerradura no se puede quitar. El subconjunto $(0,1)$ de $[0,1]$ admite la cubierta

$$U_n=(1/(n+2),2),\qquad n\in\mathbb N.$$

Para cada $x\in(0,1)$, arquimedianidad permite $n$ con $1/(n+2)<x$, de modo que la familia cubre. Una subfamilia finita no vacía tiene índice máximo $m$, y su unión es $U_m$ porque los abiertos aumentan con $n$. El punto $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de esa unión. Ninguna subfamilia finita cubre el dominio; la vacía tampoco. Éste es el escape que la cerradura relativa impediría.

![Un=(1/(n+2),2), n≥0, cubre (0,1). Toda subfamilia finita no vacía tiene máximo m y omite x=1/\[2(m+2)\]. Arriba se ilustra m=3; abajo el acercamiento de umbrales a cero es esquemático. El caso de subfamilia vacía se descarta por no vacuidad de K.](../../assets/books/anm/C16/C16-F03.svg){#fig-anm-c16-f03 fig-alt="Un=(1/(n+2),2), n≥0, cubre (0,1). Toda subfamilia finita no vacía tiene máximo m y omite x=1/\[2(m+2)\]. Arriba se ilustra m=3; abajo el acercamiento de umbrales a cero es esquemático. El caso de subfamilia vacía se descarta por no vacuidad de K."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-016-017}

¿Qué representación se usa para un cerrado relativo $A\subseteq K$?

[]{#MA-MSOL-ANM-01-016-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

**Respuesta.**

$A=K\cap F$ con $F$ cerrado en toda la recta. Su complemento ambiental $\mathbb R\setminus F$ es abierto y cubre los puntos de $K$ que no están en $A$.

**Fundamento en la sección 16.3.**

Una parte de un compacto puede dejar escapar puntos de adherencia. Antes de conocer Heine–Borel necesitamos identificar qué partes conservan la propiedad de cubiertas.

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-016-018}

¿Por qué se añade todo $\mathbb R\setminus F$ a la cubierta de $A$?

[]{#MA-MSOL-ANM-01-016-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

**Respuesta.**

Para cubrir cada punto de $K\setminus A$. Añadir sólo una porción próxima a un extremo podría dejar puntos de ese complemento sin cubrir.

**Fundamento en la sección 16.3.**

Una parte de un compacto puede dejar escapar puntos de adherencia. Antes de conocer Heine–Borel necesitamos identificar qué partes conservan la propiedad de cubiertas.

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-016-019}

¿Para qué sirve etiquetar el índice nuevo de la cubierta ampliada?

[]{#MA-MSOL-ANM-01-016-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

**Respuesta.**

Para que sea distinto de todos los originales, aunque algún valor de abierto coincida. Así se puede retirar el índice añadido sin perder la procedencia de los miembros originales.

**Fundamento en la sección 16.3.**

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-016-020}

¿Por qué el abierto añadido no es necesario para cubrir puntos de $A$?

[]{#MA-MSOL-ANM-01-016-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

**Respuesta.**

Todo $x\in A$ está en $F$, así no pertenece a $\mathbb R\setminus F$. En una subcubierta ampliada debe estar cubierto por algún índice original.

**Fundamento en la sección 16.3.**

Una parte de un compacto puede dejar escapar puntos de adherencia. Antes de conocer Heine–Borel necesitamos identificar qué partes conservan la propiedad de cubiertas.

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-016-021}

¿Todo subconjunto de un compacto es compacto?

[]{#MA-MSOL-ANM-01-016-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

**Respuesta.**

No. $(0,1)\subseteq[0,1]$ no lo es. La cubierta $U_n=(1/(n+2),2)$ cubre el intervalo abierto pero ninguna subfamilia finita lo cubre.

**Fundamento en la sección 16.3.**

La hipótesis de cerradura no se puede quitar. El subconjunto $(0,1)$ de $[0,1]$ admite la cubierta

$$U_n=(1/(n+2),2),\qquad n\in\mathbb N.$$

Para cada $x\in(0,1)$, arquimedianidad permite $n$ con $1/(n+2)<x$, de modo que la familia cubre. Una subfamilia finita no vacía tiene índice máximo $m$, y su unión es $U_m$ porque los abiertos aumentan con $n$. El punto $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de esa unión. Ninguna subfamilia finita cubre el dominio; la vacía tampoco. Éste es el escape que la cerradura relativa impediría.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-016-022}

¿Qué punto queda fuera de una subfamilia finita de esa cubierta, con índice máximo $m$?

[]{#MA-MSOL-ANM-01-016-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

**Respuesta.**

$x=1/(2(m+2))$ pertenece a $(0,1)$ y es menor que el extremo izquierdo $1/(m+2)$ del mayor abierto seleccionado. Está fuera de toda la unión finita.

**Fundamento en la sección 16.3.**

Para cada $x\in(0,1)$, arquimedianidad permite $n$ con $1/(n+2)<x$, de modo que la familia cubre. Una subfamilia finita no vacía tiene índice máximo $m$, y su unión es $U_m$ porque los abiertos aumentan con $n$. El punto $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de esa unión. Ninguna subfamilia finita cubre el dominio; la vacía tampoco. Éste es el escape que la cerradura relativa impediría.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-016-023}

¿Es compacta la intersección de un compacto con un cerrado real?

[]{#MA-MSOL-ANM-01-016-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

**Respuesta.**

Sí. Es cerrada relativa al compacto por la representación como intersección, y R3 transmite compacidad.

**Fundamento en la sección 16.3.**

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-016-024}

¿La herencia de compacidad exige que el cerrado relativo sea intervalo?

[]{#MA-MSOL-ANM-01-016-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

**Respuesta.**

No. Sólo exige cerrado relativo. Por ejemplo $[-2,-1]\cup[1,2]$ es un cerrado relativo del compacto $[-2,2]$ y es compacto aunque tenga un hueco.

**Fundamento en la sección 16.3.**

**Primera reutilización.** Si $F$ es cerrado real, $K\cap F$ es compacto por R3. Todo cerrado acotado contenido en un segmento será, por tanto, candidato para la dirección suficiente de Heine–Borel. Para $K=[-2,2]$ y $F=(-\infty,-1]\cup[1,\infty)$ obtenemos el compacto $[-2,-1]\cup[1,2]$, aunque tenga dos piezas.

La hipótesis de cerradura no se puede quitar. El subconjunto $(0,1)$ de $[0,1]$ admite la cubierta

$$U_n=(1/(n+2),2),\qquad n\in\mathbb N.$$

Para cada $x\in(0,1)$, arquimedianidad permite $n$ con $1/(n+2)<x$, de modo que la familia cubre. Una subfamilia finita no vacía tiene índice máximo $m$, y su unión es $U_m$ porque los abiertos aumentan con $n$. El punto $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de esa unión. Ninguna subfamilia finita cubre el dominio; la vacía tampoco. Éste es el escape que la cerradura relativa impediría.

</details>

### Ejercicios de la sección 16.3

#### Ejercicio 11. Cubrir el complemento completo

[]{#MA-EX-ANM-01-016-011}

Para heredar compacidad de $A=K\cap F$, una prueba añade sólo $V=(M-1,M+1)\cap(\mathbb R\setminus F)$ cuando $K=[-M,M]$. Muestra con $M=2$, $F=\{0\}$ y una cubierta de $A$ que la familia ampliada puede no cubrir $K$. Repara el abierto añadido.

[]{#MA-SOL-ANM-01-016-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

**Respuesta.**

Aquí $A=\{0\}$. La familia con un solo miembro $U=(-1/4,1/4)$ cubre $A$, y el abierto propuesto es $(1,3)$. La unión de ambos no contiene, por ejemplo, $-1\in K$. No cubre $K$, así no puede aplicarse compacidad del segmento. La reparación es añadir todo $V=\mathbb R\setminus F$. Si un punto de $K$ no está en $F$, lo cubre $V$; si está en $F$, pertenece a $A$ y lo cubre la familia original. $V$ no toca $A$, por lo que sus índices se pueden retirar después de obtener una subcubierta finita ampliada.

**Fundamento en la sección 16.3.**

**R3. Un cerrado relativo de un compacto es compacto.** Sea $K$ compacto, $A\subseteq K$ cerrado relativo. Por C04/C14 existe un cerrado real $F$ con $A=K\cap F$. Fijamos una cubierta abierta arbitraria $(U_i)_{i\in I}$ de $A$. Puede no cubrir $K\setminus A$. Para cubrir lo que falta añadimos el abierto completo $V=\mathbb R\setminus F$.

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

</details>

#### Ejercicio 12. Cerrar dos piezas dentro de un segmento

[]{#MA-EX-ANM-01-016-012}

Prueba compacidad de $A=[-2,-1]\cup[1,2]$ como cerrado relativo de $K=[-2,2]$, sin usar todavía Heine–Borel. Describe el abierto añadido en la prueba de herencia.

[]{#MA-SOL-ANM-01-016-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

**Respuesta.**

$K$ es compacto por R2. Tomamos $F=(-\infty,-1]\cup[1,\infty)$, cerrado real porque su complemento $(-1,1)$ es abierto. Entonces $A=K\cap F$. R3 da compacidad. Para una cubierta de $A$, se añade $\mathbb R\setminus F=(-1,1)$, que cubre precisamente la zona de $K$ no cubierta por pertenencia a $A$; después una subcubierta finita de $K$ conserva suficientes índices originales para cubrir $A$, pues el abierto añadido no toca sus puntos.

**Fundamento en la sección 16.3.**

El abierto añadido debe cubrir **todo** $K\setminus A$, no sólo la zona próxima a un extremo de un segmento ambiente. Y se retiran índices, no necesariamente un valor de abierto de una colección sin etiquetas: si un valor estaba repetido, las etiquetas mantienen qué miembros procedían de la cubierta original.

**Primera reutilización.** Si $F$ es cerrado real, $K\cap F$ es compacto por R3. Todo cerrado acotado contenido en un segmento será, por tanto, candidato para la dirección suficiente de Heine–Borel. Para $K=[-2,2]$ y $F=(-\infty,-1]\cup[1,\infty)$ obtenemos el compacto $[-2,-1]\cup[1,2]$, aunque tenga dos piezas.

</details>

#### Ejercicio 13. Etiquetas y abiertos repetidos

[]{#MA-EX-ANM-01-016-013}

Desarrolla el sistema de índices al añadir un abierto $V$ a una cubierta $(U_i)_{i\in I}$ y al retirar ese miembro tras aplicar compacidad. Permite que $V$ coincida como conjunto con algún $U_i$.

[]{#MA-SOL-ANM-01-016-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

**Respuesta.**

Usamos $I^*=(I\times\{0\})\cup\{(\varnothing,1)\}$ y definimos $W_{(i,0)}=U_i$, $W_{(\varnothing,1)}=V$. Las etiquetas $0\ne1$ garantizan índice excepcional distinto. Una subcubierta finita $J^*$ determina $J=\{i\in I:(i,0)\in J^*\}$, finito por proyección de una parte finita. Para $x\in A$ con $A\cap V=\varnothing$, un índice que lo cubre no es el excepcional; proviene de $J$ y $x\in U_i$. La coincidencia de valores abiertos no cambia la prueba: se retiran sólo índices etiquetados, no todos los miembros de igual valor.

**Fundamento en la sección 16.3.**

Si $x\in K$, o está en $F$, y entonces pertenece a $A$ y a algún $U_i$, o está en $V$. Por ello la familia ampliada cubre $K$. Para que el índice adicional no colisione con uno antiguo, etiquetamos los índices originales como $(i,0)$ y reservamos un índice nuevo $*$ con etiqueta distinta. En la familia ampliada, $(i,0)$ conserva el valor $U_i$ y $*$ tiene valor $V$. Compacidad entrega un conjunto finito de índices ampliados.

Retenemos los índices originales que aparecen allí; la proyección $(i,0)\mapsto i$ conserva finitud. Para un $x\in A$, ningún abierto adicional puede ser el único que lo cubra: $x\in F$ implica $x\notin V$. Por tanto un índice original de la lista finita cubre $x$. Los índices retenidos dan una subcubierta finita de la cubierta original de $A$. Puesto que ésta era arbitraria, $A$ es compacto.

</details>

#### Ejercicio 14. Un subconjunto que pierde compacidad

[]{#MA-EX-ANM-01-016-014}

Prueba mediante una cubierta que $(0,1)$ no es compacto, aunque esté dentro del compacto $[0,1]$. Trata las subfamilias vacías y no vacías.

[]{#MA-SOL-ANM-01-016-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

**Respuesta.**

La cubierta $U_n=(1/(n+2),2)$ cubre $(0,1)$ por arquimedianidad. La subfamilia vacía no cubre su punto $1/2$. Si $J\subseteq\mathbb N$ es finito no vacío, su máximo $m$ da unión $U_m$, pues los miembros son crecientes. El punto $x=1/(2(m+2))$ es positivo y menor que uno pero está por debajo de $1/(m+2)$, luego no pertenece a ningún abierto seleccionado. No existe subcubierta finita. La hipótesis de cerrado relativo de R3 no puede omitirse.

**Retorno visual.** Véase [C16-F03](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 16.3.**

**Primera reutilización.** Si $F$ es cerrado real, $K\cap F$ es compacto por R3. Todo cerrado acotado contenido en un segmento será, por tanto, candidato para la dirección suficiente de Heine–Borel. Para $K=[-2,2]$ y $F=(-\infty,-1]\cup[1,\infty)$ obtenemos el compacto $[-2,-1]\cup[1,2]$, aunque tenga dos piezas.

La hipótesis de cerradura no se puede quitar. El subconjunto $(0,1)$ de $[0,1]$ admite la cubierta

$$U_n=(1/(n+2),2),\qquad n\in\mathbb N.$$

Para cada $x\in(0,1)$, arquimedianidad permite $n$ con $1/(n+2)<x$, de modo que la familia cubre. Una subfamilia finita no vacía tiene índice máximo $m$, y su unión es $U_m$ porque los abiertos aumentan con $n$. El punto $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de esa unión. Ninguna subfamilia finita cubre el dominio; la vacía tampoco. Éste es el escape que la cerradura relativa impediría.

</details>

#### Ejercicio 15. Intersección con un cerrado

[]{#MA-EX-ANM-01-016-015}

Prueba que $K\cap F$ es compacto cuando $K$ lo es y $F$ es cerrado real. Deduce que la intersección de toda familia no vacía de compactos reales es compacta, una vez disponible R4. Separa el caso de familia vacía.

[]{#MA-SOL-ANM-01-016-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

La intersección $K\cap F$ es cerrada relativa a $K$, y R3 la hace compacta. Para una familia de compactos con al menos un miembro, R4 hace a todos cerrados reales. Su intersección $A$ es cerrada, porque su complemento es unión de complementos abiertos, y está contenida en un miembro fijo $K_0$. Es $K_0\cap A$, por tanto compacta por la primera afirmación; esto vale incluso si el conjunto resultante es vacío. Para una familia sin miembros, la intersección ambiental es $\mathbb R$, que no es compacta. La no vacuidad requerida es la de la familia de índices, no la del conjunto intersección.

</details>
## 16.4. Heine–Borel: cerrar las dos direcciones

[]{#MA-SEC-ANM-01-016-004}

**R4. En la recta real, compacto equivale a cerrado y acotado.** Probaremos las dos necesidades desde cubiertas y la suficiencia desde R2/R3. No intervienen sucesiones ni una equivalencia secuencial anticipada.

**Acotación necesaria.** Sea $K$ compacto no vacío. La cubierta $U_n=(-(n+1),n+1)$ cubre toda la recta y también $K$. Una subcubierta finita debe tener índices no vacíos. Si $m$ es su máximo, $K\subseteq U_m\subseteq[-(m+1),m+1]$. Para $K=\varnothing$ sirven las cotas cero. Aquí el máximo se toma después de obtener finitud, no sobre la familia infinita original.

**Cerradura necesaria.** Fijemos $p\notin K$, con $K$ no vacío. Los abiertos determinados por fórmula

$$V_n=\{x\in\mathbb R:|x-p|>1/(n+1)\},\qquad n\in\mathbb N,$$

son uniones de dos rayos abiertos. Cubren $K$: para cada $x\in K$, $|x-p|>0$, y algún recíproco $1/(n+1)$ es menor que esa distancia. Una subcubierta finita con máximo índice $m$ da $K\subseteq V_m$, pues los $V_n$ aumentan. Por consiguiente, la bola de centro $p$ y radio $1/(m+1)>0$ no toca $K$. Se ha construido una vecindad del punto exterior dentro del complemento. Como $p$ era arbitrario, $\mathbb R\setminus K$ es abierto y $K$ cerrado. Si $K$ es vacío, su complemento es la recta y ya es abierto.

**Suficiencia.** Supongamos $K$ cerrado y acotado. Hay $M>0$ tal que $K\subseteq[-M,M]$. Ese segmento es compacto por R2. La igualdad $K=[-M,M]\cap K$ presenta a $K$ como cerrado relativo del segmento, y R3 prueba su compacidad. Se incluyen los conjuntos vacíos.

![Heine–Borel real exige cerradura y acotación. El segmento cerrado cumple ambas; (0,1\] pierde cerradura y R pierde acotación. La unión de los dos segmentos cumple ambas aunque tiene un hueco. Las pruebas generales preceden a la clasificación.](../../assets/books/anm/C16/C16-F04.svg){#fig-anm-c16-f04 fig-alt="Heine–Borel real exige cerradura y acotación. El segmento cerrado cumple ambas; (0,1\] pierde cerradura y R pierde acotación. La unión de los dos segmentos cumple ambas aunque tiene un hueco. Las pruebas generales preceden a la clasificación."}

Heine–Borel es un teorema que identifica una propiedad universal de cubiertas con dos condiciones geométricas; no redefinimos retrospectivamente la compacidad. Tampoco lo aplicamos a espacios arbitrarios: aquí el orden completo y la geometría real son parte del argumento.

La acotación sola falla en $(0,1)$; la cerradura sola falla en $\mathbb R$. $[-2,-1]\cup[1,2]$ es compacto y no conexo, mientras $(0,1)$ es conexo por C15 y no compacto. Son propiedades distintas. El conjunto

$$K=\{0\}\cup\{1/(n+1):n\in\mathbb N\}$$

también es compacto. Está en $[0,1]$. Para probar cerradura sin una recíproca secuencial, fijamos $p\notin K$. Si $p$ está fuera de $[0,1]$, una bola pequeña evita el segmento. Si $0<p\le1$, una cola de los recíprocos es menor que $p/2$ y queda lejos de $p$; los términos anteriores son una lista finita, ninguno igual a $p$, y el mínimo de sus distancias junto con $p/2$ es positivo. La mitad de ese mínimo da una bola disjunta de $K$. El complemento es abierto; Heine–Borel concluye compacidad. Quitar cero deja un conjunto acotado no cerrado, porque los recíprocos entran en toda vecindad de cero, y destruye compacidad.

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-016-025}

¿Qué dos propiedades identifica Heine–Borel con la compacidad real?

[]{#MA-MSOL-ANM-01-016-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

**Respuesta.**

Cerradura en $\mathbb R$ y acotación. Se demuestran ambas necesidades por cubiertas y la suficiencia por segmento compacto y herencia a un cerrado relativo.

**Fundamento en la sección 16.4.**

**Suficiencia.** Supongamos $K$ cerrado y acotado. Hay $M>0$ tal que $K\subseteq[-M,M]$. Ese segmento es compacto por R2. La igualdad $K=[-M,M]\cap K$ presenta a $K$ como cerrado relativo del segmento, y R3 prueba su compacidad. Se incluyen los conjuntos vacíos.

Heine–Borel es un teorema que identifica una propiedad universal de cubiertas con dos condiciones geométricas; no redefinimos retrospectivamente la compacidad. Tampoco lo aplicamos a espacios arbitrarios: aquí el orden completo y la geometría real son parte del argumento.

La acotación sola falla en $(0,1)$; la cerradura sola falla en $\mathbb R$. $[-2,-1]\cup[1,2]$ es compacto y no conexo, mientras $(0,1)$ es conexo por C15 y no compacto. Son propiedades distintas. El conjunto

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-016-026}

¿En qué momento se toma el máximo de índices para probar acotación?

[]{#MA-MSOL-ANM-01-016-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

**Respuesta.**

Después de obtener una subcubierta finita de $U_n=(-(n+1),n+1)$. Para $K$ no vacío sus índices no son vacíos y tienen máximo; no se toma máximo de toda $\mathbb N$.

**Fundamento en la sección 16.4.**

**R4. En la recta real, compacto equivale a cerrado y acotado.** Probaremos las dos necesidades desde cubiertas y la suficiencia desde R2/R3. No intervienen sucesiones ni una equivalencia secuencial anticipada.

**Acotación necesaria.** Sea $K$ compacto no vacío. La cubierta $U_n=(-(n+1),n+1)$ cubre toda la recta y también $K$. Una subcubierta finita debe tener índices no vacíos. Si $m$ es su máximo, $K\subseteq U_m\subseteq[-(m+1),m+1]$. Para $K=\varnothing$ sirven las cotas cero. Aquí el máximo se toma después de obtener finitud, no sobre la familia infinita original.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-016-027}

¿Por qué $V_n=\{x:|x-p|>1/(n+1)\}$ es abierto real?

[]{#MA-MSOL-ANM-01-016-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

**Respuesta.**

Es la unión de los rayos $(-\infty,p-1/(n+1))$ y $(p+1/(n+1),\infty)$, ambos abiertos.

**Fundamento en la sección 16.4.**

son uniones de dos rayos abiertos. Cubren $K$: para cada $x\in K$, $|x-p|>0$, y algún recíproco $1/(n+1)$ es menor que esa distancia. Una subcubierta finita con máximo índice $m$ da $K\subseteq V_m$, pues los $V_n$ aumentan. Por consiguiente, la bola de centro $p$ y radio $1/(m+1)>0$ no toca $K$. Se ha construido una vecindad del punto exterior dentro del complemento. Como $p$ era arbitrario, $\mathbb R\setminus K$ es abierto y $K$ cerrado. Si $K$ es vacío, su complemento es la recta y ya es abierto.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-016-028}

¿Por qué los $V_n$ cubren $K$ cuando $p\notin K$?

[]{#MA-MSOL-ANM-01-016-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

**Respuesta.**

Para cada $x\in K$, su distancia positiva $|x-p|$ supera algún recíproco $1/(n+1)$ por arquimedianidad. Entonces $x\in V_n$.

**Fundamento en la sección 16.4.**

**Cerradura necesaria.** Fijemos $p\notin K$, con $K$ no vacío. Los abiertos determinados por fórmula

$$V_n=\{x\in\mathbb R:|x-p|>1/(n+1)\},\qquad n\in\mathbb N,$$

son uniones de dos rayos abiertos. Cubren $K$: para cada $x\in K$, $|x-p|>0$, y algún recíproco $1/(n+1)$ es menor que esa distancia. Una subcubierta finita con máximo índice $m$ da $K\subseteq V_m$, pues los $V_n$ aumentan. Por consiguiente, la bola de centro $p$ y radio $1/(m+1)>0$ no toca $K$. Se ha construido una vecindad del punto exterior dentro del complemento. Como $p$ era arbitrario, $\mathbb R\setminus K$ es abierto y $K$ cerrado. Si $K$ es vacío, su complemento es la recta y ya es abierto.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-016-029}

¿Qué radio exterior se obtiene del máximo $m$ de una subcubierta de $V_n$?

[]{#MA-MSOL-ANM-01-016-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

**Respuesta.**

$1/(m+1)>0$. Como $K\subseteq V_m$, ningún punto a distancia menor que ese radio de $p$ está en $K$. Da una bola dentro del complemento.

**Fundamento en la sección 16.4.**

son uniones de dos rayos abiertos. Cubren $K$: para cada $x\in K$, $|x-p|>0$, y algún recíproco $1/(n+1)$ es menor que esa distancia. Una subcubierta finita con máximo índice $m$ da $K\subseteq V_m$, pues los $V_n$ aumentan. Por consiguiente, la bola de centro $p$ y radio $1/(m+1)>0$ no toca $K$. Se ha construido una vecindad del punto exterior dentro del complemento. Como $p$ era arbitrario, $\mathbb R\setminus K$ es abierto y $K$ cerrado. Si $K$ es vacío, su complemento es la recta y ya es abierto.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-016-030}

¿Cómo se prueba compacidad de un cerrado acotado sin sucesiones?

[]{#MA-MSOL-ANM-01-016-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

**Respuesta.**

Se encierra en $[-M,M]$, compacto por R2. El conjunto es cerrado relativo a ese segmento y R3 lo hace compacto.

**Fundamento en la sección 16.4.**

**Suficiencia.** Supongamos $K$ cerrado y acotado. Hay $M>0$ tal que $K\subseteq[-M,M]$. Ese segmento es compacto por R2. La igualdad $K=[-M,M]\cap K$ presenta a $K$ como cerrado relativo del segmento, y R3 prueba su compacidad. Se incluyen los conjuntos vacíos.

Heine–Borel es un teorema que identifica una propiedad universal de cubiertas con dos condiciones geométricas; no redefinimos retrospectivamente la compacidad. Tampoco lo aplicamos a espacios arbitrarios: aquí el orden completo y la geometría real son parte del argumento.

La acotación sola falla en $(0,1)$; la cerradura sola falla en $\mathbb R$. $[-2,-1]\cup[1,2]$ es compacto y no conexo, mientras $(0,1)$ es conexo por C15 y no compacto. Son propiedades distintas. El conjunto

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-016-031}

¿Compacidad y conexidad coinciden en la recta?

[]{#MA-MSOL-ANM-01-016-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

**Respuesta.**

No. $[-2,-1]\cup[1,2]$ es compacto y no conexo. $(0,1)$ es conexo y no compacto. Las condiciones de cubierta y ausencia de huecos son distintas.

**Fundamento en la sección 16.4.**

**Suficiencia.** Supongamos $K$ cerrado y acotado. Hay $M>0$ tal que $K\subseteq[-M,M]$. Ese segmento es compacto por R2. La igualdad $K=[-M,M]\cap K$ presenta a $K$ como cerrado relativo del segmento, y R3 prueba su compacidad. Se incluyen los conjuntos vacíos.

Heine–Borel es un teorema que identifica una propiedad universal de cubiertas con dos condiciones geométricas; no redefinimos retrospectivamente la compacidad. Tampoco lo aplicamos a espacios arbitrarios: aquí el orden completo y la geometría real son parte del argumento.

La acotación sola falla en $(0,1)$; la cerradura sola falla en $\mathbb R$. $[-2,-1]\cup[1,2]$ es compacto y no conexo, mientras $(0,1)$ es conexo por C15 y no compacto. Son propiedades distintas. El conjunto

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-016-032}

¿Por qué añadir cero a los recíprocos restaura compacidad?

[]{#MA-MSOL-ANM-01-016-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

**Respuesta.**

El conjunto resultante es acotado y cerrado: cero incluye el punto de acumulación de la cola, y todo punto exterior se separa de una cola lejana y de un prefijo finito por un radio positivo. Heine–Borel da compacidad.

**Fundamento en la sección 16.4.**

también es compacto. Está en $[0,1]$. Para probar cerradura sin una recíproca secuencial, fijamos $p\notin K$. Si $p$ está fuera de $[0,1]$, una bola pequeña evita el segmento. Si $0<p\le1$, una cola de los recíprocos es menor que $p/2$ y queda lejos de $p$; los términos anteriores son una lista finita, ninguno igual a $p$, y el mínimo de sus distancias junto con $p/2$ es positivo. La mitad de ese mínimo da una bola disjunta de $K$. El complemento es abierto; Heine–Borel concluye compacidad. Quitar cero deja un conjunto acotado no cerrado, porque los recíprocos entran en toda vecindad de cero, y destruye compacidad.

</details>

### Ejercicios de la sección 16.4

#### Ejercicio 16. Acotación desde una cubierta creciente

[]{#MA-EX-ANM-01-016-016}

Prueba que todo compacto real es acotado usando sólo la cubierta $U_n=(-(n+1),n+1)$. Incluye el vacío.

[]{#MA-SOL-ANM-01-016-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

**Respuesta.**

El vacío está en $[0,0]$. Para $K\ne\varnothing$, la familia cubre toda la recta por arquimedianidad y en particular $K$. Compacidad entrega índices finitos $J$, que no pueden ser vacíos. Tienen máximo $m$. Cada $U_j$ seleccionado está contenido en $U_m$, así $K\subseteq(-(m+1),m+1)\subseteq[-(m+1),m+1]$. Los extremos son cotas reales. No se usó ninguna sucesión fabricada de puntos lejanos.

**Fundamento en la sección 16.4.**

**R4. En la recta real, compacto equivale a cerrado y acotado.** Probaremos las dos necesidades desde cubiertas y la suficiencia desde R2/R3. No intervienen sucesiones ni una equivalencia secuencial anticipada.

**Acotación necesaria.** Sea $K$ compacto no vacío. La cubierta $U_n=(-(n+1),n+1)$ cubre toda la recta y también $K$. Una subcubierta finita debe tener índices no vacíos. Si $m$ es su máximo, $K\subseteq U_m\subseteq[-(m+1),m+1]$. Para $K=\varnothing$ sirven las cotas cero. Aquí el máximo se toma después de obtener finitud, no sobre la familia infinita original.

</details>

#### Ejercicio 17. Un radio exterior por índices finitos

[]{#MA-EX-ANM-01-016-017}

Fija $p\notin K$, con $K$ compacto no vacío. Usando $V_n=\{x:|x-p|>1/(n+1)\}$, demuestra que alguna bola positiva alrededor de $p$ evita $K$.

[]{#MA-SOL-ANM-01-016-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

**Respuesta.**

Cada $V_n$ es unión de dos rayos abiertos. Para cualquier $x\in K$, la distancia $|x-p|$ es positiva y supera algún recíproco, así la familia cubre $K$. Compacidad entrega una subfamilia finita no vacía; con máximo índice $m$, su unión está en $V_m$ porque los miembros crecen. Por tanto todos los puntos de $K$ distan de $p$ más que $1/(m+1)$. La bola abierta de ese radio en $p$ no toca $K$. Como se puede hacer para cada punto exterior, el complemento de $K$ es abierto y $K$ cerrado.

**Fundamento en la sección 16.4.**

**Acotación necesaria.** Sea $K$ compacto no vacío. La cubierta $U_n=(-(n+1),n+1)$ cubre toda la recta y también $K$. Una subcubierta finita debe tener índices no vacíos. Si $m$ es su máximo, $K\subseteq U_m\subseteq[-(m+1),m+1]$. Para $K=\varnothing$ sirven las cotas cero. Aquí el máximo se toma después de obtener finitud, no sobre la familia infinita original.

**Cerradura necesaria.** Fijemos $p\notin K$, con $K$ no vacío. Los abiertos determinados por fórmula

$$V_n=\{x\in\mathbb R:|x-p|>1/(n+1)\},\qquad n\in\mathbb N,$$

son uniones de dos rayos abiertos. Cubren $K$: para cada $x\in K$, $|x-p|>0$, y algún recíproco $1/(n+1)$ es menor que esa distancia. Una subcubierta finita con máximo índice $m$ da $K\subseteq V_m$, pues los $V_n$ aumentan. Por consiguiente, la bola de centro $p$ y radio $1/(m+1)>0$ no toca $K$. Se ha construido una vecindad del punto exterior dentro del complemento. Como $p$ era arbitrario, $\mathbb R\setminus K$ es abierto y $K$ cerrado. Si $K$ es vacío, su complemento es la recta y ya es abierto.

</details>

#### Ejercicio 18. Reconocer cinco dominios

[]{#MA-EX-ANM-01-016-018}

Usa Heine–Borel para decidir compacidad de $[0,1]$, $(0,1]$, $\mathbb R$, $\{-1,1\}$ y $\mathbb Q\cap[0,1]$. Justifica el fallo cuando corresponda.

[]{#MA-SOL-ANM-01-016-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

$[0,1]$ es cerrado y acotado, compacto. $(0,1]$ es acotado pero no cerrado, pues cero es adherente por los recíprocos y falta; no es compacto. $\mathbb R$ es cerrado pero no acotado, no compacto. El conjunto finito $\{-1,1\}$ es cerrado y acotado, compacto. Los racionales de $[0,1]$ son acotados pero no cerrados: el irracional $p=\sqrt2/2\in(0,1)$ no pertenece y toda bola suya suficientemente pequeña dentro de $(0,1)$ contiene racionales por densidad. Toda bola, por contener una más pequeña de ese tipo, toca el conjunto. No es compacto. La interfaz algebraica de raíz e irracionalidad viene de C04/C10.

</details>

#### Ejercicio 19. La cola y el prefijo

[]{#MA-EX-ANM-01-016-019}

Prueba cerradura y compacidad de $K=\{0\}\cup\{1/(n+1):n\in\mathbb N\}$ sin usar la recíproca secuencial. Para un exterior positivo, construye el radio desde una cola y un prefijo finito.

[]{#MA-SOL-ANM-01-016-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

$K\subseteq[0,1]$. Si $p\notin K$ y $p<0$ o $p>1$, la mitad de su distancia al segmento da una bola exterior. En el caso restante $0<p<1$ y $p$ no es ningún recíproco, elegimos $N\ge1$ con $1/(N+1)<p/2$. Para todo $n\ge N$, $t_n=1/(n+1)<p/2$, luego $|p-t_n|>p/2$; cero también dista $p$. Los valores $|p-t_n|$ para $n<N$ son una familia finita no vacía positiva. Sea $d$ el mínimo de ellos y $p/2$, positivo. La bola de radio $d/2$ no contiene cero, prefijo ni cola. El complemento es abierto, por tanto $K$ cerrado; al ser acotado, Heine–Borel lo hace compacto. No se eligió una sucesión de testigos arbitrarios de vecindades.

**Retorno visual.** Véase [C16-F04](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 20. Dos propiedades distintas

[]{#MA-EX-ANM-01-016-020}

Da un compacto real no conexo y un conexo real no compacto. Justifica ambas propiedades con los resultados correspondientes.

[]{#MA-SOL-ANM-01-016-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

**Respuesta.**

$[-2,-1]\cup[1,2]$ es cerrado y acotado, compacto por R4; se separa por los rayos a ambos lados de cero, o no es intervalo por el punto omitido cero entre $-1$ y $1$, así no conexo por C15. $(0,1)$ es intervalo, conexo por C15; no es cerrado porque cero es adherente y falta, así no compacto por Heine–Borel. Los ejemplos muestran que ninguna de las dos propiedades implica la otra.

**Fundamento en la sección 16.4.**

**Suficiencia.** Supongamos $K$ cerrado y acotado. Hay $M>0$ tal que $K\subseteq[-M,M]$. Ese segmento es compacto por R2. La igualdad $K=[-M,M]\cap K$ presenta a $K$ como cerrado relativo del segmento, y R3 prueba su compacidad. Se incluyen los conjuntos vacíos.

Heine–Borel es un teorema que identifica una propiedad universal de cubiertas con dos condiciones geométricas; no redefinimos retrospectivamente la compacidad. Tampoco lo aplicamos a espacios arbitrarios: aquí el orden completo y la geometría real son parte del argumento.

La acotación sola falla en $(0,1)$; la cerradura sola falla en $\mathbb R$. $[-2,-1]\cup[1,2]$ es compacto y no conexo, mientras $(0,1)$ es conexo por C15 y no compacto. Son propiedades distintas. El conjunto

</details>
## 16.5. Sucesiones: extraer y seleccionar son tareas distintas

[]{#MA-SEC-ANM-01-016-005}

**Compacidad secuencial.** $K$ es secuencialmente compacto si toda sucesión dada $(x_n)$ de puntos de $K$ tiene una subsucesión $(x_{\varphi(n)})$ que converge a un punto $\ell\in K$, con $\varphi:\mathbb N\to\mathbb N$ estrictamente creciente. El requisito de pertenencia del límite es decisivo. Si $K$ es vacío, no hay sucesión con todos sus términos en él y la condición universal es vacía.

**R5, dirección directa.** Todo compacto real es secuencialmente compacto. Por R4 es cerrado y acotado. Una sucesión dada de puntos de $K$ es acotada, y Bolzano–Weierstrass de C08 proporciona una subsucesión convergente en $\mathbb R$. Su límite está en $K$: si estuviera fuera, la apertura del complemento daría una bola exterior que la convergencia obligaría a ocupar a términos que pertenecen a $K$, contradicción. La extracción actúa sobre una sucesión ya dada mediante el mecanismo de C08, con bisección e índices naturales mínimos; no fabrica puntos de un conjunto arbitrario.

En $(0,1]$, la sucesión $x_n=1/(n+1)$ converge a cero y toda subsucesión también. Por unicidad, ninguna converge a un miembro de $(0,1]$. Ese dominio no es secuencialmente compacto. Añadir cero restaura cerradura y compacidad, y por R5 toda sucesión dada tiene una extracción adecuada, no sólo esta sucesión especial.

**Recíproca con alcance.** Para un conjunto arbitrario, probar «secuencialmente compacto implica compacto» requiere, en el argumento siguiente, la hipótesis adicional $\mathrm{CC}(\mathbb R)$: toda familia numerable dada de subconjuntos reales no vacíos admite una selección simultánea. Esta hipótesis es local al enunciado condicional; no se adopta globalmente.

Si $K$ no fuera acotado, los conjuntos

$$E_n=\{x\in K:|x|>n\}$$

serían no vacíos. Bajo $\mathrm{CC}(\mathbb R)$ escogemos una sucesión $x_n\in E_n$. Toda subsucesión con índices crecientes cumple $|x_{\varphi(k)}|>\varphi(k)\ge k$, luego es no acotada y no puede converger; contradice compacidad secuencial. Así $K$ es acotado.

Si no fuera cerrado, habría un punto $p\notin K$ adherente a $K$. Los conjuntos $F_n=K\cap(p-1/(n+1),p+1/(n+1))$ serían no vacíos. La misma hipótesis permite una sucesión $z_n\in F_n$, que converge a $p$. Compacidad secuencial entrega una subsucesión con límite $\ell\in K$; como toda subsucesión de una convergente conserva el límite, también converge a $p$. Unicidad da $\ell=p$, contradicción. Así $K$ es cerrado, y R4 lo hace compacto.

Las dos fabricaciones de rutas son el gasto exacto de selección; no lo es la posterior extracción. Si $K\ne\varnothing$ viene con una sobreyección **dada** $e:\mathbb N\to K$, la recíproca se prueba sin ese gasto adicional: en cada $E_n$ o $F_n$ se toma el menor índice $j$ con $e(j)$ en el conjunto requerido, que existe por sobreyectividad y buen orden natural. Esa regla determina la ruta. El vacío se trata aparte. No inferimos una enumeración de un conjunto real arbitrario.

![La ruta an=1/(n+1) y cada subsucesión convergen a cero. En (0,1\] ese límite queda fuera; al añadir cero al conjunto de recíprocos queda dentro de un compacto. Sólo se muestran los primeros términos. La recíproca secuencial general requiere CC(R), mientras una enumeración sobreyectiva dada permite mínimos de índices.](../../assets/books/anm/C16/C16-F05.svg){#fig-anm-c16-f05 fig-alt="La ruta an=1/(n+1) y cada subsucesión convergen a cero. En (0,1\] ese límite queda fuera; al añadir cero al conjunto de recíprocos queda dentro de un compacto. Sólo se muestran los primeros términos. La recíproca secuencial general requiere CC(R), mientras una enumeración sobreyectiva dada permite mínimos de índices."}

Por tanto disponemos de compacto $\Longleftrightarrow$ cerrado y acotado y de compacto $\Longrightarrow$ secuencialmente compacto sin selección adicional en estas pruebas. La equivalencia con compacidad secuencial se establece bajo $\mathrm{CC}(\mathbb R)$ o con una enumeración dada del dominio no vacío. No afirmamos una equivalencia universal sin su premisa. Ésta es la misma disciplina de selección usada en C13/C14.

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-016-033}

¿Dónde debe quedar el límite en la definición de compacidad secuencial?

[]{#MA-MSOL-ANM-01-016-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

**Respuesta.**

Dentro de $K$, no sólo en $\mathbb R$. Una subsucesión convergente a un punto exterior no satisface la definición.

**Fundamento en la sección 16.5.**

**Compacidad secuencial.** $K$ es secuencialmente compacto si toda sucesión dada $(x_n)$ de puntos de $K$ tiene una subsucesión $(x_{\varphi(n)})$ que converge a un punto $\ell\in K$, con $\varphi:\mathbb N\to\mathbb N$ estrictamente creciente. El requisito de pertenencia del límite es decisivo. Si $K$ es vacío, no hay sucesión con todos sus términos en él y la condición universal es vacía.

**R5, dirección directa.** Todo compacto real es secuencialmente compacto. Por R4 es cerrado y acotado. Una sucesión dada de puntos de $K$ es acotada, y Bolzano–Weierstrass de C08 proporciona una subsucesión convergente en $\mathbb R$. Su límite está en $K$: si estuviera fuera, la apertura del complemento daría una bola exterior que la convergencia obligaría a ocupar a términos que pertenecen a $K$, contradicción. La extracción actúa sobre una sucesión ya dada mediante el mecanismo de C08, con bisección e índices naturales mínimos; no fabrica puntos de un conjunto arbitrario.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-016-034}

¿Qué aporta Bolzano–Weierstrass de C08 para una sucesión dada en un compacto?

[]{#MA-MSOL-ANM-01-016-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

**Respuesta.**

Como está acotada, aporta una subsucesión convergente en $\mathbb R$. La cerradura del compacto es el paso adicional que coloca el límite en $K$.

**Fundamento en la sección 16.5.**

**R5, dirección directa.** Todo compacto real es secuencialmente compacto. Por R4 es cerrado y acotado. Una sucesión dada de puntos de $K$ es acotada, y Bolzano–Weierstrass de C08 proporciona una subsucesión convergente en $\mathbb R$. Su límite está en $K$: si estuviera fuera, la apertura del complemento daría una bola exterior que la convergencia obligaría a ocupar a términos que pertenecen a $K$, contradicción. La extracción actúa sobre una sucesión ya dada mediante el mecanismo de C08, con bisección e índices naturales mínimos; no fabrica puntos de un conjunto arbitrario.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-016-035}

¿Por qué la dirección compacta a secuencialmente compacta no fabrica una ruta por selección?

[]{#MA-MSOL-ANM-01-016-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

**Respuesta.**

La sucesión de entrada ya está dada. C08 extrae índices de esa sucesión y después se usa cerradura; no se escoge un punto de cada uno de infinitos conjuntos arbitrarios.

**Fundamento en la sección 16.5.**

**Compacidad secuencial.** $K$ es secuencialmente compacto si toda sucesión dada $(x_n)$ de puntos de $K$ tiene una subsucesión $(x_{\varphi(n)})$ que converge a un punto $\ell\in K$, con $\varphi:\mathbb N\to\mathbb N$ estrictamente creciente. El requisito de pertenencia del límite es decisivo. Si $K$ es vacío, no hay sucesión con todos sus términos en él y la condición universal es vacía.

**R5, dirección directa.** Todo compacto real es secuencialmente compacto. Por R4 es cerrado y acotado. Una sucesión dada de puntos de $K$ es acotada, y Bolzano–Weierstrass de C08 proporciona una subsucesión convergente en $\mathbb R$. Su límite está en $K$: si estuviera fuera, la apertura del complemento daría una bola exterior que la convergencia obligaría a ocupar a términos que pertenecen a $K$, contradicción. La extracción actúa sobre una sucesión ya dada mediante el mecanismo de C08, con bisección e índices naturales mínimos; no fabrica puntos de un conjunto arbitrario.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-016-036}

¿Por qué $1/(n+1)$ refuta compacidad secuencial de $(0,1]$?

[]{#MA-MSOL-ANM-01-016-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

**Respuesta.**

Toda subsucesión también converge a cero, que no pertenece al dominio. Por unicidad no puede tener otro límite dentro de $(0,1]$.

**Fundamento en la sección 16.5.**

En $(0,1]$, la sucesión $x_n=1/(n+1)$ converge a cero y toda subsucesión también. Por unicidad, ninguna converge a un miembro de $(0,1]$. Ese dominio no es secuencialmente compacto. Añadir cero restaura cerradura y compacidad, y por R5 toda sucesión dada tiene una extracción adecuada, no sólo esta sucesión especial.

**Recíproca con alcance.** Para un conjunto arbitrario, probar «secuencialmente compacto implica compacto» requiere, en el argumento siguiente, la hipótesis adicional $\mathrm{CC}(\mathbb R)$: toda familia numerable dada de subconjuntos reales no vacíos admite una selección simultánea. Esta hipótesis es local al enunciado condicional; no se adopta globalmente.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-016-037}

¿Qué familia se usa si un secuencialmente compacto fuera no acotado?

[]{#MA-MSOL-ANM-01-016-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

**Respuesta.**

$E_n=\{x\in K:|x|>n\}$, todos no vacíos. Fabricar una sucesión $x_n\in E_n$ requiere aquí CC(R), o una enumeración dada que permita mínimos de índices.

**Fundamento en la sección 16.5.**

**Recíproca con alcance.** Para un conjunto arbitrario, probar «secuencialmente compacto implica compacto» requiere, en el argumento siguiente, la hipótesis adicional $\mathrm{CC}(\mathbb R)$: toda familia numerable dada de subconjuntos reales no vacíos admite una selección simultánea. Esta hipótesis es local al enunciado condicional; no se adopta globalmente.

Si $K$ no fuera acotado, los conjuntos

$$E_n=\{x\in K:|x|>n\}$$

serían no vacíos. Bajo $\mathrm{CC}(\mathbb R)$ escogemos una sucesión $x_n\in E_n$. Toda subsucesión con índices crecientes cumple $|x_{\varphi(k)}|>\varphi(k)\ge k$, luego es no acotada y no puede converger; contradice compacidad secuencial. Así $K$ es acotado.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-016-038}

¿Qué familia se usa si hay un punto adherente $p\notin K$?

[]{#MA-MSOL-ANM-01-016-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

**Respuesta.**

$F_n=K\cap(p-1/(n+1),p+1/(n+1))$, todos no vacíos. Una selección simultánea da una ruta hacia $p$, y después compacidad secuencial y unicidad llevan a contradicción.

**Fundamento en la sección 16.5.**

Si no fuera cerrado, habría un punto $p\notin K$ adherente a $K$. Los conjuntos $F_n=K\cap(p-1/(n+1),p+1/(n+1))$ serían no vacíos. La misma hipótesis permite una sucesión $z_n\in F_n$, que converge a $p$. Compacidad secuencial entrega una subsucesión con límite $\ell\in K$; como toda subsucesión de una convergente conserva el límite, también converge a $p$. Unicidad da $\ell=p$, contradicción. Así $K$ es cerrado, y R4 lo hace compacto.

Las dos fabricaciones de rutas son el gasto exacto de selección; no lo es la posterior extracción. Si $K\ne\varnothing$ viene con una sobreyección **dada** $e:\mathbb N\to K$, la recíproca se prueba sin ese gasto adicional: en cada $E_n$ o $F_n$ se toma el menor índice $j$ con $e(j)$ en el conjunto requerido, que existe por sobreyectividad y buen orden natural. Esa regla determina la ruta. El vacío se trata aparte. No inferimos una enumeración de un conjunto real arbitrario.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-016-039}

¿Cómo una sobreyección dada $e:\mathbb N\to K$ reemplaza ese gasto de selección?

[]{#MA-MSOL-ANM-01-016-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

**Respuesta.**

Para cada conjunto requerido se toma el menor índice $j$ con $e(j)$ en él. Existe por sobreyectividad y no vacuidad; el buen orden natural determina un valor único. No se inventa una enumeración de $K$.

**Fundamento en la sección 16.5.**

Las dos fabricaciones de rutas son el gasto exacto de selección; no lo es la posterior extracción. Si $K\ne\varnothing$ viene con una sobreyección **dada** $e:\mathbb N\to K$, la recíproca se prueba sin ese gasto adicional: en cada $E_n$ o $F_n$ se toma el menor índice $j$ con $e(j)$ en el conjunto requerido, que existe por sobreyectividad y buen orden natural. Esa regla determina la ruta. El vacío se trata aparte. No inferimos una enumeración de un conjunto real arbitrario.

Por tanto disponemos de compacto $\Longleftrightarrow$ cerrado y acotado y de compacto $\Longrightarrow$ secuencialmente compacto sin selección adicional en estas pruebas. La equivalencia con compacidad secuencial se establece bajo $\mathrm{CC}(\mathbb R)$ o con una enumeración dada del dominio no vacío. No afirmamos una equivalencia universal sin su premisa. Ésta es la misma disciplina de selección usada en C13/C14.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-016-040}

¿Cuál es el alcance de la recíproca secuencial demostrada?

[]{#MA-MSOL-ANM-01-016-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

**Respuesta.**

Para dominios reales arbitrarios se establece bajo CC(R) explícita, local al enunciado. También se demuestra sin esa hipótesis extra cuando el dominio no vacío viene con enumeración sobreyectiva dada. El vacío se trata por separado.

**Fundamento en la sección 16.5.**

Las dos fabricaciones de rutas son el gasto exacto de selección; no lo es la posterior extracción. Si $K\ne\varnothing$ viene con una sobreyección **dada** $e:\mathbb N\to K$, la recíproca se prueba sin ese gasto adicional: en cada $E_n$ o $F_n$ se toma el menor índice $j$ con $e(j)$ en el conjunto requerido, que existe por sobreyectividad y buen orden natural. Esa regla determina la ruta. El vacío se trata aparte. No inferimos una enumeración de un conjunto real arbitrario.

Por tanto disponemos de compacto $\Longleftrightarrow$ cerrado y acotado y de compacto $\Longrightarrow$ secuencialmente compacto sin selección adicional en estas pruebas. La equivalencia con compacidad secuencial se establece bajo $\mathrm{CC}(\mathbb R)$ o con una enumeración dada del dominio no vacío. No afirmamos una equivalencia universal sin su premisa. Ésta es la misma disciplina de selección usada en C13/C14.

</details>

### Ejercicios de la sección 16.5

#### Ejercicio 21. Acotar la ruta y retener su límite

[]{#MA-EX-ANM-01-016-021}

Demuestra que un compacto real es secuencialmente compacto usando Bolzano–Weierstrass de C08. Identifica el paso que coloca el límite en el conjunto.

[]{#MA-SOL-ANM-01-016-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

R4 hace cerrado y acotado a $K$. Dada una sucesión de puntos de $K$, es acotada y C08 entrega una subsucesión convergente en la recta a $\ell$. Si $\ell\notin K$, cerradura da un radio $r>0$ cuya bola en $\ell$ no toca $K$. Convergencia obliga a que los términos de la subsucesión estén eventualmente dentro de esa bola, contradiciendo que todos están en $K$. Por tanto $\ell\in K$. Si $K$ es vacío, no existe tal sucesión y la condición universal se cumple. No se fabrica la sucesión inicial; era un dato.

</details>

#### Ejercicio 22. Un límite exterior para todas las extracciones

[]{#MA-EX-ANM-01-016-022}

Prueba que $(0,1]$ no es secuencialmente compacto mediante una sucesión concreta. No basta decir que esa sucesión converge fuera: debes tratar todas sus subsucesiones.

[]{#MA-SOL-ANM-01-016-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

**Respuesta.**

Tomamos $x_n=1/(n+1)$, todos en $(0,1]$, con límite cero. Para un selector estrictamente creciente $\varphi$, $\varphi(k)\ge k$ por inducción; entonces $0<x_{\varphi(k)}\le1/(k+1)\to0$. Toda subsucesión converge a cero. Si alguna convergiera a $\ell\in(0,1]$, unicidad del límite daría $\ell=0$, imposible. No hay subsucesión con límite en el dominio, refutando su compacidad secuencial.

**Retorno visual.** Véase [C16-F05](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 16.5.**

**Compacidad secuencial.** $K$ es secuencialmente compacto si toda sucesión dada $(x_n)$ de puntos de $K$ tiene una subsucesión $(x_{\varphi(n)})$ que converge a un punto $\ell\in K$, con $\varphi:\mathbb N\to\mathbb N$ estrictamente creciente. El requisito de pertenencia del límite es decisivo. Si $K$ es vacío, no hay sucesión con todos sus términos en él y la condición universal es vacía.

**R5, dirección directa.** Todo compacto real es secuencialmente compacto. Por R4 es cerrado y acotado. Una sucesión dada de puntos de $K$ es acotada, y Bolzano–Weierstrass de C08 proporciona una subsucesión convergente en $\mathbb R$. Su límite está en $K$: si estuviera fuera, la apertura del complemento daría una bola exterior que la convergencia obligaría a ocupar a términos que pertenecen a $K$, contradicción. La extracción actúa sobre una sucesión ya dada mediante el mecanismo de C08, con bisección e índices naturales mínimos; no fabrica puntos de un conjunto arbitrario.

</details>

#### Ejercicio 23. Una fabricación que necesita permiso

[]{#MA-EX-ANM-01-016-023}

Un argumento dice: «Si $K$ no es acotado, para cada $n$ hay $x_n\in K$ con $|x_n|>n$; luego tenemos una sucesión». Distingue las afirmaciones y completa la contradicción bajo CC(R) explícita.

[]{#MA-SOL-ANM-01-016-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

**Respuesta.**

No acotación da que cada $E_n=\{x\in K:|x|>n\}$ es no vacío. Eso es $\forall n\exists x$, no aún una sola función que elija todos los valores. Bajo CC(R) sí existe una sucesión $x_n\in E_n$. Si $K$ fuera secuencialmente compacto, alguna subsucesión $x_{\varphi(k)}$ convergería y por tanto sería acotada por un $M$. Pero $|x_{\varphi(k)}|>\varphi(k)\ge k$, que supera $M$ para algún natural por arquimedianidad. Contradicción. Se prueba acotación bajo la hipótesis indicada; no se adopta CC(R) globalmente.

**Fundamento en la sección 16.5.**

**Recíproca con alcance.** Para un conjunto arbitrario, probar «secuencialmente compacto implica compacto» requiere, en el argumento siguiente, la hipótesis adicional $\mathrm{CC}(\mathbb R)$: toda familia numerable dada de subconjuntos reales no vacíos admite una selección simultánea. Esta hipótesis es local al enunciado condicional; no se adopta globalmente.

Si $K$ no fuera acotado, los conjuntos

$$E_n=\{x\in K:|x|>n\}$$

serían no vacíos. Bajo $\mathrm{CC}(\mathbb R)$ escogemos una sucesión $x_n\in E_n$. Toda subsucesión con índices crecientes cumple $|x_{\varphi(k)}|>\varphi(k)\ge k$, luego es no acotada y no puede converger; contradice compacidad secuencial. Así $K$ es acotado.

</details>

#### Ejercicio 24. La ruta hacia un punto omitido

[]{#MA-EX-ANM-01-016-024}

Bajo CC(R), prueba que un secuencialmente compacto es cerrado. Declara la familia seleccionada y todos los límites utilizados.

[]{#MA-SOL-ANM-01-016-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

**Respuesta.**

Si $K$ no fuese cerrado, habría $p\notin K$ adherente. Los $F_n=K\cap(p-1/(n+1),p+1/(n+1))$ son no vacíos. CC(R) da una sucesión $z_n\in F_n$. La cota $|z_n-p|<1/(n+1)$ prueba $z_n\to p$. Compacidad secuencial da una subsucesión con límite $\ell\in K$. Toda subsucesión de la convergente también converge a $p$; unicidad da $\ell=p$, contradicción. La selección fue la fabricación de $z_n$, mientras la extracción posterior usa la propiedad secuencial. Por ello $K$ es cerrado bajo la premisa declarada.

**Fundamento en la sección 16.5.**

Si no fuera cerrado, habría un punto $p\notin K$ adherente a $K$. Los conjuntos $F_n=K\cap(p-1/(n+1),p+1/(n+1))$ serían no vacíos. La misma hipótesis permite una sucesión $z_n\in F_n$, que converge a $p$. Compacidad secuencial entrega una subsucesión con límite $\ell\in K$; como toda subsucesión de una convergente conserva el límite, también converge a $p$. Unicidad da $\ell=p$, contradicción. Así $K$ es cerrado, y R4 lo hace compacto.

Las dos fabricaciones de rutas son el gasto exacto de selección; no lo es la posterior extracción. Si $K\ne\varnothing$ viene con una sobreyección **dada** $e:\mathbb N\to K$, la recíproca se prueba sin ese gasto adicional: en cada $E_n$ o $F_n$ se toma el menor índice $j$ con $e(j)$ en el conjunto requerido, que existe por sobreyectividad y buen orden natural. Esa regla determina la ruta. El vacío se trata aparte. No inferimos una enumeración de un conjunto real arbitrario.

</details>

#### Ejercicio 25. Una enumeración dada determina testigos

[]{#MA-EX-ANM-01-016-025}

Sea $K\ne\varnothing$ secuencialmente compacto y sea $e:\mathbb N\to K$ una sobreyección dada. Prueba que $K$ es cerrado y acotado, y por ello compacto, sin invocar CC(R).

[]{#MA-SOL-ANM-01-016-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Si $K$ fuera no acotado, cada $E_n=\{x\in K:|x|>n\}$ sería no vacío. La sobreyectividad hace no vacío $\{j:e(j)\in E_n\}$. Tomamos su menor índice $j_n$, determinado por buen orden, y $x_n=e(j_n)$. Cualquier subsucesión tiene $|x_{\varphi(k)}|>\varphi(k)\ge k$, y no converge, contradicción. Si hubiera $p\notin K$ adherente, los $F_n=K\cap B_{1/(n+1)}(p)$ serían no vacíos. Tomamos el menor índice $k_n$ con $e(k_n)\in F_n$ y $z_n=e(k_n)\to p$. Compacidad secuencial daría una subsucesión convergente a $\ell\in K$, también a $p$, contradicción por unicidad. Ambas rutas están determinadas por fórmulas de mínimo de índices, sin elegir puntos arbitrariamente. Cerrado y acotado, R4 hace compacto a $K$. No se infiere la enumeración: estaba dada.

</details>
## 16.6. La continuidad lleva compactos a compactos

[]{#MA-SEC-ANM-01-016-006}

**R6. Imagen continua de un compacto.** Sea $f:D\to\mathbb R$ continua y $K\subseteq D$ compacto. Entonces $H=f[K]$ es compacto. Para vacío, la imagen es vacía. En general fijamos una cubierta abierta arbitraria $(V_i)_{i\in I}$ de $H$. La restricción $h=f\mathbin{\upharpoonright}K$ es continua por C14. Sus preimágenes

$$A_i=h^{-1}[V_i]=\{x\in K:f(x)\in V_i\}$$

son abiertas **relativas a $K$**, y cubren $K$. La definición de compacidad pide abiertos de toda la recta. No podemos ignorar ese cambio de ambiente ni escoger sin justificación un abierto ambiente para cada índice.

La cerradura de $K$, ya probada en R4, resuelve el problema por una fórmula única:

$$W_i=(\mathbb R\setminus K)\cup A_i.$$

Cada $W_i$ es abierto real. Un punto fuera de $K$ tiene una bola en el complemento abierto, contenida en $W_i$. Para un punto $x\in A_i$, la apertura relativa da, para este índice y punto fijados, un abierto $O$ con $A_i=K\cap O$. Entonces $x\in O$ y todo punto de $O$ está fuera de $K$ o en $A_i$; por eso $O\subseteq W_i$ proporciona la vecindad necesaria. No construimos una familia elegida $(O_i)$: la familia $(W_i)$ ya está determinada por la fórmula. Además

$$K\cap W_i=A_i.$$

La familia $W$ cubre $K$ porque cada $f(x)$ está en algún $V_i$. Compacidad da un $J\subseteq I$ finito que cubre $K$ mediante los $W_j$. Para cualquier $y\in H$ hay un $x\in K$ con $f(x)=y$. Un índice $j\in J$ cubre ese $x$; como $x\in K\cap W_j=A_j$, obtenemos $y\in V_j$. Los mismos índices finitos cubren $H$ en la cubierta original. Ésta era arbitraria, luego $H$ es compacto.

![Para q(x)=x² sobre K=\[−2,−1\]∪\[1,2\], H=\[1,4\]. V1=(1/2,5/2) y V2=(2,9/2) cubren H; sus preimágenes relativas cubren K. Antes de aplicar compacidad se levantan mediante Wi=(R menos K)∪q⁻¹\[Vi\], una fórmula canónica de abiertos reales. No se requiere inyectividad ni elegir un ambiente por índice.](../../assets/books/anm/C16/C16-F06.svg){#fig-anm-c16-f06 fig-alt="Para q(x)=x² sobre K=\[−2,−1\]∪\[1,2\], H=\[1,4\]. V1=(1/2,5/2) y V2=(2,9/2) cubren H; sus preimágenes relativas cubren K. Antes de aplicar compacidad se levantan mediante Wi=(R menos K)∪q⁻¹\[Vi\], una fórmula canónica de abiertos reales. No se requiere inyectividad ni elegir un ambiente por índice."}

La prueba convierte preimágenes relativas en abiertos ambientales antes de aplicar compacidad; después devuelve índices, no una función inversa. No necesita inyectividad, sucesiones seleccionadas ni compacidad del dominio completo $D$. Por Heine–Borel, $f[K]$ es cerrado y acotado. Así toda continua sobre un compacto tiene valores acotados, incluso si el compacto está formado por varias piezas.

Las direcciones inversas fallan. Una constante en $\mathbb R$ tiene imagen singleton compacta aunque el dominio no lo sea. Y para $f(x)=1/(1+x^2)$ en $\mathbb R$, continua por C14, el singleton compacto $\{0\}$ tiene preimagen vacía compacta, mientras $\{1\}$ tiene preimagen singleton; ninguno describe la compacidad del dominio. Para ver que una preimagen compacta de salida puede ser no compacta, basta la constante $f:\mathbb R\to\mathbb R$, $f=0$: la preimagen de $\{0\}$ es toda $\mathbb R$. Preservación de imagen no significa preservación de preimagen.

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-016-041}

¿Qué ambiente tienen las preimágenes $A_i$ de una cubierta de la imagen?

[]{#MA-MSOL-ANM-01-016-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

**Respuesta.**

Son abiertas relativas al dominio restringido $K$, por continuidad de $f\upharpoonright K$. No se afirma que sean abiertas en toda $\mathbb R$.

**Fundamento en la sección 16.6.**

**R6. Imagen continua de un compacto.** Sea $f:D\to\mathbb R$ continua y $K\subseteq D$ compacto. Entonces $H=f[K]$ es compacto. Para vacío, la imagen es vacía. En general fijamos una cubierta abierta arbitraria $(V_i)_{i\in I}$ de $H$. La restricción $h=f\mathbin{\upharpoonright}K$ es continua por C14. Sus preimágenes

$$A_i=h^{-1}[V_i]=\{x\in K:f(x)\in V_i\}$$

son abiertas **relativas a $K$**, y cubren $K$. La definición de compacidad pide abiertos de toda la recta. No podemos ignorar ese cambio de ambiente ni escoger sin justificación un abierto ambiente para cada índice.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-016-042}

¿Qué fórmula levanta esas preimágenes a abiertos reales?

[]{#MA-MSOL-ANM-01-016-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

**Respuesta.**

$W_i=(\mathbb R\setminus K)\cup A_i$. La cerradura de $K$ y la apertura relativa de $A_i$ prueban apertura real de cada $W_i$.

**Fundamento en la sección 16.6.**

La cerradura de $K$, ya probada en R4, resuelve el problema por una fórmula única:

$$W_i=(\mathbb R\setminus K)\cup A_i.$$

Cada $W_i$ es abierto real. Un punto fuera de $K$ tiene una bola en el complemento abierto, contenida en $W_i$. Para un punto $x\in A_i$, la apertura relativa da, para este índice y punto fijados, un abierto $O$ con $A_i=K\cap O$. Entonces $x\in O$ y todo punto de $O$ está fuera de $K$ o en $A_i$; por eso $O\subseteq W_i$ proporciona la vecindad necesaria. No construimos una familia elegida $(O_i)$: la familia $(W_i)$ ya está determinada por la fórmula. Además

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-016-043}

¿Por qué un punto de $A_i$ tiene una vecindad real dentro de $W_i$?

[]{#MA-MSOL-ANM-01-016-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

**Respuesta.**

Para ese índice, $A_i=K\cap O$ con $O$ abierto real. Todo punto de $O$ está fuera de $K$ o en $A_i$, así $O\subseteq W_i$ y da la vecindad del punto.

**Fundamento en la sección 16.6.**

Cada $W_i$ es abierto real. Un punto fuera de $K$ tiene una bola en el complemento abierto, contenida en $W_i$. Para un punto $x\in A_i$, la apertura relativa da, para este índice y punto fijados, un abierto $O$ con $A_i=K\cap O$. Entonces $x\in O$ y todo punto de $O$ está fuera de $K$ o en $A_i$; por eso $O\subseteq W_i$ proporciona la vecindad necesaria. No construimos una familia elegida $(O_i)$: la familia $(W_i)$ ya está determinada por la fórmula. Además

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-016-044}

¿Se eligió una familia de abiertos ambientes $O_i$?

[]{#MA-MSOL-ANM-01-016-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

**Respuesta.**

No. La familia $W_i$ se define directamente por fórmula única. Un ambiente $O$ se usa sólo para probar apertura en el índice considerado, sin reunir elecciones simultáneas.

**Fundamento en la sección 16.6.**

son abiertas **relativas a $K$**, y cubren $K$. La definición de compacidad pide abiertos de toda la recta. No podemos ignorar ese cambio de ambiente ni escoger sin justificación un abierto ambiente para cada índice.

La cerradura de $K$, ya probada en R4, resuelve el problema por una fórmula única:

$$W_i=(\mathbb R\setminus K)\cup A_i.$$

Cada $W_i$ es abierto real. Un punto fuera de $K$ tiene una bola en el complemento abierto, contenida en $W_i$. Para un punto $x\in A_i$, la apertura relativa da, para este índice y punto fijados, un abierto $O$ con $A_i=K\cap O$. Entonces $x\in O$ y todo punto de $O$ está fuera de $K$ o en $A_i$; por eso $O\subseteq W_i$ proporciona la vecindad necesaria. No construimos una familia elegida $(O_i)$: la familia $(W_i)$ ya está determinada por la fórmula. Además

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-016-045}

¿Qué identidad permite devolver una subcubierta finita a las salidas?

[]{#MA-MSOL-ANM-01-016-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

**Respuesta.**

$K\cap W_i=A_i$. Si $x\in K$ está cubierto por $W_i$, pertenece a la preimagen $A_i$ y su salida está en $V_i$.

**Fundamento en la sección 16.6.**

La familia $W$ cubre $K$ porque cada $f(x)$ está en algún $V_i$. Compacidad da un $J\subseteq I$ finito que cubre $K$ mediante los $W_j$. Para cualquier $y\in H$ hay un $x\in K$ con $f(x)=y$. Un índice $j\in J$ cubre ese $x$; como $x\in K\cap W_j=A_j$, obtenemos $y\in V_j$. Los mismos índices finitos cubren $H$ en la cubierta original. Ésta era arbitraria, luego $H$ es compacto.

La prueba convierte preimágenes relativas en abiertos ambientales antes de aplicar compacidad; después devuelve índices, no una función inversa. No necesita inyectividad, sucesiones seleccionadas ni compacidad del dominio completo $D$. Por Heine–Borel, $f[K]$ es cerrado y acotado. Así toda continua sobre un compacto tiene valores acotados, incluso si el compacto está formado por varias piezas.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-016-046}

¿Se necesita una inversa funcional para cubrir cada salida de $f[K]$?

[]{#MA-MSOL-ANM-01-016-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

**Respuesta.**

No. Para cada salida fijada, pertenencia a la imagen garantiza una entrada testigo. Se obtiene un índice finito que cubre esa entrada y por ello la salida.

**Fundamento en la sección 16.6.**

La familia $W$ cubre $K$ porque cada $f(x)$ está en algún $V_i$. Compacidad da un $J\subseteq I$ finito que cubre $K$ mediante los $W_j$. Para cualquier $y\in H$ hay un $x\in K$ con $f(x)=y$. Un índice $j\in J$ cubre ese $x$; como $x\in K\cap W_j=A_j$, obtenemos $y\in V_j$. Los mismos índices finitos cubren $H$ en la cubierta original. Ésta era arbitraria, luego $H$ es compacto.

La prueba convierte preimágenes relativas en abiertos ambientales antes de aplicar compacidad; después devuelve índices, no una función inversa. No necesita inyectividad, sucesiones seleccionadas ni compacidad del dominio completo $D$. Por Heine–Borel, $f[K]$ es cerrado y acotado. Así toda continua sobre un compacto tiene valores acotados, incluso si el compacto está formado por varias piezas.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-016-047}

¿La imagen compacta de una continua implica dominio compacto?

[]{#MA-MSOL-ANM-01-016-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

**Respuesta.**

No. Una constante en $\mathbb R$ tiene imagen singleton compacta, pero $\mathbb R$ no es compacto.

**Fundamento en la sección 16.6.**

Las direcciones inversas fallan. Una constante en $\mathbb R$ tiene imagen singleton compacta aunque el dominio no lo sea. Y para $f(x)=1/(1+x^2)$ en $\mathbb R$, continua por C14, el singleton compacto $\{0\}$ tiene preimagen vacía compacta, mientras $\{1\}$ tiene preimagen singleton; ninguno describe la compacidad del dominio. Para ver que una preimagen compacta de salida puede ser no compacta, basta la constante $f:\mathbb R\to\mathbb R$, $f=0$: la preimagen de $\{0\}$ es toda $\mathbb R$. Preservación de imagen no significa preservación de preimagen.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-016-048}

¿La preimagen de un compacto por una continua siempre es compacta?

[]{#MA-MSOL-ANM-01-016-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

**Respuesta.**

No. Para la constante cero en $\mathbb R$, la preimagen del singleton compacto $\{0\}$ es toda la recta. Hace falta información adicional del dominio.

**Fundamento en la sección 16.6.**

Las direcciones inversas fallan. Una constante en $\mathbb R$ tiene imagen singleton compacta aunque el dominio no lo sea. Y para $f(x)=1/(1+x^2)$ en $\mathbb R$, continua por C14, el singleton compacto $\{0\}$ tiene preimagen vacía compacta, mientras $\{1\}$ tiene preimagen singleton; ninguno describe la compacidad del dominio. Para ver que una preimagen compacta de salida puede ser no compacta, basta la constante $f:\mathbb R\to\mathbb R$, $f=0$: la preimagen de $\{0\}$ es toda $\mathbb R$. Preservación de imagen no significa preservación de preimagen.

</details>

### Ejercicios de la sección 16.6

#### Ejercicio 26. Levantar un abierto relativo

[]{#MA-EX-ANM-01-016-026}

Sea $K$ cerrado real y $A$ abierto relativo a $K$. Prueba que $W=(\mathbb R\setminus K)\cup A$ es abierto real y que $K\cap W=A$. Explica por qué esta fórmula sirve para una familia sin elegir ambientes simultáneamente.

[]{#MA-SOL-ANM-01-016-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

**Respuesta.**

La identidad es distributividad, pues $K\cap(\mathbb R\setminus K)=\varnothing$ y $A\subseteq K$. Para un punto fuera de $K$, apertura del complemento da una bola dentro de $W$. Para un punto de $A$, representamos $A=K\cap O$ con $O$ abierto real. Todo punto de $O$ está fuera de $K$ o en $A$, así $O\subseteq W$ y da una vecindad del punto. Todos los puntos de $W$ tienen vecindad real dentro, luego $W$ abierto. Para una familia $A_i$, cada $W_i$ está determinado por la misma fórmula; se usa la existencia de un $O$ para probar cada caso, sin reunir una función elegida $i\mapsto O_i$.

**Fundamento en la sección 16.6.**

La cerradura de $K$, ya probada en R4, resuelve el problema por una fórmula única:

$$W_i=(\mathbb R\setminus K)\cup A_i.$$

Cada $W_i$ es abierto real. Un punto fuera de $K$ tiene una bola en el complemento abierto, contenida en $W_i$. Para un punto $x\in A_i$, la apertura relativa da, para este índice y punto fijados, un abierto $O$ con $A_i=K\cap O$. Entonces $x\in O$ y todo punto de $O$ está fuera de $K$ o en $A_i$; por eso $O\subseteq W_i$ proporciona la vecindad necesaria. No construimos una familia elegida $(O_i)$: la familia $(W_i)$ ya está determinada por la fórmula. Además

</details>

#### Ejercicio 27. Devolver los mismos índices

[]{#MA-EX-ANM-01-016-027}

En R6, una subfamilia finita $W_j$ cubre $K$. Prueba que los mismos índices $j$ cubren $f[K]$ con los $V_j$ originales. No supongas que $f$ tenga inversa.

[]{#MA-SOL-ANM-01-016-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

**Respuesta.**

Para $y\in f[K]$ hay una entrada concreta $x\in K$ con $f(x)=y$, por definición de imagen. Algún índice seleccionado $j$ cumple $x\in W_j$. La identidad $K\cap W_j=A_j=f^{-1}[V_j]$ en el dominio restringido da $f(x)\in V_j$, esto es $y\in V_j$. Como $y$ era arbitrario, los mismos índices finitos cubren toda la imagen. Se fija sólo una entrada testigo para el valor considerado; ni unicidad ni una función inversa son necesarias.

**Fundamento en la sección 16.6.**

La familia $W$ cubre $K$ porque cada $f(x)$ está en algún $V_i$. Compacidad da un $J\subseteq I$ finito que cubre $K$ mediante los $W_j$. Para cualquier $y\in H$ hay un $x\in K$ con $f(x)=y$. Un índice $j\in J$ cubre ese $x$; como $x\in K\cap W_j=A_j$, obtenemos $y\in V_j$. Los mismos índices finitos cubren $H$ en la cubierta original. Ésta era arbitraria, luego $H$ es compacto.

La prueba convierte preimágenes relativas en abiertos ambientales antes de aplicar compacidad; después devuelve índices, no una función inversa. No necesita inyectividad, sucesiones seleccionadas ni compacidad del dominio completo $D$. Por Heine–Borel, $f[K]$ es cerrado y acotado. Así toda continua sobre un compacto tiene valores acotados, incluso si el compacto está formado por varias piezas.

</details>

#### Ejercicio 28. Imagen compacta con un hueco

[]{#MA-EX-ANM-01-016-028}

Para $K=[-2,-1]\cup[1,2]$ y $q(x)=x^2$, calcula $q[K]$ y una cubierta de esa imagen con dos miembros abiertos. Describe las preimágenes relativas y sus levantamientos canónicos.

[]{#MA-SOL-ANM-01-016-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

**Respuesta.**

Cada rama da valores entre $1$ y $4$, y para $y\in[1,4]$ la raíz positiva $\sqrt y\in[1,2]$ es preimagen; así $q[K]=[1,4]$. Sirven $V_1=(1/2,5/2)$ y $V_2=(2,9/2)$, que solapan y cubren $[1,4]$. Las preimágenes son $A_1=\{x\in K:x^2<5/2\}$ y $A_2=\{x\in K:x^2>2\}$. Son abiertas relativas por continuidad de $q$. $W_i=(\mathbb R\setminus K)\cup A_i$ son abiertos reales porque $K$ es cerrado, y conservan $K\cap W_i=A_i$. El hueco del dominio no impide compacidad ni el transporte de la cubierta.

**Retorno visual.** Véase [C16-F06](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 16.6.**

La prueba convierte preimágenes relativas en abiertos ambientales antes de aplicar compacidad; después devuelve índices, no una función inversa. No necesita inyectividad, sucesiones seleccionadas ni compacidad del dominio completo $D$. Por Heine–Borel, $f[K]$ es cerrado y acotado. Así toda continua sobre un compacto tiene valores acotados, incluso si el compacto está formado por varias piezas.

Las direcciones inversas fallan. Una constante en $\mathbb R$ tiene imagen singleton compacta aunque el dominio no lo sea. Y para $f(x)=1/(1+x^2)$ en $\mathbb R$, continua por C14, el singleton compacto $\{0\}$ tiene preimagen vacía compacta, mientras $\{1\}$ tiene preimagen singleton; ninguno describe la compacidad del dominio. Para ver que una preimagen compacta de salida puede ser no compacta, basta la constante $f:\mathbb R\to\mathbb R$, $f=0$: la preimagen de $\{0\}$ es toda $\mathbb R$. Preservación de imagen no significa preservación de preimagen.

</details>

#### Ejercicio 29. Una preimagen demasiado grande

[]{#MA-EX-ANM-01-016-029}

Da una continua cuya imagen sea compacta y cuyo dominio no lo sea. Usa el mismo ejemplo para refutar compacidad universal de preimágenes de compactos.

[]{#MA-SOL-ANM-01-016-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

**Respuesta.**

La constante $f:\mathbb R\to\mathbb R$, $f(x)=0$, es continua: el error de salida siempre es cero. Su imagen es el singleton $\{0\}$, compacto por R1, pero su dominio $\mathbb R$ no es compacto. Además $f^{-1}[\{0\}]=\mathbb R$, una preimagen no compacta de un conjunto compacto. R6 sólo preserva imágenes directas de dominios compactos; no afirma las dos recíprocas refutadas.

**Fundamento en la sección 16.6.**

Las direcciones inversas fallan. Una constante en $\mathbb R$ tiene imagen singleton compacta aunque el dominio no lo sea. Y para $f(x)=1/(1+x^2)$ en $\mathbb R$, continua por C14, el singleton compacto $\{0\}$ tiene preimagen vacía compacta, mientras $\{1\}$ tiene preimagen singleton; ninguno describe la compacidad del dominio. Para ver que una preimagen compacta de salida puede ser no compacta, basta la constante $f:\mathbb R\to\mathbb R$, $f=0$: la preimagen de $\{0\}$ es toda $\mathbb R$. Preservación de imagen no significa preservación de preimagen.

</details>

#### Ejercicio 30. El ambiente importa antes de aplicar compacidad

[]{#MA-EX-ANM-01-016-030}

Una prueba afirma que las preimágenes $A_i\subseteq K$ de abiertos de salida son abiertos reales y aplica directamente la definición ambiental de compacidad. Da un ejemplo de preimagen no abierta real y repara la prueba.

[]{#MA-SOL-ANM-01-016-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

**Respuesta.**

Para la identidad $h:[0,1]\to\mathbb R$, la preimagen de $(-1,1/2)$ es $[0,1/2)$, abierta relativa a $K=[0,1]$ pero no abierta real: toda bola alrededor de cero contiene negativos ajenos al conjunto. Para un $K$ compacto, R4 lo hace cerrado real. Se reemplaza cada preimagen por $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real por el argumento de E026 y con $K\cap W_i=A_i$. La compacidad se aplica ahora a la cubierta ambiental $W$; por E027 los índices finitos vuelven a cubrir salidas con los abiertos originales. No se afirma que $A_i$ cambie de ambiente sin prueba.

**Fundamento en la sección 16.6.**

son abiertas **relativas a $K$**, y cubren $K$. La definición de compacidad pide abiertos de toda la recta. No podemos ignorar ese cambio de ambiente ni escoger sin justificación un abierto ambiente para cada índice.

La cerradura de $K$, ya probada en R4, resuelve el problema por una fórmula única:

$$W_i=(\mathbb R\setminus K)\cup A_i.$$

Cada $W_i$ es abierto real. Un punto fuera de $K$ tiene una bola en el complemento abierto, contenida en $W_i$. Para un punto $x\in A_i$, la apertura relativa da, para este índice y punto fijados, un abierto $O$ con $A_i=K\cap O$. Entonces $x\in O$ y todo punto de $O$ está fuera de $K$ o en $A_i$; por eso $O\subseteq W_i$ proporciona la vecindad necesaria. No construimos una familia elegida $(O_i)$: la familia $(W_i)$ ya está determinada por la fórmula. Además

</details>
## 16.7. Por qué los extremos llegan a alcanzarse

[]{#MA-SEC-ANM-01-016-007}

Acotar valores permite formar supremo e ínfimo; no garantiza que sean valores alcanzados. El paso nuevo es combinar acotación con cerradura de la imagen.

**Lema de extremos de un compacto.** Si $H\subseteq\mathbb R$ es compacto y no vacío, $M=\sup H$ y $m=\inf H$ existen por R4 y completitud. Si $M\notin H$, la cerradura da $r>0$ con $(M-r,M+r)\cap H=\varnothing$. Pero $M-r/2<M$ no es cota superior, así existe $y\in H$ con $M-r/2<y\le M$, que cae en la bola excluida. Contradicción: $M\in H$ y es máximo. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, mientras $m+s/2>m$ no es cota inferior; existe $z\in H$ con $m\le z<m+s/2$, de nuevo contradicción. Así $m\in H$ y es mínimo. No elegimos una sucesión que aproxime extremos.

**R7. Weierstrass.** Si $f:D\to\mathbb R$ es continua y $K\subseteq D$ compacto no vacío, hay $x_-,x_+\in K$ con

$$f(x_-)\le f(x)\le f(x_+)\qquad(x\in K).$$

R6 hace compacta la imagen $H=f[K]$. La no vacuidad de $K$ proporciona una entrada y una salida, así $H$ tampoco es vacío. El lema da $m,M\in H$. Por definición de imagen existen dos entradas $x_-,x_+$ con $f(x_-)=m$, $f(x_+)=M$, y sus desigualdades sobre todo $H$ dan la conclusión. Son dos testigos concretos, no una selección de preimágenes para todos los valores. No se garantiza que los puntos sean únicos, distintos ni extremos del dominio.

![En \[0,3\], f(x)=(x−1)² alcanza mínimo cero en x=1 y máximo cuatro en x=3. La existencia general procede de la compacidad de la imagen y de su cerradura, que hacen miembros al ínfimo y al supremo. Un extremo de salida puede tener un argumento interior; no se afirma unicidad en general.](../../assets/books/anm/C16/C16-F07.svg){#fig-anm-c16-f07 fig-alt="En \[0,3\], f(x)=(x−1)² alcanza mínimo cero en x=1 y máximo cuatro en x=3. La existencia general procede de la compacidad de la imagen y de su cerradura, que hacen miembros al ínfimo y al supremo. Un extremo de salida puede tener un argumento interior; no se afirma unicidad en general."}

Por ejemplo, $f(x)=(x-1)^2$ en $[0,3]$ tiene mínimo $0$ en el punto interior $1$ y máximo $4$ en $3$: $0\le(x-1)^2\le4$ porque $-1\le x-1\le2$, y las igualdades indicadas se alcanzan. En $\{-1,1\}$, $x^2$ es constante con valor $1$, y ambos puntos son minimizadores y maximizadores. No hace falta conexidad para extremos.

Si el dominio es además un segmento, C15 añade que la imagen es intervalo. Junto con los extremos alcanzados obtenemos $f[[a,b]]=[m,M]$, donde $m,M$ son extremos **globales**, no necesariamente $f(a),f(b)$. Ésta es una combinación posterior de dos herramientas ya probadas: compacidad proporciona los extremos y conexidad rellena entre ellos. En un compacto roto, la imagen puede ser compacta y omitir valores intermedios; la identidad en $[-2,-1]\cup[1,2]$ lo muestra.

Las hipótesis tienen fallos distintos. La identidad en $(0,1)$ es continua y acotada, pero no alcanza sus extremos $0,1$, porque el dominio no es compacto. En $[0,1]$, la función $u(x)=x$ para $x<1$ y $u(1)=0$ es acotada pero no tiene máximo: toda salida positiva menor que $1$ tiene otra mayor y $1$ nunca se alcanza. Es discontinua en $1$; ahí se perdió la continuidad requerida por R6. El vacío es compacto, pero no tiene entradas que puedan servir de minimizadores: no vacuidad no es una formalidad.

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-016-049}

¿Qué diferencia hay entre supremo de una imagen y máximo alcanzado?

[]{#MA-MSOL-ANM-01-016-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

**Respuesta.**

El supremo es la menor cota superior; ser máximo exige además pertenecer a la imagen. La identidad en $(0,1)$ tiene supremo $1$ pero no lo alcanza.

**Fundamento en la sección 16.7.**

Si el dominio es además un segmento, C15 añade que la imagen es intervalo. Junto con los extremos alcanzados obtenemos $f[[a,b]]=[m,M]$, donde $m,M$ son extremos **globales**, no necesariamente $f(a),f(b)$. Ésta es una combinación posterior de dos herramientas ya probadas: compacidad proporciona los extremos y conexidad rellena entre ellos. En un compacto roto, la imagen puede ser compacta y omitir valores intermedios; la identidad en $[-2,-1]\cup[1,2]$ lo muestra.

Las hipótesis tienen fallos distintos. La identidad en $(0,1)$ es continua y acotada, pero no alcanza sus extremos $0,1$, porque el dominio no es compacto. En $[0,1]$, la función $u(x)=x$ para $x<1$ y $u(1)=0$ es acotada pero no tiene máximo: toda salida positiva menor que $1$ tiene otra mayor y $1$ nunca se alcanza. Es discontinua en $1$; ahí se perdió la continuidad requerida por R6. El vacío es compacto, pero no tiene entradas que puedan servir de minimizadores: no vacuidad no es una formalidad.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-016-050}

¿Por qué el supremo de un compacto no vacío pertenece al conjunto?

[]{#MA-MSOL-ANM-01-016-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

**Respuesta.**

Si quedara fuera, cerradura daría una bola exterior; la propiedad aproximante del supremo daría un punto del conjunto dentro de esa bola, contradicción.

**Fundamento en la sección 16.7.**

Acotar valores permite formar supremo e ínfimo; no garantiza que sean valores alcanzados. El paso nuevo es combinar acotación con cerradura de la imagen.

**Lema de extremos de un compacto.** Si $H\subseteq\mathbb R$ es compacto y no vacío, $M=\sup H$ y $m=\inf H$ existen por R4 y completitud. Si $M\notin H$, la cerradura da $r>0$ con $(M-r,M+r)\cap H=\varnothing$. Pero $M-r/2<M$ no es cota superior, así existe $y\in H$ con $M-r/2<y\le M$, que cae en la bola excluida. Contradicción: $M\in H$ y es máximo. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, mientras $m+s/2>m$ no es cota inferior; existe $z\in H$ con $m\le z<m+s/2$, de nuevo contradicción. Así $m\in H$ y es mínimo. No elegimos una sucesión que aproxime extremos.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-016-051}

¿Cómo se prueba la pertenencia del ínfimo sin seleccionar una sucesión?

[]{#MA-MSOL-ANM-01-016-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

**Respuesta.**

Si $m$ estuviera fuera, una bola de radio $s$ no tocaría el conjunto. Como $m+s/2$ no es cota inferior, existe un punto entre $m$ y $m+s/2$ del conjunto, que invade esa bola.

**Fundamento en la sección 16.7.**

Acotar valores permite formar supremo e ínfimo; no garantiza que sean valores alcanzados. El paso nuevo es combinar acotación con cerradura de la imagen.

**Lema de extremos de un compacto.** Si $H\subseteq\mathbb R$ es compacto y no vacío, $M=\sup H$ y $m=\inf H$ existen por R4 y completitud. Si $M\notin H$, la cerradura da $r>0$ con $(M-r,M+r)\cap H=\varnothing$. Pero $M-r/2<M$ no es cota superior, así existe $y\in H$ con $M-r/2<y\le M$, que cae en la bola excluida. Contradicción: $M\in H$ y es máximo. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, mientras $m+s/2>m$ no es cota inferior; existe $z\in H$ con $m\le z<m+s/2$, de nuevo contradicción. Así $m\in H$ y es mínimo. No elegimos una sucesión que aproxime extremos.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-016-052}

¿Dónde se usa que el dominio de Weierstrass sea no vacío?

[]{#MA-MSOL-ANM-01-016-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

**Respuesta.**

Para que la imagen sea no vacía y admita supremo/ínfimo reales como extremos, y para que existan entradas minimizadoras y maximizadoras. El vacío compacto no tiene esas entradas.

**Fundamento en la sección 16.7.**

R6 hace compacta la imagen $H=f[K]$. La no vacuidad de $K$ proporciona una entrada y una salida, así $H$ tampoco es vacío. El lema da $m,M\in H$. Por definición de imagen existen dos entradas $x_-,x_+$ con $f(x_-)=m$, $f(x_+)=M$, y sus desigualdades sobre todo $H$ dan la conclusión. Son dos testigos concretos, no una selección de preimágenes para todos los valores. No se garantiza que los puntos sean únicos, distintos ni extremos del dominio.

Por ejemplo, $f(x)=(x-1)^2$ en $[0,3]$ tiene mínimo $0$ en el punto interior $1$ y máximo $4$ en $3$: $0\le(x-1)^2\le4$ porque $-1\le x-1\le2$, y las igualdades indicadas se alcanzan. En $\{-1,1\}$, $x^2$ es constante con valor $1$, y ambos puntos son minimizadores y maximizadores. No hace falta conexidad para extremos.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-016-053}

¿Weierstrass obliga a que los puntos extremos sean extremos del dominio?

[]{#MA-MSOL-ANM-01-016-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

**Respuesta.**

No. $(x-1)^2$ en $[0,3]$ tiene mínimo en el punto interior $1$. Se garantizan puntos que alcanzan los valores globales, no una posición prefijada.

**Fundamento en la sección 16.7.**

Por ejemplo, $f(x)=(x-1)^2$ en $[0,3]$ tiene mínimo $0$ en el punto interior $1$ y máximo $4$ en $3$: $0\le(x-1)^2\le4$ porque $-1\le x-1\le2$, y las igualdades indicadas se alcanzan. En $\{-1,1\}$, $x^2$ es constante con valor $1$, y ambos puntos son minimizadores y maximizadores. No hace falta conexidad para extremos.

Si el dominio es además un segmento, C15 añade que la imagen es intervalo. Junto con los extremos alcanzados obtenemos $f[[a,b]]=[m,M]$, donde $m,M$ son extremos **globales**, no necesariamente $f(a),f(b)$. Ésta es una combinación posterior de dos herramientas ya probadas: compacidad proporciona los extremos y conexidad rellena entre ellos. En un compacto roto, la imagen puede ser compacta y omitir valores intermedios; la identidad en $[-2,-1]\cup[1,2]$ lo muestra.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-016-054}

¿Puede haber varios minimizadores y maximizadores?

[]{#MA-MSOL-ANM-01-016-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

**Respuesta.**

Sí. Para $x^2$ en $\{-1,1\}$ ambas entradas dan $1$, de modo que ambos puntos minimizan y maximizan.

**Fundamento en la sección 16.7.**

R6 hace compacta la imagen $H=f[K]$. La no vacuidad de $K$ proporciona una entrada y una salida, así $H$ tampoco es vacío. El lema da $m,M\in H$. Por definición de imagen existen dos entradas $x_-,x_+$ con $f(x_-)=m$, $f(x_+)=M$, y sus desigualdades sobre todo $H$ dan la conclusión. Son dos testigos concretos, no una selección de preimágenes para todos los valores. No se garantiza que los puntos sean únicos, distintos ni extremos del dominio.

Por ejemplo, $f(x)=(x-1)^2$ en $[0,3]$ tiene mínimo $0$ en el punto interior $1$ y máximo $4$ en $3$: $0\le(x-1)^2\le4$ porque $-1\le x-1\le2$, y las igualdades indicadas se alcanzan. En $\{-1,1\}$, $x^2$ es constante con valor $1$, y ambos puntos son minimizadores y maximizadores. No hace falta conexidad para extremos.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-016-055}

¿Qué añade conexidad a la imagen compacta de un segmento?

[]{#MA-MSOL-ANM-01-016-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

**Respuesta.**

C15 dice que es intervalo; C16 da extremos globales alcanzados $m,M$. Juntas las propiedades identifican la imagen como $[m,M]$, sin atribuir esos valores a los extremos del dominio.

**Fundamento en la sección 16.7.**

Por ejemplo, $f(x)=(x-1)^2$ en $[0,3]$ tiene mínimo $0$ en el punto interior $1$ y máximo $4$ en $3$: $0\le(x-1)^2\le4$ porque $-1\le x-1\le2$, y las igualdades indicadas se alcanzan. En $\{-1,1\}$, $x^2$ es constante con valor $1$, y ambos puntos son minimizadores y maximizadores. No hace falta conexidad para extremos.

Si el dominio es además un segmento, C15 añade que la imagen es intervalo. Junto con los extremos alcanzados obtenemos $f[[a,b]]=[m,M]$, donde $m,M$ son extremos **globales**, no necesariamente $f(a),f(b)$. Ésta es una combinación posterior de dos herramientas ya probadas: compacidad proporciona los extremos y conexidad rellena entre ellos. En un compacto roto, la imagen puede ser compacta y omitir valores intermedios; la identidad en $[-2,-1]\cup[1,2]$ lo muestra.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-016-056}

¿Una función acotada en $[0,1]$ tiene máximo aunque no sea continua?

[]{#MA-MSOL-ANM-01-016-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

**Respuesta.**

No necesariamente. Si vale $x$ para $x<1$ y cero en $1$, su imagen es $[0,1)$ y no tiene máximo. La función es discontinua en el extremo $1$.

**Fundamento en la sección 16.7.**

Si el dominio es además un segmento, C15 añade que la imagen es intervalo. Junto con los extremos alcanzados obtenemos $f[[a,b]]=[m,M]$, donde $m,M$ son extremos **globales**, no necesariamente $f(a),f(b)$. Ésta es una combinación posterior de dos herramientas ya probadas: compacidad proporciona los extremos y conexidad rellena entre ellos. En un compacto roto, la imagen puede ser compacta y omitir valores intermedios; la identidad en $[-2,-1]\cup[1,2]$ lo muestra.

Las hipótesis tienen fallos distintos. La identidad en $(0,1)$ es continua y acotada, pero no alcanza sus extremos $0,1$, porque el dominio no es compacto. En $[0,1]$, la función $u(x)=x$ para $x<1$ y $u(1)=0$ es acotada pero no tiene máximo: toda salida positiva menor que $1$ tiene otra mayor y $1$ nunca se alcanza. Es discontinua en $1$; ahí se perdió la continuidad requerida por R6. El vacío es compacto, pero no tiene entradas que puedan servir de minimizadores: no vacuidad no es una formalidad.

</details>

### Ejercicios de la sección 16.7

#### Ejercicio 31. Un supremo que se alcanza

[]{#MA-EX-ANM-01-016-031}

Prueba que un compacto no vacío $H\subseteq\mathbb R$ contiene su supremo y su ínfimo. No construyas una sucesión de puntos próximos a esos valores.

[]{#MA-SOL-ANM-01-016-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

**Respuesta.**

Heine–Borel da acotación y cerradura, así completitud da $M=\sup H$ y $m=\inf H$. Si $M\notin H$, alguna bola de radio $r>0$ en $M$ no toca $H$. Como $M-r/2$ no es cota superior, existe $y\in H$ con $M-r/2<y\le M$, dentro de esa bola, contradicción. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, pero $m+s/2$ no es cota inferior; hay $z\in H$ con $m\le z<m+s/2$, también dentro, contradicción. Ambos valores pertenecen y son extremos. Sólo se usan testigos individuales para dos vecindades.

**Fundamento en la sección 16.7.**

Acotar valores permite formar supremo e ínfimo; no garantiza que sean valores alcanzados. El paso nuevo es combinar acotación con cerradura de la imagen.

**Lema de extremos de un compacto.** Si $H\subseteq\mathbb R$ es compacto y no vacío, $M=\sup H$ y $m=\inf H$ existen por R4 y completitud. Si $M\notin H$, la cerradura da $r>0$ con $(M-r,M+r)\cap H=\varnothing$. Pero $M-r/2<M$ no es cota superior, así existe $y\in H$ con $M-r/2<y\le M$, que cae en la bola excluida. Contradicción: $M\in H$ y es máximo. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, mientras $m+s/2>m$ no es cota inferior; existe $z\in H$ con $m\le z<m+s/2$, de nuevo contradicción. Así $m\in H$ y es mínimo. No elegimos una sucesión que aproxime extremos.

</details>

#### Ejercicio 32. Extremos que no son ambos extremos de entrada

[]{#MA-EX-ANM-01-016-032}

Encuentra mínimo, máximo y todos los argumentos que los alcanzan para $f(x)=(x-1)^2$ en $[0,3]$. Justifica con desigualdades, sin derivadas.

[]{#MA-SOL-ANM-01-016-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

**Respuesta.**

$-1\le x-1\le2$. Si $x\le1$, $|x-1|\le1$; si $x\ge1$, $|x-1|\le2$. En todo el dominio $0\le(x-1)^2\le4$. El mínimo cero requiere $x=1$ y se alcanza allí, punto interior. El máximo cuatro requiere $|x-1|=2$, es decir $x=3$ o $x=-1$; sólo $3$ pertenece al dominio. Así el máximo es $4$ único en $3$. No se evaluaron sólo los extremos del dominio para inferir el mínimo.

**Retorno visual.** Véase [C16-F07](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 16.7.**

R6 hace compacta la imagen $H=f[K]$. La no vacuidad de $K$ proporciona una entrada y una salida, así $H$ tampoco es vacío. El lema da $m,M\in H$. Por definición de imagen existen dos entradas $x_-,x_+$ con $f(x_-)=m$, $f(x_+)=M$, y sus desigualdades sobre todo $H$ dan la conclusión. Son dos testigos concretos, no una selección de preimágenes para todos los valores. No se garantiza que los puntos sean únicos, distintos ni extremos del dominio.

Por ejemplo, $f(x)=(x-1)^2$ en $[0,3]$ tiene mínimo $0$ en el punto interior $1$ y máximo $4$ en $3$: $0\le(x-1)^2\le4$ porque $-1\le x-1\le2$, y las igualdades indicadas se alcanzan. En $\{-1,1\}$, $x^2$ es constante con valor $1$, y ambos puntos son minimizadores y maximizadores. No hace falta conexidad para extremos.

</details>

#### Ejercicio 33. Un compacto sin continuidad suficiente

[]{#MA-EX-ANM-01-016-033}

En $[0,1]$, define $u(x)=x$ si $x<1$ y $u(1)=0$. Calcula su imagen, decide si alcanza máximo y refuta continuidad en $1$ con un testigo para cada radio.

[]{#MA-SOL-ANM-01-016-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

**Respuesta.**

La imagen es $[0,1)$: los argumentos menores que uno producen todos esos valores y el extremo añade cero ya presente. No hay máximo, porque cada $y<1$ de la imagen tiene $(y+1)/2$ mayor dentro de ella. Para $\delta>0$, tomamos $h=\min(\delta/2,1/4)>0$ y $x=1-h\in[0,1)$. Dista menos que $\delta$ de $1$ y $|u(x)-u(1)|=1-h\ge3/4>1/2$. La tolerancia $1/2$ refuta continuidad. El dominio compacto no basta sin la hipótesis funcional de R7.

**Fundamento en la sección 16.7.**

Si el dominio es además un segmento, C15 añade que la imagen es intervalo. Junto con los extremos alcanzados obtenemos $f[[a,b]]=[m,M]$, donde $m,M$ son extremos **globales**, no necesariamente $f(a),f(b)$. Ésta es una combinación posterior de dos herramientas ya probadas: compacidad proporciona los extremos y conexidad rellena entre ellos. En un compacto roto, la imagen puede ser compacta y omitir valores intermedios; la identidad en $[-2,-1]\cup[1,2]$ lo muestra.

Las hipótesis tienen fallos distintos. La identidad en $(0,1)$ es continua y acotada, pero no alcanza sus extremos $0,1$, porque el dominio no es compacto. En $[0,1]$, la función $u(x)=x$ para $x<1$ y $u(1)=0$ es acotada pero no tiene máximo: toda salida positiva menor que $1$ tiene otra mayor y $1$ nunca se alcanza. Es discontinua en $1$; ahí se perdió la continuidad requerida por R6. El vacío es compacto, pero no tiene entradas que puedan servir de minimizadores: no vacuidad no es una formalidad.

</details>

#### Ejercicio 34. No vacuidad y no unicidad

[]{#MA-EX-ANM-01-016-034}

Explica por qué Weierstrass requiere dominio no vacío pero no garantiza unicidad de los extremizadores. Da un ejemplo compacto no vacío con varios mínimos y máximos.

[]{#MA-SOL-ANM-01-016-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

**Respuesta.**

El vacío es compacto, pero no contiene ninguna entrada que sirva de $x_-$ o $x_+$. Su imagen es vacía y no tiene mínimo o máximo real alcanzado. Para no unicidad, $K=\{-1,1\}$ es compacto y $f(x)=x^2$ es continua en él y vale $1$ en ambos puntos. Los dos argumentos minimizan y maximizan; la desigualdad global de Weierstrass permite ese caso. No exige puntos distintos ni únicos.

**Fundamento en la sección 16.7.**

R6 hace compacta la imagen $H=f[K]$. La no vacuidad de $K$ proporciona una entrada y una salida, así $H$ tampoco es vacío. El lema da $m,M\in H$. Por definición de imagen existen dos entradas $x_-,x_+$ con $f(x_-)=m$, $f(x_+)=M$, y sus desigualdades sobre todo $H$ dan la conclusión. Son dos testigos concretos, no una selección de preimágenes para todos los valores. No se garantiza que los puntos sean únicos, distintos ni extremos del dominio.

Por ejemplo, $f(x)=(x-1)^2$ en $[0,3]$ tiene mínimo $0$ en el punto interior $1$ y máximo $4$ en $3$: $0\le(x-1)^2\le4$ porque $-1\le x-1\le2$, y las igualdades indicadas se alcanzan. En $\{-1,1\}$, $x^2$ es constante con valor $1$, y ambos puntos son minimizadores y maximizadores. No hace falta conexidad para extremos.

</details>

#### Ejercicio 35. Dos teoremas para describir la imagen

[]{#MA-EX-ANM-01-016-035}

Sea $a\le b$ y $f:[a,b]\to\mathbb R$ continua. Prueba que su imagen es $[m,M]$, identificando qué aporta C15 y qué aporta C16. Refuta que se puedan tomar siempre $m=f(a)$ y $M=f(b)$.

[]{#MA-SOL-ANM-01-016-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

**Respuesta.**

R2 hace compacto al segmento y R7 aporta extremos globales alcanzados $m\le M$ de la imagen. Toda salida está en $[m,M]$. C15 hace intervalar la imagen porque la función es continua en un intervalo. Como $m,M$ pertenecen a ella, incluye todo $[m,M]$. Ambas inclusiones dan igualdad. Para $f(x)=(x-1)^2$ en $[0,3]$, el mínimo es $0=f(1)$, mientras $f(0)=1$; la propuesta de usar siempre valores de entrada extremos es falsa. Compacidad da extremos alcanzados y conexidad rellena entre ellos, funciones distintas de las dos hipótesis.

**Fundamento en la sección 16.7.**

Si el dominio es además un segmento, C15 añade que la imagen es intervalo. Junto con los extremos alcanzados obtenemos $f[[a,b]]=[m,M]$, donde $m,M$ son extremos **globales**, no necesariamente $f(a),f(b)$. Ésta es una combinación posterior de dos herramientas ya probadas: compacidad proporciona los extremos y conexidad rellena entre ellos. En un compacto roto, la imagen puede ser compacta y omitir valores intermedios; la identidad en $[-2,-1]\cup[1,2]$ lo muestra.

Las hipótesis tienen fallos distintos. La identidad en $(0,1)$ es continua y acotada, pero no alcanza sus extremos $0,1$, porque el dominio no es compacto. En $[0,1]$, la función $u(x)=x$ para $x<1$ y $u(1)=0$ es acotada pero no tiene máximo: toda salida positiva menor que $1$ tiene otra mayor y $1$ nunca se alcanza. Es discontinua en $1$; ahí se perdió la continuidad requerida por R6. El vacío es compacto, pero no tiene entradas que puedan servir de minimizadores: no vacuidad no es una formalidad.

</details>
## 16.8. Márgenes positivos e inversas sobre compactos

[]{#MA-SEC-ANM-01-016-008}

**R8, margen respecto de cero.** Sea $K$ compacto no vacío y $f:K\to\mathbb R$ continua sin ceros. La función $|f|$ es continua por C14. R7 entrega $x_0\in K$ donde alcanza su mínimo $m=|f(x_0)|$. Como no hay ceros, $m>0$, y

$$|f(x)|\ge m>0\qquad(x\in K).$$

Todos los puntos quedan separados de cero por el mismo margen. Así $1/f$ está definida en todo $K$, es continua por C14 y cumple $|1/f(x)|\le1/m$. Si $g:K\to\mathbb R$ es continua, R7 o R6 acota $|g|$ por algún $B\ge0$, y $|g(x)/f(x)|\le B/m$. La ausencia de ceros determina el dominio del cociente; compacidad y continuidad dan la cota global. Sin compacidad, $f(x)=x$ en $(0,1]$ es positiva pero no admite $m>0$ común: algún $1/(n+1)$ es menor que cualquier candidato positivo.

![La función x² en K=\[−2,−1\]∪\[1,2\] tiene mínimo alcanzado m=1. Ningún valor de |f| entra en \[0,1); por tanto |1/f|≤1. El margen requiere compacidad, continuidad y ausencia de ceros. En (0,1\], la identidad es positiva pero carece de margen positivo global.](../../assets/books/anm/C16/C16-F08.svg){#fig-anm-c16-f08 fig-alt="La función x² en K=\[−2,−1\]∪\[1,2\] tiene mínimo alcanzado m=1. Ningún valor de |f| entra en \[0,1); por tanto |1/f|≤1. El margen requiere compacidad, continuidad y ausencia de ceros. En (0,1\], la identidad es positiva pero carece de margen positivo global."}

Otra aplicación es el punto más próximo a un real dado $p$. La función $d_p(x)=|x-p|$ es continua por C14, y R7 le da un mínimo en $K$. Si $p\notin K$, ese mínimo es positivo; si $p\in K$, es cero. Puede haber dos minimizadores: para $K=\{-1,1\}$ y $p=0$ ambos están a distancia $1$. La prueba produce un minimizador para este $p$ fijado, sin construir una selección global para todos los puntos exteriores.

**Fibras compactas.** Para una continua $f:K\to\mathbb R$ y un cerrado real $F$, la preimagen $f^{-1}[F]$ es cerrada relativa a $K$ por C14 y compacta por R3. En particular, cada fibra $f^{-1}[\{y\}]$ es compacta, incluso vacía. Aquí sí se conserva compacidad de preimágenes, porque el dominio compacto y la cerradura de la condición de salida son premisas adicionales. No se afirma ese resultado en dominios arbitrarios.

**Inversa en un compacto.** Una inyección continua $f:K\to\mathbb R$ con $K$ compacto es un homeomorfismo $K\to H=f[K]$. Retipar la salida de f a H conserva la continuidad, porque las distancias de salida son las mismas. Inyectividad y definición de imagen dan una inversa $h:H\to K$. Para probar continuidad de $h$ usamos el criterio de preimágenes de cerrados relativos de C14. Si $A$ es cerrado relativo a $K$, R3 lo hace compacto y R6 hace compacta su imagen $f[A]$. R4 dice que ésta es cerrada real y por tanto cerrada relativa a $H$. Por bijectividad,

$$h^{-1}[A]=f[A].$$

Así la preimagen por $h$ de todo cerrado relativo a su codominio $K$ es cerrada relativa a su dominio $H$, y C14 concluye continuidad. No requiere que $K$ sea intervalo ni que haya una orientación monótona global. El vacío tampoco causa problema: su inversa vacía es continua.

Comparemos con C15: allí un intervalo permitía construir la inversa continua mediante barreras de orden; aquí la compacidad permite transportar cerrados y justificar continuidad incluso en dominios rotos. Son dos hipótesis suficientes distintas. El ejemplo $[0,1)\cup[2,3]$ de C14/C15, con ramas $x$ y $x-1$, no contradice este resultado: falta el punto $1$ adherente al primer segmento, así el dominio no es cerrado ni compacto.

La herramienta principal de C16 es reducir cubiertas arbitrarias a datos finitos. Heine–Borel facilita reconocerla, la extracción secuencial la refleja con su alcance declarado, y continuidad la convierte en extremos y márgenes positivos. C17 estudiará un uso adicional del mismo recurso: obtener un radio de continuidad que funcione para todos los centros a la vez. No lo hemos usado para probar ninguno de los resultados actuales.

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-016-057}

¿Qué función recibe Weierstrass para obtener un margen positivo de una continua sin ceros?

[]{#MA-MSOL-ANM-01-016-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

**Respuesta.**

$|f|$, continua por C14. Su mínimo se alcanza en $x_0\in K$ y vale $|f(x_0)|>0$ porque no hay ceros.

**Fundamento en la sección 16.8.**

**R8, margen respecto de cero.** Sea $K$ compacto no vacío y $f:K\to\mathbb R$ continua sin ceros. La función $|f|$ es continua por C14. R7 entrega $x_0\in K$ donde alcanza su mínimo $m=|f(x_0)|$. Como no hay ceros, $m>0$, y

$$|f(x)|\ge m>0\qquad(x\in K).$$

Todos los puntos quedan separados de cero por el mismo margen. Así $1/f$ está definida en todo $K$, es continua por C14 y cumple $|1/f(x)|\le1/m$. Si $g:K\to\mathbb R$ es continua, R7 o R6 acota $|g|$ por algún $B\ge0$, y $|g(x)/f(x)|\le B/m$. La ausencia de ceros determina el dominio del cociente; compacidad y continuidad dan la cota global. Sin compacidad, $f(x)=x$ en $(0,1]$ es positiva pero no admite $m>0$ común: algún $1/(n+1)$ es menor que cualquier candidato positivo.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-016-058}

¿Qué cota da ese margen $m>0$ al recíproco?

[]{#MA-MSOL-ANM-01-016-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

**Respuesta.**

$|1/f(x)|=1/|f(x)|\le1/m$ para todos los puntos del compacto. No ceros asegura que el recíproco esté definido en todo el dominio.

**Fundamento en la sección 16.8.**

**R8, margen respecto de cero.** Sea $K$ compacto no vacío y $f:K\to\mathbb R$ continua sin ceros. La función $|f|$ es continua por C14. R7 entrega $x_0\in K$ donde alcanza su mínimo $m=|f(x_0)|$. Como no hay ceros, $m>0$, y

$$|f(x)|\ge m>0\qquad(x\in K).$$

Todos los puntos quedan separados de cero por el mismo margen. Así $1/f$ está definida en todo $K$, es continua por C14 y cumple $|1/f(x)|\le1/m$. Si $g:K\to\mathbb R$ es continua, R7 o R6 acota $|g|$ por algún $B\ge0$, y $|g(x)/f(x)|\le B/m$. La ausencia de ceros determina el dominio del cociente; compacidad y continuidad dan la cota global. Sin compacidad, $f(x)=x$ en $(0,1]$ es positiva pero no admite $m>0$ común: algún $1/(n+1)$ es menor que cualquier candidato positivo.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-016-059}

¿Una función positiva en $(0,1]$ tiene siempre cota inferior positiva?

[]{#MA-MSOL-ANM-01-016-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

**Respuesta.**

No. La identidad es positiva pero sus valores $1/(n+1)$ tienden a cero. El dominio no es compacto; falta la hipótesis que garantiza alcanzar un mínimo positivo.

**Fundamento en la sección 16.8.**

**R8, margen respecto de cero.** Sea $K$ compacto no vacío y $f:K\to\mathbb R$ continua sin ceros. La función $|f|$ es continua por C14. R7 entrega $x_0\in K$ donde alcanza su mínimo $m=|f(x_0)|$. Como no hay ceros, $m>0$, y

$$|f(x)|\ge m>0\qquad(x\in K).$$

Todos los puntos quedan separados de cero por el mismo margen. Así $1/f$ está definida en todo $K$, es continua por C14 y cumple $|1/f(x)|\le1/m$. Si $g:K\to\mathbb R$ es continua, R7 o R6 acota $|g|$ por algún $B\ge0$, y $|g(x)/f(x)|\le B/m$. La ausencia de ceros determina el dominio del cociente; compacidad y continuidad dan la cota global. Sin compacidad, $f(x)=x$ en $(0,1]$ es positiva pero no admite $m>0$ común: algún $1/(n+1)$ es menor que cualquier candidato positivo.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-016-060}

¿Qué función proporciona un punto del compacto más próximo a un real $p$?

[]{#MA-MSOL-ANM-01-016-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

**Respuesta.**

$x\mapsto|x-p|$, continua. Weierstrass da un minimizador; si $p$ está fuera de $K$, el mínimo alcanzado no puede ser cero y es positivo.

**Fundamento en la sección 16.8.**

Otra aplicación es el punto más próximo a un real dado $p$. La función $d_p(x)=|x-p|$ es continua por C14, y R7 le da un mínimo en $K$. Si $p\notin K$, ese mínimo es positivo; si $p\in K$, es cero. Puede haber dos minimizadores: para $K=\{-1,1\}$ y $p=0$ ambos están a distancia $1$. La prueba produce un minimizador para este $p$ fijado, sin construir una selección global para todos los puntos exteriores.

**Fibras compactas.** Para una continua $f:K\to\mathbb R$ y un cerrado real $F$, la preimagen $f^{-1}[F]$ es cerrada relativa a $K$ por C14 y compacta por R3. En particular, cada fibra $f^{-1}[\{y\}]$ es compacta, incluso vacía. Aquí sí se conserva compacidad de preimágenes, porque el dominio compacto y la cerradura de la condición de salida son premisas adicionales. No se afirma ese resultado en dominios arbitrarios.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-016-061}

¿El punto más próximo tiene que ser único?

[]{#MA-MSOL-ANM-01-016-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

**Respuesta.**

No. Para $K=\{-1,1\}$ y $p=0$, ambos puntos tienen distancia mínima $1$. Se garantiza existencia, no una selección única.

**Fundamento en la sección 16.8.**

Todos los puntos quedan separados de cero por el mismo margen. Así $1/f$ está definida en todo $K$, es continua por C14 y cumple $|1/f(x)|\le1/m$. Si $g:K\to\mathbb R$ es continua, R7 o R6 acota $|g|$ por algún $B\ge0$, y $|g(x)/f(x)|\le B/m$. La ausencia de ceros determina el dominio del cociente; compacidad y continuidad dan la cota global. Sin compacidad, $f(x)=x$ en $(0,1]$ es positiva pero no admite $m>0$ común: algún $1/(n+1)$ es menor que cualquier candidato positivo.

Otra aplicación es el punto más próximo a un real dado $p$. La función $d_p(x)=|x-p|$ es continua por C14, y R7 le da un mínimo en $K$. Si $p\notin K$, ese mínimo es positivo; si $p\in K$, es cero. Puede haber dos minimizadores: para $K=\{-1,1\}$ y $p=0$ ambos están a distancia $1$. La prueba produce un minimizador para este $p$ fijado, sin construir una selección global para todos los puntos exteriores.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-016-062}

¿Por qué la fibra de un valor por una continua en un compacto es compacta?

[]{#MA-MSOL-ANM-01-016-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

**Respuesta.**

El singleton de salida es cerrado real, su preimagen es cerrada relativa al compacto por C14 y R3 la hace compacta. Se incluye la fibra vacía.

**Fundamento en la sección 16.8.**

**Fibras compactas.** Para una continua $f:K\to\mathbb R$ y un cerrado real $F$, la preimagen $f^{-1}[F]$ es cerrada relativa a $K$ por C14 y compacta por R3. En particular, cada fibra $f^{-1}[\{y\}]$ es compacta, incluso vacía. Aquí sí se conserva compacidad de preimágenes, porque el dominio compacto y la cerradura de la condición de salida son premisas adicionales. No se afirma ese resultado en dominios arbitrarios.

**Inversa en un compacto.** Una inyección continua $f:K\to\mathbb R$ con $K$ compacto es un homeomorfismo $K\to H=f[K]$. Retipar la salida de f a H conserva la continuidad, porque las distancias de salida son las mismas. Inyectividad y definición de imagen dan una inversa $h:H\to K$. Para probar continuidad de $h$ usamos el criterio de preimágenes de cerrados relativos de C14. Si $A$ es cerrado relativo a $K$, R3 lo hace compacto y R6 hace compacta su imagen $f[A]$. R4 dice que ésta es cerrada real y por tanto cerrada relativa a $H$. Por bijectividad,

$$h^{-1}[A]=f[A].$$

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-016-063}

¿Qué identidad demuestra continuidad de la inversa de una inyección continua compacta?

[]{#MA-MSOL-ANM-01-016-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

**Respuesta.**

Para todo cerrado relativo $A\subseteq K$, $h^{-1}[A]=f[A]$. El conjunto $A$ es compacto, su imagen también y por ello es cerrada relativa a $H=f[K]$. El criterio de preimágenes cerradas de C14 da continuidad de $h$.

**Fundamento en la sección 16.8.**

**Inversa en un compacto.** Una inyección continua $f:K\to\mathbb R$ con $K$ compacto es un homeomorfismo $K\to H=f[K]$. Retipar la salida de f a H conserva la continuidad, porque las distancias de salida son las mismas. Inyectividad y definición de imagen dan una inversa $h:H\to K$. Para probar continuidad de $h$ usamos el criterio de preimágenes de cerrados relativos de C14. Si $A$ es cerrado relativo a $K$, R3 lo hace compacto y R6 hace compacta su imagen $f[A]$. R4 dice que ésta es cerrada real y por tanto cerrada relativa a $H$. Por bijectividad,

$$h^{-1}[A]=f[A].$$

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-016-064}

¿La prueba de esa inversa necesita intervalo o continuidad uniforme?

[]{#MA-MSOL-ANM-01-016-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

**Respuesta.**

No. Usa compacidad de cerrados relativos, imagen compacta y criterio de continuidad por cerrados. Puede haber un dominio roto; continuidad uniforme/Heine–Cantor quedan para C17.

**Fundamento en la sección 16.8.**

**Fibras compactas.** Para una continua $f:K\to\mathbb R$ y un cerrado real $F$, la preimagen $f^{-1}[F]$ es cerrada relativa a $K$ por C14 y compacta por R3. En particular, cada fibra $f^{-1}[\{y\}]$ es compacta, incluso vacía. Aquí sí se conserva compacidad de preimágenes, porque el dominio compacto y la cerradura de la condición de salida son premisas adicionales. No se afirma ese resultado en dominios arbitrarios.

**Inversa en un compacto.** Una inyección continua $f:K\to\mathbb R$ con $K$ compacto es un homeomorfismo $K\to H=f[K]$. Retipar la salida de f a H conserva la continuidad, porque las distancias de salida son las mismas. Inyectividad y definición de imagen dan una inversa $h:H\to K$. Para probar continuidad de $h$ usamos el criterio de preimágenes de cerrados relativos de C14. Si $A$ es cerrado relativo a $K$, R3 lo hace compacto y R6 hace compacta su imagen $f[A]$. R4 dice que ésta es cerrada real y por tanto cerrada relativa a $H$. Por bijectividad,

$$h^{-1}[A]=f[A].$$

</details>

### Ejercicios de la sección 16.8

#### Ejercicio 36. Positividad con margen

[]{#MA-EX-ANM-01-016-036}

En $K=[-2,-1]\cup[1,2]$, considera $f(x)=x^2$ y $g(x)=x+1$. Encuentra un margen positivo de $|f|$ y cotas de $|1/f|$ y $|g/f|$ válidas en todo $K$.

[]{#MA-SOL-ANM-01-016-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

**Respuesta.**

Para todo $x\in K$, $1\le x^2\le4$, así $m=1$ es un margen positivo, alcanzado en $\pm1$. El recíproco está definido y $|1/f(x)|=1/x^2\le1$. Además $|g(x)|=|x+1|\le|x|+1\le3$, y $|g(x)/f(x)|\le3$. Las funciones son continuas por C14; las cotas explícitas verifican la consecuencia de R8 sin exigir conectividad del dominio. La cota $3$ es válida aunque no se afirme que sea óptima.

**Retorno visual.** Véase [C16-F08](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 16.8.**

**R8, margen respecto de cero.** Sea $K$ compacto no vacío y $f:K\to\mathbb R$ continua sin ceros. La función $|f|$ es continua por C14. R7 entrega $x_0\in K$ donde alcanza su mínimo $m=|f(x_0)|$. Como no hay ceros, $m>0$, y

$$|f(x)|\ge m>0\qquad(x\in K).$$

Todos los puntos quedan separados de cero por el mismo margen. Así $1/f$ está definida en todo $K$, es continua por C14 y cumple $|1/f(x)|\le1/m$. Si $g:K\to\mathbb R$ es continua, R7 o R6 acota $|g|$ por algún $B\ge0$, y $|g(x)/f(x)|\le B/m$. La ausencia de ceros determina el dominio del cociente; compacidad y continuidad dan la cota global. Sin compacidad, $f(x)=x$ en $(0,1]$ es positiva pero no admite $m>0$ común: algún $1/(n+1)$ es menor que cualquier candidato positivo.

</details>

#### Ejercicio 37. Punto más cercano y dos candidatos

[]{#MA-EX-ANM-01-016-037}

Prueba que cualquier compacto no vacío tiene un punto más próximo a un real fijado $p$. Para $K=\{-1,1\}$ y $p=0$, calcula todos los minimizadores y el margen.

[]{#MA-SOL-ANM-01-016-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

**Respuesta.**

$d_p(x)=|x-p|$ es continua por C14; R7 da un $x_0\in K$ donde alcanza mínimo $m$. Así $|x-p|\ge m$ para todo $x\in K$. Si $p\notin K$, $m=|x_0-p|>0$; si $p\in K$, la entrada $p$ da mínimo cero. En $\{-1,1\}$ con $p=0$ ambas distancias valen $1$, luego ambos puntos son minimizadores y el margen es $1$. No se garantiza unicidad ni se construye una elección para todos los $p$ simultáneamente.

**Fundamento en la sección 16.8.**

Todos los puntos quedan separados de cero por el mismo margen. Así $1/f$ está definida en todo $K$, es continua por C14 y cumple $|1/f(x)|\le1/m$. Si $g:K\to\mathbb R$ es continua, R7 o R6 acota $|g|$ por algún $B\ge0$, y $|g(x)/f(x)|\le B/m$. La ausencia de ceros determina el dominio del cociente; compacidad y continuidad dan la cota global. Sin compacidad, $f(x)=x$ en $(0,1]$ es positiva pero no admite $m>0$ común: algún $1/(n+1)$ es menor que cualquier candidato positivo.

Otra aplicación es el punto más próximo a un real dado $p$. La función $d_p(x)=|x-p|$ es continua por C14, y R7 le da un mínimo en $K$. Si $p\notin K$, ese mínimo es positivo; si $p\in K$, es cero. Puede haber dos minimizadores: para $K=\{-1,1\}$ y $p=0$ ambos están a distancia $1$. La prueba produce un minimizador para este $p$ fijado, sin construir una selección global para todos los puntos exteriores.

</details>

#### Ejercicio 38. Una fibra compacta que se divide

[]{#MA-EX-ANM-01-016-038}

Para $q(x)=x^2$ en $K=[-2,2]$, calcula la fibra de $1$ y prueba su compacidad y su desconexión. Generaliza la compacidad a la preimagen de cualquier cerrado real por una continua en compacto.

[]{#MA-SOL-ANM-01-016-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

**Respuesta.**

La ecuación $x^2=1$ da $\{-1,1\}$, finito y compacto. No es intervalo porque omite cero entre sus puntos, así no conexo por C15. En general, si $f:K\to\mathbb R$ es continua y $F$ cerrado real, C14 da $f^{-1}[F]$ cerrado relativo a $K$, y R3 lo hace compacto. Se incluyen fibras vacías. No hay contradicción entre compacidad y desconexión ni una afirmación de preimágenes compactas para dominios arbitrarios.

**Fundamento en la sección 16.8.**

Otra aplicación es el punto más próximo a un real dado $p$. La función $d_p(x)=|x-p|$ es continua por C14, y R7 le da un mínimo en $K$. Si $p\notin K$, ese mínimo es positivo; si $p\in K$, es cero. Puede haber dos minimizadores: para $K=\{-1,1\}$ y $p=0$ ambos están a distancia $1$. La prueba produce un minimizador para este $p$ fijado, sin construir una selección global para todos los puntos exteriores.

**Fibras compactas.** Para una continua $f:K\to\mathbb R$ y un cerrado real $F$, la preimagen $f^{-1}[F]$ es cerrada relativa a $K$ por C14 y compacta por R3. En particular, cada fibra $f^{-1}[\{y\}]$ es compacta, incluso vacía. Aquí sí se conserva compacidad de preimágenes, porque el dominio compacto y la cerradura de la condición de salida son premisas adicionales. No se afirma ese resultado en dominios arbitrarios.

</details>

#### Ejercicio 39. Inversa por transporte de cerrados

[]{#MA-EX-ANM-01-016-039}

Sea $K$ compacto y $f:K\to\mathbb R$ continua e inyectiva. Demuestra que la inversa $h:f[K]\to K$ es continua mediante preimágenes de cerrados relativos. Trata el vacío.

[]{#MA-SOL-ANM-01-016-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Inyectividad y pertenencia a la imagen dan una entrada única para cada salida, por lo que $h$ existe. Si $A\subseteq K$ es cerrado relativo, R3 lo hace compacto. Su imagen $f[A]$ es compacta por R6, cerrada real por R4 y por ello cerrada relativa a $H=f[K]$. La identidad de la biyección $h^{-1}[A]=f[A]$ prueba que todas esas preimágenes son cerradas relativas. El criterio de C14 para funciones entre dominios y codominios reales relativos da continuidad de $h$. Re-tipar la función directa hacia $H$ conserva el mismo control de distancias y su continuidad. Si $K$ es vacío, también lo es $H$, y las funciones vacías son continuas por la condición universal sin entradas.

</details>

#### Ejercicio 40. Homeomorfismo compacto sin monotonía global

[]{#MA-EX-ANM-01-016-040}

Sea $K=[0,1]\cup[2,3]$ y define $f(x)=x$ en la primera pieza, $f(x)=x-4$ en la segunda. Calcula la imagen, prueba inyectividad y continuidad, decide si es monótona en todo $K$ y justifica continuidad de su inversa.

[]{#MA-SOL-ANM-01-016-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La imagen es $H=[0,1]\cup[-2,-1]$. Las imágenes de ramas son disjuntas y cada rama es inyectiva; por tanto la función es inyectiva y sobreyectiva sobre $H$. Para un centro de $K$ y $\varepsilon>0$, $\delta=\min(1/2,\varepsilon)$ evita la otra pieza y en la misma rama el error de salida es la distancia de entradas, menor que $\varepsilon$. Es continua relativa. No es creciente porque $f(1)=1>f(2)=-2$ aunque $1<2$; no es decreciente porque $f(0)=0<f(1)=1$. $K$ es cerrado y acotado, compacto, así la prueba de E039 da inversa continua sin monotonía global. Explícitamente vale $h(y)=y$ en $[0,1]$ y $h(y)=y+4$ en $[-2,-1]$. La hipótesis compacta sirve aunque el dominio esté roto.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-16)

[← Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Capítulo 17 →](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html)
