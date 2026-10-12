---
content-id: MA-BCH-0277
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-018-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 18
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C18_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §18.1 — Pendientes con un centro fijo

### Microcontrol 001

[]{#MA-MIC-ANM-01-018-001}

[]{#MA-MSOL-ANM-01-018-001}

[]{#MA-SEC-ANM-01-018-001}

**Pregunta.** ¿Dónde vive el cociente incremental centrado en $a$?

**Solución.** En $D\setminus\{a\}$; $f(a)$ debe existir, pero $q_{f,a}(a)$ no está definido.

### Microcontrol 002

[]{#MA-MIC-ANM-01-018-002}

[]{#MA-MSOL-ANM-01-018-002}

**Pregunta.** ¿Por qué se exige $a\in\operatorname{Acc}(D)$?

**Solución.** Para disponer de entradas distintas del centro en todo radio y garantizar unicidad del límite; en un aislado la condición sería vacía para cualquier pendiente.

### Microcontrol 003

[]{#MA-MIC-ANM-01-018-003}

[]{#MA-MSOL-ANM-01-018-003}

**Pregunta.** ¿Qué variables están fijadas antes de elegir el radio de derivabilidad?

**Solución.** La función, su dominio, el centro y la tolerancia para el error de pendiente. El radio se fija antes de la entrada variable.

### Microcontrol 004

[]{#MA-MIC-ANM-01-018-004}

[]{#MA-MSOL-ANM-01-018-004}

**Pregunta.** ¿Cuál es la derivada de $x^2$ en $a$ y qué identidad la prueba?

**Solución.** Es $2a$, porque el cociente en $a+h$ es $2a+h$ para $h\ne0$ y su diferencia respecto de $2a$ vale $h$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-018-005}

[]{#MA-MSOL-ANM-01-018-005}

**Pregunta.** ¿Una pendiente secante muy grande equivale a una derivada real?

**Solución.** No. La derivada definida aquí exige un límite finito único de todas las secantes suficientemente cercanas.

### Microcontrol 006

[]{#MA-MIC-ANM-01-018-006}

[]{#MA-MSOL-ANM-01-018-006}

**Pregunta.** ¿Qué debe conservar una restricción para heredar la derivada?

**Solución.** El centro y su acumulación en el dominio restringido; luego los mismos radios controlan sus argumentos perforados.

### Microcontrol 007

[]{#MA-MIC-ANM-01-018-007}

[]{#MA-MSOL-ANM-01-018-007}

**Pregunta.** ¿Qué derivada relativa tiene $|x|$ en cero sobre $[0,\infty)$?

**Solución.** Uno: todos los cocientes relativos perforados valen uno. Esto no afirma derivabilidad bilateral sobre toda la recta.

### Microcontrol 008

[]{#MA-MIC-ANM-01-018-008}

[]{#MA-MSOL-ANM-01-018-008}

**Pregunta.** ¿Tiene derivada según R1 una función en un singleton?

**Solución.** No en su único punto, porque ese punto no es de acumulación del dominio.

## §18.2 — El error que desaparece al ampliar

### Microcontrol 009

[]{#MA-MIC-ANM-01-018-009}

[]{#MA-MSOL-ANM-01-018-009}

[]{#MA-SEC-ANM-01-018-002}

**Pregunta.** ¿Qué error identifica la pendiente correcta?

**Solución.** El resto dividido por el incremento, que debe tender a cero; equivalentemente, $|r_L(x)|<\eta|x-a|$ para toda tolerancia en algún radio.

### Microcontrol 010

[]{#MA-MIC-ANM-01-018-010}

[]{#MA-MSOL-ANM-01-018-010}

**Pregunta.** ¿Por qué error absoluto tendente a cero no identifica $L$?

**Solución.** Para una función continua, restar cualquier recta por el centro sigue dando error tendente a cero. La normalización por $x-a$ distingue las pendientes.

### Microcontrol 011

[]{#MA-MIC-ANM-01-018-011}

[]{#MA-MSOL-ANM-01-018-011}

**Pregunta.** ¿Cuánto vale el resto del cuadrado con pendiente $2a$?

**Solución.** $r_{2a}(a+h)=h^2$, por expansión exacta.

### Microcontrol 012

[]{#MA-MIC-ANM-01-018-012}

[]{#MA-MSOL-ANM-01-018-012}

**Pregunta.** ¿Qué papel cumple la acumulación en la unicidad del modelo?

**Solución.** Proporciona una entrada perforada dentro del mínimo de dos radios; al dividir allí, dos pendientes distintas contradicen ambos presupuestos de error.

### Microcontrol 013

[]{#MA-MIC-ANM-01-018-013}

[]{#MA-MSOL-ANM-01-018-013}

**Pregunta.** ¿Qué entradas admite $G_t(u)$?

**Solución.** Sólo las que cumplen $a+tu\in D$; si el dominio está roto no puede suponerse que todo un marco de $u$ sea admisible.

### Microcontrol 014

[]{#MA-MIC-ANM-01-018-014}

[]{#MA-MSOL-ANM-01-018-014}

**Pregunta.** ¿Por qué se limita el marco de zoom a $|u|\le R$?

**Solución.** La cota $\eta|u|$ se convierte en una cota común $\eta R$. Sin limitar $u$, ese presupuesto no protege toda la recta.

### Microcontrol 015

[]{#MA-MIC-ANM-01-018-015}

[]{#MA-MSOL-ANM-01-018-015}

**Pregunta.** ¿Qué significa $o(|x-a|)$ en este capítulo?

**Solución.** Una abreviatura del límite cero del error normalizado sobre el dominio perforado, sin imponer una tasa cuadrática.

### Microcontrol 016

[]{#MA-MIC-ANM-01-018-016}

[]{#MA-MSOL-ANM-01-018-016}

**Pregunta.** ¿La recta de R2 minimiza necesariamente todo error a distancia finita?

**Solución.** No. Su propiedad es el error de orden menor que $|x-a|$ al acercarse al centro.

## §18.3 — Continuidad, esquinas y alcance del control

### Microcontrol 017

[]{#MA-MIC-ANM-01-018-017}

[]{#MA-MSOL-ANM-01-018-017}

[]{#MA-SEC-ANM-01-018-003}

**Pregunta.** ¿Qué tolerancia inicial produce una cota de pendientes?

**Solución.** La tolerancia uno respecto de $L$; resulta $|q|<|L|+1$ cerca del centro.

### Microcontrol 018

[]{#MA-MIC-ANM-01-018-018}

[]{#MA-MSOL-ANM-01-018-018}

**Pregunta.** ¿Cómo se trata el argumento $x=a$ al demostrar continuidad?

**Solución.** Se comprueba aparte: el error de salida es cero. No se evalúa allí el cociente perforado.

### Microcontrol 019

[]{#MA-MIC-ANM-01-018-019}

[]{#MA-MSOL-ANM-01-018-019}

**Pregunta.** ¿Qué radio transforma la cota $C|x-a|$ en error menor que $\varepsilon$?

**Solución.** $\min(r,\varepsilon/C)$ con $C>0$, usando el radio $r$ donde la cota está probada.

### Microcontrol 020

[]{#MA-MIC-ANM-01-018-020}

[]{#MA-MSOL-ANM-01-018-020}

**Pregunta.** ¿Por qué falla la derivada bilateral de $|x|$ en cero?

**Solución.** Las pendientes de las entradas positivas y negativas son uno y menos uno; no pueden acercarse al mismo real con error menor que $1/2$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-018-021}

[]{#MA-MSOL-ANM-01-018-021}

**Pregunta.** ¿Pendiente nula en un punto implica constancia cerca?

**Solución.** No. $x^3$ tiene derivada cero en cero y cambia de valor y de signo arbitrariamente cerca.

### Microcontrol 022

[]{#MA-MIC-ANM-01-018-022}

[]{#MA-MSOL-ANM-01-018-022}

**Pregunta.** ¿Qué centro queda fijo en la cota de R3?

**Solución.** $a$. El resultado compara $f(x)$ con $f(a)$, sin controlar todos los pares $x,y$ próximos.

### Microcontrol 023

[]{#MA-MIC-ANM-01-018-023}

[]{#MA-MSOL-ANM-01-018-023}

**Pregunta.** ¿Qué derivada tiene en cero la función racional/irracional de R3?

**Solución.** Cero, pues su cociente tiene magnitud a lo sumo $|x|$ aunque sea discontinua en todos los otros puntos.

### Microcontrol 024

[]{#MA-MIC-ANM-01-018-024}

[]{#MA-MSOL-ANM-01-018-024}

**Pregunta.** ¿Qué comparación local permite $f\prime(a)>0$?

**Solución.** Cerca del centro, las entradas mayores que $a$ tienen salida mayor que $f(a)$ y las menores tienen salida menor. No es aún monotonía entre todos los pares.

## §18.4 — Operaciones sobre incrementos

### Microcontrol 025

[]{#MA-MIC-ANM-01-018-025}

[]{#MA-MSOL-ANM-01-018-025}

[]{#MA-SEC-ANM-01-018-004}

**Pregunta.** ¿Qué factor requiere continuidad en la prueba del producto?

**Solución.** El factor $f(x)$ en $f(x)q_g(x)+g(a)q_f(x)$; R3 da su límite $f(a)$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-018-026}

[]{#MA-MSOL-ANM-01-018-026}

**Pregunta.** ¿Qué dominio comparte la regla de suma?

**Solución.** Un mismo dominio $D$ para ambos sumandos, con $a\in D\cap\operatorname{Acc}(D)$ y ambas derivadas existentes allí.

### Microcontrol 027

[]{#MA-MIC-ANM-01-018-027}

[]{#MA-MSOL-ANM-01-018-027}

**Pregunta.** ¿Qué margen da $g(a)\ne0$ junto con continuidad?

**Solución.** En una vecindad relativa, $|g(x)|>|g(a)|/2>0$, por lo que el recíproco está definido cerca.

### Microcontrol 028

[]{#MA-MIC-ANM-01-018-028}

[]{#MA-MSOL-ANM-01-018-028}

**Pregunta.** ¿Cuál es el dominio efectivo de $f/g$?

**Solución.** $E=\{x\in D:g(x)\ne0\}$, con numerador restringido expresamente a ese dominio.

### Microcontrol 029

[]{#MA-MIC-ANM-01-018-029}

[]{#MA-MSOL-ANM-01-018-029}

**Pregunta.** ¿Por qué ese dominio efectivo acumula en $a$?

**Solución.** Contiene toda una vecindad relativa de $a$ en $D$ y $a$ ya era de acumulación en $D$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-018-030}

[]{#MA-MSOL-ANM-01-018-030}

**Pregunta.** ¿Qué signo aparece en la derivada de $1/g$?

**Solución.** El negativo: $-(g\prime(a))/g(a)^2$, procedente de la diferencia de recíprocos.

### Microcontrol 031

[]{#MA-MIC-ANM-01-018-031}

[]{#MA-MSOL-ANM-01-018-031}

**Pregunta.** ¿Cómo se trata la potencia cero en el origen?

**Solución.** Como la constante uno, con derivada cero; no se escribe una fórmula que contenga $0a^{-1}$ en $a=0$.

### Microcontrol 032

[]{#MA-MIC-ANM-01-018-032}

[]{#MA-MSOL-ANM-01-018-032}

**Pregunta.** ¿Cancelar $x/x$ añade cero al dominio original?

**Solución.** No. Vale uno y deriva a cero sólo en $\mathbb R\setminus\{0\}$. Incluir cero requiere una extensión distinta.

## §18.5 — La cadena cuando el incremento interior se anula

### Microcontrol 033

[]{#MA-MIC-ANM-01-018-033}

[]{#MA-MSOL-ANM-01-018-033}

[]{#MA-SEC-ANM-01-018-005}

**Pregunta.** ¿Qué división falla si $g(x)=g(a)$?

**Solución.** La división por $g(x)-g(a)$ en la factorización habitual de secantes; el cociente de la composición sí está definido si $x\ne a$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-018-034}

[]{#MA-MSOL-ANM-01-018-034}

**Pregunta.** ¿Qué valor se asigna al factor exterior $A$ en $b$?

**Solución.** $f\prime(b)$, como valor de una nueva función, sin efectuar la división exterior en el centro.

### Microcontrol 035

[]{#MA-MIC-ANM-01-018-035}

[]{#MA-MSOL-ANM-01-018-035}

**Pregunta.** ¿Por qué $A$ es continua en $b$?

**Solución.** Fuera del centro sus valores convergen a $f\prime(b)$ por derivabilidad, y en el centro su diferencia respecto de ese valor es cero.

### Microcontrol 036

[]{#MA-MIC-ANM-01-018-036}

[]{#MA-MSOL-ANM-01-018-036}

**Pregunta.** ¿Qué identidad admite incremento interior cero?

**Solución.** $q_{f\circ g,a}(x)=A(g(x))q_{g,a}(x)$; ambos incrementos de salida son cero cuando $g(x)=b$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-018-037}

[]{#MA-MSOL-ANM-01-018-037}

**Pregunta.** ¿Exige la cadena una derivada interior no nula?

**Solución.** No. El producto de límites sigue siendo válido si $g\prime(a)=0$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-018-038}

[]{#MA-MSOL-ANM-01-018-038}

**Pregunta.** ¿Qué inclusión de tipos simplifica la composición?

**Solución.** $g:D\to E$ y $f:E\to\mathbb R$, de modo que toda imagen interior es entrada admisible exterior.

### Microcontrol 039

[]{#MA-MIC-ANM-01-018-039}

[]{#MA-MSOL-ANM-01-018-039}

**Pregunta.** ¿Qué condición adicional hay que verificar sobre un dominio efectivo $T$?

**Solución.** $a\in T\cap\operatorname{Acc}(T)$. La acumulación del dominio original y del exterior no la garantiza.

### Microcontrol 040

[]{#MA-MIC-ANM-01-018-040}

[]{#MA-MSOL-ANM-01-018-040}

**Pregunta.** ¿La imagen de una función interior constante acumula en su valor?

**Solución.** No, es un singleton. Aun así la cadena funciona si la función exterior es derivable en su propio dominio acumulante.

## §18.6 — Invertir la pendiente exige volver al punto

### Microcontrol 041

[]{#MA-MIC-ANM-01-018-041}

[]{#MA-MSOL-ANM-01-018-041}

[]{#MA-SEC-ANM-01-018-006}

**Pregunta.** ¿Qué hipótesis construye una inversa única sobre la imagen?

**Solución.** Inyectividad de $f$; cada $y\in f[D]$ tiene un único antecedente en $D$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-018-042}

[]{#MA-MSOL-ANM-01-018-042}

**Pregunta.** ¿Qué asegura la acumulación de la imagen en $f(a)$?

**Solución.** Continuidad de $f$ en el centro, acumulación de $D$ e inyectividad para que un antecedente distinto produzca un valor distinto.

### Microcontrol 043

[]{#MA-MIC-ANM-01-018-043}

[]{#MA-MSOL-ANM-01-018-043}

**Pregunta.** ¿Qué hipótesis aproxima $h(y)$ a $a$ cuando $y$ se acerca a $b$?

**Solución.** Continuidad de la inversa $h$ en $b$; no basta saber que la inversa existe.

### Microcontrol 044

[]{#MA-MIC-ANM-01-018-044}

[]{#MA-MSOL-ANM-01-018-044}

**Pregunta.** ¿Para qué se exige $L\ne0$?

**Solución.** Para separar las pendientes originales de cero y controlar sus recíprocos mediante el margen $|L|/2$.

### Microcontrol 045

[]{#MA-MIC-ANM-01-018-045}

[]{#MA-MSOL-ANM-01-018-045}

**Pregunta.** ¿Por qué $y\ne b$ implica $h(y)\ne a$?

**Solución.** Porque $h(y)=a$ daría $y=f(h(y))=f(a)=b$, contradicción.

### Microcontrol 046

[]{#MA-MIC-ANM-01-018-046}

[]{#MA-MSOL-ANM-01-018-046}

**Pregunta.** ¿Cuál es la derivada de la raíz en $b>0$?

**Solución.** $1/(2\sqrt b)$, aplicando la inversa del cuadrado en $a=\sqrt b>0$.

### Microcontrol 047

[]{#MA-MIC-ANM-01-018-047}

[]{#MA-MSOL-ANM-01-018-047}

**Pregunta.** ¿Por qué no se deriva primero $f\circ h=\mathrm{id}$ para probar R6?

**Solución.** Eso aplicaría la cadena suponiendo ya la derivabilidad de $h$, precisamente lo que falta demostrar.

### Microcontrol 048

[]{#MA-MIC-ANM-01-018-048}

[]{#MA-MSOL-ANM-01-018-048}

**Pregunta.** ¿Qué falla para la raíz en cero?

**Solución.** Su cociente relativo es $1/\sqrt y$, sin límite real finito. La pendiente del cuadrado que se invertiría vale cero.

## §18.7 — Una derivada es otra función

### Microcontrol 049

[]{#MA-MIC-ANM-01-018-049}

[]{#MA-MSOL-ANM-01-018-049}

[]{#MA-SEC-ANM-01-018-007}

**Pregunta.** ¿Cuál es el dominio de $f\prime$?

**Solución.** $\operatorname{Diff}(f)$: centros del dominio que son de acumulación y donde el límite de pendientes existe finito.

### Microcontrol 050

[]{#MA-MIC-ANM-01-018-050}

[]{#MA-MSOL-ANM-01-018-050}

**Pregunta.** ¿Puede preguntarse continuidad de $f\prime$ en un punto donde no está definida?

**Solución.** No. Puede preguntarse un límite si el punto acumula en su dominio, pero continuidad requiere un valor en el punto.

### Microcontrol 051

[]{#MA-MIC-ANM-01-018-051}

[]{#MA-MSOL-ANM-01-018-051}

**Pregunta.** ¿Qué impide solapamiento de los intervalos $I_n$?

**Solución.** La suma de semianchos vecinos $5c_n^2/32$ es menor que la distancia entre centros $c_n/2$; los intervalos ordenados quedan separados.

### Microcontrol 052

[]{#MA-MIC-ANM-01-018-052}

[]{#MA-MSOL-ANM-01-018-052}

**Pregunta.** ¿Qué cota prueba $F\prime(0)=0$?

**Solución.** $0\le F(x)\le x^2/2$, por lo que el cociente centrado en cero tiene magnitud a lo sumo $|x|/2$.

### Microcontrol 053

[]{#MA-MIC-ANM-01-018-053}

[]{#MA-MSOL-ANM-01-018-053}

**Pregunta.** ¿Por qué coinciden las derivadas en los extremos de cada bulto?

**Solución.** La rama interior se anula con orden al menos dos y da cociente tendente a cero; la rama exterior es cero.

### Microcontrol 054

[]{#MA-MIC-ANM-01-018-054}

[]{#MA-MSOL-ANM-01-018-054}

**Pregunta.** ¿Qué puntos refutan continuidad de $F\prime$ en cero?

**Solución.** $x_n=c_n+w_n/2\to0$, con $F\prime(x_n)=-3/2$ para todo $n$, frente a $F\prime(0)=0$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-018-055}

[]{#MA-MSOL-ANM-01-018-055}

**Pregunta.** ¿Cómo se evita usar un pegado infinito sin justificación?

**Solución.** Fuera de cero sólo hay finitos intervalos en una vecindad; cero se trata directamente con la cota global del cociente.

### Microcontrol 056

[]{#MA-MIC-ANM-01-018-056}

[]{#MA-MSOL-ANM-01-018-056}

**Pregunta.** ¿La figura con varios bultos prueba el caso infinito?

**Solución.** No. La prueba usa fórmulas y cotas para todo $n$; la imagen representa una muestra finita.

## §18.8 — Certificar una aproximación local

### Microcontrol 057

[]{#MA-MIC-ANM-01-018-057}

[]{#MA-MSOL-ANM-01-018-057}

[]{#MA-SEC-ANM-01-018-008}

**Pregunta.** ¿Qué dato convierte una recta local en certificado cuadrático?

**Solución.** Una cota demostrada $|r(a+h)|\le Bh^2$ en una vecindad especificada, adicional a la mera existencia de la derivada.

### Microcontrol 058

[]{#MA-MIC-ANM-01-018-058}

[]{#MA-MSOL-ANM-01-018-058}

**Pregunta.** ¿Cuánto vale el modelo de $\sqrt{1+h}$ en $h=1/100$?

**Solución.** $1+h/2=201/200$; el error absoluto está acotado por $1/20000$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-018-059}

[]{#MA-MSOL-ANM-01-018-059}

**Pregunta.** ¿En qué lado del valor exacto queda ese modelo de raíz?

**Solución.** Por encima: el resto exacto es $-h^2/[2(\sqrt{1+h}+1)^2]\le0$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-018-060}

[]{#MA-MSOL-ANM-01-018-060}

**Pregunta.** ¿Qué diferencia hay entre error de valor y error de pendiente secante?

**Solución.** El segundo es el resto dividido por $h\ne0$; con cota $Bh^2$, sus magnitudes son a lo sumo $Bh^2$ y $B|h|$, respectivamente.

### Microcontrol 061

[]{#MA-MIC-ANM-01-018-061}

[]{#MA-MSOL-ANM-01-018-061}

**Pregunta.** ¿La derivabilidad garantiza resto cuadrático?

**Solución.** No. $|x|\sqrt{|x|}$ tiene derivada cero en cero, pero el cociente de su resto por $x^2$ es $1/\sqrt{|x|}$ y no está acotado.

### Microcontrol 062

[]{#MA-MIC-ANM-01-018-062}

[]{#MA-MSOL-ANM-01-018-062}

**Pregunta.** ¿Qué significa el producto vacío en $p_c$?

**Solución.** Uno. Si las únicas muestras son el centro, la construcción da simplemente $p_c(x)=cx$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-018-063}

[]{#MA-MSOL-ANM-01-018-063}

**Pregunta.** ¿Qué derivada en cero tiene $p_c$ aunque sus muestras sean cero?

**Solución.** $c$, pues su cociente es $c$ por un producto finito de factores que tienden a uno.

### Microcontrol 064

[]{#MA-MIC-ANM-01-018-064}

[]{#MA-MSOL-ANM-01-018-064}

**Pregunta.** ¿Qué controla un certificado de derivada que no controla una tabla finita?

**Solución.** Todas las entradas admisibles dentro de un radio para cada tolerancia, no sólo los puntos muestreados.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)
