---
content-id: MA-BCH-0254
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-013
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
title: 'Capítulo 13 — Límites de funciones: control de dos escalas'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C13.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-13)

¿Qué significa que unas entradas próximas a un punto produzcan salidas próximas a un destino? En cálculo aprendimos a reconocer y calcular límites; aquí reconstruiremos el contrato que autoriza esas operaciones. No basta ensayar unas pocas entradas ni encontrar una ruta favorable: queremos controlar toda una ventana del dominio y responder a cualquier precisión de salida.

Usaremos las bolas y la acumulación de C04, las sucesiones de C06 y el transporte de conjuntos de C12. Primero entregaremos radios explícitos desde la definición; después construiremos unicidad, negación, criterios secuenciales y reglas. Mantendremos visible qué escala depende de cuál y dónde una hipótesis permite dar el siguiente paso.

## 13.1. Aproximarse sin tocar el centro

[]{#MA-SEC-ANM-01-013-001}

En C12 aprendimos a transportar una ventana de entradas dentro de una ventana de salidas. Ahora queremos hacerlo para cualquier precisión de salida que se nos proponga. El tamaño de la ventana de entrada se adaptará al desafío. Ésta es la diferencia entre haber comprobado una inclusión concreta y disponer de un límite.

Empecemos con $q(x)=x^2$ cerca de $1$. La identidad $x^2-1=(x-1)(x+1)$ sugiere que las salidas se aproximan a $1$ cuando las entradas se aproximan a $1$. Pero podemos cambiar la función sólo en el centro: $h(1)=4$, $h(x)=x^2$ si $x\ne1$. Las salidas de las entradas próximas y distintas de $1$ siguen siendo las mismas. El límite que queremos estudiar no puede depender del valor aislado $h(1)$.

### El conjunto por el que nos aproximamos

Sean $D\subseteq\mathbb R$ y $a\in\mathbb R$. Recordemos de C04 que $a$ es punto de acumulación de $D$ si para cada $r>0$ existe $x\in D$ con $0<|x-a|<r$. Escribiremos $a\in D'$. No se requiere $a\in D$: cero es punto de acumulación de $(0,\infty)$ sin pertenecer a ese dominio.

Llamemos $U_D(a,r)=\{x\in D:0<|x-a|<r\}$ a la ventana perforada de entrada. La intersección con $D$ conserva el tipo; la perforación elimina el centro. Por acumulación, $U_D(a,r)$ es no vacía para todo radio positivo. No hemos elegido una sucesión de puntos: sólo afirmamos existencia para cada radio.

**Definición.** Para $f:D\to\mathbb R$, $a\in D'$ y $L\in\mathbb R$, decimos que $f$ tiene límite $L$ en $a$ a través de $D$ si

$$
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:
\quad 0<|x-a|<\delta\ \Longrightarrow\ |f(x)-L|<\varepsilon.
$$

Escribimos $\lim_{x\to a,\ x\in D}f(x)=L$, abreviando el dominio cuando sea inequívoco. En este capítulo todos los límites funcionales son reales finitos en puntos reales finitos.

La condición equivale a $f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$ para cada desafío $\varepsilon$ y alguna respuesta $\delta$. En efecto, un valor de la imagen tiene un testigo $x$ en la ventana perforada y la desigualdad lo coloca en la bola de salida. A la inversa, si cada imagen está en la bola, evaluar en cualquier $x$ de esa ventana da la desigualdad exigida. Por C12 también equivale a $U_D(a,\delta)\subseteq f^{-1}[B(L,\varepsilon)]$.

![C13-F01. La perforación omite el valor h(1)=4. Las entradas no centrales siguen la regla x² y se aproximan al destino 1. El círculo vacío distingue el hueco del valor asignado; la banda es un desafío, no una prueba.](../../assets/books/anm/C13/C13-F01.svg){#fig-anm-c13-f01 fig-alt="C13-F01. La perforación omite el valor h(1)=4. Las entradas no centrales siguen la regla x² y se aproximan al destino 1. El círculo vacío distingue el hueco del valor asignado; la banda es un desafío, no una prueba."}

### Por qué exigimos acumulación

Si $D=\{a\}$, ninguna entrada cumple $0<|x-a|<\delta$. La implicación sería verdadera para cualquier candidato $L$, por vacuidad. La fórmula lógica sigue teniendo sentido, pero no distingue un destino. Nuestra convención reserva la palabra límite para $a\in D'$.

Tampoco importa cambiar valores lejos del centro. Si $f,g:D\to\mathbb R$ coinciden en $U_D(a,r)$ para algún $r>0$ y $f\to L$, dado $\varepsilon$ tomamos un radio válido $\delta_f$ y usamos $\delta=\min(r,\delta_f)$. Toda entrada pertinente ve $g(x)=f(x)$ y el mismo control. Intercambiar las funciones prueba la equivalencia. Cambiar sólo $f(a)$, si existe, es un caso particular.

La ventana se encoge alrededor de $a$; la ventana de salida alrededor de $L$. Esos centros cumplen papeles distintos y aún no hemos relacionado $L$ con $f(a)$.

### Antes de seguir

#### Microcontrol 1

[]{#MA-MIC-ANM-01-013-001}

¿Tiene que pertenecer $a$ al dominio para preguntar por el límite en $a$?

[]{#MA-MSOL-ANM-01-013-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

No. Debe ser punto de acumulación del dominio. Por ejemplo, $0\notin(0,\infty)$ y cada radio positivo contiene una entrada positiva distinta de cero.

El límite observa entradas del dominio arbitrariamente próximas a $a$, no una evaluación en $a$. En el dominio positivo, dado cualquier radio $r>0$, la entrada $r/2$ es positiva y está a distancia menor que $r$ de cero. Así cero acumula entradas aunque no sea una de ellas. La condición de acumulación garantiza que la aproximación tenga contenido; pertenecer al dominio, en cambio, sólo permitiría hablar además del valor central.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-013-002}

¿Qué elimina $0<|x-a|$?

[]{#MA-MSOL-ANM-01-013-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Elimina $x=a$; asegura que sólo se usan entradas distintas del centro.

La magnitud $|x-a|$ es cero exactamente cuando $x=a$. Pedir que sea positiva descarta esa entrada y deja una ventana perforada. El límite puede coincidir con $f(a)$, diferir de él o existir cuando $f(a)$ ni siquiera está definido. La definición no decide esa relación, porque todas sus estimaciones se aplican a otras entradas. Confundir la ventana con una bola sin perforar añadiría un control sobre el valor central.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-013-003}

¿Qué significa $a\in D^{\prime}$ en forma cuantificada?

[]{#MA-MSOL-ANM-01-013-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

$\forall r>0\ \exists x\in D:0<|x-a|<r$. Toda ventana perforada contiene una entrada.

Primero se recibe un radio positivo arbitrario y después se busca una entrada del dominio distinta del centro dentro de él. El testigo puede variar con el radio; no se exige una entrada que esté en todas las ventanas. La condición significa que ninguna escala positiva agota las aproximaciones disponibles. Si existiera un radio sin esas entradas, el punto no sería de acumulación, aunque perteneciera al dominio como punto aislado.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-013-004}

Si $D=\{a\}$, ¿la fórmula perforada distingue un candidato $L$?

[]{#MA-MSOL-ANM-01-013-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

No. Su antecedente nunca se cumple, por lo que vale por vacuidad para todo $L$. Nuestra definición no asigna límite en ese caso.

Para este dominio, ninguna entrada cumple simultáneamente $x\in D$ y $x\ne a$. Por eso la implicación que exige error pequeño nunca encuentra una entrada a la que aplicarse y es verdadera para cualquier candidato. No distingue un destino único. Exigir acumulación elimina esta vacuidad y permite la prueba de unicidad. Bajo la convención del capítulo, en un punto aislado no se declara un límite perforado mediante esa fórmula.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-013-005}

¿Cómo se escribe el control mediante imágenes de ventanas?

[]{#MA-MSOL-ANM-01-013-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Para cada $\varepsilon>0$ hay $\delta>0$ con $f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$.

La ventana $U_D(a,\delta)=\{x\in D:0<|x-a|<\delta\}$ reúne exactamente las entradas sometidas al control. Pedir que su imagen esté en $B(L,\varepsilon)$ equivale a pedir $|f(x)-L|<\varepsilon$ para cada una. La inclusión es universal: ningún punto de la ventana puede dar una salida fuera de la bola. La escala de entrada se elige para responder a la precisión solicitada en las salidas.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-013-006}

¿Qué preimagen contiene la ventana perforada cuando el radio es válido?

[]{#MA-MSOL-ANM-01-013-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

$f^{-1}[B(L,\varepsilon)]$. Cada entrada de la ventana produce una salida en esa bola.

La preimagen de la bola de salidas es el conjunto de entradas $x\in D$ que satisfacen $|f(x)-L|<\varepsilon$. Si el radio es válido, toda entrada de la ventana perforada pertenece a ese conjunto. Así el control puede expresarse como $U_D(a,\delta)\subseteq f^{-1}[B(L,\varepsilon)]$. Esta formulación no necesita una función inversa: utiliza la preimagen para seleccionar entradas por sus salidas.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-013-007}

¿Cambia el límite si sólo cambiamos $f(a)$?

[]{#MA-MSOL-ANM-01-013-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

No. Las entradas que evalúa la definición son distintas de $a$, por lo que sus valores permanecen iguales.

Si dos funciones coinciden en las entradas distintas de $a$ de una misma ventana, las estimaciones del límite ven exactamente los mismos valores allí. Modificar sólo la evaluación central no cambia ninguna de esas desigualdades. Si se añade o elimina el propio centro del dominio, tampoco cambian las entradas perforadas ni la acumulación. El resultado permite comparar el comportamiento próximo al punto con el dato particular de su evaluación.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-013-008}

¿Qué radio reúne coincidencia local y control de $f$?

[]{#MA-MSOL-ANM-01-013-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

$\min(r,\delta_f)$, donde $r>0$ es el radio de coincidencia y $\delta_f>0$ controla el error. Así se cumplen las dos condiciones.

El radio de coincidencia asegura que podemos sustituir $g(x)$ por $f(x)$; el radio de precisión asegura que este valor está cerca de $L$. Tomar el mínimo mantiene ambas garantías simultáneamente, porque una entrada más cercana que ese mínimo está dentro de las dos ventanas. El mínimo de dos números positivos sigue siendo positivo. Sólo entonces el control de una función se transporta a la otra.

</details>

### Ejercicios de la sección 13.1

[]{#ejercicios-13}

#### Ejercicio 1. El agujero no decide el destino

[]{#MA-EX-ANM-01-013-001}

Define $f:\mathbb R\to\mathbb R$ por $f(x)=2x+5$ si $x\ne-1$ y $f(-1)=100$. Prueba desde la definición el límite en $-1$ y explica qué dato se excluye.

[]{#MA-SOL-ANM-01-013-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

El candidato es $3$. Para $\varepsilon>0$ tomamos $\delta=\varepsilon/2$. Si $0<|x+1|<\delta$, entonces $x\ne-1$, por lo que $|f(x)-3|=2|x+1|<\varepsilon$. El punto $-1$ acumula entradas reales, por ejemplo $-1+\delta/2$. La definición controla entradas distintas del centro; el valor $100$ no interviene.

**Retorno visual.** Véase [C13-F01](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Una pregunta sin entradas

[]{#MA-EX-ANM-01-013-002}

Para $D=\{0\}\cup[2,3]$ y cualquier $f:D\to\mathbb R$, analiza la fórmula perforada en $a=0$. ¿Hay un límite bajo la convención del capítulo?

[]{#MA-SOL-ANM-01-013-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Con $\delta=1$, no existe $x\in D$ con $0<|x|<1$. La implicación sería verdadera para todo $L$ y toda tolerancia usando ese mismo radio. Pero $0$ no es punto de acumulación de $D$, así que no asignamos límite. El fallo no depende de los valores de $f$: depende de las rutas inexistentes.

</details>

#### Ejercicio 3. Dos lenguajes del mismo control

[]{#MA-EX-ANM-01-013-003}

Prueba directamente que $f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$ equivale a $U_D(a,\delta)\subseteq f^{-1}[B(L,\varepsilon)]$. Mantén separados valores y conjuntos.

[]{#MA-SOL-ANM-01-013-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Si vale la inclusión de imágenes y $x\in U_D(a,\delta)$, entonces $f(x)\in f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$, luego $x\in f^{-1}[B(L,\varepsilon)]$. A la inversa, si toda entrada de la ventana está en esa preimagen y $y$ pertenece a la imagen, existe un testigo $x$ de la ventana con $y=f(x)$; la pertenencia a la preimagen da $y\in B(L,\varepsilon)$. $f(x)$ es un valor; la imagen y la preimagen son conjuntos.

</details>

#### Ejercicio 4. Igualdad en un germen perforado

[]{#MA-EX-ANM-01-013-004}

Sean $f,g:D\to\mathbb R$ iguales siempre que $0<|x-a|<r$, con $r>0$ y $a\in D^{\prime}$. Prueba que tienen exactamente los mismos candidatos de límite.

[]{#MA-SOL-ANM-01-013-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Fijemos un candidato $L$ y supongamos $f\to L$. Para cada $\varepsilon>0$, un radio $\delta_f$ de $f$ se reúne con $r$ mediante $\delta=\min(r,\delta_f)>0$. En la ventana resultante $g(x)=f(x)$ y $|g(x)-L|<\varepsilon$. Luego $g\to L$. Intercambiar $f,g$ prueba la recíproca para ese mismo candidato. Como $L$ era arbitrario, los conjuntos de candidatos coinciden.

</details>

#### Ejercicio 5. Cambiar valores en infinitos puntos lejanos

[]{#MA-EX-ANM-01-013-005}

Construye dos funciones reales que difieran en infinitos puntos, una no acotada globalmente, y que tengan límite cero en cero por coincidencia local. Prueba las afirmaciones.

[]{#MA-SOL-ANM-01-013-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Sea $f(x)=0$ para todo real, y sea $g(x)=0$ si $|x|<1$, $g(x)=x^2$ si $|x|\ge1$. Difieren en todos los enteros positivos, un conjunto infinito. $g(n)=n^2$ no admite cota global por arquimedianidad. Ambas coinciden en la ventana de radio $1$; para toda tolerancia, ese radio hace el error cero. La información fuera de una ventana fija no determina el límite.

</details>
## 13.2. Diseñar una respuesta para toda la ventana

[]{#MA-SEC-ANM-01-013-002}

La definición propone un juego con orden fijo: se declaran $f,D,a,L$; se recibe $\varepsilon$; se produce $\delta$; después se verifica toda entrada admisible. Elegir $\delta$ después de ver $x$ cambia el problema. Una respuesta puede depender de los datos fijos y de $\varepsilon$, pero no de la entrada universal.

### Trabajar hacia atrás y escribir hacia delante

Para $f(x)=3x-2$ y $a=1$, el candidato es $L=1$. Queremos $|(3x-2)-1|<\varepsilon$. Simplificar revela $3|x-1|<\varepsilon$, lo que sugiere $\delta=\varepsilon/3$.

La prueba final comienza con el desafío: fijado $\varepsilon>0$, sea $\delta=\varepsilon/3>0$. Si $0<|x-1|<\delta$, entonces $|f(x)-1|=3|x-1|<3\delta=\varepsilon$. No se calcula primero una entrada favorable: el argumento sirve para todas las que satisfacen la hipótesis.

![C13-F02. Para 3x−2 en a=1, el error de salida es tres veces el de entrada. Cada desafío ε tiene respuesta δ=ε/3; los bordes se excluyen. Dos instancias ilustran la fórmula que la prueba verifica para todo ε.](../../assets/books/anm/C13/C13-F02.svg){#fig-anm-c13-f02 fig-alt="C13-F02. Para 3x−2 en a=1, el error de salida es tres veces el de entrada. Cada desafío ε tiene respuesta δ=ε/3; los bordes se excluyen. Dos instancias ilustran la fórmula que la prueba verifica para todo ε."}

Para una función afín $mx+c$ cerca de cualquier $a$, la identidad de errores es $|f(x)-(ma+c)|=|m||x-a|$. Si $m\ne0$, funciona $\delta=\varepsilon/|m|$. Si $m=0$, el error es cero y cualquier radio positivo sirve. Reducir un radio válido conserva su validez; no hay razón para exigir un único radio.

### Un factor variable necesita primero una barrera

Volvamos a $q(x)=x^2$ en $a$. La identidad $|x^2-a^2|=|x-a||x+a|$ contiene un factor no controlado. Introducimos una condición auxiliar: $|x-a|<1$. Entonces $|x+a|\le |x-a|+2|a|<1+2|a|=:C$, con $C>0$. Ahora podemos controlar el otro factor.

Fijado $\varepsilon>0$, elijamos $\delta=\min(1,\varepsilon/C)$. Para toda entrada con $0<|x-a|<\delta$ obtenemos $|x^2-a^2|<C|x-a|<C\delta\le\varepsilon$. Las dos tareas son distintas: el radio $1$ congela el factor variable; el radio $\varepsilon/C$ ajusta la precisión. El mínimo hace que se cumplan simultáneamente.

![C13-F03. En x² alrededor de 1 y con ε=1/2, el certificado de la prueba usa δ=1/6. El mayor radio simétrico es √(3/2)−1. El certificado conservador basta para demostrar el límite; la optimización exige el argumento adicional del ejercicio 13.8.](../../assets/books/anm/C13/C13-F03.svg){#fig-anm-c13-f03 fig-alt="C13-F03. En x² alrededor de 1 y con ε=1/2, el certificado de la prueba usa δ=1/6. El mayor radio simétrico es √(3/2)−1. El certificado conservador basta para demostrar el límite; la optimización exige el argumento adicional del ejercicio 13.8."}

El radio no necesita ser el mayor posible. En $a=1$, $\delta=\min(1,\varepsilon/3)$ es cómodo aunque conservador. Buscar el radio óptimo puede ser un problema distinto; para demostrar un límite basta un certificado verificable.

### Evitar un denominador pequeño

Para $r(x)=1/x$ en $a\ne0$, restringimos $|x-a|<|a|/2$. La triangular inversa da $|x|\ge |a|-|x-a|>|a|/2$. En esa ventana el dominio excluye cero automáticamente y

$$
\left|\frac1x-\frac1a\right|
=\frac{|x-a|}{|x||a|}
<\frac{2|x-a|}{|a|^2}.
$$

El radio $\delta=\min(|a|/2,\varepsilon |a|^2/2)$ prueba $\lim_{x\to a}1/x=1/a$. No basta decir que un denominador es distinto de cero: hay que separarlo de cero por una barrera positiva válida para toda la ventana.

Cada ejemplo sigue el mismo método: descomponer el error, controlar factores auxiliares y reunir restricciones mediante un mínimo. No usamos reglas de límites todavía; estamos construyéndolas desde desigualdades.

### Antes de seguir

#### Microcontrol 9

[]{#MA-MIC-ANM-01-013-009}

¿Puede $\delta$ depender de la entrada $x$ bajo el cuantificador universal?

[]{#MA-MSOL-ANM-01-013-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

No. Se fija antes de verificar toda entrada. Puede depender de $\varepsilon$ y de los datos fijados.

La definición tiene el orden $\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D$. El radio debe responder al desafío antes de considerar la entrada arbitraria y servir para todas las entradas de su ventana. Elegirlo después de conocer cada $x$ cambiaría ese orden e incluso permitiría excluir esa entrada escogiendo un radio menor que su distancia al centro. Eso no demostraría un control común de aproximación.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-013-010}

Para $f(x)=3x-2$ en $a=1$, ¿qué radio explícito sirve?

[]{#MA-MSOL-ANM-01-013-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

$\delta=\varepsilon/3$, pues $|f(x)-1|=3|x-1|<3\delta=\varepsilon$.

La salida candidata es $3\cdot1-2=1$. Restarla de la regla da $f(x)-1=3(x-1)$, y al tomar magnitudes el error de salida es tres veces el de entrada. Por eso recibida $\varepsilon>0$ escogemos el radio positivo $\varepsilon/3$. Cualquier entrada con $0<|x-1|<\delta$ cumple el error estricto. La misma elección funciona para toda la ventana y no depende de una entrada concreta.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-013-011}

¿Es válido exigir un solo $\delta>0$ para todas las tolerancias?

[]{#MA-MSOL-ANM-01-013-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Es una condición más fuerte. Para una afín no constante no existe tal radio: una entrada no central dentro de él tiene error positivo, y una tolerancia menor lo refuta.

En una afín de pendiente $m\ne0$ y dominio real, fijado un radio $\delta>0$ podemos escoger $x=a+\delta/2$. Su error respecto de $ma+c$ es $|m|\delta/2>0$. Una tolerancia igual a la mitad de ese error refuta ese radio. Por tanto una única escala de entrada no puede responder a todas las precisiones. La definición permite que el radio se reduzca a medida que la tolerancia lo exige.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-013-012}

¿Qué ocurre con la afín si $m=0$?

[]{#MA-MSOL-ANM-01-013-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Es constante y su error respecto de $c$ es cero; cualquier radio positivo sirve.

La asignación se reduce a $f(x)=c$ y el destino es $c$. Para cualquier entrada del dominio, $|f(x)-c|=0$, menor que cualquier tolerancia positiva. Podemos escoger, por ejemplo, $\delta=1$ sin dividir por la pendiente. Como siempre, el centro debe acumular entradas del dominio para formular el límite bajo esta convención. El caso constante separa una estimación trivial de las fórmulas que requieren $|m|>0$.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-013-013}

¿Qué cota para $|x+a|$ produce $|x-a|<1$?

[]{#MA-MSOL-ANM-01-013-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

$|x+a|\le |x-a|+2|a|<1+2|a|$. Esa constante permite controlar el producto de errores.

Escribimos $x+a=(x-a)+2a$. La triangular da $|x+a|\le|x-a|+2|a|$, y la ventana auxiliar de radio uno hace el primer sumando menor que uno. La constante $1+2|a|$ está fijada por el centro y no por la entrada variable. Así la factorización $|x^2-a^2|=|x-a||x+a|$ se convierte en un error pequeño multiplicado por un factor uniformemente acotado.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-013-014}

¿Por qué se toma un mínimo en la prueba del cuadrado?

[]{#MA-MSOL-ANM-01-013-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Para asegurar a la vez el radio auxiliar $1$ y el radio de precisión $\varepsilon/(1+2|a|)$.

Si sólo usáramos el radio de precisión, quizá no podríamos controlar el factor $|x+a|$. Si sólo usáramos el auxiliar, el error no tendría por qué satisfacer una tolerancia pequeña. Escogemos $\delta=\min\{1,\varepsilon/(1+2|a|)\}$: la primera condición acota el factor y la segunda ajusta la precisión. El denominador es siempre positivo, incluso en $a=0$, y el mínimo también es positivo.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-013-015}

¿Un radio válido debe ser el máximo posible?

[]{#MA-MSOL-ANM-01-013-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

No. Basta un radio positivo cuyo control universal se pueda verificar; cualquier reducción positiva también sirve.

La definición pide existencia de algún radio válido, no una optimización. Si funciona $\delta$, también funciona cualquier $0<\delta'\le\delta$, porque la nueva ventana contiene menos entradas y todas ellas estaban ya controladas. Una elección conservadora puede facilitar las estimaciones sin cambiar la conclusión. Afirmar que un radio es máximo requiere una prueba adicional que descarte todos los radios mayores; no forma parte de demostrar el límite.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-013-016}

¿Qué barrera protege $1/x$ si $|x-a|<|a|/2$ y $a\ne0$?

[]{#MA-MSOL-ANM-01-013-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

$|x|\ge |a|-|x-a|>|a|/2>0$, de modo que el denominador está separado de cero uniformemente en la ventana.

La triangular inversa da $|x|\ge|a|-|x-a|$. Bajo el radio indicado, ese margen supera $|a|/2$, que es positivo porque $a\ne0$. De esta forma todas las entradas de la ventana evitan cero con una misma separación. Entonces $|1/x-1/a|=|x-a|/(|x||a|)$ se domina por $2|x-a|/|a|^2$. La barrera convierte el denominador variable en una constante segura para diseñar el radio de precisión.

</details>

### Ejercicios de la sección 13.2

#### Ejercicio 6. Diseñar el radio de una afín decreciente

[]{#MA-EX-ANM-01-013-006}

Prueba desde la definición que $-4x+7$ tiene límite $-1$ en $a=2$. Determina el mayor radio simétrico válido para un desafío $\varepsilon>0$.

[]{#MA-SOL-ANM-01-013-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

El error es $4|x-2|$. $\delta=\varepsilon/4$ sirve porque la entrada satisface una desigualdad estricta. Si $\delta>\varepsilon/4$, tomamos $t=(\delta+\varepsilon/4)/2$ y $x=2+t$. Entonces $0<t<\delta$ y $4t>\varepsilon$, infracción. Por tanto el radio dado es el mayor. El signo de la pendiente invierte orden, pero el error depende de su magnitud.

**Retorno visual.** Véase [C13-F02](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 7. Un radio conservador para un cuadrado

[]{#MA-EX-ANM-01-013-007}

Prueba desde la definición $x^2\to4$ en $2$ y da un radio explícito que no necesite resolver una desigualdad cuadrática.

[]{#MA-SOL-ANM-01-013-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Para $|x-2|<1$, $|x+2|\le|x-2|+4<5$. Dado $\varepsilon>0$, tomamos $\delta=\min(1,\varepsilon/5)$. Entonces $|x^2-4|=|x-2||x+2|<5|x-2|<5\delta\le\varepsilon$. El radio auxiliar elimina el factor variable.

</details>

#### Ejercicio 8. Radio óptimo del cuadrado en uno

[]{#MA-EX-ANM-01-013-008}

Para $0<\varepsilon<1$, demuestra que el mayor radio simétrico para $|x^2-1|<\varepsilon$ alrededor de $1$ es $\delta_*=\sqrt{1+\varepsilon}-1$.

[]{#MA-SOL-ANM-01-013-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

La componente de entradas positivas que satisface el error es $(\sqrt{1-\varepsilon},\sqrt{1+\varepsilon})$. Los márgenes desde $1$ son $1-\sqrt{1-\varepsilon}$ y $\sqrt{1+\varepsilon}-1$. El segundo es menor: racionalizar da $\varepsilon/(1+\sqrt{1-\varepsilon})>\varepsilon/(1+\sqrt{1+\varepsilon})$. Así el intervalo simétrico de radio $\delta_*$ queda dentro de esa componente, pues su extremo inferior supera $\sqrt{1-\varepsilon}$. Si un radio es mayor, incluye $x=\sqrt{1+\varepsilon}$, distinto de $1$, cuyo error es exactamente $\varepsilon$, infracción.

**Retorno visual.** Véase [C13-F03](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. Reparar una respuesta que depende de la entrada

[]{#MA-EX-ANM-01-013-009}

Un borrador afirma: «Para probar $x^2\to1$, tomo $\delta=\varepsilon/(|x+1|+1)$; así el error será pequeño». Localiza el defecto y escribe una prueba válida.

[]{#MA-SOL-ANM-01-013-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

La expresión de $\delta$ utiliza el $x$ que debía verificarse después de fijar el radio. No produce una respuesta única para toda la ventana. La reparación fija primero $|x-1|<1$, que da $|x+1|<3$, y elige $\delta=\min(1,\varepsilon/3)$. Para toda entrada de esa ventana, $|x^2-1|<3|x-1|<\varepsilon$. La fórmula defectuosa queda como objeto de diagnóstico, no como prueba.

</details>

#### Ejercicio 10. Proteger un recíproco desplazado

[]{#MA-EX-ANM-01-013-010}

Prueba desde la definición que $1/(x-3)$ tiene límite $-1/2$ en $a=1$.

[]{#MA-SOL-ANM-01-013-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Si $|x-1|<1$, entonces $|x-3|\ge2-|x-1|>1$; las entradas no alcanzan $3$. El error es $|1/(x-3)+1/2|=|x-1|/(2|x-3|)<|x-1|/2$. Tomamos $\delta=\min(1,2\varepsilon)$. Para toda entrada del dominio dentro de esa ventana, el error es menor que $\delta/2\le\varepsilon$.

</details>
## 13.3. Un destino, barreras locales y orden

[]{#MA-SEC-ANM-01-013-003}

La definición presenta un candidato $L$. Antes de llamarlo el límite debemos comprobar que ningún otro candidato puede cumplir el mismo contrato. La geometría sugiere usar dos ventanas de salida disjuntas, pero necesitamos una entrada que ambas estén obligadas a controlar.

### Unicidad

**Teorema.** Si $a\in D'$ y $f:D\to\mathbb R$ tiene límites $L$ y $M$ en $a$, entonces $L=M$.

Si fueran distintos, $d=|L-M|>0$. Proponemos $\varepsilon=d/3$ a ambos contratos, obteniendo $\delta_L,\delta_M>0$. Tomamos $\delta=\min(\delta_L,\delta_M)$. Aquí gastamos la acumulación: existe $x\in D$ con $0<|x-a|<\delta$. Para esa misma entrada las dos cotas dan $d\le |L-f(x)|+|f(x)-M|<2d/3$, contradicción. La coincidencia de la entrada importa tanto como la separación de las salidas.

### Acotación suficiente cerca del centro

Si $f\to L$, usamos una sola tolerancia, $\varepsilon=1$. Existe $r>0$ con $|f(x)-L|<1$ en $U_D(a,r)$; por tanto $|f(x)|\le |f(x)-L|+|L|<|L|+1$. Ésta es una cota local perforada. No afirma acotación de toda la función: $x^2\to0$ en cero y es no acotada en $\mathbb R$.

Si $a\in D$ podemos incluir su valor en una cota mayor, por ejemplo $\max(|L|+1,|f(a)|+1)$. Esto no transforma el límite en una afirmación sobre el valor central; sólo añade un dato finito a una cota.

### El orden eventual pasa al límite

Supongamos $f,g:D\to\mathbb R$, $f\to L$, $g\to M$ y $f(x)\le g(x)$ en alguna ventana perforada. Si $L>M$, ponemos $\varepsilon=(L-M)/3$ y reunimos los dos radios y la ventana de orden. Acumulación entrega una entrada allí. Entonces $f(x)>L-\varepsilon>M+\varepsilon>g(x)$, contradicción. Concluimos $L\le M$. Un orden estricto de valores no fuerza orden estricto de límites: $0<x$ en $(0,\infty)$ y ambas funciones tienen límite cero.

**Teorema del encierro.** Si $p(x)\le f(x)\le q(x)$ cerca de $a$, $p\to L$ y $q\to L$, entonces $f\to L$. Para $\varepsilon>0$, reúna radios para $p,q$ y para el orden. Allí $L-\varepsilon<p(x)\le f(x)\le q(x)<L+\varepsilon$, luego $|f(x)-L|<\varepsilon$. No hemos supuesto existencia previa del límite de $f$; acabamos de probarla.

Como primer uso, sea $b:D\to\mathbb R$ con $|b(x)|\le K$ cerca de cero, donde $K\ge0$ y $0\in D'$. Para $h(x)=xb(x)$, $|h(x)|\le K|x|$. Si $K=0$, el error es cero localmente. Si $K>0$, $\delta=\min(r,\varepsilon/K)$ prueba $h\to0$. El factor $b$ puede carecer de límite: sólo usamos su cota.

Un límite finito proporciona barreras locales; las barreras también pueden construir límites. Esta doble dirección será útil al operar con funciones que oscilan.

### Antes de seguir

#### Microcontrol 17

[]{#MA-MIC-ANM-01-013-017}

¿Dónde se utiliza acumulación al demostrar unicidad?

[]{#MA-MSOL-ANM-01-013-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Al obtener una entrada en el mínimo de los dos radios. Sin esa entrada, las dos cotas no podrían compararse.

Los dos candidatos proporcionan radios, pero para confrontar sus estimaciones necesitamos una entrada donde ambas valgan. La acumulación entrega $x\in D$ distinto de $a$ en la ventana de radio mínimo. Su salida sirve entonces como punto intermedio entre los dos candidatos. Si no hubiera entradas, ambos controles serían vacíos y no producirían contradicción. Éste es el lugar concreto donde la hipótesis de acumulación asegura contenido a la prueba.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-013-018}

¿Qué tolerancia se usa para dos destinos separados por $d>0$?

[]{#MA-MSOL-ANM-01-013-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

$\varepsilon=d/3$. Las dos distancias a una salida común suman menos que $2d/3<d$, contradicción.

Si los candidatos son $L$ y $M$ con $d=|L-M|>0$, elegimos radios para tolerancia $d/3$ respecto de cada uno. Una entrada común a ambas ventanas tiene salida $f(x)$ que satisface las dos cotas. La triangular da $d\le|L-f(x)|+|f(x)-M|<2d/3<d$, imposible. La elección divide el presupuesto dejando un margen estricto; no basta hablar de dos destinos cercanos sin fijar una tolerancia que los separe.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-013-019}

¿Un límite finito implica acotación global?

[]{#MA-MSOL-ANM-01-013-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

No. Sólo proporciona acotación en alguna ventana perforada; $x^2$ tiene límite cero en cero y no está acotada en $\mathbb R$.

El límite sólo controla entradas suficientemente cercanas al centro. La función puede crecer sin cota lejos de esa región. Para el cuadrado en cero, $|x|<\sqrt\varepsilon$ implica $x^2<\varepsilon$, lo que prueba el límite. Pero ninguna barrera global domina $x^2$ para todos los reales. La conclusión válida es acotación local perforada, no una propiedad de todo el dominio.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-013-020}

¿Qué cota local sale del desafío $\varepsilon=1$?

[]{#MA-MSOL-ANM-01-013-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

$|f(x)|<|L|+1$ cerca del centro, al usar $|f(x)|\le|f(x)-L|+|L|$.

El desafío uno proporciona un radio donde $|f(x)-L|<1$. Introducimos $L$ en la diferencia y usamos $|f(x)|\le|f(x)-L|+|L|<1+|L|$. Esto acota todas las salidas de esa ventana por la misma constante. No hemos controlado aún el centro excluido ni entradas lejanas. Si el centro pertenece al dominio y queremos incluirlo, basta ampliar la barrera para incorporar también su valor.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-013-021}

¿El orden estricto $f(x)<g(x)$ obliga $L<M$?

[]{#MA-MSOL-ANM-01-013-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

No. Por ejemplo $f(x)=0$, $g(x)=x$ en $(0,\infty)$ tienen límite cero en cero.

En el dominio positivo, cada entrada cumple $0<x$, así que la función cero está estrictamente debajo de la identidad. Sin embargo, ambas se aproximan a cero cuando las entradas se acercan a cero. La diferencia positiva puede hacerse arbitrariamente pequeña y desaparecer en el límite. El orden de límites conserva una desigualdad no estricta: un control estricto entre valores no obliga a mantener separación positiva entre los destinos.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-013-022}

¿Qué hay que suponer de $f$ antes de usar el encierro?

[]{#MA-MSOL-ANM-01-013-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Que esté entre las dos barreras localmente, con el mismo dominio pertinente. No se supone que ya tenga límite: el argumento construye su convergencia.

Las barreras deben satisfacer $u(x)\le f(x)\le v(x)$ en una ventana pertinente y tender ambas al mismo $L$. Para cada tolerancia tomamos una ventana donde las dos barreras estén cerca de $L$, junto con la de encierro. Entonces $L-\varepsilon<f(x)<L+\varepsilon$. Esa estimación demuestra el límite de $f$ sin suponerlo. El dominio y la acumulación siguen siendo necesarios para que el límite formulado tenga contenido.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-013-023}

Si $|b(x)|\le K$ cerca de cero, ¿qué error controla $xb(x)$?

[]{#MA-MSOL-ANM-01-013-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

$|xb(x)|\le K|x|$. Para $K>0$ se usa $\delta\le\varepsilon/K$; para $K=0$ el error es cero.

Si la acotación de $b$ vale en un radio $r$, para $K>0$ tomamos $\delta=\min\{r,\varepsilon/K\}$. Cada entrada perforada de esa ventana satisface $|xb(x)|\le K|x|<\varepsilon$. El mínimo reúne la región de acotación y la precisión. Para $K=0$, $b(x)=0$ en la ventana y el producto ya tiene error cero. Separar ese caso evita una división por cero.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-013-024}

¿Necesita $b$ tener límite para que $xb(x)\to0$?

[]{#MA-MSOL-ANM-01-013-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

No. Basta su acotación local, que domina la oscilación por un factor que se hace pequeño.

Una función localmente acotada puede oscilar sin aproximarse a un único número. Por ejemplo, cerca de cero puede valer uno en entradas racionales y menos uno en irracionales. Al multiplicarla por $x$, el error absoluto queda a lo sumo $|x|$, que se hace pequeño uniformemente. La oscilación no necesita desaparecer por sí sola; basta que su tamaño esté limitado y que el otro factor tienda a cero.

</details>

### Ejercicios de la sección 13.3

#### Ejercicio 11. Una cota que incluye el centro

[]{#MA-EX-ANM-01-013-011}

Si $a\in D$, $a\in D^{\prime}$ y $f\to L$, prueba que $f$ está acotada en alguna ventana no perforada $D\cap B(a,r)$, sin suponer $f(a)=L$.

[]{#MA-SOL-ANM-01-013-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

La tolerancia $1$ entrega $r>0$ con $|f(x)|<|L|+1$ para toda entrada no central de la ventana. Elegimos $K=\max(|L|+1,|f(a)|+1)$. En el centro, $|f(a)|<K$; fuera del centro, la cota previa da $|f(x)|<K$. La unión de ambos casos prueba acotación. Sólo se añadió un valor finito a una cota local.

</details>

#### Ejercicio 12. Encierro sin existencia supuesta

[]{#MA-EX-ANM-01-013-012}

Sea $f:\mathbb R\to\mathbb R$ y supongamos $-x^2\le f(x)\le2x^2$ para $0<|x|<1$. Prueba $f\to0$ sin usar reglas algebraicas posteriores.

[]{#MA-SOL-ANM-01-013-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Las cotas implican $|f(x)|\le2x^2$ en esa ventana. Para $\varepsilon>0$ tomamos $\delta=\min(1,\sqrt{\varepsilon/2})>0$. Si $0<|x|<\delta$, entonces $|f(x)|\le2x^2<2\delta^2\le\varepsilon$. No se supuso que $f$ tuviera límite: el control universal lo establece. Las raíces positivas pertenecen al álgebra real elemental.

</details>

#### Ejercicio 13. Oscilar y aun así converger

[]{#MA-EX-ANM-01-013-013}

Sea $b(x)=1$ para $x$ racional y $b(x)=-1$ para $x$ irracional. Prueba que $h(x)=xb(x)$ tiene límite cero en cero, sin decidir si $b$ tiene límite.

[]{#MA-SOL-ANM-01-013-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Para toda entrada, $|b(x)|=1$ y $|h(x)|=|x|$. Dado $\varepsilon>0$ basta $\delta=\varepsilon$. Si $0<|x|<\delta$, el error de $h$ es menor que $\varepsilon$. El control procede de la magnitud del factor, no de la existencia de su límite.

</details>

#### Ejercicio 14. El orden no conserva separación estricta

[]{#MA-EX-ANM-01-013-014}

Construye $f<g$ en una ventana perforada con el mismo límite, y prueba que en general sí se conserva el orden no estricto de límites.

[]{#MA-SOL-ANM-01-013-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

En $(0,\infty)$, $f(x)=0$ y $g(x)=x$ satisfacen $f<g$ y ambas tienen límite cero: para la identidad sirve $\delta=\varepsilon$. Para la afirmación general, si $f\to L$, $g\to M$ y $L>M$, pedimos errores menores que $(L-M)/3$, reunimos radios con la ventana de orden y obtenemos una entrada por acumulación. Allí $f>L-(L-M)/3>M+(L-M)/3>g$, contradicción. Luego $L\le M$.

</details>

#### Ejercicio 15. Dos destinos no caben en una misma ventana

[]{#MA-EX-ANM-01-013-015}

Reconstruye la unicidad usando tolerancia $|L-M|/2$ en vez de un tercio. Explica por qué las desigualdades estrictas siguen bastando.

[]{#MA-SOL-ANM-01-013-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Si $L\ne M$, $d=|L-M|>0$. Ambos contratos para $\varepsilon=d/2$ dan radios positivos. Acumulación proporciona una entrada en su mínimo. La triangular da $d\le|L-f(x)|+|f(x)-M|<d/2+d/2=d$, contradicción. La igualdad en la suma de tolerancias es admisible porque los errores individuales son estrictamente menores.

</details>
## 13.4. Negar un candidato y construir infracciones

[]{#MA-SEC-ANM-01-013-004}

Para probar un límite debemos responder a todas las tolerancias. Para refutar un candidato basta encontrar una tolerancia que ninguna ventana de entrada pueda satisfacer. La tolerancia de fracaso permanece fija mientras el radio de entrada cambia.

### La negación conserva el orden de dependencias

Con los datos $f,D,a,L$ fijados y $a\in D'$, negar el contrato equivale a

$$
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D:
\quad 0<|x-a|<\delta,\qquad |f(x)-L|\ge\varepsilon_0.
$$

El punto infractor sí puede depender del radio. La desigualdad final es $\ge$, no $>$: alcanzar la frontera de la bola abierta ya incumple el control.

Decir que $L$ no es límite es diferente de decir que la función no tiene ningún límite. Para lo segundo debemos descartar todo $L\in\mathbb R$ o usar un argumento que impida un destino único.

### Una infracción en cada escala

Para $n\in\mathbb N=\{0,1,\ldots\}$, sea $\eta_n=1/(n+1)$. Por C06, $\eta_n\to0$. Un candidato falla si y sólo si hay $\varepsilon_0>0$ para el que todos los conjuntos

$$
E_n=\{x\in D:0<|x-a|<\eta_n,\ |f(x)-L|\ge\varepsilon_0\}
$$

son no vacíos. La negación completa implica esto al usar $\delta=\eta_n$. Recíprocamente, fijado cualquier $\delta>0$, elegimos un índice con $\eta_n<\delta$ y obtenemos un único testigo de $E_n$. Ese punto incumple también el radio $\delta$.

Hemos construido una familia de conjuntos de infractores. No hemos construido automáticamente una función que elija un elemento de cada $E_n$. La distinción entre $\forall n\,\exists x$ y $\exists(x_n)\,\forall n$ se volverá necesaria en la equivalencia secuencial.

![C13-F04. Para f(x)=1 y el candidato L=0, xₙ=1/(n+2) infringe la tolerancia fija ε₀=1/2 dentro de cada escala ηₙ=1/(n+1). Esto refuta sólo el candidato 0: la función sí tiene límite 1. La fórmula proporciona aquí la ruta explícita.](../../assets/books/anm/C13/C13-F04.svg){#fig-anm-c13-f04 fig-alt="C13-F04. Para f(x)=1 y el candidato L=0, xₙ=1/(n+2) infringe la tolerancia fija ε₀=1/2 dentro de cada escala ηₙ=1/(n+1). Esto refuta sólo el candidato 0: la función sí tiene límite 1. La fórmula proporciona aquí la ruta explícita."}

### Refutar todos los destinos

Sea $s(x)=-1$ para $x<0$ y $s(x)=1$ para $x\ge0$, en dominio real. Para cualquier $L$, al menos una de las distancias $|-1-L|$, $|1-L|$ es $\ge1$: si ambas fueran menores que $1$, la triangular daría $2<2$.

Elegimos un signo cuya salida tenga esa distancia. Dado $\delta>0$, el punto $x=-\delta/2$ o $x=\delta/2$, según el signo elegido, es infractor con la tolerancia fija $\varepsilon_0=1$. El signo depende de $L$; el punto depende de $\delta$. Así se descarta todo candidato sin convertir el dibujo en una prueba.

Otra refutación útil: $r(x)=1/x$ en $(0,\infty)$ no tiene límite real finito en cero. Para cualquier $L$ y $\delta>0$, elijamos $x=\min(\delta/2,1/[2(|L|+1)])>0$. Entonces $x<\delta$ y $1/x\ge2(|L|+1)$, de donde $|1/x-L|\ge1/x-|L|>1$. No hemos definido aquí un límite infinito; sólo descartamos todos los reales.

### Antes de seguir

#### Microcontrol 25

[]{#MA-MIC-ANM-01-013-025}

¿Cuál es el orden de cuantificadores al refutar un candidato?

[]{#MA-MSOL-ANM-01-013-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

$\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$. La tolerancia queda fija y el infractor puede depender del radio.

Fijado el candidato $L$, refutarlo exige una tolerancia positiva que ninguna ventana consiga cumplir. Después de que se proponga cualquier radio, encontramos una entrada $x\in D$ con $0<|x-a|<\delta$ y $|f(x)-L|\ge\varepsilon_0$. El infractor puede cambiar con el radio; la tolerancia no. Esta persistencia a todas las escalas distingue una refutación de observar un único valor lejano al candidato.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-013-026}

¿Por qué la negación usa $\ge\varepsilon_0$?

[]{#MA-MSOL-ANM-01-013-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Porque negar $|f(x)-L|<\varepsilon_0$ en el orden real da $|f(x)-L|\ge\varepsilon_0$. La frontera también infringe una bola abierta.

La bola de precisión usa desigualdad estricta. Su complemento incluye tanto salidas más lejanas como las que quedan exactamente en su frontera. Por ejemplo, un error igual a uno incumple el desafío $\varepsilon_0=1$. Si en la negación exigiéramos sólo errores mayores que la tolerancia, eliminaríamos infractores legítimos. La inversión de cuantificadores debe acompañarse de la negación exacta de la desigualdad.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-013-027}

¿Refutar $L=0$ basta para demostrar que no existe ningún límite?

[]{#MA-MSOL-ANM-01-013-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

No. Otro real podría ser límite. Hay que descartar todos los candidatos o usar una contradicción independiente del candidato.

La función constante uno no tiene límite cero, pero sí tiene límite uno. Por eso una refutación del candidato cero no descarta existencia de límite. Para demostrar inexistencia, debemos mostrar que cada real propuesto falla, o producir datos que contradigan cualquier posible destino, como dos rutas admisibles cuyas imágenes tengan límites distintos. La conclusión debe conservar el alcance lógico del argumento que se ha probado.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-013-028}

¿Por qué usamos $1/(n+1)$ en vez de $1/n$ desde $n=0$?

[]{#MA-MSOL-ANM-01-013-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Porque $n+1>0$ para todos los índices, mientras $1/0$ no está definido.

La indexación comienza en cero, de modo que $1/n$ no define el primer término. Sustituir el denominador por $n+1$ lo hace positivo para todos los índices y produce una sucesión completa. Sus términos se acercan a cero porque, para cualquier tolerancia, podemos hacer $n+1$ mayor que su recíproco. El desplazamiento corrige la definición sin cambiar el mecanismo de aproximación por escalas cada vez menores.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-013-029}

¿Qué prueba la no vaciedad de todos los conjuntos $E_n$?

[]{#MA-MSOL-ANM-01-013-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Que el candidato falla. Para cualquier radio elegimos una escala menor y un único infractor de ese conjunto.

Cada $E_n$ reúne infractores de la misma tolerancia dentro de la escala $\eta_n=1/(n+1)$. Para un radio arbitrario $\delta$, arquimedianidad permite elegir $n$ con $\eta_n<\delta$. La no vaciedad de ese conjunto proporciona una entrada que también está dentro del radio propuesto y mantiene el error grande. Para refutar el candidato sólo escogemos un testigo de un conjunto a la vez; no necesitamos todavía una sucesión de testigos.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-013-030}

¿La no vaciedad de cada $E_n$ proporciona por sí sola un selector?

[]{#MA-MSOL-ANM-01-013-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

No. $\forall n\exists x\in E_n$ no permite intercambiar cuantificadores sin una regla de selección o una hipótesis adicional.

Construir una sucesión requiere una asignación simultánea $n\mapsto x_n$ con $x_n\in E_n$ para todo índice. La afirmación de que cada conjunto tiene algún elemento no especifica esa asignación. En el marco fundacional explícito del capítulo, el paso se justifica mediante una regla dada, una enumeración que permita seleccionar mínimos o el principio adicional de elección numerable. No debe quedar oculto en la frase «escojamos un infractor para cada escala».

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-013-031}

Para el salto con valores $\pm1$, ¿por qué una distancia a $L$ es al menos $1$?

[]{#MA-MSOL-ANM-01-013-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Si ambas fueran menores que $1$, la triangular daría $2=|1-(-1)|<2$, contradicción.

Las dos salidas del salto están separadas por dos unidades. Si el candidato estuviera a menos de una unidad de ambas, usarlo como punto intermedio daría una separación menor que dos, contradicción. Al menos una rama conserva por tanto error mayor o igual que uno. Elegimos esa rama según $L$ y, para cada radio, una entrada de su signo a distancia $\delta/2$. Así el error persiste arbitrariamente cerca del centro.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-013-032}

¿Qué asegura $x=\min(\delta/2,1/[2(|L|+1)])$ en la refutación de $1/x$?

[]{#MA-MSOL-ANM-01-013-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

$0<x<\delta$ y $1/x\ge2(|L|+1)$, luego $|1/x-L|>1$. Funciona para cualquier candidato real.

Los dos números del mínimo son positivos, de modo que $x>0$. Además $x\le\delta/2<\delta$ y $x\le1/[2(|L|+1)]$, lo que implica $1/x\ge2(|L|+1)$. La triangular inversa da $|1/x-L|\ge1/x-|L|\ge|L|+2>1$. La misma tolerancia uno refuta cada candidato finito, usando una entrada que puede depender de él y del radio.

</details>

### Ejercicios de la sección 13.4

#### Ejercicio 16. La frontera ya es infracción

[]{#MA-EX-ANM-01-013-016}

Para $f(x)=x$ en cero y candidato $L=1$, da una tolerancia fija y un infractor explícito para cada radio.

[]{#MA-SOL-ANM-01-013-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Tomemos $\varepsilon_0=1$. Dado $\delta>0$, sea $x=-\delta/2$. Entonces $0<|x|<\delta$ y $|x-1|=1+\delta/2>1$. El candidato se refuta aunque la función sí tiene otro límite, cero.

**Retorno visual.** Véase [C13-F04](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 17. Una escala basta para todos los radios

[]{#MA-EX-ANM-01-013-017}

Sean $r_n>0$ tales que para cada $\delta>0$ existe $n$ con $r_n<\delta$. Prueba que la negación del límite equivale a no vaciedad de los infractores en cada escala $r_n$, para una misma tolerancia.

[]{#MA-SOL-ANM-01-013-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

La negación completa aplicada a $\delta=r_n$ produce un infractor para cada $n$ con la misma $\varepsilon_0$. A la inversa, dados conjuntos no vacíos y un radio cualquiera $\delta$, la propiedad de la escala da $n$ con $r_n<\delta$. Un único punto infractor de ese conjunto también está en la ventana de radio $\delta$ y conserva el error $\ge\varepsilon_0$. No hace falta escoger todos los puntos a la vez.

</details>

#### Ejercicio 18. Todos los reales quedan descartados

[]{#MA-EX-ANM-01-013-018}

Prueba directamente, sin sucesiones, que $f(x)=1/|x|$ en $\mathbb R\setminus\{0\}$ no tiene límite real finito en cero.

[]{#MA-SOL-ANM-01-013-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Fijemos cualquier $L$. Para tolerancia $1$ y cualquier $\delta>0$, elegimos $x=\min(\delta/2,1/[2(|L|+1)])>0$. Está en el dominio y en la ventana perforada; $1/|x|\ge2(|L|+1)$ implica $|f(x)-L|\ge f(x)-|L|>1$. Cada candidato tiene infractores arbitrariamente próximos, por lo que no existe límite real finito.

</details>

#### Ejercicio 19. Cada entrada favorable no es un límite

[]{#MA-EX-ANM-01-013-019}

Prueba que la condición «para todo $\varepsilon,\delta>0$ existe $x$ con $0<|x|<\delta$ y $|f(x)|<\varepsilon$» no garantiza $f\to0$.

[]{#MA-SOL-ANM-01-013-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Sea $f(x)=0$ para $x>0$, $f(x)=1$ para $x\le0$. Dadas $\varepsilon,\delta>0$, el punto $\delta/2$ cumple la condición favorable. Pero el punto $-\delta/2$ tiene error $1$ para cada radio, por lo que la tolerancia $\varepsilon_0=1/2$ refuta $L=0$. La condición débil elige una entrada; el límite debe controlar todas.

</details>

#### Ejercicio 20. Fallo sin magnitud infinita

[]{#MA-EX-ANM-01-013-020}

Construye una función globalmente acotada sin límite en cero y refútala para todo candidato mediante una tolerancia fija.

[]{#MA-SOL-ANM-01-013-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

El salto con salidas $-1$ y $1$ está acotado por $1$. Para cada candidato $L$ una de las distancias a esas dos salidas es $\ge1$, por triangular. Fijado ese signo, el punto con ese signo y magnitud $\delta/2$ infringe el error para cualquier radio, con tolerancia $1$. La falta de límite puede deberse a incompatibilidad de destinos sin que los valores sean grandes.

</details>
## 13.5. Lo que detectan las sucesiones

[]{#MA-SEC-ANM-01-013-005}

Una aproximación secuencial elige una ruta numerada dentro del dominio. El límite funcional debe controlar todas esas rutas, pero una ruta favorable no certifica el comportamiento de toda una ventana.

Llamemos admisible a una sucesión $(x_n)$ con $x_n\in D\setminus\{a\}$ para todos los índices y $x_n\to a$. Las imágenes forman una sucesión bien tipada: $x:\mathbb N\to D$ se compone con $f:D\to\mathbb R$. No basta que $x_n$ sea real; debe pertenecer al dominio y evitar el centro.

### De la ventana a cualquier ruta

**Proposición.** Si $f\to L$ en $a$, entonces $f(x_n)\to L$ para toda sucesión admisible.

Fijemos tal sucesión y $\varepsilon>0$. El límite funcional ofrece $\delta>0$. La convergencia de entradas ofrece $N$ con $|x_n-a|<\delta$ para $n\ge N$. Por admisibilidad, también $0<|x_n-a|$; la implicación funcional da $|f(x_n)-L|<\varepsilon$ en toda esa cola. No se ha elegido una nueva sucesión.

Si permitiéramos términos iguales a $a$, la sucesión constante del centro exigiría $f(a)=L$. La definición perforada no proporciona esa igualdad. Se puede permitir un prefijo finito de centros si la cola los evita, usando el carácter eventual de C06.

### La recíproca: dónde aparece una selección

Si el candidato falla, §13.4 ofrece conjuntos $E_n$ no vacíos. Para contradecir el control de todas las rutas queremos una ruta con $x_n\in E_n$. Una colección de existencias no es todavía una regla de selección.

**Teorema para un dominio enumerado.** Si está dada una sobreyección $e:\mathbb N\to D$, entonces $f\to L$ si y sólo si todas las sucesiones admisibles tienen imágenes que convergen a $L$.

La dirección directa está probada. Para la inversa, si el límite falla, fijemos $\varepsilon_0$ y los $E_n$. El conjunto $I_n=\{k\in\mathbb N:e(k)\in E_n\}$ es no vacío por sobreyectividad. Definimos $k_n=\min I_n$, mínimo único de naturales, y $x_n=e(k_n)$. Entonces $0<|x_n-a|<1/(n+1)$, luego $x_n\to a$, mientras $|f(x_n)-L|\ge\varepsilon_0$ para todo índice. Sus imágenes no convergen a $L$, contradicción. Los $k_n$ no tienen que ser estrictamente crecientes; ésta no es una extracción de una sucesión previa.

![C13-F05. En el dominio de recíprocos enteros, con f=1, a=L=0 y ε₀=1/2, la enumeración empieza con los denominadores 1,4,2,8,3,5,7,6 y continúa 9,10,… . Se marca e(k)<1/(n+1) y se rodea el menor índice válido. Los índices seleccionados pueden repetirse; el mínimo es de índices, no de valores reales.](../../assets/books/anm/C13/C13-F05.svg){#fig-anm-c13-f05 fig-alt="C13-F05. En el dominio de recíprocos enteros, con f=1, a=L=0 y ε₀=1/2, la enumeración empieza con los denominadores 1,4,2,8,3,5,7,6 y continúa 9,10,… . Se marca e(k)&lt;1/(n+1) y se rodea el menor índice válido. Los índices seleccionados pueden repetirse; el mínimo es de índices, no de valores reales."}

**Teorema condicional para dominios arbitrarios.** Bajo el principio de elección numerable para subconjuntos de reales, $\mathrm{CC}(\mathbb R)$, vale la misma equivalencia para todo $D\subseteq\mathbb R$. Este principio dice que cada familia numerable de subconjuntos reales no vacíos admite un selector. Aplicarlo a los $E_n$ produce $x_n\in E_n$; las dos desigualdades anteriores completan la contradicción. Es exactamente el paso adicional. No lo necesitamos para la dirección directa ni para el caso enumerado, y no lo incorporamos silenciosamente como axioma.

### Refutar con rutas ya dadas

Para el salto de §13.4, $u_n=-1/(n+1)$ y $v_n=1/(n+1)$ son admisibles en cero. Sus imágenes son constantes $-1$ y $1$. Si hubiese límite funcional $L$, la dirección directa y la unicidad secuencial de C06 obligarían $L=-1=1$. Esta refutación es incondicional: las rutas están dadas mediante fórmulas, no elegidas de conjuntos arbitrarios.

Una sola ruta con imágenes que no convergen a un candidato lo refuta. Dos rutas con destinos distintos refutan la existencia de cualquier límite. Muchas rutas favorables, sin argumento universal, no prueban existencia.

### Antes de seguir

#### Microcontrol 33

[]{#MA-MIC-ANM-01-013-033}

¿Qué tres condiciones hacen admisible a $(x_n)$?

[]{#MA-MSOL-ANM-01-013-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

$x_n\in D$, $x_n\ne a$ para todos los índices y $x_n\to a$.

Las dos primeras condiciones aseguran que cada evaluación $f(x_n)$ está definida y corresponde a una entrada perforada. La convergencia de las entradas asegura que toda cola suficientemente tardía queda dentro de cualquier radio dado. Juntas permiten transportar el control funcional a un control secuencial. Acercarse al centro no basta si se utilizan entradas fuera del dominio o si se repite el centro que la definición excluye.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-013-034}

¿Cómo se encadenan $\varepsilon$, $\delta$ y $N$ en la dirección directa?

[]{#MA-MSOL-ANM-01-013-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

$\varepsilon$ exige un radio $\delta$ para la función; la convergencia de entradas proporciona $N$ para ese radio; la cola cumple el error de salida.

Recibida $\varepsilon>0$, el límite funcional entrega un radio $\delta>0$. La convergencia $x_n\to a$ entrega luego un corte $N$ con $|x_n-a|<\delta$ para todos los índices tardíos. La admisibilidad aporta $x_n\ne a$ y $x_n\in D$, completando el antecedente del control funcional. Por eso $|f(x_n)-L|<\varepsilon$ en toda esa cola. Cada escala se elige después de la que debe responder.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-013-035}

¿Por qué la sucesión constante $x_n=a$ no es admisible?

[]{#MA-MSOL-ANM-01-013-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Porque alcanza siempre el centro excluido. Evaluaría $f(a)$, un dato que el límite perforado no controla.

La sucesión constante en el centro sí converge a él, pero no cumple $x_n\ne a$. Si $f(a)$ está definido, sus imágenes serían constantemente ese valor, que puede diferir del límite perforado. Si el centro no pertenece al dominio, las imágenes ni siquiera podrían evaluarse. Excluirlo evita que un dato central ajeno al límite se introduzca en una ruta que pretende comprobar la aproximación.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-013-036}

Si una ruta admisible tiene imágenes que no convergen a $L$, ¿qué concluyes?

[]{#MA-MSOL-ANM-01-013-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Que $L$ no puede ser el límite funcional. Si lo fuera, la dirección directa controlaría también esa ruta.

La dirección directa afirma que un límite funcional debe controlar todas las sucesiones admisibles. Encontrar una sola que incumpla la convergencia hacia $L$ contradice esa consecuencia necesaria. Esto refuta precisamente ese candidato. Si las imágenes convergen a otro valor, podríamos estar viendo el verdadero destino; para descartar cualquier límite hacen falta además datos que contradigan todos los candidatos, por ejemplo dos rutas con destinos diferentes.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-013-037}

¿Qué regla elige infractores cuando está dada $e:\mathbb N\to D$ sobreyectiva?

[]{#MA-MSOL-ANM-01-013-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

$k_n=\min\{k:e(k)\in E_n\}$ y $x_n=e(k_n)$. La no vaciedad garantiza un mínimo natural único.

La sobreyectividad de $e$ garantiza que algún índice de la enumeración representa un elemento del conjunto no vacío $E_n$. El conjunto de esos índices es entonces un subconjunto no vacío de naturales y tiene un mínimo único. Esta regla define $x_n$ sin escoger arbitrariamente entre reales. Como $x_n\in E_n$, sus distancias al centro quedan por debajo de $1/(n+1)$ y sus errores de salida mantienen la tolerancia que refuta el candidato.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-013-038}

¿Deben crecer estrictamente los $k_n$ de ese selector?

[]{#MA-MSOL-ANM-01-013-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

No. No se está construyendo una subsucesión de $e$; se escoge una entrada que infringe cada escala.

El objetivo es satisfacer una condición de pertenencia a $E_n$ en cada escala, no preservar el orden de una enumeración. La regla vuelve a buscar el primer índice admisible para cada conjunto y no impone crecimiento estricto. Para que $x_n\to a$ basta la cota $0<|x_n-a|<1/(n+1)$. No hace falta interpretar la ruta como extracción de $e$ ni añadir condiciones a los índices que la construcción no proporciona.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-013-039}

¿Qué hipótesis permite la recíproca en cualquier dominio real?

[]{#MA-MSOL-ANM-01-013-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

$\mathrm{CC}(\mathbb R)$, aplicada explícitamente a la familia de conjuntos reales no vacíos $E_n$. El teorema es condicional a esa hipótesis.

Cuando el dominio no tiene una enumeración dada, los conjuntos $E_n$ siguen siendo subconjuntos reales no vacíos, pero falta la regla anterior de mínimos de índices. El principio $\mathrm{CC}(\mathbb R)$ entrega un selector para esa familia numerable. Con él construimos una ruta que se acerca a $a$ mientras mantiene el error grande y contradice la hipótesis secuencial. El capítulo registra esta hipótesis adicional explícitamente; la dirección directa no la utiliza.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-013-040}

¿Necesita elección numerable la refutación por las rutas $\pm1/(n+1)$?

[]{#MA-MSOL-ANM-01-013-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No. Las dos rutas están dadas por fórmulas y la dirección directa basta para comparar sus destinos distintos.

Las fórmulas ya definen cada término de las dos rutas, por lo que no se seleccionan elementos de conjuntos arbitrarios. En el salto, sus imágenes son constantemente menos uno y uno. Si existiera un límite funcional, la dirección directa obligaría a que ambas imágenes convergieran a él; la unicidad del límite de sucesiones lo identificaría con dos números distintos. La contradicción se obtiene sin recurrir a la recíproca condicional.

</details>

### Ejercicios de la sección 13.5

#### Ejercicio 21. Una ruta favorable engaña

[]{#MA-EX-ANM-01-013-021}

Sea $f(x)=0$ si $x=1/(n+1)$ para algún $n\in\mathbb N$ y $f(x)=1$ en las demás entradas reales. Encuentra dos rutas admisibles en cero que descarten un límite.

[]{#MA-SOL-ANM-01-013-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

La ruta $u_n=1/(n+1)$ tiene imágenes cero. La ruta $v_n=-1/(n+1)$ tiene imágenes uno, pues nunca coincide con una entrada positiva de la primera ruta. Ambas evitan cero y convergen a él por C06. Si hubiese límite $L$, la dirección directa y la unicidad secuencial darían a la vez $L=0$ y $L=1$, contradicción.

</details>

#### Ejercicio 22. Un prefijo puede tocar el centro

[]{#MA-EX-ANM-01-013-022}

Supón $f\to L$ en $a$, $x_n\in D$ y $x_n\to a$, con $x_n\ne a$ para todos los índices a partir de cierto $N_0$. Prueba $f(x_n)\to L$ si $f$ está definida en todos los términos.

[]{#MA-SOL-ANM-01-013-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Dado $\varepsilon>0$, el límite funcional ofrece $\delta$. La convergencia de $x_n$ da $N_1$ que asegura $|x_n-a|<\delta$. Para $n\ge\max(N_0,N_1)$ también hay distancia positiva, y la implicación funcional produce error menor que $\varepsilon$. Los términos anteriores no afectan la convergencia.

</details>

#### Ejercicio 23. El mínimo vive en los índices

[]{#MA-EX-ANM-01-013-023}

En un dominio enumerado, justifica la existencia del selector $x_n=e(\min I_n)$ y explica por qué no se toma el mínimo de $E_n\subseteq\mathbb R$.

[]{#MA-SOL-ANM-01-013-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Por sobreyectividad y no vaciedad de $E_n$, el conjunto $I_n=\{k:e(k)\in E_n\}$ contiene algún natural. El buen orden da un mínimo único. La regla $n\mapsto\min I_n$ es funcional y su composición con $e$ produce el selector real. Un conjunto real no vacío puede no tener mínimo, por ejemplo $(0,1)$; no se puede reemplazar el mínimo de índices por uno de valores.

**Retorno visual.** Véase [C13-F05](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 24. La ruta de infracciones prueba la recíproca

[]{#MA-EX-ANM-01-013-024}

Bajo $\mathrm{CC}(\mathbb R)$, prueba la recíproca secuencial y localiza exactamente el uso de la hipótesis.

[]{#MA-SOL-ANM-01-013-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Supongamos que todas las rutas admisibles tienen imágenes tendiendo a $L$ y que falla el contrato funcional. Hay $\varepsilon_0>0$ y conjuntos reales $E_n$ no vacíos de infractores con $0<|x-a|<1/(n+1)$. Aplicamos aquí, y sólo aquí, $\mathrm{CC}(\mathbb R)$ para obtener una función $n\mapsto x_n\in E_n$. Las cotas implican $x_n\to a$, pero $|f(x_n)-L|\ge\varepsilon_0$ para todos los índices impide convergencia de imágenes a $L$. La contradicción prueba el límite. No se presenta como prueba incondicional.

</details>

#### Ejercicio 25. No hace falta una ruta distinta en cada paso

[]{#MA-EX-ANM-01-013-025}

Para el selector de infractores, demuestra que los términos no necesitan ser distintos entre sí, pero ningún punto fijo distinto de $a$ puede aparecer en índices arbitrariamente grandes.

[]{#MA-SOL-ANM-01-013-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

La prueba de convergencia sólo necesita $|x_n-a|<1/(n+1)$; no usa inyectividad. Si un punto fijo $t\ne a$ apareciera en índices arbitrariamente grandes, su distancia $d=|t-a|>0$ tendría que ser menor que $1/(n+1)$ para índices con esa escala menor que $d$, imposible. Puede haber repeticiones finitas de valores, aunque no se hayan exigido términos diferentes.

</details>
## 13.6. Combinar límites con presupuestos de error

[]{#MA-SEC-ANM-01-013-006}

Ya sabemos construir radios para funciones concretas. Ahora probaremos reglas que permitan combinar límites sin rehacer toda la estimación. Las pruebas se harán con ventanas, de modo que no dependerán de la recíproca secuencial condicional.

Sean $f,g:D\to\mathbb R$, $a\in D'$, $f\to L$ y $g\to M$. Todas las restricciones siguientes se cumplen en ventanas perforadas de ese mismo dominio.

### Sumas, constantes y magnitudes

Para $\varepsilon>0$, tomamos radios que aseguren $|f-L|<\varepsilon/2$ y $|g-M|<\varepsilon/2$. Su mínimo da $|(f+g)-(L+M)|\le |f-L|+|g-M|<\varepsilon$. Por tanto $f+g\to L+M$.

Para $\lambda f$, si $\lambda=0$ el error es cero; si $\lambda\ne0$, pedimos $|f-L|<\varepsilon/|\lambda|$. Entonces $|\lambda f-\lambda L|<\varepsilon$. Esto prueba también restas usando $\lambda=-1$ y la regla de suma. La triangular inversa da $||f|-|L||\le |f-L|$, así que $|f|\to|L|$ con el mismo radio.

### El producto necesita una barrera y dos errores

La identidad útil es $fg-LM=f(g-M)+M(f-L)$. El primer factor $f$ varía; §13.3 nos permite fijar $|f|<A:=|L|+1$ en algún radio $r$. Sea $B=|M|+1>0$. Para $\varepsilon>0$ pedimos $|g-M|<\varepsilon/(2A)$ y $|f-L|<\varepsilon/(2B)$, y reunimos esos radios con $r$. Allí

$$
|fg-LM|\le |f||g-M|+|M||f-L|
<A\frac{\varepsilon}{2A}+B\frac{\varepsilon}{2B}
=\varepsilon.
$$

El uso de $B$ evita dividir por $|M|$ cuando $M=0$. La identidad no basta sola: la cota local convierte un coeficiente variable en una constante que permite repartir el presupuesto.

### Recíprocos y cocientes: restringir el dominio a tiempo

Si $M\ne0$, pedir $|g-M|<|M|/2$ da $|g|>|M|/2$. Por tanto $g(x)\ne0$ cerca de $a$ y

$$
\left|\frac1{g(x)}-\frac1M\right|
=\frac{|g(x)-M|}{|g(x)||M|}
<\frac{2|g(x)-M|}{|M|^2}.
$$

Pedimos además $|g-M|<\varepsilon |M|^2/2$ y tomamos el mínimo de radios. Así $1/g\to1/M$ en $D_0=\{x\in D:g(x)\ne0\}$. Este dominio tiene a $a$ como punto de acumulación: para cualquier radio, la acumulación de $D$ ofrece un punto dentro del mínimo con la ventana de no anulación, y ese punto pertenece a $D_0$.

La restricción de $f$ a $D_0$ conserva su límite porque el control universal en $D$ vale en el subconjunto. Aplicar la regla del producto a $f|_{D_0}$ y $1/g$ prueba $f/g\to L/M$. No se afirma que el cociente esté definido en todos los puntos del dominio original.

### Primer uso y una trampa

Suma y producto prueban por inducción finita que un polinomio $P$ tiene límite $P(a)$ en cada $a$: las constantes y la identidad cumplen la definición, multiplicar construye potencias y sumar reúne términos. Si $Q(a)\ne0$, el cociente $P/Q$ tiene límite $P(a)/Q(a)$ en su dominio natural. Esta prueba no usa continuidad ni derivadas.

Si $Q(a)=0$, la regla de cocientes no decide nada. $(x^2-1)/(x-1)$ en $x\ne1$ se simplifica a $x+1$ y tiene límite $2$ en $1$. En cambio $1/(x-1)$ no tiene límite finito allí. El denominador límite no nulo es una hipótesis suficiente del criterio, no una clasificación de todo cociente posible.

### Antes de seguir

#### Microcontrol 41

[]{#MA-MIC-ANM-01-013-041}

¿Cómo se reparte $\varepsilon$ en una suma?

[]{#MA-MSOL-ANM-01-013-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Con errores menores que $\varepsilon/2$ para cada sumando y el mínimo de ambos radios.

La diferencia de la suma respecto del destino es $(f-L)+(g-M)$. La triangular la domina por la suma de ambos errores. Pedimos que cada uno sea menor que $\varepsilon/2$ y escogemos el mínimo de sus radios, para que los dos controles valgan en la misma ventana. El error total queda entonces estrictamente por debajo de $\varepsilon$. Reducir ventanas permite sincronizar condiciones; no hace falta conocer un radio óptimo.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-013-042}

¿Cómo se trata la multiplicación por una constante nula?

[]{#MA-MSOL-ANM-01-013-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Por separado: el error de la función cero es cero, sin dividir por la constante.

Si la constante es cero, tanto la función multiplicada como el destino multiplicado son cero en toda entrada admitida. El error es por tanto cero y cualquier radio positivo sirve. Para una constante $c\ne0$ se pide al límite original una precisión $\varepsilon/|c|$. Esta fórmula sólo se usa después de separar el caso cero, porque dividir por su magnitud en ese caso no tendría sentido.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-013-043}

¿Qué identidad prepara el producto?

[]{#MA-MSOL-ANM-01-013-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

$fg-LM=f(g-M)+M(f-L)$. Se controla $f$ con una barrera local y los dos errores con radios.

Añadir y restar $fM$ produce la identidad $fg-LM=f(g-M)+M(f-L)$. El primer error aparece multiplicado por un valor variable de $f$, que necesita una barrera local común; el segundo por la constante $M$. Una cota como $|f|<|L|+1$ convierte ambos multiplicadores en datos fijos. Entonces podemos distribuir la tolerancia entre los dos errores y reunir los radios que aseguran barrera y precisión.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-013-044}

¿Por qué $|M|+1$ es útil en el presupuesto de producto?

[]{#MA-MSOL-ANM-01-013-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Es positivo incluso si $M=0$, y domina $|M|$. Permite dividir por una constante segura.

Si usáramos $|M|$ en un denominador, el caso $M=0$ dejaría la expresión sin definir. Usar $|M|+1$ mantiene un denominador positivo y no menor que la magnitud del multiplicador. Por ejemplo, pedir $|f-L|<\varepsilon/[2(|M|+1)]$ garantiza que $|M||f-L|<\varepsilon/2$ cuando el multiplicador es positivo; si es cero, el producto del error es cero. La elección deja un margen uniforme y cubre ambos casos.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-013-045}

¿Qué tolerancia garantiza que $g$ no se anule si $M\ne0$?

[]{#MA-MSOL-ANM-01-013-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

$|g-M|<|M|/2$, que implica $|g|>|M|/2>0$.

El límite de $g$ entrega un radio para la tolerancia positiva $|M|/2$. En esa ventana, la triangular inversa da $|g(x)|\ge|M|-|g(x)-M|>|M|/2$. Así $g$ no sólo evita cero, sino que queda separado de él por una constante común. Esta barrera permite controlar errores de recíprocos y cocientes sin dejar crecer arbitrariamente el denominador invertido.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-013-046}

¿Cuál es el dominio correcto de $f/g$?

[]{#MA-MSOL-ANM-01-013-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

$D_0=\{x\in D:g(x)\ne0\}$. Si $M\ne0$, incluye toda una ventana perforada del dominio original.

El cociente sólo se evalúa donde el denominador es distinto de cero. Declarar $D_0$ hace visible esa condición. Si $M\ne0$, la barrera local anterior muestra que toda entrada del dominio original suficientemente próxima y distinta de $a$ pertenece a $D_0$. Como $a$ acumulaba esas entradas, también acumula el dominio del cociente. Los ceros lejanos pueden excluirse sin alterar la pregunta de límite local.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-013-047}

¿Qué sucede con el cociente si el límite del denominador es cero?

[]{#MA-MSOL-ANM-01-013-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

La regla no se aplica. Puede haber cancelación y límite finito, o puede faltar límite; hace falta otro argumento.

El dato $g\to0$ no proporciona la barrera inferior positiva usada en la regla. Por ejemplo, en entradas no nulas el cociente $x/x$ vale uno y tiene límite uno; en cambio $1/x$ no tiene límite real finito en cero. Ambos tienen denominador que tiende a cero y conclusiones diferentes. No se asigna significado a una división por el límite cero; se estudia el cociente en su dominio mediante otro control.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-013-048}

¿Necesita la regla de producto el criterio secuencial recíproco?

[]{#MA-MSOL-ANM-01-013-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

No. Se demostró directamente con radios, cota local e identidades algebraicas.

Las estimaciones del producto trabajan con una entrada arbitraria de una ventana perforada. Usan una identidad algebraica, acotación local y radios que hacen pequeños los errores. No seleccionan una sucesión de entradas ni convierten condiciones secuenciales en condiciones funcionales. Por tanto la prueba directa no hereda la hipótesis de elección numerable que se declaró en otro teorema. Mantener separadas las vías de prueba preserva su alcance fundacional.

</details>

### Ejercicios de la sección 13.6

#### Ejercicio 26. Cancelar antes de usar un cociente

[]{#MA-EX-ANM-01-013-026}

Calcula y prueba el límite en $2$ de $(x^2-4)/(x-2)$ en su dominio natural. ¿Por qué no se usa directamente la regla de cociente?

[]{#MA-SOL-ANM-01-013-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

El dominio es $\mathbb R\setminus\{2\}$. Allí la factorización da $(x^2-4)/(x-2)=x+2$, que tiene límite $4$: con $\delta=\varepsilon$ el error es $|x-2|<\varepsilon$. El límite del denominador es cero, por lo que el criterio de cocientes no se aplica. La cancelación es válida sólo fuera del punto excluido, exactamente el dominio pertinente.

</details>

#### Ejercicio 27. Un denominador con ceros lejanos

[]{#MA-EX-ANM-01-013-027}

Sean $f(x)=x+1$, $g(x)=x^2-4$. Prueba el límite de $f/g$ en cero y declara el dominio.

[]{#MA-SOL-ANM-01-013-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

El dominio es $D_0=\mathbb R\setminus\{-2,2\}$. Polinomios dan límites $1$ y $-4$ en cero; el segundo es no nulo. La regla de cocientes prueba límite $-1/4$. Los ceros lejanos no impiden una ventana local: para $|x|<1$, $|g(x)|=4-x^2>3$. No se afirma que el cociente esté definido en los puntos excluidos.

</details>

#### Ejercicio 28. Producto desde una identidad diferente

[]{#MA-EX-ANM-01-013-028}

Prueba la regla de producto utilizando $fg-LM=(f-L)(g-M)+L(g-M)+M(f-L)$ y un solo presupuesto para ambos errores.

[]{#MA-SOL-ANM-01-013-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Sea $A=1+|L|+|M|>0$. Dado $\varepsilon>0$, exigimos ambos errores menores que $t=\min(1,\varepsilon/A)$. En el mínimo de radios, $|(f-L)(g-M)|<t^2\le t$, y los otros términos están acotados por $|L|t$ y $|M|t$. Sumando con la estricta cota del primer término obtenemos error $<At\le\varepsilon$. Esta variante usa el pequeño tamaño del producto de errores en vez de una cota separada de $f$.

</details>

#### Ejercicio 29. Norma y diferencia de normas

[]{#MA-EX-ANM-01-013-029}

Si $f\to L$ y $g\to M$, prueba $\bigl||f|-|g|\bigr|\to\bigl||L|-|M|\bigr|$ y da un control directo del error con los dos errores originales.

[]{#MA-SOL-ANM-01-013-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

La triangular inversa aplicada primero a los dos reales $|f|-|g|$ y $|L|-|M|$ da error final $\le\bigl|(|f|-|g|)-(|L|-|M|)\bigr|$. La triangular y la inversa de nuevo lo acotan por $||f|-|L||+||g|-|M||\le|f-L|+|g-M|$. Pedimos cada error menor que $\varepsilon/2$ y reunimos radios. La cota prueba la conclusión directamente.

</details>

#### Ejercicio 30. Un producto converge sin límites de los factores

[]{#MA-EX-ANM-01-013-030}

Construye funciones $f,g$ sin límite en cero cuyo producto sí tenga límite. Prueba todas las afirmaciones.

[]{#MA-SOL-ANM-01-013-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Sea $f(x)=g(x)=s(x)$, el salto con valores $\pm1$. Las rutas positivas y negativas dan destinos distintos y refutan el límite de cada factor. Pero $f(x)g(x)=s(x)^2=1$ para toda entrada, así que el producto tiene límite $1$ con cualquier radio y error cero. La regla del producto es suficiente, no una condición necesaria para que el producto converja.

</details>
## 13.7. Cambiar las rutas disponibles

[]{#MA-SEC-ANM-01-013-007}

El dominio forma parte de la pregunta. Si retiramos entradas, retiramos posibles infractores. Un límite que vale en un dominio grande se conserva al restringirlo; un límite obtenido en un dominio pequeño puede dejar de valer al devolver entradas.

### Restricción y reunión finita

Si $A\subseteq D$, $a\in A'$ y $f\to L$ a través de $D$, el mismo radio controla $f|_A$. La acumulación de $A$ asegura que la nueva pregunta no sea vacía.

Más generalmente, sean $D_1,\ldots,D_k\subseteq D$, con $k\ge1$, $a\in D_i'$ para todos, y supongamos que existe $r>0$ con $U_D(a,r)\subseteq D_1\cup\cdots\cup D_k$. Si las restricciones tienen el mismo límite $L$, dado $\varepsilon$ tomamos un radio por cada una y el mínimo con $r$. Toda entrada de la ventana pertenece a alguna pieza y cumple su estimación. Así $f\to L$ en $D$. Es una reunión finita de radios positivos; una familia infinita no proporciona necesariamente un mínimo positivo.

### Lados disponibles, lados inexistentes

Definimos $D_-=D\cap(-\infty,a)$ y $D_+=D\cap(a,\infty)$. El límite por la izquierda es el límite de $f|_{D_-}$ en $a$, siempre que $a\in D_-'$; análogamente a la derecha. No asignamos un límite a un lado que no acumula entradas.

Cuando ambos lados acumulan, el límite en $D$ existe y es $L$ si y sólo si ambos límites laterales existen y son $L$. La ida es restricción; la vuelta usa la reunión finita, pues toda entrada perforada pertenece a un lado.

![C13-F06. El salto tiene destinos laterales −1 y 1 en el dominio real, por lo que no admite un destino común. Restringido a entradas positivas, tiene límite 1 en cero. El lado izquierdo ausente no recibe un límite por vacuidad.](../../assets/books/anm/C13/C13-F06.svg){#fig-anm-c13-f06 fig-alt="C13-F06. El salto tiene destinos laterales −1 y 1 en el dominio real, por lo que no admite un destino común. Restringido a entradas positivas, tiene límite 1 en cero. El lado izquierdo ausente no recibe un límite por vacuidad."}

Si sólo acumula $D_+$, existe un radio sin entradas de $D_-$: ésa es la negación de acumulación del lado izquierdo. En esa ventana el límite en $D$ equivale al de la derecha. Si $a\in D'$, al menos un lado acumula: si ninguno lo hiciera, el mínimo de sus radios sin entradas eliminaría toda ventana perforada, contradicción.

El salto $s$ tiene límites laterales $-1$ y $1$, y no tiene límite en el dominio real. Restringir a $(0,\infty)$ deja un límite perfectamente válido en cero, aunque cero no pertenezca al dominio.

### Un dominio denso puede ocultar todas las infracciones

Sea $d:\mathbb R\to\mathbb R$, con $d(x)=0$ si $x\in\mathbb Q$ y $d(x)=1$ en caso contrario; aquí $\mathbb Q$ significa su copia canónica en $\mathbb R$. La restricción racional tiene límite cero en cada punto de acumulación de ese dominio porque es constante.

En cero, la función completa no tiene límite. Las rutas $u_n=1/(n+1)$ y $v_n=\sqrt2/(n+1)$ convergen a cero, son no nulas, y sus valores son respectivamente $0$ y $1$. Cada $v_n$ es irracional: de ser racional, multiplicarlo por el entero no nulo $n+1$ haría racional a $\sqrt2$, contradiciendo C10. La dirección secuencial ya probada descarta un destino común.

Densidad garantiza entradas próximas; no garantiza que probar sólo en esas entradas describa una función arbitraria. Para rescatar tal inferencia harían falta hipótesis adicionales, que no estamos suponiendo.

### Antes de seguir

#### Microcontrol 49

[]{#MA-MIC-ANM-01-013-049}

¿Qué condición adicional se exige al restringir a $A\subseteq D$?

[]{#MA-MSOL-ANM-01-013-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

$a\in A'$. Garantiza una pregunta de límite no vacía en el dominio restringido.

Reducir el dominio reduce las rutas disponibles, pero puede eliminarlas todas cerca del centro. Si $A$ sólo contiene el centro como punto aislado, la fórmula perforada sería vacía. Exigir $a\in A'$ garantiza aproximaciones en el dominio restringido. Bajo esa condición, el mismo radio del límite original controla todas las entradas de $A$ que quedan en su ventana, porque también pertenecen a $D$.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-013-050}

¿Por qué sirve reunir finitos radios positivos mediante un mínimo?

[]{#MA-MSOL-ANM-01-013-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

Porque su mínimo sigue siendo positivo y garantiza simultáneamente todos los controles locales.

Para una cantidad finita de controles, cada radio es positivo y al menos uno de ellos es el menor. Ese menor sigue siendo positivo. Una entrada dentro de su ventana está dentro de todas las ventanas originales y satisface todos los controles simultáneamente. El argumento permite reunir acotación, coincidencia local, precisión y restricciones de dominio sin perder la existencia de una escala válida.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-013-051}

¿Un mínimo de infinitos radios positivos tiene que ser positivo?

[]{#MA-MSOL-ANM-01-013-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

No. Los radios $1/(n+1)$ son positivos y no tienen ninguna cota inferior positiva.

La familia $1,1/2,1/3,\ldots$ se acerca a cero: ante cualquier propuesta $r>0$, existe un índice con $1/(n+1)<r$. Por eso no hay un radio positivo que quede por debajo de todos. En esta familia ni siquiera existe un mínimo; su ínfimo es cero. La técnica de tomar mínimos finitos no se extiende automáticamente a infinitos controles, porque podría dejar una ventana sin radio positivo.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-013-052}

¿Cuándo está definido el límite por la izquierda bajo nuestra convención?

[]{#MA-MSOL-ANM-01-013-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Cuando $a$ es punto de acumulación de $D\cap(-\infty,a)$. No basta que el lado esté nombrado.

El límite izquierdo es el límite de la función restringida a las entradas menores que $a$. Para formularlo necesitamos entradas de ese lado arbitrariamente próximas al centro. Si el dominio es $[a,\infty)$, la parte izquierda está vacía y no acumula en $a$, aunque el límite derecho pueda tener sentido. Nombrar un lado no garantiza que existan aproximaciones desde él.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-013-053}

Si ambos lados acumulan, ¿qué permite reunirlos?

[]{#MA-MSOL-ANM-01-013-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Que ambos límites laterales sean el mismo $L$. Se usa el mínimo de sus radios y toda entrada perforada pertenece a uno de los lados.

Para una tolerancia, cada límite lateral entrega un radio que controla sus entradas. Tomamos el mínimo. Cualquier entrada distinta del centro es menor o mayor que él, así que cae en uno de los dos lados y cumple la misma estimación respecto de $L$. Si los destinos fueran diferentes, esta unión de controles hacia un único número no sería posible. La igualdad de destinos es lo que permite construir el límite conjunto.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-013-054}

Si un lado no acumula, ¿qué información local ofrece?

[]{#MA-MSOL-ANM-01-013-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Existe un radio positivo sin entradas de ese lado. En una ventana suficientemente pequeña sólo importa el otro lado.

Negar acumulación en un lado significa que existe un radio donde no hay entradas de ese lado distintas del centro. Reduciendo también al radio válido del otro lado, toda entrada pertinente pertenece a éste y queda controlada. No se necesita asignar un límite ficticio al lado ausente. El límite en el dominio completo puede quedar determinado por las rutas realmente disponibles, junto con la condición de acumulación del dominio.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-013-055}

¿Probar un límite en un subconjunto denso basta para una función arbitraria?

[]{#MA-MSOL-ANM-01-013-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

No. La función puede tener valores distintos en todas las entradas omitidas; el indicador racional de §13.7 es un contraejemplo.

La densidad asegura que existen muchas entradas del subconjunto cerca de cada punto, pero no impone ninguna relación entre sus valores y los de las entradas omitidas. El indicador de los racionales vale uno sobre los racionales y cero sobre los irracionales. Restringir a cada uno de esos conjuntos produce destinos diferentes, aunque ambos sean densos. Para una función arbitraria, una familia de rutas favorables no reemplaza el control de todas las entradas.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-013-056}

¿Por qué $\sqrt2/(n+1)$ es irracional para todo índice?

[]{#MA-MSOL-ANM-01-013-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

Si fuese racional, multiplicarlo por el entero positivo $n+1$ haría racional a $\sqrt2$, contradicción.

El denominador $n+1$ es un entero positivo, así que multiplicar un supuesto cociente racional por él conserva racionalidad. Eso produciría una expresión racional para $\sqrt2$, contradiciendo su irracionalidad ya demostrada. Además sus magnitudes tienden a cero, por lo que la fórmula proporciona una ruta de entradas irracionales próximas a cero sin una selección abstracta. La prueba valida cada término y la propiedad de aproximación.

</details>

### Ejercicios de la sección 13.7

#### Ejercicio 31. El único lado disponible

[]{#MA-EX-ANM-01-013-031}

Sea $D=\{0\}\cup(0,2)$ y $f(x)=x^2$ para $x>0$, $f(0)=9$. Prueba el límite en cero a través de $D$ y analiza los límites laterales.

[]{#MA-SOL-ANM-01-013-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

El lado derecho acumula y el izquierdo está vacío, por lo que no le asignamos límite. Para $\varepsilon>0$, $\delta=\min(1,\sqrt\varepsilon)$ hace que toda entrada perforada sea positiva y tenga $|f(x)|=x^2<\varepsilon$. El límite en $D$ es cero y coincide con el límite derecho; el valor central $9$ se excluye.

**Retorno visual.** Véase [C13-F06](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 32. Reunir piezas finitas

[]{#MA-EX-ANM-01-013-032}

Sea $D=D_1\cup D_2$, $a\in D_1^{\prime}\cap D_2^{\prime}$, y supón que las dos restricciones de $f$ tienen el mismo límite $L$. Prueba el límite en $D$ y la recíproca.

[]{#MA-SOL-ANM-01-013-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Para $\varepsilon>0$, tomamos radios $\delta_1,\delta_2$ válidos. Su mínimo es positivo. Toda entrada perforada de $D$ pertenece a una pieza y recibe el error menor que $\varepsilon$ de esa pieza, aunque pueda pertenecer a ambas. Luego hay límite en $D$. Si el límite vale en $D$, el mismo radio funciona en cada subconjunto; la acumulación supuesta permite formular ambos límites restringidos.

</details>

#### Ejercicio 33. Infinitas piezas no garantizan reunión

[]{#MA-EX-ANM-01-013-033}

Sea $D=(0,\infty)$ y $D_k=\{1/k\}\cup((0,\infty)\setminus\{1/j:j\in\mathbb N,\ j\ge1\})$ para $k\ge1$. Para $f(x)=1$ en los puntos $1/j$ y $f(x)=0$ en las demás entradas, prueba que cada restricción tiene límite cero y su unión no.

[]{#MA-SOL-ANM-01-013-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Cada $D_k$ acumula cero: para un radio $r>0$ existe un real positivo irracional menor que $r$, que no es un recíproco entero. Tal entrada puede obtenerse explícitamente como $\sqrt2/m$ con entero $m>\sqrt2/r$. Si $\delta=1/(2k)$, la ventana de $D_k$ excluye su único punto con valor uno, $1/k$, y el error es cero para toda tolerancia. La unión de las piezas es todo $D$: los no recíprocos están en todas y cada recíproco en su pieza. La ruta $x_n=1/(n+1)$ tiene imágenes uno; para cada radio hay tal entrada con error uno, así que el candidato cero falla en la unión. Además, la ruta $\sqrt2/(n+1)$ tiene imágenes cero y descarta cualquier límite junto a la primera.

</details>

#### Ejercicio 34. Una prueba densa puede omitir todo el problema

[]{#MA-EX-ANM-01-013-034}

Para el indicador de irracionales, prueba el límite restringido a los racionales en cero y refuta cualquier límite en el dominio real usando rutas explícitas.

[]{#MA-SOL-ANM-01-013-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

La restricción racional es constante cero y $\delta=1$ sirve para cualquier tolerancia; cero acumula racionales por los puntos $1/m$. En el dominio completo, $1/(n+1)$ y $\sqrt2/(n+1)$ son rutas no nulas tendiendo a cero. La segunda es irracional en cada índice, pues de lo contrario $\sqrt2$ sería racional. Las imágenes son constantes cero y uno. Un límite funcional daría el mismo límite a ambas rutas por la dirección directa, contradicción.

</details>

#### Ejercicio 35. Al menos un lado acumula

[]{#MA-EX-ANM-01-013-035}

Si $a\in D^{\prime}$, demuestra que acumula al menos uno de $D\cap(-\infty,a)$ y $D\cap(a,\infty)$. Si exactamente uno acumula, prueba que ese lado decide el límite completo.

[]{#MA-SOL-ANM-01-013-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Si ninguno acumulara, habría radios positivos $r_-,r_+$ sin entradas de cada lado en sus ventanas. En el mínimo no habría ninguna entrada distinta de $a$ del dominio, contradicción. Si sólo el derecho acumula, el izquierdo tiene un radio sin entradas. Todo control del límite derecho se reúne con ese radio y controla el dominio completo; la implicación inversa es restricción. El caso izquierdo es simétrico.

</details>
## 13.8. Componer controles sin perder la perforación

[]{#MA-SEC-ANM-01-013-008}

Transportar dos ventanas consecutivas parece inmediato: primero $f$ acerca $x$ a $b$; después $g$ acerca la salida a $L$. Pero el segundo límite controla entradas próximas a $b$ y distintas de $b$. La primera función puede enviar muchas entradas directamente a ese centro.

### Composición con evitación del centro intermedio

**Teorema.** Sean $f:D\to E$, con $D,E\subseteq\mathbb R$, $a\in D'$, $b\in E'$ y $g:E\to\mathbb R$. Supongamos $f\to b$ en $a$, $g\to L$ en $b$, y que existe $r>0$ con $f(x)\ne b$ para todo $x\in U_D(a,r)$. Entonces $g\circ f\to L$ en $a$.

**Mapa de la prueba.** El desafío final $\varepsilon$ determina un radio intermedio $\eta$ para $g$; ese radio es el desafío que presentamos a $f$. La evitación garantiza que el punto intermedio esté en la ventana perforada y no sólo en la ventana completa.

Fijemos $\varepsilon>0$. Para $g$ obtenemos $\eta>0$ tal que $y\in E$, $0<|y-b|<\eta$ implica $|g(y)-L|<\varepsilon$. Para $f$ obtenemos $\delta_f>0$ que asegura $|f(x)-b|<\eta$. Sea $\delta=\min(r,\delta_f)$. Para cualquier $x\in U_D(a,\delta)$, el tipo da $f(x)\in E$, la primera cota da distancia menor que $\eta$ y la evitación da distancia positiva. Podemos aplicar el segundo contrato: $|g(f(x))-L|<\varepsilon$. Así se reensamblan las dos metas.

### Una alternativa permite tocar el centro

Si $b\in E$ y $g(b)=L$, podemos retirar la evitación. Con el mismo radio de $f$, cada entrada produce uno de dos casos. Si $f(x)\ne b$, usamos el límite de $g$; si $f(x)=b$, el error final es $|g(b)-L|=0$. El argumento prueba la composición sin haber introducido aún el vocabulario de continuidad.

![C13-F07. La interior envía toda entrada a 0. La exterior tiene límite 0 en 0, pero g(0)=1; su contrato perforado no controla ese valor. La composición es constante 1. La cercanía intermedia necesita además evitación del centro o un valor central compatible.](../../assets/books/anm/C13/C13-F07.svg){#fig-anm-c13-f07 fig-alt="C13-F07. La interior envía toda entrada a 0. La exterior tiene límite 0 en 0, pero g(0)=1; su contrato perforado no controla ese valor. La composición es constante 1. La cercanía intermedia necesita además evitación del centro o un valor central compatible."}

La alternativa es necesaria para ese mecanismo. Sea $f(x)=0$ en todo $\mathbb R$ y $g(y)=0$ si $y\ne0$, $g(0)=1$. Tenemos $f\to0$ en cero y $g\to0$ en cero, pero $(g\circ f)(x)=1$ para toda entrada, cuyo límite es $1$, no $0$. No falló la cercanía: falló la autorización para aplicar un contrato perforado en su centro.

### Un certificado que se puede reutilizar

Supongamos que $|f(x)-b|\le C|x-a|$ cerca de $a$, con $C>0$, y que para cada $\varepsilon>0$ tenemos un radio válido $\eta_g(\varepsilon)$ para $g$. Si se cumple la evitación o la alternativa $g(b)=L$, sirve

$$
\delta(\varepsilon)=\min\left(r,\frac{\eta_g(\varepsilon)}{C}\right),
$$

donde $r$ reúne las restricciones locales. Para $x$ dentro de ese radio, $|f(x)-b|<\eta_g(\varepsilon)$, y el argumento anterior decide el caso central. Si $C=0$, la cota fuerza $f(x)=b$ localmente; sólo la alternativa central permite esta prueba y el resultado es inmediato.

Una prueba de límite consta de dos piezas: un procedimiento para producir radios y una verificación universal en el dominio. Un gráfico propone el mecanismo; una tabla ensaya casos; una sucesión puede detectar una infracción. La desigualdad o el argumento universal es lo que certifica toda la ventana.

Este capítulo ha separado cercanía, evaluación central y rutas disponibles. En el siguiente preguntaremos qué cambia al exigir que el destino sea precisamente el valor de la función en el centro.

### Antes de seguir

#### Microcontrol 57

[]{#MA-MIC-ANM-01-013-057}

¿Qué desafío se presenta a $f$ después de fijar $\varepsilon$ para $g\circ f$?

[]{#MA-MSOL-ANM-01-013-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

El radio intermedio $\eta$ que entrega el límite de $g$ para esa tolerancia final.

El límite exterior convierte el desafío final $\varepsilon$ en una escala intermedia $\eta$ alrededor de $b$. A continuación pedimos al límite interior que haga $f(x)$ suficientemente cercano a $b$ para entrar en esa escala. El radio final es el que responde a este segundo desafío, combinado con las restricciones locales. La composición encadena dos controles y su orden de diseño va desde la precisión final hacia la entrada inicial.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-013-058}

¿Qué dato falta si sólo sabemos $|f(x)-b|<\eta$?

[]{#MA-MSOL-ANM-01-013-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

Que $f(x)\ne b$, si vamos a usar el límite perforado de $g$. La cercanía sola permite alcanzar el centro.

El control del límite exterior se aplica a entradas con $0<|y-b|<\eta$. La estimación $|f(x)-b|<\eta$ sólo da la desigualdad superior y permite que la magnitud sea cero. Si la salida interior alcanza $b$, estaríamos evaluando $g(b)$, que el límite perforado de $g$ no controla. Por eso hace falta evitar localmente ese centro o verificar por separado que su valor exterior sea el destino correcto.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-013-059}

¿Qué alternativa permite que $f(x)=b$?

[]{#MA-MSOL-ANM-01-013-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Que $b\in E$ y $g(b)=L$. En ese caso la salida central tiene error exactamente cero.

Si la salida interior alcanza $b$ y $g(b)=L$, la composición entrega exactamente $L$ y tiene error cero. Si no alcanza $b$, se aplica el control perforado exterior. Separar ambos casos permite cubrir toda la ventana de entradas. También hay que tener $b$ en el dominio de $g$ para usar su evaluación. La condición sobre el valor central resuelve el caso que la desigualdad perforada dejaba fuera.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-013-060}

¿Qué falla en la composición de una función cero con $g(0)=1$, $g(y)=0$ fuera de cero?

[]{#MA-MSOL-ANM-01-013-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

La interior cae siempre en el centro. Aunque ambos límites aislados son cero, la composición es constante uno.

La función interior $f(x)=0$ tiene límite cero, y la exterior dada tiene límite perforado cero en cero porque vale cero en todas las entradas no centrales. Pero cada composición evalúa precisamente el centro exterior, donde $g(0)=1$. Por eso $g(f(x))=1$ en toda entrada y su límite es uno. El ejemplo refuta la aplicación de una regla de composición que ignore la perforación y el valor central.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-013-061}

¿Qué papel desempeña el tipo $f:D\to E$?

[]{#MA-MSOL-ANM-01-013-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

Garantiza que $g(f(x))$ esté definido. Una regla algebraica sin pertenencia al dominio de $g$ no basta.

Si el dominio exterior de $g$ es $E$, el tipo $f:D\to E$ asegura que cada salida intermedia pertenece a ese dominio. La cercanía a $b$ no bastaría: una salida muy próxima podría seguir siendo una entrada no admitida. Primero verificamos que la composición pueda evaluarse en las entradas pertinentes y después diseñamos las estimaciones de límite. Un certificado numérico no reemplaza la comprobación del dominio.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-013-062}

Con $|f(x)-b|\le C|x-a|$, $C>0$, ¿qué radio de precisión sirve?

[]{#MA-MSOL-ANM-01-013-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

$\eta_g(\varepsilon)/C$, combinado por mínimo con las restricciones locales. La desigualdad estricta de entrada produce error intermedio menor que $\eta_g(\varepsilon)$.

La cota interior entrega $|f(x)-b|\le C|x-a|$. Elegir $\delta\le\eta_g(\varepsilon)/C$ hace que la desigualdad estricta $|x-a|<\delta$ produzca $|f(x)-b|<\eta_g(\varepsilon)$. El mínimo con radios auxiliares asegura la validez de la cota y la condición de evitación o del valor central. Se debe conservar ese último requisito: la cota superior de distancias no prueba por sí sola que la salida interior evite $b$.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-013-063}

Si $C=0$ en esa cota, ¿qué ocurre localmente?

[]{#MA-MSOL-ANM-01-013-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

$f(x)=b$. El mecanismo de composición necesita $g(b)=L$; la evitación es incompatible con la ventana no vacía.

La cota $|f(x)-b|\le0$ fuerza igualdad con $b$ en toda la ventana donde vale. Si esas entradas son no vacías por acumulación, no pueden además satisfacer $f(x)\ne b$. La vía de evitación queda descartada. La composición local evalúa siempre $g(b)$ y sólo obtiene el destino propuesto si ese valor es $L$. Este caso se estudia directamente y no se divide por $C$.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-013-064}

¿Qué verifica finalmente un certificado de límite?

[]{#MA-MSOL-ANM-01-013-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Que el radio sea positivo y dependa sólo de datos permitidos, y que todas las entradas del dominio en su ventana perforada satisfagan el error de salida.

Después de proponer el radio debemos comprobar que sea positivo para cada tolerancia positiva y que se elija antes de la entrada arbitraria. Luego tomamos cualquier $x\in D$ con $0<|x-a|<\delta$ y derivamos el error estricto. El argumento debe verificar también las condiciones de dominio y cualquier denominador usado. La acumulación garantiza que no se trate de ventanas vacías. Una fórmula para $\delta$ sin esta comprobación universal todavía no completa la prueba.

</details>

### Ejercicios de la sección 13.8

#### Ejercicio 36. La composición pierde el centro perforado

[]{#MA-EX-ANM-01-013-036}

Construye $f,g:\mathbb R\to\mathbb R$ con $\lim_{x\to0}f(x)=0$ y $\lim_{y\to0}g(y)=0$ pero $\lim_{x\to0}g(f(x))=2$. Explica la falla del argumento usual.

[]{#MA-SOL-ANM-01-013-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Tomamos $f(x)=0$ para todos los reales; $g(y)=0$ si $y\ne0$ y $g(0)=2$. Los dos límites son cero porque sus errores son cero en las ventanas pertinentes. La composición es constante dos y tiene límite dos. El límite perforado de $g$ sólo controla entradas distintas de cero; la interior cae siempre en cero.

**Retorno visual.** Véase [C13-F07](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 37. Componer dos cuadrados con certificados

[]{#MA-EX-ANM-01-013-037}

Prueba directamente mediante radios anidados que $x^4\to1$ en $1$, usando el certificado del cuadrado y la alternativa central para la segunda etapa.

[]{#MA-SOL-ANM-01-013-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Para $g(y)=y^2$ en $b=1$, el radio $\eta=\min(1,\varepsilon/3)$ es válido y $g(1)=1$. Para $f(x)=x^2$ en $1$, tomamos $\delta=\min(1,\eta/3)$. Entonces $|f(x)-1|<\eta$. Si $f(x)\ne1$ aplica el control de $g$; si $f(x)=1$, el error final es cero. El tipo real de ambas funciones permite componerlas. Así $|x^4-1|<\varepsilon$ en toda la ventana.

</details>

#### Ejercicio 38. La alternativa central sin límites conocidos

[]{#MA-EX-ANM-01-013-038}

Sean $f:D\to E$, $g:E\to\mathbb R$, $a\in D^{\prime}$. Supón que $f(x)=b\in E$ en alguna ventana perforada. Determina y prueba el límite de la composición sin suponer que exista un límite de $g$ en $b$.

[]{#MA-SOL-ANM-01-013-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

En esa misma ventana la composición tiene valor constante $g(b)$. Para cualquier $\varepsilon>0$ usamos su radio $r$ y el error es cero. Por tanto el límite es $g(b)$. No importa el comportamiento de $g$ fuera de la salida única localmente alcanzada; las hipótesis del teorema general de composición eran suficientes, no necesarias.

</details>

#### Ejercicio 39. Composición a través de un subconjunto de salidas

[]{#MA-EX-ANM-01-013-039}

Sean $f:D\to E$, $a\in D^{\prime}$, $b\in A^{\prime}$ para $A\subseteq E$, y $g:E\to\mathbb R$. Supón $f\to b$, $g|_A\to L$ y que $f(x)\in A\setminus\{b\}$ cerca de $a$. Prueba el límite de $g\circ f$ aunque $g$ no tenga límite en todo $E$.

[]{#MA-SOL-ANM-01-013-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Fijado $\varepsilon>0$, el contrato de $g|_A$ ofrece $\eta>0$ para entradas de $A$ próximas y distintas de $b$. El límite de $f$ ofrece $\delta_f>0$ para ese radio. Reunimos $\delta_f$ con el radio $r$ de pertenencia y evitación. Para toda entrada de la nueva ventana, $f(x)\in A\setminus\{b\}$ y $|f(x)-b|<\eta$, de modo que $|g(f(x))-L|<\varepsilon$. El segundo contrato sólo se necesita en las salidas realmente disponibles.

</details>

#### Ejercicio 40. Un criterio exacto para tocar una salida defectuosa

[]{#MA-EX-ANM-01-013-040}

Sean $f:D\to E$, $a\in D^{\prime}$, $b\in E\cap E^{\prime}$, $g:E\to\mathbb R$, $f\to b$ y $g\to L$ en $b$, con $g(b)\ne L$. Prueba que $g\circ f\to L$ si y sólo si $f(x)\ne b$ en alguna ventana perforada de $a$.

[]{#MA-SOL-ANM-01-013-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La evitación es suficiente por el teorema del texto. Para probar necesidad, supongamos que la composición tiende a $L$ y sea $d=|g(b)-L|>0$. Su contrato para $\varepsilon=d/2$ da $\delta>0$ con error menor que $d/2$ en la ventana. Si alguna entrada allí tuviera $f(x)=b$, el error final sería $d$, contradicción. Luego todas evitan $b$. El defecto central convierte una condición suficiente en una condición necesaria para ese destino particular.

**Retorno visual.** Véase [C13-F07](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html#fig-anm-c13-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-13)

[← Capítulo 12](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html) · [Capítulo 14 →](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html)
