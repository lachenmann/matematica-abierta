## §1 — Un número no es todavía una magnitud física {#fpm-i-02-s01}

### 1.1. El resultado «42»

El capítulo anterior terminó con una regla que acompañará todo el tratado: un cálculo físico no se cierra cuando aparece un número. Debemos todavía interpretarlo respecto del sistema, las premisas, el régimen y la observación.

Ahora haremos esa regla más concreta.

Supongamos que resolvemos un problema y escribimos:

$$
42.
$$

¿Es una respuesta física?

No podemos saberlo.

Podría significar:

- $42\,\mathrm m$;
- $42\,\mathrm s$;
- $42\,\mathrm{kg}$;
- $42$ partículas;
- un índice sin dimensión;
- un número puramente matemático que todavía no ha recibido ninguna interpretación física.

Shankar formula esta dificultad de manera pedagógica al introducir el movimiento unidimensional: una posición necesita una unidad de longitud y un tiempo necesita una unidad de tiempo; un resultado numérico sin esa información no permite siquiera decidir qué se está afirmando.[^s1-shankar-units]

La primera distinción del capítulo será, por tanto:

$$
\boxed{
\text{número}
\neq
\text{valor de una magnitud}
\neq
\text{magnitud física}.
}
$$

Esta separación parece elemental. Sin embargo, una gran cantidad de errores posteriores —conversiones mal hechas, ecuaciones dimensionalmente imposibles, argumentos de funciones con unidades incompatibles— puede rastrearse hasta su pérdida.

### 1.2. Magnitud física

El vocabulario metrológico internacional llama **magnitud** a una propiedad de un fenómeno, cuerpo o sustancia cuya magnitud puede expresarse mediante un número y una referencia.[^s1-vim-quantity]

Para nuestro tratado necesitaremos una formulación ligeramente orientada al modelado.

::: {.ma-block .ma-definicion #fpm-i-02-d01}
**Definición 1 — Magnitud física**
Una **magnitud física** es una propiedad cuantificable de un fenómeno, sistema o proceso que el modelo trata como comparable y representable mediante valores de magnitud.
:::

Ejemplos:

- longitud;
- duración;
- masa;
- temperatura termodinámica;
- velocidad;
- energía.

La definición no dice todavía **cómo** medir cada magnitud.

Tampoco afirma que toda propiedad física sea una magnitud.

El color nominal de una etiqueta, por ejemplo, puede ser una propiedad del sistema sin constituir por sí mismo una magnitud en el sentido metrológico adoptado aquí. En cambio, una longitud de onda asociada con cierta radiación sí es una magnitud.

Debemos separar entonces:

$$
\text{propiedad física}
$$

de:

$$
\text{propiedad cuantificable según una estructura de comparación}.
$$

Esta distinción prolonga el capítulo 1: antes de escribir una ecuación, el modelo ya ha seleccionado qué propiedades considera relevantes.

### 1.3. Una magnitud no es uno de sus valores particulares

Consideremos la **longitud**.

«Longitud» designa una clase o tipo de magnitud.

Pero la longitud de una barra concreta puede tener un valor particular:

$$
2\,\mathrm m.
$$

Otra barra puede tener:

$$
0.30\,\mathrm m.
$$

Y una tercera:

$$
1.7\,\mathrm m.
$$

No debemos confundir:

$$
\boxed{
\text{la magnitud longitud}
}
$$

con:

$$
\boxed{
\text{el valor de longitud de un objeto particular}.
}
$$

::: {.ma-block .ma-definicion #fpm-i-02-d02}
**Definición 2 — Valor de una magnitud**
Un **valor de una magnitud** es una especificación cuantitativa de una magnitud particular, expresada mediante un número y una referencia adecuada; cuando la referencia es una unidad de medida, el valor se expresa como número por unidad.
:::

Así, la expresión

$$
L=2\,\mathrm m
$$

contiene varios niveles:

- $L$: símbolo que representa la longitud particular que estamos considerando;
- $2\,\mathrm m$: valor de esa longitud;
- $2$: valor numérico respecto de la unidad elegida;
- $\mathrm m$: unidad.

El BIPM resume esta estructura mediante la idea de que el valor de una magnitud se expresa generalmente como producto de un número y una unidad.[^s1-bipm-quantity-value]

### 1.4. La unidad es una referencia, no un adorno tipográfico

¿Qué trabajo realiza el metro en

$$
L=2\,\mathrm m?
$$

No es una etiqueta decorativa colocada después del número.

Nos proporciona una referencia con la que comparamos el valor de longitud.

::: {.ma-block .ma-definicion #fpm-i-02-d03}
**Definición 3 — Unidad de medida**
Una **unidad de medida** para una magnitud de cierto tipo es una cantidad particular de ese mismo tipo adoptada por convención como referencia para expresar valores de magnitudes comparables.
:::

Si $u$ representa una unidad apropiada para una magnitud $Q$, podemos escribir:

$$
Q=q\,u,
$$

donde $q$ es un número.

Por ejemplo:

$$
L=2\,\mathrm m.
$$

Aquí:

$$
u=1\,\mathrm m
$$

y:

$$
q=2.
$$

La unidad nos permite convertir una comparación física en una representación numérica.

No debemos leer:

$$
2\,\mathrm m
$$

como una yuxtaposición informal entre «el número 2» y «la palabra metro».

Dentro del cálculo de magnitudes, la unidad participa algebraicamente.

### 1.5. El valor numérico depende de la unidad

El BIPM escribe conceptualmente:

$$
\text{valor de magnitud}
=
\text{valor numérico}
\times
\text{unidad}.
$$

Podemos hacerlo explícito.

::: {.ma-block .ma-definicion #fpm-i-02-d04}
**Definición 4 — Valor numérico relativo a una unidad**
Si un valor de magnitud $Q$ se expresa respecto de una unidad $u$ como

$$
Q=q\,u,
$$

llamaremos **valor numérico de $Q$ respecto de $u$** al número $q$. Lo denotaremos

$$
\{Q\}_u:=q.
$$
:::

Equivalentemente:

$$
\{Q\}_u=\frac{Q}{u}.
$$

Esta escritura es importante porque hace visible algo que la notación cotidiana suele ocultar:

$$
\boxed{
\text{el valor numérico depende de la unidad elegida}.
}
$$

La magnitud representada puede permanecer exactamente igual.

### 1.6. La misma longitud, números diferentes

Consideremos una misma longitud física:

$$
L=2\,\mathrm m.
$$

Como:

$$
1\,\mathrm m=100\,\mathrm{cm},
$$

también podemos escribir:

$$
L=200\,\mathrm{cm}.
$$

Y como:

$$
1\,\mathrm m=1000\,\mathrm{mm},
$$

tenemos:

$$
L=2000\,\mathrm{mm}.
$$

Por tanto:

$$
\boxed{
2\,\mathrm m
=
200\,\mathrm{cm}
=
2000\,\mathrm{mm}.
}
$$

Pero:

$$
2\neq200\neq2000.
$$

Los números cambian.

La longitud no.

| Unidad elegida | Valor numérico | Valor de la longitud |
|---|---:|---|
| $\mathrm m$ | $2$ | $2\,\mathrm m$ |
| $\mathrm{cm}$ | $200$ | $200\,\mathrm{cm}$ |
| $\mathrm{mm}$ | $2000$ | $2000\,\mathrm{mm}$ |

::: {.ma-block .ma-metodo #fpm-i-02-mp01}
**Principio 1 — No confundir magnitud, valor, número y unidad**
En una expresión física distinguiremos siempre la magnitud considerada, su valor particular, el valor numérico y la unidad o referencia usada para expresarlo.
:::

::: {.ma-block .ma-metodo #fpm-i-02-mp02}
**Principio 2 — Cambiar la unidad cambia el número, no la magnitud representada**
Cuando dos unidades representan el mismo tipo de magnitud y están relacionadas por un cambio de escala, la misma magnitud física recibe valores numéricos diferentes de manera compensatoria.
:::

### 1.7. Por qué aparece la compensación inversa

Supongamos que tenemos una unidad $u$ y otra unidad $u'$ del mismo tipo.

Sea:

$$
u'=\lambda u,
\qquad
\lambda>0.
$$

Si $u'$ es una unidad **más grande** que $u$, entonces:

$$
\lambda>1.
$$

Por ejemplo:

$$
1\,\mathrm{km}=1000\,\mathrm m.
$$

La misma longitud necesitará menos unidades grandes para expresarse.

Si:

$$
L=3000\,\mathrm m,
$$

entonces:

$$
L=3\,\mathrm{km}.
$$

El número disminuye exactamente en el factor en que aumentó el tamaño de la unidad.

Esto no es una regla memorizada de conversión.

Es una consecuencia algebraica de que estamos representando la **misma magnitud**.

### 1.8. Primera proposición formal

::: {.ma-block .ma-enunciado #fpm-i-02-p01}
**Proposición 1 — Covariancia del valor numérico bajo un cambio multiplicativo de unidad**

Sea $Q$ un valor de magnitud. Supongamos que

$$
Q=q\,u=q'\,u'
$$

y que las unidades del mismo tipo satisfacen

$$
u'=\lambda u,
\qquad
\lambda>0.
$$

Entonces:

$$
\boxed{
q'=\frac{q}{\lambda}.
}
$$
:::

#### Demostración

Partimos de:

$$
Q=q\,u.
$$

También:

$$
Q=q'\,u'.
$$

Por tanto:

$$
q\,u=q'\,u'.
$$

Usando:

$$
u'=\lambda u,
$$

obtenemos:

$$
q\,u=q'\lambda u.
$$

Como $u$ es una unidad no nula, podemos dividir ambos miembros por $u$:

$$
q=\lambda q'.
$$

Finalmente:

$$
q'=\frac{q}{\lambda}.
$$

Por tanto:

$$
\boxed{
q'=\frac{q}{\lambda}.
}
$$

$$
\boxed{\text{QED}}
$$

### 1.9. Interpretación de la Proposición 1

Si agrandamos la unidad por un factor $\lambda$, el valor numérico disminuye por el mismo factor:

$$
u\longrightarrow\lambda u
$$

implica:

$$
q\longrightarrow\frac{q}{\lambda}.
$$

El producto permanece invariante:

$$
q\,u
=
\left(\frac{q}{\lambda}\right)(\lambda u).
$$

Ésta es una primera forma de covariancia de representación:

$$
\boxed{
\text{cambia la representación numérica}
\quad
\text{mientras permanece la magnitud física}.
}
$$

Más adelante veremos una idea análoga cuando cambiemos sistemas de coordenadas.

### 1.10. Ejemplo desarrollado 1 — Metros y kilómetros

Sea:

$$
L=7500\,\mathrm m.
$$

Como:

$$
1\,\mathrm{km}
=
1000\,\mathrm m,
$$

tenemos $\lambda=1000$. Por la Proposición 1:

$$
q'
=
\frac{7500}{1000}
=
7.5.
$$

Luego:

$$
\boxed{
7500\,\mathrm m
=
7.5\,\mathrm{km}.
}
$$

La conversión no consistió en mover mecánicamente una coma.

Consistió en mantener fija la magnitud mientras cambiábamos la referencia utilizada para expresarla.

### 1.11. Ejemplo desarrollado 2 — Segundos y milisegundos

Consideremos:

$$
T=0.032\,\mathrm s.
$$

Como:

$$
1\,\mathrm{ms}
=
10^{-3}\,\mathrm s,
$$

tenemos:

$$
\lambda=10^{-3}.
$$

Por la Proposición 1:

$$
q'
=
\frac{0.032}{10^{-3}}
=
32.
$$

Por tanto:

$$
\boxed{
0.032\,\mathrm s
=
32\,\mathrm{ms}.
}
$$

La unidad disminuyó por un factor $1000$ y el valor numérico aumentó por un factor $1000$.

### 1.12. No todas las conversiones son de escala pura

La Proposición 1 tiene una hipótesis explícita:

$$
u'=\lambda u.
$$

No debemos extenderla fuera de ese caso.

Hay escalas de uso físico en las que la relación entre los números incluye además un desplazamiento de origen. La temperatura Celsius y la temperatura termodinámica en kelvin ofrecen un ejemplo importante.

Por eso no diremos:

> «Toda conversión de unidades es una regla de tres».

La formulación correcta es:

> la Proposición 1 describe los cambios **multiplicativos de unidad**.

El tratamiento preciso de kelvin, grado Celsius y SI aparecerá en §3.

### 1.13. El símbolo de la magnitud no debería depender de la unidad

Si:

$$
L=2\,\mathrm m
$$

y:

$$
L=200\,\mathrm{cm},
$$

el símbolo $L$ no cambia.

Eso expresa:

$$
\boxed{
\text{la magnitud representada es independiente de cómo elijamos expresarla}.
}
$$

Podemos tener:

$$
\{L\}_{\mathrm m}=2
$$

y:

$$
\{L\}_{\mathrm{cm}}=200,
$$

pero ambos corresponden al mismo $L$.

Una ley física no debería depender accidentalmente de que el investigador prefiera metros o centímetros.

### 1.14. Del número a la observación

En el capítulo 1 introdujimos relaciones `[OBS]`.

Ahora podemos refinar esa cadena:

$$
\boxed{
\text{sistema físico}
\longrightarrow
\text{magnitud seleccionada}
\longrightarrow
\text{procedimiento de comparación}
\longrightarrow
\text{valor respecto de una referencia}
\longrightarrow
\text{representación numérica}.
}
$$

Por ejemplo:

$$
[\mathrm{OBS}]
\qquad
L
\longleftrightarrow
\text{procedimiento de medición de longitud}.
$$

Después escogemos una unidad $u=\mathrm m$ y obtenemos:

$$
L=\{L\}_{\mathrm m}\,\mathrm m.
$$

En el capítulo 3 estudiaremos la incertidumbre del procedimiento de medida. Aquí construimos solamente la gramática que permitirá hablar de ella sin confundirla con la unidad.

### 1.15. Un número puro también puede tener significado físico

Debemos evitar el error contrario.

No toda cantidad físicamente significativa necesita llevar un símbolo de unidad distinto de $1$.

Existen magnitudes de **dimensión uno**:

- cocientes entre magnitudes del mismo tipo;
- ciertas fracciones;
- conteos;
- ángulos expresados en radianes, bajo la convención del SI.

Su tratamiento requiere cuidado y se desarrollará en §8.

Por ahora conservamos:

$$
\boxed{
\text{un número aislado no determina por sí mismo su interpretación física}.
}
$$

No afirmamos:

$$
\boxed{
\text{todo número físicamente significativo debe llevar siempre una unidad con nombre}.
}
$$

La segunda afirmación sería falsa.

### 1.16. Ficha de lectura cuantitativa

::: {.ma-block .ma-metodo}
**Ficha de lectura de un valor**
1. **Magnitud:** ¿qué propiedad física representa el símbolo?
2. **Valor:** ¿qué valor particular se atribuye?
3. **Unidad:** ¿qué referencia se utiliza?
4. **Número:** ¿cuál es el valor numérico respecto de esa unidad?
5. **Cambio de unidad:** ¿la transformación es multiplicativa?
6. **Observación:** ¿qué procedimiento conecta la magnitud con el dato?
7. **Interpretación:** ¿el número conserva sentido físico si borramos la referencia?
:::

### 1.17. Ejercicios de §1

::: {.ma-block .ma-enunciado #fpm-i-02-e01}
**Ejercicio 1 — Número, valor o magnitud**

**Tipo:** conceptual · **Nivel:** básico

Considera:

1. $3$;
2. $3\,\mathrm m$;
3. $L=3\,\mathrm m$;
4. «la longitud de la barra»;
5. $\{L\}_{\mathrm m}=3$.

Explica qué representa cada expresión y cuáles no bastan, por sí solas, para identificar un valor físico completo.
:::

#### Solución

1. $3$ es un número. Sin contexto no determina una magnitud.
2. $3\,\mathrm m$ es un valor de longitud, pero no identifica qué objeto posee esa longitud.
3. $L=3\,\mathrm m$ asigna ese valor a la magnitud particular $L$.
4. «La longitud de la barra» identifica una magnitud particular, pero no su valor.
5. $\{L\}_{\mathrm m}=3$ dice que el valor numérico de $L$ respecto del metro es $3$; equivale a $L=3\,\mathrm m$.

La conclusión es:

$$
\boxed{
\text{magnitud},\quad
\text{valor},\quad
\text{número},\quad
\text{unidad}
}
$$

son conceptos relacionados pero no intercambiables.

---

::: {.ma-block .ma-enunciado #fpm-i-02-e02}
**Ejercicio 2 — La misma longitud en tres unidades**

**Tipo:** cálculo · **Nivel:** básico

Una barra tiene:

$$
L=2.35\,\mathrm m.
$$

1. Exprésala en centímetros.
2. Exprésala en milímetros.
3. Calcula $\{L\}_{\mathrm m}$, $\{L\}_{\mathrm{cm}}$ y $\{L\}_{\mathrm{mm}}$.
4. Explica qué cambia y qué permanece invariante.
:::

#### Solución

Como $1\,\mathrm m=100\,\mathrm{cm}$:

$$
2.35\,\mathrm m
=
235\,\mathrm{cm}.
$$

Como $1\,\mathrm m=1000\,\mathrm{mm}$:

$$
2.35\,\mathrm m
=
2350\,\mathrm{mm}.
$$

Así:

$$
\boxed{
L
=
2.35\,\mathrm m
=
235\,\mathrm{cm}
=
2350\,\mathrm{mm}.
}
$$

Y:

$$
\{L\}_{\mathrm m}=2.35,
$$

$$
\{L\}_{\mathrm{cm}}=235,
$$

$$
\{L\}_{\mathrm{mm}}=2350.
$$

Cambian la unidad y el valor numérico. Permanece invariante la longitud física $L$.

---

::: {.ma-block .ma-enunciado #fpm-i-02-e03}
**Ejercicio 3 — Cambio de unidad y cambio de número**

**Tipo:** demostración · **Nivel:** central

Una distancia se expresa como

$$
D=q\,u.
$$

Introducimos

$$
u'=5u.
$$

1. Demuestra que:

$$
\{D\}_{u'}
=
\frac{1}{5}\{D\}_u.
$$

2. Si $\{D\}_u=60$, calcula $\{D\}_{u'}$.
3. Explica por qué sería incorrecto afirmar que la distancia se volvió cinco veces menor.
:::

#### Solución

Tenemos:

$$
D=q\,u=q'\,u'.
$$

Como $u'=5u$:

$$
q\,u=q'(5u).
$$

Dividiendo por $u$:

$$
q=5q'.
$$

Luego:

$$
\boxed{
q'=\frac{q}{5}.
}
$$

Por tanto:

$$
\boxed{
\{D\}_{u'}
=
\frac{1}{5}\{D\}_u.
}
$$

Si $\{D\}_u=60$:

$$
\{D\}_{u'}=\frac{60}{5}=12.
$$

Así:

$$
\boxed{
60u=12u'.
}
$$

La distancia no cambió. La unidad nueva es cinco veces mayor y por eso hacen falta cinco veces menos unidades para representar la misma distancia.

### 1.18. Cierre

Hemos construido la primera capa cuantitativa del tratado:

$$
\boxed{
Q
=
\{Q\}_u\,u.
}
$$

Esta escritura separa:

- la magnitud representada;
- el valor particular;
- la unidad;
- el valor numérico.

Y la Proposición 1 mostró que, bajo:

$$
u'=\lambda u,
$$

el número transforma como:

$$
\{Q\}_{u'}
=
\frac{\{Q\}_u}{\lambda}.
$$

Por tanto:

$$
\boxed{
\text{la física no está contenida en el número aislado}.
}
$$

La sección siguiente profundizará en una pregunta que aquí hemos tratado de manera operativa:

> **¿qué significa que dos magnitudes sean del mismo tipo y puedan compararse mediante una misma unidad?**

Entramos así en:

$$
\boxed{
\text{§2 — Magnitudes, clases de magnitudes y referencias}.
}
$$

---

[^s1-shankar-units]: R. Shankar, *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*, expanded ed., Yale University Press, 2019, cap. 1, §1.3, p. 4.

[^s1-vim-quantity]: JCGM, *International Vocabulary of Metrology — Basic and general concepts and associated terms (VIM)*, 3.ª ed., JCGM 200:2012, entrada 1.1, «quantity», DOI 10.59161/JCGM200-2012.

[^s1-bipm-quantity-value]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01, junio de 2026, §2.1, p. 123, DOI 10.59161/AUEZ1291.
