---
title: 'Tratado moderno de Álgebra — Capítulo 24: Cuerpo de fracciones de un dominio íntegro'
description: Capítulo del Tratado moderno de Álgebra dedicado a cuerpo de fracciones de un dominio íntegro, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0049
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-16'
date-modified: '2026-09-26'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
prerequisites:
- MA-BCH-0048
related:
- MA-BOK-0007
- MA-BCH-0048
- MA-BCH-0050
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 24 — Cuerpo de fracciones de un dominio íntegro

## 24.0. El problema: hacer divisibles los elementos no nulos

Sea

$$
\mathcal D=\langle D,+,\cdot\rangle
$$

un dominio íntegro. En $D$ podemos sumar, restar y multiplicar, y los factores no nulos se pueden cancelar. Pero nada garantiza que un elemento no nulo $b$ posea inverso multiplicativo dentro de $D$.

El objetivo de este capítulo es construir, **a partir de $D$ y sin elegir representantes privilegiados**, un cuerpo en el que todo cociente formal $a/b$ con $b\neq0$ exista y en el que $D$ aparezca fielmente mediante una inmersión canónica.

La idea tiene tres capas:

```text
pares (numerador, denominador no nulo)
        ↓
identificación de representaciones equivalentes
        ↓
clases sobre las que suma y producto están bien definidos
```

La dificultad no está en adivinar las fórmulas habituales de las fracciones. La dificultad es demostrar que esas fórmulas dependen sólo de la **fracción representada** y no del par elegido para representarla.

> **Profundidad pedagógica — P3.** Este bloque combina representación, cociente, buena definición y una frontera lógica real. La lectura debe distinguir en todo momento el par $(a,b)$, la clase que representa, la igualdad entre clases y la eventual computabilidad de esa igualdad.

### Interfaz 24.0.1 — Aritmética entera y racional para los ejemplos {#talg-imp-00005}

Los ejemplos numéricos de este capítulo y de los capítulos 26–27 utilizan las estructuras construidas en los [capítulos 2 — Enteros](tratado-de-analisis-capitulo-2-los-numeros-enteros.md) y [3 — Racionales](tratado-de-analisis-capitulo-3-los-numeros-racionales.md) del *Tratado de análisis*. Importamos explícitamente los siguientes resultados cerrados:

| Estructura o dato | Resultados de Análisis importados |
|---|---|
| Enteros: forma normal con signo y dominio íntegro | Teoremas 2.8.1 y 2.8.4 |
| Orden total entero y compatibilidad con suma y producto | Teorema 2.9.3, Proposición 2.9.4 y Corolario 2.9.6 (tricotomía) |
| Numerales naturales dentro de los enteros | Proposiciones 2.7.2 y 2.9.5 |
| Producto de enteros estrictamente positivos | Lema 3.1.4 |
| Racionales como cuerpo | Teorema 3.6.8 |
| Orden total racional y compatibilidad con las operaciones | Teorema 3.7.5 y Proposición 3.7.8 |
| Incrustación de los enteros en los racionales | Proposiciones 3.5.2 y 3.7.9 |
| División racional y criterio de igualdad de fracciones | Definición 3.6.6 y Proposición 3.2.6 |

Los enteros y racionales son aquí conjuntos con operaciones ya construidas; los numerales se transportan mediante las incrustaciones indicadas. La barra racional tiene el significado fijado en Análisis. En particular, para enteros $a,b$ con $b\ne0$, la clase racional $a/b$ coincide con el cociente de sus imágenes en el cuerpo racional: al multiplicar esa clase por la imagen de $b$ se recupera la imagen de $a$, y la invertibilidad de $b$ determina el cociente de manera única.

Las leyes importadas satisfacen las definiciones algebraicas de los capítulos 14, 21 y 22; sus leyes de orden proporcionan los modelos numéricos usados posteriormente en la Parte V. El cuerpo abstracto que construiremos desde un dominio arbitrario sigue dependiendo sólo de las hipótesis declaradas sobre ese dominio. No identificamos literalmente su conjunto de clases con el conjunto de racionales de otra construcción.

**Alcance fundacional.** Esta importación se apoya en una cadena cerrada de fundamentos, naturales, enteros y racionales del *Tratado de análisis*. Incorpora el uso de Infinito de la construcción de los naturales y se acepta bajo ZF y la lógica declarada en las fuentes, sin Choice. No importa densidad, propiedad arquimediana, reales ni completitud. Sus dependencias no vuelven al Tratado de álgebra. El carácter ilustrativo de un ejemplo no exime de declarar esta procedencia.


> **Modelo aritmético familiar — sólo motivación.** En la aritmética ordinaria, $(1,2)$ y $(2,4)$ no son pares iguales, pero representan la misma fracción porque $1\cdot4=2\cdot2$. La construcción abstracta conserva exactamente esa idea y elimina todo lo que depende de propiedades particulares de los enteros.

### Frontera fundacional del capítulo

la auditoría fundacional del capítulo fija dos capas que mantendremos visibles:

1. la construcción principal trabaja en ZF + lógica clásica y no usa Choice;
2. el único puente clásico sustantivo del núcleo de la construcción aparece al demostrar la transitividad de la relación fraccionaria desde la definición negativa actual de dominio íntegro.

Cuando ese paso pueda formularse con una hipótesis positiva de cancelación, registraremos también esa variante constructivamente compatible. No afirmaremos que $b\neq0$ sea decidible, que la igualdad de fracciones sea decidible ni que las operaciones construidas sean algoritmos.

---

## 24.1. Pares fraccionarios

### Definición 24.1.1 — Pares fraccionarios sobre un dominio íntegro {#talg-def-00051}

Sea $\mathcal D=\langle D,+,\cdot\rangle$ un dominio íntegro. Definimos el conjunto de **pares fraccionarios** de $D$ por

$$
\boxed{
P_D
:=
\{\langle a,b\rangle\in D\times D:b\neq0\}.
}
$$

El primer componente se interpreta como numerador y el segundo como denominador.

La condición $b\neq0$ significa literalmente

$$
\neg(b=0).
$$

No se presupone que exista un procedimiento que decida, dado $b\in D$, si $b=0$ o $b\neq0$.

La existencia de $P_D$ como conjunto se obtiene en ZF por Separación a partir de $D\times D$. No hay aquí ninguna elección de representantes ni uso de Choice.

> **Lectura de la definición.** Un par fraccionario todavía **no es una fracción**. Dos pares distintos podrán representar posteriormente el mismo elemento del cuerpo de fracciones.

---

### Proposición 24.1.2 — El conjunto de pares fraccionarios está habitado {#talg-pro-00055}

Para todo dominio íntegro $\mathcal D$,

$$
\exists p\in P_D.
$$

Más precisamente,

$$
\boxed{\langle0,1\rangle\in P_D.}
$$

#### Demostración {#talg-prf-00090}

Por la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047), todo dominio íntegro es no trivial. Por tanto,

$$
0\neq1,
$$

y, por simetría de la desigualdad,

$$
1\neq0.
$$

Como $0,1\in D$, la definición de $P_D$ da

$$
\langle0,1\rangle\in P_D.
$$

Así $P_D$ no sólo es no vacío: disponemos de un testigo explícito de que está habitado. $\square$

---

## 24.2. Cuándo dos pares representan la misma fracción

### Definición 24.2.1 — Relación fraccionaria {#talg-def-00052}

Sobre $P_D$ definimos la relación $\sim_D$ mediante

$$
\boxed{
\langle a,b\rangle\sim_D\langle c,d\rangle
\quad\Longleftrightarrow\quad
ad=bc.
}
$$

Formalmente,

$$
\sim_D
=
\left\{
\left\langle\langle a,b\rangle,\langle c,d\rangle\right\rangle
\in P_D\times P_D
:
ad=bc
\right\}.
$$

La ecuación cruzada no afirma que los pares sean iguales. Afirma que serán identificados al formar el cociente.

> **Prueba de estrés.** Si usáramos igualdad literal de pares, $(a,b)$ y $(ac,bc)$ serían distintos cuando $c\neq1$, aun cuando expresan la misma razón siempre que los denominadores permanezcan no nulos. La relación cruzada está diseñada precisamente para olvidar esa redundancia representacional.

---

### Lema 24.2.2 — Transitividad bajo cancelación positiva {#talg-lem-00006}

Supongamos que, además de las leyes de dominio conmutativo necesarias para la manipulación algebraica, disponemos de la siguiente forma **positiva** de cancelación:

$$
\boxed{
r\neq0\ \land\ rx=ry\Longrightarrow x=y.}
$$

Entonces $\sim_D$ es transitiva.

#### Demostración {#talg-prf-00091}

Sean

$$
\langle a,b\rangle,
\langle c,d\rangle,
\langle e,f\rangle
\in P_D
$$

y supongamos

$$
\langle a,b\rangle\sim_D\langle c,d\rangle,
\qquad
\langle c,d\rangle\sim_D\langle e,f\rangle.
$$

Por definición,

$$
ad=bc,
\qquad
cf=de.
$$

Multiplicando la primera igualdad por $f$ y usando la segunda,

$$
adf=bcf=b(cf)=b(de)=bde.
$$

Por asociatividad y conmutatividad,

$$
d(af)=d(be).
$$

Como $\langle c,d\rangle\in P_D$, tenemos $d\neq0$. La hipótesis positiva de cancelación permite concluir

$$
af=be.
$$

Por la [Definición 24.2.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-def-00052),

$$
\langle a,b\rangle\sim_D\langle e,f\rangle.
$$

Así $\sim_D$ es transitiva. $\square$

> **Lectura crítica.** Toda la prueba anterior es transformación algebraica de datos excepto el último paso. El punto lógico exacto es: de $d(af)=d(be)$ y $d\neq0$ queremos obtener $af=be$.

---

### Proposición 24.2.3 — La relación fraccionaria es una equivalencia {#talg-pro-00056}

La relación $\sim_D$ es una relación de equivalencia sobre $P_D$.

#### Demostración {#talg-prf-00092}

**Reflexividad.** Sea $\langle a,b\rangle\in P_D$. Como la multiplicación en un dominio íntegro es conmutativa,

$$
ab=ba.
$$

Por tanto,

$$
\langle a,b\rangle\sim_D\langle a,b\rangle.
$$

**Simetría.** Supongamos

$$
\langle a,b\rangle\sim_D\langle c,d\rangle.
$$

Entonces $ad=bc$. Por simetría de la igualdad,

$$
bc=ad.
$$

Por conmutatividad,

$$
cb=da,
$$

y por consiguiente

$$
\langle c,d\rangle\sim_D\langle a,b\rangle.
$$

**Transitividad.** El [Corolario 21.3.2](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-cor-00013) proporciona en el dominio íntegro la ley de cancelación por factores no nulos. Bajo la definición negativa canónica de dominio, la auditoría fundacional ha clasificado ese puente como clásico y registra DNE. Instanciando esa ley en el [Lema 24.2.2](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-lem-00006), obtenemos la transitividad de $\sim_D$.

Por tanto $\sim_D$ es reflexiva, simétrica y transitiva: es una relación de equivalencia. $\square$

> **Interfaz constructiva.** Si la cancelación por factores no nulos se aporta directamente como hipótesis positiva, la parte transitiva queda cubierta por el [Lema 24.2.2](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-lem-00006) sin DNE. No se redefine por ello la noción canónica de dominio íntegro.

---

## 24.3. Las fracciones son clases, no pares

### Definición 24.3.1 — Conjunto cociente de fracciones {#talg-def-00053}

Como la [Proposición 24.2.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00056) demuestra que $\sim_D$ es una equivalencia sobre $P_D$, existe el conjunto cociente

$$
P_D/\sim_D.
$$

Sus elementos son las clases de equivalencia de pares fraccionarios.

No se ha elegido ningún representante distinguido de cada clase. El cociente está formado por las clases mismas, concebidas como conjuntos en la interfaz fundacional ya cerrada.

---

### Notación 24.3.2 — Fracciones y cuerpo de fracciones subyacente {#talg-not-00016}

Escribiremos

$$
\boxed{
\operatorname{Frac}(D):=P_D/\sim_D.
}
$$

Si $\langle a,b\rangle\in P_D$, su clase se denotará indistintamente por

$$
[\langle a,b\rangle]_{\sim_D},
\qquad
[a,b]_D,
\qquad
\frac ab.
$$

La escritura $a/b$ designa, por tanto, **una clase de equivalencia**, no el par ordenado $\langle a,b\rangle$.

---

### Proposición 24.3.3 — Criterio exacto de igualdad de fracciones {#talg-pro-00057}

Para cualesquiera pares fraccionarios $\langle a,b\rangle,\langle c,d\rangle\in P_D$,

$$
\boxed{
\frac ab=\frac cd
\quad\Longleftrightarrow\quad
ad=bc.
}
$$

#### Demostración {#talg-prf-00093}

En un cociente por una relación de equivalencia, dos clases son iguales exactamente cuando sus representantes están relacionados por la equivalencia correspondiente. Aplicando esta caracterización a $\sim_D$,

$$
\frac ab=\frac cd
\quad\Longleftrightarrow\quad
\langle a,b\rangle\sim_D\langle c,d\rangle.
$$

Por la [Definición 24.2.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-def-00052), la condición de la derecha equivale a

$$
ad=bc.
$$

Esto demuestra la equivalencia. $\square$

> **Caracterización no es decisión.** El criterio reduce una igualdad de clases a una igualdad en $D$. No proporciona, por sí mismo, un algoritmo que decida si $ad=bc$. La igualdad en $\operatorname{Frac}(D)$ queda caracterizada, pero su decidibilidad no se ha establecido.

---

## 24.4. Preparar las operaciones: el denominador sigue siendo no nulo

### Proposición 24.4.1 — Producto de denominadores no nulos {#talg-pro-00058}

Si $b,d\in D$ satisfacen

$$
b\neq0,
\qquad
d\neq0,
$$

entonces

$$
\boxed{bd\neq0.}
$$

En particular, si $\langle a,b\rangle,\langle c,d\rangle\in P_D$, los pares

$$
\langle ad+bc,bd\rangle,
\qquad
\langle ac,bd\rangle
$$

pertenecen a $P_D$.

#### Demostración {#talg-prf-00094}

Supongamos, buscando contradicción, que

$$
bd=0.
$$

Como $b\neq0$ y $d\neq0$, los elementos $b$ y $d$ formarían un par de elementos no nulos cuyo producto es cero. Esto contradice directamente la cláusula negativa de ausencia de divisores de cero incorporada en la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047).

Por tanto,

$$
bd\neq0.
$$

Las expresiones $ad+bc$ y $ac$ pertenecen a $D$ por cierre de las operaciones del anillo, y acabamos de demostrar que $bd$ es un denominador admisible. Los dos pares anunciados pertenecen a $P_D$. $\square$

> **Nota lógica.** No hemos inferido la disyunción positiva $b=0\lor d=0$ desde $bd=0$. La prueba utiliza directamente la formulación negativa del dominio y, por ello, no introduce aquí DNE.

---

## 24.5. Independencia de representantes

### Proposición 24.5.1 — Compatibilidad de la suma fraccionaria {#talg-pro-00059}

Supongamos

$$
\langle a,b\rangle\sim_D\langle a',b'\rangle,
\qquad
\langle c,d\rangle\sim_D\langle c',d'\rangle.
$$

Entonces

$$
\boxed{
\langle ad+bc,bd\rangle
\sim_D
\langle a'd'+b'c',b'd'\rangle.
}
$$

#### Demostración {#talg-prf-00095}

Las hipótesis de equivalencia significan

$$
ab'=a'b,
\qquad
cd'=c'd.
$$

Por la [Proposición 24.4.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00058), $bd\neq0$ y $b'd'\neq0$, de modo que ambos pares candidatos pertenecen a $P_D$.

Para probar que son equivalentes debemos verificar

$$
(ad+bc)b'd'=(a'd'+b'c')bd.
$$

Distribuyendo y reordenando por conmutatividad,

$$
(ad+bc)b'd'
=
adb'd'+bcb'd'
=
(ab')dd'+bb'(cd').
$$

Usando $ab'=a'b$ y $cd'=c'd$,

$$
(ab')dd'+bb'(cd')
=
(a'b)dd'+bb'(c'd)
=
a'd'bd+b'c'bd.
$$

Factorizando,

$$
a'd'bd+b'c'bd
=(a'd'+b'c')bd.
$$

Por la [Definición 24.2.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-def-00052), los pares candidatos son equivalentes. $\square$

---

### Proposición 24.5.2 — Compatibilidad del producto fraccionario {#talg-pro-00060}

Bajo las mismas hipótesis,

$$
\boxed{
\langle ac,bd\rangle
\sim_D
\langle a'c',b'd'\rangle.
}
$$

#### Demostración {#talg-prf-00096}

Nuevamente,

$$
ab'=a'b,
\qquad
cd'=c'd,
$$

y los denominadores $bd$ y $b'd'$ son no nulos por la [Proposición 24.4.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00058).

La condición requerida es

$$
(ac)b'd'=(a'c')bd.
$$

Por asociatividad y conmutatividad,

$$
(ac)b'd'
=(ab')(cd')
=(a'b)(c'd)
=(a'c')bd.
$$

Por la [Definición 24.2.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-def-00052), los pares producto son equivalentes. $\square$

> **Error plausible.** Escribir inmediatamente
> $$
> \frac ab+\frac cd=\frac{ad+bc}{bd}
> $$
> antes de estas dos proposiciones sería anticipar una operación todavía no construida. Las fórmulas sobre representantes sólo descienden al cociente después de probar independencia.

---

### Lema 24.5.3 — Existencia y unicidad de las operaciones sobre el cociente {#talg-lem-00007}

Existen únicas funciones

$$
+_{\mathrm{Frac}}:
\operatorname{Frac}(D)\times\operatorname{Frac}(D)
\to
\operatorname{Frac}(D)
$$

y

$$
\cdot_{\mathrm{Frac}}:
\operatorname{Frac}(D)\times\operatorname{Frac}(D)
\to
\operatorname{Frac}(D)
$$

tales que, para todos los pares fraccionarios,

$$
\frac ab+_{\mathrm{Frac}}\frac cd
=
\frac{ad+bc}{bd},
$$

$$
\frac ab\cdot_{\mathrm{Frac}}\frac cd
=
\frac{ac}{bd}.
$$

#### Demostración {#talg-prf-00097}

Definimos primero una relación $G_+$ sobre

$$
\bigl(\operatorname{Frac}(D)\times\operatorname{Frac}(D)\bigr)
\times\operatorname{Frac}(D)
$$
mediante

$$
\left\langle\langle x,y\rangle,z\right\rangle\in G_+
$$
si y sólo si existen $a,b,c,d\in D$ con

$$
x=\frac ab,
\qquad
y=\frac cd,
\qquad
z=\frac{ad+bc}{bd},
$$

y $\langle a,b\rangle,\langle c,d\rangle\in P_D$.

Fijemos $x,y\in\operatorname{Frac}(D)$. Como $x$ e $y$ son clases de equivalencia de pares de $P_D$, existen localmente pares $\langle a,b\rangle$ y $\langle c,d\rangle$ que los representan. La [Proposición 24.4.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00058) garantiza que $bd\neq0$, así que la clase

$$
\frac{ad+bc}{bd}
$$
existe. Esto prueba existencia de un valor relacionado con $\langle x,y\rangle$.

Si elegimos otros representantes $\langle a',b'\rangle$ y $\langle c',d'\rangle$, la [Proposición 24.5.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00059) demuestra que las clases resultantes coinciden. Por tanto el valor es único.

Así $G_+$ es el grafo de una función con dominio

$$
\operatorname{Frac}(D)\times\operatorname{Frac}(D)
$$
y codominio $\operatorname{Frac}(D)$. Esa función es la única que satisface la fórmula anunciada.

Para el producto definimos análogamente $G_\cdot$ mediante

$$
z=\frac{ac}{bd}.
$$

La existencia vuelve a usar la [Proposición 24.4.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00058), y la unicidad se obtiene de la [Proposición 24.5.2](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00060). Resulta así una única función $\cdot_{\mathrm{Frac}}$ con la segunda fórmula.

No se ha construido una función que elija simultáneamente un representante para cada clase. En cada argumento fijo sólo eliminamos existenciales locales, y la independencia de representantes hace que el valor resultante sea canónico. Por tanto no se usa Choice. $\square$

> **Autoexplicación.** La pregunta correcta no es «¿qué representante elegimos?», sino «¿por qué cualquier representante produce la misma clase resultado?». Esa inversión de perspectiva es el mecanismo central de toda definición por cociente.

---

### Notación 24.5.4 — Operaciones fraccionarias {#talg-not-00017}

A partir de ahora omitiremos el subíndice cuando no haya ambigüedad y escribiremos

$$
\boxed{
\frac ab+\frac cd
:=
\frac{ad+bc}{bd},
}
$$

$$
\boxed{
\frac ab\cdot\frac cd
:=
\frac{ac}{bd}.
}
$$

Estas expresiones denotan las **funciones sobre clases** cuya existencia y unicidad fueron demostradas en el [Lema 24.5.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-lem-00007).

---

## 24.6. La estructura de cuerpo

### Definición 24.6.1 — Estructura fraccionaria inducida {#talg-def-00054}

Definimos la estructura

$$
\boxed{
\mathcal F_D
:=
\left\langle
\operatorname{Frac}(D),
+_{\mathrm{Frac}},
\cdot_{\mathrm{Frac}}
\right\rangle.
}
$$

Como en la convención general para anillos, esta escritura abrevia la codificación conjuntista anidada ya adoptada por el tratado.

---

### Teorema 24.6.2 — El cuerpo de fracciones {#talg-thm-00017}

La estructura $\mathcal F_D$ es un cuerpo. Sus elementos neutros son

$$
\boxed{
0_{\mathcal F_D}=\frac01,
\qquad
1_{\mathcal F_D}=\frac11.
}
$$

Además, si

$$
x=\frac ab\neq0_{\mathcal F_D},
$$

entonces $a\neq0$ y

$$
\boxed{
x^{-1}=\frac ba.}
$$

#### Demostración {#talg-prf-00098}

Fijemos clases fraccionarias y, cuando sea necesario, eliminemos localmente los existenciales que proporcionan representantes. No necesitamos una elección simultánea de representantes para todas las clases.

### Estructura aditiva

Sean

$$
x=\frac ab,
\qquad
y=\frac cd,
\qquad
z=\frac ef.
$$

Por la fórmula ya bien definida,

$$
(x+y)+z
=
\frac{ad+bc}{bd}+\frac ef
=
\frac{(ad+bc)f+bde}{bdf}.
$$

Por distributividad, asociatividad y conmutatividad en $D$,

$$
(ad+bc)f+bde
=
adf+bcf+bde.
$$

Por otro lado,

$$
x+(y+z)
=
\frac ab+\frac{cf+de}{df}
=
\frac{adf+b(cf+de)}{bdf}
=
\frac{adf+bcf+bde}{bdf}.
$$

Luego la suma es asociativa. La conmutatividad se obtiene igualmente de

$$
ad+bc=cb+da.
$$

La clase $0/1$ es neutra porque

$$
\frac ab+\frac01
=
\frac a b,
$$

usando la fórmula de suma y la [Proposición 24.3.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00057). El opuesto aditivo de $a/b$ es

$$
\frac{-a}{b},
$$

pues

$$
\frac ab+\frac{-a}{b}
=
\frac{ab+b(-a)}{b^2}
=
\frac0{b^2}
=
\frac01.
$$

La última igualdad se verifica por el criterio de la [Proposición 24.3.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00057):

$$
0\cdot1=0\cdot b^2.
$$

Así la suma hace de $\operatorname{Frac}(D)$ un grupo abeliano.

### Estructura multiplicativa

La multiplicación es asociativa porque

$$
\left(\frac ab\frac cd\right)\frac ef
=
\frac{ace}{bdf}
=
\frac ab\left(\frac cd\frac ef\right),
$$

y es conmutativa porque $ac=ca$ y $bd=db$ en $D$.

La clase $1/1$ es neutra:

$$
\frac ab\frac11=\frac ab.
$$

### Distributividad

Tenemos

$$
\frac ab\left(\frac cd+\frac ef\right)
=
\frac ab\frac{cf+de}{df}
=
\frac{acf+ade}{bdf}.
$$

Mientras que

$$
\frac ab\frac cd+\frac ab\frac ef
=
\frac{ac}{bd}+\frac{ae}{bf}
=
\frac{acbf+aebd}{b^2df}.
$$

Para comparar ambas clases usamos la [Proposición 24.3.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00057). El producto cruzado del primer numerador con el segundo denominador es

$$
(acf+ade)b^2df,
$$

y el del segundo numerador con el primer denominador es

$$
(acbf+aebd)bdf.
$$

Distribuyendo y reordenando, ambas expresiones son

$$
a b^2 c d f^2+a b^2 d^2 e f.
$$

Por tanto se cumple la distributividad. La otra ley distributiva coincide por conmutatividad del producto.

Hemos demostrado que $\mathcal F_D$ es un anillo conmutativo.

### No trivialidad

Si

$$
\frac01=\frac11,
$$

La [Proposición 24.3.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00057) daría

$$
0\cdot1=1\cdot1,
$$
esto es,

$$
0=1,
$$
contradiciendo la no trivialidad de $D$. Luego

$$
\frac01\neq\frac11.
$$

### Inversos de las clases no nulas

Sea

$$
x=\frac ab\neq\frac01.
$$

Afirmamos que $a\neq0$. En efecto, si $a=0$, entonces

$$
a\cdot1=0=b\cdot0,
$$

y la [Proposición 24.3.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00057) implicaría

$$
\frac ab=\frac01,
$$
contradicción.

Por tanto $a\neq0$, así que $\langle b,a\rangle\in P_D$ y la clase $b/a$ existe. Entonces

$$
\frac ab\frac ba
=
\frac{ab}{ba}
=
\frac11,
$$

donde la última igualdad se obtiene de la [Proposición 24.3.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00057) porque

$$
(ab)\cdot1=ba.
$$

Por conmutatividad, el producto en el orden inverso también es $1/1$. Todo elemento no nulo posee así inverso multiplicativo.

Por la [Definición 22.1.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048), $\mathcal F_D$ es un cuerpo. $\square$

> **Qué no se ha demostrado.** La fórmula $[a,b]^{-1}=[b,a]$ es una construcción formal del inverso una vez disponemos de un representante de la clase y de una prueba de que la clase es no nula. No se ha construido un test general que decida si una clase dada es cero.

---

## 24.7. El dominio original dentro del cuerpo de fracciones

### Definición 24.7.1 — Inmersión canónica en el cuerpo de fracciones {#talg-def-00055}

Definimos la función canónica

$$
\boxed{
\iota_D:D\to\operatorname{Frac}(D),
\qquad
\iota_D(a):=\frac a1.
}
$$

Está bien tipada porque $1\neq0$ en todo dominio íntegro, de modo que $\langle a,1\rangle\in P_D$ para cada $a\in D$.

La definición no selecciona ningún dato auxiliar: el denominador $1$ es canónico.

---

### Proposición 24.7.2 — La inmersión canónica es un homomorfismo unital inyectivo {#talg-pro-00061}

La función

$$
\iota_D:D\to\operatorname{Frac}(D)
$$

definida por $\iota_D(a)=a/1$ es un homomorfismo de anillos unital e inyectivo.

#### Demostración {#talg-prf-00099}

Sean $a,c\in D$. Entonces

$$
\iota_D(a+c)
=
\frac{a+c}{1},
$$

mientras

$$
\iota_D(a)+\iota_D(c)
=
\frac a1+\frac c1
=
\frac{a+c}{1}.
$$

Por tanto preserva suma. Asimismo,

$$
\iota_D(ac)
=
\frac{ac}{1}
=
\frac a1\frac c1
=
\iota_D(a)\iota_D(c).
$$

Además,

$$
\iota_D(1_D)=\frac11=1_{\mathcal F_D}.
$$

Así $\iota_D$ es un homomorfismo de anillos en el sentido de la [Definición 17.2.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00039).

Para la inyectividad, supongamos

$$
\iota_D(a)=\iota_D(c).
$$

Entonces

$$
\frac a1=\frac c1.
$$

Por la [Proposición 24.3.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00057),

$$
a\cdot1=c\cdot1,
$$
y por neutralidad

$$
a=c.
$$

Luego $\iota_D$ es inyectiva. $\square$

> **Interpretación correcta.** La inyectividad permite tratar a $D$ como una copia isomorfa de un subanillo de $\operatorname{Frac}(D)$ cuando convenga, pero no convierte literalmente ambos conjuntos en el mismo conjunto.

---

### Corolario 24.7.3 — Todo dominio íntegro es isomorfo a un subanillo de un cuerpo {#talg-cor-00015}

Todo dominio íntegro $\mathcal D$ es isomorfo, como anillo, a un subanillo del cuerpo $\mathcal F_D$.

#### Demostración {#talg-prf-00100}

Por el [Teorema 24.6.2](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-thm-00017), $\mathcal F_D$ es un cuerpo y, en particular, un anillo. Por la [Proposición 24.7.2](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00061),

$$
\iota_D:D\to\operatorname{Frac}(D)
$$

es un homomorfismo de anillos inyectivo. La [Proposición 17.3.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00035) implica que

$$
\operatorname{im}\iota_D
$$

determina un subanillo de $\mathcal F_D$.

Consideremos la misma regla funcional con codominio restringido a la imagen:

$$
\widehat\iota_D:
D\to\operatorname{im}\iota_D,
\qquad
\widehat\iota_D(a)=\iota_D(a).
$$

Es sobreyectiva por definición de imagen e inyectiva porque $\iota_D$ lo es. Conserva las operaciones y la unidad por la misma prueba de la [Proposición 24.7.2](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00061). Por la [Definición 20.1.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-def-00046), $\widehat\iota_D$ es un isomorfismo de anillos.

Por tanto $\mathcal D$ es isomorfo a un subanillo de un cuerpo. $\square$

---

## 24.8. Cierre conceptual y fundacional

La construcción puede resumirse así:

$$
\boxed{
D
\longrightarrow
P_D
\longrightarrow
P_D/\sim_D
\longrightarrow
\mathcal F_D
}
$$

con

$$
\boxed{
\iota_D:D\hookrightarrow\operatorname{Frac}(D).
}
$$

El cambio conceptual decisivo es pasar de **representaciones** a **objetos definidos por equivalencia**. Una fracción abstracta no es un par elegido: es aquello que permanece invariante cuando cambiamos de representante mediante la ecuación cruzada.

La auditoría lógica del capítulo queda localizada:

- [Definición 24.1.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-def-00051), [Definición 24.2.1](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-def-00052) y las construcciones de cociente son compatibles con lectura constructiva en el sentido auditado;
- [Lema 24.2.2](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-lem-00006) identifica la interfaz positiva suficiente para la transitividad;
- [Proposición 24.2.3](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md#talg-pro-00056) usa la cancelación clásica ya cerrada y registra `DNE`;
- las pruebas posteriores no añaden un nuevo puente clásico sustantivo;
- no se usa Choice;
- no se afirma decidibilidad de $b\neq0$ ni de la igualdad en $\operatorname{Frac}(D)$;
- no se afirma computabilidad uniforme de las operaciones ni de los inversos.

> **Variación.** Si se parte de una estructura con una forma positiva de no nulidad y cancelación, la misma arquitectura de pares y cociente puede reutilizarse, pero el significado computacional de los datos adicionales debe estudiarse por separado. Esta observación no modifica la construcción clásica canónica del tratado.

> **Conexión.** La propiedad universal del cuerpo de fracciones no se incorpora aquí. Pertenece a la futura síntesis de propiedades universales de la Parte VI, donde podrá formularse después de haber desarrollado de manera transversal las nociones de extensión y factorización.

Con este capítulo queda cerrada la **Parte IV — Cuerpos**. La siguiente parte del tratado estudia cómo las estructuras algebraicas interactúan con un orden.

---

[← **Capítulo 23 — Homomorfismos de cuerpos**](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md) · [**Capítulo 25 — Grupos ordenados** →](tratado-de-algebra-capitulo-25-grupos-ordenados.md)
