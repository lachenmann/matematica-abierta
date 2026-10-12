---
content-id: MA-BCH-0265
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-015-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 15
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C15_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Ejercicios](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §15.1 — Qué tendría que hacer una separación

### Microcontrol 001

[]{#MA-MIC-ANM-01-015-001}

[]{#MA-MSOL-ANM-01-015-001}

[]{#MA-SEC-ANM-01-015-001}

**Pregunta.** ¿Qué cuatro condiciones conjuntistas acompañan la apertura relativa en una separación?

**Solución.** No vacuidad de ambas partes, disjunción, cobertura del conjunto y pertenencia de las partes al conjunto ambiente. Junto a la apertura relativa, se escriben $A,B\subseteq E$, $A,B\ne\varnothing$, $A\cap B=\varnothing$, $A\cup B=E$.

### Microcontrol 002

[]{#MA-MIC-ANM-01-015-002}

[]{#MA-MSOL-ANM-01-015-002}

**Pregunta.** ¿Por qué $[-2,-1]$ puede ser una parte abierta relativa de $[-2,-1]\cup[1,2]$?

**Solución.** Es la intersección del ambiente con el abierto real $(-\infty,0)$. La apertura se mide dentro del ambiente, aunque el segmento no sea abierto real.

### Microcontrol 003

[]{#MA-MIC-ANM-01-015-003}

[]{#MA-MSOL-ANM-01-015-003}

**Pregunta.** ¿Dónde falla la partición $[-1,0)$ y $[0,1]$ de $[-1,1]$?

**Solución.** La segunda parte no es abierta relativa en cero: dado $r>0$, $-\min(r/2,1/2)$ pertenece al ambiente, dista menos que $r$ de cero y no pertenece a $[0,1]$.

### Microcontrol 004

[]{#MA-MIC-ANM-01-015-004}

[]{#MA-MSOL-ANM-01-015-004}

**Pregunta.** ¿Qué complemento convierte una parte abierta y cerrada relativa en una separación candidata?

**Solución.** $E\setminus A$. Si $A$ es propia y no vacía, el complemento también es no vacío; la cerradura relativa de $A$ significa que ese complemento es abierto relativo. Disjunción y cobertura son identidades de complementos.

### Microcontrol 005

[]{#MA-MIC-ANM-01-015-005}

[]{#MA-MSOL-ANM-01-015-005}

**Pregunta.** ¿El vacío es conexo bajo la definición adoptada?

**Solución.** Sí. Toda parte del vacío es vacía, y no pueden existir las dos partes no vacías exigidas por una separación.

### Microcontrol 006

[]{#MA-MIC-ANM-01-015-006}

[]{#MA-MSOL-ANM-01-015-006}

**Pregunta.** ¿Hace falta que un singleton sea abierto real para probar que es conexo?

**Solución.** No. Sus únicos subconjuntos son el vacío y él mismo; no admite dos partes disjuntas no vacías. La apertura real del singleton no interviene.

### Microcontrol 007

[]{#MA-MIC-ANM-01-015-007}

[]{#MA-MSOL-ANM-01-015-007}

**Pregunta.** ¿Basta dibujar una partición de dos colores para negar conexidad?

**Solución.** No. Hay que demostrar apertura relativa de ambas partes y verificar no vacuidad, disjunción y cobertura. Una frontera mal asignada puede impedir la apertura de una parte.

### Microcontrol 008

[]{#MA-MIC-ANM-01-015-008}

[]{#MA-MSOL-ANM-01-015-008}

**Pregunta.** ¿Qué niega exactamente la afirmación «$E$ es conexo»?

**Solución.** Niega la existencia de cualquier par que satisfaga todas las condiciones de separación; no niega la existencia de particiones arbitrarias. Un intervalo sí admite particiones, pero ninguna con ambas partes abiertas relativas y no vacías.

## §15.2 — El supremo impide romper un intervalo

### Microcontrol 009

[]{#MA-MIC-ANM-01-015-009}

[]{#MA-MSOL-ANM-01-015-009}

[]{#MA-SEC-ANM-01-015-002}

**Pregunta.** ¿Qué definición de intervalo incluye las semirrectas y el vacío?

**Solución.** La condición $a,b\in I$, $a\le b\Rightarrow[a,b]\subseteq I$. En el vacío no hay pares y la condición es vacía; en una semirrecta todo punto entre dos miembros satisface la misma desigualdad que define la semirrecta.

### Microcontrol 010

[]{#MA-MIC-ANM-01-015-010}

[]{#MA-MSOL-ANM-01-015-010}

**Pregunta.** ¿Por qué $S=A\cap[a,b]$ tiene supremo en la prueba R2?

**Solución.** Contiene $a$ y está acotado superiormente por $b$. La completitud real da un supremo para todo conjunto real no vacío acotado superiormente.

### Microcontrol 011

[]{#MA-MIC-ANM-01-015-011}

[]{#MA-MSOL-ANM-01-015-011}

**Pregunta.** ¿Dónde se usa que el dominio sea intervalo para ubicar la frontera $c$?

**Solución.** De $a\le c\le b$ y $a,b\in I$ se deduce $c\in[a,b]\subseteq I$. Sin esa inclusión la cobertura por las dos partes no permitiría asignar $c$ a una de ellas.

### Microcontrol 012

[]{#MA-MIC-ANM-01-015-012}

[]{#MA-MSOL-ANM-01-015-012}

**Pregunta.** Si $c\in A$, ¿por qué $b-c$ es positivo?

**Solución.** $b\in B$ y la disjunción impiden $c=b$; además $c\le b$ por la cota del supremo. Por tanto $c<b$.

### Microcontrol 013

[]{#MA-MIC-ANM-01-015-013}

[]{#MA-MSOL-ANM-01-015-013}

**Pregunta.** ¿Qué dos controles satisface $h=\min((b-c)/2,r/2)$?

**Solución.** Es positivo, no avanza hasta $b$ y es menor que $r$. Así $c+h$ pertenece al segmento original y a la vecindad relativa de $c$; ambas pertenencias son necesarias para concluir que está en $A$.

### Microcontrol 014

[]{#MA-MIC-ANM-01-015-014}

[]{#MA-MSOL-ANM-01-015-014}

**Pregunta.** Si $c\in B$, ¿por qué existe $t\in S$ mayor que $c-s/2$?

**Solución.** El número $c-s/2<c$ no puede ser cota superior de $S$, pues $c$ es la menor cota superior. La negación de ser cota da un $t\in S$ con $t>c-s/2$, y $t\le c$ por ser $c$ cota.

### Microcontrol 015

[]{#MA-MIC-ANM-01-015-015}

[]{#MA-MSOL-ANM-01-015-015}

**Pregunta.** ¿Se supone en R2 que $c$ sea máximo de $S$?

**Solución.** No. Si $c$ está en $B$, ni siquiera pertenece a $S\subseteq A$. Se usa la aproximación por debajo del supremo, no la existencia de un máximo.

### Microcontrol 016

[]{#MA-MIC-ANM-01-015-016}

[]{#MA-MSOL-ANM-01-015-016}

**Pregunta.** ¿Se necesita compacidad del intervalo original para R2?

**Solución.** No. Se acota sólo el auxiliar $S$ entre dos puntos concretos. Supremo, propiedad intervalar y apertura relativa bastan, incluso para intervalos no acotados.

## §15.3 — Un hueco produce dos lados

### Microcontrol 017

[]{#MA-MIC-ANM-01-015-017}

[]{#MA-MSOL-ANM-01-015-017}

[]{#MA-SEC-ANM-01-015-003}

**Pregunta.** ¿Qué omisión permite construir un corte que separa un conjunto?

**Solución.** Un $c\notin E$ situado estrictamente entre dos puntos $a<b$ de $E$. Una omisión fuera de todos sus puntos no asegura dos partes no vacías.

### Microcontrol 018

[]{#MA-MIC-ANM-01-015-018}

[]{#MA-MSOL-ANM-01-015-018}

**Pregunta.** ¿Por qué las partes $E\cap(-\infty,c)$ y $E\cap(c,\infty)$ cubren $E$?

**Solución.** Como $c\notin E$, todo $x\in E$ es distinto de $c$. La tricotomía deja sólo $x<c$ o $x>c$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-015-019}

[]{#MA-MSOL-ANM-01-015-019}

**Pregunta.** ¿Qué testigos aseguran la no vacuidad de ambos lados del corte?

**Solución.** Los puntos dados $a<c<b$: $a$ está en el lado izquierdo y $b$ en el derecho.

### Microcontrol 020

[]{#MA-MIC-ANM-01-015-020}

[]{#MA-MSOL-ANM-01-015-020}

**Pregunta.** ¿La densidad de $\mathbb Q$ implica su conexidad?

**Solución.** No. $\sqrt2$ es un punto real entre $1$ y $2$ que no es racional. Los racionales menores y mayores que ese corte forman una separación; aproximarse al corte no lo incluye en el dominio.

### Microcontrol 021

[]{#MA-MIC-ANM-01-015-021}

[]{#MA-MSOL-ANM-01-015-021}

**Pregunta.** ¿Por qué una intersección de intervalos es intervalo?

**Solución.** Si $a,b$ pertenecen a todos los miembros, cada miembro contiene $[a,b]$, luego la intersección también lo contiene. Si la intersección es vacía, la condición entre pares se cumple vacíamente.

### Microcontrol 022

[]{#MA-MIC-ANM-01-015-022}

[]{#MA-MSOL-ANM-01-015-022}

**Pregunta.** ¿Qué ocurre al unir $(0,1)$ y $(2,3)$?

**Solución.** La unión omite, por ejemplo, $3/2$ entre los puntos presentes $1/2$ y $5/2$. No es intervalo y por R3 no es conexa.

### Microcontrol 023

[]{#MA-MIC-ANM-01-015-023}

[]{#MA-MSOL-ANM-01-015-023}

**Pregunta.** ¿Por qué un punto común ayuda a unir dos conexos?

**Solución.** En una supuesta separación de la unión, cada conexo debe quedar en una sola parte. El punto común obliga a que ambos queden en la misma, dejando vacía la otra parte.

### Microcontrol 024

[]{#MA-MIC-ANM-01-015-024}

[]{#MA-MSOL-ANM-01-015-024}

**Pregunta.** ¿La intersección no vacía es necesaria para que dos intervalos tengan unión conexa?

**Solución.** No. $[0,1)$ y $[1,2]$ son disjuntos, pero su unión es $[0,2]$, que es intervalo y conexo. La condición de punto común es suficiente, no necesaria.

## §15.4 — La continuidad transporta la imposibilidad de separar

### Microcontrol 025

[]{#MA-MIC-ANM-01-015-025}

[]{#MA-MSOL-ANM-01-015-025}

[]{#MA-SEC-ANM-01-015-004}

**Pregunta.** ¿Qué operación de conjuntos usa la continuidad para transportar una separación de la imagen?

**Solución.** Preimágenes. Si las partes de la imagen son $H\cap V$ y $H\cap W$, sus preimágenes por $h:E\to\mathbb R$ son $h^{-1}[V]$ y $h^{-1}[W]$, abiertas relativas a $E$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-015-026}

[]{#MA-MSOL-ANM-01-015-026}

**Pregunta.** ¿Por qué se restringe $f$ al conexo $E\subseteq D$?

**Solución.** Así la función $h=f\upharpoonright E$ tiene exactamente el ambiente de entradas que queremos separar. Su continuidad se hereda de $f$ y su imagen es $f[E]$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-015-027}

[]{#MA-MSOL-ANM-01-015-027}

**Pregunta.** ¿Qué garantiza que la preimagen de una parte no vacía de $f[E]$ sea no vacía?

**Solución.** Que sus valores pertenecen a la imagen: para un valor concreto $y$ de esa parte existe $x\in E$ con $f(x)=y$. No bastaría que $y$ perteneciera solamente al codominio.

### Microcontrol 028

[]{#MA-MIC-ANM-01-015-028}

[]{#MA-MSOL-ANM-01-015-028}

**Pregunta.** ¿R4 necesita escoger una entrada para cada valor de la imagen?

**Solución.** No. Para refutar la separación se fijan sólo un valor y una preimagen en cada una de sus dos partes. No se construye un selector global de fibras.

### Microcontrol 029

[]{#MA-MIC-ANM-01-015-029}

[]{#MA-MSOL-ANM-01-015-029}

**Pregunta.** ¿La preimagen de un conexo por una función continua tiene que ser conexa?

**Solución.** No. Para $q(x)=x^2$ en $[-2,2]$, $q^{-1}[\{1\}]=\{-1,1\}$, que no es intervalo, aunque $\{1\}$ sí es conexo.

### Microcontrol 030

[]{#MA-MIC-ANM-01-015-030}

[]{#MA-MSOL-ANM-01-015-030}

**Pregunta.** ¿Una imagen singleton prueba que el dominio es conexo?

**Solución.** No. Una función constante en $\{-1,1\}$ es continua en el dominio relativo y tiene imagen singleton, pero el dominio admite un corte por cero.

### Microcontrol 031

[]{#MA-MIC-ANM-01-015-031}

[]{#MA-MSOL-ANM-01-015-031}

**Pregunta.** ¿Cómo una separación define una función continua con valores cero y uno?

**Solución.** Se asigna cero a una parte y uno a la otra. En cada punto la apertura relativa da una vecindad donde la función es constante; el error de salida allí es cero para cualquier tolerancia positiva.

### Microcontrol 032

[]{#MA-MIC-ANM-01-015-032}

[]{#MA-MSOL-ANM-01-015-032}

**Pregunta.** ¿Qué significa «constante» para una función con dominio vacío en este criterio?

**Solución.** Que para todos $x,z$ del dominio se cumple $u(x)=u(z)$. La condición universal es vacía; no se exige un valor alcanzado ni una entrada testigo.

## §15.5 — El valor intermedio como consecuencia estructural

### Microcontrol 033

[]{#MA-MIC-ANM-01-015-033}

[]{#MA-MSOL-ANM-01-015-033}

[]{#MA-SEC-ANM-01-015-005}

**Pregunta.** ¿En qué segmento se localiza el testigo del valor intermedio entre $f(u)$ y $f(v)$?

**Solución.** En $[\min(u,v),\max(u,v)]$, contenido en el intervalo de partida. Se aplica preservación a ese segmento, no sólo a todo el dominio.

### Microcontrol 034

[]{#MA-MIC-ANM-01-015-034}

[]{#MA-MSOL-ANM-01-015-034}

**Pregunta.** ¿Por qué un nivel estrictamente intermedio no se alcanza en los extremos de ese segmento?

**Solución.** Porque es distinto de $f(u)$ y $f(v)$. Un testigo con esa salida no puede ser $u$ ni $v$, así queda en el interior si son distintos.

### Microcontrol 035

[]{#MA-MIC-ANM-01-015-035}

[]{#MA-MSOL-ANM-01-015-035}

**Pregunta.** ¿Qué cambia si sólo se conoce $f(a)\le0\le f(b)$?

**Solución.** Se garantiza un cero en $[a,b]$, que puede estar en un extremo. Para asegurar uno en $(a,b)$ hacen falta signos estrictos opuestos.

### Microcontrol 036

[]{#MA-MIC-ANM-01-015-036}

[]{#MA-MSOL-ANM-01-015-036}

**Pregunta.** ¿Cómo se reduce encontrar $f(x)=y$ a encontrar un cero?

**Solución.** Con $g(x)=f(x)-y$, continua por álgebra de C14. Entonces $g(x)=0$ equivale exactamente a $f(x)=y$ y el dominio no cambia.

### Microcontrol 037

[]{#MA-MIC-ANM-01-015-037}

[]{#MA-MSOL-ANM-01-015-037}

**Pregunta.** ¿Qué prueba signo constante de una continua sin ceros en un intervalo no vacío?

**Solución.** Si hubiera dos valores de signos opuestos, R5 produciría un cero entre sus argumentos. Fijando un valor, todos los demás deben tener su mismo signo.

### Microcontrol 038

[]{#MA-MIC-ANM-01-015-038}

[]{#MA-MSOL-ANM-01-015-038}

**Pregunta.** ¿Por qué $1/x$ no contradice ese resultado al tener ambos signos?

**Solución.** Su dominio $\mathbb R\setminus\{0\}$ no es intervalo. La continuidad se conserva en ese dominio roto, pero falta la hipótesis que conecta los argumentos de signos opuestos.

### Microcontrol 039

[]{#MA-MIC-ANM-01-015-039}

[]{#MA-MSOL-ANM-01-015-039}

**Pregunta.** ¿R5 afirma unicidad del argumento que alcanza un nivel?

**Solución.** No. $x^2$ alcanza $1$ en $-1$ y $1$. La existencia de al menos un argumento se distingue de cualquier prueba adicional de inyectividad o monotonía.

### Microcontrol 040

[]{#MA-MIC-ANM-01-015-040}

[]{#MA-MSOL-ANM-01-015-040}

**Pregunta.** ¿La imagen de una continua intervalar tiene necesariamente mínimo y máximo?

**Solución.** No bajo estas hipótesis. La identidad en $(0,1)$ tiene imagen $(0,1)$, sin mínimo ni máximo. R5 prueba ausencia de huecos entre valores alcanzados, no extremos alcanzados.

## §15.6 — Bisección: existencia, localización y alcance del cálculo

### Microcontrol 041

[]{#MA-MIC-ANM-01-015-041}

[]{#MA-MSOL-ANM-01-015-041}

[]{#MA-SEC-ANM-01-015-006}

**Pregunta.** ¿Cuál es la longitud del encierro después de $n$ actualizaciones de bisección?

**Solución.** Con $L_0=a$, $U_0=b$, es $(b-a)/2^n$, mientras no haya detención por un cero exacto. Cada transición divide por dos la longitud anterior.

### Microcontrol 042

[]{#MA-MIC-ANM-01-015-042}

[]{#MA-MSOL-ANM-01-015-042}

**Pregunta.** ¿Qué extremo se reemplaza cuando $g(M_n)<0$ y los signos iniciales son negativo/positivo?

**Solución.** El inferior: $L_{n+1}=M_n$, $U_{n+1}=U_n$. El nuevo inferior conserva signo negativo y el superior conserva positivo.

### Microcontrol 043

[]{#MA-MIC-ANM-01-015-043}

[]{#MA-MSOL-ANM-01-015-043}

**Pregunta.** ¿Por qué $U_n$ es cota de todos los extremos inferiores y no sólo de $L_n$?

**Solución.** Para $k\le n$, $L_k\le L_n\le U_n$. Para $k>n$, el anidamiento da $L_k\le U_k\le U_n$. Ambos casos prueban la cota para todo $k$.

### Microcontrol 044

[]{#MA-MIC-ANM-01-015-044}

[]{#MA-MSOL-ANM-01-015-044}

**Pregunta.** ¿Qué dirección secuencial de continuidad se usa para pasar al cero límite?

**Solución.** La directa: convergencia de entradas a $c$ implica convergencia de salidas a $g(c)$. No se usa la recíproca secuencial ni selección de infractores.

### Microcontrol 045

[]{#MA-MIC-ANM-01-015-045}

[]{#MA-MSOL-ANM-01-015-045}

**Pregunta.** ¿Cuál es el error posicional máximo del punto medio $M_n$ respecto del cero encerrado?

**Solución.** Como $c\in[L_n,U_n]$, $|M_n-c|\le(U_n-L_n)/2=(b-a)/2^{n+1}$. Es una cota de distancia de argumentos.

### Microcontrol 046

[]{#MA-MIC-ANM-01-015-046}

[]{#MA-MSOL-ANM-01-015-046}

**Pregunta.** ¿Un encierro pequeño da por sí solo una cota numérica del residual $|g(M_n)|$?

**Solución.** No. Falta control cuantitativo de la variación de $g$. Continuidad permite un radio para una tolerancia dada, pero la longitud sola no proporciona una fórmula universal de residual.

### Microcontrol 047

[]{#MA-MIC-ANM-01-015-047}

[]{#MA-MSOL-ANM-01-015-047}

**Pregunta.** ¿Un intervalo de evaluación que contiene cero certifica que $g(M_n)=0$?

**Solución.** No. Sólo indica que no se certificó un signo estricto. Puede contener valores positivos o negativos; no autoriza detención por raíz exacta ni actualización de uno de los extremos.

### Microcontrol 048

[]{#MA-MIC-ANM-01-015-048}

[]{#MA-MSOL-ANM-01-015-048}

**Pregunta.** ¿Por qué la recurrencia clásica no es una promesa de algoritmo efectivo para toda función continua?

**Solución.** Las hipótesis no incluyen una evaluación computable ni una decisión efectiva de signos reales exactos. La regla única es válida matemáticamente por tricotomía; una implementación exige certificados de signo.

## §15.7 — Inyectividad, orden y continuidad de la inversa

### Microcontrol 049

[]{#MA-MIC-ANM-01-015-049}

[]{#MA-MSOL-ANM-01-015-049}

[]{#MA-SEC-ANM-01-015-007}

**Pregunta.** ¿Qué condición entre las imágenes de $x<y<z$ inicia la prueba de monotonía?

**Solución.** $f(y)$ está estrictamente entre $f(x)$ y $f(z)$. Un pico o valle permitiría, por R5 en los dos subsegmentos, dos argumentos distintos con una misma salida, violando inyectividad.

### Microcontrol 050

[]{#MA-MIC-ANM-01-015-050}

[]{#MA-MSOL-ANM-01-015-050}

**Pregunta.** ¿Por qué se escoge un nivel estrictamente entre el pico y ambos extremos?

**Solución.** Para que R5 entregue un punto interior en cada subsegmento. Así los dos testigos son distintos, uno antes de $y$ y otro después, y la contradicción de inyectividad es segura.

### Microcontrol 051

[]{#MA-MIC-ANM-01-015-051}

[]{#MA-MSOL-ANM-01-015-051}

**Pregunta.** ¿Basta estudiar un único triple para concluir monotonía en todo el intervalo?

**Solución.** No. Se fija un par orientado $a<b$ y se ordenan junto con cualquier par $x<y$. Los triples consecutivos propagan el signo de las diferencias en ese conjunto finito; el par fijado determina la orientación.

### Microcontrol 052

[]{#MA-MIC-ANM-01-015-052}

[]{#MA-MSOL-ANM-01-015-052}

**Pregunta.** ¿Qué garantiza que exista una inversa $h:f[I]\to I$?

**Solución.** Inyectividad da unicidad de la entrada por valor; la definición de imagen da existencia para todo valor de $f[I]$. No se requiere sobreyectividad sobre toda $\mathbb R$.

### Microcontrol 053

[]{#MA-MIC-ANM-01-015-053}

[]{#MA-MSOL-ANM-01-015-053}

**Pregunta.** ¿Qué hipótesis permite usar $x_0-\varepsilon/2$ como barrera si existe una entrada $x\le x_0-\varepsilon$?

**Solución.** Que $I$ sea intervalo: el punto barrera está entre esa entrada y $x_0$, ambos de $I$. Así la evaluación $f(x_0-\varepsilon/2)$ está definida.

### Microcontrol 054

[]{#MA-MIC-ANM-01-015-054}

[]{#MA-MSOL-ANM-01-015-054}

**Pregunta.** ¿Qué se hace si no hay entradas de $I$ menores o iguales que $x_0-\varepsilon$?

**Solución.** No hace falta barrera izquierda porque todas las entradas ya superan ese umbral. Se asigna a ese lado una tolerancia positiva arbitraria, por ejemplo $1$, para formar el mínimo final.

### Microcontrol 055

[]{#MA-MIC-ANM-01-015-055}

[]{#MA-MSOL-ANM-01-015-055}

**Pregunta.** ¿La inversa continua obtenida requiere una cota lineal inferior de $f$?

**Solución.** No. El radio se obtiene por diferencias positivas de valores en puntos barrera y monotonía. No se supone $|f(x)-f(z)|\ge c|x-z|$ ni derivada no nula.

### Microcontrol 056

[]{#MA-MIC-ANM-01-015-056}

[]{#MA-MSOL-ANM-01-015-056}

**Pregunta.** ¿Estricto crecimiento por sí solo excluye saltos?

**Solución.** No. $k(x)=x$ para $x<0$ y $k(x)=x+1$ para $x\ge0$ es estrictamente creciente, pero en cero las salidas por la izquierda se aproximan a cero y $k(0)=1$. Falta continuidad.

## §15.8 — Componentes: los intervalos máximos dentro de un dominio

### Microcontrol 057

[]{#MA-MIC-ANM-01-015-057}

[]{#MA-MSOL-ANM-01-015-057}

[]{#MA-SEC-ANM-01-015-008}

**Pregunta.** ¿Qué relación determina las componentes reales sin escoger representantes?

**Solución.** $x\sim y$ si el segmento entre $x$ y $y$ está contenido en $D$. Cada clase $C_x$ se define por esa fórmula; la familia de todas las clases existe como colección de subconjuntos de $D$ determinados por la relación.

### Microcontrol 058

[]{#MA-MIC-ANM-01-015-058}

[]{#MA-MSOL-ANM-01-015-058}

**Pregunta.** ¿Por qué es transitiva la relación por segmentos?

**Solución.** Los segmentos entre $x,y$ y entre $y,z$ están en $D$ y comparten $y$. Su unión es intervalo y contiene $x,z$, por lo que incluye el segmento entre ellos.

### Microcontrol 059

[]{#MA-MIC-ANM-01-015-059}

[]{#MA-MSOL-ANM-01-015-059}

**Pregunta.** ¿Cómo se prueba la maximalidad conexa de $C_x$?

**Solución.** Si un conexo $E\subseteq D$ contiene $x$, R3 dice que es intervalo. Para cada $y\in E$, el segmento entre $x,y$ está en $E\subseteq D$, luego $y\in C_x$. Así $E\subseteq C_x$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-015-060}

[]{#MA-MSOL-ANM-01-015-060}

**Pregunta.** ¿Dos componentes diferentes pueden intersectarse?

**Solución.** No. Son clases de equivalencia; si compartieran $z$, cualquier miembro de una estaría relacionado con $z$ y por transitividad con los miembros de la otra. Las clases serían iguales.

### Microcontrol 061

[]{#MA-MIC-ANM-01-015-061}

[]{#MA-MSOL-ANM-01-015-061}

**Pregunta.** ¿En qué ambiente son siempre cerradas las componentes de $D$?

**Solución.** Relativamente a $D$. El argumento de adherencia exige que el punto adherente también esté en $D$; no incorpora puntos exteriores al dominio. Una componente como $(0,1)$ no es cerrada real.

### Microcontrol 062

[]{#MA-MIC-ANM-01-015-062}

[]{#MA-MSOL-ANM-01-015-062}

**Pregunta.** ¿Por qué $\{0\}$ no es abierta relativa en $\{0\}\cup\{1/(n+1):n\in\mathbb N\}$?

**Solución.** Para todo $r>0$, por arquimedianidad existe $n$ con $0<1/(n+1)<r$. La vecindad de cero en el dominio siempre contiene otro punto. Aun así $\{0\}$ es una componente.

### Microcontrol 063

[]{#MA-MIC-ANM-01-015-063}

[]{#MA-MSOL-ANM-01-015-063}

**Pregunta.** ¿Cuáles son las componentes de $\mathbb Q$ y son abiertas relativas?

**Solución.** Son singletons, porque entre dos racionales distintos hay un irracional omitido. Ningún singleton es abierto relativo: todo radio alrededor de un racional contiene otro racional por densidad.

### Microcontrol 064

[]{#MA-MIC-ANM-01-015-064}

[]{#MA-MSOL-ANM-01-015-064}

**Pregunta.** ¿Qué refuerzo garantiza transporte exacto de componentes y no sólo inclusión?

**Solución.** Que la función sea homeomorfismo. Continuidad lleva una componente a un conexo contenido en una componente de la imagen; continuidad de la inversa y maximalidad dan la inclusión contraria. Una constante puede fusionar componentes.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Ejercicios](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-microcontroles.html)
