## Ejercicios

### El dominio que falta {#apm-t1-c03-e0201}
Considera:

$$
\exists x\,(2x=1).
$$

Una persona afirma:

> «La fórmula es verdadera».

Otra afirma:

> «La fórmula es falsa».

Explica por qué ninguna de las dos afirmaciones está suficientemente justificada mientras no se declare el dominio. Después compara los dominios de los enteros y de los racionales.

#### Solución


La fórmula:

$$
\exists x\,(2x=1)
$$

afirma que hay al menos un valor permitido de $x$ que satisface la ecuación.

Pero no sabemos todavía qué valores están permitidos.

#### Dominio de los enteros

No existe un entero:

$$
x
$$

tal que:

$$
2x=1.
$$

Por tanto, la fórmula es falsa.

#### Dominio de los racionales

Podemos tomar:

$$
x=\frac12.
$$

Entonces:

$$
2\cdot\frac12=1.
$$

Por tanto, la fórmula es verdadera.

Así, el diagnóstico correcto es:

$$
\boxed{
\text{falta declarar el dominio}.
}
$$

---

### «No todos» no es «todos no» {#apm-t1-c03-e0202}
El dominio contiene únicamente los valores:

$$
0
\qquad\text{y}\qquad
1.
$$

Definimos:

$$
P(x):\quad x=0.
$$

Compara:

$$
\neg\forall x\,P(x)
$$

con:

$$
\forall x\,\neg P(x).
$$

Determina el valor de verdad de cada una y explica el error de tratarlas como equivalentes.

#### Solución


Primero:

$$
\forall x\,P(x)
$$

afirma que tanto:

$$
0
$$

como:

$$
1
$$

son iguales a cero.

Eso es falso.

Por tanto:

$$
\neg\forall x\,P(x)
$$

es verdadera.

Ahora consideremos:

$$
\forall x\,\neg P(x).
$$

Esta fórmula afirma que ninguno de los dos valores es igual a cero.

Pero:

$$
0=0.
$$

Por tanto, la fórmula es falsa.

Así:

$$
\boxed{
\neg\forall x\,P(x)
\not\equiv
\forall x\,\neg P(x).
}
$$

«No todos» significa que hay al menos una excepción.

«Todos no» significa que todos incumplen la condición.

---

### La variable que quedó libre {#apm-t1-c03-e0203}
Considera:

$$
\forall x\,R(x,y).
$$

No se ha declarado ningún parámetro.

#### a)

Clasifica las apariciones de $x$ y $y$.

#### b)

Explica por qué la fórmula no está cerrada.

#### c)

¿Por qué no podemos decidir automáticamente si la reparación correcta es añadir $\forall y$ o $\exists y$?

#### Solución


#### a)

Las apariciones de:

$$
x
$$

están ligadas por:

$$
\forall x.
$$

La aparición de:

$$
y
$$

está libre porque no se encuentra bajo ningún cuantificador que cuantifique $y$.

#### b)

Una fórmula cerrada no contiene apariciones libres.

Como $y$ permanece libre:

$$
\forall x\,R(x,y)
$$

no está cerrada.

#### c)

No conocemos la afirmación que se pretendía expresar.

Podría querer decir:

> «Para todo $y$ y para todo $x$, se cumple $R(x,y)$»,

en cuyo caso escribiríamos:

$$
\forall y\,\forall x\,R(x,y).
$$

Pero también podría querer decir:

> «Existe un $y$ que funciona para todo $x$»,

en cuyo caso escribiríamos:

$$
\exists y\,\forall x\,R(x,y).
$$

Incluso podría ocurrir que $y$ debiera ser fijada como parámetro.

Por tanto, primero debemos reconstruir la intención y solo después reparar la fórmula.

---

### Refutar una inversión de cuantificadores {#apm-t1-c03-e0204}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x+1.
$$

Una persona afirma que:

$$
\forall x\,\exists y\,R(x,y)
$$

y:

$$
\exists y\,\forall x\,R(x,y)
$$

son equivalentes porque «usan los mismos símbolos».

Refuta la afirmación.

#### Solución


Consideremos primero:

$$
\forall x\,\exists y\,(y=x+1).
$$

Para cualquier entero $x$, podemos elegir:

$$
y=x+1.
$$

Por tanto, la fórmula es verdadera.

Ahora:

$$
\exists y\,\forall x\,(y=x+1)
$$

exigiría un único entero $y$ que funcionara para todos los enteros $x$.

Eso es imposible.

Para cualquier entero propuesto como $y$, tomemos:

$$
x=y.
$$

La condición exigiría:

$$
y=y+1,
$$

que es falsa.

Por tanto:

- la primera fórmula es verdadera;
- la segunda es falsa.

Así:

$$
\boxed{
\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y).
}
$$

El contraejemplo muestra que los cuantificadores mixtos no pueden intercambiarse en general.

---

### Existencia no implica unicidad {#apm-t1-c03-e0205}
Trabajamos con valores enteros.

Una persona observa que:

$$
2^2=4
$$

y concluye:

$$
\exists!x\,(x^2=4).
$$

Refuta la conclusión y explica exactamente qué parte del razonamiento sí es válida.

#### Solución


El cálculo:

$$
2^2=4
$$

muestra que:

$$
x=2
$$

es un testigo.

Por tanto, sí podemos concluir:

$$
\exists x\,(x^2=4).
$$

Pero también:

$$
(-2)^2=4.
$$

Tenemos dos valores distintos:

$$
2\ne-2
$$

que satisfacen la condición.

Por tanto:

$$
\exists!x\,(x^2=4)
$$

es falsa.

La parte válida del razonamiento establece **existencia**.

El error consiste en inferir **unicidad** a partir de un solo testigo.

---

### Diagnóstico integral {#apm-t1-c03-e0206}
Trabajamos con valores enteros.

Queremos expresar:

> «No es verdad que para cada entero $x$ exista un entero $y$ tal que $x+y=0$».

Una persona propone:

$$
\forall x\,\exists y\,(x+y\ne0).
$$

Otra propone:

$$
\exists y\,\forall x\,(x+y\ne0).
$$

#### a)

Escribe primero la traducción directa correcta de la frase, conservando la negación exterior.

#### b)

Transforma completamente esa negación mediante [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007).

#### c)

Diagnostica el error de la primera propuesta.

#### d)

Diagnostica el error de la segunda propuesta.

#### e)

Determina el valor de verdad de la afirmación original sobre los enteros.

#### f)

Explica qué información tuviste que controlar para resolver correctamente todo el problema.

#### Solución


#### a)

La frase interior es:

> «Para cada entero $x$, existe un entero $y$ tal que $x+y=0$».

Eso se escribe:

$$
\forall x\,\exists y\,(x+y=0).
$$

La frase completa niega esa afirmación.

Por tanto:

$$
\boxed{
\neg\forall x\,\exists y\,(x+y=0).
}
$$

#### b)

Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-t1-c03-p0007) una capa a la vez:

$$
\neg\forall x\,\exists y\,(x+y=0)
\equiv
\exists x\,\neg\exists y\,(x+y=0).
$$

Después:

$$
\exists x\,\neg\exists y\,(x+y=0)
\equiv
\exists x\,\forall y\,\neg(x+y=0).
$$

Negando la igualdad:

$$
\boxed{
\exists x\,\forall y\,(x+y\ne0).
}
$$

#### c)

La primera propuesta era:

$$
\forall x\,\exists y\,(x+y\ne0).
$$

El error consiste en haber negado solamente la condición interna:

$$
x+y=0
$$

sin cambiar los cuantificadores atravesados por la negación.

La negación correcta de:

$$
\forall x\,\exists y
$$

produce:

$$
\exists x\,\forall y.
$$

#### d)

La segunda propuesta era:

$$
\exists y\,\forall x\,(x+y\ne0).
$$

Esta fórmula sí usa un existencial y un universal, pero **invierte el orden de las variables**.

La transformación correcta conserva:

$$
x
\quad\text{antes que}\quad
y.
$$

Por tanto, debe ser:

$$
\exists x\,\forall y\,(x+y\ne0).
$$

#### e)

La afirmación interior:

$$
\forall x\,\exists y\,(x+y=0)
$$

es verdadera sobre los enteros.

Para cada entero:

$$
x,
$$

podemos elegir:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

Por tanto, su negación:

$$
\neg\forall x\,\exists y\,(x+y=0)
$$

es falsa.

La forma transformada:

$$
\exists x\,\forall y\,(x+y\ne0)
$$

también es falsa.

Para cualquier entero $x$, podemos elegir:

$$
y=-x,
$$

y entonces:

$$
x+y=0.
$$

#### f)

Para resolver el problema tuvimos que controlar:

- el dominio;
- las variables;
- el orden de los cuantificadores;
- el alcance de la negación;
- las leyes de negación de cuantificadores;
- la negación de la igualdad;
- la lectura en prosa;
- el valor de verdad final.

El diagnóstico integral puede resumirse:

$$
\boxed{
\text{contexto}
+
\text{estructura}
+
\text{equivalencias justificadas}
+
\text{control semántico}.
}
$$

---
