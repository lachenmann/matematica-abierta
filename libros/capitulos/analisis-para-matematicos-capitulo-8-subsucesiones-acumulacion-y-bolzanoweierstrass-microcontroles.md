---
content-id: MA-BCH-0237
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-008-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 8
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C08_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html) · [Ejercicios](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §8.1 — Seleccionar términos sin perder el orden

### Microcontrol 001

[]{#MA-MIC-ANM-01-008-001}

[]{#MA-MSOL-ANM-01-008-001}

[]{#MA-SEC-ANM-01-008-001}

**Pregunta.** Para $a_n=(-1)^n$ y $\varphi(k)=2k+1$, calcula $\varphi(0)$, $\varphi(2)$ y $b_2=a_{\varphi(2)}$.

**Solución.** $\varphi(0)=1$, $\varphi(2)=5$ y $b_2=a_5=-1$. Los dos primeros son índices originales; el último es un valor real.

### Microcontrol 002

[]{#MA-MIC-ANM-01-008-002}

[]{#MA-MSOL-ANM-01-008-002}

**Pregunta.** ¿Por qué $\varphi(k)=k+3$ define una subsucesión desde $k=0$?

**Solución.** Toma valores naturales y $\varphi(k+1)=\varphi(k)+1>\varphi(k)$. Selecciona la cola desde el índice tres y la reindexa desde cero.

### Microcontrol 003

[]{#MA-MIC-ANM-01-008-003}

[]{#MA-MSOL-ANM-01-008-003}

**Pregunta.** ¿Es $\varphi(k)=0$ un selector de subsucesión? Justifica.

**Solución.** No es estrictamente creciente: $\varphi(0)=\varphi(1)=0$. Que la composición con una sucesión sea una función no convierte a este mapa en selector.

### Microcontrol 004

[]{#MA-MIC-ANM-01-008-004}

[]{#MA-MSOL-ANM-01-008-004}

**Pregunta.** ¿Puede una subsucesión constante provenir de índices todos distintos?

**Solución.** Sí. La selección impar de $(-1)^n$ usa índices $1,3,5,\ldots$ y tiene valor constante $-1$. El crecimiento se exige a los índices, no a los valores.

### Microcontrol 005

[]{#MA-MIC-ANM-01-008-005}

[]{#MA-MSOL-ANM-01-008-005}

**Pregunta.** Escribe dominio y codominio de $a$, $\varphi$ y $a\circ\varphi$.

**Solución.** $a:\mathbb N\to\mathbb R$, $\varphi:\mathbb N\to\mathbb N$ y $a\circ\varphi:\mathbb N\to\mathbb R$. La composición está definida porque los valores de $\varphi$ son índices admisibles de $a$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-008-006}

[]{#MA-MSOL-ANM-01-008-006}

**Pregunta.** ¿Qué paso permite deducir $\varphi(k+1)\ge k+1$ a partir de $\varphi(k)\ge k$?

**Solución.** El crecimiento estricto entre naturales implica $\varphi(k+1)\ge\varphi(k)+1\ge k+1$. No basta una desigualdad entre reales arbitrarios para garantizar ese incremento mínimo de uno.

### Microcontrol 007

[]{#MA-MIC-ANM-01-008-007}

[]{#MA-MSOL-ANM-01-008-007}

**Pregunta.** Si $\varphi(k)=2k+1$ y $\psi(j)=3j$, calcula el selector de una extracción de la extracción.

**Solución.** Es $(\varphi\circ\psi)(j)=6j+1$. Primero se elige la posición $3j$ de la primera subsucesión y luego su posición original.

### Microcontrol 008

[]{#MA-MIC-ANM-01-008-008}

[]{#MA-MSOL-ANM-01-008-008}

**Pregunta.** ¿Dónde se representa en la gráfica nueva el término original $(5,-1)$ de la selección impar?

**Solución.** Como $(2,-1)$, porque $\varphi(2)=5$. Se conserva la altura y cambia el índice horizontal; no se identifica el punto original con el nuevo.

## §8.2 — Lo que conserva una subsucesión

### Microcontrol 009

[]{#MA-MIC-ANM-01-008-009}

[]{#MA-MSOL-ANM-01-008-009}

[]{#MA-SEC-ANM-01-008-002}

**Pregunta.** Si $N$ sirve para una tolerancia de $a_n\to L$, ¿por qué $K=N$ sirve para cualquier subsucesión?

**Solución.** Si $k\ge K=N$, entonces $\varphi(k)\ge k\ge N$ y por ello $|a_{\varphi(k)}-L|<\varepsilon$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-008-010}

[]{#MA-MSOL-ANM-01-008-010}

**Pregunta.** ¿Debe $K=N$ ser el menor umbral de la subsucesión?

**Solución.** No. Un selector puede omitir todos los términos que incumplían la tolerancia antes de $N$. La prueba sólo acredita que ese umbral es suficiente.

### Microcontrol 011

[]{#MA-MIC-ANM-01-008-011}

[]{#MA-MSOL-ANM-01-008-011}

**Pregunta.** ¿Qué contradicción producen las selecciones par e impar de $(-1)^n$ si suponemos convergencia?

**Solución.** Un límite global sería límite de ambas selecciones. Como éstas convergen a uno y menos uno, la unicidad obligaría a $1=-1$, imposible.

### Microcontrol 012

[]{#MA-MIC-ANM-01-008-012}

[]{#MA-MSOL-ANM-01-008-012}

**Pregunta.** En el ejemplo $b_k=1/(k+1)$, ¿entra $b_1$ en la ventana de radio $1/2$ alrededor de cero?

**Solución.** No: $|b_1|=1/2$ es la frontera. La ventana exige distancia estrictamente menor que $1/2$.

### Microcontrol 013

[]{#MA-MIC-ANM-01-008-013}

[]{#MA-MSOL-ANM-01-008-013}

**Pregunta.** Para ese mismo radio, verifica que $K=2$ funciona para $b$.

**Solución.** Si $k\ge2$, $0<b_k\le1/3<1/2$. Así todos los términos de la cola nueva entran en la ventana.

### Microcontrol 014

[]{#MA-MIC-ANM-01-008-014}

[]{#MA-MSOL-ANM-01-008-014}

**Pregunta.** ¿Por qué la selección par convergente del ejemplo par-impar no demuestra convergencia global?

**Solución.** No controla los términos descartados. Los impares son siempre dos; su límite es dos, diferente del límite cero de la selección par.

### Microcontrol 015

[]{#MA-MIC-ANM-01-008-015}

[]{#MA-MSOL-ANM-01-008-015}

**Pregunta.** Si $|a_n|\le7$ para todo $n$, ¿qué cota hereda $a_{\varphi(k)}$?

**Solución.** La misma: $|a_{\varphi(k)}|\le7$ para todo $k$, porque cada $\varphi(k)$ pertenece al dominio original.

### Microcontrol 016

[]{#MA-MIC-ANM-01-008-016}

[]{#MA-MSOL-ANM-01-008-016}

**Pregunta.** ¿Cómo se prueba que una subsucesión de una sucesión no decreciente es no decreciente?

**Solución.** Como $\varphi(k)<\varphi(k+1)$, el orden de los términos originales da $a_{\varphi(k)}\le a_{\varphi(k+1)}$. Se permiten valores iguales.

## §8.3 — Regresar cerca de un punto

### Microcontrol 017

[]{#MA-MIC-ANM-01-008-017}

[]{#MA-MSOL-ANM-01-008-017}

[]{#MA-SEC-ANM-01-008-003}

**Pregunta.** Escribe los cuantificadores que definen un punto de acumulación secuencial $L$.

**Solución.** $\forall\varepsilon>0\ \forall N\in\mathbb N\ \exists n\ge N:\ |a_n-L|<\varepsilon$. El testigo puede depender de la tolerancia y del corte.

### Microcontrol 018

[]{#MA-MIC-ANM-01-008-018}

[]{#MA-MSOL-ANM-01-008-018}

**Pregunta.** ¿Por qué una sola aparición de $L$ no garantiza acumulación secuencial?

**Solución.** La definición exige visitas después de todo corte. Por ejemplo, $a_0=0$ y $a_n=1$ para $n\ge1$ no visita $B(0,1/2)$ después del corte uno.

### Microcontrol 019

[]{#MA-MIC-ANM-01-008-019}

[]{#MA-MSOL-ANM-01-008-019}

**Pregunta.** ¿Por qué un conjunto infinito de índices contiene un índice mayor que cualquier $m$ fijado?

**Solución.** Si no lo contuviera, estaría incluido en el conjunto finito $\{0,\ldots,m\}$ y sería finito, contradicción.

### Microcontrol 020

[]{#MA-MIC-ANM-01-008-020}

[]{#MA-MSOL-ANM-01-008-020}

**Pregunta.** ¿Qué dos requisitos se imponen al elegir $n_{k+1}$ en la prueba?

**Solución.** $n_{k+1}\ge n_k+1$ y $|a_{n_{k+1}}-L|<1/(k+2)$. El primero asegura avance y el segundo reduce el error.

### Microcontrol 021

[]{#MA-MIC-ANM-01-008-021}

[]{#MA-MSOL-ANM-01-008-021}

**Pregunta.** ¿Qué garantiza que cada conjunto admisible de índices tenga mínimo?

**Solución.** La acumulación secuencial garantiza que es no vacío; el buen orden de $\mathbb N$ garantiza su mínimo. Son dos obligaciones distintas.

### Microcontrol 022

[]{#MA-MIC-ANM-01-008-022}

[]{#MA-MSOL-ANM-01-008-022}

**Pregunta.** Si $|a_{n_k}-L|<1/(k+1)$, ¿cómo eliges un umbral para $\varepsilon>0$?

**Solución.** Por arquimedianidad toma $K$ con $K+1>1/\varepsilon$. Para $k\ge K$ el error es menor que $1/(K+1)<\varepsilon$.

### Microcontrol 023

[]{#MA-MIC-ANM-01-008-023}

[]{#MA-MSOL-ANM-01-008-023}

**Pregunta.** En la dirección inversa, ¿por qué se toma $k=\max\{K,N\}$?

**Solución.** Así $k\ge K$ da cercanía del valor y $\varphi(k)\ge k\ge N$ da un índice original posterior al corte solicitado.

### Microcontrol 024

[]{#MA-MIC-ANM-01-008-024}

[]{#MA-MSOL-ANM-01-008-024}

**Pregunta.** En el ejemplo par-impar, ¿por qué el primer mínimo para error menor que uno es $n_0=2$ y no cero?

**Solución.** $a_0=1$ no tiene error menor que uno, $a_1=2$ tampoco y $a_2=1/2$ sí. Por eso el mínimo admisible es dos.

## §8.4 — Puntos de una sucesión y puntos de un conjunto

### Microcontrol 025

[]{#MA-MIC-ANM-01-008-025}

[]{#MA-MSOL-ANM-01-008-025}

[]{#MA-SEC-ANM-01-008-004}

**Pregunta.** ¿Qué condición sobre el testigo distingue adherencia de acumulación de un conjunto?

**Solución.** En acumulación el testigo debe ser distinto del centro $L$; en adherencia puede ser $L$. En ambos casos debe pertenecer al conjunto y a cada bola solicitada.

### Microcontrol 026

[]{#MA-MIC-ANM-01-008-026}

[]{#MA-MSOL-ANM-01-008-026}

**Pregunta.** Para $c_n=0$, distingue acumulación secuencial de acumulación de su imagen.

**Solución.** Cero es punto secuencial porque aparece después de todo corte. La imagen $\{0\}$ no tiene puntos de acumulación. En el centro $0$, cualquier bola perforada queda sin puntos de la imagen. Si $x\ne0$, el radio $|x|/2>0$ produce una bola que no contiene $0$, porque su distancia al centro es $|x|$. Así se excluyen todos los centros reales.

### Microcontrol 027

[]{#MA-MIC-ANM-01-008-027}

[]{#MA-MSOL-ANM-01-008-027}

**Pregunta.** Para $d_0=0$, $d_n=1$ si $n\ge1$, ¿es cero adherente a la imagen? ¿Es punto secuencial?

**Solución.** Es adherente porque pertenece a la imagen. No es punto secuencial: con radio $1/2$ y corte uno no hay visitas cerca de cero.

### Microcontrol 028

[]{#MA-MIC-ANM-01-008-028}

[]{#MA-MSOL-ANM-01-008-028}

**Pregunta.** ¿Qué estimación asegura convergencia de los testigos de adherencia elegidos?

**Solución.** $|x_k-L|<1/(k+1)$; arquimedianidad convierte esta escala en un umbral válido para cualquier tolerancia positiva.

### Microcontrol 029

[]{#MA-MIC-ANM-01-008-029}

[]{#MA-MSOL-ANM-01-008-029}

**Pregunta.** ¿Puede existir una sucesión de dominio $\mathbb N$ con valores en el conjunto vacío?

**Solución.** No. Ya su evaluación en cero tendría que ser un elemento del vacío. Esto concuerda con que el vacío carezca de puntos adherentes.

### Microcontrol 030

[]{#MA-MIC-ANM-01-008-030}

[]{#MA-MSOL-ANM-01-008-030}

**Pregunta.** ¿Por qué el radio de exclusión de valores anteriores es positivo?

**Solución.** Para $k\ge1$ hay finitos valores previos, todos distintos de $L$. Sus distancias al centro son positivas y tienen un mínimo positivo; su mitad y $1/(k+1)$ también lo son.

### Microcontrol 031

[]{#MA-MIC-ANM-01-008-031}

[]{#MA-MSOL-ANM-01-008-031}

**Pregunta.** ¿Cómo se trata el paso inicial de la construcción de valores distintos?

**Solución.** Se elige $x_0\in A\cap B(L,1)\setminus\{L\}$ por acumulación. No se toma mínimo de distancias anteriores, pues todavía no hay valores anteriores.

### Microcontrol 032

[]{#MA-MIC-ANM-01-008-032}

[]{#MA-MSOL-ANM-01-008-032}

**Pregunta.** ¿La elección de $x_k\in A\cap B(L,r)$ significa tomar el menor real de ese conjunto?

**Solución.** No. Ese conjunto puede no tener menor elemento. Se usa una función de elección clásica sobre subconjuntos no vacíos de $A$, diferente del mínimo de índices naturales.

## §8.5 — Dividir el espacio y conservar índices

### Microcontrol 033

[]{#MA-MIC-ANM-01-008-033}

[]{#MA-MSOL-ANM-01-008-033}

[]{#MA-SEC-ANM-01-008-005}

**Pregunta.** ¿Qué ocurre si la cota inicial es $M=0$?

**Solución.** $|a_n|\le0$ obliga a $a_n=0$ para todo $n$. La selección identidad converge a cero y no hace falta bisecar.

### Microcontrol 034

[]{#MA-MIC-ANM-01-008-034}

[]{#MA-MSOL-ANM-01-008-034}

**Pregunta.** ¿Por qué se conservan infinitos índices y no sólo algún término en cada intervalo?

**Solución.** Un solo término podría corresponder siempre al mismo índice. Infinitos índices garantizan que después de cualquier elección finita quede uno posterior para continuar la extracción.

### Microcontrol 035

[]{#MA-MIC-ANM-01-008-035}

[]{#MA-MSOL-ANM-01-008-035}

**Pregunta.** ¿Qué contradicción habría si las dos mitades recibieran sólo finitos índices?

**Solución.** Su unión recibiría sólo finitos índices. Como las mitades cubren $I_k$, esa unión es $E_k$, que por construcción es infinito.

### Microcontrol 036

[]{#MA-MIC-ANM-01-008-036}

[]{#MA-MSOL-ANM-01-008-036}

**Pregunta.** ¿Las mitades cerradas de un intervalo son disjuntas? ¿Afecta esto al argumento?

**Solución.** Comparten el punto medio. No afecta: la unión de dos conjuntos finitos sigue siendo finita aunque se solapen.

### Microcontrol 037

[]{#MA-MIC-ANM-01-008-037}

[]{#MA-MSOL-ANM-01-008-037}

**Pregunta.** ¿Cuál es la anchura de $I_k$ cuando $I_0=[-M,M]$?

**Solución.** $w_k=2M/2^k$, porque la anchura inicial es $2M$ y cada paso la divide por dos.

### Microcontrol 038

[]{#MA-MIC-ANM-01-008-038}

[]{#MA-MSOL-ANM-01-008-038}

**Pregunta.** ¿Qué cambio de índice permite usar la formulación de C03 con índices positivos?

**Solución.** $J_m=I_{m-1}$ para $m\ge1$. Así $J_1=I_0$ y la familia conserva exactamente los mismos intervalos e intersección.

### Microcontrol 039

[]{#MA-MIC-ANM-01-008-039}

[]{#MA-MSOL-ANM-01-008-039}

**Pregunta.** ¿Dónde se usa directamente la completitud?

**Solución.** En el teorema de intervalos cerrados encajados de C03, que garantiza un real común a todos los $I_k$. La reducción de anchuras por sí sola no proporciona esa existencia.

### Microcontrol 040

[]{#MA-MIC-ANM-01-008-040}

[]{#MA-MSOL-ANM-01-008-040}

**Pregunta.** ¿Cómo excluye la anchura arbitrariamente pequeña dos puntos comunes distintos?

**Solución.** Si su distancia es $d>0$ y $M>0$, toma $K=\lfloor2M/d\rfloor+1$. La desigualdad $2^K\ge K+1$ da $w_K=2M/2^K\le2M/(K+1)<d$. Si $M=0$, el intervalo inicial ya es el singleton $\{0\}$. En el caso $M>0$, los dos puntos pertenecen a $I_K$ y tendrían distancia a lo sumo $w_K$, dando $d\le w_K<d$.

## §8.6 — Bolzano–Weierstrass: construir la extracción

### Microcontrol 041

[]{#MA-MIC-ANM-01-008-041}

[]{#MA-MSOL-ANM-01-008-041}

[]{#MA-SEC-ANM-01-008-006}

**Pregunta.** Enuncia la conclusión precisa de Bolzano–Weierstrass para una sucesión real acotada.

**Solución.** Existe un selector estrictamente creciente $\varphi:\mathbb N\to\mathbb N$ y un real $L$ tales que $a_{\varphi(k)}\to L$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-008-042}

[]{#MA-MSOL-ANM-01-008-042}

**Pregunta.** ¿Por qué existe un elemento de $E_{k+1}$ mayor que $n_k$?

**Solución.** El conjunto $E_{k+1}\setminus\{0,\ldots,n_k\}$ es no vacío: si fuera vacío, $E_{k+1}$ estaría contenido en un conjunto finito y sería finito. Cualquier elemento de esa diferencia es mayor que $n_k$.

### Microcontrol 043

[]{#MA-MIC-ANM-01-008-043}

[]{#MA-MSOL-ANM-01-008-043}

**Pregunta.** ¿Qué acredita que $b_k=a_{n_k}$ sea una subsucesión?

**Solución.** La regla $n_{k+1}>n_k$ implica crecimiento estricto del mapa $k\mapsto n_k$. La pertenencia a intervalos sin ese crecimiento no bastaría.

### Microcontrol 044

[]{#MA-MIC-ANM-01-008-044}

[]{#MA-MSOL-ANM-01-008-044}

**Pregunta.** ¿Por qué $a_{n_k}$ y $L$ pertenecen a $I_K$ cuando $k\ge K$?

**Solución.** Ambos pertenecen a $I_k$, y el encajamiento da $I_k\subseteq I_K$.

### Microcontrol 045

[]{#MA-MIC-ANM-01-008-045}

[]{#MA-MSOL-ANM-01-008-045}

**Pregunta.** Completa la estimación final que demuestra convergencia.

**Solución.** Para $k\ge K$ se tiene $|a_{n_k}-L|\le w_K<\varepsilon$, eligiendo primero $K$ para que la anchura sea menor que la tolerancia.

### Microcontrol 046

[]{#MA-MIC-ANM-01-008-046}

[]{#MA-MSOL-ANM-01-008-046}

**Pregunta.** En el ejemplo alternante recíproco, calcula $a_{15}$ y la anchura de $I_5$.

**Solución.** $a_{15}=-1/16$ y $I_5=[-1/16,0]$ tiene anchura $1/16$. Índice, valor y anchura son objetos distintos.

### Microcontrol 047

[]{#MA-MIC-ANM-01-008-047}

[]{#MA-MSOL-ANM-01-008-047}

**Pregunta.** ¿Por qué $K=4$ sirve para $\varepsilon=1/4$ en ese ejemplo?

**Solución.** Porque $w_4=1/8<1/4$. Para todos los $k\ge4$, los términos seleccionados y cero están en $I_4$; no se afirma que cuatro sea el menor umbral.

### Microcontrol 048

[]{#MA-MIC-ANM-01-008-048}

[]{#MA-MSOL-ANM-01-008-048}

**Pregunta.** ¿Demuestra el teorema que toda sucesión acotada converge?

**Solución.** No. Sólo garantiza una selección convergente. $(-1)^n$ es acotada y no converge, aunque sus selecciones de paridad sí convergen.

## §8.7 — De la extracción a los conjuntos

### Microcontrol 049

[]{#MA-MIC-ANM-01-008-049}

[]{#MA-MSOL-ANM-01-008-049}

[]{#MA-SEC-ANM-01-008-007}

**Pregunta.** ¿Por qué de un conjunto infinito se pueden elegir recursivamente valores distintos?

**Solución.** En cada paso se han retirado sólo finitos valores; el resto del conjunto infinito es no vacío. La función de elección fijada permite elegir allí el siguiente.

### Microcontrol 050

[]{#MA-MIC-ANM-01-008-050}

[]{#MA-MSOL-ANM-01-008-050}

**Pregunta.** ¿La sucesión de valores distintos tiene que recorrer todo el conjunto?

**Solución.** No. Basta elegir un subconjunto numerable de valores distintos. La prueba no afirma que el conjunto original sea numerable.

### Microcontrol 051

[]{#MA-MIC-ANM-01-008-051}

[]{#MA-MSOL-ANM-01-008-051}

**Pregunta.** ¿En qué paso se usa la acotación del conjunto?

**Solución.** Para que la sucesión elegida sea acotada y se pueda aplicar Bolzano–Weierstrass.

### Microcontrol 052

[]{#MA-MIC-ANM-01-008-052}

[]{#MA-MSOL-ANM-01-008-052}

**Pregunta.** ¿Por qué a lo sumo un término de la extracción puede ser igual a su límite?

**Solución.** Porque sus valores son dos a dos distintos. Dos términos iguales al límite repetirían un valor.

### Microcontrol 053

[]{#MA-MIC-ANM-01-008-053}

[]{#MA-MSOL-ANM-01-008-053}

**Pregunta.** Si $y_{j_0}=L$, ¿qué sucesión permite evitar el centro?

**Solución.** $z_k=y_{j_0+1+k}$. Todos sus valores difieren de $L$ y conserva el límite por invariancia bajo eliminación de un prefijo finito.

### Microcontrol 054

[]{#MA-MIC-ANM-01-008-054}

[]{#MA-MSOL-ANM-01-008-054}

**Pregunta.** ¿Pertenece cero a $A=\{1/(n+1):n\in\mathbb N\}$? ¿Es punto de acumulación de $A$?

**Solución.** No pertenece porque todos los valores son positivos. Sí es punto de acumulación: para cada $r>0$, arquimedianidad da $0<1/(n+1)<r$ para algún $n$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-008-055}

[]{#MA-MSOL-ANM-01-008-055}

**Pregunta.** ¿Qué añade que el conjunto que contiene los términos sea cerrado?

**Solución.** El límite de una extracción es adherente al conjunto; si éste es cerrado, contiene a todos sus puntos adherentes y por tanto contiene ese límite.

### Microcontrol 056

[]{#MA-MIC-ANM-01-008-056}

[]{#MA-MSOL-ANM-01-008-056}

**Pregunta.** Da un conjunto infinito sin punto de acumulación real y señala la hipótesis que falta.

**Solución.** $\mathbb N\subset\mathbb R$ es infinito y no acotado. Para un centro $x<0$, el radio $-x/2$ da una bola contenida en los negativos, sin naturales. Si $x\in\mathbb N$, el radio $1/2$ excluye todos los naturales distintos de $x$. En el caso restante, $x>0$ no es natural: con $q=\lfloor x\rfloor$ tenemos $q<x<q+1$, y el radio $\min\{x-q,q+1-x\}/2>0$ produce una bola contenida en $(q,q+1)$, sin naturales. Todos los centros quedan excluidos como puntos de acumulación. La hipótesis que falta es acotación.

## §8.8 — Cuándo las extracciones determinan la sucesión

### Microcontrol 057

[]{#MA-MIC-ANM-01-008-057}

[]{#MA-MSOL-ANM-01-008-057}

[]{#MA-SEC-ANM-01-008-008}

**Pregunta.** Escribe la negación de $a_n\to L$ con una tolerancia fija.

**Solución.** Existe $\varepsilon_0>0$ tal que para todo $N\in\mathbb N$ existe $n\ge N$ con $|a_n-L|\ge\varepsilon_0$. La tolerancia no depende de $N$.

### Microcontrol 058

[]{#MA-MIC-ANM-01-008-058}

[]{#MA-MSOL-ANM-01-008-058}

**Pregunta.** ¿Qué propiedad tienen todos los términos de la subsucesión que incumple esa tolerancia?

**Solución.** $|b_k-L|\ge\varepsilon_0$ para todo $k$. El mismo margen se conserva al extraer de nuevo.

### Microcontrol 059

[]{#MA-MIC-ANM-01-008-059}

[]{#MA-MSOL-ANM-01-008-059}

**Pregunta.** ¿Dónde se necesita acotación en la prueba del criterio de destino único?

**Solución.** La subsucesión $b$ hereda la cota y por eso Bolzano–Weierstrass le proporciona una extracción convergente.

### Microcontrol 060

[]{#MA-MIC-ANM-01-008-060}

[]{#MA-MSOL-ANM-01-008-060}

**Pregunta.** ¿Por qué el límite de una extracción de $b$ es punto secuencial de $a$?

**Solución.** La composición de los dos selectores es estrictamente creciente, así que la nueva extracción es una subsucesión de $a$; §8.3 caracteriza su límite como punto secuencial.

### Microcontrol 061

[]{#MA-MIC-ANM-01-008-061}

[]{#MA-MSOL-ANM-01-008-061}

**Pregunta.** ¿Cuál es la contradicción después de identificar ese límite con $L$?

**Solución.** Convergencia exige distancia menor que $\varepsilon_0$ eventualmente, mientras la construcción mantiene distancia al menos $\varepsilon_0$ en cada término.

### Microcontrol 062

[]{#MA-MIC-ANM-01-008-062}

[]{#MA-MSOL-ANM-01-008-062}

**Pregunta.** Para $c_{2j}=0$, $c_{2j+1}=j+1$, ¿qué selección converge a cero?

**Solución.** La par: $c_{2j}=0$ para todo $j$. Su selector $j\mapsto2j$ es estrictamente creciente.

### Microcontrol 063

[]{#MA-MIC-ANM-01-008-063}

[]{#MA-MSOL-ANM-01-008-063}

**Pregunta.** ¿Por qué ese ejemplo no converge a pesar de tener un único punto secuencial?

**Solución.** No es acotado: sus términos impares superan cualquier cota. Toda sucesión convergente es acotada. Para comprobar que $0$ es el único punto secuencial, sea $H\ne0$ y fija $r=\min\{|H|/2,1\}>0$. Elige un natural $K>\max\{0,H+1\}$ y toma el corte $N=2K$. Todo término par tiene valor $0$ y error $|H|>r$. Si $n=2j+1\ge N$, entonces $j\ge K$ y $c_n=j+1\ge K+1>H+r$, por lo que también queda fuera de $B(H,r)$. Esa bola no recibe visitas después de $N$, y $H$ no es punto secuencial. El destino $0$ sí lo es por la selección par.

### Microcontrol 064

[]{#MA-MIC-ANM-01-008-064}

[]{#MA-MSOL-ANM-01-008-064}

**Pregunta.** ¿Qué añade Bolzano–Weierstrass si una sucesión acotada tiene a lo sumo un punto secuencial?

**Solución.** Añade existencia de al menos uno. Junto con «a lo sumo uno» resulta unicidad, y el criterio de la sección da convergencia a ese punto.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html) · [Ejercicios](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-microcontroles.html)
