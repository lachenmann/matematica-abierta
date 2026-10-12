---
content-id: MA-BCH-0274
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-018
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
title: 'Capítulo 18 — Diferenciabilidad: mirar cada vez más cerca'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C18.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-18)

Una secante compara cambios de valores; una derivada identifica un único límite finito de esas pendientes. Al ampliar alrededor del centro, esa pendiente será la única recta cuyo error se vuelve pequeño en relación con la escala de entrada. Estudiaremos lo que esta información permite y las hipótesis que impiden convertirla en conclusiones demasiado fuertes.

Los prerrequisitos centrales son límites relativos de C13 y continuidad de C14. Acumulación y densidad C04, rutas dadas C06, raíces C10 y tipos/finitud C12 son interfaces heredadas. C15/C16 sólo se mencionan como garantías adicionales de continuidad de inversas. Todas las reglas se prueban antes de reutilizarlas. No usamos Rolle, valor medio, convexidad, Taylor ni integrales; el zoom se controla por estimaciones explícitas dentro de marcos admisibles.

## 18.1. Pendientes con un centro fijo

[]{#MA-SEC-ANM-01-018-001}

La secante conserva un extremo en $(a,f(a))$ y mueve el otro dentro del dominio. Su pendiente compara cambio de salida con cambio de entrada. Para hablar de un límite de pendientes debemos poder acercarnos al centro con puntos distintos de él.

**R1 — Derivada relativa.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Definimos una función perforada
$$q_{f,a}:D\setminus\{a\}\to\mathbb R,\qquad q_{f,a}(x)=\frac{f(x)-f(a)}{x-a}.$$
Decimos que $f$ es diferenciable o derivable en $a$, relativamente a $D$, si existe un real $L$ tal que
$$\forall\eta>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ |q_{f,a}(x)-L|<\eta.$$
La unicidad del límite de C13 hace único a $L$, que escribimos $f'(a)$. El dominio de $q$ no contiene $a$: la notación $f'(a)$ designa un límite, nunca una división por cero. El valor $f(a)$ sí interviene en cada secante.

**Por qué la acumulación es necesaria.** Si $a$ fuera aislado, un radio sin otros puntos haría verdadera la condición para cualquier $L$. Por ejemplo, una función en $\{0\}$ no tendría una pendiente identificada. Nuestra definición excluye esa vacuidad. En $D=[0,\infty)$, el cero sí es de acumulación; el límite relativo usa sólo entradas positivas. Hay que indicar ese dominio: una derivada derecha no es automáticamente una derivada bilateral en $\mathbb R$.

**Primera reutilización.** Para $f(x)=mx+b$ en $\mathbb R$, $q_{f,a}=m$ y $f'(a)=m$. Para $f(x)=x^2$,
$$q_{f,a}(a+h)=2a+h\qquad(h\ne0).$$
El radio $\delta=\eta$ prueba $f'(a)=2a$ para cada $a$. En particular las secantes del cuadrado centradas en uno tienen pendientes $2+h$, que convergen a dos desde ambos lados. Para $x^3$ en cero el cociente es $h^2$, con radio $\sqrt\eta$. Una pendiente infinita no es un real $L$; la raíz en cero tendrá precisamente esa dificultad.

![Para x² en a=1, las secantes de incrementos 1/2, −1/2 y 1/10 tienen pendientes 5/2, 3/2 y 21/10. La función de pendientes es 2+h para h≠0; el círculo abierto recuerda que no se evalúa el cociente en h=0. El límite es dos, probado para todos los argumentos por R1.](../../assets/books/anm/C18/C18-F01.svg){#fig-anm-c18-f01 fig-alt="Para x² en a=1, las secantes de incrementos 1/2, −1/2 y 1/10 tienen pendientes 5/2, 3/2 y 21/10. La función de pendientes es 2+h para h≠0; el círculo abierto recuerda que no se evalúa el cociente en h=0. El límite es dos, probado para todos los argumentos por R1."}

**Restricción que conserva el centro.** Si $a\in A\subseteq D$ y $a\in\operatorname{Acc}(A)$, una derivada respecto de $D$ conserva su valor respecto de $A$: los mismos radios sirven sobre menos entradas. La recíproca falla: restringir $|x|$ a $[0,\infty)$ elimina las secantes izquierdas. Si $A$ coincide con $D$ dentro de alguna bola centrada en $a$, la acumulación y las pendientes cercanas se conservan en ambos sentidos. Para un radio arbitrario $r$, un testigo de acumulación en una bola menor que $\min(r,\rho)$ pertenece también a $A$.

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-018-001}

¿Dónde vive el cociente incremental centrado en $a$?

[]{#MA-MSOL-ANM-01-018-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

En $D\setminus\{a\}$; $f(a)$ debe existir, pero $q_{f,a}(a)$ no está definido.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-018-002}

¿Por qué se exige $a\in\operatorname{Acc}(D)$?

[]{#MA-MSOL-ANM-01-018-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Para disponer de entradas distintas del centro en todo radio y garantizar unicidad del límite; en un aislado la condición sería vacía para cualquier pendiente.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-018-003}

¿Qué variables están fijadas antes de elegir el radio de derivabilidad?

[]{#MA-MSOL-ANM-01-018-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

La función, su dominio, el centro y la tolerancia para el error de pendiente. El radio se fija antes de la entrada variable.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-018-004}

¿Cuál es la derivada de $x^2$ en $a$ y qué identidad la prueba?

[]{#MA-MSOL-ANM-01-018-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

Es $2a$, porque el cociente en $a+h$ es $2a+h$ para $h\ne0$ y su diferencia respecto de $2a$ vale $h$.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-018-005}

¿Una pendiente secante muy grande equivale a una derivada real?

[]{#MA-MSOL-ANM-01-018-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

No. La derivada definida aquí exige un límite finito único de todas las secantes suficientemente cercanas.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-018-006}

¿Qué debe conservar una restricción para heredar la derivada?

[]{#MA-MSOL-ANM-01-018-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

El centro y su acumulación en el dominio restringido; luego los mismos radios controlan sus argumentos perforados.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-018-007}

¿Qué derivada relativa tiene $|x|$ en cero sobre $[0,\infty)$?

[]{#MA-MSOL-ANM-01-018-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Uno: todos los cocientes relativos perforados valen uno. Esto no afirma derivabilidad bilateral sobre toda la recta.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-018-008}

¿Tiene derivada según R1 una función en un singleton?

[]{#MA-MSOL-ANM-01-018-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No en su único punto, porque ese punto no es de acumulación del dominio.

</details>

### Ejercicios de la sección 18.1

[]{#ejercicios-18}

#### Ejercicio 1. El centro y el dominio perforado

[]{#MA-EX-ANM-01-018-001}

Escribe la definición relativa de derivada para $f:D\to\mathbb R$ y explica por qué un centro aislado no sirve. Trata $D=\{0\}$ y $D=[0,\infty)$.

[]{#MA-SOL-ANM-01-018-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Se exige $a\in D\cap\operatorname{Acc}(D)$ y un real $L$ con $\forall\eta>0\exists\delta>0\forall x\in D$, $0<|x-a|<\delta$ implica $|(f(x)-f(a))/(x-a)-L|<\eta$. El cociente vive en $D\setminus\{a\}$. En un aislado existe un radio sin entradas perforadas, de modo que cualquier $L$ cumpliría la condición vacía y se perdería unicidad. En $\{0\}$ no se define derivada. En $[0,\infty)$, cero es de acumulación y el límite relativo sólo usa entradas positivas; es un concepto de derivada derecha respecto de ese dominio.

</details>

#### Ejercicio 2. Secantes del cuadrado

[]{#MA-EX-ANM-01-018-002}

Calcula la pendiente secante de $x^2$ centrada en $a$. Prueba la derivada con radio explícito y compara los valores para $a=1$, $h=1/2,-1/2,1/10$.

[]{#MA-SOL-ANM-01-018-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Para $h\ne0$, $[(a+h)^2-a^2]/h=2a+h$. Dada tolerancia $\eta>0$, $\delta=\eta$ hace la diferencia respecto de $2a$ menor que $\eta$, así $f\prime(a)=2a$. En uno, las tres pendientes son $5/2,3/2,21/10$. Ninguna secante concreta se identifica con la derivada sólo por estar cerca; el límite es dos y controla todas las entradas suficientemente próximas.

**Retorno visual.** Véase [C18-F01](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 3. Dos límites candidatos

[]{#MA-EX-ANM-01-018-003}

Prueba directamente unicidad de la derivada con acumulación, sin usar una sucesión seleccionada.

[]{#MA-SOL-ANM-01-018-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Si $L,M$ cumplen la definición y $d=|L-M|>0$, pedimos tolerancia $d/3$ a ambas condiciones. El mínimo de sus radios es positivo. Acumulación entrega un único testigo perforado dentro de ese mínimo. Para su pendiente $q$, $d\le|L-q|+|q-M|<2d/3$, contradicción. Se obtiene existencia de un testigo para el radio fijado, sin una elección simultánea de entradas.

</details>

#### Ejercicio 4. Una restricción pierde un lado

[]{#MA-EX-ANM-01-018-004}

Prueba la derivada relativa de $|x|$ en cero sobre $[0,\infty)$ y refuta inferir de ella la derivada sobre $\mathbb R$.

[]{#MA-SOL-ANM-01-018-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

En el dominio positivo perforado, el cociente es $|x|/x=1$, así cualquier radio sirve para cualquier tolerancia y la derivada relativa es uno. Sobre la recta, el cociente en las entradas negativas es menos uno. Para todo radio hay entradas positivas y negativas con pendientes separadas por dos, incompatibles con acercamiento común a un real. La restricción de una derivada existente la conserva si acumula en el centro, pero una derivada restringida puede omitir entradas que impiden el límite en el dominio mayor.

</details>

#### Ejercicio 5. Cambiar el valor central

[]{#MA-EX-ANM-01-018-005}

Sea $F(x)=x^2$ para $x\ne0$ y $F(0)=1$. Decide derivabilidad en cero y compara con el cuadrado usual.

[]{#MA-SOL-ANM-01-018-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Para $x\ne0$, $q_{F,0}(x)=x-1/x$, que no tiene límite finito en cero. Más directamente, $F$ no es continua en cero: las entradas $x_n=1/(n+1)$ tienen salidas tendentes a cero, distintas del valor central uno; R3 refuta derivabilidad. Este uso de R3 es una consecuencia posterior de R1 dentro del capítulo. El cuadrado usual sí tiene valor central cero y derivada cero. Que dos funciones coincidan en el dominio perforado no garantiza iguales cocientes si sus valores centrales difieren.

</details>
## 18.2. El error que desaparece al ampliar

[]{#MA-SEC-ANM-01-018-002}

Una recta que pase por el punto puede tener error absoluto tendente a cero sin tener la pendiente correcta. La escala relevante compara ese error con el incremento que estamos ampliando.

**R2 — Mejor aproximación lineal local.** Con los tipos y el centro de R1, sea
$$r_L(x)=f(x)-f(a)-L(x-a),\qquad r_L(a)=0.$$
Entonces $f'(a)=L$ si y sólo si
$$\forall\eta>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ |r_L(x)|<\eta|x-a|.$$
**Estrategia y prueba.** Restamos la recta candidata y dividimos únicamente en el dominio perforado. Allí
$$\frac{r_L(x)}{x-a}=q_{f,a}(x)-L,$$
así la condición es exactamente el límite cero de este cociente. Esta equivalencia prueba existencia en ambos sentidos, sin una fórmula futura de Taylor. La notación $r_L(x)=o(|x-a|)$ abrevia esta condición relativa; no designa una función nueva ni una cota cuadrática obligatoria.

**Unicidad desde el error.** Si $L$ y $M$ sirvieran y $d=|L-M|>0$, pedimos a ambas estimaciones presupuesto $d/3$. Tomamos el mínimo de sus dos radios y un solo testigo $x\in D$ distinto de $a$ dentro de él, obtenido de la acumulación. Como $r_M-r_L=(L-M)(x-a)$, al dividir magnitudes resulta $d<2d/3$, contradicción. No se elige una sucesión de testigos.

**Zoom con la misma escala en los dos ejes.** Para $t>0$ y entradas admisibles $u$ tales que $a+tu\in D$, definimos
$$G_t(u)=\frac{f(a+tu)-f(a)}t.$$
Si $|u|\le R$ y $0<t<\delta/(R+1)$, la estimación anterior da $|G_t(u)-Lu|<\eta|u|\le\eta R$ para $u\ne0$; en $u=0$ el error es cero. Para un presupuesto $\varepsilon>0$ elegimos primero $\eta=\varepsilon/(R+1)$ y luego ese límite para $t$. Todos los puntos admisibles del marco $|u|\le R$ quedan a error menor que $\varepsilon$. Si $D$ contiene una vecindad de $a$, todo el marco se vuelve admisible para $t$ pequeño; en dominios rotos hay que conservar el conjunto de $u$ permitido. Aquí se prueba una estimación común, sin introducir teoría de sucesiones de funciones.

![Para el cuadrado en a=1, G_t(u)=2u+tu². Los tres paneles usan el mismo marco |u|≤2 y los mismos ejes; el error respecto de 2u está acotado por 4t. Se ilustran t=1/2,1/8,1/32. La prueba controla todos los puntos del marco, sin inferir el límite de tres imágenes.](../../assets/books/anm/C18/C18-F02.svg){#fig-anm-c18-f02 fig-alt="Para el cuadrado en a=1, G_t(u)=2u+tu². Los tres paneles usan el mismo marco |u|≤2 y los mismos ejes; el error respecto de 2u está acotado por 4t. Se ilustran t=1/2,1/8,1/32. La prueba controla todos los puntos del marco, sin inferir el límite de tres imágenes."}

**Ejemplo y diagnóstico.** Para el cuadrado, $r_{2a}(a+h)=h^2$ y $G_t(u)=2au+tu^2$. La desaparición del término $tu^2$ explica el acercamiento a la recta dentro de un marco acotado. Con otra pendiente $M$, el error absoluto $(2a-M)h+h^2$ también tiende a cero, pero su cociente por $h$ tiende a $2a-M$, que sólo es cero para $M=2a$. «Mejor» significa única recta con error de orden menor que $|h|$, sin afirmar que minimice cada error a distancia finita.

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-018-009}

¿Qué error identifica la pendiente correcta?

[]{#MA-MSOL-ANM-01-018-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

El resto dividido por el incremento, que debe tender a cero; equivalentemente, $|r_L(x)|<\eta|x-a|$ para toda tolerancia en algún radio.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-018-010}

¿Por qué error absoluto tendente a cero no identifica $L$?

[]{#MA-MSOL-ANM-01-018-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

Para una función continua, restar cualquier recta por el centro sigue dando error tendente a cero. La normalización por $x-a$ distingue las pendientes.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-018-011}

¿Cuánto vale el resto del cuadrado con pendiente $2a$?

[]{#MA-MSOL-ANM-01-018-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

$r_{2a}(a+h)=h^2$, por expansión exacta.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-018-012}

¿Qué papel cumple la acumulación en la unicidad del modelo?

[]{#MA-MSOL-ANM-01-018-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Proporciona una entrada perforada dentro del mínimo de dos radios; al dividir allí, dos pendientes distintas contradicen ambos presupuestos de error.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-018-013}

¿Qué entradas admite $G_t(u)$?

[]{#MA-MSOL-ANM-01-018-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Sólo las que cumplen $a+tu\in D$; si el dominio está roto no puede suponerse que todo un marco de $u$ sea admisible.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-018-014}

¿Por qué se limita el marco de zoom a $|u|\le R$?

[]{#MA-MSOL-ANM-01-018-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

La cota $\eta|u|$ se convierte en una cota común $\eta R$. Sin limitar $u$, ese presupuesto no protege toda la recta.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-018-015}

¿Qué significa $o(|x-a|)$ en este capítulo?

[]{#MA-MSOL-ANM-01-018-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

Una abreviatura del límite cero del error normalizado sobre el dominio perforado, sin imponer una tasa cuadrática.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-018-016}

¿La recta de R2 minimiza necesariamente todo error a distancia finita?

[]{#MA-MSOL-ANM-01-018-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

No. Su propiedad es el error de orden menor que $|x-a|$ al acercarse al centro.

</details>

### Ejercicios de la sección 18.2

#### Ejercicio 6. Traducir el error

[]{#MA-EX-ANM-01-018-006}

Prueba equivalencia entre derivada $L$ y resto $r_L=o(|x-a|)$ sobre el dominio relativo.

[]{#MA-SOL-ANM-01-018-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Para $x\ne a$, $r_L(x)/(x-a)=q_{f,a}(x)-L$. Por tanto la condición de límite cero de ese cociente equivale término a término a la definición de derivada. En magnitudes, multiplicar o dividir por el positivo $|x-a|$ traduce $|q-L|<\eta$ en $|r_L|<\eta|x-a|$. En el centro $r_L(a)=0$, sin atribuir allí un cociente. Ambos sentidos conservan el mismo radio y dominio perforado.

</details>

#### Ejercicio 7. Un marco completo de zoom

[]{#MA-EX-ANM-01-018-007}

Para $f(x)=x^2$, centro uno y $|u|\le2$, escribe $G_t$ y da una condición en $t>0$ para error menor que $\varepsilon$ respecto de la recta límite.

[]{#MA-SOL-ANM-01-018-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

$G_t(u)=[(1+tu)^2-1]/t=2u+tu^2$. En el marco $|u|\le2$, el error es $tu^2\le4t$. Si $0<t<\varepsilon/4$, es menor que $\varepsilon$ para todos los puntos del marco simultáneamente. El dominio es toda la recta, así todos son admisibles. El marco acotado permite una cota común; sin acotarlo el término $tu^2$ no queda pequeño para todo $u$ con un mismo $t>0$.

**Retorno visual.** Véase [C18-F02](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 8. Todas las rectas tienen error absoluto pequeño

[]{#MA-EX-ANM-01-018-008}

Para el cuadrado centrado en $a$, demuestra que cualquier recta de pendiente $M$ por el punto tiene error absoluto tendente a cero. Explica por qué sólo $M=2a$ es modelo de primer orden.

[]{#MA-SOL-ANM-01-018-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

El resto es $(2a-M)h+h^2$, cuya magnitud no supera $(|2a-M|+|h|)|h|$ y tiende a cero cuando $h\to0$. Pero su cociente por $h$ es $2a-M+h$, con límite $2a-M$. Este límite sólo vale cero si $M=2a$. El error absoluto no distingue pendientes porque todas las rectas pasan por el mismo punto y son continuas allí; el error normalizado sí las distingue.

</details>

#### Ejercicio 9. No hace falta escoger rutas

[]{#MA-EX-ANM-01-018-009}

Prueba unicidad del modelo lineal usando únicamente estimaciones de resto y un testigo de acumulación.

[]{#MA-SOL-ANM-01-018-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Si sirven $L,M$ distintos, sea $d=|L-M|>0$. Las estimaciones con presupuesto $d/3$ entregan dos radios. Acumulación permite un punto distinto del centro en el menor de ellos. Como $(L-M)(x-a)=r_M(x)-r_L(x)$, la triangular y ambas cotas dan $d|x-a|<2d|x-a|/3$. Dividir por $|x-a|>0$ contradice $d>0$. No se construye una sucesión ni se elige un testigo para cada radio a la vez.

</details>

#### Ejercicio 10. Zoom sobre un dominio roto

[]{#MA-EX-ANM-01-018-010}

Sea $D=\{0\}\cup\{1/(n+1):n\in\mathbb N\}$ y $f(x)=x^2$ en $D$. Prueba derivada relativa en cero y describe las entradas permitidas del zoom.

[]{#MA-SOL-ANM-01-018-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Cero acumula en $D$ por las entradas explícitas $1/(n+1)$. Para $x\in D\setminus\{0\}$, $q=x$, por lo que $\delta=\eta$ prueba derivada cero. Para $t>0$, las entradas del zoom son $u=0$ y $u=1/[t(n+1)]$. Allí $G_t(u)=tu^2$. En $|u|\le R$ el error no supera $tR^2$, pero no se ha definido $G_t$ en los otros puntos del marco. La estimación es común a las entradas admisibles y no rellena los huecos del dominio.

</details>
## 18.3. Continuidad, esquinas y alcance del control

[]{#MA-SEC-ANM-01-018-003}

El límite finito de pendientes tiene una consecuencia inmediata sobre valores. Conviene demostrarla antes de usar álgebra o composición de derivadas.

**R3 — Diferenciabilidad implica continuidad.** Sean $L=f'(a)$ y $C=|L|+1>0$. La tolerancia uno en R1 entrega un radio $r$ para el que $|q_{f,a}(x)|<C$ en la bola perforada. Por tanto
$$|f(x)-f(a)|<C|x-a|\qquad(0<|x-a|<r,\ x\in D).$$
Para $\varepsilon>0$, $\delta=\min(r,\varepsilon/C)$ controla el error de salida por $\varepsilon$ si $x\ne a$; si $x=a$, el error vale cero. Ésta es la continuidad de C14 sobre el mismo dominio. También queda la cota no estricta $|f(x)-f(a)|\le C|x-a|$ incluyendo el centro.

**La cota tiene un centro fijo.** No controla automáticamente $|f(x)-f(y)|$ por $C|x-y|$ para cualquier par vecino. Para ver la diferencia, definamos $F:\mathbb R\to\mathbb R$ por $F(x)=x^2$ si $x\in\mathbb Q$ y $F(x)=0$ si $x\notin\mathbb Q$. En cero, $F(0)=0$ y $|q_{F,0}(x)|\le|x|$, así $F'(0)=0$. En cualquier $b\ne0$, la densidad de racionales e irracionales impide continuidad. Si $b$ es racional, irracionales arbitrariamente próximos tienen salida cero, separada de $b^2$. Si es irracional, racionales próximos con $|x-b|<|b|/2$ tienen $x^2>b^2/4$ mientras $F(b)=0$. Un control Lipschitz para todos los pares de alguna vecindad de cero implicaría continuidad en sus puntos interiores, contradicción. Diferenciabilidad en un punto no asegura diferenciabilidad cerca.

**Una esquina continua.** La triangular inversa da $||x|-|y||\le|x-y|$, por lo que $|x|$ es continua. Su cociente en cero vale uno para $x>0$ y menos uno para $x<0$. Si existiera un límite $L$, con tolerancia $1/2$ y testigos $\pm\delta/2$ tendríamos $|1-L|<1/2$ y $|-1-L|<1/2$, contradiciendo $2\le|1-L|+|L+1|$. Una gráfica puede mostrar la esquina; los dos testigos refutan todo radio candidato.

![La función |x| es continua en cero, pero su cociente perforado vale −1 a la izquierda y 1 a la derecha. Los puntos abiertos indican que el cociente no se define en cero. R3 refuta cualquier límite común mediante los testigos ±δ/2. Sobre el dominio no negativo sólo permanece la rama derecha.](../../assets/books/anm/C18/C18-F03.svg){#fig-anm-c18-f03 fig-alt="La función |x| es continua en cero, pero su cociente perforado vale −1 a la izquierda y 1 a la derecha. Los puntos abiertos indican que el cociente no se define en cero. R3 refuta cualquier límite común mediante los testigos ±δ/2. Sobre el dominio no negativo sólo permanece la rama derecha."}

**Pendiente nula no significa constancia.** $x^3$ tiene derivada cero en cero y cambia de signo allí: no es constante ni tiene extremo en ese punto. El dato sólo identifica su recta local horizontal. Si $L>0$, la tolerancia $L/2$ sí asegura que $q_{f,a}(x)>0$ cerca: las salidas a la derecha superan $f(a)$ y las de la izquierda quedan por debajo. Son comparaciones con $a$, sin una conclusión sobre todos los pares de la vecindad. El paso a propiedades en intervalos exigirá otras herramientas.

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-018-017}

¿Qué tolerancia inicial produce una cota de pendientes?

[]{#MA-MSOL-ANM-01-018-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

La tolerancia uno respecto de $L$; resulta $|q|<|L|+1$ cerca del centro.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-018-018}

¿Cómo se trata el argumento $x=a$ al demostrar continuidad?

[]{#MA-MSOL-ANM-01-018-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Se comprueba aparte: el error de salida es cero. No se evalúa allí el cociente perforado.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-018-019}

¿Qué radio transforma la cota $C|x-a|$ en error menor que $\varepsilon$?

[]{#MA-MSOL-ANM-01-018-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

$\min(r,\varepsilon/C)$ con $C>0$, usando el radio $r$ donde la cota está probada.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-018-020}

¿Por qué falla la derivada bilateral de $|x|$ en cero?

[]{#MA-MSOL-ANM-01-018-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Las pendientes de las entradas positivas y negativas son uno y menos uno; no pueden acercarse al mismo real con error menor que $1/2$.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-018-021}

¿Pendiente nula en un punto implica constancia cerca?

[]{#MA-MSOL-ANM-01-018-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

No. $x^3$ tiene derivada cero en cero y cambia de valor y de signo arbitrariamente cerca.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-018-022}

¿Qué centro queda fijo en la cota de R3?

[]{#MA-MSOL-ANM-01-018-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

$a$. El resultado compara $f(x)$ con $f(a)$, sin controlar todos los pares $x,y$ próximos.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-018-023}

¿Qué derivada tiene en cero la función racional/irracional de R3?

[]{#MA-MSOL-ANM-01-018-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

Cero, pues su cociente tiene magnitud a lo sumo $|x|$ aunque sea discontinua en todos los otros puntos.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-018-024}

¿Qué comparación local permite $f\prime(a)>0$?

[]{#MA-MSOL-ANM-01-018-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

Cerca del centro, las entradas mayores que $a$ tienen salida mayor que $f(a)$ y las menores tienen salida menor. No es aún monotonía entre todos los pares.

</details>

### Ejercicios de la sección 18.3

#### Ejercicio 11. De pendientes a valores

[]{#MA-EX-ANM-01-018-011}

Reconstruye la prueba de continuidad desde una derivada finita, incluidos los presupuestos y el centro.

[]{#MA-SOL-ANM-01-018-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

La tolerancia uno de derivabilidad da $r>0$ con $|q-L|<1$ en el radio perforado, así $|q|<C=|L|+1>0$. Multiplicar por $|x-a|$ da error de valores menor que $C|x-a|$. Para $\varepsilon>0$, $\delta=\min(r,\varepsilon/C)$ sirve para todo argumento distinto del centro de distancia menor. En el centro el error es cero. Esta última comprobación convierte un control perforado en continuidad sobre una bola no perforada del mismo dominio.

</details>

#### Ejercicio 12. La esquina refuta todos los radios

[]{#MA-EX-ANM-01-018-012}

Prueba continuidad de $|x|$ en toda la recta y no derivabilidad en cero con dos testigos para un radio arbitrario.

[]{#MA-SOL-ANM-01-018-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

La triangular inversa da $||x|-|a||\le|x-a|$, de modo que $\delta=\varepsilon$ prueba continuidad en cada $a$. Si existiera derivada $L$ en cero, tolerancia $1/2$ daría un radio $\delta$. En $\delta/2$ y $-\delta/2$ los cocientes valen uno y menos uno, respectivamente, y ambos tendrían error menor que $1/2$ respecto de $L$. Entonces $2\le|1-L|+|L+1|<1$, contradicción. La prueba no se apoya en la apariencia del gráfico.

**Retorno visual.** Véase [C18-F03](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 13. Pendiente cero sin extremo

[]{#MA-EX-ANM-01-018-013}

Prueba que $x^3$ tiene derivada cero en cero y que allí no es constante ni tiene máximo o mínimo local.

[]{#MA-SOL-ANM-01-018-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Para $h\ne0$, el cociente vale $h^2$; $\delta=\sqrt\eta$ da error menor que $\eta$ y prueba derivada cero. Todo radio admite $h=\delta/2>0$ y $-h<0$, con valores $h^3>0$ y $-h^3<0$ respecto del valor central cero. Así ninguna vecindad relativa tiene todos sus valores por encima o por debajo del central, y tampoco son constantes. La recta horizontal local no contiene información suficiente para decidir extremos.

</details>

#### Ejercicio 14. Control centrado sin Lipschitz vecino

[]{#MA-EX-ANM-01-018-014}

Analiza $F(x)=x^2$ en racionales y cero en irracionales. Prueba $F\prime(0)=0$ y que no es Lipschitz en ninguna vecindad de cero.

[]{#MA-SOL-ANM-01-018-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Como $F(0)=0$ y $|F(x)|\le x^2$, $|q_{F,0}(x)|\le|x|$ prueba derivada cero con $\delta=\eta$. En cada $b\ne0$ es discontinua: si es racional, irracionales arbitrariamente próximos tienen salida cero en lugar de $b^2$; si es irracional, racionales con $|x-b|<|b|/2$ tienen salida mayor que $b^2/4$ en lugar de cero. La densidad garantiza tales testigos en cualquier radio. Una cota Lipschitz para todos los pares de alguna bola de cero implicaría continuidad en cada punto interior de esa bola, por radio $\varepsilon/L$ si $L>0$, o constancia si $L=0$. Elegir allí un $b\ne0$ produce contradicción. La cota centrada de R3 sigue siendo válida y no equivale a esa cota de pares.

</details>

#### Ejercicio 15. Comparar sólo con el centro

[]{#MA-EX-ANM-01-018-015}

Si $f\prime(a)=L>0$, prueba las comparaciones locales con $f(a)$ a cada lado del centro. Indica el alcance exacto.

[]{#MA-SOL-ANM-01-018-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Con tolerancia $L/2$, la definición entrega un radio donde $q>L/2>0$ para argumentos perforados. La identidad $f(x)-f(a)=q(x)(x-a)$ da diferencia positiva para $x>a$ y negativa para $x<a$, dentro de ese radio y del dominio. No se exige que ambos lados tengan entradas; sólo se afirma la implicación cuando las hay. El centro está fijo: no se han comparado salidas de dos entradas arbitrarias diferentes de $a$, por lo que no se ha probado monotonía en toda una vecindad.

</details>
## 18.4. Operaciones sobre incrementos

[]{#MA-SEC-ANM-01-018-004}

Las reglas algebraicas serán identidades de incrementos seguidas de límites. Hay que justificar los dominios antes de cancelar denominadores.

**R4 — Suma y producto.** Sean $f,g:D\to\mathbb R$ derivables en $a\in D\cap\operatorname{Acc}(D)$, con derivadas $L,M$. Para constantes $\alpha,\beta$, la identidad $q_{\alpha f+\beta g,a}=\alpha q_{f,a}+\beta q_{g,a}$ y el álgebra de límites C13 dan
$$ (\alpha f+\beta g)'(a)=\alpha L+\beta M.$$
Para el producto, sumar y restar $f(a)g(x)$ produce
$$q_{fg,a}(x)=f(x)q_{g,a}(x)+g(a)q_{f,a}(x).$$
R3 asegura $f(x)\to f(a)$; C13 permite multiplicar los límites finitos. Así $(fg)'(a)=f(a)M+g(a)L$. La continuidad se usa exactamente para el factor no centrado. Todos los cocientes viven en $D\setminus\{a\}$; no se ha aplicado la cadena.

**Recíproco y cociente.** Si $g(a)\ne0$, continuidad con tolerancia $|g(a)|/2$ da $\rho>0$ tal que $|g(x)|>|g(a)|/2$ en $D\cap B(a,\rho)$. El dominio efectivo $E=\{x\in D:g(x)\ne0\}$ contiene esa vecindad relativa y acumula en $a$. Las derivadas de las restricciones conservan sus valores por R1. En $E\setminus\{a\}$,
$$q_{1/g,a}(x)=-\frac{q_{g,a}(x)}{g(x)g(a)}.$$
Los límites del denominador y el margen anterior justifican
$$ (1/g)'(a)=-\frac{M}{g(a)^2},\qquad
(f/g)'(a)=\frac{L g(a)-f(a)M}{g(a)^2}.$$
La segunda fórmula resulta del producto de $f|_E$ con $1/g$, ambos tipados $E\to\mathbb R$. Es una derivada relativa a $E$, aunque use datos calculados primero sobre $D$.

**Reutilización finita.** De $(x)'=1$, constantes y producto se obtiene por inducción $(x^n)'(a)=na^{n-1}$ para enteros $n\ge1$ en $\mathbb R$. La potencia cero es constante uno y su derivada es cero, sin escribir $0a^{-1}$ en $a=0$. Para enteros $n\ge1$, el recíproco da $(x^{-n})'(a)=-na^{-n-1}$ en $\mathbb R\setminus\{0\}$. Sumas finitas derivan polinomios; cocientes derivan funciones racionales en sus dominios efectivos. No se extiende esta prueba a exponentes reales no construidos.

**Cancelar no cambia el dominio.** $x/x$ en $\mathbb R\setminus\{0\}$ vale uno y tiene derivada cero en cada punto de ese dominio. En cero no hay valor ni derivada. La constante uno en $\mathbb R$ es una extensión distinta. Si numerador y denominador se anulan en el centro, la regla de cociente no sirve; se debe estudiar una extensión expresamente definida, si existe.

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-018-025}

¿Qué factor requiere continuidad en la prueba del producto?

[]{#MA-MSOL-ANM-01-018-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

El factor $f(x)$ en $f(x)q_g(x)+g(a)q_f(x)$; R3 da su límite $f(a)$.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-018-026}

¿Qué dominio comparte la regla de suma?

[]{#MA-MSOL-ANM-01-018-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Un mismo dominio $D$ para ambos sumandos, con $a\in D\cap\operatorname{Acc}(D)$ y ambas derivadas existentes allí.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-018-027}

¿Qué margen da $g(a)\ne0$ junto con continuidad?

[]{#MA-MSOL-ANM-01-018-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

En una vecindad relativa, $|g(x)|>|g(a)|/2>0$, por lo que el recíproco está definido cerca.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-018-028}

¿Cuál es el dominio efectivo de $f/g$?

[]{#MA-MSOL-ANM-01-018-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

$E=\{x\in D:g(x)\ne0\}$, con numerador restringido expresamente a ese dominio.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-018-029}

¿Por qué ese dominio efectivo acumula en $a$?

[]{#MA-MSOL-ANM-01-018-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Contiene toda una vecindad relativa de $a$ en $D$ y $a$ ya era de acumulación en $D$.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-018-030}

¿Qué signo aparece en la derivada de $1/g$?

[]{#MA-MSOL-ANM-01-018-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

El negativo: $-(g\prime(a))/g(a)^2$, procedente de la diferencia de recíprocos.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-018-031}

¿Cómo se trata la potencia cero en el origen?

[]{#MA-MSOL-ANM-01-018-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Como la constante uno, con derivada cero; no se escribe una fórmula que contenga $0a^{-1}$ en $a=0$.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-018-032}

¿Cancelar $x/x$ añade cero al dominio original?

[]{#MA-MSOL-ANM-01-018-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

No. Vale uno y deriva a cero sólo en $\mathbb R\setminus\{0\}$. Incluir cero requiere una extensión distinta.

</details>

### Ejercicios de la sección 18.4

#### Ejercicio 16. El producto como identidad

[]{#MA-EX-ANM-01-018-016}

Deriva suma y producto desde las identidades de cocientes, e indica dónde se usa continuidad.

[]{#MA-SOL-ANM-01-018-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

En el dominio perforado común, $q_{\alpha f+\beta g}=\alpha q_f+\beta q_g$; límites finitos dan $\alpha f\prime(a)+\beta g\prime(a)$. Para producto, sumar y restar $f(a)g(x)$ da $q_{fg}=f(x)q_g+g(a)q_f$. La diferenciabilidad de $f$ da continuidad por R3, así el primer factor tiende a $f(a)$; los demás límites son los de los cocientes o la constante. El resultado es $f(a)g\prime(a)+g(a)f\prime(a)$. Sin ese paso no se habría justificado el límite del factor $f(x)$.

</details>

#### Ejercicio 17. Dominio del recíproco

[]{#MA-EX-ANM-01-018-017}

Prueba la regla del recíproco y justifica acumulación de su dominio efectivo.

[]{#MA-SOL-ANM-01-018-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Si $g(a)\ne0$, continuidad da una vecindad relativa donde $|g(x)|>|g(a)|/2$. Por tanto $E=\{g\ne0\}$ contiene esa vecindad y $a\in E$. Para cada radio, acumulación de $D$ da un testigo perforado dentro de su mínimo con el radio de la vecindad, así $a\in\operatorname{Acc}(E)$. En $E\setminus\{a\}$, $q_{1/g}=-q_g/[g(x)g(a)]$. El denominador tiende al no nulo $g(a)^2$; C13 prueba el límite $-g\prime(a)/g(a)^2$. El margen verifica tanto las divisiones como el dominio de la derivada.

</details>

#### Ejercicio 18. Un cociente racional

[]{#MA-EX-ANM-01-018-018}

Deriva $f(x)=(x+1)/(x^2+1)$ en su dominio real e indica por qué no hay puntos excluidos.

[]{#MA-SOL-ANM-01-018-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

El denominador es $x^2+1\ge1$, así el dominio es toda $\mathbb R$. Numerador y denominador tienen derivadas uno y $2a$. La regla da $f\prime(a)=[(a^2+1)-2a(a+1)]/(a^2+1)^2=(1-2a-a^2)/(a^2+1)^2$. Cada centro real es de acumulación y el denominador no se anula allí. La identidad se obtiene dentro de R4 sin regla de la cadena ni valor medio.

</details>

#### Ejercicio 19. Un hueco no desaparece al cancelar

[]{#MA-EX-ANM-01-018-019}

Una solución simplifica $(x^2-1)/(x-1)$ a $x+1$ y asigna derivada uno en $x=1$. Revisa el dominio y describe una extensión.

[]{#MA-SOL-ANM-01-018-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

La función original tiene dominio $\mathbb R\setminus\{1\}$; no tiene valor ni derivada en uno. En ese dominio coincide con $x+1$ y su derivada es uno en cada centro válido. La función $G:\mathbb R\to\mathbb R$, $G(x)=x+1$, es una extensión distinta que asigna $G(1)=2$ y sí tiene $G\prime(1)=1$. Cancelar permite igualdad de valores donde ambas expresiones están definidas, sin cambiar el dominio de la función original.

</details>

#### Ejercicio 20. Potencias enteras con base cero

[]{#MA-EX-ANM-01-018-020}

Prueba por inducción la derivada de $x^n$ para $n\ge1$, trata $n=0$ y deriva $x^{-n}$ para $n\ge1$.

[]{#MA-SOL-ANM-01-018-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

La base $n=1$ es la identidad, con derivada uno. Si la fórmula vale para $n\ge1$, producto de $x^n$ e identidad da $na^{n-1}a+a^n=(n+1)a^n$, también en cero; no hay exponentes negativos en esa igualdad. La potencia cero es constante uno, con derivada cero por su cociente, sin usar $0a^{-1}$. En el dominio sin cero, recíproco de $x^n$ da $-na^{n-1}/a^{2n}=-na^{-n-1}$. Cada división está legitimada por $a\ne0$.

</details>
## 18.5. La cadena cuando el incremento interior se anula

[]{#MA-SEC-ANM-01-018-005}

En una composición, puede variar $x$ mientras el valor interior permanece igual. Dividir por ese cambio interior perdería argumentos válidos.

**R5 — Regla de la cadena.** Sean $g:D\to E$, $f:E\to\mathbb R$, $a\in D\cap\operatorname{Acc}(D)$ y $b=g(a)\in E\cap\operatorname{Acc}(E)$. Supongamos $g'(a)=L$ y $f'(b)=M$. Construimos la función auxiliar
$$A:E\to\mathbb R,\qquad
A(y)=\begin{cases}\dfrac{f(y)-f(b)}{y-b},&y\ne b,\\ M,&y=b.\end{cases}$$
Es continua en $b$: en argumentos perforados lo dice la definición de $M$; en $b$ la diferencia respecto de $M$ vale cero. No se ha definido un cociente con denominador cero; $A$ es otra función. Para todo $y\in E$ se tiene $f(y)-f(b)=A(y)(y-b)$, también si $y=b$, porque ambos lados valen cero.

**Identidad y paso al límite.** Para todo $x\in D\setminus\{a\}$,
$$q_{f\circ g,a}(x)=A(g(x))q_{g,a}(x).$$
R3 da continuidad de $g$ en $a$; C14 da $A(g(x))\to M$, incluso en los puntos que llegan exactamente a $b$. El álgebra de límites C13 concluye $(f\circ g)'(a)=ML$. Para ver los presupuestos, fijamos $C=|L|+1$: cerca del centro $|q_g|<C$. Pedimos a $A\circ g$ error $\varepsilon/(2C)$ y a $q_g$ error $\varepsilon/[2(|M|+1)]$, además de su cota. El mínimo de los radios da
$$|A(g(x))q_g(x)-ML|\le |A(g(x))-M||q_g(x)|+|M||q_g(x)-L|<\varepsilon.$$
La única división en la identidad es por $x-a\ne0$. No se exige $L\ne0$ ni que $g[D]$ acumule en $b$; una función interior constante queda incluida.

![La interior vale 1 para x<0 y 1+x² para x≥0. Su derivada en cero es cero; la exterior y² tiene derivada dos en uno. La composición tiene derivada cero. En toda la rama negativa el incremento interior es cero: el factor A(1)=2 conserva la identidad de cocientes multiplicándolo por q_g=0, sin división 0/0.](../../assets/books/anm/C18/C18-F04.svg){#fig-anm-c18-f04 fig-alt="La interior vale 1 para x&lt;0 y 1+x² para x≥0. Su derivada en cero es cero; la exterior y² tiene derivada dos en uno. La composición tiene derivada cero. En toda la rama negativa el incremento interior es cero: el factor A(1)=2 conserva la identidad de cocientes multiplicándolo por q_g=0, sin división 0/0."}

**Detención de la función interior.** Sea $g(x)=1$ para $x<0$ y $g(x)=1+x^2$ para $x\ge0$. En cero, $q_g(x)=0$ a la izquierda y $q_g(x)=x$ a la derecha; $g'(0)=0$. Para $f(y)=y^2$, $f'(1)=2$ y $(f\circ g)'(0)=0$. El cociente que divide por $g(x)-1$ no existe en ningún $x<0$; la identidad con $A$ sigue siendo válida allí.

**Si no está dada la inclusión de imágenes.** Para $g:D\to\mathbb R$ y $f:E\to\mathbb R$, el dominio de composición es $T=\{x\in D:g(x)\in E\}$. Hay que exigir $a\in T\cap\operatorname{Acc}(T)$, restringir $g$ a $T$ y cambiar su codominio a $E$. La acumulación no se deduce de la de $D$ y $E$: con $g(x)=x^2$, $E=(-\infty,0]$ y $D=\mathbb R$, resulta $T=\{0\}$. Incluso si $f(y)=y$ es derivable relativamente a $E$ en cero, la composición sobre ese singleton no tiene derivada según R1.

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-018-033}

¿Qué división falla si $g(x)=g(a)$?

[]{#MA-MSOL-ANM-01-018-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

La división por $g(x)-g(a)$ en la factorización habitual de secantes; el cociente de la composición sí está definido si $x\ne a$.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-018-034}

¿Qué valor se asigna al factor exterior $A$ en $b$?

[]{#MA-MSOL-ANM-01-018-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

$f\prime(b)$, como valor de una nueva función, sin efectuar la división exterior en el centro.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-018-035}

¿Por qué $A$ es continua en $b$?

[]{#MA-MSOL-ANM-01-018-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Fuera del centro sus valores convergen a $f\prime(b)$ por derivabilidad, y en el centro su diferencia respecto de ese valor es cero.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-018-036}

¿Qué identidad admite incremento interior cero?

[]{#MA-MSOL-ANM-01-018-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

$q_{f\circ g,a}(x)=A(g(x))q_{g,a}(x)$; ambos incrementos de salida son cero cuando $g(x)=b$.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-018-037}

¿Exige la cadena una derivada interior no nula?

[]{#MA-MSOL-ANM-01-018-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

No. El producto de límites sigue siendo válido si $g\prime(a)=0$.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-018-038}

¿Qué inclusión de tipos simplifica la composición?

[]{#MA-MSOL-ANM-01-018-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

$g:D\to E$ y $f:E\to\mathbb R$, de modo que toda imagen interior es entrada admisible exterior.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-018-039}

¿Qué condición adicional hay que verificar sobre un dominio efectivo $T$?

[]{#MA-MSOL-ANM-01-018-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

$a\in T\cap\operatorname{Acc}(T)$. La acumulación del dominio original y del exterior no la garantiza.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-018-040}

¿La imagen de una función interior constante acumula en su valor?

[]{#MA-MSOL-ANM-01-018-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No, es un singleton. Aun así la cadena funciona si la función exterior es derivable en su propio dominio acumulante.

</details>

### Ejercicios de la sección 18.5

#### Ejercicio 21. Rellenar el factor exterior

[]{#MA-EX-ANM-01-018-021}

Construye $A$ para una función exterior derivable en $b$ y prueba su continuidad y su identidad de incrementos.

[]{#MA-SOL-ANM-01-018-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

En $E\setminus\{b\}$ ponemos $A(y)=(f(y)-f(b))/(y-b)$ y en $b$ ponemos $A(b)=M=f\prime(b)$. Para cualquier tolerancia, los radios de derivabilidad controlan $|A(y)-M|$ fuera del centro; en él esa diferencia es cero, así $A$ es continua en $b$. Multiplicar la definición da $f(y)-f(b)=A(y)(y-b)$ para $y\ne b$, y en $b$ ambos lados valen cero. Es una nueva función con un valor declarado en el centro, no una división por cero.

</details>

#### Ejercicio 22. Los dos presupuestos de la cadena

[]{#MA-EX-ANM-01-018-022}

Prueba la cadena con una estimación de error que siga siendo válida cuando el incremento interior es cero.

[]{#MA-SOL-ANM-01-018-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Sea $L=g\prime(a)$, $M=f\prime(b)$ y $C=|L|+1$. La identidad de incrementos con $A$ da $q_{f\circ g}=A(g(x))q_g$ para todo $x\ne a$, incluidos los que satisfacen $g(x)=b$. Cerca del centro, $|q_g|<C$. Continuidad de $A$ en $b$ y de $g$ en $a$ entrega radio para error $|A(g(x))-M|<\varepsilon/(2C)$. Derivabilidad interior entrega otro para $|q_g-L|<\varepsilon/[2(|M|+1)]$. En el mínimo de estos radios y el de la cota, la diferencia respecto de $ML$ es a lo sumo $|A-M||q_g|+|M||q_g-L|<\varepsilon$. De este modo se prueba el límite sin dividir por $g(x)-b$.

</details>

#### Ejercicio 23. Una rama detenida

[]{#MA-EX-ANM-01-018-023}

Para $g(x)=1$ si $x<0$ y $g(x)=1+x^2$ si $x\ge0$, calcula la derivada de $g$ y de $g(x)^2$ en cero. Explica el fallo de la factorización que divide por el incremento interior.

[]{#MA-SOL-ANM-01-018-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

El cociente interior es cero a la izquierda y $x$ a la derecha, por lo que su magnitud es a lo sumo $|x|$ y $g\prime(0)=0$. La exterior $f(y)=y^2$ tiene derivada dos en uno. La cadena correcta da derivada cero. Directamente, el cociente compuesto es cero para $x<0$ y $2x+x^3$ para $x>0$, con límite cero. En cualquier argumento negativo, $g(x)-g(0)=0$, así el factor exterior habitual es una división $0/0$. Usar $A(1)=2$ mantiene la identidad: factor dos por cociente interior cero da cero.

**Retorno visual.** Véase [C18-F04](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 24. Acumulación perdida en la composición

[]{#MA-EX-ANM-01-018-024}

Sean $g(x)=x^2$ sobre $\mathbb R$ y $f(y)=y$ sobre $E=(-\infty,0]$. Halla el dominio efectivo, revisa las derivadas de los factores y explica por qué no hay derivada compuesta en cero.

[]{#MA-SOL-ANM-01-018-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

El dominio efectivo $T=\{x:x^2\le0\}$ es $\{0\}$. La interior tiene derivada cero en cero sobre la recta; la exterior tiene derivada relativa uno en cero sobre $E$, que acumula allí desde la izquierda. Pero cero no acumula en $T$, por lo que R1 no define una derivada de la composición sobre su dominio. Las acumulaciones de los dominios originales no garantizan la de la preimagen efectiva. La multiplicación formal de derivadas omite una hipótesis de la cadena.

</details>

#### Ejercicio 25. Interior constante y exterior no lineal

[]{#MA-EX-ANM-01-018-025}

Sea $g:D\to E$ constante con valor $b$ y $a\in D\cap\operatorname{Acc}(D)$. Si $f$ es derivable en $b$ respecto de $E$, comprueba la cadena y la acumulación de la imagen interior.

[]{#MA-SOL-ANM-01-018-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

La interior tiene cociente cero en todo su dominio perforado, así $g\prime(a)=0$. La composición es constante con valor $f(b)$ y también tiene derivada cero. La fórmula da $f\prime(b)\cdot0=0$. La imagen $g[D]=\{b\}$ no acumula en $b$; esto no impide usar la derivada exterior calculada en $E$, donde sí se exige acumulación. El factor $A$ puede evaluarse en $b$ y vale $f\prime(b)$ en todas las entradas compuestas.

</details>
## 18.6. Invertir la pendiente exige volver al punto

[]{#MA-SEC-ANM-01-018-006}

La pendiente inversa intercambia cambio de entrada y salida. Pero una salida próxima al valor central debe recuperar una entrada próxima al centro original.

**R6 — Derivada de la inversa.** Sea $f:D\to\mathbb R$ inyectiva, $a\in D\cap\operatorname{Acc}(D)$ y $f'(a)=L\ne0$. Ponemos $H=f[D]$, $b=f(a)$ y construimos la inversa $h:H\to D$, considerada con los mismos valores como función real $h:H\to\mathbb R$. Suponemos explícitamente que es continua en $b$ respecto de $H$. Entonces $h'(b)=1/L$.

**Metas intermedias y prueba.** Primero $b\in\operatorname{Acc}(H)$. Para $\rho>0$, continuidad de $f$ en $a$ da $\delta$ con error menor que $\rho$. La acumulación de $D$ proporciona un $x\ne a$ dentro de ese radio, y la inyectividad asegura $f(x)\ne b$. Así $0<|f(x)-b|<\rho$. El dominio perforado de la inversa es legítimo.

Después pedimos a $q_{f,a}$ error $|L|/2$; en algún radio $r$ resulta $|q_{f,a}|>|L|/2$. Para una tolerancia final $\varepsilon$, otro radio $s$ asegura error menor que $\varepsilon|L|^2/2$. Continuidad de $h$ da $\eta>0$ tal que $|y-b|<\eta$, $y\in H$, implica $|h(y)-a|<\min(r,s)$. Si $y\ne b$, inyectividad fuerza $h(y)\ne a$, y
$$q_{h,b}(y)=\frac1{q_{f,a}(h(y))},\qquad
\left|q_{h,b}(y)-\frac1L\right|
=\frac{|q_{f,a}(h(y))-L|}{|L|\,|q_{f,a}(h(y))|}<\varepsilon.$$
Esto prueba existencia de la derivada de $h$ sin derivar primero la identidad $f\circ h=\mathrm{id}$. Aquella derivación sería circular si aún no sabemos que $h$ es derivable. Inyectividad construye la inversa; continuidad aproxima entradas recuperadas; $L\ne0$ separa el denominador de cero.

![Para el cuadrado no negativo, el par 1,3/2 produce valores 1,9/4 y pendiente 5/2. La inversa raíz intercambia coordenadas y tiene pendiente secante 2/5 para ese par. En los centros 1, las pendientes límite son dos y un medio. R6 justifica el paso al límite con inversa continua y pendiente original no nula.](../../assets/books/anm/C18/C18-F05.svg){#fig-anm-c18-f05 fig-alt="Para el cuadrado no negativo, el par 1,3/2 produce valores 1,9/4 y pendiente 5/2. La inversa raíz intercambia coordenadas y tiene pendiente secante 2/5 para ese par. En los centros 1, las pendientes límite son dos y un medio. R6 justifica el paso al límite con inversa continua y pendiente original no nula."}

**Raíz con centro positivo.** En $D=[0,\infty)$, el cuadrado es inyectivo y su inversa es $\sqrt y$ por C10. En $b=a^2>0$,
$|\sqrt y-a|=|y-a^2|/(\sqrt y+a)\le|y-a^2|/a$, de modo que la inversa es continua. R6 da $(\sqrt y)'|_{y=b}=1/(2a)$. En cero, el cuadrado tiene derivada relativa cero, pero el cociente de su inversa es $1/\sqrt y$ para $y>0$ y crece sin cota al acercarse a cero; no hay derivada finita allí. Para cualquier cota $B>0$ y radio $r>0$, tomar $0<y<\min(r,1/(B+1)^2)$ da cociente mayor que $B$.

**La continuidad de la inversa no es automática.** Sea $D=[0,1)\cup[2,3]$, con $f(x)=x$ en la primera pieza y $f(x)=x-1$ en la segunda. Es inyectiva, tiene imagen $H=[0,2]$ y derivada relativa uno en $a=2$. Sin embargo $h(1)=2$, mientras $y_n=1-1/(n+2)$ satisface $h(y_n)=y_n\to1$. La inversa no es continua en $b=1$; R3 impide que sea derivable allí. En compactos, C16 proporciona continuidad de la inversa de una función continua e inyectiva; en intervalos, se puede usar la interfaz correspondiente de C15. Son garantías adicionales sobre el dominio, no parte oculta de R6.

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-018-041}

¿Qué hipótesis construye una inversa única sobre la imagen?

[]{#MA-MSOL-ANM-01-018-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Inyectividad de $f$; cada $y\in f[D]$ tiene un único antecedente en $D$.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-018-042}

¿Qué asegura la acumulación de la imagen en $f(a)$?

[]{#MA-MSOL-ANM-01-018-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Continuidad de $f$ en el centro, acumulación de $D$ e inyectividad para que un antecedente distinto produzca un valor distinto.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-018-043}

¿Qué hipótesis aproxima $h(y)$ a $a$ cuando $y$ se acerca a $b$?

[]{#MA-MSOL-ANM-01-018-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Continuidad de la inversa $h$ en $b$; no basta saber que la inversa existe.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-018-044}

¿Para qué se exige $L\ne0$?

[]{#MA-MSOL-ANM-01-018-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Para separar las pendientes originales de cero y controlar sus recíprocos mediante el margen $|L|/2$.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-018-045}

¿Por qué $y\ne b$ implica $h(y)\ne a$?

[]{#MA-MSOL-ANM-01-018-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

Porque $h(y)=a$ daría $y=f(h(y))=f(a)=b$, contradicción.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-018-046}

¿Cuál es la derivada de la raíz en $b>0$?

[]{#MA-MSOL-ANM-01-018-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

$1/(2\sqrt b)$, aplicando la inversa del cuadrado en $a=\sqrt b>0$.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-018-047}

¿Por qué no se deriva primero $f\circ h=\mathrm{id}$ para probar R6?

[]{#MA-MSOL-ANM-01-018-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

Eso aplicaría la cadena suponiendo ya la derivabilidad de $h$, precisamente lo que falta demostrar.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-018-048}

¿Qué falla para la raíz en cero?

[]{#MA-MSOL-ANM-01-018-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Su cociente relativo es $1/\sqrt y$, sin límite real finito. La pendiente del cuadrado que se invertiría vale cero.

</details>

### Ejercicios de la sección 18.6

#### Ejercicio 26. Tres hipótesis, tres funciones

[]{#MA-EX-ANM-01-018-026}

En R6 explica por separado el papel de inyectividad, continuidad de la inversa y derivada no nula. Prueba que la imagen acumula en $b$.

[]{#MA-SOL-ANM-01-018-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Inyectividad construye un único antecedente por valor de la imagen y hace que $x\ne a$ produzca $f(x)\ne b$. Continuidad de $h$ en $b$ convierte aproximación de salidas en aproximación de antecedentes a $a$. La condición $L\ne0$ separa las pendientes originales de cero para invertirlas. Para cada $\rho>0$, continuidad de $f$ en $a$ da un radio con error menor que $\rho$; acumulación de $D$ entrega una entrada distinta del centro dentro de él. Su imagen pertenece a $H$, es distinta de $b$ y está a distancia menor que $\rho$. Esto prueba acumulación de la imagen sin seleccionar una sucesión.

</details>

#### Ejercicio 27. Secantes recíprocas del cuadrado

[]{#MA-EX-ANM-01-018-027}

Para el cuadrado en $[0,\infty)$ y $a>0$, prueba continuidad y derivada de la inversa en $b=a^2$. Relaciona las secantes originales e inversas.

[]{#MA-SOL-ANM-01-018-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

La inyectividad del cuadrado en el dominio no negativo y C10 identifican la inversa con $h(y)=\sqrt y$. Se tiene $|h(y)-a|=|y-a^2|/(\sqrt y+a)\le|y-a^2|/a$, por lo que es continua en $b$. R6 con $L=2a\ne0$ da $h\prime(b)=1/(2a)$. Para $y=x^2\ne a^2$, con $x\ge0$, la pendiente inversa es $(x-a)/(x^2-a^2)=1/(x+a)$, recíproca de la pendiente original $x+a$. Ambas divisiones requieren $x\ne a$, asegurado por inyectividad.

**Retorno visual.** Véase [C18-F05](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 28. Un centro de pendiente cero

[]{#MA-EX-ANM-01-018-028}

Prueba que el cuadrado tiene derivada relativa cero en cero y que su inversa raíz no tiene allí derivada real finita.

[]{#MA-SOL-ANM-01-018-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Para $x>0$, la pendiente del cuadrado centrada en cero es $x\to0$. La pendiente de la raíz sobre $[0,\infty)$ es $1/\sqrt y$ para $y>0$. Dadas cota $B>0$ y escala $r>0$, se elige $0<y<\min(r,1/(B+1)^2)$ y se obtiene cociente mayor que $B$. Si hubiera límite finito, sus cocientes estarían acotados por $|L|+1$ en algún radio, contradicción. La inversa existe y es continua, pero no se satisface la hipótesis de pendiente original no nula.

</details>

#### Ejercicio 29. Una inversa que salta

[]{#MA-EX-ANM-01-018-029}

En $D=[0,1)\cup[2,3]$, sea $f(x)=x$ en la primera pieza y $x-1$ en la segunda. Analiza inyectividad, imagen, derivada en dos y continuidad de la inversa en uno.

[]{#MA-SOL-ANM-01-018-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Las imágenes son $[0,1)$ y $[1,2]$, disjuntas, y ambas ramas son inyectivas; la imagen total es $[0,2]$. En una bola de radio menor que uno centrada en dos sólo hay puntos de la segunda pieza y su cociente es uno, así $f\prime(2)=1$ relativamente a $D$. La inversa satisface $h(1)=2$, pero para $y_n=1-1/(n+2)$ se tiene $h(y_n)=y_n\to1$. Sus diferencias respecto de dos son mayores que uno mientras las entradas convergen a uno. No es continua allí y, por R3, no es derivable. Esto refuta que derivada original no nula e inyectividad hagan innecesaria continuidad de la inversa en dominios arbitrarios.

</details>

#### Ejercicio 30. Evitar una prueba circular

[]{#MA-EX-ANM-01-018-030}

Una demostración deriva $f\circ h=\mathrm{id}$ y despeja $h\prime(b)$ sin haber demostrado que existe. Repara la prueba por cocientes.

[]{#MA-SOL-ANM-01-018-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La cadena sólo se aplica si la derivada interior existe, así el despeje presupone la conclusión. Se toma directamente un $y\ne b$ de la imagen y $x=h(y)\ne a$. La identidad de inversa da $q_h(y)=1/q_f(x)$. Continuidad de $h$ asegura $x\to a$; derivada original no nula entrega margen $|q_f|>|L|/2$. Entonces $|q_h-1/L|\le2|q_f-L|/|L|^2$, que se hace menor que cualquier tolerancia con los radios de derivabilidad y continuidad. Así se obtiene existencia antes de usar una regla que la exigiría.

</details>
## 18.7. Una derivada es otra función

[]{#MA-SEC-ANM-01-018-007}

Cuando cambiamos el centro obtenemos otra función, con su propio dominio. Que cada derivada exista no significa que sus valores dependan continuamente del centro.

**R7 — Dominio de la función derivada.** Definimos
$$\operatorname{Diff}(f)=\{a\in D\cap\operatorname{Acc}(D):f\text{ es derivable en }a\},\qquad
f':\operatorname{Diff}(f)\to\mathbb R.$$
R1 da un valor único por punto, así esta regla determina una función, sin escoger entre pendientes. Para $|x|$ sobre $\mathbb R$, el dominio es $\mathbb R\setminus\{0\}$; sus valores son $-1$ a la izquierda y $1$ a la derecha. El límite de esta función en cero puede preguntarse porque cero acumula en su dominio; su continuidad en cero no puede afirmarse porque no está definido allí.

**Ejemplo sin herramientas trigonométricas.** Para $n\in\mathbb N$ (desde cero), sean $c_n=2^{-(n+1)}$, $w_n=c_n^2/8$ y $I_n=[c_n-w_n,c_n+w_n]$. Los intervalos son positivos y disjuntos: entre centros consecutivos hay distancia $c_n/2$, mientras la suma de semianchos es $5c_n^2/32<c_n/2$. Todos quedan dentro de $[c_n/2,3c_n/2]$. Definimos $\phi(u)=(1-u^2)^2$ en $[-1,1]$ y
$$F(x)=\begin{cases}w_n\phi((x-c_n)/w_n),&x\in I_n\text{ para algún }n,\\0,&x\notin\bigcup_n I_n.\end{cases}$$
La disjunción evita valores incompatibles. En cada intervalo $0\le F(x)\le w_n\le x^2/2$, y fuera de ellos $F=0$. Como $F(0)=0$, $|q_{F,0}(x)|\le|x|/2$, de donde $F'(0)=0$.

**Comprobar los otros puntos.** En el interior de $I_n$, R4/R5 derivan el polinomio y dan
$$F'(x)=\phi'((x-c_n)/w_n)=-4u(1-u^2),\qquad u=(x-c_n)/w_n.$$
En los extremos, $\phi(\pm1)=\phi'(\pm1)=0$. Más explícitamente, si $e=c_n\pm w_n$ y $x$ está en la rama interior, $|\phi(u)|\le4|u\mp1|^2$, así $|F(x)|\le4|x-e|^2/w_n$. El cociente centrado en $e$ tiende a cero; en la rama exterior es cero. No se usa un teorema de pegado de derivadas sin probarlo. Cada punto distinto de cero tiene una vecindad que sólo puede tocar finitos intervalos: los centros de la cola tienden a cero; se separan después los intervalos restantes que no contienen el punto. Fuera de ellos hay una vecindad constante. Esto justifica las ramas anteriores y demuestra diferenciabilidad en toda $\mathbb R$.

![Se muestran n=0,…,4 de la familia con c_n=2^{−(n+1)}, w_n=c_n²/8 y perfil (1−u²)². Toda la función satisface 0≤F(x)≤x²/2 y F′(0)=0. En x_n=c_n+w_n/2, la derivada vale −3/2 para todo n, refutando continuidad de F′ en cero. La figura representa una muestra finita; disjunción, extremos, finitud local y cola se prueban en R7.](../../assets/books/anm/C18/C18-F06.svg){#fig-anm-c18-f06 fig-alt="Se muestran n=0,…,4 de la familia con c_n=2^{−(n+1)}, w_n=c_n²/8 y perfil (1−u²)². Toda la función satisface 0≤F(x)≤x²/2 y F′(0)=0. En x_n=c_n+w_n/2, la derivada vale −3/2 para todo n, refutando continuidad de F′ en cero. La figura representa una muestra finita; disjunción, extremos, finitud local y cola se prueban en R7."}

**La derivada no es continua.** Para $x_n=c_n+w_n/2$, tenemos $x_n\to0$ pero $F'(x_n)=\phi'(1/2)=-3/2$, distinto del valor $F'(0)=0$. La continuidad de $F'$ en cero exigiría diferencias menores que uno desde algún radio, contradichas por estos puntos explícitos. La amplitud de cada bulto es cuadrática respecto de su distancia al origen, suficiente para la derivada cero allí; su anchura permite pendientes interiores que no se hacen pequeñas. La figura muestra sólo una cantidad finita de bultos; la prueba controla toda la familia.

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-018-049}

¿Cuál es el dominio de $f\prime$?

[]{#MA-MSOL-ANM-01-018-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

$\operatorname{Diff}(f)$: centros del dominio que son de acumulación y donde el límite de pendientes existe finito.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-018-050}

¿Puede preguntarse continuidad de $f\prime$ en un punto donde no está definida?

[]{#MA-MSOL-ANM-01-018-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

No. Puede preguntarse un límite si el punto acumula en su dominio, pero continuidad requiere un valor en el punto.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-018-051}

¿Qué impide solapamiento de los intervalos $I_n$?

[]{#MA-MSOL-ANM-01-018-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

La suma de semianchos vecinos $5c_n^2/32$ es menor que la distancia entre centros $c_n/2$; los intervalos ordenados quedan separados.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-018-052}

¿Qué cota prueba $F\prime(0)=0$?

[]{#MA-MSOL-ANM-01-018-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

$0\le F(x)\le x^2/2$, por lo que el cociente centrado en cero tiene magnitud a lo sumo $|x|/2$.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-018-053}

¿Por qué coinciden las derivadas en los extremos de cada bulto?

[]{#MA-MSOL-ANM-01-018-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

La rama interior se anula con orden al menos dos y da cociente tendente a cero; la rama exterior es cero.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-018-054}

¿Qué puntos refutan continuidad de $F\prime$ en cero?

[]{#MA-MSOL-ANM-01-018-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

$x_n=c_n+w_n/2\to0$, con $F\prime(x_n)=-3/2$ para todo $n$, frente a $F\prime(0)=0$.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-018-055}

¿Cómo se evita usar un pegado infinito sin justificación?

[]{#MA-MSOL-ANM-01-018-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Fuera de cero sólo hay finitos intervalos en una vecindad; cero se trata directamente con la cota global del cociente.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-018-056}

¿La figura con varios bultos prueba el caso infinito?

[]{#MA-MSOL-ANM-01-018-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No. La prueba usa fórmulas y cotas para todo $n$; la imagen representa una muestra finita.

</details>

### Ejercicios de la sección 18.7

#### Ejercicio 31. El dominio de otra función

[]{#MA-EX-ANM-01-018-031}

Escribe el dominio y los valores de la función derivada de $|x|$ sobre $\mathbb R$. Distingue límite y continuidad de esa derivada en cero.

[]{#MA-SOL-ANM-01-018-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

En cada centro positivo hay una vecindad donde la función es la identidad y la derivada vale uno; en cada centro negativo hay una donde es menos la identidad y vale menos uno. En cero no existe derivada. Así su dominio es $\mathbb R\setminus\{0\}$. Cero acumula en ese dominio, por lo que puede preguntarse su límite; no existe por los dos valores laterales diferentes. No se habla de continuidad allí porque falta un valor de la función derivada en cero.

</details>

#### Ejercicio 32. Separar la familia de bultos

[]{#MA-EX-ANM-01-018-032}

Para $c_n=2^{-(n+1)}$, $w_n=c_n^2/8$, prueba positividad y disjunción de $I_n$. Justifica que fuera de cero la familia es localmente finita.

[]{#MA-SOL-ANM-01-018-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Como $c_n\le1/2$, $w_n<c_n/2$, por lo que el intervalo es positivo y queda en $[c_n/2,3c_n/2]$. La distancia entre centros vecinos es $c_n/2$ y la suma de semianchos $w_n+w_{n+1}=5c_n^2/32<c_n/2$. Los intervalos quedan ordenados y separados, lo que implica disjunción de cualquier par. Si el punto $x>0$ está fijado, los centros de la cola y sus extremos quedan por debajo de $x/2$ desde algún índice, dejando sólo finitos intervalos posibles en una bola pequeña. Si $x<0$, una bola dentro de la semirrecta negativa no toca ninguno. Sólo en cero se acumula la familia.

</details>

#### Ejercicio 33. Una derivada discontinua sin trigonometría

[]{#MA-EX-ANM-01-018-033}

Completa la prueba de R7: diferenciabilidad en cero, en extremos y en interiores, y discontinuidad de la función derivada en cero.

[]{#MA-SOL-ANM-01-018-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

En cada intervalo, $0\le F\le w_n=c_n^2/8\le x^2/2$ porque $x\ge c_n/2$; fuera de ellos es cero. Así $|q_{F,0}|\le|x|/2$ y $F\prime(0)=0$. En interiores, reglas algebraicas y cadena dan $\phi\prime(u)=-4u(1-u^2)$. En un extremo $e$, la rama interior satisface $|F(x)|\le4|x-e|^2/w_n$, así su cociente tiende a cero; la exterior es cero. La finitud local permite aislar el intervalo o la zona exterior en todo punto no nulo. Por tanto $F$ es derivable en toda la recta. Los puntos $x_n=c_n+w_n/2\to0$ tienen derivada $\phi\prime(1/2)=-3/2$, así contradicen continuidad de $F\prime$ en cero con tolerancia uno. No se depende de representar gráficamente la cola infinita.

**Retorno visual.** Véase [C18-F06](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. La forma del extremo

[]{#MA-EX-ANM-01-018-034}

Prueba la cota $|\phi(u)|\le4|u-1|^2$ cerca del extremo derecho en $[-1,1]$, y su análoga izquierda. Tradúcela al cociente de un bulto.

[]{#MA-SOL-ANM-01-018-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

En $[-1,1]$, $(1-u^2)^2=(1-u)^2(1+u)^2\le4(u-1)^2$ y también $\le4(u+1)^2$. Si $e=c_n+w_n$, entonces $u-1=(x-e)/w_n$, de donde $|F(x)|\le4|x-e|^2/w_n$. Como $F(e)=0$, el cociente centrado en $e$ tiene magnitud a lo sumo $4|x-e|/w_n$ en la rama interior y cero fuera. El radio $\eta w_n/4$, reducido para aislar el bulto, da error menor que $\eta$. El extremo izquierdo se trata con $u+1$ y el mismo presupuesto.

</details>

#### Ejercicio 35. Pendiente puntual y función derivada

[]{#MA-EX-ANM-01-018-035}

Compara el dominio de la derivada de la función racional/irracional de R3 con el de la familia de bultos de R7. ¿Qué dos inferencias fallan?

[]{#MA-SOL-ANM-01-018-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

La primera es derivable en cero y discontinua en todo otro punto; por R3 no es derivable fuera de cero. Su dominio de derivada es exactamente $\{0\}$ y la función derivada allí vale cero. La familia de bultos es derivable en toda la recta, pero su derivada es discontinua en cero. Así fallan dos inferencias distintas: derivabilidad en un centro no garantiza derivabilidad en una vecindad, y derivabilidad en toda una vecindad no garantiza continuidad de la función derivada. La derivada sobre un singleton es continua relativamente a él, aunque ese hecho no la extienda al entorno.

</details>
## 18.8. Certificar una aproximación local

[]{#MA-SEC-ANM-01-018-008}

Una derivada identifica la recta local. Para convertirla en una aproximación con tolerancia hace falta una estimación del resto en el dominio donde se va a evaluar.

**R8 — De una cota a un certificado.** Si $f'(a)=L$ y para $|h|<\rho$, $a+h\in D$, se conoce
$$|f(a+h)-f(a)-Lh|\le B h^2\qquad(B\ge0),$$
entonces la aproximación $f(a)+Lh$ tiene error absoluto a lo sumo $Bh^2$. Si $B>0$, pedir además $|h|<\eta/B$ certifica error normalizado menor que $\eta$. Si $B=0$, el error es exactamente cero en esa vecindad. La existencia de la derivada sólo garantiza un resto $o(|h|)$, sin garantizar por sí sola una cota cuadrática o un algoritmo para encontrar radios.

**Un certificado por álgebra.** Para $f(x)=\sqrt x$ y $a=1$, R6 da $L=1/2$. Con $h>-1$ y $s=\sqrt{1+h}$, dos racionalizaciones dan la identidad exacta
$$\sqrt{1+h}=1+\frac h2-\frac{h^2}{2(\sqrt{1+h}+1)^2}.$$
Para $|h|\le1/2$, $s\ge0$ y por tanto el resto tiene magnitud a lo sumo $h^2/2$. En $h=1/100$, el valor aproximado es $201/200$ y el error está entre cero y $1/20000$ por debajo de esa recta. También $q_{f,1}(1+h)=1/(s+1)$ y $|q_{f,1}-1/2|\le|h|/2$. Son dos errores distintos: error del valor y error de la pendiente secante.

![En |h|≤1/2, el modelo 1+h/2 aproxima √(1+h) por encima. La identidad exacta da error h²/\[2(√(1+h)+1)²\]≤h²/2. En h=1/100, el modelo es 201/200 y el error es a lo sumo 1/20000. El panel de errores tiene su propia escala vertical; no es el error de pendiente secante, que divide por |h|.](../../assets/books/anm/C18/C18-F07.svg){#fig-anm-c18-f07 fig-alt="En |h|≤1/2, el modelo 1+h/2 aproxima √(1+h) por encima. La identidad exacta da error h²/\[2(√(1+h)+1)²\]≤h²/2. En h=1/100, el modelo es 201/200 y el error es a lo sumo 1/20000. El panel de errores tiene su propia escala vertical; no es el error de pendiente secante, que divide por |h|."}

**Existencia sin resto cuadrático.** Para $f(x)=|x|^{3/2}=|x|\sqrt{|x|}$, $f(0)=0$ y $|q_{f,0}(x)|=\sqrt{|x|}\to0$, así $f'(0)=0$. Si hubiera una cota $|x|^{3/2}\le Bx^2$ con $B>0$ en una vecindad perforada, tendríamos $1/\sqrt{|x|}\le B$, imposible. Aquí la potencia fraccionaria sólo abrevia producto y raíz ya construidos; no se ha usado una regla de potencias reales.

**Las muestras finitas no determinan la derivada.** Sea $S\subseteq\mathbb R$ finito con $0\in S$, y sea $c\in\mathbb R$ cualquier pendiente prescrita. El polinomio
$$p_c(x)=c x\prod_{s\in S\setminus\{0\}}\frac{x-s}{-s}$$
se anula en todos los puntos de $S$, pero $p_c'(0)=c$. Cada denominador es no nulo y el producto vacío vale uno. Para $x\ne0$, el cociente centrado en cero es $c$ por el producto de los factores, que tienden a uno; C13 prueba el límite $c$. Una tabla finita de ceros es compatible con cualquier pendiente. La certificación de la derivada exige control sobre todos los argumentos suficientemente cercanos, no sólo sobre secantes muestreadas.

**Herramientas que salen.** Disponemos de derivada relativa, único modelo lineal de primer orden, continuidad, reglas algebraicas, cadena sin división por incremento interior e inversa bajo continuidad y pendiente no nula. Sabemos distinguir el dominio de $f'$ y su continuidad, y certificar errores cuando tenemos una cota demostrada. Los próximos resultados deberán explicar cuándo información local en todos los centros gobierna un intervalo completo.

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-018-057}

¿Qué dato convierte una recta local en certificado cuadrático?

[]{#MA-MSOL-ANM-01-018-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Una cota demostrada $|r(a+h)|\le Bh^2$ en una vecindad especificada, adicional a la mera existencia de la derivada.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-018-058}

¿Cuánto vale el modelo de $\sqrt{1+h}$ en $h=1/100$?

[]{#MA-MSOL-ANM-01-018-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

$1+h/2=201/200$; el error absoluto está acotado por $1/20000$.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-018-059}

¿En qué lado del valor exacto queda ese modelo de raíz?

[]{#MA-MSOL-ANM-01-018-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Por encima: el resto exacto es $-h^2/[2(\sqrt{1+h}+1)^2]\le0$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-018-060}

¿Qué diferencia hay entre error de valor y error de pendiente secante?

[]{#MA-MSOL-ANM-01-018-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

El segundo es el resto dividido por $h\ne0$; con cota $Bh^2$, sus magnitudes son a lo sumo $Bh^2$ y $B|h|$, respectivamente.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-018-061}

¿La derivabilidad garantiza resto cuadrático?

[]{#MA-MSOL-ANM-01-018-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

No. $|x|\sqrt{|x|}$ tiene derivada cero en cero, pero el cociente de su resto por $x^2$ es $1/\sqrt{|x|}$ y no está acotado.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-018-062}

¿Qué significa el producto vacío en $p_c$?

[]{#MA-MSOL-ANM-01-018-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

Uno. Si las únicas muestras son el centro, la construcción da simplemente $p_c(x)=cx$.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-018-063}

¿Qué derivada en cero tiene $p_c$ aunque sus muestras sean cero?

[]{#MA-MSOL-ANM-01-018-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

$c$, pues su cociente es $c$ por un producto finito de factores que tienden a uno.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-018-064}

¿Qué controla un certificado de derivada que no controla una tabla finita?

[]{#MA-MSOL-ANM-01-018-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Todas las entradas admisibles dentro de un radio para cada tolerancia, no sólo los puntos muestreados.

</details>

### Ejercicios de la sección 18.8

#### Ejercicio 36. Racionalizar el error de raíz

[]{#MA-EX-ANM-01-018-036}

Demuestra la identidad exacta del resto de $\sqrt{1+h}$ respecto de $1+h/2$, para $h>-1$. Da una cota cuadrática en $|h|\le1/2$.

[]{#MA-SOL-ANM-01-018-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Con $s=\sqrt{1+h}\ge0$, $s-1=h/(s+1)$. Entonces $s-1-h/2=h(1-s)/[2(s+1)]=-h^2/[2(s+1)^2]$. El denominador es positivo. Para $|h|\le1/2$ sigue siendo al menos dos, así el error tiene magnitud a lo sumo $h^2/2$. La identidad incluye $h=0$ sin dividir por $h$ y prueba además que el modelo afín está por encima del valor exacto. Se obtuvo por álgebra y raíces C10, sin Taylor.

**Retorno visual.** Véase [C18-F07](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 37. Un valor y dos tolerancias

[]{#MA-EX-ANM-01-018-037}

Certifica la aproximación de $\sqrt{101/100}$ mediante $201/200$. Compara el error absoluto con el error de la secante usada para aproximar la derivada en uno.

[]{#MA-SOL-ANM-01-018-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

El incremento es $h=1/100$ y R8 da $0\le201/200-\sqrt{101/100}\le h^2/2=1/20000$. El error de la pendiente secante respecto de $1/2$ es el resto dividido por $h$, con magnitud a lo sumo $1/200$. No son la misma tolerancia: multiplicar el error de pendiente por la magnitud del incremento produce el error del valor. Ambos son certificados para esta entrada admisible, derivados de una identidad que controla toda la vecindad, sin tomar la cifra visual del gráfico como evidencia.

**Retorno visual.** Véase [C18-F07](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 38. Tolerancias desde una cota dada

[]{#MA-EX-ANM-01-018-038}

Si $|r(a+h)|\le Bh^2$ en $|h|<\rho$, da condiciones para error de valor menor que $\varepsilon$ y error normalizado menor que $\eta$. Trata $B=0$.

[]{#MA-SOL-ANM-01-018-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Si $B>0$, basta $|h|<\min(\rho,\sqrt{\varepsilon/B})$ para tener $Bh^2<\varepsilon$. Para el cociente con $h\ne0$, basta $|h|<\min(\rho,\eta/B)$, porque $|r/h|\le B|h|<\eta$. En $h=0$ el error del valor es cero; no se evalúa el cociente. Si $B=0$, el resto es cero en toda la vecindad admisible y cualquier incremento de ella da valor exacto, mientras todas sus secantes perforadas tienen pendiente exactamente $L$.

</details>

#### Ejercicio 39. Un resto menor que lineal y mayor que cuadrático

[]{#MA-EX-ANM-01-018-039}

Para $f(x)=|x|\sqrt{|x|}$, prueba derivada cero en cero y ausencia de una cota cuadrática local finita.

[]{#MA-SOL-ANM-01-018-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

El cociente tiene magnitud $\sqrt{|x|}$, de modo que $\delta=\eta^2$ prueba derivada cero. Si una cota $|f(x)|\le Bx^2$ con $B>0$ valiera en una vecindad perforada, dividir por $x^2$ daría $1/\sqrt{|x|}\le B$. Elegir allí $0<|x|<1/(B+1)^2$ lo contradice. Para $B=0$ cualquier entrada no nula ya contradice la cota. La derivada sólo exige resto de orden menor que lineal; no impone una tasa cuadrática. La expresión usa producto y raíz, sin regla general de potencias fraccionarias.

</details>

#### Ejercicio 40. Muestras idénticas, pendientes arbitrarias

[]{#MA-EX-ANM-01-018-040}

Dado $S\subseteq\mathbb R$ finito con $0\in S$ y un real $c$, construye un polinomio que se anule en $S$ y tenga derivada $c$ en cero. Explica la limitación de certificar derivadas con muestras finitas.

[]{#MA-SOL-ANM-01-018-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Sea $p_c(x)=cx\prod_{s\in S\setminus\{0\}}(x-s)/(-s)$, con producto vacío igual a uno. Todos los denominadores son no nulos. En cero se anula por el factor $x$; en cada otro nodo se anula por su factor correspondiente. En $x\ne0$, el cociente centrado en cero es $c\prod_s(x-s)/(-s)$, que tiende a $c$ porque cada factor tiende a uno y sólo hay finitos. Por tanto $p_c\prime(0)=c$, incluso si $c=0$ o no hay otros nodos. La misma tabla de ceros es compatible con toda pendiente prescrita. Las muestras no determinan un control de todas las entradas cercanas y no sustituyen la condición de derivabilidad.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-18)

[← Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Capítulo 19 →](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html)
