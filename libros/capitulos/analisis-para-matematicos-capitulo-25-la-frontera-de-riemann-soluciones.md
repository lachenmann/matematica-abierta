---
content-id: MA-BCH-0304
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-025-SOLUCIONES
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
title: Soluciones — Capítulo 25
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C25_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)

## 25.1. Longitud de las piezas malas

[]{#MA-EX-ANM-01-025-001}

[]{#MA-SOL-ANM-01-025-001}

[]{#MA-SEC-ANM-01-025-001}

En las malas, $\omega_i\Delta_i\ge\eta\Delta_i$; sumar esos términos y conservar los restantes no negativos da $\eta\lambda\le G$. En las buenas, cada término es menor que $\eta\Delta_i$, luego a lo sumo esa cota. En las malas la cota global es $2B\Delta_i$. Sumar y usar que todas las anchuras suman $b-a$ da $G\le\eta(b-a)+2B\lambda$.

**Retorno visual.** Véase [C25-F01](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.2. Oscilación puntual y continuidad

[]{#MA-EX-ANM-01-025-002}

[]{#MA-SOL-ANM-01-025-002}

Si f es continua, para cualquier ε>0 una vecindad tiene errores de centro menores que ε/3. Dos valores difieren menos que 2ε/3, y la oscilación es a lo sumo esa cantidad; el ínfimo no negativo es cero. Si el ínfimo es cero, para cada ε>0 existe una oscilación de vecindad menor que ε por la propiedad del ínfimo. El valor central está entre sus cotas, así todas las diferencias de salida respecto de él son menores que ε. Esto da continuidad con ese radio testigo.

## 25.3. Nivel cerrado

[]{#MA-EX-ANM-01-025-003}

[]{#MA-SOL-ANM-01-025-003}

Para un centro fuera del nivel, una vecindad tiene oscilación menor que η por la propiedad del ínfimo. Si su radio es r, un centro a distancia menor que r/2 admite una vecindad de radio pequeño contenida en la primera. Su oscilación puntual es menor que η, por restricción. El complemento del nivel es abierto relativo. Cerrado relativo de un compacto es compacto por C16, incluyendo el caso vacío.

## 25.4. Un presupuesto numérico

[]{#MA-EX-ANM-01-025-004}

[]{#MA-SOL-ANM-01-025-004}

R1 da $G\le(1/10)3+2\cdot2\cdot(1/100)=3/10+1/25=17/50$. No es necesariamente exacta: las oscilaciones buenas pueden ser mucho menores y las malas no alcanzar4. La cota requiere control de todas las piezas, no una tabla de muestras.

## 25.5. Nodos y oscilación

[]{#MA-EX-ANM-01-025-005}

[]{#MA-SOL-ANM-01-025-005}

Las piezas son cerradas y ambos vecinos contienen el nodo. Si el valor allí difiere de los demás, ambas imágenes pueden tener una nueva altura extrema y mayor oscilación. La longitud sigue siendo suma de anchuras de piezas, sin término del singleton. Por cambios finitos de C23 el valor integral, cuando existe, no cambia.

## 25.6. Collares de un conjunto finito

[]{#MA-EX-ANM-01-025-006}

[]{#MA-SOL-ANM-01-025-006}

[]{#MA-SEC-ANM-01-025-002}

Con k>0, centre un intervalo de radio $r=\sigma/[4(k+1)]$ en cada punto. La suma de longitudes es $2kr=\sigma k/[2(k+1)]<\sigma$. Con k0 use la cobertura vacía, de longitud cero. Positividad del denominador evita excepciones o división por k.

## 25.7. Fabricar una escala común

[]{#MA-EX-ANM-01-025-007}

[]{#MA-SOL-ANM-01-025-007}

Forme el conjunto de todos los pares centro/radio que cumplen una de dos propiedades: vecindad grande dentro de los collares, o de oscilación menor que η. Cada centro admite alguno por apertura o continuidad, así sus vecindades medias cubren el segmento. C16 extrae finitísimos pares; mínimo de sus radios medios es positivo. Una pieza de malla menor queda entera dentro de una vecindad grande que contiene alguno de sus puntos.

## 25.8. El escalón y su brecha

[]{#MA-EX-ANM-01-025-008}

[]{#MA-SOL-ANM-01-025-008}

La pieza anterior al corte de anchura r tiene ínfimo0 y supremo1 porque incluye el nodo de valor1. La posterior es constante1; las otras son constantes en su lado. Así $L=1/2$, $U=1/2+r$ y $G=r$ para el valor nodal1. La cota general2r de R2 sigue siendo válida, pero aquí no es igualdad. Si el nodo tuviera otro valor, hay que recalcular las dos piezas cerradas. La integral vale1/2 por C23.

**Retorno visual.** Véase [C25-F02](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.9. La hipótesis de acotación

[]{#MA-EX-ANM-01-025-009}

[]{#MA-SOL-ANM-01-025-009}

En[0,1], tome h(0)=0 y h(x)=1/x para x>0. Es continua fuera del punto0. Para cualquier B>0, una entrada positiva menor que1/(B+1) da h(x)>B. No es acotada, mientras C23 probó que integrabilidad propia fuerza acotación. La afirmación sin esa premisa es falsa.

## 25.10. Gastar la tolerancia

[]{#MA-EX-ANM-01-025-010}

[]{#MA-SOL-ANM-01-025-010}

La longitud mala es menor que σ y las oscilaciones buenas menores que η. Usando la cota no estricta de R1 queda $G\le\eta(b-a)+2B\sigma=\varepsilon/2+B\varepsilon/[2(B+1)]<\varepsilon$ porque B/(B+1)<1. Si B0, ya G0 y la misma cota es menor que ε. El argumento no divide por B.

## 25.11. Racionales en toda pieza

[]{#MA-EX-ANM-01-025-011}

[]{#MA-SOL-ANM-01-025-011}

[]{#MA-SEC-ANM-01-025-003}

Elija n positivo con n(v−u)>1. Elija M natural con nu+M≥0. Sea j el menor natural estrictamente mayor que nu+M; existe por arquimedianidad, j>0 y j−1≤nu+M por minimalidad. Entonces nu<j−M≤nu+1<nv. El entero k=j−M produce el racional k/n interior. Se ha construido un testigo para el intervalo fijado.

## 25.12. Irracionales en toda pieza

[]{#MA-EX-ANM-01-025-012}

[]{#MA-SOL-ANM-01-025-012}

Si q∈(u,v) es racional, elija n positivo con raíz2/n<v−q. La entrada z=q+raíz2/n satisface u<z<v. Si fuera racional, n(z−q) sería racional e igual a raíz2, contradicción. La existencia de la raíz y la prueba por paridad se declaran herramientas aritméticas heredadas.

## 25.13. La longitud correcta

[]{#MA-EX-ANM-01-025-013}

[]{#MA-SOL-ANM-01-025-013}

Todas las piezas no degeneradas contienen valores0 y1 por densidad; m0,M1. Por tanto L0,UΣΔ=3,G3 para toda partición. El criterio falla con ε=3/2: ninguna brecha es menor que ella. La suma superior no es1 en ese intervalo.

**Retorno visual.** Véase [C25-F03](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.14. Etiquetas incompatibles

[]{#MA-EX-ANM-01-025-014}

[]{#MA-SOL-ANM-01-025-014}

Para cualquier radio de malla, construya una partición uniforme más fina por C22. Finitas elecciones de racionales e irracionales en cada pieza dan dos familias de etiquetas con sumas b−a y0. Si un candidato I cumpliera error menor que ε=(b−a)/3 para ambas, triangular daría b−a<2(b−a)/3, contradicción. Ninguna malla resuelve el problema.

## 25.15. Una muestra no prueba densidad

[]{#MA-EX-ANM-01-025-015}

[]{#MA-SOL-ANM-01-025-015}

Una figura tiene finitísimos puntos y puede dejar una pieza sin ningún punto representado de uno de los tipos. Las cotas requieren existencia de racional e irracional en toda pieza real no degenerada. Eso se prueba aritméticamente para un intervalo arbitrario, no se deduce de densidad aparente de un gráfico.

## 25.16. Contar picos de denominador pequeño

[]{#MA-EX-ANM-01-025-016}

[]{#MA-SOL-ANM-01-025-016}

[]{#MA-SEC-ANM-01-025-004}

Cada denominador q entre1 yN admite a lo sumo q+1 numeradores0≤p≤q; la suma es N(N+1)/2+N=N(N+3)/2. Reducir fracciones y eliminar duplicados sólo baja el número. E4=(0,1/4,1/3,1/2,2/3,3/4,1), con7 entradas, menor que la cota14.

**Retorno visual.** Véase [C25-F04](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.17. Un irracional evita picos grandes

[]{#MA-EX-ANM-01-025-017}

[]{#MA-SOL-ANM-01-025-017}

Dado ε>0, elija N con1/(N+1)<ε. Todas las distancias entre el irracional x y el conjunto finito E_N son positivas; su mínimo d es positivo. El radio d/2 evita esos puntos. Fuera de ellos T≤1/(N+1), y T(x)=0, por lo que el error de salida es menor que ε. Si el conjunto fuera vacío, cualquier radio positivo serviría.

## 25.18. Oscilación en un racional

[]{#MA-EX-ANM-01-025-018}

[]{#MA-SOL-ANM-01-025-018}

Toda vecindad contiene el centro de valor1/q y un irracional de valor0, así su oscilación es al menos1/q. Un radio que evite E_q salvo el centro deja todos los demás valores≤1/(q+1), de modo que la oscilación de esa vecindad es exactamente1/q. El ínfimo es ese valor. Además, los irracionales arbitrariamente cercanos violan continuidad con tolerancia1/(2q).

## 25.19. Un certificado para Thomae

[]{#MA-EX-ANM-01-025-019}

[]{#MA-SOL-ANM-01-025-019}

Las piezas del primer grupo tienen supremo≤1 y contribuyen≤α. Las demás tienen supremo≤1/(N+1), y su anchura total≤1. Sumar da la cota. Por densidad irracional L0. Si los dos términos se hacen menores que ε/2 mediante N y collares, la brecha es menor que ε y la integral es cero.

## 25.20. Discontinuidades densas, integral cero

[]{#MA-EX-ANM-01-025-020}

[]{#MA-SOL-ANM-01-025-020}

Ambas son discontinuas en racionales; Dirichlet también lo es en irracionales porque toda vecindad tiene ambos valores0/1. En Thomae los irracionales son continuos y los picos de cada altura positiva están entre finitísimos denominadores. Collares de esos picos y cota del resto hacen U arbitrariamente pequeña. Dirichlet mantiene amplitud1 en todas las piezas y brecha fija1.

## 25.21. Cubrir los niveles desde una brecha

[]{#MA-EX-ANM-01-025-021}

[]{#MA-SOL-ANM-01-025-021}

[]{#MA-SEC-ANM-01-025-005}

Elija P con G<ησ/4. Las piezas con ω≥η suman anchura<σ/4 por R1. Un punto de Dη que no sea nodo está interior a una pieza; si fuera buena, una vecindad contenida allí daría Ω<η. Por tanto el nivel queda en malas y nodos. Si hay n piezas, expandir malas y cubrir los n+1 nodos con radio σ/[8(n+1)] agrega menos que σ/2 de longitud. La cobertura total es menor que3σ/4<σ.

## 25.22. De niveles pequeños a integrabilidad

[]{#MA-EX-ANM-01-025-022}

[]{#MA-SOL-ANM-01-025-022}

Tome η=ε/[2(b−a)], σ=ε/[4(B+1)] y cobertura finita de Dη de longitud<σ. Fuera de su unión O, Ω<η da vecindades buenas; dentro, apertura da vecindades contenidas en O. Todos los pares válidos y radios medios cubren el segmento; C16 da subcubrimiento finito y δ mínimo. Una partición de malla<δ queda pieza a pieza en O o buena. Longitud mala<σ y R1 dan G≤ε/2+Bε/[2(B+1)]<ε; C23 concluye.

## 25.23. No cubrir toda la unión

[]{#MA-EX-ANM-01-025-023}

[]{#MA-SOL-ANM-01-025-023}

En Thomae, cada nivel de oscilación≥η contiene sólo finitísimos racionales de denominador≤1/η. Admite collares arbitrariamente cortos. La unión de todos esos niveles positivos es el conjunto racional, denso, que no admite coberturas abiertas finitas de longitud total<1. El criterio por niveles conserva la integrabilidad demostrada; exigir la propiedad a toda la unión sería más fuerte.

**Retorno visual.** Véase [C25-F05](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.24. Longitud de una cobertura del segmento

[]{#MA-EX-ANM-01-025-024}

[]{#MA-SOL-ANM-01-025-024}

Corte en todos los extremos y en a,b. Las celdas interiores del segmento están cubiertas; cada una contribuye una vez a longitud b−a y al menos una a la suma de longitudes de los intervalos de cobertura que la contienen. Sumar finitamente da la desigualdad. Las fronteras de celdas no agregan anchura. Intervalos redundantes sólo aumentan la suma.

## 25.25. Los casos vacíos

[]{#MA-EX-ANM-01-025-025}

[]{#MA-SOL-ANM-01-025-025}

El vacío usa cobertura vacía. Para k puntos use radios σ/[4(k+1)], cuya suma es menor que σ. Si B0, f0, todas las oscilaciones y niveles positivos son vacíos y G0. Los parámetros con B+1 permanecen positivos y no requieren dividir por una cota nula.

## 25.26. Etapas ternarias

[]{#MA-EX-ANM-01-025-026}

[]{#MA-SOL-ANM-01-025-026}

[]{#MA-SEC-ANM-01-025-006}

En etapa0 hay un segmento de longitud1. Cada componente se sustituye por dos tercios extremos cerrados, cada uno de un tercio de su longitud. Si la etapa n tiene2^n componentes de3^−n, la siguiente tiene2^(n+1) de3^(−n−1). Las componentes no se solapan en interiores. La suma total es2^n3^−n=(2/3)^n.

**Retorno visual.** Véase [C25-F06](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.27. Una cobertura abierta del conjunto final

[]{#MA-EX-ANM-01-025-027}

[]{#MA-SOL-ANM-01-025-027}

Cada C_n es cerrado, luego la intersección C es cerrada por C04 y está en[0,1], compacto por C16. Elija n con(2/3)^n<σ/2. Expanda cada una de sus2^n componentes por radio r<σ/[4·2^n]. La suma ampliada es(2/3)^n+2·2^n r<σ. Todos los puntos de C están en C_n y quedan cubiertos.

## 25.28. Interior vacío

[]{#MA-EX-ANM-01-025-028}

[]{#MA-SOL-ANM-01-025-028}

Si lo contuviera, tendría dentro un segmento de anchura $\ell$>0. Elija n con3^−n<$\ell$. Ese segmento debería estar en C_n. No cabe en una componente y no puede cruzar un hueco abierto entre componentes sin salir de C_n. Contradicción. La prueba vale independientemente de las primeras etapas dibujadas.

## 25.29. Indicadora y discontinuidades

[]{#MA-EX-ANM-01-025-029}

[]{#MA-SOL-ANM-01-025-029}

Fuera de C, su complemento abierto proporciona vecindad constante0. En un punto de C, toda vecindad relativa contiene un punto fuera, por interior vacío, mientras el centro vale1; tolerancia1/2 refuta continuidad. C es compacto de contenido finito nulo, por lo que el lema de soporte prueba integrabilidad y valor0. Los bordes0 y1 se tratan relativamente.

## 25.30. Controlar todas las piezas que tocan el soporte

[]{#MA-EX-ANM-01-025-030}

[]{#MA-SOL-ANM-01-025-030}

La cubierta abierta O contiene E. Todos los radios con vecindad grande dentro de O dan vecindades medias que cubren E; un subcubrimiento finito proporciona δ mínimo radio medio. Si una pieza de malla<δ toca E en t, un centro de la cubierta está a distancia<r/2 de t; cualquier otro punto de la pieza queda a distancia<δ+r/2≤r. Toda la pieza está en O, aun si t era un extremo compartido. Su suma de anchuras se controla por la longitud de la cobertura.

## 25.31. Dos errores de salida, una oscilación

[]{#MA-EX-ANM-01-025-031}

[]{#MA-SOL-ANM-01-025-031}

[]{#MA-SEC-ANM-01-025-007}

Para cualesquiera s,t de I, $f(s)-f(t)\le g(s)-g(t)+2\delta\le\omega(g,I)+2\delta$. Fijando t y tomando supremo de f(s), después tomando ínfimo de f(t), resulta la cota de oscilación. Las imágenes son no vacías acotadas. No se supone que los extremos estén alcanzados.

## 25.32. Aproximantes integrables certifican existencia

[]{#MA-EX-ANM-01-025-032}

[]{#MA-SOL-ANM-01-025-032}

Para ε>0, elija integrable g con error global δ=ε/[4(b−a)]. Elija P de g con brecha<ε/2. La comparación da Gf(P)≤Gg(P)+2δ(b−a)<ε; f es integrable por C23. Ahora, y sólo ahora, linealidad y orden aplicados a f−g dan distancia de integrales≤δ(b−a).

## 25.33. Truncar alturas de Thomae

[]{#MA-EX-ANM-01-025-033}

[]{#MA-SOL-ANM-01-025-033}

T_N coincide con T en E_N y vale0 fuera. Tiene soporte finito, así es integrable con integral0 por C23. En E_N el error es0; fuera de allí T≤1/(N+1), por lo que la cota sirve para todas las entradas. R7 prueba existencia de la integral de T y distancia a0≤1/(N+1) para todo N. Arquimedianidad fuerza valor0.

## 25.34. Estabilizar entradas no controla la familia

[]{#MA-EX-ANM-01-025-034}

[]{#MA-SOL-ANM-01-025-034}

En un racional reducido de denominador q, para N≥q el valor es1; en un irracional siempre0. Ésa es la estabilización requerida para cada entrada. Para cualquier N, hay racionales fuera del conjunto finito E_N, porque todo intervalo contiene infinitos racionales por densidad repetida. En uno de ellos d1 y d_N0, error1. No existe un índice que controle todas las entradas con tolerancia1/2.

**Retorno visual.** Véase [C25-F07](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.35. Regla finita y cambios infinitos

[]{#MA-EX-ANM-01-025-035}

[]{#MA-SOL-ANM-01-025-035}

Thomae y cero difieren sólo en los racionales; la primera es integrable con valor0 por R4/R7. Dirichlet y cero también difieren sólo allí, pero Dirichlet no es integrable por R3. Por tanto la regla de cambios finitos no puede ampliarse a una familia numerable dada sin nueva prueba. No se escribe una integral de Dirichlet inexistente.

## 25.36. Una cobertura de racionales

[]{#MA-EX-ANM-01-025-036}

[]{#MA-SOL-ANM-01-025-036}

[]{#MA-SEC-ANM-01-025-008}

Sea una unión finita de abiertos que cubre los racionales del segmento. Su clausura, unión finita de los correspondientes intervalos cerrados, contiene[0,1] por densidad. Cerrar intervalos no cambia sus longitudes. La longitud del segmento es a lo sumo la suma de longitudes de esa cobertura cerrada, por la prueba finita de cortes. La suma original es por tanto≥1 y no puede ser arbitrariamente pequeña.

## 25.37. Un punto problemático no acotado

[]{#MA-EX-ANM-01-025-037}

[]{#MA-SOL-ANM-01-025-037}

Si integrara propiamente, C23 forzaría una cota finita. Dado B>0, tome x positivo menor que min{1,1/(B+1)}; entonces h(x)>B. Si una cota inicial fuera cero o negativa, basta sustituirla por un número positivo mayor. No existe cota finita, luego no existe esa integral. No se ha afirmado nada sobre otro tipo de integral.

## 25.38. Qué certifica una etapa de Cantor

[]{#MA-EX-ANM-01-025-038}

[]{#MA-SOL-ANM-01-025-038}

La etapa C_n es una unión finita de intervalos con esa longitud total. C está contenido en todas esas etapas, pero muchos puntos de cada una serán eliminados después. Por ello la etapa permite cubrir C con longitud pequeña; no certifica que sus intervalos completos pertenezcan a C ni da una medida construida de la intersección.

## 25.39. Frontera exacta y condición más fuerte

[]{#MA-EX-ANM-01-025-039}

[]{#MA-SOL-ANM-01-025-039}

R5 exige acotación y propiedad de cobertura finita para cada nivel Dη positivo. Si todas las discontinuidades tuvieran la propiedad, también cada Dη, por inclusión, y R5 daría integrabilidad. La recíproca falla en Thomae: niveles finitos y función integrable, pero todas las discontinuidades son racionales, sin contenido finito nulo.

## 25.40. Cerrar sin importar otra integral

[]{#MA-EX-ANM-01-025-040}

[]{#MA-SOL-ANM-01-025-040}

Dirichlet tiene brecha fija porque cada pieza contiene valores0 y1. Thomae separa finitísimos picos grandes de una cota pequeña universal del resto. La indicadora de C confina su soporte compacto con coberturas finitas cortas. No se definió una medida ni una integral de Lebesgue, ni se asignó por otro método un valor a Dirichlet. C26 abrirá la teoría de familias de funciones.

**Retorno visual.** Véase [C25-F08](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)
