## §8 — Cantidades de dimensión uno {#fpm-i-02-s08}

### 8.1. Intuir: «adimensional» no significa «sin física»

Consideremos estas cantidades:

- el índice de refracción de un medio;
- el número de Mach;
- una fracción de masa;
- un ángulo plano;
- el número de vueltas de una bobina.

Todas tienen una característica común: su dimensión es

$$
1.
$$

Pero no significan lo mismo.

Un índice de refracción no es un ángulo.

Un ángulo no es un conteo.

Una fracción de masa no es un número de Mach.

Por tanto, la primera intuición que debemos corregir es:

$$
\boxed{
\text{dimensión uno}
\neq
\text{ausencia de significado físico}.
}
$$

El VIM conserva históricamente el término «cantidad adimensional», pero recomienda entenderlo como una **cantidad de dimensión uno**: todos sus exponentes dimensionales son cero. Además, advierte que estas cantidades transmiten más información que un número desnudo.[^s8-vim-dim-one]

### 8.2. Precisar: cantidad de dimensión uno

::: {.ma-block .ma-definicion #fpm-i-02-d20}
**Definición 20 — Cantidad de dimensión uno**
Una **cantidad de dimensión uno** es una magnitud cuya expresión dimensional tiene todos sus exponentes iguales a cero:

$$
[Q]
=
T^0L^0M^0I^0\Theta^0N^0J^0
=
1.
$$
:::

En términos de firmas dimensionales,

$$
\mathbf d(Q)
=
(0,0,0,0,0,0,0).
$$

Esta definición no dice que $Q$ carezca de contenido físico.

Dice que su valor no cambia mediante factores asociados a una reescala independiente de las unidades base.

::: {.ma-block .ma-metodo #fpm-i-02-mp15}
**Principio 15 — Dimensión uno no borra la semántica**
Dos cantidades pueden tener dimensión uno y, sin embargo, pertenecer a tipos físicos diferentes, requerir convenciones distintas y desempeñar papeles distintos dentro de un modelo.
:::

### 8.3. Representar: cociente de magnitudes del mismo tipo

Una fuente frecuente de cantidades de dimensión uno es el cociente de dos magnitudes del mismo tipo.

Si

$$
R=\frac{Q_1}{Q_2}
$$

y

$$
[Q_1]=[Q_2],
$$

entonces

$$
[R]
=
\frac{[Q_1]}{[Q_2]}
=
1.
$$

Por ejemplo, si

$$
R=\frac{\ell_1}{\ell_2},
$$

entonces

$$
[R]
=
\frac{L}{L}
=
1.
$$

Esto explica muchas razones relativas.

Pero no toda cantidad de dimensión uno debe interpretarse simplemente como «una división entre dos números parecidos».

El VIM incluye también:

- ángulo plano;
- ángulo sólido;
- conteos;
- número de Mach;
- índice de refracción.

La igualdad dimensional no colapsa estas interpretaciones.

### 8.4. Una razón conserva información sobre qué se comparó

Supongamos

$$
R=\frac{2\,\mathrm m}{1\,\mathrm m}=2.
$$

El valor final es numéricamente $2$.

Pero la construcción física fue:

$$
\text{longitud}
\div
\text{longitud}.
$$

Si en cambio contamos dos partículas, obtenemos también el número

$$
2,
$$

pero la procedencia conceptual es diferente.

Así:

$$
\boxed{
\text{mismo número}
\not\Rightarrow
\text{misma cantidad física}.
}
$$

Esta observación generaliza §2: la semántica no puede reconstruirse desde el valor numérico final.

### 8.5. La unidad coherente es uno

Para una cantidad de dimensión uno, la unidad SI derivada coherente es

$$
1.
$$

Normalmente el símbolo $1$ no se escribe.

Por ejemplo, un índice de refracción puede aparecer como

$$
n=1.50
$$

y no como

$$
n=1.50\,1.
$$

Sin embargo, el hecho de que la unidad coherente sea uno no significa que cualquier convención de representación sea irrelevante.

El VIM señala que algunas cantidades de dimensión uno emplean unidades especiales o cocientes convencionales.[^s8-vim-unit-one]

### 8.6. Porcentajes y razones escaladas

Una fracción

$$
r=0.25
$$

puede expresarse también como

$$
25\%.
$$

El símbolo

$$
\%
$$

representa el factor

$$
10^{-2}.
$$

Por tanto,

$$
25\%
=
25\times10^{-2}
=
0.25.
$$

Análogamente,

$$
1\,\mathrm{mmol/mol}
=
10^{-3}.
$$

Aquí aparece una distinción útil:

$$
\boxed{
\text{unidad de dimensión uno}
\neq
\text{factor numérico necesariamente igual a }1.
}
$$

La unidad coherente es uno, pero podemos emplear unidades o convenciones escaladas para comunicar mejor ciertos valores.

### 8.7. El ángulo plano: el caso que obliga a pensar

El ángulo plano es una cantidad de dimensión uno en el SI.

Su unidad coherente es el **radián**:

$$
\mathrm{rad}.
$$

Geométricamente, para un círculo de radio $r$ y arco de longitud $s$,

$$
\theta
=
\frac{s}{r}\,\mathrm{rad}.
$$

Como

$$
[s]=[r]=L,
$$

la razón

$$
\frac{s}{r}
$$

tiene dimensión uno.

Pero la SI Brochure advierte que identificar sin más

$$
\mathrm{rad}
=
\frac{\mathrm m}{\mathrm m}
$$

puede ser engañoso: un ángulo no es simplemente cualquier razón de dos longitudes.[^s8-bipm-angle]

Por eso conviene mantener explícitamente

$$
\mathrm{rad}
$$

cuando ayuda a conservar el significado físico.

::: {.ma-block .ma-definicion #fpm-i-02-d21}
**Definición 21 — Ángulo plano en radianes**
Para una circunferencia de radio $r$, el valor angular en radianes asociado a un arco de longitud $s$ es la razón

$$
\theta=\frac{s}{r},
$$

acompañada por la interpretación geométrica de ángulo plano y expresada coherentemente en radianes.
:::

La definición no identifica «ángulo» con «razón de longitudes» como tipos de magnitud.

La razón construye su medida radian.

### 8.8. El radián es dimensión uno, pero no es semánticamente vacío

Tenemos

$$
[\theta]=1.
$$

Sin embargo,

$$
30^\circ
$$

y

$$
\frac{\pi}{6}\,\mathrm{rad}
$$

representan el mismo ángulo con convenciones distintas.

La relación exacta es

$$
360^\circ=2\pi\,\mathrm{rad}.
$$

El grado no es unidad SI, aunque su uso está ampliamente establecido.

El valor numérico depende de la unidad angular:

$$
30
\neq
\frac{\pi}{6}.
$$

Así, incluso una cantidad de dimensión uno puede presentar una transformación no trivial de valor numérico al cambiar su unidad.

Esto refuerza una idea de §1:

$$
\boxed{
\text{dimensión}
\neq
\text{unidad}
\neq
\text{valor numérico}.
}
$$

### 8.9. Ángulo sólido

El ángulo sólido también tiene dimensión uno.

Su unidad coherente es el estereorradián:

$$
\mathrm{sr}.
$$

Para una esfera de radio $r$, si una región de su superficie tiene área $A$, puede escribirse

$$
\Omega
=
\frac{A}{r^2}\,\mathrm{sr}.
$$

Dimensionalmente,

$$
[\Omega]
=
\frac{L^2}{L^2}
=
1.
$$

Pero, igual que con el radián, la SI Brochure advierte que

$$
\mathrm{sr}
=
\frac{\mathrm{m^2}}{\mathrm{m^2}}
$$

no debe interpretarse como si cualquier razón de áreas fuese automáticamente un ángulo sólido.[^s8-bipm-angle]

La interpretación geométrica sigue siendo indispensable.

### 8.10. Poner a prueba una intuición: ¿«1» significa intercambiable?

Consideremos:

$$
n=1.50
$$

para un índice de refracción, y

$$
M=1.50
$$

para un número de Mach.

Ambos tienen dimensión uno.

Ambos pueden tener el mismo valor numérico.

Sin embargo,

$$
n=M
$$

no constituye automáticamente una igualdad física significativa.

El número coincide.

La dimensión coincide.

El tipo de magnitud no necesariamente.

Por tanto:

$$
\boxed{
\text{mismo valor}
+
\text{misma dimensión}
\not\Rightarrow
\text{misma magnitud}.
}
$$

### 8.11. Funciones no algebraicas: aparece una nueva exigencia

En §6 dejamos pendiente expresiones como

$$
\sin x,
$$

$$
e^x,
$$

o

$$
\log x.
$$

Consideremos la serie formal

$$
e^x
=
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots.
$$

Para poder sumar los términos, la Proposición 2 exige que todos tengan la misma dimensión.

El primer término,

$$
1,
$$

tiene dimensión uno.

Por tanto necesitamos

$$
[x]=1.
$$

La misma lógica aparece en las expansiones de seno y coseno.

::: {.ma-block .ma-metodo #fpm-i-02-mp16}
**Principio 16 — Los argumentos de funciones trascendentes deben ser dimensionalmente apropiados**
En expresiones físicas con funciones como exponencial, logaritmo, seno o coseno, el argumento debe construirse como una cantidad de dimensión uno, o mediante una convención equivalente que haga explícita la normalización necesaria.
:::

### 8.12. Exponencial: por qué aparece $t/\tau$

Consideremos

$$
Q(t)=Q_0e^{-t/\tau}.
$$

Aquí

$$
[t]=T
$$

y

$$
[\tau]=T.
$$

Por tanto,

$$
\left[\frac{t}{\tau}\right]
=
1.
$$

El exponente es dimensionalmente admisible.

En cambio,

$$
Q(t)=Q_0e^{-t}
$$

es una escritura incompleta si $t$ representa un tiempo dimensional y no se ha declarado una normalización.

Cambiar segundos por minutos alteraría el número introducido en la exponencial de una manera que no representa la misma relación física.

### 8.13. Logaritmo: no tomar logaritmos de una magnitud desnuda

Supongamos que escribimos

$$
\log p,
$$

donde $p$ es una presión.

Si cambiamos de pascales a kilopascales, el valor numérico de $p$ cambia por un factor.

La expresión depende de la unidad elegida.

En cambio,

$$
\log\left(\frac{p}{p_0}\right)
$$

utiliza una razón de presiones:

$$
\left[\frac{p}{p_0}\right]
=
1.
$$

Al cambiar coherentemente la unidad de ambas,

$$
\frac{\{p\}'}{\{p_0\}'}
=
\frac{\{p\}}{\{p_0\}},
$$

de modo que el argumento permanece invariante.

### 8.14. Seno y coseno: el papel especial del radián

En matemática escribimos

$$
\sin\theta.
$$

Si $\theta$ representa un ángulo físico, el número que entra en la función matemática debe corresponder a su medida coherente, normalmente en radianes.

Por ejemplo,

$$
30^\circ
=
\frac{\pi}{6}\,\mathrm{rad}.
$$

La función matemática recibe entonces el número

$$
\frac{\pi}{6}.
$$

Esto explica por qué el radián ocupa una posición especial en cálculo y física.

No porque el grado sea «incorrecto», sino porque las fórmulas analíticas estándar de derivación, series y límites utilizan naturalmente la medida angular coherente en radianes.

### 8.15. No toda cantidad de dimensión uno es una razón continua

El VIM incluye entre las cantidades de dimensión uno los **números de entidades**.[^s8-vim-dim-one]

Por ejemplo,

$$
N=20
$$

puede representar un conteo.

La dimensión es uno.

Pero este objeto no tiene la misma estructura operacional que una fracción continua como

$$
0.20.
$$

La dimensión no codifica:

- discreción;
- continuidad;
- carácter angular;
- interpretación probabilística;
- interpretación geométrica.

De nuevo:

$$
\boxed{
\text{dimensión}
\neq
\text{estructura física completa}.
}
$$

### 8.16. Mapa conceptual

| Cantidad | Origen conceptual | Dimensión | Representación frecuente |
|---|---|---:|---|
| razón de longitudes | cociente de mismo tipo | $1$ | número |
| fracción de masa | cociente de masas | $1$ | número, % |
| índice de refracción | relación física | $1$ | número |
| número de Mach | cociente de velocidades | $1$ | número |
| ángulo plano | estructura geométrica | $1$ | rad, ° |
| ángulo sólido | estructura geométrica | $1$ | sr |
| conteo | número de entidades | $1$ | entero |

La tabla evita dos simplificaciones:

1. creer que todas son «solo ratios»;
2. creer que, por ser adimensionales, son intercambiables.

### 8.17. Autoexplicación

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Explica sin consultar la tabla:

1. por qué $30^\circ$ y $\pi/6\,\mathrm{rad}$ tienen valores numéricos diferentes pero representan el mismo ángulo;
2. por qué $\log(p)$ es problemático si $p$ conserva dimensión de presión;
3. por qué dos cantidades con firma dimensional nula no tienen por qué pertenecer al mismo tipo físico.
:::

Una respuesta satisfactoria debe distinguir:

$$
\text{dimensión},
\quad
\text{unidad},
\quad
\text{valor numérico},
\quad
\text{significado físico}.
$$

### 8.18. Práctica guiada

::: {.ma-block .ma-enunciado #fpm-i-02-e18}
**Ejercicio 18 — Reconocer dimensión uno**

**Objetivo:** `Recuperación → Consolidación`

**Intenta primero: 3–5 min antes de leer la solución.**

Determina cuáles tienen dimensión uno:

1. $\ell_1/\ell_2$;
2. $v/c$, con $v,c$ velocidades;
3. $m/V$;
4. $p/p_0$;
5. $A/r^2$;
6. $t/\tau$;
7. $F/(ma)$.

Para cada caso explica además qué estructura física podría representar.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

1.

$$
\left[\frac{\ell_1}{\ell_2}\right]=1.
$$

Razón de longitudes.

2.

$$
\left[\frac vc\right]=1.
$$

Razón de velocidades.

3.

$$
\left[\frac mV\right]=ML^{-3}.
$$

No tiene dimensión uno.

4.

$$
\left[\frac p{p_0}\right]=1.
$$

Razón entre presiones.

5.

$$
\left[\frac A{r^2}\right]=1.
$$

Con interpretación geométrica adecuada puede intervenir en un ángulo sólido.

6.

$$
\left[\frac t\tau\right]=1.
$$

Escala temporal normalizada.

7.

Como

$$
[F]=[ma]=MLT^{-2},
$$

tenemos

$$
\left[\frac{F}{ma}\right]=1.
$$

El punto común es dimensional, pero las interpretaciones siguen siendo distintas.
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e19}
**Ejercicio 19 — Diagnóstico de argumentos de funciones**

**Objetivo:** `Diagnóstico — transferencia`

**Intenta primero: 3–5 min antes de leer la solución.**

Examina:

1. $e^{-t}$;
2. $e^{-t/\tau}$;
3. $\log p$;
4. $\log(p/p_0)$;
5. $\sin(\omega t)$, con $[\omega]=T^{-1}$;
6. $\sin(vt)$, con $[v]=LT^{-1}$.

Decide cuáles son dimensionalmente admisibles tal como están escritas.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

**1.** Si $[t]=T$, el argumento conserva dimensión temporal. No está normalizado.

**2.**

$$
\left[\frac t\tau\right]=1.
$$

Es admisible.

**3.** $\log p$ depende de la unidad usada para representar $p$. No es una forma física completa tal como está escrita.

**4.**

$$
\left[\frac p{p_0}\right]=1.
$$

Es admisible.

**5.**

$$
[\omega t]=1.
$$

Es admisible.

**6.**

$$
[vt]=L.
$$

No es admisible como argumento directo del seno sin una escala adicional de longitud.

Por ejemplo:

$$
\sin\left(\frac{vt}{\ell_0}\right)
$$

sí posee argumento de dimensión uno.

Regla:

$$
\boxed{
\text{antes de una función trascendente,
auditar la dimensión de su argumento}.
}
$$
:::

### 8.19. Variar

Si aparece

$$
e^{-kx},
$$

la homogeneidad del argumento exige

$$
[kx]=1.
$$

Por tanto,

$$
[k]=[x]^{-1}.
$$

Si

$$
[x]=L,
$$

entonces

$$
[k]=L^{-1}.
$$

Lo mismo ocurre en

$$
\sin(kx).
$$

El análisis dimensional no determina el valor de $k$, pero sí la dimensión necesaria.

### 8.20. Conectar

Las cantidades de dimensión uno permiten construir **parámetros que comparan escalas**.

En §9 estudiaremos órdenes de magnitud y estimaciones.

En §§10–11 aparecerán razones que controlan aproximaciones y semejanza.

En §12, Buckingham $\Pi$ reorganizará problemas mediante combinaciones

$$
\Pi_1,\Pi_2,\ldots,\Pi_k
$$

de dimensión uno.

Por tanto:

$$
\boxed{
\text{la física compara escalas mediante combinaciones de dimensión uno}.
}
$$

### 8.21. Síntesis

Una cantidad de dimensión uno satisface

$$
[Q]=1,
$$

o

$$
\mathbf d(Q)=\mathbf 0.
$$

Pero:

$$
\boxed{
[Q]=1
\not\Rightarrow
Q\text{ es semánticamente vacío}.
}
$$

Puede representar una razón, un ángulo, un conteo, una fracción, un índice o un parámetro de semejanza.

Además,

$$
e^x,\qquad
\log x,\qquad
\sin x
$$

exigen argumentos construidos de manera dimensionalmente apropiada.

La regla práctica queda:

$$
\boxed{
\text{función trascendente}
\longrightarrow
\text{auditar primero el argumento}.
}
$$

El siguiente paso será:

$$
\boxed{
\text{§9 — Escalas características y órdenes de magnitud}.
}
$$

---

### Notas y fuentes

[^s8-vim-dim-one]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.8, «quantity of dimension one».
[^s8-vim-unit-one]: JCGM, *VIM*, 3.ª ed., entradas 1.9, 1.12 y 1.20.
[^s8-bipm-angle]: BIPM, *SI Brochure*, v4.01 (2026), §§2.3.3–2.3.4, pp. 132–136, y §5.4.7, pp. 146–147.
