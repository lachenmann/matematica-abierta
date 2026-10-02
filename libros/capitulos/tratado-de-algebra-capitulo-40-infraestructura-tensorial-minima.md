---
title: 'Tratado moderno de Álgebra — Capítulo 40: Infraestructura tensorial mínima'
description: Construcción del producto tensorial por cociente, aplicación canónica, tensores puros, propiedad universal, mapas inducidos y bases tensoriales dadas.
author: Gustav A. Tachek
content-id: MA-BCH-0148
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
- producto-tensorial
- propiedad-universal
- aplicaciones-bilineales
- bases
- dimension-finita
prerequisites:
- MA-BCH-0146
- MA-BCH-0145
- MA-BCH-0144
- MA-BCH-0143
- MA-BCH-0142
- MA-BCH-0141
- MA-BCH-0140
- MA-BCH-0136
- MA-BCH-0047
- MA-BCH-0021
related:
- MA-BOK-0007
- MA-BCH-0147
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## 40.0. Propósito y posición deductiva

Se construirá el producto tensorial binario de dos espacios vectoriales sobre un mismo cuerpo conmutativo mediante un [cociente vectorial](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md#talg-pro-00115) de un [espacio vectorial libre](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00114). La construcción precede a la notación tensorial: primero se definen las [relaciones bilineales](#talg-def-00081) en el espacio libre, después se certifica su span como subespacio, luego se forma el cociente vectorial y sólo entonces se introducen $U\otimes_F V$ y los tensores puros.

El alcance queda restringido a la infraestructura algebraica mínima necesaria para tratados posteriores: construcción por cociente, aplicación bilineal canónica, [propiedad universal](#talg-thm-00044), unicidad hasta isomorfismo, mapas inducidos y comportamiento sobre bases dadas. No se desarrollan módulos sobre anillos, categorías generales, completaciones, productos tensoriales topológicos, álgebras simétricas o exteriores ni teoría de representaciones.

El marco fundacional es ZF, con los usos de lógica clásica declarados en las dependencias y en la comparación de índices para la base tensorial. No se presupone igualdad decidible. Las bases arbitrarias se reciben como datos; los representantes se utilizan como testigos locales. No se usa el axioma de elección ni la rama de Zorn.

---

## 40.1. Relaciones bilineales en el espacio libre

### Definición 40.1.1 — Familias de relaciones bilineales y su span {#talg-def-00081}

Sean $U$ y $V$ espacios vectoriales sobre un mismo cuerpo conmutativo $F$. En el espacio libre
$$
E_F(U,V)=F^{(U\times V)}
$$
escribimos $\delta_{(u,v)}$ para el vector delta canónico asociado a $(u,v)\in U\times V$.

Definimos cuatro subconjuntos de $E_F(U,V)$:
$$
\begin{aligned}
\mathcal R_1&=\{\delta_{(u+u',v)}-\delta_{(u,v)}-\delta_{(u',v)}:
                 u,u'\in U,\ v\in V\},\\
\mathcal R_2&=\{\delta_{(au,v)}-a\delta_{(u,v)}:
                 a\in F,\ u\in U,\ v\in V\},\\
\mathcal R_3&=\{\delta_{(u,v+v')}-\delta_{(u,v)}-\delta_{(u,v')}:
                 u\in U,\ v,v'\in V\},\\
\mathcal R_4&=\{\delta_{(u,av)}-a\delta_{(u,v)}:
                 a\in F,\ u\in U,\ v\in V\}.
\end{aligned}
$$

Cada familia existe por Separación dentro de $E_F(U,V)$: las expresiones que aparecen en ella están bien tipadas por las operaciones del espacio libre y por las operaciones de $U$ y $V$. Llamamos **familia de relaciones bilineales** a
$$
\mathcal R_F(U,V)=\mathcal R_1\cup\mathcal R_2\cup\mathcal R_3\cup\mathcal R_4
$$
y definimos su **span de relaciones** por
$$
R_F(U,V)=\operatorname{span}_F\!\bigl(\mathcal R_F(U,V)\bigr)
\subseteq E_F(U,V).
$$

En este punto $R_F(U,V)$ es únicamente el conjunto definido mediante el [span ya construido](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-def-00072). Todavía no se utiliza que sea un subespacio, no se forma ningún cociente y no se introduce la notación $U\otimes_F V$.

## 40.2. El subespacio de relaciones

### Proposición 40.2.1 — El span de relaciones bilineales es un subespacio {#talg-pro-00120}

Sean $U$ y $V$ espacios vectoriales sobre el mismo cuerpo conmutativo $F$. Entonces
$$
R_F(U,V)\le E_F(U,V)=F^{(U\times V)}.
$$
En particular, el span de relaciones bilineales es un subespacio del espacio vectorial libre sobre $U\times V$.

#### Demostración {#talg-prf-00193}

Por la [Definición 40.1.1](#talg-def-00081), $\mathcal R_F(U,V)$ es un subconjunto de $E_F(U,V)$ y
$$
R_F(U,V)=\operatorname{span}_F\!\bigl(\mathcal R_F(U,V)\bigr).
$$
La [Proposición 33.5.1](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00110) afirma que, para todo subconjunto $A$ de un espacio vectorial $X$, $\operatorname{span}_F(A)$ es un subespacio de $X$. Al aplicarla con
$$
X=E_F(U,V),\qquad A=\mathcal R_F(U,V),
$$
se obtiene inmediatamente $R_F(U,V)\le E_F(U,V)$. No se requiere una nueva verificación de cierre por suma o por escalares. $\square$

## 40.3. Cociente vectorial preliminar

### Definición 40.3.1 — Cociente vectorial preliminar de la construcción tensorial {#talg-def-00082}

Sean $U$ y $V$ espacios vectoriales sobre un mismo cuerpo conmutativo $F$. Como
$$
R_F(U,V)\le E_F(U,V),
$$
definimos el **cociente vectorial preliminar de la construcción tensorial** por
$$
Q_F(U,V):=E_F(U,V)/R_F(U,V).
$$

La [Definición 37.1.1](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md#talg-def-00076) proporciona el conjunto cociente aditivo y la [Proposición 37.2.1](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md#talg-pro-00115) certifica que este cociente es un espacio vectorial sobre $F$. En particular, la proyección cociente
$$
q_{R_F(U,V)}:E_F(U,V)\longrightarrow Q_F(U,V)
$$
es lineal y sobreyectiva, y satisface
$$
\ker q_{R_F(U,V)}=R_F(U,V).
$$

La letra $Q_F(U,V)$ es deliberadamente provisional. En esta etapa no se identifica todavía este espacio con $U\otimes_F V$, no se define la notación $u\otimes v$ y no se afirma aún que la aplicación $(u,v)\mapsto q_{R_F(U,V)}(\delta_{(u,v)})$ sea bilineal.

## 40.4. Notación tensorial y aplicación canónica

### Notación 40.4.1 — Producto tensorial {#talg-not-00020}

Sean $U$ y $V$ espacios vectoriales sobre un mismo cuerpo conmutativo $F$. Como el cociente vectorial $Q_F(U,V)$ ya fue construido en la [Definición 40.3.1](#talg-def-00082), escribimos
$$
U\otimes_F V:=Q_F(U,V)
=E_F(U,V)/R_F(U,V)
$$
y llamamos a este espacio vectorial el **producto tensorial de $U$ y $V$ sobre $F$**.

Esta escritura es una abreviatura para el espacio ya existente; no constituye una nueva construcción ni incorpora todavía su propiedad universal. En particular, en este punto no se define $u\otimes v$, no se ha construido aún la aplicación canónica $U\times V\to U\otimes_F V$ y no se afirma bilinealidad.

### Definición 40.4.2 — Aplicación tensorial canónica {#talg-def-00083}

Sean $U,V$ espacios sobre el mismo cuerpo conmutativo $F$. La función
$$
\tau_{U,V}:U\times V\longrightarrow U\otimes_F V,\qquad
\tau_{U,V}(u,v)=q_{R_F(U,V)}(\delta_{(u,v)})
$$
existe: para cada pareja la función delta tiene un valor único en $E_F(U,V)$, y la proyección tiene un valor único en el cociente. El grafo del compuesto se obtiene por Separación en $(U\times V)\times(U\otimes_F V)$. La llamamos **aplicación tensorial canónica**. Su bilinealidad se probará en [§40.5](#talg-pro-00121).

### Notación 40.4.3 — Tensor puro {#talg-not-00021}

Una vez definida $\tau_{U,V}$, escribimos
$$
u\otimes v:=\tau_{U,V}(u,v).
$$
Un elemento del producto tensorial se llama **tensor puro** o **descomponible** cuando pertenece a la imagen de $\tau_{U,V}$; esto significa que existen $u\in U,v\in V$ cuyo tensor es ese elemento. No se exige unicidad de los factores ni se afirma que todos los tensores sean puros.

## 40.5. Bilinealidad y generación

### Proposición 40.5.1 — Bilinealidad y generación por tensores puros {#talg-pro-00121}

La aplicación $\tau_{U,V}$ es bilineal. Para $a\in F$,
$$
\begin{aligned}
(u+u')\otimes v&=u\otimes v+u'\otimes v,\\
(au)\otimes v&=a(u\otimes v),\\
u\otimes(v+v')&=u\otimes v+u\otimes v',\\
u\otimes(av)&=a(u\otimes v).
\end{aligned}
$$
En particular $0\otimes v=u\otimes0=0$, y
$$
(au)\otimes v=u\otimes(av).
$$
Todo tensor es una combinación lineal finita de tensores puros. Una aplicación lineal que sale de $U\otimes_F V$ queda determinada por sus valores en los tensores puros. Si $U=0$ o $V=0$, el producto tensorial es el espacio cero.

#### Demostración {#talg-prf-00194}

Cada generador de las cuatro familias de [§40.1](#talg-def-00081) pertenece a $R_F(U,V)=\ker q_{R_F(U,V)}$. Aplicar la proyección lineal al generador de $\mathcal R_1$ da
$$
q(\delta_{(u+u',v)})-q(\delta_{(u,v)})-q(\delta_{(u',v)})=0,
$$
que es la primera identidad. Aplicarla a los generadores de $\mathcal R_2,\mathcal R_3,\mathcal R_4$ da, respectivamente, la segunda, tercera y cuarta. Estas son exactamente las cuatro leyes de bilinealidad. Poner $a=0$ en las leyes homogéneas prueba las identidades con cero. Las dos leyes homogéneas tienen el mismo lado derecho, lo que prueba el traslado del escalar.

Sea $t$ un elemento del cociente. Por sobreyectividad existe localmente $x\in E_F(U,V)$ con $q(x)=t$. La [expansión canónica de soporte finito del espacio libre](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00114) da
$$
x=\sum_{(u,v)\in D}x(u,v)\delta_{(u,v)}
$$
para algún conjunto finito $D$. La linealidad de $q$ implica
$$
t=\sum_{(u,v)\in D}x(u,v)(u\otimes v).
$$
No se selecciona simultáneamente un representante para cada tensor. Si dos aplicaciones lineales coinciden en cada tensor puro, conservan esta suma y coinciden en $t$; Extensionalidad prueba su igualdad.

Si $U=0$, todo puro tiene primer factor cero, luego es cero. La generación recién probada muestra que todo tensor es cero. Para $V=0$ se usa el segundo factor. Se incluyen sumas vacías. $\square$

## 40.6. Propiedad universal

### Teorema 40.6.1 — Propiedad universal del producto tensorial {#talg-thm-00044}

Para cualquier espacio $W$ sobre $F$ y aplicación bilineal $\beta:U\times V\to W$, existe una única aplicación lineal
$$
\widehat\beta:U\otimes_F V\longrightarrow W
$$
tal que $\widehat\beta(u\otimes v)=\beta(u,v)$ para todo $u,v$, es decir,
$$
\widehat\beta\circ\tau_{U,V}=\beta.
$$
En consecuencia, la función
$$
\Phi_W:\mathcal L_F(U\otimes_F V,W)\longrightarrow
\operatorname{Bil}_F(U,V;W),\qquad
T\longmapsto T\circ\tau_{U,V}
$$
es un isomorfismo vectorial. No se presupone una base de $U$ o de $V$.

#### Demostración {#talg-prf-00195}

Apliquemos el [Teorema 36.4.1](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-thm-00038) al espacio libre sobre $U\times V$ y a la función dada $\beta$. Obtenemos una única aplicación lineal $L:E_F(U,V)\to W$ con
$$
L(\delta_{(u,v)})=\beta(u,v).
$$
Para un generador de $\mathcal R_1$,
$$
L(\delta_{(u+u',v)}-\delta_{(u,v)}-\delta_{(u',v)})
=\beta(u+u',v)-\beta(u,v)-\beta(u',v)=0.
$$
En $\mathcal R_2$, el valor es $\beta(au,v)-a\beta(u,v)=0$; en $\mathcal R_3$, $\beta(u,v+v')-\beta(u,v)-\beta(u,v')=0$; en $\mathcal R_4$, $\beta(u,av)-a\beta(u,v)=0$. Así $\mathcal R_F(U,V)\subseteq\ker L$. El [núcleo es subespacio](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113) y la propiedad mínima del span implica $R_F(U,V)\subseteq\ker L$.

La factorización lineal del [Teorema 37.3.1](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md#talg-thm-00040) produce $\widehat\beta$ sobre el cociente, con $\widehat\beta\circ q=L$. Esta aplicación ya está bien definida sobre clases por ese teorema, antes de utilizarla. Al evaluar en $\delta_{(u,v)}$ se obtiene la identidad requerida. Si $S$ es otra aplicación lineal con esos valores, coincide con $\widehat\beta$ en los tensores puros; la [Proposición 40.5.1](#talg-pro-00121) da $S=\widehat\beta$.

Para cualquier $T$ lineal, $T\circ\tau_{U,V}$ es bilineal: aplicar $T$ a cada una de las cuatro identidades de [§40.5](#talg-pro-00121) conserva suma y escalares. Por tanto $\Phi_W$ tiene el codominio anunciado. La existencia anterior da sobreyectividad de $\Phi_W$, y la unicidad da inyectividad. Además,
$$
\Phi_W(S+T)(u,v)=S(u\otimes v)+T(u\otimes v),\qquad
\Phi_W(aT)(u,v)=aT(u\otimes v).
$$
Son las identidades de linealidad para las estructuras puntuales ya certificadas en [§§37.5](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md#talg-pro-00116) y [38.2](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md#talg-pro-00118). Así $\Phi_W$ es lineal y biyectiva, y su inversa es lineal por la [Proposición 36.2.1](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113). $\square$

## 40.7. Unicidad del objeto universal

### Teorema 40.7.1 — Unicidad hasta isomorfismo compatible {#talg-thm-00045}

Sea $X$ un espacio sobre $F$ y $\sigma:U\times V\to X$ una aplicación bilineal con la siguiente propiedad: para todo espacio $W$ y todo mapa bilineal $\beta:U\times V\to W$ existe un único mapa lineal $A:X\to W$ con $A\circ\sigma=\beta$. Entonces existe un único isomorfismo lineal
$$
I:U\otimes_F V\longrightarrow X,\qquad I\circ\tau_{U,V}=\sigma.
$$
La unicidad corresponde al isomorfismo que respeta las aplicaciones canónicas; no es una igualdad literal de los conjuntos subyacentes.

#### Demostración {#talg-prf-00196}

La propiedad universal de $U\otimes_F V$, aplicada a $\sigma$, da un mapa lineal $I$ con $I\circ\tau=\sigma$. La propiedad supuesta de $(X,\sigma)$, aplicada a $\tau$, da un mapa lineal $J:X\to U\otimes_F V$ con $J\circ\sigma=\tau$.

Las composiciones son lineales y cumplen
$$
(J\circ I)\circ\tau=\tau,\qquad
(I\circ J)\circ\sigma=\sigma.
$$
También las identidades de los dos espacios cumplen estas ecuaciones. La unicidad en cada propiedad universal fuerza
$$
J\circ I=\operatorname{id}_{U\otimes_F V},\qquad
I\circ J=\operatorname{id}_X.
$$
Así $I$ es biyectivo, con inversa lineal $J$. Cualquier isomorfismo compatible es, en particular, un mapa lineal que factoriza $\sigma$ a través de $\tau$, y coincide con $I$ por la misma unicidad. $\square$

## 40.8. Mapas inducidos

### Proposición 40.8.1 — Mapas tensoriales inducidos {#talg-pro-00122}

Para mapas lineales $f:U\to U'$ y $g:V\to V'$ sobre $F$, existe un único mapa lineal
$$
f\otimes_F g:U\otimes_F V\longrightarrow U'\otimes_F V'
$$
con
$$
(f\otimes_F g)(u\otimes v)=f(u)\otimes g(v).
$$
La notación designa ahora un mapa lineal, y sus dominios distinguen este uso del tensor de vectores. Para $f':U'\to U''$ y $g':V'\to V''$,
$$
(f'\circ f)\otimes_F(g'\circ g)
=(f'\otimes_F g')\circ(f\otimes_F g).
$$
También $\operatorname{id}_U\otimes_F\operatorname{id}_V
=\operatorname{id}_{U\otimes_F V}$. Si $f$ y $g$ son isomorfismos, $f\otimes_F g$ lo es y su inversa es $f^{-1}\otimes_F g^{-1}$.

#### Demostración {#talg-prf-00197}

La función $(u,v)\mapsto f(u)\otimes g(v)$ existe como compuesto de funciones dadas. En la primera variable, la aditividad de $f$ y la bilinealidad de $\tau_{U',V'}$ dan
$$
f(u+u')\otimes g(v)=f(u)\otimes g(v)+f(u')\otimes g(v),
$$
y $f(au)\otimes g(v)=a(f(u)\otimes g(v))$. En la segunda variable se obtienen las dos leyes restantes usando $g$. Es bilineal, y el [Teorema 40.6.1](#talg-thm-00044) proporciona el mapa lineal único anunciado.

Los dos lados de la fórmula de composición, evaluados en $u\otimes v$, dan $f'(f(u))\otimes g'(g(v))$. Ambos son lineales, luego la generación por puros prueba su igualdad. El mismo argumento prueba la fórmula para identidades. Si ambos mapas son isomorfismos, sus inversas son lineales, y las fórmulas ya probadas muestran que $f^{-1}\otimes_F g^{-1}$ es inversa por ambos lados. $\square$

## 40.9. Bases dadas y cálculos finitos

### Teorema 40.9.1 — Base tensorial a partir de bases dadas {#talg-thm-00046}

Sean $B\subseteq U$ y $C\subseteq V$ bases dadas. La familia
$$
(b\otimes c)_{(b,c)\in B\times C}
$$
es independiente y genera $U\otimes_F V$; por tanto su imagen es una base. Para las funciones de coordenadas de soporte finito,
$$
u\otimes v=\sum_{b\in B}\sum_{c\in C}a_u(b)a_v(c)(b\otimes c),
$$
donde sólo se suman sobre soportes finitos. Si $B$ o $C$ es vacío, la base tensorial es vacía y el producto es cero. Cuando $U,V$ tienen dimensión finita,
$$
\dim(U\otimes_F V)=\dim U\,\dim V.
$$
Las bases arbitrarias se suponen dadas; no se obtiene aquí su existencia.

#### Demostración {#talg-prf-00198}

La expansión bilineal de [§38.2](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md#talg-pro-00118), aplicada a $\tau$, da la fórmula de coordenadas. Cada tensor es suma finita de puros por [§40.5](#talg-pro-00121), y cada puro se expande así en la familia indicada. Por tanto esa familia genera.

Para independencia fijemos una pareja $(b_0,c_0)\in B\times C$. La función dada
$$
h_{b_0,c_0}:B\times C\to F,\qquad
h_{b_0,c_0}(b,c)=
\begin{cases}
1_F,&(b,c)=(b_0,c_0),\\
0_F,&(b,c)\ne(b_0,c_0)
\end{cases}
$$
existe por Separación y la disyunción clásica de igualdad de índices; no se atribuye decidibilidad efectiva. El [Teorema 38.3.1](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md#talg-thm-00042) la extiende a una forma bilineal $\beta_{b_0,c_0}:U\times V\to F$. El [Teorema 40.6.1](#talg-thm-00044) da el mapa lineal $\widehat\beta_{b_0,c_0}$ cuyo valor en $b\otimes c$ es $h_{b_0,c_0}(b,c)$.

En una relación finita con parejas distintas,
$$
\sum_{k<n}\lambda_k(b_k\otimes c_k)=0,
$$
aplicar $\widehat\beta_{b_j,c_j}$ deja exactamente $\lambda_j=0$. Esto prueba independencia. Además, evaluar uno de estos mapas muestra que cada vector de la familia es no nulo; evaluar en una pareja distingue su tensor del de cualquier pareja diferente. Por ello la imagen no tiene repeticiones y es una base en el sentido de [§34.1](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-def-00073).

Si una base es vacía, su espacio está generado por la suma vacía y es cero; [§40.5](#talg-pro-00121) da el producto cero y la base vacía. Para bases finitas de longitudes $r,s$, las parejas se enumeran mediante $s$ bloques de $r$ elementos, sin repeticiones. Su número satisface $N(r,0)=0$ y $N(r,s+1)=N(r,s)+r$, las [ecuaciones recursivas del producto natural](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006) $rs$. La dimensión, definida como la longitud de una base finita, vale entonces $rs$. $\square$

## 40.99. Síntesis

El cociente del espacio libre impone las cuatro relaciones de bilinealidad. Los tensores puros generan, pero esa afirmación no identifica generación con descomponibilidad. La propiedad universal permite factorizar mapas bilineales sin escoger bases ni representantes. La unicidad del objeto universal es una isomorfía compatible; los mapas inducidos y las bases dadas se deducen después.

El caso cero queda incluido. Para dimensiones finitas, el conteo es un producto de longitudes de bases; para bases infinitas dadas sólo se afirman generación e independencia, sin dimensión cardinal. Todo uso clásico nuevo se limita a funciones delta por igualdad de índices, además de los usos ya declarados en las dependencias. No se usa el axioma de elección ni la rama de Zorn del capítulo 34.

---

[← **Capítulo 39 — Multilinealidad y formas**](tratado-de-algebra-capitulo-39-multilinealidad-y-formas.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
