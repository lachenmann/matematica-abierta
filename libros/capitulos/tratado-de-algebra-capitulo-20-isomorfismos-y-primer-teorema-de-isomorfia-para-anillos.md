---
title: 'Tratado moderno de Álgebra — Capítulo 20: Isomorfismos y primer teorema de isomorfía para anillos'
description: Capítulo del Tratado moderno de Álgebra dedicado a isomorfismos y primer teorema de isomorfía para anillos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0045
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-16'
date-modified: '2026-09-16'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
prerequisites:
- MA-BCH-0044
related:
- MA-BOK-0007
- MA-BCH-0044
- MA-BCH-0046
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 20 — Isomorfismos y primer teorema de isomorfía para anillos

## 20.0. Propósito y posición deductiva

La teoría desarrollada hasta aquí dispone ya de las cuatro piezas necesarias para el primer teorema de isomorfía en anillos:

1. homomorfismos unitarios de anillos;
2. núcleos como ideales bilaterales;
3. cocientes por ideales bilaterales;
4. imágenes como subanillos unitarios.

Falta únicamente fijar la noción de **isomorfismo de anillos** y demostrar que la biyectividad permite invertir un homomorfismo sin perder ninguna de las dos operaciones ni la unidad multiplicativa. Después podremos hacer descender un homomorfismo

$$
f:R\to S
$$

al cociente por su núcleo y obtener

$$
\boxed{
\mathcal R/\ker f
\cong
\text{el subanillo de }\mathcal S\text{ inducido sobre }\operatorname{im}f.
}
$$

Como en el caso de grupos, el punto conjuntista delicado no es la fórmula informal

$$
[a]_{\ker f}\longmapsto f(a),
$$

sino demostrar que el valor es independiente del representante y construir una función genuina sobre el conjunto cociente sin efectuar una elección global de representantes.

> **Contraste bibliográfico.** La arquitectura se contrasta con Dummit–Foote (`BIB-TALG-0001`), Lam (`BIB-TALG-0008`) y, para el caso conmutativo, Atiyah–Macdonald (`BIB-TALG-0007`). Las demostraciones se desarrollan íntegramente dentro del tratado.

---

## 20.1. Isomorfismos de anillos

### Definición 20.1.1 — Isomorfismo de anillos {#talg-def-00046}

Sean

$$
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

anillos. Una función

$$
f:R\to S
$$

es un **isomorfismo de anillos** si se cumplen simultáneamente:

1. $f$ es un homomorfismo de anillos en el sentido de la [Definición 17.2.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00039);
2. $f$ es biyectiva en el sentido importado por [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002).

Por nuestra convención unital, la primera condición incluye explícitamente

$$
f(1_{\mathcal R})=1_{\mathcal S}.
$$

No se exige como axioma adicional que la inversa funcional preserve la estructura: eso se demostrará a continuación.

---

### Proposición 20.1.2 — La inversa de un isomorfismo de anillos es un isomorfismo {#talg-pro-00046}

Sean $\mathcal R$ y $\mathcal S$ anillos y sea

$$
f:R\to S
$$

un isomorfismo de anillos. Entonces la función inversa

$$
f^{-1}:S\to R
$$

es un isomorfismo de anillos de $\mathcal S$ en $\mathcal R$.

#### Demostración {#talg-prf-00070}

Como $f$ es biyectiva, [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) proporciona una función inversa

$$
f^{-1}:S\to R
$$

con

$$
f^{-1}\circ f=\operatorname{id}_R,
\qquad
f\circ f^{-1}=\operatorname{id}_S.
$$

Sean $u,v\in S$ y escribamos

$$
a:=f^{-1}(u),
\qquad
b:=f^{-1}(v).
$$

Entonces $f(a)=u$ y $f(b)=v$. Como $f$ preserva la suma,

$$
f(a+_R b)=f(a)+_S f(b)=u+_S v.
$$

Aplicando $f^{-1}$,

$$
f^{-1}(u+_S v)=a+_R b
=f^{-1}(u)+_R f^{-1}(v).
$$

Del mismo modo, por preservación del producto,

$$
f(a\cdot_R b)=f(a)\cdot_S f(b)=u\cdot_S v,
$$

y por tanto

$$
f^{-1}(u\cdot_S v)
=
f^{-1}(u)\cdot_R f^{-1}(v).
$$

Finalmente, como

$$
f(1_{\mathcal R})=1_{\mathcal S},
$$

aplicar $f^{-1}$ da

$$
f^{-1}(1_{\mathcal S})=1_{\mathcal R}.
$$

Así, $f^{-1}$ es un homomorfismo de anillos. Además, $f$ es una inversa bilateral de $f^{-1}$, de modo que [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) implica que $f^{-1}$ es biyectiva. Por la [Definición 20.1.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-def-00046), $f^{-1}$ es un isomorfismo de anillos. $\square$

---

### Proposición 20.1.3 — Identidad y composición de isomorfismos de anillos {#talg-pro-00047}

Sean $\mathcal R$, $\mathcal S$ y $\mathcal T$ anillos.

1. La identidad
   $$
   \operatorname{id}_R:R\to R
   $$
   es un isomorfismo de anillos de $\mathcal R$ consigo mismo.
2. Si
   $$
   f:R\to S
   \qquad\text{y}\qquad
   g:S\to T
   $$
   son isomorfismos de anillos, entonces
   $$
   g\circ f:R\to T
   $$
   es un isomorfismo de anillos.

#### Demostración {#talg-prf-00071}

Por la [Proposición 17.2.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00033), $\operatorname{id}_R$ es un homomorfismo de anillos. Ella misma es inversa bilateral de sí misma, por lo que [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) implica que es biyectiva. Así, la [Definición 20.1.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-def-00046) la identifica como isomorfismo.

Sean ahora $f$ y $g$ isomorfismos. Por la [Proposición 17.2.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00033), la composición $g\circ f$ es un homomorfismo de anillos. Por la [Proposición 20.1.2](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-pro-00046) existen isomorfismos inversos

$$
f^{-1}:S\to R,
\qquad
g^{-1}:T\to S.
$$

Definamos

$$
h:=f^{-1}\circ g^{-1}:T\to R.
$$

Para $a\in R$,

$$
\begin{aligned}
h((g\circ f)(a))
&=f^{-1}(g^{-1}(g(f(a))))\\
&=f^{-1}(f(a))\\
&=a,
\end{aligned}
$$

y para $c\in T$,

$$
\begin{aligned}
(g\circ f)(h(c))
&=g(f(f^{-1}(g^{-1}(c))))\\
&=g(g^{-1}(c))\\
&=c.
\end{aligned}
$$

Por tanto, $h$ es inversa bilateral de $g\circ f$. [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) implica que $g\circ f$ es biyectiva. Junto con su carácter de homomorfismo, la [Definición 20.1.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-def-00046) concluye que es un isomorfismo de anillos. $\square$

> **Consecuencia notacional.** La notación ya activa $\cong$ ([Notación 8.3.1](tratado-de-algebra-capitulo-8-isomorfismos.md#talg-not-00005)) se interpreta desde ahora también en contexto de anillos: expresa la existencia de un isomorfismo de anillos, nunca igualdad literal de estructuras.

---

## 20.2. Primer teorema de isomorfía para anillos

### Teorema 20.2.1 — Primer teorema de isomorfía para anillos {#talg-thm-00012}

Sean

$$
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

anillos, y sea

$$
f:R\to S
$$

un homomorfismo de anillos. Escribamos

$$
K:=\ker f,
$$

donde el núcleo se toma respecto del homomorfismo de los grupos aditivos subyacentes.

Entonces $K$ es un ideal bilateral de $R$ y existe una única función

$$
\overline f:R/K\longrightarrow\operatorname{im}f
$$

que satisface

$$
\overline f([a]_K)=f(a)
\qquad(a\in R).
$$

Esta función es un isomorfismo de anillos entre el anillo cociente

$$
\mathcal R/K
$$

y el subanillo de $\mathcal S$ inducido sobre $\operatorname{im}f$. En particular,

$$
\boxed{
\mathcal R/\ker f
\cong
\left\langle
\operatorname{im}f,
+_{\operatorname{im}f},
\cdot_{\operatorname{im}f}
\right\rangle.
}
$$

#### Demostración {#talg-prf-00072}

Por la [Proposición 18.3.1](tratado-de-algebra-capitulo-18-ideales.md#talg-pro-00038),

$$
K=\ker f
$$

es un ideal bilateral de $R$. Por el [Teorema 19.3.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-thm-00011), el cociente

$$
\mathcal R/K
$$

es un anillo. Por la [Proposición 17.3.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00035), $\operatorname{im}f$ determina un subanillo de $\mathcal S$; por la [Proposición 17.1.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00030), la estructura inducida sobre la imagen es un anillo y tiene el mismo cero y la misma unidad que $\mathcal S$.

La demostración se divide en cinco pasos.

### Paso 1. Independencia del representante

Supongamos

$$
[a]_K=[b]_K.
$$

Por la [Proposición 19.1.5](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00040),

$$
a-b\in K=\ker f.
$$

Por definición de núcleo,

$$
f(a-b)=0_S.
$$

Por la [Proposición 17.2.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00032), $f$ preserva opuestos aditivos, y como es aditiva,

$$
\begin{aligned}
f(a-b)
&=f(a+(-b))\\
&=f(a)+f(-b)\\
&=f(a)-f(b).
\end{aligned}
$$

Luego

$$
f(a)-f(b)=0_S.
$$

En el grupo aditivo de $S$,

$$
\begin{aligned}
f(a)
&=f(a)+0_S\\
&=f(a)+\bigl(-f(b)+f(b)\bigr)\\
&=\bigl(f(a)-f(b)\bigr)+f(b)\\
&=0_S+f(b)\\
&=f(b).
\end{aligned}
$$

Por tanto,

$$
\boxed{[a]_K=[b]_K\Longrightarrow f(a)=f(b)}.
$$

### Paso 2. Construcción de $\overline f$ sin elección global de representantes

Definimos

$$
\Gamma_{\overline f}
:=
\left\{
\langle C,y\rangle\in (R/K)\times\operatorname{im}f:
\exists a\in R\;\bigl(C=[a]_K\land y=f(a)\bigr)
\right\}.
$$

Este conjunto existe por producto cartesiano y Separación.

Sea $C\in R/K$. Por definición de conjunto cociente, existe $a\in R$ tal que

$$
C=[a]_K.
$$

Entonces $f(a)\in\operatorname{im}f$ y

$$
\langle C,f(a)\rangle\in\Gamma_{\overline f}.
$$

Así, el grafo es total sobre $R/K$.

Para la funcionalidad, supongamos

$$
\langle C,y\rangle,
\langle C,z\rangle
\in\Gamma_{\overline f}.
$$

Existen $a,b\in R$ tales que

$$
C=[a]_K=[b]_K,
\qquad
y=f(a),
\qquad
z=f(b).
$$

Por el Paso 1, $f(a)=f(b)$, y por tanto $y=z$. El grafo define una función

$$
\overline f:R/K\to\operatorname{im}f
$$

con

$$
\overline f([a]_K)=f(a).
$$

No se ha elegido simultáneamente un representante de cada clase: se utiliza sólo la existencia local de algún representante y la funcionalidad prueba que todos producen el mismo valor.

La unicidad es inmediata. Si

$$
\psi:R/K\to\operatorname{im}f
$$

satisface

$$
\psi([a]_K)=f(a)
$$

para todo $a\in R$, entonces para cada $C\in R/K$ existe $a\in R$ con $C=[a]_K$, y

$$
\psi(C)=f(a)=\overline f(C).
$$

Por Extensionalidad de funciones,

$$
\psi=\overline f.
$$

### Paso 3. $\overline f$ es un homomorfismo de anillos

Sean $[a]_K,[b]_K\in R/K$. Por las operaciones cociente,

$$
[a]_K+_K[b]_K=[a+b]_K,
$$

por lo que

$$
\begin{aligned}
\overline f([a]_K+_K[b]_K)
&=\overline f([a+b]_K)\\
&=f(a+b)\\
&=f(a)+_S f(b).
\end{aligned}
$$

Como la suma del subanillo inducido sobre $\operatorname{im}f$ es la restricción de $+_S$,

$$
f(a)+_S f(b)
=
f(a)+_{\operatorname{im}f}f(b).
$$

Así,

$$
\overline f([a]_K+_K[b]_K)
=
\overline f([a]_K)+_{\operatorname{im}f}\overline f([b]_K).
$$

Análogamente,

$$
\begin{aligned}
\overline f([a]_K\cdot_K[b]_K)
&=\overline f([ab]_K)\\
&=f(ab)\\
&=f(a)\cdot_S f(b)\\
&=f(a)\cdot_{\operatorname{im}f}f(b).
\end{aligned}
$$

Para la unidad, el [Teorema 19.3.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-thm-00011) da

$$
1_{\mathcal R/K}=[1_R]_K,
$$

y entonces

$$
\overline f(1_{\mathcal R/K})
=
\overline f([1_R]_K)
=
f(1_R)
=
1_S.
$$

Por la [Proposición 17.1.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00030), el subanillo inducido sobre $\operatorname{im}f$ tiene unidad $1_S$. Por tanto $\overline f$ preserva también la unidad multiplicativa y es un homomorfismo de anillos.

### Paso 4. $\overline f$ es sobreyectiva

Sea $y\in\operatorname{im}f$. Por definición de imagen existe $a\in R$ tal que

$$
y=f(a).
$$

Entonces

$$
y=f(a)=\overline f([a]_K).
$$

Luego $\overline f$ es sobreyectiva.

### Paso 5. $\overline f$ es inyectiva

Supongamos

$$
\overline f([a]_K)=\overline f([b]_K).
$$

Entonces

$$
f(a)=f(b).
$$

Por aditividad y preservación de opuestos,

$$
\begin{aligned}
f(a-b)
&=f(a)-f(b)\\
&=0_S.
\end{aligned}
$$

Por definición de núcleo,

$$
a-b\in K.
$$

La [Proposición 19.1.5](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00040) implica entonces

$$
[a]_K=[b]_K.
$$

Así, $\overline f$ es inyectiva.

Hemos probado que $\overline f$ es un homomorfismo de anillos biyectivo. Por la [Definición 20.1.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-def-00046), es un isomorfismo de anillos. En consecuencia,

$$
\mathcal R/\ker f
\cong
\left\langle
\operatorname{im}f,
+_{\operatorname{im}f},
\cdot_{\operatorname{im}f}
\right\rangle.
$$

$\square$

> **Lectura estructural.** El núcleo contiene exactamente las diferencias que el homomorfismo vuelve invisibles. Cocientar por él elimina esa pérdida de información; restringir el codominio a la imagen elimina los elementos nunca alcanzados. El resultado restante es reversible.

---

## 20.3. Forma sobreyectiva

### Corolario 20.3.1 — Forma sobreyectiva del primer teorema de isomorfía para anillos {#talg-cor-00011}

Sea

$$
f:R\to S
$$

un homomorfismo **sobreyectivo** de anillos. Entonces existe un isomorfismo de anillos

$$
\widehat f:R/\ker f\longrightarrow S
$$

caracterizado por

$$
\widehat f([a]_{\ker f})=f(a)
\qquad(a\in R).
$$

En particular,

$$
\boxed{
\mathcal R/\ker f\cong\mathcal S.
}
$$

#### Demostración {#talg-prf-00073}

Por sobreyectividad, para todo $s\in S$ existe $a\in R$ con $f(a)=s$. Por definición de imagen,

$$
\operatorname{im}f\subseteq S.
$$

La sobreyectividad da la inclusión inversa, y por Extensionalidad

$$
\operatorname{im}f=S.
$$

El [Teorema 20.2.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-thm-00012) proporciona una función biyectiva

$$
\overline f:R/\ker f\to\operatorname{im}f
$$

con

$$
\overline f([a]_{\ker f})=f(a).
$$

Como $\operatorname{im}f=S$ es una igualdad literal de conjuntos, el codominio de esa misma función es $S$; no estamos sustituyendo el codominio por una estructura meramente isomorfa. Denotemos esta misma función por

$$
\widehat f:R/\ker f\to S.
$$

La biyectividad se conserva inmediatamente. Además, para $a,b\in R$,

$$
\begin{aligned}
\widehat f([a]_{\ker f}+_{\ker f}[b]_{\ker f})
&=f(a+b)\\
&=f(a)+_S f(b),
\end{aligned}
$$

$$
\begin{aligned}
\widehat f([a]_{\ker f}\cdot_{\ker f}[b]_{\ker f})
&=f(ab)\\
&=f(a)\cdot_S f(b),
\end{aligned}
$$

y

$$
\widehat f(1_{\mathcal R/\ker f})
=
\widehat f([1_R]_{\ker f})
=
f(1_R)
=
1_S.
$$

Así, $\widehat f$ es un homomorfismo de anillos. Al ser biyectiva, la [Definición 20.1.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-def-00046) implica que es un isomorfismo. $\square$

---

## 20.4. Cierre del bloque

La cadena estructural queda ahora cerrada en la forma

```text
homomorfismo de anillos f:R→S
        ↓
ker f = ideal bilateral
        ↓
anillo cociente R/ker f
        ↓
mapa inducido [a] ↦ f(a)
        ↓
buena definición sin elección global de representantes
        ↓
homomorfismo biyectivo R/ker f → im f
        ↓
primer teorema de isomorfía
        ↓
si f es sobreyectivo: R/ker f ≅ S
```

Con esto puede abrirse ya la noción de **dominio íntegro** sin dejar pendiente la infraestructura elemental de isomorfismos y cocientes de anillos.

---

[← **Capítulo 19 — Cocientes de anillos**](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md) · [**Capítulo 21 — Dominios íntegros** →](tratado-de-algebra-capitulo-21-dominios-integros.md)
