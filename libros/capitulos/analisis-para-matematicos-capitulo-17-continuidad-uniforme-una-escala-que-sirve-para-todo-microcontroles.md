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
date-modified: '2026-10-11'
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

### Microcontrol 002

[]{#MA-MIC-ANM-01-017-002}

[]{#MA-MSOL-ANM-01-017-002}

**Pregunta.** ¿Qué dependencia adicional admite la continuidad puntual?

**Solución.** El radio se elige después del centro $a$, y puede depender de él además de la tolerancia, función y dominio.

### Microcontrol 003

[]{#MA-MIC-ANM-01-017-003}

[]{#MA-MSOL-ANM-01-017-003}

**Pregunta.** ¿Por qué la uniformidad implica continuidad en cada punto?

**Solución.** Se fija el centro como uno de los dos argumentos y se conserva el mismo radio uniforme para todos los otros puntos del dominio.

### Microcontrol 004

[]{#MA-MIC-ANM-01-017-004}

[]{#MA-MSOL-ANM-01-017-004}

**Pregunta.** ¿Qué tolerancia se mantiene fija al negar uniformidad?

**Solución.** Una $\varepsilon_0>0$ para la que todo radio positivo admite un par de entradas próximas con diferencia de salida al menos $\varepsilon_0$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-017-005}

[]{#MA-MSOL-ANM-01-017-005}

**Pregunta.** ¿Un radio local dependiente del centro prueba falta de uniformidad?

**Solución.** No. Es una solución local, no una prueba de que todo candidato común falla. Hay que producir testigos para cada $\delta>0$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-017-006}

[]{#MA-MSOL-ANM-01-017-006}

**Pregunta.** ¿Qué radio sirve para una constante Lipschitz $L>0$?

**Solución.** $\delta=\varepsilon/L$; la desigualdad $|f(x)-f(y)|\le L|x-y|$ convierte distancia estrictamente menor que ese radio en error menor que $\varepsilon$.

### Microcontrol 007

[]{#MA-MIC-ANM-01-017-007}

[]{#MA-MSOL-ANM-01-017-007}

**Pregunta.** ¿Por qué la raíz puede ser uniforme sin ser Lipschitz?

**Solución.** Su control es $|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}$, que da radio $\varepsilon^2$. En cero, los cocientes $1/\sqrt{x}$ no están acotados.

### Microcontrol 008

[]{#MA-MIC-ANM-01-017-008}

[]{#MA-MSOL-ANM-01-017-008}

**Pregunta.** ¿Qué ocurre con el dominio vacío?

**Solución.** La condición sobre pares es vacía y cualquier radio positivo sirve; no hay puntos que exigir controlar.

## §17.2 — Una cubierta y una escala de protección

### Microcontrol 009

[]{#MA-MIC-ANM-01-017-009}

[]{#MA-MSOL-ANM-01-017-009}

[]{#MA-SEC-ANM-01-017-002}

**Pregunta.** ¿Qué expresa un número de Lebesgue para una cubierta de $K$?

**Solución.** Una escala $\lambda>0$ tal que, para cada $z\in K$, algún miembro de la cubierta contiene toda la bola relativa $K\cap B(z,\lambda)$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-017-010}

[]{#MA-MSOL-ANM-01-017-010}

**Pregunta.** ¿Por qué se reúnen todos los triples admisibles?

**Solución.** La familia queda determinada por una fórmula; la existencia local de un triple no se convierte en una elección simultánea por punto.

### Microcontrol 011

[]{#MA-MIC-ANM-01-017-011}

[]{#MA-MSOL-ANM-01-017-011}

**Pregunta.** ¿Con qué bolas se cubre y en cuáles se reserva protección?

**Solución.** Las bolas $B(a,r)$ cubren; las dobles $B(a,2r)$ están contenidas en los abiertos originales.

### Microcontrol 012

[]{#MA-MIC-ANM-01-017-012}

[]{#MA-MSOL-ANM-01-017-012}

**Pregunta.** ¿Qué ocurre antes de tomar el mínimo de radios?

**Solución.** Compacidad produce un conjunto finito no vacío de triples cuyas bolas cubren $K$. Sólo sus radios concretos forman el mínimo positivo.

### Microcontrol 013

[]{#MA-MIC-ANM-01-017-013}

[]{#MA-MSOL-ANM-01-017-013}

**Pregunta.** ¿Qué desigualdad mueve la protección desde $a$ hasta $z$?

**Solución.** Si $|z-a|<r$ y $|w-z|<\lambda\le r$, entonces $|w-a|<\lambda+r\le2r$.

### Microcontrol 014

[]{#MA-MIC-ANM-01-017-014}

[]{#MA-MSOL-ANM-01-017-014}

**Pregunta.** ¿Se elige un abierto para todos los centros simultáneamente?

**Solución.** No. La escala es global, pero para un centro $z$ fijado basta el índice de uno de los triples de la lista que lo cubre.

### Microcontrol 015

[]{#MA-MIC-ANM-01-017-015}

[]{#MA-MSOL-ANM-01-017-015}

**Pregunta.** ¿Cómo se tratan cubiertas por abiertos relativos?

**Solución.** Con $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real por C16 y con $K\cap W_i=A_i$; se aplica R2 al levantamiento canónico.

### Microcontrol 016

[]{#MA-MIC-ANM-01-017-016}

[]{#MA-MSOL-ANM-01-017-016}

**Pregunta.** ¿Qué número sirve para el compacto vacío?

**Solución.** $\lambda=1$, porque no hay centros que verificar, incluso si la familia de índices es vacía.

## §17.3 — Heine–Cantor: reducir antes de tomar el mínimo

### Microcontrol 017

[]{#MA-MIC-ANM-01-017-017}

[]{#MA-MSOL-ANM-01-017-017}

[]{#MA-SEC-ANM-01-017-003}

**Pregunta.** ¿Qué uniformiza Heine–Cantor cuando $K\subseteq D$?

**Solución.** La restricción $h:K\to\mathbb R$, si $K$ es compacto y $f$ es continua en sus puntos relativamente a $D$. No uniformiza necesariamente todo $D$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-017-018}

[]{#MA-MSOL-ANM-01-017-018}

**Pregunta.** ¿Qué información guarda un par admisible $(a,r)$?

**Solución.** Que todo punto de $K$ a distancia menor que $2r$ de $a$ tiene salida a distancia menor que $\varepsilon/2$ de $h(a)$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-017-019}

[]{#MA-MSOL-ANM-01-017-019}

**Pregunta.** ¿Cómo se verifica cobertura sin función de radios?

**Solución.** Para un $a$ fijado, continuidad entrega $\rho$ y el par $(a,\rho/2)$ pertenece a la familia ya definida; su bola contiene $a$.

### Microcontrol 020

[]{#MA-MIC-ANM-01-017-020}

[]{#MA-MSOL-ANM-01-017-020}

**Pregunta.** ¿Tiene que entrar $y$ en la bola pequeña que cubre $x$?

**Solución.** No. $|y-a|<\delta+r\le2r$ lo coloca en la bola doble, que conserva el control necesario.

### Microcontrol 021

[]{#MA-MIC-ANM-01-017-021}

[]{#MA-MSOL-ANM-01-017-021}

**Pregunta.** ¿Por qué se divide el error en dos mitades?

**Solución.** Ambas salidas se comparan con $h(a)$; la suma de los dos errores estrictos menores que $\varepsilon/2$ es menor que $\varepsilon$.

### Microcontrol 022

[]{#MA-MIC-ANM-01-017-022}

[]{#MA-MSOL-ANM-01-017-022}

**Pregunta.** ¿Se usa la recíproca secuencial para Heine–Cantor?

**Solución.** No. La prueba reduce una familia explícita de bolas por compacidad y usa el mínimo de una lista finita.

### Microcontrol 023

[]{#MA-MIC-ANM-01-017-023}

[]{#MA-MSOL-ANM-01-017-023}

**Pregunta.** ¿Necesita $K$ ser un intervalo?

**Solución.** No. Compactos con varias piezas o conjuntos finitos admiten el mismo argumento.

### Microcontrol 024

[]{#MA-MIC-ANM-01-017-024}

[]{#MA-MSOL-ANM-01-017-024}

**Pregunta.** ¿Compacidad es necesaria para uniformidad de una función particular?

**Solución.** No. La identidad en toda $\mathbb R$ es uniforme con $\delta=\varepsilon$, aunque su dominio no sea compacto.

## §17.4 — Medir la oscilación a cada escala

### Microcontrol 025

[]{#MA-MIC-ANM-01-017-025}

[]{#MA-MSOL-ANM-01-017-025}

[]{#MA-SEC-ANM-01-017-004}

**Pregunta.** ¿Qué garantiza que el módulo global definido sea real finito?

**Solución.** En el marco usado, $D$ no vacío y $|f|\le B$: las diferencias contienen cero y están acotadas por $2B$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-017-026}

[]{#MA-MSOL-ANM-01-017-026}

**Pregunta.** ¿Qué significa $\omega_f(t)$?

**Solución.** El supremo de todas las diferencias de salida de pares del dominio a distancia a lo sumo $t$. No exige que un par alcance ese supremo.

### Microcontrol 027

[]{#MA-MIC-ANM-01-017-027}

[]{#MA-MSOL-ANM-01-017-027}

**Pregunta.** ¿Por qué $\omega_f(0)=0$?

**Solución.** La distancia cero implica $x=y$, así todas las diferencias del conjunto son cero. Para dominio vacío se fijó módulo cero por convención.

### Microcontrol 028

[]{#MA-MIC-ANM-01-017-028}

[]{#MA-MSOL-ANM-01-017-028}

**Pregunta.** ¿Por qué el módulo no decrece?

**Solución.** Al aumentar $t$ se admiten todos los pares anteriores y quizá otros; el supremo de un conjunto contenido no supera el del mayor.

### Microcontrol 029

[]{#MA-MIC-ANM-01-017-029}

[]{#MA-MSOL-ANM-01-017-029}

**Pregunta.** ¿Por qué una cota estricta de todos los valores no da supremo estrictamente menor?

**Solución.** Por ejemplo, todos los valores de $[0,1)$ son menores que uno pero su supremo es uno. Se usa presupuesto $\varepsilon/2$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-017-030}

[]{#MA-MSOL-ANM-01-017-030}

**Pregunta.** ¿Cómo da uniformidad el límite del módulo en cero?

**Solución.** Se toma una escala $t>0$ con $\omega_f(t)<\varepsilon$ y se fija $\delta=t$; los pares con distancia menor que ella tienen error a lo sumo ese módulo.

### Microcontrol 031

[]{#MA-MIC-ANM-01-017-031}

[]{#MA-MSOL-ANM-01-017-031}

**Pregunta.** ¿Qué par alcanza el módulo de $x^2$ en $[0,1]$ para $0\le t\le1$?

**Solución.** El par $1,1-t$ tiene distancia $t$ y diferencia $2t-t^2$, igual a la cota probada para todos los pares.

### Microcontrol 032

[]{#MA-MIC-ANM-01-017-032}

[]{#MA-MSOL-ANM-01-017-032}

**Pregunta.** ¿Uniformidad obliga a valores acotados en todo dominio?

**Solución.** No: la identidad uniforme en $\mathbb R$ es no acotada, aunque sí tiene módulo finito $\omega(t)=t$.

## §17.5 — Transportar tolerancias por operaciones

### Microcontrol 033

[]{#MA-MIC-ANM-01-017-033}

[]{#MA-MSOL-ANM-01-017-033}

[]{#MA-SEC-ANM-01-017-005}

**Pregunta.** ¿Cómo se combinan dos radios para una suma?

**Solución.** Se pide error $\varepsilon/2$ a cada sumando y se toma el mínimo de los dos radios positivos.

### Microcontrol 034

[]{#MA-MIC-ANM-01-017-034}

[]{#MA-MSOL-ANM-01-017-034}

**Pregunta.** ¿Qué hipótesis suficientes se añaden para productos?

**Solución.** Cotas globales $M_f,M_g$ de los valores; controlan los factores que multiplican las diferencias en la identidad de producto.

### Microcontrol 035

[]{#MA-MIC-ANM-01-017-035}

[]{#MA-MSOL-ANM-01-017-035}

**Pregunta.** ¿Qué producto refuta conservación automática en dominios arbitrarios?

**Solución.** La identidad por sí misma en $\mathbb R$: ambos factores son uniformes, pero su producto $x^2$ no lo es.

### Microcontrol 036

[]{#MA-MIC-ANM-01-017-036}

[]{#MA-MSOL-ANM-01-017-036}

**Pregunta.** ¿Qué dato positivo controla un recíproco?

**Solución.** Un margen global $|g(x)|\ge m>0$; entonces la diferencia de recíprocos es a lo sumo la diferencia de $g$ dividida por $m^2$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-017-037}

[]{#MA-MSOL-ANM-01-017-037}

**Pregunta.** ¿Ausencia de ceros basta para ese margen?

**Solución.** No. $g(x)=x$ en $(0,1]$ nunca vale cero pero tiene valores positivos arbitrariamente pequeños.

### Microcontrol 038

[]{#MA-MIC-ANM-01-017-038}

[]{#MA-MSOL-ANM-01-017-038}

**Pregunta.** ¿Qué tolerancia se elige primero en una composición?

**Solución.** La tolerancia intermedia $\eta$ que produce error final $\varepsilon$ en la función exterior; después el radio de la interior que produce error menor que $\eta$.

### Microcontrol 039

[]{#MA-MIC-ANM-01-017-039}

[]{#MA-MSOL-ANM-01-017-039}

**Pregunta.** ¿Qué dominio basta controlar uniformemente para la función exterior?

**Solución.** La imagen $f[D]$, porque sólo esos valores se usan al evaluar $g\circ f$.

### Microcontrol 040

[]{#MA-MIC-ANM-01-017-040}

[]{#MA-MSOL-ANM-01-017-040}

**Pregunta.** ¿Por qué una inversa compacta continua es también uniforme?

**Solución.** La imagen $H$ es compacta por C16 y la inversa es continua allí; Heine–Cantor se aplica con dominio $H$.

## §17.6 — Pares próximos y rutas dadas

### Microcontrol 041

[]{#MA-MIC-ANM-01-017-041}

[]{#MA-MSOL-ANM-01-017-041}

[]{#MA-SEC-ANM-01-017-006}

**Pregunta.** ¿Deben converger las dos rutas próximas de R6?

**Solución.** No. Sólo se exige que su distancia mutua tienda a cero; pueden escaparse al infinito.

### Microcontrol 042

[]{#MA-MIC-ANM-01-017-042}

[]{#MA-MSOL-ANM-01-017-042}

**Pregunta.** ¿Dónde se gasta selección en la recíproca general?

**Solución.** Primero al escoger $x_n\in A_n$ y después $y_n\in B_n$. Ambas familias reales no vacías se seleccionan bajo la premisa local CC(R).

### Microcontrol 043

[]{#MA-MIC-ANM-01-017-043}

[]{#MA-MSOL-ANM-01-017-043}

**Pregunta.** ¿Qué reemplaza CC(R) con una enumeración dada?

**Solución.** El menor índice de la primera entrada que tiene un compañero malo, y luego el menor índice de ese compañero. La sobreyección dada garantiza existencia.

### Microcontrol 044

[]{#MA-MIC-ANM-01-017-044}

[]{#MA-MSOL-ANM-01-017-044}

**Pregunta.** ¿Qué diferencia de salida tienen los pares del cuadrado que escapan?

**Solución.** Para $x_n=n+1$, $y_n=x_n+1/(n+1)$, es $2+1/(n+1)^2\ge2$, aunque la distancia de entrada tiende a cero.

### Microcontrol 045

[]{#MA-MIC-ANM-01-017-045}

[]{#MA-MSOL-ANM-01-017-045}

**Pregunta.** ¿Por qué una uniforme preserva una ruta de Cauchy?

**Solución.** El radio uniforme para $\varepsilon$ se inserta en la condición de Cauchy de entrada, y desde un mismo índice controla todos los pares de términos de salida.

### Microcontrol 046

[]{#MA-MIC-ANM-01-017-046}

[]{#MA-MSOL-ANM-01-017-046}

**Pregunta.** ¿Esa preservación caracteriza uniformidad en toda $\mathbb R$?

**Solución.** No. El cuadrado preserva rutas de Cauchy porque cada una está acotada y allí tiene constante Lipschitz, pero no es uniforme en toda la recta.

### Microcontrol 047

[]{#MA-MIC-ANM-01-017-047}

[]{#MA-MSOL-ANM-01-017-047}

**Pregunta.** ¿Por qué las diferencias de salida separadas refutan uniformidad sin recíproca?

**Solución.** Basta la implicación directa R6: si la función fuera uniforme, esos pares dados tendrían diferencias tendentes a cero, contradicción.

### Microcontrol 048

[]{#MA-MIC-ANM-01-017-048}

[]{#MA-MSOL-ANM-01-017-048}

**Pregunta.** ¿Qué valor evita el problema del índice inicial cero?

**Solución.** Las escalas son $1/(n+1)$ y los pares recíprocos usan $n+2,n+3$; no se divide por $n$ cuando $n=0$.

## §17.7 — Completar el dominio sin seleccionar aproximantes

### Microcontrol 049

[]{#MA-MIC-ANM-01-017-049}

[]{#MA-MSOL-ANM-01-017-049}

[]{#MA-SEC-ANM-01-017-007}

**Pregunta.** ¿Qué garantiza que $E_{p,r}$ no sea vacía?

**Solución.** $p\in\overline D$: toda bola positiva centrada en $p$ toca $D$, por lo que su imagen tiene un valor.

### Microcontrol 050

[]{#MA-MIC-ANM-01-017-050}

[]{#MA-MSOL-ANM-01-017-050}

**Pregunta.** ¿Cómo se acotan las imágenes locales sin elegir aproximantes globales?

**Solución.** Para un $p$ fijado se usa una entrada $a$ en la bola inicial; uniformidad con error uno acota todos sus valores por $f(a)\pm1$. No se forma una familia $a_p$.

### Microcontrol 051

[]{#MA-MIC-ANM-01-017-051}

[]{#MA-MSOL-ANM-01-017-051}

**Pregunta.** ¿Qué corte define el valor extendido?

**Solución.** $F(p)=\sup\{L_{p,r}:0<r\le r_0\}$, con $L_{p,r}$ el ínfimo de la imagen local no vacía y acotada.

### Microcontrol 052

[]{#MA-MIC-ANM-01-017-052}

[]{#MA-MSOL-ANM-01-017-052}

**Pregunta.** ¿Por qué ese corte no supera ningún $U_{p,r}$?

**Solución.** Para toda otra escala $s$, la imagen de la bola de radio $\min(r,s)$ es no vacía y está en ambas imágenes; así $L_{p,s}\le U_{p,r}$ y ese supremo acota todo el corte.

### Microcontrol 053

[]{#MA-MIC-ANM-01-017-053}

[]{#MA-MSOL-ANM-01-017-053}

**Pregunta.** ¿Qué hace único al valor entre todos los intervalos?

**Solución.** Sus anchuras pueden ser menores que cualquier distancia positiva; dos valores distintos no cabrían en uno de esos intervalos suficientemente estrechos.

### Microcontrol 054

[]{#MA-MIC-ANM-01-017-054}

[]{#MA-MSOL-ANM-01-017-054}

**Pregunta.** ¿Por qué la extensión coincide con $f$ en $D$?

**Solución.** Si $p\in D$, $f(p)$ pertenece a toda imagen local y queda entre sus ínfimos/supremos. La unicidad identifica ese valor con $F(p)$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-017-055}

[]{#MA-MSOL-ANM-01-017-055}

**Pregunta.** ¿Qué radio uniforme sobre el cierre se obtiene en la prueba?

**Solución.** Para un radio $\delta$ que controla $f$ con error $\varepsilon/3$, sirve $\Delta=\delta/3$; vecindades pequeñas de ambos puntos mantienen todos los pares cruzados dentro de $\delta$.

### Microcontrol 056

[]{#MA-MIC-ANM-01-017-056}

[]{#MA-MSOL-ANM-01-017-056}

**Pregunta.** ¿Se necesita una sucesión aproximante por punto de frontera?

**Solución.** No. Se usan todas las imágenes locales, supremos/ínfimos y un valor único por fórmula; no se seleccionan rutas.

## §17.8 — Datos finitos y aproximaciones poligonales

### Microcontrol 057

[]{#MA-MIC-ANM-01-017-057}

[]{#MA-MSOL-ANM-01-017-057}

[]{#MA-SEC-ANM-01-017-008}

**Pregunta.** ¿Qué condición cumple el paso de la malla?

**Solución.** $h=(b-a)/n<\delta$, donde $\delta$ es el radio uniforme para el presupuesto $\varepsilon/2$ y $n\ge1$.

### Microcontrol 058

[]{#MA-MIC-ANM-01-017-058}

[]{#MA-MSOL-ANM-01-017-058}

**Pregunta.** ¿Por qué coinciden las fórmulas de dos celdas en un nodo?

**Solución.** Una da peso uno al extremo derecho y la otra peso uno al extremo izquierdo; ambas dan el valor de $f$ en el nodo común.

### Microcontrol 059

[]{#MA-MIC-ANM-01-017-059}

[]{#MA-MSOL-ANM-01-017-059}

**Pregunta.** ¿Qué mantiene a $\theta$ entre cero y uno?

**Solución.** $x\in[t_j,t_{j+1}]$ y $h>0$, por lo que $0\le x-t_j\le h$ y $\theta=(x-t_j)/h\in[0,1]$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-017-060}

[]{#MA-MSOL-ANM-01-017-060}

**Pregunta.** ¿Cómo se controla el error entre las muestras?

**Solución.** Ambos extremos distan a lo sumo $h<\delta$ de $x$; sus errores son menores que $\varepsilon/2$ y la combinación convexa mantiene esa cota.

### Microcontrol 061

[]{#MA-MIC-ANM-01-017-061}

[]{#MA-MSOL-ANM-01-017-061}

**Pregunta.** ¿Por qué el pegado poligonal es continuo?

**Solución.** Cada rama afín lo es, sus valores coinciden en nodos y C14 permite el pegado finito sobre las celdas cerradas relativas.

### Microcontrol 062

[]{#MA-MIC-ANM-01-017-062}

[]{#MA-MSOL-ANM-01-017-062}

**Pregunta.** ¿Cuál es el error máximo del cuadrado con cuatro celdas iguales?

**Solución.** $h=1/4$, por lo que $h^2/4=1/64$, alcanzado en los medios de cada celda.

### Microcontrol 063

[]{#MA-MIC-ANM-01-017-063}

[]{#MA-MSOL-ANM-01-017-063}

**Pregunta.** ¿Por qué muestras finitas sin escala no dan error certificado?

**Solución.** Entre dos nodos se puede insertar un pico triangular continuo de altura arbitraria que siga valiendo cero en todos los nodos.

### Microcontrol 064

[]{#MA-MIC-ANM-01-017-064}

[]{#MA-MSOL-ANM-01-017-064}

**Pregunta.** ¿Qué aproximante sirve en un segmento degenerado?

**Solución.** La constante con valor $f(a)$ en $[a,a]$ tiene error cero; no se divide por una longitud de malla cero.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html)
