## §7. Transformar sin cambiar el valor

Hasta ahora hemos aprendido a leer expresiones, sustituir valores, interpretar el signo igual y distinguir identidades de ecuaciones.

Ahora llegamos a una actividad que suele asociarse inmediatamente con el álgebra:

> **transformar expresiones**.

Consideremos:

$$
3(x+2)+2x.
$$

Tal vez ya sepas convertirla en:

$$
5x+6.
$$

Pero la pregunta que nos interesa no es solo:

> ¿cómo se hace?

Queremos preguntar:

> **¿por qué cada paso está permitido?**

Podemos escribir:

$$
\begin{aligned}
3(x+2)+2x
&=3x+6+2x\\
&=3x+2x+6\\
&=(3+2)x+6\\
&=5x+6.
\end{aligned}
$$

Cada línea representa la misma cantidad que la anterior para los valores permitidos de $x$.

Eso no ocurre por magia ni porque ciertos símbolos «se muevan». Ocurre porque en cada paso aplicamos una ley algebraica.

La idea central de esta sección será:

::: {.ma-block .ma-intuicion}
**Idea clave**

Transformar una expresión consiste en reemplazarla por otra expresión que conserva el mismo valor, y cada reemplazo debe estar respaldado por una razón matemática.
:::

Por tanto, aprender álgebra no significa memorizar movimientos de símbolos. Significa aprender **qué transformaciones conservan el valor y por qué**.

---

### 7.1 Una transformación no es un desplazamiento de símbolos

Volvamos a:

$$
3(x+2)+2x.
$$

El primer paso fue:

$$
3(x+2)+2x
=
3x+6+2x.
$$

¿Qué ocurrió?

Aplicamos la distributividad:

$$
3(x+2)
=
3x+3\cdot2
=
3x+6.
$$

No «sacamos el paréntesis».

No «metimos el $3$».

No «repartimos porque sí».

Usamos una ley conocida:

$$
a(b+c)=ab+ac.
$$

Después escribimos:

$$
3x+6+2x
=
3x+2x+6.
$$

Aquí reordenamos y reagrupamos una suma. La justificación procede de las leyes conmutativa y asociativa de la suma.

Finalmente:

$$
3x+2x
=
(3+2)x
$$

es nuevamente una aplicación de la distributividad, ahora leída de derecha a izquierda:

$$
ax+bx=(a+b)x.
$$

Así obtenemos:

$$
(3+2)x+6
=
5x+6.
$$

La cadena completa puede escribirse haciendo visibles las razones:

$$
\begin{aligned}
3(x+2)+2x
&=3x+6+2x
&&\text{distributividad}\\
&=3x+2x+6
&&\text{conmutatividad y asociatividad}\\
&=(3+2)x+6
&&\text{distributividad}\\
&=5x+6
&&\text{aritmética}.
\end{aligned}
$$

Este formato será uno de nuestros hábitos fundamentales.

---

### 7.2 Tres leyes operativas

En este capítulo utilizaremos tres familias de leyes que el lector probablemente conoce por experiencia aritmética.

No las estamos presentando todavía como axiomas de una estructura abstracta. Eso ocurrirá mucho más adelante.

Por ahora las usamos como **leyes operativas** del sistema numérico en el que estamos trabajando.

#### Conmutatividad

En una suma:

$$
a+b=b+a.
$$

En un producto:

$$
ab=ba.
$$

La conmutatividad permite cambiar el orden de los términos de una suma o de los factores de un producto.

Por ejemplo:

$$
2x+7+3x
=
2x+3x+7.
$$

#### Asociatividad

En una suma:

$$
(a+b)+c=a+(b+c).
$$

En un producto:

$$
(ab)c=a(bc).
$$

La asociatividad permite cambiar la agrupación cuando repetimos la misma operación.

Por ejemplo:

$$
(2x+3x)+7
=
2x+(3x+7).
$$

No debe confundirse con cambiar arbitrariamente una operación por otra.

#### Distributividad

La multiplicación se distribuye sobre la suma:

$$
a(b+c)=ab+ac.
$$

También podemos leer la misma igualdad en la dirección contraria:

$$
ab+ac=a(b+c).
$$

En una dirección solemos hablar de **desarrollar** o **expandir**; en la otra, de **extraer un factor común** o **factorizar** en este sentido elemental.

Por ejemplo:

$$
4(x+3)=4x+12,
$$

y también:

$$
4x+12=4(x+3).
$$

Son expresiones distintas, pero representan el mismo valor para los valores permitidos en el contexto.

---

### 7.3 La dirección de una transformación depende del objetivo

Consideremos:

$$
5(x+2).
$$

Podemos transformarla en:

$$
5x+10.
$$

¿Es esta segunda expresión «mejor»?

No necesariamente.

Depende de qué queramos hacer.

Si deseamos ver una suma de términos, puede ser útil:

$$
5x+10.
$$

Si deseamos hacer visible el factor común $5$, puede ser más informativa:

$$
5(x+2).
$$

Ambas formas conservan el mismo valor:

$$
5(x+2)=5x+10.
$$

Por tanto:

::: {.ma-block .ma-intuicion}
**Idea clave**

Transformar una expresión no significa necesariamente hacerla más corta.  
Significa obtener una forma que conserve el valor y resulte útil para el propósito actual.
:::

Esto será cada vez más importante.

Una misma expresión puede tener varias formas correctas, y cada forma puede revelar una estructura distinta.

---

### 7.4 La distributividad funciona en ambas direcciones

Consideremos:

$$
6x+9x.
$$

Podemos ver dos términos:

$$
6x
\qquad\text{y}\qquad
9x.
$$

Ambos contienen el factor $x$.

Por distributividad:

$$
6x+9x
=
(6+9)x
=
15x.
$$

No estamos «sumando las letras».

Estamos usando:

$$
ax+bx=(a+b)x.
$$

El factor $x$ permanece común y sumamos los coeficientes.

Del mismo modo:

$$
4a+4b
=
4(a+b).
$$

Aquí no obtenemos:

$$
8ab
$$

ni ninguna combinación semejante. Lo que hacemos es reconocer un factor común.

La lectura estructural determina la transformación correcta.

---

### 7.5 Reordenar exige una razón

Consideremos:

$$
2x+5+3x.
$$

Queremos reunir los términos que contienen $x$.

Podemos escribir:

$$
2x+5+3x
=
2x+3x+5.
$$

A veces se dice informalmente:

> «muevo el $3x$ junto al $2x$».

Pero esa frase oculta la razón matemática.

Lo que realmente usamos es que podemos reordenar y reagrupar los sumandos mediante conmutatividad y asociatividad.

Después:

$$
2x+3x+5
=
(2+3)x+5
=
5x+5.
$$

El proceso completo puede escribirse:

$$
\begin{aligned}
2x+5+3x
&=2x+3x+5
&&\text{conmutatividad y asociatividad}\\
&=(2+3)x+5
&&\text{distributividad}\\
&=5x+5
&&\text{aritmética}.
\end{aligned}
$$

La expresión no cambia de valor en ningún paso.

---

### 7.6 Ejemplo desarrollado: justificar cada transformación

::: {.ma-block .ma-observacion #apm-t1-c01-x0006}
**Ejemplo — De \(3(x+2)+2x\) a \(5x+6\)**

:::

Queremos transformar:

$$
3(x+2)+2x.
$$

#### Paso 1 — Desarrollar el producto

Aplicamos distributividad:

$$
3(x+2)
=
3x+3\cdot2.
$$

Por tanto:

$$
3(x+2)+2x
=
3x+6+2x.
$$

#### Paso 2 — Reunir los términos con \(x\)

Reordenamos y reagrupamos la suma:

$$
3x+6+2x
=
3x+2x+6.
$$

La razón es la conmutatividad y la asociatividad de la suma.

#### Paso 3 — Extraer el factor común \(x\)

Aplicamos distributividad en sentido inverso:

$$
3x+2x
=
(3+2)x.
$$

Entonces:

$$
3x+2x+6
=
(3+2)x+6.
$$

#### Paso 4 — Realizar la aritmética

$$
(3+2)x+6
=
5x+6.
$$

#### Cadena completa

$$
\begin{aligned}
3(x+2)+2x
&=3x+6+2x
&&\text{distributividad}\\
&=3x+2x+6
&&\text{conmutatividad y asociatividad}\\
&=(3+2)x+6
&&\text{distributividad}\\
&=5x+6
&&\text{aritmética}.
\end{aligned}
$$

No hemos aplicado una receta de «quitar paréntesis y juntar letras».

Hemos construido una cadena de igualdades, y cada igualdad tiene una justificación.

---

### 7.7 Dos caminos correctos pueden llegar al mismo lugar

Consideremos:

$$
2(x+3)+4(x+3).
$$

#### Camino A — Desarrollar primero

Aplicamos distributividad a cada producto:

$$
2(x+3)+4(x+3)
=
2x+6+4x+12.
$$

Reordenamos:

$$
2x+6+4x+12
=
2x+4x+6+12.
$$

Reunimos términos:

$$
2x+4x+6+12
=
6x+18.
$$

#### Camino B — Reconocer primero el factor común

Ambos términos contienen el factor:

$$
x+3.
$$

Por distributividad en sentido inverso:

$$
2(x+3)+4(x+3)
=
(2+4)(x+3).
$$

Entonces:

$$
(2+4)(x+3)
=
6(x+3).
$$

Si deseamos desarrollar:

$$
6(x+3)
=
6x+18.
$$

Los dos caminos llegan a:

$$
6x+18.
$$

Ninguno es «el único método correcto».

Sin embargo, el segundo camino reconoce antes una estructura común y requiere menos pasos.

Esto introduce otro hábito importante:

$$
\boxed{
\text{una transformación puede ser correcta y, además, más o menos conveniente}.
}
$$

La corrección y la eficiencia son cuestiones distintas.

---

### 7.8 Cómo detectar un paso inválido

Consideremos la supuesta transformación:

$$
3(x+2)+2x
=
3x+2+2x.
$$

¿Qué ocurrió?

Parece que alguien escribió:

$$
3(x+2)=3x+2.
$$

Pero la distributividad exige multiplicar **cada término** de la suma por $3$:

$$
3(x+2)=3x+6.
$$

Podemos detectar el error también mediante una comprobación numérica.

Tomemos:

$$
x=0.
$$

La expresión original vale:

$$
3(0+2)+2\cdot0=6.
$$

La expresión supuestamente transformada vale:

$$
3\cdot0+2+2\cdot0=2.
$$

Como:

$$
6\ne2,
$$

las dos expresiones no conservan el mismo valor.

La comprobación numérica no sustituye la explicación estructural, pero puede ayudarnos a detectar que algo salió mal.

::: {.ma-block .ma-error}
**Atención**

Una transformación algebraica no es válida porque «parezca habitual». Debemos poder indicar la ley que la justifica.
:::

---

### 7.9 «Mover», «pasar» y «cancelar» pueden ocultar matemáticas

En muchos cursos se oyen expresiones como:

- «muevo este término»;
- «paso este número»;
- «cambia de signo al cruzar»;
- «cancelo estas letras».

A veces estas frases se utilizan como abreviaturas informales de razonamientos correctos.

El problema aparece cuando la abreviatura sustituye a la razón.

En una expresión como:

$$
2x+5+3x,
$$

decir «movemos $3x$» no explica por qué está permitido escribir:

$$
2x+3x+5.
$$

La razón es la conmutatividad y asociatividad de la suma.

Más adelante, cuando estudiemos ecuaciones, veremos que «pasar al otro lado» tampoco es una operación algebraica independiente. Habrá que justificar qué hacemos a ambos miembros de la igualdad.

Por ahora adoptaremos una regla editorial para todo el libro:

::: {.ma-block .ma-intuicion}
**Idea clave**

Podemos usar una abreviatura verbal solo después de que la operación matemática que resume haya quedado clara. Nunca reemplazaremos una justificación por la imagen de que los símbolos «se trasladan» solos.
:::

---

### 7.10 Transformar no es cambiar arbitrariamente

Una expresión puede adoptar muchas formas correctas, pero no cualquier forma.

Por ejemplo:

$$
2(x+5)
=
2x+10
$$

es correcto por distributividad.

Pero:

$$
2(x+5)
=
2x+5
$$

es falso.

Asimismo:

$$
3x+4x=7x
$$

es correcto porque:

$$
3x+4x=(3+4)x.
$$

En cambio:

$$
3x+4=7x
$$

no está justificado: los dos términos no comparten el factor $x$.

La pregunta decisiva ante cada paso es:

> **¿qué ley permite reemplazar la expresión anterior por la nueva?**

Si no podemos responder, debemos revisar el paso.

---

## Ejercicios

### Nombrar la ley {#apm-t1-c01-e0034}

Indica qué ley justifica cada igualdad.

#### a)

$$
a+b=b+a
$$

#### b)

$$
(a+b)+c=a+(b+c)
$$

#### c)

$$
3(x+4)=3x+12
$$

#### d)

$$
5x+2x=(5+2)x
$$

#### e)

$$
ab=ba
$$

#### Solución

#### a)

$$
a+b=b+a
$$

usa la **conmutatividad de la suma**.

#### b)

$$
(a+b)+c=a+(b+c)
$$

usa la **asociatividad de la suma**.

#### c)

$$
3(x+4)=3x+12
$$

usa la **distributividad**:

$$
3(x+4)=3x+3\cdot4=3x+12.
$$

#### d)

$$
5x+2x=(5+2)x
$$

usa la **distributividad en sentido inverso**.

#### e)

$$
ab=ba
$$

usa la **conmutatividad del producto**.

---

### Justificar cada paso {#apm-t1-c01-e0035}

Completa las razones de la transformación:

$$
\begin{aligned}
4(x+2)+3x
&=4x+8+3x\\
&=4x+3x+8\\
&=(4+3)x+8\\
&=7x+8.
\end{aligned}
$$

#### Solución

La primera igualdad:

$$
4(x+2)+3x
=
4x+8+3x
$$

usa distributividad.

La segunda:

$$
4x+8+3x
=
4x+3x+8
$$

usa conmutatividad y asociatividad de la suma para reordenar y reagrupar.

La tercera:

$$
4x+3x+8
=
(4+3)x+8
$$

usa distributividad en sentido inverso.

La cuarta:

$$
(4+3)x+8
=
7x+8
$$

usa aritmética.

---

### Transformar sin saltos {#apm-t1-c01-e0036}

Transforma:

$$
5(x+1)+2x
$$

hasta obtener una expresión de la forma:

$$
ax+b.
$$

Justifica cada paso.

#### Solución

Comenzamos con:

$$
5(x+1)+2x.
$$

Por distributividad:

$$
5(x+1)+2x
=
5x+5+2x.
$$

Reordenamos y reagrupamos:

$$
5x+5+2x
=
5x+2x+5.
$$

Por distributividad en sentido inverso:

$$
5x+2x+5
=
(5+2)x+5.
$$

Finalmente:

$$
(5+2)x+5
=
7x+5.
$$

La cadena completa es:

$$
\begin{aligned}
5(x+1)+2x
&=5x+5+2x
&&\text{distributividad}\\
&=5x+2x+5
&&\text{conmutatividad y asociatividad}\\
&=(5+2)x+5
&&\text{distributividad}\\
&=7x+5
&&\text{aritmética}.
\end{aligned}
$$

---

### Dos caminos {#apm-t1-c01-e0037}

Transforma:

$$
3(x+2)+5(x+2)
$$

de dos maneras:

1. desarrollando primero ambos productos;
2. reconociendo primero el factor común $x+2$.

Comprueba que ambos caminos conducen a la misma forma desarrollada.

#### Solución

#### Camino 1 — Desarrollar

$$
\begin{aligned}
3(x+2)+5(x+2)
&=3x+6+5x+10\\
&=3x+5x+6+10\\
&=8x+16.
\end{aligned}
$$

#### Camino 2 — Factor común

Por distributividad en sentido inverso:

$$
3(x+2)+5(x+2)
=
(3+5)(x+2).
$$

Entonces:

$$
(3+5)(x+2)
=
8(x+2).
$$

Desarrollamos:

$$
8(x+2)
=
8x+16.
$$

Ambos caminos llegan a:

$$
\boxed{8x+16}.
$$

El segundo camino reconoce antes la estructura común.

---

### Encontrar el primer paso inválido {#apm-t1-c01-e0038}

Un estudiante escribe:

$$
\begin{aligned}
2(x+4)+3x
&=2x+4+3x\\
&=5x+4.
\end{aligned}
$$

1. Identifica el primer paso incorrecto.
2. Explica qué ley se aplicó mal.
3. Corrige toda la transformación.

#### Solución

El primer paso incorrecto es:

$$
2(x+4)=2x+4.
$$

La distributividad se aplicó de manera incompleta.

Debe multiplicarse por $2$ cada término del paréntesis:

$$
2(x+4)
=
2x+8.
$$

Por tanto:

$$
\begin{aligned}
2(x+4)+3x
&=2x+8+3x\\
&=2x+3x+8\\
&=(2+3)x+8\\
&=5x+8.
\end{aligned}
$$

La forma correcta es:

$$
\boxed{5x+8}.
$$

---

### ¿Puede reunirse? {#apm-t1-c01-e0039}

Decide si la transformación propuesta está justificada. Explica por qué.

#### a)

$$
3x+4x=7x
$$

#### b)

$$
3x+4=7x
$$

#### c)

$$
2a+5a=(2+5)a
$$

#### d)

$$
2a+5b=7ab
$$

#### Solución

#### a)

Sí.

$$
3x+4x
=
(3+4)x
=
7x
$$

por distributividad.

#### b)

No.

En:

$$
3x+4,
$$

los términos $3x$ y $4$ no comparten el factor $x$.

No existe una aplicación de distributividad que permita escribir:

$$
3x+4=7x.
$$

#### c)

Sí.

$$
2a+5a
=
(2+5)a
=
7a.
$$

#### d)

No.

Los términos:

$$
2a
\qquad\text{y}\qquad
5b
$$

no tienen la estructura necesaria para obtener:

$$
7ab.
$$

La transformación propuesta no está justificada.

---

### Elegir una forma útil {#apm-t1-c01-e0040}

Considera:

$$
6x+18.
$$

#### a)

Escribe una forma factorizada usando distributividad en sentido inverso.

#### b)

¿Cuál de las dos formas hace más visible el factor común $6$?

#### c)

¿Cuál hace más visible que la expresión es una suma de dos términos?

#### Solución

#### a)

Extraemos el factor común $6$:

$$
6x+18
=
6x+6\cdot3
=
6(x+3).
$$

#### b)

La forma:

$$
6(x+3)
$$

hace visible el factor común $6$.

#### c)

La forma:

$$
6x+18
$$

hace visible inmediatamente que tenemos una suma de dos términos.

Ninguna forma es absolutamente «mejor». Cada una revela una estructura distinta.

---

## Resumen de la sección

Transformar una expresión no consiste en desplazar símbolos.

Consiste en construir una cadena de igualdades donde cada paso conserva el valor y está respaldado por una ley conocida.

Las tres leyes operativas principales de esta sección han sido:

$$
\boxed{
a+b=b+a
}
$$

y:

$$
\boxed{
ab=ba
}
$$

para la conmutatividad;

$$
\boxed{
(a+b)+c=a+(b+c)
}
$$

y:

$$
\boxed{
(ab)c=a(bc)
}
$$

para la asociatividad; y:

$$
\boxed{
a(b+c)=ab+ac
}
$$

para la distributividad.

Hemos aprendido además que:

- la distributividad puede leerse en ambas direcciones;
- reordenar términos exige conmutatividad y asociatividad;
- reunir términos semejantes es una aplicación de distributividad;
- distintas transformaciones correctas pueden conducir al mismo resultado;
- una forma no es siempre mejor por ser más corta;
- una comprobación numérica puede detectar un error, pero la justificación es la ley algebraica;
- expresiones como «mover», «pasar» o «cancelar» no deben sustituir a la razón matemática.

El principio que debe quedar instalado es:

$$
\boxed{
\text{cada paso algebraico debe poder responder a la pregunta: «¿por qué?»}
}
$$

---

## Hacia la sección siguiente

Las leyes algebraicas nos permiten transformar expresiones correctamente.

Pero incluso una transformación matemáticamente válida puede resultar difícil de leer si la notación es ambigua.

Consideremos:

$$
-x^2
$$

y:

$$
(-x)^2.
$$

¿Representan lo mismo?

O comparemos:

$$
\frac{a+b}{c}
$$

con:

$$
a+\frac{b}{c}.
$$

En ambos casos, pequeños cambios en la escritura alteran la estructura.

La próxima sección estudiará precisamente ese problema:
