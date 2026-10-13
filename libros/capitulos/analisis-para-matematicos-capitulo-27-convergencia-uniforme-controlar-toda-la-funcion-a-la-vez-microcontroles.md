---
content-id: MA-BCH-0313
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-027-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 27
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C27_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §27.1 — Una cola que sirve para todas las entradas

### Microcontrol 001

[]{#MA-MIC-ANM-01-027-001}

[]{#MA-MSOL-ANM-01-027-001}

[]{#MA-SEC-ANM-01-027-001}

**Pregunta.** ¿Qué dato recibe primero el contrato uniforme?

**Solución.** El contrato recibe $\varepsilon>0$ y proporciona después un natural $N$. Ese corte debe garantizar $|f_n(x)-f(x)|<\varepsilon$ para todo $n\ge N$ y toda $x\in X$. La entrada se examina cuando el corte ya está fijado, de modo que una misma cola responde a todas las columnas.

### Microcontrol 002

[]{#MA-MIC-ANM-01-027-002}

[]{#MA-MSOL-ANM-01-027-002}

**Pregunta.** ¿Puede el corte uniforme depender de la entrada?

**Solución.** El corte puede depender de la tolerancia, pero debe funcionar para cualquier entrada del dominio común. Si la elección dependiera de $x$, sólo se tendría el contrato puntual de C26. El cambio de orden entre elegir el corte y recibir la entrada es lo que añade la uniformidad.

### Microcontrol 003

[]{#MA-MIC-ANM-01-027-003}

[]{#MA-MSOL-ANM-01-027-003}

**Pregunta.** ¿Qué anchura tiene la banda de tolerancia $\varepsilon$?

**Solución.** En cada entrada, la banda abierta va de $f(x)-\varepsilon$ a $f(x)+\varepsilon$, con anchura vertical $2\varepsilon$. El error permitido es estrictamente menor que $\varepsilon$, así las dos fronteras quedan excluidas. Desde el corte, todas las gráficas posteriores deben quedar dentro de esa banda en el dominio completo.

### Microcontrol 004

[]{#MA-MIC-ANM-01-027-004}

[]{#MA-MSOL-ANM-01-027-004}

**Pregunta.** ¿Implica uniformidad convergencia puntual?

**Solución.** Fijada una entrada $x$, el corte uniforme ya asegura el error pedido para ella en toda la cola. Por tanto cada columna converge al valor $f(x)$. La definición puntual admite ese mismo corte aunque no dependa de la entrada.

### Microcontrol 005

[]{#MA-MIC-ANM-01-027-005}

[]{#MA-MSOL-ANM-01-027-005}

**Pregunta.** ¿Qué entrada puede variar en una refutación uniforme?

**Solución.** Para refutar uniformidad se fija una tolerancia $\varepsilon_0>0$ y, ante cada corte $N$, se producen algún $n\ge N$ y alguna $x\in X$ con error al menos $\varepsilon_0$. La entrada puede cambiar con el corte. Esta libertad permite seguir picos móviles que cada columna fija termina perdiendo.

### Microcontrol 006

[]{#MA-MIC-ANM-01-027-006}

[]{#MA-MSOL-ANM-01-027-006}

**Pregunta.** ¿Qué error tiene $x+1/(n+1)$ respecto de $x$?

**Solución.** La diferencia $(x+1/(n+1))-x$ es la constante $1/(n+1)$, independiente de la entrada. Esa cota tiende a cero y prueba uniformidad sobre toda la recta. Las funciones mismas son no acotadas; el contrato limita sus discrepancias, que aquí sí son acotadas.

### Microcontrol 007

[]{#MA-MIC-ANM-01-027-007}

[]{#MA-MSOL-ANM-01-027-007}

**Pregunta.** ¿Qué testigo refuta uniformidad de $x/(n+1)$ en la recta?

**Solución.** En la etapa $n$, tomamos $x=n+1$ y obtenemos $|x/(n+1)|=1$. Con tolerancia $1/2$, ante cualquier corte sirve el infractor de esa misma etapa. La entrada móvil refuta uniformidad en la recta, mientras cada entrada fija mantiene su límite cero.

### Microcontrol 008

[]{#MA-MIC-ANM-01-027-008}

[]{#MA-MSOL-ANM-01-027-008}

**Pregunta.** ¿Qué ocurre en un dominio vacío?

**Solución.** En el dominio vacío sólo existe la función vacía. Para cualquier tolerancia se puede tomar $N=0$, porque no hay entradas que deban satisfacer una desigualdad. El contrato es vacuo y no exige producir un punto del dominio.

## §27.2 — La envolvente de error y sus fronteras

### Microcontrol 009

[]{#MA-MIC-ANM-01-027-009}

[]{#MA-MSOL-ANM-01-027-009}

[]{#MA-SEC-ANM-01-027-002}

**Pregunta.** ¿Qué se comprueba antes de formar una envolvente real?

**Solución.** Para $X\ne\varnothing$, la imagen $\{|f_n(x)-f(x)|:x\in X\}$ es no vacía. Antes de tomar su supremo real hay que demostrar una cota superior finita. Entonces completitud define $E_n$; si el error es no acotado, esa envolvente real no existe.

### Microcontrol 010

[]{#MA-MIC-ANM-01-027-010}

[]{#MA-MSOL-ANM-01-027-010}

**Pregunta.** ¿Se exige envolvente real para todas las filas iniciales?

**Solución.** La convergencia uniforme ignora cualquier prefijo finito. Basta que desde algún índice las imágenes de error estén acotadas y sus supremos tiendan a cero. Una primera fila no acotada, seguida por filas idénticas al límite, no impide uniformidad.

### Microcontrol 011

[]{#MA-MIC-ANM-01-027-011}

[]{#MA-MSOL-ANM-01-027-011}

**Pregunta.** ¿Qué margen convierte control puntual estricto en supremo estricto?

**Solución.** Si todos los errores son menores que $\varepsilon$, su supremo puede ser exactamente $\varepsilon$. Aplicar primero el contrato con $\varepsilon/2$ da $E_n\le\varepsilon/2<\varepsilon$. El margen convierte la cota no estricta del supremo en el error estricto requerido para su límite numérico.

### Microcontrol 012

[]{#MA-MIC-ANM-01-027-012}

[]{#MA-MSOL-ANM-01-027-012}

**Pregunta.** ¿Puede cada error ser menor que1 y su supremo ser1?

**Solución.** Para $e(x)=x$ en $(0,1)$, cada error es menor que uno. Sin embargo, cualquier $c<1$ queda superado por alguna entrada suficientemente próxima a uno, así el supremo es uno. Ese valor no se alcanza: la imagen no contiene su extremo superior.

### Microcontrol 013

[]{#MA-MIC-ANM-01-027-013}

[]{#MA-MSOL-ANM-01-027-013}

**Pregunta.** ¿Qué diferencia entre vacío y convención de error cero se conserva?

**Solución.** La imagen de errores sobre el dominio vacío es vacía y carece de supremo real. Se define aparte su envolvente como cero para la única función. Esa convención permite incluir el caso vacío sin atribuirle una propiedad de completitud que no posee.

### Microcontrol 014

[]{#MA-MIC-ANM-01-027-014}

[]{#MA-MSOL-ANM-01-027-014}

**Pregunta.** ¿Qué son los conjuntos $B_n(\eta)$?

**Solución.** Para $\eta>0$, ponemos $B_n(\eta)=\{x\in X:|f_n(x)-f(x)|\ge\eta\}$. Contiene las entradas que incumplen en la fila $n$ el error estricto menor que $\eta$. Puede incluir puntos distintos en etapas distintas.

### Microcontrol 015

[]{#MA-MIC-ANM-01-027-015}

[]{#MA-MSOL-ANM-01-027-015}

**Pregunta.** ¿Qué dice uniformidad sobre esos conjuntos?

**Solución.** La uniformidad equivale a que, para cada $\eta>0$, exista $N$ tal que $B_n(\eta)=\varnothing$ para todo $n\ge N$. El mismo corte hace desaparecer todas las entradas infractoras de todas las filas posteriores.

### Microcontrol 016

[]{#MA-MIC-ANM-01-027-016}

[]{#MA-MSOL-ANM-01-027-016}

**Pregunta.** ¿Qué dice puntualidad sobre una entrada fija y esos conjuntos?

**Solución.** La convergencia puntual exige que, fijadas $x$ y $\eta$, desde algún corte esa entrada no pertenezca a $B_n(\eta)$. El corte puede depender de $x$. Los conjuntos completos pueden seguir siendo no vacíos porque otros puntos ocupan el lugar de los que dejaron de infringir.

## §27.3 — Calcular la peor discrepancia

### Microcontrol 017

[]{#MA-MIC-ANM-01-027-017}

[]{#MA-MSOL-ANM-01-027-017}

[]{#MA-SEC-ANM-01-027-003}

**Pregunta.** ¿Cuál es la envolvente de las potencias en $[0,1]$ para $n\ge1$?

**Solución.** El límite de las potencias vale cero antes de uno y uno en el extremo. Para $n\ge1$, su error es $x^n<1$ si $x<1$ y cero en uno. Entradas próximas al extremo hacen el error arbitrariamente cercano a uno, así $E_n=1$ sin máximo. La envolvente no tiende a cero.

### Microcontrol 018

[]{#MA-MIC-ANM-01-027-018}

[]{#MA-MSOL-ANM-01-027-018}

**Pregunta.** ¿Qué controla las potencias en $[0,c]$ con $c<1$?

**Solución.** En $[0,c]$, con $0<c<1$, el límite es cero y para $n\ge1$ se cumple $x^n\le c^n$, con igualdad en $c$. Por tanto $E_n=c^n$. La prueba geométrica por Bernoulli da un corte independiente de la entrada y demuestra uniformidad en ese segmento.

### Microcontrol 019

[]{#MA-MIC-ANM-01-027-019}

[]{#MA-MSOL-ANM-01-027-019}

**Pregunta.** ¿Qué ocurre si $c=0$?

**Solución.** El dominio $[0,0]$ contiene sólo cero. La fila inicial declarada vale uno, pero desde $n=1$ todas las potencias allí son cero. Sus errores posteriores respecto del límite cero tienen envolvente cero y la convergencia es uniforme.

### Microcontrol 020

[]{#MA-MIC-ANM-01-027-020}

[]{#MA-MSOL-ANM-01-027-020}

**Pregunta.** ¿Dónde alcanza su error máximo la tienda $t_n$?

**Solución.** La tienda $t_n$ está entre cero y uno y en su centro $2/(n+3)$ alcanza uno. Su límite puntual es cero, así el máximo de error es uno en cada etapa. El centro móvil proporciona una infracción para cualquier cola candidata a ser uniforme.

### Microcontrol 021

[]{#MA-MIC-ANM-01-027-021}

[]{#MA-MSOL-ANM-01-027-021}

**Pregunta.** ¿Qué envolvente tiene la tienda normalizada?

**Solución.** Si $b_n=kt_n$ con $k=n+3$, sus alturas están entre cero y $k$ y alcanzan $k$ en $2/k$. Respecto del límite nulo, $E_n=k$. La envolvente crece aunque cada columna sea eventualmente cero.

### Microcontrol 022

[]{#MA-MIC-ANM-01-027-022}

[]{#MA-MSOL-ANM-01-027-022}

**Pregunta.** ¿Qué cuadrado produce la cota global de $h_n$?

**Solución.** Para $k=n+1$, el cuadrado $(\sqrt{k}|x|-1)^2\ge0$ produce $1+kx^2\ge2\sqrt{k}|x|$. Al dividir para $x\ne0$ se obtiene $|h_n(x)|\le1/(2\sqrt{k})$; en cero se verifica directamente. La desigualdad controla todas las entradas de la recta.

### Microcontrol 023

[]{#MA-MIC-ANM-01-027-023}

[]{#MA-MSOL-ANM-01-027-023}

**Pregunta.** ¿Dónde alcanza $h_n$ su máximo de magnitud?

**Solución.** En $x=\pm1/\sqrt{k}$, el denominador de $h_n$ vale dos y su magnitud es $1/(2\sqrt{k})$. Estos puntos alcanzan la cota global, así dan el máximo exacto. Con $k=n+1$, los máximos tienden a cero y certifican uniformidad.

### Microcontrol 024

[]{#MA-MIC-ANM-01-027-024}

[]{#MA-MSOL-ANM-01-027-024}

**Pregunta.** ¿Decide un dominio no acotado que la convergencia falle?

**Solución.** El tamaño del dominio no decide por sí solo la uniformidad. En toda la recta, $h_n(x)=x/[1+(n+1)x^2]$ tiene error máximo $1/(2\sqrt{n+1})\to0$. En cambio $x/(n+1)$ tiene errores no acotados en cada fila. Lo decisivo es el control global de discrepancias.

## §27.4 — Restringir el dominio y seguir rutas

### Microcontrol 025

[]{#MA-MIC-ANM-01-027-025}

[]{#MA-MSOL-ANM-01-027-025}

[]{#MA-SEC-ANM-01-027-004}

**Pregunta.** ¿Qué corte sirve después de restringir el dominio?

**Solución.** Si $Y\subseteq X$, el corte uniforme en $X$ ya controla todas las entradas de $Y$. Por tanto se conserva sin cambios al restringir. Cuando existen las envolventes reales y los dominios no son vacíos, la imagen de errores menor está contenida en la mayor, así $E_n(Y)\le E_n(X)$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-027-026}

[]{#MA-MSOL-ANM-01-027-026}

**Pregunta.** ¿Cómo se reúnen finitariamente los cortes de piezas?

**Solución.** Para una tolerancia dada, cada una de las finitísimas piezas proporciona un corte. Su máximo natural sirve en la unión, porque cada entrada pertenece a alguna pieza y todo índice posterior supera su corte. El argumento exige una candidata compatible en las intersecciones.

### Microcontrol 027

[]{#MA-MIC-ANM-01-027-027}

[]{#MA-MSOL-ANM-01-027-027}

**Pregunta.** ¿Hace falta que las piezas sean abiertas o cerradas?

**Solución.** La reunión finita sólo utiliza que cada entrada del dominio pertenece a alguna pieza. No depende de que las piezas sean abiertas, cerradas o de otra clase topológica. El control proviene del máximo finito de cortes ya válidos en ellas.

### Microcontrol 028

[]{#MA-MIC-ANM-01-027-028}

[]{#MA-MSOL-ANM-01-027-028}

**Pregunta.** ¿Qué puede fallar en una unión infinita?

**Solución.** En una unión infinita, los cortes válidos en cada pieza pueden crecer sin una barrera natural común. Las potencias convergen uniformemente en cada $[0,c]$ con $c<1$, pero no en la unión $[0,1)$. No puede sustituirse el máximo finito por un máximo infinito sin justificar su existencia.

### Microcontrol 029

[]{#MA-MIC-ANM-01-027-029}

[]{#MA-MSOL-ANM-01-027-029}

**Pregunta.** ¿Qué error controla uniformidad para cualquier ruta $x_n$?

**Solución.** Para cualquier ruta dada $x_n\in X$, el corte uniforme controla la entrada $x_n$ de cada fila posterior. Así $|f_n(x_n)-f(x_n)|\to0$. No hace falta que la ruta converja; la comparación usa el límite evaluado en la misma entrada móvil.

### Microcontrol 030

[]{#MA-MIC-ANM-01-027-030}

[]{#MA-MSOL-ANM-01-027-030}

**Pregunta.** ¿Qué dato adicional permite comparar con $f(x)$?

**Solución.** Si además $x_n\to x\in X$ y $f$ es continua en $x$, entonces $f(x_n)\to f(x)$. La triangular suma ese error de cambio de entrada con $|f_n(x_n)-f(x_n)|$. Se obtiene $f_n(x_n)\to f(x)$.

### Microcontrol 031

[]{#MA-MIC-ANM-01-027-031}

[]{#MA-MSOL-ANM-01-027-031}

**Pregunta.** ¿Qué cota de índices tiene una subsucesión estrictamente creciente?

**Solución.** Una sucesión estrictamente creciente de índices naturales cumple $n_0\ge0$ y $n_{j+1}\ge n_j+1$, así por inducción $n_j\ge j$. Si $j\ge N$, entonces $n_j\ge N$ y el corte uniforme original controla la fila de la subsucesión.

### Microcontrol 032

[]{#MA-MIC-ANM-01-027-032}

[]{#MA-MSOL-ANM-01-027-032}

**Pregunta.** ¿Basta una subsucesión uniforme para afirmar uniformidad de la familia?

**Solución.** Las filas constantes $(-1)^n$ sobre un dominio no vacío tienen subsucesión par idénticamente uno, que converge uniformemente. La familia completa conserva también filas menos uno en cualquier cola, así no converge ni puntualmente. Una subsucesión favorable no controla las etapas omitidas.

## §27.5 — Operar bajo un presupuesto común

### Microcontrol 033

[]{#MA-MIC-ANM-01-027-033}

[]{#MA-MSOL-ANM-01-027-033}

[]{#MA-SEC-ANM-01-027-005}

**Pregunta.** ¿Qué permite la suma de dos errores uniformes?

**Solución.** Para una combinación lineal, el error está acotado por la suma de los errores de cada familia multiplicados por los coeficientes absolutos. Se asigna una parte de la tolerancia a cada uno y se toma el máximo de sus dos cortes. Como ambos cortes preceden a las entradas, la conclusión es uniforme.

### Microcontrol 034

[]{#MA-MIC-ANM-01-027-034}

[]{#MA-MSOL-ANM-01-027-034}

**Pregunta.** ¿Qué desigualdad controla el valor absoluto?

**Solución.** La triangular inversa da $\big||f_n(x)|-|f(x)|\big|\le|f_n(x)-f(x)|$. El mismo corte que controla la familia original controla sus valores absolutos para todas las entradas. No requiere cotas de magnitud de las funciones.

### Microcontrol 035

[]{#MA-MIC-ANM-01-027-035}

[]{#MA-MSOL-ANM-01-027-035}

**Pregunta.** ¿Qué hipótesis suficiente se declara para una composición exterior?

**Solución.** Una condición suficiente es que la función exterior sea Lipschitz con una misma constante $L$ en un dominio que contenga todos los valores de filas y límite utilizados. Entonces el error compuesto no supera $L|f_n-f|$. Pedir el error original menor que $\varepsilon/(L+1)$ proporciona uniformidad, también si $L=0$.

### Microcontrol 036

[]{#MA-MIC-ANM-01-027-036}

[]{#MA-MSOL-ANM-01-027-036}

**Pregunta.** ¿Qué barrera obtiene la prueba del producto para $f_n$?

**Solución.** Si $|f|\le A$, el contrato uniforme con tolerancia uno proporciona una cola con $|f_n-f|<1$ en toda entrada. La triangular da allí $|f_n|\le A+1$. Esta barrera independiente de la entrada permite controlar el producto con otra familia.

### Microcontrol 037

[]{#MA-MIC-ANM-01-027-037}

[]{#MA-MSOL-ANM-01-027-037}

**Pregunta.** ¿Por qué el producto con $x$ puede perder uniformidad?

**Solución.** En la recta, la familia constante en etapa $f_n(x)=x$ tiene error cero y $g_n(x)=1/(n+1)$ converge uniformemente a cero. Su producto es $x/(n+1)$, cuyos errores crecen sin cota con la entrada. Falta una barrera de magnitud del factor $x$ que proteja todo el dominio.

### Microcontrol 038

[]{#MA-MIC-ANM-01-027-038}

[]{#MA-MSOL-ANM-01-027-038}

**Pregunta.** ¿Basta continuidad del cuadrado para conservar uniformidad en valores no acotados?

**Solución.** Para $f_n(x)=x+1/(n+1)$, el error original es uniforme, pero el de los cuadrados es $|2x/(n+1)+1/(n+1)^2|$, no acotado en la recta. En una franja de valores $[-M,M]$, el cuadrado sí tiene cota Lipschitz $2M$, que permitiría transportar la aproximación.

### Microcontrol 039

[]{#MA-MIC-ANM-01-027-039}

[]{#MA-MSOL-ANM-01-027-039}

**Pregunta.** ¿Qué margen uniforme evita ceros en denominadores?

**Solución.** Si $|g(x)|\ge m>0$ y el error uniforme es menor que $m/2$ en una cola, la triangular inversa da $|g_n(x)|>m/2$ para toda entrada de ella. Por tanto todos esos recíprocos están definidos y sus errores no superan $2|g_n-g|/m^2$. El margen debe ser común al dominio completo.

### Microcontrol 040

[]{#MA-MIC-ANM-01-027-040}

[]{#MA-MSOL-ANM-01-027-040}

**Pregunta.** ¿Qué debe revisarse para recíprocos desde el índice inicial?

**Solución.** El límite separado de cero garantiza recíprocos sobre el dominio común desde un corte uniforme, pero no elimina ceros de filas anteriores. Para definir una familia de recíprocos desde $n=0$ hay que comprobar esas filas o declarar sus reemplazos iniciales por funciones definidas. Un prefijo finito reparado no altera la convergencia.

## §27.6 — Una distancia entre funciones acotadas

### Microcontrol 041

[]{#MA-MIC-ANM-01-027-041}

[]{#MA-MSOL-ANM-01-027-041}

[]{#MA-SEC-ANM-01-027-006}

**Pregunta.** ¿Qué funciones pertenecen a $\mathcal B(X)$?

**Solución.** Una función $u:X\to\mathbb R$ pertenece a $\mathcal B(X)$ si existe un real $B\ge0$ con $|u(x)|\le B$ para toda entrada. La barrera limita la función completa. Sumas, diferencias y múltiplos de dos funciones de esta clase siguen acotados.

### Microcontrol 042

[]{#MA-MIC-ANM-01-027-042}

[]{#MA-MSOL-ANM-01-027-042}

**Pregunta.** ¿Qué principio asegura existencia de la norma cuando $X$ no es vacío?

**Solución.** Si $X$ es no vacío, la imagen $\{|u(x)|:x\in X\}$ es no vacía y acotada porque $u\in\mathcal B(X)$. Completitud de los reales proporciona su supremo $\|u\|_\infty$. No se requiere que ninguna entrada alcance esa altura máxima.

### Microcontrol 043

[]{#MA-MIC-ANM-01-027-043}

[]{#MA-MSOL-ANM-01-027-043}

**Pregunta.** ¿Qué valor de norma se declara en el dominio vacío?

**Solución.** Para la única función de dominio vacío se define $\|u\|_\infty=0$. Su imagen de magnitudes es vacía, así no se obtiene ese valor tomando un supremo real. La convención incluye el caso vacío en las identidades de norma y distancia.

### Microcontrol 044

[]{#MA-MIC-ANM-01-027-044}

[]{#MA-MSOL-ANM-01-027-044}

**Pregunta.** ¿Qué dice norma cero sobre la función?

**Solución.** Cada magnitud $|u(x)|$ está entre cero y la norma. Si ésta es cero, todos los valores de $u$ son cero y la función coincide con la función nula. Recíprocamente, la función nula tiene norma cero; la misma equivalencia vale en el dominio vacío por su convención.

### Microcontrol 045

[]{#MA-MIC-ANM-01-027-045}

[]{#MA-MSOL-ANM-01-027-045}

**Pregunta.** ¿Cómo se trata el escalar cero en homogeneidad?

**Solución.** Si $\alpha=0$, la función $\alpha u$ es nula y su norma es cero, igual a $|\alpha|\|u\|_\infty$. El caso se verifica directamente. Para $\alpha\ne0$ se puede dividir por $|\alpha|$ al demostrar la optimalidad de la cota escalada.

### Microcontrol 046

[]{#MA-MIC-ANM-01-027-046}

[]{#MA-MSOL-ANM-01-027-046}

**Pregunta.** ¿Qué identidad da la distancia triangular?

**Solución.** La identidad $u-w=(u-v)+(v-w)$ y la triangular de valores dan $|u(x)-w(x)|\le d_\infty(u,v)+d_\infty(v,w)$ en cada entrada. El miembro derecho acota toda la imagen de magnitudes de $u-w$. Tomar supremo prueba la triangular de la distancia.

### Microcontrol 047

[]{#MA-MIC-ANM-01-027-047}

[]{#MA-MSOL-ANM-01-027-047}

**Pregunta.** ¿Puede una gráfica estar en una banda abierta sin quedar en la bola estricta del mismo radio?

**Solución.** En $(0,1)$, la función $u(x)=x$ tiene $|u(x)|<1$ en toda entrada, así su gráfica está en la banda abierta alrededor de cero. Pero su norma es uno, de modo que no pertenece a la bola estricta $d_\infty(u,0)<1$. El supremo puede caer en la frontera que ninguna altura alcanza.

### Microcontrol 048

[]{#MA-MIC-ANM-01-027-048}

[]{#MA-MSOL-ANM-01-027-048}

**Pregunta.** ¿Qué permite una clase $f_0+\mathcal B(X)$?

**Solución.** En la clase $f_0+\mathcal B(X)$, dos funciones se escriben $f_0+u$ y $f_0+v$ con $u,v$ acotadas. Su diferencia es $u-v$, también acotada, así tiene norma real y define una distancia. La parte común $f_0$ puede ser no acotada y se cancela al medir discrepancias.

## §27.7 — Cauchy uniforme y completitud

### Microcontrol 049

[]{#MA-MIC-ANM-01-027-049}

[]{#MA-MSOL-ANM-01-027-049}

[]{#MA-SEC-ANM-01-027-007}

**Pregunta.** ¿Cuántos índices universales controla Cauchy uniforme?

**Solución.** El contrato uniforme de Cauchy pide, para cada $\varepsilon>0$, un corte $N$ con $|f_n(x)-f_m(x)|<\varepsilon$ para todo $m,n\ge N$ y todo $x\in X$. Una misma cola controla cualquier pareja tardía de filas en cualquier entrada.

### Microcontrol 050

[]{#MA-MIC-ANM-01-027-050}

[]{#MA-MSOL-ANM-01-027-050}

**Pregunta.** ¿Qué dirección del criterio no usa completitud?

**Solución.** Si existe un límite uniforme $f$, un corte para error $\varepsilon/3$ controla simultáneamente ambas filas respecto de él. La triangular da $|f_n-f_m|<2\varepsilon/3<\varepsilon$. Esta dirección utiliza el destino ya existente y no necesita construir límites por completitud.

### Microcontrol 051

[]{#MA-MIC-ANM-01-027-051}

[]{#MA-MSOL-ANM-01-027-051}

**Pregunta.** ¿Dónde interviene completitud en la vuelta?

**Solución.** Una familia uniformemente de Cauchy hace de Cauchy a cada columna numérica. La completitud de $\mathbb R$, en el criterio de C10, proporciona su límite real. La unicidad permite reunir esas salidas en una función y después comprobar el control uniforme hacia ella.

### Microcontrol 052

[]{#MA-MIC-ANM-01-027-052}

[]{#MA-MSOL-ANM-01-027-052}

**Pregunta.** ¿Qué se mantiene fijo al llevar $m$ al límite?

**Solución.** Elegido el corte común, se fijan una entrada $x$ y un índice $n\ge N$. Sólo varía $m$ en $|f_n(x)-f_m(x)|$ mientras su columna converge. El corte no dependía de $n$ ni de $x$, así la cota obtenida al pasar al límite vale para ambos universalmente.

### Microcontrol 053

[]{#MA-MIC-ANM-01-027-053}

[]{#MA-MSOL-ANM-01-027-053}

**Pregunta.** ¿Qué sentido tiene la desigualdad tras ese límite?

**Solución.** Si los errores entre filas son menores que $\varepsilon/3$, al llevar una columna al límite se conserva la cota no estricta $|f_n(x)-f(x)|\le\varepsilon/3$. Ese número sigue siendo menor que $\varepsilon$. El paso al límite conserva una cota superior; no invierte el sentido de la desigualdad.

### Microcontrol 054

[]{#MA-MIC-ANM-01-027-054}

[]{#MA-MSOL-ANM-01-027-054}

**Pregunta.** ¿Qué fila demuestra acotación del límite en $\mathcal B(X)$?

**Solución.** Con el contrato de Cauchy para tolerancia uno se fija una fila de referencia $f_N$. Pasar al límite en las demás da $|f-f_N|\le1$ en toda entrada. Si $f_N$ es acotada, entonces $|f(x)|\le\|f_N\|_\infty+1$ y el límite sigue en $\mathcal B(X)$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-027-055}

[]{#MA-MSOL-ANM-01-027-055}

**Pregunta.** ¿Qué significa completitud secuencial para esa distancia?

**Solución.** La completitud secuencial afirma que cualquier sucesión de Cauchy para $d_\infty$ converge en esa distancia a una función de la misma clase $\mathcal B(X)$. Se construye el destino por columnas y se prueba que es acotado usando una fila de referencia. El criterio de envolventes identifica después el contrato uniforme con convergencia en distancia.

### Microcontrol 056

[]{#MA-MIC-ANM-01-027-056}

[]{#MA-MSOL-ANM-01-027-056}

**Pregunta.** ¿Por qué no basta que las diferencias de vecinos tiendan a cero?

**Solución.** En las filas constantes de sumas armónicas, los incrementos vecinos son $1/(n+1)\to0$. Sin embargo $H_{2m}-H_m$ suma $m$ términos de tamaño al menos $1/(2m)$, así es al menos $1/2$. Pares lejanos de cualquier cola conservan esa separación y refutan Cauchy.

## §27.8 — Certificar una aproximación completa

### Microcontrol 057

[]{#MA-MIC-ANM-01-027-057}

[]{#MA-MSOL-ANM-01-027-057}

[]{#MA-SEC-ANM-01-027-008}

**Pregunta.** ¿Qué suma usa el presupuesto geométrico de incrementos?

**Solución.** Para comparar $f_n$ con $f_m$ se escribe $f_n-f_m=\sum_{j=m}^{n-1}(f_{j+1}-f_j)$ cuando $n>m$. Es una telescopía finita. La cota geométrica de cada incremento se suma en esa lista, sin presuponer la existencia de una serie de funciones.

### Microcontrol 058

[]{#MA-MIC-ANM-01-027-058}

[]{#MA-MSOL-ANM-01-027-058}

**Pregunta.** ¿Qué cota común se obtiene para dos etapas con $n>m$?

**Solución.** Si $|f_{j+1}-f_j|\le Cq^j$ con $C\ge0$ y $0<q<1$, la suma finita da $|f_n-f_m|\le Cq^m(1-q^{n-m})/(1-q)\le Cq^m/(1-q)$ para $n>m$. La cota vale para toda entrada y tiende a cero con el menor índice.

### Microcontrol 059

[]{#MA-MIC-ANM-01-027-059}

[]{#MA-MSOL-ANM-01-027-059}

**Pregunta.** ¿Qué error se certifica después de construir el límite?

**Solución.** El presupuesto geométrico prueba Cauchy uniforme y construye un límite $f$. Fijar $m,x$ y llevar $n$ al límite conserva $|f(x)-f_m(x)|\le Cq^m/(1-q)$. Por tanto la misma barrera certifica el error de la aproximación completa, también cuando el supremo no se alcance.

### Microcontrol 060

[]{#MA-MIC-ANM-01-027-060}

[]{#MA-MSOL-ANM-01-027-060}

**Pregunta.** ¿Qué ocurre si $C=0$?

**Solución.** Si $C=0$, la cota de incrementos obliga a $|f_{j+1}(x)-f_j(x)|=0$ para todo índice y entrada. Todas las filas coinciden con $f_0$ y la convergencia es inmediata. No hace falta dividir por $C$ para elegir un corte.

### Microcontrol 061

[]{#MA-MIC-ANM-01-027-061}

[]{#MA-MSOL-ANM-01-027-061}

**Pregunta.** ¿Cómo se evita ambigüedad si se permite $q=0$?

**Solución.** Para admitir $q=0$, se especifica una cota inicial $C$ para $f_1-f_0$ y cotas cero para todos los incrementos posteriores. Así $f_n=f_1$ desde $n=1$. Esta declaración evita utilizar una potencia inicial ambigua y prueba uniformidad por constancia de la cola.

### Microcontrol 062

[]{#MA-MIC-ANM-01-027-062}

[]{#MA-MSOL-ANM-01-027-062}

**Pregunta.** ¿Cuándo se concluye que el límite es acotado?

**Solución.** El presupuesto controla $|f-f_0|\le C/(1-q)$. Si la base está acotada, sumar sus dos barreras acota al límite. Con base arbitraria sólo se garantiza una diferencia acotada y pertenencia a $f_0+\mathcal B(X)$; el límite puede conservar la parte no acotada de la base.

### Microcontrol 063

[]{#MA-MIC-ANM-01-027-063}

[]{#MA-MSOL-ANM-01-027-063}

**Pregunta.** ¿Qué refuta $s_n=\mathbf1_{(0,1/(n+1))}$?

**Solución.** Los intervalos $(0,1/(n+1))$ se encogen y las columnas de $s_n$ decrecen a cero. Ese límite es continuo. Pero en $x_n=1/[2(n+1)]$ el error vale uno para toda etapa, así la convergencia no es uniforme. Las filas son discontinuas, dato que debe conservarse al comparar el ejemplo con resultados de monotonía.

### Microcontrol 064

[]{#MA-MIC-ANM-01-027-064}

[]{#MA-MSOL-ANM-01-027-064}

**Pregunta.** ¿Qué única puerta sigue a este capítulo?

**Solución.** C28 estudia las hipótesis que permiten conservar continuidad y pasar límites a través de integración y diferenciación. La convergencia uniforme y sus certificados quedan disponibles para esas pruebas. Cada intercambio deberá verificar también la existencia de las operaciones que compara.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)
