## §7 — El análisis dimensional como auditoría {#fpm-i-02-s07}

### 7.1. Por qué aparece: una ecuación puede parecer razonable y estar mal construida

Consideremos la expresión

$$
x=x_0+v_0t+\frac12 at.
$$

A primera vista tiene una apariencia familiar:

- posición inicial;
- velocidad;
- aceleración;
- tiempo.

Incluso contiene los símbolos que esperaríamos encontrar en un problema de movimiento.

Sin embargo, antes de sustituir un solo número podemos preguntar:

$$
\boxed{
\text{¿pueden sumarse físicamente estos términos?}
}
$$

Tenemos

$$
[x]=L,
$$

$$
[x_0]=L,
$$

$$
[v_0t]
=
LT^{-1}T
=
L,
$$

pero

$$
[at]
=
LT^{-2}T
=
LT^{-1}.
$$

El último término tiene dimensión de velocidad, no de longitud.

Por tanto, la expresión falla antes de cualquier cálculo numérico.

Ésta es la función práctica que comenzaremos a atribuir al análisis dimensional:

$$
\boxed{
\text{usar la estructura dimensional para auditar una expresión física}.
}
$$

La palabra **auditar** es deliberada.

No significa derivar toda la física de las dimensiones.

Significa someter una fórmula, un cálculo o un modelo a una prueba estructural que puede descubrir ciertos errores antes de continuar.[^s7-zorich-audit]

### 7.2. Qué podríamos pensar inicialmente

Un lector puede formular una primera intuición:

> «Si las unidades finales son correctas, la ecuación está bien.»

Esta intuición contiene una parte útil y una parte peligrosa.

La parte útil es que una incompatibilidad de unidades puede revelar un problema.

La parte peligrosa es creer que una coincidencia dimensional certifica la física.

Por ejemplo,

$$
E=\frac12 mv^2
$$

y

$$
E=37mv^2
$$

tienen exactamente la misma dimensión:

$$
ML^2T^{-2}.
$$

También la tiene

$$
E=-mv^2.
$$

El análisis dimensional no puede decidir, por sí solo, cuál de estas expresiones describe una energía física en un modelo determinado.

Por eso la intuición inicial debe corregirse:

$$
\boxed{
\text{las dimensiones pueden refutar ciertas formas,
pero no verificar por sí solas una ley}.
}
$$

Esta asimetría ya apareció en el Principio 12.

En §7 la convertiremos en un procedimiento de trabajo.

### 7.3. Primera representación: la ecuación como colección de términos

Cuando vemos

$$
Q_1+Q_2+\cdots+Q_n=R,
$$

la primera representación útil no es todavía numérica.

Separamos la ecuación en términos:

$$
Q_1,\quad Q_2,\quad\ldots,\quad Q_n,\quad R.
$$

Después reemplazamos cada término por su dimensión:

$$
[Q_1],\quad [Q_2],\quad\ldots,\quad [Q_n],\quad [R].
$$

Por la Proposición 2, si la relación pretende ser una ecuación física aditiva independiente de la elección de unidades, necesitamos:

$$
[Q_1]
=
[Q_2]
=
\cdots
=
[Q_n]
=
[R].
$$

Este cambio de representación transforma una expresión física en un problema algebraico sobre exponentes dimensionales.

### 7.4. Segunda representación: la firma dimensional

En §5 escribimos, para una magnitud $Q$,

$$
[Q]
=
T^\alpha
L^\beta
M^\gamma
I^\delta
\Theta^\varepsilon
N^\zeta
J^\eta.
$$

Podemos registrar los mismos datos mediante el vector

$$
\mathbf d(Q)
=
(\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta),
$$

usando el orden fijo

$$
(T,L,M,I,\Theta,N,J).
$$

::: {.ma-block .ma-definicion}
**Definición 18 — Firma dimensional**
La **firma dimensional** de una magnitud $Q$ es el vector ordenado de exponentes de sus dimensiones base:

$$
\mathbf d(Q)
=
(\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta)
$$

cuando

$$
[Q]
=
T^\alpha
L^\beta
M^\gamma
I^\delta
\Theta^\varepsilon
N^\zeta
J^\eta.
$$
:::

Por ejemplo,

$$
[v]=LT^{-1}
$$

corresponde a

$$
\mathbf d(v)
=
(-1,1,0,0,0,0,0).
$$

Para una aceleración,

$$
[a]=LT^{-2},
$$

por lo que

$$
\mathbf d(a)
=
(-2,1,0,0,0,0,0).
$$

Para una fuerza,

$$
[F]=MLT^{-2},
$$

de modo que

$$
\mathbf d(F)
=
(-2,1,1,0,0,0,0).
$$

La firma dimensional no añade nueva física.

Solo reorganiza la información de una manera que facilitará:

- auditorías;
- comparación de términos;
- sistemas de ecuaciones para exponentes;
- el teorema $\Pi$ de Buckingham en §12.

### 7.5. Leer operaciones mediante firmas

La notación vectorial convierte las reglas dimensionales en operaciones muy simples.

#### Producto

Si

$$
Q=AB,
$$

entonces

$$
[Q]=[A][B].
$$

Por tanto,

$$
\boxed{
\mathbf d(Q)
=
\mathbf d(A)
+
\mathbf d(B).
}
$$

#### Cociente

Si

$$
Q=\frac{A}{B},
$$

entonces

$$
\boxed{
\mathbf d(Q)
=
\mathbf d(A)
-
\mathbf d(B).
}
$$

#### Potencia

Si

$$
Q=A^n,
$$

entonces

$$
\boxed{
\mathbf d(Q)
=
n\,\mathbf d(A).
}
$$

#### Suma

Si

$$
Q=A+B
$$

representa una suma física admisible, entonces necesitamos

$$
\boxed{
\mathbf d(Q)
=
\mathbf d(A)
=
\mathbf d(B).
}
$$

La suma es diferente de las otras operaciones.

No combina firmas: exige igualdad de firmas.

### 7.6. Precisar el método: qué es una auditoría dimensional

::: {.ma-block .ma-definicion}
**Definición 19 — Auditoría dimensional**
Una **auditoría dimensional** es el procedimiento de analizar una expresión, ecuación o cadena de cálculo reemplazando sus magnitudes por dimensiones o firmas dimensionales para comprobar la compatibilidad estructural exigida por sus operaciones y localizar posibles inconsistencias.
:::

La definición contiene tres verbos:

1. **analizar**;
2. **comprobar**;
3. **localizar**.

Una auditoría no se limita a pronunciar «correcto» o «incorrecto».

Debe intentar identificar **dónde** aparece la incompatibilidad.

::: {.ma-block .ma-metodo}
**Principio 13 — Auditar la estructura antes de sustituir números**
Cuando una relación física contiene varios términos, parámetros o conversiones, conviene verificar primero su estructura dimensional. Una incompatibilidad detectada en esta etapa evita cálculos numéricos que no pueden reparar el problema.
:::

### 7.7. Protocolo FPM de auditoría dimensional

Aplicaremos el siguiente procedimiento.

#### Paso 1 — Declarar el significado de los símbolos

No comenzamos con letras desnudas.

Escribimos, por ejemplo:

$$
x:\text{ posición},
$$

$$
v:\text{ velocidad},
$$

$$
t:\text{ tiempo}.
$$

Esta etapa evita asignar una dimensión incorrecta a una letra por hábito.

#### Paso 2 — Registrar dimensiones conocidas

Por ejemplo:

$$
[x]=L,
$$

$$
[v]=LT^{-1},
$$

$$
[t]=T.
$$

#### Paso 3 — Descomponer cada término

Si aparece

$$
v^2t,
$$

calculamos:

$$
[v^2t]
=
[v]^2[t].
$$

No intentamos adivinar el resultado visualmente.

#### Paso 4 — Simplificar dimensiones o firmas

Tenemos

$$
[v^2t]
=
(LT^{-1})^2T
=
L^2T^{-1}.
$$

#### Paso 5 — Aplicar la regla algebraica pertinente

- producto: multiplicar dimensiones;
- cociente: dividir;
- potencia: elevar;
- suma o igualdad aditiva: exigir igualdad dimensional.

#### Paso 6 — Si falla, localizar el primer punto incompatible

No basta decir:

> «las unidades no dan».

Debemos señalar, por ejemplo:

$$
[at]=LT^{-1}
\neq
L=[x_0].
$$

#### Paso 7 — Si pasa, no detener la revisión física

Después del control dimensional todavía debemos preguntar:

- ¿la manipulación algebraica es correcta?;
- ¿los símbolos representan lo que creemos?;
- ¿la ecuación tiene el estatus físico declarado?;
- ¿las hipótesis del modelo son adecuadas?;
- ¿estamos dentro del régimen de validez?;
- ¿la relación está apoyada por una ley, derivación o evidencia?

La auditoría dimensional es una capa de control dentro de una auditoría física más amplia.

### 7.8. Ejemplo desarrollado 1 — Encontrar el término defectuoso

Consideremos:

$$
x=x_0+v_0t+\frac12 at.
$$

#### Intuir

Sabemos que todos los términos sumados a una posición deberían representar contribuciones a una posición.

#### Representar

Asignamos:

$$
[x]=[x_0]=L,
$$

$$
[v_0]=LT^{-1},
$$

$$
[a]=LT^{-2},
$$

$$
[t]=T.
$$

#### Precisar

Calculamos:

$$
[v_0t]
=
LT^{-1}T
=
L,
$$

pero:

$$
[at]
=
LT^{-2}T
=
LT^{-1}.
$$

#### Poner a prueba

Comparamos las firmas:

$$
\mathbf d(x)
=
(0,1,0,0,0,0,0),
$$

$$
\mathbf d(v_0t)
=
(0,1,0,0,0,0,0),
$$

$$
\mathbf d(at)
=
(-1,1,0,0,0,0,0).
$$

El último término no pertenece a la misma clase dimensional.

#### Diagnóstico

La ecuación falla por **inhomogeneidad dimensional**.

La auditoría no nos dice automáticamente cuál era la fórmula pretendida.

Podría faltar, por ejemplo, otro factor de tiempo.

Pero reconstruir ese factor requiere información adicional.

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Antes de continuar, explica sin mirar las ecuaciones:

**¿por qué sustituir valores numéricos de $a$ y $t$ no puede corregir el defecto dimensional de $at$ dentro de una suma de longitudes?**

Una respuesta adecuada debe mencionar que cambiar números no cambia la dimensión del término.
:::

### 7.9. Ejemplo desarrollado 2 — Una fórmula que pasa y puede seguir siendo falsa

Consideremos:

$$
E=7mv^2.
$$

Tenemos

$$
[m]=M
$$

y

$$
[v^2]=L^2T^{-2}.
$$

Por tanto,

$$
[7mv^2]
=
ML^2T^{-2}.
$$

La fórmula posee dimensión de energía.

Pasa el control dimensional.

Pero el análisis dimensional no demuestra que el coeficiente $7$ tenga justificación física.

Tampoco demuestra que la dependencia exacta en $v^2$ sea la ley apropiada en cualquier teoría o régimen.

La fórmula puede ser:

- algebraicamente homogénea;
- dimensionalmente admisible;
- físicamente incorrecta.

Éste es un **no-ejemplo** crucial de la inferencia:

$$
\text{«es homogénea»}
\Longrightarrow
\text{«es una ley correcta»}.
$$

La inferencia es inválida.

### 7.10. Tres clases de fallo que no debemos confundir

La auditoría dimensional ayuda a separar errores distintos.

#### A. Fallo dimensional

Ejemplo:

$$
x=x_0+at.
$$

Tenemos

$$
L\neq LT^{-1}.
$$

El problema es estructural y puede detectarse sin conocer los valores.

#### B. Fallo algebraico

Supongamos una ecuación dimensionalmente correcta:

$$
v=v_0+at.
$$

Si alguien parte de ella y escribe

$$
v-v_0=a+t,
$$

la nueva expresión puede contener un error algebraico aunque el problema original fuera dimensionalmente correcto.

El análisis dimensional puede detectar además que

$$
[a+t]
$$

intenta sumar

$$
LT^{-2}
$$

y

$$
T,
$$

pero la causa inmediata del fallo fue una manipulación algebraica ilegítima.

#### C. Fallo físico o de modelización

Una fórmula puede ser dimensionalmente homogénea y algebraicamente impecable, pero utilizar:

- una ley inaplicable;
- una aproximación fuera de régimen;
- una condición inicial incorrecta;
- una interpretación equivocada;
- una idealización físicamente insuficiente.

Por eso necesitamos una jerarquía de auditorías.

### 7.11. Representación por capas

Organizaremos el diagnóstico así:

$$
\boxed{
\text{dimensional}
\to
\text{algebraica}
\to
\text{semántica}
\to
\text{física}
}
$$

#### Capa 1 — Auditoría dimensional

Pregunta:

> ¿las operaciones combinan dimensiones compatibles?

#### Capa 2 — Auditoría algebraica

Pregunta:

> ¿las transformaciones matemáticas son válidas?

#### Capa 3 — Auditoría semántica

Pregunta:

> ¿cada símbolo conserva el significado físico que le asignamos?

#### Capa 4 — Auditoría física

Pregunta:

> ¿las leyes, hipótesis, idealizaciones y aproximaciones son adecuadas para el sistema y el régimen?

::: {.ma-block .ma-metodo}
**Principio 14 — Identificar el nivel del fallo**
Detectar que una expresión es incorrecta no basta. Siempre que sea posible distinguiremos si el problema es dimensional, algebraico, semántico o físico, porque cada clase de fallo exige una corrección diferente.
:::

Este principio extiende el protocolo de revisión del capítulo 1.

### 7.12. Conflicto típico: «las unidades se cancelan, así que está bien»

Consideremos:

$$
Q=\frac{ab}{c}.
$$

Un estudiante sustituye números y obtiene finalmente una unidad esperada.

¿Basta eso para validar todo el cálculo?

No necesariamente.

Dos errores de conversión pueden compensarse.

Una constante dimensional puede haberse interpretado mal.

Una manipulación algebraica previa puede ser incorrecta.

Incluso una fórmula físicamente falsa puede producir la dimensión esperada.

La revisión correcta no observa únicamente la unidad de la última línea.

Debe seguir la estructura de los términos relevantes.

Por eso:

$$
\boxed{
\text{unidad final plausible}
\not\Rightarrow
\text{cálculo íntegro correcto}.
}
$$

### 7.13. Conflicto típico: «si falla, puedo arreglarlo con una constante»

Supongamos:

$$
x=t^2.
$$

La expresión es inhomogénea:

$$
L\neq T^2.
$$

Podemos introducir una constante $\alpha$ con dimensión

$$
[\alpha]=LT^{-2}
$$

y escribir:

$$
x=\alpha t^2.
$$

Ahora la ecuación es homogénea.

Pero la operación solo muestra que **existe una manera dimensional de completar la forma**.

No demuestra:

- que $\alpha$ sea constante físicamente;
- que $x$ dependa de $t^2$;
- que el modelo describa un sistema real.

La reparación dimensional genera una **familia admisible de formas**, no una ley verificada.

### 7.14. Variación: detectar la dimensión que falta

Aunque §7 no está dedicado todavía a inferir leyes, la auditoría puede localizar información ausente.

Supongamos:

$$
F=k\frac{m_1m_2}{r^2}.
$$

Sin interpretar todavía la ecuación como una ley concreta, podemos preguntar qué dimensión necesitaría $k$ para que la relación fuera homogénea.

Tenemos:

$$
[F]=MLT^{-2},
$$

y

$$
\left[
\frac{m_1m_2}{r^2}
\right]
=
\frac{M^2}{L^2}
=
M^2L^{-2}.
$$

Por tanto,

$$
[k]
=
\frac{MLT^{-2}}{M^2L^{-2}}
=
M^{-1}L^3T^{-2}.
$$

La auditoría ha determinado una restricción necesaria sobre $k$.

No ha demostrado la relación.

Esta forma de razonamiento prepara §§10–12.

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

La práctica guiada exige distinguir la estrategia de las manipulaciones.

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

En el capítulo 1 fijamos la cadena:

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

### 7.19. Práctica guiada

::: {.ma-block .ma-enunciado}
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
