---
content-id: MA-BCH-0289
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-021-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 21
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C21_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §21.1 — Un polinomio para los datos de un centro

### Microcontrol 001

[]{#MA-MIC-ANM-01-021-001}

[]{#MA-MSOL-ANM-01-021-001}

[]{#MA-SEC-ANM-01-021-001}

**Pregunta.** ¿Qué datos conserva el polinomio de Taylor de orden $n$?

**Solución.** El valor y las derivadas de órdenes1 a$n$ en el centro, si están definidos; orden0 significa el propio valor.

### Microcontrol 002

[]{#MA-MIC-ANM-01-021-002}

[]{#MA-MSOL-ANM-01-021-002}

**Pregunta.** ¿Cuál es el valor de $0!$ y por qué importa?

**Solución.** Es1. Su copia real positiva permite el coeficiente de orden0 y evita un denominador nulo.

### Microcontrol 003

[]{#MA-MIC-ANM-01-021-003}

[]{#MA-MSOL-ANM-01-021-003}

**Pregunta.** ¿Qué significa $k!$ cuando aparece en un cociente real?

**Solución.** La copia real del factorial natural mediante la incrustación declarada; no se identifican tácitamente naturales y reales.

### Microcontrol 004

[]{#MA-MIC-ANM-01-021-004}

[]{#MA-MSOL-ANM-01-021-004}

**Pregunta.** ¿Qué coeficiente corresponde a la derivada de orden $j$?

**Solución.** $a_j=f^{(j)}(c)/j!$, porque $P^{(j)}(c)=j!a_j$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-021-005}

[]{#MA-MSOL-ANM-01-021-005}

**Pregunta.** ¿El orden $n$ obliga a grado exactamente $n$?

**Solución.** No. El último coeficiente puede ser cero, y el grado sólo está acotado superiormente por$n$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-021-006}

[]{#MA-MSOL-ANM-01-021-006}

**Pregunta.** ¿Dónde está definido el polinomio y dónde el resto?

**Solución.** El polinomio está en toda la recta; el resto $f-T_{n,c}f$ sólo en el dominio de$f$.

### Microcontrol 007

[]{#MA-MIC-ANM-01-021-007}

[]{#MA-MSOL-ANM-01-021-007}

**Pregunta.** ¿Qué resto tiene $t^3$ a orden2 y centro1?

**Solución.** Con $t=1+h$, el polinomio es $1+3h+3h^2$ y el resto exacto es$h^3$.

### Microcontrol 008

[]{#MA-MIC-ANM-01-021-008}

[]{#MA-MSOL-ANM-01-021-008}

**Pregunta.** ¿Los datos centrales hasta orden $n$ determinan una función completa?

**Solución.** No. Añadir $A(t-c)^{n+1}$ conserva todos esos datos y puede cambiar la función fuera del centro.

## §21.2 — Rolle se repite sin perder sus hipótesis

### Microcontrol 009

[]{#MA-MIC-ANM-01-021-009}

[]{#MA-MSOL-ANM-01-021-009}

[]{#MA-SEC-ANM-01-021-002}

**Pregunta.** ¿Qué igualdades centrales se necesitan para Rolle repetido de orden $n$?

**Solución.** $H_k(c)=0$ para $0\le k\le n$, más $H_0(x)=0$ con $x\ne c$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-021-010}

[]{#MA-MSOL-ANM-01-021-010}

**Pregunta.** ¿Cuántas aplicaciones de Rolle produce la última derivada nula?

**Solución.** $n+1$ aplicaciones, incluida una sola cuando$n=0$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-021-011}

[]{#MA-MSOL-ANM-01-021-011}

**Pregunta.** ¿Qué invariante permite continuar el paso $k$?

**Solución.** $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$ y continuidad/derivabilidad en el subsegmento correspondiente.

### Microcontrol 012

[]{#MA-MIC-ANM-01-021-012}

[]{#MA-MSOL-ANM-01-021-012}

**Pregunta.** ¿Qué relación enlaza los miembros de la cadena?

**Solución.** $H_k\prime=H_{k+1}$ en el interior para $k<n$; la derivada del último miembro también debe existir interiormente.

### Microcontrol 013

[]{#MA-MIC-ANM-01-021-013}

[]{#MA-MSOL-ANM-01-021-013}

**Pregunta.** ¿Se pide continuidad de la derivada final?

**Solución.** No. Se necesita que exista en el interior para el último Rolle; los miembros anteriores sí son continuos sobre los segmentos.

### Microcontrol 014

[]{#MA-MIC-ANM-01-021-014}

[]{#MA-MSOL-ANM-01-021-014}

**Pregunta.** ¿Cómo se ordena el segmento si $x<c$?

**Solución.** Con extremos $\min(c,x)$ y $\max(c,x)$; los puntos sucesivos quedan entre$c$ y el punto anterior por el lado izquierdo.

### Microcontrol 015

[]{#MA-MIC-ANM-01-021-015}

[]{#MA-MSOL-ANM-01-021-015}

**Pregunta.** ¿Qué punto intermedio se afirma si $x=c$?

**Solución.** Ninguno. No hay segmento con extremos distintos y el caso se resuelve por la igualdad central.

### Microcontrol 016

[]{#MA-MIC-ANM-01-021-016}

[]{#MA-MSOL-ANM-01-021-016}

**Pregunta.** ¿Se selecciona una familia infinita de testigos?

**Solución.** No. Para un orden y una entrada fijados, la inducción realiza sólo un número finito de pasos existenciales.

## §21.3 — Forzar el resto: la fórmula de Lagrange

### Microcontrol 017

[]{#MA-MIC-ANM-01-021-017}

[]{#MA-MSOL-ANM-01-021-017}

[]{#MA-SEC-ANM-01-021-003}

**Pregunta.** ¿Qué coeficiente fuerza la anulación del auxiliar en $x\ne c$?

**Solución.** $A=R_{n,c}(x)/(x-c)^{n+1}$; el incremento no nulo permite dividir.

### Microcontrol 018

[]{#MA-MIC-ANM-01-021-018}

[]{#MA-MSOL-ANM-01-021-018}

**Pregunta.** ¿Qué función auxiliar se usa en la prueba de Lagrange?

**Solución.** $H(t)=f(t)-T_{n,c}f(t)-A(t-c)^{n+1}$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-021-019}

[]{#MA-MSOL-ANM-01-021-019}

**Pregunta.** ¿Por qué se anulan sus datos centrales hasta orden $n$?

**Solución.** Taylor conserva los datos y la potencia adicional tiene todas esas derivadas nulas en$c$.

### Microcontrol 020

[]{#MA-MIC-ANM-01-021-020}

[]{#MA-MSOL-ANM-01-021-020}

**Pregunta.** ¿Qué igualdad deja el último Rolle?

**Solución.** $f^{(n+1)}(\xi)-A(n+1)!=0$, pues el polinomio de orden$n$ ya tiene derivada$n+1$ nula.

### Microcontrol 021

[]{#MA-MIC-ANM-01-021-021}

[]{#MA-MSOL-ANM-01-021-021}

**Pregunta.** ¿Qué posición tiene $\xi$?

**Solución.** Está estrictamente entre$c$ y$x$, para$x\ne c$; no se predetermina como punto medio.

### Microcontrol 022

[]{#MA-MIC-ANM-01-021-022}

[]{#MA-MSOL-ANM-01-021-022}

**Pregunta.** ¿De qué datos puede depender el testigo?

**Solución.** De la función, el orden, el centro y la entrada; no se conserva como una constante al variarlos.

### Microcontrol 023

[]{#MA-MIC-ANM-01-021-023}

[]{#MA-MSOL-ANM-01-021-023}

**Pregunta.** ¿Es necesaria continuidad de $f^{(n+1)}$ para la prueba por Rolle?

**Solución.** No. Basta su existencia interior y la continuidad de los miembros hasta orden$n$ sobre el segmento.

### Microcontrol 024

[]{#MA-MIC-ANM-01-021-024}

[]{#MA-MSOL-ANM-01-021-024}

**Pregunta.** ¿Qué se usa como dato central en el contrato cerrado?

**Solución.** Los valores de las extensiones continuas dadas $f_k(c)$; no se presupone derivar en un borde.

## §21.4 — Un punto desconocido, una cota verificable

### Microcontrol 025

[]{#MA-MIC-ANM-01-021-025}

[]{#MA-MSOL-ANM-01-021-025}

[]{#MA-SEC-ANM-01-021-004}

**Pregunta.** ¿Qué cota elimina el testigo de Lagrange?

**Solución.** Una cota $|f^{(n+1)}|\le M$ válida en todo el interior donde puede estar el testigo.

### Microcontrol 026

[]{#MA-MIC-ANM-01-021-026}

[]{#MA-MSOL-ANM-01-021-026}

**Pregunta.** ¿Qué hacer si $M=0$?

**Solución.** La cota obliga al resto a ser cero; no se divide por$M$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-021-027}

[]{#MA-MSOL-ANM-01-021-027}

**Pregunta.** ¿Qué número controla todos los errores si $|x-c|\le\rho$?

**Solución.** $M\rho^{n+1}/(n+1)!$, siempre que la misma cota de derivada valga en toda la región.

### Microcontrol 028

[]{#MA-MIC-ANM-01-021-028}

[]{#MA-MSOL-ANM-01-021-028}

**Pregunta.** ¿Qué función permite derivar telescópicamente la forma de Cauchy?

**Solución.** $G(t)=f(x)-\sum_{k=0}^n f^{(k)}(t)(x-t)^k/k!$, con$x$ fijado.

### Microcontrol 029

[]{#MA-MIC-ANM-01-021-029}

[]{#MA-MSOL-ANM-01-021-029}

**Pregunta.** ¿Cuál es su derivada después de cancelar términos?

**Solución.** $G\prime(t)=-f^{(n+1)}(t)(x-t)^n/n!$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-021-030}

[]{#MA-MSOL-ANM-01-021-030}

**Pregunta.** ¿Qué forma tiene el resto de Cauchy?

**Solución.** $R=f^{(n+1)}(\eta)(x-\eta)^n(x-c)/n!$, con$\eta$ estrictamente interior.

### Microcontrol 031

[]{#MA-MIC-ANM-01-021-031}

[]{#MA-MSOL-ANM-01-021-031}

**Pregunta.** ¿Los testigos de Lagrange y Cauchy tienen que coincidir?

**Solución.** No. Son existencias obtenidas de auxiliares diferentes.

### Microcontrol 032

[]{#MA-MIC-ANM-01-021-032}

[]{#MA-MSOL-ANM-01-021-032}

**Pregunta.** ¿Qué ocurre al multiplicar la banda de coeficientes por un incremento elevado negativo?

**Solución.** Se invierte el orden de las cotas; una banda firmada exige controlar paridad y lado del centro.

## §21.5 — Peano: lo que desaparece al cambiar de escala

### Microcontrol 033

[]{#MA-MIC-ANM-01-021-033}

[]{#MA-MSOL-ANM-01-021-033}

[]{#MA-SEC-ANM-01-021-005}

**Pregunta.** ¿Qué significa $R(c+h)=o(|h|^n)$?

**Solución.** Para cada$\varepsilon>0$ hay un radio que hace$|R(c+h)|<\varepsilon|h|^n$ en todas las entradas perforadas de ese radio.

### Microcontrol 034

[]{#MA-MIC-ANM-01-021-034}

[]{#MA-MSOL-ANM-01-021-034}

**Pregunta.** ¿Qué caso de Peano corresponde a$n=1$?

**Solución.** La definición de derivada en el centro; no exige derivabilidad de la función en otros centros.

### Microcontrol 035

[]{#MA-MIC-ANM-01-021-035}

[]{#MA-MSOL-ANM-01-021-035}

**Pregunta.** ¿Dónde se exige la derivada de orden$n$ en el contrato de Peano?

**Solución.** Sólo en el centro, como derivada de$f^{(n-1)}$; las inferiores necesarias están definidas en un entorno.

### Microcontrol 036

[]{#MA-MIC-ANM-01-021-036}

[]{#MA-MSOL-ANM-01-021-036}

**Pregunta.** ¿Qué herramienta recupera$H$ desde una cota para$H\prime$ en la inducción?

**Solución.** Cauchy sobre$H$ y$(t-c)^n$, cuyo cociente de derivadas divide por$n(\xi-c)^{n-1}\ne0$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-021-037}

[]{#MA-MSOL-ANM-01-021-037}

**Pregunta.** ¿Peano proporciona una constante para$|h|^{n+1}$?

**Solución.** No. Describe un error normalizado que tiende a cero, sin garantizar una cota del siguiente orden.

### Microcontrol 038

[]{#MA-MIC-ANM-01-021-038}

[]{#MA-MSOL-ANM-01-021-038}

**Pregunta.** ¿Qué cociente tiende a cero para$h^2\sqrt{|h|}$ a orden2?

**Solución.** $f(h)/|h|^2=\sqrt{|h|}\to0$.

### Microcontrol 039

[]{#MA-MIC-ANM-01-021-039}

[]{#MA-MSOL-ANM-01-021-039}

**Pregunta.** ¿Por qué ese ejemplo no tiene una cota$C|h|^3$ en un radio?

**Solución.** Su cociente por$|h|^3$ es$1/\sqrt{|h|}$, no acotado cerca de cero.

### Microcontrol 040

[]{#MA-MIC-ANM-01-021-040}

[]{#MA-MSOL-ANM-01-021-040}

**Pregunta.** ¿Puede derivarse un símbolo$o$ sin hipótesis adicionales?

**Solución.** No. Un control de valores del resto no proporciona automáticamente un control de su derivada.

## §21.6 — La primera derivada que no se anula

### Microcontrol 041

[]{#MA-MIC-ANM-01-021-041}

[]{#MA-MSOL-ANM-01-021-041}

[]{#MA-SEC-ANM-01-021-006}

**Pregunta.** ¿Qué término decide el criterio de la primera derivada no nula?

**Solución.** $ah^m$, con$a=f^{(m)}(c)/m!\ne0$, tras anular las derivadas anteriores.

### Microcontrol 042

[]{#MA-MIC-ANM-01-021-042}

[]{#MA-MSOL-ANM-01-021-042}

**Pregunta.** ¿Qué tolerancia evita que el resto cambie el signo principal?

**Solución.** $|r(h)|<(|a|/2)|h|^m$ en un radio perforado.

### Microcontrol 043

[]{#MA-MIC-ANM-01-021-043}

[]{#MA-MSOL-ANM-01-021-043}

**Pregunta.** ¿Qué da un primer orden no nulo par con coeficiente positivo?

**Solución.** Un mínimo local estricto en un centro interior, porque el término principal es positivo en ambos lados.

### Microcontrol 044

[]{#MA-MIC-ANM-01-021-044}

[]{#MA-MSOL-ANM-01-021-044}

**Pregunta.** ¿Qué da un primer orden no nulo impar?

**Solución.** No hay extremo local interior: el incremento de la función cambia de signo entre ambos lados.

### Microcontrol 045

[]{#MA-MIC-ANM-01-021-045}

[]{#MA-MSOL-ANM-01-021-045}

**Pregunta.** ¿Qué concluye el criterio si todas las derivadas disponibles son cero?

**Solución.** No clasifica el centro; datos de orden mayor pueden producir mínimo, máximo o ninguna de esas alternativas.

### Microcontrol 046

[]{#MA-MIC-ANM-01-021-046}

[]{#MA-MSOL-ANM-01-021-046}

**Pregunta.** ¿Un mínimo local de Taylor es automáticamente global?

**Solución.** No. $h^2-h^4$ tiene mínimo local en cero y valores negativos lejos; convexidad global era una hipótesis adicional en C20.

### Microcontrol 047

[]{#MA-MIC-ANM-01-021-047}

[]{#MA-MSOL-ANM-01-021-047}

**Pregunta.** ¿Qué cambia al aplicar paridad en una frontera?

**Solución.** Puede faltar uno de los lados; por ejemplo la identidad tiene mínimo de borde en$[0,1]$.

### Microcontrol 048

[]{#MA-MIC-ANM-01-021-048}

[]{#MA-MSOL-ANM-01-021-048}

**Pregunta.** ¿Peano determina por sí solo el signo del resto?

**Solución.** No. Lo hace pequeño frente a un término principal no nulo; una cota firmada de Lagrange añade otra información.

## §21.7 — Aproximantes con certificados racionales

### Microcontrol 049

[]{#MA-MIC-ANM-01-021-049}

[]{#MA-MSOL-ANM-01-021-049}

[]{#MA-SEC-ANM-01-021-007}

**Pregunta.** ¿Qué polinomio central tiene$1/(1-h)$ a orden$n$?

**Solución.** $\sum_{k=0}^n h^k$, por$f^{(k)}(0)=k!$.

### Microcontrol 050

[]{#MA-MIC-ANM-01-021-050}

[]{#MA-MSOL-ANM-01-021-050}

**Pregunta.** ¿Cuál es su resto exacto finito?

**Solución.** $h^{n+1}/(1-h)$, siempre que$h\ne1$ y dentro del dominio declarado.

### Microcontrol 051

[]{#MA-MIC-ANM-01-021-051}

[]{#MA-MSOL-ANM-01-021-051}

**Pregunta.** ¿Qué margen protege el denominador en$|h|\le\rho<1$?

**Solución.** $1-h\ge1-\rho>0$, que produce$|R|\le\rho^{n+1}/(1-\rho)$.

### Microcontrol 052

[]{#MA-MIC-ANM-01-021-052}

[]{#MA-MSOL-ANM-01-021-052}

**Pregunta.** ¿Qué polinomio de orden2 aproxima$\sqrt{1+h}$ en cero?

**Solución.** $1+h/2-h^2/8$.

### Microcontrol 053

[]{#MA-MIC-ANM-01-021-053}

[]{#MA-MSOL-ANM-01-021-053}

**Pregunta.** ¿Qué cota racional de tercera derivada sirve en$|h|\le1/4$?

**Solución.** $0<g^{(3)}\le8/9$, usando$1+h\ge3/4$ y$\sqrt{1+h}\ge3/4$.

### Microcontrol 054

[]{#MA-MIC-ANM-01-021-054}

[]{#MA-MSOL-ANM-01-021-054}

**Pregunta.** ¿Qué certificado da Taylor para$\sqrt{5/4}$?

**Solución.** $143/128<\sqrt{5/4}\le143/128+1/432$; el resto es positivo y está acotado.

### Microcontrol 055

[]{#MA-MIC-ANM-01-021-055}

[]{#MA-MSOL-ANM-01-021-055}

**Pregunta.** ¿Qué diferencia de cuadrados permite un cotejo independiente?

**Solución.** $5/4-(143/128)^2=31/16384$; racionalizar y usar raíz al menos1 da error$\le31/34688$.

### Microcontrol 056

[]{#MA-MIC-ANM-01-021-056}

[]{#MA-MSOL-ANM-01-021-056}

**Pregunta.** ¿Una muestra de derivada basta para certificar el error?

**Solución.** No. La cota debe controlar todo el segmento donde puede encontrarse el testigo.

## §21.8 — Combinar modelos y elegir la resolución

### Microcontrol 057

[]{#MA-MIC-ANM-01-021-057}

[]{#MA-MSOL-ANM-01-021-057}

[]{#MA-SEC-ANM-01-021-008}

**Pregunta.** ¿Qué errores aparecen al multiplicar$P+u$ por$Q+v$?

**Solución.** $Pv+Qu+uv$, además de eliminar términos del producto polinómico que superen el orden fijado.

### Microcontrol 058

[]{#MA-MIC-ANM-01-021-058}

[]{#MA-MSOL-ANM-01-021-058}

**Pregunta.** ¿Por qué un polinomio de términos de grado mayor que$n$ es$o(|h|^n)$?

**Solución.** Se factoriza como$h^{n+1}$ por un polinomio acotado cerca de cero; tras normalizar queda un factor$|h|\to0$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-021-059}

[]{#MA-MSOL-ANM-01-021-059}

**Pregunta.** ¿Qué margen tiene$1-h-h^2$ en$|h|\le1/4$?

**Solución.** Al menos$11/16>0$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-021-060}

[]{#MA-MSOL-ANM-01-021-060}

**Pregunta.** ¿Qué Taylor de orden2 tiene$1/(1-h-h^2)$ en cero?

**Solución.** $1+h+2h^2$; el resto exacto es$(3h^3+2h^4)/(1-h-h^2)$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-021-061}

[]{#MA-MSOL-ANM-01-021-061}

**Pregunta.** ¿Qué orden certifica error menor que$1/1000$ para$1/(1-h)$ en$|h|\le1/4$?

**Solución.** Orden5, con cota$1/3072$; orden4 tiene error$1/768$ en$h=1/4$ y falla.

### Microcontrol 062

[]{#MA-MIC-ANM-01-021-062}

[]{#MA-MSOL-ANM-01-021-062}

**Pregunta.** ¿Qué dos procesos no deben confundirse?

**Solución.** Reducir el radio con un orden fijo y aumentar el grado sobre una región fija; cada uno necesita su propio control del resto.

### Microcontrol 063

[]{#MA-MIC-ANM-01-021-063}

[]{#MA-MSOL-ANM-01-021-063}

**Pregunta.** ¿Cómo preservar datos centrales y un número finito de muestras mientras se cambia otra salida?

**Solución.** Añadiendo$A h^{n+1}\prod_j(h-h_j)^2$; su factor se anula en las muestras y hasta el orden central indicado.

### Microcontrol 064

[]{#MA-MIC-ANM-01-021-064}

[]{#MA-MSOL-ANM-01-021-064}

**Pregunta.** ¿Qué representación infinita se ha probado en este capítulo?

**Solución.** Ninguna. Se prueban polinomios finitos, residuos y cotas; una expansión infinita exige justificar por separado su suma y su resto.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)
