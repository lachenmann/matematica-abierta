---
content-id: MA-BCH-0265
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-015-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 15
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C15_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Ejercicios](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §15.1 — Qué tendría que hacer una separación

### Microcontrol 001

[]{#MA-MIC-ANM-01-015-001}

[]{#MA-MSOL-ANM-01-015-001}

[]{#MA-SEC-ANM-01-015-001}

**Pregunta.** ¿Qué cuatro condiciones conjuntistas acompañan la apertura relativa en una separación?

**Solución.** No vacuidad de ambas partes, disjunción, cobertura del conjunto y pertenencia de las partes al conjunto ambiente. Junto a la apertura relativa, se escriben $A,B\subseteq E$, $A,B\ne\varnothing$, $A\cap B=\varnothing$, $A\cup B=E$.

La cobertura garantiza que cada entrada queda en alguna parte, y la disjunción que no queda en ambas. La no vacuidad evita la partición trivial en todo el conjunto y vacío. La pertenencia al ambiente impide añadir puntos exteriores. Después debe comprobarse apertura relativa de las dos partes: sin ese control local, las cuatro condiciones sólo describen una partición.

### Microcontrol 002

[]{#MA-MIC-ANM-01-015-002}

[]{#MA-MSOL-ANM-01-015-002}

**Pregunta.** ¿Por qué $[-2,-1]$ puede ser una parte abierta relativa de $[-2,-1]\cup[1,2]$?

**Solución.** Es la intersección del ambiente con el abierto real $(-\infty,0)$. La apertura se mide dentro del ambiente, aunque el segmento no sea abierto real.

Si una entrada del segmento está suficientemente cerca de otra entrada del ambiente, no puede saltar a la pieza positiva, separada por un hueco. El abierto real usado para representar la parte puede contener números ajenos al ambiente; el recorte los elimina. Así los extremos del segmento no impiden apertura relativa, aunque sí impiden apertura del segmento en la recta completa.

### Microcontrol 003

[]{#MA-MIC-ANM-01-015-003}

[]{#MA-MSOL-ANM-01-015-003}

**Pregunta.** ¿Dónde falla la partición $[-1,0)$ y $[0,1]$ de $[-1,1]$?

**Solución.** La segunda parte no es abierta relativa en cero: dado $r>0$, $-\min(r/2,1/2)$ pertenece al ambiente, dista menos que $r$ de cero y no pertenece a $[0,1]$.

El testigo propuesto es negativo, pertenece a $[-1,1]$ y está dentro de la bola de radio $r$ de cero porque su magnitud es a lo sumo $r/2<r$. No pertenece a la parte no negativa. Esto funciona para todo radio y niega exactamente la existencia de una bola relativa interior en cero. Las demás condiciones de partición siguen cumpliéndose.

### Microcontrol 004

[]{#MA-MIC-ANM-01-015-004}

[]{#MA-MSOL-ANM-01-015-004}

**Pregunta.** ¿Qué complemento convierte una parte abierta y cerrada relativa en una separación candidata?

**Solución.** $E\setminus A$. Si $A$ es propia y no vacía, el complemento también es no vacío; la cerradura relativa de $A$ significa que ese complemento es abierto relativo. Disjunción y cobertura son identidades de complementos.

Ser propia significa $A\ne E$ y da alguna entrada en $E\setminus A$. Ser cerrada relativa significa que este complemento es abierto en el mismo ambiente, mientras la apertura de $A$ está dada. Por ello ambas partes satisfacen todos los requisitos. En una separación, recíprocamente, cada parte es complemento de la otra y resulta también cerrada relativa.

### Microcontrol 005

[]{#MA-MIC-ANM-01-015-005}

[]{#MA-MSOL-ANM-01-015-005}

**Pregunta.** ¿El vacío es conexo bajo la definición adoptada?

**Solución.** Sí. Toda parte del vacío es vacía, y no pueden existir las dos partes no vacías exigidas por una separación.

La definición de conexidad afirma que no existe una separación, en lugar de exigir un punto testigo. Por eso también puede cumplirse cuando no hay entradas. Si se exigiera no vacuidad como parte de otra convención, cambiaría la conclusión, pero en este capítulo la no vacuidad corresponde a las dos partes de una separación, no al conjunto conexo.

### Microcontrol 006

[]{#MA-MIC-ANM-01-015-006}

[]{#MA-MSOL-ANM-01-015-006}

**Pregunta.** ¿Hace falta que un singleton sea abierto real para probar que es conexo?

**Solución.** No. Sus únicos subconjuntos son el vacío y él mismo; no admite dos partes disjuntas no vacías. La apertura real del singleton no interviene.

Si ambas partes no vacías de una partición del singleton contuvieran su única entrada, se intersectarían. Si una no la contuviera, sería vacía. Es imposible satisfacer simultáneamente no vacuidad y disjunción, antes incluso de estudiar apertura. La prueba funciona en cualquier ambiente que contenga ese punto.

### Microcontrol 007

[]{#MA-MIC-ANM-01-015-007}

[]{#MA-MSOL-ANM-01-015-007}

**Pregunta.** ¿Basta dibujar una partición de dos colores para negar conexidad?

**Solución.** No. Hay que demostrar apertura relativa de ambas partes y verificar no vacuidad, disjunción y cobertura. Una frontera mal asignada puede impedir la apertura de una parte.

En un intervalo podemos asignar cada punto a un color sin producir una separación topológica. La parte que recibe la frontera puede tener entradas del otro color arbitrariamente próximas. Para negar conexidad hay que proporcionar una bola relativa interior en cada punto de cada parte, además de las condiciones conjuntistas. El dibujo sólo sugiere dónde intentar esos controles.

### Microcontrol 008

[]{#MA-MIC-ANM-01-015-008}

[]{#MA-MSOL-ANM-01-015-008}

**Pregunta.** ¿Qué niega exactamente la afirmación «$E$ es conexo»?

**Solución.** Niega la existencia de cualquier par que satisfaga todas las condiciones de separación; no niega la existencia de particiones arbitrarias. Un intervalo sí admite particiones, pero ninguna con ambas partes abiertas relativas y no vacías.

La afirmación es universal sobre todas las posibles parejas de partes: ninguna satisface el conjunto completo de requisitos. Comprobar que una partición particular falla no acredita conexidad, pues podría existir otra separación. En cambio, para refutar conexidad basta exhibir una única pareja válida y demostrar todas sus condiciones.

## §15.2 — El supremo impide romper un intervalo

### Microcontrol 009

[]{#MA-MIC-ANM-01-015-009}

[]{#MA-MSOL-ANM-01-015-009}

[]{#MA-SEC-ANM-01-015-002}

**Pregunta.** ¿Qué definición de intervalo incluye las semirrectas y el vacío?

**Solución.** La condición $a,b\in I$, $a\le b\Rightarrow[a,b]\subseteq I$. En el vacío no hay pares y la condición es vacía; en una semirrecta todo punto entre dos miembros satisface la misma desigualdad que define la semirrecta.

Esta formulación usa únicamente puntos ya presentes y todos los puntos entre ellos. No pide extremos globales alcanzados ni acotación. Si ambos puntos coinciden, el segmento es un singleton; si no hay puntos, no existe un par que infrinja la condición. Así la misma definición cubre intervalos abiertos, cerrados, no acotados y degenerados.

### Microcontrol 010

[]{#MA-MIC-ANM-01-015-010}

[]{#MA-MSOL-ANM-01-015-010}

**Pregunta.** ¿Por qué $S=A\cap[a,b]$ tiene supremo en la prueba R2?

**Solución.** Contiene $a$ y está acotado superiormente por $b$. La completitud real da un supremo para todo conjunto real no vacío acotado superiormente.

Antes de escribir $\sup S$ comprobamos las dos premisas de completitud por separado. La pertenencia de $a$ aporta no vacuidad; la inclusión en $[a,b]$ aporta la cota superior. No se exige que todo $A$ sea acotado. Este recorte es lo que permite aplicar completitud incluso si el intervalo original se extiende indefinidamente.

### Microcontrol 011

[]{#MA-MIC-ANM-01-015-011}

[]{#MA-MSOL-ANM-01-015-011}

**Pregunta.** ¿Dónde se usa que el dominio sea intervalo para ubicar la frontera $c$?

**Solución.** De $a\le c\le b$ y $a,b\in I$ se deduce $c\in[a,b]\subseteq I$. Sin esa inclusión la cobertura por las dos partes no permitiría asignar $c$ a una de ellas.

El supremo es un real por completitud, pero esa existencia no asegura por sí sola que sea una entrada del dominio. La condición intervalar completa la justificación al incluir todos los reales entre $a$ y $b$. Sólo después puede usarse $I=A\cup B$ para dividir el argumento en los dos casos. Separar existencia de pertenencia evita un paso inválido en dominios con huecos.

### Microcontrol 012

[]{#MA-MIC-ANM-01-015-012}

[]{#MA-MSOL-ANM-01-015-012}

**Pregunta.** Si $c\in A$, ¿por qué $b-c$ es positivo?

**Solución.** $b\in B$ y la disjunción impiden $c=b$; además $c\le b$ por la cota del supremo. Por tanto $c<b$.

Si $c=b$, la pertenencia de $c$ a $A$ y de $b$ a $B$ daría una entrada común, prohibida por disjunción. La cota $c\le b$ deja entonces la desigualdad estricta. Esa positividad permite diseñar un avance que permanezca en el segmento; no sería legítimo dividir la distancia restante y afirmar un avance positivo antes de verificarla.

### Microcontrol 013

[]{#MA-MIC-ANM-01-015-013}

[]{#MA-MSOL-ANM-01-015-013}

**Pregunta.** ¿Qué dos controles satisface $h=\min((b-c)/2,r/2)$?

**Solución.** Es positivo, no avanza hasta $b$ y es menor que $r$. Así $c+h$ pertenece al segmento original y a la vecindad relativa de $c$; ambas pertenencias son necesarias para concluir que está en $A$.

Los dos números del mínimo son positivos, así $h>0$. Además $h\le(b-c)/2<b-c$ y $h\le r/2<r$. La primera desigualdad mantiene $c+h$ entre $c$ y $b$, dentro de $I$; la segunda lo mantiene en la ventana que garantiza pertenencia a $A$. El nuevo punto pertenece a $S$ y supera su cota superior $c$, que es la contradicción.

### Microcontrol 014

[]{#MA-MIC-ANM-01-015-014}

[]{#MA-MSOL-ANM-01-015-014}

**Pregunta.** Si $c\in B$, ¿por qué existe $t\in S$ mayor que $c-s/2$?

**Solución.** El número $c-s/2<c$ no puede ser cota superior de $S$, pues $c$ es la menor cota superior. La negación de ser cota da un $t\in S$ con $t>c-s/2$, y $t\le c$ por ser $c$ cota.

Para cualquier tolerancia positiva por debajo de $c$, la minimalidad del supremo impide que ese umbral sea una cota superior. Aquí se usa el umbral $c-s/2$, de modo que la entrada encontrada está a distancia menor que $s$ de $c$. Como está en $S\subseteq A$, la apertura de $B$ la colocaría también en $B$, contradiciendo disjunción.

### Microcontrol 015

[]{#MA-MIC-ANM-01-015-015}

[]{#MA-MSOL-ANM-01-015-015}

**Pregunta.** ¿Se supone en R2 que $c$ sea máximo de $S$?

**Solución.** No. Si $c$ está en $B$, ni siquiera pertenece a $S\subseteq A$. Se usa la aproximación por debajo del supremo, no la existencia de un máximo.

Un máximo es un miembro del conjunto que domina a todos los demás; un supremo sólo es la menor cota superior. La prueba conserva esa diferencia: en el caso $c\in B$ obtiene miembros próximos por debajo, sin asignar $c$ a $S$. Pedir un máximo impediría tratar precisamente ese caso y añadiría una hipótesis no demostrada.

### Microcontrol 016

[]{#MA-MIC-ANM-01-015-016}

[]{#MA-MSOL-ANM-01-015-016}

**Pregunta.** ¿Se necesita compacidad del intervalo original para R2?

**Solución.** No. Se acota sólo el auxiliar $S$ entre dos puntos concretos. Supremo, propiedad intervalar y apertura relativa bastan, incluso para intervalos no acotados.

Después de suponer una separación basta fijar un punto de cada parte y recortar entre ellos. Toda la estimación ocurre en ese segmento, aunque el dominio sea la recta o una semirrecta. No se extrae una subcobertura ni una subsucesión. El recurso global utilizado es completitud real aplicada al auxiliar acotado, seguido de dos controles locales de apertura.

## §15.3 — Un hueco produce dos lados

### Microcontrol 017

[]{#MA-MIC-ANM-01-015-017}

[]{#MA-MSOL-ANM-01-015-017}

[]{#MA-SEC-ANM-01-015-003}

**Pregunta.** ¿Qué omisión permite construir un corte que separa un conjunto?

**Solución.** Un $c\notin E$ situado estrictamente entre dos puntos $a<b$ de $E$. Una omisión fuera de todos sus puntos no asegura dos partes no vacías.

La posición estrictamente intermedia aporta entradas presentes a ambos lados. La ausencia de $c$ permite que los rayos abiertos cubran todas las entradas sin dejar ninguna en la frontera. Si el punto omitido estuviera a la izquierda o derecha de todo el conjunto, uno de los recortes podría ser vacío y no tendríamos una separación.

### Microcontrol 018

[]{#MA-MIC-ANM-01-015-018}

[]{#MA-MSOL-ANM-01-015-018}

**Pregunta.** ¿Por qué las partes $E\cap(-\infty,c)$ y $E\cap(c,\infty)$ cubren $E$?

**Solución.** Como $c\notin E$, todo $x\in E$ es distinto de $c$. La tricotomía deja sólo $x<c$ o $x>c$.

Los dos rayos no incluyen la frontera $c$, y por eso su unión no es toda la recta. Al recortarlos por $E$, el único punto que podría faltar ya estaba ausente. La cobertura se prueba entrada por entrada usando tricotomía. Si $c$ perteneciera a $E$, estos dos recortes dejarían fuera esa entrada y no formarían una separación.

### Microcontrol 019

[]{#MA-MIC-ANM-01-015-019}

[]{#MA-MSOL-ANM-01-015-019}

**Pregunta.** ¿Qué testigos aseguran la no vacuidad de ambos lados del corte?

**Solución.** Los puntos dados $a<c<b$: $a$ está en el lado izquierdo y $b$ en el derecho.

No basta que los rayos reales sean no vacíos: sus recortes con el dominio podrían no serlo. Las entradas $a$ y $b$ verifican no vacuidad de los recortes efectivos. Además, las desigualdades opuestas garantizan disjunción y los rayos aportan apertura relativa. Así cada requisito se vincula con un dato concreto de la construcción.

### Microcontrol 020

[]{#MA-MIC-ANM-01-015-020}

[]{#MA-MSOL-ANM-01-015-020}

**Pregunta.** ¿La densidad de $\mathbb Q$ implica su conexidad?

**Solución.** No. $\sqrt2$ es un punto real entre $1$ y $2$ que no es racional. Los racionales menores y mayores que ese corte forman una separación; aproximarse al corte no lo incluye en el dominio.

Densidad significa que los racionales visitan todo intervalo abierto real, no que contengan todos los puntos entre dos miembros. En el corte irracional, cada racional pertenece exactamente a un lado; ambos lados son abiertos relativos y contienen $1$ o $2$. Los racionales pueden aproximarse a la frontera sin que ésta sea una entrada que conecte las partes.

### Microcontrol 021

[]{#MA-MIC-ANM-01-015-021}

[]{#MA-MSOL-ANM-01-015-021}

**Pregunta.** ¿Por qué una intersección de intervalos es intervalo?

**Solución.** Si $a,b$ pertenecen a todos los miembros, cada miembro contiene $[a,b]$, luego la intersección también lo contiene. Si la intersección es vacía, la condición entre pares se cumple vacíamente.

Para verificar la condición intervalar tomamos un par de la intersección y un punto entre ellos. En cada intervalo ese punto pertenece por intervalaridad, por lo que pertenece a todos y a su intersección. No se requiere seleccionar extremos de los miembros. Con la convención de familia vacía, la intersección es la recta completa y también satisface la condición.

### Microcontrol 022

[]{#MA-MIC-ANM-01-015-022}

[]{#MA-MSOL-ANM-01-015-022}

**Pregunta.** ¿Qué ocurre al unir $(0,1)$ y $(2,3)$?

**Solución.** La unión omite, por ejemplo, $3/2$ entre los puntos presentes $1/2$ y $5/2$. No es intervalo y por R3 no es conexa.

El corte $3/2$ deja una parte a cada lado, ambas abiertas relativas y con entradas dadas. Como el corte falta, esas partes cubren la unión y son disjuntas. Los intervalos originales son conexos individualmente, pero esa propiedad no obliga a la unión a contener los puntos entre piezas distintas.

### Microcontrol 023

[]{#MA-MIC-ANM-01-015-023}

[]{#MA-MSOL-ANM-01-015-023}

**Pregunta.** ¿Por qué un punto común ayuda a unir dos conexos?

**Solución.** En una supuesta separación de la unión, cada conexo debe quedar en una sola parte. El punto común obliga a que ambos queden en la misma, dejando vacía la otra parte.

Al intersectar las partes de la separación con uno de los conexos obtenemos partes abiertas relativas, disjuntas y que lo cubren. Si ambas fueran no vacías lo separarían, así debe quedar entero de un lado. La entrada compartida pertenece al mismo lado para los dos conjuntos. Por ello toda la unión queda allí, contradiciendo no vacuidad del otro lado.

### Microcontrol 024

[]{#MA-MIC-ANM-01-015-024}

[]{#MA-MSOL-ANM-01-015-024}

**Pregunta.** ¿La intersección no vacía es necesaria para que dos intervalos tengan unión conexa?

**Solución.** No. $[0,1)$ y $[1,2]$ son disjuntos, pero su unión es $[0,2]$, que es intervalo y conexo. La condición de punto común es suficiente, no necesaria.

El punto uno no pertenece a la primera pieza pero sí a la segunda. Así no falta en la unión y tampoco hay otros huecos entre cero y dos. La unión es un intervalo aunque las piezas no se intersecten. No podemos aplicar directamente el criterio de punto común, pero sí comprobar intervalaridad y usar R2.

## §15.4 — La continuidad transporta la imposibilidad de separar

### Microcontrol 025

[]{#MA-MIC-ANM-01-015-025}

[]{#MA-MSOL-ANM-01-015-025}

[]{#MA-SEC-ANM-01-015-004}

**Pregunta.** ¿Qué operación de conjuntos usa la continuidad para transportar una separación de la imagen?

**Solución.** Preimágenes. Si las partes de la imagen son $H\cap V$ y $H\cap W$, sus preimágenes por $h:E\to\mathbb R$ son $h^{-1}[V]$ y $h^{-1}[W]$, abiertas relativas a $E$.

La apertura de una parte de la imagen se expresa como recorte por un abierto real. Como todas las evaluaciones están en la imagen, tomar su preimagen equivale a tomar la del abierto real entero. El criterio de C14 da apertura relativa de las entradas seleccionadas. Se transporta una separación hacia atrás; no se afirma que las imágenes de abiertos sean abiertas.

### Microcontrol 026

[]{#MA-MIC-ANM-01-015-026}

[]{#MA-MSOL-ANM-01-015-026}

**Pregunta.** ¿Por qué se restringe $f$ al conexo $E\subseteq D$?

**Solución.** Así la función $h=f\upharpoonright E$ tiene exactamente el ambiente de entradas que queremos separar. Su continuidad se hereda de $f$ y su imagen es $f[E]$.

Las preimágenes deben tener ambiente $E$, pues la contradicción buscada es una separación de $E$. Usar todo $D$ podría producir una separación de un dominio que no se ha supuesto conexo. Restringir la función conserva continuidad relativa y hace que sus valores alcanzados sean exactamente los que aparecen en la separación hipotética de $f[E]$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-015-027}

[]{#MA-MSOL-ANM-01-015-027}

**Pregunta.** ¿Qué garantiza que la preimagen de una parte no vacía de $f[E]$ sea no vacía?

**Solución.** Que sus valores pertenecen a la imagen: para un valor concreto $y$ de esa parte existe $x\in E$ con $f(x)=y$. No bastaría que $y$ perteneciera solamente al codominio.

Una preimagen de un subconjunto no vacío del codominio puede ser vacía si la función no alcanza sus valores. Aquí cada valor elegido ya tiene una entrada porque pertenece a $f[E]$. Esa entrada queda en la preimagen de la parte correspondiente. Sólo se necesitan dos testimonios, uno por parte, para verificar no vacuidad.

### Microcontrol 028

[]{#MA-MIC-ANM-01-015-028}

[]{#MA-MSOL-ANM-01-015-028}

**Pregunta.** ¿R4 necesita escoger una entrada para cada valor de la imagen?

**Solución.** No. Para refutar la separación se fijan sólo un valor y una preimagen en cada una de sus dos partes. No se construye un selector global de fibras.

La prueba de no vacuidad trabaja con dos existencias concretas. No necesita reunir una entrada para cada salida ni invertir globalmente una función que podría no ser inyectiva. Las preimágenes se definen como conjuntos de todas las entradas que cumplen la condición. Así el argumento no introduce una selección simultánea de fibras.

### Microcontrol 029

[]{#MA-MIC-ANM-01-015-029}

[]{#MA-MSOL-ANM-01-015-029}

**Pregunta.** ¿La preimagen de un conexo por una función continua tiene que ser conexa?

**Solución.** No. Para $q(x)=x^2$ en $[-2,2]$, $q^{-1}[\{1\}]=\{-1,1\}$, que no es intervalo, aunque $\{1\}$ sí es conexo.

El singleton de salida es un intervalo degenerado y por ello conexo. Su preimagen contiene dos puntos y omite cero entre ellos; el corte por cero la separa. La continuidad de $q$ y la conexidad de su dominio siguen siendo verdaderas. El ejemplo muestra que invertir la dirección del resultado de preservación cambia la afirmación y puede hacerla falsa.

### Microcontrol 030

[]{#MA-MIC-ANM-01-015-030}

[]{#MA-MSOL-ANM-01-015-030}

**Pregunta.** ¿Una imagen singleton prueba que el dominio es conexo?

**Solución.** No. Una función constante en $\{-1,1\}$ es continua en el dominio relativo y tiene imagen singleton, pero el dominio admite un corte por cero.

La constante tiene error cero para cualquier par de entradas, de modo que es continua incluso en este dominio separado. Su imagen olvida la diferencia entre las entradas y queda reducida a un punto. Preservación sólo afirma que un dominio conexo produce una imagen conexa; una imagen conexa puede proceder de un dominio desconexo.

### Microcontrol 031

[]{#MA-MIC-ANM-01-015-031}

[]{#MA-MSOL-ANM-01-015-031}

**Pregunta.** ¿Cómo una separación define una función continua con valores cero y uno?

**Solución.** Se asigna cero a una parte y uno a la otra. En cada punto la apertura relativa da una vecindad donde la función es constante; el error de salida allí es cero para cualquier tolerancia positiva.

La cobertura y la disjunción aseguran que cada entrada recibe exactamente una regla. Para una entrada de $A$, su apertura ofrece una bola relativa contenida en $A$ y por ello salida siempre cero; para una de $B$, siempre uno. Las bolas pueden cambiar con el centro. La no vacuidad de las dos partes garantiza que esta continua no sea constante.

### Microcontrol 032

[]{#MA-MIC-ANM-01-015-032}

[]{#MA-MSOL-ANM-01-015-032}

**Pregunta.** ¿Qué significa «constante» para una función con dominio vacío en este criterio?

**Solución.** Que para todos $x,z$ del dominio se cumple $u(x)=u(z)$. La condición universal es vacía; no se exige un valor alcanzado ni una entrada testigo.

No hay dos entradas del vacío que tengan salidas distintas, por lo que se cumple la igualdad universal. Bajo esta convención el criterio de dos valores incluye el vacío de forma coherente con su conexidad. Pedir además que exista una entrada o un valor alcanzado introduciría un requisito diferente y excluiría innecesariamente ese caso.

## §15.5 — El valor intermedio como consecuencia estructural

### Microcontrol 033

[]{#MA-MIC-ANM-01-015-033}

[]{#MA-MSOL-ANM-01-015-033}

[]{#MA-SEC-ANM-01-015-005}

**Pregunta.** ¿En qué segmento se localiza el testigo del valor intermedio entre $f(u)$ y $f(v)$?

**Solución.** En $[\min(u,v),\max(u,v)]$, contenido en el intervalo de partida. Se aplica preservación a ese segmento, no sólo a todo el dominio.

El segmento entre los dos argumentos está en $I$ y es conexo. Su imagen por la restricción continua es un intervalo que contiene ambas salidas, así también contiene el nivel intermedio. Pertenecer a esa imagen proporciona un argumento dentro del segmento específico. Aplicar el resultado sólo a todo $I$ daría un testigo sin esa localización precisa.

### Microcontrol 034

[]{#MA-MIC-ANM-01-015-034}

[]{#MA-MSOL-ANM-01-015-034}

**Pregunta.** ¿Por qué un nivel estrictamente intermedio no se alcanza en los extremos de ese segmento?

**Solución.** Porque es distinto de $f(u)$ y $f(v)$. Un testigo con esa salida no puede ser $u$ ni $v$, así queda en el interior si son distintos.

Un argumento igual a un extremo produciría su salida extrema, distinta del nivel solicitado. Excluir esos dos argumentos del segmento cerrado deja el segmento abierto entre ellos. La estrictitud se usa para esa exclusión, no para la existencia básica. Si el nivel coincide con una salida extrema, ese extremo ya es un testigo válido.

### Microcontrol 035

[]{#MA-MIC-ANM-01-015-035}

[]{#MA-MSOL-ANM-01-015-035}

**Pregunta.** ¿Qué cambia si sólo se conoce $f(a)\le0\le f(b)$?

**Solución.** Se garantiza un cero en $[a,b]$, que puede estar en un extremo. Para asegurar uno en $(a,b)$ hacen falta signos estrictos opuestos.

Si $f(a)=0$ o $f(b)=0$, la existencia ya queda probada por ese extremo. Si ninguna igualdad ocurre, los signos son estrictamente opuestos y el valor intermedio produce un cero interior. Las desigualdades débiles por sí solas no garantizan interioridad: la función $f(x)=x$ en $[0,1]$ sólo se anula en cero.

### Microcontrol 036

[]{#MA-MIC-ANM-01-015-036}

[]{#MA-MSOL-ANM-01-015-036}

**Pregunta.** ¿Cómo se reduce encontrar $f(x)=y$ a encontrar un cero?

**Solución.** Con $g(x)=f(x)-y$, continua por álgebra de C14. Entonces $g(x)=0$ equivale exactamente a $f(x)=y$ y el dominio no cambia.

Restar una constante conserva continuidad en el mismo dominio. Las desigualdades respecto del nivel $y$ se convierten en signos de $g$: por debajo da negativo y por encima positivo. Encontrar un cero de $g$ resuelve exactamente la ecuación original, sin cambiar sus argumentos ni imponer unicidad.

### Microcontrol 037

[]{#MA-MIC-ANM-01-015-037}

[]{#MA-MSOL-ANM-01-015-037}

**Pregunta.** ¿Qué prueba signo constante de una continua sin ceros en un intervalo no vacío?

**Solución.** Si hubiera dos valores de signos opuestos, R5 produciría un cero entre sus argumentos. Fijando un valor, todos los demás deben tener su mismo signo.

Fijamos una entrada porque el intervalo es no vacío. Su salida no nula tiene uno de los dos signos. Cualquier salida de signo contrario, junto a ella, obligaría a alcanzar cero en el segmento entre sus argumentos. Como no hay ceros, todas las salidas tienen el signo fijado. La conclusión utiliza conexión del dominio, además de estabilidad local del signo.

### Microcontrol 038

[]{#MA-MIC-ANM-01-015-038}

[]{#MA-MSOL-ANM-01-015-038}

**Pregunta.** ¿Por qué $1/x$ no contradice ese resultado al tener ambos signos?

**Solución.** Su dominio $\mathbb R\setminus\{0\}$ no es intervalo. La continuidad se conserva en ese dominio roto, pero falta la hipótesis que conecta los argumentos de signos opuestos.

Entre una entrada negativa y una positiva aparece cero, que el dominio excluye. No podemos restringir $1/x$ al segmento que las une porque la función no está definida en toda esa región. Las dos componentes admiten signos diferentes sin ninguna discontinuidad relativa. Se mantiene continuidad y ausencia de ceros, pero se pierde la hipótesis intervalar.

### Microcontrol 039

[]{#MA-MIC-ANM-01-015-039}

[]{#MA-MSOL-ANM-01-015-039}

**Pregunta.** ¿R5 afirma unicidad del argumento que alcanza un nivel?

**Solución.** No. $x^2$ alcanza $1$ en $-1$ y $1$. La existencia de al menos un argumento se distingue de cualquier prueba adicional de inyectividad o monotonía.

La afirmación de existencia permite uno o varios argumentos con la misma salida. La continuidad controla proximidad y el valor intermedio ausencia de huecos; ninguna de esas propiedades impide fibras con varios miembros. Para obtener unicidad puede demostrarse por separado inyectividad, por ejemplo mediante estricto crecimiento en el dominio pertinente.

### Microcontrol 040

[]{#MA-MIC-ANM-01-015-040}

[]{#MA-MSOL-ANM-01-015-040}

**Pregunta.** ¿La imagen de una continua intervalar tiene necesariamente mínimo y máximo?

**Solución.** No bajo estas hipótesis. La identidad en $(0,1)$ tiene imagen $(0,1)$, sin mínimo ni máximo. R5 prueba ausencia de huecos entre valores alcanzados, no extremos alcanzados.

Que la imagen sea intervalo sólo obliga a incluir los valores entre salidas ya alcanzadas. No obliga a alcanzar su ínfimo o supremo ni a ser acotada. En la identidad sobre $(0,1)$, cada salida tiene otras menores y mayores en la imagen, así no hay extremos. No se ha supuesto compacidad ni se ha probado un teorema de extremos.

## §15.6 — Bisección: existencia, localización y alcance del cálculo

### Microcontrol 041

[]{#MA-MIC-ANM-01-015-041}

[]{#MA-MSOL-ANM-01-015-041}

[]{#MA-SEC-ANM-01-015-006}

**Pregunta.** ¿Cuál es la longitud del encierro después de $n$ actualizaciones de bisección?

**Solución.** Con $L_0=a$, $U_0=b$, es $(b-a)/2^n$, mientras no haya detención por un cero exacto. Cada transición divide por dos la longitud anterior.

En el índice cero todavía no se ha actualizado el encierro y su longitud es $b-a$. Cada paso que continúa conserva una de las dos mitades y multiplica la longitud por $1/2$. La inducción produce el exponente $n$ después de $n$ pasos. Si se detecta un cero exacto, la construcción puede detenerse y ya tenemos el argumento buscado.

### Microcontrol 042

[]{#MA-MIC-ANM-01-015-042}

[]{#MA-MSOL-ANM-01-015-042}

**Pregunta.** ¿Qué extremo se reemplaza cuando $g(M_n)<0$ y los signos iniciales son negativo/positivo?

**Solución.** El inferior: $L_{n+1}=M_n$, $U_{n+1}=U_n$. El nuevo inferior conserva signo negativo y el superior conserva positivo.

El medio pertenece al interior del encierro. Si su salida es negativa, comparte signo con el extremo inferior y puede sustituirlo; el extremo superior positivo permanece. Así el nuevo intervalo mantiene signos opuestos y la mitad de longitud. Si la salida fuera positiva, se reemplazaría el superior; si fuera cero, tendríamos una raíz exacta.

### Microcontrol 043

[]{#MA-MIC-ANM-01-015-043}

[]{#MA-MSOL-ANM-01-015-043}

**Pregunta.** ¿Por qué $U_n$ es cota de todos los extremos inferiores y no sólo de $L_n$?

**Solución.** Para $k\le n$, $L_k\le L_n\le U_n$. Para $k>n$, el anidamiento da $L_k\le U_k\le U_n$. Ambos casos prueban la cota para todo $k$.

Para comparar un extremo inferior cualquiera con $U_n$ dividimos según su índice sea anterior o posterior. Antes de $n$, usamos crecimiento de los inferiores; después, decrecimiento de los superiores y pertenencia del inferior a su propio intervalo. Esos dos casos justifican que el supremo de todos los inferiores quede por debajo de cada $U_n$.

### Microcontrol 044

[]{#MA-MIC-ANM-01-015-044}

[]{#MA-MSOL-ANM-01-015-044}

**Pregunta.** ¿Qué dirección secuencial de continuidad se usa para pasar al cero límite?

**Solución.** La directa: convergencia de entradas a $c$ implica convergencia de salidas a $g(c)$. No se usa la recíproca secuencial ni selección de infractores.

Las sucesiones de extremos ya están definidas por una recurrencia única y sus convergencias se prueban con cotas de longitud. Continuidad se aplica a esas rutas dadas para obtener convergencia de las salidas. No se deduce continuidad de un criterio secuencial ni se elige un testigo por cada escala. Por eso no aparece la hipótesis adicional de selección de infractores.

### Microcontrol 045

[]{#MA-MIC-ANM-01-015-045}

[]{#MA-MSOL-ANM-01-015-045}

**Pregunta.** ¿Cuál es el error posicional máximo del punto medio $M_n$ respecto del cero encerrado?

**Solución.** Como $c\in[L_n,U_n]$, $|M_n-c|\le(U_n-L_n)/2=(b-a)/2^{n+1}$. Es una cota de distancia de argumentos.

El medio divide el encierro en dos distancias iguales. Cualquier punto de ese encierro, incluido el cero límite, dista a lo sumo la mitad de la longitud. Sustituir la fórmula de longitud aporta un factor adicional de dos y el exponente $n+1$. El resultado mide error en el argumento, no en el valor evaluado de la función.

### Microcontrol 046

[]{#MA-MIC-ANM-01-015-046}

[]{#MA-MSOL-ANM-01-015-046}

**Pregunta.** ¿Un encierro pequeño da por sí solo una cota numérica del residual $|g(M_n)|$?

**Solución.** No. Falta control cuantitativo de la variación de $g$. Continuidad permite un radio para una tolerancia dada, pero la longitud sola no proporciona una fórmula universal de residual.

Una función puede cambiar sus salidas muy rápidamente en un encierro pequeño. Por ejemplo, multiplicar una función por una constante positiva no modifica sus ceros ni los signos, pero amplifica el residual. Para una cota explícita de salida haría falta un control cuantitativo adicional, como una estimación de variación. Continuidad cualitativa no convierte la longitud en una fórmula universal.

### Microcontrol 047

[]{#MA-MIC-ANM-01-015-047}

[]{#MA-MSOL-ANM-01-015-047}

**Pregunta.** ¿Un intervalo de evaluación que contiene cero certifica que $g(M_n)=0$?

**Solución.** No. Sólo indica que no se certificó un signo estricto. Puede contener valores positivos o negativos; no autoriza detención por raíz exacta ni actualización de uno de los extremos.

La inclusión certificada afirma que el valor verdadero está en el intervalo de evaluación, pero no que sea cada uno de sus miembros. Si cero está dentro junto a números de ambos signos, el valor aún puede ser positivo, negativo o cero. Sólo un certificado de signo estricto autoriza descartar una mitad según la regla; igualdad exacta exige su propio certificado.

### Microcontrol 048

[]{#MA-MIC-ANM-01-015-048}

[]{#MA-MSOL-ANM-01-015-048}

**Pregunta.** ¿Por qué la recurrencia clásica no es una promesa de algoritmo efectivo para toda función continua?

**Solución.** Las hipótesis no incluyen una evaluación computable ni una decisión efectiva de signos reales exactos. La regla única es válida matemáticamente por tricotomía; una implementación exige certificados de signo.

La tricotomía da matemáticamente un caso único para cada valor real exacto. No proporciona por sí misma un procedimiento que decida ese caso a partir de aproximaciones finitas. Una implementación necesita datos de evaluación y reglas para certificar signos, y puede quedar sin decidir cuando un intervalo de evaluación contiene cero. Esto limita la promesa computacional, sin invalidar la recurrencia matemática.

## §15.7 — Inyectividad, orden y continuidad de la inversa

### Microcontrol 049

[]{#MA-MIC-ANM-01-015-049}

[]{#MA-MSOL-ANM-01-015-049}

[]{#MA-SEC-ANM-01-015-007}

**Pregunta.** ¿Qué condición entre las imágenes de $x<y<z$ inicia la prueba de monotonía?

**Solución.** $f(y)$ está estrictamente entre $f(x)$ y $f(z)$. Un pico o valle permitiría, por R5 en los dos subsegmentos, dos argumentos distintos con una misma salida, violando inyectividad.

La inyectividad hace distintas las tres salidas. Si la central fuese mayor que ambas o menor que ambas, habría un nivel compartido por las imágenes de los dos subsegmentos. El valor intermedio entregaría dos argumentos distintos con ese nivel. Por ello sólo quedan las dos orientaciones estrictamente ordenadas de las tres salidas.

### Microcontrol 050

[]{#MA-MIC-ANM-01-015-050}

[]{#MA-MSOL-ANM-01-015-050}

**Pregunta.** ¿Por qué se escoge un nivel estrictamente entre el pico y ambos extremos?

**Solución.** Para que R5 entregue un punto interior en cada subsegmento. Así los dos testigos son distintos, uno antes de $y$ y otro después, y la contradicción de inyectividad es segura.

Si el nivel coincidiera con la salida central, los dos testigos podrían ser el mismo punto $y$ y no habría contradicción. Al elegirlo estrictamente entre el pico y el mayor de los extremos, se excluyen todos los extremos de ambos subsegmentos. Queda un testigo a cada lado de $y$, necesariamente distinto del otro.

### Microcontrol 051

[]{#MA-MIC-ANM-01-015-051}

[]{#MA-MSOL-ANM-01-015-051}

**Pregunta.** ¿Basta estudiar un único triple para concluir monotonía en todo el intervalo?

**Solución.** No. Se fija un par orientado $a<b$ y se ordenan junto con cualquier par $x<y$. Los triples consecutivos propagan el signo de las diferencias en ese conjunto finito; el par fijado determina la orientación.

La propiedad de triples se aplica a todos los triples de la lista ordenada formada por el par fijado y el par solicitado. Dos diferencias adyacentes tienen el mismo signo en cada triple consecutivo; al enlazarlos, todas comparten orientación. La desigualdad del par fijado decide cuál es ese signo. Así el argumento alcanza pares situados fuera de ese primer segmento.

### Microcontrol 052

[]{#MA-MIC-ANM-01-015-052}

[]{#MA-MSOL-ANM-01-015-052}

**Pregunta.** ¿Qué garantiza que exista una inversa $h:f[I]\to I$?

**Solución.** Inyectividad da unicidad de la entrada por valor; la definición de imagen da existencia para todo valor de $f[I]$. No se requiere sobreyectividad sobre toda $\mathbb R$.

Para cada $y\in f[I]$ existe algún $x\in I$ con $f(x)=y$ por definición de imagen. Inyectividad hace ese $x$ único y permite definir $h(y)$ sin ambigüedad. Un valor real fuera de la imagen no tiene por qué disponer de entrada. Declarar el dominio exacto de la inversa evita confundir invertibilidad sobre la imagen con sobreyectividad real.

### Microcontrol 053

[]{#MA-MIC-ANM-01-015-053}

[]{#MA-MSOL-ANM-01-015-053}

**Pregunta.** ¿Qué hipótesis permite usar $x_0-\varepsilon/2$ como barrera si existe una entrada $x\le x_0-\varepsilon$?

**Solución.** Que $I$ sea intervalo: el punto barrera está entre esa entrada y $x_0$, ambos de $I$. Así la evaluación $f(x_0-\varepsilon/2)$ está definida.

La entrada lejana dada queda a la izquierda de la barrera y el centro a la derecha. Intervalaridad incluye el punto intermedio, habilitando su evaluación. Monotonía convierte entonces esa barrera de argumentos en una separación positiva de salidas. Sin pertenencia de la barrera al dominio, esa diferencia de valores no sería una expresión definida.

### Microcontrol 054

[]{#MA-MIC-ANM-01-015-054}

[]{#MA-MSOL-ANM-01-015-054}

**Pregunta.** ¿Qué se hace si no hay entradas de $I$ menores o iguales que $x_0-\varepsilon$?

**Solución.** No hace falta barrera izquierda porque todas las entradas ya superan ese umbral. Se asigna a ese lado una tolerancia positiva arbitraria, por ejemplo $1$, para formar el mínimo final.

En ese lado no existen argumentos que violen la distancia deseada, de modo que no hay nada que excluir con un control de salidas. La tolerancia arbitraria sólo permite formar un mínimo positivo con la barrera del otro lado. No afirma que la función esté definida en un punto exterior. Este tratamiento incluye centros que son extremos del intervalo.

### Microcontrol 055

[]{#MA-MIC-ANM-01-015-055}

[]{#MA-MSOL-ANM-01-015-055}

**Pregunta.** ¿La inversa continua obtenida requiere una cota lineal inferior de $f$?

**Solución.** No. El radio se obtiene por diferencias positivas de valores en puntos barrera y monotonía. No se supone $|f(x)-f(z)|\ge c|x-z|$ ni derivada no nula.

Fijados centro y precisión, las barreras interiores tienen salidas distintas de la central por monotonía estricta. Sus diferencias positivas sirven como tolerancias y excluyen argumentos demasiado lejanos. La magnitud de esas diferencias puede depender del centro y de la precisión de cualquier manera. La prueba no exige una tasa lineal ni divide por una derivada.

### Microcontrol 056

[]{#MA-MIC-ANM-01-015-056}

[]{#MA-MSOL-ANM-01-015-056}

**Pregunta.** ¿Estricto crecimiento por sí solo excluye saltos?

**Solución.** No. $k(x)=x$ para $x<0$ y $k(x)=x+1$ para $x\ge0$ es estrictamente creciente, pero en cero las salidas por la izquierda se aproximan a cero y $k(0)=1$. Falta continuidad.

Cada rama conserva el orden, y al cruzar cero la salida de la rama derecha supera a toda salida cercana de la izquierda. Eso acredita estricto crecimiento, pero permite un hueco de valores entre cero y uno. Las entradas negativas se aproximan al centro mientras sus salidas no se aproximan a $k(0)$. Monotonía y continuidad son obligaciones distintas.

## §15.8 — Componentes: los intervalos máximos dentro de un dominio

### Microcontrol 057

[]{#MA-MIC-ANM-01-015-057}

[]{#MA-MSOL-ANM-01-015-057}

[]{#MA-SEC-ANM-01-015-008}

**Pregunta.** ¿Qué relación determina las componentes reales sin escoger representantes?

**Solución.** $x\sim y$ si el segmento entre $x$ y $y$ está contenido en $D$. Cada clase $C_x$ se define por esa fórmula; la familia de todas las clases existe como colección de subconjuntos de $D$ determinados por la relación.

La relación examina si todos los puntos entre dos entradas también están disponibles en el dominio. Definir $C_x=\{y\in D:x\sim y\}$ recoge directamente todos los miembros relacionados con $x$. La familia de clases se obtiene reuniendo estas clases para todos los $x\in D$, eliminando repeticiones como conjuntos. No se escoge un representante por clase.

### Microcontrol 058

[]{#MA-MIC-ANM-01-015-058}

[]{#MA-MSOL-ANM-01-015-058}

**Pregunta.** ¿Por qué es transitiva la relación por segmentos?

**Solución.** Los segmentos entre $x,y$ y entre $y,z$ están en $D$ y comparten $y$. Su unión es intervalo y contiene $x,z$, por lo que incluye el segmento entre ellos.

Los dos segmentos compartidos cubren todos los puntos entre el menor y el mayor de $x,y,z$, sea cual sea su orden. Su unión no tiene huecos y está contenida en $D$. Como $x$ y $z$ pertenecen a ella, contiene su segmento. Esto verifica transitividad sin imponer que $y$ esté necesariamente entre $x$ y $z$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-015-059}

[]{#MA-MSOL-ANM-01-015-059}

**Pregunta.** ¿Cómo se prueba la maximalidad conexa de $C_x$?

**Solución.** Si un conexo $E\subseteq D$ contiene $x$, R3 dice que es intervalo. Para cada $y\in E$, el segmento entre $x,y$ está en $E\subseteq D$, luego $y\in C_x$. Así $E\subseteq C_x$.

Primero sabemos que $C_x$ es intervalo y por ello conexo. Luego cualquier conexo del dominio que contenga $x$ se incluye en la clase usando su propia intervalaridad. Si un conexo mayor contuviera a $C_x$, contendría a $x$ y también quedaría en $C_x$. Así la clase no puede ampliarse dentro de $D$ manteniendo conexidad.

### Microcontrol 060

[]{#MA-MIC-ANM-01-015-060}

[]{#MA-MSOL-ANM-01-015-060}

**Pregunta.** ¿Dos componentes diferentes pueden intersectarse?

**Solución.** No. Son clases de equivalencia; si compartieran $z$, cualquier miembro de una estaría relacionado con $z$ y por transitividad con los miembros de la otra. Las clases serían iguales.

Una entrada compartida conecta por la relación a cualquier miembro de una clase con cualquier miembro de la otra. Transitividad produce las inclusiones en ambas direcciones, de modo que las clases coinciden. Además cada entrada está en su propia clase por reflexividad. Las componentes forman así una partición de $D$, sin elegir una clase preferida para cada punto.

### Microcontrol 061

[]{#MA-MIC-ANM-01-015-061}

[]{#MA-MSOL-ANM-01-015-061}

**Pregunta.** ¿En qué ambiente son siempre cerradas las componentes de $D$?

**Solución.** Relativamente a $D$. El argumento de adherencia exige que el punto adherente también esté en $D$; no incorpora puntos exteriores al dominio. Una componente como $(0,1)$ no es cerrada real.

Para demostrar cerradura relativa se toman puntos adherentes que además pertenecen a $D$. La pertenencia permite completar los extremos del segmento que relaciona ese punto con la clase. Un extremo ausente del dominio puede ser adherente en la recta sin incorporarse a la componente. La conclusión protege el ambiente original y no afirma cerradura absoluta.

### Microcontrol 062

[]{#MA-MIC-ANM-01-015-062}

[]{#MA-MSOL-ANM-01-015-062}

**Pregunta.** ¿Por qué $\{0\}$ no es abierta relativa en $\{0\}\cup\{1/(n+1):n\in\mathbb N\}$?

**Solución.** Para todo $r>0$, por arquimedianidad existe $n$ con $0<1/(n+1)<r$. La vecindad de cero en el dominio siempre contiene otro punto. Aun así $\{0\}$ es una componente.

La cota arquimediana produce una entrada positiva en toda bola de cero. Por tanto ninguna bola relativa se reduce al singleton y éste no es abierto relativo. Sin embargo, entre cero y cualquier entrada positiva hay puntos que faltan en $D$, lo que impide una componente intervalar mayor. Ser una componente no exige aislamiento.

### Microcontrol 063

[]{#MA-MIC-ANM-01-015-063}

[]{#MA-MSOL-ANM-01-015-063}

**Pregunta.** ¿Cuáles son las componentes de $\mathbb Q$ y son abiertas relativas?

**Solución.** Son singletons, porque entre dos racionales distintos hay un irracional omitido. Ningún singleton es abierto relativo: todo radio alrededor de un racional contiene otro racional por densidad.

Si una componente racional tuviera dos miembros distintos, su intervalaridad incluiría un irracional entre ellos, imposible. Cada clase es por ello un singleton. Pero la densidad racional proporciona otros racionales en toda vecindad de su punto, así ninguno es abierto relativo. La cerradura de las componentes no implica apertura, incluso cuando todas son singletons.

### Microcontrol 064

[]{#MA-MIC-ANM-01-015-064}

[]{#MA-MSOL-ANM-01-015-064}

**Pregunta.** ¿Qué refuerzo garantiza transporte exacto de componentes y no sólo inclusión?

**Solución.** Que la función sea homeomorfismo. Continuidad lleva una componente a un conexo contenido en una componente de la imagen; continuidad de la inversa y maximalidad dan la inclusión contraria. Una constante puede fusionar componentes.

Continuidad da una imagen conexa, y maximalidad la ubica dentro de una componente del codominio. Para recuperar toda esa componente es necesario llevarla atrás mediante una inversa continua. El conjunto recuperado es conexo y su maximalidad en el dominio fuerza la inclusión opuesta al volver a aplicar la biyección. Una continua sin ese retorno puede fusionar componentes distintas.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Ejercicios](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-microcontroles.html)
