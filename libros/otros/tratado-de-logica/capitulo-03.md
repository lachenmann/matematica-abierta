---
title: Capítulo 3 — Cálculo proposicional
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
content-id: MA-BCH-0205
content-type: book-chapter
source-id: TLOG-CH03-0001
prerequisites:
- MA-BCH-0203
related:
- MA-BOK-0014
source-sha256: 2b00b8629226285ca58bb03bef612dbc03d51f83f21bc13578b44da1867bfbb3
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 2](capitulo-02.md) · [Capítulo 4 →](capitulo-04.md)

## 3.0. Función del capítulo

Los capítulos anteriores separaron y cerraron dos capas: la sintaxis de `CPL` y su semántica bivalente. Falta ahora fijar una noción **puramente sintáctica** de prueba formal.

La frontera del capítulo es:

$$
\text{fórmulas}
\longrightarrow
\text{axiomas y reglas}
\longrightarrow
\text{derivaciones}
\longrightarrow
\text{derivabilidad}.
$$

En particular,

$$
\Gamma\vdash\varphi
$$

no significa todavía

$$
\Gamma\models\varphi.
$$

La relación entre ambas se demostrará en el Capítulo 4 mediante corrección y completitud.

Este primer microtramo fija un cálculo de Hilbert para las cinco conectivas primitivas ya adoptadas por `CPL`, formaliza las derivaciones como secuencias finitas y establece sólo sus propiedades estructurales inmediatas.

### Fuentes efectivamente cotejadas

- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001), cap. 2 §2.4, pp. 109–112, usado como modelo de la noción de deducción finita y de la regla modus ponens.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010), cap. 1 §1.6, pp. 35–40, usado como modelo principal de cálculo de Hilbert, prueba como secuencia finita e inducción sobre pruebas.

Existe una divergencia deliberada. En Rautenberg §1.6, $\to$ se usa como conectiva definida a partir de $\neg,\land$. En `CPL`, por [TLOG-CNV-00003](capitulo-01.md#tlog-cnv-00003), $\to$ es **primitiva**. Por ello TLOG no importa literalmente su base axiomática: reconstruye un sistema clásico para la firma primitiva completa

$$
\{\neg,\land,\lor,\to,\leftrightarrow\}.
$$

## 3.1. Cálculo proposicional de referencia

### Convención 3.1.1 — El cálculo $\mathsf H_{\mathrm{CPL}}$ {#tlog-cnv-00006}

Denotamos por

$$
\mathsf H_{\mathrm{CPL}}
$$

el cálculo hilbertiano de referencia del tratado sobre el lenguaje objeto `CPL`.

Sus fórmulas son exactamente

$$
\mathrm{Fm}_{\mathrm{CPL}}.
$$

El cálculo tendrá:

1. una base finita de **esquemas axiomáticos**;
2. una sola regla primitiva de inferencia, **modus ponens**;
3. derivaciones finitas desde un conjunto arbitrario de premisas.

La elección de un cálculo de Hilbert no afirma que sea la única presentación posible de la lógica clásica. Su función es proporcionar una noción sintáctica estable, finitaria y apta para la aritmetización posterior de pruebas.

## 3.2. Esquemas axiomáticos

### Esquema axiomático 3.2.1 — Base de $\mathsf H_{\mathrm{CPL}}$ {#tlog-axm-00001}

Sean

$$
\alpha,\beta,\gamma\in\mathrm{Fm}_{\mathrm{CPL}}
$$

metavariables de fórmula. La clase $\operatorname{Ax}_{\mathsf H}$ de instancias axiomáticas se obtiene tomando **todas** las instancias de los siguientes esquemas:

### Núcleo implicativo-clásico

$$
\tag{H1}
\alpha\to(\beta\to\alpha),
$$

$$
\tag{H2}
(\alpha\to(\beta\to\gamma))
\to
((\alpha\to\beta)\to(\alpha\to\gamma)),
$$

$$
\tag{H3}
(\neg\beta\to\neg\alpha)\to(\alpha\to\beta).
$$

### Conjunción

$$
\tag{H4}
(\alpha\land\beta)\to\alpha,
$$

$$
\tag{H5}
(\alpha\land\beta)\to\beta,
$$

$$
\tag{H6}
\alpha\to(\beta\to(\alpha\land\beta)).
$$

### Disyunción

$$
\tag{H7}
\alpha\to(\alpha\lor\beta),
$$

$$
\tag{H8}
\beta\to(\alpha\lor\beta),
$$

$$
\tag{H9}
(\alpha\to\gamma)
\to
((\beta\to\gamma)\to((\alpha\lor\beta)\to\gamma)).
$$

### Bicondicional

$$
\tag{H10}
(\alpha\leftrightarrow\beta)\to(\alpha\to\beta),
$$

$$
\tag{H11}
(\alpha\leftrightarrow\beta)\to(\beta\to\alpha),
$$

$$
\tag{H12}
(\alpha\to\beta)
\to
((\beta\to\alpha)\to(\alpha\leftrightarrow\beta)).
$$

Cada línea anterior es un **esquema**, no una fórmula singular. Por ejemplo, `H1` autoriza una instancia para cada par ordenado de fórmulas $(\alpha,\beta)$.

::: {.callout-important}
## Firma primitiva

Ninguna de $\land,\lor,\to,\leftrightarrow$ se introduce aquí como abreviatura definicional. Son las conectivas primitivas ya fijadas en `CPL`. Los esquemas `H4`–`H12` controlan deductivamente las conectivas adicionales al núcleo $\neg,\to$.
:::

No se afirma todavía que estas instancias sean exactamente las fórmulas válidas derivables del cálculo. Eso pertenece a corrección y completitud.

## 3.3. Regla primitiva

### Regla 3.3.1 — Modus ponens {#tlog-rul-00001}

La única regla primitiva de inferencia de $\mathsf H_{\mathrm{CPL}}$ es

$$
\frac{\alpha\qquad \alpha\to\beta}{\beta}
\quad
(\mathrm{MP}),
$$

donde

$$
\alpha,\beta\in\mathrm{Fm}_{\mathrm{CPL}}.
$$

No hay condiciones laterales ni descarga de hipótesis. `MP` es una regla binaria sobre fórmulas del sistema objeto.

## 3.4. Derivaciones desde premisas

### Definición 3.4.1 — Derivación en $\mathsf H_{\mathrm{CPL}}$ {#tlog-def-00019}

Sea

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}.
$$

Una **derivación desde $\Gamma$** es una secuencia finita no vacía

$$
\Pi=(\varphi_0,\ldots,\varphi_n)
$$

de fórmulas de `CPL` tal que, para cada $k\le n$, ocurre al menos una de las siguientes alternativas:

1. $\varphi_k\in\Gamma$;
2. $\varphi_k\in\operatorname{Ax}_{\mathsf H}$;
3. existen $i,j<k$ y fórmulas $\alpha,\beta$ tales que
   $$
   \varphi_i=\alpha,
   \qquad
   \varphi_j=\alpha\to\beta,
   \qquad
   \varphi_k=\beta.
   $$

En el tercer caso decimos que la línea $k$ se obtiene por `MP` de las líneas $i,j$.

La **conclusión** de $\Pi$ es su última fórmula $\varphi_n$, y su **longitud** es $n+1$.

La definición es finitaria incluso cuando $\Gamma$ es infinito: una derivación concreta sólo contiene un número finito de líneas.

## 3.5. Derivabilidad y teoremas

### Definición 3.5.1 — Derivabilidad {#tlog-def-00020}

Para

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}},
\qquad
\varphi\in\mathrm{Fm}_{\mathrm{CPL}},
$$

escribimos

$$
\Gamma\vdash_{\mathsf H}\varphi
$$

si existe una derivación desde $\Gamma$ cuya conclusión es $\varphi$.

Si

$$
\varnothing\vdash_{\mathsf H}\varphi,
$$

escribimos

$$
\vdash_{\mathsf H}\varphi
$$

y decimos que $\varphi$ es un **teorema de $\mathsf H_{\mathrm{CPL}}$**.

La negación metalingüística

$$
\Gamma\nvdash_{\mathsf H}\varphi
$$

significa que no existe tal derivación.

::: {.callout-important}
## Separación de niveles

$$
\Gamma\vdash_{\mathsf H}\varphi
\neq
\Gamma\models_{\mathrm{CPL}}\varphi.
$$
La izquierda es existencia de una secuencia sintáctica finita del tipo definido en §3.4. La derecha cuantifica sobre valuaciones. Ninguna dirección entre ambas se presupone.
:::

## 3.6. Inducción sobre derivaciones

### Metateorema 3.6.1 — Principio de inducción sobre derivaciones {#tlog-mth-00007}

Fijemos $\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ y una propiedad metateórica $P$ de fórmulas. Supongamos:

1. $P(\gamma)$ para toda $\gamma\in\Gamma$;
2. $P(A)$ para toda $A\in\operatorname{Ax}_{\mathsf H}$;
3. para todas $\alpha,\beta$,
   $$
   P(\alpha)\land P(\alpha\to\beta)
   \Longrightarrow
   P(\beta).
   $$

Entonces

$$
\Gamma\vdash_{\mathsf H}\varphi
\Longrightarrow
P(\varphi)
$$

para toda $\varphi\in\mathrm{Fm}_{\mathrm{CPL}}$.

#### Demostración

Sea

$$
\Pi=(\varphi_0,\ldots,\varphi_n)
$$

una derivación desde $\Gamma$. Probamos por inducción ordinaria sobre $k\le n$ que $P(\varphi_k)$.

Si $\varphi_k\in\Gamma$, se aplica (1). Si $\varphi_k\in\operatorname{Ax}_{\mathsf H}$, se aplica (2). En el caso restante, existen $i,j<k$ con

$$
\varphi_j=\varphi_i\to\varphi_k.
$$

Por hipótesis inductiva,

$$
P(\varphi_i)
\quad\text{y}\quad
P(\varphi_i\to\varphi_k),
$$

y (3) da $P(\varphi_k)$.

En particular $P(\varphi_n)$. $\square$

La medida bien fundada usada es la posición de la línea dentro de una secuencia finita.

## 3.7. Propiedades estructurales inmediatas

### Proposición 3.7.1 — Premisa, MP, monotonía, finitariedad y composición {#tlog-pro-00003}

Para conjuntos de fórmulas $\Gamma,\Delta$ y fórmulas $\alpha,\beta,\varphi$:

1. **Premisa.**
   $$
   \varphi\in\Gamma
   \Longrightarrow
   \Gamma\vdash_{\mathsf H}\varphi.
   $$

2. **Instancia axiomática.** Si
   $$
   A\in\operatorname{Ax}_{\mathsf H},
   $$
   entonces
   $$
   \vdash_{\mathsf H}A
   \quad\text{y}\quad
   \Gamma\vdash_{\mathsf H}A.
   $$

3. **Cierre por MP.**
   $$
   \Gamma\vdash_{\mathsf H}\alpha,
   \qquad
   \Gamma\vdash_{\mathsf H}\alpha\to\beta
   \Longrightarrow
   \Gamma\vdash_{\mathsf H}\beta.
   $$

4. **Monotonía.**
   $$
   \Gamma\subseteq\Delta
   \quad\text{y}\quad
   \Gamma\vdash_{\mathsf H}\varphi
   \Longrightarrow
   \Delta\vdash_{\mathsf H}\varphi.
   $$

5. **Finitariedad.**
   $$
   \Gamma\vdash_{\mathsf H}\varphi
   \Longrightarrow
   \exists\Gamma_0\subseteq\Gamma
   \quad
   \bigl(
   \Gamma_0\text{ finito}
   \land
   \Gamma_0\vdash_{\mathsf H}\varphi
   \bigr).
   $$

6. **Composición de derivaciones.** Si
   $$
   \Delta\vdash_{\mathsf H}\varphi
   $$
   y
   $$
   \Gamma\vdash_{\mathsf H}\delta
   \quad
   \text{para toda }\delta\in\Delta,
   $$
   entonces
   $$
   \Gamma\vdash_{\mathsf H}\varphi.
   $$

#### Demostración

(1) y (2) son derivaciones de una sola línea.

(3) se obtiene concatenando derivaciones de $\alpha$ y $\alpha\to\beta$ y añadiendo $\beta$ por `MP`.

Para (4), toda línea de una derivación desde $\Gamma$ que sea premisa sigue siendo premisa desde $\Delta$; axiomas y aplicaciones de `MP` no cambian.

Para (5), una derivación es finita. Reunimos las fórmulas de $\Gamma$ que aparecen efectivamente como líneas-premisa. Ese conjunto $\Gamma_0$ es finito y la misma secuencia es una derivación desde $\Gamma_0$.

Para (6), una derivación concreta de $\varphi$ desde $\Delta$ usa sólo finitas premisas $\delta_1,\ldots,\delta_m\in\Delta$. Sustituimos cada aparición inicial de $\delta_r$ por una derivación de $\delta_r$ desde $\Gamma$, concatenamos las secuencias y conservamos las aplicaciones de `MP`. El resultado es una derivación finita de $\varphi$ desde $\Gamma$. $\square$

Todas estas propiedades son **sintácticas**. No usan valuaciones ni consecuencia semántica.

## 3.8. Ejemplo desarrollado — una derivación elemental

Sean

$$
\Gamma=\{p_1,p_2\}.
$$

La instancia de `H6`

$$
p_1\to(p_2\to(p_1\land p_2))
$$

permite la derivación:

| Línea | Fórmula | Justificación |
|---:|---|---|
| 1 | $p_1$ | premisa |
| 2 | $p_2$ | premisa |
| 3 | $p_1\to(p_2\to(p_1\land p_2))$ | `H6` |
| 4 | $p_2\to(p_1\land p_2)$ | `MP` 1,3 |
| 5 | $p_1\land p_2$ | `MP` 2,4 |

Por tanto

$$
\{p_1,p_2\}
\vdash_{\mathsf H}
p_1\land p_2.
$$

No se infiere aquí ninguna afirmación semántica sobre esta derivación.

## 3.11. Estado y próximo frente

El Capítulo 3 queda en

```text
PARTIAL-CLOSURE / NOT CLOSED
```

con siete nodos cerrados. Todavía no se han demostrado reglas derivadas sustantivas ni el teorema de deducción.

Próximo microtramo:

```text
TLOG-CH03-M02
Teorema de deducción y reglas derivadas básicas
```

## 3.12. Autoimplicación

### Lema 3.12.1 — Toda fórmula implica a sí misma {#tlog-lem-00004}

Para toda fórmula $\alpha\in\mathrm{Fm}_{\mathrm{CPL}}$,

$$
\vdash_{\mathsf H}\alpha\to\alpha.
$$

#### Demostración

Aplicamos únicamente `H1`, `H2` y `MP`.

1. Instancia de `H1`:
   $$
   \alpha\to((\alpha\to\alpha)\to\alpha).
   $$
2. Segunda instancia de `H1`:
   $$
   \alpha\to(\alpha\to\alpha).
   $$
3. Instancia de `H2`:
   $$
   \bigl(\alpha\to((\alpha\to\alpha)\to\alpha)\bigr)
   \to
   \bigl((\alpha\to(\alpha\to\alpha))\to(\alpha\to\alpha)\bigr).
   $$
4. Por `MP` sobre 1 y 3:
   $$
   (\alpha\to(\alpha\to\alpha))\to(\alpha\to\alpha).
   $$
5. Por `MP` sobre 2 y 4:
   $$
   \alpha\to\alpha.
   $$

Por tanto $\vdash_{\mathsf H}\alpha\to\alpha$. $\square$

::: {.callout-note}
## Función del lema

La autoimplicación no se toma como axioma adicional. Se deriva de la base ya fijada y será el caso no trivial de premisa descargada en el teorema de deducción.
:::

## 3.13. Teorema de deducción

### Metateorema 3.13.1 — Teorema de deducción de $\mathsf H_{\mathrm{CPL}}$ {#tlog-mth-00008}

Sean

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}},
\qquad
\alpha,\beta\in\mathrm{Fm}_{\mathrm{CPL}}.
$$

Usaremos la abreviación

$$
\Gamma,\alpha:=\Gamma\cup\{\alpha\}.
$$

Entonces

$$
\boxed{
\Gamma,\alpha\vdash_{\mathsf H}\beta
\iff
\Gamma\vdash_{\mathsf H}\alpha\to\beta
}.
$$

No hay condiciones laterales sobre variables: el lenguaje es proposicional y la única regla primitiva es `MP`.

#### Demostración

**Dirección $(\Rightarrow)$.** Supongamos

$$
\Gamma,\alpha\vdash_{\mathsf H}\beta.
$$

Aplicamos [TLOG-MTH-00007](#tlog-mth-00007) a una derivación desde $\Gamma,\alpha$ con la propiedad

$$
P(\delta)
\quad:\!\!\iff\quad
\Gamma\vdash_{\mathsf H}\alpha\to\delta.
$$

Debemos verificar los casos de generación de una derivación.

1. **Premisa de $\Gamma$.** Si $\delta\in\Gamma$, entonces
   $$
   \Gamma\vdash_{\mathsf H}\delta
   $$
   por [TLOG-PRO-00003](#tlog-pro-00003). La instancia de `H1`
   $$
   \delta\to(\alpha\to\delta)
   $$
   y `MP` dan
   $$
   \Gamma\vdash_{\mathsf H}\alpha\to\delta.
   $$

2. **Premisa descargada.** Si $\delta=\alpha$, [TLOG-LEM-00004](#tlog-lem-00004) da
   $$
   \vdash_{\mathsf H}\alpha\to\alpha,
   $$
   y por monotonía
   $$
   \Gamma\vdash_{\mathsf H}\alpha\to\alpha.
   $$

3. **Instancia axiomática.** Si $\delta\in\operatorname{Ax}_{\mathsf H}$, entonces
   $$
   \Gamma\vdash_{\mathsf H}\delta
   $$
   por [TLOG-PRO-00003](#tlog-pro-00003). Como en el primer caso, `H1` y `MP` producen
   $$
   \Gamma\vdash_{\mathsf H}\alpha\to\delta.
   $$

4. **Paso de `MP`.** Supongamos que una línea $\delta$ se obtiene de líneas anteriores
   $$
   \rho,
   \qquad
   \rho\to\delta.
   $$
   Por hipótesis inductiva,
   $$
   \Gamma\vdash_{\mathsf H}\alpha\to\rho,
   \qquad
   \Gamma\vdash_{\mathsf H}\alpha\to(\rho\to\delta).
   $$
   La instancia de `H2`
   $$
   (\alpha\to(\rho\to\delta))
   \to
   ((\alpha\to\rho)\to(\alpha\to\delta))
   $$
   seguida de dos aplicaciones de `MP` da
   $$
   \Gamma\vdash_{\mathsf H}\alpha\to\delta.
   $$

La inducción sobre la derivación alcanza su última línea $\beta$, y por tanto

$$
\Gamma\vdash_{\mathsf H}\alpha\to\beta.
$$

**Dirección $(\Leftarrow)$.** Supongamos

$$
\Gamma\vdash_{\mathsf H}\alpha\to\beta.
$$

Por monotonía,

$$
\Gamma,\alpha\vdash_{\mathsf H}\alpha\to\beta.
$$

Además, $\alpha\in\Gamma,\alpha$, de modo que

$$
\Gamma,\alpha\vdash_{\mathsf H}\alpha.
$$

Una aplicación de `MP` concluye

$$
\Gamma,\alpha\vdash_{\mathsf H}\beta.
$$

Quedan demostradas ambas direcciones. $\square$

::: {.callout-important}
## Naturaleza del resultado

El teorema de deducción transforma derivaciones en derivaciones. No afirma ni utiliza ninguna relación semántica. En particular, no depende de corrección ni de completitud.
:::

## 3.14. Reglas derivadas básicas

### Proposición 3.14.1 — Reglas derivadas para las conectivas primitivas {#tlog-pro-00004}

Sean $\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ y $\alpha,\beta,\gamma\in\mathrm{Fm}_{\mathrm{CPL}}$. Son admisibles las siguientes reglas derivadas.

1. **Introducción de conjunción**
   $$
   \frac{\Gamma\vdash_{\mathsf H}\alpha
   \qquad
   \Gamma\vdash_{\mathsf H}\beta}
   {\Gamma\vdash_{\mathsf H}\alpha\land\beta}.
   $$

2. **Eliminación de conjunción**
   $$
   \frac{\Gamma\vdash_{\mathsf H}\alpha\land\beta}
   {\Gamma\vdash_{\mathsf H}\alpha},
   \qquad
   \frac{\Gamma\vdash_{\mathsf H}\alpha\land\beta}
   {\Gamma\vdash_{\mathsf H}\beta}.
   $$

3. **Introducción de disyunción**
   $$
   \frac{\Gamma\vdash_{\mathsf H}\alpha}
   {\Gamma\vdash_{\mathsf H}\alpha\lor\beta},
   \qquad
   \frac{\Gamma\vdash_{\mathsf H}\beta}
   {\Gamma\vdash_{\mathsf H}\alpha\lor\beta}.
   $$

4. **Análisis por casos**
   $$
   \frac{
   \Gamma,\alpha\vdash_{\mathsf H}\gamma
   \qquad
   \Gamma,\beta\vdash_{\mathsf H}\gamma
   }
   {
   \Gamma,\alpha\lor\beta\vdash_{\mathsf H}\gamma
   }.
   $$

5. **Eliminación de bicondicional**
   $$
   \frac{\Gamma\vdash_{\mathsf H}\alpha\leftrightarrow\beta}
   {\Gamma\vdash_{\mathsf H}\alpha\to\beta},
   \qquad
   \frac{\Gamma\vdash_{\mathsf H}\alpha\leftrightarrow\beta}
   {\Gamma\vdash_{\mathsf H}\beta\to\alpha}.
   $$

6. **Introducción de bicondicional**
   $$
   \frac{
   \Gamma\vdash_{\mathsf H}\alpha\to\beta
   \qquad
   \Gamma\vdash_{\mathsf H}\beta\to\alpha
   }
   {
   \Gamma\vdash_{\mathsf H}\alpha\leftrightarrow\beta
   }.
   $$

7. **Silogismo hipotético**
   $$
   \frac{
   \Gamma\vdash_{\mathsf H}\alpha\to\beta
   \qquad
   \Gamma\vdash_{\mathsf H}\beta\to\gamma
   }
   {
   \Gamma\vdash_{\mathsf H}\alpha\to\gamma
   }.
   $$

#### Demostración

(1) es una instancia de `H6` seguida de dos aplicaciones de `MP`.

(2) se obtiene de `H4` y `H5` mediante `MP`.

(3) se obtiene de `H7` y `H8` mediante `MP`.

Para (4), el teorema de deducción transforma las dos premisas metateóricas en

$$
\Gamma\vdash_{\mathsf H}\alpha\to\gamma,
\qquad
\Gamma\vdash_{\mathsf H}\beta\to\gamma.
$$

Aplicando `H9` y `MP` dos veces obtenemos

$$
\Gamma\vdash_{\mathsf H}(\alpha\lor\beta)\to\gamma.
$$

La dirección inversa del teorema de deducción produce entonces

$$
\Gamma,\alpha\lor\beta\vdash_{\mathsf H}\gamma.
$$

(5) resulta de `H10` y `H11` por `MP`.

(6) resulta de `H12` por dos aplicaciones de `MP`.

Para (7), por la dirección inversa del teorema de deducción,

$$
\Gamma,\alpha\vdash_{\mathsf H}\beta.
$$

Por monotonía,

$$
\Gamma,\alpha\vdash_{\mathsf H}\beta\to\gamma,
$$

y `MP` da

$$
\Gamma,\alpha\vdash_{\mathsf H}\gamma.
$$

Aplicando ahora la dirección directa del teorema de deducción,

$$
\Gamma\vdash_{\mathsf H}\alpha\to\gamma.
$$

Todas las reglas son, por tanto, admisibles en $\mathsf H_{\mathrm{CPL}}$. $\square$

::: {.callout-note}
## Regla derivada

“Admisible” significa aquí que toda instancia cuyas premisas son derivables tiene conclusión derivable en el cálculo ya fijado. No se añade ninguna nueva regla primitiva a $\mathsf H_{\mathrm{CPL}}$.
:::

## 3.15. Internalización finita de premisas

### Corolario 3.15.1 — Descarga iterada de un contexto finito {#tlog-cor-00001}

Sean

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}},
\qquad
\alpha_1,\ldots,\alpha_n,\beta\in\mathrm{Fm}_{\mathrm{CPL}},
$$

con $n\ge 1$. Entonces

$$
\Gamma\cup\{\alpha_1,\ldots,\alpha_n\}
\vdash_{\mathsf H}\beta
$$

si y sólo si

$$
\Gamma
\vdash_{\mathsf H}
\alpha_1\to
\bigl(
\alpha_2\to
\cdots
(\alpha_n\to\beta)
\cdots
\bigr),
$$

donde la cadena de implicaciones se asocia a la derecha.

#### Demostración

Aplicamos [TLOG-MTH-00008](#tlog-mth-00008) sucesivamente, descargando una premisa por vez. La dirección recíproca se obtiene leyendo las equivalencias en sentido contrario y aplicando, en cada paso, la dirección $(\Leftarrow)$ del mismo teorema. $\square$

Para $n=0$ la afirmación se reduce a la identidad

$$
\Gamma\vdash_{\mathsf H}\beta
\iff
\Gamma\vdash_{\mathsf H}\beta.
$$

Este corolario será útil al comparar, en el capítulo siguiente, derivabilidad desde un conjunto finito de premisas con fórmulas condicionales; esa comparación requerirá allí los teoremas semánticos correspondientes.

## 3.16. Ejemplo desarrollado — conmutatividad de la conjunción como teorema

Trabajemos desde la única premisa

$$
\alpha\land\beta.
$$

Por eliminación derivada de conjunción obtenemos

$$
\alpha
\qquad\text{y}\qquad
\beta.
$$

Por introducción derivada de conjunción,

$$
\beta\land\alpha.
$$

Así,

$$
\alpha\land\beta
\vdash_{\mathsf H}
\beta\land\alpha.
$$

El teorema de deducción descarga la premisa y produce

$$
\boxed{
\vdash_{\mathsf H}
(\alpha\land\beta)\to(\beta\land\alpha)
}.
$$

Este resultado es una afirmación de **teoremicidad sintáctica**. Su validez semántica no se utiliza aquí.

## 3.19. Cierre del capítulo

Con `TLOG-CH03-M02` quedan satisfechas las obligaciones arquitectónicas del Capítulo 3:

$$
\text{axiomas y regla primitiva}
\longrightarrow
\text{derivaciones}
\longrightarrow
\text{derivabilidad}
\longrightarrow
\text{inducción sobre pruebas}
\longrightarrow
\text{teorema de deducción y reglas derivadas}.
$$

No se ha usado consecuencia semántica para cerrar ningún resultado deductivo. Corrección y completitud continúan diferidas al Capítulo 4.

$$
\boxed{\texttt{TLOG-CH03-0001 — CLOSED}}
$$

Próximo frente:

```text
TLOG-CH04-0001 — Corrección y completitud proposicional
```

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 2](capitulo-02.md) · [Capítulo 4 →](capitulo-04.md)

