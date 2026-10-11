---
title: Capítulo 2 — Semántica proposicional
status: published
draft: false
book-id: MA-BOK-0014
editorial-project: TLOG
date-modified: '2026-10-11'
license: GFDL-1.3-or-later
areas:
- fundamentos
level: avanzado
topics:
- logica
number-sections: false
content-id: MA-BCH-0204
content-type: book-chapter
source-id: TLOG-CH02-0001
prerequisites:
- MA-BCH-0203
related:
- MA-BOK-0014
source-sha256: 951947d1cb8df454f51abc33219de7d66850abc0d23adf49cb3519454bf2ff74
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 1](capitulo-01.md) · [Capítulo 3 →](capitulo-03.md)

## 2.0. Función del capítulo

El Capítulo 1 construyó las fórmulas de `CPL` como objetos sintácticos y cerró los principios de inducción, legibilidad única y recursión estructural necesarios para operar sobre ellas. El presente capítulo inicia una capa distinta: **interpretar** esas fórmulas mediante valores de verdad.

La separación es estricta:

$$
\text{sintaxis de }CPL
\neq
\text{semántica de }CPL.
$$

Una fórmula no es verdadera o falsa por su mera pertenencia a $\mathrm{Fm}_{\mathrm{CPL}}$. Su valor dependerá de una valuación y de las funciones de verdad asignadas a los conectivos primitivos.

Este primer microtramo se limita a:

$$
\text{valores de verdad}
\longrightarrow
\text{valuaciones atómicas}
\longrightarrow
\text{evaluación recursiva}
\longrightarrow
\text{satisfacción bajo una valuación}.
$$

Todavía **no** se definen satisfacibilidad de conjuntos, validez, consecuencia semántica global ni equivalencia semántica.

### Fuentes efectivamente cotejadas para este bloque

- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001), §1.2, pp. 20–23.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010), cap. 1, §1.1, pp. 8–9.

Enderton controla directamente las cinco tablas de verdad, la extensión de una asignación y la noción de satisfacción. Rautenberg sirve de contracontrol para la presentación de una valuación como función $\mathrm{PV}\to\{0,1\}$ y para la extensión recursiva a fórmulas.

TLOG adopta una decisión propia: las valuaciones serán **totales** sobre $\mathrm{PV}$. La localidad de la evaluación se demostrará en §2.5, de modo que esta elección no obliga a inspeccionar variables que no aparecen en la fórmula evaluada.

## 2.1. Valores de verdad y funciones semánticas

### Convención 2.1.1 — Semántica bivalente de los conectivos de `CPL` {#tlog-cnv-00005}

Fijamos el conjunto de valores de verdad

$$
\mathbf 2:=\{0,1\},
$$

con la convención

$$
1=\text{verdadero},
\qquad
0=\text{falso}.
$$

Los cinco conectivos primitivos del lenguaje objeto reciben las siguientes funciones metateóricas:

$$
f_{\neg}:\mathbf 2\to\mathbf 2,
$$

$$
f_{\land},f_{\lor},f_{\to},f_{\leftrightarrow}:
\mathbf 2^2\to\mathbf 2.
$$

Quedan fijadas por la tabla:

| $a$ | $b$ | $f_{\neg}(a)$ | $f_{\land}(a,b)$ | $f_{\lor}(a,b)$ | $f_{\to}(a,b)$ | $f_{\leftrightarrow}(a,b)$ |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 1 | 1 |

La columna de $f_{\neg}$ depende sólo de $a$; la repetición de filas sirve únicamente para presentar todas las funciones en una tabla común.

::: {.callout-important}
## Distinción de nivel

Los símbolos $\neg,\land,\lor,\to,\leftrightarrow$ son signos del **lenguaje objeto** cuando forman parte de una fórmula. Las funciones $f_{\neg},f_{\land},f_{\lor},f_{\to},f_{\leftrightarrow}$ viven en la **metateoría** y asignan valores en $\mathbf 2$. No son el mismo objeto.
:::

En particular,

$$
f_{\to}(1,0)=0,
$$

y en los otros tres pares de argumentos $f_{\to}$ vale $1$. Ésta es la condición material clásica que regirá `CPL`.

## 2.2. Valuaciones proposicionales

### Definición 2.2.1 — Valuación de `CPL` {#tlog-def-00010}

Una **valuación proposicional** de `CPL` es una función total

$$
v:\mathrm{PV}\to\mathbf 2.
$$

Denotamos por

$$
\mathrm{Val}_{\mathrm{CPL}}
:=
\mathbf 2^{\mathrm{PV}}
$$

al conjunto de todas las valuaciones de `CPL`.

Una valuación asigna valores únicamente a las variables proposicionales. Aún no hemos definido $v(\varphi)$ para una fórmula compuesta $\varphi$; hacerlo sin justificación confundiría el dato inicial con su extensión recursiva.

## 2.3. Extensión semántica de una valuación

### Metateorema 2.3.1 — Extensión única de una valuación a todas las fórmulas {#tlog-mth-00004}

Para toda valuación

$$
v:\mathrm{PV}\to\mathbf 2
$$

existe una única función

$$
\widehat v:
\mathrm{Fm}_{\mathrm{CPL}}
\to
\mathbf 2
$$

que satisface, para todo $n\ge 1$, toda $\alpha,\beta\in\mathrm{Fm}_{\mathrm{CPL}}$ y todo

$$
\circ\in\{\land,\lor,\to,\leftrightarrow\},
$$

las ecuaciones

$$
\widehat v(p_n)=v(p_n),
$$

$$
\widehat v(E_{\neg}(\alpha))
=
f_{\neg}(\widehat v(\alpha)),
$$

$$
\widehat v(E_{\circ}(\alpha,\beta))
=
f_{\circ}(\widehat v(\alpha),\widehat v(\beta)).
$$

Llamaremos $\widehat v(\varphi)$ al **valor de verdad de $\varphi$ bajo $v$**.

#### Demostración

Aplicamos [TLOG-MTH-00003](capitulo-01.md#tlog-mth-00003) con

$$
A=\mathbf 2,
\qquad
g=v,
$$

$$
F_{\neg}=f_{\neg},
\qquad
F_{\circ}=f_{\circ}
\quad
(\circ\in\{\land,\lor,\to,\leftrightarrow\}).
$$

Todas las funciones requeridas por el teorema de recursión están definidas por [TLOG-CNV-00005](#tlog-cnv-00005), y el dato atómico $g=v$ está tipado por [TLOG-DEF-00010](#tlog-def-00010). Por tanto existe una única función $\widehat v$ que satisface las cinco cláusulas recursivas. $\square$

::: {.callout-note}
## Por qué usamos $\widehat v$

Algunos textos reutilizan el símbolo $v$ para la valuación atómica y para su extensión. TLOG mantiene inicialmente $v$ y $\widehat v$ separados para que dominio y construcción sean recuperables. Más adelante podrá omitirse el sombrero cuando no exista riesgo de ambigüedad.
:::

## 2.4. Satisfacción bajo una valuación

### Definición 2.4.1 — Satisfacción proposicional local {#tlog-def-00011}

Sean

$$
v\in\mathrm{Val}_{\mathrm{CPL}},
\qquad
\varphi\in\mathrm{Fm}_{\mathrm{CPL}}.
$$

Decimos que **$v$ satisface $\varphi$** y escribimos

$$
v\models_{\mathrm{CPL}}\varphi
$$

si y sólo si

$$
\widehat v(\varphi)=1.
$$

Cuando el sistema sea inequívocamente `CPL`, escribiremos simplemente

$$
v\models\varphi.
$$

Su negación,

$$
v\not\models\varphi,
$$

equivale a $\widehat v(\varphi)=0$.

Esta definición introduce **satisfacción por una valuación concreta**. Todavía no se introduce la notación

$$
\Gamma\models\varphi,
$$

que corresponderá a consecuencia semántica y requerirá cuantificar sobre valuaciones.

## 2.5. Localidad de la evaluación

### Lema 2.5.1 — La evaluación depende sólo de las variables que aparecen {#tlog-lem-00002}

Sean $v,w\in\mathrm{Val}_{\mathrm{CPL}}$ y $\varphi\in\mathrm{Fm}_{\mathrm{CPL}}$. Supongamos que

$$
v(p_n)=w(p_n)
$$

para toda variable proposicional $p_n$ que sea subfórmula de $\varphi$, es decir, para todo

$$
p_n\in
\mathrm{PV}
\cap
\operatorname{Sub}_{\mathrm{CPL}}(\varphi).
$$

Entonces

$$
\widehat v(\varphi)
=
\widehat w(\varphi).
$$

En particular,

$$
v\models\varphi
\iff
w\models\varphi.
$$

#### Demostración

Aplicamos [TLOG-MTH-00001](capitulo-01.md#tlog-mth-00001) a la construcción de $\varphi$.

**Caso atómico.** Si $\varphi=p_n$, entonces $p_n\in\operatorname{Sub}_{\mathrm{CPL}}(\varphi)$. Por hipótesis,

$$
v(p_n)=w(p_n),
$$

y por [TLOG-MTH-00004](#tlog-mth-00004),

$$
\widehat v(p_n)=\widehat w(p_n).
$$

**Caso de negación.** Sea $\varphi=E_{\neg}(\alpha)$. Por [TLOG-DEF-00008](capitulo-01.md#tlog-def-00008), toda variable proposicional que aparece como subfórmula de $\alpha$ es también subfórmula de $\varphi$. La hipótesis inductiva da

$$
\widehat v(\alpha)=\widehat w(\alpha).
$$

Aplicando la misma función $f_{\neg}$ a ambos valores,

$$
\widehat v(E_{\neg}(\alpha))
=
\widehat w(E_{\neg}(\alpha)).
$$

**Caso binario.** Sea

$$
\varphi=E_{\circ}(\alpha,\beta).
$$

Toda variable proposicional que sea subfórmula de $\alpha$ o de $\beta$ es subfórmula de $\varphi$. Las dos hipótesis inductivas producen

$$
\widehat v(\alpha)=\widehat w(\alpha),
\qquad
\widehat v(\beta)=\widehat w(\beta).
$$

Entonces

$$
f_{\circ}(\widehat v(\alpha),\widehat v(\beta))
=
f_{\circ}(\widehat w(\alpha),\widehat w(\beta)),
$$

y [TLOG-MTH-00004](#tlog-mth-00004) concluye

$$
\widehat v(\varphi)=\widehat w(\varphi).
$$

Por inducción estructural, el resultado vale para toda fórmula. La equivalencia de satisfacción es inmediata por [TLOG-DEF-00011](#tlog-def-00011). $\square$

::: {.callout-important}
## Consecuencia metodológica

Aunque TLOG define las valuaciones sobre todo $\mathrm{PV}$, el valor de una fórmula sólo depende de las variables que efectivamente aparecen en ella. Esta propiedad permitirá trabajar con tablas finitas sin cambiar la definición global de valuación.
:::

## 2.6. Ejemplo desarrollado — evaluar no es demostrar

Retomemos la fórmula sintáctica del capítulo anterior:

$$
\varphi
=
((p_1\land(\neg p_2))\to p_3).
$$

Sea $v\in\mathrm{Val}_{\mathrm{CPL}}$ tal que

$$
v(p_1)=1,
\qquad
v(p_2)=0,
\qquad
v(p_3)=0.
$$

Los valores de $v$ sobre las demás variables son irrelevantes para $\varphi$ por [TLOG-LEM-00002](#tlog-lem-00002).

Aplicando las cláusulas de [TLOG-MTH-00004](#tlog-mth-00004):

$$
\widehat v((\neg p_2))
=
f_{\neg}(0)
=1,
$$

$$
\widehat v((p_1\land(\neg p_2)))
=
f_{\land}(1,1)
=1,
$$

por lo que

$$
\widehat v(\varphi)
=
f_{\to}(1,0)
=0.
$$

Así,

$$
v\not\models\varphi.
$$

Esto no afirma que $\varphi$ sea inválida, indemostrable ni contradictoria. Sólo afirma que **esta valuación concreta no la satisface**. Las nociones globales se introducirán después.

## 2.9. Estado y próximo frente

Este microtramo **no cierra el Capítulo 2**. Quedan pendientes, como mínimo:

1. satisfacibilidad de fórmulas y conjuntos de fórmulas;
2. validez proposicional;
3. consecuencia semántica $\Gamma\models\varphi$;
4. equivalencia semántica;
5. procedimientos finitos de tabla de verdad y las propiedades básicas que se decida cerrar en este capítulo.

Próximo microtramo:

```text
TLOG-CH02-M02
Satisfacibilidad, validez, consecuencia y equivalencia semántica
```

## 2.10. Modelos de conjuntos de fórmulas

La satisfacción definida en [TLOG-DEF-00011](#tlog-def-00011) es local: relaciona una valuación con una sola fórmula. Para formular satisfacibilidad y consecuencia necesitamos elevarla a conjuntos de fórmulas sin cambiar de nivel semántico.

### Definición 2.10.1 — Satisfacción de un conjunto y conjunto de modelos {#tlog-def-00012}

Sean

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}},
\qquad
v\in\mathrm{Val}_{\mathrm{CPL}}.
$$

Decimos que **$v$ satisface $\Gamma$**, y escribimos

$$
v\models_{\mathrm{CPL}}\Gamma,
$$

si y sólo si

$$
\forall\gamma\in\Gamma,
\quad
v\models_{\mathrm{CPL}}\gamma.
$$

El **conjunto de modelos proposicionales** de $\Gamma$ es

$$
\operatorname{Mod}_{\mathrm{CPL}}(\Gamma)
:=
\{v\in\mathrm{Val}_{\mathrm{CPL}}\mid v\models_{\mathrm{CPL}}\Gamma\}.
$$

Para una fórmula $\varphi$ usaremos la abreviación

$$
\operatorname{Mod}_{\mathrm{CPL}}(\varphi)
:=
\operatorname{Mod}_{\mathrm{CPL}}(\{\varphi\}).
$$

La definición cuantifica metateóricamente sobre fórmulas ya construidas. No convierte $\Gamma$ en una fórmula del lenguaje objeto.

::: {.callout-note}
## El conjunto vacío de premisas

Toda valuación satisface $\varnothing$, pues la condición universal sobre sus miembros es vacua. Por tanto
$$
\operatorname{Mod}_{\mathrm{CPL}}(\varnothing)
=
\mathrm{Val}_{\mathrm{CPL}}.
$$
:::

## 2.11. Satisfacibilidad

### Definición 2.11.1 — Satisfacibilidad e insatisfacibilidad {#tlog-def-00013}

Un conjunto

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}
$$

es **satisfacible** si posee al menos un modelo:

$$
\operatorname{Mod}_{\mathrm{CPL}}(\Gamma)\neq\varnothing.
$$

Es **insatisfacible** si

$$
\operatorname{Mod}_{\mathrm{CPL}}(\Gamma)=\varnothing.
$$

Una fórmula $\varphi$ es satisfacible si $\{\varphi\}$ es satisfacible, es decir, si existe alguna valuación $v$ tal que

$$
v\models\varphi.
$$

Una fórmula insatisfacible se llamará también una **contradicción semántica**. Este uso de “contradicción” no afirma todavía nada acerca de derivabilidad ni de inconsistencia de un cálculo deductivo.

## 2.12. Validez proposicional

### Definición 2.12.1 — Validez {#tlog-def-00014}

Una fórmula

$$
\varphi\in\mathrm{Fm}_{\mathrm{CPL}}
$$

es **válida en `CPL`** si toda valuación la satisface:

$$
\forall v\in\mathrm{Val}_{\mathrm{CPL}},
\quad
v\models\varphi.
$$

Escribiremos

$$
\models_{\mathrm{CPL}}\varphi,
$$

y, cuando `CPL` sea inequívoco,

$$
\models\varphi.
$$

En lógica proposicional clásica también llamaremos **tautología** a una fórmula válida. La validez es una propiedad semántica global: no debe confundirse con ser teorema de un cálculo, noción que se introducirá en el capítulo siguiente.

## 2.13. Consecuencia semántica

### Definición 2.13.1 — Consecuencia semántica proposicional {#tlog-def-00015}

Sean

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}},
\qquad
\varphi\in\mathrm{Fm}_{\mathrm{CPL}}.
$$

Decimos que $\varphi$ es **consecuencia semántica** de $\Gamma$, y escribimos

$$
\Gamma\models_{\mathrm{CPL}}\varphi,
$$

si y sólo si toda valuación que satisface $\Gamma$ satisface también $\varphi$:

$$
\forall v\in\mathrm{Val}_{\mathrm{CPL}},
\quad
\bigl(v\models\Gamma\Longrightarrow v\models\varphi\bigr).
$$

Equivalentemente,

$$
\Gamma\models\varphi
\iff
\operatorname{Mod}_{\mathrm{CPL}}(\Gamma)
\subseteq
\operatorname{Mod}_{\mathrm{CPL}}(\varphi).
$$

::: {.callout-important}
## Separación obligatoria

$$
\Gamma\models\varphi
\neq
\Gamma\vdash\varphi.
$$
La primera expresión acaba de recibir una definición semántica. La segunda quedará reservada para derivabilidad en un cálculo proposicional. Cualquier relación posterior entre ambas requerirá teoremas de corrección y completitud.
:::

## 2.14. Equivalencia semántica

### Definición 2.14.1 — Equivalencia semántica proposicional {#tlog-def-00016}

Sean $\varphi,\psi\in\mathrm{Fm}_{\mathrm{CPL}}$. Decimos que son **semánticamente equivalentes** y escribimos

$$
\varphi\equiv_{\mathrm{CPL}}\psi
$$

si para toda valuación $v$,

$$
v\models\varphi
\iff
v\models\psi.
$$

Por bivalencia, esto equivale a

$$
\widehat v(\varphi)=\widehat v(\psi)
$$

para toda $v\in\mathrm{Val}_{\mathrm{CPL}}$, y también a

$$
\operatorname{Mod}_{\mathrm{CPL}}(\varphi)
=
\operatorname{Mod}_{\mathrm{CPL}}(\psi).
$$

El signo $=$ continúa reservado para identidad sintáctica o igualdad metalingüística de objetos. Por tanto

$$
\varphi=\psi
$$

y

$$
\varphi\equiv_{\mathrm{CPL}}\psi
$$

son afirmaciones de tipos distintos.

## 2.15. Relaciones fundamentales entre las nociones semánticas

### Proposición 2.15.1 — Caracterizaciones básicas {#tlog-pro-00001}

Para todo $\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ y todas $\varphi,\psi\in\mathrm{Fm}_{\mathrm{CPL}}$:

1. $\varphi$ es válida si y sólo si
   $$
   \varnothing\models\varphi.
   $$
2. $\Gamma\models\varphi$ si y sólo si
   $$
   \Gamma\cup\{\neg\varphi\}
   $$
   es insatisfacible.
3. $\varphi\equiv_{\mathrm{CPL}}\psi$ si y sólo si
   $$
   \varphi\models\psi
   \quad\text{y}\quad
   \psi\models\varphi.
   $$
4. $\varphi\equiv_{\mathrm{CPL}}\psi$ si y sólo si
   $$
   \models(\varphi\leftrightarrow\psi).
   $$
5. $\Gamma$ es insatisfacible si y sólo si, para toda fórmula $\chi$,
   $$
   \Gamma\models\chi.
   $$

#### Demostración

1. Por [TLOG-DEF-00012](#tlog-def-00012), toda valuación satisface $\varnothing$. Así, la definición de $\varnothing\models\varphi$ se reduce exactamente a que toda valuación satisfaga $\varphi$, que es [TLOG-DEF-00014](#tlog-def-00014).

2. Si $\Gamma\models\varphi$, no puede existir una valuación que satisfaga simultáneamente $\Gamma$ y $\neg\varphi$: por [TLOG-MTH-00004](#tlog-mth-00004) y la tabla de [TLOG-CNV-00005](#tlog-cnv-00005), satisfacer $\neg\varphi$ equivale a no satisfacer $\varphi$. El argumento inverso es la misma implicación leída contrapositivamente en la metateoría clásica.

3. Por [TLOG-DEF-00015](#tlog-def-00015), $\varphi\models\psi$ significa
   $$
   \operatorname{Mod}_{\mathrm{CPL}}(\varphi)\subseteq\operatorname{Mod}_{\mathrm{CPL}}(\psi),
   $$
   y la consecuencia inversa da la inclusión opuesta. Ambas equivalen a la igualdad de conjuntos de modelos, que es [TLOG-DEF-00016](#tlog-def-00016).

4. Por la tabla de $f_{\leftrightarrow}$,
   $$
   v\models(\varphi\leftrightarrow\psi)
   $$
   si y sólo si $\widehat v(\varphi)=\widehat v(\psi)$. Cuantificando sobre todas las valuaciones obtenemos exactamente [TLOG-DEF-00016](#tlog-def-00016).

5. Si $\Gamma$ no tiene modelos, la implicación
   $$
   v\models\Gamma\Longrightarrow v\models\chi
   $$
   es verdadera para toda valuación y toda $\chi$. Recíprocamente, si $\Gamma$ fuese satisfacible, elija $v\models\Gamma$ y una variable $p_n$; una de $p_n$ o $\neg p_n$ falla bajo $v$, de modo que no todas las fórmulas pueden ser consecuencia de $\Gamma$. $\square$

## 2.16. Propiedades estructurales de la consecuencia semántica

### Proposición 2.16.1 — Reflexividad, monotonía y corte semántico {#tlog-pro-00002}

Sean $\Gamma,\Delta\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ y $\varphi\in\mathrm{Fm}_{\mathrm{CPL}}$.

1. **Reflexividad.** Si $\varphi\in\Gamma$, entonces
   $$
   \Gamma\models\varphi.
   $$
2. **Monotonía.** Si
   $$
   \Gamma\subseteq\Delta
   \quad\text{y}\quad
   \Gamma\models\varphi,
   $$
   entonces
   $$
   \Delta\models\varphi.
   $$
3. **Corte semántico.** Si
   $$
   \Gamma\models\delta
   \quad\text{para todo }\delta\in\Delta,
   $$
   y
   $$
   \Delta\models\varphi,
   $$
   entonces
   $$
   \Gamma\models\varphi.
   $$

#### Demostración

Sea $v$ una valuación arbitraria.

1. Si $v\models\Gamma$ y $\varphi\in\Gamma$, entonces por definición de satisfacción de conjuntos $v\models\varphi$.
2. Si $v\models\Delta$ y $\Gamma\subseteq\Delta$, entonces $v\models\Gamma$; de $\Gamma\models\varphi$ se sigue $v\models\varphi$.
3. Si $v\models\Gamma$, la primera hipótesis implica $v\models\delta$ para cada $\delta\in\Delta$; por tanto $v\models\Delta$. La segunda hipótesis da entonces $v\models\varphi$. $\square$

Estas propiedades pertenecen a la relación semántica recién definida. No son todavía reglas de inferencia de un cálculo objeto.

## 2.17. Ejemplo desarrollado — premisas sin modelo y consecuencia vacua

Consideremos

$$
\Gamma=\{p_1,\neg p_1\}.
$$

No existe $v\in\mathrm{Val}_{\mathrm{CPL}}$ con

$$
v\models p_1
\quad\text{y}\quad
v\models\neg p_1,
$$

porque la segunda condición exige exactamente el valor opuesto a la primera. Por tanto $\Gamma$ es insatisfacible.

En consecuencia, para cualquier fórmula $\chi$,

$$
\Gamma\models\chi.
$$

Este hecho no expresa que desde una contradicción ya hayamos **derivado** $\chi$. Expresa únicamente que no existe una valuación que satisfaga todas las premisas y falle en la conclusión. La comparación con explosión deductiva pertenece al estudio del cálculo y de su corrección/completitud.

## 2.20. Estado y próximo frente

El Capítulo 2 queda en `PARTIAL-CLOSURE / NOT CLOSED` con doce nodos cerrados. El próximo bloque deberá convertir la localidad demostrada en [TLOG-LEM-00002](#tlog-lem-00002) en un procedimiento finito explícito.

```text
TLOG-CH02-M03
Tablas de verdad, decidibilidad semántica y cierre del capítulo
```

## 2.21. Soporte proposicional de una fórmula y de una familia finita

La localidad demostrada en [TLOG-LEM-00002](#tlog-lem-00002) indica que una fórmula no depende de toda valuación global, sino sólo de las variables que efectivamente aparecen en ella. Para convertir esa observación en un procedimiento finito, aislamos primero ese conjunto de variables.

### Definición 2.21.1 — Soporte proposicional {#tlog-def-00017}

Para toda fórmula $\varphi\in\mathrm{Fm}_{\mathrm{CPL}}$, definimos

$$
\operatorname{Var}_{\mathrm{CPL}}(\varphi)
:=
\mathrm{PV}\cap\operatorname{Sub}_{\mathrm{CPL}}(\varphi).
$$

Si $\Phi\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ es una familia **finita** de fórmulas, definimos

$$
\operatorname{Var}_{\mathrm{CPL}}(\Phi)
:=
\bigcup_{\varphi\in\Phi}\operatorname{Var}_{\mathrm{CPL}}(\varphi).
$$

Cuando `CPL` sea inequívoco, omitiremos el subíndice.

## 2.22. Finitud del soporte

### Lema 2.22.1 — Toda fórmula tiene soporte finito {#tlog-lem-00003}

Para toda $\varphi\in\mathrm{Fm}_{\mathrm{CPL}}$, $\operatorname{Var}(\varphi)$ es finito. Más generalmente, si $\Phi\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ es finito, entonces $\operatorname{Var}(\Phi)$ es finito.

#### Demostración

Aplicamos inducción estructural ([TLOG-MTH-00001](capitulo-01.md#tlog-mth-00001)). Si $\varphi=p_n$, entonces
$$
\operatorname{Var}(p_n)=\{p_n\}.
$$
Si $\varphi=(\neg\alpha)$, entonces
$$
\operatorname{Var}(\varphi)=\operatorname{Var}(\alpha),
$$
finito por hipótesis inductiva. Si
$$
\varphi=(\alpha\circ\beta),
\qquad
\circ\in\{\land,\lor,\to,\leftrightarrow\},
$$
entonces
$$
\operatorname{Var}(\varphi)=\operatorname{Var}(\alpha)\cup\operatorname{Var}(\beta),
$$
unión de dos conjuntos finitos. La afirmación para una familia finita sigue porque una unión finita de conjuntos finitos es finita. $\square$

## 2.23. Tabla de verdad de una familia finita

### Definición 2.23.1 — Tabla de verdad {#tlog-def-00018}

Sea
$$
\Phi=\{\varphi_1,\ldots,\varphi_m\}
\subseteq\mathrm{Fm}_{\mathrm{CPL}}
$$
una familia finita, y pongamos $W:=\operatorname{Var}(\Phi)$.

Una **fila** sobre $W$ es una función
$$
a:W\to\mathbf 2.
$$

A cada fila asociamos la valuación total canónica
$$
\overline a:\mathrm{PV}\to\mathbf 2
$$
definida por
$$
\overline a(p)=
\begin{cases}
a(p),& p\in W,\\
0,& p\notin W.
\end{cases}
$$

La **tabla de verdad de $\Phi$** es la tabla finita cuyas filas recorren todas las funciones $a:W\to\mathbf 2$ y cuyas columnas de fórmulas contienen
$$
\widehat{\overline a}(\varphi_1),\ldots,\widehat{\overline a}(\varphi_m).
$$

Si $|W|=n$, la tabla tiene exactamente $2^n$ filas.

La elección del valor $0$ fuera de $W$ es sólo una forma canónica de producir una valuación total. El teorema siguiente mostrará que ningún valor fuera de $W$ puede alterar las columnas de $\Phi$.

## 2.24. Exhaustividad de las tablas de verdad

### Metateorema 2.24.1 — Reducción finita de la evaluación {#tlog-mth-00005}

Sea $\Phi\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ finito y $W=\operatorname{Var}(\Phi)$. Entonces la tabla de verdad de $\Phi$ contiene **todos y sólo** los patrones de valores que las fórmulas de $\Phi$ pueden adoptar bajo valuaciones totales.

Más precisamente, para toda valuación $v\in\mathrm{Val}_{\mathrm{CPL}}$, si
$$
a:=v\!\upharpoonright W,
$$
entonces, para cada $\varphi\in\Phi$,
$$
\widehat v(\varphi)=\widehat{\overline a}(\varphi).
$$
Recíprocamente, cada fila $a:W\to\mathbf 2$ es la restricción a $W$ de la valuación total $\overline a$.

#### Demostración

Sea $v$ una valuación total y $a=v\!\upharpoonright W$. Por construcción,
$$
v(p)=\overline a(p)
$$
para todo $p\in W$. Como $\operatorname{Var}(\varphi)\subseteq W$ para toda $\varphi\in\Phi$, [TLOG-LEM-00002](#tlog-lem-00002) implica
$$
\widehat v(\varphi)=\widehat{\overline a}(\varphi).
$$
La recíproca es inmediata, pues $\overline a$ extiende a $a$. $\square$

::: {.callout-important}
## Consecuencia

La infinitud de $\mathrm{PV}$ no obliga a inspeccionar infinitas valuaciones distintas al evaluar una entrada finita. Toda la información semántica pertinente queda comprimida en las $2^{|W|}$ filas sobre su soporte finito.
:::

## 2.25. Decidibilidad semántica finitaria

### Metateorema 2.25.1 — Procedimientos finitos de decisión en `CPL` {#tlog-mth-00006}

Existen procedimientos finitos que, para entradas sintácticas finitas de `CPL`, deciden:

1. si una fórmula $\varphi$ es satisfacible;
2. si una fórmula $\varphi$ es válida;
3. si dos fórmulas $\varphi,\psi$ son semánticamente equivalentes;
4. si un conjunto **finito** $\Gamma$ es satisfacible;
5. si, para un conjunto **finito** $\Gamma$, $\Gamma\models\varphi$.

#### Demostración

En cada caso se toma la familia finita de fórmulas que aparece en la entrada y se calcula su soporte
$$
W=\operatorname{Var}(\Phi).
$$
Por [TLOG-LEM-00003](#tlog-lem-00003), $W$ es finito. Se enumeran las $2^{|W|}$ funciones
$$
a:W\to\mathbf 2
$$
y se evalúan recursivamente las fórmulas en la valuación canónica $\overline a$.

La evaluación de cada fórmula termina porque recorre una estructura sintáctica finita y en cada paso pasa a constituyentes propios. La enumeración de filas termina porque $W$ es finito.

Por [TLOG-MTH-00005](#tlog-mth-00005), esas filas agotan todos los comportamientos semánticos posibles de la entrada. Por tanto:

- $\varphi$ es satisfacible si y sólo si alguna fila da valor $1$;
- $\varphi$ es válida si y sólo si todas las filas dan valor $1$;
- $\varphi\equiv\psi$ si y sólo si sus columnas coinciden en todas las filas;
- $\Gamma$ es satisfacible si y sólo si existe una fila que da valor $1$ a cada miembro de $\Gamma$;
- $\Gamma\models\varphi$ si y sólo si toda fila que satisface cada miembro de $\Gamma$ da también valor $1$ a $\varphi$.

Cada prueba es, por tanto, una inspección finita exhaustiva. $\square$

::: {.callout-warning}
## Alcance exacto de “decidible”

Este resultado no afirma que la consecuencia desde un conjunto arbitrario e infinito de premisas pueda decidirse mediante una sola tabla finita. Tampoco introduce todavía la teoría general de computabilidad del tratado ni hace una claim de complejidad óptima. Establece únicamente un procedimiento explícito y terminante para los problemas semánticos finitos enumerados arriba.
:::

## 2.26. Ejemplo desarrollado — una tabla, dos controles semánticos

Consideremos
$$
\varphi=p_1\to p_2,
\qquad
\psi=(\neg p_1)\lor p_2.
$$
Su soporte común es $W=\{p_1,p_2\}$, por lo que hay $2^2=4$ filas:

| $p_1$ | $p_2$ | $p_1\to p_2$ | $(\neg p_1)\lor p_2$ |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 0 | 0 | 1 | 1 |

Las dos últimas columnas coinciden, de modo que
$$
p_1\to p_2\equiv_{\mathrm{CPL}}(\neg p_1)\lor p_2.
$$

La misma tabla permite controlar
$$
\{p_1,\ p_1\to p_2\}\models p_2.
$$
En efecto, la única fila que satisface simultáneamente las dos premisas tiene $p_2=1$.

Este ejemplo ilustra la función exacta de una tabla de verdad: no reemplaza la definición de consecuencia, sino que proporciona un procedimiento finito completo para verificarla cuando la entrada es finita.

## 2.29. Cierre del capítulo

Con `TLOG-CH02-M03` quedan satisfechas las obligaciones arquitectónicas del Capítulo 2:

$$
\text{valuaciones}
\longrightarrow
\text{evaluación}
\longrightarrow
\text{satisfacción}
\longrightarrow
\text{satisfacibilidad/validez}
\longrightarrow
\text{consecuencia/equivalencia}
\longrightarrow
\text{reducción finita y decisión}.
$$

No queda pendiente ninguna definición semántica requerida por la salida arquitectónica del capítulo. El estudio de derivaciones, reglas y teoremas pertenece al Capítulo 3; la comparación entre $\vdash$ y $\models$ pertenece al Capítulo 4.

$$
\boxed{\texttt{TLOG-CH02-0001 — CLOSED}}
$$

Próximo frente:

```text
TLOG-CH03-0001 — Cálculo proposicional
```

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 1](capitulo-01.md) · [Capítulo 3 →](capitulo-03.md)

