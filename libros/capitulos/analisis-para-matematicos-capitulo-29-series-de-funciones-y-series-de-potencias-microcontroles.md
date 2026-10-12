---
content-id: MA-BCH-0321
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-029-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 29
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C29_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §29.1 — Una serie es una sucesión de sumas parciales

### Microcontrol 001

[]{#MA-MIC-ANM-01-029-001}

[]{#MA-MSOL-ANM-01-029-001}

[]{#MA-SEC-ANM-01-029-001}

**Pregunta.** ¿Qué objeto existe antes de definir la suma de una serie funcional?

**Solución.** Cada parcial finito $S_n=\sum_{j=0}^n u_j$, con dominio común $X$.

### Microcontrol 002

[]{#MA-MIC-ANM-01-029-002}

[]{#MA-MSOL-ANM-01-029-002}

**Pregunta.** ¿Qué define el dominio $D$?

**Solución.** La existencia de un límite real finito de $S_n(x)$ en esa entrada.

### Microcontrol 003

[]{#MA-MIC-ANM-01-029-003}

[]{#MA-MSOL-ANM-01-029-003}

**Pregunta.** ¿Desde qué índice empieza $R_n$?

**Solución.** Desde $n+1$, pues el parcial incluye el término de índice $n$.

### Microcontrol 004

[]{#MA-MIC-ANM-01-029-004}

[]{#MA-MSOL-ANM-01-029-004}

**Pregunta.** ¿Cuál es el orden de cuantificadores uniforme?

**Solución.** $\forall\varepsilon>0\exists N\forall n\ge N\forall x\in Y$ para el error menor que $\varepsilon$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-029-005}

[]{#MA-MSOL-ANM-01-029-005}

**Pregunta.** ¿Cauchy uniforme requiere conocer primero la suma?

**Solución.** No. Construye cada destino por completitud real y luego acredita un corte común.

### Microcontrol 006

[]{#MA-MIC-ANM-01-029-006}

[]{#MA-MSOL-ANM-01-029-006}

**Pregunta.** ¿Qué implica uniformidad sobre los términos?

**Solución.** Que tienden uniformemente a cero, comparando dos parciales consecutivos.

### Microcontrol 007

[]{#MA-MIC-ANM-01-029-007}

[]{#MA-MSOL-ANM-01-029-007}

**Pregunta.** ¿Por qué un prefijo no acotado puede ser inocuo?

**Solución.** Porque se cancela en diferencias de parciales posteriores y en el resto frente al destino.

### Microcontrol 008

[]{#MA-MIC-ANM-01-029-008}

[]{#MA-MSOL-ANM-01-029-008}

**Pregunta.** ¿La geométrica es uniforme en todo $(-1,1)$?

**Solución.** No. Cada resto es no acotado cerca de $1$, aunque haya uniformidad en ventanas cerradas interiores.

## §29.2 — El criterio M y lo que no afirma

### Microcontrol 009

[]{#MA-MIC-ANM-01-029-009}

[]{#MA-MSOL-ANM-01-029-009}

[]{#MA-SEC-ANM-01-029-002}

**Pregunta.** ¿Qué debe dominar $M_j$?

**Solución.** $|u_j(x)|$ para todas las entradas del dominio elegido, con el mismo número $M_j\ge0$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-029-010}

[]{#MA-MSOL-ANM-01-029-010}

**Pregunta.** ¿Qué condición numérica falta si sólo se dan mayorantes?

**Solución.** Que la serie $\sum M_j$ converja; tener cada mayorante finito no basta.

### Microcontrol 011

[]{#MA-MIC-ANM-01-029-011}

[]{#MA-MSOL-ANM-01-029-011}

**Pregunta.** ¿Cómo se controla un bloque finito bajo M?

**Solución.** Por $|\sum_{j=n+1}^m u_j|\le\sum_{j=n+1}^m M_j$, una cola numérica común.

### Microcontrol 012

[]{#MA-MIC-ANM-01-029-012}

[]{#MA-MSOL-ANM-01-029-012}

**Pregunta.** ¿Qué desigualdad queda al pasar al límite?

**Solución.** $|S-S_n|\le T_n$. Se conserva la desigualdad débil y se añade margen para tolerancia estricta.

### Microcontrol 013

[]{#MA-MIC-ANM-01-029-013}

[]{#MA-MSOL-ANM-01-029-013}

**Pregunta.** ¿M controla la serie de magnitudes?

**Solución.** Sí. Sus bloques positivos tienen los mismos mayorantes numéricos sumables.

### Microcontrol 014

[]{#MA-MIC-ANM-01-029-014}

[]{#MA-MSOL-ANM-01-029-014}

**Pregunta.** ¿Es necesario M para uniformidad?

**Solución.** No. Los términos con soportes puntuales disjuntos tienen cola uniforme $1/(n+2)$ y normas armónicas no sumables.

### Microcontrol 015

[]{#MA-MIC-ANM-01-029-015}

[]{#MA-MSOL-ANM-01-029-015}

**Pregunta.** ¿Absoluta puntual implica uniforme?

**Solución.** No. La geométrica en todo $(-1,1)$ es absoluta puntual y no uniforme.

### Microcontrol 016

[]{#MA-MIC-ANM-01-029-016}

[]{#MA-MSOL-ANM-01-029-016}

**Pregunta.** Con $E_n\le2^{-n}$, ¿qué corte certifica error menor que $1/8$?

**Solución.** $n\ge4$. En $n=3$ la cota sólo es igual a la tolerancia.

## §29.3 — Operaciones sobre sumas infinitas

### Microcontrol 017

[]{#MA-MIC-ANM-01-029-017}

[]{#MA-MSOL-ANM-01-029-017}

[]{#MA-SEC-ANM-01-029-003}

**Pregunta.** ¿Por qué son continuos los parciales si lo son los términos?

**Solución.** Por cierre de continuidad bajo sumas finitas; después C28 usa uniformidad para el destino.

### Microcontrol 018

[]{#MA-MIC-ANM-01-029-018}

[]{#MA-MSOL-ANM-01-029-018}

**Pregunta.** ¿Cuál es el marco del intercambio de integral?

**Solución.** Un intervalo cerrado fijo de longitud finita, términos integrables y convergencia uniforme de parciales.

### Microcontrol 019

[]{#MA-MIC-ANM-01-029-019}

[]{#MA-MSOL-ANM-01-029-019}

**Pregunta.** ¿Qué debe probarse antes de integrar el destino?

**Solución.** Su integrabilidad. C28 la construye por Darboux a partir de las aproximaciones uniformes.

### Microcontrol 020

[]{#MA-MIC-ANM-01-029-020}

[]{#MA-MSOL-ANM-01-029-020}

**Pregunta.** ¿Cuál es la cota de error integral?

**Solución.** $(b-a)E_n$ en $[a,b]$; desde un ancla $c$, $|x-c|E_n$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-029-021}

[]{#MA-MSOL-ANM-01-029-021}

**Pregunta.** ¿Qué serie debe ser uniforme para derivar?

**Solución.** La serie de derivadas, además de convergencia numérica de los valores en una ancla.

### Microcontrol 022

[]{#MA-MIC-ANM-01-029-022}

[]{#MA-MSOL-ANM-01-029-022}

**Pregunta.** ¿Por qué hace falta el ancla?

**Solución.** Las derivadas no ven constantes; los niveles de los parciales pueden divergir aun con derivadas cero.

### Microcontrol 023

[]{#MA-MIC-ANM-01-029-023}

[]{#MA-MSOL-ANM-01-029-023}

**Pregunta.** ¿Se exige continuidad de las derivadas en ese teorema?

**Solución.** No. C28 utiliza valor medio e incrementos de filas derivables.

### Microcontrol 024

[]{#MA-MIC-ANM-01-029-024}

[]{#MA-MSOL-ANM-01-029-024}

**Pregunta.** ¿Qué muestra el telescopio de raíces suavizadas?

**Solución.** Una serie de términos suaves con suma uniforme $|x|$ que no es derivable en cero.

## §29.4 — Un punto de convergencia abre una región interior

### Microcontrol 025

[]{#MA-MIC-ANM-01-029-025}

[]{#MA-MSOL-ANM-01-029-025}

[]{#MA-SEC-ANM-01-029-004}

**Pregunta.** ¿Cuánto vale una serie de potencias en su centro?

**Solución.** $a_0$; el monomio de orden cero es la función constante $1$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-029-026}

[]{#MA-MSOL-ANM-01-029-026}

**Pregunta.** ¿Qué acotación proporciona convergencia en $t\ne c$?

**Solución.** Los términos $a_j(t-c)^j$ tienden a cero y por ello tienen magnitudes acotadas por un $M$ común.

### Microcontrol 027

[]{#MA-MIC-ANM-01-029-027}

[]{#MA-MSOL-ANM-01-029-027}

**Pregunta.** ¿Cuál es la razón del mayorante interior?

**Solución.** $\rho=r/|t-c|<1$ para el segmento de radio $r$.

### Microcontrol 028

[]{#MA-MIC-ANM-01-029-028}

[]{#MA-MSOL-ANM-01-029-028}

**Pregunta.** ¿Cómo se define un radio finito?

**Solución.** Como el supremo de las distancias al centro de todas las entradas convergentes.

### Microcontrol 029

[]{#MA-MIC-ANM-01-029-029}

[]{#MA-MSOL-ANM-01-029-029}

**Pregunta.** ¿Debe alcanzarse el supremo?

**Solución.** No. Para proteger un radio menor basta una distancia convergente mayor que él.

### Microcontrol 030

[]{#MA-MIC-ANM-01-029-030}

[]{#MA-MSOL-ANM-01-029-030}

**Pregunta.** ¿Qué significa $R=0$?

**Solución.** Que sólo converge en el centro, con suma $a_0$.

### Microcontrol 031

[]{#MA-MIC-ANM-01-029-031}

[]{#MA-MSOL-ANM-01-029-031}

**Pregunta.** ¿Qué significa $R=\infty$?

**Solución.** Convergencia en toda la recta y uniformidad en cada segmento acotado, sin prometer uniformidad global.

### Microcontrol 032

[]{#MA-MIC-ANM-01-029-032}

[]{#MA-MSOL-ANM-01-029-032}

**Pregunta.** ¿El radio decide los dos extremos?

**Solución.** No. Se sustituyen por separado para estudiar sus dos series numéricas.

## §29.5 — Calcular el radio y examinar los extremos

### Microcontrol 033

[]{#MA-MIC-ANM-01-029-033}

[]{#MA-MSOL-ANM-01-029-033}

[]{#MA-SEC-ANM-01-029-005}

**Pregunta.** ¿Qué demuestra un cociente límite menor que $1$?

**Solución.** Una barrera geométrica eventual con razón $q<1$, que garantiza convergencia absoluta.

### Microcontrol 034

[]{#MA-MIC-ANM-01-029-034}

[]{#MA-MSOL-ANM-01-029-034}

**Pregunta.** ¿Qué demuestra un cociente límite mayor que $1$?

**Solución.** Crecimiento eventual de magnitudes por un factor $q>1$, impidiendo que los términos tiendan a cero.

### Microcontrol 035

[]{#MA-MIC-ANM-01-029-035}

[]{#MA-MSOL-ANM-01-029-035}

**Pregunta.** ¿Qué decide un cociente límite igual a $1$?

**Solución.** Nada por ese método; pueden ocurrir convergencia o divergencia.

### Microcontrol 036

[]{#MA-MIC-ANM-01-029-036}

[]{#MA-MSOL-ANM-01-029-036}

**Pregunta.** ¿Cuándo se prohíbe el cociente consecutivo de coeficientes?

**Solución.** Cuando los denominadores son cero infinitamente a menudo y no hay tramo final donde esté definido.

### Microcontrol 037

[]{#MA-MIC-ANM-01-029-037}

[]{#MA-MSOL-ANM-01-029-037}

**Pregunta.** ¿Qué radio da un límite de raíces $L\in(0,\infty)$?

**Solución.** $R=1/L$, por aplicar barreras geométricas a los términos en cada entrada.

### Microcontrol 038

[]{#MA-MIC-ANM-01-029-038}

[]{#MA-MSOL-ANM-01-029-038}

**Pregunta.** ¿Qué radios dan los casos $L=0$ y $L=\infty$?

**Solución.** Radio infinito y radio cero respectivamente; son casos, no divisiones reales.

### Microcontrol 039

[]{#MA-MIC-ANM-01-029-039}

[]{#MA-MSOL-ANM-01-029-039}

**Pregunta.** ¿Cómo convergen los extremos de $\sum_{j\ge1}x^j/j$?

**Solución.** En $-1$ condicionalmente por alternada; en $1$ diverge la armónica.

### Microcontrol 040

[]{#MA-MIC-ANM-01-029-040}

[]{#MA-MSOL-ANM-01-029-040}

**Pregunta.** ¿Por qué converge $\sum1/(j+1)^2$ sin otro criterio?

**Solución.** Para $j\ge1$ se domina por $1/j-1/(j+1)$, una serie telescópica positiva sumable.

## §29.6 — Derivar e integrar dentro del radio

### Microcontrol 041

[]{#MA-MIC-ANM-01-029-041}

[]{#MA-MSOL-ANM-01-029-041}

[]{#MA-SEC-ANM-01-029-006}

**Pregunta.** ¿Por qué se reservan dos radios $r<s<R$?

**Solución.** Para que el margen geométrico $r/s<1$ absorba los factores de índice de los términos derivados.

### Microcontrol 042

[]{#MA-MIC-ANM-01-029-042}

[]{#MA-MSOL-ANM-01-029-042}

**Pregunta.** ¿Qué ancla tienen los parciales originales en $c$?

**Solución.** $S_n(c)=a_0$ exactamente para todo $n$.

### Microcontrol 043

[]{#MA-MIC-ANM-01-029-043}

[]{#MA-MSOL-ANM-01-029-043}

**Pregunta.** ¿Cómo se justifica el mayorante derivado sin circularidad?

**Solución.** Se deriva una identidad polinómica finita y se pasan límites numéricos ya controlados.

### Microcontrol 044

[]{#MA-MIC-ANM-01-029-044}

[]{#MA-MSOL-ANM-01-029-044}

**Pregunta.** ¿Cuál es el radio de la serie derivada?

**Solución.** El mismo que el original, por convergencia interior y la comparación inversa de magnitudes.

### Microcontrol 045

[]{#MA-MIC-ANM-01-029-045}

[]{#MA-MSOL-ANM-01-029-045}

**Pregunta.** ¿La integrada puede aumentar el radio?

**Solución.** No. Convergencia a una distancia $d$ da una barrera ponderada que fuerza convergencia original en cada radio menor.

### Microcontrol 046

[]{#MA-MIC-ANM-01-029-046}

[]{#MA-MSOL-ANM-01-029-046}

**Pregunta.** ¿Dónde se permite la fórmula de derivación?

**Solución.** Sólo en $|x-c|<R$, con una ventana interior alrededor del punto.

### Microcontrol 047

[]{#MA-MIC-ANM-01-029-047}

[]{#MA-MSOL-ANM-01-029-047}

**Pregunta.** ¿Qué se fija antes del corte para derivadas iteradas?

**Solución.** El orden finito $k$; no se promete control común de todos los órdenes.

### Microcontrol 048

[]{#MA-MIC-ANM-01-029-048}

[]{#MA-MSOL-ANM-01-029-048}

**Pregunta.** ¿Qué vale $F^{(k)}(c)$?

**Solución.** $k!a_k$, pues todos los monomios restantes de grado positivo se anulan en el centro.

## §29.7 — Coeficientes, funciones y certificados

### Microcontrol 049

[]{#MA-MIC-ANM-01-029-049}

[]{#MA-MSOL-ANM-01-029-049}

[]{#MA-SEC-ANM-01-029-007}

**Pregunta.** ¿Por qué $E$ se deriva en toda la recta?

**Solución.** Tiene radio infinito y alrededor de cada entrada hay un segmento interior acotado con el control requerido.

### Microcontrol 050

[]{#MA-MIC-ANM-01-029-050}

[]{#MA-MSOL-ANM-01-029-050}

**Pregunta.** ¿Qué reindexación da $E^{\prime}=E$?

**Solución.** $j/j!=1/(j-1)!$ para $j\ge1$, seguido del índice $k=j-1$.

### Microcontrol 051

[]{#MA-MIC-ANM-01-029-051}

[]{#MA-MSOL-ANM-01-029-051}

**Pregunta.** ¿Cómo se acredita $E(x)E(-x)=1$?

**Solución.** El producto tiene derivada cero y valor $1$ en cero; valor medio lo hace constante en cada segmento.

### Microcontrol 052

[]{#MA-MIC-ANM-01-029-052}

[]{#MA-MSOL-ANM-01-029-052}

**Pregunta.** ¿Por qué $E$ es positiva?

**Solución.** No tiene ceros por el producto recíproco, es continua y vale $1$ en cero; valor intermedio excluye valores negativos.

### Microcontrol 053

[]{#MA-MIC-ANM-01-029-053}

[]{#MA-MSOL-ANM-01-029-053}

**Pregunta.** ¿Qué barrera usa la cola factorial después del grado $n$?

**Solución.** Primer término $r^{n+1}/(n+1)!$ y cociente máximo $r/(n+2)<1$.

### Microcontrol 054

[]{#MA-MIC-ANM-01-029-054}

[]{#MA-MSOL-ANM-01-029-054}

**Pregunta.** ¿Qué cota da grado cuatro en $[-1,1]$?

**Solución.** $1/100$, estrictamente menor que $1/50$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-029-055}

[]{#MA-MSOL-ANM-01-029-055}

**Pregunta.** ¿La unicidad de coeficientes construye una serie para toda función suave?

**Solución.** No. Compara representaciones convergentes ya existentes en una vecindad del mismo centro.

### Microcontrol 056

[]{#MA-MIC-ANM-01-029-056}

[]{#MA-MSOL-ANM-01-029-056}

**Pregunta.** ¿Qué identifica la integral geométrica sin nombrar logaritmos?

**Solución.** $L(x)=\int_0^x(1-t)^{-1}\,dt=\sum_{j\ge1}x^j/j$ sólo en el intervalo abierto interior.

## §29.8 — Productos y el puente hacia análisis complejo

### Microcontrol 057

[]{#MA-MIC-ANM-01-029-057}

[]{#MA-MSOL-ANM-01-029-057}

[]{#MA-SEC-ANM-01-029-008}

**Pregunta.** ¿Cómo se define el coeficiente del producto de Cauchy?

**Solución.** $\gamma_n=\sum_{j=0}^n\alpha_j\beta_{n-j}$, una suma finita.

### Microcontrol 058

[]{#MA-MIC-ANM-01-029-058}

[]{#MA-MSOL-ANM-01-029-058}

**Pregunta.** ¿Qué pares recoge el parcial de grado $N$?

**Solución.** El triángulo de índices no negativos $j+k\le N$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-029-059}

[]{#MA-MSOL-ANM-01-029-059}

**Pregunta.** ¿Por qué sirve $h=\lfloor N/2\rfloor$?

**Solución.** Si $j+k>N$, al menos uno de los índices excede $h$; de otro modo su suma sería a lo sumo $N$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-029-060}

[]{#MA-MSOL-ANM-01-029-060}

**Pregunta.** ¿Cuál es la cota de resto del producto?

**Solución.** $B_*T_\alpha(h)+A_*T_\beta(h)$ para series numéricas absolutamente convergentes.

### Microcontrol 061

[]{#MA-MIC-ANM-01-029-061}

[]{#MA-MSOL-ANM-01-029-061}

**Pregunta.** ¿Qué límite se toma primero en la prueba?

**Solución.** El del cuadrado $m\to\infty$ con triángulo $N$ fijo; después se hace $N\to\infty$.

### Microcontrol 062

[]{#MA-MIC-ANM-01-029-062}

[]{#MA-MSOL-ANM-01-029-062}

**Pregunta.** ¿El radio del producto debe ser igual al mínimo?

**Solución.** No. Es al menos el mínimo y puede crecer por cancelación de coeficientes.

### Microcontrol 063

[]{#MA-MIC-ANM-01-029-063}

[]{#MA-MSOL-ANM-01-029-063}

**Pregunta.** ¿Qué protegen los mayorantes comunes en una ventana?

**Solución.** Uniformidad de las colas y barreras comunes para que los factores no amplifiquen los errores.

### Microcontrol 064

[]{#MA-MIC-ANM-01-029-064}

[]{#MA-MSOL-ANM-01-029-064}

**Pregunta.** ¿Qué cambia al anticipar el plano complejo?

**Solución.** Las regiones radiales serán discos. Aquí no se ha demostrado diferenciabilidad compleja ni comportamiento general de la frontera.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)
