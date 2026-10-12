---
content-id: MA-BCH-0273
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-017-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 17
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C17_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §17.1 — Un radio antes de conocer los dos puntos

### Microcontrol 001

[]{#MA-MIC-ANM-01-017-001}

[]{#MA-MSOL-ANM-01-017-001}

[]{#MA-SEC-ANM-01-017-001}

**Pregunta.** ¿Qué debe quedar fijado antes de conocer $x,y$ en continuidad uniforme?

**Solución.** Para cada tolerancia $\varepsilon>0$, un solo $\delta>0$ que sirva para todos los pares del dominio fijado.

El radio responde a la precisión solicitada y puede depender de la función y del dominio fijados. Después de elegirlo se comprueba cualquier par de entradas que esté suficientemente próximo. Cambiarlo al conocer uno de los puntos destruiría el orden uniforme de cuantificadores. La misma escala debe controlar simultáneamente todas las regiones del dominio.

### Microcontrol 002

[]{#MA-MIC-ANM-01-017-002}

[]{#MA-MSOL-ANM-01-017-002}

**Pregunta.** ¿Qué dependencia adicional admite la continuidad puntual?

**Solución.** El radio se elige después del centro $a$, y puede depender de él además de la tolerancia, función y dominio.

En un centro fijado, sólo se compara con su valor de salida y se puede adaptar la escala a ese lugar. Eso permite radios cada vez menores al cambiar de centro sin invalidar continuidad puntual. Para uniformidad hay que demostrar que una sola elección basta para todos los centros. No es una diferencia de fórmula de error, sino de dependencia del radio.

### Microcontrol 003

[]{#MA-MIC-ANM-01-017-003}

[]{#MA-MSOL-ANM-01-017-003}

**Pregunta.** ¿Por qué la uniformidad implica continuidad en cada punto?

**Solución.** Se fija el centro como uno de los dos argumentos y se conserva el mismo radio uniforme para todos los otros puntos del dominio.

Dado $a\in D$, aplicamos el control uniforme al par $(x,a)$. Como el radio ya funciona para todos los pares, también funciona para todos los $x$ próximos a ese centro. La salida de comparación pasa a ser exactamente $f(a)$, como exige continuidad. El argumento acredita continuidad en cada punto sin volver a elegir la escala según él.

### Microcontrol 004

[]{#MA-MIC-ANM-01-017-004}

[]{#MA-MSOL-ANM-01-017-004}

**Pregunta.** ¿Qué tolerancia se mantiene fija al negar uniformidad?

**Solución.** Una $\varepsilon_0>0$ para la que todo radio positivo admite un par de entradas próximas con diferencia de salida al menos $\varepsilon_0$.

Se fija primero la tolerancia infringida y después se permite que el par dependa del radio propuesto. El error debe ser mayor o igual que esa tolerancia, negación del error estricto de la definición. Un único par distante no refuta todos los radios. Para negar uniformidad necesitamos infractores arbitrariamente próximos con una separación de salidas que no disminuya.

### Microcontrol 005

[]{#MA-MIC-ANM-01-017-005}

[]{#MA-MSOL-ANM-01-017-005}

**Pregunta.** ¿Un radio local dependiente del centro prueba falta de uniformidad?

**Solución.** No. Es una solución local, no una prueba de que todo candidato común falla. Hay que producir testigos para cada $\delta>0$.

Una elección local es sólo un certificado posible de continuidad. Su dependencia del centro no demuestra que otra elección independiente sea imposible. Por ejemplo, la identidad admite también radios locales innecesariamente variables y sigue siendo uniforme. La negación exige comprobar el fracaso de todo candidato común con una tolerancia fija.

### Microcontrol 006

[]{#MA-MIC-ANM-01-017-006}

[]{#MA-MSOL-ANM-01-017-006}

**Pregunta.** ¿Qué radio sirve para una constante Lipschitz $L>0$?

**Solución.** $\delta=\varepsilon/L$; la desigualdad $|f(x)-f(y)|\le L|x-y|$ convierte distancia estrictamente menor que ese radio en error menor que $\varepsilon$.

La constante $L$ controla todas las parejas y no cambia con sus posiciones. Si la distancia es estrictamente menor que $\varepsilon/L$, la cota no estricta inicial se convierte en error estrictamente menor que $\varepsilon$. Si $L=0$, todas las salidas son iguales y cualquier radio positivo sirve; se trata por separado para no dividir por cero.

### Microcontrol 007

[]{#MA-MIC-ANM-01-017-007}

[]{#MA-MSOL-ANM-01-017-007}

**Pregunta.** ¿Por qué la raíz puede ser uniforme sin ser Lipschitz?

**Solución.** Su control es $|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}$, que da radio $\varepsilon^2$. En cero, los cocientes $1/\sqrt{x}$ no están acotados.

El radio cuadrático responde a la tolerancia sin conocer las entradas y por ello sí es uniforme. Un control Lipschitz exigiría una constante lineal común para la relación entre error y distancia. Comparar una entrada positiva con cero hace crecer sin cota ese cociente. Fallar esa condición más fuerte no invalida el control no lineal ya probado.

### Microcontrol 008

[]{#MA-MIC-ANM-01-017-008}

[]{#MA-MSOL-ANM-01-017-008}

**Pregunta.** ¿Qué ocurre con el dominio vacío?

**Solución.** La condición sobre pares es vacía y cualquier radio positivo sirve; no hay puntos que exigir controlar.

Para una tolerancia cualquiera podemos elegir, por ejemplo, radio uno. No existen parejas del vacío que deban satisfacer la implicación ni que puedan refutarla. La conclusión no requiere un valor central o una muestra de salida. En un singleton sí existe un par diagonal, pero su error es cero y cualquier radio también sirve.

## §17.2 — Una cubierta y una escala de protección

### Microcontrol 009

[]{#MA-MIC-ANM-01-017-009}

[]{#MA-MSOL-ANM-01-017-009}

[]{#MA-SEC-ANM-01-017-002}

**Pregunta.** ¿Qué expresa un número de Lebesgue para una cubierta de $K$?

**Solución.** Una escala $\lambda>0$ tal que, para cada $z\in K$, algún miembro de la cubierta contiene toda la bola relativa $K\cap B(z,\lambda)$.

La escala se elige una vez para la cubierta completa, antes de fijar el centro. El miembro que contiene la bola puede cambiar con ese centro. La bola es relativa: sólo se exige contener entradas de $K$, no todos los reales cercanos. Esta distinción permite aplicar la propiedad en extremos y en compactos separados.

### Microcontrol 010

[]{#MA-MIC-ANM-01-017-010}

[]{#MA-MSOL-ANM-01-017-010}

**Pregunta.** ¿Por qué se reúnen todos los triples admisibles?

**Solución.** La familia queda determinada por una fórmula; la existencia local de un triple no se convierte en una elección simultánea por punto.

La pertenencia al conjunto de triples se determina por una condición explícita sobre centro, índice y radio. Incluir todos los que la cumplen evita necesitar un triple preferido para cada centro. Los testigos locales acreditan que alguno de esos triples cubre el punto considerado. La compacidad reduce después esa familia ya definida a datos finitos.

### Microcontrol 011

[]{#MA-MIC-ANM-01-017-011}

[]{#MA-MSOL-ANM-01-017-011}

**Pregunta.** ¿Con qué bolas se cubre y en cuáles se reserva protección?

**Solución.** Las bolas $B(a,r)$ cubren; las dobles $B(a,2r)$ están contenidas en los abiertos originales.

La bola pequeña deja un margen libre dentro de la doble. Si otro punto está próximo a una entrada de la pequeña, la triangular lo coloca en la doble, donde sí se conserva la inclusión en el abierto original. Cubrir sólo con bolas del mismo tamaño que la región protegida no reservaría ese margen para desplazar el centro.

### Microcontrol 012

[]{#MA-MIC-ANM-01-017-012}

[]{#MA-MSOL-ANM-01-017-012}

**Pregunta.** ¿Qué ocurre antes de tomar el mínimo de radios?

**Solución.** Compacidad produce un conjunto finito no vacío de triples cuyas bolas cubren $K$. Sólo sus radios concretos forman el mínimo positivo.

Una familia infinita de radios positivos puede tener ínfimo cero. La reducción por compacidad entrega primero una lista finita que aún cubre todos los puntos. Si $K$ no es vacío, esa lista tampoco lo es y su mínimo es uno de sus radios positivos. Para el vacío se asigna una escala directamente y no se toma un mínimo inexistente.

### Microcontrol 013

[]{#MA-MIC-ANM-01-017-013}

[]{#MA-MSOL-ANM-01-017-013}

**Pregunta.** ¿Qué desigualdad mueve la protección desde $a$ hasta $z$?

**Solución.** Si $|z-a|<r$ y $|w-z|<\lambda\le r$, entonces $|w-a|<\lambda+r\le2r$.

La desigualdad triangular compara $w$ con $a$ pasando por $z$. Las dos distancias estrictas dan $|w-a|<\lambda+r$, y el mínimo elegido asegura $\lambda\le r$. Así queda distancia estrictamente menor que $2r$, incluso cuando $\lambda=r$. La estrictitud final es la necesaria para pertenecer a la bola doble abierta.

### Microcontrol 014

[]{#MA-MIC-ANM-01-017-014}

[]{#MA-MSOL-ANM-01-017-014}

**Pregunta.** ¿Se elige un abierto para todos los centros simultáneamente?

**Solución.** No. La escala es global, pero para un centro $z$ fijado basta el índice de uno de los triples de la lista que lo cubre.

La lista finita ya cubre todo $K$. Para un centro concreto, pertenecer a la unión proporciona uno de sus triples. Su radio domina la escala global y su abierto protege la bola relativa de ese centro. No hace falta convertir esas existencias por centro en una función de índices elegidos para todos a la vez.

### Microcontrol 015

[]{#MA-MIC-ANM-01-017-015}

[]{#MA-MSOL-ANM-01-017-015}

**Pregunta.** ¿Cómo se tratan cubiertas por abiertos relativos?

**Solución.** Con $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real por C16 y con $K\cap W_i=A_i$; se aplica R2 al levantamiento canónico.

Un compacto real es cerrado, así el complemento de $K$ es abierto real. El levantamiento agrega esas entradas exteriores y conserva las interiores exactamente: $K\cap W_i=A_i$. La protección obtenida con el abierto ambiental se recorta después por $K$ y queda en el abierto relativo original. La fórmula evita reunir representantes ambientales seleccionados.

### Microcontrol 016

[]{#MA-MIC-ANM-01-017-016}

[]{#MA-MSOL-ANM-01-017-016}

**Pregunta.** ¿Qué número sirve para el compacto vacío?

**Solución.** $\lambda=1$, porque no hay centros que verificar, incluso si la familia de índices es vacía.

La propiedad pide una comprobación para cada centro del compacto. Si no hay centros, esa afirmación universal se cumple sin elegir ningún miembro de la cubierta. El número uno es positivo y satisface la obligación completa. Esto evita exigir una lista finita no vacía o un mínimo de radios en el caso vacío.

## §17.3 — Heine–Cantor: reducir antes de tomar el mínimo

### Microcontrol 017

[]{#MA-MIC-ANM-01-017-017}

[]{#MA-MSOL-ANM-01-017-017}

[]{#MA-SEC-ANM-01-017-003}

**Pregunta.** ¿Qué uniformiza Heine–Cantor cuando $K\subseteq D$?

**Solución.** La restricción $h:K\to\mathbb R$, si $K$ es compacto y $f$ es continua en sus puntos relativamente a $D$. No uniformiza necesariamente todo $D$.

La continuidad de la función original en los puntos de $K$ se conserva al restringir sus entradas. Heine–Cantor utiliza la compacidad de ese conjunto restringido para obtener un radio común allí. No controla pares que incluyan entradas de $D\setminus K$. La distinción de dominios impide extender la conclusión a regiones no cubiertas por la prueba.

### Microcontrol 018

[]{#MA-MIC-ANM-01-017-018}

[]{#MA-MSOL-ANM-01-017-018}

**Pregunta.** ¿Qué información guarda un par admisible $(a,r)$?

**Solución.** Que todo punto de $K$ a distancia menor que $2r$ de $a$ tiene salida a distancia menor que $\varepsilon/2$ de $h(a)$.

El par registra un control ya válido para toda la bola doble relativa. Tanto la entrada inicialmente cubierta como otra suficientemente próxima podrán compararse con la salida central $h(a)$. Se reserva medio presupuesto para cada comparación. La condición de admisibilidad incluye el control de todos los puntos de esa bola, no sólo el del centro.

### Microcontrol 019

[]{#MA-MIC-ANM-01-017-019}

[]{#MA-MSOL-ANM-01-017-019}

**Pregunta.** ¿Cómo se verifica cobertura sin función de radios?

**Solución.** Para un $a$ fijado, continuidad entrega $\rho$ y el par $(a,\rho/2)$ pertenece a la familia ya definida; su bola contiene $a$.

Para el punto que se examina, el radio de continuidad $\rho$ controla error menor que $\varepsilon/2$. Tomar $r=\rho/2$ hace que la bola doble tenga precisamente ese radio, y el centro está en la pequeña. Esto acredita cobertura por la familia de todos los pares admisibles. No se forma un mapa de radios seleccionados para todos los centros.

### Microcontrol 020

[]{#MA-MIC-ANM-01-017-020}

[]{#MA-MSOL-ANM-01-017-020}

**Pregunta.** ¿Tiene que entrar $y$ en la bola pequeña que cubre $x$?

**Solución.** No. $|y-a|<\delta+r\le2r$ lo coloca en la bola doble, que conserva el control necesario.

El punto $x$ determina una bola pequeña de la lista finita que lo contiene. Su cercanía a $y$ añade a la distancia al centro hasta otro radio, por lo que sólo se garantiza pertenencia de $y$ a la doble. Esa región fue protegida de antemano en la admisibilidad. Confundir ambas bolas omitiría el margen que hace funcionar la prueba.

### Microcontrol 021

[]{#MA-MIC-ANM-01-017-021}

[]{#MA-MSOL-ANM-01-017-021}

**Pregunta.** ¿Por qué se divide el error en dos mitades?

**Solución.** Ambas salidas se comparan con $h(a)$; la suma de los dos errores estrictos menores que $\varepsilon/2$ es menor que $\varepsilon$.

La triangular escribe $|h(x)-h(y)|\le|h(x)-h(a)|+|h(a)-h(y)|$. Los dos términos se controlan con el mismo índice y cada uno es estrictamente menor que la mitad del desafío. La suma queda estrictamente menor que el total. Comparar directamente las salidas sin ese centro común gastaría un control que aún no se había acreditado.

### Microcontrol 022

[]{#MA-MIC-ANM-01-017-022}

[]{#MA-MSOL-ANM-01-017-022}

**Pregunta.** ¿Se usa la recíproca secuencial para Heine–Cantor?

**Solución.** No. La prueba reduce una familia explícita de bolas por compacidad y usa el mínimo de una lista finita.

La familia de controles se define por una condición explícita y la compacidad proporciona su reducción finita. La elección del mínimo ocurre después de esa reducción. No se fabrican rutas de infractores ni se deduce continuidad de un criterio secuencial. Por ello la prueba de Heine–Cantor no depende de CC(R) usada en otra recíproca.

### Microcontrol 023

[]{#MA-MIC-ANM-01-017-023}

[]{#MA-MSOL-ANM-01-017-023}

**Pregunta.** ¿Necesita $K$ ser un intervalo?

**Solución.** No. Compactos con varias piezas o conjuntos finitos admiten el mismo argumento.

El argumento sólo usa cobertura por controles locales, compacidad y una lista finita de radios positivos. No necesita todos los puntos entre dos entradas ni monotonía. Las bolas relativas ignoran las entradas ausentes entre piezas. Así un compacto desconexo puede recibir exactamente el mismo control uniforme.

### Microcontrol 024

[]{#MA-MIC-ANM-01-017-024}

[]{#MA-MSOL-ANM-01-017-024}

**Pregunta.** ¿Compacidad es necesaria para uniformidad de una función particular?

**Solución.** No. La identidad en toda $\mathbb R$ es uniforme con $\delta=\varepsilon$, aunque su dominio no sea compacto.

Heine–Cantor es una condición suficiente para toda continua en el compacto. Una función particular puede disponer de una estimación global que funcione en un dominio mayor. La identidad conserva exactamente la distancia de entrada y por eso usa radio $\varepsilon$ en toda la recta. No se invierte la implicación del teorema.

## §17.4 — Medir la oscilación a cada escala

### Microcontrol 025

[]{#MA-MIC-ANM-01-017-025}

[]{#MA-MSOL-ANM-01-017-025}

[]{#MA-SEC-ANM-01-017-004}

**Pregunta.** ¿Qué garantiza que el módulo global definido sea real finito?

**Solución.** En el marco usado, $D$ no vacío y $|f|\le B$: las diferencias contienen cero y están acotadas por $2B$.

Para cualquier escala no negativa, un par diagonal aporta error cero si el dominio no es vacío. La triangular y la barrera de valores dan error a lo sumo $2B$ para todos los pares. No vacuidad y acotación permiten aplicar completitud al conjunto de errores. En otros ejemplos una estimación directa por escala puede reemplazar la acotación global de valores.

### Microcontrol 026

[]{#MA-MIC-ANM-01-017-026}

[]{#MA-MSOL-ANM-01-017-026}

**Pregunta.** ¿Qué significa $\omega_f(t)$?

**Solución.** El supremo de todas las diferencias de salida de pares del dominio a distancia a lo sumo $t$. No exige que un par alcance ese supremo.

La condición de distancia admite también parejas exactamente a escala $t$. El módulo domina a todos sus errores mediante una cota óptima, aunque ningún par produzca el mayor error. Para interpretarlo como máximo haría falta demostrar que se alcanza. Su definición como supremo evita asumir esa pertenencia.

### Microcontrol 027

[]{#MA-MIC-ANM-01-017-027}

[]{#MA-MSOL-ANM-01-017-027}

**Pregunta.** ¿Por qué $\omega_f(0)=0$?

**Solución.** La distancia cero implica $x=y$, así todas las diferencias del conjunto son cero. Para dominio vacío se fijó módulo cero por convención.

Si $|x-y|\le0$, la no negatividad de la distancia obliga a igualdad de entradas. La diferencia de salidas es entonces cero. En un dominio no vacío el conjunto de errores es exactamente $\{0\}$ y su supremo vale cero. En el vacío se usa la convención declarada porque el conjunto vacío no tiene supremo real.

### Microcontrol 028

[]{#MA-MIC-ANM-01-017-028}

[]{#MA-MSOL-ANM-01-017-028}

**Pregunta.** ¿Por qué el módulo no decrece?

**Solución.** Al aumentar $t$ se admiten todos los pares anteriores y quizá otros; el supremo de un conjunto contenido no supera el del mayor.

El conjunto de parejas de escala menor está incluido en el de escala mayor. Por ello todo error anterior también aparece entre los nuevos errores, y la menor cota superior del primero no supera la del segundo. La conclusión no dice que el crecimiento sea estricto: puede haber escalas en que no se agreguen errores mayores.

### Microcontrol 029

[]{#MA-MIC-ANM-01-017-029}

[]{#MA-MSOL-ANM-01-017-029}

**Pregunta.** ¿Por qué una cota estricta de todos los valores no da supremo estrictamente menor?

**Solución.** Por ejemplo, todos los valores de $[0,1)$ son menores que uno pero su supremo es uno. Se usa presupuesto $\varepsilon/2$.

El supremo puede estar en la frontera que ningún valor alcanza. De controles puntuales menores que $\varepsilon$ sólo deducimos una cota superior no estricta $\omega\le\varepsilon$. Pedir la mitad del presupuesto permite después concluir $\omega\le\varepsilon/2<\varepsilon$. Esta reserva recupera la estrictitud sin atribuir al supremo un par maximizador.

### Microcontrol 030

[]{#MA-MIC-ANM-01-017-030}

[]{#MA-MSOL-ANM-01-017-030}

**Pregunta.** ¿Cómo da uniformidad el límite del módulo en cero?

**Solución.** Se toma una escala $t>0$ con $\omega_f(t)<\varepsilon$ y se fija $\delta=t$; los pares con distancia menor que ella tienen error a lo sumo ese módulo.

Se fija primero una escala positiva en la que el módulo esté por debajo del desafío. Después todo par a distancia menor que ella también cumple la condición no estricta usada para definir los errores del módulo. Su error está dominado por éste y queda por debajo de la tolerancia. La escala no depende del par considerado.

### Microcontrol 031

[]{#MA-MIC-ANM-01-017-031}

[]{#MA-MSOL-ANM-01-017-031}

**Pregunta.** ¿Qué par alcanza el módulo de $x^2$ en $[0,1]$ para $0\le t\le1$?

**Solución.** El par $1,1-t$ tiene distancia $t$ y diferencia $2t-t^2$, igual a la cota probada para todos los pares.

La primera entrada es el extremo superior uno y la segunda retrocede exactamente $t$, permaneciendo en $[0,1]$. Al restar sus cuadrados se obtiene $1-(1-t)^2=2t-t^2$. La cota global y este par que la alcanza prueban igualdad del módulo, no sólo una estimación superior. Para escalas mayores que uno, el par de extremos alcanza el valor máximo uno.

### Microcontrol 032

[]{#MA-MIC-ANM-01-017-032}

[]{#MA-MSOL-ANM-01-017-032}

**Pregunta.** ¿Uniformidad obliga a valores acotados en todo dominio?

**Solución.** No: la identidad uniforme en $\mathbb R$ es no acotada, aunque sí tiene módulo finito $\omega(t)=t$.

La uniformidad limita cuánto cambia la salida entre entradas próximas, no qué tan grande puede ser una salida individual. La identidad en la recta tiene valores arbitrariamente grandes, pero cambios iguales a las distancias de entrada. Su módulo es finito a cada escala aunque no exista una barrera global de valores. Son obligaciones diferentes.

## §17.5 — Transportar tolerancias por operaciones

### Microcontrol 033

[]{#MA-MIC-ANM-01-017-033}

[]{#MA-MSOL-ANM-01-017-033}

[]{#MA-SEC-ANM-01-017-005}

**Pregunta.** ¿Cómo se combinan dos radios para una suma?

**Solución.** Se pide error $\varepsilon/2$ a cada sumando y se toma el mínimo de los dos radios positivos.

La distancia menor que el mínimo cumple simultáneamente los dos controles uniformes. La triangular de diferencias de la suma añade sus dos errores, cada uno menor que medio desafío. Los radios se diseñan antes del par y por ello su mínimo también es uniforme. El mismo procedimiento sirve para diferencias con un cambio de signo.

### Microcontrol 034

[]{#MA-MIC-ANM-01-017-034}

[]{#MA-MSOL-ANM-01-017-034}

**Pregunta.** ¿Qué hipótesis suficientes se añaden para productos?

**Solución.** Cotas globales $M_f,M_g$ de los valores; controlan los factores que multiplican las diferencias en la identidad de producto.

En $f(x)g(x)-f(y)g(y)$ aparece una diferencia pequeña multiplicada por un valor de la otra función. Las cotas globales impiden que ese factor amplifique el error sin límite al cambiar las entradas. La regla ofrece condiciones suficientes, no necesarias para cada producto. En dominios compactos, continuidad de los factores puede proporcionar esas cotas mediante Weierstrass.

### Microcontrol 035

[]{#MA-MIC-ANM-01-017-035}

[]{#MA-MSOL-ANM-01-017-035}

**Pregunta.** ¿Qué producto refuta conservación automática en dominios arbitrarios?

**Solución.** La identidad por sí misma en $\mathbb R$: ambos factores son uniformes, pero su producto $x^2$ no lo es.

Ambas identidades conservan distancias y por ello tienen radios uniformes. Pero el producto compara cuadrados, cuyo factor $|x+y|$ puede hacerse arbitrariamente grande. Los pares próximos que escapan producen errores de cuadrado separados de cero. Así el ejemplo conserva uniformidad de los factores mientras refuta una regla general de producto sin más control.

### Microcontrol 036

[]{#MA-MIC-ANM-01-017-036}

[]{#MA-MSOL-ANM-01-017-036}

**Pregunta.** ¿Qué dato positivo controla un recíproco?

**Solución.** Un margen global $|g(x)|\ge m>0$; entonces la diferencia de recíprocos es a lo sumo la diferencia de $g$ dividida por $m^2$.

La identidad exacta es $|1/g(x)-1/g(y)|=|g(x)-g(y)|/(|g(x)||g(y)|)$. Cada factor del denominador es al menos $m$, así el producto es al menos $m^2>0$. Pedir a $g$ error menor que $m^2\varepsilon$ permite usar su radio uniforme para el recíproco. El margen también asegura que todas sus evaluaciones estén definidas.

### Microcontrol 037

[]{#MA-MIC-ANM-01-017-037}

[]{#MA-MSOL-ANM-01-017-037}

**Pregunta.** ¿Ausencia de ceros basta para ese margen?

**Solución.** No. $g(x)=x$ en $(0,1]$ nunca vale cero pero tiene valores positivos arbitrariamente pequeños.

No anularse es una afirmación separada para cada entrada y no asegura una distancia común de las salidas a cero. En la identidad positiva, los recíprocos de naturales infringen cualquier barrera positiva propuesta. Al invertir la función esas pequeñas salidas amplifican cambios de entrada. Compacidad y continuidad aportarían un margen, pero aquí el dominio omite su frontera cero.

### Microcontrol 038

[]{#MA-MIC-ANM-01-017-038}

[]{#MA-MSOL-ANM-01-017-038}

**Pregunta.** ¿Qué tolerancia se elige primero en una composición?

**Solución.** La tolerancia intermedia $\eta$ que produce error final $\varepsilon$ en la función exterior; después el radio de la interior que produce error menor que $\eta$.

La función exterior traduce primero el desafío final a una precisión de entradas intermedias. La interior traduce después esa precisión a una distancia del dominio inicial. Al verificar un par, se recorren esas traducciones en el orden de evaluación de la composición. Diseñar la escala en orden inverso al cálculo garantiza el presupuesto final.

### Microcontrol 039

[]{#MA-MIC-ANM-01-017-039}

[]{#MA-MSOL-ANM-01-017-039}

**Pregunta.** ¿Qué dominio basta controlar uniformemente para la función exterior?

**Solución.** La imagen $f[D]$, porque sólo esos valores se usan al evaluar $g\circ f$.

Toda evaluación intermedia pertenece a la imagen declarada, así sólo se comparan pares de esa imagen al aplicar la exterior. Su comportamiento fuera de ella no interviene en el error compuesto. Hay que conservar pertenencia al dominio exterior para definir la composición. La restricción uniforme a la imagen basta para las tolerancias que se utilizan.

### Microcontrol 040

[]{#MA-MIC-ANM-01-017-040}

[]{#MA-MSOL-ANM-01-017-040}

**Pregunta.** ¿Por qué una inversa compacta continua es también uniforme?

**Solución.** La imagen $H$ es compacta por C16 y la inversa es continua allí; Heine–Cantor se aplica con dominio $H$.

Primero la compacidad del dominio directo hace compacta su imagen por continuidad. Después la inversa continua tiene esa imagen como dominio y cumple las premisas de Heine–Cantor. La uniformidad obtenida compara pares de salidas intermedias antes de conocerlos. No se necesita que el dominio o la imagen sean intervalos.

## §17.6 — Pares próximos y rutas dadas

### Microcontrol 041

[]{#MA-MIC-ANM-01-017-041}

[]{#MA-MSOL-ANM-01-017-041}

[]{#MA-SEC-ANM-01-017-006}

**Pregunta.** ¿Deben converger las dos rutas próximas de R6?

**Solución.** No. Sólo se exige que su distancia mutua tienda a cero; pueden escaparse al infinito.

Las rutas pueden alejarse conjuntamente sin converger a un centro real. La condición uniforme controla sus parejas por la distancia mutua, independientemente de su posición. Para cada precisión, esa distancia eventualmente entra en el radio común. Eso basta para hacer tender a cero la diferencia de salidas.

### Microcontrol 042

[]{#MA-MIC-ANM-01-017-042}

[]{#MA-MSOL-ANM-01-017-042}

**Pregunta.** ¿Dónde se gasta selección en la recíproca general?

**Solución.** Primero al escoger $x_n\in A_n$ y después $y_n\in B_n$. Ambas familias reales no vacías se seleccionan bajo la premisa local CC(R).

La negación proporciona parejas infractoras a cada escala, pero no todavía dos funciones de términos. Se selecciona primero una entrada que admita compañero y después un compañero de esa entrada ya fijada. Las dos selecciones son de familias de subconjuntos reales no vacíos. La premisa local CC(R) justifica ambas, mientras la dirección directa trabaja con rutas ya dadas.

### Microcontrol 043

[]{#MA-MIC-ANM-01-017-043}

[]{#MA-MSOL-ANM-01-017-043}

**Pregunta.** ¿Qué reemplaza CC(R) con una enumeración dada?

**Solución.** El menor índice de la primera entrada que tiene un compañero malo, y luego el menor índice de ese compañero. La sobreyección dada garantiza existencia.

La sobreyección representa todas las posibles entradas y compañeros. Para cada escala, el conjunto de índices de primeras entradas admisibles es no vacío y tiene mínimo. Fijado ese índice, se toma el mínimo de los índices de compañeros. Las reglas únicas determinan ambos términos y evitan elección arbitraria, sin suponer que los índices fabricados sean crecientes.

### Microcontrol 044

[]{#MA-MIC-ANM-01-017-044}

[]{#MA-MSOL-ANM-01-017-044}

**Pregunta.** ¿Qué diferencia de salida tienen los pares del cuadrado que escapan?

**Solución.** Para $x_n=n+1$, $y_n=x_n+1/(n+1)$, es $2+1/(n+1)^2\ge2$, aunque la distancia de entrada tiende a cero.

La diferencia se calcula como $2x_nh_n+h_n^2$ con $h_n=1/(n+1)$. El producto $x_nh_n$ vale uno, de modo que el error queda al menos en dos aunque $h_n$ tienda a cero. Este cálculo exhibe cómo una distancia pequeña puede amplificarse cuando las entradas crecen. Ambas fórmulas están definidas desde el índice cero.

### Microcontrol 045

[]{#MA-MIC-ANM-01-017-045}

[]{#MA-MSOL-ANM-01-017-045}

**Pregunta.** ¿Por qué una uniforme preserva una ruta de Cauchy?

**Solución.** El radio uniforme para $\varepsilon$ se inserta en la condición de Cauchy de entrada, y desde un mismo índice controla todos los pares de términos de salida.

La condición de Cauchy controla simultáneamente todos los pares tardíos de una ruta, no sólo términos consecutivos. El radio uniforme entrega una única precisión de entrada que esa condición puede satisfacer con un corte. Después todos los pares de salidas tardías cumplen el desafío. No es necesario que el límite de la ruta pertenezca al dominio.

### Microcontrol 046

[]{#MA-MIC-ANM-01-017-046}

[]{#MA-MSOL-ANM-01-017-046}

**Pregunta.** ¿Esa preservación caracteriza uniformidad en toda $\mathbb R$?

**Solución.** No. El cuadrado preserva rutas de Cauchy porque cada una está acotada y allí tiene constante Lipschitz, pero no es uniforme en toda la recta.

Cada ruta de Cauchy particular tiene una barrera de valores y el cuadrado posee allí una constante lineal de control. Esa barrera puede cambiar al cambiar de ruta. Preservar cada ruta por separado no produce una escala para todos los pares de la recta. Los pares que escapan refutan precisamente esa conclusión global adicional.

### Microcontrol 047

[]{#MA-MIC-ANM-01-017-047}

[]{#MA-MSOL-ANM-01-017-047}

**Pregunta.** ¿Por qué las diferencias de salida separadas refutan uniformidad sin recíproca?

**Solución.** Basta la implicación directa R6: si la función fuera uniforme, esos pares dados tendrían diferencias tendentes a cero, contradicción.

Las rutas explícitas ya constituyen datos de la implicación directa. Si su distancia mutua tiende a cero y la diferencia de salidas mantiene una tolerancia positiva, la consecuencia necesaria de uniformidad falla. No hay que seleccionar parejas infractoras de una familia abstracta. Por ello este modo de refutar uniformidad no depende de la recíproca bajo CC(R).

### Microcontrol 048

[]{#MA-MIC-ANM-01-017-048}

[]{#MA-MSOL-ANM-01-017-048}

**Pregunta.** ¿Qué valor evita el problema del índice inicial cero?

**Solución.** Las escalas son $1/(n+1)$ y los pares recíprocos usan $n+2,n+3$; no se divide por $n$ cuando $n=0$.

Al empezar en $n=0$, las expresiones $n+1$, $n+2$ y $n+3$ son todas positivas. Esto garantiza definición de las escalas y pertenencia de las entradas recíprocas al dominio desde el primer término. Una fórmula con $1/n$ tendría que cambiar su índice inicial o repararse antes de usarla como sucesión del capítulo.

## §17.7 — Completar el dominio sin seleccionar aproximantes

### Microcontrol 049

[]{#MA-MIC-ANM-01-017-049}

[]{#MA-MSOL-ANM-01-017-049}

[]{#MA-SEC-ANM-01-017-007}

**Pregunta.** ¿Qué garantiza que $E_{p,r}$ no sea vacía?

**Solución.** $p\in\overline D$: toda bola positiva centrada en $p$ toca $D$, por lo que su imagen tiene un valor.

La imagen local reúne salidas de entradas de $D$ dentro de una bola de radio positivo. La adherencia de $p$ garantiza al menos una entrada allí, aunque $p$ mismo esté fuera de $D$. Por eso el conjunto de salidas no es vacío. Esta premisa debe comprobarse antes de usar sus ínfimos y supremos reales.

### Microcontrol 050

[]{#MA-MIC-ANM-01-017-050}

[]{#MA-MSOL-ANM-01-017-050}

**Pregunta.** ¿Cómo se acotan las imágenes locales sin elegir aproximantes globales?

**Solución.** Para un $p$ fijado se usa una entrada $a$ en la bola inicial; uniformidad con error uno acota todos sus valores por $f(a)\pm1$. No se forma una familia $a_p$.

La primera bola se elige tan pequeña que dos de sus entradas estén dentro del radio uniforme para error uno. Fijar una de ellas como referencia acota las salidas de todas las demás. Las bolas menores heredan esa barrera y siguen siendo no vacías por adherencia. El testigo de referencia sólo acredita acotación para el punto examinado y no define la extensión.

### Microcontrol 051

[]{#MA-MIC-ANM-01-017-051}

[]{#MA-MSOL-ANM-01-017-051}

**Pregunta.** ¿Qué corte define el valor extendido?

**Solución.** $F(p)=\sup\{L_{p,r}:0<r\le r_0\}$, con $L_{p,r}$ el ínfimo de la imagen local no vacía y acotada.

Los ínfimos locales existen por no vacuidad y acotación. Su colección también es no vacía y está acotada por una cota superior local inicial. El supremo de esa colección define un real único mediante fórmula. La construcción no pide elegir una entrada aproximante a cada radio ni una ruta para cada punto de frontera.

### Microcontrol 052

[]{#MA-MIC-ANM-01-017-052}

[]{#MA-MSOL-ANM-01-017-052}

**Pregunta.** ¿Por qué ese corte no supera ningún $U_{p,r}$?

**Solución.** Para toda otra escala $s$, la imagen de la bola de radio $\min(r,s)$ es no vacía y está en ambas imágenes; así $L_{p,s}\le U_{p,r}$ y ese supremo acota todo el corte.

La escala común $\min(r,s)$ tiene una imagen no vacía contenida en las dos imágenes mayores. Una de sus salidas está por encima del ínfimo a escala $s$ y por debajo del supremo a escala $r$. Así cada ínfimo que participa en el corte está dominado por $U_{p,r}$. La misma cota domina entonces al supremo de todos ellos.

### Microcontrol 053

[]{#MA-MIC-ANM-01-017-053}

[]{#MA-MSOL-ANM-01-017-053}

**Pregunta.** ¿Qué hace único al valor entre todos los intervalos?

**Solución.** Sus anchuras pueden ser menores que cualquier distancia positiva; dos valores distintos no cabrían en uno de esos intervalos suficientemente estrechos.

Si dos candidatos distaran $d>0$, se pediría una escala con anchura menor que $d$. Ambos deben quedar entre los mismos extremos locales, así su distancia no puede superar esa anchura. La contradicción fuerza igualdad. El argumento no necesita que los ínfimos o supremos locales sean valores alcanzados.

### Microcontrol 054

[]{#MA-MIC-ANM-01-017-054}

[]{#MA-MSOL-ANM-01-017-054}

**Pregunta.** ¿Por qué la extensión coincide con $f$ en $D$?

**Solución.** Si $p\in D$, $f(p)$ pertenece a toda imagen local y queda entre sus ínfimos/supremos. La unicidad identifica ese valor con $F(p)$.

El centro $p$ pertenece a todas sus bolas positivas cuando ya está en $D$. Su salida está por ello en todas las imágenes locales y cumple sus cotas inferior y superior. El corte construido cumple las mismas cotas y la anchura decreciente fuerza igualdad de ambos reales. Así se prueba extensión sin modificar ningún valor original.

### Microcontrol 055

[]{#MA-MIC-ANM-01-017-055}

[]{#MA-MSOL-ANM-01-017-055}

**Pregunta.** ¿Qué radio uniforme sobre el cierre se obtiene en la prueba?

**Solución.** Para un radio $\delta$ que controla $f$ con error $\varepsilon/3$, sirve $\Delta=\delta/3$; vecindades pequeñas de ambos puntos mantienen todos los pares cruzados dentro de $\delta$.

La distancia entre entradas de dos vecindades se acota sumando sus distancias a los centros y la distancia entre éstos. El radio $\Delta$ y los radios locales menores dejan esa suma por debajo de $\delta$. El control cruzado de salidas pasa a ínfimos y supremos con desigualdades no estrictas. El presupuesto $\varepsilon/3$ deja margen para recuperar error final estricto.

### Microcontrol 056

[]{#MA-MIC-ANM-01-017-056}

[]{#MA-MSOL-ANM-01-017-056}

**Pregunta.** ¿Se necesita una sucesión aproximante por punto de frontera?

**Solución.** No. Se usan todas las imágenes locales, supremos/ínfimos y un valor único por fórmula; no se seleccionan rutas.

La definición utiliza todos los valores locales disponibles y cotas reales, de modo que no requiere una entrada preferida para cada escala. La unicidad identifica el real que ocupa todas las bandas cada vez más estrechas. Las existencias puntuales usadas para no vacuidad o acotación no se reúnen como familias de elecciones. Así se separa este procedimiento de una construcción por rutas seleccionadas.

## §17.8 — Datos finitos y aproximaciones poligonales

### Microcontrol 057

[]{#MA-MIC-ANM-01-017-057}

[]{#MA-MSOL-ANM-01-017-057}

[]{#MA-SEC-ANM-01-017-008}

**Pregunta.** ¿Qué condición cumple el paso de la malla?

**Solución.** $h=(b-a)/n<\delta$, donde $\delta$ es el radio uniforme para el presupuesto $\varepsilon/2$ y $n\ge1$.

Como $a<b$, la longitud es positiva y arquimedianidad permite un entero suficientemente grande para que su división sea menor que el radio. La estrictitud $h<\delta$ controla también puntos a distancia exactamente $h$ de un nodo. El entero es al menos uno, por lo que hay celdas y la fórmula no divide por cero.

### Microcontrol 058

[]{#MA-MIC-ANM-01-017-058}

[]{#MA-MSOL-ANM-01-017-058}

**Pregunta.** ¿Por qué coinciden las fórmulas de dos celdas en un nodo?

**Solución.** Una da peso uno al extremo derecho y la otra peso uno al extremo izquierdo; ambas dan el valor de $f$ en el nodo común.

En el nodo compartido, la fórmula de la celda anterior evalúa su extremo derecho y la siguiente su extremo izquierdo. Los pesos nulos eliminan el otro valor en cada caso. Ambas asignaciones coinciden exactamente con la misma muestra. Esto acredita que el pegado define una única función antes de estudiar su continuidad.

### Microcontrol 059

[]{#MA-MIC-ANM-01-017-059}

[]{#MA-MSOL-ANM-01-017-059}

**Pregunta.** ¿Qué mantiene a $\theta$ entre cero y uno?

**Solución.** $x\in[t_j,t_{j+1}]$ y $h>0$, por lo que $0\le x-t_j\le h$ y $\theta=(x-t_j)/h\in[0,1]$.

La pertenencia a la celda garantiza $0\le x-t_j\le h$. Dividir por la longitud positiva conserva las desigualdades y produce pesos $\theta$ y $1-\theta$ no negativos de suma uno. Esa condición permite acotar el error de interpolación como combinación de dos errores de muestra. Fuera de la celda no podríamos afirmar esos signos.

### Microcontrol 060

[]{#MA-MIC-ANM-01-017-060}

[]{#MA-MSOL-ANM-01-017-060}

**Pregunta.** ¿Cómo se controla el error entre las muestras?

**Solución.** Ambos extremos distan a lo sumo $h<\delta$ de $x$; sus errores son menores que $\varepsilon/2$ y la combinación convexa mantiene esa cota.

La expresión $P(x)-f(x)$ es la combinación de las diferencias entre cada muestra y $f(x)$. La triangular introduce los dos pesos no negativos, que suman uno. Como ambos errores están bajo el mismo presupuesto, su combinación también lo está. En los nodos un peso vale cero y el otro uno; el argumento conserva esos casos sin excluirlos.

### Microcontrol 061

[]{#MA-MIC-ANM-01-017-061}

[]{#MA-MSOL-ANM-01-017-061}

**Pregunta.** ¿Por qué el pegado poligonal es continuo?

**Solución.** Cada rama afín lo es, sus valores coinciden en nodos y C14 permite el pegado finito sobre las celdas cerradas relativas.

Cada celda es cerrada relativa al segmento y la lista es finita. Las ramas afines son continuas y sus valores coinciden en las intersecciones, los nodos. Estas son las hipótesis del pegado finito de C14. Una lista de fórmulas afines sin el acuerdo en nodos no definiría necesariamente una poligonal continua.

### Microcontrol 062

[]{#MA-MIC-ANM-01-017-062}

[]{#MA-MSOL-ANM-01-017-062}

**Pregunta.** ¿Cuál es el error máximo del cuadrado con cuatro celdas iguales?

**Solución.** $h=1/4$, por lo que $h^2/4=1/64$, alcanzado en los medios de cada celda.

En una celda el error es $\theta(1-\theta)h^2$. La identidad $\theta(1-\theta)=1/4-(\theta-1/2)^2$ da su máximo $h^2/4$ y localiza la igualdad en el medio. Con cuatro celdas hay cuatro medios, y todos producen el mismo error $1/64$. Los nodos tienen error cero.

### Microcontrol 063

[]{#MA-MIC-ANM-01-017-063}

[]{#MA-MSOL-ANM-01-017-063}

**Pregunta.** ¿Por qué muestras finitas sin escala no dan error certificado?

**Solución.** Entre dos nodos se puede insertar un pico triangular continuo de altura arbitraria que siga valiendo cero en todos los nodos.

Las muestras determinan valores sólo en un conjunto finito de argumentos. Una función continua puede coincidir en todos ellos y variar mucho dentro de una celda. El pico triangular conserva continuidad y permite fijar una altura arbitraria sin alterar los datos de nodos. Para certificar error entre muestras hace falta una escala de control de la función, no sólo sus valores finitos.

### Microcontrol 064

[]{#MA-MIC-ANM-01-017-064}

[]{#MA-MSOL-ANM-01-017-064}

**Pregunta.** ¿Qué aproximante sirve en un segmento degenerado?

**Solución.** La constante con valor $f(a)$ en $[a,a]$ tiene error cero; no se divide por una longitud de malla cero.

Si $a=b$, hay una sola entrada y la interpolación puede definirse directamente con su valor. La diferencia respecto de $f$ es cero en todo el dominio. La fórmula de pesos con longitud $h=0$ no está definida y no debe utilizarse. Separar este caso conserva la afirmación de aproximación sin introducir una división inválida.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html)
