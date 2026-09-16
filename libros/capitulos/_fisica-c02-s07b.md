### 7.15. Variación: usar firmas para localizar un error

Sea

$$
R=A+B+C.
$$

Supongamos:

$$
\mathbf d(A)
=
(-2,2,1,0,0,0,0),
$$

$$
\mathbf d(B)
=
(-2,2,1,0,0,0,0),
$$

$$
\mathbf d(C)
=
(-3,2,1,0,0,0,0),
$$

y

$$
\mathbf d(R)
=
(-2,2,1,0,0,0,0).
$$

No necesitamos reconstruir inmediatamente los nombres físicos de las magnitudes.

Vemos que $C$ difiere solo en el exponente temporal:

$$
-3
$$

en lugar de

$$
-2.
$$

Esto orienta el diagnóstico:

> el término sospechoso contiene probablemente un factor temporal adicional o faltante.

La firma dimensional funciona así como una herramienta de **localización**, no solo de clasificación.

### 7.16. Qué no puede detectar el análisis dimensional

Una auditoría dimensional puede no advertir:

#### Coeficientes numéricos incorrectos

$$
E=2mv^2
$$

y

$$
E=\frac12 mv^2
$$

tienen la misma dimensión.

#### Signos incorrectos

$$
A+B=C
$$

y

$$
A-B=C
$$

pueden ser igualmente homogéneas.

#### Dependencias funcionales distintas con igual dimensión

Dos funciones diferentes pueden producir la misma dimensión final.

#### Hipótesis físicas incorrectas

Una ecuación puede utilizar una aproximación fuera de régimen y seguir siendo homogénea.

#### Confusión entre magnitudes de igual dimensión

Presión y densidad de energía pueden compartir dimensión sin ser intercambiables en cualquier contexto.

Ésta es la frontera conceptual de la herramienta.

### 7.17. Lectura de una auditoría: estrategia global y pasos locales

práctica guiada exige distinguir la estrategia de las manipulaciones.

En una auditoría dimensional:

#### Estrategia global

Queremos comprobar si la estructura de la ecuación puede permanecer independiente de la elección de unidades.

#### Pasos locales

Calculamos dimensiones, sumamos exponentes y comparamos firmas.

No debemos confundir ambos niveles.

Las operaciones algebraicas son el mecanismo.

La razón física de hacerlas es la invariancia estructural expresada por la Proposición 2.

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Explica en tus propias palabras:

1. por qué una firma dimensional diferente detecta un problema en una suma;
2. por qué una firma dimensional igual no basta para probar una ley;
3. qué papel cumple la Proposición 2 dentro del protocolo de auditoría.
:::

Si las tres respuestas pueden darse sin recurrir a una fórmula memorizada, la herramienta empieza a estar comprendida y no solo aplicada.

### 7.18. Conectar con el protocolo general de Física para matemáticos

En `el capítulo 1` fijamos la cadena:

$$
\text{fenómeno}
\to
\text{modelo}
\to
\text{predicción}
\to
\text{contraste}
\to
\text{revisión}.
$$

La auditoría dimensional se inserta dentro de la construcción y revisión del modelo:

$$
\boxed{
\text{representación}
\to
\text{ecuaciones}
\to
\text{auditoría dimensional}
\to
\text{derivación matemática}
\to
\text{interpretación física}.
}
$$

No sustituye:

- observaciones;
- teoría;
- modelización;
- prueba matemática;
- contraste experimental.

Cumple una función más específica:

$$
\boxed{
\text{descartar incompatibilidades estructurales baratas de detectar}.
}
$$

### 7.19. Práctica guiada práctica guiada

::: {.ma-block .ma-enunciado #fpm-i-02-e17}
**Ejercicio 17 — Auditoría dimensional completa**

**Objetivo:** `Síntesis — auditoría`

**Intenta primero: 3–5 min antes de leer la solución.**

Los cuatro apartados siguen la secuencia:

$$
\text{Recuperación}
\to
\text{Consolidación}
\to
\text{Diagnóstico}
\to
\text{Síntesis}.
$$

### A. Recuperación

Calcula las firmas dimensionales de:

$$
v,\qquad a,\qquad F,\qquad E.
$$

Usa el orden

$$
(T,L,M,I,\Theta,N,J).
$$

### B. Consolidación

Audita:

$$
x=x_0+v_0t+\frac12 at^2.
$$

Verifica la dimensión de cada término y explica por qué el factor $1/2$ no interviene en el control dimensional.

### C. Diagnóstico

Un estudiante propone:

$$
v=v_0+at^2.
$$

Otro responde:

> «La fórmula puede arreglarse cambiando el valor numérico de $a$.»

Identifica el error dimensional y explica por qué la respuesta no puede repararlo.

### D. Síntesis

Considera:

$$
Q=C\,m^\alpha v^\beta,
$$

donde $C$ es un número puro y queremos que $Q$ tenga dimensión de energía.

1. Determina las condiciones sobre $\alpha$ y $\beta$.
2. Decide si esas condiciones determinan completamente una ley física para la energía.
3. Clasifica qué parte de tu razonamiento es dimensional y qué información adicional sería física.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

### A. Recuperación

Para velocidad:

$$
[v]=LT^{-1},
$$

por tanto

$$
\boxed{
\mathbf d(v)
=
(-1,1,0,0,0,0,0).
}
$$

Para aceleración:

$$
[a]=LT^{-2},
$$

entonces

$$
\boxed{
\mathbf d(a)
=
(-2,1,0,0,0,0,0).
}
$$

Para fuerza:

$$
[F]=MLT^{-2},
$$

de modo que

$$
\boxed{
\mathbf d(F)
=
(-2,1,1,0,0,0,0).
}
$$

Para energía:

$$
[E]=ML^2T^{-2},
$$

luego

$$
\boxed{
\mathbf d(E)
=
(-2,2,1,0,0,0,0).
}
$$

### B. Consolidación

Tenemos:

$$
[x]=[x_0]=L.
$$

Además:

$$
[v_0t]
=
LT^{-1}T
=
L.
$$

Y:

$$
[at^2]
=
LT^{-2}T^2
=
L.
$$

Por tanto:

$$
\boxed{
[x]
=
[x_0]
=
[v_0t]
=
[at^2]
=
L.
}
$$

La expresión es dimensionalmente homogénea.

El factor

$$
\frac12
$$

es un número puro y no introduce ninguna potencia de las dimensiones base.

### C. Diagnóstico

La velocidad tiene dimensión:

$$
[v]=LT^{-1}.
$$

También:

$$
[v_0]=LT^{-1}.
$$

Pero:

$$
[at^2]
=
LT^{-2}T^2
=
L.
$$

Por tanto:

$$
LT^{-1}\neq L.
$$

La ecuación intenta sumar una velocidad y una longitud.

Cambiar el valor numérico de $a$ no altera:

$$
[a]=LT^{-2}.
$$

Luego ningún ajuste numérico puede convertir

$$
at^2
$$

en una velocidad.

El fallo es dimensional, no numérico.

### D. Síntesis

Queremos:

$$
[Q]
=
ML^2T^{-2}.
$$

Como:

$$
[m^\alpha v^\beta]
=
M^\alpha
(LT^{-1})^\beta,
$$

obtenemos:

$$
[Q]
=
M^\alpha
L^\beta
T^{-\beta}.
$$

Igualamos exponentes con:

$$
M^1L^2T^{-2}.
$$

Para masa:

$$
\alpha=1.
$$

Para longitud:

$$
\beta=2.
$$

Para tiempo:

$$
-\beta=-2,
$$

que es compatible con:

$$
\beta=2.
$$

Por tanto:

$$
\boxed{
\alpha=1,\qquad \beta=2.
}
$$

La forma dimensional es:

$$
Q=Cmv^2.
$$

Sin embargo, el análisis dimensional no determina $C$.

Tampoco demuestra que una magnitud física concreta llamada energía deba depender exactamente de $mv^2$ en todo modelo y régimen.

El razonamiento dimensional determinó los exponentes compatibles con la dimensión objetivo bajo las hipótesis dadas.

La identificación física de $Q$, el valor de $C$ y el régimen de validez requieren información adicional.

Esta separación es el objetivo de la práctica:

$$
\boxed{
\text{restricción dimensional}
\neq
\text{ley física completa}.
}
$$
:::

### 7.20. Variar el método

El ejercicio anterior usó una dimensión objetivo conocida.

Podemos variar el problema de tres maneras.

#### Variación 1 — Ocultar una dimensión

Dar una ecuación y pedir la dimensión de una constante desconocida.

#### Variación 2 — Ocultar un exponente

Dar una forma como

$$
Q=AX^\alpha Y^\beta
$$

y usar homogeneidad para restringir $\alpha,\beta$.

#### Variación 3 — Insertar un término defectuoso

Dar una ecuación casi correcta y pedir localizar exactamente el primer término incompatible.

Las tres variaciones practican actividades cognitivas distintas:

- reconstrucción;
- inferencia;
- diagnóstico.

El análisis dimensional se vuelve más potente cuando el lector puede pasar de una a otra sin depender de una plantilla memorizada.

### 7.21. Red conceptual

§7 conecta directamente con lo ya construido:

$$
\boxed{
\text{§1 cambio de unidad}
\to
\text{§5 dimensión}
\to
\text{§6 homogeneidad}
\to
\text{§7 auditoría}.
}
$$

Y prepara:

$$
\boxed{
\text{§8 cantidades de dimensión uno}
}
$$

porque funciones como seno, exponencial y logaritmo requieren un análisis especial de sus argumentos;

$$
\boxed{
\text{§10–§12 inferencia dimensional y semejanza}
}
$$

porque las firmas dimensionales pueden organizarse como ecuaciones lineales entre exponentes.

La firma dimensional introducida aquí será, por tanto, una herramienta reutilizable y no una notación decorativa.

### 7.22. Qué debe haber cambiado en la comprensión

Al cerrar la sección, el lector no debería limitarse a saber «comprobar unidades».

Debe poder:

1. representar una magnitud mediante su firma dimensional;
2. traducir productos, cocientes y potencias a operaciones con firmas;
3. auditar sumas e igualdades usando la Proposición 2;
4. localizar un término dimensionalmente incompatible;
5. distinguir un fallo dimensional de uno algebraico o físico;
6. explicar por qué pasar el control dimensional no demuestra una ley;
7. reconocer cuándo el análisis dimensional solo restringe una forma y cuándo se necesita información física adicional.

Podemos condensar el método completo:

$$
\boxed{
\text{significado}
\to
\text{dimensión}
\to
\text{firma}
\to
\text{operación}
\to
\text{comparación}
\to
\text{diagnóstico}
\to
\text{control físico}.
}
$$

La siguiente sección aborda la frontera que hemos pospuesto desde §6:

$$
\boxed{
\text{§8 — Cantidades de dimensión uno}.
}
$$

Allí veremos por qué «adimensional» no significa «sin significado físico» y por qué los argumentos de ciertas funciones requieren un tratamiento especial.

---

### Notas y fuentes

[^s7-zorich-audit]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §§1.1–1.2, pp. 5–8.
