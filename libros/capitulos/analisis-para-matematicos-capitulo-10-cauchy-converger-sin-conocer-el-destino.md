---
content-id: MA-BCH-0242
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-010
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
title: 'Capítulo 10 — Cauchy: converger sin conocer el destino'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C10.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-10)

Una lista de aproximaciones puede estabilizarse aunque aún no sepamos nombrar su destino. Queremos reconocer esa estabilización desde las relaciones entre los términos de una cola. La pregunta será cómo detectar convergencia sin conocer de antemano el límite: pasaremos de una referencia externa a un control interno de distancias.

Primero definiremos Cauchy con dos índices universales y probaremos qué conserva de la convergencia. Después recuperaremos acotación y construiremos un destino real usando completitud. Esa prueba principal sólo necesita las interfaces de C03 y C06, además de las bases de orden, valor absoluto y colas. Distinguiremos control de vecinos y control de todos los pares, y veremos por qué la misma distancia puede estabilizar una sucesión racional sin darle un destino racional. El capítulo termina con estimaciones de error e iteraciones reales construidas desde sumas finitas.

## 10.1. Comparar términos sin nombrar un límite

[]{#MA-SEC-ANM-01-010-001}

Para demostrar $a_n\to L$ en C06 había que proponer un real $L$ y controlar $|a_n-L|$. Si sólo conocemos aproximaciones sucesivas, ese candidato puede estar oculto. ¿Cómo detectar convergencia sin conocer de antemano el destino? Podemos empezar preguntando si dos términos suficientemente tardíos se acercan entre sí, sea cual sea la distancia temporal entre sus índices.

Una sucesión real $a:\mathbb N\to\mathbb R$ es **de Cauchy** si

$$
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall p,q\in\mathbb N:
\quad p,q\ge N\ \Longrightarrow\ |a_p-a_q|<\varepsilon.
$$

Usaremos siempre $\mathbb N=\{0,1,2,\ldots\}$. El corte $N$ se escoge después de recibir $\varepsilon$, pero antes de los dos índices universales. No puede depender de $p,q$. Se permite $p=q$, caso en que la distancia es cero. Por simetría basta comprobar $p>q\ge N$ y agregar el caso de igualdad; no basta comprobar $p=q+1$.

El objeto controlado es toda la cola. Dos índices muy separados deben dar valores próximos tanto como dos vecinos. La definición no nombra un límite, no exige monotonía ni valores distintos y no afirma todavía que exista un real al que converger. Esa existencia será una obligación nueva.

**Primer control explícito.** En $a_n=1/(n+1)$, si $p,q\ge N$, ambos valores están en $(0,1/(N+1)]$, luego $|a_p-a_q|\le1/(N+1)$. Para $\varepsilon>0$, definamos $N(\varepsilon)$ como el mínimo natural $N$ con $N+1>1/\varepsilon$. El conjunto es no vacío por arquimedianidad. Entonces $1/(N+1)<\varepsilon$ y el mismo corte sirve para cualquier par posterior. No hemos usado cero como candidato para verificar Cauchy.

Las constantes también son de Cauchy con $N=0$ para cualquier tolerancia. La alternancia $(-1)^n$ falla: después de cualquier corte, los índices $N,N+1$ tienen distancia dos. Esto ya sugiere una negación de la definición, que escribiremos con cuidado en §10.5.

La definición garantiza un corte para cada precisión, pero no entrega por sí sola un algoritmo para encontrarlo. Una regla explícita como $N(\varepsilon)$ en el ejemplo contiene información adicional útil para calcular. Conviene distinguir existencia lógica de un umbral, una fórmula que lo describe y un procedimiento efectivo que puede evaluarlo con los datos disponibles.

![En los recíprocos, desde el corte cuatro toda la cola cabe en una banda de anchura un quinto, menor que un cuarto. El par de índices seis y diez muestra una distancia cuatro setenta y sieteavos dentro del mismo control.](../../assets/books/anm/C10/C10-F01.svg){#fig-anm-c10-f01 fig-alt="En los recíprocos, desde el corte cuatro toda la cola cabe en una banda de anchura un quinto, menor que un cuarto. El par de índices seis y diez muestra una distancia cuatro setenta y sieteavos dentro del mismo control."}

### Antes de seguir

#### Microcontrol 1

[]{#MA-MIC-ANM-01-010-001}

¿Qué objetos compara la condición de Cauchy?

[]{#MA-MSOL-ANM-01-010-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Compara dos términos $a_p,a_q$ de una misma cola mediante $|a_p-a_q|$, sin nombrar un candidato a límite.

Los índices $p$ y $q$ pueden elegirse independientemente: ambos deben estar después del mismo corte $N$. Así se comprueba que la cola entera se concentra, aunque todavía no sepamos alrededor de qué número. La diferencia entre los términos mide una separación en la recta de valores; la diferencia entre sus índices sólo mide separación temporal. La definición controla la primera y permite que la segunda sea arbitrariamente grande.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-010-002}

¿Puede el corte $N$ depender de los índices $p,q$?

[]{#MA-MSOL-ANM-01-010-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

No. Para cada tolerancia se escoge $N$ antes de los dos índices universales y debe servir para todos los pares posteriores.

Leamos la definición en su orden: se recibe $\varepsilon>0$, se encuentra un $N$, y después se consideran cualesquiera $p,q\ge N$. Por eso el corte puede adaptarse a la precisión, pero debe funcionar simultáneamente para todos esos pares. Elegir un corte después de conocer cada par permitiría excluir precisamente los términos difíciles; no demostraría que existe una cola con el control requerido.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-010-003}

¿Se permite $p=q$ en la definición?

[]{#MA-MSOL-ANM-01-010-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

Sí. La distancia es entonces cero y cumple toda tolerancia positiva.

Los cuantificadores no exigen que los índices sean distintos. Si elegimos el mismo índice dos veces, obtenemos $|a_p-a_p|=0<\varepsilon$, pues la tolerancia es positiva. Ese caso siempre cumple la estimación. Sin embargo, comprobar únicamente los pares iguales no sirve: quedan pendientes todos los pares de índices diferentes. Ésta es la diferencia entre verificar un caso permitido y verificar la condición universal.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-010-004}

¿Basta controlar pares de vecinos?

[]{#MA-MSOL-ANM-01-010-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

No. La definición exige todos los pares de una cola, incluso con separación temporal arbitrariamente grande.

Una sucesión puede avanzar mediante saltos pequeños y acumular una separación grande tras muchos pasos. Las sumas parciales armónicas de §10.5 lo muestran: sus saltos vecinos tienden a cero, pero hay pares arbitrariamente tardíos separados al menos por $1/2$. La condición de Cauchy obliga a controlar también esos pares. Por eso un gráfico que muestre sólo diferencias entre vecinos puede sugerir estabilización sin demostrarla.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-010-005}

Da un corte suficiente de Cauchy para $a_n=1/(n+1)$.

[]{#MA-MSOL-ANM-01-010-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Para $\varepsilon>0$ sirve cualquier natural $N$ con $N+1>1/\varepsilon$, pues las distancias posteriores son a lo sumo $1/(N+1)<\varepsilon$.

Si $p,q\ge N$, ambos términos son positivos y no superan $1/(N+1)$. La distancia entre dos números de ese intervalo no supera su longitud, de modo que $|a_p-a_q|\le1/(N+1)$. Buscamos entonces que esta cota sea estrictamente menor que $\varepsilon$, lo que equivale a $N+1>1/\varepsilon$. La propiedad arquimediana garantiza un natural con esa propiedad. Una vez escogido, sirve para cualquier par posterior.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-010-006}

¿Qué corte sirve para una sucesión constante?

[]{#MA-MSOL-ANM-01-010-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

$N=0$ para toda tolerancia, porque todas sus distancias son cero.

Si $a_n=c$ para todo $n$, entonces, cualesquiera que sean $p$ y $q$, tenemos $|a_p-a_q|=|c-c|=0$. Esta cantidad es menor que toda tolerancia positiva. Como no hay términos excepcionales al comienzo, no necesitamos descartar un prefijo: el corte inicial $N=0$ basta. El ejemplo también muestra que Cauchy no exige valores distintos ni un desplazamiento continuo de los términos.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-010-007}

¿La condición de Cauchy exige monotonía?

[]{#MA-MSOL-ANM-01-010-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

No. Por ejemplo, $(-1)^n/(n+1)$ es de Cauchy y alterna de signo.

Para comprobar el ejemplo sin depender de un dibujo, dados $p,q\ge N$ usamos
$$
\left|\frac{(-1)^p}{p+1}-\frac{(-1)^q}{q+1}\right|
\le\frac1{p+1}+\frac1{q+1}\le\frac2{N+1}.
$$
Escogemos $N+1>2/\varepsilon$. El error entre cualquier par queda por debajo de $\varepsilon$, aunque los términos cambien de signo. La concentración de una cola depende del tamaño de las separaciones, no de que todos los términos avancen en una misma dirección.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-010-008}

¿La definición por sí sola proporciona un algoritmo para calcular los cortes?

[]{#MA-MSOL-ANM-01-010-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No. Afirma existencia para cada tolerancia. Una regla efectiva de cortes requiere información adicional sobre la sucesión.

El enunciado tiene la forma «para cada precisión existe un corte». Eso no describe cómo obtenerlo a partir de datos finitos, ni establece cuánto tiempo llevaría encontrarlo. En ejemplos con una fórmula explícita de error, podemos construir cortes mediante desigualdades. Para una sucesión dada abstractamente, esa información puede faltar. Conviene distinguir la existencia matemática del testigo de un procedimiento efectivo que lo calcule.

</details>

### Ejercicios de la sección 10.1

[]{#ejercicios-10}

#### Ejercicio 1. Dos índices universales

[]{#MA-EX-ANM-01-010-001}

Compara la definición de Cauchy con la condición: para todo $\varepsilon>0$ y todo $p$, existe $q\ge p$ con $|a_p-a_q|<\varepsilon$. ¿La segunda impone control?

[]{#MA-SOL-ANM-01-010-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La definición de Cauchy exige un corte antes de todos los pares posteriores. La segunda condición es verdadera para cualquier sucesión tomando $q=p$, con distancia cero. No impone Cauchy: $(-1)^n$ la satisface y no es de Cauchy.

</details>

#### Ejercicio 2. Un corte recíproco

[]{#MA-EX-ANM-01-010-002}

Prueba directamente que $a_n=1/(n+1)$ es de Cauchy, dando un corte que incluya el índice cero cuando sirva.

[]{#MA-SOL-ANM-01-010-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Los términos posteriores a $N$ están en $(0,1/(N+1)]$, luego cualquier distancia es a lo sumo $1/(N+1)$. Para $\varepsilon>0$ tomar el mínimo natural con $N+1>1/\varepsilon$; existe por arquimedianidad y garantiza distancia menor que $\varepsilon$. Si $\varepsilon\ge1$, podemos tomar directamente $N=0$, porque todas las distancias son estrictamente menores que uno. Si $\varepsilon<1$, cero no sirve: una distancia $1-1/(n+1)$ lo bastante tardía alcanza esa tolerancia. No es necesario proponer un destino.

Después de la prueba, puede retomarse la [figura 10.1](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f01) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 3. Constantes y repetición

[]{#MA-EX-ANM-01-010-003}

Prueba que toda sucesión constante es de Cauchy y explica por qué no se exigen valores distintos.

[]{#MA-SOL-ANM-01-010-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Si $a_n=c$ para todos los índices, $|a_p-a_q|=0$ para todo par. El corte cero sirve para toda tolerancia positiva. La sucesión sigue siendo una función aunque repita un valor; Cauchy controla distancias, no inyectividad.

</details>

#### Ejercicio 4. Simetría de los pares

[]{#MA-EX-ANM-01-010-004}

Prueba que en la definición basta exigir el control para $p>q\ge N$, además de recordar el caso de igualdad.

[]{#MA-SOL-ANM-01-010-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Para pares iguales la distancia es cero. Para $p<q$, intercambiar los índices usa $|a_p-a_q|=|a_q-a_p|$ y reduce al caso comprobado. El corte es el mismo y no se altera el orden de cuantificadores. Esta reducción no permite limitar la separación a un desplazamiento fijo.

Después de la prueba, puede retomarse la [figura 10.1](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f01) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 5. Una escala discreta de tolerancias

[]{#MA-EX-ANM-01-010-005}

Demuestra que basta probar: para todo entero $k\ge1$ existe $N_k$ que controla todos los pares posteriores con distancia menor que $1/k$.

[]{#MA-SOL-ANM-01-010-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

La condición de Cauchy implica cada una de esas condiciones al usar $\varepsilon=1/k$. Recíprocamente, dada $\varepsilon>0$, arquimedianidad da $k\ge1$ con $1/k<\varepsilon$; el corte de esa condición controla cualquier par posterior con distancia menor que $\varepsilon$. No se intercambia el índice universal de par con el corte.

</details>
## 10.2. Del destino común al control interno

[]{#MA-SEC-ANM-01-010-002}

Si todos los términos tardíos están cerca de un mismo destino, deberían estar cerca unos de otros. La desigualdad triangular convierte esa imagen en una prueba. Debemos repartir la tolerancia porque la distancia entre dos términos puede contener dos errores.

**Toda sucesión real convergente es de Cauchy.** Supongamos $a_n\to L$. Fijemos $\varepsilon>0$. Por convergencia existe $N$ tal que $|a_n-L|<\varepsilon/2$ para todo $n\ge N$. Sean ahora $p,q\ge N$. Entonces

$$
|a_p-a_q|\le |a_p-L|+|a_q-L|
<\varepsilon/2+\varepsilon/2=\varepsilon.
$$

El mismo corte de convergencia controla ambos errores. La prueba usa sólo la noción de límite y la desigualdad triangular; no gasta completitud. Tampoco necesita una fórmula del término general. Si contamos con un corte que garantiza radio $\varepsilon/2$ alrededor de $L$, ese corte es suficiente para Cauchy con tolerancia $\varepsilon$.

El radio y el diámetro deben distinguirse. Una ventana de radio $\varepsilon$ alrededor de $L$ sólo da, por este argumento, distancia menor que $2\varepsilon$ entre términos. Para obtener distancia menor que $\varepsilon$ conviene usar una ventana de radio $\varepsilon/2$. En sentido inverso, una cola con distancias menores que $\varepsilon$ cabe en la ventana de radio $\varepsilon$ alrededor de cualquier término de esa cola, pero eso no identifica todavía un centro común para todas las precisiones.

Como primer uso, $a_n=(-1)^n/(n+1)$ converge a cero por la estimación $|a_n|=1/(n+1)$ de C06, luego es de Cauchy aunque alterne de signo. También podemos verificarlo sin nombrar el destino: si $p,q\ge N$, entonces $|a_p-a_q|\le1/(p+1)+1/(q+1)\le2/(N+1)$. El mínimo natural con $N+1>2/\varepsilon$ proporciona un corte suficiente. Aquí el control por un intervalo de valores cuesta dos recíprocos, mientras que en la sucesión positiva de §10.1 bastaba uno.

Hemos probado una implicación. Su recíproca no debe esconderse en la intuición de que los términos «se juntan»: todavía hay que construir un real que los reciba. Primero recuperaremos acotación y después veremos cómo interviene completitud.

![La ventana de radio medio controla dos errores, un tercio y un cuarto. Su suma siete doceavos acota la distancia entre los términos y es menor que la tolerancia uno.](../../assets/books/anm/C10/C10-F02.svg){#fig-anm-c10-f02 fig-alt="La ventana de radio medio controla dos errores, un tercio y un cuarto. Su suma siete doceavos acota la distancia entre los términos y es menor que la tolerancia uno."}

### Antes de seguir

#### Microcontrol 9

[]{#MA-MIC-ANM-01-010-009}

¿Qué tolerancia de convergencia se usa para probar Cauchy con tolerancia $\varepsilon$?

[]{#MA-MSOL-ANM-01-010-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

$\varepsilon/2$; así los dos errores respecto del límite suman menos que $\varepsilon$.

Queremos controlar una distancia entre dos términos, pero la convergencia controla cada término respecto de $L$. Introducimos ese centro como punto intermedio y repartimos el presupuesto de error en dos partes. Si ambas distancias a $L$ son menores que $\varepsilon/2$, su suma es menor que $\varepsilon$. Usar directamente $\varepsilon$ en cada una sólo garantizaría una suma menor que $2\varepsilon$, insuficiente para el objetivo fijado.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-010-010}

Escribe la desigualdad triangular que une $a_p,a_q$ con el límite $L$.

[]{#MA-MSOL-ANM-01-010-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

$|a_p-a_q|\le|a_p-L|+|a_q-L|$.

Escribimos $a_p-a_q=(a_p-L)+(L-a_q)$ y aplicamos $|u+v|\le|u|+|v|$. Como $|L-a_q|=|a_q-L|$, aparece exactamente la desigualdad indicada. Geométricamente, el recorrido de $a_p$ a $a_q$ pasando por $L$ no puede ser más corto que la separación directa. La utilidad del paso es que transforma una distancia desconocida entre términos en dos errores que la convergencia ya permite controlar.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-010-011}

¿Por qué el mismo corte controla ambos errores?

[]{#MA-MSOL-ANM-01-010-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Porque la convergencia con tolerancia $\varepsilon/2$ vale para todo índice posterior, incluidos $p$ y $q$.

La definición de convergencia entrega un único corte $N$ tal que $|a_n-L|<\varepsilon/2$ para todo $n\ge N$. Al tomar $p,q\ge N$, aplicamos esa misma afirmación primero con $n=p$ y después con $n=q$. No estamos escogiendo cortes nuevos para esos índices. La universalidad sobre toda la cola permite sumar los dos controles y obtener $|a_p-a_q|<\varepsilon$.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-010-012}

¿Interviene completitud en convergente implica Cauchy?

[]{#MA-MSOL-ANM-01-010-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

No. El límite ya existe por hipótesis; se usa su definición y la desigualdad triangular.

Completitud serviría para garantizar la existencia de un límite cuando aún no lo tenemos. En esta dirección, la hipótesis ya afirma que existe $L$ y que la sucesión converge a él. Basta elegir el corte para $\varepsilon/2$ y aplicar la desigualdad triangular. El argumento funciona también en cualquier espacio métrico, completo o incompleto, siempre que la sucesión considerada tenga un límite dentro de ese espacio.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-010-013}

¿Qué distancia máxima garantiza por estimación una ventana abierta de radio $r$?

[]{#MA-MSOL-ANM-01-010-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Distancia menor que $2r$ entre cualesquiera dos términos en esa ventana; el diámetro se distingue del radio.

Si $x$ e $y$ pertenecen a $(L-r,L+r)$, entonces $|x-L|<r$ y $|y-L|<r$. La desigualdad triangular da $|x-y|\le|x-L|+|y-L|<2r$. No se obtiene en general una cota $r$: los puntos $L-3r/4$ y $L+3r/4$ están dentro de la ventana y distan $3r/2$. El radio mide distancia al centro; entre dos puntos puede intervenir casi todo el ancho.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-010-014}

Da un corte directo para $a_n=(-1)^n/(n+1)$ con tolerancia $\varepsilon$.

[]{#MA-MSOL-ANM-01-010-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Sirve cualquier $N$ con $N+1>2/\varepsilon$, pues $|a_p-a_q|\le2/(N+1)<\varepsilon$ para $p,q\ge N$.

Aplicamos la desigualdad triangular a la diferencia de los dos términos. Los signos desaparecen al tomar valores absolutos y obtenemos $|a_p-a_q|\le1/(p+1)+1/(q+1)$. Como ambos índices superan el mismo corte, cada sumando es a lo sumo $1/(N+1)$. La condición $N+1>2/\varepsilon$ hace que la suma sea menor que la tolerancia solicitada. No hace falta separar los casos de paridad.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-010-015}

¿Tener signos alternantes contradice convergencia?

[]{#MA-MSOL-ANM-01-010-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

No. La magnitud $1/(n+1)$ puede tender a cero; entonces la alternancia amortiguada converge y es de Cauchy.

Para el ejemplo $a_n=(-1)^n/(n+1)$, la distancia al candidato cero es $|a_n|=1/(n+1)$. Recibida $\varepsilon>0$, escogemos $N+1>1/\varepsilon$; entonces todos los índices $n\ge N$ cumplen $|a_n|<\varepsilon$. El signo indica de qué lado se aproxima un término, pero la definición exige cercanía en ambos lados. Alternar no impide converger cuando la magnitud de la oscilación se reduce.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-010-016}

¿La implicación ya demostrada permite concluir Cauchy implica convergente?

[]{#MA-MSOL-ANM-01-010-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

Todavía no en esta fase lógica: la recíproca exige construir un destino usando completitud, como se hará en §10.4.

Una implicación no autoriza su recíproca. Haber probado que todo límite produce control de Cauchy no construye un límite para cualquier sucesión que tenga ese control. Precisamente ése será el trabajo posterior: encerrar las colas y usar la propiedad del supremo para obtener un candidato real. El codominio importa; en $\mathbb Q$ hay sucesiones de Cauchy cuyo destino sólo existe al pasar a $\mathbb R$.

</details>

### Ejercicios de la sección 10.2

#### Ejercicio 6. Dos errores

[]{#MA-EX-ANM-01-010-006}

Demuestra convergente implica Cauchy e identifica dónde se reparte la tolerancia.

[]{#MA-SOL-ANM-01-010-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Si $a_n\to L$, para $\varepsilon>0$ escoger un corte que haga $|a_n-L|<\varepsilon/2$ en toda la cola. Para $p,q$ posteriores, la desigualdad triangular da $|a_p-a_q|\le|a_p-L|+|a_q-L|<\varepsilon$. La división en dos errores se hace antes de fijar $p,q$. El límite viene dado por hipótesis; no se utiliza completitud.

Después de la prueba, puede retomarse la [figura 10.2](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f02) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 7. Alternancia amortiguada

[]{#MA-EX-ANM-01-010-007}

Prueba Cauchy directamente para $a_n=(-1)^n/(n+1)$ y compara el corte con el de la sucesión positiva.

[]{#MA-SOL-ANM-01-010-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

$|a_p-a_q|\le1/(p+1)+1/(q+1)\le2/(N+1)$ para pares posteriores a $N$. Tomar cualquier natural con $N+1>2/\varepsilon$ garantiza control. Para términos positivos bastaba $N+1>1/\varepsilon$; aquí pueden sumarse las magnitudes de signos opuestos. Ambos son cortes suficientes, sin afirmar optimalidad.

Después de la prueba, puede retomarse la [figura 10.2](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f02) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 8. Radio no es diámetro

[]{#MA-EX-ANM-01-010-008}

Si todos los términos de una cola están en $(L-r,L+r)$, prueba que sus distancias son menores que $2r$. Da dos puntos de esa ventana separados por más de $r$.

[]{#MA-SOL-ANM-01-010-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Por triangular, dos errores menores que $r$ suman menos que $2r$. Los puntos $L-3r/4$ y $L+3r/4$ pertenecen a la ventana y están separados por $3r/2>r$. Una ventana de radio $r$ no proporciona automáticamente tolerancia de Cauchy $r$.

Después de la prueba, puede retomarse la [figura 10.2](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f02) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 9. Transportar un corte conocido

[]{#MA-EX-ANM-01-010-009}

Supón que $|a_n-L|\le C/(n+1)$ para todos los índices y $C\ge0$. Da un corte de Cauchy para cada tolerancia.

[]{#MA-SOL-ANM-01-010-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Si $C=0$, la sucesión es constante $L$ y sirve cero. Si $C>0$, para $p,q\ge N$ la distancia es a lo sumo $2C/(N+1)$. Cualquier $N$ con $N+1>2C/\varepsilon$ garantiza la condición. La cota no estricta inicial se convierte en estricta al escoger el corte.

</details>

#### Ejercicio 10. Una recíproca pendiente

[]{#MA-EX-ANM-01-010-010}

Explica qué obligación falta después de demostrar que una convergente es de Cauchy. ¿La desigualdad triangular por sí sola la resuelve?

[]{#MA-SOL-ANM-01-010-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Falta demostrar que cada sucesión con control interno tiene un destino dentro del codominio. La desigualdad triangular relaciona distancias con un centro ya dado; no crea ese centro. La prueba de §10.4 lo construirá por completitud. El contraste racional de §10.7 mostrará por qué esa obligación no es meramente formal.

</details>
## 10.3. Encerrar una cola y recuperar la acotación

[]{#MA-SEC-ANM-01-010-003}

El control de Cauchy no acota explícitamente cada término respecto de cero. Podemos convertirlo en una cota usando un término de referencia que la propia cola determina.

**Toda sucesión de Cauchy es acotada.** Aplicamos la definición con tolerancia uno y obtenemos un corte $N_0$. Al fijar uno de los dos índices en $N_0$, para todo $n\ge N_0$ tenemos $|a_n-a_{N_0}|<1$. Por desigualdad triangular, $|a_n|<|a_{N_0}|+1$. Si $N_0=0$, esta cota controla todos los términos. Si $N_0>0$, tomamos

$$
B=\max\{|a_{N_0}|+1,|a_0|,\ldots,|a_{N_0-1}|\}.
$$

El conjunto del máximo es finito y no vacío; $B$ controla también el prefijo. Así $|a_n|\le B$ para todo índice. La acotación necesita una sola tolerancia de Cauchy y no usa completitud. La recíproca es falsa: $(-1)^n$ permanece entre menos uno y uno y sigue teniendo pares separados por dos.

La acotación permite ahora representar toda cola por un intervalo real. Definamos $T_N=\{a_n:n\ge N\}$, $\ell_N=\inf T_N$, $u_N=\sup T_N$ e $I_N=[\ell_N,u_N]$. Las colas son no vacías porque contienen $a_N$, y son acotadas por lo recién probado. Aquí sí interviene completitud, al asegurar sus extremos reales. Esta construcción coincide con la vista en C09, pero su existencia y las propiedades necesarias se justifican aquí para conservar los prerrequisitos C03/C06.

Como $T_{N+1}\subseteq T_N$, $\ell_N\le\ell_{N+1}$ y $u_{N+1}\le u_N$. Los intervalos están encajados. Puede haber extremos no alcanzados por los términos: para $1/(n+1)$, el extremo inferior de cada intervalo es cero, aunque ningún término valga cero.

La condición de Cauchy fuerza anchura pequeña. Fijemos $\eta>0$ y un corte $N_0$ desde el cual todas las distancias sean menores que $\eta$. Para $N\ge N_0$ y cualquier $y\in T_N$, cada $x\in T_N$ cumple $x-y\le|x-y|<\eta$. Por tanto $y+\eta$ es cota superior de $T_N$, y $u_N\le y+\eta$. Esta desigualdad vale para todos los $y$, luego $u_N-\eta$ es cota inferior de $T_N$ y $u_N-\eta\le\ell_N$. En consecuencia,

$$
0\le u_N-\ell_N\le\eta\qquad(N\ge N_0).
$$

La desigualdad final puede ser no estricta, porque supremos e ínfimos pueden no alcanzarse. Para hacer la anchura menor que una precisión $\varepsilon$, aplicaremos este argumento con $\eta=\varepsilon/2$. La estimación no selecciona un máximo y un mínimo de cola inexistentes; compara cotas para todos los valores.

![Para el ejemplo con términos iniciales nueve y menos seis y a_n=1/(n−1) desde n=2, el corte cuatro permite anclar la cola en un tercio. La cota de esa cola no controla el prefijo; la cota global nueve sí lo incorpora.](../../assets/books/anm/C10/C10-F03.svg){#fig-anm-c10-f03 fig-alt="Para el ejemplo con términos iniciales nueve y menos seis y a_n=1/(n−1) desde n=2, el corte cuatro permite anclar la cola en un tercio. La cota de esa cola no controla el prefijo; la cota global nueve sí lo incorpora."}

### Antes de seguir

#### Microcontrol 17

[]{#MA-MIC-ANM-01-010-017}

¿Qué tolerancia fija basta para recuperar acotación de una sucesión de Cauchy?

[]{#MA-MSOL-ANM-01-010-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

La tolerancia uno proporciona una cola próxima al término de su corte.

La condición de Cauchy responde a cualquier tolerancia, así que podemos usar la precisión particular $1$. Obtenemos $N_0$ con $|a_p-a_q|<1$ para todos $p,q\ge N_0$. Al fijar $q=N_0$, todos los términos de esa cola quedan en la ventana $(a_{N_0}-1,a_{N_0}+1)$. Eso ya proporciona una cota para la cola; después sólo habrá que incorporar los finitos términos anteriores.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-010-018}

¿Qué término se toma como ancla de la cola?

[]{#MA-MSOL-ANM-01-010-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

$a_{N_0}$, donde $N_0$ es el corte de Cauchy para tolerancia uno.

El término $a_{N_0}$ pertenece a la cola que controla el corte $N_0$. Por ello es lícito sustituir uno de los dos índices universales por $N_0$. Para cualquier $n\ge N_0$ resulta $|a_n-a_{N_0}|<1$. No podríamos utilizar de la misma manera un término situado antes del corte: la definición no garantiza distancias entre esa entrada temprana y las entradas de la cola.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-010-019}

¿Qué cota de $|a_n|$ se obtiene para $n\ge N_0$?

[]{#MA-MSOL-ANM-01-010-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

$|a_n|<|a_{N_0}|+1$, por $|a_n-a_{N_0}|<1$ y desigualdad triangular.

Separamos el término como $a_n=(a_n-a_{N_0})+a_{N_0}$. Por la desigualdad triangular,
$$|a_n|\le|a_n-a_{N_0}|+|a_{N_0}|<1+|a_{N_0}|.$$
La cantidad de la derecha es fija: depende del ancla elegida, pero ya no del índice $n$. Esa independencia es lo que permite usarla como cota de toda la cola. La misma estimación no se ha probado todavía para el prefijo anterior.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-010-020}

¿Cómo se trata el prefijo si $N_0=0$?

[]{#MA-MSOL-ANM-01-010-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

No hay prefijo anterior que controlar; $|a_0|+1$ acota ya todos los términos y no se toma un máximo vacío.

Con nuestra convención, los índices naturales comienzan en cero. Si $N_0=0$, no existe ningún índice natural $n<N_0$, así que el prefijo que normalmente se controla por finitud está vacío. La cota de cola ya vale para toda la sucesión. Escribir un máximo de los términos del prefijo vacío introduciría una expresión sin definir; en este caso se omite ese paso y se conserva la cota $|a_0|+1$.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-010-021}

¿Acotada implica Cauchy?

[]{#MA-MSOL-ANM-01-010-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

No. $(-1)^n$ es acotada y tiene pares posteriores separados por dos después de cualquier corte.

Tomemos $a_n=(-1)^n$. Todos sus términos tienen valor absoluto uno, por lo que es acotada. Sin embargo, para cualquier corte $N$, elegimos $p=2N$ y $q=2N+1$: ambos son posteriores al corte y $|a_p-a_q|=|1-(-1)|=2$. Con la tolerancia fija $\varepsilon_0=1$, ningún corte controla todos los pares. Acotación encierra la sucesión en una región fija; Cauchy exige regiones cada vez más estrechas.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-010-022}

¿Por qué existen los extremos reales de $T_N$?

[]{#MA-MSOL-ANM-01-010-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

$T_N$ contiene $a_N$ y es acotado; completitud garantiza su supremo e ínfimo reales.

El conjunto $T_N=\{a_n:n\ge N\}$ no es vacío, pues contiene el término de índice $N$. La acotación de la sucesión proporciona cotas superiores e inferiores de ese conjunto. La completitud de $\mathbb R$ permite definir $u_N=\sup T_N$ y $\ell_N=\inf T_N$. No se afirma que esos extremos sean términos de la sucesión: supremo e ínfimo pueden existir sin alcanzarse.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-010-023}

Si todas las distancias de una cola son menores que $\eta$, ¿qué cota se obtiene para su anchura?

[]{#MA-MSOL-ANM-01-010-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

$0\le u_N-\ell_N\le\eta$. Al tomar extremos puede perderse la desigualdad estricta.

Fijemos $b\in T_N$. Para cada $a\in T_N$, $|a-b|<\eta$ implica $a<b+\eta$, así que $b+\eta$ es una cota superior y $u_N\le b+\eta$. Esto vale para todos los $b$, luego $u_N-\eta$ es cota inferior de $T_N$ y $u_N-\eta\le\ell_N$. Obtenemos $u_N-\ell_N\le\eta$. La no negatividad sigue de $\ell_N\le u_N$. Al tomar extremos, las cotas pueden quedar en la frontera aunque cada par efectivo tenga distancia estrictamente menor.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-010-024}

¿Qué tolerancia de Cauchy garantiza anchura estrictamente menor que $\varepsilon$ por esa cota?

[]{#MA-MSOL-ANM-01-010-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

Usar $\eta=\varepsilon/2$ da anchura a lo sumo $\varepsilon/2$, y por tanto menor que $\varepsilon$.

La estimación de anchura entrega una desigualdad no estricta. Si pidiéramos Cauchy sólo con $\eta=\varepsilon$, podríamos concluir $u_N-\ell_N\le\varepsilon$, pero no necesariamente una anchura menor que $\varepsilon$. Reservamos un margen: con $\eta=\varepsilon/2$ obtenemos $u_N-\ell_N\le\varepsilon/2<\varepsilon$. La última desigualdad es estricta porque la tolerancia original es positiva. Esta reserva evita perder precisión al pasar de términos a extremos.

</details>

### Ejercicios de la sección 10.3

#### Ejercicio 11. Ancla y prefijo

[]{#MA-EX-ANM-01-010-011}

Reconstruye la prueba de acotación de una sucesión de Cauchy y trata por separado el corte cero.

[]{#MA-SOL-ANM-01-010-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Con tolerancia uno obtener $N_0$, fijar el índice ancla en $N_0$ y deducir $|a_n|<|a_{N_0}|+1$ para $n\ge N_0$. Si $N_0=0$, esa cota es global. Si $N_0>0$, el máximo de ella y las finitas magnitudes anteriores acota toda la sucesión. El conjunto del máximo es no vacío y no se usa completitud.

Después de la prueba, puede retomarse la [figura 10.3](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f03) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 12. La cota no basta

[]{#MA-EX-ANM-01-010-012}

Da una sucesión real acotada que no sea de Cauchy y prueba ambas afirmaciones.

[]{#MA-SOL-ANM-01-010-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

$a_n=(-1)^n$ tiene magnitud uno. Para cualquier corte, $p=N,q=N+1$ dan distancia dos. La tolerancia fija uno impide la condición de Cauchy en cualquier cola. La acotación sólo evita escape; no obliga a proximidad mutua.

</details>

#### Ejercicio 13. Intervalos de cola

[]{#MA-EX-ANM-01-010-013}

Para $a_n=1/(n+1)$, calcula $I_N$ y sus anchuras. ¿Son intervalos de valores alcanzados?

[]{#MA-SOL-ANM-01-010-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

$I_N=[0,1/(N+1)]$ y su anchura es $1/(N+1)$. El extremo superior se alcanza en $N$; el inferior cero no es término. El intervalo encierra toda la cola y también valores que ésta nunca toma. Los extremos se calculan por optimalidad y arquimedianidad.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 14. Ancho no estricto

[]{#MA-EX-ANM-01-010-014}

Prueba que si todos los pares de una cola tienen distancia menor que $\eta$, entonces su intervalo de extremos tiene anchura a lo sumo $\eta$.

[]{#MA-SOL-ANM-01-010-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Para cada valor fijo $y$ de la cola, todos sus valores $x$ cumplen $x<y+\eta$. Tomando supremo, $u_N\le y+\eta$. Así $u_N-\eta$ acota inferiormente todos los $y$, y $u_N-\eta\le\ell_N$. Restar da anchura a lo sumo $\eta$. No se supone que existan valores extremos alcanzados.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 15. La igualdad puede sobrevivir

[]{#MA-EX-ANM-01-010-015}

Construye una sucesión de Cauchy cuya cola de corte cero tenga todas sus distancias menores que uno y anchura exactamente uno.

[]{#MA-SOL-ANM-01-010-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Tomar $a_n=1/(n+1)$. Todos sus valores son positivos y a lo sumo uno, de modo que cada distancia es menor que uno. El supremo es uno y el ínfimo cero, luego anchura uno. La sucesión es de Cauchy por el control recíproco. Se verifica que pasar a extremos puede perder la desigualdad estricta.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

</details>
## 10.4. La completitud construye el destino

[]{#MA-SEC-ANM-01-010-004}

Tenemos intervalos de cola encajados con anchuras arbitrariamente pequeñas. Falta un real común a todos ellos. La completitud convierte este control interno en existencia de un destino.

**Mapa de la prueba.** Formaremos el conjunto de los extremos inferiores; construiremos su supremo $L$; probaremos que cada extremo superior lo acota; finalmente usaremos el ancho de una cola para controlar todos sus términos. El punto delicado es comparar extremos de cortes diferentes: no basta conocer $\ell_N\le u_N$ para el mismo $N$.

Sea $a$ de Cauchy y usemos los intervalos de §10.3. El conjunto $E=\{\ell_N:N\in\mathbb N\}$ contiene $\ell_0$ y está acotado superiormente por la cota global $B$. Por completitud existe el real $L=\sup E$. Cada $\ell_N\le L$.

Para cualquier par de cortes $M,N$, tomemos $r=\max\{M,N\}$. El término $a_r$ pertenece a ambas colas, de modo que $\ell_M\le a_r\le u_N$. Por tanto $u_N$ acota superiormente todos los elementos de $E$, y la minimalidad del supremo da $L\le u_N$. Como $N$ era arbitrario,

$$
\ell_N\le L\le u_N\qquad\text{para todo }N.
$$

Éste es el paso de existencia que el control de distancias no proporcionaba: el centro común es un real gracias a la propiedad del supremo. Ninguna sucesión de candidatos a límite fue escogida, ni usamos convergencia monótona o Bolzano–Weierstrass.

Ahora fijemos $\varepsilon>0$. Cauchy con tolerancia $\varepsilon/2$ produce un corte $N$ cuyo intervalo tiene anchura $u_N-\ell_N\le\varepsilon/2$. Para cualquier $n\ge N$, tanto $a_n$ como $L$ pertenecen a $I_N$, luego

$$
|a_n-L|\le u_N-\ell_N\le\varepsilon/2<\varepsilon.
$$

Hemos probado $a_n\to L$ desde la definición. Si hubiera otro real $L'$ en todos los intervalos, para cualquier $\varepsilon>0$ su distancia a $L$ sería a lo sumo la anchura de una cola adecuada y, por tanto, menor que $\varepsilon$. La mitad de una supuesta distancia positiva daría contradicción. Así el punto común es único; la unicidad del límite también sigue de C06.

Junto con §10.2 queda demostrado el **criterio de Cauchy en $\mathbb R$**:

$$
(a_n)\text{ converge a algún real}\quad\Longleftrightarrow\quad
(a_n)\text{ es de Cauchy}.
$$

Como primer uso, una sucesión real cuyas colas tienen distancias arbitrariamente pequeñas ya tiene un destino, aunque sus datos no permitan adivinarlo. El criterio demuestra existencia; para calcular ese destino o controlar un error concreto necesitaremos información adicional, como la que desarrollaremos en §10.8.

El retorno geométrico es preciso: Cauchy estrecha intervalos y completitud asegura un real en su intersección. En $\mathbb Q$ pueden estrecharse del mismo modo sin contener un centro racional. La distancia y el conjunto en que se exige vivir al destino desempeñan funciones distintas.

![Los intervalos de cola de la alternancia recíproca se estrechan y contienen el mismo real cero. La prueba construye el centro como supremo de todos los inferiores; la muestra de cuatro intervalos sólo ilustra ese mecanismo.](../../assets/books/anm/C10/C10-F04.svg){#fig-anm-c10-f04 fig-alt="Los intervalos de cola de la alternancia recíproca se estrechan y contienen el mismo real cero. La prueba construye el centro como supremo de todos los inferiores; la muestra de cuatro intervalos sólo ilustra ese mecanismo."}

### Antes de seguir

#### Microcontrol 25

[]{#MA-MIC-ANM-01-010-025}

¿Cómo se define el candidato $L$ de la prueba principal?

[]{#MA-MSOL-ANM-01-010-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

$L=\sup\{\ell_N:N\in\mathbb N\}$, que existe por completitud porque el conjunto es no vacío y acotado superiormente.

El conjunto de extremos inferiores contiene $\ell_0$, así que no es vacío. Además, cada $\ell_N$ queda por debajo de $u_0$: basta tomar un término perteneciente a las dos colas para comparar ambos extremos. Por completitud existe su supremo $L$. Esta elección toma la barrera inferior más alta que imponen las colas. Luego se comprobará que ningún extremo superior queda por debajo de ella y que la anchura de las colas fuerza la convergencia.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-010-026}

¿Qué término compara $\ell_M$ con $u_N$ cuando los cortes son distintos?

[]{#MA-MSOL-ANM-01-010-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

$a_r$ con $r=\max\{M,N\}$ pertenece a ambas colas y da $\ell_M\le a_r\le u_N$.

Al elegir $r=\max\{M,N\}$ garantizamos simultáneamente $r\ge M$ y $r\ge N$. Por la primera desigualdad, $a_r\in T_M$ y $\ell_M\le a_r$; por la segunda, $a_r\in T_N$ y $a_r\le u_N$. Encadenando ambas relaciones obtenemos la comparación buscada. Usar sólo $a_M$ o sólo $a_N$ podría situar el término antes de uno de los cortes y dejar sin justificar una mitad del argumento.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-010-027}

¿Por qué $L\le u_N$ para cada $N$?

[]{#MA-MSOL-ANM-01-010-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

$u_N$ acota todos los $\ell_M$ por la comparación entre cortes, y el supremo $L$ es la menor cota superior de ese conjunto.

Fijemos $N$. La comparación anterior muestra que $\ell_M\le u_N$ para todo $M$, incluso cuando $M$ es anterior o posterior a $N$. Por tanto, $u_N$ es cota superior de todo el conjunto cuyo supremo define $L$. Como el supremo es la menor cota superior, $L\le u_N$. A la vez, $\ell_N\le L$ porque $\ell_N$ pertenece a ese conjunto. Así $L\in[\ell_N,u_N]$ para cada corte.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-010-028}

¿Dónde interviene completitud además de la existencia de extremos de cola?

[]{#MA-MSOL-ANM-01-010-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

En la existencia del supremo de los extremos inferiores, que construye el centro real común a todos los intervalos.

Hay dos usos de existencia distintos. Primero, cada cola acotada tiene sus propios extremos $\ell_N,u_N$. Después, el conjunto de todos los extremos inferiores tiene un supremo $L$. Este segundo paso reúne los encierros sucesivos en un candidato único que no cambia al pedir otra tolerancia. Sin él sólo tendríamos intervalos cada vez más estrechos, pero todavía no un punto del codominio cuya existencia y convergencia hubiéramos demostrado.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-010-029}

¿Por qué $|a_n-L|$ queda acotada por la anchura para $n\ge N$?

[]{#MA-MSOL-ANM-01-010-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Tanto $a_n$ como $L$ pertenecen a $[\ell_N,u_N]$, por lo que su distancia es a lo sumo $u_N-\ell_N$.

Si $x,y\in[\ell_N,u_N]$, entonces $x-y\le u_N-\ell_N$ y $y-x\le u_N-\ell_N$. Esas dos desigualdades equivalen a $|x-y|\le u_N-\ell_N$. Aplicamos esto con $x=a_n$ e $y=L$. Ahora Cauchy permite escoger un corte cuya anchura sea menor que cualquier tolerancia dada. La distancia a $L$ queda controlada por esa anchura para todos los índices posteriores, que es exactamente la convergencia.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-010-030}

¿Qué prueba la unicidad del real común a todos los intervalos?

[]{#MA-MSOL-ANM-01-010-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Dos supuestos centros tendrían distancia menor que cualquier tolerancia por el ancho pequeño; una distancia positiva contradice usar su mitad como tolerancia.

Supongamos que $L$ y $M$ pertenecen a todos los encierros y que $d=|L-M|>0$. Las anchuras pueden hacerse menores que $d/2$. Elegimos un corte con esa propiedad; como ambos puntos están en su intervalo, $d\le u_N-\ell_N<d/2$, contradicción. Por tanto $d=0$ y los puntos coinciden. El argumento usa una distancia fija entre los supuestos candidatos y una tolerancia escogida para contradecirla.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-010-031}

¿Necesita la prueba principal Bolzano–Weierstrass?

[]{#MA-MSOL-ANM-01-010-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

No. Construye $L$ mediante supremo y verifica convergencia directamente con los intervalos de cola y Cauchy.

La estrategia no extrae una subsucesión convergente. Obtiene los extremos de todas las colas, define $L$ como supremo de los inferiores y demuestra que $L$ está en cada encierro. Después usa la anchura pequeña para controlar $|a_n-L|$ en toda la cola. Así la prueba depende directamente de la completitud expresada mediante supremos. Bolzano–Weierstrass permitiría otra vía, pero no es necesario para cerrar ésta.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-010-032}

Enuncia el criterio de Cauchy con su codominio.

[]{#MA-MSOL-ANM-01-010-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

Una sucesión $a:\mathbb N\to\mathbb R$ converge a algún real si y sólo si es de Cauchy para la distancia usual.

La dirección «converge $\Rightarrow$ Cauchy» usa el límite ya existente y la desigualdad triangular. La dirección «Cauchy $\Rightarrow$ converge» construye ese límite mediante completitud. Debemos escribir el codominio porque la conclusión afirma la existencia de un destino dentro de él. La misma afirmación con $\mathbb Q$ sería falsa: la bisección que aproxima un número de cuadrado dos produce una sucesión racional de Cauchy sin límite racional.

</details>

### Ejercicios de la sección 10.4

#### Ejercicio 16. Comparar cortes distintos

[]{#MA-EX-ANM-01-010-016}

Prueba $\ell_M\le u_N$ para cualesquiera cortes $M,N$ y explica por qué se necesita en la construcción del destino.

[]{#MA-SOL-ANM-01-010-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

El índice $r=\max\{M,N\}$ pertenece a ambas colas y da $\ell_M\le a_r\le u_N$. Por ello cada $u_N$ acota a todo el conjunto de inferiores. Esto permite deducir $\sup_M\ell_M\le u_N$. La desigualdad de extremos con el mismo corte no proporciona por sí sola esa cota de todo el conjunto.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 17. Existencia y comprobación

[]{#MA-EX-ANM-01-010-017}

Construye $L$ para una sucesión de Cauchy sin invocar convergencia monótona ni Bolzano–Weierstrass y verifica el límite.

[]{#MA-SOL-ANM-01-010-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Por acotación existen extremos reales de cada cola. El conjunto no vacío de inferiores es acotado superiormente y tiene supremo $L$ por completitud. La comparación entre cortes da $\ell_N\le L\le u_N$ para todo $N$. Dada $\varepsilon>0$, usar Cauchy con $\varepsilon/2$ para obtener anchura a lo sumo $\varepsilon/2$ en una cola. Todos sus términos y $L$ están en ese intervalo, de modo que $|a_n-L|\le\varepsilon/2<\varepsilon$.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 18. Intersección única

[]{#MA-EX-ANM-01-010-018}

Demuestra que la intersección de los intervalos de cola de una sucesión real de Cauchy es un singleton.

[]{#MA-SOL-ANM-01-010-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

El real $L$ construido pertenece a todos los intervalos. Si $x,y$ estuvieran en la intersección y su distancia fuera $d>0$, Cauchy con tolerancia $d/2$ daría un intervalo de anchura a lo sumo $d/2$ que contiene a ambos. Eso contradice su distancia $d$. Por tanto sólo contiene a $L$.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 19. Recuperar el criterio desde anchuras

[]{#MA-EX-ANM-01-010-019}

Para una sucesión real acotada, prueba que es de Cauchy si y sólo si $u_N-\ell_N\to0$, sin usar el criterio de convergencia.

[]{#MA-SOL-ANM-01-010-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Cauchy con tolerancia $\varepsilon/2$ fuerza anchura a lo sumo $\varepsilon/2$ en todos los cortes posteriores, por §10.3; así las anchuras tienden a cero. Recíprocamente, dada $\varepsilon>0$, escoger un corte con anchura menor que $\varepsilon$. Todo par posterior está en su intervalo, por lo que su distancia es a lo sumo la anchura y menor que $\varepsilon$. Se compara control de pares y geometría sin usar aún existencia de límite.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 20. Conocer una extracción basta con Cauchy

[]{#MA-EX-ANM-01-010-020}

Supón que $a$ es de Cauchy y que $a_{\varphi(k)}\to L$, donde $\varphi:\mathbb N\to\mathbb N$ es estrictamente creciente. Demuestra directamente $a_n\to L$.

[]{#MA-SOL-ANM-01-010-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Una inducción da $\varphi(k)\ge k$. Para $\varepsilon>0$, tomar el corte $N_1$ de Cauchy con tolerancia $\varepsilon/2$ y el corte $K$ de la extracción para la misma tolerancia respecto de $L$. Fijar $k=\max\{K,N_1\}$, así $\varphi(k)\ge N_1$ y $|a_{\varphi(k)}-L|<\varepsilon/2$. Para todo $n\ge N_1$, $|a_n-L|\le|a_n-a_{\varphi(k)}|+|a_{\varphi(k)}-L|<\varepsilon$. Se necesita una extracción ya dada, no BW.

</details>
## 10.5. Negar Cauchy: encontrar pares separados

[]{#MA-SEC-ANM-01-010-005}

El criterio ofrece un método para demostrar que una sucesión real no converge: basta encontrar una tolerancia que ninguna cola pueda satisfacer. La negación completa es

$$
\exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists p,q\ge N:
\quad |a_p-a_q|\ge\varepsilon_0.
$$

La tolerancia $\varepsilon_0$ queda fija antes del corte adversario. Los testigos pueden depender de $N$. La igualdad pertenece a la negación porque la definición original exige desigualdad estricta. Si se permitiera una tolerancia positiva diferente en cada cola, no estaríamos negando Cauchy: incluso $1/(n+1)$ tiene términos distintos después de cualquier corte.

En $(-1)^n$ sirven $\varepsilon_0=1$ y $p=N,q=N+1$. En $a_n=n$, los mismos índices dan distancia uno y vuelven a impedir Cauchy. El primer ejemplo es acotado y el segundo no; el argumento pareado funciona en ambos.

Hay un error más sutil: confundir Cauchy con $|a_{n+1}-a_n|\to0$. Cauchy sí implica esa condición: recibido $\varepsilon$, su corte controla los pares $(n+1,n)$ para todo $n\ge N$. La vuelta es falsa porque una separación pequeña repetida muchas veces puede producir una distancia grande.

Para verlo sin usar teoría de series, definamos las **sumas finitas** $h_n=\sum_{j=1}^{n+1}1/j$. Cada $h_n$ es un real obtenido por una suma con finitos sumandos. Su salto es $h_{n+1}-h_n=1/(n+2)$ y tiende a cero. Sin embargo, para cada entero $m\ge1$,

$$
h_{2m-1}-h_{m-1}=\sum_{j=m+1}^{2m}\frac1j
\ge m\frac1{2m}=\frac12.
$$

Después de cualquier corte $N$, tomamos $m=N+1$. Ambos índices $m-1$ y $2m-1$ están después del corte y su distancia es al menos $1/2$. La tolerancia fija $\varepsilon_0=1/2$ prueba que $h$ no es de Cauchy y, por el criterio, no converge en $\mathbb R$. No necesitamos dar un significado a una suma infinita ni aplicar un criterio del capítulo siguiente.

El contraejemplo también explica por qué controlar sólo un número fijo de vecinos es insuficiente. Para cada desplazamiento fijo $r$, la diferencia $h_{n+r}-h_n$ tiene $r$ sumandos y es a lo sumo $r/(n+2)$, que tiende a cero. Cauchy exige un corte válido aunque la separación entre índices crezca sin una cota fija.

Una gráfica temporal de muestra finita puede mostrar los saltos cada vez menores y aun ocultar la separación de bloques muy tardíos. La prueba debe elegir pares después de cualquier corte; esa libertad del adversario es la que el gráfico por sí solo no resuelve.

![En las sumas finitas de recíprocos, los saltos entre vecinos disminuyen. Los pares al final de bloques de longitud creciente siguen separados por al menos medio; un desplazamiento temporal creciente detecta el fallo de Cauchy.](../../assets/books/anm/C10/C10-F05.svg){#fig-anm-c10-f05 fig-alt="En las sumas finitas de recíprocos, los saltos entre vecinos disminuyen. Los pares al final de bloques de longitud creciente siguen separados por al menos medio; un desplazamiento temporal creciente detecta el fallo de Cauchy."}

### Antes de seguir

#### Microcontrol 33

[]{#MA-MIC-ANM-01-010-033}

¿Qué orden de cuantificadores expresa no ser de Cauchy?

[]{#MA-MSOL-ANM-01-010-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Existe $\varepsilon_0>0$ tal que para todo corte $N$ existen $p,q\ge N$ con $|a_p-a_q|\ge\varepsilon_0$.

La definición es $\forall\varepsilon>0\;\exists N\;\forall p,q\ge N:\ |a_p-a_q|<\varepsilon$. Al negarla, cada cuantificador cambia: existe una tolerancia para la cual ningún corte funciona, y después de cada corte aparece algún par infractor. La pertenencia de ambos índices a la cola debe mantenerse junto con la infracción. No basta presentar un único par temprano; hay que producir pares posteriores a cualquier corte que se proponga.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-010-034}

¿Puede la tolerancia de la negación cambiar con $N$?

[]{#MA-MSOL-ANM-01-010-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

No. Debe quedar fija antes de considerar cualquier corte; los índices testigo sí pueden depender de $N$.

Para refutar Cauchy debemos encontrar una precisión fija que siga fallando, por mucho que avancemos. Si permitiéramos que $\varepsilon_0$ disminuyera después de recibir cada $N$, estaríamos cambiando el desafío y podríamos confundir una sucesión que se concentra con otra que no lo hace. En cambio, los índices del par infractor se eligen después del corte: su función es mostrar que aquella precisión fija todavía falla en esa cola.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-010-035}

¿Por qué la negación usa $\ge$ y no sólo $>$?

[]{#MA-MSOL-ANM-01-010-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Porque se niega una desigualdad estricta $|a_p-a_q|<\varepsilon_0$; la igualdad también hace fallar la condición.

La negación de $d<\varepsilon_0$ es $d\ge\varepsilon_0$, porque el caso de igualdad también queda fuera del intervalo permitido. Por ejemplo, en $a_n=n$ los pares vecinos tienen distancia exactamente uno. Esa igualdad basta para hacer fallar la tolerancia $\varepsilon_0=1$. Si exigiéramos sólo distancias mayores que uno, estaríamos descartando testigos legítimos y no habríamos escrito la negación lógica exacta.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-010-036}

Da testigos para negar Cauchy en $a_n=n$.

[]{#MA-MSOL-ANM-01-010-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Con $\varepsilon_0=1$ y cualquier corte $N$, tomar $p=N,q=N+1$ da distancia uno.

Fijamos primero $\varepsilon_0=1$. Cuando se propone un corte arbitrario $N$, respondemos con $p=N$ y $q=N+1$, que satisfacen las dos condiciones de pertenencia a la cola. Como $a_p=p$ y $a_q=q$, resulta $|a_p-a_q|=|N-(N+1)|=1\ge\varepsilon_0$. La construcción funciona para todo $N$ con la misma tolerancia. Esto verifica todos los cuantificadores de la negación, no sólo un ejemplo de separación.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-010-037}

¿Qué ocurre con $|a_{n+1}-a_n|$ si $a$ es de Cauchy?

[]{#MA-MSOL-ANM-01-010-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

Tiende a cero: para cada tolerancia, el corte de Cauchy controla todos los pares vecinos posteriores.

Sea $\varepsilon>0$. Cauchy entrega un corte $N$ que controla cualquier par de índices posteriores. Para todo $n\ge N$, los dos índices $n$ y $n+1$ cumplen esa condición, luego $|a_{n+1}-a_n|<\varepsilon$. Como el salto es no negativo, esta desigualdad prueba que converge a cero. La recíproca no está contenida en el argumento: controlar vecinos no controla automáticamente la acumulación de muchos saltos.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-010-038}

¿Cuál es el salto de $h_n=\sum_{j=1}^{n+1}1/j$?

[]{#MA-MSOL-ANM-01-010-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

$h_{n+1}-h_n=1/(n+2)$, que tiende a cero por arquimedianidad.

Al restar las dos sumas finitas, se cancelan los términos desde $1$ hasta $1/(n+1)$ y sólo queda el término nuevo $1/(n+2)$. Para demostrar que tiende a cero, dados $\varepsilon>0$ escogemos $N$ con $N+2>1/\varepsilon$. Si $n\ge N$, entonces $0<1/(n+2)\le1/(N+2)<\varepsilon$. La cancelación explica la fórmula y la elección del corte demuestra el límite, sin invocar una suma infinita.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-010-039}

¿Qué pares de índices muestran que $h$ no es de Cauchy?

[]{#MA-MSOL-ANM-01-010-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

Para $m\ge1$, los índices $m-1$ y $2m-1$ tienen distancia al menos $1/2$. Dado $N$, elegir $m=N+1$ los deja ambos posteriores al corte.

La diferencia correspondiente es
$$h_{2m-1}-h_{m-1}=\sum_{j=m+1}^{2m}\frac1j.$$
Hay $m$ sumandos y cada uno es al menos $1/(2m)$; por tanto la suma es al menos $1/2$. Fijamos esa tolerancia y, recibido $N$, tomamos $m=N+1$. Los índices son entonces $N$ y $2N+1$, ambos posteriores. Este bloque finito conserva una separación fija aunque cada salto vecino sea cada vez menor.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-010-040}

¿El contraejemplo de $h$ necesita una suma infinita?

[]{#MA-MSOL-ANM-01-010-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No. Todos los términos y diferencias usados son sumas finitas; la separación de bloques basta para negar Cauchy.

Para cada índice $n$, $h_n$ está definido por una suma finita. También la diferencia entre dos términos es una suma finita sobre un bloque de índices. La negación de Cauchy se acredita estimando ese bloque desde abajo por $1/2$. No necesitamos decidir el valor de una serie infinita ni afirmar previamente su divergencia. El contraejemplo queda establecido por pares explícitos que sobreviven después de cualquier corte.

</details>

### Ejercicios de la sección 10.5

#### Ejercicio 21. Negación exacta

[]{#MA-EX-ANM-01-010-021}

Escribe la negación de Cauchy y úsala para $a_n=(-1)^n$.

[]{#MA-SOL-ANM-01-010-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Existe $\varepsilon_0>0$ tal que para cada $N$ existen $p,q\ge N$ con $|a_p-a_q|\ge\varepsilon_0$. Para la alternancia escoger $\varepsilon_0=1$ y los índices $N,N+1$, cuya distancia es dos. La tolerancia se fija primero; los testigos se escogen después del corte.

</details>

#### Ejercicio 22. Tolerancia móvil

[]{#MA-EX-ANM-01-010-022}

¿Niega Cauchy que para cada corte haya dos términos distintos? Da un ejemplo que decida.

[]{#MA-SOL-ANM-01-010-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

No. $1/(n+1)$ tiene términos distintos después de cada corte, pero es de Cauchy. La distancia de los testigos puede hacerse tan pequeña como se quiera al mover el corte; no hay una tolerancia positiva fija que todas las colas infrinjan.

</details>

#### Ejercicio 23. Bloques separados

[]{#MA-EX-ANM-01-010-023}

Prueba que $h_n=\sum_{j=1}^{n+1}1/j$ no es de Cauchy aunque $h_{n+1}-h_n\to0$.

[]{#MA-SOL-ANM-01-010-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

El salto es $1/(n+2)$ y tiende a cero. Para $m\ge1$, la diferencia $h_{2m-1}-h_{m-1}$ contiene $m$ sumandos, cada uno al menos $1/(2m)$, y por tanto es al menos $1/2$. Dado $N$, tomar $m=N+1$ deja ambos índices posteriores. La tolerancia fija $1/2$ niega Cauchy. Todas las sumas usadas son finitas.

Después de la prueba, puede retomarse la [figura 10.5](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f05) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 24. Vecindad de longitud fija

[]{#MA-EX-ANM-01-010-024}

Prueba que para cada natural fijo $r$, $h_{n+r}-h_n\to0$ en el ejemplo anterior. ¿Por qué sigue fallando Cauchy?

[]{#MA-SOL-ANM-01-010-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Si $r=0$ la diferencia es cero. Si $r>0$, contiene $r$ sumandos con denominadores al menos $n+2$, luego $0\le h_{n+r}-h_n\le r/(n+2)\to0$. El corte suficiente puede depender de $r$. Cauchy exige un único corte para todas las separaciones posibles, y los bloques con longitud creciente mantienen distancia al menos $1/2$.

Después de la prueba, puede retomarse la [figura 10.5](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f05) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 25. Acotada con saltos pequeños

[]{#MA-EX-ANM-01-010-025}

Construye una sucesión acotada con saltos que tienden a cero y que no sea de Cauchy. Sugerencia: concatena para $m=1,2,\ldots$ los bloques $0,1/m,\ldots,1,(m-1)/m,\ldots,0$.

[]{#MA-SOL-ANM-01-010-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Concatenar los bloques de la sugerencia y reindexar desde cero. Todos los valores están en $[0,1]$. Dentro del bloque $m$, cada salto es $1/m$; entre bloques ambos valores de unión son cero y el salto es cero. Dada $\varepsilon>0$, después de los finitos bloques con $m$ pequeño todos los saltos son menores que $\varepsilon$. Pero cada bloque tardío contiene cero y uno; después de cualquier corte se puede elegir un bloque completo y dos índices con distancia uno. La tolerancia fija uno niega Cauchy. La acotación no repara el fallo de controlar sólo vecinos.

</details>
## 10.6. Conservar el control al operar

[]{#MA-SEC-ANM-01-010-006}

El criterio permite transportar las reglas de convergencia de C06. También conviene reconocer cómo actúan directamente sobre las distancias: así sabremos qué hipótesis usa cada operación sin necesitar los destinos.

Si $a,b$ son de Cauchy, para $\varepsilon>0$ elegimos sus cortes con tolerancia $\varepsilon/2$ y tomamos el máximo. Para todo par posterior,

$$
|(a_p+b_p)-(a_q+b_q)|
\le|a_p-a_q|+|b_p-b_q|<\varepsilon.
$$

Por ello $a+b$ es de Cauchy. La misma estimación con una resta prueba que $a-b$ lo es. Una traslación constante no cambia distancias. Para multiplicar por un real $c\ne0$, basta usar tolerancia $\varepsilon/|c|$ en $a$; si $c=0$, el producto es constante cero y sirve corte cero.

**El producto necesita cotas.** Por §10.3, fijemos $A,B\ge0$ con $|a_n|\le A$, $|b_n|\le B$ en todos los índices. Descomponer en dos errores da

$$
|a_pb_p-a_qb_q|
\le |a_p|\,|b_p-b_q|+|b_q|\,|a_p-a_q|.
$$

Elegimos cortes de $b$ con tolerancia $\varepsilon/[2(A+1)]$ y de $a$ con tolerancia $\varepsilon/[2(B+1)]$. Para pares posteriores al máximo, la cota es menor que $\varepsilon$, porque $A/(A+1)<1$ y $B/(B+1)<1$. Los denominadores añadidos evitan dividir por una cota cero. El producto es de Cauchy sin hipótesis de signo sobre los términos.

**Los recíprocos necesitan distancia a cero.** Si $|a_n|\ge c>0$ para $n\ge N_0$, los recíprocos de esa cola están definidos y

$$
\left|\frac1{a_p}-\frac1{a_q}\right|
=\frac{|a_p-a_q|}{|a_pa_q|}\le\frac{|a_p-a_q|}{c^2}.
$$

Usamos el corte de Cauchy de $a$ para tolerancia $c^2\varepsilon$ y lo combinamos con $N_0$. Si algún término previo es cero, no existe una sucesión de recíprocos en todos los índices: podemos reindexar esa cola o asignar al prefijo valores reales arbitrarios. Si todos los términos son no nulos, la sucesión completa de recíprocos es de Cauchy. La condición «ningún término es cero» por sí sola no basta: $a_n=1/(n+1)$ es de Cauchy y no nula, pero sus recíprocos $n+1$ no lo son.

También el valor absoluto conserva Cauchy, porque $\big||a_p|-|a_q|\big|\le|a_p-a_q|$. Si $a$ es de Cauchy y $b_n-a_n\to0$, entonces la diferencia es de Cauchy por §10.2 y la regla de suma hace a $b$ de Cauchy. Por C06 comparten límite cuando la diferencia tiende a cero. El signo oscilante de una perturbación no impide su desaparición.

Finalmente, cambiar finitos términos o suprimir un prefijo conserva Cauchy: después del último índice cambiado las distancias son las mismas; al reindexar una cola sólo se trasladan cortes. Estas reglas separan cambios del objeto completo de cambios en su comportamiento tardío.

### Antes de seguir

#### Microcontrol 41

[]{#MA-MIC-ANM-01-010-041}

¿Qué corte sirve para probar que la suma de dos sucesiones de Cauchy es de Cauchy?

[]{#MA-MSOL-ANM-01-010-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

El máximo de sus cortes para tolerancia $\varepsilon/2$; las dos diferencias de sumandos dan una distancia total menor que $\varepsilon$.

Sean $a$ y $b$ las dos sucesiones. Elegimos cortes $N_a,N_b$ para la precisión $\varepsilon/2$ y tomamos $N=\max\{N_a,N_b\}$. Si $p,q\ge N$, ambos controles valen y
$$|(a_p+b_p)-(a_q+b_q)|\le|a_p-a_q|+|b_p-b_q|<\varepsilon.$$
El máximo sincroniza las colas; la desigualdad triangular reúne los errores. Así obtenemos un solo corte que funciona para todos los pares de la suma.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-010-042}

¿Qué sucede al multiplicar por cero?

[]{#MA-MSOL-ANM-01-010-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

La sucesión resultante es constante cero y es de Cauchy con corte cero; no se divide por el escalar.

Para el escalar cero, los términos son $0a_n=0$ cualquiera que sea la sucesión original. La distancia entre dos términos resultantes es cero y el corte inicial sirve para toda tolerancia. Este caso debe separarse de la regla para un escalar $c\ne0$, que escoge la precisión $\varepsilon/|c|$ en la sucesión original. Escribir esa división cuando $c=0$ introduciría una cantidad no definida.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-010-043}

¿Por qué el argumento del producto necesita acotación?

[]{#MA-MSOL-ANM-01-010-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Porque la diferencia del producto contiene factores $|a_p|$ y $|b_q|$ multiplicando las diferencias; cotas globales los controlan.

La identidad útil es $a_pb_p-a_qb_q=a_p(b_p-b_q)+b_q(a_p-a_q)$. Al tomar valor absoluto aparecen los factores $|a_p|$ y $|b_q|$. Las diferencias pequeñas no bastarían si esos factores pudieran crecer sin control. Como las sucesiones de Cauchy son acotadas, elegimos cotas globales $A,B$ y obtenemos $|a_pb_p-a_qb_q|\le A|b_p-b_q|+B|a_p-a_q|$. Ahora sí podemos repartir una tolerancia final entre dos errores controlables.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-010-044}

¿Por qué se usan denominadores $A+1$ y $B+1$ al escoger tolerancias para el producto?

[]{#MA-MSOL-ANM-01-010-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Para mantenerlos positivos incluso si una cota es cero y obtener una estimación estrictamente menor que la tolerancia final.

Si $|a_n|\le A$ y $|b_n|\le B$, pedimos $|b_p-b_q|<\varepsilon/(2(A+1))$ y $|a_p-a_q|<\varepsilon/(2(B+1))$. El máximo de los cortes garantiza ambas condiciones. La cota del producto resulta menor que
$$\frac\varepsilon2\frac A{A+1}+\frac\varepsilon2\frac B{B+1}<\varepsilon.$$
Los denominadores son positivos incluso si una cota vale cero. La elección evita dividir por cero y deja un margen respecto de la tolerancia final.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-010-045}

¿Qué hipótesis de una cola permite controlar recíprocos?

[]{#MA-MSOL-ANM-01-010-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

$|a_n|\ge c>0$ desde algún corte; entonces la diferencia de recíprocos es a lo sumo $|a_p-a_q|/c^2$.

Sobre esa cola los términos no son cero, así que podemos escribir
$$\left|\frac1{a_p}-\frac1{a_q}\right|=\frac{|a_p-a_q|}{|a_pa_q|}\le\frac{|a_p-a_q|}{c^2}.$$
Recibida $\varepsilon>0$, pedimos a $a$ la precisión $\varepsilon c^2$. Tomamos el máximo de su corte y del corte que garantiza la separación respecto de cero. Entonces la distancia entre los recíprocos es menor que $\varepsilon$. Si sólo están definidos eventualmente, el argumento se aplica a esa cola.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-010-046}

¿Ser no nula término a término basta para que una sucesión de Cauchy tenga recíprocos de Cauchy?

[]{#MA-MSOL-ANM-01-010-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

No. $1/(n+1)$ es no nula y de Cauchy, pero sus recíprocos $n+1$ no lo son.

En $a_n=1/(n+1)$, cada término es positivo, pero no existe una cota inferior positiva común para una cola. Al invertirlos obtenemos $b_n=n+1$. Para cualquier corte $N$, los índices $N$ y $N+1$ dan $|b_{N+1}-b_N|=1$, de modo que falla la tolerancia fija uno. La inversión amplifica las diferencias cerca de cero; por eso hace falta estar separado de cero, además de evitar el valor cero término a término.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-010-047}

¿Qué desigualdad demuestra que el valor absoluto conserva Cauchy?

[]{#MA-MSOL-ANM-01-010-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

$\big||a_p|-|a_q|\big|\le|a_p-a_q|$, la desigualdad triangular inversa.

La desigualdad triangular da $|a_p|\le|a_p-a_q|+|a_q|$, luego $|a_p|-|a_q|\le|a_p-a_q|$. Intercambiando los índices obtenemos la desigualdad contraria para la diferencia de magnitudes. Juntas implican la cota indicada. Para cada tolerancia, el mismo corte que controla $|a_p-a_q|$ controla entonces la distancia entre $|a_p|$ y $|a_q|$. No se requieren cortes nuevos ni conocer los signos de los términos.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-010-048}

¿Cambiar finitos términos conserva Cauchy?

[]{#MA-MSOL-ANM-01-010-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Sí. Después del último índice cambiado las distancias de todos los pares coinciden con las originales.

Sea $K$ un índice a partir del cual las sucesiones original y modificada coinciden. Dada una tolerancia, elegimos un corte $N$ de Cauchy para la original y usamos $\max\{N,K\}$. Después de ese corte, ninguno de los dos términos de un par ha sido modificado, así que sus distancias son las originales y satisfacen la misma estimación. El argumento funciona en ambas direcciones porque la coincidencia eventual es simétrica.

</details>

### Ejercicios de la sección 10.6

#### Ejercicio 26. Álgebra por distancias

[]{#MA-EX-ANM-01-010-026}

Prueba directamente que suma, diferencia y escala real de sucesiones de Cauchy son de Cauchy, tratando el escalar cero.

[]{#MA-SOL-ANM-01-010-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Para suma y diferencia, triangular acota su diferencia de términos por la suma de las diferencias de cada factor; tomar máximo de cortes con tolerancia $\varepsilon/2$. Para escalar no cero, usar la tolerancia $\varepsilon/|c|$, ya que la nueva distancia es $|c|$ veces la original. Si $c=0$, la sucesión es constante y sirve corte cero.

</details>

#### Ejercicio 27. Producto sin conocer destinos

[]{#MA-EX-ANM-01-010-027}

Prueba que el producto de dos sucesiones reales de Cauchy es de Cauchy usando sus cotas globales.

[]{#MA-SOL-ANM-01-010-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Por acotación, fijar $A,B\ge0$ con magnitudes de $a,b$ a lo sumo esos números. La identidad $a_pb_p-a_qb_q=a_p(b_p-b_q)+b_q(a_p-a_q)$ da cota $A|b_p-b_q|+B|a_p-a_q|$. Escoger cortes con tolerancias $\varepsilon/[2(A+1)]$ para $b$ y $\varepsilon/[2(B+1)]$ para $a$. Después del máximo la cota es a lo sumo la suma de dos cantidades menores que $\varepsilon/2$, con casos de cota cero igualmente controlados. No se requiere signo positivo de términos.

</details>

#### Ejercicio 28. Recíprocos y prefijo

[]{#MA-EX-ANM-01-010-028}

Sea $a$ de Cauchy y $|a_n|\ge c>0$ para $n\ge N_0$. Prueba que la sucesión $b_k=1/a_{k+N_0}$ es de Cauchy. ¿Qué ocurre con términos cero anteriores?

[]{#MA-SOL-ANM-01-010-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Los recíprocos de esta cola están definidos. Para un corte original $H$ que controle $a$ con tolerancia $c^2\varepsilon$, tomar un corte nuevo $K=\max\{H,N_0\}$. Si $p,q\ge K$, sus índices originales $p+N_0,q+N_0$ superan ambos cortes y la distancia de recíprocos es a lo sumo la distancia de términos dividida por $c^2$, menor que $\varepsilon$. Los ceros previos no afectan a esta cola reindexada, pero impedirían definir recíprocos en todos los índices de $a$.

</details>

#### Ejercicio 29. Diferencia de Cauchy no es error nulo

[]{#MA-EX-ANM-01-010-029}

Si $a,b$ son de Cauchy y $a-b$ también lo es, ¿deben tener el mismo límite? ¿Qué condición basta?

[]{#MA-SOL-ANM-01-010-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

No. Las constantes $a_n=0$ y $b_n=1$ son de Cauchy y su diferencia constante menos uno también, con destinos distintos. Basta que $a_n-b_n\to0$: ambos tienen límites reales por el criterio y la regla de resta de C06 da diferencia de límites cero. Ser de Cauchy para la diferencia sólo asegura que ésta tiene algún límite, no que sea cero.

</details>

#### Ejercicio 30. Valor absoluto no tiene recíproca

[]{#MA-EX-ANM-01-010-030}

Prueba que $a$ de Cauchy implica $|a|$ de Cauchy y muestra que la vuelta falla.

[]{#MA-SOL-ANM-01-010-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La triangular inversa $\big||a_p|-|a_q|\big|\le|a_p-a_q|$ permite usar el mismo corte. Para la vuelta, $a_n=(-1)^n$ no es de Cauchy, mientras $|a_n|=1$ es constante. La operación olvida el signo y puede borrar separaciones.

</details>
## 10.7. La distancia permanece; el codominio cambia

[]{#MA-SEC-ANM-01-010-007}

Una sucesión con valores racionales puede verse como $q:\mathbb N\to\mathbb Q$ y, mediante la inclusión canónica $\iota:\mathbb Q\to\mathbb R$, como $\iota\circ q:\mathbb N\to\mathbb R$. Los valores numéricos transportados y sus distancias coinciden. Pero «converge en $\mathbb Q$» exige un destino racional y «converge en $\mathbb R$» permite un destino real. Cambiar codominio cambia el contrato de convergencia, aunque no cambie los números de cada evaluación.

Construiremos un ejemplo desde el control interno, sin presuponer que ya existe una raíz real de dos. Primero recordemos un argumento algebraico: no hay un racional cuyo cuadrado sea dos. Si $r=s/t$ con enteros coprimos y $t>0$ cumpliera $r^2=2$, tendríamos $s^2=2t^2$. Un entero con cuadrado par es par, de modo que $s=2v$. Sustituyendo, $t^2=2v^2$, por lo que $t$ también sería par, contradiciendo coprimalidad.

Partimos del intervalo racional $[l_0,u_0]=[1,2]$. Dado $[l_n,u_n]$, formamos el punto medio racional $t_n=(l_n+u_n)/2$. Si $t_n^2<2$, ponemos $l_{n+1}=t_n,u_{n+1}=u_n$; si $t_n^2>2$, ponemos $l_{n+1}=l_n,u_{n+1}=t_n$. La igualdad es imposible por el argumento anterior. La recursión determina extremos racionales y conserva

$$
1\le l_n<u_n\le2,\qquad l_n^2<2<u_n^2,
\qquad u_n-l_n=2^{-n}.
$$

Los intervalos están encajados y la anchura se divide por dos en cada paso. Si $p,q\ge N$, ambos extremos inferiores $l_p,l_q$ están dentro de $[l_N,u_N]$, por lo que $|l_p-l_q|\le2^{-N}$. La desigualdad $2^N\ge N+1$, probada por inducción, y arquimedianidad permiten escoger $N$ con $2^{-N}<\varepsilon$. Así la sucesión de extremos inferiores es de Cauchy. Lo mismo vale para los superiores.

Por el criterio real recién demostrado, $l_n\to L\in\mathbb R$. Como $u_n-l_n=2^{-n}\to0$, las reglas de C06 dan $u_n\to L$. Las cotas $1\le l_n<u_n\le2$ implican $1\le L\le2$. La regla del producto y conservación del orden aplicada a $l_n^2<2<u_n^2$ dan $L^2\le2$ y $L^2\ge2$. En consecuencia $L^2=2$. Hemos construido el real positivo que se denota $\sqrt2$; es único, porque si $x,y>0$ y $x^2=y^2$, entonces $(x-y)(x+y)=0$ con $x+y>0$, luego $x=y$.

Ese límite no es racional. Si la sucesión racional $l$ convergiera a algún $r\in\mathbb Q$, al incluirla en $\mathbb R$ convergería a $\iota(r)$. La unicidad del límite real obligaría $\iota(r)=L$, lo cual contradice que ningún racional tiene cuadrado dos. La sucesión es de Cauchy en distancia usual y no tiene límite en $\mathbb Q$.

La diferencia con la recta real está ahora probada: Cauchy proporciona coherencia de una cola; completitud del codominio proporciona el destino dentro de él. Llamaremos **secuencialmente completo**, para la distancia usual en un subconjunto de $\mathbb R$, a un conjunto en el que toda sucesión de Cauchy con valores en ese conjunto converge a un elemento suyo. Hemos probado que $\mathbb R$ lo es y que $\mathbb Q$ no lo es. No estamos construyendo otro modelo de los reales por clases de sucesiones; identificamos una propiedad del modelo ya disponible.

**Raíces generales: reunir una herramienta ya demostrada.** El ejercicio 30 de C07 y su solución construyeron la raíz de cualquier parámetro positivo. Recuperemos aquí el argumento para que la herramienta quede disponible en el manuscrito, sin depender de que el lector haya resuelto ese ejercicio. Sea $\rho>0$, tomemos $x_0=\rho+1$ y definamos $x_{n+1}=(x_n+\rho/x_n)/2$. La positividad y las identidades finitas
$$x_{n+1}^2-\rho=\frac{(x_n^2-\rho)^2}{4x_n^2},\qquad
x_n-x_{n+1}=\frac{x_n^2-\rho}{2x_n}$$
conservan $x_n^2>\rho$ y hacen decrecer estrictamente la sucesión, porque $x_0^2-\rho=\rho^2+\rho+1>0$. Con $m=\min\{1,\rho\}>0$, se tiene $m^2\le\rho$; por ello $x_n\le m$ contradiría $x_n^2>\rho$. C07 da un límite $L\ge m>0$. Las reglas de C06 permiten pasar al límite en la recurrencia, incluido el cociente, y dan $L=(L+\rho/L)/2$, luego $L^2=\rho$.

Si $u,v>0$ tienen ese cuadrado, $(u-v)(u+v)=0$ y $u+v>0$ fuerzan $u=v$. Para $\rho=0$, la única raíz no negativa es cero. Así queda definida para todo $\rho\ge0$ una única raíz no negativa $\sqrt\rho$. Su orden también está acreditado: si $0\le\rho\le\sigma$ pero $\sqrt\rho>\sqrt\sigma$, la comparación de cuadrados no negativos daría $\rho>\sigma$, contradicción. Este resultado sólo usa monotonía, completitud y álgebra de límites anteriores; no continuidad de funciones, valor intermedio ni derivadas. La continuidad de la función raíz se probará después en su lugar correspondiente.

![Los extremos racionales de la bisección conservan el cuadrado dos entre sus cuadrados y reducen la anchura. El centro común existe en la recta real; ningún punto racional puede ocuparlo.](../../assets/books/anm/C10/C10-F06.svg){#fig-anm-c10-f06 fig-alt="Los extremos racionales de la bisección conservan el cuadrado dos entre sus cuadrados y reducen la anchura. El centro común existe en la recta real; ningún punto racional puede ocuparlo."}

| n | Extremo inferior racional | Extremo superior racional | Anchura |
|---|---|---|---|
| 0 | 1 | 2 | 1 |
| 1 | 1 | 3/2 | 1/2 |
| 2 | 5/4 | 3/2 | 1/4 |
| 3 | 11/8 | 3/2 | 1/8 |
| 4 | 11/8 | 23/16 | 1/16 |
| 5 | 45/32 | 23/16 | 1/32 |

### Antes de seguir

#### Microcontrol 49

[]{#MA-MIC-ANM-01-010-049}

¿Qué cambia al pasar de $q:\mathbb N\to\mathbb Q$ a $\iota\circ q:\mathbb N\to\mathbb R$?

[]{#MA-MSOL-ANM-01-010-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

Cambia el codominio y el conjunto permitido de destinos; los valores transportados y sus distancias usuales coinciden.

La inclusión usual $\iota:\mathbb Q\to\mathbb R$ conserva las distancias: $|\iota(r)-\iota(s)|=|r-s|$. Por eso los mismos cortes verifican Cauchy antes y después de incluir la sucesión en los reales. Lo que cambia es la conclusión de existencia: un límite en $\mathbb R$ puede no estar en la copia de $\mathbb Q$. Conservar distancias no garantiza que el sistema de partida contenga todos los destinos que sus aproximaciones necesitan.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-010-050}

¿Por qué el punto medio racional de la bisección no tiene cuadrado dos?

[]{#MA-MSOL-ANM-01-010-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

Ningún racional tiene cuadrado dos: en una fracción reducida esa igualdad obligaría a que numerador y denominador fueran ambos pares.

Si un racional $m/n$ en términos reducidos, con $n>0$, tuviera cuadrado dos, entonces $m^2=2n^2$. El cuadrado de un impar es impar, así que $m$ debe ser par: $m=2k$. Sustituyendo resulta $n^2=2k^2$, lo que obliga también a que $n$ sea par. Ambos tendrían el factor común dos, contradiciendo que la fracción estaba reducida. El punto medio de dos racionales es racional y queda sujeto al mismo argumento.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-010-051}

¿Cuál es la anchura del intervalo tras $n$ bisecciones?

[]{#MA-MSOL-ANM-01-010-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

$u_n-l_n=2^{-n}$, porque se empieza con anchura uno y cada paso la divide por dos.

La anchura inicial es $u_0-l_0=1$. Si en el paso $n$ vale $2^{-n}$, sustituir uno de los extremos por el punto medio deja una anchura igual a la mitad: $2^{-n}/2=2^{-(n+1)}$. Por inducción, la fórmula vale para todo índice. La elección de la mitad izquierda o derecha cambia la localización del intervalo, pero no esta regla de longitud. No estamos suponiendo todavía que exista un número de cuadrado dos.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-010-052}

¿Qué controla $|l_p-l_q|$ cuando $p,q\ge N$?

[]{#MA-MSOL-ANM-01-010-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

La anchura $2^{-N}$, porque ambos extremos inferiores están en el intervalo encajado $[l_N,u_N]$.

Los intervalos de bisección están encajados: cada intervalo posterior está contenido en todos los anteriores. Si $p,q\ge N$, los puntos $l_p$ y $l_q$ pertenecen a $[l_N,u_N]$. La distancia entre dos puntos de ese intervalo es a lo sumo su anchura, por lo que $|l_p-l_q|\le2^{-N}$. Para cualquier tolerancia escogemos un corte con $2^{-N}<\varepsilon$. El control vale para todos los pares, no sólo para extremos consecutivos.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-010-053}

¿Cómo se demuestra que los dos extremos tienen el mismo límite real?

[]{#MA-MSOL-ANM-01-010-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

$l_n$ converge por el criterio real y $u_n-l_n=2^{-n}\to0$; la regla de suma de C06 da a $u_n$ el mismo límite.

La estimación de pares demuestra que $l_n$ es de Cauchy; el criterio en $\mathbb R$ proporciona su límite $L$. Después escribimos $u_n=l_n+2^{-n}$. El segundo sumando tiende a cero, así que la regla de suma da $u_n\to L+0=L$. Hemos separado dos obligaciones: obtener primero la existencia de un destino y demostrar después que ambas fronteras se acercan a ese mismo destino.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-010-054}

¿Por qué el límite real construido cumple $L^2=2$?

[]{#MA-MSOL-ANM-01-010-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Las desigualdades $l_n^2<2<u_n^2$ pasan al límite mediante la regla del producto y conservación de orden, dando $L^2\le2\le L^2$.

Como $l_n,u_n\to L$, la regla del producto implica $l_n^2,u_n^2\to L^2$. El orden se conserva en el límite como desigualdad no estricta: de $l_n^2<2$ obtenemos $L^2\le2$, y de $2<u_n^2$ obtenemos $2\le L^2$. Ambas relaciones fuerzan la igualdad. La desigualdad estricta de los términos puede convertirse en igualdad precisamente porque las fronteras se aproximan al mismo punto.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-010-055}

¿Por qué la sucesión racional no converge en $\mathbb Q$?

[]{#MA-MSOL-ANM-01-010-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Un límite racional también sería límite real de su inclusión; unicidad lo igualaría a $L$, cuyo cuadrado es dos, contradiciendo la irracionalidad probada.

Supongamos que la sucesión racional tuviera límite $r\in\mathbb Q$. Al incluirla en los reales, la conservación de distancias muestra que también convergería a $\iota(r)$. Pero ya hemos probado que converge a $L$; la unicidad del límite real obliga a $\iota(r)=L$. Entonces $r^2=2$, contradiciendo la prueba de irracionalidad. La dificultad no es el comportamiento de las distancias, sino que el destino falta en el codominio racional.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-010-056}

¿Qué significa completitud secuencial para un subconjunto con distancia usual?

[]{#MA-MSOL-ANM-01-010-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

Que toda sucesión de Cauchy con valores en ese conjunto converge a un elemento del mismo conjunto. El lugar del destino es parte de la condición.

Para un subconjunto $E\subseteq\mathbb R$, no basta saber que toda sucesión de Cauchy con términos en $E$ converge en la recta real. Eso ya lo garantiza la completitud de $\mathbb R$. La condición adicional es que su límite pertenezca a $E$. Por ejemplo, $1/(n+1)$ tiene términos en $(0,1]$ y es de Cauchy, pero su límite cero queda fuera. Este ejemplo distingue la existencia de un límite ambiente de la completitud del subespacio.

</details>

### Ejercicios de la sección 10.7

#### Ejercicio 31. Tres pasos racionales

[]{#MA-EX-ANM-01-010-031}

Calcula los intervalos de bisección de §10.7 para $n=0,1,2,3$ y comprueba los cuadrados de sus extremos.

[]{#MA-SOL-ANM-01-010-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Los intervalos son $[1,2]$, $[1,3/2]$, $[5/4,3/2]$, $[11/8,3/2]$. Los puntos medios $3/2$, $5/4$, $11/8$ tienen cuadrados $9/4>2$, $25/16<2$, $121/64<2$, respectivamente. Así se elige cada mitad correcta, las anchuras son uno, medio, cuarto y octavo, y los extremos siguen encerrando el valor dos entre sus cuadrados.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 32. Cauchy racional sin raíz presupuesta

[]{#MA-EX-ANM-01-010-032}

Demuestra que los extremos inferiores de esa bisección son de Cauchy antes de construir su límite real.

[]{#MA-SOL-ANM-01-010-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Los intervalos están encajados y tienen anchura $2^{-N}$. Para $p,q\ge N$, los extremos inferiores posteriores pertenecen a $[l_N,u_N]$, luego su distancia es a lo sumo $2^{-N}$. Escoger por arquimedianidad $N$ con $2^{-N}<\varepsilon$ garantiza todos los pares. La existencia de una raíz real aún no se ha usado: sólo extremos racionales y anchuras conocidas.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 33. El destino no es racional

[]{#MA-EX-ANM-01-010-033}

Prueba que el límite real de los extremos inferiores tiene cuadrado dos y no puede ser límite en $\mathbb Q$.

[]{#MA-SOL-ANM-01-010-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

El criterio real proporciona $l_n\to L$, y $u_n-l_n=2^{-n}\to0$ da $u_n\to L$. Por regla de producto y orden, $l_n^2<2<u_n^2$ implica $L^2\le2\le L^2$. Si un racional reducido $s/t$ tuviera cuadrado dos, $s^2=2t^2$ obligaría a que $s$ y luego $t$ fueran pares, contradicción. Un límite racional de $l$ también sería un límite real y por unicidad igual a $L$, imposible.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 34. Un intervalo retiene el destino

[]{#MA-EX-ANM-01-010-034}

Prueba que toda sucesión de Cauchy con valores en $[A,B]$, con $A\le B$ reales, converge a un punto de ese mismo intervalo. Contrasta con $(0,1)$.

[]{#MA-SOL-ANM-01-010-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

El criterio real proporciona un límite $L$. Las cotas $A\le a_n\le B$ pasan al límite por C06, luego $A\le L\le B$. En $(0,1)$, la sucesión $1/(n+2)$ es de Cauchy y converge en $\mathbb R$ a cero, fuera del conjunto; unicidad impide otro destino interior. La pertenencia del límite al codominio no se sigue sólo de proximidad.

</details>

#### Ejercicio 35. Conjunto finito

[]{#MA-EX-ANM-01-010-035}

Demuestra que una sucesión con valores en un conjunto real finito no vacío es de Cauchy si y sólo si es eventualmente constante.

[]{#MA-SOL-ANM-01-010-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Si el conjunto tiene un único valor, la afirmación es inmediata. Si tiene varios, sea $\delta>0$ la mínima distancia entre dos valores distintos, existente por finitud. Cauchy con tolerancia $\delta$ fuerza que todos los términos posteriores sean iguales entre sí, pues distintos darían distancia al menos $\delta$. Así la cola es constante. Recíprocamente, una cola constante tiene todas sus distancias cero y prueba Cauchy.

</details>
## 10.8. Estimar el error antes de conocer la respuesta

[]{#MA-SEC-ANM-01-010-008}

Los saltos que tienden a cero no bastan. Los saltos dominados por una progresión geométrica sí permiten controlar cualquier acumulación finita de errores. Supongamos que $C\ge0$, $0<\rho<1$ y

$$
|a_{n+1}-a_n|\le C\rho^n\qquad(n\in\mathbb N).
$$

Si $p>q$, la identidad telescópica y la desigualdad triangular finita dan

$$
|a_p-a_q|\le C\sum_{j=q}^{p-1}\rho^j
=\frac{C\rho^q(1-\rho^{p-q})}{1-\rho}
\le\frac{C\rho^q}{1-\rho}.
$$

La identidad de suma finita se verifica multiplicando por $1-\rho$ y cancelando términos consecutivos. No usamos una suma infinita. Para comprobar $\rho^N\to0$ sin herramientas posteriores, escribamos $\rho^{-1}=1+t$ con $t>0$. Por inducción, $(1+t)^N\ge1+Nt$, luego $0<\rho^N\le1/(1+Nt)\to0$ por arquimedianidad. Si $C=0$, todos los saltos son cero y la sucesión es constante. Si $C>0$, recibida $\varepsilon>0$ podemos escoger $N$ con $C\rho^N/(1-\rho)<\varepsilon$. La estimación controla todo par posterior; por simetría incluye $p<q$ y el caso de igualdad tiene distancia cero. La sucesión es de Cauchy y tiene un límite real $L$.

También obtenemos un error verificable. Para $q$ fijo, hacemos tender $p$ a infinito en la cota anterior. Por C06, $|a_p-a_q|\to|L-a_q|$; la conservación del orden produce

$$
|L-a_q|\le\frac{C\rho^q}{1-\rho}.
$$

Si necesitamos error estrictamente menor que $\varepsilon$, escogemos $q$ con el lado derecho menor que $\varepsilon$. Existencia del límite y estimación del error son obligaciones distintas, ambas cerradas ahora. La cota puede ser conservadora; no afirmamos que sea el error exacto ni que el corte elegido sea mínimo.

**Una iteración real sin destino supuesto.** Sea $F:\mathbb R\to\mathbb R$ y supongamos que para algún $0<\rho<1$ se cumple $|F(x)-F(y)|\le\rho|x-y|$ para todos los reales $x,y$. Fijado $x_0$, definimos $x_{n+1}=F(x_n)$. La recursión existe porque $F$ es total en $\mathbb R$. Con $D=|x_1-x_0|$, una inducción da $|x_{n+1}-x_n|\le D\rho^n$. Por el resultado anterior $x_n\to L$ y $|L-x_n|\le D\rho^n/(1-\rho)$.

Debemos comprobar que el destino satisface la ecuación de la iteración. Para todo $n$,

$$
|F(L)-L|\le |F(L)-F(x_n)|+|x_{n+1}-L|
\le\rho|L-x_n|+|x_{n+1}-L|.
$$

El lado derecho tiende a cero, por lo que la distancia fija del izquierdo es cero y $F(L)=L$. Si $M$ fuera otro punto fijo, $|L-M|=|F(L)-F(M)|\le\rho|L-M|$, luego $(1-\rho)|L-M|\le0$ y $L=M$. Esta prueba no invoca continuidad general ni un teorema de espacios métricos: desarrolla la consecuencia de una desigualdad concreta sobre $\mathbb R$.

Por ejemplo, $F(x)=(x+3)/2$ satisface la condición con $\rho=1/2$. Desde cualquier valor inicial la iteración converge al único punto fijo, que al resolver $L=(L+3)/2$ resulta ser tres. Desde $x_0=0$, $D=3/2$ y la cota es $|L-x_n|\le3\,2^{-n}$. Aquí primero demostramos existencia y error y después identificamos el destino. La misma estrategia sirve cuando no hay una fórmula cómoda para los términos.

Quedan autorizados el criterio real de Cauchy, la negación por pares y el control de errores por acumulación geométrica finita. La arquitectura central ha sido proximidad interna, acotación, intervalos de cola y existencia por completitud. A partir de ella podemos estudiar nuevas sucesiones sin adivinar primero su límite.

![En esta iteración los saltos se reducen a la mitad y la cota de error $3\,2^{-n}$ coincide con el error exacto. Desde el índice cuatro el error es menor que un cuarto; el corte es suficiente y está justificado por la estimación.](../../assets/books/anm/C10/C10-F07.svg){#fig-anm-c10-f07 fig-alt="En esta iteración los saltos se reducen a la mitad y la cota de error $3\,2^{-n}$ coincide con el error exacto. Desde el índice cuatro el error es menor que un cuarto; el corte es suficiente y está justificado por la estimación."}

### Antes de seguir

#### Microcontrol 57

[]{#MA-MIC-ANM-01-010-057}

¿Qué controla una cota geométrica de saltos que no controla el mero salto tendiendo a cero?

[]{#MA-MSOL-ANM-01-010-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Controla uniformemente la acumulación de cualquier cantidad finita de saltos posteriores mediante una suma geométrica finita.

Saber que cada salto se hace pequeño no controla cuántos de esos saltos se acumulan entre dos índices lejanos. La cota geométrica permite sumar cualquier bloque: su longitud puede ser arbitrariamente grande, pero la suma queda por debajo de $C\rho^q/(1-\rho)$ cuando comienza en $q$. Esa cota depende del inicio del bloque y tiende a cero con él. Así produce exactamente el control uniforme sobre pares que exige Cauchy.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-010-058}

Escribe la cota de pares si $|a_{n+1}-a_n|\le C\rho^n$ con $0<\rho<1$.

[]{#MA-MSOL-ANM-01-010-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

Para $p>q$, $|a_p-a_q|\le C\rho^q/(1-\rho)$; por simetría se usa el índice menor para cualquier par.

Para $p>q$, telescopamos $a_p-a_q=\sum_{j=q}^{p-1}(a_{j+1}-a_j)$ y aplicamos la desigualdad triangular. Resulta
$$|a_p-a_q|\le C\sum_{j=q}^{p-1}\rho^j=C\rho^q\frac{1-\rho^{p-q}}{1-\rho}\le\frac{C\rho^q}{1-\rho}.$$
Sólo interviene una suma finita. Si los índices están en el otro orden, los intercambiamos; si coinciden, la distancia es cero. Para pares posteriores a $N$, el índice menor es al menos $N$.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-010-059}

¿Qué caso especial ocurre si $C=0$?

[]{#MA-MSOL-ANM-01-010-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Todos los saltos son cero, luego la sucesión es constante y de Cauchy con corte cero.

La cota se convierte en $|a_{n+1}-a_n|\le0$. Como un valor absoluto es no negativo, necesariamente $a_{n+1}=a_n$ para todo $n$. Por inducción todos los términos coinciden con $a_0$. La sucesión es constante, tiene distancias de pares iguales a cero y converge a su valor inicial. Separar este caso evita escoger cortes mediante fórmulas que podrían introducir innecesariamente una división por $C$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-010-060}

¿Cómo se justifica aquí que $\rho^N\to0$?

[]{#MA-MSOL-ANM-01-010-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

Escribir $\rho^{-1}=1+t$ con $t>0$ y usar $(1+t)^N\ge1+Nt$ por inducción; así $\rho^N\le1/(1+Nt)\to0$.

Como $0<\rho<1$, podemos poner $t=\rho^{-1}-1>0$. La desigualdad $(1+t)^N\ge1+Nt$ se prueba por inducción: multiplicar la cota del paso $N$ por $1+t$ añade además el término no negativo $Nt^2$. Invirtiendo cantidades positivas obtenemos $\rho^N\le1/(1+Nt)$. Para una tolerancia, la propiedad arquimediana permite hacer el denominador mayor que su recíproco. Eso prueba el límite y permite construir cortes en la estimación geométrica.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-010-061}

¿Qué cota de error al límite se obtiene?

[]{#MA-MSOL-ANM-01-010-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

$|L-a_q|\le C\rho^q/(1-\rho)$, dejando tender el otro índice a infinito en la cota de pares.

Fijemos $q$. La cota de pares vale para todo $p>q$ y su lado derecho ya no depende de $p$. Como $a_p\to L$, la continuidad del valor absoluto, expresada mediante la desigualdad triangular inversa, da $|a_p-a_q|\to|L-a_q|$. El orden pasa al límite y conserva la cota no estricta. Así obtenemos una estimación del error del término $a_q$ respecto del destino, usando sólo datos de los saltos.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-010-062}

¿Qué número inicia la estimación de saltos en una iteración contractiva?

[]{#MA-MSOL-ANM-01-010-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

$D=|x_1-x_0|$; la inducción da $|x_{n+1}-x_n|\le D\rho^n$.

Para $x_{n+1}=F(x_n)$ y una contracción de factor $\rho$, cada salto cumple $|x_{n+2}-x_{n+1}|\le\rho|x_{n+1}-x_n|$. El salto inicial es $D=|x_1-x_0|$, que corresponde al caso $n=0$. Si el salto de índice $n$ no supera $D\rho^n$, el siguiente no supera $D\rho^{n+1}$. La inducción convierte un dato inicial conocido en cotas de todos los saltos, antes de haber calculado el punto fijo.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-010-063}

¿Cómo se prueba $F(L)=L$ sin invocar continuidad general?

[]{#MA-MSOL-ANM-01-010-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

$|F(L)-L|\le\rho|L-x_n|+|x_{n+1}-L|\to0$, por lo que la distancia fija debe ser cero.

Una vez obtenido $x_n\to L$ en el dominio de $F$, la desigualdad de contracción proporciona $|F(L)-F(x_n)|\le\rho|L-x_n|$. Como $F(x_n)=x_{n+1}$, la desigualdad triangular da la cota indicada para $|F(L)-L|$. Sus dos sumandos tienden a cero. El lado izquierdo es una distancia fija; si fuera positiva, una cota menor que su mitad sería imposible. Por tanto $F(L)=L$, sin necesitar un teorema general de continuidad.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-010-064}

¿Qué garantiza unicidad de un punto fijo con factor $\rho<1$?

[]{#MA-MSOL-ANM-01-010-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Dos puntos fijos tendrían $|L-M|\le\rho|L-M|$; como $1-\rho>0$, su distancia sólo puede ser cero.

Si $F(L)=L$ y $F(M)=M$, la condición contractiva da $|L-M|=|F(L)-F(M)|\le\rho|L-M|$. Restando el segundo miembro resulta $(1-\rho)|L-M|\le0$. Ambos factores son no negativos y el primero es estrictamente positivo; en consecuencia $|L-M|=0$ y $L=M$. Aquí se ve por qué importa $\rho<1$: con factor uno, la identidad satisface la cota y puede tener muchos puntos fijos.

</details>

### Ejercicios de la sección 10.8

#### Ejercicio 36. Saltos geométricos

[]{#MA-EX-ANM-01-010-036}

Supón $|a_{n+1}-a_n|\le5\,2^{-n}$. Prueba existencia de límite y da un corte que asegure error menor que $\varepsilon$.

[]{#MA-SOL-ANM-01-010-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

La estimación de §10.8 con $C=5,\rho=1/2$ da $|a_p-a_q|\le10\,2^{-q}$ para $p>q$. Escoger $N$ con $10\,2^{-N}<\varepsilon$ garantiza Cauchy. Completitud real aporta $L$ y el paso al límite en el primer índice da $|L-a_n|\le10\,2^{-n}$. El mismo corte suficiente asegura error estricto al límite.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 37. Sumar antes de tomar un límite

[]{#MA-EX-ANM-01-010-037}

Prueba la identidad geométrica finita usada en §10.8 y explica por qué no presupone una serie convergente.

[]{#MA-SOL-ANM-01-010-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Para $p>q$, multiplicar $S=\rho^q+\cdots+\rho^{p-1}$ por $1-\rho$ deja $S-\rho S=\rho^q-\rho^p$ tras cancelar términos. Como $1-\rho\ne0$, $S=\rho^q(1-\rho^{p-q})/(1-\rho)$. Todas las operaciones son finitas; el control de pares y luego Cauchy construyen el límite de la sucesión, sin asignar valor a una suma infinita.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 38. Error exacto en una iteración

[]{#MA-EX-ANM-01-010-038}

Para $x_0=0$ y $x_{n+1}=(x_n+3)/2$, demuestra $x_n=3(1-2^{-n})$ y compara su error con la cota general.

[]{#MA-SOL-ANM-01-010-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

En cero la fórmula da cero. Si vale en $n$, entonces $(3(1-2^{-n})+3)/2=3(1-2^{-(n+1)})$, lo que cierra inducción. Su límite es tres y el error exacto $3\,2^{-n}$. La contracción tiene $\rho=1/2$ y $D=3/2$, por lo que la cota general $D\rho^n/(1-\rho)$ coincide aquí con el error exacto. No todas las iteraciones saturan esa cota.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 39. Iterar dentro de un intervalo

[]{#MA-EX-ANM-01-010-039}

Sea $F:[A,B]\to[A,B]$ con $A\le B$ y $|F(x)-F(y)|\le\rho|x-y|$, $0<\rho<1$. Prueba que desde cualquier $x_0\in[A,B]$ la iteración converge a un único punto fijo en ese intervalo.

[]{#MA-SOL-ANM-01-010-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

La imagen en el mismo intervalo permite definir todos los iterados por recursión. Con $D=|x_1-x_0|$, la inducción de §10.8 da saltos a lo sumo $D\rho^n$, por lo que es de Cauchy y converge en $\mathbb R$. Las cotas $A\le x_n\le B$ pasan al límite y retienen $L$ en el dominio de $F$. La desigualdad $|F(L)-L|\le\rho|L-x_n|+|x_{n+1}-L|$ prueba que es fijo. Dos puntos fijos cumplen distancia a lo sumo $\rho$ veces sí misma, luego coinciden. Si $A=B$, la iteración es constante y la conclusión sigue.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 40. La misma contracción con codominio incompleto

[]{#MA-EX-ANM-01-010-040}

En $X=\mathbb Q\cap[1,2]$, define $F(x)=(x+2/x)/2$. Prueba que $F:X\to X$ contrae distancias con factor $1/2$ pero no tiene punto fijo en $X$. Explica qué falla al trasladar el resultado anterior.

[]{#MA-SOL-ANM-01-010-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Es racional para todo racional no cero. Para $1\le x\le2$, $F(x)-1=(x^2-2x+2)/(2x)=((x-1)^2+1)/(2x)>0$ y $2-F(x)=(4x-x^2-2)/(2x)\ge1/(2x)>0$, pues $4x-x^2-2=2-(x-2)^2\ge1$ en ese intervalo. Así $F(x)\in X$. Además $|F(x)-F(y)|=|x-y|\,|1-2/(xy)|/2$. Como $1\le xy\le4$, $1/2\le2/(xy)\le2$ y el último factor absoluto es a lo sumo uno, dando contracción por $1/2$. Un punto fijo resolvería $x^2=2$, imposible en $\mathbb Q$. Los iterados son de Cauchy y convergen en $\mathbb R$; el centro real no tiene por qué pertenecer a $X$. Falta completitud del codominio, y por eso no se puede evaluar allí $F(L)$ como una función sobre $X$.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-10)

[← Capítulo 9](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html) · [Capítulo 11 →](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html)
