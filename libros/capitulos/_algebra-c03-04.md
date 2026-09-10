## §4. El cuantificador existencial

En la sección anterior introdujimos una manera de cerrar una fórmula abierta:

$$
P(x)
\longrightarrow
\forall x\,P(x).
$$

La afirmación universal exige que la condición se cumpla para **cada** valor permitido del dominio.

Pero muchas afirmaciones matemáticas tienen una exigencia diferente. Consideremos, en el dominio de los enteros:

$$
P(x):\quad x^2=9.
$$

No es cierto que:

$$
\forall x\,P(x),
$$

porque, por ejemplo:

$$
P(0):\quad 0^2=9
$$

es falsa.

Sin embargo, sí hay valores enteros que hacen verdadera la condición: $P(3):\quad 3^2=9$, y $P(-3):\quad (-3)^2=9$.

Por tanto, aunque la condición no se cumple para todos los enteros, podemos afirmar algo importante:

> hay al menos un valor permitido de $x$ que la satisface.

Para expresar esta idea utilizaremos nuestro segundo cuantificador fundamental.

---

### 4.1 «Existe» significa «hay al menos uno»

Escribimos $\exists x\,P(x)$. El símbolo $\exists$ se lee:

> «existe»

o:

> «hay al menos un».

Así, $\exists x\,P(x)$ se lee:

> «Existe un valor de $x$ para el cual se cumple $P(x)$».

En nuestro ejemplo:

$$
\exists x\,(x^2=9)
$$

se lee:

> «Existe un entero $x$ cuyo cuadrado es igual a $9$».

La afirmación es verdadera porque podemos encontrar valores permitidos que hacen verdadera la condición.

Por ejemplo:

$$
x=3.
$$

---

### 4.2 El cuantificador existencial

::: {.ma-block .ma-definicion #apm-i-d0029}
**Definición — Cuantificador existencial**

El **cuantificador existencial** es el símbolo:

$$
\exists.
$$

Si $P(x)$ es un predicado y el dominio de $x$ está fijado, la fórmula:

$$
\exists x\,P(x)
$$

afirma que $P(x)$ es verdadera para **al menos un valor permitido de $x$**.
:::

El dominio sigue siendo indispensable. La expresión $\exists x\,P(x)$ no nos dice por sí sola qué objetos pueden ocupar el lugar de $x$.

Esa información debe estar declarada por el contexto.

---

### 4.3 Una tercera manera de pasar de fórmula abierta a proposición

Ya conocemos tres situaciones.

#### Sustitución concreta

$$
P(x)
\longrightarrow
P(3).
$$

Hablamos de un valor particular.

#### Cuantificación universal

$$
P(x)
\longrightarrow
\forall x\,P(x).
$$

Afirmamos que la condición se cumple para cada valor permitido.

#### Cuantificación existencial

$$
P(x)
\longrightarrow
\exists x\,P(x).
$$

Afirmamos que la condición se cumple para al menos un valor permitido.

Podemos resumir:

$$
\boxed{
\begin{array}{ccl}
P(3) &:& \text{este valor concreto funciona},\\[4pt]
\forall x\,P(x) &:& \text{todos los valores funcionan},\\[4pt]
\exists x\,P(x) &:& \text{al menos un valor funciona}.
\end{array}
}
$$

Las tres afirmaciones tienen exigencias lógicas distintas.

---

### 4.4 Testigos de una afirmación existencial

Consideremos $\exists x\,(x^2=9)$ en el dominio de los enteros. El valor $x=3$ hace verdadera la condición:

$$
3^2=9.
$$

Por tanto, $3$ confirma concretamente que la afirmación existencial es verdadera.

Llamaremos **testigo** a un valor permitido que hace verdadera la condición de una afirmación existencial.

Así, $3$ es un testigo de:

$$
\exists x\,(x^2=9).
$$

También:

$$
-3
$$

es otro testigo, porque:

$$
(-3)^2=9.
$$

Esto muestra algo importante:

$$

\text{un testigo basta para confirmar una afirmación existencial concreta}.

$$

No necesitamos encontrar todos los valores que funcionan. Basta uno.

---

### 4.5 Existencia no significa unicidad

La afirmación:

$$
\exists x\,P(x)
$$

significa:

> «hay al menos un valor de $x$ que satisface $P(x)$».

No significa:

> «hay exactamente un valor».

Volvamos a $P(x):\quad x^2=9$ en los enteros. Tenemos dos testigos: $x=3$ y $x=-3$.

Por tanto:

$$
\exists x\,P(x)
$$

es verdadera.

Pero la condición no tiene un único valor que la satisfaga.

Esta distinción debe quedar fijada desde ahora:

$$

\text{«existe»}
\neq
\text{«existe exactamente uno».}

$$

Más adelante estudiaremos cómo expresar simbólicamente la existencia única.

---

### 4.6 Una afirmación existencial también puede ser falsa

El cuantificador existencial no convierte automáticamente una condición en una afirmación verdadera.

Consideremos, en el dominio de los enteros:

$$
Q(x):\quad 2x=1.
$$

La fórmula $\exists x\,Q(x)$ afirma:

> «Existe un entero $x$ tal que $2x=1$».

Pero ningún entero satisface esa ecuación. Por tanto:

$$
\exists x\,(2x=1)
$$

es falsa en el dominio de los enteros. La exigencia existencial es menos fuerte que la universal, pero sigue siendo una exigencia:

$$
\boxed{
\text{debe haber al menos un valor permitido que funcione}.
}
$$

---

### 4.7 El dominio puede cambiar una afirmación existencial

Consideremos nuevamente:

$$
Q(x):\quad 2x=1.
$$

#### Dominio de los enteros

No hay un entero que satisfaga:

$$
2x=1.
$$

Por tanto:

$$
\exists x\,(2x=1)
$$

es falsa.

#### Dominio de los racionales

Ahora el valor $x=\frac12$ está permitido. Y:

$$
2\cdot\frac12=1.
$$

Por tanto:

$$
\exists x\,(2x=1)
$$

es verdadera en este segundo dominio. La fórmula escrita es la misma.

El dominio cambia qué valores pueden servir como testigos.

Así:

$$
\boxed{
\text{el valor de verdad de una afirmación existencial puede depender del dominio}.
}
$$

---

### 4.8 Universal y existencial no dicen lo mismo

Consideremos, en el dominio de los enteros:

$$
P(x):\quad x^2=9.
$$

La afirmación:

$$
\forall x\,P(x)
$$

es falsa, porque no todos los enteros tienen cuadrado igual a $9$.

En cambio, $\exists x\,P(x)$ es verdadera, porque:

$$
x=3
$$

es un testigo. Por tanto: $\forall x\,P(x)$ y $\exists x\,P(x)$ no son dos maneras de escribir la misma idea.

El universal exige:

> todos.

El existencial exige:

> al menos uno.

Podemos visualizar la diferencia:

$$
\boxed{
\forall:\ \text{ninguna excepción}
\qquad
\exists:\ \text{al menos un caso favorable}.
}
$$

---

### 4.9 Encontrar muchos casos tampoco cambia el significado de «existe»

Si encontramos varios testigos, una afirmación existencial sigue diciendo solamente:

> «hay al menos uno».

Por ejemplo, en los enteros:

$$
\exists x\,(x^2=9)
$$

tiene al menos los testigos:

$$
3,\qquad -3.
$$

El hecho de que encontremos dos testigos no cambia el significado del cuantificador.

La afirmación existencial no lleva incorporado un conteo exacto de cuántos valores funcionan.

Por eso debemos resistir dos errores opuestos:

- creer que «existe» significa «existe exactamente uno»;
- creer que para justificar una existencia concreta debemos encontrar todos los valores que funcionan.

Ninguno de los dos es correcto.

---

### 4.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0024}
**Ejemplo — Existencia, testigos y ausencia de unicidad**
:::

Trabajaremos con valores enteros y definimos:

$$
P(x):\quad x^2=9.
$$

Consideremos $\exists x\,P(x)$. La fórmula afirma:

> «Existe al menos un entero $x$ cuyo cuadrado es igual a $9$».

Tomemos $x=3$. Entonces $P(3):\quad 3^2=9$, que es verdadera. Por tanto:

$$
x=3
$$

es un testigo y la afirmación existencial es verdadera.

Pero también podemos tomar:

$$
x=-3.
$$

Entonces $P(-3):\quad (-3)^2=9$, que también es verdadera. Así, tenemos al menos dos testigos:

$$
3
\qquad\text{y}\qquad
-3.
$$

#### Qué demuestra esto

Primero:

$$
\exists x\,(x^2=9)
$$

es verdadera en los enteros. Segundo, la afirmación existencial no dice que haya un único valor que funcione.

Por tanto:

$$
\boxed{
\text{existencia}
\quad\text{y}\quad
\text{unicidad}
}
$$

son cuestiones distintas.

---
## Ejercicios

### Escribir «existe» {#apm-i-e0153}
En el dominio de los enteros, sea:

$$
P(x):\quad x+2=7.
$$

Escribe simbólicamente:

> «Existe un valor de $x$ para el cual se cumple $P(x)$».

Después escribe la fórmula sin utilizar el nombre $P$.

#### Solución


Con el nombre del predicado:

$$
\boxed{
\exists x\,P(x).
}
$$

Como:

$$
P(x):\quad x+2=7,
$$

podemos escribir:

$$
\boxed{
\exists x\,(x+2=7).
}
$$

La afirmación es verdadera, pues:

$$
x=5
$$

es un testigo.

---

### «Existe» significa «al menos uno» {#apm-i-e0154}
Explica por qué:

$$
\exists x\,P(x)
$$

no afirma que exista exactamente un valor que satisfaga $P(x)$.

#### Solución


El cuantificador existencial exige solamente que haya **al menos un** valor permitido para el cual:

$$
P(x)
$$

sea verdadera.

Puede haber un solo valor, dos, diez o muchos más.

Por ejemplo, en los enteros:

$$
\exists x\,(x^2=9)
$$

es verdadera y tiene al menos dos testigos:

$$
3
\qquad\text{y}\qquad
-3.
$$

Por tanto, existencia y unicidad son afirmaciones diferentes.

---

### Por qué basta un testigo {#apm-i-e0155}
Trabajamos con valores enteros.

Considera:

$$
\exists x\,(x^2=16).
$$

Explica por qué exhibir:

$$
x=4
$$

es suficiente para determinar que la afirmación existencial es verdadera.

#### Solución


La afirmación:

$$
\exists x\,(x^2=16)
$$

exige que haya al menos un entero cuyo cuadrado sea $16$.

Tomamos:

$$
x=4.
$$

Entonces:

$$
4^2=16.
$$

Hemos encontrado un valor permitido que hace verdadera la condición.

Por tanto, la exigencia existencial ya está satisfecha.

No necesitamos encontrar todos los valores que funcionen para concluir que la afirmación es verdadera.

---

### Más de un testigo {#apm-i-e0156}
Trabajamos con valores enteros.

Considera:

$$
P(x):\quad x^2=25.
$$

#### a)

Encuentra un testigo de:

$$
\exists x\,P(x).
$$

#### b)

Encuentra un segundo testigo distinto.

#### c)

¿Qué muestra esto acerca de la relación entre existencia y unicidad?

#### Solución


#### a)

Podemos tomar:

$$
x=5.
$$

Entonces:

$$
5^2=25.
$$

Por tanto, $5$ es un testigo.

#### b)

También:

$$
x=-5
$$

satisface:

$$
(-5)^2=25.
$$

Así, $-5$ es un segundo testigo.

#### c)

La afirmación existencial es verdadera, pero hay más de un valor que satisface la condición.

Por tanto:

$$
\boxed{
\text{existencia no implica unicidad}.
}
$$

---

### Formular una afirmación existencial {#apm-i-e0157}
Trabajamos con valores enteros.

Escribe simbólicamente:

> «Existe un entero cuyo triple es igual a $12$».

Después encuentra un testigo y determina el valor de verdad de la afirmación.

#### Solución


Podemos escribir:

$$
\boxed{
\exists x\,(3x=12).
}
$$

Tomamos:

$$
x=4.
$$

Entonces:

$$
3\cdot4=12.
$$

Por tanto, $4$ es un testigo y la afirmación existencial es verdadera.

---

### La misma existencia en dos dominios {#apm-i-e0158}
Considera:

$$
P(x):\quad 2x=3.
$$

#### Contexto A

El dominio es el de los enteros.

#### Contexto B

El dominio es el de los racionales.

#### a)

Determina el valor de verdad de:

$$
\exists x\,P(x)
$$

en el contexto A.

#### b)

Determina el valor de verdad de la misma fórmula en el contexto B.

#### c)

Explica qué papel desempeña el dominio.

#### Solución


#### a)

En los enteros, la ecuación:

$$
2x=3
$$

no tiene una solución entera.

Por tanto:

$$
\boxed{
\exists x\,(2x=3)
}
$$

es falsa en el contexto A.

#### b)

En los racionales podemos tomar:

$$
x=\frac32.
$$

Entonces:

$$
2\cdot\frac32=3.
$$

Por tanto:

$$
\boxed{
\exists x\,(2x=3)
}
$$

es verdadera en el contexto B.

#### c)

El dominio determina qué valores pueden actuar como testigos.

La fórmula es la misma, pero un valor permitido en un dominio puede no estar permitido en otro.

Por eso el dominio forma parte del significado de la afirmación existencial.

---

## Síntesis

Ahora disponemos de los dos cuantificadores fundamentales del capítulo.

El universal:

$$
\forall x\,P(x)
$$

afirma:

> «$P(x)$ se cumple para cada valor permitido».

El existencial:

$$
\exists x\,P(x)
$$

afirma:

> «$P(x)$ se cumple para al menos un valor permitido».

La diferencia puede condensarse así:

$$

\forall:\ \text{todos}
\qquad
\exists:\ \text{al menos uno}.

$$

También introdujimos la idea de **testigo**:

$$

\text{un testigo es un valor permitido que hace verdadera la condición existencial}.

$$

Y fijamos una distinción que será esencial:

$$

\text{existencia}
\neq
\text{unicidad}.

$$

Ya podemos leer afirmaciones con:

$$
\forall
\qquad\text{y}\qquad
\exists.
$$

El siguiente problema será aprender a **negarlas correctamente**.

## Hacia la sección siguiente

¿Qué significa decir que no es verdad que todos los valores satisfacen una condición?

¿Y qué significa decir que no existe ningún valor que la satisfaga?

La negación hará que los dos cuantificadores se relacionen entre sí.
