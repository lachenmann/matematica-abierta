## §11. Leer y negar fórmulas cuantificadas largas

Hasta ahora hemos estudiado por separado:

- negación;
- cuantificadores;
- alcance;
- variables libres y ligadas;
- orden;
- conectivos proposicionales.

Ahora debemos hacerlos trabajar juntos. Consideremos:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Esta fórmula contiene tres capas lógicas:

1. una negación exterior;
2. un cuantificador universal;
3. un cuantificador existencial.

No conviene intentar transformarla «de un vistazo». La estrategia será leer y operar **desde fuera hacia dentro**, una capa a la vez.

Aplicando [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007) al cuantificador exterior:

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

Aplicamos de nuevo [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\exists x\,\neg\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
$$

Así obtenemos:

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
}
$$

La transformación no intercambia arbitrariamente cuantificadores. Cada cambio ocurre porque una negación atraviesa un cuantificador.

---

### 11.1 Leer la estructura antes de transformar

Ante una fórmula como:

$$
\neg\forall x\,\exists y\,R(x,y),
$$

conviene responder primero:

#### ¿Cuál es la operación exterior?

La negación:

$$
\neg.
$$

#### ¿Qué fórmula está siendo negada?

$$
\forall x\,\exists y\,R(x,y).
$$

#### ¿Cuál es el cuantificador exterior de esa fórmula?

$$
\forall x.
$$

#### ¿Qué queda dentro de su alcance?

$$
\exists y\,R(x,y).
$$

Solo después de identificar esta estructura comenzamos la transformación.

Podemos resumir:

$$

\text{leer primero}
\longrightarrow
\text{transformar después}.

$$

---

### 11.2 Una negación atraviesa los cuantificadores uno por uno

Recordemos [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

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

La negación cambia el tipo de cuantificador:

$$
\forall
\longleftrightarrow
\exists
$$

y continúa hacia el interior. Por tanto:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

no se transforma directamente por una regla nueva. Usamos dos veces una regla ya conocida.

#### Primer paso

Tomamos como condición completa:

$$
P(x):\quad \exists y\,R(x,y).
$$

Entonces:

$$
\neg\forall x\,P(x)
\equiv
\exists x\,\neg P(x).
$$

Por tanto:

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

#### Segundo paso

Ahora la negación exterior alcanza:

$$
\exists y\,R(x,y).
$$

Aplicamos nuevamente [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\exists y\,R(x,y)
\equiv
\forall y\,\neg R(x,y).
$$

Así:

$$
\exists x\,\neg\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
$$

---

### 11.3 El orden final no se elige libremente

Observemos qué ocurrió:

$$
\forall x\,\exists y
$$

se convirtió, bajo negación, en:

$$
\exists x\,\forall y.
$$

Pero no hemos intercambiado:

$$
x
\qquad\text{y}\qquad
y.
$$

El orden de las variables sigue siendo el mismo.

Lo que cambió fue el tipo de cada cuantificador al ser atravesado por la negación.

Por tanto:

$$

\neg\forall x\,\exists y
\quad\longrightarrow\quad
\exists x\,\forall y\,\neg

$$

y no:

$$
\forall y\,\exists x\,\neg
$$

ni ninguna otra permutación arbitraria. La regla práctica es:

$$

\text{conservar el orden de las variables}
\quad+\quad
\text{cambiar cada cuantificador atravesado por }\neg.

$$

---

### 11.4 Llegar hasta el predicado

Una negación puede quedar finalmente delante de una condición elemental:

$$
\neg R(x,y).
$$

En ese punto ya no hay cuantificadores que atravesar.

Por ejemplo, $\neg\exists x\,\forall y\,R(x,y)$ se transforma:

$$
\neg\exists x\,\forall y\,R(x,y)
\equiv
\forall x\,\neg\forall y\,R(x,y)
$$

y después:

$$
\forall x\,\neg\forall y\,R(x,y)
\equiv
\forall x\,\exists y\,\neg R(x,y).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\forall y\,R(x,y)
\equiv
\forall x\,\exists y\,\neg R(x,y).
}
$$

De nuevo, la negación ha llegado hasta el predicado.

---

### 11.5 Cuando dentro hay conectivos

Consideremos:

$$
\neg\forall x\,\bigl(P(x)\Rightarrow Q(x)\bigr).
$$

Primero atravesamos el cuantificador:

$$
\neg\forall x\,\bigl(P(x)\Rightarrow Q(x)\bigr)
\equiv
\exists x\,\neg\bigl(P(x)\Rightarrow Q(x)\bigr).
$$

En [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md) demostramos:

$$
\neg(A\Rightarrow B)
\equiv
A\land\neg B.
$$

Aplicándola:

$$
\exists x\,\neg\bigl(P(x)\Rightarrow Q(x)\bigr)
\equiv
\exists x\,\bigl(P(x)\land\neg Q(x)\bigr).
$$

Así:

$$
\boxed{
\neg\forall x\,\bigl(P(x)\Rightarrow Q(x)\bigr)
\equiv
\exists x\,\bigl(P(x)\land\neg Q(x)\bigr).
}
$$

En prosa:

> «No todo objeto que cumple $P$ cumple $Q$»

equivale a:

> «Existe al menos un objeto que cumple $P$ y no cumple $Q$».

Aquí se combinan una ley cuantificacional y una ley proposicional.

---

### 11.6 De Morgan dentro de una fórmula cuantificada

Consideremos:

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr).
$$

Primero negamos el cuantificador:

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\neg\bigl(P(x)\land Q(x)\bigr).
$$

Después aplicamos De Morgan:

$$
\neg\bigl(P(x)\land Q(x)\bigr)
\equiv
\neg P(x)\lor\neg Q(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\bigl(\neg P(x)\lor\neg Q(x)\bigr).
}
$$

La transformación ocurre por capas:

$$
\boxed{
\text{cuantificador}
\longrightarrow
\text{conectivo}
\longrightarrow
\text{condiciones elementales}.
}
$$

---

### 11.7 Un protocolo de lectura y transformación

Cuando una fórmula cuantificada es larga, seguiremos este orden.

#### Paso 1 — Identificar la operación exterior

Puede ser:

- una negación;
- un cuantificador;
- un conectivo proposicional.

#### Paso 2 — Marcar el alcance

Preguntar qué parte de la fórmula controla esa operación.

#### Paso 3 — Aplicar una sola equivalencia

No saltar varias capas a la vez.

#### Paso 4 — Repetir desde la nueva operación exterior relevante

Si queda: $\neg\forall$ o $\neg\exists$, volver a usar [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007).

#### Paso 5 — Cuando la negación llegue a conectivos, usar las leyes de [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md)

Por ejemplo:

$$
\neg(A\land B)
\equiv
\neg A\lor\neg B,
$$

$$
\neg(A\lor B)
\equiv
\neg A\land\neg B,
$$

$$
\neg(A\Rightarrow B)
\equiv
A\land\neg B.
$$

#### Paso 6 — Leer el resultado en prosa

Esto sirve como control semántico. El procedimiento puede resumirse:

$$
\boxed{
\text{estructura}
\longrightarrow
\text{una equivalencia}
\longrightarrow
\text{nueva estructura}
\longrightarrow
\cdots
\longrightarrow
\text{lectura final}.
}
$$

---

### 11.8 No cambiar más de lo que autoriza cada ley

Supongamos que partimos de:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Sería incorrecto escribir directamente:

$$
\forall x\,\exists y\,\neg R(x,y).
$$

¿Por qué?

Porque al negar:

$$
\forall x
$$

debemos cambiarlo por:

$$
\exists x.
$$

Y al negar:

$$
\exists y
$$

debemos cambiarlo por:

$$
\forall y.
$$

La transformación correcta es:

$$
\exists x\,\forall y\,\neg R(x,y).
$$

Una buena práctica es exigir que **cada cambio de símbolo tenga una razón identificable**.

Si un cuantificador cambia, debemos poder señalar qué negación lo atravesó.

Si un conectivo cambia, debemos poder señalar qué ley proposicional estamos usando.

---

### 11.9 Comprobación semántica con un dominio pequeño

Las equivalencias se justifican por las leyes ya demostradas.

Pero un ejemplo concreto puede ayudarnos a detectar errores.

Tomemos un dominio formado únicamente por los valores:

$$
0
\qquad\text{y}\qquad
1,
$$

y definamos:

$$
R(x,y):\quad x<y.
$$

Consideremos $\forall x\,\exists y\,R(x,y)$ Para:

$$
x=1,
$$

no hay ningún valor permitido de $y$ tal que:

$$
1<y.
$$

Por tanto, la afirmación universal-existencial es falsa. Su negación:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

es verdadera. Ahora examinemos la forma equivalente:

$$
\exists x\,\forall y\,\neg R(x,y).
$$

Tomemos $x=1$ Para: $y=0$ y $y=1$, se cumple:

$$
\neg(1<y).
$$

La fórmula es verdadera. Las dos formas tienen el mismo valor de verdad, como corresponde.

Este ejemplo no reemplaza la derivación. Funciona como **control semántico**.

---

### 11.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0031}
**Ejemplo — Negar dos cuantificadores sin perder el orden**
:::

Partimos de:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Queremos llevar la negación hasta el predicado.

#### Paso 1 — Identificar la primera capa

La fórmula negada comienza con:

$$
\forall x.
$$

Aplicamos [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

#### Paso 2 — Identificar la segunda capa

Ahora tenemos $\neg\exists y\,R(x,y)$. Aplicamos de nuevo [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\exists y\,R(x,y)
\equiv
\forall y\,\neg R(x,y).
$$

Sustituyendo:

$$
\exists x\,\neg\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
$$

#### Resultado

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
}
$$

#### Lectura de la primera fórmula

> «No es verdad que para todo $x$ exista algún $y$ para el cual se cumple $R(x,y)$».

#### Lectura de la segunda

> «Existe algún $x$ tal que, para todo $y$, no se cumple $R(x,y)$».

Las dos frases expresan la misma situación:

> hay al menos un valor de $x$ para el cual ningún valor de $y$ consigue hacer verdadera $R(x,y)$.

#### Qué no hicimos

No intercambiamos:

$$
x
\qquad\text{y}\qquad
y.
$$

No inventamos una nueva regla. Aplicamos dos veces:

$$
\neg\forall
\equiv
\exists\neg
$$

o:

$$
\neg\exists
\equiv
\forall\neg,
$$

según correspondía.

---
## Ejercicios

### Negar dos cuantificadores {#apm-i-e0195}
Niega y transforma completamente:

$$
\forall x\,\exists y\,R(x,y).
$$

La respuesta final debe tener la negación aplicada directamente al predicado.

#### Solución


Comenzamos:

$$
\neg\forall x\,\exists y\,R(x,y).
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\neg\exists y\,R(x,y).
$$

Aplicamos nuevamente [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\exists y\,R(x,y)
\equiv
\forall y\,\neg R(x,y).
$$

Por tanto:

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\equiv
\exists x\,\forall y\,\neg R(x,y).
}
$$

---

### Negar un cuantificador y una conjunción {#apm-i-e0196}
Niega completamente:

$$
\exists x\,\bigl(P(x)\land Q(x)\bigr).
$$

#### Solución


Partimos de:

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr).
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\neg\bigl(P(x)\land Q(x)\bigr).
$$

Aplicamos De Morgan:

$$
\neg\bigl(P(x)\land Q(x)\bigr)
\equiv
\neg P(x)\lor\neg Q(x).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\bigl(P(x)\land Q(x)\bigr)
\equiv
\forall x\,\bigl(\neg P(x)\lor\neg Q(x)\bigr).
}
$$

---

### Justificar cada cambio {#apm-i-e0197}
Explica cada paso de:

$$
\neg\exists x\,\forall y\,P(x,y)
\equiv
\forall x\,\exists y\,\neg P(x,y).
$$

#### Solución


Comenzamos con:

$$
\neg\exists x\,\forall y\,P(x,y).
$$

La negación alcanza primero al cuantificador:

$$
\exists x.
$$

Por [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\exists x\,\forall y\,P(x,y)
\equiv
\forall x\,\neg\forall y\,P(x,y).
$$

Ahora la negación alcanza al cuantificador:

$$
\forall y.
$$

Aplicamos nuevamente [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\neg\forall y\,P(x,y)
\equiv
\exists y\,\neg P(x,y).
$$

Así:

$$
\forall x\,\neg\forall y\,P(x,y)
\equiv
\forall x\,\exists y\,\neg P(x,y).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\forall y\,P(x,y)
\equiv
\forall x\,\exists y\,\neg P(x,y).
}
$$

Cada cuantificador cambió porque una negación lo atravesó.

El orden de las variables:

$$
x,\ y
$$

se conservó.

---

### Detectar una negación incorrecta {#apm-i-e0198}
Trabajamos con valores enteros y definimos:

$$
R(x,y):\quad y=x.
$$

Una persona afirma que:

$$
\neg\forall x\,\exists y\,R(x,y)
\equiv
\forall x\,\exists y\,\neg R(x,y).
$$

Demuestra mediante esta interpretación concreta que la equivalencia propuesta es falsa.

#### Solución


Primero analizamos:

$$
\forall x\,\exists y\,R(x,y).
$$

Como:

$$
R(x,y):\quad y=x,
$$

para cada entero $x$ podemos elegir:

$$
y=x.
$$

Por tanto:

$$
\forall x\,\exists y\,R(x,y)
$$

es verdadera.

Su negación:

$$
\neg\forall x\,\exists y\,R(x,y)
$$

es, entonces, falsa.

Ahora evaluemos la fórmula propuesta como equivalente:

$$
\forall x\,\exists y\,\neg R(x,y).
$$

Esto dice:

> «Para todo entero $x$, existe un entero $y$ distinto de $x$».

Es verdadera.

Para cada entero $x$ podemos tomar:

$$
y=x+1.
$$

Entonces:

$$
y\ne x.
$$

Hemos obtenido:

- lado izquierdo: falso;
- lado derecho: verdadero.

Por tanto:

$$
\boxed{
\neg\forall x\,\exists y\,R(x,y)
\not\equiv
\forall x\,\exists y\,\neg R(x,y).
}
$$

La transformación incorrecta no cambió los tipos de cuantificador como exige [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007).

---

### Transformar y volver a la prosa {#apm-i-e0199}
El dominio está previamente fijado.

Niega completamente:

$$
\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr).
$$

Después expresa la fórmula final en prosa.

#### Solución


Partimos de:

$$
\neg\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr).
$$

Primero:

$$
\neg\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr)
\equiv
\forall x\,\neg\forall y\,\bigl(P(x)\lor Q(y)\bigr).
$$

Después:

$$
\forall x\,\neg\forall y\,\bigl(P(x)\lor Q(y)\bigr)
\equiv
\forall x\,\exists y\,\neg\bigl(P(x)\lor Q(y)\bigr).
$$

Aplicamos De Morgan:

$$
\neg\bigl(P(x)\lor Q(y)\bigr)
\equiv
\neg P(x)\land\neg Q(y).
$$

Por tanto:

$$
\boxed{
\neg\exists x\,\forall y\,\bigl(P(x)\lor Q(y)\bigr)
\equiv
\forall x\,\exists y\,\bigl(\neg P(x)\land\neg Q(y)\bigr).
}
$$

Una lectura en prosa de la fórmula final es:

> «Para todo valor de $x$, existe al menos un valor de $y$ tal que $x$ no cumple $P$ y $y$ no cumple $Q$».

La lectura conserva el orden:

$$
\forall x\,\exists y.
$$

---

### Tres capas y conectivos {#apm-i-e0200}
Niega completamente:

$$
\forall x\,\exists y\,\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

Muestra todas las equivalencias hasta que la negación haya llegado a las condiciones elementales.

#### Solución


Partimos de:

$$
\neg\forall x\,\exists y\,\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Primera capa

Por [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\equiv
\exists x\,\neg\exists y\,\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Segunda capa

De nuevo por [la proposición «Leyes de negación de cuantificadores»](#apm-i-p0007):

$$
\equiv
\exists x\,\forall y\,\neg\forall z\,
\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Tercera capa

Otra vez:

$$
\equiv
\exists x\,\forall y\,\exists z\,
\neg\bigl(
P(x,z)\Rightarrow(Q(y)\lor R(x,y,z))
\bigr).
$$

#### Negar la implicación

En [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md) demostramos:

$$
\neg(A\Rightarrow B)
\equiv
A\land\neg B.
$$

Por tanto:

$$
\equiv
\exists x\,\forall y\,\exists z\,
\Bigl(
P(x,z)\land
\neg(Q(y)\lor R(x,y,z))
\Bigr).
$$

#### Aplicar De Morgan

$$
\neg(Q(y)\lor R(x,y,z))
\equiv
\neg Q(y)\land\neg R(x,y,z).
$$

Así:

$$
\equiv
\exists x\,\forall y\,\exists z\,
\Bigl(
P(x,z)\land
(\neg Q(y)\land\neg R(x,y,z))
\Bigr).
$$

Por asociatividad de la conjunción podemos escribir:

$$
\boxed{
\exists x\,\forall y\,\exists z\,
\bigl(
P(x,z)\land
\neg Q(y)\land
\neg R(x,y,z)
\bigr).
}
$$

#### Control de la estructura

Los cuantificadores originales eran:

$$
\forall x\,\exists y\,\forall z.
$$

Al atravesarlos la negación se convirtieron, en el mismo orden, en:

$$
\exists x\,\forall y\,\exists z.
$$

Después la negación alcanzó la implicación y finalmente las condiciones elementales.

No se permutó ninguna variable.

---

## Síntesis

Una fórmula cuantificada larga debe transformarse por **capas**. El principio básico es:

$$

\text{leer desde fuera hacia dentro}

$$

y aplicar una sola equivalencia en cada paso. Cuando una negación atraviesa cuantificadores:

$$

\forall
\longleftrightarrow
\exists

$$

mientras el orden de las variables se conserva. Cuando la negación alcanza conectivos proposicionales, utilizamos las leyes ya demostradas en [el capítulo 2](algebra-para-matematicos-capitulo-2-logica-proposicional-y-algebra-de-proposiciones.md).

Así, $\neg\forall x\,\exists y\,R(x,y)$ se transforma en:

$$

\exists x\,\forall y\,\neg R(x,y).

$$

Y una fórmula más compleja puede exigir una cadena como:

$$

\text{cuantificadores}
\longrightarrow
\text{conectivos}
\longrightarrow
\text{condiciones elementales}.

$$

El criterio de seguridad es sencillo:

> **cada cambio de símbolo debe poder justificarse por una equivalencia ya demostrada.**

Nos queda una última tarea. Ya sabemos construir, leer, traducir y negar fórmulas cuantificadas.

Ahora debemos aprender a detectar rápidamente cuándo una fórmula o una traducción está mal formada conceptualmente.

## Hacia la sección siguiente

Los errores más frecuentes ya han aparecido a lo largo del capítulo:

- olvidar el dominio;
- confundir $\forall$ con $\exists$;
- intercambiar cuantificadores mixtos;
- dejar una variable libre sin advertirlo;
- interpretar «no todos» como «ninguno»;
- confundir existencia con unicidad.

La sección final reunirá estos errores y los convertirá en una herramienta de diagnóstico.
