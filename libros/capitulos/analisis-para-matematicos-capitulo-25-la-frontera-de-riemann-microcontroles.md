---
content-id: MA-BCH-0305
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-025-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 25
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C25_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §25.1 — El presupuesto de oscilación

### Microcontrol 001

[]{#MA-MIC-ANM-01-025-001}

[]{#MA-MSOL-ANM-01-025-001}

[]{#MA-SEC-ANM-01-025-001}

**Pregunta.** ¿Qué presupuesto define la brecha?

**Solución.** $G=\sum_i\omega_i\Delta_i$, oscilación ponderada por anchura de todas las piezas.

### Microcontrol 002

[]{#MA-MIC-ANM-01-025-002}

[]{#MA-MSOL-ANM-01-025-002}

**Pregunta.** ¿Cómo se define una pieza mala para nivel $\eta>0$?

**Solución.** Su oscilación es al menos $\eta$.

### Microcontrol 003

[]{#MA-MIC-ANM-01-025-003}

[]{#MA-MSOL-ANM-01-025-003}

**Pregunta.** ¿Qué cota inferior usa las piezas malas?

**Solución.** $\eta\lambda_P(\eta)\le G(f,P)$.

### Microcontrol 004

[]{#MA-MIC-ANM-01-025-004}

[]{#MA-MSOL-ANM-01-025-004}

**Pregunta.** ¿Qué cota superior da $|f|\le B$?

**Solución.** $G(f,P)\le\eta(b-a)+2B\lambda_P(\eta)$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-025-005}

[]{#MA-MSOL-ANM-01-025-005}

**Pregunta.** ¿La oscilación puntual exige un radio mínimo?

**Solución.** No. Es el ínfimo de las oscilaciones de todas las vecindades relativas de radio positivo.

### Microcontrol 006

[]{#MA-MIC-ANM-01-025-006}

[]{#MA-MSOL-ANM-01-025-006}

**Pregunta.** ¿Qué equivale a continuidad en un punto?

**Solución.** $\Omega_f(x)=0$, bajo la acotación declarada.

### Microcontrol 007

[]{#MA-MIC-ANM-01-025-007}

[]{#MA-MSOL-ANM-01-025-007}

**Pregunta.** ¿Por qué $D_\eta$ es cerrado relativo?

**Solución.** Si la oscilación puntual es menor que el nivel, una vecindad buena transmite esa desigualdad a centros próximos.

### Microcontrol 008

[]{#MA-MIC-ANM-01-025-008}

[]{#MA-MSOL-ANM-01-025-008}

**Pregunta.** ¿Qué hace compacto a $D_\eta$?

**Solución.** Su cerradura relativa dentro del segmento compacto, por C16.

## §25.2 — Discontinuidades que caben en collares

### Microcontrol 009

[]{#MA-MIC-ANM-01-025-009}

[]{#MA-MSOL-ANM-01-025-009}

[]{#MA-SEC-ANM-01-025-002}

**Pregunta.** ¿Basta un número finito de discontinuidades para integrar?

**Solución.** Sí si la función está acotada; esa hipótesis no puede omitirse.

### Microcontrol 010

[]{#MA-MIC-ANM-01-025-010}

[]{#MA-MSOL-ANM-01-025-010}

**Pregunta.** ¿Qué se controla con los collares?

**Solución.** La longitud total de piezas donde puede persistir oscilación grande.

### Microcontrol 011

[]{#MA-MIC-ANM-01-025-011}

[]{#MA-MSOL-ANM-01-025-011}

**Pregunta.** ¿Dónde se obtiene la escala común de las piezas buenas?

**Solución.** De un subcubrimiento finito de vecindades de radio medio, por compacidad de C16.

### Microcontrol 012

[]{#MA-MIC-ANM-01-025-012}

[]{#MA-MSOL-ANM-01-025-012}

**Pregunta.** ¿Por qué usar todos los pares centro/radio válidos?

**Solución.** Para formar una cubierta sin elegir previamente un radio para cada centro de una familia infinita.

### Microcontrol 013

[]{#MA-MIC-ANM-01-025-013}

[]{#MA-MSOL-ANM-01-025-013}

**Pregunta.** ¿Qué garantiza malla menor que el mínimo radio medio?

**Solución.** Cada pieza cabe en una vecindad grande de la cubierta y es buena o está dentro de los collares.

### Microcontrol 014

[]{#MA-MIC-ANM-01-025-014}

[]{#MA-MSOL-ANM-01-025-014}

**Pregunta.** ¿Qué justifica sumar longitudes dentro de una unión?

**Solución.** Cortar en los finitísimos extremos y usar subaditividad finita de anchuras.

### Microcontrol 015

[]{#MA-MIC-ANM-01-025-015}

[]{#MA-MSOL-ANM-01-025-015}

**Pregunta.** ¿Qué cota de brecha da el collar del escalón con cortes $c-r,c,c+r$?

**Solución.** A lo sumo $2r$; con valor nodal uno, la brecha exacta es $r$ porque la pieza derecha es constante.

### Microcontrol 016

[]{#MA-MIC-ANM-01-025-016}

[]{#MA-MSOL-ANM-01-025-016}

**Pregunta.** ¿El nodo compartido afecta una sola pieza?

**Solución.** Puede afectar ambas piezas cerradas vecinas; no agrega anchura propia.

## §25.3 — La obstrucción densa de Dirichlet

### Microcontrol 017

[]{#MA-MIC-ANM-01-025-017}

[]{#MA-MSOL-ANM-01-025-017}

[]{#MA-SEC-ANM-01-025-003}

**Pregunta.** ¿Qué debe probarse para las cotas de Dirichlet?

**Solución.** Que toda pieza no degenerada contiene un racional y un irracional.

### Microcontrol 018

[]{#MA-MIC-ANM-01-025-018}

[]{#MA-MSOL-ANM-01-025-018}

**Pregunta.** ¿Cómo se obtiene un racional entre $u<v$?

**Solución.** Arquimedianidad y un entero $k$ con $nu<k<nv$ permiten tomar $k/n$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-025-019}

[]{#MA-MSOL-ANM-01-025-019}

**Pregunta.** ¿Cómo se obtiene un irracional después de un racional interior?

**Solución.** Añadir $\sqrt2/n$ con n grande conserva la entrada en el intervalo y no puede volverla racional.

### Microcontrol 020

[]{#MA-MIC-ANM-01-025-020}

[]{#MA-MSOL-ANM-01-025-020}

**Pregunta.** ¿Cuál es la suma inferior de Dirichlet?

**Solución.** Cero para cualquier partición.

### Microcontrol 021

[]{#MA-MIC-ANM-01-025-021}

[]{#MA-MSOL-ANM-01-025-021}

**Pregunta.** ¿Cuál es su suma superior en $[a,b]$?

**Solución.** $b-a$, no uno salvo longitud uno.

### Microcontrol 022

[]{#MA-MIC-ANM-01-025-022}

[]{#MA-MSOL-ANM-01-025-022}

**Pregunta.** ¿Qué nivel puntual de oscilación tiene Dirichlet?

**Solución.** Uno en todos los puntos, incluidos bordes relativos.

### Microcontrol 023

[]{#MA-MIC-ANM-01-025-023}

[]{#MA-MSOL-ANM-01-025-023}

**Pregunta.** ¿Refinar reduce su brecha?

**Solución.** No. Todas las piezas siguen teniendo oscilación uno y sus anchuras suman $b-a$.

### Microcontrol 024

[]{#MA-MIC-ANM-01-025-024}

[]{#MA-MSOL-ANM-01-025-024}

**Pregunta.** ¿Un dibujo de racionales certifica densidad?

**Solución.** No. Es una muestra finita; la prueba aritmética certifica todos los intervalos.

## §25.4 — Thomae: alturas pequeñas y picos finitos

### Microcontrol 025

[]{#MA-MIC-ANM-01-025-025}

[]{#MA-MSOL-ANM-01-025-025}

[]{#MA-SEC-ANM-01-025-004}

**Pregunta.** ¿Qué valor tiene Thomae en una fracción reducida $p/q$?

**Solución.** $1/q$, con denominador positivo y normalización única.

### Microcontrol 026

[]{#MA-MIC-ANM-01-025-026}

[]{#MA-MSOL-ANM-01-025-026}

**Pregunta.** ¿Cuánto vale en cero?

**Solución.** Uno, porque la forma reducida es $0/1$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-025-027}

[]{#MA-MSOL-ANM-01-025-027}

**Pregunta.** ¿Por qué es finito $E_N$?

**Solución.** Está contenido en los candidatos $p/q$ con $1\le q\le N$, $0\le p\le q$, una familia finita.

### Microcontrol 028

[]{#MA-MIC-ANM-01-025-028}

[]{#MA-MSOL-ANM-01-025-028}

**Pregunta.** ¿Qué cota vale fuera de $E_N$?

**Solución.** $T\le1/(N+1)$.

### Microcontrol 029

[]{#MA-MIC-ANM-01-025-029}

[]{#MA-MSOL-ANM-01-025-029}

**Pregunta.** ¿Por qué es continua en un irracional?

**Solución.** Un radio positivo evita los finitísimos picos grandes, y todos los restantes son pequeños.

### Microcontrol 030

[]{#MA-MIC-ANM-01-025-030}

[]{#MA-MSOL-ANM-01-025-030}

**Pregunta.** ¿Por qué falla continuidad en un racional?

**Solución.** Toda vecindad contiene un irracional de valor cero, separado del valor central positivo.

### Microcontrol 031

[]{#MA-MIC-ANM-01-025-031}

[]{#MA-MSOL-ANM-01-025-031}

**Pregunta.** ¿Cuál es la oscilación puntual en $p/q$?

**Solución.** $1/q$; una vecindad evita otros picos de denominador≤q y contiene tanto el centro como un irracional.

### Microcontrol 032

[]{#MA-MIC-ANM-01-025-032}

[]{#MA-MSOL-ANM-01-025-032}

**Pregunta.** ¿Qué integral tiene Thomae?

**Solución.** Cero, por cotas superiores arbitrariamente pequeñas y sumas inferiores cero.

## §25.5 — Un criterio exacto por niveles

### Microcontrol 033

[]{#MA-MIC-ANM-01-025-033}

[]{#MA-MSOL-ANM-01-025-033}

[]{#MA-SEC-ANM-01-025-005}

**Pregunta.** ¿Qué significa contenido finito nulo?

**Solución.** Toda tolerancia de longitud admite una cobertura por finitísimos intervalos abiertos de longitud total menor que ella.

### Microcontrol 034

[]{#MA-MIC-ANM-01-025-034}

[]{#MA-MSOL-ANM-01-025-034}

**Pregunta.** ¿Se ha definido una medida?

**Solución.** No. Sólo una propiedad de coberturas finitas; no aditividad numerable.

### Microcontrol 035

[]{#MA-MIC-ANM-01-025-035}

[]{#MA-MSOL-ANM-01-025-035}

**Pregunta.** ¿Qué caracteriza R5?

**Solución.** Integrabilidad de una acotada equivale a contenido finito nulo de cada $D_\eta$ con $\eta>0$.

### Microcontrol 036

[]{#MA-MIC-ANM-01-025-036}

[]{#MA-MSOL-ANM-01-025-036}

**Pregunta.** ¿Por qué cubrir también los nodos en la necesidad?

**Solución.** Un punto con oscilación puntual grande puede quedar en el borde de piezas y no en sus interiores.

### Microcontrol 037

[]{#MA-MIC-ANM-01-025-037}

[]{#MA-MSOL-ANM-01-025-037}

**Pregunta.** ¿Qué da $G<\eta\sigma/4$?

**Solución.** Las piezas de oscilación≥η suman longitud menor que $\sigma/4$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-025-038}

[]{#MA-MSOL-ANM-01-025-038}

**Pregunta.** ¿Qué se cubre en la suficiencia?

**Solución.** El nivel compacto $D_\eta$ con abiertos de longitud total pequeña; fuera de ellos hay vecindades buenas.

### Microcontrol 039

[]{#MA-MIC-ANM-01-025-039}

[]{#MA-MSOL-ANM-01-025-039}

**Pregunta.** ¿Se exige una cobertura pequeña de todas las discontinuidades juntas?

**Solución.** No. Se exige por cada nivel positivo; la unión puede ser densa.

### Microcontrol 040

[]{#MA-MIC-ANM-01-025-040}

[]{#MA-MSOL-ANM-01-025-040}

**Pregunta.** ¿Qué falla en Dirichlet según R5?

**Solución.** Su nivel $D_\eta$ es el segmento completo si $0<\eta\le1$, sin cobertura finita arbitrariamente corta.

## §25.6 — Un soporte infinito de longitud evanescente

### Microcontrol 041

[]{#MA-MIC-ANM-01-025-041}

[]{#MA-MSOL-ANM-01-025-041}

[]{#MA-SEC-ANM-01-025-006}

**Pregunta.** ¿Qué hipótesis usa el lema de soporte?

**Solución.** Soporte contenido en un compacto de contenido finito nulo, función acotada no negativa y cero fuera.

### Microcontrol 042

[]{#MA-MIC-ANM-01-025-042}

[]{#MA-MSOL-ANM-01-025-042}

**Pregunta.** ¿Qué controla la malla en ese lema?

**Solución.** Toda pieza que toque el soporte queda dentro de su cubierta abierta pequeña.

### Microcontrol 043

[]{#MA-MIC-ANM-01-025-043}

[]{#MA-MSOL-ANM-01-025-043}

**Pregunta.** ¿Cuántas componentes tiene $C_n$?

**Solución.** $2^n$ segmentos cerrados.

### Microcontrol 044

[]{#MA-MIC-ANM-01-025-044}

[]{#MA-MSOL-ANM-01-025-044}

**Pregunta.** ¿Cuál es la anchura de cada componente?

**Solución.** $3^{-n}$.

### Microcontrol 045

[]{#MA-MIC-ANM-01-025-045}

[]{#MA-MSOL-ANM-01-025-045}

**Pregunta.** ¿Cuál es la longitud total de una etapa?

**Solución.** $(2/3)^n$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-025-046}

[]{#MA-MSOL-ANM-01-025-046}

**Pregunta.** ¿Por qué el conjunto final es compacto?

**Solución.** Es cerrado por intersección de cerrados y está contenido en el segmento compacto.

### Microcontrol 047

[]{#MA-MIC-ANM-01-025-047}

[]{#MA-MSOL-ANM-01-025-047}

**Pregunta.** ¿Dónde es discontinua $\mathbf1_C$?

**Solución.** Exactamente en C: el complemento es abierto y C tiene interior vacío.

### Microcontrol 048

[]{#MA-MIC-ANM-01-025-048}

[]{#MA-MSOL-ANM-01-025-048}

**Pregunta.** ¿Qué integral tiene esa indicadora?

**Solución.** Cero, por el lema de soporte compacto y las coberturas de longitud pequeña.

## §25.7 — Cambiar muchos valores y aproximar

### Microcontrol 049

[]{#MA-MIC-ANM-01-025-049}

[]{#MA-MSOL-ANM-01-025-049}

[]{#MA-SEC-ANM-01-025-007}

**Pregunta.** ¿Qué cota global compara oscilaciones de $f$ y $g$?

**Solución.** Si $|f-g|\le\delta$, entonces $\omega(f,I)\le\omega(g,I)+2\delta$.

### Microcontrol 050

[]{#MA-MIC-ANM-01-025-050}

[]{#MA-MSOL-ANM-01-025-050}

**Pregunta.** ¿Qué cota compara sus brechas?

**Solución.** $G(f,P)\le G(g,P)+2\delta(b-a)$.

### Microcontrol 051

[]{#MA-MIC-ANM-01-025-051}

[]{#MA-MSOL-ANM-01-025-051}

**Pregunta.** ¿Cuándo se puede comparar los valores de sus integrales?

**Solución.** Después de demostrar que ambos existen, no como prueba circular de existencia.

### Microcontrol 052

[]{#MA-MIC-ANM-01-025-052}

[]{#MA-MSOL-ANM-01-025-052}

**Pregunta.** ¿Qué soporte tiene $T_N$?

**Solución.** El conjunto finito $E_N$; por tanto su integral es cero.

### Microcontrol 053

[]{#MA-MIC-ANM-01-025-053}

[]{#MA-MSOL-ANM-01-025-053}

**Pregunta.** ¿Qué error global aproxima Thomae?

**Solución.** $|T-T_N|\le1/(N+1)$ para todas las entradas.

### Microcontrol 054

[]{#MA-MIC-ANM-01-025-054}

[]{#MA-MSOL-ANM-01-025-054}

**Pregunta.** ¿Qué límite entrada por entrada tienen $d_N=\mathbf1_{E_N}$?

**Solución.** La función de Dirichlet, porque cada racional acaba incluido y ningún irracional lo está.

### Microcontrol 055

[]{#MA-MIC-ANM-01-025-055}

[]{#MA-MSOL-ANM-01-025-055}

**Pregunta.** ¿Qué error global conservan esos indicadores?

**Solución.** Uno para cada N: quedan racionales fuera del conjunto finito.

### Microcontrol 056

[]{#MA-MIC-ANM-01-025-056}

[]{#MA-MSOL-ANM-01-025-056}

**Pregunta.** ¿Cambiar numerablemente muchos valores es la regla de cambios finitos?

**Solución.** No. Puede conservar integral en un ejemplo o destruir integrabilidad en otro.

## §25.8 — La frontera y el paso que todavía falta

### Microcontrol 057

[]{#MA-MIC-ANM-01-025-057}

[]{#MA-MSOL-ANM-01-025-057}

[]{#MA-SEC-ANM-01-025-008}

**Pregunta.** ¿Cuál es la primera exigencia para Riemann propia?

**Solución.** Acotación en el cerrado no degenerado, forzada por el contrato de C23.

### Microcontrol 058

[]{#MA-MIC-ANM-01-025-058}

[]{#MA-MSOL-ANM-01-025-058}

**Pregunta.** ¿El conjunto completo de discontinuidades debe ser de contenido finito nulo?

**Solución.** No necesariamente; Thomae tiene discontinuidades racionales densas y niveles positivos finitos.

### Microcontrol 059

[]{#MA-MIC-ANM-01-025-059}

[]{#MA-MSOL-ANM-01-025-059}

**Pregunta.** ¿Los racionales de $[0,1]$ tienen contenido finito nulo?

**Solución.** No. La clausura de cualquier cobertura abierta finita los extiende al segmento y obliga longitud total≥1.

### Microcontrol 060

[]{#MA-MIC-ANM-01-025-060}

[]{#MA-MSOL-ANM-01-025-060}

**Pregunta.** ¿Basta continuidad salvo un punto sin acotación?

**Solución.** No. $h(x)=1/x$ para x>0 y h(0)=0 falla acotación e integrabilidad propia.

### Microcontrol 061

[]{#MA-MIC-ANM-01-025-061}

[]{#MA-MSOL-ANM-01-025-061}

**Pregunta.** ¿Una etapa finita de Cantor es su intersección?

**Solución.** No. Es una envolvente que contiene al conjunto final.

### Microcontrol 062

[]{#MA-MIC-ANM-01-025-062}

[]{#MA-MSOL-ANM-01-025-062}

**Pregunta.** ¿Una tabla de alturas certifica todos los picos omitidos?

**Solución.** No. La cota aritmética universal de denominadores sí los controla.

### Microcontrol 063

[]{#MA-MIC-ANM-01-025-063}

[]{#MA-MSOL-ANM-01-025-063}

**Pregunta.** ¿Se asignó una integral de Lebesgue a Dirichlet?

**Solución.** No. La teoría más amplia sólo se motiva; no se construyó ni usó aquí.

### Microcontrol 064

[]{#MA-MIC-ANM-01-025-064}

[]{#MA-MSOL-ANM-01-025-064}

**Pregunta.** ¿Qué puerta sigue después del cierre?

**Solución.** C26: sucesiones de funciones y convergencia punto por punto, sin abrirla durante C25.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)
