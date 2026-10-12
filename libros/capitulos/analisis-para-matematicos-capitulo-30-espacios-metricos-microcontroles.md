---
content-id: MA-BCH-0325
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-030-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 30
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C30_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §30.1 — Conservar la distancia, soltar las coordenadas

### Microcontrol 001

[]{#MA-MIC-ANM-01-030-001}

[]{#MA-MSOL-ANM-01-030-001}

[]{#MA-SEC-ANM-01-030-001}

**Pregunta.** ¿Qué estructura deben tener los puntos de un espacio métrico?

**Solución.** Sólo pertenecer a un conjunto con una métrica; no se exige orden ni operaciones.

### Microcontrol 002

[]{#MA-MIC-ANM-01-030-002}

[]{#MA-MSOL-ANM-01-030-002}

**Pregunta.** ¿Qué tipo de números son las distancias?

**Solución.** Reales no negativos y finitos.

### Microcontrol 003

[]{#MA-MIC-ANM-01-030-003}

[]{#MA-MSOL-ANM-01-030-003}

**Pregunta.** ¿Qué axioma impide distancia cero entre puntos distintos?

**Solución.** La separación: $d(x,y)=0$ si y sólo si $x=y$.

### Microcontrol 004

[]{#MA-MIC-ANM-01-030-004}

[]{#MA-MSOL-ANM-01-030-004}

**Pregunta.** ¿Por qué la discreta cumple triangular?

**Solución.** Entre extremos distintos, el desvío cuesta uno o dos y domina la distancia uno.

### Microcontrol 005

[]{#MA-MIC-ANM-01-030-005}

[]{#MA-MSOL-ANM-01-030-005}

**Pregunta.** ¿Qué cuenta Hamming?

**Solución.** Coordenadas diferentes en palabras de longitud fija.

### Microcontrol 006

[]{#MA-MIC-ANM-01-030-006}

[]{#MA-MSOL-ANM-01-030-006}

**Pregunta.** ¿Qué triple refuta la distancia usual al cuadrado?

**Solución.** $0,1,2$: la distancia directa es cuatro y el desvío suma dos.

### Microcontrol 007

[]{#MA-MIC-ANM-01-030-007}

[]{#MA-MSOL-ANM-01-030-007}

**Pregunta.** ¿Qué se resta en la triangular inversa?

**Solución.** Valores reales de distancias, no puntos abstractos.

### Microcontrol 008

[]{#MA-MIC-ANM-01-030-008}

[]{#MA-MSOL-ANM-01-030-008}

**Pregunta.** ¿Una restricción de una métrica sigue siendo métrica?

**Solución.** Sí. Conserva sus tres propiedades en todos los triples del subconjunto.

## §30.2 — Bolas y el margen de una ventana

### Microcontrol 009

[]{#MA-MIC-ANM-01-030-009}

[]{#MA-MSOL-ANM-01-030-009}

[]{#MA-SEC-ANM-01-030-002}

**Pregunta.** ¿Qué desigualdad define una bola abierta?

**Solución.** $d(x,a)<r$ con radio $r>0$ y entrada $x\in X$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-030-010}

[]{#MA-MSOL-ANM-01-030-010}

**Pregunta.** ¿Qué radio interior entrega un punto $y\in B(a,r)$?

**Solución.** $r-d(a,y)>0$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-030-011}

[]{#MA-MSOL-ANM-01-030-011}

**Pregunta.** ¿Por qué ese radio produce inclusión de bolas?

**Solución.** La triangular suma la distancia del centro a $y$ y una distancia menor que el margen.

### Microcontrol 012

[]{#MA-MIC-ANM-01-030-012}

[]{#MA-MSOL-ANM-01-030-012}

**Pregunta.** ¿Una vecindad tiene que ser una bola?

**Solución.** No. Basta que contenga una bola positiva del centro.

### Microcontrol 013

[]{#MA-MIC-ANM-01-030-013}

[]{#MA-MSOL-ANM-01-030-013}

**Pregunta.** ¿Qué forma tiene la bola unidad de $d_1$ en el plano?

**Solución.** Un rombo abierto definido por $|x_1|+|x_2|<1$.

### Microcontrol 014

[]{#MA-MIC-ANM-01-030-014}

[]{#MA-MSOL-ANM-01-030-014}

**Pregunta.** ¿Qué forma tiene la bola unidad de $d_\infty$?

**Solución.** Un cuadrado abierto con ambas coordenadas de magnitud menor que uno.

### Microcontrol 015

[]{#MA-MIC-ANM-01-030-015}

[]{#MA-MSOL-ANM-01-030-015}

**Pregunta.** ¿Cuánto contiene $B_D(a,1)$?

**Solución.** Sólo el centro, porque los otros puntos tienen distancia exactamente uno.

### Microcontrol 016

[]{#MA-MIC-ANM-01-030-016}

[]{#MA-MSOL-ANM-01-030-016}

**Pregunta.** ¿Bola cerrada y clausura de bola abierta siempre coinciden?

**Solución.** No. En la discreta con varios puntos y radio uno, la primera es todo el espacio y la segunda sólo el centro.

## §30.3 — Abiertos, cerrados y ambiente relativo

### Microcontrol 017

[]{#MA-MIC-ANM-01-030-017}

[]{#MA-MSOL-ANM-01-030-017}

[]{#MA-SEC-ANM-01-030-003}

**Pregunta.** ¿Cómo se define abierto sin coordenadas?

**Solución.** Cada punto del conjunto posee una bola abierta completa contenida en él.

### Microcontrol 018

[]{#MA-MIC-ANM-01-030-018}

[]{#MA-MSOL-ANM-01-030-018}

**Pregunta.** ¿Qué operación arbitraria conserva abiertos?

**Solución.** La unión; cada entrada reutiliza un radio de un miembro.

### Microcontrol 019

[]{#MA-MIC-ANM-01-030-019}

[]{#MA-MSOL-ANM-01-030-019}

**Pregunta.** ¿Por qué sólo se promete intersección finita de abiertos?

**Solución.** El mínimo de finitísimos radios positivos es positivo; una familia infinita puede dejar sólo radio cero.

### Microcontrol 020

[]{#MA-MIC-ANM-01-030-020}

[]{#MA-MSOL-ANM-01-030-020}

**Pregunta.** ¿Qué exige pertenecer a la clausura?

**Solución.** Que cada bola del punto encuentre al conjunto.

### Microcontrol 021

[]{#MA-MIC-ANM-01-030-021}

[]{#MA-MSOL-ANM-01-030-021}

**Pregunta.** ¿Qué caracteriza la frontera?

**Solución.** Cada bola encuentra tanto el conjunto como su complemento dentro del ambiente declarado.

### Microcontrol 022

[]{#MA-MIC-ANM-01-030-022}

[]{#MA-MSOL-ANM-01-030-022}

**Pregunta.** ¿Qué bola tiene un subespacio $Y$?

**Solución.** $B_Y(y,r)=Y\cap B_X(y,r)$.

### Microcontrol 023

[]{#MA-MIC-ANM-01-030-023}

[]{#MA-MSOL-ANM-01-030-023}

**Pregunta.** ¿Cómo cambia la clausura al restringir el ambiente?

**Solución.** $\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A$ para $A\subset Y$.

### Microcontrol 024

[]{#MA-MIC-ANM-01-030-024}

[]{#MA-MSOL-ANM-01-030-024}

**Pregunta.** ¿El interior relativo se obtiene siempre intersectando el absoluto?

**Solución.** No. Un extremo del propio subespacio puede ser interior relativo sin ser interior absoluto.

## §30.4 — Convergencia con un destino en el espacio

### Microcontrol 025

[]{#MA-MIC-ANM-01-030-025}

[]{#MA-MSOL-ANM-01-030-025}

[]{#MA-SEC-ANM-01-030-004}

**Pregunta.** ¿Dónde debe vivir el destino de una sucesión en $X$?

**Solución.** En $X$, no sólo en un espacio mayor que lo contenga.

### Microcontrol 026

[]{#MA-MIC-ANM-01-030-026}

[]{#MA-MSOL-ANM-01-030-026}

**Pregunta.** ¿Qué orden de cuantificadores expresa convergencia?

**Solución.** $\forall\varepsilon>0\exists N\forall n\ge N$ para la distancia al destino menor que $\varepsilon$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-030-027}

[]{#MA-MSOL-ANM-01-030-027}

**Pregunta.** ¿Qué prueba unicidad sin completitud?

**Solución.** Dos ventanas de radios un tercio de la separación y un corte común contradicen triangular.

### Microcontrol 028

[]{#MA-MIC-ANM-01-030-028}

[]{#MA-MSOL-ANM-01-030-028}

**Pregunta.** ¿Cómo se acota el prefijo de una convergente?

**Solución.** Por el máximo de sus finitísimas distancias al destino; se reúne con la cota de cola.

### Microcontrol 029

[]{#MA-MIC-ANM-01-030-029}

[]{#MA-MSOL-ANM-01-030-029}

**Pregunta.** ¿Por qué una subsucesión conserva un corte?

**Solución.** Sus índices estrictamente crecientes satisfacen $n_k\ge k$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-030-030}

[]{#MA-MSOL-ANM-01-030-030}

**Pregunta.** ¿Qué hace una perturbación de distancia nula al destino?

**Solución.** Lo conserva, sumando el error de perturbación y el de la sucesión por triangular.

### Microcontrol 031

[]{#MA-MIC-ANM-01-030-031}

[]{#MA-MSOL-ANM-01-030-031}

**Pregunta.** ¿Qué dirección entre clausura y sucesiones no requiere selección?

**Solución.** Una sucesión de $A$ convergente en $X$ tiene su destino en la clausura de $A$.

### Microcontrol 032

[]{#MA-MIC-ANM-01-030-032}

[]{#MA-MSOL-ANM-01-030-032}

**Pregunta.** ¿Qué interfaz se declara para construir testigos de clausura?

**Solución.** $\mathrm{CC}(X)$, elección numerable para los conjuntos no vacíos de testigos, o una selección explícitamente dada.

## §30.5 — Cauchy compara toda la cola

### Microcontrol 033

[]{#MA-MIC-ANM-01-030-033}

[]{#MA-MSOL-ANM-01-030-033}

[]{#MA-SEC-ANM-01-030-005}

**Pregunta.** ¿Qué compara Cauchy?

**Solución.** Todos los pares de términos posteriores a un corte común, sin nombrar destino.

### Microcontrol 034

[]{#MA-MIC-ANM-01-030-034}

[]{#MA-MSOL-ANM-01-030-034}

**Pregunta.** ¿Cuál es la negación correcta de Cauchy?

**Solución.** Existe una tolerancia positiva fija tal que después de cualquier corte hay un par separado al menos por ella.

### Microcontrol 035

[]{#MA-MIC-ANM-01-030-035}

[]{#MA-MSOL-ANM-01-030-035}

**Pregunta.** ¿Qué tolerancia de convergencia demuestra Cauchy con $\varepsilon$?

**Solución.** $\varepsilon/2$, para sumar dos errores alrededor del destino.

### Microcontrol 036

[]{#MA-MIC-ANM-01-030-036}

[]{#MA-MSOL-ANM-01-030-036}

**Pregunta.** ¿Qué tolerancia de Cauchy basta para acotar?

**Solución.** Una sola, por ejemplo uno, y un término de referencia más el prefijo finito.

### Microcontrol 037

[]{#MA-MIC-ANM-01-030-037}

[]{#MA-MSOL-ANM-01-030-037}

**Pregunta.** ¿Cauchy implica destino en cualquier métrica?

**Solución.** No. Los recíprocos en $(0,1)$ son Cauchy y su único posible destino real queda fuera.

### Microcontrol 038

[]{#MA-MIC-ANM-01-030-038}

[]{#MA-MSOL-ANM-01-030-038}

**Pregunta.** ¿Qué significa Cauchy en la discreta?

**Solución.** Que la cola es constante, por usar tolerancia $1/2$.

### Microcontrol 039

[]{#MA-MIC-ANM-01-030-039}

[]{#MA-MSOL-ANM-01-030-039}

**Pregunta.** ¿Una subsucesión convergente basta sin Cauchy?

**Solución.** No. La hipótesis Cauchy es la que acerca toda la cola al término de referencia elegido.

### Microcontrol 040

[]{#MA-MIC-ANM-01-030-040}

[]{#MA-MSOL-ANM-01-030-040}

**Pregunta.** ¿Qué acredita una barrera geométrica de saltos?

**Solución.** Cauchy por bloques finitos; el destino requiere otra justificación y, si existe, se obtiene una cota de error.

## §30.6 — Continuidad entre espacios métricos

### Microcontrol 041

[]{#MA-MIC-ANM-01-030-041}

[]{#MA-MSOL-ANM-01-030-041}

[]{#MA-SEC-ANM-01-030-006}

**Pregunta.** ¿Cuál es el centro de salida en continuidad en $a$?

**Solución.** El valor efectivo $f(a)$, perteneciente al codominio declarado.

### Microcontrol 042

[]{#MA-MIC-ANM-01-030-042}

[]{#MA-MSOL-ANM-01-030-042}

**Pregunta.** ¿Qué sucede en un punto aislado?

**Solución.** Toda función es continua allí, porque una bola puede contener sólo el centro.

### Microcontrol 043

[]{#MA-MIC-ANM-01-030-043}

[]{#MA-MSOL-ANM-01-030-043}

**Pregunta.** ¿Continuidad transporta una sucesión dada sin elección?

**Solución.** Sí. Primero obtiene un radio y luego un corte de esa sucesión.

### Microcontrol 044

[]{#MA-MIC-ANM-01-030-044}

[]{#MA-MSOL-ANM-01-030-044}

**Pregunta.** ¿Qué necesita la recíproca secuencial general?

**Solución.** Reunir infractores en una sucesión, mediante $\mathrm{CC}(X)$ o testigos suministrados.

### Microcontrol 045

[]{#MA-MIC-ANM-01-030-045}

[]{#MA-MSOL-ANM-01-030-045}

**Pregunta.** ¿En qué dirección viajan los abiertos bajo continuidad?

**Solución.** Hacia atrás por preimágenes, que son abiertas en el dominio.

### Microcontrol 046

[]{#MA-MIC-ANM-01-030-046}

[]{#MA-MSOL-ANM-01-030-046}

**Pregunta.** ¿El criterio por preimágenes necesita construir sucesiones?

**Solución.** No. Se prueba directamente con radios en cada punto y bolas del codominio.

### Microcontrol 047

[]{#MA-MIC-ANM-01-030-047}

[]{#MA-MSOL-ANM-01-030-047}

**Pregunta.** ¿Por qué la distancia a un punto es continua?

**Solución.** La triangular inversa acota su error de salida por la distancia de entrada.

### Microcontrol 048

[]{#MA-MIC-ANM-01-030-048}

[]{#MA-MSOL-ANM-01-030-048}

**Pregunta.** ¿Una biyección continua siempre tiene inversa continua?

**Solución.** No. La identidad de la recta discreta hacia la usual tiene inversa discontinua.

## §30.7 — Una escala común y espacios de funciones

### Microcontrol 049

[]{#MA-MIC-ANM-01-030-049}

[]{#MA-MSOL-ANM-01-030-049}

[]{#MA-SEC-ANM-01-030-007}

**Pregunta.** ¿Qué cambia en los cuantificadores de continuidad uniforme?

**Solución.** El radio se elige antes de cualquier par de entradas y debe servir para todos.

### Microcontrol 050

[]{#MA-MIC-ANM-01-030-050}

[]{#MA-MSOL-ANM-01-030-050}

**Pregunta.** ¿Qué radio da una cota Lipschitz con $L>0$?

**Solución.** $\delta=\varepsilon/L$.

### Microcontrol 051

[]{#MA-MIC-ANM-01-030-051}

[]{#MA-MSOL-ANM-01-030-051}

**Pregunta.** ¿Por qué la uniforme transporta Cauchy?

**Solución.** Un radio común de entrada se aplica a todos los pares de una cola de Cauchy.

### Microcontrol 052

[]{#MA-MIC-ANM-01-030-052}

[]{#MA-MSOL-ANM-01-030-052}

**Pregunta.** ¿Qué pares refutan uniformidad de $1/x$ en $(0,1)$?

**Solución.** $1/(n+2)$ y $1/(n+3)$: su distancia desaparece y la de imágenes vale uno.

### Microcontrol 053

[]{#MA-MIC-ANM-01-030-053}

[]{#MA-MSOL-ANM-01-030-053}

**Pregunta.** ¿Qué condición necesita la distancia real a un conjunto?

**Solución.** Que el conjunto sea no vacío, para tener un ínfimo real finito de distancias.

### Microcontrol 054

[]{#MA-MIC-ANM-01-030-054}

[]{#MA-MSOL-ANM-01-030-054}

**Pregunta.** ¿Distancia cero a $A$ implica pertenencia a $A$?

**Solución.** Implica pertenencia a su clausura; pertenece a $A$ si éste es cerrado.

### Microcontrol 055

[]{#MA-MIC-ANM-01-030-055}

[]{#MA-MSOL-ANM-01-030-055}

**Pregunta.** ¿Qué asegura finitud de $D_\infty(f,g)$?

**Solución.** Que ambas funciones sean acotadas y el dominio de evaluación no vacío.

### Microcontrol 056

[]{#MA-MIC-ANM-01-030-056}

[]{#MA-MSOL-ANM-01-030-056}

**Pregunta.** ¿Cómo se pasa de error uniforme estricto a supremo estricto?

**Solución.** Se usa tolerancia $\varepsilon/2$, que deja supremo a lo sumo $\varepsilon/2<\varepsilon$.

## §30.8 — Cambiar la métrica y auditar lo que permanece

### Microcontrol 057

[]{#MA-MIC-ANM-01-030-057}

[]{#MA-MSOL-ANM-01-030-057}

[]{#MA-SEC-ANM-01-030-008}

**Pregunta.** ¿Qué compara $d_1$ y $d_\infty$ en el plano?

**Solución.** $d_\infty\le d_1\le2d_\infty$ para todos los pares.

### Microcontrol 058

[]{#MA-MIC-ANM-01-030-058}

[]{#MA-MSOL-ANM-01-030-058}

**Pregunta.** ¿Qué preserva una comparación global por constantes positivas?

**Solución.** Abiertos, destinos de convergencia, sucesiones de Cauchy y acotación.

### Microcontrol 059

[]{#MA-MIC-ANM-01-030-059}

[]{#MA-MSOL-ANM-01-030-059}

**Pregunta.** ¿Qué radios conservan bolas al usar $\min\{1,d\}$?

**Solución.** Todos los radios abiertos $0<r\le1$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-030-060}

[]{#MA-MSOL-ANM-01-030-060}

**Pregunta.** ¿La métrica recortada conserva acotación global?

**Solución.** Puede cambiarla: hace acotado todo espacio no vacío aunque la métrica original no lo hiciera.

### Microcontrol 061

[]{#MA-MIC-ANM-01-030-061}

[]{#MA-MSOL-ANM-01-030-061}

**Pregunta.** ¿Cuál es la inversa de $\phi(x)=x/(1+|x|)$?

**Solución.** $\psi(t)=t/(1-|t|)$ en $(-1,1)$.

### Microcontrol 062

[]{#MA-MIC-ANM-01-030-062}

[]{#MA-MSOL-ANM-01-030-062}

**Pregunta.** ¿Por qué $n$ es Cauchy en $e_\phi$?

**Solución.** Sus imágenes $n/(n+1)$ tienen todas las distancias de cola a lo sumo $1/(N+1)$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-030-063}

[]{#MA-MSOL-ANM-01-030-063}

**Pregunta.** ¿Mismos abiertos garantizan mismas Cauchy?

**Solución.** No. La usual y $e_\phi$ tienen los mismos abiertos y difieren para la sucesión $n$.

### Microcontrol 064

[]{#MA-MIC-ANM-01-030-064}

[]{#MA-MSOL-ANM-01-030-064}

**Pregunta.** ¿Qué queda para C31?

**Solución.** Examinar existencia de destinos de Cauchy y las nociones de compacidad y conexidad, con sus hipótesis métricas.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)
