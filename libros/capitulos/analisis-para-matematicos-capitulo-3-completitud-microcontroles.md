---
title: "Soluciones de microcontroles — Capítulo 3"
content-id: MA-BCH-0095
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-003-MICROCONTROLES
book-id: MA-BOK-0009
status: published
solution-status: complete
date-created: 2026-09-30
date-modified: 2026-09-30
areas: [analisis]
level: universitario
topics: [analisis-real, orden, topologia]
prerequisites: [MA-BCH-0084]
related: [MA-BOK-0009]
provenance:
  type: original
  sources:
    - "Manuscrito ANM C03; referencias de contraste en la portada del libro."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Capítulo 3](analisis-para-matematicos-capitulo-3-completitud.md) · [Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Ejercicios](analisis-para-matematicos-capitulo-3-completitud-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-3-completitud-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-3-completitud-microcontroles.md)

# Soluciones de microcontroles — Capítulo 3

## §3.1. El problema heredado: definir no basta

[]{#MA-MSOL-ANM-01-003-001}

### 1. ¿Qué información expresa la igualdad $\sup A=\min U(A)$ y qué información **no** expresa por sí sola?

La igualdad

$$
\sup A=\min U(A)
$$

expresa **qué propiedad debe satisfacer el supremo cuando existe**: debe ser una cota superior de $A$ y, además, la menor de todas las cotas superiores. En otras palabras, identifica al supremo con el mínimo de la familia $U(A)$.

Pero la igualdad, leída como definición condicional, no demuestra por sí sola que ese mínimo exista. Antes de poder escribir un número concreto $s=\sup A$, todavía habría que justificar que

$$
U(A)\ne\varnothing
$$

y que existe

$$
\min U(A).
$$

Tampoco afirma que el supremo pertenezca a $A$; por tanto, no convierte automáticamente al supremo en máximo.

La separación lógica es:

$$
\text{definir qué sería }\sup A
\quad\not\Rightarrow\quad
\text{garantizar que }\sup A\text{ exista}.
$$

**Uso de completitud:** ninguno. Precisamente se está distinguiendo la definición del futuro principio de existencia.

[]{#MA-MSOL-ANM-01-003-002}

### 2. Si $U(A)\ne\varnothing$, ¿por qué eso no obliga lógicamente a que $U(A)$ tenga un mínimo?

De la sola afirmación

$$
U(A)\ne\varnothing
$$

sólo sabemos que hay **alguna** cota superior. No se sigue que entre todas ellas haya una menor.

El punto lógico puede verse incluso en un ejemplo elemental: el conjunto

$$
(0,1)
$$

es no vacío, pero no tiene mínimo. Dado cualquier $x\in(0,1)$, el número $x/2$ sigue perteneciendo a $(0,1)$ y satisface $x/2<x$.

En el problema específico del capítulo ocurre el mismo tipo de separación con la familia de cotas racionales de $S_2$: sabemos que

$$
U_{\mathbb Q}(S_2)\ne\varnothing,
$$

pero esa familia no posee un mínimo racional.

Por tanto,

$$
U(A)\ne\varnothing
\quad\not\Rightarrow\quad
\exists\min U(A).
$$

**Uso de completitud:** ninguno.

[]{#MA-MSOL-ANM-01-003-003}

### 3. Verifica que $1\in S_2$ y que $2$ es una cota superior racional de $S_2$.

Recordemos

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}.
$$

Para verificar que $1\in S_2$ comprobamos las dos condiciones definitorias:

$$
0\le1
$$

y

$$
1^2=1<2.
$$

Luego

$$
\boxed{1\in S_2}.
$$

Ahora probemos que $2$ es una cota superior racional. Sea $q\in S_2$. Si ocurriera $q\ge2$, como $q\ge0$ tendríamos

$$
q^2\ge2^2=4>2,
$$

lo que contradice la condición $q^2<2$ que define a $S_2$. Por tanto, todo $q\in S_2$ satisface

$$
q<2,
$$

y en particular $q\le2$. Como $2\in\mathbb Q$,

$$
\boxed{2\in U_{\mathbb Q}(S_2)}.
$$

Así quedan verificadas simultáneamente la no vaciedad de $S_2$ y la existencia de al menos una cota superior racional.

**Uso de completitud:** ninguno.

[]{#MA-MSOL-ANM-01-003-004}

### 4. ¿Qué falla exactamente para $S_2$ dentro de $\mathbb Q$: la existencia de cotas superiores o la existencia de una menor cota superior racional?

Para $S_2$ **no falla la existencia de cotas superiores racionales**. El microcontrol anterior ya exhibe una:

$$
2\in U_{\mathbb Q}(S_2).
$$

Por tanto,

$$
U_{\mathbb Q}(S_2)\ne\varnothing.
$$

Lo que falla es la existencia de una **menor** cota superior racional:

$$
\boxed{\min U_{\mathbb Q}(S_2)\text{ no existe en }\mathbb Q.}
$$

Equivalentemente, $S_2$ no posee supremo **dentro de $\mathbb Q$**.

Ésta es la distinción que interesa al capítulo: tener barreras superiores no implica que el sistema contenga una barrera extremal que sea la mejor de todas.

**Uso de completitud:** ninguno; estamos describiendo precisamente el defecto de existencia que una propiedad de completitud deberá reparar en $\mathbb R$.

[]{#MA-MSOL-ANM-01-003-005}

### 5. ¿Por qué la densidad de $\mathbb Q$ no resuelve ese fallo?

La densidad de $\mathbb Q$ afirma que, dados racionales $p<q$, existe otro racional $r$ tal que

$$
p<r<q.
$$

Es una propiedad **local**: permite insertar un punto entre dos puntos racionales ya dados.

El fallo de $S_2$ es de otra naturaleza. Allí preguntamos si toda la familia de cotas superiores racionales posee un elemento extremal $s$ que sea simultáneamente cota superior y menor que cualquier otra cota superior.

Poder insertar nuevos racionales entre dos racionales no produce por sí solo semejante mínimo. De hecho, aun cuando podamos encontrar cotas cada vez más ajustadas, todavía puede ocurrir que ninguna de ellas sea la menor.

Por eso

$$
\text{densidad}
\quad\not\Rightarrow\quad
\text{existencia de una menor cota superior}.
$$

La densidad permite **refinar entre puntos existentes**; no garantiza que el sistema contenga la frontera extremal exigida por una familia global de restricciones.

**Uso de completitud:** ninguno.

[]{#MA-MSOL-ANM-01-003-006}

### 6. ¿Qué tendría que añadir una propiedad de completitud para convertir la teoría condicional de C02 en una teoría de existencia?

La propiedad adicional tendría que transformar las hipótesis elementales de existencia de elementos y de cotas en una **garantía de existencia de la mejor cota dentro del propio sistema**.

En el caso real, la forma que necesitamos anticipar es:

$$
A\subseteq\mathbb R,
\qquad
A\ne\varnothing,
\qquad
U(A)\ne\varnothing
$$

implica que existe un número $s\in\mathbb R$ tal que

$$
s=\min U(A).
$$

Por la definición ya disponible, ese mismo número satisface

$$
s=\sup A.
$$

Así, la propiedad buscada debe autorizar el salto

$$
\boxed{
A\ne\varnothing,
\quad
A\text{ acotado superiormente}
\Longrightarrow
\exists s\in\mathbb R:\ s=\sup A.
}
$$

En §3.1 esto es todavía la **forma de la garantía que necesitamos**, no un principio ya usado para demostrar otros resultados. §3.2 será la sección encargada de formularla como propiedad estructural de $\mathbb R$.

**Uso de completitud:** anticipatorio. El microcontrol identifica qué garantía debe aportar; no la emplea todavía como resultado disponible.

## §3.2. El principio del supremo

[]{#MA-MSOL-ANM-01-003-007}

### 7. Separa, en el principio del supremo, las tres hipótesis escritas sobre $A$ de la conclusión de existencia.

Las tres hipótesis son:

$$
A\subseteq\mathbb R,
$$

$$
A\ne\varnothing,
$$

y

$$
A\text{ está acotado superiormente},
$$

lo que equivale a

$$
U(A)\ne\varnothing.
$$

La conclusión no es otra hipótesis sobre $A$, sino una afirmación de existencia:

$$
\boxed{\exists s\in\mathbb R:\ s=\sup A.}
$$

Desplegada mediante la definición de supremo, significa que existe $s\in\mathbb R$ tal que

$$
a\le s
\qquad\text{para todo }a\in A,
$$

y que, para toda cota superior $u\in U(A)$,

$$
s\le u.
$$

Por tanto, el principio transforma las tres condiciones de entrada en la existencia de una menor cota superior real.

**Uso de completitud:** directo, exactamente en el paso que afirma que tal $s$ existe.

[]{#MA-MSOL-ANM-01-003-008}

### 8. ¿Por qué la definición $s=\min U(A)$ no basta para demostrar que $s$ existe?

La expresión

$$
s=\min U(A)
$$

indica **qué tendría que cumplir** $s$ si el mínimo de $U(A)$ existiera. En particular, exige que

$$
s\in U(A)
$$

y que

$$
s\le u
\qquad\text{para todo }u\in U(A).
$$

Pero una definición no fabrica automáticamente un objeto que satisfaga esas condiciones.

Incluso si sabemos que

$$
U(A)\ne\varnothing,
$$

puede ocurrir que ese conjunto no tenga mínimo. Ése es precisamente el tipo de fallo diagnosticado en §3.1 para las cotas superiores racionales de $S_2$.

Así,

$$
\text{describir el mínimo de }U(A)
\quad\not\Rightarrow\quad
\text{probar que ese mínimo existe}.
$$

La existencia requiere una propiedad estructural adicional; en $\mathbb R$, esa propiedad es el principio del supremo.

**Uso de completitud:** la explicación identifica por qué hace falta, pero no la usa para derivar nada más.

[]{#MA-MSOL-ANM-01-003-009}

### 9. Si $A$ es no vacío y está acotado superiormente, ¿qué garantiza la completitud sobre $U(A)$?

Como $A$ es no vacío y está acotado superiormente, el principio del supremo garantiza que existe

$$
s=\sup A\in\mathbb R.
$$

Por la definición ya establecida en C02,

$$
s=\min U(A).
$$

Por tanto, la completitud no se limita a afirmar que $U(A)$ es no vacío —eso ya venía de la hipótesis de acotación superior—, sino que garantiza que la familia de cotas superiores posee una **menor** cota superior:

$$
\boxed{\exists\min U(A).}
$$

Más precisamente,

$$
\boxed{\min U(A)=\sup A.}
$$

**Uso de completitud:** directo, al pasar de $A\ne\varnothing$ y $U(A)\ne\varnothing$ a la existencia de $\min U(A)$.

[]{#MA-MSOL-ANM-01-003-010}

### 10. Explica por qué el principio del supremo no implica que $\sup A\in A$.

El principio del supremo garantiza que, bajo las hipótesis adecuadas, existe un número real

$$
s=\sup A
$$

que es la menor cota superior de $A$.

Pero la definición de supremo no contiene la condición

$$
s\in A.
$$

Un ejemplo es

$$
A=(0,1).
$$

El conjunto es no vacío y está acotado superiormente. Su supremo es

$$
\sup A=1,
$$

pero

$$
1\notin A.
$$

Por tanto, completitud garantiza la existencia de la **frontera extremal**, no que esa frontera sea alcanzada por el conjunto.

La condición adicional

$$
\sup A\in A
$$

es justamente la que permite identificar al supremo con un máximo.

**Uso de completitud:** sólo para garantizar que el supremo existe; la cuestión de pertenencia se decide por la estructura concreta de $A$.

[]{#MA-MSOL-ANM-01-003-011}

### 11. Para $S_2\subseteq\mathbb Q$, identifica el paso que falla en $\mathbb Q$ pero queda autorizado cuando consideramos $S_2\subseteq\mathbb R$.

En ambos universos podemos verificar las mismas condiciones elementales:

$$
S_2\ne\varnothing
$$

y existen cotas superiores; por ejemplo, $2$ es una cota superior racional y, por tanto, también real.

Dentro de $\mathbb Q$, el paso que **no** está autorizado es

$$
\text{“como }S_2\ne\varnothing\text{ y está acotado superiormente, existe }\sup_{\mathbb Q}S_2\text{”.}
$$

De hecho, §3.1 estableció que esa menor cota superior racional no existe.

En cambio, al considerar el mismo conjunto como subconjunto de $\mathbb R$,

$$
S_2\subseteq\mathbb R,
$$

el principio del supremo sí autoriza

$$
\boxed{\exists s\in\mathbb R:\ s=\sup_{\mathbb R}S_2.}
$$

La diferencia no está en la no vaciedad, la acotación o la densidad, sino en la garantía estructural de existencia disponible en $\mathbb R$.

**Uso de completitud:** exactamente en la existencia de $\sup_{\mathbb R}S_2$; no se identifica ese real con ningún número concreto.

[]{#MA-MSOL-ANM-01-003-012}

### 12. Cadena de completitud y caracterización por $\varepsilon$

En la cadena
   $$
   A\ne\varnothing,\ A\text{ acotado superiormente}
   \Longrightarrow
   s=\sup A
   \Longrightarrow
   \forall\varepsilon>0\;\exists a\in A:
   s-\varepsilon<a\le s,
   $$
   ¿qué flecha usa completitud y qué flecha usa resultados de C02?

La primera flecha,

$$
A\ne\varnothing,\ A\text{ acotado superiormente}
\Longrightarrow
\exists s=\sup A,
$$

es el **Paso de completitud**. Las hipótesis sólo dicen que $A$ contiene elementos y posee cotas superiores; el principio del supremo garantiza que existe la menor de esas cotas.

La segunda flecha,

$$
s=\sup A
\Longrightarrow
\forall\varepsilon>0\;\exists a\in A:
s-\varepsilon<a\le s,
$$

no requiere una segunda aplicación de completitud. Es la caracterización por $\varepsilon$ del supremo demostrada en C02, aplicada a un supremo cuya existencia ya está establecida.

La cadena de dependencias es, por tanto,

$$
\boxed{
\text{hipótesis}
\Longrightarrow_{\text{completitud}}
\text{supremo existente}
\Longrightarrow_{\text{C02}}
\text{aproximación }\varepsilon.
}
$$

**Uso de completitud:** sólo en la primera flecha.

[]{#MA-MSOL-ANM-01-003-013}

### 13. ¿Por qué sería incorrecto aplicar el principio del supremo a $A=\mathbb R$ sin más?

Porque una de las hipótesis del principio falla.

El conjunto

$$
A=\mathbb R
$$

es ciertamente no vacío, pero no está acotado superiormente en $\mathbb R$.

En efecto, dado cualquier candidato $u\in\mathbb R$, el número

$$
u+1\in\mathbb R
$$

y satisface

$$
u+1>u.
$$

Por tanto, ningún real domina a todos los reales y

$$
U(\mathbb R)=\varnothing.
$$

Como falta la hipótesis de acotación superior, el principio del supremo no autoriza ninguna conclusión de existencia para $\sup\mathbb R$ como número real.

**Uso de completitud:** ninguno, porque el principio ni siquiera es aplicable; primero deben verificarse sus hipótesis.

[]{#MA-MSOL-ANM-01-003-014}

### 14. En la prueba “si $r<\sup A$, entonces existe $a\in A$ con $r<a$”, localiza exactamente el único paso que depende de completitud.

Supongamos que $A$ es no vacío y está acotado superiormente.

El único paso que depende de completitud es el inicial:

> **Paso de completitud.** Por el principio del supremo existe
>
> $$
> s=\sup A.
> $$

Una vez disponible $s$, tomamos un real $r<s$.

Como $s$ es la **menor** cota superior, $r$ no puede ser una cota superior de $A$: si lo fuera, la minimalidad de $s$ obligaría a

$$
s\le r,
$$

contradiciendo $r<s$.

Negar que $r$ sea cota superior significa

$$
\exists a\in A:\ a>r.
$$

Por tanto,

$$
\boxed{r<\sup A\Longrightarrow\exists a\in A:\ r<a.}
$$

La anatomía lógica es:

$$
\text{completitud}
\Longrightarrow
s=\sup A\text{ existe},
$$

seguida únicamente de minimalidad del supremo y negación de la definición de cota superior.

**Uso de completitud:** una sola vez, en la existencia de $s=\sup A$.

## §3.3. La cara dual: el principio del ínfimo

[]{#MA-MSOL-ANM-01-003-015}

### 15. Si $A$ es no vacío y está acotado inferiormente, ¿por qué $-A$ está acotado superiormente?

Como $A$ está acotado inferiormente, existe algún $l\in\mathbb R$ tal que

$$
l\le a
\qquad\text{para todo }a\in A.
$$

Multiplicar por $-1$ invierte la desigualdad:

$$
-a\le -l
\qquad\text{para todo }a\in A.
$$

Pero los elementos de $-A$ son precisamente los números $-a$ con $a\in A$. Por tanto, $-l$ domina a todos los elementos de $-A$ y

$$
\boxed{-l\in U(-A).}
$$

Así, $-A$ está acotado superiormente. Además, como $A\ne\varnothing$, si $a_0\in A$ entonces $-a_0\in -A$, de modo que $-A\ne\varnothing$.

**Uso de completitud:** ninguno. Sólo se usan la hipótesis de acotación inferior y la inversión del orden bajo la reflexión.

[]{#MA-MSOL-ANM-01-003-016}

### 16. En la prueba de existencia de $\inf A$, ¿cuál es exactamente el **Paso de completitud**?

Primero se verifican dos hechos elementales:

$$
-A\ne\varnothing
$$

y

$$
-A\text{ está acotado superiormente}.
$$

Sólo después aparece el paso estructural:

> **Paso de completitud.** Por el principio del supremo, existe
>
> $$
> s=\sup(-A).
> $$

Éste es el único paso directo de completitud. La definición posterior

$$
i=-s
$$

y la demostración de que $i$ es la mayor cota inferior de $A$ usan únicamente orden, reflexión y las propiedades de un supremo ya existente.

Por tanto, la anatomía es

$$
A\text{ acotado inferiormente}
\Longrightarrow
-A\text{ acotado superiormente}
\Longrightarrow_{\text{completitud}}
\exists s=\sup(-A)
\Longrightarrow
\inf A=-s.
$$

[]{#MA-MSOL-ANM-01-003-017}

### 17. Si $s=\sup(-A)$, demuestra sin omitir la inversión de desigualdades que $-s$ es una cota inferior de $A$.

Sea $a\in A$ cualquiera. Entonces

$$
-a\in -A.
$$

Como $s=\sup(-A)$, el número $s$ es una cota superior de $-A$. Por tanto,

$$
-a\le s.
$$

Multiplicamos ambos miembros por $-1$. Al hacerlo, el sentido de la desigualdad se invierte:

$$
a\ge -s.
$$

Es decir,

$$
-s\le a.
$$

Como $a\in A$ era arbitrario,

$$
\boxed{-s\le a\quad\text{para todo }a\in A.}
$$

Por definición, $-s$ es una cota inferior de $A$.

**Uso de completitud:** ninguno nuevo. Se usa solamente que el supremo $s$ ya existe y que es cota superior de $-A$.

[]{#MA-MSOL-ANM-01-003-018}

### 18. Si $l$ es una cota inferior cualquiera de $A$, ¿por qué $-l$ es una cota superior de $-A$ y cómo conduce eso a $l\le -s$?

Si $l$ es cota inferior de $A$, entonces

$$
l\le a
\qquad\text{para todo }a\in A.
$$

Multiplicando por $-1$ e invirtiendo la desigualdad,

$$
-a\le -l
\qquad\text{para todo }a\in A.
$$

Como cada elemento de $-A$ tiene la forma $-a$, esto significa que

$$
-l\in U(-A).
$$

Ahora usamos la minimalidad de

$$
s=\sup(-A).
$$

Como $-l$ es una cota superior de $-A$, necesariamente

$$
s\le -l.
$$

Multiplicando otra vez por $-1$ e invirtiendo el sentido,

$$
\boxed{l\le -s.}
$$

Así, toda cota inferior $l$ de $A$ queda por debajo de $-s$. Junto con el microcontrol anterior, esto muestra que $-s$ es la **mayor** cota inferior.

**Uso de completitud:** ninguno nuevo; la desigualdad usa sólo la minimalidad del supremo ya existente.

[]{#MA-MSOL-ANM-01-003-019}

### 19. Explica por qué la identidad $\inf A=-\sup(-A)$ cumple ahora una función de existencia que no tenía en C02.

En C02 la identidad

$$
\inf A=-\sup(-A)
$$

era **condicional**: describía la relación entre dos extremos suponiendo que los extremos pertinentes ya existían.

En C03 disponemos de una garantía adicional. Si $A$ es no vacío y está acotado inferiormente, entonces $-A$ es no vacío y está acotado superiormente. Por completitud existe

$$
s=\sup(-A).
$$

A partir de ese objeto ya existente definimos

$$
i=-s
$$

y la reflexión demuestra que $i$ es la mayor cota inferior de $A$. Por tanto,

$$
\boxed{\inf A=-\sup(-A)}
$$

no sólo compara dos objetos previamente disponibles: ahora **produce la existencia del ínfimo** a partir de la existencia garantizada del supremo reflejado.

La fórmula pasa, pues, de identidad condicional a mecanismo de transporte de existencia.

**Uso de completitud:** directo en la existencia de $\sup(-A)$; la reflexión posterior no añade otra aplicación.

[]{#MA-MSOL-ANM-01-003-020}

### 20. Demuestra la implicación `INF ⇒ SUP` usando sólo la reflexión.

Supongamos como principio **INF**:

> todo subconjunto no vacío de $\mathbb R$ acotado inferiormente posee ínfimo.

Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente. Entonces $-A$ es no vacío. Además, si $u$ es una cota superior de $A$, de

$$
a\le u
\qquad\text{para todo }a\in A
$$

obtenemos, al multiplicar por $-1$,

$$
-u\le -a
\qquad\text{para todo }a\in A.
$$

Así, $-u$ es una cota inferior de $-A$, de modo que $-A$ está acotado inferiormente.

Por **INF** existe

$$
j=\inf(-A).
$$

Definamos

$$
s=-j.
$$

Probemos que $s=\sup A$.

Si $a\in A$, entonces $-a\in -A$. Como $j$ es cota inferior de $-A$,

$$
j\le -a.
$$

Multiplicando por $-1$,

$$
a\le -j=s.
$$

Así, $s$ es cota superior de $A$.

Ahora sea $u$ cualquier cota superior de $A$. Entonces $-u$ es cota inferior de $-A$. Como $j$ es la **mayor** cota inferior,

$$
-u\le j.
$$

Multiplicando por $-1$,

$$
-j\le u,
$$

es decir,

$$
s\le u.
$$

Por tanto $s$ es la menor cota superior de $A$:

$$
\boxed{s=\sup A.}
$$

Luego

$$
\boxed{\mathrm{INF}\Longrightarrow\mathrm{SUP}.}
$$

La prueba usa sólo el principio INF supuesto y la reflexión del orden.

[]{#MA-MSOL-ANM-01-003-021}

### 21. ¿Por qué `SUP ⇔ INF` no significa que hayamos adoptado dos axiomas independientes?

Porque una equivalencia lógica permite derivar cada formulación a partir de la otra.

En el desarrollo del libro se eligió **SUP** como principio estructural inicial. Después se demostró

$$
\mathrm{SUP}\Longrightarrow\mathrm{INF}
$$

mediante la reflexión $A\mapsto -A$. El microcontrol anterior muestra también

$$
\mathrm{INF}\Longrightarrow\mathrm{SUP}.
$$

Por tanto,

$$
\boxed{\mathrm{SUP}\Longleftrightarrow\mathrm{INF}.}
$$

Pero sólo **SUP** fue postulado como punto de partida. INF es recuperable como teorema derivado. Si hubiéramos elegido INF como base, SUP habría sido el teorema derivado.

Así, la equivalencia significa “misma información estructural expresada en dos lenguajes”, no “dos hipótesis independientes que deban acumularse”.

[]{#MA-MSOL-ANM-01-003-022}

### 22. Para $A=(2,\infty)$, identifica qué principio puede aplicarse, qué reflejo conviene estudiar y cuál es el ínfimo.

El conjunto

$$
A=(2,\infty)
$$

no está acotado superiormente, de modo que el principio del supremo no puede aplicarse **directamente a $A$**.

Sí está acotado inferiormente; por ejemplo, $2$ es una cota inferior. Por ello puede aplicarse el **principio del ínfimo derivado**.

Para abrir su fundamento conviene reflejar:

$$
-A=(-\infty,-2).
$$

Este conjunto es no vacío y está acotado superiormente. Su supremo es

$$
\sup(-A)=-2.
$$

Por la identidad de reflexión,

$$
\inf A=-\sup(-A)=-(-2)=2.
$$

Por tanto,

$$
\boxed{\inf(2,\infty)=2.}
$$

Obsérvese que $2\notin A$: el ínfimo existe aunque no sea mínimo.

**Uso de completitud:** en la garantía general de existencia del supremo de $-A$ —o, equivalentemente, del ínfimo de $A$—; la identificación concreta del valor usa la teoría elemental de C02.

[]{#MA-MSOL-ANM-01-003-023}

### 23. En la cadena que conduce a la caracterización $\varepsilon$ del ínfimo, distingue el paso que usa completitud del paso que usa C02.

La cadena es

$$
A\ne\varnothing,
\quad
A\text{ acotado inferiormente}
\Longrightarrow
\exists i=\inf A
\Longrightarrow
\forall\varepsilon>0\;\exists a\in A:
\quad i\le a<i+\varepsilon.
$$

La **primera flecha** depende de completitud. Si abrimos el principio del ínfimo derivado, el mecanismo es

$$
A\text{ acotado inferiormente}
\Longrightarrow
-A\text{ acotado superiormente}
\Longrightarrow_{\mathrm{SUP}}
\exists s=\sup(-A)
\Longrightarrow
\exists i=-s=\inf A.
$$

El único gasto directo de completitud está en la existencia de $s=\sup(-A)$.

La **segunda flecha** no usa una nueva completitud. Una vez que $i=\inf A$ existe, la afirmación

$$
\forall\varepsilon>0\;\exists a\in A:
\quad i\le a<i+\varepsilon
$$

es exactamente la caracterización por $\varepsilon$ del ínfimo demostrada en C02.

Por tanto,

$$
\boxed{
\text{hipótesis inferiores}
\Longrightarrow_{\text{completitud}}
\text{ínfimo existente}
\Longrightarrow_{\text{C02}}
\text{aproximación }\varepsilon.
}
$$

## §3.4. Una consecuencia decisiva: la propiedad arquimediana

[]{#MA-MSOL-ANM-01-003-024}

### 24. ¿Por qué la hipótesis “$\mathbb N$ está acotado superiormente” permite invocar el principio del supremo?

El principio del supremo exige dos condiciones sobre el conjunto al que se aplica: que sea no vacío y que esté acotado superiormente.

Bajo la hipótesis contradictoria del argumento ya tenemos la segunda:

$$
\mathbb N\text{ está acotado superiormente en }\mathbb R.
$$

La primera es elemental: $\mathbb N\ne\varnothing$; por ejemplo, $1\in\mathbb N$.

Por tanto, bajo esa hipótesis, quedan verificadas exactamente las condiciones de entrada del principio del supremo:

$$
\mathbb N\ne\varnothing,
\qquad
\mathbb N\text{ acotado superiormente}.
$$

Sólo entonces estamos autorizados a concluir que existe

$$
s=\sup\mathbb N.
$$

**Uso de completitud:** directo únicamente en esta conclusión de existencia. La no vaciedad y la acotación supuesta son las hipótesis que permiten aplicar el principio.

[]{#MA-MSOL-ANM-01-003-025}

### 25. En la prueba de arquimedianidad, ¿cuál es exactamente el único **Paso de completitud**?

El único paso directo es éste:

> **Paso de completitud.** Suponiendo, para obtener una contradicción, que $\mathbb N$ está acotado superiormente, como además $\mathbb N\ne\varnothing$, el principio del supremo garantiza que existe
>
> $$
> s=\sup\mathbb N.
> $$

Todo lo que viene después usa propiedades de ese supremo ya existente, el orden y la aritmética elemental:

$$
s-1<s,
$$

la minimalidad de $s$, la negación de “ser cota superior”, la existencia de $n\in\mathbb N$ con $n>s-1$, la suma de $1$ y la clausura $n+1\in\mathbb N$.

La trazabilidad completa es

$$
\mathbb N\text{ acotado}
\Longrightarrow_{\text{completitud}}
\exists s=\sup\mathbb N
\Longrightarrow_{\text{orden + aritmética}}
\text{contradicción}.
$$

**Uso de completitud:** una sola vez, en la existencia de $s$.

[]{#MA-MSOL-ANM-01-003-026}

### 26. ¿Por qué $s-1$ no puede ser una cota superior si $s=\sup\mathbb N$?

Como

$$
s-1<s,
$$

si $s-1$ fuera también una cota superior de $\mathbb N$, tendríamos una cota superior estrictamente menor que $s$.

Pero $s=\sup\mathbb N$ significa precisamente que $s$ es la **menor** de todas las cotas superiores. En particular, para toda cota superior $u$ de $\mathbb N$ debe cumplirse

$$
s\le u.
$$

Aplicando esto al supuesto $u=s-1$ obtendríamos

$$
s\le s-1,
$$

lo cual contradice $s-1<s$.

Por tanto,

$$
\boxed{s-1\text{ no es una cota superior de }\mathbb N.}
$$

**Uso de completitud:** ninguno nuevo. Sólo se usa la minimalidad del supremo cuya existencia ya fue obtenida.

[]{#MA-MSOL-ANM-01-003-027}

### 27. Explica cuidadosamente cómo la negación de “$s-1$ es cota superior” produce un natural $n$ con $n>s-1$.

Decir que $s-1$ es una cota superior de $\mathbb N$ significa

$$
\forall n\in\mathbb N,
\qquad
n\le s-1.
$$

Negar esta afirmación cuantificada da

$$
\exists n\in\mathbb N
\quad\text{tal que}\quad
\neg(n\le s-1).
$$

Como el orden de $\mathbb R$ es total,

$$
\neg(n\le s-1)
\quad\Longleftrightarrow\quad
n>s-1.
$$

Por tanto,

$$
\boxed{\exists n\in\mathbb N:\ n>s-1.}
$$

El testigo $n$ no lo produce una nueva aplicación de completitud. Aparece al negar correctamente la definición universal de cota superior.

[]{#MA-MSOL-ANM-01-003-028}

### 28. ¿Dónde se usa que $n+1$ vuelve a pertenecer a $\mathbb N$?

Del paso anterior obtenemos un natural $n$ tal que

$$
n>s-1.
$$

Sumando $1$ a ambos miembros,

$$
n+1>s.
$$

Para convertir esta desigualdad en una contradicción con el hecho de que $s$ es cota superior de $\mathbb N$, necesitamos saber que el número que acaba de superar a $s$ sigue perteneciendo al conjunto que $s$ debía dominar.

Ahí se usa exactamente la clausura de los naturales bajo sucesor:

$$
n\in\mathbb N
\quad\Longrightarrow\quad
n+1\in\mathbb N.
$$

Como $s$ es cota superior de $\mathbb N$, todo elemento de $\mathbb N$ debería satisfacer $m\le s$. Pero $m=n+1\in\mathbb N$ satisface $n+1>s$. Ésa es la contradicción.

**Uso de completitud:** ninguno nuevo; este paso es puramente aritmético y de pertenencia.

[]{#MA-MSOL-ANM-01-003-029}

### 29. Demuestra que “$\mathbb N$ no está acotado superiormente” equivale a “para todo $x\in\mathbb R$ existe $n\in\mathbb N$ con $n>x$”.

Probemos las dos implicaciones.

**Primera dirección.** Supongamos que $\mathbb N$ no está acotado superiormente. Sea $x\in\mathbb R$. Si no existiera ningún $n\in\mathbb N$ con $n>x$, entonces tendríamos

$$
\forall n\in\mathbb N,
\qquad
n\le x.
$$

Eso diría exactamente que $x$ es una cota superior de $\mathbb N$, contradiciendo la hipótesis. Luego existe $n\in\mathbb N$ tal que

$$
n>x.
$$

**Segunda dirección.** Supongamos ahora que

$$
\forall x\in\mathbb R\;\exists n\in\mathbb N:\ n>x.
$$

Si $\mathbb N$ tuviera una cota superior $M\in\mathbb R$, la propiedad aplicada a $x=M$ produciría un natural $n$ con

$$
n>M,
$$

contradiciendo que $M$ domina a todos los naturales.

Por tanto,

$$
\boxed{
\mathbb N\text{ no está acotado superiormente}
\Longleftrightarrow
\forall x\in\mathbb R\;\exists n\in\mathbb N:\ n>x.
}
$$

**Uso de completitud:** ninguno en esta equivalencia. La completitud fue necesaria antes para demostrar que la primera formulación es verdadera en $\mathbb R$.

[]{#MA-MSOL-ANM-01-003-030}

### 30. Dado $\varepsilon>0$, justifica cada paso de la deducción

   $$
   n>\frac{1}{\varepsilon}
   \quad\Longrightarrow\quad
   \frac{1}{n}<\varepsilon.
   $$

Como $\varepsilon>0$, tenemos

$$
\frac{1}{\varepsilon}>0.
$$

Si

$$
n>\frac{1}{\varepsilon},
$$

entonces en particular $n>0$. Por tanto $n\varepsilon>0$ y podemos multiplicar la desigualdad original por el número positivo $\varepsilon$ sin cambiar su sentido:

$$
n\varepsilon>1.
$$

Ahora dividimos por el número positivo $n$:

$$
\varepsilon>\frac{1}{n}.
$$

Es decir,

$$
\boxed{\frac{1}{n}<\varepsilon.}
$$

Equivalentemente, puesto que $n$ y $1/\varepsilon$ son positivos, tomar recíprocos invierte el orden:

$$
n>\frac1\varepsilon
\quad\Longrightarrow\quad
\frac1n<\varepsilon.
$$

La positividad es indispensable para justificar tanto las divisiones como el sentido de las desigualdades.

[]{#MA-MSOL-ANM-01-003-031}

### 31. ¿Por qué la afirmación $\forall\varepsilon>0\;\exists n:1/n<\varepsilon$ no necesita todavía el lenguaje de convergencia?

Porque la afirmación ya tiene un significado completo usando sólo cuantificadores, orden y aritmética:

$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}
\quad\text{tal que}\quad
\frac1n<\varepsilon.
$$

Para cada tolerancia positiva se pide **algún** natural cuyo recíproco quede por debajo de ella. Eso es una afirmación de existencia de una escala suficientemente pequeña.

No hace falta introducir una definición de límite ni afirmar todavía que

$$
\frac1n\longrightarrow0.
$$

En particular, aquí no estamos usando como argumento una condición “eventual” del tipo “existe $N$ tal que para todo $n\ge N$...”. Sólo necesitamos elegir un natural adecuado para la tolerancia concreta dada.

Por tanto, el contenido de §3.4 permanece enteramente dentro de la propiedad arquimediana y del orden.

[]{#MA-MSOL-ANM-01-003-032}

### 32. ¿Qué muestra $\mathbb Q$ acerca de la conversa “arquimediano $\Rightarrow$ completo”?

Muestra que la conversa es falsa.

Los racionales son arquimedianos: dado cualquier $q\in\mathbb Q$, existe un natural $n$ con

$$
n>q.
$$

Sin embargo, $\mathbb Q$ no es completo en el sentido de orden usado en C03. El conjunto racional

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}
$$

es no vacío y está acotado superiormente dentro de $\mathbb Q$, pero no posee supremo racional.

Así,

$$
\boxed{
\text{arquimedianidad}
\not\Longrightarrow
\text{completitud}.
}
$$

La implicación demostrada en la sección es sólo

$$
\text{completitud}\Longrightarrow\text{arquimedianidad}.
$$

$\mathbb Q$ conserva la propiedad arquimediana pero carece de la garantía general de existencia de supremos.

[]{#MA-MSOL-ANM-01-003-033}

### 33. En una prueba futura que use $1/n<\varepsilon$, ¿qué dependencia estructural queda escondida detrás de esa elección de $n$?

La elección de $n$ usa la propiedad arquimediana en la forma

$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}:
\frac1n<\varepsilon.
$$

Pero en este capítulo esa propiedad no fue tomada como axioma independiente. Se obtuvo a partir de la completitud mediante la cadena

$$
\text{SUP}
\Longrightarrow
\mathbb N\text{ no acotado superiormente}
\Longrightarrow
\text{propiedad arquimediana}
\Longrightarrow
\forall\varepsilon>0\;\exists n:\frac1n<\varepsilon.
$$

Por eso, cuando una prueba posterior diga simplemente “elija $n$ suficientemente grande para que $1/n<\varepsilon$”, el uso de completitud será **indirecto**: la completitud ya fue consumida al demostrar la propiedad arquimediana que autoriza esa elección.

La trazabilidad correcta es

$$
\boxed{
\text{completitud}
\Longrightarrow
\text{arquimedianidad}
\Longrightarrow
\text{escala }1/n<\varepsilon.
}
$$

No hay una nueva aplicación directa del principio del supremo en cada elección de $n$; hay una dependencia heredada del teorema arquimediano.
## §3.5. Intervalos encajados: conservar un punto al refinar

[]{#MA-MSOL-ANM-01-003-034}

### 34. Si $I_{n+1}\subseteq I_n$, demuestra directamente que $a_n\le a_{n+1}$ y $b_{n+1}\le b_n$.

Como

$$
I_{n+1}=[a_{n+1},b_{n+1}]
\subseteq
I_n=[a_n,b_n],
$$

los dos extremos de $I_{n+1}$ pertenecen también a $I_n$.

Primero,

$$
a_{n+1}\in I_{n+1}\subseteq I_n.
$$

Pertenecer a $I_n=[a_n,b_n]$ significa

$$
a_n\le a_{n+1}\le b_n.
$$

En particular,

$$
\boxed{a_n\le a_{n+1}.}
$$

Del mismo modo,

$$
b_{n+1}\in I_{n+1}\subseteq I_n,
$$

así que

$$
a_n\le b_{n+1}\le b_n.
$$

Por tanto,

$$
\boxed{b_{n+1}\le b_n.}
$$

La inclusión de intervalos fuerza, pues, que los extremos izquierdos avancen hacia la derecha y los derechos retrocedan hacia la izquierda.

**Uso de completitud:** ninguno. Sólo se usa pertenencia a intervalos cerrados e inclusión.

[]{#MA-MSOL-ANM-01-003-035}

### 35. Demuestra por casos que $a_m\le b_n$ para cualesquiera $m,n\ge1$.

Sean $m,n\ge1$.

**Caso 1: $m\le n$.** Por el resultado anterior,

$$
a_m\le a_n.
$$

Como $I_n=[a_n,b_n]$ es no vacío,

$$
a_n\le b_n.
$$

Por transitividad,

$$
a_m\le b_n.
$$

**Caso 2: $m>n$.** Del encajamiento iterado obtenemos

$$
I_m\subseteq I_n.
$$

Como $a_m\in I_m$, también

$$
a_m\in I_n=[a_n,b_n].
$$

Por definición de intervalo cerrado,

$$
a_n\le a_m\le b_n.
$$

En particular,

$$
a_m\le b_n.
$$

En ambos casos,

$$
\boxed{a_m\le b_n\qquad\text{para todos }m,n\ge1.}
$$

**Uso de completitud:** ninguno. La compatibilidad cruzada procede sólo del encajamiento y del orden.

[]{#MA-MSOL-ANM-01-003-036}

### 36. ¿Por qué el conjunto $A=\{a_n:n\ge1\}$ es no vacío?

Por definición,

$$
A=\{a_n:n\ge1\}.
$$

Como la familia comienza en $n=1$, el extremo izquierdo

$$
a_1
$$

pertenece a $A$. Por tanto,

$$
\boxed{A\ne\varnothing.}
$$

Esta verificación es necesaria antes de invocar el principio del supremo.

**Uso de completitud:** ninguno. Sólo se exhibe un elemento de $A$.

[]{#MA-MSOL-ANM-01-003-037}

### 37. ¿Por qué **cada** $b_n$ es una cota superior de $A$?

Fijemos un índice $n\ge1$.

Para probar que $b_n$ es cota superior de

$$
A=\{a_m:m\ge1\},
$$

debemos verificar que todo elemento de $A$ queda por debajo de $b_n$.

Pero la compatibilidad cruzada ya demostrada afirma que, para todo $m\ge1$,

$$
a_m\le b_n.
$$

Como los elementos de $A$ son precisamente los $a_m$, se sigue que

$$
\forall a\in A,\qquad a\le b_n.
$$

Por definición,

$$
\boxed{b_n\in U(A).}
$$

Como $n$ era arbitrario, esto vale para **cada** extremo derecho $b_n$.

**Uso de completitud:** ninguno. Esta acotación se deduce de la compatibilidad cruzada.

[]{#MA-MSOL-ANM-01-003-038}

### 38. Localiza exactamente el único **Paso de completitud** en la prueba del teorema.

Antes de usar completitud se verifican dos hechos:

$$
A=\{a_n:n\ge1\}\ne\varnothing
$$

y

$$
A\text{ está acotado superiormente},
$$

porque, por ejemplo, $b_1$ —y de hecho cada $b_n$— es una cota superior de $A$.

Sólo entonces aparece el paso estructural:

> **Paso de completitud.** Por el principio del supremo, existe
>
> $$
> x=\sup A.
> $$

Éste es el único uso directo de completitud.

Después, las desigualdades

$$
a_n\le x
$$

y

$$
x\le b_n
$$

proceden respectivamente de que $x$ es cota superior de $A$ y de que $x$ es la menor cota superior de $A$.

La trazabilidad es

$$
\boxed{
A\ne\varnothing,\ A\text{ acotado superiormente}
\Longrightarrow_{\text{completitud}}
\exists x=\sup A
\Longrightarrow_{\text{orden}}
x\in I_n\ \forall n.
}
$$

[]{#MA-MSOL-ANM-01-003-039}

### 39. Una vez definido $x=\sup A$, ¿qué propiedad del supremo da $a_n\le x$?

Como

$$
a_n\in A
$$

y

$$
x=\sup A,
$$

el número $x$ es, por definición, una **cota superior** de $A$.

Por tanto todo elemento de $A$ satisface

$$
a\le x.
$$

Aplicando esto al elemento concreto $a_n\in A$ obtenemos

$$
\boxed{a_n\le x.}
$$

**Uso de completitud:** ninguno nuevo. La completitud garantizó previamente que $x$ existe; esta desigualdad usa sólo la propiedad de cota superior del supremo.

[]{#MA-MSOL-ANM-01-003-040}

### 40. ¿Qué propiedad del supremo da $x\le b_n$?

Ya sabemos que, para cada $n$,

$$
b_n
$$

es una cota superior de $A$.

Como

$$
x=\sup A
$$

es la **menor** de todas las cotas superiores de $A$, debe quedar por debajo de cualquier otra cota superior. En particular,

$$
\boxed{x\le b_n.}
$$

**Uso de completitud:** ninguno nuevo. Se usa únicamente la minimalidad del supremo ya existente.

[]{#MA-MSOL-ANM-01-003-041}

### 41. ¿Por qué esas dos desigualdades permiten concluir $x\in I_n$ sólo porque $I_n$ es cerrado?

Las dos desigualdades son

$$
a_n\le x\le b_n.
$$

Para un intervalo cerrado,

$$
I_n=[a_n,b_n],
$$

la condición de pertenencia es exactamente

$$
x\in I_n
\quad\Longleftrightarrow\quad
a_n\le x\le b_n.
$$

Por tanto,

$$
\boxed{x\in I_n.}
$$

El carácter **cerrado** es decisivo porque los extremos están incluidos. Si sólo supiéramos que

$$
a_n\le x\le b_n
$$

y el intervalo fuera abierto,

$$
(a_n,b_n),
$$

todavía podría ocurrir que $x=a_n$ o $x=b_n$, casos en los que $x$ no pertenecería al intervalo.

Así, las desigualdades no bastan para un intervalo abierto, pero sí bastan exactamente para $[a_n,b_n]$.

**Uso de completitud:** ninguno nuevo.

[]{#MA-MSOL-ANM-01-003-042}

### 42. Verifica sin lenguaje de límites que los intervalos $J_n=(0,1/n)$ están encajados y tienen intersección vacía.

Primero probemos el encajamiento.

Para todo $n\ge1$,

$$
n+1>n>0.
$$

Al tomar recíprocos positivos se invierte el orden:

$$
\frac1{n+1}<\frac1n.
$$

Por tanto, si

$$
x\in J_{n+1}=\left(0,\frac1{n+1}\right),
$$

entonces

$$
0<x<\frac1{n+1}<\frac1n,
$$

de modo que

$$
x\in J_n.
$$

Así,

$$
\boxed{J_{n+1}\subseteq J_n.}
$$

Ahora supongamos, para obtener una contradicción, que existe

$$
x\in\bigcap_{n=1}^{\infty}J_n.
$$

Entonces, por pertenecer a cada $J_n$,

$$
x>0.
$$

La propiedad arquimediana de §3.4 permite elegir $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<x.
$$

Pero la pertenencia $x\in J_n$ exige simultáneamente

$$
x<\frac1n.
$$

Contradicción.

Por tanto,

$$
\boxed{
\bigcap_{n=1}^{\infty}\left(0,\frac1n\right)=\varnothing.
}
$$

No se ha usado lenguaje de límites. La única dependencia no elemental es la propiedad arquimediana ya demostrada en §3.4, que a su vez depende indirectamente de completitud.

[]{#MA-MSOL-ANM-01-003-043}

### 43. Da un ejemplo de intervalos cerrados encajados cuya intersección contenga más de un punto.

Tomemos la familia constante

$$
I_n=[0,1]
\qquad\text{para todo }n\ge1.
$$

Cada intervalo es cerrado y no vacío. Además,

$$
I_{n+1}=I_n,
$$

por lo que ciertamente

$$
I_{n+1}\subseteq I_n.
$$

La intersección es

$$
\bigcap_{n=1}^{\infty}I_n=[0,1].
$$

Este conjunto contiene, por ejemplo, tanto $0$ como $1$, y de hecho infinitos puntos.

Por tanto, una familia cerrada y encajada puede satisfacer todas las hipótesis de §3.5 sin que su intersección sea un singleton.

[]{#MA-MSOL-ANM-01-003-044}

### 44. ¿Por qué el teorema de esta sección garantiza existencia pero no unicidad?

La conclusión demostrada en §3.5 es únicamente

$$
\boxed{
\bigcap_{n=1}^{\infty}I_n\ne\varnothing.
}
$$

Eso significa que existe **al menos un** punto común a todos los intervalos.

En ninguna parte de las hipótesis se exige que la anchura de los intervalos se haga arbitrariamente pequeña. Por ello puede sobrevivir una región completa.

El ejemplo

$$
I_n=[0,1]
\qquad\forall n
$$

satisface cierre, no vaciedad y encajamiento, pero

$$
\bigcap_{n=1}^{\infty}I_n=[0,1].
$$

Así, las hipótesis de §3.5 son suficientes para **existencia**, pero no para **unicidad**.

La unicidad requerirá una condición adicional de estrechamiento, reservada para §3.6; aquí no la usamos todavía.

[]{#MA-MSOL-ANM-01-003-045}

### 45. ¿Qué diferencia de estatus lógico debemos conservar entre el caso numerable encajado de §3.5 y el principio general de intersección que aparecerá en §3.7?

El resultado de §3.5 es una **consecuencia concreta** de la completitud:

$$
\text{completitud}
\Longrightarrow
\text{intersección no vacía para una familia numerable de intervalos cerrados encajados}.
$$

Su estructura particular incluye un índice numerable y la condición fuerte

$$
I_{n+1}\subseteq I_n.
$$

En cambio, §3.7 introducirá una formulación intervalar más general basada en una familia de intervalos cerrados cuyos extremos satisfacen una condición cruzada del tipo

$$
a_i\le b_j
\qquad\text{para todos los índices }i,j.
$$

Esa formulación general será incorporada a la cadena de **equivalencias** de completitud.

Por tanto debemos evitar el salto lógico

$$
\text{caso numerable encajado}
\quad\Longrightarrow\quad
\text{“ésta es ya la formulación intervalar general equivalente”.}
$$

La relación correcta en este punto es:

$$
\boxed{
\text{§3.5: consecuencia especializada}
\qquad\text{vs.}\qquad
\text{§3.7: formulación general equivalente}.
}
$$

Aquí sólo registramos esa diferencia de estatus, tal como la sección la anuncia; no adelantamos todavía la demostración de la equivalencia general.

## §3.6. Refinar hasta aislar un único punto

[]{#MA-MSOL-ANM-01-003-046}

### 46. ¿Por qué el estrechamiento arbitrario, por sí solo, garantiza como máximo un punto pero no existencia?

La hipótesis de estrechamiento dice

$$
\forall\varepsilon>0\;\exists n:
\quad b_n-a_n<\varepsilon.
$$

Supongamos que dos puntos distintos $x$ e $y$ pertenecen a todos los intervalos. Entonces

$$
\delta=|x-y|>0.
$$

Podemos usar $\varepsilon=\delta$ en la hipótesis y obtener un índice $n$ con

$$
b_n-a_n<\delta.
$$

Pero, como $x,y\in[a_n,b_n]$, necesariamente

$$
|x-y|\le b_n-a_n,
$$

lo que produce

$$
\delta\le b_n-a_n<\delta,
$$

una contradicción. Por tanto la intersección contiene **a lo sumo un punto**.

Sin embargo, esta argumentación comienza suponiendo que hay dos puntos candidatos; no construye ninguno. Una intersección puede ser vacía y satisfacer vacíamente la propiedad “contiene a lo sumo un punto”.

Así,

$$
\boxed{
\text{estrechamiento arbitrario}
\Longrightarrow
\left|\bigcap_n I_n\right|\le1,
}
$$

pero no

$$
\text{estrechamiento arbitrario}
\Longrightarrow
\bigcap_n I_n\ne\varnothing.
$$

**Uso de completitud:** ninguno. Esta respuesta describe sólo el mecanismo de unicidad.

[]{#MA-MSOL-ANM-01-003-047}

### 47. Si $x\ne y$ pertenecieran a todos los intervalos, ¿por qué $\delta=|x-y|$ es una tolerancia legítima en la hipótesis de estrechamiento?

La hipótesis de estrechamiento puede aplicarse a **cualquier** número real positivo $\varepsilon$.

Si

$$
x\ne y,
$$

entonces, por la propiedad definida positiva del valor absoluto,

$$
|x-y|>0.
$$

Por tanto

$$
\delta=|x-y|
$$

es un número real estrictamente positivo y satisface exactamente la condición exigida para desempeñar el papel de $\varepsilon$.

Así podemos sustituir legítimamente

$$
\varepsilon:=\delta=|x-y|
$$

en

$$
\forall\varepsilon>0\;\exists n:
\quad b_n-a_n<\varepsilon,
$$

y concluir que existe $n$ tal que

$$
\boxed{b_n-a_n<|x-y|.}
$$

No se ha elegido una tolerancia especial desde fuera del problema: la propia separación positiva entre los dos candidatos proporciona la escala que el estrechamiento debe superar.

**Uso de completitud:** ninguno.

[]{#MA-MSOL-ANM-01-003-048}

### 48. Si $x,y\in[a_n,b_n]$, demuestra que $|x-y|\le b_n-a_n$.

Como

$$
x,y\in[a_n,b_n],
$$

tenemos

$$
a_n\le x\le b_n,
\qquad
a_n\le y\le b_n.
$$

Hay dos casos.

Si $x\le y$, entonces

$$
a_n\le x\le y\le b_n.
$$

Restando $x$ en la desigualdad $y\le b_n$ obtenemos

$$
y-x\le b_n-x.
$$

Y de $a_n\le x$ se sigue

$$
b_n-x\le b_n-a_n.
$$

Por transitividad,

$$
y-x\le b_n-a_n.
$$

Como $x\le y$,

$$
|x-y|=y-x,
$$

y por tanto

$$
|x-y|\le b_n-a_n.
$$

Si $y\le x$, el mismo argumento intercambiando $x$ e $y$ da

$$
x-y\le b_n-a_n.
$$

Ahora

$$
|x-y|=x-y.
$$

En ambos casos,

$$
\boxed{|x-y|\le b_n-a_n.}
$$

**Uso de completitud:** ninguno; es una propiedad métrica elemental de un intervalo cerrado.

[]{#MA-MSOL-ANM-01-003-049}

### 49. ¿Dónde aparece la contradicción al elegir $n$ con $b_n-a_n<|x-y|$?

Si $x$ e $y$ pertenecen a todos los intervalos, entonces también pertenecen al intervalo particular $I_n=[a_n,b_n]$ elegido mediante el estrechamiento.

Por el microcontrol anterior,

$$
|x-y|\le b_n-a_n.
$$

Pero el índice $n$ fue escogido precisamente para que

$$
b_n-a_n<|x-y|.
$$

Al encadenar ambas desigualdades obtenemos

$$
\boxed{|x-y|\le b_n-a_n<|x-y|.}
$$

Por transitividad esto implicaría

$$
|x-y|<|x-y|,
$$

lo cual es imposible.

Ésa es la contradicción exacta. Por tanto la hipótesis $x\ne y$ no puede mantenerse y necesariamente

$$
x=y.
$$

**Uso de completitud:** ninguno nuevo. La contradicción usa sólo pertenencia al intervalo, distancia y estrechamiento.

[]{#MA-MSOL-ANM-01-003-050}

### 50. ¿Qué parte del teorema “la intersección es un singleton” hereda completitud desde §3.5?

La conclusión

$$
\bigcap_{n=1}^{\infty}I_n=\{x\}
$$

combina dos afirmaciones lógicamente distintas.

La primera es **existencia**:

$$
\bigcap_{n=1}^{\infty}I_n\ne\varnothing.
$$

Ésta es la parte heredada de §3.5. Allí se construyó

$$
A=\{a_n:n\ge1\}
$$

y se usó completitud exactamente para obtener

$$
x=\sup A.
$$

Después se probó que $x\in I_n$ para todo $n$.

La segunda afirmación es **unicidad**:

$$
\left|\bigcap_{n=1}^{\infty}I_n\right|\le1.
$$

Ésta procede del estrechamiento arbitrario y no requiere una segunda aplicación del principio del supremo.

Por tanto,

$$
\boxed{
\underbrace{\text{existencia}}_{\text{hereda completitud desde §3.5}}
+
\underbrace{\text{unicidad}}_{\text{estrechamiento}}
\Longrightarrow
\text{singleton}.
}
$$

[]{#MA-MSOL-ANM-01-003-051}

### 51. ¿Por qué la prueba de unicidad no necesita una segunda aplicación del principio del supremo?

Una vez que estudiamos la unicidad, el argumento ya no necesita producir un nuevo extremo.

Suponemos que existen dos candidatos comunes $x$ e $y$ y, buscando contradicción, que

$$
x\ne y.
$$

Entonces

$$
\delta=|x-y|>0.
$$

La hipótesis de estrechamiento produce un índice $n$ con

$$
b_n-a_n<\delta.
$$

Como ambos puntos pertenecen a $I_n$,

$$
\delta=|x-y|\le b_n-a_n,
$$

y aparece la contradicción.

En ninguno de esos pasos se construye un supremo ni un ínfimo. Se usan solamente:

- positividad de la distancia entre puntos distintos;
- la hipótesis cuantificada de estrechamiento;
- la desigualdad $|x-y|\le b_n-a_n$ para dos puntos de un mismo intervalo.

Así,

$$
\boxed{
\text{la completitud produce existencia una vez;}
\quad
\text{el estrechamiento fuerza unicidad sin otro SUP.}
}
$$

[]{#MA-MSOL-ANM-01-003-052}

### 52. Explica por qué $I_n=[0,1]$ viola exactamente la hipótesis de estrechamiento.

Para la familia constante

$$
I_n=[0,1]
\qquad\text{para todo }n,
$$

el ancho de cada intervalo es

$$
b_n-a_n=1-0=1.
$$

La hipótesis de estrechamiento exigiría que para **todo** $\varepsilon>0$ existiera algún $n$ con

$$
1<\varepsilon.
$$

Basta elegir una tolerancia positiva menor que $1$, por ejemplo

$$
\varepsilon=\frac12.
$$

Entonces la condición requerida sería

$$
1<\frac12,
$$

lo cual es falso para todos los índices.

Por tanto,

$$
\boxed{
\exists\varepsilon>0\;\forall n:
\quad b_n-a_n\ge\varepsilon,
}
$$

y falla exactamente el estrechamiento arbitrario.

Las demás hipótesis sí se cumplen: los intervalos son cerrados, no vacíos y encajados. Por eso este ejemplo aísla con precisión la necesidad de la nueva condición para obtener unicidad.

[]{#MA-MSOL-ANM-01-003-053}

### 53. ¿Por qué los intervalos abiertos $(0,1/n)$ muestran que estrechamiento no sustituye a la hipótesis de existencia?

Consideremos

$$
J_n=\left(0,\frac1n\right).
$$

Su ancho es

$$
\frac1n-0=\frac1n.
$$

Dado cualquier $\varepsilon>0$, la propiedad arquimediana permite elegir $n$ tal que

$$
\frac1n<\varepsilon.
$$

Por tanto la familia satisface la condición de estrechamiento arbitrario.

Sin embargo, como ya se demostró en §3.5,

$$
\bigcap_{n=1}^{\infty}J_n=\varnothing.
$$

El problema es que los intervalos son abiertos: el mecanismo de existencia de §3.5 para intervalos **cerrados** encajados no se aplica.

Así, el estrechamiento sólo controla cuántos puntos podrían sobrevivir; no obliga a que sobreviva alguno:

$$
\boxed{
\text{estrechamiento}
\not\Rightarrow
\text{existencia}.
}
$$

La existencia y la unicidad son capas lógicas distintas.

**Dependencia estructural:** la finura $1/n<\varepsilon$ usa indirectamente la completitud a través de la propiedad arquimediana, pero eso no repara la falta de la hipótesis cerrada de existencia.

[]{#MA-MSOL-ANM-01-003-054}

### 54. Verifica por inducción que tras $k$ bisecciones el ancho es $L/2^k$.

Sea $L>0$ el ancho inicial del intervalo $J_0$.

Demostraremos por inducción que

$$
\operatorname{anch}(J_k)=\frac{L}{2^k}
$$

para todo $k\ge0$.

**Caso base: $k=0$.** Por definición,

$$
\operatorname{anch}(J_0)=L=\frac{L}{2^0}.
$$

**Paso inductivo.** Supongamos que para cierto $k\ge0$ se cumple

$$
\operatorname{anch}(J_k)=\frac{L}{2^k}.
$$

La siguiente etapa conserva una de las dos mitades cerradas de $J_k$. Cada mitad tiene exactamente la mitad del ancho de $J_k$. Por tanto,

$$
\operatorname{anch}(J_{k+1})
=\frac12\operatorname{anch}(J_k)
=\frac12\frac{L}{2^k}
=\frac{L}{2^{k+1}}.
$$

Por inducción,

$$
\boxed{
\operatorname{anch}(J_k)=\frac{L}{2^k}
\quad\text{para todo }k\ge0.
}
$$

**Uso de completitud:** ninguno; es una identidad finita obtenida por inducción.

[]{#MA-MSOL-ANM-01-003-055}

### 55. Demuestra por inducción que $2^r\ge r+1$ para todo $r\ge1$.

Procedemos por inducción sobre $r$.

**Caso base: $r=1$.**

$$
2^1=2=1+1.
$$

Luego la desigualdad vale para $r=1$.

**Paso inductivo.** Supongamos que para cierto $r\ge1$ tenemos

$$
2^r\ge r+1.
$$

Multiplicando por $2>0$,

$$
2^{r+1}=2\cdot2^r\ge2(r+1).
$$

Ahora

$$
2(r+1)=2r+2
$$

y, como $r\ge0$,

$$
2r+2\ge r+2.
$$

Por tanto,

$$
2^{r+1}\ge r+2=(r+1)+1.
$$

La propiedad queda demostrada para $r+1$.

Concluimos por inducción que

$$
\boxed{2^r\ge r+1\quad\text{para todo }r\ge1.}
$$

**Uso de completitud:** ninguno.

[]{#MA-MSOL-ANM-01-003-056}

### 56. Dado $\varepsilon>0$, reconstruye el argumento finito que produce $k$ con $L/2^k<\varepsilon$ sin usar notación de límite.

Supongamos $L>0$ y fijemos

$$
\varepsilon>0.
$$

Como

$$
\frac{L}{\varepsilon}>0,
$$

la propiedad arquimediana garantiza que existe

$$
m\in\mathbb N_{>0}
$$

tal que

$$
m>\frac{L}{\varepsilon}.
$$

Tomemos

$$
k=m.
$$

Por el resultado inductivo anterior,

$$
2^k=2^m\ge m+1>m>\frac{L}{\varepsilon}.
$$

Todos los términos son positivos. Al tomar recíprocos, el orden se invierte:

$$
\frac1{2^k}<\frac{\varepsilon}{L}.
$$

Multiplicando por $L>0$ obtenemos

$$
\boxed{
\frac{L}{2^k}<\varepsilon.
}
$$

El argumento es enteramente finito: dada una tolerancia concreta, produce un entero concreto $k$ cuya existencia queda garantizada por arquimedianidad. No se ha escrito ni utilizado ninguna afirmación de límite.

**Dependencia estructural:** la elección de $m$ usa arquimedianidad; ésta fue derivada previamente de completitud, de modo que aquí la dependencia de completitud es indirecta.

[]{#MA-MSOL-ANM-01-003-057}

### 57. Señala por separado dónde intervienen completitud, arquimedianidad, encajamiento y estrechamiento en el argumento de bisección.

Las cuatro piezas cumplen funciones distintas.

**1. Encajamiento.** La construcción por bisección conserva una mitad de la etapa anterior, de modo que

$$
J_{k+1}\subseteq J_k.
$$

Junto con cierre y no vaciedad, esto prepara la aplicación del resultado de §3.5.

**2. Completitud.** En §3.5, para una familia cerrada, no vacía y encajada, la completitud produce un punto común mediante

$$
x=\sup\{a_k:k\ge0\}.
$$

Por tanto,

$$
\bigcap_k J_k\ne\varnothing.
$$

Éste es el componente de existencia.

**3. Arquimedianidad.** Dada $\varepsilon>0$, permite elegir un entero $m$ con

$$
m>\frac{L}{\varepsilon}.
$$

Combinada con $2^m\ge m+1$, produce un $k$ finito tal que

$$
\frac{L}{2^k}<\varepsilon.
$$

Así se verifica que la bisección puede hacerse arbitrariamente fina. Como la arquimedianidad fue derivada de completitud, ésta es una dependencia **indirecta**.

**4. Estrechamiento.** Una vez establecida

$$
\forall\varepsilon>0\;\exists k:
\operatorname{anch}(J_k)<\varepsilon,
$$

si dos puntos distintos sobrevivieran en todos los intervalos, su distancia positiva proporcionaría una tolerancia incompatible con algún ancho. Esto da unicidad.

La arquitectura completa es, por tanto,

$$
\boxed{
\begin{aligned}
\text{encajamiento + cierre}
&\Longrightarrow_{\text{completitud}}
\text{existencia},\\
\text{completitud}
&\Longrightarrow
\text{arquimedianidad}
\Longrightarrow
\text{bisección arbitrariamente fina},\\
\text{estrechamiento}
&\Longrightarrow
\text{unicidad}.
\end{aligned}
}
$$

No se usa convergencia como argumento en ninguna de estas tres cadenas.

## §3.7. Tres lenguajes para una recta sin huecos

[]{#MA-MSOL-ANM-01-003-058}

### 58. En la prueba `SUP ⇒ SEP`, ¿por qué la no vaciedad de $B$ permite demostrar que $A$ está acotado superiormente?

La no vaciedad de $B$ permite **elegir un testigo concreto** $b_0\in B$.

La hipótesis cruzada de separación dice

$$
a\le b
\qquad
\text{para todo }a\in A,\ b\in B.
$$

Como $b_0\in B$, podemos especializar el cuantificador universal en $b=b_0$. Entonces

$$
a\le b_0
\qquad
\text{para todo }a\in A.
$$

Ésta es exactamente la definición de que $b_0$ sea una cota superior de $A$. Por tanto,

$$
b_0\in U(A),
$$

y en particular

$$
U(A)\ne\varnothing.
$$

Así, la no vaciedad de $B$ no es decorativa: proporciona el elemento que certifica la acotación superior de $A$, una de las hipótesis necesarias para aplicar **SUP**.

**Uso de completitud:** ninguno todavía. Aquí sólo se verifica la hipótesis de acotación superior.

[]{#MA-MSOL-ANM-01-003-059}

### 59. Una vez definido $s=\sup A$, ¿por qué cada $b\in B$ debe satisfacer $s\le b$?

Sea $b\in B$ cualquiera.

Por la condición cruzada,

$$
a\le b
\qquad
\text{para todo }a\in A.
$$

Luego $b$ es una cota superior de $A$:

$$
b\in U(A).
$$

Como

$$
s=\sup A
$$

es la **menor** de todas las cotas superiores de $A$, debe cumplirse

$$
s\le b.
$$

Y como $b\in B$ era arbitrario,

$$
\boxed{s\le b\quad\text{para todo }b\in B.}
$$

Junto con $a\le s$ para todo $a\in A$, esto demuestra que $s$ separa ambas clases.

**Uso de completitud:** ninguno nuevo. La completitud ya se gastó al producir $s=\sup A$; este paso usa sólo la minimalidad del supremo.

[]{#MA-MSOL-ANM-01-003-060}

### 60. En la prueba `SEP ⇒ SUP`, ¿por qué un separador entre $A$ y $U(A)$ es automáticamente una cota superior de $A$?

En la prueba **SEP $\Rightarrow$ SUP** aplicamos separación a las dos clases

$$
A
\qquad\text{y}\qquad
U(A).
$$

El separador $c$ satisface

$$
a\le c\le u
\qquad
\text{para todo }a\in A,\ u\in U(A).
$$

La mitad izquierda de esta doble desigualdad es

$$
a\le c
\qquad
\forall a\in A.
$$

Pero ésa es exactamente la definición de cota superior. Por tanto,

$$
\boxed{c\in U(A).}
$$

No hace falta ninguna inferencia adicional: la propiedad de separación ya entrega universalmente que $c$ domina a todos los elementos de $A$.

**Uso de completitud:** si SEP se toma como principio en esta dirección, no se invoca SUP; se está reconstruyendo SUP a partir de SEP.

[]{#MA-MSOL-ANM-01-003-061}

### 61. ¿Qué parte de la desigualdad $a\le c\le u$ demuestra que $c$ es la **menor** cota superior?

La desigualdad

$$
a\le c\le u
\qquad
\forall a\in A,\ u\in U(A)
$$

contiene dos informaciones distintas.

La primera,

$$
a\le c
\qquad
\forall a\in A,
$$

demuestra que $c$ es una cota superior de $A$, es decir,

$$
c\in U(A).
$$

La segunda,

$$
c\le u
\qquad
\forall u\in U(A),
$$

afirma que $c$ está por debajo de **toda** cota superior de $A$.

Por tanto, entre los elementos de $U(A)$, $c$ es el menor:

$$
c=\min U(A).
$$

Y por la definición de supremo,

$$
\boxed{c=\sup A.}
$$

Así, la parte que demuestra la **minimalidad** es precisamente

$$
\boxed{c\le u\quad\forall u\in U(A).}
$$

[]{#MA-MSOL-ANM-01-003-062}

### 62. Formula con todos sus cuantificadores la condición cruzada de **GCI**.

Sea una familia no vacía de intervalos cerrados

$$
\bigl([a_i,b_i]\bigr)_{i\in I},
\qquad
I\ne\varnothing.
$$

La condición cruzada de **GCI** se escribe con todos sus cuantificadores como

$$
\boxed{
\forall i\in I\;\forall j\in I:
\quad a_i\le b_j.
}
$$

Es importante que los índices sean **independientes**: no se exige sólo

$$
a_i\le b_i,
$$

sino que cada extremo izquierdo $a_i$ quede a la izquierda de **cada** extremo derecho $b_j$, incluso cuando $i\ne j$.

Ésta es la compatibilidad global que permitirá encontrar un mismo real $c$ con

$$
a_i\le c\le b_i
\qquad
\forall i\in I.
$$

[]{#MA-MSOL-ANM-01-003-063}

### 63. ¿Por qué la condición cruzada implica que cada intervalo $[a_i,b_i]$ es no vacío?

La condición cruzada afirma

$$
\forall i,j\in I:
\quad a_i\le b_j.
$$

En particular podemos tomar

$$
j=i.
$$

Entonces, para cada $i\in I$,

$$
a_i\le b_i.
$$

Pero un intervalo cerrado

$$
[a_i,b_i]
$$

es no vacío exactamente cuando su extremo izquierdo no excede al derecho. De hecho,

$$
a_i\in[a_i,b_i]
$$

porque

$$
a_i\le a_i\le b_i.
$$

Por tanto,

$$
\boxed{[a_i,b_i]\ne\varnothing\quad\text{para todo }i\in I.}
$$

La no vaciedad individual de cada intervalo es así una consecuencia inmediata de la condición cruzada.

[]{#MA-MSOL-ANM-01-003-064}

### 64. En la prueba `SEP ⇒ GCI`, explica por qué separar los conjuntos de extremos izquierdos y derechos produce un punto perteneciente a **todos** los intervalos.

En la prueba **SEP $\Rightarrow$ GCI** formamos los conjuntos de extremos

$$
A_L=\{a_i:i\in I\},
\qquad
A_R=\{b_i:i\in I\}.
$$

La condición cruzada

$$
a_i\le b_j
\qquad
\forall i,j\in I
$$

dice exactamente que

$$
a\le b
\qquad
\forall a\in A_L,\ b\in A_R.
$$

Por **SEP** existe entonces un real $c$ tal que

$$
a\le c\le b
\qquad
\forall a\in A_L,\ b\in A_R.
$$

Ahora fijemos un índice $i\in I$. Como

$$
a_i\in A_L
\qquad\text{y}\qquad
b_i\in A_R,
$$

la propiedad del separador da

$$
a_i\le c\le b_i.
$$

Luego

$$
c\in[a_i,b_i].
$$

Como $i$ era arbitrario,

$$
\boxed{
c\in\bigcap_{i\in I}[a_i,b_i].
}
$$

La clave es que SEP controla simultáneamente **todos** los extremos izquierdos y **todos** los derechos; por eso el mismo $c$ pertenece a cada intervalo.

[]{#MA-MSOL-ANM-01-003-065}

### 65. En la prueba `GCI ⇒ SEP`, ¿por qué usamos la familia indexada por $A\times B$?

En **GCI $\Rightarrow$ SEP** partimos de dos conjuntos no vacíos $A,B\subseteq\mathbb R$ tales que

$$
a\le b
\qquad
\forall a\in A,\ b\in B.
$$

Queremos obtener un único $c$ que satisfaga simultáneamente

$$
a\le c
\qquad\forall a\in A
$$

y

$$
c\le b
\qquad\forall b\in B.
$$

Para codificar **todas** esas desigualdades en lenguaje intervalar necesitamos imponer la restricción

$$
c\in[a,b]
$$

para cada combinación posible de un extremo izquierdo $a\in A$ y un extremo derecho $b\in B$.

La colección natural de índices es, por tanto,

$$
A\times B.
$$

A cada par $(a,b)$ asociamos

$$
I_{(a,b)}=[a,b].
$$

Usar sólo algunos pares podría dejar fuera alguna de las restricciones universales. En cambio, indexar por el producto cartesiano conserva exactamente los dos cuantificadores:

$$
\boxed{
\forall a\in A\;\forall b\in B.
}
$$

Por eso $A\times B$ es la indexación correcta.

[]{#MA-MSOL-ANM-01-003-066}

### 66. Justifica cuidadosamente por qué un punto común a todos los intervalos $[a,b]$, con $(a,b)\in A\times B$, queda por encima de todo $A$ y por debajo de todo $B$.

Supongamos que

$$
c\in[a,b]
\qquad
\text{para todo }(a,b)\in A\times B.
$$

Debemos separar los dos cuantificadores.

Como $B\ne\varnothing$, fijemos un elemento

$$
b_0\in B.
$$

Sea ahora $a\in A$ arbitrario. Entonces

$$
(a,b_0)\in A\times B.
$$

Por la propiedad de $c$,

$$
c\in[a,b_0],
$$

y por tanto

$$
a\le c.
$$

Como $a$ era arbitrario,

$$
\boxed{a\le c\quad\forall a\in A.}
$$

Análogamente, como $A\ne\varnothing$, fijemos

$$
a_0\in A.
$$

Para cualquier $b\in B$,

$$
(a_0,b)\in A\times B,
$$

de modo que

$$
c\in[a_0,b]
$$

y, por tanto,

$$
c\le b.
$$

Como $b$ era arbitrario,

$$
\boxed{c\le b\quad\forall b\in B.}
$$

Juntando ambas conclusiones,

$$
\boxed{
a\le c\le b
\qquad
\forall a\in A,\ b\in B.
}
$$

Así el punto común es exactamente un separador.

[]{#MA-MSOL-ANM-01-003-067}

### 67. ¿Cómo recupera directamente **GCI** el supremo de un conjunto $A$ usando la familia $[a,u]$ con $u\in U(A)$?

Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente. Entonces

$$
U(A)\ne\varnothing.
$$

Consideremos la familia de intervalos

$$
[a,u],
\qquad
(a,u)\in A\times U(A).
$$

La familia es no vacía porque ambos factores lo son.

Verifiquemos la condición cruzada de **GCI**. Tomemos dos índices

$$
(a,u),\ (a',u')\in A\times U(A).
$$

Como $u'\in U(A)$, el número $u'$ es cota superior de $A$. En particular, como $a\in A$,

$$
a\le u'.
$$

Por GCI existe un punto común $c$ a todos los intervalos:

$$
c\in[a,u]
\qquad
\forall(a,u)\in A\times U(A).
$$

De aquí obtenemos las dos propiedades del supremo.

Fijando cualquier $u_0\in U(A)$, para todo $a\in A$,

$$
c\in[a,u_0]
\Longrightarrow
a\le c.
$$

Luego $c$ es cota superior de $A$.

Fijando cualquier $a_0\in A$, para todo $u\in U(A)$,

$$
c\in[a_0,u]
\Longrightarrow
c\le u.
$$

Así $c$ es menor o igual que toda cota superior.

Por tanto,

$$
\boxed{c=\sup A.}
$$

Esto muestra directamente

$$
\boxed{\mathrm{GCI}\Longrightarrow\mathrm{SUP}.}
$$

[]{#MA-MSOL-ANM-01-003-068}

### 68. ¿Por qué el caso numerable encajado de §3.5 satisface la condición cruzada?

En §3.5, para una familia cerrada y encajada

$$
I_n=[a_n,b_n],
\qquad
I_{n+1}\subseteq I_n,
$$

se demostró que los extremos satisfacen

$$
a_m\le b_n
\qquad
\text{para todos }m,n\in\mathbb N_{>0}.
$$

Ésta es exactamente la condición cruzada de **GCI** para la familia indexada por

$$
I=\mathbb N_{>0}:
$$

$$
\forall m\in\mathbb N_{>0}\;
\forall n\in\mathbb N_{>0}:
\quad a_m\le b_n.
$$

Por tanto toda familia numerable de intervalos cerrados no vacíos y encajados considerada en §3.5 es un caso particular de las familias admitidas por GCI.

De ahí,

$$
\boxed{
\mathrm{GCI}
\Longrightarrow
\bigcap_{n=1}^{\infty}[a_n,b_n]\ne\varnothing.
}
$$

[]{#MA-MSOL-ANM-01-003-069}

### 69. ¿Por qué en este libro escribimos `GCI ⇒ caso numerable encajado` y no cerramos automáticamente una equivalencia en sentido inverso?

Porque lo demostrado en esta arquitectura es una implicación **desde la formulación general hacia un caso particular**:

$$
\mathrm{GCI}
\Longrightarrow
\mathrm{NESTED\_INTERVALS}_{\mathbb N}.
$$

La razón es que una familia numerable encajada satisface la condición cruzada y, por tanto, entra en GCI.

Pero de que una propiedad valga para una clase particular de familias —las numerables y encajadas— no se sigue automáticamente que permita resolver el caso general de familias arbitrariamente indexadas y sólo cruzadamente compatibles.

Para escribir una equivalencia inversa habría que demostrar explícitamente

$$
\mathrm{NESTED\_INTERVALS}_{\mathbb N}
\Longrightarrow
\mathrm{GCI},
$$

con las hipótesis exactas necesarias. Esa demostración no se ha establecido como parte de la arquitectura de C03.

Por eso el libro conserva la afirmación lógicamente justificada:

$$
\boxed{
\mathrm{GCI}
\Longrightarrow
\text{caso numerable encajado},
}
$$

y evita convertir “caso particular” en “formulación equivalente” por mera semejanza verbal.

[]{#MA-MSOL-ANM-01-003-070}

### 70. Explica por qué el estrechamiento arbitrario pertenece a la capa de unicidad y no a la equivalencia básica `SUP ⇔ INF ⇔ SEP ⇔ GCI`.

La cadena básica de equivalencias trata de **existencia estructural**:

$$
\mathrm{SUP}
\Longleftrightarrow
\mathrm{INF}
\Longleftrightarrow
\mathrm{SEP}
\Longleftrightarrow
\mathrm{GCI}.
$$

Cada una de esas formulaciones garantiza, en un lenguaje distinto, la existencia de un objeto requerido: una barrera extremal, un separador o un punto común.

El estrechamiento arbitrario,

$$
\forall\varepsilon>0\;\exists n:
\quad b_n-a_n<\varepsilon,
$$

cumple otra función. Si dos puntos distintos $x,y$ pertenecieran a todos los intervalos, entonces

$$
\delta=|x-y|>0
$$

sería una tolerancia legítima. El estrechamiento produciría un intervalo con ancho menor que $\delta$, contradiciendo que contenga a ambos.

Por tanto,

$$
\boxed{
\text{estrechamiento arbitrario}
\Longrightarrow
\text{unicidad},
}
$$

no existencia.

La existencia del punto proviene de la infraestructura de completitud; el estrechamiento elimina la posibilidad de que sobrevivan dos puntos diferentes. Por eso pertenece a una capa adicional y no constituye, sin más, una quinta formulación equivalente.

[]{#MA-MSOL-ANM-01-003-071}

### 71. Para $S_2\subseteq\mathbb Q$, demuestra que un separador racional entre $S_2$ y sus cotas superiores racionales sería necesariamente $\sup_{\mathbb Q}S_2$.

Sea

$$
S_2\subseteq\mathbb Q
$$

y sea

$$
U_{\mathbb Q}(S_2)
$$

el conjunto de sus cotas superiores racionales.

Supongamos que existiera un separador racional

$$
c\in\mathbb Q
$$

tal que

$$
a\le c\le u
\qquad
\forall a\in S_2,\ 
\forall u\in U_{\mathbb Q}(S_2).
$$

La mitad izquierda,

$$
a\le c
\qquad
\forall a\in S_2,
$$

dice que $c$ es una cota superior racional de $S_2$. Por tanto,

$$
c\in U_{\mathbb Q}(S_2).
$$

La mitad derecha,

$$
c\le u
\qquad
\forall u\in U_{\mathbb Q}(S_2),
$$

dice que $c$ es menor o igual que toda cota superior racional.

Así,

$$
c=\min U_{\mathbb Q}(S_2),
$$

es decir,

$$
\boxed{c=\sup_{\mathbb Q}S_2.}
$$

Pero §3.1 estableció que ese supremo racional no existe. Por contradicción, tampoco puede existir tal separador racional.

Así se traduce exactamente el fallo de SUP al lenguaje SEP.

[]{#MA-MSOL-ANM-01-003-072}

### 72. Explica cómo el mismo fallo de $\mathbb Q$ puede leerse como ausencia de supremo, ausencia de separador y fallo de una intersección general de intervalos cerrados racionales.

El mismo defecto estructural de $\mathbb Q$ puede describirse en tres vocabularios.

**1. Lenguaje de supremos.**

Para

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\},
$$

sabemos que $S_2\ne\varnothing$ y que está acotado superiormente en $\mathbb Q$, pero

$$
\boxed{\sup_{\mathbb Q}S_2\text{ no existe}.}
$$

Éste es el fallo de **SUP**.

**2. Lenguaje de separación.**

Tomemos

$$
A=S_2,
\qquad
B=U_{\mathbb Q}(S_2).
$$

Ambos son no vacíos y

$$
a\le b
\qquad
\forall a\in A,\ b\in B.
$$

Si existiera un separador racional $c$, el microcontrol anterior demuestra que necesariamente

$$
c=\sup_{\mathbb Q}S_2,
$$

lo cual es imposible. Por tanto,

$$
\boxed{\text{no existe separador racional para }A\text{ y }B.}
$$

Éste es el fallo de **SEP**.

**3. Lenguaje intervalar.**

Para cada

$$
(a,b)\in A\times B
$$

consideremos el intervalo cerrado racional

$$
[a,b]_{\mathbb Q}
=
\{q\in\mathbb Q:a\le q\le b\}.
$$

La familia satisface la condición cruzada. Si existiera

$$
c\in\bigcap_{(a,b)\in A\times B}[a,b]_{\mathbb Q},
$$

entonces $c$ estaría por encima de todo $A$ y por debajo de todo $B$. Sería, por tanto, un separador racional y finalmente el supremo racional inexistente.

Luego

$$
\boxed{
\bigcap_{(a,b)\in A\times B}[a,b]_{\mathbb Q}
=\varnothing.
}
$$

Éste es el fallo de **GCI**.

Por tanto, no son tres defectos independientes:

$$
\boxed{
\text{sin supremo racional}
\Longleftrightarrow
\text{sin separador racional}
\Longleftrightarrow
\text{falla la intersección general racional}.
}
$$

La densidad de $\mathbb Q$ no corrige ninguno de estos fallos; lo que falta es la garantía de existencia de la frontera compatible exigida.

## §3.8. Dónde se gasta la completitud

[]{#MA-MSOL-ANM-01-003-073}

### 73. Da un ejemplo de una afirmación sobre supremos que use sólo la **definición** y no la garantía general de existencia.

Un ejemplo es la afirmación siguiente:

> Si $s=\sup A$ y $u$ es una cota superior de $A$, entonces $s\le u$.

Aquí partimos de la hipótesis de que el supremo **ya existe** y vale $s$. Por definición, ser supremo significa precisamente dos cosas:

1. $s$ es cota superior de $A$;
2. $s$ es menor o igual que toda cota superior de $A$.

Así, si

$$
u\in U(A),
$$

la segunda cláusula da inmediatamente

$$
\boxed{s\le u.}
$$

No hemos usado el principio del supremo para producir $s$. Sólo hemos explotado la propiedad definitoria de un objeto cuya existencia estaba ya supuesta.

Por tanto,

$$
\boxed{
 s=\sup A\text{ existe}
 \Longrightarrow
 s\le u\quad\forall u\in U(A)
}
$$

es una afirmación de **Nivel 1: orden y definición**, no un nuevo gasto de completitud.

[]{#MA-MSOL-ANM-01-003-074}

### 74. En la prueba de existencia del ínfimo, ¿dónde se encuentra exactamente el uso heredado del principio del supremo?

Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente.

Primero, por reflexión, se demuestra sin completitud que

$$
-A\ne\varnothing
$$

y que $-A$ está acotado superiormente. Si $l$ es una cota inferior de $A$, entonces

$$
l\le a\quad\forall a\in A
$$

implica

$$
-a\le -l\quad\forall a\in A,
$$

de modo que $-l$ es cota superior de $-A$.

El uso heredado del principio del supremo aparece exactamente en la línea

$$
\boxed{
-A\ne\varnothing,
\quad
-A\text{ acotado superiormente}
\Longrightarrow_{\mathrm{SUP}}
\exists s=\sup(-A).
}
$$

Después se define

$$
i=-s
$$

y se demuestra mediante orden y reflexión que $i$ es la mayor cota inferior de $A$.

Por tanto,

$$
\boxed{
\text{el gasto de completitud está en la existencia de }\sup(-A),
}
$$

no en las inversiones posteriores de desigualdad ni en la definición $i=-s$.

[]{#MA-MSOL-ANM-01-003-075}

### 75. En la prueba de arquimedianidad, separa el único paso que usa completitud de los pasos puramente aritméticos.

La prueba comienza suponiendo, para obtener una contradicción, que

$$
\mathbb N
$$

está acotado superiormente.

Como además $\mathbb N\ne\varnothing$, aparece el único paso de completitud:

$$
\boxed{
\mathbb N\text{ acotado superiormente}
\Longrightarrow_{\text{completitud}}
\exists s=\sup\mathbb N.
}
$$

A partir de ahí no se vuelve a invocar completitud.

Los pasos restantes son de orden y aritmética:

1. Como $s-1<s$, el número $s-1$ no puede ser cota superior de $\mathbb N$, pues $s$ es la menor cota superior.
2. Negar que $s-1$ sea cota superior produce
   $$
   \exists n\in\mathbb N:\quad n>s-1.
   $$
3. Sumando $1$ a ambos lados,
   $$
   n+1>s.
   $$
4. Por clausura de $\mathbb N$ bajo sucesor,
   $$
   n+1\in\mathbb N.
   $$
5. Esto contradice que $s$ sea cota superior de todos los naturales.

La anatomía completa queda

$$
\boxed{
\text{completitud: }\exists\sup\mathbb N
\quad+
\quad
\text{orden y aritmética: contradicción}.
}
$$

[]{#MA-MSOL-ANM-01-003-076}

### 76. ¿Por qué usar después la afirmación $1/n<\varepsilon$ puede constituir un uso **indirecto** de completitud?

La afirmación pertinente es

$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}:
\frac1n<\varepsilon.
$$

Cuando la usamos en una prueba posterior, normalmente no escribimos de nuevo «por el principio del supremo». Elegimos simplemente un natural $n$ suficientemente grande.

Sin embargo, en este capítulo esa posibilidad fue demostrada a partir de la propiedad arquimediana, y la propiedad arquimediana fue obtenida usando completitud en la existencia hipotética de

$$
\sup\mathbb N.
$$

Por tanto la cadena de dependencia es

$$
\boxed{
\text{completitud}
\Longrightarrow
\text{arquimedianidad}
\Longrightarrow
\forall\varepsilon>0\;\exists n:\frac1n<\varepsilon.
}
$$

Así, una prueba que invoque sólo el último eslabón puede no tener un **uso directo** del principio del supremo, pero sí un uso **indirecto o heredado** de completitud.

Eso es precisamente lo que significa encapsular una dependencia en un teorema previo.

[]{#MA-MSOL-ANM-01-003-077}

### 77. En el teorema de intervalos cerrados encajados, identifica las líneas de orden y la línea exacta de existencia proporcionada por completitud.

Sea

$$
I_n=[a_n,b_n]
$$

una familia de intervalos cerrados no vacíos y encajados.

Las primeras líneas son puramente de orden. Del encajamiento se obtiene la monotonía de los extremos y, en particular, la compatibilidad cruzada

$$
\boxed{a_m\le b_n\qquad\forall m,n.}
$$

Luego se forma

$$
A=\{a_n:n\ge1\}.
$$

También por razones elementales:

- $A\ne\varnothing$;
- para cada $n$, el número $b_n$ es una cota superior de $A$, porque $a_m\le b_n$ para todo $m$.

Sólo entonces aparece la línea de existencia proporcionada por completitud:

$$
\boxed{
A\ne\varnothing,
\quad
A\text{ acotado superiormente}
\Longrightarrow_{\text{completitud}}
\exists x=\sup A.
}
$$

Una vez que $x$ existe, vuelven los pasos de orden:

$$
a_n\le x
$$

porque $x$ es cota superior de $A$, y

$$
x\le b_n
$$

porque cada $b_n$ es una cota superior de $A$ y $x$ es la menor.

Así,

$$
a_n\le x\le b_n,
$$

por lo que

$$
x\in I_n
\qquad\forall n.
$$

La completitud se gasta exactamente una vez: en producir $x=\sup A$.

[]{#MA-MSOL-ANM-01-003-078}

### 78. ¿Por qué la unicidad por estrechamiento no necesita otra aplicación del principio del supremo?

Supongamos que ya existen dos puntos

$$
x,y\in\bigcap_n I_n
$$

y que la familia satisface

$$
\forall\varepsilon>0\;\exists n:
 b_n-a_n<\varepsilon.
$$

Para demostrar unicidad razonamos por contradicción. Si $x\ne y$, entonces

$$
\delta=|x-y|>0.
$$

Por estrechamiento existe un índice $n$ tal que

$$
b_n-a_n<\delta.
$$

Como $x,y\in I_n=[a_n,b_n]$, ambos están contenidos en el mismo intervalo y por tanto

$$
|x-y|\le b_n-a_n.
$$

Combinando,

$$
|x-y|
\le b_n-a_n
<\delta
=|x-y|,
$$

contradicción.

Toda esta prueba usa únicamente:

- la existencia ya disponible de $x$ e $y$;
- el orden dentro de un intervalo;
- la distancia $|x-y|$;
- la hipótesis cuantificada de estrechamiento.

No se construye ningún nuevo supremo. Por eso

$$
\boxed{
\text{estrechamiento}\Longrightarrow\text{unicidad}
}
$$

no consume completitud de forma directa.

[]{#MA-MSOL-ANM-01-003-079}

### 79. Explica cómo una sola prueba puede contener a la vez una dependencia directa, una dependencia indirecta y pasos puramente elementales.

La construcción por bisección de §3.6 proporciona un ejemplo completo.

**Dependencia directa.** Para una familia cerrada y encajada, la existencia de un punto común procede del teorema de §3.5. Si abrimos su demostración, aparece

$$
x=\sup\{a_n:n\ge1\},
$$

y esa existencia usa directamente completitud.

**Dependencia indirecta.** Para demostrar que la bisección alcanza un ancho menor que cualquier $\varepsilon>0$, usamos la propiedad arquimediana, ya derivada de completitud. Con ancho inicial $L$ obtenemos un $k$ tal que

$$
\frac{L}{2^k}<\varepsilon.
$$

Aquí no se invoca SUP de nuevo, pero la dependencia está heredada a través de arquimedianidad.

**Pasos elementales.** Entre ambos aparecen hechos que sólo usan orden y álgebra, por ejemplo:

$$
\operatorname{anch}(J_k)=\frac{L}{2^k},
$$

la inclusión encajada de los intervalos y la desigualdad

$$
|x-y|\le \operatorname{anch}(J_k)
$$

para dos puntos del mismo intervalo.

Por tanto, dentro de una sola prueba puede aparecer el esquema

$$
\boxed{
\text{uso directo}
+
\text{uso indirecto}
+
\text{pasos elementales}.
}
$$

Clasificar la demostración completa con una única etiqueta ocultaría esta estructura interna.

[]{#MA-MSOL-ANM-01-003-080}

### 80. ¿Por qué `SUP`, `INF`, `SEP` y `GCI` deben entenderse como interfaces equivalentes y no como cuatro axiomas acumulativos?

Porque en §3.3 y §3.7 se demostraron implicaciones suficientes para obtener

$$
\boxed{
\mathrm{SUP}
\Longleftrightarrow
\mathrm{INF}
\Longleftrightarrow
\mathrm{SEP}
\Longleftrightarrow
\mathrm{GCI}.
}
$$

Una equivalencia lógica significa que cualquiera de esas formulaciones permite recuperar las demás.

En la arquitectura adoptada aquí se escogió **SUP** como punto de partida. Entonces:

- **INF** se obtiene por reflexión;
- **SEP** se obtiene usando el supremo de la clase izquierda;
- **GCI** se obtiene a partir de separación de los extremos izquierdos y derechos.

Las conversas muestran que no hemos perdido información al cambiar de lenguaje.

Por eso no debemos leer la cadena como

$$
\text{SUP} + \text{INF} + \text{SEP} + \text{GCI}
$$

ni añadir cuatro hipótesis independientes a una prueba.

La lectura correcta es

$$
\boxed{
\text{una misma infraestructura de completitud}
\longleftrightarrow
\text{cuatro interfaces equivalentes}.
}
$$

Una prueba futura puede elegir la interfaz más natural para su problema sin multiplicar los supuestos estructurales.

[]{#MA-MSOL-ANM-01-003-081}

### 81. ¿Qué propiedades relevantes conserva $\mathbb Q$ y qué garantía de existencia general le falta?

El contraste del capítulo muestra que $\mathbb Q$ conserva mucha estructura relevante.

Dentro de $\mathbb Q$ podemos:

- usar las operaciones de campo;
- trabajar con un orden total compatible con esas operaciones;
- comparar números y desigualdades;
- definir cotas superiores e inferiores;
- definir qué significaría ser supremo o ínfimo;
- demostrar unicidad de esos extremos **si existen**;
- reflejar desigualdades;
- trabajar con intervalos racionales;
- usar densidad;
- usar la propiedad arquimediana.

Lo que falta es la garantía general

$$
A\ne\varnothing,
\quad
A\subseteq\mathbb Q,
\quad
A\text{ acotado superiormente en }\mathbb Q
\Longrightarrow
\exists\sup_{\mathbb Q}A.
$$

Esta implicación es falsa en general. El conjunto

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}
$$

es el ejemplo de control: es no vacío y está acotado superiormente en $\mathbb Q$, pero no tiene supremo racional.

Así,

$$
\boxed{
\mathbb Q\text{ conserva orden, densidad y arquimedianidad,}
\quad
\text{pero carece de completitud de orden.}
}
$$

Por equivalencia, también pueden fallar allí las garantías generales SEP y GCI.

[]{#MA-MSOL-ANM-01-003-082}

### 82. ¿Por qué el hecho de que $\mathbb Q$ sea denso no repara su falta de completitud?

La densidad responde a una pregunta local:

$$
p<q,
\quad p,q\in\mathbb Q
\Longrightarrow
\exists r\in\mathbb Q:
 p<r<q.
$$

Es decir, dados **dos puntos ya existentes**, podemos insertar otro racional entre ellos.

La completitud responde a una pregunta diferente: dada una familia global de restricciones compatibles, ¿existe dentro del sistema la frontera extremal o el separador requerido?

El conjunto $S_2$ muestra que ambas propiedades son independientes en este sentido. Aunque $\mathbb Q$ es denso, la familia de sus cotas superiores racionales para $S_2$ no posee mínimo racional.

Por tanto,

$$
\boxed{
\text{tener puntos intermedios}
\not\Rightarrow
\text{tener la frontera extremal exigida}.
}
$$

La densidad permite refinar entre racionales existentes, pero no crea el objeto que falta cuando una familia completa de restricciones exige una menor cota superior no racional.

[]{#MA-MSOL-ANM-01-003-083}

### 83. Distingue el papel futuro de C07, C10 y C23 respecto de C03 sin demostrar todavía ninguno de sus resultados.

Los tres capítulos consumirán la infraestructura de C03 de maneras distintas, pero ninguno de sus resultados debe considerarse demostrado aquí.

**C07 — sucesiones monótonas acotadas.**

C03 entrega la garantía de existencia de barreras extremales. Cuando C07 estudie una sucesión monótona y acotada, podrá aplicar esa infraestructura al conjunto de valores para obtener un candidato extremal. La demostración de que ese candidato es efectivamente el límite pertenece a C07 y no se adelanta aquí.

**C10 — Cauchy y convergencia en $\mathbb R$.**

C03 trabaja con completitud de orden. C10 introducirá una formulación expresada mediante sucesiones de Cauchy y convergencia. Su tarea será comparar o relacionar esa nueva noción con la infraestructura de orden ya disponible; no se identifican ambas por definición en C03.

**C23 — supremos, ínfimos y Darboux.**

Las construcciones inferiores y superiores de Darboux necesitarán usar supremos e ínfimos de manera sistemática. C03 proporciona la garantía de existencia que impide que esas construcciones queden en un nivel meramente condicional. La teoría de integración y sus demostraciones pertenecen a C23.

Así, los papeles pueden resumirse como

$$
\boxed{
\begin{array}{ll}
\text{C07:} & \text{consumir una barrera extremal como candidato futuro},\\
\text{C10:} & \text{comparar/reformular nociones de completitud},\\
\text{C23:} & \text{consumir supremos e ínfimos en construcciones de integración}.
\end{array}
}
$$

Éste es sólo un mapa de dependencias futuras, no una demostración anticipada de esos capítulos.

[]{#MA-MSOL-ANM-01-003-084}

### 84. Formula con tus propias palabras la idea de «recta sin huecos» sin usar como definición ni «recta continua» ni «tener muchísimos puntos».

Una formulación compatible con lo demostrado en C03 es ésta:

> La recta real es «sin huecos» en el sentido relevante para este capítulo porque ciertas familias compatibles de restricciones de orden no obligan a salir de $\mathbb R$ para encontrar el objeto que esas restricciones requieren.

Ese objeto puede aparecer bajo distintos lenguajes:

- como una mejor barrera superior o inferior;
- como un separador entre dos clases globalmente ordenadas;
- como un punto común a una familia compatible de intervalos cerrados.

Por eso la idea puede condensarse en

$$
\boxed{
\text{restricciones compatibles}
\Longrightarrow_{\text{completitud}}
\text{objeto requerido dentro de }\mathbb R.
}
$$

Esta formulación no depende de imaginar una línea dibujada ni de contar cuántos puntos hay entre dos reales. De hecho, $\mathbb Q$ es denso y contiene infinitos racionales entre racionales distintos, pero sigue fallando la garantía general de existencia.

La síntesis conceptual de C03 es, por tanto:

$$
\boxed{\text{la completitud es infraestructura de existencia}.}
$$
