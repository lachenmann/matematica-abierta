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
date-modified: '2026-10-11'
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

### Microcontrol 002

[]{#MA-MIC-ANM-01-010-002}

[]{#MA-MSOL-ANM-01-010-002}

**Pregunta.** ¿Puede el corte $N$ depender de los índices $p,q$?

**Solución.** No. Para cada tolerancia se escoge $N$ antes de los dos índices universales y debe servir para todos los pares posteriores.

### Microcontrol 003

[]{#MA-MIC-ANM-01-010-003}

[]{#MA-MSOL-ANM-01-010-003}

**Pregunta.** ¿Se permite $p=q$ en la definición?

**Solución.** Sí. La distancia es entonces cero y cumple toda tolerancia positiva.

### Microcontrol 004

[]{#MA-MIC-ANM-01-010-004}

[]{#MA-MSOL-ANM-01-010-004}

**Pregunta.** ¿Basta controlar pares de vecinos?

**Solución.** No. La definición exige todos los pares de una cola, incluso con separación temporal arbitrariamente grande.

### Microcontrol 005

[]{#MA-MIC-ANM-01-010-005}

[]{#MA-MSOL-ANM-01-010-005}

**Pregunta.** Da un corte suficiente de Cauchy para $a_n=1/(n+1)$.

**Solución.** Para $\varepsilon>0$ sirve cualquier natural $N$ con $N+1>1/\varepsilon$, pues las distancias posteriores son a lo sumo $1/(N+1)<\varepsilon$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-010-006}

[]{#MA-MSOL-ANM-01-010-006}

**Pregunta.** ¿Qué corte sirve para una sucesión constante?

**Solución.** $N=0$ para toda tolerancia, porque todas sus distancias son cero.

### Microcontrol 007

[]{#MA-MIC-ANM-01-010-007}

[]{#MA-MSOL-ANM-01-010-007}

**Pregunta.** ¿La condición de Cauchy exige monotonía?

**Solución.** No. Por ejemplo, $(-1)^n/(n+1)$ es de Cauchy y alterna de signo.

### Microcontrol 008

[]{#MA-MIC-ANM-01-010-008}

[]{#MA-MSOL-ANM-01-010-008}

**Pregunta.** ¿La definición por sí sola proporciona un algoritmo para calcular los cortes?

**Solución.** No. Afirma existencia para cada tolerancia. Una regla efectiva de cortes requiere información adicional sobre la sucesión.

## §10.2 — Del destino común al control interno

### Microcontrol 009

[]{#MA-MIC-ANM-01-010-009}

[]{#MA-MSOL-ANM-01-010-009}

[]{#MA-SEC-ANM-01-010-002}

**Pregunta.** ¿Qué tolerancia de convergencia se usa para probar Cauchy con tolerancia $\varepsilon$?

**Solución.** $\varepsilon/2$; así los dos errores respecto del límite suman menos que $\varepsilon$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-010-010}

[]{#MA-MSOL-ANM-01-010-010}

**Pregunta.** Escribe la desigualdad triangular que une $a_p,a_q$ con el límite $L$.

**Solución.** $|a_p-a_q|\le|a_p-L|+|a_q-L|$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-010-011}

[]{#MA-MSOL-ANM-01-010-011}

**Pregunta.** ¿Por qué el mismo corte controla ambos errores?

**Solución.** Porque la convergencia con tolerancia $\varepsilon/2$ vale para todo índice posterior, incluidos $p$ y $q$.

### Microcontrol 012

[]{#MA-MIC-ANM-01-010-012}

[]{#MA-MSOL-ANM-01-010-012}

**Pregunta.** ¿Interviene completitud en convergente implica Cauchy?

**Solución.** No. El límite ya existe por hipótesis; se usa su definición y la desigualdad triangular.

### Microcontrol 013

[]{#MA-MIC-ANM-01-010-013}

[]{#MA-MSOL-ANM-01-010-013}

**Pregunta.** ¿Qué distancia máxima garantiza por estimación una ventana abierta de radio $r$?

**Solución.** Distancia menor que $2r$ entre cualesquiera dos términos en esa ventana; el diámetro se distingue del radio.

### Microcontrol 014

[]{#MA-MIC-ANM-01-010-014}

[]{#MA-MSOL-ANM-01-010-014}

**Pregunta.** Da un corte directo para $a_n=(-1)^n/(n+1)$ con tolerancia $\varepsilon$.

**Solución.** Sirve cualquier $N$ con $N+1>2/\varepsilon$, pues $|a_p-a_q|\le2/(N+1)<\varepsilon$ para $p,q\ge N$.

### Microcontrol 015

[]{#MA-MIC-ANM-01-010-015}

[]{#MA-MSOL-ANM-01-010-015}

**Pregunta.** ¿Tener signos alternantes contradice convergencia?

**Solución.** No. La magnitud $1/(n+1)$ puede tender a cero; entonces la alternancia amortiguada converge y es de Cauchy.

### Microcontrol 016

[]{#MA-MIC-ANM-01-010-016}

[]{#MA-MSOL-ANM-01-010-016}

**Pregunta.** ¿La implicación ya demostrada permite concluir Cauchy implica convergente?

**Solución.** Todavía no en esta fase lógica: la recíproca exige construir un destino usando completitud, como se hará en §10.4.

## §10.3 — Encerrar una cola y recuperar la acotación

### Microcontrol 017

[]{#MA-MIC-ANM-01-010-017}

[]{#MA-MSOL-ANM-01-010-017}

[]{#MA-SEC-ANM-01-010-003}

**Pregunta.** ¿Qué tolerancia fija basta para recuperar acotación de una sucesión de Cauchy?

**Solución.** La tolerancia uno proporciona una cola próxima al término de su corte.

### Microcontrol 018

[]{#MA-MIC-ANM-01-010-018}

[]{#MA-MSOL-ANM-01-010-018}

**Pregunta.** ¿Qué término se toma como ancla de la cola?

**Solución.** $a_{N_0}$, donde $N_0$ es el corte de Cauchy para tolerancia uno.

### Microcontrol 019

[]{#MA-MIC-ANM-01-010-019}

[]{#MA-MSOL-ANM-01-010-019}

**Pregunta.** ¿Qué cota de $|a_n|$ se obtiene para $n\ge N_0$?

**Solución.** $|a_n|<|a_{N_0}|+1$, por $|a_n-a_{N_0}|<1$ y desigualdad triangular.

### Microcontrol 020

[]{#MA-MIC-ANM-01-010-020}

[]{#MA-MSOL-ANM-01-010-020}

**Pregunta.** ¿Cómo se trata el prefijo si $N_0=0$?

**Solución.** No hay prefijo anterior que controlar; $|a_0|+1$ acota ya todos los términos y no se toma un máximo vacío.

### Microcontrol 021

[]{#MA-MIC-ANM-01-010-021}

[]{#MA-MSOL-ANM-01-010-021}

**Pregunta.** ¿Acotada implica Cauchy?

**Solución.** No. $(-1)^n$ es acotada y tiene pares posteriores separados por dos después de cualquier corte.

### Microcontrol 022

[]{#MA-MIC-ANM-01-010-022}

[]{#MA-MSOL-ANM-01-010-022}

**Pregunta.** ¿Por qué existen los extremos reales de $T_N$?

**Solución.** $T_N$ contiene $a_N$ y es acotado; completitud garantiza su supremo e ínfimo reales.

### Microcontrol 023

[]{#MA-MIC-ANM-01-010-023}

[]{#MA-MSOL-ANM-01-010-023}

**Pregunta.** Si todas las distancias de una cola son menores que $\eta$, ¿qué cota se obtiene para su anchura?

**Solución.** $0\le u_N-\ell_N\le\eta$. Al tomar extremos puede perderse la desigualdad estricta.

### Microcontrol 024

[]{#MA-MIC-ANM-01-010-024}

[]{#MA-MSOL-ANM-01-010-024}

**Pregunta.** ¿Qué tolerancia de Cauchy garantiza anchura estrictamente menor que $\varepsilon$ por esa cota?

**Solución.** Usar $\eta=\varepsilon/2$ da anchura a lo sumo $\varepsilon/2$, y por tanto menor que $\varepsilon$.

## §10.4 — La completitud construye el destino

### Microcontrol 025

[]{#MA-MIC-ANM-01-010-025}

[]{#MA-MSOL-ANM-01-010-025}

[]{#MA-SEC-ANM-01-010-004}

**Pregunta.** ¿Cómo se define el candidato $L$ de la prueba principal?

**Solución.** $L=\sup\{\ell_N:N\in\mathbb N\}$, que existe por completitud porque el conjunto es no vacío y acotado superiormente.

### Microcontrol 026

[]{#MA-MIC-ANM-01-010-026}

[]{#MA-MSOL-ANM-01-010-026}

**Pregunta.** ¿Qué término compara $\ell_M$ con $u_N$ cuando los cortes son distintos?

**Solución.** $a_r$ con $r=\max\{M,N\}$ pertenece a ambas colas y da $\ell_M\le a_r\le u_N$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-010-027}

[]{#MA-MSOL-ANM-01-010-027}

**Pregunta.** ¿Por qué $L\le u_N$ para cada $N$?

**Solución.** $u_N$ acota todos los $\ell_M$ por la comparación entre cortes, y el supremo $L$ es la menor cota superior de ese conjunto.

### Microcontrol 028

[]{#MA-MIC-ANM-01-010-028}

[]{#MA-MSOL-ANM-01-010-028}

**Pregunta.** ¿Dónde interviene completitud además de la existencia de extremos de cola?

**Solución.** En la existencia del supremo de los extremos inferiores, que construye el centro real común a todos los intervalos.

### Microcontrol 029

[]{#MA-MIC-ANM-01-010-029}

[]{#MA-MSOL-ANM-01-010-029}

**Pregunta.** ¿Por qué $|a_n-L|$ queda acotada por la anchura para $n\ge N$?

**Solución.** Tanto $a_n$ como $L$ pertenecen a $[\ell_N,u_N]$, por lo que su distancia es a lo sumo $u_N-\ell_N$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-010-030}

[]{#MA-MSOL-ANM-01-010-030}

**Pregunta.** ¿Qué prueba la unicidad del real común a todos los intervalos?

**Solución.** Dos supuestos centros tendrían distancia menor que cualquier tolerancia por el ancho pequeño; una distancia positiva contradice usar su mitad como tolerancia.

### Microcontrol 031

[]{#MA-MIC-ANM-01-010-031}

[]{#MA-MSOL-ANM-01-010-031}

**Pregunta.** ¿Necesita la prueba principal Bolzano–Weierstrass?

**Solución.** No. Construye $L$ mediante supremo y verifica convergencia directamente con los intervalos de cola y Cauchy.

### Microcontrol 032

[]{#MA-MIC-ANM-01-010-032}

[]{#MA-MSOL-ANM-01-010-032}

**Pregunta.** Enuncia el criterio de Cauchy con su codominio.

**Solución.** Una sucesión $a:\mathbb N\to\mathbb R$ converge a algún real si y sólo si es de Cauchy para la distancia usual.

## §10.5 — Negar Cauchy: encontrar pares separados

### Microcontrol 033

[]{#MA-MIC-ANM-01-010-033}

[]{#MA-MSOL-ANM-01-010-033}

[]{#MA-SEC-ANM-01-010-005}

**Pregunta.** ¿Qué orden de cuantificadores expresa no ser de Cauchy?

**Solución.** Existe $\varepsilon_0>0$ tal que para todo corte $N$ existen $p,q\ge N$ con $|a_p-a_q|\ge\varepsilon_0$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-010-034}

[]{#MA-MSOL-ANM-01-010-034}

**Pregunta.** ¿Puede la tolerancia de la negación cambiar con $N$?

**Solución.** No. Debe quedar fija antes de considerar cualquier corte; los índices testigo sí pueden depender de $N$.

### Microcontrol 035

[]{#MA-MIC-ANM-01-010-035}

[]{#MA-MSOL-ANM-01-010-035}

**Pregunta.** ¿Por qué la negación usa $\ge$ y no sólo $>$?

**Solución.** Porque se niega una desigualdad estricta $|a_p-a_q|<\varepsilon_0$; la igualdad también hace fallar la condición.

### Microcontrol 036

[]{#MA-MIC-ANM-01-010-036}

[]{#MA-MSOL-ANM-01-010-036}

**Pregunta.** Da testigos para negar Cauchy en $a_n=n$.

**Solución.** Con $\varepsilon_0=1$ y cualquier corte $N$, tomar $p=N,q=N+1$ da distancia uno.

### Microcontrol 037

[]{#MA-MIC-ANM-01-010-037}

[]{#MA-MSOL-ANM-01-010-037}

**Pregunta.** ¿Qué ocurre con $|a_{n+1}-a_n|$ si $a$ es de Cauchy?

**Solución.** Tiende a cero: para cada tolerancia, el corte de Cauchy controla todos los pares vecinos posteriores.

### Microcontrol 038

[]{#MA-MIC-ANM-01-010-038}

[]{#MA-MSOL-ANM-01-010-038}

**Pregunta.** ¿Cuál es el salto de $h_n=\sum_{j=1}^{n+1}1/j$?

**Solución.** $h_{n+1}-h_n=1/(n+2)$, que tiende a cero por arquimedianidad.

### Microcontrol 039

[]{#MA-MIC-ANM-01-010-039}

[]{#MA-MSOL-ANM-01-010-039}

**Pregunta.** ¿Qué pares de índices muestran que $h$ no es de Cauchy?

**Solución.** Para $m\ge1$, los índices $m-1$ y $2m-1$ tienen distancia al menos $1/2$. Dado $N$, elegir $m=N+1$ los deja ambos posteriores al corte.

### Microcontrol 040

[]{#MA-MIC-ANM-01-010-040}

[]{#MA-MSOL-ANM-01-010-040}

**Pregunta.** ¿El contraejemplo de $h$ necesita una suma infinita?

**Solución.** No. Todos los términos y diferencias usados son sumas finitas; la separación de bloques basta para negar Cauchy.

## §10.6 — Conservar el control al operar

### Microcontrol 041

[]{#MA-MIC-ANM-01-010-041}

[]{#MA-MSOL-ANM-01-010-041}

[]{#MA-SEC-ANM-01-010-006}

**Pregunta.** ¿Qué corte sirve para probar que la suma de dos sucesiones de Cauchy es de Cauchy?

**Solución.** El máximo de sus cortes para tolerancia $\varepsilon/2$; las dos diferencias de sumandos dan una distancia total menor que $\varepsilon$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-010-042}

[]{#MA-MSOL-ANM-01-010-042}

**Pregunta.** ¿Qué sucede al multiplicar por cero?

**Solución.** La sucesión resultante es constante cero y es de Cauchy con corte cero; no se divide por el escalar.

### Microcontrol 043

[]{#MA-MIC-ANM-01-010-043}

[]{#MA-MSOL-ANM-01-010-043}

**Pregunta.** ¿Por qué el argumento del producto necesita acotación?

**Solución.** Porque la diferencia del producto contiene factores $|a_p|$ y $|b_q|$ multiplicando las diferencias; cotas globales los controlan.

### Microcontrol 044

[]{#MA-MIC-ANM-01-010-044}

[]{#MA-MSOL-ANM-01-010-044}

**Pregunta.** ¿Por qué se usan denominadores $A+1$ y $B+1$ al escoger tolerancias para el producto?

**Solución.** Para mantenerlos positivos incluso si una cota es cero y obtener una estimación estrictamente menor que la tolerancia final.

### Microcontrol 045

[]{#MA-MIC-ANM-01-010-045}

[]{#MA-MSOL-ANM-01-010-045}

**Pregunta.** ¿Qué hipótesis de una cola permite controlar recíprocos?

**Solución.** $|a_n|\ge c>0$ desde algún corte; entonces la diferencia de recíprocos es a lo sumo $|a_p-a_q|/c^2$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-010-046}

[]{#MA-MSOL-ANM-01-010-046}

**Pregunta.** ¿Ser no nula término a término basta para que una sucesión de Cauchy tenga recíprocos de Cauchy?

**Solución.** No. $1/(n+1)$ es no nula y de Cauchy, pero sus recíprocos $n+1$ no lo son.

### Microcontrol 047

[]{#MA-MIC-ANM-01-010-047}

[]{#MA-MSOL-ANM-01-010-047}

**Pregunta.** ¿Qué desigualdad demuestra que el valor absoluto conserva Cauchy?

**Solución.** $\big||a_p|-|a_q|\big|\le|a_p-a_q|$, la desigualdad triangular inversa.

### Microcontrol 048

[]{#MA-MIC-ANM-01-010-048}

[]{#MA-MSOL-ANM-01-010-048}

**Pregunta.** ¿Cambiar finitos términos conserva Cauchy?

**Solución.** Sí. Después del último índice cambiado las distancias de todos los pares coinciden con las originales.

## §10.7 — La distancia permanece; el codominio cambia

### Microcontrol 049

[]{#MA-MIC-ANM-01-010-049}

[]{#MA-MSOL-ANM-01-010-049}

[]{#MA-SEC-ANM-01-010-007}

**Pregunta.** ¿Qué cambia al pasar de $q:\mathbb N\to\mathbb Q$ a $\iota\circ q:\mathbb N\to\mathbb R$?

**Solución.** Cambia el codominio y el conjunto permitido de destinos; los valores transportados y sus distancias usuales coinciden.

### Microcontrol 050

[]{#MA-MIC-ANM-01-010-050}

[]{#MA-MSOL-ANM-01-010-050}

**Pregunta.** ¿Por qué el punto medio racional de la bisección no tiene cuadrado dos?

**Solución.** Ningún racional tiene cuadrado dos: en una fracción reducida esa igualdad obligaría a que numerador y denominador fueran ambos pares.

### Microcontrol 051

[]{#MA-MIC-ANM-01-010-051}

[]{#MA-MSOL-ANM-01-010-051}

**Pregunta.** ¿Cuál es la anchura del intervalo tras $n$ bisecciones?

**Solución.** $u_n-l_n=2^{-n}$, porque se empieza con anchura uno y cada paso la divide por dos.

### Microcontrol 052

[]{#MA-MIC-ANM-01-010-052}

[]{#MA-MSOL-ANM-01-010-052}

**Pregunta.** ¿Qué controla $|l_p-l_q|$ cuando $p,q\ge N$?

**Solución.** La anchura $2^{-N}$, porque ambos extremos inferiores están en el intervalo encajado $[l_N,u_N]$.

### Microcontrol 053

[]{#MA-MIC-ANM-01-010-053}

[]{#MA-MSOL-ANM-01-010-053}

**Pregunta.** ¿Cómo se demuestra que los dos extremos tienen el mismo límite real?

**Solución.** $l_n$ converge por el criterio real y $u_n-l_n=2^{-n}\to0$; la regla de suma de C06 da a $u_n$ el mismo límite.

### Microcontrol 054

[]{#MA-MIC-ANM-01-010-054}

[]{#MA-MSOL-ANM-01-010-054}

**Pregunta.** ¿Por qué el límite real construido cumple $L^2=2$?

**Solución.** Las desigualdades $l_n^2<2<u_n^2$ pasan al límite mediante la regla del producto y conservación de orden, dando $L^2\le2\le L^2$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-010-055}

[]{#MA-MSOL-ANM-01-010-055}

**Pregunta.** ¿Por qué la sucesión racional no converge en $\mathbb Q$?

**Solución.** Un límite racional también sería límite real de su inclusión; unicidad lo igualaría a $L$, cuyo cuadrado es dos, contradiciendo la irracionalidad probada.

### Microcontrol 056

[]{#MA-MIC-ANM-01-010-056}

[]{#MA-MSOL-ANM-01-010-056}

**Pregunta.** ¿Qué significa completitud secuencial para un subconjunto con distancia usual?

**Solución.** Que toda sucesión de Cauchy con valores en ese conjunto converge a un elemento del mismo conjunto. El lugar del destino es parte de la condición.

## §10.8 — Estimar el error antes de conocer la respuesta

### Microcontrol 057

[]{#MA-MIC-ANM-01-010-057}

[]{#MA-MSOL-ANM-01-010-057}

[]{#MA-SEC-ANM-01-010-008}

**Pregunta.** ¿Qué controla una cota geométrica de saltos que no controla el mero salto tendiendo a cero?

**Solución.** Controla uniformemente la acumulación de cualquier cantidad finita de saltos posteriores mediante una suma geométrica finita.

### Microcontrol 058

[]{#MA-MIC-ANM-01-010-058}

[]{#MA-MSOL-ANM-01-010-058}

**Pregunta.** Escribe la cota de pares si $|a_{n+1}-a_n|\le C\rho^n$ con $0<\rho<1$.

**Solución.** Para $p>q$, $|a_p-a_q|\le C\rho^q/(1-\rho)$; por simetría se usa el índice menor para cualquier par.

### Microcontrol 059

[]{#MA-MIC-ANM-01-010-059}

[]{#MA-MSOL-ANM-01-010-059}

**Pregunta.** ¿Qué caso especial ocurre si $C=0$?

**Solución.** Todos los saltos son cero, luego la sucesión es constante y de Cauchy con corte cero.

### Microcontrol 060

[]{#MA-MIC-ANM-01-010-060}

[]{#MA-MSOL-ANM-01-010-060}

**Pregunta.** ¿Cómo se justifica aquí que $\rho^N\to0$?

**Solución.** Escribir $\rho^{-1}=1+t$ con $t>0$ y usar $(1+t)^N\ge1+Nt$ por inducción; así $\rho^N\le1/(1+Nt)\to0$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-010-061}

[]{#MA-MSOL-ANM-01-010-061}

**Pregunta.** ¿Qué cota de error al límite se obtiene?

**Solución.** $|L-a_q|\le C\rho^q/(1-\rho)$, dejando tender el otro índice a infinito en la cota de pares.

### Microcontrol 062

[]{#MA-MIC-ANM-01-010-062}

[]{#MA-MSOL-ANM-01-010-062}

**Pregunta.** ¿Qué número inicia la estimación de saltos en una iteración contractiva?

**Solución.** $D=|x_1-x_0|$; la inducción da $|x_{n+1}-x_n|\le D\rho^n$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-010-063}

[]{#MA-MSOL-ANM-01-010-063}

**Pregunta.** ¿Cómo se prueba $F(L)=L$ sin invocar continuidad general?

**Solución.** $|F(L)-L|\le\rho|L-x_n|+|x_{n+1}-L|\to0$, por lo que la distancia fija debe ser cero.

### Microcontrol 064

[]{#MA-MIC-ANM-01-010-064}

[]{#MA-MSOL-ANM-01-010-064}

**Pregunta.** ¿Qué garantiza unicidad de un punto fijo con factor $\rho<1$?

**Solución.** Dos puntos fijos tendrían $|L-M|\le\rho|L-M|$; como $1-\rho>0$, su distancia sólo puede ser cero.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Ejercicios](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-microcontroles.html)
