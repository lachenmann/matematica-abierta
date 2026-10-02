---
title: 'Tratado moderno de Álgebra — Capítulo 27: Cuerpos ordenados'
description: Capítulo del Tratado moderno de Álgebra dedicado a cuerpos ordenados, inversos, división y comparación de cocientes.
author: Gustav A. Tachek
content-id: MA-BCH-0135
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-10-02'
date-modified: '2026-10-02'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
- cuerpos-ordenados
prerequisites:
- MA-BCH-0062
related:
- MA-BOK-0007
- MA-BCH-0062
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 27 — Cuerpos ordenados

## 27.0. El problema: introducir la división sin perder el orden

El capítulo 22 construyó los cuerpos como **anillos conmutativos no triviales** en los que todo elemento no nulo es invertible (Definición 22.1.1). El capítulo 26 construyó independientemente los anillos totalmente ordenados (Definición 26.12.1): el grupo aditivo es totalmente ordenado y el conjunto de elementos no negativos es cerrado bajo multiplicación.

Al reunir ambas condiciones no debemos introducir clandestinamente otra propiedad. En particular, la positividad de la unidad, la inexistencia de divisores de cero y las reglas estrictas del producto serán **consecuencias de resultados anteriores**, no axiomas adicionales de la nueva definición.

```text
    cuerpo                            anillo totalmente ordenado
    (Def. 22.1.1)                    (Def. 26.12.1)
    conmutativo                       grupo aditivo totalmente ordenado
    no trivial                        producto de no negativos ≥ 0
    inversos para a ≠ 0                      │
         └─────────────────────────┬────────┘
                                   ▼
                            CUERPO ORDENADO
```

**Pregunta de activación.** ¿Qué distingue al nuevo objeto de un anillo totalmente ordenado? Que todo elemento no nulo dispone ahora de inverso multiplicativo; además, la definición previa de cuerpo ya proporciona conmutatividad y $0\ne1$.

---

## 27.1. Definición de cuerpo ordenado

### Definición 27.1.1 — Cuerpo ordenado {#talg-def-00061}
Sea $F$ un conjunto con operaciones binarias $+$, $\cdot$ y una relación $\le$ sobre $F$. Diremos que

$$
\langle F,+,\cdot,\le\rangle
$$

es un **cuerpo ordenado** si se satisfacen simultáneamente las siguientes condiciones:

1. $\langle F,+,\cdot\rangle$ es un **cuerpo** en el sentido de la Definición 22.1.1.
2. $\langle F,+,\cdot,\le\rangle$ es un **anillo totalmente ordenado** en el sentido de la Definición 26.12.1.

La segunda condición significa, explícitamente, que $\le$ es un orden total compatible con las traslaciones aditivas y que

$$
\forall a,b\in F,\qquad
(0\le a\ \land\ 0\le b)\Longrightarrow 0\le ab.
$$

La primera incorpora conmutatividad, $0\ne1$ y la existencia de inversos multiplicativos para todos los elementos no nulos. Por ello la estructura no es un «anillo de división ordenado» no conmutativo ni admite el anillo trivial.

> **Consecuencia ya demostrada, no axioma nuevo.** La Proposición 26.16.1 prueba que la unidad de cualquier anillo totalmente ordenado es no negativa y, si el anillo es no trivial, estrictamente positiva. Como un cuerpo cumple $0\ne1$, en todo cuerpo ordenado tenemos $0<1$. No constituye una condición tercera de la definición.

La notación de cuádrupla es una abreviatura tipográfica de la codificación conjuntista convencional. La definición no presupone que la comparación o la igualdad sean decidibles, ni proporciona un algoritmo para calcular inversos. La existencia de inversos se toma de la definición de cuerpo, sin apelar a Choice.

---

## 27.2. Qué no forma parte de la definición

| enunciado | estatus lógico |
|---|---|
| $0<1$ | consecuencia previa: cuerpo no trivial + Proposición 26.16.1 |
| todo $a\ne0$ posee inverso multiplicativo | contenido de la definición previa de cuerpo |
| no existen divisores de cero | teorema previo para cuerpos, no axioma adicional |
| $0<a\Longrightarrow 0<a^{-1}$ | Proposición 27.4.1, demostrada en esta unidad |
| la comparación $a\le b$ es algorítmicamente decidible | no se afirma |
| existen supremos de subconjuntos acotados | no se afirma |
| el cuerpo es arquimediano | no se afirma |

Los ejemplos enteros y racionales de este capítulo usan las estructuras y las incrustaciones importadas en la Interfaz 24.0.1.

**No-ejemplo conceptual.** Un anillo totalmente ordenado con elementos no nulos que carecen de inverso no es automáticamente un cuerpo ordenado. Así, el orden usual de $\mathbb Z$ es compatible con suma y multiplicación y es total, pero $2$ no tiene inverso multiplicativo en $\mathbb Z$. En efecto, la forma normal entera y el orden natural dan, para todo entero $z$, $z\le0$ o $1\le z$. En el primer caso $2z\le0<1$; en el segundo $2z\ge2>1$. Por tanto $2z=1$ es imposible. Esta observación ilustra la necesidad de la primera condición; no interviene en ninguna demostración.

**Lectura inversa.** Para comprobar si una estructura dada es un cuerpo ordenado hay que verificar primero las propiedades de cuerpo y, separadamente, la compatibilidad ordenada. No basta con demostrar $0<1$ ni con disponer de un orden total cualquiera: el cono no negativo debe ser multiplicativamente estable.

---

## 27.4. El inverso de un elemento positivo conserva la positividad

La división introduce una dificultad que no surgía para la multiplicación: sabemos que un elemento positivo y no nulo posee un inverso, pero todavía no conocemos su signo. Por tanto, **no está permitido multiplicar una desigualdad por $a^{-1}$ como si su positividad ya estuviera probada**. La estrategia correcta es multiplicar por el elemento $a$, cuyo signo sí está controlado, y utilizar la totalidad para identificar el signo del inverso.

```text
0 < a  ⇒  a ≠ 0  ⇒  existe a⁻¹ y a·a⁻¹ = 1
                              │
                    ¿a⁻¹ ≤ 0? ── multiplicar por a ≥ 0
                              │
                              ▼
                          1 ≤ 0  ✗  (porque 0 < 1)
                              │
             totalidad: 0 ≤ a⁻¹  o  a⁻¹ ≤ 0
                              │
                  sólo queda 0 ≤ a⁻¹
                              │
                  a⁻¹ ≠ 0  ⇒  0 < a⁻¹
```

### Proposición 27.4.1 — Positividad del inverso de un elemento positivo {#talg-pro-00079}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Para todo $a\in F$,

$$
0<a\ \Longrightarrow\ 0<a^{-1}.
$$

El inverso del consecuente existe porque $0<a$ implica $a\ne0$, y la definición de cuerpo garantiza que todo elemento no nulo es invertible.

#### Demostración {#talg-prf-00123}
Supongamos $0<a$. Por la definición de orden estricto asociado (interfaz de órdenes, Interfaz 25.1.1), tenemos simultáneamente

$$
0\le a,\qquad a\ne0.
$$

La definición de cuerpo garantiza un inverso multiplicativo, escrito $a^{-1}$ según la Notación 15.3.1, que satisface

$$
a\cdot a^{-1}=1.
$$

Además, la Proposición 26.16.1 da $0<1$, pues el cuerpo es un anillo totalmente ordenado y no trivial. En particular,

$$
0\le1,\qquad 0\ne1.
$$

**Primer paso: excluir que el inverso sea no positivo.** Supongamos que $a^{-1}\le0$. Como $0\le a$, la monotonía multiplicativa por factores no negativos (Proposición 26.6.1), aplicada **por la izquierda** con factor $a$, produce

$$
a\cdot a^{-1}\le a\cdot0.
$$

La identidad del inverso y la absorción del cero (Proposición 14.3.1) convierten esto en

$$
1\le0.
$$

Pero $0\le1$ y la antisimetría del orden implicarían $0=1$, en contradicción con $0\ne1$. Por consiguiente,

$$
\neg(a^{-1}\le0).
$$

**Segundo paso: usar la totalidad, sin postular decidibilidad.** Como el orden del cuerpo es total, aplicado a $0$ y $a^{-1}$ da la disyunción

$$
0\le a^{-1}\quad\lor\quad a^{-1}\le0.
$$

La segunda alternativa contradice lo ya probado; por eliminación de la disyunción se obtiene

$$
0\le a^{-1}.
$$

**Tercer paso: descartar el cero.** Si $a^{-1}=0$, entonces

$$
1=a\cdot a^{-1}=a\cdot0=0,
$$

otra contradicción con la no trivialidad. Así, $a^{-1}\ne0$. La definición de orden estricto asociado, aplicada a $0\le a^{-1}$ y $a^{-1}\ne0$, concluye

$$
0<a^{-1}.
$$

Queda demostrada la proposición. $\square$

> **Lectura guiada de la prueba.** La desigualdad que se multiplica es $a^{-1}\le0$, una hipótesis provisional. El factor elegido es $a\ge0$, cuyo signo está demostrado desde el comienzo. Multiplicar por el inverso en este momento sería circular, pues precisamente se busca averiguar si dicho inverso es positivo.

> **Ejemplo intuitivo, no premisa.** En el cuerpo de los racionales con su orden usual, $2>0$ y $2^{-1}=1/2>0$. El argumento anterior prueba la misma conclusión en *todo* cuerpo ordenado sin apelar a una representación numérica de sus elementos.

> **Caso frontera.** $a=0$ queda excluido por el antecedente estricto; el cero no posee inverso en un cuerpo no trivial. El caso $a<0$ no se infiere de esta proposición por sustitución informal: su tratamiento será un resultado separado.

---

## 27.6. El inverso de un elemento negativo es negativo

El caso negativo no se obtiene multiplicando una desigualdad por $a^{-1}$ antes de conocer su signo. La idea consiste en transformar primero el dato $a<0$ en una positividad ya tratada: $0<-a$. Falta justificar una identidad algebraica que no debe darse por supuesta, la relación entre el inverso multiplicativo del opuesto y el opuesto del inverso.

```text
     a < 0
       │  inversión del orden por opuesto aditivo (25.5.1)
       ▼
     0 < -a
       │  positividad del inverso (27.4.1)
       ▼
     0 < (-a)⁻¹
       │  reglas de signos + unicidad del inverso multiplicativo
       ▼
     0 < -(a⁻¹)
       │  inversión del orden por opuesto aditivo (25.5.1)
       ▼
     a⁻¹ < 0
```

### Proposición 27.6.1 — Negatividad del inverso de un elemento negativo {#talg-pro-00080}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Para todo $a\in F$,

$$
a<0\quad\Longrightarrow\quad a^{-1}<0.
$$

El antecedente implica $a\ne0$ y, por la definición de cuerpo, asegura la existencia del inverso multiplicativo del consecuente.

#### Demostración {#talg-prf-00124}
Supongamos $a<0$. Por la definición del orden estricto asociado, $a\ne0$. La estructura de cuerpo garantiza un inverso bilateral $a^{-1}$, determinado de manera única y denotado según la Notación 15.3.1:

$$
a\cdot a^{-1}=a^{-1}\cdot a=1.
$$

**Primer paso: convertir el antecedente en una desigualdad positiva.** La inversión del orden estricto por el opuesto aditivo (Proposición 25.5.1), aplicada a $a<0$, da $-0<-a$. Como el opuesto aditivo del cero es el propio cero,

$$
0<-a.
$$

En particular, $-a\ne0$ y existe su inverso multiplicativo $(-a)^{-1}$. La Proposición 27.4.1, aplicada **a $-a$**, cuyo signo ya está demostrado, implica

$$
0<(-a)^{-1}.
$$

**Segundo paso: justificar la identidad algebraica de inversos.** El elemento $-(a^{-1})$ es candidato a inverso bilateral de $-a$. Las reglas de signos de la Proposición 14.4.1 prueban, sin emplear desigualdades,

$$
(-a)\cdot\bigl(-(a^{-1})\bigr)
=a\cdot a^{-1}=1,
$$

y, conservando explícitamente la otra lateralidad,

$$
\bigl(-(a^{-1})\bigr)\cdot(-a)
=a^{-1}\cdot a=1.
$$

La unicidad del inverso multiplicativo (Proposición 15.2.1) permite identificar ambos elementos:

$$
(-a)^{-1}=-(a^{-1}).
$$

No se trata de una convención de signos, sino de una igualdad demostrada. Sustituyéndola en la desigualdad del primer paso obtenemos

$$
0<-(a^{-1}).
$$

**Tercer paso: recuperar el signo buscado.** Aplicamos de nuevo la inversión del orden estricto por el opuesto aditivo (Proposición 25.5.1):

$$
-\bigl(-(a^{-1})\bigr)<-0.
$$

Por la involución del opuesto y la identidad $-0=0$,

$$
a^{-1}<0.
$$

Queda demostrada la proposición. $\square$

> **Lectura guiada.** El primer inverso cuyo signo se estudia es el de $-a$, elemento positivo. La igualdad $(-a)^{-1}=-(a^{-1})$ se comprueba con los dos productos y la unicidad del inverso. Sólo entonces se traslada el signo a $a^{-1}$; en ningún momento se multiplicó por un factor de signo desconocido.

> **Ejemplo ilustrativo, no premisa.** Con el orden usual de los racionales, $-2<0$ y $(-2)^{-1}=-1/2<0$. El razonamiento anterior no depende de esta representación y se aplica a cualquier cuerpo ordenado.

> **Caso frontera.** No puede sustituirse $a<0$ por $a\le0$: $a=0$ satisface la desigualdad débil, pero carece de inverso multiplicativo en un cuerpo no trivial.

---

## 27.8. Inversión y reversión del orden entre positivos

Ya sabemos que el inverso de un positivo es positivo (Proposición 27.4.1). Eso **no prueba todavía** cómo se comparan dos inversos. La estrategia preserva inicialmente una desigualdad no estricta multiplicándola por factores cuyo signo ya está demostrado; la estricta se recupera mediante la inyectividad de la inversión, justificada algebraicamente, y no mediante un supuesto tácito de cancelación.

```text
         0 < a < b
           │  positividad de los inversos (27.4.1)
           ▼
       0 < a⁻¹, b⁻¹
           │  a ≤ b; multiplicar a la derecha por b⁻¹ ≥ 0
           ▼
         ab⁻¹ ≤ 1
           │  multiplicar a la izquierda por a⁻¹ ≥ 0
           ▼
         b⁻¹ ≤ a⁻¹
           │  igualdad de inversos ⇒ a=b; contradice a<b
           ▼
         b⁻¹ < a⁻¹
```

### Proposición 27.8.1 — La inversión revierte el orden entre elementos positivos {#talg-pro-00081}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Para cualesquiera $a,b\in F$ tales que $0<a$ y $0<b$,

$$
a<b\quad\Longleftrightarrow\quad b^{-1}<a^{-1}.
$$

En particular, la inversión es **estrictamente antítona** en el conjunto de elementos positivos. Las hipótesis $0<a$ y $0<b$ garantizan la existencia de ambos inversos y el conocimiento previo de sus signos.

#### Demostración {#talg-prf-00125}
Por $0<a$ y $0<b$, la definición de cuerpo y la Notación 15.3.1 proporcionan inversos bilaterales, con

$$
a^{-1}a=aa^{-1}=1,\qquad b^{-1}b=bb^{-1}=1.
$$

La Proposición 27.4.1, aplicada **por separado a $a$ y a $b$**, establece

$$
0<a^{-1},\qquad 0<b^{-1}.
$$

Por la definición del orden estricto asociado, ambos inversos son también no negativos.

**Primera implicación.** Supongamos $a<b$. Por definición, $a\le b$ y $a\ne b$. Multiplicamos $a\le b$ **por la derecha** por $b^{-1}\ge0$; la Proposición 26.6.1 da

$$
ab^{-1}\le bb^{-1}=1.
$$

Multiplicamos ahora esta desigualdad **por la izquierda** por $a^{-1}\ge0$, usando nuevamente la Proposición 26.6.1. Por asociatividad e identidad multiplicativa,

$$
a^{-1}(ab^{-1})\le a^{-1}1,
\qquad\text{es decir,}\qquad b^{-1}\le a^{-1}.
$$

Justifiquemos que la desigualdad es estricta. Si $b^{-1}=a^{-1}$, podemos multiplicar **la igualdad** por $a$ a la izquierda y por $b$ a la derecha; las identidades de inversos dan

$$
a(b^{-1}b)=(aa^{-1})b
\quad\Longrightarrow\quad a=b,
$$

contrariamente a $a\ne b$. Luego $b^{-1}\ne a^{-1}$, y la definición de orden estricto concluye

$$
b^{-1}<a^{-1}.
$$

**Segunda implicación.** Supongamos $b^{-1}<a^{-1}$. Ya hemos probado que $b^{-1}$ y $a^{-1}$ son positivos. Podemos aplicarles la **primera implicación ya demostrada**, tomando $u=b^{-1}$ y $v=a^{-1}$; resulta

$$
(a^{-1})^{-1}<(b^{-1})^{-1}.
$$

Para identificar estos inversos iterados no postulamos una nueva ley: $a$ es inverso bilateral de $a^{-1}$ porque $aa^{-1}=a^{-1}a=1$. La unicidad del inverso multiplicativo (Proposición 15.2.1) asegura $(a^{-1})^{-1}=a$. Análogamente, $(b^{-1})^{-1}=b$. Por sustitución,

$$
a<b.
$$

Quedan probadas las dos implicaciones. $\square$

> **Lectura guiada.** No se multiplica por un inverso hasta conocer su positividad, probada en §27.4. La monotonía no estricta proporciona primero $b^{-1}\le a^{-1}$; el paso a $<$ necesita descartar la igualdad mediante identidades multiplicativas. La vuelta de la equivalencia sólo reutiliza la implicación directa ya cerrada y la unicidad de inversos, sin razonamiento circular.

> **Ejemplo no deductivo.** En $\mathbb Q$ con el orden usual, $0<2<5$ y $0<1/5<1/2$: el menor positivo tiene inverso mayor. El ejemplo ilustra, pero no fundamenta, la proposición.

> **Límite del dominio.** La inversión no revierte el orden en todo $F\setminus\{0\}$ sin distinguir signos: $-1<1$, pero $1^{-1}=1$ no es menor que $(-1)^{-1}=-1$. El caso de dos números negativos exige una prueba independiente, reservada para §27.10. Si $a=0$ o $b=0$, alguna expresión inversa carece de sentido.

---

## 27.10. La inversión revierte el orden también entre negativos

La reversión del orden entre positivos (Proposición 27.8.1) no puede aplicarse *directamente* a números negativos. Pero la inversión del orden estricto al tomar opuestos convierte ambos negativos en positivos. Hay que conservar cuidadosamente el orden de los términos: si $a<b<0$, entonces $0<-b<-a$, no $0<-a<-b$. El vínculo entre ambos inversos ya fue establecido en la demostración de la Proposición 27.6.1.

```text
            a < b < 0
               │ tomar opuestos; invertir el orden (25.5.1)
               ▼
           0 < -b < -a
               │ aplicar 27.8.1 a los positivos -b y -a
               ▼
        (-a)⁻¹ < (-b)⁻¹
               │ identidad de inversos de opuestos (§27.6)
               ▼
          -a⁻¹ < -b⁻¹
               │ tomar opuestos; invertir el orden
               ▼
            b⁻¹ < a⁻¹
```

### Proposición 27.10.1 — La inversión revierte el orden entre elementos negativos {#talg-pro-00082}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Para cualesquiera $a,b\in F$ tales que $a<0$ y $b<0$,

$$
a<b\quad\Longleftrightarrow\quad b^{-1}<a^{-1}.
$$

Además, ambos inversos son negativos:

$$
a^{-1}<0,\qquad b^{-1}<0.
$$

Las hipótesis excluyen el cero y garantizan que los inversos existen. El enunciado es una comparación **dentro de la región negativa**, no entre factores de signos opuestos.

#### Demostración {#talg-prf-00126}
Sean $a,b<0$. Por la Definición 27.1.1 y la Notación 15.3.1 existen sus inversos bilaterales $a^{-1}$ y $b^{-1}$. La Proposición 27.6.1 prueba que

$$
a^{-1}<0,\qquad b^{-1}<0.
$$

**Paso preparatorio: establecer los opuestos y la identidad algebraica pertinente.** De $a<0$ y $b<0$, la Proposición 25.5.1 (inversión del orden estricto por el opuesto aditivo) da

$$
0<-a,\qquad 0<-b.
$$

Por tanto también existen $(-a)^{-1}$ y $(-b)^{-1}$. La demostración de la Proposición 27.6.1 justificó, multiplicando los candidatos en **ambos órdenes** y usando la unicidad de inversos, que

$$
(-a)^{-1}=-(a^{-1}),\qquad (-b)^{-1}=-(b^{-1}). \tag{1}
$$

Esta igualdad es un resultado algebraico previo; no se introduce por una manipulación informal de exponentes.

**Primera implicación.** Supongamos $a<b$. La inversión del orden por el opuesto aditivo da

$$
-b<-a.
$$

Ambos miembros son positivos, de manera que la equivalencia ya demostrada en la Proposición 27.8.1, aplicada a $u=-b$ y $v=-a$, produce

$$
(-a)^{-1}<(-b)^{-1}.
$$

Sustituyendo las dos identidades de (1), tenemos

$$
-(a^{-1})<-(b^{-1}).
$$

Una segunda aplicación de la Proposición 25.5.1, seguida de la involución del opuesto aditivo, invierte el orden:

$$
b^{-1}<a^{-1}.
$$

**Segunda implicación.** Supongamos ahora $b^{-1}<a^{-1}$. Al tomar opuestos, por la misma Proposición 25.5.1,

$$
-(a^{-1})<-(b^{-1}).
$$

Mediante las identidades (1), esto equivale a

$$
(-a)^{-1}<(-b)^{-1}.
$$

Los elementos $-b$ y $-a$ son positivos. Aplicamos **la implicación inversa de la Proposición 27.8.1** a $u=-b$ y $v=-a$; resulta

$$
-b<-a.
$$

Tomando opuestos una vez más y usando la involución aditiva obtenemos $a<b$. Quedan demostradas la equivalencia y, por el primer párrafo, la negatividad de ambos inversos. $\square$

> **Lectura guiada.** La prueba no multiplica desigualdades por números negativos ni considera conocido el signo de un inverso antes de establecerlo. Traslada la comparación al semieje positivo, donde hay una equivalencia previa, y vuelve a través de la identidad algebraica de (1). Las dos implicaciones son distintas y están escritas explícitamente.

> **Ejemplo racional, no premisa.** En $\mathbb Q$, $-5<-2<0$ y $-1/2<-1/5<0$. Se invierte el orden en el semieje negativo: el inverso de $-2$ es menor que el inverso de $-5$.

> **Caso frontera y contraejemplo.** El cero carece de inverso en un cuerpo no trivial. Si se cruza el cero, $-1<1$, pero $1^{-1}=1$ **no** es menor que $(-1)^{-1}=-1$; por tanto, la inversión no es antítona en todo $F\setminus\{0\}$. Las hipótesis de signo común no deben omitirse.

---

## 27.12. El signo de un producto por un inverso

La notación $ab^{-1}$ expresa la multiplicación en el cuerpo por **el inverso multiplicativo de $b$**; todavía no es necesario definir una operación nueva de división ni emplear una barra de fracción. La condición $b\ne0$ asegura que ese inverso exista. Los dos resultados de signos de §27.4 y §27.6 permiten identificar su signo antes de aplicar las reglas multiplicativas del capítulo 26.

```text
 b ≠ 0  ──► existe b⁻¹;  b·b⁻¹ = b⁻¹·b = 1
   │
   ├── b > 0 ──► b⁻¹ > 0  (§27.4)
   └── b < 0 ──► b⁻¹ < 0  (§27.6)

 a·b⁻¹ = 0 ──► (a·b⁻¹)·b = 0·b ──► a = 0
                                │
       a ≠ 0 ──► a·b⁻¹ ≠ 0 ─────┘

 signo(a), signo(b⁻¹) ──► signo(a·b⁻¹)
```

### Proposición 27.12.1 — Regla de signos de productos por inversos {#talg-pro-00083}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Para cualesquiera $a,b\in F$ con $b\ne0$, sea $p=a\cdot b^{-1}$. Entonces:

**I. Criterio exacto de nulidad:**

$$
p=0\quad\Longleftrightarrow\quad a=0.
$$

**II. Reglas de signos estrictos:**

| signo de $a$ | signo de $b$ | signo de $a\cdot b^{-1}$ |
|---|---|---|
| $0<a$ | $0<b$ | $0<p$ |
| $a<0$ | $b<0$ | $0<p$ |
| $0<a$ | $b<0$ | $p<0$ |
| $a<0$ | $0<b$ | $p<0$ |
| $a=0$ | $b\ne0$ | $p=0$ |

La misma tabla vale para $b^{-1}a$, puesto que el cuerpo es conmutativo y $a b^{-1}=b^{-1}a$. La hipótesis $b\ne0$ es indispensable: no se asigna ningún valor a $b^{-1}$ cuando $b=0$.

#### Demostración {#talg-prf-00127}
Fijemos $a,b\in F$ con $b\ne0$. Por la Definición 27.1.1 y la Notación 15.3.1 existe un inverso bilateral $b^{-1}$, con

$$
b\cdot b^{-1}=b^{-1}\cdot b=1. \tag{1}
$$

**1. Criterio de nulidad.** Si $a=0$, la absorción del cero (Proposición 14.3.1) da $p=0\cdot b^{-1}=0$. Recíprocamente, si $p=0$, multiplicamos **la igualdad** por $b$ a la derecha, sin efectuar ninguna operación sobre desigualdades:

$$
0=0\cdot b=(a\cdot b^{-1})\cdot b
 =a\cdot(b^{-1}\cdot b)=a\cdot1=a.
$$

Aquí sólo se emplean absorción, asociatividad, la segunda identidad de (1) y la unidad del cuerpo. Obtenemos

$$
a\cdot b^{-1}=0\ \Longleftrightarrow\ a=0. \tag{2}
$$

En particular, en cada uno de los cuatro casos de signos estrictos se cumple $a\ne0$ por la definición de $<$; por (2), tenemos

$$
p\ne0. \tag{3}
$$

Esto verifica la no nulidad **local del producto**, en vez de invocar tácitamente una ley global del producto nulo.

**2. Signo del inverso.** Si $0<b$, la Proposición 27.4.1 proporciona $0<b^{-1}$. Si $b<0$, la Proposición 27.6.1 proporciona $b^{-1}<0$. Ninguna regla posterior se aplica antes de establecer estos signos.

**3. Los dos casos de igual signo.** Si $0<a$ y $0<b$, ahora sabemos $0<a$, $0<b^{-1}$ y $p\ne0$. La Proposición 26.18.1 sobre productos de positivos, con su hipótesis local de no nulidad verificada en (3), da $0<p$.

Si $a<0$ y $b<0$, ahora $a<0$, $b^{-1}<0$ y $p\ne0$. El Corolario 26.28.1, aplicado al producto en ese orden y usando (3), da también $0<p$.

**4. Los dos casos de signos opuestos.** Si $0<a$ y $b<0$, se cumple $0<a$, $b^{-1}<0$ y $p\ne0$. El Corolario 26.24.1, en el orden de factores $a,b^{-1}$, proporciona $p<0$.

Si $a<0$ y $0<b$, entonces $a<0$, $0<b^{-1}$ y $p\ne0$. La variante del mismo Corolario 26.24.1 para el orden de signos negativo–positivo proporciona igualmente $p<0$.

**5. Producto por la izquierda.** La definición previa de cuerpo incluye conmutatividad multiplicativa. Por ello $b^{-1}a=a b^{-1}=p$; trasladamos a esta expresión todas las igualdades y desigualdades ya probadas. No se está atribuyendo este cambio de lateralidad a la definición de anillo ordenado, que también admite productos no conmutativos. Quedan probadas todas las afirmaciones. $\square$

> **Lectura guiada.** El orden de razonamiento importa: primero se comprueba que existe $b^{-1}$; después se prueba (2), que proporciona $p\ne0$ cuando $a\ne0$; luego se identifica el signo del inverso; por último se aplican las reglas estrictas de producto, cuyas hipótesis de no nulidad no deben ocultarse.

> **Ejemplos ilustrativos, no premisas.** En los racionales usuales, $2\cdot3^{-1}>0$, $(-2)\cdot(-3)^{-1}>0$, $2\cdot(-3)^{-1}<0$ y $(-2)\cdot3^{-1}<0$. Si $a=0$ y $b\ne0$, el producto siempre es cero.

> **Límite de alcance.** Esta proposición estudia signos de productos por inversos, no la antitonicidad de la inversión entre signos opuestos ni un procedimiento algorítmico para decidir el signo de un elemento arbitrario. No se ha definido todavía una nueva operación de cociente, ni se presupone completitud o propiedad arquimediana.

---

## 27.14. Multiplicar por un inverso fijo: preservar o invertir el orden

En §27.12 establecimos cómo el signo de un elemento determina el signo de su producto por un inverso. Para $c\ne0$, fijamos **un mismo multiplicador** $c^{-1}$ y comparamos las imágenes de dos elementos distintos, $a$ y $b$. Esta cuestión no es la antitonicidad de la función $x\mapsto x^{-1}$ de §§27.8 y 27.10: aquí **no varía el elemento invertido**.

La hipótesis $c\ne0$ precede a toda aparición de $c^{-1}$. Su signo se obtiene en §27.4 o §27.6, antes de invocar resultados sobre desigualdades multiplicativas. Para pasar de una comparación estricta a otra, no basta con multiplicar por un elemento de signo conocido en un anillo general: hay que excluir que se anule el producto de la diferencia por ese elemento.

```text
                  c ≠ 0  ──► existe u = c⁻¹; uc = cu = 1
                    │
           ┌────────┴────────┐
           │                 │
         c > 0             c < 0
           │                 │
         u > 0             u < 0
           │                 │
    a < b  ⇔  au < bu   a < b  ⇔  bu < au
    a < b  ⇔  ua < ub   a < b  ⇔  ub < ua
           └────────┬────────┘
                ambos lados;
           diferencia · u ≠ 0
```

### Proposición 27.14.1 — Compatibilidad del orden estricto con la multiplicación por inversos de signo conocido {#talg-pro-00084}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b,c\in F$. Supongamos, **antes de formar el inverso**, que $c\ne0$. Entonces se verifican las cuatro equivalencias siguientes, según el signo conocido de $c$.

**I. Factor positivo.** Si $0<c$, entonces

$$
a<b\quad\Longleftrightarrow\quad ac^{-1}<bc^{-1}, \tag{1}
$$

$$
a<b\quad\Longleftrightarrow\quad c^{-1}a<c^{-1}b. \tag{2}
$$

**II. Factor negativo.** Si $c<0$, entonces

$$
a<b\quad\Longleftrightarrow\quad bc^{-1}<ac^{-1}, \tag{3}
$$

$$
a<b\quad\Longleftrightarrow\quad c^{-1}b<c^{-1}a. \tag{4}
$$

Las fórmulas (1)–(4) distinguen la multiplicación por la derecha y por la izquierda. En un cuerpo sus expresiones correspondientes coinciden por conmutatividad, aunque los resultados del capítulo 26 se enunciaron y demostraron con ambas lateralidades independientes. No se define aquí una operación adicional de división.

#### Demostración {#talg-prf-00128}
**1. Existencia, signo y no nulidad del multiplicador.** Fijemos $c\ne0$. La Definición 27.1.1 y la Notación 15.3.1 proporcionan el inverso bilateral $u:=c^{-1}$, con

$$
cu=uc=1. \tag{5}
$$

Como $1\ne0$, necesariamente $u\ne0$: si $u=0$, la absorción del cero daría $cu=0$, en contradicción con (5). Si $0<c$, la Proposición 27.4.1 establece $0<u$; si $c<0$, la Proposición 27.6.1 establece $u<0$. **No** se infiere el signo de $u$ sin haber establecido primero cuál de estas dos hipótesis rige.

**2. Exclusión explícita del producto nulo.** Para las implicaciones que parten de $a<b$, definamos la diferencia aditiva

$$
d:=b+(-a).
$$

La compatibilidad estricta con las traslaciones (Proposición 25.5.1) proporciona $0<d$, luego $d\ne0$. Aplicando la Proposición 27.12.1 al numerador $d$ y al elemento no nulo $c$, su criterio exacto de nulidad da

$$
du=dc^{-1}\ne0. \tag{6}
$$

En este punto, y sólo porque la estructura es un **cuerpo conmutativo**, también

$$
ud=du\ne0. \tag{7}
$$

Así se satisfacen **por separado** las dos condiciones locales de no nulidad requeridas para obtener desigualdades estrictas por la derecha y por la izquierda. Una justificación alternativa, no necesaria para (6)–(7), es el Teorema 22.3.1: todo cuerpo es un dominio íntegro, por lo que el producto de $d\ne0$ por $u\ne0$ no se anula en ningún orden.

**3. Caso positivo: ambas implicaciones y lateralidades.** Supongamos $0<c$. Por el paso 1, $0<u$. Si $a<b$, el criterio local **derecho** de la Proposición 26.30.1, con factor $u$ y condición $du\ne0$ de (6), proporciona $au<bu$. El criterio **izquierdo** de la misma proposición, ahora con $ud\ne0$ de (7), da $ua<ub$. Reemplazando $u$ por $c^{-1}$ obtenemos los sentidos directos de (1) y (2).

Recíprocamente, de $au<bu$ y $0<u$, la **reflexión derecha** de la Proposición 26.30.1 deduce $a<b$; de $ua<ub$ y $0<u$, su **reflexión izquierda** deduce igualmente $a<b$. Estas reflexiones son válidas sin postular de nuevo la no nulidad de productos. Quedan justificadas individualmente las dos direcciones de (1) y de (2).

**4. Caso negativo: ambas implicaciones y lateralidades.** Supongamos $c<0$. El paso 1 establece $u<0$. Si $a<b$, el criterio local **derecho** de la Proposición 26.32.1 con $du\ne0$ proporciona $bu<au$; su criterio **izquierdo**, con $ud\ne0$, proporciona $ub<ua$. Son los sentidos directos de (3) y (4).

A la inversa, $bu<au$ y $u<0$ implican $a<b$ por la reflexión derecha de la Proposición 26.32.1. Si $ub<ua$, se aplica la reflexión izquierda de la misma proposición y se obtiene $a<b$. La inversión del orden se debe al signo **negativo del factor fijo**, no a la antitonicidad de la función inversa. Con ello se han probado (3) y (4).

**5. Comprobación inversa mediante la multiplicación por $c$.** Podemos verificar adicionalmente los cuatro sentidos recíprocos deshaciendo la multiplicación por $u$. El Teorema 22.3.1 asegura que, en $F$, el producto de dos elementos no nulos es no nulo: se cumple, por tanto, la condición global del apartado 4 de las Proposiciones 26.30.1 y 26.32.1. Si $c>0$, aplicamos la conservación estricta por el factor $c$ a $au<bu$ por la derecha, o a $ua<ub$ por la izquierda; por (5) y asociatividad obtenemos respectivamente

$$
(au)c=a<(bu)c=b,\qquad c(ua)=a<c(ub)=b.
$$

Si $c<0$, aplicamos la inversión estricta por el factor $c$ a $bu<au$ o a $ub<ua$, respetando la lateralidad:

$$
(au)c=a<(bu)c=b,\qquad c(ua)=a<c(ub)=b.
$$

Esta comprobación concuerda con las reflexiones de los pasos 3 y 4; **multiplicar una desigualdad** requiere las hipótesis de orden y de no anulación que acabamos de señalar, mientras que las identidades $(au)c=a=c(ua)$ son puramente algebraicas. La igualdad $au=ua$ permite identificar las dos lateralidades en $F$ por conmutatividad, sin atribuir esa propiedad a los anillos ordenados generales. $\square$

> **Lectura guiada.** El recorrido directo tiene cuatro estaciones: inverso existente, signo del inverso conocido, diferencia $d=b-a$ estrictamente positiva, productos $du$ y $ud$ no nulos. Sólo entonces se aplican los criterios estrictos de 26.30.1 o 26.32.1. El recorrido inverso utiliza las reflexiones ya demostradas; el paso 5 comprueba además que multiplicar por $c$ recupera el orden inicial, con su signo y las condiciones de no anulación explícitos.

> **Ejemplo de orientación (no deductivo).** En $\mathbb Q$ con su orden usual, fijemos $a=2$, $b=5$. Con $c=3>0$ obtenemos $2\cdot3^{-1}<5\cdot3^{-1}$ y $3^{-1}\cdot2<3^{-1}\cdot5$. Con $c=-3<0$ obtenemos $5\cdot(-3)^{-1}<2\cdot(-3)^{-1}$ y $(-3)^{-1}\cdot5<(-3)^{-1}\cdot2$: el sentido se invierte.

> **Caso frontera y no-ejemplo.** Con $a=b$ los productos de ambos miembros son iguales y ninguna desigualdad estricta aparece, sea cual sea el signo de $c$. Si $c=0$, el inverso $c^{-1}$ **no existe**, por lo que (1)–(4) ni siquiera se formulan. En un anillo totalmente ordenado con divisores de cero, el mero signo del multiplicador no garantiza estrictitud: el ejemplo de los números duales del §26.30 muestra productos de una diferencia positiva que se anulan. La hipótesis de cuerpo elimina esa obstrucción; no hemos presupuesto completitud, arquimedianidad ni un algoritmo para decidir comparaciones.

---

## 27.16. Orden no estricto al multiplicar por un inverso de signo conocido

La conservación estricta de la Proposición 27.14.1 no debe trasladarse sin más a la desigualdad no estricta: esta última **admite la igualdad**. Tampoco necesitamos reconstruir el caso general de reflexión de los anillos totalmente ordenados. Para un factor $c\ne0$, después de multiplicar por su inverso fijo podemos recuperar cada elemento mediante la multiplicación por $c$: $cc^{-1}=c^{-1}c=1$.

**Pregunta de activación.** Si $a=b$, ¿qué ocurre al multiplicar ambos miembros por $c^{-1}$? Los dos productos siguen siendo iguales. Por ello la afirmación correcta emplea $\le$ tanto en la hipótesis como en la conclusión.

**Estrategia.** Excluir primero $c=0$, identificar el signo de $u:=c^{-1}$ mediante las Proposiciones 27.4.1 y 27.6.1, y aplicar las reglas no estrictas de los anillos ordenados: Proposición 26.6.1 para factores no negativos y Proposición 26.8.1 para factores no positivos. Para cada recíproca multiplicar por $c$ en **el mismo lado**, de manera que la identidad inversa suprima el factor. Este argumento no exige ausencia general de productos nulos ni una ley de cancelación obtenida clásicamente.

### Proposición 27.16.1 — Compatibilidad del orden no estricto con la multiplicación por inversos de signo conocido {#talg-pro-00085}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b,c\in F$. Supongamos **antes de utilizar la notación de inverso** que $c\ne0$. Entonces:

**I. Si $0<c$,** se verifican las equivalencias

$$
a\le b\quad\Longleftrightarrow\quad ac^{-1}\le bc^{-1}, \tag{1}
$$

$$
a\le b\quad\Longleftrightarrow\quad c^{-1}a\le c^{-1}b. \tag{2}
$$

**II. Si $c<0$,** se verifican las equivalencias

$$
a\le b\quad\Longleftrightarrow\quad bc^{-1}\le ac^{-1}, \tag{3}
$$

$$
a\le b\quad\Longleftrightarrow\quad c^{-1}b\le c^{-1}a. \tag{4}
$$

Se mantienen las dos lateralidades por separado. La conmutatividad del cuerpo permitirá finalmente identificarlas, pero no se usará para deducir una de la otra.

#### Demostración {#talg-prf-00129}
**1. Inverso bilateral y signos establecidos antes de multiplicar.** Como $c\ne0$, la definición de cuerpo y la Notación 15.3.1 permiten fijar un inverso $u:=c^{-1}\in F$ que satisface

$$
cu=uc=1. \tag{5}
$$

Si $0<c$, la Proposición 27.4.1 proporciona $0<u$; por tanto $0\le u$ y $0\le c$. Si $c<0$, la Proposición 27.6.1 proporciona $u<0$; por tanto $u\le0$ y $c\le0$. Estas conclusiones utilizan la relación entre orden estricto y no estricto de la interfaz de órdenes; **no** presuponen que los signos sean algorítmicamente decidibles.

**2. Factor positivo: implicaciones directas.** Supongamos $0<c$ y $a\le b$. Como $0\le u$, aplicamos la Proposición 26.6.1 por la derecha y por la izquierda, respectivamente:

$$
au\le bu,\qquad ua\le ub. \tag{6}
$$

Al sustituir $u=c^{-1}$, obtenemos las implicaciones directas de (1) y (2).

**3. Factor positivo: implicaciones recíprocas.** Supongamos $au\le bu$. Puesto que $0\le c$, la misma Proposición 26.6.1 permite multiplicar **por la derecha**:

$$
(au)c\le(bu)c.
$$

La asociatividad y $uc=1$ de (5) reducen esta desigualdad a $a\le b$. Si, en cambio, suponemos $ua\le ub$, multiplicamos **por la izquierda** con $c\ge0$:

$$
c(ua)\le c(ub).
$$

Por asociatividad y $cu=1$, obtenemos nuevamente $a\le b$. Quedan demostradas ambas direcciones de (1) y (2), sin recurrir a conmutatividad ni a un teorema de cancelación.

**4. Factor negativo: implicaciones directas.** Supongamos $c<0$ y $a\le b$. Como $u\le0$, la Proposición 26.8.1 invierte el orden al multiplicar por el factor no positivo, con ambas lateralidades:

$$
bu\le au,\qquad ub\le ua. \tag{7}
$$

Sustituir $u=c^{-1}$ proporciona las implicaciones directas de (3) y (4).

**5. Factor negativo: implicaciones recíprocas.** Si $bu\le au$, multiplicamos **por la derecha** por $c\le0$ mediante la Proposición 26.8.1, que vuelve a invertir el sentido:

$$
(au)c\le(bu)c.
$$

Gracias a $uc=1$, queda $a\le b$. Si $ub\le ua$, multiplicamos **por la izquierda** con el mismo factor negativo:

$$
c(ua)\le c(ub),
$$

que se simplifica a $a\le b$ gracias a $cu=1$. Así se han establecido las cuatro equivalencias. Sólo ahora, por la conmutatividad incluida en la definición de cuerpo, puede añadirse $au=ua$ y $bu=ub$: esto identifica las formulaciones laterales sin sustituir sus demostraciones. $\square$

> **Lectura guiada.** En el recorrido directo, el signo del inverso determina si se emplea conservación (26.6.1) o inversión (26.8.1). En el recorrido recíproco se usa el signo de $c$, **no** el del inverso, y se multiplica en el mismo lado del producto inicial. El efecto de multiplicar dos veces por factores inversos es la identidad, tanto si las dos aplicaciones conservan el orden como si las dos lo invierten.

> **Ejemplo orientador, no deductivo.** En $\mathbb Q$ con el orden usual, si $a=1$, $b=3$ y $c=2$, (1) da $1/2\le3/2$. Si $c=-2$, (3) da $-3/2\le-1/2$. Los dos ejemplos también satisfacen las correspondientes formulaciones izquierdas.

> **Caso frontera.** Si $a=b$, todos los productos correspondientes coinciden y las cuatro desigualdades no estrictas siguen siendo verdaderas; precisamente por eso la versión estricta no bastaría para cubrir este caso. Si $c=0$, no existe $c^{-1}$ en un cuerpo y las fórmulas (1)–(4) no se formulan. No aparece aquí una nueva operación de división ni se afirma antitonicidad de la función variable $x\mapsto x^{-1}$.

---

## 27.18. División: convertir la multiplicación por un inverso en una función de dominio explícito

Hemos estudiado los productos $ab^{-1}$ y $b^{-1}a$ sin introducir una operación adicional. Ahora podemos fijar la escritura usual de cociente, pero **sólo después de determinar el conjunto de pares para el cual existe el inverso del denominador**.

**Pregunta de activación.** ¿Por qué $0/b$ tiene sentido cuando $b\ne0$, mientras que $a/0$ no está definido, incluso si $a=0$? La primera expresión necesita el inverso de $b$; la segunda exigiría el inverso del cero, inexistente en un cuerpo no trivial.

### Definición 27.18.1 — División en un cuerpo: dominio de denominadores no nulos y notación {#talg-def-00062}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Por la Proposición 22.2.1, el conjunto de unidades de su anillo subyacente coincide con el conjunto de elementos no nulos:

$$
F^\times=\{b\in F:b\ne0\}=F\setminus\{0\}. \tag{1}
$$

Llamaremos **división del cuerpo $F$** a la función

$$
\operatorname{div}_F:F\times F^\times\longrightarrow F,\qquad
\operatorname{div}_F(\langle a,b\rangle):=a\cdot b^{-1}. \tag{2}
$$

Para $a,b\in F$ **con $b\ne0$**, adoptamos la notación

$$
\boxed{\displaystyle \frac{a}{b}:=\operatorname{div}_F(\langle a,b\rangle)=a\cdot b^{-1}.} \tag{3}
$$

La expresión $a/b$ designa así un elemento de $F$. La aplicación es **total sobre el dominio restringido** $F\times F^\times$ y no está definida sobre $F\times F$ entero; si $b=0$, el par $\langle a,b\rangle$ no pertenece a su dominio. El numerador puede ser cualquier elemento de $F$, incluido $0$.

**Verificación definicional del tipado.** Por (1), cada denominador admisible es una unidad, y la Notación 15.3.1 le asigna un único inverso multiplicativo $b^{-1}\in F$. El cierre de la multiplicación de un cuerpo garantiza $a\cdot b^{-1}\in F$. Por tanto, la regla (2) asigna un único valor del codominio a cada par de su dominio y determina una función conforme a la interfaz fundacional de pares y funciones. No se eligen inversos de una familia de conjuntos: la unicidad ya está demostrada, y **Choice no interviene**.

> **No confundir dos construcciones.** La Notación 24.3.2 ya emplea $a/b$ para la *clase de equivalencia* $[a,b]_D\in\operatorname{Frac}(D)$ de un par fraccionario de un dominio íntegro $D$. En (3), en cambio, $a,b\in F$ y $a/b$ es el producto $ab^{-1}$ calculado **dentro de un cuerpo ya dado**. El tipo de los operandos y la construcción indicada por el contexto distinguen ambos usos. No se identifica literalmente una clase de pares con un elemento de $D$, ni se presupone aquí un teorema de compatibilidad con la inmersión $\iota_D$.

> **Ejemplo orientador, no premisa.** En $\mathbb Q$, $6/3=6\cdot3^{-1}=2$ y $0/3=0$; en cambio $6/0$ y $0/0$ no son valores de $\operatorname{div}_{\mathbb Q}$. Que un numerador sea cero no subsana un denominador inadmisible.

> **Lectura guiada.** Primero se verifica el tipo $\langle a,b\rangle\in F\times F^\times$; luego se toma el único inverso multiplicativo de $b$; finalmente se aplica la multiplicación del cuerpo. Las equivalencias de orden de §§27.14 y 27.16 pueden reescribirse con la barra sólo después de esta definición, sin generar nuevos teoremas.

---

## 27.20. Las identidades de división son teoremas sobre inversos

La barra ya tiene un significado preciso: $a/b=ab^{-1}$, pero escribirla no demuestra por sí solo ninguna ley. Antes de operar con cocientes, probaremos las igualdades que enlazan la división con la multiplicación y delimitaremos su criterio de nulidad.

**Pregunta de activación.** ¿Por qué la igualdad $xb=a$ determina un único valor de $x$ cuando $b\ne0$, mientras que no podemos usar el mismo argumento cuando $b=0$? En el primer caso existe $b^{-1}$ y podemos recuperar $x$ multiplicando la igualdad por ese inverso; en el segundo caso no está disponible tal operación.

### Proposición 27.20.1 — Identidades básicas de la división y criterio de nulidad {#talg-pro-00086}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Para cualesquiera $a,b\in F$ con **$b\ne0$**, los cocientes siguientes están definidos y satisfacen:

$$
\boxed{\frac a1=a,} \tag{1}
$$

$$
\boxed{\frac0b=0,} \tag{2}
$$

$$
\boxed{\frac bb=1,} \tag{3}
$$

$$
\boxed{\left(\frac ab\right)b=a.} \tag{4}
$$

El **criterio exacto de nulidad** es

$$
\boxed{\frac ab=0\quad\Longleftrightarrow\quad a=0.} \tag{5}
$$

Más aún, el cociente es la **única solución** de la ecuación multiplicativa $xb=a$: para todo $x\in F$,

$$
\boxed{xb=a\quad\Longleftrightarrow\quad x=\frac ab.} \tag{6}
$$

En (1), la expresión $a/1$ está permitida porque el cuerpo es no trivial y $1\ne0$. En (2)–(6), la hipótesis $b\ne0$ debe permanecer explícita; ninguna identidad asigna significado a $a/0$ o $0/0$.

#### Demostración {#talg-prf-00130}
**1. Preparación: todo cociente escrito está definido.** El cuerpo es no trivial por la Definición 27.1.1, de modo que $1\ne0$. La Proposición 22.2.1 identifica $F^\times=F\setminus\{0\}$: así, tanto $1$ como el elemento concreto $b\ne0$ son denominadores admisibles para la función de la Definición 27.18.1. Por la notación de inversos multiplicativos, existen $1^{-1},b^{-1}\in F$ y se cumple

$$
1\cdot1^{-1}=1,\qquad b^{-1}b=bb^{-1}=1. \tag{7}
$$

**2. División por la unidad.** Como $1$ es el neutro multiplicativo, $1\cdot1^{-1}=1^{-1}$. Combinado con (7), esto da $1^{-1}=1$; por la definición de cociente,

$$
\frac a1=a\cdot1^{-1}=a\cdot1=a.
$$

**3. Numerador cero.** La Proposición 14.3.1 (absorción del cero) y la definición de división dan

$$
\frac0b=0\cdot b^{-1}=0.
$$

**4. División de un elemento por sí mismo.** Por $b\ne0$, (7) permite escribir

$$
\frac bb=b\cdot b^{-1}=1.
$$

**5. Recuperación del numerador.** Aplicando sucesivamente la definición, la asociatividad, la identidad inversa bilateral de (7) y la unidad multiplicativa, obtenemos

$$
\left(\frac ab\right)b
=(ab^{-1})b
=a(b^{-1}b)
=a\cdot1=a. \tag{8}
$$

**6. Criterio de nulidad.** Si $a=0$, (2) implica $a/b=0$. Si $a/b=0$, por (8) y por la absorción del cero,

$$
a=\left(\frac ab\right)b=0\cdot b=0.
$$

Esto prueba (5). La equivalencia ya había sido establecida para el producto $ab^{-1}$ en la Proposición 27.12.1; aquí queda reformulada mediante el cociente **ahora definido**, y la verificación anterior hace explícita la recuperación del numerador. No se necesita inferir la nulidad de un factor mediante una regla global de divisores de cero.

**7. Existencia y unicidad como solución de $xb=a$.** La identidad (8) proporciona la solución $x=a/b$. Recíprocamente, si un $x\in F$ satisface $xb=a$, multiplicamos **a la derecha por $b^{-1}$** y asociamos:

$$
x=x\cdot1=x(bb^{-1})=(xb)b^{-1}=ab^{-1}=\frac ab.
$$

Por tanto, cualquier solución coincide con $a/b$, lo que demuestra (6). La conclusión se ha obtenido exclusivamente mediante inversos de denominadores no nulos y las leyes algebraicas de cuerpo. $\square$

> **Lectura guiada.** El orden correcto es verificar el denominador, desplegar $a/b=ab^{-1}$, asociar productos y aplicar $bb^{-1}=b^{-1}b=1$. La igualdad (4) reconstruye el numerador, mientras que (6) caracteriza la división como resolución **única** de una ecuación multiplicativa.

> **Ejemplo de comprobación, no premisa.** En los racionales usuales, $6/3=2$ porque $2\cdot3=6$; $0/3=0$ y $3/3=1$. Nada en este ejemplo define $6/0$ ni $0/0$.

> **Distinción de tipos.** Los cocientes de esta proposición son elementos de $F$; los símbolos de fracción del capítulo 24 designan clases en $\operatorname{Frac}(D)$. Las identidades (1)–(6) no afirman igualdad literal entre ambas construcciones.

---

## 27.22. Los cocientes heredan el signo y el orden de la multiplicación por inversos

Ya se definió el cociente $a/b$ para $b\ne0$ en la Definición 27.18.1. Las reglas de signos de §27.12 y las equivalencias de orden de §§27.14 y 27.16 se formularon deliberadamente para productos por inversos, antes de introducir la barra. Ahora podemos trasladar esos resultados al lenguaje de la división **sin redefinir una operación** ni volver a probar sus lemas estrictos.

**Pregunta de activación.** Si comparamos $a/b$ con $c/b$, ¿qué cambia al reemplazar un denominador positivo por uno negativo? La división es multiplicación por $b^{-1}$: el primer signo conserva el orden del numerador y el segundo lo invierte. En ambas comparaciones el denominador debe ser el mismo y no nulo.

### Proposición 27.22.1 — Reglas de signos y comparación de cocientes con denominador de signo conocido {#talg-pro-00087}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b,c\in F$, con **$b\ne0$**. Entonces todas las fracciones siguientes son elementos definidos de $F$ y se cumplen las afirmaciones siguientes.

**I. Signo del cociente.** Las cinco combinaciones controladas son:

| signo de $a$ | signo de $b$ | conclusión |
|---|---|---|
| $0<a$ | $0<b$ | $0<a/b$ |
| $a<0$ | $b<0$ | $0<a/b$ |
| $0<a$ | $b<0$ | $a/b<0$ |
| $a<0$ | $0<b$ | $a/b<0$ |
| $a=0$ | $b\ne0$ | $a/b=0$ |

En particular, $a/b=0\Longleftrightarrow a=0$. Esta última equivalencia es **reutilización** de la Proposición 27.20.1, no un teorema nuevo sobre productos nulos.

**II. Comparación estricta, denominador fijo.** Si $0<b$, entonces

$$
\boxed{a<c\quad\Longleftrightarrow\quad\frac ab<\frac cb.} \tag{1}
$$

Si $b<0$, entonces

$$
\boxed{a<c\quad\Longleftrightarrow\quad\frac cb<\frac ab.} \tag{2}
$$

**III. Comparación no estricta y caso de igualdad.** Si $0<b$, entonces

$$
\boxed{a\le c\quad\Longleftrightarrow\quad\frac ab\le\frac cb.} \tag{3}
$$

Si $b<0$, entonces

$$
\boxed{a\le c\quad\Longleftrightarrow\quad\frac cb\le\frac ab.} \tag{4}
$$

En cualquiera de los dos casos de signo —y, de hecho, para todo $b\ne0$—,

$$
\boxed{\frac ab=\frac cb\quad\Longleftrightarrow\quad a=c.} \tag{5}
$$

No se afirma ninguna comparación con **denominadores distintos**: expresiones como $a/b$ y $c/d$, con $b\ne d$, requieren otro enunciado.

#### Demostración {#talg-prf-00131}
**1. Control del dominio y traducción.** Como $b\ne0$, la Definición 27.18.1 garantiza que $a/b,c/b\in F$. Para los tres elementos $a,b,c$ se tiene, por la misma definición,

$$
\frac ab=ab^{-1},\qquad \frac cb=cb^{-1}. \tag{6}
$$

No se necesita ningún inverso de $a$ o $c$. Todas las sustituciones siguientes son igualdades de elementos de $F$.

**2. Signos.** La Proposición 27.12.1 establece los cuatro signos estrictos de $ab^{-1}$ bajo las correspondientes hipótesis y además prueba $ab^{-1}=0\iff a=0$ con $b\ne0$. Sustituir (6) transforma exactamente cada una de esas conclusiones en la tabla de I. Alternativamente, la fila $a=0$ y el criterio de nulidad se siguen de la Proposición 27.20.1. Así no se deduce el signo a partir de una comparación informal ni se omite la no nulidad del producto requerida por los resultados de §26.

**3. Desigualdades estrictas.** Supongamos primero $0<b$. La Proposición 27.14.1, aplicada al multiplicador fijo $b^{-1}$, afirma en ambos sentidos

$$
a<c\quad\Longleftrightarrow\quad ab^{-1}<cb^{-1}.
$$

Sustituir (6) demuestra (1). Si, en cambio, $b<0$, la variante negativa de esa misma proposición afirma

$$
a<c\quad\Longleftrightarrow\quad cb^{-1}<ab^{-1},
$$

que por (6) es (2). El trabajo previo de §27.14 ya certificó los signos de los inversos y excluyó los productos nulos necesarios para la estricta desigualdad; no se presume aquí ningún nuevo criterio de cancelación.

**4. Desigualdades no estrictas.** La Proposición 27.16.1 proporciona, respectivamente,

$$
0<b\quad\Longrightarrow\quad\bigl(a\le c\iff ab^{-1}\le cb^{-1}\bigr),
$$

$$
b<0\quad\Longrightarrow\quad\bigl(a\le c\iff cb^{-1}\le ab^{-1}\bigr).
$$

La sustitución de (6) demuestra (3) y (4). Estas fórmulas incluyen $a=c$; reemplazar $\le$ por $<$ habría excluido indebidamente ese caso.

**5. Igualdad.** Si $a=c$, la definición de cociente da $a/b=c/b$ por sustitución. Recíprocamente, si $a/b=c/b$, multiplicamos esta **igualdad**, no una desigualdad, por $b$; la identidad $(x/b)b=x$ de la Proposición 27.20.1 da

$$
a=\left(\frac ab\right)b=\left(\frac cb\right)b=c.
$$

La deducción sólo exige $b\ne0$; no necesita elegir entre $b>0$ y $b<0$. Quedan demostradas las afirmaciones. $\square$

> **Lectura guiada.** Primero verificar $b\ne0$; después traducir a $ab^{-1}$; luego aplicar el resultado previo cuyo cuantificador y sentido corresponden al signo conocido de $b$. El paso de estricta a no estricta no debe improvisarse: se invoca separadamente la Proposición 27.16.1. La igualdad final se recupera multiplicando por el mismo denominador.

> **Ejemplo orientador, no premisa.** En los racionales usuales, $1<3$ produce $1/2<3/2$ cuando el denominador es positivo y $3/(-2)<1/(-2)$ cuando es negativo. Los dos cocientes son valores del mismo cuerpo, no clases fraccionarias identificadas con el numerador.

> **Caso frontera.** Si $a=c$, las dos comparaciones estrictas de II son falsas, mientras que las dos comparaciones no estrictas de III son verdaderas. Si $b=0$, ni (1)–(5) están formuladas: no se define $a/0$. Con denominadores distintos no basta esta proposición para comparar.

---

## 27.24. Suma y producto de cocientes: justificar primero el denominador

Los cocientes $a/b$ y $c/d$ ya son elementos de $F$ cuando $b$ y $d$ son no nulos. Queremos calcular su suma y su producto mediante una sola división. La operación no puede comenzar escribiendo una nueva barra: **hay que probar que el denominador propuesto $bd$ no se anula**. Esto procede de que todo cuerpo es un dominio íntegro (Teorema 22.3.1), no de una suposición sobre el signo de $b$ o de $d$.

**Pregunta de activación.** ¿Cómo reconocer el valor de un cociente sin transformar explícitamente un producto de inversos? La Proposición 27.20.1 caracteriza $t/e$ como la única solución de $ze=t$ cuando $e\ne0$. Bastará multiplicar la suma y el producto buscados por $bd$ y recuperar sus numeradores.

### Proposición 27.24.1 — Suma y producto de cocientes con denominadores no nulos {#talg-pro-00088}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado. Para cualesquiera $a,b,c,d\in F$ tales que **$b\ne0$ y $d\ne0$**, se tiene $bd\ne0$ y, por consiguiente, todos los cocientes de las siguientes identidades están definidos:

$$
\boxed{\frac ab+\frac cd=\frac{ad+bc}{bd}.} \tag{1}
$$

$$
\boxed{\frac ab\cdot\frac cd=\frac{ac}{bd}.} \tag{2}
$$

Ni $a$ ni $c$ deben ser no nulos; tampoco se exige que $b$ o $d$ tengan signo conocido.

#### Demostración {#talg-prf-00132}
**1. Control de dominios.** Por $b\ne0$ y $d\ne0$, la Definición 27.18.1 asegura que $a/b,c/d\in F$. Como todo cuerpo es un dominio íntegro (Teorema 22.3.1), el producto de dos elementos no nulos no puede ser cero; por tanto,

$$
bd\ne0. \tag{3}
$$

La misma definición permite ahora formar $(ad+bc)/(bd)$ y $(ac)/(bd)$, ambos elementos de $F$. Esta comprobación precede a cualquier uso de la Proposición 27.20.1 con denominador $bd$.

**2. Recuperación de los numeradores iniciales.** Pongamos $x=a/b$ e $y=c/d$. La identidad (4) de la Proposición 27.20.1, aplicada por separado a los dos denominadores originales, proporciona

$$
xb=a,\qquad yd=c. \tag{4}
$$

**3. Suma.** Por distributividad del anillo (Definición 14.1.1), asociatividad y conmutatividad de la multiplicación del cuerpo (Definición 27.1.1),

$$
\begin{aligned}
(x+y)(bd)
 &=x(bd)+y(bd)\\
 &=(xb)d+(yd)b\\
 &=ad+cb\\
 &=ad+bc.
\end{aligned} \tag{5}
$$

Puesto que $bd\ne0$, el criterio de solución única de la Proposición 27.20.1 se aplica a $z(bd)=ad+bc$ y concluye

$$
x+y=\frac{ad+bc}{bd}.
$$

Sustituyendo las definiciones de $x$ e $y$ se obtiene (1).

**4. Producto.** Nuevamente por asociatividad y conmutatividad multiplicativas,

$$
(xy)(bd)=(xb)(yd)=ac. \tag{6}
$$

La misma caracterización única de §27.20, ahora aplicada a $z(bd)=ac$, da

$$
xy=\frac{ac}{bd},
$$

que es (2). Queda demostrada la proposición. $\square$

> **Lectura guiada.** La prueba separa dos obligaciones distintas: garantizar que cada cociente está definido y demostrar su valor. El paso decisivo no es «cancelar denominadores» informalmente, sino probar una ecuación multiplicativa cuyo coeficiente $bd$ es no nulo y utilizar la unicidad de su solución.

> **Ejemplo, no premisa.** En los racionales usuales, $1/2+1/3=(1\cdot3+2\cdot1)/(2\cdot3)=5/6$, mientras $(1/2)(1/3)=1/6$. Las fórmulas probadas no dependen de este ejemplo ni del orden de $F$: son leyes algebraicas válidas en cualquier cuerpo, aquí formuladas dentro del capítulo de cuerpos ordenados.

> **Casos frontera y alcance.** Si $a=0$ o $c=0$, ambas fórmulas siguen bien definidas. Si $b=0$ o $d=0$, el enunciado deja de ser aplicable; no asigna valor a una división por cero. No se ha probado todavía la fórmula de un cociente de cocientes ni una regla de comparación entre denominadores distintos. En (1) y (2), las barras representan valores de $F$ conforme a la Definición 27.18.1, no clases del cuerpo de fracciones del capítulo 24. No se usa Choice, completitud, arquimedianidad ni formalización Lean.

---

## 27.26. Opuestos y división sucesiva: condiciones de existencia

La suma y el producto de cocientes se obtuvieron en la Proposición 27.24.1. Quedan dos operaciones que no deben confundirse: tomar el **opuesto aditivo** de un cociente y **dividir por otro cociente**. La primera sólo requiere un denominador no nulo; la segunda necesita, además, que el cociente usado como divisor no se anule. Por la Proposición 27.20.1, para $d\ne0$ tenemos $c/d\ne0$ exactamente cuando $c\ne0$.

**Pregunta de activación.** Aunque $c/d$ esté definido porque $d\ne0$, ¿podemos usarlo siempre como denominador? No: si $c=0$, entonces $c/d=0$. La hipótesis adicional $c\ne0$ es indispensable.

### Proposición 27.26.1 — Opuestos y cocientes sucesivos con denominadores no nulos {#talg-pro-00089}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b,c,d\in F$.

**(I) Opuestos.** Si $b\ne0$, entonces $-b\ne0$ y

$$
\boxed{-\!\left(\frac ab\right)=\frac{-a}{b}=\frac{a}{-b}.} \tag{1}
$$

**(II) Cocientes sucesivos.** Si $b\ne0$, $c\ne0$ y $d\ne0$, se encuentran definidos $a/b$, $c/d$, $d/c$, $ad/(bc)$ y el cociente exterior $(a/b)/(c/d)$. Además,

$$
\boxed{\frac{\,a/b\,}{\,c/d\,}=\frac{ad}{bc}.} \tag{2}
$$

En ninguno de los dos apartados se exige $a\ne0$ ni se fija el signo de $b,c,d$.

#### Demostración {#talg-prf-00133}
**1. Dominios y opuestos.** Supongamos $b\ne0$. Si $-b=0$, la involución del opuesto aditivo en el anillo (Definición 14.1.1) daría $b=-(-b)=-0=0$, contradicción; por tanto $-b\ne0$. La Definición 27.18.1 permite formar los tres cocientes involucrados en (1).

Pongamos $x=a/b$. La identidad $(a/b)b=a$ de la Proposición 27.20.1 y las reglas de signos del anillo (Proposición 14.4.1) dan

$$
(-x)b=-(xb)=-a. \tag{3}
$$

Como $b\ne0$, el criterio de solución única $zb=-a\iff z=(-a)/b$ de la Proposición 27.20.1 muestra que $-x=(-a)/b$. Por otra parte,

$$
(-x)(-b)=xb=a. \tag{4}
$$

Aquí $-b\ne0$, de modo que la misma caracterización, aplicada ahora a $z(-b)=a$, proporciona $-x=a/(-b)$. Sustituyendo $x=a/b$ obtenemos (1).

**2. Dominios de la división sucesiva.** Supongamos además $c\ne0$ y $d\ne0$. Por la Definición 27.18.1 existen $y=c/d$ y $r=d/c$. La equivalencia de nulidad de la Proposición 27.20.1, aplicada con $d\ne0$, implica

$$
y=\frac cd\ne0. \tag{5}
$$

Todo cuerpo es un dominio íntegro (Teorema 22.3.1), por lo cual $bc\ne0$ y $cd\ne0$. Así, tanto $ad/(bc)$ como $dc/(cd)$ están definidos. La propia no nulidad (5) autoriza formar $(a/b)/(c/d)$.

**3. El inverso del divisor como cociente.** La regla de producto de la Proposición 27.24.1, con denominadores $c,d\ne0$, da

$$
ry=\frac dc\cdot\frac cd=\frac{dc}{cd}=\frac{cd}{cd}=1. \tag{6}
$$

El penúltimo paso usa la conmutatividad del cuerpo (Definición 27.1.1); el último, la identidad $e/e=1$ de la Proposición 27.20.1, aplicada a $e=cd\ne0$.

**4. Identificación del cociente exterior.** Sea $x=a/b$. Aplicamos de nuevo la Proposición 27.24.1, ahora a $x\cdot r$, y obtenemos

$$
xr=\frac ab\cdot\frac dc=\frac{ad}{bc}. \tag{7}
$$

Por asociatividad, (6) y la identidad multiplicativa,

$$
(xr)y=x(ry)=x\cdot1=x. \tag{8}
$$

Como $y=c/d\ne0$, el criterio de solución única de la Proposición 27.20.1 caracteriza $x/y$ como el único $z\in F$ que cumple $zy=x$. La igualdad (8) prueba que ese elemento es $xr$; (7) concluye

$$
\frac{\,a/b\,}{\,c/d\,}=\frac{ad}{bc}.
$$

Quedan demostradas ambas afirmaciones. $\square$

> **Lectura guiada.** En (I) no se «traslada» informalmente el signo menos: se multiplica cada candidato por su denominador y se usa la unicidad del cociente. En (II), primero se prueba $c/d\ne0$; después se verifica que $(d/c)(c/d)=1$ y sólo entonces se identifica la división exterior con una multiplicación. Son pasos algebraicos, sin suponer signos de los denominadores.

> **Ejemplo ilustrativo, no premisa.** En los racionales, $-(2/3)=(-2)/3=2/(-3)$; además, $(2/3)/(4/5)=(2\cdot5)/(3\cdot4)=5/6$. El ejemplo no sustituye el control de dominios ni la prueba general.

> **Casos frontera.** $a=0$ es admisible en ambos apartados. Si $b=0$, no existe el primer cociente; si $d=0$, no existe $c/d$; y si $c=0$ con $d\ne0$, el divisor exterior es exactamente $0$ y la expresión $(a/b)/(c/d)$ no está definida. Tampoco se han comparado cocientes de denominadores distintos. Las barras designan elementos de $F$, no clases de $\operatorname{Frac}(D)$.

---

## 27.28. Comparar cocientes: los productos cruzados y el signo del factor

Las Proposiciones 27.22.1 y 27.24.1 permiten comparar cocientes con denominador común y operar con cocientes de denominadores distintos. Pero una comparación de $a/b$ con $c/d$ no se decide simplemente «multiplicando en cruz»: hay que conocer el signo de **$bd$**, pues multiplicar por un factor negativo invierte el orden. La ventaja de trabajar en un cuerpo es que $b,d\ne0$ implican $bd\ne0$.

**Pregunta de activación.** Si $b<0<d$, ¿debemos conservar el sentido de $a/b<c/d$ al comparar $ad$ con $bc$? No: en ese caso el producto $bd$ es negativo y las desigualdades se invierten. En lugar de confiar en una regla mnemotécnica, vamos a recuperar ambos numeradores por multiplicación y aplicar resultados de orden ya demostrados.

### Proposición 27.28.1 — Comparación de cocientes por productos cruzados con denominadores de signo conocido {#talg-pro-00090}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b,c,d\in F$ con **$b\ne0$ y $d\ne0$**. Entonces $bd\ne0$ y ambos cocientes $a/b,c/d\in F$ están definidos. Se verifican las siguientes equivalencias.

**(I) Producto positivo.** Si $0<bd$, entonces

$$
\boxed{\frac ab<\frac cd\ \Longleftrightarrow\ ad<bc,} \tag{1}
$$

$$
\boxed{\frac ab\le\frac cd\ \Longleftrightarrow\ ad\le bc.} \tag{2}
$$

**(II) Producto negativo.** Si $bd<0$, entonces

$$
\boxed{\frac ab<\frac cd\ \Longleftrightarrow\ bc<ad,} \tag{3}
$$

$$
\boxed{\frac ab\le\frac cd\ \Longleftrightarrow\ bc\le ad.} \tag{4}
$$

**(III) Igualdad, sin hipótesis de signo.** Para todo $b,d\ne0$,

$$
\boxed{\frac ab=\frac cd\ \Longleftrightarrow\ ad=bc.} \tag{5}
$$

La condición de signo se impone al **producto $bd$**, no a los numeradores. No se exige $a\ne0$ ni $c\ne0$; el criterio (5) tampoco exige conocer qué signo tiene $bd$.

#### Demostración {#talg-prf-00134}
**1. Definición y no nulidad.** Fijemos $a,b,c,d\in F$ con $b,d\ne0$. Por la Definición 27.18.1 existen los elementos

$$
x:=\frac ab,\qquad y:=\frac cd.
$$

Como todo cuerpo es un dominio íntegro (Teorema 22.3.1), el producto

$$
t:=bd\ne0. \tag{6}
$$

La definición de cuerpo incluye la estructura de anillo conmutativo (Definiciones 14.1.1 y 27.1.1). Por recuperación de los numeradores (Proposición 27.20.1), $xb=a$ y $yd=c$. Asociamos y reordenamos los factores para obtener, sin dividir por nada nuevo,

$$
xt=(xb)d=ad,\qquad yt=(yd)b=cb=bc. \tag{7}
$$

Estas dos identidades justifican **toda** la comparación cruzada posterior: los productos $ad$ y $bc$ no son recetas independientes, sino $x$ e $y$ multiplicados por el **mismo factor no nulo** $t$.

**Regularidad derecha del factor.** Si $zt=0$, tanto $z$ como $0$ resuelven $wt=0$. Como $t\ne0$, la unicidad de la solución en la Proposición 27.20.1 da $z=0$. Por tanto $t$ satisface la hipótesis de regularidad derecha de la Proposición 26.34.1. Usaremos esa variante, cuya cancelación no requiere eliminación de doble negación.

**2. Caso $0<t$.** La Proposición 26.30.1 establece que, en un anillo totalmente ordenado sin productos nulos de factores no nulos, multiplicar por un factor positivo preserva y refleja el orden estricto. La hipótesis global de esa proposición se satisface por el Teorema 22.3.1. Por tanto,

$$
x<y\quad\Longleftrightarrow\quad xt<yt
\quad\stackrel{(7)}{\Longleftrightarrow}\quad ad<bc.
$$

Ésta es (1). Para el orden no estricto, la Proposición 26.34.1 —aplicada al mismo anillo, al mismo factor positivo y a la regularidad derecha que acabamos de demostrar— da

$$
x\le y\quad\Longleftrightarrow\quad xt\le yt
\quad\stackrel{(7)}{\Longleftrightarrow}\quad ad\le bc,
$$

que demuestra (2).

**3. Caso $t<0$.** La Proposición 26.32.1 proporciona, bajo la misma condición global de no anulación, la equivalencia estricta con sentido invertido:

$$
x<y\quad\Longleftrightarrow\quad yt<xt
\quad\stackrel{(7)}{\Longleftrightarrow}\quad bc<ad.
$$

La variante negativa de la Proposición 26.34.1, bajo esa misma regularidad derecha, proporciona la equivalencia no estricta

$$
x\le y\quad\Longleftrightarrow\quad yt\le xt
\quad\stackrel{(7)}{\Longleftrightarrow}\quad bc\le ad.
$$

Éstas son (3) y (4). En ningún paso se ha multiplicado una desigualdad por un factor de signo desconocido.

**4. Igualdad sin distinguir signos.** Si $x=y$, la sustitución en (7) produce $ad=bc$. En sentido recíproco, supongamos $ad=bc$. Entonces (7) implica $xt=yt=ad$. Puesto que $t\ne0$, la caracterización única de la solución de $zt=ad$ en la Proposición 27.20.1 obliga a que $x=y$. Sustituyendo sus definiciones se obtiene (5), sin realizar ninguna comparación de signos. $\square$

> **Lectura guiada.** Compruébese primero $b\ne0$, $d\ne0$ y $bd\ne0$. Después, las igualdades $\bigl(a/b\bigr)(bd)=ad$ y $\bigl(c/d\bigr)(bd)=bc$ reducen el problema a comparar $x$ e $y$ tras multiplicarlos por un único factor $bd$. Las Proposiciones 26.30.1, 26.32.1 y 26.34.1 ya contienen las dos direcciones de las equivalencias; la ausencia de divisores de cero evita perder la estrictitud.

> **Dos ejemplos, no premisas.** Con denominadores positivos, $1/2<2/3$ se lee $1\cdot3<2\cdot2$. Con denominadores de signo contrario, $1/(-2)<1/3$ se lee $(-2)\cdot1<1\cdot3$, es decir, $bc<ad$: la comparación cruzada invierte su dirección. En ambos ejemplos el denominador exterior común es el producto $bd$.

> **Errores y casos frontera.** No se puede afirmar $a/b<c/d\iff ad<bc$ sin controlar $bd$: si $bd<0$, la fórmula correcta es (3). Si $b=0$ o $d=0$, las expresiones iniciales no están definidas; por el contrario, $a=0$ o $c=0$ es admisible. La igualdad (5) no requiere signo, pero sí exige ambos denominadores no nulos. Los cocientes designan elementos del cuerpo $F$, no clases de $\operatorname{Frac}(D)$ del capítulo 24.

---

## 27.30. Amplificar y simplificar un cociente: el factor común debe ser no nulo

La regla escolar de «multiplicar numerador y denominador por el mismo número» sólo es correcta bajo una condición que aquí no puede quedar implícita: el factor añadido al denominador debe ser **no nulo**. Si se multiplicara por $0$, el nuevo denominador sería $0$ y la expresión dejaría de pertenecer al dominio de la división definido en §27.18.

**Pregunta de activación.** Si $a/b$ ya está definido porque $b\ne0$, ¿por qué no podemos escribir también $a/b=(a\cdot0)/(b\cdot0)$? Porque la segunda barra exigiría dividir por $b\cdot0=0$. La igualdad intuitiva «$0/0$» no es una fracción permitida en el cuerpo.

### Proposición 27.30.1 — Amplificación y simplificación de cocientes por factores no nulos {#talg-pro-00091}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b,k\in F$ con

$$
b\ne0,\qquad k\ne0.
$$

Entonces $bk\ne0$, ambos cocientes siguientes están definidos y

$$
\boxed{\frac ab=\frac{ak}{bk}.} \tag{1}
$$

Leída de izquierda a derecha, (1) es la **amplificación** del cociente por el factor no nulo $k$; leída de derecha a izquierda, es la **simplificación** de un factor común no nulo. No se exige $a\ne0$ ni se impone signo alguno a $b$ o a $k$.

#### Demostración {#talg-prf-00135}
**1. Comprobar el dominio antes de formar el cociente amplificado.** Por hipótesis, $b\ne0$ y $k\ne0$. Todo cuerpo es un dominio íntegro (Teorema 22.3.1), de modo que el producto de dos elementos no nulos no puede ser cero. Por tanto,

$$
bk\ne0. \tag{2}
$$

La Definición 27.18.1 garantiza así que tanto $a/b$ como $(ak)/(bk)$ están definidos.

**2. Recuperar el numerador del cociente original.** Pongamos

$$
x:=\frac ab.
$$

La identidad fundamental de la Proposición 27.20.1 da

$$
xb=a. \tag{3}
$$

**3. Multiplicar una igualdad, no una desigualdad.** Multiplicamos ambos miembros de (3) por $k$ a la derecha:

$$
(xb)k=ak. \tag{4}
$$

Por asociatividad de la multiplicación del anillo (Definición 14.1.1),

$$
x(bk)=ak. \tag{5}
$$

No se necesita conocer el signo de $k$: estamos preservando una **igualdad**, no el sentido de una desigualdad.

**4. Usar la caracterización única del cociente.** Como $bk\ne0$ por (2), la Proposición 27.20.1 aplicada ahora al denominador $bk$ afirma que la ecuación

$$
z(bk)=ak
$$

tiene una única solución, precisamente

$$
z=\frac{ak}{bk}.
$$

Pero (5) muestra que $x$ es una solución de esa ecuación. Por unicidad,

$$
x=\frac{ak}{bk}.
$$

Sustituyendo $x=a/b$ obtenemos (1). $\square$

> **Lectura guiada.** La demostración no comienza «cancelando $k$». Primero prueba que $bk$ es un denominador legítimo; después transforma la identidad ya conocida $(a/b)b=a$ en $\bigl(a/b\bigr)(bk)=ak$; finalmente utiliza la unicidad de la solución de $z(bk)=ak$. La simplificación es, por tanto, la lectura inversa de una igualdad previamente demostrada.

> **Ejemplo ilustrativo, no premisa.** En los racionales usuales, $2/3=(2\cdot5)/(3\cdot5)=10/15$. El papel matemático de $5$ no es que sea positivo, sino que sea no nulo. El mismo resultado vale con $k=-5$.

> **Error típico y casos frontera.** El paso $a/b=(ak)/(bk)$ es inválido si $k=0$, porque el denominador derecho se vuelve $0$. En cambio, $a=0$ no causa dificultad: si $b,k\ne0$, entonces $0/b=0/(bk)=0$. Tampoco se requiere que $b$ y $k$ tengan el mismo signo.

---

## 27.32. Normalizar el signo del denominador

Un cociente puede estar perfectamente definido y, sin embargo, aparecer con denominador negativo. Para las comparaciones posteriores resulta conveniente saber que ese signo puede trasladarse simultáneamente al numerador y al denominador, de modo que el denominador quede positivo. Esta operación no crea una «fracción reducida» ni una representación canónica: sólo normaliza el **signo** del denominador.

**Pregunta de activación.** Si únicamente sabemos que $b\ne0$, ¿podemos decidir sin más que $b>0$ o que $b<0$? Matemáticamente sí obtenemos una disyunción a partir de la totalidad del orden y la no nulidad de $b$; eso no proporciona por sí mismo un algoritmo que determine cuál de las dos alternativas ocurre.

### Proposición 27.32.1 — Normalización de cocientes a denominador positivo {#talg-pro-00092}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b\in F$ con $b\ne0$. Entonces exactamente una de las dos situaciones siguientes ocurre:

1. $0<b$, y el cociente $a/b$ ya tiene denominador positivo;
2. $b<0$, en cuyo caso
   $$
   0<-b
   $$
   y
   $$
   \boxed{\frac ab=\frac{-a}{-b}.} \tag{1}
   $$

En particular, existen $n,d\in F$ tales que

$$
0<d
\qquad\text{y}\qquad
\boxed{\frac ab=\frac nd.} \tag{2}
$$

El enunciado (2) es existencial: no afirma que el par $(n,d)$ sea único ni que el orden de $F$ disponga de un procedimiento algorítmico para escoger entre los dos casos.

#### Demostración {#talg-prf-00136}
**1. El cociente inicial está definido.** La hipótesis $b\ne0$ coloca a $b$ en el dominio permitido por la Definición 27.18.1. Por tanto,

$$
\frac ab\in F
$$

está definido antes de efectuar cualquier transformación de signos.

**2. Obtener los dos casos desde la totalidad, sin postular tricotomía.** Como el orden de $F$ es total, aplicado a $0$ y $b$ proporciona la disyunción

$$
0\le b\quad\lor\quad b\le0. \tag{3}
$$

Supongamos primero $0\le b$. Si $0=b$, la simetría de la igualdad daría $b=0$, contradicción. Luego $0\ne b$ y, por la definición de orden estricto de la Interfaz 25.1.1,

$$
0<b. \tag{4}
$$

Supongamos ahora $b\le0$. Junto con la hipótesis $b\ne0$, la misma definición de orden estricto da directamente

$$
b<0. \tag{5}
$$

Así, (3) se ha refinado a la disyunción

$$
0<b\quad\lor\quad b<0. \tag{6}
$$

No hemos importado una proposición general de tricotomía: sólo usamos totalidad y la no nulidad concreta del denominador.

**3. Normalizar el caso negativo.** Supongamos $b<0$. La Proposición 25.5.1, aplicada al grupo aditivo subyacente, invierte el orden estricto al tomar opuestos:

$$
-0<-b.
$$

En todo grupo aditivo, el opuesto del neutro es el propio neutro; por tanto,

$$
0<-b. \tag{7}
$$

En particular, $-b\ne0$, de modo que el cociente con denominador $-b$ está definido.

Para justificar la igualdad de cocientes no moveremos signos de manera informal. Aplicamos la Proposición 27.26.1 al numerador $-a$ y al denominador $b\ne0$. Su identidad de opuestos afirma

$$
-\!\left(\frac{-a}{b}\right)
=
\frac{-(-a)}{b}
=
\frac{-a}{-b}. \tag{8}
$$

La involución del opuesto aditivo convierte el término central en $a/b$, y por tanto (8) da exactamente

$$
\frac ab=\frac{-a}{-b}. \tag{9}
$$

Combinando (7) y (9), el denominador normalizado es positivo.

**4. Construir los testigos de (2).** Si ocurre el primer caso de (6), tomamos

$$
n:=a,\qquad d:=b.
$$

Entonces $0<d$ por (4) y $a/b=n/d$ por sustitución.

Si ocurre el segundo caso, tomamos

$$
n:=-a,\qquad d:=-b.
$$

Entonces $0<d$ por (7) y $a/b=n/d$ por (9). En ambos casos existen los testigos requeridos.

**5. Exclusión mutua de los dos signos.** Si simultáneamente $0<b$ y $b<0$, la definición del orden estricto proporciona $0\le b$ y $b\le0$. Por antisimetría,

$$
0=b,
$$

contradiciendo $b\ne0$. Por ello las dos alternativas son mutuamente excluyentes. $\square$

> **Lectura guiada.** La prueba separa tres tareas que suelen comprimirse en una regla escolar: primero obtiene el signo del denominador desde totalidad más no nulidad; después demuestra que cambiar simultáneamente ambos signos conserva el cociente; sólo al final elige los testigos con denominador positivo. Ningún paso presupone una función de signo computable.

> **Ejemplo ilustrativo, no premisa.** En los racionales usuales, $2/(-3)=(-2)/3$. El segundo denominador es positivo, pero el valor del cociente no cambió. Si el denominador ya era positivo, como en $2/3$, no hay nada que modificar.

> **Qué significa aquí «normalizar».** La normalización afecta únicamente al signo del denominador. No se ha definido máximo común divisor, coprimalidad, «fracción irreducible» ni una representación canónica del elemento de $F$. La Proposición 27.30.1 muestra, de hecho, que un mismo cociente admite amplificaciones por factores no nulos.

> **Casos frontera y alcance.** El numerador puede ser $0$; entonces también $-a=0$ y la normalización funciona sin excepción. El denominador $0$ queda excluido desde el inicio. No se usa Choice, una tricotomía importada, decidibilidad del orden, completitud, arquimedianidad, algoritmos ni formalización Lean.

---

## 27.34. Comparar después de normalizar: un único sentido de cruce

La Proposición 27.32.1 permite representar cada cociente con denominador positivo. Una vez hecho esto, la bifurcación de §27.28 desaparece: el producto de dos denominadores positivos vuelve a ser positivo, de modo que la comparación cruzada conserva siempre el sentido del orden.

**Pregunta de activación.** Si dos cocientes admiten muchas representaciones con denominador positivo, ¿depende la comparación del par de representaciones elegido? No. Cada representación positiva satisface por separado el mismo criterio de productos cruzados, porque la Proposición 27.28.1 se aplica a cualquiera de ellas.

### Corolario 27.34.1 — Reducción de comparaciones de cocientes a denominadores positivos {#talg-cor-00020}
Sea $\langle F,+,\cdot,\le\rangle$ un cuerpo ordenado y sean $a,b,c,d\in F$ con

$$
b\ne0,\qquad d\ne0.
$$

Entonces existen $n_1,e_1,n_2,e_2\in F$ tales que

$$
0<e_1,\qquad 0<e_2, \tag{1}
$$

$$
\frac ab=\frac{n_1}{e_1},
\qquad
\frac cd=\frac{n_2}{e_2}. \tag{2}
$$

Además, **para cualesquiera** $n_1,e_1,n_2,e_2$ que satisfagan (1) y (2), se verifican simultáneamente

$$
\boxed{
\frac ab<\frac cd
\quad\Longleftrightarrow\quad
n_1e_2<n_2e_1,
} \tag{3}
$$

$$
\boxed{
\frac ab\le\frac cd
\quad\Longleftrightarrow\quad
n_1e_2\le n_2e_1,
} \tag{4}
$$

y

$$
\boxed{
\frac ab=\frac cd
\quad\Longleftrightarrow\quad
n_1e_2=n_2e_1.
} \tag{5}
$$

En particular, si los denominadores originales ya son positivos, $0<b$ y $0<d$, podemos tomar

$$
(n_1,e_1,n_2,e_2)=(a,b,c,d),
$$

y (3)–(5) se reducen a las reglas usuales de productos cruzados sin distinguir un caso adicional de signo negativo.

#### Demostración {#talg-prf-00137}
**1. Existencia de representaciones con denominador positivo.** Las hipótesis $b\ne0$ y $d\ne0$ permiten formar los cocientes iniciales por la Definición 27.18.1. Aplicamos la Proposición 27.32.1 primero a $a/b$ y luego a $c/d$. Obtenemos testigos $n_1,e_1,n_2,e_2\in F$ tales que

$$
0<e_1,\qquad
\frac ab=\frac{n_1}{e_1}, \tag{6}
$$

$$
0<e_2,\qquad
\frac cd=\frac{n_2}{e_2}. \tag{7}
$$

Estas son exactamente (1) y (2). Se han usado dos testigos locales proporcionados por dos aplicaciones concretas de una proposición existencial; no se ha escogido simultáneamente una representación para una familia arbitraria de cocientes y, por tanto, no interviene Choice.

**2. Fijar representaciones positivas arbitrarias.** Para demostrar que el criterio no depende de los testigos particulares obtenidos en el paso 1, fijemos ahora cualesquiera $n_1,e_1,n_2,e_2$ que satisfagan (1) y (2). De $0<e_1$ y $0<e_2$, la definición de orden estricto implica

$$
e_1\ne0,\qquad e_2\ne0. \tag{8}
$$

Como todo cuerpo es un dominio íntegro (Teorema 22.3.1), (8) da

$$
e_1e_2\ne0. \tag{9}
$$

Los dos factores son positivos. La Proposición 26.18.1, aplicada con la no nulidad local (9), concluye

$$
0<e_1e_2. \tag{10}
$$

Éste es el punto que elimina la bifurcación de signo de §27.28: el factor común usado para la comparación cruzada es ahora necesariamente positivo.

**3. Comparación estricta.** La Proposición 27.28.1, aplicada a los cocientes $n_1/e_1$ y $n_2/e_2$ y al caso positivo (10), da

$$
\frac{n_1}{e_1}<\frac{n_2}{e_2}
\quad\Longleftrightarrow\quad
n_1e_2<e_1n_2. \tag{11}
$$

La estructura de cuerpo es conmutativa, de modo que $e_1n_2=n_2e_1$. Sustituyendo esta igualdad en (11),

$$
\frac{n_1}{e_1}<\frac{n_2}{e_2}
\quad\Longleftrightarrow\quad
n_1e_2<n_2e_1. \tag{12}
$$

Por (2), la sustitución de iguales en la relación $<$ transforma (12) exactamente en (3).

**4. Comparación no estricta.** La misma Proposición 27.28.1, bajo la misma positividad (10), proporciona

$$
\frac{n_1}{e_1}\le\frac{n_2}{e_2}
\quad\Longleftrightarrow\quad
n_1e_2\le e_1n_2.
$$

Conmutatividad y las igualdades (2) producen inmediatamente

$$
\frac ab\le\frac cd
\quad\Longleftrightarrow\quad
n_1e_2\le n_2e_1,
$$

que es (4).

**5. Igualdad.** El apartado de igualdad de la Proposición 27.28.1 no necesita hipótesis sobre el signo del producto de denominadores; basta $e_1,e_2\ne0$, ya probado en (8). Por tanto,

$$
\frac{n_1}{e_1}=\frac{n_2}{e_2}
\quad\Longleftrightarrow\quad
n_1e_2=e_1n_2
\quad\Longleftrightarrow\quad
n_1e_2=n_2e_1.
$$

Sustituyendo nuevamente (2) obtenemos (5).

**6. Caso de denominadores ya positivos.** Si $0<b$ y $0<d$, entonces la elección local

$$
n_1=a,\quad e_1=b,\quad n_2=c,\quad e_2=d
$$

satisface (1) y (2) por reflexividad de la igualdad. Las fórmulas (3)–(5) se especializan así a los productos cruzados $ad$ y $cb=bc$. Queda demostrado el corolario. $\square$

> **Lectura guiada.** Normalizar no significa escoger una fracción irreducible. Sólo se necesita que ambos denominadores sean positivos. Después, su producto es positivo y la Proposición 27.28.1 entra siempre por su rama positiva. La prueba separa deliberadamente la **existencia** de representaciones positivas de la **independencia del criterio respecto de cuál representación positiva se use**.

> **Ejemplo ilustrativo, no premisa.** En $\mathbb Q$, comparar $2/(-3)$ con $1/4$ puede reemplazarse por comparar $(-2)/3$ con $1/4$. Como $3,4>0$, basta comparar $(-2)\cdot4$ con $1\cdot3$. El cambio de representación absorbe el signo del denominador antes de cruzar productos.

> **Error típico.** La normalización no autoriza a comparar los numeradores solos: incluso con denominadores positivos, $n_1/e_1<n_2/e_2$ depende de los productos $n_1e_2$ y $n_2e_1$. Tampoco convierte la representación positiva en única; la Proposición 27.30.1 sigue permitiendo amplificaciones por cualquier factor positivo no nulo.

---

## 27.36. Síntesis deductiva del capítulo

El problema planteado en §27.0 era introducir la inversión y la división en un cuerpo totalmente ordenado **sin perder el control del signo, del dominio de definición ni del sentido de las desigualdades**. La cadena cerrada del capítulo puede resumirse así:

```text
cuerpo + anillo totalmente ordenado
        │
        ├── cuerpo ordenado (§27.1)
        │   ├── signo del inverso: conserva el signo (§§27.4–27.6)
        │   └── inversión: antítona dentro de cada región de signo (§§27.8–27.10)
        │
        ├── producto por inversos (§§27.12–27.16)
        │   ├── nulidad exacta y regla de signos
        │   ├── orden estricto: conserva o invierte según el signo
        │   └── orden no estricto: mismas equivalencias
        │
        └── división interna del cuerpo (§§27.18–27.34)
            ├── dominio F × F^× y cociente a/b = ab⁻¹
            ├── identidades, nulidad y solución única de xb = a
            ├── signos y comparación con denominador fijo
            ├── suma, producto, opuestos y cocientes sucesivos
            ├── productos cruzados con signo controlado
            ├── amplificación por factores no nulos
            ├── normalización existencial a denominador positivo
            └── comparación uniforme tras normalización positiva
```

La separación entre **inversión** y **división** es esencial. Antes de §27.18, $b^{-1}$ es el inverso multiplicativo de un elemento no nulo; desde §27.18, $a/b$ es una abreviatura tipada de $ab^{-1}$ dentro del mismo cuerpo $F$. Esta barra no identifica el elemento de $F$ con las clases fraccionarias construidas en el capítulo 24.

El control del signo también se mantiene separado del control de nulidad. La positividad o negatividad de un factor determina el sentido de una desigualdad; la inexistencia de productos nulos en un cuerpo, heredada de su condición de dominio íntegro, impide que una desigualdad estricta colapse a igualdad. En los resultados de cocientes se verifican los denominadores no nulos **antes** de formar cada expresión.

La normalización final no construye una forma canónica. Todo cociente admite una representación con denominador positivo, pero esa representación puede amplificarse por factores positivos no nulos. Lo que sí queda demostrado es que **cualquier** par de representaciones con denominadores positivos conduce al mismo criterio de comparación por productos cruzados.

Tampoco se ha demostrado una antitonicidad global de $x\mapsto x^{-1}$ sobre $F\setminus\{0\}$: el resultado es válido separadamente entre positivos y entre negativos y falla al cruzar cero. Del mismo modo, la totalidad del orden se emplea como propiedad lógica de comparabilidad, no como algoritmo de decisión.

Finalmente, el capítulo no usa completitud, supremos, topología ni propiedad arquimediana. Esas nociones quedan fuera de este capítulo. No se utiliza el axioma de elección. La única dependencia clásica relevante en §27.28 es la ya incorporada en la Proposición 26.34.1 para obtener cancelación desde la condición (NZ).

---

---

[← **Capítulo 26 — Anillos ordenados**](tratado-de-algebra-capitulo-26-anillos-ordenados.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
