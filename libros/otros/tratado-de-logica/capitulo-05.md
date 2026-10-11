---
title: Capítulo 5 — Signaturas, términos y fórmulas
status: published
draft: false
book-id: MA-BOK-0014
editorial-project: TLOG
date-modified: '2026-10-11'
license: GFDL-1.3-or-later
areas:
- fundamentos
level: avanzado
topics:
- logica
number-sections: false
content-id: MA-BCH-0207
content-type: book-chapter
source-id: TLOG-CH05-0001
prerequisites:
- MA-BCH-0202
- MA-BCH-0203
related:
- MA-BOK-0014
source-sha256: e5adfe753afb36c575ac53c145ff652ec6b6dfb7cf398cc38c1d597afb5154c8
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 4](capitulo-04.md) · [Capítulo 6 →](capitulo-06.md)

## 5.0. Objeto y frontera del capítulo

La Parte I ha construido una lógica proposicional clásica en la que sintaxis, semántica y prueba formal constituyen objetos distintos. Su coincidencia extensional está demostrada para el sistema específico `CPL/HCPL`. La Parte II introduce una clase de lenguajes con variables individuales, símbolos relacionales, símbolos funcionales y cuantificadores. **No se transporta automáticamente la semántica proposicional ni su teorema de completitud a estos lenguajes.**

El Capítulo 5 debe dar una gramática de expresiones y fórmulas de primer orden con igualdad lógica. El microtramo `TLOG-CH05-M01` termina en las fórmulas atómicas: fija el tipo de las signaturas, los constructores de términos, su legibilidad única y su inducción estructural. La formación de fórmulas compuestas y cuantificadas queda para `M02`. Variables libres/ligadas, sustitución, captura y recursión sobre fórmulas se tratarán en el Capítulo 6. Interpretaciones en estructuras y satisfacción sólo empiezan después, en los capítulos 7–8.

### Fuentes cotejadas para este bloque

- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001), cap. 2, §2.1, pp. 67–76: convenciones de lenguaje, símbolos de función y relación, términos y fórmulas atómicas. `proof-model / countercheck`.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010), cap. 2, §§2.1–2.2, pp. 43–44 y 54–57: signatura extralógica, variables, formación e inducción sobre términos, igualdad lógica. `countercheck`.

Las diferencias de firma y abreviaturas se registran en el maestro de procedencia: el presente tratado usa cinco conectivas y ambos cuantificadores como símbolos **primitivos**. La gramática se reconstruye para esa decisión y para una signatura unisortada arbitraria.

## 5.1. Familia de lenguajes de primer orden con igualdad

### Convención 5.1.1 — Lenguajes de primer orden de referencia {#tlog-cnv-00007}

Trabajamos en la metateoría externa `\mathsf M_{\mathrm{ext}}` y llamamos `\mathrm{FOL}_{=}` a la **familia** de lenguajes de primer orden clásicos, unisortados, parametrizados por una signatura extralógica `\tau` y dotados de un símbolo lógico de igualdad. Esta convención no nombra todavía un cálculo deductivo ni una semántica ya construida.

Se fijan, como símbolos lógicos primitivos para las futuras fórmulas, `\neg,\land,\lor,\to,\leftrightarrow,\forall,\exists,=`. Los cuantificadores `\forall` y `\exists` son ambos primitivos; las convenciones sobre su alcance requieren la formación de fórmulas, pendiente. El símbolo `=` de la gramática es un **token lógico del lenguaje objeto**, no el signo de igualdad usado en la metateoría entre sus expresiones. No habrá cuantificadores sobre subconjuntos ni variables de predicado de segundo orden.

El término *clásico* fija la familia de razonamientos pretendida, pero **no** declara corrección/completitud de ningún cálculo de primer orden; esos metateoremas tienen capítulos propios.

## 5.2. Signaturas y aridades

### Definición 5.2.1 — Signatura unisortada {#tlog-def-00022}

Una **signatura de primer orden** es una familia ordenada de conjuntos

$$
\tau:=\bigl((F_n)_{n\in\omega},(R_n)_{n\in\omega}\bigr),
$$

cuyos miembros son conjuntos de **tokens** extralógicos, con la condición de que las clases de símbolos `F_n` y `R_m` sean mutuamente disjuntas para todos los índices, incluidos dos índices distintos dentro de una misma familia. Cada `f\in F_n` es un símbolo **funcional** de aridad exactamente `n`; cada `R\in R_n` es un símbolo **relacional** de aridad exactamente `n`. Todas las aridades son números naturales finitos. No se impone que `\tau` sea finita, numerable o no vacía.

Los elementos de `F_0` son las **constantes**, consideradas como símbolos funcionales nularios. Se permiten `R_0`: designan símbolos relacionales nularios y darán lugar a fórmulas atómicas sin términos argumentos. Que existan predicados nularios no convierte a la signatura en un lenguaje de segundo orden. Los nombres de símbolos son tokens diferenciados de su tipografía visible; si se reusa una letra impresa, la identificación exacta se decide por su etiqueta de símbolo y aridad.

**Igualdad lógica:** `=` no pertenece a ninguno de los conjuntos `R_n`. Tampoco se define como relación extralógica arbitraria. Su interpretación como identidad en las estructuras correspondientes será obligación del Capítulo 7.

La elección de signatura es un parámetro de **sintaxis**. No está asociada aquí a dominio, funciones concretas ni relaciones interpretadas.

## 5.3. Variables y alfabeto

### Definición 5.3.1 — Alfabeto de `\tau` y variables individuales {#tlog-def-00023}

Fijamos un conjunto numerable de **variables individuales**

$$
X:=\{x_i:i\in\omega\},
$$

formado por tokens distintos entre sí, disjuntos de los símbolos lógicos y separadores. Las categorías de variable, función y relación se codifican mediante etiquetas diferenciadas de token; por ello, incluso si dos nombres impresos coinciden, sus tokens formales son disjuntos. En las cláusulas de formación identificaremos el token `x_i` con la secuencia unitaria que lo contiene; esto no identifica las categorías de token entre sí. Los nombres `x,y,z` sirven como metavariables que recorren `X` cuando no importan sus índices. Las variables `p_n` de `CPL` no se identifican con estas variables individuales.

El alfabeto de la signatura `\tau` será

$$
\Sigma_\tau := X\;\sqcup\;\bigcup_{n\in\omega}F_n
\;\sqcup\;\bigcup_{n\in\omega}R_n
\;\sqcup\;\{\neg,\land,\lor,\to,\leftrightarrow,
\forall,\exists,=,\mathtt{(},\mathtt{)},\mathtt{,}\}.
$$

El signo `\sqcup` indica unión **disjunta por categorías de token**. En particular, los paréntesis y las comas son separadores sintácticos, no símbolos funcionales. Por [TLOG-DEF-00002](capitulo-00.md#tlog-def-00002), las expresiones sobre `\Sigma_\tau` son secuencias **finitas** de tokens. La presentación tipográfica de los índices de `x_i` es metanotación de un token individual, no una secuencia infinita ni una cadena decimal implícita.

Una expresión sobre `\Sigma_\tau` no es automáticamente un término ni una fórmula. Esas clases se seleccionan mediante reglas explícitas de formación. La igualdad metalingüística entre dos cadenas se seguirá escribiendo `=` en texto matemático externo y **no** constituye, por ello, una fórmula objeto.

## 5.4. Términos

### Definición 5.4.1 — Términos de signatura `\tau` {#tlog-def-00024}

El conjunto `\operatorname{Tm}_\tau` de **términos de `\tau`** es el menor subconjunto de `\Sigma_\tau^{<\omega}` cerrado bajo estas cláusulas:

1. **Variable.** Para cada `x\in X`, la expresión de un solo token `x` es un término.
2. **Aplicación funcional.** Para cada `n\in\omega`, `f\in F_n` y `t_1,\ldots,t_n\in\operatorname{Tm}_\tau`, se forma el término
   $$
   \operatorname{App}_f(t_1,\ldots,t_n),
   $$
   cuya escritura canónica es `f(t_1,\ldots,t_n)` con **paréntesis y comas de nivel externo**. Si `n=0`, la cláusula da la constante `f()`; se autoriza escribir el token `f` a solas **como abreviación editorial**, pero `f()` es su serialización canónica.

Sólo las aplicaciones finitas de estas reglas forman términos. Los símbolos relacionales, conectivas, cuantificadores y la igualdad lógica no son constructores de términos.

Para precisar *menor* sin circularidad, definimos en `\mathsf M_{\mathrm{ext}}` la sucesión de etapas

$$
T_0:=X\cup\{f():f\in F_0\},
$$
$$
T_{k+1}:=T_k\cup
\bigcup_{n\ge 1}\{f(t_1,\ldots,t_n):f\in F_n,\ (t_1,\ldots,t_n)\in T_k^n\},
$$
$$
\operatorname{Tm}_\tau:=\bigcup_{k<\omega}T_k.
$$

La formación se efectúa sobre conjuntos: cada `T_k` es un conjunto y cada paso utiliza productos **finitos**, uniones indexadas por `\omega` y separación/reemplazo en `ZF`. No se introduce elección. La unión satisface las dos cláusulas, y todo conjunto de expresiones que las satisfaga contiene cada `T_k` por inducción; de ahí la minimalidad. La secuencia de etapas proporciona una medida bien fundada de **altura de construcción** para la inducción del §5.6, sin prejuzgar un teorema general de recursión sobre términos (Capítulo 6).

> [!important] Restricción tipada
> `f(t_1,\ldots,t_m)` sólo es término cuando el símbolo `f` tiene exactamente aridad `m` y cada argumento es término. Por ejemplo, si `f\in F_2`, las expresiones `f(x_0)` y `f(x_0,x_1,x_2)` no son términos.

## 5.5. Legibilidad única de términos

### Lema 5.5.1 — Unicidad de la descomposición inmediata {#tlog-lem-00009}

Todo término `t` pertenece a **exactamente una** de estas dos clases: (i) una variable `x_i`; (ii) una expresión de la forma `f(t_1,\ldots,t_n)` para un único símbolo `f\in F_n` y una única `n`-tupla de términos `(t_1,\ldots,t_n)`. Más precisamente,

$$
\operatorname{App}_{f}(t_1,\ldots,t_n)
=
\operatorname{App}_{g}(s_1,\ldots,s_m)
\Longrightarrow
n=m,\ f=g,\ t_i=s_i\quad(1\le i\le n).
$$

La igualdad de esta fórmula está en la **metateoría** entre términos como expresiones; no es una fórmula atómica.

#### Demostración

Por disjunción de tokens de [TLOG-DEF-00023](#tlog-def-00023), una cadena formada por una sola variable no puede comenzar con un símbolo funcional ni coincidir con `f(...)`. Si una cadena empieza con `f`, el token inicial identifica un único `f\in F_n` y su aridad `n` por [TLOG-DEF-00022](#tlog-def-00022). La serialización canónica delimita los argumentos por paréntesis; para recuperarlos, recorremos la cadena finita desde el paréntesis externo y marcamos únicamente las comas que aparecen a **profundidad de paréntesis uno** respecto de ese paréntesis. Una coma interna a un subargumento está a profundidad mayor y no lo separa. Así, los separadores externos determinan una única partición ordenada en `n` segmentos. Cada segmento es un término menor, y la comparación token a token de dos serializaciones iguales obliga a la coincidencia de los segmentos correspondientes. El caso `n=0` tiene una única lista vacía. No hay otra descomposición inmediata. `\square`

Este lema justifica que `\operatorname{App}_f` sea un constructor libre y que las operaciones posteriores puedan consultar los subárboles inmediatos sin ambigüedad. **No** demuestra todavía legibilidad única de fórmulas con cuantificadores: será otro problema.

## 5.6. Inducción estructural sobre términos

### Metateorema 5.6.1 — Principio de inducción de términos {#tlog-mth-00014}

Sea `P(t)` una propiedad metateórica de términos de `\tau` que satisface:

1. Para toda variable `x\in X`, vale `P(x)`.
2. Para todo `n\in\omega`, `f\in F_n` y términos `t_1,\ldots,t_n`, si valen `P(t_1),\ldots,P(t_n)`, entonces vale `P(f(t_1,\ldots,t_n))`. Para `n=0`, la condición antecedente es vacía; de aquí se exige `P(f())` para cada constante.

Entonces

$$
(\forall t\in\operatorname{Tm}_\tau)\;P(t).
$$

#### Demostración

Usamos la sucesión `T_k` de [TLOG-DEF-00024](#tlog-def-00024). Mostramos por inducción ordinaria sobre `k` que cada elemento de `T_k` satisface `P`. En `T_0`, todo elemento es una variable o un término nulario, y la tesis corresponde respectivamente a las condiciones 1 y 2 con `n=0`. Para el paso, si `t\in T_{k+1}`, o ya pertenece a `T_k`, o es `f(t_1,\ldots,t_n)` con `n\ge 1` y cada `t_i\in T_k`. En el segundo caso las hipótesis inductivas dan `P(t_i)` y la cláusula 2 da `P(t)`. Por tanto la propiedad vale en cada etapa y, como `\operatorname{Tm}_\tau=\bigcup_{k<\omega}T_k`, vale para todo término. `\square`

> [!important] Diferencia de método
> Una **prueba** de `P(t)` por inducción no es una **definición** de una función sobre términos por recursión. El principio de existencia y unicidad para funciones recursivas, junto con sustitución de términos, se trabajará después de controlar sus condiciones de formación en el Capítulo 6.

## 5.7. Fórmulas atómicas

### Definición 5.7.1 — Átomos relacionales y ecuaciones {#tlog-def-00025}

El conjunto `\operatorname{At}_\tau` de **fórmulas atómicas** contiene exactamente los objetos sintácticos de dos clases:

1. **Átomo relacional:** `\operatorname{Rel}_R(t_1,\ldots,t_n)` cuando `R\in R_n` y `t_i\in\operatorname{Tm}_\tau`. Su serialización canónica es `R(t_1,\ldots,t_n)`. Si `R\in R_0`, el átomo `R()` carece de argumentos, pero sigue siendo una fórmula atómica.
2. **Ecuación:** `\operatorname{Eq}(s,t)` cuando `s,t\in\operatorname{Tm}_\tau`; su escritura canónica parentizada es `(s\doteq t)`, donde el signo impreso `=` pertenece al **lenguaje objeto** y `\doteq` distingue ese uso tipográficamente. **No** significa que las expresiones `s` y `t` sean iguales en `\mathsf M_{\mathrm{ext}}`.

Estas dos clases son disjuntas por etiqueta de constructor. En una ecuación se requieren dos términos completos; en un átomo relacional, exactamente tantos argumentos como exige la aridad. **Ningún término aislado es por ello una fórmula atómica**, salvo que esté efectivamente convertido en átomo mediante uno de los constructores anteriores.

Las fórmulas atómicas **no** requieren cuantificadores ni conectivas. La igualdad lógica es primitiva aun en la **signatura vacía** (`F_n=R_n=\varnothing` para todo `n`): por ejemplo, `(x_0\doteq x_1)` sigue siendo atómica.

El conjunto de **todas** las fórmulas de primer orden no se ha definido todavía; se formará inductivamente desde `\operatorname{At}_\tau` en `TLOG-CH05-M02`. No se anticipan nociones de fórmula cerrada, de verdad en una estructura ni de demostrabilidad.

## 5.8. Ejemplos de formación y errores tipados

**Signatura aritmética mínima.** Sean `F_0=\{0\}`, `F_1=\{S\}`, `F_2=\{+\}`, `R_2=\{<\}` y vacías las restantes clases de símbolos. Entonces `0()` y `x_0` son términos; también `S(0())` y `+(S(0()),x_0)`. Por ejemplo, son átomos:

$$
\operatorname{Eq}(+(S(0()),x_0),S(x_1)),
\qquad
\operatorname{Rel}_{<}(x_0,x_1).
$$

La escritura matemática usual `S(0)+x_0=S(x_1)` es una **abreviación legible** de la primera expresión y no sustituye la gramática canónica. Ni el símbolo `+` sin sus argumentos ni `S(x_0,x_1)` son términos de esta signatura.

**Lenguaje puro de identidad.** Para la signatura vacía `\tau_{\varnothing}:=((\varnothing)_{n\in\omega},(\varnothing)_{n\in\omega})`, los únicos términos son las variables. Pese a ello, existen átomos `(x_i\doteq x_j)`; la igualdad no depende de la presencia de símbolos extralógicos.

**Símbolo relacional nulario.** Si `R_0=\{Q\}`, `Q()` es un átomo; no es un término y no debe confundirse con una constante de `F_0`.

## 5.9. Controles de frontera

1. **Meta/objeto.** `s=t` entre términos denota igualdad metateórica de expresiones; `(s\doteq t)` denota una **fórmula objeto** aún sin valor de verdad asignado.
2. **Lenguaje/signatura.** `\tau` es sólo la signatura extralógica; `\Sigma_\tau` es su alfabeto total con símbolos lógicos y variables; `\operatorname{Tm}_\tau` y `\operatorname{At}_\tau` son subconjuntos seleccionados mediante formación.
3. **Formación/semántica.** La definición de un término no le asigna un elemento de una estructura. En particular `R_n` no designa aquí una relación sobre un dominio.
4. **Átomos/fórmulas generales.** `\operatorname{At}_\tau` está definido, pero `\operatorname{Fm}_\tau` permanece reservado para `M02`.
5. **Aridades/igualdad.** Los símbolos `R_2` no incluyen el token lógico `=`; las aridades de cualquier `f` y `R` son únicas y finitas.
6. **Elección/tamaño.** Signaturas y términos son conjuntos de `ZF`, y la inducción usa sólo etapas finitas; no se exige que `\tau` sea enumerable ni se emplea AC.

## 5.12. Estado y próximo frente

```text
TLOG-CH05-0001 = PARTIAL-CLOSURE / NOT CLOSED
CH05-M01 = CLOSED / PASS
new closed nodes = 7
TLOG registered/closed = 64/64
DAG = 64 nodes / 136 direct edges / PASS
CH00–CH04 = CLOSED
PART I = CLOSED / PASS
PART II = OPEN / CH05 PARTIAL-CLOSURE
```

Próximo microtramo: `TLOG-CH05-M02 — Formación de fórmulas, cuantificación, inducción y legibilidad única`.


## 5.13. Formación general de fórmulas de primer orden

### Definición 5.13.1 — Fórmulas bien formadas de signatura $\tau$ {#tlog-def-00026}

Sea $\tau$ una signatura arbitraria como en §5.2, $X=\{x_i:i\in\omega\}$ su conjunto de variables individuales y $\operatorname{At}_\tau$ el conjunto de átomos de §5.7. Definimos el conjunto de **fórmulas** $\operatorname{Fm}_\tau\subseteq\Sigma_\tau^{<\omega}$ como la menor colección de expresiones que contiene $\operatorname{At}_\tau$ y es cerrada bajo estos constructores **distintos**:

1. **Negación.** Si $\varphi\in\operatorname{Fm}_\tau$, también $\operatorname{Neg}(\varphi)$ es fórmula. Su serialización canónica, con paréntesis externos, es $(\neg\varphi)$.
2. **Conectivos binarios.** Para $\circ\in\{\land,\lor,\to,\leftrightarrow\}$ y $\varphi,\psi\in\operatorname{Fm}_\tau$, también $\operatorname{Bin}_\circ(\varphi,\psi)$ es fórmula. Su serialización es $(\varphi\circ\psi)$.
3. **Cuantificación.** Para $Q\in\{\forall,\exists\}$, $x\in X$ y $\varphi\in\operatorname{Fm}_\tau$, también $\operatorname{Quant}_{Q,x}(\varphi)$ es fórmula. Su serialización es $(Qx\,\varphi)$, donde `\,` es exclusivamente un espacio tipográfico: **no introduce ningún token en la serialización**. La cadena objeto canónica resulta de concatenar `(`, el token `Q`, el token `x`, la cadena de $\varphi$ y `)`.

En particular, las cadenas objeto de los dos cuantificadores son **distintas**: $(\forall x\,\varphi)$ y $(\exists x\,\varphi)$ son fórmulas generadas por dos operadores primitivos. El espacio después de $x$ en la impresión matemática no es un símbolo objeto adicional. Cuando no haya riesgo, usaremos $(\forall x\,\varphi)$ como nombre editorial de esa concatenación, y análogamente para $\exists$.

La cláusula de cuantificación exige **una variable individual** como parámetro, incluso si esa variable no aparece entre los tokens de la matriz. No exige que los nombres de los cuantificadores anidados sean distintos: $(\forall x_0\,(\exists x_0\,(x_0\doteq x_0)))$ es bien formada. El análisis de ocurrencias libres, ligadas y de sustituciones admisibles se reserva al Capítulo 6.

Para garantizar existencia del menor conjunto en $\mathsf M_{\mathrm{ext}}$, construimos etapas:

$$
W_0:=\operatorname{At}_\tau,
$$
$$
\begin{aligned}
W_{k+1}:={}&W_k\cup\{\operatorname{Neg}(\varphi):\varphi\in W_k\}\\
&\cup\bigcup_{\circ\in\{\land,\lor,\to,\leftrightarrow\}}
\{\operatorname{Bin}_\circ(\varphi,\psi):\varphi,\psi\in W_k\}\\
&\cup\bigcup_{Q\in\{\forall,\exists\},\,x\in X}
\{\operatorname{Quant}_{Q,x}(\varphi):\varphi\in W_k\},
\end{aligned}
$$
$$
\boxed{\operatorname{Fm}_\tau:=\bigcup_{k<\omega}W_k}.
$$

Cada etapa es un conjunto de cadenas finitas sobre un alfabeto que es un conjunto; los productos finitos, imágenes, uniones y la recursión sobre $\omega$ existen en ZF. La unión es cerrada bajo los operadores, y cualquier conjunto de expresiones con las mismas propiedades contiene cada $W_k$ por inducción ordinaria. Así se obtiene su minimalidad. **No se presupone numerabilidad de la signatura, un procedimiento global de decisión para ella ni axioma de elección.**

Las únicas fórmulas atómicas son las de $\operatorname{At}_\tau$; un término $t\in\operatorname{Tm}_\tau$ no es fórmula por sí solo. La igualdad lógica $\doteq$ pertenece únicamente al caso atómico; no es un operador binario sobre fórmulas.

## 5.14. Legibilidad única de fórmulas

### Lema 5.14.1 — Descomposición inmediata única {#tlog-lem-00010}

Toda $\theta\in\operatorname{Fm}_\tau$ tiene **exactamente una** descomposición inmediata de uno de los cuatro tipos: atómica; negación de una fórmula; aplicación de un único conectivo binario a dos fórmulas ordenadas; o aplicación de un cuantificador, con variable individual determinada, a una única matriz. En particular, si

$$
\operatorname{Quant}_{Q,x}(\varphi)=
\operatorname{Quant}_{Q',y}(\psi),
$$

entonces $Q=Q'$, $x=y$ y $\varphi=\psi$; una igualdad de fórmulas binarias fuerza el mismo conectivo y las mismas dos subfórmulas ordenadas.

#### Demostración

Comparamos **secuencias de tokens**, no expresiones informales ni sus significados. La disjunción de categorías de $\Sigma_\tau$ y la serialización canónica permiten leer la raíz de una expresión bien formada:

1. Si su primer token pertenece a algún $R_n$, es un átomo relacional. El token inicial fija $R$ y $n$; los paréntesis y las comas a profundidad externa uno delimitan unívocamente los $n$ términos argumentos por [TLOG-LEM-00009](#tlog-lem-00009). Para $n=0$ se reconoce $R()$.
2. Si comienza con `(` y el token siguiente pertenece a $X$ o a alguna $F_n$, sólo puede ser una ecuación atómica $(s\doteq t)$. El símbolo $\doteq$ de profundidad uno separa exactamente dos términos, que se leen unívocamente por [TLOG-LEM-00009](#tlog-lem-00009).
3. Si comienza con `(` y el siguiente token es $\neg$, es negación. Su única matriz es la fórmula que aparece después de ese token y antes del paréntesis final.
4. Si comienza con `(` y el siguiente token es $\forall$ o $\exists$, es cuantificación. Los tokens siguientes fijan, en ese orden, el cuantificador y la variable individual; el resto anterior al cierre externo es la matriz única.
5. En el caso restante, comienza con `(` seguido del inicio de una **fórmula** (un token relacional o `(`). Debe ser una composición binaria. Exploramos la cadena desde el primer paréntesis, llevando el balance de apertura/cierre: el **único token conectivo de profundidad uno** es el operador binario de la raíz. Su posición divide de manera única los dos segmentos, ambos fórmulas; todos los conectivos internos están a profundidad mayor.

El análisis exhaustivo cubre todas las cláusulas inductivas de §5.13. Los casos están disjuntos por sus tokens iniciales y, en el binario, por el separador de profundidad uno; los argumentos resultan únicos. Cada subfórmula inmediata es una cadena estrictamente más corta que la fórmula de partida, de modo que repetir el procedimiento termina y produce un **árbol finito de análisis unívoco**. $\square$

Esta prueba distingue asimismo $(s\doteq t)$ de $(\varphi\leftrightarrow\psi)$: igualdad lógica y bicondicional son símbolos de clases sintácticas distintas. Ninguna ley de interpretación de la igualdad, semántica de cuantificadores o sustitución ha intervenido.

## 5.15. Inducción estructural de fórmulas

### Metateorema 5.15.1 — Principio de inducción sobre $\operatorname{Fm}_\tau$ {#tlog-mth-00015}

Sea $P(\varphi)$ una propiedad metateórica de fórmulas que cumple estas hipótesis:

1. $P(\alpha)$ para toda $\alpha\in\operatorname{At}_\tau$.
2. Si $P(\varphi)$, entonces $P(\operatorname{Neg}(\varphi))$.
3. Para cada $\circ\in\{\land,\lor,\to,\leftrightarrow\}$, si $P(\varphi)$ y $P(\psi)$, entonces $P(\operatorname{Bin}_\circ(\varphi,\psi))$.
4. Para cada $Q\in\{\forall,\exists\}$ y **todo** $x\in X$, si $P(\varphi)$, entonces $P(\operatorname{Quant}_{Q,x}(\varphi))$.

Entonces

$$
\boxed{(\forall\varphi\in\operatorname{Fm}_\tau)\;P(\varphi)}.
$$

#### Demostración

Probamos por inducción ordinaria en $k$ que $P$ se cumple en cada $W_k$ del §5.13. En $W_0=\operatorname{At}_\tau$ vale por la hipótesis 1. Supóngase la tesis para $W_k$; un elemento de $W_{k+1}$ ya pertenecía a $W_k$, o se obtuvo de uno o dos elementos de $W_k$ por alguno de los siete operadores: una negación, cuatro conectivos binarios o uno de los dos cuantificadores con variable individual. Corresponde a las hipótesis 2, 3 o 4, respectivamente. Concluimos la tesis para $W_{k+1}$. Finalmente $\operatorname{Fm}_\tau=\bigcup_kW_k$; por ello vale en toda fórmula. $\square$

**Delimitación.** Inducir propiedades sobre fórmulas no equivale a disponer de un teorema general de **recursión para definir funciones** sobre ellas. La existencia/unicidad de tales transformaciones, y en especial la sustitución que evita captura, seguirá en el Capítulo 6.

## 5.16. Subfórmulas y altura sintáctica

### Definición 5.16.1 — Subfórmulas y rango {#tlog-def-00027}

El árbol finito determinado por [TLOG-LEM-00010](#tlog-lem-00010) tiene como raíz la fórmula $\varphi$; sus **nodos de fórmula** son precisamente las ocurrencias de fórmulas que resultan de descomponer cada constructor. El conjunto finito de etiquetas de esos nodos se denota

$$
\operatorname{SubFm}_\tau(\varphi).
$$

La fórmula completa es subfórmula de sí misma. Para el caso atómico $\alpha$, este conjunto es $\{\alpha\}$. Para negación y cuantificación, se añade la raíz al conjunto de subfórmulas de la matriz; para un conectivo binario, se añade la raíz a la unión de los conjuntos de subfórmulas de ambos argumentos. Si dos ocurrencias de una misma fórmula aparecen en posiciones distintas, el **árbol de ocurrencias** distingue esas posiciones, mientras que $\operatorname{SubFm}_\tau$ las identifica como un solo elemento del conjunto. Los subárboles de **términos** dentro de un átomo no son subfórmulas.

Definimos la **altura o rango sintáctico** de la fórmula como la altura de ese árbol:

$$
\operatorname{rk}_\tau(\alpha):=0 \quad (\alpha\in\operatorname{At}_\tau),
$$
$$
\begin{aligned}
\operatorname{rk}_\tau(\operatorname{Neg}(\varphi))&:=1+\operatorname{rk}_\tau(\varphi),\\
\operatorname{rk}_\tau(\operatorname{Bin}_\circ(\varphi,\psi))&:=1+\max\{\operatorname{rk}_\tau(\varphi),\operatorname{rk}_\tau(\psi)\},\\
\operatorname{rk}_\tau(\operatorname{Quant}_{Q,x}(\varphi))&:=1+\operatorname{rk}_\tau(\varphi).
\end{aligned}
$$

Por el árbol de análisis único y finito, estas especificaciones producen un conjunto finito de subfórmulas y un único número natural para el rango. Más explícitamente, la inducción de [TLOG-MTH-00015](#tlog-mth-00015) prueba a la vez ambas afirmaciones: son inmediatas en un átomo; agregar una raíz a uno o dos árboles finitos conserva finitud, y el máximo de uno o dos rangos naturales es natural. **Esto es una medida combinatoria concreta**, no la adopción anticipada del teorema general de recursión sintáctica del Capítulo 6.

## 5.17. Escritura compacta y alcance recuperable

### Convención 5.17.1 — Notación editorial de conectivos y cuantificadores {#tlog-cnv-00008}

La fuente sintáctica autoritativa sigue siendo la **serialización canónica** de §5.13. Para exposición ordinaria, autorízanse las abreviaciones $\neg\varphi$, $\varphi\land\psi$, etc. cuando el agrupamiento resulte inequívoco por paréntesis expresos o por la precedencia heredada editorialmente del capítulo proposicional:

$$
\neg>\land>\lor>\to>\leftrightarrow.
$$

Las fórmulas cuantificadas se escribirán preferentemente $\forall x(\varphi)$ y $\exists x(\varphi)$, con la **matriz encerrada explícitamente** cuando sea compuesta. Así $\forall x(P(x)\to Q(x))$ denota que todo el condicional está dentro del cuantificador, mientras que $(\forall x P(x))\to Q(x)$ sitúa el condicional fuera. En esta notación abreviada $P,Q$ son símbolos relacionales de la signatura declarada y la impresión omite los paréntesis estructurales externos; **ninguna abreviación añade operadores ni modifica la clase $\operatorname{Fm}_\tau$**.

El símbolo $\doteq$ se emplea para recordar que una ecuación es fórmula objeto; el signo $=$ entre expresiones es igualdad **metateórica** salvo declaración inequívoca en contrario. La abreviación $\exists x\varphi$ **no** significa aquí $\neg\forall x\neg\varphi$ por definición: ambos cuantificadores son primitivos, y ni siquiera se ha definido una semántica de primer orden que permita probar equivalencias.

## 5.18. Ejemplos de alcance y tipado

Sea una signatura con $F_0=\{0\}$, $F_1=\{S\}$, $F_2=\{+\}$ y $R_2=\{<\}$, con los demás conjuntos de símbolos vacíos. Sean

$$
A:=\operatorname{Rel}_{<}(x_0,x_1),
\qquad
B:=\operatorname{Eq}(+(x_0,0()),S(x_1)).
$$

Entonces $A,B\in\operatorname{At}_\tau$, y la siguiente es una **fórmula**, obtenida mediante cuantificación existencial de $B$, implicación desde $A$ y cuantificación universal del resultado:

$$
\Phi:=\operatorname{Quant}_{\forall,x_0}
\bigl(\operatorname{Bin}_{\to}
\bigl(A,\operatorname{Quant}_{\exists,x_1}(B)\bigr)\bigr).
$$

Su impresión usual es

$$
\forall x_0\bigl(x_0<x_1\to\exists x_1( x_0+0\doteq S(x_1))\bigr).
$$

La subfórmula $A$ queda **fuera del alcance sintáctico** del cuantificador existencial que antecede a $B$, aunque ambas contengan la misma variable impresa $x_1$. La distinción formal entre ocurrencias libres y ligadas se fijará en el Capítulo 6.

En la **signatura vacía** también existen fórmulas, por ejemplo $\forall x_0(x_0\doteq x_0)$; no se precisan símbolos relacionales extralógicos. En cambio, ni $x_0$ ni $\neg x_0$ son fórmulas: $x_0$ es un término, y la negación sólo admite fórmulas como argumentos. La expresión $(\forall\varphi)$ tampoco es fórmula, pues falta la variable individual exigida por el constructor.

## 5.20. Cierre del Capítulo 5

Quedan fijados signatura, aridades, variables, términos, átomos, fórmulas de primer orden, cuantificación con ambos símbolos primitivos, legibilidad única e inducción, además de subfórmulas y rango. El capítulo satisface así su **salida arquitectónica sintáctica**. Las operaciones sobre variables, sustitución y recursión general, así como toda semántica y prueba de primer orden, permanecen fuera de este cierre.

```text
TLOG-CH05-M02 = CLOSED / PASS
TLOG-CH05-0001 = CLOSED
chapter 5 nodes = 12/12 closed
registered TLOG nodes = 69
closed TLOG nodes = 69
DAG = 69 nodes / 146 direct edges / PASS
cross-treaty direct edges = 0
formalization candidates = 15
compiled / verified = 0
chapters closed = 6/24
PART I = CLOSED / PASS
PART II = OPEN / CH06 PENDING
```

**Próximo frente:** `TLOG-CH06-0001 — Variables, sustitución y recursión sintáctica`.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 4](capitulo-04.md) · [Capítulo 6 →](capitulo-06.md)

