## Síntesis del capítulo

Comenzamos con una escritura aparentemente sencilla:

$$
x+2=5.
$$

Descubrimos que no era todavía una proposición mientras el valor de $x$ permaneciera sin fijar.

Eso nos obligó a preguntar:

> ¿qué puede variar y sobre qué dominio?

A partir de ahí construimos el lenguaje de los predicados y de la cuantificación.

Aprendimos que:

$$
\forall x\,P(x)
$$

afirma que la condición se cumple para cada valor permitido, mientras:

$$
\exists x\,P(x)
$$

afirma que se cumple para al menos uno. La negación conectó ambos cuantificadores:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x),
$$

$$
\neg\exists x\,P(x)
\equiv
\forall x\,\neg P(x).
$$

Después vimos que los cuantificadores tienen **alcance**, que las apariciones de variables pueden ser **libres** o **ligadas**, y que una fórmula es **cerrada** cuando no queda ninguna aparición libre.

El orden introdujo una nueva dimensión:

$$
\forall x\,\exists y\,R(x,y)
$$

no significa, en general, lo mismo que:

$$
\exists y\,\forall x\,R(x,y).
$$

En cambio:

$$
\forall x\,\forall y\,R(x,y)
\equiv
\forall y\,\forall x\,R(x,y),
$$

y:

$$
\exists x\,\exists y\,R(x,y)
\equiv
\exists y\,\exists x\,R(x,y).
$$

También aprendimos a traducir entre prosa y símbolos, a distinguir variables de parámetros fijados por contexto y a expresar existencia única mediante:

$$
\exists!x\,P(x).
$$

Finalmente integramos estas piezas para leer y negar fórmulas largas sin perder el orden ni el alcance.

El principio rector del capítulo puede escribirse ahora con mayor precisión:

$$

\text{variable}
+
\text{dominio}
+
\text{predicado}
+
\text{cuantificador}
=
\text{afirmación matemática precisa}.

$$

Pero esta fórmula todavía contiene una palabra que hemos tratado de manera deliberadamente preteórica:

> **dominio**.

Hasta ahora nos ha bastado decir:

> «el dominio es el de los enteros»

o:

> «el dominio contiene ciertos valores».

El siguiente capítulo dará el paso que falta. Construiremos el lenguaje de los **conjuntos** para poder hablar de colecciones matemáticas como objetos, expresar pertenencia y, después, estudiar de manera precisa las funciones.

## Hacia el capítulo siguiente

Pasaremos de preguntar:

> «¿sobre qué objetos puede variar $x$?»

a construir un lenguaje en el que podamos escribir y estudiar esos dominios como objetos matemáticos.

La transición será:

$$
\boxed{
\text{dominios y predicados}
\longrightarrow
\text{conjuntos}
\longrightarrow
\text{funciones}.
}
$$

**Capítulo 4. Conjuntos y funciones: lenguaje básico**
