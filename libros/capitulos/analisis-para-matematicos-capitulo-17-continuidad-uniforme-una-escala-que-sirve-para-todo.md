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
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C17.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-17)

Para el cuadrado, la identidad $|x^2-y^2|=|x-y||x+y|$ muestra por qué el dominio importa al controlar un error. En un segmento acotado podemos poner una barrera al segundo factor y obtener una escala de entrada que sirva para cualquier par; en toda la recta, ese factor puede amplificar separaciones arbitrariamente pequeñas. La continuidad en cada centro permite adaptar el radio al lugar donde estamos. La continuidad uniforme exige fijarlo antes de conocer cualquiera de las dos entradas.

Los prerrequisitos centrales son continuidad de C14 y compacidad de C16. Supremo e ínfimo de C00, adherencia de C04, sucesiones de C06, Cauchy y raíces de C10 y tipos de C12 son interfaces heredadas. La prueba de Heine–Cantor usa una cubierta de todos los pares centro-radio admisibles y finitud, sin seleccionar radios por todos los puntos ni fabricar rutas. Las recíprocas secuenciales se declaran condicionales a CC(R) o a una enumeración dada. La extensión al cierre se construye por cortes de imágenes locales y la aproximación poligonal por una malla finita. No usamos derivadas, integrales ni teoría de límites uniformes de funciones.

## 17.1. Un radio antes de conocer los dos puntos

[]{#MA-SEC-ANM-01-017-001}

En la continuidad de C14 fijábamos un centro y buscábamos un radio para comparar sus valores cercanos con la salida central. Al cambiar de centro podíamos cambiar de radio. Para obtener un control simultáneo de la función en todo su dominio necesitamos invertir ese orden: dada la precisión de salida, encontrar una escala que siga sirviendo al desplazarnos de un lugar a otro. Tanto la función como el dominio forman parte del problema.

**Definición.** Para $f:D\to\mathbb R$, la continuidad uniforme en $D$ significa

$$\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in D:
|x-y|<\delta\Longrightarrow|f(x)-f(y)|<\varepsilon.$$

La función y el dominio están fijados antes de pedir la precisión $\varepsilon$. El radio puede depender de esos datos, pero debe quedar elegido antes de $x,y$. En continuidad puntual, el orden $\forall a\in D\;\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D$ permite usar el centro $a$ al construirlo. Un radio uniforme satisface esa obligación puntual al tomar $y=a$; también sirve para cualquier restricción, pues todos los pares del subconjunto siguen siendo pares de $D$. Si $D$ es vacío, no hay pares que verificar y $\delta=1$ sirve para cualquier tolerancia.

**Negación.** Fallar la uniformidad significa que existe **una** tolerancia $\varepsilon_0>0$ tal que, para **todo** $\delta>0$, hay $x,y\in D$ con

$$|x-y|<\delta,\qquad |f(x)-f(y)|\ge\varepsilon_0.$$

La tolerancia infringida queda fija mientras el par puede cambiar con cada radio propuesto: las entradas se acercan tanto como se quiera y sus salidas conservan una separación positiva. Para demostrar ese fallo debemos refutar todos los candidatos comunes. Haber construido un radio local dependiente del centro sólo describe una forma de probar continuidad; todavía podría existir otro radio que sirviera en todo el dominio.

**R1. Controles algebraicos.** Si $|f(x)-f(y)|\le L|x-y|$ en todo $D$, con una constante $L\ge0$, llamamos a $f$ Lipschitz. Cuando $L>0$, $\delta=\varepsilon/L$ da uniformidad; cuando $L=0$, todas las diferencias son cero y sirve cualquier radio positivo. Por ejemplo, $f(x)=ax+b$ en $\mathbb R$ tiene constante $|a|$. El valor absoluto tiene constante uno por la desigualdad triangular inversa.

Para $q(x)=x^2$ en $[-M,M]$, $M>0$,

$$|q(x)-q(y)|=|x-y||x+y|\le2M|x-y|.$$

La barrera $2M$ convierte así $\varepsilon/(2M)$ en un radio uniforme sobre el segmento. Al pasar a toda la recta podemos compensar una separación pequeña con una entrada grande. Fijamos $\varepsilon_0=1$ y, dado cualquier $\delta>0$, tomamos $h=\min(\delta/2,1)>0$, $x=1/h$ e $y=x+h$. Si $\delta\le2$, tenemos $h=\delta/2<\delta$; si $\delta>2$, tenemos $h=1<\delta$. En ambos casos,

$$y^2-x^2=h(2x+h)=2+h^2>1.$$

Cada candidato $\delta$ admite, por tanto, un par que infringe la misma tolerancia uno. Esto demuestra el fallo de uniformidad en la recta, aunque el cuadrado siga siendo continuo en cada punto por C14.

![En \[−1,1\], la identidad de diferencia de cuadrados da radio 1/2 para tolerancia 1. En la recta, el par 4 y 17/4 tiene distancia 1/4 y error 33/16, y refuta ese candidato. La prueba general de R1/E002 produce testigos para todo radio: un solo gráfico no refuta todos los candidatos.](../../assets/books/anm/C17/C17-F01.svg){#fig-anm-c17-f01 fig-alt="Dos ventanas de la parábola, una en el segmento acotado y otra en entradas grandes; se compara una distancia pequeña con una diferencia de salida mucho mayor."}

Un control uniforme también puede depender de la escala de forma no lineal. La raíz cuadrada ofrece un ejemplo en todo el semieje no negativo. Para $x\ge y\ge0$, escribimos $a=\sqrt{x}$ y $b=\sqrt{y}$; el orden de las raíces da $a\ge b$, de donde

$$(a-b)^2\le(a-b)(a+b)=x-y.$$

Al intercambiar las entradas cubrimos el otro orden y obtenemos $|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}$ en $[0,\infty)$. El radio $\delta=\varepsilon^2$ controla cualquier par, incluido uno con entrada cero. Sin embargo, una constante Lipschitz $L>0$ en $[0,1]$ exigiría, al comparar $x>0$ con cero, que $1/\sqrt{x}\le L$. La entrada $x=1/(n+1)^2$, con $n+1>L$, contradice esa cota. Tampoco sirve $L=0$, porque la raíz no es constante. La uniformidad admite, pues, este control cuadrático aun cuando falle el lineal; sólo hemos usado las raíces y sus reglas de orden y álgebra de C10.

### Ejercicios de la sección 17.1

[]{#ejercicios-17}

#### Ejercicio 1. El orden de los cuantificadores

[]{#MA-EX-ANM-01-017-001}

Escribe continuidad puntual, uniformidad y negación de uniformidad para $f:D\to\mathbb R$. Explica qué variables puede conocer cada radio y trata el vacío.

[]{#MA-SOL-ANM-01-017-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Puntual: $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$, distancia menor que $\delta$ implica error respecto de $a$ menor que $\varepsilon$. Uniforme: $\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in D$ con la implicación de R1. En la primera el radio puede depender del centro; en la segunda se fija antes de los dos puntos. Negación: existe $\varepsilon_0>0$ tal que todo $\delta>0$ admite un par con distancia menor que $\delta$ y error al menos $\varepsilon_0$. Función y dominio están fijados en los tres casos. En el vacío la uniformidad es vacía y su negación es falsa, porque no existen pares.

La negación uniforme fija una sola precisión infringida y permite que las entradas cambien después de cada radio. En continuidad puntual se fija además el centro antes de diseñar la escala. Por eso no se niegan las dos propiedades con los mismos testigos. En el vacío, la existencia de una pareja infractora es imposible y toda escala positiva satisface el control.

</details>

#### Ejercicio 2. Un radio dependiente no refuta otro posible

[]{#MA-EX-ANM-01-017-002}

Una prueba de continuidad de $x^2$ produce radios dependientes del centro y concluye que no hay radio uniforme. Diagnostica el fallo y prueba la conclusión correcta en $\mathbb R$ con testigos para cada radio. Contrasta $[-M,M]$.

[]{#MA-SOL-ANM-01-017-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Que una construcción dependa del centro no excluye otras construcciones independientes. Para refutar uniformidad fijamos $\varepsilon_0=1$; dado $\delta>0$, sea $h=\min(\delta/2,1)>0$, $x=1/h$, $y=x+h$. Si $\delta\le2$, $h=\delta/2<\delta$; si $\delta>2$, $h=1<\delta$. El error es $h(2/h+h)=2+h^2>1$. Estos testigos sí refutan todo radio común. En $[-M,M]$, $M>0$, $|x^2-y^2|\le2M|x-y|$ y $\delta=\varepsilon/(2M)$ da uniformidad. Para $M=0$ el dominio es singleton y cualquier radio sirve.

**Retorno visual.** Véase [C17-F01](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El par construido depende del candidato $\delta$, como permite la negación, mientras la tolerancia uno permanece fija. La pequeña separación $h$ se compensa con la entrada grande $1/h$ y mantiene el error mayor que uno. En el dominio acotado esa compensación ya no puede crecer sin límite, pues $|x+y|\le2M$. El caso $M=0$ debe tratarse antes de dividir por esa barrera.

</details>

#### Ejercicio 3. Una escala no lineal

[]{#MA-EX-ANM-01-017-003}

Prueba uniformidad de $\sqrt{x}$ en $[0,\infty)$ sin derivadas y refuta que sea Lipschitz en $[0,1]$.

[]{#MA-SOL-ANM-01-017-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Para $x\ge y\ge0$, con $a=\sqrt{x}\ge b=\sqrt{y}$, $(a-b)^2\le(a-b)(a+b)=x-y$. Intercambiar los argumentos cubre el otro orden, así la diferencia de raíces es a lo sumo la raíz de la distancia. $\delta=\varepsilon^2$ sirve en todo el dominio. Si una constante $L>0$ diera control Lipschitz en $[0,1]$, tomar $x=1/(n+1)^2$, $y=0$ exigiría $1/(n+1)\le L/(n+1)^2$, es decir $n+1\le L$, falso para un índice grande. $L=0$ falla entre cero y uno.

La desigualdad de raíces compara cualquier par no negativo y no presupone un centro positivo. Por ello el radio cuadrático incluye cero y vale en todo el semieje. Para refutar Lipschitz en el segmento basta examinar parejas con una entrada cero: la razón error/distancia supera cualquier constante al escoger un índice grande. El mismo ejemplo distingue control uniforme de control lineal.

</details>

#### Ejercicio 4. Restricción y regreso imposible

[]{#MA-EX-ANM-01-017-004}

Prueba que uniformidad se hereda por restricción. Da una función cuya restricción a un subconjunto sea uniforme aunque ella no sea uniforme en el dominio mayor.

[]{#MA-SOL-ANM-01-017-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

El mismo radio uniforme sirve para todos los pares del subconjunto, porque también son pares del dominio original. La recíproca falla: $x^2$ en $\mathbb R$ no es uniforme por E002, pero en $[0,1]$ tiene constante Lipschitz dos. Incluso la restricción a un singleton sería uniforme sin informar sobre el resto.

Restringir elimina parejas que había que controlar, sin crear otras nuevas. Por eso el certificado uniforme anterior sigue siendo válido. La vuelta agregaría parejas sobre las que no hay información. El cuadrado permite comprobar ambas afirmaciones concretamente: la barrera del dominio pequeño funciona allí y los pares que escapan en el mayor refutan uniformidad global.

</details>

#### Ejercicio 5. Uniformidad sin compacidad ni acotación

[]{#MA-EX-ANM-01-017-005}

Para $f(x)=3x-2$ en $\mathbb R$, da un radio uniforme y determina si la imagen y el dominio son acotados o compactos. ¿Refuta Heine–Cantor?

[]{#MA-SOL-ANM-01-017-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

La diferencia de salidas es $3|x-y|$, por lo que $\delta=\varepsilon/3$ sirve. El dominio es toda la recta, no acotado ni compacto por C16. La imagen también es toda la recta: $y$ tiene entrada $(y+2)/3$, así tampoco es acotada ni compacta. No refuta Heine–Cantor: éste da compacidad como condición suficiente, no necesaria para una función particular.

La traslación menos dos desaparece al restar valores y el factor tres determina la escala. La imagen se identifica por un despeje válido para cualquier salida real, no sólo observando que la función crece. La uniformidad puede coexistir con entrada y salida no acotadas. Heine–Cantor no declara que todo dominio de una uniforme deba ser compacto.

</details>

## 17.2. Una cubierta y una escala de protección

[]{#MA-SEC-ANM-01-017-002}

La compacidad permite conservar una cubierta usando finitos miembros, pero la continuidad uniforme necesitará además mover un poco los puntos sin salir de un mismo abierto. Para conseguirlo cubriremos con bolas pequeñas cuya bola doble ya esté protegida dentro de un miembro original. Después de reducir la cubierta a finitos datos, el mínimo de sus radios reservará un margen común.

**R2. Número de Lebesgue para una cubierta dada.** Sea $K\subseteq\mathbb R$ compacto y $(U_i)_{i\in I}$ una cubierta por abiertos reales. Existe $\lambda>0$ tal que

$$\forall z\in K\;\exists i\in I:\quad
K\cap(z-\lambda,z+\lambda)\subseteq U_i.$$

La escala es común a todos los centros; el miembro de la cubierta puede variar con $z$. El enunciado no exige una función que reúna esos índices elegidos por centro. Si $K=\varnothing$, sirve $\lambda=1$ incluso cuando $I=\varnothing$, porque no hay centros que verificar. Supongamos en lo que sigue que $K$ no es vacío.

Construimos **todos** los triples admisibles

$$T=\{(a,i,r)\in K\times I\times\mathbb R_{>0}:
(a-2r,a+2r)\subseteq U_i\}.$$

Cada triple determina por fórmula el abierto $B(a,r)=(a-r,a+r)$, así que tenemos una familia definida sin escoger un radio preferido para cada centro. Para comprobar que cubre $K$, fijamos un $a\in K$: cobertura proporciona algún $i$ con $a\in U_i$, y apertura proporciona $\rho>0$ con $B(a,\rho)\subseteq U_i$. El triple $(a,i,\rho/2)$ pertenece a $T$ y su bola pequeña contiene $a$. Este testigo para el punto fijado basta para demostrar cobertura.

Aplicamos compacidad a esa familia de bolas pequeñas. Obtenemos un conjunto finito $J\subseteq T$ que todavía cubre $K$, y $J$ no puede ser vacío porque $K$ no lo es. Sus radios forman entonces un conjunto finito no vacío de reales positivos; por C16 posee un mínimo positivo, con el que definimos

$$\lambda=\min\{r:(a,i,r)\in J\}>0.$$

Para $z\in K$ hay un triple $(a,i,r)\in J$ con $|z-a|<r$. Si $w\in B(z,\lambda)$, entonces

$$|w-a|\le|w-z|+|z-a|<\lambda+r\le2r.$$

La bola ambiental completa queda dentro de $B(a,2r)\subseteq U_i$, y al recortarla por $K$ obtenemos la inclusión relativa del enunciado. El radio $\lambda$ se fijó usando sólo la cubierta finita; el triple que contiene a $z$ se utiliza después, para ese centro.

![Para K=\[0,1\] y los dos abiertos indicados, λ=1/10 sirve: se usa U1 si z≤1/2 y U2 si z>1/2. Los tres centros dibujados son ilustrativos. λ=1/5 falla en el centro 1/2, porque su bola relativa contiene 2/5 y 3/5, y ningún miembro contiene ambos. Extremos de la bola se interpretan por desigualdades estrictas del texto.](../../assets/books/anm/C17/C17-F02.svg){#fig-anm-c17-f02 fig-alt="Dos abiertos solapados y vecindades pequeñas que caben en un miembro; debajo una vecindad mayor contiene dos puntos que impiden incluirla en un solo abierto."}

El orden de estos pasos es esencial. Una familia infinita de radios positivos puede tener ínfimo cero, como ocurre con $1/(n+1)$. La compacidad entrega primero una lista finita que conserva cobertura; sólo entonces tomamos su mínimo. La protección en las bolas dobles permite trasladar ese margen desde el centro $a$ de una bola de la lista hasta cualquier $z$ que esté en su bola pequeña.

Por ejemplo, en $K=[0,1]$ la cubierta $U_1=(-1,3/5)$ y $U_2=(2/5,2)$ admite $\lambda=1/10$ para la inclusión relativa. Si $z\le1/2$, todo $w\in K$ con $|w-z|<1/10$ satisface $w<3/5$ y entra en $U_1$. Si $z>1/2$, satisface $w>2/5$ y entra en $U_2$. La desigualdad estricta protege también el caso $z=1/2$.

En un dominio no compacto puede faltar toda escala de protección. Para $D=(0,1)$, los abiertos $U_n=(1/(n+2),2)$ forman la cubierta sin subcubierta finita de C16. Dado $\lambda>0$, tomamos $0<z<\min(\lambda,1)$. La bola relativa $D\cap B(z,\lambda)$ contiene puntos positivos arbitrariamente próximos a cero y, por ello, puntos por debajo de cada umbral $1/(n+2)$. Ningún $U_n$ contiene esa bola, de modo que tampoco existe un número de Lebesgue positivo para esta cubierta.

Si recibimos una cubierta por abiertos relativos $A_i$ de un compacto $K$, el levantamiento canónico de C16, $W_i=(\mathbb R\setminus K)\cup A_i$, es abierto real y satisface $K\cap W_i=A_i$. Aplicamos R2 a la familia $W$ y recortamos su conclusión por $K$. La misma escala protege las bolas relativas dentro de los $A_i$, sin elegir representantes ambientales para cada abierto relativo.

### Ejercicios de la sección 17.2

#### Ejercicio 6. Proteger una cubierta concreta

[]{#MA-EX-ANM-01-017-006}

Para $K=[0,1]$, $U_1=(-1,3/5)$ y $U_2=(2/5,2)$, verifica que $\lambda=1/10$ es número de Lebesgue relativo. ¿Sirve $\lambda=1/5$?

[]{#MA-SOL-ANM-01-017-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Para $z\le1/2$, $w\in K$ a distancia menor que $1/10$ satisface $w<z+1/10\le3/5$, y como $w\ge0>-1$ pertenece a $U_1$. Si $z>1/2$, $w>z-1/10>2/5$ y $w\le1<2$, luego está en $U_2$. Para $\lambda=1/5$, el centro $z=1/2$ tiene bola relativa que contiene $3/5$ y $2/5$. El primero no está en $U_1$ y el segundo no está en $U_2$; ningún miembro contiene la bola. Así ese radio falla.

**Retorno visual.** Véase [C17-F02](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El corte de centros en $1/2$ permite decidir qué abierto protege la bola relativa completa. Los extremos del dominio no molestan porque las entradas de la bola siguen en $[0,1]$. Para el radio propuesto mayor, ambos testigos están estrictamente dentro de la bola de centro medio, pero cada uno refuta un miembro distinto de la cubierta. Así se descarta toda posibilidad de que alguno contenga esa bola.

</details>

#### Ejercicio 7. Familia de todos los triples

[]{#MA-EX-ANM-01-017-007}

Reconstruye R2 mostrando por qué $T$ determina una familia abierta y cubre $K$ sin escoger un triple para cada punto.

[]{#MA-SOL-ANM-01-017-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

$T$ contiene exactamente los triples $(a,i,r)$ con $a\in K$, $i\in I$, $r>0$ y $B(a,2r)\subseteq U_i$. Cada triple tiene componentes únicas y determina el abierto $B(a,r)$; esto es una regla funcional, no una elección entre radios. Para un $a$ arbitrario, cobertura da un $i$ y apertura un $\rho>0$; el triple $(a,i,\rho/2)$ pertenece a $T$ y su bola contiene $a$. La prueba establece cobertura punto por punto, sin definir un mapa de triples elegidos por centro.

La familia indexada por triples puede tener varias bolas con el mismo centro, y todas son admitidas si cumplen la protección doble. Para cobertura se necesita únicamente un triple para el centro fijado, obtenido de cobertura y apertura. La asignación de una bola a cada triple es una fórmula única. No es una selección de un triple preferido entre todas las posibilidades de cada centro.

</details>

#### Ejercicio 8. Tomar un ínfimo demasiado pronto

[]{#MA-EX-ANM-01-017-008}

Un argumento toma el ínfimo de todos los radios locales positivos y lo declara positivo. Repara la prueba de R2 y explica el papel de la bola doble.

[]{#MA-SOL-ANM-01-017-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Positividad de todos los miembros no da ínfimo positivo: los recíprocos $1/(n+1)$ tienen ínfimo cero. Primero se aplica compacidad a las bolas pequeñas de todos los triples admisibles, obteniendo una lista finita no vacía $J$. El mínimo de sus radios es positivo por ser uno de los miembros. Si $z$ está a distancia menor que $r$ de un centro de la lista y $|w-z|<\lambda\le r$, entonces $|w-a|<2r$. La bola doble contenida en el abierto original reserva justamente ese margen; cobertura por bolas pequeñas sola no demuestra dicha inclusión.

La familia completa incluye radios arbitrariamente pequeños en muchos ejemplos y su ínfimo puede no proteger nada. La subcubierta finita conserva cobertura y permite tomar un mínimo positivo. La doble bola se utiliza después para mover la protección al centro que se está examinando. Son dos pasos distintos: reducir los datos y reservar margen para las distancias.

</details>

#### Ejercicio 9. Levantar sin elegir ambientes

[]{#MA-EX-ANM-01-017-009}

Una cubierta de compacto se da por abiertos relativos $(A_i)$. Explica cómo obtener su número de Lebesgue sin elegir simultáneamente abiertos ambientales que representen cada $A_i$.

[]{#MA-SOL-ANM-01-017-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

C16 prueba que $W_i=(\mathbb R\setminus K)\cup A_i$ es abierto real y que $K\cap W_i=A_i$. La regla determina toda la familia por fórmula, y ésta cubre $K$. R2 da $\lambda>0$ para $W$. Para cada $z\in K$, algún $W_i$ contiene la bola relativa; al intersectar con $K$ se obtiene inclusión en $A_i$. No se seleccionó una familia de representantes ambientales. El vacío se resuelve con $\lambda=1$.

El levantamiento se define con la misma fórmula para todos los índices y no altera la selección de entradas dentro del compacto. Como $K$ es cerrado, esos levantamientos sí son abiertos reales. El número de Lebesgue ambiental protege bolas relativas en $K$, y la identidad de recorte las sitúa dentro de $A_i$. La prueba mantiene procedencia de índices y evita una familia de representantes elegidos.

</details>

#### Ejercicio 10. Una cubierta finita sin margen

[]{#MA-EX-ANM-01-017-010}

Sea $D=\{p_n=1/(n+1):n\ge0\}$. Pon $r_n=1/[4(n+1)(n+2)]$ y divide las bolas $B(p_n,r_n)$ en dos abiertos, según paridad de $n$. Prueba que cubren $D$ y que esa cubierta finita no tiene número de Lebesgue positivo.

[]{#MA-SOL-ANM-01-017-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Cada bola es abierta y contiene su centro; sus uniones pares e impares son abiertos y cubren $D$. Ninguna bola contiene otro $p_m$: para $m>n$, $p_n-p_m\ge p_n-p_{n+1}=1/[(n+1)(n+2)]=4r_n$; para $m<n$, la distancia al vecino anterior, cuando existe, es $1/[n(n+1)]>4r_n$. Así cada $p_n$ pertenece sólo al abierto de su paridad. Dado $\lambda>0$, elegimos $n$ con $p_n-p_{n+1}<\lambda$. La bola relativa centrada en $p_n$ contiene ambos puntos, de paridades opuestas, y no está contenida en ninguno de los dos abiertos. No hay escala positiva. El dominio omitió cero y no es compacto; finitud de una cubierta particular no sustituye compacidad.

Las bolas originales aíslan a sus propios puntos dentro de $D$. Eso hace que los dos abiertos asignen cada entrada exclusivamente según su paridad. Sin embargo, las distancias entre vecinos de distinta paridad tienden a cero. Cualquier escala positiva admite una bola relativa que contiene dos vecinos y no cabe en ninguno de los dos miembros. La cubierta es finita, pero el dominio no es compacto.

</details>

## 17.3. Heine–Cantor: reducir antes de tomar el mínimo

[]{#MA-SEC-ANM-01-017-003}

**R3. Heine–Cantor.** Si $f:D\to\mathbb R$ es continua en cada punto de un compacto $K\subseteq D$, relativamente a $D$, su restricción $h:K\to\mathbb R$ es uniformemente continua. No hace falta que $D$ sea compacto ni que $K$ sea intervalo.

La restricción es continua por C14. Fijada $\varepsilon>0$, necesitamos un radio anterior a cualquier par de puntos de $K$. Si $K$ es vacío, sirve $\delta=1$. Para $K$ no vacío, la continuidad ofrece controles locales con error $\varepsilon/2$; los reuniremos todos y reservaremos una bola doble para poder comparar dos salidas con el mismo valor central:

$$T_\varepsilon=\{(a,r)\in K\times\mathbb R_{>0}:
\forall z\in K,\ |z-a|<2r\Longrightarrow|h(z)-h(a)|<\varepsilon/2\}.$$

La familia $B(a,r)$ indexada por $T_\varepsilon$ cubre $K$. En efecto, para un centro $a$ fijado, continuidad con tolerancia $\varepsilon/2$ da $\rho>0$, y el par $(a,\rho/2)$ es admisible y contiene su centro en la bola pequeña. La relación que define $T_\varepsilon$ incluye todos esos controles posibles; verificar cobertura de esta manera no requiere construir una función $a\mapsto r_a$.

Compacidad entrega un $J\subseteq T_\varepsilon$ finito que cubre $K$ mediante las bolas pequeñas. Es no vacío, y

$$\delta=\min\{r:(a,r)\in J\}>0.$$

Con el radio ya fijado, sean $x,y\in K$ tales que $|x-y|<\delta$. Alguna bola pequeña de la lista contiene $x$, de modo que para cierto $(a,r)\in J$ tenemos $|x-a|<r$. El punto $y$ puede quedar fuera de ella; la protección disponible está en la doble, y la triangular da precisamente

$$|y-a|\le|y-x|+|x-a|<\delta+r\le2r.$$

Ambos puntos pertenecen a la bola doble relativa donde el mismo par $(a,r)$ controla las salidas respecto de $h(a)$. La comparación a través de ese valor central consume las dos mitades del error:

$$|h(x)-h(y)|\le|h(x)-h(a)|+|h(a)-h(y)|
<\varepsilon/2+\varepsilon/2=\varepsilon.$$

Este $\delta$ sirve para todo par de $K$ y demuestra la uniformidad de $h$. La prueba usó una familia de bolas definida por fórmula, una reducción finita y su mínimo; no recurrió a compacidad secuencial ni a seleccionar rutas o radios para todos los centros.

![Esquema con a=0, r=1, δ=3/5, x=4/5 e y=13/10. El par tiene distancia 1/2<δ; y queda fuera de la bola pequeña pero dentro de la doble. Cada índice admisible asegura error menor que ε/2 respecto de f(a) en toda la bola doble relativa. La geometría representa el paso de la prueba, no una función particular.](../../assets/books/anm/C17/C17-F03.svg){#fig-anm-c17-f03 fig-alt="Una bola pequeña dentro de otra de radio doble; x está en la pequeña e y fuera de ella, pero su distancia mutua es menor que el radio común y ambos están en la grande."}

**Segunda lectura mediante R2.** Para cada $a\in K$, definimos $A_a=\{z\in K:|h(z)-h(a)|<\varepsilon/2\}$. Continuidad hace abiertos relativos estos conjuntos, y $a\in A_a$ demuestra que cubren $K$. Los levantamos por $W_a=(\mathbb R\setminus K)\cup A_a$ y aplicamos R2 para obtener $\lambda>0$. Dados $x,y\in K$ con $|x-y|<\lambda$, algún $A_a$ contiene toda la bola relativa de centro $x$; en particular contiene tanto a $x$ como a $y$. Las dos salidas distan menos que $\varepsilon/2$ de $h(a)$ y la triangular concluye. El número de Lebesgue concentra en una propiedad de la cubierta el margen que antes construimos con bolas dobles.

Heine–Borel de C16 permite aplicar el resultado a cualquier cerrado acotado real: segmentos, conjuntos finitos, compactos con varias piezas y conjuntos de recíprocos con su límite. La compacidad garantiza uniformidad para toda función continua en ese dominio. Una función particular puede tener una estimación uniforme en un dominio mayor, como la identidad en $\mathbb R$, cuyo radio es $\delta=\varepsilon$ aunque la recta no sea compacta.

Acotación sola no asegura la garantía: $1/x$ en $(0,1]$ es continua pero falla la uniformidad. En efecto, para $x_n=1/(n+2)$, $y_n=1/(n+3)$,

$$|x_n-y_n|=\frac1{(n+2)(n+3)}\longrightarrow0,
\qquad |1/x_n-1/y_n|=1.$$

Para cualquier radio positivo, arquimedianidad permite encontrar un índice con distancia de entrada menor que él, mientras el error de salida sigue siendo uno. El extremo omitido impide aplicar Heine–Borel a este dominio acotado. La recta, por su parte, es cerrada, pero el cuadrado ya mostró que cerradura sin acotación tampoco garantiza uniformidad. En ambos ejemplos contamos con pares infractores explícitos.

### Ejercicios de la sección 17.3

#### Ejercicio 11. Las dos bolas del mismo índice

[]{#MA-EX-ANM-01-017-011}

En R3, justifica todas las condiciones que llevan de un par $|x-y|<\delta$ al error menor que $\varepsilon$. ¿Por qué no basta decir que ambos están en la misma bola pequeña?

[]{#MA-SOL-ANM-01-017-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

La lista finita cubre $x$ con $B(a,r)$ y tiene $\delta\le r$. Entonces $|x-a|<r<2r$ y $|y-a|\le|y-x|+|x-a|<\delta+r\le2r$. El segundo punto puede estar fuera de $B(a,r)$, pero ambos cumplen la condición del índice en $B(a,2r)\cap K$, así sus salidas distan menos que $\varepsilon/2$ de $h(a)$. La triangular da error menor que $\varepsilon$. Afirmar pertenencia a la bola pequeña para $y$ gastaría una inclusión no probada.

**Retorno visual.** Véase [C17-F03](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La distancia de $y$ al centro de la bola se controla pasando por $x$, que sí está en la bola pequeña. El mínimo de radios aporta el margen para que ambos queden en la doble. Allí la admisibilidad controla cada salida respecto del mismo valor central. La suma de los dos presupuestos medios completa el error del par sin una inclusión adicional no demostrada.

</details>

#### Ejercicio 12. Uniformizar sólo la restricción

[]{#MA-EX-ANM-01-017-012}

Para $f(x)=x^2$ en $D=\mathbb R$ y $K=[-2,-1]\cup[1,2]$, aplica Heine–Cantor y da además un radio explícito. ¿Qué se puede concluir sobre todo $D$?

[]{#MA-SOL-ANM-01-017-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

$K$ es cerrado/acotado, compacto por C16, y $f$ es continua en sus puntos relativamente a $D$. R3 hace uniforme la restricción sobre $K$, sin exigir que sea intervalo. Además $|x+y|\le4$ allí, por lo que $\delta=\varepsilon/4$ controla el error. Nada de esto uniformiza todo $D$; E002 ya refuta uniformidad del cuadrado en la recta.

Las dos piezas son cerradas y acotadas, de modo que su unión es compacta aunque no sea intervalo. El radio explícito usa una cota de $|x+y|$ válida para cualquier par de $K$, incluso si sus puntos pertenecen a piezas diferentes. La conclusión corresponde a esa restricción. Los infractores que escapan en $D$ siguen siendo posibles fuera del compacto.

</details>

#### Ejercicio 13. La lectura por cubiertas de salida

[]{#MA-EX-ANM-01-017-013}

Prueba Heine–Cantor usando los abiertos relativos $A_a=\{z\in K:|h(z)-h(a)|<\varepsilon/2\}$ y R2. Declara el orden de los testigos.

[]{#MA-SOL-ANM-01-017-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Cada $A_a$ es preimagen relativa de un intervalo abierto y contiene $a$, así forman cubierta. Se levantan por $W_a=(\mathbb R\setminus K)\cup A_a$ y R2 da una escala $\lambda>0$ antes de los puntos $x,y$. Para $x\in K$, R2 proporciona un índice $a$ que contiene su bola relativa. Si $|x-y|<\lambda$, tanto $x$ como $y$ están en ella y por tanto en $A_a$. Ambos errores respecto de $h(a)$ son menores que $\varepsilon/2$, y su suma controla la diferencia. No se construye un selector $x\mapsto a_x$. Para $K$ vacío sirve cualquier radio.

Las preimágenes se definen para todos los centros por una condición de salida y quedan abiertas relativas por continuidad. El número de Lebesgue se obtiene antes del par solicitado. Para ese par se fija sólo un miembro que proteja la bola de $x$, y ésta contiene también a $y$. El índice puede variar con $x$, pero el radio no, que es la conclusión uniforme.

</details>

#### Ejercicio 14. Acotación sin frontera incluida

[]{#MA-EX-ANM-01-017-014}

Refuta uniformidad de $1/x$ en $(0,1]$ con pares dados válidos desde $n=0$. Explica qué hipótesis de Heine–Cantor falta.

[]{#MA-SOL-ANM-01-017-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Tomamos $x_n=1/(n+2)$ y $y_n=1/(n+3)$, ambos del dominio desde cero. La distancia es $1/[(n+2)(n+3)]$, tendente a cero, pero las salidas son $n+2,n+3$ y difieren uno. Para $\varepsilon_0=1$, todo radio positivo admite un índice con distancia menor, refutando uniformidad. El dominio es acotado pero no cerrado: cero es adherente y está omitido. Falta compacidad, no continuidad de la función en el dominio efectivo.

Los pares están en el dominio efectivo desde el primer término y sus diferencias se calculan exactamente. Una precisión fija uno se infringe para entradas con distancia tan pequeña como se quiera. Acotación del dominio no basta para Heine–Cantor: también hace falta cerradura para compacidad. La discontinuidad no se afirma en cero, porque cero no es una entrada del recíproco dado.

</details>

#### Ejercicio 15. Vacuidad y prueba sin rutas

[]{#MA-EX-ANM-01-017-015}

Explica dónde entra no vacuidad en el mínimo de R3 y por qué la prueba no necesita CC(R). Contrasta la demostración por pares malos de una negación.

[]{#MA-SOL-ANM-01-017-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Para $K$ no vacío, una subcubierta no puede tener conjunto de índices vacío; por ello sus radios forman conjunto finito no vacío y poseen mínimo positivo. Para $K$ vacío no se toma mínimo: $\delta=1$ satisface la condición vacía. La prueba define todos los pares admisibles, verifica cobertura con testigos individuales y usa una aplicación de compacidad seguida de datos finitos; no fabrica rutas ni selecciona radios por todos los centros. Una prueba que fabrica pares malos para cada escala necesita justificar esa selección numerable, como en la recíproca condicional de R6.

La no vacuidad de $K$ obliga a que una reducción que lo cubre contenga algún índice. Ese hecho permite el mínimo de radios positivos. Para el vacío se elige uno directamente y no se usa ese paso. La prueba por cubiertas usa existencias puntuales y un conjunto finito, mientras una ruta de pares malos exige reunir testigos para todas las escalas naturales.

</details>

## 17.4. Medir la oscilación a cada escala

[]{#MA-SEC-ANM-01-017-004}

Una vez obtenido el radio común, podemos reunir en una sola cantidad todos los errores que admite cada escala de entrada. El supremo permite hacerlo incluso cuando ningún par produce el mayor error, por lo que primero comprobaremos que el conjunto de diferencias es no vacío y acotado.

**R4. Módulo de oscilación.** Supongamos $D$ no vacío y $f:D\to\mathbb R$ acotada: $|f(x)|\le B$ con $B\ge0$. Para $t\ge0$ definimos

$$\omega_f(t)=\sup\{|f(x)-f(y)|:x,y\in D,\ |x-y|\le t\}.$$

Los pares diagonales aportan diferencia cero y la barrera de valores da $|f(x)-f(y)|\le2B$. El conjunto de la definición es, por tanto, no vacío y acotado, y C00 proporciona su supremo real. Para $D$ vacío declaramos por convención $\omega_f(t)=0$, sin atribuir un supremo real al conjunto vacío. La acotación de $f$ es suficiente para esta construcción, pero hay funciones no acotadas con módulo finito a cada escala: la identidad en $\mathbb R$ tiene $\omega(t)=t$, pues todos sus errores admitidos son a lo sumo $t$ y el par $0,t$ alcanza esa cota.

Los conjuntos de diferencias aumentan al aumentar $t$; por eso $\omega$ es no decreciente, $\omega(0)=0$, y

$$|f(x)-f(y)|\le\omega_f(t)\quad\text{si }|x-y|\le t.$$

En este marco acotado, $f$ es uniformemente continua si y sólo si $\omega_f(t)\to0$ cuando $t\downarrow0$. Para la dirección directa, dada $\varepsilon>0$, uniformidad con tolerancia $\varepsilon/2$ da $\delta>0$. Si $0<t<\delta$, todos los valores del conjunto que define $\omega(t)$ son menores que $\varepsilon/2$, por lo que

$$0\le\omega(t)\le\varepsilon/2<\varepsilon.$$

Al pasar de todos los errores a su supremo sólo conservamos una desigualdad no estricta: por ejemplo, todos los miembros de $[0,1)$ son menores que uno y su supremo es uno. El presupuesto medio deja el margen necesario. Para la recíproca, el límite proporciona $\eta>0$ tal que $\omega(t)<\varepsilon$ cuando $0<t<\eta$. Fijamos $t=\eta/2$ y $\delta=t$ antes de considerar el par; si su distancia es menor que $\delta$, también es a lo sumo $t$, y su error queda acotado por $\omega(t)<\varepsilon$.

Si $f$ es Lipschitz con constante $L$, su módulo satisface $\omega_f(t)\le Lt$. La raíz tiene $\omega(t)\le\sqrt t$ en cualquier dominio no negativo donde este módulo sea definido; son dos tipos distintos de dependencia entre escalas.

**Un módulo exacto.** Para $q(x)=x^2$ en $[0,1]$,

$$\omega_q(t)=
\begin{cases}2t-t^2,&0\le t\le1,\\1,&t\ge1.\end{cases}$$

Ordenamos un par arbitrario como $0\le v\le u\le1$ y ponemos $d=u-v\le t\le1$. Su diferencia de cuadrados satisface $u^2-v^2=d(2u-d)\le d(2-d)\le t(2-t)$; la última desigualdad se debe a $(t-d)(2-t-d)\ge0$. El par $1,1-t$ alcanza esa barrera y prueba la igualdad del módulo para $t\le1$. Cuando $t\ge1$, todos los pares están admitidos y $1,0$ alcanza la mayor diferencia, uno. La cota Lipschitz $\omega_q(t)\le2t$ sigue siendo válida a cualquier escala, aunque pierde la precisión del cálculo exacto.

Para la raíz en $[0,1]$, R1 da $\omega(t)\le\sqrt t$ y el par $t,0$ alcanza la cota si $0\le t\le1$. A partir de uno, el par $1,0$ alcanza toda la variación posible y el módulo vale uno. Así ambos módulos tienden a cero, aunque el de la raíz no admita una barrera lineal común cerca de cero.

![En \[0,1\], los módulos exactos de x² y √x son 2t−t² y √t para 0≤t≤1; después de uno ambos valen uno. La recta 2t es una cota más sencilla del módulo del cuadrado. Las fórmulas se prueban por álgebra y pares que alcanzan las cotas; las curvas sólo las representan.](../../assets/books/anm/C17/C17-F04.svg){#fig-anm-c17-f04 fig-alt="Dos curvas de módulos que parten de cero, junto a una cota lineal del cuadrado; la raíz exige una relación de escalas diferente de una cota lineal cerca de cero."}

En estos dos ejemplos los pares explícitos acreditan que los supremos se alcanzan. Para aplicar el criterio en un dominio arbitrario basta disponer del supremo y controlar su límite en cero; no necesitamos que sea máximo ni que el módulo sea continuo como función de $t$. En particular, C16 acota toda continua sobre un compacto y R3 asegura que su módulo tiende a cero.

### Ejercicios de la sección 17.4

#### Ejercicio 16. Existencia y orden del módulo

[]{#MA-EX-ANM-01-017-016}

Para $f:D\to\mathbb R$ acotada en un dominio no vacío, justifica existencia de $\omega_f(t)$, su monotonía, valor en cero y la cota de diferencias. Trata el dominio vacío.

[]{#MA-SOL-ANM-01-017-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Si $|f|\le B$, toda diferencia está entre cero y $2B$. Para cada $t\ge0$, los pares diagonales aportan cero, por lo que el conjunto es no vacío y tiene supremo. Si $s\le t$, todos los pares admitidos a escala $s$ también lo son a escala $t$, así $\omega(s)\le\omega(t)$. A escala cero sólo hay pares iguales y el módulo vale cero. Toda diferencia admitida es a lo sumo el supremo. Para vacío se define módulo cero por convención; no se atribuye un supremo real al conjunto vacío.

La cota global produce una barrera uniforme $2B$ para errores, no sólo para un par. Los pares diagonales dan no vacuidad a cada escala. El supremo domina cada diferencia sin prometer un par maximizador. La convención para el vacío se declara aparte porque completitud real no entrega un supremo del conjunto vacío.

</details>

#### Ejercicio 17. Supremo y presupuesto estricto

[]{#MA-EX-ANM-01-017-017}

Una prueba dice: «todos los errores son menores que $\varepsilon$, luego su supremo también». Repara la dirección uniforme implica módulo tendente a cero y prueba la recíproca.

[]{#MA-SOL-ANM-01-017-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

El supremo de $[0,\varepsilon)$ es $\varepsilon$, así la estrictitud no pasa así al supremo. Se pide primero error $\varepsilon/2$ a uniformidad; para $0<t<\delta$, el supremo es a lo sumo $\varepsilon/2<\varepsilon$, lo que prueba el límite cero. Recíprocamente, dado $\varepsilon$, el límite da $\eta>0$ y $\omega(t)<\varepsilon$ para $0<t<\eta$. Fijamos $t=\eta/2$ y $\delta=t$. Todo par de distancia menor que $\delta$ tiene error a lo sumo $\omega(t)<\varepsilon$. Se conserva el orden de los cuantificadores.

La definición del módulo admite distancias menores o iguales que $t$, mientras uniformidad controla distancias estrictamente menores que $\delta$. Por eso se toma $t<\delta$ al usarla. El presupuesto medio conserva margen cuando se pasa al supremo. En la recíproca se fija una escala positiva concreta con módulo pequeño antes de verificar cualquier pareja.

</details>

#### Ejercicio 18. Módulo exacto del cuadrado

[]{#MA-EX-ANM-01-017-018}

Calcula $\omega(t)$ para $x^2$ en $[0,1]$, para todo $t\ge0$. Da los pares que alcanzan cada cota y compara con $2t$.

[]{#MA-SOL-ANM-01-017-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Si $0\le v\le u\le1$, $d=u-v\le t\le1$, la diferencia es $d(2u-d)\le d(2-d)\le t(2-t)$ porque la última diferencia es $(t-d)(2-t-d)\ge0$. El par $1,1-t$ alcanza $2t-t^2$ para $0\le t\le1$. Si $t\ge1$, la diferencia no supera uno y el par $1,0$ lo alcanza. Así el módulo es $2t-t^2$ en la primera escala y uno después. Siempre está bajo $2t$; para $0<t\le1$ la mejora exacta es $t^2$.

**Retorno visual.** Véase [C17-F04](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La cota se demuestra primero para un par arbitrario ordenado, con separación $d\le t$. El factor algebraico $(t-d)(2-t-d)$ es no negativo en la escala hasta uno, lo que compara su error con el candidato exacto. Un par explícito alcanza después la cota y acredita igualdad. Más allá del diámetro del dominio ya se admiten todos los pares y el módulo queda constante en uno.

</details>

#### Ejercicio 19. Una raíz y su módulo

[]{#MA-EX-ANM-01-017-019}

Calcula el módulo exacto de $\sqrt{x}$ en $[0,1]$. Contrasta la dependencia en $t$ con la del cuadrado.

[]{#MA-SOL-ANM-01-017-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

R1 da diferencia a lo sumo $\sqrt{|x-y|}$, por tanto $\omega(t)\le\sqrt t$ para $0\le t\le1$. El par $t,0$ alcanza esa cota. Para $t\ge1$, todas las diferencias son a lo sumo uno y el par $1,0$ la alcanza. El módulo es $\sqrt t$ hasta uno y uno después. Tiende a cero, pero su cociente por $t$ es $1/\sqrt t$ cerca de cero y no admite cota lineal uniforme. El cuadrado sí tiene módulo a lo sumo $2t$.

El par que alcanza $\sqrt t$ está dentro del segmento sólo para $t\le1$, y por eso se separa la escala mayor. Allí el par de extremos ya alcanza toda la variación de salida. El módulo de la raíz tiende a cero, lo que confirma uniformidad. Su crecimiento como raíz de la escala impide una barrera lineal común cerca de cero.

</details>

#### Ejercicio 20. Valores no acotados y módulo finito

[]{#MA-EX-ANM-01-017-020}

Explica por qué no se puede concluir que una uniforme en $\mathbb R$ tiene valores acotados. Calcula el módulo de la identidad y prueba uniformidad directamente.

[]{#MA-SOL-ANM-01-017-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

La identidad tiene valores que recorren toda la recta y no están acotados. A escala $t\ge0$, las diferencias admitidas están entre cero y $t$, y el par $0,t$ alcanza $t$, así el módulo es finito e igual a $t$. Directamente, $\delta=\varepsilon$ da uniformidad. La hipótesis de acotación de R4 era suficiente para construir un módulo real global sin más análisis, no necesaria en todos los ejemplos.

El módulo examina diferencias de salida a una distancia fijada, no el conjunto de salidas individuales. Para la identidad esas diferencias nunca superan $t$ y una pareja separada exactamente $t$ alcanza la cota. Así hay módulo finito a cada escala aunque las salidas no admitan cota global. El ejemplo precisa el carácter suficiente de la hipótesis de acotación en R4.

</details>

## 17.5. Transportar tolerancias por operaciones

[]{#MA-SEC-ANM-01-017-005}

Al restar los valores de una suma podemos sumar sus errores, pero en un producto cada diferencia queda multiplicada por un valor del otro factor. Las reglas uniformes deben controlar también esos multiplicadores y, en los cocientes, la distancia del denominador a cero. Consideramos siempre las funciones sobre el mismo dominio efectivo.

**R5. Sumas y productos.** Si $f,g:D\to\mathbb R$ son uniformemente continuas, $f+g$ también: elegimos radios para error $\varepsilon/2$ en cada una y tomamos su mínimo. La desigualdad triangular suma los dos errores. Multiplicar por una constante $c$ se trata con $\varepsilon/|c|$ cuando $c\ne0$; para $c=0$ la salida es constante.

Para el producto añadimos las cotas globales $|f|\le M_f$ y $|g|\le M_g$, con $M_f,M_g\ge0$. Al separar la diferencia aparecerán esos factores como multiplicadores; por eso pedimos a ambas funciones error menor que $\eta=\varepsilon/(M_f+M_g+1)>0$ y tomamos el mínimo de sus dos radios. El uno añadido mantiene positivo el denominador aun si ambas cotas son cero. Obtenemos

$$|f(x)g(x)-f(y)g(y)|
\le |g(x)|\,|f(x)-f(y)|+|f(y)|\,|g(x)-g(y)|
\le(M_f+M_g)\eta<\varepsilon.$$

Si $M_f+M_g=0$, la diferencia es cero y la conclusión también se cumple. Hemos combinado sólo dos radios. Las cotas globales ofrecen una garantía suficiente: sin ellas, las dos identidades uniformes $f(x)=g(x)=x$ en $\mathbb R$ producen el cuadrado, que no es uniforme. Tampoco se exige acotación de ambos factores para cada producto particular, pues la identidad multiplicada por la constante uno sigue siendo uniforme.

**Recíprocos y cocientes.** Si $g$ es uniforme y $|g(x)|\ge m>0$ en $D$, entonces $1/g$ tiene exactamente ese dominio y

$$\left|\frac1{g(x)}-\frac1{g(y)}\right|
\le\frac{|g(x)-g(y)|}{m^2}.$$

Pedimos a $g$ error menor que $\varepsilon m^2$ y su radio uniforme hace menor que $\varepsilon$ la diferencia de recíprocos. Además $|1/g|\le1/m$, de modo que, si $f$ es uniforme y acotada, la regla de producto se aplica a $f$ y $1/g$ y da uniformidad de $f/g$. El margen positivo es un dato global: la identidad en $(0,1]$ nunca se anula y es uniforme, pero sus valores se aproximan a cero y su recíproco ya demostró que falla uniformidad.

En un compacto, C16 proporciona acotación para las continuas y un margen positivo para el denominador continuo sin ceros. R3 uniformiza las funciones, y las reglas anteriores justifican el cociente. Alternativamente, C14 da continuidad del cociente y R3 vuelve a aplicarse, siempre con el dominio compacto declarado.

**Composición.** Sea $f:D\to E$ uniforme y $g:E\to\mathbb R$ uniforme sobre $E$; bastaría uniformidad de $g$ en $f[D]$. Para error final $\varepsilon$, primero elegimos $\eta>0$ que controle $g$. Después elegimos $\delta>0$ que produzca error de salida menor que $\eta$ para $f$. Así

$$|x-y|<\delta\Longrightarrow|f(x)-f(y)|<\eta
\Longrightarrow|g(f(x))-g(f(y))|<\varepsilon.$$

![Para f(x)=2x en \[0,1\] y g(y)=y² en \[0,2\], el error exterior tiene cota cuatro veces la distancia. Para ε=1, sirve η=1/4 y después δ=η/2=1/8. El par de entrada 1/2,3/5 ilustra distancias 1/10,1/5 y 11/25, cada una bajo su presupuesto. Las tolerancias se eligen desde la salida final hacia la entrada.](../../assets/books/anm/C17/C17-F05.svg){#fig-anm-c17-f05 fig-alt="Tres segmentos representan el transporte de un par por duplicación y cuadrado; cada distancia queda por debajo de una barra de presupuesto, elegida empezando por el error final."}

Las funciones se evalúan de dentro hacia fuera, mientras las tolerancias se diseñan desde el error final hacia la entrada inicial. La continuidad puntual exterior sólo ofrecería radios dependientes de cada salida intermedia. Puede faltar uno común: la identidad uniforme en $\mathbb R$ seguida del cuadrado continuo tiene como composición el propio cuadrado, que no es uniforme.

Para una inyección continua sobre un compacto $K$, C16 proporciona continuidad de la inversa en $H=f[K]$ y compacidad de $H$. Al considerar la inversa como función $H\to\mathbb R$ conservamos las mismas distancias de salida, así que R3 la hace uniforme. Esta conclusión incluye compactos con varias piezas y no asegura una constante Lipschitz: el cuadrado en $[0,1]$ tiene por inversa la raíz, cuyo control uniforme cuadrático ya examinamos.

### Ejercicios de la sección 17.5

#### Ejercicio 21. Radios para una suma

[]{#MA-EX-ANM-01-017-021}

Prueba uniformidad de $af+bg$ si $f,g$ son uniformes en el mismo dominio y $a,b$ son constantes. Trata constantes cero.

[]{#MA-SOL-ANM-01-017-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Si $a\ne0$, pedimos a $f$ error menor que $\varepsilon/(2|a|)$ y obtenemos un radio; si $a=0$, el término tiene error cero y usamos radio uno para él. Hacemos lo mismo con $g,b$. El mínimo de ambos radios positivos sirve para todos los pares y la diferencia de $af+bg$ es a lo sumo la suma de los dos errores escalados, cada uno menor que $\varepsilon/2$ cuando no es cero. La suma es menor que $\varepsilon$.

Las constantes no nulas multiplican los errores y requieren dividir el presupuesto por su magnitud. Una constante cero elimina su sumando y puede recibir cualquier radio auxiliar positivo. El mínimo garantiza ambos controles antes de conocer las entradas. La triangular permite combinar los errores escalados sin suponer cotas globales de los valores de $f$ y $g$.

</details>

#### Ejercicio 22. Factores que amplifican errores

[]{#MA-EX-ANM-01-017-022}

Prueba la regla de producto bajo cotas $M_f,M_g$. Muestra que eliminar ambas cotas pierde la garantía y que no son necesarias para todo producto particular.

[]{#MA-SOL-ANM-01-017-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Pedimos errores menores que $\eta=\varepsilon/(M_f+M_g+1)$ a ambas funciones y tomamos el mínimo de sus radios. La identidad de diferencias del producto da cota $(M_f+M_g)\eta<\varepsilon$, incluidos sumandos nulos. En $\mathbb R$, ambos factores identidad son uniformes y no acotados, pero su producto cuadrado falla uniformidad. En cambio, identidad por constante uno es uniforme aunque el primer factor sea no acotado. La regla declara condiciones suficientes y el ejemplo sólo refuta una regla universal sin ellas.

La identidad de producto separa cada cambio de factor y deja un valor del otro como multiplicador. Las cotas globales y el presupuesto común impiden amplificación sin control. El uno añadido al denominador conserva positividad incluso si ambas barreras valen cero. Los dos ejemplos finales distinguen perder una garantía universal de afirmar que todo producto sin esas cotas debe fallar.

</details>

#### Ejercicio 23. Un cociente sobre dos piezas

[]{#MA-EX-ANM-01-017-023}

En $K=[-2,-1]\cup[1,2]$, sean $f(x)=x+1$ y $g(x)=x^2$. Da un radio explícito uniforme para $f/g$, usando cotas de numerador, denominador y diferencias.

[]{#MA-SOL-ANM-01-017-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

En $K$, $|f|\le3$, $g\ge1$, $|f(x)-f(y)|=|x-y|$, y $|g(x)-g(y)|\le4|x-y|$. Sea $d=|x-y|$. La identidad $f(x)/g(x)-f(y)/g(y)=(f(x)-f(y))/g(x)+f(y)(1/g(x)-1/g(y))$ da error a lo sumo $d+3\cdot4d=13d$, porque los denominadores tienen magnitud al menos uno. Por tanto $\delta=\varepsilon/13$ sirve para todos los pares, incluso en piezas distintas. El cociente está definido en todo $K$.

El margen del denominador vale uno en todas las entradas, incluidas las dos piezas. La identidad de recíprocos acota su diferencia por la del cuadrado, a lo sumo cuatro veces la distancia. El numerador tiene diferencia igual a la distancia y magnitud a lo sumo tres. Reunir ambos términos da el control trece, suficiente para un radio común sin exigir que sea óptimo.

</details>

#### Ejercicio 24. El orden inverso de tolerancias

[]{#MA-EX-ANM-01-017-024}

Sean $f:D\to E$ y $g:E\to\mathbb R$ uniformes. Prueba uniformidad de $g\circ f$ y refuta sustituir uniformidad de $g$ por continuidad puntual.

[]{#MA-SOL-ANM-01-017-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Primero uniformidad de $g$ para $\varepsilon$ da $\eta>0$. Después uniformidad de $f$ para $\eta$ da $\delta>0$. Distancia de entrada menor que $\delta$ produce salidas de $f$ a distancia menor que $\eta$, y por tanto error final menor que $\varepsilon$. Basta control de $g$ sobre $f[D]$. Si $D=E=\mathbb R$, $f$ identidad es uniforme, $g$ cuadrado es continua pero no uniforme, y la composición también es cuadrado no uniforme. La continuidad puntual exterior no da una tolerancia intermedia común.

**Retorno visual.** Véase [C17-F05](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La tolerancia intermedia debe servir para cualquier par de salidas de la interior. Continuidad puntual de la exterior permitiría que esa tolerancia cambiara al cambiar la salida central y no satisface ese requisito. La identidad seguida del cuadrado mantiene uniformidad de la interior y continuidad de la exterior, pero falla uniformidad de la composición. El ejemplo refuta exactamente la sustitución propuesta.

</details>

#### Ejercicio 25. Inversa uniforme sin control lineal

[]{#MA-EX-ANM-01-017-025}

Justifica que una inyección continua $f:K\to\mathbb R$ sobre compacto tiene inversa uniforme en su imagen. Da un ejemplo en que esa inversa no sea Lipschitz.

[]{#MA-SOL-ANM-01-017-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

C16 hace compacta $H=f[K]$ y prueba continuidad de la inversa $h:H\to K$. Retipar su salida a $\mathbb R$ conserva continuidad, por usar la misma distancia; Heine–Cantor la hace uniforme sobre $H$. El vacío también queda incluido. Para $f(x)=x^2$ sobre $[0,1]$, la inyectividad sigue del orden no negativo, su imagen es $[0,1]$ por raíces C10 y su inversa es $\sqrt y$. R1 prueba que ésta es uniforme y no Lipschitz en ese dominio.

La continuidad inversa se obtiene primero por transporte de cerrados en C16, con dominio en la imagen. Esa imagen es compacta por continuidad de la directa. Heine–Cantor añade uniformidad de la inversa allí. La raíz sobre $[0,1]$ cumple esta conclusión con radio cuadrático aunque no disponga de una constante Lipschitz.

</details>

## 17.6. Pares próximos y rutas dadas

[]{#MA-SEC-ANM-01-017-006}

**R6. Prueba mediante dos sucesiones dadas.** Si $f:D\to\mathbb R$ es uniforme y $(x_n),(y_n)$ son dos sucesiones dadas en $D$ con $|x_n-y_n|\to0$, entonces $|f(x_n)-f(y_n)|\to0$. Para $\varepsilon>0$ fijamos el radio uniforme $\delta$. La convergencia de las distancias proporciona $N$ tal que son menores que $\delta$ para $n\ge N$; desde ese índice las diferencias de salida son menores que $\varepsilon$. No hace falta que ninguna de las dos rutas converja, ni que sea acotada.

Por ejemplo, $x_n=n+1$ y $y_n=n+1+1/(n+1)$ se acercan entre sí aunque escapen al infinito. Para el cuadrado,

$$|y_n-x_n|=\frac1{n+1}\to0,
\qquad y_n^2-x_n^2=2+\frac1{(n+1)^2}\ge2.$$

Si el cuadrado fuera uniforme, R6 obligaría a que esas diferencias de salida tendieran a cero, contradiciendo la cota dos. Las rutas están dadas por fórmula y este uso de la implicación directa no requiere selección. Los pares recíprocos de R3 muestran el mismo fallo cuando las entradas se aproximan a un extremo omitido.

![Se representan n=0,1,2,4 de las rutas recíprocas dadas. La distancia de entrada es 1/\[(n+2)(n+3)\] y tiende a cero; bajo f(x)=1/x la distancia de salida es siempre uno. R6 directo refuta uniformidad; no se usa la recíproca ni selección de rutas. Muestra finita, no prueba visual de convergencia.](../../assets/books/anm/C17/C17-F06.svg){#fig-anm-c17-f06 fig-alt="Cuatro filas de pares de entrada con distancias cada vez menores y pares de salida separados siempre por una unidad."}

**Recíproca con alcance declarado.** Supongamos que toda pareja de rutas dadas en $D$ con distancia tendente a cero tiene diferencias de salida tendentes a cero. Para deducir uniformidad en un dominio arbitrario mediante el argumento siguiente usamos $\mathrm{CC}(\mathbb R)$, sólo como premisa del resultado condicional.

Si falla uniformidad, fijamos la tolerancia $\varepsilon_0>0$ de la negación. Los conjuntos

$$A_n=\{x\in D:\exists y\in D,
|x-y|<1/(n+1),\ |f(x)-f(y)|\ge\varepsilon_0\}$$

son no vacíos. Una aplicación de $\mathrm{CC}(\mathbb R)$ da una ruta $x_n\in A_n$. Definimos ahora

$$B_n=\{y\in D:|x_n-y|<1/(n+1),
|f(x_n)-f(y)|\ge\varepsilon_0\}.$$

La pertenencia $x_n\in A_n$ garantiza que cada $B_n$ es no vacío. Una segunda aplicación de $\mathrm{CC}(\mathbb R)$ proporciona $y_n\in B_n$. Hemos obtenido dos rutas cuya distancia tiende a cero mientras sus salidas permanecen separadas al menos por $\varepsilon_0$, en contradicción con la propiedad supuesta. La primera selección fija entradas que admiten compañero; la segunda fija los compañeros de esas entradas. Ambas corresponden a familias de subconjuntos reales y pertenecen sólo a esta recíproca condicional; la dirección directa y Heine–Cantor conservan sus pruebas independientes.

Si el dominio no vacío viene con una sobreyección dada $e:\mathbb N\to D$, el buen orden permite determinar los pares sin CC(R). Para cada $n$, la negación de uniformidad y la sobreyectividad garantizan índices $j,k$ que representan un par malo a escala $1/(n+1)$. Tomamos el menor $j$ que admita algún compañero y, fijado éste, el menor $k$ que satisfaga la condición. Los mínimos únicos definen ambas rutas; sus índices no tienen que ser crecientes, pues no construimos una extracción. Usamos la enumeración recibida, sin inferir una para dominios arbitrarios. El dominio vacío es uniforme por separado.

**Preservación de Cauchy.** Toda uniforme envía una sucesión de Cauchy dada a otra de Cauchy. Para $\varepsilon>0$ elegimos $\delta$ uniforme; la condición de Cauchy de entrada da un $N$ con $|x_n-x_m|<\delta$ para $n,m\ge N$, y entonces las diferencias de salida son menores que $\varepsilon$. La definición y acotación de rutas de Cauchy son interfaces de C07.

La preservación de Cauchy tampoco caracteriza uniformidad en dominios arbitrarios. Cada ruta de Cauchy en $\mathbb R$ está acotada por algún $M>0$, y la estimación $|x_n^2-x_m^2|\le2M|x_n-x_m|$ hace Cauchy a su imagen bajo el cuadrado. Esa barrera pertenece a la ruta concreta y puede variar entre rutas, mientras un radio uniforme tendría que servir para todos los pares de la recta. Las dos rutas próximas que escapan muestran el fallo de esta exigencia mayor.

### Ejercicios de la sección 17.6

#### Ejercicio 26. Rutas que no convergen

[]{#MA-EX-ANM-01-017-026}

Para $x_n=n+1$ y $y_n=n+1+1/(n+1)$, calcula las distancias de entrada y salida bajo el cuadrado. Usa sólo la dirección directa de R6 para concluir.

[]{#MA-SOL-ANM-01-017-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La distancia de entrada es $1/(n+1)$, tendente a cero. La diferencia de cuadrados es $2+1/(n+1)^2$, que nunca baja de dos y por tanto no tiende a cero. Si el cuadrado fuera uniforme, la dirección directa R6 obligaría a que esas diferencias tendieran a cero, contradicción. Ninguna ruta de entrada converge o es acotada; la dirección directa no lo exigía. Los pares están dados por fórmula desde $n=0$, sin selección adicional.

La pequeña separación compensa exactamente la entrada creciente en el término lineal de la diferencia de cuadrados. El error queda mayor o igual que dos para todos los índices. Esto infringe la consecuencia directa necesaria de uniformidad para las rutas dadas. No se necesita convergencia individual, acotación ni seleccionar testigos de conjuntos abstractos.

</details>

#### Ejercicio 27. Dos familias y dos selecciones

[]{#MA-EX-ANM-01-017-027}

Reconstruye la recíproca secuencial de R6 bajo CC(R). Identifica las dos familias reales no vacías y explica por qué Heine–Cantor no queda condicionado por esta prueba.

[]{#MA-SOL-ANM-01-017-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

El fallo de uniformidad fija $\varepsilon_0>0$. Para cada $n$, $A_n$ contiene entradas que tienen algún compañero a distancia menor que $1/(n+1)$ y error al menos $\varepsilon_0$; negación garantiza no vacuidad. CC(R) selecciona $x_n\in A_n$. Luego $B_n$ reúne los compañeros de ese $x_n$ con ambas propiedades y es no vacío; CC(R) selecciona $y_n\in B_n$. Estas rutas tienen distancia tendente a cero y salida separada, contradiciendo la propiedad de pares dada. Sólo esta recíproca usa las selecciones. Heine–Cantor fue demostrado directamente por una cubierta explícita y finitud, sin recurrir a la recíproca.

La primera familia contiene entradas que admiten algún compañero infractor; su selección no determina todavía quién es ese compañero. La segunda familia se define a partir de la primera ruta ya seleccionada y permite completar los pares. CC(R) respalda ambas funciones de términos. La prueba por cubiertas de Heine–Cantor es independiente y conserva su conclusión sin adoptar esta premisa adicional.

</details>

#### Ejercicio 28. Una enumeración de pares malos

[]{#MA-EX-ANM-01-017-028}

Supón dada una sobreyección $e:\mathbb N\to D$ no vacío. Construye los pares malos de una negación de uniformidad mediante mínimos de índices, sin CC(R).

[]{#MA-SOL-ANM-01-017-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Fijamos $\varepsilon_0$ de la negación. Para cada $n$, existe un par malo en $D$ y, por sobreyectividad, índices $j,k$ que lo representan. El conjunto de $j$ para los que existe algún $k$ malo a escala $1/(n+1)$ es no vacío; tomamos su mínimo $j_n$. Para ese índice, el conjunto de compañeros $k$ es no vacío y tiene mínimo $k_n$. Los mínimos únicos definen $x_n=e(j_n)$ y $y_n=e(k_n)$, que tienen distancia menor que $1/(n+1)$ y error al menos $\varepsilon_0$. Se usa la enumeración dada, sin inferirla para dominios arbitrarios.

La negación asegura al menos un par a cada escala, y la sobreyección representa sus dos miembros por índices. El mínimo exterior fija una primera entrada que tenga compañero y el mínimo interior fija uno para ella. No se exige que los mínimos aumenten con la escala: construyen dos rutas, no una extracción. Las cotas de distancia y error son las propiedades que esas rutas deben conservar.

</details>

#### Ejercicio 29. Preservar una ruta de Cauchy

[]{#MA-EX-ANM-01-017-029}

Prueba que una uniforme envía toda ruta de Cauchy dada a otra de Cauchy. Refuta la recíproca universal con el cuadrado en $\mathbb R$.

[]{#MA-SOL-ANM-01-017-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Para error $\varepsilon$ elegimos el radio uniforme $\delta$. La condición Cauchy de entrada da $N$ con todas las distancias entre términos posteriores menores que $\delta$; uniformidad hace todas las diferencias de salida posteriores menores que $\varepsilon$. Para el cuadrado, cada ruta Cauchy es acotada, digamos $|x_n|\le M$ con $M>0$. Entonces $|x_n^2-x_m^2|\le2M|x_n-x_m|$, que convierte su condición Cauchy de entrada en la de salida. Sin embargo el cuadrado falla uniformidad en toda la recta, por E002/E026. No se confundió una ruta acotada particular con control sobre todo el dominio.

La condición Cauchy entrega un corte que vale para todos los pares tardíos, y el radio uniforme lo transforma en control Cauchy de salida. Para el cuadrado, la barrera $M$ pertenece a la ruta concreta y puede cambiar entre rutas diferentes. Ese control individual no ofrece un radio para toda la recta. Así preservación de rutas no equivale a uniformidad global en un dominio arbitrario.

</details>

#### Ejercicio 30. Pares recíprocos y una frontera

[]{#MA-EX-ANM-01-017-030}

En $(0,1]$, usa $x_n=1/(n+2)$ y $y_n=1/(n+3)$ para comparar identidad y recíproco. ¿Qué aprende el test de pares?

[]{#MA-SOL-ANM-01-017-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La distancia de entrada es $1/[(n+2)(n+3)]\to0$. Bajo identidad la diferencia es la misma y tiende a cero, conforme a uniformidad. Bajo recíproco la diferencia vale uno para todo $n$, refutando uniformidad por R6 directo. Las dos rutas convergen a cero, que está fuera del dominio; no se evalúa el recíproco en ese punto exterior. El test controla pares dentro del dominio efectivo.

**Retorno visual.** Véase [C17-F06](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La identidad transporta la separación exactamente y su diferencia de salida tiende a cero. El recíproco transforma los mismos argumentos en naturales consecutivos con diferencia uno. El test muestra que proximidad de entradas no se transporta uniformemente para esa función. Ambas evaluaciones se realizan dentro de $(0,1]$, sin asignar un valor a la frontera ausente.

</details>

## 17.7. Completar el dominio sin seleccionar aproximantes

[]{#MA-SEC-ANM-01-017-007}

La raíz en $(0,1]$ conserva su control uniforme al acercarse a cero, aunque cero no sea una entrada original. Para una función uniforme general, las salidas de todas las entradas próximas a un punto adherente quedarán en bandas cada vez más estrechas. Usaremos los ínfimos y supremos de esas imágenes locales para definir el valor de la extensión, sin escoger aproximantes ni sucesiones por punto.

**R7. Extensión uniforme al cierre.** Toda uniforme $f:D\to\mathbb R$ admite una extensión uniforme $F:\overline D\to\mathbb R$, y ésta es la única extensión continua. Si $D$ es vacío, también lo es su cierre y la función vacía resuelve el enunciado. Supongamos $D$ no vacío.

Uniformidad para error uno da un $\delta_0>0$, que fijamos una sola vez para toda la construcción. Sea $r_0=\delta_0/4$. Para $p\in\overline D$ y $0<r\le r_0$, ponemos

$$E_{p,r}=f[D\cap B(p,r)],\qquad
L_{p,r}=\inf E_{p,r},\quad U_{p,r}=\sup E_{p,r}.$$

Adherencia garantiza una entrada en cada bola positiva y, por ello, una salida en cada $E_{p,r}$. Para probar acotación, fijamos sólo para este $p$ un $a\in D\cap B(p,r_0)$. Cualquier otra entrada $x$ de esa bola satisface $|x-a|<2r_0<\delta_0$, luego $|f(x)-f(a)|<1$. Toda la imagen inicial queda entre $f(a)-1$ y $f(a)+1$, y las imágenes de bolas menores heredan la cota. El testigo $a$ demuestra acotación para el punto considerado; no se reúne una familia $p\mapsto a_p$ para definir la extensión.

Las imágenes se anidan al disminuir $r$. El conjunto de todos los $L_{p,r}$ es no vacío y está acotado superiormente por $U_{p,r_0}$; definimos por fórmula

$$F(p)=\sup\{L_{p,r}:0<r\le r_0\}.$$

Por definición de supremo, $L_{p,r}\le F(p)$ para cada radio admisible. Para la otra cota, fijamos $r$ y consideramos cualquier $s$: la imagen a escala $\min(r,s)$ es no vacía y está contenida en ambas imágenes mayores. Uno de sus valores está por encima de $L_{p,s}$ y por debajo de $U_{p,r}$, de modo que $U_{p,r}$ domina todos los ínfimos que intervienen en el corte. Al tomar su supremo obtenemos

$$L_{p,r}\le F(p)\le U_{p,r}\qquad(0<r\le r_0).$$

**Anchura pequeña.** Dada $\eta>0$, uniformidad entrega $\delta>0$ para error $\eta$. Si $0<r\le r_0$ y $2r<\delta$, cualesquiera dos entradas de $D\cap B(p,r)$ tienen salidas a distancia menor que $\eta$. Para deducir $U_{p,r}-L_{p,r}\le\eta$ sin suponer extremos alcanzados, fijamos un valor $v$ de la imagen: todos sus valores son a lo sumo $v+\eta$, y por ello $U_{p,r}\le v+\eta$. Como esto vale para todo $v$, el real $U_{p,r}-\eta$ es cota inferior de la imagen y no supera $L_{p,r}$. Podemos hacer la anchura menor que cualquier $\varepsilon>0$ pidiendo primero $\eta=\varepsilon/2$ y reduciendo el radio.

Dos candidatos a distancia $d>0$ no pueden quedar ambos en un intervalo de anchura a lo sumo $d/2$. Por tanto, $F(p)$ es el único real que cumple todas las bandas locales. Si comenzamos con otro radio inicial admisible, las bandas coinciden a todas las escalas menores que ambos radios y fuerzan el mismo valor. Cuando $p\in D$, su salida $f(p)$ pertenece a cada imagen local y cumple esas mismas cotas; la unicidad da $F(p)=f(p)$. La fórmula determina así un único valor por punto y define una función sin selección entre límites posibles.

![Para p=0 y f(x)=√x en (0,1\], las imágenes de bolas de radio r≤1 son (0,√r); sus envolventes cerradas son \[0,√r\]. Se ilustran cuatro escalas exactas. Cero no es un valor de las imágenes originales, pero pertenece a todas las envolventes y es el único candidato al estrecharse. La prueba de R7 usa todas las escalas, no sólo las cuatro dibujadas.](../../assets/books/anm/C17/C17-F07.svg){#fig-anm-c17-f07 fig-alt="La raíz extendida a cero y cuatro intervalos cerrados cada vez menores con extremo izquierdo común en cero, que representan cotas de imágenes locales abiertas."}

**Uniformidad en el cierre.** Dada $\varepsilon>0$, tomamos $\delta>0$ uniforme para $f$ con error $\varepsilon/3$ y fijamos $\Delta=\delta/3$. Sean $p,q\in\overline D$ con $|p-q|<\Delta$. Elijamos un solo radio $0<r\le r_0$ con $r\le\delta/6$. Para cualesquiera entradas $a\in D\cap B(p,r)$ y $b\in D\cap B(q,r)$,

$$|a-b|\le|a-p|+|p-q|+|q-b|<2r+\delta/3\le2\delta/3<\delta.$$

Todos los valores de $E_{p,r}$ quedan a distancia menor que $\varepsilon/3$ de todos los de $E_{q,r}$. Fijado un valor $v$ de la segunda imagen, resulta $U_{p,r}\le v+\varepsilon/3$; al pasar después al ínfimo, $U_{p,r}-L_{q,r}\le\varepsilon/3$. Intercambiando las imágenes obtenemos $U_{q,r}-L_{p,r}\le\varepsilon/3$. Como los valores extendidos están entre sus extremos respectivos, $|F(p)-F(q)|\le\varepsilon/3<\varepsilon$. El radio $\Delta$, fijado antes de ambos puntos, demuestra uniformidad en todo el cierre.

**Unicidad continua.** Sea $G:\overline D\to\mathbb R$ continua y coincidente con $f$ en $D$. Para un $p$ fijado y $\varepsilon>0$, su continuidad proporciona un radio donde $|G(x)-G(p)|<\varepsilon/2$. Tomamos una escala $r$ menor que ese radio y que $r_0$. Todas las salidas de $E_{p,r}$ están en la banda abierta alrededor de $G(p)$; su ínfimo y su supremo quedan en la banda cerrada correspondiente y encierran a $F(p)$. De ahí $|F(p)-G(p)|\le\varepsilon/2<\varepsilon$. Al valer para todo $\varepsilon>0$, esto fuerza igualdad. Sólo se usó continuidad puntual de la extensión rival.

Las funciones identidad y raíz continuas en $[0,1]$ coinciden con sus restricciones a $(0,1]$, así que la unicidad identifica sus extensiones y da valor cero en la frontera. El recíproco no admite una extensión real continua en cero: cualquier valor finito propuesto queda fuera de una banda de radio uno para entradas recíprocas suficientemente pequeñas. Este contraste se desarrolla en E034.

Si $D$ es acotado, su cierre sigue acotado y es cerrado, luego es compacto por C16. En ese caso, admitir una extensión continua al cierre equivale a ser uniforme: R7 construye la extensión en una dirección; en la otra, Heine–Cantor uniformiza la extensión y la restricción conserva su radio. Para el vacío ambas funciones son vacías. La construcción de R7 no exigió acotación global del dominio ni selección numerable.

### Ejercicios de la sección 17.7

#### Ejercicio 31. Construir el corte de frontera

[]{#MA-EX-ANM-01-017-031}

Justifica no vacuidad/acotación de $E_{p,r}$ y que el corte $F(p)$ queda entre $L_{p,r}$ y $U_{p,r}$ para todo radio admisible. No elijas sucesiones aproximantes.

[]{#MA-SOL-ANM-01-017-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Adherencia da entrada en cada bola. Fijamos el radio uniforme $\delta_0$ para error uno y $r_0=\delta_0/4$. Para este $p$, una entrada $a$ en la bola inicial acota todas las salidas allí por $f(a)\pm1$, porque la distancia entre dos entradas de ella es menor que $2r_0<\delta_0$. Todas las imágenes menores son no vacías/acotadas. Los ínfimos forman conjunto no vacío acotado superiormente por $U_{p,r_0}$, así su supremo $F(p)$ existe. Supera cada ínfimo. Para un $r$ fijado y cualquier $s$, una salida de la imagen a escala $\min(r,s)$ da $L_{p,s}\le U_{p,r}$. Por tanto ese supremo acota todo el corte y $F(p)\le U_{p,r}$. No se seleccionó entrada por todos los puntos o radios.

La cota inicial se obtiene para un punto de frontera fijado y se conserva al reducir radios. Para comparar dos escalas se usa su mínimo, cuya imagen local no es vacía y pertenece a ambas imágenes. Eso hace que cualquier supremo local sea cota de todos los ínfimos del corte. La fórmula de $F$ se define con esas cotas, sin escoger una entrada o sucesión para cada radio.

</details>

#### Ejercicio 32. Anchuras que determinan un único real

[]{#MA-EX-ANM-01-017-032}

Prueba que diferencias menores que $\eta$ entre todos los valores de una imagen no vacía/acotada implican $U-L\le\eta$. Usa esto para justificar unicidad del valor extendido y coincidencia en $D$.

[]{#MA-SOL-ANM-01-017-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Para cada valor $v$, todos los valores son a lo sumo $v+\eta$, así $U\le v+\eta$. Entonces $U-\eta$ es cota inferior y no supera $L$, dando $U-L\le\eta$. Uniformidad hace arbitrariamente pequeñas estas anchuras al disminuir el radio. Dos candidatos distintos a distancia $d>0$ no caben en un intervalo de anchura a lo sumo $d/2$, por tanto el candidato es único. Si $p\in D$, $f(p)$ pertenece a cada imagen local y queda entre su ínfimo/supremo; por unicidad coincide con el corte $F(p)$.

Las diferencias estrictamente menores que $\eta$ producen una anchura sólo menor o igual que $\eta$ al pasar a extremos. Esa conclusión basta porque la uniformidad permite pedir un presupuesto más pequeño que la distancia entre dos candidatos. La coincidencia con $f$ utiliza además que la salida central pertenece a todas las imágenes cuando el centro está en $D$. Se demuestra existencia por el corte y unicidad por anchuras, en pasos distintos.

</details>

#### Ejercicio 33. Uniformidad y unicidad de la extensión

[]{#MA-EX-ANM-01-017-033}

Completa la prueba de uniformidad de $F$ sobre $\overline D$ y de unicidad entre extensiones continuas. Declara los presupuestos y radios.

[]{#MA-SOL-ANM-01-017-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Para $\varepsilon>0$ tomamos radio $\delta$ de $f$ para error $\varepsilon/3$ y fijamos $\Delta=\delta/3$. Dados $p,q$ del cierre a distancia menor que $\Delta$, usamos $0<r\le\min(r_0,\delta/6)$. Todo par cruzado de entradas de sus bolas tiene distancia menor que $2r+\delta/3\le2\delta/3<\delta$. Las cotas de supremo/ínfimo dan $U_{p,r}-L_{q,r}\le\varepsilon/3$ y la desigualdad simétrica; los cortes entre esos extremos satisfacen error a lo sumo $\varepsilon/3<\varepsilon$. Para una extensión continua $G$, su radio en un $p$ para error $\varepsilon/2$ sitúa todas las salidas locales en la banda de $G(p)$. Sus ínfimos/supremos y el corte quedan en la banda cerrada, luego $|F(p)-G(p)|\le\varepsilon/2<\varepsilon$. Para todo $\varepsilon$ esto fuerza igualdad; no se usa uniformidad de $G$ para unicidad.

El radio global $\Delta$ se fija antes de $p,q$ y el radio local $r$ asegura que cualquier par cruzado de sus bolas quede en la escala original. Las cotas de supremo e ínfimo conservan el error con desigualdades no estrictas, cubiertas por el presupuesto reservado. Para unicidad basta un control puntual de la otra extensión en cada $p$. Así no se exige que una extensión continua rival sea uniforme como hipótesis.

</details>

#### Ejercicio 34. Extender y no poder extender

[]{#MA-EX-ANM-01-017-034}

Determina las extensiones continuas a $[0,1]$ de identidad y raíz en $(0,1]$. Prueba que el recíproco no admite extensión real continua allí.

[]{#MA-SOL-ANM-01-017-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Identidad y raíz son uniformes en $(0,1]$, por R1, y sus extensiones tienen valor cero en la frontera: las funciones identidad y raíz ya son continuas en $[0,1]$ y coinciden en el dominio, así unicidad R7 las identifica. Si el recíproco tuviera extensión real continua $G$ con valor $c$ en cero, para error uno existiría $\rho>0$ con $|G(x)-c|<1$ para $0\le x<\rho$. Elegimos $n$ con $1/(n+1)<\min(\rho,1)$ y $n+1>|c|+1$. Entonces $G(1/(n+1))=n+1$ tiene diferencia respecto de $c$ mayor que uno, contradicción. Sólo se usan entradas positivas válidas y un valor finito propuesto en la frontera.

**Retorno visual.** Véase [C17-F07](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las extensiones conocidas conservan los valores originales y son continuas también en cero, por lo que la unicidad determina su valor de frontera. El recíproco, en cambio, produce valores que superan cualquier banda alrededor de un valor real propuesto. Arquimedianidad permite una entrada positiva dentro del radio de continuidad y con salida demasiado grande. La contradicción muestra imposibilidad de una extensión real continua, no sólo fracaso de una fórmula candidata.

</details>

#### Ejercicio 35. Uniformidad en un dominio acotado

[]{#MA-EX-ANM-01-017-035}

Para $D\subseteq\mathbb R$ acotado, prueba que $f:D\to\mathbb R$ es uniforme si y sólo si admite extensión continua al cierre. Trata vacío y explica el papel del cierre compacto.

[]{#MA-SOL-ANM-01-017-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

La dirección uniforme a extensión continua es R7, incluso vacío. Recíprocamente, el cierre es cerrado y sigue acotado: si $D\subseteq[-M,M]$, su cierre está en ese cerrado. Heine–Borel lo hace compacto; una extensión continua $G$ sobre él es uniforme por R3, y su restricción $f$ lo es por R1. Para vacío sólo hay función vacía y extensión vacía. La compacidad se usa en esta recíproca sobre dominio acotado; existencia R7 no exigía acotación global del dominio.

La existencia de extensión uniforme al cierre no necesita acotación del dominio. La acotación sí se usa al volver desde una extensión meramente continua: junto con cerradura del cierre produce compacidad y habilita Heine–Cantor. Después la restricción conserva el radio uniforme. En el vacío ambas funciones y sus dominios son vacíos y la equivalencia se resuelve directamente.

</details>

## 17.8. Datos finitos y aproximaciones poligonales

[]{#MA-SEC-ANM-01-017-008}

En un segmento podemos colocar nodos a una distancia menor que el radio uniforme. Entonces cada punto queda próximo a los dos extremos de su celda, y ambos valores de muestra aproximan su salida. Al interpolar entre ellos conservaremos ese control en toda la celda, obteniendo una aproximación definida por finitos datos con error certificado. La existencia de esos valores finitos no presupone un procedimiento computable para evaluarlos.

**R8. Aproximación poligonal de una continua en un segmento.** Sea $f:[a,b]\to\mathbb R$ continua, $a<b$, y $\varepsilon>0$. R3 proporciona $\delta>0$ uniforme con tolerancia $\varepsilon/2$. Por arquimedianidad elegimos un entero $n\ge1$ tal que

$$h=\frac{b-a}{n}<\delta.$$

Definimos nodos $t_j=a+jh$, $0\le j\le n$. En cada celda $[t_j,t_{j+1}]$, la función interpolante es

$$P(x)=(1-\theta)f(t_j)+\theta f(t_{j+1}),
\qquad \theta=\frac{x-t_j}{h}\in[0,1].$$

En un nodo compartido, la fórmula de la celda anterior da peso uno al extremo derecho y la siguiente da peso uno al izquierdo. Ambas asignan el mismo valor $f(t_j)$, así que definen una sola función $P$ sobre el segmento. Cada rama afín es continua; las celdas constituyen una cubierta finita por cerrados relativos y el pegado de C14 demuestra continuidad de $P$.

Para $x$ en esa celda, sus distancias a ambos nodos son a lo sumo $h<\delta$. Entonces ambas diferencias $|f(t_j)-f(x)|$ y $|f(t_{j+1})-f(x)|$ son menores que $\varepsilon/2$. Por combinación convexa y desigualdad triangular,

$$|P(x)-f(x)|
\le(1-\theta)|f(t_j)-f(x)|+\theta|f(t_{j+1})-f(x)|
<\varepsilon/2.$$

La cota estricta se conserva también en los nodos: cuando un peso es cero, el otro vale uno y mantiene su error menor que $\varepsilon/2$. El supremo de todos los errores es, por tanto, a lo sumo $\varepsilon/2<\varepsilon$, lo que ya certifica la aproximación global. Además $|P-f|$ es continua en el segmento compacto y alcanza su máximo por C16; ese máximo es uno de los errores puntuales y resulta incluso menor que $\varepsilon/2$. Si $a=b$, tomamos directamente la constante $f(a)$, de error cero, sin dividir por una longitud nula. En el segmento vacío la afirmación es vacía.

![La poligonal interpola x² en los nodos 0,1/4,1/2,3/4,1. En cada celda, P(x)−x²=(x−t)(t+1/4−x) y el máximo es 1/64, alcanzado en 1/8,3/8,5/8,7/8. El cálculo es algebraico, sin derivadas ni convexidad futura. Para una continua general, el radio uniforme da existencia de una malla suficientemente fina, sin promesa de evaluación computable.](../../assets/books/anm/C17/C17-F08.svg){#fig-anm-c17-f08 fig-alt="Parábola y poligonal coinciden en cinco nodos; debajo cuatro arcos de error tienen altura máxima un sesentaicuatroavo en los medios."}

**Certificado exacto para el cuadrado.** En $[0,1]$, tomando $f(x)=x^2$ y una malla de paso $h=1/n$, dentro de una celda con extremo izquierdo $t$ y $x=t+\theta h$, la expansión algebraica da

$$P(x)-x^2=\theta(1-\theta)h^2
=(x-t)(t+h-x)\ge0.$$

La identidad $(2\theta-1)^2\ge0$ da $\theta(1-\theta)\le1/4$, con igualdad exactamente cuando $\theta=1/2$. El máximo del error es así $h^2/4$ y se alcanza en el medio de cada celda. Para cuatro celdas, $h=1/4$ y el valor es $1/64$, alcanzado en $1/8,3/8,5/8,7/8$. El certificado procede de la expansión algebraica y de un cuadrado no negativo, sin recurrir a derivadas ni a un teorema posterior de convexidad.

La garantía entre nodos depende de haber elegido la malla con una escala de control de la función. Si sólo recibimos finitas muestras sobre un segmento no degenerado, podemos insertar entre dos nodos consecutivos un pico triangular continuo de altura arbitraria, manteniendo valor cero en todos los nodos. Su interpolante será cero y el error en el medio tendrá la altura del pico. Heine–Cantor proporciona una escala para cada función dada; no proporciona una sola malla que certifique el mismo error para todas las continuas con esas muestras.

### Ejercicios de la sección 17.8

#### Ejercicio 36. Construir la poligonal

[]{#MA-EX-ANM-01-017-036}

Para una continua $f:[a,b]\to\mathbb R$, $a<b$, construye $P$ y prueba existencia de malla, coincidencia en nodos y continuidad. No uses derivadas.

[]{#MA-SOL-ANM-01-017-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Heine–Cantor para error $\varepsilon/2$ da $\delta>0$. Arquimedianidad permite un entero $n\ge1$ con $(b-a)/n<\delta$. Con $h=(b-a)/n$ y $t_j=a+jh$, definimos en cada celda $P(x)=(1-\theta)f(t_j)+\theta f(t_{j+1})$, $\theta=(x-t_j)/h$. En el extremo derecho $\theta=1$ y en el izquierdo de la siguiente celda $\theta=0$, por lo que ambas ramas dan el valor del nodo compartido. Cada rama afín es continua; las celdas forman cubierta finita por cerrados relativos y C14 da continuidad del pegado. Se usaron sólo los valores finitos en los nodos y no una capacidad computable de evaluarlos.

La escala uniforme se obtiene para un presupuesto común antes de construir nodos. Una malla suficientemente fina mantiene cada celda dentro de esa escala. Las fórmulas afines comparten valores en los nodos y por ello definen una sola función. El pegado finito sobre celdas cerradas acredita continuidad sin usar derivadas ni presuponer un algoritmo de evaluación de todas las muestras.

</details>

#### Ejercicio 37. Controlar todo lo que queda entre nodos

[]{#MA-EX-ANM-01-017-037}

Prueba la cota uniforme de error de R8, incluidos pesos cero y la diferencia entre error puntual, supremo y máximo.

[]{#MA-SOL-ANM-01-017-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Dentro de una celda, ambos extremos distan a lo sumo $h<\delta$ de $x$; los dos errores de $f$ son menores que $\varepsilon/2$. La triangular para su combinación con pesos no negativos de suma uno da error menor que $\varepsilon/2$, también si un peso es cero porque el otro es uno. Por tanto el supremo de errores es a lo sumo $\varepsilon/2<\varepsilon$. Además $|P-f|$ es continua en compacto no vacío y alcanza máximo por C16; como es uno de los errores puntuales, ese máximo es incluso menor que $\varepsilon/2$. En el degenerado se toma constante y no se divide por cero.

Los pesos suman uno y no son negativos, así la interpolación combina dos errores bajo el mismo presupuesto. Los nodos, donde uno de los pesos es cero, siguen cumpliendo la estimación. Pasar al supremo sólo conserva una desigualdad no estricta, pero el presupuesto medio deja error global menor que $\varepsilon$. Si se usa que el error continuo alcanza máximo en el compacto, ese máximo también hereda la cota puntual estricta.

</details>

#### Ejercicio 38. Certificado exacto de cuatro celdas

[]{#MA-EX-ANM-01-017-038}

Para $x^2$ en $[0,1]$, interpola con cuatro celdas iguales. Calcula el error máximo y todos los puntos donde se alcanza, por álgebra.

[]{#MA-SOL-ANM-01-017-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Con $h=1/4$ y $x=t+\theta h$, expandir la interpolación de los cuadrados de los extremos y restar $(t+\theta h)^2$ da $\theta(1-\theta)h^2$. Es no negativo y a lo sumo $h^2/4=1/64$, porque $(2\theta-1)^2\ge0$. La igualdad exige $\theta=1/2$. Los cuatro medios son $1/8,3/8,5/8,7/8$, y en cada uno se alcanza $1/64$. No se emplea teoría diferencial ni convexidad futura.

**Retorno visual.** Véase [C17-F08](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La fórmula exacta cancela los términos que dependen del extremo izquierdo de la celda. Queda el mismo error según el peso $\theta$ en todas las celdas. La identidad cuadrática de $\theta(1-\theta)$ localiza la igualdad únicamente en su medio. Así se obtienen el valor máximo y todos sus argumentos, mientras en cada nodo la poligonal coincide exactamente con el cuadrado.

</details>

#### Ejercicio 39. Muestras iguales y errores arbitrarios

[]{#MA-EX-ANM-01-017-039}

Dada una malla finita en $[a,b]$ con $a<b$, construye una función continua que valga cero en todos sus nodos y alcance una altura prescrita $H>0$ entre dos de ellos. Explica qué garantía falta.

[]{#MA-SOL-ANM-01-017-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Elegimos una celda de longitud positiva $[u,v]$ entre nodos consecutivos y su medio $m=(u+v)/2$. Fuera de ella ponemos cero; en $[u,m]$ ponemos $H(x-u)/(m-u)$ y en $[m,v]$ ponemos $H(v-x)/(v-m)$. Los denominadores son positivos y las ramas coinciden en valores cero en los extremos y $H$ en el medio. El pegado finito C14 da continuidad, y todos los nodos siguen teniendo valor cero. La poligonal interpolante es cero y su error en $m$ es $H$, arbitrario. Los datos de muestras sin una escala para la función entre ellas no certifican error; Heine–Cantor da escala para cada función dada, no para toda la clase con la misma malla.

La celda de longitud positiva existe porque la malla recorre un segmento no degenerado. Sus dos mitades tienen denominadores positivos, y el acuerdo en el medio y extremos hace continua la función triangular. Ningún nodo interior de esa celda existe entre consecutivos, así todas las muestras siguen siendo cero. La altura demuestra que una malla fija no certifica el error de toda función continua que coincida en esos datos.

</details>

#### Ejercicio 40. Elegir una malla a partir de tolerancia

[]{#MA-EX-ANM-01-017-040}

Para $x^2$ en $[0,1]$, da una condición en $n$ que asegure error poligonal estrictamente menor que $\varepsilon>0$. Compárala con usar sólo el control Lipschitz dos y presupuesto $\varepsilon/2$.

[]{#MA-SOL-ANM-01-017-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

El certificado exacto da máximo $1/(4n^2)$, así basta $n>1/(2\sqrt\varepsilon)$ con $n\ge1$. La raíz de $\varepsilon$ es positiva; arquimedianidad garantiza tal entero. Si sólo usamos Lipschitz dos, para error local $\varepsilon/2$ podemos tomar $\delta=\varepsilon/4$, y R8 pide $1/n<\varepsilon/4$, es decir $n>4/\varepsilon$. Ambas condiciones son suficientes, pero la exacta aprovecha la regla algebraica del cuadrado y puede usar muchas menos celdas. No se concluye que esa mejora exista para una continua arbitraria.

El error exacto de una malla de $n$ celdas es $h^2/4=1/(4n^2)$, y la desigualdad estricta pide un entero que supere el umbral indicado. La garantía Lipschitz sólo usa una cota lineal y el presupuesto medio, por eso impone una condición más conservadora. Son dos certificados suficientes basados en información diferente. La mejora cuadrática procede de la identidad algebraica de esta función particular.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-17)

[← Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Capítulo 18 →](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html)
