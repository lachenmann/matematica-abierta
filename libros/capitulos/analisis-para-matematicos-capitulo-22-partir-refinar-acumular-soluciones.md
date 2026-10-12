---
content-id: MA-BCH-0292
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-022-SOLUCIONES
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
title: Soluciones — Capítulo 22
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C22_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-microcontroles.html)

## 22.1. Lista o dibujo

[]{#MA-EX-ANM-01-022-001}

[]{#MA-SOL-ANM-01-022-001}

[]{#MA-SEC-ANM-01-022-001}

Sólo la primera: conserva extremos y tiene comparaciones estrictas. La segunda repite un nodo, por lo que hay anchura cero; la tercera disminuye de3/4 a1/4. Un dibujo con varios cortes no corrige esas fallas.

## 22.2. Longitudes que telescopan

[]{#MA-EX-ANM-01-022-002}

[]{#MA-SOL-ANM-01-022-002}

Son3/4,3/4,3/2; suman3=2−(−1). Para una pieza la identidad es $x_1-x_0$. Si vale para $r$ piezas, añadir $x_{r+1}-x_r$ da $(x_r-x_0)+(x_{r+1}-x_r)=x_{r+1}-x_0$, que prueba el paso.

**Retorno visual.** Véase [C22-F01](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.3. Una entrada en su pieza

[]{#MA-EX-ANM-01-022-003}

[]{#MA-SOL-ANM-01-022-003}

Cero pertenece a $[-1/4,1/2]$ y2 al último intervalo. En general, si $t<b$, el menor $j$ con $t<x_j$ existe pues $n$ pertenece; no es0 porque $t\ge a$. La minimalidad da $x_{j-1}\le t<x_j$. Si $t=b$ pertenece al último, existente por $n\ge1$.

## 22.4. Cerrar no es separar

[]{#MA-EX-ANM-01-022-004}

[]{#MA-SOL-ANM-01-022-004}

Los cerrados vecinos comparten1/3 o2/3. La cobertura disjunta es $[0,1/3]$, $(1/3,2/3]$, $(2/3,1]$; cada punto pertenece a una sola pieza y la unión es $[0,1]$. No cambian las anchuras.

## 22.5. El tipo de los objetos

[]{#MA-EX-ANM-01-022-005}

[]{#MA-SOL-ANM-01-022-005}

Codificar por $(n,p)$ con $p:\{0,\ldots,n\}\to[a,b]$ tipada. Sus grafos están en $\mathcal P(\mathbb N\times[a,b])$ y dominios en $\mathcal P(\mathbb N)$; el producto con $\mathbb N$ es conjunto ambiente. Separar los que tienen extremos y crecimiento estricto da el conjunto. $(1,p)$ con $p(0)=a,p(1)=b$ es un elemento porque $a<b$.

## 22.6. Insertar sin repetir

[]{#MA-EX-ANM-01-022-006}

[]{#MA-SOL-ANM-01-022-006}

[]{#MA-SEC-ANM-01-022-002}

La lista es $(0,1/4,2/5,3/4,1)$. La pieza original de anchura1/2 se divide en3/20 y7/20, cuya suma es1/2. Las restantes anchuras son1/4. El crecimiento estricto queda preservado.

## 22.7. La unión que compara

[]{#MA-EX-ANM-01-022-007}

[]{#MA-SOL-ANM-01-022-007}

Es $(0,1/3,1/2,2/3,1)$. Cada nodo viene de una de las listas, por lo que refina a ambas. Cualquier refinamiento de ambas contiene su unión, y por eso refina a esta lista. Sus anchuras son1/3,1/6,1/6,1/3.

**Retorno visual.** Véase [C22-F02](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.8. Un nodo antiguo

[]{#MA-EX-ANM-01-022-008}

[]{#MA-SOL-ANM-01-022-008}

El conjunto de nodos permanece igual. Repetir1/2 en la lista rompería la comparación estricta y produciría una pieza de anchura cero. La única lista ordenada de ese conjunto es la original.

## 22.9. Orden de resolución

[]{#MA-EX-ANM-01-022-009}

[]{#MA-SOL-ANM-01-022-009}

Las dos primeras son las propiedades de inclusión de nodos. Si $P\preceq Q$ y $Q\preceq P$, los conjuntos finitos coinciden. Sus listas crecientes tienen el mismo mínimo; eliminarlo y repetir por inducción da igualdad de todas las entradas y longitudes, luego $P=Q$.

## 22.10. Mover no es añadir

[]{#MA-EX-ANM-01-022-010}

[]{#MA-SOL-ANM-01-022-010}

Ninguna refina a la otra:1/2 falta en la segunda y1/3 falta en la primera. La comparación legítima se hace en la unión ordenada, que conserva todos los cortes y es refinamiento común.

## 22.11. Máximo o promedio

[]{#MA-EX-ANM-01-022-011}

[]{#MA-SOL-ANM-01-022-011}

[]{#MA-SEC-ANM-01-022-003}

Malla3/4, promedio1/2. Como cada anchura es≤malla, sumar $n$ desigualdades da $b-a\le n\|P\|$. La copia real de $n$ es positiva, por lo que dividir conserva el orden y da la cota.

## 22.12. Cada hija tiene padre

[]{#MA-EX-ANM-01-022-012}

[]{#MA-SOL-ANM-01-022-012}

Una pieza entre dos nodos consecutivos de $Q$ no puede contener un nodo de $P$ en su interior: también sería nodo de $Q$, contradicción. Localizarla entre nodos consecutivos antiguos da un padre que la contiene. Su anchura≤anchura padre≤malla antigua; el máximo de todas las hijas conserva la cota.

**Retorno visual.** Véase [C22-F03](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.13. Más piezas, mismo defecto

[]{#MA-EX-ANM-01-022-013}

[]{#MA-SOL-ANM-01-022-013}

Para $k\ge0$, usar0,1/2 y los cortes $1/2+j/2^{k+1}$ con $1\le j\le2^k$. Cada siguiente lista divide las piezas de la mitad derecha y conserva los nodos anteriores. La izquierda mide1/2 y las derechas≤1/2; la malla es siempre1/2, aunque hay $2^k+1$ piezas.

## 22.14. Resolución prescrita

[]{#MA-EX-ANM-01-022-014}

[]{#MA-SOL-ANM-01-022-014}

Longitud3; elegir uniforme con31 piezas da malla3/31<1/10. Los nodos $-1+3i/31$ son crecientes y tienen los extremos exigidos. Una de30 piezas sólo daría igualdad, que no satisface el pedido estricto.

## 22.15. Conservar y mejorar

[]{#MA-EX-ANM-01-022-015}

[]{#MA-SOL-ANM-01-022-015}

Arquimedianidad proporciona $n>(b-a)/\delta$. $U_n$ tiene malla $(b-a)/n<\delta$. El menor refinamiento común $R$ de $P,U_n$ refina a $P$ y su malla≤malla de $U_n$, por el ejercicio anterior; así cumple el radio.

## 22.16. Lineal con tres etiquetas

[]{#MA-EX-ANM-01-022-016}

[]{#MA-SOL-ANM-01-022-016}

[]{#MA-SEC-ANM-01-022-004}

Las alturas son $(0,1/2)$, $(1/4,3/4)$ y $(1/2,1)$; las anchuras son ambas1/2. Las sumas son1/4,1/2 y3/4. No hay todavía igualdad de todas las sumas de una partición.

## 22.17. Acumular con signo

[]{#MA-EX-ANM-01-022-017}

[]{#MA-SOL-ANM-01-022-017}

Alturas izquierda−1,0 dan−1/2; medias−1/2,1/2 dan0; derechas0,1 dan1/2. En la media hay una contribución−1/4 y otra1/4. El valor0 es su suma firmada y no una afirmación de área geométrica nula.

**Retorno visual.** Véase [C22-F04](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.18. Álgebra de una suma

[]{#MA-EX-ANM-01-022-018}

[]{#MA-SOL-ANM-01-022-018}

Sustituir $(\alpha f+\beta g)(\xi_i)=\alpha f(\xi_i)+\beta g(\xi_i)$, multiplicar por anchura y usar distributividad finita separa las dos sumas. Si $f\le g$, cada diferencia $(g(\xi_i)-f(\xi_i))\Delta_i\ge0$; sumar da el orden.

## 22.19. Compartir una etiqueta

[]{#MA-EX-ANM-01-022-019}

[]{#MA-SOL-ANM-01-022-019}

Sí:1/2 pertenece a ambos intervalos cerrados. Ambas alturas valen1/4; multiplicar por1/2 y sumar da1/4. La familia de etiquetas conserva dos índices aun cuando sus valores coinciden.

## 22.20. Cota sin máximo

[]{#MA-EX-ANM-01-022-020}

[]{#MA-SOL-ANM-01-022-020}

Comparar con las constantes−2 y3 da $-6\le S\le9$. También $|f|\le3$ da $|S|\le9$ por triangular y longitud3. No se requiere que $f$ alcance−2 o3; son cotas universales dadas.

## 22.21. Etiquetas que cambian

[]{#MA-EX-ANM-01-022-021}

[]{#MA-SOL-ANM-01-022-021}

[]{#MA-SEC-ANM-01-022-005}

Restar sumas y triangular da $|S_\xi-S_\eta|\le\sum|f(\xi_i)-f(\eta_i)|\Delta_i$. Para $x$, cada diferencia≤anchura, de modo que la suma≤$\sum\Delta_i^2\le\|P\|$, usando telescopía de longitudes1.

## 22.22. De muestras a todas las entradas

[]{#MA-EX-ANM-01-022-022}

[]{#MA-SOL-ANM-01-022-022}

Se puede definir una función cero en los dos puntos muestreados y con valor arbitrariamente grande en un tercer punto de la pieza. Las dos muestras coinciden, pero una etiqueta en el tercer punto cambia la suma en esa altura por la anchura. La cota $d_i$ necesita todos los pares, no dos evaluaciones.
## 22.23. Comparar con hijas

[]{#MA-EX-ANM-01-022-023}

[]{#MA-SOL-ANM-01-022-023}

Las hijas de cada padre tienen anchuras que suman la antigua. Reescribir la suma vieja como $\sum_{J\subset I_i}f(\xi_i)|J|$ y restar las hijas. La diferencia de alturas≤$L\Delta_i$ porque ambas entradas están en el padre. Triangular y sumar dan $L\sum_i\Delta_i^2\le L\|P\|(b-a)$.

## 22.24. Una suma puede ir a ambos lados

[]{#MA-EX-ANM-01-022-024}

[]{#MA-SOL-ANM-01-022-024}

Refinar en0,1/2,1. Etiquetas izquierdas dan1/4 y derechas3/4, respectivamente menores y mayores que1/2. Se conservan función e intervalo; cambia sólo la familia de etiquetas. Refinamiento no obliga monotonía de suma.

**Retorno visual.** Véase [C22-F05](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.25. Dos resoluciones distintas

[]{#MA-EX-ANM-01-022-025}

[]{#MA-SOL-ANM-01-022-025}

El refinamiento común $R$ y etiquetas dadas en él permiten triangular dos comparaciones con padres. La cota es $3\cdot2(\|P\|+\|Q\|)\le6(1/10+1/20)=9/10$. Es independiente de todas las etiquetas; no afirma por sí sola un valor integral.

## 22.26. Un escalón firmado

[]{#MA-EX-ANM-01-022-026}

[]{#MA-SOL-ANM-01-022-026}

[]{#MA-SEC-ANM-01-022-006}

$A=2/3-2/3=0$. Insertar dentro de una región reemplaza $c(v-u)$ por $c(t-u)+c(v-t)=c(v-u)$. Los nodos excepcionales no entran en la fórmula de $A$. En el refinamiento común de dos representaciones las mismas constantes interiores prueban invariancia completa.

## 22.27. Una etiqueta excepcional

[]{#MA-EX-ANM-01-022-027}

[]{#MA-SOL-ANM-01-022-027}

Ambas alturas son10 y cada anchura1/2; $S=10$. Las constantes interiores son cero y $A=0$. Una suma etiquetada finita puede diferir mucho por repetir una etiqueta excepcional, aunque la integral futura sea0.

**Retorno visual.** Véase [C22-F06](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.28. Dos piezas por punto

[]{#MA-EX-ANM-01-022-028}

[]{#MA-SOL-ANM-01-022-028}

Una etiqueta con diferencia no nula debe ser uno de esos puntos. Cada punto está en a lo sumo dos piezas cerradas; las piezas no vecinas están separadas por nodos. Hay a lo sumo $2k$ términos no nulos, cada uno de valor absoluto≤$D\|P\|$. Triangular da la cota; para $k=0$ no hay términos.

## 22.29. Sin alinear los cortes

[]{#MA-EX-ANM-01-022-029}

[]{#MA-SOL-ANM-01-022-029}

Refinar $P$ con todos los nodos del escalón y sumar las constantes interiores en las hijas: da $A$. Un padre que no toca ningún nodo aporta exactamente esa suma. Los otros padres son a lo sumo $2(m+1)$, porque cada nodo toca como máximo dos; su longitud total≤$2(m+1)\|P\|$. En ellos la diferencia de alturas≤$2B$. Multiplicar y triangular da la cota, con posibles sobrecuentas que sólo la ensanchan.

## 22.30. Representación duplicada

[]{#MA-EX-ANM-01-022-030}

[]{#MA-SOL-ANM-01-022-030}

Una pieza da $3\cdot2=6$. Las tres anchuras son1/2,1,1/2 y dan3/2+3+3/2=6. La invariancia general usa el refinamiento común y las constantes iguales en cada interior hijo, no un acuerdo casual de este ejemplo.

## 22.31. El orden de los cuantificadores

[]{#MA-EX-ANM-01-022-031}

[]{#MA-SOL-ANM-01-022-031}

[]{#MA-SEC-ANM-01-022-007}

Existe $I$ tal que para cada $\varepsilon>0$ hay $\delta>0$ que sirve para todas las particiones y etiquetas con malla<radio. Si la partición se elige primero, se puede tomar un radio≤su malla y la implicación será vacía para ese objeto. No se controla ninguna familia de resoluciones pequeñas ni las demás etiquetas.

## 22.32. Un valor único

[]{#MA-EX-ANM-01-022-032}

[]{#MA-SOL-ANM-01-022-032}

Si $I\ne J$, sea $d=|I-J|>0$. Obtener radios $\delta_I,\delta_J$ para tolerancia $d/3$; una uniforme suficientemente fina cumple ambos. Con etiquetas izquierdas dadas, triangular da $d\le|I-S|+|S-J|<2d/3$, contradicción. La existencia de esa partición es arquimediana.

## 22.33. Un radio efectivo

[]{#MA-EX-ANM-01-022-033}

[]{#MA-SOL-ANM-01-022-033}

Tomar $\delta=1/500$. Malla estrictamente menor da error<1/100. La uniforme de501 piezas cumple1/501<1/500;500 piezas sólo garantizarían error≤1/100 y no la exigencia estricta.

**Retorno visual.** Véase [C22-F07](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.34. Cambiar finitos valores

[]{#MA-EX-ANM-01-022-034}

[]{#MA-SOL-ANM-01-022-034}

Triangular $|S_g-I|\le|S_g-S_f|+|S_f-I|$. Pedir a $f$ error<ε/2. Si $2kD>0$, tomar además malla<ε/(4kD), que da diferencia<ε/2. El mínimo de los dos radios sirve. Si $2kD=0$, las sumas coinciden y basta el radio de $f$.

## 22.35. De universal a una sucesión

[]{#MA-EX-ANM-01-022-035}

[]{#MA-SOL-ANM-01-022-035}

Para ε, obtener δ del contrato universal; la convergencia de mallas da un índice tras el cual todas son<δ. Entonces todos los errores son<ε, que es convergencia a $I$. Invertir esta prueba no es válido: el control de una sola lista de particiones/etiquetas no abarca todas las demás.

## 22.36. Una integral sin antiderivada

[]{#MA-EX-ANM-01-022-036}

[]{#MA-SOL-ANM-01-022-036}

[]{#MA-SEC-ANM-01-022-008}

En cada pieza, media por anchura es $(v^2-u^2)/2$; sumar telescopa a $(4-1)/2=3/2$. Cualquier etiqueta difiere de la media≤anchura/2, por lo que el error total≤$(1/2)\sum\Delta_i^2\le(3/2)\|P\|$. El contrato con ese certificado prueba el valor3/2.

## 22.37. Afín y firmada

[]{#MA-EX-ANM-01-022-037}

[]{#MA-SOL-ANM-01-022-037}

La suma es dos veces la de $x$ menos1, pues las anchuras suman1. El valor candidato es $2(1/2)-1=0$. El error≤$2\cdot\|P\|/2=\|P\|$. Escoger radioε prueba el contrato; no se ha interpretado el resultado como área geométrica total.

## 22.38. El cubo controla el cuadrado

[]{#MA-EX-ANM-01-022-038}

[]{#MA-SOL-ANM-01-022-038}

En $[u,v]$, la media $(u^2+uv+v^2)/3$ está entre $u^2,v^2$, igual que $\xi^2$. La diferencia≤$v^2-u^2\le2(v-u)$. Multiplicar por anchura y comparar con $(v^3-u^3)/3$ da error≤$2\Delta^2$. Sumar telescopa a1/3 y error≤$2\|P\|$. Para ε tomarδ=ε/2.

## 22.39. Cuatro piezas no son el límite

[]{#MA-EX-ANM-01-022-039}

[]{#MA-SOL-ANM-01-022-039}

Izquierda: $(0+1+4+9)/64=7/32$. Derecha: $(1+4+9+16)/64=15/32$. Media: $(1+9+25+49)/256=21/64$. Para todo n, inducción de $\sum i=n(n+1)/2$ y $\sum i^2=n(n+1)(2n+1)/6$, expandir $(i-1)^2$ o $(i-1/2)^2$ da las fórmulas del texto;21/64=1/3−1/192. Ninguna de estas sumas finitas es el límite1/3.

## 22.40. Resolución de una tolerancia

[]{#MA-EX-ANM-01-022-040}

[]{#MA-SOL-ANM-01-022-040}

La cota universal es2/n, así que n201 da2/201<1/100 para cualquier etiqueta. El error medio exacto es1/(12·201²), mucho menor. La cota universal sirve aun al mezclar etiquetas arbitrarias; usar sólo el error medio no certifica las demás familias.

**Retorno visual.** Véase [C22-F08](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-microcontroles.html)
