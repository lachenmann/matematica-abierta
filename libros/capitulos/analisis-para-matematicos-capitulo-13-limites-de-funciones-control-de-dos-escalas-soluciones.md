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
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C13_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html)

## 13.1. El agujero no decide el destino

[]{#MA-EX-ANM-01-013-001}

[]{#MA-SOL-ANM-01-013-001}

[]{#MA-SEC-ANM-01-013-001}

El candidato es $3$. Para $\varepsilon>0$ tomamos $\delta=\varepsilon/2$. Si $0<|x+1|<\delta$, entonces $x\ne-1$, por lo que $|f(x)-3|=2|x+1|<\varepsilon$. El punto $-1$ acumula entradas reales, por ejemplo $-1+\delta/2$. La definición controla entradas distintas del centro; el valor $100$ no interviene.

**Retorno visual.** Véase [C13-F01](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La condición positiva $0<|x+1|$ garantiza que se aplica la rama afín y no la evaluación excepcional. Restar el candidato tres da $2x+2=2(x+1)$, por lo que el error se controla exactamente mediante la distancia de entrada. El radio elegido es positivo para toda tolerancia positiva y funciona para todas las entradas de la ventana. El valor cien queda excluido por la definición, no porque sea pequeño o despreciable.

## 13.2. Una pregunta sin entradas

[]{#MA-EX-ANM-01-013-002}

[]{#MA-SOL-ANM-01-013-002}

Con $\delta=1$, no existe $x\in D$ con $0<|x|<1$. La implicación sería verdadera para todo $L$ y toda tolerancia usando ese mismo radio. Pero $0$ no es punto de acumulación de $D$, así que no asignamos límite. El fallo no depende de los valores de $f$: depende de las rutas inexistentes.

El centro cero pertenece al dominio, pero sus demás entradas están al menos a distancia dos. Por eso una ventana suficientemente pequeña no contiene entradas perforadas. La fórmula de precisión no discrimina ningún candidato y sería satisfecha incluso por números incompatibles entre sí. La hipótesis de acumulación evita esta ambigüedad: pertenecer al dominio no basta para preguntar por un límite perforado bajo la convención adoptada.

## 13.3. Dos lenguajes del mismo control

[]{#MA-EX-ANM-01-013-003}

[]{#MA-SOL-ANM-01-013-003}

Si vale la inclusión de imágenes y $x\in U_D(a,\delta)$, entonces $f(x)\in f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$, luego $x\in f^{-1}[B(L,\varepsilon)]$. A la inversa, si toda entrada de la ventana está en esa preimagen y $y$ pertenece a la imagen, existe un testigo $x$ de la ventana con $y=f(x)$; la pertenencia a la preimagen da $y\in B(L,\varepsilon)$. $f(x)$ es un valor; la imagen y la preimagen son conjuntos.

La primera inclusión controla salidas y la segunda selecciona entradas. Para pasar de una a otra se usa la misma evaluación $f(x)$, sin invertir la función. En la vuelta, una salida de la imagen viene acompañada de una entrada testigo de la ventana. La prueba conserva el recorte por $D$ y la exclusión del centro. Así ambas formulaciones expresan el mismo control universal, aunque sus conjuntos vivan en espacios distintos.

## 13.4. Igualdad en un germen perforado

[]{#MA-EX-ANM-01-013-004}

[]{#MA-SOL-ANM-01-013-004}

Fijemos un candidato $L$ y supongamos $f\to L$. Para cada $\varepsilon>0$, un radio $\delta_f$ de $f$ se reúne con $r$ mediante $\delta=\min(r,\delta_f)>0$. En la ventana resultante $g(x)=f(x)$ y $|g(x)-L|<\varepsilon$. Luego $g\to L$. Intercambiar $f,g$ prueba la recíproca para ese mismo candidato. Como $L$ era arbitrario, los conjuntos de candidatos coinciden.

El candidato se mantiene fijo durante cada dirección de la prueba. El radio mínimo asegura que las funciones coincidan donde se aplica la estimación del límite, y por eso el error puede trasladarse sin cambiarlo. Después invertimos los papeles. No importa que las funciones difieran en el centro o en entradas lejanas: el límite se decide en alguna ventana perforada donde ambas tienen los mismos datos de salida.

## 13.5. Cambiar valores en infinitos puntos lejanos

[]{#MA-EX-ANM-01-013-005}

[]{#MA-SOL-ANM-01-013-005}

Sea $f(x)=0$ para todo real, y sea $g(x)=0$ si $|x|<1$, $g(x)=x^2$ si $|x|\ge1$. Difieren en todos los enteros positivos, un conjunto infinito. $g(n)=n^2$ no admite cota global por arquimedianidad. Ambas coinciden en la ventana de radio $1$; para toda tolerancia, ese radio hace el error cero. La información fuera de una ventana fija no determina el límite.

Cada entero positivo produce salida cero en $f$ y salida $n^2$ en $g$, de modo que existen infinitas discrepancias. Para refutar cualquier barrera global propuesta a $g$, basta escoger un entero cuyo cuadrado la supere. Cerca de cero, en cambio, ambas funciones valen exactamente cero. El mismo radio uno responde a todas las tolerancias. La cantidad de discrepancias no decide el límite; importa su ubicación respecto de las ventanas locales.

## 13.6. Diseñar el radio de una afín decreciente

[]{#MA-EX-ANM-01-013-006}

[]{#MA-SOL-ANM-01-013-006}

[]{#MA-SEC-ANM-01-013-002}

El error es $4|x-2|$. $\delta=\varepsilon/4$ sirve porque la entrada satisface una desigualdad estricta. Si $\delta>\varepsilon/4$, tomamos $t=(\delta+\varepsilon/4)/2$ y $x=2+t$. Entonces $0<t<\delta$ y $4t>\varepsilon$, infracción. Por tanto el radio dado es el mayor. El signo de la pendiente invierte orden, pero el error depende de su magnitud.

**Retorno visual.** Véase [C13-F02](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Como la magnitud de la pendiente es cuatro, el error de salida es exactamente cuatro veces el de entrada. El radio $\varepsilon/4$ sirve incluso en el caso frontera, porque las entradas están a distancia estrictamente menor que el radio. Para cualquier radio mayor, la distancia $t$ elegida entre ambos umbrales produce un infractor dentro de la ventana. Estos dos argumentos demuestran validez y maximalidad, que son obligaciones diferentes.

## 13.7. Un radio conservador para un cuadrado

[]{#MA-EX-ANM-01-013-007}

[]{#MA-SOL-ANM-01-013-007}

Para $|x-2|<1$, $|x+2|\le|x-2|+4<5$. Dado $\varepsilon>0$, tomamos $\delta=\min(1,\varepsilon/5)$. Entonces $|x^2-4|=|x-2||x+2|<5|x-2|<5\delta\le\varepsilon$. El radio auxiliar elimina el factor variable.

La factorización introduce un factor variable $x+2$. Antes de ajustar la precisión, imponemos una ventana de radio uno para acotar su magnitud por cinco. Luego la condición $|x-2|<\varepsilon/5$ hace pequeño el producto. El mínimo conserva ambas condiciones a la vez. No se afirma que sea el mayor radio, ni se necesita resolver la desigualdad exacta para demostrar existencia del límite.

## 13.8. Radio óptimo del cuadrado en uno

[]{#MA-EX-ANM-01-013-008}

[]{#MA-SOL-ANM-01-013-008}

La componente de entradas positivas que satisface el error es $(\sqrt{1-\varepsilon},\sqrt{1+\varepsilon})$. Los márgenes desde $1$ son $1-\sqrt{1-\varepsilon}$ y $\sqrt{1+\varepsilon}-1$. El segundo es menor: racionalizar da $\varepsilon/(1+\sqrt{1-\varepsilon})>\varepsilon/(1+\sqrt{1+\varepsilon})$. Así el intervalo simétrico de radio $\delta_*$ queda dentro de esa componente, pues su extremo inferior supera $\sqrt{1-\varepsilon}$. Si un radio es mayor, incluye $x=\sqrt{1+\varepsilon}$, distinto de $1$, cuyo error es exactamente $\varepsilon$, infracción.

**Retorno visual.** Véase [C13-F03](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Alrededor de uno, con $0<\varepsilon<1$, las entradas admisibles positivas están entre las dos raíces indicadas. El lado derecho ofrece el margen menor, por lo que determina la mayor ventana simétrica. El radio óptimo aún funciona porque su extremo superior queda fuera de la bola abierta de entradas. Cualquier aumento lo incluye y produce error exactamente igual a la tolerancia, que ya infringe el requisito estricto. Así la frontera permite acreditar la optimalidad.

## 13.9. Reparar una respuesta que depende de la entrada

[]{#MA-EX-ANM-01-013-009}

[]{#MA-SOL-ANM-01-013-009}

La expresión de $\delta$ utiliza el $x$ que debía verificarse después de fijar el radio. No produce una respuesta única para toda la ventana. La reparación fija primero $|x-1|<1$, que da $|x+1|<3$, y elige $\delta=\min(1,\varepsilon/3)$. Para toda entrada de esa ventana, $|x^2-1|<3|x-1|<\varepsilon$. La fórmula defectuosa queda como objeto de diagnóstico, no como prueba.

La respuesta debe fijarse antes de considerar la entrada arbitraria. El borrador usa precisamente esa entrada para definir el tamaño de su ventana, por lo que no prueba un radio común. La reparación sustituye el factor variable por una constante obtenida en una ventana auxiliar. Con $|x-1|<1$, $|x+1|<3$, y el mínimo propuesto hace $|x^2-1|=|x-1||x+1|<\varepsilon$ para toda la ventana.

## 13.10. Proteger un recíproco desplazado

[]{#MA-EX-ANM-01-013-010}

[]{#MA-SOL-ANM-01-013-010}

Si $|x-1|<1$, entonces $|x-3|\ge2-|x-1|>1$; las entradas no alcanzan $3$. El error es $|1/(x-3)+1/2|=|x-1|/(2|x-3|)<|x-1|/2$. Tomamos $\delta=\min(1,2\varepsilon)$. Para toda entrada del dominio dentro de esa ventana, el error es menor que $\delta/2\le\varepsilon$.

El dominio natural excluye tres. La ventana auxiliar alrededor de uno permanece separada de ese punto porque $|x-3|>1$. Después de reunir los cocientes, el numerador del error es $x-1$ y el denominador tiene magnitud mayor que dos. El radio de precisión $2\varepsilon$ controla ese error y el mínimo conserva la protección del denominador. La prueba declara por qué cada evaluación está permitida antes de aplicar la estimación.

## 13.11. Una cota que incluye el centro

[]{#MA-EX-ANM-01-013-011}

[]{#MA-SOL-ANM-01-013-011}

[]{#MA-SEC-ANM-01-013-003}

La tolerancia $1$ entrega $r>0$ con $|f(x)|<|L|+1$ para toda entrada no central de la ventana. Elegimos $K=\max(|L|+1,|f(a)|+1)$. En el centro, $|f(a)|<K$; fuera del centro, la cota previa da $|f(x)|<K$. La unión de ambos casos prueba acotación. Sólo se añadió un valor finito a una cota local.

La definición da una barrera sólo para las entradas no centrales. Para ampliar a la ventana completa hay que añadir el valor particular $f(a)$, que es un real finito porque $a\in D$. Tomar el máximo de ambas barreras cubre los dos casos. No se necesita que ese valor central coincida con $L$: una evaluación excepcional puede estar lejos del destino y aun así incluirse en una cota local finita.

## 13.12. Encierro sin existencia supuesta

[]{#MA-EX-ANM-01-013-012}

[]{#MA-SOL-ANM-01-013-012}

Las cotas implican $|f(x)|\le2x^2$ en esa ventana. Para $\varepsilon>0$ tomamos $\delta=\min(1,\sqrt{\varepsilon/2})>0$. Si $0<|x|<\delta$, entonces $|f(x)|\le2x^2<2\delta^2\le\varepsilon$. No se supuso que $f$ tuviera límite: el control universal lo establece. Las raíces positivas pertenecen al álgebra real elemental.

Si $f(x)$ es no negativo, la cota superior da $|f(x)|\le2x^2$; si es negativo, la inferior da $|f(x)|\le x^2\le2x^2$. Por eso la estimación absoluta es válida en ambos casos. El radio elegido permanece en la región de encierro y hace $2x^2<\varepsilon$. La prueba parte de desigualdades sobre valores y construye directamente el límite, sin presuponer un destino de $f$.

## 13.13. Oscilar y aun así converger

[]{#MA-EX-ANM-01-013-013}

[]{#MA-SOL-ANM-01-013-013}

Para toda entrada, $|b(x)|=1$ y $|h(x)|=|x|$. Dado $\varepsilon>0$ basta $\delta=\varepsilon$. Si $0<|x|<\delta$, el error de $h$ es menor que $\varepsilon$. El control procede de la magnitud del factor, no de la existencia de su límite.

La magnitud de $b(x)$ es uno en cualquiera de sus dos ramas, así que no hace falta conocer su comportamiento de límite. La identidad $|xb(x)|=|x|$ reduce el control de salida al de entrada. La elección $\delta=\varepsilon$ funciona uniformemente para entradas racionales e irracionales. Las oscilaciones del signo pueden mantenerse, mientras el tamaño de las salidas se aproxima a cero.

## 13.14. El orden no conserva separación estricta

[]{#MA-EX-ANM-01-013-014}

[]{#MA-SOL-ANM-01-013-014}

En $(0,\infty)$, $f(x)=0$ y $g(x)=x$ satisfacen $f<g$ y ambas tienen límite cero: para la identidad sirve $\delta=\varepsilon$. Para la afirmación general, si $f\to L$, $g\to M$ y $L>M$, pedimos errores menores que $(L-M)/3$, reunimos radios con la ventana de orden y obtenemos una entrada por acumulación. Allí $f>L-(L-M)/3>M+(L-M)/3>g$, contradicción. Luego $L\le M$.

El ejemplo demuestra que una diferencia positiva entre funciones puede desaparecer en el límite. Para el resultado general, suponemos lo contrario, $L>M$, y usamos una tolerancia menor que la separación de los destinos. Los radios y la ventana de orden deben reunirse para que las tres condiciones valgan en la misma entrada. La acumulación proporciona esa entrada. Las cotas colocarían a $f$ por encima de $g$, contradiciendo su orden local.

## 13.15. Dos destinos no caben en una misma ventana

[]{#MA-EX-ANM-01-013-015}

[]{#MA-SOL-ANM-01-013-015}

Si $L\ne M$, $d=|L-M|>0$. Ambos contratos para $\varepsilon=d/2$ dan radios positivos. Acumulación proporciona una entrada en su mínimo. La triangular da $d\le|L-f(x)|+|f(x)-M|<d/2+d/2=d$, contradicción. La igualdad en la suma de tolerancias es admisible porque los errores individuales son estrictamente menores.

Cada error es estrictamente menor que la mitad de la distancia entre candidatos. Al sumarlos obtenemos una cantidad estrictamente menor que la distancia completa, aunque los dos presupuestos sumen exactamente esa distancia. Por eso no se exige un margen de un tercio en esta variante. La entrada común sigue siendo indispensable y viene de la acumulación; sin ella, los controles podrían ser vacíos y la triangular no podría aplicarse a una salida real.

## 13.16. La frontera ya es infracción

[]{#MA-EX-ANM-01-013-016}

[]{#MA-SOL-ANM-01-013-016}

[]{#MA-SEC-ANM-01-013-004}

Tomemos $\varepsilon_0=1$. Dado $\delta>0$, sea $x=-\delta/2$. Entonces $0<|x|<\delta$ y $|x-1|=1+\delta/2>1$. El candidato se refuta aunque la función sí tiene otro límite, cero.

**Retorno visual.** Véase [C13-F04](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El candidato uno queda a distancia $1+\delta/2$ de la salida negativa elegida. La tolerancia uno se fija antes del radio y todos los radios tienen un infractor no central. Esto refuta el candidato uno, mientras la función identidad tiene límite cero por el control $\delta=\varepsilon$. Para ilustrar específicamente la frontera también puede usarse tolerancia $1/2$ y una entrada positiva suficientemente pequeña, pero el infractor negativo ya prueba la refutación pedida.

## 13.17. Una escala basta para todos los radios

[]{#MA-EX-ANM-01-013-017}

[]{#MA-SOL-ANM-01-013-017}

La negación completa aplicada a $\delta=r_n$ produce un infractor para cada $n$ con la misma $\varepsilon_0$. A la inversa, dados conjuntos no vacíos y un radio cualquiera $\delta$, la propiedad de la escala da $n$ con $r_n<\delta$. Un único punto infractor de ese conjunto también está en la ventana de radio $\delta$ y conserva el error $\ge\varepsilon_0$. No hace falta escoger todos los puntos a la vez.

No se exige que la escala sea monótona: sólo que contenga algún radio menor que cualquier radio propuesto. En la dirección inversa escogemos ese índice y usamos un testigo del conjunto correspondiente. La tolerancia debe ser la misma en todos los conjuntos, para que la infracción persista al cambiar de escala. La prueba refuta el candidato sin construir todavía una función que elija testigos para todos los índices simultáneamente.

## 13.18. Todos los reales quedan descartados

[]{#MA-EX-ANM-01-013-018}

[]{#MA-SOL-ANM-01-013-018}

Fijemos cualquier $L$. Para tolerancia $1$ y cualquier $\delta>0$, elegimos $x=\min(\delta/2,1/[2(|L|+1)])>0$. Está en el dominio y en la ventana perforada; $1/|x|\ge2(|L|+1)$ implica $|f(x)-L|\ge f(x)-|L|>1$. Cada candidato tiene infractores arbitrariamente próximos, por lo que no existe límite real finito.

El candidato real $L$ es arbitrario, y la tolerancia uno sirve para todos. El segundo término del mínimo hace que la salida sea mayor que la magnitud de $L$ con un margen superior a uno; el primero sitúa la entrada dentro de cualquier ventana propuesta. Se verifican dominio, perforación y error grande. La conclusión descarta todos los límites reales finitos, sin introducir aquí una definición de límite infinito.

## 13.19. Cada entrada favorable no es un límite

[]{#MA-EX-ANM-01-013-019}

[]{#MA-SOL-ANM-01-013-019}

Sea $f(x)=0$ para $x>0$, $f(x)=1$ para $x\le0$. Dadas $\varepsilon,\delta>0$, el punto $\delta/2$ cumple la condición favorable. Pero el punto $-\delta/2$ tiene error $1$ para cada radio, por lo que la tolerancia $\varepsilon_0=1/2$ refuta $L=0$. La condición débil elige una entrada; el límite debe controlar todas.

En cada ventana hay una entrada positiva que entrega salida cero, por lo que el enunciado débil encuentra un testigo favorable para cualquier precisión. En la misma ventana hay también una entrada negativa con salida uno. El límite exige controlar ambas, no sólo seleccionar la que conviene. La tolerancia fija $1/2$ y los infractores negativos muestran la diferencia entre existencia de un punto bueno y control universal de la ventana.

## 13.20. Fallo sin magnitud infinita

[]{#MA-EX-ANM-01-013-020}

[]{#MA-SOL-ANM-01-013-020}

El salto con salidas $-1$ y $1$ está acotado por $1$. Para cada candidato $L$ una de las distancias a esas dos salidas es $\ge1$, por triangular. Fijado ese signo, el punto con ese signo y magnitud $\delta/2$ infringe el error para cualquier radio, con tolerancia $1$. La falta de límite puede deberse a incompatibilidad de destinos sin que los valores sean grandes.

Para cada candidato, la distancia entre las dos salidas obliga a que una de ellas quede separada de él al menos por uno. Elegimos esa rama una vez fijado el candidato. Después cada radio proporciona una entrada de la rama con magnitud $\delta/2$. Así se verifican todos los cuantificadores de la refutación. La función mantiene magnitudes iguales a uno, de modo que la inexistencia del límite no puede atribuirse a falta de acotación.

## 13.21. Una ruta favorable engaña

[]{#MA-EX-ANM-01-013-021}

[]{#MA-SOL-ANM-01-013-021}

[]{#MA-SEC-ANM-01-013-005}

La ruta $u_n=1/(n+1)$ tiene imágenes cero. La ruta $v_n=-1/(n+1)$ tiene imágenes uno, pues nunca coincide con una entrada positiva de la primera ruta. Ambas evitan cero y convergen a él por C06. Si hubiese límite $L$, la dirección directa y la unicidad secuencial darían a la vez $L=0$ y $L=1$, contradicción.

Las dos rutas pertenecen al dominio real, nunca alcanzan cero y sus magnitudes $1/(n+1)$ tienden a cero. La primera coincide por construcción con las entradas de valor cero; la segunda es negativa y por eso siempre produce uno. La dirección directa del criterio secuencial obligaría a ambas imágenes a tener el mismo destino si existiera un límite funcional. Basta esta contradicción y no se utiliza elección numerable, porque las rutas están dadas por fórmulas.

## 13.22. Un prefijo puede tocar el centro

[]{#MA-EX-ANM-01-013-022}

[]{#MA-SOL-ANM-01-013-022}

Dado $\varepsilon>0$, el límite funcional ofrece $\delta$. La convergencia de $x_n$ da $N_1$ que asegura $|x_n-a|<\delta$. Para $n\ge\max(N_0,N_1)$ también hay distancia positiva, y la implicación funcional produce error menor que $\varepsilon$. Los términos anteriores no afectan la convergencia.

El corte máximo reúne aproximación al centro y evitación eventual del centro. A partir de él, cada término satisface todas las condiciones del límite perforado. Los términos iniciales pueden evaluar $f(a)$, pero sólo forman un prefijo finito y no alteran la convergencia de las imágenes. La hipótesis de que todas las evaluaciones estén definidas asegura que la sucesión de imágenes sea un objeto completo, no una lista con términos ausentes.

## 13.23. El mínimo vive en los índices

[]{#MA-EX-ANM-01-013-023}

[]{#MA-SOL-ANM-01-013-023}

Por sobreyectividad y no vaciedad de $E_n$, el conjunto $I_n=\{k:e(k)\in E_n\}$ contiene algún natural. El buen orden da un mínimo único. La regla $n\mapsto\min I_n$ es funcional y su composición con $e$ produce el selector real. Un conjunto real no vacío puede no tener mínimo, por ejemplo $(0,1)$; no se puede reemplazar el mínimo de índices por uno de valores.

**Retorno visual.** Véase [C13-F05](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La enumeración permite convertir una búsqueda entre reales en una búsqueda entre naturales. Por sobreyectividad, algún índice representa un infractor; el conjunto de índices es no vacío y su menor elemento es único. Esa unicidad define una regla para cada escala. Un conjunto de reales puede no tener un menor valor y, aunque lo tuviera en algunos casos, no se ha supuesto tal propiedad para todos los $E_n$. El buen orden utilizado pertenece a los índices naturales.

## 13.24. La ruta de infracciones prueba la recíproca

[]{#MA-EX-ANM-01-013-024}

[]{#MA-SOL-ANM-01-013-024}

Supongamos que todas las rutas admisibles tienen imágenes tendiendo a $L$ y que falla el contrato funcional. Hay $\varepsilon_0>0$ y conjuntos reales $E_n$ no vacíos de infractores con $0<|x-a|<1/(n+1)$. Aplicamos aquí, y sólo aquí, $\mathrm{CC}(\mathbb R)$ para obtener una función $n\mapsto x_n\in E_n$. Las cotas implican $x_n\to a$, pero $|f(x_n)-L|\ge\varepsilon_0$ para todos los índices impide convergencia de imágenes a $L$. La contradicción prueba el límite. No se presenta como prueba incondicional.

La hipótesis adicional sólo aparece al convertir los conjuntos de infractores en una sucesión simultáneamente seleccionada. Una vez dada esa sucesión, las distancias al centro tienden a cero por su cota $1/(n+1)$, y los errores de salida permanecen por encima de la misma tolerancia positiva. La ruta contradice el supuesto de convergencia de todas las imágenes admisibles. Las demás estimaciones no necesitan una nueva elección, y la conclusión mantiene explícita la condición fundacional.

## 13.25. No hace falta una ruta distinta en cada paso

[]{#MA-EX-ANM-01-013-025}

[]{#MA-SOL-ANM-01-013-025}

La prueba de convergencia sólo necesita $|x_n-a|<1/(n+1)$; no usa inyectividad. Si un punto fijo $t\ne a$ apareciera en índices arbitrariamente grandes, su distancia $d=|t-a|>0$ tendría que ser menor que $1/(n+1)$ para índices con esa escala menor que $d$, imposible. Puede haber repeticiones finitas de valores, aunque no se hayan exigido términos diferentes.

Si $t\ne a$ tiene distancia fija $d>0$, existe un corte desde el cual $1/(n+1)<d$. La cota de los infractores excluye entonces que $x_n=t$ en cualquier índice posterior. Cada valor no central puede repetirse al principio, pero sólo finitas veces. No se deduce que todos los términos sean distintos ni se necesita imponerlo: la convergencia sigue únicamente de que sus distancias al centro se reduzcan con la escala.

## 13.26. Cancelar antes de usar un cociente

[]{#MA-EX-ANM-01-013-026}

[]{#MA-SOL-ANM-01-013-026}

[]{#MA-SEC-ANM-01-013-006}

El dominio es $\mathbb R\setminus\{2\}$. Allí la factorización da $(x^2-4)/(x-2)=x+2$, que tiene límite $4$: con $\delta=\varepsilon$ el error es $|x-2|<\varepsilon$. El límite del denominador es cero, por lo que el criterio de cocientes no se aplica. La cancelación es válida sólo fuera del punto excluido, exactamente el dominio pertinente.

Factorizamos el numerador como $(x-2)(x+2)$. En el dominio permitido el factor $x-2$ es no nulo y puede cancelarse, obteniendo igualdad exacta con la afín $x+2$. No se extiende esa igualdad como evaluación del cociente en dos, donde el cociente no está definido. Para el límite sólo hacen falta las entradas perforadas; allí el error respecto de cuatro es $|x-2|$. La regla de cocientes no permite dividir por el límite cero del denominador.

## 13.27. Un denominador con ceros lejanos

[]{#MA-EX-ANM-01-013-027}

[]{#MA-SOL-ANM-01-013-027}

El dominio es $D_0=\mathbb R\setminus\{-2,2\}$. Polinomios dan límites $1$ y $-4$ en cero; el segundo es no nulo. La regla de cocientes prueba límite $-1/4$. Los ceros lejanos no impiden una ventana local: para $|x|<1$, $|g(x)|=4-x^2>3$. No se afirma que el cociente esté definido en los puntos excluidos.

Los puntos excluidos menos dos y dos no impiden que cero sea punto de acumulación del dominio. En una ventana de radio uno no aparecen esos ceros, y la cota $4-x^2>3$ protege el denominador. Los límites del numerador y denominador son uno y menos cuatro, así que la regla se aplica con destino $-1/4$. Declarar el dominio conserva la diferencia entre una estimación local válida y una fórmula evaluable en todos los reales.

## 13.28. Producto desde una identidad diferente

[]{#MA-EX-ANM-01-013-028}

[]{#MA-SOL-ANM-01-013-028}

Sea $A=1+|L|+|M|>0$. Dado $\varepsilon>0$, exigimos ambos errores menores que $t=\min(1,\varepsilon/A)$. En el mínimo de radios, $|(f-L)(g-M)|<t^2\le t$, y los otros términos están acotados por $|L|t$ y $|M|t$. Sumando con la estricta cota del primer término obtenemos error $<At\le\varepsilon$. Esta variante usa el pequeño tamaño del producto de errores en vez de una cota separada de $f$.

La nueva identidad separa un producto de errores y dos errores multiplicados por destinos fijos. Pedir ambos errores menores que $t\le1$ controla su producto por $t^2\le t$. Los otros dos términos añaden presupuestos $|L|t$ y $|M|t$, y la constante $A$ reúne los tres. El mínimo de los radios hace disponibles los dos errores a la vez. Incluso si alguno de los destinos es cero, $A$ sigue siendo positivo y la elección está definida.

## 13.29. Norma y diferencia de normas

[]{#MA-EX-ANM-01-013-029}

[]{#MA-SOL-ANM-01-013-029}

La triangular inversa aplicada primero a los dos reales $|f|-|g|$ y $|L|-|M|$ da error final $\le\bigl|(|f|-|g|)-(|L|-|M|)\bigr|$. La triangular y la inversa de nuevo lo acotan por $||f|-|L||+||g|-|M||\le|f-L|+|g-M|$. Pedimos cada error menor que $\varepsilon/2$ y reunimos radios. La cota prueba la conclusión directamente.

El error final se estima aplicando la triangular inversa al valor absoluto exterior y luego a los dos valores absolutos interiores. Cada paso reduce el problema a las diferencias originales $f-L$ y $g-M$. La suma de esos dos errores se hace menor que $\varepsilon$ usando mitades y el mínimo de radios. Este control directo no exige separar casos según los signos de los valores ni conocer previamente límites de todas las expresiones intermedias.

## 13.30. Un producto converge sin límites de los factores

[]{#MA-EX-ANM-01-013-030}

[]{#MA-SOL-ANM-01-013-030}

Sea $f(x)=g(x)=s(x)$, el salto con valores $\pm1$. Las rutas positivas y negativas dan destinos distintos y refutan el límite de cada factor. Pero $f(x)g(x)=s(x)^2=1$ para toda entrada, así que el producto tiene límite $1$ con cualquier radio y error cero. La regla del producto es suficiente, no una condición necesaria para que el producto converja.

Para cada factor, las entradas a ambos lados de cero producen valores constantes diferentes, y las rutas explícitas de cada signo refutan cualquier destino común. Al multiplicar los factores iguales, los signos se cancelan y queda siempre uno. El producto tiene error cero respecto de uno en toda entrada. Por tanto la convergencia de ambos factores es una hipótesis suficiente de la regla del producto, pero no una condición necesaria para que el producto concreto converja.

## 13.31. El único lado disponible

[]{#MA-EX-ANM-01-013-031}

[]{#MA-SOL-ANM-01-013-031}

[]{#MA-SEC-ANM-01-013-007}

El lado derecho acumula y el izquierdo está vacío, por lo que no le asignamos límite. Para $\varepsilon>0$, $\delta=\min(1,\sqrt\varepsilon)$ hace que toda entrada perforada sea positiva y tenga $|f(x)|=x^2<\varepsilon$. El límite en $D$ es cero y coincide con el límite derecho; el valor central $9$ se excluye.

**Retorno visual.** Véase [C13-F06](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Toda entrada perforada del dominio es positiva. La ventana propuesta la mantiene además dentro de la región donde vale la regla $x^2$ y hace su cuadrado menor que la tolerancia. La acumulación derecha puede verificarse escogiendo un positivo menor que el radio y menor que dos. El lado izquierdo no ofrece ninguna entrada, por lo que no se formula un límite allí. La evaluación nueve en el centro no interviene en el control perforado.

## 13.32. Reunir piezas finitas

[]{#MA-EX-ANM-01-013-032}

[]{#MA-SOL-ANM-01-013-032}

Para $\varepsilon>0$, tomamos radios $\delta_1,\delta_2$ válidos. Su mínimo es positivo. Toda entrada perforada de $D$ pertenece a una pieza y recibe el error menor que $\varepsilon$ de esa pieza, aunque pueda pertenecer a ambas. Luego hay límite en $D$. Si el límite vale en $D$, el mismo radio funciona en cada subconjunto; la acumulación supuesta permite formular ambos límites restringidos.

El mínimo de dos radios positivos vuelve a ser positivo, y cualquier entrada del dominio unión pertenece al menos a una pieza. El control de esa pieza basta para asegurar la precisión, incluso si la entrada también pertenece a la otra. En la vuelta, restringir sólo elimina entradas y conserva la estimación. La hipótesis de acumulación en cada pieza permite que ambos límites restringidos tengan sentido y no sean fórmulas vacías.

## 13.33. Infinitas piezas no garantizan reunión

[]{#MA-EX-ANM-01-013-033}

[]{#MA-SOL-ANM-01-013-033}

Cada $D_k$ acumula cero: para un radio $r>0$ existe un real positivo irracional menor que $r$, que no es un recíproco entero. Tal entrada puede obtenerse explícitamente como $\sqrt2/m$ con entero $m>\sqrt2/r$. Si $\delta=1/(2k)$, la ventana de $D_k$ excluye su único punto con valor uno, $1/k$, y el error es cero para toda tolerancia. La unión de las piezas es todo $D$: los no recíprocos están en todas y cada recíproco en su pieza. La ruta $x_n=1/(n+1)$ tiene imágenes uno; para cada radio hay tal entrada con error uno, así que el candidato cero falla en la unión. Además, la ruta $\sqrt2/(n+1)$ tiene imágenes cero y descarta cualquier límite junto a la primera.

En cada pieza sólo hay un punto con salida uno, y puede excluirse con un radio menor que su distancia a cero. Pero las distancias de esos puntos se reducen al variar la pieza, de modo que no hay una ventana común que los elimine todos. La unión vuelve a incorporar infinitas entradas de valor uno próximas a cero. Las dos rutas finales acreditan destinos incompatibles. Tener un radio adecuado para cada pieza no produce automáticamente un radio positivo para toda su unión.

## 13.34. Una prueba densa puede omitir todo el problema

[]{#MA-EX-ANM-01-013-034}

[]{#MA-SOL-ANM-01-013-034}

La restricción racional es constante cero y $\delta=1$ sirve para cualquier tolerancia; cero acumula racionales por los puntos $1/m$. En el dominio completo, $1/(n+1)$ y $\sqrt2/(n+1)$ son rutas no nulas tendiendo a cero. La segunda es irracional en cada índice, pues de lo contrario $\sqrt2$ sería racional. Las imágenes son constantes cero y uno. Un límite funcional daría el mismo límite a ambas rutas por la dirección directa, contradicción.

El indicador de irracionales vale cero en cada racional, así que el límite restringido es cero con error nulo. En el dominio completo la ruta racional conserva esa salida, mientras la ruta irracional conserva la salida uno. Ambas están dadas por fórmulas y convergen a cero; el cociente de $\sqrt2$ por un entero positivo sigue siendo irracional. La densidad del conjunto favorable no impone ningún control sobre los valores del conjunto omitido.

## 13.35. Al menos un lado acumula

[]{#MA-EX-ANM-01-013-035}

[]{#MA-SOL-ANM-01-013-035}

Si ninguno acumulara, habría radios positivos $r_-,r_+$ sin entradas de cada lado en sus ventanas. En el mínimo no habría ninguna entrada distinta de $a$ del dominio, contradicción. Si sólo el derecho acumula, el izquierdo tiene un radio sin entradas. Todo control del límite derecho se reúne con ese radio y controla el dominio completo; la implicación inversa es restricción. El caso izquierdo es simétrico.

Si ninguno de los lados acumulara, existirían dos radios que eliminan sus respectivas entradas. Su mínimo eliminaría todas las entradas distintas del centro, contradiciendo la acumulación del dominio. Si sólo un lado acumula, el otro está ausente en alguna ventana y puede descartarse al reducir el radio. El límite completo se vuelve exactamente el límite del lado disponible. No se asigna un destino por vacuidad al lado que falta.

## 13.36. La composición pierde el centro perforado

[]{#MA-EX-ANM-01-013-036}

[]{#MA-SOL-ANM-01-013-036}

[]{#MA-SEC-ANM-01-013-008}

Tomamos $f(x)=0$ para todos los reales; $g(y)=0$ si $y\ne0$ y $g(0)=2$. Los dos límites son cero porque sus errores son cero en las ventanas pertinentes. La composición es constante dos y tiene límite dos. El límite perforado de $g$ sólo controla entradas distintas de cero; la interior cae siempre en cero.

**Retorno visual.** Véase [C13-F07](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El límite exterior observa sólo entradas distintas de cero y por eso no controla $g(0)=2$. La interior, en cambio, entrega cero en todas las entradas y obliga a la composición a evaluar ese valor excepcional. Esto separa el límite perforado de la exterior de su evaluación central. El ejemplo satisface los tipos y demuestra todas las conclusiones mediante errores nulos; el fallo de la regla ingenua está en perder la perforación, no en una composición mal definida.

## 13.37. Componer dos cuadrados con certificados

[]{#MA-EX-ANM-01-013-037}

[]{#MA-SOL-ANM-01-013-037}

Para $g(y)=y^2$ en $b=1$, el radio $\eta=\min(1,\varepsilon/3)$ es válido y $g(1)=1$. Para $f(x)=x^2$ en $1$, tomamos $\delta=\min(1,\eta/3)$. Entonces $|f(x)-1|<\eta$. Si $f(x)\ne1$ aplica el control de $g$; si $f(x)=1$, el error final es cero. El tipo real de ambas funciones permite componerlas. Así $|x^4-1|<\varepsilon$ en toda la ventana.

El diseño empieza con la tolerancia final. La segunda etapa entrega una escala intermedia $\eta$, y la primera entrega un radio que sitúa sus salidas dentro de esa escala. Si la salida intermedia coincide con uno, el valor central de la exterior es el destino correcto y el error es cero. Si no coincide, se aplica su certificado perforado. La prueba cubre ambas posibilidades en toda la ventana y evita usar el límite exterior donde su hipótesis no valga.

## 13.38. La alternativa central sin límites conocidos

[]{#MA-EX-ANM-01-013-038}

[]{#MA-SOL-ANM-01-013-038}

En esa misma ventana la composición tiene valor constante $g(b)$. Para cualquier $\varepsilon>0$ usamos su radio $r$ y el error es cero. Por tanto el límite es $g(b)$. No importa el comportamiento de $g$ fuera de la salida única localmente alcanzada; las hipótesis del teorema general de composición eran suficientes, no necesarias.

Sólo necesitamos saber que la interior es localmente constante y que $b$ está en el dominio de la exterior. Todas las salidas compuestas de esa ventana son exactamente $g(b)$, por lo que el mismo radio responde a cualquier tolerancia. El comportamiento de $g$ en otras entradas resulta irrelevante para esta composición local. No estamos deduciendo un límite exterior: construimos directamente el de la composición mediante las salidas que realmente alcanza.

## 13.39. Composición a través de un subconjunto de salidas

[]{#MA-EX-ANM-01-013-039}

[]{#MA-SOL-ANM-01-013-039}

Fijado $\varepsilon>0$, el contrato de $g|_A$ ofrece $\eta>0$ para entradas de $A$ próximas y distintas de $b$. El límite de $f$ ofrece $\delta_f>0$ para ese radio. Reunimos $\delta_f$ con el radio $r$ de pertenencia y evitación. Para toda entrada de la nueva ventana, $f(x)\in A\setminus\{b\}$ y $|f(x)-b|<\eta$, de modo que $|g(f(x))-L|<\varepsilon$. El segundo contrato sólo se necesita en las salidas realmente disponibles.

La restricción exterior sólo controla entradas de $A$ diferentes de $b$. La hipótesis de pertenencia y evitación asegura que la interior entregue precisamente entradas de ese tipo, y su límite las aproxima a $b$ dentro del radio requerido. El mínimo reúne estos dos controles. La exterior puede comportarse de otra manera en $E\setminus A$ sin afectar la conclusión, porque esas salidas intermedias no aparecen localmente en la composición.

## 13.40. Un criterio exacto para tocar una salida defectuosa

[]{#MA-EX-ANM-01-013-040}

[]{#MA-SOL-ANM-01-013-040}

La evitación es suficiente por el teorema del texto. Para probar necesidad, supongamos que la composición tiende a $L$ y sea $d=|g(b)-L|>0$. Su contrato para $\varepsilon=d/2$ da $\delta>0$ con error menor que $d/2$ en la ventana. Si alguna entrada allí tuviera $f(x)=b$, el error final sería $d$, contradicción. Luego todas evitan $b$. El defecto central convierte una condición suficiente en una condición necesaria para ese destino particular.

**Retorno visual.** Véase [C13-F07](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El defecto central tiene magnitud fija $d=|g(b)-L|>0$. Un control de la composición con tolerancia $d/2$ no puede permitir ni una entrada local que alcance $b$, porque su salida final tendría error exactamente $d$. Esto demuestra necesidad de la evitación. La dirección suficiente utiliza después los límites interior y exterior con radios anidados. La equivalencia es para el destino particular $L$; no afirma que cualquier composición que toque el centro carezca de todo límite.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html)
