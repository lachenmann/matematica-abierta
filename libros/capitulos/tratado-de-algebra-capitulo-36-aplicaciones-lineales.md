---
title: 'Tratado moderno de Álgebra — Capítulo 36: Aplicaciones lineales'
description: Linealidad, núcleo e imagen, espacio libre de soporte finito, extensión sobre una base dada y fórmula de rango-nulidad en dimensión finita.
author: Gustav A. Tachek
content-id: MA-BCH-0144
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
- aplicaciones-lineales
- nucleo
- imagen
- espacio-libre
- rango-nulidad
prerequisites:
- MA-BCH-0143
- MA-BCH-0142
- MA-BCH-0141
- MA-BCH-0140
- MA-BCH-0022
- MA-BCH-0047
- MA-BCH-0136
related:
- MA-BOK-0007
- MA-BCH-0143
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## 36.0. Propósito y posición deductiva

Una aplicación lineal conserva suma y escalares del mismo cuerpo. Se demuestran las propiedades de núcleo e imagen, la construcción del [espacio libre de soporte finito](#talg-pro-00114), la determinación de un mapa por una [base dada](#talg-thm-00038) y [rango-nulidad en dimensión finita](#talg-thm-00039). El espacio libre prepara también la construcción tensorial posterior.

Trabajamos con [espacios vectoriales](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-def-00070) sobre un mismo [cuerpo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) $F$ y con las [sumas finitas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) ya disponibles.

El marco fundacional es ZF con lógica clásica. Los usos clásicos de igualdad y pertenencia al soporte se declaran en las demostraciones. Cuando interviene una base arbitraria, ésta es un dato de hipótesis; la base del espacio libre se construye explícitamente. Las bases finitas de núcleo e imagen se obtienen por los resultados finitos anteriores. Ninguna demostración invoca Zorn.

---

## 36.1. Aplicación lineal e isomorfismo vectorial

### Definición 36.1.1 — Aplicación lineal e isomorfismo vectorial {#talg-def-00075}

Para espacios $V,W$ sobre el mismo cuerpo $F$, una función $T:V\to W$ es **lineal** si
$$
T(u+v)=T(u)+T(v),\qquad T(au)=aT(u).
$$
Una aplicación lineal biyectiva es un **isomorfismo vectorial**. Su inversa funcional existe por la [interfaz de biyecciones](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002); su linealidad se probará a continuación. El **núcleo** y la **imagen** son los subconjuntos
$$
\ker T=\{v\in V:T(v)=0_W\},\qquad
\operatorname{im}T=\{w\in W:\exists v\in V,\ T(v)=w\}.
$$
Estas definiciones existen por Separación y coinciden con núcleo e imagen del homomorfismo de grupos aditivos subyacente. La coincidencia no presupone todavía que sean subespacios.

## 36.2. Núcleo, imagen y operaciones de aplicaciones lineales

### Proposición 36.2.1 — Núcleo, imagen y operaciones de aplicaciones lineales {#talg-pro-00113}

Una aplicación lineal conserva cero, opuestos y combinaciones finitas. Identidades y composiciones son lineales; $\ker T$ y $\operatorname{im}T$ son subespacios. Además,
$$
T\text{ inyectiva}\iff\ker T=\{0_V\},\qquad
T\text{ sobreyectiva}\iff\operatorname{im}T=W.
$$
La inversa de un isomorfismo vectorial es lineal. Un isomorfismo entre espacios de dimensión finita conserva la dimensión.

#### Demostración {#talg-prf-00180}

De $T(0_V)=T(0_V+0_V)=T(0_V)+T(0_V)$, cancelación en el grupo aditivo de $W$ da $T(0_V)=0_W$. Como $T(v)+T(-v)=T(v-v)=0_W$, unicidad del opuesto da $T(-v)=-T(v)$. Inducción en la longitud de la suma, con base $T(0_V)=0_W$, y las [dos leyes de linealidad](#talg-def-00075) prueban $T(\sum_i a_iv_i)=\sum_i a_iT(v_i)$.

La identidad conserva suma y acción por igualdad funcional. Si $S:W\to X$ es lineal, entonces $(S\circ T)(u+v)=S(T(u)+T(v))=S(T(u))+S(T(v))$ y $(S\circ T)(au)=S(aT(u))=aS(T(u))$.

El núcleo contiene $0_V$; para $u,v$ en él, $T(u+v)=0+0=0$ y $T(au)=a0=0$. Es subespacio por el [criterio](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00109). La imagen contiene $T(0_V)=0_W$. Si $x=T(u)$, $y=T(v)$, los valores $x+y=T(u+v)$ y $ax=T(au)$ están en la imagen. Los testigos son locales; el [criterio](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00109) certifica la imagen.

Si $T$ es inyectiva, $T(v)=0=T(0)$ implica $v=0$, de donde el núcleo es singleton. Si el núcleo es singleton y $T(u)=T(v)$, entonces $T(u-v)=0$, luego $u-v=0$ y $u=v$. La sobreyectividad equivale a que cada elemento de $W$ tenga una preimagen, exactamente la igualdad de imagen indicada.

Si $T$ es biyectiva y $x=T(u)$, $y=T(v)$, entonces $x+y=T(u+v)$ y $ax=T(au)$. Aplicando la inversa funcional $T^{-1}$ resulta
$$
T^{-1}(x+y)=u+v=T^{-1}(x)+T^{-1}(y),\qquad
T^{-1}(ax)=au=aT^{-1}(x).
$$
Cada entrada tiene una preimagen única, por lo que la inversa es lineal.

Para [dimensión](tratado-de-algebra-capitulo-35-dimension-finita.md#talg-def-00074), fijemos localmente una lista base $(v_i)_{i<n}$ de $V$. La sobreyectividad y la preservación de combinaciones muestran que $(T(v_i))_{i<n}$ genera $W$. Si $\sum_i a_iT(v_i)=0$, la linealidad da $T(\sum_i a_iv_i)=0$; inyectividad da $\sum_i a_iv_i=0$, e independencia obliga a todos los coeficientes cero. Es base de $W$ de longitud $n$, luego $\dim W=\dim V$. No se identifica literalmente ninguno de los dos espacios. $\square$

## 36.3. Espacio libre de soporte finito y base canónica

### Proposición 36.3.1 — Espacio libre de soporte finito y base canónica {#talg-pro-00114}

Para cualquier conjunto $I$, $F^{(I)}$ es subespacio de $F^I$ con las operaciones puntuales. Para $i\in I$, sea $\delta_i:I\to F$ igual a $1_F$ en $i$ y a $0_F$ fuera de $i$. El conjunto $\{\delta_i:i\in I\}$ es una [base canónica](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-def-00073) de $F^{(I)}$, y
$$
a=\sum_{i\in E}a(i)\delta_i
$$
para cualquier testigo finito de soporte $E$ de $a$. Si $I=\varnothing$, se obtiene el espacio cero con base vacía. Se llama a $F^{(I)}$ el **espacio vectorial libre sobre el conjunto $I$**.

#### Demostración {#talg-prf-00181}

El conjunto ya existe como subconjunto del [espacio de funciones](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-pro-00108). La función cero posee soporte testigo vacío. Si $a,c$ tienen testigos finitos $E,D$, fuera de $E\cup D$ ambos valores son cero, de modo que $a+c$ también vale cero allí. Esa unión es finita. Si $\lambda\in F$, fuera de $E$ vale $(\lambda a)(i)=\lambda0_F=0_F$, luego $E$ es testigo de soporte para $\lambda a$. El [criterio de subespacio](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00109) certifica $F^{(I)}$.

El grafo de $\delta_i$ existe por Separación con las condiciones de igualdad $j=i$ o $j\ne i$, usadas clásicamente. El singleton $\{i\}$ es testigo de soporte. Si $i\ne j$, evaluar en $i$ distingue $\delta_i(i)=1_F$ de $\delta_j(i)=0_F$, usando la no trivialidad del cuerpo; la familia está indexada sin repeticiones.

Sea $a$ con testigo finito $E$. Para $j\in I$, si $j\in E$, la suma $\sum_{i\in E}a(i)\delta_i$ evaluada en $j$ tiene un término $a(j)$ y los demás cero. Si $j\notin E$, todos sus términos son cero y $a(j)=0_F$ por el testigo de soporte. La disyunción de pertenencia usada aquí es clásica y explícita. Extensionalidad funcional prueba la fórmula y por tanto generación.

En una relación sobre índices distintos $i_0,\ldots,i_{n-1}$,
$$
\sum_{k<n}b_k\delta_{i_k}=0,
$$
evaluar en $i_j$ deja sólo el término $b_j$, luego $b_j=0_F$. Esto prueba independencia. La familia canónica es base. Si $I$ es vacío, el conjunto de funciones tiene un solo elemento, la función vacía, y las afirmaciones se reducen al caso cero.

La base se construyó con funciones delta definidas por igualdad; no se eligió una base de un espacio arbitrario ni se aplicó Zorn. La existencia de esta base específica no implica que pertenencia o igualdad en $I$ sean decidibles efectivamente. $\square$

## 36.4. Determinación de una aplicación lineal por una base dada

### Teorema 36.4.1 — Determinación de una aplicación lineal por una base dada {#talg-thm-00038}

Si $B$ es una base dada de $V$ y $h:B\to W$ una función dada, existe una única aplicación lineal $T:V\to W$ con $T(b)=h(b)$ para $b\in B$. Está determinada por
$$
T(v)=\sum_{b\in B}a_v(b)h(b),
$$
donde $a_v$ es la función única de coordenadas de $v$ sobre $B$.

Para cualquier conjunto $I$ y función $h:I\to W$, existe asimismo una única aplicación lineal $T:F^{(I)}\to W$ con $T(\delta_i)=h(i)$, dada por $T(a)=\sum_{i\in I}a(i)h(i)$. La hipótesis es una función dada, no una selección de valores desde una familia de conjuntos no vacíos.

#### Demostración {#talg-prf-00182}

La evaluación $E_B:F^{(B)}\to V$ del [Lema 34.2.1](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-lem-00009) es biyectiva cuando $B$ es base. Es también lineal: para funciones de soporte finito $a,c$, se toma localmente la unión de sus soportes y se aplica distributividad finita para obtener $E_B(a+c)=E_B(a)+E_B(c)$; la misma ley da $E_B(\lambda a)=\lambda E_B(a)$. El espacio de soporte finito está certificado en la [proposición anterior](#talg-pro-00114). Por la [linealidad de inversas](#talg-pro-00113), $v\mapsto a_v=E_B^{-1}(v)$ es lineal.

Definamos $E_h:F^{(B)}\to W$ por $E_h(a)=\sum_b a(b)h(b)$. La independencia del soporte y la existencia del grafo se prueban como en el [lema de evaluación](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-lem-00009): añadir términos fuera de un soporte añade términos cero, y el valor es único. Para dos entradas, en la unión de soportes,
$$
E_h(a+c)=\sum_b(a(b)+c(b))h(b)=E_h(a)+E_h(c),
$$
y
$$
E_h(\lambda a)=\sum_b\lambda a(b)h(b)=\lambda E_h(a).
$$
Así $E_h$ es lineal. La composición $T=E_h\circ E_B^{-1}$ existe y es lineal. Para $b\in B$, la función delta de índice $b$ evalúa a $b$; por unicidad es $a_b$, y $T(b)=h(b)$.

Si $S$ es otra aplicación lineal con esos valores, para cualquier vector y su representación finita,
$$
S(v)=S\left(\sum_ba_v(b)b\right)
=\sum_ba_v(b)S(b)=\sum_ba_v(b)h(b)=T(v).
$$
Extensionalidad funcional da $S=T$.

En el espacio libre sobre $I$, la fórmula directa $E_h(a)=\sum_i a(i)h(i)$ está bien definida y es lineal por las dos verificaciones sobre soportes anteriores, ahora con índices en $I$. Su valor en $\delta_i$ es $h(i)$. Cada entrada posee la expresión canónica $a=\sum_i a(i)\delta_i$, por lo que cualquier aplicación lineal con los valores indicados debe coincidir con esa fórmula. Esto prueba existencia y unicidad también en el caso libre. No se invoca la existencia de una base arbitraria: $B$ es dato o la base delta es canónica. $\square$

## 36.5. Rango y nulidad en dimensión finita

### Teorema 36.5.1 — Rango y nulidad en dimensión finita {#talg-thm-00039}

Si $V$ es de dimensión finita y $T:V\to W$ lineal, el núcleo y la imagen son de dimensión finita aunque $W$ no lo sea. Definimos $\operatorname{nul}T=\dim\ker T$ y $\operatorname{rg}T=\dim\operatorname{im}T$. Entonces
$$
\operatorname{nul}T+\operatorname{rg}T=\dim V.
$$
Si además $\dim W=\dim V$, la inyectividad de $T$ equivale a su sobreyectividad, y cualquiera de ambas implica que $T$ es un isomorfismo.

#### Demostración {#talg-prf-00183}

El núcleo es subespacio de $V$, luego es [finito](tratado-de-algebra-capitulo-35-dimension-finita.md#talg-thm-00037). Tomemos localmente una lista base $(u_i)_{i<r}$ del núcleo y [extendámosla](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-pro-00111) a una lista base de $V$,
$$
(u_0,\ldots,u_{r-1},v_0,\ldots,v_{s-1}).
$$
Las imágenes de esa base generan $\operatorname{im}T$: para $x=\sum_i a_iu_i+\sum_jb_jv_j$,
$$
T(x)=\sum_i a_iT(u_i)+\sum_jb_jT(v_j)
=\sum_jb_jT(v_j).
$$
Así la lista $(T(v_j))_{j<s}$ genera la imagen.

Para independencia, si $\sum_jc_jT(v_j)=0$, entonces $y=\sum_jc_jv_j$ está en el núcleo. Existe una expresión $y=\sum_i d_iu_i$ en su base. La relación
$$
\sum_jc_jv_j-\sum_i d_iu_i=0
$$
en la base completa de $V$ obliga a que todos los $c_j$ y $d_i$ sean cero. Por tanto las imágenes $T(v_j)$ constituyen una lista base de la imagen. Ésta es finita, su dimensión es $s$, y $\dim V=r+s$. Esto prueba la fórmula de rango-nulidad con independencia del tamaño de $W$.

Supongamos ahora $\dim W=\dim V=n$. Si $T$ es inyectiva, su núcleo es cero, de dimensión cero, luego la imagen tiene dimensión $n$. Como es subespacio de $W$, el [criterio de igualdad de dimensión bajo inclusión](tratado-de-algebra-capitulo-35-dimension-finita.md#talg-thm-00037) da $\operatorname{im}T=W$ y sobreyectividad.

Si $T$ es sobreyectiva, $s=\dim W=n$ y $r+n=n$. Esto fuerza $r=0$: una concatenación con $r$ términos iniciales adicionales tiene longitud $r+n$, y si $r$ fuese un sucesor, esa longitud sería estrictamente mayor que $n$ por la [recursión del orden natural](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006); inducción en $r$ prueba esa propiedad. La base del núcleo es vacía, luego el núcleo es el espacio cero y $T$ es inyectiva. Ambas condiciones juntas hacen a $T$ un isomorfismo. En el caso $V=0$, $r=s=0$ y todas las afirmaciones mantienen sus hipótesis exactas. $\square$

## 36.99. Síntesis

La linealidad preserva combinaciones finitas y convierte núcleo e imagen en subespacios. El espacio libre posee una base canónica sin elección, y una base dada determina mapas por sus valores. Rango-nulidad se obtuvo extendiendo una base finita del núcleo; no se presupuso finitud del codominio. El [capítulo siguiente](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md) añadirá la acción escalar a los cocientes aditivos y construirá el dual algebraico.

---

[← **Capítulo 35 — Dimensión finita**](tratado-de-algebra-capitulo-35-dimension-finita.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md) · [**Capítulo 37 — Cocientes y dualidad elemental →**](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md)
