---
title: "Cuantificadores, predicados y lenguaje matemático"
description: "Sexto capítulo del Tomo I de Álgebra para matemáticos: predicados, dominios, variables libres y ligadas, cuantificadores universal y existencial, negación, alcance, dependencia, orden de cuantificadores y existencia única."
content-id: MA-BCH-0017
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C06
editorial-id: MA-BCH-APM-01-006
status: published
date-created: 2026-09-12
date-modified: 2026-09-12
areas:
  - algebra
  - fundamentos
  - logica
level: fundamental
topics:
  - predicados
  - dominio-de-discurso
  - variables-libres-y-ligadas
  - cuantificador-universal
  - cuantificador-existencial
  - negacion-de-cuantificadores
  - alcance
  - orden-de-cuantificadores
  - dependencia-de-variables
  - existencia-unica
prerequisites:
  - MA-BCH-0016
related:
  - MA-BOK-0006
  - MA-BCH-0014
  - MA-BCH-0015
  - MA-BCH-0016
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 6. Cuantificadores, predicados y lenguaje matemático

En los capítulos 4 y 5 trabajamos con proposiciones completas: afirmaciones que ya podían ser verdaderas o falsas. Pero la matemática real está llena de frases como “$x$ es par”, “$x^2<y$”, “$n$ divide a $m$” o “$x$ tiene una raíz cuadrada”. Antes de decidir su verdad necesitamos saber **qué objetos pueden ocupar esas variables** y **qué estamos afirmando acerca de ellos**.

Aquí aparece una capa nueva del lenguaje matemático. Ya no basta con combinar proposiciones mediante $\neg$, $\land$, $\lor$ o $\Rightarrow$. Debemos aprender a manejar **predicados, dominios, variables libres y ligadas, cuantificadores, alcance y dependencia**.

La pregunta rectora del capítulo es:

> **¿Cómo convertimos una condición abierta en una afirmación matemática precisa, y cómo leemos exactamente qué promete una frase con “para todo”, “existe” o “existe un único”?**

Salvo indicación contraria, los dominios que usemos serán no vacíos. No desarrollaremos todavía una teoría formal de lógica de primer orden; el objetivo es operativo y matemático: leer, escribir, negar y comparar afirmaciones cuantificadas con la precisión que exigirá todo el resto del libro.

***
## 6.1. De una expresión abierta a una afirmación

Comparemos tres escrituras:

- $x+3$;
- $x+3=7$;
- $4+3=7$.

La primera es una **expresión**: representa un objeto numérico una vez que se conoce $x$. La segunda es una **condición abierta**: según el valor que adopte $x$, puede resultar verdadera o falsa. La tercera ya es una **proposición**: no queda ninguna variable sin determinar y podemos asignarle un valor de verdad.

A una condición como

$P(x): x+3=7$

la llamaremos **predicado** en la variable $x$. Si sustituimos $x=4$, obtenemos la proposición verdadera $P(4)$. Si sustituimos $x=10$, obtenemos la proposición falsa $P(10)$.

Hay otra forma de cerrar la condición: cuantificarla. Por ejemplo,

$\exists x\in\mathbb R\;(x+3=7)$

dice que existe al menos un real que satisface la condición, mientras que

$\forall x\in\mathbb R\;(x+3=7)$

dice que todos los reales la satisfacen. La primera afirmación es verdadera; la segunda, falsa.

La lección inicial es sencilla pero decisiva:

> **Una fórmula con variables libres no es, en general, una afirmación completa. Para obtener una proposición debemos fijar valores o ligar las variables mediante cuantificadores.**

## 6.2. Predicados y dominio de discurso

El predicado no vive aislado del conjunto de objetos que estamos autorizados a considerar. Ese conjunto se llama **dominio**, **universo de discurso** o simplemente universo.

Consideremos

$P(x): x^2=2$.

La pregunta “¿existe un $x$ tal que $P(x)$?” tiene respuestas distintas según el dominio:

- en $\mathbb Z$, no hay solución;
- en $\mathbb Q$, tampoco;
- en $\mathbb R$, sí: $x=\sqrt2$ y $x=-\sqrt2$.

Por eso la escritura

$\exists x\;P(x)$

es incompleta si el contexto no deja claro qué objetos puede recorrer $x$.

El dominio puede aparecer explícitamente, como en $\forall n\in\mathbb Z$, o quedar fijado por el contexto. En un texto bien escrito, esa información nunca debería ser ambigua.

### El mismo símbolo, distinta afirmación

La fórmula

$\forall x\;(x^2\ge x)$

es verdadera si el dominio es $\{0,1\}$, pero falsa sobre $\mathbb R$, pues $x=\tfrac12$ da $\tfrac14<\tfrac12$.

El dominio no es un detalle externo: forma parte del significado matemático de la afirmación.

## 6.3. Variables libres y variables ligadas

Una variable es **libre** cuando todavía no está controlada por un cuantificador dentro de la expresión considerada. Es **ligada** cuando un cuantificador determina su alcance.

Ejemplos:

- en $x^2>0$, la variable $x$ es libre;
- en $\forall x\in\mathbb R\;(x^2\ge0)$, $x$ está ligada por $\forall$;
- en $\forall x\,P(x,y)$, $x$ está ligada y $y$ queda libre;
- en $\forall x\,\exists y\,R(x,y)$, ambas variables están ligadas.

Una fórmula puede contener simultáneamente variables libres y ligadas. Mientras quede una variable libre cuyo valor no esté fijado por el contexto, no tenemos todavía una proposición cerrada.

### El nombre de la variable no es lo esencial

Las afirmaciones

$\forall x\in\mathbb R\;(x^2\ge0)$

y

$\forall t\in\mathbb R\;(t^2\ge0)$

tienen el mismo significado. Cambiar el nombre de una variable ligada es inocuo si se hace de manera coherente y no se produce una colisión con otra variable que ya tenga función distinta.

Más adelante veremos un error típico: renombrar una variable ligada con el mismo nombre de una variable libre puede cambiar el significado al **capturarla**.

## 6.4. El cuantificador universal

El símbolo $\forall$ se lee “para todo” o “para cada”. La afirmación

$$
\forall x\in D\;P(x)
$$

dice que **cada elemento** del dominio $D$ satisface el predicado $P$.

Por ejemplo,

$\forall n\in\mathbb Z\;(n+0=n)$

es verdadera. No afirma que exista algún entero con esa propiedad, sino que ninguno queda fuera.

### Una afirmación universal es fuerte

Para establecer $\forall x\in D\;P(x)$ no basta comprobar muchos casos. Incluso un millón de ejemplos compatibles no elimina la posibilidad de que exista un caso posterior que falle.

En un dominio finito pequeño podríamos revisar todos los elementos. En dominios grandes o infinitos, normalmente necesitaremos un argumento general. Ese repertorio de argumentos será tema de C10; aquí nos importa reconocer la estructura lógica del objetivo.

### Universal con condición

Una forma extremadamente común es

$$
\forall x\in D\;[A(x)\Rightarrow B(x)].
$$

Se lee: “para todo $x$ del dominio, si $x$ cumple $A$, entonces cumple $B$”. Los objetos que no satisfacen $A$ no constituyen contraejemplos, porque en ellos el antecedente es falso.

## 6.5. Refutar un universal: el poder de un contraejemplo

Hay una asimetría fundamental entre demostrar y refutar una afirmación universal.

Para confirmar

$\forall x\in D\;P(x)$

necesitamos controlar todos los casos. Para refutarla basta encontrar un solo elemento $a\in D$ tal que $P(a)$ sea falsa.

Ese elemento se llama **contraejemplo**.

Consideremos la afirmación:

> Para todo entero $n$, se cumple $n^2>n$.

Basta tomar $n=0$. Entonces $0^2>0$ es falso. Por tanto la afirmación universal es falsa.

Un contraejemplo debe respetar exactamente el dominio y las hipótesis. Si la afirmación dice “todo entero par mayor que $2$...”, un número impar o el entero $2$ no puede refutarla.

### Ejemplo no es demostración

Encontrar cinco casos en los que una propiedad funciona puede sugerir una conjetura. No demuestra una afirmación universal. En cambio, encontrar un solo caso en el que falla sí decide la cuestión en sentido negativo.

## 6.6. El cuantificador existencial

El símbolo $\exists$ se lee “existe al menos uno”. La afirmación

$$
\exists x\in D\;P(x)
$$

dice que hay **por lo menos un elemento** del dominio que satisface $P$.

Para demostrar una afirmación existencial concreta suele bastar exhibir un **testigo**.

Por ejemplo,

$\exists n\in\mathbb Z\;(n^2=49)$

es verdadera porque $n=7$ es un testigo. También $n=-7$ lo es. La existencia no implica unicidad.

### Existencia no significa “sé cuál es”

En matemática avanzada existen demostraciones de existencia que no construyen explícitamente el objeto. En este capítulo, sin embargo, la mayoría de nuestros ejemplos serán constructivos: producir un testigo será el modo más transparente de entender el cuantificador.

### Refutar un existencial

Para mostrar que $\exists x\in D\;P(x)$ es falsa debemos establecer que **ningún** elemento del dominio funciona. La mera frase “no encontré ninguno” no es un argumento.

## 6.7. Negar cuantificadores

Éste es uno de los núcleos del capítulo.

Negar “todos cumplen $P$” significa afirmar “hay al menos uno que no cumple $P$”. Por eso:

$$
\neg(\forall x\,P(x))\equiv\exists x\,\neg P(x).
$$

Del mismo modo, negar “existe alguno que cumple $P$” significa afirmar “ninguno cumple $P$”, es decir:

$$
\neg(\exists x\,P(x))\equiv\forall x\,\neg P(x).
$$

Estas leyes son los análogos cuantificados de las leyes de De Morgan de C5: al atravesar el cuantificador, la negación **cambia $\forall$ por $\exists$ y $\exists$ por $\forall$**.

### La negación debe seguir avanzando

Supongamos

$$
\forall n\in\mathbb Z\;[E(n)\Rightarrow E(n^2)],
$$

donde $E(n)$ significa “$n$ es par”. Su negación no es simplemente cambiar $\forall$ por $\exists$. Debemos negar también el contenido:

$$
\exists n\in\mathbb Z\;\neg[E(n)\Rightarrow E(n^2)].
$$

Por C5, $\neg(A\Rightarrow B)\equiv A\land\neg B$. Así obtenemos

$$
\exists n\in\mathbb Z\;[E(n)\land\neg E(n^2)].
$$

Es decir: “existe un entero par cuyo cuadrado no es par”.

### “No todos” y “ninguno” no son lo mismo

“no todos los elementos cumplen $P$” se traduce como $\exists x\,\neg P(x)$.

“ningún elemento cumple $P$” se traduce como $\forall x\,\neg P(x)$.

Confundir estas dos frases es uno de los errores lógicos más frecuentes.

## 6.8. Cuantificación restringida

La notación

$\forall x\in A\;P(x)$

dice que sólo nos interesan los elementos de $A$. Conceptualmente puede leerse como

$$
\forall x\;[x\in A\Rightarrow P(x)].
$$

En cambio,

$\exists x\in A\;P(x)$

se interpreta como

$$
\exists x\;[x\in A\land P(x)].
$$

La diferencia entre implicación y conjunción es esencial.

Para un universal restringido, un objeto que no pertenece a $A$ no debe convertirse en contraejemplo. Para un existencial restringido, el testigo debe cumplir simultáneamente dos requisitos: pertenecer a $A$ y satisfacer $P$.

No desarrollaremos aún operaciones con conjuntos; C7 dará a $\in$, subconjunto, unión, intersección y complemento un tratamiento sistemático. Aquí usamos la pertenencia sólo para expresar dominios restringidos.

### Negaciones restringidas

De las reglas anteriores obtenemos directamente:

$$
\neg[\forall x\in A\;P(x)]\equiv\exists x\in A\;\neg P(x),
$$

$$
\neg[\exists x\in A\;P(x)]\equiv\forall x\in A\;\neg P(x).
$$

## 6.9. Alcance, paréntesis y variables

Todo cuantificador tiene un **alcance**: la parte de la fórmula sobre la cual actúa.

Comparemos:

$$
\forall x\,[P(x)\lor Q(x)]
$$

y

$$
(\forall x\,P(x))\lor Q(x).
$$

En la primera fórmula, las dos apariciones de $x$ están bajo el alcance del cuantificador. En la segunda, sólo la aparición dentro de $P(x)$ está ligada; la $x$ de $Q(x)$ queda libre.

Los paréntesis no son decoración. Determinan qué fragmento está cuantificado.

### Renombrar sin capturar

En

$\forall x\,P(x,y)$

podemos cambiar la variable ligada $x$ por $t$ y escribir $\forall t\,P(t,y)$. Pero no deberíamos renombrarla como $y$ sin más, porque la $y$ original era libre. La escritura $\forall y\,P(y,y)$ ha ligado una variable que antes no lo estaba y, por tanto, puede expresar algo distinto.

La disciplina de alcance cumple aquí la misma función que el control de subfórmulas en C5: antes de transformar símbolos debemos saber **qué estructura estamos modificando**.

## 6.10. Dos cuantificadores: el orden importa

Cuando aparecen cuantificadores de distinto tipo, cambiar su orden puede cambiar radicalmente el significado.

Consideremos, sobre $\mathbb R$:

$$
\forall x\;\exists y\;(y>x).
$$

La afirmación es verdadera: dado un real $x$, podemos elegir $y=x+1$.

Comparemos con

$$
\exists y\;\forall x\;(y>x).
$$

Ahora se pide un único real $y$ que sea mayor que **todos** los reales. Eso es imposible.

La diferencia verbal es:

- $\forall x\exists y$: **para cada** $x$ podemos buscar un $y$, posiblemente distinto;
- $\exists y\forall x$: debe existir **un mismo** $y$ que funcione para todos los $x$.

### Cuantificadores del mismo tipo

Bajo condiciones ordinarias,

$\forall x\forall y\,P(x,y)$

y

$\forall y\forall x\,P(x,y)$

expresan lo mismo. Análogamente ocurre con dos existenciales. El peligro aparece especialmente al intercambiar $\forall$ y $\exists$.

## 6.11. Dependencia entre variables y elección de testigos

En

$$
\forall x\;\exists y\;R(x,y),
$$

el valor de $y$ puede elegirse **después** de conocer $x$. Por ello el testigo puede depender de $x$.

Ejemplo:

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y=2x).
$$

Una elección natural es $y=2x$. No estamos exhibiendo un único número real; estamos dando una regla de elección que produce un testigo para cada $x$.

En cambio, en

$$
\exists y\;\forall x\;R(x,y),
$$

el $y$ debe fijarse **antes** de recorrer todos los $x$. Ya no puede adaptarse a cada caso.

Esta idea anticipa un tema futuro: una regla que asigna a cada entrada una salida. C9 estudiará las funciones de forma sistemática. Aquí sólo necesitamos comprender la dependencia lógica.

### Una advertencia

De $\forall x\exists y\,R(x,y)$ no se sigue automáticamente que haya un único $y$ para cada $x$, ni que la elección sea canónica. La afirmación promete existencia local, nada más.

## 6.12. “Existe un único”: el cuantificador de unicidad

La notación

$$
\exists!x\;P(x)
$$

se lee “existe un único $x$ tal que $P(x)$”. Contiene dos afirmaciones distintas:

1. **existencia:** al menos un elemento satisface $P$;
2. **unicidad:** no hay dos elementos distintos que satisfagan $P$.

Una expansión útil es

$$
\exists x\,[P(x)\land\forall y\,(P(y)\Rightarrow y=x)].
$$

El primer $P(x)$ garantiza existencia. El universal posterior dice que cualquier otro candidato $y$ que satisfaga $P$ debe coincidir con $x$.

Por ejemplo,

$\exists!x\in\mathbb R\;(x+3=5)$

es verdadera: $x=2$ existe y cualquier real que satisfaga la ecuación debe ser $2$.

En cambio,

$\exists!x\in\mathbb R\;(x^2=4)$

es falsa. Hay soluciones, pero son dos: $2$ y $-2$.

Existencia y unicidad deben comprobarse por separado.

## 6.13. Traducir lenguaje matemático a símbolos

La traducción correcta comienza identificando tres cosas:

1. **dominio**;
2. **cuantificador**;
3. **predicado y conectivos internos**.

Ejemplo:

> Todo entero par es divisible por $2$.

Una formalización natural es

$$
\forall n\in\mathbb Z\;[E(n)\Rightarrow D_2(n)],
$$

donde $E(n)$ significa “$n$ es par” y $D_2(n)$ significa “$2$ divide a $n$”.

Ejemplo:

> Algunos enteros no son cuadrados perfectos.

Puede escribirse

$$
\exists n\in\mathbb Z\;\neg C(n),
$$

donde $C(n)$ significa “$n$ es un cuadrado perfecto”.

### Palabras que revelan estructura

- “todo”, “cada”, “cualquiera” suelen señalar $\forall$;
- “algún”, “existe”, “hay al menos uno” suelen señalar $\exists$;
- “ningún” suele convertirse en $\forall x\,\neg P(x)$ o, equivalentemente, $\neg\exists x\,P(x)$;
- “no todos” significa $\exists x\,\neg P(x)$;
- “exactamente uno” señala $\exists!$.

No debemos traducir palabra por palabra: debemos traducir **estructura por estructura**.

## 6.14. Traducir símbolos a lenguaje matemático

La dirección inversa exige la misma disciplina. Consideremos

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x).
$$

Una lectura fiel es:

> Para todo número real $x$, existe un número real $y$ mayor que $x$.

Una lectura defectuosa sería:

> Existe un real mayor que todos los reales.

Esa frase corresponde al orden inverso de cuantificadores.

### Leer desde afuera hacia adentro

Una rutina segura es:

1. leer el cuantificador más externo;
2. fijar mentalmente su variable;
3. pasar al siguiente cuantificador;
4. respetar el orden;
5. leer finalmente el predicado interno.

Por ejemplo,

$$
\exists m\in\mathbb Z\;\forall n\in\mathbb Z\;(m+n=n)
$$

se lee: “existe un entero $m$ tal que, para todo entero $n$, se cumple $m+n=n$”. La afirmación resulta verdadera porque $m=0$ funciona para todos los $n$.

## 6.15. Diagnóstico de errores de cuantificación

Los errores más importantes de este capítulo no son de cálculo, sino de significado.

### Error 1: cambiar el cuantificador al traducir

“Todo entero tiene un sucesor entero” no significa “existe un entero que es sucesor de todos los enteros”.

### Error 2: negar sin cambiar cuantificador

La negación de $\forall x\,P(x)$ no es $\forall x\,\neg P(x)$, sino $\exists x\,\neg P(x)$.

### Error 3: ignorar el dominio

El predicado $x^2=2$ produce afirmaciones existenciales distintas sobre $\mathbb Q$ y sobre $\mathbb R$.

### Error 4: confundir testigo dependiente con testigo fijo

En $\forall x\exists y$, el $y$ puede variar con $x$. En $\exists y\forall x$, no.

### Error 5: confundir existencia con unicidad

Encontrar un testigo prueba existencia, no existencia única.

### Error 6: perder el alcance

Mover paréntesis o renombrar variables puede ligar una variable que antes era libre.

Ante una solución dudosa conviene localizar **el primer paso donde cambia el significado**, no sólo el lugar donde aparece un resultado falso.

## 6.16. Cierre — protocolo de lectura cuantificada

Cuando encuentres una afirmación con variables y cuantificadores, utiliza esta rutina:

```text
1. ¿CUÁL ES EL DOMINIO?
2. ¿CUÁL ES EL PREDICADO?
3. ¿QUÉ VARIABLES ESTÁN LIBRES?
4. ¿QUÉ VARIABLES ESTÁN LIGADAS?
5. ¿QUÉ CUANTIFICADOR LIGA A CADA VARIABLE?
6. ¿CUÁL ES EL ALCANCE DE CADA CUANTIFICADOR?
7. ¿EN QUÉ ORDEN APARECEN?
8. ¿UN TESTIGO PUEDE DEPENDER DE VARIABLES ANTERIORES?
9. ¿CÓMO SE NIEGA LA AFIRMACIÓN COMPLETA?
10. ¿QUÉ BASTARÍA PARA REFUTARLA O PARA EXHIBIR EXISTENCIA?
```

El paso conceptual de C6 puede resumirse así:

$$
\text{condición abierta}
\longrightarrow
\text{dominio + cuantificación}
\longrightarrow
\text{afirmación precisa}.
$$

A partir de ahora, expresiones como “para todo”, “existe” y “existe un único” dejarán de ser palabras de apoyo y se convertirán en parte visible de la estructura matemática.

***

## Ejercicios del capítulo

### A — Predicados y dominios

**1.** Clasifica cada escritura como **expresión**, **predicado abierto** o **proposición**: (a) $x+1$; (b) $x+1=5$; (c) $4+1=5$; (d) $n$ es par; (e) “$6$ es par”.

**2.** Sea $P(x):x^2=2$. Decide la verdad de $\exists x\,P(x)$ cuando el dominio es (a) $\mathbb Z$; (b) $\mathbb Q$; (c) $\mathbb R$.

**3.** Sea $P(x):x^2\ge x$. Decide si $\forall x\,P(x)$ es verdadera sobre (a) $\{0,1\}$; (b) $\mathbb Z$; (c) $\mathbb R$.

**4.** Para $Q(x):1/x>0$, explica por qué el dominio $\mathbb R$ exige una precisión adicional antes de evaluar $Q(0)$.

**5.** Da un dominio finito $D$ con al menos dos elementos para el cual $\forall x\in D\;(x^2=1)$ sea verdadera, y otro dominio finito $E$ para el cual sea falsa.

**6.** Sea $R(x):x^2<4$. Compara $\forall x\,R(x)$ y $\exists x\,R(x)$ sobre los dominios $\mathbb Z$ y $\mathbb R$.

### B — Variables libres y ligadas

**7.** Identifica las variables libres y ligadas en $\forall x\,P(x,y)$.

**8.** Identifica las variables libres y ligadas en $\exists y\,[R(x,y)\land Q(y,z)]$.

**9.** ¿Es una proposición cerrada $\forall x\,\exists y\,R(x,y)$? ¿Y $\forall x\,\exists y\,R(x,y,z)$?

**10.** Convierte el predicado $P(x):x^2=9$ en (a) una proposición mediante sustitución; (b) una proposición existencial; (c) una proposición universal, usando dominio $\mathbb R$.

**11.** En $\forall x\,[P(x,y)\Rightarrow\exists z\,R(x,z)]$, clasifica $x,y,z$ como libres o ligadas.

**12.** Reescribe $\forall x\,P(x,y)$ cambiando el nombre de la variable ligada sin cambiar el significado. Explica por qué $\forall y\,P(y,y)$ no es, en general, una renominación válida.

### C — Universales y contraejemplos

**13.** Decide si $\forall n\in\mathbb Z\;(n^2\ge0)$ es verdadera y explica qué tipo de justificación requiere.

**14.** Refuta $\forall n\in\mathbb Z\;(n^2>n)$ con un contraejemplo.

**15.** Refuta la afirmación “la suma de dos enteros impares es impar”.

**16.** Un estudiante verifica que $n^2+n+17$ es primo para $n=0,1,\dots,15$ y concluye que es primo para todo $n\ge0$. Explica el error y encuentra un contraejemplo.

**17.** La afirmación es: “para todo entero $n$, si $n$ es par entonces $n^2$ es par”. ¿Puede un entero impar ser contraejemplo? Justifica.

**18.** Da un contraejemplo a “para todo real $x$, si $x^2>1$ entonces $x>1$”.

### D — Existenciales y testigos

**19.** Demuestra exhibiendo un testigo que $\exists n\in\mathbb Z\;(n^2=49)$.

**20.** Decide si $\exists n\in\mathbb Z\;(2n=7)$ es verdadera.

**21.** Exhibe un testigo para $\exists x\in\mathbb R\;(0<x<1\land x^2<x)$.

**22.** Exhibe enteros $a,b$ que prueben $\exists a,b\in\mathbb Z\;(a^2-b^2=15)$.

**23.** Demuestra que $\exists n\in\mathbb Z\;(n>1000)$ exhibiendo un testigo. ¿Qué demuestra este ejercicio sobre el tamaño del testigo?

**24.** Un estudiante encuentra dos testigos distintos para $\exists x\,P(x)$ y concluye que la afirmación era falsa porque “$x$ no es único”. Diagnostica el error.

### E — Negación de cuantificadores

**25.** Niega $\forall x\in\mathbb R\;(x^2\ge0)$ sin dejar una negación delante del cuantificador.

**26.** Niega $\exists n\in\mathbb Z\;(n^2=2)$.

**27.** Niega $\forall n\in\mathbb Z\;[E(n)\Rightarrow E(n^2)]$, donde $E(k)$ significa “$k$ es par”.

**28.** Niega $\exists x\in\mathbb R\;(x>0\land x^2<1)$.

**29.** Niega $\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x)$.

**30.** Niega $\exists y\in\mathbb R\;\forall x\in\mathbb R\;(y>x)$.

**31.** Traduce simbólicamente: “No todos los enteros son positivos”.

**32.** Explica con un ejemplo por qué $\neg\forall x\,P(x)$ no equivale a $\forall x\,\neg P(x)$.

### F — Cuantificación restringida

**33.** Reescribe $\forall n\in\mathbb Z\;P(n)$ usando un dominio mayor $D$ que contiene a $\mathbb Z$ y una implicación con pertenencia.

**34.** Reescribe $\exists n\in\mathbb Z\;(n^2=9)$ usando un dominio mayor $D$ y una conjunción con pertenencia.

**35.** Niega $\forall x\in A\;P(x)$.

**36.** Niega $\exists x\in A\;P(x)$.

**37.** Un estudiante escribe “todo entero es racional” como $\forall x\,[x\in\mathbb Z\land x\in\mathbb Q]$. Explica por qué esa forma es incorrecta y corrígela suponiendo un dominio numérico mayor.

**38.** Un estudiante escribe “existe un entero negativo” como $\exists x\,[x\in\mathbb Z\Rightarrow x<0]$. Diagnostica el error y corrige.

### G — Alcance y paréntesis

**39.** En $\forall x\,[P(x)\Rightarrow(Q(x)\lor R)]$, ¿qué apariciones de $x$ están ligadas?

**40.** En $(\forall x\,P(x,y))\lor Q(y)$, ¿qué variables quedan libres?

**41.** Compara $\forall x\,[P(x)\lor Q(x)]$ con $(\forall x\,P(x))\lor Q(x)$. ¿Por qué no son la misma clase de expresión?

**42.** Renombra la variable ligada en $\exists x\,[x>y\land P(x)]$ sin alterar la variable libre $y$.

**43.** Explica por qué sustituir $\forall x\,P(x,y)$ por $\forall y\,P(y,y)$ puede cambiar el significado.

**44.** Distingue $\forall x\,[P(x)\land Q(x)]$ de $(\forall x\,P(x))\land Q(x)$.

### H — Orden de cuantificadores

**45.** Sobre $\mathbb R$, decide la verdad de (a) $\forall x\exists y\;(y>x)$; (b) $\exists y\forall x\;(y>x)$.

**46.** Sobre $\mathbb R$, compara $\forall x\exists y\;(y=x+1)$ con $\exists y\forall x\;(y=x+1)$.

**47.** Sobre $\mathbb Z$, decide $\forall n\exists m\;(m=n+2)$ y su versión con cuantificadores invertidos.

**48.** Sobre $\mathbb Z$, decide (a) $\exists n\forall m\;(n+m=m)$; (b) $\forall m\exists n\;(n+m=m)$.

**49.** Sobre $\mathbb R$, decide $\forall x\exists y\;(xy=1)$. ¿Qué cambia si el dominio de $x$ es $\mathbb R\setminus\{0\}$?

**50.** Sobre $\mathbb R$, decide (a) $\exists y\forall x\;(xy=x)$; (b) $\forall x\exists y\;(xy=x)$.

**51.** Explica por qué $\forall x\forall y\,P(x,y)$ puede reordenarse como $\forall y\forall x\,P(x,y)$, y análogamente para dos existenciales, mientras que el intercambio $\forall x\exists y\leftrightarrow\exists y\forall x$ no es válido en general.

**52.** En el dominio $D=\{1,2\}$, sea $R(x,y)$ la relación “$x=y$”. Decide $\forall x\exists y\,R(x,y)$ y $\exists y\forall x\,R(x,y)$.

### I — Dependencia y elección de testigos

**53.** Para $\forall x\in\mathbb R\exists y\in\mathbb R\;(y=2x)$, da una elección de testigo y explica su dependencia.

**54.** Explica por qué en $\forall x\in\mathbb R\exists y\in\mathbb R\;(y>x)$ no puede usarse un único $y$ fijo para todos los $x$, aunque la afirmación sea verdadera.

**55.** Interpreta la dependencia en $\forall n\in\mathbb Z\exists m\in\mathbb Z\;(m=n^2)$.

**56.** En $\exists m\in\mathbb Z\forall n\in\mathbb Z\;(m+n=n)$, encuentra el testigo y explica por qué debe ser fijo.

**57.** ¿Implica $\forall x\exists y\,R(x,y)$ que para cada $x$ haya exactamente un $y$ con $R(x,y)$? Justifica.

**58.** Sea $M(p,q)$ el predicado “$q$ es madre de $p$”. Traduce y compara: (a) “toda persona tiene alguna madre”; (b) “existe una persona que es madre de todas las personas”.

### J — Existencia única

**59.** Decide $\exists!x\in\mathbb R\;(x+3=5)$ y justifica existencia y unicidad.

**60.** Decide $\exists!n\in\mathbb Z\;(2n=6)$.

**61.** Decide $\exists!x\in\mathbb R\;(x^2=4)$.

**62.** Expande $\exists!x\,P(x)$ usando sólo $\exists$, $\forall$, $\land$, $\Rightarrow$ e igualdad.

### K — Traducción bidireccional

**63.** Formaliza: “Todo entero tiene un entero mayor”.

**64.** Formaliza: “Entre un entero $n$ y su sucesor $n+1$ no existe ningún entero”.

**65.** Formaliza: “Existe un real positivo cuyo cuadrado es menor que él mismo”.

**66.** Formaliza: “No todo número real es positivo”.

**67.** Traduce a lenguaje verbal: $\forall n\in\mathbb Z\;[O(n)\Rightarrow O(n^2)]$, donde $O(k)$ significa “$k$ es impar”.

**68.** Traduce a lenguaje verbal: $\exists m\in\mathbb Z\;\forall n\in\mathbb Z\;(m+n=n)$.

### L — Diagnóstico y síntesis

**69.** Un estudiante niega $\forall x\in\mathbb R\;(x^2\ge0)$ escribiendo $\forall x\in\mathbb R\;(x^2<0)$. Localiza el primer error y repara la negación.

**70.** Un estudiante traduce “para cada estudiante hay un libro que ese estudiante eligió” como $\exists b\forall e\,E(e,b)$. Explica el cambio de significado y corrige.

**71.** Sobre $\mathbb R$, decide la verdad de: (a) $\forall x\exists y\;(x+y=0)$; (b) $\exists y\forall x\;(x+y=0)$; (c) $\forall x\forall y\;(x+y=0)$; (d) $\exists x\exists y\;(x+y=0)$. Niega además la afirmación (a).

**72.** Analiza la afirmación: “Para todo real $x$ existe un único real $y$ tal que $2y+x=0$”. (a) Escríbela simbólicamente; (b) decide su verdad; (c) identifica la dependencia de $y$; (d) escribe su negación sin usar $\exists!$.

***

#### M — Problemas tipo prueba

Los siguientes ejercicios están pensados como problemas de evaluación escrita. Exigen desarrollo completo, control del alcance de los cuantificadores y justificación explícita de testigos, contraejemplos o dependencias.

**73.** Sobre $\mathbb R$, analiza las cuatro afirmaciones siguientes. Para cada una: (i) decide si es verdadera o falsa; (ii) si es verdadera, da una regla explícita para elegir el testigo; (iii) si es falsa, exhibe una contradicción o un contraejemplo; (iv) explica qué cambia al invertir el orden de los cuantificadores.

(a) $\forall x\in\mathbb R\setminus\{0\}\;\exists y\in\mathbb R\;(xy=1)$.

(b) $\exists y\in\mathbb R\;\forall x\in\mathbb R\setminus\{0\}\;(xy=1)$.

(c) $\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x)$.

(d) $\exists y\in\mathbb R\;\forall x\in\mathbb R\;(y>x)$.

**74.** Considera la afirmación

$$
\forall x\in\mathbb R\;\Big[x\ge0\Rightarrow\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big].
$$

(a) Exprésala en lenguaje natural.  
(b) Négala paso a paso hasta obtener una fórmula en la que la negación actúe sólo sobre relaciones atómicas.  
(c) Decide la verdad de la afirmación original y de su negación.  
(d) Explica por qué cambiar sólo $\forall$ por $\exists$ no produce todavía la negación correcta.

**75.** Estudia la afirmación

$$
\forall x\in\mathbb R\;\exists!y\in\mathbb R\;(3y-2=x).
$$

(a) Expande $\exists!$ usando únicamente $\exists$, $\forall$, igualdad e implicación.  
(b) Demuestra existencia y unicidad para un $x$ arbitrario.  
(c) Escribe una negación equivalente que exprese explícitamente las dos maneras en que puede fallar la unicidad existencial: inexistencia o existencia de dos testigos distintos.  
(d) Compara con $\exists!y\in\mathbb R\;\forall x\in\mathbb R\;(3y-2=x)$ y decide su valor de verdad.

**76.** Sobre $\mathbb Z$, compara

$$
A:\quad \forall m\;\exists n\;\forall k\;(k\ge n\Rightarrow k>m)
$$

y

$$
B:\quad \exists n\;\forall m\;\forall k\;(k\ge n\Rightarrow k>m).
$$

(a) Decide la verdad de $A$ y construye un testigo $n$ en función de $m$.  
(b) Decide la verdad de $B$ y da un contraejemplo que funcione para cualquier candidato $n$.  
(c) Niega $A$ empujando la negación hasta la relación atómica.  
(d) Explica en una frase qué dependencia permite $A$ y prohíbe $B$.

**77.** Para un dominio $D$, considera

$$
S(D):\quad \forall x\in D\;\exists y\in D\;(y^2=x^2+1).
$$

(a) Decide si $S(\mathbb R)$ es verdadera y justifica una elección de $y$ para cada $x$.  
(b) Decide si $S(\mathbb Z)$ es verdadera. Si es falsa, encuentra el contraejemplo más simple que puedas.  
(c) Escribe la negación de $S(\mathbb Z)$ sin dejar una negación delante de un cuantificador.  
(d) Explica por qué la misma fórmula sintáctica expresa afirmaciones diferentes al cambiar el dominio.

**78.** Sean $E$ el conjunto de estudiantes, $P$ el conjunto de problemas y $S(e,p)$ el predicado “el estudiante $e$ resolvió el problema $p$”. Formaliza la frase:

> Todo estudiante resolvió al menos un problema que ningún otro estudiante resolvió.

(a) Escribe una fórmula cuantificada completa.  
(b) Niega tu fórmula y lleva la negación hasta los predicados atómicos.  
(c) Traduce la negación obtenida nuevamente al castellano.  
(d) Explica por qué mover el cuantificador $\exists p$ delante de $\forall e$ cambia el significado.

**79.** Considera la fórmula abierta

$$
F(y,z):\quad \forall x\,[P(x,y)\Rightarrow\exists y\,Q(x,y,z)].
$$

(a) Identifica todas las apariciones libres y ligadas de variables.  
(b) Renombra la variable ligada del cuantificador existencial para eliminar la reutilización del símbolo $y$ sin cambiar el significado.  
(c) Explica por qué renombrar ingenuamente el $\forall x$ como $\forall y$ puede capturar una variable que antes era libre.  
(d) Forma la clausura universal de la fórmula corregida.  
(e) Niega esa clausura universal hasta obtener una fórmula donde la negación actúe sólo sobre $Q$.

**80.** Analiza la afirmación

$$
\forall x\in\mathbb R\;\exists!y\in\mathbb R\;
\Big[y>x\land\forall z\in\mathbb R\,(z>x\Rightarrow y\le z)\Big].
$$

(a) Traduce cuidadosamente la afirmación al castellano.  
(b) Decide si es verdadera o falsa.  
(c) Si suponemos que un $y$ satisface la condición para cierto $x$, construye explícitamente un real $z$ que destruya esa posibilidad.  
(d) Explica si el fracaso está en la existencia, en la unicidad o en ambas.  
(e) Escribe en lenguaje natural una negación exacta de la afirmación original.

# Soluciones razonadas

Las soluciones forman parte del capítulo canónico. En los ejercicios de traducción puede haber variantes lingüísticas equivalentes; lo esencial es conservar dominio, cuantificadores, alcance y dependencia.

### Soluciones — A — Predicados y dominios

**Solución 1.** (a) $x+1$ es una expresión: representa un número una vez fijado $x$. (b) $x+1=5$ es un predicado abierto porque su verdad depende de $x$. (c) $4+1=5$ es una proposición y es verdadera. (d) “$n$ es par” es un predicado abierto. (e) “$6$ es par” es una proposición verdadera.

**Solución 2.** En $\mathbb Z$ no existe entero con cuadrado $2$, así que es falsa. En $\mathbb Q$ también es falsa: $\sqrt2$ no es racional. En $\mathbb R$ es verdadera, con testigos $\sqrt2$ y $-\sqrt2$. El ejercicio muestra que el dominio forma parte del significado.

**Solución 3.** Sobre $\{0,1\}$ es verdadera: hay sólo dos casos y ambos dan igualdad. Sobre $\mathbb Z$ también es verdadera, pues $x^2-x=x(x-1)$ y para todo entero $x$ el producto es no negativo: si $x\le0$, ambos factores son no positivos; si $x\ge1$, ambos son no negativos. Sobre $\mathbb R$ es falsa: $x=1/2$ produce $1/4<1/2$.

**Solución 4.** La expresión $1/x$ no está definida en $x=0$. Por tanto, si queremos usar $Q$ como predicado numérico debemos restringir el dominio a valores donde tenga sentido, por ejemplo $\mathbb R\setminus\{0\}$. No es correcto declarar simplemente $Q(0)$ falsa: la fórmula ni siquiera está definida allí.

**Solución 5.** Una elección es $D=\{-1,1\}$: ambos elementos satisfacen $x^2=1$. Para que sea falsa basta incluir un contraejemplo; por ejemplo $E=\{-1,0,1\}$, porque $0^2\ne1$.

**Solución 6.** Sobre $\mathbb Z$, el universal es falso porque $x=2$ da $4<4$, falso; el existencial es verdadero, por ejemplo con $x=0$. Sobre $\mathbb R$, el universal también es falso, por ejemplo con $x=3$, y el existencial es verdadero con $x=0$. Las dos afirmaciones conservan aquí su valor de verdad al cambiar de dominio, aunque sus conjuntos de testigos y contraejemplos cambian.

### Soluciones — B — Variables libres y ligadas

**Solución 7.** El cuantificador $\forall x$ liga a $x$ dentro de $P(x,y)$. La variable $y$ no tiene cuantificador y queda libre. Por ello la fórmula completa sigue siendo abierta respecto de $y$.

**Solución 8.** $y$ está ligada por $\exists y$ en todo el alcance entre corchetes. Las variables $x$ y $z$ quedan libres.

**Solución 9.** La primera es cerrada: todas las variables que aparecen, $x$ e $y$, están ligadas. La segunda no es cerrada porque $z$ queda libre. Su valor de verdad puede depender del valor o interpretación de $z$.

**Solución 10.** (a) Por ejemplo, sustituyendo $x=3$ obtenemos $3^2=9$, verdadera. (b) $\exists x\in\mathbb R\;(x^2=9)$, verdadera. (c) $\forall x\in\mathbb R\;(x^2=9)$, falsa. Las tres operaciones cierran la variable, pero producen proposiciones diferentes.

**Solución 11.** $x$ está ligada por el cuantificador universal y su alcance incluye tanto $P(x,y)$ como $R(x,z)$. $z$ está ligada por $\exists z$ dentro del consecuente. $y$ queda libre porque no aparece cuantificada.

**Solución 12.** Podemos escribir $\forall t\,P(t,y)$: $t$ reemplaza coherentemente a la variable ligada $x$, mientras $y$ permanece libre. En cambio, $\forall y\,P(y,y)$ hace que el cuantificador ligue también la posición que antes correspondía a la $y$ libre. Se produce captura de variable y el significado puede cambiar.

### Soluciones — C — Universales y contraejemplos

**Solución 13.** Es verdadera. No basta una lista de ejemplos; usamos el hecho general de que el cuadrado de todo real, y por tanto de todo entero, es no negativo. La justificación debe cubrir simultáneamente todos los enteros.

**Solución 14.** Toma $n=0$. Entonces $0^2>0$ es $0>0$, falso. Por tanto el universal queda refutado. También $n=1$ funciona como contraejemplo.

**Solución 15.** Basta un par de enteros impares cuya suma sea par. Por ejemplo, $1$ y $3$ son impares y $1+3=4$ es par. En realidad la afirmación correcta es la contraria: la suma de dos impares es par.

**Solución 16.** Comprobar finitos casos no demuestra una afirmación universal sobre todos los enteros no negativos. En $n=16$ se obtiene $16^2+16+17=289=17^2$, que no es primo. Éste es un contraejemplo decisivo.

**Solución 17.** No. La forma lógica es $\forall n\,[E(n)\Rightarrow E(n^2)]$. Para un entero impar, el antecedente $E(n)$ es falso; por tanto la implicación no falla allí. Un contraejemplo tendría que ser un entero par cuyo cuadrado fuera impar.

**Solución 18.** Toma $x=-2$. Se cumple $x^2=4>1$, pero $x=-2$ no es mayor que $1$. Por tanto el antecedente es verdadero y el consecuente falso: exactamente la forma necesaria para refutar una implicación universal.

### Soluciones — D — Existenciales y testigos

**Solución 19.** El entero $n=7$ sirve: $7^2=49$. Con un solo testigo válido queda demostrada la existencia. También $-7$ es testigo, lo que muestra que la afirmación no contiene unicidad.

**Solución 20.** Sería necesario $n=7/2$, pero $7/2$ no es entero. Por tanto ningún $n\in\mathbb Z$ satisface la ecuación y la afirmación es falsa.

**Solución 21.** Toma $x=1/2$. Entonces $0<1/2<1$ y $(1/2)^2=1/4<1/2$. Por tanto $x=1/2$ satisface simultáneamente todas las condiciones.

**Solución 22.** Elige $a=4$ y $b=1$. Entonces $a^2-b^2=16-1=15$. El par $(4,1)$ es un testigo para la existencia conjunta de $a$ y $b$.

**Solución 23.** Por ejemplo $n=1001$ es un testigo. No se necesita encontrar el “mejor” ni el menor testigo salvo que el enunciado lo exija; cualquier elemento del dominio que satisfaga el predicado basta para la existencia.

**Solución 24.** El cuantificador $\exists$ significa “existe al menos uno”, no “existe exactamente uno”. Tener dos testigos refuerza la existencia; no la contradice. La unicidad requeriría $\exists!x\,P(x)$.

### Soluciones — E — Negación de cuantificadores

**Solución 25.** La negación es $\exists x\in\mathbb R\;(x^2<0)$. Cambiamos $\forall$ por $\exists$ y negamos $x^2\ge0$, cuya negación sobre los reales es $x^2<0$.

**Solución 26.** La negación es $\forall n\in\mathbb Z\;(n^2\ne2)$. Cambiamos $\exists$ por $\forall$ y negamos la igualdad.

**Solución 27.** Primero: $\neg\forall n\,A(n)\equiv\exists n\,\neg A(n)$. Luego $\neg(E(n)\Rightarrow E(n^2))\equiv E(n)\land\neg E(n^2)$. La negación completa es $\exists n\in\mathbb Z\;[E(n)\land\neg E(n^2)]$.

**Solución 28.** La negación es $\forall x\in\mathbb R\;\neg(x>0\land x^2<1)$. Por De Morgan, queda $\forall x\in\mathbb R\;(x\le0\lor x^2\ge1)$.

**Solución 29.** Negamos desde afuera: $\exists x\in\mathbb R\;\neg\exists y\in\mathbb R\;(y>x)$. Luego cambia $\exists y$ por $\forall y$: $\exists x\in\mathbb R\;\forall y\in\mathbb R\;\neg(y>x)$. Por tanto, $\exists x\in\mathbb R\;\forall y\in\mathbb R\;(y\le x)$.

**Solución 30.** La negación es $\forall y\in\mathbb R\;\exists x\in\mathbb R\;\neg(y>x)$, es decir, $\forall y\in\mathbb R\;\exists x\in\mathbb R\;(y\le x)$.

**Solución 31.** “No todos” niega un universal: $\neg\forall n\in\mathbb Z\;(n>0)$. En forma positiva equivalente: $\exists n\in\mathbb Z\;(n\le0)$. Por ejemplo $0$ es un testigo.

**Solución 32.** Toma dominio $D=\{1,2\}$ y $P(x)$ = “$x=1$”. Entonces $\neg\forall x\,P(x)$ es verdadera porque no todos los elementos son $1$; concretamente $2$ falla. Pero $\forall x\,\neg P(x)$ es falsa porque $P(1)$ es verdadera. La primera dice “al menos uno falla”; la segunda, “todos fallan”.

### Soluciones — F — Cuantificación restringida

**Solución 33.** La forma conceptual es $\forall n\in D\;[n\in\mathbb Z\Rightarrow P(n)]$. Los elementos de $D$ que no son enteros no deben actuar como contraejemplos; por eso aparece una implicación.

**Solución 34.** La forma es $\exists n\in D\;[n\in\mathbb Z\land n^2=9]$. Un testigo debe cumplir a la vez pertenecer a $\mathbb Z$ y satisfacer la ecuación.

**Solución 35.** La negación es $\exists x\in A\;\neg P(x)$. En palabras: existe al menos un elemento de $A$ que no satisface $P$.

**Solución 36.** La negación es $\forall x\in A\;\neg P(x)$. En palabras: ningún elemento de $A$ satisface $P$.

**Solución 37.** La conjunción exige que **todo elemento del dominio mayor** sea simultáneamente entero y racional, lo cual es mucho más fuerte. La forma correcta es $\forall x\,[x\in\mathbb Z\Rightarrow x\in\mathbb Q]$: sólo los elementos que son enteros activan la condición.

**Solución 38.** En un existencial restringido necesitamos que el testigo sea entero **y** negativo. La implicación puede ser verdadera para un objeto no entero sin demostrar lo deseado. La forma correcta es $\exists x\,[x\in\mathbb Z\land x<0]$.

### Soluciones — G — Alcance y paréntesis

**Solución 39.** Las dos apariciones de $x$, en $P(x)$ y $Q(x)$, están dentro del alcance del cuantificador y por tanto ligadas. $R$ no contiene $x$.

**Solución 40.** Dentro de $P(x,y)$, $x$ está ligada por $\forall x$ y $y$ permanece libre. En $Q(y)$, $y$ también es libre. Por tanto la fórmula completa tiene a $y$ como variable libre.

**Solución 41.** En la primera, todas las apariciones de $x$ están ligadas y la fórmula puede ser cerrada. En la segunda, la $x$ de $Q(x)$ queda fuera del alcance del cuantificador, así que la expresión sigue abierta respecto de $x$. Cambiar los paréntesis cambia el alcance y, por tanto, la estructura lógica.

**Solución 42.** Podemos escribir, por ejemplo, $\exists t\,[t>y\land P(t)]$. El cuantificador y todas las apariciones ligadas de $x$ se sustituyen coherentemente por $t$; $y$ permanece libre.

**Solución 43.** La $y$ original era libre: podía representar un parámetro fijado externamente. Al renombrar $x$ como $y$, el cuantificador $\forall y$ pasa a ligar ambas posiciones. Esa variable libre queda capturada. La transformación no es una mera renominación, sino un cambio de estructura.

**Solución 44.** La primera afirma que cada $x$ satisface simultáneamente $P$ y $Q$. La segunda afirma que todos satisfacen $P$, pero deja $Q(x)$ como condición abierta sobre una $x$ libre. No son expresiones equivalentes ni tienen el mismo estatus lógico.

### Soluciones — H — Orden de cuantificadores

**Solución 45.** (a) Verdadera: dado $x$, elige $y=x+1$. (b) Falsa: si se propone un real fijo $y$, tomando $x=y+1$ obtenemos $y>x$ falso. El cambio de orden altera la dependencia permitida.

**Solución 46.** La primera es verdadera: para cada $x$, elige $y=x+1$. La segunda es falsa: un mismo $y$ no puede ser simultáneamente $x+1$ para todos los reales $x$; por ejemplo exigiría $y=1$ cuando $x=0$ y $y=2$ cuando $x=1$.

**Solución 47.** $\forall n\exists m\;(m=n+2)$ es verdadera: para cada $n$, toma $m=n+2$. $\exists m\forall n\;(m=n+2)$ es falsa: un entero fijo $m$ no puede valer $n+2$ para todos los enteros $n$.

**Solución 48.** Ambas son verdaderas. En (a), el testigo fijo $n=0$ funciona para todo $m$. En (b), para cada $m$ podemos elegir $n=0$; de hecho la elección no necesita depender de $m$. Que ambas sean verdaderas no significa que las formas lógicas sean equivalentes en general.

**Solución 49.** Sobre todo $\mathbb R$ es falsa: para $x=0$ no existe $y$ con $0\cdot y=1$. Si restringimos $x$ a $\mathbb R\setminus\{0\}$, es verdadera: dado $x\ne0$, elige $y=1/x$.

**Solución 50.** (a) Verdadera con $y=1$, pues $1\cdot x=x$ para todo real $x$. (b) También verdadera; incluso puede usarse el mismo $y=1$ para cada $x$. Este ejemplo recuerda que invertir cuantificadores puede cambiar el significado aunque ocasionalmente ambas afirmaciones resulten verdaderas.

**Solución 51.** Dos universales exigen que $P$ sea verdadera para todos los pares $(x,y)$; el orden en que recorremos los componentes no cambia esa exigencia. Dos existenciales sólo piden que exista algún par $(x,y)$ y el orden tampoco cambia eso. En cambio, $\forall x\exists y$ permite que $y$ dependa de $x$, mientras $\exists y\forall x$ exige un único $y$ fijo; por eso no son equivalentes en general.

**Solución 52.** $\forall x\exists y\,R(x,y)$ es verdadera: para $x=1$ elige $y=1$, y para $x=2$ elige $y=2$. En cambio, $\exists y\forall x\,R(x,y)$ es falsa: ningún único $y$ es igual simultáneamente a $1$ y a $2$.

### Soluciones — I — Dependencia y elección de testigos

**Solución 53.** La elección $y=2x$ funciona. El testigo no es un número fijo: depende del valor de $x$ que haya sido dado. Esa dependencia es permitida porque $\exists y$ aparece después de $\forall x$.

**Solución 54.** Si fijamos cualquier real $y$, podemos tomar $x=y+1$ y entonces $y>x$ falla. La afirmación sigue siendo verdadera porque permite elegir un $y$ nuevo después de conocer cada $x$, por ejemplo $y=x+1$.

**Solución 55.** Para cada entero $n$ podemos elegir el testigo $m=n^2$. En general cambia cuando cambia $n$. La afirmación no promete un único entero $m$ que sea igual al cuadrado de todos los enteros.

**Solución 56.** El testigo es $m=0$. Como $\exists m$ aparece primero, debemos elegir un solo entero antes de considerar los distintos $n$. Ese mismo $m=0$ funciona para todos porque $0+n=n$.

**Solución 57.** No. El cuantificador existencial sólo garantiza al menos un testigo. Puede haber varios. Por ejemplo, sobre $\mathbb R$, si $R(x,y)$ significa $y>x$, para cada $x$ hay infinitos valores de $y$ posibles. La unicidad requeriría una condición adicional.

**Solución 58.** (a) $\forall p\exists q\,M(p,q)$. El testigo $q$ puede depender de $p$. (b) $\exists q\forall p\,M(p,q)$. Aquí se exige una sola persona $q$ que satisfaga la relación con todas las personas. Las frases no tienen la misma estructura.

### Soluciones — J — Existencia única

**Solución 59.** Existe: $x=2$ satisface $2+3=5$. Es único porque si $x+3=5$, restando $3$ en ambos lados se obtiene necesariamente $x=2$. Por tanto la afirmación es verdadera.

**Solución 60.** Existe el entero $n=3$. Si $2n=6$, dividir por $2$ obliga a $n=3$, así que no hay otro entero posible. La afirmación es verdadera.

**Solución 61.** Es falsa. Hay existencia, pues $x=2$ funciona, pero también $x=-2$. Como hay dos testigos distintos, falla la unicidad.

**Solución 62.** Una expansión estándar es $\exists x\,[P(x)\land\forall y\,(P(y)\Rightarrow y=x)]$. La primera parte afirma existencia; la segunda fuerza que cualquier otro candidato que cumpla $P$ coincida con el testigo $x$.

### Soluciones — K — Traducción bidireccional

**Solución 63.** $\forall n\in\mathbb Z\;\exists m\in\mathbb Z\;(m>n)$. El orden es universal-existencial porque el entero mayor puede depender del entero inicial.

**Solución 64.** Una forma es $\forall n\in\mathbb Z\;\neg\exists m\in\mathbb Z\;(n<m<n+1)$. Equivalentemente, $\forall n\in\mathbb Z\;\forall m\in\mathbb Z\;\neg(n<m<n+1)$.

**Solución 65.** $\exists x\in\mathbb R\;(x>0\land x^2<x)$. También podría escribirse $\exists x\in\mathbb R\;(0<x<1)$ si ya se ha justificado la equivalencia pertinente para positivos, pero la traducción directa conserva exactamente el enunciado dado.

**Solución 66.** $\neg\forall x\in\mathbb R\;(x>0)$, equivalente a $\exists x\in\mathbb R\;(x\le0)$.

**Solución 67.** “Para todo entero $n$, si $n$ es impar, entonces $n^2$ es impar.” También puede decirse: “el cuadrado de todo entero impar es impar”.

**Solución 68.** “Existe un entero $m$ tal que, para todo entero $n$, se cumple $m+n=n$.” La estructura exige un mismo $m$ para todos los $n$; concretamente ese entero es $0$.

### Soluciones — L — Diagnóstico y síntesis

**Solución 69.** El primer error es conservar el cuantificador universal. Al negar un universal debe aparecer un existencial. La forma correcta es $\exists x\in\mathbb R\;(x^2<0)$. Luego observamos que esta negación es falsa, coherente con la verdad del enunciado original.

**Solución 70.** La traducción propuesta dice que existe **un mismo libro** $b$ elegido por todos los estudiantes. La frase original permite que cada estudiante haya elegido un libro distinto. La forma adecuada es $\forall e\exists b\,E(e,b)$.

**Solución 71.** (a) Verdadera: dado $x$, toma $y=-x$. (b) Falsa: un único $y$ no puede satisfacer $x+y=0$ para todos los reales $x$; por ejemplo, $x=0$ exige $y=0$ y $x=1$ exige $y=-1$. (c) Falsa: basta $x=y=1$, pues $1+1\ne0$. (d) Verdadera: por ejemplo $x=0,y=0$. La negación de (a) es $\exists x\forall y\;(x+y\ne0)$, que es falsa porque para cualquier $x$ siempre podemos elegir $y=-x$.

**Solución 72.** (a) $\forall x\in\mathbb R\;\exists!y\in\mathbb R\;(2y+x=0)$. (b) Es verdadera: dado $x$, la ecuación obliga a $y=-x/2$, que es real. (c) El testigo depende de $x$ mediante la regla $y=-x/2$; no hay un único $y$ global para todos los $x$. (d) Expandiendo unicidad, el original dice que para todo $x$ existe un $y$ con $2y+x=0$ y cualquier $z$ que también satisfaga $2z+x=0$ debe ser igual a $y$. Su negación puede expresarse conceptualmente como: $\exists x\in\mathbb R$ tal que **o bien** no existe ningún $y$ con $2y+x=0$, **o bien** existen dos reales distintos $y,z$ que satisfacen ambos la ecuación. Simbólicamente:

$$
\exists x\in\mathbb R\;\Big([\forall y\in\mathbb R\;(2y+x\ne0)]\lor[\exists y,z\in\mathbb R\;(y\ne z\land 2y+x=0\land 2z+x=0)]\Big).
$$

En este caso la negación es falsa porque para cada $x$ existe exactamente el único valor $-x/2$.

***

### Soluciones — M — Problemas tipo prueba

**Solución 73.**

(a) Es verdadera. Dado $x\ne0$, basta elegir $y=1/x$. Entonces $xy=1$. El testigo depende de $x$.

(b) Es falsa. Si existiera un real fijo $y$ tal que $xy=1$ para todo $x\ne0$, al tomar $x=1$ obtendríamos $y=1$, mientras que con $x=2$ obtendríamos $y=1/2$. Contradicción.

(c) Es verdadera. Para cada $x$ podemos tomar $y=x+1$, y entonces $y>x$.

(d) Es falsa. Si existiera un real $y$ mayor que todo real $x$, tomando $x=y+1$ tendríamos $y>y+1$, contradicción.

En (a) y (c), el existencial está dentro del alcance del universal: el testigo puede variar con la entrada. En (b) y (d), el testigo debe fijarse antes y funcionar para todos los valores universales.

**Solución 74.**

(a) Dice: “Todo real no negativo posee una raíz cuadrada real no negativa”.

(b)

$$
\begin{aligned}
&\neg\forall x\in\mathbb R\;\Big[x\ge0\Rightarrow\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\neg\Big[x\ge0\Rightarrow\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\Big[x\ge0\land\neg\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\Big[x\ge0\land\forall y\in\mathbb R\;\neg(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\Big[x\ge0\land\forall y\in\mathbb R\;(y<0\lor y^2\ne x)\Big].
\end{aligned}
$$

(c) La afirmación original es verdadera: si $x\ge0$, existe $y=\sqrt{x}\ge0$ y $y^2=x$. Por tanto su negación es falsa.

(d) Cambiar sólo $\forall$ por $\exists$ niega únicamente la capa externa. También deben negarse la implicación y el existencial interior.

**Solución 75.**

(a)

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R\;
\Big[(3y-2=x)\land
\forall z\in\mathbb R\,(3z-2=x\Rightarrow z=y)\Big].
$$

(b) Fijado $x$, la ecuación obliga a $y=(x+2)/3$, que es real. Si $z$ también satisface $3z-2=x$, entonces $3z-2=3y-2$, de donde $z=y$. Hay existencia y unicidad.

(c) La negación expresa que existe algún $x$ para el cual o no hay solución o hay dos soluciones distintas:

$$
\exists x\in\mathbb R\;
\Big(
[\forall y\in\mathbb R\;(3y-2\ne x)]
\lor
[\exists y,z\in\mathbb R\;(y\ne z\land 3y-2=x\land 3z-2=x)]
\Big).
$$

(d) $\exists!y\,\forall x\,(3y-2=x)$ es falsa: fijado $y$, $3y-2$ es un solo real y no puede coincidir con todos los reales $x$.

**Solución 76.**

(a) $A$ es verdadera. Dado $m$, elige $n=m+1$. Si $k\ge n$, entonces $k\ge m+1>m$.

(b) $B$ es falsa. Para cualquier candidato fijo $n$, toma $m=n$ y $k=n$. Entonces $k\ge n$ es verdadera, pero $k>m$ se convierte en $n>n$, falsa.

(c)

$$
\begin{aligned}
\neg A
&\equiv \exists m\;\forall n\;\exists k\;\neg(k\ge n\Rightarrow k>m)\\
&\equiv \exists m\;\forall n\;\exists k\;(k\ge n\land k\le m).
\end{aligned}
$$

(d) En $A$, $n$ puede depender de $m$. En $B$, $n$ debe elegirse una sola vez y funcionar para todos los $m$.

**Solución 77.**

(a) Es verdadera en $\mathbb R$: dado $x$, elige $y=\sqrt{x^2+1}$.

(b) Es falsa en $\mathbb Z$. Para $x=1$ se exigiría $y^2=2$, imposible para un entero.

(c)

$$
\exists x\in\mathbb Z\;\forall y\in\mathbb Z\;(y^2\ne x^2+1).
$$

El valor $x=1$ es un testigo.

(d) Los cuantificadores recorren objetos distintos según el dominio. El mismo patrón formal puede ser verdadero en $\mathbb R$ y falso en $\mathbb Z$ porque cambian los testigos permitidos.

**Solución 78.**

(a)

$$
\forall e\in E\;\exists p\in P\;
\Big[
S(e,p)\land
\forall e'\in E\;(e'\ne e\Rightarrow\neg S(e',p))
\Big].
$$

(b)

$$
\begin{aligned}
&\neg\forall e\in E\;\exists p\in P\;
\Big[S(e,p)\land\forall e'\in E\;(e'\ne e\Rightarrow\neg S(e',p))\Big]\\
&\equiv
\exists e\in E\;\forall p\in P\;
\Big[\neg S(e,p)\lor
\exists e'\in E\;(e'\ne e\land S(e',p))\Big].
\end{aligned}
$$

(c) “Existe un estudiante tal que, para cada problema, o bien ese estudiante no lo resolvió, o bien algún otro estudiante también lo resolvió.” Es decir, existe un estudiante que no posee ningún problema resuelto exclusivamente por él.

(d) Mover $\exists p$ delante de $\forall e$ obliga a escoger un mismo problema para todos los estudiantes. La frase original permite que el problema dependa del estudiante.

**Solución 79.**

(a) En $\forall x\,[P(x,y)\Rightarrow\exists y\,Q(x,y,z)]$, $x$ está ligada por $\forall$. La $y$ de $P(x,y)$ es libre; la $y$ de $Q(x,y,z)$ está ligada por $\exists$; $z$ es libre.

(b) Una renominación segura es

$$
\forall x\,[P(x,y)\Rightarrow\exists t\,Q(x,t,z)].
$$

(c) Si se reemplaza ingenuamente $\forall x$ por $\forall y$, la $y$ libre que aparece en $P(x,y)$ quedaría bajo el alcance del nuevo cuantificador. Esa captura cambia el significado.

(d) Una clausura universal es

$$
\forall y\;\forall z\;\forall x\;
[P(x,y)\Rightarrow\exists t\,Q(x,t,z)].
$$

(e)

$$
\begin{aligned}
&\neg\forall y\forall z\forall x\,[P(x,y)\Rightarrow\exists t\,Q(x,t,z)]\\
&\equiv
\exists y\exists z\exists x\,[P(x,y)\land\neg\exists t\,Q(x,t,z)]\\
&\equiv
\exists y\exists z\exists x\,[P(x,y)\land\forall t\,\neg Q(x,t,z)].
\end{aligned}
$$

**Solución 80.**

(a) Afirma que para todo real $x$ existe un único real $y$ que es estrictamente mayor que $x$ y que es menor o igual que cualquier otro real estrictamente mayor que $x$. Es decir, afirma que todo real tiene un menor real estrictamente mayor que él.

(b) Es falsa.

(c) Fijemos $x$ y supongamos $y>x$. Toma

$$
z=\frac{x+y}{2}.
$$

Entonces $x<z<y$. Como $z>x$, la condición universal exigiría $y\le z$, contradicción.

(d) Falla ya la existencia: para ningún $x$ existe un $y$ con la propiedad. Por tanto la unicidad ni siquiera llega a entrar en juego.

(e) Una negación exacta es: “Existe un real $x$ para el cual no existe exactamente un real $y$ que sea el menor real estrictamente mayor que $x$”. De hecho hemos probado algo más fuerte: para todo $x$ no existe ninguno.

***

## Autoevaluación de salida

Antes de continuar a C7, deberías poder responder afirmativamente:

- ¿distingo una expresión de un predicado y de una proposición?
- ¿puedo declarar el dominio relevante?
- ¿identifico variables libres y ligadas?
- ¿leo $\forall$, $\exists$ y $\exists!$ sin perder su alcance?
- ¿sé que un contraejemplo refuta un universal?
- ¿sé que un testigo establece una existencia?
- ¿puedo negar cuantificadores cambiando $\forall\leftrightarrow\exists$ y negando el contenido interno?
- ¿distingo $\forall x\exists y$ de $\exists y\forall x$?
- ¿puedo explicar cuándo un testigo depende de una variable previa?
- ¿puedo traducir afirmaciones de complejidad media en ambos sentidos?

Si alguna respuesta es negativa, vuelve primero a las secciones 6.7, 6.9–6.11 y a los ejercicios de los bloques E, G, H y L. Son los puntos de mayor transferencia del capítulo.
