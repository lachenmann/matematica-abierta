::: {.ma-block .ma-definicion #fpm-i-01-d11}
**Definición operativa FPM-I-01-D11 — Variable de estado**
Una **variable de estado** es una cantidad utilizada por el modelo para describir o distinguir estados del sistema.
:::

Si dos estados pueden diferir en una cantidad $q$, podemos representarla esquemáticamente mediante

$$
q:\mathcal S\to V,
$$
donde $V$ es el conjunto de valores posibles.

Esta escritura no afirma todavía que toda variable física sea una función ordinaria en todas las teorías. Es una plantilla apropiada para los modelos clásicos elementales que comenzaremos a estudiar.
### 3.8. Parámetro: fijo dentro del problema, variable entre modelos o realizaciones

Consideremos un péndulo idealizado de longitud $\ell$.

En un experimento concreto podemos fijar $\ell=1\,\mathrm{m}$ y estudiar cómo cambia el estado del péndulo con el tiempo.

Entonces $\ell$ funciona como un **parámetro** del modelo, no como una variable que necesitemos actualizar para describir cada instante.

::: {.ma-block .ma-definicion #fpm-i-01-d12}
**Definición operativa FPM-I-01-D12 — Parámetro**
Un **parámetro** es una cantidad que caracteriza al sistema o al modelo y que se trata como fija al describir una realización determinada, aunque pueda tomar otros valores al comparar sistemas, experimentos o miembros de una familia de modelos.
:::

Podemos escribir una familia de modelos como

$$
\mathcal M_\theta,
$$
donde $\theta$ representa uno o varios parámetros.

La distinción importante no es:

$$
\text{variable}=\text{cambia realmente},\qquad
\text{parámetro}=\text{no cambia realmente}.
$$
Es una distinción de **papel dentro del modelo**.

La longitud de una barra puede tratarse como parámetro en un problema y convertirse en variable de estado en otro problema donde estudiamos su dilatación.
### 3.9. La misma magnitud puede cambiar de papel

Este punto merece un ejemplo explícito.

#### Problema A — Péndulo de longitud fija

La longitud $\ell$ se mide antes del experimento y se mantiene fija.

Rol:

$$
\ell \quad \text{parámetro}.
$$
#### Problema B — Hilo elástico

Ahora la longitud puede cambiar durante el movimiento.

Rol:

$$
\ell \quad \text{variable de estado}.
$$
#### Problema C — Calibración de una regla

La longitud del objeto puede ser precisamente la cantidad que queremos inferir de una observación.

Rol:

$$
\ell \quad \text{cantidad observada o estimada}.
$$
La magnitud física no lleva escrita una etiqueta eterna.

::: {.ma-block .ma-metodo #fpm-i-01-mp06}
**Principio FPM-I-01-MP06 — Los roles pertenecen al modelo**
«Variable», «parámetro», «observable» y «dato de control» describen el papel que una cantidad cumple dentro de una modelización o experimento; una misma magnitud puede desempeñar papeles distintos en problemas diferentes.
:::

### 3.10. Observable: ahora podemos precisar la definición

En §2 dijimos que un observable es una propiedad que el modelo conecta con un procedimiento de observación o medición.

Ahora podemos expresarlo matemáticamente en el caso clásico elemental.

Si el sistema está en un estado $s\in\mathcal S$, un observable puede representarse por una función

$$
O:\mathcal S\to\mathcal V,
$$
de modo que

$$
O(s)
$$
sea el valor que el modelo asocia al estado.

Pero todavía falta la física.

La función matemática por sí sola no nos dice cómo obtener un dato.

Necesitamos una regla `[OBS]` que conecte:

$$
O(s)
\quad\longleftrightarrow\quad
\text{procedimiento experimental}.
$$
Por tanto, un observable físico posee dos caras:

$$
\boxed{
\text{estructura matemática}
+
\text{interpretación operacional}
}.
$$
En mecánica cuántica esta descripción mediante funciones ordinarias sobre estados dejará de ser adecuada y la noción de observable adquirirá una estructura distinta. No adelantaremos esa teoría, pero evitaremos construir una definición que después debamos deshacer.
### 3.11. Estado y observable tampoco son lo mismo

Supongamos que un modelo necesita dos variables para especificar el estado:

$$
s=(q_1,q_2).
$$
Podemos medir solamente una combinación

$$
O(s)=q_1+q_2.
$$
Dos estados diferentes pueden producir el mismo valor observable:

$$
(q_1,q_2)=(1,2)
$$
y

$$
(q_1,q_2)=(2,1)
$$
dan en ambos casos

$$
O=3.
$$
Por tanto,

$$
\boxed{
\text{un valor observable no tiene por qué determinar el estado}
}.
$$
Este ejemplo algebraico elemental anticipa un problema muy general: **reconstruir estados a partir de observaciones**.

Más adelante aparecerá bajo formas mucho más sofisticadas.
### 3.12. Ejemplo desarrollado 6 — La Tierra bajo cinco preguntas

La Tierra ofrece un excelente laboratorio conceptual porque el mismo objeto admite modelos radicalmente distintos.

#### Pregunta A — ¿Dónde está una persona dentro de una habitación?

Podemos tratar el suelo local como un plano.

La curvatura global de la Tierra queda fuera del modelo.

#### Pregunta B — ¿Cuál es una ruta aproximada entre ciudades lejanas?

La geometría esférica se vuelve relevante.

#### Pregunta C — ¿Cuál es la forma de referencia necesaria para geodesia precisa?

Una esfera perfecta puede no bastar; entran modelos más refinados como el geoide y el elipsoide de referencia.

#### Pregunta D — ¿Cómo describimos ciertos efectos de la rotación terrestre?

La Tierra debe poseer orientación y movimiento de rotación; un simple punto deja de contener la información necesaria.

#### Pregunta E — ¿Cómo aproximamos su influencia gravitatoria sobre un objeto muy lejano?

En ciertas circunstancias puede bastar un modelo de masa concentrada.

Podemos resumir:

| Pregunta | Modelo de Tierra | Información retenida |
|---|---|---|
| habitación | plano local | geometría local |
| navegación global | esfera | curvatura global aproximada |
| geodesia | geoide/elipsoide | forma refinada |
| rotación | cuerpo extenso en rotación | orientación y rotación |
| interacción lejana | masa puntual aproximada | masa y posición |

El cambio de modelo cambia también qué entendemos por **estado** de la Tierra.

Una masa puntual necesita mucha menos información que un cuerpo extenso en rotación.
### 3.13. Ejemplo desarrollado 7 — Una habitación y su temperatura

Consideremos la pregunta:

> ¿Cómo cambia la temperatura de una habitación cuando encendemos un calefactor?

Podemos elegir varios sistemas.

#### Sistema 1 — El aire de la habitación

Paredes, ventanas, calefactor y exterior pertenecen al entorno.

#### Sistema 2 — Aire + paredes + muebles

Ahora parte del almacenamiento de energía térmica queda dentro de la frontera.

#### Sistema 3 — Habitación + calefactor

El mecanismo de producción y transferencia de energía puede representarse con mayor detalle.

Una variable que en un modelo era externa puede convertirse en variable interna al ampliar el sistema.

La frontera reorganiza la descripción.
### 3.14. Ejemplo desarrollado 8 — ¿Parámetro u observable?

Supongamos un bloque cuya masa $m$ ha sido medida antes de comenzar un experimento.

Durante una serie de movimientos tratamos

$$
m=0.50\,\mathrm{kg}
$$
como valor fijo.

En el modelo dinámico:

$$
m \quad \text{es parámetro}.
$$
Pero para obtener ese valor realizamos previamente una medición.

En el experimento de calibración:

$$
m \quad \text{fue una cantidad inferida observacionalmente}.
$$
No hay contradicción.

Debemos distinguir:

- **estatus epistemológico:** ¿cómo conocemos el valor?;
- **rol matemático dentro del modelo:** ¿se actualiza con el estado o se mantiene fijo?;
- **rol experimental:** ¿es control, entrada o resultado?

Esta triple distinción será útil en todo el libro.
### 3.15. Una ficha mínima de sistema

Desde ahora podremos construir una ficha preliminar:

::: {.ma-block .ma-metodo}
**Ficha FPM de sistema — versión 1**
- **Pregunta:** ¿qué queremos explicar, calcular o comparar?
- **Sistema:** ¿qué queda dentro?
- **Entorno:** ¿qué queda fuera y puede influir?
- **Estado:** ¿qué información considera suficiente el modelo?
- **Variables de estado:** ¿qué cantidades distinguen estados?
- **Parámetros:** ¿qué cantidades se mantienen fijas dentro de una realización?
- **Observables:** ¿qué propiedades se conectan con procedimientos de medida?
- **Controles experimentales:** ¿qué fijamos deliberadamente?
- **Omisiones:** ¿qué estructura real no estamos representando?
:::

En capítulos posteriores añadiremos:

- unidades;
- escalas;
- incertidumbres;
- condiciones iniciales y de frontera;
- leyes;
- simetrías;
- aproximaciones;
- dominios de validez.
### 3.16. Ejercicios de §3


::: {.ma-block .ma-enunciado #fpm-i-01-e011}
**Ejercicio FPM-I-01-E011 — Tres fronteras para un péndulo**

**Familia:** `E-MOD / CORE`

Construye tres elecciones distintas de sistema para estudiar un péndulo:

1. una en la que el sistema sea mínimo;
2. una en la que el hilo forme parte explícita del sistema;
3. una en la que también la Tierra quede dentro de la frontera.

Para cada elección, indica qué elementos pasan al entorno y qué preguntas podrían justificar esa frontera.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

**Modelo A: esfera únicamente.**

Entorno: hilo, soporte, aire, Tierra.

Puede ser adecuado para una primera descripción de la posición de la esfera cuando los efectos del hilo y de la Tierra se representan de manera externa.

**Modelo B: esfera + hilo.**

Entorno: soporte, aire, Tierra.

Puede ser necesario si nos interesa la masa, elasticidad o vibración del hilo.

**Modelo C: esfera + hilo + Tierra.**

Entorno: aire, soporte y resto del universo, según el problema.
