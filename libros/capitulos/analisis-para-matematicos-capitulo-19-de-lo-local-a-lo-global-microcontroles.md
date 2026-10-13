---
content-id: MA-BCH-0281
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-019-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 19
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C19_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §19.1 — Un extremo interior obliga a detenerse

### Microcontrol 001

[]{#MA-MIC-ANM-01-019-001}

[]{#MA-MSOL-ANM-01-019-001}

[]{#MA-SEC-ANM-01-019-001}

**Pregunta.** ¿Qué es un mínimo local relativo?

**Solución.** Un centro $a\in D$ y un radio donde todas las entradas del dominio tienen valores al menos $f(a)$; no se exige desigualdad fuera de ese radio.

El radio fija una región de comparación y se recorta por el dominio real de la función. El valor central existe y sirve de cota inferior en esa región. No se exige que sea único ni que todos los valores del dominio sean mayores; esas condiciones corresponderían a conclusiones distintas.

### Microcontrol 002

[]{#MA-MIC-ANM-01-019-002}

[]{#MA-MSOL-ANM-01-019-002}

**Pregunta.** ¿Qué aporta interioridad a Fermat?

**Solución.** Entradas admisibles a ambos lados del centro dentro de cualquier radio suficientemente pequeño.

Una bola real contenida en el dominio permite construir entradas a izquierda y derecha dentro del radio del extremo y del radio de derivabilidad. Sus incrementos tienen signos opuestos. Esa disponibilidad geométrica es el paso que fuerza a la pendiente límite a ser simultáneamente no negativa y no positiva.

### Microcontrol 003

[]{#MA-MIC-ANM-01-019-003}

[]{#MA-MSOL-ANM-01-019-003}

**Pregunta.** ¿Qué signo tienen las secantes a la izquierda de un mínimo?

**Solución.** No positivo: el numerador es no negativo y el denominador negativo.

La condición de mínimo controla el numerador, mientras la posición de la entrada controla el denominador. Dividir un número no negativo por uno estrictamente negativo produce una secante no positiva. La conclusión incluye la posibilidad de numerador cero, importante en mínimos no estrictos.

### Microcontrol 004

[]{#MA-MIC-ANM-01-019-004}

[]{#MA-MSOL-ANM-01-019-004}

**Pregunta.** ¿Qué signo tienen las secantes a la derecha de un mínimo?

**Solución.** No negativo: tanto el numerador como el denominador son no negativos, y el segundo es positivo.

A la derecha el incremento es estrictamente positivo y la condición de mínimo hace no negativo el numerador. La secante es por ello no negativa. Junto al signo del lado izquierdo, este control obliga a la derivada a ser cero cuando ambas aproximaciones están disponibles.

### Microcontrol 005

[]{#MA-MIC-ANM-01-019-005}

[]{#MA-MSOL-ANM-01-019-005}

**Pregunta.** ¿Por qué una derivada positiva contradice un mínimo interior?

**Solución.** Fuerza cocientes positivos cerca del centro, incluidos argumentos de la izquierda donde el mínimo exige cocientes no positivos.

La tolerancia igual a media pendiente mantiene todas las secantes suficientemente próximas por encima de cero. Interioridad aporta una entrada izquierda dentro del mínimo de los radios necesarios. Su secante debería ser a la vez positiva y no positiva, contradicción. Una derivada negativa se descarta usando el lado derecho.

### Microcontrol 006

[]{#MA-MIC-ANM-01-019-006}

[]{#MA-MSOL-ANM-01-019-006}

**Pregunta.** ¿Qué ocurre con la identidad en los bordes de $[0,1]$?

**Solución.** Tiene extremos globales y derivadas relativas uno; los bordes no son interiores y no satisfacen la premisa geométrica de Fermat.

En los bordes la aproximación relativa sólo dispone de un lado. Sus secantes valen uno y no contradicen las comparaciones de extremo en ese único lado. Fermat necesita ambas clases de entradas para excluir los signos no nulos. El ejemplo conserva derivadas relativas válidas y muestra la función exacta de interioridad.

### Microcontrol 007

[]{#MA-MIC-ANM-01-019-007}

[]{#MA-MSOL-ANM-01-019-007}

**Pregunta.** ¿Pendiente cero basta para un extremo?

**Solución.** No: el cubo tiene derivada cero en cero y valores de ambos signos arbitrariamente cerca.

La derivada describe el término lineal del comportamiento local. El cubo tiene un término lineal nulo, pero conserva valores positivos y negativos a ambos lados. Por eso no es ni mínimo ni máximo local. Fermat es una condición necesaria para un extremo interior derivable, no una equivalencia.

### Microcontrol 008

[]{#MA-MIC-ANM-01-019-008}

[]{#MA-MSOL-ANM-01-019-008}

**Pregunta.** ¿Se usa valor medio para probar Fermat?

**Solución.** No. Se emplean directamente signos de cocientes, radios de derivabilidad y entradas de ambos lados.

Los radios de derivabilidad controlan secantes centradas en el extremo. La condición de extremo les impone signos, y el dominio permite encontrar entradas de ambos lados. Estos datos bastan para excluir pendientes positivas y negativas. No se utiliza todavía una relación global entre puntos diferentes.

## §19.2 — Rolle: volver a la misma altura

### Microcontrol 009

[]{#MA-MIC-ANM-01-019-009}

[]{#MA-MSOL-ANM-01-019-009}

[]{#MA-SEC-ANM-01-019-002}

**Pregunta.** ¿Dónde se exige continuidad en Rolle?

**Solución.** En todo $[a,b]$, incluidos sus extremos con continuidad relativa al segmento.

La continuidad relativa en los extremos permite aplicar Weierstrass al segmento completo. Una discontinuidad de borde podría impedir que el valor que domina las salidas se alcance. La derivabilidad interior garantiza continuidad allí, pero no sustituye esa comprobación en los bordes incluidos.

### Microcontrol 010

[]{#MA-MIC-ANM-01-019-010}

[]{#MA-MSOL-ANM-01-019-010}

**Pregunta.** ¿Dónde se exige derivabilidad en Rolle?

**Solución.** En todos los puntos de $(a,b)$; no se piden derivadas en los bordes.

Cada centro interior dispone de las dos direcciones necesarias para Fermat. En los bordes Rolle sólo necesita continuidad y la igualdad de valores, no una pendiente. Así el teorema puede utilizarse aunque no existan derivadas en esos dos puntos. Las regiones de sus dos premisas son diferentes y deben declararse.

### Microcontrol 011

[]{#MA-MIC-ANM-01-019-011}

[]{#MA-MSOL-ANM-01-019-011}

**Pregunta.** ¿Qué herramienta asegura extremos alcanzados?

**Solución.** El teorema de extremos sobre compactos de C16, aplicado al segmento cerrado no vacío y la función continua.

El segmento cerrado es compacto y, como $a<b$, no es vacío. La continuidad de la función permite que su imagen tenga máximo y mínimo alcanzados. Después se localiza alguno de sus argumentos dentro del interior. Sólo en esa localización se aplica Fermat; acotación de valores sola no bastaría.

### Microcontrol 012

[]{#MA-MIC-ANM-01-019-012}

[]{#MA-MSOL-ANM-01-019-012}

**Pregunta.** ¿Por qué una altura mayor que la de los bordes produce un extremo interior?

**Solución.** El máximo alcanzado tiene valor mayor que ambos valores de borde, así su punto no puede ser ninguno de ellos.

Los extremos tienen el mismo valor $k$. Si algún valor supera $k$, el máximo global es también mayor que $k$ y no puede producirse en esos bordes. Su argumento interior es un extremo local y tiene derivada cero por Fermat. Si hay un valor menor, se usa el mínimo con la misma lógica.

### Microcontrol 013

[]{#MA-MIC-ANM-01-019-013}

[]{#MA-MSOL-ANM-01-019-013}

**Pregunta.** ¿Qué punto sirve si la función es constante?

**Solución.** El punto medio, que es interior para $a<b$; sus cocientes son cero.

Para $a<b$ el punto $(a+b)/2$ pertenece a $(a,b)$. Todas las secantes de una constante tienen numerador cero y pendiente cero. Esto resuelve el caso que no ofrece ningún valor diferente del de los bordes. La prueba general distingue ese caso antes de localizar un extremo de altura distinta.

### Microcontrol 014

[]{#MA-MIC-ANM-01-019-014}

[]{#MA-MSOL-ANM-01-019-014}

**Pregunta.** ¿Rolle exige que ambos extremos globales sean interiores?

**Solución.** No. Basta uno interior en el caso no constante; el argumento distingue si hay valor superior o inferior al de los bordes.

Un único valor diferente de la altura de borde decide qué extremo global conviene utilizar. Si está por encima, sirve el máximo; si está por debajo, sirve el mínimo. El otro extremo puede permanecer en el borde sin afectar la prueba. Rolle sólo requiere encontrar al menos un centro interior de pendiente cero.

### Microcontrol 015

[]{#MA-MIC-ANM-01-019-015}

[]{#MA-MSOL-ANM-01-019-015}

**Pregunta.** ¿Un cero de la derivada entre dos ceros es necesariamente otro cero de la función?

**Solución.** No. Por ejemplo, $x(1-x)$ tiene ceros en cero y uno y derivada cero en un medio, donde su valor es un cuarto.

Rolle transforma igualdad de valores en una conclusión sobre la pendiente de algún punto interior. No exige que la altura de ese punto coincida con la de los bordes. En la parábola, resolver la ecuación de derivada da medio y evaluar allí da un cuarto. Son preguntas diferentes sobre el mismo testigo.

### Microcontrol 016

[]{#MA-MIC-ANM-01-019-016}

[]{#MA-MSOL-ANM-01-019-016}

**Pregunta.** ¿La conclusión de Rolle identifica un punto único?

**Solución.** No. Asegura al menos uno, y las constantes satisfacen la igualdad en todos los puntos interiores.

La existencia permite varios centros válidos y no prescribe cuál debe tomarse. Para una constante todos los puntos interiores satisfacen la conclusión. El teorema tampoco produce una elección simultánea para una familia infinita de funciones o segmentos. En cada aplicación basta un testigo para los datos fijados.

## §19.3 — Restar la secante para encontrar una tangente

### Microcontrol 017

[]{#MA-MIC-ANM-01-019-017}

[]{#MA-MSOL-ANM-01-019-017}

[]{#MA-SEC-ANM-01-019-003}

**Pregunta.** ¿Qué pendiente se resta en la prueba de Lagrange?

**Solución.** La pendiente secante $m=[f(b)-f(a)]/(b-a)$, fijada antes del argumento variable.

La condición $a<b$ asegura que el denominador es positivo y la secante está definida. Su pendiente es un número fijo en la construcción de la auxiliar. Restar la recta de esa pendiente hace coincidir las alturas de los bordes sin alterar continuidad ni derivabilidad interior. Esto permite aplicar Rolle.

### Microcontrol 018

[]{#MA-MIC-ANM-01-019-018}

[]{#MA-MSOL-ANM-01-019-018}

**Pregunta.** ¿Qué función tiene bordes cero?

**Solución.** $H(x)=f(x)-f(a)-m(x-a)$ en el mismo segmento.

En $a$ se anulan directamente las dos diferencias. En $b$, el término $m(b-a)$ coincide con el incremento de salida por definición de $m$. Así ambos valores son cero. La identidad no se supone a partir del gráfico: se calcula usando los bordes y un denominador válido.

### Microcontrol 019

[]{#MA-MIC-ANM-01-019-019}

[]{#MA-MSOL-ANM-01-019-019}

**Pregunta.** ¿Cuánto vale $H\prime$ en el interior?

**Solución.** $f\prime-m$, por la regla algebraica de C18.

La recta que se resta tiene pendiente constante $m$ y la función central $f(a)$ también es constante respecto del argumento. La regla de suma de C18 entrega la diferencia de derivadas en cada centro interior. No se supone continuidad de esas derivadas. La igualdad algebraica basta para traducir la conclusión de Rolle.

### Microcontrol 020

[]{#MA-MIC-ANM-01-019-020}

[]{#MA-MSOL-ANM-01-019-020}

**Pregunta.** ¿Qué convierte Rolle en la igualdad de valor medio?

**Solución.** $H\prime(c)=0$ implica $f\prime(c)=m$ para algún centro interior.

Rolle se aplica a la auxiliar de bordes iguales y da un punto, sin fijar su posición exacta. Anular su derivada equivale a igualar la pendiente original con la secante. Como ese punto es interior, su derivada estaba incluida en las hipótesis. El teorema establece existencia y no una fórmula universal para el centro.

### Microcontrol 021

[]{#MA-MIC-ANM-01-019-021}

[]{#MA-MSOL-ANM-01-019-021}

**Pregunta.** ¿Por qué no se admite $a=b$?

**Solución.** La secante dividiría por cero y el interior sería vacío.

Aunque una función esté definida en el singleton, no hay secante entre extremos distintos ni centro interior. La fórmula de pendiente requeriría un denominador no nulo y la conclusión un punto del interior. Ambas obligaciones fallan en el segmento degenerado. Por eso el enunciado conserva $a<b$.

### Microcontrol 022

[]{#MA-MIC-ANM-01-019-022}

[]{#MA-MSOL-ANM-01-019-022}

**Pregunta.** ¿Qué debe comprobarse antes de restringir al par $u<v$?

**Solución.** Que todo $[u,v]$ está en el dominio, con continuidad sobre él y derivabilidad en su interior.

Que los extremos sean entradas no obliga al dominio a incluir lo que hay entre ellos. La inclusión del segmento permite restringir y aplicar los teoremas de intervalos. Deben conservarse continuidad en los extremos y derivabilidad en todos los centros interiores. Una función en dos piezas separadas puede fallar precisamente esa inclusión.

### Microcontrol 023

[]{#MA-MIC-ANM-01-019-023}

[]{#MA-MSOL-ANM-01-019-023}

**Pregunta.** ¿El punto de valor medio del cubo en $[0,1]$ es un medio?

**Solución.** No. Es $1/\sqrt3$, porque $3c^2=1$ y $c>0$.

La secante del cubo entre cero y uno tiene pendiente uno. Su derivada interior es $3c^2$, así la igualdad exige $c^2=1/3$. Interioridad selecciona la raíz positiva y excluye la negativa. En medio la derivada vale tres cuartos, por lo que esa ubicación no satisface el teorema.

### Microcontrol 024

[]{#MA-MIC-ANM-01-019-024}

[]{#MA-MSOL-ANM-01-019-024}

**Pregunta.** ¿Hace falta continuidad de $f\prime$?

**Solución.** No. Las hipótesis requieren continuidad de $f$ y existencia de sus derivadas interiores.

La prueba utiliza continuidad de la función auxiliar para alcanzar un extremo y derivabilidad interior para aplicar Fermat. Ningún paso requiere que la función derivada sea continua. El ejemplo de bultos cumple todas esas premisas aunque su derivada sea discontinua. Diferenciar ambas funciones evita añadir una hipótesis innecesaria.

## §19.4 — El intervalo convierte signos en orden

### Microcontrol 025

[]{#MA-MIC-ANM-01-019-025}

[]{#MA-MSOL-ANM-01-019-025}

[]{#MA-SEC-ANM-01-019-004}

**Pregunta.** ¿Qué propiedad del dominio conecta dos entradas por Lagrange?

**Solución.** Ser un intervalo: todo el segmento entre las entradas pertenece al dominio.

Para un par ordenado del intervalo, el segmento que los une sigue dentro del dominio. Su interior dispone de derivadas y la restricción cumple continuidad de bordes. Lagrange relaciona entonces el incremento con una derivada interior. Los huecos de un dominio separado impedirían esa aplicación entre piezas distintas.

### Microcontrol 026

[]{#MA-MIC-ANM-01-019-026}

[]{#MA-MSOL-ANM-01-019-026}

**Pregunta.** ¿Qué conclusión da $f\prime\ge0$ en el interior?

**Solución.** Que $f$ es no decreciente, si también se verifican continuidad en el intervalo y derivabilidad interior.

Fijado $x<y$, el valor medio expresa la diferencia como $f\prime(c)(y-x)$. La derivada es no negativa y el incremento positivo, así la diferencia es no negativa. Como el par era arbitrario, se obtiene orden global en el intervalo. No se afirma crecimiento estricto si la derivada puede anularse.

### Microcontrol 027

[]{#MA-MIC-ANM-01-019-027}

[]{#MA-MSOL-ANM-01-019-027}

**Pregunta.** ¿Qué condición suficiente da crecimiento estricto?

**Solución.** $f\prime>0$ en todo el interior bajo las mismas hipótesis de intervalo y continuidad.

En cada par ordenado, el punto de valor medio tiene derivada estrictamente positiva. Multiplicarla por el incremento positivo produce una diferencia de salida estrictamente positiva. Esta condición es suficiente para todos los pares, pero no necesaria en todos los centros de una función estrictamente creciente.

### Microcontrol 028

[]{#MA-MIC-ANM-01-019-028}

[]{#MA-MSOL-ANM-01-019-028}

**Pregunta.** ¿Una función estrictamente creciente tiene siempre derivada positiva?

**Solución.** No: el cubo es estrictamente creciente y su derivada vale cero en el origen.

El cubo aumenta entre cualquier par ordenado porque su diferencia factoriza en un incremento positivo y otro factor estrictamente positivo. Sin embargo, su derivada en cero es cero. El ejemplo refuta la recíproca de la condición suficiente de crecimiento estricto. Donde una creciente tiene derivada, la condición necesaria sólo es no negatividad.

### Microcontrol 029

[]{#MA-MIC-ANM-01-019-029}

[]{#MA-MSOL-ANM-01-019-029}

**Pregunta.** ¿Qué da derivada idénticamente cero en un intervalo?

**Solución.** Constancia, por aplicar valor medio a cada par; se conserva continuidad en extremos incluidos.

Para dos entradas distintas, Lagrange multiplica el incremento por una derivada interior cero y fuerza igualdad de salidas. Los pares iguales no requieren el teorema. En extremos incluidos se conserva continuidad para aplicar la restricción correspondiente. En un dominio desconexo, las constantes pueden diferir entre piezas.

### Microcontrol 030

[]{#MA-MIC-ANM-01-019-030}

[]{#MA-MSOL-ANM-01-019-030}

**Pregunta.** ¿Qué da igualdad de dos derivadas en el interior?

**Solución.** La diferencia de las funciones es constante sobre el intervalo, bajo sus condiciones de continuidad.

La diferencia $f-g$ es continua y derivable donde corresponde, y su derivada interior vale cero. El resultado de constancia se aplica a esa función en el mismo intervalo. Si además ambas coinciden en una entrada, el valor de la constante se determina como cero. Igualar derivadas sin ese dato deja una diferencia constante posible.

### Microcontrol 031

[]{#MA-MIC-ANM-01-019-031}

[]{#MA-MSOL-ANM-01-019-031}

**Pregunta.** ¿Qué falla para constantes diferentes en dos piezas separadas?

**Solución.** No existe el segmento completo entre puntos de piezas distintas, así el valor medio no permite comparar sus constantes.

Cada pieza permite secantes de numerador cero y derivada relativa cero. Una entrada de una pieza y otra de la segunda no tienen entre ellas un segmento de dominio completo. Por eso no puede aplicarse valor medio a ese par. La constancia local por piezas no obliga a igualdad de sus alturas.

### Microcontrol 032

[]{#MA-MIC-ANM-01-019-032}

[]{#MA-MSOL-ANM-01-019-032}

**Pregunta.** ¿Se selecciona un punto $c$ para todos los pares a la vez?

**Solución.** No. Se fija un par arbitrario y se usa la existencia de un punto para esa instancia.

La demostración de orden o de cota empieza fijando un par arbitrario. El teorema proporciona un testigo para ese segmento y las hipótesis globales controlan su derivada. Después se concluye la desigualdad para el par. No se construye una función que elija testigos para todas las parejas simultáneamente.

## §19.5 — De cotas de derivadas a cotas de incrementos

### Microcontrol 033

[]{#MA-MIC-ANM-01-019-033}

[]{#MA-MSOL-ANM-01-019-033}

[]{#MA-SEC-ANM-01-019-005}

**Pregunta.** ¿Qué desigualdad producen $m\le f\prime\le M$?

**Solución.** Para $x<y$, $m(y-x)\le f(y)-f(x)\le M(y-x)$ bajo las hipótesis del intervalo.

El punto de valor medio pertenece al interior del segmento entre las entradas y cumple las dos cotas de derivada. Su pendiente multiplicada por el incremento reproduce la diferencia de salidas. Como el incremento es positivo, se conservan las desigualdades. La conclusión puede controlar todas las parejas sin conocer el testigo concreto.

### Microcontrol 034

[]{#MA-MIC-ANM-01-019-034}

[]{#MA-MSOL-ANM-01-019-034}

**Pregunta.** ¿Por qué no se invierte el orden al multiplicar?

**Solución.** El incremento de entrada $y-x$ es positivo.

Para entradas ordenadas distintas, la distancia dirigida $y-x$ es estrictamente positiva. Multiplicar por ella conserva el sentido de las dos cotas. Si se invierte el par hay que ordenar primero o pasar a magnitudes con simetría. Si las entradas coinciden, el incremento de salidas es cero y no se aplica Lagrange.

### Microcontrol 035

[]{#MA-MIC-ANM-01-019-035}

[]{#MA-MSOL-ANM-01-019-035}

**Pregunta.** ¿Qué controla una cota $|f\prime|\le L$?

**Solución.** Todos los pares: $|f(y)-f(x)|\le L|y-x|$, sin exigir continuidad de la derivada.

La cota simétrica de derivada controla el valor de cualquier testigo interior que produzca Lagrange. Tomar magnitudes en la identidad da la cota de incremento. Así se obtiene una constante Lipschitz global en el intervalo. No se utiliza un máximo de la derivada ni se requiere su continuidad.

### Microcontrol 036

[]{#MA-MIC-ANM-01-019-036}

[]{#MA-MSOL-ANM-01-019-036}

**Pregunta.** ¿Cómo se trata $L=0$?

**Solución.** La función es constante y cualquier radio prueba uniformidad; no se divide por cero.

La cota de pares se vuelve $|f(y)-f(x)|\le0$ y fuerza igualdad de todas las salidas. El error uniforme es entonces cero para cualquier tolerancia y cualquier radio positivo. Este caso debe separarse antes de usar la fórmula $\varepsilon/L$. La afirmación conserva las hipótesis de intervalo y continuidad.

### Microcontrol 037

[]{#MA-MIC-ANM-01-019-037}

[]{#MA-MSOL-ANM-01-019-037}

**Pregunta.** ¿Qué radio uniforme da $L>0$?

**Solución.** $\varepsilon/L$, a partir del control Lipschitz de todos los pares.

La barrera de derivadas se ha convertido primero en una cota de todos los pares mediante valor medio. A partir de ella, una distancia estrictamente menor que $\varepsilon/L$ produce error estrictamente menor que $\varepsilon$. El radio se fija antes de conocer los puntos. Esta es la conexión entre cotas de derivada y continuidad uniforme.

### Microcontrol 038

[]{#MA-MIC-ANM-01-019-038}

[]{#MA-MSOL-ANM-01-019-038}

**Pregunta.** ¿Qué cota funciona para el cubo en $[-A,A]$?

**Solución.** $L=3A^2$, pues su derivada es $3t^2$.

La magnitud del centro interior no supera $A$, por lo que $3t^2\le3A^2$. Esa barrera vale en todos los interiores y da el control de pares. Para $A>0$ se puede dividir el presupuesto por ella. Para $A=0$ el dominio es singleton y se verifica uniformidad directamente.

### Microcontrol 039

[]{#MA-MIC-ANM-01-019-039}

[]{#MA-MSOL-ANM-01-019-039}

**Pregunta.** ¿Lipschitz implica existencia de derivada en cada punto?

**Solución.** No. Sólo acota las derivadas donde existen; $|x|$ tiene cota Lipschitz uno y no es derivable en cero.

Una cota Lipschitz limita las magnitudes de las secantes y de sus límites si existen. No obliga a que esas secantes tengan un único destino. La esquina del valor absoluto mantiene magnitud uno pero tiene valores laterales opuestos. Así el control global de pares no asegura derivabilidad en cada centro.

### Microcontrol 040

[]{#MA-MIC-ANM-01-019-040}

[]{#MA-MSOL-ANM-01-019-040}

**Pregunta.** ¿Basta la derivada en un centro para acotar las derivadas vecinas?

**Solución.** No. La cota sobre otros centros es una hipótesis adicional, distinta del error normalizado de C18.

La derivada en un centro controla secantes que conservan ese centro fijo. Acotar una familia de derivadas de otros centros es una obligación universal adicional. El capítulo aplica valor medio cuando esa familia ya está controlada. No se deduce esa barrera vecina únicamente de un modelo de primer orden puntual.

## §19.6 — Comparar dos variaciones en el mismo punto

### Microcontrol 041

[]{#MA-MIC-ANM-01-019-041}

[]{#MA-MSOL-ANM-01-019-041}

[]{#MA-SEC-ANM-01-019-006}

**Pregunta.** ¿Qué forma de Cauchy permite incrementos nulos?

**Solución.** La igualdad de productos cruzados $\Delta f\,g\prime(c)=\Delta g\,f\prime(c)$.

Los productos cruzados están definidos incluso si una derivada o un incremento vale cero. La auxiliar de Rolle produce la igualdad antes de hacer cualquier división. Una forma de cocientes exige comprobar luego sus denominadores. Mantener la forma inicial permite tratar casos que esa segunda forma excluiría.

### Microcontrol 042

[]{#MA-MIC-ANM-01-019-042}

[]{#MA-MSOL-ANM-01-019-042}

**Pregunta.** ¿Qué coeficientes tiene la función auxiliar?

**Solución.** Los incrementos de borde de la otra función: $\Delta g$ multiplica $f-f(a)$ y $-\Delta f$ multiplica $g-g(a)$.

Los incrementos de borde son números fijos y no dependen del argumento de la auxiliar. Elegirlos cruzados hace que los valores de la auxiliar se anulen en ambos bordes. Las reglas algebraicas dan su derivada sin cambiar el dominio. Rolle relaciona después las dos derivadas en un mismo centro.

### Microcontrol 043

[]{#MA-MIC-ANM-01-019-043}

[]{#MA-MSOL-ANM-01-019-043}

**Pregunta.** ¿Por qué sus bordes coinciden?

**Solución.** Ambos son cero: en el primer borde se anulan las diferencias y en el segundo se cancelan los productos cruzados.

En $a$ los factores $f(x)-f(a)$ y $g(x)-g(a)$ son cero. En $b$ se obtiene $\Delta g\,\Delta f-\Delta f\,\Delta g=0$. La cancelación no divide por ningún incremento y conserva el caso de incrementos nulos. Esa identidad verifica la premisa de igualdad de bordes para Rolle.

### Microcontrol 044

[]{#MA-MIC-ANM-01-019-044}

[]{#MA-MSOL-ANM-01-019-044}

**Pregunta.** ¿Qué condición evita todos los denominadores nulos en la forma de cocientes?

**Solución.** $g\prime(t)\ne0$ en todo el interior; Rolle también fuerza $\Delta g\ne0$.

Si los valores de borde de $g$ fueran iguales, Rolle produciría una derivada nula interior, contradiciendo la premisa. Así el incremento de $g$ es no nulo. El testigo de Cauchy también tiene derivada de $g$ no nula porque la premisa vale en todo el interior. Sólo entonces se dividen los productos cruzados.

### Microcontrol 045

[]{#MA-MIC-ANM-01-019-045}

[]{#MA-MSOL-ANM-01-019-045}

**Pregunta.** ¿Por qué dos aplicaciones separadas de Lagrange no bastan?

**Solución.** Pueden producir puntos diferentes; Cauchy necesita relacionar ambas derivadas en un mismo centro.

Cada aplicación de Lagrange responde al incremento de una función y puede localizar una pendiente en un centro diferente. Dividir esas dos igualdades daría una razón de derivadas en centros distintos. La auxiliar de Cauchy combina ambas variaciones antes de aplicar Rolle. Así se obtiene un testigo compartido, que es la obligación nueva.

### Microcontrol 046

[]{#MA-MIC-ANM-01-019-046}

[]{#MA-MSOL-ANM-01-019-046}

**Pregunta.** ¿Qué punto sirve para $f=x^2$, $g=x^3$ en $[0,1]$?

**Solución.** $c=2/3$, porque sus incrementos son uno y $3c^2=2c$ con $c>0$.

Los dos incrementos son uno y la igualdad cruzada exige $3c^2=2c$. Factorizar da $c(3c-2)=0$ y la pertenencia a $(0,1)$ excluye cero. El valor restante es dos tercios. La ubicación no coincide con los puntos separados que proporcionarían las dos aplicaciones de Lagrange.

### Microcontrol 047

[]{#MA-MIC-ANM-01-019-047}

[]{#MA-MSOL-ANM-01-019-047}

**Pregunta.** ¿Qué ocurre si $g$ es constante?

**Solución.** El producto cruzado sigue siendo válido como $0=0$, pero la razón por $\Delta g$ y $g\prime$ no existe.

La derivada y el incremento de una constante son cero. La igualdad cruzada no se altera y no necesita información adicional sobre $f$. En cambio, ambas posibles razones tienen denominador cero. La forma cruzada es el enunciado general válido; la división es una consecuencia condicional.

### Microcontrol 048

[]{#MA-MIC-ANM-01-019-048}

[]{#MA-MSOL-ANM-01-019-048}

**Pregunta.** ¿Cómo se recupera Lagrange?

**Solución.** Tomando $g(x)=x$, con incremento $b-a>0$ y derivada uno.

La identidad tiene incremento positivo $b-a$ y derivada uno en todo centro interior. Sustituirla en la igualdad cruzada da $\Delta f=(b-a)f\prime(c)$. Dividir por la longitud no nula recupera la pendiente secante. Así Lagrange es un caso particular de la comparación de dos variaciones.

## §19.7 — Darboux: discontinuidad sin saltar valores

### Microcontrol 049

[]{#MA-MIC-ANM-01-019-049}

[]{#MA-MSOL-ANM-01-019-049}

[]{#MA-SEC-ANM-01-019-007}

**Pregunta.** ¿Darboux presupone continuidad de la derivada?

**Solución.** No. Prueba sus valores intermedios usando continuidad de la función auxiliar, extremos y Fermat.

La auxiliar $f-\lambda x$ es continua porque la función original es derivable. Los signos de sus derivadas de borde excluyen un mínimo allí y Weierstrass lo coloca dentro. Fermat anula su derivada y entrega el nivel solicitado. La continuidad utilizada corresponde a la auxiliar, no a la función derivada.

### Microcontrol 050

[]{#MA-MIC-ANM-01-019-050}

[]{#MA-MSOL-ANM-01-019-050}

**Pregunta.** ¿Qué resta se usa para buscar $f\prime(c)=\lambda$?

**Solución.** $H(x)=f(x)-\lambda x$, cuya derivada es $f\prime(x)-\lambda$.

Restar la recta de pendiente $\lambda$ convierte la ecuación buscada en derivada cero de la auxiliar. Sus pendientes de borde tienen signos opuestos cuando $\lambda$ es intermedio. Eso permite localizar un extremo interior y aplicar Fermat. El dominio intervalar conserva el segmento y los centros donde se desarrolla el argumento.

### Microcontrol 051

[]{#MA-MIC-ANM-01-019-051}

[]{#MA-MSOL-ANM-01-019-051}

**Pregunta.** ¿Por qué $H\prime(u)<0$ impide mínimo en el borde izquierdo?

**Solución.** Una entrada próxima a la derecha tiene cociente negativo y por tanto valor menor que $H(u)$.

El límite negativo de secantes permite un radio donde éstas siguen siendo negativas. Una entrada derecha dentro de ese radio y del segmento tiene incremento positivo y diferencia de valor negativa. Su altura es menor que la del borde izquierdo. Ese borde no puede ser minimizador global del segmento.

### Microcontrol 052

[]{#MA-MIC-ANM-01-019-052}

[]{#MA-MSOL-ANM-01-019-052}

**Pregunta.** ¿Por qué $H\prime(v)>0$ impide mínimo en el borde derecho?

**Solución.** Una entrada próxima a la izquierda tiene incremento negativo y cociente positivo, así su valor es menor que $H(v)$.

La secante izquierda es positiva y su incremento negativo. Multiplicar ambos da una diferencia de valor negativa respecto del borde derecho. Una entrada izquierda suficientemente cercana está dentro del segmento y alcanza una altura menor. Así tampoco ese borde puede minimizar, dejando un minimizador interior.

### Microcontrol 053

[]{#MA-MIC-ANM-01-019-053}

[]{#MA-MSOL-ANM-01-019-053}

**Pregunta.** ¿Qué ocurre si se invierte el orden de los dos valores de derivada?

**Solución.** Se aplica el mismo argumento a $-f$ y $-\lambda$, o se busca un máximo de la función auxiliar.

Cambiar $f$ por $-f$ invierte las dos alturas de derivada y cambia el nivel buscado a $-\lambda$. La regla de signo de C18 conserva derivabilidad. Aplicar el caso ya probado y volver a multiplicar por menos uno entrega el nivel original. No se necesita un nuevo supuesto de continuidad de la derivada.

### Microcontrol 054

[]{#MA-MIC-ANM-01-019-054}

[]{#MA-MSOL-ANM-01-019-054}

**Pregunta.** ¿Qué garantiza una derivada que nunca se anula en un intervalo abierto?

**Solución.** Su signo es constante; dos signos opuestos obligarían por Darboux a alcanzar cero entre ellos.

En un intervalo no vacío se fija una entrada y su derivada tiene un signo porque no es cero. Si otra entrada tuviera el signo opuesto, cero sería un nivel estrictamente intermedio. Darboux lo produciría entre ambas, contradicción. El argumento prueba signo común, pero no un margen uniforme positivo de magnitudes.

### Microcontrol 055

[]{#MA-MIC-ANM-01-019-055}

[]{#MA-MSOL-ANM-01-019-055}

**Pregunta.** ¿Valores intermedios implican continuidad?

**Solución.** No. La derivada discontinua de los bultos de C18 satisface Darboux aunque sus valores no converjan al central.

Darboux garantiza que entre dos valores se alcanzan los niveles intermedios. Continuidad exige además que salidas próximas al centro se aproximen a su valor central. La ruta de bultos mantiene derivadas menos tres medios frente al valor cero, aunque entre esos centros también aparezcan los demás niveles. Las dos propiedades pueden separarse.

### Microcontrol 056

[]{#MA-MIC-ANM-01-019-056}

[]{#MA-MSOL-ANM-01-019-056}

**Pregunta.** ¿Puede una derivada saltar directamente de menos uno a uno omitiendo cero?

**Solución.** No en un intervalo donde sea la derivada de una función derivable en todos sus puntos; Darboux fuerza ese valor intermedio.

Si ambos signos aparecen en dos centros del intervalo, el nivel cero debe alcanzarse en el segmento intermedio por Darboux. Omitirlo contradice que la función propuesta sea una derivada existente en todo el intervalo. Esto descarta un escalón directo, sin afirmar que todas las derivadas sean continuas.

## §19.8 — Certificar ceros y soluciones únicas

### Microcontrol 057

[]{#MA-MIC-ANM-01-019-057}

[]{#MA-MSOL-ANM-01-019-057}

[]{#MA-SEC-ANM-01-019-008}

**Pregunta.** ¿Qué da Rolle si dos entradas tienen el mismo valor?

**Solución.** Un punto interior de derivada cero, siempre que su segmento esté en el dominio y se verifiquen continuidad y derivabilidad.

El teorema se aplica a igualdad de dos valores cualesquiera, no sólo a ceros de la función. El segmento completo y sus condiciones de continuidad y derivabilidad son premisas necesarias. Si la derivada nunca se anula, esa igualdad resulta imposible para entradas distintas. Se obtiene inyectividad, pero aún no existencia de una solución para un nivel dado.

### Microcontrol 058

[]{#MA-MIC-ANM-01-019-058}

[]{#MA-MSOL-ANM-01-019-058}

**Pregunta.** ¿Qué cota de ceros de $f$ da a lo sumo $k$ ceros de $f\prime$?

**Solución.** A lo sumo $k+1$ ceros distintos de $f$, usando los segmentos entre una lista finita de ceros ordenados.

Si hubiera $k+2$ ceros distintos, se ordenaría esa lista finita. Los $k+1$ segmentos vecinos aportarían por Rolle otros tantos ceros de derivada en interiores separados. Eso infringiría la cota $k$. El argumento cuenta raíces distintas y no sus multiplicidades.

### Microcontrol 059

[]{#MA-MIC-ANM-01-019-059}

[]{#MA-MSOL-ANM-01-019-059}

**Pregunta.** ¿Por qué los ceros de derivada de los segmentos vecinos son distintos?

**Solución.** Cada uno está en un interior diferente, y esos interiores no se solapan.

Cada testigo queda estrictamente entre los extremos de su propio segmento. Los interiores de segmentos consecutivos no se intersectan, aunque compartan un extremo de borde. Por ello sus testigos no pueden coincidir. Esa localización permite convertir aplicaciones de Rolle en un recuento de ceros distintos.

### Microcontrol 060

[]{#MA-MIC-ANM-01-019-060}

[]{#MA-MSOL-ANM-01-019-060}

**Pregunta.** ¿Qué herramienta garantiza existencia del cero de $x^3+x-1$?

**Solución.** Continuidad y valor intermedio de C15, con signos opuestos en cero y uno; Rolle sólo prueba unicidad.

El valor intermedio convierte signos opuestos de una continua en existencia de raíz. La derivada positiva permite después descartar una segunda mediante Rolle o crecimiento. Son pasos lógicamente diferentes. Ausencia de derivadas nulas por sí sola no asegura que el nivel cero se alcance.

### Microcontrol 061

[]{#MA-MIC-ANM-01-019-061}

[]{#MA-MSOL-ANM-01-019-061}

**Pregunta.** ¿Qué cota inferior de derivada vale en $[0,1]$ para ese polinomio?

**Solución.** Uno, porque $p\prime(t)=3t^2+1\ge1$.

El cuadrado es no negativo en todo centro y por ello $3t^2+1$ es al menos uno. La barrera es global en el segmento, no una estimación basada en muestras. Valor medio la convierte en una cota inferior de incrementos. Esa cota permite traducir un residual conocido en distancia a la raíz.

### Microcontrol 062

[]{#MA-MIC-ANM-01-019-062}

[]{#MA-MSOL-ANM-01-019-062}

**Pregunta.** ¿Qué residuo tiene el aproximante $2/3$?

**Solución.** $p(2/3)=-1/27$; la raíz única queda a su derecha por crecimiento estricto.

Sustituir dos tercios produce $8/27+18/27-27/27=-1/27$. Como el polinomio es estrictamente creciente y en la raíz vale cero, la entrada de valor negativo queda a su izquierda. El signo del residual determina así el sentido del error. Su magnitud y una cota inferior de derivada controlarán después su tamaño.

### Microcontrol 063

[]{#MA-MIC-ANM-01-019-063}

[]{#MA-MSOL-ANM-01-019-063}

**Pregunta.** ¿Qué error da una cota $f\prime\ge m>0$ entre $x$ y un cero $r$?

**Solución.** $|x-r|\le|f(x)|/m$, obtenido de la cota de incrementos en ese segmento.

La raíz tiene valor cero, así la magnitud del incremento de salida entre ella y $x$ es $|f(x)|$. La barrera positiva da al menos $m|x-r|$ para ese incremento. Dividir por $m>0$ produce la cota posicional. Se necesitan las hipótesis en todo el segmento entre ambos, no sólo en el aproximante.

### Microcontrol 064

[]{#MA-MIC-ANM-01-019-064}

[]{#MA-MSOL-ANM-01-019-064}

**Pregunta.** ¿Qué falta cuando sólo se han muestreado unas pocas derivadas?

**Solución.** Una cota válida para todos los puntos interiores pertinentes; la tabla finita no certifica esa premisa universal.

Los valores muestreados no excluyen una pendiente menor, mayor o nula entre las muestras. El certificado de valor medio utiliza una cota válida para cualquier testigo interior posible. Esa obligación debe demostrarse mediante fórmulas o estimaciones sobre toda la región. La tabla finita por sí sola no justifica el paso de residual a distancia.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html)
