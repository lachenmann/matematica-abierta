## §10. Leer antes de operar

Este capítulo comenzó con una pregunta muy sencilla:

> ¿qué estamos mirando cuando vemos una expresión matemática?

Desde entonces hemos aprendido que una escritura algebraica no es una fila de símbolos sobre la que debamos actuar inmediatamente.

Antes de operar podemos tener que:

- reconocer la estructura;
- interpretar el papel de una letra;
- distinguir términos y factores;
- sustituir un valor;
- leer una igualdad;
- decidir si una igualdad expresa un patrón general o una condición;
- justificar una transformación;
- aclarar el alcance de una operación;
- detectar una regla falsa.

La idea que reúne todo el capítulo es:

$$
\boxed{
\text{leer}
\longrightarrow
\text{decidir}
\longrightarrow
\text{operar o justificar}.
}
$$

No siempre la primera acción correcta es calcular.

A veces debemos detenernos y preguntar:

> **¿qué clase de objeto matemático tengo delante y qué se me está pidiendo hacer con él?**

Esta última sección no introducirá nuevas reglas. Su función es reunir las anteriores en problemas donde la técnica apropiada no viene anunciada de antemano.

---

### 10.1 Una misma escritura puede invitar a preguntas distintas

Consideremos:

$$
2(x+3)+x.
$$

Podríamos preguntar:

> ¿cuál es su operación principal?

O:

> ¿cuánto vale cuando $x=-2$?

O:

> ¿puede transformarse en una forma más simple?

Cada pregunta exige una acción distinta.

#### Pregunta estructural

La expresión completa es una suma:

$$
2(x+3)+x.
$$

Sus dos términos exteriores son:

$$
2(x+3)
\qquad\text{y}\qquad
x.
$$

#### Pregunta de evaluación

Si:

$$
x=-2,
$$

sustituimos:

$$
2((-2)+3)+(-2)
=
2\cdot1-2
=
0.
$$

#### Pregunta de transformación

Podemos escribir:

$$
\begin{aligned}
2(x+3)+x
&=2x+6+x\\
&=3x+6.
\end{aligned}
$$

Las tres respuestas hablan de la misma expresión, pero responden a preguntas diferentes.

::: {.ma-block .ma-intuicion}
**Idea clave**

Una buena lectura comienza identificando **qué problema se está planteando**, no aplicando automáticamente la última técnica aprendida.
:::

---

### 10.2 Antes de transformar, comprueba qué estás transformando

Consideremos:

$$
3x+5.
$$

No tiene sentido preguntar simplemente:

> «¿cuánto da?»

si no conocemos el valor de $x$.

Tampoco tiene sentido «simplificar» por obligación:

$$
3x+5
$$

ya expresa con claridad una suma de dos términos.

En cambio, si encontramos:

$$
3x+5+2x,
$$

podemos reconocer una estructura que permite escribir:

$$
\begin{aligned}
3x+5+2x
&=3x+2x+5\\
&=5x+5.
\end{aligned}
$$

La diferencia no consiste en que una expresión sea «larga» y otra «corta».

Consiste en que una ley algebraica ofrece una transformación útil.

---

### 10.3 Antes de confiar en una igualdad, pregúntate qué afirma

Comparemos:

$$
3(x+2)=3x+6
$$

y:

$$
3x+2=11.
$$

En el primer caso, reconocemos una identidad basada en distributividad.

En el segundo, reconocemos una ecuación: la igualdad impone una condición sobre $x$.

Ahora comparemos:

$$
3(x+2)=3x+2.
$$

Aquí no basta con observar que «hay distributividad».

Precisamente la distributividad nos permite detectar que la transformación está mal:

$$
3(x+2)
=
3x+6,
$$

no:

$$
3x+2.
$$

Podemos confirmarlo con un valor sencillo, por ejemplo:

$$
x=0.
$$

La igualdad falsa produciría:

$$
6=2.
$$

Así, una misma lectura estructural nos permite:

- reconocer una identidad correcta;
- reconocer una ecuación;
- refutar una supuesta identidad.

---

### 10.4 Antes de cancelar, busca factores

Consideremos:

$$
\frac{x(x+4)}{x}
$$

y:

$$
\frac{x+4}{x}.
$$

En la primera expresión, cuando $x\ne0$, existe un factor común $x$:

$$
\frac{x(x+4)}{x}=x+4.
$$

En la segunda, $x$ es solo un término del numerador:

$$
\frac{x+4}{x}
=
1+\frac4x,
\qquad x\ne0.
$$

No se cancela.

La pregunta adecuada antes de tachar símbolos es:

> ¿lo que quiero cancelar es realmente un factor de toda la expresión correspondiente?

El hábito de **leer antes de operar** evita aquí un error que no podría corregirse únicamente con rapidez de cálculo.

---

### 10.5 Antes de aceptar una notación, reconstruye su alcance

Comparemos:

$$
-x^2
$$

con:

$$
(-x)^2.
$$

O:

$$
\frac{a+b}{c}
$$

con:

$$
a+\frac bc.
$$

En cada par, pequeños cambios de notación producen estructuras distintas.

Cuando recibimos una expresión compleja, conviene leerla desde fuera hacia dentro:

1. identificar la operación exterior;
2. reconocer sus partes principales;
3. continuar con las subexpresiones;
4. solo después operar.

Este procedimiento no añade una regla nueva al álgebra.

Añade disciplina a la lectura.

---

### 10.6 Un protocolo mínimo para afrontar una expresión

Podemos reunir el capítulo en una secuencia de preguntas.

#### 1. ¿Qué está escrito?

¿Es una expresión, una igualdad, una cadena de igualdades?

#### 2. ¿Cuál es su estructura?

¿Qué operación actúa desde fuera? ¿Cuáles son las subexpresiones?

#### 3. ¿Qué significan las letras?

¿Hay valores dados? ¿Son variables generales? ¿Hay alguna por determinar?

#### 4. ¿Qué se pide?

¿Evaluar, transformar, comparar, justificar, refutar?

#### 5. Si transformo, ¿qué ley uso?

¿Conmutatividad, asociatividad, distributividad u otra regla ya establecida?

#### 6. Si sospecho que algo es falso, ¿puedo probar un caso sencillo?

El valor concreto puede revelar rápidamente una inconsistencia.

#### 7. ¿La escritura final conserva lo que quería expresar?

¿Los paréntesis, exponentes y barras de fracción tienen el alcance correcto?

Este protocolo resume la transición que buscaba el capítulo:

$$
\boxed{
\text{hacer cuentas}
\longrightarrow
\text{leer estructuras}
\longrightarrow
\text{justificar transformaciones}.
}
$$

---

## Problemas de síntesis

### Una expresión, varias preguntas {#apm-t1-c01-e0052}

Considera:

$$
4(x-1)+2x.
$$

#### a)

Identifica la operación principal y los términos exteriores.

#### b)

Evalúa la expresión cuando:

$$
x=3.
$$

#### c)

Transfórmala a una expresión de la forma:

$$
ax+b
$$

y justifica cada paso.

#### Solución

#### a)

La operación principal es una suma.

Los términos exteriores son:

$$
4(x-1)
$$

y:

$$
2x.
$$

#### b)

Sustituimos:

$$
x=3.
$$

Entonces:

$$
4(3-1)+2\cdot3
=
4\cdot2+6
=
14.
$$

#### c)

Por distributividad:

$$
4(x-1)+2x
=
4x-4+2x.
$$

Reordenamos y agrupamos:

$$
4x-4+2x
=
4x+2x-4.
$$

Por distributividad en sentido inverso:

$$
4x+2x-4
=
(4+2)x-4.
$$

Por aritmética:

$$
(4+2)x-4
=
6x-4.
$$

Así:

$$
\boxed{4(x-1)+2x=6x-4}.
$$

---

### Una línea, dos estructuras {#apm-t1-c01-e0053}

Considera la escritura lineal:

```text
12/3+1
```

#### a)

Escríbela de manera inequívoca si se quiere representar:

$$
\frac{12}{3}+1.
$$

Calcula su valor e identifica la operación principal.

#### b)

Modifica los paréntesis para representar:

$$
\frac{12}{3+1}.
$$

Calcula su valor e identifica la operación principal.

#### c)

Explica por qué una escritura lineal clara debe conservar la estructura de la expresión original.

#### Solución

#### a)

Podemos escribir:

```text
(12/3)+1
```

o simplemente:

```text
12/3+1
```

si usamos la precedencia usual.

La expresión matemática es:

$$
\frac{12}{3}+1.
$$

Calculamos:

$$
\frac{12}{3}+1
=
4+1
=
5.
$$

La operación principal es la suma.

#### b)

Debemos escribir:

```text
12/(3+1)
```

porque todo $3+1$ forma el denominador.

Entonces:

$$
\frac{12}{3+1}
=
\frac{12}{4}
=
3.
$$

La operación principal es la división.

#### c)

Las dos expresiones contienen los mismos números y signos básicos, pero los paréntesis determinan agrupamientos diferentes.

Por tanto:

$$
\boxed{
\text{la escritura lineal debe conservar el alcance de las operaciones}.
}
$$


### Reparar una cadena {#apm-t1-c01-e0054}

Un estudiante quiere calcular:

$$
3(5+1)+2.
$$

Escribe:

$$
5+1=6\cdot3=18+2=20.
$$

#### a)

Explica por qué la cadena es incorrecta.

#### b)

Escribe una cadena correcta.

#### c)

Indica qué principio sobre el signo igual estás utilizando.

#### Solución

#### a)

La cadena usa $=$ como si significara «y después».

Por ejemplo, afirma:

$$
5+1=6\cdot3,
$$

es decir:

$$
6=18,
$$

lo cual es falso.

#### b)

Debemos conservar el valor de la expresión original:

$$
\begin{aligned}
3(5+1)+2
&=3\cdot6+2\\
&=18+2\\
&=20.
\end{aligned}
$$

#### c)

Cada signo igual afirma que las expresiones que conecta representan el mismo valor.

Por eso todos los miembros de una cadena correcta de igualdades deben representar lo mismo.

---

### Identidad, ecuación o falsa regla {#apm-t1-c01-e0055}

Clasifica cada escritura en el contexto indicado.

#### a)

> «La distributividad nos da»:

$$
7(x+2)=7x+14.
$$

#### b)

> «Determina qué valores de $x$ hacen verdadera»:

$$
7x+2=16.
$$

#### c)

> «Esta regla vale para cualquier $x$»:

$$
7(x+2)=7x+2.
$$

En el caso c), decide además si la afirmación es correcta.

#### Solución

#### a)

Se presenta como una **identidad**.

La distributividad justifica:

$$
7(x+2)
=
7x+14.
$$

#### b)

Se presenta como una **ecuación**.

La pregunta pide determinar qué valores de $x$ hacen verdadera la igualdad.

No necesitamos resolverla aquí para clasificarla.

#### c)

Se pretende presentar como una identidad, pero es falsa.

Tomemos:

$$
x=0.
$$

Entonces el lado izquierdo vale:

$$
7(0+2)=14,
$$

mientras que el derecho vale:

$$
7\cdot0+2=2.
$$

Como:

$$
14\ne2,
$$

la supuesta identidad queda refutada.

---

### Diagnóstico final {#apm-t1-c01-e0056}

Un estudiante escribe:

$$
\frac{2x+6}{2}=x+6.
$$

#### a)

Decide si la igualdad es correcta.

#### b)

Si es falsa, encuentra un contraejemplo numérico.

#### c)

Analiza la estructura del numerador.

#### d)

Corrige la transformación.

#### Solución

#### a)

La igualdad es falsa.

#### b)

Tomemos:

$$
x=0.
$$

Entonces:

$$
\frac{2\cdot0+6}{2}
=
\frac62
=
3,
$$

mientras que:

$$
0+6=6.
$$

Por tanto:

$$
3\ne6.
$$

#### c)

El numerador es:

$$
2x+6.
$$

Podemos extraer el factor común $2$:

$$
2x+6
=
2x+2\cdot3
=
2(x+3).
$$

#### d)

Así:

$$
\frac{2x+6}{2}
=
\frac{2(x+3)}{2}
=
x+3.
$$

La transformación correcta es:

$$
\boxed{
\frac{2x+6}{2}=x+3.
}
$$

El error consistió en dividir correctamente $2x$ por $2$, pero no dividir también $6$ por $2$.

---

## Cierre del capítulo

El objetivo de este capítulo no era enseñar una colección de trucos algebraicos.

Era cambiar la manera de mirar una escritura matemática.

Comenzamos distinguiendo una expresión de su valor.

Después vimos que las letras adquieren significado por el contexto, que una expresión tiene partes y niveles, y que sustituir exige conservar su estructura.

Aprendimos que:

$$
=
$$

no significa «ahora hago otra cosa», sino que afirma igualdad.

Distinguimos una identidad de una ecuación en un primer sentido operativo.

Vimos que transformar una expresión exige una ley, que la notación debe hacer visible el alcance de las operaciones y que muchas reglas falsas nacen de aplicar una regla correcta a la estructura equivocada.

Podemos condensar el capítulo en cinco hábitos.

::: {.ma-block .ma-observacion}
**Síntesis**

**1. Leer antes de calcular.**  
**2. Conservar la estructura al sustituir.**  
**3. Usar el signo igual con significado.**  
**4. Justificar cada transformación.**  
**5. Buscar la estructura antes de aplicar una regla.**
:::

El resultado no es todavía una teoría abstracta del álgebra.

Es algo previo y necesario: una disciplina del lenguaje simbólico.

---

## Hacia el capítulo siguiente

Consideremos ahora dos afirmaciones:

$$
x=2
$$

y:

$$
x^2=4.
$$

Podemos preguntar:

- si la primera es correcta, ¿qué podemos decir de la segunda?
- si la segunda es correcta, ¿podemos concluir la primera?
- ¿cómo expresamos «y», «o» y «no» dentro del razonamiento matemático?
- ¿cuándo dos afirmaciones dicen esencialmente lo mismo?
- ¿cómo podemos transformar una afirmación sin cambiar su contenido?

Hasta ahora hemos trabajado principalmente con **expresiones** e **igualdades**.

El paso siguiente será estudiar las afirmaciones mismas y las operaciones que podemos realizar con ellas.

Eso abre:

**Capítulo 2. Lógica proposicional y álgebra de proposiciones**

Allí encontraremos una nueva clase de objetos simbólicos y una nueva colección de operaciones y leyes.

La misma idea estructural reaparecerá:

$$
\boxed{
\text{objetos}
+
\text{operaciones}
+
\text{leyes}.
}
$$

Y descubriremos que el tipo de pensamiento que acabamos de practicar con expresiones algebraicas puede aplicarse también al razonamiento lógico.
