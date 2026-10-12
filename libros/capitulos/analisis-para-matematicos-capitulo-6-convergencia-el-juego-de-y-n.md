---
content-id: MA-BCH-0226
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-006
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
title: 'Capítulo 6 — Convergencia: el juego de ε y N'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C06.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-6)

[]{#MA-SEC-ANM-01-006-008}

Al terminar el capítulo anterior sabíamos expresar que una cola de una sucesión queda dentro de un conjunto fijo. El centro y el tamaño de una bola, por ejemplo, se elegían antes de buscar el umbral: preguntábamos si, desde algún índice, todos los términos pertenecían a esa bola. Ese lenguaje permite controlar lo que ocurre tarde, pero aún no expresa que podamos exigir una aproximación con cualquier precisión.

Imaginemos que alguien afirma que una sucesión se aproxima a cero. Le pedimos que sus términos queden entre −1 y 1 a partir de algún índice; nos ofrece un umbral que cumple esa condición. Podemos pedir ahora una ventana menor, entre −1/10 y 1/10. La primera respuesta ya no basta: hace falta comprobar que también esa ventana captura una cola. Y ninguna de esas dos comprobaciones sustituye la obligación de responder a cualquier tolerancia positiva que se nos proponga.

C06 comienza al convertir esta exigencia en una definición. La pregunta rectora será: **¿qué control permite afirmar que una sucesión se aproxima a un número con cualquier precisión que se le exija?** Primero construiremos el lenguaje y aprenderemos a leer sus elecciones; después demostraremos qué permite hacer con las sucesiones que cumplen la definición. Las reglas de cálculo vendrán acompañadas de sus hipótesis y de las estimaciones que las justifican.

Conservamos la convención $\mathbb N=\{0,1,2,\ldots\}$. Una sucesión real es una función $a:\mathbb N\to\mathbb R$; $n$ es un índice y $a_n$ un número real. El candidato al que queremos aproximarnos será otro número real, que llamaremos $A$. El índice y el candidato tienen papeles distintos: podemos exigir índices mayores para controlar la distancia de los valores a $A$, pero $A$ permanece fijo durante toda la comprobación.

## 6.1. Una ventana para cada tolerancia

[]{#MA-SEC-ANM-01-006-001}

### De una captura fija a una familia de exigencias

Fijemos una sucesión $a:\mathbb N\to\mathbb R$ y un candidato $A\in\mathbb R$. Si nos dan una tolerancia real $\varepsilon>0$, la ventana correspondiente es la bola $B(A,\varepsilon)=(A-\varepsilon,A+\varepsilon)$ que ya conocemos. Exigir que un término esté en ella significa exactamente $|a_n-A|<\varepsilon$.

C05 nos permite decir que esa ventana captura una cola:

$$
\exists N\in\mathbb N\ \forall n\in\mathbb N,\qquad
n\ge N\Longrightarrow |a_n-A|<\varepsilon.
$$

Por ahora se trata de una sola tolerancia fijada. Para expresar la aproximación que buscamos, exigimos que esta captura pueda conseguirse **para cada** $\varepsilon>0$. La sucesión y el candidato no cambian al reducir el tamaño de la ventana; lo que puede cambiar es el umbral que necesitamos.

Esta diferencia se ve incluso en sucesiones muy sencillas. Consideremos $r_n=0$ cuando $n$ es par y $r_n=1$ cuando $n$ es impar. Todos los términos están en $B(0,2)$, de modo que esa ventana captura la sucesión desde el índice 0. Sin embargo, la ventana $B(0,1/2)$ no captura ninguna cola: tras cualquier umbral $N$ encontramos el índice impar $2N+1\ge N$, cuyo término vale 1 y queda fuera.

Hemos comprobado que una captura fija alrededor de cero no asegura capturas a todas las escalas alrededor del mismo candidato. No hemos analizado otros candidatos de esta sucesión. Esa distinción será importante cuando aprendamos a refutar afirmaciones de convergencia.

### La definición

> **Convergencia a un candidato real.** Sean $a:\mathbb N\to\mathbb R$ y $A\in\mathbb R$. Decimos que la sucesión **converge a $A$**, y escribimos $a_n\to A$, si para cada $\varepsilon>0$ existe un $N\in\mathbb N$ tal que, para todo $n\in\mathbb N$ con $n\ge N$, se cumple $|a_n-A|<\varepsilon$.

Su forma simbólica completa es

$$
a_n\to A
\quad\Longleftrightarrow\quad
\forall\varepsilon>0\ \exists N\in\mathbb N\
\forall n\in\mathbb N,\qquad
n\ge N\Longrightarrow |a_n-A|<\varepsilon.
$$

También diremos que $A$ es un límite de la sucesión cuando se cumple esta afirmación. Demostraremos en §6.4 que no puede haber dos candidatos distintos que la satisfagan; hasta entonces la expresión $a_n\to A$ designa la propiedad que acabamos de definir, sin apoyarse en una unicidad todavía no demostrada.

El signo de aproximación relaciona el comportamiento de la sucesión con un candidato. No es una igualdad entre la función $a$ y el número $A$. Tampoco introduce un término final $a_\infty$: infinito no es un índice de $\mathbb N$ y la definición sólo habla de términos de índices naturales.

La tolerancia $\varepsilon$ mide distancia en la recta de **valores**; el umbral $N$ marca un corte en el conjunto de **índices**. Pedir una precisión menor no añade índices fraccionarios ni términos intermedios. La gráfica de la sucesión sigue siendo la colección discreta de puntos $(n,a_n)$.

### Volver de los símbolos a la ventana

Leamos la definición en el orden en que impone sus obligaciones. La sucesión $a$ y el candidato $A$ están fijados. Se nos propone una tolerancia positiva $\varepsilon$; debemos encontrar un índice $N$ a partir del cual ningún término quede fuera de la ventana. Una vez elegido ese umbral, la afirmación debe valer para cualquier índice natural $n\ge N$.

No basta con señalar un término cercano ni con encontrar muchos términos cercanos. La definición exige toda la cola desde el corte elegido. En el ejemplo de $r$, los índices pares proporcionan visitas a cero tan tardías como queramos, pero los impares siguen impidiendo la captura por la ventana de radio 1/2.

El umbral puede depender de la tolerancia. La definición no pide un corte único que responda a todas las precisiones ni pide que el corte elegido sea el menor posible. Si $N$ controla una ventana y $K\ge N$, el corte $K$ también la controla: un índice $n\ge K$ satisface $n\ge N$, por lo que conserva la estimación. Esta sencilla comprobación recuerda que un testigo de captura no es necesariamente único.

La desigualdad del error es estricta. Para $A=0$ y $\varepsilon=1/3$, un término que valga $1/3$ queda sobre la frontera de la ventana y no cumple $|a_n-A|<\varepsilon$. Podrá quedar dentro de una ventana mayor, pero no de ésta. Mantendremos esa precisión al construir umbrales.

### Una representación anticipatoria

La sucesión $s_n=(-1)^n/(n+1)$ es útil para imaginar una aproximación que cambia de lado. Sus primeros términos son $1,-1/2,1/3,-1/4,\ldots$: el signo alterna mientras las magnitudes que aparecen en esta muestra disminuyen. Para conservar esa diferencia entre índice y valor, podemos leer algunos términos en una tabla:

| Índice $n$ | Término $s_n$ | Distancia a cero $\lvert s_n\rvert$ |
|---:|---:|---:|
| 0 | $1$ | $1$ |
| 1 | $-1/2$ | $1/2$ |
| 2 | $1/3$ | $1/3$ |
| 3 | $-1/4$ | $1/4$ |
| 4 | $1/5$ | $1/5$ |
| 5 | $-1/6$ | $1/6$ |
| 6 | $1/7$ | $1/7$ |
| 7 | $-1/8$ | $1/8$ |
| 8 | $1/9$ | $1/9$ |

Imaginemos tres gráficas de estos mismos puntos, con ventanas centradas en cero y radios $1/2$, $1/4$ y $1/8$. Dentro de la muestra, los puntos desde los índices 2, 4 y 8, respectivamente, satisfacen las desigualdades estrictas correspondientes. El punto de índice 7, por ejemplo, está sobre la frontera inferior de la ventana de radio $1/8$, mientras que el de índice 8 está dentro.

La tabla ayuda a leer qué exigiría una captura, pero sólo muestra nueve índices y tres tolerancias. No demuestra el control de una cola infinita para cualquier $\varepsilon>0$. En §6.3 construiremos un umbral para la sucesión $1/(n+1)$ y después verificaremos directamente este ejemplo alternante mediante la identidad $|s_n|=1/(n+1)$. Hasta entonces lo usamos como representación anticipatoria, no como herramienta de límites ya probada.

Comparemos ahora las tres ventanas sobre la misma sucesión. En la figura [C06-F01](#fig-anm-c06-f01), cambiar la tolerancia modifica la exigencia sobre los valores, mientras que el corte sigue siendo un índice natural.

### Figura [C06-F01](#fig-anm-c06-f01)

![La misma sucesión alternante se muestra con ventanas abiertas de radios 1/2, 1/4 y 1/8 y cortes 2, 4 y 8. Cada panel es una muestra finita. La prueba general se encuentra en §6.3.](../../assets/books/anm/C06/C06-F01.svg){#fig-anm-c06-f01 fig-alt="La misma sucesión alternante se muestra con ventanas abiertas de radios 1/2, 1/4 y 1/8 y cortes 2, 4 y 8. Cada panel es una muestra finita. La prueba general se encuentra en §6.3."}

**Figura [C06-F01](#fig-anm-c06-f01).** La tolerancia se impone sobre los valores y el umbral se elige sobre los índices. Cada ventana exige capturar una cola completa de la misma sucesión, aunque los términos cambien de lado. La muestra ilustra la exigencia; la garantía se demuestra en §6.3.

Los términos resaltados empiezan en los cortes 2, 4 y 8; la franja abierta actúa sobre sus alturas. Cada panel conserva la misma regla de evaluación. La garantía para cualquier tolerancia se establecerá en §6.3, sin extrapolar los puntos dibujados.

### Casos que podemos comprobar desde ahora

Una sucesión constante ofrece una comprobación completa que no necesita construir umbrales mediante desigualdades más difíciles. Si $a_n=A$ para todo $n\in\mathbb N$, recibida cualquier tolerancia $\varepsilon>0$ elegimos $N=0$. Para todo $n\ge0$, el error es $|a_n-A|=0<\varepsilon$. Por la definición, $a_n\to A$.

Aquí todos los términos coinciden con el candidato. Por tanto, la convergencia no exige aproximarse sin alcanzarlo ni exige valores distintos entre sí. Tampoco obliga a que el umbral crezca estrictamente cuando la tolerancia disminuye: en este caso $N=0$ sirve para cualquier tolerancia.

Podemos variar el ejemplo sin utilizar aún una regla general sobre cambios finitos. Supongamos que hay un $T\in\mathbb N$ tal que $b_n=A$ para todos los índices $n\ge T$; antes de $T$, los términos pueden ser cualesquiera números reales. Dada $\varepsilon>0$, tomamos $N=T$ y comprobamos de nuevo que $|b_n-A|=0<\varepsilon$ para todo $n\ge N$. Así, **toda sucesión eventualmente constante de valor $A$ converge a $A$**.

Por ejemplo, $b=(7,-3,2,2,2,\ldots)$ converge a 2 con el umbral $N=2$ para cualquier tolerancia. El primer término puede estar lejos del candidato; la condición de convergencia empieza a exigir su estimación después del corte elegido. La prueba usa que la cola es exactamente constante, no una regla de invariancia que demostraremos más adelante.

### Captura por cada vecindad

La definición usa bolas porque el radio permite expresar la precisión numéricamente. En C04 aprendimos a reconocer una vecindad de $A$ sin exigir que ella misma sea una bola: un conjunto $U\subseteq\mathbb R$ es vecindad de $A$ cuando contiene alguna bola $B(A,r)$ con $r>0$. Podemos aprovechar esa interfaz para dar otra lectura de la convergencia.

> **Caracterización por vecindades.** Una sucesión $a:\mathbb N\to\mathbb R$ converge a $A\in\mathbb R$ si y sólo si está eventualmente en cada vecindad de $A$.

Hay dos direcciones que comprobar. En una, una bola suficientemente pequeña permite entrar en una vecindad más amplia; en la otra, las propias bolas son vecindades y recuperan las tolerancias de la definición.

**Demostración.** Supongamos primero que $a_n\to A$ y fijemos una vecindad $U$ de $A$. Por la definición de vecindad, existe un $r>0$ tal que $B(A,r)\subseteq U$. La convergencia, aplicada a la tolerancia $r$, proporciona un $N\in\mathbb N$ para el cual $a_n\in B(A,r)$ siempre que $n\ge N$. La inclusión da $a_n\in U$ para esos mismos índices, de modo que la sucesión está eventualmente en $U$.

Recíprocamente, supongamos que la sucesión está eventualmente en cada vecindad de $A$. Sea $\varepsilon>0$ una tolerancia arbitraria. La bola $B(A,\varepsilon)$ es una vecindad de $A$, así que existe un $N\in\mathbb N$ tal que $a_n\in B(A,\varepsilon)$ para todos los índices $n\ge N$. Esa pertenencia equivale a $|a_n-A|<\varepsilon$ y cumple exactamente la definición de $a_n\to A$. Quedan demostradas ambas direcciones.

La inclusión de una bola en $U$ es el puente decisivo: no necesitamos que $U$ sea abierto, que sea un intervalo ni que tenga una forma especial fuera de esa bola. El umbral puede depender de la vecindad. Del mismo modo que antes no pedíamos una única captura para todas las tolerancias, ahora no pedimos que todas las vecindades compartan un mismo corte.

Podemos usar inmediatamente esta caracterización con el ejemplo $b=(7,-3,2,2,\ldots)$. Toda vecindad de 2 contiene al punto 2, por lo que desde el índice 2 todos sus términos están en ella. La nueva formulación recupera su convergencia sin calcular radios. Para sucesiones cuyas colas no son constantes, en cambio, la inclusión de una bola será lo que permita transferir una estimación numérica a una vecindad cualquiera.

### Qué cambió respecto de C05

En C05 fijábamos un conjunto $U$ y preguntábamos si capturaba una cola. Ahora fijamos un candidato $A$ y pedimos que **cada** ventana de radio positivo alrededor suyo capture alguna cola; equivalentemente, que lo haga cada vecindad de $A$. El nuevo cuantificador no obliga a que todas esas colas empiecen en el mismo lugar.

La definición ya permite formular una meta de prueba. Todavía queda aprender a construir los umbrales, a negar correctamente esa meta y a decidir qué consecuencias podemos extraer de ella. El próximo paso será mirar con mayor cuidado quién elige la tolerancia, quién responde con el umbral y qué puede depender de cada elección.

### Antes de seguir

#### Microcontrol 1

[]{#MA-MIC-ANM-01-006-001}

En la afirmación $a_n\to A$, identifica el tipo de cada objeto $a$, $n$, $a_n$, $A$, $\varepsilon$ y $N$, e indica cuáles se fijan antes de recibir la tolerancia.

[]{#MA-MSOL-ANM-01-006-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

$a$ es una función $\mathbb N\to\mathbb R$; $n\in\mathbb N$ es un índice y $a_n\in\mathbb R$ su término. El candidato $A\in\mathbb R$ es otro número real, $\varepsilon>0$ una tolerancia real y $N\in\mathbb N$ un umbral. Primero se fijan la sucesión $a$ y el candidato $A$. Después se recibe $\varepsilon$, se elige $N$ y se toma un índice arbitrario $n\ge N$.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-006-002}

Escribe la definición de $a_n\to A$ como una oración completa y luego en forma simbólica, conservando la condición $n\ge N$ y la desigualdad estricta del error.

[]{#MA-MSOL-ANM-01-006-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

La sucesión $a$ converge al candidato $A$ si, para cada tolerancia real positiva, existe un umbral natural desde el que todos los términos tienen distancia a $A$ estrictamente menor que esa tolerancia. Simbólicamente,

$$
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N:\quad n\ge N\Longrightarrow |a_n-A|<\varepsilon.
$$

La sucesión y el candidato están fijados antes de esa cuantificación.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-006-003}

Para $r_n=0$ si $n$ es par y $r_n=1$ si es impar, da un umbral de captura en $B(0,2)$. Explica por qué ningún umbral captura una cola en $B(0,1/2)$ y qué afirma esto sobre el candidato 0.

[]{#MA-MSOL-ANM-01-006-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

En $B(0,2)$ sirve $N=0$, pues los dos valores posibles, 0 y 1, tienen módulo menor que 2. En $B(0,1/2)$ no sirve ningún umbral: para cualquier $N$, el índice impar $2N+1\ge N$ tiene valor 1 y error $1\ge1/2$. Por tanto, $r$ no converge al candidato 0. Esta comprobación, por sí sola, refuta ese candidato; no formula todavía una refutación de todos los reales.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-006-004}

Supón que $N$ satisface la estimación para una tolerancia fija y que $K\ge N$. Justifica que $K$ también es un testigo válido. ¿Exige la definición escoger el menor umbral?

[]{#MA-MSOL-ANM-01-006-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

Si $n\ge K\ge N$, entonces $n\ge N$ y se aplica la estimación acreditada por el corte original. Así $K$ controla la misma tolerancia en toda su cola. La definición exige algún testigo natural suficiente, no el menor. La posibilidad de aumentar el umbral permite sincronizar controles sin tener que minimizar cada corte.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-006-005}

Con candidato $A=2$ y tolerancia $\varepsilon=1/3$, clasifica como interiores o de frontera los valores $2$, $5/3$ y $7/3$. ¿Cuáles cumplen el error estricto?

[]{#MA-MSOL-ANM-01-006-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

El valor 2 es interior, con error 0. Los valores $5/3$ y $7/3$ están en la frontera de $B(2,1/3)$, porque sus errores respecto de 2 son exactamente $1/3$. Sólo el valor 2 cumple el error estricto. Estar en el intervalo cerrado correspondiente no equivale a estar en la bola abierta.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-006-006}

Demuestra directamente desde la definición que $b=(9,-4,1,1,1,\ldots)$ converge a 1. Indica un umbral válido para cualquier tolerancia y explica por qué los dos primeros términos no invalidan tu prueba.

[]{#MA-MSOL-ANM-01-006-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

Con la convención de índice inicial 0, tenemos $b_0=9$, $b_1=-4$ y $b_n=1$ desde $n=2$. Para cualquier $\varepsilon>0$, elegimos $N=2$. Si $n\ge N$, entonces $|b_n-1|=0<\varepsilon$. Los dos términos anteriores no pertenecen a la cola que debe controlarse; sus errores no invalidan el testigo.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-006-007}

¿Qué dos limitaciones impiden que la tabla del ejemplo alternante constituya por sí sola una demostración de convergencia? Distingue la cantidad de índices mostrados de la cantidad de tolerancias comprobadas.

[]{#MA-MSOL-ANM-01-006-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

La tabla sólo muestra finitos índices, mientras que una captura exige controlar todos los índices posteriores al corte. Además, sólo comprueba las tolerancias que aparecen en ella, mientras que la definición exige responder a cualquier real positivo. Una fórmula de error y una estimación general pueden cerrar ambas obligaciones; la inspección de esas filas no las cierra.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-006-008}

Reconstruye las dos direcciones de la caracterización por vecindades. Señala en una la inclusión de una bola y en la otra la vecindad concreta que recupera una tolerancia arbitraria.

[]{#MA-MSOL-ANM-01-006-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

Si $a_n\to A$ y $U$ es una vecindad de $A$, existe $r>0$ con $B(A,r)\subseteq U$. La convergencia captura una cola en esa bola, y la inclusión la sitúa en $U$. Recíprocamente, si cada vecindad captura una cola, para una tolerancia arbitraria $\varepsilon>0$ usamos la vecindad concreta $U=B(A,\varepsilon)$. Su captura significa $|a_n-A|<\varepsilon$ eventualmente, que recupera la definición.

</details>

### Ejercicios de la sección 6.1

[]{#ejercicios-6}

#### Ejercicio 1. Ventanas con lados distintos

[]{#MA-EX-ANM-01-006-001}

Fija una sucesión $a:\mathbb N\to\mathbb R$ y $A\in\mathbb R$. Compara la afirmación $a_n\to A$ con la siguiente: para cada $r,s>0$ existe $N\in\mathbb N$ tal que $A-r<a_n<A+s$ para todo $n\ge N$. Demuestra la equivalencia e identifica qué datos se fijan y cuáles se eligen.

[]{#MA-SOL-ANM-01-006-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La sucesión $a$ y el candidato real $A$ se fijan al comienzo; $n$ y $N$ son índices, mientras que $a_n,r,s$ son reales. Si $a_n\to A$, dados $r,s>0$ usamos la tolerancia $\delta=\min\{r,s\}>0$. Su umbral garantiza $-r<a_n-A<s$ en toda la cola. Recíprocamente, recibida $\varepsilon>0$, aplicamos la condición con $r=s=\varepsilon$. Entonces $A-\varepsilon<a_n<A+\varepsilon$, que equivale a $|a_n-A|<\varepsilon$. En cada dirección el umbral se elige antes de tomar un índice arbitrario de la cola; no hace falta que las ventanas iniciales sean simétricas.

</details>

#### Ejercicio 2. Lo que un prefijo no decide

[]{#MA-EX-ANM-01-006-002}

Dados $m\in\mathbb N$ y $x_0,\ldots,x_m\in\mathbb R$, construye dos sucesiones que coincidan con esos datos: una que converja a 0 y otra que no converja a 0. Justifica ambas afirmaciones sin inferir propiedades de una cola a partir de una muestra. Explica qué comparten sus gráficas para $0\le n\le m$.

[]{#MA-SOL-ANM-01-006-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Definimos $a_n=b_n=x_n$ para $n\le m$, y ponemos $a_n=0$, $b_n=2$ para $n>m$. Son funciones con dominio $\mathbb N$ y valores reales. Para cualquier $\varepsilon>0$, el umbral $m+1$ da $|a_n|=0<\varepsilon$, de modo que $a_n\to0$. Para $b$ fijamos la tolerancia 1. Ningún corte $N$ captura su cola alrededor de 0: el índice $n=\max\{N,m+1\}$ tiene $|b_n|=2\ge1$. Las gráficas comparten exactamente los puntos prescritos $(n,x_n)$ en el intervalo de índices mostrado. Ese prefijo no decide la captura de una cola ni la convergencia a 0.

</details>

#### Ejercicio 3. Una familia con destino común

[]{#MA-EX-ANM-01-006-003}

Fija $T\in\mathbb N$ y $A\in\mathbb R$. Para cada familia de reales $x=(x_0,\ldots,x_{T-1})$, define $a^x_n=x_n$ si $n<T$ y $a^x_n=A$ si $n\ge T$. Describe el caso $T=0$, demuestra directamente la convergencia a $A$ y determina cuándo $a^x=a^y$ como funciones. ¿La igualdad del candidato obliga a esa igualdad de funciones?

[]{#MA-SOL-ANM-01-006-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Cuando $T=0$, el prefijo es vacío y la única sucesión de esta familia es la constante $A$. Para cualquier $T$ y cualquier $\varepsilon>0$, tomamos $N=T$. Todos los índices $n\ge N$ cumplen $|a^x_n-A|=0<\varepsilon$; la prueba no depende de las magnitudes del prefijo. Las funciones $a^x$ y $a^y$ tienen el mismo dominio y coinciden desde $T$. Son iguales si y sólo si $x_j=y_j$ para todos los índices $j<T$, pues ésa es la única zona en que pueden diferir. Si $T>0$, basta escoger $x_0\ne y_0$ para obtener funciones diferentes con el mismo candidato de convergencia. No se necesita aquí el teorema posterior de unicidad.

</details>

#### Ejercicio 4. Qué familia de ventanas basta

[]{#MA-EX-ANM-01-006-004}

Demuestra que $a_n\to A$ equivale a que todo intervalo abierto $(u,v)$ con $u<A<v$ capture una cola. Compara esta condición con la captura por cada vecindad de $A$, entendiendo vecindad en el sentido de C04.

[]{#MA-SOL-ANM-01-006-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Si $a_n\to A$ y $u<A<v$, la tolerancia $\delta=\min\{A-u,v-A\}>0$ produce una cola en $(A-\delta,A+\delta)\subseteq(u,v)$. A la inversa, los intervalos $(A-\varepsilon,A+\varepsilon)$ están entre los intervalos exigidos, por lo que recuperamos la definición para cada $\varepsilon>0$. Todo intervalo abierto que contiene $A$ es una vecindad: contiene esa bola de radio $\delta$. Además, por la definición de C04, cualquier vecindad $U$ de $A$ contiene una bola $B(A,r)$ con $r>0$. Así, capturar cada vecindad implica capturar cada intervalo, y capturar cada intervalo implica capturar una bola contenida en cada vecindad. Las inclusiones transmiten la captura a $U$, aunque $U$ no sea un intervalo.

</details>
## 6.2. Quién elige qué: leer y negar la definición

[]{#MA-SEC-ANM-01-006-002}

La definición de §6.1 relaciona tres elecciones: una tolerancia, un umbral y un índice que recorre la cola. Sus cuantificadores no forman una lista de requisitos independientes. El orden determina qué información está disponible al hacer cada elección y, por tanto, qué debemos demostrar.

Fijemos durante esta sección una sucesión $a:\mathbb N\to\mathbb R$ y un candidato $A\in\mathbb R$. La meta es aprender a leer la afirmación $a_n\to A$ y su negación con suficiente precisión para construir después argumentos correctos. No necesitaremos todavía reglas de cálculo de límites.

### La tolerancia se recibe; el umbral se construye

En una prueba de convergencia, la tolerancia $\varepsilon>0$ es arbitraria. Podemos conocer su valor mientras buscamos el umbral, pero no escoger únicamente una tolerancia cómoda y dar por terminada la prueba. El argumento debe responder a cualquiera que se le proponga.

Después de recibir $\varepsilon$, buscamos un $N\in\mathbb N$. Esta elección puede depender de la sucesión fijada, del candidato y de la tolerancia. Una vez construido $N$, tomamos un índice natural $n\ge N$ arbitrario y verificamos $|a_n-A|<\varepsilon$. El índice no se elige para facilitar la estimación: representa cualquiera de los índices que quedan después del corte.

| Momento | Dato o elección | Obligación |
|---|---|---|
| Antes de la prueba | a y A fijados | Analizar esta sucesión y este candidato |
| Entrada | ε>0 arbitraria | Responder a cualquier tolerancia positiva |
| Construcción | N natural | Elegir un corte usando los datos anteriores |
| Verificación | n≥N arbitrario | Controlar todos los términos de esa cola |

La tabla organiza una prueba, no describe un proceso temporal que produzca términos nuevos. La sucesión ya es una función definida en todos los naturales; al variar $\varepsilon$ cambia la exigencia con que la examinamos.

En §6.1, la sucesión $b=(7,-3,2,2,\ldots)$ permitió elegir $N=2$ para toda tolerancia. Era una respuesta válida porque el error de su cola es exactamente cero. Que allí sirviera el mismo corte no transforma esa elección en una obligación para las demás sucesiones.

### Qué significa pedir un corte para todas las tolerancias

Comparemos la definición, que empieza con $\forall\varepsilon>0\ \exists N$, con una condición que invierte esas dos elecciones:

$$
\exists N\in\mathbb N\ \forall\varepsilon>0\
\forall n\in\mathbb N,\qquad
n\ge N\Longrightarrow |a_n-A|<\varepsilon.
$$

Esta condición pide escoger el corte sin conocer la tolerancia y exige que su cola responda a todas las precisiones. Tiene una consecuencia mucho más fuerte: la cola debe ser exactamente constante de valor $A$.

Para comprobarlo, supongamos que ese $N$ existe y fijemos un $n\ge N$. Si el error $d=|a_n-A|$ fuese positivo, podríamos usar la tolerancia $\varepsilon=d/2$. La condición daría $d<d/2$, imposible. Por tanto $d=0$, es decir, $a_n=A$. Como el índice tardío era arbitrario, todos los términos desde $N$ valen $A$.

Recíprocamente, si $a_n=A$ para todo $n\ge T$, elegimos el corte $N=T$. El error es cero y queda por debajo de cualquier tolerancia positiva. Hemos demostrado que la condición con $\exists N$ antes de $\forall\varepsilon$ equivale a ser eventualmente constante de valor $A$.

Podemos usar esta equivalencia con $b=(7,-3,2,2,\ldots)$: además de converger a 2, satisface la condición más fuerte con $N=2$. El argumento muestra qué significa realmente intercambiar esos cuantificadores. La definición original permite un corte adaptado a la tolerancia; no exige esta constancia de la cola.

### Dos formas de perder la obligación de controlar una cola

También podemos debilitar la condición hasta dejar de expresar la convergencia. Una tentación es permitir que cada índice se acompañe de una tolerancia hecha a su medida. Para cualquier sucesión y cualquier candidato, la elección $\varepsilon_n=|a_n-A|+1$ cumple $|a_n-A|<\varepsilon_n$. Esta desigualdad no acredita aproximación: la ventana se adapta al error que ya encontramos. La definición exige responder a una tolerancia previamente impuesta.

Otro cambio defectuoso aparece si se permite elegir $N$ después de conocer el mismo índice $n$ que supuestamente debemos controlar. En la fórmula

$$
\forall\varepsilon>0\ \forall n\in\mathbb N\
\exists N\in\mathbb N,\qquad
n\ge N\Longrightarrow |a_n-A|<\varepsilon,
$$

podemos tomar siempre $N=n+1$. Entonces $n\ge N$ es falso y la implicación se cumple sin imponer ninguna estimación. Cualquier sucesión y cualquier candidato satisfacen esa fórmula. El cambio de orden ha permitido colocar el corte después del índice examinado y vaciar la condición.

Una prueba válida elige el corte antes de verificar un índice arbitrario de su cola. Conviene seguir esa dependencia incluso cuando la fórmula de $N$ parece sencilla: un testigo bien calculado puede dejar de probar lo que queremos si responde a una obligación lógica distinta.

### Visitas arbitrariamente tardías

Recordemos la sucesión $r_n=0$ para n par y $r_n=1$ para n impar. Si fijamos $A=0$, cualquier tolerancia $\varepsilon>0$ y cualquier umbral $N$, el índice $n=2N$ satisface $n\ge N$ y $|r_n-0|=0<\varepsilon$. Por tanto r cumple la condición

$$
\forall\varepsilon>0\ \forall N\in\mathbb N\
\exists n\in\mathbb N,\qquad
n\ge N\ \text{y}\ |r_n-0|<\varepsilon.
$$

Cada ventana alrededor de cero recibe visitas arbitrariamente tardías. Pero r no converge a cero: los índices impares permanecen fuera de la ventana de radio 1/2. La condición de visitas conserva un índice favorable tras cada corte; la convergencia exige que desde algún corte sean favorables todos los índices.

Ésta es la distinción de C05 entre reaparición y eventualidad, aplicada ahora a una distancia y a una tolerancia. La inspección de muchos puntos cercanos, incluso puntos tan tardíos como queramos, no sustituye una estimación válida para toda la cola.

### Derivar la negación sin cambiar de candidato

¿Cómo se demuestra que $a_n\to A$ es falso? Debemos negar la definición completa. Con a y A fijados, la convergencia dice que **toda** tolerancia positiva admite **algún** umbral desde el que **todos** los índices cumplen el error estricto. Su negación afirma que hay una tolerancia para la que ningún umbral consigue ese control.

Neguemos primero la obligación sobre una cola. Que sea falso «para todo n natural, si $n\ge N$ entonces $|a_n-A|<\varepsilon$» significa que existe un índice en el que falla la implicación. Para que falle, su antecedente debe ser verdadero y su conclusión falsa: se necesita a la vez $n\ge N$ y $|a_n-A|\ge\varepsilon$. No sirve un índice anterior al corte.

Al negar los cuantificadores exteriores, «existe N que controla» se convierte en «para todo N hay un fallo», y «para toda ε positiva» se convierte en «existe una ε positiva». Así obtenemos:

> **Refutación de un candidato.** Para a y A fijados, la afirmación $a_n\not\to A$ equivale a que exista una tolerancia $\varepsilon_0>0$ tal que, para cada $N\in\mathbb N$, haya un $n\in\mathbb N$ con $n\ge N$ y $|a_n-A|\ge\varepsilon_0$.

En símbolos,

$$
a_n\not\to A
\quad\Longleftrightarrow\quad
\exists\varepsilon_0>0\ \forall N\in\mathbb N\
\exists n\in\mathbb N,\qquad
n\ge N\ \text{y}\ |a_n-A|\ge\varepsilon_0.
$$

La tolerancia infranqueable $\varepsilon_0$ queda fijada antes de recibir $N$. El índice infractor puede depender de ese umbral. Los papeles han cambiado: para probar convergencia respondemos a una tolerancia con un corte que controla toda una cola; para refutarla presentamos una tolerancia y respondemos a cada corte con una infracción posterior.

La negación de $|a_n-A|<\varepsilon_0$ incluye la igualdad. Un término sobre la frontera ya impide la captura por la ventana abierta. Por eso la desigualdad de refutación es $\ge$, y no solamente $>$.

### Una refutación completa

Apliquemos el criterio a r y al candidato 0. Elegimos $\varepsilon_0=1/2$. Dado cualquier $N\in\mathbb N$, tomamos $n=2N+1$. Este índice es impar y satisface $n\ge N$; por tanto $r_n=1$ y $|r_n-0|=1\ge1/2$. La tolerancia permanece fija mientras el índice infractor responde a cada corte. Queda demostrado $r_n\not\to0$.

Los índices pares no estorban esta prueba: la refutación pide algún infractor después de cada umbral, no que todos los términos tardíos queden fuera. Exigir una cola entera de infracciones sería una afirmación más fuerte, que r no satisface para esta ventana porque siempre hay ceros tardíos.

Un único infractor, en cambio, tampoco basta. Para $b=(7,-3,2,2,\ldots)$ y $A=2$, el término inicial tiene error 5 y queda fuera de la ventana de radio 1. Pero desde $N=2$ no queda ninguna infracción y b converge a 2. La refutación debe resistir cualquier corte, incluidos los que dejan atrás el término señalado.

La figura [C06-F02](#fig-anm-c06-f02) reúne las visitas y las infracciones que acabamos de justificar. La ventana se mantiene fija al cambiar el corte.

### Figura [C06-F02](#fig-anm-c06-f02)

![Para cortes 2, 5 y 8 se muestran una visita par y una infracción impar. La tolerancia 1/2 permanece fija. Las fórmulas 2N y 2N+1 justifican ambos índices tras cualquier corte y refutan el candidato cero.](../../assets/books/anm/C06/C06-F02.svg){#fig-anm-c06-f02 fig-alt="Para cortes 2, 5 y 8 se muestran una visita par y una infracción impar. La tolerancia 1/2 permanece fija. Las fórmulas 2N y 2N+1 justifican ambos índices tras cualquier corte y refutan el candidato cero."}

**Figura [C06-F02](#fig-anm-c06-f02).** Cada corte tiene visitas posteriores a la ventana y también infracciones posteriores. La tolerancia un medio refuta la captura por una cola alrededor de cero.

Los puntos interiores posteriores al corte no eliminan los infractores. La fórmula del índice impar, válida para cualquier N natural, sostiene la refutación del candidato cero.

Si volvemos a la gráfica discreta de r, el mismo corte tiene después puntos de altura cero y de altura uno. Para la convergencia, los puntos interiores no compensan a los exteriores: todos tendrían que estar dentro desde algún corte. Para la refutación, basta conservar un punto exterior después de cada corte. El dibujo ayuda a separar esas obligaciones, pero la fórmula $2N+1$ es la que acredita el infractor para cualquier umbral natural.

### Un candidato incorrecto no significa ausencia de todo límite

Consideremos la sucesión constante $c_n=1$. Sabemos por §6.1 que converge a 1. Si intentamos usar $A=0$, la tolerancia $\varepsilon_0=1$ refuta ese candidato: para cada $N$ podemos tomar $n=N$, y el error $|c_n-0|=1$ cumple la desigualdad $\ge\varepsilon_0$.

Este ejemplo tiene dos funciones. Primero muestra que una sucesión puede converger a un candidato y fallar respecto de otro; refutar cero no demuestra ausencia de todo límite. Además, el error de refutación cae exactamente sobre la frontera. La exigencia errónea $|c_n-0|>1$ no produciría ningún infractor, aunque la ventana abierta de radio 1 no capture un solo término.

Decir que a no tiene ningún límite real es afirmar que **cada** $A\in\mathbb R$ queda refutado. Al escribir la condición completa, A se elige antes de la tolerancia que lo refuta:

$$
\forall A\in\mathbb R\ \exists\varepsilon_0>0\
\forall N\in\mathbb N\ \exists n\in\mathbb N,\qquad
n\ge N\ \text{y}\ |a_n-A|\ge\varepsilon_0.
$$

La tolerancia puede depender del candidato A; después queda fija mientras recorremos los umbrales. No se exige encontrar una sola tolerancia que refute de antemano todos los candidatos. Tampoco se permite cambiar de candidato en medio de la comprobación de uno.

### Una convención sobre el corte

Usamos $n\ge N$ para que el corte incluya su propio índice, como en C05. A veces se escribe una definición con $n>N$. Las dos formulaciones describen la misma convergencia, pero no siempre aceptan el mismo testigo numérico.

Si un corte N controla todos los índices $n\ge N$, controla en particular los que cumplen $n>N$. En sentido inverso, si controla los índices $n>N$, elegimos el corte $K=N+1$: todo natural $n\ge K$ cumple $n>N$ y conserva la estimación.

Por ejemplo, para $d=(1,0,0,\ldots)$, candidato 0 y tolerancia 1/2, el corte N=0 funciona con $n>0$. Falla con $n\ge0$ porque incluye el término inicial de valor 1. Al trasladar el testigo a K=1 obtenemos la captura según nuestra convención. La equivalencia de dos definiciones no autoriza a copiar sin revisión los valores concretos de sus testigos.

### Antes de seguir

#### Microcontrol 9

[]{#MA-MIC-ANM-01-006-009}

Describe el orden de elecciones de una prueba de $a_n\to A$. ¿De qué datos puede depender N y por qué no puede construirse después de escoger el índice que debe controlar?

[]{#MA-MSOL-ANM-01-006-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

Se fijan $a$ y $A$, se recibe $\varepsilon>0$, se construye $N\in\mathbb N$ y se verifica el error para un $n\ge N$ arbitrario. El umbral puede depender de $a,A,\varepsilon$, pero no del índice posterior que recorre la cola. Elegirlo después de conocer ese índice cambiaría la obligación: no se habría construido un corte común para todos los términos tardíos.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-006-010}

Demuestra que pedir un mismo N para todas las tolerancias equivale a que la sucesión sea eventualmente constante de valor A. Identifica la tolerancia que excluye un error positivo.

[]{#MA-MSOL-ANM-01-006-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

Si un mismo $N$ funciona para todas las tolerancias y algún $n\ge N$ tiene error $d=|a_n-A|>0$, elegimos $\varepsilon=d/2$. La captura exigiría $d<d/2$, contradicción. Luego $a_n=A$ para todos los índices desde $N$. A la inversa, si la sucesión es constante de valor $A$ desde un corte, el error cero hace que ese corte sirva para cualquier tolerancia positiva.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-006-011}

Explica por qué las elecciones $\varepsilon_n=|a_n-A|+1$ no prueban convergencia, aunque produzcan una desigualdad estricta en cada índice.

[]{#MA-MSOL-ANM-01-006-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Las cantidades $\varepsilon_n=|a_n-A|+1$ se adaptan al error de cada término y garantizan una desigualdad automática. No responden a una tolerancia arbitraria recibida previamente ni producen un corte que la controle. Por ejemplo, para $a_n=1$ y candidato 0 esas elecciones siempre dan 2, pero la tolerancia $1/2$ no captura ningún término. El procedimiento elude las exigencias pequeñas en lugar de acreditarlas.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-006-012}

En la fórmula con orden $\forall\varepsilon>0\ \forall n\in\mathbb N\ \exists N\in\mathbb N$ y conclusión $n\ge N\Rightarrow |a_n-A|<\varepsilon$, muestra cómo N=n+1 la hace verdadera para cualquier sucesión y candidato. ¿Qué obligación se perdió?

[]{#MA-MSOL-ANM-01-006-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Tras recibir $\varepsilon$ y escoger $n$, se puede poner $N=n+1$. Entonces $n\ge N$ es falso y la implicación resulta verdadera, cualquiera que sea el error. Se perdió el control de todos los índices posteriores a un único umbral: la elección depende del término que se quería comprobar y lo deja fuera de su propia cola.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-006-013}

Deriva la negación de la definición para un candidato fijo. Explica por qué deben aparecer n≥N y error ≥ε₀ unidos por «y», y no por una implicación.

[]{#MA-MSOL-ANM-01-006-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Negar sucesivamente los cuantificadores y la implicación da

$$
\exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists n\in\mathbb N:\quad n\ge N\ \text{y}\ |a_n-A|\ge\varepsilon_0.
$$

El candidato permanece fijo. La negación de $P\Rightarrow Q$ es $P\land\neg Q$: el índice debe pertenecer a la cola y fallar la estimación. Una implicación permitiría que un índice anterior al corte acreditase vacíamente la condición, sin producir ningún infractor tardío.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-006-014}

Para $r_n=0$ si n es par y $r_n=1$ si es impar, fija A=0 y ε₀=1/2. Da, después de un N arbitrario, un índice interior y otro infractor. ¿Cuál de ellos acredita la refutación y por qué no importa que exista el otro?

[]{#MA-MSOL-ANM-01-006-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

El índice $2N\ge N$ es interior: su valor es 0 y su error es cero. El índice $2N+1\ge N$ es infractor: su valor es 1 y el error es al menos $1/2$. El segundo acredita la refutación, pues impide que todos los términos de la cola estén en la ventana. La existencia simultánea de visitas interiores no elimina la infracción que sobrevive a cada corte.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-006-015}

Usa la sucesión constante $c_n=3$ para refutar el candidato A=1 con una tolerancia cuyo error caiga exactamente en la frontera. Explica por qué esa refutación no demuestra ausencia de todo límite real.

[]{#MA-MSOL-ANM-01-006-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

El error respecto de 1 es $|3-1|=2$ en todo índice. Fijamos $\varepsilon_0=2$ y, después de cualquier corte $N$, elegimos $n=N$. El error cae en la frontera y falla la desigualdad estricta. Esto refuta el candidato 1, pero la sucesión converge a 3: con ese candidato el error es cero desde el índice 0. Refutar un número no refuta los demás.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-006-016}

Para $d=(1,0,0,\ldots)$, candidato 0 y tolerancia 1/2, compara el corte N=0 bajo n>N y bajo n≥N. Produce un testigo válido con nuestra convención y justifica la traducción general entre ambas formulaciones.

[]{#MA-MSOL-ANM-01-006-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

Con el corte 0 y condición $n>0$, sólo se inspeccionan términos nulos, así que el error es menor que $1/2$. Con $n\ge0$ se incluye $d_0=1$ y ese corte falla; bajo nuestra convención sirve $N=1$. En general, un umbral $K$ para $n>K$ se transforma en $K+1$ para $n\ge K+1$, porque los índices son naturales. Si un umbral $N$ funciona para $n\ge N$, también sirve para $n>N$, ya que se reduce la cola exigida.

</details>
Ya podemos distinguir una captura de toda la cola, una visita tardía y un infractor que sobrevive a cada corte. En §6.3 usaremos estas obligaciones para construir y comprobar umbrales explícitos; la fórmula de un testigo deberá responder a la definición que acabamos de aprender a leer.

### Ejercicios de la sección 6.2

#### Ejercicio 5. Un candidato elegido demasiado tarde

[]{#MA-EX-ANM-01-006-005}

Alguien escribe: «Para cada $\varepsilon>0$ puedo elegir $A_\varepsilon\in\mathbb R$ y $N_\varepsilon\in\mathbb N$ que satisfacen $|a_n-A_\varepsilon|<\varepsilon$ para todos los índices $n\ge N_\varepsilon$. Por tanto, $a_n\to0$». Localiza la falta en esa conclusión y refútala con una sucesión concreta. ¿Cuál sería la obligación correcta para acreditar el candidato 0? No se pide decidir si la premisa implica alguna otra propiedad.

[]{#MA-SOL-ANM-01-006-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

La premisa controla distancias a centros elegidos después de la tolerancia; no los identifica con 0. Para la sucesión constante $a_n=5$, basta elegir $A_\varepsilon=5$ y $N_\varepsilon=0$ para cualquier tolerancia: el error es cero. Sin embargo, con candidato 0 y tolerancia 1, cada término tiene error 5, así que ningún corte funciona. Para probar $a_n\to0$ hay que fijar ese centro antes de recibir $\varepsilon$ y, para cada tolerancia, construir un umbral que controle $|a_n|$ en toda la cola. Este ejemplo refuta la conclusión propuesta; no pretende negar que la premisa pueda tener consecuencias distintas en una teoría posterior.

</details>

#### Ejercicio 6. Negar la existencia de un destino

[]{#MA-EX-ANM-01-006-006}

Escribe con todos sus dominios la afirmación «$a$ no converge a ningún número real» y deriva su forma cuantificada desde la negación de «existe $A\in\mathbb R$ al que converge». Compara el orden de elecciones con la refutación de un candidato fijo.

[]{#MA-SOL-ANM-01-006-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

La existencia de un destino real se expresa mediante $\exists A\in\mathbb R\ \forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N:\ n\ge N\Rightarrow |a_n-A|<\varepsilon$. Al negar sucesivamente los cuantificadores y la implicación obtenemos

$$
\forall A\in\mathbb R\ \exists\varepsilon_A>0\ \forall N\in\mathbb N\ \exists n\in\mathbb N:\quad n\ge N\ \text{y}\ |a_n-A|\ge\varepsilon_A.
$$

La sucesión queda fijada. Para cada candidato se elige una tolerancia de refutación, que puede depender de él, pero no del corte posterior. Después de cada corte se construye un índice infractor. Para refutar un solo candidato $A_0$ se exige la misma condición únicamente para ese número: desaparece el cuantificador inicial sobre todos los reales. Tal refutación deja sin decidir los demás candidatos.

</details>

#### Ejercicio 7. Visitar sin permanecer

[]{#MA-EX-ANM-01-006-007}

Construye una sucesión real que tome el valor 0 en índices arbitrariamente tardíos y que también tome valores de módulo al menos 2 arbitrariamente tarde, sin ser una sucesión de sólo dos valores. Verifica que visita toda bola alrededor de 0 después de cada corte y que no converge a 0.

[]{#MA-SOL-ANM-01-006-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Definimos $a_n=0$ si $n$ es par y $a_n=n+2$ si es impar. El conjunto de valores no tiene sólo dos elementos: los índices impares producen valores distintos. Dados una tolerancia $\varepsilon>0$ y un corte $N\in\mathbb N$, el índice $2N\ge N$ satisface $a_{2N}=0\in B(0,\varepsilon)$. Por tanto, cada ventana es visitada arbitrariamente tarde. En cambio, fijamos $\varepsilon_0=2$. Después de cualquier corte, el índice $2N+1$ tiene $|a_{2N+1}|=2N+3\ge2$. Ninguna cola completa queda en $B(0,2)$. Los índices de visitas e infracciones se han construido explícitamente; no se usan resultados sobre subsucesiones.

</details>

#### Ejercicio 8. Cambiar la frontera del error

[]{#MA-EX-ANM-01-006-008}

Compara la definición usual de $a_n\to A$ con la condición que exige $|a_n-A|\le\varepsilon$ eventualmente para cada $\varepsilon>0$. Demuestra su equivalencia y deriva la negación de la segunda condición. Explica por qué las distintas desigualdades en las negaciones no cambian su alcance global.

[]{#MA-SOL-ANM-01-006-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Una captura con error estricto implica la misma captura con error no estricto. Recíprocamente, si tenemos la condición no estricta para toda tolerancia, recibida $\varepsilon>0$ usamos $\varepsilon/2$; el umbral correspondiente garantiza $|a_n-A|\le\varepsilon/2<\varepsilon$. Su negación es: existe $\eta>0$ tal que, después de cada corte, aparece un índice con $|a_n-A|>\eta$. Esta condición implica la refutación usual con error $\ge\eta$. Si la refutación usual proporciona $\varepsilon_0>0$ y errores $\ge\varepsilon_0$ después de cada corte, esos mismos índices tienen errores $>\varepsilon_0/2$. Así obtenemos la otra negación. La posibilidad de cambiar de tolerancia permite absorber la diferencia de frontera.

</details>

#### Ejercicio 9. Sólo tolerancias pequeñas

[]{#MA-EX-ANM-01-006-009}

Sea $r>0$ fijo. Demuestra que basta verificar la captura con error estricto para todas las tolerancias $\delta$ tales que $0<\delta<r$ para acreditar $a_n\to A$. ¿Basta verificar únicamente la tolerancia $r$? Justifica la respuesta.

[]{#MA-SOL-ANM-01-006-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Para una tolerancia arbitraria $\varepsilon>0$, elegimos $\delta=\min\{\varepsilon/2,r/2\}$. Es positiva, menor que $r$ y menor que $\varepsilon$. La hipótesis proporciona un umbral para $\delta$, que sirve también para $\varepsilon$, pues $|a_n-A|<\delta<\varepsilon$. No hemos elegido un único corte para todas las tolerancias. Verificar solamente $r$ no basta: la constante $a_n=A+r/2$ satisface $|a_n-A|=r/2<r$ en todos los índices, pero no converge a $A$. La tolerancia $r/4$ falla en toda la sucesión. Una familia de exigencias pequeñas conserva la posibilidad de refinar la captura; una sola exigencia no la conserva.

</details>
## 6.3. Construir el umbral

[]{#MA-SEC-ANM-01-006-003}

Ya sabemos qué obligación impone la convergencia: dada una tolerancia positiva, debemos producir un corte que controle todos los índices posteriores. Ahora construiremos una respuesta explícita para $a_n=1/(n+1)$ y candidato 0. El denominador está definido desde n=0; la dificultad consiste en convertir la precisión que nos piden en un índice natural adecuado.

La prueba tendrá dos recorridos. Primero trabajaremos desde la desigualdad que queremos obtener para descubrir una condición suficiente sobre el índice. Después redactaremos el argumento en el orden de la definición: recibir la tolerancia, elegir el umbral y comprobar un índice tardío arbitrario.

### Buscar desde el error

Para $\varepsilon>0$ y $n\in\mathbb N$, el error respecto de cero es $|a_n-0|=1/(n+1)$. Como n+1 y ε son positivos, podemos transformar la estimación deseada:

$$
\frac1{n+1}<\varepsilon
\quad\Longleftrightarrow\quad
n+1>\frac1\varepsilon.
$$

Esta equivalencia explica la elección que falta. Debemos encontrar un natural N cuyo sucesor sea mayor que $1/\varepsilon$; así, si n≥N, también n+1≥N+1>1/ε. La última comparación controlará de una vez toda la cola.

C03 §3.4 demostró que para cualquier real t hay un natural mayor que t. Esa propiedad arquimediana bastaría para escoger un corte suficientemente grande. Aquí queremos además escribir una respuesta mediante una fórmula reconocible, el piso de t. Antes de usar ese símbolo debemos demostrar la propiedad que le pediremos.

### Construir el piso positivo

> **Piso de un real positivo.** Para cada $t>0$ existe un único $K\in\mathbb N$ tal que $K\le t<K+1$. Lo denotamos por $\lfloor t\rfloor$.

Sólo necesitamos esta construcción para t positivo. El conjunto de naturales que no superan t contiene al menos al 0; la propiedad arquimediana permitirá situarlo dentro de una lista finita y escoger su último elemento.

**Demostración.** Sea t>0. Por C03 §3.4 elegimos un $m\in\mathbb N$ con m>t. Consideremos

$$
F=\{k\in\{0,1,\ldots,m\}:k\le t\}.
$$

Este conjunto es finito y no vacío, pues 0≤t. Tiene un máximo K: se obtiene comparando sus elementos, conservando en cada comparación el mayor de los examinados. Formalmente, la existencia de máximo para una lista finita no vacía se demuestra por inducción sobre su cantidad de elementos.

Como K∈F, tenemos K≤t. Además K<m, pues m>t; por el orden de los naturales, K+1≤m. Si K+1≤t, entonces K+1 también pertenecería a F, contradiciendo que K es su máximo. Por tanto t<K+1. Hemos construido un natural que satisface K≤t<K+1.

Para la unicidad, supongamos que K y J cumplen esas desigualdades. Si K<J, entonces K+1≤J≤t<K+1, contradicción. Si J<K, el mismo argumento con los papeles intercambiados da J+1≤K≤t<J+1, también imposible. Sólo queda K=J. Esto termina la prueba.

El natural obtenido no depende de cuál m>t hayamos elegido: cualquier construcción produce las mismas desigualdades y la unicidad identifica sus resultados. Si 0<t<1, el piso es 0; si t es un natural positivo, su piso es el propio t. Por ejemplo, $\lfloor5/2\rfloor=2$ y $\lfloor3\rfloor=3$.

La propiedad arquimediana se usa una vez, al elegir m. En C03 fue deducida de completitud; aquí reutilizamos ese resultado ya demostrado y después sólo comparamos elementos de un conjunto finito. No estamos recurriendo de nuevo al principio del supremo para crear el máximo de F.

### La primera prueba con un testigo explícito

Volvamos a $a_n=1/(n+1)$. Para t=1/ε, el piso satisface $\lfloor1/\varepsilon\rfloor+1>1/\varepsilon$, que era exactamente la condición suficiente descubierta al trabajar desde el error. Éste es el primer uso del lema.

> **Primera prueba de convergencia con N explícito.** La sucesión $a:\mathbb N\to\mathbb R$ dada por $a_n=1/(n+1)$ converge a 0.

**Demostración.** Sea $\varepsilon>0$ arbitraria. Como 1/ε>0, el resultado anterior permite elegir

$$
N=\left\lfloor\frac1\varepsilon\right\rfloor\in\mathbb N.
$$

Sea ahora $n\in\mathbb N$ con n≥N. La propiedad del piso da n+1≥N+1>1/ε>0. Al tomar recíprocos de números positivos, obtenemos

$$
|a_n-0|=\frac1{n+1}
\le\frac1{N+1}
<\varepsilon.
$$

Hemos comprobado el error estricto para todos los índices n≥N. Como la tolerancia era arbitraria, la definición da $a_n\to0$.

La prueba no necesita reglas algebraicas de límites. Sus herramientas son la definición, el piso que acabamos de construir y el orden de los recíprocos positivos. El paso n≥N⇒n+1≥N+1 es el puente que convierte una elección de corte en control de toda una cola.

Si ε>1, el número 1/ε está entre 0 y 1 y nuestra fórmula produce N=0. La estimación sigue siendo válida: desde el primer índice, $1/(n+1)\le1<\varepsilon$. Así el mismo argumento incluye tolerancias grandes sin pedir un índice negativo ni cambiar el dominio.

### Comprobar y reparar un testigo

La fórmula de N debe leerse junto con la convención n≥N y el error estricto. Algunos valores permiten comprobar ambos detalles:

| Tolerancia ε | 1/ε | Corte $N=\lfloor1/\varepsilon\rfloor$ | Error en el primer índice incluido |
|---:|---:|---:|---:|
| $2$ | $1/2$ | $0$ | $1<2$ |
| $1$ | $1$ | $1$ | $1/2<1$ |
| $1/3$ | $3$ | $3$ | $1/4<1/3$ |
| $1/8$ | $8$ | $8$ | $1/9<1/8$ |

La tabla comprueba casos concretos; el argumento anterior es el que responde a todas las tolerancias. Tampoco bastaría verificar el error en un único término si no hubiéramos demostrado el control de los posteriores. En esta sucesión, la comparación de denominadores es la razón explícita por la que el error de la cola queda dominado por 1/(N+1).

Examinemos una propuesta defectuosa: usar $N'=\lfloor1/\varepsilon\rfloor-1$. Con ε=1/3 da N'=2, pero el término de índice 2 vale 1/3 y queda sobre la frontera. La desigualdad requerida no se cumple. Si ε>1, el mismo intento produce N'=−1, que ni siquiera pertenece a nuestro dominio de umbrales.

Ambos defectos deben diagnosticarse por separado: un supuesto testigo puede estar mal tipado o puede ser natural y aun así no controlar el error. En este caso se repara tomando $N=\lfloor1/\varepsilon\rfloor$, cuya validez ya demostramos. No basta con corregir la frontera de un ejemplo numérico; necesitamos una elección que vuelva a responder a la tolerancia arbitraria.

La figura [C06-F03](#fig-anm-c06-f03) separa el término que cae exactamente sobre la frontera de los términos que sí satisfacen el error estricto.

### Figura [C06-F03](#fig-anm-c06-f03)

![El punto de índice 2 vale 1/3 y se marca como frontera excluida. El corte 3 incluye un primer error 1/4 y controla la cola mediante la estimación general. Se conserva n mayor o igual que N.](../../assets/books/anm/C06/C06-F03.svg){#fig-anm-c06-f03 fig-alt="El punto de índice 2 vale 1/3 y se marca como frontera excluida. El corte 3 incluye un primer error 1/4 y controla la cola mediante la estimación general. Se conserva n mayor o igual que N."}

**Figura [C06-F03](#fig-anm-c06-f03).** Con tolerancia un tercio, el término de índice 2 queda sobre la frontera y no cumple el error estricto. El corte 3 sí controla toda la cola, como muestra la estimación general.

El punto de índice 2 existe y pertenece a la sucesión; lo que se excluye es la frontera de la ventana abierta. Al tomar N=3, ese punto queda en el prefijo y el primer término controlado tiene error 1/4.

Geométricamente, con ε=1/3, el punto (2,1/3) pertenece a la frontera superior de la ventana abierta alrededor de cero. El corte 3 lo deja fuera de la cola que debemos controlar; desde ese corte la estimación general sitúa todos los puntos dentro. La gráfica sigue siendo discreta: no añadimos una curva entre sus índices.

Un corte mayor también sirve, como demostramos en §6.1. No hay que optimizar el testigo para acreditar convergencia; hay que justificar que el elegido funciona. Por ejemplo, cualquier M natural con M≥N conserva la misma estimación para n≥M.

### El ejemplo alternante ya puede demostrarse

En §6.1 presentamos $s_n=(-1)^n/(n+1)$ como imagen anticipatoria de una aproximación que cambia de lado. Ahora podemos verificar la afirmación para todas las tolerancias, sin extrapolar la tabla ni invocar una regla de límites nueva.

Sea ε>0 y elijamos de nuevo $N=\lfloor1/\varepsilon\rfloor$. Para cualquier n≥N, el factor $(-1)^n$ tiene valor absoluto 1, de modo que

$$
|s_n-0|=\frac1{n+1}<\varepsilon.
$$

Esta comprobación, válida para un índice tardío arbitrario, demuestra $s_n\to0$. La primera prueba nos proporciona el corte y la estimación; la igualdad $|s_n|=1/(n+1)$ permite reutilizarlos directamente. Los términos cambian de signo y la sucesión no es monótona: s₀=1, s₁=−1/2 y s₂=1/3 muestran un descenso seguido de un ascenso. Esa alternancia es compatible con la convergencia.

Las ventanas de radios 1/2, 1/4 y 1/8 de §6.1 admiten, respectivamente, los cortes 2, 4 y 8. Ahora la afirmación se apoya en el argumento general para todos los índices posteriores y, además, podemos responder a cualquier otro radio positivo. Ésta es la diferencia entre reconocer la imagen y demostrar la captura.

### Variar centro y escala sin usar reglas de límites

Podemos trasladar la misma técnica a una familia de ejemplos, conservando visibles los parámetros. Fijemos $A,c\in\mathbb R$ y definamos $u_n=A+c/(n+1)$. El objetivo es demostrar $u_n\to A$ desde la definición.

Si c=0, la sucesión es constante y elegimos N=0 para cualquier tolerancia. Si c≠0, dada ε>0 elegimos $N=\lfloor|c|/\varepsilon\rfloor$; el argumento del piso se aplica porque |c|/ε>0. Para n≥N tenemos n+1≥N+1>|c|/ε, y por tanto $|u_n-A|=|c|/(n+1)<\varepsilon$. Queda demostrado el resultado, con ambos signos de c cubiertos.

Esta comprobación no invoca todavía una regla general de suma o de producto de límites. Sólo calcula el error de una función concreta y diseña un corte que lo domina. El centro A desaparece de la expresión del error; la escala |c| determina cuánto debemos pedir al índice. Para $u_n=3-2/(n+1)$, por ejemplo, la elección $N=\lfloor2/\varepsilon\rfloor$ controla la distancia a 3.

### Construir infractores en lugar de umbrales

La negación de §6.2 pide una construcción distinta: escoger una tolerancia que ningún corte pueda controlar y, después de cada corte, presentar un infractor. Con el ejemplo $q_n=(-1)^n$ podemos demostrar algo más fuerte que refutar un candidato particular: no tiene ningún límite real.

Fijemos un candidato arbitrario $A\in\mathbb R$. Los valores 1 y −1 están a distancia 2 entre sí. Por la desigualdad triangular,

$$
2=|1-(-1)|\le|1-A|+|A+1|.
$$

No pueden ser ambas distancias menores que 1, porque entonces su suma sería menor que 2. Por tanto al menos uno de los valores 1 o −1 dista de A al menos 1. Elegimos ε₀=1.

Dado cualquier $N\in\mathbb N$, si $|1-A|\ge1$ tomamos el índice par n=2N; satisface n≥N y $q_n=1$, así que $|q_n-A|\ge1$. Si $|1-A|<1$, la desigualdad anterior obliga a $|A+1|\ge1$; tomamos el índice impar n=2N+1, también posterior al corte, y obtenemos la misma infracción. Hemos respondido a cualquier N con un índice natural cuyo error es al menos ε₀.

Por el criterio de §6.2, $q_n\not\to A$. Como A era arbitrario, todos los candidatos reales quedan refutados. La prueba usa distancia, paridad y la triangular, sin una teoría de subsucesiones ni un teorema de unicidad. La elección uniforme ε₀=1 funciona en este ejemplo, aunque la definición de ausencia de límite no exige esa uniformidad respecto de A.

Comparemos q con s. Ambas alternan lados, pero en s la magnitud del error respecto de cero puede controlarse bajo cualquier tolerancia; en q, una separación fija impide esa captura respecto de todo candidato. La alternancia por sí sola no decide la convergencia: hay que comprobar la magnitud del error y la obligación sobre todos los índices tardíos.

### Antes de seguir

#### Microcontrol 17

[]{#MA-MIC-ANM-01-006-017}

Reconstruye la existencia del piso de t>0 desde la propiedad arquimediana. ¿Por qué el conjunto F es no vacío y por qué su máximo K tiene un sucesor dentro de {0,…,m}?

[]{#MA-MSOL-ANM-01-006-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Por la propiedad arquimediana de C03, elegimos $m\in\mathbb N$ con $m>t$. El conjunto finito $F=\{j\in\{0,\ldots,m\}:j\le t\}$ contiene 0 y tiene máximo $K$. Como $m>t$, el índice $m$ no pertenece a $F$, luego $K<m$ y $K+1\le m$. Si $K+1\le t$, su sucesor pertenecería a $F$, contradiciendo la maximalidad. Así $K\le t<K+1$.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-006-018}

Demuestra la unicidad del natural K que satisface K≤t<K+1 y explica por qué la elección inicial de m>t no cambia el resultado.

[]{#MA-MSOL-ANM-01-006-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Si $K$ y $J$ cumplen las dos desigualdades y $K<J$, el orden natural da $K+1\le J\le t$, contradiciendo $t<K+1$. Si $J<K$, se obtiene la contradicción simétrica. Por tanto, $K=J$. Toda elección de $m>t$ que produzca esa propiedad conduce al mismo natural, pues la unicidad depende sólo de $t$ y no del conjunto auxiliar elegido.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-006-019}

Para $a_n=1/(n+1)$ y ε=2/5, calcula $N=\lfloor1/\varepsilon\rfloor$ y comprueba el error para un n≥N arbitrario. Identifica el paso que controla toda la cola.

[]{#MA-MSOL-ANM-01-006-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Para $\varepsilon=2/5$, $N=\lfloor5/2\rfloor=2$. Si $n\ge2$, entonces $n+1\ge3>5/2$ y, al invertir cantidades positivas, $|a_n|=1/(n+1)\le1/3<2/5$. El paso $n+1\ge N+1>1/\varepsilon$ vale para cualquier índice posterior, no sólo para el primero; por eso controla toda la cola.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-006-020}

Analiza la propuesta $N'=\lfloor1/\varepsilon\rfloor-1$ con ε=1/3 y con ε=2. Distingue el defecto de frontera del defecto de dominio y produce una reparación válida para cualquier ε>0.

[]{#MA-MSOL-ANM-01-006-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Con $\varepsilon=1/3$, la propuesta da $N'=2$ y el índice 2 tiene error $1/3$, de frontera, que no satisface la condición estricta. Con $\varepsilon=2$, da $N'=-1$, que no es un natural. La reparación $N=\lfloor1/\varepsilon\rfloor$ funciona para cualquier tolerancia positiva: $n\ge N$ implica $n+1\ge N+1>1/\varepsilon$, luego $1/(n+1)<\varepsilon$. Cierra tanto el dominio del testigo como la estrictitud.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-006-021}

En la primera prueba, explica por qué ε>1 permite N=0 y por qué ese caso no obliga a empezar la sucesión en el índice 1.

[]{#MA-MSOL-ANM-01-006-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

Si $\varepsilon>1$, entonces $0<1/\varepsilon<1$ y su piso es 0. La sucesión está definida en el índice 0, donde $a_0=1<\varepsilon$; además, para todos los naturales $n$, $a_n\le1<\varepsilon$. Así el corte 0 controla incluso el primer término. Cambia el umbral suficiente para esa tolerancia, no el dominio $\mathbb N$ de la sucesión.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-006-022}

Demuestra directamente que $s_n=(-1)^n/(n+1)$ converge a cero. ¿Qué parte de la primera prueba reutilizas y qué identidad nueva debes comprobar?

[]{#MA-MSOL-ANM-01-006-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Para todo natural $n$, $|(-1)^n|=1$ y $n+1>0$, de modo que $|s_n-0|=1/(n+1)$. Dado $\varepsilon>0$, reutilizamos $N=\lfloor1/\varepsilon\rfloor$ y la estimación de la primera prueba: si $n\ge N$, ese error es menor que $\varepsilon$. La identidad del módulo elimina el signo alternante; la construcción del corte y su verificación permanecen iguales.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-006-023}

Para $u_n=3-2/(n+1)$, construye un umbral que controle el error respecto de 3 para cualquier ε>0. Explica cómo se modificaría tu construcción si el coeficiente −2 se sustituyera por 0.

[]{#MA-MSOL-ANM-01-006-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

El error es $|u_n-3|=2/(n+1)$. Para $\varepsilon>0$ elegimos $N=\lfloor2/\varepsilon\rfloor$; si $n\ge N$, $n+1\ge N+1>2/\varepsilon$, luego el error es menor que $\varepsilon$. Si el coeficiente se sustituye por 0, la sucesión es constante de valor 3 y basta $N=0$ para todas las tolerancias. No hay que aplicar el piso construido para argumentos positivos a un argumento cero.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-006-024}

Reconstruye la refutación de todos los candidatos para $q_n=(-1)^n$. Señala dónde se usa la triangular, cómo se elige la paridad del infractor y por qué este argumento demuestra más que refutar solamente A=0.

[]{#MA-MSOL-ANM-01-006-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

Fijamos un candidato arbitrario $A$. La triangular da $2\le|1-A|+|-1-A|$, así que alguno de esos errores es al menos 1. Fijamos la tolerancia 1 y elegimos el valor separado de $A$. Después de cualquier corte $N$, usamos $2N$ si ese valor es 1, o $2N+1$ si es −1; el índice elegido es tardío y su error es al menos 1. El argumento vale para cada real $A$, por lo que excluye todo límite real, no sólo el candidato 0.

</details>
La construcción de un testigo empieza en la estimación deseada, pero su prueba termina verificando la definición completa. Ya podemos acreditar aproximaciones concretas y refutar candidatos mediante índices explícitos. En §6.4 preguntaremos qué impide que una misma sucesión cumpla la definición para dos candidatos distintos y qué control conserva al cambiar su comienzo.

### Ejercicios de la sección 6.3

#### Ejercicio 10. Centro, escala y denominador

[]{#MA-EX-ANM-01-006-010}

Fija $A,c\in\mathbb R$ y $d,e>0$. Para $a_n=A+c/(dn+e)$, demuestra directamente que $a_n\to A$. Da un umbral explícito para cada $\varepsilon>0$, trata $c=0$ y verifica que la sucesión está definida también en $n=0$.

[]{#MA-SOL-ANM-01-006-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

El denominador cumple $dn+e\ge e>0$ para todo $n\in\mathbb N$, incluido 0. Si $c=0$, la sucesión es constante y $N=0$ sirve para cualquier tolerancia. Si $c\ne0$, ponemos $t=|c|/(d\varepsilon)>0$ y elegimos $N=\lfloor t\rfloor+1$. El piso usado es el construido en §6.3; por su propiedad, $N>t$. Para un índice arbitrario $n\ge N$, tenemos $dn+e>d t=|c|/\varepsilon$. Al dividir por cantidades positivas obtenemos $|a_n-A|=|c|/(dn+e)<\varepsilon$. El testigo es suficiente, aunque el término $e$ pueda permitir uno menor. No se invoca ninguna regla algebraica de límites.

</details>

#### Ejercicio 11. Dos cortes defectuosos

[]{#MA-EX-ANM-01-006-011}

Para la familia del ejercicio 10 con $c\ne0$, se proponen $N_1=\max\{0,\lfloor(|c|/\varepsilon-e)/d\rfloor\}$ y $N_2=\lfloor|c|/(d\varepsilon)\rfloor-1$. Refuta cada propuesta como fórmula válida para todos los parámetros: muestra una falla de estrictitud de $N_1$ y una falla de dominio de $N_2$. Repara ambas con un testigo universal suficiente.

[]{#MA-SOL-ANM-01-006-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Tomamos $c=d=e=1$ y $\varepsilon=1/3$. Entonces $N_1=2$, pero en el índice $n=2$ el error es $1/3$, exactamente la tolerancia. La condición estricta falla, aunque $N_1$ sea un natural. Para $N_2$, con los mismos parámetros y $\varepsilon=2$, resulta $N_2=\lfloor1/2\rfloor-1=-1$, que no pertenece a $\mathbb N$ y no puede servir como umbral de la definición. En ambas fórmulas el defecto ocurre antes de acreditar toda la cola. Una reparación común es $N=\lfloor|c|/(d\varepsilon)\rfloor+1$. Es natural y mayor que $|c|/(d\varepsilon)$; el argumento del ejercicio 10 verifica el error estricto para cada $n\ge N$. Esta reparación no pretende conservar la minimalidad.

La [figura C06-F03](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.3 muestra el mismo fallo de estrictitud en n=2. No representa el segundo defecto: N₂=−1 falla por no pertenecer al dominio de índices.

</details>

#### Ejercicio 12. Un prefijo arbitrario

[]{#MA-EX-ANM-01-006-012}

Sea $T\in\mathbb N$. Define $a_n=x_n$ para $n<T$, con valores reales arbitrarios, y $a_n=A+c/(dn+e)$ para $n\ge T$, donde $A,c\in\mathbb R$ y $d,e>0$. Prueba $a_n\to A$ desde la definición, sin usar aún invariancia por modificaciones finitas. Cubre el prefijo vacío.

[]{#MA-SOL-ANM-01-006-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Los términos del prefijo son reales y los restantes están definidos porque $dn+e>0$. Si $c=0$, elegimos $N=T$ y el error es cero en toda la cola. Si $c\ne0$, dado $\varepsilon>0$ ponemos $K=\lfloor|c|/(d\varepsilon)\rfloor+1$ y $N=\max\{T,K\}$. Para cualquier $n\ge N$ se cumplen las dos obligaciones: usamos la fórmula de la cola porque $n\ge T$, y su denominador es mayor que $|c|/\varepsilon$ porque $n\ge K$. Por tanto, $|a_n-A|<\varepsilon$. Cuando $T=0$ no hay valores iniciales que controlar y la misma construcción funciona. La prueba explica directamente por qué ningún tamaño del prefijo interviene en la estimación tardía.

</details>

#### Ejercicio 13. Un corte suficiente y el menor corte

[]{#MA-EX-ANM-01-006-013}

Considera $a_n=2/(n+3)$ y candidato 0. Para cada $\varepsilon>0$, determina el menor umbral natural que da error estricto en toda la cola. Compáralo con $K=\lfloor2/\varepsilon\rfloor+1$. Examina $\varepsilon=2/5$ y $\varepsilon=1$, e identifica el papel de la frontera.

[]{#MA-SOL-ANM-01-006-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Como $n+3>0$, la condición es $n>2/\varepsilon-3$. Ponemos $m=\lfloor2/\varepsilon\rfloor$, usando sólo el piso de un real positivo. El menor umbral es

$$
N_{\min}=\max\{0,m-2\}.
$$

Si $m\le2$, entonces $2/\varepsilon<m+1\le3$, por lo que el índice 0 y todos los posteriores cumplen la condición. Si $m\ge3$, el índice $m-2$ satisface $n+3=m+1>2/\varepsilon$. Todo natural anterior tiene $n+3\le m\le2/\varepsilon$ y falla el error estricto. Esto acredita la minimalidad y el control de toda la cola. El corte $K=m+1$ del ejercicio 10 es válido pero mayor. Para $\varepsilon=2/5$, $N_{\min}=3$: el índice 2 tiene error $2/5$ y debe excluirse. Para $\varepsilon=1$, $N_{\min}=0$, mientras que $K=3$. Un testigo suficiente responde a la definición; determinar el menor requiere examinar también por qué fallan los índices anteriores.

</details>

#### Ejercicio 14. Dos valores que no desaparecen

[]{#MA-EX-ANM-01-006-014}

Sean $p,q\in\mathbb R$, $p\ne q$, y una sucesión $a$. Supón que existen fórmulas $i,j:\mathbb N\to\mathbb N$ tales que $i(N),j(N)\ge N$, $a_{i(N)}=p$ y $a_{j(N)}=q$ para cada $N$. Demuestra que $a$ no converge a ningún real. Construye además un ejemplo con $p=-2$, $q=4$ y valores adicionales en otros índices.

[]{#MA-SOL-ANM-01-006-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Fijamos un candidato arbitrario $A$ y $D=|p-q|>0$. La triangular da $D\le|p-A|+|q-A|$, de modo que alguno de los dos errores es al menos $D/2$. Elegimos ese valor una vez para este candidato y fijamos $\varepsilon_A=D/2$. Después de cualquier corte usamos $i(N)$ o $j(N)$, según el valor elegido, para obtener el infractor requerido. Como el argumento vale para cada $A$, no hay destino real. Para el ejemplo, ponemos $a_{3k}=-2$, $a_{3k+1}=4$ y $a_{3k+2}=k$. Las fórmulas $i(N)=3N$ y $j(N)=3N+1$ acreditan las hipótesis. Los valores adicionales no eliminan la separación persistente que refuta cada candidato.

</details>
## 6.4. Un solo destino; el comienzo puede cambiar

[]{#MA-SEC-ANM-01-006-004}

En §6.3 acreditamos candidatos concretos mediante umbrales explícitos. Queda una pregunta necesaria antes de tratar el límite como un número determinado por la sucesión: ¿podrían dos candidatos distintos satisfacer la definición para la misma función?

La captura por una sola ventana no lo impediría, porque dos ventanas grandes pueden solaparse. La convergencia ofrece más control: permite reducir sus radios usando la separación entre los candidatos. Después necesitaremos sincronizar ambas capturas para exigir que un mismo término pertenezca a las dos ventanas.

### Unicidad: un índice común para dos capturas

> **Unicidad del límite.** Sean $a:\mathbb N\to\mathbb R$ y $A,B\in\mathbb R$. Si $a_n\to A$ y $a_n\to B$, entonces A=B.

La estrategia consiste en suponer que la distancia entre A y B es positiva y pedir errores suficientemente pequeños para que la triangular no pueda reconstruir esa distancia. El punto decisivo será usar ambas estimaciones en un mismo índice; para ello recuperaremos el máximo de umbrales de C05.

**Demostración.** Supongamos que $a_n\to A$ y $a_n\to B$, y que A≠B. Entonces $d=|A-B|>0$. Aplicamos ambas convergencias con la tolerancia d/3. Existen $N_A,N_B\in\mathbb N$ tales que, para todo índice $n≥N_A$, se cumple $|a_n-A|<d/3$, y para todo $n≥N_B$ se cumple $|a_n-B|<d/3$.

Tomemos $N=\max\{N_A,N_B\}$. En el índice n=N valen simultáneamente las dos estimaciones. Por la desigualdad triangular,

$$
d=|A-B|
\le |A-a_N|+|a_N-B|
<\frac d3+\frac d3
=\frac{2d}{3}.
$$

Como d>0, tenemos 2d/3<d, contradicción. La suposición A≠B es imposible; por tanto A=B.

La tolerancia d/3 se elige después de suponer una separación positiva. El máximo asegura que no comparamos dos términos distintos: es el mismo número $a_N$ el que tendría que estar suficientemente cerca de ambos candidatos. Pedir radios d, en cambio, sólo daría d<2d y no produciría esta contradicción.

No se usa completitud ni una regla algebraica de límites. La prueba combina definición, triangular y sincronización de dos obligaciones eventuales. Si imaginamos A<B, las ventanas de radios d/3 están separadas; sus dos supuestas capturas exigirían una pertenencia simultánea imposible. La orientación A<B sirve para esa lectura geométrica, mientras que el argumento con |A−B| cubre ambas orientaciones.

La figura [C06-F04](#fig-anm-c06-f04) muestra por qué sincronizar los cortes obligaría al mismo término a pertenecer a dos ventanas disjuntas. Sus carriles de índices representan las dos capturas supuestas, no una sucesión que pueda cumplirlas.

### Figura [C06-F04](#fig-anm-c06-f04)

![Dos ventanas abiertas de radio d/3 están separadas por un hueco d/3. Los cortes de dos capturas hipotéticas se reúnen en su máximo y exigirían una pertenencia simultánea imposible para el mismo término.](../../assets/books/anm/C06/C06-F04.svg){#fig-anm-c06-f04 fig-alt="Dos ventanas abiertas de radio d/3 están separadas por un hueco d/3. Los cortes de dos capturas hipotéticas se reúnen en su máximo y exigirían una pertenencia simultánea imposible para el mismo término."}

**Figura [C06-F04](#fig-anm-c06-f04).** La sincronización exige que un mismo término tardío esté en ambas ventanas. La separación de los candidatos y la triangular hacen imposible esa doble pertenencia.

El hueco entre las ventanas tiene longitud d/3. El máximo no aproxima los candidatos: sólo hace disponibles las dos obligaciones en un mismo índice. La contradicción procede de exigir ambas pertenencias.

### El límite como número bien determinado

La unicidad permite introducir ahora la notación

$$
\lim_{n\to\infty}a_n=A
$$

cuando $a_n\to A$. Si existe un candidato que satisface la definición, el resultado anterior garantiza que esta escritura asigna un único número a la sucesión. La existencia se comprueba por separado; la unicidad no construye un límite para una sucesión cualquiera.

Como primer uso, §6.3 demostró que $u_n=3-2/(n+1)$ converge a 3. Podemos escribir $\lim_{n\to\infty}u_n=3$ y descartar cualquier resultado distinto para ese mismo límite: si una segunda prueba acreditara $u_n\to B$, la unicidad obligaría a B=3. No es necesario refutar uno por uno los demás candidatos.

La expresión n→∞ en la notación describe el comportamiento de los índices sin cota superior; no añade un término final ni permite evaluar la función en un índice llamado infinito. Para $q_n=(-1)^n$, cuya ausencia de límite real ya demostramos, no asignamos un número a $\lim_{n\to\infty}q_n$.

### La convergencia se transfiere por coincidencia eventual

El límite es único para una sucesión, pero sucesiones distintas pueden tener el mismo límite. Un mecanismo que lo produce es cambiar un número finito de términos iniciales. C05 estableció cómo transferir propiedades eventuales cuando dos funciones coinciden desde un corte; ahora aplicaremos ese mecanismo a cada tolerancia de la definición.

> **Coincidencia eventual y convergencia.** Sean $a,b:\mathbb N\to\mathbb R$. Supongamos que existe un $T\in\mathbb N$ tal que $a_n=b_n$ para todo n≥T. Entonces, para cada $A\in\mathbb R$, se cumple $a_n\to A$ si y sólo si $b_n\to A$.

Para una tolerancia dada habrá dos cortes que respetar: el de la estimación original y el de la igualdad de términos. Su máximo dejará ambas condiciones disponibles en una sola cola.

**Demostración.** Fijemos A y supongamos primero que $a_n\to A$. Sea ε>0. La convergencia proporciona un $N_a\in\mathbb N$ tal que $|a_n-A|<\varepsilon$ para todo $n≥N_a$. Tomemos $N_b=\max\{T,N_a\}$. Si $n≥N_b$, se cumplen n≥T y $n≥N_a$; por tanto $b_n=a_n$ y $|b_n-A|=|a_n-A|<\varepsilon$. Esto demuestra $b_n\to A$.

Recíprocamente, si $b_n\to A$, para cada ε>0 elegimos un umbral $N_b$ de su estimación y tomamos $N_a=\max\{T,N_b\}$. Todo índice $n≥N_a$ satisface $a_n=b_n$ y la estimación de b, de modo que $|a_n-A|<\varepsilon$. Así $a_n\to A$ y quedan probadas ambas direcciones.

El resultado conserva todos los candidatos de convergencia y, cuando existe alguno, su límite único. También conserva la ausencia de límite: si a no tiene límite real y b lo tuviera, la dirección inversa produciría un límite para a. La hipótesis no dice que a y b sean la misma función, sino que sus evaluaciones coinciden desde T.

Por ejemplo, sea $a_n=1/(n+1)$ y definamos b₀=7, b₁=−3, b₂=2 y $b_n=a_n$ para n≥3. Las funciones difieren en el prefijo, pero coinciden desde T=3. Por la convergencia de a ya demostrada y el resultado anterior, $b_n\to0$; la unicidad permite escribir que ambos límites son 0. Para una tolerancia ε, un testigo explícito de b es $\max\{3,\lfloor1/\varepsilon\rfloor\}$.

Esto no vuelve invariantes todas las propiedades de la sucesión. En a todos los términos son positivos; en b el término de índice 1 es negativo. La propiedad global «todos los términos son positivos» se pierde al cambiar el comienzo, aunque la convergencia se conserva. El resultado tiene el alcance de su demostración: cada estimación de error debe valer desde algún índice.

### Mismo límite sin coincidencia eventual

La conversa de la última explicación sería falsa. Tener el mismo límite no obliga a compartir una cola de valores idénticos.

Las sucesiones $a_n=1/(n+1)$ y $v_n=-1/(n+1)$ convergen a cero por las pruebas directas de §6.3. Sin embargo, $a_n>0$ y $v_n<0$ para todo $n\in\mathbb N$, de modo que sus términos nunca coinciden en un mismo índice. Sus límites son iguales como números reales, pero las funciones son distintas y ni siquiera coinciden eventualmente.

Así podemos usar la coincidencia eventual como una condición suficiente para transferir convergencia, sin convertirla en una condición necesaria para que dos sucesiones tengan el mismo destino.

### Reindexar una cola conserva la convergencia

Cambiar un prefijo mantiene las posiciones de los términos tardíos. Reindexar una cola cambia sus nombres de índice. Recordemos la distinción de C05: la restricción $a|_{\mathbb N_{\ge T}}$ tiene dominio $\mathbb N_{\ge T}=\{n\in\mathbb N:n\ge T\}$; para obtener otra sucesión con dominio $\mathbb N$ definimos $b_k=a_{T+k}$ para $k\in\mathbb N$.

> **Convergencia de una cola reindexada.** Sean $a:\mathbb N\to\mathbb R$, $T\in\mathbb N$ y $b:\mathbb N\to\mathbb R$ dada por $b_k=a_{T+k}$. Para cada $A\in\mathbb R$, se cumple $a_n\to A$ si y sólo si $b_k\to A$.

En esta prueba no disponemos de la igualdad $a_n=b_n$ en los mismos índices. Debemos traducir el índice de cada función: k en la nueva sucesión corresponde a T+k en la original.

**Demostración.** Supongamos primero que $a_n\to A$ y recibamos ε>0. Sea N un umbral de a para esa tolerancia. Si k≥N, entonces T+k≥k≥N y $|b_k-A|=|a_{T+k}-A|<\varepsilon$. Por tanto el mismo corte N, ahora sobre los índices k, demuestra $b_k\to A$. Es un testigo suficiente, aunque puede ser mayor que el necesario.

Para la dirección inversa, supongamos que $b_k\to A$. Dada ε>0, elijamos un umbral K tal que $|b_k-A|<\varepsilon$ para todo k≥K. Tomemos el umbral original N=T+K. Si n≥N, entonces n≥T, el número k=n−T pertenece a $\mathbb N$ y satisface k≥K. Además $a_n=b_{n-T}=b_k$, por lo que $|a_n-A|<\varepsilon$. Esto acredita $a_n\to A$ y completa la equivalencia.

El primer sentido usa que T es un natural no negativo; el segundo necesita que n esté después del corte T para que n−T sea un índice permitido. La traducción por T+K no es un cambio de candidato ni un desplazamiento de los valores sobre la recta real.

Podemos aplicarlo a $a_n=1/(n+1)$ y T=3. La sucesión reindexada es $b_k=a_{3+k}=1/(k+4)$; como a converge a cero, b también. El término b₀=1/4 corresponde al término a₃, y no a a₀. Al escribir las dos gráficas discretas cambia la coordenada de índice que asignamos a esos valores.

Si en una prueba de b se ha encontrado el corte K=5 para cierta tolerancia, la dirección inversa controla a desde N=3+5=8. En la dirección directa, un corte N=8 de a permite elegir K=8 para b: no necesitamos encontrar el corte óptimo para demostrar la transferencia.

La figura [C06-F05](#fig-anm-c06-f05) reúne el cambio de prefijo y la reindexación. En sus rótulos, b designa la sucesión con prefijo modificado y c la cola reindexada; esta última es la función llamada b en el teorema anterior.

### Figura [C06-F05](#fig-anm-c06-f05)

![Las filas a y b comparten términos desde n=3, pero sus prefijos difieren. La fila c comienza en k=0 con a_3. Las flechas sólo traducen índices, no desplazan valores. Restricción y conjunto de valores tienen tipos distintos.](../../assets/books/anm/C06/C06-F05.svg){#fig-anm-c06-f05 fig-alt="Las filas a y b comparten términos desde n=3, pero sus prefijos difieren. La fila c comienza en k=0 con a_3. Las flechas sólo traducen índices, no desplazan valores. Restricción y conjunto de valores tienen tipos distintos."}

**Figura [C06-F05](#fig-anm-c06-f05).** Cambiar un prefijo conserva el límite, aunque cambie la sucesión. Reindexar una cola devuelve su dominio a los naturales y exige traducir los umbrales.

La flecha entre a₃ y c₀ conserva el valor 1/4 y cambia su nombre de índice. En cambio, las filas a y b conservan los índices originales y comparten sus términos desde 3. Ninguna de estas relaciones identifica una función con su conjunto de valores.

La restricción y el conjunto de valores tardíos tampoco deben confundirse con la nueva función b. La restricción conserva los índices originales; b vuelve a tener dominio $\mathbb N$; el conjunto $\{a_n:n\ge T\}$ sólo recoge valores y pierde sus posiciones y repeticiones. El teorema se enuncia para b porque la definición de convergencia que fijamos usa sucesiones con dominio $\mathbb N$.

Cuando T=0, $b_k=a_k$ y el resultado incluye la propia sucesión. Para cualquier T natural, quitar ese prefijo finito conserva la convergencia y la ausencia de límite real en ambos sentidos. No afirmamos aquí una transferencia mediante selecciones arbitrarias de índices: hemos demostrado exactamente el desplazamiento k↦T+k.

### Antes de seguir

#### Microcontrol 25

[]{#MA-MIC-ANM-01-006-025}

Reconstruye la unicidad del límite e identifica por qué la triangular debe aplicarse a un mismo término. ¿Qué asegura el corte máximo?

[]{#MA-MSOL-ANM-01-006-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

Si $a_n\to A$ y $a_n\to B$ con $A\ne B$, ponemos $d=|A-B|>0$. Las capturas con tolerancia $d/3$ proporcionan cortes $N_A,N_B$. En un mismo índice $n\ge\max\{N_A,N_B\}$, la triangular da $d\le|A-a_n|+|a_n-B|<2d/3$, contradicción. El máximo asegura que ambos controles recaigan en ese mismo término, necesario para enlazar las dos distancias. Así $A=B$.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-006-026}

En la prueba de unicidad, compara las tolerancias d/3 y d para d=|A−B|>0. ¿Cuál produce la contradicción mediante la estimación escrita y por qué?

[]{#MA-MSOL-ANM-01-006-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Con tolerancia $d/3$ para cada candidato, la estimación da $d<2d/3$, imposible para $d>0$. Si usamos $d$ para ambos, sólo obtenemos $d<2d$, que no contradice la separación. Las capturas pueden ajustarse porque la convergencia responde a todas las tolerancias; el reparto debe mantener el error total por debajo de la distancia entre los candidatos.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-006-027}

Si una prueba acredita $u_n\to3$ y otra pretende acreditar $u_n\to B$, explica qué permite concluir la unicidad. ¿Garantiza ese teorema que toda sucesión tenga un límite real?

[]{#MA-MSOL-ANM-01-006-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

Si las dos pruebas fueran válidas, la unicidad aplicada a $u$ obligaría a $B=3$. Cuando $B\ne3$, sus conclusiones no pueden acreditarse simultáneamente para la misma sucesión. El teorema garantiza a lo sumo un destino real; no garantiza que exista alguno. La sucesión $(-1)^n$, cuya ausencia de todo límite ya se demostró, muestra esa diferencia.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-006-028}

Supón que $a_n=b_n$ desde T=5 y que a tiene un umbral $N_a=9$ para cierta tolerancia respecto de A. Da un umbral para b y demuestra la estimación que debe satisfacer.

[]{#MA-MSOL-ANM-01-006-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Tomamos $N_b=\max\{5,9\}=9$. Para cualquier $n\ge9$, está disponible tanto la igualdad $b_n=a_n$ como la captura de $a$ respecto de $A$. Por tanto, $|b_n-A|=|a_n-A|<\varepsilon$ para la tolerancia considerada. Un corte que sólo controlase una de esas dos obligaciones no justificaría la transferencia.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-006-029}

Construye dos sucesiones que tengan el mismo límite y no coincidan en ningún índice, usando sólo ejemplos ya demostrados. Explica la diferencia entre igualdad de límites e igualdad de funciones.

[]{#MA-MSOL-ANM-01-006-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Podemos tomar $a_n=0$ y $b_n=1/(n+1)$. Ambas convergen a cero por pruebas ya disponibles y, como $b_n>0$, nunca coinciden en un índice común. Los límites son números reales iguales; las sucesiones son funciones distintas, pues sus valores difieren en cada índice. Tener igual límite no significa igualdad de funciones ni coincidencia eventual.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-006-030}

Para $b_k=a_{3+k}$, traduce un umbral K=5 de b a uno de a y un umbral N=8 de a a un testigo suficiente de b. Justifica los índices y sus dominios en ambas direcciones.

[]{#MA-MSOL-ANM-01-006-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Si el corte de $b$ es $K=5$, tomamos $N=3+5=8$ para $a$: para todo $n\ge8$, el natural $k=n-3\ge5$ satisface $a_n=b_k$. Si el corte de $a$ es $N=8$, sirve $K=5$ para $b$, pues $k\ge5$ implica $3+k\ge8$. También serviría el corte suficiente $K=8$. En cada dirección se transportan índices de funciones con dominio $\mathbb N$ mediante la relación $n=3+k$.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-006-031}

Distingue los objetos $a|_{\mathbb N_{\ge T}}$, la función $b_k=a_{T+k}$ y el conjunto $\{a_n:n\ge T\}$. ¿A cuál se aplica literalmente nuestra definición de sucesión real con dominio $\mathbb N$?

[]{#MA-MSOL-ANM-01-006-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

La restricción $a|_{\mathbb N_{\ge T}}$ es una función $\mathbb N_{\ge T}\to\mathbb R$. La cola reindexada $b_k=a_{T+k}$ es una función $\mathbb N\to\mathbb R$. El conjunto $\{a_n:n\ge T\}$ es un subconjunto de $\mathbb R$ y no conserva posiciones ni repeticiones como información indexada. Nuestra definición se aplica literalmente a $b$. Si $T=0$, la restricción también tiene dominio $\mathbb N$ y coincide con $a$; para $T>0$ tiene otro dominio.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-006-032}

Si a no tiene ningún límite real y b coincide con a desde algún T, demuestra que b tampoco lo tiene. ¿Cómo se modifica el argumento si b es una cola reindexada de a?

[]{#MA-MSOL-ANM-01-006-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

Si $b$ coincidiese eventualmente con $a$ y convergiese a algún $B$, la equivalencia por coincidencia eventual transmitiría esa convergencia a $a$, contra la hipótesis. Por tanto, $b$ no tiene límite real. Si $b_k=a_{T+k}$ es una cola reindexada, una supuesta convergencia de $b$ se transmite a $a$ usando, para cada corte $K$ de $b$, el corte $T+K$ en los índices originales. La misma contradicción excluye su convergencia.

</details>
La unicidad permite tratar el límite existente como un número determinado; la transferencia eventual y la reindexación permiten identificar qué cambios del objeto conservan ese número. En §6.5 estudiaremos otro tipo de consecuencia: qué control global y qué estimaciones de error deja disponible una convergencia ya demostrada.

### Ejercicios de la sección 6.4

#### Ejercicio 15. Cómo repartir una separación

[]{#MA-EX-ANM-01-006-015}

En una prueba de unicidad con candidatos distintos $A,B$, escribe $D=|A-B|$. Se desean tolerancias $\alpha D$ y $\beta D$, con $\alpha,\beta>0$. Determina cuándo la triangular y las dos capturas bastan por sí solas para dar contradicción. Explica qué ocurre cuando $\alpha+\beta>1$.

[]{#MA-SOL-ANM-01-006-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Sincronizados los umbrales, un mismo término satisface ambas capturas y la triangular da $D\le|A-a_n|+|a_n-B|<(\alpha+\beta)D$. Hay contradicción si $\alpha+\beta\le1$, incluida la igualdad, porque el error total es estricto. Si la suma es mayor que 1, esa estimación aislada no contradice $D>0$. Más aún, las ventanas pueden compartir un punto: con $A=0$, $B=D$, elegimos un real $t$ en $(\max\{0,1-\beta\},\min\{1,\alpha\})$, intervalo no vacío cuando $\alpha+\beta>1$. El punto $tD$ tiene distancias menores que $\alpha D$ y $\beta D$. Esto no permite dos límites reales distintos: para la unicidad pueden elegirse otras tolerancias cuya suma sea menor o igual que la separación. Sólo muestra que el reparto propuesto no cierra esa contradicción.

</details>

#### Ejercicio 16. Transportar índices y cortes

[]{#MA-EX-ANM-01-006-016}

Fija $T\in\mathbb N$, una sucesión $a$ y $A\in\mathbb R$. Compara $r=a|_{\mathbb N_{\ge T}}$ con $b_k=a_{T+k}$. Declara dominios y codominios y escribe el transporte $k\mapsto T+k$ y su inversa. Para una tolerancia, transforma un umbral de $a$ en uno de $b$, y un umbral de $b$ en uno de $a$, justificando las dos capturas.

[]{#MA-SOL-ANM-01-006-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

La función $r$ tiene dominio $\mathbb N_{\ge T}$ y codominio $\mathbb R$; $b$ tiene dominio $\mathbb N$ y el mismo codominio. La biyección $\tau_T(k)=T+k$ lleva $\mathbb N$ a $\mathbb N_{\ge T}$ y tiene inversa $n\mapsto n-T$. Se cumple $b=r\circ\tau_T$, no igualdad de las dos funciones. Si $a$ tiene umbral $N$ para la tolerancia dada, podemos usar $K=\max\{0,N-T\}$ para $b$. Cuando $k\ge K$, se tiene $T+k\ge N$, tanto si $N\le T$ como si $N>T$; de ahí $|b_k-A|<\varepsilon$. Si $b$ tiene umbral $K$, tomamos $N=T+K$ para $a$. Cada $n\ge N$ admite $k=n-T\in\mathbb N$ con $k\ge K$, y $a_n=b_k$. La correspondencia de índices transporta el control de toda la cola.

En la [figura C06-F05](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.4, la fila c ilustra la reindexación con T=3. Aquí b cumple ese papel para T general; el corte optimizado K=max{0,N−T} se justifica por las desigualdades anteriores, no por el corte suficiente de la figura.

</details>

#### Ejercicio 17. Tres funciones y un destino

[]{#MA-EX-ANM-01-006-017}

Construye tres sucesiones reales distintas que converjan a 0, de modo que las dos primeras coincidan eventualmente y la tercera difiera de ambas en todos los índices suficientemente grandes. Justifica la convergencia y explica qué igualdades se conservan y cuáles no.

[]{#MA-SOL-ANM-01-006-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Tomamos $a_n=0$ para todo $n$, $b_0=7$ y $b_n=0$ para $n\ge1$, y $c_n=1/(n+1)$. La convergencia de $a$ sigue del error cero; $b$ converge a 0 con umbral 1 para cualquier tolerancia. La convergencia de $c$ es la prueba directa de §6.3. Las tres funciones son distintas: $a_0\ne b_0$, $c_0\ne a_0$ y $c_0\ne b_0$. Además, $c_n>0=a_n=b_n$ para todo $n\ge1$. Hay coincidencia eventual entre $a$ y $b$, pero no entre éstas y $c$. Después de la unicidad de §6.4 sus límites pueden escribirse como el mismo número 0; la igualdad de esos números no implica igualdad de funciones ni coincidencia eventual.

</details>

#### Ejercicio 18. Alguna cola y todas las colas

[]{#MA-EX-ANM-01-006-018}

Para $a:\mathbb N\to\mathbb R$ y $A\in\mathbb R$, prueba la equivalencia de: $a_n\to A$; existe $T\in\mathbb N$ tal que $a_{T+k}\to A$ al recorrer $k\in\mathbb N$; para cada $T\in\mathbb N$ esa cola reindexada converge a $A$. Distingue el candidato común de los cortes, que pueden variar.

[]{#MA-SOL-ANM-01-006-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Si $a_n\to A$, fijamos cualquier $T$. Dada una tolerancia con umbral $N$ para $a$, el mismo umbral para $k$ es suficiente, porque $T+k\ge k\ge N$. Así converge cada cola reindexada al candidato común. Que converjan todas implica que converge alguna, por ejemplo la de $T=0$. Si converge una cola con índice inicial $T$, recibimos $\varepsilon>0$ y obtenemos su corte $K$. El umbral $N=T+K$ controla $a$: para todo $n\ge N$, el natural $k=n-T\ge K$ tiene $a_n=a_{T+k}$ y error menor que $\varepsilon$. Esta última dirección explica por qué basta alguna cola. El candidato $A$ queda fijo en las tres afirmaciones; los cortes dependen de la tolerancia y pueden depender de $T$.

</details>
## 6.5. Qué control deja una sucesión convergente

[]{#MA-SEC-ANM-01-006-005}

La definición permite pedir un error tan pequeño como queramos, siempre que aceptemos buscar un umbral para cada tolerancia. Esa exigencia tiene consecuencias que conviene extraer antes de calcular con límites. ¿Puede una sucesión convergente tener términos de tamaño arbitrariamente grande? ¿Cómo podemos aprovechar una estimación de error ya conocida para controlar otra sucesión?

Empezaremos con una tolerancia fija para obtener una cota global. Después volveremos a las tolerancias arbitrarias: expresaremos la convergencia como desaparición del error y aprenderemos a transferirla mediante una desigualdad. Son tareas distintas. Una sola ventana basta para acotar una cola; para demostrar convergencia necesitamos responder a todas las ventanas.

### De una cola controlada a una cota global

Recordemos que una sucesión real $a:\mathbb N\to\mathbb R$ es acotada si existe un número real $M\ge0$ tal que $|a_n|\le M$ para todo $n\in\mathbb N$. La cota se elige una vez y sirve para todos los índices, incluido el comienzo.

> **Acotación de una sucesión convergente.** Si $a_n\to A$ para algún $A\in\mathbb R$, entonces a es acotada. Se puede elegir una cota $M\ge1$.

La convergencia controla términos tardíos; la conclusión exige controlar todos. La estrategia será dividir los índices en una cola y un prefijo finito. Una tolerancia fija dará una cota para la cola, y un máximo finito recogerá los valores que quedaron antes de ella.

**Demostración.** Como $a_n\to A$, podemos pedir la tolerancia 1. Existe $N\in\mathbb N$ tal que $|a_n-A|<1$ para todo $n\ge N$. Para esos índices, la triangular da

$$
|a_n|\le |a_n-A|+|A|<1+|A|.
$$

Formemos ahora el conjunto finito

$$
S=\{1,|A|+1\}\cup\{|a_n|:n\in\mathbb N,\ n<N\}.
$$

S es no vacío porque contiene 1 y $|A|+1$. Por la existencia de máximo para un conjunto finito no vacío de números reales, podemos definir $M=\max S$. En particular, $M\ge1$.

Si $n<N$, el número $|a_n|$ pertenece a S, por lo que $|a_n|\le M$. Si $n\ge N$, la estimación de la cola da $|a_n|<|A|+1\le M$, y por tanto también $|a_n|\le M$. Estas dos posibilidades cubren todo índice natural. Así M es una cota global.

Si el umbral obtenido es $N=0$, no hay índices naturales con $n<N$: el prefijo está vacío. La construcción sigue funcionando porque entonces $S=\{1,|A|+1\}$. No necesitamos tomar el máximo de un conjunto vacío ni separar una prueba nueva.

La cota final es no estricta. Un término del prefijo puede alcanzar M, y la propiedad de máximo sólo asegura que los elementos de S son menores o iguales que él. Tampoco buscamos la menor cota posible. La utilidad del teorema consiste en disponer de un número fijo que controle todos los términos. En §6.6 ese número sustituirá a un factor variable en la estimación del error de un producto.

Como primer uso de la construcción, tomemos $c_0=4$ y $c_n=1/(n+1)$ para $n\ge1$. Esta sucesión converge a cero por coincidencia eventual con el ejemplo de §6.3. La tolerancia 1 admite el umbral $N=1$, pues $0<c_n\le1/2<1$ cuando $n\ge1$. Entonces $S=\{1,4\}$ y $M=4$. La cola cabe en la ventana $(-1,1)$, pero la cota global debe incluir el término inicial 4: para todo n vale $|c_n|\le4$, y la igualdad se alcanza en $n=0$.

En la gráfica discreta, las dos fronteras de la cota global están a alturas −4 y 4. La banda de tolerancia alrededor del límite sólo captura la cola desde 1. La construcción del máximo explica cómo reunir ambos controles sin convertir una ventana eventual en una afirmación sobre el prefijo.

En la figura [C06-F06](#fig-anm-c06-f06), comparemos la banda que sólo controla la cola con las fronteras que deben contener todos los términos.

### Figura [C06-F06](#fig-anm-c06-f06)

![El término inicial alcanza la frontera global 4. La cola desde índice 1 queda en la banda abierta entre menos uno y uno. Las cotas globales menos cuatro y cuatro son cerradas y contienen todo el dominio.](../../assets/books/anm/C06/C06-F06.svg){#fig-anm-c06-f06 fig-alt="El término inicial alcanza la frontera global 4. La cola desde índice 1 queda en la banda abierta entre menos uno y uno. Las cotas globales menos cuatro y cuatro son cerradas y contienen todo el dominio."}

**Figura [C06-F06](#fig-anm-c06-f06).** La tolerancia uno controla una cola. El máximo de esa cota y de un prefijo finito controla todos los términos; la cota global puede ser alcanzada.

El punto inicial alcanza 4 y debe admitirse en la cota global. Los términos de la cola quedan estrictamente dentro de la banda de radio 1, pero esa banda no contiene el comienzo. El máximo finito reúne ambos controles.

La prueba sólo usa una captura, la triangular y un máximo finito. No necesita el principio del supremo, compacidad ni un teorema de existencia de límites.

### La acotación no basta para converger

El resultado anterior tiene una dirección precisa: convergencia implica acotación. Su conversa es falsa.

La sucesión $q_n=(-1)^n$ es acotada, porque $|q_n|=1$ para todo n. Sin embargo, §6.3 mostró que no converge a ningún número real. Podemos recuperar aquí la razón sin emplear subsucesiones. Para cualquier candidato A, la triangular da

$$
2=|1-(-1)|\le |1-A|+|-1-A|.
$$

Por tanto al menos uno de los valores 1 y −1 está a distancia mayor o igual que 1 de A. Para cada umbral propuesto $N\in\mathbb N$, los índices $2N$ y $2N+1$ son mayores o iguales que N y producen los valores 1 y −1, respectivamente. Podemos elegir uno de esos índices donde $|q_n-A|\ge1$. La tolerancia 1 impide acreditar ese candidato; como A era arbitrario, no hay límite real.

Una cota global dice dónde pueden estar todos los valores. No obliga a que las colas quepan en ventanas arbitrariamente pequeñas alrededor de un mismo centro. En este ejemplo, ningún comienzo que se descarte elimina la separación entre los dos valores.

### Converger a A equivale a que el error tienda a cero

Para estudiar la aproximación a A conviene formar una nueva sucesión: el error con signo $e:\mathbb N\to\mathbb R$, definido por $e_n=a_n-A$. Sus índices son los mismos que los de a, pero sus valores miden el desplazamiento respecto del candidato.

> **Identidad de errores.** Para cualquier sucesión real a y cualquier $A\in\mathbb R$, se cumple $a_n\to A$ si y sólo si $e_n\to0$, donde $e_n=a_n-A$.

**Demostración.** Para todo índice n tenemos $|e_n-0|=|a_n-A|$. Por tanto, para cada tolerancia $\varepsilon>0$ y cada umbral N, la condición $|e_n|<\varepsilon$ para todo $n\ge N$ es exactamente la condición $|a_n-A|<\varepsilon$ para todo $n\ge N$. Los mismos umbrales acreditan ambas convergencias.

No hemos usado una regla de resta de límites. La equivalencia se demuestra antes de esas reglas mediante una igualdad de números que vale en cada índice. Si la convergencia está acreditada, los límites únicos de a y e son A y 0; las funciones a y e pueden ser distintas.

Por ejemplo, para $a_n=3-2/(n+1)$ y $A=3$, el error es $e_n=-2/(n+1)$. La prueba directa de §6.3 ya controla $|a_n-3|=2/(n+1)$; ahora reconocemos que esa misma prueba acredita $e_n\to0$. Cambia el objeto que describimos, pero no cambia la estimación ni sus testigos.

### Transferir un control de error

A menudo una nueva diferencia no tiene una fórmula tan simple como el error conocido. Basta entonces encontrar una desigualdad que la domine. Queremos extraer una herramienta que evite reconstruir desde cero la misma elección de tolerancias.

> **Lema de transferencia de error.** Sean $u,v:\mathbb N\to\mathbb R$. Supongamos que $u_n\to0$ y que existen un número real fijo $C\ge0$ y un índice $T\in\mathbb N$ tales que $|v_n|\le C|u_n|$ para todo $n\ge T$. Entonces $v_n\to0$.

La constante C mide cuánto puede amplificarse el error conocido. Si es positiva, pediremos a u una tolerancia dividida por C. También habrá que sincronizar ese control con el corte T desde el cual vale la comparación.

**Demostración.** Primero supongamos $C>0$. Sea $\varepsilon>0$. Como $\varepsilon/C>0$ y $u_n\to0$, existe $N_u\in\mathbb N$ tal que $|u_n|<\varepsilon/C$ para todo $n\ge N_u$. Tomemos $N=\max\{T,N_u\}$. Para todo $n\ge N$ disponemos de la comparación y del control de u; así,

$$
|v_n|\le C|u_n|<C\frac{\varepsilon}{C}=\varepsilon.
$$

La desigualdad estricta se conserva porque C es positivo. Hemos respondido a una tolerancia arbitraria con un umbral que sirve para todos los índices posteriores.

Si $C=0$, para todo $n\ge T$ tenemos $0\le|v_n|\le0$, de modo que $v_n=0$. Dada cualquier tolerancia positiva, el propio corte T satisface $|v_n|=0<\varepsilon$. Esto demuestra también $v_n\to0$ en ese caso.

La escala se elige antes del umbral: recibimos ε, calculamos $\varepsilon/C$ cuando $C>0$, obtenemos $N_u$ y lo reunimos con T. No multiplicamos una desigualdad estricta por cero. El caso nulo se resuelve mediante igualdad eventual con cero.

Es esencial que C sea una constante fija. Si permitiéramos un factor dependiente del índice sin más control, la conclusión fallaría: $u_n=1/(n+1)$ converge a cero, pero la sucesión constante $v_n=1$ satisface $|v_n|=(n+1)|u_n|$ y no converge a cero. Por ejemplo, para la tolerancia $1/2$ ningún umbral consigue $|v_n|<1/2$. La amplificación variable puede deshacer el control que aporta u.

### Primer uso del lema: valor absoluto

Ahora podemos resolver una pregunta concreta. Si los valores de a se aproximan a A, ¿sus distancias al origen se aproximan a la distancia de A al origen?

> **Convergencia del valor absoluto.** Si $a_n\to A$, entonces $|a_n|\to|A|$.

La distancia entre dos distancias al origen se controla mediante la triangular inversa de C04. Ese control encaja con el lema que acabamos de demostrar.

**Demostración.** Definamos $u_n=a_n-A$ y $v_n=|a_n|-|A|$. La identidad de errores acredita $u_n\to0$. Para todo n, la triangular inversa da

$$
|v_n|=\bigl||a_n|-|A|\bigr|\le |a_n-A|=|u_n|.
$$

Aplicamos la transferencia con $C=1$ y $T=0$. Obtenemos $v_n\to0$. Por la identidad de errores aplicada a la sucesión $b_n=|a_n|$ y al candidato $|A|$, esto equivale a $b_n\to|A|$, que es la conclusión buscada.

La desigualdad central no es estricta: puede haber igualdad entre ambas magnitudes. La estrictitud que exige la definición procede del control $|u_n|<\varepsilon$ en la cola. No necesitamos que la comparación mejore el error en cada índice, ni usamos continuidad del valor absoluto.

En el ejemplo $a_n=-1/(n+1)$, la sucesión a converge a cero y el resultado acredita que $|a_n|=1/(n+1)$ también converge a cero. Para $a_n=3-2/(n+1)$, acredita que $|a_n|\to3$. Las dos aplicaciones parten de convergencias ya probadas.

La conversa general vuelve a ser falsa: para $q_n=(-1)^n$, la sucesión de valores absolutos es constante e igual a 1, por lo que converge a 1; q no tiene límite real. Tomar valor absoluto puede perder la información de signo que impedía la captura alrededor de un único candidato.

Como segundo uso del lema, definamos $z_0=9$ y $z_n=(-1)^n/(n+1)^3$ para $n\ge1$. La función z tiene dominio natural completo. Para $n\ge1$, como $n+1\ge1$, tenemos

$$
|z_n|=\frac1{(n+1)^3}\le\frac1{n+1}.
$$

El control conocido $u_n=1/(n+1)\to0$ se transfiere con $C=1$ y $T=1$; por tanto $z_n\to0$. El valor inicial 9 no entra en la comparación tardía. Para una tolerancia ε podemos usar explícitamente $N=\max\{1,\lfloor1/\varepsilon\rfloor\}$, reuniendo el comienzo de la desigualdad con el testigo de u. La estimación controla la magnitud aunque los términos de z cambien de signo.

Hemos obtenido dos herramientas de alcance distinto. La acotación proporciona un número fijo que controla todos los términos; la transferencia convierte un error que tiende a cero en otro que también lo hace. La primera usó una tolerancia fija y un prefijo finito; la segunda conservó la obligación de responder a cada tolerancia positiva.

### Antes de seguir

#### Microcontrol 33

[]{#MA-MIC-ANM-01-006-033}

Reconstruye la prueba de acotación indicando qué controla la tolerancia 1 y qué aporta el máximo finito. ¿Por qué esa sola tolerancia no demostraría convergencia?

[]{#MA-MSOL-ANM-01-006-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

La convergencia proporciona un corte $N$ para la tolerancia 1. Desde él, $|a_n|\le|A|+|a_n-A|<|A|+1$. El conjunto finito $S=\{1,|A|+1\}\cup\{|a_j|:j<N\}$ tiene máximo $M$, que cubre el prefijo y la cola, con $|a_n|\le M$ para todos los índices. Esa sola tolerancia basta para obtener una cota; la convergencia exige capturas para todas las tolerancias positivas y no se deduce de esta única banda.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-006-034}

En la definición de S de la prueba, explica qué sucede cuando N=0. ¿Por qué S sigue teniendo máximo sin tomar el máximo de un conjunto vacío?

[]{#MA-MSOL-ANM-01-006-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Si $N=0$, no hay índices naturales $j<N$ y el prefijo es vacío. Pero $S=\{1,|A|+1\}$ permanece finito y no vacío; su máximo existe y controla la cola, que en ese caso comprende todos los índices. Se ha incluido una cota explícita antes de formar el máximo, en lugar de intentar tomar el máximo del prefijo vacío.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-006-035}

Para $c_0=4$ y $c_n=1/(n+1)$ cuando $n\ge1$, usa el corte N=1 y calcula la cota M de la construcción. ¿Puedes sustituir $|c_n|\le M$ por $|c_n|<M$ para todos los índices?

[]{#MA-MSOL-ANM-01-006-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

El candidato es 0 y, desde $N=1$, $0<c_n\le1/2<1$. La construcción da $S=\{1,|0|+1\}\cup\{|c_0|\}=\{1,4\}$ y $M=4$. En todos los índices vale $|c_n|\le4$, pero no puede reemplazarse por $|c_n|<4$: el término inicial tiene módulo exactamente 4. La desigualdad estricta disponible para la cola no convierte el máximo del prefijo en una cota estricta.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-006-036}

Demuestra que $(-1)^n$ es acotada pero no converge a ningún número real. Distingue refutar un candidato fijo de refutar todos los candidatos.

[]{#MA-MSOL-ANM-01-006-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

La sucesión tiene módulo 1 en todos los índices y está acotada por 1. Para cualquier candidato $A$, la triangular da $2\le|1-A|+|-1-A|$; al menos un error es mayor o igual que 1. Ese valor se obtiene después de cualquier corte $N$ en $2N$ o $2N+1$. La tolerancia 1 refuta cada candidato, luego no hay límite real. Refutar sólo un $A$ dejaría abiertos los demás; aquí $A$ fue arbitrario.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-006-037}

Define la sucesión de error de $a_n=3-2/(n+1)$ respecto de A=3 y justifica la equivalencia de convergencias mediante una identidad. ¿Necesitas una regla de resta de límites?

[]{#MA-MSOL-ANM-01-006-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

La sucesión de error es $e_n=a_n-3=-2/(n+1)$, función real con el mismo dominio $\mathbb N$. En cada índice $|e_n-0|=|a_n-3|=2/(n+1)$. Por tanto, los mismos umbrales para todas las tolerancias acreditan $a_n\to3$ y $e_n\to0$, en ambas direcciones. La equivalencia procede de una identidad de errores, sin usar una regla de resta de límites.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-006-038}

En el lema de transferencia, supón C=3, T=4 y que para una tolerancia ε el control de u con tolerancia ε/3 vale desde $N_u=7$. Elige un umbral para v y verifica la estimación. Explica por separado cómo se prueba el caso C=0.

[]{#MA-MSOL-ANM-01-006-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Para $C=3$ tomamos $N=\max\{4,7\}=7$. Si $n\ge7$, ambas obligaciones están disponibles y $|v_n|\le3|u_n|<3(\varepsilon/3)=\varepsilon$. Si $C=0$, la comparación desde $T$ da $|v_n|\le0$, luego $v_n=0$ en esa cola. El corte $T$ sirve para todas las tolerancias positivas; no se divide por cero.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-006-039}

Reconstruye la prueba de convergencia del valor absoluto identificando u, v, C y T. ¿Qué aporta la triangular inversa y dónde se obtiene la desigualdad estricta?

[]{#MA-MSOL-ANM-01-006-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

Definimos $u_n=a_n-A$ y $v_n=|a_n|-|A|$. La identidad de errores da $u_n\to0$. La triangular inversa asegura $|v_n|\le|u_n|$ para todo índice, así que usamos $C=1$ y $T=0$. La transferencia produce $v_n\to0$, equivalente a $|a_n|\to|A|$. La comparación puede ser una igualdad; la estrictitud final viene de $|u_n|<\varepsilon$ en la cola, no de una mejora estricta en la triangular inversa.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-006-040}

Usa ejemplos de esta sección para refutar dos afirmaciones: que la convergencia de $|a_n|$ obliga a la de a, y que basta una comparación $|v_n|\le C_n|u_n|$ con factores variables para transferir $u_n\to0$ a $v_n\to0$.

[]{#MA-MSOL-ANM-01-006-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Para $a_n=(-1)^n$, los módulos son la constante 1 y convergen, pero $a$ no tiene límite real. Para la segunda afirmación tomamos $u_n=1/(n+1)$, $v_n=1$ y $C_n=n+1$. Entonces $|v_n|=C_n|u_n|$ en todos los índices y $u_n\to0$, mientras que $v$ no converge a cero. Los coeficientes variables sin una cota fija pueden compensar por completo el error pequeño. El lema requiere una constante fija, o un control que permita reducirse a ella.

</details>
En §6.6 volveremos a estas herramientas para justificar las reglas de cálculo. Tendremos que elegir tolerancias de entrada, reunir sus umbrales y comprobar las hipótesis que permiten controlar cada operación.

### Ejercicios de la sección 6.5

#### Ejercicio 19. Acotar con otra tolerancia

[]{#MA-EX-ANM-01-006-019}

Supón $a_n\to A$. Para $r>0$, sea $N_r$ un umbral con error menor que $r$. Construye una cota global usando esa cola y el prefijo, incluido $N_r=0$. Para $a_0=20$, $a_n=0$ si $n\ge1$, compara las cotas obtenidas con $r=1,N_r=1$ y con $r=30,N_r=0$. ¿Se minimiza necesariamente la cota eligiendo una tolerancia mayor?

[]{#MA-SOL-ANM-01-006-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Definimos el conjunto finito no vacío $S_r=\{1,|A|+r\}\cup\{|a_j|:j<N_r\}$ y $M_r=\max S_r$. Para $n<N_r$ la cota está incluida en el conjunto; para $n\ge N_r$, la triangular da $|a_n|\le|A|+|a_n-A|<|A|+r\le M_r$. Por tanto, $|a_n|\le M_r$ en todos los índices, sin pretender estrictitud en el prefijo. Si $N_r=0$, el prefijo es vacío, pero $S_r$ sigue conteniendo 1. En el ejemplo $A=0$: la primera elección produce $M_1=20$ y la segunda $M_{30}=30$. Un corte anterior puede reducir el prefijo que se inspecciona, pero una tolerancia mayor aumenta la cota de cola. No hay una minimización automática por ese cambio.

La [figura C06-F06](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.5 muestra cómo reunir cola y prefijo. Su cota 4 corresponde a otro ejemplo; las cotas 20 y 30 de esta solución se calculan con sus propios datos.

</details>

#### Ejercicio 20. Qué decide el módulo

[]{#MA-EX-ANM-01-006-020}

Construye una sucesión $a$ cuyo módulo converja a un número positivo pero que no converja a ningún real. Demuestra, por contraste, que $|b_n|\to0$ sí obliga a $b_n\to0$. Da un ejemplo de esta segunda situación con signos alternantes.

[]{#MA-SOL-ANM-01-006-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Podemos tomar $a_n=2(-1)^n$. Su módulo es la constante 2, que converge a 2. Los valores 2 y −2 reaparecen después de cada corte, y el argumento de separación del ejercicio 14 refuta todos los candidatos para $a$. Si $|b_n|\to0$, en cambio, su captura dice $||b_n|-0|<\varepsilon$ para toda cola suficientemente tardía. Esa expresión es precisamente $|b_n-0|$, por lo que el mismo umbral prueba $b_n\to0$. La sucesión $b_n=(-1)^n/(n+1)$ es un ejemplo: su módulo es $1/(n+1)$, cuya convergencia a cero ya se demostró directamente. El caso de módulo límite cero conserva toda la información de distancia al candidato 0; un módulo límite positivo no determina de qué lado están los términos.

</details>

#### Ejercicio 21. Un coeficiente variable controlado

[]{#MA-EX-ANM-01-006-021}

Sean $u_n\to0$, $v:\mathbb N\to\mathbb R$ y $C:\mathbb N\to\mathbb R$. Supón que $|v_n|\le C_n|u_n|$ desde $T$ y que $0\le C_n\le M$ desde $S$, con $M\ge0$ fijo. Demuestra $v_n\to0$ y separa $M=0$ de $M>0$. Explica qué sustituye a la constancia del coeficiente.

[]{#MA-SOL-ANM-01-006-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Desde $R=\max\{T,S\}$ tenemos $|v_n|\le M|u_n|$. Si $M=0$, esto obliga a $v_n=0$ para $n\ge R$, y $R$ sirve para cualquier tolerancia positiva. Si $M>0$, recibimos $\varepsilon>0$ y escogemos un corte $K$ para $u$ con tolerancia $\varepsilon/M$. Para $n\ge N=\max\{R,K\}$ se cumple $|v_n|\le M|u_n|<\varepsilon$. Lo decisivo es una cota eventual fija que pueda usarse para elegir la tolerancia auxiliar antes de recorrer la cola. El coeficiente $C_n$ puede variar dentro de esa cota; su mera existencia sin control uniforme no permite el mismo argumento.

</details>

#### Ejercicio 22. Una comparación intermitente

[]{#MA-EX-ANM-01-006-022}

Examina este argumento: «$u_n\to0$ y, después de cada corte, hay un índice con $|v_n|\le3|u_n|$; luego $v_n\to0$». Construye un contraejemplo y localiza el cuantificador que falta. Formula una reparación suficiente y demuéstrala.

[]{#MA-SOL-ANM-01-006-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Tomamos $u_n=1/(n+1)$ y $v_n=0$ en índices pares, $v_n=2$ en impares. La convergencia de $u$ ya está probada. Para cada corte $N$, el índice $2N$ satisface $|v_{2N}|=0\le3|u_{2N}|$. Pero con tolerancia 1, el índice $2N+1$ es un infractor para $v$ después de cualquier corte; no hay convergencia a cero. El argumento necesita que la comparación valga para todos los índices desde un mismo $T$, no sólo que algún índice la satisfaga después de cada corte. Bajo esa reparación, dado $\varepsilon>0$, elegimos $K$ para $u$ con tolerancia $\varepsilon/3$ y tomamos $\max\{T,K\}$. Cada índice posterior satisface $|v_n|\le3|u_n|<\varepsilon$.

</details>

#### Ejercicio 23. Compartir destino por un error pequeño

[]{#MA-EX-ANM-01-006-023}

Supón $a_n-b_n\to0$. Demuestra que $a_n\to A$ si y sólo si $b_n\to A$, para un candidato real fijo $A$. Usa la definición y la triangular; no invoques la regla posterior de suma de límites.

[]{#MA-SOL-ANM-01-006-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Si $a_n\to A$, recibimos $\varepsilon>0$. Elegimos $N_1$ para $|a_n-A|<\varepsilon/2$ y $N_2$ para $|a_n-b_n|<\varepsilon/2$. Para todo $n\ge\max\{N_1,N_2\}$, la triangular da $|b_n-A|\le|b_n-a_n|+|a_n-A|<\varepsilon$. Así converge $b$ al mismo candidato. Si $b_n\to A$, repetimos el control usando $|a_n-A|\le|a_n-b_n|+|b_n-A|$ y sus dos umbrales con tolerancia $\varepsilon/2$. El módulo de la diferencia es el mismo al invertir su orden; no hay que justificar una resta de límites para usarlo. La hipótesis aporta un control de la distancia entre las sucesiones, no coincidencia eventual entre sus términos.

</details>
## 6.6. Calcular límites sin perder las hipótesis

[]{#MA-SEC-ANM-01-006-006}

Los ejemplos de §6.3 se demostraron construyendo un umbral desde una fórmula de error. Ahora tenemos otras herramientas: una sucesión convergente está acotada, y un error dominado por una constante fija veces otro error que tiende a cero también tiende a cero. Podemos usarlas para justificar reglas de cálculo.

El objetivo de cada regla será preciso: a partir de convergencias acreditadas, demostrar la convergencia de una nueva sucesión. No supondremos continuidad de las operaciones ni importaremos las reglas del libro de cálculo como pruebas. Trabajaremos con identidades y estimaciones en los números reales.

Organizaremos el argumento en tres bloques. Las reglas lineales reparten la tolerancia entre errores; el producto necesita además una cota para un factor variable; el inverso exige separar el denominador de cero y definir correctamente la función antes de estimarla.

### Reglas lineales: repartir la tolerancia

Sean $a,b:\mathbb N\to\mathbb R$, con $a_n\to A$ y $b_n\to B$. La función $s:\mathbb N\to\mathbb R$ dada por $s_n=a_n+b_n$ está definida en todos los índices. Queremos controlar su error respecto de $A+B$.

> **Regla de la suma.** Si $a_n\to A$ y $b_n\to B$, entonces $a_n+b_n\to A+B$.

La identidad $(a_n+b_n)-(A+B)=(a_n-A)+(b_n-B)$ separa dos aportes. Podemos pedir que cada uno tenga magnitud menor que la mitad de la tolerancia de salida, y después reunir sus umbrales.

**Demostración.** Sea $\varepsilon>0$. Elegimos $N_a,N_b\in\mathbb N$ tales que $|a_n-A|<\varepsilon/2$ para todo $n\ge N_a$ y $|b_n-B|<\varepsilon/2$ para todo $n\ge N_b$. Tomemos $N=\max\{N_a,N_b\}$. Para todo $n\ge N$, la triangular da

$$
|(a_n+b_n)-(A+B)|
\le |a_n-A|+|b_n-B|
<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
=\varepsilon.
$$

Así se cumple la definición para la sucesión suma.

La elección $\varepsilon/2$ es un reparto suficiente, no una obligación de dividir siempre en partes iguales. Lo necesario es que los presupuestos sean positivos y que su suma no exceda la tolerancia de salida. El máximo aparece después del reparto: primero elegimos qué errores necesitamos y luego sincronizamos dónde están controlados.

Como primer uso, $h_n=1/(n+1)$ converge a 0 y $t_n=3-2/(n+1)$ converge a 3 por §6.3. La regla acredita $h_n+t_n\to3$. La identidad $h_n+t_n=3-1/(n+1)$ permite reconocer la función resultante; la conclusión procede de dos hipótesis verificadas.

> **Regla del factor escalar.** Si $a_n\to A$ y c es un número real fijo, entonces $ca_n\to cA$.

El error es $|ca_n-cA|=|c||a_n-A|$. Debemos separar el caso nulo antes de dividir una tolerancia por $|c|$.

**Demostración.** Si $c=0$, la nueva sucesión es constante e igual a cero, y su candidato $cA$ también es cero. Para toda $\varepsilon>0$, el corte $N=0$ sirve porque el error es $0<\varepsilon$.

Si $c\ne0$, entonces $|c|>0$. Dada $\varepsilon>0$, la convergencia de a proporciona un umbral N para la tolerancia $\varepsilon/|c|$. Para todo $n\ge N$,

$$
|ca_n-cA|=|c||a_n-A|
<|c|\frac{\varepsilon}{|c|}
=\varepsilon.
$$

Esto demuestra la regla para todo escalar real.

El signo de c no cambia el argumento porque el control usa $|c|$. Por ejemplo, la regla aplicada a h con $c=-2$ da $-2h_n\to0$; con $c=0$ da la sucesión nula sin una división auxiliar.

Ya podemos derivar la diferencia y las combinaciones lineales. El escalar −1 acredita $-b_n\to-B$; la suma acredita $a_n-b_n\to A-B$. Para números reales fijos α y β, las dos aplicaciones del escalar dan $\alpha a_n\to\alpha A$ y $\beta b_n\to\beta B$; la suma da $\alpha a_n+\beta b_n\to\alpha A+\beta B$. Estas conclusiones reutilizan pruebas anteriores, incluidas sus hipótesis, en lugar de repetir la misma estimación.

Una constante real d define una sucesión constante que converge a d, pues su error es cero en todo índice. Así, de $h_n\to0$ obtenemos $2+5h_n\to2$ mediante escalar y suma. La regla construye nuevas convergencias a partir de las que conocemos.

La dirección inversa no está incluida. La suma de dos sucesiones puede converger aunque un sumando no tenga límite: $q_n=(-1)^n$ no converge, pero $q_n+(-q_n)=0$ para todo n. La cancelación exacta demuestra la convergencia de esa suma; no autoriza aplicar la regla para deducir límites de los sumandos.

### Producto: controlar el factor variable

> **Regla del producto.** Si $a_n\to A$ y $b_n\to B$, entonces $a_nb_n\to AB$.

La sucesión producto tiene dominio $\mathbb N$ porque cada evaluación $a_nb_n$ es un número real. Su error se puede descomponer mediante la identidad

$$
a_nb_n-AB=a_n(b_n-B)+B(a_n-A).
$$

El segundo aporte tiene el coeficiente fijo B. En el primero aparece el coeficiente variable $a_n$: pedir que $b_n-B$ sea pequeño no basta si no controlamos cuánto puede amplificarlo ese factor. Aquí se gasta la acotación de §6.5.

**Demostración.** Por la convergencia de a, existe una cota global $M\ge1$ tal que $|a_n|\le M$ para todo n. Fijemos esa cota antes de recibir la tolerancia.

Sea $\varepsilon>0$. Pedimos a b la tolerancia $\varepsilon/(2M)$ y a a la tolerancia $\varepsilon/[2(|B|+1)]$. Ambas son positivas: $M\ge1$ y $|B|+1>0$. Existen umbrales $N_b,N_a\in\mathbb N$ para esas dos estimaciones. Tomemos $N=\max\{N_a,N_b\}$.

Para todo $n\ge N$, la identidad y la triangular dan

$$
|a_nb_n-AB|
\le |a_n||b_n-B|+|B||a_n-A|
\le M|b_n-B|+|B||a_n-A|.
$$

El primer aporte satisface $M|b_n-B|<\varepsilon/2$, porque M es positivo. Para el segundo usamos la cota no estricta $|B||a_n-A|\le |B|\varepsilon/[2(|B|+1)]$, válida también si $B=0$. En consecuencia,

$$
|a_nb_n-AB|
<\frac{\varepsilon}{2}
+\frac{|B|}{|B|+1}\frac{\varepsilon}{2}
\le\varepsilon.
$$

Hemos obtenido el error estrictamente menor que ε que exige la definición.

El término $|B|+1$ evita una división por cero en la tolerancia de a. Cuando $B=0$, el segundo aporte se anula; su estimación no se presenta como estricta, porque multiplicar por cero no conserva una desigualdad estricta. La estrictitud del primer aporte basta para cerrar el argumento en todos los casos.

La cota M ya controla todos los índices, así que no añadimos un tercer umbral para ella. Si sólo dispusiéramos de una cota desde otro corte, también tendríamos que incluir ese corte en el máximo. La prueba separa dos tareas: obtener un coeficiente fijo y diseñar los errores que ese coeficiente podrá amplificar.

Volvamos al reparto de la suma. Allí ambos coeficientes de error eran 1, y las tolerancias $\varepsilon/2$ bastaban directamente. Aquí el primer presupuesto exige dividir por M, mientras que el segundo debe tener en cuenta B. Los segmentos que representen estos presupuestos corresponden a magnitudes no negativas de error; no representan términos con signo ni una curva continua de la sucesión.

La figura [C06-F07](#fig-anm-c06-f07) permite reconstruir el orden de las elecciones: fijar los presupuestos positivos, pedir las capturas y reunir sus cortes.

### Figura [C06-F07](#fig-anm-c06-f07)

![La suma divide el error en dos aportes estrictamente menores que ε/2. El producto controla el coeficiente variable por M y elige tolerancias positivas para ambos factores. El segundo aporte puede ser cero; el primero aporta la estrictitud final.](../../assets/books/anm/C06/C06-F07.svg){#fig-anm-c06-f07 fig-alt="La suma divide el error en dos aportes estrictamente menores que ε/2. El producto controla el coeficiente variable por M y elige tolerancias positivas para ambos factores. El segundo aporte puede ser cero; el primero aporta la estrictitud final."}

**Figura [C06-F07](#fig-anm-c06-f07).** El presupuesto de salida determina las tolerancias que pedimos a cada sucesión. El máximo reúne los controles; en el producto la cota fija impide que un coeficiente variable amplifique el error sin control.

En el producto, el aporte con coeficiente M queda estrictamente por debajo de ε/2. El aporte con coeficiente |B| puede ser cero y sólo necesita la cota no estricta escrita en la prueba. La suma final sigue siendo estrictamente menor que ε, incluido B=0.

Como primer uso, las convergencias $h_n\to0$ y $t_n\to3$ acreditan $h_nt_n\to0$. Además, aplicando la regla con ambos factores iguales a h, obtenemos $h_n^2=1/(n+1)^2\to0$. Este segundo ejemplo usa el caso $B=0$ que la prueba acaba de cubrir.

También puede converger un producto sin que converjan todos sus factores: $q_n\cdot0=0$ para todo n, aunque q no tiene límite real. La regla es una herramienta suficiente bajo sus hipótesis; una identidad particular puede acreditar otros casos sin satisfacerlas.

### Denominador: margen, objeto y estimación

Para multiplicar no había restricciones sobre los valores de los términos. Dividir requiere comprobar que el denominador sea no nulo en cada índice donde se use. Un límite no nulo proporciona ese control en una cola, pero no garantiza nada semejante sobre el prefijo.

Supongamos $b_n\to B$ con $B\ne0$. Resolveremos el problema en pasos: obtener una separación uniforme de cero; construir una sucesión con dominio completo; estimar su error de inverso; transferir convergencia; usar el producto para el cociente.

**Margen frente a cero.** Como $|B|/2>0$, la convergencia de b proporciona $T\in\mathbb N$ tal que $|b_n-B|<|B|/2$ para todo $n\ge T$. La triangular, escrita como $|B|\le|B-b_n|+|b_n|$, da entonces

$$
|b_n|\ge |B|-|b_n-B|>\frac{|B|}{2}>0.
$$

Desde T, los términos de b son no nulos y su magnitud tiene una cota inferior fija. La hipótesis $B\ne0$ permitió elegir una tolerancia positiva y obtener esa separación. La estimación cubre tanto $B>0$ como $B<0$.

**Una función definida antes de estimar.** Puede haber ceros entre los términos con índice menor que T. Por eso no declaramos todavía que el recíproco de b sea una sucesión real definida en todo $\mathbb N$. Construimos la función $c:\mathbb N\to\mathbb R$ por

$$
c_n=
\begin{cases}
0,& n<T,\\
1/b_n,& n\ge T.
\end{cases}
$$

En el prefijo asignamos el valor real 0. En la cola tomamos el recíproco, permitido por el margen demostrado. Cada índice tiene exactamente un valor real, de modo que c sí es una sucesión con dominio $\mathbb N$. El cero asignado al prefijo es una elección de extensión; no es el recíproco de un denominador nulo.

> **Regla del inverso extendido.** Si $b_n\to B\ne0$, la sucesión c recién definida converge a $1/B$. Cualquier otra asignación de valores reales en el prefijo, conservando $c_n=1/b_n$ desde T, tiene el mismo límite.

**Estimación y demostración.** Para todo $n\ge T$, tanto $b_n$ como B son no nulos. Podemos calcular

$$
\left|c_n-\frac1B\right|
=\left|\frac1{b_n}-\frac1B\right|
=\frac{|b_n-B|}{|b_n||B|}
\le\frac{2}{|B|^2}|b_n-B|.
$$

El margen da la última comparación: el denominador $|b_n||B|$ está separado de cero por $|B|^2/2$. La constante $C=2/|B|^2$ es positiva y fija.

Definamos las sucesiones de error $u_n=b_n-B$ y $v_n=c_n-1/B$. La identidad de errores de §6.5 acredita $u_n\to0$. La comparación eventual $|v_n|\le C|u_n|$ permite aplicar el lema de transferencia, y obtenemos $v_n\to0$. La misma identidad, aplicada ahora a c, concluye $c_n\to1/B$.

Podemos hacer visible el testigo. Recibida una tolerancia $\varepsilon>0$, pedimos a b el error menor que $\varepsilon|B|^2/2$, obtenemos un umbral $N_b$ y usamos $N=\max\{T,N_b\}$. Para todo $n\ge N$, la estimación del inverso produce un error menor que ε.

Si otra extensión $\widetilde c:\mathbb N\to\mathbb R$ toma valores reales distintos antes de T y coincide con el recíproco desde T, entonces $\widetilde c_n=c_n$ para todo $n\ge T$. Por coincidencia eventual, $\widetilde c_n\to1/B$. Las funciones pueden ser distintas, aunque sus límites sean el mismo número.

Si todos los términos de b son no nulos, existe además la sucesión recíproca global $r_n=1/b_n$. Coincide con c desde T, así que también converge a $1/B$. Sólo bajo esa condición global escribimos el recíproco sin una extensión ni una restricción de dominio.

La lectura geométrica del margen consiste en una ventana alrededor de B que no toca cero. Una cola queda dentro de esa ventana; el prefijo puede contener ceros. El recorrido «margen, definición de c, estimación, transferencia» describe los subobjetivos de la prueba. La recta de valores y los índices de la función representan objetos matemáticos distintos de ese recorrido lógico.

La figura [C06-F08](#fig-anm-c06-f08) distingue tres tareas: separar los valores de cero, definir una función en todo el dominio y controlar su error. El carril inferior resume la prueba; los paneles superiores representan valores e índices.

### Figura [C06-F08](#fig-anm-c06-f08)

![Ventanas de candidatos positivos y negativos quedan separadas de cero. Dos filas muestran un denominador con ceros iniciales y una extensión del inverso que asigna cero al prefijo. Sólo desde T=2 se calculan recíprocos. El carril lógico describe los subobjetivos de la prueba.](../../assets/books/anm/C06/C06-F08.svg){#fig-anm-c06-f08 fig-alt="Ventanas de candidatos positivos y negativos quedan separadas de cero. Dos filas muestran un denominador con ceros iniciales y una extensión del inverso que asigna cero al prefijo. Sólo desde T=2 se calculan recíprocos. El carril lógico describe los subobjetivos de la prueba."}

**Figura [C06-F08](#fig-anm-c06-f08).** El límite no nulo separa de cero una cola del denominador. Los ceros iniciales requieren declarar otra sucesión extendida; sólo después tiene sentido estimar su inverso tardío.

Las ventanas para candidatos de ambos signos evitan cero. Los ceros del prefijo no tienen recíproco: en la fila extendida se les asignan valores declarados. El ejemplo numérico B=1 y T=2 se verifica a continuación; el margen y la estimación de la prueba valen para cualquier B no nulo.

Como primer uso, recordemos $s_n=(-1)^n/(n+1)\to0$, probado en §6.3. La suma con la constante 1 da $1+s_n\to1$. Definamos ahora $b_0=b_1=0$ y $b_n=1+s_n$ para $n\ge2$. Por coincidencia eventual, $b_n\to1$. Para $n\ge2$ tenemos $|s_n|\le1/3$, de modo que $b_n\ge2/3>1/2$; podemos elegir $T=2$.

La extensión $c_0=c_1=0$, $c_n=1/b_n$ para $n\ge2$, converge a 1. No hemos definido recíprocos de los dos ceros iniciales: hemos asignado dos valores y demostrado que esa asignación no altera la conclusión tardía.

Para un ejemplo con límite negativo, $d_n=-2+1/(n+1)$ converge a −2 por §6.3. Cada término es menor o igual que −1, por lo que ninguno es cero. La regla acredita que la sucesión global $1/d_n$ converge a $-1/2$; no exige que el límite del denominador sea positivo.

**Cociente.** Sean ahora $a_n\to A$ y $b_n\to B\ne0$, y sea c una extensión del recíproco de b como la anterior. Definamos $z:\mathbb N\to\mathbb R$ por $z_n=a_nc_n$. El inverso acreditó $c_n\to1/B$; la regla del producto da

$$
z_n\to A\frac1B=\frac AB.
$$

Desde T, $z_n=a_n/b_n$. Antes de T, esta construcción asigna 0. Cualquier función real de dominio $\mathbb N$ que coincida con ese cociente desde T converge también a $A/B$, por coincidencia eventual. Así el cociente extendido está bien definido antes de que se le atribuya un límite.

Si $b_n\ne0$ para todo n, la función $z_n=a_n/b_n$ ya tiene dominio natural completo, y la conclusión se aplica a ese cociente global. Si sólo sabemos no anulación desde T, también podemos trabajar sin extensión con la cola reindexada $y_k=a_{T+k}/b_{T+k}$ para $k\in\mathbb N$. Está definida en todos sus índices y es la cola reindexada de z, de modo que $y_k\to A/B$ por §6.4. La restricción de z a los índices originales mayores o iguales que T tiene otro dominio; no la confundimos con y.

En el ejemplo del denominador con dos ceros iniciales, tomemos $a_n=2+1/(n+1)\to2$. El producto con la extensión c acredita $z_n\to2$. Aquí $z_0=z_1=0$ y $z_n=a_n/b_n$ para $n\ge2$. La formulación nombra exactamente la función cuyo límite acabamos de demostrar.

La hipótesis $B\ne0$ tiene un alcance concreto. Si B=0, no hay candidato $1/B$ ni presupuesto positivo $|B|/2$; esta regla no se aplica. Eso no decide por sí solo el comportamiento de cada cociente particular. Por ejemplo, con $h_n=1/(n+1)$, todos los denominadores son positivos y $h_n/h_n=1$ converge a 1, mientras que $h_n^2/h_n=h_n$ converge a 0. En ambos casos el denominador tiende a cero y el cociente está definido en todo $\mathbb N$; las identidades permiten concluir sin invocar la regla de cociente.

Las reglas obtenidas tienen una misma disciplina: comprobar convergencias de entrada, definir la nueva función y justificar los controles que producen su convergencia. En la suma repartimos errores; en el producto gastamos una cota; en el inverso gastamos un margen frente a cero. La conclusión sólo se usa después de haber cubierto esas obligaciones.

### Antes de seguir

#### Microcontrol 41

[]{#MA-MIC-ANM-01-006-041}

Reconstruye la prueba de la suma. ¿En qué orden se eligen la tolerancia de salida, las dos tolerancias de entrada y el umbral común? Da otro reparto positivo que también permita cerrar la estimación.

[]{#MA-MSOL-ANM-01-006-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Con $a_n\to A$ y $b_n\to B$, primero se recibe $\varepsilon>0$, luego se eligen tolerancias auxiliares $\varepsilon/2$ para cada sucesión, después sus cortes $N_a,N_b$ y finalmente $N=\max\{N_a,N_b\}$. Para todo $n\ge N$, la triangular da $|(a_n+b_n)-(A+B)|\le|a_n-A|+|b_n-B|<\varepsilon$. También sirve el reparto $\varepsilon/3$ y $2\varepsilon/3$: ambos son positivos y su suma es la tolerancia de salida.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-006-042}

Demuestra la regla del escalar separando c=0 y c≠0. Después deriva la diferencia usando únicamente escalar y suma, con sus hipótesis explícitas.

[]{#MA-MSOL-ANM-01-006-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Si $a_n\to A$ y $c=0$, el error de $ca_n$ respecto de $cA$ es cero y basta el corte 0. Si $c\ne0$, dado $\varepsilon>0$ pedimos a $a$ la tolerancia $\varepsilon/|c|$; entonces $|ca_n-cA|=|c||a_n-A|<\varepsilon$ en la cola. Para la diferencia suponemos además $b_n\to B$. El escalar −1 da $-b_n\to-B$, y la regla de suma aplicada a $a$ y $-b$ acredita $a_n-b_n\to A-B$.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-006-043}

En la prueba del producto, justifica la identidad de error, explica por qué se necesita una cota fija M≥1 y reconstruye las dos tolerancias auxiliares. ¿Dónde se ha usado la convergencia de a además de pedir un error pequeño?

[]{#MA-MSOL-ANM-01-006-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

La identidad $a_nb_n-AB=a_n(b_n-B)+B(a_n-A)$ se obtiene al sumar y restar $a_nB$. La acotación de $a$, consecuencia de su convergencia, permite elegir $|a_n|\le M$ con $M\ge1$. Usamos tolerancias $\varepsilon/(2M)$ para $b$ y $\varepsilon/[2(|B|+1)]$ para $a$, y reunimos sus cortes. Entonces el error es a lo sumo $M|b_n-B|+|B||a_n-A|$. El primer aporte es menor que $\varepsilon/2$ y el segundo es menor o igual que $\varepsilon/2$, por lo que el total es menor que $\varepsilon$. La convergencia de $a$ se gasta tanto en su cota fija como en su captura de error.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-006-044}

Analiza el caso B=0 en la estimación del producto. ¿Por qué el segundo aporte se controla con una desigualdad no estricta y qué aporte asegura la estrictitud final?

[]{#MA-MSOL-ANM-01-006-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Si $B=0$, el segundo aporte $|B||a_n-A|$ es exactamente cero. No se puede conservar una desigualdad estricta al multiplicar por cero: se usa $0\le\varepsilon/2$. El primer aporte cumple $M|b_n-B|<\varepsilon/2$, porque $M\ge1$ es positivo y se pidió la tolerancia $\varepsilon/(2M)$. Ese aporte basta para cerrar el error total estrictamente por debajo de $\varepsilon$, sin dividir por $B$.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-006-045}

Si $b_n\to B\ne0$, demuestra el margen $|b_n|>|B|/2$ desde algún T. ¿Qué autoriza B≠0 y por qué la prueba también cubre B<0?

[]{#MA-MSOL-ANM-01-006-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

Como $B\ne0$, $|B|/2>0$ es una tolerancia legítima. La convergencia da un corte $T$ con $|b_n-B|<|B|/2$ desde él. Por la triangular, $|b_n|\ge|B|-|b_n-B|>|B|/2>0$. La hipótesis autoriza esa escala positiva y la no anulación tardía necesaria para invertir los términos. La prueba sólo usa módulos y también cubre $B<0$.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-006-046}

Supón $b_0=b_1=0$ y $b_n=1+(-1)^n/(n+1)$ para n≥2. Acredita su límite, comprueba un margen desde T=2, define una extensión real del inverso y justifica su convergencia. ¿Cambiar los valores asignados al prefijo cambia el límite o la función?

[]{#MA-MSOL-ANM-01-006-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

La sucesión $s_n=(-1)^n/(n+1)$ converge a cero. Por suma con la constante 1, $1+s_n\to1$; cambiar los dos términos iniciales conserva ese límite, así que $b_n\to1$. Para $n\ge2$, $|s_n|\le1/3$ y $b_n\ge2/3>1/2$, margen válido desde $T=2$. Definimos $c_0=c_1=0$ y $c_n=1/b_n$ para $n\ge2$. Es una función $\mathbb N\to\mathbb R$ y la regla del inverso extendido da $c_n\to1$. Cambiar efectivamente algún valor del prefijo cambia la función; la coincidencia eventual conserva el límite. No se toman recíprocos de los ceros iniciales.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-006-047}

Con $a_n\to A$ y $b_n\to B\ne0$, distingue el cociente global cuando todos los denominadores son no nulos, un cociente extendido desde T y la cola reindexada $a_{T+k}/b_{T+k}$. Indica sus dominios y la herramienta que acredita cada convergencia.

[]{#MA-MSOL-ANM-01-006-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

Si todos los $b_n$ son no nulos, $q_n=a_n/b_n$ es una función $\mathbb N\to\mathbb R$ y la regla del cociente global da $A/B$. Si sólo se garantiza no anulación desde $T$, definimos $z_n=0$ antes de $T$ y $z_n=a_n/b_n$ desde él: la extensión tiene dominio $\mathbb N$ y converge por inverso extendido y producto. La función $y_k=a_{T+k}/b_{T+k}$ también tiene dominio $\mathbb N$, pero sus índices son reindexados; es la cola reindexada de $z$ y converge a $A/B$ por la equivalencia de colas. La restricción a los índices originales desde $T$ tiene dominio $\mathbb N_{\ge T}$ y es otro objeto.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-006-048}

Explica por qué B=0 impide aplicar la regla de cociente sin implicar que todo cociente con ese denominador carezca de límite. Usa las dos identidades con h de esta sección. ¿Permite una suma convergente concluir, sin más hipótesis, que sus sumandos convergen?

[]{#MA-MSOL-ANM-01-006-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Si $B=0$, ni $1/B$ ni $A/B$ son números reales, y la regla no proporciona un límite. Eso no decide todos los cocientes: para $h_n=1/(n+1)>0$, las identidades $h_n/h_n=1$ y $h_n^2/h_n=h_n$ acreditan límites 1 y 0, respectivamente, pese a que el denominador tiende a cero. Una suma convergente tampoco obliga a converger a sus sumandos: $a_n=(-1)^n$ y $b_n=-(-1)^n$ no tienen límite real, pero su suma es la constante cero.

</details>
En §6.7 estudiaremos controles de otro tipo: cómo una desigualdad entre términos se refleja en los límites y cómo dos fronteras con un destino común pueden capturar una sucesión cuyo límite todavía no se conoce.

### Ejercicios de la sección 6.6

#### Ejercicio 24. Un reparto a medida

[]{#MA-EX-ANM-01-006-024}

Sean $a_n\to A$, $b_n\to B$, $c,d\in\mathbb R$ y $0<\theta<1$. Construye una prueba de $ca_n+db_n\to cA+dB$ que reserve $\theta\varepsilon$ al primer error y $(1-\theta)\varepsilon$ al segundo. Trata los coeficientes nulos y da un ejemplo de reparto no simétrico.

[]{#MA-SOL-ANM-01-006-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Si $c,d\ne0$, usamos las tolerancias auxiliares $\theta\varepsilon/|c|$ y $(1-\theta)\varepsilon/|d|$. Tras sincronizar sus umbrales, la identidad del error y la triangular dan $|c(a_n-A)+d(b_n-B)|\le|c||a_n-A|+|d||b_n-B|<\theta\varepsilon+(1-\theta)\varepsilon=\varepsilon$. Si $c=0$ y $d\ne0$, sólo se requiere la segunda captura; su aporte es menor que $(1-\theta)\varepsilon<\varepsilon$. El caso $d=0,c\ne0$ se resuelve con la primera. Si ambos son cero, el error es cero desde el índice 0. El valor $\theta=1/3$ reserva un tercio al primer aporte y dos tercios al segundo. Las divisiones se realizan únicamente cuando el coeficiente correspondiente es no nulo.

La [figura C06-F07](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.6 muestra la elección de presupuestos antes de sincronizar. Aquí las fracciones son θ y 1−θ, con los coeficientes c,d; no tienen que ser las dos mitades del panel de suma.

</details>

#### Ejercicio 25. Una cantidad finita de operaciones

[]{#MA-EX-ANM-01-006-025}

Para $m\ge1$, sean $a^{(1)},\ldots,a^{(m)}$ sucesiones con $a^{(j)}_n\to A_j$. Demuestra que la suma de sus términos converge a $\sum_{j=1}^m A_j$ y que su producto converge a $\prod_{j=1}^m A_j$. Usa inducción y las reglas binarias demostradas. Describe también el caso de familia vacía con las convenciones usuales.

[]{#MA-SOL-ANM-01-006-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Para $m=1$ ambas afirmaciones son las hipótesis. Si valen para una familia de tamaño $m$, la sucesión de sumas parciales tiene límite $S_m=\sum_{j=1}^m A_j$. La regla binaria de suma, aplicada a esa sucesión y a $a^{(m+1)}$, produce límite $S_m+A_{m+1}$. Del mismo modo, la sucesión de productos parciales tiene límite $P_m=\prod_{j=1}^m A_j$ y la regla binaria del producto da $P_mA_{m+1}$. Cada paso usa convergencias ya acreditadas, incluso si algún $A_j=0$. Todas las operaciones son entre reales y definen sucesiones en $\mathbb N$. Para $m=0$, las convenciones de suma vacía 0 y producto vacío 1 dan sucesiones constantes con esos límites. La inducción sólo autoriza familias finitas; no demuestra una regla de suma o producto infinito.

</details>

#### Ejercicio 26. Leer un producto al revés

[]{#MA-EX-ANM-01-006-026}

Se afirma: «Si $a_nb_n$ converge, ambos factores convergen». Refuta la afirmación con un producto idénticamente cero y con un producto idénticamente no nulo. En el segundo caso comprueba que ninguno de los factores tiene límite real.

[]{#MA-SOL-ANM-01-006-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Para el producto cero tomamos $a_n=(-1)^n$ y $b_n=0$. El producto es la constante cero, pero $a$ toma 1 y −1 arbitrariamente tarde y no tiene límite real, por el argumento de separación. Para el producto no nulo elegimos $a_n=b_n=(-1)^n$. Ambos factores carecen de límite real por la misma separación, mientras que $a_nb_n=1$ para todo índice y, por tanto, el producto converge a 1. La regla del producto parte de la convergencia de cada factor para controlar dos errores; su conclusión no contiene información suficiente para recuperar esos controles. La convergencia del producto puede ocultar oscilaciones que se compensan entre los factores.

</details>

#### Ejercicio 27. Un factor pequeño y otro acotado

[]{#MA-EX-ANM-01-006-027}

Supón $u_n\to0$ y $|p_n|\le M$ desde $T$, con $M\ge0$ fijo. Prueba $u_np_n\to0$ sin suponer convergencia de $p$. Da un ejemplo en que esa última convergencia falle.

[]{#MA-SOL-ANM-01-006-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

La identidad $|u_np_n|=|u_n||p_n|$ da $|u_np_n|\le M|u_n|$ desde $T$. Si $M=0$, el producto es cero en esa cola y converge a cero. Si $M>0$, para $\varepsilon>0$ escogemos un corte $K$ de $u$ con tolerancia $\varepsilon/M$; el umbral $\max\{T,K\}$ da $|u_np_n|<\varepsilon$ en todos los índices posteriores. Es el mecanismo de transferencia de §6.5, no la regla binaria del producto con dos límites. Por ejemplo, $u_n=1/(n+1)$ y $p_n=(-1)^n$: el segundo factor no tiene límite real, pero está acotado por 1 y el producto converge a cero. La cota eventual sustituye aquí el control de un segundo límite.

</details>

#### Ejercicio 28. El inverso como conjunto de obligaciones

[]{#MA-EX-ANM-01-006-028}

Supón $b_n\to B\ne0$ y $|b_n|>|B|/2$ desde $T$. Para cualquier prefijo real $x_0,\ldots,x_{T-1}$, define $c^x_n=x_n$ si $n<T$ y $c^x_n=1/b_n$ si $n\ge T$. Organiza la prueba de $c^x_n\to1/B$ en cuatro obligaciones: margen, definición, estimación y transferencia. Compara dos prefijos distintos.

[]{#MA-SOL-ANM-01-006-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

El margen garantiza que $b_n\ne0$ para $n\ge T$; $B\ne0$ hace legítimo $1/B$. Por tanto, cada elección de prefijo define una función $c^x:\mathbb N\to\mathbb R$, incluso si $b$ tiene ceros anteriores. En la cola obtenemos

$$
\left|c^x_n-\frac1B\right|=\frac{|b_n-B|}{|b_n||B|}\le\frac{2}{|B|^2}|b_n-B|.
$$

El error $b_n-B$ tiende a cero por la identidad de §6.5. Su comparación con la constante positiva $2/|B|^2$ permite transferir la convergencia al error de $c^x$, sincronizando con $T$. Así $c^x_n\to1/B$. Este orden importa: estimar un inverso sin definirlo previamente dejaría abierta una obligación de dominio. Dos prefijos que difieran en alguna posición producen funciones distintas, pero las estimaciones tardías y el límite son los mismos. Si $T=0$, no hay dos prefijos distintos.

La [figura C06-F08](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.6 separa margen, definición, estimación y transferencia. La elección del prefijo forma parte de definir cˣ; ningún recíproco de cero queda implícito.

</details>

#### Ejercicio 29. Un denominador negativo con ceros

[]{#MA-EX-ANM-01-006-029}

Construye una sucesión $b$ con $b_0=b_1=0$, límite −2 y términos no nulos desde 2. Toma $a_n=3+1/(n+1)$. Define dos sucesiones distintas que extiendan el cociente $a_n/b_n$ desde 2 y demuestra que ambas convergen a −3/2. Comprueba un margen explícito para el denominador.

[]{#MA-SOL-ANM-01-006-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Elegimos $b_n=-2+1/(n+1)$ para $n\ge2$, además de los dos ceros prescritos. La sucesión dada por esa fórmula en todos los índices converge a −2 por las reglas lineales, y la modificación de dos términos conserva el límite. Para $n\ge2$, $b_n\le-5/3<0$, de modo que $|b_n|\ge5/3>1=|-2|/2$. Definimos $q_0=q_1=0$, $r_0=5,r_1=-7$ y $q_n=r_n=a_n/b_n$ para $n\ge2$. Ambos objetos son sucesiones reales definidas en todo $\mathbb N$ y difieren en el prefijo. Como $a_n\to3$ y $b_n\to-2\ne0$, el cociente extendido con prefijo cero converge a −3/2. La coincidencia eventual transmite ese límite a $r$. El cociente sin extensión no está definido en los índices 0 y 1.

En la [figura C06-F08](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.6, la ventana negativa muestra el mismo mecanismo de separación de cero. La fila numérica B=1 ilustra otro denominador; aquí B=−2, el margen elegido es 1 y el límite del cociente extendido es −3/2.

</details>

#### Ejercicio 30. Tres cálculos que necesitan una auditoría

[]{#MA-EX-ANM-01-006-030}

Examina las propuestas siguientes: (i) $(3n+2)/(2n+5)$ tiene límite «$\lim(3n+2)/\lim(2n+5)$»; (ii) con $h_n=1/(n+1)$, $h_n/h_n$ tiene límite «0/0»; (iii) $(-1)^n/h_n$ tiene límite «un número dividido por 0». Localiza los usos ilegítimos, resuelve los casos (i) y (ii) mediante identidades válidas y decide si (iii) tiene algún límite real sin usar límites infinitos.

[]{#MA-SOL-ANM-01-006-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

En (i) las sucesiones lineales no tienen límites reales finitos: son no acotadas, mientras que toda sucesión convergente es acotada. La regla del cociente no se aplica a esos factores. Sin embargo, como $h_n>0$, la identidad $(3n+2)/(2n+5)=(3-h_n)/(2+3h_n)$ permite usar límites 3 y 2; el resultado es $3/2$, con denominador siempre positivo. En (ii), $h_n\ne0$ en todos los índices y el cociente es exactamente 1, por lo que converge a 1. La expresión $0/0$ no es un número real ni el resultado de la regla. En (iii), el numerador no converge y el límite cero del denominador tampoco habilita la regla. El cociente está definido, pero su módulo es $n+1$, que no está acotado: para cualquier cota real positiva hay un natural mayor, por C03. Así no tiene límite real finito. No se le asigna aquí un límite infinito.

</details>

#### Ejercicio 31. Construir un cociente y revisar su margen

[]{#MA-EX-ANM-01-006-031}

Sean $a_n\to A$ y $b_n\to B$. Determina cuándo puedes proponer coeficientes reales $r,s,t,u$ para los que $D=tA+uB\ne0$ y estudia la expresión $(ra_n+sb_n)/(ta_n+ub_n)$. Justifica un margen eventual, define un cociente real en todo $\mathbb N$ aunque haya ceros iniciales y determina su límite. Da dos ejemplos con $D=0$ que impidan asignar una conclusión única por esa fórmula.

[]{#MA-SOL-ANM-01-006-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Siempre que $(A,B)\ne(0,0)$ puede elegirse $(t,u)=(1,0)$ si $A\ne0$, o $(0,1)$ si sólo $B\ne0$; por ejemplo, tomamos $(r,s)=(1,1)$. Si $A=B=0$, ninguna elección lineal del denominador da $D\ne0$, limitación que debe declararse. Para cualquier elección válida, las reglas lineales dan numerador $P=rA+sB$ y denominador $D\ne0$. La tolerancia $|D|/2$ proporciona un corte $T$ con $|ta_n+ub_n|>|D|/2$. Asignando cero al cociente antes de $T$ y la fórmula desde $T$ definimos una sucesión real cuyo límite es $P/D$. Si $D=0$, la regla deja de decidir: con $a_n=b_n=h_n$, la expresión $a_n/b_n$ es 1; con $a_n=h_n$, $b_n=h_n^2$, es $n+1$ y no tiene límite real por no acotación. En ambos ejemplos $A=B=0$ y los denominadores son no nulos en todos los índices.

</details>
## 6.7. Orden y captura entre dos sucesiones

[]{#MA-SEC-ANM-01-006-007}

Las reglas de §6.6 parten de convergencias conocidas y construyen otras mediante operaciones. Una desigualdad entre términos ofrece un control distinto. Si una sucesión queda por debajo de otra desde algún corte y ambas convergen, ¿qué podemos afirmar sobre sus límites? Y si dos sucesiones con el mismo límite encierran una tercera, ¿podemos demostrar la convergencia de la intermedia sin presuponerla?

En la primera pregunta ya existen los dos límites. En la segunda sólo conocemos los de las fronteras. Mantendremos esa diferencia durante las pruebas: preservar orden entre límites acreditados y construir una captura para un candidato son tareas distintas.

### El orden eventual se conserva en los límites

> **Paso al límite en una desigualdad.** Sean $a,b:\mathbb N\to\mathbb R$ tales que $a_n\to A$ y $b_n\to B$. Si existe $T\in\mathbb N$ con $a_n\le b_n$ para todo $n\ge T$, entonces $A\le B$.

La estrategia recuerda la unicidad. Supondremos que los destinos tienen el orden contrario y elegiremos ventanas suficientemente pequeñas para mantener esa separación. Al reunir las capturas con el corte de la desigualdad, un mismo índice tendría que satisfacer dos órdenes incompatibles.

**Demostración.** Supongamos, buscando una contradicción, que $A>B$. Entonces $d=A-B>0$. La convergencia de a proporciona un umbral $N_a$ para la tolerancia $d/3$, y la de b proporciona un umbral $N_b$ para esa misma tolerancia.

Tomemos $N=\max\{T,N_a,N_b\}$. Para todo $n\ge N$ tenemos $a_n\le b_n$ y, por las dos capturas,

$$
a_n>A-\frac d3,
\qquad
b_n<B+\frac d3.
$$

Pero $A-d/3=B+2d/3>B+d/3$. Por tanto, en cualquier índice $n\ge N$,

$$
a_n>A-\frac d3>B+\frac d3>b_n.
$$

En particular, el índice natural $n=N$ cumple a la vez $a_N>b_N$ y $a_N\le b_N$, contradicción. La suposición $A>B$ es imposible; concluimos $A\le B$.

La prueba reúne tres obligaciones, no sólo las dos convergencias. El corte T autoriza la comparación entre los términos. Si esa comparación comienza tarde, la conclusión sigue siendo válida; no hemos exigido nada sobre el orden de los prefijos.

Como primer uso, supongamos que $x_n\to X$ y que $x_n\ge0$ desde algún corte. La sucesión constante cero converge a 0 y queda eventualmente por debajo de x. El resultado da $0\le X$. De forma semejante, si $x_n\le m$ eventualmente, donde m es un número real fijo, la comparación con la sucesión constante m da $X\le m$. Estas aplicaciones presuponen la convergencia de x: una cota por sí sola no la demuestra.

Por ejemplo, $x_n=2+1/(n+1)$ converge a 2 por §6.3 y satisface $2\le x_n\le3$ para todo n. Comparando con las dos sucesiones constantes obtenemos $2\le X\le3$ para su límite X. Las cotas son compatibles con el valor ya acreditado, pero no bastan por sí solas para identificarlo como 2.

### Una desigualdad estricta puede llegar a una igualdad

Si $a_n<b_n$ desde algún corte, también vale $a_n\le b_n$, así que el resultado anterior permite concluir $A\le B$. No permite reemplazar esa conclusión por $A<B$.

Tomemos $a_n=0$ y $b_n=1/(n+1)$. Para todo índice natural, el denominador es positivo y $a_n<b_n$. La primera sucesión es constante y converge a 0; la segunda converge a 0 por la primera prueba de §6.3. Sus límites son el mismo número, aunque sus términos nunca coincidan en un índice común y las funciones sean distintas.

La separación $b_n-a_n=1/(n+1)$ es positiva en cada índice, pero no tiene un margen positivo uniforme. Para cualquier $\delta>0$, la convergencia de esa diferencia a cero proporciona índices tardíos donde es menor que δ. La estrictitud de cada comparación no mantiene por sí sola una separación entre los destinos.

En la gráfica discreta, los puntos de a están a altura cero y los de b por encima de ellos. Ningún punto se añade en un «índice infinito». La igualdad de límites habla de dos números acreditados por la definición, no de una igualdad de términos finales.

La figura [C06-F10](#fig-anm-c06-f10) muestra una separación positiva en cada índice que no obliga a separar los dos números límite.

### Figura [C06-F10](#fig-anm-c06-f10)

![La sucesión constante cero queda por debajo de cada punto de 1/(n+1). Flechas verticales muestran distancias positivas que no tienen margen uniforme. Las dos convergencias a cero ya están demostradas; no existe un punto final en infinito.](../../assets/books/anm/C06/C06-F10.svg){#fig-anm-c06-f10 fig-alt="La sucesión constante cero queda por debajo de cada punto de 1/(n+1). Flechas verticales muestran distancias positivas que no tienen margen uniforme. Las dos convergencias a cero ya están demostradas; no existe un punto final en infinito."}

**Figura [C06-F10](#fig-anm-c06-f10).** Cada diferencia es positiva, pero no existe aquí un margen positivo uniforme. Las sucesiones son distintas y sus límites son el mismo número.

Las flechas muestran diferencias entre términos, no entre límites. Cada diferencia es positiva y ambas convergencias a cero ya están demostradas; no aparece un término final en un índice infinito.

Un margen fijo sí añade información. Si además sabemos que existe $\delta>0$ con $a_n+\delta\le b_n$ desde algún corte, la regla de suma acredita $a_n+\delta\to A+\delta$. El paso al límite en la desigualdad da $A+\delta\le B$, de donde $A<B$. Aquí la conclusión estricta se justifica por una separación uniforme, no sólo por el símbolo < entre términos.

### Dos fronteras con el mismo destino

Ahora queremos usar el orden para producir una convergencia que aún no conocemos.

> **Teorema del sándwich.** Sean $u,a,v:\mathbb N\to\mathbb R$. Supongamos que $u_n\to L$ y $v_n\to L$ para un mismo $L\in\mathbb R$, y que existe $T\in\mathbb N$ tal que $u_n\le a_n\le v_n$ para todo $n\ge T$. Entonces $a_n\to L$.

No se incluye entre las hipótesis que a converja. Tampoco se obtiene su existencia pasando al límite en $u_n\le a_n\le v_n$: ese procedimiento exigiría disponer previamente de un límite de a. Debemos verificar directamente la definición para el candidato L.

La estrategia usa una parte del control de cada frontera. Para encerrar a en $(L-\varepsilon,L+\varepsilon)$ basta que u quede por encima del extremo inferior y que v quede por debajo del superior. El orden eventual trasladará ambos controles al término intermedio.

Podemos anticipar la lectura con tres gráficas discretas: las fronteras $u_n=-1/(n+1)$ y $v_n=1/(n+1)$, y los valores intermedios $w_n=(-1)^n/(n+1)^2$. La figura [C06-F09](#fig-anm-c06-f09) señala dónde actúan las comparaciones, pero la captura de una cola para cualquier tolerancia tendrá que provenir de la prueba. Estos valores intermedios se estudiarán como primera aplicación después de demostrar el teorema.

La figura [C06-F09](#fig-anm-c06-f09) anticipa el mecanismo de la prueba con las tres sucesiones descritas. La muestra y su ventana no acreditan por sí solas una captura para toda tolerancia.

### Figura [C06-F09](#fig-anm-c06-f09)

![Tres conjuntos discretos se distinguen por triángulos y cruces. En n=0 la intermedia coincide con la frontera superior. Con tolerancia 1/3 y corte 3, ambas fronteras aportan las desigualdades exteriores estrictas que capturan la intermedia. La prueba no presupone que ésta converja.](../../assets/books/anm/C06/C06-F09.svg){#fig-anm-c06-f09 fig-alt="Tres conjuntos discretos se distinguen por triángulos y cruces. En n=0 la intermedia coincide con la frontera superior. Con tolerancia 1/3 y corte 3, ambas fronteras aportan las desigualdades exteriores estrictas que capturan la intermedia. La prueba no presupone que ésta converja."}

**Figura [C06-F09](#fig-anm-c06-f09).** Las fronteras −1/(n+1) y 1/(n+1) convergen a cero. La sucesión intermedia (−1)^n/(n+1)^2 queda entre ellas y, al sincronizar los controles, dentro de cada ventana prescrita.

En el índice 0, w coincide con la frontera superior; esa igualdad está permitida. Para capturar una cola se necesitan los dos controles exteriores estrictos y las comparaciones interiores no estrictas. La demostración siguiente obtiene esos controles sin suponer de antemano que w converja.

**Demostración.** Sea $\varepsilon>0$. De $u_n\to L$ obtenemos un umbral $N_u$ tal que $|u_n-L|<\varepsilon$ para todo $n\ge N_u$. De $v_n\to L$ obtenemos un umbral $N_v$ tal que $|v_n-L|<\varepsilon$ para todo $n\ge N_v$.

Tomemos $N=\max\{T,N_u,N_v\}$. Para cualquier $n\ge N$, las capturas implican $L-\varepsilon<u_n$ y $v_n<L+\varepsilon$. Las desigualdades eventuales están disponibles en ese mismo índice. Por tanto,

$$
L-\varepsilon<u_n\le a_n\le v_n<L+\varepsilon.
$$

De aquí se sigue $L-\varepsilon<a_n<L+\varepsilon$, equivalente a $|a_n-L|<\varepsilon$. Hemos construido, para cada tolerancia positiva, un umbral natural que controla todos los términos posteriores de a. Así $a_n\to L$.

Las comparaciones intermedias son no estrictas. Aunque a coincida con una frontera en algún índice, los extremos abiertos de la ventana proceden de las convergencias exteriores y conservan el error estrictamente menor que ε.

Si $u_n\le a_n$ sólo se sabe desde un corte $T_1$ y $a_n\le v_n$ desde otro $T_2$, podemos tomar primero $T=\max\{T_1,T_2\}$. El umbral final reúne las cuatro obligaciones originales mediante $\max\{T_1,T_2,N_u,N_v\}$. La coincidencia de los comienzos de las comparaciones no es una hipótesis necesaria.

El candidato común L permite usar la misma ventana para ambos controles. La prueba no usa completitud, convergencia monótona ni selección de subsucesiones. Verifica la definición de a con estimaciones ya acreditadas para las fronteras.

### Primer uso: alternancia dentro de fronteras que se estrechan

Definamos ahora $w:\mathbb N\to\mathbb R$ por $w_n=(-1)^n/(n+1)^2$. Tiene $w_0=1$. Acreditaremos su convergencia mediante las dos fronteras recién descritas.

Como $n+1\ge1$ para todo $n\in\mathbb N$, tenemos

$$
|w_n|=\frac1{(n+1)^2}\le\frac1{n+1}.
$$

En consecuencia, $-1/(n+1)\le w_n\le1/(n+1)$ en todos los índices. La frontera superior converge a cero por §6.3; la inferior converge a cero por la regla del escalar −1. El sándwich se aplica con $L=0$ y $T=0$, y acredita $w_n\to0$.

En $n=0$, la frontera superior y w toman el mismo valor 1, mientras que la inferior vale −1. Para $n\ge1$, tenemos $n+1>1$ y $1/(n+1)^2<1/(n+1)$; por tanto w queda estrictamente entre las dos fronteras. La coincidencia inicial es compatible con las hipótesis no estrictas del teorema.

Podemos recuperar un testigo explícito sin calcular el umbral óptimo de w. Dada $\varepsilon>0$, la primera prueba ofrece $N=\lfloor1/\varepsilon\rfloor$ para las dos fronteras, porque ambas tienen error $1/(n+1)$ respecto de cero. Desde ese corte,

$$
-\varepsilon<-\frac1{n+1}\le w_n\le\frac1{n+1}<\varepsilon.
$$

Así $|w_n|<\varepsilon$. El mismo máximo de controles de la prueba general se reduce aquí a N, ya que las comparaciones valen desde 0 y las fronteras comparten testigo.

Al volver a las gráficas discretas, la función de las fronteras queda clara: aportan las dos barreras que sitúan cada término tardío dentro de la ventana prescrita. La alternancia de w no obstaculiza ese control; tampoco se requiere que las sucesiones sean monótonas. Un número finito de puntos dibujados sólo ilustra la estimación, mientras que la prueba la garantiza para todos los índices desde N.

### Qué ocurre si las hipótesis cambian

El destino común es esencial para esta conclusión. La sucesión $q_n=(-1)^n$ satisface $-1\le q_n\le1$ para todo n. Las fronteras constantes convergen a −1 y 1, respectivamente, pero q no tiene ningún límite real, como demostramos en §6.3. Tener dos fronteras convergentes con límites distintos no basta para asegurar que la intermedia converja.

La comparación debe valer en una cola completa. Consideremos las fronteras constantes $u_n=v_n=0$ y definamos $r_n=0$ si n es par y $r_n=1$ si n es impar. Entonces $u_n\le r_n\le v_n$ se cumple en cada índice par, arbitrariamente grande, pero no en ningún índice impar.

Esta r no converge a ningún candidato real A. Como $1\le|A|+|1-A|$, al menos uno de los valores 0 y 1 dista de A al menos $1/2$. Para cada umbral N, los índices $2N$ y $2N+1$ presentan ambos valores; uno de ellos tiene error mayor o igual que $1/2$. La tolerancia $1/2$ refuta cada candidato. Las capturas de las fronteras no sustituyen la desigualdad que falta en parte de la cola.

Podemos cambiar, en cambio, cualquier prefijo sin perder la conclusión, siempre que las comparaciones y las convergencias exteriores sigan acreditadas desde algún corte. El teorema organiza sus obligaciones mediante ese corte; no pide que las desigualdades valgan desde el primer término.

### Antes de seguir

#### Microcontrol 49

[]{#MA-MIC-ANM-01-006-049}

Reconstruye el paso al límite en una desigualdad eventual. Si supones A>B, ¿qué tolerancia eliges y cuáles son los tres controles que reúne el máximo?

[]{#MA-MSOL-ANM-01-006-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

Si $a_n\to A$, $b_n\to B$ y $a_n\le b_n$ desde $T$, suponemos $A>B$ y ponemos $d=A-B>0$. Elegimos tolerancia $d/3$ para las dos convergencias y cortes $N_a,N_b$. Desde $N=\max\{T,N_a,N_b\}$ valen las dos capturas y la comparación eventual. Pero $a_n>A-d/3=B+2d/3>B+d/3>b_n$, contradiciendo $a_n\le b_n$. Luego $A\le B$. El máximo reúne tres controles, incluido el corte de comparación.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-006-050}

Si $x_n\to X$ y $x_n\ge0$ desde algún corte, demuestra X≥0 comparando con una sucesión constante. ¿Permite la sola positividad eventual acreditar la existencia de X?

[]{#MA-MSOL-ANM-01-006-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

La sucesión constante cero converge a 0 y satisface $0\le x_n$ en la cola indicada. El paso al límite en el orden, aplicado a esa constante y a $x_n\to X$, da $0\le X$. La sola positividad eventual no construye un límite: por ejemplo, $x_n=2+(-1)^n$ es positiva y toma 1 y 3 arbitrariamente tarde, por lo que ningún candidato puede capturar todas sus colas en ventanas pequeñas.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-006-051}

Comprueba que $0<1/(n+1)$ en todos los índices y que ambas sucesiones tienen límite cero. Distingue desigualdad entre términos, igualdad de límites e igualdad de funciones.

[]{#MA-MSOL-ANM-01-006-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Para todo $n\in\mathbb N$, $n+1>0$ y por tanto $0<1/(n+1)$. La constante cero converge a cero y la primera prueba de §6.3 acredita el mismo destino para $1/(n+1)$. Sus términos están estrictamente ordenados y nunca son iguales; las funciones son distintas. Sus límites son dos números iguales a 0. La comparación estricta entre términos no obliga a una separación estricta de esos números.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-006-052}

Supón $a_n\to A$, $b_n\to B$ y $a_n+\delta\le b_n$ eventualmente para un δ>0 fijo. Justifica A<B con herramientas ya demostradas. ¿Qué hipótesis adicional aporta δ frente a la sola desigualdad estricta?

[]{#MA-MSOL-ANM-01-006-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

La regla de suma da $a_n+\delta\to A+\delta$. Como $a_n+\delta\le b_n$ eventualmente y ambas sucesiones convergen, el paso al límite en el orden produce $A+\delta\le B$. Al ser $\delta>0$, resulta $A<B$. La hipótesis adicional es un margen positivo fijo entre las sucesiones; la sola diferencia positiva en cada índice podría tender a cero y permitir límites iguales.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-006-053}

Reconstruye la prueba del sándwich sin suponer que la sucesión intermedia converge. Identifica qué parte de cada captura exterior se usa y de dónde sale la desigualdad estricta del error.

[]{#MA-MSOL-ANM-01-006-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Dada $\varepsilon>0$, las convergencias de $u,v$ hacia el mismo $L$ proporcionan cortes $N_u,N_v$. Reunimos éstos con el corte $T$ de $u_n\le a_n\le v_n$. Para todo $n\ge\max\{T,N_u,N_v\}$, la parte inferior de la captura de $u$ y la parte superior de la de $v$ dan $L-\varepsilon<u_n\le a_n\le v_n<L+\varepsilon$. Así $|a_n-L|<\varepsilon$. La estrictitud procede de las capturas exteriores; no se supone convergencia previa de $a$.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-006-054}

Si las comparaciones del sándwich empiezan en $T_1=3$ y $T_2=8$, y los controles de sus fronteras para cierta tolerancia empiezan en $N_u=5$ y $N_v=6$, da un umbral común y escribe la cadena que captura el término intermedio.

[]{#MA-MSOL-ANM-01-006-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Tomamos $N=\max\{3,8,5,6\}=8$. Si $n\ge8$, ambas comparaciones y ambas capturas están disponibles. Para el destino exterior común $L$ y la tolerancia considerada, se obtiene $L-\varepsilon<u_n\le a_n\le v_n<L+\varepsilon$. Por tanto, el error del término intermedio respecto de $L$ es menor que $\varepsilon$ en toda la cola desde 8.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-006-055}

Aplica el sándwich a $w_n=(-1)^n/(n+1)^2$ entre las fronteras $-1/(n+1)$ y $1/(n+1)$. Justifica sus límites, la comparación y el caso n=0. ¿Por qué no se exige que w sea monótona ni que las desigualdades intermedias sean estrictas?

[]{#MA-MSOL-ANM-01-006-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Como $n+1\ge1$, $|w_n|=1/(n+1)^2\le1/(n+1)$, de donde $-1/(n+1)\le w_n\le1/(n+1)$. Las fronteras convergen a cero por la primera prueba y la regla del escalar −1. El sándwich da $w_n\to0$. En $n=0$, $w_0=1$ coincide con la frontera superior; desde $n=1$, su módulo es estrictamente menor que $1/(n+1)$. El teorema admite comparaciones no estrictas y no requiere monotonía de la intermedia: las capturas exteriores son las que aseguran el error estricto.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-006-056}

Explica qué hipótesis fallan en los dos contrastes finales: q entre las constantes −1 y 1, y r entre dos fronteras cero sólo en índices pares. ¿Por qué dos fronteras convergentes o comparaciones arbitrariamente tardías no bastan por sí solas?

[]{#MA-MSOL-ANM-01-006-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

En $-1\le q_n=(-1)^n\le1$, las fronteras convergen pero a destinos distintos; falta el candidato exterior común. La separación de los valores de $q$ impide su convergencia. Para $r_n=0$ en índices pares y 1 en impares, las fronteras cero sí tienen destino común, pero sólo en los pares se cumple $0\le r_n\le0$. No existe un corte desde el que esa comparación valga para todos los índices. Los impares arbitrariamente tardíos refutan el candidato 0. Cada una de las dos hipótesis ausentes es necesaria para aplicar el sándwich.

</details>
Ya podemos distinguir tres usos de una desigualdad: acotar valores, preservar orden entre límites conocidos y producir una convergencia mediante fronteras con destino común. En §6.8 reuniremos estas herramientas para elegir un argumento y comprobar que sus hipótesis cubren exactamente la conclusión buscada.

### Ejercicios de la sección 6.7

#### Ejercicio 32. Llegar a la frontera de un intervalo

[]{#MA-EX-ANM-01-006-032}

Sean $p<q$ reales, $a_n\to A$ y $p\le a_n\le q$ eventualmente. Prueba $A\in[p,q]$. Decide si la conclusión puede sustituirse por $A\in(p,q)$ cuando todos los términos tardíos están en ese intervalo abierto. Construye un ejemplo que llegue a cada frontera.

[]{#MA-SOL-ANM-01-006-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Las sucesiones constantes $p$ y $q$ convergen a esos números. El paso al límite en las dos desigualdades eventuales da $p\le A\le q$. Si los términos están en $(p,q)$, también satisfacen las comparaciones no estrictas y sólo se conserva, en general, el intervalo cerrado. Para la frontera inferior elegimos $a_n=p+(q-p)/(n+2)$; para la superior, $b_n=q-(q-p)/(n+2)$. Como $0<1/(n+2)\le1/2<1$, ambos términos quedan estrictamente entre $p$ y $q$ en todos los índices. Las reglas lineales y la prueba de esa familia racional dan límites $p$ y $q$, respectivamente. La positividad de una distancia en cada índice no proporciona un margen fijo que excluya un extremo del límite.

</details>

#### Ejercicio 33. Orden estricto y margen uniforme

[]{#MA-EX-ANM-01-006-033}

Construye $a,b$ con $a_n<b_n$ en todos los índices y límite común 2. Construye también $c,d$ con límites distintos y $c_n+\delta\le d_n$ para alguna constante $\delta>0$. Demuestra en general que ese margen, junto con la convergencia de ambos factores, obliga a que el primer límite sea estrictamente menor que el segundo.

[]{#MA-SOL-ANM-01-006-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Tomamos $a_n=2-1/(n+2)$ y $b_n=2+1/(n+2)$; la desigualdad es estricta en todos los índices y los dos límites son 2. Para el segundo ejemplo podemos usar las constantes $c_n=0,d_n=3$ con $\delta=1$. En general, si $c_n\to C$, $d_n\to D$ y $c_n+\delta\le d_n$ eventualmente, las reglas lineales dan $c_n+\delta\to C+\delta$. El orden eventual pasa a los límites, de modo que $C+\delta\le D$. Como $\delta>0$, obtenemos $C<D$. Una desigualdad estricta sin escala positiva fija puede estrecharse hasta la igualdad; el margen uniforme impide ese estrechamiento.

La [figura C06-F10](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.7 ilustra la pérdida de estrictitud entre los límites con otro par de sucesiones que converge a 0. En nuestro primer ejemplo, los dos límites son 2; la diferencia sigue siendo positiva y no posee un margen uniforme.

</details>

#### Ejercicio 34. Dos presupuestos de error exteriores

[]{#MA-EX-ANM-01-006-034}

Sean $r_n,s_n\ge0$ con $r_n\to0$, $s_n\to0$, y supón $L-r_n\le a_n$ desde $T_1$ y $a_n\le L+s_n$ desde $T_2$. Demuestra directamente $a_n\to L$ sin presuponer su convergencia ni exigir que las dos cotas de error coincidan.

[]{#MA-SOL-ANM-01-006-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Dada $\varepsilon>0$, elegimos cortes $N_r,N_s$ para que $r_n<\varepsilon$ y $s_n<\varepsilon$ en las respectivas colas; el valor absoluto de cada término coincide con él por no negatividad. Tomamos $N=\max\{T_1,T_2,N_r,N_s\}$. Para todo $n\ge N$ tenemos $L-\varepsilon<L-r_n\le a_n\le L+s_n<L+\varepsilon$. Las dos desigualdades exteriores son estrictas por las capturas de $r$ y $s$, aunque las comparaciones interiores no lo sean. La cadena equivale a $|a_n-L|<\varepsilon$ y establece la convergencia buscada desde la definición. Las cotas pueden decrecer de modos distintos, oscilar o alcanzar cero; únicamente importa que cada una permita responder a la misma tolerancia.

La [figura C06-F09](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.7 permite seguir los dos controles exteriores. Aquí rₙ y sₙ pueden ser distintos y se reúnen cuatro cortes; no se trasladan sin cambio el radio ni el corte numérico del ejemplo dibujado.

</details>

#### Ejercicio 35. Una frontera conocida sólo por su módulo

[]{#MA-EX-ANM-01-006-035}

Se propone: «$u_n\le a_n\le v_n$ eventualmente, $|u_n|\to1$ y $v_n\to1$; por el sándwich, $a_n\to1$». Refuta la propuesta con un ejemplo en que $u$ no tenga límite real. Formula una reparación sobre la frontera inferior y justifica el resultado.

[]{#MA-SOL-ANM-01-006-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Ponemos $u_n=a_n=(-1)^n$ y $v_n=1$. Las comparaciones valen en todos los índices, $|u_n|=1$ converge a 1 y $v$ es constante. Sin embargo, $a$ y $u$ no tienen límite real, pues sus valores 1 y −1 reaparecen arbitrariamente tarde. La hipótesis sobre el módulo no determina el destino de la frontera inferior. Una reparación es exigir $u_n\to1$, manteniendo $v_n\to1$ y las comparaciones eventuales: ahora el sándwich sí produce $a_n\to1$. Una reparación más fuerte que basta para recuperar esa convergencia es añadir $u_n\ge0$ eventualmente a la condición original; entonces $u_n=|u_n|$ en una cola y la coincidencia eventual da $u_n\to1$.

</details>

#### Ejercicio 36. Una caracterización por fronteras

[]{#MA-EX-ANM-01-006-036}

Prueba que $a_n\to L$ equivale a la existencia de sucesiones $u,v$ tales que $u_n\le a_n\le v_n$ eventualmente y $u_n,v_n\to L$. En la dirección que construye fronteras desde $a$, procura que éstas tengan fórmulas distintas y justifica la captura sin importar resultados posteriores.

[]{#MA-SOL-ANM-01-006-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Si existen esas fronteras, el sándwich probado en §6.7 da $a_n\to L$ sin suponer la conclusión. Para la dirección inversa, partimos de $a_n\to L$ y construimos $u_n=a_n-1/(n+1)$ y $v_n=a_n+1/(n+1)$. Son funciones reales en $\mathbb N$ y satisfacen $u_n<a_n<v_n$ en todos los índices, además de $u_n\ne v_n$. La convergencia de $1/(n+1)$ a cero y las reglas lineales acreditan $u_n,v_n\to L$. No se usa el sándwich para probar aquí la convergencia de $a$, que ya es una hipótesis de esta dirección. Las dos implicaciones tienen puntos de partida distintos; confundirlos produciría una circularidad.

</details>
## 6.8. Elegir un argumento y comprobar su alcance

Al comenzar el capítulo, demostrar una convergencia significaba encontrar una respuesta para cada tolerancia. Las herramientas que hemos obtenido permiten organizar esas respuestas: transferir errores, combinar convergencias, controlar un denominador o capturar una sucesión entre dos fronteras. Elegir una herramienta requiere reconocer qué sabemos y qué estamos intentando demostrar.

En esta sección volveremos a esas decisiones sin introducir un resultado nuevo. El propósito es que puedas explicar por qué un argumento se aplica, qué función está estudiando y qué conclusión ha quedado acreditada.

### Identificar la obligación antes de calcular

La expresión de una sucesión puede sugerir un candidato, pero no determina por sí sola el tipo de prueba que necesitamos. Conviene empezar escribiendo la afirmación exacta.

Para acreditar $a_n\to A$, debemos responder a cada $\varepsilon>0$ con un $N\in\mathbb N$ tal que $|a_n-A|<\varepsilon$ para todo índice $n\ge N$. N puede depender de ε y de los datos fijos del problema, pero no del índice n que luego recorrerá la cola.

Para refutar ese candidato A, la obligación cambia: debemos encontrar una tolerancia $\varepsilon_0>0$ tal que, para cada umbral N, exista un índice $n\ge N$ con $|a_n-A|\ge\varepsilon_0$. La igualdad en la frontera ya infringe el error estrictamente menor que la tolerancia.

Para demostrar que no hay ningún límite real, hay que refutar todos los candidatos. La forma lógica completa es

$$
\forall A\in\mathbb R\ \exists\varepsilon_0>0\
\forall N\in\mathbb N\ \exists n\in\mathbb N:
\quad n\ge N\ \text{y}\ |a_n-A|\ge\varepsilon_0.
$$

La tolerancia de refutación puede depender de A. En algunos ejemplos, como $(-1)^n$, una misma tolerancia sirve para todos los candidatos, pero esa ventaja no es una exigencia de la negación.

Acreditar convergencia, refutar un candidato y refutar todos los candidatos son tareas distintas. También lo es demostrar sólo acotación. Una banda fija puede resolver esta última tarea; una prueba de convergencia debe responder a cualquier radio positivo.

### Elegir una herramienta a partir de los datos

Las formas de una fórmula orientan la búsqueda, pero las hipótesis disponibles deciden si una regla está autorizada.

| Datos que podemos acreditar | Herramienta disponible | Obligación que permanece |
|---|---|---|
| Una fórmula manejable para $\lvert a_n-A\rvert$ | Definición y umbral explícito | Controlar todos los índices desde N, incluida la desigualdad estricta |
| Un error conocido $u_n\to0$ y $\lvert a_n-A\rvert\le C\lvert u_n\rvert$ eventualmente, con C fijo no negativo | Identidad de errores y transferencia | Justificar la comparación y reunir su corte con el de u |
| Convergencias de los sumandos o factores | Reglas de §6.6 | Verificar cada convergencia de entrada y definir la función resultante |
| Un denominador con límite B distinto de cero | Margen, inverso y cociente | Comprobar dominio global o declarar extensión o cola reindexada |
| Dos fronteras con el mismo límite y comparaciones eventuales | Sándwich | Reunir ambas capturas y todos los cortes de comparación |
| Dos sucesiones eventualmente iguales, o una cola reindexada | Transferencia de §6.4 | Identificar la igualdad o la traducción de índices que se está usando |

La tabla reúne herramientas ya demostradas; no convierte una semejanza de fórmulas en una hipótesis. Para aplicar el producto hacen falta convergencias de ambos factores. Un factor acotado y otro que tiende a cero pueden sugerir una transferencia de errores, pero la regla del producto no atribuye un límite al factor sólo por estar acotado.

La elección tampoco exige usar siempre la herramienta más elaborada. Una identidad sencilla puede hacer inmediata una estimación directa. Una regla ya probada puede ahorrar esa reconstrucción. Lo decisivo es que el argumento elegido deje visibles sus datos y cierre la obligación exacta.

### Una misma convergencia por dos recorridos

Consideremos la función $f:\mathbb N\to\mathbb R$ dada por $f_n=(2n+1)/(n+2)$. Como $n+2>0$ para todo índice natural, f está definida en todo su dominio. Queremos acreditar el candidato 2.

**Recorrido directo.** La identidad $f_n=2-3/(n+2)$ da $|f_n-2|=3/(n+2)$. Recibida una tolerancia $\varepsilon>0$, elegimos $N=\lfloor3/\varepsilon\rfloor$. La propiedad del piso demostrada en §6.3 asegura $N+1>3/\varepsilon$. Si $n\ge N$, entonces $n+2\ge N+2>3/\varepsilon$, y obtenemos $|f_n-2|<\varepsilon$. El testigo es natural, no depende del n posterior y sirve para toda la cola. Así $f_n\to2$.

**Recorrido mediante reglas.** Tomemos $h_n=1/(n+1)$, cuya convergencia a cero ya está acreditada. Podemos escribir

$$
f_n=\frac{2-h_n}{1+h_n}.
$$

La identidad se comprueba en cada índice multiplicando numerador y denominador por el número positivo $n+1$. Las reglas de escalar y suma dan $2-h_n\to2$ y $1+h_n\to1$. El límite del denominador es no nulo y, además, todos sus términos son positivos. La regla del cociente se aplica a la función global y concluye $f_n\to2$.

El primer recorrido ofrece de inmediato un testigo concreto. El segundo muestra cómo la expresión se construye a partir de convergencias conocidas. Ambos acreditan la misma función y el mismo candidato. La unicidad asegura que, si otra prueba propusiera un límite real distinto para f, las conclusiones no podrían ser simultáneamente correctas.

No sería válido calcular primero el cociente de unos supuestos límites de $2n+1$ y $n+2$: no hemos acreditado convergencias reales de esas dos sucesiones. La reescritura mediante h aporta precisamente las hipótesis que el cociente necesita.

Podemos refutar también el candidato 3 sin negar la convergencia de f. Para todo n tenemos $f_n=2-3/(n+2)<2$, así que $|f_n-3|>1$. La tolerancia 1 y el índice $n=N$ infringen la captura respecto de 3 para cualquier corte N. Hemos refutado 3; la prueba anterior acredita 2. Una refutación local no equivale a ausencia de límite real.

### Cuando un factor sólo está controlado

Supongamos que $p:\mathbb N\to\mathbb R$ es una sucesión de la que sólo sabemos lo siguiente: existe $T\in\mathbb N$ tal que $|p_n|\le5$ para todo $n\ge T$. No se nos da un límite de p. Definamos $x_n=3+p_n/(n+1)$ en todo $\mathbb N$.

La fórmula de producto no autoriza multiplicar un supuesto límite de p por el de $1/(n+1)$. En cambio, los datos proporcionan directamente, para $n\ge T$,

$$
|x_n-3|=\frac{|p_n|}{n+1}\le\frac5{n+1}.
$$

El error conocido $h_n=1/(n+1)$ tiende a cero. La identidad de errores y la transferencia con $C=5$ acreditan $x_n\to3$. Para una tolerancia ε, podemos pedir a h la tolerancia ε/5 y usar el corte $N=\max\{T,\lfloor5/\varepsilon\rfloor\}$. La comparación eventual y el control del error están disponibles desde ese mismo N.

También podemos organizar los mismos datos como un sándwich. De $|p_n|\le5$ y $n+1>0$ se sigue, desde T,

$$
3-\frac5{n+1}\le x_n\le3+\frac5{n+1}.
$$

Las fronteras convergen a 3 por escalar y suma. El sándwich acredita de nuevo $x_n\to3$ sin suponer convergencia de p ni de x entre sus hipótesis.

Ambos argumentos aprovechan un control de magnitud. Si elegimos, por ejemplo, $p_n=(-1)^n$, p no tiene límite real, pero cumple la cota requerida y la conclusión sobre x sigue siendo válida. Una hipótesis de convergencia sería aquí más fuerte que los datos que la prueba necesita.

La lectura geométrica recoge relaciones ya usadas en el capítulo: el error de x queda dominado por un error que se hace pequeño, o x queda entre dos fronteras que capturan la misma cola alrededor de 3. Las gráficas son conjuntos discretos de puntos; las estimaciones justifican la afirmación sobre toda la cola.

### Revisar función, índices y conclusión

Antes de dar por terminado un argumento, podemos recorrerlo con cuatro preguntas.

**¿Qué función está definida?** Si aparece un cociente, comprobamos cada denominador donde se evalúa. Ante ceros iniciales, nombramos la extensión o la cola reindexada, en lugar de atribuir un dominio completo a una fórmula que no lo tiene. Cambiar un prefijo puede conservar el límite sin conservar la igualdad de funciones.

**¿Qué datos autorizan la herramienta?** En el producto buscamos convergencias de entrada y la cota usada en su prueba. En el inverso buscamos un límite no nulo. En el sándwich buscamos un destino exterior común y dos comparaciones eventuales. Si falta una hipótesis, la regla queda fuera de alcance; el comportamiento del ejemplo puede requerir otro argumento.

**¿Qué índice debe cumplir todos los controles?** Una prueba que reúne obligaciones toma sus umbrales después de elegir las tolerancias auxiliares. El máximo debe incluir también los cortes de igualdad, desigualdad o no anulación que autoricen el cálculo. En una cola reindexada, k y T+k pertenecen a las funciones correspondientes; no se sustituyen índices sin esa traducción.

**¿Qué se ha demostrado exactamente?** El paso al límite en desigualdades concluye un orden no estricto, salvo que se añada un margen que justifique más. La unicidad no construye un límite. La acotación no acredita convergencia. Refutar un candidato no refuta los demás. La conclusión escrita debe coincidir con la obligación que el argumento resolvió.

Estas preguntas permiten localizar un defecto concreto. Si un supuesto testigo depende del n que pretende controlar, hay un problema en el orden de elecciones. Si el error queda sólo menor o igual que ε, falta cerrar la estrictitud. Si se infiere permanencia desde unos pocos puntos, falta una estimación sobre todos los índices tardíos. La corrección consiste en reparar esa obligación, no en añadir una afirmación más fuerte al final.

### Antes de seguir

#### Microcontrol 57

[]{#MA-MIC-ANM-01-006-057}

Escribe las obligaciones lógicas de acreditar $a_n\to A$, refutar ese candidato y demostrar ausencia de todo límite real. Indica de qué datos puede depender la tolerancia de refutación en la última tarea.

[]{#MA-MSOL-ANM-01-006-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Acreditar $a_n\to A$ exige $\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\ge N:\ |a_n-A|<\varepsilon$. Refutar ese candidato exige $\exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists n\ge N:\ |a_n-A|\ge\varepsilon_0$. Para excluir todo límite real se antepone $\forall A\in\mathbb R$ a esta última obligación. La tolerancia puede depender de la sucesión fijada y de $A$, pero debe quedar elegida antes del corte $N$ y del índice infractor posterior.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-006-058}

Para $f_n=(2n+1)/(n+2)$, reconstruye el recorrido directo hacia 2 y verifica el testigo con ε=1/2. ¿Qué asegura que el corte controla una cola completa y no un único término?

[]{#MA-MSOL-ANM-01-006-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

Como $n+2>0$, la identidad $f_n=2-3/(n+2)$ da error $3/(n+2)$. Para $\varepsilon>0$, tomamos $N=\lfloor3/\varepsilon\rfloor$; si $n\ge N$, $n+2\ge N+2>3/\varepsilon$, luego el error es menor que $\varepsilon$. Con $\varepsilon=1/2$, el testigo es 6 y, para cualquier $n\ge6$, el error es a lo sumo $3/8<1/2$. La desigualdad se verificó para un índice arbitrario posterior al corte; no sólo en el índice 6.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-006-059}

Reconstruye el recorrido de f mediante h y las reglas de cálculo. Verifica la identidad y la no anulación del denominador. ¿Qué hipótesis faltarían si intentaras aplicar el cociente directamente a las sucesiones $2n+1$ y $n+2$?

[]{#MA-MSOL-ANM-01-006-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Con $h_n=1/(n+1)\to0$, se tiene $f_n=(2-h_n)/(1+h_n)$: multiplicar numerador y denominador por $n+1>0$ recupera $(2n+1)/(n+2)$. Las reglas lineales dan límites 2 y 1 para las nuevas sucesiones. Además, $1+h_n>0$ en todo índice, así que el cociente global está definido y converge a 2. Aplicar directamente la regla a $2n+1$ y $n+2$ exigiría convergencias reales finitas de ambos factores, que no están disponibles: ambas sucesiones son no acotadas y no pueden tener tales límites.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-006-060}

Refuta el candidato 3 para f con una tolerancia y un infractor posteriores a cualquier corte. Explica por qué esta refutación es compatible con la convergencia acreditada hacia 2.

[]{#MA-MSOL-ANM-01-006-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

La identidad $f_n=2-3/(n+2)<2$ vale en todos los índices. Luego $|f_n-3|=3-f_n=1+3/(n+2)>1$. Fijamos la tolerancia 1 y, para cualquier corte $N$, elegimos el infractor $n=N$. Se refuta el candidato 3, mientras que las pruebas anteriores acreditan el candidato 2. Las afirmaciones son compatibles: la refutación de un destino incorrecto no niega la convergencia a otro.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-006-061}

Si $|p_n|\le5$ desde T y $x_n=3+p_n/(n+1)$, demuestra $x_n\to3$ mediante transferencia. Explica por qué no necesitas conocer un límite de p y qué corte reúne las dos obligaciones.

[]{#MA-MSOL-ANM-01-006-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

Sea $h_n=1/(n+1)\to0$ y $v_n=x_n-3=p_n/(n+1)$. Desde $T$, $|v_n|\le5h_n$, así que la transferencia con $C=5$ da $v_n\to0$ y la identidad de errores da $x_n\to3$. Para $\varepsilon>0$, podemos usar $N=\max\{T,\lfloor5/\varepsilon\rfloor\}$: reúne la cota de $p$ con la captura de $h$ para $\varepsilon/5$. Sólo se necesita la magnitud eventual de $p$, no una convergencia suya.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-006-062}

Resuelve el mismo problema de x mediante sándwich. Identifica las fronteras, sus límites y las comparaciones. ¿En qué parte del argumento producirías una circularidad si dieras por supuesta la convergencia de x?

[]{#MA-MSOL-ANM-01-006-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

Desde $T$, la cota $|p_n|\le5$ y el denominador positivo dan $3-5/(n+1)\le x_n\le3+5/(n+1)$. Las fronteras $u_n=3-5h_n$ y $v_n=3+5h_n$ convergen a 3 por reglas lineales. El sándwich acredita $x_n\to3$ sin suponer su convergencia. Sería circular pasar al límite en las dos comparaciones atribuyendo previamente un límite a $x$, pues justamente su existencia y su candidato deben producirse mediante la captura exterior.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-006-063}

Para un denominador que sólo es no nulo desde T, distingue una extensión real del cociente de su cola reindexada. ¿Qué debe verificarse sobre sus dominios antes de usar las reglas y qué conserva una modificación del prefijo?

[]{#MA-MSOL-ANM-01-006-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

Si $b_n\ne0$ sólo desde $T$, una extensión $z:\mathbb N\to\mathbb R$ asigna valores reales antes de $T$ y pone $z_n=a_n/b_n$ desde él. La cola reindexada $y_k=a_{T+k}/b_{T+k}$ también tiene dominio $\mathbb N$, pero elimina el prefijo y usa otra correspondencia de índices. Antes de calcular se comprueba no anulación en cada evaluación y se identifica cuál función está definida. Para aplicar la regla del cociente se requieren además $a_n\to A$, $b_n\to B\ne0$. Bajo esas hipótesis, extensión y reindexación tienen límite $A/B$. Una modificación del prefijo conserva el límite, aunque pueda cambiar la función.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-006-064}

Elige dos afirmaciones erróneas examinadas en el capítulo, entre acotación que supuestamente implica convergencia, orden estricto que supuestamente da límites distintos y refutación de un candidato que supuestamente elimina todo límite. Refuta cada una con un ejemplo ya demostrado e identifica la conclusión válida que sí permanece.

[]{#MA-MSOL-ANM-01-006-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Elegimos las dos primeras afirmaciones. La sucesión $(-1)^n$ es acotada por 1, pero no tiene límite real: la triangular separa alguno de sus valores persistentes de cada candidato. La conclusión válida que queda es que convergencia implica acotación, no su conversa. Para el orden, las sucesiones $a_n=0$ y $b_n=1/(n+1)$ satisfacen $a_n<b_n$ en todos los índices y ambas convergen a 0. Con convergencias acreditadas y orden eventual se conserva la conclusión no estricta $A\le B$; obtener $A<B$ necesita información adicional, como un margen positivo uniforme.

</details>
La definición sigue siendo el criterio que sostiene las herramientas del capítulo. Ahora podemos leer una propuesta de límite, elegir un método y explicar cómo sus hipótesis producen la captura requerida. Cuando una regla no alcanza, la estimación directa permite volver a la obligación original; cuando alcanza, su demostración explica qué controles podemos reutilizar.

### Ejercicios de la sección 6.8

#### Ejercicio 37. Dos recorridos para una expresión racional

[]{#MA-EX-ANM-01-006-037}

Para $f_n=(5n+2)/(2n+3)$, demuestra su convergencia por una estimación directa del error y por normalización con $h_n=1/(n+1)$. Determina el candidato, construye un testigo suficiente y revisa los denominadores en todo $\mathbb N$.

[]{#MA-SOL-ANM-01-006-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

El candidato es $5/2$. Como $2n+3\ge3>0$, la sucesión está definida y la identidad $f_n-5/2=-11/[2(2n+3)]$ da $|f_n-5/2|=11/(4n+6)$. Para $\varepsilon>0$, tomamos $N=\lfloor11/(4\varepsilon)\rfloor+1$. Si $n\ge N$, $4n+6>11/\varepsilon$ y el error es menor que $\varepsilon$. El recorrido por reglas usa la identidad $f_n=(5-3h_n)/(2+h_n)$. Numerador y denominador convergen a 5 y 2; el segundo es positivo para todo índice, así que el cociente converge a $5/2$. La normalización transforma factores originalmente no acotados en sucesiones con límites finitos. La prueba directa aporta un corte explícito suficiente; la regla del cociente evita reconstruirlo, pero su validez depende de esas convergencias y del límite denominador no nulo.

</details>

#### Ejercicio 38. Una perturbación que conserva el destino

[]{#MA-EX-ANM-01-006-038}

Sea $a_n\to A$. Diseña una sucesión $p$ sin límite real pero eventualmente acotada, y una sucesión $b$ con prefijo arbitrario que desde un corte $T$ satisfaga $b_n=a_n+p_n/(n+1)$. Demuestra $b_n\to A$ e identifica qué partes del argumento no necesitan un límite de $p$.

[]{#MA-SOL-ANM-01-006-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Elegimos $p_n=3(-1)^n$, que está acotada por 3 y no tiene límite real por la separación persistente de 3 y −3. La sucesión $h_n=1/(n+1)$ converge a cero; el ejercicio 27, o la transferencia de errores, da $p_nh_n\to0$ sin suponer un límite de $p$. Definimos primero $c_n=a_n+p_nh_n$ en todos los índices. La regla de suma produce $c_n\to A+0=A$. Finalmente asignamos cualquier prefijo real a $b$ antes de $T$ y ponemos $b_n=c_n$ desde $T$. La coincidencia eventual conserva la convergencia. Los tres controles usados son la cota del factor variable, la convergencia del factor pequeño y la transferencia de un prefijo finito; ninguno exige conocer un destino para $p$.

</details>

#### Ejercicio 39. Qué puede recuperarse de las operaciones

[]{#MA-EX-ANM-01-006-039}

Para sucesiones reales $a,b$, estudia estas afirmaciones, con cocientes globalmente definidos cuando se mencionan: (i) si $a_n+b_n\to S$ y $a_n\to A$, entonces $b_n\to S-A$; (ii) si $a_nb_n\to P$ y $a_n\to A\ne0$, entonces $b_n\to P/A$; (iii) si $a_n/b_n\to Q$ y $b_n\to B$, entonces $a_n\to QB$, incluso si $B=0$; (iv) la convergencia simultánea de la suma y el producto obliga a converger a ambos factores; (v) en (ii) basta $A=0$. Justifica las inferencias o construye contraejemplos.

[]{#MA-SOL-ANM-01-006-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

En (i), $b_n=(a_n+b_n)-a_n$; las reglas lineales prueban el destino indicado. En (ii), la convergencia de $a$ a un número no nulo garantiza un corte desde el que $a_n\ne0$. El cociente tardío $(a_nb_n)/a_n$ converge a $P/A$ al extenderlo, y coincide con $b$ en esa cola; así converge $b$, aunque $a$ tuviera ceros iniciales. En (iii), ponemos $q_n=a_n/b_n$, sucesión global por la hipótesis. La identidad $a_n=q_nb_n$ y la regla del producto dan $QB$, sin dividir por $B$. En (iv), tomamos $a_n=(-1)^n$ y $b_n=-(-1)^n$: suma cero y producto −1 convergen, pero ninguno de los factores converge. En (v), $a_n=0$ y $b_n=(-1)^n$ dan producto cero y $A=0$, sin convergencia de $b$. Recuperar un factor por división necesita el margen que aporta $A\ne0$.

</details>

#### Ejercicio 40. Cambiar todo el orden de los índices

[]{#MA-EX-ANM-01-006-040}

Sea $\pi:\mathbb N\to\mathbb N$ una biyección y $b_n=a_{\pi(n)}$. Demuestra que $a_n\to A$ si y sólo si $b_n\to A$, sin suponer que la permutación conserve el orden ni que $a,b$ coincidan eventualmente. Construye el corte usando la preimagen de un prefijo finito, trata el caso vacío y demuestra la dirección inversa.

[]{#MA-SOL-ANM-01-006-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La composición define $b:\mathbb N\to\mathbb R$. Supongamos $a_n\to A$ y recibamos $\varepsilon>0$, con umbral $K$ para $a$. El conjunto $F=\pi^{-1}(\{0,\ldots,K-1\})$ es finito: por biyectividad, cada uno de los $K$ índices tiene una sola preimagen. Si $F$ es vacío, ponemos $N=0$; en otro caso, $N=1+\max F$. Para todo $n\ge N$, el índice $n$ no pertenece a $F$, por lo que $\pi(n)\ge K$. Luego $|b_n-A|=|a_{\pi(n)}-A|<\varepsilon$. En particular, cuando $K=0$ el prefijo y su preimagen son vacíos. El corte controla posiciones de la permutación que caían en el prefijo original, no el tamaño numérico de $\pi(n)$ por una presunta monotonía.

Si $b_n\to A$, aplicamos el argumento a la biyección inversa $\pi^{-1}$: la identidad $a_n=b_{\pi^{-1}(n)}$ acredita la convergencia de $a$. La inyectividad impide repetir infinitamente un índice inicial; la sobreyectividad permite recuperar todos los índices mediante la inversa. El mecanismo es la finitud de las posiciones problemáticas, no una teoría de subsucesiones.

La figura [C06-F11](#fig-anm-c06-f11) muestra cómo elegir el corte en las posiciones nuevas. El ejemplo de biyección sólo ilustra el conjunto disperso de preimágenes; la finitud que acaba de probarse sostiene el argumento general.

### Figura [C06-F11](#fig-anm-c06-f11)

![En un ejemplo de biyección, el prefijo original 0,1,2 tiene preimágenes 8,5,2. El corte nuevo 9 queda después de todas ellas. Un recuadro separado da el argumento general por finitud, el caso vacío y la dirección inversa. Las flechas relacionan índices, no valores de la sucesión.](../../assets/books/anm/C06/C06-F11.svg){#fig-anm-c06-f11 fig-alt="En un ejemplo de biyección, el prefijo original 0,1,2 tiene preimágenes 8,5,2. El corte nuevo 9 queda después de todas ellas. Un recuadro separado da el argumento general por finitud, el caso vacío y la dirección inversa. Las flechas relacionan índices, no valores de la sucesión."}

**Figura [C06-F11](#fig-anm-c06-f11).** Las posiciones nuevas que envían al prefijo original forman un conjunto finito. Si no es vacío, un corte posterior a su máximo evita todas esas posiciones; si es vacío, basta el corte cero. La biyección no necesita conservar el orden.

Para K=3, el prefijo original es {0,1,2} y sus preimágenes en la biyección dibujada son {2,5,8}; N=9 evita todas esas posiciones. Si K=0, se elige N=0 sin tomar un máximo del conjunto vacío. En la dirección inversa se aplica la misma construcción a π⁻¹. Las flechas relacionan índices naturales; los términos reales aparecen al evaluar las funciones a y b.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-6)

[← Capítulo 5](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.html) · [Capítulo 7 →](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html)
