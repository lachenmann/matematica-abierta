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
date-modified: '2026-10-11'
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

### Microcontrol 002

[]{#MA-MIC-ANM-01-014-002}

[]{#MA-MSOL-ANM-01-014-002}

**Pregunta.** ¿Se excluye $x=a$ en el contrato de continuidad?

**Solución.** No. El centro está permitido y tiene error $|f(a)-f(a)|=0$.

### Microcontrol 003

[]{#MA-MIC-ANM-01-014-003}

[]{#MA-MSOL-ANM-01-014-003}

**Pregunta.** ¿Necesita $a$ ser interior del dominio?

**Solución.** No. La continuidad es relativa a las entradas de $D$; puede estudiarse en extremos y puntos aislados.

### Microcontrol 004

[]{#MA-MIC-ANM-01-014-004}

[]{#MA-MSOL-ANM-01-014-004}

**Pregunta.** ¿En qué se centra la bola de salida?

**Solución.** En el valor efectivo $f(a)$, no en un candidato independiente.

### Microcontrol 005

[]{#MA-MIC-ANM-01-014-005}

[]{#MA-MSOL-ANM-01-014-005}

**Pregunta.** ¿Cuál es el orden global de cuantificadores?

**Solución.** $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$. El radio puede depender de $a$ y de $\varepsilon$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-014-006}

[]{#MA-MSOL-ANM-01-014-006}

**Pregunta.** ¿Qué hipótesis legitima comparar continuidad con el límite perforado?

**Solución.** $a\in D\cap D^{\prime}$. Pertenencia legitima $f(a)$; acumulación legitima el límite de C13.

### Microcontrol 007

[]{#MA-MIC-ANM-01-014-007}

[]{#MA-MSOL-ANM-01-014-007}

**Pregunta.** ¿La existencia de un límite finito basta para continuidad?

**Solución.** No. En un punto de acumulación del dominio debe además coincidir con $f(a)$.

### Microcontrol 008

[]{#MA-MIC-ANM-01-014-008}

[]{#MA-MSOL-ANM-01-014-008}

**Pregunta.** ¿Qué inclusión de conjuntos expresa continuidad?

**Solución.** Para cada $\varepsilon>0$ hay $\delta>0$ con $f[D\cap B(a,\delta)]\subseteq B(f(a),\varepsilon)$, equivalentemente $D\cap B(a,\delta)\subseteq f^{-1}[B(f(a),\varepsilon)]$.

## §14.2 — El dominio y la reparación de un hueco

### Microcontrol 009

[]{#MA-MIC-ANM-01-014-009}

[]{#MA-MSOL-ANM-01-014-009}

[]{#MA-SEC-ANM-01-014-002}

**Pregunta.** ¿Qué radio sirve en un punto aislado?

**Solución.** Uno positivo $r$ con $D\cap B(a,r)=\{a\}$. Sirve para toda tolerancia porque la única entrada produce error cero.

### Microcontrol 010

[]{#MA-MIC-ANM-01-014-010}

[]{#MA-MSOL-ANM-01-014-010}

**Pregunta.** ¿Asignamos un límite perforado en ese punto aislado?

**Solución.** No bajo la convención de C13. La continuidad se prueba directamente sin inventar un límite vacuo.

### Microcontrol 011

[]{#MA-MIC-ANM-01-014-011}

[]{#MA-MSOL-ANM-01-014-011}

**Pregunta.** ¿La restricción a $A\subseteq D$ exige acumulación para conservar continuidad?

**Solución.** No. Basta $a\in A$; el mismo radio controla las entradas del subconjunto y conserva el valor central.

### Microcontrol 012

[]{#MA-MIC-ANM-01-014-012}

[]{#MA-MSOL-ANM-01-014-012}

**Pregunta.** ¿Qué debe incluir la coincidencia local de dos funciones para preservar continuidad?

**Solución.** Debe incluir el centro: $f=g$ en $D\cap B(a,r)$. Así sus valores centrales y sus errores coinciden.

### Microcontrol 013

[]{#MA-MIC-ANM-01-014-013}

[]{#MA-MSOL-ANM-01-014-013}

**Pregunta.** ¿Qué valor completa de forma continua un hueco con límite $L$?

**Solución.** El valor $L$. Los puntos originales obedecen el control del límite y el nuevo centro tiene error cero.

### Microcontrol 014

[]{#MA-MIC-ANM-01-014-014}

[]{#MA-MSOL-ANM-01-014-014}

**Pregunta.** ¿Qué resultado garantiza unicidad de esa reparación?

**Solución.** La unicidad del límite de C13, pues el centro que faltaba era punto de acumulación del dominio original.

### Microcontrol 015

[]{#MA-MIC-ANM-01-014-015}

[]{#MA-MSOL-ANM-01-014-015}

**Pregunta.** ¿Qué hipótesis adicional permite afirmar continuidad de la extensión en todos los puntos?

**Solución.** Que la función original sea continua en todo $D$. Un radio menor que la mitad de la distancia al nuevo punto preserva cada control anterior.

### Microcontrol 016

[]{#MA-MIC-ANM-01-014-016}

[]{#MA-MSOL-ANM-01-014-016}

**Pregunta.** ¿Puede un solo valor reparar dos límites laterales distintos?

**Solución.** No. La continuidad en el punto forzaría que ambos destinos laterales coincidieran con ese mismo valor.

## §14.3 — Transportar sucesiones que sí pueden tocar el centro

### Microcontrol 017

[]{#MA-MIC-ANM-01-014-017}

[]{#MA-MSOL-ANM-01-014-017}

[]{#MA-SEC-ANM-01-014-003}

**Pregunta.** ¿Puede una ruta para continuidad alcanzar el centro infinitas veces?

**Solución.** Sí. Puede incluso ser constantemente igual a $a$; esos términos tienen error de salida cero.

### Microcontrol 018

[]{#MA-MIC-ANM-01-014-018}

[]{#MA-MSOL-ANM-01-014-018}

**Pregunta.** ¿Qué flujo de escalas prueba la dirección secuencial directa?

**Solución.** $\varepsilon\to\delta\to N$: continuidad da el radio, convergencia de entradas da la cola y esa cola satisface el error de salida.

### Microcontrol 019

[]{#MA-MIC-ANM-01-014-019}

[]{#MA-MSOL-ANM-01-014-019}

**Pregunta.** ¿Qué ocurre con una ruta convergente a un punto aislado del dominio?

**Solución.** Es eventualmente constante en ese punto, porque acaba dentro de una bola relativa que sólo lo contiene a él.

### Microcontrol 020

[]{#MA-MIC-ANM-01-014-020}

[]{#MA-MSOL-ANM-01-014-020}

**Pregunta.** ¿Por qué un infractor de continuidad nunca es el centro?

**Solución.** Porque la tolerancia fija es positiva y en el centro el error es cero, no puede ser $\ge\varepsilon_0$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-014-021}

[]{#MA-MSOL-ANM-01-014-021}

**Pregunta.** ¿Cómo se escribe la negación de continuidad?

**Solución.** $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$: $|x-a|<\delta$ y $|f(x)-f(a)|\ge\varepsilon_0$.

### Microcontrol 022

[]{#MA-MIC-ANM-01-014-022}

[]{#MA-MSOL-ANM-01-014-022}

**Pregunta.** ¿Qué selector se obtiene de una enumeración sobreyectiva dada?

**Solución.** $k_n=\min\{k:e(k)\in E_n\}$ y $x_n=e(k_n)$. El mínimo es de índices naturales, no de valores reales.

### Microcontrol 023

[]{#MA-MIC-ANM-01-014-023}

[]{#MA-MSOL-ANM-01-014-023}

**Pregunta.** ¿Qué premisa adicional se declara para la recíproca secuencial en cualquier dominio real?

**Solución.** $\mathrm{CC}(\mathbb R)$, aplicada a la familia de infractores no vacíos. El teorema general permanece condicional.

### Microcontrol 024

[]{#MA-MIC-ANM-01-014-024}

[]{#MA-MSOL-ANM-01-014-024}

**Pregunta.** ¿Necesita selección numerable una refutación mediante una ruta explícita?

**Solución.** No. La ruta ya está construida; la dirección directa y la unicidad secuencial bastan para refutar la continuidad.

## §14.4 — Preimágenes: de controles locales a conjuntos abiertos

### Microcontrol 025

[]{#MA-MIC-ANM-01-014-025}

[]{#MA-MSOL-ANM-01-014-025}

[]{#MA-SEC-ANM-01-014-004}

**Pregunta.** ¿Qué significa que $A$ sea abierto relativo a $D$?

**Solución.** Que $A=D\cap U$ para algún abierto $U$ de la recta.

### Microcontrol 026

[]{#MA-MIC-ANM-01-014-026}

[]{#MA-MSOL-ANM-01-014-026}

**Pregunta.** ¿Por qué $[0,1/2)$ puede ser abierto en $[0,1]$?

**Solución.** Porque es $[0,1]\cap(-1,1/2)$. La bola sólo debe quedar dentro tras intersectarla con el dominio.

### Microcontrol 027

[]{#MA-MIC-ANM-01-014-027}

[]{#MA-MSOL-ANM-01-014-027}

**Pregunta.** ¿Qué criterio por bolas caracteriza la apertura relativa?

**Solución.** $\forall a\in A\ \exists r>0:D\cap B(a,r)\subseteq A$.

### Microcontrol 028

[]{#MA-MIC-ANM-01-014-028}

[]{#MA-MSOL-ANM-01-014-028}

**Pregunta.** ¿Por qué se unen todas las bolas válidas en vez de elegir una por punto?

**Solución.** La unión sigue siendo abierta y representa exactamente $A$ al intersectarla con $D$, sin necesitar una selección simultánea de radios.

### Microcontrol 029

[]{#MA-MIC-ANM-01-014-029}

[]{#MA-MSOL-ANM-01-014-029}

**Pregunta.** ¿La continuidad conserva apertura por imagen o por preimagen?

**Solución.** Por preimagen: todo abierto de salida tiene preimagen abierta relativa al dominio.

### Microcontrol 030

[]{#MA-MIC-ANM-01-014-030}

[]{#MA-MSOL-ANM-01-014-030}

**Pregunta.** ¿Qué abierto de salida recupera el contrato para una tolerancia $\varepsilon$?

**Solución.** $B(f(a),\varepsilon)$. Su preimagen abierta contiene el centro y por ello una bola relativa de entrada.

### Microcontrol 031

[]{#MA-MIC-ANM-01-014-031}

[]{#MA-MSOL-ANM-01-014-031}

**Pregunta.** ¿Cuál es la identidad de complementos para preimágenes?

**Solución.** $D\setminus f^{-1}[F]=f^{-1}[\mathbb R\setminus F]$. Para una función con codominio $E$, se usa $E\setminus F$ cuando $F\subseteq E$.

### Microcontrol 032

[]{#MA-MIC-ANM-01-014-032}

[]{#MA-MSOL-ANM-01-014-032}

**Pregunta.** ¿En qué ambiente es cerrado el conjunto de ceros de una función continua en $D$?

**Solución.** Es cerrado relativo a $D$. No tiene por qué ser cerrado en toda la recta si $D$ no lo es.

## §14.5 — Operar y componer sin perder el dominio

### Microcontrol 033

[]{#MA-MIC-ANM-01-014-033}

[]{#MA-MSOL-ANM-01-014-033}

[]{#MA-SEC-ANM-01-014-005}

**Pregunta.** ¿Cómo se reparte el error para una suma?

**Solución.** Con tolerancias $\varepsilon/2$ para ambos sumandos y el mínimo de sus radios.

### Microcontrol 034

[]{#MA-MIC-ANM-01-014-034}

[]{#MA-MSOL-ANM-01-014-034}

**Pregunta.** ¿Qué se hace con un escalar nulo?

**Solución.** Su producto es la función cero y tiene error cero; no se divide por el escalar.

### Microcontrol 035

[]{#MA-MIC-ANM-01-014-035}

[]{#MA-MSOL-ANM-01-014-035}

**Pregunta.** ¿Qué proporciona continuidad con tolerancia $1$ para el producto?

**Solución.** Una cota local $|f(x)|<|f(a)|+1$ en una bola relativa completa.

### Microcontrol 036

[]{#MA-MIC-ANM-01-014-036}

[]{#MA-MSOL-ANM-01-014-036}

**Pregunta.** ¿Qué hipótesis permite el recíproco en el centro?

**Solución.** Que $g(a)\ne0$. La tolerancia $|g(a)|/2$ separa el denominador de cero cerca de $a$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-014-037}

[]{#MA-MSOL-ANM-01-014-037}

**Pregunta.** ¿Cuál es el dominio efectivo de $f/g$?

**Solución.** $D_g=\{x\in D:g(x)\ne0\}$. Si $g(a)\ne0$, incluye el centro y una bola relativa alrededor de él.

### Microcontrol 038

[]{#MA-MIC-ANM-01-014-038}

[]{#MA-MSOL-ANM-01-014-038}

**Pregunta.** ¿Hay que exigir $f(x)\ne f(a)$ para componer funciones continuas?

**Solución.** No. El contrato de la exterior incluye su centro y controla su valor.

### Microcontrol 039

[]{#MA-MIC-ANM-01-014-039}

[]{#MA-MSOL-ANM-01-014-039}

**Pregunta.** ¿Qué conjunto permite componer si no sabemos que $f[D]\subseteq E$?

**Solución.** $T=\{x\in D:f(x)\in E\}$. Se compone la restricción con codominio $E$ y la continuidad se afirma en $T$.

### Microcontrol 040

[]{#MA-MIC-ANM-01-014-040}

[]{#MA-MSOL-ANM-01-014-040}

**Pregunta.** ¿Qué identidad da la prueba global de composición?

**Solución.** $(g\circ f)^{-1}[V]=f^{-1}[g^{-1}[V]]$, con los tipos y ambientes relativos correspondientes.

## §14.6 — Lo que la continuidad no promete sobre imágenes e inversas

### Microcontrol 041

[]{#MA-MIC-ANM-01-014-041}

[]{#MA-MSOL-ANM-01-014-041}

[]{#MA-SEC-ANM-01-014-006}

**Pregunta.** ¿Qué imagen abierta refuta que continuidad implique aplicación abierta?

**Solución.** El cuadrado envía el abierto $\mathbb R$ a $[0,\infty)$, que no es abierto en la recta.

### Microcontrol 042

[]{#MA-MIC-ANM-01-014-042}

[]{#MA-MSOL-ANM-01-014-042}

**Pregunta.** ¿Qué ejemplo continuo tiene imagen no cerrada aunque su dominio sea cerrado?

**Solución.** $r(x)=1/(1+x^2)$ en $\mathbb R$, con imagen $(0,1]$. Cero es adherente y no pertenece a ella.

### Microcontrol 043

[]{#MA-MIC-ANM-01-014-043}

[]{#MA-MSOL-ANM-01-014-043}

**Pregunta.** ¿Qué añade la bijectividad a una función continua?

**Solución.** Añade la existencia de una función inversa, pero no garantiza la continuidad de esa inversa.

### Microcontrol 044

[]{#MA-MIC-ANM-01-014-044}

[]{#MA-MSOL-ANM-01-014-044}

**Pregunta.** En la biyección de §14.6, ¿cuál es la inversa en $y=1$?

**Solución.** $h(1)=2$, porque el valor uno procede del punto $x=2$ de la segunda pieza.

### Microcontrol 045

[]{#MA-MIC-ANM-01-014-045}

[]{#MA-MSOL-ANM-01-014-045}

**Pregunta.** ¿Qué entradas refutan la continuidad de esa inversa en uno?

**Solución.** $y=1-t$ con $t=\min(\delta/2,1/2)>0$: la distancia de entrada es $t<\delta$ y la de salida a $2$ es $1+t$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-014-046}

[]{#MA-MSOL-ANM-01-014-046}

**Pregunta.** ¿Qué es un homeomorfismo entre subconjuntos reales?

**Solución.** Una biyección continua cuya inversa es continua, con continuidad relativa en ambos ambientes.

### Microcontrol 047

[]{#MA-MIC-ANM-01-014-047}

[]{#MA-MSOL-ANM-01-014-047}

**Pregunta.** ¿Qué condición de imágenes equivale a continuidad de la inversa de una biyección?

**Solución.** Que la biyección sea abierta: envía abiertos relativos del dominio a abiertos relativos del codominio.

### Microcontrol 048

[]{#MA-MIC-ANM-01-014-048}

[]{#MA-MSOL-ANM-01-014-048}

**Pregunta.** ¿Por qué no contradice el criterio de preimágenes el fallo de imagen abierta?

**Solución.** Porque imagen y preimagen son operaciones distintas. El criterio sólo garantiza apertura al transportar conjuntos de salida hacia atrás.

## §14.7 — Reunir definiciones locales y piezas cerradas

### Microcontrol 049

[]{#MA-MIC-ANM-01-014-049}

[]{#MA-MSOL-ANM-01-014-049}

[]{#MA-SEC-ANM-01-014-007}

**Pregunta.** ¿Necesita ser finita una cobertura por abiertos para comprobar continuidad localmente?

**Solución.** No. En cada punto se usa una pieza abierta que lo contiene y una bola relativa dentro de esa pieza.

### Microcontrol 050

[]{#MA-MIC-ANM-01-014-050}

[]{#MA-MSOL-ANM-01-014-050}

**Pregunta.** ¿Qué función cumplen las piezas cerradas que no contienen el centro en el pegado finito?

**Solución.** Sus complementos abiertos dan radios que excluyen esas piezas de una ventana alrededor del centro.

### Microcontrol 051

[]{#MA-MIC-ANM-01-014-051}

[]{#MA-MSOL-ANM-01-014-051}

**Pregunta.** ¿Dónde se usa la finitud de la cobertura cerrada?

**Solución.** Al tomar el mínimo de todos los radios de control y exclusión, que sigue siendo positivo.

### Microcontrol 052

[]{#MA-MIC-ANM-01-014-052}

[]{#MA-MSOL-ANM-01-014-052}

**Pregunta.** ¿Qué asegura el acuerdo de las funciones en intersecciones?

**Solución.** Que la función pegada está bien definida y su restricción coincide con cada función de pieza. No asegura por sí solo continuidad en fronteras.

### Microcontrol 053

[]{#MA-MIC-ANM-01-014-053}

[]{#MA-MSOL-ANM-01-014-053}

**Pregunta.** ¿Qué piezas y valores permiten pegar $|x|$?

**Solución.** $-x$ en $(-\infty,0]$ y $x$ en $[0,\infty)$. Son piezas cerradas con valor común cero en la intersección.

### Microcontrol 054

[]{#MA-MIC-ANM-01-014-054}

[]{#MA-MSOL-ANM-01-014-054}

**Pregunta.** ¿Por qué falla pegar cero en $(-\infty,0)$ y uno en $[0,\infty)$?

**Solución.** La pieza izquierda no es cerrada ni puede excluirse cerca de cero. Sus entradas próximas tienen error uno respecto del valor central uno.

### Microcontrol 055

[]{#MA-MIC-ANM-01-014-055}

[]{#MA-MSOL-ANM-01-014-055}

**Pregunta.** ¿Qué tolerancia conserva localmente un valor central positivo?

**Solución.** $f(a)/2$. Continuidad da $f(x)>f(a)/2>0$ cerca del centro.

### Microcontrol 056

[]{#MA-MIC-ANM-01-014-056}

[]{#MA-MSOL-ANM-01-014-056}

**Pregunta.** ¿La conservación local de signo prueba el valor intermedio?

**Solución.** No. Sólo protege el signo cerca de un punto. La existencia de valores entre salidas en un intervalo se estudia en C15.

## §14.8 — Certificados de proximidad y límites del control lineal

### Microcontrol 057

[]{#MA-MIC-ANM-01-014-057}

[]{#MA-MSOL-ANM-01-014-057}

[]{#MA-SEC-ANM-01-014-008}

**Pregunta.** Con una cota local $|f(x)-f(a)|\le K|x-a|$, $K>0$, ¿qué radio sirve?

**Solución.** $\delta=\min(r,\varepsilon/K)$, donde $r$ es el radio en que vale la cota.

### Microcontrol 058

[]{#MA-MIC-ANM-01-014-058}

[]{#MA-MSOL-ANM-01-014-058}

**Pregunta.** ¿Qué ocurre si $K=0$?

**Solución.** La función coincide localmente con $f(a)$; sirve el radio $r$ y el error es cero.

### Microcontrol 059

[]{#MA-MIC-ANM-01-014-059}

[]{#MA-MSOL-ANM-01-014-059}

**Pregunta.** ¿Qué dependencia aparece en el certificado del cuadrado?

**Solución.** $\delta=\min(1,\varepsilon/(1+2|a|))$ depende del centro $a$ y del desafío $\varepsilon$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-014-060}

[]{#MA-MSOL-ANM-01-014-060}

**Pregunta.** ¿Qué identidad controla el error de la raíz?

**Solución.** Para $u=\sqrt{x}$, $v=\sqrt{a}$, se tiene $(u-v)^2\le|x-a|$ al factorizar la diferencia de cuadrados y distinguir el orden de $u,v$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-014-061}

[]{#MA-MSOL-ANM-01-014-061}

**Pregunta.** ¿Qué radio certifica continuidad de la raíz en cero?

**Solución.** $\delta=\varepsilon^2$, para entradas del dominio no negativo: $\sqrt{x}<\varepsilon$ si $0\le x<\varepsilon^2$.

### Microcontrol 062

[]{#MA-MIC-ANM-01-014-062}

[]{#MA-MSOL-ANM-01-014-062}

**Pregunta.** ¿Una función continua debe admitir una cota lineal local de ese error?

**Solución.** No. La raíz es continua en cero pero $\sqrt{x}/x=1/\sqrt{x}$ supera cualquier constante para entradas positivas suficientemente pequeñas.

### Microcontrol 063

[]{#MA-MIC-ANM-01-014-063}

[]{#MA-MSOL-ANM-01-014-063}

**Pregunta.** ¿Por qué la cota inferior para probar continuidad inversa se exige a todo $x\in D$?

**Solución.** Para excluir que entradas lejanas produzcan salidas cercanas al valor central. Una cota sólo local no puede aplicarse antes de saber que la inversa es cercana.

### Microcontrol 064

[]{#MA-MIC-ANM-01-014-064}

[]{#MA-MSOL-ANM-01-014-064}

**Pregunta.** ¿Qué radios aportan las cotas $c|x-z|\le|f(x)-f(z)|\le C|x-z|$, con $c,C>0$?

**Solución.** Para la función sirve $\varepsilon/C$; para la inversa sirve $c\varepsilon$. La bijectividad legitima usar la entrada inversa única.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html)
