---
content-id: MA-BCH-0268
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-016-SOLUCIONES
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
title: Soluciones — Capítulo 16
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C16_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)

## 16.1. Una sola cubierta no basta

[]{#MA-EX-ANM-01-016-001}

[]{#MA-SOL-ANM-01-016-001}

[]{#MA-SEC-ANM-01-016-001}

Compacidad exige que para toda cubierta abierta dada exista una subcubierta finita de esa misma familia. El argumento sólo presenta una cubierta conveniente. Para $\mathbb R$, la familia $U_n=(-(n+1),n+1)$ cubre por arquimedianidad. Toda lista finita no vacía de índices tiene máximo $m$ y su unión está en $U_m$, que no contiene $m+2$. La subfamilia vacía tampoco cubre la recta. Por tanto hay una cubierta sin ninguna subcubierta finita y la recta no es compacta.

La afirmación inválida sustituye «para toda cubierta» por «existe alguna cubierta». La familia creciente es una cubierta abierta concreta que refuta la afirmación universal para la recta. El máximo sólo se toma tras fijar una subfamilia finita no vacía. Tratar también la vacía completa la refutación de todas las reducciones posibles.

## 16.2. Subcubierta concreta

[]{#MA-EX-ANM-01-016-002}

[]{#MA-SOL-ANM-01-016-002}

Los índices $J=\{1,2,3\}$ sirven: $U_1$ cubre desde cero hasta antes de $2/5$, $U_2$ solapa desde $3/10$ y cubre hasta antes de $4/5$, y $U_3$ solapa desde $7/10$ y alcanza uno. Su unión contiene $[0,1]$. Al quitar $U_1$, cero queda fuera; al quitar $U_3$, uno queda fuera; al quitar $U_2$, $1/2$ no está en $U_1$ ni $U_3$. Es una subcubierta concreta, y su irredundancia dentro de esos tres no prueba por sí sola compacidad de $K$, que debe valer para cualquier cubierta.

**Retorno visual.** Véase [C16-F01](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las desigualdades $3/10<2/5$ y $7/10<4/5$ verifican los solapes, evitando huecos entre los tres abiertos. Los testigos cero, uno y medio muestran irredundancia respecto de esa lista elegida. Al retirar un miembro no se reincorpora $U_4$, pues la pregunta examina esa subfamilia de tres. Nada de ello sustituye la comprobación para cubiertas arbitrarias que exige compacidad.

## 16.3. Uniones finitas desde la definición

[]{#MA-EX-ANM-01-016-003}

[]{#MA-SOL-ANM-01-016-003}

El vacío es compacto porque dentro de cualquier cubierta sirve la subfamilia vacía. Para dos compactos, una cubierta de la unión cubre cada uno; existen conjuntos finitos de índices $J_1,J_2$ que cubren las piezas. Su unión finita cubre la unión de las piezas. Por inducción sobre una lista finita de compactos, partiendo de la unión vacía y añadiendo una pieza por paso, se obtiene el resultado. Sólo se combinan testigos finitos de la cubierta fijada; no se escogen subcubiertas de infinitos compactos.

Para una cubierta fijada de la unión, sus miembros cubren cada compacto de la lista. La inducción combina una reducción de la unión anterior con una de la pieza añadida, manteniendo índices de esa cubierta. La finitud de las piezas asegura que el proceso termina con una lista finita. Una familia infinita podría requerir añadir índices indefinidamente y no cumple este argumento.

## 16.4. El mínimo positivo tiene una hipótesis

[]{#MA-EX-ANM-01-016-004}

[]{#MA-SOL-ANM-01-016-004}

Una lista finita no vacía $r_1,\ldots,r_k$ admite un mínimo: empezamos por $r_1$ y comparamos sucesivamente con el siguiente valor, conservando el menor. El resultado es uno de los $r_j$, luego es positivo. Para $r_n=1/(n+1)$, todos los radios son positivos y cero es cota inferior. Para cualquier $c>0$, arquimedianidad da $n$ con $1/(n+1)<c$, así ninguna cota inferior positiva es posible. El ínfimo es cero y no hay un radio positivo que sea menor o igual que todos.

La construcción del mínimo finito termina tras comparar todos los valores y devuelve uno de ellos. Por ello no sólo obtiene una cota, sino un valor positivo de la lista. En la familia infinita, cualquier barrera positiva deja de ser cota inferior al elegir un recíproco más pequeño. El paso finito que conserva una escala positiva no puede reemplazarse por un ínfimo sin comprobar su positividad.

## 16.5. Una unión infinita que escapa

[]{#MA-EX-ANM-01-016-005}

[]{#MA-SOL-ANM-01-016-005}

Por arquimedianidad cada real está en algún $[-n,n]$, así la unión es $\mathbb R$. R2 prueba compacidad de cada segmento, incluido $n=0$. Pero la cubierta $U_n=(-(n+1),n+1)$ de la recta no tiene reducción finita: si $m$ es máximo de los índices seleccionados, $m+2$ queda fuera. La conclusión de unión finita no se extiende a uniones infinitas; las reducciones entregadas por cada pieza no se convierten automáticamente en una sola lista finita.

Cada real tiene magnitud menor o igual que algún natural y por eso pertenece a uno de los segmentos. Esta identidad de la unión sitúa el ejemplo exactamente en la recta, cuyo fallo de compacidad ya se muestra por una cubierta. No basta que cada pieza individual admita reducciones: sus listas pueden crecer sin una cota finita común al recorrer todas las piezas.

## 16.6. Registrar cobertura finita

[]{#MA-EX-ANM-01-016-006}

[]{#MA-SOL-ANM-01-016-006}

[]{#MA-SEC-ANM-01-016-002}

La cobertura da un índice con $a\in U_i$, y ese único miembro cubre $[a,a]$. Por tanto $a\in S$ y $S$ no es vacío. Como $S\subseteq[a,b]$, $b$ es cota superior. Completitud da $c=\sup S$; $a\le c$ porque $a\in S$ y $c\le b$ porque $b$ es cota. Así $c\in[a,b]$ y puede aplicarse la cobertura a ese punto. No se supone que $c\in S$.

La definición de $S$ usa existencia de una lista finita para cada segmento registrado. El primer testigo sólo se necesita para $a$, y permite demostrar no vacuidad. La localización del supremo usa simultáneamente que $a$ es miembro y que $b$ es cota. Quedar en el segmento habilita aplicar la cubierta a $c$, antes de saber si pertenece a $S$.

## 16.7. Prolongar con un solo abierto

[]{#MA-EX-ANM-01-016-007}

[]{#MA-SOL-ANM-01-016-007}

$c\le d\le b$ y $t\le c$, así $a\le t\le d\le b$. Para $z\in[t,d]$, $z\ge t>c-r/2>c-r$ y $z\le d\le c+r/2<c+r$, luego $z\in U_{i_c}$. Por $t\in S$ hay un conjunto finito $J_t$ que cubre $[a,t]$. La unión $J_t\cup\{i_c\}$ es finita y cubre $[a,t]\cup[t,d]=[a,d]$. Esto es exactamente la propiedad que define $d\in S$. Sólo se fijó una subcubierta asociada al $t$ concreto.

La estimación se realiza para cada punto $z$ del tramo nuevo, no únicamente para $d$. Así el mismo abierto $U_{i_c}$ cubre todo lo que falta después de $t$. La lista $J_t$ existe por la pertenencia del $t$ concreto a $S$. Unirla con el índice del abierto central produce una lista finita original y acredita el predicado que define $d\in S$.

## 16.8. El extremo omitido de una prueba

[]{#MA-EX-ANM-01-016-008}

[]{#MA-SOL-ANM-01-016-008}

Con $a<b$, $S=[a,b)$ tiene supremo $b$ y no lo contiene; la igualdad de supremo no implica pertenencia. En R2 se construye además $d=\min(b,c+r/2)\in S$, usando una cobertura de $[a,t]$ y un abierto que contiene a $c$. Si $c<b$, ese $d$ sería mayor que $c$, contradicción con la cota. Luego $c=b$, y la misma fórmula da $d=b$. Como ya se probó $d\in S$, ahora sí $b\in S$. Su definición suministra los índices finitos que cubren $[a,b]$.

**Retorno visual.** Véase [C16-F02](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Si $c<b$, tanto $b$ como $c+r/2$ son mayores que $c$, así su mínimo también lo es. Ese $d\in S$ contradiría que $c$ domina a $S$. Una vez excluido ese caso, se conserva la construcción ya verificada y se obtiene $d=b\in S$. La prueba de pertenencia es indispensable: completitud sola no convierte cualquier supremo en máximo.

## 16.9. No elegir una subcubierta por segmento

[]{#MA-EX-ANM-01-016-009}

[]{#MA-SOL-ANM-01-016-009}

El predicado existencial determina qué puntos están en $S$ sin asociarles un testigo elegido. Primero se usa un índice que cubre $a$ para probar $a\in S$. Después se fija un índice $i_c$ que cubre el supremo, un radio de apertura y un único $t\in S$ próximo al supremo. Sólo para ese $t$ se instancia la existencia de $J_t$. La lista finita $J_t\cup\{i_c\}$ concluye la prueba. No se forma una familia de elecciones sobre todos los $x\in S$.

Definir un conjunto mediante una existencia sólo decide qué elementos cumplen el predicado. Para la prolongación se fija un único punto aproximante y se instancia la existencia de su lista finita. El índice que cubre $c$ y su radio de apertura también se usan sólo en ese paso. No hay una asignación simultánea de subcubiertas o radios sobre todos los segmentos posibles.

## 16.10. Cobertura del intervalo abierto frente al cerrado

[]{#MA-EX-ANM-01-016-010}

[]{#MA-SOL-ANM-01-016-010}

No cubre $[0,1]$ porque ningún miembro contiene cero. Sí cubre $(0,1)$: dado un punto positivo, algún recíproco $1/(n+2)$ es menor que él. Para una subfamilia finita no vacía con máximo índice $m$, $1/(2(m+2))$ pertenece a $(0,1)$ y queda fuera de su unión $U_m$. Por eso el intervalo abierto no es compacto. R2 cuantifica sobre cubiertas que realmente cubren todo el segmento cerrado; esta familia no satisface esa premisa.

La ausencia de cero de todos los abiertos invalida cobertura del segmento cerrado, aunque cubran cada punto positivo. Para el intervalo abierto, el testigo fuera de cualquier reducción finita muestra un fallo real de compacidad. R2 se aplica a familias que cubren también los extremos del segmento. La misma familia puede ser una cubierta de un subconjunto y no serlo del conjunto mayor.

## 16.11. Cubrir el complemento completo

[]{#MA-EX-ANM-01-016-011}

[]{#MA-SOL-ANM-01-016-011}

[]{#MA-SEC-ANM-01-016-003}

Aquí $A=\{0\}$. La familia con un solo miembro $U=(-1/4,1/4)$ cubre $A$, y el abierto propuesto es $(1,3)$. La unión de ambos no contiene, por ejemplo, $-1\in K$. No cubre $K$, así no puede aplicarse compacidad del segmento. La reparación es añadir todo $V=\mathbb R\setminus F$. Si un punto de $K$ no está en $F$, lo cubre $V$; si está en $F$, pertenece a $A$ y lo cubre la familia original. $V$ no toca $A$, por lo que sus índices se pueden retirar después de obtener una subcubierta finita ampliada.

La familia original elegida sólo necesita cubrir cero y por eso puede ser muy pequeña. El recorte del complemento añadido no alcanza la zona negativa de $K$, que tampoco cubre ese original. La reparación con el complemento entero verifica cobertura por los dos casos de pertenencia a $F$. Su disjunción con $A$ garantiza que después pueda retirarse el índice excepcional sin perder cobertura de $A$.

## 16.12. Cerrar dos piezas dentro de un segmento

[]{#MA-EX-ANM-01-016-012}

[]{#MA-SOL-ANM-01-016-012}

$K$ es compacto por R2. Tomamos $F=(-\infty,-1]\cup[1,\infty)$, cerrado real porque su complemento $(-1,1)$ es abierto. Entonces $A=K\cap F$. R3 da compacidad. Para una cubierta de $A$, se añade $\mathbb R\setminus F=(-1,1)$, que cubre precisamente la zona de $K$ no cubierta por pertenencia a $A$; después una subcubierta finita de $K$ conserva suficientes índices originales para cubrir $A$, pues el abierto añadido no toca sus puntos.

El cerrado real $F$ conserva exactamente las dos piezas al recortar por $K$. El abierto añadido cubre el hueco central de ese segmento, mientras una cubierta dada de $A$ cubre sus otras entradas. La reducción finita ampliada puede usar ese abierto, pero ningún punto de $A$ depende de él. Esto permite volver a índices originales y demostrar herencia sin adelantar Heine–Borel.

## 16.13. Etiquetas y abiertos repetidos

[]{#MA-EX-ANM-01-016-013}

[]{#MA-SOL-ANM-01-016-013}

Usamos $I^*=(I\times\{0\})\cup\{(\varnothing,1)\}$ y definimos $W_{(i,0)}=U_i$, $W_{(\varnothing,1)}=V$. Las etiquetas $0\ne1$ garantizan índice excepcional distinto. Una subcubierta finita $J^*$ determina $J=\{i\in I:(i,0)\in J^*\}$, finito por proyección de una parte finita. Para $x\in A$ con $A\cap V=\varnothing$, un índice que lo cubre no es el excepcional; proviene de $J$ y $x\in U_i$. La coincidencia de valores abiertos no cambia la prueba: se retiran sólo índices etiquetados, no todos los miembros de igual valor.

Las etiquetas distinguen posiciones en la familia aunque sus valores como conjuntos sean iguales. El conjunto de índices originales conservados es la proyección de una parte de la lista finita ampliada y sigue siendo finito. Para cada entrada de $A$, el índice excepcional queda descartado por disjunción de su abierto con $A$. Se elimina ese índice concreto, conservando los originales que tengan el mismo valor si los hubiera.

## 16.14. Un subconjunto que pierde compacidad

[]{#MA-EX-ANM-01-016-014}

[]{#MA-SOL-ANM-01-016-014}

La cubierta $U_n=(1/(n+2),2)$ cubre $(0,1)$ por arquimedianidad. La subfamilia vacía no cubre su punto $1/2$. Si $J\subseteq\mathbb N$ es finito no vacío, su máximo $m$ da unión $U_m$, pues los miembros son crecientes. El punto $x=1/(2(m+2))$ es positivo y menor que uno pero está por debajo de $1/(m+2)$, luego no pertenece a ningún abierto seleccionado. No existe subcubierta finita. La hipótesis de cerrado relativo de R3 no puede omitirse.

**Retorno visual.** Véase [C16-F03](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La familia crece porque sus extremos izquierdos disminuyen al aumentar el índice. De ahí que cualquier reducción no vacía tenga unión exactamente igual al abierto de mayor índice. El testigo construido está en el dominio pero por debajo de ese extremo izquierdo. La inclusión en $[0,1]$ se mantiene verdadera; lo que falta para heredar compacidad es ser cerrado relativo allí.

## 16.15. Intersección con un cerrado

[]{#MA-EX-ANM-01-016-015}

[]{#MA-SOL-ANM-01-016-015}

La intersección $K\cap F$ es cerrada relativa a $K$, y R3 la hace compacta. Para una familia de compactos con al menos un miembro, R4 hace a todos cerrados reales. Su intersección $A$ es cerrada, porque su complemento es unión de complementos abiertos, y está contenida en un miembro fijo $K_0$. Es $K_0\cap A$, por tanto compacta por la primera afirmación; esto vale incluso si el conjunto resultante es vacío. Para una familia sin miembros, la intersección ambiental es $\mathbb R$, que no es compacta. La no vacuidad requerida es la de la familia de índices, no la del conjunto intersección.

Después de Heine–Borel, cada miembro compacto es cerrado real, y una intersección arbitraria de cerrados sigue siendo cerrada. Fijar un único miembro de la familia no vacía aporta un ambiente compacto que contiene toda la intersección. No se requiere que haya una entrada común ni seleccionar un miembro por cada índice. La familia vacía no ofrece ese ambiente y su intersección convencional es la recta no compacta.

## 16.16. Acotación desde una cubierta creciente

[]{#MA-EX-ANM-01-016-016}

[]{#MA-SOL-ANM-01-016-016}

[]{#MA-SEC-ANM-01-016-004}

El vacío está en $[0,0]$. Para $K\ne\varnothing$, la familia cubre toda la recta por arquimedianidad y en particular $K$. Compacidad entrega índices finitos $J$, que no pueden ser vacíos. Tienen máximo $m$. Cada $U_j$ seleccionado está contenido en $U_m$, así $K\subseteq(-(m+1),m+1)\subseteq[-(m+1),m+1]$. Los extremos son cotas reales. No se usó ninguna sucesión fabricada de puntos lejanos.

La arquimedianidad verifica cobertura sin construir una sucesión de entradas alejadas. La compacidad entrega una lista finita que cubre todo $K$ y su máximo permite dominar todos los abiertos seleccionados con uno. Esa contención aporta cotas inferior y superior uniformes de entradas. Para el vacío, cualquier cota es válida y no se necesita un máximo de índices.

## 16.17. Un radio exterior por índices finitos

[]{#MA-EX-ANM-01-016-017}

[]{#MA-SOL-ANM-01-016-017}

Cada $V_n$ es unión de dos rayos abiertos. Para cualquier $x\in K$, la distancia $|x-p|$ es positiva y supera algún recíproco, así la familia cubre $K$. Compacidad entrega una subfamilia finita no vacía; con máximo índice $m$, su unión está en $V_m$ porque los miembros crecen. Por tanto todos los puntos de $K$ distan de $p$ más que $1/(m+1)$. La bola abierta de ese radio en $p$ no toca $K$. Como se puede hacer para cada punto exterior, el complemento de $K$ es abierto y $K$ cerrado.

Cada entrada de $K$ tiene distancia positiva a $p$, pero esas distancias podrían a priori ser arbitrariamente pequeñas. La reducción finita de la cubierta transforma los umbrales individuales en uno común mediante el mayor índice. El radio resultante separa toda la bola de $K$. Así se demuestra cerradura desde cubiertas sin seleccionar una ruta convergente hacia el punto exterior.

## 16.18. Reconocer cinco dominios

[]{#MA-EX-ANM-01-016-018}

[]{#MA-SOL-ANM-01-016-018}

$[0,1]$ es cerrado y acotado, compacto. $(0,1]$ es acotado pero no cerrado, pues cero es adherente por los recíprocos y falta; no es compacto. $\mathbb R$ es cerrado pero no acotado, no compacto. El conjunto finito $\{-1,1\}$ es cerrado y acotado, compacto. Los racionales de $[0,1]$ son acotados pero no cerrados: el irracional $p=\sqrt2/2\in(0,1)$ no pertenece y toda bola suya suficientemente pequeña dentro de $(0,1)$ contiene racionales por densidad. Toda bola, por contener una más pequeña de ese tipo, toca el conjunto. No es compacto. La interfaz algebraica de raíz e irracionalidad viene de C04/C10.

Heine–Borel requiere comprobar cerradura y acotación por separado. Un solo fallo basta para negar compacidad. En los racionales del segmento, la densidad produce entradas próximas al irracional interior sin incluirlo en el dominio. Para una bola grande se recorta a otra menor dentro del segmento, lo que asegura adherencia para todas las escalas y no sólo para algunas.

## 16.19. La cola y el prefijo

[]{#MA-EX-ANM-01-016-019}

[]{#MA-SOL-ANM-01-016-019}

$K\subseteq[0,1]$. Si $p\notin K$ y $p<0$ o $p>1$, la mitad de su distancia al segmento da una bola exterior. En el caso restante $0<p<1$ y $p$ no es ningún recíproco, elegimos $N\ge1$ con $1/(N+1)<p/2$. Para todo $n\ge N$, $t_n=1/(n+1)<p/2$, luego $|p-t_n|>p/2$; cero también dista $p$. Los valores $|p-t_n|$ para $n<N$ son una familia finita no vacía positiva. Sea $d$ el mínimo de ellos y $p/2$, positivo. La bola de radio $d/2$ no contiene cero, prefijo ni cola. El complemento es abierto, por tanto $K$ cerrado; al ser acotado, Heine–Borel lo hace compacto. No se eligió una sucesión de testigos arbitrarios de vecindades.

**Retorno visual.** Véase [C16-F04](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El exterior no puede ser cero ni uno porque ambos pertenecen a $K$. En el caso positivo interior, un único corte $N$ controla de una vez toda la cola. Las entradas restantes son finitas y tienen distancia no nula al exterior. El mínimo positivo combina ambos controles y su mitad evita todas las entradas, incluido cero, acreditando apertura del complemento.

## 16.20. Dos propiedades distintas

[]{#MA-EX-ANM-01-016-020}

[]{#MA-SOL-ANM-01-016-020}

$[-2,-1]\cup[1,2]$ es cerrado y acotado, compacto por R4; se separa por los rayos a ambos lados de cero, o no es intervalo por el punto omitido cero entre $-1$ y $1$, así no conexo por C15. $(0,1)$ es intervalo, conexo por C15; no es cerrado porque cero es adherente y falta, así no compacto por Heine–Borel. Los ejemplos muestran que ninguna de las dos propiedades implica la otra.

El compacto con dos piezas obtiene sus propiedades de cerradura y acotación, pero el corte cero muestra su separación. El intervalo abierto obtiene conexidad de intervalaridad, mientras una frontera ausente le impide cerradura y compacidad. Los dos ejemplos son necesarios para descartar las dos implicaciones posibles. Las propiedades pueden coexistir en otros dominios sin que una caracterice a la otra.

## 16.21. Acotar la ruta y retener su límite

[]{#MA-EX-ANM-01-016-021}

[]{#MA-SOL-ANM-01-016-021}

[]{#MA-SEC-ANM-01-016-005}

R4 hace cerrado y acotado a $K$. Dada una sucesión de puntos de $K$, es acotada y C08 entrega una subsucesión convergente en la recta a $\ell$. Si $\ell\notin K$, cerradura da un radio $r>0$ cuya bola en $\ell$ no toca $K$. Convergencia obliga a que los términos de la subsucesión estén eventualmente dentro de esa bola, contradiciendo que todos están en $K$. Por tanto $\ell\in K$. Si $K$ es vacío, no existe tal sucesión y la condición universal se cumple. No se fabrica la sucesión inicial; era un dato.

El límite que proporciona C08 está inicialmente sólo en la recta. La cerradura del dominio lo retiene: una bola exterior sería incompatible con la visita eventual que exige convergencia. La sucesión inicial y sus valores ya son datos, así este paso no fabrica una selección de puntos de familias arbitrarias. En el vacío la afirmación secuencial universal no tiene sucesiones que examinar.

## 16.22. Un límite exterior para todas las extracciones

[]{#MA-EX-ANM-01-016-022}

[]{#MA-SOL-ANM-01-016-022}

Tomamos $x_n=1/(n+1)$, todos en $(0,1]$, con límite cero. Para un selector estrictamente creciente $\varphi$, $\varphi(k)\ge k$ por inducción; entonces $0<x_{\varphi(k)}\le1/(k+1)\to0$. Toda subsucesión converge a cero. Si alguna convergiera a $\ell\in(0,1]$, unicidad del límite daría $\ell=0$, imposible. No hay subsucesión con límite en el dominio, refutando su compacidad secuencial.

**Retorno visual.** Véase [C16-F05](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El selector de una subsucesión puede saltar índices, pero su crecimiento estricto obliga a $\varphi(k)\ge k$. La cota por recíprocos controla por ello cualquier extracción, sin importar sus saltos. La unicidad del límite impide que la misma extracción tenga también un destino interior positivo. Este argumento es más fuerte que comprobar únicamente el destino de la ruta original.

## 16.23. Una fabricación que necesita permiso

[]{#MA-EX-ANM-01-016-023}

[]{#MA-SOL-ANM-01-016-023}

No acotación da que cada $E_n=\{x\in K:|x|>n\}$ es no vacío. Eso es $\forall n\exists x$, no aún una sola función que elija todos los valores. Bajo CC(R) sí existe una sucesión $x_n\in E_n$. Si $K$ fuera secuencialmente compacto, alguna subsucesión $x_{\varphi(k)}$ convergería y por tanto sería acotada por un $M$. Pero $|x_{\varphi(k)}|>\varphi(k)\ge k$, que supera $M$ para algún natural por arquimedianidad. Contradicción. Se prueba acotación bajo la hipótesis indicada; no se adopta CC(R) globalmente.

El cambio que debe justificarse es pasar de existencias individuales a una sola función de términos. CC(R) respalda precisamente ese paso en la recíproca general. Después, una extracción convergente sería acotada, pero sus magnitudes superan índices que crecen sin cota. La contradicción utiliza la ruta seleccionada y deja visible de dónde procede su existencia.

## 16.24. La ruta hacia un punto omitido

[]{#MA-EX-ANM-01-016-024}

[]{#MA-SOL-ANM-01-016-024}

Si $K$ no fuese cerrado, habría $p\notin K$ adherente. Los $F_n=K\cap(p-1/(n+1),p+1/(n+1))$ son no vacíos. CC(R) da una sucesión $z_n\in F_n$. La cota $|z_n-p|<1/(n+1)$ prueba $z_n\to p$. Compacidad secuencial da una subsucesión con límite $\ell\in K$. Toda subsucesión de la convergente también converge a $p$; unicidad da $\ell=p$, contradicción. La selección fue la fabricación de $z_n$, mientras la extracción posterior usa la propiedad secuencial. Por ello $K$ es cerrado bajo la premisa declarada.

La familia seleccionada contiene entradas de $K$ dentro de ventanas decrecientes alrededor del exterior. Las cotas de distancia acreditan convergencia de la ruta completa, y por tanto de todas sus extracciones, a $p$. La extracción que ofrece compacidad secuencial tiene además un destino en $K$. Unicidad identifica ambos destinos y contradice que el punto adherente haya sido exterior.

## 16.25. Una enumeración dada determina testigos

[]{#MA-EX-ANM-01-016-025}

[]{#MA-SOL-ANM-01-016-025}

Si $K$ fuera no acotado, cada $E_n=\{x\in K:|x|>n\}$ sería no vacío. La sobreyectividad hace no vacío $\{j:e(j)\in E_n\}$. Tomamos su menor índice $j_n$, determinado por buen orden, y $x_n=e(j_n)$. Cualquier subsucesión tiene $|x_{\varphi(k)}|>\varphi(k)\ge k$, y no converge, contradicción. Si hubiera $p\notin K$ adherente, los $F_n=K\cap B_{1/(n+1)}(p)$ serían no vacíos. Tomamos el menor índice $k_n$ con $e(k_n)\in F_n$ y $z_n=e(k_n)\to p$. Compacidad secuencial daría una subsucesión convergente a $\ell\in K$, también a $p$, contradicción por unicidad. Ambas rutas están determinadas por fórmulas de mínimo de índices, sin elegir puntos arbitrariamente. Cerrado y acotado, R4 hace compacto a $K$. No se infiere la enumeración: estaba dada.

La enumeración sobreyectiva es un dato adicional: no se deduce de compacidad secuencial ni se construye sin justificación. El buen orden natural determina un índice mínimo para cada condición no vacía y con ello un término único. Los índices de fabricación pueden repetirse y no son los índices de extracción. Una vez fabricadas las rutas, las dos contradicciones prueban acotación y cerradura, suficientes por R4.

## 16.26. Levantar un abierto relativo

[]{#MA-EX-ANM-01-016-026}

[]{#MA-SOL-ANM-01-016-026}

[]{#MA-SEC-ANM-01-016-006}

La identidad es distributividad, pues $K\cap(\mathbb R\setminus K)=\varnothing$ y $A\subseteq K$. Para un punto fuera de $K$, apertura del complemento da una bola dentro de $W$. Para un punto de $A$, representamos $A=K\cap O$ con $O$ abierto real. Todo punto de $O$ está fuera de $K$ o en $A$, así $O\subseteq W$ y da una vecindad del punto. Todos los puntos de $W$ tienen vecindad real dentro, luego $W$ abierto. Para una familia $A_i$, cada $W_i$ está determinado por la misma fórmula; se usa la existencia de un $O$ para probar cada caso, sin reunir una función elegida $i\mapsto O_i$.

Con un representante $O$ del abierto relativo se puede escribir también $W=(\mathbb R\setminus K)\cup O$. La igualdad se verifica separando las entradas de $O$ que están dentro y fuera de $K$. Ambas piezas de esta última unión son abiertas reales porque $K$ es cerrado. La fórmula inicial define $W$ sin depender de cuál representante se haya utilizado para probar su apertura.

## 16.27. Devolver los mismos índices

[]{#MA-EX-ANM-01-016-027}

[]{#MA-SOL-ANM-01-016-027}

Para $y\in f[K]$ hay una entrada concreta $x\in K$ con $f(x)=y$, por definición de imagen. Algún índice seleccionado $j$ cumple $x\in W_j$. La identidad $K\cap W_j=A_j=f^{-1}[V_j]$ en el dominio restringido da $f(x)\in V_j$, esto es $y\in V_j$. Como $y$ era arbitrario, los mismos índices finitos cubren toda la imagen. Se fija sólo una entrada testigo para el valor considerado; ni unicidad ni una función inversa son necesarias.

La salida arbitraria se fija primero y luego se usa una entrada que la alcance. La cobertura finita de esa entrada proporciona un índice de la misma lista seleccionada. El levantamiento no altera su pertenencia a la preimagen dentro de $K$, así el abierto de salida correspondiente cubre el valor. No se ha supuesto unicidad de entrada ni un selector global de fibras.

## 16.28. Imagen compacta con un hueco

[]{#MA-EX-ANM-01-016-028}

[]{#MA-SOL-ANM-01-016-028}

Cada rama da valores entre $1$ y $4$, y para $y\in[1,4]$ la raíz positiva $\sqrt y\in[1,2]$ es preimagen; así $q[K]=[1,4]$. Sirven $V_1=(1/2,5/2)$ y $V_2=(2,9/2)$, que solapan y cubren $[1,4]$. Las preimágenes son $A_1=\{x\in K:x^2<5/2\}$ y $A_2=\{x\in K:x^2>2\}$. Son abiertas relativas por continuidad de $q$. $W_i=(\mathbb R\setminus K)\cup A_i$ son abiertos reales porque $K$ es cerrado, y conservan $K\cap W_i=A_i$. El hueco del dominio no impide compacidad ni el transporte de la cubierta.

**Retorno visual.** Véase [C16-F06](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La raíz positiva verifica que todo valor entre uno y cuatro se alcanza, incluso si hay también una entrada negativa que lo produzca. Los dos abiertos de salida solapan entre dos y cinco medios. En el dominio, esa cobertura se traduce en las condiciones $x^2<5/2$ o $x^2>2$, que juntas cubren todas las entradas. Los levantamientos conservan esas selecciones al recortar por $K$.

## 16.29. Una preimagen demasiado grande

[]{#MA-EX-ANM-01-016-029}

[]{#MA-SOL-ANM-01-016-029}

La constante $f:\mathbb R\to\mathbb R$, $f(x)=0$, es continua: el error de salida siempre es cero. Su imagen es el singleton $\{0\}$, compacto por R1, pero su dominio $\mathbb R$ no es compacto. Además $f^{-1}[\{0\}]=\mathbb R$, una preimagen no compacta de un conjunto compacto. R6 sólo preserva imágenes directas de dominios compactos; no afirma las dos recíprocas refutadas.

El mismo ejemplo refuta dos afirmaciones distintas: una recíproca sobre el dominio y una preservación universal por preimagen. La imagen constante es compacta, pero su fibra completa reproduce un dominio no acotado. Continuidad conserva imágenes de compactos; no limita el tamaño de todas las entradas que producen una salida particular.

## 16.30. El ambiente importa antes de aplicar compacidad

[]{#MA-EX-ANM-01-016-030}

[]{#MA-SOL-ANM-01-016-030}

Para la identidad $h:[0,1]\to\mathbb R$, la preimagen de $(-1,1/2)$ es $[0,1/2)$, abierta relativa a $K=[0,1]$ pero no abierta real: toda bola alrededor de cero contiene negativos ajenos al conjunto. Para un $K$ compacto, R4 lo hace cerrado real. Se reemplaza cada preimagen por $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real por el argumento de E026 y con $K\cap W_i=A_i$. La compacidad se aplica ahora a la cubierta ambiental $W$; por E027 los índices finitos vuelven a cubrir salidas con los abiertos originales. No se afirma que $A_i$ cambie de ambiente sin prueba.

El extremo cero pertenece a la preimagen y toda bola real suya incluye negativos, de modo que apertura relativa no puede reinterpretarse como real. El levantamiento añade las entradas exteriores a $K$ y sí proporciona abiertos ambientales. Su identidad al recortar garantiza que la reparación no cambia qué entradas del compacto corresponden a cada abierto de salida. Así los índices finitos aún vuelven a la cubierta original.

## 16.31. Un supremo que se alcanza

[]{#MA-EX-ANM-01-016-031}

[]{#MA-SOL-ANM-01-016-031}

[]{#MA-SEC-ANM-01-016-007}

Heine–Borel da acotación y cerradura, así completitud da $M=\sup H$ y $m=\inf H$. Si $M\notin H$, alguna bola de radio $r>0$ en $M$ no toca $H$. Como $M-r/2$ no es cota superior, existe $y\in H$ con $M-r/2<y\le M$, dentro de esa bola, contradicción. Si $m\notin H$, una bola de radio $s>0$ no toca $H$, pero $m+s/2$ no es cota inferior; hay $z\in H$ con $m\le z<m+s/2$, también dentro, contradicción. Ambos valores pertenecen y son extremos. Sólo se usan testigos individuales para dos vecindades.

La acotación suministra cotas reales y la no vacuidad permite usar completitud. La cerradura aporta la bola exterior si el extremo no pertenece al conjunto. La propiedad aproximante del supremo o ínfimo encuentra una entrada dentro de esa bola y contradice la hipótesis exterior. Sólo después de ese paso se pueden llamar máximo y mínimo a las cotas óptimas.

## 16.32. Extremos que no son ambos extremos de entrada

[]{#MA-EX-ANM-01-016-032}

[]{#MA-SOL-ANM-01-016-032}

$-1\le x-1\le2$. Si $x\le1$, $|x-1|\le1$; si $x\ge1$, $|x-1|\le2$. En todo el dominio $0\le(x-1)^2\le4$. El mínimo cero requiere $x=1$ y se alcanza allí, punto interior. El máximo cuatro requiere $|x-1|=2$, es decir $x=3$ o $x=-1$; sólo $3$ pertenece al dominio. Así el máximo es $4$ único en $3$. No se evaluaron sólo los extremos del dominio para inferir el mínimo.

**Retorno visual.** Véase [C16-F07](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La no negatividad da la cota inferior y la igualdad exige anular $x-1$. La cota superior se obtiene controlando la magnitud de $x-1$ en las dos zonas del dominio. Para hallar todos los maximizadores hay que resolver también la igualdad y descartar el candidato menos uno que queda fuera. Así se acreditan valores extremos y sus fibras completas, sin derivadas.

## 16.33. Un compacto sin continuidad suficiente

[]{#MA-EX-ANM-01-016-033}

[]{#MA-SOL-ANM-01-016-033}

La imagen es $[0,1)$: los argumentos menores que uno producen todos esos valores y el extremo añade cero ya presente. No hay máximo, porque cada $y<1$ de la imagen tiene $(y+1)/2$ mayor dentro de ella. Para $\delta>0$, tomamos $h=\min(\delta/2,1/4)>0$ y $x=1-h\in[0,1)$. Dista menos que $\delta$ de $1$ y $|u(x)-u(1)|=1-h\ge3/4>1/2$. La tolerancia $1/2$ refuta continuidad. El dominio compacto no basta sin la hipótesis funcional de R7.

El extremo de entrada uno tiene una salida que ya estaba en la imagen y no cierra su frontera superior. La imagen permanece acotada pero sin máximo. El testigo para cada radio se mantiene dentro del dominio y compara con el valor central cero, como exige continuidad. Por ello el ejemplo conserva compacidad del dominio y muestra exactamente la necesidad de continuidad de la función.

## 16.34. No vacuidad y no unicidad

[]{#MA-EX-ANM-01-016-034}

[]{#MA-SOL-ANM-01-016-034}

El vacío es compacto, pero no contiene ninguna entrada que sirva de $x_-$ o $x_+$. Su imagen es vacía y no tiene mínimo o máximo real alcanzado. Para no unicidad, $K=\{-1,1\}$ es compacto y $f(x)=x^2$ es continua en él y vale $1$ en ambos puntos. Los dos argumentos minimizan y maximizan; la desigualdad global de Weierstrass permite ese caso. No exige puntos distintos ni únicos.

La compacidad incluye el vacío, mientras existencia de extremizadores exige entradas reales del dominio. Esa diferencia explica la hipótesis de no vacuidad. En el ejemplo no vacío, dos entradas comparten ambas salidas extremas y satisfacen todas las desigualdades globales. Weierstrass permite empates y no impone que mínimo y máximo sean distintos.

## 16.35. Dos teoremas para describir la imagen

[]{#MA-EX-ANM-01-016-035}

[]{#MA-SOL-ANM-01-016-035}

R2 hace compacto al segmento y R7 aporta extremos globales alcanzados $m\le M$ de la imagen. Toda salida está en $[m,M]$. C15 hace intervalar la imagen porque la función es continua en un intervalo. Como $m,M$ pertenecen a ella, incluye todo $[m,M]$. Ambas inclusiones dan igualdad. Para $f(x)=(x-1)^2$ en $[0,3]$, el mínimo es $0=f(1)$, mientras $f(0)=1$; la propuesta de usar siempre valores de entrada extremos es falsa. Compacidad da extremos alcanzados y conexidad rellena entre ellos, funciones distintas de las dos hipótesis.

La primera inclusión procede de las cotas globales alcanzadas de Weierstrass. La segunda procede de intervalaridad de la imagen y pertenencia de los dos valores extremos. Si $a=b$, la imagen es un singleton y ambas inclusiones siguen siendo válidas. El contraejemplo muestra que los valores globales deben identificarse por la función completa, no asignarse de antemano a los extremos de entrada.

## 16.36. Positividad con margen

[]{#MA-EX-ANM-01-016-036}

[]{#MA-SOL-ANM-01-016-036}

[]{#MA-SEC-ANM-01-016-008}

Para todo $x\in K$, $1\le x^2\le4$, así $m=1$ es un margen positivo, alcanzado en $\pm1$. El recíproco está definido y $|1/f(x)|=1/x^2\le1$. Además $|g(x)|=|x+1|\le|x|+1\le3$, y $|g(x)/f(x)|\le3$. Las funciones son continuas por C14; las cotas explícitas verifican la consecuencia de R8 sin exigir conectividad del dominio. La cota $3$ es válida aunque no se afirme que sea óptima.

**Retorno visual.** Véase [C16-F08](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html#fig-anm-c16-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El margen uno se alcanza en ambos puntos de magnitud uno y es válido en las dos piezas del dominio. Invertirlo controla el recíproco. La triangular y $|x|\le2$ dan una cota del numerador; dividir por un denominador de magnitud al menos uno conserva esa cota. Estos controles son globales y no necesitan conectar las dos piezas por un intervalo.

## 16.37. Punto más cercano y dos candidatos

[]{#MA-EX-ANM-01-016-037}

[]{#MA-SOL-ANM-01-016-037}

$d_p(x)=|x-p|$ es continua por C14; R7 da un $x_0\in K$ donde alcanza mínimo $m$. Así $|x-p|\ge m$ para todo $x\in K$. Si $p\notin K$, $m=|x_0-p|>0$; si $p\in K$, la entrada $p$ da mínimo cero. En $\{-1,1\}$ con $p=0$ ambas distancias valen $1$, luego ambos puntos son minimizadores y el margen es $1$. No se garantiza unicidad ni se construye una elección para todos los $p$ simultáneamente.

El mínimo de distancia pertenece a la imagen de la función continua y por eso hay una entrada que lo alcanza. Si el punto fijado es exterior, esa entrada no coincide con él y el valor mínimo es positivo. Los dos candidatos del ejemplo tienen la misma distancia y ninguno mejora al otro. Existencia de un minimizador no equivale a una regla única de elección para todos los puntos exteriores.

## 16.38. Una fibra compacta que se divide

[]{#MA-EX-ANM-01-016-038}

[]{#MA-SOL-ANM-01-016-038}

La ecuación $x^2=1$ da $\{-1,1\}$, finito y compacto. No es intervalo porque omite cero entre sus puntos, así no conexo por C15. En general, si $f:K\to\mathbb R$ es continua y $F$ cerrado real, C14 da $f^{-1}[F]$ cerrado relativo a $K$, y R3 lo hace compacto. Se incluyen fibras vacías. No hay contradicción entre compacidad y desconexión ni una afirmación de preimágenes compactas para dominios arbitrarios.

La fibra concreta tiene dos entradas y su compacidad proviene de finitud, pero su desconexión proviene del hueco entre ellas. En la generalización, cerrado de salida se convierte por continuidad en cerrado relativo de entradas, y R3 utiliza el dominio compacto. La conclusión no exige que el cerrado de salida sea acotado, pues la acotación relevante ya está en el dominio.

## 16.39. Inversa por transporte de cerrados

[]{#MA-EX-ANM-01-016-039}

[]{#MA-SOL-ANM-01-016-039}

Inyectividad y pertenencia a la imagen dan una entrada única para cada salida, por lo que $h$ existe. Si $A\subseteq K$ es cerrado relativo, R3 lo hace compacto. Su imagen $f[A]$ es compacta por R6, cerrada real por R4 y por ello cerrada relativa a $H=f[K]$. La identidad de la biyección $h^{-1}[A]=f[A]$ prueba que todas esas preimágenes son cerradas relativas. El criterio de C14 para funciones entre dominios y codominios reales relativos da continuidad de $h$. Re-tipar la función directa hacia $H$ conserva el mismo control de distancias y su continuidad. Si $K$ es vacío, también lo es $H$, y las funciones vacías son continuas por la condición universal sin entradas.

La inversa tiene dominio exactamente la imagen y codominio $K$. Cada cerrado relativo de ese codominio debe tener preimagen cerrada relativa en la imagen. La identidad con $f[A]$ traduce esa obligación en transporte de compactos y Heine–Borel. El vacío satisface el criterio sin entradas; no hay necesidad de excluirlo ni de añadir monotonía o continuidad uniforme.

## 16.40. Homeomorfismo compacto sin monotonía global

[]{#MA-EX-ANM-01-016-040}

[]{#MA-SOL-ANM-01-016-040}

La imagen es $H=[0,1]\cup[-2,-1]$. Las imágenes de ramas son disjuntas y cada rama es inyectiva; por tanto la función es inyectiva y sobreyectiva sobre $H$. Para un centro de $K$ y $\varepsilon>0$, $\delta=\min(1/2,\varepsilon)$ evita la otra pieza y en la misma rama el error de salida es la distancia de entradas, menor que $\varepsilon$. Es continua relativa. No es creciente porque $f(1)=1>f(2)=-2$ aunque $1<2$; no es decreciente porque $f(0)=0<f(1)=1$. $K$ es cerrado y acotado, compacto, así la prueba de E039 da inversa continua sin monotonía global. Explícitamente vale $h(y)=y$ en $[0,1]$ y $h(y)=y+4$ en $[-2,-1]$. La hipótesis compacta sirve aunque el dominio esté roto.

Las imágenes de las dos piezas son disjuntas, por lo que la inyectividad local de cada rama se convierte en inyectividad global. La separación de las piezas permite un radio común auxiliar que mantiene una entrada próxima en la misma rama. Las comparaciones dadas refutan tanto crecimiento como decrecimiento globales. Aun así compacidad e inyectividad permiten aplicar E039 y obtener continuidad de la inversa sobre la imagen separada.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)
