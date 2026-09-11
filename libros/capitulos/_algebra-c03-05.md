## §5. Negar cuantificadores

Ya sabemos leer:

$$
\forall x\,P(x)
$$

como:

> «$P(x)$ se cumple para cada valor permitido de $x$»,

y:

$$
\exists x\,P(x)
$$

como:

> «$P(x)$ se cumple para al menos un valor permitido de $x$».

Ahora queremos responder una pregunta decisiva:

> ¿qué significa negar correctamente una afirmación cuantificada?

Consideremos primero:

$$
\forall x\,P(x).
$$

Negarla significa afirmar:

> «No es verdad que $P(x)$ se cumpla para todos los valores».

Pero eso no significa que $P(x)$ falle para todos.

Basta que falle para **al menos uno**. Por tanto:

$$
\neg\forall x\,P(x)
$$

expresa la misma condición lógica que:

$$
\exists x\,\neg P(x).
$$

El universal se convierte en existencial y la negación alcanza finalmente a la condición.

Algo dual ocurre con:

$$
\exists x\,P(x).
$$

Negar que exista al menos un valor que haga verdadera $P(x)$ significa que **cada** valor permitido hace falsa $P(x)$.

Así, $\neg\exists x\,P(x)$ expresa lo mismo que:

$$
\forall x\,\neg P(x).
$$

Estas dos equivalencias serán las primeras leyes formales de lógica cuantificacional del capítulo.

---

### 5.1 Negar «todos»

Trabajemos con valores enteros y consideremos:

$$
P(x):\quad x>0.
$$

La afirmación:

$$
\forall x\,P(x)
$$

dice:

> «Todo entero es positivo».

Su negación es:

> «No todo entero es positivo».

¿Qué tendría que ocurrir para que esa negación fuera verdadera?

Basta que exista un entero que **no** sea positivo.

Por ejemplo, $x=0$ hace falsa la condición:

$$
x>0.
$$

Por tanto, decir:

$$
\neg\forall x\,P(x)
$$

equivale a decir:

$$
\exists x\,\neg P(x).
$$

En prosa:

> «No todos cumplen $P$»

equivale a:

> «Hay al menos uno que no cumple $P$».

La estructura es:

$$
\boxed{
\neg\forall
\quad\longrightarrow\quad
\exists\neg.
}
$$

---

### 5.2 «No todos» no significa «ninguno»

Esta distinción merece atención especial. Consideremos un dominio formado por los valores:

$$
1
\qquad\text{y}\qquad
2,
$$

y definamos:

$$
P(x):\quad x\text{ es par}.
$$

La afirmación:

> «No todos los valores del dominio son pares»

es verdadera, porque:

$$
1
$$

no es par. En símbolos:

$$
\neg\forall x\,P(x).
$$

Pero la afirmación:

> «Todos los valores del dominio no son pares»

es falsa, porque:

$$
2
$$

sí es par. En símbolos:

$$
\forall x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\forall x\,P(x)
\not\equiv
\forall x\,\neg P(x).
}
$$

La negación de «todos» no produce «ninguno». Produce:

> «al menos uno no».

---

### 5.3 Negar «existe»

Consideremos ahora, en el dominio de los enteros:

$$
Q(x):\quad x^2=-1.
$$

La afirmación:

$$
\exists x\,Q(x)
$$

dice:

> «Existe un entero cuyo cuadrado es $-1$».

Negarla significa:

> «No existe ningún entero cuyo cuadrado sea $-1$».

¿Qué expresa esto acerca de cada entero?

Expresa que, cualquiera sea el valor permitido de $x$:

$$
x^2\ne-1.
$$

Por tanto:

$$
\neg\exists x\,Q(x)
$$

equivale a:

$$
\forall x\,\neg Q(x).
$$

En prosa:

> «No existe ninguno que cumpla $Q$»

equivale a:

> «Todos incumplen $Q$».

La estructura es:

$$
\boxed{
\neg\exists
\quad\longrightarrow\quad
\forall\neg.
}
$$

---

### 5.4 Las dos leyes

Ya podemos formular el resultado general.

::: {.ma-block .ma-enunciado #apm-t1-c03-p0007}
**Proposición — Leyes de negación de cuantificadores**

Sea $P(x)$ un predicado sobre un dominio no vacío previamente fijado. Entonces:

$$
\boxed{
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x)
}
$$

y:

$$
\boxed{
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
}
$$
:::

#### Demostración de la primera equivalencia

Consideremos $\neg\forall x\,P(x)$. Esta fórmula afirma que no es verdad que:

$$
P(x)
$$

se cumpla para cada valor permitido. Que una afirmación universal falle significa precisamente que hay al menos un valor permitido para el cual la condición falla.

Existe un valor de $x$ para el cual:

$$
\neg P(x)
$$

es verdadera. Eso es exactamente lo que afirma:

$$
\exists x\,\neg P(x).
$$

Así:

$$
\boxed{
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
}
$$

#### Demostración de la segunda equivalencia

Consideremos $\neg\exists x\,P(x)$. Esta fórmula afirma que no es verdad que haya al menos un valor permitido para el cual:

$$
P(x)
$$

sea verdadera. Por tanto, ningún valor permitido hace verdadera $P(x)$.

Dicho de otro modo, para cada valor permitido de $x$:

$$
P(x)
$$

es falsa, es decir:

$$
\neg P(x)
$$

es verdadera. Eso es exactamente lo que afirma:

$$
\forall x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
}
$$

Quedan demostradas las dos leyes.

---

### 5.5 Una manera de recordarlas

No conviene aprender las leyes como un simple intercambio de símbolos.

Conviene reconstruir su significado.

#### Si negamos un universal

$$
\neg\forall x\,P(x),
$$

preguntamos:

> «¿Qué hace que falle la afirmación de que todos cumplen $P$?»

Respuesta:

> «Que haya al menos uno que no cumpla $P$».

Por eso:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

#### Si negamos un existencial

$$
\neg\exists x\,P(x),
$$

preguntamos:

> «¿Qué significa que no haya ni un solo valor que cumpla $P$?»

Respuesta:

> «Que todos los valores incumplan $P$».

Por eso:

$$
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
$$

Podemos condensarlo así:

$$

\text{al negar un cuantificador, cambia su tipo y la negación continúa hacia la condición}.

$$

---

### 5.6 La negación debe llegar hasta la condición

Consideremos $\neg\forall x\,(x^2=x)$ No debemos detenernos en:

> «No todos los enteros satisfacen $x^2=x$».

Esa frase es correcta, pero podemos expresar la negación en una forma equivalente más informativa.

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,(x^2=x)
\equiv
\exists x\,\neg(x^2=x).
$$

Negar la igualdad $x^2=x$ produce:

$$
x^2\ne x.
$$

Por tanto:

$$
\boxed{
\neg\forall x\,(x^2=x)
\equiv
\exists x\,(x^2\ne x).
}
$$

En prosa:

> «No todos los enteros satisfacen $x^2=x$»

equivale a:

> «Existe al menos un entero cuyo cuadrado no es igual a él mismo».

Por ejemplo, $x=2$ confirma la segunda afirmación.

---

### 5.7 Negar una existencia concreta

Consideremos, en el dominio de los enteros:

$$
\neg\exists x\,(2x=1).
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,(2x=1)
\equiv
\forall x\,\neg(2x=1).
$$

Negando la igualdad $\neg(2x=1)$ obtenemos:

$$
2x\ne1.
$$

Así:

$$
\boxed{
\neg\exists x\,(2x=1)
\equiv
\forall x\,(2x\ne1).
}
$$

Las dos fórmulas expresan la misma idea:

> «No existe un entero que satisfaga $2x=1$»

y:

> «Todo entero incumple $2x=1$».

---

### 5.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-t1-c03-x0025}
**Ejemplo — De «no todos» a «existe una excepción»**
:::

Trabajaremos con valores enteros y consideramos:

$$
P(x):\quad x^2=x.
$$

La afirmación universal:

$$
\forall x\,P(x)
$$

dice:

> «Todo entero satisface $x^2=x$».

Queremos negarla.

#### Paso 1 — Negar la afirmación completa

Escribimos $\neg\forall x\,P(x)$. En prosa:

> «No todos los enteros satisfacen $P$».

#### Paso 2 — Aplicar [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007)

Tenemos:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

#### Paso 3 — Recuperar la condición concreta

Como:

$$
P(x):\quad x^2=x,
$$

obtenemos $\exists x\,\neg(x^2=x)$. Por tanto:

$$

\exists x\,(x^2\ne x).

$$

#### Paso 4 — Volver a la prosa

La negación correcta es:

> «Existe al menos un entero cuyo cuadrado no es igual a él mismo».

#### Paso 5 — Comprobar el significado

Tomemos $x=2$. Entonces $2^2\ne2$. Por tanto, $2$ es un valor que hace verdadera la negación de la afirmación universal.

El ejemplo muestra que:

$$

\text{negar «todos»}
\quad\text{no produce}\quad
\text{«ninguno»,}

$$

sino:

$$

\text{«existe al menos una excepción».}

$$

---
## Ejercicios

### Negar un universal {#apm-t1-c03-e0159}
Trabajamos con valores enteros.

Niega correctamente:

$$
\forall x\,(x+0=x).
$$

Expresa el resultado en símbolos y en prosa.

#### Solución


Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,(x+0=x)
\equiv
\exists x\,\neg(x+0=x).
$$

Negando la igualdad:

$$
\neg(x+0=x)
$$

obtenemos:

$$
x+0\ne x.
$$

Por tanto, la negación es:

$$
\boxed{
\exists x\,(x+0\ne x).
}
$$

En prosa:

> «Existe al menos un entero para el cual $x+0\ne x$».

Esta negación es falsa, porque sumar cero no cambia ningún entero.

Eso es coherente con que la afirmación universal original sea verdadera.

---

### Negar un existencial {#apm-t1-c03-e0160}
Trabajamos con valores enteros.

Niega correctamente:

$$
\exists x\,(2x=1).
$$

Expresa el resultado en símbolos y en prosa.

#### Solución


Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\exists x\,(2x=1)
\equiv
\forall x\,\neg(2x=1).
$$

Negando la igualdad:

$$
\neg(2x=1)
$$

obtenemos:

$$
2x\ne1.
$$

Por tanto:

$$
\boxed{
\forall x\,(2x\ne1).
}
$$

En prosa:

> «Para todo entero $x$, $2x$ es distinto de $1$».

Equivalentemente:

> «Ningún entero satisface $2x=1$».

---

### «No todos» frente a «todos no» {#apm-t1-c03-e0161}
El dominio contiene únicamente los valores:

$$
1
\qquad\text{y}\qquad
2.
$$

Sea:

$$
P(x):\quad x\text{ es par}.
$$

Compara:

$$
\neg\forall x\,P(x)
$$

con:

$$
\forall x\,\neg P(x).
$$

Determina el valor de verdad de cada fórmula y explica por qué no son equivalentes.

#### Solución


Primero:

$$
\neg\forall x\,P(x)
$$

significa:

> «No todos los valores del dominio son pares».

Esto es verdadero, porque:

$$
1
$$

no es par.

Ahora:

$$
\forall x\,\neg P(x)
$$

significa:

> «Todos los valores del dominio no son pares».

Esto es falso, porque:

$$
2
$$

sí es par.

Por tanto:

$$
\neg\forall x\,P(x)
$$

es verdadera, mientras que:

$$
\forall x\,\neg P(x)
$$

es falsa.

Así:

$$
\boxed{
\neg\forall x\,P(x)
\not\equiv
\forall x\,\neg P(x).
}
$$

---

### Justificar la primera ley {#apm-t1-c03-e0162}
Explica, sin limitarte a repetir la fórmula, por qué:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

#### Solución


La afirmación:

$$
\forall x\,P(x)
$$

exige que $P(x)$ sea verdadera para cada valor permitido.

Negarla significa que esa exigencia universal falla.

Para que falle, debe haber al menos un valor permitido para el cual:

$$
P(x)
$$

sea falsa.

Decir que hay al menos un valor para el cual $P(x)$ es falsa equivale a decir que hay al menos un valor para el cual:

$$
\neg P(x)
$$

es verdadera.

Eso es exactamente:

$$
\exists x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
}
$$

---

### Justificar la segunda ley {#apm-t1-c03-e0163}
Explica por qué:

$$
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
$$

#### Solución


La afirmación:

$$
\exists x\,P(x)
$$

dice que hay al menos un valor permitido que hace verdadera $P(x)$.

Negarla significa que no hay ningún valor permitido con esa propiedad.

Por tanto, cada valor permitido hace falsa $P(x)$.

Decir que $P(x)$ es falsa para cada valor equivale a decir que:

$$
\neg P(x)
$$

es verdadera para cada valor.

Eso es:

$$
\forall x\,\neg P(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
}
$$

---

### De la prosa a la negación y de vuelta {#apm-t1-c03-e0164}
Trabajamos con valores enteros.

Considera la afirmación:

> «Todo entero satisface $x^2=x$».

#### a)

Escríbela simbólicamente.

#### b)

Escribe su negación.

#### c)

Transforma la negación mediante [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

#### d)

Vuelve a expresar el resultado en prosa.

#### e)

Exhibe un valor que confirme que la negación es verdadera.

#### Solución


#### a)

La afirmación universal es:

$$
\forall x\,(x^2=x).
$$

#### b)

Su negación es:

$$
\neg\forall x\,(x^2=x).
$$

#### c)

Por [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007):

$$
\neg\forall x\,(x^2=x)
\equiv
\exists x\,\neg(x^2=x).
$$

Negando la igualdad:

$$
\boxed{
\exists x\,(x^2\ne x).
}
$$

#### d)

En prosa:

> «Existe al menos un entero cuyo cuadrado no es igual a él mismo».

#### e)

Podemos tomar:

$$
x=2.
$$

Entonces:

$$
2^2\ne2.
$$

Por tanto, la negación es verdadera.

---

## Síntesis

Los cuantificadores universal y existencial están conectados por la negación.

Las dos leyes fundamentales son:

$$

\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x)

$$

y:

$$

\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).

$$

La lectura semántica es:

$$

\text{«no todos»}
\longleftrightarrow
\text{«al menos uno no»}

$$

y:

$$

\text{«no existe ninguno que cumpla»}
\longleftrightarrow
\text{«todos incumplen».}

$$

La regla práctica puede reconstruirse así:

$$

\text{negar cuantificador}
=
\text{cambiar }\forall\leftrightarrow\exists
+
\text{continuar la negación hacia la condición}.

$$

Pero las fórmulas cuantificadas pueden ser más complejas que: $\forall x\,P(x)$ o $\exists x\,P(x)$ Para leer correctamente expresiones mayores necesitaremos saber con precisión **qué parte de una fórmula controla cada cuantificador** y qué apariciones de las variables dependen de él.

## Hacia la sección siguiente

Consideremos:

$$
\forall x\,(P(x)\Rightarrow Q(x,y)).
$$

El símbolo $\forall x$ actúa sobre una parte determinada de la fórmula.

Además, las apariciones de $x$ y $y$ no tienen el mismo comportamiento lógico.

La próxima sección introducirá las herramientas necesarias para describir esa diferencia.
