---
content-id: MA-BCH-0253
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-012-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 12
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C12_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 12](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html) · [Ejercicios](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §12.1 — Una función tiene un tipo

### Microcontrol 001

[]{#MA-MIC-ANM-01-012-001}

[]{#MA-MSOL-ANM-01-012-001}

[]{#MA-SEC-ANM-01-012-001}

**Pregunta.** ¿Basta la fórmula $x^2$ para determinar una función?

**Solución.** No. Deben declararse dominio, codominio y asignación. La fórmula puede definir funciones distintas al cambiar esos conjuntos.

### Microcontrol 002

[]{#MA-MIC-ANM-01-012-002}

[]{#MA-MSOL-ANM-01-012-002}

**Pregunta.** ¿Qué diferencia hay entre $f$ y $f(2)$ si $f(x)=x^2$?

**Solución.** $f$ es la función; si $2$ pertenece al dominio, $f(2)=4$ es un elemento del codominio.

### Microcontrol 003

[]{#MA-MIC-ANM-01-012-003}

[]{#MA-MSOL-ANM-01-012-003}

**Pregunta.** ¿Incumple la definición de función que $f(-2)=f(2)$?

**Solución.** No. Entradas distintas pueden compartir salida. Se exige una única salida para cada entrada.

### Microcontrol 004

[]{#MA-MIC-ANM-01-012-004}

[]{#MA-MSOL-ANM-01-012-004}

**Pregunta.** ¿Qué conjunto contiene al grafo de $f:D\to E$?

**Solución.** $D\times E$, pues cada par del grafo tiene entrada en $D$ y salida en $E$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-012-005}

[]{#MA-MSOL-ANM-01-012-005}

**Pregunta.** ¿Son iguales dos funciones con el mismo grafo y codominios distintos bajo nuestra convención?

**Solución.** No. El codominio forma parte del objeto tipado, aunque coincidan todos los pares.

### Microcontrol 006

[]{#MA-MIC-ANM-01-012-006}

[]{#MA-MSOL-ANM-01-012-006}

**Pregunta.** ¿Tres evaluaciones iguales prueban igualdad de funciones en $\mathbb R$?

**Solución.** No. Se necesita el mismo tipo e igualdad de valores para toda entrada del dominio; tres entradas no cubren $\mathbb R$.

### Microcontrol 007

[]{#MA-MIC-ANM-01-012-007}

[]{#MA-MSOL-ANM-01-012-007}

**Pregunta.** ¿Puede evaluarse en cero $h:\mathbb R\setminus\{0\}\to\mathbb R$, $h(x)=1/x$?

**Solución.** No: cero no pertenece al dominio, por lo que $h(0)$ no es una evaluación definida.

### Microcontrol 008

[]{#MA-MIC-ANM-01-012-008}

[]{#MA-MSOL-ANM-01-012-008}

**Pregunta.** ¿Incluye el grafo de $a_n=n^2$ el punto $(1/2,1/4)$?

**Solución.** No. $a:\mathbb N\to\mathbb R$ sólo admite índices naturales, con $\mathbb N=\{0,1,2,\ldots\}$; $1/2$ no es un índice.

## §12.2 — Imagen: transportar un conjunto

### Microcontrol 009

[]{#MA-MIC-ANM-01-012-009}

[]{#MA-MSOL-ANM-01-012-009}

[]{#MA-SEC-ANM-01-012-002}

**Pregunta.** ¿Qué testigo exige $y\in f[A]$?

**Solución.** Una entrada $x\in A$ con $f(x)=y$. Sin pertenencia a $A$, resolver la ecuación no basta.

### Microcontrol 010

[]{#MA-MIC-ANM-01-012-010}

[]{#MA-MSOL-ANM-01-012-010}

**Pregunta.** ¿Son el mismo objeto $f(2)$ y $f[\{2\}]$?

**Solución.** No: el primero es un valor; el segundo es el conjunto unitario $\{f(2)\}$, si $2$ está en el dominio.

### Microcontrol 011

[]{#MA-MIC-ANM-01-012-011}

[]{#MA-MSOL-ANM-01-012-011}

**Pregunta.** Para $q(x)=x^2$, ¿cuál es $q[\{-2,2\}]$?

**Solución.** $\{4\}$. La imagen es un conjunto y no conserva dos copias del mismo valor.

### Microcontrol 012

[]{#MA-MIC-ANM-01-012-012}

[]{#MA-MSOL-ANM-01-012-012}

**Pregunta.** ¿Cuál es la imagen del conjunto vacío?

**Solución.** $f[\varnothing]=\varnothing$, porque no existe una entrada que pueda ser testigo.

### Microcontrol 013

[]{#MA-MIC-ANM-01-012-013}

[]{#MA-MSOL-ANM-01-012-013}

**Pregunta.** ¿Implica $A\subseteq C$ que $f[A]\subseteq f[C]$?

**Solución.** Sí, si ambos son subconjuntos del dominio. Todo testigo en $A$ también pertenece a $C$.

### Microcontrol 014

[]{#MA-MIC-ANM-01-012-014}

[]{#MA-MSOL-ANM-01-012-014}

**Pregunta.** ¿Tiene que coincidir $f[D]$ con el codominio $E$?

**Solución.** No. Sólo $f[D]\subseteq E$ es obligatorio. La igualdad caracteriza sobreyectividad.

### Microcontrol 015

[]{#MA-MIC-ANM-01-012-015}

[]{#MA-MSOL-ANM-01-012-015}

**Pregunta.** ¿Qué entrada de $[-2,1]$ alcanza $4$ bajo el cuadrado?

**Solución.** $-2$, pues $(-2)^2=4$ y $-2\in[-2,1]$. La otra raíz, $2$, no es un testigo en ese intervalo.

### Microcontrol 016

[]{#MA-MIC-ANM-01-012-016}

[]{#MA-MSOL-ANM-01-012-016}

**Pregunta.** ¿Cuál es $q[(-2,2)]$ para $q(x)=x^2$?

**Solución.** $[0,4)$: todo cuadrado de esas entradas está allí y, para $0\le y<4$, $x=\sqrt y\in(-2,2)$ alcanza $y$.

## §12.3 — Preimagen: seleccionar por la salida

### Microcontrol 017

[]{#MA-MIC-ANM-01-012-017}

[]{#MA-MSOL-ANM-01-012-017}

[]{#MA-SEC-ANM-01-012-003}

**Pregunta.** ¿En qué conjunto vive $f^{-1}[B]$ si $f:D\to E$?

**Solución.** En $D$: por definición es el conjunto de entradas del dominio cuya salida pertenece a $B\subseteq E$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-012-018}

[]{#MA-MSOL-ANM-01-012-018}

**Pregunta.** ¿Se necesita que $f$ tenga función inversa para tomar preimágenes?

**Solución.** No. La preimagen comprueba $f(x)\in B$ para $x\in D$; existe para cualquier función.

### Microcontrol 019

[]{#MA-MIC-ANM-01-012-019}

[]{#MA-MSOL-ANM-01-012-019}

**Pregunta.** ¿Cuál es la fibra del cuadrado real sobre $4$?

**Solución.** $\{-2,2\}$: ambas entradas y sólo ellas satisfacen $x^2=4$.

### Microcontrol 020

[]{#MA-MIC-ANM-01-012-020}

[]{#MA-MSOL-ANM-01-012-020}

**Pregunta.** ¿Cuál es la fibra del cuadrado real sobre $-1$?

**Solución.** $\varnothing$, porque un cuadrado real es no negativo.

### Microcontrol 021

[]{#MA-MIC-ANM-01-012-021}

[]{#MA-MSOL-ANM-01-012-021}

**Pregunta.** ¿Cuál es $f^{-1}[E]$?

**Solución.** $D$, pues toda entrada del dominio tiene salida en el codominio.

### Microcontrol 022

[]{#MA-MIC-ANM-01-012-022}

[]{#MA-MSOL-ANM-01-012-022}

**Pregunta.** ¿Cuál es $q^{-1}[(1,4]]$ para el cuadrado en $\mathbb R$?

**Solución.** $[-2,-1)\cup(1,2]$, ya que $1<x^2\le4$ equivale a $1<|x|\le2$.

### Microcontrol 023

[]{#MA-MIC-ANM-01-012-023}

[]{#MA-MSOL-ANM-01-012-023}

**Pregunta.** ¿Cómo cambia esa preimagen si el dominio se restringe a $[0,\infty)$?

**Solución.** Se recorta por el nuevo dominio y queda $(1,2]$. Las entradas negativas dejan de estar disponibles.

### Microcontrol 024

[]{#MA-MIC-ANM-01-012-024}

[]{#MA-MSOL-ANM-01-012-024}

**Pregunta.** ¿Qué recupera $f[f^{-1}[B]]$?

**Solución.** $B\cap f[D]$. Recupera exactamente las salidas de $B$ que la función realmente alcanza, no las salidas imposibles.

## §12.4 — Qué operaciones sobreviven al transporte

### Microcontrol 025

[]{#MA-MIC-ANM-01-012-025}

[]{#MA-MSOL-ANM-01-012-025}

[]{#MA-SEC-ANM-01-012-004}

**Pregunta.** ¿La imagen conserva la unión de dos conjuntos de entradas?

**Solución.** Sí: $f[A\cup C]=f[A]\cup f[C]$. Un testigo en la unión pertenece a uno de los conjuntos, y recíprocamente.

### Microcontrol 026

[]{#MA-MIC-ANM-01-012-026}

[]{#MA-MSOL-ANM-01-012-026}

**Pregunta.** ¿Qué inclusión siempre vale para la imagen de una intersección?

**Solución.** $f[A\cap C]\subseteq f[A]\cap f[C]$, porque un testigo común sirve para ambas imágenes.

### Microcontrol 027

[]{#MA-MIC-ANM-01-012-027}

[]{#MA-MSOL-ANM-01-012-027}

**Pregunta.** Con $q(x)=x^2$, $A=\{-1\}$ y $C=\{1\}$, ¿por qué falla la igualdad anterior?

**Solución.** $A\cap C=\varnothing$ tiene imagen vacía, pero $q[A]\cap q[C]=\{1\}$. La salida común procede de dos entradas distintas.

### Microcontrol 028

[]{#MA-MIC-ANM-01-012-028}

[]{#MA-MSOL-ANM-01-012-028}

**Pregunta.** ¿Qué hipótesis reúne los dos testigos de una salida común?

**Solución.** Inyectividad: de $f(a)=f(c)$ se obtiene $a=c$, que pertenece entonces a ambos conjuntos.

### Microcontrol 029

[]{#MA-MIC-ANM-01-012-029}

[]{#MA-MSOL-ANM-01-012-029}

**Pregunta.** ¿Qué preimagen tiene $B\cap H$?

**Solución.** $f^{-1}[B]\cap f^{-1}[H]$, pues una entrada cumple ambas condiciones exactamente cuando su única salida pertenece a ambos conjuntos.

### Microcontrol 030

[]{#MA-MIC-ANM-01-012-030}

[]{#MA-MSOL-ANM-01-012-030}

**Pregunta.** ¿Cuáles son los universos de los complementos en la ley de preimagen?

**Solución.** $E$ a la izquierda y $D$ a la derecha: $f^{-1}[E\setminus B]=D\setminus f^{-1}[B]$.

### Microcontrol 031

[]{#MA-MIC-ANM-01-012-031}

[]{#MA-MSOL-ANM-01-012-031}

**Pregunta.** ¿Siempre se cumple $A=f^{-1}[f[A]]$?

**Solución.** No. Siempre hay inclusión de $A$ en el lado derecho, pero para el cuadrado y $A=\{1\}$ el lado derecho es $\{-1,1\}$. Inyectividad garantiza igualdad.

### Microcontrol 032

[]{#MA-MIC-ANM-01-012-032}

[]{#MA-MSOL-ANM-01-012-032}

**Pregunta.** ¿Cuál es la preimagen de $B\setminus H$?

**Solución.** $f^{-1}[B]\setminus f^{-1}[H]$: equivale a exigir $f(x)\in B$ y $f(x)\notin H$ a una entrada $x\in D$.

## §12.5 — Componer, restringir y deshacer

### Microcontrol 033

[]{#MA-MIC-ANM-01-012-033}

[]{#MA-MSOL-ANM-01-012-033}

[]{#MA-SEC-ANM-01-012-005}

**Pregunta.** ¿Qué tipo tiene $g\circ f$ si $f:D\to E$ y $g:E\to F$?

**Solución.** $D\to F$, con $(g\circ f)(x)=g(f(x))$; la salida de $f$ es una entrada autorizada de $g$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-012-034}

[]{#MA-MSOL-ANM-01-012-034}

**Pregunta.** ¿Cómo se calcula $(g\circ f)[A]$ por etapas?

**Solución.** Como $g[f[A]]$: primero transportamos las entradas por $f$ y después sus salidas por $g$.

### Microcontrol 035

[]{#MA-MIC-ANM-01-012-035}

[]{#MA-MSOL-ANM-01-012-035}

**Pregunta.** ¿En qué orden se calcula $(g\circ f)^{-1}[C]$?

**Solución.** Primero $g^{-1}[C]$ en $E$, después $f^{-1}[g^{-1}[C]]$ en $D$. Es la condición $g(f(x))\in C$.

### Microcontrol 036

[]{#MA-MIC-ANM-01-012-036}

[]{#MA-MSOL-ANM-01-012-036}

**Pregunta.** ¿Cuál es el dominio de $f|_A$?

**Solución.** $A\subseteq D$. La restricción mantiene los valores en $A$ y el codominio $E$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-012-037}

[]{#MA-MSOL-ANM-01-012-037}

**Pregunta.** ¿Cuál es $(f|_A)^{-1}[B]$?

**Solución.** $A\cap f^{-1}[B]$, porque sólo se admiten las entradas de $A$ cuya salida está en $B$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-012-038}

[]{#MA-MSOL-ANM-01-012-038}

**Pregunta.** ¿Qué dos propiedades permiten construir una función inversa $E\to D$?

**Solución.** Sobreyectividad, para que cada $y\in E$ tenga entrada, e inyectividad, para que esa entrada sea única; juntas forman biyectividad.

### Microcontrol 039

[]{#MA-MIC-ANM-01-012-039}

[]{#MA-MSOL-ANM-01-012-039}

**Pregunta.** ¿Cuál es la inversa de $f:\mathbb R\to\mathbb R$, $f(x)=2x+1$?

**Solución.** $h(y)=(y-1)/2$. Sustituir verifica $h(f(x))=x$ y $f(h(y))=y$ para todos los reales.

### Microcontrol 040

[]{#MA-MIC-ANM-01-012-040}

[]{#MA-MSOL-ANM-01-012-040}

**Pregunta.** ¿Por qué restringir el cuadrado a entradas no negativas no basta para hacerlo biyectivo hacia $\mathbb R$?

**Solución.** Porque ninguna entrada alcanza una salida negativa. Para biyectividad hay que declarar codominio $[0,\infty)$ además de restringir el dominio.

## §12.6 — Transportar el orden no rellena los huecos

### Microcontrol 041

[]{#MA-MIC-ANM-01-012-041}

[]{#MA-MSOL-ANM-01-012-041}

[]{#MA-SEC-ANM-01-012-006}

**Pregunta.** ¿Qué significa no decreciente en un dominio $D\subseteq\mathbb R$?

**Solución.** Para todos $x,y\in D$, $x\le y$ implica $f(x)\le f(y)$. El sentido no estricto permite valores iguales.

### Microcontrol 042

[]{#MA-MIC-ANM-01-012-042}

[]{#MA-MSOL-ANM-01-012-042}

**Pregunta.** ¿Una función estrictamente creciente es inyectiva?

**Solución.** Sí. Entradas distintas se ordenan por tricotomía y sus salidas quedan estrictamente ordenadas, luego son distintas.

### Microcontrol 043

[]{#MA-MIC-ANM-01-012-043}

[]{#MA-MSOL-ANM-01-012-043}

**Pregunta.** ¿Una función no decreciente tiene que ser inyectiva?

**Solución.** No. Una constante en un dominio con dos entradas distintas es no decreciente y les asigna la misma salida.

### Microcontrol 044

[]{#MA-MIC-ANM-01-012-044}

[]{#MA-MSOL-ANM-01-012-044}

**Pregunta.** ¿Qué controla el intervalo $[f(a),f(b)]$ si $f$ es no decreciente?

**Solución.** Contiene $f[D\cap[a,b]]$, pues $a\le x\le b$ implica $f(a)\le f(x)\le f(b)$. No promete todas las salidas intermedias.

### Microcontrol 045

[]{#MA-MIC-ANM-01-012-045}

[]{#MA-MSOL-ANM-01-012-045}

**Pregunta.** Para la función de salto $s$ del texto, ¿se alcanza $1/2$?

**Solución.** No. Las entradas negativas dan salidas negativas y las no negativas dan salidas al menos $1$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-012-046}

[]{#MA-MSOL-ANM-01-012-046}

**Pregunta.** ¿Cuál es $s[[-1,1]]$?

**Solución.** $[-1,0)\cup[1,2]$, transportando cada una de las dos ramas con sus extremos correctos.

### Microcontrol 047

[]{#MA-MIC-ANM-01-012-047}

[]{#MA-MSOL-ANM-01-012-047}

**Pregunta.** ¿Qué signo de $m$ hace decreciente estricta a $h(x)=mx+c$?

**Solución.** $m<0$, porque para $x<y$ el producto $m(y-x)$ es negativo, luego $h(y)<h(x)$.

### Microcontrol 048

[]{#MA-MIC-ANM-01-012-048}

[]{#MA-MSOL-ANM-01-012-048}

**Pregunta.** ¿En qué rama es creciente estricta la función cuadrado?

**Solución.** En $[0,\infty)$: si $0\le x<y$, $y^2-x^2=(y-x)(y+x)>0$. En la rama no positiva es decreciente estricta.

## §12.7 — Distancia y escala: medir la deformación

### Microcontrol 049

[]{#MA-MIC-ANM-01-012-049}

[]{#MA-MSOL-ANM-01-012-049}

[]{#MA-SEC-ANM-01-012-007}

**Pregunta.** ¿Qué factor multiplica las distancias bajo $h(x)=mx+c$?

**Solución.** $|m|$, ya que $|h(x)-h(y)|=|m||x-y|$; $c$ se cancela.

### Microcontrol 050

[]{#MA-MIC-ANM-01-012-050}

[]{#MA-MSOL-ANM-01-012-050}

**Pregunta.** ¿Puede una función invertir el orden y conservar todas las distancias?

**Solución.** Sí: $h(x)=-x$ es estrictamente decreciente y $|-x-(-y)|=|x-y|$.

### Microcontrol 051

[]{#MA-MIC-ANM-01-012-051}

[]{#MA-MSOL-ANM-01-012-051}

**Pregunta.** ¿De qué puede depender una cota de expansión $L$?

**Solución.** Puede depender de la función y del dominio declarado, pero debe fijarse antes de elegir el par $x,y$ y servir para todos los pares de ese dominio.

### Microcontrol 052

[]{#MA-MIC-ANM-01-012-052}

[]{#MA-MSOL-ANM-01-012-052}

**Pregunta.** ¿Qué cota de expansión tiene $x\mapsto|x|$?

**Solución.** $L=1$, por $\bigl||x|-|y|\bigr|\le|x-y|$, consecuencia de la desigualdad triangular en ambos sentidos.

### Microcontrol 053

[]{#MA-MIC-ANM-01-012-053}

[]{#MA-MSOL-ANM-01-012-053}

**Pregunta.** ¿Qué cota da la factorización del cuadrado en $[-R,R]$ con $R>0$?

**Solución.** $2R$: $|x^2-y^2|=|x-y||x+y|\le2R|x-y|$.

### Microcontrol 054

[]{#MA-MIC-ANM-01-012-054}

[]{#MA-MSOL-ANM-01-012-054}

**Pregunta.** ¿Por qué no sirve una cota finita $L\ge0$ para el cuadrado en toda la recta?

**Solución.** El par $x=L+1$, $y=x+1$ tiene distancia $1$ y distancia de salidas $2L+3>L$, contradiciendo la cota propuesta.

### Microcontrol 055

[]{#MA-MIC-ANM-01-012-055}

[]{#MA-MSOL-ANM-01-012-055}

**Pregunta.** ¿Qué garantiza una cota inferior $c|x-y|\le|f(x)-f(y)|$ con $c>0$?

**Solución.** Inyectividad: si las salidas coinciden, la desigualdad obliga a $|x-y|=0$, luego $x=y$.

### Microcontrol 056

[]{#MA-MIC-ANM-01-012-056}

[]{#MA-MSOL-ANM-01-012-056}

**Pregunta.** ¿Qué cota tiene una composición de funciones con cotas $L$ y $M$ compatibles?

**Solución.** $ML$, al aplicar primero $|g(f(x))-g(f(y))|\le M|f(x)-f(y)|$ y después la cota $L$.

## §12.8 — Representaciones y ventanas de control

### Microcontrol 057

[]{#MA-MIC-ANM-01-012-057}

[]{#MA-MSOL-ANM-01-012-057}

[]{#MA-SEC-ANM-01-012-008}

**Pregunta.** ¿Qué tipo tiene $T(u,v)=(u+v,v)$ en el texto?

**Solución.** $T:\mathbb R^2\to\mathbb R^2$; tanto entrada como salida son pares reales, no valores escalares.

### Microcontrol 058

[]{#MA-MIC-ANM-01-012-058}

[]{#MA-MSOL-ANM-01-012-058}

**Pregunta.** ¿Cuál es la inversa de esa transformación de rejilla?

**Solución.** $S(a,b)=(a-b,b)$, pues $S(T(u,v))=(u,v)$ y $T(S(a,b))=(a,b)$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-012-059}

[]{#MA-MSOL-ANM-01-012-059}

**Pregunta.** ¿En qué se transforma la recta $u=j$ bajo $T$?

**Solución.** En la recta parametrizada por $(j+v,v)$, que cumple $a-b=j$ en coordenadas de salida $(a,b)$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-012-060}

[]{#MA-MSOL-ANM-01-012-060}

**Pregunta.** ¿Multiplica $T$ todas las longitudes por un mismo factor?

**Solución.** No: el segmento de $(0,0)$ a $(1,0)$ conserva longitud $1$, mientras que el de $(0,0)$ a $(0,1)$ pasa a longitud $\sqrt2$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-012-061}

[]{#MA-MSOL-ANM-01-012-061}

**Pregunta.** ¿Qué inclusión de entradas equivale a $f[A]\subseteq B$?

**Solución.** $A\subseteq f^{-1}[B]$. Ambas dicen que toda entrada de $A$ tiene salida en $B$.

### Microcontrol 062

[]{#MA-MIC-ANM-01-012-062}

[]{#MA-MSOL-ANM-01-012-062}

**Pregunta.** ¿Por qué se recorta $B(x_0,r)$ por $D$ al usarla como ventana de entrada?

**Solución.** Porque sólo se puede transportar un subconjunto del dominio. Entradas fuera de $D$ no tienen evaluación por $f$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-012-063}

[]{#MA-MSOL-ANM-01-012-063}

**Pregunta.** Para el cuadrado, ¿qué cota certifica la ventana de radio $1/4$ alrededor de $1$ hacia radio $1$ alrededor de su salida?

**Solución.** Si $|x-1|<1/4$, entonces $|x+1|<9/4$ y $|x^2-1|<9/16<1$. Así toda la ventana de entrada se transporta dentro de la de salida.

### Microcontrol 064

[]{#MA-MIC-ANM-01-012-064}

[]{#MA-MSOL-ANM-01-012-064}

**Pregunta.** ¿Es vecindad de cero la preimagen $s^{-1}[B(1,1/4)]=[0,1/4)$?

**Solución.** No. Contiene cero pero ninguna bola de radio positivo centrada en cero, ya que toda esa bola contiene entradas negativas.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 12](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html) · [Ejercicios](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-microcontroles.html)
