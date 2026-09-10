## §12. Demostrar una tautología y elegir método

A lo largo del capítulo hemos construido varias herramientas para estudiar fórmulas proposicionales.

Podemos:

1. **evaluarlas** mediante una tabla de verdad;
2. **clasificarlas** como tautologías, contradicciones o contingencias;
3. **compararlas** mediante equivalencia lógica;
4. **transformarlas** mediante leyes ya demostradas;
5. **refutar** una afirmación mediante una contraasignación;
6. **reconstruirlas** desde su tabla mediante FND o FNC.

Estas herramientas no compiten entre sí.

Responden a preguntas distintas.

El problema final del capítulo será aprender a elegir:

$$
\boxed{
\text{qué queremos demostrar}
\quad\longrightarrow\quad
\text{qué método conviene utilizar}.
}
$$

Una buena solución no es solamente correcta.

También debe ser **proporcionada al problema**.

Construir una tabla de ocho filas para una equivalencia que se reduce en tres pasos puede ser correcto, pero innecesariamente costoso.

Intentar simplificar algebraicamente una fórmula cuando basta una sola contraasignación también puede ser correcto, pero poco eficiente.

La madurez lógica comienza cuando podemos reconocer esa diferencia.

---

### 12.1 Método 1 — Tabla de verdad

La tabla de verdad es el procedimiento semántico más directo.

Resulta especialmente útil cuando queremos:

- conocer el comportamiento completo de una fórmula;
- decidir si es tautología, contradicción o contingencia;
- comparar dos fórmulas con pocas variables;
- obtener una FND o una FNC desde las filas de la tabla.

Su principal ventaja es:

$$
\boxed{\text{exhaustividad}.}
$$

Si una fórmula contiene:

$$
n
$$

variables proposicionales distintas, la tabla contiene:

$$
2^n
$$

filas.

Eso mismo muestra su principal costo.

Con dos variables necesitamos:

$$
4
$$

filas.

Con tres:

$$
8.
$$

Con cuatro:

$$
16.
$$

Con cinco:

$$
32.
$$

Por tanto, una tabla completa es conceptualmente sencilla, pero puede crecer rápidamente.

---

### 12.2 Método 2 — Cadena de equivalencias

Si reconocemos en una fórmula estructuras ya cubiertas por nuestras leyes, podemos transformarla mediante:

$$
F_0
\equiv
F_1
\equiv
\cdots
\equiv
F_n.
$$

Este método es especialmente útil cuando queremos:

- simplificar una fórmula;
- eliminar implicaciones o bicondicionales;
- demostrar que dos fórmulas son equivalentes;
- demostrar una tautología reduciéndola a una fórmula tautológica conocida.

Por ejemplo:

$$
P\Rightarrow P
$$

se transforma en:

$$
\neg P\lor P.
$$

Por complemento:

$$
\neg P\lor P\equiv T.
$$

Luego:

$$
P\Rightarrow P
$$

es una tautología.

No hemos necesitado construir su tabla.

La ventaja es:

$$
\boxed{\text{economía cuando la estructura es reconocible}.}
$$

La exigencia es igualmente clara:

> cada paso debe estar autorizado por una equivalencia previamente demostrada.

---

### 12.3 Método 3 — Contraasignación

Supongamos que alguien afirma:

> «$F$ es una tautología».

Para refutarlo no necesitamos saber qué ocurre en todas las filas.

Basta encontrar una donde:

$$
F=\mathrm F.
$$

Análogamente, para refutar:

$$
P\equiv Q,
$$

basta una asignación donde $P$ y $Q$ reciban valores distintos.

La contraasignación es, por tanto, el método natural cuando la tarea consiste en **refutar una afirmación universal sobre todas las asignaciones**.

Su ventaja es:

$$
\boxed{\text{una sola fila puede bastar}.}
$$

Por ejemplo, la fórmula:

$$
(P\lor Q)\Rightarrow P
$$

no es una tautología, porque para:

$$
P=\mathrm F,
\qquad
Q=\mathrm V
$$

obtenemos:

$$
(P\lor Q)\Rightarrow P
=
\mathrm V\Rightarrow\mathrm F
=
\mathrm F.
$$

No hace falta calcular las otras tres filas.

---

### 12.4 Método 4 — Formas normales

Las formas normales son especialmente útiles cuando queremos reconstruir una fórmula desde su comportamiento semántico.

Desde una tabla:

$$
\text{filas }\mathrm V
\longrightarrow
\text{FND},
$$

$$
\text{filas }\mathrm F
\longrightarrow
\text{FNC}.
$$

También pueden ser útiles cuando queremos una forma regular que utilice solamente:

$$
\neg,\qquad
\land,\qquad
\lor.
$$

Pero una forma normal obtenida directamente de una tabla no tiene por qué ser la forma más corta.

Así, las formas normales son especialmente valiosas para:

$$
\boxed{\text{existencia, reconstrucción y organización}},
$$

más que para garantizar simplificación mínima.

---

### 12.5 Una guía de elección

Podemos resumir provisionalmente:

| Pregunta | Método que conviene probar primero |
|---|---|
| ¿Qué ocurre en todas las asignaciones? | tabla de verdad |
| ¿Es tautología con pocas variables? | tabla o equivalencias |
| ¿Puedo reducirla rápidamente a leyes conocidas? | equivalencias |
| ¿Quiero refutar que sea tautología? | contraasignación |
| ¿Quiero refutar una equivalencia? | contraasignación |
| ¿Quiero construir una fórmula desde una tabla? | FND/FNC |
| ¿Quiero una forma regular con $\neg,\land,\lor$? | transformación o formas normales |

Esta tabla no es un algoritmo obligatorio.

Una misma tarea puede admitir varios métodos correctos.

La elección depende de la estructura concreta de la fórmula.

---

### 12.6 Demostrar una tautología mediante equivalencias

Consideremos:

$$
(P\land Q)\Rightarrow P.
$$

Podemos construir una tabla.

Pero la transformación algebraica es muy corta.

Eliminamos la implicación:

$$
(P\land Q)\Rightarrow P
\equiv
\neg(P\land Q)\lor P.
$$

Por De Morgan:

$$
\equiv
(\neg P\lor\neg Q)\lor P.
$$

Por asociatividad y conmutatividad:

$$
\equiv
(\neg P\lor P)\lor\neg Q.
$$

Por complemento:

$$
\equiv
T\lor\neg Q.
$$

Por dominación:

$$
\equiv
T.
$$

Por tanto:

$$
\boxed{
(P\land Q)\Rightarrow P
\text{ es una tautología}.
}
$$

Aquí la cadena de equivalencias revela además **por qué** la fórmula es siempre verdadera.

---

### 12.7 Demostrar una tautología mediante una tabla

Ahora tomemos una fórmula más compleja:

$$
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r).
$$

En [el ejercicio «Una equivalencia de implicaciones anidadas»](#apm-i-e0120) ya demostramos algebraicamente que las dos partes del bicondicional son lógicamente equivalentes.

Ahora construiremos la tabla completa para comprobarlo semánticamente.

Necesitamos ocho filas.

| $p$ | $q$ | $r$ | $q\Rightarrow r$ | $p\Rightarrow(q\Rightarrow r)$ | $p\land q$ | $(p\land q)\Rightarrow r$ | Fórmula completa |
|---|---|---|---|---|---|---|---|
| $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |
| $\mathrm F$ | $\mathrm F$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ | $\mathrm F$ | $\mathrm V$ | $\mathrm V$ |

La columna final contiene únicamente:

$$
\mathrm V.
$$

Por definición:

$$
\boxed{
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
}
$$

es una tautología.

---

### 12.8 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0020}
**Ejemplo — Una tautología por dos métodos**

:::

Demostremos nuevamente que:

$$
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
$$

es una tautología, pero ahora comparemos deliberadamente dos métodos.

#### Método A — Tabla

La tabla de §12.7 muestra que la columna final contiene:

$$
\mathrm V
$$

en las ocho asignaciones.

Por tanto, la fórmula es una tautología.

#### Método B — Transformación algebraica

Estudiemos primero el lado izquierdo del bicondicional:

$$
p\Rightarrow(q\Rightarrow r).
$$

Eliminamos la implicación exterior:

$$
\equiv
\neg p\lor(q\Rightarrow r).
$$

Eliminamos la implicación interior:

$$
\equiv
\neg p\lor(\neg q\lor r).
$$

Por asociatividad:

$$
\equiv
(\neg p\lor\neg q)\lor r.
$$

Por De Morgan en sentido inverso:

$$
\equiv
\neg(p\land q)\lor r.
$$

Por [la proposición «Equivalencias fundamentales de la implicación»](#apm-i-p0005) en sentido inverso:

$$
\equiv
(p\land q)\Rightarrow r.
$$

Por tanto:

$$
\boxed{
p\Rightarrow(q\Rightarrow r)
\equiv
(p\land q)\Rightarrow r.
}
$$

Por [la proposición «Criterio bicondicional para la equivalencia lógica»](#apm-i-p0001), el bicondicional entre dos fórmulas lógicamente equivalentes es una tautología.

Luego:

$$
\boxed{
(p\Rightarrow(q\Rightarrow r))
\leftrightarrow
((p\land q)\Rightarrow r)
}
$$

es una tautología.

#### Comparación

La tabla tiene una ventaja:

> hace visible el comportamiento completo de las ocho asignaciones.

La transformación tiene otra:

> muestra que las dos partes son en realidad dos escrituras equivalentes de la misma condición lógica.

Ambos métodos son rigurosos.

Pero responden a intuiciones diferentes.

---

### 12.9 Elegir un método no significa adivinar

La elección estratégica puede apoyarse en preguntas concretas.

#### ¿Hay pocas variables?

Una tabla puede ser razonable.

#### ¿Reconozco una ley inmediata?

Conviene intentar equivalencias.

#### ¿La afirmación que quiero demostrar parece falsa?

Antes de construir una tabla completa, conviene buscar una contraasignación.

#### ¿Tengo una tabla y quiero reconstruir la fórmula?

Las formas normales son naturales.

#### ¿Una primera ruta se vuelve larga?

Puede ser señal de que otra herramienta es mejor.

No hay contradicción en cambiar de método durante una solución.

La lógica matemática no exige fidelidad a una técnica.

Exige que cada conclusión esté justificada.

---

### 12.10 Verificar y demostrar

Una tabla completa puede demostrar una afirmación semántica porque enumera todas las asignaciones posibles.

Una cadena de equivalencias puede demostrarla porque cada paso conserva el comportamiento lógico.

Una contraasignación puede refutarla porque una sola excepción basta.

Una forma normal puede reconstruirla porque está diseñada para reproducir exactamente las filas verdaderas o falsas.

Los cuatro procedimientos son diferentes manifestaciones de una misma disciplina:

$$
\boxed{
\text{no basta obtener el resultado;}
\quad
\text{hay que controlar por qué el procedimiento lo garantiza}.
}
$$

---
