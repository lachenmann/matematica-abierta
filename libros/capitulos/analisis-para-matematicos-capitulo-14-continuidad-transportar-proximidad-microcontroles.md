---
content-id: MA-BCH-0261
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-014-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 14
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C14_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §14.1 — Hacer del valor central el destino

### Microcontrol 001

[]{#MA-MIC-ANM-01-014-001}

[]{#MA-MSOL-ANM-01-014-001}

[]{#MA-SEC-ANM-01-014-001}

**Pregunta.** ¿Por qué debe pertenecer $a$ a $D$ para preguntar por continuidad?

**Solución.** Porque el destino es $f(a)$ y esa evaluación sólo está definida para $a\in D$.

En continuidad comparamos cada salida cercana con la salida central de la misma función. Si $a$ estuviera fuera del dominio, no habría valor $f(a)$ con el que comparar. El límite perforado puede estudiarse sin esa evaluación, pero continuidad exige que exista. La pertenencia al dominio es una condición sobre el objeto, anterior a elegir tolerancias y radios.

### Microcontrol 002

[]{#MA-MIC-ANM-01-014-002}

[]{#MA-MSOL-ANM-01-014-002}

**Pregunta.** ¿Se excluye $x=a$ en el contrato de continuidad?

**Solución.** No. El centro está permitido y tiene error $|f(a)-f(a)|=0$.

Para $x=a$ la distancia de entrada es cero y pertenece a cualquier bola de radio positivo. El error de salida también es cero y satisface cualquier tolerancia positiva. Por eso incluir el centro no crea una dificultad en una prueba correcta. Sí obliga a centrar el control en el valor real $f(a)$, que no puede sustituirse por otro destino independiente.

### Microcontrol 003

[]{#MA-MIC-ANM-01-014-003}

[]{#MA-MSOL-ANM-01-014-003}

**Pregunta.** ¿Necesita $a$ ser interior del dominio?

**Solución.** No. La continuidad es relativa a las entradas de $D$; puede estudiarse en extremos y puntos aislados.

Las entradas consideradas son $x\in D$ con $|x-a|<\delta$. No se exige que la bola completa de la recta esté en $D$. En un extremo sólo se controlan las entradas disponibles de un lado; en un punto aislado puede quedar sólo el centro. La continuidad usa la proximidad dentro del dominio declarado, no la disponibilidad de entradas en todas las direcciones.

### Microcontrol 004

[]{#MA-MIC-ANM-01-014-004}

[]{#MA-MSOL-ANM-01-014-004}

**Pregunta.** ¿En qué se centra la bola de salida?

**Solución.** En el valor efectivo $f(a)$, no en un candidato independiente.

El desafío pide $|f(x)-f(a)|<\varepsilon$. La bola de salida se construye alrededor de esa evaluación fija. Si el límite perforado existe pero es distinto, podremos controlar las salidas hacia otro número y aun así fallará continuidad. Esta elección del centro de salida es lo que vincula el comportamiento próximo con el valor asignado en el punto.

### Microcontrol 005

[]{#MA-MIC-ANM-01-014-005}

[]{#MA-MSOL-ANM-01-014-005}

**Pregunta.** ¿Cuál es el orden global de cuantificadores?

**Solución.** $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$. El radio puede depender de $a$ y de $\varepsilon$.

Primero fijamos un centro y una precisión; después elegimos una ventana que responda a ambos y verificamos todas sus entradas. La expresión no promete una ventana común para centros distintos. Por ejemplo, el certificado del cuadrado contiene $|a|$ en su denominador. Exigir que el radio sólo dependa de la precisión cambia el orden de cuantificadores y añade otra propiedad.

### Microcontrol 006

[]{#MA-MIC-ANM-01-014-006}

[]{#MA-MSOL-ANM-01-014-006}

**Pregunta.** ¿Qué hipótesis legitima comparar continuidad con el límite perforado?

**Solución.** $a\in D\cap D^{\prime}$. Pertenencia legitima $f(a)$; acumulación legitima el límite de C13.

La continuidad necesita $a\in D$ para usar $f(a)$, mientras el límite de C13 necesita acumulación para evitar una condición perforada vacía. Cuando se cumplen ambas, continuidad equivale a que el límite perforado sea exactamente $f(a)$. La vuelta añade al control perforado el caso central, cuyo error es cero. En puntos aislados se estudia continuidad directamente, sin invocar esa equivalencia.

### Microcontrol 007

[]{#MA-MIC-ANM-01-014-007}

[]{#MA-MSOL-ANM-01-014-007}

**Pregunta.** ¿La existencia de un límite finito basta para continuidad?

**Solución.** No. En un punto de acumulación del dominio debe además coincidir con $f(a)$.

Tomemos $f(x)=0$ para $x\ne0$ y $f(0)=1$. Sus salidas perforadas tienen límite cero, pero su distancia al valor central uno es siempre uno. La tolerancia $1/2$ falla con una entrada no nula dentro de cualquier radio. El ejemplo muestra que existencia del destino y coincidencia con la evaluación central son dos obligaciones distintas para continuidad.

### Microcontrol 008

[]{#MA-MIC-ANM-01-014-008}

[]{#MA-MSOL-ANM-01-014-008}

**Pregunta.** ¿Qué inclusión de conjuntos expresa continuidad?

**Solución.** Para cada $\varepsilon>0$ hay $\delta>0$ con $f[D\cap B(a,\delta)]\subseteq B(f(a),\varepsilon)$, equivalentemente $D\cap B(a,\delta)\subseteq f^{-1}[B(f(a),\varepsilon)]$.

La bola relativa $D\cap B(a,\delta)$ reúne todas las entradas admitidas, incluido el centro. La inclusión de imágenes dice que cada una produce una salida en la bola requerida. La formulación por preimagen expresa la misma selección desde las entradas. No supone inversa funcional ni inyectividad; sólo utiliza la definición de imagen y la condición de pertenencia de la salida.

## §14.2 — El dominio y la reparación de un hueco

### Microcontrol 009

[]{#MA-MIC-ANM-01-014-009}

[]{#MA-MSOL-ANM-01-014-009}

[]{#MA-SEC-ANM-01-014-002}

**Pregunta.** ¿Qué radio sirve en un punto aislado?

**Solución.** Uno positivo $r$ con $D\cap B(a,r)=\{a\}$. Sirve para toda tolerancia porque la única entrada produce error cero.

El aislamiento proporciona una escala donde no hay otra entrada del dominio. En esa ventana, evaluar cualquier punto permitido equivale a evaluar el centro y el error es cero. El radio no necesita adaptarse a la precisión porque no hay separaciones de salida que controlar. Así cualquier función es continua en un punto aislado de su dominio, cualquiera que sea su valor allí.

### Microcontrol 010

[]{#MA-MIC-ANM-01-014-010}

[]{#MA-MSOL-ANM-01-014-010}

**Pregunta.** ¿Asignamos un límite perforado en ese punto aislado?

**Solución.** No bajo la convención de C13. La continuidad se prueba directamente sin inventar un límite vacuo.

En el límite perforado se elimina el centro, y la ventana aislada queda vacía. La fórmula permitiría cualquier candidato sin distinguir un destino. La convención de C13 evita asignar un límite así. En continuidad el centro permanece y su salida proporciona el destino definido, de modo que la prueba es válida. No hay contradicción entre continuidad en ese punto y ausencia de un límite perforado declarado.

### Microcontrol 011

[]{#MA-MIC-ANM-01-014-011}

[]{#MA-MSOL-ANM-01-014-011}

**Pregunta.** ¿La restricción a $A\subseteq D$ exige acumulación para conservar continuidad?

**Solución.** No. Basta $a\in A$; el mismo radio controla las entradas del subconjunto y conserva el valor central.

Si $a\in A$, la restricción conserva $f(a)$. Además, cada entrada de $A$ dentro de una ventana pertenece también a $D$, por lo que el radio original controla su error. Eliminar entradas nunca invalida ese control. A diferencia de los límites perforados, no necesitamos acumulación en $A$: si el punto se vuelve aislado, el caso central sigue definiendo una prueba de continuidad.

### Microcontrol 012

[]{#MA-MIC-ANM-01-014-012}

[]{#MA-MSOL-ANM-01-014-012}

**Pregunta.** ¿Qué debe incluir la coincidencia local de dos funciones para preservar continuidad?

**Solución.** Debe incluir el centro: $f=g$ en $D\cap B(a,r)$. Así sus valores centrales y sus errores coinciden.

La igualdad local debe proporcionar tanto igualdad de salidas próximas como igualdad de destinos centrales. Si sólo coincide fuera del centro, los errores pueden medirse desde valores distintos y la continuidad no se transfiere. Incluyendo el centro, $f(a)=g(a)$; el mínimo del radio de coincidencia y el radio de continuidad permite reemplazar una función por la otra en toda la estimación.

### Microcontrol 013

[]{#MA-MIC-ANM-01-014-013}

[]{#MA-MSOL-ANM-01-014-013}

**Pregunta.** ¿Qué valor completa de forma continua un hueco con límite $L$?

**Solución.** El valor $L$. Los puntos originales obedecen el control del límite y el nuevo centro tiene error cero.

Definimos la extensión con valor $L$ en el punto que faltaba. Para las entradas originales de la ventana, el límite da error menor que la tolerancia. Para la entrada añadida, el error respecto de $L$ es cero. Separar ambos casos verifica continuidad en el nuevo punto. La construcción no cambia ninguno de los valores originales y sólo completa el dato central.

### Microcontrol 014

[]{#MA-MIC-ANM-01-014-014}

[]{#MA-MSOL-ANM-01-014-014}

**Pregunta.** ¿Qué resultado garantiza unicidad de esa reparación?

**Solución.** La unicidad del límite de C13, pues el centro que faltaba era punto de acumulación del dominio original.

Si otra extensión fuera continua en el nuevo centro con valor $c$, su límite perforado sería $c$. Las entradas originales coinciden en ambas extensiones y tenían límite $L$. Como el centro acumula esas entradas, la unicidad de C13 obliga a $c=L$. La acumulación es esencial: si se añadiera un punto aislado, distintos valores centrales podrían producir extensiones continuas allí.

### Microcontrol 015

[]{#MA-MIC-ANM-01-014-015}

[]{#MA-MSOL-ANM-01-014-015}

**Pregunta.** ¿Qué hipótesis adicional permite afirmar continuidad de la extensión en todos los puntos?

**Solución.** Que la función original sea continua en todo $D$. Un radio menor que la mitad de la distancia al nuevo punto preserva cada control anterior.

La reparación en el hueco no corrige fallos que ya existieran en otros puntos. Si la original es continua en cada $x\in D$, podemos conservar su control tomando un radio menor que $|x-a|/2$, que evita el nuevo centro $a$. Dentro de esa ventana la extensión coincide con la original. La prueba en el nuevo punto y estas pruebas en todos los anteriores dan continuidad global.

### Microcontrol 016

[]{#MA-MIC-ANM-01-014-016}

[]{#MA-MSOL-ANM-01-014-016}

**Pregunta.** ¿Puede un solo valor reparar dos límites laterales distintos?

**Solución.** No. La continuidad en el punto forzaría que ambos destinos laterales coincidieran con ese mismo valor.

Si los dos lados acumulan y sus destinos son distintos, una extensión continua obligaría a que ambos límites restringidos fueran el mismo valor central. Eso contradice los destinos ya demostrados. Elegir un valor intermedio entre ellos no acerca las dos ramas a ese valor: cada una conserva su propio destino. Un hueco reparable requiere compatibilidad de todas las aproximaciones pertinentes.

## §14.3 — Transportar sucesiones que sí pueden tocar el centro

### Microcontrol 017

[]{#MA-MIC-ANM-01-014-017}

[]{#MA-MSOL-ANM-01-014-017}

[]{#MA-SEC-ANM-01-014-003}

**Pregunta.** ¿Puede una ruta para continuidad alcanzar el centro infinitas veces?

**Solución.** Sí. Puede incluso ser constantemente igual a $a$; esos términos tienen error de salida cero.

La continuidad controla la bola completa, por lo que cada visita al centro cumple automáticamente el error requerido. Una ruta puede alternar entre el centro y entradas no centrales, o permanecer siempre allí. La condición importante es pertenecer al dominio y aproximarse al centro. No se impone la evitación necesaria en el criterio de límites perforados.

### Microcontrol 018

[]{#MA-MIC-ANM-01-014-018}

[]{#MA-MSOL-ANM-01-014-018}

**Pregunta.** ¿Qué flujo de escalas prueba la dirección secuencial directa?

**Solución.** $\varepsilon\to\delta\to N$: continuidad da el radio, convergencia de entradas da la cola y esa cola satisface el error de salida.

Para una precisión de salida, continuidad entrega un radio de entrada. La convergencia de la ruta entrega después un corte a partir del cual todos sus términos están dentro de ese radio. Aplicar el control a cada término tardío da convergencia de las imágenes a $f(a)$. Si algún término es el centro, el mismo argumento vale porque no hay una condición de distancia positiva.

### Microcontrol 019

[]{#MA-MIC-ANM-01-014-019}

[]{#MA-MSOL-ANM-01-014-019}

**Pregunta.** ¿Qué ocurre con una ruta convergente a un punto aislado del dominio?

**Solución.** Es eventualmente constante en ese punto, porque acaba dentro de una bola relativa que sólo lo contiene a él.

Sea $r$ un radio cuya bola relativa contiene únicamente a $a$. La convergencia de $x_n$ entrega una cola dentro de esa bola. Como todos sus términos pertenecen a $D$, necesariamente son $a$. Las imágenes son entonces eventualmente constantes $f(a)$. No hace falta que la función tenga otras propiedades: el aislamiento reduce la aproximación a igualdad eventual.

### Microcontrol 020

[]{#MA-MIC-ANM-01-014-020}

[]{#MA-MSOL-ANM-01-014-020}

**Pregunta.** ¿Por qué un infractor de continuidad nunca es el centro?

**Solución.** Porque la tolerancia fija es positiva y en el centro el error es cero, no puede ser $\ge\varepsilon_0$.

Un infractor debe tener error al menos igual a una tolerancia estrictamente positiva. En $x=a$ el error es cero y no puede cumplir esa desigualdad. Por eso la evitación del centro resulta automáticamente de la condición de infracción. La negación de continuidad no necesita escribirla como una hipótesis adicional, aunque los testigos obtenidos sean siempre no centrales.

### Microcontrol 021

[]{#MA-MIC-ANM-01-014-021}

[]{#MA-MSOL-ANM-01-014-021}

**Pregunta.** ¿Cómo se escribe la negación de continuidad?

**Solución.** $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$: $|x-a|<\delta$ y $|f(x)-f(a)|\ge\varepsilon_0$.

La tolerancia se fija primero y debe fallar en toda ventana. Para cada radio propuesto se encuentra una entrada suficientemente próxima cuyo error respecto de $f(a)$ alcanza o supera esa tolerancia. El punto puede cambiar con el radio, pero la precisión infringida no. Un solo error en una entrada lejana no refuta continuidad, porque podría excluirse reduciendo la ventana.

### Microcontrol 022

[]{#MA-MIC-ANM-01-014-022}

[]{#MA-MSOL-ANM-01-014-022}

**Pregunta.** ¿Qué selector se obtiene de una enumeración sobreyectiva dada?

**Solución.** $k_n=\min\{k:e(k)\in E_n\}$ y $x_n=e(k_n)$. El mínimo es de índices naturales, no de valores reales.

La enumeración dada representa cada entrada de $D$. Como cada conjunto de infractores $E_n$ es no vacío, algún índice lo representa y el conjunto de índices admisibles tiene mínimo. El buen orden natural proporciona una regla única de selección para cada escala. No se toma un mínimo de valores reales, que podría no existir. Las distancias acotadas por las escalas hacen converger la ruta seleccionada al centro.

### Microcontrol 023

[]{#MA-MIC-ANM-01-014-023}

[]{#MA-MSOL-ANM-01-014-023}

**Pregunta.** ¿Qué premisa adicional se declara para la recíproca secuencial en cualquier dominio real?

**Solución.** $\mathrm{CC}(\mathbb R)$, aplicada a la familia de infractores no vacíos. El teorema general permanece condicional.

En un dominio real arbitrario, construir simultáneamente una entrada de cada conjunto no vacío requiere una regla o una hipótesis de selección. El capítulo declara $\mathrm{CC}(\mathbb R)$ para justificar ese paso en la recíproca general. Una vez seleccionada la ruta, la cota de distancias y la persistencia del error dan la contradicción. La dirección directa de continuidad a convergencia de imágenes no utiliza esa premisa.

### Microcontrol 024

[]{#MA-MIC-ANM-01-014-024}

[]{#MA-MSOL-ANM-01-014-024}

**Pregunta.** ¿Necesita selección numerable una refutación mediante una ruta explícita?

**Solución.** No. La ruta ya está construida; la dirección directa y la unicidad secuencial bastan para refutar la continuidad.

Una fórmula para la ruta ya determina todos sus términos, por lo que no se extraen de una familia arbitraria de conjuntos. Si se aproxima a $a$ dentro del dominio y sus imágenes no tienden a $f(a)$, contradice la consecuencia necesaria de continuidad. Esto refuta continuidad sin usar la recíproca secuencial. Mantener separadas ambas direcciones evita introducir hipótesis adicionales innecesarias.

## §14.4 — Preimágenes: de controles locales a conjuntos abiertos

### Microcontrol 025

[]{#MA-MIC-ANM-01-014-025}

[]{#MA-MSOL-ANM-01-014-025}

[]{#MA-SEC-ANM-01-014-004}

**Pregunta.** ¿Qué significa que $A$ sea abierto relativo a $D$?

**Solución.** Que $A=D\cap U$ para algún abierto $U$ de la recta.

Un conjunto puede ser abierto al mirar únicamente las entradas disponibles, aunque no lo sea en la recta completa. La igualdad $A=D\cap U$ expresa que el dominio recorta un abierto real. Los puntos que quedan fuera de $D$ no necesitan pertenecer a $A$. Por eso la apertura relativa siempre debe nombrar su ambiente y no confundirse con apertura absoluta.

### Microcontrol 026

[]{#MA-MIC-ANM-01-014-026}

[]{#MA-MSOL-ANM-01-014-026}

**Pregunta.** ¿Por qué $[0,1/2)$ puede ser abierto en $[0,1]$?

**Solución.** Porque es $[0,1]\cap(-1,1/2)$. La bola sólo debe quedar dentro tras intersectarla con el dominio.

El intervalo abierto $(-1,1/2)$ contiene también números negativos, pero al recortarlo por $[0,1]$ éstos desaparecen y queda $[0,1/2)$. En cero una bola real no cabe en ese conjunto, pero una bola relativa sí: sólo conserva sus entradas no negativas. La frontera del dominio puede estar dentro de un abierto relativo porque la aproximación se mide únicamente entre entradas del dominio.

### Microcontrol 027

[]{#MA-MIC-ANM-01-014-027}

[]{#MA-MSOL-ANM-01-014-027}

**Pregunta.** ¿Qué criterio por bolas caracteriza la apertura relativa?

**Solución.** $\forall a\in A\ \exists r>0:D\cap B(a,r)\subseteq A$.

El criterio pide una ventana relativa interior para cada punto del conjunto. Si $A=D\cap U$ y $U$ es abierto, un radio alrededor de $a\in A$ cabe en $U$ y su recorte cabe en $A$. Para la vuelta se reúnen las bolas que cumplen esa propiedad. La unión es abierta y al intersectarla con $D$ devuelve exactamente $A$, demostrando la representación requerida.

### Microcontrol 028

[]{#MA-MIC-ANM-01-014-028}

[]{#MA-MSOL-ANM-01-014-028}

**Pregunta.** ¿Por qué se unen todas las bolas válidas en vez de elegir una por punto?

**Solución.** La unión sigue siendo abierta y representa exactamente $A$ al intersectarla con $D$, sin necesitar una selección simultánea de radios.

Formamos la unión de todas las bolas centradas en puntos de $A$ cuyos recortes por $D$ quedan en $A$. Cada punto de $A$ dispone de alguna por la hipótesis local y queda cubierto. Cualquier entrada de $D$ cubierta por una de ellas pertenece a $A$. Se obtienen ambas inclusiones sin escoger una bola determinada para cada punto; la unión de todas las válidas evita ese paso de selección simultánea.

### Microcontrol 029

[]{#MA-MIC-ANM-01-014-029}

[]{#MA-MSOL-ANM-01-014-029}

**Pregunta.** ¿La continuidad conserva apertura por imagen o por preimagen?

**Solución.** Por preimagen: todo abierto de salida tiene preimagen abierta relativa al dominio.

Un abierto de salidas contiene una bola alrededor de cada salida que pertenece a él. La continuidad transporta una bola relativa de entradas dentro de esa bola de salidas. Así cada entrada de la preimagen tiene una ventana relativa contenida en la misma preimagen, que por ello es abierta. El argumento va desde una condición de salidas hacia entradas; no afirma que imágenes de abiertos sean abiertas.

### Microcontrol 030

[]{#MA-MIC-ANM-01-014-030}

[]{#MA-MSOL-ANM-01-014-030}

**Pregunta.** ¿Qué abierto de salida recupera el contrato para una tolerancia $\varepsilon$?

**Solución.** $B(f(a),\varepsilon)$. Su preimagen abierta contiene el centro y por ello una bola relativa de entrada.

La bola $B(f(a),\varepsilon)$ contiene la salida central y su preimagen contiene a $a$. Si todas las preimágenes de abiertos son abiertas relativas, ésta contiene una bola relativa alrededor de $a$. Sus entradas producen salidas dentro de la bola de precisión, lo que es exactamente continuidad puntual. Así el criterio topológico recupera el orden de escalas del control mediante radios.

### Microcontrol 031

[]{#MA-MIC-ANM-01-014-031}

[]{#MA-MSOL-ANM-01-014-031}

**Pregunta.** ¿Cuál es la identidad de complementos para preimágenes?

**Solución.** $D\setminus f^{-1}[F]=f^{-1}[\mathbb R\setminus F]$. Para una función con codominio $E$, se usa $E\setminus F$ cuando $F\subseteq E$.

Para una entrada $x\in D$, quedar fuera de la preimagen de $F$ significa que $f(x)$ no pertenece a $F$. Como la salida pertenece al codominio, equivale a estar en su complemento relativo. Por eso el complemento de entradas se toma en $D$ y el de salidas en el codominio. La identidad permite pasar del criterio de abiertos al de cerrados sin cambiar ambientes.

### Microcontrol 032

[]{#MA-MIC-ANM-01-014-032}

[]{#MA-MSOL-ANM-01-014-032}

**Pregunta.** ¿En qué ambiente es cerrado el conjunto de ceros de una función continua en $D$?

**Solución.** Es cerrado relativo a $D$. No tiene por qué ser cerrado en toda la recta si $D$ no lo es.

El conjunto de ceros es $f^{-1}[\{0\}]$, preimagen de un cerrado real. Continuidad lo hace cerrado dentro de $D$. Si la función cero tiene dominio $(0,1)$, su conjunto de ceros es todo ese intervalo, cerrado relativo a sí mismo pero no cerrado en la recta. La conclusión topológica conserva el ambiente del dominio y no incorpora automáticamente puntos que faltaban en él.

## §14.5 — Operar y componer sin perder el dominio

### Microcontrol 033

[]{#MA-MIC-ANM-01-014-033}

[]{#MA-MSOL-ANM-01-014-033}

[]{#MA-SEC-ANM-01-014-005}

**Pregunta.** ¿Cómo se reparte el error para una suma?

**Solución.** Con tolerancias $\varepsilon/2$ para ambos sumandos y el mínimo de sus radios.

El error de la suma es $|(f(x)-f(a))+(g(x)-g(a))|$. La triangular lo domina por la suma de los dos errores. Pedimos cada uno menor que $\varepsilon/2$ y tomamos el mínimo de radios para disponer de ambos controles. En el centro los dos errores son cero y cumplen la misma prueba. No es necesario perforar las ventanas.

### Microcontrol 034

[]{#MA-MIC-ANM-01-014-034}

[]{#MA-MSOL-ANM-01-014-034}

**Pregunta.** ¿Qué se hace con un escalar nulo?

**Solución.** Su producto es la función cero y tiene error cero; no se divide por el escalar.

Multiplicar por cero produce salida central cero y todas las demás salidas cero. Por tanto cualquier radio positivo satisface cualquier precisión. Para un escalar no nulo se usa el presupuesto $\varepsilon/|c|$ de la función original. Separar el caso cero evita escribir una división sin definir y muestra que la afirmación también vale cuando la regla se vuelve constante.

### Microcontrol 035

[]{#MA-MIC-ANM-01-014-035}

[]{#MA-MSOL-ANM-01-014-035}

**Pregunta.** ¿Qué proporciona continuidad con tolerancia $1$ para el producto?

**Solución.** Una cota local $|f(x)|<|f(a)|+1$ en una bola relativa completa.

La precisión uno asegura $|f(x)-f(a)|<1$ cerca del centro. La triangular da entonces $|f(x)|<|f(a)|+1$. Esta constante controla el factor variable que aparece en la identidad de error del producto. La barrera incluye el centro, porque allí también vale la estimación. Reunir su radio con los radios de precisión permite que todos los controles actúen en la misma ventana.

### Microcontrol 036

[]{#MA-MIC-ANM-01-014-036}

[]{#MA-MSOL-ANM-01-014-036}

**Pregunta.** ¿Qué hipótesis permite el recíproco en el centro?

**Solución.** Que $g(a)\ne0$. La tolerancia $|g(a)|/2$ separa el denominador de cero cerca de $a$.

La continuidad con tolerancia $|g(a)|/2$ asegura que $g(x)$ no puede alejarse del valor no nulo central lo suficiente para alcanzar cero. La triangular inversa da $|g(x)|>|g(a)|/2>0$. Esa separación común permite invertir el denominador y estimar su error. Si $g(a)=0$, el recíproco no estaría definido en el propio centro y esta prueba no se aplica.

### Microcontrol 037

[]{#MA-MIC-ANM-01-014-037}

[]{#MA-MSOL-ANM-01-014-037}

**Pregunta.** ¿Cuál es el dominio efectivo de $f/g$?

**Solución.** $D_g=\{x\in D:g(x)\ne0\}$. Si $g(a)\ne0$, incluye el centro y una bola relativa alrededor de él.

Los puntos donde $g$ se anula deben excluirse del dominio de evaluación. Si el centro tiene denominador no nulo, la barrera local muestra que una bola relativa del dominio original está contenida en $D_g$. Así la continuidad del cociente se formula en un dominio que incluye el centro y donde todas las operaciones están definidas. No se afirma nada sobre evaluaciones en los ceros excluidos.

### Microcontrol 038

[]{#MA-MIC-ANM-01-014-038}

[]{#MA-MSOL-ANM-01-014-038}

**Pregunta.** ¿Hay que exigir $f(x)\ne f(a)$ para componer funciones continuas?

**Solución.** No. El contrato de la exterior incluye su centro y controla su valor.

La función exterior es continua en $f(a)$ y controla también la evaluación en ese mismo punto. Si alguna entrada cercana produce $f(x)=f(a)$, el error compuesto es cero. Las demás entradas se controlan mediante las escalas anidadas habituales. A diferencia de un límite exterior perforado, continuidad no deja un valor central excepcional sin controlar, por lo que no exige evitación.

### Microcontrol 039

[]{#MA-MIC-ANM-01-014-039}

[]{#MA-MSOL-ANM-01-014-039}

**Pregunta.** ¿Qué conjunto permite componer si no sabemos que $f[D]\subseteq E$?

**Solución.** $T=\{x\in D:f(x)\in E\}$. Se compone la restricción con codominio $E$ y la continuidad se afirma en $T$.

La composición sólo se puede evaluar cuando la salida intermedia pertenece al dominio $E$ de la exterior. El conjunto $T$ reúne exactamente esas entradas. Para afirmar continuidad en un centro de $T$ se restringe la interior a $T$ y se declara su codominio compatible. La cercanía numérica de una salida no reemplaza la pertenencia al dominio; el tipo debe comprobarse antes de la estimación.

### Microcontrol 040

[]{#MA-MIC-ANM-01-014-040}

[]{#MA-MSOL-ANM-01-014-040}

**Pregunta.** ¿Qué identidad da la prueba global de composición?

**Solución.** $(g\circ f)^{-1}[V]=f^{-1}[g^{-1}[V]]$, con los tipos y ambientes relativos correspondientes.

Un abierto de salida final se selecciona primero mediante $g$, obteniendo un abierto relativo de entradas intermedias. La preimagen de éste mediante $f$ es abierta relativa en el dominio inicial. La identidad muestra que ese conjunto es precisamente la preimagen de la composición. Así todas las preimágenes finales son abiertas en el ambiente correcto y el criterio concluye continuidad global.

## §14.6 — Lo que la continuidad no promete sobre imágenes e inversas

### Microcontrol 041

[]{#MA-MIC-ANM-01-014-041}

[]{#MA-MSOL-ANM-01-014-041}

[]{#MA-SEC-ANM-01-014-006}

**Pregunta.** ¿Qué imagen abierta refuta que continuidad implique aplicación abierta?

**Solución.** El cuadrado envía el abierto $\mathbb R$ a $[0,\infty)$, que no es abierto en la recta.

El conjunto de entradas $\mathbb R$ es abierto y el cuadrado es continuo. Su imagen contiene todos los no negativos y ningún negativo, por lo que es $[0,\infty)$. Ninguna bola real centrada en cero cabe allí, así que la imagen no es abierta en el codominio real. Un solo abierto cuya imagen falla basta para refutar que toda función continua sea una aplicación abierta.

### Microcontrol 042

[]{#MA-MIC-ANM-01-014-042}

[]{#MA-MSOL-ANM-01-014-042}

**Pregunta.** ¿Qué ejemplo continuo tiene imagen no cerrada aunque su dominio sea cerrado?

**Solución.** $r(x)=1/(1+x^2)$ en $\mathbb R$, con imagen $(0,1]$. Cero es adherente y no pertenece a ella.

El denominador $1+x^2$ es siempre positivo y continuo, de modo que su recíproco es continuo. Las salidas están entre cero, excluido, y uno, incluido; cada valor de ese intervalo se alcanza tomando una raíz adecuada. Las salidas pueden acercarse arbitrariamente a cero aunque ninguna sea cero. Así la imagen no es cerrada, pese a que el dominio completo real sí lo es.

### Microcontrol 043

[]{#MA-MIC-ANM-01-014-043}

[]{#MA-MSOL-ANM-01-014-043}

**Pregunta.** ¿Qué añade la bijectividad a una función continua?

**Solución.** Añade la existencia de una función inversa, pero no garantiza la continuidad de esa inversa.

La biyectividad garantiza que cada salida declarada tiene una única entrada y permite construir la inversa como función. Continuidad de la inversa exige además que salidas cercanas recuperen entradas cercanas. Esto no se sigue únicamente del control hacia delante: salidas próximas pueden proceder de piezas del dominio separadas entre sí. El ejemplo de §14.6 verifica esa diferencia mediante un centro concreto.

### Microcontrol 044

[]{#MA-MIC-ANM-01-014-044}

[]{#MA-MSOL-ANM-01-014-044}

**Pregunta.** En la biyección de §14.6, ¿cuál es la inversa en $y=1$?

**Solución.** $h(1)=2$, porque el valor uno procede del punto $x=2$ de la segunda pieza.

La primera pieza $[0,1)$ se envía a sí misma y no alcanza uno. La segunda $[2,3]$ se envía por $x\mapsto x-1$ a $[1,2]$, y la entrada dos produce uno. Como ambas imágenes son disjuntas, esa entrada es única. La inversa vale $h(y)=y$ por debajo de uno y $h(y)=y+1$ desde uno; en el centro solicitado, debe usarse la segunda regla.

### Microcontrol 045

[]{#MA-MIC-ANM-01-014-045}

[]{#MA-MSOL-ANM-01-014-045}

**Pregunta.** ¿Qué entradas refutan la continuidad de esa inversa en uno?

**Solución.** $y=1-t$ con $t=\min(\delta/2,1/2)>0$: la distancia de entrada es $t<\delta$ y la de salida a $2$ es $1+t$.

El número $t$ es positivo, no supera $1/2$ y es menor que $\delta$. Por eso $y=1-t$ pertenece al codominio y está dentro de cualquier ventana propuesta alrededor de uno. Su inversa es $1-t$, mientras la inversa del centro es dos. La distancia $1+t$ supera uno. La tolerancia fija uno falla para todos los radios y refuta directamente continuidad inversa.

### Microcontrol 046

[]{#MA-MIC-ANM-01-014-046}

[]{#MA-MSOL-ANM-01-014-046}

**Pregunta.** ¿Qué es un homeomorfismo entre subconjuntos reales?

**Solución.** Una biyección continua cuya inversa es continua, con continuidad relativa en ambos ambientes.

La definición exige control de proximidad en ambas direcciones de un transporte reversible. Los dos controles son relativos a los subconjuntos declarados como dominio y codominio. Una biyección continua sólo cumple la mitad de esta exigencia. Un homeomorfismo asegura que podemos pasar a las salidas y volver a las entradas sin introducir una discontinuidad en ninguno de los dos recorridos.

### Microcontrol 047

[]{#MA-MIC-ANM-01-014-047}

[]{#MA-MSOL-ANM-01-014-047}

**Pregunta.** ¿Qué condición de imágenes equivale a continuidad de la inversa de una biyección?

**Solución.** Que la biyección sea abierta: envía abiertos relativos del dominio a abiertos relativos del codominio.

Para $h=f^{-1}$ y $U\subseteq D$, tenemos $h^{-1}[U]=f[U]$: una salida queda seleccionada por $h$ exactamente cuando su entrada inversa pertenece a $U$. El criterio de continuidad de $h$ pide que esas preimágenes sean abiertas relativas en $E$ para todo abierto relativo $U$ de $D$. Eso es precisamente que $f$ sea abierta. La identidad depende de la inversa legítima de una biyección.

### Microcontrol 048

[]{#MA-MIC-ANM-01-014-048}

[]{#MA-MSOL-ANM-01-014-048}

**Pregunta.** ¿Por qué no contradice el criterio de preimágenes el fallo de imagen abierta?

**Solución.** Porque imagen y preimagen son operaciones distintas. El criterio sólo garantiza apertura al transportar conjuntos de salida hacia atrás.

La continuidad de $f$ controla conjuntos de entradas seleccionados por condiciones abiertas sobre sus salidas. Una aplicación abierta controla, en cambio, conjuntos de salidas producidos desde abiertos de entradas. Son direcciones diferentes del transporte. El cuadrado satisface el primer criterio y puede fallar el segundo sin contradicción. Cambiar preimagen por imagen altera la propiedad que se está afirmando.

## §14.7 — Reunir definiciones locales y piezas cerradas

### Microcontrol 049

[]{#MA-MIC-ANM-01-014-049}

[]{#MA-MSOL-ANM-01-014-049}

[]{#MA-SEC-ANM-01-014-007}

**Pregunta.** ¿Necesita ser finita una cobertura por abiertos para comprobar continuidad localmente?

**Solución.** No. En cada punto se usa una pieza abierta que lo contiene y una bola relativa dentro de esa pieza.

Fijado un punto, basta tomar una pieza abierta que lo contenga. Su apertura proporciona un radio que mantiene las entradas próximas dentro de esa pieza, y allí se usa el radio de continuidad de la restricción. Sólo se reúnen esos dos radios. No es necesario obtener una escala común para toda la cobertura, por lo que puede tener infinitas piezas.

### Microcontrol 050

[]{#MA-MIC-ANM-01-014-050}

[]{#MA-MSOL-ANM-01-014-050}

**Pregunta.** ¿Qué función cumplen las piezas cerradas que no contienen el centro en el pegado finito?

**Solución.** Sus complementos abiertos dan radios que excluyen esas piezas de una ventana alrededor del centro.

Si una pieza cerrada relativa no contiene al centro, su complemento es abierto relativo y sí lo contiene. Ese complemento ofrece una ventana donde ninguna entrada pertenece a la pieza. Así la prueba puede eliminar localmente las piezas que no disponen de un control centrado en el punto. Las piezas que sí lo contienen aportan, en cambio, sus radios de continuidad.

### Microcontrol 051

[]{#MA-MIC-ANM-01-014-051}

[]{#MA-MSOL-ANM-01-014-051}

**Pregunta.** ¿Dónde se usa la finitud de la cobertura cerrada?

**Solución.** Al tomar el mínimo de todos los radios de control y exclusión, que sigue siendo positivo.

Cada pieza proporciona un radio de control o un radio de exclusión. Para una cobertura finita podemos tomar su mínimo y sigue siendo positivo. Toda entrada de la ventana resultante pertenece sólo a piezas controladas y cumple la precisión. Para infinitas piezas el ínfimo de radios puede ser cero, dejando sin una escala común. Éste es el paso específico donde no puede omitirse la finitud.

### Microcontrol 052

[]{#MA-MIC-ANM-01-014-052}

[]{#MA-MSOL-ANM-01-014-052}

**Pregunta.** ¿Qué asegura el acuerdo de las funciones en intersecciones?

**Solución.** Que la función pegada está bien definida y su restricción coincide con cada función de pieza. No asegura por sí solo continuidad en fronteras.

Si un punto pertenece a dos piezas, las dos reglas deben asignarle el mismo valor para que exista una única función pegada. El acuerdo garantiza esa consistencia. Pero no controla por sí solo aproximaciones desde piezas que llegan arbitrariamente cerca del punto sin contenerlo. Para concluir continuidad hacen falta las hipótesis topológicas del pegado, además de continuidad de las restricciones.

### Microcontrol 053

[]{#MA-MIC-ANM-01-014-053}

[]{#MA-MSOL-ANM-01-014-053}

**Pregunta.** ¿Qué piezas y valores permiten pegar $|x|$?

**Solución.** $-x$ en $(-\infty,0]$ y $x$ en $[0,\infty)$. Son piezas cerradas con valor común cero en la intersección.

Los semiejes cerrados cubren la recta y se intersectan únicamente en cero. Ambas reglas afines dan allí cero y son continuas en sus dominios relativos. El teorema de pegado finito permite reunirlas y obtener la función valor absoluto continua en toda la recta. Que las reglas tengan pendientes diferentes no importa: el control se verifica en cada pieza y los valores coinciden en el punto compartido.

### Microcontrol 054

[]{#MA-MIC-ANM-01-014-054}

[]{#MA-MSOL-ANM-01-014-054}

**Pregunta.** ¿Por qué falla pegar cero en $(-\infty,0)$ y uno en $[0,\infty)$?

**Solución.** La pieza izquierda no es cerrada ni puede excluirse cerca de cero. Sus entradas próximas tienen error uno respecto del valor central uno.

La regla global está bien definida porque las piezas son disjuntas, pero en cero su valor es uno. Para cualquier radio, una entrada negativa próxima tiene salida cero y error uno. La pieza izquierda llega arbitrariamente cerca de cero sin contenerlo y no puede excluirse con una ventana. Falta la hipótesis de cerradura de esa pieza para aplicar el pegado finito.

### Microcontrol 055

[]{#MA-MIC-ANM-01-014-055}

[]{#MA-MSOL-ANM-01-014-055}

**Pregunta.** ¿Qué tolerancia conserva localmente un valor central positivo?

**Solución.** $f(a)/2$. Continuidad da $f(x)>f(a)/2>0$ cerca del centro.

Como $f(a)>0$, la mitad de ese valor es una tolerancia positiva válida. El control implica $f(x)>f(a)-f(a)/2=f(a)/2>0$ en la ventana relativa. La estimación no sólo conserva el signo: mantiene una separación positiva común respecto de cero. Puede usarse para proteger denominadores o describir localmente la preimagen de los positivos.

### Microcontrol 056

[]{#MA-MIC-ANM-01-014-056}

[]{#MA-MSOL-ANM-01-014-056}

**Pregunta.** ¿La conservación local de signo prueba el valor intermedio?

**Solución.** No. Sólo protege el signo cerca de un punto. La existencia de valores entre salidas en un intervalo se estudia en C15.

La estabilidad local de signo responde a qué sucede cerca de un valor central no nulo. El teorema del valor intermedio responde a una pregunta de existencia entre salidas de puntos distintos de un intervalo. Para pasar de datos locales a esa conclusión global hay que utilizar propiedades adicionales del dominio y un argumento nuevo. La protección de un signo en una ventana no construye por sí sola una entrada de valor cero.

## §14.8 — Certificados de proximidad y límites del control lineal

### Microcontrol 057

[]{#MA-MIC-ANM-01-014-057}

[]{#MA-MSOL-ANM-01-014-057}

[]{#MA-SEC-ANM-01-014-008}

**Pregunta.** Con una cota local $|f(x)-f(a)|\le K|x-a|$, $K>0$, ¿qué radio sirve?

**Solución.** $\delta=\min(r,\varepsilon/K)$, donde $r$ es el radio en que vale la cota.

El radio $r$ mantiene la entrada en la región donde vale la cota, y $\varepsilon/K$ ajusta el tamaño del error. Tomar el mínimo garantiza ambas condiciones. Entonces $|f(x)-f(a)|\le K|x-a|<K\delta\le\varepsilon$. La desigualdad no estricta inicial admite el centro y la condición estricta de entrada proporciona la precisión final. La elección es positiva porque $K>0$.

### Microcontrol 058

[]{#MA-MIC-ANM-01-014-058}

[]{#MA-MSOL-ANM-01-014-058}

**Pregunta.** ¿Qué ocurre si $K=0$?

**Solución.** La función coincide localmente con $f(a)$; sirve el radio $r$ y el error es cero.

La cota se vuelve $|f(x)-f(a)|\le0$ y fuerza igualdad de valores en toda la ventana pertinente. Cualquier desafío tiene allí error cero. No necesitamos reducir el radio según la precisión ni dividir por $K$. El caso muestra que una estimación lineal degenerada describe constancia local, que es una forma particularmente directa de continuidad.

### Microcontrol 059

[]{#MA-MIC-ANM-01-014-059}

[]{#MA-MSOL-ANM-01-014-059}

**Pregunta.** ¿Qué dependencia aparece en el certificado del cuadrado?

**Solución.** $\delta=\min(1,\varepsilon/(1+2|a|))$ depende del centro $a$ y del desafío $\varepsilon$.

La factorización $x^2-a^2=(x-a)(x+a)$ introduce un multiplicador que cambia con el centro. En una ventana de radio uno, su magnitud se domina por $1+2|a|$. La elección de radio responde a esa constante y a la precisión. Esto proporciona continuidad en cada centro, pero no afirma que el mismo radio funcione para todos ellos; la dependencia forma parte explícita del certificado.

### Microcontrol 060

[]{#MA-MIC-ANM-01-014-060}

[]{#MA-MSOL-ANM-01-014-060}

**Pregunta.** ¿Qué identidad controla el error de la raíz?

**Solución.** Para $u=\sqrt{x}$, $v=\sqrt{a}$, se tiene $(u-v)^2\le|x-a|$ al factorizar la diferencia de cuadrados y distinguir el orden de $u,v$.

Si $u\ge v\ge0$, entonces $x-a=(u-v)(u+v)$ y $u+v\ge u-v$, por lo que $x-a\ge(u-v)^2$. Si el orden es el contrario, intercambiamos los dos valores. Así $|\sqrt{x}-\sqrt{a}|^2\le|x-a|$ para todas las entradas no negativas. La estimación evita dividir por una raíz que podría ser cero y sirve también en el extremo del dominio.

### Microcontrol 061

[]{#MA-MIC-ANM-01-014-061}

[]{#MA-MSOL-ANM-01-014-061}

**Pregunta.** ¿Qué radio certifica continuidad de la raíz en cero?

**Solución.** $\delta=\varepsilon^2$, para entradas del dominio no negativo: $\sqrt{x}<\varepsilon$ si $0\le x<\varepsilon^2$.

El centro cero pertenece al dominio no negativo. Para una precisión $\varepsilon>0$, el radio $\varepsilon^2$ es positivo. Si una entrada admitida satisface $|x|<\varepsilon^2$, entonces $0\le x<\varepsilon^2$ y su raíz es menor que $\varepsilon$. El centro tiene error cero y los negativos no son entradas de esta función real. La prueba es continuidad relativa en un extremo.

### Microcontrol 062

[]{#MA-MIC-ANM-01-014-062}

[]{#MA-MSOL-ANM-01-014-062}

**Pregunta.** ¿Una función continua debe admitir una cota lineal local de ese error?

**Solución.** No. La raíz es continua en cero pero $\sqrt{x}/x=1/\sqrt{x}$ supera cualquier constante para entradas positivas suficientemente pequeñas.

Una cota lineal pediría $\sqrt{x}\le Kx$ en una ventana de cero. Para $x>0$ equivale a $1/\sqrt{x}\le K$, pero ese cociente crece sin barrera al acercarse a cero. Puede elegirse una entrada positiva menor que cualquier radio donde falle la cota. Continuidad sí existe con un radio cuadrático en la tolerancia. La ausencia de un certificado lineal no es ausencia de continuidad.

### Microcontrol 063

[]{#MA-MIC-ANM-01-014-063}

[]{#MA-MSOL-ANM-01-014-063}

**Pregunta.** ¿Por qué la cota inferior para probar continuidad inversa se exige a todo $x\in D$?

**Solución.** Para excluir que entradas lejanas produzcan salidas cercanas al valor central. Una cota sólo local no puede aplicarse antes de saber que la inversa es cercana.

Una cota inferior que sólo vale para entradas ya cercanas al centro no puede usarse para demostrar que una entrada inversa es cercana: eso supondría la conclusión. Una cota válida para todas las entradas compara también las lejanas y prohíbe que produzcan salidas demasiado próximas. El ejemplo por piezas muestra que una rama distante puede acercar sus salidas al mismo centro exterior y hacer fallar la inversa.

### Microcontrol 064

[]{#MA-MIC-ANM-01-014-064}

[]{#MA-MSOL-ANM-01-014-064}

**Pregunta.** ¿Qué radios aportan las cotas $c|x-z|\le|f(x)-f(z)|\le C|x-z|$, con $c,C>0$?

**Solución.** Para la función sirve $\varepsilon/C$; para la inversa sirve $c\varepsilon$. La bijectividad legitima usar la entrada inversa única.

La cota superior da continuidad directa mediante $C|x-a|<\varepsilon$. Para la inversa, una salida $y$ cercana a $f(a)$ corresponde a una entrada única $x$, y la cota inferior global da $|x-a|\le|y-f(a)|/c$. Pedir distancia de salida menor que $c\varepsilon$ produce error inverso menor que $\varepsilon$. Las dos constantes deben ser positivas y los tipos inversos legítimos.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html)
