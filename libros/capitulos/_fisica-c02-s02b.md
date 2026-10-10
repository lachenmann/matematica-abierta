### 2.17. Misma magnitud general, instancias diferentes

La palabra «longitud» puede aparecer en dos niveles.

Por un lado, hablamos del tipo general:

$$
\text{longitud}.
$$

Por otro, hablamos de una longitud concreta:

$$
L_{\mathrm{barra}}.
$$

La primera organiza una clase de magnitudes comparables.

La segunda es una instancia física particular.

Para evitar una carga terminológica excesiva no construiremos una teoría formal de universales e instancias.

Pero mantendremos la distinción operativa:

$$
\boxed{
\text{tipo de magnitud}
\neq
\text{magnitud particular de un sistema}.
}
$$

### 2.18. Una advertencia sobre temperaturas y escalas

El lenguaje de comparación por razón funciona limpiamente para magnitudes como longitud y masa.

No todas las escalas cuantitativas se comportan de la misma manera.

En particular, la temperatura Celsius introduce un desplazamiento convencional de origen respecto de la temperatura termodinámica expresada en kelvin.

Por eso debemos evitar inferencias del tipo:

> «$20\,^{\circ}\mathrm C$ es el doble de $10\,^{\circ}\mathrm C$».

Esa afirmación no expresa una razón de temperaturas termodinámicas.

El caso será tratado cuidadosamente en §3.

Aquí cumple una función conceptual:

$$
\boxed{
\text{que algo se exprese con un número y una referencia}
\not\Rightarrow
\text{que todas las operaciones numéricas tengan interpretación física directa}.
}
$$

### 2.19. Segunda regla metodológica de §2

::: {.ma-block .ma-metodo #fpm-i-02-mp04}
**Principio 4 — La notación de unidad no determina por sí sola el significado físico**
Una expresión de unidad restringe las magnitudes que puede representar, pero la identificación del tipo de magnitud exige además el contexto físico, la definición de la cantidad y su regla de interpretación.
:::

Así, ante:

$$
2\,\mathrm{s}^{-1},
$$

no preguntaremos únicamente:

> «¿qué unidad tiene?»

También preguntaremos:

> «¿qué magnitud física representa?»

### 2.20. Ficha de lectura: identificar correctamente una cantidad física

A partir de ahora, cuando encontremos una cantidad en una fórmula, podemos aplicar esta ficha mínima.

1. **Sistema:** ¿de qué sistema o fenómeno es propiedad?
2. **Magnitud particular:** ¿qué cantidad concreta representa el símbolo?
3. **Tipo:** ¿a qué clase de magnitud pertenece?
4. **Referencia:** ¿respecto de qué se expresa su valor?
5. **Unidad:** si corresponde, ¿qué unidad se ha elegido?
6. **Valor numérico:** ¿qué número resulta respecto de esa unidad?
7. **Interpretación:** ¿cómo se conecta con el modelo y con `[OBS]`?

Esta secuencia impide reducir prematuramente la física a números.

### 2.21. Ejercicios de §2

::: {.ma-block .ma-enunciado #fpm-i-02-e04}
**Ejercicio 4 — Misma unidad, magnitudes diferentes**

**Tipo:** conceptual · **Nivel:** central

Considera los siguientes casos conceptuales:

1. una frecuencia expresada en $\mathrm{s}^{-1}$;
2. una actividad radiactiva expresada en $\mathrm{s}^{-1}$;
3. la longitud de onda de una señal expresada en metros;
4. el diámetro de una esfera expresado en metros;
5. una duración expresada en segundos.

Responde:

a. ¿Qué pares pertenecen claramente al mismo tipo de magnitud?
b. ¿Qué ejemplo muestra que una misma expresión de unidad no basta para identificar el tipo de magnitud?
c. ¿Por qué tener el mismo valor numérico tampoco basta?
d. Explica por qué $2\,\mathrm{Hz}$ y $2\,\mathrm{Bq}$ no deben interpretarse como la misma magnitud física aunque ambas unidades sean algebraicamente equivalentes a $\mathrm{s}^{-1}$.
:::

#### Solución del ejercicio 4

#### a. Magnitudes del mismo tipo

La longitud de onda y el diámetro son ambas longitudes.

Por tanto pertenecen al mismo tipo de magnitud:

$$
\boxed{\text{longitud}.}
$$

Pueden compararse mediante una misma familia de unidades de longitud.

La frecuencia y la actividad radiactiva no se consideran, en general, magnitudes del mismo tipo.

La duración pertenece al tipo tiempo o duración y tampoco coincide con los anteriores.

#### b. Misma expresión de unidad

Frecuencia y actividad ofrecen el ejemplo buscado:

$$
[\text{frecuencia}]\sim\mathrm{s}^{-1},
$$

$$
[\text{actividad}]\sim\mathrm{s}^{-1}.
$$

Sin embargo, representan conceptos físicos distintos.

Por eso el SI usa nombres especiales diferentes:

$$
\mathrm{Hz}
$$

y:

$$
\mathrm{Bq}.
$$

La lección es:

$$
\boxed{
\text{misma expresión algebraica de unidad}
\not\Rightarrow
\text{mismo tipo de magnitud}.
}
$$

#### c. Mismo valor numérico

Supongamos:

$$
L=2\,\mathrm m
$$

y:

$$
T=2\,\mathrm s.
$$

Entonces ambos valores numéricos son $2$, pero una cantidad es longitud y la otra duración.

Por tanto:

$$
\boxed{
\{L\}_{\mathrm m}=\{T\}_{\mathrm s}
\not\Rightarrow
L\text{ y }T\text{ son del mismo tipo}.
}
$$

#### d. Hertz frente a becquerel

Tenemos las igualdades de unidades:

$$
1\,\mathrm{Hz}=1\,\mathrm{s}^{-1},
$$

$$
1\,\mathrm{Bq}=1\,\mathrm{s}^{-1}.
$$

Pero los nombres especiales señalan usos físicos diferentes:

- hertz para frecuencia;
- becquerel para actividad de radionúclidos.

Así, aunque:

$$
2=2
$$

y las expresiones algebraicas de unidad coincidan, la interpretación física no coincide.

La cantidad no queda identificada solo por el par «número + forma algebraica de unidad» si hemos perdido el tipo físico que el modelo asigna.

::: {.ma-block .ma-enunciado #fpm-i-02-e05}
**Ejercicio 5 — Diseñar una referencia de medida**

**Tipo:** modelización · **Nivel:** central

Una comunidad aislada desea comparar longitudes antes de adoptar un sistema internacional. Decide conservar una barra y declarar su longitud como una unidad provisional $u$.

1. Explica qué debe significar la afirmación

$$
L=3.7\,u.
$$

2. ¿Por qué $u$ debe representar una longitud y no una masa o una duración?
3. Si otra barra $u'$ tiene una longitud igual a la mitad de $u$, ¿qué valor numérico tendrá la misma longitud $L$ respecto de $u'$?
4. Identifica qué partes del procedimiento son convencionales y qué parte expresa una comparación física.
5. Explica por qué este modelo local no equivale todavía a construir el SI contemporáneo.
:::

#### Solución del ejercicio 5

#### 1. Significado de $L=3.7u$

La expresión afirma que la longitud particular $L$ tiene, respecto de la referencia de longitud $u$, el valor numérico:

$$
\{L\}_u=3.7.
$$

Equivalentemente:

$$
\frac{L}{u}=3.7.
$$

No significa que $3.7$ sea la longitud.

Significa que la longitud $L$ se expresa como $3.7$ veces la referencia elegida.

#### 2. Compatibilidad de tipo

Para formar la razón:

$$
\frac{L}{u},
$$

$L$ y $u$ deben ser magnitudes comparables del mismo tipo.

Como $L$ es una longitud, $u$ debe ser también una longitud.

Una masa o una duración no constituyen una unidad de longitud.

#### 3. Nueva referencia

Tenemos:

$$
u'=\frac12u.
$$

La unidad nueva es dos veces más pequeña.

Por la Proposición 1, si:

$$
u'=\lambda u
$$

con:

$$
\lambda=\frac12,
$$

entonces el nuevo valor numérico es:

$$
q'=\frac{q}{\lambda}
=
\frac{3.7}{1/2}
=
7.4.
$$

Por tanto:

$$
\boxed{
L=7.4\,u'.
}
$$

La magnitud no cambió.

Cambió la referencia.

#### 4. Convención y comparación física

Es convencional:

- elegir cierta barra como referencia;
- llamarla $u$;
- adoptar esa referencia de manera común.

La comparación física consiste en establecer la relación entre la longitud que queremos expresar y la longitud de referencia.

Podemos esquematizar:

$$
\boxed{
\text{convención de referencia}
+
\text{comparación física}
\longrightarrow
\text{valor numérico}.
}
$$

#### 5. Por qué no es todavía el SI

El ejercicio construye un sistema local muy simple basado en una barra material.

El SI contemporáneo es una estructura internacional mucho más precisa: sus unidades se definen mediante valores fijados de constantes definitorias y requieren procedimientos de realización y trazabilidad metrológica.

Por tanto:

$$
\boxed{
\text{referencia local mediante una barra}
\neq
\text{definición moderna del SI}.
}
$$

El SI será el objeto de §3.

### 2.22. Síntesis

§1 mostró que:

$$
\boxed{
Q=\{Q\}_u\,u.
}
$$

§2 ha añadido la condición estructural que esa escritura presupone:

$$
\boxed{
Q\text{ y }u\text{ deben pertenecer al mismo tipo de magnitud}.
}
$$

Definimos:

- la Definición 5 — tipo de magnitud;
- la Definición 6 — referencia de un valor de magnitud.

Y fijamos dos principios:

$$
\boxed{
\text{comparabilidad física antes que comparación numérica}
}
$$

y:

$$
\boxed{
\text{la unidad no determina por sí sola el significado físico}.
}
$$

Las cuatro negaciones que debemos conservar son:

$$
\boxed{
\text{mismo número}
\not\Rightarrow
\text{mismo tipo},
}
$$

$$
\boxed{
\text{misma letra}
\not\Rightarrow
\text{mismo tipo},
}
$$

$$
\boxed{
\text{misma expresión de unidad}
\not\Rightarrow
\text{mismo tipo},
}
$$

y:

$$
\boxed{
\text{misma clase de magnitud}
\not\Rightarrow
\text{misma magnitud particular}.
}
$$

El siguiente paso será construir el sistema de unidades que usaremos de manera predominante en el tratado:

$$
\boxed{
\text{§3 — El Sistema Internacional contemporáneo}.
}
$$

Allí distinguiremos cuidadosamente:

- las siete magnitudes base;
- las siete unidades base;
- las siete constantes definitorias;
- definición de una unidad;
- realización práctica;
- prefijos y escritura correcta de símbolos.

---

[^s2-vim-kind]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.2, «kind of quantity».
[^s2-vim-unit]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.9, «measurement unit».
[^s2-vim-value]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.19, «quantity value».
