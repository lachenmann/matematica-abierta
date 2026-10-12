---
content-id: MA-BCH-0256
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-013-SOLUCIONES
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
title: Soluciones — Capítulo 13
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C13_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-microcontroles.html)

## 13.1. El agujero no decide el destino

[]{#MA-EX-ANM-01-013-001}

[]{#MA-SOL-ANM-01-013-001}

[]{#MA-SEC-ANM-01-013-001}

El candidato es $3$. Para $\varepsilon>0$ tomamos $\delta=\varepsilon/2$. Si $0<|x+1|<\delta$, entonces $x\ne-1$, por lo que $|f(x)-3|=2|x+1|<\varepsilon$. El punto $-1$ acumula entradas reales, por ejemplo $-1+\delta/2$. La definición controla entradas distintas del centro; el valor $100$ no interviene.

**Retorno visual.** Véase [C13-F01](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 13.2. Una pregunta sin entradas

[]{#MA-EX-ANM-01-013-002}

[]{#MA-SOL-ANM-01-013-002}

Con $\delta=1$, no existe $x\in D$ con $0<|x|<1$. La implicación sería verdadera para todo $L$ y toda tolerancia usando ese mismo radio. Pero $0$ no es punto de acumulación de $D$, así que no asignamos límite. El fallo no depende de los valores de $f$: depende de las rutas inexistentes.

## 13.3. Dos lenguajes del mismo control

[]{#MA-EX-ANM-01-013-003}

[]{#MA-SOL-ANM-01-013-003}

Si vale la inclusión de imágenes y $x\in U_D(a,\delta)$, entonces $f(x)\in f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$, luego $x\in f^{-1}[B(L,\varepsilon)]$. A la inversa, si toda entrada de la ventana está en esa preimagen y $y$ pertenece a la imagen, existe un testigo $x$ de la ventana con $y=f(x)$; la pertenencia a la preimagen da $y\in B(L,\varepsilon)$. $f(x)$ es un valor; la imagen y la preimagen son conjuntos.

## 13.4. Igualdad en un germen perforado

[]{#MA-EX-ANM-01-013-004}

[]{#MA-SOL-ANM-01-013-004}

Fijemos un candidato $L$ y supongamos $f\to L$. Para cada $\varepsilon>0$, un radio $\delta_f$ de $f$ se reúne con $r$ mediante $\delta=\min(r,\delta_f)>0$. En la ventana resultante $g(x)=f(x)$ y $|g(x)-L|<\varepsilon$. Luego $g\to L$. Intercambiar $f,g$ prueba la recíproca para ese mismo candidato. Como $L$ era arbitrario, los conjuntos de candidatos coinciden.

## 13.5. Cambiar valores en infinitos puntos lejanos

[]{#MA-EX-ANM-01-013-005}

[]{#MA-SOL-ANM-01-013-005}

Sea $f(x)=0$ para todo real, y sea $g(x)=0$ si $|x|<1$, $g(x)=x^2$ si $|x|\ge1$. Difieren en todos los enteros positivos, un conjunto infinito. $g(n)=n^2$ no admite cota global por arquimedianidad. Ambas coinciden en la ventana de radio $1$; para toda tolerancia, ese radio hace el error cero. La información fuera de una ventana fija no determina el límite.

## 13.6. Diseñar el radio de una afín decreciente

[]{#MA-EX-ANM-01-013-006}

[]{#MA-SOL-ANM-01-013-006}

[]{#MA-SEC-ANM-01-013-002}

El error es $4|x-2|$. $\delta=\varepsilon/4$ sirve porque la entrada satisface una desigualdad estricta. Si $\delta>\varepsilon/4$, tomamos $t=(\delta+\varepsilon/4)/2$ y $x=2+t$. Entonces $0<t<\delta$ y $4t>\varepsilon$, infracción. Por tanto el radio dado es el mayor. El signo de la pendiente invierte orden, pero el error depende de su magnitud.

**Retorno visual.** Véase [C13-F02](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 13.7. Un radio conservador para un cuadrado

[]{#MA-EX-ANM-01-013-007}

[]{#MA-SOL-ANM-01-013-007}

Para $|x-2|<1$, $|x+2|\le|x-2|+4<5$. Dado $\varepsilon>0$, tomamos $\delta=\min(1,\varepsilon/5)$. Entonces $|x^2-4|=|x-2||x+2|<5|x-2|<5\delta\le\varepsilon$. El radio auxiliar elimina el factor variable.

## 13.8. Radio óptimo del cuadrado en uno

[]{#MA-EX-ANM-01-013-008}

[]{#MA-SOL-ANM-01-013-008}

La componente de entradas positivas que satisface el error es $(\sqrt{1-\varepsilon},\sqrt{1+\varepsilon})$. Los márgenes desde $1$ son $1-\sqrt{1-\varepsilon}$ y $\sqrt{1+\varepsilon}-1$. El segundo es menor: racionalizar da $\varepsilon/(1+\sqrt{1-\varepsilon})>\varepsilon/(1+\sqrt{1+\varepsilon})$. Así el intervalo simétrico de radio $\delta_*$ queda dentro de esa componente, pues su extremo inferior supera $\sqrt{1-\varepsilon}$. Si un radio es mayor, incluye $x=\sqrt{1+\varepsilon}$, distinto de $1$, cuyo error es exactamente $\varepsilon$, infracción.

**Retorno visual.** Véase [C13-F03](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 13.9. Reparar una respuesta que depende de la entrada

[]{#MA-EX-ANM-01-013-009}

[]{#MA-SOL-ANM-01-013-009}

La expresión de $\delta$ utiliza el $x$ que debía verificarse después de fijar el radio. No produce una respuesta única para toda la ventana. La reparación fija primero $|x-1|<1$, que da $|x+1|<3$, y elige $\delta=\min(1,\varepsilon/3)$. Para toda entrada de esa ventana, $|x^2-1|<3|x-1|<\varepsilon$. La fórmula defectuosa queda como objeto de diagnóstico, no como prueba.

## 13.10. Proteger un recíproco desplazado

[]{#MA-EX-ANM-01-013-010}

[]{#MA-SOL-ANM-01-013-010}

Si $|x-1|<1$, entonces $|x-3|\ge2-|x-1|>1$; las entradas no alcanzan $3$. El error es $|1/(x-3)+1/2|=|x-1|/(2|x-3|)<|x-1|/2$. Tomamos $\delta=\min(1,2\varepsilon)$. Para toda entrada del dominio dentro de esa ventana, el error es menor que $\delta/2\le\varepsilon$.

## 13.11. Una cota que incluye el centro

[]{#MA-EX-ANM-01-013-011}

[]{#MA-SOL-ANM-01-013-011}

[]{#MA-SEC-ANM-01-013-003}

La tolerancia $1$ entrega $r>0$ con $|f(x)|<|L|+1$ para toda entrada no central de la ventana. Elegimos $K=\max(|L|+1,|f(a)|+1)$. En el centro, $|f(a)|<K$; fuera del centro, la cota previa da $|f(x)|<K$. La unión de ambos casos prueba acotación. Sólo se añadió un valor finito a una cota local.

## 13.12. Encierro sin existencia supuesta

[]{#MA-EX-ANM-01-013-012}

[]{#MA-SOL-ANM-01-013-012}

Las cotas implican $|f(x)|\le2x^2$ en esa ventana. Para $\varepsilon>0$ tomamos $\delta=\min(1,\sqrt{\varepsilon/2})>0$. Si $0<|x|<\delta$, entonces $|f(x)|\le2x^2<2\delta^2\le\varepsilon$. No se supuso que $f$ tuviera límite: el control universal lo establece. Las raíces positivas pertenecen al álgebra real elemental.

## 13.13. Oscilar y aun así converger

[]{#MA-EX-ANM-01-013-013}

[]{#MA-SOL-ANM-01-013-013}

Para toda entrada, $|b(x)|=1$ y $|h(x)|=|x|$. Dado $\varepsilon>0$ basta $\delta=\varepsilon$. Si $0<|x|<\delta$, el error de $h$ es menor que $\varepsilon$. El control procede de la magnitud del factor, no de la existencia de su límite.

## 13.14. El orden no conserva separación estricta

[]{#MA-EX-ANM-01-013-014}

[]{#MA-SOL-ANM-01-013-014}

En $(0,\infty)$, $f(x)=0$ y $g(x)=x$ satisfacen $f<g$ y ambas tienen límite cero: para la identidad sirve $\delta=\varepsilon$. Para la afirmación general, si $f\to L$, $g\to M$ y $L>M$, pedimos errores menores que $(L-M)/3$, reunimos radios con la ventana de orden y obtenemos una entrada por acumulación. Allí $f>L-(L-M)/3>M+(L-M)/3>g$, contradicción. Luego $L\le M$.

## 13.15. Dos destinos no caben en una misma ventana

[]{#MA-EX-ANM-01-013-015}

[]{#MA-SOL-ANM-01-013-015}

Si $L\ne M$, $d=|L-M|>0$. Ambos contratos para $\varepsilon=d/2$ dan radios positivos. Acumulación proporciona una entrada en su mínimo. La triangular da $d\le|L-f(x)|+|f(x)-M|<d/2+d/2=d$, contradicción. La igualdad en la suma de tolerancias es admisible porque los errores individuales son estrictamente menores.

## 13.16. La frontera ya es infracción

[]{#MA-EX-ANM-01-013-016}

[]{#MA-SOL-ANM-01-013-016}

[]{#MA-SEC-ANM-01-013-004}

Tomemos $\varepsilon_0=1$. Dado $\delta>0$, sea $x=-\delta/2$. Entonces $0<|x|<\delta$ y $|x-1|=1+\delta/2>1$. El candidato se refuta aunque la función sí tiene otro límite, cero.

**Retorno visual.** Véase [C13-F04](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 13.17. Una escala basta para todos los radios

[]{#MA-EX-ANM-01-013-017}

[]{#MA-SOL-ANM-01-013-017}

La negación completa aplicada a $\delta=r_n$ produce un infractor para cada $n$ con la misma $\varepsilon_0$. A la inversa, dados conjuntos no vacíos y un radio cualquiera $\delta$, la propiedad de la escala da $n$ con $r_n<\delta$. Un único punto infractor de ese conjunto también está en la ventana de radio $\delta$ y conserva el error $\ge\varepsilon_0$. No hace falta escoger todos los puntos a la vez.

## 13.18. Todos los reales quedan descartados

[]{#MA-EX-ANM-01-013-018}

[]{#MA-SOL-ANM-01-013-018}

Fijemos cualquier $L$. Para tolerancia $1$ y cualquier $\delta>0$, elegimos $x=\min(\delta/2,1/[2(|L|+1)])>0$. Está en el dominio y en la ventana perforada; $1/|x|\ge2(|L|+1)$ implica $|f(x)-L|\ge f(x)-|L|>1$. Cada candidato tiene infractores arbitrariamente próximos, por lo que no existe límite real finito.

## 13.19. Cada entrada favorable no es un límite

[]{#MA-EX-ANM-01-013-019}

[]{#MA-SOL-ANM-01-013-019}

Sea $f(x)=0$ para $x>0$, $f(x)=1$ para $x\le0$. Dadas $\varepsilon,\delta>0$, el punto $\delta/2$ cumple la condición favorable. Pero el punto $-\delta/2$ tiene error $1$ para cada radio, por lo que la tolerancia $\varepsilon_0=1/2$ refuta $L=0$. La condición débil elige una entrada; el límite debe controlar todas.

## 13.20. Fallo sin magnitud infinita

[]{#MA-EX-ANM-01-013-020}

[]{#MA-SOL-ANM-01-013-020}

El salto con salidas $-1$ y $1$ está acotado por $1$. Para cada candidato $L$ una de las distancias a esas dos salidas es $\ge1$, por triangular. Fijado ese signo, el punto con ese signo y magnitud $\delta/2$ infringe el error para cualquier radio, con tolerancia $1$. La falta de límite puede deberse a incompatibilidad de destinos sin que los valores sean grandes.

## 13.21. Una ruta favorable engaña

[]{#MA-EX-ANM-01-013-021}

[]{#MA-SOL-ANM-01-013-021}

[]{#MA-SEC-ANM-01-013-005}

La ruta $u_n=1/(n+1)$ tiene imágenes cero. La ruta $v_n=-1/(n+1)$ tiene imágenes uno, pues nunca coincide con una entrada positiva de la primera ruta. Ambas evitan cero y convergen a él por C06. Si hubiese límite $L$, la dirección directa y la unicidad secuencial darían a la vez $L=0$ y $L=1$, contradicción.

## 13.22. Un prefijo puede tocar el centro

[]{#MA-EX-ANM-01-013-022}

[]{#MA-SOL-ANM-01-013-022}

Dado $\varepsilon>0$, el límite funcional ofrece $\delta$. La convergencia de $x_n$ da $N_1$ que asegura $|x_n-a|<\delta$. Para $n\ge\max(N_0,N_1)$ también hay distancia positiva, y la implicación funcional produce error menor que $\varepsilon$. Los términos anteriores no afectan la convergencia.

## 13.23. El mínimo vive en los índices

[]{#MA-EX-ANM-01-013-023}

[]{#MA-SOL-ANM-01-013-023}

Por sobreyectividad y no vaciedad de $E_n$, el conjunto $I_n=\{k:e(k)\in E_n\}$ contiene algún natural. El buen orden da un mínimo único. La regla $n\mapsto\min I_n$ es funcional y su composición con $e$ produce el selector real. Un conjunto real no vacío puede no tener mínimo, por ejemplo $(0,1)$; no se puede reemplazar el mínimo de índices por uno de valores.

**Retorno visual.** Véase [C13-F05](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 13.24. La ruta de infracciones prueba la recíproca

[]{#MA-EX-ANM-01-013-024}

[]{#MA-SOL-ANM-01-013-024}

Supongamos que todas las rutas admisibles tienen imágenes tendiendo a $L$ y que falla el contrato funcional. Hay $\varepsilon_0>0$ y conjuntos reales $E_n$ no vacíos de infractores con $0<|x-a|<1/(n+1)$. Aplicamos aquí, y sólo aquí, $\mathrm{CC}(\mathbb R)$ para obtener una función $n\mapsto x_n\in E_n$. Las cotas implican $x_n\to a$, pero $|f(x_n)-L|\ge\varepsilon_0$ para todos los índices impide convergencia de imágenes a $L$. La contradicción prueba el límite. No se presenta como prueba incondicional.

## 13.25. No hace falta una ruta distinta en cada paso

[]{#MA-EX-ANM-01-013-025}

[]{#MA-SOL-ANM-01-013-025}

La prueba de convergencia sólo necesita $|x_n-a|<1/(n+1)$; no usa inyectividad. Si un punto fijo $t\ne a$ apareciera en índices arbitrariamente grandes, su distancia $d=|t-a|>0$ tendría que ser menor que $1/(n+1)$ para índices con esa escala menor que $d$, imposible. Puede haber repeticiones finitas de valores, aunque no se hayan exigido términos diferentes.

## 13.26. Cancelar antes de usar un cociente

[]{#MA-EX-ANM-01-013-026}

[]{#MA-SOL-ANM-01-013-026}

[]{#MA-SEC-ANM-01-013-006}

El dominio es $\mathbb R\setminus\{2\}$. Allí la factorización da $(x^2-4)/(x-2)=x+2$, que tiene límite $4$: con $\delta=\varepsilon$ el error es $|x-2|<\varepsilon$. El límite del denominador es cero, por lo que el criterio de cocientes no se aplica. La cancelación es válida sólo fuera del punto excluido, exactamente el dominio pertinente.

## 13.27. Un denominador con ceros lejanos

[]{#MA-EX-ANM-01-013-027}

[]{#MA-SOL-ANM-01-013-027}

El dominio es $D_0=\mathbb R\setminus\{-2,2\}$. Polinomios dan límites $1$ y $-4$ en cero; el segundo es no nulo. La regla de cocientes prueba límite $-1/4$. Los ceros lejanos no impiden una ventana local: para $|x|<1$, $|g(x)|=4-x^2>3$. No se afirma que el cociente esté definido en los puntos excluidos.

## 13.28. Producto desde una identidad diferente

[]{#MA-EX-ANM-01-013-028}

[]{#MA-SOL-ANM-01-013-028}

Sea $A=1+|L|+|M|>0$. Dado $\varepsilon>0$, exigimos ambos errores menores que $t=\min(1,\varepsilon/A)$. En el mínimo de radios, $|(f-L)(g-M)|<t^2\le t$, y los otros términos están acotados por $|L|t$ y $|M|t$. Sumando con la estricta cota del primer término obtenemos error $<At\le\varepsilon$. Esta variante usa el pequeño tamaño del producto de errores en vez de una cota separada de $f$.

## 13.29. Norma y diferencia de normas

[]{#MA-EX-ANM-01-013-029}

[]{#MA-SOL-ANM-01-013-029}

La triangular inversa aplicada primero a los dos reales $|f|-|g|$ y $|L|-|M|$ da error final $\le\bigl|(|f|-|g|)-(|L|-|M|)\bigr|$. La triangular y la inversa de nuevo lo acotan por $||f|-|L||+||g|-|M||\le|f-L|+|g-M|$. Pedimos cada error menor que $\varepsilon/2$ y reunimos radios. La cota prueba la conclusión directamente.

## 13.30. Un producto converge sin límites de los factores

[]{#MA-EX-ANM-01-013-030}

[]{#MA-SOL-ANM-01-013-030}

Sea $f(x)=g(x)=s(x)$, el salto con valores $\pm1$. Las rutas positivas y negativas dan destinos distintos y refutan el límite de cada factor. Pero $f(x)g(x)=s(x)^2=1$ para toda entrada, así que el producto tiene límite $1$ con cualquier radio y error cero. La regla del producto es suficiente, no una condición necesaria para que el producto converja.

## 13.31. El único lado disponible

[]{#MA-EX-ANM-01-013-031}

[]{#MA-SOL-ANM-01-013-031}

[]{#MA-SEC-ANM-01-013-007}

El lado derecho acumula y el izquierdo está vacío, por lo que no le asignamos límite. Para $\varepsilon>0$, $\delta=\min(1,\sqrt\varepsilon)$ hace que toda entrada perforada sea positiva y tenga $|f(x)|=x^2<\varepsilon$. El límite en $D$ es cero y coincide con el límite derecho; el valor central $9$ se excluye.

**Retorno visual.** Véase [C13-F06](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 13.32. Reunir piezas finitas

[]{#MA-EX-ANM-01-013-032}

[]{#MA-SOL-ANM-01-013-032}

Para $\varepsilon>0$, tomamos radios $\delta_1,\delta_2$ válidos. Su mínimo es positivo. Toda entrada perforada de $D$ pertenece a una pieza y recibe el error menor que $\varepsilon$ de esa pieza, aunque pueda pertenecer a ambas. Luego hay límite en $D$. Si el límite vale en $D$, el mismo radio funciona en cada subconjunto; la acumulación supuesta permite formular ambos límites restringidos.

## 13.33. Infinitas piezas no garantizan reunión

[]{#MA-EX-ANM-01-013-033}

[]{#MA-SOL-ANM-01-013-033}

Cada $D_k$ acumula cero: para un radio $r>0$ existe un real positivo irracional menor que $r$, que no es un recíproco entero. Tal entrada puede obtenerse explícitamente como $\sqrt2/m$ con entero $m>\sqrt2/r$. Si $\delta=1/(2k)$, la ventana de $D_k$ excluye su único punto con valor uno, $1/k$, y el error es cero para toda tolerancia. La unión de las piezas es todo $D$: los no recíprocos están en todas y cada recíproco en su pieza. La ruta $x_n=1/(n+1)$ tiene imágenes uno; para cada radio hay tal entrada con error uno, así que el candidato cero falla en la unión. Además, la ruta $\sqrt2/(n+1)$ tiene imágenes cero y descarta cualquier límite junto a la primera.

## 13.34. Una prueba densa puede omitir todo el problema

[]{#MA-EX-ANM-01-013-034}

[]{#MA-SOL-ANM-01-013-034}

La restricción racional es constante cero y $\delta=1$ sirve para cualquier tolerancia; cero acumula racionales por los puntos $1/m$. En el dominio completo, $1/(n+1)$ y $\sqrt2/(n+1)$ son rutas no nulas tendiendo a cero. La segunda es irracional en cada índice, pues de lo contrario $\sqrt2$ sería racional. Las imágenes son constantes cero y uno. Un límite funcional daría el mismo límite a ambas rutas por la dirección directa, contradicción.

## 13.35. Al menos un lado acumula

[]{#MA-EX-ANM-01-013-035}

[]{#MA-SOL-ANM-01-013-035}

Si ninguno acumulara, habría radios positivos $r_-,r_+$ sin entradas de cada lado en sus ventanas. En el mínimo no habría ninguna entrada distinta de $a$ del dominio, contradicción. Si sólo el derecho acumula, el izquierdo tiene un radio sin entradas. Todo control del límite derecho se reúne con ese radio y controla el dominio completo; la implicación inversa es restricción. El caso izquierdo es simétrico.

## 13.36. La composición pierde el centro perforado

[]{#MA-EX-ANM-01-013-036}

[]{#MA-SOL-ANM-01-013-036}

[]{#MA-SEC-ANM-01-013-008}

Tomamos $f(x)=0$ para todos los reales; $g(y)=0$ si $y\ne0$ y $g(0)=2$. Los dos límites son cero porque sus errores son cero en las ventanas pertinentes. La composición es constante dos y tiene límite dos. El límite perforado de $g$ sólo controla entradas distintas de cero; la interior cae siempre en cero.

**Retorno visual.** Véase [C13-F07](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 13.37. Componer dos cuadrados con certificados

[]{#MA-EX-ANM-01-013-037}

[]{#MA-SOL-ANM-01-013-037}

Para $g(y)=y^2$ en $b=1$, el radio $\eta=\min(1,\varepsilon/3)$ es válido y $g(1)=1$. Para $f(x)=x^2$ en $1$, tomamos $\delta=\min(1,\eta/3)$. Entonces $|f(x)-1|<\eta$. Si $f(x)\ne1$ aplica el control de $g$; si $f(x)=1$, el error final es cero. El tipo real de ambas funciones permite componerlas. Así $|x^4-1|<\varepsilon$ en toda la ventana.

## 13.38. La alternativa central sin límites conocidos

[]{#MA-EX-ANM-01-013-038}

[]{#MA-SOL-ANM-01-013-038}

En esa misma ventana la composición tiene valor constante $g(b)$. Para cualquier $\varepsilon>0$ usamos su radio $r$ y el error es cero. Por tanto el límite es $g(b)$. No importa el comportamiento de $g$ fuera de la salida única localmente alcanzada; las hipótesis del teorema general de composición eran suficientes, no necesarias.

## 13.39. Composición a través de un subconjunto de salidas

[]{#MA-EX-ANM-01-013-039}

[]{#MA-SOL-ANM-01-013-039}

Fijado $\varepsilon>0$, el contrato de $g|_A$ ofrece $\eta>0$ para entradas de $A$ próximas y distintas de $b$. El límite de $f$ ofrece $\delta_f>0$ para ese radio. Reunimos $\delta_f$ con el radio $r$ de pertenencia y evitación. Para toda entrada de la nueva ventana, $f(x)\in A\setminus\{b\}$ y $|f(x)-b|<\eta$, de modo que $|g(f(x))-L|<\varepsilon$. El segundo contrato sólo se necesita en las salidas realmente disponibles.

## 13.40. Un criterio exacto para tocar una salida defectuosa

[]{#MA-EX-ANM-01-013-040}

[]{#MA-SOL-ANM-01-013-040}

La evitación es suficiente por el teorema del texto. Para probar necesidad, supongamos que la composición tiende a $L$ y sea $d=|g(b)-L|>0$. Su contrato para $\varepsilon=d/2$ da $\delta>0$ con error menor que $d/2$ en la ventana. Si alguna entrada allí tuviera $f(x)=b$, el error final sería $d$, contradicción. Luego todas evitan $b$. El defecto central convierte una condición suficiente en una condición necesaria para ese destino particular.

**Retorno visual.** Véase [C13-F07](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-microcontroles.html)
