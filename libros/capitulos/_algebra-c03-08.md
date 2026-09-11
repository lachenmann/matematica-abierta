## §8. Traducir entre prosa y símbolos

Los símbolos lógicos no sustituyen al lenguaje matemático ordinario.

Lo hacen **más preciso**. Una fórmula como:

$$
\forall x\,(P(x)\Rightarrow Q(x))
$$

debe poder leerse en castellano sin perder nada de su estructura.

Y una frase como:

> «Todo objeto que cumple $P$ cumple también $Q$»

debe poder convertirse en una fórmula sin cambiar su significado.

Traducir bien exige conservar, al menos, cuatro elementos:

1. **el dominio**;
2. **los cuantificadores**;
3. **el orden y el alcance**;
4. **los conectivos que relacionan las condiciones**.

Una traducción que cambia alguno de estos elementos puede producir una afirmación matemática diferente.

Por tanto:

$$
\boxed{
\text{traducir}
\neq
\text{sustituir palabras por símbolos}.
}
$$

Traducir es reconstruir la **estructura lógica** de una afirmación.

---

### 8.1 Antes de traducir: fijar el dominio

Consideremos la frase:

> «Todo número tiene una propiedad $P$».

La palabra:

> «número»

es demasiado amplia si el contexto no ha dicho qué clase de números estamos considerando.

En una discusión podríamos estar trabajando con enteros. En otra, con racionales.

En otra, con reales. En este capítulo no escribiremos todavía cuantificadores restringidos mediante pertenencia.

Por eso declararemos primero el dominio. Por ejemplo:

> **Dominio:** números enteros.

Después escribiremos:

$$
\forall x\,P(x).
$$

El dominio no desaparece al pasar a símbolos. Permanece fijado por el contexto.

---

### 8.2 «Todo $P$ es $Q$»: aparece una implicación

Supongamos que el dominio ya está fijado y que:

$$
P(x)
$$

significa:

> «$x$ tiene la propiedad $P$»,

mientras:

$$
Q(x)
$$

significa:

> «$x$ tiene la propiedad $Q$».

Queremos traducir:

> «Todo objeto que cumple $P$ cumple $Q$».

La estructura no es:

$$
\forall x\,(P(x)\land Q(x)).
$$

Esa fórmula diría que **todos los objetos del dominio** cumplen simultáneamente $P$ y $Q$.

La frase original dice otra cosa:

> si un objeto cumple $P$, entonces cumple $Q$.

Por tanto:

$$

\forall x\,(P(x)\Rightarrow Q(x)).

$$

La implicación es esencial. El patrón es:

$$
\boxed{
\text{«todo }P\text{ es }Q\text{»}
\longrightarrow
\forall x\,(P(x)\Rightarrow Q(x)).
}
$$

---

### 8.3 «Algún $P$ es $Q$»: aparece una conjunción

Ahora traduzcamos:

> «Algún objeto cumple $P$ y cumple $Q$».

Necesitamos afirmar que existe al menos un valor para el cual las dos condiciones son verdaderas.

Por tanto:

$$

\exists x\,(P(x)\land Q(x)).

$$

Aquí la conjunción cumple un papel distinto del que tenía la implicación en el caso universal.

El patrón es:

$$
\boxed{
\text{«algún }P\text{ es }Q\text{»}
\longrightarrow
\exists x\,(P(x)\land Q(x)).
}
$$

Comparemos:

$$
\forall x\,(P(x)\Rightarrow Q(x))
$$

con:

$$
\exists x\,(P(x)\land Q(x)).
$$

La primera formula una condición universal. La segunda afirma la existencia de un caso donde ambas propiedades se cumplen.

---

### 8.4 Traducir «ningún»

La frase:

> «Ningún objeto que cumple $P$ cumple $Q$»

puede expresarse de más de una forma equivalente. Una opción es:

$$
\forall x\,(P(x)\Rightarrow\neg Q(x)).
$$

Se lee:

> «Para todo $x$, si $x$ cumple $P$, entonces no cumple $Q$».

Otra opción es decir que no existe ningún caso que cumpla simultáneamente ambas propiedades:

$$
\neg\exists x\,(P(x)\land Q(x)).
$$

Por las leyes ya demostradas en [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007), ambas formulaciones expresan la misma exclusión.

Así:

$$

\text{«ningún }P\text{ es }Q\text{»}

$$

puede representarse como:

$$

\forall x\,(P(x)\Rightarrow\neg Q(x))

$$

o, equivalentemente:

$$

\neg\exists x\,(P(x)\land Q(x)).

$$

La elección entre ambas formas puede depender de cuál sea más clara en el contexto.

---

### 8.5 Traducir «no todos»

Consideremos:

> «No todos los objetos cumplen $P$».

La traducción inmediata es:

$$
\neg\forall x\,P(x).
$$

Pero [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007) nos permite escribir una forma equivalente:

$$
\exists x\,\neg P(x).
$$

Por tanto:

$$

\text{«no todos cumplen }P\text{»}
\longleftrightarrow
\exists x\,\neg P(x).

$$

La frase **no** significa:

$$
\forall x\,\neg P(x).
$$

Eso diría:

> «Ninguno cumple $P$».

La diferencia lingüística corresponde exactamente a la diferencia lógica estudiada en §5.

---

### 8.6 Dos cuantificadores: preservar el orden

Supongamos ahora que:

$$
R(x,y)
$$

expresa una condición entre dos variables. La frase:

> «Para cada valor de $x$, existe algún valor de $y$ para el cual se cumple $R(x,y)$»

se traduce:

$$
\boxed{
\forall x\,\exists y\,R(x,y).
}
$$

En cambio:

> «Existe algún valor de $y$ tal que, para cada valor de $x$, se cumple $R(x,y)$»

se traduce:

$$
\boxed{
\exists y\,\forall x\,R(x,y).
}
$$

Ya sabemos que estas dos fórmulas no son equivalentes en general.

Por eso, al traducir una frase con varios cuantificadores:

$$
\boxed{
\text{el orden de la prosa debe conservarse en la fórmula}.
}
$$

No podemos decidir el orden por comodidad tipográfica.

---

### 8.7 El alcance también debe conservarse

Consideremos ahora una proposición $Q$ que no depende de $x$.

Comparemos las frases:

> «Si todos los valores de $x$ cumplen $P(x)$, entonces $Q$».

y:

> «Para todo valor de $x$, si $P(x)$ se cumple, entonces $Q$».

La primera tiene la estructura:

$$
(\forall x\,P(x))\Rightarrow Q.
$$

La segunda tiene la estructura:

$$
\forall x\,(P(x)\Rightarrow Q).
$$

Los mismos símbolos aparecen en ambas expresiones, pero el alcance del cuantificador es distinto.

En la primera, el universal forma parte del antecedente completo de la implicación:

$$
\forall x\,P(x).
$$

En la segunda, el universal gobierna toda la implicación $P(x)\Rightarrow Q$ No podemos mover los paréntesis sin analizar el significado.

Por ejemplo, si $Q$ es falsa y el dominio contiene dos valores, uno que satisface $P$ y otro que no la satisface, entonces $(\forall x\,P(x))\Rightarrow Q$ es verdadera, porque su antecedente es falso; en cambio:

$$
\forall x\,(P(x)\Rightarrow Q)
$$

es falsa, porque para el valor que satisface $P$ obtenemos una implicación con antecedente verdadero y consecuente falso.

Así:

$$
\boxed{
\text{preservar el alcance también es preservar el significado}.
}
$$

---

### 8.8 Símbolos hacia prosa: no leer mecánicamente

Consideremos:

$$
\forall x\,(P(x)\Rightarrow Q(x)).
$$

Una lectura demasiado mecánica sería:

> «Para todo $x$, $P(x)$ implica $Q(x)$».

No es incorrecta, pero puede ocultar el contenido. Una lectura matemática más natural es:

> «Todo objeto del dominio que cumple $P$ cumple también $Q$».

De manera semejante:

$$
\exists x\,(P(x)\land Q(x))
$$

puede leerse:

> «Existe al menos un objeto del dominio que cumple tanto $P$ como $Q$».

La traducción hacia prosa debe conservar la estructura lógica, pero puede utilizar una redacción natural.

---

### 8.9 Un procedimiento de traducción

Ante una frase matemática, conviene seguir este orden.

#### Paso 1 — Identificar el dominio

¿De qué objetos estamos hablando?

#### Paso 2 — Identificar las variables

¿Qué puede variar?

#### Paso 3 — Localizar las palabras cuantificacionales

Por ejemplo:

- todo;
- cada;
- algún;
- existe;
- ningún;
- no todos.

#### Paso 4 — Identificar los conectivos

Buscar estructuras como:

- «y»;
- «o»;
- «si..., entonces...»;
- «no».

#### Paso 5 — Determinar el alcance

¿Qué parte de la afirmación queda gobernada por cada cuantificador o conectivo?

#### Paso 6 — Preservar el orden

Especialmente cuando aparecen varios cuantificadores.

#### Paso 7 — Volver a leer la fórmula en prosa

La prueba final de una traducción es preguntar:

> «¿La fórmula que escribí vuelve a decir exactamente la frase original?»

Podemos resumir:

$$
\boxed{
\text{prosa}
\longrightarrow
\text{estructura}
\longrightarrow
\text{símbolos}
\longrightarrow
\text{prosa}.
}
$$

---

### 8.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0028}
**Ejemplo — Traducir en ambos sentidos**
:::

Trabajaremos sobre un dominio previamente fijado. Sean:

$$
P(x),
\qquad
Q(x),
\qquad
R(x,y)
$$

predicados.

#### A. «Todo objeto que cumple $P$ cumple $Q$»

La palabra:

> «todo»

indica cuantificación universal. La estructura:

> «que cumple $P$ ... cumple $Q$»

se expresa mediante una implicación. Por tanto:

$$
\boxed{
\forall x\,(P(x)\Rightarrow Q(x)).
}
$$

#### B. «Algún objeto cumple $P$ y $Q$»

La palabra:

> «algún»

indica cuantificación existencial. Debemos encontrar un mismo valor de $x$ para el cual se cumplan ambas condiciones.

Por tanto:

$$
\boxed{
\exists x\,(P(x)\land Q(x)).
}
$$

#### C. «Ningún objeto que cumple $P$ cumple $Q$»

Podemos escribir:

$$
\boxed{
\forall x\,(P(x)\Rightarrow\neg Q(x)).
}
$$

Equivalentemente:

$$
\boxed{
\neg\exists x\,(P(x)\land Q(x)).
}
$$

#### D. «No todos los objetos cumplen $P$»

Escribimos $\neg\forall x\,P(x)$. Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\boxed{
\exists x\,\neg P(x).
}
$$

#### E. «Para cada $x$, existe algún $y$ tal que $R(x,y)$»

El orden verbal es:

> «para cada $x$» → «existe algún $y$».

Por tanto:

$$
\boxed{
\forall x\,\exists y\,R(x,y).
}
$$

#### F. «Existe algún $y$ tal que, para cada $x$, se cumple $R(x,y)$»

Ahora el orden es el contrario:

> «existe algún $y$» → «para cada $x$».

Por tanto:

$$
\boxed{
\exists y\,\forall x\,R(x,y).
}
$$

Las fórmulas E y F utilizan los mismos símbolos, pero no dicen lo mismo en general.

#### G. Volver de símbolos a prosa

Consideremos:

$$
\forall x\,\exists y\,(P(x)\Rightarrow R(x,y)).
$$

Una lectura estructural es:

> «Para todo valor de $x$, existe al menos un valor de $y$ tal que, si $P(x)$ se cumple, entonces $R(x,y)$ se cumple».

La traducción preserva:

- el universal exterior;
- el existencial interior;
- el orden;
- la implicación;
- el alcance de los cuantificadores.

---
## Ejercicios

### De una frase universal a símbolos {#apm-t1-c03-e0177}
El dominio está previamente fijado.

Sean:

$$
P(x)
$$

y:

$$
Q(x)
$$

predicados.

Traduce:

> «Todo objeto que cumple $P$ cumple también $Q$».

#### Solución


La palabra:

> «todo»

indica que debemos cuantificar universalmente.

La frase no afirma que todos los objetos cumplan $P$ y $Q$.

Afirma que **si** un objeto cumple $P$, **entonces** cumple $Q$.

Por tanto:

$$
\boxed{
\forall x\,(P(x)\Rightarrow Q(x)).
}
$$

---

### Una existencia con dos condiciones {#apm-t1-c03-e0178}
El dominio está previamente fijado.

Traduce:

> «Existe al menos un objeto que cumple $P$ y no cumple $Q$».

#### Solución


La expresión:

> «existe al menos un»

indica:

$$
\exists x.
$$

Para ese mismo valor de $x$ deben cumplirse simultáneamente:

$$
P(x)
$$

y:

$$
\neg Q(x).
$$

Por tanto:

$$
\boxed{
\exists x\,(P(x)\land\neg Q(x)).
}
$$

---

### De símbolos a prosa {#apm-t1-c03-e0179}
Lee en prosa:

$$
\neg\exists x\,(P(x)\land Q(x)).
$$

Después da una segunda formulación equivalente utilizando [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

#### Solución


Una lectura natural es:

> «No existe ningún objeto del dominio que cumpla simultáneamente $P$ y $Q$».

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,(P(x)\land Q(x))
\equiv
\forall x\,\neg(P(x)\land Q(x)).
$$

Por la ley de De Morgan de [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md):

$$
\neg(P(x)\land Q(x))
\equiv
\neg P(x)\lor\neg Q(x).
$$

Por tanto, también podemos escribir:

$$
\boxed{
\forall x\,(\neg P(x)\lor\neg Q(x)).
}
$$

En prosa:

> «Para todo objeto del dominio, o bien no cumple $P$, o bien no cumple $Q$».

---

### Por qué no podemos invertir los cuantificadores {#apm-t1-c03-e0180}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x+1.
$$

Una persona traduce:

> «Para cada entero $x$, existe un entero $y$ tal que $y=x+1$»

como:

$$
\exists y\,\forall x\,R(x,y).
$$

Explica con precisión cuál es el error.

#### Solución


La frase comienza:

> «Para cada entero $x$...»

Por tanto, el cuantificador exterior debe ser:

$$
\forall x.
$$

Después dice:

> «...existe un entero $y$...»

Por tanto, dentro de ese universal debe aparecer:

$$
\exists y.
$$

La traducción correcta es:

$$
\boxed{
\forall x\,\exists y\,R(x,y).
}
$$

La fórmula propuesta:

$$
\exists y\,\forall x\,R(x,y)
$$

cambia el orden y, con él, el significado.

La fórmula correcta permite elegir un $y$ distinto para cada $x$.

La fórmula incorrecta exige un único $y$ que funcione para todos los enteros $x$.

En este ejemplo, la primera es verdadera y la segunda es falsa.

---

### Una implicación dentro del alcance {#apm-t1-c03-e0181}
El dominio está previamente fijado.

Sean:

$$
P(x)
$$

y:

$$
R(x,y)
$$

predicados.

Traduce:

> «Para todo valor de $x$, si $P(x)$ se cumple, entonces existe al menos un valor de $y$ para el cual se cumple $R(x,y)$».

Explica el alcance de cada cuantificador.

#### Solución


El primer fragmento:

> «Para todo valor de $x$»

produce:

$$
\forall x.
$$

Después aparece una implicación:

> «si $P(x)$ se cumple, entonces...»

La consecuencia afirma:

> «existe al menos un valor de $y$ para el cual se cumple $R(x,y)$».

Por tanto, la traducción es:

$$
\boxed{
\forall x\,(P(x)\Rightarrow\exists y\,R(x,y)).
}
$$

El alcance de:

$$
\forall x
$$

es toda la implicación:

$$
P(x)\Rightarrow\exists y\,R(x,y).
$$

El alcance de:

$$
\exists y
$$

es:

$$
R(x,y).
$$

---

### Traducción bidireccional con dos cuantificadores {#apm-t1-c03-e0182}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad x+y=0.
$$

#### a)

Traduce a símbolos:

> «Para cada entero $x$, existe un entero $y$ cuya suma con $x$ es igual a cero».

#### b)

Decide si la afirmación es verdadera y explica su significado.

#### c)

Ahora lee en prosa:

$$
\exists y\,\forall x\,R(x,y).
$$

#### d)

Decide si esta segunda afirmación es verdadera.

#### e)

Explica qué información de la prosa debe conservarse necesariamente al traducir entre ambas direcciones.

#### Solución


#### a)

La frase comienza con:

> «Para cada entero $x$»

y después afirma:

> «existe un entero $y$».

Por tanto:

$$
\boxed{
\forall x\,\exists y\,(x+y=0).
}
$$

#### b)

La afirmación es verdadera.

Para cada entero $x$ podemos elegir:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

La fórmula dice que cada entero admite algún entero que, sumado con él, produce cero.

#### c)

La fórmula:

$$
\exists y\,\forall x\,R(x,y)
$$

se lee:

> «Existe un entero $y$ tal que, para todo entero $x$, se cumple $x+y=0$».

#### d)

La segunda afirmación es falsa.

Si existiera un entero fijo $y$ que cumpliera:

$$
x+y=0
$$

para todo entero $x$, debería funcionar tanto para:

$$
x=0
$$

como para:

$$
x=1.
$$

Del primer caso obtendríamos:

$$
y=0.
$$

Pero entonces el segundo exigiría:

$$
1+0=0,
$$

lo cual es falso.

#### e)

Al traducir debemos conservar necesariamente:

- el dominio;
- qué variables aparecen;
- qué cuantificador corresponde a cada variable;
- el orden de los cuantificadores;
- el alcance;
- la condición expresada por el predicado.

Cambiar alguno de esos elementos puede producir una afirmación distinta.

---

## Síntesis

Traducir entre prosa y símbolos es una operación estructural.

No basta con reconocer palabras aisladas. Debemos identificar:

$$

\text{dominio}
+
\text{variables}
+
\text{cuantificadores}
+
\text{orden}
+
\text{alcance}
+
\text{conectivos}.

$$

Algunos patrones importantes son:

$$

\text{«todo }P\text{ es }Q\text{»}
\longrightarrow
\forall x\,(P(x)\Rightarrow Q(x))

$$

$$

\text{«algún }P\text{ es }Q\text{»}
\longrightarrow
\exists x\,(P(x)\land Q(x))

$$

$$

\text{«no todos cumplen }P\text{»}
\longrightarrow
\exists x\,\neg P(x)

$$

y:

$$

\text{«para cada }x\text{ existe un }y\text{»}
\longrightarrow
\forall x\,\exists y.

$$

La comprobación final consiste siempre en regresar a la prosa:

$$

\text{prosa}
\longrightarrow
\text{símbolos}
\longrightarrow
\text{prosa}.

$$

Si el significado cambia al volver, la traducción inicial no era correcta.

Hasta ahora todas las letras variables que hemos cuantificado podían variar dentro del dominio.

Pero en muchas discusiones matemáticas una letra queda **fijada** mientras otras continúan variando.

Para describir esa situación necesitamos distinguir una variable de un parámetro.

## Hacia la sección siguiente

Consideremos $P_a(x):\quad x+a=a$. Podemos estudiar esta condición manteniendo $a$ fijo mientras $x$ varía.

¿Qué significa exactamente que una letra permanezca fija dentro de una discusión?
