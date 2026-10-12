---
content-id: MA-BCH-0245
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-010-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 10
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C10_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Ejercicios](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §10.1 — Comparar términos sin nombrar un límite

### Microcontrol 001

[]{#MA-MIC-ANM-01-010-001}

[]{#MA-MSOL-ANM-01-010-001}

[]{#MA-SEC-ANM-01-010-001}

**Pregunta.** ¿Qué objetos compara la condición de Cauchy?

**Solución.** Compara dos términos $a_p,a_q$ de una misma cola mediante $|a_p-a_q|$, sin nombrar un candidato a límite.

Los índices $p$ y $q$ pueden elegirse independientemente: ambos deben estar después del mismo corte $N$. Así se comprueba que la cola entera se concentra, aunque todavía no sepamos alrededor de qué número. La diferencia entre los términos mide una separación en la recta de valores; la diferencia entre sus índices sólo mide separación temporal. La definición controla la primera y permite que la segunda sea arbitrariamente grande.

### Microcontrol 002

[]{#MA-MIC-ANM-01-010-002}

[]{#MA-MSOL-ANM-01-010-002}

**Pregunta.** ¿Puede el corte $N$ depender de los índices $p,q$?

**Solución.** No. Para cada tolerancia se escoge $N$ antes de los dos índices universales y debe servir para todos los pares posteriores.

Leamos la definición en su orden: se recibe $\varepsilon>0$, se encuentra un $N$, y después se consideran cualesquiera $p,q\ge N$. Por eso el corte puede adaptarse a la precisión, pero debe funcionar simultáneamente para todos esos pares. Elegir un corte después de conocer cada par permitiría excluir precisamente los términos difíciles; no demostraría que existe una cola con el control requerido.

### Microcontrol 003

[]{#MA-MIC-ANM-01-010-003}

[]{#MA-MSOL-ANM-01-010-003}

**Pregunta.** ¿Se permite $p=q$ en la definición?

**Solución.** Sí. La distancia es entonces cero y cumple toda tolerancia positiva.

Los cuantificadores no exigen que los índices sean distintos. Si elegimos el mismo índice dos veces, obtenemos $|a_p-a_p|=0<\varepsilon$, pues la tolerancia es positiva. Ese caso siempre cumple la estimación. Sin embargo, comprobar únicamente los pares iguales no sirve: quedan pendientes todos los pares de índices diferentes. Ésta es la diferencia entre verificar un caso permitido y verificar la condición universal.

### Microcontrol 004

[]{#MA-MIC-ANM-01-010-004}

[]{#MA-MSOL-ANM-01-010-004}

**Pregunta.** ¿Basta controlar pares de vecinos?

**Solución.** No. La definición exige todos los pares de una cola, incluso con separación temporal arbitrariamente grande.

Una sucesión puede avanzar mediante saltos pequeños y acumular una separación grande tras muchos pasos. Las sumas parciales armónicas de §10.5 lo muestran: sus saltos vecinos tienden a cero, pero hay pares arbitrariamente tardíos separados al menos por $1/2$. La condición de Cauchy obliga a controlar también esos pares. Por eso un gráfico que muestre sólo diferencias entre vecinos puede sugerir estabilización sin demostrarla.

### Microcontrol 005

[]{#MA-MIC-ANM-01-010-005}

[]{#MA-MSOL-ANM-01-010-005}

**Pregunta.** Da un corte suficiente de Cauchy para $a_n=1/(n+1)$.

**Solución.** Para $\varepsilon>0$ sirve cualquier natural $N$ con $N+1>1/\varepsilon$, pues las distancias posteriores son a lo sumo $1/(N+1)<\varepsilon$.

Si $p,q\ge N$, ambos términos son positivos y no superan $1/(N+1)$. La distancia entre dos números de ese intervalo no supera su longitud, de modo que $|a_p-a_q|\le1/(N+1)$. Buscamos entonces que esta cota sea estrictamente menor que $\varepsilon$, lo que equivale a $N+1>1/\varepsilon$. La propiedad arquimediana garantiza un natural con esa propiedad. Una vez escogido, sirve para cualquier par posterior.

### Microcontrol 006

[]{#MA-MIC-ANM-01-010-006}

[]{#MA-MSOL-ANM-01-010-006}

**Pregunta.** ¿Qué corte sirve para una sucesión constante?

**Solución.** $N=0$ para toda tolerancia, porque todas sus distancias son cero.

Si $a_n=c$ para todo $n$, entonces, cualesquiera que sean $p$ y $q$, tenemos $|a_p-a_q|=|c-c|=0$. Esta cantidad es menor que toda tolerancia positiva. Como no hay términos excepcionales al comienzo, no necesitamos descartar un prefijo: el corte inicial $N=0$ basta. El ejemplo también muestra que Cauchy no exige valores distintos ni un desplazamiento continuo de los términos.

### Microcontrol 007

[]{#MA-MIC-ANM-01-010-007}

[]{#MA-MSOL-ANM-01-010-007}

**Pregunta.** ¿La condición de Cauchy exige monotonía?

**Solución.** No. Por ejemplo, $(-1)^n/(n+1)$ es de Cauchy y alterna de signo.

Para comprobar el ejemplo sin depender de un dibujo, dados $p,q\ge N$ usamos
$$
\left|\frac{(-1)^p}{p+1}-\frac{(-1)^q}{q+1}\right|
\le\frac1{p+1}+\frac1{q+1}\le\frac2{N+1}.
$$
Escogemos $N+1>2/\varepsilon$. El error entre cualquier par queda por debajo de $\varepsilon$, aunque los términos cambien de signo. La concentración de una cola depende del tamaño de las separaciones, no de que todos los términos avancen en una misma dirección.

### Microcontrol 008

[]{#MA-MIC-ANM-01-010-008}

[]{#MA-MSOL-ANM-01-010-008}

**Pregunta.** ¿La definición por sí sola proporciona un algoritmo para calcular los cortes?

**Solución.** No. Afirma existencia para cada tolerancia. Una regla efectiva de cortes requiere información adicional sobre la sucesión.

El enunciado tiene la forma «para cada precisión existe un corte». Eso no describe cómo obtenerlo a partir de datos finitos, ni establece cuánto tiempo llevaría encontrarlo. En ejemplos con una fórmula explícita de error, podemos construir cortes mediante desigualdades. Para una sucesión dada abstractamente, esa información puede faltar. Conviene distinguir la existencia matemática del testigo de un procedimiento efectivo que lo calcule.

## §10.2 — Del destino común al control interno

### Microcontrol 009

[]{#MA-MIC-ANM-01-010-009}

[]{#MA-MSOL-ANM-01-010-009}

[]{#MA-SEC-ANM-01-010-002}

**Pregunta.** ¿Qué tolerancia de convergencia se usa para probar Cauchy con tolerancia $\varepsilon$?

**Solución.** $\varepsilon/2$; así los dos errores respecto del límite suman menos que $\varepsilon$.

Queremos controlar una distancia entre dos términos, pero la convergencia controla cada término respecto de $L$. Introducimos ese centro como punto intermedio y repartimos el presupuesto de error en dos partes. Si ambas distancias a $L$ son menores que $\varepsilon/2$, su suma es menor que $\varepsilon$. Usar directamente $\varepsilon$ en cada una sólo garantizaría una suma menor que $2\varepsilon$, insuficiente para el objetivo fijado.

### Microcontrol 010

[]{#MA-MIC-ANM-01-010-010}

[]{#MA-MSOL-ANM-01-010-010}

**Pregunta.** Escribe la desigualdad triangular que une $a_p,a_q$ con el límite $L$.

**Solución.** $|a_p-a_q|\le|a_p-L|+|a_q-L|$.

Escribimos $a_p-a_q=(a_p-L)+(L-a_q)$ y aplicamos $|u+v|\le|u|+|v|$. Como $|L-a_q|=|a_q-L|$, aparece exactamente la desigualdad indicada. Geométricamente, el recorrido de $a_p$ a $a_q$ pasando por $L$ no puede ser más corto que la separación directa. La utilidad del paso es que transforma una distancia desconocida entre términos en dos errores que la convergencia ya permite controlar.

### Microcontrol 011

[]{#MA-MIC-ANM-01-010-011}

[]{#MA-MSOL-ANM-01-010-011}

**Pregunta.** ¿Por qué el mismo corte controla ambos errores?

**Solución.** Porque la convergencia con tolerancia $\varepsilon/2$ vale para todo índice posterior, incluidos $p$ y $q$.

La definición de convergencia entrega un único corte $N$ tal que $|a_n-L|<\varepsilon/2$ para todo $n\ge N$. Al tomar $p,q\ge N$, aplicamos esa misma afirmación primero con $n=p$ y después con $n=q$. No estamos escogiendo cortes nuevos para esos índices. La universalidad sobre toda la cola permite sumar los dos controles y obtener $|a_p-a_q|<\varepsilon$.

### Microcontrol 012

[]{#MA-MIC-ANM-01-010-012}

[]{#MA-MSOL-ANM-01-010-012}

**Pregunta.** ¿Interviene completitud en convergente implica Cauchy?

**Solución.** No. El límite ya existe por hipótesis; se usa su definición y la desigualdad triangular.

Completitud serviría para garantizar la existencia de un límite cuando aún no lo tenemos. En esta dirección, la hipótesis ya afirma que existe $L$ y que la sucesión converge a él. Basta elegir el corte para $\varepsilon/2$ y aplicar la desigualdad triangular. El argumento funciona también en cualquier espacio métrico, completo o incompleto, siempre que la sucesión considerada tenga un límite dentro de ese espacio.

### Microcontrol 013

[]{#MA-MIC-ANM-01-010-013}

[]{#MA-MSOL-ANM-01-010-013}

**Pregunta.** ¿Qué distancia máxima garantiza por estimación una ventana abierta de radio $r$?

**Solución.** Distancia menor que $2r$ entre cualesquiera dos términos en esa ventana; el diámetro se distingue del radio.

Si $x$ e $y$ pertenecen a $(L-r,L+r)$, entonces $|x-L|<r$ y $|y-L|<r$. La desigualdad triangular da $|x-y|\le|x-L|+|y-L|<2r$. No se obtiene en general una cota $r$: los puntos $L-3r/4$ y $L+3r/4$ están dentro de la ventana y distan $3r/2$. El radio mide distancia al centro; entre dos puntos puede intervenir casi todo el ancho.

### Microcontrol 014

[]{#MA-MIC-ANM-01-010-014}

[]{#MA-MSOL-ANM-01-010-014}

**Pregunta.** Da un corte directo para $a_n=(-1)^n/(n+1)$ con tolerancia $\varepsilon$.

**Solución.** Sirve cualquier $N$ con $N+1>2/\varepsilon$, pues $|a_p-a_q|\le2/(N+1)<\varepsilon$ para $p,q\ge N$.

Aplicamos la desigualdad triangular a la diferencia de los dos términos. Los signos desaparecen al tomar valores absolutos y obtenemos $|a_p-a_q|\le1/(p+1)+1/(q+1)$. Como ambos índices superan el mismo corte, cada sumando es a lo sumo $1/(N+1)$. La condición $N+1>2/\varepsilon$ hace que la suma sea menor que la tolerancia solicitada. No hace falta separar los casos de paridad.

### Microcontrol 015

[]{#MA-MIC-ANM-01-010-015}

[]{#MA-MSOL-ANM-01-010-015}

**Pregunta.** ¿Tener signos alternantes contradice convergencia?

**Solución.** No. La magnitud $1/(n+1)$ puede tender a cero; entonces la alternancia amortiguada converge y es de Cauchy.

Para el ejemplo $a_n=(-1)^n/(n+1)$, la distancia al candidato cero es $|a_n|=1/(n+1)$. Recibida $\varepsilon>0$, escogemos $N+1>1/\varepsilon$; entonces todos los índices $n\ge N$ cumplen $|a_n|<\varepsilon$. El signo indica de qué lado se aproxima un término, pero la definición exige cercanía en ambos lados. Alternar no impide converger cuando la magnitud de la oscilación se reduce.

### Microcontrol 016

[]{#MA-MIC-ANM-01-010-016}

[]{#MA-MSOL-ANM-01-010-016}

**Pregunta.** ¿La implicación ya demostrada permite concluir Cauchy implica convergente?

**Solución.** Todavía no en esta fase lógica: la recíproca exige construir un destino usando completitud, como se hará en §10.4.

Una implicación no autoriza su recíproca. Haber probado que todo límite produce control de Cauchy no construye un límite para cualquier sucesión que tenga ese control. Precisamente ése será el trabajo posterior: encerrar las colas y usar la propiedad del supremo para obtener un candidato real. El codominio importa; en $\mathbb Q$ hay sucesiones de Cauchy cuyo destino sólo existe al pasar a $\mathbb R$.

## §10.3 — Encerrar una cola y recuperar la acotación

### Microcontrol 017

[]{#MA-MIC-ANM-01-010-017}

[]{#MA-MSOL-ANM-01-010-017}

[]{#MA-SEC-ANM-01-010-003}

**Pregunta.** ¿Qué tolerancia fija basta para recuperar acotación de una sucesión de Cauchy?

**Solución.** La tolerancia uno proporciona una cola próxima al término de su corte.

La condición de Cauchy responde a cualquier tolerancia, así que podemos usar la precisión particular $1$. Obtenemos $N_0$ con $|a_p-a_q|<1$ para todos $p,q\ge N_0$. Al fijar $q=N_0$, todos los términos de esa cola quedan en la ventana $(a_{N_0}-1,a_{N_0}+1)$. Eso ya proporciona una cota para la cola; después sólo habrá que incorporar los finitos términos anteriores.

### Microcontrol 018

[]{#MA-MIC-ANM-01-010-018}

[]{#MA-MSOL-ANM-01-010-018}

**Pregunta.** ¿Qué término se toma como ancla de la cola?

**Solución.** $a_{N_0}$, donde $N_0$ es el corte de Cauchy para tolerancia uno.

El término $a_{N_0}$ pertenece a la cola que controla el corte $N_0$. Por ello es lícito sustituir uno de los dos índices universales por $N_0$. Para cualquier $n\ge N_0$ resulta $|a_n-a_{N_0}|<1$. No podríamos utilizar de la misma manera un término situado antes del corte: la definición no garantiza distancias entre esa entrada temprana y las entradas de la cola.

### Microcontrol 019

[]{#MA-MIC-ANM-01-010-019}

[]{#MA-MSOL-ANM-01-010-019}

**Pregunta.** ¿Qué cota de $|a_n|$ se obtiene para $n\ge N_0$?

**Solución.** $|a_n|<|a_{N_0}|+1$, por $|a_n-a_{N_0}|<1$ y desigualdad triangular.

Separamos el término como $a_n=(a_n-a_{N_0})+a_{N_0}$. Por la desigualdad triangular,
$$|a_n|\le|a_n-a_{N_0}|+|a_{N_0}|<1+|a_{N_0}|.$$
La cantidad de la derecha es fija: depende del ancla elegida, pero ya no del índice $n$. Esa independencia es lo que permite usarla como cota de toda la cola. La misma estimación no se ha probado todavía para el prefijo anterior.

### Microcontrol 020

[]{#MA-MIC-ANM-01-010-020}

[]{#MA-MSOL-ANM-01-010-020}

**Pregunta.** ¿Cómo se trata el prefijo si $N_0=0$?

**Solución.** No hay prefijo anterior que controlar; $|a_0|+1$ acota ya todos los términos y no se toma un máximo vacío.

Con nuestra convención, los índices naturales comienzan en cero. Si $N_0=0$, no existe ningún índice natural $n<N_0$, así que el prefijo que normalmente se controla por finitud está vacío. La cota de cola ya vale para toda la sucesión. Escribir un máximo de los términos del prefijo vacío introduciría una expresión sin definir; en este caso se omite ese paso y se conserva la cota $|a_0|+1$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-010-021}

[]{#MA-MSOL-ANM-01-010-021}

**Pregunta.** ¿Acotada implica Cauchy?

**Solución.** No. $(-1)^n$ es acotada y tiene pares posteriores separados por dos después de cualquier corte.

Tomemos $a_n=(-1)^n$. Todos sus términos tienen valor absoluto uno, por lo que es acotada. Sin embargo, para cualquier corte $N$, elegimos $p=2N$ y $q=2N+1$: ambos son posteriores al corte y $|a_p-a_q|=|1-(-1)|=2$. Con la tolerancia fija $\varepsilon_0=1$, ningún corte controla todos los pares. Acotación encierra la sucesión en una región fija; Cauchy exige regiones cada vez más estrechas.

### Microcontrol 022

[]{#MA-MIC-ANM-01-010-022}

[]{#MA-MSOL-ANM-01-010-022}

**Pregunta.** ¿Por qué existen los extremos reales de $T_N$?

**Solución.** $T_N$ contiene $a_N$ y es acotado; completitud garantiza su supremo e ínfimo reales.

El conjunto $T_N=\{a_n:n\ge N\}$ no es vacío, pues contiene el término de índice $N$. La acotación de la sucesión proporciona cotas superiores e inferiores de ese conjunto. La completitud de $\mathbb R$ permite definir $u_N=\sup T_N$ y $\ell_N=\inf T_N$. No se afirma que esos extremos sean términos de la sucesión: supremo e ínfimo pueden existir sin alcanzarse.

### Microcontrol 023

[]{#MA-MIC-ANM-01-010-023}

[]{#MA-MSOL-ANM-01-010-023}

**Pregunta.** Si todas las distancias de una cola son menores que $\eta$, ¿qué cota se obtiene para su anchura?

**Solución.** $0\le u_N-\ell_N\le\eta$. Al tomar extremos puede perderse la desigualdad estricta.

Fijemos $b\in T_N$. Para cada $a\in T_N$, $|a-b|<\eta$ implica $a<b+\eta$, así que $b+\eta$ es una cota superior y $u_N\le b+\eta$. Esto vale para todos los $b$, luego $u_N-\eta$ es cota inferior de $T_N$ y $u_N-\eta\le\ell_N$. Obtenemos $u_N-\ell_N\le\eta$. La no negatividad sigue de $\ell_N\le u_N$. Al tomar extremos, las cotas pueden quedar en la frontera aunque cada par efectivo tenga distancia estrictamente menor.

### Microcontrol 024

[]{#MA-MIC-ANM-01-010-024}

[]{#MA-MSOL-ANM-01-010-024}

**Pregunta.** ¿Qué tolerancia de Cauchy garantiza anchura estrictamente menor que $\varepsilon$ por esa cota?

**Solución.** Usar $\eta=\varepsilon/2$ da anchura a lo sumo $\varepsilon/2$, y por tanto menor que $\varepsilon$.

La estimación de anchura entrega una desigualdad no estricta. Si pidiéramos Cauchy sólo con $\eta=\varepsilon$, podríamos concluir $u_N-\ell_N\le\varepsilon$, pero no necesariamente una anchura menor que $\varepsilon$. Reservamos un margen: con $\eta=\varepsilon/2$ obtenemos $u_N-\ell_N\le\varepsilon/2<\varepsilon$. La última desigualdad es estricta porque la tolerancia original es positiva. Esta reserva evita perder precisión al pasar de términos a extremos.

## §10.4 — La completitud construye el destino

### Microcontrol 025

[]{#MA-MIC-ANM-01-010-025}

[]{#MA-MSOL-ANM-01-010-025}

[]{#MA-SEC-ANM-01-010-004}

**Pregunta.** ¿Cómo se define el candidato $L$ de la prueba principal?

**Solución.** $L=\sup\{\ell_N:N\in\mathbb N\}$, que existe por completitud porque el conjunto es no vacío y acotado superiormente.

El conjunto de extremos inferiores contiene $\ell_0$, así que no es vacío. Además, cada $\ell_N$ queda por debajo de $u_0$: basta tomar un término perteneciente a las dos colas para comparar ambos extremos. Por completitud existe su supremo $L$. Esta elección toma la barrera inferior más alta que imponen las colas. Luego se comprobará que ningún extremo superior queda por debajo de ella y que la anchura de las colas fuerza la convergencia.

### Microcontrol 026

[]{#MA-MIC-ANM-01-010-026}

[]{#MA-MSOL-ANM-01-010-026}

**Pregunta.** ¿Qué término compara $\ell_M$ con $u_N$ cuando los cortes son distintos?

**Solución.** $a_r$ con $r=\max\{M,N\}$ pertenece a ambas colas y da $\ell_M\le a_r\le u_N$.

Al elegir $r=\max\{M,N\}$ garantizamos simultáneamente $r\ge M$ y $r\ge N$. Por la primera desigualdad, $a_r\in T_M$ y $\ell_M\le a_r$; por la segunda, $a_r\in T_N$ y $a_r\le u_N$. Encadenando ambas relaciones obtenemos la comparación buscada. Usar sólo $a_M$ o sólo $a_N$ podría situar el término antes de uno de los cortes y dejar sin justificar una mitad del argumento.

### Microcontrol 027

[]{#MA-MIC-ANM-01-010-027}

[]{#MA-MSOL-ANM-01-010-027}

**Pregunta.** ¿Por qué $L\le u_N$ para cada $N$?

**Solución.** $u_N$ acota todos los $\ell_M$ por la comparación entre cortes, y el supremo $L$ es la menor cota superior de ese conjunto.

Fijemos $N$. La comparación anterior muestra que $\ell_M\le u_N$ para todo $M$, incluso cuando $M$ es anterior o posterior a $N$. Por tanto, $u_N$ es cota superior de todo el conjunto cuyo supremo define $L$. Como el supremo es la menor cota superior, $L\le u_N$. A la vez, $\ell_N\le L$ porque $\ell_N$ pertenece a ese conjunto. Así $L\in[\ell_N,u_N]$ para cada corte.

### Microcontrol 028

[]{#MA-MIC-ANM-01-010-028}

[]{#MA-MSOL-ANM-01-010-028}

**Pregunta.** ¿Dónde interviene completitud además de la existencia de extremos de cola?

**Solución.** En la existencia del supremo de los extremos inferiores, que construye el centro real común a todos los intervalos.

Hay dos usos de existencia distintos. Primero, cada cola acotada tiene sus propios extremos $\ell_N,u_N$. Después, el conjunto de todos los extremos inferiores tiene un supremo $L$. Este segundo paso reúne los encierros sucesivos en un candidato único que no cambia al pedir otra tolerancia. Sin él sólo tendríamos intervalos cada vez más estrechos, pero todavía no un punto del codominio cuya existencia y convergencia hubiéramos demostrado.

### Microcontrol 029

[]{#MA-MIC-ANM-01-010-029}

[]{#MA-MSOL-ANM-01-010-029}

**Pregunta.** ¿Por qué $|a_n-L|$ queda acotada por la anchura para $n\ge N$?

**Solución.** Tanto $a_n$ como $L$ pertenecen a $[\ell_N,u_N]$, por lo que su distancia es a lo sumo $u_N-\ell_N$.

Si $x,y\in[\ell_N,u_N]$, entonces $x-y\le u_N-\ell_N$ y $y-x\le u_N-\ell_N$. Esas dos desigualdades equivalen a $|x-y|\le u_N-\ell_N$. Aplicamos esto con $x=a_n$ e $y=L$. Ahora Cauchy permite escoger un corte cuya anchura sea menor que cualquier tolerancia dada. La distancia a $L$ queda controlada por esa anchura para todos los índices posteriores, que es exactamente la convergencia.

### Microcontrol 030

[]{#MA-MIC-ANM-01-010-030}

[]{#MA-MSOL-ANM-01-010-030}

**Pregunta.** ¿Qué prueba la unicidad del real común a todos los intervalos?

**Solución.** Dos supuestos centros tendrían distancia menor que cualquier tolerancia por el ancho pequeño; una distancia positiva contradice usar su mitad como tolerancia.

Supongamos que $L$ y $M$ pertenecen a todos los encierros y que $d=|L-M|>0$. Las anchuras pueden hacerse menores que $d/2$. Elegimos un corte con esa propiedad; como ambos puntos están en su intervalo, $d\le u_N-\ell_N<d/2$, contradicción. Por tanto $d=0$ y los puntos coinciden. El argumento usa una distancia fija entre los supuestos candidatos y una tolerancia escogida para contradecirla.

### Microcontrol 031

[]{#MA-MIC-ANM-01-010-031}

[]{#MA-MSOL-ANM-01-010-031}

**Pregunta.** ¿Necesita la prueba principal Bolzano–Weierstrass?

**Solución.** No. Construye $L$ mediante supremo y verifica convergencia directamente con los intervalos de cola y Cauchy.

La estrategia no extrae una subsucesión convergente. Obtiene los extremos de todas las colas, define $L$ como supremo de los inferiores y demuestra que $L$ está en cada encierro. Después usa la anchura pequeña para controlar $|a_n-L|$ en toda la cola. Así la prueba depende directamente de la completitud expresada mediante supremos. Bolzano–Weierstrass permitiría otra vía, pero no es necesario para cerrar ésta.

### Microcontrol 032

[]{#MA-MIC-ANM-01-010-032}

[]{#MA-MSOL-ANM-01-010-032}

**Pregunta.** Enuncia el criterio de Cauchy con su codominio.

**Solución.** Una sucesión $a:\mathbb N\to\mathbb R$ converge a algún real si y sólo si es de Cauchy para la distancia usual.

La dirección «converge $\Rightarrow$ Cauchy» usa el límite ya existente y la desigualdad triangular. La dirección «Cauchy $\Rightarrow$ converge» construye ese límite mediante completitud. Debemos escribir el codominio porque la conclusión afirma la existencia de un destino dentro de él. La misma afirmación con $\mathbb Q$ sería falsa: la bisección que aproxima un número de cuadrado dos produce una sucesión racional de Cauchy sin límite racional.

## §10.5 — Negar Cauchy: encontrar pares separados

### Microcontrol 033

[]{#MA-MIC-ANM-01-010-033}

[]{#MA-MSOL-ANM-01-010-033}

[]{#MA-SEC-ANM-01-010-005}

**Pregunta.** ¿Qué orden de cuantificadores expresa no ser de Cauchy?

**Solución.** Existe $\varepsilon_0>0$ tal que para todo corte $N$ existen $p,q\ge N$ con $|a_p-a_q|\ge\varepsilon_0$.

La definición es $\forall\varepsilon>0\;\exists N\;\forall p,q\ge N:\ |a_p-a_q|<\varepsilon$. Al negarla, cada cuantificador cambia: existe una tolerancia para la cual ningún corte funciona, y después de cada corte aparece algún par infractor. La pertenencia de ambos índices a la cola debe mantenerse junto con la infracción. No basta presentar un único par temprano; hay que producir pares posteriores a cualquier corte que se proponga.

### Microcontrol 034

[]{#MA-MIC-ANM-01-010-034}

[]{#MA-MSOL-ANM-01-010-034}

**Pregunta.** ¿Puede la tolerancia de la negación cambiar con $N$?

**Solución.** No. Debe quedar fija antes de considerar cualquier corte; los índices testigo sí pueden depender de $N$.

Para refutar Cauchy debemos encontrar una precisión fija que siga fallando, por mucho que avancemos. Si permitiéramos que $\varepsilon_0$ disminuyera después de recibir cada $N$, estaríamos cambiando el desafío y podríamos confundir una sucesión que se concentra con otra que no lo hace. En cambio, los índices del par infractor se eligen después del corte: su función es mostrar que aquella precisión fija todavía falla en esa cola.

### Microcontrol 035

[]{#MA-MIC-ANM-01-010-035}

[]{#MA-MSOL-ANM-01-010-035}

**Pregunta.** ¿Por qué la negación usa $\ge$ y no sólo $>$?

**Solución.** Porque se niega una desigualdad estricta $|a_p-a_q|<\varepsilon_0$; la igualdad también hace fallar la condición.

La negación de $d<\varepsilon_0$ es $d\ge\varepsilon_0$, porque el caso de igualdad también queda fuera del intervalo permitido. Por ejemplo, en $a_n=n$ los pares vecinos tienen distancia exactamente uno. Esa igualdad basta para hacer fallar la tolerancia $\varepsilon_0=1$. Si exigiéramos sólo distancias mayores que uno, estaríamos descartando testigos legítimos y no habríamos escrito la negación lógica exacta.

### Microcontrol 036

[]{#MA-MIC-ANM-01-010-036}

[]{#MA-MSOL-ANM-01-010-036}

**Pregunta.** Da testigos para negar Cauchy en $a_n=n$.

**Solución.** Con $\varepsilon_0=1$ y cualquier corte $N$, tomar $p=N,q=N+1$ da distancia uno.

Fijamos primero $\varepsilon_0=1$. Cuando se propone un corte arbitrario $N$, respondemos con $p=N$ y $q=N+1$, que satisfacen las dos condiciones de pertenencia a la cola. Como $a_p=p$ y $a_q=q$, resulta $|a_p-a_q|=|N-(N+1)|=1\ge\varepsilon_0$. La construcción funciona para todo $N$ con la misma tolerancia. Esto verifica todos los cuantificadores de la negación, no sólo un ejemplo de separación.

### Microcontrol 037

[]{#MA-MIC-ANM-01-010-037}

[]{#MA-MSOL-ANM-01-010-037}

**Pregunta.** ¿Qué ocurre con $|a_{n+1}-a_n|$ si $a$ es de Cauchy?

**Solución.** Tiende a cero: para cada tolerancia, el corte de Cauchy controla todos los pares vecinos posteriores.

Sea $\varepsilon>0$. Cauchy entrega un corte $N$ que controla cualquier par de índices posteriores. Para todo $n\ge N$, los dos índices $n$ y $n+1$ cumplen esa condición, luego $|a_{n+1}-a_n|<\varepsilon$. Como el salto es no negativo, esta desigualdad prueba que converge a cero. La recíproca no está contenida en el argumento: controlar vecinos no controla automáticamente la acumulación de muchos saltos.

### Microcontrol 038

[]{#MA-MIC-ANM-01-010-038}

[]{#MA-MSOL-ANM-01-010-038}

**Pregunta.** ¿Cuál es el salto de $h_n=\sum_{j=1}^{n+1}1/j$?

**Solución.** $h_{n+1}-h_n=1/(n+2)$, que tiende a cero por arquimedianidad.

Al restar las dos sumas finitas, se cancelan los términos desde $1$ hasta $1/(n+1)$ y sólo queda el término nuevo $1/(n+2)$. Para demostrar que tiende a cero, dados $\varepsilon>0$ escogemos $N$ con $N+2>1/\varepsilon$. Si $n\ge N$, entonces $0<1/(n+2)\le1/(N+2)<\varepsilon$. La cancelación explica la fórmula y la elección del corte demuestra el límite, sin invocar una suma infinita.

### Microcontrol 039

[]{#MA-MIC-ANM-01-010-039}

[]{#MA-MSOL-ANM-01-010-039}

**Pregunta.** ¿Qué pares de índices muestran que $h$ no es de Cauchy?

**Solución.** Para $m\ge1$, los índices $m-1$ y $2m-1$ tienen distancia al menos $1/2$. Dado $N$, elegir $m=N+1$ los deja ambos posteriores al corte.

La diferencia correspondiente es
$$h_{2m-1}-h_{m-1}=\sum_{j=m+1}^{2m}\frac1j.$$
Hay $m$ sumandos y cada uno es al menos $1/(2m)$; por tanto la suma es al menos $1/2$. Fijamos esa tolerancia y, recibido $N$, tomamos $m=N+1$. Los índices son entonces $N$ y $2N+1$, ambos posteriores. Este bloque finito conserva una separación fija aunque cada salto vecino sea cada vez menor.

### Microcontrol 040

[]{#MA-MIC-ANM-01-010-040}

[]{#MA-MSOL-ANM-01-010-040}

**Pregunta.** ¿El contraejemplo de $h$ necesita una suma infinita?

**Solución.** No. Todos los términos y diferencias usados son sumas finitas; la separación de bloques basta para negar Cauchy.

Para cada índice $n$, $h_n$ está definido por una suma finita. También la diferencia entre dos términos es una suma finita sobre un bloque de índices. La negación de Cauchy se acredita estimando ese bloque desde abajo por $1/2$. No necesitamos decidir el valor de una serie infinita ni afirmar previamente su divergencia. El contraejemplo queda establecido por pares explícitos que sobreviven después de cualquier corte.

## §10.6 — Conservar el control al operar

### Microcontrol 041

[]{#MA-MIC-ANM-01-010-041}

[]{#MA-MSOL-ANM-01-010-041}

[]{#MA-SEC-ANM-01-010-006}

**Pregunta.** ¿Qué corte sirve para probar que la suma de dos sucesiones de Cauchy es de Cauchy?

**Solución.** El máximo de sus cortes para tolerancia $\varepsilon/2$; las dos diferencias de sumandos dan una distancia total menor que $\varepsilon$.

Sean $a$ y $b$ las dos sucesiones. Elegimos cortes $N_a,N_b$ para la precisión $\varepsilon/2$ y tomamos $N=\max\{N_a,N_b\}$. Si $p,q\ge N$, ambos controles valen y
$$|(a_p+b_p)-(a_q+b_q)|\le|a_p-a_q|+|b_p-b_q|<\varepsilon.$$
El máximo sincroniza las colas; la desigualdad triangular reúne los errores. Así obtenemos un solo corte que funciona para todos los pares de la suma.

### Microcontrol 042

[]{#MA-MIC-ANM-01-010-042}

[]{#MA-MSOL-ANM-01-010-042}

**Pregunta.** ¿Qué sucede al multiplicar por cero?

**Solución.** La sucesión resultante es constante cero y es de Cauchy con corte cero; no se divide por el escalar.

Para el escalar cero, los términos son $0a_n=0$ cualquiera que sea la sucesión original. La distancia entre dos términos resultantes es cero y el corte inicial sirve para toda tolerancia. Este caso debe separarse de la regla para un escalar $c\ne0$, que escoge la precisión $\varepsilon/|c|$ en la sucesión original. Escribir esa división cuando $c=0$ introduciría una cantidad no definida.

### Microcontrol 043

[]{#MA-MIC-ANM-01-010-043}

[]{#MA-MSOL-ANM-01-010-043}

**Pregunta.** ¿Por qué el argumento del producto necesita acotación?

**Solución.** Porque la diferencia del producto contiene factores $|a_p|$ y $|b_q|$ multiplicando las diferencias; cotas globales los controlan.

La identidad útil es $a_pb_p-a_qb_q=a_p(b_p-b_q)+b_q(a_p-a_q)$. Al tomar valor absoluto aparecen los factores $|a_p|$ y $|b_q|$. Las diferencias pequeñas no bastarían si esos factores pudieran crecer sin control. Como las sucesiones de Cauchy son acotadas, elegimos cotas globales $A,B$ y obtenemos $|a_pb_p-a_qb_q|\le A|b_p-b_q|+B|a_p-a_q|$. Ahora sí podemos repartir una tolerancia final entre dos errores controlables.

### Microcontrol 044

[]{#MA-MIC-ANM-01-010-044}

[]{#MA-MSOL-ANM-01-010-044}

**Pregunta.** ¿Por qué se usan denominadores $A+1$ y $B+1$ al escoger tolerancias para el producto?

**Solución.** Para mantenerlos positivos incluso si una cota es cero y obtener una estimación estrictamente menor que la tolerancia final.

Si $|a_n|\le A$ y $|b_n|\le B$, pedimos $|b_p-b_q|<\varepsilon/(2(A+1))$ y $|a_p-a_q|<\varepsilon/(2(B+1))$. El máximo de los cortes garantiza ambas condiciones. La cota del producto resulta menor que
$$\frac\varepsilon2\frac A{A+1}+\frac\varepsilon2\frac B{B+1}<\varepsilon.$$
Los denominadores son positivos incluso si una cota vale cero. La elección evita dividir por cero y deja un margen respecto de la tolerancia final.

### Microcontrol 045

[]{#MA-MIC-ANM-01-010-045}

[]{#MA-MSOL-ANM-01-010-045}

**Pregunta.** ¿Qué hipótesis de una cola permite controlar recíprocos?

**Solución.** $|a_n|\ge c>0$ desde algún corte; entonces la diferencia de recíprocos es a lo sumo $|a_p-a_q|/c^2$.

Sobre esa cola los términos no son cero, así que podemos escribir
$$\left|\frac1{a_p}-\frac1{a_q}\right|=\frac{|a_p-a_q|}{|a_pa_q|}\le\frac{|a_p-a_q|}{c^2}.$$
Recibida $\varepsilon>0$, pedimos a $a$ la precisión $\varepsilon c^2$. Tomamos el máximo de su corte y del corte que garantiza la separación respecto de cero. Entonces la distancia entre los recíprocos es menor que $\varepsilon$. Si sólo están definidos eventualmente, el argumento se aplica a esa cola.

### Microcontrol 046

[]{#MA-MIC-ANM-01-010-046}

[]{#MA-MSOL-ANM-01-010-046}

**Pregunta.** ¿Ser no nula término a término basta para que una sucesión de Cauchy tenga recíprocos de Cauchy?

**Solución.** No. $1/(n+1)$ es no nula y de Cauchy, pero sus recíprocos $n+1$ no lo son.

En $a_n=1/(n+1)$, cada término es positivo, pero no existe una cota inferior positiva común para una cola. Al invertirlos obtenemos $b_n=n+1$. Para cualquier corte $N$, los índices $N$ y $N+1$ dan $|b_{N+1}-b_N|=1$, de modo que falla la tolerancia fija uno. La inversión amplifica las diferencias cerca de cero; por eso hace falta estar separado de cero, además de evitar el valor cero término a término.

### Microcontrol 047

[]{#MA-MIC-ANM-01-010-047}

[]{#MA-MSOL-ANM-01-010-047}

**Pregunta.** ¿Qué desigualdad demuestra que el valor absoluto conserva Cauchy?

**Solución.** $\big||a_p|-|a_q|\big|\le|a_p-a_q|$, la desigualdad triangular inversa.

La desigualdad triangular da $|a_p|\le|a_p-a_q|+|a_q|$, luego $|a_p|-|a_q|\le|a_p-a_q|$. Intercambiando los índices obtenemos la desigualdad contraria para la diferencia de magnitudes. Juntas implican la cota indicada. Para cada tolerancia, el mismo corte que controla $|a_p-a_q|$ controla entonces la distancia entre $|a_p|$ y $|a_q|$. No se requieren cortes nuevos ni conocer los signos de los términos.

### Microcontrol 048

[]{#MA-MIC-ANM-01-010-048}

[]{#MA-MSOL-ANM-01-010-048}

**Pregunta.** ¿Cambiar finitos términos conserva Cauchy?

**Solución.** Sí. Después del último índice cambiado las distancias de todos los pares coinciden con las originales.

Sea $K$ un índice a partir del cual las sucesiones original y modificada coinciden. Dada una tolerancia, elegimos un corte $N$ de Cauchy para la original y usamos $\max\{N,K\}$. Después de ese corte, ninguno de los dos términos de un par ha sido modificado, así que sus distancias son las originales y satisfacen la misma estimación. El argumento funciona en ambas direcciones porque la coincidencia eventual es simétrica.

## §10.7 — La distancia permanece; el codominio cambia

### Microcontrol 049

[]{#MA-MIC-ANM-01-010-049}

[]{#MA-MSOL-ANM-01-010-049}

[]{#MA-SEC-ANM-01-010-007}

**Pregunta.** ¿Qué cambia al pasar de $q:\mathbb N\to\mathbb Q$ a $\iota\circ q:\mathbb N\to\mathbb R$?

**Solución.** Cambia el codominio y el conjunto permitido de destinos; los valores transportados y sus distancias usuales coinciden.

La inclusión usual $\iota:\mathbb Q\to\mathbb R$ conserva las distancias: $|\iota(r)-\iota(s)|=|r-s|$. Por eso los mismos cortes verifican Cauchy antes y después de incluir la sucesión en los reales. Lo que cambia es la conclusión de existencia: un límite en $\mathbb R$ puede no estar en la copia de $\mathbb Q$. Conservar distancias no garantiza que el sistema de partida contenga todos los destinos que sus aproximaciones necesitan.

### Microcontrol 050

[]{#MA-MIC-ANM-01-010-050}

[]{#MA-MSOL-ANM-01-010-050}

**Pregunta.** ¿Por qué el punto medio racional de la bisección no tiene cuadrado dos?

**Solución.** Ningún racional tiene cuadrado dos: en una fracción reducida esa igualdad obligaría a que numerador y denominador fueran ambos pares.

Si un racional $m/n$ en términos reducidos, con $n>0$, tuviera cuadrado dos, entonces $m^2=2n^2$. El cuadrado de un impar es impar, así que $m$ debe ser par: $m=2k$. Sustituyendo resulta $n^2=2k^2$, lo que obliga también a que $n$ sea par. Ambos tendrían el factor común dos, contradiciendo que la fracción estaba reducida. El punto medio de dos racionales es racional y queda sujeto al mismo argumento.

### Microcontrol 051

[]{#MA-MIC-ANM-01-010-051}

[]{#MA-MSOL-ANM-01-010-051}

**Pregunta.** ¿Cuál es la anchura del intervalo tras $n$ bisecciones?

**Solución.** $u_n-l_n=2^{-n}$, porque se empieza con anchura uno y cada paso la divide por dos.

La anchura inicial es $u_0-l_0=1$. Si en el paso $n$ vale $2^{-n}$, sustituir uno de los extremos por el punto medio deja una anchura igual a la mitad: $2^{-n}/2=2^{-(n+1)}$. Por inducción, la fórmula vale para todo índice. La elección de la mitad izquierda o derecha cambia la localización del intervalo, pero no esta regla de longitud. No estamos suponiendo todavía que exista un número de cuadrado dos.

### Microcontrol 052

[]{#MA-MIC-ANM-01-010-052}

[]{#MA-MSOL-ANM-01-010-052}

**Pregunta.** ¿Qué controla $|l_p-l_q|$ cuando $p,q\ge N$?

**Solución.** La anchura $2^{-N}$, porque ambos extremos inferiores están en el intervalo encajado $[l_N,u_N]$.

Los intervalos de bisección están encajados: cada intervalo posterior está contenido en todos los anteriores. Si $p,q\ge N$, los puntos $l_p$ y $l_q$ pertenecen a $[l_N,u_N]$. La distancia entre dos puntos de ese intervalo es a lo sumo su anchura, por lo que $|l_p-l_q|\le2^{-N}$. Para cualquier tolerancia escogemos un corte con $2^{-N}<\varepsilon$. El control vale para todos los pares, no sólo para extremos consecutivos.

### Microcontrol 053

[]{#MA-MIC-ANM-01-010-053}

[]{#MA-MSOL-ANM-01-010-053}

**Pregunta.** ¿Cómo se demuestra que los dos extremos tienen el mismo límite real?

**Solución.** $l_n$ converge por el criterio real y $u_n-l_n=2^{-n}\to0$; la regla de suma de C06 da a $u_n$ el mismo límite.

La estimación de pares demuestra que $l_n$ es de Cauchy; el criterio en $\mathbb R$ proporciona su límite $L$. Después escribimos $u_n=l_n+2^{-n}$. El segundo sumando tiende a cero, así que la regla de suma da $u_n\to L+0=L$. Hemos separado dos obligaciones: obtener primero la existencia de un destino y demostrar después que ambas fronteras se acercan a ese mismo destino.

### Microcontrol 054

[]{#MA-MIC-ANM-01-010-054}

[]{#MA-MSOL-ANM-01-010-054}

**Pregunta.** ¿Por qué el límite real construido cumple $L^2=2$?

**Solución.** Las desigualdades $l_n^2<2<u_n^2$ pasan al límite mediante la regla del producto y conservación de orden, dando $L^2\le2\le L^2$.

Como $l_n,u_n\to L$, la regla del producto implica $l_n^2,u_n^2\to L^2$. El orden se conserva en el límite como desigualdad no estricta: de $l_n^2<2$ obtenemos $L^2\le2$, y de $2<u_n^2$ obtenemos $2\le L^2$. Ambas relaciones fuerzan la igualdad. La desigualdad estricta de los términos puede convertirse en igualdad precisamente porque las fronteras se aproximan al mismo punto.

### Microcontrol 055

[]{#MA-MIC-ANM-01-010-055}

[]{#MA-MSOL-ANM-01-010-055}

**Pregunta.** ¿Por qué la sucesión racional no converge en $\mathbb Q$?

**Solución.** Un límite racional también sería límite real de su inclusión; unicidad lo igualaría a $L$, cuyo cuadrado es dos, contradiciendo la irracionalidad probada.

Supongamos que la sucesión racional tuviera límite $r\in\mathbb Q$. Al incluirla en los reales, la conservación de distancias muestra que también convergería a $\iota(r)$. Pero ya hemos probado que converge a $L$; la unicidad del límite real obliga a $\iota(r)=L$. Entonces $r^2=2$, contradiciendo la prueba de irracionalidad. La dificultad no es el comportamiento de las distancias, sino que el destino falta en el codominio racional.

### Microcontrol 056

[]{#MA-MIC-ANM-01-010-056}

[]{#MA-MSOL-ANM-01-010-056}

**Pregunta.** ¿Qué significa completitud secuencial para un subconjunto con distancia usual?

**Solución.** Que toda sucesión de Cauchy con valores en ese conjunto converge a un elemento del mismo conjunto. El lugar del destino es parte de la condición.

Para un subconjunto $E\subseteq\mathbb R$, no basta saber que toda sucesión de Cauchy con términos en $E$ converge en la recta real. Eso ya lo garantiza la completitud de $\mathbb R$. La condición adicional es que su límite pertenezca a $E$. Por ejemplo, $1/(n+1)$ tiene términos en $(0,1]$ y es de Cauchy, pero su límite cero queda fuera. Este ejemplo distingue la existencia de un límite ambiente de la completitud del subespacio.

## §10.8 — Estimar el error antes de conocer la respuesta

### Microcontrol 057

[]{#MA-MIC-ANM-01-010-057}

[]{#MA-MSOL-ANM-01-010-057}

[]{#MA-SEC-ANM-01-010-008}

**Pregunta.** ¿Qué controla una cota geométrica de saltos que no controla el mero salto tendiendo a cero?

**Solución.** Controla uniformemente la acumulación de cualquier cantidad finita de saltos posteriores mediante una suma geométrica finita.

Saber que cada salto se hace pequeño no controla cuántos de esos saltos se acumulan entre dos índices lejanos. La cota geométrica permite sumar cualquier bloque: su longitud puede ser arbitrariamente grande, pero la suma queda por debajo de $C\rho^q/(1-\rho)$ cuando comienza en $q$. Esa cota depende del inicio del bloque y tiende a cero con él. Así produce exactamente el control uniforme sobre pares que exige Cauchy.

### Microcontrol 058

[]{#MA-MIC-ANM-01-010-058}

[]{#MA-MSOL-ANM-01-010-058}

**Pregunta.** Escribe la cota de pares si $|a_{n+1}-a_n|\le C\rho^n$ con $0<\rho<1$.

**Solución.** Para $p>q$, $|a_p-a_q|\le C\rho^q/(1-\rho)$; por simetría se usa el índice menor para cualquier par.

Para $p>q$, telescopamos $a_p-a_q=\sum_{j=q}^{p-1}(a_{j+1}-a_j)$ y aplicamos la desigualdad triangular. Resulta
$$|a_p-a_q|\le C\sum_{j=q}^{p-1}\rho^j=C\rho^q\frac{1-\rho^{p-q}}{1-\rho}\le\frac{C\rho^q}{1-\rho}.$$
Sólo interviene una suma finita. Si los índices están en el otro orden, los intercambiamos; si coinciden, la distancia es cero. Para pares posteriores a $N$, el índice menor es al menos $N$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-010-059}

[]{#MA-MSOL-ANM-01-010-059}

**Pregunta.** ¿Qué caso especial ocurre si $C=0$?

**Solución.** Todos los saltos son cero, luego la sucesión es constante y de Cauchy con corte cero.

La cota se convierte en $|a_{n+1}-a_n|\le0$. Como un valor absoluto es no negativo, necesariamente $a_{n+1}=a_n$ para todo $n$. Por inducción todos los términos coinciden con $a_0$. La sucesión es constante, tiene distancias de pares iguales a cero y converge a su valor inicial. Separar este caso evita escoger cortes mediante fórmulas que podrían introducir innecesariamente una división por $C$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-010-060}

[]{#MA-MSOL-ANM-01-010-060}

**Pregunta.** ¿Cómo se justifica aquí que $\rho^N\to0$?

**Solución.** Escribir $\rho^{-1}=1+t$ con $t>0$ y usar $(1+t)^N\ge1+Nt$ por inducción; así $\rho^N\le1/(1+Nt)\to0$.

Como $0<\rho<1$, podemos poner $t=\rho^{-1}-1>0$. La desigualdad $(1+t)^N\ge1+Nt$ se prueba por inducción: multiplicar la cota del paso $N$ por $1+t$ añade además el término no negativo $Nt^2$. Invirtiendo cantidades positivas obtenemos $\rho^N\le1/(1+Nt)$. Para una tolerancia, la propiedad arquimediana permite hacer el denominador mayor que su recíproco. Eso prueba el límite y permite construir cortes en la estimación geométrica.

### Microcontrol 061

[]{#MA-MIC-ANM-01-010-061}

[]{#MA-MSOL-ANM-01-010-061}

**Pregunta.** ¿Qué cota de error al límite se obtiene?

**Solución.** $|L-a_q|\le C\rho^q/(1-\rho)$, dejando tender el otro índice a infinito en la cota de pares.

Fijemos $q$. La cota de pares vale para todo $p>q$ y su lado derecho ya no depende de $p$. Como $a_p\to L$, la continuidad del valor absoluto, expresada mediante la desigualdad triangular inversa, da $|a_p-a_q|\to|L-a_q|$. El orden pasa al límite y conserva la cota no estricta. Así obtenemos una estimación del error del término $a_q$ respecto del destino, usando sólo datos de los saltos.

### Microcontrol 062

[]{#MA-MIC-ANM-01-010-062}

[]{#MA-MSOL-ANM-01-010-062}

**Pregunta.** ¿Qué número inicia la estimación de saltos en una iteración contractiva?

**Solución.** $D=|x_1-x_0|$; la inducción da $|x_{n+1}-x_n|\le D\rho^n$.

Para $x_{n+1}=F(x_n)$ y una contracción de factor $\rho$, cada salto cumple $|x_{n+2}-x_{n+1}|\le\rho|x_{n+1}-x_n|$. El salto inicial es $D=|x_1-x_0|$, que corresponde al caso $n=0$. Si el salto de índice $n$ no supera $D\rho^n$, el siguiente no supera $D\rho^{n+1}$. La inducción convierte un dato inicial conocido en cotas de todos los saltos, antes de haber calculado el punto fijo.

### Microcontrol 063

[]{#MA-MIC-ANM-01-010-063}

[]{#MA-MSOL-ANM-01-010-063}

**Pregunta.** ¿Cómo se prueba $F(L)=L$ sin invocar continuidad general?

**Solución.** $|F(L)-L|\le\rho|L-x_n|+|x_{n+1}-L|\to0$, por lo que la distancia fija debe ser cero.

Una vez obtenido $x_n\to L$ en el dominio de $F$, la desigualdad de contracción proporciona $|F(L)-F(x_n)|\le\rho|L-x_n|$. Como $F(x_n)=x_{n+1}$, la desigualdad triangular da la cota indicada para $|F(L)-L|$. Sus dos sumandos tienden a cero. El lado izquierdo es una distancia fija; si fuera positiva, una cota menor que su mitad sería imposible. Por tanto $F(L)=L$, sin necesitar un teorema general de continuidad.

### Microcontrol 064

[]{#MA-MIC-ANM-01-010-064}

[]{#MA-MSOL-ANM-01-010-064}

**Pregunta.** ¿Qué garantiza unicidad de un punto fijo con factor $\rho<1$?

**Solución.** Dos puntos fijos tendrían $|L-M|\le\rho|L-M|$; como $1-\rho>0$, su distancia sólo puede ser cero.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Ejercicios](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-microcontroles.html)

Si $F(L)=L$ y $F(M)=M$, la condición contractiva da $|L-M|=|F(L)-F(M)|\le\rho|L-M|$. Restando el segundo miembro resulta $(1-\rho)|L-M|\le0$. Ambos factores son no negativos y el primero es estrictamente positivo; en consecuencia $|L-M|=0$ y $L=M$. Aquí se ve por qué importa $\rho<1$: con factor uno, la identidad satisface la cota y puede tener muchos puntos fijos.
