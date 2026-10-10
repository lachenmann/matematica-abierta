---
{
  "title": "Fracciones algebraicas y expresiones racionales",
  "description": "Capítulo 20 del Tomo I de Álgebra para matemáticos, con 88 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0195",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C20",
  "editorial-id": "MA-BCH-APM-01-025",
  "status": "published",
  "date-created": "2026-10-09",
  "date-modified": "2026-10-09",
  "areas": [
    "algebra",
    "fundamentos"
  ],
  "level": "fundamental",
  "topics": [
    "numeros-complejos-y-el-horizonte-de-las-ecuaciones"
  ],
  "prerequisites": [
    "MA-BCH-0194"
  ],
  "related": [
    "MA-BOK-0006"
  ],
  "provenance": {
    "type": "original",
    "sources": []
  },
  "license": "GFDL-1.3-or-later"
}
---

En C19 aprendimos a cambiar la forma de una expresión para hacer visible su estructura multiplicativa. Esa habilidad se vuelve decisiva en cuanto aparece una división, porque una transformación que simplifica mucho la fórmula puede ocultar parte de la información con la que empezamos.

Considere, por ejemplo,

$$
\frac{x^2-9}{x-3}.
$$

La factorización de la diferencia de cuadrados nos invita a escribir

$$
x^2-9=(x-3)(x+3).
$$

Parece entonces que basta cancelar el factor $x-3$ y obtener $x+3$. El cálculo es correcto, pero hay una pregunta que debemos responder antes de declarar terminada la transformación:

> **¿para qué valores de $x$ tenía sentido la expresión original?**

Ésta será la pregunta rectora del capítulo. Trabajaremos con expresiones que contienen cocientes, productos, sumas y divisiones anidadas, y aprenderemos a transformarlas sin perder las condiciones bajo las cuales esas transformaciones son válidas.

La idea central puede adelantarse desde ahora:

> **Una fórmula más simple puede conservar todos los valores de la expresión original allí donde ésta estaba definida y, sin embargo, estar definida en puntos nuevos.**

Por eso, en este capítulo una simplificación no estará completa mientras no conservemos también el dominio original.

## 20.1. Una fórmula más simple, un dominio distinto {#apm-c20-s01}

Volvamos a

$$
E(x)=\frac{x^2-9}{x-3}.
$$

Antes de factorizar, leamos el denominador. La división sólo tiene sentido cuando

$$
x-3\neq 0,
$$

es decir, cuando

$$
x\neq 3.
$$

Por tanto, la expresión $E(x)$ está definida para todos los números reales excepto $3$.

Ahora sí factorizamos el numerador:

$$
E(x)
=
\frac{(x-3)(x+3)}{x-3}.
$$

Si $x\neq 3$, entonces $x-3\neq 0$, y podemos dividir numerador y denominador por el factor no nulo $x-3$. Así obtenemos

$$
E(x)=x+3,
\qquad x\neq 3.
$$

La restricción escrita al lado de la fórmula no es un comentario accesorio. Forma parte de la información que debemos conservar.

### ¿Qué significa realmente la simplificación?

Para cualquier $x\neq 3$, ambas fórmulas producen el mismo valor. Por ejemplo,

| $x$ | $\dfrac{x^2-9}{x-3}$ | $x+3$ |
|---:|---:|---:|
| $0$ | $3$ | $3$ |
| $2$ | $5$ | $5$ |
| $4$ | $7$ | $7$ |

Nada extraño ocurre mientras $x$ permanezca en el dominio de la expresión original.

Pero en $x=3$ la situación cambia. La fórmula simplificada da

$$
3+3=6,
$$

mientras que la expresión original exigiría calcular

$$
\frac{3^2-9}{3-3}=\frac{0}{0},
$$

que no está definido.

Así que no podemos escribir sin condiciones

$$
\frac{x^2-9}{x-3}=x+3
$$

como una afirmación válida para todo $x\in\mathbb R$. La afirmación correcta es

$$
\frac{x^2-9}{x-3}=x+3
\qquad\text{para }x\neq 3.
$$

Esta pequeña diferencia será fundamental una y otra vez.

### La cancelación no crea el valor que faltaba

Es tentador pensar que, después de cancelar $x-3$, hemos descubierto que el cociente original “vale $6$” cuando $x=3$. Eso sería incorrecto.

La cancelación se justificó precisamente bajo la condición $x-3\neq 0$. En $x=3$ no existe un factor no nulo por el cual podamos dividir. La expresión $x+3$ nos proporciona una fórmula que coincide con el cociente en todos los puntos permitidos, pero no cambia retroactivamente el significado de la expresión inicial.

Dicho de otra manera: la transformación algebraica conserva valores **dentro del dominio en que está autorizada**. No amplía por sí sola ese dominio.

### Dos datos que deben viajar juntos

A partir de ahora, cuando simplifiquemos una expresión de este tipo, registraremos dos cosas:

1. la fórmula obtenida;
2. las restricciones heredadas de la expresión original.

En nuestro ejemplo, la respuesta completa es

$$
\boxed{E(x)=x+3,\qquad x\neq 3.}
$$

La fórmula $x+3$ es más simple, pero por sí sola contiene menos información sobre el problema del que surgió.

### Un no-ejemplo: una igualdad demasiado amplia

Considere la afirmación

$$
\frac{x^2-9}{x-3}=x+3
\qquad\text{para todo }x\in\mathbb R.
$$

El cálculo de factorización que parece sostenerla es

$$
\frac{(x-3)(x+3)}{x-3}=x+3.
$$

¿Dónde está la falla? No está en la factorización. Tampoco está en el resultado $x+3$. La falla consiste en omitir la hipótesis que autoriza cancelar: $x-3\neq0$.

Éste es un tipo de error especialmente importante, porque la parte visible del álgebra puede ser correcta mientras la afirmación completa es falsa.

### Una lectura funcional que desarrollaremos después

Podemos anticipar una distinción que formalizaremos en [§20.4](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s04). Si consideramos las fórmulas con sus dominios naturales, entonces

$$
f(x)=\frac{x^2-9}{x-3}
$$

tiene dominio $\mathbb R\setminus\{3\}$, mientras que

$$
g(x)=x+3
$$

tiene dominio $\mathbb R$.

Coinciden en todos los puntos del dominio de $f$, pero no son la misma función si cada una conserva su dominio natural. Más adelante precisaremos exactamente cómo expresar esta situación. Por ahora basta con retener la regla operacional: **simplificar una fórmula no autoriza a olvidar dónde estaba definida la expresión original**.

### Recuperación breve

Simplifique

$$
\frac{x^2-4}{x-2}
$$

y conserve toda la información necesaria.

**Respuesta razonada.** La expresión original exige $x-2\neq0$, de modo que $x\neq2$. Como

$$
x^2-4=(x-2)(x+2),
$$

para $x\neq2$ podemos cancelar el factor $x-2$:

$$
\frac{x^2-4}{x-2}=x+2,
\qquad x\neq2.
$$

En $x=2$ la fórmula $x+2$ vale $4$, pero el cociente original no está definido. Por tanto, la respuesta completa es

$$
\boxed{x+2,\qquad x\neq2.}
$$

### Qué debemos conservar de esta sección

La primera regla del cálculo racional no es una técnica de simplificación, sino un hábito de lectura:

> **Antes de transformar una expresión, determine dónde está definida. Después de transformar, conserve esas restricciones aunque hayan desaparecido de la fórmula visible.**

En la sección siguiente distinguiremos con precisión qué llamaremos **expresión fraccionaria** y qué llamaremos **expresión racional**. Esa terminología nos permitirá describir con mayor cuidado los objetos que acabamos de manipular.


## 20.2. Expresiones fraccionarias y expresiones racionales {#apm-c20-s02}

En [§20.1](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s01) trabajamos con

$$
\frac{x^2-9}{x-3}.
$$

La forma de la expresión nos dice inmediatamente que hay una división, pero todavía necesitamos una terminología que distinga dos ideas diferentes: **estar escrito como un cociente** y **ser un cociente de polinomios**.

Esta distinción será útil porque más adelante aparecerán cocientes con radicales, cocientes de otros cocientes y expresiones que, después de varias transformaciones, pueden adquirir una forma mucho más simple que aquella con la que empezaron.

### Expresión fraccionaria: la forma de cociente

Llamaremos **expresión fraccionaria** a una expresión escrita como un cociente

$$
\frac{A}{B},
$$

donde $A$ y $B$ son expresiones algebraicas y el denominador $B$ debe estar definido y ser distinto de cero en cada valor donde pretendamos evaluar el cociente.

Por ejemplo,

$$
\frac{x+1}{x-4},
\qquad
\frac{\sqrt{x}+1}{x+2},
\qquad
\frac{x^2+1}{\sqrt{x}-3}
$$

son expresiones fraccionarias: las tres presentan una división entre dos expresiones algebraicas.

La palabra *fraccionaria* describe aquí una forma de construcción. No afirma todavía que numerador y denominador sean polinomios.

### Expresión racional: un cociente de polinomios

Una **expresión racional** en la variable $x$ es una expresión que puede escribirse en la forma

$$
\frac{P(x)}{Q(x)},
$$

donde $P$ y $Q$ son expresiones polinómicas y $Q$ no es el polinomio cero.

Así,

$$
\frac{x^2-5x+6}{x^2-1}
$$

es racional porque tanto el numerador como el denominador son polinomios. También lo son

$$
\frac{3}{x^2+1}
\qquad\text{y}\qquad
\frac{2x^3-x+7}{5x-4}.
$$

En cambio,

$$
\frac{\sqrt{x}+1}{x-2}
$$

es fraccionaria, pero no es racional en esta forma: el numerador $\sqrt{x}+1$ no es una expresión polinómica.

Análogamente,

$$
\frac{x+1}{\sqrt{x}+2}
$$

es fraccionaria pero no racional, porque el denominador contiene $\sqrt{x}$.

Por tanto,

> **Toda expresión racional escrita como $P/Q$ es una expresión fraccionaria, pero no toda expresión fraccionaria es racional.**

### Los polinomios también están dentro de la clase racional

Puede parecer extraño llamar racional a una expresión que no muestra ninguna fracción. Sin embargo, cualquier polinomio $P(x)$ puede escribirse como

$$
P(x)=\frac{P(x)}{1}.
$$

Como $1$ es un polinomio que nunca se anula, toda expresión polinómica puede considerarse también una expresión racional.

Por ejemplo,

$$
x^2-3x+5
$$

es polinómica y, al mismo tiempo, racional porque

$$
x^2-3x+5=\frac{x^2-3x+5}{1}.
$$

Esto no significa que debamos reescribir todos los polinomios como fracciones. La inclusión es conceptual: la clase de las expresiones racionales contiene a las polinómicas.

### «Racional» no describe los valores numéricos que produce

Aquí conviene detener una posible confusión. El adjetivo **racional** no significa que la expresión sólo pueda tomar valores que sean números racionales.

Considere

$$
R(x)=x+1.
$$

Como acabamos de ver, $R$ es una expresión racional. Pero si evaluamos en $x=\sqrt{2}$, obtenemos

$$
R(\sqrt{2})=\sqrt{2}+1,
$$

que no es un número racional.

La palabra *racional* describe la **estructura algebraica de la expresión** —cociente de polinomios—, no la naturaleza aritmética de todos sus valores.

### Clasificar antes de operar

Compare ahora las expresiones siguientes:

| Expresión | ¿Fraccionaria? | ¿Racional? | Razón |
|---|:---:|:---:|---|
| $\dfrac{x^2+1}{x-3}$ | sí | sí | numerador y denominador son polinomios |
| $\dfrac{\sqrt{x}+1}{x-3}$ | sí | no | aparece un radical en el numerador |
| $x^3-2x+1$ | no está escrita como cociente | sí | puede escribirse como $\dfrac{x^3-2x+1}{1}$ |
| $\dfrac{x+1}{\sqrt{x}+3}$ | sí | no | aparece un radical en el denominador |

La clasificación evita una costumbre peligrosa: llamar «racional» a cualquier expresión que visualmente tenga una barra de fracción. La barra sólo indica división; para hablar de expresión racional debemos mirar qué tipo de expresiones ocupan numerador y denominador.

### Una fórmula puede cambiar de aspecto sin perder su procedencia

Considere de nuevo

$$
\frac{x^2-9}{x-3}.
$$

Es una expresión racional porque es cociente de dos polinomios. Para $x\neq3$ se simplifica a

$$
x+3,
$$

que es una expresión polinómica y, por tanto, también racional.

Aquí aparecen dos hechos distintos:

1. la **clase algebraica** se conserva: ambas fórmulas son racionales;
2. el **dominio original** no se recupera mirando sólo la fórmula final.

La clasificación de una expresión y el estudio de su dominio están relacionados, pero no son la misma tarea. En [§20.3](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s03) aprenderemos a leer sistemáticamente las restricciones de una expresión antes de realizar ninguna operación.

### Una precaución con las formas equivalentes

A veces una expresión que no está presentada inicialmente como un cociente simple de polinomios puede transformarse, bajo ciertas restricciones, en una expresión racional. Por ejemplo, una fracción compleja puede contener dentro de sí otras expresiones racionales y terminar reduciéndose a un solo cociente de polinomios.

No utilizaremos esta posibilidad para borrar su historia algebraica. Cuando una transformación cambie la forma visible, seguiremos registrando las condiciones necesarias para que cada paso sea válido.

Ésta es la misma disciplina que apareció en [§20.1](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s01): **la forma final no sustituye al dominio de procedencia**.

### No-ejemplo: una clasificación por apariencia

Supongamos que alguien afirma:

> «$\dfrac{\sqrt{x}+1}{x-2}$ es racional porque es una fracción de dos expresiones algebraicas.»

La segunda parte de la frase sólo permite concluir que es una expresión fraccionaria. Para que sea racional, numerador y denominador deben ser polinomios. Como $\sqrt{x}+1$ no es polinómico, la conclusión no se sigue.

El error no está en una manipulación, sino en haber usado una definición demasiado amplia.

### Recuperación breve

Clasifique cada expresión como polinómica, racional y/o fraccionaria. Cuando una expresión pertenezca a más de una clase, indíquelo.

1. $\displaystyle \frac{2x-1}{x^2+4}$;
2. $\displaystyle \frac{x+3}{\sqrt{x}+1}$;
3. $x^4-5x^2+2$;
4. $\displaystyle \frac{\sqrt{x^2+1}}{x-1}$.

**Respuesta razonada.**

1. $\dfrac{2x-1}{x^2+4}$ es fraccionaria y racional, porque numerador y denominador son polinomios.
2. $\dfrac{x+3}{\sqrt{x}+1}$ es fraccionaria, pero no racional en esta forma, porque el denominador no es polinómico.
3. $x^4-5x^2+2$ es polinómica y también racional, pues puede escribirse como $\dfrac{x^4-5x^2+2}{1}$. No está presentada en forma fraccionaria visible.
4. $\dfrac{\sqrt{x^2+1}}{x-1}$ es fraccionaria, pero no racional en esta forma, porque el numerador contiene un radical.

### Qué debemos conservar de esta sección

La terminología puede resumirse así:

$$
\text{polinómica}
\subset
\text{racional},
$$

mientras que **fraccionaria** describe la presencia de un cociente visible y puede abarcar expresiones racionales y no racionales.

La pregunta siguiente ya no será «¿qué tipo de expresión es?», sino otra más operativa:

> **¿Para qué valores de la variable está realmente definida?**

Responderla de manera sistemática es el objetivo de [§20.3](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s03).

## 20.3. Leer el dominio antes de operar {#apm-c20-s03}

En [§20.1](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s01) vimos que una simplificación puede ocultar una exclusión. En [§20.2](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s02) distinguimos la clase algebraica de una expresión de las condiciones bajo las cuales está definida. Ahora convertiremos esas observaciones en un procedimiento sistemático.

La pregunta que debe preceder a cualquier transformación es:

> **¿Qué tiene que ser cierto para que cada parte de la expresión esté definida?**

Cuando trabajamos sobre los números reales, una expresión racional simple $P(x)/Q(x)$ está definida exactamente en los valores para los cuales $Q(x)\neq0$. Pero las expresiones que aparecerán en este capítulo pueden contener varios cocientes, unos dentro de otros. En ese caso no existe un único denominador visible que podamos mirar al final: debemos leer la expresión por niveles.

### El dominio se construye, no se adivina

Considere primero

$$
R(x)=\frac{x+5}{(x-2)(x+4)^2}.
$$

El numerador no impone ninguna restricción. El denominador, en cambio, debe ser distinto de cero. Como

$$
(x-2)(x+4)^2\neq0
$$

si y sólo si ninguno de sus factores es cero, debemos exigir

$$
x\neq2
\qquad\text{y}\qquad
x\neq-4.
$$

Por tanto,

$$
\operatorname{Dom}(R)=\mathbb R\setminus\{-4,2\}.
$$

Observe que la potencia no crea una exclusión nueva: $(x+4)^2$ y $x+4$ se anulan en el mismo punto. Lo que importa para el dominio no es cuántas veces aparece un factor, sino en qué valores puede hacer cero un denominador.

### A veces conviene factorizar sólo para leer el dominio

Ahora mire

$$
S(x)=\frac{2x-1}{x^2-x-6}.
$$

El denominador no muestra de inmediato sus ceros, pero C19 nos permite factorizarlo:

$$
x^2-x-6=(x-3)(x+2).
$$

Así, la condición de definición es

$$
(x-3)(x+2)\neq0,
$$

y por tanto

$$
x\neq3,
\qquad
x\neq-2.
$$

De modo que

$$
\operatorname{Dom}(S)=\mathbb R\setminus\{-2,3\}.
$$

Aquí la factorización no se utilizó para simplificar la expresión. Se utilizó para **hacer visibles las restricciones**. Esta diferencia de propósito será importante: antes de modificar una fórmula debemos saber primero dónde tenía sentido.

### Las restricciones de las subexpresiones se acumulan

Considere ahora una expresión con más de un nivel de división:

$$
T(x)=
\frac{\dfrac{1}{x-1}}
     {\dfrac{x+2}{x-3}}.
$$

No operemos todavía. Limitémonos a leer qué condiciones exige la escritura tal como está.

Primero, la subexpresión del numerador

$$
\frac{1}{x-1}
$$

requiere

$$
x\neq1.
$$

Segundo, la subexpresión que aparece en el denominador exterior,

$$
\frac{x+2}{x-3},
$$

debe estar definida. Por ello,

$$
x\neq3.
$$

Pero todavía falta una condición. Ese cociente completo ocupa el **denominador de la fracción exterior**, de modo que no basta con que exista: también debe ser distinto de cero. Bajo la condición $x\neq3$, tenemos

$$
\frac{x+2}{x-3}=0
$$

exactamente cuando $x+2=0$. Por tanto debemos excluir también

$$
x=-2.
$$

Reuniendo las tres condiciones,

$$
\boxed{
\operatorname{Dom}(T)
=
\mathbb R\setminus\{-2,1,3\}.
}
$$

No hemos invertido ninguna fracción ni simplificado la expresión. Sólo hemos leído todas las obligaciones de definición que ya estaban presentes.

### Dominio por capas

El ejemplo anterior sugiere un procedimiento que utilizaremos durante todo el capítulo.

1. **Identifique las subexpresiones.** En particular, localice cada división, no sólo la barra de fracción más grande.
2. **Exija que cada subexpresión esté definida.** Todo denominador interno debe ser distinto de cero.
3. **Mire los denominadores exteriores.** Una expresión que funciona como divisor debe, además de estar definida, ser no nula.
4. **Reúna las restricciones.** El dominio final es la intersección de todas las condiciones obtenidas.
5. **Sólo después opere.** Factorizar, cancelar, multiplicar o invertir viene después de fijar el dominio original.

Podemos condensar el método así:

```text
LEER LA EXPRESIÓN
       ↓
LOCALIZAR SUBEXPRESIONES
       ↓
REGISTRAR CONDICIONES DE DEFINICIÓN
       ↓
EXIGIR DENOMINADORES NO NULOS
       ↓
INTERSECTAR LAS RESTRICCIONES
       ↓
OPERAR
```

La palabra **intersectar** recuerda una idea ya conocida de C7–C9: para que la expresión completa tenga sentido, todas las condiciones deben cumplirse simultáneamente.

### Un denominador puede ser una expresión completa

La dificultad de $T(x)$ no provenía de un cálculo complicado, sino de una lectura incompleta. Es fácil mirar sólo $x-1$ y $x-3$, porque ambos aparecen escritos como denominadores pequeños. Sin embargo, el verdadero denominador exterior es

$$
\frac{x+2}{x-3}.
$$

Ese objeto entero debe ser no nulo. Por eso $x=-2$ queda excluido aunque $-2$ no haga cero ninguno de los dos denominadores internos visibles.

Ésta es una regla general:

> **Si una expresión completa ocupa el lugar de un divisor, debemos comprobar dos cosas: que esté definida y que su valor no sea cero.**

Más adelante, en [§20.8](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s08), esta distinción controlará la división de expresiones racionales. Aquí sólo nos interesa reconocerla antes de operar.

### No-ejemplo: mirar únicamente los denominadores internos

Supongamos que, para

$$
T(x)=
\frac{\dfrac{1}{x-1}}
     {\dfrac{x+2}{x-3}},
$$

alguien declara

$$
\operatorname{Dom}(T)=\mathbb R\setminus\{1,3\}.
$$

Las dos exclusiones registradas son correctas, pero la respuesta está incompleta. Si $x=-2$, la subexpresión

$$
\frac{x+2}{x-3}
$$

está definida y vale $0$. Entonces la expresión exterior intentaría dividir por cero. El primer punto omitido no es un error de cálculo: es no haber reconocido que el denominador exterior era una subexpresión completa que también debía ser no nula.

Este diagnóstico será recurrente en el capítulo. Una lista de restricciones puede contener condiciones correctas y, aun así, no ser todavía el dominio.

### Restricciones heredadas y restricciones nuevas

Durante una transformación posterior puede aparecer una fórmula con menos denominadores visibles. Eso no elimina las condiciones que acabamos de registrar. El dominio que calculamos **antes de operar** es parte de los datos iniciales del problema y debe viajar con la expresión.

También puede ocurrir lo contrario: una ruta de cálculo puede introducir temporalmente un denominador auxiliar. En ese caso habrá que comprobar si esa elección impone una restricción nueva. Trataremos esa situación cuando estudiemos denominadores comunes y fracciones complejas. Por ahora basta con distinguir dos fuentes de condiciones:

- **restricciones heredadas**, que ya pertenecen a la expresión original;
- **restricciones introducidas por una transformación**, que sólo son legítimas si se controlan explícitamente.

Nuestro objetivo será siempre preservar las primeras y no añadir las segundas de manera inadvertida.

### Recuperación breve

Determine el dominio de cada expresión **sin simplificarla**.

1. $\displaystyle A(x)=\frac{x-1}{(x+5)(x-2)^2}$;
2. $\displaystyle B(x)=\frac{3x+1}{x^2+x-6}$;
3. $\displaystyle C(x)=\frac{\dfrac{1}{x+2}}{\dfrac{x-3}{x+1}}$.

**Respuesta razonada.**

1. En $A(x)$ el denominador es $(x+5)(x-2)^2$. Se anula en $x=-5$ y $x=2$. Por tanto,

$$
\operatorname{Dom}(A)=\mathbb R\setminus\{-5,2\}.
$$

2. Para $B(x)$ factorizamos sólo para localizar los ceros del denominador:

$$
x^2+x-6=(x+3)(x-2).
$$

Así,

$$
\operatorname{Dom}(B)=\mathbb R\setminus\{-3,2\}.
$$

3. En $C(x)$ aparecen tres obligaciones. La fracción $1/(x+2)$ exige $x\neq-2$. La fracción $(x-3)/(x+1)$ exige $x\neq-1$. Finalmente, como esta última fracción es el denominador exterior, también debe ser no nula; bajo $x\neq-1$ se anula en $x=3$. Por tanto,

$$
\boxed{
\operatorname{Dom}(C)=\mathbb R\setminus\{-2,-1,3\}.
}
$$

### Qué debemos conservar de esta sección

El dominio de una expresión compuesta se obtiene imponiendo **simultáneamente** las condiciones de definición de todas sus partes. No basta con buscar símbolos que parezcan denominadores: una subexpresión completa puede funcionar como divisor y, en ese caso, debe existir y ser distinta de cero.

La regla de trabajo queda fijada:

> **primero dominio; después álgebra.**

En [§20.4](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s04) usaremos este control para formular con precisión qué significa que dos expresiones sean equivalentes sobre un dominio declarado y por qué una fórmula simplificada puede tener un dominio natural mayor que la expresión de la que provino.



## 20.4. Equivalencia sobre un dominio declarado {#apm-c20-s04}

En [§20.1](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s01) apareció una situación que ahora podemos formular con precisión. Las expresiones

$$
\frac{x^2-9}{x-3}
\qquad\text{y}\qquad
x+3
$$

producen el mismo valor para todo $x\neq3$, pero no tienen el mismo dominio natural. La primera no está definida en $x=3$; la segunda sí.

Por tanto, antes de escribir que dos expresiones son «iguales», conviene responder una pregunta:

> **¿sobre qué dominio estamos haciendo la comparación?**

### Equivalencia de expresiones sobre un dominio

Sean $E(x)$ y $F(x)$ dos expresiones y sea $D$ un conjunto de valores en el que ambas están definidas. Diremos que **$E$ y $F$ son equivalentes sobre $D$** si

$$
E(x)=F(x)
\qquad\text{para todo }x\in D.
$$

El dominio $D$ no es una decoración de la afirmación. Forma parte de ella.

En el ejemplo inicial,

$$
E(x)=\frac{x^2-9}{x-3},
\qquad
F(x)=x+3,
$$

podemos declarar

$$
E(x)=F(x)
\qquad\text{para todo }x\in\mathbb R\setminus\{3\}.
$$

Así, las dos expresiones son equivalentes sobre $\mathbb R\setminus\{3\}$.

No estamos afirmando que la primera expresión adquiera un valor en $x=3$. Estamos diciendo que, en el dominio donde ambas pueden compararse y donde la cancelación está autorizada, producen exactamente los mismos valores.

### El mismo cálculo puede describir funciones distintas

Recordemos la convención de C9. Si

$$
f,g:A\to B,
$$

entonces $f=g$ cuando

$$
f(a)=g(a)
\qquad\text{para todo }a\in A.
$$

Si cambian el dominio o el codominio, tratamos editorialmente las funciones como objetos distintos, aunque utilicen la misma regla simbólica.

Apliquemos esto al ejemplo. Defina

$$
f:\mathbb R\setminus\{3\}\to\mathbb R,
\qquad
f(x)=\frac{x^2-9}{x-3},
$$

y

$$
g:\mathbb R\to\mathbb R,
\qquad
g(x)=x+3.
$$

Aunque

$$
f(x)=g(x)
\qquad\text{para todo }x\neq3,
$$

las funciones $f$ y $g$ no son iguales, porque tienen dominios distintos.

En cambio, si restringimos $g$ al dominio de $f$ y definimos

$$
g_{\!*}:\mathbb R\setminus\{3\}\to\mathbb R,
\qquad
g_{\!*}(x)=x+3,
$$

entonces

$$
f=g_{\!*}.
$$

Aquí sí coinciden todos los datos que estamos usando para comparar funciones: mismo dominio, mismo codominio y mismos valores en cada punto.

### Una identidad algebraica puede necesitar un dominio de lectura

Considere ahora

$$
A(x)=\frac{x^2-4}{x^2-x-2}.
$$

Factorizando,

$$
x^2-4=(x-2)(x+2)
$$

y

$$
x^2-x-2=(x-2)(x+1).
$$

El dominio natural de $A$ es

$$
\mathbb R\setminus\{-1,2\}.
$$

En ese dominio, como $x-2\neq0$, podemos cancelar:

$$
A(x)=\frac{x+2}{x+1},
\qquad
x\neq-1,2.
$$

La fórmula

$$
B(x)=\frac{x+2}{x+1}
$$

tiene, en cambio, dominio natural

$$
\mathbb R\setminus\{-1\}.
$$

Por tanto,

$$
A(x)=B(x)
\qquad\text{para todo }x\in\mathbb R\setminus\{-1,2\},
$$

pero las funciones naturales asociadas a $A$ y $B$ no son iguales si cada una conserva su propio dominio.

El punto $x=2$ resume toda la diferencia: $B(2)=4/3$, mientras que $A(2)$ no está definido.

### Fórmula final y dominio de procedencia

Cuando una transformación elimina un factor del denominador, pueden quedar dos dominios en juego:

1. el **dominio original**, fijado antes de transformar;
2. el **dominio natural de la fórmula final**, que puede ser mayor.

Para conservar la equivalencia de la transformación, la fórmula final debe leerse sobre el dominio original, salvo que se declare expresamente otra función u otro objeto.

Por ejemplo,

$$
\frac{x^2-4}{x^2-x-2}
=
\frac{x+2}{x+1},
\qquad
x\neq-1,2,
$$

es una afirmación correcta y completa.

En cambio, escribir solamente

$$
\frac{x^2-4}{x^2-x-2}
=
\frac{x+2}{x+1}
$$

sin indicar el dominio puede ocultar que la expresión de la derecha está definida en un punto adicional.

### No toda coincidencia parcial es una equivalencia útil

Supongamos que dos expresiones coinciden en algunos valores aislados. Eso no basta para afirmar que son equivalentes sobre un dominio.

Por ejemplo,

$$
x^2=x
$$

es verdad cuando $x=0$ y cuando $x=1$, pero no para todo $x\in\mathbb R$.

Si declaramos

$$
D=\{0,1\},
$$

entonces sí podemos decir que $x^2$ y $x$ son equivalentes sobre $D$. Si el dominio declarado fuera $\mathbb R$, la afirmación sería falsa.

Esto muestra por qué el dominio debe aparecer en la proposición completa:

$$
\text{fórmula}
+
\text{dominio}
=
\text{afirmación verificable}.
$$

### Igualdad en el dominio común

A veces dos expresiones poseen dominios naturales diferentes, pero existe un dominio común sobre el cual ambas están definidas. En ese caso podemos comparar sus valores allí.

Si $D_E$ y $D_F$ son los dominios naturales de $E$ y $F$, respectivamente, una comparación válida requiere al menos

$$
D\subseteq D_E\cap D_F.
$$

Sobre un conjunto así podemos preguntar si

$$
E(x)=F(x)
\qquad\text{para todo }x\in D.
$$

En el cálculo racional de este capítulo, el dominio declarado será normalmente el dominio de la expresión original. Esa elección preserva exactamente las condiciones bajo las cuales se justificó la transformación.

### No-ejemplo: «misma fórmula simplificada, misma función»

Considere nuevamente

$$
f:\mathbb R\setminus\{3\}\to\mathbb R,
\qquad
f(x)=\frac{x^2-9}{x-3},
$$

y

$$
g:\mathbb R\to\mathbb R,
\qquad
g(x)=x+3.
$$

La afirmación

> «Como al simplificar obtenemos $x+3$, entonces $f=g$»

es incorrecta.

La simplificación demuestra que ambos valores coinciden para todo $x$ del dominio de $f$. No demuestra que los dominios sean iguales. El primer dato que falla en la comparación de funciones es precisamente ése.

### Recuperación breve

Considere

$$
E(x)=\frac{x^2-1}{x-1}
$$

y

$$
F(x)=x+1.
$$

Responda:

1. ¿Cuál es el dominio natural de cada expresión?
2. ¿Son equivalentes sobre $\mathbb R\setminus\{1\}$?
3. Si cada fórmula define una función con su dominio natural y codominio $\mathbb R$, ¿son iguales esas funciones?
4. ¿Qué ocurre si restringimos $F$ a $\mathbb R\setminus\{1\}$?

**Respuesta razonada.**

La expresión $E$ exige $x\neq1$, mientras que $F$ está definida para todo real. Por tanto,

$$
\operatorname{Dom}(E)=\mathbb R\setminus\{1\},
\qquad
\operatorname{Dom}(F)=\mathbb R.
$$

Como

$$
x^2-1=(x-1)(x+1),
$$

para $x\neq1$ tenemos

$$
E(x)=x+1=F(x).
$$

Así, $E$ y $F$ son equivalentes sobre $\mathbb R\setminus\{1\}$.

Sin embargo, las funciones con sus dominios naturales no son iguales porque sus dominios difieren. Si restringimos $F$ a $\mathbb R\setminus\{1\}$ y mantenemos codominio $\mathbb R$, entonces ambas funciones tienen el mismo dominio, el mismo codominio y los mismos valores; en ese caso sí son iguales.

### Qué debemos conservar de esta sección

Una transformación algebraica no debe leerse separada de su dominio. La afirmación

$$
E(x)=F(x)
$$

sólo es completa cuando sabemos dónde se pretende que sea válida.

Para este capítulo fijamos la regla:

> **Dos expresiones pueden ser equivalentes sobre un dominio declarado aunque sus fórmulas naturales definan funciones distintas. Una simplificación preserva valores en el dominio autorizado; no borra ni amplía automáticamente el dominio de procedencia.**

En [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05) utilizaremos esta precisión para justificar formalmente la cancelación de factores y señalar exactamente qué hipótesis permite efectuarla.

## 20.5. Cancelar factores: demostración y condiciones {#apm-c20-s05}

Hasta ahora hemos usado la cancelación varias veces, pero siempre bajo una condición explícita. Conviene detenernos y justificarla con precisión, porque «cancelar» no es una operación primitiva ni significa tachar símbolos iguales. Es una consecuencia de poder dividir por una cantidad que sabemos que no es cero.

La pregunta central es:

> **¿Qué estamos haciendo realmente cuando cancelamos un factor?**

### La regla general

Considere una expresión de la forma

$$
\frac{A C}{B C}.
$$

Para que el cociente original esté definido debemos tener $BC\neq0$. En los números reales, un producto es distinto de cero exactamente cuando cada factor lo es, de modo que necesitamos

$$
B\neq0
\qquad\text{y}\qquad
C\neq0.
$$

Bajo estas condiciones, $C$ posee inverso multiplicativo. Podemos escribir

$$
\frac{AC}{BC}
=
AC\,(BC)^{-1}.
$$

Como $B\neq0$ y $C\neq0$,

$$
(BC)^{-1}=B^{-1}C^{-1},
$$

y por tanto

$$
AC\,(BC)^{-1}
=
ACB^{-1}C^{-1}
=
AB^{-1}(CC^{-1})
=
AB^{-1}
=
\frac{A}{B}.
$$

Así obtenemos la regla

$$
\boxed{
\frac{AC}{BC}=\frac{A}{B}
\qquad\text{si }B\neq0\text{ y }C\neq0.
}
$$

La condición $C\neq0$ es la que autoriza eliminar el factor común. La condición $B\neq0$ garantiza que tanto el cociente original como la expresión final estén definidos.

### Cancelar es dividir por un factor común no nulo

La misma idea puede verse de manera más directa. Si $C\neq0$, podemos dividir numerador y denominador por $C$:

$$
\frac{AC}{BC}
=
\frac{AC/C}{BC/C}
=
\frac{A}{B}.
$$

Pero esta escritura sólo tiene sentido porque $C$ no es cero. Por eso una cancelación nunca debe leerse como un gesto puramente tipográfico.

En particular, la cadena mental correcta es

```text
FACTOR COMÚN
      ↓
COMPROBAR QUE NO SEA CERO
      ↓
DIVIDIR NUMERADOR Y DENOMINADOR POR ÉL
      ↓
CONSERVAR LAS RESTRICCIONES ORIGINALES
```

### Ejemplo: un factor que desaparece, una exclusión que permanece

Considere

$$
R(x)=\frac{x^2-4}{x^2+x-6}.
$$

Antes de cancelar, determinamos el dominio. Factorizamos:

$$
x^2-4=(x-2)(x+2)
$$

y

$$
x^2+x-6=(x-2)(x+3).
$$

La expresión original exige

$$
x\neq2
\qquad\text{y}\qquad
x\neq-3.
$$

En ese dominio,

$$
R(x)
=
\frac{(x-2)(x+2)}{(x-2)(x+3)}.
$$

Como $x\neq2$, el factor $x-2$ es no nulo y puede cancelarse:

$$
R(x)=\frac{x+2}{x+3},
\qquad
x\neq2,-3.
$$

La fórmula final ya no contiene $x-2$, pero la exclusión $x=2$ no desaparece. La cancelación eliminó un factor de la **escritura**, no una condición del dominio original.

### Sólo se cancelan factores

La regla anterior tiene una consecuencia decisiva: para cancelar, aquello que aparece arriba y abajo debe ser un **factor** de todo el numerador y de todo el denominador.

Considere

$$
\frac{x+3}{x+5}.
$$

Aquí $x$ aparece en numerador y denominador, pero no es factor de ninguno de los dos. No podemos «cancelar la $x$» y escribir $3/5$.

Podemos detectar inmediatamente el error con $x=1$:

$$
\frac{1+3}{1+5}=\frac{4}{6}=\frac23,
$$

mientras que

$$
\frac35\neq\frac23.
$$

El problema estructural es más importante que el contraejemplo numérico: en $x+3$ y $x+5$, la variable forma parte de una **suma**. La cancelación actúa sobre productos.

### Factorizar puede convertir términos en factores

Considere ahora

$$
\frac{x^2+3x}{x^2+5x}.
$$

Aquí tampoco debemos cancelar términos directamente. Primero reconocemos la estructura multiplicativa:

$$
x^2+3x=x(x+3),
$$

$$
x^2+5x=x(x+5).
$$

El dominio original exige

$$
x(x+5)\neq0,
$$

es decir,

$$
x\neq0,
\qquad
x\neq-5.
$$

Sólo entonces escribimos

$$
\frac{x(x+3)}{x(x+5)}
=
\frac{x+3}{x+5},
\qquad
x\neq0,-5.
$$

La variable $x$ pudo cancelarse **después de convertirse en factor común de los dos miembros del cociente**.

Ésta será una pauta recurrente:

> **Si parece haber algo «igual arriba y abajo», pregunte primero si es realmente un factor de todo el numerador y de todo el denominador.**

### Por qué no se cancelan términos de una suma

Supongamos que alguien intenta pasar de

$$
\frac{A+C}{B+C}
$$

a

$$
\frac{A}{B}
$$

«cancelando $C$».

No existe una propiedad algebraica que justifique ese paso en general. Para obtener $A/B$ cancelando $C$, los bloques originales tendrían que ser $CA$ y $CB$, no $A+C$ y $B+C$.

Si $C\ne0$, sí podemos factorizar numéricamente $C$ mediante

$$
A+C=C(A/C+1),\qquad B+C=C(B/C+1).
$$

Pero esa cancelación deja $(A/C+1)/(B/C+1)$, no $A/B$, y conserva la condición $B+C\ne0$. Por tanto, extraer un factor no equivale a borrar un sumando.

La suma no distribuye sobre la división de esa manera. Por tanto, la regla

$$
\frac{A+C}{B+C}=\frac{A}{B}
$$

es falsa en general.

### El cero en el numerador no borra restricciones

Considere

$$
Z(x)=\frac{0}{x-1}.
$$

Para todo $x\neq1$,

$$
Z(x)=0.
$$

Sin embargo, en $x=1$ aparece $0/0$, que no está definido. Por tanto,

$$
\frac{0}{x-1}=0,
\qquad
x\neq1,
$$

pero no como identidad válida para todo real.

Este ejemplo muestra otra vez que una fórmula final muy simple puede ocultar información de dominio. «El numerador es cero» no autoriza a ignorar el denominador.

### No-ejemplo: una cancelación que divide por cero

Considere

$$
\frac{x(x+1)}{x(x-2)}.
$$

Si escribimos

$$
\frac{x(x+1)}{x(x-2)}=\frac{x+1}{x-2}
$$

sin registrar condiciones, hemos omitido parte de la afirmación.

La expresión original exige

$$
x\neq0,
\qquad
x\neq2.
$$

La cancelación del factor $x$ sólo está autorizada porque estamos trabajando bajo $x\neq0$. Por tanto, la forma correcta es

$$
\frac{x(x+1)}{x(x-2)}
=
\frac{x+1}{x-2},
\qquad
x\neq0,2.
$$

En $x=0$ la fórmula de la derecha sí está definida y vale $-1/2$, pero la expresión original no existe. La cancelación no puede utilizarse para fabricar un valor allí donde hubo división por cero.

### Recuperación breve

Simplifique cuando sea posible y justifique cada cancelación. Conserve siempre el dominio original.

1. $\displaystyle \frac{(x-4)(x+1)}{(x-4)(x+3)}$;
2. $\displaystyle \frac{x^2+2x}{x^2-3x}$;
3. $\displaystyle \frac{x+2}{x+5}$, frente a la propuesta de «cancelar $x$».

**Respuesta razonada.**

1. El denominador exige $x\neq4$ y $x\neq-3$. Bajo $x\neq4$, el factor $x-4$ es no nulo y puede cancelarse:

$$
\frac{(x-4)(x+1)}{(x-4)(x+3)}
=
\frac{x+1}{x+3},
\qquad
x\neq4,-3.
$$

2. Primero factorizamos:

$$
x^2+2x=x(x+2),
\qquad
x^2-3x=x(x-3).
$$

El dominio original exige $x\neq0$ y $x\neq3$. Como $x\neq0$, podemos cancelar el factor $x$:

$$
\frac{x^2+2x}{x^2-3x}
=
\frac{x+2}{x-3},
\qquad
x\neq0,3.
$$

3. No existe cancelación posible. En $x+2$ y $x+5$, la $x$ no es un factor común sino parte de dos sumas. La expresión permanece

$$
\frac{x+2}{x+5},
\qquad
x\neq-5.
$$

### Qué debemos conservar de esta sección

La cancelación es una división por un factor común no nulo. Por eso exige tres controles simultáneos:

1. reconocer un **factor** común, no simplemente símbolos o términos parecidos;
2. comprobar que ese factor no sea cero en el dominio declarado;
3. conservar todas las restricciones de la expresión original después de simplificar.

La regla conceptual puede resumirse así:

> **No se cancelan símbolos: se dividen numerador y denominador por un factor común que sabemos no nulo.**

En [§20.6](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s06) recuperaremos las técnicas de factorización de C19 para hacer visibles esos factores y normalizar factores opuestos antes de simplificar.

## 20.6. Factorizar para simplificar y normalizar factores opuestos {#apm-c20-s06}

En [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05) justificamos la cancelación cuando un factor común ya era visible. En la práctica, sin embargo, muchas expresiones racionales llegan en una forma que oculta precisamente los factores que necesitamos ver. Ahí vuelve a entrar C19: no para abrir una teoría nueva de factorización, sino para escoger una representación que haga posible una simplificación legítima.

La pregunta de esta sección es:

> **¿Qué transformación conviene hacer antes de cancelar para que la estructura multiplicativa quede visible?**

La respuesta tendrá dos componentes: **factorizar** y, cuando sea necesario, **normalizar factores que sólo difieren por un signo**.

### Factorizar antes de cancelar

Considere

$$
R(x)=\frac{x^2-9x+20}{x^2-16}.
$$

Antes de transformar nada, leemos el dominio original. Como

$$
x^2-16=(x-4)(x+4),
$$

la expresión exige

$$
x\neq4,
\qquad
x\neq-4.
$$

Ahora factorizamos también el numerador:

$$
x^2-9x+20=(x-4)(x-5).
$$

Así,

$$
R(x)
=
\frac{(x-4)(x-5)}{(x-4)(x+4)}.
$$

Como el dominio original ya impone $x\neq4$, el factor $x-4$ es no nulo y podemos cancelarlo. Obtenemos

$$
\boxed{
R(x)=\frac{x-5}{x+4},
\qquad
x\neq-4,4.
}
$$

La factorización no fue un paso ornamental. Cambió la representación de manera que una estructura cancelable se volvió visible.

### La forma expandida puede ocultar lo importante

Si hubiéramos permanecido en

$$
\frac{x^2-9x+20}{x^2-16},
$$

no habría ningún símbolo que pudiera cancelarse directamente. La posibilidad de simplificar aparece sólo después de reconocer que numerador y denominador comparten un **factor**, no un término.

Por eso la secuencia correcta es

```text
DOMINIO ORIGINAL
      ↓
FACTORIZAR
      ↓
COMPARAR FACTORES
      ↓
CANCELAR SÓLO FACTORES NO NULOS
      ↓
CONSERVAR LAS RESTRICCIONES
```

Esta secuencia evita dos errores opuestos: intentar cancelar dentro de sumas y expandir una expresión que ya estaba mostrando la estructura útil.

### Factores repetidos: cancelar sólo lo que corresponde

Considere

$$
S(x)=\frac{x^2-6x+9}{x^2-2x-3}.
$$

Factorizando,

$$
x^2-6x+9=(x-3)^2
$$

y

$$
x^2-2x-3=(x-3)(x+1).
$$

El dominio original exige

$$
x\neq3,
\qquad
x\neq-1.
$$

Entonces

$$
S(x)
=
\frac{(x-3)^2}{(x-3)(x+1)}.
$$

Como $x\neq3$, podemos cancelar **una copia** del factor $x-3$:

$$
\boxed{
S(x)=\frac{x-3}{x+1},
\qquad
x\neq-1,3.
}
$$

El factor no desaparece por completo del numerador porque allí aparecía con multiplicidad dos. Cancelar un factor común reduce una copia en numerador y denominador; no borra todas sus apariciones.

### Factores opuestos

A veces dos factores no son literalmente iguales, pero sí difieren por un factor $-1$. C19 nos dio la identidad

$$
a-b=-(b-a).
$$

En particular,

$$
3-x=-(x-3).
$$

Esta observación permite reconocer factores que, a primera vista, parecen distintos.

Considere

$$
T(x)=\frac{(3-x)(x+5)}{(x-3)(x-2)}.
$$

El dominio original exige

$$
x\neq3,
\qquad
x\neq2.
$$

Como

$$
3-x=-(x-3),
$$

podemos escribir

$$
T(x)
=
\frac{-(x-3)(x+5)}{(x-3)(x-2)}.
$$

Ahora el factor común $x-3$ es visible. Bajo $x\neq3$ podemos cancelarlo:

$$
\boxed{
T(x)=-\frac{x+5}{x-2},
\qquad
x\neq2,3.
}
$$

El signo negativo no es una complicación secundaria: es exactamente la información que distingue a $3-x$ de $x-3$.

### Normalizar orientación de factores

Cuando aparecen factores como

$$
x-a
\qquad\text{y}\qquad
a-x,
$$

conviene escoger una orientación común antes de cancelar. Cada inversión del orden introduce un factor $-1$:

$$
a-x=-(x-a).
$$

Por ejemplo,

$$
\frac{5-x}{x-5}=-1,
\qquad x\neq5,
$$

porque

$$
5-x=-(x-5).
$$

Si aparecen dos factores opuestos, aparecen dos signos negativos y su producto es positivo. Por ejemplo,

$$
\frac{(2-x)(5-x)}{(x-2)(x-5)}=1,
\qquad x\neq2,5.
$$

En efecto,

$$
2-x=-(x-2)
\qquad\text{y}\qquad
5-x=-(x-5),
$$

de modo que los dos factores $-1$ se multiplican y producen $1$.

### Normalizar signos no es hacer análisis de signos

En esta sección sólo usamos identidades algebraicas como

$$
a-x=-(x-a)
$$

para poner factores en una forma comparable. No estamos preguntando cuándo un factor es positivo o negativo, ni dividiendo la recta real en intervalos, ni construyendo tablas de signos. Esas técnicas pertenecen al estudio de inequaciones de C22.

Aquí el signo se manipula **algebraicamente y de manera global**.

### Un error típico: tratar factores opuestos como si fueran iguales

Supongamos que alguien escribe

$$
\frac{3-x}{x-3}=1.
$$

La cancelación es incorrecta porque $3-x$ y $x-3$ no son el mismo factor. Su relación es

$$
3-x=-(x-3).
$$

Por tanto,

$$
\frac{3-x}{x-3}
=
\frac{-(x-3)}{x-3}
=-1,
\qquad x\neq3.
$$

El error consiste en perder un factor $-1$. Una buena normalización evita precisamente ese tipo de pérdida.

### Factorizar con un propósito

No toda factorización posible merece hacerse. En cálculo racional buscamos una forma que cumpla alguna función concreta:

- revelar factores comunes;
- hacer visibles las restricciones del dominio;
- comparar orientaciones de factores;
- reducir productos antes de multiplicar;
- evitar expansiones innecesarias.

Por ejemplo, en

$$
\frac{(x-1)(x+2)}{(x-1)(x+5)},
$$

la estructura ya está visible. Expandir numerador y denominador antes de simplificar sería retroceder: destruiría temporalmente la información que necesitamos.

En cambio, en

$$
\frac{x^2+x-2}{x^2+4x+3},
$$

la factorización sí es útil:

$$
x^2+x-2=(x-1)(x+2),
$$

$$
x^2+4x+3=(x+1)(x+3).
$$

No aparece ningún factor común, de modo que la factorización nos permite concluir que **no hay cancelación disponible** mediante las técnicas actuales. Factorizar también puede servir para saber cuándo detenerse.

### Protocolo operativo

Ante una expresión racional que todavía no muestra factores comunes, usaremos este orden:

1. **registre el dominio original**;
2. **factorice sólo donde aporte estructura**;
3. **normalice factores opuestos**, extrayendo los signos $-1$ necesarios;
4. **compare factores completos** de numerador y denominador;
5. **cancele únicamente factores no nulos**;
6. **conserve todas las exclusiones originales**.

El punto 3 es nuevo en esta sección. Los demás reúnen hábitos ya construidos desde [§20.1](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s01).

### Recuperación breve

Simplifique cada expresión, justificando la factorización, los signos y las restricciones que permanecen.

1. $\displaystyle A(x)=\frac{x^2-7x+10}{x^2-4}$;
2. $\displaystyle B(x)=\frac{(4-x)(x+1)}{(x-4)(x-3)}$;
3. $\displaystyle C(x)=\frac{(x-1)^3}{(x-1)(x+2)}$.

**Respuesta razonada.**

1. El denominador original factoriza como

$$
x^2-4=(x-2)(x+2),
$$

por lo que $x\neq2,-2$. Además,

$$
x^2-7x+10=(x-2)(x-5).
$$

Así,

$$
A(x)
=
\frac{(x-2)(x-5)}{(x-2)(x+2)}
=
\frac{x-5}{x+2},
\qquad
x\neq-2,2.
$$

2. El dominio original exige $x\neq4,3$. Como

$$
4-x=-(x-4),
$$

tenemos

$$
B(x)
=
\frac{-(x-4)(x+1)}{(x-4)(x-3)}
=
-\frac{x+1}{x-3},
\qquad
x\neq3,4.
$$

3. El denominador original exige $x\neq1,-2$. Bajo $x\neq1$, cancelamos una copia del factor $x-1$:

$$
C(x)
=
\frac{(x-1)^3}{(x-1)(x+2)}
=
\frac{(x-1)^2}{x+2},
\qquad
x\neq-2,1.
$$

### Qué debemos conservar de esta sección

Factorizar es útil en cálculo racional cuando cambia la representación de una manera que hace visible la estructura relevante. La regla práctica es:

> **Primero conserve el dominio; luego factorice para revelar factores, normalice los factores opuestos mediante signos globales y sólo entonces cancele.**

La identidad

$$
a-x=-(x-a)
$$

permite comparar factores opuestos sin confundirlos. El signo $-1$ debe viajar con la transformación igual que las restricciones del dominio.

En [§20.7](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s07) aplicaremos estas ideas al producto de expresiones racionales, donde factorizar antes de multiplicar puede reducir drásticamente el trabajo y evitar expansiones innecesarias.

## 20.7. Multiplicación de expresiones racionales {#apm-c20-s07}

En las dos secciones anteriores aprendimos a hacer visibles factores, justificar su cancelación y conservar las restricciones que desaparecen de la fórmula final. Al multiplicar expresiones racionales, esas tres ideas actúan al mismo tiempo.

La pregunta que guiará esta sección es:

> **¿Conviene multiplicar primero o mirar primero la estructura de los factores?**

La regla aritmética de la multiplicación es sencilla. La dificultad real consiste en aplicarla sin destruir una estructura que podría simplificar el cálculo.

### La regla de multiplicación

Supongamos que las expresiones

$$
\frac{A}{B}
\qquad\text{y}\qquad
\frac{C}{D}
$$

están definidas en el dominio que estamos considerando. En particular, necesitamos

$$
B\neq0
\qquad\text{y}\qquad
D\neq0.
$$

Entonces

$$
\frac{A}{B}\cdot\frac{C}{D}
=
\frac{AC}{BD}.
$$

Podemos justificarlo mediante inversos:

$$
\frac{A}{B}\cdot\frac{C}{D}
=
AB^{-1}CD^{-1}
=
ACB^{-1}D^{-1}
=
AC(BD)^{-1}
=
\frac{AC}{BD}.
$$

Por tanto,

$$
\boxed{
\frac{A}{B}\cdot\frac{C}{D}
=
\frac{AC}{BD},
\qquad
B\neq0,\ D\neq0.
}
$$

No aparece aquí una condición nueva distinta de las que ya exigían los dos factores. El producto original está definido exactamente donde **ambas expresiones racionales están definidas**.

Si $D_1$ y $D_2$ son sus dominios respectivos, entonces el dominio del producto escrito originalmente es

$$
D_1\cap D_2.
$$

Una simplificación posterior puede producir una fórmula con dominio natural mayor, pero el dominio de procedencia sigue siendo esta intersección.

### Un producto que conviene factorizar antes de ejecutar

Considere

$$
P(x)
=
\frac{x^2-9}{x^2-x-6}
\cdot
\frac{x-2}{x+3}.
$$

Antes de multiplicar, registramos el dominio original. El primer denominador factoriza como

$$
x^2-x-6=(x-3)(x+2),
$$

de modo que exige $x\neq3$ y $x\neq-2$. El segundo factor exige además $x\neq-3$. Por tanto,

$$
\operatorname{Dom}(P)
=
\mathbb R\setminus\{-3,-2,3\}.
$$

Ahora observamos que

$$
x^2-9=(x-3)(x+3).
$$

Así,

$$
P(x)
=
\frac{(x-3)(x+3)}{(x-3)(x+2)}
\cdot
\frac{x-2}{x+3}.
$$

En el dominio original, tanto $x-3$ como $x+3$ son no nulos. Podemos simplificarlos antes de efectuar ninguna multiplicación extensa:

$$
\boxed{
P(x)=\frac{x-2}{x+2},
\qquad
x\neq-3,-2,3.
}
$$

La fórmula final sólo muestra la exclusión $x\neq-2$ si se lee aisladamente. Sin embargo, $x=-3$ y $x=3$ permanecen fuera del dominio porque hacían indefinidos factores del producto original.

### La cancelación cruzada no es una regla nueva

En el ejemplo anterior cancelamos factores que estaban en fracciones distintas. A veces se habla informalmente de **cancelación cruzada**, pero no hay una nueva propiedad algebraica detrás de ella.

Considere

$$
\frac{AU}{B}\cdot\frac{C}{DU},
$$

con $B\neq0$, $D\neq0$ y $U\neq0$. Multiplicar primero daría

$$
\frac{AU}{B}\cdot\frac{C}{DU}
=
\frac{AUC}{BDU}.
$$

Ahora $U$ es un factor común del numerador y del denominador, de modo que [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05) permite escribir

$$
\frac{AUC}{BDU}
=
\frac{AC}{BD}.
$$

Hacer esa cancelación antes de escribir el producto completo sólo evita una escritura intermedia. La justificación sigue siendo la misma: dividimos numerador y denominador por un factor no nulo.

### Comparar dos rutas

Volvamos a

$$
P(x)
=
\frac{x^2-9}{x^2-x-6}
\cdot
\frac{x-2}{x+3}.
$$

La ruta estructural fue

```text
DOMINIO
  ↓
FACTORIZAR
  ↓
CANCELAR FACTORES NO NULOS
  ↓
MULTIPLICAR LO QUE QUEDA
```

y condujo rápidamente a $(x-2)/(x+2)$.

Si multiplicamos primero las formas expandidas, obtenemos

$$
P(x)
=
\frac{(x^2-9)(x-2)}
     {(x^2-x-6)(x+3)}
=
\frac{x^3-2x^2-9x+18}
     {x^3+2x^2-9x-18}.
$$

La expresión es correcta en el mismo dominio original, pero la estructura que permitía simplificar quedó oculta. Para recuperar la forma simple tendríamos que factorizar de nuevo dos polinomios cúbicos que nosotros mismos acabamos de crear.

Expandir no produjo un error lógico; produjo una **representación peor para el objetivo del problema**.

### No es obligatorio expandir lo que ya está bien organizado

Considere

$$
Q(x)
=
\frac{x+1}{x-2}
\cdot
\frac{x+4}{x+3}.
$$

El dominio original es $\mathbb R\setminus\{-3,2\}$. No existe ningún factor común entre numeradores y denominadores. Podemos escribir directamente

$$
\boxed{
Q(x)
=
\frac{(x+1)(x+4)}
     {(x-2)(x+3)},
\qquad
x\neq-3,2.
}
$$

Expandir hasta

$$
\frac{x^2+5x+4}{x^2+x-6}
$$

no constituye una simplificación automática. Ha cambiado la representación, pero no ha reducido la estructura relevante. En este capítulo, cuando queremos controlar dominio y cancelaciones, la forma factorizada suele contener más información visible.

### Un producto puede terminar en una constante

Considere

$$
R(x)
=
\frac{x^2-1}{x^2+3x+2}
\cdot
\frac{x+2}{x-1}.
$$

Como

$$
x^2+3x+2=(x+1)(x+2),
$$

el primer factor exige $x\neq-1,-2$, y el segundo exige $x\neq1$. Así,

$$
\operatorname{Dom}(R)
=
\mathbb R\setminus\{-2,-1,1\}.
$$

Además,

$$
x^2-1=(x-1)(x+1),
$$

por lo que

$$
R(x)
=
\frac{(x-1)(x+1)}{(x+1)(x+2)}
\cdot
\frac{x+2}{x-1}.
$$

Todos los factores visibles se cancelan en el dominio original y obtenemos

$$
\boxed{
R(x)=1,
\qquad
x\neq-2,-1,1.
}
$$

La constante $1$ está definida para todo real, pero el producto original no. Cuanto más simple se vuelve la fórmula final, más fácil puede ser olvidar el dominio de procedencia.

### Qué puede cancelarse en un producto

Cuando varias fracciones se multiplican, podemos comparar **todos los factores del numerador total** con **todos los factores del denominador total**.

Por ejemplo,

$$
\frac{(x-1)(x+4)}{(x+2)(x-3)}
\cdot
\frac{(x+2)(x+5)}{(x-1)(x+7)}
$$

posee factores $x-1$ y $x+2$ que aparecen una vez arriba y una vez abajo. Si el dominio original garantiza que son no nulos, pueden cancelarse.

En cambio, en

$$
\frac{x+1}{x-2}\cdot\frac{x+3}{x+4},
$$

la aparición repetida del símbolo $x$ no crea ningún factor común. La unidad relevante sigue siendo el **factor completo**.

### No-ejemplo: simplificar el producto y reconstruir mal el dominio

Supongamos que alguien calcula

$$
\frac{x^2-1}{x^2+3x+2}
\cdot
\frac{x+2}{x-1}
=1
$$

y concluye que el dominio es $\mathbb R$.

La simplificación algebraica produjo correctamente la fórmula $1$, pero la reconstrucción del dominio es falsa. Los denominadores originales eran

$$
x^2+3x+2=(x+1)(x+2)
$$

y $x-1$. Por tanto, $x=-2$, $x=-1$ y $x=1$ ya estaban prohibidos antes de cualquier cancelación.

El primer error no está en el resultado $1$, sino en intentar deducir el dominio original **a partir de la fórmula final**.

### Protocolo operativo para productos

Para multiplicar expresiones racionales, usaremos el orden

```text
1. LEER EL DOMINIO DE CADA FACTOR.
2. INTERSECTAR LAS RESTRICCIONES.
3. FACTORIZAR NUMERADORES Y DENOMINADORES CUANDO SEA ÚTIL.
4. NORMALIZAR FACTORES OPUESTOS SI APARECEN.
5. CANCELAR SÓLO FACTORES NO NULOS.
6. MULTIPLICAR LOS FACTORES QUE QUEDAN.
7. CONSERVAR TODO EL DOMINIO ORIGINAL.
```

El paso 6 aparece deliberadamente tarde. Multiplicar es fácil; escoger una representación que no multiplique el trabajo innecesariamente es la parte estratégica.

### Recuperación breve

Simplifique los productos siguientes y conserve su dominio original.

1. $\displaystyle A(x)=\frac{x^2-4}{x^2+x-6}\cdot\frac{x+3}{x+2}$;
2. $\displaystyle B(x)=\frac{(x-1)^2}{(x+2)(x-3)}\cdot\frac{x+2}{x-1}$;
3. $\displaystyle C(x)=\frac{x+1}{x-4}\cdot\frac{x+2}{x+5}$.

**Respuesta razonada.**

1. Factorizamos

$$
x^2-4=(x-2)(x+2)
$$

y

$$
x^2+x-6=(x+3)(x-2).
$$

El primer factor exige $x\neq-3,2$ y el segundo exige $x\neq-2$. En el dominio $\mathbb R\setminus\{-3,-2,2\}$,

$$
A(x)
=
\frac{(x-2)(x+2)}{(x+3)(x-2)}
\cdot
\frac{x+3}{x+2}
=1.
$$

Por tanto,

$$
\boxed{
A(x)=1,
\qquad
x\neq-3,-2,2.
}
$$

2. El primer factor exige $x\neq-2,3$ y el segundo exige $x\neq1$. En el dominio $\mathbb R\setminus\{-2,1,3\}$,

$$
B(x)
=
\frac{(x-1)^2}{(x+2)(x-3)}
\cdot
\frac{x+2}{x-1}
=
\frac{x-1}{x-3}.
$$

Así,

$$
\boxed{
B(x)=\frac{x-1}{x-3},
\qquad
x\neq-2,1,3.
}
$$

3. No hay factores comunes. El dominio original exige $x\neq4,-5$, y la forma factorizada ya es adecuada:

$$
\boxed{
C(x)
=
\frac{(x+1)(x+2)}
     {(x-4)(x+5)},
\qquad
x\neq-5,4.
}
$$

### Qué debemos conservar de esta sección

Multiplicar expresiones racionales no significa expandir de inmediato. La regla de cálculo es

$$
\frac{A}{B}\cdot\frac{C}{D}
=
\frac{AC}{BD},
$$

pero la estrategia eficaz es:

> **fijar primero el dominio, factorizar antes de multiplicar, cancelar sólo factores no nulos y multiplicar únicamente lo que sobreviva.**

Las cancelaciones entre fracciones distintas no constituyen una nueva ley: son cancelaciones ordinarias en el numerador y denominador del producto total. Y ninguna de ellas borra las restricciones de los factores originales.

En [§20.8](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s08) estudiaremos la división. Allí aparecerá una obligación adicional: el divisor no sólo deberá estar definido, sino que deberá ser distinto de cero.

## 20.8. División: invertir el divisor completo {#apm-c20-s08}

En [§20.7](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s07) vimos que multiplicar expresiones racionales no añade restricciones distintas de las que ya exigían los factores originales. La división cambia la situación: no basta con que las dos expresiones que participan estén definidas. La expresión que ocupa el lugar de **divisor** debe, además, tener un valor distinto de cero.

La pregunta central será:

> **¿Qué condiciones deben cumplirse antes de reemplazar una división por una multiplicación por el recíproco?**

### La regla de división

Considere

$$
\frac{A}{B}
\div
\frac{C}{D}.
$$

Para que el dividendo $A/B$ esté definido necesitamos $B\neq0$. Para que el divisor $C/D$ esté definido necesitamos $D\neq0$. Pero todavía falta una condición: como estamos dividiendo por $C/D$, ese cociente debe ser distinto de cero.

Bajo $D\neq0$, el cociente $C/D$ es cero exactamente cuando $C=0$. Por tanto, debemos exigir también $C\neq0$.

Si $C\neq0$ y $D\neq0$, entonces el recíproco de $C/D$ es $D/C$, porque

$$
\frac{C}{D}\cdot\frac{D}{C}=1.
$$

Así podemos transformar la división en multiplicación:

$$
\frac{A}{B}
\div
\frac{C}{D}
=
\frac{A}{B}
\cdot
\frac{D}{C}
=
\frac{AD}{BC}.
$$

La regla completa es, por tanto,

$$
\boxed{
\frac{A}{B}
\div
\frac{C}{D}
=
\frac{AD}{BC},
\qquad
B\neq0,\ C\neq0,\ D\neq0.
}
$$

Observe qué símbolo no aparece entre las condiciones: no necesitamos exigir $A\neq0$. Un dividendo puede valer cero; cero dividido por una cantidad no nula sigue siendo cero. La condición adicional de la división recae sobre el **divisor**.

### Estar definido no es lo mismo que ser no nulo

Esta distinción es la parte conceptual más importante de la operación.

Considere como divisor

$$
D(x)=\frac{x-2}{x+5}.
$$

En $x=-5$, la expresión $D(x)$ ni siquiera está definida. En cambio, en $x=2$ sí está definida, pero vale cero:

$$
D(2)=0.
$$

Por tanto, si otra expresión se divide por $D(x)$, ambos valores deben excluirse, aunque por razones diferentes:

- $x=-5$, porque el divisor **no existe**;
- $x=2$, porque el divisor **existe pero vale cero**.

Esta doble comprobación puede resumirse así:

```text
DIVISOR
  ↓
¿ESTÁ DEFINIDO?
  ↓ sí
¿ES DISTINTO DE CERO?
  ↓ sí
SE PUEDE DIVIDIR POR ÉL
```

Una respuesta que controle sólo los denominadores internos del divisor puede seguir siendo incompleta.

### Ejemplo rector: una exclusión que nace del numerador del divisor

Considere

$$
Q(x)
=
\frac{x-2}{x+1}
\div
\frac{x-2}{x-4}.
$$

Antes de invertir nada, determinamos todas las condiciones de la expresión original.

El dividendo exige $x\neq-1$. El divisor $(x-2)/(x-4)$ exige $x\neq4$ para estar definido. Además, ese divisor debe ser distinto de cero. Bajo $x\neq4$, se anula cuando $x-2=0$, de modo que debemos excluir también $x=2$.

Así,

$$
\operatorname{Dom}(Q)
=
\mathbb R\setminus\{-1,2,4\}.
$$

Sólo ahora invertimos el **divisor completo**:

$$
Q(x)
=
\frac{x-2}{x+1}
\cdot
\frac{x-4}{x-2}.
$$

Como $x\neq2$ forma parte del dominio original, el factor $x-2$ es no nulo y puede cancelarse. Obtenemos

$$
\boxed{
Q(x)=\frac{x-4}{x+1},
\qquad
x\neq-1,2,4.
}
$$

La fórmula final ya no muestra las exclusiones $x=2$ ni $x=4$. Sin embargo, ambas pertenecen a la expresión original: en $x=2$ el divisor valía cero y en $x=4$ el divisor ni siquiera estaba definido.

### Invertir el divisor completo

La frase «multiplicar por el recíproco» puede inducir errores si no se identifica qué objeto está siendo invertido.

En

$$
\frac{A}{B}
\div
\frac{C}{D},
$$

el divisor es **todo** el cociente $C/D$. Su recíproco es $D/C$. Por eso

$$
\frac{A}{B}
\div
\frac{C}{D}
=
\frac{A}{B}
\cdot
\frac{D}{C}.
$$

No se invierte el dividendo. Tampoco se invierten simultáneamente las dos fracciones. Y no se conserva el divisor sin cambios.

Por ejemplo,

$$
\frac23\div\frac45
=
\frac23\cdot\frac54
=
\frac56,
$$

mientras que multiplicar sin invertir daría $8/15$, que corresponde a otra operación.

La disciplina de lectura es sencilla:

> **localice primero el signo de división; el objeto completo situado a su derecha es el que debe reemplazarse por su recíproco.**

### El denominador del divisor se mueve, pero su restricción permanece

Considere ahora

$$
R(x)
=
\frac{x^2-9}{x+2}
\div
\frac{x-3}{x+1}.
$$

La expresión original impone tres restricciones.

El dividendo exige $x\neq-2$. El divisor exige $x\neq-1$ para estar definido. Además, el divisor debe ser no nulo, de modo que $x\neq3$.

Por tanto,

$$
\operatorname{Dom}(R)
=
\mathbb R\setminus\{-2,-1,3\}.
$$

Invertimos el divisor completo:

$$
R(x)
=
\frac{x^2-9}{x+2}
\cdot
\frac{x+1}{x-3}.
$$

Ahora factorizamos $x^2-9=(x-3)(x+3)$ y, como $x\neq3$, cancelamos el factor $x-3$:

$$
\boxed{
R(x)
=
\frac{(x+3)(x+1)}{x+2},
\qquad
x\neq-2,-1,3.
}
$$

Observe lo ocurrido con $x=-1$. El factor $x+1$ estaba originalmente en el **denominador del divisor**. Después de invertir, aparece en el numerador y deja de producir una exclusión visible en la fórmula final. Sin embargo, $x=-1$ continúa prohibido porque el divisor original no estaba definido allí.

Éste es un patrón característico de la división: al invertir el divisor, un antiguo denominador puede pasar al numerador, pero su restricción no se borra.

### Por qué aparece la condición $C\neq0$

La transformación

$$
\frac{C}{D}
\longmapsto
\frac{D}{C}
$$

introduce visualmente a $C$ como denominador. Pero la condición $C\neq0$ no es una restricción artificial creada por nuestra técnica. Ya estaba implícita en la operación original, porque dividir por $C/D$ exigía que ese divisor fuera no nulo.

Así, cuando la inversión hace aparecer una nueva barra de fracción con $C$ abajo, sólo está **haciendo visible una obligación previa**.

Esto distingue la inversión legítima del uso de un factor auxiliar arbitrario. Aquí no estamos reduciendo el dominio por conveniencia: estamos expresando explícitamente el dominio que la división ya exigía.

### Un dividendo nulo sí está permitido

Para evitar una simetría falsa entre dividendo y divisor, considere

$$
Z(x)
=
\frac{x-1}{x+2}
\div
\frac{x+3}{x+4}.
$$

En $x=1$, el dividendo vale cero. Eso no produce ningún problema mientras el divisor esté definido y sea no nulo. En efecto,

$$
Z(1)
=
0\div\frac45
=0.
$$

Las restricciones proceden de $x+2\neq0$, de $x+4\neq0$ y de $x+3\neq0$ porque el divisor no puede valer cero. No aparece la condición $x-1\neq0$.

Por tanto, al auditar una división, no debemos declarar «todos los numeradores y denominadores distintos de cero». La regla es más precisa: **los denominadores deben ser no nulos y el divisor completo debe ser no nulo**.

### No-ejemplo: controlar sólo que el divisor esté definido

Vuelva al ejemplo

$$
Q(x)
=
\frac{x-2}{x+1}
\div
\frac{x-2}{x-4}.
$$

Supongamos que alguien registra únicamente $x\neq-1$ y $x\neq4$ y, a continuación, invierte el divisor.

La lista sigue siendo incompleta. En $x=2$ ambas fracciones originales están individualmente definidas, pero la segunda vale cero. La expresión completa intentaría calcular

$$
0\div0,
$$

que no está definido.

El primer error ocurre **antes** de cualquier cancelación: se confundió «el divisor existe» con «podemos dividir por él».

### Cancelar después de invertir

Una vez reemplazada la división por multiplicación, vuelven a aplicarse exactamente las reglas de §[§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05)–20.7: factorizar, normalizar factores opuestos cuando sea necesario y cancelar sólo factores que sabemos no nulos.

La secuencia completa será

```text
1. LEER EL DOMINIO DEL DIVIDENDO.
2. LEER EL DOMINIO DEL DIVISOR.
3. EXIGIR ADEMÁS QUE EL DIVISOR SEA NO NULO.
4. INVERTIR EL DIVISOR COMPLETO.
5. FACTORIZAR Y CANCELAR SÓLO FACTORES AUTORIZADOS.
6. MULTIPLICAR LO QUE QUEDE.
7. CONSERVAR TODAS LAS RESTRICCIONES ORIGINALES.
```

El paso 3 es la diferencia estructural entre multiplicar y dividir expresiones racionales.

### Una simplificación del divisor no puede ampliar retroactivamente el dominio

Considere

$$
H(x)
=
1
\div
\frac{x-2}{x-2}.
$$

La fracción que actúa como divisor está definida sólo para $x\neq2$. En ese dominio vale $1$, por lo que

$$
H(x)=1,
\qquad x\neq2.
$$

No sería correcto simplificar primero $(x-2)/(x-2)$ a $1$ y concluir después que $H$ está definida para todo real. La simplificación del divisor preserva sus valores en el dominio autorizado; no repara el punto donde el divisor original no existía.

Este ejemplo reúne las ideas centrales de §[§20.4](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s04)–20.8: una forma final puede ser extremadamente simple y, aun así, conservar una historia de restricciones que no aparece en su escritura.

### Recuperación breve

Simplifique cada cociente y conserve su dominio original.

1. $\displaystyle A(x)=\frac{x+1}{x-2}\div\frac{x-3}{x+4}$;
2. $\displaystyle B(x)=\frac{x^2-4}{x+1}\div\frac{x-2}{x+3}$;
3. $\displaystyle C(x)=\frac{x-1}{x+2}\div\frac{x^2-1}{x-1}$.

**Respuesta razonada.**

1. El dividendo exige $x\neq2$. El divisor exige $x\neq-4$ y, para ser no nulo, también $x\neq3$. Por tanto,

$$
\operatorname{Dom}(A)
=
\mathbb R\setminus\{-4,2,3\}.
$$

Invertimos el divisor:

$$
A(x)
=
\frac{x+1}{x-2}
\cdot
\frac{x+4}{x-3}.
$$

No hay factores comunes, de modo que

$$
\boxed{
A(x)
=
\frac{(x+1)(x+4)}{(x-2)(x-3)},
\qquad
x\neq-4,2,3.
}
$$

2. El dividendo exige $x\neq-1$. El divisor exige $x\neq-3$ y debe además ser no nulo, de modo que $x\neq2$. Como $x^2-4=(x-2)(x+2)$,

$$
B(x)
=
\frac{(x-2)(x+2)}{x+1}
\cdot
\frac{x+3}{x-2}.
$$

Bajo $x\neq2$, cancelamos $x-2$ y obtenemos

$$
\boxed{
B(x)
=
\frac{(x+2)(x+3)}{x+1},
\qquad
x\neq-3,-1,2.
}
$$

3. El dividendo exige $x\neq-2$. El divisor $(x^2-1)/(x-1)$ exige $x\neq1$. Además, bajo esa condición, el divisor se anula cuando $x^2-1=0$; como $x^2-1=(x-1)(x+1)$ y $x=1$ ya está excluido, debemos excluir también $x=-1$. Así,

$$
\operatorname{Dom}(C)
=
\mathbb R\setminus\{-2,-1,1\}.
$$

Invertimos el divisor y factorizamos:

$$
C(x)
=
\frac{x-1}{x+2}
\cdot
\frac{x-1}{(x-1)(x+1)}.
$$

Como $x\neq1$, cancelamos una copia de $x-1$:

$$
\boxed{
C(x)
=
\frac{x-1}{(x+2)(x+1)},
\qquad
x\neq-2,-1,1.
}
$$

### Qué debemos conservar de esta sección

Dividir por una expresión racional exige más que multiplicar por otra expresión racional. Antes de invertir debemos comprobar que el divisor **existe y no vale cero**.

La regla algebraica es

$$
\frac{A}{B}
\div
\frac{C}{D}
=
\frac{A}{B}
\cdot
\frac{D}{C}
=
\frac{AD}{BC},
$$

con $B\neq0$, $C\neq0$ y $D\neq0$.

La regla de lectura es todavía más importante:

> **registre primero las restricciones del dividendo y del divisor; añada los ceros del divisor completo; sólo entonces invierta el divisor completo y simplifique.**

En [§20.9](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s09) pasaremos a suma y resta. Allí el problema estratégico ya no será invertir, sino escoger un denominador común que permita operar sin introducir trabajo innecesario ni perder el dominio original.

## 20.9. Elegir un denominador común {#apm-c20-s09}

En [§20.8](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s08) la operación exigía identificar un divisor completo y reemplazarlo por su recíproco. En una suma o una resta aparece otro problema: antes de combinar numeradores necesitamos expresar los términos con un mismo denominador.

La pregunta estratégica será:

> **¿Qué denominador común conviene elegir para que todas las fracciones puedan reescribirse sin introducir trabajo ni restricciones innecesarias?**

Existe una respuesta que siempre funciona: multiplicar los denominadores. Pero que una elección sea válida no significa que sea la más económica.

### Un denominador común siempre disponible

Supongamos que trabajamos con

$$
\frac{A}{B}
\qquad\text{y}\qquad
\frac{C}{D},
$$

bajo las condiciones $B\neq0$ y $D\neq0$.

El producto $BD$ es siempre un denominador común. En efecto,

$$
\frac{A}{B}
=
\frac{AD}{BD}
$$

y

$$
\frac{C}{D}
=
\frac{BC}{BD}.
$$

Estas reescrituras son legítimas en el dominio original: para obtener la primera multiplicamos por $D/D$, y allí $D\neq0$; para obtener la segunda multiplicamos por $B/B$, y allí $B\neq0$.

Por tanto, cuando no vemos una estructura mejor, el producto de los denominadores ofrece una ruta segura.

Sin embargo, puede repetir factores que ya estaban compartidos y aumentar innecesariamente el tamaño de la expresión.

### Comparar factores antes de multiplicar denominadores

Considere

$$
\frac{1}{x(x+2)}
\qquad\text{y}\qquad
\frac{3}{x+2}.
$$

El dominio original exige

$$
x\neq0,
\qquad
x\neq-2.
$$

Si multiplicamos los denominadores sin mirar su estructura, obtenemos

$$
x(x+2)^2.
$$

Es un denominador común válido, porque contiene como factores a $x(x+2)$ y a $x+2$. Pero contiene **dos copias** de $x+2$ aunque una sola basta para ambos denominadores.

La estructura muestra inmediatamente una opción más económica:

$$
x(x+2).
$$

La primera fracción ya tiene ese denominador. Para la segunda sólo falta el factor $x$, así que

$$
\frac{3}{x+2}
=
\frac{3x}{x(x+2)},
\qquad x\neq0,-2.
$$

No hemos sumado todavía. Sólo hemos puesto ambas fracciones en una forma compatible usando el mínimo trabajo visible.

### Un factor compartido se escribe una sola vez

Considere ahora los denominadores

$$
x(x+1)
\qquad\text{y}\qquad
(x+1)(x-2).
$$

El producto bruto sería

$$
x(x+1)^2(x-2).
$$

Pero ambos denominadores ya contienen el factor $x+1$. Para que cada uno divida al denominador común basta tomar

$$
\boxed{x(x+1)(x-2)}.
$$

Así, para expresiones como

$$
\frac{A}{x(x+1)}
\qquad\text{y}\qquad
\frac{C}{(x+1)(x-2)},
$$

podemos reescribir

$$
\frac{A}{x(x+1)}
=
\frac{A(x-2)}{x(x+1)(x-2)}
$$

y

$$
\frac{C}{(x+1)(x-2)}
=
\frac{Cx}{x(x+1)(x-2)}.
$$

Las restricciones originales son $x\neq0,-1,2$. Los factores que introdujimos en cada fracción eran precisamente factores de **otro denominador original**, de modo que ya sabíamos que eran no nulos en el dominio común.

Esta observación es importante: la elección económica no se basa en una regla nueva, sino en **no repetir factores que ya están presentes**.

### Potencias repetidas: conservar la potencia suficiente

El mismo principio aparece cuando un factor se repite con distintas potencias. Considere

$$
\frac{1}{(x-1)^2}
\qquad\text{y}\qquad
\frac{2}{(x-1)^3(x+4)}.
$$

El dominio original exige $x\neq1,-4$.

El segundo denominador ya contiene tres copias del factor $x-1$, suficientes para absorber las dos copias que necesita el primero. Por eso un denominador común económico es

$$
\boxed{(x-1)^3(x+4)}.
$$

La primera fracción se reescribe multiplicando por

$$
\frac{(x-1)(x+4)}{(x-1)(x+4)},
$$

que vale $1$ en el dominio original, mientras que la segunda fracción ya posee el denominador elegido.

No necesitamos sumar los exponentes $2+3$. Para construir un denominador que contenga a ambos basta conservar la **mayor potencia necesaria** de cada factor visible.

### Un inventario local de factores

En este capítulo no desarrollaremos una teoría de máximo común divisor o mínimo común múltiplo de polinomios. Esa infraestructura pertenece a C23. Aquí basta con una lectura local de los factores que ya sabemos reconocer.

Cuando los denominadores están factorizados, podemos proceder así:

```text
1. REGISTRAR EL DOMINIO ORIGINAL.
2. FACTORIZAR LOS DENOMINADORES CUANDO SEA ÚTIL.
3. HACER UN INVENTARIO DE LOS FACTORES VISIBLES.
4. PARA CADA FACTOR, CONSERVAR LA POTENCIA MÁXIMA NECESARIA.
5. REESCRIBIR CADA FRACCIÓN MULTIPLICANDO SÓLO POR LOS FACTORES QUE LE FALTAN.
6. COMPROBAR QUE ESOS MULTIPLICADORES SON NO NULOS EN EL DOMINIO ORIGINAL.
```

Este procedimiento no pretende decidir el denominador común «óptimo» en toda situación algebraica. Sólo evita repeticiones evidentes dentro del repertorio de factorizaciones ya disponible.

### Elegir un denominador común no debe reducir el dominio

Aquí aparece una precaución que no debemos perder.

Considere

$$
\frac{1}{x-1}
\qquad\text{y}\qquad
\frac{1}{x+1}.
$$

El dominio original es

$$
\mathbb R\setminus\{-1,1\}.
$$

El denominador

$$
(x-1)(x+1)
$$

es una elección natural. Pero también podríamos fabricar el denominador más grande

$$
(x-1)(x+1)(x+5).
$$

Para hacerlo tendríamos que introducir factores $(x+5)/(x+5)$. Eso exige $x\neq-5$, condición que **no pertenecía al dominio original**.

Por tanto, esa ruta sólo produciría expresiones equivalentes en

$$
\mathbb R\setminus\{-5,-1,1\},
$$

un dominio menor que el original.

El problema no es que el nuevo denominador sea «demasiado grande» en sentido estético. El problema es que hemos introducido una división por una expresión que puede anularse en un punto originalmente permitido.

Así que fijamos una regla:

> **Un denominador común es adecuado para una transformación sobre el dominio original sólo si los factores usados para construirlo son no nulos en todo ese dominio.**

Los factores tomados de los denominadores originales satisfacen automáticamente esta condición en el dominio común; un factor auxiliar arbitrario puede no satisfacerla.

### No confundir denominador común con producto obligatorio

Supongamos que debemos compatibilizar

$$
\frac{2}{(x-3)^2}
\qquad\text{y}\qquad
\frac{x}{x-3}.
$$

El producto de denominadores es $(x-3)^3$, pero no es necesario. Como $(x-3)^2$ ya contiene el factor requerido por $x-3$, podemos usar simplemente

$$
(x-3)^2.
$$

La segunda fracción se transforma en

$$
\frac{x}{x-3}
=
\frac{x(x-3)}{(x-3)^2},
\qquad x\neq3.
$$

La regla «multiplique siempre los denominadores» produce una respuesta válida cuando se preservan las condiciones, pero puede multiplicar también el trabajo. Conviene leer primero la relación entre los denominadores.

### Verificar una reescritura

Una transformación hacia un denominador común debe poder comprobarse sin realizar todavía la suma o la resta.

Por ejemplo, en el dominio $x\neq0,-2$,

$$
\frac{3}{x+2}
=
\frac{3x}{x(x+2)}.
$$

Podemos verificarla cancelando el factor no nulo $x$ en la expresión de la derecha:

$$
\frac{3x}{x(x+2)}
=
\frac{3}{x+2}.
$$

Esta recomposición confirma dos cosas al mismo tiempo: que la fracción conserva su valor y que el factor introducido estaba autorizado por el dominio declarado.

### No-ejemplo: repetir todos los factores sin mirar

Considere

$$
\frac{1}{x(x-1)}
\qquad\text{y}\qquad
\frac{1}{(x-1)^2}.
$$

El producto de los denominadores es

$$
x(x-1)^3.
$$

Es un denominador común válido para $x\neq0,1$, pero no es necesario. El inventario de factores muestra que necesitamos una copia de $x$ y, como máximo, dos copias de $x-1$. Por tanto,

$$
\boxed{x(x-1)^2}
$$

es suficiente.

El error conceptual no sería usar $x(x-1)^3$: esa elección sigue siendo válida en el dominio original. El error sería creer que **multiplicar todos los denominadores es la única manera** de construir un denominador común.

### Recuperación breve

Para cada par de fracciones, determine el dominio original y elija un denominador común económico. Reescriba las fracciones, pero no efectúe todavía la suma o resta.

1. $\displaystyle \frac{2}{x(x-2)}$ y $\displaystyle \frac{3}{x-2}$;
2. $\displaystyle \frac{1}{(x+1)^2}$ y $\displaystyle \frac{4}{(x+1)(x-3)}$;
3. $\displaystyle \frac{1}{x-1}$ y $\displaystyle \frac{1}{x+1}$, frente a la propuesta de usar $(x-1)(x+1)(x+4)$.

**Respuesta razonada.**

1. El dominio original exige $x\neq0,2$. El primer denominador $x(x-2)$ ya contiene al segundo. Elegimos

$$
x(x-2).
$$

Así,

$$
\frac{2}{x(x-2)}
$$

queda igual y

$$
\frac{3}{x-2}
=
\frac{3x}{x(x-2)},
\qquad x\neq0,2.
$$

2. El dominio original exige $x\neq-1,3$. Los factores necesarios son $(x+1)^2$ y $x-3$, de modo que elegimos

$$
(x+1)^2(x-3).
$$

Entonces

$$
\frac{1}{(x+1)^2}
=
\frac{x-3}{(x+1)^2(x-3)}
$$

y

$$
\frac{4}{(x+1)(x-3)}
=
\frac{4(x+1)}{(x+1)^2(x-3)},
\qquad x\neq-1,3.
$$

3. El dominio original es $\mathbb R\setminus\{-1,1\}$. El denominador común natural es

$$
(x-1)(x+1).
$$

La propuesta que añade $x+4$ obligaría a usar $(x+4)/(x+4)$ y excluiría artificialmente $x=-4$, que sí pertenecía al dominio original. Por tanto, no es una transformación equivalente sobre todo el dominio de procedencia.

### Qué debemos conservar de esta sección

Para sumar o restar expresiones racionales necesitamos un denominador común, pero **común** no significa necesariamente **producto completo de todos los denominadores**.

El producto siempre ofrece una opción disponible. Cuando la factorización revela factores compartidos o potencias repetidas, podemos evitar duplicaciones conservando cada factor con la potencia máxima que realmente se necesita.

La regla estratégica queda fijada:

> **lea primero el dominio y los factores; elija después un denominador común que contenga lo necesario, pero no introduzca ceros nuevos en el dominio original.**

En [§20.10](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s10) utilizaremos esta elección para efectuar sumas y restas completas, donde además habrá que controlar con cuidado los signos y la estructura del numerador resultante.

## 20.10. Sumar y restar con estructura visible y signos {#apm-c20-s10}

En [§20.9](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s09) aprendimos a escoger un denominador común sin repetir factores innecesarios ni reducir artificialmente el dominio. Ahora sí efectuaremos la operación completa. La dificultad principal ya no está en encontrar una barra común, sino en conservar tres estructuras al mismo tiempo: el dominio original, los numeradores completos y los signos que actúan sobre ellos.

La pregunta central será:

> **¿Cómo combinar varias expresiones racionales sin perder factores, paréntesis ni signos antes de simplificar el resultado?**

### Cuando el denominador ya es común

Si dos fracciones tienen el mismo denominador, la operación ocurre en el numerador. Bajo $B\neq0$,

$$
\frac{A}{B}+\frac{C}{B}
=
\frac{A+C}{B}
$$

y

$$
\frac{A}{B}-\frac{C}{B}
=
\frac{A-C}{B}.
$$

El denominador no se suma ni se resta. Su función es indicar la unidad fraccionaria común respecto de la cual combinamos los numeradores.

Por ejemplo,

$$
\frac{3}{x-4}+\frac{2x-1}{x-4}
=
\frac{3+(2x-1)}{x-4}
=
\frac{2x+2}{x-4}
=
\frac{2(x+1)}{x-4},
\qquad x\neq4.
$$

Observe el primer paréntesis: escribir $3+(2x-1)$ deja visible que el segundo numerador entra como un bloque completo. En una suma sencilla podríamos omitirlo sin riesgo, pero esa disciplina será decisiva cuando aparezca un signo menos.

### Denominadores distintos: primero compatibilizar, después combinar

Para

$$
\frac{A}{B}
\pm
\frac{C}{D},
$$

con $B\neq0$ y $D\neq0$, el producto $BD$ siempre permite escribir

$$
\frac{A}{B}
\pm
\frac{C}{D}
=
\frac{AD\pm BC}{BD}.
$$

Esta fórmula es correcta, pero [§20.9](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s09) ya mostró que $BD$ no siempre es la elección más económica. En la práctica seguiremos este orden:

1. registrar el dominio original;
2. factorizar denominadores cuando eso revele estructura;
3. elegir un denominador común adecuado;
4. reescribir **cada numerador como un bloque completo**;
5. combinar esos bloques con el signo correcto;
6. simplificar el numerador resultante;
7. factorizar y cancelar sólo después de que la suma o resta se haya convertido en una sola fracción;
8. conservar todas las restricciones originales.

La posición del paso 7 es importante: antes de combinar no existe todavía un único numerador total en el que podamos buscar factores comunes con el denominador.

### Ejemplo rector: una resta que se simplifica sólo al final

Considere

$$
E(x)=
\frac{1}{x-1}
-
\frac{2}{x^2-1}.
$$

Antes de operar, determinamos el dominio. Como

$$
x^2-1=(x-1)(x+1),
$$

la expresión original exige

$$
x\neq1,
\qquad
x\neq-1.
$$

El segundo denominador ya contiene al primero. Por tanto elegimos como denominador común

$$
(x-1)(x+1).
$$

Reescribimos la primera fracción multiplicando por $(x+1)/(x+1)$:

$$
\frac{1}{x-1}
=
\frac{x+1}{(x-1)(x+1)},
\qquad x\neq-1,1.
$$

Ahora sí restamos:

$$
E(x)
=
\frac{x+1}{(x-1)(x+1)}
-
\frac{2}{(x-1)(x+1)}
=
\frac{(x+1)-2}{(x-1)(x+1)}.
$$

Simplificamos el numerador:

$$
(x+1)-2=x-1.
$$

Sólo en este punto aparece un factor común entre numerador y denominador:

$$
E(x)
=
\frac{x-1}{(x-1)(x+1)}.
$$

Como $x\neq1$ pertenece al dominio original, podemos cancelar $x-1$ y obtener

$$
\boxed{
E(x)=\frac{1}{x+1},
\qquad x\neq-1,1.
}
$$

La fórmula final sólo muestra la exclusión $x\neq-1$. La exclusión $x=1$ desapareció visualmente después de la cancelación, pero sigue perteneciendo al dominio original.

Este ejemplo muestra por qué **sumar o restar puede crear un factor cancelable que no existía antes de combinar los numeradores**.

### El signo menos actúa sobre el numerador completo

Considere ahora

$$
F(x)=
\frac{2x+1}{x+2}
-
\frac{x-3}{x-1}.
$$

El dominio original es

$$
\mathbb R\setminus\{-2,1\}.
$$

Como los denominadores no comparten factores, usamos $(x+2)(x-1)$. Entonces

$$
F(x)
=
\frac{(2x+1)(x-1)}{(x+2)(x-1)}
-
\frac{(x-3)(x+2)}{(x-1)(x+2)}.
$$

Al combinar, el signo menos debe aplicarse al **segundo numerador completo**:

$$
F(x)
=
\frac{(2x+1)(x-1)-(x-3)(x+2)}{(x+2)(x-1)}.
$$

Ahora expandimos sólo el numerador, porque allí necesitamos efectuar la resta:

$$
(2x+1)(x-1)=2x^2-x-1
$$

y

$$
(x-3)(x+2)=x^2-x-6.
$$

Por tanto,

$$
\begin{aligned}
(2x+1)(x-1)-(x-3)(x+2)
&=(2x^2-x-1)-(x^2-x-6)\\
&=x^2+5.
\end{aligned}
$$

Así,

$$
\boxed{
F(x)=\frac{x^2+5}{(x+2)(x-1)},
\qquad x\neq-2,1.
}
$$

No necesitamos expandir el denominador. Su forma factorizada sigue mostrando mejor las restricciones y permite comprobar de inmediato que no existe cancelación con el numerador.

### Un error de signo que nace al quitar demasiado pronto los paréntesis

En el cálculo anterior, una escritura peligrosa sería

$$
(2x+1)(x-1)-(x-3)(x+2)
$$

seguida de una expansión en la que sólo se cambia el signo del primer término del segundo producto. El signo menos no actúa sobre una parte del producto: actúa sobre **todo el resultado** de $(x-3)(x+2)$.

La escritura segura es

$$
(2x^2-x-1)-\bigl(x^2-x-6\bigr),
$$

y sólo después distribuir el signo:

$$
2x^2-x-1-x^2+x+6.
$$

Por eso fijamos una regla de microgramática algebraica:

> **En una resta de fracciones, mantenga el numerador sustraído entre paréntesis hasta que el signo menos haya sido distribuido por completo.**

### Factores opuestos dentro de una suma

La normalización de [§20.6](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s06) sigue siendo útil. Considere

$$
G(x)=
\frac{1}{x-2}
+
\frac{1}{2-x}.
$$

El dominio original exige $x\neq2$. Como

$$
2-x=-(x-2),
$$

podemos escribir

$$
\frac{1}{2-x}
=
-\frac{1}{x-2},
\qquad x\neq2.
$$

Por tanto,

$$
\boxed{
G(x)=0,
\qquad x\neq2.
}
$$

La fórmula final $0$ está definida para todo real, pero la suma original no existía en $x=2$. Una vez más, una simplificación extrema puede ocultar por completo el dominio de procedencia.

### Tres o más fracciones: conservar bloques antes de reducir

Considere

$$
H(x)=
\frac{1}{x}
+
\frac{1}{x+1}
-
\frac{1}{x(x+1)}.
$$

El dominio original exige

$$
x\neq0,
\qquad
x\neq-1.
$$

El denominador común económico es $x(x+1)$. Reescribimos cada término:

$$
H(x)
=
\frac{x+1}{x(x+1)}
+
\frac{x}{x(x+1)}
-
\frac{1}{x(x+1)}.
$$

Ahora combinamos los numeradores conservando sus signos:

$$
H(x)
=
\frac{(x+1)+x-1}{x(x+1)}
=
\frac{2x}{x(x+1)}.
$$

Como $x\neq0$, podemos cancelar el factor $x$:

$$
\boxed{
H(x)=\frac{2}{x+1},
\qquad x\neq-1,0.
}
$$

Este ejemplo concentra varias ideas del capítulo: denominador común económico, suma de tres términos, signo menos, cancelación posterior y conservación de una exclusión que deja de ser visible.

### No cancelar a través de una suma o una resta

Vuelva al ejemplo rector:

$$
\frac{1}{x-1}
-
\frac{2}{(x-1)(x+1)}.
$$

Podría resultar tentador «cancelar $x-1$» porque aparece en ambos denominadores. Eso no tiene sentido: los dos términos están separados por una resta. No forman todavía un único cociente con un factor común arriba y abajo.

La cancelación sólo aparece después de combinar:

$$
\frac{x+1-2}{(x-1)(x+1)}
=
\frac{x-1}{(x-1)(x+1)}.
$$

Ahora sí $x-1$ es factor del **numerador total** y del denominador total. La misma regla de [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05) sigue vigente: se cancelan factores de un producto, no fragmentos separados por sumas o restas.

### No-ejemplo: sumar denominadores

Una regla falsa muy común es

$$
\frac{A}{B}+\frac{C}{D}
=
\frac{A+C}{B+D}.
$$

No existe una propiedad algebraica que justifique esta transformación.

Por ejemplo, con $x=1$,

$$
\frac1x+\frac1{x+1}
=1+\frac12
=\frac32,
$$

mientras que la regla falsa produciría

$$
\frac{1+1}{x+(x+1)}\bigg|_{x=1}
=
\frac23.
$$

El error aparece antes de cualquier simplificación: para sumar fracciones necesitamos **un mismo denominador**, no sumar los denominadores existentes.

### Verificar sin rehacer todo el cálculo

Después de obtener una sola fracción conviene realizar al menos dos controles breves:

1. **control estructural:** ¿el denominador final contiene sólo factores autorizados y las restricciones originales siguen registradas?;
2. **control puntual:** elegir un valor permitido sencillo y comprobar que la expresión original y la final producen el mismo número.

El control puntual puede detectar un signo perdido, pero no reemplaza la demostración algebraica. Dos fórmulas que coinciden en uno o varios valores no son por ello equivalentes en todo el dominio, como ya vimos en [§20.4](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s04).

En el ejemplo rector, podemos usar $x=2$:

$$
\frac{1}{2-1}-\frac{2}{2^2-1}
=1-\frac23
=\frac13,
$$

mientras que la fórmula final da

$$
\frac{1}{2+1}=\frac13.
$$

La coincidencia confirma el cálculo en ese punto; la cadena algebraica anterior es la que justifica la igualdad para todo $x\neq-1,1$.

### Protocolo operativo para sumas y restas

Usaremos el siguiente orden:

```text
1. LEER EL DOMINIO ORIGINAL.
2. FACTORIZAR LOS DENOMINADORES CUANDO SEA ÚTIL.
3. ELEGIR UN DENOMINADOR COMÚN ADECUADO.
4. REESCRIBIR CADA TÉRMINO CON SU NUMERADOR COMPLETO ENTRE PARÉNTESIS.
5. COMBINAR LOS NUMERADORES CONSERVANDO TODOS LOS SIGNOS.
6. SIMPLIFICAR Y, SI CONVIENE, FACTORIZAR EL NUMERADOR RESULTANTE.
7. CANCELAR SÓLO FACTORES DEL COCIENTE TOTAL Y SÓLO SI SON NO NULOS.
8. CONSERVAR LAS RESTRICCIONES ORIGINALES.
9. VERIFICAR LA FORMA FINAL SIN RECONSTRUIR EL DOMINIO DESDE ELLA.
```

El punto 4 evita errores de signo; el punto 7 evita cancelaciones ilegales a través de sumas; el punto 8 impide que una simplificación final borre información de procedencia.

### Recuperación breve

Simplifique cada expresión y conserve su dominio original.

1. $\displaystyle A(x)=\frac{3}{x-2}+\frac{x+1}{(x-2)(x+4)}$;
2. $\displaystyle B(x)=\frac{2x-1}{x+1}-\frac{x+3}{x-2}$;
3. $\displaystyle C(x)=\frac1x+\frac1{x+1}-\frac1{x(x+1)}$.

**Respuesta razonada.**

1. El dominio original exige $x\neq2,-4$. El denominador común $(x-2)(x+4)$ ya contiene al primer denominador, de modo que

$$
A(x)
=
\frac{3(x+4)}{(x-2)(x+4)}
+
\frac{x+1}{(x-2)(x+4)}.
$$

Combinando,

$$
A(x)
=
\frac{3x+12+x+1}{(x-2)(x+4)}
=
\boxed{
\frac{4x+13}{(x-2)(x+4)},
\qquad x\neq-4,2.
}
$$

No aparece ningún factor común adicional que pueda cancelarse.

2. El dominio original exige $x\neq-1,2$. Usamos $(x+1)(x-2)$ y mantenemos entre paréntesis el numerador sustraído:

$$
B(x)
=
\frac{(2x-1)(x-2)-(x+3)(x+1)}{(x+1)(x-2)}.
$$

Como

$$
(2x-1)(x-2)=2x^2-5x+2
$$

y

$$
(x+3)(x+1)=x^2+4x+3,
$$

obtenemos

$$
\boxed{
B(x)=\frac{x^2-9x-1}{(x+1)(x-2)},
\qquad x\neq-1,2.
}
$$

3. El dominio original exige $x\neq0,-1$. El denominador común es $x(x+1)$:

$$
C(x)
=
\frac{x+1}{x(x+1)}
+
\frac{x}{x(x+1)}
-
\frac1{x(x+1)}.
$$

Por tanto,

$$
C(x)
=
\frac{(x+1)+x-1}{x(x+1)}
=
\frac{2x}{x(x+1)}.
$$

Como $x\neq0$, cancelamos $x$ y obtenemos

$$
\boxed{
C(x)=\frac2{x+1},
\qquad x\neq-1,0.
}
$$

### Qué debemos conservar de esta sección

Sumar o restar expresiones racionales requiere mucho más que «ponerlas sobre una misma barra». Debemos preservar el dominio, escoger una representación útil y tratar cada numerador como una unidad sintáctica completa.

La regla de trabajo queda fijada:

> **denominador común primero; numeradores completos después; distribuya el signo menos antes de simplificar y cancele sólo cuando ya exista un único cociente factorizable.**

En [§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11) aplicaremos estas ideas dentro de fracciones complejas. Allí el numerador exterior y el denominador exterior podrán contener, cada uno, varias fracciones; el primer método consistirá en reducir cada bloque interior a una sola fracción y sólo entonces efectuar la división exterior.

## 20.11. Fracciones complejas: método interior {#apm-c20-s11}

Hasta ahora hemos operado con expresiones racionales cuyos numeradores y denominadores eran bloques relativamente simples. Una **fracción compleja** añade un nivel de estructura: el numerador exterior, el denominador exterior o ambos contienen a su vez fracciones.

Por ejemplo,

$$
F(x)=
\frac{\dfrac1x+1}
     {\dfrac1x-1}
$$

no debe leerse como una colección plana de símbolos. Hay una división exterior cuyo numerador es el bloque $1/x+1$ y cuyo denominador es el bloque $1/x-1$.

La pregunta central será:

> **¿Cómo simplificar una fracción compleja sin perder las restricciones de sus denominadores internos ni olvidar que el denominador exterior completo debe ser distinto de cero?**

En esta sección usaremos el **método interior**: reducir por separado el numerador exterior y el denominador exterior a una sola fracción, y sólo después efectuar la división entre esos dos resultados.

### Antes de simplificar: leer la expresión por niveles

Volvamos a

$$
F(x)=
\frac{\dfrac1x+1}
     {\dfrac1x-1}.
$$

La primera restricción aparece en las dos fracciones internas $1/x$:

$$
x\neq0.
$$

Pero eso no basta. El denominador exterior completo,

$$
\frac1x-1,
$$

debe además ser distinto de cero.

Bajo $x\neq0$,

$$
\frac1x-1
=
\frac{1-x}{x}.
$$

Este bloque se anula cuando

$$
1-x=0,
$$

es decir, cuando $x=1$. Por tanto,

$$
\boxed{
\operatorname{Dom}(F)
=
\mathbb R\setminus\{0,1\}.
}
$$

Observe que las dos exclusiones tienen orígenes diferentes:

- $x=0$ hace indefinidas las fracciones internas;
- $x=1$ deja definidas esas fracciones, pero hace cero el **denominador exterior completo**.

Esta distinción recupera exactamente la lectura por capas de [§20.3](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s03) y la condición adicional de la división estudiada en [§20.8](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s08).

### Paso 1: reducir el numerador exterior

Trabajemos ahora dentro del bloque superior:

$$
\frac1x+1.
$$

Con denominador común $x$,

$$
\frac1x+1
=
\frac1x+\frac{x}{x}
=
\frac{x+1}{x},
\qquad x\neq0.
$$

El numerador exterior completo se ha convertido en una sola fracción.

### Paso 2: reducir el denominador exterior

Ahora trabajamos dentro del bloque inferior:

$$
\frac1x-1.
$$

De manera análoga,

$$
\frac1x-1
=
\frac1x-\frac{x}{x}
=
\frac{1-x}{x},
\qquad x\neq0.
$$

Además, como este bloque ocupa el lugar de divisor exterior, ya sabemos que debemos mantener

$$
x\neq1.
$$

Por tanto, la fracción compleja original queda representada como

$$
F(x)
=
\frac{\dfrac{x+1}{x}}
     {\dfrac{1-x}{x}},
\qquad x\neq0,1.
$$

### Paso 3: efectuar la división exterior

Ahora la estructura es exactamente la de [§20.8](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s08): una fracción dividida por otra fracción. Invertimos el divisor completo:

$$
F(x)
=
\frac{x+1}{x}
\div
\frac{1-x}{x}
=
\frac{x+1}{x}
\cdot
\frac{x}{1-x}.
$$

Como $x\neq0$ forma parte del dominio original, podemos cancelar el factor $x$:

$$
\boxed{
F(x)=\frac{x+1}{1-x},
\qquad x\neq0,1.
}
$$

La fórmula final sólo muestra de manera visible la exclusión $x\neq1$. La restricción $x\neq0$ ha desaparecido de la escritura, pero no del dominio de procedencia.

### La estructura general del método interior

Una fracción compleja puede pensarse como

$$
\frac{N(x)}{D(x)},
$$

donde tanto $N(x)$ como $D(x)$ pueden contener a su vez varias fracciones.

El método interior sigue esta arquitectura:

```text
1. LEER TODAS LAS FRACCIONES INTERNAS.
2. REGISTRAR SUS RESTRICCIONES.
3. EXIGIR QUE EL DENOMINADOR EXTERIOR COMPLETO SEA NO NULO.
4. REDUCIR EL NUMERADOR EXTERIOR A UNA SOLA FRACCIÓN.
5. REDUCIR EL DENOMINADOR EXTERIOR A UNA SOLA FRACCIÓN.
6. REEMPLAZAR LA BARRA EXTERIOR POR UNA DIVISIÓN ENTRE ESAS DOS FRACCIONES.
7. INVERTIR EL DIVISOR COMPLETO.
8. FACTORIZAR Y CANCELAR SÓLO FACTORES AUTORIZADOS.
9. CONSERVAR TODAS LAS RESTRICCIONES ORIGINALES.
```

Los pasos 4 y 5 organizan la expresión; los pasos 6 y 7 no introducen una técnica nueva, sino que reutilizan la división de [§20.8](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s08).

### El denominador exterior puede crear una exclusión nueva

Considere

$$
G(x)=
\frac{\dfrac1{x-1}+1}
     {\dfrac1{x+1}-1}.
$$

Las fracciones internas exigen

$$
x\neq1,
\qquad
x\neq-1.
$$

Pero aún debemos estudiar el denominador exterior completo. Reducimos ese bloque:

$$
\frac1{x+1}-1
=
\frac{1-(x+1)}{x+1}
=
-\frac{x}{x+1}.
$$

En el dominio donde está definido, este denominador exterior vale cero cuando $x=0$. Por tanto,

$$
\operatorname{Dom}(G)
=
\mathbb R\setminus\{-1,0,1\}.
$$

Ahora reducimos también el numerador exterior:

$$
\frac1{x-1}+1
=
\frac{1+(x-1)}{x-1}
=
\frac{x}{x-1}.
$$

Así,

$$
G(x)
=
\frac{\dfrac{x}{x-1}}
     {-\dfrac{x}{x+1}}
=
\frac{x}{x-1}
\cdot
\frac{x+1}{-x}.
$$

Como $x\neq0$ ya pertenece al dominio original, podemos cancelar $x$ y obtenemos

$$
\boxed{
G(x)=-\frac{x+1}{x-1},
\qquad x\neq-1,0,1.
}
$$

El punto $x=0$ es especialmente instructivo: ninguna fracción interna era indefinida allí. La exclusión aparece porque el **bloque inferior completo** se vuelve cero.

### Una forma final polinómica puede conservar varias exclusiones

Considere ahora

$$
H(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac2{x^2-1}}.
$$

Las fracciones internas imponen

$$
x\neq-1,
\qquad
x\neq1.
$$

El denominador exterior $2/(x^2-1)$ nunca vale cero cuando está definido, de modo que no aparece una exclusión adicional.

Reducimos el numerador exterior:

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{(x+1)+(x-1)}{(x-1)(x+1)}
=
\frac{2x}{x^2-1}.
$$

El denominador exterior ya es una sola fracción. Entonces

$$
H(x)
=
\frac{\dfrac{2x}{x^2-1}}
     {\dfrac2{x^2-1}}
=
\frac{2x}{x^2-1}
\cdot
\frac{x^2-1}{2}.
$$

Como $x\neq\pm1$, el factor $x^2-1$ es no nulo en el dominio original y puede cancelarse. También cancelamos el factor constante $2$:

$$
\boxed{
H(x)=x,
\qquad x\neq-1,1.
}
$$

La fórmula final $x$ está definida para todo real. Sin embargo, la fracción compleja original no existía en $x=\pm1$.

### No simplificar el denominador exterior sin conservar su historia

Supongamos que, en el ejemplo rector, alguien reduce primero

$$
\frac1x-1
=
\frac{1-x}{x}
$$

y luego mira sólo la fórmula final de toda la expresión,

$$
\frac{x+1}{1-x},
$$

para reconstruir el dominio. Concluiría únicamente $x\neq1$ y perdería $x\neq0$.

La reducción interior fue algebraicamente correcta, pero el dominio no puede reconstruirse desde la última forma. Las restricciones deben haberse registrado **antes** de simplificar los bloques interiores.

Este principio puede expresarse así:

> **En una fracción compleja, simplifique los bloques interiores sobre el dominio ya fijado; no use sus formas simplificadas para volver a decidir dónde existía la expresión original.**

### No-ejemplo: olvidar que el bloque inferior es un divisor

Considere nuevamente

$$
G(x)=
\frac{\dfrac1{x-1}+1}
     {\dfrac1{x+1}-1}.
$$

Si alguien registra sólo $x\neq1$ y $x\neq-1$, ha controlado los denominadores internos, pero no la división exterior.

En $x=0$,

$$
\frac1{x+1}-1=1-1=0.
$$

La expresión completa intentaría dividir por cero. El error ocurre **antes** de invertir o cancelar: se olvidó que el bloque inferior entero es un divisor y, por tanto, debe ser distinto de cero.

### Método interior y economía de escritura

El método interior resulta especialmente natural cuando cada bloque exterior contiene pocas fracciones y puede reducirse con rapidez.

Por ejemplo, en

$$
\frac{\dfrac1x+2}
     {\dfrac1x+1}
$$

ambos bloques usan el mismo denominador interno $x$. Reducir cada uno por separado deja inmediatamente

$$
\frac{\dfrac{1+2x}{x}}
     {\dfrac{1+x}{x}},
$$

y la división exterior permite cancelar el factor $x$ bajo $x\neq0$.

En cambio, cuando muchos denominadores internos distintos aparecen a ambos lados de la barra exterior, puede ser más económico eliminarlos todos mediante un multiplicador común. Ése será el segundo método de [§20.12](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s12). Ambos métodos deben producir expresiones equivalentes sobre el mismo dominio original; la diferencia estará en la **ruta** y en el coste algebraico.

### Verificación por recomposición

Después de obtener una forma simple conviene comprobar que la división exterior fue leída correctamente.

En el ejemplo rector,

$$
F(x)=\frac{x+1}{1-x},
\qquad x\neq0,1.
$$

Para $x=2$, la expresión original da

$$
\frac{\frac12+1}{\frac12-1}
=
\frac{\frac32}{-\frac12}
=-3,
$$

mientras que la forma final da

$$
\frac{2+1}{1-2}=-3.
$$

La coincidencia es un control puntual, no una demostración independiente. La justificación general está en la reducción algebraica de los dos bloques y la división posterior.

### Recuperación breve

Simplifique mediante el método interior y conserve el dominio original.

1. $\displaystyle A(x)=\frac{\dfrac1x+2}{\dfrac1x+1}$;
2. $\displaystyle B(x)=\frac{\dfrac1{x-1}-\dfrac1{x+1}}{\dfrac1{x-1}+\dfrac1{x+1}}$;
3. $\displaystyle C(x)=\frac{\dfrac2{x+2}}{\dfrac{x-1}{x+2}+1}$.

**Respuesta razonada.**

1. Las fracciones internas exigen $x\neq0$. El denominador exterior es

$$
\frac1x+1
=
\frac{x+1}{x},
$$

de modo que debe cumplirse además $x\neq-1$. El numerador exterior se reduce a

$$
\frac1x+2
=
\frac{1+2x}{x}.
$$

Por tanto,

$$
A(x)
=
\frac{\dfrac{1+2x}{x}}
     {\dfrac{x+1}{x}}
=
\frac{1+2x}{x}
\cdot
\frac{x}{x+1},
$$

y, como $x\neq0$,

$$
\boxed{
A(x)=\frac{2x+1}{x+1},
\qquad x\neq-1,0.
}
$$

2. Las fracciones internas exigen $x\neq1,-1$. Reducimos el numerador exterior:

$$
\frac1{x-1}-\frac1{x+1}
=
\frac{(x+1)-(x-1)}{x^2-1}
=
\frac2{x^2-1}.
$$

El denominador exterior es

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{(x+1)+(x-1)}{x^2-1}
=
\frac{2x}{x^2-1}.
$$

Además de $x\neq\pm1$, este bloque debe ser no nulo, así que $x\neq0$. Entonces

$$
B(x)
=
\frac{\dfrac2{x^2-1}}
     {\dfrac{2x}{x^2-1}}
=
\frac2{x^2-1}
\cdot
\frac{x^2-1}{2x}
=
\boxed{
\frac1x,
\qquad x\neq-1,0,1.
}
$$

3. La expresión interna exige $x\neq-2$. Reducimos el denominador exterior:

$$
\frac{x-1}{x+2}+1
=
\frac{x-1+x+2}{x+2}
=
\frac{2x+1}{x+2}.
$$

Como este bloque es divisor, debe ser no nulo; por tanto $2x+1\neq0$, es decir, $x\neq-\tfrac12$. Así,

$$
C(x)
=
\frac{\dfrac2{x+2}}
     {\dfrac{2x+1}{x+2}}
=
\frac2{x+2}
\cdot
\frac{x+2}{2x+1}.
$$

Bajo $x\neq-2$ cancelamos $x+2$ y obtenemos

$$
\boxed{
C(x)=\frac2{2x+1},
\qquad x\neq-2,-\frac12.
}
$$

### Qué debemos conservar de esta sección

Una fracción compleja no exige una teoría nueva: combina suma o resta interior con una división exterior. La dificultad está en respetar los niveles de la expresión.

La regla de trabajo queda fijada:

> **dominio por niveles primero; reduzca después el numerador y el denominador exteriores a una fracción cada uno; sólo entonces ejecute la división exterior y simplifique sobre el dominio ya declarado.**

En [§20.12](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s12) resolveremos las mismas clases de expresiones mediante otra ruta: eliminaremos de una vez los denominadores internos multiplicando el numerador y el denominador exteriores por un denominador común no nulo. La comparación entre ambos métodos permitirá escoger la representación más económica sin alterar las condiciones de validez.

## 20.12. Fracciones complejas: eliminar denominadores internos {#apm-c20-s12}

En [§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11) resolvimos fracciones complejas reduciendo primero el numerador exterior y el denominador exterior a una fracción cada uno. Ese método hace visible la división final, pero no es la única ruta posible. Cuando varios denominadores internos comparten factores o aparecen repetidos en ambos bloques, puede resultar más económico eliminarlos todos de una vez.

La pregunta central será:

> **¿Cuándo podemos multiplicar el numerador y el denominador exteriores por una misma expresión para hacer desaparecer las fracciones internas sin cambiar el valor ni reducir el dominio?**

La respuesta contiene una condición decisiva: el multiplicador debe ser **no nulo en todo el dominio original**.

### La transformación que permite limpiar una fracción compleja

Considere una fracción compleja escrita como

$$
\frac{N(x)}{D(x)},
$$

donde $N(x)$ y $D(x)$ pueden contener otras fracciones y donde, por supuesto, $D(x)\neq0$ en el dominio que estamos considerando.

Si elegimos una expresión $M(x)$ tal que

$$
M(x)\neq0
$$

para todo $x$ del dominio original, entonces podemos multiplicar el numerador y el denominador exteriores por $M(x)$:

$$
\frac{N(x)}{D(x)}
=
\frac{M(x)N(x)}{M(x)D(x)}.
$$

La igualdad está justificada porque $M(x)$ es un factor común no nulo del numerador y del denominador del nuevo cociente. En efecto, si quisiéramos recomponer la expresión original, podríamos cancelar ese factor $M(x)$ precisamente porque sabemos que no vale cero.

Esta observación convierte la técnica en una aplicación directa de [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05). No estamos inventando una nueva regla de fracciones: estamos multiplicando arriba y abajo por la misma cantidad no nula.

### Cómo escoger el multiplicador

El objetivo de $M(x)$ será contener todos los factores necesarios para eliminar los denominadores internos que aparecen en el numerador y el denominador exteriores.

En la práctica seguiremos la misma lectura local usada en [§20.9](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s09):

1. registrar primero el dominio original;
2. identificar los denominadores internos;
3. factorizar esos denominadores cuando sea útil;
4. construir un denominador común que contenga los factores necesarios;
5. comprobar que ese multiplicador es no nulo en todo el dominio original;
6. multiplicar por él el numerador y el denominador exteriores;
7. simplificar cada producto por distributividad y cancelaciones autorizadas;
8. conservar todas las restricciones originales.

No necesitamos desarrollar una teoría de mínimo común múltiplo de polinomios. Nos basta un multiplicador común adecuado y controlado.

### Ejemplo rector: limpiar de una vez los denominadores internos

Volvamos a la fracción compleja de [§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11):

$$
F(x)=
\frac{\dfrac1x+1}
     {\dfrac1x-1}.
$$

Ya sabemos que las fracciones internas exigen $x\neq0$ y que el denominador exterior completo se anula en $x=1$. Por tanto,

$$
\operatorname{Dom}(F)
=
\mathbb R\setminus\{0,1\}.
$$

Los denominadores internos son ambos $x$. Elegimos entonces

$$
M(x)=x.
$$

Esta elección es legítima sobre el dominio original porque allí $x\neq0$.

Multiplicamos el numerador y el denominador exteriores por $x$:

$$
F(x)
=
\frac{x\left(\dfrac1x+1\right)}
     {x\left(\dfrac1x-1\right)}.
$$

Distribuyendo,

$$
x\left(\frac1x+1\right)=1+x
$$

y

$$
x\left(\frac1x-1\right)=1-x.
$$

Por tanto,

$$
\boxed{
F(x)=\frac{x+1}{1-x},
\qquad x\neq0,1.
}
$$

Llegamos exactamente a la misma forma obtenida mediante el método interior, pero sin reducir por separado dos fracciones antes de efectuar la división exterior.

### Por qué el multiplicador no puede anularse

La condición $M(x)\neq0$ no es un detalle técnico. Si $M(x)=0$ en un punto del dominio original, la nueva expresión tendría allí numerador y denominador multiplicados por cero y dejaría de representar la fracción de partida.

Por ejemplo, en el caso anterior podríamos intentar usar

$$
M(x)=x(x+2).
$$

Ese multiplicador elimina también los denominadores $x$, pero contiene un factor innecesario $x+2$. En $x=-2$, la fracción original está perfectamente definida, pues $-2\neq0,1$. Sin embargo, al multiplicar arriba y abajo por $x(x+2)$ obtendríamos en ese punto un denominador exterior multiplicado por cero.

La ruta quedaría justificada sólo en

$$
\mathbb R\setminus\{-2,0,1\},
$$

que es un dominio menor que el original.

El problema no es que $x(x+2)$ sea algebraicamente «demasiado grande». El problema es que introduce un cero nuevo en un punto originalmente permitido.

Fijamos así una regla:

> **Para limpiar denominadores internos sin cambiar el dominio de procedencia, el multiplicador debe ser no nulo en todo el dominio original.**

### Un multiplicador construido con denominadores originales es seguro

Cuando $M(x)$ se construye exclusivamente con factores procedentes de denominadores internos originales, su no nulidad suele estar ya garantizada por el dominio.

Considere

$$
H(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac2{x^2-1}}.
$$

Las fracciones internas exigen

$$
x\neq-1,
\qquad
x\neq1.
$$

El denominador exterior $2/(x^2-1)$ no puede valer cero mientras esté definido, porque su numerador es la constante no nula $2$. Por tanto,

$$
\operatorname{Dom}(H)
=
\mathbb R\setminus\{-1,1\}.
$$

Como

$$
x^2-1=(x-1)(x+1),
$$

podemos elegir

$$
M(x)=x^2-1.
$$

Ese multiplicador es no nulo precisamente en el dominio original. Multiplicamos los dos bloques exteriores:

$$
H(x)
=
\frac{(x^2-1)\left(\dfrac1{x-1}+\dfrac1{x+1}\right)}
     {(x^2-1)\left(\dfrac2{x^2-1}\right)}.
$$

En el numerador,

$$
(x^2-1)\frac1{x-1}=x+1
$$

y

$$
(x^2-1)\frac1{x+1}=x-1.
$$

En el denominador,

$$
(x^2-1)\frac2{x^2-1}=2.
$$

Por tanto,

$$
H(x)
=
\frac{(x+1)+(x-1)}{2}
=
\frac{2x}{2}
=x,
$$

con las restricciones heredadas

$$
\boxed{
H(x)=x,
\qquad x\neq-1,1.
}
$$

Este ejemplo muestra con especial claridad la ventaja del método: tres denominadores internos desaparecen mediante una sola elección de representación.

### El denominador exterior sigue necesitando un control propio

Limpiar denominadores internos no sustituye el análisis del denominador exterior completo.

Considere

$$
G(x)=
\frac{\dfrac1{x-1}+1}
     {\dfrac1{x+1}-1}.
$$

Las fracciones internas exigen $x\neq1,-1$. Además, como vimos en [§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11),

$$
\frac1{x+1}-1
=
-\frac{x}{x+1},
$$

de modo que el bloque inferior se anula en $x=0$. Así,

$$
\operatorname{Dom}(G)
=
\mathbb R\setminus\{-1,0,1\}.
$$

Ahora elegimos

$$
M(x)=(x-1)(x+1).
$$

Este multiplicador es no nulo en todo el dominio declarado. Entonces

$$
G(x)
=
\frac{(x-1)(x+1)\left(\dfrac1{x-1}+1\right)}
     {(x-1)(x+1)\left(\dfrac1{x+1}-1\right)}.
$$

Simplificando cada bloque,

$$
(x-1)(x+1)\left(\frac1{x-1}+1\right)
=
(x+1)+(x^2-1)
=
x(x+1),
$$

y

$$
(x-1)(x+1)\left(\frac1{x+1}-1\right)
=
(x-1)-(x^2-1)
=
x(1-x).
$$

Por tanto,

$$
G(x)
=
\frac{x(x+1)}{x(1-x)}.
$$

Como $x\neq0$ ya forma parte del dominio original, podemos cancelar $x$ y obtener

$$
\boxed{
G(x)=\frac{x+1}{1-x}
=-\frac{x+1}{x-1},
\qquad x\neq-1,0,1.
}
$$

El multiplicador común eliminó los denominadores internos, pero la exclusión $x=0$ no procedía de ellos: procedía del denominador exterior completo. Por eso tenía que registrarse **antes** de aplicar el método.

### Multiplicar ambos bloques no significa cancelar una suma

Conviene precisar qué ocurre en una escritura como

$$
M\left(\frac1A+\frac1B\right).
$$

No estamos «cancelando $M$» con términos de una suma. Estamos usando la distributividad:

$$
M\left(\frac1A+\frac1B\right)
=
\frac{M}{A}+\frac{M}{B},
$$

y después simplificamos cada cociente cuando $A$ o $B$ es un factor no nulo de $M$.

Por ejemplo, si $M=AB$ y $A\neq0$, $B\neq0$, entonces

$$
AB\left(\frac1A+\frac1B\right)
=
B+A.
$$

La simplificación ocurre **después de distribuir el producto**. Esto conserva la regla de [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05): nunca cancelamos a través de una suma.

### Comparar los dos métodos

Las §[§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11)–20.12 proporcionan dos rutas para la misma clase de expresiones.

En el **método interior**:

```text
DOMINIO
  ↓
REDUCIR EL BLOQUE SUPERIOR A UNA FRACCIÓN
  ↓
REDUCIR EL BLOQUE INFERIOR A UNA FRACCIÓN
  ↓
DIVIDIR ESAS DOS FRACCIONES
```

En el método de **eliminación de denominadores internos**:

```text
DOMINIO
  ↓
ELEGIR UN MULTIPLICADOR COMÚN NO NULO
  ↓
MULTIPLICAR ARRIBA Y ABAJO POR ÉL
  ↓
DISTRIBUIR Y ELIMINAR LAS FRACCIONES INTERNAS
```

Ninguno es universalmente mejor. El método interior suele ser transparente cuando cada bloque contiene pocas fracciones y sus denominadores comunes son inmediatos. El segundo método puede ser más económico cuando muchos denominadores internos comparten factores y una sola multiplicación los elimina simultáneamente.

Lo que no cambia entre ambos métodos es el dominio. Si las dos rutas están bien justificadas, deben producir expresiones equivalentes **sobre el mismo dominio original**.

### Un criterio práctico de coste

Antes de empezar, conviene mirar la estructura y preguntar:

- ¿puedo reducir cada bloque interior en uno o dos pasos?;
- ¿aparece el mismo conjunto de denominadores varias veces?;
- ¿existe un multiplicador común sencillo cuyo no cero ya esté garantizado por el dominio?;
- ¿qué ruta evita más expansiones y denominadores auxiliares?

Estas preguntas no definen una complejidad formal. Funcionan como criterio de representación: escoger una forma que haga visibles las cancelaciones legítimas y reduzca el número de transformaciones necesarias.

### No-ejemplo: limpiar primero y estudiar el dominio después

Supongamos que partimos de

$$
F(x)=
\frac{\dfrac1x+1}
     {\dfrac1x-1}
$$

y multiplicamos inmediatamente arriba y abajo por $x$:

$$
F(x)=\frac{x+1}{1-x}.
$$

Si a partir de esta última fórmula intentáramos reconstruir el dominio, concluiríamos sólo $x\neq1$. La exclusión $x=0$ habría desaparecido.

El cálculo con $x$ fue legítimo **porque previamente sabíamos que $x\neq0$**. Por tanto, la secuencia correcta no es «limpiar y luego buscar restricciones», sino exactamente la contraria:

> **primero dominio; después multiplicador; después eliminación de denominadores internos.**

### Recuperación breve

Simplifique mediante eliminación de denominadores internos y conserve el dominio original.

1. $\displaystyle A(x)=\frac{\dfrac1x+2}{\dfrac1x+1}$;
2. $\displaystyle B(x)=\frac{\dfrac1{x-1}-\dfrac1{x+1}}{\dfrac1{x-1}+\dfrac1{x+1}}$;
3. $\displaystyle C(x)=\frac{\dfrac2{x+2}}{\dfrac{x-1}{x+2}+1}$.

**Respuesta razonada.**

1. Las fracciones internas exigen $x\neq0$. El denominador exterior $1/x+1=(x+1)/x$ debe además ser no nulo, de modo que $x\neq-1$. Elegimos $M(x)=x$, que es no nulo en el dominio original. Entonces

$$
A(x)
=
\frac{x\left(\dfrac1x+2\right)}
     {x\left(\dfrac1x+1\right)}
=
\frac{1+2x}{1+x}.
$$

Por tanto,

$$
\boxed{
A(x)=\frac{2x+1}{x+1},
\qquad x\neq-1,0.
}
$$

2. Los denominadores internos exigen $x\neq1,-1$. El denominador exterior

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{2x}{x^2-1}
$$

debe ser no nulo, así que también $x\neq0$. Elegimos

$$
M(x)=x^2-1=(x-1)(x+1),
$$

que es no nulo en el dominio original. Entonces

$$
B(x)
=
\frac{(x^2-1)\left(\dfrac1{x-1}-\dfrac1{x+1}\right)}
     {(x^2-1)\left(\dfrac1{x-1}+\dfrac1{x+1}\right)}
=
\frac{(x+1)-(x-1)}{(x+1)+(x-1)}
=
\frac2{2x}.
$$

Así,

$$
\boxed{
B(x)=\frac1x,
\qquad x\neq-1,0,1.
}
$$

3. La fracción interna exige $x\neq-2$. El denominador exterior es

$$
\frac{x-1}{x+2}+1
=
\frac{2x+1}{x+2},
$$

por lo que también debemos exigir $x\neq-\tfrac12$. Elegimos $M(x)=x+2$, no nulo en el dominio original. Entonces

$$
C(x)
=
\frac{(x+2)\left(\dfrac2{x+2}\right)}
     {(x+2)\left(\dfrac{x-1}{x+2}+1\right)}
=
\frac{2}{(x-1)+(x+2)}
=
\frac2{2x+1}.
$$

Por tanto,

$$
\boxed{
C(x)=\frac2{2x+1},
\qquad x\neq-2,-\frac12.
}
$$

Las tres respuestas coinciden con las obtenidas por el método interior en [§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11). La igualdad de resultados no es accidental: ambos procedimientos transforman la misma expresión sobre el mismo dominio declarado.

### Qué debemos conservar de esta sección

Eliminar denominadores internos consiste en multiplicar el numerador y el denominador exteriores por una misma expresión que sea no nula en todo el dominio original. La técnica es legítima por la misma razón que cualquier cancelación: estamos introduciendo un factor común que vale $1$ al comparar numerador y denominador.

La regla de trabajo queda fijada:

> **determine primero el dominio; elija después un multiplicador común no nulo en ese dominio; distribúyalo sobre los dos bloques exteriores; elimine las fracciones internas y conserve todas las restricciones de procedencia.**

Los métodos de §[§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11)–20.12 producen la misma matemática, pero pueden tener costes algebraicos distintos. En [§20.13](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s13) ampliaremos esta comparación a cadenas más largas de operaciones, donde escoger una representación adecuada puede ser tan importante como ejecutar correctamente cada paso.

## 20.13. Cadenas largas y elección de representación {#apm-c20-s13}

En las secciones anteriores aprendimos operaciones concretas: factorizar antes de cancelar, multiplicar y dividir expresiones racionales, escoger denominadores comunes y resolver fracciones complejas por dos métodos. En una cadena larga, sin embargo, el problema principal ya no es recordar una regla aislada. Hay que decidir **en qué orden conviene usar las reglas que ya conocemos**.

La pregunta central será:

> **¿Qué forma de una expresión conviene conservar en cada etapa para que la siguiente transformación sea más simple, más visible y más fácil de justificar?**

Una cadena larga no es una orden de «hacer todo». Es una sucesión de decisiones. En cada paso debemos saber qué objetivo cumple la transformación y sobre qué dominio continúa siendo válida.

### Una cadena larga no obliga a expandir

Considere

$$
E(x)=
\frac{x^2-1}{x^2+x}
\cdot
\frac{x}{x-1}
-
\frac1{x+1}.
$$

Antes de elegir una ruta, fijamos el dominio original. Como

$$
x^2+x=x(x+1),
$$

el primer factor exige $x\neq0,-1$. El segundo exige $x\neq1$ y el último vuelve a exigir $x\neq-1$. Por tanto,

$$
\operatorname{Dom}(E)
=
\mathbb R\setminus\{-1,0,1\}.
$$

Ahora aparece la decisión estratégica. Podríamos multiplicar inmediatamente las dos primeras fracciones en forma expandida. Pero también podemos mirar si su estructura permite reducir primero un bloque completo.

Factorizamos

$$
x^2-1=(x-1)(x+1)
$$

y

$$
x^2+x=x(x+1).
$$

Entonces el producto inicial se convierte en

$$
\frac{(x-1)(x+1)}{x(x+1)}
\cdot
\frac{x}{x-1}.
$$

En el dominio original, los factores $x+1$, $x$ y $x-1$ son no nulos. Podemos cancelarlos y obtenemos

$$
\frac{x^2-1}{x^2+x}
\cdot
\frac{x}{x-1}
=1,
\qquad x\neq-1,0,1.
$$

La cadena completa queda ahora reducida a

$$
E(x)=1-\frac1{x+1}.
$$

Con denominador común $x+1$,

$$
E(x)
=
\frac{x+1-1}{x+1}
=
\frac{x}{x+1}.
$$

Por tanto,

$$
\boxed{
E(x)=\frac{x}{x+1},
\qquad x\neq-1,0,1.
}
$$

La fórmula final sólo muestra $x\neq-1$. Las exclusiones $x=0$ y $x=1$ pertenecen a bloques que desaparecieron durante la simplificación, pero continúan formando parte del dominio de procedencia.

### Cada paso debe tener una razón

La ruta anterior puede escribirse como una cadena de decisiones:

```text
DOMINIO ORIGINAL
  ↓
FACTORAR EL BLOQUE MULTIPLICATIVO
  razón: revelar factores comunes
  ↓
CANCELAR FACTORES NO NULOS
  razón: reducir ese bloque antes de combinarlo con el resto
  ↓
CONSERVAR EL RESULTADO 1 COMO BLOQUE
  razón: no reconstruir una expresión más complicada
  ↓
EFECTUAR LA RESTA RESTANTE
  razón: ahora la estructura es mínima
```

Ninguna flecha significa simplemente «hacer álgebra». Cada transformación tiene una función local.

Este hábito será especialmente importante en problemas no rutinarios: una transformación puede ser correcta y, sin embargo, ser una mala elección porque destruye la estructura que necesitábamos para el siguiente paso.

### Una ruta correcta puede ser estratégicamente mala

Volvamos al producto inicial de $E(x)$:

$$
\frac{x^2-1}{x^2+x}
\cdot
\frac{x}{x-1}.
$$

Si multiplicamos primero sin factorizar, obtenemos

$$
\frac{x(x^2-1)}{(x^2+x)(x-1)}.
$$

Expandiendo,

$$
x(x^2-1)=x^3-x
$$

y

$$
(x^2+x)(x-1)=x^3-x.
$$

Así llegamos a

$$
\frac{x^3-x}{x^3-x}.
$$

Esta expresión vale $1$ donde está definida, pero ahora los ceros relevantes están ocultos dentro del polinomio cúbico. Para justificar la cancelación tendríamos que volver a factorizar

$$
x^3-x=x(x-1)(x+1),
$$

es decir, reconstruir la información que ya estaba visible antes de expandir.

La ruta expandida no es falsa. Es simplemente peor para este problema porque aumenta el trabajo y vuelve menos visible el dominio.

> **Una transformación útil no sólo debe ser correcta: debe conservar o revelar la estructura que hará más fácil el siguiente paso.**

### Los bloques simplificados conservan su historia de dominio

Una cadena larga suele contener subexpresiones que conviene tratar como bloques. Pero simplificar un bloque no borra las condiciones bajo las cuales fue simplificado.

Considere

$$
Q(x)=
\frac{\dfrac{x^2-4}{x^2-x-2}}
     {\dfrac{x+2}{x+1}}.
$$

El bloque superior exige

$$
x^2-x-2=(x-2)(x+1)\neq0,
$$

por lo que $x\neq2,-1$. Además,

$$
\frac{x^2-4}{x^2-x-2}
=
\frac{(x-2)(x+2)}{(x-2)(x+1)}
=
\frac{x+2}{x+1},
$$

pero sólo sobre ese dominio.

El bloque inferior $(x+2)/(x+1)$ exige $x\neq-1$ y, por ser divisor exterior, debe además ser no nulo, de modo que $x\neq-2$.

Por tanto,

$$
\operatorname{Dom}(Q)
=
\mathbb R\setminus\{-2,-1,2\}.
$$

Sobre ese dominio, la fracción compleja toma la forma

$$
Q(x)
=
\frac{\dfrac{x+2}{x+1}}
     {\dfrac{x+2}{x+1}}
=1.
$$

Así,

$$
\boxed{
Q(x)=1,
\qquad x\neq-2,-1,2.
}
$$

El punto $x=2$ ya no aparece en ninguno de los dos bloques visibles después de simplificar el numerador exterior. Sin embargo, sigue excluido porque pertenecía a la historia del bloque original.

Esta observación permite formular una regla para cadenas largas:

> **Cada bloque simplificado debe viajar con las restricciones bajo las cuales fue obtenido.**

### Conservar un bloque puede ser mejor que «aplanar» toda la expresión

Considere ahora

$$
R(x)=
\left(
\frac{
\dfrac1x+\dfrac1{x+1}
}{
\dfrac1x-\dfrac1{x+1}
}
\right)
\cdot
\frac1{2x+1}.
$$

Las fracciones internas exigen $x\neq0,-1$. El denominador exterior de la fracción compleja es

$$
\frac1x-\frac1{x+1}
=
\frac{1}{x(x+1)},
$$

que nunca vale cero cuando está definido. El último factor exige además

$$
2x+1\neq0,
$$

es decir, $x\neq-\tfrac12$.

Por tanto,

$$
\operatorname{Dom}(R)
=
\mathbb R\setminus\left\{-1,-\frac12,0\right\}.
$$

En vez de distribuir el último factor por toda la fracción compleja, simplifiquemos primero el bloque entre paréntesis. Su numerador es

$$
\frac1x+\frac1{x+1}
=
\frac{2x+1}{x(x+1)},
$$

mientras que su denominador es

$$
\frac1x-\frac1{x+1}
=
\frac1{x(x+1)}.
$$

Así, el bloque completo vale

$$
2x+1,
$$

sobre el dominio ya declarado. Entonces

$$
R(x)
=(2x+1)\frac1{2x+1}
=1.
$$

Por tanto,

$$
\boxed{
R(x)=1,
\qquad
x\neq-1,-\frac12,0.
}
$$

La decisión clave fue **cerrar primero un bloque** cuyo resultado estaba diseñado para cancelar con el factor siguiente.

### Mirar hacia adelante sin razonar hacia atrás de manera inválida

Elegir representación exige cierta anticipación. Podemos preguntar qué forma sería útil para el siguiente paso, pero esa expectativa no autoriza una transformación.

En $R(x)$ era útil sospechar que la fracción compleja podía producir un factor relacionado con $2x+1$, porque el último factor era $1/(2x+1)$. Esa observación orienta la búsqueda. Sin embargo, seguimos necesitando demostrar que

$$
\frac{
\dfrac1x+\dfrac1{x+1}
}{
\dfrac1x-\dfrac1{x+1}
}
=2x+1
$$

sobre el dominio correspondiente.

La expectativa decide **qué intentar**; las identidades algebraicas justifican **por qué funciona**.

### Criterios para comparar dos rutas

En este capítulo no definiremos una medida formal de complejidad algebraica. Aun así, podemos comparar rutas con criterios concretos.

Una ruta suele ser preferible si:

1. mantiene visibles las restricciones del dominio;
2. conserva factores útiles en lugar de destruirlos mediante expansiones;
3. reduce temprano bloques que después se repiten o se cancelan;
4. evita denominadores auxiliares innecesarios;
5. disminuye el número de productos extensos y distribuciones de signos;
6. permite justificar cada transición con una regla ya establecida;
7. deja una forma final adecuada para la tarea siguiente.

El último punto impide identificar automáticamente «más expandido» con «más simple» o «más factorizado» con «mejor». La representación adecuada depende del objetivo local.

### Saber cuándo detenerse

Considere

$$
S(x)=
\frac{(x+1)(x+4)}{(x-2)(x+3)}.
$$

No hay factores comunes que cancelar. Si el objetivo es mostrar dominio y estructura multiplicativa, esta forma ya es adecuada. Expandir hasta

$$
\frac{x^2+5x+4}{x^2+x-6}
$$

no resuelve ningún problema nuevo.

En cambio, si una suma posterior exigiera combinar numeradores expandidos, podría convenir expandir **en ese momento**. La misma transformación puede ser inútil en una etapa y útil en otra.

Por eso una cadena bien resuelta no consiste en llevar toda expresión a una única forma canónica informal. Consiste en cambiar de representación cuando existe una razón para hacerlo.

### No-ejemplo: una simplificación local correcta y una conclusión global incompleta

Supongamos que, en

$$
Q(x)=
\frac{\dfrac{x^2-4}{x^2-x-2}}
     {\dfrac{x+2}{x+1}},
$$

alguien simplifica el numerador exterior a $(x+2)/(x+1)$ y escribe inmediatamente

$$
Q(x)=1,
\qquad x\neq-2,-1.
$$

El álgebra visible final parece correcta, pero falta $x\neq2$.

El error no está en la cancelación final. Ocurrió antes: el bloque superior fue reemplazado por una forma equivalente sin conservar la restricción $x\neq2$ que pertenecía a su dominio de procedencia.

Este tipo de fallo es característico de las cadenas largas: **cada paso individual puede parecer correcto y, sin embargo, la composición completa perder información**.

### Un protocolo para cadenas largas

Cuando una expresión reúne varias operaciones, usaremos el siguiente procedimiento:

```text
1. LEER TODA LA EXPRESIÓN Y FIJAR SU DOMINIO ORIGINAL.
2. IDENTIFICAR BLOQUES NATURALES.
3. MIRAR QUÉ FORMA SERÍA ÚTIL PARA EL PASO SIGUIENTE.
4. ELEGIR UNA TRANSFORMACIÓN CON UNA RAZÓN CONCRETA.
5. EJECUTARLA SIN PERDER LAS RESTRICCIONES VIGENTES.
6. CERRAR EL BLOQUE CUANDO YA TENGA UNA FORMA ÚTIL.
7. EVITAR EXPANDIR O REFACTORIZAR SIN PROPÓSITO.
8. REPETIR EL PROCESO CON EL SIGUIENTE BLOQUE.
9. VERIFICAR LA FORMA FINAL Y CONSERVAR EL DOMINIO ORIGINAL COMPLETO.
```

El paso 3 introduce la estrategia. El paso 5 mantiene el rigor. Ninguno sustituye al otro.

### Recuperación breve

Simplifique las expresiones siguientes. Antes de calcular, indique qué bloque conviene transformar primero y por qué. Conserve el dominio original completo.

1. $\displaystyle A(x)=\frac{x^2-9}{x^2-x-6}\cdot\frac{x-2}{x+3}+\frac2{x+2}$;
2. $\displaystyle B(x)=\left(\frac{\dfrac1{x-1}+\dfrac1{x+1}}{\dfrac1{x-1}-\dfrac1{x+1}}\right)\frac1x$;
3. $\displaystyle C(x)=\frac{\dfrac{x^2-4}{x^2-x-2}}{\dfrac{x+2}{x+1}}$.

**Respuesta razonada.**

1. Conviene simplificar primero el producto. Factorizamos

$$
x^2-9=(x-3)(x+3)
$$

y

$$
x^2-x-6=(x-3)(x+2).
$$

El dominio original exige $x\neq3,-2,-3$. Entonces

$$
\frac{x^2-9}{x^2-x-6}\cdot\frac{x-2}{x+3}
=
\frac{x-2}{x+2}.
$$

Ahora la suma restante usa ya el denominador $x+2$:

$$
A(x)
=
\frac{x-2}{x+2}+\frac2{x+2}
=
\frac{x}{x+2}.
$$

Por tanto,

$$
\boxed{
A(x)=\frac{x}{x+2},
\qquad x\neq-3,-2,3.
}
$$

2. Las fracciones internas exigen $x\neq1,-1$, y el factor final $1/x$ exige además $x\neq0$. El denominador exterior de la fracción compleja es

$$
\frac1{x-1}-\frac1{x+1}
=
\frac2{x^2-1},
$$

que no se anula cuando está definido. Conviene reducir primero toda la fracción compleja. Su numerador es

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{2x}{x^2-1}.
$$

Por tanto,

$$
\frac{\dfrac{2x}{x^2-1}}
     {\dfrac2{x^2-1}}
=x.
$$

Entonces

$$
B(x)=x\cdot\frac1x=1,
$$

con el dominio original conservado:

$$
\boxed{
B(x)=1,
\qquad x\neq-1,0,1.
}
$$

3. El bloque superior exige $x\neq2,-1$ y se simplifica, sobre ese dominio, a

$$
\frac{x+2}{x+1}.
$$

El divisor exterior exige $x\neq-1$ y además debe ser no nulo, así que $x\neq-2$. Conviene conservar el bloque simplificado sin olvidar $x\neq2$. Entonces

$$
C(x)
=
\frac{\dfrac{x+2}{x+1}}
     {\dfrac{x+2}{x+1}}
=1.
$$

Así,

$$
\boxed{
C(x)=1,
\qquad x\neq-2,-1,2.
}
$$

### Qué debemos conservar de esta sección

Una cadena larga no exige una nueva colección de reglas. Exige coordinar las que ya conocemos y elegir una representación que sirva al siguiente paso.

La regla estratégica queda fijada:

> **fije primero el dominio; identifique después bloques y objetivos locales; transforme sólo cuando la nueva forma revele estructura, reduzca trabajo o prepare el paso siguiente; y haga viajar las restricciones con cada bloque durante toda la cadena.**

La corrección algebraica y la elección estratégica son problemas distintos. Una ruta puede ser correcta pero innecesariamente costosa; una ruta breve puede ser inválida si pierde una hipótesis. En [§20.14](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s14) añadiremos parámetros y una transferencia limitada desde C18, donde esta disciplina tendrá que conservar condiciones que pueden depender de valores paramétricos o de radicales.



### Dos planes que deben acompañarse

Un plan de cálculo y un plan de verificación responden a preguntas distintas. Para $E=[1/(x-a)-1/(x-b)]\div[(a-b)/((x-a)(x-b))]$, primero se fija $a\ne b$ y $x\ne a,b$. Después, la resta tiene numerador $a-b$ y ambos bloques coinciden: $E=1$. La verificación no consiste solo en sustituir un valor: se reconstruye la resta y se comprueba que el divisor no es cero. **Control resuelto:** si $a=b$, no podemos conservar $E=1$; el divisor original vale cero en todo punto donde existe. Ese caso tiene dominio vacío. Planificar las operaciones no exime de certificar sus hipótesis; detectar un parámetro excepcional es parte del cálculo completo.

## 20.14. Parámetros y transferencia desde C18 {#apm-c20-s14}

Hasta ahora, las restricciones del dominio aparecían como números concretos: $x\neq2$, $x\neq-1$, $x>0$. En muchas expresiones algebraicas, sin embargo, los puntos problemáticos dependen de **parámetros**. Una fórmula puede contener factores como $x-a$ o $x-b$, y el aspecto del dominio puede cambiar cuando dos parámetros toman el mismo valor.

La pregunta central será:

> **¿Cómo conservar correctamente el dominio cuando las exclusiones dependen de parámetros y algunas de ellas pueden coincidir?**

Añadiremos además una transferencia limitada desde C18: aplicaremos los mismos hábitos de lectura a expresiones fraccionarias con radicales. No abriremos una teoría nueva de radicales; reutilizaremos únicamente las condiciones ya establecidas allí.

### Un parámetro se trata como fijo mientras operamos en $x$

Supongamos que $a,b\in\mathbb R$ son parámetros. Al estudiar una expresión en la variable $x$, interpretamos $a$ y $b$ como números reales **fijos**, aunque todavía no conozcamos sus valores concretos.

Considere

$$
F_{a,b}(x)
=
\frac{2(x-a)}
     {(x-a)(x-b)}.
$$

El denominador original exige

$$
(x-a)(x-b)\neq0.
$$

Por tanto debemos tener

$$
x\neq a
\qquad\text{y}\qquad
x\neq b.
$$

Esta escritura lógica es correcta incluso si $a=b$: en ese caso las dos condiciones describen el mismo punto excluido. Si queremos hacer visible el número de puntos distintos del dominio, conviene separar los casos:

$$
\operatorname{Dom}(F_{a,b})
=
\begin{cases}
\mathbb R\setminus\{a,b\}, & a\neq b,\\[4pt]
\mathbb R\setminus\{a\}, & a=b.
\end{cases}
$$

En cualquier caso, $x\neq a$ pertenece al dominio original, de modo que el factor $x-a$ es no nulo y puede cancelarse:

$$
F_{a,b}(x)
=
\frac{2}{x-b},
$$

pero la forma final debe seguir leyéndose sobre el dominio original.

Así,

$$
\boxed{
F_{a,b}(x)=\frac{2}{x-b}
}
$$

con

$$
\boxed{
x\neq a,\quad x\neq b.
}
$$

Si $a\neq b$, la exclusión $x=a$ ha desaparecido de la fórmula simplificada y debe conservarse explícitamente. Si $a=b$, esa exclusión coincide con la que todavía muestra el denominador final.

### Una coincidencia de parámetros puede fusionar exclusiones

La expresión

$$
S_{a,b}(x)
=
\frac1{x-a}
+
\frac1{x-b}
$$

ofrece un segundo tipo de fenómeno.

Para cualquier elección de $a$ y $b$, la expresión original requiere

$$
x\neq a,
\qquad
x\neq b.
$$

Usando como denominador común $(x-a)(x-b)$, obtenemos

$$
S_{a,b}(x)
=
\frac{x-b}{(x-a)(x-b)}
+
\frac{x-a}{(x-a)(x-b)}.
$$

Por tanto,

$$
S_{a,b}(x)
=
\frac{2x-a-b}{(x-a)(x-b)}.
$$

Esta fórmula es correcta sobre el dominio original. Ahora comparemos los dos casos paramétricos.

Si $a\neq b$, los puntos $a$ y $b$ son exclusiones distintas y no aparece ninguna cancelación adicional forzada por la estructura.

Si $a=b$, entonces

$$
S_{a,a}(x)
=
\frac{2x-2a}{(x-a)^2}
=
\frac{2(x-a)}{(x-a)^2}.
$$

Como el dominio original ya exige $x\neq a$, podemos cancelar una copia de $x-a$:

$$
\boxed{
S_{a,a}(x)=\frac2{x-a},
\qquad x\neq a.
}
$$

La coincidencia $a=b$ no autoriza a olvidar restricciones. Lo que ocurre es más preciso: **dos condiciones que antes podían describir puntos distintos pasan a describir el mismo punto**.

### El conjunto de exclusiones, no su repetición escrita, controla el dominio

En una lista de condiciones puede aparecer varias veces el mismo requisito. Por ejemplo, si $a=b$, escribir

$$
x\neq a,\qquad x\neq b
$$

sigue siendo correcto, pero ya no representa dos exclusiones diferentes.

La forma de conjunto evita la ambigüedad:

$$
\mathbb R\setminus\{a,b\}.
$$

Cuando $a=b$,

$$
\{a,b\}=\{a\},
$$

y por tanto

$$
\mathbb R\setminus\{a,b\}
=
\mathbb R\setminus\{a\}.
$$

Este detalle será importante en ejercicios con parámetros: contar condiciones escritas no equivale a contar puntos excluidos.

### Un divisor paramétrico puede añadir otra exclusión

Considere ahora

$$
Q_{a,b}(x)
=
\frac{\dfrac1{x-a}}
     {\dfrac{x-b}{x-a}}.
$$

Primero leemos el dominio por niveles.

Las dos fracciones internas exigen

$$
x\neq a.
$$

Además, el denominador exterior completo

$$
\frac{x-b}{x-a}
$$

debe ser distinto de cero. Bajo $x\neq a$, este cociente se anula cuando

$$
x=b.
$$

Por tanto debemos exigir también

$$
x\neq b.
$$

Así,

$$
\operatorname{Dom}(Q_{a,b})
=
\mathbb R\setminus\{a,b\},
$$

entendiendo nuevamente que si $a=b$ el conjunto posee un único punto.

Sobre este dominio,

$$
Q_{a,b}(x)
=
\frac1{x-a}
\cdot
\frac{x-a}{x-b}
=
\frac1{x-b}.
$$

Por tanto,

$$
\boxed{
Q_{a,b}(x)=\frac1{x-b},
\qquad x\neq a,\quad x\neq b.
}
$$

Si $a\neq b$, la fórmula final ya no muestra $x\neq a$. Si $a=b$, la única exclusión continúa visible porque $x-b=x-a$.

Este ejemplo combina dos ideas ya estudiadas: las restricciones internas de una fracción compleja y los ceros del divisor completo.

### Los casos paramétricos se separan sólo cuando cambian la estructura relevante

No toda aparición de parámetros obliga a una larga clasificación por casos.

Por ejemplo, en

$$
\frac{x-a}{x-b},
$$

el dominio es simplemente $x\neq b$ para todos los valores de $a$ y $b$. Si $a=b$, la expresión se convierte en

$$
\frac{x-a}{x-a},
$$

que vale $1$ para $x\neq a$; pero esa simplificación especial sólo merece destacarse si el objetivo del problema requiere describir la forma resultante.

En cambio, cuando la relación entre parámetros cambia

- cuántos puntos quedan excluidos;
- qué factores coinciden;
- qué cancelaciones aparecen;
- o si un divisor completo puede anularse,

entonces sí debemos distinguir los casos relevantes.

La regla práctica es:

> **No divida en casos por costumbre; divida en casos cuando una relación entre parámetros cambie el dominio o la estructura de la transformación.**

### Transferencia desde C18: un radical en un denominador

C18 estableció que, trabajando en $\mathbb R$, una raíz cuadrada principal $\sqrt{u}$ exige $u\ge0$. Si además aparece en un denominador, necesitamos

$$
\sqrt{u}\neq0,
$$

lo que equivale a exigir $u>0$.

Apliquemos esta lectura a

$$
R_a(x)
=
\frac{x-a}{\sqrt{x-a}},
$$

donde $a\in\mathbb R$ es fijo.

Para que la raíz exista necesitamos

$$
x-a\ge0.
$$

Pero la raíz está en el denominador, así que además debe ser distinta de cero:

$$
\sqrt{x-a}\neq0.
$$

En conjunto,

$$
x-a>0,
$$

es decir,

$$
x>a.
$$

Sobre este dominio podemos usar

$$
x-a=\left(\sqrt{x-a}\right)^2
$$

y escribir

$$
R_a(x)
=
\frac{\left(\sqrt{x-a}\right)^2}{\sqrt{x-a}}.
$$

Como $\sqrt{x-a}\neq0$ para $x>a$, cancelamos una copia:

$$
\boxed{
R_a(x)=\sqrt{x-a},
\qquad x>a.
}
$$

La fórmula final $\sqrt{x-a}$ también está definida en $x=a$, donde vale $0$. Sin embargo, la expresión original no estaba definida allí porque tenía $\sqrt{x-a}$ en el denominador.

La misma disciplina de C20 vuelve a aparecer: **la forma final puede poseer un dominio natural mayor que la expresión de procedencia**.

### Esta transferencia no convierte la expresión en racional

La expresión

$$
\frac{x-a}{\sqrt{x-a}}
$$

es fraccionaria, pero no es una expresión racional en el sentido de [§20.2](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s02), porque su denominador contiene un radical.

Que pueda simplificarse a $\sqrt{x-a}$ no cambia ese hecho histórico ni convierte la expresión original en un cociente de polinomios.

C20 utiliza aquí técnicas de dominio, cancelación y equivalencia sobre un dominio declarado; la teoría del radical proviene de C18.

### No-ejemplo: olvidar la raíz principal

C18 también fijó la identidad

$$
\sqrt{u^2}=|u|
$$

para todo real $u$.

Por tanto, no es correcto afirmar que

$$
\frac{\sqrt{(x-a)^2}}{x-a}=1
$$

para todo $x\neq a$.

La transformación correcta empieza por

$$
\sqrt{(x-a)^2}=|x-a|,
$$

de modo que

$$
\frac{\sqrt{(x-a)^2}}{x-a}
=
\frac{|x-a|}{x-a},
\qquad x\neq a.
$$

No necesitamos desarrollar aquí un análisis sistemático de signos. Un solo valor basta para refutar la identidad propuesta: si $x=a-1$, entonces

$$
\frac{\sqrt{(x-a)^2}}{x-a}
=
\frac1{-1}
=-1.
$$

El error habría sido importar una regla falsa para el radical, no una regla de cálculo racional.

### Dos capas de condiciones pueden coexistir

En una expresión fraccionaria con radicales debemos distinguir las fuentes de restricciones.

Por ejemplo, en

$$
T_a(x)=\frac{\sqrt{x-a}}{x-a},
$$

la raíz exige

$$
x-a\ge0,
$$

mientras que el denominador exige

$$
x-a\neq0.
$$

Juntas producen

$$
x>a.
$$

En ese dominio,

$$
x-a=\left(\sqrt{x-a}\right)^2,
$$

y como $\sqrt{x-a}\neq0$ podemos simplificar:

$$
\boxed{
T_a(x)=\frac1{\sqrt{x-a}},
\qquad x>a.
}
$$

La condición $x>a$ no procede de una sola regla. Es la intersección entre la condición de existencia de la raíz y la condición de no nulidad del denominador.

### Protocolo para parámetros y transferencia radical

Cuando aparezcan parámetros o radicales en una expresión fraccionaria, usaremos este orden:

```text
1. IDENTIFICAR QUÉ SÍMBOLOS SON VARIABLES Y CUÁLES SON PARÁMETROS FIJOS.
2. LEER EL DOMINIO ORIGINAL EN LA VARIABLE.
3. REGISTRAR RESTRICCIONES DEPENDIENTES DE LOS PARÁMETROS.
4. COMPROBAR SI DOS RESTRICCIONES COINCIDEN PARA ALGÚN CASO PARAMÉTRICO RELEVANTE.
5. APLICAR LAS REGLAS DE C20 SIN PERDER ESAS CONDICIONES.
6. SI HAY RADICALES, IMPORTAR SÓLO LAS CONDICIONES YA ESTABLECIDAS EN C18.
7. NO CLASIFICAR AUTOMÁTICAMENTE COMO RACIONAL UNA EXPRESIÓN QUE CONTENGA RADICALES.
8. CONSERVAR EL DOMINIO ORIGINAL AUNQUE LA FORMA FINAL SEA MÁS AMPLIA.
```

Los pasos 3 y 4 controlan los parámetros. El paso 6 evita reabrir la teoría de radicales. El paso 8 mantiene la tesis central de todo el capítulo.

### Recuperación breve

Simplifique cuando sea posible y conserve el dominio original. En los ejercicios con parámetros, distinga los casos sólo si cambia la estructura del dominio o de la simplificación.

1. $\displaystyle A_{a,b}(x)=\frac{3(x-a)}{(x-a)(x-b)}$;
2. $\displaystyle B_{a,b}(x)=\frac1{x-a}+\frac1{x-b}$;
3. $\displaystyle C_a(x)=\frac{\sqrt{x-a}}{x-a}$.

**Respuesta razonada.**

1. El denominador original exige $x\neq a$ y $x\neq b$. Si $a\neq b$, son dos puntos distintos; si $a=b$, describen una sola exclusión. Como $x\neq a$, podemos cancelar el factor $x-a$:

$$
\boxed{
A_{a,b}(x)=\frac{3}{x-b},
\qquad x\neq a,\quad x\neq b.
}
$$

Si $a\neq b$, la exclusión $x=a$ queda oculta en la forma final. Si $a=b$, coincide con la exclusión todavía visible en $x-b$.

2. El dominio original exige $x\neq a$ y $x\neq b$. Con denominador común $(x-a)(x-b)$,

$$
B_{a,b}(x)
=
\frac{x-b+x-a}{(x-a)(x-b)}
=
\frac{2x-a-b}{(x-a)(x-b)}.
$$

Por tanto,

$$
\boxed{
B_{a,b}(x)
=
\frac{2x-a-b}{(x-a)(x-b)},
\qquad x\neq a,\quad x\neq b.
}
$$

Si $a=b$, aparece una simplificación adicional:

$$
B_{a,a}(x)
=
\frac{2(x-a)}{(x-a)^2}
=
\frac2{x-a},
\qquad x\neq a.
$$

3. La raíz exige $x-a\ge0$, mientras que el denominador exige $x-a\neq0$. Por tanto,

$$
x>a.
$$

En ese dominio,

$$
x-a=\left(\sqrt{x-a}\right)^2,
$$

de modo que

$$
C_a(x)
=
\frac{\sqrt{x-a}}
     {\left(\sqrt{x-a}\right)^2}
=
\boxed{
\frac1{\sqrt{x-a}},
\qquad x>a.
}
$$

Esta expresión es fraccionaria con radical y no debe clasificarse automáticamente como racional.

### Qué debemos conservar de esta sección

Los parámetros no modifican las reglas algebraicas, pero pueden modificar **cómo se describen las restricciones**. Dos exclusiones simbólicamente distintas pueden coincidir cuando dos parámetros toman el mismo valor, y una cancelación puede ocultar una condición paramétrica que pertenecía al dominio original.

La transferencia desde C18 obedece a la misma disciplina. Una raíz aporta sus propias condiciones de existencia; si aparece en un denominador, debe además ser no nula.

La regla de trabajo queda fijada:

> **trate los parámetros como fijos, separe sólo los casos que cambien realmente el dominio o la estructura, importe de C18 las condiciones de los radicales y conserve siempre el dominio de procedencia después de simplificar.**

En [§20.15](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s15) utilizaremos todo el repertorio construido hasta aquí para auditar errores: distinguiremos una transformación algebraicamente falsa de una transformación correcta cuyo dominio fue registrado de manera incompleta.

## 20.15. Laboratorio de errores {#apm-c20-s15}

Hasta aquí hemos aprendido a transformar expresiones racionales preservando dominio, estructura y condiciones de validez. En esta sección invertiremos la tarea: en lugar de construir una solución desde cero, **auditaremos soluciones ya escritas**.

La pregunta central será:

> **Cuando una cadena contiene un error, ¿en qué paso aparece por primera vez y de qué tipo es?**

Esta pregunta es más precisa que preguntar simplemente si el resultado final es correcto. Una cadena puede terminar en una fórmula falsa por una manipulación algebraica incorrecta, pero también puede terminar en una fórmula algebraicamente correcta acompañada de un dominio equivocado. Del mismo modo, varios pasos posteriores pueden ser perfectamente válidos respecto de una línea que ya era falsa.

Nuestro objetivo será localizar siempre la **primera ruptura**.

### Cuatro tipos de fallo que debemos distinguir

En este capítulo aparecen, sobre todo, cuatro clases de error.

1. **Error algebraico.** Se aplica una transformación que no preserva el valor de la expresión: se cancelan términos de una suma, se suman denominadores o se invierte incorrectamente un cociente.
2. **Error de dominio.** La transformación algebraica es válida sobre cierto dominio, pero se omite una exclusión original o se reconstruye el dominio a partir de la fórmula final.
3. **Error de divisor.** Se comprueba que un divisor está definido, pero no que sea distinto de cero.
4. **Error de signo.** Se pierde un factor $-1$, se distribuye incorrectamente una resta o se confunden factores opuestos.

Estas categorías pueden coexistir en una misma solución, pero el diagnóstico debe comenzar por la primera línea injustificada.

### Caso 1: cancelación ilegal dentro de una suma

Considere la cadena

$$
\frac{x+3}{x+5}=\frac35.
$$

La primera ruptura está en el único paso escrito. El símbolo $x$ aparece arriba y abajo, pero no es un factor común de todo el numerador y de todo el denominador. La transformación sería legítima sólo ante una estructura multiplicativa como $xA/(xB)$, con $x\neq0$. En cambio, $x+3$ y $x+5$ son sumas.

Éste es un **error algebraico**. No puede repararse agregando una restricción de dominio. En $x=1$,

$$
\frac{1+3}{1+5}=\frac23\neq\frac35.
$$

La reparación correcta consiste en reconocer que no hay factor común que cancelar.

### Caso 2: álgebra correcta, afirmación incompleta

Considere ahora

$$
\frac{x^2-9}{x-3}
=
\frac{(x-3)(x+3)}{x-3}
=
x+3.
$$

Cada transformación algebraica es correcta **para $x\neq3$**. El problema aparece si la cadena se presenta como una identidad válida para todo real. La primera ruptura no está en la factorización ni en la cancelación, sino en haber omitido la condición $x\neq3$.

Éste es un **error de dominio**. La reparación es

$$
\boxed{
\frac{x^2-9}{x-3}=x+3,
\qquad x\neq3.
}
$$

Una solución puede tener todas sus cuentas correctas y seguir siendo matemáticamente incompleta.

### Caso 3: un divisor definido que vale cero

Auditemos

$$
\frac{x-2}{x+1}
\div
\frac{x-2}{x-4}
=
\frac{x-2}{x+1}
\cdot
\frac{x-4}{x-2}
=
\frac{x-4}{x+1},
$$

acompañado sólo de $x\neq-1,4$.

La inversión y la cancelación son correctas **si** el divisor original es no nulo. Pero

$$
\frac{x-2}{x-4}
$$

está definido en $x=2$ y allí vale cero. La primera ruptura ocurre **antes de invertir**: se confundió «el divisor está definido» con «podemos dividir por él».

La reparación exige $x\neq2$:

$$
\boxed{
\frac{x-2}{x+1}
\div
\frac{x-2}{x-4}
=
\frac{x-4}{x+1},
\qquad x\neq-1,2,4.
}
$$

Es un **error de divisor** y, al mismo tiempo, una omisión de dominio.

### Los pasos posteriores pueden ser correctos desde una línea ya falsa

Supongamos que alguien escribe

$$
\frac{x-1}{x+2}
\div
\frac{x-3}{x+4}
=
\frac{x-1}{x+2}
\cdot
\frac{x-3}{x+4}
=
\frac{(x-1)(x-3)}{(x+2)(x+4)}.
$$

La primera igualdad es falsa: debía invertirse el **divisor completo**. Sin embargo, la segunda igualdad sí multiplica correctamente las dos fracciones de la línea anterior.

Eso no salva la solución. Una cadena exige que **cada enlace** sea válido. Una vez rota la primera igualdad, los pasos posteriores pueden describir correctamente otra expresión, pero ya no la original.

La reparación vuelve al primer punto falso:

$$
\frac{x-1}{x+2}
\div
\frac{x-3}{x+4}
=
\frac{x-1}{x+2}
\cdot
\frac{x+4}{x-3},
$$

con $x\neq-2,-4,3$.

> **No busque el último resultado falso; busque la primera transición que dejó de estar justificada.**

### Caso 4: perder el signo de un factor opuesto

Considere

$$
\frac1{x-2}+\frac1{2-x}
=
\frac1{x-2}+\frac1{x-2}
=
\frac2{x-2}.
$$

La primera ruptura ocurre al reemplazar $2-x$ por $x-2$. La relación correcta es

$$
2-x=-(x-2).
$$

Por tanto,

$$
\frac1{2-x}=-\frac1{x-2},
\qquad x\neq2,
$$

y

$$
\boxed{
\frac1{x-2}+\frac1{2-x}=0,
\qquad x\neq2.
}
$$

Éste es un **error de signo**: se perdió el factor global $-1$ que relaciona factores opuestos.

### Caso 5: sumar denominadores

Considere

$$
\frac1{x-1}+\frac1{x+1}=\frac2{2x}=\frac1x.
$$

La primera ruptura aparece al sumar los denominadores. La operación correcta requiere un denominador común. Para $x\neq-1,1$,

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{x+1+x-1}{(x-1)(x+1)}
=
\frac{2x}{x^2-1}.
$$

El resultado falso $1/x$ no sólo cambia los valores: además introduce la exclusión $x=0$, que no pertenecía al dominio original. Una transformación falsa puede alterar simultáneamente la fórmula y el dominio aparente.

### Caso 6: una restricción que desaparece sólo de la escritura

La identidad

$$
\frac1{x-1}-\frac2{x^2-1}=\frac1{x+1}
$$

es correcta sobre $\mathbb R\setminus\{-1,1\}$. Si después de simplificar alguien concluye que el dominio es $\mathbb R\setminus\{-1\}$ porque ése es el dominio natural de la fórmula final, **no hay un error algebraico**: la primera ruptura aparece al reconstruir el dominio desde la última forma.

La exclusión $x=1$ pertenecía a la expresión original y no se borra porque un factor desaparezca de la escritura.

### Caso 7: introducir una restricción que no pertenecía al problema

También podemos excluir demasiado. En

$$
\frac1{x-1}+\frac1{x+1},
$$

el dominio original es $\mathbb R\setminus\{-1,1\}$. Si al construir un denominador común se introduce arbitrariamente un factor $x+5$ mediante $(x+5)/(x+5)$, la ruta exige $x\neq-5$, una condición que no pertenecía al problema.

La nueva cadena podría ser válida sólo sobre un dominio menor, pero ya no sería una transformación equivalente sobre todo el dominio de procedencia.

La auditoría del dominio debe comprobar las dos direcciones:

- no perder condiciones originales;
- no introducir condiciones nuevas sin necesidad.

### Caso 8: una prueba puntual detecta, pero no demuestra

Si alguien propone

$$
\frac{x+1}{x+2}=\frac{x+3}{x+4},
$$

basta evaluar en $x=0$ para obtener $1/2\neq3/4$ y refutar la identidad en cualquier dominio que contenga a $0$.

En cambio, que dos expresiones coincidan en un valor concreto no demuestra que sean equivalentes en todo el dominio.

> **Un contraejemplo puntual puede refutar una identidad; una coincidencia puntual no puede demostrarla.**

La verificación numérica es un instrumento de diagnóstico, no un sustituto de una transformación algebraica justificada.

### Una tabla de diagnóstico

| Síntoma | Primera pregunta | Tipo de fallo probable |
|---|---|---|
| desaparece una suma al «cancelar» | ¿lo eliminado era factor de todo el bloque? | algebraico |
| la fórmula final está definida en más puntos | ¿se conservaron las exclusiones originales? | dominio |
| se divide por una fracción | ¿el divisor existe y además es no nulo? | divisor/dominio |
| aparecen $a-x$ y $x-a$ como si fueran iguales | ¿se perdió un factor $-1$? | signo |
| se obtiene un denominador añadiendo factores arbitrarios | ¿el multiplicador puede anularse en el dominio original? | dominio introducido |
| una larga cadena falla | ¿cuál es la primera flecha injustificada? | primera ruptura |

La tabla no reemplaza el razonamiento. Su función es indicar dónde mirar primero.

### Protocolo de auditoría

```text
1. FIJAR EL DOMINIO DE LA EXPRESIÓN ORIGINAL.
2. LEER LA CADENA DE IZQUIERDA A DERECHA.
3. PARA CADA TRANSICIÓN, IDENTIFICAR LA REGLA QUE LA JUSTIFICA.
4. COMPROBAR LAS HIPÓTESIS DE ESA REGLA EN EL DOMINIO VIGENTE.
5. DETENERSE EN LA PRIMERA TRANSICIÓN NO JUSTIFICADA.
6. CLASIFICAR EL FALLO: ÁLGEBRA, DOMINIO, DIVISOR O SIGNO.
7. NO ATRIBUIR A LOS PASOS POSTERIORES LA CAUSA DEL ERROR ORIGINAL.
8. REPARAR DESDE LA PRIMERA RUPTURA.
9. VERIFICAR QUE EL RESULTADO REPARADO CONSERVE EL DOMINIO DE PROCEDENCIA.
```

No basta con saber que «algo salió mal»: debemos explicar **qué regla dejó de aplicarse y por qué**.

### Recuperación breve

Localice la primera ruptura de cada cadena, clasifique el error y repare la solución.

1. $\displaystyle \frac{x+4}{x+7}=\frac47$.
2. $\displaystyle \frac{x^2-4}{x-2}=x+2$, declarada para todo $x\in\mathbb R$.
3. $\displaystyle \frac{x+1}{x-2}\div\frac{x-3}{x+4}=\frac{x+1}{x-2}\cdot\frac{x-3}{x+4}$.
4. $\displaystyle \frac1{x-3}+\frac1{3-x}=\frac2{x-3}$.

**Respuesta razonada.**

1. La ruptura es una cancelación ilegal de $x$ dentro de dos sumas. Es un error algebraico. No hay factor común que cancelar, de modo que queda

$$
\boxed{\frac{x+4}{x+7},\qquad x\neq-7.}
$$

2. La simplificación es correcta para $x\neq2$, pero la afirmación universal pierde el dominio de procedencia. La forma reparada es

$$
\boxed{
\frac{x^2-4}{x-2}=x+2,
\qquad x\neq2.
}
$$

3. La primera ruptura está al transformar la división en multiplicación sin invertir el divisor. Además, el divisor debe estar definido y ser no nulo, de modo que $x\neq2,-4,3$. La reparación es

$$
\frac{x+1}{x-2}\div\frac{x-3}{x+4}
=
\frac{x+1}{x-2}\cdot\frac{x+4}{x-3},
$$

y por tanto

$$
\boxed{
\frac{(x+1)(x+4)}{(x-2)(x-3)},
\qquad x\neq-4,2,3.
}
$$

4. La primera ruptura consiste en tratar $3-x$ como si fuera $x-3$. Como $3-x=-(x-3)$,

$$
\frac1{3-x}=-\frac1{x-3},
$$

y

$$
\boxed{
\frac1{x-3}+\frac1{3-x}=0,
\qquad x\neq3.
}
$$

### Qué debemos conservar de esta sección

Auditar una solución exige separar tres preguntas:

1. ¿la transformación algebraica preserva el valor?;
2. ¿están satisfechas las hipótesis que autorizan esa transformación?;
3. ¿el dominio de procedencia sigue acompañando a la forma obtenida?

Una cadena deja de justificar la expresión original en la **primera transición que falla**, aunque después continúe con cálculos correctos sobre la expresión equivocada.

La regla de trabajo queda fijada:

> **localice la primera ruptura, identifique la regla que debía justificarla, compruebe sus hipótesis y repare desde ese punto; no confunda un error algebraico con una omisión de dominio.**

En [§20.16](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s16) reuniremos todo el capítulo en un único protocolo de lectura, planificación, transformación, verificación e interpretación. Ese cierre preparará el paso a C21 sin comenzar todavía la resolución sistemática de ecuaciones.



## 20.16. Síntesis y puente a C21 {#apm-c20-s16}

Durante este capítulo aprendimos muchas técnicas: factorizar antes de cancelar, multiplicar y dividir expresiones racionales, elegir denominadores comunes, operar fracciones complejas, controlar parámetros y auditar errores. Pero ninguna de esas técnicas funciona de manera aislada. Todas responden a una misma disciplina: **transformar una expresión sin perder las condiciones que hacen válidas sus transformaciones**.

La pregunta final del capítulo es, por tanto:

> **¿Qué protocolo permite decidir, ejecutar y verificar una transformación racional completa sin separar la fórmula de su dominio?**

La respuesta puede condensarse en seis verbos:

```text
LEER
  ↓
DOMINIO
  ↓
PLAN
  ↓
TRANSFORMAR
  ↓
VERIFICAR
  ↓
INTERPRETAR
```

No son seis trámites independientes. Cada etapa protege a la siguiente.

### 1. Leer: reconocer la arquitectura antes de calcular

Antes de operar, debemos identificar qué objeto tenemos delante.

Preguntamos, por ejemplo:

- ¿hay una sola fracción o una fracción compleja?;
- ¿aparece una multiplicación, una división, una suma o una resta entre bloques?;
- ¿algún cociente completo funciona como divisor?;
- ¿los denominadores ya están factorizados?;
- ¿hay factores opuestos como $a-x$ y $x-a$?;
- ¿aparecen parámetros o radicales cuya interpretación ya conocemos de capítulos anteriores?

Leer bien una expresión evita aplicar una regla correcta al bloque equivocado. En particular, una barra exterior, un signo menos o un divisor completo deben identificarse **antes** de comenzar a simplificar.

### 2. Dominio: fijar dónde existe la expresión original

El dominio no se reconstruye al final. Se determina al comienzo.

Para expresiones racionales simples, todo denominador debe ser distinto de cero. En expresiones anidadas, además, cualquier subexpresión que funcione como divisor debe estar definida y ser no nula.

Por eso el dominio puede contener restricciones que después desaparezcan por completo de la fórmula visible.

Si una expresión original está definida en un conjunto $D$, nuestras transformaciones deben entenderse sobre $D$ salvo que declaremos explícitamente otro objeto.

Ésta es la idea que atravesó todo el capítulo:

> **La forma final puede tener un dominio natural mayor; la transformación conserva el dominio de procedencia.**

### 3. Plan: escoger una representación con propósito

Una vez fijado el dominio, no conviene transformar mecánicamente.

Podemos decidir, según la estructura:

- factorizar antes de multiplicar;
- normalizar factores opuestos;
- conservar una forma factorizada en vez de expandir;
- elegir un denominador común económico;
- reducir por separado los bloques de una fracción compleja;
- o eliminar denominadores internos mediante un multiplicador común no nulo.

Una representación es buena cuando hace visible lo que necesitamos y no introduce restricciones artificiales.

Por tanto, **simplificar** no significa siempre «expandir menos» ni «escribir menos símbolos». Significa escoger una forma que reduzca el trabajo sin ocultar la estructura relevante.

### 4. Transformar: justificar cada paso bajo sus hipótesis

Toda transformación debe responder a una propiedad concreta.

Cuando cancelamos, dividimos por un factor común no nulo. Cuando invertimos un divisor, ya sabemos que ese divisor existe y no vale cero. Cuando multiplicamos por $M/M$, ya sabemos que $M\neq0$ en el dominio vigente. Cuando distribuimos un signo menos, lo aplicamos al bloque completo.

La pregunta local que acompaña a cada flecha es:

> **¿Qué regla autoriza este paso y qué hipótesis exige?**

Si no podemos responderla, todavía no tenemos una transformación justificada.

### 5. Verificar: controlar estructura y valores

Una forma final merece al menos dos controles.

El primero es **estructural**:

- ¿se conservaron todas las restricciones originales?;
- ¿cada cancelación actuó sobre factores completos?;
- ¿los divisores fueron controlados también como posibles ceros?;
- ¿algún factor auxiliar introdujo una exclusión nueva?;
- ¿se perdió un signo al normalizar factores opuestos?

El segundo puede ser **puntual**: escoger un valor sencillo del dominio original y comprobar que la expresión inicial y la forma final coinciden allí.

Ese control numérico es útil para detectar fallos, pero no demuestra por sí solo una identidad. La demostración sigue siendo la cadena algebraica justificada sobre el dominio declarado.

### 6. Interpretar: declarar qué se ha demostrado realmente

El resultado de una simplificación no es sólo una fórmula.

Si partimos de una expresión $E$ definida en $D$ y obtenemos una fórmula $F$, la conclusión completa es

$$
E(x)=F(x)
\qquad\text{para todo }x\in D.
$$

Puede ocurrir que $F$ tenga sentido en puntos que no pertenecían a $D$. Eso no amplía retroactivamente el dominio de $E$.

Por tanto, al cerrar una transformación debemos poder responder:

1. ¿cuál es la fórmula obtenida?;
2. ¿sobre qué dominio hemos demostrado su equivalencia con la expresión original?;
3. ¿qué restricciones dejaron de ser visibles en la fórmula final?;
4. ¿la forma final representa la misma función natural o sólo una regla equivalente sobre un dominio restringido?

### Ejemplo de síntesis: una cadena que termina mucho más simple de lo que empieza

Considere

$$
E(x)=
\frac{x^2-1}{x^2-3x+2}
\cdot
\frac{x-2}{x+1}
-
\frac1{x+3}.
$$

**Leer.** Hay un producto de dos expresiones racionales seguido de una resta.

**Dominio.** Factorizamos sólo para leer las restricciones:

$$
x^2-3x+2=(x-1)(x-2).
$$

La primera fracción exige $x\neq1,2$; la segunda exige $x\neq-1$; la tercera exige $x\neq-3$. Por tanto,

$$
D=\mathbb R\setminus\{-3,-1,1,2\}.
$$

**Plan.** Conviene factorizar el numerador $x^2-1$ antes de multiplicar:

$$
x^2-1=(x-1)(x+1).
$$

**Transformar.** Sobre el dominio $D$,

$$
\frac{x^2-1}{x^2-3x+2}
\cdot
\frac{x-2}{x+1}
=
\frac{(x-1)(x+1)}{(x-1)(x-2)}
\cdot
\frac{x-2}{x+1}.
$$

Los factores $x-1$, $x-2$ y $x+1$ son no nulos en $D$, así que las cancelaciones están autorizadas y el producto vale $1$. Entonces

$$
E(x)=1-\frac1{x+3}.
$$

Con denominador común $x+3$,

$$
E(x)
=
\frac{x+3-1}{x+3}
=
\frac{x+2}{x+3}.
$$

Así,

$$
\boxed{
E(x)=\frac{x+2}{x+3},
\qquad
x\neq-3,-1,1,2.
}
$$

**Verificar.** En $x=0$, que pertenece al dominio original,

$$
\frac{-1}{2}\cdot(-2)-\frac13
=1-\frac13
=\frac23,
$$

mientras que la forma final da

$$
\frac{0+2}{0+3}=\frac23.
$$

La comprobación puntual concuerda con la cadena algebraica.

**Interpretar.** La fórmula $(x+2)/(x+3)$ sólo excluye naturalmente $x=-3$, pero la expresión original también excluía $x=-1,1,2$. Por ello la respuesta completa conserva las cuatro restricciones.

Este ejemplo resume el capítulo: la simplificación puede hacer desaparecer casi toda la historia visible de la expresión, pero esa historia sigue formando parte de la afirmación matemática.

### El protocolo completo

Podemos reunir ahora el método en una sola secuencia operativa:

```text
1. LEER LA EXPRESIÓN POR BLOQUES Y NIVELES.
2. FIJAR EL DOMINIO ORIGINAL ANTES DE TRANSFORMAR.
3. IDENTIFICAR LA ESTRUCTURA QUE CONVIENE HACER VISIBLE.
4. ELEGIR UNA RUTA: FACTORIZAR, NORMALIZAR, COMPATIBILIZAR O REDUCIR BLOQUES.
5. JUSTIFICAR CADA TRANSFORMACIÓN CON SUS HIPÓTESIS.
6. CANCELAR SÓLO FACTORES COMPLETOS Y NO NULOS.
7. NO INTRODUCIR DIVISORES AUXILIARES QUE SE ANULEN EN EL DOMINIO ORIGINAL.
8. CONSERVAR TODAS LAS RESTRICCIONES DE PROCEDENCIA.
9. VERIFICAR LA FORMA FINAL ESTRUCTURALMENTE Y, SI CONVIENE, EN UN PUNTO.
10. INTERPRETAR EL RESULTADO SOBRE EL DOMINIO DECLARADO.
```

Los diez pasos no obligan a escribir diez líneas en cada problema. Con práctica se vuelven una disciplina mental. Lo importante es que ninguno desaparezca de la lógica de la solución.

### Lo que cambia cuando aparece una ecuación

Hasta aquí hemos transformado **expresiones**. En C21 aparecerá una pregunta nueva: no sólo querremos saber si dos fórmulas representan los mismos valores en un dominio, sino **qué valores de la variable hacen verdadera una igualdad**.

Considere, por ejemplo, la ecuación

$$
\frac{x^2-9}{x-3}=6.
$$

C20 ya nos permite afirmar que, sobre el dominio $x\neq3$,

$$
\frac{x^2-9}{x-3}=x+3.
$$

Por tanto, dentro de ese mismo dominio, la ecuación anterior puede reemplazarse por

$$
x+3=6,
\qquad x\neq3.
$$

Aquí nos detenemos. Resolver sistemáticamente la ecuación pertenece a C21.

Lo importante para el puente es otra cosa: **la restricción $x\neq3$ debe acompañar a la ecuación transformada**. Cualquier valor que aparezca más adelante como candidato tendrá que ser compatible con el dominio original.

Éste será uno de los problemas centrales del capítulo siguiente: distinguir transformaciones que preservan exactamente el conjunto solución de aquellas que pueden introducir o perder candidatos y, por tanto, exigen comprobación adicional.

### Expresiones equivalentes y ecuaciones equivalentes

Podemos anticipar la relación lógica sin desarrollar todavía la teoría de C21.

Si $E$ y $F$ son equivalentes sobre un dominio $D$, entonces para cualquier expresión $G$ definida en $D$,

$$
E(x)=G(x)
$$

y

$$
F(x)=G(x)
$$

tienen el mismo valor de verdad para cada $x\in D$.

La condición **sobre $D$** es esencial. Si al pasar de $E$ a $F$ olvidamos el dominio, podemos terminar comparando ecuaciones sobre conjuntos distintos de valores admisibles.

C20 proporciona, por tanto, la infraestructura que C21 necesita:

- dominio antes de transformar;
- equivalencia sobre un dominio declarado;
- hipótesis explícitas para cancelar e invertir;
- control de factores auxiliares;
- diagnóstico de la primera ruptura;
- y verificación de la forma obtenida.

C21 añadirá una nueva capa: el estudio del **conjunto solución**.

### No-ejemplo de puente: borrar el dominio al pasar a una ecuación

Supongamos que alguien parte de

$$
\frac{x^2-1}{x-1}=4
$$

y escribe simplemente

$$
x+1=4
$$

como si ambas ecuaciones vivieran automáticamente sobre todos los reales.

La simplificación de la expresión de la izquierda sólo estaba autorizada bajo $x\neq1$. Por eso la forma correcta del puente es

$$
\frac{x^2-1}{x-1}=4
\quad\Longleftrightarrow\quad
x+1=4
\qquad\text{para }x\neq1.
$$

No resolveremos aquí la ecuación. El objetivo es reconocer que una transformación de expresiones sólo puede convertirse en una transformación de ecuaciones **sobre el dominio donde ya sabíamos que era válida**.

### Recuperación final

Aplique el protocolo del capítulo. No resuelva las ecuaciones del punto 3; sólo prepare correctamente el paso a C21.

1. Simplifique

$$
A(x)=
\frac{x^2-4}{x-2}
\cdot
\frac{x-2}{x+1}
$$

y conserve el dominio original.

2. Para

$$
B(x)=
\frac{\dfrac1x+1}{\dfrac1x-1},
$$

indique primero el dominio y después una forma simple equivalente sobre ese dominio.

3. Reescriba, sin resolverla, la ecuación

$$
\frac{x^2-1}{x-1}=5
$$

mediante una expresión más simple y conserve la condición de admisibilidad.

**Respuesta razonada.**

1. La primera fracción exige $x\neq2$ y la segunda exige $x\neq-1$. Como

$$
x^2-4=(x-2)(x+2),
$$

sobre el dominio $\mathbb R\setminus\{-1,2\}$ tenemos

$$
A(x)
=
\frac{(x-2)(x+2)}{x-2}
\cdot
\frac{x-2}{x+1}
=
\frac{(x+2)(x-2)}{x+1}.
$$

Por tanto,

$$
\boxed{
A(x)=\frac{(x-2)(x+2)}{x+1},
\qquad x\neq-1,2.
}
$$

La exclusión $x=2$ sigue presente aunque una copia del factor $x-2$ haya desaparecido durante la primera simplificación.

2. Las fracciones internas exigen $x\neq0$. Además, el denominador exterior

$$
\frac1x-1=\frac{1-x}{x}
$$

debe ser no nulo, por lo que $x\neq1$. Así,

$$
\operatorname{Dom}(B)=\mathbb R\setminus\{0,1\}.
$$

Reduciendo los dos bloques interiores,

$$
B(x)=\frac{x+1}{1-x},
$$

de modo que

$$
\boxed{
B(x)=\frac{x+1}{1-x},
\qquad x\neq0,1.
}
$$

3. La expresión de la izquierda exige $x\neq1$. Bajo esa condición,

$$
\frac{x^2-1}{x-1}=x+1.
$$

Por tanto, la ecuación puede prepararse para C21 como

$$
\boxed{
x+1=5,
\qquad x\neq1.
}
$$

No hemos resuelto la ecuación; sólo hemos reemplazado una expresión por otra equivalente en el dominio autorizado.

### Qué debemos conservar del capítulo

El cálculo racional no consiste en mover símbolos hasta obtener una forma más corta. Consiste en controlar simultáneamente **valor, estructura y dominio**.

La tesis central del capítulo puede formularse ahora de manera completa:

> **Una transformación algebraica de expresiones racionales conserva valores sobre un dominio declarado cuando cada paso satisface las hipótesis que lo justifican. La fórmula final puede ocultar restricciones, pero no puede borrarlas.**

Por eso la secuencia que debe quedar disponible al terminar C20 es

$$
\boxed{
\text{leer}
\to
\text{dominio}
\to
\text{plan}
\to
\text{transformar}
\to
\text{verificar}
\to
\text{interpretar}.
}
$$

En C21 conservaremos este protocolo y cambiaremos la pregunta final. Ya no bastará con obtener una expresión equivalente: tendremos que determinar qué valores de la variable hacen verdadera una ecuación y demostrar que el conjunto solución obtenido corresponde exactamente al problema original.


***
### Recuperar el prerrequisito que corresponde al error

Ante una ruptura conviene volver al recurso que la explica. Si se cancela $x$ en $(x+1)/x$, el problema es la estructura aditiva: C19 exige factores de todo el numerador y denominador. Si se reemplaza $\sqrt{x^2}$ por $x$ para $x<0$, se ha perdido la raíz principal: C18 da $|x|$. Si una división por una fracción acepta que su numerador sea cero, falta el dominio de la operación de C20. **Control resuelto:** $\sqrt{x^2}/x=|x|/x$ para $x\ne0$, y vale $1$ si $x>0$ y $-1$ si $x<0$. El resultado no es una única constante. Identificar el origen del fallo permite reparar el primer paso, no acumular reglas de memoria sobre una cadena ya inválida.

# Ejercicios

El banco de ejercicios está organizado por **función cognitiva**. En este primer bloque no se busca velocidad de cálculo: se busca leer con precisión qué tipo de expresión aparece, qué divisiones contiene, cuál es su dominio de procedencia y qué afirmaciones pueden hacerse sin confundir una fórmula con la función natural que determina.

Salvo que se indique lo contrario, trabajamos sobre los números reales. No resuelva ecuaciones ni efectúe simplificaciones extensas si no son necesarias para justificar la respuesta.

## A. Reconocimiento y lectura estructural


**1.** **Nivel A.** Clasifique cada expresión como **polinómica**, **racional** y/o **fraccionaria**. Cuando pertenezca a más de una clase, indíquelo y justifique la clasificación a partir de la estructura, no de los valores que pueda tomar:
   (a) $\dfrac{3x-1}{x^2+4}$;  
   (b) $\dfrac{\sqrt{x}+2}{x-5}$;  
   (c) $2x^4-x+7$;  
   (d) $\dfrac{x+1}{\sqrt{x^2+1}}$.


**2.** **Nivel A.** Para cada una de las expresiones siguientes, distinga entre **tener una barra de fracción visible** y **pertenecer a la clase de las expresiones racionales**. No haga una simplificación completa; explique qué estructura permite decidir:
   (a) $\dfrac{x^2-1}{x+3}$;  
   (b) $x+\dfrac{1}{x-2}$;  
   (c) $\dfrac{\sqrt{x-1}}{x+4}$;  
   (d) $\dfrac{\dfrac{x+1}{x-2}}{\dfrac{x+3}{x+4}}$.


**3.** **Nivel A.** Lea, sin simplificar,

$$
T(x)=
\frac{\dfrac{2}{x-1}+1}
     {\dfrac{x+3}{x-4}}.
$$

Identifique: (i) el numerador exterior; (ii) el denominador exterior; (iii) todos los denominadores internos visibles; (iv) qué **subexpresión completa**, además de estar definida, debe ser distinta de cero. Explique por qué mirar sólo los denominadores pequeños no basta.


**4.** **Nivel A.** Considere

$$
E(x)=
\frac{x^2-9}{x^2-x-6}
\cdot
\frac{x-2}{x+3}
+
\frac{2}{x+2}.
$$

Sin efectuar la cadena completa, separe la expresión en **bloques naturales**, indique cuál convendría transformar primero y nombre la finalidad de esa transformación: revelar factores, escoger denominador común, invertir un divisor o expandir. Justifique por qué una expansión total inmediata no es la primera lectura más informativa.


**5.** **Nivel A.** Determine el dominio de

$$
A(x)=\frac{x+1}{(x-2)^2(x+4)}
$$

sin simplificar ni expandir. Explique por qué la potencia $(x-2)^2$ no crea dos puntos excluidos y por qué el numerador no impone ninguna restricción adicional.


**6.** **Nivel A.** Determine el dominio de la expresión compuesta

$$
B(x)=
\frac{\dfrac{1}{x-2}}
     {\dfrac{x+1}{x+4}}
$$

**sin invertir todavía el divisor**. Para cada punto excluido, indique si la causa es: denominador interno nulo o denominador exterior completo igual a cero.


**7.** **Nivel A.** Compare

$$
E(x)=\frac{x^2-25}{x-5}
\qquad\text{y}\qquad
F(x)=x+5.
$$

Responda razonadamente: (i) ¿cuál es el dominio natural de cada expresión?; (ii) ¿son equivalentes sobre $\mathbb R\setminus\{5\}$?; (iii) si cada fórmula define una función con su dominio natural y codominio $\mathbb R$, ¿son la misma función?; (iv) ¿qué dato impide identificarlas aunque la fórmula simplificada coincida?


**8.** **Nivel A.** Considere

$$
G(x)=\frac{x^2-1}{x^2+x}
\qquad\text{y}\qquad
H(x)=\frac{x-1}{x}.
$$

Determine sus dominios naturales y decida sobre qué dominio pueden compararse como expresiones equivalentes. Después explique por qué las funciones naturales asociadas no son iguales. Use el valor $x=-1$ para hacer visible la diferencia entre las dos situaciones, sin tomar esa comprobación puntual como demostración de la equivalencia general.


**9.** **Nivel A.** Antes de efectuar ninguna división, analice

$$
Q(x)=
\frac{x+1}{x-3}
\div
\frac{x-2}{x+4}.
$$

Enumere todas las restricciones del dominio original y explique la causa de cada una. En particular, responda: ¿por qué debe excluirse $x=2$ aunque no anule ningún denominador interno? ¿Debe excluirse $x=-1$ porque anula el numerador del dividendo? Justifique ambas respuestas.


**10.** **Nivel A.** Estudie la expresión

$$
R(x)=
\frac{x+2}{x-1}
\div
\frac{x^2-9}{x^2+x-6}.
$$

Sin simplificar el cociente completo, determine su dominio original. Factorice sólo lo necesario para distinguir cuatro fenómenos: (i) un punto donde el dividendo no está definido; (ii) puntos donde el divisor no está definido; (iii) un punto donde el divisor está definido pero vale cero; (iv) un factor que podría desaparecer si el divisor se simplificara. Explique por qué ninguna cancelación posterior puede borrar una exclusión ya registrada.

## B. Fluidez técnica

En este bloque sí se espera ejecutar las operaciones completas. En todos los ejercicios, determine primero el dominio original y consérvelo después de simplificar. Factorice antes de expandir cuando ello haga visible una cancelación; no cancele términos separados por sumas o restas.


**11.** **Nivel B.** Simplifique

$$
\frac{x^2-5x+6}{x^2-4}
$$

factorizando numerador y denominador. Justifique cada cancelación y escriba la forma final junto con **todas** las restricciones del dominio original.


**12.** **Nivel B.** Simplifique

$$
\frac{x^2-6x+9}{x^2-x-6}.
$$

Controle la multiplicidad del factor común: indique cuántas copias aparecen arriba y abajo, cuál se cancela y cuál permanece visible en la forma final. Conserve el dominio original.


**13.** **Nivel B.** Simplifique

$$
\frac{(5-x)(x+2)}{(x-5)(x-1)}.
$$

Normalice primero los factores opuestos mediante un signo global y sólo después cancele. Registre el dominio antes de operar.


**14.** **Nivel B.** Simplifique

$$
\frac{x^3-4x^2}{x^2-16}.
$$

Factorice sólo lo necesario para hacer visible la estructura multiplicativa. No expanda la forma final. Declare qué restricción desaparece de la escritura después de cancelar.


**15.** **Nivel B.** Simplifique el producto

$$
\frac{x^2-4}{x^2+5x+6}
\cdot
\frac{x+3}{x-2}.
$$

Determine primero la intersección de los dominios de los dos factores. Factorice antes de multiplicar y conserve todas las exclusiones aunque el producto termine en una constante.


**16.** **Nivel B.** Simplifique

$$
\frac{(x-1)^2}{(x+2)(x-3)}
\cdot
\frac{x+2}{x-1}.
$$

Realice las cancelaciones antes de efectuar productos innecesarios y escriba el resultado con el dominio original completo.


**17.** **Nivel B.** Simplifique el cociente

$$
\frac{x^2-9}{x+4}
\div
\frac{x-3}{x+2}.
$$

Distinga las restricciones que hacen que el dividendo y el divisor estén definidos de la condición adicional que impide que el divisor valga cero. Invierta únicamente el divisor completo.


**18.** **Nivel B.** Simplifique

$$
\frac{x-1}{x+2}
\div
\frac{x^2-1}{x-1}.
$$

Factorice el divisor sólo después de registrar su dominio. Identifique expresamente el valor que hace cero al divisor completo y conserve todas las restricciones después de cancelar.


**19.** **Nivel B.** Sume y simplifique

$$
\frac{3x+1}{x-2}
+
\frac{x-5}{x-2}.
$$

Mantenga el denominador común, combine los numeradores como bloques y conserve el dominio original.


**20.** **Nivel B.** Simplifique

$$
\frac{2}{x(x-1)}
+
\frac{3}{x-1}.
$$

Elija un denominador común económico: no multiplique denominadores completos si uno ya contiene todos los factores del otro. Declare el dominio antes de reescribir las fracciones.


**21.** **Nivel B.** Reste y simplifique

$$
\frac{2x+3}{x+1}
-
\frac{x-4}{x-2}.
$$

Mantenga entre paréntesis el numerador sustraído hasta distribuir por completo el signo menos. Conserve la forma factorizada del denominador final si no aparece una cancelación legítima.


**22.** **Nivel B.** Simplifique la suma de tres términos

$$
\frac1x+
\frac2{x+1}-
\frac1{x(x+1)}.
$$

Use el denominador común $x(x+1)$, combine cuidadosamente los numeradores y cancele sólo después de haber obtenido una única fracción. Conserve las dos exclusiones originales.


**23.** **Nivel B.** Simplifique mediante el **método interior**

$$
\frac{\dfrac1x+3}
     {\dfrac1x+1}.
$$

Determine el dominio por niveles antes de operar: incluya tanto la restricción de las fracciones internas como el valor que hace cero al denominador exterior completo.


**24.** **Nivel B.** Simplifique mediante el método interior

$$
\frac{\dfrac1{x-2}-\dfrac1{x+2}}
     {\dfrac1{x-2}+\dfrac1{x+2}}.
$$

Registre primero las restricciones internas y determine después si el bloque inferior introduce una exclusión adicional. Conserve el dominio original en la forma final.


**25.** **Nivel B.** Simplifique eliminando denominadores internos:

$$
\frac{\dfrac2{x+1}}
     {\dfrac{x-2}{x+1}+1}.
$$

Determine antes el dominio original, elija un multiplicador común no nulo en ese dominio y distribúyalo sobre el numerador y el denominador exteriores. No reconstruya el dominio a partir de la fórmula final.


**26.** **Nivel B.** Simplifique

$$
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac3{x^2-1}}.
$$

Puede usar el método interior o eliminar denominadores internos, pero debe declarar el dominio **antes** de elegir la ruta. Explique brevemente por qué el denominador exterior no añade un cero nuevo además de los ya excluidos por $x^2-1$.



## C. Justificación y reconstrucción

En este bloque no basta con obtener una forma equivalente. Cada respuesta debe identificar **qué regla se usa, qué hipótesis la autorizan y sobre qué dominio sigue siendo válida la transformación**. Cuando una forma final tenga un dominio natural mayor, conserve explícitamente el dominio de procedencia. En los ejercicios 35–38 compare también la calidad de distintas rutas, no sólo su corrección.


**27.** **Nivel C.** Justifique la regla de cancelación

$$
\frac{AC}{BC}=\frac{A}{B}.
$$

Indique las hipótesis exactas que deben satisfacerse sobre $B$ y $C$, explique por qué la cancelación equivale a dividir numerador y denominador por un factor común no nulo y describa qué falla si $C=0$. No use la palabra «cancelar» como justificación en sí misma.


**28.** **Nivel C.** Reconstruya y justifique la regla

$$
\frac{A}{B}\div\frac{C}{D}
=
\frac{AD}{BC}.
$$

Separe tres obligaciones: que el dividendo esté definido, que el divisor esté definido y que el divisor completo sea distinto de cero. Explique por qué las hipótesis son $B\neq0$, $C\neq0$ y $D\neq0$, y por qué no es necesario exigir $A\neq0$.


**29.** **Nivel C.** Suponga que $B\neq0$ y $D\neq0$. Justifique las reescrituras

$$
\frac{A}{B}=\frac{AD}{BD}
\qquad\text{y}\qquad
\frac{C}{D}=\frac{BC}{BD}.
$$

Identifique en cada paso el factor por el cual se multiplica numerador y denominador, explique por qué ese factor representa $1$ en el dominio vigente y deduzca de ahí por qué $BD$ es siempre un denominador común disponible. Distinga «válido» de «económico».


**30.** **Nivel C.** Sea

$$
F(x)=\frac{N(x)}{D(x)}
$$

una fracción compleja definida en un dominio $E$, y sea $M(x)$ una expresión. Explique por qué la transformación

$$
\frac{N(x)}{D(x)}
=
\frac{M(x)N(x)}{M(x)D(x)}
$$

preserva el valor en todo $E$ sólo si $M(x)\neq0$ para cada $x\in E$. Relacione esta condición con la regla de cancelación de [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05) y explique por qué un factor auxiliar que se anule en un punto de $E$ reduce artificialmente el dominio de la ruta.


**31.** **Nivel C.** Considere

$$
R(x)=\frac{x^2-9}{x^2-x-6}.
$$

Factorice y simplifique sólo después de determinar el dominio original. Después responda: (i) ¿qué restricción deja de ser visible en la forma final?; (ii) ¿cuál es el dominio natural de esa forma final?; (iii) ¿sobre qué dominio es correcta la equivalencia obtenida? Explique por qué esos tres datos no son redundantes.


**32.** **Nivel C.** Estudie el producto

$$
P(x)=
\frac{x^2-1}{x^2+3x+2}
\cdot
\frac{x+2}{x-1}.
$$

Demuestre que la fórmula final puede reducirse a la constante $1$, pero reconstruya antes el dominio original a partir de los dos factores. Compare ese dominio con el dominio natural de la constante $1$ y explique por qué concluir «$P(x)=1$ para todo real» sería una afirmación más fuerte y falsa.


**33.** **Nivel C.** Justifique completamente la identidad restringida

$$
\frac1{x-1}-\frac2{x^2-1}
=
\frac1{x+1}.
$$

Debe incluir: dominio original, elección del denominador común, momento exacto en que aparece un factor cancelable y dominio de la fórmula final. Explique por qué la igualdad es correcta sobre $\mathbb R\setminus\{-1,1\}$ y no debe presentarse como identidad sobre todo el dominio natural de $1/(x+1)$.


**34.** **Nivel C.** Analice

$$
H(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac2{x^2-1}}.
$$

Determine primero el dominio por niveles y luego simplifique hasta una forma polinómica. Explique por qué una forma final sin denominadores visibles puede seguir representando correctamente la expresión original sólo acompañada de restricciones. Indique con precisión cuáles son.


**35.** **Nivel C.** Considere

$$
F(x)=
\frac{\dfrac1x+1}
     {\dfrac1x-1}.
$$

Resuélvala por las dos rutas estudiadas en §[§20.11](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s11)–20.12:

1. **método interior**: reduzca por separado el numerador exterior y el denominador exterior;
2. **eliminación de denominadores internos**: multiplique ambos bloques exteriores por un multiplicador común adecuado.

Antes de operar, fije un único dominio original para ambas rutas. Compare después: número de reescrituras, aparición de fracciones intermedias y visibilidad de las restricciones. Explique por qué dos métodos distintos deben producir expresiones equivalentes sobre el mismo dominio.


**36.** **Nivel C.** Para transformar

$$
\frac1{x-1}+\frac1{x+1},
$$

un estudiante propone usar como denominador común

$$
(x-1)(x+1)(x+5).
$$

Otro propone usar sólo

$$
(x-1)(x+1).
$$

Determine el dominio original y analice ambas propuestas. Explique por qué la primera puede producir una transformación algebraicamente correcta en un dominio menor y, sin embargo, no constituye una equivalencia sobre todo el dominio de procedencia. Identifique exactamente qué factor auxiliar causa el problema.


**37.** **Nivel C.** Compare dos rutas para

$$
P(x)=
\frac{x^2-9}{x^2-x-6}
\cdot
\frac{x-2}{x+3}.
$$

- **Ruta I:** factorizar antes de multiplicar;
- **Ruta II:** multiplicar primero las formas expandidas.

Muestre que ambas rutas pueden ser correctas sobre el mismo dominio si se justifican adecuadamente. Después explique por qué la Ruta I es estratégicamente superior para este problema: señale qué factores permanecen visibles, qué trabajo evita y qué información de dominio se vuelve más fácil de controlar.


**38.** **Nivel C.** Considere

$$
G(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac1{x-1}-\dfrac1{x+1}}.
$$

Un estudiante quiere eliminar denominadores internos y duda entre

$$
M_1(x)=x^2-1
\qquad\text{y}\qquad
M_2(x)=(x^2-1)(x-4).
$$

Determine primero el dominio original completo de $G$. Después decida cuál de los dos multiplicadores permite una transformación equivalente sobre **todo** ese dominio y cuál introduce una restricción artificial. Ejecute la ruta válida hasta obtener una forma simple y explique por qué la ruta con el multiplicador extra no es «más general» por contener más factores.


## D. Diagnóstico y primera ruptura

En este bloque no se pide sólo corregir un resultado. Para cada cadena, localice **la primera transición que deja de estar justificada**, clasifique el fallo y repare la solución desde ese punto. Distinga con precisión entre error algebraico, pérdida o introducción de dominio, divisor nulo y error de signo. Si el resultado visible es correcto pero la justificación no lo es, deberá decirlo expresamente.


**39.** **Nivel D.** Audite la afirmación

$$
\frac{x+4}{x+7}=\frac47.
$$

Un estudiante dice que «se cancela la $x$ porque aparece arriba y abajo». Localice la primera ruptura, explique por qué $x$ no es un factor común de los dos miembros del cociente y use un valor permitido sencillo para refutar la igualdad propuesta. Indique también el dominio original y escriba qué puede afirmarse correctamente sobre la expresión.


**40.** **Nivel D.** Un estudiante transforma

$$
\frac{(x-2)(x+3)+5}{(x-2)(x+4)}
$$

mediante la cadena

$$
\frac{(x-2)(x+3)+5}{(x-2)(x+4)}
=
\frac{x+3+5}{x+4}.
$$

Afirma que canceló el factor $x-2$. Determine el dominio original, localice la primera transición inválida y explique por qué $x-2$ no es factor de **todo** el numerador. Dé un contraejemplo puntual permitido y describa qué factorización tendría que existir para que una cancelación semejante fuese legítima.


**41.** **Nivel D.** Examine la cadena

$$
\frac{x^2+3x}{x^2+5x}
=
\frac{x+3}{x+5}.
$$

El estudiante afirma que obtuvo el resultado «cancelando $x^2$». Decida por separado si **el resultado final** es correcto y si **la razón dada** lo justifica. Reconstruya una cadena válida mediante factorización, determine el dominio original y explique por qué un resultado correcto no convierte una regla falsa en una regla válida.


**42.** **Nivel D.** Considere

$$
\frac{(x-1)(x+2)+(x-1)}{(x-1)(x+5)}.
$$

Un estudiante escribe directamente

$$
\frac{(x-1)(x+2)+(x-1)}{(x-1)(x+5)}
=
\frac{x+3}{x+5}
$$

porque «canceló $x-1$ en cada término del numerador». La fórmula final es correcta en el dominio original. Decida si la explicación puede justificarse dividiendo todo el numerador y todo el denominador por el mismo factor no nulo y aplicando distributividad. Compare esa ruta con factorizar primero el numerador completo, reconstruya ambas cadenas y conserve todas las restricciones originales.


**43.** **Nivel D.** Audite

$$
\frac1{x-3}+\frac1{3-x}
=
\frac1{x-3}+\frac1{x-3}
=
\frac2{x-3}.
$$

Localice la primera ruptura y clasifíquela. Escriba la relación correcta entre $3-x$ y $x-3$, repare la cadena completa y conserve el dominio original. Explique por qué el error es de signo antes que de denominador común.


**44.** **Nivel D.** Un estudiante comienza correctamente con

$$
\frac{2x+1}{x+1}-\frac{x-3}{x-2}
=
\frac{(2x+1)(x-2)-(x-3)(x+1)}{(x+1)(x-2)}.
$$

Luego escribe

$$
\frac{(2x^2-3x-2)-(x^2-2x-3)}{(x+1)(x-2)}
=
\frac{2x^2-3x-2-x^2-2x-3}{(x+1)(x-2)}.
$$

Localice la primera transición errónea, explique qué términos deben cambiar de signo al retirar el segundo paréntesis, repare el numerador y dé la forma final con su dominio original.


**45.** **Nivel D.** Audite la cadena

$$
\frac1{x-1}+\frac1{x+1}
=
\frac2{(x-1)+(x+1)}
=
\frac1x.
$$

Indique la primera regla falsa que se ha usado. Determine el dominio original, obtenga la suma correcta mediante un denominador común y explique por qué la fórmula errónea $1/x$ introduce además una exclusión aparente que no pertenecía al problema inicial.


**46.** **Nivel D.** Considere

$$
\frac{x+1}{x-2}
\div
\frac{x-3}{x+4}
=
\frac{x+1}{x-2}
\cdot
\frac{x-3}{x+4}.
$$

Localice la primera ruptura, identifique qué objeto completo debía invertirse y determine todas las restricciones del cociente original antes de reparar la operación. Distinga expresamente entre el valor que hace al divisor indefinido y el valor que lo hace cero.


**47.** **Nivel D.** Un estudiante calcula

$$
\frac{x^2-16}{x-4}
=
\frac{(x-4)(x+4)}{x-4}
=
x+4
$$

sin error algebraico visible y concluye después que el dominio es $\mathbb R$ porque $x+4$ está definido para todo real. ¿Dónde aparece la primera ruptura? Clasifique el fallo, escriba la afirmación completa correcta y explique por qué la fórmula final no puede usarse para reconstruir el dominio de procedencia.


**48.** **Nivel D.** Se propone

$$
\frac{x-2}{x+1}
\div
\frac{x-2}{x-4}
=
\frac{x-4}{x+1},
\qquad x\neq-1,4.
$$

La simplificación visible coincide con la forma correcta, pero la lista de restricciones es incompleta. Identifique el valor omitido, explique por qué el divisor está definido allí pero no puede usarse como divisor, y clasifique el fallo antes de reparar la afirmación completa.


**49.** **Nivel D.** Para sumar

$$
\frac1{x-1}+\frac1{x+1},
$$

un estudiante decide usar el denominador común

$$
(x-1)(x+1)(x+5)
$$

y multiplica cada fracción por los factores necesarios, incluido $(x+5)/(x+5)$. Afirma después que su ruta es «más general» porque utiliza un denominador que contiene más factores. Determine el dominio original, localice la primera decisión que impide conservar la equivalencia sobre todo ese dominio y explique qué nueva exclusión se introduce. Repare la ruta con un denominador común adecuado.


**50.** **Nivel D.** Audite la siguiente solución completa:

$$
T(x)=
\frac{\dfrac{x^2-1}{x-1}}
     {\dfrac{x+1}{x+2}}.
$$

El estudiante escribe

$$
\operatorname{Dom}(T)=\mathbb R\setminus\{-2,-1\},
$$

porque el bloque inferior exige $x\neq-2$ y, al ser divisor, también $x\neq-1$. Luego continúa

$$
T(x)
=
\frac{x+1}{\dfrac{x+1}{x+2}}
=
(x+1)\frac{x+2}{x+1}
=
x+2,
$$

y concluye

$$
T(x)=x+2,
\qquad x\neq-2,-1.
$$

Localice la **primera ruptura** de la solución. Explique por qué los pasos algebraicos posteriores pueden ser correctos sobre un dominio más restringido y, sin embargo, no reparar la omisión inicial. Determine el dominio original completo y escriba la conclusión corregida.


## E. Estrategia y elección de ruta

En este bloque puede haber varias rutas algebraicamente correctas. La tarea consiste en **elegir con propósito**: preservar el dominio original, conservar visibles los factores útiles, evitar expansiones o denominadores auxiliares innecesarios y justificar por qué una representación es preferible para el objetivo concreto. Una ruta más larga no es falsa por ser larga; una ruta más corta no es válida por ser corta.


**51.** **Nivel E.** Para calcular

$$
\frac{2}{x(x-1)}+\frac{3}{(x-1)^2},
$$

considere los tres candidatos a denominador común

$$
D_1=x(x-1)^2,\qquad
D_2=x(x-1)^3,\qquad
D_3=x(x-1)^2(x+2).
$$

Determine primero el dominio original. Después clasifique cada candidato como **adecuado y económico**, **adecuado pero innecesariamente grande** o **inadecuado para conservar equivalencia en todo el dominio original**. Justifique la clasificación en términos de factores faltantes y ceros introducidos. Finalmente, ejecute la suma usando la opción que considere estratégicamente mejor.


**52.** **Nivel E.** Considere

$$
\frac{1}{(x+2)^2(x-3)}
-
\frac{4}{(x+2)(x-3)^2}.
$$

Compare las opciones

$$
D_1=(x+2)^2(x-3)^2,
$$

$$
D_2=(x+2)^3(x-3)^3,
$$

y

$$
D_3=(x+2)^2(x-3)^2(x-5).
$$

Determine el dominio original y explique, sin apelar a una teoría general de mcm polinómico, cuál es la potencia necesaria de cada factor. Distinga entre una elección válida pero costosa y una elección que introduce una restricción artificial. Use después el denominador que preserve mejor la estructura y efectúe la resta.


**53.** **Nivel E.** Simplifique

$$
S(x)=
\frac{1}{x(x-1)}
+
\frac{2}{x^2(x-1)}
-
\frac{3}{x(x-1)^2}.
$$

Antes de combinar numeradores:

1. determine el dominio original;
2. haga un inventario de los factores y sus mayores potencias necesarias;
3. proponga un denominador común que no repita factores innecesariamente;
4. explique qué tendría de estratégicamente peor multiplicar sin inspección los tres denominadores originales.

Ejecute después la ruta elegida y conserve el dominio de procedencia aunque la fórmula final admita más valores.


**54.** **Nivel E.** Para la fracción compleja

$$
F(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac1{x-1}-\dfrac1{x+1}},
$$

se proponen tres multiplicadores para eliminar denominadores internos:

$$
M_1=x^2-1,\qquad
M_2=(x^2-1)^2,\qquad
M_3=(x^2-1)(x-4).
$$

Determine primero el dominio original completo, incluido el control del denominador exterior. Analice luego los tres multiplicadores: indique cuáles son no nulos en todo el dominio original, cuál elimina los denominadores con menor coste y cuál reduce artificialmente el dominio. Ejecute la mejor ruta hasta obtener una forma simple.


**55.** **Nivel E.** Compare dos rutas para

$$
P(x)=
\frac{x^2-25}{x^2-2x-15}
\cdot
\frac{x-5}{x+5}.
$$

- **Ruta A:** registrar el dominio, factorizar y cancelar antes de multiplicar;
- **Ruta B:** multiplicar primero las formas expandidas y factorizar sólo si resulta necesario al final.

Desarrolle ambas hasta una forma comparable. Después explique cuál conserva mejor la estructura multiplicativa, cuál hace más visibles las restricciones y qué trabajo algebraico adicional crea la expansión prematura. No declare una ruta falsa sólo por ser menos eficiente.


**56.** **Nivel E.** Estudie

$$
Q(x)=
\frac{x^2-4}{x^2+x-6}
\div
\frac{x-2}{x+3}.
$$

Compare estas estrategias:

1. simplificar primero el bloque del dividendo **sin perder su dominio**, y sólo después ejecutar la división;
2. invertir de inmediato el divisor completo, factorizar todos los polinomios y simplificar el producto total.

Determine el dominio original antes de elegir. Ejecute las dos rutas, compruebe que conducen a la misma forma sobre ese dominio y explique cuál deja más transparente la razón de cada cancelación.


**57.** **Nivel E.** Considere

$$
H(x)=
\frac{\dfrac1x+\dfrac1{x+1}}
     {\dfrac1x-\dfrac1{x+1}}.
$$

Resuélvala por:

- el **método interior**;
- la **eliminación de denominadores internos** con un multiplicador común elegido por usted.

Antes de operar, determine un único dominio original. Compare después las dos rutas según cuatro criterios: número de fracciones intermedias, cantidad de distributividades, visibilidad del dominio y facilidad para detectar la cancelación final. Explique por qué el método más corto en este ejemplo no se convierte por ello en una regla universal.


**58.** **Nivel E.** Simplifique

$$
E(x)=
\left(
\frac{x^2-4}{x-2}
\div
\frac{x+2}{x+1}
\right)
+
\frac1{x+1}.
$$

Diseñe primero un **plan de bloques**: decida qué cociente conviene cerrar antes de construir un denominador común para toda la expresión. Compare su ruta con la alternativa de combinar desde el comienzo todas las fracciones visibles en una sola estructura. En ambas discusiones, registre por separado las restricciones que provienen del dividendo, del divisor y del último sumando. Termine con una forma simple y el dominio original completo.


**59.** **Nivel E.** Construya un producto de **dos expresiones racionales no constantes**, ambas con denominador no constante, que cumpla simultáneamente:

- su forma simplificada sea $x+2$;
- su dominio original sea exactamente
  $$
  \mathbb R\setminus\{-1,3\};
  $$
- las dos exclusiones dejen de ser visibles en la fórmula final;
- la simplificación requiera al menos una cancelación entre factores pertenecientes a fracciones distintas.

No basta con escribir un ejemplo: factorice su construcción, determine el dominio desde la expresión original y demuestre que satisface las cuatro condiciones.


**60.** **Nivel E.** Diseñe un **cociente de dos expresiones racionales** cuya forma simplificada sea la constante $1$ y cuyo dominio original sea exactamente

$$
\mathbb R\setminus\{-3,-2,1,4\}.
$$

Su construcción debe lograr además que:

- una exclusión proceda de un factor removible del denominador del **dividendo**;
- otra proceda de un factor removible del denominador del **divisor**;
- $x=1$ quede excluido porque el divisor completo vale cero;
- la forma final $1$ no muestre ninguna de las cuatro restricciones.

Puede partir de dos representaciones distintas de una misma expresión racional simple. Verifique por separado el dominio del dividendo, el dominio del divisor, los ceros del divisor y la simplificación del cociente. Explique por qué el diseño sería matemáticamente incompleto si sólo presentara la fórmula final.


## F. Transferencia C18–C19 y varias capas

Este bloque exige reutilizar conocimientos anteriores sin abrir teorías nuevas. En 61–64 los parámetros se consideran reales fijos mientras se opera respecto de $x$; se distinguen casos sólo cuando cambian el dominio o la estructura. En 65–68 se importan de C18 y C19 únicamente las reglas ya establecidas para raíces principales, factorización, diferencia de cuadrados y factores opuestos. En 69–72 aparecen cocientes de incrementos **puramente algebraicos**: $h$ es una variable o parámetro adicional sujeto a sus propias restricciones; no se estudian límites ni se hace tender $h$ a cero.


**61.** **Nivel F.** Sean $a,b\in\mathbb R$ parámetros fijos. Estudie

$$
F_{a,b}(x)=
\frac{3(x-a)}{(x-a)(x-b)}.
$$

Determine el dominio original y simplifique. Distinga los casos $a\neq b$ y $a=b$ **sólo para describir cuántos puntos distintos quedan excluidos**. Explique por qué la forma final puede ocultar $x=a$ cuando $a\neq b$ y por qué escribir dos condiciones simbólicas no implica siempre dos puntos excluidos.


**62.** **Nivel F.** Para parámetros reales fijos $a,b$, simplifique

$$
S_{a,b}(x)=
\frac1{x-a}
-
\frac1{x-b}.
$$

Obtenga una sola fracción y conserve el dominio original. Analice después qué cambia cuando $a=b$: compare la expresión original, la fórmula combinada y el conjunto de exclusiones. Justifique por qué el caso $a=b$ no debe tratarse como una excepción algebraica misteriosa, sino como una coincidencia de factores y restricciones.


**63.** **Nivel F.** Sean $a,b\in\mathbb R$. Lea por niveles y simplifique

$$
Q_{a,b}(x)=
\frac{\dfrac1{x-a}}
     {\dfrac{x-b}{x-a}}.
$$

Antes de invertir, determine qué valores hacen indefinidas las fracciones internas y cuál hace cero al divisor completo. Obtenga una forma simple y conserve el dominio de procedencia. Compare $a\neq b$ con $a=b$ y explique por qué, en este último caso, dos restricciones simbólicas pueden fusionarse en un único punto excluido.


**64.** **Nivel F.** Para $a,b\in\mathbb R$, considere

$$
P_{a,b}(x)=
\frac{(x-a)(x+a)}{x-b}
\cdot
\frac{x-b}{x-a}.
$$

Determine el dominio original antes de cancelar. Simplifique después y describa con precisión el dominio cuando $a\neq b$ y cuando $a=b$. Explique por qué la fórmula final puede ser polinómica aunque la expresión de partida conserve una o dos exclusiones según los valores de los parámetros.


**65.** **Nivel F.** Sea $a\in\mathbb R$ fijo. Usando únicamente las reglas de C18 para la raíz cuadrada principal y las reglas de C20 para denominadores, simplifique

$$
R_a(x)=
\frac{x-a}{\sqrt{x-a}}.
$$

Determine primero el dominio real de la expresión original. Justifique cada paso de la cancelación escribiendo $x-a$ como el cuadrado de una raíz principal cuando corresponda. Compare el dominio original con el dominio natural de la fórmula final y explique por qué no coinciden.


**66.** **Nivel F.** Audite la propuesta

$$
\frac{\sqrt{(x-a)^2}}{x-a}=1,
\qquad x\neq a.
$$

No haga análisis sistemático de signos. Use la identidad de C18

$$
\sqrt{u^2}=|u|
$$

para escribir la forma correcta, y utilice al menos un valor permitido —por ejemplo $x=a-1$— para refutar la identidad propuesta. Indique además por qué la expresión es fraccionaria pero no debe clasificarse automáticamente como racional.


**67.** **Nivel F.** Recupere de C19 la diferencia de cuadrados y la normalización de factores opuestos para simplificar

$$
A(x)=
\frac{x^2-16}{(4-x)(x+4)}.
$$

Determine primero el dominio original. Factorice el numerador, convierta $4-x$ en un múltiplo de $x-4$ y controle el signo global. Explique por qué el resultado final constante no permite recuperar las dos exclusiones originales.


**68.** **Nivel F.** Trabajando en $\mathbb R$, simplifique

$$
B(x)=
\frac{x-9}{\sqrt{x}-3}.
$$

Determine el dominio original combinando la condición de existencia de $\sqrt{x}$ con la no nulidad del denominador. Después use

$$
x-9=(\sqrt{x}-3)(\sqrt{x}+3)
$$

en el dominio donde esa escritura tiene sentido. Conserve la exclusión que desaparece de la fórmula final y explique por qué este ejercicio combina una regla de C18 con una factorización de tipo C19 sin convertir la expresión original en racional.


**69.** **Nivel F.** Simplifique algebraicamente, sin usar límites,

$$
D(x,h)=
\frac{\dfrac1{x+h}-\dfrac1x}{h}.
$$

Trabaje con pares reales $(x,h)$. Determine **antes de operar** todas las restricciones provenientes de los dos denominadores internos y de la división exterior por $h$. Obtenga una sola fracción y conserve las tres condiciones aunque la forma final oculte alguna de ellas.


**70.** **Nivel F.** Simplifique, sin interpretar el resultado como derivada ni tomar ningún límite,

$$
E(x,h)=
\frac{(x+h)^2-x^2}{h}.
$$

Registre primero la condición que impone la expresión original. Elija entre expandir todo desde el comienzo o usar una factorización estructural de la diferencia de cuadrados; compare brevemente ambas rutas y escriba la fórmula final junto con la restricción heredada.


**71.** **Nivel F.** Simplifique puramente por álgebra

$$
G(x,h)=
\frac{\dfrac1{(x+h)^2}-\dfrac1{x^2}}{h}.
$$

Determine el dominio original en el plano $(x,h)$: controle $x$, $x+h$ y $h$ por separado. Combine las fracciones internas, factorice el numerador resultante antes de cancelar y conserve todas las restricciones en la forma final.


**72.** **Nivel F.** Sea

$$
f(x)=\frac{x+1}{x-1}.
$$

Sin usar cálculo diferencial, simplifique el cociente de incremento algebraico

$$
C(x,h)=
\frac{f(x+h)-f(x)}{h}
=
\frac{
\dfrac{x+h+1}{x+h-1}
-
\dfrac{x+1}{x-1}
}{h}.
$$

Fije primero el dominio original en términos de $x$ y $h$. Mantenga los dos numeradores completos al construir el denominador común, simplifique sólo después de efectuar la resta y explique por qué las condiciones $x\neq1$, $x+h\neq1$ y $h\neq0$ deben acompañar a la forma final aunque ninguna de ellas pueda descartarse por mirar únicamente el último cociente.


## G. Síntesis avanzada

Los ocho ejercicios finales no anuncian una técnica principal. Cada problema exige leer la estructura completa, fijar el dominio de procedencia, escoger una ruta, justificar sus hipótesis y explicar qué información deja de ser visible en la forma final. No basta con obtener una fórmula correcta: debe quedar claro **por qué la cadena es válida sobre exactamente el dominio declarado**.


**73.** **Nivel G. Dominio invisible en el resultado.** Simplifique completamente

$$
E(x)=
\left(
\frac{x^2-1}{x-1}
\cdot
\frac{x-2}{x+1}
\right)
\div
\frac{x-2}{x+3}.
$$

La forma final debe ser polinómica. Antes de operar:

1. determine el dominio original y clasifique la causa de cada exclusión;
2. identifique qué restricciones proceden de denominadores internos y cuál procede de que el divisor completo valga cero;
3. elija una ruta que mantenga visibles los factores útiles hasta la última cancelación.

Después de simplificar, compare expresamente los puntos $x=1$ y $x=2$: en ambos la fórmula final tendrá sentido, pero las expresiones originales fallan por razones distintas. Explique por qué ese contraste impide reconstruir el dominio desde el resultado final.


**74.** **Nivel G. Auditoría de dos rutas.** Considere

$$
Q(x)=
\frac{x+3}{x-2}
\div
\frac{x^2-1}{x-1}.
$$

Un estudiante propone dos rutas.

**Ruta A.** Registra primero el dominio del cociente completo y sólo después factoriza el divisor.

**Ruta B.** Simplifica inmediatamente

$$
\frac{x^2-1}{x-1}=x+1
$$

y, mirando sólo esta última fórmula, declara como restricciones del divisor únicamente las que se ven en $x+1$.

Desarrolle ambas rutas. Determine cuál conserva el dominio original y localice con precisión la información que pierde la Ruta B. Muestre que sus manipulaciones algebraicas posteriores pueden ser correctas y, aun así, la afirmación completa quedar dañada. Termine con una forma simplificada común y compare los dominios que cada ruta declararía.


**75.** **Nivel G. Fracción compleja con parámetros.** Sean $a,b\in\mathbb R$ parámetros fijos. Estudie

$$
F_{a,b}(x)=
\frac{
\dfrac1{x-a}+\dfrac1{x-b}
}{
\dfrac1{x-a}-\dfrac1{x-b}
}.
$$

No convierta el problema en una ecuación. Debe:

1. determinar el dominio por niveles;
2. separar los casos $a\neq b$ y $a=b$ sólo cuando cambie realmente la estructura;
3. simplificar la fracción compleja en cada caso pertinente;
4. explicar qué ocurre con el denominador exterior cuando $a=b$;
5. distinguir entre «dos restricciones simbólicas» y «dos puntos distintos excluidos».

Su conclusión debe describir tanto la fórmula obtenida como el dominio en que esa fórmula representa a la expresión original.


**76.** **Nivel G. Construcción inversa.** Construya una expresión racional $R(x)$ que satisfaga simultáneamente:

- sea equivalente a $x^2+1$ sobre
  $$
  \mathbb R\setminus\{-2,3\};
  $$
- su dominio original sea **exactamente** ese conjunto;
- las dos exclusiones desaparezcan por completo de la fórmula simplificada;
- numerador y denominador de la expresión construida sean no constantes.

No basta con presentar una fórmula. Debe determinar su dominio directamente desde la expresión original, justificar cada cancelación y demostrar que no ha introducido ninguna exclusión adicional. Después explique por qué $R$ y la función polinómica natural $x\mapsto x^2+1$ no son la misma función si cada una conserva su dominio natural.


**77.** **Nivel G. Denominadores repetidos.** Simplifique

$$
S(x)=
\frac1{x(x-1)^2}
+
\frac2{x^2(x-1)}
-
\frac3{x(x-1)^3}.
$$

Compare dos planes:

- **Plan bruto:** usar el producto completo de los tres denominadores;
- **Plan estructural:** conservar de cada factor sólo la mayor potencia necesaria.

Antes de efectuar la suma, determine el dominio original y escriba ambos candidatos a denominador común. Justifique por qué los dos pueden ser válidos en el mismo dominio, pero uno introduce mucho más trabajo. Ejecute el plan estructural, obtenga una sola fracción y verifique por **recomposición** que cada una de las tres reescrituras individuales conserva su valor en el dominio declarado.


**78.** **Nivel G. Transferencia con radical e inversión.** Trabajando en $\mathbb R$, simplifique

$$
R(x)=
\frac{\sqrt{x-1}}{x-1}
\div
\frac{\sqrt{x-1}-2}{\sqrt{x-1}}.
$$

Separe rigurosamente las fuentes de restricción:

1. existencia de la raíz principal;
2. no nulidad de los denominadores internos;
3. no nulidad del divisor completo.

Sólo después invierta el divisor y simplifique. Compare el dominio original con el dominio natural de la fórmula final. Indique además por qué la expresión de partida es fraccionaria, pero no debe clasificarse como racional en el sentido de [§20.2](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s02).


**79.** **Nivel G. Primera ruptura en una cadena extensa.** Considere

$$
T(x)=
\left(
\frac{x^2-1}{x-1}
\div
\frac{x+1}{x+2}
\right)
\frac{x+2}{x+3}
-
\frac1{x+3}.
$$

Un estudiante escribe la siguiente cadena:

$$
\begin{aligned}
T(x)
&=
\left(
\frac{(x-1)(x+1)}{x-1}
\div
\frac{x+1}{x+2}
\right)
\frac{x+2}{x+3}
-
\frac1{x+3}\\
&=
\left(
(x+1)
\div
\frac{x+1}{x+2}
\right)
\frac{x+2}{x+3}
-
\frac1{x+3}\\
&=
(x+1)
\frac{x+1}{x+2}
\frac{x+2}{x+3}
-
\frac1{x+3}\\
&=
\frac{(x+1)^2(x+2)}{(x+2)(x+3)}
-
\frac1{x+3}\\
&=
\frac{(x+1)^2}{x+3}
-
\frac1{x+3}\\
&=
\frac{(x+1)^2-1}{x+3}\\
&=
\frac{x^2+2x+1-1}{x+3}\\
&=
\frac{x^2+2x}{x+3}\\
&=
\frac{x(x+2)}{x+3}.
\end{aligned}
$$

Audite la cadena de izquierda a derecha. Debe:

1. determinar primero el dominio de la expresión original;
2. localizar la **primera** transición injustificada;
3. explicar por qué varias transiciones posteriores son algebraicamente válidas respecto de la expresión equivocada que ya se obtuvo;
4. reparar la cadena desde la primera ruptura;
5. comparar el resultado correcto con el resultado de la cadena defectuosa.

No atribuya el error a una línea posterior si la equivalencia con la expresión original ya se había perdido antes.


**80.** **Nivel G. Síntesis sin método anunciado.** Simplifique y audite completamente

$$
S(x)=
\left(
\frac{x^2-9}{x^2-x-6}
\div
\frac{x+3}{x-2}
\right)
+
\frac4{x+2}.
$$

No se indica qué método usar. Su solución debe contener, en un orden que usted justifique:

- lectura por bloques y dominio por capas;
- factorización sólo donde revele información útil;
- control de que el divisor esté definido y sea no nulo;
- elección del orden entre simplificar el dividendo e invertir el divisor;
- construcción del denominador común para la suma final;
- conservación de todas las restricciones después de las cancelaciones;
- una **segunda ruta de verificación** que empiece invirtiendo el divisor antes de simplificar el primer cociente;
- explicación de qué información de dominio queda completamente oculta en la forma final.

Cierre indicando por qué una comprobación puntual puede servir como control adicional, pero no reemplaza la equivalencia algebraica demostrada sobre el dominio original.


## H. Profundización y reconstrucción

Intente cada tarea antes de consultar su solución. Los parámetros son reales salvo indicación distinta.



#### Ejercicio 081. Construcción mínima de dos huecos

Sean $a\ne b$. Entre las fracciones $N/D$ con denominador mónico y dominio exactamente $\mathbb R\setminus\{a,b\}$ que satisfacen la identidad formal $N=(x+1)D$, construya la de menor grado de denominador. Pruebe minimalidad y unicidad en ese grado.



#### Ejercicio 082. Hacer desaparecer una exclusión al invertir

Dados reales distintos $a,b$, diseñe una división entre fracciones que simplifique a $x-b$ y cuyo dominio excluya tanto $a$ como $b$.



#### Ejercicio 083. Dos rutas y una misma condición excepcional

Para $a,b\in\mathbb R$, simplifique $E=[1/(x-a)-1/(x-b)]\div[(a-b)/((x-a)(x-b))$. Compare simplificar primero con invertir primero y clasifique $a=b$.



#### Ejercicio 084. Comprobar una ruta radical por signos

Simplifique $\dfrac{\sqrt{x^2}}x\dfrac{x-a}{x-a}$ y compare una ruta por cancelación con otra por casos. Incluya todos los valores reales de $a$.



#### Ejercicio 085. Un denominador común que cambia con el parámetro

Estudie $F_t=1/[(x-t)(x-1)]+1/[(x+t)(x-1)]$. Dé un denominador común económico para $t\notin\{0,1,-1\}$ y para cada valor excepcional.



#### Ejercicio 086. Normalizar factores opuestos antes de sumar

Simplifique $G_t=1/(x-t)+1/(t-x)+1/(x+t)$ para todo $t\in\mathbb R$. Compare el dominio original y el natural de la forma final.



#### Ejercicio 087. Reparar una fracción compleja

Una resolución afirma $\dfrac{1/x+1/y}{1/x-1/y}=1$ «cancelando los términos $1/x$». Localice la ruptura, repare y certifique el dominio.



#### Ejercicio 088. Verificar una cadena por reconstrucción

Simplifique $H=\left[(x^2-a^2)/(x^2+ax)\right]\div[(x-a)/x]-a/x$ para todo $a\in\mathbb R$. Dé el dominio y un certificado inverso.

# Soluciones razonadas

Las soluciones conservan la función cognitiva del banco. En el bloque A la meta no es acelerar el cálculo, sino leer con precisión la estructura, el dominio y la afirmación matemática completa. Cuando una simplificación sirve para justificar una comparación, se usa sólo hasta el punto necesario y se conservan las restricciones de procedencia.

## A. Reconocimiento y lectura estructural


### Solución 1

(a) $\dfrac{3x-1}{x^2+4}$ está escrita como cociente, de modo que es **fraccionaria**. Numerador y denominador son polinomios, por lo que también es **racional**. No es una expresión polinómica: el denominador no es la constante $1$ ni desaparece mediante una cancelación algebraica.

(b) $\dfrac{\sqrt{x}+2}{x-5}$ es **fraccionaria**, porque presenta una división entre dos expresiones algebraicas. No es racional en el sentido de este capítulo, ya que $\sqrt{x}+2$ no es un polinomio. Tampoco es polinómica.

(c) $2x^4-x+7$ es **polinómica**. Todo polinomio es además una expresión racional, pues puede escribirse como

$$
2x^4-x+7=\frac{2x^4-x+7}{1}.
$$

No está presentada como una expresión fraccionaria visible.

(d) $\dfrac{x+1}{\sqrt{x^2+1}}$ es **fraccionaria**, pero no racional en esta forma porque el denominador contiene un radical y no es un polinomio. Tampoco es polinómica.

La clasificación depende de la estructura algebraica de la expresión, no de que algunos valores numéricos obtenidos sean racionales o irracionales.


### Solución 2

(a) $\dfrac{x^2-1}{x+3}$ tiene una barra de fracción visible y es **racional**, porque numerador y denominador son polinomios.

(b) $x+\dfrac1{x-2}$ contiene una fracción visible como subexpresión, pero la expresión completa está escrita como una suma, no como un único cociente. Sin embargo, pertenece a la clase racional porque puede escribirse, para $x\neq2$, como

$$
x+\frac1{x-2}
=
\frac{x(x-2)+1}{x-2}
=
\frac{x^2-2x+1}{x-2}.
$$

La clase racional no depende de que la barra exterior esté visible desde el comienzo.

(c) $\dfrac{\sqrt{x-1}}{x+4}$ tiene una barra de fracción visible, por lo que es fraccionaria. No es racional en esta forma porque el numerador contiene un radical y no es polinómico.

(d) $\dfrac{\dfrac{x+1}{x-2}}{\dfrac{x+3}{x+4}}$ posee una barra exterior y varias barras internas: es una fracción compleja y, por tanto, una expresión fraccionaria. Sus bloques internos son racionales y, sobre su dominio original, la expresión puede reducirse a un cociente de polinomios:

$$
\frac{x+1}{x-2}
\div
\frac{x+3}{x+4}
=
\frac{(x+1)(x+4)}{(x-2)(x+3)}.
$$

Por ello pertenece a la clase racional. Esta última fórmula no debe usarse para reconstruir el dominio original: el bloque divisor exigía además $x\neq-4$, aunque ese factor pase después al numerador.


### Solución 3

La barra exterior separa dos bloques completos. El **numerador exterior** es

$$
\frac2{x-1}+1,
$$

y el **denominador exterior** es

$$
\frac{x+3}{x-4}.
$$

Los denominadores internos visibles son $x-1$ y $x-4$. Por tanto, para que las subexpresiones existan necesitamos

$$
x\neq1,
\qquad
x\neq4.
$$

Pero el bloque inferior completo ocupa el lugar de divisor exterior. No basta con que esté definido: debe ser distinto de cero. Bajo $x\neq4$,

$$
\frac{x+3}{x-4}=0
$$

exactamente cuando $x=-3$. Así, también se requiere $x\neq-3$.

Por consiguiente,

$$
\boxed{
\operatorname{Dom}(T)=\mathbb R\setminus\{-3,1,4\}.
}
$$

Mirar sólo los denominadores pequeños detectaría $1$ y $4$, pero perdería $-3$, que aparece porque **la subexpresión completa** $(x+3)/(x-4)$ funciona como divisor.


### Solución 4

La expresión posee dos bloques principales: primero el producto

$$
P(x)=
\frac{x^2-9}{x^2-x-6}
\cdot
\frac{x-2}{x+3},
$$

y después la suma de $P(x)$ con $2/(x+2)$.

Conviene transformar **primero el bloque multiplicativo**. La finalidad es **revelar factores**, no expandir. En efecto,

$$
x^2-9=(x-3)(x+3),
\qquad
x^2-x-6=(x-3)(x+2).
$$

Estas factorizaciones muestran inmediatamente factores que pueden simplificarse dentro del producto sobre el dominio correspondiente. Además, anticipan que el bloque reducido conservará el factor $x+2$ en el denominador, precisamente el mismo denominador que aparece en el último sumando.

Una expansión total inmediata produciría polinomios de mayor grado y ocultaría los factores $x-3$ y $x+3$ que ya están preparados para simplificarse. Por eso la primera decisión estratégica es

$$
\boxed{\text{factorizar el bloque multiplicativo para revelar factores}.}
$$

No hay aquí un divisor que deba invertirse. El denominador común sólo será relevante **después** de reducir el producto, al abordar la suma final.


### Solución 5

La única fuente de restricciones es el denominador

$$
(x-2)^2(x+4).
$$

Para que el cociente esté definido necesitamos

$$
(x-2)^2(x+4)\neq0.
$$

Un producto es no nulo exactamente cuando ninguno de sus factores es cero. Por tanto,

$$
x-2\neq0
\qquad\text{y}\qquad
x+4\neq0,
$$

es decir,

$$
x\neq2,
\qquad
x\neq-4.
$$

La potencia $(x-2)^2$ no crea dos puntos excluidos: se anula en el mismo único valor que $x-2$, a saber, $x=2$. El numerador $x+1$ puede valer cero sin producir una división por cero; simplemente hace que toda la fracción valga $0$ cuando el denominador sigue siendo no nulo.

Así,

$$
\boxed{
\operatorname{Dom}(A)=\mathbb R\setminus\{-4,2\}.
}
$$


### Solución 6

Leemos la expresión por niveles, sin invertir todavía el divisor.

El bloque superior

$$
\frac1{x-2}
$$

exige $x\neq2$ porque su denominador interno no puede ser cero.

El bloque inferior

$$
\frac{x+1}{x+4}
$$

debe primero estar definido, lo que exige $x\neq-4$. Pero ese bloque completo es además el **denominador exterior**, de modo que también debe ser distinto de cero. Bajo $x\neq-4$, se anula exactamente cuando $x+1=0$, es decir, en $x=-1$.

Las tres exclusiones tienen, por tanto, procedencias distintas:

- $x=2$: denominador interno del numerador exterior;
- $x=-4$: denominador interno del divisor;
- $x=-1$: el divisor completo está definido, pero vale cero.

Así,

$$
\boxed{
\operatorname{Dom}(B)=\mathbb R\setminus\{-4,-1,2\}.
}
$$


### Solución 7

Para

$$
E(x)=\frac{x^2-25}{x-5},
$$

el denominador exige $x\neq5$. Por tanto,

$$
\operatorname{Dom}(E)=\mathbb R\setminus\{5\}.
$$

En cambio,

$$
F(x)=x+5
$$

es polinómica y está definida para todo real:

$$
\operatorname{Dom}(F)=\mathbb R.
$$

Como

$$
x^2-25=(x-5)(x+5),
$$

para $x\neq5$ podemos cancelar el factor no nulo $x-5$ y obtener

$$
E(x)=x+5=F(x).
$$

Así, $E$ y $F$ son equivalentes sobre

$$
\mathbb R\setminus\{5\}.
$$

Sin embargo, si cada fórmula define una función con su dominio natural y codominio $\mathbb R$, esas funciones **no son iguales**, porque sus dominios son distintos. El dato que impide identificarlas no es la regla de cálculo —que coincide donde ambas pueden compararse—, sino el **dominio**: $F(5)=10$, mientras que $E(5)$ no está definido.


### Solución 8

Factorizamos sólo para leer el dominio y comparar las fórmulas:

$$
x^2+x=x(x+1),
\qquad
x^2-1=(x-1)(x+1).
$$

Por tanto,

$$
\operatorname{Dom}(G)=\mathbb R\setminus\{-1,0\},
$$

mientras que

$$
\operatorname{Dom}(H)=\mathbb R\setminus\{0\}.
$$

Sobre el dominio de $G$, el factor $x+1$ es no nulo y puede cancelarse:

$$
G(x)
=
\frac{(x-1)(x+1)}{x(x+1)}
=
\frac{x-1}{x}
=
H(x).
$$

Así, ambas expresiones son equivalentes sobre

$$
\boxed{\mathbb R\setminus\{-1,0\}.}
$$

Las funciones naturales asociadas no son iguales porque sus dominios difieren. El valor $x=-1$ hace visible la diferencia: $G(-1)$ no existe, ya que el denominador original $x(x+1)$ vale cero; en cambio,

$$
H(-1)=\frac{-2}{-1}=2.
$$

Este único valor muestra que los dominios no coinciden. La equivalencia general, sin embargo, no se demuestra por esa comprobación puntual, sino por la factorización y cancelación válidas para todo $x\neq-1,0$.


### Solución 9

Antes de efectuar la división, registramos las condiciones de cada bloque.

El dividendo

$$
\frac{x+1}{x-3}
$$

exige

$$
x\neq3.
$$

El divisor

$$
\frac{x-2}{x+4}
$$

debe estar definido, de modo que

$$
x\neq-4.
$$

Además, como estamos dividiendo por ese cociente, debe ser distinto de cero. Bajo $x\neq-4$, se anula cuando $x-2=0$, es decir, en $x=2$. Por eso $x=2$ debe excluirse aunque no anule ningún denominador interno: hace cero al **divisor completo**.

En cambio, $x=-1$ anula el numerador del dividendo. Eso está permitido: cero dividido por una cantidad no nula sigue siendo cero. De hecho, en $x=-1$ el divisor vale

$$
\frac{-3}{3}=-1,
$$

por lo que no hay ninguna obstrucción.

Así,

$$
\boxed{
\operatorname{Dom}(Q)=\mathbb R\setminus\{-4,2,3\}.
}
$$


### Solución 10

El dividendo

$$
\frac{x+2}{x-1}
$$

no está definido en

$$
x=1.
$$

Ahora analizamos el divisor

$$
\frac{x^2-9}{x^2+x-6}.
$$

Factorizamos únicamente para hacer visibles sus ceros y sus posibles factores comunes:

$$
x^2-9=(x-3)(x+3),
$$

$$
x^2+x-6=(x+3)(x-2).
$$

El divisor no está definido cuando su denominador vale cero, es decir, en

$$
x=-3
\qquad\text{o}\qquad
x=2.
$$

Además, el divisor completo debe ser no nulo. En su dominio, el numerador se anula en $x=3$; el otro cero del numerador, $x=-3$, ya estaba fuera del dominio porque también anula el denominador. Por tanto, debemos excluir además

$$
x=3.
$$

El dominio original del cociente completo es

$$
\boxed{
\operatorname{Dom}(R)=\mathbb R\setminus\{-3,1,2,3\}.
}
$$

Los cuatro fenómenos pedidos quedan separados así:

1. **Dividendo indefinido:** $x=1$.
2. **Divisor indefinido:** $x=-3$ y $x=2$.
3. **Divisor definido pero igual a cero:** $x=3$.
4. **Factor que puede desaparecer al simplificar el divisor:** el factor $x+3$, porque

$$
\frac{(x-3)(x+3)}{(x+3)(x-2)}
=
\frac{x-3}{x-2}
$$

sólo bajo la restricción ya registrada $x\neq-3$.

Precisamente por eso una cancelación posterior no puede borrar una exclusión. La cancelación cambia la fórmula visible sobre el dominio permitido; no modifica retroactivamente los valores para los cuales la expresión original estaba indefinida o actuaba como divisor nulo.


## B. Fluidez técnica


### Solución 11

Antes de cancelar, determinamos el dominio original. El denominador factoriza como

$$
x^2-4=(x-2)(x+2),
$$

de modo que

$$
x\neq2,
\qquad
x\neq-2.
$$

El numerador también factoriza:

$$
x^2-5x+6=(x-2)(x-3).
$$

Por tanto,

$$
\frac{x^2-5x+6}{x^2-4}
=
\frac{(x-2)(x-3)}{(x-2)(x+2)}.
$$

Como el dominio original ya impone $x\neq2$, el factor $x-2$ es no nulo y puede cancelarse:

$$
\boxed{
\frac{x^2-5x+6}{x^2-4}
=
\frac{x-3}{x+2},
\qquad x\neq-2,2.
}
$$

La exclusión $x=2$ ya no aparece en la fórmula final, pero sigue perteneciendo al dominio de procedencia.


### Solución 12

Factorizamos numerador y denominador:

$$
x^2-6x+9=(x-3)^2,
$$

$$
x^2-x-6=(x-3)(x+2).
$$

El dominio original exige

$$
x\neq3,
\qquad
x\neq-2.
$$

En el numerador hay **dos copias** del factor $x-3$ y en el denominador hay **una copia**. Bajo $x\neq3$ podemos cancelar una sola copia:

$$
\frac{(x-3)^2}{(x-3)(x+2)}
=
\frac{x-3}{x+2}.
$$

Así,

$$
\boxed{
\frac{x^2-6x+9}{x^2-x-6}
=
\frac{x-3}{x+2},
\qquad x\neq-2,3.
}
$$

Una copia de $x-3$ permanece visible en el numerador; la exclusión $x=3$ permanece en el dominio aunque ya no sea una restricción natural de la fórmula final.


### Solución 13

El denominador original es $(x-5)(x-1)$, de modo que

$$
x\neq5,
\qquad
x\neq1.
$$

Los factores $5-x$ y $x-5$ son opuestos:

$$
5-x=-(x-5).
$$

Por tanto,

$$
\frac{(5-x)(x+2)}{(x-5)(x-1)}
=
-\frac{(x-5)(x+2)}{(x-5)(x-1)}.
$$

Como $x\neq5$, podemos cancelar el factor no nulo $x-5$:

$$
\boxed{
\frac{(5-x)(x+2)}{(x-5)(x-1)}
=
-\frac{x+2}{x-1},
\qquad x\neq1,5.
}
$$

El signo negativo es indispensable: los factores opuestos no son iguales, sino que difieren exactamente por un factor $-1$.


### Solución 14

Factorizamos el denominador para leer el dominio:

$$
x^2-16=(x-4)(x+4),
$$

por lo que

$$
x\neq4,
\qquad
x\neq-4.
$$

En el numerador extraemos el factor común $x^2$:

$$
x^3-4x^2=x^2(x-4).
$$

Así,

$$
\frac{x^3-4x^2}{x^2-16}
=
\frac{x^2(x-4)}{(x-4)(x+4)}.
$$

Como $x\neq4$, cancelamos $x-4$ y obtenemos

$$
\boxed{
\frac{x^3-4x^2}{x^2-16}
=
\frac{x^2}{x+4},
\qquad x\neq-4,4.
}
$$

La restricción que desaparece de la escritura es $x\neq4$. No expandimos la forma final porque la forma factorizada ya muestra con claridad el denominador restante.


### Solución 15

Leemos primero el dominio de cada factor. Como

$$
x^2+5x+6=(x+2)(x+3),
$$

la primera fracción exige

$$
x\neq-2,-3.
$$

La segunda fracción exige

$$
x\neq2.
$$

Por tanto, el producto original está definido en

$$
\mathbb R\setminus\{-3,-2,2\}.
$$

Factorizamos también

$$
x^2-4=(x-2)(x+2).
$$

Entonces

$$
\frac{x^2-4}{x^2+5x+6}
\cdot
\frac{x+3}{x-2}
=
\frac{(x-2)(x+2)}{(x+2)(x+3)}
\cdot
\frac{x+3}{x-2}.
$$

En el dominio original, los factores $x-2$, $x+2$ y $x+3$ son todos no nulos, de modo que pueden cancelarse. Queda

$$
\boxed{
1,
\qquad x\neq-3,-2,2.
}
$$

La constante $1$ tiene dominio natural $\mathbb R$, pero el producto original no estaba definido en los tres puntos excluidos.


### Solución 16

El primer factor exige

$$
x\neq-2,
\qquad
x\neq3,
$$

y el segundo exige

$$
x\neq1.
$$

Así, el dominio original es

$$
\mathbb R\setminus\{-2,1,3\}.
$$

Sin multiplicar los polinomios, observamos los factores comunes:

$$
\frac{(x-1)^2}{(x+2)(x-3)}
\cdot
\frac{x+2}{x-1}.
$$

Como $x\neq-2$ y $x\neq1$, podemos cancelar una copia de $x+2$ y una copia de $x-1$. Resulta

$$
\boxed{
\frac{x-1}{x-3},
\qquad x\neq-2,1,3.
}
$$

La exclusión $x=-2$ deja de ser visible en la fórmula final y $x=1$ tampoco aparece como cero del denominador final, pero ambas restricciones proceden del producto original.


### Solución 17

El dividendo

$$
\frac{x^2-9}{x+4}
$$

exige

$$
x\neq-4.
$$

El divisor

$$
\frac{x-3}{x+2}
$$

debe estar definido, así que

$$
x\neq-2.
$$

Además, el divisor debe ser distinto de cero. Bajo $x\neq-2$, se anula cuando $x-3=0$, por lo que también

$$
x\neq3.
$$

El dominio original es entonces

$$
\mathbb R\setminus\{-4,-2,3\}.
$$

Sólo ahora invertimos el divisor completo:

$$
\frac{x^2-9}{x+4}
\div
\frac{x-3}{x+2}
=
\frac{x^2-9}{x+4}
\cdot
\frac{x+2}{x-3}.
$$

Factorizamos $x^2-9=(x-3)(x+3)$ y, como $x\neq3$, cancelamos $x-3$:

$$
\boxed{
\frac{(x+3)(x+2)}{x+4},
\qquad x\neq-4,-2,3.
}
$$

Las tres exclusiones tienen procedencias distintas: $-4$ viene del dividendo, $-2$ de la definición del divisor y $3$ de la obligación adicional de que el divisor no sea cero.


### Solución 18

El dividendo

$$
\frac{x-1}{x+2}
$$

exige

$$
x\neq-2.
$$

Antes de simplificar el divisor,

$$
\frac{x^2-1}{x-1},
$$

registramos su dominio: exige

$$
x\neq1.
$$

Además, como ese cociente funciona como divisor, debe ser distinto de cero. Factorizamos

$$
x^2-1=(x-1)(x+1).
$$

En el dominio $x\neq1$, el divisor se anula cuando $x+1=0$, es decir, en

$$
x=-1.
$$

Por tanto,

$$
\operatorname{Dom}
=
\mathbb R\setminus\{-2,-1,1\}.
$$

Invertimos el divisor completo:

$$
\frac{x-1}{x+2}
\div
\frac{x^2-1}{x-1}
=
\frac{x-1}{x+2}
\cdot
\frac{x-1}{x^2-1}.
$$

Sustituyendo $x^2-1=(x-1)(x+1)$ y cancelando una copia de $x-1$, autorizada porque $x\neq1$,

$$
\boxed{
\frac{x-1}{(x+2)(x+1)},
\qquad x\neq-2,-1,1.
}
$$

La restricción $x=1$ permanece aunque el factor correspondiente se haya cancelado.


### Solución 19

Las dos fracciones tienen el mismo denominador, que exige

$$
x\neq2.
$$

Por tanto combinamos únicamente los numeradores:

$$
\frac{3x+1}{x-2}
+
\frac{x-5}{x-2}
=
\frac{(3x+1)+(x-5)}{x-2}.
$$

Simplificando el numerador,

$$
(3x+1)+(x-5)=4x-4=4(x-1).
$$

Así,

$$
\boxed{
\frac{4(x-1)}{x-2},
\qquad x\neq2.
}
$$

No existe factor común entre $x-1$ y $x-2$, de modo que no hay cancelación adicional.


### Solución 20

El dominio original exige

$$
x\neq0,
\qquad
x\neq1.
$$

El denominador $x(x-1)$ de la primera fracción ya contiene al denominador $x-1$ de la segunda. Por eso usamos el denominador común económico $x(x-1)$:

$$
\frac{3}{x-1}
=
\frac{3x}{x(x-1)},
$$

válidamente porque $x\neq0$ en el dominio original.

Entonces

$$
\frac{2}{x(x-1)}
+
\frac{3}{x-1}
=
\frac{2+3x}{x(x-1)}.
$$

No aparece ningún factor cancelable, de modo que

$$
\boxed{
\frac{3x+2}{x(x-1)},
\qquad x\neq0,1.
}
$$

No era necesario multiplicar los denominadores completos y producir una copia adicional de $x-1$.


### Solución 21

El dominio original es

$$
\mathbb R\setminus\{-1,2\}.
$$

Usamos el denominador común $(x+1)(x-2)$:

$$
\frac{2x+3}{x+1}
-
\frac{x-4}{x-2}
=
\frac{(2x+3)(x-2)-(x-4)(x+1)}
     {(x+1)(x-2)}.
$$

Conservamos el segundo numerador entre paréntesis hasta completar la resta. Calculamos

$$
(2x+3)(x-2)=2x^2-x-6,
$$

$$
(x-4)(x+1)=x^2-3x-4.
$$

Por tanto,

$$
\begin{aligned}
(2x+3)(x-2)-(x-4)(x+1)
&=(2x^2-x-6)-(x^2-3x-4)\\
&=x^2+2x-2.
\end{aligned}
$$

Así,

$$
\boxed{
\frac{x^2+2x-2}{(x+1)(x-2)},
\qquad x\neq-1,2.
}
$$

El numerador no contiene ninguno de los factores lineales del denominador, por lo que no hay una cancelación legítima. La forma factorizada del denominador conserva visibles las restricciones.


### Solución 22

El dominio original exige

$$
x\neq0,
\qquad
x\neq-1.
$$

Usamos el denominador común indicado, $x(x+1)$:

$$
\frac1x
+
\frac2{x+1}
-
\frac1{x(x+1)}
=
\frac{x+1}{x(x+1)}
+
\frac{2x}{x(x+1)}
-
\frac1{x(x+1)}.
$$

Combinamos los numeradores:

$$
(x+1)+2x-1=3x.
$$

Entonces

$$
\frac{3x}{x(x+1)}.
$$

Como $x\neq0$, el factor $x$ puede cancelarse:

$$
\boxed{
\frac3{x+1},
\qquad x\neq-1,0.
}
$$

La exclusión $x=0$ desaparece de la fórmula visible, pero pertenece al dominio original.


### Solución 23

La fracción interna $1/x$ exige

$$
x\neq0.
$$

El denominador exterior completo es

$$
\frac1x+1
=
\frac{x+1}{x},
$$

que, además de estar definido, debe ser distinto de cero. Por tanto,

$$
x\neq-1.
$$

Así,

$$
\operatorname{Dom}
=
\mathbb R\setminus\{-1,0\}.
$$

Aplicamos el método interior. El numerador exterior se reduce a

$$
\frac1x+3
=
\frac{1+3x}{x},
$$

y el denominador exterior a

$$
\frac1x+1
=
\frac{x+1}{x}.
$$

Por tanto,

$$
\frac{\dfrac{1+3x}{x}}
     {\dfrac{x+1}{x}}
=
\frac{1+3x}{x}
\cdot
\frac{x}{x+1}.
$$

Como $x\neq0$, cancelamos $x$ y obtenemos

$$
\boxed{
\frac{3x+1}{x+1},
\qquad x\neq-1,0.
}
$$

La fórmula final ya no muestra la exclusión $x=0$, que procede de las fracciones internas.


### Solución 24

Las fracciones internas exigen

$$
x\neq2,
\qquad
x\neq-2.
$$

Reducimos el denominador exterior:

$$
\frac1{x-2}+\frac1{x+2}
=
\frac{(x+2)+(x-2)}{(x-2)(x+2)}
=
\frac{2x}{x^2-4}.
$$

En el dominio donde está definido, este bloque vale cero cuando $x=0$. Como ocupa el lugar de divisor exterior, debemos excluir también

$$
x\neq0.
$$

Así,

$$
\operatorname{Dom}
=
\mathbb R\setminus\{-2,0,2\}.
$$

El numerador exterior es

$$
\frac1{x-2}-\frac1{x+2}
=
\frac{(x+2)-(x-2)}{x^2-4}
=
\frac4{x^2-4}.
$$

Entonces

$$
\frac{\dfrac4{x^2-4}}
     {\dfrac{2x}{x^2-4}}
=
\frac4{x^2-4}
\cdot
\frac{x^2-4}{2x}.
$$

Como $x\neq\pm2$, cancelamos $x^2-4$ y simplificamos el factor numérico:

$$
\boxed{
\frac2x,
\qquad x\neq-2,0,2.
}
$$

La exclusión adicional $x=0$ no procede de un denominador interno: aparece porque el bloque inferior completo se anula allí.


### Solución 25

La fracción interna exige

$$
x\neq-1.
$$

El denominador exterior completo es

$$
\frac{x-2}{x+1}+1
=
\frac{x-2+x+1}{x+1}
=
\frac{2x-1}{x+1}.
$$

Como ese bloque funciona como divisor, debe ser distinto de cero. Por tanto,

$$
2x-1\neq0,
$$

es decir,

$$
x\neq\frac12.
$$

El dominio original es

$$
\mathbb R\setminus\left\{-1,\frac12\right\}.
$$

Elegimos como multiplicador común

$$
M(x)=x+1.
$$

Es una elección legítima porque $x+1\neq0$ en todo el dominio original. Multiplicamos el numerador y el denominador exteriores por $x+1$:

$$
\frac{(x+1)\left(\dfrac2{x+1}\right)}
     {(x+1)\left(\dfrac{x-2}{x+1}+1\right)}.
$$

Distribuyendo en el bloque inferior,

$$
(x+1)\left(\frac{x-2}{x+1}+1\right)
=
(x-2)+(x+1)
=
2x-1.
$$

Así,

$$
\boxed{
\frac2{2x-1},
\qquad
x\neq-1,\frac12.
}
$$

La forma final sólo hace visible $x\neq1/2$; la exclusión $x=-1$ debe conservarse porque pertenecía a la expresión original.


### Solución 26

Los denominadores internos $x-1$, $x+1$ y $x^2-1$ exigen

$$
x\neq1,
\qquad
x\neq-1.
$$

El denominador exterior es

$$
\frac3{x^2-1}.
$$

En su dominio nunca vale cero, porque su numerador es la constante no nula $3$. Por tanto, no añade ninguna exclusión nueva.

Reducimos el numerador exterior:

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{(x+1)+(x-1)}{x^2-1}
=
\frac{2x}{x^2-1}.
$$

Entonces

$$
\frac{\dfrac{2x}{x^2-1}}
     {\dfrac3{x^2-1}}
=
\frac{2x}{x^2-1}
\cdot
\frac{x^2-1}{3}.
$$

Como $x\neq\pm1$, el factor $x^2-1$ es no nulo y puede cancelarse:

$$
\boxed{
\frac{2x}{3},
\qquad x\neq-1,1.
}
$$

La fórmula final es polinómica salvo por el factor constante $1/3$, pero conserva las dos exclusiones heredadas de las fracciones internas.


## C. Justificación y reconstrucción


### Solución 27

La expresión original

$$
\frac{AC}{BC}
$$

está definida cuando $BC\neq0$. En los números reales esto equivale a exigir simultáneamente

$$
B\neq0
\qquad\text{y}\qquad
C\neq0.
$$

Bajo esas hipótesis, $C$ posee inverso multiplicativo y podemos dividir numerador y denominador por el mismo factor no nulo:

$$
\frac{AC}{BC}
=
\frac{AC/C}{BC/C}
=
\frac{A}{B}.
$$

Ésta es la justificación de la llamada cancelación: no se tachan símbolos, sino que se divide arriba y abajo por una misma cantidad que sabemos no nula.

Si $C=0$, el cociente original tendría denominador $BC=0$ y ni siquiera estaría definido. Además, el paso $AC/C$ exigiría dividir por cero. Por eso la condición $C\neq0$ no es opcional ni puede recuperarse después de simplificar.

En resumen,

$$
\boxed{
\frac{AC}{BC}=\frac AB
\quad\text{si }B\neq0\text{ y }C\neq0.
}
$$

La equivalencia debe leerse precisamente sobre el dominio en el que esas hipótesis se cumplen.


### Solución 28

Partimos de

$$
\frac AB\div\frac CD.
$$

Hay tres obligaciones distintas.

Primero, el dividendo $A/B$ debe estar definido:

$$
B\neq0.
$$

Segundo, el divisor $C/D$ debe estar definido:

$$
D\neq0.
$$

Tercero, no basta con que el divisor exista: como estamos dividiendo por él, también debe ser distinto de cero. Bajo $D\neq0$,

$$
\frac CD=0
$$

si y sólo si $C=0$. Por tanto necesitamos

$$
C\neq0.
$$

Con $C\neq0$ y $D\neq0$, el recíproco de $C/D$ es $D/C$, así que

$$
\frac AB\div\frac CD
=
\frac AB\cdot\frac DC
=
\frac{AD}{BC}.
$$

La regla completa es

$$
\boxed{
\frac AB\div\frac CD
=
\frac{AD}{BC},
\qquad
B\neq0,\ C\neq0,\ D\neq0.
}
$$

No necesitamos imponer $A\neq0$: el dividendo puede valer cero. Si $A=0$ y el divisor es no nulo, la división está perfectamente definida y su resultado es $0$.


### Solución 29

Suponemos

$$
B\neq0
\qquad\text{y}\qquad
D\neq0.
$$

Para la primera fracción multiplicamos numerador y denominador por $D$:

$$
\frac AB
=
\frac AB\cdot\frac DD
=
\frac{AD}{BD}.
$$

Esta transformación está autorizada porque $D\neq0$, de modo que $D/D=1$.

Para la segunda fracción multiplicamos numerador y denominador por $B$:

$$
\frac CD
=
\frac CD\cdot\frac BB
=
\frac{BC}{BD},
$$

y aquí la hipótesis $B\neq0$ garantiza que $B/B=1$.

Por tanto, ambas fracciones pueden escribirse con denominador $BD$. Eso demuestra que $BD$ es siempre un denominador común disponible cuando $B$ y $D$ son no nulos.

Sin embargo, **disponible** no significa **económico**. Si $B$ y $D$ comparten factores, el producto $BD$ puede repetirlos innecesariamente. Por ejemplo, si $B=x(x+1)$ y $D=(x+1)(x-2)$, el producto bruto contiene $(x+1)^2$, aunque una sola copia de $x+1$ basta. La validez depende de las hipótesis de no nulidad; la economía depende de la estructura factorizada.


### Solución 30

Sea

$$
F(x)=\frac{N(x)}{D(x)}
$$

una fracción compleja definida en un dominio $E$. En particular, para todo $x\in E$ debemos tener $D(x)\neq0$.

Queremos sustituirla por

$$
\frac{M(x)N(x)}{M(x)D(x)}.
$$

Para que esta nueva escritura conserve exactamente el valor de $F$ en todo $E$, necesitamos

$$
M(x)\neq0
\qquad\text{para todo }x\in E.
$$

Bajo esa condición,

$$
\frac{M(x)N(x)}{M(x)D(x)}
=
\frac{N(x)}{D(x)},
$$

porque podemos dividir numerador y denominador por el factor común no nulo $M(x)$. Es exactamente la regla de [§20.5](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s05) aplicada al factor $M(x)$.

Si existe $x_0\in E$ tal que $M(x_0)=0$, la fracción original sigue estando definida en $x_0$, pero la nueva escritura tiene denominador

$$
M(x_0)D(x_0)=0.
$$

La ruta deja entonces de ser válida en ese punto. No hemos encontrado una equivalencia sobre todo $E$, sino sólo sobre el subconjunto

$$
\{x\in E:M(x)\neq0\}.
$$

Por eso un factor auxiliar que se anula dentro del dominio original **reduce artificialmente el dominio de la transformación**, aunque después pueda cancelarse de la fórmula final.


### Solución 31

Consideramos

$$
R(x)=\frac{x^2-9}{x^2-x-6}.
$$

Primero determinamos el dominio original. Factorizamos el denominador:

$$
x^2-x-6=(x-3)(x+2).
$$

Por tanto,

$$
\operatorname{Dom}(R)
=
\mathbb R\setminus\{-2,3\}.
$$

Ahora factorizamos también el numerador:

$$
x^2-9=(x-3)(x+3).
$$

Sobre el dominio original, $x-3\neq0$, así que

$$
R(x)
=
\frac{(x-3)(x+3)}{(x-3)(x+2)}
=
\frac{x+3}{x+2}.
$$

La respuesta completa es

$$
\boxed{
R(x)=\frac{x+3}{x+2},
\qquad x\neq-2,3.
}
$$

(i) La restricción que deja de ser visible es $x\neq3$.

(ii) El dominio natural de la fórmula final $(x+3)/(x+2)$ es

$$
\mathbb R\setminus\{-2\}.
$$

(iii) La equivalencia obtenida es correcta sobre el dominio original,

$$
\mathbb R\setminus\{-2,3\}.
$$

Los tres datos no son redundantes: la fórmula final informa de los valores; su dominio natural informa dónde esa nueva fórmula existe por sí sola; y el dominio de procedencia indica dónde hemos demostrado que representa a la expresión original.


### Solución 32

Sea

$$
P(x)=
\frac{x^2-1}{x^2+3x+2}
\cdot
\frac{x+2}{x-1}.
$$

Antes de simplificar, factorizamos sólo para leer el dominio:

$$
x^2+3x+2=(x+1)(x+2).
$$

El primer factor exige

$$
x\neq-1,-2,
$$

y el segundo exige

$$
x\neq1.
$$

Por tanto,

$$
\operatorname{Dom}(P)
=
\mathbb R\setminus\{-2,-1,1\}.
$$

Además,

$$
x^2-1=(x-1)(x+1),
$$

de modo que, en el dominio original,

$$
P(x)
=
\frac{(x-1)(x+1)}{(x+1)(x+2)}
\cdot
\frac{x+2}{x-1}.
$$

Los tres factores $x-1$, $x+1$ y $x+2$ son no nulos allí, así que se cancelan y obtenemos

$$
\boxed{
P(x)=1,
\qquad x\neq-2,-1,1.
}
$$

La constante $1$ tiene dominio natural $\mathbb R$. Sin embargo, afirmar $P(x)=1$ para todo real sería falso como afirmación sobre la expresión original, porque $P$ no existe en $x=-2,-1,1$. La simplificación conserva valores sobre el dominio de procedencia; no convierte esos puntos excluidos en puntos admisibles.


### Solución 33

Estudiamos

$$
\frac1{x-1}-\frac2{x^2-1}.
$$

El dominio original se obtiene de

$$
x-1\neq0
$$

y

$$
x^2-1=(x-1)(x+1)\neq0.
$$

Así,

$$
x\neq1,
\qquad
x\neq-1.
$$

El denominador común económico es

$$
(x-1)(x+1).
$$

Reescribimos la primera fracción:

$$
\frac1{x-1}
=
\frac{x+1}{(x-1)(x+1)}.
$$

Entonces

$$
\frac1{x-1}-\frac2{x^2-1}
=
\frac{(x+1)-2}{(x-1)(x+1)}
=
\frac{x-1}{(x-1)(x+1)}.
$$

**Éste es el momento exacto** en que aparece un factor cancelable: sólo después de combinar los numeradores. Como $x\neq1$ pertenece al dominio original, podemos cancelar $x-1$:

$$
\boxed{
\frac1{x-1}-\frac2{x^2-1}
=
\frac1{x+1},
\qquad
x\neq-1,1.
}
$$

La fórmula final $1/(x+1)$ tiene dominio natural $\mathbb R\setminus\{-1\}$, pero la equivalencia demostrada conserva también $x\neq1$. Por eso no debe presentarse como identidad sobre todo el dominio natural de la fórmula final.


### Solución 34

Consideramos

$$
H(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac2{x^2-1}}.
$$

Leemos el dominio por niveles. Las fracciones internas exigen

$$
x\neq1,
\qquad
x\neq-1.
$$

El denominador exterior completo es

$$
\frac2{x^2-1}.
$$

En los puntos donde está definido nunca vale cero, porque su numerador es la constante no nula $2$. Por tanto, no añade una exclusión nueva y

$$
\operatorname{Dom}(H)
=
\mathbb R\setminus\{-1,1\}.
$$

Reducimos el numerador exterior:

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{(x+1)+(x-1)}{x^2-1}
=
\frac{2x}{x^2-1}.
$$

Así,

$$
H(x)
=
\frac{\dfrac{2x}{x^2-1}}
     {\dfrac2{x^2-1}}
=
\frac{2x}{x^2-1}
\cdot
\frac{x^2-1}{2}.
$$

Como $x^2-1\neq0$ en el dominio original, cancelamos y obtenemos

$$
\boxed{
H(x)=x,
\qquad x\neq-1,1.
}
$$

La fórmula final es polinómica y tiene dominio natural $\mathbb R$, pero eso no altera el dominio de procedencia. La forma correcta de conservar la equivalencia es escribir la fórmula $x$ acompañada de las restricciones $x\neq-1,1$.


### Solución 35

Sea

$$
F(x)=
\frac{\dfrac1x+1}
     {\dfrac1x-1}.
$$

Primero fijamos un único dominio para ambas rutas. Las fracciones internas exigen $x\neq0$. Además, el denominador exterior completo

$$
\frac1x-1
=
\frac{1-x}{x}
$$

debe ser no nulo, así que $x\neq1$. Por tanto,

$$
\operatorname{Dom}(F)
=
\mathbb R\setminus\{0,1\}.
$$

**Ruta 1: método interior.**

Reducimos los dos bloques:

$$
\frac1x+1=\frac{x+1}{x},
\qquad
\frac1x-1=\frac{1-x}{x}.
$$

Luego

$$
F(x)
=
\frac{\dfrac{x+1}{x}}
     {\dfrac{1-x}{x}}
=
\frac{x+1}{x}\cdot\frac{x}{1-x}
=
\frac{x+1}{1-x},
$$

porque $x\neq0$.

**Ruta 2: eliminación de denominadores internos.**

Elegimos

$$
M(x)=x.
$$

Es válido porque $x\neq0$ en todo el dominio original. Multiplicamos ambos bloques exteriores por $x$:

$$
F(x)
=
\frac{x\left(\dfrac1x+1\right)}
     {x\left(\dfrac1x-1\right)}
=
\frac{x+1}{1-x}.
$$

Así, en ambos casos,

$$
\boxed{
F(x)=\frac{x+1}{1-x},
\qquad x\neq0,1.
}
$$

El método interior introduce dos fracciones intermedias simples y hace muy visible la división exterior. El segundo método elimina de una vez los denominadores internos y usa menos reescrituras en este ejemplo. Ninguno cambia el dominio: si ambas rutas están bien justificadas, deben conservar los mismos valores sobre el mismo conjunto $\mathbb R\setminus\{0,1\}$.


### Solución 36

La expresión

$$
\frac1{x-1}+\frac1{x+1}
$$

está definida cuando

$$
x\neq1,
\qquad
x\neq-1.
$$

Por tanto, su dominio original es

$$
D=\mathbb R\setminus\{-1,1\}.
$$

La propuesta económica usa

$$
(x-1)(x+1).
$$

En $D$, ambos factores son no nulos. Reescribimos:

$$
\frac1{x-1}
=
\frac{x+1}{(x-1)(x+1)}
$$

y

$$
\frac1{x+1}
=
\frac{x-1}{(x-1)(x+1)}.
$$

Así,

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{2x}{x^2-1},
\qquad x\neq-1,1.
$$

La primera propuesta añade el factor $x+5$ y usa el denominador

$$
(x-1)(x+1)(x+5).
$$

Para construirlo habría que multiplicar por expresiones que contienen

$$
\frac{x+5}{x+5},
$$

lo que exige $x\neq-5$. Pero $-5\in D$. La ruta queda entonces justificada sólo en

$$
D\setminus\{-5\}
=
\mathbb R\setminus\{-5,-1,1\}.
$$

Dentro de ese dominio menor el álgebra puede ser correcta y, después de combinar, incluso puede cancelarse $x+5$. Sin embargo, la ruta no constituye una equivalencia sobre todo el dominio original, porque perdió artificialmente el punto $x=-5$.

El factor responsable es exactamente **$x+5$**.


### Solución 37

Sea

$$
P(x)=
\frac{x^2-9}{x^2-x-6}
\cdot
\frac{x-2}{x+3}.
$$

El dominio original se obtiene de

$$
x^2-x-6=(x-3)(x+2)
$$

y del segundo denominador $x+3$. Así,

$$
\operatorname{Dom}(P)
=
\mathbb R\setminus\{-3,-2,3\}.
$$

**Ruta I: factorizar antes de multiplicar.**

Como

$$
x^2-9=(x-3)(x+3),
$$

tenemos

$$
P(x)
=
\frac{(x-3)(x+3)}{(x-3)(x+2)}
\cdot
\frac{x-2}{x+3}.
$$

En el dominio original, $x-3$ y $x+3$ son no nulos. Cancelamos y obtenemos

$$
\boxed{
P(x)=\frac{x-2}{x+2},
\qquad x\neq-3,-2,3.
}
$$

**Ruta II: multiplicar primero las formas expandidas.**

Podemos escribir

$$
P(x)
=
\frac{x^3-2x^2-9x+18}
     {x^3+2x^2-9x-18}.
$$

Esta igualdad sigue siendo correcta sobre el mismo dominio original. Para simplificar debemos volver a factorizar:

$$
x^3-2x^2-9x+18
=
(x-3)(x+3)(x-2),
$$

$$
x^3+2x^2-9x-18
=
(x-3)(x+3)(x+2).
$$

Entonces recuperamos nuevamente $(x-2)/(x+2)$ sobre el mismo dominio.

Las dos rutas pueden ser correctas, pero la Ruta I es estratégicamente superior aquí: mantiene visibles desde el comienzo los factores $x-3$, $x+3$ y $x+2$, permite cancelar antes de crear polinomios cúbicos y hace más fácil recordar qué ceros pertenecían a denominadores originales. La Ruta II destruye temporalmente esa información y obliga a refactorizar lo que acabamos de expandir.


### Solución 38

Consideramos

$$
G(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac1{x-1}-\dfrac1{x+1}}.
$$

Las fracciones internas exigen

$$
x\neq1,
\qquad
x\neq-1.
$$

Además, el denominador exterior completo debe ser distinto de cero. Lo reducimos:

$$
\frac1{x-1}-\frac1{x+1}
=
\frac{(x+1)-(x-1)}{x^2-1}
=
\frac2{x^2-1}.
$$

En su dominio este bloque nunca vale cero, porque el numerador es la constante $2$. Por tanto,

$$
\operatorname{Dom}(G)
=
\mathbb R\setminus\{-1,1\}.
$$

Para

$$
M_1(x)=x^2-1
$$

tenemos $M_1(x)\neq0$ en todo el dominio original. Por tanto, $M_1$ es un multiplicador válido.

En cambio,

$$
M_2(x)=(x^2-1)(x-4)
$$

se anula en $x=4$, y $4$ pertenece al dominio original. Usar $M_2$ reduciría la ruta a un dominio menor e introduciría artificialmente la restricción $x\neq4$.

Ejecutamos la ruta válida con $M_1=x^2-1$:

$$
G(x)
=
\frac{(x^2-1)\left(\dfrac1{x-1}+\dfrac1{x+1}\right)}
     {(x^2-1)\left(\dfrac1{x-1}-\dfrac1{x+1}\right)}.
$$

Distribuyendo,

$$
(x^2-1)\left(\frac1{x-1}+\frac1{x+1}\right)
=
(x+1)+(x-1)
=
2x,
$$

mientras que

$$
(x^2-1)\left(\frac1{x-1}-\frac1{x+1}\right)
=
(x+1)-(x-1)
=
2.
$$

Así,

$$
\boxed{
G(x)=x,
\qquad x\neq-1,1.
}
$$

El multiplicador $M_2$ no es «más general» por contener más factores. Contener un factor adicional sólo es inocuo si ese factor es no nulo en todo el dominio original; aquí $x-4$ falla precisamente esa condición.


## D. Diagnóstico y primera ruptura

En estas soluciones no basta con exhibir una forma correcta. La tarea consiste en localizar **la primera transición injustificada**, clasificarla y reconstruir la cadena desde el último paso válido. Cuando el resultado visible sea correcto pero la razón dada no lo sea, ambas cosas se distinguirán explícitamente.


### Solución 39

Partimos de

$$
\frac{x+4}{x+7}.
$$

El dominio original exige

$$
x+7\neq0,
$$

por lo que

$$
\operatorname{Dom}=
\mathbb R\setminus\{-7\}.
$$

La primera ruptura aparece cuando se afirma que puede «cancelarse la $x$». La cancelación sólo actúa sobre **factores** del numerador y del denominador completos. En

$$
x+4
\qquad\text{y}\qquad
x+7,
$$

la variable $x$ forma parte de dos sumas; no es un factor común.

Un contraejemplo permitido basta para refutar la igualdad propuesta. Tomando $x=1$,

$$
\frac{1+4}{1+7}=\frac58,
$$

mientras que

$$
\frac47\neq\frac58.
$$

Por tanto, no existe la identidad

$$
\frac{x+4}{x+7}=\frac47.
$$

Lo correcto es conservar la expresión tal como está:

$$
\boxed{
\frac{x+4}{x+7},
\qquad x\neq-7.
}
$$

Puede ocurrir que ambas expresiones coincidan en algún punto aislado; de hecho, en $x=0$ ambas valen $4/7$. Esa coincidencia puntual no autoriza una cancelación ni convierte la afirmación en una identidad.

**Clasificación del fallo:** cancelación ilegal de términos de una suma.


### Solución 40

La expresión es

$$
E(x)=
\frac{(x-2)(x+3)+5}{(x-2)(x+4)}.
$$

El denominador original exige

$$
x\neq2,
\qquad
x\neq-4.
$$

La primera transición inválida es

$$
\frac{(x-2)(x+3)+5}{(x-2)(x+4)}
\longmapsto
\frac{x+3+5}{x+4}.
$$

Para cancelar $x-2$, ese factor tendría que multiplicar **todo** el numerador. Pero el numerador es una suma:

$$
(x-2)(x+3)+5.
$$

El término $5$ no contiene el factor $x-2$. De hecho, si evaluamos el numerador en $x=2$, obtenemos $5\neq0$, lo que confirma que $x-2$ no es factor del numerador completo.

Podemos además usar un contraejemplo permitido. En $x=0$,

$$
E(0)
=
\frac{(-2)(3)+5}{(-2)(4)}
=
\frac{-1}{-8}
=
\frac18,
$$

mientras que la expresión propuesta daría

$$
\frac{0+3+5}{0+4}=2.
$$

Por tanto, la transición es falsa.

Una cancelación semejante sería legítima si el numerador pudiera escribirse, por ejemplo, como

$$
(x-2)N(x),
$$

de modo que la fracción completa tuviera la forma

$$
\frac{(x-2)N(x)}{(x-2)(x+4)}.
$$

Entonces, bajo $x\neq2$, sí podríamos cancelar el factor común.

**Clasificación del fallo:** cancelación a través de una suma; $x-2$ no es factor del numerador total.


### Solución 41

Consideramos

$$
\frac{x^2+3x}{x^2+5x}.
$$

Primero leemos el dominio original. Factorizando el denominador,

$$
x^2+5x=x(x+5),
$$

obtenemos

$$
x\neq0,
\qquad
x\neq-5.
$$

El resultado final propuesto,

$$
\frac{x+3}{x+5},
$$

**sí es correcto sobre el dominio original**. Lo incorrecto es la explicación «cancelé $x^2$».

No existe un factor común $x^2$ en los dos polinomios. La factorización correcta es

$$
x^2+3x=x(x+3),
$$

y

$$
x^2+5x=x(x+5).
$$

Así,

$$
\frac{x^2+3x}{x^2+5x}
=
\frac{x(x+3)}{x(x+5)}.
$$

Como el dominio original ya exige $x\neq0$, podemos cancelar **el factor $x$**:

$$
\boxed{
\frac{x^2+3x}{x^2+5x}
=
\frac{x+3}{x+5},
\qquad x\neq0,-5.
}
$$

Por tanto, debemos separar dos juicios:

1. la fórmula final es correcta sobre el dominio declarado;
2. la regla verbal usada para justificarla es falsa.

Un resultado correcto puede alcanzarse mediante una explicación inválida; eso no convierte la explicación en una regla algebraica aceptable.

**Clasificación del fallo:** justificación falsa de una simplificación cuyo resultado final es correcto.


### Solución 42

La expresión original es

$$
E(x)=
\frac{(x-1)(x+2)+(x-1)}{(x-1)(x+5)}.
$$

El denominador exige

$$
x\neq1,
\qquad
x\neq-5.
$$

La fórmula final

$$
\frac{x+3}{x+5}
$$

puede obtenerse correctamente. La frase «cancelando $x-1$ en cada término» puede expresar una operación válida si significa dividir **todo** el numerador y **todo** el denominador por el mismo factor $x-1\ne0$, distribuyendo la división sobre la suma. No basta con tachar símbolos sin declarar esa operación y su hipótesis. Una primera ruta hace explícita la factorización.

Factorizamos $x-1$:

$$
(x-1)(x+2)+(x-1)
=
(x-1)\bigl((x+2)+1\bigr)
=
(x-1)(x+3).
$$

Ahora sí la expresión completa tiene la forma

$$
E(x)
=
\frac{(x-1)(x+3)}{(x-1)(x+5)}.
$$

Como $x\neq1$ en el dominio original, cancelamos el factor común no nulo $x-1$:

$$
\boxed{
E(x)=\frac{x+3}{x+5},
\qquad x\neq1,-5.
}
$$

Una segunda ruta divide ambos bloques por $x-1\ne0$ y usa distributividad:

$$
E(x)=\frac{\dfrac{(x-1)(x+2)+(x-1)}{x-1}}
{\dfrac{(x-1)(x+5)}{x-1}}
=\frac{(x+2)+1}{x+5}=\frac{x+3}{x+5}.
$$

Las dos rutas son válidas bajo $x\ne1,-5$. Factorizar primero ayuda a mostrar el factor común, pero no es la única justificación posible. Aquí todos los sumandos contienen el factor; en el ejercicio 40, el sumando $5$ no lo contiene.

**Diagnóstico:** resultado correcto; la explicación abreviada necesita explicitar la división común y la distributividad, no declararse una regla falsa.


### Solución 43

La cadena propuesta comienza con

$$
\frac1{x-3}+\frac1{3-x}.
$$

El dominio original exige únicamente

$$
x\neq3.
$$

La primera ruptura es

$$
\frac1{3-x}
=
\frac1{x-3}.
$$

La relación correcta entre los factores es

$$
3-x=-(x-3).
$$

Por tanto,

$$
\frac1{3-x}
=
-\frac1{x-3}.
$$

Reparamos la cadena:

$$
\frac1{x-3}+\frac1{3-x}
=
\frac1{x-3}-\frac1{x-3}
=0.
$$

Así,

$$
\boxed{
\frac1{x-3}+\frac1{3-x}=0,
\qquad x\neq3.
}
$$

El fallo aparece **antes** de cualquier problema de denominador común. Los dos denominadores ya son factores opuestos y pueden normalizarse inmediatamente; el error consiste en tratarlos como si fueran iguales y perder el factor $-1$.

**Clasificación del fallo:** error de signo por factores opuestos.


### Solución 44

El primer paso de la cadena es correcto:

$$
\frac{2x+1}{x+1}-\frac{x-3}{x-2}
=
\frac{(2x+1)(x-2)-(x-3)(x+1)}{(x+1)(x-2)}.
$$

El dominio original es

$$
x\neq-1,
\qquad
x\neq2.
$$

Las expansiones también son correctas:

$$
(2x+1)(x-2)=2x^2-3x-2,
$$

$$
(x-3)(x+1)=x^2-2x-3.
$$

La primera ruptura aparece al retirar el segundo paréntesis. Debemos tener

$$
(2x^2-3x-2)-(x^2-2x-3)
$$

igual a

$$
2x^2-3x-2-x^2+2x+3,
$$

porque el signo menos cambia el signo de **cada término** del segundo polinomio.

Entonces

$$
2x^2-3x-2-x^2+2x+3
=
x^2-x+1.
$$

Por tanto,

$$
\boxed{
\frac{2x+1}{x+1}-\frac{x-3}{x-2}
=
\frac{x^2-x+1}{(x+1)(x-2)},
\qquad x\neq-1,2.
}
$$

No aparece un factor común que pueda cancelarse con el denominador.

**Clasificación del fallo:** distribución incorrecta del signo menos sobre un numerador completo.


### Solución 45

La expresión original es

$$
\frac1{x-1}+\frac1{x+1}.
$$

Su dominio es

$$
\mathbb R\setminus\{-1,1\}.
$$

La primera regla falsa aparece al escribir

$$
\frac1{x-1}+\frac1{x+1}
=
\frac2{(x-1)+(x+1)}.
$$

No se suman los denominadores. Para sumar fracciones necesitamos un **denominador común**.

Elegimos

$$
(x-1)(x+1)=x^2-1.
$$

Entonces

$$
\frac1{x-1}
=
\frac{x+1}{(x-1)(x+1)}
$$

y

$$
\frac1{x+1}
=
\frac{x-1}{(x-1)(x+1)}.
$$

Sumando,

$$
\frac1{x-1}+\frac1{x+1}
=
\frac{(x+1)+(x-1)}{x^2-1}
=
\frac{2x}{x^2-1}.
$$

Por tanto,

$$
\boxed{
\frac1{x-1}+\frac1{x+1}
=
\frac{2x}{x^2-1},
\qquad x\neq-1,1.
}
$$

La fórmula errónea $1/x$ introduciría además la exclusión aparente $x=0$. Pero $x=0$ sí pertenece al dominio original:

$$
\frac1{-1}+\frac11=0.
$$

Así, la ruta falsa no sólo produce valores incorrectos; también fabrica una restricción que no pertenecía al problema.

**Clasificación del fallo:** regla falsa de suma de fracciones, con introducción posterior de una exclusión artificial.


### Solución 46

Partimos de

$$
Q(x)=
\frac{x+1}{x-2}
\div
\frac{x-3}{x+4}.
$$

Antes de operar determinamos el dominio del cociente original.

El dividendo exige

$$
x\neq2.
$$

El divisor $(x-3)/(x+4)$ debe estar definido, por lo que

$$
x\neq-4.
$$

Además, como funciona como divisor, debe ser distinto de cero. Bajo $x\neq-4$, se anula cuando

$$
x-3=0,
$$

es decir, en

$$
x=3.
$$

Por tanto,

$$
\operatorname{Dom}(Q)
=
\mathbb R\setminus\{-4,2,3\}.
$$

La primera ruptura de la cadena propuesta consiste en reemplazar la división por una multiplicación **sin invertir el divisor**. El objeto que debe invertirse es el cociente completo

$$
\frac{x-3}{x+4},
$$

cuyo recíproco es

$$
\frac{x+4}{x-3}.
$$

Así,

$$
Q(x)
=
\frac{x+1}{x-2}
\cdot
\frac{x+4}{x-3}.
$$

No hay factores comunes, de modo que

$$
\boxed{
Q(x)=
\frac{(x+1)(x+4)}{(x-2)(x-3)},
\qquad x\neq-4,2,3.
}
$$

Las exclusiones $x=-4$ y $x=3$ tienen causas distintas: en $x=-4$ el divisor **no está definido**; en $x=3$ está definido, pero **vale cero**.

**Clasificación del fallo:** inversión incorrecta del divisor completo.


### Solución 47

La expresión original es

$$
R(x)=\frac{x^2-16}{x-4}.
$$

Su dominio se fija antes de simplificar:

$$
x\neq4.
$$

La factorización

$$
x^2-16=(x-4)(x+4)
$$

es correcta, y sobre el dominio original también es correcta la cancelación:

$$
R(x)
=
\frac{(x-4)(x+4)}{x-4}
=
x+4.
$$

Por tanto, **no hay una ruptura algebraica** en esos pasos. La primera ruptura aparece después, cuando el estudiante mira la fórmula final $x+4$ y concluye que el dominio original era $\mathbb R$.

La afirmación completa correcta es

$$
\boxed{
\frac{x^2-16}{x-4}=x+4,
\qquad x\neq4.
}
$$

La fórmula $x+4$ tiene dominio natural $\mathbb R$, pero sólo coincide con el cociente original en el conjunto donde éste estaba definido. En $x=4$ la forma final vale $8$, mientras que la expresión original contiene división por cero.

**Clasificación del fallo:** pérdida de dominio al reconstruirlo desde la fórmula simplificada.


### Solución 48

Consideramos

$$
Q(x)=
\frac{x-2}{x+1}
\div
\frac{x-2}{x-4}.
$$

La lista propuesta excluye $x=-1$ y $x=4$, pero falta una tercera condición.

El dividendo exige

$$
x\neq-1.
$$

El divisor exige

$$
x\neq4
$$

para estar definido. Además, debe ser distinto de cero. Bajo $x\neq4$,

$$
\frac{x-2}{x-4}=0
$$

cuando

$$
x=2.
$$

Así, el dominio correcto es

$$
\mathbb R\setminus\{-1,2,4\}.
$$

En $x=2$ el divisor está perfectamente definido:

$$
\frac{2-2}{2-4}=0,
$$

pero precisamente por valer cero no puede ocupar el lugar de divisor.

Ahora invertimos el divisor completo:

$$
Q(x)
=
\frac{x-2}{x+1}
\cdot
\frac{x-4}{x-2}.
$$

Como $x\neq2$ pertenece al dominio original, cancelamos $x-2$:

$$
\boxed{
Q(x)=\frac{x-4}{x+1},
\qquad x\neq-1,2,4.
}
$$

La fórmula visible propuesta era correcta, pero la afirmación completa era falsa por omitir $x=2$.

**Clasificación del fallo:** pérdida de una restricción producida por un divisor definido pero nulo.


### Solución 49

La suma original es

$$
S(x)=\frac1{x-1}+\frac1{x+1}.
$$

Su dominio es

$$
D=\mathbb R\setminus\{-1,1\}.
$$

El denominador propuesto

$$
(x-1)(x+1)(x+5)
$$

contiene un factor auxiliar $x+5$ que no procede de ninguno de los denominadores originales. Para introducirlo habría que multiplicar por

$$
\frac{x+5}{x+5},
$$

operación que sólo representa al número $1$ cuando

$$
x\neq-5.
$$

Pero $-5$ pertenece al dominio original $D$. Por tanto, la primera decisión que impide conservar la equivalencia sobre **todo** el dominio es escoger un denominador que obliga a introducir el factor auxiliar $x+5$.

La ruta quedaría restringida artificialmente a

$$
\mathbb R\setminus\{-5,-1,1\}.
$$

La reparación consiste en usar el denominador común adecuado

$$
(x-1)(x+1).
$$

Entonces

$$
S(x)
=
\frac{x+1}{(x-1)(x+1)}
+
\frac{x-1}{(x-1)(x+1)}
$$

y, por tanto,

$$
\boxed{
S(x)=\frac{2x}{x^2-1},
\qquad x\neq-1,1.
}
$$

Un denominador con más factores no es «más general». Si esos factores poseen ceros dentro del dominio original, la transformación es válida en menos puntos, no en más.

**Clasificación del fallo:** introducción artificial de una restricción mediante un factor auxiliar.


### Solución 50

La expresión es

$$
T(x)=
\frac{\dfrac{x^2-1}{x-1}}
     {\dfrac{x+1}{x+2}}.
$$

La primera ruptura ocurre ya en la declaración del dominio.

Leemos la expresión por niveles.

El bloque superior

$$
\frac{x^2-1}{x-1}
$$

exige

$$
x\neq1.
$$

El bloque inferior

$$
\frac{x+1}{x+2}
$$

exige

$$
x\neq-2
$$

para estar definido. Como además ese bloque funciona como divisor exterior, debe ser distinto de cero; por tanto,

$$
x\neq-1.
$$

Así, el dominio original completo es

$$
\boxed{
\operatorname{Dom}(T)
=
\mathbb R\setminus\{-2,-1,1\}.
}
$$

La omisión de $x=1$ es la primera ruptura. Ocurre **antes** de los pasos algebraicos posteriores.

Ahora, sobre el dominio correcto, podemos simplificar el bloque superior:

$$
\frac{x^2-1}{x-1}
=
\frac{(x-1)(x+1)}{x-1}
=
x+1,
\qquad x\neq1.
$$

Entonces

$$
T(x)
=
\frac{x+1}{\dfrac{x+1}{x+2}}
=
(x+1)\frac{x+2}{x+1}.
$$

Como $x\neq-1$ ya pertenece al dominio original, cancelamos $x+1$ y obtenemos

$$
\boxed{
T(x)=x+2,
\qquad x\neq-2,-1,1.
}
$$

Los pasos posteriores a la declaración incorrecta del dominio pueden ser algebraicamente válidos **sobre el dominio correcto** o sobre un subconjunto donde sus hipótesis se cumplan. Pero no reparan retroactivamente la omisión inicial. Una cadena no recupera una restricción perdida sólo porque llegue a una fórmula algebraicamente correcta.

**Clasificación del fallo:** primera ruptura en la lectura del dominio; omisión de una restricción heredada del bloque superior.


## E. Estrategia y elección de ruta


### Solución 51

La expresión original es

$$
\frac{2}{x(x-1)}+\frac{3}{(x-1)^2}.
$$

El dominio se obtiene de los denominadores originales:

$$
x\neq0,
\qquad
x\neq1.
$$

Por tanto,

$$
D=\mathbb R\setminus\{0,1\}.
$$

Analicemos los tres candidatos.

- $D_1=x(x-1)^2$ contiene una copia de $x$ y dos de $x-1$, exactamente lo necesario para absorber ambos denominadores. Es **adecuado y económico**.
- $D_2=x(x-1)^3$ también es no nulo en todo $D$, porque sus únicos ceros son $0$ y $1$, ya excluidos. Es **adecuado pero innecesariamente grande**: repite una copia adicional de $x-1$.
- $D_3=x(x-1)^2(x+2)$ se anula además en $x=-2$, valor que sí pertenece al dominio original. Para usarlo habría que introducir un factor $(x+2)/(x+2)$ y restringir artificialmente la transformación a $x\neq-2$. Por tanto, es **inadecuado para conservar equivalencia en todo el dominio original**.

Elegimos $D_1$. Entonces

$$
\frac{2}{x(x-1)}
=
\frac{2(x-1)}{x(x-1)^2}
$$

y

$$
\frac{3}{(x-1)^2}
=
\frac{3x}{x(x-1)^2}.
$$

Sumando,

$$
\frac{2(x-1)+3x}{x(x-1)^2}
=
\frac{5x-2}{x(x-1)^2}.
$$

No aparece ningún factor común que pueda cancelarse. Así,

$$
\boxed{
\frac{2}{x(x-1)}+\frac{3}{(x-1)^2}
=
\frac{5x-2}{x(x-1)^2},
\qquad x\neq0,1.
}
$$

La mejor elección no es simplemente la más pequeña por apariencia: es la que contiene todos los factores necesarios, no introduce ceros nuevos y evita repeticiones inútiles.


### Solución 52

La expresión es

$$
\frac{1}{(x+2)^2(x-3)}
-
\frac{4}{(x+2)(x-3)^2}.
$$

El dominio original exige

$$
x\neq-2,
\qquad
x\neq3.
$$

En los denominadores aparecen los factores $x+2$ y $x-3$. La mayor potencia necesaria de cada uno es $2$, de modo que

$$
D_1=(x+2)^2(x-3)^2
$$

contiene exactamente la estructura requerida.

El candidato

$$
D_2=(x+2)^3(x-3)^3
$$

es también válido en el dominio original: no introduce ceros nuevos. Sin embargo, añade una copia innecesaria de cada factor y multiplica el trabajo algebraico.

En cambio,

$$
D_3=(x+2)^2(x-3)^2(x-5)
$$

introduce el cero $x=5$, que no estaba excluido originalmente. Por tanto, sólo permitiría una transformación equivalente en un dominio menor.

Usamos $D_1$. La primera fracción necesita una copia adicional de $x-3$ y la segunda una copia adicional de $x+2$:

$$
\frac{x-3}{(x+2)^2(x-3)^2}
-
\frac{4(x+2)}{(x+2)^2(x-3)^2}.
$$

Así,

$$
\frac{(x-3)-4(x+2)}{(x+2)^2(x-3)^2}
=
\frac{-3x-11}{(x+2)^2(x-3)^2}.
$$

Por tanto,

$$
\boxed{
\frac{1}{(x+2)^2(x-3)}
-
\frac{4}{(x+2)(x-3)^2}
=
\frac{-3x-11}{(x+2)^2(x-3)^2},
\qquad x\neq-2,3.
}
$$

La potencia correcta de cada factor se obtiene mirando la máxima multiplicidad ya exigida por alguno de los denominadores; no es necesario sumar las potencias de todos ellos.


### Solución 53

Tenemos

$$
S(x)=
\frac{1}{x(x-1)}
+
\frac{2}{x^2(x-1)}
-
\frac{3}{x(x-1)^2}.
$$

Todos los denominadores exigen

$$
x\neq0,
\qquad
x\neq1.
$$

El inventario de factores es:

- para $x$, la mayor potencia necesaria es $x^2$;
- para $x-1$, la mayor potencia necesaria es $(x-1)^2$.

Por tanto, un denominador común económico es

$$
x^2(x-1)^2.
$$

Multiplicar sin inspección los tres denominadores produciría

$$
x^4(x-1)^4,
$$

que sigue siendo válido en el mismo dominio, pero repite factores muchas veces y obliga a introducir numeradores mucho más grandes para llegar finalmente a una expresión equivalente.

Con el denominador económico,

$$
\frac{1}{x(x-1)}
=
\frac{x(x-1)}{x^2(x-1)^2},
$$

$$
\frac{2}{x^2(x-1)}
=
\frac{2(x-1)}{x^2(x-1)^2},
$$

y

$$
\frac{3}{x(x-1)^2}
=
\frac{3x}{x^2(x-1)^2}.
$$

Entonces

$$
S(x)
=
\frac{x(x-1)+2(x-1)-3x}{x^2(x-1)^2}.
$$

El numerador se reduce a

$$
x^2-x+2x-2-3x
=
x^2-2x-2.
$$

Así,

$$
\boxed{
S(x)=\frac{x^2-2x-2}{x^2(x-1)^2},
\qquad x\neq0,1.
}
$$

La comparación entre rutas muestra que un denominador bruto puede ser correcto y, aun así, ser una mala elección estratégica.


### Solución 54

Consideramos

$$
F(x)=
\frac{\dfrac1{x-1}+\dfrac1{x+1}}
     {\dfrac1{x-1}-\dfrac1{x+1}}.
$$

Las fracciones internas exigen

$$
x\neq1,
\qquad
x\neq-1.
$$

Además debemos comprobar que el denominador exterior completo no sea cero. Reducimos sólo ese bloque:

$$
\frac1{x-1}-\frac1{x+1}
=
\frac{(x+1)-(x-1)}{(x-1)(x+1)}
=
\frac{2}{x^2-1}.
$$

En el dominio $x\neq\pm1$, esta expresión nunca vale cero. Por tanto,

$$
\operatorname{Dom}(F)=\mathbb R\setminus\{-1,1\}.
$$

Ahora analizamos los multiplicadores.

- $M_1=x^2-1=(x-1)(x+1)$ es no nulo en todo el dominio original y contiene exactamente los factores necesarios. Es la mejor elección.
- $M_2=(x^2-1)^2$ también es no nulo en todo el dominio original, pero repite innecesariamente los factores.
- $M_3=(x^2-1)(x-4)$ se anula en $x=4$, punto permitido originalmente. Por tanto, reduce artificialmente el dominio.

Usamos $M_1$. Multiplicamos los dos bloques exteriores por $x^2-1$:

$$
F(x)
=
\frac{(x^2-1)\left(\dfrac1{x-1}+\dfrac1{x+1}\right)}
     {(x^2-1)\left(\dfrac1{x-1}-\dfrac1{x+1}\right)}.
$$

Por distributividad y cancelaciones autorizadas,

$$
(x^2-1)\left(\frac1{x-1}+\frac1{x+1}\right)
=(x+1)+(x-1)=2x,
$$

mientras que

$$
(x^2-1)\left(\frac1{x-1}-\frac1{x+1}\right)
=(x+1)-(x-1)=2.
$$

Por tanto,

$$
\boxed{
F(x)=x,
\qquad x\neq-1,1.
}
$$

La elección estratégica correcta elimina simultáneamente todos los denominadores internos sin introducir ninguna condición ajena a la expresión original.


### Solución 55

Sea

$$
P(x)=
\frac{x^2-25}{x^2-2x-15}
\cdot
\frac{x-5}{x+5}.
$$

Primero fijamos el dominio. Como

$$
x^2-2x-15=(x-5)(x+3),
$$

el primer factor exige $x\neq5,-3$. El segundo exige $x\neq-5$. Por tanto,

$$
D=\mathbb R\setminus\{-5,-3,5\}.
$$

**Ruta A: factorizar antes de multiplicar.** Como

$$
x^2-25=(x-5)(x+5),
$$

obtenemos

$$
P(x)
=
\frac{(x-5)(x+5)}{(x-5)(x+3)}
\cdot
\frac{x-5}{x+5}.
$$

En $D$, los factores $x-5$ y $x+5$ son no nulos. Cancelando una copia de cada factor adecuado,

$$
\boxed{
P(x)=\frac{x-5}{x+3},
\qquad x\neq-5,-3,5.
}
$$

**Ruta B: expandir primero.** Multiplicando las formas visibles obtenemos

$$
P(x)
=
\frac{(x^2-25)(x-5)}{(x^2-2x-15)(x+5)}
$$

y luego

$$
P(x)
=
\frac{x^3-5x^2-25x+125}
     {x^3+3x^2-25x-75}.
$$

La expresión sigue siendo correcta sobre el mismo dominio $D$, pero la estructura útil ha desaparecido. Para simplificar debemos factorizar de nuevo:

$$
x^3-5x^2-25x+125=(x-5)^2(x+5),
$$

$$
x^3+3x^2-25x-75=(x-5)(x+3)(x+5),
$$

y volvemos a

$$
\frac{x-5}{x+3}.
$$

Las dos rutas son válidas. La ruta A es preferible porque conserva visibles tanto los factores cancelables como las restricciones del dominio y evita crear dos polinomios cúbicos que después debemos volver a factorizar.


### Solución 56

Consideremos

$$
Q(x)=
\frac{x^2-4}{x^2+x-6}
\div
\frac{x-2}{x+3}.
$$

El dividendo exige

$$
x^2+x-6=(x+3)(x-2)\neq0,
$$

así que $x\neq-3,2$. El divisor exige $x\neq-3$ para estar definido y, además, debe ser no nulo; por tanto $x\neq2$. El dominio original es

$$
D=\mathbb R\setminus\{-3,2\}.
$$

**Estrategia 1: simplificar primero el dividendo.** Factorizamos

$$
x^2-4=(x-2)(x+2),
$$

por lo que, sobre el dominio original,

$$
\frac{x^2-4}{x^2+x-6}
=
\frac{(x-2)(x+2)}{(x+3)(x-2)}
=
\frac{x+2}{x+3},
$$

manteniendo $x\neq-3,2$.

Entonces

$$
Q(x)
=
\frac{x+2}{x+3}
\div
\frac{x-2}{x+3}
=
\frac{x+2}{x+3}
\cdot
\frac{x+3}{x-2}.
$$

Como $x\neq-3$, cancelamos $x+3$:

$$
Q(x)=\frac{x+2}{x-2}.
$$

**Estrategia 2: invertir primero el divisor.** Escribimos

$$
Q(x)
=
\frac{x^2-4}{x^2+x-6}
\cdot
\frac{x+3}{x-2}.
$$

Factorizando todos los polinomios,

$$
Q(x)
=
\frac{(x-2)(x+2)}{(x+3)(x-2)}
\cdot
\frac{x+3}{x-2}.
$$

Las cancelaciones autorizadas conducen de nuevo a

$$
\frac{x+2}{x-2}.
$$

Por tanto,

$$
\boxed{
Q(x)=\frac{x+2}{x-2},
\qquad x\neq-3,2.
}
$$

Las dos rutas son correctas. La primera deja más transparente la procedencia de la primera cancelación: ocurre dentro del dividendo y sólo bajo su dominio heredado. La segunda es algo más compacta, pero concentra varias cancelaciones en un único producto total.


### Solución 57

Tenemos

$$
H(x)=
\frac{\dfrac1x+\dfrac1{x+1}}
     {\dfrac1x-\dfrac1{x+1}}.
$$

Las fracciones internas exigen

$$
x\neq0,
\qquad
x\neq-1.
$$

El denominador exterior es

$$
\frac1x-\frac1{x+1}
=
\frac{(x+1)-x}{x(x+1)}
=
\frac1{x(x+1)},
$$

que nunca vale cero cuando está definido. Por tanto,

$$
D=\mathbb R\setminus\{-1,0\}.
$$

**Método interior.** Reducimos los dos bloques:

$$
\frac1x+\frac1{x+1}
=
\frac{2x+1}{x(x+1)},
$$

$$
\frac1x-\frac1{x+1}
=
\frac1{x(x+1)}.
$$

Entonces

$$
H(x)
=
\frac{\dfrac{2x+1}{x(x+1)}}
     {\dfrac1{x(x+1)}}
=
2x+1.
$$

**Eliminación de denominadores internos.** Elegimos

$$
M(x)=x(x+1),
$$

que es no nulo en todo $D$. Entonces

$$
H(x)
=
\frac{x(x+1)\left(\dfrac1x+\dfrac1{x+1}\right)}
     {x(x+1)\left(\dfrac1x-\dfrac1{x+1}\right)}.
$$

Distribuyendo,

$$
\text{numerador}=(x+1)+x=2x+1,
$$

$$
\text{denominador}=(x+1)-x=1.
$$

Así obtenemos otra vez

$$
\boxed{
H(x)=2x+1,
\qquad x\neq-1,0.
}
$$

En este ejemplo, eliminar denominadores internos es más corto: evita construir dos fracciones intermedias y la posterior inversión del denominador exterior. El método interior, sin embargo, hace muy explícita la estructura de cada bloque. Ninguna de estas ventajas es universal; en otras fracciones complejas la reducción separada de los bloques puede ser más transparente o más económica.


### Solución 58

La expresión es

$$
E(x)=
\left(
\frac{x^2-4}{x-2}
\div
\frac{x+2}{x+1}
\right)
+
\frac1{x+1}.
$$

Primero registramos las restricciones por procedencia.

- El dividendo exige $x\neq2$.
- El divisor exige $x\neq-1$ para estar definido y $x\neq-2$ para ser no nulo.
- El último sumando exige nuevamente $x\neq-1$.

Por tanto,

$$
D=\mathbb R\setminus\{-2,-1,2\}.
$$

El plan más económico es cerrar primero el cociente entre paréntesis.

En el dominio original,

$$
\frac{x^2-4}{x-2}
=
\frac{(x-2)(x+2)}{x-2}
=
x+2,
$$

manteniendo $x\neq2$. Entonces

$$
\frac{x^2-4}{x-2}
\div
\frac{x+2}{x+1}
=
(x+2)\cdot\frac{x+1}{x+2}.
$$

Como $x\neq-2$ pertenece al dominio original, cancelamos $x+2$ y el bloque completo se reduce a

$$
x+1.
$$

Ahora sólo queda

$$
E(x)=x+1+\frac1{x+1}.
$$

Usamos el denominador $x+1$:

$$
E(x)
=
\frac{(x+1)^2+1}{x+1}
=
\frac{x^2+2x+2}{x+1}.
$$

Así,

$$
\boxed{
E(x)=\frac{x^2+2x+2}{x+1},
\qquad x\neq-2,-1,2.
}
$$

La alternativa de combinar desde el comienzo todas las fracciones visibles es algebraicamente posible, pero mezcla en una sola cadena la división interior y la suma exterior. Cerrar primero el cociente preserva un bloque natural de la expresión y reduce el número de denominadores que deben gestionarse simultáneamente.


### Solución 59

Una construcción que satisface las cuatro condiciones es

$$
P(x)=
\frac{(x+2)(x-3)}{x+1}
\cdot
\frac{x+1}{x-3}.
$$

Ambos factores son expresiones racionales no constantes y ambos tienen denominador no constante.

El primer factor exige

$$
x\neq-1,
$$

mientras que el segundo exige

$$
x\neq3.
$$

Así, el dominio original del producto es exactamente

$$
D=\mathbb R\setminus\{-1,3\}.
$$

En ese dominio,

$$
P(x)
=
\frac{(x+2)(x-3)(x+1)}{(x+1)(x-3)}.
$$

Los factores $x+1$ y $x-3$ aparecen en fracciones distintas antes de formar el producto total; por tanto, la simplificación incluye cancelaciones entre factores procedentes de fracciones diferentes. Como ambos son no nulos en $D$,

$$
\boxed{
P(x)=x+2,
\qquad x\neq-1,3.
}
$$

La fórmula final $x+2$ está definida para todo real, de modo que ninguna de las dos exclusiones permanece visible. La construcción satisface, por tanto, las cuatro condiciones pedidas.


### Solución 60

Partimos de la expresión simple

$$
R(x)=\frac{x-1}{x+3}.
$$

Queremos construir dos representaciones distintas de $R$ que introduzcan huecos removibles diferentes. Definimos

$$
A(x)=
\frac{(x-1)(x+2)}{(x+3)(x+2)}
$$

y

$$
B(x)=
\frac{(x-1)(x-4)}{(x+3)(x-4)}.
$$

Tomamos entonces el cociente

$$
Q(x)=A(x)\div B(x).
$$

Estudiemos el dominio por partes.

El **dividendo** $A$ exige

$$
x\neq-3,-2.
$$

La exclusión $x=-2$ procede del factor removible $x+2$ situado en su denominador.

El **divisor** $B$ exige

$$
x\neq-3,4.
$$

La exclusión $x=4$ procede del factor removible $x-4$ situado en su denominador.

Además, el divisor completo debe ser distinto de cero. En su dominio,

$$
B(x)=\frac{x-1}{x+3},
$$

por lo que se anula exactamente en

$$
x=1.
$$

Así, el dominio de $Q$ es exactamente

$$
\boxed{
\operatorname{Dom}(Q)
=
\mathbb R\setminus\{-3,-2,1,4\}.
}
$$

Ahora simplificamos sobre ese dominio. Como los factores removibles son no nulos allí,

$$
A(x)=\frac{x-1}{x+3}
$$

y

$$
B(x)=\frac{x-1}{x+3}.
$$

Por tanto,

$$
Q(x)
=
\frac{\dfrac{x-1}{x+3}}
     {\dfrac{x-1}{x+3}}
=1,
$$

porque $x\neq1$ garantiza que el divisor no es cero. En consecuencia,

$$
\boxed{
Q(x)=1,
\qquad x\neq-3,-2,1,4.
}
$$

La forma final $1$ no muestra ninguna de las cuatro restricciones. Por eso presentar sólo esa fórmula sería matemáticamente incompleto: se perdería la procedencia de $x=-2$ y $x=4$ como huecos removibles, de $x=1$ como cero del divisor y de $x=-3$ como cero del denominador esencial compartido.

## F. Transferencia C18–C19 y varias capas


### Solución 61

Los parámetros $a$ y $b$ se consideran reales fijos. La expresión es

$$
F_{a,b}(x)=
\frac{3(x-a)}{(x-a)(x-b)}.
$$

El dominio se determina **antes** de cancelar. El denominador exige

$$
x-a\neq0
\qquad\text{y}\qquad
x-b\neq0.
$$

Por tanto,

$$
\operatorname{Dom}(F_{a,b})
=
\mathbb R\setminus\{a,b\},
$$

entendiendo que, si $a=b$, el conjunto $\{a,b\}$ contiene un solo punto.

Sobre ese dominio, $x-a$ es no nulo y puede cancelarse:

$$
F_{a,b}(x)
=
\frac{3(x-a)}{(x-a)(x-b)}
=
\frac{3}{x-b}.
$$

Así,

$$
\boxed{
F_{a,b}(x)=\frac3{x-b},
\qquad x\neq a,b.
}
$$

Si $a\neq b$, hay dos puntos excluidos. La forma final sólo muestra $x\neq b$, de modo que la exclusión $x=a$ queda oculta por la cancelación.

Si $a=b$, las dos condiciones simbólicas $x\neq a$ y $x\neq b$ describen el mismo punto. En ese caso hay una sola exclusión y la forma final es

$$
\frac3{x-a},
\qquad x\neq a.
$$

No hay aquí dos restricciones geométricamente distintas: hay dos expresiones simbólicas que coinciden porque los parámetros coinciden.


### Solución 62

Partimos de

$$
S_{a,b}(x)=
\frac1{x-a}
-
\frac1{x-b}.
$$

El dominio original exige

$$
x\neq a,
\qquad
x\neq b.
$$

Con denominador común $(x-a)(x-b)$,

$$
S_{a,b}(x)
=
\frac{x-b}{(x-a)(x-b)}
-
\frac{x-a}{(x-a)(x-b)}.
$$

Combinando los numeradores,

$$
(x-b)-(x-a)=a-b,
$$

por lo que

$$
\boxed{
S_{a,b}(x)
=
\frac{a-b}{(x-a)(x-b)},
\qquad x\neq a,b.
}
$$

Si $a\neq b$, las exclusiones $a$ y $b$ son dos puntos distintos.

Si $a=b$, la expresión original se convierte en

$$
\frac1{x-a}-\frac1{x-a}=0,
\qquad x\neq a.
$$

La fórmula combinada también refleja lo mismo:

$$
\frac{a-a}{(x-a)^2}
=
\frac0{(x-a)^2}
=0,
\qquad x\neq a.
$$

Por tanto, el caso $a=b$ no introduce una regla nueva. Sólo hace coincidir los dos factores del denominador y fusiona las dos exclusiones simbólicas en un único punto del dominio.


### Solución 63

La expresión es

$$
Q_{a,b}(x)=
\frac{\dfrac1{x-a}}
     {\dfrac{x-b}{x-a}}.
$$

Leemos primero el dominio por niveles.

La fracción del numerador exige

$$
x\neq a.
$$

El divisor

$$
\frac{x-b}{x-a}
$$

también exige $x\neq a$ para estar definido. Además, como ocupa el lugar de divisor exterior, debe ser distinto de cero. Bajo $x\neq a$ se anula exactamente cuando

$$
x-b=0,
$$

es decir, cuando $x=b$.

Por tanto,

$$
\operatorname{Dom}(Q_{a,b})
=
\mathbb R\setminus\{a,b\},
$$

con una sola exclusión si $a=b$.

Ahora sí invertimos el divisor completo:

$$
Q_{a,b}(x)
=
\frac1{x-a}
\cdot
\frac{x-a}{x-b}.
$$

Como $x\neq a$ ya pertenece al dominio original, cancelamos $x-a$ y obtenemos

$$
\boxed{
Q_{a,b}(x)=\frac1{x-b},
\qquad x\neq a,b.
}
$$

Si $a\neq b$, la forma final deja visible sólo $x\neq b$ y oculta $x=a$.

Si $a=b$, entonces las dos restricciones se refieren al mismo punto y la fórmula final es

$$
\frac1{x-a},
\qquad x\neq a.
$$

La fusión de restricciones procede de la igualdad de los parámetros, no de una excepción en la regla de división.


### Solución 64

Consideremos

$$
P_{a,b}(x)=
\frac{(x-a)(x+a)}{x-b}
\cdot
\frac{x-b}{x-a}.
$$

Antes de cancelar, los denominadores originales imponen

$$
x\neq b
\qquad\text{y}\qquad
x\neq a.
$$

Así,

$$
\operatorname{Dom}(P_{a,b})
=
\mathbb R\setminus\{a,b\}.
$$

En ese dominio, tanto $x-b$ como $x-a$ son no nulos. Por tanto,

$$
P_{a,b}(x)
=
\frac{(x-a)(x+a)}{x-b}
\cdot
\frac{x-b}{x-a}
=
x+a.
$$

La respuesta completa es

$$
\boxed{
P_{a,b}(x)=x+a,
\qquad x\neq a,b.
}
$$

Si $a\neq b$, la expresión original excluye dos puntos y la fórmula polinómica final no muestra ninguno de ellos.

Si $a=b$, ambos denominadores se anulan en el mismo punto y queda una sola exclusión:

$$
\boxed{
P_{a,a}(x)=x+a,
\qquad x\neq a.
}
$$

La naturaleza polinómica de la fórmula final no amplía el dominio de procedencia.


### Solución 65

Tenemos

$$
R_a(x)=
\frac{x-a}{\sqrt{x-a}}.
$$

Para que la raíz cuadrada principal sea real necesitamos

$$
x-a\ge0.
$$

Pero la raíz aparece además en el denominador, así que debe ser no nula:

$$
\sqrt{x-a}\neq0.
$$

Esto equivale a

$$
x-a>0,
$$

por lo que

$$
\operatorname{Dom}(R_a)=(a,\infty).
$$

En ese dominio, la raíz principal satisface

$$
x-a=\bigl(\sqrt{x-a}\bigr)^2.
$$

Por tanto,

$$
R_a(x)
=
\frac{\bigl(\sqrt{x-a}\bigr)^2}{\sqrt{x-a}}
=
\sqrt{x-a},
$$

porque $\sqrt{x-a}\neq0$ en el dominio original. Así,

$$
\boxed{
R_a(x)=\sqrt{x-a},
\qquad x>a.
}
$$

La fórmula final $\sqrt{x-a}$ tiene dominio natural $x\ge a$, mientras que la expresión original sólo existe para $x>a$. El punto $x=a$ queda oculto por la cancelación y no puede recuperarse como valor de la expresión inicial.


### Solución 66

La propuesta era

$$
\frac{\sqrt{(x-a)^2}}{x-a}=1,
\qquad x\neq a.
$$

La regla correcta de C18 es

$$
\sqrt{u^2}=|u|.
$$

Tomando $u=x-a$,

$$
\sqrt{(x-a)^2}=|x-a|.
$$

Por tanto, la expresión correcta es

$$
\boxed{
\frac{\sqrt{(x-a)^2}}{x-a}
=
\frac{|x-a|}{x-a},
\qquad x\neq a.
}
$$

La identidad propuesta se refuta con un solo valor permitido. Si elegimos

$$
x=a-1,
$$

entonces

$$
\frac{\sqrt{(x-a)^2}}{x-a}
=
\frac{\sqrt{(-1)^2}}{-1}
=
\frac1{-1}
=-1,
$$

que no es $1$.

No necesitamos construir una tabla de signos: basta usar la identidad de raíz principal y un contraejemplo.

La expresión original es **fraccionaria** porque está escrita como un cociente. No debe clasificarse automáticamente como racional: su numerador contiene una raíz cuadrada y no es, en esa forma, una expresión polinómica.


### Solución 67

La expresión es

$$
A(x)=
\frac{x^2-16}{(4-x)(x+4)}.
$$

El dominio original exige

$$
4-x\neq0
\qquad\text{y}\qquad
x+4\neq0,
$$

por lo que

$$
x\neq4,
\qquad
x\neq-4.
$$

Factorizamos la diferencia de cuadrados:

$$
x^2-16=(x-4)(x+4).
$$

Además,

$$
4-x=-(x-4).
$$

Así,

$$
A(x)
=
\frac{(x-4)(x+4)}{-(x-4)(x+4)}.
$$

En el dominio original ambos factores son no nulos, de modo que pueden cancelarse y queda

$$
\boxed{
A(x)=-1,
\qquad x\neq-4,4.
}
$$

La constante $-1$ está definida para todo real, pero la expresión original no existe en $x=\pm4$. El signo negativo procede exactamente de la normalización $4-x=-(x-4)$ y no puede perderse durante la cancelación.


### Solución 68

Consideremos

$$
B(x)=
\frac{x-9}{\sqrt{x}-3}.
$$

Para trabajar en $\mathbb R$, la raíz principal exige

$$
x\ge0.
$$

Además, el denominador debe ser no nulo:

$$
\sqrt{x}-3\neq0.
$$

Como $\sqrt{x}=3$ exactamente cuando $x=9$, el dominio original es

$$
\boxed{
[0,\infty)\setminus\{9\}.
}
$$

En ese dominio podemos escribir

$$
x-9
=(\sqrt{x})^2-3^2
=(\sqrt{x}-3)(\sqrt{x}+3).
$$

Por tanto,

$$
B(x)
=
\frac{(\sqrt{x}-3)(\sqrt{x}+3)}{\sqrt{x}-3}
=
\sqrt{x}+3,
$$

porque $\sqrt{x}-3\neq0$ en el dominio original. Así,

$$
\boxed{
B(x)=\sqrt{x}+3,
\qquad x\ge0,
\quad x\neq9.
}
$$

La fórmula final está definida también en $x=9$, pero la expresión inicial no. El ejercicio combina la raíz principal de C18 con una diferencia de cuadrados de C19. Sin embargo, la expresión original no es racional en la terminología de C20 porque contiene un radical en el denominador.


### Solución 69

La expresión es

$$
D(x,h)=
\frac{\dfrac1{x+h}-\dfrac1x}{h}.
$$

Trabajamos con pares reales $(x,h)$. Antes de operar registramos todas las restricciones:

$$
x+h\neq0,
\qquad
x\neq0,
\qquad
h\neq0.
$$

Combinamos primero las fracciones internas:

$$
\frac1{x+h}-\frac1x
=
\frac{x-(x+h)}{x(x+h)}
=
\frac{-h}{x(x+h)}.
$$

Entonces

$$
D(x,h)
=
\frac{-h}{x(x+h)}\cdot\frac1h.
$$

Como $h\neq0$ pertenece al dominio original, cancelamos $h$:

$$
\boxed{
D(x,h)
=
-\frac1{x(x+h)},
\qquad
x\neq0,
\quad x+h\neq0,
\quad h\neq0.
}
$$

La forma final ya no muestra la condición $h\neq0$, pero esa restricción procede de la división exterior original y debe conservarse.


### Solución 70

Partimos de

$$
E(x,h)=
\frac{(x+h)^2-x^2}{h}.
$$

La única restricción original es

$$
h\neq0.
$$

Podemos expandir el numerador:

$$
(x+h)^2-x^2
=
x^2+2xh+h^2-x^2
=
h(2x+h).
$$

Pero la diferencia de cuadrados muestra la estructura más directamente:

$$
(x+h)^2-x^2
=
\bigl((x+h)-x\bigr)\bigl((x+h)+x\bigr)
=
h(2x+h).
$$

Esta segunda ruta hace visible de inmediato el factor que podrá cancelarse. Como $h\neq0$,

$$
E(x,h)
=
\frac{h(2x+h)}h
=
2x+h.
$$

Por tanto,

$$
\boxed{
E(x,h)=2x+h,
\qquad h\neq0.
}
$$

Ambas rutas son válidas, pero la factorización estructural evita una expansión que luego tendría que reorganizarse. La restricción $h\neq0$ no aparece en la fórmula final y, sin embargo, sigue siendo parte de la afirmación completa.


### Solución 71

La expresión es

$$
G(x,h)=
\frac{\dfrac1{(x+h)^2}-\dfrac1{x^2}}{h}.
$$

El dominio original exige simultáneamente

$$
x+h\neq0,
\qquad
x\neq0,
\qquad
h\neq0.
$$

Combinamos las fracciones internas:

$$
\frac1{(x+h)^2}-\frac1{x^2}
=
\frac{x^2-(x+h)^2}{x^2(x+h)^2}.
$$

Antes de expandir, factorizamos el numerador como diferencia de cuadrados:

$$
x^2-(x+h)^2
=
\bigl(x-(x+h)\bigr)\bigl(x+(x+h)\bigr)
=
(-h)(2x+h).
$$

Por tanto,

$$
G(x,h)
=
\frac{-h(2x+h)}{x^2(x+h)^2}\cdot\frac1h.
$$

Como $h\neq0$ forma parte del dominio original, cancelamos $h$ y obtenemos

$$
\boxed{
G(x,h)
=
-\frac{2x+h}{x^2(x+h)^2},
\qquad
x\neq0,
\quad x+h\neq0,
\quad h\neq0.
}
$$

La factorización antes de cancelar evita perder el signo negativo. La condición $h\neq0$ deja de ser visible en la fórmula final, pero sigue heredada de la división exterior.


### Solución 72

Tenemos

$$
f(x)=\frac{x+1}{x-1}
$$

y

$$
C(x,h)=
\frac{
\dfrac{x+h+1}{x+h-1}
-
\dfrac{x+1}{x-1}
}{h}.
$$

El dominio original exige tres condiciones independientes:

$$
x\neq1,
\qquad
x+h\neq1,
\qquad
h\neq0.
$$

Las dos primeras garantizan que $f(x)$ y $f(x+h)$ estén definidos; la tercera procede de la división exterior.

Construimos el denominador común conservando completos los dos numeradores:

$$
\frac{x+h+1}{x+h-1}
-
\frac{x+1}{x-1}
=
\frac{
(x+h+1)(x-1)
-
(x+1)(x+h-1)
}
{(x+h-1)(x-1)}.
$$

Ahora simplificamos el numerador. Tenemos

$$
(x+h+1)(x-1)=x^2+xh-h-1
$$

y

$$
(x+1)(x+h-1)=x^2+xh+h-1.
$$

Por tanto,

$$
(x+h+1)(x-1)-(x+1)(x+h-1)
=-2h.
$$

Así,

$$
C(x,h)
=
\frac{-2h}{(x+h-1)(x-1)}\cdot\frac1h.
$$

Como $h\neq0$, cancelamos $h$ y obtenemos

$$
\boxed{
C(x,h)
=
-\frac{2}{(x-1)(x+h-1)},
\qquad
x\neq1,
\quad x+h\neq1,
\quad h\neq0.
}
$$

Las condiciones $x\neq1$ y $x+h\neq1$ siguen visibles en el denominador final. En cambio, $h\neq0$ desaparece después de la cancelación y debe conservarse por procedencia. Nada en este cálculo utiliza límites ni derivadas: se trata únicamente de una identidad algebraica sobre el dominio declarado.


## G. Síntesis avanzada

En estas soluciones la meta no es encontrar una técnica dominante, sino cerrar la cadena completa: **dominio original, elección de representación, transformación justificada, verificación e interpretación de la forma final**. Cuando una restricción desaparece de la escritura, se conserva por procedencia; cuando una ruta alternativa es correcta pero menos eficiente, se distingue estrategia de validez.


### Solución 73

Consideramos

$$
E(x)=
\left(
\frac{x^2-1}{x-1}
\cdot
\frac{x-2}{x+1}
\right)
\div
\frac{x-2}{x+3}.
$$

Antes de operar fijamos el dominio original.

La primera fracción exige

$$
x\neq1.
$$

La segunda exige

$$
x\neq-1.
$$

El divisor $(x-2)/(x+3)$ debe estar definido, de modo que

$$
x\neq-3,
$$

y además debe ser distinto de cero. Bajo $x\neq-3$, se anula en

$$
x=2.
$$

Por tanto,

$$
\operatorname{Dom}(E)
=
\mathbb R\setminus\{-3,-1,1,2\}.
$$

Las exclusiones tienen dos tipos de procedencia:

- $x=1$ y $x=-1$ provienen de denominadores internos del bloque multiplicativo;
- $x=-3$ hace indefinido al divisor;
- $x=2$ hace que el divisor completo exista pero valga cero.

Ahora elegimos una ruta que conserve visibles los factores. Factorizamos

$$
x^2-1=(x-1)(x+1).
$$

Así,

$$
\frac{x^2-1}{x-1}
\cdot
\frac{x-2}{x+1}
=
\frac{(x-1)(x+1)}{x-1}
\cdot
\frac{x-2}{x+1}.
$$

En el dominio original, $x-1$ y $x+1$ son no nulos. Cancelamos ambos factores y obtenemos

$$
x-2.
$$

La expresión completa queda

$$
E(x)
=
(x-2)
\div
\frac{x-2}{x+3}.
$$

Como el divisor es no nulo en el dominio original, invertimos:

$$
E(x)
=
(x-2)\frac{x+3}{x-2}.
$$

También $x-2\neq0$ en el dominio original, por lo que

$$
\boxed{
E(x)=x+3,
\qquad
x\neq-3,-1,1,2.
}
$$

La forma final es polinómica y está definida para todo real, pero las cuatro exclusiones continúan perteneciendo a la expresión de procedencia.

Los puntos $x=1$ y $x=2$ muestran dos mecanismos distintos. En $x=1$, la primera fracción original contiene división por cero. En $x=2$, las fracciones internas están definidas, pero el divisor completo vale cero. En ambos casos la fórmula final $x+3$ tiene sentido. Por eso el dominio original no puede reconstruirse desde el resultado simplificado.


### Solución 74

Sea

$$
Q(x)=
\frac{x+3}{x-2}
\div
\frac{x^2-1}{x-1}.
$$

La Ruta A comienza por el dominio completo.

El dividendo exige

$$
x\neq2.
$$

El divisor exige $x\neq1$ para estar definido. Además, debe ser distinto de cero. Factorizamos su numerador:

$$
x^2-1=(x-1)(x+1).
$$

En el dominio $x\neq1$, el divisor se anula exactamente cuando

$$
x+1=0,
$$

es decir, en $x=-1$. Por tanto,

$$
\operatorname{Dom}(Q)
=
\mathbb R\setminus\{-1,1,2\}.
$$

Ahora, y sólo ahora, simplificamos el divisor:

$$
\frac{x^2-1}{x-1}
=
\frac{(x-1)(x+1)}{x-1}
=
x+1,
\qquad x\neq1.
$$

Entonces

$$
Q(x)
=
\frac{x+3}{x-2}
\div
(x+1)
=
\frac{x+3}{(x-2)(x+1)}.
$$

La conclusión de la Ruta A es

$$
\boxed{
Q(x)=
\frac{x+3}{(x-2)(x+1)},
\qquad
x\neq-1,1,2.
}
$$

La Ruta B simplifica inmediatamente el divisor a $x+1$ y después reconstruye sus restricciones mirando sólo esa forma. Así detectaría $x\neq-1$ por la no nulidad del divisor y $x\neq2$ por el dividendo, pero perdería

$$
x\neq1.
$$

Las manipulaciones posteriores pueden ser algebraicamente correctas sobre el dominio ampliado que la Ruta B está usando, y producir la misma fórmula visible

$$
\frac{x+3}{(x-2)(x+1)}.
$$

Sin embargo, su afirmación completa sería incorrecta si declarara únicamente

$$
x\neq-1,2.
$$

La información perdida es la restricción $x\neq1$ perteneciente al **dominio de procedencia del divisor antes de simplificarlo**.

Por tanto, las dos rutas pueden llegar a la misma fórmula, pero sólo la Ruta A conserva el dominio original completo.


### Solución 75

Consideramos

$$
F_{a,b}(x)=
\frac{
\dfrac1{x-a}+\dfrac1{x-b}
}{
\dfrac1{x-a}-\dfrac1{x-b}
},
$$

con $a,b\in\mathbb R$ fijos.

Debemos separar los casos $a\neq b$ y $a=b$ porque cambia la estructura del denominador exterior.

#### Caso 1: $a\neq b$

Las fracciones internas exigen

$$
x\neq a,
\qquad
x\neq b.
$$

Sobre ese dominio, el numerador exterior es

$$
\frac1{x-a}+\frac1{x-b}
=
\frac{(x-b)+(x-a)}{(x-a)(x-b)}
=
\frac{2x-a-b}{(x-a)(x-b)}.
$$

El denominador exterior es

$$
\frac1{x-a}-\frac1{x-b}
=
\frac{(x-b)-(x-a)}{(x-a)(x-b)}
=
\frac{a-b}{(x-a)(x-b)}.
$$

Como $a\neq b$, el numerador constante $a-b$ no es cero. Por tanto, el denominador exterior nunca se anula en el dominio donde está definido y no añade una exclusión nueva.

Así,

$$
\operatorname{Dom}(F_{a,b})
=
\mathbb R\setminus\{a,b\},
\qquad a\neq b.
$$

Ejecutamos la división exterior:

$$
F_{a,b}(x)
=
\frac{\dfrac{2x-a-b}{(x-a)(x-b)}}
     {\dfrac{a-b}{(x-a)(x-b)}}.
$$

Como $(x-a)(x-b)\neq0$ en el dominio original,

$$
\boxed{
F_{a,b}(x)
=
\frac{2x-a-b}{a-b},
\qquad
x\neq a,b,
\quad a\neq b.
}
$$

La fórmula final es afín en $x$ y ya no muestra ninguna de las dos exclusiones.

#### Caso 2: $a=b$

Ahora las dos restricciones simbólicas

$$
x\neq a,
\qquad
x\neq b
$$

describen un único punto, porque $a=b$.

Pero aparece un fenómeno más fuerte. Para todo $x\neq a$,

$$
\frac1{x-a}-\frac1{x-a}=0.
$$

Es decir, el denominador exterior completo vale cero **en todo punto donde las fracciones internas están definidas**.

Por tanto, no existe ningún valor real admisible:

$$
\boxed{
\operatorname{Dom}(F_{a,a})=\varnothing.
}
$$

En este caso no hay una fórmula simplificada que represente a la fracción compleja sobre un dominio no vacío: la división exterior nunca está definida.

La distinción entre «dos restricciones simbólicas» y «dos puntos distintos» sigue siendo importante, pero aquí no basta con fusionar $\{a,b\}$ en $\{a\}$; también debemos comprobar la no nulidad del denominador exterior, que elimina todos los puntos restantes.


### Solución 76

Queremos construir una expresión racional cuyo dominio original sea exactamente

$$
\mathbb R\setminus\{-2,3\}
$$

y cuya forma simplificada sea

$$
x^2+1.
$$

Una construcción directa es

$$
R(x)
=
\frac{(x^2+1)(x+2)(x-3)}
     {(x+2)(x-3)}.
$$

El numerador y el denominador son ambos no constantes. El denominador se anula exactamente cuando

$$
x=-2
\qquad\text{o}\qquad
x=3.
$$

Por tanto,

$$
\operatorname{Dom}(R)
=
\mathbb R\setminus\{-2,3\}.
$$

En ese dominio, los factores $x+2$ y $x-3$ son no nulos y pueden cancelarse:

$$
R(x)
=
\frac{(x^2+1)(x+2)(x-3)}
     {(x+2)(x-3)}
=
x^2+1.
$$

Así,

$$
\boxed{
R(x)=x^2+1,
\qquad x\neq-2,3.
}
$$

No aparece ninguna exclusión adicional: todos los ceros del denominador son precisamente los dos prescritos.

La función polinómica natural

$$
p:\mathbb R\to\mathbb R,
\qquad
p(x)=x^2+1,
$$

no es la misma función que la función natural definida por $R$, porque sus dominios son distintos. Coinciden en todos los puntos de $\mathbb R\setminus\{-2,3\}$, pero $p$ también está definida en $-2$ y $3$, mientras que $R$ no.


### Solución 77

La expresión es

$$
S(x)=
\frac1{x(x-1)^2}
+
\frac2{x^2(x-1)}
-
\frac3{x(x-1)^3}.
$$

Todos los denominadores contienen sólo los factores $x$ y $x-1$. Por tanto,

$$
\operatorname{Dom}(S)
=
\mathbb R\setminus\{0,1\}.
$$

#### Comparación de denominadores comunes

El **plan bruto** multiplica los tres denominadores:

$$
x(x-1)^2
\cdot
x^2(x-1)
\cdot
x(x-1)^3
=
x^4(x-1)^6.
$$

Ese denominador es común y es válido sobre el mismo dominio original, pero repite muchas copias innecesarias.

El **plan estructural** conserva la mayor potencia necesaria de cada factor:

- para $x$, la mayor potencia es $x^2$;
- para $x-1$, la mayor potencia es $(x-1)^3$.

Por tanto elegimos

$$
L=x^2(x-1)^3.
$$

Reescribimos cada término.

Para el primero falta el factor $x(x-1)$:

$$
\frac1{x(x-1)^2}
=
\frac{x(x-1)}{x^2(x-1)^3}.
$$

Para el segundo falta $(x-1)^2$:

$$
\frac2{x^2(x-1)}
=
\frac{2(x-1)^2}{x^2(x-1)^3}.
$$

Para el tercero falta $x$:

$$
\frac3{x(x-1)^3}
=
\frac{3x}{x^2(x-1)^3}.
$$

Estas tres reescrituras pueden verificarse por recomposición: en el dominio $x\neq0,1$, cancelando respectivamente $x(x-1)$, $(x-1)^2$ y $x$ se recuperan exactamente las fracciones originales.

Ahora combinamos:

$$
S(x)
=
\frac{x(x-1)+2(x-1)^2-3x}
     {x^2(x-1)^3}.
$$

Simplificamos el numerador:

$$
x(x-1)+2(x-1)^2-3x
=
x^2-x+2x^2-4x+2-3x
=
3x^2-8x+2.
$$

No aparece un factor $x$ ni $x-1$ que pueda cancelarse. Por tanto,

$$
\boxed{
S(x)
=
\frac{3x^2-8x+2}{x^2(x-1)^3},
\qquad x\neq0,1.
}
$$

Los dos planes pueden ser algebraicamente válidos sobre el mismo dominio. La ventaja del plan estructural no es lógica sino estratégica: evita introducir $x^4(x-1)^6$ y reduce drásticamente la cantidad de productos y simplificaciones posteriores.


### Solución 78

Consideramos

$$
R(x)=
\frac{\sqrt{x-1}}{x-1}
\div
\frac{\sqrt{x-1}-2}{\sqrt{x-1}}.
$$

Leemos las restricciones en tres capas.

Primero, la raíz principal exige

$$
x-1\ge0,
$$

es decir,

$$
x\ge1.
$$

Segundo, el denominador $x-1$ de la primera fracción debe ser no nulo y el denominador $\sqrt{x-1}$ del divisor también debe ser no nulo. Ambas condiciones fuerzan

$$
x>1.
$$

Tercero, el divisor completo debe ser distinto de cero. En $x>1$, su denominador ya es no nulo, así que se anula exactamente cuando

$$
\sqrt{x-1}-2=0.
$$

Esto ocurre cuando

$$
\sqrt{x-1}=2,
$$

y por tanto

$$
x=5.
$$

Así,

$$
\operatorname{Dom}(R)
=
(1,\infty)\setminus\{5\}.
$$

Sólo ahora invertimos el divisor:

$$
R(x)
=
\frac{\sqrt{x-1}}{x-1}
\cdot
\frac{\sqrt{x-1}}{\sqrt{x-1}-2}.
$$

Como

$$
x-1=\left(\sqrt{x-1}\right)^2
$$

para $x\ge1$, el numerador total de los dos primeros factores contiene precisamente $x-1$:

$$
\sqrt{x-1}\,\sqrt{x-1}=x-1.
$$

Por tanto, sobre el dominio original,

$$
R(x)
=
\frac{x-1}
     {(x-1)(\sqrt{x-1}-2)}
=
\frac1{\sqrt{x-1}-2}.
$$

Así,

$$
\boxed{
R(x)=
\frac1{\sqrt{x-1}-2},
\qquad
x>1,
\quad x\neq5.
}
$$

La fórmula final tiene dominio natural

$$
[1,\infty)\setminus\{5\},
$$

porque en $x=1$ vale $-1/2$. Ese punto, sin embargo, no pertenecía al dominio original: allí los denominadores $x-1$ y $\sqrt{x-1}$ se anulaban.

La expresión de partida es fraccionaria, pero no racional en el sentido de [§20.2](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md#apm-c20-s02), porque contiene radicales y no es un cociente de polinomios.


### Solución 79

Partimos de

$$
T(x)=
\left(
\frac{x^2-1}{x-1}
\div
\frac{x+1}{x+2}
\right)
\frac{x+2}{x+3}
-
\frac1{x+3}.
$$

Antes de auditar la cadena fijamos el dominio original.

La primera fracción exige

$$
x\neq1.
$$

El divisor $(x+1)/(x+2)$ exige

$$
x\neq-2
$$

para estar definido y

$$
x\neq-1
$$

para ser no nulo.

El factor $(x+2)/(x+3)$ y el último término exigen

$$
x\neq-3.
$$

Por tanto,

$$
\operatorname{Dom}(T)
=
\mathbb R\setminus\{-3,-2,-1,1\}.
$$

Ahora auditamos la cadena propuesta.

La factorización

$$
x^2-1=(x-1)(x+1)
$$

es correcta. También es correcto pasar de

$$
\frac{(x-1)(x+1)}{x-1}
$$

a

$$
x+1
$$

sobre el dominio vigente, porque $x\neq1$.

La **primera ruptura** aparece en la transición

$$
(x+1)
\div
\frac{x+1}{x+2}
\longmapsto
(x+1)\frac{x+1}{x+2}.
$$

Al transformar una división en multiplicación debía invertirse el **divisor completo**. El recíproco correcto es

$$
\frac{x+2}{x+1}.
$$

Desde la expresión equivocada obtenida en esa línea, varias operaciones posteriores del estudiante —multiplicar fracciones, cancelar $x+2$, combinar sobre $x+3$ y expandir— pueden ser algebraicamente correctas. Pero ya describen otra expresión. La equivalencia con $T$ se perdió en la primera inversión incorrecta.

Reparamos desde ese punto:

$$
T(x)
=
(x+1)
\frac{x+2}{x+1}
\frac{x+2}{x+3}
-
\frac1{x+3}.
$$

Como $x\neq-1$, cancelamos $x+1$:

$$
T(x)
=
\frac{(x+2)^2}{x+3}
-
\frac1{x+3}.
$$

Combinamos:

$$
T(x)
=
\frac{(x+2)^2-1}{x+3}.
$$

Factorizamos la diferencia de cuadrados:

$$
(x+2)^2-1
=
\bigl((x+2)-1\bigr)\bigl((x+2)+1\bigr)
=
(x+1)(x+3).
$$

Como $x\neq-3$, cancelamos $x+3$:

$$
\boxed{
T(x)=x+1,
\qquad
x\neq-3,-2,-1,1.
}
$$

La cadena defectuosa terminaba en

$$
\frac{x(x+2)}{x+3},
$$

que no coincide con el resultado correcto. Por ejemplo, $x=0$ pertenece al dominio original: la expresión correcta vale $1$, mientras que la forma defectuosa vale $0$.

Ese control puntual detecta la discrepancia, pero la causa matemática ya quedó localizada antes: la primera inversión del divisor fue incorrecta.


### Solución 80

Consideramos

$$
S(x)=
\left(
\frac{x^2-9}{x^2-x-6}
\div
\frac{x+3}{x-2}
\right)
+
\frac4{x+2}.
$$

#### 1. Lectura por bloques y dominio

El primer bloque es un cociente entre dos expresiones racionales; después aparece una suma con $4/(x+2)$.

Factorizamos el denominador del dividendo sólo para leer sus restricciones:

$$
x^2-x-6=(x-3)(x+2).
$$

Por tanto, el dividendo exige

$$
x\neq3,
\qquad
x\neq-2.
$$

El divisor $(x+3)/(x-2)$ exige

$$
x\neq2
$$

para estar definido y

$$
x\neq-3
$$

para ser no nulo.

El último sumando vuelve a exigir $x\neq-2$.

Así,

$$
\operatorname{Dom}(S)
=
\mathbb R\setminus\{-3,-2,2,3\}.
$$

#### 2. Primera ruta: simplificar el dividendo antes de invertir

Factorizamos también el numerador:

$$
x^2-9=(x-3)(x+3).
$$

Sobre el dominio original,

$$
\frac{x^2-9}{x^2-x-6}
=
\frac{(x-3)(x+3)}{(x-3)(x+2)}
=
\frac{x+3}{x+2}.
$$

La restricción $x\neq3$ debe seguir viajando con este bloque aunque haya desaparecido de su fórmula visible.

Ahora ejecutamos la división:

$$
\frac{x+3}{x+2}
\div
\frac{x+3}{x-2}
=
\frac{x+3}{x+2}
\cdot
\frac{x-2}{x+3}.
$$

Como $x\neq-3$, cancelamos $x+3$:

$$
\frac{x-2}{x+2}.
$$

La suma final tiene ya denominador común $x+2$:

$$
S(x)
=
\frac{x-2}{x+2}
+
\frac4{x+2}
=
\frac{x+2}{x+2}.
$$

Como $x\neq-2$,

$$
\boxed{
S(x)=1,
\qquad
x\neq-3,-2,2,3.
}
$$

#### 3. Segunda ruta: invertir antes de simplificar el dividendo

Partimos del mismo dominio original y transformamos primero la división en producto:

$$
S(x)
=
\frac{x^2-9}{x^2-x-6}
\cdot
\frac{x-2}{x+3}
+
\frac4{x+2}.
$$

Ahora factorizamos:

$$
x^2-9=(x-3)(x+3),
$$

$$
x^2-x-6=(x-3)(x+2).
$$

Entonces

$$
S(x)
=
\frac{(x-3)(x+3)}{(x-3)(x+2)}
\cdot
\frac{x-2}{x+3}
+
\frac4{x+2}.
$$

En el dominio original, $x-3$ y $x+3$ son no nulos. Cancelamos:

$$
S(x)
=
\frac{x-2}{x+2}
+
\frac4{x+2}
=
1.
$$

Las dos rutas producen la misma fórmula sobre el mismo dominio. La primera hace más visible la historia del bloque simplificado; la segunda exhibe directamente todas las cancelaciones dentro de un único producto. Ninguna es válida sin el dominio fijado al comienzo.

#### 4. Interpretación y verificación

La forma final $1$ tiene dominio natural $\mathbb R$, por lo que **todas** las restricciones originales han quedado ocultas:

$$
x\neq-3,-2,2,3.
$$

Cada una sigue siendo necesaria por procedencia.

Como control adicional podemos evaluar en un punto permitido, por ejemplo $x=0$. La expresión original da

$$
\left(
\frac{-9}{-6}
\div
\frac3{-2}
\right)
+
\frac42
=
\left(
\frac32\div-\frac32
\right)+2
=
-1+2
=
1.
$$

Coincide con la forma final. Esta comprobación puntual puede detectar un error, pero no demuestra la identidad general. La equivalencia para todo $x$ del dominio original está justificada por las dos cadenas algebraicas anteriores.

## H. Soluciones de profundización y reconstrucción



#### Solución 081

El denominador debe anularse en los dos reales distintos, así no puede ser constante ni lineal. El grado mínimo es dos y el único denominador mónico cuadrático con esos ceros es $D=(x-a)(x-b)$. La identidad formal impuesta fija entonces $N=(x+1)(x-a)(x-b)$ de manera única. Para comprobar la unicidad sin usar el futuro teorema del resto, comparar un denominador $x^2+ux+v$ en los dos ceros y restar las ecuaciones da $u=-(a+b)$, $v=ab$. La fracción construida tiene exactamente los dos huecos y cancela a $x+1$ en su dominio.



#### Solución 082

Tomemos $R=[(x-a)/(x-b)]\div[(x-a)/(x-b)^2]$. Ambas fracciones exigen $x\ne b$; la segunda, como divisor, debe ser no nula y exige $x\ne a$. Allí invertirla produce $[(x-a)/(x-b)][(x-b)^2/(x-a)]=x-b$. La multiplicación inversa comprueba el cálculo. En $a$ la segunda fracción es cero; en $b$ está indefinida. Son dos razones diferentes que deben conservarse aunque la fórmula final sea polinómica.



#### Solución 083

Si $a\ne b$, el dominio es $x\ne a,b$. La resta es $(a-b)/[(x-a)(x-b)]$, idéntica al divisor no nulo, así que $E=1$. Invertir primero da $[1/(x-a)-1/(x-b)](x-a)(x-b)/(a-b)=[(x-b)-(x-a)]/(a-b)=1$. Ambas rutas usan las mismas tres condiciones no nulas. Si $a=b$, el divisor es cero en todos los puntos donde está definido, luego el dominio completo es vacío. No existe entonces una función constante obtenida por cancelación.



#### Solución 084

El dominio exige $x\ne0,a$. La segunda fracción vale $1$ allí; la primera es $|x|/x$. Para $x>0$ resulta $1$ y para $x<0$ resulta $-1$, siempre quitando $a$ si pertenece a la región. Si $a=0$, las dos exclusiones coinciden y solo se retira cero. Una ruta por casos sustituye desde el principio $\sqrt{x^2}$ por $x$ o $-x$ y llega a los mismos valores. Sustituir siempre por $x$ falla en cada punto negativo permitido.



#### Solución 085

En el caso genérico los tres factores distintos requieren $D=(x-t)(x+t)(x-1)$ y $F_t=2x/[(x^2-t^2)(x-1)]$, con $x\ne t,-t,1$. Si $t=0$, ambas fracciones son iguales y $F_0=2/[x(x-1)]$, con $x\ne0,1$. Si $t=1$ o $-1$, los sumandos tienen denominadores $(x-1)^2$ y $(x+1)(x-1)$, en orden intercambiado: $F_t=2x/[(x-1)^2(x+1)]$, con $x\ne\pm1$. La suma reconstruye cada numerador; tomar solo factores distintos en los últimos casos perdería la potencia necesaria.



#### Solución 086

Como $t-x=-(x-t)$, los dos primeros términos suman cero sobre $x\ne t$. Queda $1/(x+t)$, conservando $x\ne t,-t$. Para $t\ne0$, la fórmula final solo excluye $-t$ y ocultó el hueco $t$. Para $t=0$, ambas exclusiones coinciden y el dominio sigue siendo $x\ne0$, igual al natural final. Reunir los dos primeros términos con denominador $x-t$ produce numerador $1-1=0$, una verificación sin atribuir cancelación a una suma.



#### Solución 087

Se canceló un sumando, no un factor del numerador completo. Las fracciones interiores requieren $x,y\ne0$ y el denominador exterior exige $y-x\ne0$. Multiplicar ambos bloques por $xy\ne0$ da $(x+y)/(y-x)$ sobre ese dominio. Como comprobación, $x=1,y=2$ da $3$, refutando la constante propuesta. La reconstrucción $(1/x-1/y)(x+y)/(y-x)=(x+y)/(xy)=1/x+1/y$ certifica la igualdad en todos los puntos permitidos, no solo en el ejemplo.



#### Solución 088

Se exigen $x\ne0,-a$ por el primer denominador, y $x\ne a$ porque el divisor debe ser no nulo. En ese dominio el primer bloque es $(x-a)/x$; dividido por el segundo vale $1$. Queda $H=1-a/x=(x-a)/x$, con $x\notin\{0,a,-a\}$. Si $a=0$, solo se excluye cero y el resultado es $1$. Para reconstruir, la suma de la forma final y $a/x$ es $1$; multiplicada por el divisor devuelve $(x-a)/x$, que al multiplicar por $x(x+a)$ devuelve $x^2-a^2$. Cada multiplicación usa los denominadores ya registrados.

***

[← Capítulo 19](algebra-para-matematicos-capitulo-19-identidades-productos-notables-y-factorizacion.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 21 →](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md)
