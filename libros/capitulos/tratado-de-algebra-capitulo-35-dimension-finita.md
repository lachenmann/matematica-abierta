---
title: 'Tratado moderno de Álgebra — Capítulo 35: Dimensión finita'
description: Intercambio finito, dimensión natural bien definida, criterios de base, finitud de subespacios y fórmula de dimensión para sumas y sumas directas internas.
author: Gustav A. Tachek
content-id: MA-BCH-0143
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
- dimension-finita
- intercambio
- bases
- subespacios
- sumas-directas
prerequisites:
- MA-BCH-0142
- MA-BCH-0141
- MA-BCH-0140
- MA-BCH-0047
- MA-BCH-0136
related:
- MA-BOK-0007
- MA-BCH-0142
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 35 — Dimensión finita

## 35.0. Propósito y posición deductiva

La dimensión natural debe ser independiente de la base elegida. Se demuestra [intercambio finito](#talg-lem-00010) antes de [definirla](#talg-def-00074); después se obtienen el control de subespacios y las fórmulas de suma.

Trabajamos en un [espacio vectorial](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-def-00070) $V$ sobre un [cuerpo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) $F$, con la [interfaz de naturales, inducción y recursión](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006) ya disponible.

El marco fundacional es ZF con lógica clásica. Los usos clásicos sobre coeficientes y pertenencia al subespacio generado se declaran en las demostraciones; los testigos de las construcciones finitas son locales. Se trabaja sólo con espacios finitamente generados. No se introduce dimensión cardinal infinita ni se usa el teorema condicionado a Zorn.

---

## 35.1. Intercambio finito y conteos

### Lema 35.1.1 — Intercambio finito y conteos {#talg-lem-00010}

Si $(u_i)_{i<r}$ es [independiente](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-def-00073) y $(w_j)_{j<s}$ [genera](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-def-00072) $V$, entonces $r\le s$. Pueden reemplazarse $r$ elementos de la lista generadora por los $u_i$, conservando una lista generadora de longitud $s$. En consecuencia, dos listas base finitas tienen la misma longitud. Los conteos de concatenaciones emplean la adición natural de la [interfaz natural](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006), con sus leyes de asociación y conmutación derivadas recursivamente.

#### Demostración {#talg-prf-00177}

**Conteos.** La longitud de concatenar una lista de longitud $m$ y una de longitud $n$ es $m+n$, por inducción en el número de términos añadidos y la ecuación $m+S(k)=S(m+k)$. Para no presuponer leyes aritméticas adicionales, las ecuaciones recursivas dan $0+n=n$ por inducción en $n$, y $S(m)+n=S(m+n)$ por la misma inducción. Con estas dos identidades, inducción en $n$ da $m+n=n+m$. Inducción en $p$ da $(m+n)+p=m+(n+p)$: el caso cero usa el neutro y el paso aplica la ecuación del sucesor a ambos lados. Se usarán estas leyes sólo para los conteos naturales finitos.

**Intercambio.** Mantengamos una lista generadora de longitud $s$ cuyos primeros $k$ vectores son $u_0,\ldots,u_{k-1}$ y los restantes proceden de los $w_j$ no reemplazados. El caso $k=0$ es la lista dada. Para introducir $u_k$, escribámoslo como combinación de la lista actual:
$$
u_k=\sum_{i<k}a_iu_i+\sum_{j}b_jw'_j.
$$
Algún coeficiente $b_j$ es no nulo. En efecto, si todos fueran cero, la igualdad produciría la relación
$$
u_k-\sum_{i<k}a_iu_i=0
$$
en la lista independiente original, con coeficiente $1_F\ne0_F$ en $u_k$, contradicción. El paso desde «no todos son cero» a un coeficiente no nulo es clásico y se declara aquí.

Elijamos ese índice sólo como testigo local. Como $b_j$ es [invertible](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-pro-00049),
$$
w'_j=b_j^{-1}u_k-\sum_{i<k}(b_j^{-1}a_i)u_i
-\sum_{\ell\ne j}(b_j^{-1}b_\ell)w'_\ell.
$$
Así la lista donde se sustituye $w'_j$ por $u_k$ sigue generando: todos sus elementos pertenecen al span original y el elemento retirado se recupera mediante la fórmula. Reordenando, cumple el invariante para $k+1$.

Cada paso consume un elemento restante de la lista original. Tras $s$ pasos no quedan $w'_j$; si todavía hubiera otro $u_s$, pertenecería al span de los anteriores y la misma relación con coeficiente $1_F$ contradiría independencia. Por tanto no pueden realizarse más de $s$ pasos y $r\le s$. La inducción finita produce los reemplazos anunciados sin selección de una familia infinita.

Si dos listas base tienen longitudes $r,s$, aplicar el resultado con la primera independiente y la segunda generadora da $r\le s$. Al invertir sus papeles se obtiene $s\le r$. La antisimetría del orden natural implica $r=s$. Los casos de listas vacías están incluidos: una lista generadora vacía sólo genera el espacio cero, que no posee una lista independiente de longitud positiva. $\square$

## 35.2. Dimensión natural de un espacio finitamente generado

### Definición 35.2.1 — Dimensión natural de un espacio finitamente generado {#talg-def-00074}

Un espacio sobre $F$ es **finitamente generado**, o de **dimensión finita**, si posee una lista generadora finita. La [extracción finita](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-pro-00111) proporciona una lista base. El [lema de intercambio](#talg-lem-00010) prueba que todas las listas base tienen una misma longitud natural. Definimos
$$
\dim_F V=n
$$
como esa longitud única. Se abrevia $\dim V$ cuando el cuerpo está fijado. Esta definición utiliza existencia y unicidad del número, sin elegir una base distinguida para cada espacio. No define dimensión cardinal para espacios arbitrarios ni compara dimensiones sobre cuerpos distintos.

## 35.3. Criterios de dimensión y finitud de subespacios

### Teorema 35.3.1 — Criterios de dimensión y finitud de subespacios {#talg-thm-00037}

Si $\dim V=n$, toda lista independiente tiene longitud a lo sumo $n$ y toda lista generadora tiene longitud al menos $n$. Una lista de longitud $n$ es base si y sólo si es independiente, y si y sólo si genera $V$.

Todo subespacio $U\le V$ es de dimensión finita, $\dim U\le n$, y $\dim U=n$ equivale a $U=V$. Además,
$$
\dim\{0_V\}=0,\qquad \dim F^n=n.
$$

#### Demostración {#talg-prf-00178}

Fijemos localmente una lista base de $V$ de longitud $n$, cuya existencia está probada. Comparar una lista independiente con esa lista generadora mediante [intercambio](#talg-lem-00010) da su cota superior. Comparar esa lista independiente con cualquier generadora da la cota inferior para generadoras.

Si una lista independiente tiene longitud $n$, la [extensión finita](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-pro-00111) la amplía a una lista base. Su longitud final es $n$ por [definición de dimensión](#talg-def-00074), de modo que no se añadió ningún elemento y la lista original ya genera. Si una lista generadora tiene longitud $n$, la [extracción finita](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-pro-00111) produce una sublista base de longitud $n$; no se retiró ningún elemento, porque retirar uno reduce la longitud natural de una lista finita. Así la original es independiente. Una base cumple ambas condiciones por definición.

**Subespacios.** Toda lista independiente de $U$ es independiente en $V$, porque la suma y la acción son restricciones y las relaciones se evalúan igual. Se construye una lista base de $U$ mediante una inducción de longitud acotada por $n$. Partimos de la lista vacía. En cada paso, para una lista independiente $L$ en $U$, usamos la disyunción clásica $\operatorname{span}(L)=U$ o no. Si son iguales, ya tenemos base. En la segunda rama, como el span está contenido en $U$, la lógica clásica proporciona un testigo local $u\in U\setminus\operatorname{span}(L)$. La [adjunción](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-lem-00009) conserva independencia y aumenta en uno la longitud.

Si no se hubiera obtenido generación al llegar a longitud $n$, se podría añadir otro vector, creando en $V$ una lista independiente de longitud $n+1$, imposible por la cota inicial. La inducción finita demuestra existencia de base de $U$, sin selección infinita. Su longitud $m$ satisface $m\le n$. Si $m=n$, esa base es una lista independiente de longitud $n$ en $V$, luego genera $V$ por el criterio ya probado. Su span en $V$ coincide con su span en $U$, pues las operaciones son restricciones; así $U=V$. La recíproca es inmediata por identidad de la estructura.

**Cero y potencias.** La lista vacía es base del espacio cero, luego su dimensión es cero. Para $F^n$, definamos $e_i(j)=1_F$ si $i=j$ y $0_F$ en otro caso, para $i,j<n$. Los grafos existen por Separación con esas condiciones de igualdad. Para $x\in F^n$, la suma finita $\sum_{i<n}x(i)e_i$ evaluada en $j$ tiene todos sus términos cero salvo el de índice $j$, y vale $x(j)$. Esto se justifica retirando términos cero por el [lema de sumas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008). Extensionalidad funcional prueba que la lista genera. Si $\sum_{i<n}a_ie_i=0$, evaluar en cada $j$ da $a_j=0$, de modo que es independiente. Por tanto es base y $\dim F^n=n$. Para $n=0$, el único vector es la función vacía y la lista base es vacía, acorde con el caso anterior. $\square$

## 35.4. Dimensión de sumas y suma directa interna

### Proposición 35.4.1 — Dimensión de sumas y suma directa interna {#talg-pro-00112}

Para subespacios $U,W$ de un espacio $V$ de dimensión finita,
$$
\dim(U+W)+\dim(U\cap W)=\dim U+\dim W.
$$
Si $U+W=V$ y $U\cap W=\{0\}$, escribimos $V=U\oplus W$ y decimos que es una **suma directa interna**. La condición de intersección trivial equivale a la unicidad de toda descomposición $x=u+w$ en $U+W$. En ese caso $\dim V=\dim U+\dim W$.

#### Demostración {#talg-prf-00179}

La intersección es subespacio por el [capítulo 33](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00110) y todos los subespacios implicados son finitos por el [Teorema 35.3.1](#talg-thm-00037). Tomemos localmente una lista base $c_0,\ldots,c_{r-1}$ de $C=U\cap W$. Extendámosla a bases de $U$ y $W$ por la [extensión finita](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-pro-00111):
$$
(c_0,\ldots,c_{r-1},u_0,\ldots,u_{p-1}),\qquad
(c_0,\ldots,c_{r-1},w_0,\ldots,w_{q-1}).
$$
Son dos aplicaciones finitas de existencia, sin elección de bases para una familia arbitraria.

La lista conjunta $(c,u,w)$ genera $U+W$: las expresiones de $u'\in U$ y $w'\in W$ en sus respectivas bases se suman, reuniendo los coeficientes de los $c_i$. Para independencia, supongamos
$$
\sum_i\alpha_ic_i+\sum_j\beta_ju_j+\sum_k\gamma_kw_k=0.
$$
Entonces $t=\sum_k\gamma_kw_k$ pertenece a $W$ y también a $U$, pues es el opuesto de los otros dos bloques. Por tanto $t\in C$ y existe una expresión local $t=\sum_i\delta_ic_i$. La relación
$$
\sum_k\gamma_kw_k-\sum_i\delta_ic_i=0
$$
en la base de $W$ obliga a $\gamma_k=0$ y $\delta_i=0$. La relación original queda en la base de $U$ y obliga a $\alpha_i=\beta_j=0$. Así la lista conjunta es base de $U+W$.

Los conteos proporcionan $\dim U=r+p$, $\dim W=r+q$ y $\dim(U+W)=r+p+q$. Las leyes naturales demostradas en el [lema de intercambio](#talg-lem-00010) dan
$$
(r+p+q)+r=(r+p)+(r+q),
$$
que es la fórmula anunciada, sin introducir resta de naturales.

Si la intersección es cero y $u+w=u'+w'$, entonces $u-u'=w'-w\in U\cap W$, de donde ambas diferencias son cero y las descomposiciones coinciden. A la inversa, para $t\in U\cap W$, las dos descomposiciones $0=t+(-t)=0+0$ pertenecen a $U+W$. La unicidad implica $t=0$. Queda probada la equivalencia.

Si además $U+W=V$, la intersección tiene dimensión cero y la fórmula se reduce a $\dim V=\dim U+\dim W$. Los casos $U=0$, $W=0$ o $V=0$ quedan incluidos, usando listas vacías. $\square$

## 35.99. Síntesis

La dimensión natural es una invariante demostrada por intercambio finito. Las cotas de independencia y generación controlan subespacios y permiten construir sus bases sin Zorn. La suma directa interna añade unicidad a la descomposición; la fórmula de dimensiones mide la superposición mediante la intersección.

---

[← **Capítulo 34 — Independencia lineal y bases**](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
