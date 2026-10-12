---
content-id: MA-BCH-0329
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-031-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 31
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C31_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

Se conservan literalmente las 64 preguntas del manuscrito.

## 31.1. Dar destino a todas las sucesiones de Cauchy

### Microcontrol 1

[]{#MA-MSOL-ANM-01-031-001}

[]{#MA-MIC-ANM-01-031-001}

**Pregunta.** ¿Qué añade completitud a la condición de Cauchy?

**Respuesta.** Un destino dentro del espacio para toda sucesión que ya cumple Cauchy.

### Microcontrol 2

[]{#MA-MSOL-ANM-01-031-002}

[]{#MA-MIC-ANM-01-031-002}

**Pregunta.** ¿Completitud obliga a converger a toda sucesión?

**Respuesta.** No; en $\mathbb R$, $n$ no es Cauchy y no converge.

### Microcontrol 3

[]{#MA-MSOL-ANM-01-031-003}

[]{#MA-MIC-ANM-01-031-003}

**Pregunta.** ¿Por qué la discreta es completa?

**Respuesta.** Una cola Cauchy para $1/2$ es constante y tiene destino interno.

### Microcontrol 4

[]{#MA-MSOL-ANM-01-031-004}

[]{#MA-MIC-ANM-01-031-004}

**Pregunta.** ¿Qué ocurre en el espacio vacío?

**Respuesta.** No hay sucesiones hacia él; la condición universal de completitud es vacua.

### Microcontrol 5

[]{#MA-MSOL-ANM-01-031-005}

[]{#MA-MIC-ANM-01-031-005}

**Pregunta.** ¿Qué prueba completitud de un cerrado en un completo?

**Respuesta.** El destino ambiental de la Cauchy queda en el cerrado por el criterio directo de C30.

### Microcontrol 6

[]{#MA-MSOL-ANM-01-031-006}

[]{#MA-MIC-ANM-01-031-006}

**Pregunta.** ¿Qué selección exige el converso de cerrado?

**Respuesta.** Testigos de $Y\cap B(a,1/(n+1))$; elección numerable o testigos dados.

### Microcontrol 7

[]{#MA-MSOL-ANM-01-031-007}

[]{#MA-MIC-ANM-01-031-007}

**Pregunta.** ¿Por qué el límite de columnas define una función sin elegir destinos?

**Respuesta.** Cada columna real Cauchy tiene un límite único; la unicidad determina el valor.

### Microcontrol 8

[]{#MA-MSOL-ANM-01-031-008}

[]{#MA-MIC-ANM-01-031-008}

**Pregunta.** ¿Cómo se acredita acotación de la función límite?

**Respuesta.** Una función $f_N$ acotada y una cota uniforme $|f-f_N|\le1/2$ dan acotación.

## 31.2. Encerrar un destino y construirlo por iteración

### Microcontrol 9

[]{#MA-MSOL-ANM-01-031-009}

[]{#MA-MIC-ANM-01-031-009}

**Pregunta.** ¿Qué hipótesis encierra un único punto común?

**Respuesta.** Recintos cerrados no vacíos anidados, diámetro que tiende a cero y espacio completo, con testigos seleccionados o dados.

### Microcontrol 10

[]{#MA-MSOL-ANM-01-031-010}

[]{#MA-MIC-ANM-01-031-010}

**Pregunta.** ¿Dónde se usa elección en esos recintos?

**Respuesta.** Al fijar un punto en cada recinto de una familia numerable.

### Microcontrol 11

[]{#MA-MSOL-ANM-01-031-011}

[]{#MA-MIC-ANM-01-031-011}

**Pregunta.** ¿Qué define una contracción?

**Respuesta.** Una razón común $q<1$, $q\ge0$, que acota la distancia de todas las imágenes.

### Microcontrol 12

[]{#MA-MSOL-ANM-01-031-012}

[]{#MA-MIC-ANM-01-031-012}

**Pregunta.** ¿La iteración de una función dada necesita elección en cada paso?

**Respuesta.** No; $x_{n+1}=Tx_n$ determina unívocamente cada término desde $x_0$.

### Microcontrol 13

[]{#MA-MSOL-ANM-01-031-013}

[]{#MA-MIC-ANM-01-031-013}

**Pregunta.** ¿Qué controla el bloque desde n hasta p?

**Respuesta.** La triangular y la suma geométrica: $d(x_p,x_n)\le Cq^n/(1-q)$.

### Microcontrol 14

[]{#MA-MSOL-ANM-01-031-014}

[]{#MA-MIC-ANM-01-031-014}

**Pregunta.** ¿Qué ocurre si q=0?

**Respuesta.** Todas las imágenes coinciden; la iteración es constante desde $x_1$, con $q^0=1$.

### Microcontrol 15

[]{#MA-MSOL-ANM-01-031-015}

[]{#MA-MIC-ANM-01-031-015}

**Pregunta.** ¿Qué corte da error menor que 1/16 en la iteración modelo?

**Respuesta.** $n\ge5$; en $4$ el error es igual a $1/16$.

### Microcontrol 16

[]{#MA-MSOL-ANM-01-031-016}

[]{#MA-MIC-ANM-01-031-016}

**Pregunta.** ¿Disminuir estrictamente cada distancia da una contracción?

**Respuesta.** No; los cocientes pueden acercarse a $1$ sin una razón uniforme menor que $1$.

## 31.3. Cubrir con pocas bolas a cada escala

### Microcontrol 17

[]{#MA-MSOL-ANM-01-031-017}

[]{#MA-MIC-ANM-01-031-017}

**Pregunta.** ¿Qué exige acotación total?

**Respuesta.** Una red finita con centros internos para cada radio positivo.

### Microcontrol 18

[]{#MA-MSOL-ANM-01-031-018}

[]{#MA-MIC-ANM-01-031-018}

**Pregunta.** ¿Una sola escala basta?

**Respuesta.** No; la cuantificación abarca todos los radios positivos.

### Microcontrol 19

[]{#MA-MSOL-ANM-01-031-019}

[]{#MA-MIC-ANM-01-031-019}

**Pregunta.** ¿Acotación total implica acotación?

**Respuesta.** Sí, una red de radio $1$ y un máximo finito de distancias de centros dan una cota global.

### Microcontrol 20

[]{#MA-MSOL-ANM-01-031-020}

[]{#MA-MIC-ANM-01-031-020}

**Pregunta.** ¿Qué refuta el converso?

**Respuesta.** Un espacio discreto infinito: acotado, pero bolas pequeñas singleton.

### Microcontrol 21

[]{#MA-MSOL-ANM-01-031-021}

[]{#MA-MIC-ANM-01-031-021}

**Pregunta.** ¿Cómo se trasladan centros a un subespacio?

**Respuesta.** Con una red ambiental de radio mitad y representantes de las finitas bolas que lo cortan.

### Microcontrol 22

[]{#MA-MSOL-ANM-01-031-022}

[]{#MA-MIC-ANM-01-031-022}

**Pregunta.** ¿Qué estructura hace funcionar las mallas reales?

**Respuesta.** Finitas coordenadas, intervalos de longitud controlada y finitas celdas.

### Microcontrol 23

[]{#MA-MSOL-ANM-01-031-023}

[]{#MA-MIC-ANM-01-031-023}

**Pregunta.** ¿Cuántos puntos separados por eta caben en una bola de radio eta/2?

**Respuesta.** A lo sumo uno, por la triangular y la desigualdad estricta de la bola.

### Microcontrol 24

[]{#MA-MSOL-ANM-01-031-024}

[]{#MA-MIC-ANM-01-031-024}

**Pregunta.** ¿Totalmente acotado significa completo?

**Respuesta.** No; $(0,1)$ tiene redes finitas y pierde destinos en sus extremos.

## 31.4. Compacidad: reducir cualquier cobertura

### Microcontrol 25

[]{#MA-MSOL-ANM-01-031-025}

[]{#MA-MIC-ANM-01-031-025}

**Pregunta.** ¿Qué familia cuantifica la definición de compacto?

**Respuesta.** Toda cobertura abierta, de la que se exige una subcobertura finita.

### Microcontrol 26

[]{#MA-MSOL-ANM-01-031-026}

[]{#MA-MIC-ANM-01-031-026}

**Pregunta.** ¿Por qué compacto implica totalmente acotado?

**Respuesta.** La cobertura por todas las bolas de un radio dado admite finitos centros.

### Microcontrol 27

[]{#MA-MSOL-ANM-01-031-027}

[]{#MA-MIC-ANM-01-031-027}

**Pregunta.** ¿Qué prueba que un compacto métrico es cerrado?

**Respuesta.** Para un punto exterior, una subcobertura finita de bolas con radios ligados a sus distancias produce una ventana disjunta.

### Microcontrol 28

[]{#MA-MSOL-ANM-01-031-028}

[]{#MA-MIC-ANM-01-031-028}

**Pregunta.** ¿Qué es propiedad de intersección finita?

**Respuesta.** Cada subfamilia finita de cerrados tiene intersección no vacía, incluida la subfamilia vacía.

### Microcontrol 29

[]{#MA-MSOL-ANM-01-031-029}

[]{#MA-MIC-ANM-01-031-029}

**Pregunta.** ¿Cómo se pasa de coberturas a intersecciones?

**Respuesta.** Tomando complementos relativos y usando las leyes de De Morgan.

### Microcontrol 30

[]{#MA-MSOL-ANM-01-031-030}

[]{#MA-MIC-ANM-01-031-030}

**Pregunta.** ¿Por qué las clausuras de colas son no vacías?

**Respuesta.** Cada cola contiene términos de la sucesión ya dada.

### Microcontrol 31

[]{#MA-MSOL-ANM-01-031-031}

[]{#MA-MIC-ANM-01-031-031}

**Pregunta.** ¿La prueba directa de compacto implica completo fabrica una nueva ruta?

**Respuesta.** No; usa cerrados de colas y la propiedad de intersección finita.

### Microcontrol 32

[]{#MA-MSOL-ANM-01-031-032}

[]{#MA-MIC-ANM-01-031-032}

**Pregunta.** ¿Una unión infinita de compactos debe ser compacta?

**Respuesta.** No; la unión de singletons de naturales es no acotada en la recta.

## 31.5. La equivalencia métrica y sus elecciones

### Microcontrol 33

[]{#MA-MSOL-ANM-01-031-033}

[]{#MA-MIC-ANM-01-031-033}

**Pregunta.** ¿Qué añade completitud a una extracción Cauchy?

**Respuesta.** Un destino interno para esa subsucesión.

### Microcontrol 34

[]{#MA-MSOL-ANM-01-031-034}

[]{#MA-MIC-ANM-01-031-034}

**Pregunta.** ¿Qué selección fija redes a todas las escalas?

**Respuesta.** Elección numerable de listas finitas de centros, declarada en el marco del capítulo.

### Microcontrol 35

[]{#MA-MSOL-ANM-01-031-035}

[]{#MA-MIC-ANM-01-031-035}

**Pregunta.** ¿Qué determina los índices crecientes de extracción?

**Respuesta.** Mínimos de conjuntos infinitos de naturales después del índice anterior.

### Microcontrol 36

[]{#MA-MSOL-ANM-01-031-036}

[]{#MA-MIC-ANM-01-031-036}

**Pregunta.** ¿Qué distancia máxima da una bola de radio 2 elevado a menos j?

**Respuesta.** Dos puntos de ella están a distancia menor que $2^{1-j}$.

### Microcontrol 37

[]{#MA-MSOL-ANM-01-031-037}

[]{#MA-MIC-ANM-01-031-037}

**Pregunta.** ¿Qué gasto tiene fabricar una ruta separada?

**Respuesta.** Elección dependiente de puntos exteriores a las bolas elegidas previamente, o un selector dado.

### Microcontrol 38

[]{#MA-MSOL-ANM-01-031-038}

[]{#MA-MIC-ANM-01-031-038}

**Pregunta.** ¿Qué certifica el número de Lebesgue usado aquí?

**Respuesta.** Cada bola de un radio común queda en algún miembro de la cobertura.

### Microcontrol 39

[]{#MA-MSOL-ANM-01-031-039}

[]{#MA-MIC-ANM-01-031-039}

**Pregunta.** ¿Por qué no falla ese radio en un secuencialmente compacto?

**Respuesta.** Puntos infractores seleccionados tendrían una subsucesión convergente que acabaría dentro de una ventana de la cobertura.

### Microcontrol 40

[]{#MA-MSOL-ANM-01-031-040}

[]{#MA-MIC-ANM-01-031-040}

**Pregunta.** ¿Cuál es la equivalencia métrica bajo la selección declarada?

**Respuesta.** Compacto, completo y totalmente acotado, y secuencialmente compacto son equivalentes.

## 31.6. Transportar compacidad por continuidad

### Microcontrol 41

[]{#MA-MSOL-ANM-01-031-041}

[]{#MA-MIC-ANM-01-031-041}

**Pregunta.** ¿Cómo se transporta una cobertura de la imagen?

**Respuesta.** Por preimágenes abiertas del dominio.

### Microcontrol 42

[]{#MA-MSOL-ANM-01-031-042}

[]{#MA-MIC-ANM-01-031-042}

**Pregunta.** ¿La imagen compacta requiere inyectividad?

**Respuesta.** No; continuidad es suficiente.

### Microcontrol 43

[]{#MA-MSOL-ANM-01-031-043}

[]{#MA-MIC-ANM-01-031-043}

**Pregunta.** ¿Por qué el supremo de la imagen real se alcanza?

**Respuesta.** Es adherente y la imagen compacta es cerrada.

### Microcontrol 44

[]{#MA-MSOL-ANM-01-031-044}

[]{#MA-MIC-ANM-01-031-044}

**Pregunta.** ¿Qué sucede si el compacto es vacío en el teorema de extremos?

**Respuesta.** No hay valores ni extremos; se requiere dominio no vacío.

### Microcontrol 45

[]{#MA-MSOL-ANM-01-031-045}

[]{#MA-MIC-ANM-01-031-045}

**Pregunta.** ¿Qué familia evita elegir infinitos radios de continuidad?

**Respuesta.** Todas las parejas admisibles de centro y radio; compacidad retiene finitas.

### Microcontrol 46

[]{#MA-MSOL-ANM-01-031-046}

[]{#MA-MIC-ANM-01-031-046}

**Pregunta.** ¿Qué hace continuo al inverso de una biyección desde un compacto?

**Respuesta.** La imagen de cada cerrado es compacta y cerrada en el codominio métrico.

### Microcontrol 47

[]{#MA-MSOL-ANM-01-031-047}

[]{#MA-MIC-ANM-01-031-047}

**Pregunta.** ¿En qué ámbito cerrado y acotado implica compacto aquí?

**Respuesta.** En $\mathbb R^m$ con las métricas finitas declaradas; no en cualquier espacio métrico.

### Microcontrol 48

[]{#MA-MSOL-ANM-01-031-048}

[]{#MA-MIC-ANM-01-031-048}

**Pregunta.** ¿Completitud y acotación bastan para continuidad uniforme?

**Respuesta.** No; la recta con métrica truncada y $x^2$ da un contraejemplo.

## 31.7. Conexidad: impedir una separación

### Microcontrol 49

[]{#MA-MSOL-ANM-01-031-049}

[]{#MA-MIC-ANM-01-031-049}

**Pregunta.** ¿Qué exige una separación?

**Respuesta.** Dos abiertos relativos no vacíos, disjuntos, cuya unión sea el espacio.

### Microcontrol 50

[]{#MA-MSOL-ANM-01-031-050}

[]{#MA-MIC-ANM-01-031-050}

**Pregunta.** ¿Qué subconjunto refuta conexidad por ser abierto y cerrado?

**Respuesta.** Uno propio y no vacío.

### Microcontrol 51

[]{#MA-MSOL-ANM-01-031-051}

[]{#MA-MIC-ANM-01-031-051}

**Pregunta.** ¿Vacío y singleton son conexos?

**Respuesta.** Sí; no admiten dos partes no vacías en separación.

### Microcontrol 52

[]{#MA-MSOL-ANM-01-031-052}

[]{#MA-MIC-ANM-01-031-052}

**Pregunta.** ¿Qué informa una continua no constante hacia dos puntos discretos?

**Respuesta.** Sus preimágenes dan una separación del dominio.

### Microcontrol 53

[]{#MA-MSOL-ANM-01-031-053}

[]{#MA-MIC-ANM-01-031-053}

**Pregunta.** ¿Qué conserva una imagen continua de un conexo?

**Respuesta.** Conexidad de la imagen, mediante preimágenes de una separación hipotética.

### Microcontrol 54

[]{#MA-MSOL-ANM-01-031-054}

[]{#MA-MIC-ANM-01-031-054}

**Pregunta.** ¿Qué son los conexos reales usuales?

**Respuesta.** Los intervalos, incluyendo vacío y singleton.

### Microcontrol 55

[]{#MA-MSOL-ANM-01-031-055}

[]{#MA-MIC-ANM-01-031-055}

**Pregunta.** ¿Conexo por caminos implica conexo?

**Respuesta.** Sí; un camino entre las dos partes de una separación separaría $[0,1]$ por preimágenes.

### Microcontrol 56

[]{#MA-MSOL-ANM-01-031-056}

[]{#MA-MIC-ANM-01-031-056}

**Pregunta.** ¿Se ha afirmado el converso de conexo por caminos?

**Respuesta.** No; la conexidad sola no se identifica con esa propiedad sin una prueba adicional.

## 31.8. Comparar lo que sobrevive y cerrar la ruta

### Microcontrol 57

[]{#MA-MSOL-ANM-01-031-057}

[]{#MA-MIC-ANM-01-031-057}

**Pregunta.** ¿Qué falta en (0,1) para ser compacto?

**Respuesta.** Completitud: una Cauchy puede tener destino sólo en un extremo exterior.

### Microcontrol 58

[]{#MA-MSOL-ANM-01-031-058}

[]{#MA-MIC-ANM-01-031-058}

**Pregunta.** ¿Qué falta en la discreta infinita para ser compacta?

**Respuesta.** Acotación total, aunque sí es completa y acotada.

### Microcontrol 59

[]{#MA-MSOL-ANM-01-031-059}

[]{#MA-MIC-ANM-01-031-059}

**Pregunta.** ¿Truncar la distancia usual hace compacta la recta?

**Respuesta.** No; los enteros siguen separados a pequeña escala.

### Microcontrol 60

[]{#MA-MSOL-ANM-01-031-060}

[]{#MA-MIC-ANM-01-031-060}

**Pregunta.** ¿Qué propiedades de la recta conserva la métrica truncada?

**Respuesta.** Topología, convergencia, Cauchy, completitud y conexidad; cambia acotación.

### Microcontrol 61

[]{#MA-MSOL-ANM-01-031-061}

[]{#MA-MIC-ANM-01-031-061}

**Pregunta.** ¿La métrica transportada por phi es completa?

**Respuesta.** No; las imágenes de $n$ se acercan al punto $1$ fuera del recorrido.

### Microcontrol 62

[]{#MA-MSOL-ANM-01-031-062}

[]{#MA-MIC-ANM-01-031-062}

**Pregunta.** ¿Qué conserva un homeomorfismo necesariamente?

**Respuesta.** Compacidad y conexidad, por continuidad en ambos sentidos.

### Microcontrol 63

[]{#MA-MSOL-ANM-01-031-063}

[]{#MA-MIC-ANM-01-031-063}

**Pregunta.** ¿Qué añade un inverso uniformemente continuo?

**Respuesta.** Transporta Cauchy y redes con tolerancias comunes, permitiendo preservar completitud y acotación total.

### Microcontrol 64

[]{#MA-MSOL-ANM-01-031-064}

[]{#MA-MIC-ANM-01-031-064}

**Pregunta.** ¿Qué propiedad depende especialmente de las mallas finitas de la recta?

**Respuesta.** Que acotación implique acotación total, base geométrica de Heine–Borel finito-dimensional.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)
