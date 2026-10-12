---
content-id: MA-BCH-0310
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-027
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
title: 'Capítulo 27 — Convergencia uniforme: controlar toda la función a la vez'
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C27.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)

El contrato de C26 permitió una cola para cada entrada. Ahora exigiremos una cola común y construiremos la envolvente y la distancia que la miden. C02/C03 justifican los supremos; C10 construye destinos de columnas de Cauchy; C14 se usa en rutas dadas. No se importan teoremas de intercambio de C28 ni series de funciones o teoría métrica posterior.

## 27.1. Una cola que sirve para todas las entradas

[]{#MA-SEC-ANM-01-027-001}

C26 mantuvo fija una entrada y construyó para ella una cola. Ahora recibimos una tolerancia y debemos entregar una sola cola que funcione en todas las entradas del dominio. Sea $X\subseteq\mathbb R$, y sean $f_n,f:X\to\mathbb R$ para $n\in\mathbb N=\{0,1,\ldots\}$. Decimos que $f_n$ converge **uniformemente** a $f$ en $X$ si
$$
\forall\varepsilon>0\ \exists N\in\mathbb N\
\forall n\ge N\ \forall x\in X:\quad |f_n(x)-f(x)|<\varepsilon.
$$
Escribimos $f_n\to f$ uniformemente en $X$. La elección de $N$ precede a la entrada que habrá que controlar. El dominio es parte del contrato; una misma fórmula puede cumplirlo en un dominio y fallarlo en otro.

### Ver una banda y formular lo que significa

Para una tolerancia fija, la banda abierta
$$
\{(x,y)\in X\times\mathbb R:f(x)-\varepsilon<y<f(x)+\varepsilon\}
$$
contiene las gráficas completas de todas las filas posteriores a $N$. La anchura vertical es $2\varepsilon$. No se afirma que la banda sea horizontal ni que el límite sea continuo: está definida alrededor de los valores de una función dada. El requisito es que ninguna entrada de ninguna fila de la cola salga de ella.

Por ejemplo, $f_n(x)=x+1/(n+1)$ converge uniformemente a $f(x)=x$ en toda $\mathbb R$. Dada $\varepsilon>0$, elegimos un natural $N>1/\varepsilon$. Para todo $n\ge N$ y todo $x$,
$$
|f_n(x)-f(x)|=\frac1{n+1}\le\frac1{N+1}<\varepsilon.
$$
El corte no depende de $x$. Aunque las funciones no están acotadas en la recta, su **diferencia** sí tiene una barrera común. No se debe confundir acotación de los valores con acotación del error.

### Comparar y negar los dos contratos

La convergencia uniforme implica la puntual: el corte que funciona en todas las entradas sirve en la entrada que fijemos. La unicidad del límite puntual de C26 da también unicidad uniforme. Si $X$ es vacío, el contrato es vacuo y todas las filas y el límite son la única función vacía; no es necesario formar un supremo de una imagen vacía.

La negación hacia una candidata fija es
$$
\exists\varepsilon_0>0\ \forall N\in\mathbb N\
\exists n\ge N\ \exists x\in X:
|f_n(x)-f(x)|\ge\varepsilon_0.
$$
Ahora la entrada infractora puede cambiar con el corte y el índice. Para $g_n(x)=x/(n+1)$ en $\mathbb R$, C26 probó límite puntual cero. Con $\varepsilon_0=1/2$, ante cualquier $N$ tomamos $n=N$ y $x=N+1$: el error es1. Por tanto la convergencia no es uniforme en la recta.

No hace falta elegir infinitamente muchos puntos de conjuntos arbitrarios para esta refutación: el testigo está dado por una fórmula para cada desafío. La negación lógica afirma existencia de infracciones; convertirlas en una sucesión simultáneamente escogida requeriría justificar una regla de selección si no disponemos de fórmulas. No usaremos esa conversión como herramienta oculta.

![En la ventana dibujada−1≤x≤1, f_n=x+1/(n+1) y límite f=x. La banda de tolerancia1/4 tiene fronteras abiertas: n=3 cae en la frontera y no sirve; n=4 y n=9 quedan dentro. La prueba controla toda la recta y todas las filas desdeN=4.](../../assets/books/anm/C27/C27-F01.svg){#fig-anm-c27-f01 fig-alt="En la ventana dibujada−1≤x≤1, f_n=x+1/(n+1) y límite f=x. La banda de tolerancia1/4 tiene fronteras abiertas: n=3 cae en la frontera y no sirve; n=4 y n=9 quedan dentro. La prueba controla toda la recta y todas las filas desdeN=4."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-001}

1. ¿Qué dato recibe primero el contrato uniforme?

[]{#MA-MIC-ANM-01-027-002}

2. ¿Puede el corte uniforme depender de la entrada?

[]{#MA-MIC-ANM-01-027-003}

3. ¿Qué anchura tiene la banda de tolerancia $\varepsilon$?

[]{#MA-MIC-ANM-01-027-004}

4. ¿Implica uniformidad convergencia puntual?

[]{#MA-MIC-ANM-01-027-005}

5. ¿Qué entrada puede variar en una refutación uniforme?

[]{#MA-MIC-ANM-01-027-006}

6. ¿Qué error tiene $x+1/(n+1)$ respecto de $x$?

[]{#MA-MIC-ANM-01-027-007}

7. ¿Qué testigo refuta uniformidad de $x/(n+1)$ en la recta?

[]{#MA-MIC-ANM-01-027-008}

8. ¿Qué ocurre en un dominio vacío?

## 27.2. La envolvente de error y sus fronteras

[]{#MA-SEC-ANM-01-027-002}

Para una fila $n$ y candidata $f$, definimos el conjunto de errores
$$
A_n=\{|f_n(x)-f(x)|:x\in X\}.
$$
Si $X$ es no vacío, este conjunto es no vacío y está formado por números no negativos. Antes de escribir un supremo real debemos comprobar que tiene una cota superior. Cuando la tiene, C03 permite definir
$$
E_n=\sup A_n.
$$
Esta **envolvente de error** es una barrera, aunque ninguna entrada la alcance.

### El criterio de las envolventes, con su dominio exacto

**Proposición.** Para $X\ne\varnothing$, la convergencia uniforme equivale a que desde algún índice todos los $A_n$ sean acotados y sus supremos reales $E_n$ tiendan a cero. Se permite que unas pocas filas iniciales tengan error no acotado.

Si hay convergencia uniforme, aplicamos primero el contrato con tolerancia1. En la cola correspondiente todos los errores son menores que1, así existe cada $E_n$. Para una precisión $\varepsilon>0$, usamos ahora la tolerancia $\varepsilon/2$ y reunimos ese corte con el primero. Entonces, en toda fila de la nueva cola,
$$
0\le E_n\le\varepsilon/2<\varepsilon.
$$
La primera desigualdad no requiere un máximo; la segunda se obtiene porque $\varepsilon/2$ es cota superior de **todos** los errores de la fila.

Recíprocamente, si los $E_n$ reales de una cola convergen a cero, un corte con $E_n<\varepsilon$ da, para toda entrada,
$$
|f_n(x)-f(x)|\le E_n<\varepsilon.
$$
Eso es el contrato uniforme. La prueba incluye todos los índices posteriores, no sólo una subsucesión de filas favorables.

Podemos adoptar para el vacío la convención $E_n=0$ y conservar la equivalencia. Es una convención para el error de la función vacía; no se dice que el conjunto vacío tenga supremo real cero en el orden usual.

### Estricto en cada entrada no es estricto en el supremo

En $X=(0,1)$, la función de error $e(x)=x$ cumple $e(x)<1$ en toda entrada y tiene supremo1. No lo alcanza. Para demostrar ese supremo,1 es cota superior y cualquier $c<1$ deja algún punto mayor que $c$ dentro del intervalo, por ejemplo $(1+\max(c,0))/2$. Por tanto no se puede inferir $E_n<\varepsilon$ sólo de errores individuales menores que $\varepsilon$. La tolerancia partida de la prueba anterior convierte una cota no estricta en la precisión estricta requerida.

Tampoco se puede exigir que todos los errores iniciales sean acotados. En $X=(0,1]$, definamos $f_0(x)=1/x$ y $f_n(x)=0$ para $n\ge1$, con candidata cero. La convergencia es uniforme: sirve $N=1$ para cualquier tolerancia. Pero la imagen de errores de la primera fila no tiene cota real. Suprimir el prefijo no altera una propiedad de cola.

### Regiones de infracción

Para $\eta>0$, sea
$$
B_n(\eta)=\{x\in X:|f_n(x)-f(x)|\ge\eta\}.
$$
La convergencia uniforme dice que para cada $\eta$ esos conjuntos son vacíos en toda una cola. La puntual dice que cada entrada deja de pertenecer a ellos eventualmente, con un corte que puede depender de ella. Todos los puntos pueden salir eventualmente sin que llegue una etapa en que el conjunto entero quede vacío. Las tiendas de C26 realizan exactamente esa posibilidad.

![En(0,1), e(x)=x es menor que1 en toda entrada pero tiene supremo1 no alcanzado. A la derecha, la familia f0=1/x y fn=0 desde n=1 converge uniformemente aunque la primera fila no tenga envolvente real. No se representa un supremo infinito como número.](../../assets/books/anm/C27/C27-F02.svg){#fig-anm-c27-f02 fig-alt="En(0,1), e(x)=x es menor que1 en toda entrada pero tiene supremo1 no alcanzado. A la derecha, la familia f0=1/x y fn=0 desde n=1 converge uniformemente aunque la primera fila no tenga envolvente real. No se representa un supremo infinito como número."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-009}

1. ¿Qué se comprueba antes de formar una envolvente real?

[]{#MA-MIC-ANM-01-027-010}

2. ¿Se exige envolvente real para todas las filas iniciales?

[]{#MA-MIC-ANM-01-027-011}

3. ¿Qué margen convierte control puntual estricto en supremo estricto?

[]{#MA-MIC-ANM-01-027-012}

4. ¿Puede cada error ser menor que1 y su supremo ser1?

[]{#MA-MIC-ANM-01-027-013}

5. ¿Qué diferencia entre vacío y convención de error cero se conserva?

[]{#MA-MIC-ANM-01-027-014}

6. ¿Qué son los conjuntos $B_n(\eta)$?

[]{#MA-MIC-ANM-01-027-015}

7. ¿Qué dice uniformidad sobre esos conjuntos?

[]{#MA-MIC-ANM-01-027-016}

8. ¿Qué dice puntualidad sobre una entrada fija y esos conjuntos?

## 27.3. Calcular la peor discrepancia

[]{#MA-SEC-ANM-01-027-003}

Calcular una envolvente puede acreditar el control global o detectar una obstrucción. En cada ejemplo distinguiremos la cota superior de la prueba de que es la mejor, y el supremo de su posible realización.

### Potencias: una barrera que no se alcanza

Con $p_0=1$, $p_n(x)=x^n$ para $n\ge1$ en $[0,1]$, C26 probó límite puntual $p=0$ antes de1 y $p(1)=1$. Para $n\ge1$, el error en1 es0 y en toda entrada menor que1 es $x^n<1$. No hay máximo de error, pero su supremo es1.

Para probar la última afirmación, sea $0\le c<1$ una supuesta cota menor. Elegimos $0<s<(1-c)/(n+1)$ y $x=1-s\in[0,1)$. Bernoulli de C26 da
$$
x^n\ge1-ns>c.
$$
Así $c$ no es cota. Las cotas negativas tampoco lo son porque hay error0. La envolvente vale1 en todas las filas, incluido el prefijo $p_0$, y no tiende a cero. En $[0,1)$ el límite es cero continuo, pero la misma envolvente1 impide convergencia uniforme.

En cambio, en $[0,c]$ con $0<c<1$, la candidata es cero y el máximo de error es $c^n$, alcanzado en $c$. Con $t=1/c-1>0$, Bernoulli da $c^n\le1/(1+nt)\to0$. Sobre $[0,0]$, el error es cero desde $n=1$. El dominio modifica la peor discrepancia.

### Tiendas: máximo móvil

Para $k=n+3$ y $t_n(x)=\max(0,1-|kx-2|)$ en $[0,1]$, C26 probó límite puntual cero. La cota $0\le t_n\le1$ se alcanza en $x=2/k$, de modo que $E_n=1$. Para las tiendas normalizadas $b_n=k\,t_n$, el máximo de error es $k$. Ambas familias fallan el contrato uniforme aunque sus columnas queden eventualmente en cero. Aquí la obstrucción es un máximo realizado, a diferencia de las potencias.

### Un máximo decreciente en toda la recta

Para $k=n+1$ y
$$
h_n(x)=\frac{x}{1+kx^2},\qquad x\in\mathbb R,
$$
el límite puntual es cero. El cuadrado $(\sqrt{k}|x|-1)^2\ge0$ demuestra $1+kx^2\ge2\sqrt{k}|x|$. En $x\ne0$, dividir por denominadores positivos da
$$
|h_n(x)|\le\frac1{2\sqrt{k}}.
$$
En cero se verifica directamente. La igualdad se alcanza en $x=\pm1/\sqrt{k}$, por lo que $E_n=1/(2\sqrt{k})$. Dada $\varepsilon>0$, un natural $N>1/(4\varepsilon^2)$ hace $E_n<\varepsilon$ para todo $n\ge N$. Tenemos convergencia uniforme en un dominio no acotado.

Una ventana de dibujo finita no decide el supremo sobre toda $\mathbb R$. El cuadrado positivo y los puntos de igualdad son el certificado global; la figura sólo los representa. En estos ejemplos el tamaño del dominio, por sí solo, no determina el modo de convergencia.

![Potencias en\[0,1\] y tiendas de altura1 conservan envolvente1; potencias en\[0,1/2\] tienen máximo2^(−n); h_n sobreR tiene máximo1/(2√(n+1)). Las líneas muestran envolventes certificadas por fórmulas, no supremos inferidos de un muestreo.](../../assets/books/anm/C27/C27-F03.svg){#fig-anm-c27-f03 fig-alt="Potencias en\[0,1\] y tiendas de altura1 conservan envolvente1; potencias en\[0,1/2\] tienen máximo2^(−n); h_n sobreR tiene máximo1/(2√(n+1)). Las líneas muestran envolventes certificadas por fórmulas, no supremos inferidos de un muestreo."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-017}

1. ¿Cuál es la envolvente de las potencias en $[0,1]$ para $n\ge1$?

[]{#MA-MIC-ANM-01-027-018}

2. ¿Qué controla las potencias en $[0,c]$ con $c<1$?

[]{#MA-MIC-ANM-01-027-019}

3. ¿Qué ocurre si $c=0$?

[]{#MA-MIC-ANM-01-027-020}

4. ¿Dónde alcanza su error máximo la tienda $t_n$?

[]{#MA-MIC-ANM-01-027-021}

5. ¿Qué envolvente tiene la tienda normalizada?

[]{#MA-MIC-ANM-01-027-022}

6. ¿Qué cuadrado produce la cota global de $h_n$?

[]{#MA-MIC-ANM-01-027-023}

7. ¿Dónde alcanza $h_n$ su máximo de magnitud?

[]{#MA-MIC-ANM-01-027-024}

8. ¿Decide un dominio no acotado que la convergencia falle?

## 27.4. Restringir el dominio y seguir rutas

[]{#MA-SEC-ANM-01-027-004}

La convergencia uniforme se refiere a un dominio concreto. Sus reglas de transporte deben conservar ese dato; olvidar el dominio puede convertir una estimación correcta en una conclusión falsa.

### Restringir y reunir finitamente

Si $f_n\to f$ uniformemente en $X$ y $Y\subseteq X$, el mismo corte funciona en $Y$. Cuando ambos conjuntos son no vacíos y las envolventes existen, la inclusión de imágenes de error da $E_n(Y)\le E_n(X)$ por C02. La igualdad no está garantizada.

Si $X=X_1\cup\cdots\cup X_m$ y hay convergencia uniforme de las restricciones hacia la misma candidata en cada pieza, para una tolerancia tomamos los $m$ cortes y su máximo. Toda entrada de $X$ pertenece a alguna pieza y queda controlada. Las piezas vacías no añaden obligaciones. No se exige que sean abiertas o cerradas: el argumento es finito y lógico.

Una unión infinita no admite automáticamente el mismo paso. En $X=[0,1)$, sea
$$
X_j=[0,c_j],\qquad c_j=1-\frac1{j+2},\quad j\in\mathbb N.
$$
Estas piezas cubren $X$: para $x<1$, la arquimedianidad permite $1/(j+2)\le1-x$. Las potencias convergen uniformemente a cero en cada $X_j$ por §27.3, pero no en su unión. Los cortes pueden crecer con la pieza y no tienen por qué tener una barrera común.

### Un contrato que controla cualquier ruta dada

Supongamos convergencia uniforme y que está dada cualquier sucesión $x_n\in X$. El mismo corte entrega
$$
|f_n(x_n)-f(x_n)|\longrightarrow0.
$$
No necesitamos que las entradas converjan. A diferencia de C26, ahora pueden variar porque todas estaban incluidas en la obligación después del corte.

Si además $x_n\to x\in X$ y $f$ es continua en $x$, la dirección secuencial directa de C14 da $f(x_n)\to f(x)$. La desigualdad
$$
|f_n(x_n)-f(x)|
\le |f_n(x_n)-f(x_n)|+|f(x_n)-f(x)|
$$
prueba convergencia de la diagonal a $f(x)$. Aquí continuidad del límite se declara como hipótesis; aún no la hemos deducido de continuidad de las filas. C28 estudiará esa preservación.

Para detectar fracaso uniforme basta una ruta explícita con errores que no desaparecen en índices arbitrariamente tardíos. Las tiendas tienen $x_n=2/(n+3)$ y error1. No afirmamos sin hipótesis de selección que todo fracaso pueda convertirse automáticamente en una diagonal previamente dada.

### Reindexar y conservar una cola

Cambiar unas pocas filas iniciales no altera convergencia uniforme: se reúne el corte anterior con el final del prefijo modificado. Para una subsucesión de índices estrictamente crecientes $n_j$, la inducción da $n_j\ge j$, así el corte uniforme en $n$ también funciona desde $j\ge N$. Toda subsucesión converge uniformemente al mismo límite.

La conversa no vale con una sola subsucesión. Filas constantes $f_n(x)=(-1)^n$ en un dominio no vacío tienen subsucesión par uniformemente igual a1, pero la familia completa no converge ni puntualmente. Capturar algunas filas no captura toda una cola.

![A la izquierda, envolventes de potencias en dos miembros de la familia X_j=\[0,1−1/(j+2)\] y en la unión de todos sus miembros\[0,1). Cada restricción cerrada tiene cota decreciente, pero la unión infinita mantiene error supremo1. A la derecha, una ruta sin límite x_n=(−1)^n sigue teniendo error1/(n+1) bajo la familia uniforme x+1/(n+1).](../../assets/books/anm/C27/C27-F04.svg){#fig-anm-c27-f04 fig-alt="A la izquierda, envolventes de potencias en dos miembros de la familia X_j=\[0,1−1/(j+2)\] y en la unión de todos sus miembros\[0,1). Cada restricción cerrada tiene cota decreciente, pero la unión infinita mantiene error supremo1. A la derecha, una ruta sin límite x_n=(−1)^n sigue teniendo error1/(n+1) bajo la familia uniforme x+1/(n+1)."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-025}

1. ¿Qué corte sirve después de restringir el dominio?

[]{#MA-MIC-ANM-01-027-026}

2. ¿Cómo se reúnen finitariamente los cortes de piezas?

[]{#MA-MIC-ANM-01-027-027}

3. ¿Hace falta que las piezas sean abiertas o cerradas?

[]{#MA-MIC-ANM-01-027-028}

4. ¿Qué puede fallar en una unión infinita?

[]{#MA-MIC-ANM-01-027-029}

5. ¿Qué error controla uniformidad para cualquier ruta $x_n$?

[]{#MA-MIC-ANM-01-027-030}

6. ¿Qué dato adicional permite comparar con $f(x)$?

[]{#MA-MIC-ANM-01-027-031}

7. ¿Qué cota de índices tiene una subsucesión estrictamente creciente?

[]{#MA-MIC-ANM-01-027-032}

8. ¿Basta una subsucesión uniforme para afirmar uniformidad de la familia?

## 27.5. Operar bajo un presupuesto común

[]{#MA-SEC-ANM-01-027-005}

Una estimación para todas las entradas permite reunir presupuestos de error sin volver a escoger el corte en cada punto. Pero los factores y denominadores necesitan barreras que también valgan en todo el dominio.

### Reglas lineales y operaciones de proximidad

Si $f_n\to f$ y $g_n\to g$ uniformemente en $X$, entonces $\alpha f_n+\beta g_n\to\alpha f+\beta g$ uniformemente. Las cotas
$$
|\alpha(f_n-f)+\beta(g_n-g)|
\le|\alpha||f_n-f|+|\beta||g_n-g|
$$
valen entrada por entrada; pedimos errores menores que $\varepsilon/[2(|\alpha|+1)]$ y $\varepsilon/[2(|\beta|+1)]$ y reunimos dos cortes independientes de la entrada.

La triangular inversa prueba uniformidad de $|f_n|\to|f|$. Para el máximo de dos valores usamos
$$
\max(u,v)=\frac{u+v+|u-v|}{2};
$$
las reglas anteriores dan $\max(f_n,g_n)\to\max(f,g)$ uniformemente.

Más generalmente, si $\phi:D\to\mathbb R$ cumple una cota Lipschitz común $|\phi(u)-\phi(v)|\le L|u-v|$ y todos los valores de $f_n,f$ están en $D$, entonces $\phi\circ f_n\to\phi\circ f$ uniformemente. La precisión $\varepsilon/(L+1)$ para las entradas de $\phi$ da el error requerido, incluido $L=0$. El dominio y la constante común van antes de la composición.

### Productos: declarar la barrera que se gasta

Supongamos además $|f(x)|\le A$ y $|g(x)|\le B$ en todo $X$. Un corte uniforme para $|f_n-f|<1$ da $|f_n(x)|\le A+1$ en todas las entradas de la cola. Allí
$$
|f_n(x)g_n(x)-f(x)g(x)|
\le (A+1)|g_n(x)-g(x)|+B|f_n(x)-f(x)|.
$$
Usando errores menores que $\varepsilon/[2(A+2)]$ y $\varepsilon/[2(B+1)]$, y el corte de la barrera, obtenemos convergencia uniforme del producto.

El supuesto de valores acotados no puede eliminarse sin otro control. En $\mathbb R$, $f_n(x)=x$ converge uniformemente a $x$ con error cero y $g_n(x)=1/(n+1)$ converge uniformemente a cero. El producto $x/(n+1)$ sólo converge puntualmente a cero, como §27.1 refutó. El error pequeño del segundo factor se multiplica por entradas sin barrera.

Tampoco continuidad de la operación exterior basta por sí sola en un dominio de valores no acotado. Las funciones $x+1/(n+1)$ convergen uniformemente a $x$, pero después de elevar al cuadrado el error es
$$
\left|\frac{2x}{n+1}+\frac1{(n+1)^2}\right|,
$$
no acotado en $\mathbb R$ para ninguna fila. En un rango $[-M,M]$ común, en cambio, $|u^2-v^2|\le2M|u-v|$ certifica esa composición.

### Recíprocos con margen común

Si $|g(x)|\ge m>0$ en todo $X$ y $g_n\to g$ uniformemente, un corte para error menor que $m/2$ da $|g_n(x)|>m/2$ simultáneamente. Los recíprocos están definidos en toda esa cola y
$$
\left|\frac1{g_n(x)}-\frac1{g(x)}\right|
\le\frac{2|g_n(x)-g(x)|}{m^2}.
$$
La estimación prueba uniformidad de la cola de recíprocos. Para una familia definida desde el índice cero se requiere que las filas iniciales no tengan ceros o que se declare una reparación; la prueba sólo garantiza el dominio de la cola. Con numeradores uniformemente convergentes a una función acotada, el producto anterior da el cociente.

![Familias x y1/(n+1) convergen uniformemente por separado enR, pero el producto x/(n+1) tiene error sin barrera global. Las gráficas sólo muestran una ventana; la ruta x_n=n+1 da error1 y acredita el fallo en cada etapa. La barrera de valores que exige la prueba del producto falta.](../../assets/books/anm/C27/C27-F05.svg){#fig-anm-c27-f05 fig-alt="Familias x y1/(n+1) convergen uniformemente por separado enR, pero el producto x/(n+1) tiene error sin barrera global. Las gráficas sólo muestran una ventana; la ruta x_n=n+1 da error1 y acredita el fallo en cada etapa. La barrera de valores que exige la prueba del producto falta."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-033}

1. ¿Qué permite la suma de dos errores uniformes?

[]{#MA-MIC-ANM-01-027-034}

2. ¿Qué desigualdad controla el valor absoluto?

[]{#MA-MIC-ANM-01-027-035}

3. ¿Qué hipótesis suficiente se declara para una composición exterior?

[]{#MA-MIC-ANM-01-027-036}

4. ¿Qué barrera obtiene la prueba del producto para $f_n$?

[]{#MA-MIC-ANM-01-027-037}

5. ¿Por qué el producto con $x$ puede perder uniformidad?

[]{#MA-MIC-ANM-01-027-038}

6. ¿Basta continuidad del cuadrado para conservar uniformidad en valores no acotados?

[]{#MA-MIC-ANM-01-027-039}

7. ¿Qué margen uniforme evita ceros en denominadores?

[]{#MA-MIC-ANM-01-027-040}

8. ¿Qué debe revisarse para recíprocos desde el índice inicial?

## 27.6. Una distancia entre funciones acotadas

[]{#MA-SEC-ANM-01-027-006}

Queremos que la envolvente no sea sólo una cuenta para cada ejemplo: puede medir la distancia entre dos funciones completas. Hay que elegir un conjunto donde esa distancia sea siempre un real.

### Construir el espacio y la norma

Sea
$$
\mathcal B(X)=\{u:X\to\mathbb R:\exists B\ge0\
\forall x\in X,\ |u(x)|\le B\}.
$$
Es un subconjunto de la colección de funciones de C26. Sumas y múltiplos permanecen en él por $|u+v|\le B_u+B_v$ y $|\alpha u|\le|\alpha|B_u$. La función cero pertenece a él.

Para $X\ne\varnothing$, la imagen de $|u|$ es no vacía y acotada; C03 da
$$
\|u\|_\infty=\sup_{x\in X}|u(x)|.
$$
Para $X=\varnothing$ definimos $\|u\|_\infty=0$. Verifiquemos las propiedades, sin suponer máximos inexistentes.

La norma es no negativa. Si vale cero, cada $|u(x)|\le0$, luego $u$ es cero; la conversa es inmediata. Para una constante $\alpha\ne0$, multiplicar todas las cotas por $|\alpha|$ y dividirlas de vuelta prueba
$$
\|\alpha u\|_\infty=|\alpha|\,\|u\|_\infty.
$$
Más explícitamente, $|\alpha|\|u\|_\infty$ es cota de los valores de $|\alpha u|$, y cualquier cota de éstos, dividida por $|\alpha|$, acota los de $|u|$. Para $\alpha=0$ la igualdad se comprueba aparte.

Finalmente,
$$
|u(x)+v(x)|\le\|u\|_\infty+\|v\|_\infty
$$
para todo $x$, de modo que el miembro derecho es cota superior y
$$
\|u+v\|_\infty\le\|u\|_\infty+\|v\|_\infty.
$$
Estas propiedades también valen para el vacío, donde sólo hay una función.

### La distancia suprema

Definimos
$$
d_\infty(u,v)=\|u-v\|_\infty.
$$
Es finita porque $u-v$ es acotada; es no negativa, simétrica y vale cero exactamente cuando $u=v$. Como $u-w=(u-v)+(v-w)$, la desigualdad de norma prueba
$$
d_\infty(u,w)\le d_\infty(u,v)+d_\infty(v,w).
$$
Estas son las propiedades de una distancia. La teoría general de espacios métricos llegará en C30; aquí la distancia ha sido construida y verificada en un caso concreto.

Converger para esta distancia significa $d_\infty(f_n,f)\to0$. Cuando todos los objetos pertenecen a $\mathcal B(X)$, §27.2 demuestra que equivale al contrato uniforme. La bola de radio $r>0$ está dada por $d_\infty(u,v)<r$: todas las diferencias de valores son menores que $r$. La conversa para un radio fijo puede fallar si todos los errores son menores que $r$ pero su supremo es $r$. Las bandas y las bolas dan el mismo modo de convergencia al permitir precisiones menores, no siempre el mismo conjunto para una frontera estricta fija.

### Funciones no acotadas y clases de diferencia acotada

No obtenemos una distancia real en la colección de **todas** las funciones poniendo el mismo símbolo. En $X=\mathbb R$, la diferencia entre $u(x)=x$ y cero no tiene cota superior de magnitud, así no tiene un supremo real. Tampoco el vacío se resuelve fingiendo un supremo que no existe.

Sin embargo, fijada una función cualquiera $f_0$, la clase
$$
f_0+\mathcal B(X)=\{f_0+u:u\in\mathcal B(X)\}
$$
sí tiene diferencias acotadas: entre dos miembros se cancela $f_0$. La misma fórmula define una distancia allí. Esto explica por qué $x+1/(n+1)$ puede converger uniformemente a $x$ aunque ninguna función pertenezca a $\mathcal B(\mathbb R)$. No se necesita asignar distancia finita a pares cuyo error no está acotado.

![Para u(x)=x en(0,1), toda gráfica cae en la banda abierta de radio1 alrededor de cero, pero d∞(u,0)=1 queda fuera de la bola estricta. A la derecha, las diferencias entre x+1/(n+1) y x son constantes: las bases no acotadas se cancelan y viven en una clase trasladada con distancia real.](../../assets/books/anm/C27/C27-F06.svg){#fig-anm-c27-f06 fig-alt="Para u(x)=x en(0,1), toda gráfica cae en la banda abierta de radio1 alrededor de cero, pero d∞(u,0)=1 queda fuera de la bola estricta. A la derecha, las diferencias entre x+1/(n+1) y x son constantes: las bases no acotadas se cancelan y viven en una clase trasladada con distancia real."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-041}

1. ¿Qué funciones pertenecen a $\mathcal B(X)$?

[]{#MA-MIC-ANM-01-027-042}

2. ¿Qué principio asegura existencia de la norma cuando $X$ no es vacío?

[]{#MA-MIC-ANM-01-027-043}

3. ¿Qué valor de norma se declara en el dominio vacío?

[]{#MA-MIC-ANM-01-027-044}

4. ¿Qué dice norma cero sobre la función?

[]{#MA-MIC-ANM-01-027-045}

5. ¿Cómo se trata el escalar cero en homogeneidad?

[]{#MA-MIC-ANM-01-027-046}

6. ¿Qué identidad da la distancia triangular?

[]{#MA-MIC-ANM-01-027-047}

7. ¿Puede una gráfica estar en una banda abierta sin quedar en la bola estricta del mismo radio?

[]{#MA-MIC-ANM-01-027-048}

8. ¿Qué permite una clase $f_0+\mathcal B(X)$?

## 27.7. Cauchy uniforme y completitud

[]{#MA-SEC-ANM-01-027-007}

C10 permitió converger sin conocer previamente el destino de una sucesión real. Podemos pedir ahora que el control de pares sirva al mismo tiempo en todas las entradas.

### El criterio uniforme de Cauchy

Una familia dada es **uniformemente de Cauchy** en $X$ si
$$
\forall\varepsilon>0\ \exists N\in\mathbb N\
\forall m,n\ge N\ \forall x\in X:\quad
|f_n(x)-f_m(x)|<\varepsilon.
$$
**Teorema.** Para funciones reales en un dominio común, este contrato equivale a la existencia de una función $f:X\to\mathbb R$ hacia la que la familia converge uniformemente.

En la ida, un corte de convergencia con tolerancia $\varepsilon/3$ controla dos errores. Para $m,n$ posteriores y cualquier $x$,
$$
|f_n(x)-f_m(x)|
\le |f_n(x)-f(x)|+|f(x)-f_m(x)|
<2\varepsilon/3<\varepsilon.
$$
Esta dirección no usa completitud.

En la vuelta, fijada cualquier entrada $x$, el contrato uniforme implica que su columna es de Cauchy en $\mathbb R$. C10, y por tanto completitud de los reales, entrega su límite. C26 construye la función $f$ mediante el grafo de esas salidas únicas, sin seleccionar arbitrariamente números límite.

Fijemos ahora $\varepsilon>0$ y recibamos un único corte $N$ del contrato de Cauchy con tolerancia $\varepsilon/3$. Para cualquier $n\ge N$ y cualquier $x$, todos los índices $m\ge N$ cumplen
$$
|f_n(x)-f_m(x)|<\varepsilon/3.
$$
Mantenemos **fijos** $n$ y $x$ y hacemos tender $m$ a infinito. El álgebra numérica, continuidad del absoluto y preservación del orden de C26 dan
$$
|f_n(x)-f(x)|\le\varepsilon/3<\varepsilon.
$$
La desigualdad después del límite es no estricta y tiene ese sentido, no el inverso. Como el corte se eligió antes de $n$ y $x$, el resultado vale para toda la cola y todo el dominio. Hemos probado uniformidad, no sólo puntualidad.

En el vacío la función única resuelve el teorema vacuamente. Ninguna parte de la vuelta requiere continuidad de las filas, un dominio compacto o una fórmula explícita del límite.

### Completitud de las funciones acotadas

Para una sucesión en $\mathcal B(X)$, el criterio de Cauchy para $d_\infty$ equivale al contrato anterior. Una distancia menor que $\varepsilon$ controla cada entrada. En sentido inverso, usar el contrato con $\varepsilon/2$ da supremo como máximo $\varepsilon/2<\varepsilon$. Otra vez se cuida la frontera del supremo.

Sea una sucesión de Cauchy en esa distancia. El teorema produce un límite uniforme real $f$. Falta probar que permanece en $\mathcal B(X)$. El contrato de Cauchy con tolerancia1 da un corte $N$. Para cualquier $x$, los valores posteriores satisfacen $|f_m(x)-f_N(x)|<1$; al pasar al límite,
$$
|f(x)|\le |f_N(x)|+1\le\|f_N\|_\infty+1.
$$
Así $f$ es acotada. §27.2 da $d_\infty(f_n,f)\to0$. Hemos demostrado **completitud secuencial**: toda sucesión de Cauchy para esta distancia tiene límite dentro del espacio. La existencia del destino procede de la completitud de $\mathbb R$ en cada columna, y el control común lo conserva dentro del conjunto de funciones acotadas.

### Dos precauciones antes de reutilizar

Cauchy puntual no basta: las tiendas de C26 tienen columnas convergentes, pero no son uniformemente de Cauchy, pues de serlo el teorema las haría uniformemente convergentes al único límite puntual cero, contra §27.3.

Controlar sólo vecinos tampoco basta. Para filas constantes $q_n(x)=H_n$, donde $H_0=0$ y $H_n=\sum_{j=1}^n1/j$, las diferencias de vecinos son $1/(n+1)\to0$ en todas las entradas. Pero entre etapas $m$ y $2m$,
$$
H_{2m}-H_m=\sum_{j=m+1}^{2m}\frac1j\ge\frac12.
$$
Para un dominio no vacío, ante cualquier corte elegimos un entero $m\ge\max(N,1)$ y obtenemos dos filas tardías separadas. El contrato exige todos los pares, no sólo los consecutivos.

![Filas constantes dyádicas f_n=1−2^(−n) admiten un presupuesto común para todos los pares y convergen a1. Las filas H_n tienen diferencias vecinas1/(n+1)→0, pero H_(2m)−H_m≥1/2 para todo m≥1. Las muestras de índices ilustran una cota demostrada para todos los pares tardíos necesarios.](../../assets/books/anm/C27/C27-F07.svg){#fig-anm-c27-f07 fig-alt="Filas constantes dyádicas f_n=1−2^(−n) admiten un presupuesto común para todos los pares y convergen a1. Las filas H_n tienen diferencias vecinas1/(n+1)→0, pero H_(2m)−H_m≥1/2 para todo m≥1. Las muestras de índices ilustran una cota demostrada para todos los pares tardíos necesarios."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-049}

1. ¿Cuántos índices universales controla Cauchy uniforme?

[]{#MA-MIC-ANM-01-027-050}

2. ¿Qué dirección del criterio no usa completitud?

[]{#MA-MIC-ANM-01-027-051}

3. ¿Dónde interviene completitud en la vuelta?

[]{#MA-MIC-ANM-01-027-052}

4. ¿Qué se mantiene fijo al llevar $m$ al límite?

[]{#MA-MIC-ANM-01-027-053}

5. ¿Qué sentido tiene la desigualdad tras ese límite?

[]{#MA-MIC-ANM-01-027-054}

6. ¿Qué fila demuestra acotación del límite en $\mathcal B(X)$?

[]{#MA-MIC-ANM-01-027-055}

7. ¿Qué significa completitud secuencial para esa distancia?

[]{#MA-MIC-ANM-01-027-056}

8. ¿Por qué no basta que las diferencias de vecinos tiendan a cero?

## 27.8. Certificar una aproximación completa

[]{#MA-SEC-ANM-01-027-008}

Ya tenemos un modo de convergencia, una envolvente real cuando el error está acotado, una distancia en un espacio adecuado y un criterio que construye destinos. Terminemos con certificados que permiten usarlos sin adivinar una fórmula límite.

### Sumar sólo un presupuesto finito de incrementos

Supongamos que hay constantes $C\ge0$ y $0<q<1$ con
$$
|f_{j+1}(x)-f_j(x)|\le Cq^j
\quad\text{para todo }j\in\mathbb N,\ x\in X.
$$
Si $n>m$, telescopar incrementos y aplicar la triangular da
$$
|f_n(x)-f_m(x)|
\le C\sum_{j=m}^{n-1}q^j
=Cq^m\frac{1-q^{n-m}}{1-q}
\le\frac{Cq^m}{1-q}.
$$
La identidad geométrica es finita y se verifica multiplicando la suma por $1-q$; no se usa teoría de series de funciones. Para $m>n$ intercambiamos los índices y para $m=n$ la diferencia es cero. Como $q^m\to0$ por C06, un corte independiente de la entrada hace esta barrera menor que cualquier tolerancia. La familia es uniformemente de Cauchy y §27.7 produce un límite uniforme $f$.

Manteniendo fijo $m$ y pasando $n$ al límite en la cota, obtenemos el certificado posterior
$$
|f(x)-f_m(x)|\le\frac{Cq^m}{1-q}
\quad\text{para toda }x.
$$
Si $C=0$ todas las filas coinciden. Si se desea permitir $q=0$, se define la cota de incremento inicial como $C$ y las posteriores como cero; desde la etapa1 la familia es constante. No se deja un $0^0$ ambiguo dentro de un presupuesto.

Si la fila inicial está acotada, telescopar desde ella da $|f_n(x)|\le\|f_0\|_\infty+C/(1-q)$ y el límite pertenece a $\mathcal B(X)$. Si no lo está, las diferencias $f_n-f_0$ sí están acotadas por la misma constante: la familia y el límite viven en la clase $f_0+\mathcal B(X)$. La acotación del destino se concluye sólo en el caso que la acredita.

Como ejemplo, con cualquier $a$ acotada por1 y cualquier función base $r$, la familia
$$
f_n(x)=r(x)+(1-2^{-n})a(x)
$$
tiene incremento $2^{-(n+1)}a(x)$, por lo que sirve $C=1/2$ y $q=1/2$. El certificado de error es $2^{-n}$ y el límite explícito es $r+a$. La construcción funciona aunque $r$ no sea acotada.

### Hipótesis que parecen suficientes y no lo son

Columnas monótonas y límite continuo no garantizan uniformidad sin otros datos. En $[0,1]$, sea
$$
s_n(x)=\mathbf1_{(0,\,1/(n+1))}(x).
$$
La columna de cero siempre vale0. Cada entrada positiva queda fuera del intervalo eventualmente, y los intervalos se encogen: $s_{n+1}(x)\le s_n(x)$ para toda entrada. El límite puntual es cero, continuo. Sin embargo, en $x_n=1/[2(n+1)]$ todas las filas valen1 y sus envolventes son1. La convergencia no es uniforme. Las filas son discontinuas; no se puede importar un teorema sobre continuidad y monotonía omitiendo esa hipótesis.

Tampoco ser uniformemente convergente significa tener valores conjuntamente acotados si las filas son no acotadas, como mostró la traslación de $x$. Si las filas sí pertenecen a $\mathcal B(X)$, uniformidad da límite acotado y una barrera común de toda la familia: la cola se controla por una fila de referencia y el límite, y los supremos de las filas iniciales finitas se reúnen por un máximo. Cada premisa desempeña un papel.

### Volver a mirar el contrato

Para acreditar uniformidad, una cota de error válida para toda entrada y toda una cola basta; no tiene que ser el supremo exacto. Para refutarla basta una tolerancia y testigos tardíos dentro del dominio. Para usar una distancia, se declara primero la clase en que las diferencias son acotadas. Para construir un límite desde Cauchy, se rastrea la completitud de las columnas y se mantiene el corte común al pasar al límite.

El próximo capítulo preguntará qué operaciones pueden atravesar este nuevo contrato: continuidad, integración y diferenciación. C27 ha preparado la herramienta y ya sabe que el control global de valores, por sí solo, no resuelve todos los intercambios. Las hipótesis que los autorizan serán demostradas en C28, sin utilizarlas antes de tiempo aquí.

![Con C=q=1/2, las cotas de incrementos son2^(−j−1) y el presupuesto posterior2^(−m). En la familia f_n=r+(1−2^(−n))a, |a|≤1, ese presupuesto controla todo el error hacia r+a, aunque r sea no acotada. El destino se acredita por Cauchy uniforme antes de usar la estimación posterior.](../../assets/books/anm/C27/C27-F08.svg){#fig-anm-c27-f08 fig-alt="Con C=q=1/2, las cotas de incrementos son2^(−j−1) y el presupuesto posterior2^(−m). En la familia f_n=r+(1−2^(−n))a, |a|≤1, ese presupuesto controla todo el error hacia r+a, aunque r sea no acotada. El destino se acredita por Cauchy uniforme antes de usar la estimación posterior."}

### Microcontroles

[]{#MA-MIC-ANM-01-027-057}

1. ¿Qué suma usa el presupuesto geométrico de incrementos?

[]{#MA-MIC-ANM-01-027-058}

2. ¿Qué cota común se obtiene para dos etapas con $n>m$?

[]{#MA-MIC-ANM-01-027-059}

3. ¿Qué error se certifica después de construir el límite?

[]{#MA-MIC-ANM-01-027-060}

4. ¿Qué ocurre si $C=0$?

[]{#MA-MIC-ANM-01-027-061}

5. ¿Cómo se evita ambigüedad si se permite $q=0$?

[]{#MA-MIC-ANM-01-027-062}

6. ¿Cuándo se concluye que el límite es acotado?

[]{#MA-MIC-ANM-01-027-063}

7. ¿Qué refuta $s_n=\mathbf1_{(0,1/(n+1))}$?

[]{#MA-MIC-ANM-01-027-064}

8. ¿Qué única puerta sigue a este capítulo?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)

[← Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Capítulo 28 →](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html)
