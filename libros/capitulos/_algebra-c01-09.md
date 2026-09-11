## §9. Errores que parecen álgebra

Aprender álgebra no consiste únicamente en conocer reglas correctas.

También debemos aprender a reconocer transformaciones que **parecen** razonables pero no conservan el valor.

Consideremos:

$$
(a+b)^2=a^2+b^2.
$$

La escritura resulta tentadora.

Alguien podría pensar:

> «el cuadrado afecta a todo lo que está dentro del paréntesis, así que elevo al cuadrado cada término».

Pero esa explicación confunde la estructura de una potencia con la estructura de una suma.

La expresión:

$$
(a+b)^2
$$

significa:

$$
(a+b)(a+b),
$$

no:

$$
a^2+b^2.
$$

Si tomamos:

$$
a=1,
\qquad
b=1,
$$

obtenemos:

$$
(a+b)^2=(1+1)^2=4,
$$

mientras que:

$$
a^2+b^2=1^2+1^2=2.
$$

Por tanto:

$$
4\ne2.
$$

La supuesta regla es falsa.

Este ejemplo muestra una estrategia que usaremos durante toda la sección:

1. identificar la regla aparente;
2. localizar la estructura que se ha ignorado;
3. buscar un caso numérico sencillo;
4. escribir la regla correcta, cuando exista.

::: {.ma-block .ma-intuicion}
**Idea clave**

Un paso algebraico no se vuelve correcto porque se parezca a una regla conocida. Debe respetar exactamente la estructura a la que esa regla se aplica.
:::

---

### 9.1 Primer error: distribuir una potencia sobre una suma

La falsa regla es:

$$
(a+b)^2=a^2+b^2.
$$

#### Qué parece haberse hecho

Se ha tratado la potencia como si pudiera distribuirse sobre la suma.

#### Qué estructura se ignoró

Un cuadrado significa multiplicar una expresión por sí misma:

$$
(a+b)^2=(a+b)(a+b).
$$

Ahora sí podemos usar distributividad:

$$
\begin{aligned}
(a+b)(a+b)
&=a(a+b)+b(a+b)\\
&=a^2+ab+ab+b^2\\
&=a^2+2ab+b^2.
\end{aligned}
$$

Por tanto:

$$
\boxed{
(a+b)^2=a^2+2ab+b^2.
}
$$

El término:

$$
2ab
$$

no aparece por un detalle accidental. Surge de los dos productos cruzados:

$$
ab
\qquad\text{y}\qquad
ba.
$$

#### Contraejemplo

Con:

$$
a=b=1,
$$

la regla falsa daría:

$$
4=2.
$$

Un solo caso donde falla basta para saber que no puede ser una identidad.

---

### 9.2 Segundo error: cancelar dentro de una suma

Consideremos:

$$
\frac{a+b}{a}=b.
$$

Podría imaginarse un razonamiento como:

> «hay una $a$ arriba y una $a$ abajo; las cancelo».

Pero en el numerador:

$$
a+b
$$

la letra $a$ no es un factor de toda la suma.

Es solamente uno de sus términos.

La fracción puede separarse, siempre que $a\ne0$:

$$
\frac{a+b}{a}
=
\frac aa+\frac ba
=
1+\frac ba.
$$

No obtenemos $b$.

#### Contraejemplo

Tomemos:

$$
a=2,
\qquad
b=4.
$$

Entonces:

$$
\frac{a+b}{a}
=
\frac{2+4}{2}
=
3,
$$

mientras que:

$$
b=4.
$$

Por tanto:

$$
3\ne4.
$$

La supuesta cancelación es falsa.

La lección estructural es:

$$
\boxed{
\text{se cancelan factores comunes, no términos aislados dentro de una suma}.
}
$$

---

### 9.3 Qué significa cancelar correctamente

Consideremos ahora:

$$
\frac{a(b+1)}{a}.
$$

Si:

$$
a\ne0,
$$

el numerador completo tiene al factor $a$:

$$
a(b+1).
$$

Podemos escribir:

$$
\frac{a(b+1)}{a}
=
\frac{a}{a}(b+1)
=
b+1.
$$

Aquí sí existe un factor común entre numerador y denominador.

Comparemos:

$$
\frac{a(b+1)}{a}
$$

con:

$$
\frac{a+b}{a}.
$$

En la primera, el numerador es un producto:

$$
a\cdot(b+1).
$$

En la segunda, el numerador es una suma:

$$
a+b.
$$

La diferencia no es visualmente enorme, pero estructuralmente es decisiva.

---

### 9.4 Tercer error: sumar términos que no tienen la misma estructura

Consideremos:

$$
2+3x=5x.
$$

Alguien podría haber sumado:

$$
2+3=5
$$

y conservado la letra $x$.

Pero el término:

$$
2
$$

no contiene el factor $x$.

En cambio:

$$
2x+3x
$$

sí puede transformarse:

$$
2x+3x
=
(2+3)x
=
5x.
$$

La distributividad explica por qué.

No existe una transformación análoga para:

$$
2+3x.
$$

#### Contraejemplo

Tomemos:

$$
x=0.
$$

El lado izquierdo vale:

$$
2+3\cdot0=2.
$$

El lado derecho vale:

$$
5\cdot0=0.
$$

Por tanto:

$$
2\ne0.
$$

La igualdad propuesta es falsa.

::: {.ma-block .ma-intuicion}
**Idea clave**

«Términos semejantes» no significa «términos que están uno al lado del otro». La posibilidad de reunirlos debe venir de una estructura común, como un factor compartido.
:::

---

### 9.5 Cuarto error: cancelar expresiones que aparecen sumando

Consideremos:

$$
\frac{x+3}{x+5}.
$$

Un estudiante podría intentar «cancelar las $x$» y escribir:

$$
\frac{x+3}{x+5}
=
\frac35.
$$

Pero las $x$ no son factores de numerador y denominador.

Son términos dentro de dos sumas distintas.

#### Contraejemplo

Tomemos:

$$
x=1.
$$

Entonces:

$$
\frac{x+3}{x+5}
=
\frac46
=
\frac23,
$$

mientras que:

$$
\frac35
$$

es otro número.

Por tanto:

$$
\frac23\ne\frac35.
$$

La cancelación es inválida.

---

### 9.6 Ejemplo desarrollado: qué puede cancelarse

::: {.ma-block .ma-observacion #apm-t1-c01-x0007}
**Ejemplo — Cancelar factores, no términos**

:::

Comparemos dos expresiones.

#### Caso A

$$
\frac{x(x+3)}{x}.
$$

Suponiendo:

$$
x\ne0,
$$

el numerador es un producto:

$$
x\cdot(x+3).
$$

Por tanto:

$$
\frac{x(x+3)}{x}
=
\frac{x}{x}(x+3)
=
x+3.
$$

La cancelación es válida porque $x$ es factor de todo el numerador y también del denominador.

#### Caso B

$$
\frac{x+3}{x}.
$$

Aquí el numerador no es:

$$
x\cdot3.
$$

Es una suma:

$$
x+3.
$$

Por tanto no podemos cancelar la $x$ como si fuera un factor común.

Si $x\ne0$, podemos escribir:

$$
\frac{x+3}{x}
=
\frac xx+\frac3x
=
1+\frac3x.
$$

#### Comparación

La diferencia estructural es:

$$
\boxed{x(x+3)}
$$

frente a:

$$
\boxed{x+3}.
$$

En el primer caso, $x$ es factor del numerador completo.

En el segundo, $x$ es solamente un término de la suma.

Por eso, la regla práctica es:

$$
\boxed{
\text{una cancelación legítima exige un factor común no nulo}
}
$$

en el numerador y el denominador.

---

### 9.7 Un contraejemplo no explica todo, pero decide mucho

Supongamos que alguien propone:

$$
(a-b)^2=a^2-b^2.
$$

Podemos elegir:

$$
a=2,
\qquad
b=1.
$$

Entonces:

$$
(a-b)^2=1,
$$

mientras que:

$$
a^2-b^2=3.
$$

Así:

$$
1\ne3.
$$

Ya sabemos que la supuesta identidad es falsa.

Pero el contraejemplo no nos dice por sí solo **por qué** alguien cometió el error.

Para comprenderlo debemos volver a la estructura:

$$
(a-b)^2
=
(a-b)(a-b),
$$

y distribuir:

$$
(a-b)^2
=
a^2-2ab+b^2.
$$

Por tanto, debemos distinguir dos funciones del contraejemplo:

- **refutar** una afirmación general falsa;
- **diagnosticar**, junto con el análisis estructural, el origen del error.

Esta sección usa ambas funciones de manera informal.

---

### 9.8 Una regla verdadera puede usarse en el lugar equivocado

Muchos errores no consisten en inventar una regla completamente nueva.

Consisten en tomar una regla verdadera y aplicarla donde no corresponde.

Por ejemplo, la distributividad dice:

$$
a(b+c)=ab+ac.
$$

Pero de ahí no se sigue:

$$
(a+b)^2=a^2+b^2.
$$

La cancelación de un factor común puede ser válida:

$$
\frac{ab}{a}=b
\qquad
(a\ne0),
$$

pero de ahí no se sigue:

$$
\frac{a+b}{a}=b.
$$

Y:

$$
2x+3x=5x
$$

es correcto, pero no autoriza:

$$
2+3x=5x.
$$

La forma superficial de dos expresiones puede parecer parecida.

La estructura es la que decide qué ley está disponible.

$$
\boxed{
\text{regla correcta}
+
\text{estructura incorrecta}
=
\text{aplicación incorrecta}.
}
$$

---

### 9.9 Un protocolo para revisar una transformación sospechosa

Cuando una transformación nos produzca dudas, podemos seguir este procedimiento.

#### Paso 1 — Leer la estructura

Preguntar:

- ¿hay una suma?
- ¿hay un producto?
- ¿qué es factor de qué?
- ¿qué operación tiene alcance sobre qué parte?

#### Paso 2 — Nombrar la ley

Preguntar:

> ¿qué propiedad concreta justifica el paso?

Si la respuesta es solamente:

> «porque se cancela»,

o:

> «porque se pasa»,

todavía falta una explicación.

#### Paso 3 — Probar un valor sencillo

Si la supuesta regla pretende valer en general, podemos probar números fáciles.

Un valor que produzca resultados diferentes demuestra que la regla es falsa.

#### Paso 4 — Reconstruir correctamente

Una vez detectado el error, no basta con tacharlo.

Conviene escribir la transformación correcta y explicar qué estructura la permite.

Este protocolo convierte el error en una oportunidad de lectura algebraica.

---

## Ejercicios

### Cuadrado de una suma {#apm-t1-c01-e0046}

Un estudiante escribe:

$$
(x+2)^2=x^2+4.
$$

1. Encuentra un valor de $x$ que muestre que la igualdad es falsa.
2. Expande correctamente $(x+2)^2$.

#### Solución

Podemos tomar:

$$
x=1.
$$

El lado izquierdo vale:

$$
(1+2)^2=9.
$$

El lado derecho de la regla falsa vale:

$$
1^2+4=5.
$$

Como:

$$
9\ne5,
$$

la igualdad no es una identidad.

Ahora:

$$
(x+2)^2=(x+2)(x+2).
$$

Por distributividad:

$$
\begin{aligned}
(x+2)(x+2)
&=x^2+2x+2x+4\\
&=x^2+4x+4.
\end{aligned}
$$

Por tanto:

$$
\boxed{(x+2)^2=x^2+4x+4}.
$$

---

### ¿Cancelación válida? {#apm-t1-c01-e0047}

Decide si cada paso es válido. Justifica.

#### a)

$$
\frac{3x}{3}=x
$$

#### b)

$$
\frac{x+3}{3}=x
$$

#### c)

$$
\frac{3(x+2)}{3}=x+2
$$

#### d)

$$
\frac{x+3}{x}=3
$$

#### Solución

#### a)

Sí.

El numerador es el producto:

$$
3\cdot x.
$$

El factor $3$ puede cancelarse con el denominador:

$$
\frac{3x}{3}=x.
$$

#### b)

No.

En:

$$
x+3,
$$

el $3$ es un término, no un factor de todo el numerador.

#### c)

Sí.

El numerador es:

$$
3(x+2),
$$

de modo que $3$ es factor de toda la expresión:

$$
\frac{3(x+2)}3=x+2.
$$

#### d)

No.

En:

$$
x+3,
$$

la letra $x$ es un término, no un factor del numerador completo.

Para $x\ne0$:

$$
\frac{x+3}{x}
=
1+\frac3x.
$$

---

### Mismo aspecto, distinta estructura {#apm-t1-c01-e0048}

Decide si cada transformación es correcta. En los casos correctos, identifica el factor común. En los incorrectos, explica qué parte de la estructura cambia.

#### a)

$$
3(x+1)+2(x+1)=5(x+1)
$$

#### b)

$$
3(x+1)+2x=5(x+1)
$$

#### c)

$$
4(a-b)-(a-b)=3(a-b)
$$

#### d)

$$
4(a-b)-(a+b)=3(a-b)
$$

#### Solución

#### a)

Es correcta.

Los dos términos comparten el factor:

$$
x+1.
$$

Por distributividad en sentido inverso:

$$
3(x+1)+2(x+1)
=
(3+2)(x+1)
=
5(x+1).
$$

#### b)

Es incorrecta.

El segundo término es:

$$
2x,
$$

no:

$$
2(x+1).
$$

Por tanto, los dos términos no comparten el factor completo $x+1$.

Por ejemplo, con $x=0$:

$$
3(0+1)+2\cdot0=3,
$$

mientras que:

$$
5(0+1)=5.
$$

Así:

$$
3\ne5.
$$

#### c)

Es correcta.

La expresión $a-b$ es factor común:

$$
4(a-b)-(a-b)
=
4(a-b)-1(a-b).
$$

Por distributividad en sentido inverso:

$$
4(a-b)-1(a-b)
=
(4-1)(a-b)
=
3(a-b).
$$

#### d)

Es incorrecta.

Las expresiones:

$$
a-b
$$

y:

$$
a+b
$$

no son el mismo factor.

Tomemos, por ejemplo:

$$
a=2,\qquad b=1.
$$

El lado izquierdo vale:

$$
4(2-1)-(2+1)
=
4-3
=
1.
$$

El lado derecho vale:

$$
3(2-1)=3.
$$

Por tanto:

$$
1\ne3.
$$


### Refutar con un contraejemplo {#apm-t1-c01-e0049}

Encuentra valores sencillos que refuten cada supuesta identidad.

#### a)

$$
(a+b)^3=a^3+b^3
$$

#### b)

$$
\frac{a+b}{a}=b
$$

#### c)

$$
2+5x=7x
$$

#### Solución

#### a)

Tomemos:

$$
a=b=1.
$$

Entonces:

$$
(a+b)^3=2^3=8,
$$

mientras que:

$$
a^3+b^3=1+1=2.
$$

Por tanto:

$$
8\ne2.
$$

#### b)

Tomemos:

$$
a=2,\qquad b=4.
$$

Entonces:

$$
\frac{a+b}{a}=3,
$$

pero:

$$
b=4.
$$

Por tanto:

$$
3\ne4.
$$

#### c)

Tomemos:

$$
x=0.
$$

Entonces:

$$
2+5x=2,
$$

mientras que:

$$
7x=0.
$$

Por tanto:

$$
2\ne0.
$$

---

### Detectar la regla mal aplicada {#apm-t1-c01-e0050}

En cada caso, explica qué regla verdadera parece haber sido utilizada fuera de su contexto.

#### a)

$$
(a+b)^2=a^2+b^2
$$

#### b)

$$
\frac{x+4}{x}=4
$$

#### c)

$$
3+2x=5x
$$

#### Solución

#### a)

Se ha tratado la potencia como si se distribuyera sobre una suma.

Pero:

$$
(a+b)^2
$$

significa:

$$
(a+b)(a+b),
$$

y debe desarrollarse mediante multiplicación y distributividad.

#### b)

Se ha intentado usar cancelación como si $x$ fuera factor de todo el numerador.

Pero el numerador:

$$
x+4
$$

es una suma.

#### c)

Se ha usado el patrón correcto:

$$
3x+2x=5x
$$

en una situación donde el primer término es $3$, no $3x$.

No existe un factor común $x$ en ambos términos.

---

### Diagnóstico completo {#apm-t1-c01-e0051}

Un estudiante escribe:

$$
\frac{x^2+2x}{x}
=
x+2x
=
3x.
$$

Supón $x\ne0$.

1. Identifica el primer paso incorrecto.
2. Explica la estructura correcta del numerador.
3. Simplifica correctamente la expresión.

#### Solución

El numerador es:

$$
x^2+2x.
$$

Ambos términos contienen el factor $x$:

$$
x^2+2x
=
x(x+2).
$$

Por tanto:

$$
\frac{x^2+2x}{x}
=
\frac{x(x+2)}{x}.
$$

Como $x\ne0$, podemos cancelar el factor común $x$:

$$
\frac{x(x+2)}{x}
=
x+2.
$$

La transformación correcta es:

$$
\boxed{
\frac{x^2+2x}{x}=x+2.
}
$$

El estudiante escribió:

$$
x+2x,
$$

como si dividir cada término por $x$ produjera $x$ y $2x$.

Pero:

$$
\frac{2x}{x}=2,
$$

no $2x$.

También podríamos separar correctamente la fracción:

$$
\frac{x^2}{x}+\frac{2x}{x}
=
x+2.
$$

---

## Resumen de la sección

Los errores algebraicos más persistentes suelen parecerse a reglas verdaderas.

Por eso no basta con memorizar una lista de prohibiciones.

Debemos leer la estructura.

Hemos analizado cuatro patrones fundamentales de error:

$$
(a+b)^2=a^2+b^2,
$$

$$
\frac{a+b}{a}=b,
$$

$$
2+3x=5x,
$$

y cancelaciones falsas en expresiones como:

$$
\frac{x+3}{x+5}.
$$

El principio central de cancelación es:

$$
\boxed{
\text{se cancelan factores comunes, no términos dentro de sumas}.
}
$$

Y el protocolo general de diagnóstico es:

$$
\boxed{
\text{estructura}
\longrightarrow
\text{ley}
\longrightarrow
\text{contraejemplo}
\longrightarrow
\text{corrección}.
}
$$

Un contraejemplo puede demostrar que una supuesta regla general es falsa.

Pero comprender el error exige además identificar qué estructura fue ignorada.

La pregunta que debemos acostumbrarnos a formular es:

> **¿qué ley justifica exactamente este paso?**

---

## Hacia la sección siguiente

El capítulo comenzó con una cuenta:

$$
3+4\cdot5.
$$

Desde entonces hemos aprendido a:

- leer estructuras;
- interpretar letras;
- distinguir términos y factores;
- sustituir y evaluar;
- comprender la igualdad;
- distinguir identidades y ecuaciones;
- justificar transformaciones;
- escribir de manera inequívoca;
- diagnosticar reglas falsas.

Solo falta reunir estas capacidades en problemas donde no se indique de antemano qué técnica utilizar.

La última sección del capítulo tendrá ese objetivo:

### §10. Leer antes de operar

Allí el lector deberá decidir por sí mismo qué está viendo antes de calcular, transformar o refutar.
