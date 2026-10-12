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
date-modified: '2026-10-12'
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

El límite observa entradas del dominio arbitrariamente próximas a $a$, no una evaluación en $a$. En el dominio positivo, dado cualquier radio $r>0$, la entrada $r/2$ es positiva y está a distancia menor que $r$ de cero. Así cero acumula entradas aunque no sea una de ellas. La condición de acumulación garantiza que la aproximación tenga contenido; pertenecer al dominio, en cambio, sólo permitiría hablar además del valor central.

### Microcontrol 002

[]{#MA-MIC-ANM-01-013-002}

[]{#MA-MSOL-ANM-01-013-002}

**Pregunta.** ¿Qué elimina $0<|x-a|$?

**Solución.** Elimina $x=a$; asegura que sólo se usan entradas distintas del centro.

La magnitud $|x-a|$ es cero exactamente cuando $x=a$. Pedir que sea positiva descarta esa entrada y deja una ventana perforada. El límite puede coincidir con $f(a)$, diferir de él o existir cuando $f(a)$ ni siquiera está definido. La definición no decide esa relación, porque todas sus estimaciones se aplican a otras entradas. Confundir la ventana con una bola sin perforar añadiría un control sobre el valor central.

### Microcontrol 003

[]{#MA-MIC-ANM-01-013-003}

[]{#MA-MSOL-ANM-01-013-003}

**Pregunta.** ¿Qué significa $a\in D^{\prime}$ en forma cuantificada?

**Solución.** $\forall r>0\ \exists x\in D:0<|x-a|<r$. Toda ventana perforada contiene una entrada.

Primero se recibe un radio positivo arbitrario y después se busca una entrada del dominio distinta del centro dentro de él. El testigo puede variar con el radio; no se exige una entrada que esté en todas las ventanas. La condición significa que ninguna escala positiva agota las aproximaciones disponibles. Si existiera un radio sin esas entradas, el punto no sería de acumulación, aunque perteneciera al dominio como punto aislado.

### Microcontrol 004

[]{#MA-MIC-ANM-01-013-004}

[]{#MA-MSOL-ANM-01-013-004}

**Pregunta.** Si $D=\{a\}$, ¿la fórmula perforada distingue un candidato $L$?

**Solución.** No. Su antecedente nunca se cumple, por lo que vale por vacuidad para todo $L$. Nuestra definición no asigna límite en ese caso.

Para este dominio, ninguna entrada cumple simultáneamente $x\in D$ y $x\ne a$. Por eso la implicación que exige error pequeño nunca encuentra una entrada a la que aplicarse y es verdadera para cualquier candidato. No distingue un destino único. Exigir acumulación elimina esta vacuidad y permite la prueba de unicidad. Bajo la convención del capítulo, en un punto aislado no se declara un límite perforado mediante esa fórmula.

### Microcontrol 005

[]{#MA-MIC-ANM-01-013-005}

[]{#MA-MSOL-ANM-01-013-005}

**Pregunta.** ¿Cómo se escribe el control mediante imágenes de ventanas?

**Solución.** Para cada $\varepsilon>0$ hay $\delta>0$ con $f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$.

La ventana $U_D(a,\delta)=\{x\in D:0<|x-a|<\delta\}$ reúne exactamente las entradas sometidas al control. Pedir que su imagen esté en $B(L,\varepsilon)$ equivale a pedir $|f(x)-L|<\varepsilon$ para cada una. La inclusión es universal: ningún punto de la ventana puede dar una salida fuera de la bola. La escala de entrada se elige para responder a la precisión solicitada en las salidas.

### Microcontrol 006

[]{#MA-MIC-ANM-01-013-006}

[]{#MA-MSOL-ANM-01-013-006}

**Pregunta.** ¿Qué preimagen contiene la ventana perforada cuando el radio es válido?

**Solución.** $f^{-1}[B(L,\varepsilon)]$. Cada entrada de la ventana produce una salida en esa bola.

La preimagen de la bola de salidas es el conjunto de entradas $x\in D$ que satisfacen $|f(x)-L|<\varepsilon$. Si el radio es válido, toda entrada de la ventana perforada pertenece a ese conjunto. Así el control puede expresarse como $U_D(a,\delta)\subseteq f^{-1}[B(L,\varepsilon)]$. Esta formulación no necesita una función inversa: utiliza la preimagen para seleccionar entradas por sus salidas.

### Microcontrol 007

[]{#MA-MIC-ANM-01-013-007}

[]{#MA-MSOL-ANM-01-013-007}

**Pregunta.** ¿Cambia el límite si sólo cambiamos $f(a)$?

**Solución.** No. Las entradas que evalúa la definición son distintas de $a$, por lo que sus valores permanecen iguales.

Si dos funciones coinciden en las entradas distintas de $a$ de una misma ventana, las estimaciones del límite ven exactamente los mismos valores allí. Modificar sólo la evaluación central no cambia ninguna de esas desigualdades. Si se añade o elimina el propio centro del dominio, tampoco cambian las entradas perforadas ni la acumulación. El resultado permite comparar el comportamiento próximo al punto con el dato particular de su evaluación.

### Microcontrol 008

[]{#MA-MIC-ANM-01-013-008}

[]{#MA-MSOL-ANM-01-013-008}

**Pregunta.** ¿Qué radio reúne coincidencia local y control de $f$?

**Solución.** $\min(r,\delta_f)$, donde $r>0$ es el radio de coincidencia y $\delta_f>0$ controla el error. Así se cumplen las dos condiciones.

El radio de coincidencia asegura que podemos sustituir $g(x)$ por $f(x)$; el radio de precisión asegura que este valor está cerca de $L$. Tomar el mínimo mantiene ambas garantías simultáneamente, porque una entrada más cercana que ese mínimo está dentro de las dos ventanas. El mínimo de dos números positivos sigue siendo positivo. Sólo entonces el control de una función se transporta a la otra.

## §13.2 — Diseñar una respuesta para toda la ventana

### Microcontrol 009

[]{#MA-MIC-ANM-01-013-009}

[]{#MA-MSOL-ANM-01-013-009}

[]{#MA-SEC-ANM-01-013-002}

**Pregunta.** ¿Puede $\delta$ depender de la entrada $x$ bajo el cuantificador universal?

**Solución.** No. Se fija antes de verificar toda entrada. Puede depender de $\varepsilon$ y de los datos fijados.

La definición tiene el orden $\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D$. El radio debe responder al desafío antes de considerar la entrada arbitraria y servir para todas las entradas de su ventana. Elegirlo después de conocer cada $x$ cambiaría ese orden e incluso permitiría excluir esa entrada escogiendo un radio menor que su distancia al centro. Eso no demostraría un control común de aproximación.

### Microcontrol 010

[]{#MA-MIC-ANM-01-013-010}

[]{#MA-MSOL-ANM-01-013-010}

**Pregunta.** Para $f(x)=3x-2$ en $a=1$, ¿qué radio explícito sirve?

**Solución.** $\delta=\varepsilon/3$, pues $|f(x)-1|=3|x-1|<3\delta=\varepsilon$.

La salida candidata es $3\cdot1-2=1$. Restarla de la regla da $f(x)-1=3(x-1)$, y al tomar magnitudes el error de salida es tres veces el de entrada. Por eso recibida $\varepsilon>0$ escogemos el radio positivo $\varepsilon/3$. Cualquier entrada con $0<|x-1|<\delta$ cumple el error estricto. La misma elección funciona para toda la ventana y no depende de una entrada concreta.

### Microcontrol 011

[]{#MA-MIC-ANM-01-013-011}

[]{#MA-MSOL-ANM-01-013-011}

**Pregunta.** ¿Es válido exigir un solo $\delta>0$ para todas las tolerancias?

**Solución.** Es una condición más fuerte. Para una afín no constante no existe tal radio: una entrada no central dentro de él tiene error positivo, y una tolerancia menor lo refuta.

En una afín de pendiente $m\ne0$ y dominio real, fijado un radio $\delta>0$ podemos escoger $x=a+\delta/2$. Su error respecto de $ma+c$ es $|m|\delta/2>0$. Una tolerancia igual a la mitad de ese error refuta ese radio. Por tanto una única escala de entrada no puede responder a todas las precisiones. La definición permite que el radio se reduzca a medida que la tolerancia lo exige.

### Microcontrol 012

[]{#MA-MIC-ANM-01-013-012}

[]{#MA-MSOL-ANM-01-013-012}

**Pregunta.** ¿Qué ocurre con la afín si $m=0$?

**Solución.** Es constante y su error respecto de $c$ es cero; cualquier radio positivo sirve.

La asignación se reduce a $f(x)=c$ y el destino es $c$. Para cualquier entrada del dominio, $|f(x)-c|=0$, menor que cualquier tolerancia positiva. Podemos escoger, por ejemplo, $\delta=1$ sin dividir por la pendiente. Como siempre, el centro debe acumular entradas del dominio para formular el límite bajo esta convención. El caso constante separa una estimación trivial de las fórmulas que requieren $|m|>0$.

### Microcontrol 013

[]{#MA-MIC-ANM-01-013-013}

[]{#MA-MSOL-ANM-01-013-013}

**Pregunta.** ¿Qué cota para $|x+a|$ produce $|x-a|<1$?

**Solución.** $|x+a|\le |x-a|+2|a|<1+2|a|$. Esa constante permite controlar el producto de errores.

Escribimos $x+a=(x-a)+2a$. La triangular da $|x+a|\le|x-a|+2|a|$, y la ventana auxiliar de radio uno hace el primer sumando menor que uno. La constante $1+2|a|$ está fijada por el centro y no por la entrada variable. Así la factorización $|x^2-a^2|=|x-a||x+a|$ se convierte en un error pequeño multiplicado por un factor uniformemente acotado.

### Microcontrol 014

[]{#MA-MIC-ANM-01-013-014}

[]{#MA-MSOL-ANM-01-013-014}

**Pregunta.** ¿Por qué se toma un mínimo en la prueba del cuadrado?

**Solución.** Para asegurar a la vez el radio auxiliar $1$ y el radio de precisión $\varepsilon/(1+2|a|)$.

Si sólo usáramos el radio de precisión, quizá no podríamos controlar el factor $|x+a|$. Si sólo usáramos el auxiliar, el error no tendría por qué satisfacer una tolerancia pequeña. Escogemos $\delta=\min\{1,\varepsilon/(1+2|a|)\}$: la primera condición acota el factor y la segunda ajusta la precisión. El denominador es siempre positivo, incluso en $a=0$, y el mínimo también es positivo.

### Microcontrol 015

[]{#MA-MIC-ANM-01-013-015}

[]{#MA-MSOL-ANM-01-013-015}

**Pregunta.** ¿Un radio válido debe ser el máximo posible?

**Solución.** No. Basta un radio positivo cuyo control universal se pueda verificar; cualquier reducción positiva también sirve.

La definición pide existencia de algún radio válido, no una optimización. Si funciona $\delta$, también funciona cualquier $0<\delta'\le\delta$, porque la nueva ventana contiene menos entradas y todas ellas estaban ya controladas. Una elección conservadora puede facilitar las estimaciones sin cambiar la conclusión. Afirmar que un radio es máximo requiere una prueba adicional que descarte todos los radios mayores; no forma parte de demostrar el límite.

### Microcontrol 016

[]{#MA-MIC-ANM-01-013-016}

[]{#MA-MSOL-ANM-01-013-016}

**Pregunta.** ¿Qué barrera protege $1/x$ si $|x-a|<|a|/2$ y $a\ne0$?

**Solución.** $|x|\ge |a|-|x-a|>|a|/2>0$, de modo que el denominador está separado de cero uniformemente en la ventana.

La triangular inversa da $|x|\ge|a|-|x-a|$. Bajo el radio indicado, ese margen supera $|a|/2$, que es positivo porque $a\ne0$. De esta forma todas las entradas de la ventana evitan cero con una misma separación. Entonces $|1/x-1/a|=|x-a|/(|x||a|)$ se domina por $2|x-a|/|a|^2$. La barrera convierte el denominador variable en una constante segura para diseñar el radio de precisión.

## §13.3 — Un destino, barreras locales y orden

### Microcontrol 017

[]{#MA-MIC-ANM-01-013-017}

[]{#MA-MSOL-ANM-01-013-017}

[]{#MA-SEC-ANM-01-013-003}

**Pregunta.** ¿Dónde se utiliza acumulación al demostrar unicidad?

**Solución.** Al obtener una entrada en el mínimo de los dos radios. Sin esa entrada, las dos cotas no podrían compararse.

Los dos candidatos proporcionan radios, pero para confrontar sus estimaciones necesitamos una entrada donde ambas valgan. La acumulación entrega $x\in D$ distinto de $a$ en la ventana de radio mínimo. Su salida sirve entonces como punto intermedio entre los dos candidatos. Si no hubiera entradas, ambos controles serían vacíos y no producirían contradicción. Éste es el lugar concreto donde la hipótesis de acumulación asegura contenido a la prueba.

### Microcontrol 018

[]{#MA-MIC-ANM-01-013-018}

[]{#MA-MSOL-ANM-01-013-018}

**Pregunta.** ¿Qué tolerancia se usa para dos destinos separados por $d>0$?

**Solución.** $\varepsilon=d/3$. Las dos distancias a una salida común suman menos que $2d/3<d$, contradicción.

Si los candidatos son $L$ y $M$ con $d=|L-M|>0$, elegimos radios para tolerancia $d/3$ respecto de cada uno. Una entrada común a ambas ventanas tiene salida $f(x)$ que satisface las dos cotas. La triangular da $d\le|L-f(x)|+|f(x)-M|<2d/3<d$, imposible. La elección divide el presupuesto dejando un margen estricto; no basta hablar de dos destinos cercanos sin fijar una tolerancia que los separe.

### Microcontrol 019

[]{#MA-MIC-ANM-01-013-019}

[]{#MA-MSOL-ANM-01-013-019}

**Pregunta.** ¿Un límite finito implica acotación global?

**Solución.** No. Sólo proporciona acotación en alguna ventana perforada; $x^2$ tiene límite cero en cero y no está acotada en $\mathbb R$.

El límite sólo controla entradas suficientemente cercanas al centro. La función puede crecer sin cota lejos de esa región. Para el cuadrado en cero, $|x|<\sqrt\varepsilon$ implica $x^2<\varepsilon$, lo que prueba el límite. Pero ninguna barrera global domina $x^2$ para todos los reales. La conclusión válida es acotación local perforada, no una propiedad de todo el dominio.

### Microcontrol 020

[]{#MA-MIC-ANM-01-013-020}

[]{#MA-MSOL-ANM-01-013-020}

**Pregunta.** ¿Qué cota local sale del desafío $\varepsilon=1$?

**Solución.** $|f(x)|<|L|+1$ cerca del centro, al usar $|f(x)|\le|f(x)-L|+|L|$.

El desafío uno proporciona un radio donde $|f(x)-L|<1$. Introducimos $L$ en la diferencia y usamos $|f(x)|\le|f(x)-L|+|L|<1+|L|$. Esto acota todas las salidas de esa ventana por la misma constante. No hemos controlado aún el centro excluido ni entradas lejanas. Si el centro pertenece al dominio y queremos incluirlo, basta ampliar la barrera para incorporar también su valor.

### Microcontrol 021

[]{#MA-MIC-ANM-01-013-021}

[]{#MA-MSOL-ANM-01-013-021}

**Pregunta.** ¿El orden estricto $f(x)<g(x)$ obliga $L<M$?

**Solución.** No. Por ejemplo $f(x)=0$, $g(x)=x$ en $(0,\infty)$ tienen límite cero en cero.

En el dominio positivo, cada entrada cumple $0<x$, así que la función cero está estrictamente debajo de la identidad. Sin embargo, ambas se aproximan a cero cuando las entradas se acercan a cero. La diferencia positiva puede hacerse arbitrariamente pequeña y desaparecer en el límite. El orden de límites conserva una desigualdad no estricta: un control estricto entre valores no obliga a mantener separación positiva entre los destinos.

### Microcontrol 022

[]{#MA-MIC-ANM-01-013-022}

[]{#MA-MSOL-ANM-01-013-022}

**Pregunta.** ¿Qué hay que suponer de $f$ antes de usar el encierro?

**Solución.** Que esté entre las dos barreras localmente, con el mismo dominio pertinente. No se supone que ya tenga límite: el argumento construye su convergencia.

Las barreras deben satisfacer $u(x)\le f(x)\le v(x)$ en una ventana pertinente y tender ambas al mismo $L$. Para cada tolerancia tomamos una ventana donde las dos barreras estén cerca de $L$, junto con la de encierro. Entonces $L-\varepsilon<f(x)<L+\varepsilon$. Esa estimación demuestra el límite de $f$ sin suponerlo. El dominio y la acumulación siguen siendo necesarios para que el límite formulado tenga contenido.

### Microcontrol 023

[]{#MA-MIC-ANM-01-013-023}

[]{#MA-MSOL-ANM-01-013-023}

**Pregunta.** Si $|b(x)|\le K$ cerca de cero, ¿qué error controla $xb(x)$?

**Solución.** $|xb(x)|\le K|x|$. Para $K>0$ se usa $\delta\le\varepsilon/K$; para $K=0$ el error es cero.

Si la acotación de $b$ vale en un radio $r$, para $K>0$ tomamos $\delta=\min\{r,\varepsilon/K\}$. Cada entrada perforada de esa ventana satisface $|xb(x)|\le K|x|<\varepsilon$. El mínimo reúne la región de acotación y la precisión. Para $K=0$, $b(x)=0$ en la ventana y el producto ya tiene error cero. Separar ese caso evita una división por cero.

### Microcontrol 024

[]{#MA-MIC-ANM-01-013-024}

[]{#MA-MSOL-ANM-01-013-024}

**Pregunta.** ¿Necesita $b$ tener límite para que $xb(x)\to0$?

**Solución.** No. Basta su acotación local, que domina la oscilación por un factor que se hace pequeño.

Una función localmente acotada puede oscilar sin aproximarse a un único número. Por ejemplo, cerca de cero puede valer uno en entradas racionales y menos uno en irracionales. Al multiplicarla por $x$, el error absoluto queda a lo sumo $|x|$, que se hace pequeño uniformemente. La oscilación no necesita desaparecer por sí sola; basta que su tamaño esté limitado y que el otro factor tienda a cero.

## §13.4 — Negar un candidato y construir infracciones

### Microcontrol 025

[]{#MA-MIC-ANM-01-013-025}

[]{#MA-MSOL-ANM-01-013-025}

[]{#MA-SEC-ANM-01-013-004}

**Pregunta.** ¿Cuál es el orden de cuantificadores al refutar un candidato?

**Solución.** $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$. La tolerancia queda fija y el infractor puede depender del radio.

Fijado el candidato $L$, refutarlo exige una tolerancia positiva que ninguna ventana consiga cumplir. Después de que se proponga cualquier radio, encontramos una entrada $x\in D$ con $0<|x-a|<\delta$ y $|f(x)-L|\ge\varepsilon_0$. El infractor puede cambiar con el radio; la tolerancia no. Esta persistencia a todas las escalas distingue una refutación de observar un único valor lejano al candidato.

### Microcontrol 026

[]{#MA-MIC-ANM-01-013-026}

[]{#MA-MSOL-ANM-01-013-026}

**Pregunta.** ¿Por qué la negación usa $\ge\varepsilon_0$?

**Solución.** Porque negar $|f(x)-L|<\varepsilon_0$ en el orden real da $|f(x)-L|\ge\varepsilon_0$. La frontera también infringe una bola abierta.

La bola de precisión usa desigualdad estricta. Su complemento incluye tanto salidas más lejanas como las que quedan exactamente en su frontera. Por ejemplo, un error igual a uno incumple el desafío $\varepsilon_0=1$. Si en la negación exigiéramos sólo errores mayores que la tolerancia, eliminaríamos infractores legítimos. La inversión de cuantificadores debe acompañarse de la negación exacta de la desigualdad.

### Microcontrol 027

[]{#MA-MIC-ANM-01-013-027}

[]{#MA-MSOL-ANM-01-013-027}

**Pregunta.** ¿Refutar $L=0$ basta para demostrar que no existe ningún límite?

**Solución.** No. Otro real podría ser límite. Hay que descartar todos los candidatos o usar una contradicción independiente del candidato.

La función constante uno no tiene límite cero, pero sí tiene límite uno. Por eso una refutación del candidato cero no descarta existencia de límite. Para demostrar inexistencia, debemos mostrar que cada real propuesto falla, o producir datos que contradigan cualquier posible destino, como dos rutas admisibles cuyas imágenes tengan límites distintos. La conclusión debe conservar el alcance lógico del argumento que se ha probado.

### Microcontrol 028

[]{#MA-MIC-ANM-01-013-028}

[]{#MA-MSOL-ANM-01-013-028}

**Pregunta.** ¿Por qué usamos $1/(n+1)$ en vez de $1/n$ desde $n=0$?

**Solución.** Porque $n+1>0$ para todos los índices, mientras $1/0$ no está definido.

La indexación comienza en cero, de modo que $1/n$ no define el primer término. Sustituir el denominador por $n+1$ lo hace positivo para todos los índices y produce una sucesión completa. Sus términos se acercan a cero porque, para cualquier tolerancia, podemos hacer $n+1$ mayor que su recíproco. El desplazamiento corrige la definición sin cambiar el mecanismo de aproximación por escalas cada vez menores.

### Microcontrol 029

[]{#MA-MIC-ANM-01-013-029}

[]{#MA-MSOL-ANM-01-013-029}

**Pregunta.** ¿Qué prueba la no vaciedad de todos los conjuntos $E_n$?

**Solución.** Que el candidato falla. Para cualquier radio elegimos una escala menor y un único infractor de ese conjunto.

Cada $E_n$ reúne infractores de la misma tolerancia dentro de la escala $\eta_n=1/(n+1)$. Para un radio arbitrario $\delta$, arquimedianidad permite elegir $n$ con $\eta_n<\delta$. La no vaciedad de ese conjunto proporciona una entrada que también está dentro del radio propuesto y mantiene el error grande. Para refutar el candidato sólo escogemos un testigo de un conjunto a la vez; no necesitamos todavía una sucesión de testigos.

### Microcontrol 030

[]{#MA-MIC-ANM-01-013-030}

[]{#MA-MSOL-ANM-01-013-030}

**Pregunta.** ¿La no vaciedad de cada $E_n$ proporciona por sí sola un selector?

**Solución.** No. $\forall n\exists x\in E_n$ no permite intercambiar cuantificadores sin una regla de selección o una hipótesis adicional.

Construir una sucesión requiere una asignación simultánea $n\mapsto x_n$ con $x_n\in E_n$ para todo índice. La afirmación de que cada conjunto tiene algún elemento no especifica esa asignación. En el marco fundacional explícito del capítulo, el paso se justifica mediante una regla dada, una enumeración que permita seleccionar mínimos o el principio adicional de elección numerable. No debe quedar oculto en la frase «escojamos un infractor para cada escala».

### Microcontrol 031

[]{#MA-MIC-ANM-01-013-031}

[]{#MA-MSOL-ANM-01-013-031}

**Pregunta.** Para el salto con valores $\pm1$, ¿por qué una distancia a $L$ es al menos $1$?

**Solución.** Si ambas fueran menores que $1$, la triangular daría $2=|1-(-1)|<2$, contradicción.

Las dos salidas del salto están separadas por dos unidades. Si el candidato estuviera a menos de una unidad de ambas, usarlo como punto intermedio daría una separación menor que dos, contradicción. Al menos una rama conserva por tanto error mayor o igual que uno. Elegimos esa rama según $L$ y, para cada radio, una entrada de su signo a distancia $\delta/2$. Así el error persiste arbitrariamente cerca del centro.

### Microcontrol 032

[]{#MA-MIC-ANM-01-013-032}

[]{#MA-MSOL-ANM-01-013-032}

**Pregunta.** ¿Qué asegura $x=\min(\delta/2,1/[2(|L|+1)])$ en la refutación de $1/x$?

**Solución.** $0<x<\delta$ y $1/x\ge2(|L|+1)$, luego $|1/x-L|>1$. Funciona para cualquier candidato real.

Los dos números del mínimo son positivos, de modo que $x>0$. Además $x\le\delta/2<\delta$ y $x\le1/[2(|L|+1)]$, lo que implica $1/x\ge2(|L|+1)$. La triangular inversa da $|1/x-L|\ge1/x-|L|\ge|L|+2>1$. La misma tolerancia uno refuta cada candidato finito, usando una entrada que puede depender de él y del radio.

## §13.5 — Lo que detectan las sucesiones

### Microcontrol 033

[]{#MA-MIC-ANM-01-013-033}

[]{#MA-MSOL-ANM-01-013-033}

[]{#MA-SEC-ANM-01-013-005}

**Pregunta.** ¿Qué tres condiciones hacen admisible a $(x_n)$?

**Solución.** $x_n\in D$, $x_n\ne a$ para todos los índices y $x_n\to a$.

Las dos primeras condiciones aseguran que cada evaluación $f(x_n)$ está definida y corresponde a una entrada perforada. La convergencia de las entradas asegura que toda cola suficientemente tardía queda dentro de cualquier radio dado. Juntas permiten transportar el control funcional a un control secuencial. Acercarse al centro no basta si se utilizan entradas fuera del dominio o si se repite el centro que la definición excluye.

### Microcontrol 034

[]{#MA-MIC-ANM-01-013-034}

[]{#MA-MSOL-ANM-01-013-034}

**Pregunta.** ¿Cómo se encadenan $\varepsilon$, $\delta$ y $N$ en la dirección directa?

**Solución.** $\varepsilon$ exige un radio $\delta$ para la función; la convergencia de entradas proporciona $N$ para ese radio; la cola cumple el error de salida.

Recibida $\varepsilon>0$, el límite funcional entrega un radio $\delta>0$. La convergencia $x_n\to a$ entrega luego un corte $N$ con $|x_n-a|<\delta$ para todos los índices tardíos. La admisibilidad aporta $x_n\ne a$ y $x_n\in D$, completando el antecedente del control funcional. Por eso $|f(x_n)-L|<\varepsilon$ en toda esa cola. Cada escala se elige después de la que debe responder.

### Microcontrol 035

[]{#MA-MIC-ANM-01-013-035}

[]{#MA-MSOL-ANM-01-013-035}

**Pregunta.** ¿Por qué la sucesión constante $x_n=a$ no es admisible?

**Solución.** Porque alcanza siempre el centro excluido. Evaluaría $f(a)$, un dato que el límite perforado no controla.

La sucesión constante en el centro sí converge a él, pero no cumple $x_n\ne a$. Si $f(a)$ está definido, sus imágenes serían constantemente ese valor, que puede diferir del límite perforado. Si el centro no pertenece al dominio, las imágenes ni siquiera podrían evaluarse. Excluirlo evita que un dato central ajeno al límite se introduzca en una ruta que pretende comprobar la aproximación.

### Microcontrol 036

[]{#MA-MIC-ANM-01-013-036}

[]{#MA-MSOL-ANM-01-013-036}

**Pregunta.** Si una ruta admisible tiene imágenes que no convergen a $L$, ¿qué concluyes?

**Solución.** Que $L$ no puede ser el límite funcional. Si lo fuera, la dirección directa controlaría también esa ruta.

La dirección directa afirma que un límite funcional debe controlar todas las sucesiones admisibles. Encontrar una sola que incumpla la convergencia hacia $L$ contradice esa consecuencia necesaria. Esto refuta precisamente ese candidato. Si las imágenes convergen a otro valor, podríamos estar viendo el verdadero destino; para descartar cualquier límite hacen falta además datos que contradigan todos los candidatos, por ejemplo dos rutas con destinos diferentes.

### Microcontrol 037

[]{#MA-MIC-ANM-01-013-037}

[]{#MA-MSOL-ANM-01-013-037}

**Pregunta.** ¿Qué regla elige infractores cuando está dada $e:\mathbb N\to D$ sobreyectiva?

**Solución.** $k_n=\min\{k:e(k)\in E_n\}$ y $x_n=e(k_n)$. La no vaciedad garantiza un mínimo natural único.

La sobreyectividad de $e$ garantiza que algún índice de la enumeración representa un elemento del conjunto no vacío $E_n$. El conjunto de esos índices es entonces un subconjunto no vacío de naturales y tiene un mínimo único. Esta regla define $x_n$ sin escoger arbitrariamente entre reales. Como $x_n\in E_n$, sus distancias al centro quedan por debajo de $1/(n+1)$ y sus errores de salida mantienen la tolerancia que refuta el candidato.

### Microcontrol 038

[]{#MA-MIC-ANM-01-013-038}

[]{#MA-MSOL-ANM-01-013-038}

**Pregunta.** ¿Deben crecer estrictamente los $k_n$ de ese selector?

**Solución.** No. No se está construyendo una subsucesión de $e$; se escoge una entrada que infringe cada escala.

El objetivo es satisfacer una condición de pertenencia a $E_n$ en cada escala, no preservar el orden de una enumeración. La regla vuelve a buscar el primer índice admisible para cada conjunto y no impone crecimiento estricto. Para que $x_n\to a$ basta la cota $0<|x_n-a|<1/(n+1)$. No hace falta interpretar la ruta como extracción de $e$ ni añadir condiciones a los índices que la construcción no proporciona.

### Microcontrol 039

[]{#MA-MIC-ANM-01-013-039}

[]{#MA-MSOL-ANM-01-013-039}

**Pregunta.** ¿Qué hipótesis permite la recíproca en cualquier dominio real?

**Solución.** $\mathrm{CC}(\mathbb R)$, aplicada explícitamente a la familia de conjuntos reales no vacíos $E_n$. El teorema es condicional a esa hipótesis.

Cuando el dominio no tiene una enumeración dada, los conjuntos $E_n$ siguen siendo subconjuntos reales no vacíos, pero falta la regla anterior de mínimos de índices. El principio $\mathrm{CC}(\mathbb R)$ entrega un selector para esa familia numerable. Con él construimos una ruta que se acerca a $a$ mientras mantiene el error grande y contradice la hipótesis secuencial. El capítulo registra esta hipótesis adicional explícitamente; la dirección directa no la utiliza.

### Microcontrol 040

[]{#MA-MIC-ANM-01-013-040}

[]{#MA-MSOL-ANM-01-013-040}

**Pregunta.** ¿Necesita elección numerable la refutación por las rutas $\pm1/(n+1)$?

**Solución.** No. Las dos rutas están dadas por fórmulas y la dirección directa basta para comparar sus destinos distintos.

Las fórmulas ya definen cada término de las dos rutas, por lo que no se seleccionan elementos de conjuntos arbitrarios. En el salto, sus imágenes son constantemente menos uno y uno. Si existiera un límite funcional, la dirección directa obligaría a que ambas imágenes convergieran a él; la unicidad del límite de sucesiones lo identificaría con dos números distintos. La contradicción se obtiene sin recurrir a la recíproca condicional.

## §13.6 — Combinar límites con presupuestos de error

### Microcontrol 041

[]{#MA-MIC-ANM-01-013-041}

[]{#MA-MSOL-ANM-01-013-041}

[]{#MA-SEC-ANM-01-013-006}

**Pregunta.** ¿Cómo se reparte $\varepsilon$ en una suma?

**Solución.** Con errores menores que $\varepsilon/2$ para cada sumando y el mínimo de ambos radios.

La diferencia de la suma respecto del destino es $(f-L)+(g-M)$. La triangular la domina por la suma de ambos errores. Pedimos que cada uno sea menor que $\varepsilon/2$ y escogemos el mínimo de sus radios, para que los dos controles valgan en la misma ventana. El error total queda entonces estrictamente por debajo de $\varepsilon$. Reducir ventanas permite sincronizar condiciones; no hace falta conocer un radio óptimo.

### Microcontrol 042

[]{#MA-MIC-ANM-01-013-042}

[]{#MA-MSOL-ANM-01-013-042}

**Pregunta.** ¿Cómo se trata la multiplicación por una constante nula?

**Solución.** Por separado: el error de la función cero es cero, sin dividir por la constante.

Si la constante es cero, tanto la función multiplicada como el destino multiplicado son cero en toda entrada admitida. El error es por tanto cero y cualquier radio positivo sirve. Para una constante $c\ne0$ se pide al límite original una precisión $\varepsilon/|c|$. Esta fórmula sólo se usa después de separar el caso cero, porque dividir por su magnitud en ese caso no tendría sentido.

### Microcontrol 043

[]{#MA-MIC-ANM-01-013-043}

[]{#MA-MSOL-ANM-01-013-043}

**Pregunta.** ¿Qué identidad prepara el producto?

**Solución.** $fg-LM=f(g-M)+M(f-L)$. Se controla $f$ con una barrera local y los dos errores con radios.

Añadir y restar $fM$ produce la identidad $fg-LM=f(g-M)+M(f-L)$. El primer error aparece multiplicado por un valor variable de $f$, que necesita una barrera local común; el segundo por la constante $M$. Una cota como $|f|<|L|+1$ convierte ambos multiplicadores en datos fijos. Entonces podemos distribuir la tolerancia entre los dos errores y reunir los radios que aseguran barrera y precisión.

### Microcontrol 044

[]{#MA-MIC-ANM-01-013-044}

[]{#MA-MSOL-ANM-01-013-044}

**Pregunta.** ¿Por qué $|M|+1$ es útil en el presupuesto de producto?

**Solución.** Es positivo incluso si $M=0$, y domina $|M|$. Permite dividir por una constante segura.

Si usáramos $|M|$ en un denominador, el caso $M=0$ dejaría la expresión sin definir. Usar $|M|+1$ mantiene un denominador positivo y no menor que la magnitud del multiplicador. Por ejemplo, pedir $|f-L|<\varepsilon/[2(|M|+1)]$ garantiza que $|M||f-L|<\varepsilon/2$ cuando el multiplicador es positivo; si es cero, el producto del error es cero. La elección deja un margen uniforme y cubre ambos casos.

### Microcontrol 045

[]{#MA-MIC-ANM-01-013-045}

[]{#MA-MSOL-ANM-01-013-045}

**Pregunta.** ¿Qué tolerancia garantiza que $g$ no se anule si $M\ne0$?

**Solución.** $|g-M|<|M|/2$, que implica $|g|>|M|/2>0$.

El límite de $g$ entrega un radio para la tolerancia positiva $|M|/2$. En esa ventana, la triangular inversa da $|g(x)|\ge|M|-|g(x)-M|>|M|/2$. Así $g$ no sólo evita cero, sino que queda separado de él por una constante común. Esta barrera permite controlar errores de recíprocos y cocientes sin dejar crecer arbitrariamente el denominador invertido.

### Microcontrol 046

[]{#MA-MIC-ANM-01-013-046}

[]{#MA-MSOL-ANM-01-013-046}

**Pregunta.** ¿Cuál es el dominio correcto de $f/g$?

**Solución.** $D_0=\{x\in D:g(x)\ne0\}$. Si $M\ne0$, incluye toda una ventana perforada del dominio original.

El cociente sólo se evalúa donde el denominador es distinto de cero. Declarar $D_0$ hace visible esa condición. Si $M\ne0$, la barrera local anterior muestra que toda entrada del dominio original suficientemente próxima y distinta de $a$ pertenece a $D_0$. Como $a$ acumulaba esas entradas, también acumula el dominio del cociente. Los ceros lejanos pueden excluirse sin alterar la pregunta de límite local.

### Microcontrol 047

[]{#MA-MIC-ANM-01-013-047}

[]{#MA-MSOL-ANM-01-013-047}

**Pregunta.** ¿Qué sucede con el cociente si el límite del denominador es cero?

**Solución.** La regla no se aplica. Puede haber cancelación y límite finito, o puede faltar límite; hace falta otro argumento.

El dato $g\to0$ no proporciona la barrera inferior positiva usada en la regla. Por ejemplo, en entradas no nulas el cociente $x/x$ vale uno y tiene límite uno; en cambio $1/x$ no tiene límite real finito en cero. Ambos tienen denominador que tiende a cero y conclusiones diferentes. No se asigna significado a una división por el límite cero; se estudia el cociente en su dominio mediante otro control.

### Microcontrol 048

[]{#MA-MIC-ANM-01-013-048}

[]{#MA-MSOL-ANM-01-013-048}

**Pregunta.** ¿Necesita la regla de producto el criterio secuencial recíproco?

**Solución.** No. Se demostró directamente con radios, cota local e identidades algebraicas.

Las estimaciones del producto trabajan con una entrada arbitraria de una ventana perforada. Usan una identidad algebraica, acotación local y radios que hacen pequeños los errores. No seleccionan una sucesión de entradas ni convierten condiciones secuenciales en condiciones funcionales. Por tanto la prueba directa no hereda la hipótesis de elección numerable que se declaró en otro teorema. Mantener separadas las vías de prueba preserva su alcance fundacional.

## §13.7 — Cambiar las rutas disponibles

### Microcontrol 049

[]{#MA-MIC-ANM-01-013-049}

[]{#MA-MSOL-ANM-01-013-049}

[]{#MA-SEC-ANM-01-013-007}

**Pregunta.** ¿Qué condición adicional se exige al restringir a $A\subseteq D$?

**Solución.** $a\in A'$. Garantiza una pregunta de límite no vacía en el dominio restringido.

Reducir el dominio reduce las rutas disponibles, pero puede eliminarlas todas cerca del centro. Si $A$ sólo contiene el centro como punto aislado, la fórmula perforada sería vacía. Exigir $a\in A'$ garantiza aproximaciones en el dominio restringido. Bajo esa condición, el mismo radio del límite original controla todas las entradas de $A$ que quedan en su ventana, porque también pertenecen a $D$.

### Microcontrol 050

[]{#MA-MIC-ANM-01-013-050}

[]{#MA-MSOL-ANM-01-013-050}

**Pregunta.** ¿Por qué sirve reunir finitos radios positivos mediante un mínimo?

**Solución.** Porque su mínimo sigue siendo positivo y garantiza simultáneamente todos los controles locales.

Para una cantidad finita de controles, cada radio es positivo y al menos uno de ellos es el menor. Ese menor sigue siendo positivo. Una entrada dentro de su ventana está dentro de todas las ventanas originales y satisface todos los controles simultáneamente. El argumento permite reunir acotación, coincidencia local, precisión y restricciones de dominio sin perder la existencia de una escala válida.

### Microcontrol 051

[]{#MA-MIC-ANM-01-013-051}

[]{#MA-MSOL-ANM-01-013-051}

**Pregunta.** ¿Un mínimo de infinitos radios positivos tiene que ser positivo?

**Solución.** No. Los radios $1/(n+1)$ son positivos y no tienen ninguna cota inferior positiva.

La familia $1,1/2,1/3,\ldots$ se acerca a cero: ante cualquier propuesta $r>0$, existe un índice con $1/(n+1)<r$. Por eso no hay un radio positivo que quede por debajo de todos. En esta familia ni siquiera existe un mínimo; su ínfimo es cero. La técnica de tomar mínimos finitos no se extiende automáticamente a infinitos controles, porque podría dejar una ventana sin radio positivo.

### Microcontrol 052

[]{#MA-MIC-ANM-01-013-052}

[]{#MA-MSOL-ANM-01-013-052}

**Pregunta.** ¿Cuándo está definido el límite por la izquierda bajo nuestra convención?

**Solución.** Cuando $a$ es punto de acumulación de $D\cap(-\infty,a)$. No basta que el lado esté nombrado.

El límite izquierdo es el límite de la función restringida a las entradas menores que $a$. Para formularlo necesitamos entradas de ese lado arbitrariamente próximas al centro. Si el dominio es $[a,\infty)$, la parte izquierda está vacía y no acumula en $a$, aunque el límite derecho pueda tener sentido. Nombrar un lado no garantiza que existan aproximaciones desde él.

### Microcontrol 053

[]{#MA-MIC-ANM-01-013-053}

[]{#MA-MSOL-ANM-01-013-053}

**Pregunta.** Si ambos lados acumulan, ¿qué permite reunirlos?

**Solución.** Que ambos límites laterales sean el mismo $L$. Se usa el mínimo de sus radios y toda entrada perforada pertenece a uno de los lados.

Para una tolerancia, cada límite lateral entrega un radio que controla sus entradas. Tomamos el mínimo. Cualquier entrada distinta del centro es menor o mayor que él, así que cae en uno de los dos lados y cumple la misma estimación respecto de $L$. Si los destinos fueran diferentes, esta unión de controles hacia un único número no sería posible. La igualdad de destinos es lo que permite construir el límite conjunto.

### Microcontrol 054

[]{#MA-MIC-ANM-01-013-054}

[]{#MA-MSOL-ANM-01-013-054}

**Pregunta.** Si un lado no acumula, ¿qué información local ofrece?

**Solución.** Existe un radio positivo sin entradas de ese lado. En una ventana suficientemente pequeña sólo importa el otro lado.

Negar acumulación en un lado significa que existe un radio donde no hay entradas de ese lado distintas del centro. Reduciendo también al radio válido del otro lado, toda entrada pertinente pertenece a éste y queda controlada. No se necesita asignar un límite ficticio al lado ausente. El límite en el dominio completo puede quedar determinado por las rutas realmente disponibles, junto con la condición de acumulación del dominio.

### Microcontrol 055

[]{#MA-MIC-ANM-01-013-055}

[]{#MA-MSOL-ANM-01-013-055}

**Pregunta.** ¿Probar un límite en un subconjunto denso basta para una función arbitraria?

**Solución.** No. La función puede tener valores distintos en todas las entradas omitidas; el indicador racional de §13.7 es un contraejemplo.

La densidad asegura que existen muchas entradas del subconjunto cerca de cada punto, pero no impone ninguna relación entre sus valores y los de las entradas omitidas. El indicador de los racionales vale uno sobre los racionales y cero sobre los irracionales. Restringir a cada uno de esos conjuntos produce destinos diferentes, aunque ambos sean densos. Para una función arbitraria, una familia de rutas favorables no reemplaza el control de todas las entradas.

### Microcontrol 056

[]{#MA-MIC-ANM-01-013-056}

[]{#MA-MSOL-ANM-01-013-056}

**Pregunta.** ¿Por qué $\sqrt2/(n+1)$ es irracional para todo índice?

**Solución.** Si fuese racional, multiplicarlo por el entero positivo $n+1$ haría racional a $\sqrt2$, contradicción.

El denominador $n+1$ es un entero positivo, así que multiplicar un supuesto cociente racional por él conserva racionalidad. Eso produciría una expresión racional para $\sqrt2$, contradiciendo su irracionalidad ya demostrada. Además sus magnitudes tienden a cero, por lo que la fórmula proporciona una ruta de entradas irracionales próximas a cero sin una selección abstracta. La prueba valida cada término y la propiedad de aproximación.

## §13.8 — Componer controles sin perder la perforación

### Microcontrol 057

[]{#MA-MIC-ANM-01-013-057}

[]{#MA-MSOL-ANM-01-013-057}

[]{#MA-SEC-ANM-01-013-008}

**Pregunta.** ¿Qué desafío se presenta a $f$ después de fijar $\varepsilon$ para $g\circ f$?

**Solución.** El radio intermedio $\eta$ que entrega el límite de $g$ para esa tolerancia final.

El límite exterior convierte el desafío final $\varepsilon$ en una escala intermedia $\eta$ alrededor de $b$. A continuación pedimos al límite interior que haga $f(x)$ suficientemente cercano a $b$ para entrar en esa escala. El radio final es el que responde a este segundo desafío, combinado con las restricciones locales. La composición encadena dos controles y su orden de diseño va desde la precisión final hacia la entrada inicial.

### Microcontrol 058

[]{#MA-MIC-ANM-01-013-058}

[]{#MA-MSOL-ANM-01-013-058}

**Pregunta.** ¿Qué dato falta si sólo sabemos $|f(x)-b|<\eta$?

**Solución.** Que $f(x)\ne b$, si vamos a usar el límite perforado de $g$. La cercanía sola permite alcanzar el centro.

El control del límite exterior se aplica a entradas con $0<|y-b|<\eta$. La estimación $|f(x)-b|<\eta$ sólo da la desigualdad superior y permite que la magnitud sea cero. Si la salida interior alcanza $b$, estaríamos evaluando $g(b)$, que el límite perforado de $g$ no controla. Por eso hace falta evitar localmente ese centro o verificar por separado que su valor exterior sea el destino correcto.

### Microcontrol 059

[]{#MA-MIC-ANM-01-013-059}

[]{#MA-MSOL-ANM-01-013-059}

**Pregunta.** ¿Qué alternativa permite que $f(x)=b$?

**Solución.** Que $b\in E$ y $g(b)=L$. En ese caso la salida central tiene error exactamente cero.

Si la salida interior alcanza $b$ y $g(b)=L$, la composición entrega exactamente $L$ y tiene error cero. Si no alcanza $b$, se aplica el control perforado exterior. Separar ambos casos permite cubrir toda la ventana de entradas. También hay que tener $b$ en el dominio de $g$ para usar su evaluación. La condición sobre el valor central resuelve el caso que la desigualdad perforada dejaba fuera.

### Microcontrol 060

[]{#MA-MIC-ANM-01-013-060}

[]{#MA-MSOL-ANM-01-013-060}

**Pregunta.** ¿Qué falla en la composición de una función cero con $g(0)=1$, $g(y)=0$ fuera de cero?

**Solución.** La interior cae siempre en el centro. Aunque ambos límites aislados son cero, la composición es constante uno.

La función interior $f(x)=0$ tiene límite cero, y la exterior dada tiene límite perforado cero en cero porque vale cero en todas las entradas no centrales. Pero cada composición evalúa precisamente el centro exterior, donde $g(0)=1$. Por eso $g(f(x))=1$ en toda entrada y su límite es uno. El ejemplo refuta la aplicación de una regla de composición que ignore la perforación y el valor central.

### Microcontrol 061

[]{#MA-MIC-ANM-01-013-061}

[]{#MA-MSOL-ANM-01-013-061}

**Pregunta.** ¿Qué papel desempeña el tipo $f:D\to E$?

**Solución.** Garantiza que $g(f(x))$ esté definido. Una regla algebraica sin pertenencia al dominio de $g$ no basta.

Si el dominio exterior de $g$ es $E$, el tipo $f:D\to E$ asegura que cada salida intermedia pertenece a ese dominio. La cercanía a $b$ no bastaría: una salida muy próxima podría seguir siendo una entrada no admitida. Primero verificamos que la composición pueda evaluarse en las entradas pertinentes y después diseñamos las estimaciones de límite. Un certificado numérico no reemplaza la comprobación del dominio.

### Microcontrol 062

[]{#MA-MIC-ANM-01-013-062}

[]{#MA-MSOL-ANM-01-013-062}

**Pregunta.** Con $|f(x)-b|\le C|x-a|$, $C>0$, ¿qué radio de precisión sirve?

**Solución.** $\eta_g(\varepsilon)/C$, combinado por mínimo con las restricciones locales. La desigualdad estricta de entrada produce error intermedio menor que $\eta_g(\varepsilon)$.

La cota interior entrega $|f(x)-b|\le C|x-a|$. Elegir $\delta\le\eta_g(\varepsilon)/C$ hace que la desigualdad estricta $|x-a|<\delta$ produzca $|f(x)-b|<\eta_g(\varepsilon)$. El mínimo con radios auxiliares asegura la validez de la cota y la condición de evitación o del valor central. Se debe conservar ese último requisito: la cota superior de distancias no prueba por sí sola que la salida interior evite $b$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-013-063}

[]{#MA-MSOL-ANM-01-013-063}

**Pregunta.** Si $C=0$ en esa cota, ¿qué ocurre localmente?

**Solución.** $f(x)=b$. El mecanismo de composición necesita $g(b)=L$; la evitación es incompatible con la ventana no vacía.

La cota $|f(x)-b|\le0$ fuerza igualdad con $b$ en toda la ventana donde vale. Si esas entradas son no vacías por acumulación, no pueden además satisfacer $f(x)\ne b$. La vía de evitación queda descartada. La composición local evalúa siempre $g(b)$ y sólo obtiene el destino propuesto si ese valor es $L$. Este caso se estudia directamente y no se divide por $C$.

### Microcontrol 064

[]{#MA-MIC-ANM-01-013-064}

[]{#MA-MSOL-ANM-01-013-064}

**Pregunta.** ¿Qué verifica finalmente un certificado de límite?

**Solución.** Que el radio sea positivo y dependa sólo de datos permitidos, y que todas las entradas del dominio en su ventana perforada satisfagan el error de salida.

Después de proponer el radio debemos comprobar que sea positivo para cada tolerancia positiva y que se elija antes de la entrada arbitraria. Luego tomamos cualquier $x\in D$ con $0<|x-a|<\delta$ y derivamos el error estricto. El argumento debe verificar también las condiciones de dominio y cualquier denominador usado. La acumulación garantiza que no se trate de ventanas vacías. Una fórmula para $\delta$ sin esta comprobación universal todavía no completa la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-microcontroles.html)
