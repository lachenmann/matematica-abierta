---
content-id: MA-BCH-0269
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-016-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 16
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C16_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §16.1 — Una cubierta dada y una reducción finita

### Microcontrol 001

[]{#MA-MIC-ANM-01-016-001}

[]{#MA-MSOL-ANM-01-016-001}

[]{#MA-SEC-ANM-01-016-001}

**Pregunta.** ¿Qué distingue una cubierta finita particular de la compacidad?

**Solución.** Una cubierta finita particular cubre el conjunto una sola vez; compacidad exige una subcubierta finita dentro de toda cubierta abierta dada. La familia $\{\mathbb R\}$ cubre finitamente cualquier conjunto, incluso los no compactos.

### Microcontrol 002

[]{#MA-MIC-ANM-01-016-002}

[]{#MA-MSOL-ANM-01-016-002}

**Pregunta.** ¿Qué debe conservar una subcubierta de $(U_i)_{i\in I}$?

**Solución.** Miembros de la familia original y cobertura de todos los puntos de $K$. Se restringe a índices $J\subseteq I$ finitos; no se reemplazan abiertos por otros nuevos.

### Microcontrol 003

[]{#MA-MIC-ANM-01-016-003}

[]{#MA-MSOL-ANM-01-016-003}

**Pregunta.** ¿La cobertura $\forall x\in K\;\exists i:x\in U_i$ ya da una función de índices por punto?

**Solución.** No. Asegura un testigo para cada punto considerado, pero no construye una selección simultánea $x\mapsto i_x$. Las pruebas usan sólo los testigos concretos que necesitan.

### Microcontrol 004

[]{#MA-MIC-ANM-01-016-004}

[]{#MA-MSOL-ANM-01-016-004}

**Pregunta.** ¿Cómo se cubre finitamente el vacío dentro de cualquier cubierta?

**Solución.** Tomando el conjunto vacío de índices. Su unión es vacía y contiene al conjunto vacío, incluso si la cubierta original no tiene índices.

### Microcontrol 005

[]{#MA-MIC-ANM-01-016-005}

[]{#MA-MSOL-ANM-01-016-005}

**Pregunta.** ¿Por qué una cubierta arbitraria de un singleton tiene subcubierta finita?

**Solución.** La cobertura del único punto $a$ da un índice $i$ con $a\in U_i$. El singleton de índices $\{i\}$ cubre todo $\{a\}$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-016-006}

[]{#MA-MSOL-ANM-01-016-006}

**Pregunta.** ¿Cómo se combinan dos subcubiertas finitas para cubrir una unión de compactos?

**Solución.** La cubierta de la unión cubre cada pieza. Cada compacto da un conjunto finito de índices y su unión, también finita, cubre ambas piezas.

### Microcontrol 007

[]{#MA-MIC-ANM-01-016-007}

[]{#MA-MSOL-ANM-01-016-007}

**Pregunta.** ¿Por qué $U_n=(-(n+1),n+1)$ no tiene una subcubierta finita de la recta?

**Solución.** Los índices de una subfamilia finita no vacía tienen máximo $m$, y todos los abiertos seleccionados están en $U_m$. El punto $m+2$ queda fuera. La familia vacía tampoco cubre la recta.

### Microcontrol 008

[]{#MA-MIC-ANM-01-016-008}

[]{#MA-MSOL-ANM-01-016-008}

**Pregunta.** ¿El ínfimo de una familia infinita de radios positivos tiene que ser positivo?

**Solución.** No. $r_n=1/(n+1)>0$ para todo $n$, pero $\inf_n r_n=0$. Un mínimo positivo se garantiza aquí sólo para una familia finita no vacía de valores positivos.

## §16.2 — El supremo prolonga los segmentos cubiertos

### Microcontrol 009

[]{#MA-MIC-ANM-01-016-009}

[]{#MA-MSOL-ANM-01-016-009}

[]{#MA-SEC-ANM-01-016-002}

**Pregunta.** ¿Qué registra el conjunto $S$ en la prueba de compacidad de $[a,b]$?

**Solución.** Los $x\in[a,b]$ para los que el segmento $[a,x]$ admite alguna subcubierta finita de la cubierta dada. Registra existencia, sin elegir una subcubierta para cada $x$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-016-010}

[]{#MA-MSOL-ANM-01-016-010}

**Pregunta.** ¿Por qué $S$ es no vacío y acotado superiormente?

**Solución.** $a\in S$ porque un solo abierto que cubre $a$ cubre $[a,a]$. Además $S\subseteq[a,b]$, así $b$ es cota superior.

### Microcontrol 011

[]{#MA-MIC-ANM-01-016-011}

[]{#MA-MSOL-ANM-01-016-011}

**Pregunta.** ¿Qué proporciona la apertura de un miembro que contiene $c=\sup S$?

**Solución.** Un radio $r>0$ con $(c-r,c+r)\subseteq U_{i_c}$. Ese margen permitirá ampliar una cobertura finita que llegue a un $t$ suficientemente próximo a $c$.

### Microcontrol 012

[]{#MA-MIC-ANM-01-016-012}

[]{#MA-MSOL-ANM-01-016-012}

**Pregunta.** ¿Por qué existe $t\in S$ con $c-r/2<t\le c$?

**Solución.** Porque $c-r/2<c$ no puede ser cota superior de $S$. La negación de ser cota produce un $t\in S$ mayor, y $t\le c$ por ser $c$ cota.

### Microcontrol 013

[]{#MA-MIC-ANM-01-016-013}

[]{#MA-MSOL-ANM-01-016-013}

**Pregunta.** ¿Qué impide que $d=\min(b,c+r/2)$ salga del segmento?

**Solución.** La fórmula da $c\le d\le b$, y $c\ge a$. Así $d\in[a,b]$, a la vez que todo $[t,d]$ queda dentro de la bola de radio $r$ alrededor de $c$.

### Microcontrol 014

[]{#MA-MIC-ANM-01-016-014}

[]{#MA-MSOL-ANM-01-016-014}

**Pregunta.** ¿Por qué $J_t\cup\{i_c\}$ cubre $[a,d]$?

**Solución.** $J_t$ cubre $[a,t]$ y $U_{i_c}$ cubre $[t,d]$. Como $a\le t\le d$, la unión de esos dos segmentos es $[a,d]$; los índices siguen siendo finitos.

### Microcontrol 015

[]{#MA-MIC-ANM-01-016-015}

[]{#MA-MSOL-ANM-01-016-015}

**Pregunta.** ¿De $\sup S=b$ se deduce siempre $b\in S$?

**Solución.** No. $S=[a,b)$ con $a<b$ tiene supremo $b$ pero no lo contiene. En R2 se obtiene además $d\in S$ y, una vez $c=b$, $d=b$, lo que sí prueba pertenencia.

### Microcontrol 016

[]{#MA-MIC-ANM-01-016-016}

[]{#MA-MSOL-ANM-01-016-016}

**Pregunta.** ¿Qué cambia para $a=b$ o para $a>b$?

**Solución.** Si $a=b$, el segmento es singleton y basta un abierto que cubra ese punto. Con $a>b$, la notación de intervalo describe el vacío, compacto por la subfamilia vacía.

## §16.3 — Heredar compacidad sin perder índices

### Microcontrol 017

[]{#MA-MIC-ANM-01-016-017}

[]{#MA-MSOL-ANM-01-016-017}

[]{#MA-SEC-ANM-01-016-003}

**Pregunta.** ¿Qué representación se usa para un cerrado relativo $A\subseteq K$?

**Solución.** $A=K\cap F$ con $F$ cerrado en toda la recta. Su complemento ambiental $\mathbb R\setminus F$ es abierto y cubre los puntos de $K$ que no están en $A$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-016-018}

[]{#MA-MSOL-ANM-01-016-018}

**Pregunta.** ¿Por qué se añade todo $\mathbb R\setminus F$ a la cubierta de $A$?

**Solución.** Para cubrir cada punto de $K\setminus A$. Añadir sólo una porción próxima a un extremo podría dejar puntos de ese complemento sin cubrir.

### Microcontrol 019

[]{#MA-MIC-ANM-01-016-019}

[]{#MA-MSOL-ANM-01-016-019}

**Pregunta.** ¿Para qué sirve etiquetar el índice nuevo de la cubierta ampliada?

**Solución.** Para que sea distinto de todos los originales, aunque algún valor de abierto coincida. Así se puede retirar el índice añadido sin perder la procedencia de los miembros originales.

### Microcontrol 020

[]{#MA-MIC-ANM-01-016-020}

[]{#MA-MSOL-ANM-01-016-020}

**Pregunta.** ¿Por qué el abierto añadido no es necesario para cubrir puntos de $A$?

**Solución.** Todo $x\in A$ está en $F$, así no pertenece a $\mathbb R\setminus F$. En una subcubierta ampliada debe estar cubierto por algún índice original.

### Microcontrol 021

[]{#MA-MIC-ANM-01-016-021}

[]{#MA-MSOL-ANM-01-016-021}

**Pregunta.** ¿Todo subconjunto de un compacto es compacto?

**Solución.** No. $(0,1)\subseteq[0,1]$ no lo es. La cubierta $U_n=(1/(n+2),2)$ cubre el intervalo abierto pero ninguna subfamilia finita lo cubre.

### Microcontrol 022

[]{#MA-MIC-ANM-01-016-022}

[]{#MA-MSOL-ANM-01-016-022}

**Pregunta.** ¿Qué punto queda fuera de una subfamilia finita de esa cubierta, con índice máximo $m$?

**Solución.** $x=1/(2(m+2))$ pertenece a $(0,1)$ y es menor que el extremo izquierdo $1/(m+2)$ del mayor abierto seleccionado. Está fuera de toda la unión finita.

### Microcontrol 023

[]{#MA-MIC-ANM-01-016-023}

[]{#MA-MSOL-ANM-01-016-023}

**Pregunta.** ¿Es compacta la intersección de un compacto con un cerrado real?

**Solución.** Sí. Es cerrada relativa al compacto por la representación como intersección, y R3 transmite compacidad.

### Microcontrol 024

[]{#MA-MIC-ANM-01-016-024}

[]{#MA-MSOL-ANM-01-016-024}

**Pregunta.** ¿La herencia de compacidad exige que el cerrado relativo sea intervalo?

**Solución.** No. Sólo exige cerrado relativo. Por ejemplo $[-2,-1]\cup[1,2]$ es un cerrado relativo del compacto $[-2,2]$ y es compacto aunque tenga un hueco.

## §16.4 — Heine–Borel: cerrar las dos direcciones

### Microcontrol 025

[]{#MA-MIC-ANM-01-016-025}

[]{#MA-MSOL-ANM-01-016-025}

[]{#MA-SEC-ANM-01-016-004}

**Pregunta.** ¿Qué dos propiedades identifica Heine–Borel con la compacidad real?

**Solución.** Cerradura en $\mathbb R$ y acotación. Se demuestran ambas necesidades por cubiertas y la suficiencia por segmento compacto y herencia a un cerrado relativo.

### Microcontrol 026

[]{#MA-MIC-ANM-01-016-026}

[]{#MA-MSOL-ANM-01-016-026}

**Pregunta.** ¿En qué momento se toma el máximo de índices para probar acotación?

**Solución.** Después de obtener una subcubierta finita de $U_n=(-(n+1),n+1)$. Para $K$ no vacío sus índices no son vacíos y tienen máximo; no se toma máximo de toda $\mathbb N$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-016-027}

[]{#MA-MSOL-ANM-01-016-027}

**Pregunta.** ¿Por qué $V_n=\{x:|x-p|>1/(n+1)\}$ es abierto real?

**Solución.** Es la unión de los rayos $(-\infty,p-1/(n+1))$ y $(p+1/(n+1),\infty)$, ambos abiertos.

### Microcontrol 028

[]{#MA-MIC-ANM-01-016-028}

[]{#MA-MSOL-ANM-01-016-028}

**Pregunta.** ¿Por qué los $V_n$ cubren $K$ cuando $p\notin K$?

**Solución.** Para cada $x\in K$, su distancia positiva $|x-p|$ supera algún recíproco $1/(n+1)$ por arquimedianidad. Entonces $x\in V_n$.

### Microcontrol 029

[]{#MA-MIC-ANM-01-016-029}

[]{#MA-MSOL-ANM-01-016-029}

**Pregunta.** ¿Qué radio exterior se obtiene del máximo $m$ de una subcubierta de $V_n$?

**Solución.** $1/(m+1)>0$. Como $K\subseteq V_m$, ningún punto a distancia menor que ese radio de $p$ está en $K$. Da una bola dentro del complemento.

### Microcontrol 030

[]{#MA-MIC-ANM-01-016-030}

[]{#MA-MSOL-ANM-01-016-030}

**Pregunta.** ¿Cómo se prueba compacidad de un cerrado acotado sin sucesiones?

**Solución.** Se encierra en $[-M,M]$, compacto por R2. El conjunto es cerrado relativo a ese segmento y R3 lo hace compacto.

### Microcontrol 031

[]{#MA-MIC-ANM-01-016-031}

[]{#MA-MSOL-ANM-01-016-031}

**Pregunta.** ¿Compacidad y conexidad coinciden en la recta?

**Solución.** No. $[-2,-1]\cup[1,2]$ es compacto y no conexo. $(0,1)$ es conexo y no compacto. Las condiciones de cubierta y ausencia de huecos son distintas.

### Microcontrol 032

[]{#MA-MIC-ANM-01-016-032}

[]{#MA-MSOL-ANM-01-016-032}

**Pregunta.** ¿Por qué añadir cero a los recíprocos restaura compacidad?

**Solución.** El conjunto resultante es acotado y cerrado: cero incluye el punto de acumulación de la cola, y todo punto exterior se separa de una cola lejana y de un prefijo finito por un radio positivo. Heine–Borel da compacidad.

## §16.5 — Sucesiones: extraer y seleccionar son tareas distintas

### Microcontrol 033

[]{#MA-MIC-ANM-01-016-033}

[]{#MA-MSOL-ANM-01-016-033}

[]{#MA-SEC-ANM-01-016-005}

**Pregunta.** ¿Dónde debe quedar el límite en la definición de compacidad secuencial?

**Solución.** Dentro de $K$, no sólo en $\mathbb R$. Una subsucesión convergente a un punto exterior no satisface la definición.

### Microcontrol 034

[]{#MA-MIC-ANM-01-016-034}

[]{#MA-MSOL-ANM-01-016-034}

**Pregunta.** ¿Qué aporta Bolzano–Weierstrass de C08 para una sucesión dada en un compacto?

**Solución.** Como está acotada, aporta una subsucesión convergente en $\mathbb R$. La cerradura del compacto es el paso adicional que coloca el límite en $K$.

### Microcontrol 035

[]{#MA-MIC-ANM-01-016-035}

[]{#MA-MSOL-ANM-01-016-035}

**Pregunta.** ¿Por qué la dirección compacta a secuencialmente compacta no fabrica una ruta por selección?

**Solución.** La sucesión de entrada ya está dada. C08 extrae índices de esa sucesión y después se usa cerradura; no se escoge un punto de cada uno de infinitos conjuntos arbitrarios.

### Microcontrol 036

[]{#MA-MIC-ANM-01-016-036}

[]{#MA-MSOL-ANM-01-016-036}

**Pregunta.** ¿Por qué $1/(n+1)$ refuta compacidad secuencial de $(0,1]$?

**Solución.** Toda subsucesión también converge a cero, que no pertenece al dominio. Por unicidad no puede tener otro límite dentro de $(0,1]$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-016-037}

[]{#MA-MSOL-ANM-01-016-037}

**Pregunta.** ¿Qué familia se usa si un secuencialmente compacto fuera no acotado?

**Solución.** $E_n=\{x\in K:|x|>n\}$, todos no vacíos. Fabricar una sucesión $x_n\in E_n$ requiere aquí CC(R), o una enumeración dada que permita mínimos de índices.

### Microcontrol 038

[]{#MA-MIC-ANM-01-016-038}

[]{#MA-MSOL-ANM-01-016-038}

**Pregunta.** ¿Qué familia se usa si hay un punto adherente $p\notin K$?

**Solución.** $F_n=K\cap(p-1/(n+1),p+1/(n+1))$, todos no vacíos. Una selección simultánea da una ruta hacia $p$, y después compacidad secuencial y unicidad llevan a contradicción.

### Microcontrol 039

[]{#MA-MIC-ANM-01-016-039}

[]{#MA-MSOL-ANM-01-016-039}

**Pregunta.** ¿Cómo una sobreyección dada $e:\mathbb N\to K$ reemplaza ese gasto de selección?

**Solución.** Para cada conjunto requerido se toma el menor índice $j$ con $e(j)$ en él. Existe por sobreyectividad y no vacuidad; el buen orden natural determina un valor único. No se inventa una enumeración de $K$.

### Microcontrol 040

[]{#MA-MIC-ANM-01-016-040}

[]{#MA-MSOL-ANM-01-016-040}

**Pregunta.** ¿Cuál es el alcance de la recíproca secuencial demostrada?

**Solución.** Para dominios reales arbitrarios se establece bajo CC(R) explícita, local al enunciado. También se demuestra sin esa hipótesis extra cuando el dominio no vacío viene con enumeración sobreyectiva dada. El vacío se trata por separado.

## §16.6 — La continuidad lleva compactos a compactos

### Microcontrol 041

[]{#MA-MIC-ANM-01-016-041}

[]{#MA-MSOL-ANM-01-016-041}

[]{#MA-SEC-ANM-01-016-006}

**Pregunta.** ¿Qué ambiente tienen las preimágenes $A_i$ de una cubierta de la imagen?

**Solución.** Son abiertas relativas al dominio restringido $K$, por continuidad de $f\upharpoonright K$. No se afirma que sean abiertas en toda $\mathbb R$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-016-042}

[]{#MA-MSOL-ANM-01-016-042}

**Pregunta.** ¿Qué fórmula levanta esas preimágenes a abiertos reales?

**Solución.** $W_i=(\mathbb R\setminus K)\cup A_i$. La cerradura de $K$ y la apertura relativa de $A_i$ prueban apertura real de cada $W_i$.

### Microcontrol 043

[]{#MA-MIC-ANM-01-016-043}

[]{#MA-MSOL-ANM-01-016-043}

**Pregunta.** ¿Por qué un punto de $A_i$ tiene una vecindad real dentro de $W_i$?

**Solución.** Para ese índice, $A_i=K\cap O$ con $O$ abierto real. Todo punto de $O$ está fuera de $K$ o en $A_i$, así $O\subseteq W_i$ y da la vecindad del punto.

### Microcontrol 044

[]{#MA-MIC-ANM-01-016-044}

[]{#MA-MSOL-ANM-01-016-044}

**Pregunta.** ¿Se eligió una familia de abiertos ambientes $O_i$?

**Solución.** No. La familia $W_i$ se define directamente por fórmula única. Un ambiente $O$ se usa sólo para probar apertura en el índice considerado, sin reunir elecciones simultáneas.

### Microcontrol 045

[]{#MA-MIC-ANM-01-016-045}

[]{#MA-MSOL-ANM-01-016-045}

**Pregunta.** ¿Qué identidad permite devolver una subcubierta finita a las salidas?

**Solución.** $K\cap W_i=A_i$. Si $x\in K$ está cubierto por $W_i$, pertenece a la preimagen $A_i$ y su salida está en $V_i$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-016-046}

[]{#MA-MSOL-ANM-01-016-046}

**Pregunta.** ¿Se necesita una inversa funcional para cubrir cada salida de $f[K]$?

**Solución.** No. Para cada salida fijada, pertenencia a la imagen garantiza una entrada testigo. Se obtiene un índice finito que cubre esa entrada y por ello la salida.

### Microcontrol 047

[]{#MA-MIC-ANM-01-016-047}

[]{#MA-MSOL-ANM-01-016-047}

**Pregunta.** ¿La imagen compacta de una continua implica dominio compacto?

**Solución.** No. Una constante en $\mathbb R$ tiene imagen singleton compacta, pero $\mathbb R$ no es compacto.

### Microcontrol 048

[]{#MA-MIC-ANM-01-016-048}

[]{#MA-MSOL-ANM-01-016-048}

**Pregunta.** ¿La preimagen de un compacto por una continua siempre es compacta?

**Solución.** No. Para la constante cero en $\mathbb R$, la preimagen del singleton compacto $\{0\}$ es toda la recta. Hace falta información adicional del dominio.

## §16.7 — Por qué los extremos llegan a alcanzarse

### Microcontrol 049

[]{#MA-MIC-ANM-01-016-049}

[]{#MA-MSOL-ANM-01-016-049}

[]{#MA-SEC-ANM-01-016-007}

**Pregunta.** ¿Qué diferencia hay entre supremo de una imagen y máximo alcanzado?

**Solución.** El supremo es la menor cota superior; ser máximo exige además pertenecer a la imagen. La identidad en $(0,1)$ tiene supremo $1$ pero no lo alcanza.

### Microcontrol 050

[]{#MA-MIC-ANM-01-016-050}

[]{#MA-MSOL-ANM-01-016-050}

**Pregunta.** ¿Por qué el supremo de un compacto no vacío pertenece al conjunto?

**Solución.** Si quedara fuera, cerradura daría una bola exterior; la propiedad aproximante del supremo daría un punto del conjunto dentro de esa bola, contradicción.

### Microcontrol 051

[]{#MA-MIC-ANM-01-016-051}

[]{#MA-MSOL-ANM-01-016-051}

**Pregunta.** ¿Cómo se prueba la pertenencia del ínfimo sin seleccionar una sucesión?

**Solución.** Si $m$ estuviera fuera, una bola de radio $s$ no tocaría el conjunto. Como $m+s/2$ no es cota inferior, existe un punto entre $m$ y $m+s/2$ del conjunto, que invade esa bola.

### Microcontrol 052

[]{#MA-MIC-ANM-01-016-052}

[]{#MA-MSOL-ANM-01-016-052}

**Pregunta.** ¿Dónde se usa que el dominio de Weierstrass sea no vacío?

**Solución.** Para que la imagen sea no vacía y admita supremo/ínfimo reales como extremos, y para que existan entradas minimizadoras y maximizadoras. El vacío compacto no tiene esas entradas.

### Microcontrol 053

[]{#MA-MIC-ANM-01-016-053}

[]{#MA-MSOL-ANM-01-016-053}

**Pregunta.** ¿Weierstrass obliga a que los puntos extremos sean extremos del dominio?

**Solución.** No. $(x-1)^2$ en $[0,3]$ tiene mínimo en el punto interior $1$. Se garantizan puntos que alcanzan los valores globales, no una posición prefijada.

### Microcontrol 054

[]{#MA-MIC-ANM-01-016-054}

[]{#MA-MSOL-ANM-01-016-054}

**Pregunta.** ¿Puede haber varios minimizadores y maximizadores?

**Solución.** Sí. Para $x^2$ en $\{-1,1\}$ ambas entradas dan $1$, de modo que ambos puntos minimizan y maximizan.

### Microcontrol 055

[]{#MA-MIC-ANM-01-016-055}

[]{#MA-MSOL-ANM-01-016-055}

**Pregunta.** ¿Qué añade conexidad a la imagen compacta de un segmento?

**Solución.** C15 dice que es intervalo; C16 da extremos globales alcanzados $m,M$. Juntas las propiedades identifican la imagen como $[m,M]$, sin atribuir esos valores a los extremos del dominio.

### Microcontrol 056

[]{#MA-MIC-ANM-01-016-056}

[]{#MA-MSOL-ANM-01-016-056}

**Pregunta.** ¿Una función acotada en $[0,1]$ tiene máximo aunque no sea continua?

**Solución.** No necesariamente. Si vale $x$ para $x<1$ y cero en $1$, su imagen es $[0,1)$ y no tiene máximo. La función es discontinua en el extremo $1$.

## §16.8 — Márgenes positivos e inversas sobre compactos

### Microcontrol 057

[]{#MA-MIC-ANM-01-016-057}

[]{#MA-MSOL-ANM-01-016-057}

[]{#MA-SEC-ANM-01-016-008}

**Pregunta.** ¿Qué función recibe Weierstrass para obtener un margen positivo de una continua sin ceros?

**Solución.** $|f|$, continua por C14. Su mínimo se alcanza en $x_0\in K$ y vale $|f(x_0)|>0$ porque no hay ceros.

### Microcontrol 058

[]{#MA-MIC-ANM-01-016-058}

[]{#MA-MSOL-ANM-01-016-058}

**Pregunta.** ¿Qué cota da ese margen $m>0$ al recíproco?

**Solución.** $|1/f(x)|=1/|f(x)|\le1/m$ para todos los puntos del compacto. No ceros asegura que el recíproco esté definido en todo el dominio.

### Microcontrol 059

[]{#MA-MIC-ANM-01-016-059}

[]{#MA-MSOL-ANM-01-016-059}

**Pregunta.** ¿Una función positiva en $(0,1]$ tiene siempre cota inferior positiva?

**Solución.** No. La identidad es positiva pero sus valores $1/(n+1)$ tienden a cero. El dominio no es compacto; falta la hipótesis que garantiza alcanzar un mínimo positivo.

### Microcontrol 060

[]{#MA-MIC-ANM-01-016-060}

[]{#MA-MSOL-ANM-01-016-060}

**Pregunta.** ¿Qué función proporciona un punto del compacto más próximo a un real $p$?

**Solución.** $x\mapsto|x-p|$, continua. Weierstrass da un minimizador; si $p$ está fuera de $K$, el mínimo alcanzado no puede ser cero y es positivo.

### Microcontrol 061

[]{#MA-MIC-ANM-01-016-061}

[]{#MA-MSOL-ANM-01-016-061}

**Pregunta.** ¿El punto más próximo tiene que ser único?

**Solución.** No. Para $K=\{-1,1\}$ y $p=0$, ambos puntos tienen distancia mínima $1$. Se garantiza existencia, no una selección única.

### Microcontrol 062

[]{#MA-MIC-ANM-01-016-062}

[]{#MA-MSOL-ANM-01-016-062}

**Pregunta.** ¿Por qué la fibra de un valor por una continua en un compacto es compacta?

**Solución.** El singleton de salida es cerrado real, su preimagen es cerrada relativa al compacto por C14 y R3 la hace compacta. Se incluye la fibra vacía.

### Microcontrol 063

[]{#MA-MIC-ANM-01-016-063}

[]{#MA-MSOL-ANM-01-016-063}

**Pregunta.** ¿Qué identidad demuestra continuidad de la inversa de una inyección continua compacta?

**Solución.** Para todo cerrado relativo $A\subseteq K$, $h^{-1}[A]=f[A]$. El conjunto $A$ es compacto, su imagen también y por ello es cerrada relativa a $H=f[K]$. El criterio de preimágenes cerradas de C14 da continuidad de $h$.

### Microcontrol 064

[]{#MA-MIC-ANM-01-016-064}

[]{#MA-MSOL-ANM-01-016-064}

**Pregunta.** ¿La prueba de esa inversa necesita intervalo o continuidad uniforme?

**Solución.** No. Usa compacidad de cerrados relativos, imagen compacta y criterio de continuidad por cerrados. Puede haber un dominio roto; continuidad uniforme/Heine–Cantor quedan para C17.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)
