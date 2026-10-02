---
title: 'Tratado moderno de Álgebra — Capítulo 39: Multilinealidad y formas'
description: Aplicaciones multilineales de aridad positiva y finita, especificación por bases dadas, formas simétricas y alternantes, y la excepción de característica dos.
author: Gustav A. Tachek
content-id: MA-BCH-0147
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
- multilinealidad
- formas-simetricas
- formas-alternantes
- caracteristica-dos
- soporte-finito
prerequisites:
- MA-BCH-0146
- MA-BCH-0145
- MA-BCH-0144
- MA-BCH-0142
- MA-BCH-0141
- MA-BCH-0140
- MA-BCH-0047
- MA-BCH-0021
related:
- MA-BOK-0007
- MA-BCH-0146
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 39 — Multilinealidad y formas

## 39.0. Propósito y posición deductiva

Se trabaja con un número positivo y finito de entradas. Se generaliza la [expansión bilineal](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md#talg-pro-00118), y se distinguen [simetría, alternancia y cambio de signo](#talg-def-00080) sobre [cuerpos](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) de cualquier característica.

La [especificación multilineal](#talg-thm-00043) se apoya en las [sumas finitas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) y en la unicidad de coordenadas sobre [bases dadas](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-def-00073). Las [operaciones puntuales](tratado-de-algebra-capitulo-37-cocientes-y-dualidad-elemental.md#talg-pro-00116) permiten construir el espacio de mapas. La recíproca que deduce alternancia del cambio de signo requiere $2_F\neq0_F$; la [excepción de característica dos](#talg-pro-00119) se demuestra con un contraejemplo.

El marco fundacional es ZF, con lógica clásica explícita para las comparaciones de índices y las distinciones de casos. No se presupone igualdad decidible ni se invoca Zorn.

---

## 39.1. Aplicaciones multilineales y formas

### Definición 39.1.1 — Aplicaciones multilineales y formas {#talg-def-00079}

Sea $k\geq1$ un natural, sean $V_1,\ldots,V_k,W$ [espacios](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-def-00070) sobre un mismo [cuerpo conmutativo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) $F$. Una función
$$
M:V_1\times\cdots\times V_k\longrightarrow W
$$
es **$k$-lineal** o multilineal si, para cada posición $r$, al fijar todas las entradas distintas de la $r$-ésima, la función restante $V_r\to W$ es lineal. Si $W=F$, se llama **forma multilineal**. Para $k=1$ es una [aplicación lineal](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-def-00075); para $k=2$, una [aplicación bilineal](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md#talg-def-00078).

Escribimos $\operatorname{Mult}_F(V_1,\ldots,V_k;W)$ para el conjunto de estas funciones, obtenido por separación del conjunto de funciones entre los conjuntos indicados. Cada producto tiene un número finito de factores. El caso $k=0$ queda fuera de esta definición.

## 39.2. Expansión y especificación multilineales

### Teorema 39.2.1 — Expansión y especificación multilineales {#talg-thm-00043}

Para una aplicación $k$-lineal $M$, se tiene la expansión finita
$$
M\!\left(\sum_{i_1}a_{1,i_1}v_{1,i_1},\ldots,
 \sum_{i_k}a_{k,i_k}v_{k,i_k}\right)
=\sum_{i_1}\cdots\sum_{i_k}
 \left(\prod_{r=1}^{k}a_{r,i_r}\right)
 M(v_{1,i_1},\ldots,v_{k,i_k}).
$$
Si alguna combinación es vacía, ambos lados son cero.

Dadas bases $B_r\subseteq V_r$ para cada $1\leq r\leq k$ y una función dada $h:B_1\times\cdots\times B_k\to W$, existe una única aplicación $k$-lineal que toma sobre las tuplas de bases los valores de $h$. El conjunto $\operatorname{Mult}_F(V_1,\ldots,V_k;W)$, con operaciones puntuales, es un espacio vectorial.

Si $\varphi_r:V_r\to F$ son funciones lineales dadas, el mapa $(v_1,\ldots,v_k)\mapsto\prod_{r=1}^k\varphi_r(v_r)$ es una forma multilineal.

#### Demostración {#talg-prf-00191}

Con todas las demás entradas fijadas, la linealidad permite expandir una combinación finita en la primera posición. Se repite en las posiciones segunda, tercera y sucesivas; la inducción sobre el número de posiciones procesadas da la fórmula. La asociatividad y conmutatividad del cuerpo permiten reunir los coeficientes en el producto indicado. Si una entrada es cero, la sección lineal en esa posición toma valor cero; esto cubre las combinaciones vacías.

Para la construcción sobre bases, sean $a_r$ las [coordenadas únicas y de soporte finito](tratado-de-algebra-capitulo-34-independencia-lineal-y-bases.md#talg-lem-00009) de $v_r$. Definimos
$$
M(v_1,\ldots,v_k)=
\sum_{b_1\in\operatorname{supp}(a_1)}\cdots
\sum_{b_k\in\operatorname{supp}(a_k)}
 \left(\prod_{r=1}^k a_r(b_r)\right)h(b_1,\ldots,b_k).
$$
El producto de soportes es finito: para un factor esto es inmediato, y añadir un factor finito equivale a una unión finita de conjuntos finitos. Las sumas son [independientes del orden](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) y de índices añadidos con coeficiente cero. Al sumar dos vectores en una posición, sus coordenadas se suman; al multiplicarlo por un escalar, sus coordenadas se multiplican por ese escalar. Calculando sobre la unión de los dos soportes en esa posición, la distributividad prueba las dos leyes de linealidad. En tuplas de bases se recupera $h$. La expansión ya probada obliga a cualquier otro mapa con esos valores a tener la misma fórmula. Las bases se reciben como datos, y las coordenadas se definen por unicidad; no hay selección de bases.

La suma y el múltiplo de dos mapas multilineales tienen secciones lineales porque [se suman o multiplican secciones lineales](tratado-de-algebra-capitulo-36-aplicaciones-lineales.md#talg-pro-00113). El mapa cero también pertenece al conjunto. Las leyes vectoriales son puntuales y se heredan de $W$. Finalmente, al fijar todas las entradas salvo una en el producto de las $\varphi_r$, los otros factores dan un escalar fijo; su producto con la función lineal restante es lineal.

## 39.3. Simetría, alternancia y cambio de signo

### Definición 39.3.1 — Simetría, alternancia y cambio de signo {#talg-def-00080}

Sea $M:V^k\to F$ una forma multilineal, con $k\geq1$. Es **simétrica** si
$$
M(v_{\sigma(1)},\ldots,v_{\sigma(k)})=M(v_1,\ldots,v_k)
$$
para toda permutación $\sigma$ de las $k$ posiciones. Es **alternante** si su valor es cero siempre que dos entradas en posiciones distintas sean iguales. Diremos que **cambia de signo bajo transposiciones** si intercambiar dos entradas en posiciones distintas reemplaza su valor por su opuesto.

Estas dos últimas condiciones se distinguen en la definición. Para $k=1$, las tres condiciones son vacías. Denotamos por $\operatorname{Sym}_F^k(V)$ y $\operatorname{Alt}_F^k(V)$ los subconjuntos de formas simétricas y alternantes, respectivamente.

## 39.4. Alternancia y la excepción de característica dos

### Proposición 39.4.1 — Alternancia y la excepción de característica dos {#talg-pro-00119}

Los conjuntos $\operatorname{Sym}_F^k(V)$ y $\operatorname{Alt}_F^k(V)$ son subespacios del espacio de formas multilineales.

Toda forma alternante cambia de signo bajo transposiciones. Si $2_F:=1_F+1_F\neq0_F$, la recíproca también vale. Si $2_F=0_F$, esa recíproca puede fallar: la forma bilineal $F\times F\to F,\ (x,y)\mapsto xy$ cambia de signo bajo la transposición, pero no es alternante.

#### Demostración {#talg-prf-00192}

El mapa cero satisface simetría y alternancia. Si dos formas son simétricas, evaluar su suma o un múltiplo después de permutar entradas da el mismo resultado que antes, por las igualdades correspondientes de cada forma. Si son alternantes, ambas valen cero ante entradas repetidas; su suma y sus múltiplos también. El [criterio de subespacio](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00109) se verifica directamente: las operaciones se realizan dentro del espacio multilineal ya construido.

Fijemos dos posiciones distintas y todas las demás entradas. Para una forma alternante, escribamos $M[\cdot,\cdot]$ para esas dos posiciones. La alternancia y la [bilinealidad en ellas](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md#talg-def-00078) dan
$$
0=M[u+v,u+v]
=M[u,u]+M[u,v]+M[v,u]+M[v,v]
=M[u,v]+M[v,u].
$$
Así $M[v,u]=-M[u,v]$. Esto sirve para cualquier pareja de posiciones y no divide por dos.

Recíprocamente, si cambiar esas posiciones da el opuesto y ambas entradas son $u$, el valor $z\in F$ satisface $z=-z$. Entonces $2_F z=0$. Bajo la hipótesis $2_F\neq0$, [su inverso existe en el cuerpo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-pro-00049) y da $z=0$. Esto demuestra alternancia para cualquier repetición.

Si $2_F=0$, todo $t\in F$ cumple $t+t=(1_F+1_F)t=0$, por lo que $-t=t$. La [multiplicación](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md#talg-pro-00118) es bilineal y conmutativa, de modo que intercambiar sus entradas conserva $xy=-xy$. Pero en $(1_F,1_F)$ vale $1_F\neq0_F$; por tanto no es alternante. Para $k=1$, ambas implicaciones se refieren a condiciones vacías.

## 39.99. Síntesis

La multilinealidad se obtiene imponiendo linealidad separada en un número positivo y finito de variables. La expansión sobre bases dadas sigue siendo finita, y la distinción entre simetría, alternancia y cambio de signo conserva explícitamente la excepción de característica dos. No se introduce todavía producto tensorial ni álgebra exterior.

---

[← **Capítulo 38 — Aplicaciones bilineales**](tratado-de-algebra-capitulo-38-aplicaciones-bilineales.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
