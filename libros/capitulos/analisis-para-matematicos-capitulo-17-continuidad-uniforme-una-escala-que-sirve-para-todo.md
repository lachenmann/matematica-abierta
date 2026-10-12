---
content-id: MA-BCH-0270
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-017
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
title: 'Capítulo 17 — Continuidad uniforme: una escala que sirve para todo'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C17.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-17)

Una función continua puede exigir radios de entrada cada vez menores al cambiar el centro. La continuidad uniforme pregunta si, para cada precisión de salida, una sola escala protege todos los pares del dominio. Aquí demostraremos cómo la compacidad produce esa escala y qué puede hacerse con ella.

Los prerrequisitos centrales son continuidad de C14 y compacidad de C16. Supremo e ínfimo de C00, adherencia de C04, sucesiones de C06, Cauchy y raíces de C10 y tipos de C12 son interfaces heredadas. La prueba de Heine–Cantor usa una cubierta de todos los pares centro-radio admisibles y finitud, sin seleccionar radios por todos los puntos ni fabricar rutas. Las recíprocas secuenciales se declaran condicionales a CC(R) o a una enumeración dada. La extensión al cierre se construye por cortes de imágenes locales y la aproximación poligonal por una malla finita. No usamos derivadas, integrales ni teoría de límites uniformes de funciones.

## 17.1. Un radio antes de conocer los dos puntos

[]{#MA-SEC-ANM-01-017-001}

La continuidad de C14 permite que el radio de entrada dependa del centro. Si queremos controlar una función en todo su dominio, debemos preguntar si una sola escala puede servir para todos los centros a la vez. Esa pregunta depende de la función **y del dominio**.

**Definición.** Para $f:D\to\mathbb R$, la continuidad uniforme en $D$ significa

$$\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in D:
|x-y|<\delta\Longrightarrow|f(x)-f(y)|<\varepsilon.$$

La función y el dominio ya están fijados. El radio puede depender de ellos y de $\varepsilon$, pero se fija antes de conocer $x,y$. En la continuidad puntual el orden es $\forall a\in D\;\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D$: conocer $a$ antes permite un radio dependiente del centro. Uniformidad implica continuidad puntual por usar el mismo radio en cada centro; también se hereda por restricción a cualquier subconjunto. En el dominio vacío ambas propiedades son vacías: $\delta=1$ sirve para cualquier tolerancia.

**Negación.** Fallar la uniformidad significa que existe **una** tolerancia $\varepsilon_0>0$ tal que, para **todo** $\delta>0$, hay $x,y\in D$ con

$$|x-y|<\delta,\qquad |f(x)-f(y)|\ge\varepsilon_0.$$

El error de salida permanece separado de cero mientras la distancia de entrada puede hacerse arbitrariamente pequeña. Un radio propuesto que dependa del centro no demuestra este fallo: podría existir otro radio común que la prueba no haya encontrado.

**R1. Controles algebraicos.** Si $|f(x)-f(y)|\le L|x-y|$ en todo $D$, con una constante $L\ge0$, llamamos a $f$ Lipschitz. Cuando $L>0$, $\delta=\varepsilon/L$ da uniformidad; cuando $L=0$, todas las diferencias son cero y sirve cualquier radio positivo. Por ejemplo, $f(x)=ax+b$ en $\mathbb R$ tiene constante $|a|$. El valor absoluto tiene constante uno por la desigualdad triangular inversa.

Para $q(x)=x^2$ en $[-M,M]$, $M>0$,

$$|q(x)-q(y)|=|x-y||x+y|\le2M|x-y|.$$

Por tanto un radio uniforme es $\varepsilon/(2M)$. En cambio, sobre toda la recta fijamos $\varepsilon_0=1$. Dado $\delta>0$, tomamos $h=\min(\delta/2,1)>0$, $x=1/h$ y $y=x+h$. Entonces $h<\delta$ y

$$y^2-x^2=h(2x+h)=2+h^2>1.$$

Estos testigos refutan todo candidato a radio común. La continuidad puntual del cuadrado sigue siendo válida por C14.

![En \[−1,1\], la identidad de diferencia de cuadrados da radio 1/2 para tolerancia 1. En la recta, el par 4 y 17/4 tiene distancia 1/4 y error 33/16, y refuta ese candidato. La prueba general de R1/E002 produce testigos para todo radio: un solo gráfico no refuta todos los candidatos.](../../assets/books/anm/C17/C17-F01.svg){#fig-anm-c17-f01 fig-alt="En \[−1,1\], la identidad de diferencia de cuadrados da radio 1/2 para tolerancia 1. En la recta, el par 4 y 17/4 tiene distancia 1/4 y error 33/16, y refuta ese candidato. La prueba general de R1/E002 produce testigos para todo radio: un solo gráfico no refuta todos los candidatos."}

La raíz cuadrada muestra que uniformidad no exige una constante Lipschitz. Para $x\ge y\ge0$, escribimos $a=\sqrt{x}$, $b=\sqrt{y}$; como $a\ge b$,

$$(a-b)^2\le(a-b)(a+b)=x-y.$$

Así $|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}$ en $[0,\infty)$, y $\delta=\varepsilon^2$ asegura uniformidad. En $[0,1]$ no es Lipschitz: si hubiera una constante $L>0$, con $y=0$ se exigiría $1/\sqrt{x}\le L$ para todo $x>0$. Tomar $x=1/(n+1)^2$ con $n+1>L$ contradice esa cota. $L=0$ tampoco sirve, porque la función no es constante. Raíces y sus reglas de orden/algebra son interfaces de C10, no resultados diferenciales.

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-017-001}

¿Qué debe quedar fijado antes de conocer $x,y$ en continuidad uniforme?

[]{#MA-MSOL-ANM-01-017-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Para cada tolerancia $\varepsilon>0$, un solo $\delta>0$ que sirva para todos los pares del dominio fijado.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-017-002}

¿Qué dependencia adicional admite la continuidad puntual?

[]{#MA-MSOL-ANM-01-017-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

El radio se elige después del centro $a$, y puede depender de él además de la tolerancia, función y dominio.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-017-003}

¿Por qué la uniformidad implica continuidad en cada punto?

[]{#MA-MSOL-ANM-01-017-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

Se fija el centro como uno de los dos argumentos y se conserva el mismo radio uniforme para todos los otros puntos del dominio.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-017-004}

¿Qué tolerancia se mantiene fija al negar uniformidad?

[]{#MA-MSOL-ANM-01-017-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

Una $\varepsilon_0>0$ para la que todo radio positivo admite un par de entradas próximas con diferencia de salida al menos $\varepsilon_0$.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-017-005}

¿Un radio local dependiente del centro prueba falta de uniformidad?

[]{#MA-MSOL-ANM-01-017-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

No. Es una solución local, no una prueba de que todo candidato común falla. Hay que producir testigos para cada $\delta>0$.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-017-006}

¿Qué radio sirve para una constante Lipschitz $L>0$?

[]{#MA-MSOL-ANM-01-017-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

$\delta=\varepsilon/L$; la desigualdad $|f(x)-f(y)|\le L|x-y|$ convierte distancia estrictamente menor que ese radio en error menor que $\varepsilon$.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-017-007}

¿Por qué la raíz puede ser uniforme sin ser Lipschitz?

[]{#MA-MSOL-ANM-01-017-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Su control es $|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}$, que da radio $\varepsilon^2$. En cero, los cocientes $1/\sqrt{x}$ no están acotados.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-017-008}

¿Qué ocurre con el dominio vacío?

[]{#MA-MSOL-ANM-01-017-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

La condición sobre pares es vacía y cualquier radio positivo sirve; no hay puntos que exigir controlar.

</details>

### Ejercicios de la sección 17.1

[]{#ejercicios-17}

#### Ejercicio 1. El orden de los cuantificadores

[]{#MA-EX-ANM-01-017-001}

Escribe continuidad puntual, uniformidad y negación de uniformidad para $f:D\to\mathbb R$. Explica qué variables puede conocer cada radio y trata el vacío.

[]{#MA-SOL-ANM-01-017-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Puntual: $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$, distancia menor que $\delta$ implica error respecto de $a$ menor que $\varepsilon$. Uniforme: $\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in D$ con la implicación de R1. En la primera el radio puede depender del centro; en la segunda se fija antes de los dos puntos. Negación: existe $\varepsilon_0>0$ tal que todo $\delta>0$ admite un par con distancia menor que $\delta$ y error al menos $\varepsilon_0$. Función y dominio están fijados en los tres casos. En el vacío la uniformidad es vacía y su negación es falsa, porque no existen pares.

</details>

#### Ejercicio 2. Un radio dependiente no refuta otro posible

[]{#MA-EX-ANM-01-017-002}

Una prueba de continuidad de $x^2$ produce radios dependientes del centro y concluye que no hay radio uniforme. Diagnostica el fallo y prueba la conclusión correcta en $\mathbb R$ con testigos para cada radio. Contrasta $[-M,M]$.

[]{#MA-SOL-ANM-01-017-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Que una construcción dependa del centro no excluye otras construcciones independientes. Para refutar uniformidad fijamos $\varepsilon_0=1$; dado $\delta>0$, sea $h=\min(\delta/2,1)>0$, $x=1/h$, $y=x+h$. Si $\delta\le2$, $h=\delta/2<\delta$; si $\delta>2$, $h=1<\delta$. El error es $h(2/h+h)=2+h^2>1$. Estos testigos sí refutan todo radio común. En $[-M,M]$, $M>0$, $|x^2-y^2|\le2M|x-y|$ y $\delta=\varepsilon/(2M)$ da uniformidad. Para $M=0$ el dominio es singleton y cualquier radio sirve.

**Retorno visual.** Véase [C17-F01](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 3. Una escala no lineal

[]{#MA-EX-ANM-01-017-003}

Prueba uniformidad de $\sqrt{x}$ en $[0,\infty)$ sin derivadas y refuta que sea Lipschitz en $[0,1]$.

[]{#MA-SOL-ANM-01-017-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Para $x\ge y\ge0$, con $a=\sqrt{x}\ge b=\sqrt{y}$, $(a-b)^2\le(a-b)(a+b)=x-y$. Intercambiar los argumentos cubre el otro orden, así la diferencia de raíces es a lo sumo la raíz de la distancia. $\delta=\varepsilon^2$ sirve en todo el dominio. Si una constante $L>0$ diera control Lipschitz en $[0,1]$, tomar $x=1/(n+1)^2$, $y=0$ exigiría $1/(n+1)\le L/(n+1)^2$, es decir $n+1\le L$, falso para un índice grande. $L=0$ falla entre cero y uno.

</details>

#### Ejercicio 4. Restricción y regreso imposible

[]{#MA-EX-ANM-01-017-004}

Prueba que uniformidad se hereda por restricción. Da una función cuya restricción a un subconjunto sea uniforme aunque ella no sea uniforme en el dominio mayor.

[]{#MA-SOL-ANM-01-017-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

El mismo radio uniforme sirve para todos los pares del subconjunto, porque también son pares del dominio original. La recíproca falla: $x^2$ en $\mathbb R$ no es uniforme por E002, pero en $[0,1]$ tiene constante Lipschitz dos. Incluso la restricción a un singleton sería uniforme sin informar sobre el resto.

</details>

#### Ejercicio 5. Uniformidad sin compacidad ni acotación

[]{#MA-EX-ANM-01-017-005}

Para $f(x)=3x-2$ en $\mathbb R$, da un radio uniforme y determina si la imagen y el dominio son acotados o compactos. ¿Refuta Heine–Cantor?

[]{#MA-SOL-ANM-01-017-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

La diferencia de salidas es $3|x-y|$, por lo que $\delta=\varepsilon/3$ sirve. El dominio es toda la recta, no acotado ni compacto por C16. La imagen también es toda la recta: $y$ tiene entrada $(y+2)/3$, así tampoco es acotada ni compacta. No refuta Heine–Cantor: éste da compacidad como condición suficiente, no necesaria para una función particular.

</details>
## 17.2. Una cubierta y una escala de protección

[]{#MA-SEC-ANM-01-017-002}

Una subcubierta finita contiene todos los puntos del compacto, pero necesitaremos algo más: un margen que asegure que una vecindad de cada punto queda dentro de un miembro de la cubierta original. No basta tomar los radios de bolas que cubren si no hemos reservado espacio para mover el centro.

**R2. Número de Lebesgue para una cubierta dada.** Sea $K\subseteq\mathbb R$ compacto y $(U_i)_{i\in I}$ una cubierta por abiertos reales. Existe $\lambda>0$ tal que

$$\forall z\in K\;\exists i\in I:\quad
K\cap(z-\lambda,z+\lambda)\subseteq U_i.$$

No se afirma una función que elija el índice para cada $z$. Para $K=\varnothing$ sirve $\lambda=1$, incluso si $I=\varnothing$. Supongamos $K$ no vacío.

Construimos **todos** los triples admisibles

$$T=\{(a,i,r)\in K\times I\times\mathbb R_{>0}:
(a-2r,a+2r)\subseteq U_i\}.$$

La regla $t=(a,i,r)\mapsto B(a,r)$, donde $B(a,r)=(a-r,a+r)$, determina una familia de abiertos reales. Cubre $K$: para un $a$ fijado la cubierta da algún $i$ con $a\in U_i$ y la apertura da $\rho>0$ con $B(a,\rho)\subseteq U_i$; $r=\rho/2$ hace admisible el triple y $a\in B(a,r)$. Ésta es una verificación de cobertura, sin seleccionar un triple para cada punto.

Compacidad entrega $J\subseteq T$ finito cuyas bolas pequeñas cubren $K$. No puede ser vacío. Por C16, el conjunto finito de sus radios positivos tiene mínimo positivo; definimos

$$\lambda=\min\{r:(a,i,r)\in J\}>0.$$

Para $z\in K$ hay un triple $(a,i,r)\in J$ con $|z-a|<r$. Si $w\in B(z,\lambda)$, entonces

$$|w-a|\le|w-z|+|z-a|<\lambda+r\le2r.$$

Por ello $B(z,\lambda)\subseteq B(a,2r)\subseteq U_i$. Hemos obtenido incluso la inclusión de la bola ambiental completa, que implica la inclusión relativa del enunciado. El índice se fija para este $z$ después de fijar $\lambda$.

![Para K=\[0,1\] y los dos abiertos indicados, λ=1/10 sirve: se usa U1 si z≤1/2 y U2 si z>1/2. Los tres centros dibujados son ilustrativos. λ=1/5 falla en el centro 1/2, porque su bola relativa contiene 2/5 y 3/5, y ningún miembro contiene ambos. Extremos de la bola se interpretan por desigualdades estrictas del texto.](../../assets/books/anm/C17/C17-F02.svg){#fig-anm-c17-f02 fig-alt="Para K=\[0,1\] y los dos abiertos indicados, λ=1/10 sirve: se usa U1 si z≤1/2 y U2 si z&gt;1/2. Los tres centros dibujados son ilustrativos. λ=1/5 falla en el centro 1/2, porque su bola relativa contiene 2/5 y 3/5, y ningún miembro contiene ambos. Extremos de la bola se interpretan por desigualdades estrictas del texto."}

La familia de todos los triples admisibles reemplaza una elección simultánea de radios. La duplicación de radios reserva margen; la finitud permite convertirlo en una escala positiva común. No tomamos el ínfimo de infinitos radios positivos, que podría ser cero.

Por ejemplo, en $K=[0,1]$ la cubierta $U_1=(-1,3/5)$ y $U_2=(2/5,2)$ admite $\lambda=1/10$ para la inclusión relativa. Si $z\le1/2$, todo $w\in K$ con $|w-z|<1/10$ satisface $w<3/5$ y entra en $U_1$. Si $z>1/2$, satisface $w>2/5$ y entra en $U_2$. La desigualdad estricta protege también el caso $z=1/2$.

Una cubierta de un dominio no compacto no garantiza este margen. En $D=(0,1)$, los abiertos $U_n=(1/(n+2),2)$ forman una cubierta sin subcubierta finita, según C16. Tampoco tienen número de Lebesgue positivo: para todo $z\in D$, cualquier bola relativa que alcance arbitrariamente cerca de cero omite estar contenida en un único $U_n$. Dado $\lambda>0$, basta tomar $0<z<\min(\lambda,1)$; su bola relativa contiene puntos positivos por debajo de cada umbral.

Si una cubierta se da por abiertos **relativos** $A_i$ de un compacto $K$, C16 proporciona el levantamiento canónico $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real, con $K\cap W_i=A_i$. Aplicar R2 a $W$ da la misma conclusión relativa para $A$. No se elige una familia de ambientes.

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-017-009}

¿Qué expresa un número de Lebesgue para una cubierta de $K$?

[]{#MA-MSOL-ANM-01-017-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

Una escala $\lambda>0$ tal que, para cada $z\in K$, algún miembro de la cubierta contiene toda la bola relativa $K\cap B(z,\lambda)$.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-017-010}

¿Por qué se reúnen todos los triples admisibles?

[]{#MA-MSOL-ANM-01-017-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

La familia queda determinada por una fórmula; la existencia local de un triple no se convierte en una elección simultánea por punto.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-017-011}

¿Con qué bolas se cubre y en cuáles se reserva protección?

[]{#MA-MSOL-ANM-01-017-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Las bolas $B(a,r)$ cubren; las dobles $B(a,2r)$ están contenidas en los abiertos originales.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-017-012}

¿Qué ocurre antes de tomar el mínimo de radios?

[]{#MA-MSOL-ANM-01-017-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Compacidad produce un conjunto finito no vacío de triples cuyas bolas cubren $K$. Sólo sus radios concretos forman el mínimo positivo.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-017-013}

¿Qué desigualdad mueve la protección desde $a$ hasta $z$?

[]{#MA-MSOL-ANM-01-017-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Si $|z-a|<r$ y $|w-z|<\lambda\le r$, entonces $|w-a|<\lambda+r\le2r$.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-017-014}

¿Se elige un abierto para todos los centros simultáneamente?

[]{#MA-MSOL-ANM-01-017-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

No. La escala es global, pero para un centro $z$ fijado basta el índice de uno de los triples de la lista que lo cubre.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-017-015}

¿Cómo se tratan cubiertas por abiertos relativos?

[]{#MA-MSOL-ANM-01-017-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

Con $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real por C16 y con $K\cap W_i=A_i$; se aplica R2 al levantamiento canónico.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-017-016}

¿Qué número sirve para el compacto vacío?

[]{#MA-MSOL-ANM-01-017-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

$\lambda=1$, porque no hay centros que verificar, incluso si la familia de índices es vacía.

</details>

### Ejercicios de la sección 17.2

#### Ejercicio 6. Proteger una cubierta concreta

[]{#MA-EX-ANM-01-017-006}

Para $K=[0,1]$, $U_1=(-1,3/5)$ y $U_2=(2/5,2)$, verifica que $\lambda=1/10$ es número de Lebesgue relativo. ¿Sirve $\lambda=1/5$?

[]{#MA-SOL-ANM-01-017-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Para $z\le1/2$, $w\in K$ a distancia menor que $1/10$ satisface $w<z+1/10\le3/5$, y como $w\ge0>-1$ pertenece a $U_1$. Si $z>1/2$, $w>z-1/10>2/5$ y $w\le1<2$, luego está en $U_2$. Para $\lambda=1/5$, el centro $z=1/2$ tiene bola relativa que contiene $3/5$ y $2/5$. El primero no está en $U_1$ y el segundo no está en $U_2$; ningún miembro contiene la bola. Así ese radio falla.

**Retorno visual.** Véase [C17-F02](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 7. Familia de todos los triples

[]{#MA-EX-ANM-01-017-007}

Reconstruye R2 mostrando por qué $T$ determina una familia abierta y cubre $K$ sin escoger un triple para cada punto.

[]{#MA-SOL-ANM-01-017-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

$T$ contiene exactamente los triples $(a,i,r)$ con $a\in K$, $i\in I$, $r>0$ y $B(a,2r)\subseteq U_i$. Cada triple tiene componentes únicas y determina el abierto $B(a,r)$; esto es una regla funcional, no una elección entre radios. Para un $a$ arbitrario, cobertura da un $i$ y apertura un $\rho>0$; el triple $(a,i,\rho/2)$ pertenece a $T$ y su bola contiene $a$. La prueba establece cobertura punto por punto, sin definir un mapa de triples elegidos por centro.

</details>

#### Ejercicio 8. Tomar un ínfimo demasiado pronto

[]{#MA-EX-ANM-01-017-008}

Un argumento toma el ínfimo de todos los radios locales positivos y lo declara positivo. Repara la prueba de R2 y explica el papel de la bola doble.

[]{#MA-SOL-ANM-01-017-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Positividad de todos los miembros no da ínfimo positivo: los recíprocos $1/(n+1)$ tienen ínfimo cero. Primero se aplica compacidad a las bolas pequeñas de todos los triples admisibles, obteniendo una lista finita no vacía $J$. El mínimo de sus radios es positivo por ser uno de los miembros. Si $z$ está a distancia menor que $r$ de un centro de la lista y $|w-z|<\lambda\le r$, entonces $|w-a|<2r$. La bola doble contenida en el abierto original reserva justamente ese margen; cobertura por bolas pequeñas sola no demuestra dicha inclusión.

</details>

#### Ejercicio 9. Levantar sin elegir ambientes

[]{#MA-EX-ANM-01-017-009}

Una cubierta de compacto se da por abiertos relativos $(A_i)$. Explica cómo obtener su número de Lebesgue sin elegir simultáneamente abiertos ambientales que representen cada $A_i$.

[]{#MA-SOL-ANM-01-017-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

C16 prueba que $W_i=(\mathbb R\setminus K)\cup A_i$ es abierto real y que $K\cap W_i=A_i$. La regla determina toda la familia por fórmula, y ésta cubre $K$. R2 da $\lambda>0$ para $W$. Para cada $z\in K$, algún $W_i$ contiene la bola relativa; al intersectar con $K$ se obtiene inclusión en $A_i$. No se seleccionó una familia de representantes ambientales. El vacío se resuelve con $\lambda=1$.

</details>

#### Ejercicio 10. Una cubierta finita sin margen

[]{#MA-EX-ANM-01-017-010}

Sea $D=\{p_n=1/(n+1):n\ge0\}$. Pon $r_n=1/[4(n+1)(n+2)]$ y divide las bolas $B(p_n,r_n)$ en dos abiertos, según paridad de $n$. Prueba que cubren $D$ y que esa cubierta finita no tiene número de Lebesgue positivo.

[]{#MA-SOL-ANM-01-017-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Cada bola es abierta y contiene su centro; sus uniones pares e impares son abiertos y cubren $D$. Ninguna bola contiene otro $p_m$: para $m>n$, $p_n-p_m\ge p_n-p_{n+1}=1/[(n+1)(n+2)]=4r_n$; para $m<n$, la distancia al vecino anterior, cuando existe, es $1/[n(n+1)]>4r_n$. Así cada $p_n$ pertenece sólo al abierto de su paridad. Dado $\lambda>0$, elegimos $n$ con $p_n-p_{n+1}<\lambda$. La bola relativa centrada en $p_n$ contiene ambos puntos, de paridades opuestas, y no está contenida en ninguno de los dos abiertos. No hay escala positiva. El dominio omitió cero y no es compacto; finitud de una cubierta particular no sustituye compacidad.

</details>
## 17.3. Heine–Cantor: reducir antes de tomar el mínimo

[]{#MA-SEC-ANM-01-017-003}

**R3. Heine–Cantor.** Si $f:D\to\mathbb R$ es continua en cada punto de un compacto $K\subseteq D$, relativamente a $D$, su restricción $h:K\to\mathbb R$ es uniformemente continua. No hace falta que $D$ sea compacto ni que $K$ sea intervalo.

La restricción es continua por C14. Fijamos $\varepsilon>0$. Si $K$ es vacío, $\delta=1$ sirve. Para $K$ no vacío, reunimos todos los pares centro-radio que controlan las salidas en la bola doble:

$$T_\varepsilon=\{(a,r)\in K\times\mathbb R_{>0}:
\forall z\in K,\ |z-a|<2r\Longrightarrow|h(z)-h(a)|<\varepsilon/2\}.$$

Cada par determina el abierto ambiental $B(a,r)$. Estas bolas cubren $K$: en un $a$ fijado, continuidad con tolerancia $\varepsilon/2$ da $\rho>0$; $r=\rho/2$ hace admisible $(a,r)$ y su bola contiene $a$. No hemos escogido una función $a\mapsto r_a$: la relación y su familia de bolas ya están determinadas por sus fórmulas.

Compacidad entrega un $J\subseteq T_\varepsilon$ finito que cubre $K$ mediante las bolas pequeñas. Es no vacío, y

$$\delta=\min\{r:(a,r)\in J\}>0.$$

Fijamos ahora $x,y\in K$ con $|x-y|<\delta$. La cubierta finita da $(a,r)\in J$ con $|x-a|<r$. No necesitamos que $y$ esté en esa misma bola pequeña. Basta observar

$$|y-a|\le|y-x|+|x-a|<\delta+r\le2r.$$

Tanto $x$ como $y$ están en la bola doble donde se guardó el control. Así

$$|h(x)-h(y)|\le|h(x)-h(a)|+|h(a)-h(y)|
<\varepsilon/2+\varepsilon/2=\varepsilon.$$

El radio quedó fijado antes de los dos puntos. La prueba produjo exactamente la uniformidad, sin compacidad secuencial ni selección de rutas o radios por todos los centros.

![Esquema con a=0, r=1, δ=3/5, x=4/5 e y=13/10. El par tiene distancia 1/2<δ; y queda fuera de la bola pequeña pero dentro de la doble. Cada índice admisible asegura error menor que ε/2 respecto de f(a) en toda la bola doble relativa. La geometría representa el paso de la prueba, no una función particular.](../../assets/books/anm/C17/C17-F03.svg){#fig-anm-c17-f03 fig-alt="Esquema con a=0, r=1, δ=3/5, x=4/5 e y=13/10. El par tiene distancia 1/2&lt;δ; y queda fuera de la bola pequeña pero dentro de la doble. Cada índice admisible asegura error menor que ε/2 respecto de f(a) en toda la bola doble relativa. La geometría representa el paso de la prueba, no una función particular."}

**Segunda lectura mediante R2.** Para cada $a\in K$, sea $A_a=\{z\in K:|h(z)-h(a)|<\varepsilon/2\}$. Son abiertos relativos por continuidad y forman una cubierta, porque $a\in A_a$. Levantarlos por $W_a=(\mathbb R\setminus K)\cup A_a$ y aplicar R2 proporciona $\lambda>0$. Si $|x-y|<\lambda$, los dos puntos pertenecen a un mismo $A_a$: $x$ está en su propia bola relativa y $y$ también. Cada salida dista menos que $\varepsilon/2$ de $h(a)$, y la desigualdad triangular concluye. Esta lectura expresa el mismo mecanismo como una propiedad de la cubierta, no como una elección global de centros.

Por Heine–Borel de C16, toda continua en un cerrado acotado real es uniformemente continua. La garantía incluye segmentos, conjuntos finitos, compactos rotos y conjuntos de recíprocos con su límite. Las hipótesis garantizan uniformidad para **toda** continua sobre ese dominio; no son necesarias para una función particular. La identidad en $\mathbb R$ es uniformemente continua aunque el dominio no sea compacto.

Acotación sola no asegura la garantía: $1/x$ en $(0,1]$ es continua pero falla la uniformidad. En efecto, para $x_n=1/(n+2)$, $y_n=1/(n+3)$,

$$|x_n-y_n|=\frac1{(n+2)(n+3)}\longrightarrow0,
\qquad |1/x_n-1/y_n|=1.$$

Dado un radio cualquiera, arquimedianidad proporciona un índice con la distancia menor que él, mientras la separación de salida sigue siendo uno. Cerradura sola tampoco basta: el cuadrado en $\mathbb R$ ya dio testigos. No se deduce ninguno de estos fallos de la mera forma de una estimación local.

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-017-017}

¿Qué uniformiza Heine–Cantor cuando $K\subseteq D$?

[]{#MA-MSOL-ANM-01-017-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

La restricción $h:K\to\mathbb R$, si $K$ es compacto y $f$ es continua en sus puntos relativamente a $D$. No uniformiza necesariamente todo $D$.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-017-018}

¿Qué información guarda un par admisible $(a,r)$?

[]{#MA-MSOL-ANM-01-017-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Que todo punto de $K$ a distancia menor que $2r$ de $a$ tiene salida a distancia menor que $\varepsilon/2$ de $h(a)$.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-017-019}

¿Cómo se verifica cobertura sin función de radios?

[]{#MA-MSOL-ANM-01-017-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Para un $a$ fijado, continuidad entrega $\rho$ y el par $(a,\rho/2)$ pertenece a la familia ya definida; su bola contiene $a$.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-017-020}

¿Tiene que entrar $y$ en la bola pequeña que cubre $x$?

[]{#MA-MSOL-ANM-01-017-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

No. $|y-a|<\delta+r\le2r$ lo coloca en la bola doble, que conserva el control necesario.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-017-021}

¿Por qué se divide el error en dos mitades?

[]{#MA-MSOL-ANM-01-017-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

Ambas salidas se comparan con $h(a)$; la suma de los dos errores estrictos menores que $\varepsilon/2$ es menor que $\varepsilon$.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-017-022}

¿Se usa la recíproca secuencial para Heine–Cantor?

[]{#MA-MSOL-ANM-01-017-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

No. La prueba reduce una familia explícita de bolas por compacidad y usa el mínimo de una lista finita.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-017-023}

¿Necesita $K$ ser un intervalo?

[]{#MA-MSOL-ANM-01-017-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

No. Compactos con varias piezas o conjuntos finitos admiten el mismo argumento.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-017-024}

¿Compacidad es necesaria para uniformidad de una función particular?

[]{#MA-MSOL-ANM-01-017-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

No. La identidad en toda $\mathbb R$ es uniforme con $\delta=\varepsilon$, aunque su dominio no sea compacto.

</details>

### Ejercicios de la sección 17.3

#### Ejercicio 11. Las dos bolas del mismo índice

[]{#MA-EX-ANM-01-017-011}

En R3, justifica todas las condiciones que llevan de un par $|x-y|<\delta$ al error menor que $\varepsilon$. ¿Por qué no basta decir que ambos están en la misma bola pequeña?

[]{#MA-SOL-ANM-01-017-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

La lista finita cubre $x$ con $B(a,r)$ y tiene $\delta\le r$. Entonces $|x-a|<r<2r$ y $|y-a|\le|y-x|+|x-a|<\delta+r\le2r$. El segundo punto puede estar fuera de $B(a,r)$, pero ambos cumplen la condición del índice en $B(a,2r)\cap K$, así sus salidas distan menos que $\varepsilon/2$ de $h(a)$. La triangular da error menor que $\varepsilon$. Afirmar pertenencia a la bola pequeña para $y$ gastaría una inclusión no probada.

**Retorno visual.** Véase [C17-F03](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 12. Uniformizar sólo la restricción

[]{#MA-EX-ANM-01-017-012}

Para $f(x)=x^2$ en $D=\mathbb R$ y $K=[-2,-1]\cup[1,2]$, aplica Heine–Cantor y da además un radio explícito. ¿Qué se puede concluir sobre todo $D$?

[]{#MA-SOL-ANM-01-017-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

$K$ es cerrado/acotado, compacto por C16, y $f$ es continua en sus puntos relativamente a $D$. R3 hace uniforme la restricción sobre $K$, sin exigir que sea intervalo. Además $|x+y|\le4$ allí, por lo que $\delta=\varepsilon/4$ controla el error. Nada de esto uniformiza todo $D$; E002 ya refuta uniformidad del cuadrado en la recta.

</details>

#### Ejercicio 13. La lectura por cubiertas de salida

[]{#MA-EX-ANM-01-017-013}

Prueba Heine–Cantor usando los abiertos relativos $A_a=\{z\in K:|h(z)-h(a)|<\varepsilon/2\}$ y R2. Declara el orden de los testigos.

[]{#MA-SOL-ANM-01-017-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Cada $A_a$ es preimagen relativa de un intervalo abierto y contiene $a$, así forman cubierta. Se levantan por $W_a=(\mathbb R\setminus K)\cup A_a$ y R2 da una escala $\lambda>0$ antes de los puntos $x,y$. Para $x\in K$, R2 proporciona un índice $a$ que contiene su bola relativa. Si $|x-y|<\lambda$, tanto $x$ como $y$ están en ella y por tanto en $A_a$. Ambos errores respecto de $h(a)$ son menores que $\varepsilon/2$, y su suma controla la diferencia. No se construye un selector $x\mapsto a_x$. Para $K$ vacío sirve cualquier radio.

</details>

#### Ejercicio 14. Acotación sin frontera incluida

[]{#MA-EX-ANM-01-017-014}

Refuta uniformidad de $1/x$ en $(0,1]$ con pares dados válidos desde $n=0$. Explica qué hipótesis de Heine–Cantor falta.

[]{#MA-SOL-ANM-01-017-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Tomamos $x_n=1/(n+2)$ y $y_n=1/(n+3)$, ambos del dominio desde cero. La distancia es $1/[(n+2)(n+3)]$, tendente a cero, pero las salidas son $n+2,n+3$ y difieren uno. Para $\varepsilon_0=1$, todo radio positivo admite un índice con distancia menor, refutando uniformidad. El dominio es acotado pero no cerrado: cero es adherente y está omitido. Falta compacidad, no continuidad de la función en el dominio efectivo.

</details>

#### Ejercicio 15. Vacuidad y prueba sin rutas

[]{#MA-EX-ANM-01-017-015}

Explica dónde entra no vacuidad en el mínimo de R3 y por qué la prueba no necesita CC(R). Contrasta la demostración por pares malos de una negación.

[]{#MA-SOL-ANM-01-017-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Para $K$ no vacío, una subcubierta no puede tener conjunto de índices vacío; por ello sus radios forman conjunto finito no vacío y poseen mínimo positivo. Para $K$ vacío no se toma mínimo: $\delta=1$ satisface la condición vacía. La prueba define todos los pares admisibles, verifica cobertura con testigos individuales y usa una aplicación de compacidad seguida de datos finitos; no fabrica rutas ni selecciona radios por todos los centros. Una prueba que fabrica pares malos para cada escala necesita justificar esa selección numerable, como en la recíproca condicional de R6.

</details>
## 17.4. Medir la oscilación a cada escala

[]{#MA-SEC-ANM-01-017-004}

Heine–Cantor garantiza una escala, pero puede no dar una fórmula sencilla para ella. Podemos registrar cuánto varía la función cuando restringimos la distancia de entrada.

**R4. Módulo de oscilación.** Supongamos $D$ no vacío y $f:D\to\mathbb R$ acotada: $|f(x)|\le B$ con $B\ge0$. Para $t\ge0$ definimos

$$\omega_f(t)=\sup\{|f(x)-f(y)|:x,y\in D,\ |x-y|\le t\}.$$

El conjunto es no vacío porque admite pares diagonales con diferencia cero; está acotado entre cero y $2B$. El supremo existe por C00. Si $D$ es vacío, fijamos por convención $\omega_f(t)=0$; no se toma supremo real del conjunto vacío. La acotación de valores es una hipótesis suficiente para que este módulo global sea real finito. Uniformidad sola no acota los valores: la identidad en $\mathbb R$ lo recuerda. Esa identidad tiene, de hecho, módulo finito $\omega(t)=t$; no afirmamos que toda función no acotada carezca de módulo finito.

Los conjuntos de diferencias aumentan al aumentar $t$; por eso $\omega$ es no decreciente, $\omega(0)=0$, y

$$|f(x)-f(y)|\le\omega_f(t)\quad\text{si }|x-y|\le t.$$

En este marco acotado, $f$ es uniformemente continua si y sólo si $\omega_f(t)\to0$ cuando $t\downarrow0$. Para la dirección directa, dada $\varepsilon>0$, uniformidad con tolerancia $\varepsilon/2$ da $\delta>0$. Si $0<t<\delta$, todos los valores del conjunto que define $\omega(t)$ son menores que $\varepsilon/2$, por lo que

$$0\le\omega(t)\le\varepsilon/2<\varepsilon.$$

El supremo podría igualar $\varepsilon/2$; por eso reservamos presupuesto. Para la recíproca, el límite da $\eta>0$ con $\omega(t)<\varepsilon$ para $0<t<\eta$. Tomamos $t=\eta/2$ y $\delta=t$. Toda pareja de distancia menor que $\delta$ está en el conjunto del módulo a escala $t$, y su diferencia es a lo sumo $\omega(t)<\varepsilon$.

Si $f$ es Lipschitz con constante $L$, su módulo satisface $\omega_f(t)\le Lt$. La raíz tiene $\omega(t)\le\sqrt t$ en cualquier dominio no negativo donde este módulo sea definido; son dos tipos distintos de dependencia entre escalas.

**Un módulo exacto.** Para $q(x)=x^2$ en $[0,1]$,

$$\omega_q(t)=
\begin{cases}2t-t^2,&0\le t\le1,\\1,&t\ge1.\end{cases}$$

Si $0\le v\le u\le1$ y $d=u-v\le t\le1$, entonces $u^2-v^2=d(2u-d)\le d(2-d)\le t(2-t)$. La última desigualdad resulta de $(t-d)(2-t-d)\ge0$. El par $u=1$, $v=1-t$ alcanza la cota. Si $t\ge1$, todas las diferencias son a lo sumo uno y el par $1,0$ lo alcanza. Para todo $t$, $\omega_q(t)\le2t$; esa cota Lipschitz es más simple pero menos precisa.

![En \[0,1\], los módulos exactos de x² y √x son 2t−t² y √t para 0≤t≤1; después de uno ambos valen uno. La recta 2t es una cota más sencilla del módulo del cuadrado. Las fórmulas se prueban por álgebra y pares que alcanzan las cotas; las curvas sólo las representan.](../../assets/books/anm/C17/C17-F04.svg){#fig-anm-c17-f04 fig-alt="En \[0,1\], los módulos exactos de x² y √x son 2t−t² y √t para 0≤t≤1; después de uno ambos valen uno. La recta 2t es una cota más sencilla del módulo del cuadrado. Las fórmulas se prueban por álgebra y pares que alcanzan las cotas; las curvas sólo las representan."}

No exigimos que el supremo sea alcanzado para un dominio arbitrario, ni continuidad del módulo como función de $t$. Para aplicar el criterio sólo necesitamos la definición del supremo y el control cerca de cero. En un compacto, C16 acota toda continua y R3 hace que su módulo tienda a cero.

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-017-025}

¿Qué garantiza que el módulo global definido sea real finito?

[]{#MA-MSOL-ANM-01-017-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

En el marco usado, $D$ no vacío y $|f|\le B$: las diferencias contienen cero y están acotadas por $2B$.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-017-026}

¿Qué significa $\omega_f(t)$?

[]{#MA-MSOL-ANM-01-017-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

El supremo de todas las diferencias de salida de pares del dominio a distancia a lo sumo $t$. No exige que un par alcance ese supremo.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-017-027}

¿Por qué $\omega_f(0)=0$?

[]{#MA-MSOL-ANM-01-017-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

La distancia cero implica $x=y$, así todas las diferencias del conjunto son cero. Para dominio vacío se fijó módulo cero por convención.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-017-028}

¿Por qué el módulo no decrece?

[]{#MA-MSOL-ANM-01-017-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Al aumentar $t$ se admiten todos los pares anteriores y quizá otros; el supremo de un conjunto contenido no supera el del mayor.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-017-029}

¿Por qué una cota estricta de todos los valores no da supremo estrictamente menor?

[]{#MA-MSOL-ANM-01-017-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Por ejemplo, todos los valores de $[0,1)$ son menores que uno pero su supremo es uno. Se usa presupuesto $\varepsilon/2$.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-017-030}

¿Cómo da uniformidad el límite del módulo en cero?

[]{#MA-MSOL-ANM-01-017-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Se toma una escala $t>0$ con $\omega_f(t)<\varepsilon$ y se fija $\delta=t$; los pares con distancia menor que ella tienen error a lo sumo ese módulo.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-017-031}

¿Qué par alcanza el módulo de $x^2$ en $[0,1]$ para $0\le t\le1$?

[]{#MA-MSOL-ANM-01-017-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

El par $1,1-t$ tiene distancia $t$ y diferencia $2t-t^2$, igual a la cota probada para todos los pares.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-017-032}

¿Uniformidad obliga a valores acotados en todo dominio?

[]{#MA-MSOL-ANM-01-017-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

No: la identidad uniforme en $\mathbb R$ es no acotada, aunque sí tiene módulo finito $\omega(t)=t$.

</details>

### Ejercicios de la sección 17.4

#### Ejercicio 16. Existencia y orden del módulo

[]{#MA-EX-ANM-01-017-016}

Para $f:D\to\mathbb R$ acotada en un dominio no vacío, justifica existencia de $\omega_f(t)$, su monotonía, valor en cero y la cota de diferencias. Trata el dominio vacío.

[]{#MA-SOL-ANM-01-017-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Si $|f|\le B$, toda diferencia está entre cero y $2B$. Para cada $t\ge0$, los pares diagonales aportan cero, por lo que el conjunto es no vacío y tiene supremo. Si $s\le t$, todos los pares admitidos a escala $s$ también lo son a escala $t$, así $\omega(s)\le\omega(t)$. A escala cero sólo hay pares iguales y el módulo vale cero. Toda diferencia admitida es a lo sumo el supremo. Para vacío se define módulo cero por convención; no se atribuye un supremo real al conjunto vacío.

</details>

#### Ejercicio 17. Supremo y presupuesto estricto

[]{#MA-EX-ANM-01-017-017}

Una prueba dice: «todos los errores son menores que $\varepsilon$, luego su supremo también». Repara la dirección uniforme implica módulo tendente a cero y prueba la recíproca.

[]{#MA-SOL-ANM-01-017-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

El supremo de $[0,\varepsilon)$ es $\varepsilon$, así la estrictitud no pasa así al supremo. Se pide primero error $\varepsilon/2$ a uniformidad; para $0<t<\delta$, el supremo es a lo sumo $\varepsilon/2<\varepsilon$, lo que prueba el límite cero. Recíprocamente, dado $\varepsilon$, el límite da $\eta>0$ y $\omega(t)<\varepsilon$ para $0<t<\eta$. Fijamos $t=\eta/2$ y $\delta=t$. Todo par de distancia menor que $\delta$ tiene error a lo sumo $\omega(t)<\varepsilon$. Se conserva el orden de los cuantificadores.

</details>

#### Ejercicio 18. Módulo exacto del cuadrado

[]{#MA-EX-ANM-01-017-018}

Calcula $\omega(t)$ para $x^2$ en $[0,1]$, para todo $t\ge0$. Da los pares que alcanzan cada cota y compara con $2t$.

[]{#MA-SOL-ANM-01-017-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Si $0\le v\le u\le1$, $d=u-v\le t\le1$, la diferencia es $d(2u-d)\le d(2-d)\le t(2-t)$ porque la última diferencia es $(t-d)(2-t-d)\ge0$. El par $1,1-t$ alcanza $2t-t^2$ para $0\le t\le1$. Si $t\ge1$, la diferencia no supera uno y el par $1,0$ lo alcanza. Así el módulo es $2t-t^2$ en la primera escala y uno después. Siempre está bajo $2t$; para $0<t\le1$ la mejora exacta es $t^2$.

**Retorno visual.** Véase [C17-F04](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 19. Una raíz y su módulo

[]{#MA-EX-ANM-01-017-019}

Calcula el módulo exacto de $\sqrt{x}$ en $[0,1]$. Contrasta la dependencia en $t$ con la del cuadrado.

[]{#MA-SOL-ANM-01-017-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

R1 da diferencia a lo sumo $\sqrt{|x-y|}$, por tanto $\omega(t)\le\sqrt t$ para $0\le t\le1$. El par $t,0$ alcanza esa cota. Para $t\ge1$, todas las diferencias son a lo sumo uno y el par $1,0$ la alcanza. El módulo es $\sqrt t$ hasta uno y uno después. Tiende a cero, pero su cociente por $t$ es $1/\sqrt t$ cerca de cero y no admite cota lineal uniforme. El cuadrado sí tiene módulo a lo sumo $2t$.

</details>

#### Ejercicio 20. Valores no acotados y módulo finito

[]{#MA-EX-ANM-01-017-020}

Explica por qué no se puede concluir que una uniforme en $\mathbb R$ tiene valores acotados. Calcula el módulo de la identidad y prueba uniformidad directamente.

[]{#MA-SOL-ANM-01-017-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

La identidad tiene valores que recorren toda la recta y no están acotados. A escala $t\ge0$, las diferencias admitidas están entre cero y $t$, y el par $0,t$ alcanza $t$, así el módulo es finito e igual a $t$. Directamente, $\delta=\varepsilon$ da uniformidad. La hipótesis de acotación de R4 era suficiente para construir un módulo real global sin más análisis, no necesaria en todos los ejemplos.

</details>
## 17.5. Transportar tolerancias por operaciones

[]{#MA-SEC-ANM-01-017-005}

La continuidad puntual se conserva por muchas operaciones. Uniformidad exige además controlar los factores que multiplican errores y los denominadores. Todas las funciones de una operación se consideran en el mismo dominio efectivo.

**R5. Sumas y productos.** Si $f,g:D\to\mathbb R$ son uniformemente continuas, $f+g$ también: elegimos radios para error $\varepsilon/2$ en cada una y tomamos su mínimo. La desigualdad triangular suma los dos errores. Multiplicar por una constante $c$ se trata con $\varepsilon/|c|$ cuando $c\ne0$; para $c=0$ la salida es constante.

Para productos suponemos además $|f|\le M_f$, $|g|\le M_g$ en $D$, con cotas no negativas. Pedimos a ambas funciones errores menores que $\eta=\varepsilon/(M_f+M_g+1)>0$ y usamos el mínimo de sus radios. Entonces

$$|f(x)g(x)-f(y)g(y)|
\le |g(x)|\,|f(x)-f(y)|+|f(y)|\,|g(x)-g(y)|
\le(M_f+M_g)\eta<\varepsilon.$$

El caso $M_f+M_g=0$ entrega diferencia cero y satisface la conclusión. Sólo se combinan dos radios dados, no una familia infinita. Las cotas son suficientes: sin ellas, dos funciones uniformes pueden tener producto no uniforme. $f(x)=g(x)=x$ en $\mathbb R$ tiene producto $x^2$. No son necesarias para cada producto particular: multiplicar la identidad por la constante uno sigue siendo uniforme.

**Recíprocos y cocientes.** Si $g$ es uniforme y $|g(x)|\ge m>0$ en $D$, entonces $1/g$ tiene exactamente ese dominio y

$$\left|\frac1{g(x)}-\frac1{g(y)}\right|
\le\frac{|g(x)-g(y)|}{m^2}.$$

Un radio que da error $\varepsilon m^2$ para $g$ da error $\varepsilon$ para el recíproco. Éste también está acotado por $1/m$. Si $f$ es uniforme y acotada, el producto de $f$ y $1/g$ muestra uniformidad del cociente. «No tener ceros» por sí solo no proporciona $m$: en $(0,1]$, la identidad es uniforme, no tiene ceros y su recíproco no es uniforme.

En un compacto, C16 proporciona acotación para las continuas y un margen positivo para el denominador continuo sin ceros. R3 uniformiza las funciones, y las reglas anteriores justifican el cociente. Alternativamente, C14 da continuidad del cociente y R3 vuelve a aplicarse, siempre con el dominio compacto declarado.

**Composición.** Sea $f:D\to E$ uniforme y $g:E\to\mathbb R$ uniforme sobre $E$; bastaría uniformidad de $g$ en $f[D]$. Para error final $\varepsilon$, primero elegimos $\eta>0$ que controle $g$. Después elegimos $\delta>0$ que produzca error de salida menor que $\eta$ para $f$. Así

$$|x-y|<\delta\Longrightarrow|f(x)-f(y)|<\eta
\Longrightarrow|g(f(x))-g(f(y))|<\varepsilon.$$

![Para f(x)=2x en \[0,1\] y g(y)=y² en \[0,2\], el error exterior tiene cota cuatro veces la distancia. Para ε=1, sirve η=1/4 y después δ=η/2=1/8. El par de entrada 1/2,3/5 ilustra distancias 1/10,1/5 y 11/25, cada una bajo su presupuesto. Las tolerancias se eligen desde la salida final hacia la entrada.](../../assets/books/anm/C17/C17-F05.svg){#fig-anm-c17-f05 fig-alt="Para f(x)=2x en \[0,1\] y g(y)=y² en \[0,2\], el error exterior tiene cota cuatro veces la distancia. Para ε=1, sirve η=1/4 y después δ=η/2=1/8. El par de entrada 1/2,3/5 ilustra distancias 1/10,1/5 y 11/25, cada una bajo su presupuesto. Las tolerancias se eligen desde la salida final hacia la entrada."}

El orden de elección sigue el transporte de tolerancias en sentido inverso al de las funciones. Continuidad meramente puntual de la función exterior no basta: componer la identidad uniforme en $\mathbb R$ con el cuadrado continuo pierde uniformidad.

Finalmente, una inyección continua sobre un compacto $K$ tiene inversa continua en $H=f[K]$ por C16. Considerar la inversa como función $H\to\mathbb R$ conserva continuidad porque las distancias de salida son las mismas. Como $H$ es compacto, R3 hace también uniforme a esa inversa. No afirmamos que tenga constante Lipschitz: el cuadrado en $[0,1]$ tiene inversa raíz, uniforme pero no Lipschitz.

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-017-033}

¿Cómo se combinan dos radios para una suma?

[]{#MA-MSOL-ANM-01-017-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Se pide error $\varepsilon/2$ a cada sumando y se toma el mínimo de los dos radios positivos.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-017-034}

¿Qué hipótesis suficientes se añaden para productos?

[]{#MA-MSOL-ANM-01-017-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Cotas globales $M_f,M_g$ de los valores; controlan los factores que multiplican las diferencias en la identidad de producto.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-017-035}

¿Qué producto refuta conservación automática en dominios arbitrarios?

[]{#MA-MSOL-ANM-01-017-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

La identidad por sí misma en $\mathbb R$: ambos factores son uniformes, pero su producto $x^2$ no lo es.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-017-036}

¿Qué dato positivo controla un recíproco?

[]{#MA-MSOL-ANM-01-017-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Un margen global $|g(x)|\ge m>0$; entonces la diferencia de recíprocos es a lo sumo la diferencia de $g$ dividida por $m^2$.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-017-037}

¿Ausencia de ceros basta para ese margen?

[]{#MA-MSOL-ANM-01-017-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

No. $g(x)=x$ en $(0,1]$ nunca vale cero pero tiene valores positivos arbitrariamente pequeños.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-017-038}

¿Qué tolerancia se elige primero en una composición?

[]{#MA-MSOL-ANM-01-017-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

La tolerancia intermedia $\eta$ que produce error final $\varepsilon$ en la función exterior; después el radio de la interior que produce error menor que $\eta$.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-017-039}

¿Qué dominio basta controlar uniformemente para la función exterior?

[]{#MA-MSOL-ANM-01-017-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

La imagen $f[D]$, porque sólo esos valores se usan al evaluar $g\circ f$.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-017-040}

¿Por qué una inversa compacta continua es también uniforme?

[]{#MA-MSOL-ANM-01-017-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

La imagen $H$ es compacta por C16 y la inversa es continua allí; Heine–Cantor se aplica con dominio $H$.

</details>

### Ejercicios de la sección 17.5

#### Ejercicio 21. Radios para una suma

[]{#MA-EX-ANM-01-017-021}

Prueba uniformidad de $af+bg$ si $f,g$ son uniformes en el mismo dominio y $a,b$ son constantes. Trata constantes cero.

[]{#MA-SOL-ANM-01-017-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Si $a\ne0$, pedimos a $f$ error menor que $\varepsilon/(2|a|)$ y obtenemos un radio; si $a=0$, el término tiene error cero y usamos radio uno para él. Hacemos lo mismo con $g,b$. El mínimo de ambos radios positivos sirve para todos los pares y la diferencia de $af+bg$ es a lo sumo la suma de los dos errores escalados, cada uno menor que $\varepsilon/2$ cuando no es cero. La suma es menor que $\varepsilon$.

</details>

#### Ejercicio 22. Factores que amplifican errores

[]{#MA-EX-ANM-01-017-022}

Prueba la regla de producto bajo cotas $M_f,M_g$. Muestra que eliminar ambas cotas pierde la garantía y que no son necesarias para todo producto particular.

[]{#MA-SOL-ANM-01-017-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Pedimos errores menores que $\eta=\varepsilon/(M_f+M_g+1)$ a ambas funciones y tomamos el mínimo de sus radios. La identidad de diferencias del producto da cota $(M_f+M_g)\eta<\varepsilon$, incluidos sumandos nulos. En $\mathbb R$, ambos factores identidad son uniformes y no acotados, pero su producto cuadrado falla uniformidad. En cambio, identidad por constante uno es uniforme aunque el primer factor sea no acotado. La regla declara condiciones suficientes y el ejemplo sólo refuta una regla universal sin ellas.

</details>

#### Ejercicio 23. Un cociente sobre dos piezas

[]{#MA-EX-ANM-01-017-023}

En $K=[-2,-1]\cup[1,2]$, sean $f(x)=x+1$ y $g(x)=x^2$. Da un radio explícito uniforme para $f/g$, usando cotas de numerador, denominador y diferencias.

[]{#MA-SOL-ANM-01-017-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

En $K$, $|f|\le3$, $g\ge1$, $|f(x)-f(y)|=|x-y|$, y $|g(x)-g(y)|\le4|x-y|$. Sea $d=|x-y|$. La identidad $f(x)/g(x)-f(y)/g(y)=(f(x)-f(y))/g(x)+f(y)(1/g(x)-1/g(y))$ da error a lo sumo $d+3\cdot4d=13d$, porque los denominadores tienen magnitud al menos uno. Por tanto $\delta=\varepsilon/13$ sirve para todos los pares, incluso en piezas distintas. El cociente está definido en todo $K$.

</details>

#### Ejercicio 24. El orden inverso de tolerancias

[]{#MA-EX-ANM-01-017-024}

Sean $f:D\to E$ y $g:E\to\mathbb R$ uniformes. Prueba uniformidad de $g\circ f$ y refuta sustituir uniformidad de $g$ por continuidad puntual.

[]{#MA-SOL-ANM-01-017-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Primero uniformidad de $g$ para $\varepsilon$ da $\eta>0$. Después uniformidad de $f$ para $\eta$ da $\delta>0$. Distancia de entrada menor que $\delta$ produce salidas de $f$ a distancia menor que $\eta$, y por tanto error final menor que $\varepsilon$. Basta control de $g$ sobre $f[D]$. Si $D=E=\mathbb R$, $f$ identidad es uniforme, $g$ cuadrado es continua pero no uniforme, y la composición también es cuadrado no uniforme. La continuidad puntual exterior no da una tolerancia intermedia común.

**Retorno visual.** Véase [C17-F05](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 25. Inversa uniforme sin control lineal

[]{#MA-EX-ANM-01-017-025}

Justifica que una inyección continua $f:K\to\mathbb R$ sobre compacto tiene inversa uniforme en su imagen. Da un ejemplo en que esa inversa no sea Lipschitz.

[]{#MA-SOL-ANM-01-017-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

C16 hace compacta $H=f[K]$ y prueba continuidad de la inversa $h:H\to K$. Retipar su salida a $\mathbb R$ conserva continuidad, por usar la misma distancia; Heine–Cantor la hace uniforme sobre $H$. El vacío también queda incluido. Para $f(x)=x^2$ sobre $[0,1]$, la inyectividad sigue del orden no negativo, su imagen es $[0,1]$ por raíces C10 y su inversa es $\sqrt y$. R1 prueba que ésta es uniforme y no Lipschitz en ese dominio.

</details>
## 17.6. Pares próximos y rutas dadas

[]{#MA-SEC-ANM-01-017-006}

**R6. Prueba mediante dos sucesiones dadas.** Si $f:D\to\mathbb R$ es uniforme y $(x_n),(y_n)$ son dos sucesiones dadas en $D$ con $|x_n-y_n|\to0$, entonces $|f(x_n)-f(y_n)|\to0$. Para $\varepsilon>0$ fijamos el radio uniforme $\delta$. La convergencia de las distancias proporciona $N$ tal que son menores que $\delta$ para $n\ge N$; desde ese índice las diferencias de salida son menores que $\varepsilon$. No hace falta que ninguna de las dos rutas converja, ni que sea acotada.

Por ejemplo, $x_n=n+1$ y $y_n=n+1+1/(n+1)$ se acercan entre sí aunque escapen al infinito. Para el cuadrado,

$$|y_n-x_n|=\frac1{n+1}\to0,
\qquad y_n^2-x_n^2=2+\frac1{(n+1)^2}\ge2.$$

R6 refuta uniformidad sin fabricar una ruta por selección: las fórmulas ya la determinan. Los pares recíprocos de R3 muestran el mismo fallo junto a un extremo omitido.

![Se representan n=0,1,2,4 de las rutas recíprocas dadas. La distancia de entrada es 1/\[(n+2)(n+3)\] y tiende a cero; bajo f(x)=1/x la distancia de salida es siempre uno. R6 directo refuta uniformidad; no se usa la recíproca ni selección de rutas. Muestra finita, no prueba visual de convergencia.](../../assets/books/anm/C17/C17-F06.svg){#fig-anm-c17-f06 fig-alt="Se representan n=0,1,2,4 de las rutas recíprocas dadas. La distancia de entrada es 1/\[(n+2)(n+3)\] y tiende a cero; bajo f(x)=1/x la distancia de salida es siempre uno. R6 directo refuta uniformidad; no se usa la recíproca ni selección de rutas. Muestra finita, no prueba visual de convergencia."}

**Recíproca con alcance declarado.** Supongamos que toda pareja de rutas dadas en $D$ con distancia tendente a cero tiene diferencias de salida tendentes a cero. Para deducir uniformidad en un dominio arbitrario mediante el argumento siguiente usamos $\mathrm{CC}(\mathbb R)$, sólo como premisa del resultado condicional.

Si falla uniformidad, fijamos la tolerancia $\varepsilon_0>0$ de la negación. Los conjuntos

$$A_n=\{x\in D:\exists y\in D,
|x-y|<1/(n+1),\ |f(x)-f(y)|\ge\varepsilon_0\}$$

son no vacíos. Una aplicación de $\mathrm{CC}(\mathbb R)$ da una ruta $x_n\in A_n$. Definimos ahora

$$B_n=\{y\in D:|x_n-y|<1/(n+1),
|f(x_n)-f(y)|\ge\varepsilon_0\}.$$

Son no vacíos por la pertenencia anterior; otra aplicación de la misma premisa da $y_n\in B_n$. Las distancias tienden a cero, pero las diferencias de salida permanecen al menos en $\varepsilon_0$, contradicción. Se gastó selección al fabricar ambas rutas, no en la prueba directa R6. Heine–Cantor no depende de esta recíproca.

Si $D$ no vacío viene con una sobreyección **dada** $e:\mathbb N\to D$, podemos fabricar estos pares sin CC(R): tomamos el menor $j$ para el que existe $k$ con el par $e(j),e(k)$ malo a escala $1/(n+1)$; después el menor $k$ que satisface la condición para ese $j$. Buen orden y sobreyectividad determinan las dos rutas. No se presupone una enumeración para dominios arbitrarios. El dominio vacío es uniforme por separado.

**Preservación de Cauchy.** Toda uniforme envía una sucesión de Cauchy dada a otra de Cauchy. Para $\varepsilon>0$ elegimos $\delta$ uniforme; la condición de Cauchy de entrada da un $N$ con $|x_n-x_m|<\delta$ para $n,m\ge N$, y entonces las diferencias de salida son menores que $\varepsilon$. La definición y acotación de rutas de Cauchy son interfaces de C07.

Esta preservación sola no caracteriza uniformidad en dominios arbitrarios. El cuadrado en $\mathbb R$ la cumple: cada ruta de Cauchy es acotada por algún $M>0$, y $|x_n^2-x_m^2|\le2M|x_n-x_m|$ hace Cauchy a su imagen. Pero el cuadrado no es uniforme en toda la recta. El test con **dos rutas próximas** es más exigente que el test sobre una ruta de Cauchy.

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-017-041}

¿Deben converger las dos rutas próximas de R6?

[]{#MA-MSOL-ANM-01-017-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

No. Sólo se exige que su distancia mutua tienda a cero; pueden escaparse al infinito.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-017-042}

¿Dónde se gasta selección en la recíproca general?

[]{#MA-MSOL-ANM-01-017-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Primero al escoger $x_n\in A_n$ y después $y_n\in B_n$. Ambas familias reales no vacías se seleccionan bajo la premisa local CC(R).

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-017-043}

¿Qué reemplaza CC(R) con una enumeración dada?

[]{#MA-MSOL-ANM-01-017-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

El menor índice de la primera entrada que tiene un compañero malo, y luego el menor índice de ese compañero. La sobreyección dada garantiza existencia.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-017-044}

¿Qué diferencia de salida tienen los pares del cuadrado que escapan?

[]{#MA-MSOL-ANM-01-017-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Para $x_n=n+1$, $y_n=x_n+1/(n+1)$, es $2+1/(n+1)^2\ge2$, aunque la distancia de entrada tiende a cero.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-017-045}

¿Por qué una uniforme preserva una ruta de Cauchy?

[]{#MA-MSOL-ANM-01-017-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

El radio uniforme para $\varepsilon$ se inserta en la condición de Cauchy de entrada, y desde un mismo índice controla todos los pares de términos de salida.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-017-046}

¿Esa preservación caracteriza uniformidad en toda $\mathbb R$?

[]{#MA-MSOL-ANM-01-017-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

No. El cuadrado preserva rutas de Cauchy porque cada una está acotada y allí tiene constante Lipschitz, pero no es uniforme en toda la recta.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-017-047}

¿Por qué las diferencias de salida separadas refutan uniformidad sin recíproca?

[]{#MA-MSOL-ANM-01-017-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

Basta la implicación directa R6: si la función fuera uniforme, esos pares dados tendrían diferencias tendentes a cero, contradicción.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-017-048}

¿Qué valor evita el problema del índice inicial cero?

[]{#MA-MSOL-ANM-01-017-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Las escalas son $1/(n+1)$ y los pares recíprocos usan $n+2,n+3$; no se divide por $n$ cuando $n=0$.

</details>

### Ejercicios de la sección 17.6

#### Ejercicio 26. Rutas que no convergen

[]{#MA-EX-ANM-01-017-026}

Para $x_n=n+1$ y $y_n=n+1+1/(n+1)$, calcula las distancias de entrada y salida bajo el cuadrado. Usa sólo la dirección directa de R6 para concluir.

[]{#MA-SOL-ANM-01-017-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La distancia de entrada es $1/(n+1)$, tendente a cero. La diferencia de cuadrados es $2+1/(n+1)^2$, que nunca baja de dos y por tanto no tiende a cero. Si el cuadrado fuera uniforme, la dirección directa R6 obligaría a que esas diferencias tendieran a cero, contradicción. Ninguna ruta de entrada converge o es acotada; la dirección directa no lo exigía. Los pares están dados por fórmula desde $n=0$, sin selección adicional.

</details>

#### Ejercicio 27. Dos familias y dos selecciones

[]{#MA-EX-ANM-01-017-027}

Reconstruye la recíproca secuencial de R6 bajo CC(R). Identifica las dos familias reales no vacías y explica por qué Heine–Cantor no queda condicionado por esta prueba.

[]{#MA-SOL-ANM-01-017-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

El fallo de uniformidad fija $\varepsilon_0>0$. Para cada $n$, $A_n$ contiene entradas que tienen algún compañero a distancia menor que $1/(n+1)$ y error al menos $\varepsilon_0$; negación garantiza no vacuidad. CC(R) selecciona $x_n\in A_n$. Luego $B_n$ reúne los compañeros de ese $x_n$ con ambas propiedades y es no vacío; CC(R) selecciona $y_n\in B_n$. Estas rutas tienen distancia tendente a cero y salida separada, contradiciendo la propiedad de pares dada. Sólo esta recíproca usa las selecciones. Heine–Cantor fue demostrado directamente por una cubierta explícita y finitud, sin recurrir a la recíproca.

</details>

#### Ejercicio 28. Una enumeración de pares malos

[]{#MA-EX-ANM-01-017-028}

Supón dada una sobreyección $e:\mathbb N\to D$ no vacío. Construye los pares malos de una negación de uniformidad mediante mínimos de índices, sin CC(R).

[]{#MA-SOL-ANM-01-017-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Fijamos $\varepsilon_0$ de la negación. Para cada $n$, existe un par malo en $D$ y, por sobreyectividad, índices $j,k$ que lo representan. El conjunto de $j$ para los que existe algún $k$ malo a escala $1/(n+1)$ es no vacío; tomamos su mínimo $j_n$. Para ese índice, el conjunto de compañeros $k$ es no vacío y tiene mínimo $k_n$. Los mínimos únicos definen $x_n=e(j_n)$ y $y_n=e(k_n)$, que tienen distancia menor que $1/(n+1)$ y error al menos $\varepsilon_0$. Se usa la enumeración dada, sin inferirla para dominios arbitrarios.

</details>

#### Ejercicio 29. Preservar una ruta de Cauchy

[]{#MA-EX-ANM-01-017-029}

Prueba que una uniforme envía toda ruta de Cauchy dada a otra de Cauchy. Refuta la recíproca universal con el cuadrado en $\mathbb R$.

[]{#MA-SOL-ANM-01-017-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Para error $\varepsilon$ elegimos el radio uniforme $\delta$. La condición Cauchy de entrada da $N$ con todas las distancias entre términos posteriores menores que $\delta$; uniformidad hace todas las diferencias de salida posteriores menores que $\varepsilon$. Para el cuadrado, cada ruta Cauchy es acotada, digamos $|x_n|\le M$ con $M>0$. Entonces $|x_n^2-x_m^2|\le2M|x_n-x_m|$, que convierte su condición Cauchy de entrada en la de salida. Sin embargo el cuadrado falla uniformidad en toda la recta, por E002/E026. No se confundió una ruta acotada particular con control sobre todo el dominio.

</details>

#### Ejercicio 30. Pares recíprocos y una frontera

[]{#MA-EX-ANM-01-017-030}

En $(0,1]$, usa $x_n=1/(n+2)$ y $y_n=1/(n+3)$ para comparar identidad y recíproco. ¿Qué aprende el test de pares?

[]{#MA-SOL-ANM-01-017-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La distancia de entrada es $1/[(n+2)(n+3)]\to0$. Bajo identidad la diferencia es la misma y tiende a cero, conforme a uniformidad. Bajo recíproco la diferencia vale uno para todo $n$, refutando uniformidad por R6 directo. Las dos rutas convergen a cero, que está fuera del dominio; no se evalúa el recíproco en ese punto exterior. El test controla pares dentro del dominio efectivo.

**Retorno visual.** Véase [C17-F06](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>
## 17.7. Completar el dominio sin seleccionar aproximantes

[]{#MA-SEC-ANM-01-017-007}

Una uniforme real no puede perder control al aproximarse a un punto omitido de adherencia. Vamos a construir el valor de frontera mediante supremos e ínfimos de **todos** los valores cercanos, sin escoger una sucesión que se aproxime a cada punto.

**R7. Extensión uniforme al cierre.** Toda uniforme $f:D\to\mathbb R$ admite una extensión uniforme $F:\overline D\to\mathbb R$, y ésta es la única extensión continua. Si $D$ es vacío, también lo es su cierre y la función vacía resuelve el enunciado. Supongamos $D$ no vacío.

Uniformidad para error uno da un $\delta_0>0$, que fijamos una sola vez para toda la construcción. Sea $r_0=\delta_0/4$. Para $p\in\overline D$ y $0<r\le r_0$, ponemos

$$E_{p,r}=f[D\cap B(p,r)],\qquad
L_{p,r}=\inf E_{p,r},\quad U_{p,r}=\sup E_{p,r}.$$

Las imágenes son no vacías por adherencia. Para probar acotación fijamos, sólo para este $p$, un $a\in D\cap B(p,r_0)$. Todos los $x$ de esa vecindad satisfacen $|x-a|<2r_0<\delta_0$, por lo que $|f(x)-f(a)|<1$. Así $E_{p,r_0}$ es acotada y también todas sus subimágenes. No se forma una familia elegida $p\mapsto a_p$.

Las imágenes se anidan al disminuir $r$. El conjunto de todos los $L_{p,r}$ es no vacío y está acotado superiormente por $U_{p,r_0}$; definimos por fórmula

$$F(p)=\sup\{L_{p,r}:0<r\le r_0\}.$$

Para cualquier $r$ admisible, $L_{p,r}\le F(p)$. También $F(p)\le U_{p,r}$: para cada $s$ admisible, la imagen a escala $\min(r,s)$ es no vacía y está contenida en las dos imágenes; un valor de esa intersección da $L_{p,s}\le U_{p,r}$. Por tanto $U_{p,r}$ acota todos los ínfimos del corte. Hemos probado

$$L_{p,r}\le F(p)\le U_{p,r}\qquad(0<r\le r_0).$$

**Anchura pequeña.** Dada $\eta>0$, uniformidad da $\delta>0$ para error $\eta$. Si $0<r\le r_0$ y $2r<\delta$, todos los pares de entradas en $B(p,r)\cap D$ distan menos que $\delta$, y todos sus valores difieren menos que $\eta$. Esto implica $U_{p,r}-L_{p,r}\le\eta$: para cada valor $v$, todos los demás son a lo sumo $v+\eta$, así $U_{p,r}\le v+\eta$; entonces $U_{p,r}-\eta$ es cota inferior y no excede $L_{p,r}$. Reservar $\eta=\varepsilon/2$ hace la anchura menor que $\varepsilon$ a una escala adecuada.

Consecuentemente sólo un real puede pertenecer a todos estos intervalos: dos candidatos distintos a distancia $d>0$ no caben en un intervalo de anchura a lo sumo $d/2$. Esta unicidad muestra que el resultado no depende del radio inicial admitido. Si se usaron dos radios iniciales, sus intervalos coinciden a todas las escalas menores que ambos y se estrechan igual. Si $p\in D$, el valor $f(p)$ está en todas las imágenes y en todos sus intervalos, luego $F(p)=f(p)$. La fórmula de valor único define una función, no una selección entre posibles límites.

![Para p=0 y f(x)=√x en (0,1\], las imágenes de bolas de radio r≤1 son (0,√r); sus envolventes cerradas son \[0,√r\]. Se ilustran cuatro escalas exactas. Cero no es un valor de las imágenes originales, pero pertenece a todas las envolventes y es el único candidato al estrecharse. La prueba de R7 usa todas las escalas, no sólo las cuatro dibujadas.](../../assets/books/anm/C17/C17-F07.svg){#fig-anm-c17-f07 fig-alt="Para p=0 y f(x)=√x en (0,1\], las imágenes de bolas de radio r≤1 son (0,√r); sus envolventes cerradas son \[0,√r\]. Se ilustran cuatro escalas exactas. Cero no es un valor de las imágenes originales, pero pertenece a todas las envolventes y es el único candidato al estrecharse. La prueba de R7 usa todas las escalas, no sólo las cuatro dibujadas."}

**Uniformidad en el cierre.** Dada $\varepsilon>0$, tomamos $\delta>0$ uniforme para $f$ con error $\varepsilon/3$ y fijamos $\Delta=\delta/3$. Sean $p,q\in\overline D$ con $|p-q|<\Delta$. Elijamos un solo radio $0<r\le r_0$ con $r\le\delta/6$. Para cualesquiera entradas $a\in D\cap B(p,r)$ y $b\in D\cap B(q,r)$,

$$|a-b|\le|a-p|+|p-q|+|q-b|<2r+\delta/3\le2\delta/3<\delta.$$

Así todo valor de $E_{p,r}$ difiere de todo valor de $E_{q,r}$ menos que $\varepsilon/3$. La regla de cotas anterior da $U_{p,r}-L_{q,r}\le\varepsilon/3$ y $U_{q,r}-L_{p,r}\le\varepsilon/3$. Como $F(p),F(q)$ están en sus respectivos intervalos, $|F(p)-F(q)|\le\varepsilon/3<\varepsilon$. El mismo $\Delta$ sirve para todos los puntos del cierre.

**Unicidad continua.** Si $G:\overline D\to\mathbb R$ es continua y coincide con $f$ en $D$, para un $p$ fijado y $\varepsilon>0$ su continuidad da un radio en el que $|G(x)-G(p)|<\varepsilon/2$. Una escala $r$ menor que ese radio y que $r_0$ hace que $E_{p,r}$ esté dentro de esa banda; por supremo e ínfimo, también $F(p)$ está en la banda cerrada correspondiente. Luego $|F(p)-G(p)|\le\varepsilon/2<\varepsilon$. Como esto vale para todo $\varepsilon>0$, son iguales.

La raíz en $(0,1]$ se extiende a cero con valor cero, y la identidad se extiende igualmente. La función $1/x$ no tiene extensión real continua en cero y ya falló uniformidad. En un dominio acotado, su cierre es compacto por C16; por tanto una función admite extensión continua al cierre si y sólo si es uniforme: R7 da una dirección y Heine–Cantor más restricción da la otra. No se ha empleado selección numerable ni anticipado teoría de límites uniformes de funciones.

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-017-049}

¿Qué garantiza que $E_{p,r}$ no sea vacía?

[]{#MA-MSOL-ANM-01-017-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

$p\in\overline D$: toda bola positiva centrada en $p$ toca $D$, por lo que su imagen tiene un valor.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-017-050}

¿Cómo se acotan las imágenes locales sin elegir aproximantes globales?

[]{#MA-MSOL-ANM-01-017-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

Para un $p$ fijado se usa una entrada $a$ en la bola inicial; uniformidad con error uno acota todos sus valores por $f(a)\pm1$. No se forma una familia $a_p$.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-017-051}

¿Qué corte define el valor extendido?

[]{#MA-MSOL-ANM-01-017-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

$F(p)=\sup\{L_{p,r}:0<r\le r_0\}$, con $L_{p,r}$ el ínfimo de la imagen local no vacía y acotada.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-017-052}

¿Por qué ese corte no supera ningún $U_{p,r}$?

[]{#MA-MSOL-ANM-01-017-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Para toda otra escala $s$, la imagen de la bola de radio $\min(r,s)$ es no vacía y está en ambas imágenes; así $L_{p,s}\le U_{p,r}$ y ese supremo acota todo el corte.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-017-053}

¿Qué hace único al valor entre todos los intervalos?

[]{#MA-MSOL-ANM-01-017-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Sus anchuras pueden ser menores que cualquier distancia positiva; dos valores distintos no cabrían en uno de esos intervalos suficientemente estrechos.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-017-054}

¿Por qué la extensión coincide con $f$ en $D$?

[]{#MA-MSOL-ANM-01-017-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Si $p\in D$, $f(p)$ pertenece a toda imagen local y queda entre sus ínfimos/supremos. La unicidad identifica ese valor con $F(p)$.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-017-055}

¿Qué radio uniforme sobre el cierre se obtiene en la prueba?

[]{#MA-MSOL-ANM-01-017-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Para un radio $\delta$ que controla $f$ con error $\varepsilon/3$, sirve $\Delta=\delta/3$; vecindades pequeñas de ambos puntos mantienen todos los pares cruzados dentro de $\delta$.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-017-056}

¿Se necesita una sucesión aproximante por punto de frontera?

[]{#MA-MSOL-ANM-01-017-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No. Se usan todas las imágenes locales, supremos/ínfimos y un valor único por fórmula; no se seleccionan rutas.

</details>

### Ejercicios de la sección 17.7

#### Ejercicio 31. Construir el corte de frontera

[]{#MA-EX-ANM-01-017-031}

Justifica no vacuidad/acotación de $E_{p,r}$ y que el corte $F(p)$ queda entre $L_{p,r}$ y $U_{p,r}$ para todo radio admisible. No elijas sucesiones aproximantes.

[]{#MA-SOL-ANM-01-017-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Adherencia da entrada en cada bola. Fijamos el radio uniforme $\delta_0$ para error uno y $r_0=\delta_0/4$. Para este $p$, una entrada $a$ en la bola inicial acota todas las salidas allí por $f(a)\pm1$, porque la distancia entre dos entradas de ella es menor que $2r_0<\delta_0$. Todas las imágenes menores son no vacías/acotadas. Los ínfimos forman conjunto no vacío acotado superiormente por $U_{p,r_0}$, así su supremo $F(p)$ existe. Supera cada ínfimo. Para un $r$ fijado y cualquier $s$, una salida de la imagen a escala $\min(r,s)$ da $L_{p,s}\le U_{p,r}$. Por tanto ese supremo acota todo el corte y $F(p)\le U_{p,r}$. No se seleccionó entrada por todos los puntos o radios.

</details>

#### Ejercicio 32. Anchuras que determinan un único real

[]{#MA-EX-ANM-01-017-032}

Prueba que diferencias menores que $\eta$ entre todos los valores de una imagen no vacía/acotada implican $U-L\le\eta$. Usa esto para justificar unicidad del valor extendido y coincidencia en $D$.

[]{#MA-SOL-ANM-01-017-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Para cada valor $v$, todos los valores son a lo sumo $v+\eta$, así $U\le v+\eta$. Entonces $U-\eta$ es cota inferior y no supera $L$, dando $U-L\le\eta$. Uniformidad hace arbitrariamente pequeñas estas anchuras al disminuir el radio. Dos candidatos distintos a distancia $d>0$ no caben en un intervalo de anchura a lo sumo $d/2$, por tanto el candidato es único. Si $p\in D$, $f(p)$ pertenece a cada imagen local y queda entre su ínfimo/supremo; por unicidad coincide con el corte $F(p)$.

</details>

#### Ejercicio 33. Uniformidad y unicidad de la extensión

[]{#MA-EX-ANM-01-017-033}

Completa la prueba de uniformidad de $F$ sobre $\overline D$ y de unicidad entre extensiones continuas. Declara los presupuestos y radios.

[]{#MA-SOL-ANM-01-017-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Para $\varepsilon>0$ tomamos radio $\delta$ de $f$ para error $\varepsilon/3$ y fijamos $\Delta=\delta/3$. Dados $p,q$ del cierre a distancia menor que $\Delta$, usamos $0<r\le\min(r_0,\delta/6)$. Todo par cruzado de entradas de sus bolas tiene distancia menor que $2r+\delta/3\le2\delta/3<\delta$. Las cotas de supremo/ínfimo dan $U_{p,r}-L_{q,r}\le\varepsilon/3$ y la desigualdad simétrica; los cortes entre esos extremos satisfacen error a lo sumo $\varepsilon/3<\varepsilon$. Para una extensión continua $G$, su radio en un $p$ para error $\varepsilon/2$ sitúa todas las salidas locales en la banda de $G(p)$. Sus ínfimos/supremos y el corte quedan en la banda cerrada, luego $|F(p)-G(p)|\le\varepsilon/2<\varepsilon$. Para todo $\varepsilon$ esto fuerza igualdad; no se usa uniformidad de $G$ para unicidad.

</details>

#### Ejercicio 34. Extender y no poder extender

[]{#MA-EX-ANM-01-017-034}

Determina las extensiones continuas a $[0,1]$ de identidad y raíz en $(0,1]$. Prueba que el recíproco no admite extensión real continua allí.

[]{#MA-SOL-ANM-01-017-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Identidad y raíz son uniformes en $(0,1]$, por R1, y sus extensiones tienen valor cero en la frontera: las funciones identidad y raíz ya son continuas en $[0,1]$ y coinciden en el dominio, así unicidad R7 las identifica. Si el recíproco tuviera extensión real continua $G$ con valor $c$ en cero, para error uno existiría $\rho>0$ con $|G(x)-c|<1$ para $0\le x<\rho$. Elegimos $n$ con $1/(n+1)<\min(\rho,1)$ y $n+1>|c|+1$. Entonces $G(1/(n+1))=n+1$ tiene diferencia respecto de $c$ mayor que uno, contradicción. Sólo se usan entradas positivas válidas y un valor finito propuesto en la frontera.

**Retorno visual.** Véase [C17-F07](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 35. Uniformidad en un dominio acotado

[]{#MA-EX-ANM-01-017-035}

Para $D\subseteq\mathbb R$ acotado, prueba que $f:D\to\mathbb R$ es uniforme si y sólo si admite extensión continua al cierre. Trata vacío y explica el papel del cierre compacto.

[]{#MA-SOL-ANM-01-017-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

La dirección uniforme a extensión continua es R7, incluso vacío. Recíprocamente, el cierre es cerrado y sigue acotado: si $D\subseteq[-M,M]$, su cierre está en ese cerrado. Heine–Borel lo hace compacto; una extensión continua $G$ sobre él es uniforme por R3, y su restricción $f$ lo es por R1. Para vacío sólo hay función vacía y extensión vacía. La compacidad se usa en esta recíproca sobre dominio acotado; existencia R7 no exigía acotación global del dominio.

</details>
## 17.8. Datos finitos y aproximaciones poligonales

[]{#MA-SEC-ANM-01-017-008}

El radio común permite elegir un número finito de muestras que controle también lo que ocurre entre ellas. No pretendemos reconstruir una función arbitraria exactamente, ni evaluar computablemente todos sus valores: probaremos existencia de una aproximación finita con error certificado.

**R8. Aproximación poligonal de una continua en un segmento.** Sea $f:[a,b]\to\mathbb R$ continua, $a<b$, y $\varepsilon>0$. R3 proporciona $\delta>0$ uniforme con tolerancia $\varepsilon/2$. Por arquimedianidad elegimos un entero $n\ge1$ tal que

$$h=\frac{b-a}{n}<\delta.$$

Definimos nodos $t_j=a+jh$, $0\le j\le n$. En cada celda $[t_j,t_{j+1}]$, la función interpolante es

$$P(x)=(1-\theta)f(t_j)+\theta f(t_{j+1}),
\qquad \theta=\frac{x-t_j}{h}\in[0,1].$$

En un nodo compartido ambas fórmulas dan el mismo valor $f(t_j)$, así la regla define una función sobre todo el segmento. Cada rama es afín continua, y el pegado finito sobre segmentos cerrados relativos, demostrado en C14, hace continua a $P$.

Para $x$ en esa celda, sus distancias a ambos nodos son a lo sumo $h<\delta$. Entonces ambas diferencias $|f(t_j)-f(x)|$ y $|f(t_{j+1})-f(x)|$ son menores que $\varepsilon/2$. Por combinación convexa y desigualdad triangular,

$$|P(x)-f(x)|
\le(1-\theta)|f(t_j)-f(x)|+\theta|f(t_{j+1})-f(x)|
<\varepsilon/2.$$

La última desigualdad también vale si un peso es cero: el otro es uno y su error mantiene la cota estricta. Por C16, la continua $|P-f|$ alcanza máximo en el segmento; su máximo es menor que $\varepsilon/2$ y, por tanto, menor que $\varepsilon$. Sin invocar la consecución de ese máximo, el supremo de errores ya sería a lo sumo $\varepsilon/2<\varepsilon$. Para $a=b$, la constante con valor $f(a)$ da error cero. En el segmento vacío la afirmación es vacía.

![La poligonal interpola x² en los nodos 0,1/4,1/2,3/4,1. En cada celda, P(x)−x²=(x−t)(t+1/4−x) y el máximo es 1/64, alcanzado en 1/8,3/8,5/8,7/8. El cálculo es algebraico, sin derivadas ni convexidad futura. Para una continua general, el radio uniforme da existencia de una malla suficientemente fina, sin promesa de evaluación computable.](../../assets/books/anm/C17/C17-F08.svg){#fig-anm-c17-f08 fig-alt="La poligonal interpola x² en los nodos 0,1/4,1/2,3/4,1. En cada celda, P(x)−x²=(x−t)(t+1/4−x) y el máximo es 1/64, alcanzado en 1/8,3/8,5/8,7/8. El cálculo es algebraico, sin derivadas ni convexidad futura. Para una continua general, el radio uniforme da existencia de una malla suficientemente fina, sin promesa de evaluación computable."}

**Certificado exacto para el cuadrado.** En $[0,1]$, tomando $f(x)=x^2$ y una malla de paso $h=1/n$, dentro de una celda con extremo izquierdo $t$ y $x=t+\theta h$, la expansión algebraica da

$$P(x)-x^2=\theta(1-\theta)h^2
=(x-t)(t+h-x)\ge0.$$

Como $(2\theta-1)^2\ge0$, $\theta(1-\theta)\le1/4$. El error máximo exacto es $h^2/4$, alcanzado en el medio de cada celda. Para $n=4$ es $1/64$. No se usaron derivadas, convexidad como teorema futuro ni fórmulas de error que requieran segundas derivadas.

La malla funciona por el radio uniforme, no por proximidad a un centro privilegiado. Una lista finita de muestras sin una hipótesis que controle lo que pasa entre nodos no da una garantía de error: entre dos nodos de una lista se puede insertar un pico triangular continuo, de altura arbitraria, que vale cero en todos ellos. R3 garantiza una escala para cada función dada; no un radio común para todas las continuas sin más restricciones.

El capítulo deja tres formas de leer la misma disciplina: elegir el radio antes de los pares, reducir una cubierta con margen antes de tomar mínimos, y transportar un presupuesto de salida hacia una escala de entrada. Las consecuencias —operaciones, rutas, frontera y aproximación finita— declaran qué hipótesis gastan. La diferenciabilidad del siguiente capítulo añadirá otra herramienta local; ninguna prueba actual depende de ella.

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-017-057}

¿Qué condición cumple el paso de la malla?

[]{#MA-MSOL-ANM-01-017-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

$h=(b-a)/n<\delta$, donde $\delta$ es el radio uniforme para el presupuesto $\varepsilon/2$ y $n\ge1$.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-017-058}

¿Por qué coinciden las fórmulas de dos celdas en un nodo?

[]{#MA-MSOL-ANM-01-017-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

Una da peso uno al extremo derecho y la otra peso uno al extremo izquierdo; ambas dan el valor de $f$ en el nodo común.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-017-059}

¿Qué mantiene a $\theta$ entre cero y uno?

[]{#MA-MSOL-ANM-01-017-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

$x\in[t_j,t_{j+1}]$ y $h>0$, por lo que $0\le x-t_j\le h$ y $\theta=(x-t_j)/h\in[0,1]$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-017-060}

¿Cómo se controla el error entre las muestras?

[]{#MA-MSOL-ANM-01-017-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

Ambos extremos distan a lo sumo $h<\delta$ de $x$; sus errores son menores que $\varepsilon/2$ y la combinación convexa mantiene esa cota.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-017-061}

¿Por qué el pegado poligonal es continuo?

[]{#MA-MSOL-ANM-01-017-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

Cada rama afín lo es, sus valores coinciden en nodos y C14 permite el pegado finito sobre las celdas cerradas relativas.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-017-062}

¿Cuál es el error máximo del cuadrado con cuatro celdas iguales?

[]{#MA-MSOL-ANM-01-017-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

$h=1/4$, por lo que $h^2/4=1/64$, alcanzado en los medios de cada celda.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-017-063}

¿Por qué muestras finitas sin escala no dan error certificado?

[]{#MA-MSOL-ANM-01-017-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

Entre dos nodos se puede insertar un pico triangular continuo de altura arbitraria que siga valiendo cero en todos los nodos.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-017-064}

¿Qué aproximante sirve en un segmento degenerado?

[]{#MA-MSOL-ANM-01-017-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

La constante con valor $f(a)$ en $[a,a]$ tiene error cero; no se divide por una longitud de malla cero.

</details>

### Ejercicios de la sección 17.8

#### Ejercicio 36. Construir la poligonal

[]{#MA-EX-ANM-01-017-036}

Para una continua $f:[a,b]\to\mathbb R$, $a<b$, construye $P$ y prueba existencia de malla, coincidencia en nodos y continuidad. No uses derivadas.

[]{#MA-SOL-ANM-01-017-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Heine–Cantor para error $\varepsilon/2$ da $\delta>0$. Arquimedianidad permite un entero $n\ge1$ con $(b-a)/n<\delta$. Con $h=(b-a)/n$ y $t_j=a+jh$, definimos en cada celda $P(x)=(1-\theta)f(t_j)+\theta f(t_{j+1})$, $\theta=(x-t_j)/h$. En el extremo derecho $\theta=1$ y en el izquierdo de la siguiente celda $\theta=0$, por lo que ambas ramas dan el valor del nodo compartido. Cada rama afín es continua; las celdas forman cubierta finita por cerrados relativos y C14 da continuidad del pegado. Se usaron sólo los valores finitos en los nodos y no una capacidad computable de evaluarlos.

</details>

#### Ejercicio 37. Controlar todo lo que queda entre nodos

[]{#MA-EX-ANM-01-017-037}

Prueba la cota uniforme de error de R8, incluidos pesos cero y la diferencia entre error puntual, supremo y máximo.

[]{#MA-SOL-ANM-01-017-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Dentro de una celda, ambos extremos distan a lo sumo $h<\delta$ de $x$; los dos errores de $f$ son menores que $\varepsilon/2$. La triangular para su combinación con pesos no negativos de suma uno da error menor que $\varepsilon/2$, también si un peso es cero porque el otro es uno. Por tanto el supremo de errores es a lo sumo $\varepsilon/2<\varepsilon$. Además $|P-f|$ es continua en compacto no vacío y alcanza máximo por C16; como es uno de los errores puntuales, ese máximo es incluso menor que $\varepsilon/2$. En el degenerado se toma constante y no se divide por cero.

</details>

#### Ejercicio 38. Certificado exacto de cuatro celdas

[]{#MA-EX-ANM-01-017-038}

Para $x^2$ en $[0,1]$, interpola con cuatro celdas iguales. Calcula el error máximo y todos los puntos donde se alcanza, por álgebra.

[]{#MA-SOL-ANM-01-017-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Con $h=1/4$ y $x=t+\theta h$, expandir la interpolación de los cuadrados de los extremos y restar $(t+\theta h)^2$ da $\theta(1-\theta)h^2$. Es no negativo y a lo sumo $h^2/4=1/64$, porque $(2\theta-1)^2\ge0$. La igualdad exige $\theta=1/2$. Los cuatro medios son $1/8,3/8,5/8,7/8$, y en cada uno se alcanza $1/64$. No se emplea teoría diferencial ni convexidad futura.

**Retorno visual.** Véase [C17-F08](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 39. Muestras iguales y errores arbitrarios

[]{#MA-EX-ANM-01-017-039}

Dada una malla finita en $[a,b]$ con $a<b$, construye una función continua que valga cero en todos sus nodos y alcance una altura prescrita $H>0$ entre dos de ellos. Explica qué garantía falta.

[]{#MA-SOL-ANM-01-017-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Elegimos una celda de longitud positiva $[u,v]$ entre nodos consecutivos y su medio $m=(u+v)/2$. Fuera de ella ponemos cero; en $[u,m]$ ponemos $H(x-u)/(m-u)$ y en $[m,v]$ ponemos $H(v-x)/(v-m)$. Los denominadores son positivos y las ramas coinciden en valores cero en los extremos y $H$ en el medio. El pegado finito C14 da continuidad, y todos los nodos siguen teniendo valor cero. La poligonal interpolante es cero y su error en $m$ es $H$, arbitrario. Los datos de muestras sin una escala para la función entre ellas no certifican error; Heine–Cantor da escala para cada función dada, no para toda la clase con la misma malla.

</details>

#### Ejercicio 40. Elegir una malla a partir de tolerancia

[]{#MA-EX-ANM-01-017-040}

Para $x^2$ en $[0,1]$, da una condición en $n$ que asegure error poligonal estrictamente menor que $\varepsilon>0$. Compárala con usar sólo el control Lipschitz dos y presupuesto $\varepsilon/2$.

[]{#MA-SOL-ANM-01-017-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

El certificado exacto da máximo $1/(4n^2)$, así basta $n>1/(2\sqrt\varepsilon)$ con $n\ge1$. La raíz de $\varepsilon$ es positiva; arquimedianidad garantiza tal entero. Si sólo usamos Lipschitz dos, para error local $\varepsilon/2$ podemos tomar $\delta=\varepsilon/4$, y R8 pide $1/n<\varepsilon/4$, es decir $n>4/\varepsilon$. Ambas condiciones son suficientes, pero la exacta aprovecha la regla algebraica del cuadrado y puede usar muchas menos celdas. No se concluye que esa mejora exista para una continua arbitraria.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-17)

[← Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Capítulo 18 →](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html)
