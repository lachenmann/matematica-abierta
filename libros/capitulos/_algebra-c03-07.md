## §7. Varios cuantificadores y orden

En la sección anterior aprendimos a leer fórmulas como:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

Sabemos reconocer qué apariciones de variables están ligadas, cuáles permanecen libres y cuándo una fórmula está cerrada.

Ahora aparece una dificultad nueva. Consideremos $\forall x\,\exists y\,R(x,y)$. Las dos variables están cuantificadas. La fórmula es cerrada.

Pero ¿qué afirma exactamente?

Y, sobre todo, ¿diría lo mismo si cambiáramos el orden?

$$
\exists y\,\forall x\,R(x,y).
$$

Las dos escrituras utilizan:

- el mismo predicado;
- las mismas variables;
- un cuantificador universal;
- un cuantificador existencial.

Sin embargo, en general **no expresan la misma afirmación**.

El orden de los cuantificadores puede determinar qué valores pueden ajustarse a otros y cuáles deben quedar fijados de una vez para todos los casos.

Este será el problema central de la sección.

---

### 7.1 Leer desde fuera hacia dentro

Consideremos $\forall x\,\exists y\,R(x,y)$. El cuantificador exterior es:

$$
\forall x.
$$

Por tanto, comenzamos leyendo:

> «Para todo valor permitido de $x$...»

Después aparece:

$$
\exists y.
$$

Continuamos:

> «...existe al menos un valor permitido de $y$...»

Finalmente leemos la condición:

$$
R(x,y).
$$

La lectura completa es:

> «Para todo valor permitido de $x$, existe al menos un valor permitido de $y$ para el cual se cumple $R(x,y)$».

La estructura importa. Primero se considera un valor de $x$.

Después debemos poder encontrar algún valor de $y$ que haga verdadera la condición correspondiente.

Ese valor de $y$ **puede ser distinto para distintos valores de $x$**.

---

### 7.2 Cuando la elección interior puede cambiar

Trabajemos con valores enteros y definamos:

$$
R(x,y):\quad y=x+1.
$$

Consideremos $\forall x\,\exists y\,R(x,y)$. La fórmula dice:

> «Para todo entero $x$, existe un entero $y$ tal que $y=x+1$».

Si:

$$
x=0,
$$

podemos tomar:

$$
y=1.
$$

Si:

$$
x=5,
$$

podemos tomar:

$$
y=6.
$$

Si:

$$
x=-3,
$$

podemos tomar:

$$
y=-2.
$$

El valor elegido para $y$ no tiene que ser siempre el mismo.

Puede ajustarse al valor de $x$ que estamos considerando.

Así:

$$
\boxed{
\forall x\,\exists y
\quad\text{permite que el valor elegido para }y\text{ cambie al cambiar }x.
}
$$

No estamos introduciendo todavía una estructura matemática adicional. Solo estamos describiendo el significado lógico del orden de los cuantificadores.

---

### 7.3 Invertir el orden cambia la exigencia

Consideremos ahora:

$$
\exists y\,\forall x\,R(x,y),
$$

con el mismo predicado:

$$
R(x,y):\quad y=x+1.
$$

La lectura es:

> «Existe un entero $y$ tal que, para todo entero $x$, se cumple $y=x+1$».

Ahora la situación es muy distinta. El cuantificador exterior es:

$$
\exists y.
$$

Primero debe existir **un solo valor de $y$**. Después ese mismo valor tiene que satisfacer la condición para cada valor de $x$.

No podemos cambiar $y$ cada vez que cambia $x$.

Pero ningún entero puede cumplir esa exigencia. En efecto, si proponemos un entero cualquiera $y$ y consideramos:

$$
x=y,
$$

la condición $y=x+1$ se convierte en:

$$
y=y+1,
$$

que es falsa. Por tanto:

$$
\exists y\,\forall x\,(y=x+1)
$$

es falsa sobre los enteros. Tenemos así:

$$

\forall x\,\exists y\,(y=x+1)

$$

verdadera, pero:

$$
\boxed{
\exists y\,\forall x\,(y=x+1)
}
$$

falsa. Por tanto:

$$
\boxed{
\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y)
}
$$

en general.

---

### 7.4 El orden codifica una dependencia

La diferencia anterior puede expresarse en lenguaje ordinario.

#### En:

$$
\forall x\,\exists y\,R(x,y),
$$

leemos:

> «Para cada $x$, podemos encontrar algún $y$ adecuado».

El valor de $y$ puede cambiar de un caso a otro.

#### En:

$$
\exists y\,\forall x\,R(x,y),
$$

leemos:

> «Hay un mismo $y$ que funciona para todos los valores de $x$».

La segunda afirmación exige mucho más. Podemos condensar:

$$
\boxed{
\forall x\,\exists y:
\quad
\text{un }y\text{ puede ajustarse a cada }x
}
$$

mientras que:

$$
\boxed{
\exists y\,\forall x:
\quad
\text{un solo }y\text{ debe servir para todos los }x.
}
$$

Esta diferencia aparecerá constantemente en matemáticas.

---

### 7.5 No todo cambio de orden altera el significado

El caso anterior podría sugerir que nunca podemos cambiar el orden de cuantificadores.

Eso también sería incorrecto. Consideremos $\forall x\,\forall y\,R(x,y)$. La fórmula afirma:

> «Para todo valor permitido de $x$ y para todo valor permitido de $y$, se cumple $R(x,y)$».

Si intercambiamos el orden:

$$
\forall y\,\forall x\,R(x,y),
$$

seguimos exigiendo que $R(x,y)$ sea verdadera para **cada valor de $x$ y cada valor de $y$**.

No importa cuál de los dos universales leamos primero.

Algo semejante ocurre con:

$$
\exists x\,\exists y\,R(x,y).
$$

La fórmula afirma que hay al menos un valor de $x$ y al menos un valor de $y$ que, juntos, hacen verdadera la condición.

Intercambiar:

$$
\exists x\,\exists y
$$

por:

$$
\exists y\,\exists x
$$

no cambia esa exigencia. El comportamiento es, por tanto, diferente cuando los cuantificadores consecutivos son del **mismo tipo**.

---

### 7.6 Conmutación de cuantificadores del mismo tipo

::: {.ma-block .ma-enunciado #apm-i-p0008}
**Proposición — Conmutación de cuantificadores consecutivos del mismo tipo**

Sean $x$ e $y$ variables con sus dominios no vacíos previamente fijados, y sea $R(x,y)$ un predicado. Entonces:

$$
\boxed{
\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y)
}
$$

y:

$$
\boxed{
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
}
$$
:::

#### Demostración del caso universal

La fórmula $\forall x\,\forall y\,R(x,y)$ afirma que:

> para cada valor permitido de $x$, la condición $R(x,y)$ es verdadera para cada valor permitido de $y$.

Esto equivale a exigir que:

$$
R(x,y)
$$

sea verdadera para cada elección permitida de $x$ y para cada elección permitida de $y$.

Pero esa misma exigencia se expresa leyendo primero $y$ y después $x$:

$$
\forall y\,\forall x\,R(x,y).
$$

Por tanto:

$$
\boxed{
\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y).
}
$$

#### Demostración del caso existencial

La fórmula $\exists x\,\exists y\,R(x,y)$ afirma que:

> hay algún valor permitido de $x$ y algún valor permitido de $y$ para los cuales $R(x,y)$ es verdadera.

Que nombremos primero el valor de $x$ o primero el valor de $y$ no altera la existencia de esos dos valores.

Por tanto, la misma exigencia se expresa mediante:

$$
\exists y\,\exists x\,R(x,y).
$$

Así:

$$
\boxed{
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
}
$$

Quedan demostradas ambas equivalencias.

---

### 7.7 Qué no dice [la proposición «Conmutación de cuantificadores consecutivos del mismo tipo»](#apm-i-p0008)

[la proposición «Conmutación de cuantificadores consecutivos del mismo tipo»](#apm-i-p0008) no autoriza a intercambiar arbitrariamente cuantificadores.

La proposición se refiere únicamente a cuantificadores consecutivos del mismo tipo: $\forall\forall$ o $\exists\exists$ No afirma:

$$
\forall x\,\exists y\,R(x,y)
\equiv
\exists y\,\forall x\,R(x,y).
$$

De hecho, ya hemos visto un contraejemplo concreto a esa equivalencia.

Por tanto:

$$

\text{mismo tipo: el orden puede conmutarse;}
\qquad
\text{tipo mixto: no, en general.}

$$

La expresión «en general» es importante. Para algún predicado particular, ambas fórmulas mixtas podrían tener el mismo valor de verdad.

Lo que no podemos hacer es suponer que son equivalentes para todo predicado y todo dominio.

---

### 7.8 Cuatro patrones diferentes

Para un predicado de dos variables podemos encontrar, entre otras, estas cuatro estructuras:

$$
\forall x\,\forall y\,R(x,y),
$$

$$
\forall x\,\exists y\,R(x,y),
$$

$$
\exists x\,\forall y\,R(x,y),
$$

$$
\exists x\,\exists y\,R(x,y).
$$

No deben confundirse. Podemos leerlas así.

#### Dos universales

$$
\forall x\,\forall y\,R(x,y)
$$

dice:

> «$R(x,y)$ se cumple para todos los valores de $x$ y todos los valores de $y$».

#### Universal y luego existencial

$$
\forall x\,\exists y\,R(x,y)
$$

dice:

> «Para cada $x$, hay al menos un $y$ que funciona».

#### Existencial y luego universal

$$
\exists x\,\forall y\,R(x,y)
$$

dice:

> «Hay al menos un $x$ que funciona para todos los valores de $y$».

#### Dos existenciales

$$
\exists x\,\exists y\,R(x,y)
$$

dice:

> «Hay al menos un $x$ y al menos un $y$ que funcionan juntos».

Cada patrón impone una exigencia diferente.

---

### 7.9 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0027}
**Ejemplo — El mismo predicado, dos órdenes**
:::

Trabajaremos con valores enteros y definiremos:

$$
R(x,y):\quad y=x+1.
$$

Comparemos $\forall x\,\exists y\,R(x,y)$ con $\exists y\,\forall x\,R(x,y)$.

#### Primera fórmula

$$
\forall x\,\exists y\,(y=x+1).
$$

La lectura es:

> «Para todo entero $x$, existe un entero $y$ tal que $y=x+1$».

Si fijamos cualquier entero $x$, el valor $y=x+1$ también es entero y satisface la condición.

Por tanto:

$$
\boxed{
\forall x\,\exists y\,(y=x+1)
}
$$

es verdadera. El valor de $y$ puede cambiar cuando cambia $x$.

#### Segunda fórmula

$$
\exists y\,\forall x\,(y=x+1).
$$

La lectura es:

> «Existe un entero $y$ que satisface $y=x+1$ para todo entero $x$».

Aquí necesitamos un solo entero $y$ que funcione para todos los valores de $x$.

Supongamos que se propone un valor cualquiera de $y$.

Como el dominio es el de los enteros, también podemos considerar:

$$
x=y.
$$

Entonces la condición exigiría:

$$
y=y+1,
$$

lo cual es falso. Ningún entero $y$ sirve para todos los enteros $x$.

Así:

$$
\boxed{
\exists y\,\forall x\,(y=x+1)
}
$$

es falsa.

#### Conclusión

Tenemos:

$$

\forall x\,\exists y\,R(x,y)=\mathrm V,

$$

pero:

$$

\exists y\,\forall x\,R(x,y)=\mathrm F.

$$

El orden de los cuantificadores mixtos ha cambiado el significado y el valor de verdad.

---
## Ejercicios

### Leer una cadena de cuantificadores {#apm-i-e0171}
Trabajamos con valores enteros.

Lee en prosa:

$$
\forall x\,\exists y\,R(x,y).
$$

Después explica cuál cuantificador se lee primero.

#### Solución


La fórmula se lee:

> «Para todo entero $x$, existe al menos un entero $y$ para el cual se cumple $R(x,y)$».

El cuantificador que se lee primero es el exterior:

$$
\forall x.
$$

Después, dentro de su alcance, aparece:

$$
\exists y.
$$

Por tanto, primero consideramos un valor de $x$ y después exigimos que haya algún valor de $y$ adecuado para ese caso.

---

### Qué puede cambiar {#apm-i-e0172}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad x+y=0.
$$

Explica qué significa:

$$
\forall x\,\exists y\,R(x,y)
$$

y por qué el valor de $y$ puede cambiar cuando cambia $x$.

#### Solución


La fórmula afirma:

> «Para todo entero $x$, existe un entero $y$ tal que $x+y=0$».

Si:

$$
x=3,
$$

podemos tomar:

$$
y=-3.
$$

Si:

$$
x=-5,
$$

podemos tomar:

$$
y=5.
$$

El cuantificador existencial está dentro del alcance del cuantificador universal.

Por tanto, después de considerar cada valor de $x$, podemos encontrar un valor de $y$ adecuado para ese caso.

No se exige que el mismo $y$ funcione para todos los valores de $x$.

---

### Justificar una conmutación válida {#apm-i-e0173}
Explica por qué:

$$
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
$$

No te limites a citar [la proposición «Conmutación de cuantificadores consecutivos del mismo tipo»](#apm-i-p0008): explica el significado de ambas fórmulas.

#### Solución


La primera fórmula:

$$
\exists x\,\exists y\,R(x,y)
$$

afirma que hay algún valor permitido de $x$ y algún valor permitido de $y$ para los cuales:

$$
R(x,y)
$$

es verdadera.

La segunda:

$$
\exists y\,\exists x\,R(x,y)
$$

afirma exactamente la misma existencia, pero nombra primero el valor de $y$ y después el de $x$.

Si existen valores adecuados de $x$ e $y$, existen independientemente del orden en que los mencionemos.

Por tanto:

$$
\boxed{
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
}
$$

---

### Un intercambio inválido {#apm-i-e0174}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x+1.
$$

#### a)

Determina el valor de verdad de:

$$
\forall x\,\exists y\,R(x,y).
$$

#### b)

Determina el valor de verdad de:

$$
\exists y\,\forall x\,R(x,y).
$$

#### c)

Explica por qué este ejemplo refuta la equivalencia general entre ambas fórmulas.

#### Solución


#### a)

La fórmula:

$$
\forall x\,\exists y\,(y=x+1)
$$

es verdadera.

Para cualquier entero $x$, podemos tomar:

$$
y=x+1,
$$

que también es entero.

#### b)

La fórmula:

$$
\exists y\,\forall x\,(y=x+1)
$$

es falsa.

Un solo entero $y$ tendría que satisfacer la ecuación para todos los valores de $x$.

Para cualquier valor propuesto de $y$, podemos tomar:

$$
x=y.
$$

Entonces necesitaríamos:

$$
y=y+1,
$$

lo cual es falso.

#### c)

La primera fórmula es verdadera y la segunda es falsa bajo el mismo dominio y el mismo predicado.

Por tanto, no pueden ser lógicamente equivalentes en general.

---

### Construir un segundo contraejemplo {#apm-i-e0175}
Trabajamos con valores enteros y definimos:

$$
S(x,y):\quad x+y=0.
$$

Compara:

$$
\forall x\,\exists y\,S(x,y)
$$

con:

$$
\exists y\,\forall x\,S(x,y).
$$

Determina el valor de verdad de cada una y explica por qué este ejemplo vuelve a mostrar que los cuantificadores mixtos no pueden intercambiarse en general.

#### Solución


#### Primera fórmula

$$
\forall x\,\exists y\,(x+y=0).
$$

Para cada entero $x$, podemos tomar:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

Por tanto, la fórmula es verdadera.

#### Segunda fórmula

$$
\exists y\,\forall x\,(x+y=0).
$$

Aquí tendría que existir un único entero $y$ que satisficiera:

$$
x+y=0
$$

para todos los enteros $x$.

Eso es imposible.

Por ejemplo, si la condición se cumpliera para:

$$
x=0,
$$

tendríamos:

$$
y=0.
$$

Pero entonces, para:

$$
x=1,
$$

obtendríamos:

$$
1+0=0,
$$

que es falso.

Por tanto, la segunda fórmula es falsa.

Una vez más:

$$
\forall x\,\exists y\,S(x,y)
$$

y:

$$
\exists y\,\forall x\,S(x,y)
$$

tienen valores de verdad distintos.

---

### Cuatro patrones cuantificados {#apm-i-e0176}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad x<y.
$$

Determina el valor de verdad de cada fórmula y justifica.

#### a)

$$
\forall x\,\forall y\,R(x,y)
$$

#### b)

$$
\forall x\,\exists y\,R(x,y)
$$

#### c)

$$
\exists x\,\forall y\,R(x,y)
$$

#### d)

$$
\exists x\,\exists y\,R(x,y)
$$

#### Solución


#### a)

$$
\forall x\,\forall y\,(x<y)
$$

es falsa.

Por ejemplo, podemos tomar:

$$
x=0,
\qquad
y=0.
$$

Entonces:

$$
0<0
$$

es falsa.

#### b)

$$
\forall x\,\exists y\,(x<y)
$$

es verdadera.

Para cualquier entero $x$, podemos tomar:

$$
y=x+1.
$$

Entonces:

$$
x<x+1.
$$

#### c)

$$
\exists x\,\forall y\,(x<y)
$$

es falsa.

Para cualquier entero propuesto como $x$, podemos tomar:

$$
y=x.
$$

Entonces la condición exigiría:

$$
x<x,
$$

que es falsa.

Por tanto, ningún entero $x$ es menor que todos los enteros.

#### d)

$$
\exists x\,\exists y\,(x<y)
$$

es verdadera.

Por ejemplo:

$$
x=0,
\qquad
y=1
$$

satisfacen:

$$
0<1.
$$

#### Comparación

Obtenemos:

$$
\boxed{
\begin{array}{c|c}
\text{Fórmula} & \text{Valor}\\
\hline
\forall x\,\forall y\,R(x,y) & \mathrm F\\
\forall x\,\exists y\,R(x,y) & \mathrm V\\
\exists x\,\forall y\,R(x,y) & \mathrm F\\
\exists x\,\exists y\,R(x,y) & \mathrm V
\end{array}
}
$$

Los cuatro patrones imponen exigencias lógicas diferentes.

---

## Síntesis

Cuando una fórmula contiene varios cuantificadores debemos leerla desde fuera hacia dentro.

El orden puede codificar una diferencia esencial. En:

$$
\forall x\,\exists y\,R(x,y),
$$

el valor de $y$ puede ajustarse al valor de $x$ que estamos considerando.

En:

$$
\exists y\,\forall x\,R(x,y),
$$

un único valor de $y$ debe funcionar para todos los valores de $x$.

Por eso, en general:

$$

\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y).

$$

En cambio, los cuantificadores consecutivos del mismo tipo sí conmutan:

$$

\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y)

$$

y:

$$

\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).

$$

La lección central es:

$$

\text{en una fórmula cuantificada, el orden también forma parte del significado}.

$$

Ahora ya sabemos leer las piezas fundamentales del lenguaje cuantificacional.

El paso siguiente será aprender a pasar sistemáticamente entre ese lenguaje simbólico y las frases matemáticas escritas en prosa.

## Hacia la sección siguiente

Una fórmula como:

$$
\forall x\,\exists y\,(P(x)\Rightarrow Q(x,y))
$$

debe poder leerse con precisión en castellano. Y una frase como:

> «Para cada valor de $x$, existe algún valor de $y$ que satisface cierta condición»

debe poder convertirse en una fórmula sin alterar el orden, el alcance ni los conectivos.
