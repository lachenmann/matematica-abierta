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
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C22_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html)

## 22.1. Lista o dibujo

[]{#MA-EX-ANM-01-022-001}

[]{#MA-SOL-ANM-01-022-001}

[]{#MA-SEC-ANM-01-022-001}

La lista $(0,1/2,1)$ cumple $0<1/2<1$ y conserva los dos extremos, así es una partición. En $(0,1/2,1/2,1)$ aparece una comparación de igualdad y la anchura correspondiente es cero. La tercera lista tiene $3/4>1/4$, por lo que deja de crecer y produce una anchura negativa. Sólo la primera satisface todas las condiciones del contrato.

## 22.2. Longitudes que telescopan

[]{#MA-EX-ANM-01-022-002}

[]{#MA-SOL-ANM-01-022-002}

Las anchuras son $-1/4-(-1)=3/4$, $1/2-(-1/4)=3/4$ y $2-1/2=3/2$. Su suma vale $3=2-(-1)$. Para una pieza, la suma general es $x_1-x_0$. Si hasta la pieza $r$ vale $x_r-x_0$, añadir $x_{r+1}-x_r$ deja $x_{r+1}-x_0$. La inducción finita prueba la identidad de longitudes para cualquier partición.

**Retorno visual.** Véase [C22-F01](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.3. Una entrada en su pieza

[]{#MA-EX-ANM-01-022-003}

[]{#MA-SOL-ANM-01-022-003}

Cero queda en $[-1/4,1/2]$, la segunda pieza, y dos en $[1/2,2]$, la última. Para una entrada $t<b$, el conjunto de índices con $t<x_j$ es no vacío porque contiene a $n$. Su mínimo $j$ es positivo y la minimalidad da $x_{j-1}\le t<x_j$. Para $t=b$ se usa directamente la última pieza, existente porque $n\ge1$. Así todo el segmento queda cubierto.

## 22.4. Cerrar no es separar

[]{#MA-EX-ANM-01-022-004}

[]{#MA-SOL-ANM-01-022-004}

Las piezas cerradas comparten sus nodos interiores: un tercio está en las dos primeras y dos tercios en las dos últimas. Una cobertura disjunta es $[0,1/3]$, $(1/3,2/3]$ y $(2/3,1]$. Los nodos compartidos se asignan ahora a una sola pieza y las demás entradas conservan su ubicación. La unión sigue siendo $[0,1]$ y las longitudes son las mismas.

## 22.5. El tipo de los objetos

[]{#MA-EX-ANM-01-022-005}

[]{#MA-SOL-ANM-01-022-005}

Una partición puede codificarse por $(n,p)$, donde $n\in\mathbb N$, $n\ge1$ y $p:\{0,\ldots,n\}\to[a,b]$. Los grafos de esas funciones pertenecen al conjunto $\mathcal P(\mathbb N\times[a,b])$, así un ambiente para los códigos es $\mathbb N\times\mathcal P(\mathbb N\times[a,b])$. Separar los códigos con extremos $p(0)=a$, $p(n)=b$ y crecimiento estricto define el conjunto de particiones. El código con $n=1$ y valores $a,b$ pertenece a él porque $a<b$.

## 22.6. Insertar sin repetir

[]{#MA-EX-ANM-01-022-006}

[]{#MA-SOL-ANM-01-022-006}

[]{#MA-SEC-ANM-01-022-002}

Las desigualdades $1/4<2/5<3/4$ localizan la inserción en la segunda pieza. La nueva lista es $(0,1/4,2/5,3/4,1)$. Sus dos anchuras nuevas son $2/5-1/4=3/20$ y $3/4-2/5=7/20$, ambas positivas y con suma $1/2$. Las otras dos anchuras siguen siendo $1/4$. Se conserva cada corte antiguo y se añade una pieza.

## 22.7. La unión que compara

[]{#MA-EX-ANM-01-022-007}

[]{#MA-SOL-ANM-01-022-007}

La unión de nodos ordenada es $(0,1/3,1/2,2/3,1)$. Contiene ambas listas originales, por lo que las refina. Cualquier refinamiento común debe contener cada nodo de una u otra y por tanto esta unión; de ahí que sea el menor. Las anchuras son $1/3,1/6,1/6,1/3$, todas positivas y con suma uno.

**Retorno visual.** Véase [C22-F02](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.8. Un nodo antiguo

[]{#MA-EX-ANM-01-022-008}

[]{#MA-SOL-ANM-01-022-008}

El punto medio ya pertenece al conjunto de nodos. Insertar una segunda copia produciría dos coordenadas consecutivas iguales y anchura cero. La inserción válida deja la lista $(0,1/2,1)$ como estaba. Su conjunto ordenado de nodos no contiene una nueva pieza.

## 22.9. Orden de resolución

[]{#MA-EX-ANM-01-022-009}

[]{#MA-SOL-ANM-01-022-009}

Reflexividad y transitividad proceden de las mismas propiedades de inclusión de conjuntos de nodos. Para antisimetría, $P\preceq Q$ y $Q\preceq P$ implican $V(P)=V(Q)$. Un conjunto finito de reales tiene una única lista estrictamente creciente: su primera entrada es el mínimo y, al retirarla, la inducción determina las restantes. Así las listas y sus longitudes coinciden y $P=Q$.

## 22.10. Mover no es añadir

[]{#MA-EX-ANM-01-022-010}

[]{#MA-SOL-ANM-01-022-010}

La segunda lista no contiene el nodo $1/2$ y la primera no contiene $1/3$ ni $2/3$. Ninguna conserva todos los nodos de la otra, así son incomparables bajo refinamiento. Su unión ordenada sí da un refinamiento común. Mover un corte o comparar sólo el número de piezas no sustituye la inclusión requerida.

## 22.11. Máximo o promedio

[]{#MA-EX-ANM-01-022-011}

[]{#MA-SOL-ANM-01-022-011}

[]{#MA-SEC-ANM-01-022-003}

Las anchuras son $1/4$ y $3/4$, por lo que la malla es $3/4$ y el promedio $1/2$. En general, cada $\Delta_i\le\|P\|$. Sumar las $n$ desigualdades y usar telescopía da $b-a\le n\|P\|$. La copia real de $n\ge1$ es positiva, y dividir entrega $(b-a)/n\le\|P\|$.

## 22.12. Cada hija tiene padre

[]{#MA-EX-ANM-01-022-012}

[]{#MA-SOL-ANM-01-022-012}

Sean $u<v$ dos nodos consecutivos de $Q$. Ningún nodo de $P$ puede quedar estrictamente entre ellos, pues también sería nodo de $Q$. Por ello la pieza $[u,v]$ está contenida en algún padre de $P$. Su anchura no supera la del padre, que a su vez no supera $\|P\|$. Tomar el máximo de todas las anchuras nuevas da $\|Q\|\le\|P\|$.

**Retorno visual.** Véase [C22-F03](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.13. Más piezas, mismo defecto

[]{#MA-EX-ANM-01-022-013}

[]{#MA-SOL-ANM-01-022-013}

Para $k\ge0$ tomamos los nodos cero, un medio y $1/2+j/2^{k+1}$ para $1\le j\le2^k$. Los nuevos cortes sólo subdividen la mitad derecha y los cortes anteriores se conservan. La mitad izquierda sigue siendo una pieza de anchura $1/2$, mientras todas las derechas miden $1/2^{k+1}\le1/2$. La malla es siempre $1/2$, aunque el número de piezas $2^k+1$ crece sin cota.

## 22.14. Resolución prescrita

[]{#MA-EX-ANM-01-022-014}

[]{#MA-SOL-ANM-01-022-014}

El segmento tiene longitud tres. Una uniforme de treinta y una piezas tiene nodos $x_i=-1+3i/31$ y anchura $3/31<1/10$. Su lista es estrictamente creciente y va de menos uno a dos. Con treinta piezas se obtendría malla exactamente $1/10$, insuficiente para el pedido estricto.

## 22.15. Conservar y mejorar

[]{#MA-EX-ANM-01-022-015}

[]{#MA-SOL-ANM-01-022-015}

Arquimedianidad da un natural $n>(b-a)/\delta$, y la uniforme $U_n$ cumple $\|U_n\|<\delta$. Formamos el refinamiento común $R$ con los nodos de $P$ y $U_n$. Conserva todos los cortes de $P$ y su malla no supera la de $U_n$. Por tanto $P\preceq R$ y $\|R\|<\delta$.

## 22.16. Lineal con tres etiquetas

[]{#MA-EX-ANM-01-022-016}

[]{#MA-SOL-ANM-01-022-016}

[]{#MA-SEC-ANM-01-022-004}

Las dos anchuras son $1/2$. Las etiquetas izquierdas $(0,1/2)$ dan $0\cdot1/2+(1/2)\cdot1/2=1/4$. Las medias $(1/4,3/4)$ dan $1/2$, y las derechas $(1/2,1)$ dan $3/4$. La función y partición son las mismas; sólo cambia la familia de alturas. Estas sumas finitas todavía no son iguales entre sí.

## 22.17. Acumular con signo

[]{#MA-EX-ANM-01-022-017}

[]{#MA-SOL-ANM-01-022-017}

Para $2x-1$, las alturas izquierdas son menos uno y cero, las medias menos un medio y un medio, y las derechas cero y uno. Ponderar cada pareja por las anchuras $1/2$ produce sumas $-1/2$, cero y $1/2$. En la media se cancelan contribuciones $-1/4$ y $1/4$. El resultado describe acumulación firmada; las magnitudes geométricas de ambas regiones no se cancelarían.

**Retorno visual.** Véase [C22-F04](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.18. Álgebra de una suma

[]{#MA-EX-ANM-01-022-018}

[]{#MA-SOL-ANM-01-022-018}

Con partición y etiquetas fijas, sustituimos $(\alpha f+\beta g)(\xi_i)=\alpha f(\xi_i)+\beta g(\xi_i)$. La distributividad de sumas finitas da $S(\alpha f+\beta g)=\alpha S(f)+\beta S(g)$. Si $f\le g$, cada término $(g(\xi_i)-f(\xi_i))\Delta_i$ es no negativo porque la anchura es positiva. Sumar prueba $S(f)\le S(g)$.

## 22.19. Compartir una etiqueta

[]{#MA-EX-ANM-01-022-019}

[]{#MA-SOL-ANM-01-022-019}

La etiqueta $1/2$ pertenece tanto a $[0,1/2]$ como a $[1/2,1]$, así es válida en ambas. Para el cuadrado, ambas alturas valen $1/4$. La suma es $(1/4)(1/2)+(1/4)(1/2)=1/4$. Las etiquetas siguen siendo dos datos indexados aunque coincida su coordenada.

## 22.20. Cota sin máximo

[]{#MA-EX-ANM-01-022-020}

[]{#MA-SOL-ANM-01-022-020}

La longitud de $[-1,2]$ es tres. Comparar las alturas con constantes da $-2\cdot3\le S\le3\cdot3$, es decir $-6\le S\le9$. La triangular y $|f|\le3$ dan además $|S|\le9$. Las barreras protegen todas las entradas sin exigir que exista un argumento de máximo o mínimo.

## 22.21. Etiquetas que cambian

[]{#MA-EX-ANM-01-022-021}

[]{#MA-SOL-ANM-01-022-021}

[]{#MA-SEC-ANM-01-022-005}

Restar sumas con las mismas anchuras da $S_\xi-S_\eta=\sum_i(f(\xi_i)-f(\eta_i))\Delta_i$. Por triangular, su magnitud no supera $\sum_i|f(\xi_i)-f(\eta_i)|\Delta_i$. Para la identidad, cada diferencia es $|\xi_i-\eta_i|\le\Delta_i$. En $[0,1]$ resulta $|S_\xi-S_\eta|\le\sum_i\Delta_i^2\le\|P\|$, porque las anchuras suman uno.

## 22.22. De muestras a todas las entradas

[]{#MA-EX-ANM-01-022-022}

[]{#MA-SOL-ANM-01-022-022}

En una pieza de longitud positiva tomamos dos entradas muestreadas y una tercera distinta. Una función puede valer cero en las dos primeras y una altura $H$ arbitrariamente grande en la tercera. Las muestras coinciden exactamente, pero usar la tercera como etiqueta cambia su contribución en $H$ por la anchura. La cota local que protege cualquier etiqueta debe limitar todas las parejas de entradas de la pieza.

## 22.23. Comparar con hijas

[]{#MA-EX-ANM-01-022-023}

[]{#MA-SOL-ANM-01-022-023}

En cada padre $I_i$, las anchuras de sus hijas suman $\Delta_i$. Reescribimos la contribución antigua como $\sum_{J\subseteq I_i}f(\xi_i)|J|$. La etiqueta de cada hija y la antigua están en ese padre, de modo que Lipschitz limita su diferencia de alturas por $L\Delta_i$. Ponderar por las longitudes hijas y sumar da $L\Delta_i^2$. Finalmente, la triangular entrega $|S_P-S_Q|\le L\sum_i\Delta_i^2\le L\|P\|(b-a)$.

## 22.24. Una suma puede ir a ambos lados

[]{#MA-EX-ANM-01-022-024}

[]{#MA-SOL-ANM-01-022-024}

La partición trivial $(0,1)$ con etiqueta media produce suma $1/2$ para la identidad. En el refinamiento $(0,1/2,1)$, las etiquetas izquierdas producen $1/4$ y las derechas $3/4$. Una queda por debajo y otra por encima de la suma antigua. Refinar conserva cortes, pero no decide un sentido de cambio para sumas etiquetadas.

**Retorno visual.** Véase [C22-F05](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.25. Dos resoluciones distintas

[]{#MA-EX-ANM-01-022-025}

[]{#MA-SOL-ANM-01-022-025}

Tomamos el refinamiento común y una familia explícita de etiquetas en él, por ejemplo las izquierdas. Cada suma original se compara con esa tercera usando su malla y la barrera Lipschitz tres. La triangular da $|S_P-S_Q|\le3\cdot2(\|P\|+\|Q\|)\le6(1/10+1/20)=9/10$. La cota protege todas las etiquetas originales y no identifica todavía un valor integral.

## 22.26. Un escalón firmado

[]{#MA-EX-ANM-01-022-026}

[]{#MA-SOL-ANM-01-022-026}

[]{#MA-SEC-ANM-01-022-006}

La acumulación es $A=2(1/3)+(-1)(2/3)=0$. Insertar un corte $t$ dentro de una región constante de altura $c$ conserva su contribución porque $c(t-u)+c(v-t)=c(v-u)$. Las demás regiones quedan intactas. Los valores nodales arbitrarios no aparecen en esta fórmula; su efecto sobre sumas etiquetadas se controla por otro argumento.

## 22.27. Una etiqueta excepcional

[]{#MA-EX-ANM-01-022-027}

[]{#MA-SOL-ANM-01-022-027}

Las dos etiquetas iguales a un medio leen la altura excepcional diez. Con anchuras medias, $S=10/2+10/2=10$. Las constantes interiores de ambos lados son cero y su acumulación $A$ es cero. Esta diferencia pertenece a una suma concreta de malla $1/2$; al reducir la malla el certificado limita cuánto pueden pesar etiquetas excepcionales.

**Retorno visual.** Véase [C22-F06](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.28. Dos piezas por punto

[]{#MA-EX-ANM-01-022-028}

[]{#MA-SOL-ANM-01-022-028}

Un término sólo cambia si su etiqueta es alguno de los $k$ puntos modificados. Cada punto pertenece como máximo a dos piezas cerradas, así hay a lo sumo $2k$ términos afectados. Cada uno tiene magnitud a lo sumo $D\Delta_i\le D\|P\|$. La triangular da $|S_f-S_g|\le2kD\|P\|$. Si $k=0$ o $D=0$, las sumas coinciden.

## 22.29. Sin alinear los cortes

[]{#MA-EX-ANM-01-022-029}

[]{#MA-SOL-ANM-01-022-029}

Refinamos $P$ añadiendo los $m+1$ nodos del escalón y calculamos $A$ con sus constantes interiores en las piezas hijas. Un padre que no toca esos nodos queda dentro de una región constante y aporta exactamente lo mismo que sus hijas. Los padres restantes son a lo sumo $2(m+1)$ y su longitud total no supera $2(m+1)\|P\|$. En cada uno, la diferencia entre su altura y cualquier altura hija no supera $2B$. Ponderar y sumar produce $|S-A|\le4B(m+1)\|P\|$, aun si el recuento repite algún padre.

## 22.30. Representación duplicada

[]{#MA-EX-ANM-01-022-030}

[]{#MA-SOL-ANM-01-022-030}

Una única pieza de longitud dos y altura tres aporta seis. Con cortes $1/2$ y $3/2$, las anchuras son $1/2$, uno y $1/2$, y las contribuciones $3/2$, tres y $3/2$ suman seis. La identidad de longitudes explica esta igualdad para cualquier subdivisión de una región constante. Dos representaciones generales se comparan mediante su refinamiento común.

## 22.31. El orden de los cuantificadores

[]{#MA-EX-ANM-01-022-031}

[]{#MA-SOL-ANM-01-022-031}

[]{#MA-SEC-ANM-01-022-007}

El contrato pide un real $I$ tal que para cada $\varepsilon>0$ exista $\delta>0$ y para toda partición etiquetada con $\|P\|<\delta$ se cumpla $|S-I|<\varepsilon$. Si se permite elegir el radio después de una partición particular, puede tomarse $\delta\le\|P\|$ y dejar falsa la premisa de esa implicación. Ese truco no controla las particiones realmente finas. El radio debe responder a la tolerancia antes de examinar cualquier partición o etiqueta.

## 22.32. Un valor único

[]{#MA-EX-ANM-01-022-032}

[]{#MA-SOL-ANM-01-022-032}

Si $I\ne J$, fijamos $d=|I-J|>0$ y obtenemos radios para error $d/3$ de ambos contratos. Arquimedianidad da una uniforme de malla menor que su mínimo. Con etiquetas izquierdas explícitas, su suma $S$ cumple ambos errores. La triangular da $d\le|I-S|+|S-J|<2d/3$, contradicción. La partición construida muestra que la prueba aplica a una suma existente.

## 22.33. Un radio efectivo

[]{#MA-EX-ANM-01-022-033}

[]{#MA-SOL-ANM-01-022-033}

La barrera cinco pide malla estrictamente menor que $(1/100)/5=1/500$. Por ello sirve radio $\delta=1/500$. Una uniforme de quinientas una piezas en $[0,1]$ tiene malla $1/501<\delta$ y garantiza el desafío. Con quinientas, la cota sólo daría error menor o igual que $1/100$, insuficiente para garantizar estrictitud.

**Retorno visual.** Véase [C22-F07](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 22.34. Cambiar finitos valores

[]{#MA-EX-ANM-01-022-034}

[]{#MA-SOL-ANM-01-022-034}

Con los mismos datos, $|S_g-I|\le|S_g-S_f|+|S_f-I|$. Pedimos primero a la integrabilidad de $f$ un radio para error $\varepsilon/2$. Si $kD>0$, la cota de modificación finita queda menor que $\varepsilon/2$ al exigir además malla menor que $\varepsilon/(4kD)$. El mínimo de ambos radios protege cualquier suma de $g$. Si $kD=0$, las sumas coinciden y basta el primer radio. Así $g$ cumple el contrato con el mismo $I$.

## 22.35. De universal a una sucesión

[]{#MA-EX-ANM-01-022-035}

[]{#MA-SOL-ANM-01-022-035}

Para una tolerancia $\varepsilon$, el contrato universal entrega $\delta>0$. Como las mallas dadas tienden a cero, existe un índice $N$ desde el que todas son menores que $\delta$. Sus sumas, con las etiquetas dadas, cumplen entonces $|S_r-I|<\varepsilon$. Esto prueba convergencia a $I$. Una sola sucesión de datos no controla por ese argumento las otras particiones y etiquetas cuantificadas por el contrato.

## 22.36. Una integral sin antiderivada

[]{#MA-EX-ANM-01-022-036}

[]{#MA-SOL-ANM-01-022-036}

[]{#MA-SEC-ANM-01-022-008}

En cada pieza $[u,v]$, la contribución media de la identidad vale $(u+v)(v-u)/2=(v^2-u^2)/2$. La suma telescópica en $[-1,2]$ es $(4-1)/2=3/2$. Cualquier etiqueta dista del medio a lo sumo media anchura, así su error total no supera $(1/2)\sum_i\Delta_i^2\le(3/2)\|P\|$. Para una tolerancia $\varepsilon$ sirve radio $2\varepsilon/3$. El contrato prueba integral $3/2$ sin antiderivadas.

## 22.37. Afín y firmada

[]{#MA-EX-ANM-01-022-037}

[]{#MA-SOL-ANM-01-022-037}

La linealidad finita da $S(2x-1)=2S(x)-1$ en $[0,1]$. El certificado de la identidad ofrece candidato $1/2$ y error a lo sumo $\|P\|/2$. Por tanto el nuevo candidato es cero y $|S(2x-1)|\le\|P\|$. El radio $\delta=\varepsilon$ satisface el contrato para todas las etiquetas. El valor cero representa una cancelación firmada de contribuciones.

## 22.38. El cubo controla el cuadrado

[]{#MA-EX-ANM-01-022-038}

[]{#MA-SOL-ANM-01-022-038}

En una pieza $[u,v]\subseteq[0,1]$, tanto $\xi^2$ como $(u^2+uv+v^2)/3$ quedan entre $u^2$ y $v^2$. Su diferencia de magnitudes no supera $v^2-u^2=(v-u)(v+u)\le2(v-u)$. Multiplicar por la anchura compara la contribución etiquetada con $(v^3-u^3)/3$ con error a lo sumo $2\Delta_i^2$. Los incrementos cúbicos telescopan a $1/3$ y la triangular da $|S-1/3|\le2\|P\|$. Para $\varepsilon>0$, el radio $\varepsilon/2$ prueba el contrato.

## 22.39. Cuatro piezas no son el límite

[]{#MA-EX-ANM-01-022-039}

[]{#MA-SOL-ANM-01-022-039}

Para cuatro piezas, las sumas de bordes son $(0+1+4+9)/64=7/32$ y $(1+4+9+16)/64=15/32$. Las medias producen $(1+9+25+49)/256=21/64$. Las identidades finitas $\sum_{i=1}^n i=n(n+1)/2$ y $\sum_{i=1}^n i^2=n(n+1)(2n+1)/6$ se prueban por inducción sumando el término siguiente. Sustituirlas da sumas izquierda $1/3-1/(2n)+1/(6n^2)$, derecha $1/3+1/(2n)+1/(6n^2)$ y media $1/3-1/(12n^2)$. En $n=4$ esta última difiere de $1/3$ en $1/192$. Las tres cuentas son sumas finitas y no el valor límite.

## 22.40. Resolución de una tolerancia

[]{#MA-EX-ANM-01-022-040}

[]{#MA-SOL-ANM-01-022-040}

La uniforme de doscientas una piezas tiene malla $1/201$. El certificado universal da error a lo sumo $2/201<1/100$ para cualquier etiqueta. Las medias de esa misma partición tienen error exacto $1/(12\cdot201^2)$, mucho menor. Esa mejora depende de usar las medias y no protege una familia arbitraria de etiquetas. La elección de resolución universal utiliza la barrera que sí cubre todas.

**Retorno visual.** Véase [C22-F08](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html)

