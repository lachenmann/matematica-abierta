---
title: 'Tratado moderno de Álgebra — Capítulo 38: Aplicaciones bilineales'
description: Bilinealidad, operaciones puntuales, expansión finita, ejemplos y especificación única por valores sobre dos bases dadas.
author: Gustav A. Tachek
content-id: MA-BCH-0146
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
- bilinealidad
- formas-bilineales
- bases
- soporte-finito
prerequisites:
- MA-BCH-0145
- MA-BCH-0144
- MA-BCH-0142
- MA-BCH-0141
- MA-BCH-0140
- MA-BCH-0047
- MA-BCH-0021
related:
- MA-BOK-0007
- MA-BCH-0145
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 38 — Aplicaciones bilineales

## 38.0. Propósito y posición deductiva

La bilinealidad exige [linealidad](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-def-00075) en cada entrada por separado. El objetivo es controlar combinaciones en ambas variables, construir [ejemplos](#talg-pro-00118) y demostrar que los valores sobre parejas de vectores de [bases dadas](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-def-00073) [determinan toda la aplicación](#talg-thm-00042). No se usa bilineal como sinónimo de lineal en el producto.

El marco fundacional es ZF. La lógica clásica se declara al comparar índices de soportes finitos; no se presupone igualdad decidible. Las coordenadas únicas y las [sumas finitas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) permiten construir la aplicación a partir de dos bases dadas, que pueden ser infinitas. No se invoca Zorn ni se afirma la existencia de bases arbitrarias.

---

## 38.1. Aplicación y forma bilineales

### Definición 38.1.1 — Aplicación y forma bilineales {#talg-def-00078}

Para [espacios](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-def-00070) $U,V,W$ sobre el mismo cuerpo $F$, una función $\beta:U\times V\to W$ es **bilineal** si, para cada $v$, $u\mapsto\beta(u,v)$ es [lineal](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-def-00075) y, para cada $u$, $v\mapsto\beta(u,v)$ es lineal. Es decir, conserva suma y acción escalar en cada variable mientras la otra permanece fija. Si $W=F$, se llama **forma bilineal**.

Escribimos $\operatorname{Bil}_F(U,V;W)$ para el conjunto de tales funciones, existente por Separación en el conjunto de funciones $U\times V\to W$. La linealidad conjunta sobre el espacio producto no forma parte de la definición. La forma cero es bilineal porque sus dos restricciones son [funciones lineales cero](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113).

## 38.2. Operaciones, expansión finita y ejemplos bilineales

### Proposición 38.2.1 — Operaciones, expansión finita y ejemplos bilineales {#talg-pro-00118}

Sean $U,V,W$ espacios sobre el mismo [cuerpo conmutativo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) $F$. Si $\beta:U\times V\to W$ es bilineal, entonces
$$
\beta(0,v)=\beta(u,0)=0,\qquad
\beta(-u,v)=\beta(u,-v)=-\beta(u,v),
$$
y para combinaciones finitas, incluidas las vacías,
$$
\beta\!\left(\sum_i a_i u_i,\sum_j b_j v_j\right)
=\sum_i\sum_j a_i b_j\,\beta(u_i,v_j).
$$
El conjunto $\operatorname{Bil}_F(U,V;W)$, con suma y multiplicación escalar puntuales, es un espacio vectorial. Son bilineales la multiplicación $F\times F\to F$, la pareja coordenada $(x,y)\mapsto\sum_{i<n}x_i y_i$ sobre $F^n$, y la evaluación $(T,v)\mapsto T(v)$ sobre $\mathcal L_F(V,W)\times V$.

#### Demostración {#talg-prf-00189}

Con una variable fijada, las identidades de cero, opuesto y [sumas finitas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) son las de una [aplicación lineal](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-def-00075). Aplicarlas primero a la primera variable y luego a la segunda da la expansión; la conmutatividad del cuerpo permite escribir $a_i b_j$. Si un índice es vacío, la suma es cero y la identidad sigue siendo válida.

Para $\beta,\gamma$ bilineales, cada sección de $\beta+\gamma$ es [suma de secciones lineales](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113), y cada sección de $a\beta$ es un múltiplo de una sección lineal. El mapa cero es bilineal. Las leyes del espacio se verifican en cada pareja $(u,v)$ mediante las leyes de $W$; la extensionalidad de funciones cierra cada igualdad.

La distributividad y la compatibilidad escalar del cuerpo prueban la bilinealidad de la multiplicación. La suma finita de los productos coordenados conserva esas dos propiedades en cada variable; para $n=0$ es el mapa cero. Para la [evaluación](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md#talg-pro-00116),
$$
(T+S)(v)=T(v)+S(v),\quad (aT)(v)=aT(v),
$$
mientras que $T(v+v')=T(v)+T(v')$ y $T(av)=aT(v)$. Estas cuatro igualdades prueban la afirmación.

## 38.3. Especificación bilineal sobre dos bases dadas

### Teorema 38.3.1 — Especificación bilineal sobre dos bases dadas {#talg-thm-00042}

Sean $B\subseteq U$ y $C\subseteq V$ [bases dadas](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-def-00073), y sea $h:B\times C\to W$ una función dada. Existe una única aplicación bilineal $\beta:U\times V\to W$ tal que $\beta(b,c)=h(b,c)$ para $b\in B,c\in C$.

Si $u=\sum_{b\in B}a_u(b)b$ y $v=\sum_{c\in C}a_v(c)c$ son sus coordenadas de soporte finito, entonces
$$
\beta(u,v)=\sum_{b\in\operatorname{supp}(a_u)}
 \sum_{c\in\operatorname{supp}(a_v)}
 a_u(b)a_v(c)h(b,c).
$$
Las bases pueden ser infinitas. No se afirma aquí su existencia.

#### Demostración {#talg-prf-00190}

Las coordenadas de cada vector existen y son únicas por la [propiedad de base](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-lem-00009). Por tanto, definen funciones $u\mapsto a_u$, $v\mapsto a_v$ mediante sus valores únicos; no se selecciona una representación entre varias. Los soportes son finitos y sus productos son finitos. Las sumas no dependen de la enumeración, por [permutación y reagrupamiento de sumas finitas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008); agregar índices con coeficiente cero tampoco altera el resultado.

Las coordenadas satisfacen $a_{u+u'}=a_u+a_{u'}$ y $a_{\lambda u}=\lambda a_u$, pues los lados derechos representan los vectores respectivos y la representación es única. Al calcular sobre la unión finita de los soportes, la distributividad demuestra aditividad y compatibilidad escalar en la primera variable. El mismo argumento en la segunda variable prueba la bilinealidad. Para $b\in B$, sus coordenadas son uno en $b$ y cero en los demás índices; análogamente para $c\in C$. La fórmula da $h(b,c)$.

Toda aplicación bilineal con esos valores debe satisfacer la [expansión finita de la proposición anterior](#talg-pro-00118). Al expandir las coordenadas de $u,v$, se obtiene exactamente la fórmula construida. Esto prueba unicidad, también cuando una base es vacía y su espacio es cero.

## 38.99. Síntesis

La bilinealidad se comprueba por secciones lineales y se calcula por expansión finita. Los valores sobre parejas de bases dadas permiten construir una única aplicación; no se añade ningún principio de existencia de bases. La [multilinealidad](tratado-de-algebra-capitulo-39-multilinealidad-y-formas.md) extiende este procedimiento a un número positivo y finito de entradas.

---

[← **Capítulo 37 — Cocientes y dualidad elemental**](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md) · [**Capítulo 39 — Multilinealidad y formas →**](tratado-de-algebra-capitulo-39-multilinealidad-y-formas.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
