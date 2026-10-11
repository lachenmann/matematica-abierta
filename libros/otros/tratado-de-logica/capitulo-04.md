---
title: Capítulo 4 — Corrección y completitud proposicional
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
content-id: MA-BCH-0206
content-type: book-chapter
source-id: TLOG-CH04-0001
prerequisites:
- MA-BCH-0203
- MA-BCH-0204
- MA-BCH-0205
related:
- MA-BOK-0014
source-sha256: 70875bba4cba9b7313d0c29b6e4a066242593654a4a90b57594f07c2644ddaa0
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 3](capitulo-03.md) · [Capítulo 5 →](capitulo-05.md)

## 4.0. Función del capítulo

Los capítulos 2 y 3 construyeron, por separado, las dos relaciones que ahora deben compararse:

$$
\Gamma\models_{\mathrm{CPL}}\varphi
\qquad\text{y}\qquad
\Gamma\vdash_{\mathsf H}\varphi.
$$

Hasta este punto no existe ninguna identificación entre ellas. El presente capítulo debe establecer dos metateoremas distintos:

$$
\text{corrección:}\quad
\Gamma\vdash_{\mathsf H}\varphi
\Longrightarrow
\Gamma\models_{\mathrm{CPL}}\varphi,
$$

$$
\text{completitud:}\quad
\Gamma\models_{\mathrm{CPL}}\varphi
\Longrightarrow
\Gamma\vdash_{\mathsf H}\varphi.
$$

Este primer microtramo cierra exclusivamente la **corrección**. La completitud permanece abierta.

### Fuentes efectivamente cotejadas

- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010), cap. 1 §1.6, pp. 36–37: modelo proposicional directo de la prueba de corrección por inducción sobre pruebas.
- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001), cap. 2 §2.5, pp. 131–135: modelo estructural de la estrategia «axiomas válidos + preservación por modus ponens + inducción sobre deducciones».

El sistema de Enderton en ese localizador es de primer orden y **no** se importa como cálculo de este capítulo. Sólo controla la arquitectura metateórica de la prueba. La verificación de `H1`–`H12` se reconstruye íntegramente para `HCPL`.

## 4.1. Validez de la base axiomática

### Lema 4.1.1 — Toda instancia axiomática de $\mathsf H_{\mathrm{CPL}}$ es válida {#tlog-lem-00005}

Para toda fórmula

$$
A\in\operatorname{Ax}_{\mathsf H},
$$

se cumple

$$
\models_{\mathrm{CPL}}A.
$$

#### Demostración

Sea $v\in\mathrm{Val}_{\mathrm{CPL}}$ arbitraria. Para fórmulas $\alpha,\beta,\gamma$ escribamos

$$
a:=\widehat v(\alpha),\qquad
b:=\widehat v(\beta),\qquad
c:=\widehat v(\gamma).
$$

Por [TLOG-MTH-00004](capitulo-02.md#tlog-mth-00004), el valor de cada instancia de `H1`–`H12` se obtiene aplicando las funciones de verdad de [TLOG-CNV-00005](capitulo-02.md#tlog-cnv-00005). Mostramos que ninguna instancia puede tomar valor $0$.

1. **`H1`** $\alpha\to(\beta\to\alpha)$. Para que fuese falsa necesitaríamos $a=1$ y $b\to a=0$; lo segundo exige $a=0$. Contradicción.
2. **`H2`**
   $$
   (\alpha\to(\beta\to\gamma))
   \to
   ((\alpha\to\beta)\to(\alpha\to\gamma)).
   $$
   Si fuese falsa, el consecuente exterior sería falso. Entonces $\alpha\to\beta=1$ y $\alpha\to\gamma=0$, de donde $a=1,c=0$ y necesariamente $b=1$. Pero así $\beta\to\gamma=0$, por lo que $\alpha\to(\beta\to\gamma)=0$, contradiciendo que el antecedente exterior deba valer $1$.
3. **`H3`** $(\neg\beta\to\neg\alpha)\to(\alpha\to\beta)$. Si fuese falsa, $a=1,b=0$; entonces $\neg b=1$ y $\neg a=0$, de modo que $\neg\beta\to\neg\alpha=0$. Contradicción.
4. **`H4`** y **`H5`**: si $a\land b=1$, entonces $a=b=1$, así que ambas proyecciones son verdaderas.
5. **`H6`** $\alpha\to(\beta\to(\alpha\land\beta))$. Si fuese falsa, tendríamos $a=1$, $b=1$ y $a\land b=0$, imposible.
6. **`H7`** y **`H8`**: si el antecedente correspondiente vale $1$, entonces $a\lor b=1$.
7. **`H9`**
   $$
   (\alpha\to\gamma)
   \to
   ((\beta\to\gamma)\to((\alpha\lor\beta)\to\gamma)).
   $$
   Si fuese falsa, $\alpha\to\gamma=1$, $\beta\to\gamma=1$ y $(\alpha\lor\beta)\to\gamma=0$. La última igualdad exige $c=0$ y $a\lor b=1$; con $c=0$, las dos primeras implicaciones fuerzan $a=b=0$, contradicción.
8. **`H10`** y **`H11`**: si $a\leftrightarrow b=1$, entonces $a=b$, y por tanto valen tanto $a\to b$ como $b\to a$.
9. **`H12`**: si $a\to b=1$ y $b\to a=1$, entonces en semántica bivalente $a=b$; por tanto $a\leftrightarrow b=1$.

En todos los casos el valor es $1$. Como $v$ era arbitraria, toda instancia axiomática es válida por [TLOG-DEF-00014](capitulo-02.md#tlog-def-00014). $\square$

::: {.callout-important}
## Alcance

Esta prueba verifica la **validez semántica** de los axiomas ya elegidos. No demuestra que toda fórmula válida sea axioma ni que toda fórmula válida sea derivable.
:::

## 4.2. Preservación semántica de modus ponens

### Lema 4.2.1 — `MP` preserva satisfacción {#tlog-lem-00006}

Sean $v\in\mathrm{Val}_{\mathrm{CPL}}$ y $\alpha,\beta\in\mathrm{Fm}_{\mathrm{CPL}}$. Si

$$
v\models\alpha
\qquad\text{y}\qquad
v\models\alpha\to\beta,
$$

entonces

$$
v\models\beta.
$$

#### Demostración

Por [TLOG-DEF-00011](capitulo-02.md#tlog-def-00011), la primera hipótesis da

$$
\widehat v(\alpha)=1.
$$

Por [TLOG-MTH-00004](capitulo-02.md#tlog-mth-00004) y la tabla de [TLOG-CNV-00005](capitulo-02.md#tlog-cnv-00005),

$$
\widehat v(\alpha\to\beta)
=
f_{\to}(\widehat v(\alpha),\widehat v(\beta))
=1.
$$

Como $f_{\to}(1,0)=0$, necesariamente

$$
\widehat v(\beta)=1.
$$

Por tanto $v\models\beta$. $\square$

La forma semántica del lema coincide exactamente con el patrón de la única regla primitiva [TLOG-RUL-00001](capitulo-03.md#tlog-rul-00001).

## 4.3. Teorema de corrección proposicional

### Metateorema 4.3.1 — Corrección de $\mathsf H_{\mathrm{CPL}}$ {#tlog-mth-00009}

Para todo conjunto de premisas

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}
$$

y toda fórmula $\varphi$,

$$
\boxed{
\Gamma\vdash_{\mathsf H}\varphi
\Longrightarrow
\Gamma\models_{\mathrm{CPL}}\varphi
}.
$$

#### Demostración

Supongamos

$$
\Gamma\vdash_{\mathsf H}\varphi.
$$

Para probar $\Gamma\models\varphi$, sea

$$
v\in\mathrm{Val}_{\mathrm{CPL}}
$$

una valuación arbitraria tal que

$$
v\models\Gamma.
$$

Aplicamos el principio de inducción sobre derivaciones [TLOG-MTH-00007](capitulo-03.md#tlog-mth-00007) con la propiedad

$$
P(\delta)
\quad:\!\!\iff\quad
v\models\delta.
$$

Debemos verificar sus tres casos.

1. **Premisa.** Si $\delta\in\Gamma$, entonces $v\models\delta$ por [TLOG-DEF-00012](capitulo-02.md#tlog-def-00012) y la hipótesis $v\models\Gamma$.
2. **Instancia axiomática.** Si $\delta\in\operatorname{Ax}_{\mathsf H}$, entonces [TLOG-LEM-00005](#tlog-lem-00005) da $\models\delta$; en particular $v\models\delta$.
3. **Paso de `MP`.** Si $\delta$ se obtiene a partir de $\rho$ y $\rho\to\delta$, las hipótesis inductivas dan
   $$
   v\models\rho,
   \qquad
   v\models\rho\to\delta.
   $$
   [TLOG-LEM-00006](#tlog-lem-00006) concluye $v\models\delta$.

Por inducción, la última línea de toda derivación desde $\Gamma$ es satisfecha por $v$; en particular,

$$
v\models\varphi.
$$

Como $v$ era un modelo arbitrario de $\Gamma$, [TLOG-DEF-00015](capitulo-02.md#tlog-def-00015) concluye

$$
\Gamma\models_{\mathrm{CPL}}\varphi.
$$

$\square$

::: {.callout-important}
## Dirección demostrada

El resultado establece solamente
$$
\vdash_{\mathsf H}\ \Longrightarrow\ \models_{\mathrm{CPL}}.
$$
La flecha inversa es el teorema de completitud y todavía no está disponible.
:::

## 4.4. Consecuencia para teoremas sin premisas

### Corolario 4.4.1 — Todo teorema de $\mathsf H_{\mathrm{CPL}}$ es válido {#tlog-cor-00002}

Para toda fórmula $\varphi$,

$$
\vdash_{\mathsf H}\varphi
\Longrightarrow
\models_{\mathrm{CPL}}\varphi.
$$

Equivalentemente, por contraposición metateórica clásica,

$$
\not\models_{\mathrm{CPL}}\varphi
\Longrightarrow
\nvdash_{\mathsf H}\varphi.
$$

#### Demostración

Si $\vdash_{\mathsf H}\varphi$, entonces

$$
\varnothing\vdash_{\mathsf H}\varphi.
$$

[TLOG-MTH-00009](#tlog-mth-00009) da

$$
\varnothing\models_{\mathrm{CPL}}\varphi.
$$

Por [TLOG-PRO-00001](capitulo-02.md#tlog-pro-00001), esto equivale a $\models_{\mathrm{CPL}}\varphi$. La forma contrapositiva se obtiene en la metateoría clásica. $\square$

Este corolario permite refutar teoremicidad mediante un solo contraejemplo semántico, pero todavía no permite demostrar teoremicidad a partir de validez.

## 4.5. Ejemplo desarrollado — un contramodelo impide teoremicidad

La variable proposicional $p_1$ no es válida. En efecto, existe una valuación $v$ con

$$
v(p_1)=0.
$$

Entonces

$$
v\not\models p_1,
$$

y por tanto

$$
\not\models p_1.
$$

Aplicando [TLOG-COR-00002](#tlog-cor-00002), concluimos

$$
\nvdash_{\mathsf H}p_1.
$$

La inferencia es legítima precisamente porque la corrección ya está demostrada. El argumento inverso —de validez a teoremicidad— seguirá prohibido hasta cerrar la completitud.

## 4.8. Estado y próximo frente

El Capítulo 4 queda en

```text
PARTIAL-CLOSURE / NOT CLOSED
```

con cuatro nodos cerrados. La dirección

$$
\Gamma\vdash_{\mathsf H}\varphi
\Longrightarrow
\Gamma\models_{\mathrm{CPL}}\varphi
$$

está cerrada; falta la dirección inversa.

Próximo microtramo:

```text
TLOG-CH04-M02
Completitud proposicional y cierre de la Parte I
```

## 4.9. Consistencia deductiva

### Definición 4.9.1 — Consistencia y consistencia maximal en $\mathsf H_{\mathrm{CPL}}$ {#tlog-def-00021}

Fijamos la fórmula de contradicción

$$
\bot_{\mathrm{CPL}}
:=
p_1\land\neg p_1.
$$

Para $\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}$:

1. $\Gamma$ es **$\mathsf H$-inconsistente** si
   $$
   \Gamma\vdash_{\mathsf H}\bot_{\mathrm{CPL}};
   $$
2. $\Gamma$ es **$\mathsf H$-consistente** si
   $$
   \Gamma\nvdash_{\mathsf H}\bot_{\mathrm{CPL}};
   $$
3. $\Gamma$ es **maximalmente $\mathsf H$-consistente** si es consistente y todo
   $$
   \Delta\supsetneq\Gamma
   $$
   es inconsistente.

La fórmula $\bot_{\mathrm{CPL}}$ no añade un símbolo nuevo al lenguaje objeto. Es una abreviación metateórica de una fórmula concreta de `CPL`.

::: {.callout-important}
## Frontera

Consistencia deductiva y satisfacibilidad no se identifican por definición. Su equivalencia será una consecuencia de corrección + existencia de modelos.
:::

## 4.10. Núcleo clásico derivado de $\mathsf H_{\mathrm{CPL}}$

### Lema 4.10.1 — Explosión, doble negación y reductio interno {#tlog-lem-00007}

Para fórmulas $\alpha,\beta$ quedan disponibles las siguientes consecuencias sintácticas.

### (a) Explosión

Si

$$
\Gamma\vdash_{\mathsf H}\alpha,
\qquad
\Gamma\vdash_{\mathsf H}\neg\alpha,
$$

entonces, para toda $\beta$,

$$
\Gamma\vdash_{\mathsf H}\beta.
$$

En efecto, de `H1` obtenemos

$$
\neg\alpha\to(\neg\beta\to\neg\alpha),
$$

y por `MP`, a partir de $\neg\alpha$,

$$
\neg\beta\to\neg\alpha.
$$

La instancia de `H3`

$$
(\neg\beta\to\neg\alpha)\to(\alpha\to\beta)
$$

da $\alpha\to\beta$, y una última aplicación de `MP` con $\alpha$ produce $\beta$.

Por el teorema de deducción también queda demostrado

$$
\vdash_{\mathsf H}
\neg\alpha\to(\alpha\to\beta).
\tag{E}
$$

### (b) Lema de evaluación implicativa

A partir de las premisas $\alpha$ y $\alpha\to\beta$, `MP` da $\beta$. Descargando sucesivamente por [TLOG-MTH-00008](capitulo-03.md#tlog-mth-00008),

$$
\vdash_{\mathsf H}
\alpha\to((\alpha\to\beta)\to\beta).
\tag{L}
$$

### (c) Doble negación

Se tiene

$$
\vdash_{\mathsf H}\neg\neg\alpha\to\alpha
\tag{DN-}
$$

y

$$
\vdash_{\mathsf H}\alpha\to\neg\neg\alpha.
\tag{DN+}
$$

Para `DN-`, elija una instancia cualquiera

$$
\theta:=\rho\to(\sigma\to\rho)
$$

de `H1`; así $\vdash\theta$. Dos instancias de `H3` dan

$$
(\neg\neg\theta\to\neg\neg\alpha)
\to
(\neg\alpha\to\neg\theta),
$$

$$
(\neg\alpha\to\neg\theta)
\to
(\theta\to\alpha).
$$

Por silogismo hipotético derivado,

$$
(\neg\neg\theta\to\neg\neg\alpha)
\to
(\theta\to\alpha).
$$

`H1` da

$$
\neg\neg\alpha\to
(\neg\neg\theta\to\neg\neg\alpha),
$$

por lo que

$$
\neg\neg\alpha\to(\theta\to\alpha).
$$

La instancia de (L)

$$
\theta\to((\theta\to\alpha)\to\alpha)
$$

y $\vdash\theta$ producen

$$
(\theta\to\alpha)\to\alpha.
$$

Componiendo obtenemos `DN-`. Para `DN+`, aplicamos `DN-` a $\neg\alpha$:

$$
\vdash\neg\neg\neg\alpha\to\neg\alpha,
$$

y después la instancia de `H3`

$$
(\neg\neg\neg\alpha\to\neg\alpha)
\to
(\alpha\to\neg\neg\alpha).
$$

### (d) Consequentia mirabilis

Se tiene

$$
\vdash_{\mathsf H}
(\neg\alpha\to\alpha)\to\alpha.
\tag{CM}
$$

Sea

$$
q:=(\neg\alpha\to\alpha).
$$

Bajo las hipótesis $q$ y $\neg\alpha$, la primera da $\alpha$ por `MP`. La fórmula de explosión (E), con $\beta:=\neg q$, da

$$
\neg\alpha\to(\alpha\to\neg q),
$$

de modo que las mismas hipótesis permiten derivar $\neg q$. Descargando primero $\neg\alpha$ y después $q$ mediante [TLOG-MTH-00008](capitulo-03.md#tlog-mth-00008), obtenemos

$$
\vdash_{\mathsf H}
q\to(\neg\alpha\to\neg q).
\tag{1}
$$

Por otra parte, `H3` con $q$ en el lugar de $\alpha$ y $\alpha$ en el lugar de $\beta$ es

$$
(\neg\alpha\to\neg q)
\to
(q\to\alpha).
\tag{2}
$$

Ahora trabajemos bajo la única hipótesis $q$. De (1) obtenemos $\neg\alpha\to\neg q$; de (2), $q\to\alpha$; y de nuevo con la propia hipótesis $q$, `MP` produce $\alpha$. Una última aplicación del teorema de deducción descarga $q$:

$$
\vdash_{\mathsf H}q\to\alpha,
$$

que, por la definición de $q$, es exactamente (CM).

### (e) Auto-refutación

Finalmente,

$$
\vdash_{\mathsf H}
(\alpha\to\neg\alpha)\to\neg\alpha.
\tag{AR}
$$

Bajo la hipótesis $\alpha\to\neg\alpha$, `DN-` y silogismo hipotético dan

$$
\neg\neg\alpha\to\neg\alpha.
$$

Aplicamos (CM) a la fórmula $\neg\alpha$:

$$
(\neg\neg\alpha\to\neg\alpha)\to\neg\alpha,
$$

y descargamos la hipótesis.

Todos estos resultados son teoremas o reglas derivadas de `HCPL`; no se ha usado completitud semántica.

## 4.11. Pruebas de consistencia

### Lema 4.11.1 — Tests $C^+$, $C^-$ y trivialidad {#tlog-lem-00008}

Para todo $\Gamma$ y toda fórmula $\alpha$:

$$
\boxed{
\Gamma\vdash_{\mathsf H}\alpha
\iff
\Gamma,\neg\alpha
\vdash_{\mathsf H}\bot_{\mathrm{CPL}}
}
\tag{C+}
$$

y

$$
\boxed{
\Gamma\vdash_{\mathsf H}\neg\alpha
\iff
\Gamma,\alpha
\vdash_{\mathsf H}\bot_{\mathrm{CPL}}
}.
\tag{C-}
$$

Además,

$$
\Gamma\vdash_{\mathsf H}\bot_{\mathrm{CPL}}
\iff
(\forall\psi\in\mathrm{Fm}_{\mathrm{CPL}})
\;\Gamma\vdash_{\mathsf H}\psi.
\tag{T}
$$

#### Demostración

Para (T), si $\Gamma\vdash\bot_{\mathrm{CPL}}$, las eliminaciones derivadas de $\land$ dan

$$
\Gamma\vdash p_1,
\qquad
\Gamma\vdash\neg p_1,
$$

y la explosión de [TLOG-LEM-00007](#tlog-lem-00007) da cualquier $\psi$. La recíproca es inmediata tomando $\psi=\bot_{\mathrm{CPL}}$.

Para `C+`, la dirección $(\Rightarrow)$ combina $\alpha$, la premisa $\neg\alpha$ y explosión. Para $(\Leftarrow)$, (T) da

$$
\Gamma,\neg\alpha\vdash\alpha.
$$

El teorema de deducción produce

$$
\Gamma\vdash\neg\alpha\to\alpha,
$$

y (CM) concluye $\Gamma\vdash\alpha$.

Para `C-`, la dirección $(\Rightarrow)$ es análoga. Para la recíproca, de

$$
\Gamma,\alpha\vdash\bot_{\mathrm{CPL}}
$$

obtenemos por (T)

$$
\Gamma,\alpha\vdash\neg\alpha,
$$

luego

$$
\Gamma\vdash\alpha\to\neg\alpha.
$$

La fórmula (AR) de [TLOG-LEM-00007](#tlog-lem-00007) da $\Gamma\vdash\neg\alpha$. $\square$

Por tanto:

$$
\Gamma\nvdash\alpha
\iff
\Gamma\cup\{\neg\alpha\}
\text{ es consistente}.
\tag{C+ contraposición}
$$

Esta equivalencia será el puente exacto hacia el contra-modelo de la prueba de completitud.

## 4.12. Extensión maximal sin elección

### Metateorema 4.12.1 — Lema de Lindenbaum enumerable para `CPL` {#tlog-mth-00010}

Todo conjunto $\mathsf H$-consistente

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}
$$

está contenido en un conjunto maximalmente $\mathsf H$-consistente.

#### Demostración

El alfabeto de `CPL` es explícitamente numerable: las variables son $p_1,p_2,\ldots$ y los restantes símbolos forman un conjunto finito. Por tanto las expresiones finitas admiten una enumeración explícita mediante longitud y una función de emparejamiento iterada sobre los índices de sus símbolos; en particular existe una enumeración

$$
\varphi_0,\varphi_1,\ldots
$$

de $\mathrm{Fm}_{\mathrm{CPL}}$. No se introduce aquí una codificación objeto ni un número de Gödel: sólo se usa numerabilidad metateórica.

Definimos recursivamente

$$
\Gamma_0:=\Gamma,
$$

y

$$
\Gamma_{n+1}:=
\begin{cases}
\Gamma_n\cup\{\varphi_n\},
&\text{si }\Gamma_n\cup\{\varphi_n\}\text{ es consistente},\\[2mm]
\Gamma_n,
&\text{en otro caso}.
\end{cases}
$$

Cada $\Gamma_n$ es consistente. Sea

$$
T:=\bigcup_{n<\omega}\Gamma_n.
$$

Si $T$ fuese inconsistente, entonces

$$
T\vdash\bot_{\mathrm{CPL}}.
$$

Por la finitariedad de [TLOG-PRO-00003](capitulo-03.md#tlog-pro-00003), existiría un conjunto finito

$$
T_0\subseteq T
$$

con

$$
T_0\vdash\bot_{\mathrm{CPL}}.
$$

Como la cadena $(\Gamma_n)$ es creciente, todo subconjunto finito de su unión está contenido en alguna $\Gamma_N$. Por monotonía,

$$
\Gamma_N\vdash\bot_{\mathrm{CPL}},
$$

contradicción. Luego $T$ es consistente.

Para la maximalidad, sea $\psi\notin T$. Tome $n$ con $\varphi_n=\psi$. Como $\psi$ no fue incorporada, $\Gamma_n\cup\{\psi\}$ era inconsistente. Por monotonía también

$$
T\cup\{\psi\}
$$

es inconsistente. Si $\Delta\supsetneq T$, elija $\psi\in\Delta\setminus T$; entonces $T\cup\{\psi\}\subseteq\Delta$, y la monotonía vuelve inconsistente a $\Delta$. Por tanto $T$ es maximalmente consistente. $\square$

::: {.callout-important}
## Fundamento

La prueba usa recursión sobre $\omega$ y finitariedad de las derivaciones. No usa el lema de Zorn ni introduce una hipótesis global de elección en $\mathsf M_{\mathrm{ext}}$.
:::

## 4.13. Valuación canónica

### Metateorema 4.13.1 — Lema de verdad para un conjunto maximalmente consistente {#tlog-mth-00011}

Sea $T\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ maximalmente $\mathsf H$-consistente. Entonces $T$ es deductivamente cerrado:

$$
T\vdash_{\mathsf H}\alpha
\Longrightarrow
\alpha\in T.
\tag{DC}
$$

En efecto, si $\alpha\notin T$, por maximalidad $T,\alpha$ es inconsistente. Pero una derivación de $\bot_{\mathrm{CPL}}$ desde $T,\alpha$, junto con $T\vdash\alpha$, se recompone mediante [TLOG-PRO-00003](capitulo-03.md#tlog-pro-00003) en una derivación de $\bot_{\mathrm{CPL}}$ desde $T$, contradicción.

De `C-`, maximalidad y (DC) se obtiene

$$
\neg\alpha\in T
\iff
\alpha\notin T.
\tag{N}
$$

Las reglas derivadas y los esquemas de `HCPL` dan además:

$$
\alpha\land\beta\in T
\iff
\alpha\in T\text{ y }\beta\in T,
\tag{A}
$$

$$
\alpha\lor\beta\in T
\iff
\alpha\in T\text{ o }\beta\in T,
\tag{O}
$$

$$
\alpha\to\beta\in T
\iff
\alpha\notin T\text{ o }\beta\in T,
\tag{I}
$$

$$
\alpha\leftrightarrow\beta\in T
\iff
(\alpha\in T\iff\beta\in T).
\tag{B}
$$

Para (A) se usan las reglas derivadas de introducción/eliminación de conjunción. Para (O), una dirección viene de las introducciones derivadas de disyunción de [TLOG-PRO-00004](capitulo-03.md#tlog-pro-00004). Si $\alpha\lor\beta\in T$ pero ninguna disyunta pertenece a $T$, (N) da $\neg\alpha,\neg\beta\in T$. Por `C-`, $T,\alpha$ y $T,\beta$ son inconsistentes; por la trivialidad de [TLOG-LEM-00008](#tlog-lem-00008), ambos contextos derivan $\bot_{\mathrm{CPL}}$. El análisis por casos de [TLOG-PRO-00004](capitulo-03.md#tlog-pro-00004) produce $T,\alpha\lor\beta\vdash\bot_{\mathrm{CPL}}$, es decir $T\vdash\bot_{\mathrm{CPL}}$, contradicción.

Para (I), si $\alpha\to\beta\in T$ y $\alpha\in T$, `MP` y (DC) dan $\beta\in T$. Recíprocamente, si $\beta\in T$, entonces $T,\alpha\vdash\beta$ por premisa y monotonía, y [TLOG-MTH-00008](capitulo-03.md#tlog-mth-00008) da $T\vdash\alpha\to\beta$. Si $\alpha\notin T$, (N) da $\neg\alpha\in T$; `C-` hace inconsistente a $T,\alpha$, de modo que por trivialidad $T,\alpha\vdash\beta$; el teorema de deducción vuelve a dar $T\vdash\alpha\to\beta$. En ambos casos (DC) concluye $\alpha\to\beta\in T$.

Para (B), las reglas derivadas de eliminación de bicondicional de [TLOG-PRO-00004](capitulo-03.md#tlog-pro-00004) dan la dirección necesaria. Si $\alpha$ y $\beta$ tienen el mismo estado de pertenencia, (I) da ambas implicaciones y la introducción derivada de bicondicional de [TLOG-PRO-00004](capitulo-03.md#tlog-pro-00004) produce $\alpha\leftrightarrow\beta$.

Definimos ahora la **valuación canónica**

$$
v_T:\mathrm{PV}\to\mathbf 2
$$

por

$$
v_T(p_n)=1
\iff
p_n\in T.
$$

Entonces, para toda fórmula $\varphi$,

$$
\boxed{
 v_T\models_{\mathrm{CPL}}\varphi
 \iff
 \varphi\in T
}.
\tag{Truth}
$$

#### Demostración

Por inducción estructural [TLOG-MTH-00001](capitulo-01.md#tlog-mth-00001). El caso atómico es la definición de $v_T$. Los cinco pasos inductivos son exactamente (N), (A), (O), (I) y (B), cotejados con las cinco funciones de verdad que gobiernan la extensión $\widehat v_T$ por [TLOG-MTH-00004](capitulo-02.md#tlog-mth-00004). $\square$

En particular,

$$
v_T\models T.
$$

## 4.14. Existencia de modelo

### Metateorema 4.14.1 — Todo conjunto consistente de fórmulas proposicionales es satisfacible {#tlog-mth-00012}

Si

$$
\Gamma\nvdash_{\mathsf H}\bot_{\mathrm{CPL}},
$$

entonces existe

$$
v\in\mathrm{Val}_{\mathrm{CPL}}
$$

tal que

$$
v\models_{\mathrm{CPL}}\Gamma.
$$

#### Demostración

Por [TLOG-MTH-00010](#tlog-mth-00010), extendemos $\Gamma$ a un conjunto maximalmente consistente $T\supseteq\Gamma$. Por [TLOG-MTH-00011](#tlog-mth-00011), su valuación canónica satisface $T$. Luego también satisface $\Gamma$. $\square$

## 4.15. Completitud fuerte

### Metateorema 4.15.1 — Completitud de $\mathsf H_{\mathrm{CPL}}$ respecto de `CPL` {#tlog-mth-00013}

Para todo conjunto —finito o infinito— de premisas

$$
\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}
$$

y toda fórmula $\varphi$,

$$
\boxed{
\Gamma\models_{\mathrm{CPL}}\varphi
\Longrightarrow
\Gamma\vdash_{\mathsf H}\varphi
}.
$$

#### Demostración

Argumentamos por contraposición. Supongamos

$$
\Gamma\nvdash_{\mathsf H}\varphi.
$$

Por `C+` de [TLOG-LEM-00008](#tlog-lem-00008),

$$
\Gamma\cup\{\neg\varphi\}
$$

es consistente. [TLOG-MTH-00012](#tlog-mth-00012) proporciona una valuación $v$ que satisface ese conjunto. Por tanto

$$
v\models\Gamma
\qquad\text{y}\qquad
v\models\neg\varphi,
$$

de modo que

$$
v\not\models\varphi.
$$

Luego

$$
\Gamma\not\models\varphi.
$$

La contraposición metateórica concluye la tesis. $\square$

::: {.callout-important}
## Fuerza del resultado

No se ha supuesto que $\Gamma$ sea finito. La finitud entra únicamente en la naturaleza de cada derivación concreta y en la construcción enumerable de Lindenbaum.
:::

## 4.16. Adecuación, finitariedad semántica y compacidad

### Corolario 4.16.1 — Coincidencia extensional de consecuencia y compacidad proposicional {#tlog-cor-00003}

Para todo $\Gamma\subseteq\mathrm{Fm}_{\mathrm{CPL}}$ y toda $\varphi$:

1. **Adecuación.**
   $$
   \boxed{
   \Gamma\vdash_{\mathsf H}\varphi
   \iff
   \Gamma\models_{\mathrm{CPL}}\varphi
   }.
   $$

2. **Consistencia = satisfacibilidad.**
   $$
   \Gamma\text{ es }\mathsf H\text{-consistente}
   \iff
   \Gamma\text{ es satisfacible}.
   $$

3. **Finitariedad semántica.** Si
   $$
   \Gamma\models\varphi,
   $$
   existe un subconjunto finito $\Gamma_0\subseteq\Gamma$ con
   $$
   \Gamma_0\models\varphi.
   $$

4. **Compacidad proposicional.**
   $$
   \Gamma\text{ es satisfacible}
   \iff
   \text{todo subconjunto finito de }\Gamma\text{ es satisfacible}.
   $$

#### Demostración

(1) combina corrección [TLOG-MTH-00009](#tlog-mth-00009) y completitud [TLOG-MTH-00013](#tlog-mth-00013).

Para (2), la dirección consistencia $\Rightarrow$ satisfacibilidad es [TLOG-MTH-00012](#tlog-mth-00012). Si $\Gamma$ fuese satisfacible e inconsistente, entonces $\Gamma\vdash\bot_{\mathrm{CPL}}$; por corrección, todo modelo de $\Gamma$ satisfaría $p_1\land\neg p_1$, imposible bajo la semántica bivalente.

Para (3), completitud da $\Gamma\vdash\varphi$. La finitariedad sintáctica de [TLOG-PRO-00003](capitulo-03.md#tlog-pro-00003) produce un $\Gamma_0\subseteq\Gamma$ finito con $\Gamma_0\vdash\varphi$; corrección da $\Gamma_0\models\varphi$.

Para (4), una dirección es inmediata. Para la otra, supongamos que todo subconjunto finito de $\Gamma$ es satisfacible pero $\Gamma$ no lo es. Entonces, vacuamente,

$$
\Gamma\models\bot_{\mathrm{CPL}}.
$$

Por (3), algún $\Gamma_0\subseteq\Gamma$ finito satisface

$$
\Gamma_0\models\bot_{\mathrm{CPL}},
$$

por lo que $\Gamma_0$ no puede ser satisfacible, contradicción. $\square$

::: {.callout-important}
## Distinción de significado

La equivalencia
$$
\Gamma\vdash\varphi\iff\Gamma\models\varphi
$$
es **extensional**: las dos relaciones tienen los mismos pares $(\Gamma,\varphi)$ en este sistema. Sus definiciones y niveles siguen siendo distintos: una cuantifica sobre derivaciones finitas y la otra sobre valuaciones.
:::

## 4.17. Ejemplo desarrollado — del valor semántico a la prueba

Por semántica bivalente,

$$
\models_{\mathrm{CPL}}
(p_1\lor\neg p_1).
$$

Antes de [TLOG-MTH-00013](#tlog-mth-00013), esta afirmación semántica no autorizaba una conclusión sintáctica. Ahora la completitud permite inferir

$$
\boxed{
\vdash_{\mathsf H}
(p_1\lor\neg p_1)
}.
$$

La conclusión no redefine validez como demostrabilidad: usa un metateorema que conecta dos relaciones previamente construidas de manera independiente.

## 4.20. Cierre del capítulo y de la Parte I

Con `TLOG-CH04-M02` quedan demostradas las dos direcciones:

$$
\Gamma\vdash_{\mathsf H}\varphi
\Longrightarrow
\Gamma\models_{\mathrm{CPL}}\varphi,
$$

$$
\Gamma\models_{\mathrm{CPL}}\varphi
\Longrightarrow
\Gamma\vdash_{\mathsf H}\varphi.
$$

Por tanto,

$$
\boxed{\texttt{TLOG-CH04-0001 — CLOSED}}
$$

y los cinco capítulos de la Parte I cumplen su función arquitectónica:

$$
\boxed{\texttt{PARTE I — CLOSED / PASS}}.
$$

La Parte I entrega un sistema proposicional completo con sintaxis, semántica y deducción construidas por separado y comparadas mediante corrección y completitud. También quedan disponibles finitariedad semántica y compacidad proposicional.

Próximo frente arquitectónico:

```text
TLOG-CH05-0001 — Signaturas, términos y fórmulas
```

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 3](capitulo-03.md) · [Capítulo 5 →](capitulo-05.md)

