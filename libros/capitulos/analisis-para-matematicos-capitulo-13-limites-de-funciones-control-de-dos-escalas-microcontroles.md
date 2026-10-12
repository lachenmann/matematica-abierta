---
content-id: MA-BCH-0257
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-013-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 13
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C13_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §13.1 — Aproximarse sin tocar el centro

### Microcontrol 001

[]{#MA-MIC-ANM-01-013-001}

[]{#MA-MSOL-ANM-01-013-001}

[]{#MA-SEC-ANM-01-013-001}

**Pregunta.** ¿Tiene que pertenecer $a$ al dominio para preguntar por el límite en $a$?

**Solución.** No. Debe ser punto de acumulación del dominio. Por ejemplo, $0\notin(0,\infty)$ y cada radio positivo contiene una entrada positiva distinta de cero.

### Microcontrol 002

[]{#MA-MIC-ANM-01-013-002}

[]{#MA-MSOL-ANM-01-013-002}

**Pregunta.** ¿Qué elimina $0<|x-a|$?

**Solución.** Elimina $x=a$; asegura que sólo se usan entradas distintas del centro.

### Microcontrol 003

[]{#MA-MIC-ANM-01-013-003}

[]{#MA-MSOL-ANM-01-013-003}

**Pregunta.** ¿Qué significa $a\in D^{\prime}$ en forma cuantificada?

**Solución.** $\forall r>0\ \exists x\in D:0<|x-a|<r$. Toda ventana perforada contiene una entrada.

### Microcontrol 004

[]{#MA-MIC-ANM-01-013-004}

[]{#MA-MSOL-ANM-01-013-004}

**Pregunta.** Si $D=\{a\}$, ¿la fórmula perforada distingue un candidato $L$?

**Solución.** No. Su antecedente nunca se cumple, por lo que vale por vacuidad para todo $L$. Nuestra definición no asigna límite en ese caso.

### Microcontrol 005

[]{#MA-MIC-ANM-01-013-005}

[]{#MA-MSOL-ANM-01-013-005}

**Pregunta.** ¿Cómo se escribe el control mediante imágenes de ventanas?

**Solución.** Para cada $\varepsilon>0$ hay $\delta>0$ con $f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-013-006}

[]{#MA-MSOL-ANM-01-013-006}

**Pregunta.** ¿Qué preimagen contiene la ventana perforada cuando el radio es válido?

**Solución.** $f^{-1}[B(L,\varepsilon)]$. Cada entrada de la ventana produce una salida en esa bola.

### Microcontrol 007

[]{#MA-MIC-ANM-01-013-007}

[]{#MA-MSOL-ANM-01-013-007}

**Pregunta.** ¿Cambia el límite si sólo cambiamos $f(a)$?

**Solución.** No. Las entradas que evalúa la definición son distintas de $a$, por lo que sus valores permanecen iguales.

### Microcontrol 008

[]{#MA-MIC-ANM-01-013-008}

[]{#MA-MSOL-ANM-01-013-008}

**Pregunta.** ¿Qué radio reúne coincidencia local y control de $f$?

**Solución.** $\min(r,\delta_f)$, donde $r>0$ es el radio de coincidencia y $\delta_f>0$ controla el error. Así se cumplen las dos condiciones.

## §13.2 — Diseñar una respuesta para toda la ventana

### Microcontrol 009

[]{#MA-MIC-ANM-01-013-009}

[]{#MA-MSOL-ANM-01-013-009}

[]{#MA-SEC-ANM-01-013-002}

**Pregunta.** ¿Puede $\delta$ depender de la entrada $x$ bajo el cuantificador universal?

**Solución.** No. Se fija antes de verificar toda entrada. Puede depender de $\varepsilon$ y de los datos fijados.

### Microcontrol 010

[]{#MA-MIC-ANM-01-013-010}

[]{#MA-MSOL-ANM-01-013-010}

**Pregunta.** Para $f(x)=3x-2$ en $a=1$, ¿qué radio explícito sirve?

**Solución.** $\delta=\varepsilon/3$, pues $|f(x)-1|=3|x-1|<3\delta=\varepsilon$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-013-011}

[]{#MA-MSOL-ANM-01-013-011}

**Pregunta.** ¿Es válido exigir un solo $\delta>0$ para todas las tolerancias?

**Solución.** Es una condición más fuerte. Para una afín no constante no existe tal radio: una entrada no central dentro de él tiene error positivo, y una tolerancia menor lo refuta.

### Microcontrol 012

[]{#MA-MIC-ANM-01-013-012}

[]{#MA-MSOL-ANM-01-013-012}

**Pregunta.** ¿Qué ocurre con la afín si $m=0$?

**Solución.** Es constante y su error respecto de $c$ es cero; cualquier radio positivo sirve.

### Microcontrol 013

[]{#MA-MIC-ANM-01-013-013}

[]{#MA-MSOL-ANM-01-013-013}

**Pregunta.** ¿Qué cota para $|x+a|$ produce $|x-a|<1$?

**Solución.** $|x+a|\le |x-a|+2|a|<1+2|a|$. Esa constante permite controlar el producto de errores.

### Microcontrol 014

[]{#MA-MIC-ANM-01-013-014}

[]{#MA-MSOL-ANM-01-013-014}

**Pregunta.** ¿Por qué se toma un mínimo en la prueba del cuadrado?

**Solución.** Para asegurar a la vez el radio auxiliar $1$ y el radio de precisión $\varepsilon/(1+2|a|)$.

### Microcontrol 015

[]{#MA-MIC-ANM-01-013-015}

[]{#MA-MSOL-ANM-01-013-015}

**Pregunta.** ¿Un radio válido debe ser el máximo posible?

**Solución.** No. Basta un radio positivo cuyo control universal se pueda verificar; cualquier reducción positiva también sirve.

### Microcontrol 016

[]{#MA-MIC-ANM-01-013-016}

[]{#MA-MSOL-ANM-01-013-016}

**Pregunta.** ¿Qué barrera protege $1/x$ si $|x-a|<|a|/2$ y $a\ne0$?

**Solución.** $|x|\ge |a|-|x-a|>|a|/2>0$, de modo que el denominador está separado de cero uniformemente en la ventana.

## §13.3 — Un destino, barreras locales y orden

### Microcontrol 017

[]{#MA-MIC-ANM-01-013-017}

[]{#MA-MSOL-ANM-01-013-017}

[]{#MA-SEC-ANM-01-013-003}

**Pregunta.** ¿Dónde se utiliza acumulación al demostrar unicidad?

**Solución.** Al obtener una entrada en el mínimo de los dos radios. Sin esa entrada, las dos cotas no podrían compararse.

### Microcontrol 018

[]{#MA-MIC-ANM-01-013-018}

[]{#MA-MSOL-ANM-01-013-018}

**Pregunta.** ¿Qué tolerancia se usa para dos destinos separados por $d>0$?

**Solución.** $\varepsilon=d/3$. Las dos distancias a una salida común suman menos que $2d/3<d$, contradicción.

### Microcontrol 019

[]{#MA-MIC-ANM-01-013-019}

[]{#MA-MSOL-ANM-01-013-019}

**Pregunta.** ¿Un límite finito implica acotación global?

**Solución.** No. Sólo proporciona acotación en alguna ventana perforada; $x^2$ tiene límite cero en cero y no está acotada en $\mathbb R$.

### Microcontrol 020

[]{#MA-MIC-ANM-01-013-020}

[]{#MA-MSOL-ANM-01-013-020}

**Pregunta.** ¿Qué cota local sale del desafío $\varepsilon=1$?

**Solución.** $|f(x)|<|L|+1$ cerca del centro, al usar $|f(x)|\le|f(x)-L|+|L|$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-013-021}

[]{#MA-MSOL-ANM-01-013-021}

**Pregunta.** ¿El orden estricto $f(x)<g(x)$ obliga $L<M$?

**Solución.** No. Por ejemplo $f(x)=0$, $g(x)=x$ en $(0,\infty)$ tienen límite cero en cero.

### Microcontrol 022

[]{#MA-MIC-ANM-01-013-022}

[]{#MA-MSOL-ANM-01-013-022}

**Pregunta.** ¿Qué hay que suponer de $f$ antes de usar el encierro?

**Solución.** Que esté entre las dos barreras localmente, con el mismo dominio pertinente. No se supone que ya tenga límite: el argumento construye su convergencia.

### Microcontrol 023

[]{#MA-MIC-ANM-01-013-023}

[]{#MA-MSOL-ANM-01-013-023}

**Pregunta.** Si $|b(x)|\le K$ cerca de cero, ¿qué error controla $xb(x)$?

**Solución.** $|xb(x)|\le K|x|$. Para $K>0$ se usa $\delta\le\varepsilon/K$; para $K=0$ el error es cero.

### Microcontrol 024

[]{#MA-MIC-ANM-01-013-024}

[]{#MA-MSOL-ANM-01-013-024}

**Pregunta.** ¿Necesita $b$ tener límite para que $xb(x)\to0$?

**Solución.** No. Basta su acotación local, que domina la oscilación por un factor que se hace pequeño.

## §13.4 — Negar un candidato y construir infracciones

### Microcontrol 025

[]{#MA-MIC-ANM-01-013-025}

[]{#MA-MSOL-ANM-01-013-025}

[]{#MA-SEC-ANM-01-013-004}

**Pregunta.** ¿Cuál es el orden de cuantificadores al refutar un candidato?

**Solución.** $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$. La tolerancia queda fija y el infractor puede depender del radio.

### Microcontrol 026

[]{#MA-MIC-ANM-01-013-026}

[]{#MA-MSOL-ANM-01-013-026}

**Pregunta.** ¿Por qué la negación usa $\ge\varepsilon_0$?

**Solución.** Porque negar $|f(x)-L|<\varepsilon_0$ en el orden real da $|f(x)-L|\ge\varepsilon_0$. La frontera también infringe una bola abierta.

### Microcontrol 027

[]{#MA-MIC-ANM-01-013-027}

[]{#MA-MSOL-ANM-01-013-027}

**Pregunta.** ¿Refutar $L=0$ basta para demostrar que no existe ningún límite?

**Solución.** No. Otro real podría ser límite. Hay que descartar todos los candidatos o usar una contradicción independiente del candidato.

### Microcontrol 028

[]{#MA-MIC-ANM-01-013-028}

[]{#MA-MSOL-ANM-01-013-028}

**Pregunta.** ¿Por qué usamos $1/(n+1)$ en vez de $1/n$ desde $n=0$?

**Solución.** Porque $n+1>0$ para todos los índices, mientras $1/0$ no está definido.

### Microcontrol 029

[]{#MA-MIC-ANM-01-013-029}

[]{#MA-MSOL-ANM-01-013-029}

**Pregunta.** ¿Qué prueba la no vaciedad de todos los conjuntos $E_n$?

**Solución.** Que el candidato falla. Para cualquier radio elegimos una escala menor y un único infractor de ese conjunto.

### Microcontrol 030

[]{#MA-MIC-ANM-01-013-030}

[]{#MA-MSOL-ANM-01-013-030}

**Pregunta.** ¿La no vaciedad de cada $E_n$ proporciona por sí sola un selector?

**Solución.** No. $\forall n\exists x\in E_n$ no permite intercambiar cuantificadores sin una regla de selección o una hipótesis adicional.

### Microcontrol 031

[]{#MA-MIC-ANM-01-013-031}

[]{#MA-MSOL-ANM-01-013-031}

**Pregunta.** Para el salto con valores $\pm1$, ¿por qué una distancia a $L$ es al menos $1$?

**Solución.** Si ambas fueran menores que $1$, la triangular daría $2=|1-(-1)|<2$, contradicción.

### Microcontrol 032

[]{#MA-MIC-ANM-01-013-032}

[]{#MA-MSOL-ANM-01-013-032}

**Pregunta.** ¿Qué asegura $x=\min(\delta/2,1/[2(|L|+1)])$ en la refutación de $1/x$?

**Solución.** $0<x<\delta$ y $1/x\ge2(|L|+1)$, luego $|1/x-L|>1$. Funciona para cualquier candidato real.

## §13.5 — Lo que detectan las sucesiones

### Microcontrol 033

[]{#MA-MIC-ANM-01-013-033}

[]{#MA-MSOL-ANM-01-013-033}

[]{#MA-SEC-ANM-01-013-005}

**Pregunta.** ¿Qué tres condiciones hacen admisible a $(x_n)$?

**Solución.** $x_n\in D$, $x_n\ne a$ para todos los índices y $x_n\to a$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-013-034}

[]{#MA-MSOL-ANM-01-013-034}

**Pregunta.** ¿Cómo se encadenan $\varepsilon$, $\delta$ y $N$ en la dirección directa?

**Solución.** $\varepsilon$ exige un radio $\delta$ para la función; la convergencia de entradas proporciona $N$ para ese radio; la cola cumple el error de salida.

### Microcontrol 035

[]{#MA-MIC-ANM-01-013-035}

[]{#MA-MSOL-ANM-01-013-035}

**Pregunta.** ¿Por qué la sucesión constante $x_n=a$ no es admisible?

**Solución.** Porque alcanza siempre el centro excluido. Evaluaría $f(a)$, un dato que el límite perforado no controla.

### Microcontrol 036

[]{#MA-MIC-ANM-01-013-036}

[]{#MA-MSOL-ANM-01-013-036}

**Pregunta.** Si una ruta admisible tiene imágenes que no convergen a $L$, ¿qué concluyes?

**Solución.** Que $L$ no puede ser el límite funcional. Si lo fuera, la dirección directa controlaría también esa ruta.

### Microcontrol 037

[]{#MA-MIC-ANM-01-013-037}

[]{#MA-MSOL-ANM-01-013-037}

**Pregunta.** ¿Qué regla elige infractores cuando está dada $e:\mathbb N\to D$ sobreyectiva?

**Solución.** $k_n=\min\{k:e(k)\in E_n\}$ y $x_n=e(k_n)$. La no vaciedad garantiza un mínimo natural único.

### Microcontrol 038

[]{#MA-MIC-ANM-01-013-038}

[]{#MA-MSOL-ANM-01-013-038}

**Pregunta.** ¿Deben crecer estrictamente los $k_n$ de ese selector?

**Solución.** No. No se está construyendo una subsucesión de $e$; se escoge una entrada que infringe cada escala.

### Microcontrol 039

[]{#MA-MIC-ANM-01-013-039}

[]{#MA-MSOL-ANM-01-013-039}

**Pregunta.** ¿Qué hipótesis permite la recíproca en cualquier dominio real?

**Solución.** $\mathrm{CC}(\mathbb R)$, aplicada explícitamente a la familia de conjuntos reales no vacíos $E_n$. El teorema es condicional a esa hipótesis.

### Microcontrol 040

[]{#MA-MIC-ANM-01-013-040}

[]{#MA-MSOL-ANM-01-013-040}

**Pregunta.** ¿Necesita elección numerable la refutación por las rutas $\pm1/(n+1)$?

**Solución.** No. Las dos rutas están dadas por fórmulas y la dirección directa basta para comparar sus destinos distintos.

## §13.6 — Combinar límites con presupuestos de error

### Microcontrol 041

[]{#MA-MIC-ANM-01-013-041}

[]{#MA-MSOL-ANM-01-013-041}

[]{#MA-SEC-ANM-01-013-006}

**Pregunta.** ¿Cómo se reparte $\varepsilon$ en una suma?

**Solución.** Con errores menores que $\varepsilon/2$ para cada sumando y el mínimo de ambos radios.

### Microcontrol 042

[]{#MA-MIC-ANM-01-013-042}

[]{#MA-MSOL-ANM-01-013-042}

**Pregunta.** ¿Cómo se trata la multiplicación por una constante nula?

**Solución.** Por separado: el error de la función cero es cero, sin dividir por la constante.

### Microcontrol 043

[]{#MA-MIC-ANM-01-013-043}

[]{#MA-MSOL-ANM-01-013-043}

**Pregunta.** ¿Qué identidad prepara el producto?

**Solución.** $fg-LM=f(g-M)+M(f-L)$. Se controla $f$ con una barrera local y los dos errores con radios.

### Microcontrol 044

[]{#MA-MIC-ANM-01-013-044}

[]{#MA-MSOL-ANM-01-013-044}

**Pregunta.** ¿Por qué $|M|+1$ es útil en el presupuesto de producto?

**Solución.** Es positivo incluso si $M=0$, y domina $|M|$. Permite dividir por una constante segura.

### Microcontrol 045

[]{#MA-MIC-ANM-01-013-045}

[]{#MA-MSOL-ANM-01-013-045}

**Pregunta.** ¿Qué tolerancia garantiza que $g$ no se anule si $M\ne0$?

**Solución.** $|g-M|<|M|/2$, que implica $|g|>|M|/2>0$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-013-046}

[]{#MA-MSOL-ANM-01-013-046}

**Pregunta.** ¿Cuál es el dominio correcto de $f/g$?

**Solución.** $D_0=\{x\in D:g(x)\ne0\}$. Si $M\ne0$, incluye toda una ventana perforada del dominio original.

### Microcontrol 047

[]{#MA-MIC-ANM-01-013-047}

[]{#MA-MSOL-ANM-01-013-047}

**Pregunta.** ¿Qué sucede con el cociente si el límite del denominador es cero?

**Solución.** La regla no se aplica. Puede haber cancelación y límite finito, o puede faltar límite; hace falta otro argumento.

### Microcontrol 048

[]{#MA-MIC-ANM-01-013-048}

[]{#MA-MSOL-ANM-01-013-048}

**Pregunta.** ¿Necesita la regla de producto el criterio secuencial recíproco?

**Solución.** No. Se demostró directamente con radios, cota local e identidades algebraicas.

## §13.7 — Cambiar las rutas disponibles

### Microcontrol 049

[]{#MA-MIC-ANM-01-013-049}

[]{#MA-MSOL-ANM-01-013-049}

[]{#MA-SEC-ANM-01-013-007}

**Pregunta.** ¿Qué condición adicional se exige al restringir a $A\subseteq D$?

**Solución.** $a\in A'$. Garantiza una pregunta de límite no vacía en el dominio restringido.

### Microcontrol 050

[]{#MA-MIC-ANM-01-013-050}

[]{#MA-MSOL-ANM-01-013-050}

**Pregunta.** ¿Por qué sirve reunir finitos radios positivos mediante un mínimo?

**Solución.** Porque su mínimo sigue siendo positivo y garantiza simultáneamente todos los controles locales.

### Microcontrol 051

[]{#MA-MIC-ANM-01-013-051}

[]{#MA-MSOL-ANM-01-013-051}

**Pregunta.** ¿Un mínimo de infinitos radios positivos tiene que ser positivo?

**Solución.** No. Los radios $1/(n+1)$ son positivos y no tienen ninguna cota inferior positiva.

### Microcontrol 052

[]{#MA-MIC-ANM-01-013-052}

[]{#MA-MSOL-ANM-01-013-052}

**Pregunta.** ¿Cuándo está definido el límite por la izquierda bajo nuestra convención?

**Solución.** Cuando $a$ es punto de acumulación de $D\cap(-\infty,a)$. No basta que el lado esté nombrado.

### Microcontrol 053

[]{#MA-MIC-ANM-01-013-053}

[]{#MA-MSOL-ANM-01-013-053}

**Pregunta.** Si ambos lados acumulan, ¿qué permite reunirlos?

**Solución.** Que ambos límites laterales sean el mismo $L$. Se usa el mínimo de sus radios y toda entrada perforada pertenece a uno de los lados.

### Microcontrol 054

[]{#MA-MIC-ANM-01-013-054}

[]{#MA-MSOL-ANM-01-013-054}

**Pregunta.** Si un lado no acumula, ¿qué información local ofrece?

**Solución.** Existe un radio positivo sin entradas de ese lado. En una ventana suficientemente pequeña sólo importa el otro lado.

### Microcontrol 055

[]{#MA-MIC-ANM-01-013-055}

[]{#MA-MSOL-ANM-01-013-055}

**Pregunta.** ¿Probar un límite en un subconjunto denso basta para una función arbitraria?

**Solución.** No. La función puede tener valores distintos en todas las entradas omitidas; el indicador racional de §13.7 es un contraejemplo.

### Microcontrol 056

[]{#MA-MIC-ANM-01-013-056}

[]{#MA-MSOL-ANM-01-013-056}

**Pregunta.** ¿Por qué $\sqrt2/(n+1)$ es irracional para todo índice?

**Solución.** Si fuese racional, multiplicarlo por el entero positivo $n+1$ haría racional a $\sqrt2$, contradicción.

## §13.8 — Componer controles sin perder la perforación

### Microcontrol 057

[]{#MA-MIC-ANM-01-013-057}

[]{#MA-MSOL-ANM-01-013-057}

[]{#MA-SEC-ANM-01-013-008}

**Pregunta.** ¿Qué desafío se presenta a $f$ después de fijar $\varepsilon$ para $g\circ f$?

**Solución.** El radio intermedio $\eta$ que entrega el límite de $g$ para esa tolerancia final.

### Microcontrol 058

[]{#MA-MIC-ANM-01-013-058}

[]{#MA-MSOL-ANM-01-013-058}

**Pregunta.** ¿Qué dato falta si sólo sabemos $|f(x)-b|<\eta$?

**Solución.** Que $f(x)\ne b$, si vamos a usar el límite perforado de $g$. La cercanía sola permite alcanzar el centro.

### Microcontrol 059

[]{#MA-MIC-ANM-01-013-059}

[]{#MA-MSOL-ANM-01-013-059}

**Pregunta.** ¿Qué alternativa permite que $f(x)=b$?

**Solución.** Que $b\in E$ y $g(b)=L$. En ese caso la salida central tiene error exactamente cero.

### Microcontrol 060

[]{#MA-MIC-ANM-01-013-060}

[]{#MA-MSOL-ANM-01-013-060}

**Pregunta.** ¿Qué falla en la composición de una función cero con $g(0)=1$, $g(y)=0$ fuera de cero?

**Solución.** La interior cae siempre en el centro. Aunque ambos límites aislados son cero, la composición es constante uno.

### Microcontrol 061

[]{#MA-MIC-ANM-01-013-061}

[]{#MA-MSOL-ANM-01-013-061}

**Pregunta.** ¿Qué papel desempeña el tipo $f:D\to E$?

**Solución.** Garantiza que $g(f(x))$ esté definido. Una regla algebraica sin pertenencia al dominio de $g$ no basta.

### Microcontrol 062

[]{#MA-MIC-ANM-01-013-062}

[]{#MA-MSOL-ANM-01-013-062}

**Pregunta.** Con $|f(x)-b|\le C|x-a|$, $C>0$, ¿qué radio de precisión sirve?

**Solución.** $\eta_g(\varepsilon)/C$, combinado por mínimo con las restricciones locales. La desigualdad estricta de entrada produce error intermedio menor que $\eta_g(\varepsilon)$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-013-063}

[]{#MA-MSOL-ANM-01-013-063}

**Pregunta.** Si $C=0$ en esa cota, ¿qué ocurre localmente?

**Solución.** $f(x)=b$. El mecanismo de composición necesita $g(b)=L$; la evitación es incompatible con la ventana no vacía.

### Microcontrol 064

[]{#MA-MIC-ANM-01-013-064}

[]{#MA-MSOL-ANM-01-013-064}

**Pregunta.** ¿Qué verifica finalmente un certificado de límite?

**Solución.** Que el radio sea positivo y dependa sólo de datos permitidos, y que todas las entradas del dominio en su ventana perforada satisfagan el error de salida.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-microcontroles.html)
