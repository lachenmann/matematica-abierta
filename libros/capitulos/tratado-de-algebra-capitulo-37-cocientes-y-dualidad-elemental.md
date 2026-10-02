---
title: 'Tratado moderno de Álgebra — Capítulo 37: Cocientes y dualidad elemental'
description: Cocientes vectoriales, factorización lineal, dual algebraico, base dual, evaluación canónica y aniquiladores en dimensión finita.
author: Gustav A. Tachek
content-id: MA-BCH-0145
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
- cocientes-vectoriales
- dual-algebraico
- base-dual
- doble-dual
- aniquiladores
prerequisites:
- MA-BCH-0144
- MA-BCH-0143
- MA-BCH-0142
- MA-BCH-0141
- MA-BCH-0140
- MA-BCH-0037
- MA-BCH-0036
- MA-BCH-0035
- MA-BCH-0047
related:
- MA-BOK-0007
- MA-BCH-0144
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 37 — Cocientes y dualidad elemental

## 37.0. Propósito y posición deductiva

El [cociente aditivo](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-thm-00005) ya existe. La tarea nueva es demostrar que la acción escalar desciende y, después, añadir factorización lineal e isomorfía.

El [dual algebraico](#talg-def-00077) reúne las aplicaciones lineales al [cuerpo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) $F$ y permite construir el mapa dual y la [evaluación canónica](#talg-pro-00116). La base dual, la biyectividad de la evaluación y la recuperación por aniquiladores se prueban en [dimensión finita](tratado-de-algebra-capitulo-35-dimension-finita.md#talg-def-00074). Se mantiene la distinción entre $V$ y $V^{**}$.

El marco fundacional es ZF con lógica clásica. Los representantes de clases y las bases finitas se utilizan como testigos locales. La acción escalar se define después de probar independencia de representantes; la estructura del dual se certifica después de construir su conjunto. Ninguna demostración invoca Zorn.

---

## 37.1. Cociente aditivo de un espacio por un subespacio

### Definición 37.1.1 — Cociente aditivo de un espacio por un subespacio {#talg-def-00076}

Para $U\le V$, el grupo aditivo de $U$ es [subgrupo normal](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-pro-00018) del grupo abeliano de $V$. El conjunto cociente aditivo $V/U$ y su proyección $q_U:V\to V/U$ están disponibles por la [construcción de cocientes de grupos](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-thm-00005). Escribimos $[v]_U=v+U$, con
$$
[v]_U=[w]_U\iff v-w\in U,\qquad
[v]_U+[w]_U=[v+w]_U.
$$
La regla candidata para escalares será $a[v]_U=[av]_U$. Todavía no se utiliza como una función sobre clases: la siguiente proposición probará su independencia de representantes y certificará la estructura vectorial. El conjunto y la suma preceden así a la acción escalar.

## 37.2. Estructura vectorial del cociente y proyección lineal

### Proposición 37.2.1 — Estructura vectorial del cociente y proyección lineal {#talg-pro-00115}

La regla $a[v]_U=[av]_U$ está bien definida y hace de $V/U$ un espacio vectorial sobre $F$. La proyección $q_U(v)=[v]_U$ es lineal y sobreyectiva, con $\ker q_U=U$. Se incluyen $U=0$ y $U=V$.

#### Demostración {#talg-prf-00184}

Si $[v]_U=[v']_U$, el [criterio de clases aditivas](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003) da $v-v'\in U$. Por cierre escalar de $U$, $a(v-v')\in U$. Las [identidades vectoriales](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-pro-00107) dan $av-av'=a(v-v')$, luego $[av]_U=[av']_U$. Cada entrada $(a,C)$ posee un representante local de $C$ y un valor único; Separación en $(F\times V/U)\times V/U$ produce el grafo de la acción, sin una sección elegida de la proyección.

El grupo aditivo cociente ya existe. Es abeliano porque
$$
[v]_U+[w]_U=[v+w]_U=[w+v]_U=[w]_U+[v]_U.
$$
Las cuatro leyes escalares se verifican sobre representantes:
$$
\begin{aligned}
a([v]_U+[w]_U)&=[a(v+w)]_U=[av+aw]_U=a[v]_U+a[w]_U,\\
(a+b)[v]_U&=[(a+b)v]_U=[av+bv]_U=a[v]_U+b[v]_U,\\
(ab)[v]_U&=[(ab)v]_U=[a(bv)]_U=a(b[v]_U),\\
1_F[v]_U&=[v]_U.
\end{aligned}
$$
Como toda clase tiene un representante local y la acción es bien definida, estas son leyes en todo el cociente.

La proyección conserva suma por la estructura de grupo cociente y conserva escalares porque $q_U(av)=[av]_U=a[v]_U=a q_U(v)$. Su sobreyectividad y núcleo $U$ ya estaban probados para la [proyección aditiva](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00023) y permanecen iguales al añadir la acción escalar.

Si $U=V$, todas las clases coinciden con la clase cero y se obtiene el espacio cero. Si $U=0$, de $q_U(v)=q_U(w)$ se obtiene $v-w\in\{0\}$ y por tanto $v=w$. La proyección es así inyectiva, además de lineal y sobreyectiva, y es un isomorfismo vectorial por definición. Esta conclusión es isomorfía, sin identificación literal del conjunto de clases con $V$. $\square$

## 37.3. Factorización, isomorfía y dimensión del cociente

### Teorema 37.3.1 — Factorización, isomorfía y dimensión del cociente {#talg-thm-00040}

Para $U\le V$ y $T:V\to W$ lineal, $U\subseteq\ker T$ equivale a la existencia de una única aplicación lineal
$$
\overline T:V/U\to W,\qquad \overline T\circ q_U=T.
$$
Está dada por $\overline T([v]_U)=T(v)$. En particular,
$$
V/\ker T\cong\operatorname{im}T.
$$
Si $V$ es de dimensión finita, también lo es $V/U$ y
$$
\dim U+\dim(V/U)=\dim V.
$$
Si $T(U)\subseteq Z\le W$, existe el descenso lineal $V/U\to W/Z$ dado por $[v]_U\mapsto[T(v)]_Z$.

#### Demostración {#talg-prf-00185}

Si $U\subseteq\ker T$ y $[v]_U=[w]_U$, $v-w\in U$ implica $T(v)-T(w)=T(v-w)=0$. Por tanto $T(v)=T(w)$ y la regla sobre clases tiene valor único. Su grafo existe por Separación y cada clase posee localmente un representante. Preserva suma porque $T(v+w)=T(v)+T(w)$ y preserva escalares porque $T(av)=aT(v)$; ambas [operaciones cociente](#talg-pro-00115) ya están bien definidas. Así produce una aplicación lineal con la identidad conmutativa. Si otra aplicación $S$ la satisface, sobre cada clase $[v]_U$ vale $S([v]_U)=T(v)$; la sobreyectividad de $q_U$ y Extensionalidad dan unicidad.

Recíprocamente, para $u\in U$, $q_U(u)=0$, luego $T(u)=\overline T(0)=0$ por [preservación del cero](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113). Así $U\subseteq\ker T$.

Para la isomorfía, tomemos $U=\ker T$ y codominio $\operatorname{im}T$ con operaciones restringidas. La aplicación inducida es sobreyectiva por la definición de imagen. Si sus valores en $[v]$ y $[w]$ coinciden, $T(v-w)=0$ implica $v-w\in\ker T$, y las clases coinciden. Es por tanto un homomorfismo lineal biyectivo, es decir, un isomorfismo vectorial.

Para dimensión, sea $(u_i)_{i<r}$ una base de $U$ y [extendámosla](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-pro-00111) a una base $(u_i,v_j)$ de $V$, con $s$ vectores adicionales. Las clases $[v_j]_U$ generan el cociente, porque para una expresión de $x$ en esa base los términos de $U$ se proyectan a cero. Si $\sum_j a_j[v_j]_U=0$, entonces $\sum_j a_jv_j\in U$. Expresándolo en la base de $U$ se obtiene una relación en la base completa de $V$; independencia fuerza todos los $a_j$ a cero. Las clases forman base del cociente, luego su dimensión es $s$ y la de $V$ es $r+s$. Esto prueba la fórmula, incluyendo las listas vacías.

Finalmente, si $T(U)\subseteq Z$, el compuesto $q_Z\circ T$ es lineal. Para $u\in U$, su valor es $[T(u)]_Z=0$, luego $U$ está en su núcleo. La factorización ya probada produce el descenso lineal anunciado y su fórmula al evaluar representantes. $\square$

## 37.4. Espacio de aplicaciones lineales y dual algebraico

### Definición 37.4.1 — Espacio de aplicaciones lineales y dual algebraico {#talg-def-00077}

Definimos
$$
\mathcal L_F(V,W)=\{T:V\to W:T\text{ lineal}\},
\qquad V^*=\mathcal L_F(V,F).
$$
El cuerpo $F$ se considera como espacio vectorial sobre sí mismo, ya construido. Los conjuntos de funciones existen por Potencia y Separación y la condición lineal selecciona subconjuntos de ellos.

Para las funciones lineales proponemos las operaciones puntuales $(S+T)(v)=S(v)+T(v)$ y $(aT)(v)=aT(v)$. La siguiente proposición probará que permanecen en $\mathcal L_F(V,W)$ y certificará su estructura vectorial. El dual es algebraico: su definición incluye todas las funciones lineales al cuerpo y no contiene una condición de continuidad.

## 37.5. Estructura del dual, mapa dual y evaluación

### Proposición 37.5.1 — Estructura del dual, mapa dual y evaluación {#talg-pro-00116}

$\mathcal L_F(V,W)$ es espacio vectorial con operaciones puntuales; en particular $V^*$ lo es. Para $T:V\to W$ lineal, la función
$$
T^*:W^*\to V^*,\qquad T^*(\ell)=\ell\circ T
$$
es lineal. Se cumple $(S\circ T)^*=T^*\circ S^*$ e $\operatorname{id}_V^*=\operatorname{id}_{V^*}$ con los dominios adecuados. El doble dual $V^{**}=(V^*)^*$ existe, y
$$
J_V:V\to V^{**},\qquad J_V(v)(\ell)=\ell(v)
$$
es una aplicación lineal canónica. Todavía no se afirma su biyectividad.

#### Demostración {#talg-prf-00186}

La función cero es lineal y pertenece a $\mathcal L_F(V,W)$. Para $A,B$ lineales,
$$
(A+B)(u+v)=A(u)+A(v)+B(u)+B(v)
=(A+B)(u)+(A+B)(v)
$$
por conmutatividad aditiva, y $(A+B)(au)=aA(u)+aB(u)=a(A+B)(u)$. Para $\lambda\in F$, $(\lambda A)(u+v)=\lambda A(u)+\lambda A(v)$; además
$$
(\lambda A)(au)=\lambda aA(u)=a\lambda A(u)=a(\lambda A)(u).
$$
El paso central usa conmutatividad del cuerpo. Así las operaciones puntuales están cerradas en el conjunto.

Los grafos de esas operaciones existen por Separación y determinación única de cada valor. La asociatividad, conmutatividad, cero y opuestos del grupo se verifican en cada $v$ mediante las leyes del grupo aditivo de $W$. Las cuatro leyes escalares se verifican asimismo punto a punto: $(a+b)A(v)=aA(v)+bA(v)$, $a(A(v)+B(v))=aA(v)+aB(v)$, $(ab)A(v)=a(bA(v))$ y $1_FA(v)=A(v)$. Extensionalidad funcional prueba la estructura vectorial.

La composición $\ell\circ T$ es lineal por la [composición ya cerrada](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113), por lo que $T^*$ está bien tipada. Evaluando en $v$,
$$
T^*(\ell_1+\ell_2)(v)=\ell_1(Tv)+\ell_2(Tv),\qquad
T^*(a\ell)(v)=a\ell(Tv).
$$
Son exactamente los valores de $T^*\ell_1+T^*\ell_2$ y $aT^*\ell$. Así $T^*$ es lineal. Si $S:W\to X$ es lineal y $\eta\in X^*$,
$$
(S\circ T)^*(\eta)(v)=\eta(S(T(v)))=(T^*(S^*(\eta)))(v).
$$
Extensionalidad primero en $v$ y luego en $\eta$ da la identidad de composición. La identidad dual se prueba por $\ell\circ\operatorname{id}_V=\ell$.

Como $V^*$ ya está certificado vectorialmente, la definición del dual se aplica a él y produce $V^{**}$. Para $v\in V$, la función $\ell\mapsto\ell(v)$ es lineal por las operaciones puntuales del dual, luego pertenece a $V^{**}$. Su grafo y el de $J_V$ existen por Separación; el valor es único para cada entrada. Finalmente, para cualquier $\ell\in V^*$,
$$
J_V(u+v)(\ell)=\ell(u)+\ell(v),\qquad
J_V(au)(\ell)=a\ell(u).
$$
Estas igualdades prueban linealidad de $J_V$. La construcción es canónica y no presupone que los funcionales separen puntos en espacios arbitrarios. $\square$

## 37.6. Base dual y evaluación en dimensión finita

### Teorema 37.6.1 — Base dual y evaluación en dimensión finita {#talg-thm-00041}

Sea $(v_i)_{i<n}$ una lista base de $V$. Existen únicos funcionales $\ell_i\in V^*$ con $\ell_i(v_j)=1_F$ si $i=j$ y cero si $i\ne j$. Constituyen una lista base dual y
$$
v=\sum_{i<n}\ell_i(v)v_i,\qquad
\ell=\sum_{i<n}\ell(v_i)\ell_i.
$$
Por tanto $\dim V^*=\dim V$. Si $V$ es de dimensión finita, la evaluación canónica $J_V:V\to V^{**}$ es un isomorfismo. Es una isomorfía canónica, no igualdad literal de conjuntos.

#### Demostración {#talg-prf-00187}

El [teorema de especificación por una base](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-thm-00038) produce cada $\ell_i$ y su unicidad a partir de los valores indicados. Para $v=\sum_ja_jv_j$, la preservación de combinaciones da $\ell_i(v)=a_i$, por lo que la primera fórmula reproduce la representación de $v$.

Para independencia de los $\ell_i$, si $\sum_i b_i\ell_i=0$, evaluar en $v_j$ da $b_j=0$ para cada $j$. Para generación del dual, fijemos $\ell\in V^*$ y consideremos $L=\sum_i\ell(v_i)\ell_i$. En cada vector de base, $L(v_j)=\ell(v_j)$. Por [unicidad del mapa lineal con valores dados en la base](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-thm-00038), $L=\ell$. Así la lista dual es base de longitud $n$ y la dimensión es la misma.

La evaluación $J_V$ es lineal por la [proposición anterior](#talg-pro-00116). Si $J_V(v)=0$, entonces $\ell_i(v)=J_V(v)(\ell_i)=0$ para todos los índices. La primera fórmula da $v=0$, y el [criterio de núcleo trivial](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113) prueba inyectividad.

Para sobreyectividad, sea $\Lambda\in V^{**}$ y definamos explícitamente
$$
v_\Lambda=\sum_{i<n}\Lambda(\ell_i)v_i.
$$
Para cualquier $\ell\in V^*$,
$$
\begin{aligned}
J_V(v_\Lambda)(\ell)
&=\ell(v_\Lambda)
=\sum_i\Lambda(\ell_i)\ell(v_i)\\
&=\sum_i\ell(v_i)\Lambda(\ell_i)
=\Lambda\left(\sum_i\ell(v_i)\ell_i\right)
=\Lambda(\ell).
\end{aligned}
$$
Se usó conmutatividad del cuerpo en el intercambio de los coeficientes y linealidad de $\Lambda$ en la penúltima igualdad. Extensionalidad funcional da $J_V(v_\Lambda)=\Lambda$. Así $J_V$ es sobreyectiva y, junto con inyectividad, isomorfismo.

Si $n=0$, $V$ es cero, el único funcional es la función cero, y los spans vacíos son los espacios cero tanto del dual como del doble dual; las dos fórmulas son sumas vacías y la evaluación sigue siendo isomorfismo. La existencia local de una base finita utiliza la [teoría finita](tratado-de-algebra-capitulo-35-dimension-finita.md#talg-thm-00037) ya cerrada, sin Zorn. $\square$

## 37.7. Aniquiladores, dual del cociente y recuperación finita

### Proposición 37.7.1 — Aniquiladores, dual del cociente y recuperación finita {#talg-pro-00117}

Para $U\le V$, definimos su **aniquilador**
$$
U^0=\{\ell\in V^*:\forall u\in U,\ \ell(u)=0_F\}.
$$
Es subespacio y el mapa $\ell\mapsto\ell\circ q_U$ identifica mediante isomorfismo $(V/U)^*$ con $U^0$.

Si $V$ es de dimensión finita,
$$
\dim U+\dim U^0=\dim V,\qquad
U=\{v\in V:\forall\ell\in U^0,\ \ell(v)=0_F\}.
$$
La última igualdad se formula en $V$; la relación con el doble dual se interpreta mediante $J_V$, sin identificación literal.

#### Demostración {#talg-prf-00188}

El aniquilador existe por Separación en $V^*$. Contiene el funcional cero; si $\alpha,\beta$ se anulan en $U$, también $(\alpha+\beta)(u)=0+0=0$ y $(a\alpha)(u)=a0=0$. El [criterio de subespacio](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00109) lo certifica.

Para $\ell\in(V/U)^*$, la composición $\ell\circ q_U$ se anula en $U$, porque $q_U(u)=0$ y $\ell(0)=0$. El mapa de composición es lineal por la [proposición de mapa dual](#talg-pro-00116), ahora con codominio restringido al aniquilador. Es inyectivo: si $\ell_1\circ q_U=\ell_2\circ q_U$, para una clase $C$ tomemos localmente $v$ con $C=q_U(v)$; entonces $\ell_1(C)=\ell_2(C)$. Extensionalidad da igualdad de funcionales. Es sobreyectivo: para $\alpha\in U^0$, la [factorización lineal del cociente](#talg-thm-00040) produce el único funcional $\ell:V/U\to F$ con $\ell\circ q_U=\alpha$. Así es isomorfismo.

Si $V$ es de dimensión finita, el cociente también es de dimensión finita. La [igualdad dimensional del dual](#talg-thm-00041) y la [invariancia bajo isomorfismos](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113) dan $\dim U^0=\dim(V/U)$. La [fórmula de dimensión del cociente](#talg-thm-00040) concluye $\dim U+\dim U^0=\dim V$.

Para recuperación, una inclusión sigue de la definición: todo $u\in U$ es anulado por cada miembro de $U^0$. A la inversa, fijemos una base finita de $U$ y [extendámosla](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-pro-00111) a una base de $V$ con vectores adicionales $w_0,\ldots,w_{s-1}$. Los funcionales de la base dual correspondientes a estos vectores adicionales se anulan en todos los vectores de la base de $U$ y, por linealidad, en todo $U$; pertenecen a $U^0$. Si $v$ es anulado por todos los miembros de $U^0$, sus coeficientes en los $w_j$ son cero, por la [fórmula de coordenadas de la base dual](#talg-thm-00041). Su expresión en la base completa sólo contiene vectores de $U$, luego $v\in U$. Esto prueba la inclusión recíproca.

Cuando $U=0$ o $U=V$, los bloques de base correspondientes pueden ser vacíos; la argumentación cubre esos casos y el espacio cero. No se afirma recuperación para un espacio arbitrario sin hipótesis adicionales que garanticen suficientes funcionales. $\square$

## 37.99. Síntesis

El cociente vectorial reutiliza el cociente aditivo y añade una acción escalar bien definida. Su propiedad universal produce factorizaciones lineales e isomorfías. La dualidad algebraica se construyó como conjunto de mapas lineales, y su evaluación se certificó canónicamente. Los resultados dimensionales y de recuperación por aniquiladores permanecen explícitamente finitos. La parte de álgebra multilineal puede utilizar mapas lineales, espacios libres y cocientes sin nuevas hipótesis de elección.

---

[← **Capítulo 36 — Aplicaciones lineales**](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
