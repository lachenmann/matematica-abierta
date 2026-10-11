---
title: Capítulo 0 — Niveles, lenguajes y sistemas formales
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
content-id: MA-BCH-0202
content-type: book-chapter
source-id: TLOG-CH00-0001
prerequisites: []
related:
- MA-BOK-0014
source-sha256: 9a8789a219d8ad5e51b2d68169529b5442f20fce7a3b2d8c2278fe61f19187b9
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[Capítulo 1 →](capitulo-01.md)

## 0.0. Función del capítulo

Este capítulo fija el vocabulario mínimo con el que el tratado hablará **acerca de** lenguajes y sistemas formales antes de estudiar un cálculo concreto. Su función no es desarrollar todavía la sintaxis proposicional ni la lógica de primer orden; es impedir que el texto cambie silenciosamente de nivel entre el lenguaje que estudiamos y el lenguaje con el que lo estudiamos.

La entrada del capítulo es la infraestructura normativa ya cerrada de TLOG: `TLOG-0001`, `TLOG-0002` y `TLOG-DOMAIN-QA-0001`. Su salida prevista es un conjunto mínimo de definiciones y convenciones reutilizables por los capítulos posteriores.

Fuentes efectivamente cotejadas para este borrador:

- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001): Introducción, pp. xi–xii; §1.0, pp. 11–13; §1.1, pp. 13–19.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010): Introducción, pp. xv–xvi.

Estas fuentes funcionan como **control expositivo y terminológico**. Las formulaciones siguientes son propias de TLOG y quedan bajo su contrato fundacional.

## 0.1. Dos niveles y una interfaz

### Convención 0.1.1 — Estratificación de trabajo {#tlog-cnv-00001}

En toda unidad del tratado distinguiremos, cuando la distinción sea sustantiva, tres capas:

$$
\texttt{meta},\qquad \texttt{object:<system-id>},\qquad \texttt{interface}.
$$

- **Metanivel (`meta`)**: nivel en el que TLOG construye, describe y demuestra hechos acerca de expresiones, lenguajes, teorías, derivaciones y modelos.
- **Nivel objeto (`object:<system-id>`)**: nivel interno del sistema formal identificado por `system-id`.
- **Interfaz (`interface`)**: capa en la que una construcción metateórica codifica, interpreta o relaciona objetos de uno o más sistemas sin identificarlos con la metateoría.

Esta convención implementa la separación exigida por `TLOG-0001` y coincide con la distinción clásica entre lenguaje objeto y metalenguaje que Rautenberg usa como rasgo central de la lógica matemática moderna. No presupone que todos los sistemas objeto compartan la misma lógica ni que el metalenguaje sea idéntico al lenguaje objeto.

En particular:

$$
\text{afirmación metateórica}\neq\text{fórmula del sistema objeto}.
$$

El cambio de una capa a otra deberá quedar autorizado por una definición, una interpretación o un metateorema explícito.

## 0.2. Símbolos y expresiones

### Definición 0.2.1 — Alfabeto formal {#tlog-def-00001}

Un **alfabeto formal** es un conjunto no vacío de objetos que, en el sistema considerado, reciben el papel de símbolos básicos. Lo denotaremos provisionalmente por

$$
\Sigma.
$$

La naturaleza ontológica concreta de los símbolos no forma parte de la sintaxis: pueden representarse por caracteres tipográficos, códigos u otros objetos, siempre que la representación elegida permita distinguirlos sin ambigüedad.

### Definición 0.2.2 — Expresión sobre un alfabeto {#tlog-def-00002}

Dado un alfabeto $\Sigma$, una **expresión sobre $\Sigma$** es una secuencia finita de símbolos de $\Sigma$. Escribiremos

$$
\Sigma^{<\omega}
$$

para la colección de todas las secuencias finitas sobre $\Sigma$.

La condición de ser expresión es puramente sintáctica. Una expresión puede o no ser admisible como término, fórmula, demostración u otro objeto bien formado de un sistema particular.

Esta separación sigue el patrón de Enderton: primero se fija el alfabeto y las secuencias de símbolos; después se decide cuáles de esas secuencias cuentan como expresiones gramaticalmente correctas.

## 0.3. Formación y lenguaje

### Definición 0.3.1 — Especificación de formación {#tlog-def-00003}

Una **especificación de formación** sobre $\Sigma$ es un conjunto explícito de cláusulas que determina qué expresiones de $\Sigma^{<\omega}$ se aceptan como bien formadas para una categoría sintáctica dada.

La especificación puede darse mediante:

- casos básicos;
- operaciones constructoras;
- reglas inductivas;
- o un procedimiento equivalente cuya extensión quede matemáticamente determinada.

Decir simplemente que una cadena “tiene sentido” no constituye una especificación formal.

### Definición 0.3.2 — Lenguaje formal {#tlog-def-00004}

Un **lenguaje formal** $L$ sobre un alfabeto $\Sigma$ es un conjunto de expresiones sobre ese alfabeto:

$$
L\subseteq\Sigma^{<\omega}.
$$

Cuando un lenguaje se presenta mediante reglas de formación, una especificación como la de la Definición 0.3.1 constituye **datos adicionales** que determinan qué expresiones pertenecen a $L$. La noción general de lenguaje formal no exige, por sí sola, que la pertenencia a $L$ sea decidible, computable, recursivamente enumerable ni generada por un mecanismo sintáctico particular.

La definición separa así tres cuestiones:

1. **qué cadenas pertenecen al lenguaje**;
2. **cómo, si corresponde, se especifica o genera esa colección**;
3. **qué interpretación, si alguna, recibirán después**.

Por eso la pertenencia a $L$ no depende por sí sola de verdad, referencia o significado, ni implica una propiedad de efectividad. Enderton sirve aquí como control de la precedencia de la sintaxis respecto de la interpretación; TLOG mantiene además, por su contrato fundacional, la separación entre existencia/definición y efectividad.

## 0.4. Qué llamaremos “sistema formal”

### Convención 0.4.1 — Datos mínimos de un sistema objeto {#tlog-cnv-00002}

Cuando TLOG declare que un objeto $\mathfrak S$ es un **sistema formal** deberá permitir recuperar, al menos cuando corresponda:

1. su lenguaje $L$;
2. las categorías sintácticas relevantes;
3. axiomas o esquemas de axiomas, si existen;
4. reglas de inferencia, si existen;
5. las condiciones laterales de esas reglas;
6. la noción de derivación o cierre deductivo que resulte de los datos anteriores;
7. la capa en que se habla del sistema.

Esta es una **convención de interfaz**, no una afirmación de que todos los sistemas formales deban presentarse mediante una única tupla rígida. La definición exacta de derivación se pospone hasta los cálculos deductivos correspondientes.

Rautenberg subraya que la metateoría estudia lenguajes y teorías formales y especifica procedimientos de inferencia mediante cálculos puramente sintácticos. TLOG adopta ese principio manteniendo explícita la capa `meta` donde se formula tal descripción.

## 0.5. Ejemplo desarrollado — expresión no equivale a fórmula

Sea

$$
\Sigma=\{a,b\}.
$$

Entonces

$$
aba\in\Sigma^{<\omega}
$$

es una expresión por la Definición 0.2.2. Ahora supongamos que fijamos el lenguaje de todas las cadenas de longitud dos; equivalentemente, puede describirse mediante una especificación de formación que acepte exactamente esas cadenas:

$$
L=\{aa,ab,ba,bb\}.
$$

Por tanto,

$$
aba\notin L.
$$

No hay contradicción: `aba` es una expresión sobre el alfabeto, pero no una expresión bien formada del lenguaje definido por esas reglas. El ejemplo muestra por qué TLOG separará sistemáticamente

$$
\text{cadena de símbolos}
\neq
\text{expresión bien formada de un lenguaje}.
$$

La envolvente pedagógica del capítulo se limita a ejemplos desarrollados como éste; no se incorpora un banco de ejercicios al cuerpo canónico.

## 0.6. Estado deductivo del bloque

Los seis nodos anteriores están registrados en estado `closed` después de la auditoría `TLOG-CH00-CLOSURE-AUDIT-0001`.

Dependencias directas del bloque:

```text
TLOG-DEF-00002 -> TLOG-DEF-00001
TLOG-DEF-00003 -> TLOG-DEF-00002
TLOG-DEF-00004 -> TLOG-DEF-00002
TLOG-CNV-00002 -> TLOG-CNV-00001
TLOG-CNV-00002 -> TLOG-DEF-00004
```

No hay dependencias intertratados activas.

## 0.8. Cierre del capítulo

`CORP-M06-09` audita los seis nodos en orden topológico bajo `TLOG-0002`, `TLOG-DOMAIN-QA-0001`, `MATH-FAP-0001`, `SOURCE_AND_QA.md` y control de aciclicidad. La auditoría detectó y corrigió antes del cierre una sobre-restricción en [TLOG-DEF-00004](#tlog-def-00004): la definición genérica de lenguaje formal ya no exige una especificación de formación ni presupone efectividad.

Orden de cierre:

1. [TLOG-CNV-00001](#tlog-cnv-00001) — `closed`;
2. [TLOG-DEF-00001](#tlog-def-00001) — `closed`;
3. [TLOG-DEF-00002](#tlog-def-00002) — `closed`;
4. [TLOG-DEF-00003](#tlog-def-00003) — `closed`;
5. [TLOG-DEF-00004](#tlog-def-00004) — `closed` tras la corrección indicada;
6. [TLOG-CNV-00002](#tlog-cnv-00002) — `closed`.

Estado final:

```text
registered nodes = 6
closed nodes = 6
DAG nodes = 6
DAG direct edges = 5
cycle-check = PASS
cross-treaty direct edges = 0
formalization selected = 0
```

La evidencia detallada queda en `TLOG-CH00-CLOSURE-AUDIT-0001`. El cierre es matemático/editorial; no implica Lean ni publicación web.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[Capítulo 1 →](capitulo-01.md)

