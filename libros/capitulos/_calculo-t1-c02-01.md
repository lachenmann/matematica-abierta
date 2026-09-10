## El hueco de los racionales {#sec-t1-c02-01}

### Una ecuación demasiado sencilla para causar problemas

Busquemos primero soluciones racionales de

$$
x^2=2.
$$

Los cuadrados de $1$ y $2$ nos dicen que, si existiera una solución positiva, tendría que encontrarse entre ellos:

$$
1^2<2<2^2.
$$

Podemos probar números racionales intermedios:

$$
\left(\frac43\right)^2=\frac{16}{9}<2,
\qquad
\left(\frac32\right)^2=\frac94>2.
$$

Así que una eventual solución tendría que estar entre $4/3$ y $3/2$. Si continuamos ensayando fracciones, podemos estrechar el intervalo cada vez más. Esto produce evidencia de que existe algún tipo de frontera entre los racionales cuyo cuadrado queda por debajo de $2$ y aquellos cuyo cuadrado queda por encima.

Pero una búsqueda de fracciones, por extensa que sea, no decide si alguna de ellas satisface **exactamente** la ecuación. Después de `T1-C01` sabemos qué pregunta debemos formular:

> ¿podemos demostrar que existe un racional con cuadrado $2$, o podemos demostrar que ninguno existe?

La segunda alternativa es la correcta.

::: {#prp-t1-0006}
**Inexistencia de una solución racional de $x^2=2$.** No existe ningún número racional $q$ tal que

$$
q^2=2.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Si un racional $q$ satisficiera $q^2=2$, podríamos escribirlo como una fracción reducida $m/n$. La ecuación obligará primero a que $m$ sea par y después a que $n$ también sea par. Pero una fracción reducida no puede tener numerador y denominador ambos pares.

El argumento utilizará precisamente la técnica de contradicción y el hecho, ya trabajado en `T1-C01`, de que si el cuadrado de un entero es par, entonces el entero es par.
:::

**Demostración.** Supongamos, para obtener una contradicción, que existe $q\in\mathbb Q$ con $q^2=2$.

Podemos escribir

$$
q=\frac{m}{n},
$$

con $m,n\in\mathbb Z$, $n\ne0$, y elegir la fracción reducida de manera que $m$ y $n$ no tengan un factor común mayor que $1$. En particular, no pueden ser ambos pares.

De

$$
\left(\frac{m}{n}\right)^2=2
$$

se obtiene

$$
m^2=2n^2.
$$

Por tanto, $m^2$ es par. En `T1-C01` demostramos, mediante contraposición, que si el cuadrado de un entero es par, entonces el entero es par. Luego $m$ es par. Existe entonces $k\in\mathbb Z$ tal que

$$
m=2k.
$$

Sustituyendo en $m^2=2n^2$,

$$
(2k)^2=2n^2,
$$

de modo que

$$
4k^2=2n^2
$$

y, al dividir por $2$,

$$
n^2=2k^2.
$$

Así, $n^2$ también es par y, por la misma razón, $n$ es par.

Hemos concluido que $m$ y $n$ son ambos pares. Esto contradice que $m/n$ se hubiese elegido como una fracción reducida. Por consiguiente, no existe $q\in\mathbb Q$ tal que $q^2=2$. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
Conviene identificar la arquitectura del argumento.

1. **Objetivo:** demostrar una inexistencia.
2. **Estrategia:** contradicción.
3. **Suposición temporal:** existe un racional $q$ con $q^2=2$.
4. **Representación útil:** $q=m/n$ en forma reducida.
5. **Mecanismo:** la ecuación fuerza paridad en $m$ y después en $n$.
6. **Contradicción:** la supuesta fracción reducida tiene un factor común $2$.

La prueba no demuestra todavía que haya un número real cuyo cuadrado sea $2$. Demuestra solamente que **si existe tal número, no puede ser racional**. Esta distinción entre inexistencia en un dominio y existencia en otro será esencial durante todo el capítulo.
:::

### Qué hemos demostrado y qué no

Es fácil deslizarse sin advertirlo desde

> ningún racional satisface $x^2=2$

hasta

> existe un número no racional que satisface $x^2=2$.

Pero estas afirmaciones no son equivalentes.

La primera acaba de ser demostrada. La segunda es una afirmación de **existencia** que todavía requiere una justificación. En particular, no utilizaremos todavía la notación habitual para la raíz cuadrada de $2$ como si su existencia dentro de nuestro sistema ya estuviera establecida. Esa notación quedará matemáticamente legitimada en §2.6, una vez que dispongamos de la completitud.

Este cuidado puede parecer excesivo porque todos hemos usado raíces cuadradas mucho antes de estudiar análisis. Sin embargo, contiene una lección importante: una notación familiar no sustituye una prueba de existencia.

### La diagonal de un cuadrado y el problema aritmético

La geometría hace que la situación sea todavía más provocadora. Consideremos un cuadrado de lado $1$. El teorema de Pitágoras nos dice que, si $d$ representa la longitud de su diagonal, entonces

$$
d^2=1^2+1^2=2.
$$

Geométricamente parece natural que esa diagonal tenga una longitud. Aritméticamente acabamos de probar que **ningún racional** puede representarla.

No utilizaremos esta imagen como demostración de la existencia de un número real particular. Su función es motivadora: muestra que el sistema racional, aunque extraordinariamente rico, no basta para representar todas las magnitudes que la geometría nos invita a considerar.

El problema no consiste en que los racionales estén muy separados. De hecho, entre dos racionales distintos siempre podemos insertar otro racional: si $r<s$, entonces

$$
r<\frac{r+s}{2}<s.
$$

Hay racionales entre racionales sin importar cuán próximos parezcan. Y, sin embargo, algo puede seguir faltando.

Para comprender qué significa exactamente ese «algo», examinaremos un famoso ejemplo con mucho más detalle del que suele recibir.

### El ejemplo introductorio de Rudin, paso a paso

En el Ejemplo 1.1 de la tercera edición de *Principles of Mathematical Analysis*, Walter Rudin utiliza la ecuación $p^2=2$ para exhibir el hueco de los racionales. Después de demostrar la inexistencia de una solución racional, considera los conjuntos

$$
A=\{p\in\mathbb Q:p>0,\ p^2<2\}
$$

y

$$
B=\{p\in\mathbb Q:p>0,\ p^2>2\}.
$$

Como ningún racional positivo tiene cuadrado exactamente igual a $2$, todo racional positivo pertenece a uno de estos dos conjuntos.

Además, todo elemento de $A$ está a la izquierda de todo elemento de $B$. En efecto, si $a\in A$ y $b\in B$ pero $b\le a$, entonces, como ambos son positivos,

$$
b^2\le a^2<2,
$$

lo que contradice $b^2>2$.

Tenemos, pues, dos regiones racionales perfectamente ordenadas:

$$
\boxed{
A\quad\text{queda por debajo del borde},
\qquad
B\quad\text{queda por encima del borde}.
}
$$

La dificultad comienza cuando Rudin quiere demostrar algo más fino:

- $A$ **no tiene un elemento mayor**;
- $B$ **no tiene un elemento menor**.

Para un racional positivo $p$, introduce de pronto

$$
q
=
 p-\frac{p^2-2}{p+2}
=
\frac{2p+2}{p+2}
=
\frac{2(p+1)}{p+2}.
$$

La fórmula funciona admirablemente, pero un lector novel puede preguntarse con toda razón:

> ¿de dónde salió $q$?

Si simplemente verificamos las cuentas después de conocer la fórmula, aprendemos que la fórmula funciona. Todavía no aprendemos **cómo podría habérsenos ocurrido construirla**. Vamos a separar esas dos cuestiones.

::: {#exm-t1-0012}
**El ejemplo de Rudin, sin pasos ocultos.** Para cada $p\in\mathbb Q$ con $p>0$, definamos

$$
q=p-\frac{p^2-2}{p+2}.
$$

Entonces:

- si $p^2<2$, se cumple $p<q$ y $q^2<2$;
- si $p^2>2$, se cumple $0<q<p$ y $q^2>2$.

Por tanto, desde cualquier elemento de $A$ podemos construir otro elemento de $A$ mayor, y desde cualquier elemento de $B$ podemos construir otro elemento de $B$ menor.
:::

#### Primera pregunta: ¿q sigue siendo racional y positivo?

Sí. Si $p\in\mathbb Q$, entonces la expresión

$$
q=\frac{2(p+1)}{p+2}
$$

está formada mediante operaciones racionales. Como $p>0$, tenemos $p+1>0$ y $p+2>0$, así que

$$
q>0.
$$

Esta comprobación es pequeña, pero no debe omitirse: para concluir que $q\in A$ o $q\in B$ necesitamos que $q$ siga perteneciendo al dominio de esos conjuntos.

#### Segunda pregunta: ¿q se mueve en la dirección correcta?

Restemos $p$:

$$
\begin{aligned}
q-p
&=
-\frac{p^2-2}{p+2}\\
&=
\frac{2-p^2}{p+2}.
\end{aligned}
$$

Como $p+2>0$, el signo de $q-p$ es exactamente el signo de $2-p^2$.

Por tanto:

- si $p^2<2$, entonces $2-p^2>0$ y $q-p>0$, de modo que $q>p$;
- si $p^2>2$, entonces $2-p^2<0$ y $q-p<0$, de modo que $q<p$.

La fórmula mueve a $p$ **hacia** el borde que separa $p^2<2$ de $p^2>2$.

Pero todavía falta algo esencial. Moverse en la dirección correcta no garantiza que no atravesemos el borde.

Por ejemplo, si partiéramos de $p=1$ y usáramos la corrección ingenua

$$
p+(2-p^2),
$$

obtendríamos $2$, cuyo cuadrado es $4$. Nos habríamos pasado al otro lado.

Así que necesitamos controlar no solo la dirección del movimiento, sino también el lado en el que termina $q$.

#### Tercera pregunta: ¿q permanece en el mismo lado?

Calculemos el nuevo «error» respecto de $2$:

$$
\begin{aligned}
q^2-2
&=
\left(\frac{2(p+1)}{p+2}\right)^2-2\\
&=
\frac{4(p+1)^2-2(p+2)^2}{(p+2)^2}\\
&=
\frac{2(p^2-2)}{(p+2)^2}.
\end{aligned}
$$

El denominador $(p+2)^2$ es positivo, y el factor $2$ también lo es. Por consiguiente,

$$
\boxed{
q^2-2\ \text{tiene el mismo signo que}\ p^2-2.
}
$$

Esto completa el mecanismo.

Si $p\in A$, entonces $p^2-2<0$. Hemos visto que

$$
q>p
$$

y

$$
q^2-2<0.
$$

Así que $q\in A$ y $q$ es mayor que $p$. Como podemos hacer esto partiendo de **cualquier** $p\in A$, ningún elemento de $A$ puede ser el mayor.

Si $p\in B$, entonces $p^2-2>0$. Hemos visto que

$$
0<q<p
$$

y

$$
q^2-2>0.
$$

Así que $q\in B$ y $q$ es menor que $p$. Como podemos hacerlo desde **cualquier** $p\in B$, ningún elemento de $B$ puede ser el menor.

La demostración está terminada. Ahora podemos abordar la pregunta más interesante: cómo fabricar la fórmula.

### Cómo se fabrica una fórmula que parece caída del cielo

Rudin presenta $q$ directamente. Nosotros reconstruiremos una ruta posible para descubrirla. No pretendemos afirmar que este haya sido históricamente el proceso mental exacto mediante el cual se eligió la fórmula. Lo que sí podemos hacer es mostrar que **la elección puede diseñarse sistemáticamente** a partir de las propiedades que necesitamos.

Empecemos con un racional positivo $p$. Definamos su defecto respecto de la ecuación por

$$
E(p)=p^2-2.
$$

Si $E(p)<0$, necesitamos aumentar $p$.

Si $E(p)>0$, necesitamos disminuirlo.

Así que resulta natural buscar una corrección cuyo signo sea el opuesto al de $E(p)$. Una primera familia razonable es

$$
q_c
=
p-\frac{p^2-2}{p+c},
$$

donde $c>0$ será un número racional que elegiremos después.

¿Por qué introducir $c$? Porque queremos **regular el tamaño de la corrección**. El numerador $p^2-2$ decide la dirección; el denominador $p+c$ amortigua el desplazamiento.

Para esta familia tenemos inmediatamente

$$
q_c-p
=
\frac{2-p^2}{p+c}.
$$

Como $p+c>0$, el movimiento tiene siempre la dirección deseada.

Ahora imponemos la segunda condición: queremos que $q_c$ no cruce el borde. Para descubrir qué debe cumplir $c$, calculamos:

$$
q_c
=
\frac{cp+2}{p+c},
$$

y por tanto

$$
\begin{aligned}
q_c^2-2
&=
\frac{(cp+2)^2-2(p+c)^2}{(p+c)^2}\\
&=
\frac{(c^2-2)(p^2-2)}{(p+c)^2}.
\end{aligned}
$$

Ahora la elección de $c$ deja de ser misteriosa.

Queremos que $q_c^2-2$ tenga el **mismo signo** que $p^2-2$. El denominador es positivo, así que basta exigir

$$
c^2-2>0.
$$

No necesitamos conocer ninguna solución de $x^2=2$ para encontrar un racional con esa propiedad. Podemos escoger sencillamente

$$
c=2,
$$

porque

$$
2^2-2=2>0.
$$

Al sustituir $c=2$ obtenemos exactamente

$$
q
=
p-\frac{p^2-2}{p+2},
$$

la fórmula utilizada por Rudin.

::: {.callout-important title="La técnica escondida"}
La expresión de Rudin no necesita verse como una inspiración inexplicable. Puede reconstruirse mediante cuatro movimientos:

1. **medir el defecto:** $E(p)=p^2-2$;
2. **corregir en la dirección opuesta al defecto:** restar una cantidad proporcional a $E(p)$;
3. **introducir un parámetro** para controlar el tamaño de la corrección;
4. **imponer un invariante:** después de corregir, el signo de $q^2-2$ debe seguir siendo el mismo.

Esta forma de diseñar un objeto —decidir primero qué propiedades debe satisfacer y después resolver algebraicamente las condiciones que las garantizan— es una técnica matemática general. Volverá a aparecer muchas veces con disfraces distintos.
:::

Hay además una consecuencia tranquilizadora: la fórmula no era única. Cualquier racional positivo $c$ con $c^2>2$ produciría una transformación del mismo tipo. Elegir $c=2$ hace la expresión particularmente simple.

### Ver la máquina funcionando

Tomemos primero un número que está por debajo del borde, por ejemplo $p=1$. La transformación produce

$$
1
\longmapsto
\frac43
\longmapsto
\frac75
\longmapsto
\frac{24}{17}.
$$

Cada nuevo racional es mayor que el anterior y su cuadrado sigue siendo menor que $2$.

Si comenzamos por encima, con $p=2$, obtenemos

$$
2
\longmapsto
\frac32
\longmapsto
\frac{10}{7}
\longmapsto
\frac{17}{12}.
$$

Cada nuevo racional es menor que el anterior y su cuadrado sigue siendo mayor que $2$.

Estas cadenas son útiles para visualizar el mecanismo, pero conviene aplicar aquí la lección del capítulo anterior: **una lista de ejemplos no demuestra la afirmación general**. La demostración está en las dos identidades

$$
q-p=\frac{2-p^2}{p+2}
$$

y

$$
q^2-2=\frac{2(p^2-2)}{(p+2)^2},
$$

porque controlan simultáneamente todos los racionales positivos $p$.

Tampoco diremos todavía que estas cadenas «convergen». El lenguaje de convergencia será construido más adelante. Por ahora solo necesitamos las desigualdades que acabamos de demostrar.

::: {.callout-tip title="Antes de seguir"}
Partiendo de $p=1$, la fórmula de Rudin da $q=4/3$.

1. ¿Es $q>p$?
2. ¿Sigue cumpliéndose $q^2<2$?
3. ¿Qué parte de la demostración general garantiza cada respuesta sin necesidad de calcular específicamente $16/9$?

**Respuesta.** Sí a las dos primeras preguntas. Como $p^2<2$, la identidad para $q-p$ garantiza $q>p$, y la identidad para $q^2-2$ garantiza que $q^2-2$ conserva signo negativo. El cálculo particular $16/9<2$ sirve como comprobación, no como fundamento de la prueba.
:::

### Entonces, ¿dónde está exactamente el hueco?

Ya podemos describir con mucha más precisión el problema de los racionales.

No existe un intervalo racional vacío alrededor del borde. Eso sería falso: entre dos racionales distintos siempre hay otros racionales.

Lo que falta es otra cosa.

El conjunto $A$ contiene racionales positivos cuyos cuadrados están por debajo de $2$. No tiene elemento mayor: desde cualquiera de ellos podemos subir a otro racional que sigue perteneciendo a $A$.

El conjunto $B$ contiene racionales positivos cuyos cuadrados están por encima de $2$. No tiene elemento menor: desde cualquiera de ellos podemos bajar a otro racional que sigue perteneciendo a $B$.

Y, sin embargo,

$$
a<b
\qquad
\text{para todo }a\in A\text{ y todo }b\in B.
$$

Intuitivamente, $A$ y $B$ se acercan a una misma frontera desde lados opuestos, pero ningún racional ocupa esa frontera.

Podemos volver a nombrar el conjunto inferior como

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Más adelante aprenderemos a formular la pregunta correcta sobre él:

> ¿posee $S_{\mathbb Q}$ una **menor cota superior** dentro del sistema numérico en el que estamos trabajando?

Todavía no hemos definido «cota superior» ni «menor cota superior». Lo haremos en §2.4. Pero el ejemplo nos ha dicho ya **por qué necesitaremos esas definiciones**.

En §2.5 regresaremos a este mismo conjunto y demostraremos formalmente que, considerado como subconjunto de $\mathbb Q$, no posee la propiedad de borde que necesitaremos. Después veremos que el paso a $\mathbb R$ no consiste simplemente en añadir números al azar, sino en exigir una propiedad estructural que garantice la existencia de esos bordes bajo hipótesis precisas.

### Una segunda lectura del ejemplo de Rudin

Vale la pena resumir ahora qué habilidades estaban comprimidas en aquellas pocas líneas del ejemplo clásico.

Para seguir el argumento hay que saber hacer, al menos, todo esto:

1. interpretar $p^2<2$ y $p^2>2$ como pertenencia a dos conjuntos distintos;
2. reconocer que «$A$ no tiene mayor» exige tomar un $p\in A$ **arbitrario** y construir otro elemento mayor;
3. reconocer que «$B$ no tiene menor» exige el problema dual;
4. inventar o aceptar una transformación racional $p\mapsto q$;
5. comprobar que $q$ sigue siendo positivo y racional;
6. comparar $q$ con $p$ mediante el signo de $q-p$;
7. comparar $q^2$ con $2$ mediante el signo de $q^2-2$;
8. entender que las dos comparaciones deben controlarse **simultáneamente**;
9. usar cuantificadores correctamente: la construcción debe funcionar para cada $p$ del conjunto correspondiente;
10. interpretar el resultado como evidencia estructural de una carencia de $\mathbb Q$, no simplemente como una curiosidad algebraica.

Rudin escribe para un lector que puede reconstruir una gran parte de esta ingeniería. Nuestro objetivo es distinto: queremos que el lector aprenda **la ingeniería misma**.

::: {.callout-note title="Por qué importa"}
El verdadero tema que acaba de aparecer no es la raíz cuadrada de $2$ en particular.

La pregunta general es:

> cuando un conjunto ordenado se aproxima a una frontera sin alcanzarla, ¿qué propiedad del sistema numérico garantiza que esa frontera exista como número del sistema?

La respuesta será la completitud de $\mathbb R$. Antes de formularla necesitamos construir cuidadosamente el vocabulario de orden, intervalos, cotas, supremos e ínfimos.
:::

### Qué nos llevamos a la sección siguiente

Esta primera sección ha producido cuatro hechos conceptuales.

Primero, los racionales son algebraicamente ricos pero no bastan para resolver todas las ecuaciones geométricamente naturales: hemos demostrado que

$$
q^2\ne2
\qquad
\text{para todo }q\in\mathbb Q.
$$

Segundo, el problema no desaparece por la densidad elemental de los racionales. Poder insertar siempre otro racional entre dos racionales no garantiza que todo conjunto racional posea el punto frontera que su orden sugiere.

Tercero, el ejemplo de Rudin nos ha enseñado una técnica de construcción que vale por sí misma:

$$
\boxed{
\text{defecto}
\to
\text{corrección dirigida}
\to
\text{control del invariante}
\to
\text{nuevo objeto}
}
$$

Cuarto, todavía no tenemos derecho a decir que el hueco ha sido llenado. Para ello necesitamos especificar qué estructura tendrán los números reales y qué propiedad adicional distinguirá a $\mathbb R$ de $\mathbb Q$.

La próxima sección comenzará ese trabajo. Presentaremos a $\mathbb R$ como un **cuerpo ordenado** y deduciremos cuidadosamente las reglas de desigualdad que hasta ahora hemos usado de manera familiar. Solo después estaremos preparados para formular con precisión qué significa que un conjunto tenga una frontera y, finalmente, qué significa que la recta real sea completa.
