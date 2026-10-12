---
content-id: MA-BCH-0269
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-016-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 16
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C16_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §16.1 — Una cubierta dada y una reducción finita

### Microcontrol 001

[]{#MA-MIC-ANM-01-016-001}

[]{#MA-MSOL-ANM-01-016-001}

[]{#MA-SEC-ANM-01-016-001}

**Pregunta.** ¿Qué distingue una cubierta finita particular de la compacidad?

**Solución.** Una cubierta finita particular cubre el conjunto una sola vez; compacidad exige una subcubierta finita dentro de toda cubierta abierta dada. La familia $\{\mathbb R\}$ cubre finitamente cualquier conjunto, incluso los no compactos.

La diferencia está en el cuantificador sobre cubiertas: se fija una familia abierta cualquiera y se debe reducir esa misma familia. Presentar una familia conveniente sólo prueba que alguna cubierta finita existe. La cubierta creciente de la recta muestra que esa existencia particular puede coexistir con otra cubierta imposible de reducir finitamente.

### Microcontrol 002

[]{#MA-MIC-ANM-01-016-002}

[]{#MA-MSOL-ANM-01-016-002}

**Pregunta.** ¿Qué debe conservar una subcubierta de $(U_i)_{i\in I}$?

**Solución.** Miembros de la familia original y cobertura de todos los puntos de $K$. Se restringe a índices $J\subseteq I$ finitos; no se reemplazan abiertos por otros nuevos.

Los índices elegidos pueden depender de la cubierta dada, pero sus abiertos deben proceder de ella. Además la reducción debe cubrir simultáneamente todas las entradas de $K$. Sustituirlos por un abierto nuevo como toda la recta perdería la obligación de procedencia y haría trivial una afirmación que no es compacidad.

### Microcontrol 003

[]{#MA-MIC-ANM-01-016-003}

[]{#MA-MSOL-ANM-01-016-003}

**Pregunta.** ¿La cobertura $\forall x\in K\;\exists i:x\in U_i$ ya da una función de índices por punto?

**Solución.** No. Asegura un testigo para cada punto considerado, pero no construye una selección simultánea $x\mapsto i_x$. Las pruebas usan sólo los testigos concretos que necesitan.

Para una entrada fijada podemos usar la existencia de un índice que la cubra. Eso no equivale a disponer de una función que elija índices para todas las entradas a la vez. Una subcubierta finita proporciona un conjunto de índices suficiente para toda la cobertura, sin asignar un índice preferido a cada punto.

### Microcontrol 004

[]{#MA-MIC-ANM-01-016-004}

[]{#MA-MSOL-ANM-01-016-004}

**Pregunta.** ¿Cómo se cubre finitamente el vacío dentro de cualquier cubierta?

**Solución.** Tomando el conjunto vacío de índices. Su unión es vacía y contiene al conjunto vacío, incluso si la cubierta original no tiene índices.

La unión de una familia vacía es vacía, y la inclusión $\varnothing\subseteq\varnothing$ verifica cobertura. El conjunto vacío de índices es finito y está contenido en cualquier familia de índices. Así el caso queda resuelto sin pedir que exista un abierto ni una entrada que lo necesite.

### Microcontrol 005

[]{#MA-MIC-ANM-01-016-005}

[]{#MA-MSOL-ANM-01-016-005}

**Pregunta.** ¿Por qué una cubierta arbitraria de un singleton tiene subcubierta finita?

**Solución.** La cobertura del único punto $a$ da un índice $i$ con $a\in U_i$. El singleton de índices $\{i\}$ cubre todo $\{a\}$.

El único punto se fija desde el dominio. La hipótesis de cobertura proporciona un solo testigo de índice, y ese mismo abierto cubre todas las entradas porque sólo hay una. No importa el tamaño de la familia original ni la forma del abierto. La finitud obtenida es la de la lista de índices seleccionados.

### Microcontrol 006

[]{#MA-MIC-ANM-01-016-006}

[]{#MA-MSOL-ANM-01-016-006}

**Pregunta.** ¿Cómo se combinan dos subcubiertas finitas para cubrir una unión de compactos?

**Solución.** La cubierta de la unión cubre cada pieza. Cada compacto da un conjunto finito de índices y su unión, también finita, cubre ambas piezas.

Se aplica la compacidad de cada pieza a la misma cubierta original, conservando la procedencia de los índices. Un punto de la unión está en alguna pieza y por ello en un abierto de su reducción. La unión de las dos listas de índices sigue siendo finita; índices repetidos no perjudican la cobertura.

### Microcontrol 007

[]{#MA-MIC-ANM-01-016-007}

[]{#MA-MSOL-ANM-01-016-007}

**Pregunta.** ¿Por qué $U_n=(-(n+1),n+1)$ no tiene una subcubierta finita de la recta?

**Solución.** Los índices de una subfamilia finita no vacía tienen máximo $m$, y todos los abiertos seleccionados están en $U_m$. El punto $m+2$ queda fuera. La familia vacía tampoco cubre la recta.

Los abiertos crecen con el índice, así el máximo de una lista finita domina a todos sus miembros. El punto $m+2$ supera el extremo derecho $m+1$ y no está en ninguno. La familia completa sí cubre cada real por arquimedianidad. Esto acredita una cubierta válida sin reducción finita, no simplemente una lista finita mal elegida.

### Microcontrol 008

[]{#MA-MIC-ANM-01-016-008}

[]{#MA-MSOL-ANM-01-016-008}

**Pregunta.** ¿El ínfimo de una familia infinita de radios positivos tiene que ser positivo?

**Solución.** No. $r_n=1/(n+1)>0$ para todo $n$, pero $\inf_n r_n=0$. Un mínimo positivo se garantiza aquí sólo para una familia finita no vacía de valores positivos.

Todo mínimo de una lista finita no vacía es uno de sus valores y hereda su positividad. En los recíprocos, en cambio, cualquier candidato positivo es superado hacia abajo por algún término. Cero es cota inferior y ninguna cota inferior positiva sirve. Reunir infinitos controles locales mediante un ínfimo podría dejar una escala nula.

## §16.2 — El supremo prolonga los segmentos cubiertos

### Microcontrol 009

[]{#MA-MIC-ANM-01-016-009}

[]{#MA-MSOL-ANM-01-016-009}

[]{#MA-SEC-ANM-01-016-002}

**Pregunta.** ¿Qué registra el conjunto $S$ en la prueba de compacidad de $[a,b]$?

**Solución.** Los $x\in[a,b]$ para los que el segmento $[a,x]$ admite alguna subcubierta finita de la cubierta dada. Registra existencia, sin elegir una subcubierta para cada $x$.

La definición de $S$ es un predicado de pertenencia: para cada $x$ pregunta si existe alguna reducción finita que cubra hasta allí. No almacena una elección de índices por punto. Cuando se fija después un $t\in S$, se puede usar la existencia para ese único segmento y extender su cobertura.

### Microcontrol 010

[]{#MA-MIC-ANM-01-016-010}

[]{#MA-MSOL-ANM-01-016-010}

**Pregunta.** ¿Por qué $S$ es no vacío y acotado superiormente?

**Solución.** $a\in S$ porque un solo abierto que cubre $a$ cubre $[a,a]$. Además $S\subseteq[a,b]$, así $b$ es cota superior.

El segmento inicial degenerado $[a,a]$ contiene sólo a $a$, y un miembro de la cubierta que lo contenga basta para registrarlo en $S$. La cota $b$ procede del recorte que aparece en la propia definición de $S$. Ambas premisas son necesarias antes de invocar completitud para obtener $\sup S$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-016-011}

[]{#MA-MSOL-ANM-01-016-011}

**Pregunta.** ¿Qué proporciona la apertura de un miembro que contiene $c=\sup S$?

**Solución.** Un radio $r>0$ con $(c-r,c+r)\subseteq U_{i_c}$. Ese margen permitirá ampliar una cobertura finita que llegue a un $t$ suficientemente próximo a $c$.

Primero se ubica $c$ en $[a,b]$, por lo que la cubierta realmente lo cubre. La apertura del miembro encontrado convierte esa pertenencia en un margen de extensión a ambos lados. No se presupone que $c$ ya esté en $S$: el margen se utiliza para unir una cobertura cercana con ese abierto y demostrar una nueva pertenencia.

### Microcontrol 012

[]{#MA-MIC-ANM-01-016-012}

[]{#MA-MSOL-ANM-01-016-012}

**Pregunta.** ¿Por qué existe $t\in S$ con $c-r/2<t\le c$?

**Solución.** Porque $c-r/2<c$ no puede ser cota superior de $S$. La negación de ser cota produce un $t\in S$ mayor, y $t\le c$ por ser $c$ cota.

Si $c-r/2$ dominara a todos los elementos de $S$, sería una cota superior menor que el supremo, imposible. El testigo obtenido queda cerca por debajo, o puede ser el propio supremo si éste pertenece a $S$. Aquí no se exige distancia positiva: lo necesario es que el tramo a prolongar permanezca en el abierto alrededor de $c$.

### Microcontrol 013

[]{#MA-MIC-ANM-01-016-013}

[]{#MA-MSOL-ANM-01-016-013}

**Pregunta.** ¿Qué impide que $d=\min(b,c+r/2)$ salga del segmento?

**Solución.** La fórmula da $c\le d\le b$, y $c\ge a$. Así $d\in[a,b]$, a la vez que todo $[t,d]$ queda dentro de la bola de radio $r$ alrededor de $c$.

El mínimo conserva a la vez la cota del segmento y la distancia de avance permitida por el radio. Para cada $z\in[t,d]$, tenemos $c-r<z<c+r$ porque $t>c-r/2$ y $d\le c+r/2$. Así todo el tramo nuevo queda cubierto, no sólo su extremo. La fórmula funciona también cuando $c=b$, caso en que $d=b$.

### Microcontrol 014

[]{#MA-MIC-ANM-01-016-014}

[]{#MA-MSOL-ANM-01-016-014}

**Pregunta.** ¿Por qué $J_t\cup\{i_c\}$ cubre $[a,d]$?

**Solución.** $J_t$ cubre $[a,t]$ y $U_{i_c}$ cubre $[t,d]$. Como $a\le t\le d$, la unión de esos dos segmentos es $[a,d]$; los índices siguen siendo finitos.

Una entrada de $[a,d]$ anterior a $t$ queda cubierta por la reducción de $[a,t]$; una posterior queda en el abierto que contiene todo $[t,d]$. En $t$ pueden funcionar ambas coberturas sin problema. Añadir un único índice a un conjunto finito mantiene finitud y todos los índices pertenecen a la familia original.

### Microcontrol 015

[]{#MA-MIC-ANM-01-016-015}

[]{#MA-MSOL-ANM-01-016-015}

**Pregunta.** ¿De $\sup S=b$ se deduce siempre $b\in S$?

**Solución.** No. $S=[a,b)$ con $a<b$ tiene supremo $b$ pero no lo contiene. En R2 se obtiene además $d\in S$ y, una vez $c=b$, $d=b$, lo que sí prueba pertenencia.

La igualdad del supremo describe una cota óptima, no un miembro del conjunto. Para cerrar R2 hay que demostrar que el segmento completo admite reducción finita. La construcción de $d$ da esa información adicional: una vez forzado $c=b$, su pertenencia a $S$ se convierte en pertenencia de $b$.

### Microcontrol 016

[]{#MA-MIC-ANM-01-016-016}

[]{#MA-MSOL-ANM-01-016-016}

**Pregunta.** ¿Qué cambia para $a=b$ o para $a>b$?

**Solución.** Si $a=b$, el segmento es singleton y basta un abierto que cubra ese punto. Con $a>b$, la notación de intervalo describe el vacío, compacto por la subfamilia vacía.

En el singleton, un único miembro de la cubierta cubre el segmento entero. En el vacío, ninguna entrada necesita cobertura y sirve la lista vacía. Tratar ambos casos directamente evita pedir radios de prolongación o máximos de índices que no son necesarios. La convención $[a,b]=\varnothing$ para $a>b$ se distingue del segmento entre dos puntos ordenado con mínimo y máximo.

## §16.3 — Heredar compacidad sin perder índices

### Microcontrol 017

[]{#MA-MIC-ANM-01-016-017}

[]{#MA-MSOL-ANM-01-016-017}

[]{#MA-SEC-ANM-01-016-003}

**Pregunta.** ¿Qué representación se usa para un cerrado relativo $A\subseteq K$?

**Solución.** $A=K\cap F$ con $F$ cerrado en toda la recta. Su complemento ambiental $\mathbb R\setminus F$ es abierto y cubre los puntos de $K$ que no están en $A$.

Los puntos de $K$ que están en $F$ son exactamente los de $A$. Los restantes pertenecen al abierto real complementario, que permite ampliar una cubierta de $A$ a una de $K$. La representación respeta el ambiente: $A$ puede ser cerrado relativo aunque no se afirme todavía que sea cerrado en toda la recta.

### Microcontrol 018

[]{#MA-MIC-ANM-01-016-018}

[]{#MA-MSOL-ANM-01-016-018}

**Pregunta.** ¿Por qué se añade todo $\mathbb R\setminus F$ a la cubierta de $A$?

**Solución.** Para cubrir cada punto de $K\setminus A$. Añadir sólo una porción próxima a un extremo podría dejar puntos de ese complemento sin cubrir.

Para aplicar compacidad de $K$, cada entrada de $K$ debe quedar cubierta. El complemento completo de $F$ cubre automáticamente todas las entradas que no pertenecen a $A$. Un recorte arbitrario de ese abierto puede dejar fuera alguna, invalidando la premisa de cobertura antes de poder extraer índices finitos.

### Microcontrol 019

[]{#MA-MIC-ANM-01-016-019}

[]{#MA-MSOL-ANM-01-016-019}

**Pregunta.** ¿Para qué sirve etiquetar el índice nuevo de la cubierta ampliada?

**Solución.** Para que sea distinto de todos los originales, aunque algún valor de abierto coincida. Así se puede retirar el índice añadido sin perder la procedencia de los miembros originales.

La subfamilia se identifica por índices y no sólo por los conjuntos abiertos que aparecen como valores. Etiquetar los índices originales y el añadido permite reconocer su procedencia aun si dos valores coinciden. Después se retira únicamente el índice excepcional y se conserva la lista finita de índices originales.

### Microcontrol 020

[]{#MA-MIC-ANM-01-016-020}

[]{#MA-MSOL-ANM-01-016-020}

**Pregunta.** ¿Por qué el abierto añadido no es necesario para cubrir puntos de $A$?

**Solución.** Todo $x\in A$ está en $F$, así no pertenece a $\mathbb R\setminus F$. En una subcubierta ampliada debe estar cubierto por algún índice original.

Si la reducción ampliada cubre una entrada de $A$, el índice que la cubre no puede ser el excepcional porque su abierto es disjunto de $A$. Por tanto algún índice original conservado la cubre. Este razonamiento vale para cada entrada de $A$ y muestra que retirar el añadido no destruye la cobertura buscada.

### Microcontrol 021

[]{#MA-MIC-ANM-01-016-021}

[]{#MA-MSOL-ANM-01-016-021}

**Pregunta.** ¿Todo subconjunto de un compacto es compacto?

**Solución.** No. $(0,1)\subseteq[0,1]$ no lo es. La cubierta $U_n=(1/(n+2),2)$ cubre el intervalo abierto pero ninguna subfamilia finita lo cubre.

Cada entrada positiva del intervalo supera algún recíproco, así la familia propuesta sí es una cubierta abierta. Una lista finita tiene un mayor índice y no llega hasta entradas suficientemente próximas a cero. El subconjunto pierde la cerradura relativa exigida por el teorema de herencia. Pertenecer a un compacto no basta para ser compacto.

### Microcontrol 022

[]{#MA-MIC-ANM-01-016-022}

[]{#MA-MSOL-ANM-01-016-022}

**Pregunta.** ¿Qué punto queda fuera de una subfamilia finita de esa cubierta, con índice máximo $m$?

**Solución.** $x=1/(2(m+2))$ pertenece a $(0,1)$ y es menor que el extremo izquierdo $1/(m+2)$ del mayor abierto seleccionado. Está fuera de toda la unión finita.

El punto dado es positivo y menor que uno, de modo que es una entrada que la reducción debería cubrir. Su valor es menor que todos los extremos izquierdos seleccionados porque el mayor índice tiene el menor de esos extremos. La estrictitud del intervalo abierto lo deja fuera. Para la lista vacía, cualquier entrada del intervalo ya refuta cobertura.

### Microcontrol 023

[]{#MA-MIC-ANM-01-016-023}

[]{#MA-MSOL-ANM-01-016-023}

**Pregunta.** ¿Es compacta la intersección de un compacto con un cerrado real?

**Solución.** Sí. Es cerrada relativa al compacto por la representación como intersección, y R3 transmite compacidad.

El complemento relativo de $K\cap F$ dentro de $K$ es $K\cap(\mathbb R\setminus F)$, abierto relativo porque el complemento real de $F$ es abierto. Así se cumple exactamente la hipótesis de cerrado relativo de R3. La conclusión incluye la intersección vacía, que también es compacta.

### Microcontrol 024

[]{#MA-MIC-ANM-01-016-024}

[]{#MA-MSOL-ANM-01-016-024}

**Pregunta.** ¿La herencia de compacidad exige que el cerrado relativo sea intervalo?

**Solución.** No. Sólo exige cerrado relativo. Por ejemplo $[-2,-1]\cup[1,2]$ es un cerrado relativo del compacto $[-2,2]$ y es compacto aunque tenga un hueco.

La prueba de herencia amplía cubiertas con un complemento abierto y no utiliza ausencia de huecos. En el ejemplo, las dos piezas son cerradas relativas al segmento mayor y pueden cubrirse finitamente aunque estén separadas. Conexidad y compacidad responden a condiciones distintas y no deben confundirse al aplicar R3.

## §16.4 — Heine–Borel: cerrar las dos direcciones

### Microcontrol 025

[]{#MA-MIC-ANM-01-016-025}

[]{#MA-MSOL-ANM-01-016-025}

[]{#MA-SEC-ANM-01-016-004}

**Pregunta.** ¿Qué dos propiedades identifica Heine–Borel con la compacidad real?

**Solución.** Cerradura en $\mathbb R$ y acotación. Se demuestran ambas necesidades por cubiertas y la suficiencia por segmento compacto y herencia a un cerrado relativo.

Para la necesidad se reduce una cubierta creciente que controla tamaño y otra que evita un punto exterior. Para la suficiencia se usa la cota para encerrar el conjunto en un segmento y la cerradura para heredar su compacidad. Cada propiedad se utiliza en un paso diferente. La cerradura requerida es real, no sólo relativa al propio conjunto.

### Microcontrol 026

[]{#MA-MIC-ANM-01-016-026}

[]{#MA-MSOL-ANM-01-016-026}

**Pregunta.** ¿En qué momento se toma el máximo de índices para probar acotación?

**Solución.** Después de obtener una subcubierta finita de $U_n=(-(n+1),n+1)$. Para $K$ no vacío sus índices no son vacíos y tienen máximo; no se toma máximo de toda $\mathbb N$.

La compacidad transforma la familia infinita en una lista finita de índices. Sólo entonces el buen orden de una lista finita permite tomar su mayor miembro. Como el conjunto no es vacío, una reducción que lo cubra tampoco puede tener índices vacíos. El vacío se acota directamente sin introducir ese máximo.

### Microcontrol 027

[]{#MA-MIC-ANM-01-016-027}

[]{#MA-MSOL-ANM-01-016-027}

**Pregunta.** ¿Por qué $V_n=\{x:|x-p|>1/(n+1)\}$ es abierto real?

**Solución.** Es la unión de los rayos $(-\infty,p-1/(n+1))$ y $(p+1/(n+1),\infty)$, ambos abiertos.

La condición de distancia estrictamente mayor que el recíproco equivale a quedar estrictamente a uno de los dos lados de un segmento cerrado centrado en $p$. Los dos rayos abiertos describen todas las entradas permitidas. Esa representación acredita apertura en la recta, como pide la definición de compacidad por cubiertas ambientales.

### Microcontrol 028

[]{#MA-MIC-ANM-01-016-028}

[]{#MA-MSOL-ANM-01-016-028}

**Pregunta.** ¿Por qué los $V_n$ cubren $K$ cuando $p\notin K$?

**Solución.** Para cada $x\in K$, su distancia positiva $|x-p|$ supera algún recíproco $1/(n+1)$ por arquimedianidad. Entonces $x\in V_n$.

La ausencia de $p$ del conjunto asegura distancia estrictamente positiva para cada entrada fijada. Arquimedianidad permite elegir un índice cuyo umbral sea menor que esa distancia. Esto prueba cobertura entrada por entrada sin reunir una elección de índices para todas las entradas. La compacidad proporciona después la reducción simultánea finita.

### Microcontrol 029

[]{#MA-MIC-ANM-01-016-029}

[]{#MA-MSOL-ANM-01-016-029}

**Pregunta.** ¿Qué radio exterior se obtiene del máximo $m$ de una subcubierta de $V_n$?

**Solución.** $1/(m+1)>0$. Como $K\subseteq V_m$, ningún punto a distancia menor que ese radio de $p$ está en $K$. Da una bola dentro del complemento.

Los $V_n$ crecen con el índice, así toda la unión seleccionada está en $V_m$. Cada entrada de $K$ queda a distancia estrictamente mayor que el radio obtenido. Por ello la bola de ese radio en $p$ pertenece al complemento. Hacer el argumento para cada punto exterior acredita que el complemento es abierto y el conjunto cerrado.

### Microcontrol 030

[]{#MA-MIC-ANM-01-016-030}

[]{#MA-MSOL-ANM-01-016-030}

**Pregunta.** ¿Cómo se prueba compacidad de un cerrado acotado sin sucesiones?

**Solución.** Se encierra en $[-M,M]$, compacto por R2. El conjunto es cerrado relativo a ese segmento y R3 lo hace compacto.

La acotación aporta un segmento que contiene al conjunto; la cerradura real lo hace cerrado relativo a ese segmento. R2 y R3 completan la prueba con cubiertas. No se construye una ruta de puntos ni se utiliza una equivalencia secuencial. Así esta dirección de Heine–Borel no requiere la hipótesis adicional de selección del apartado siguiente.

### Microcontrol 031

[]{#MA-MIC-ANM-01-016-031}

[]{#MA-MSOL-ANM-01-016-031}

**Pregunta.** ¿Compacidad y conexidad coinciden en la recta?

**Solución.** No. $[-2,-1]\cup[1,2]$ es compacto y no conexo. $(0,1)$ es conexo y no compacto. Las condiciones de cubierta y ausencia de huecos son distintas.

El compacto separado satisface cerradura y acotación, pero omite cero entre entradas presentes. El intervalo abierto satisface ausencia de huecos, pero omite puntos adherentes de su frontera. Los dos ejemplos muestran que ninguna propiedad implica la otra. Un segmento cerrado puede poseer ambas, sin que eso las identifique.

### Microcontrol 032

[]{#MA-MIC-ANM-01-016-032}

[]{#MA-MSOL-ANM-01-016-032}

**Pregunta.** ¿Por qué añadir cero a los recíprocos restaura compacidad?

**Solución.** El conjunto resultante es acotado y cerrado: cero incluye el punto de acumulación de la cola, y todo punto exterior se separa de una cola lejana y de un prefijo finito por un radio positivo. Heine–Borel da compacidad.

Para un punto exterior positivo, una cola de recíprocos queda por debajo de la mitad de ese punto y se separa de él con un margen fijo. Las distancias al prefijo restante forman una lista finita positiva y admiten mínimo positivo. Reunir ese mínimo con el margen de la cola da una bola exterior. Incluir cero elimina precisamente el punto límite que antes faltaba.

## §16.5 — Sucesiones: extraer y seleccionar son tareas distintas

### Microcontrol 033

[]{#MA-MIC-ANM-01-016-033}

[]{#MA-MSOL-ANM-01-016-033}

[]{#MA-SEC-ANM-01-016-005}

**Pregunta.** ¿Dónde debe quedar el límite en la definición de compacidad secuencial?

**Solución.** Dentro de $K$, no sólo en $\mathbb R$. Una subsucesión convergente a un punto exterior no satisface la definición.

La extracción debe producir índices estrictamente crecientes y un límite que sea una entrada admisible del mismo conjunto. Convergencia en la recta por sí sola no garantiza esa pertenencia. Los recíprocos en $(0,1]$ muestran por qué: todas las extracciones pueden converger, pero sólo hacia un punto exterior.

### Microcontrol 034

[]{#MA-MIC-ANM-01-016-034}

[]{#MA-MSOL-ANM-01-016-034}

**Pregunta.** ¿Qué aporta Bolzano–Weierstrass de C08 para una sucesión dada en un compacto?

**Solución.** Como está acotada, aporta una subsucesión convergente en $\mathbb R$. La cerradura del compacto es el paso adicional que coloca el límite en $K$.

La acotación de $K$ acota todos los términos de la sucesión dada. Bolzano–Weierstrass obtiene una extracción con límite real. Si el límite quedara fuera, la apertura del complemento del compacto daría una bola que ningún término puede visitar, contradiciendo convergencia. La cerradura retiene el límite dentro del dominio.

### Microcontrol 035

[]{#MA-MIC-ANM-01-016-035}

[]{#MA-MSOL-ANM-01-016-035}

**Pregunta.** ¿Por qué la dirección compacta a secuencialmente compacta no fabrica una ruta por selección?

**Solución.** La sucesión de entrada ya está dada. C08 extrae índices de esa sucesión y después se usa cerradura; no se escoge un punto de cada uno de infinitos conjuntos arbitrarios.

No se inicia la prueba con una familia de conjuntos no vacíos de la que haya que fabricar términos. La sucesión está dada como función de los naturales al dominio. La extracción trabaja con sus índices y sus valores ya disponibles. Esta dirección debe distinguirse de la recíproca, donde no acotación o falta de cerradura obligan a construir una nueva ruta.

### Microcontrol 036

[]{#MA-MIC-ANM-01-016-036}

[]{#MA-MSOL-ANM-01-016-036}

**Pregunta.** ¿Por qué $1/(n+1)$ refuta compacidad secuencial de $(0,1]$?

**Solución.** Toda subsucesión también converge a cero, que no pertenece al dominio. Por unicidad no puede tener otro límite dentro de $(0,1]$.

Todo selector estrictamente creciente de índices cumple $\varphi(k)\ge k$, de modo que sus recíprocos se dominan por $1/(k+1)$. Así la subsucesión también converge a cero. Un límite diferente dentro de $(0,1]$ contradiría unicidad. No basta observar el límite de la sucesión inicial: esta cota descarta todas las extracciones posibles.

### Microcontrol 037

[]{#MA-MIC-ANM-01-016-037}

[]{#MA-MSOL-ANM-01-016-037}

**Pregunta.** ¿Qué familia se usa si un secuencialmente compacto fuera no acotado?

**Solución.** $E_n=\{x\in K:|x|>n\}$, todos no vacíos. Fabricar una sucesión $x_n\in E_n$ requiere aquí CC(R), o una enumeración dada que permita mínimos de índices.

La no acotación acredita no vacuidad de cada $E_n$ por separado. CC(R) permite reunir esos testimonios en una sola sucesión. Una extracción estrictamente creciente conserva magnitudes mayores que su índice y por ello no puede ser acotada ni convergente. Con una enumeración dada, mínimos de índices pueden determinar esos términos sin elección arbitraria.

### Microcontrol 038

[]{#MA-MIC-ANM-01-016-038}

[]{#MA-MSOL-ANM-01-016-038}

**Pregunta.** ¿Qué familia se usa si hay un punto adherente $p\notin K$?

**Solución.** $F_n=K\cap(p-1/(n+1),p+1/(n+1))$, todos no vacíos. Una selección simultánea da una ruta hacia $p$, y después compacidad secuencial y unicidad llevan a contradicción.

La adherencia hace no vacía cada ventana de $K$ alrededor de $p$. Si se dispone de una selección simultánea, las distancias menores que los recíprocos hacen converger la ruta a $p$. La propiedad secuencial produce un límite en $K$ para alguna extracción; como también converge a $p$, unicidad fuerza una pertenencia imposible.

### Microcontrol 039

[]{#MA-MIC-ANM-01-016-039}

[]{#MA-MSOL-ANM-01-016-039}

**Pregunta.** ¿Cómo una sobreyección dada $e:\mathbb N\to K$ reemplaza ese gasto de selección?

**Solución.** Para cada conjunto requerido se toma el menor índice $j$ con $e(j)$ en él. Existe por sobreyectividad y no vacuidad; el buen orden natural determina un valor único. No se inventa una enumeración de $K$.

Para cada conjunto requerido, su no vacuidad y la sobreyección hacen no vacío el conjunto de índices admisibles. El menor índice es único y define el término mediante una regla. Esos mínimos no tienen por qué crecer; aquí construyen una sucesión nueva, no un selector de subsucesión. La extracción creciente se utilizará después cuando actúe compacidad secuencial.

### Microcontrol 040

[]{#MA-MIC-ANM-01-016-040}

[]{#MA-MSOL-ANM-01-016-040}

**Pregunta.** ¿Cuál es el alcance de la recíproca secuencial demostrada?

**Solución.** Para dominios reales arbitrarios se establece bajo CC(R) explícita, local al enunciado. También se demuestra sin esa hipótesis extra cuando el dominio no vacío viene con enumeración sobreyectiva dada. El vacío se trata por separado.

La conclusión general conserva CC(R) como premisa local y no la adopta silenciosamente para todo el libro. La versión con enumeración aprovecha una regla de mínimos ya disponible. Ambas producen cerradura y acotación y luego aplican Heine–Borel. Para el vacío, la compacidad se verifica directamente y no puede exigirse una sobreyección desde los naturales.

## §16.6 — La continuidad lleva compactos a compactos

### Microcontrol 041

[]{#MA-MIC-ANM-01-016-041}

[]{#MA-MSOL-ANM-01-016-041}

[]{#MA-SEC-ANM-01-016-006}

**Pregunta.** ¿Qué ambiente tienen las preimágenes $A_i$ de una cubierta de la imagen?

**Solución.** Son abiertas relativas al dominio restringido $K$, por continuidad de $f\upharpoonright K$. No se afirma que sean abiertas en toda $\mathbb R$.

La restricción tiene dominio $K$, así una condición abierta sobre sus salidas selecciona un abierto relativo dentro de $K$. En un extremo del compacto, esa preimagen puede contener el extremo sin incluir entradas exteriores próximas. Para aplicar la definición ambiental de compacidad hay que pasar a una cubierta de abiertos reales mediante el levantamiento explícito.

### Microcontrol 042

[]{#MA-MIC-ANM-01-016-042}

[]{#MA-MSOL-ANM-01-016-042}

**Pregunta.** ¿Qué fórmula levanta esas preimágenes a abiertos reales?

**Solución.** $W_i=(\mathbb R\setminus K)\cup A_i$. La cerradura de $K$ y la apertura relativa de $A_i$ prueban apertura real de cada $W_i$.

La fórmula añade a la preimagen todas las entradas exteriores a $K$. Si $A_i=K\cap O$ con $O$ abierto real, entonces $W_i=(\mathbb R\setminus K)\cup O$. Esta igualdad prueba apertura real usando que $K$ es cerrado. A la vez $K\cap W_i=A_i$, de modo que no cambia qué entradas del compacto se seleccionan.

### Microcontrol 043

[]{#MA-MIC-ANM-01-016-043}

[]{#MA-MSOL-ANM-01-016-043}

**Pregunta.** ¿Por qué un punto de $A_i$ tiene una vecindad real dentro de $W_i$?

**Solución.** Para ese índice, $A_i=K\cap O$ con $O$ abierto real. Todo punto de $O$ está fuera de $K$ o en $A_i$, así $O\subseteq W_i$ y da la vecindad del punto.

Para el índice fijado, la representación relativa aporta un abierto $O$ que contiene al punto. Una entrada de $O$ dentro de $K$ está en $A_i$; una fuera está en el complemento que ya forma parte de $W_i$. Así todo $O$ queda dentro de $W_i$ y proporciona la vecindad real requerida.

### Microcontrol 044

[]{#MA-MIC-ANM-01-016-044}

[]{#MA-MSOL-ANM-01-016-044}

**Pregunta.** ¿Se eligió una familia de abiertos ambientes $O_i$?

**Solución.** No. La familia $W_i$ se define directamente por fórmula única. Un ambiente $O$ se usa sólo para probar apertura en el índice considerado, sin reunir elecciones simultáneas.

Cada $W_i$ queda determinado por operaciones de conjuntos sobre $K$ y $A_i$, sin un testigo elegido adicional. Para acreditar que es abierto se puede usar un abierto representante del índice que se esté considerando. La prueba universal de apertura no necesita guardar todos esos representantes como una familia seleccionada.

### Microcontrol 045

[]{#MA-MIC-ANM-01-016-045}

[]{#MA-MSOL-ANM-01-016-045}

**Pregunta.** ¿Qué identidad permite devolver una subcubierta finita a las salidas?

**Solución.** $K\cap W_i=A_i$. Si $x\in K$ está cubierto por $W_i$, pertenece a la preimagen $A_i$ y su salida está en $V_i$.

Al intersectar con $K$, desaparece el complemento y queda exactamente la preimagen relativa. Por tanto el índice que cubre una entrada del compacto también cubre su salida con el abierto original correspondiente. La reducción conserva los mismos índices al volver a las salidas. Esto es lo que convierte la compacidad de entradas en compacidad de la imagen.

### Microcontrol 046

[]{#MA-MIC-ANM-01-016-046}

[]{#MA-MSOL-ANM-01-016-046}

**Pregunta.** ¿Se necesita una inversa funcional para cubrir cada salida de $f[K]$?

**Solución.** No. Para cada salida fijada, pertenencia a la imagen garantiza una entrada testigo. Se obtiene un índice finito que cubre esa entrada y por ello la salida.

Para una salida concreta tomamos una entrada que la alcance, cuya existencia ya está incluida en pertenecer a $f[K]$. Esa entrada está cubierta por uno de los índices finitos seleccionados. El cálculo de preimágenes coloca la salida en su abierto. No importa si otras entradas alcanzan la misma salida: la inyectividad no interviene.

### Microcontrol 047

[]{#MA-MIC-ANM-01-016-047}

[]{#MA-MSOL-ANM-01-016-047}

**Pregunta.** ¿La imagen compacta de una continua implica dominio compacto?

**Solución.** No. Una constante en $\mathbb R$ tiene imagen singleton compacta, pero $\mathbb R$ no es compacto.

La función constante borra toda la diferencia de tamaño entre las entradas y su imagen. Su error de salida siempre es cero, así conserva continuidad en la recta. El singleton de salida tiene reducciones finitas para toda cubierta, pero el dominio admite una cubierta creciente sin reducción. Preservación de imagen es una implicación que no puede invertirse así.

### Microcontrol 048

[]{#MA-MIC-ANM-01-016-048}

[]{#MA-MSOL-ANM-01-016-048}

**Pregunta.** ¿La preimagen de un compacto por una continua siempre es compacta?

**Solución.** No. Para la constante cero en $\mathbb R$, la preimagen del singleton compacto $\{0\}$ es toda la recta. Hace falta información adicional del dominio.

La fibra de cero de la constante es el dominio entero, pues todas las entradas cumplen la condición de salida. La cerradura de esa fibra no basta para compacidad cuando el dominio es no acotado. Más adelante, si el dominio fuera compacto, la preimagen de un cerrado sí heredaría compacidad. Ese dato de dominio es justamente el que falta aquí.

## §16.7 — Por qué los extremos llegan a alcanzarse

### Microcontrol 049

[]{#MA-MIC-ANM-01-016-049}

[]{#MA-MSOL-ANM-01-016-049}

[]{#MA-SEC-ANM-01-016-007}

**Pregunta.** ¿Qué diferencia hay entre supremo de una imagen y máximo alcanzado?

**Solución.** El supremo es la menor cota superior; ser máximo exige además pertenecer a la imagen. La identidad en $(0,1)$ tiene supremo $1$ pero no lo alcanza.

La completitud da un número que domina las salidas y es óptimo entre las cotas, pero no una entrada que lo produzca. Para pasar a máximo hay que probar que ese número está en la imagen. En $(0,1)$, todas las salidas quedan por debajo de uno y se aproximan a él, sin alcanzarlo. Weierstrass añade el argumento de pertenencia mediante compacidad.

### Microcontrol 050

[]{#MA-MIC-ANM-01-016-050}

[]{#MA-MSOL-ANM-01-016-050}

**Pregunta.** ¿Por qué el supremo de un compacto no vacío pertenece al conjunto?

**Solución.** Si quedara fuera, cerradura daría una bola exterior; la propiedad aproximante del supremo daría un punto del conjunto dentro de esa bola, contradicción.

La acotación y no vacuidad permiten formar el supremo $M$. Si fuera exterior, la cerradura ofrecería un radio $r$ que evita el conjunto. La minimalidad de $M$ produce un miembro mayor que $M-r/2$ y menor o igual que $M$, dentro de esa bola. La contradicción obliga a pertenencia y convierte la cota en máximo.

### Microcontrol 051

[]{#MA-MIC-ANM-01-016-051}

[]{#MA-MSOL-ANM-01-016-051}

**Pregunta.** ¿Cómo se prueba la pertenencia del ínfimo sin seleccionar una sucesión?

**Solución.** Si $m$ estuviera fuera, una bola de radio $s$ no tocaría el conjunto. Como $m+s/2$ no es cota inferior, existe un punto entre $m$ y $m+s/2$ del conjunto, que invade esa bola.

La optimalidad de la cota inferior produce una entrada menor que cualquier umbral estrictamente superior a $m$. Como $m$ sigue siendo cota inferior, esa entrada queda a distancia menor que $s/2$ de él. Invade la bola exterior y fuerza pertenencia. Se usa un testigo concreto para un radio, no una selección numerable de aproximaciones.

### Microcontrol 052

[]{#MA-MIC-ANM-01-016-052}

[]{#MA-MSOL-ANM-01-016-052}

**Pregunta.** ¿Dónde se usa que el dominio de Weierstrass sea no vacío?

**Solución.** Para que la imagen sea no vacía y admita supremo/ínfimo reales como extremos, y para que existan entradas minimizadoras y maximizadoras. El vacío compacto no tiene esas entradas.

Una continua en dominio vacío tiene imagen vacía, aunque ambos conjuntos sean compactos. No hay entrada que pueda alcanzar un extremo real. En el caso no vacío, pertenecer el mínimo y máximo a la imagen proporciona entradas que los alcanzan. Esa última obligación explica por qué no vacuidad debe conservarse en el enunciado.

### Microcontrol 053

[]{#MA-MIC-ANM-01-016-053}

[]{#MA-MSOL-ANM-01-016-053}

**Pregunta.** ¿Weierstrass obliga a que los puntos extremos sean extremos del dominio?

**Solución.** No. $(x-1)^2$ en $[0,3]$ tiene mínimo en el punto interior $1$. Se garantizan puntos que alcanzan los valores globales, no una posición prefijada.

La expresión es un cuadrado y por ello no negativa; en uno vale cero, su menor valor posible. Ese argumento está en el interior de $[0,3]$. Weierstrass garantiza existencia de extremizadores globales, pero encontrarlos requiere estudiar la función. Evaluar sólo los extremos del dominio no bastaría para detectar este mínimo.

### Microcontrol 054

[]{#MA-MIC-ANM-01-016-054}

[]{#MA-MSOL-ANM-01-016-054}

**Pregunta.** ¿Puede haber varios minimizadores y maximizadores?

**Solución.** Sí. Para $x^2$ en $\{-1,1\}$ ambas entradas dan $1$, de modo que ambos puntos minimizan y maximizan.

Cada salida en el ejemplo es uno, así todo argumento cumple simultáneamente la desigualdad de mínimo y la de máximo. Compacidad y continuidad acreditan existencia, pero no inyectividad ni unicidad de las fibras extremas. Tampoco se exige que el mínimo y máximo tengan valores distintos.

### Microcontrol 055

[]{#MA-MIC-ANM-01-016-055}

[]{#MA-MSOL-ANM-01-016-055}

**Pregunta.** ¿Qué añade conexidad a la imagen compacta de un segmento?

**Solución.** C15 dice que es intervalo; C16 da extremos globales alcanzados $m,M$. Juntas las propiedades identifican la imagen como $[m,M]$, sin atribuir esos valores a los extremos del dominio.

Compacidad de la imagen proporciona valores $m,M$ alcanzados y encierra todas las salidas entre ellos. Conexidad de la imagen, por ser continua sobre un segmento, incluye todos los valores entre esos dos. Las dos inclusiones dan igualdad con $[m,M]$. Sin conexidad, una imagen compacta podría conservar un hueco entre sus extremos.

### Microcontrol 056

[]{#MA-MIC-ANM-01-016-056}

[]{#MA-MSOL-ANM-01-016-056}

**Pregunta.** ¿Una función acotada en $[0,1]$ tiene máximo aunque no sea continua?

**Solución.** No necesariamente. Si vale $x$ para $x<1$ y cero en $1$, su imagen es $[0,1)$ y no tiene máximo. La función es discontinua en el extremo $1$.

La imagen propuesta es $[0,1)$: el valor nuevo en uno repite cero y no añade el valor límite uno. Cada salida tiene otra mayor en la imagen, así no existe máximo aunque esté acotada. La discontinuidad en uno impide aplicar preservación de compactos a la imagen. El dominio compacto por sí solo no garantiza extremos de una función arbitraria.

## §16.8 — Márgenes positivos e inversas sobre compactos

### Microcontrol 057

[]{#MA-MIC-ANM-01-016-057}

[]{#MA-MSOL-ANM-01-016-057}

[]{#MA-SEC-ANM-01-016-008}

**Pregunta.** ¿Qué función recibe Weierstrass para obtener un margen positivo de una continua sin ceros?

**Solución.** $|f|$, continua por C14. Su mínimo se alcanza en $x_0\in K$ y vale $|f(x_0)|>0$ porque no hay ceros.

Se aplica Weierstrass a la función magnitud, no se toma simplemente el ínfimo y se supone positivo. El mínimo alcanzado tiene la forma $|f(x_0)|$, y ausencia de ceros lo hace estrictamente positivo. Para todo $x\in K$ queda $|f(x)|\ge m>0$. Así una propiedad puntual en cada entrada se convierte en un margen común.

### Microcontrol 058

[]{#MA-MIC-ANM-01-016-058}

[]{#MA-MSOL-ANM-01-016-058}

**Pregunta.** ¿Qué cota da ese margen $m>0$ al recíproco?

**Solución.** $|1/f(x)|=1/|f(x)|\le1/m$ para todos los puntos del compacto. No ceros asegura que el recíproco esté definido en todo el dominio.

Para números positivos, invertir una desigualdad invierte su sentido. Del margen $|f(x)|\ge m>0$ obtenemos la cota superior del recíproco. La misma constante vale para todas las entradas del compacto. La positividad del margen protege tanto la definición del recíproco como su acotación global.

### Microcontrol 059

[]{#MA-MIC-ANM-01-016-059}

[]{#MA-MSOL-ANM-01-016-059}

**Pregunta.** ¿Una función positiva en $(0,1]$ tiene siempre cota inferior positiva?

**Solución.** No. La identidad es positiva pero sus valores $1/(n+1)$ tienden a cero. El dominio no es compacto; falta la hipótesis que garantiza alcanzar un mínimo positivo.

La identidad nunca se anula en ese dominio, pero puede acercarse arbitrariamente a cero. Cualquier candidato $m>0$ es infringido por algún recíproco menor que él. Falta cerradura del dominio y por ello compacidad. La no anulación local no basta para una barrera común positiva en un conjunto no compacto.

### Microcontrol 060

[]{#MA-MIC-ANM-01-016-060}

[]{#MA-MSOL-ANM-01-016-060}

**Pregunta.** ¿Qué función proporciona un punto del compacto más próximo a un real $p$?

**Solución.** $x\mapsto|x-p|$, continua. Weierstrass da un minimizador; si $p$ está fuera de $K$, el mínimo alcanzado no puede ser cero y es positivo.

La función distancia es continua y toma valores no negativos. En un compacto no vacío alcanza su menor valor en una entrada concreta $x_0$. Si $p$ está fuera, esa entrada no puede ser $p$, y la distancia mínima es positiva. Si $p$ pertenece al compacto, la evaluación en $p$ alcanza cero y la distancia mínima es cero.

### Microcontrol 061

[]{#MA-MIC-ANM-01-016-061}

[]{#MA-MSOL-ANM-01-016-061}

**Pregunta.** ¿El punto más próximo tiene que ser único?

**Solución.** No. Para $K=\{-1,1\}$ y $p=0$, ambos puntos tienen distancia mínima $1$. Se garantiza existencia, no una selección única.

El ejemplo tiene dos entradas distintas a la misma distancia del punto exterior. Ambas satisfacen la desigualdad de minimización respecto de todo el conjunto. El teorema ofrece algún minimizador, pero no una regla que escoja uno de manera única para cada $p$. La existencia y la unicidad son conclusiones diferentes.

### Microcontrol 062

[]{#MA-MIC-ANM-01-016-062}

[]{#MA-MSOL-ANM-01-016-062}

**Pregunta.** ¿Por qué la fibra de un valor por una continua en un compacto es compacta?

**Solución.** El singleton de salida es cerrado real, su preimagen es cerrada relativa al compacto por C14 y R3 la hace compacta. Se incluye la fibra vacía.

La fibra se define como todas las entradas con una salida fijada. Continuidad la hace cerrada en el ambiente $K$, y la compacidad del ambiente permite transmitir esa propiedad. Si el valor no se alcanza, la fibra es vacía y también compacta. No se necesita que la fibra sea conexa ni que la función sea inyectiva.

### Microcontrol 063

[]{#MA-MIC-ANM-01-016-063}

[]{#MA-MSOL-ANM-01-016-063}

**Pregunta.** ¿Qué identidad demuestra continuidad de la inversa de una inyección continua compacta?

**Solución.** Para todo cerrado relativo $A\subseteq K$, $h^{-1}[A]=f[A]$. El conjunto $A$ es compacto, su imagen también y por ello es cerrada relativa a $H=f[K]$. El criterio de preimágenes cerradas de C14 da continuidad de $h$.

Una salida pertenece a $h^{-1}[A]$ exactamente cuando su entrada recuperada pertenece a $A$, es decir cuando fue producida desde $A$. La biyección hacia la imagen acredita esa identidad. Cada cerrado relativo de entradas es compacto, y su imagen compacta es cerrada real y por tanto relativa a $H$. Así se cumple el criterio de continuidad de la inversa para todos los cerrados de su codominio.

### Microcontrol 064

[]{#MA-MIC-ANM-01-016-064}

[]{#MA-MSOL-ANM-01-016-064}

**Pregunta.** ¿La prueba de esa inversa necesita intervalo o continuidad uniforme?

**Solución.** No. Usa compacidad de cerrados relativos, imagen compacta y criterio de continuidad por cerrados. Puede haber un dominio roto; continuidad uniforme/Heine–Cantor quedan para C17.

El argumento no diseña barreras de orden entre puntos del dominio. Transporta cerrados mediante compacidad y los identifica con preimágenes de la inversa. Por eso funciona en compactos separados y no requiere monotonía global. La continuidad uniforme es otra conclusión y no debe anticiparse como premisa para esta prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)
