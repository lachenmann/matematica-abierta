---
title: 'Tratado moderno de Álgebra — Capítulo 34: Independencia lineal y bases'
description: Independencia lineal, coordenadas de soporte finito, extracción y extensión finitas de bases y existencia general bajo la hipótesis adicional de Zorn.
author: Gustav A. Tachek
content-id: MA-BCH-0142
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
- independencia-lineal
- bases
- soporte-finito
- coordenadas
- lema-de-zorn
prerequisites:
- MA-BCH-0141
- MA-BCH-0140
- MA-BCH-0047
- MA-BCH-0050
- MA-BCH-0136
related:
- MA-BOK-0007
- MA-BCH-0141
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 34 — Independencia lineal y bases

## 34.0. Propósito y posición deductiva

Generar proporciona expresiones; la independencia controla su unicidad. Se distinguen listas finitas, familias arbitrarias con combinaciones finitas y bases como conjuntos.

Trabajamos en un [espacio vectorial](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-def-00070) $V$ sobre un [cuerpo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) $F$. Las [sumas finitas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) y el [subespacio generado](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-def-00072) ya están disponibles.

El marco fundacional es ZF con lógica clásica. La [extracción y extensión finitas](#talg-pro-00111) se demuestran en ese marco. La existencia de una base para un espacio arbitrario se formula en una [rama condicionada a Zorn](#talg-cnv-00001), cuya hipótesis adicional aparece expresamente en el [Teorema 34.5.1](#talg-thm-00036). Los usos clásicos sobre coeficientes y pertenencia al span se declaran en las pruebas.

---

## 34.1. Independencia, base y coeficientes de soporte finito

### Definición 34.1.1 — Independencia, base y coeficientes de soporte finito {#talg-def-00073}

Una familia $(v_i)_{i\in I}$ es **linealmente independiente** si, para cada lista finita de índices distintos $i_0,\ldots,i_{n-1}$ y escalares $a_0,\ldots,a_{n-1}$,
$$
\sum_{k<n}a_kv_{i_k}=0_V\Longrightarrow \forall k<n,\ a_k=0_F.
$$
Una relación con algún coeficiente no nulo se llama relación de dependencia. En lógica clásica, una familia no independiente posee tal relación; este paso lógico se declarará al utilizarlo. Una lista finita se trata como familia indexada por sus posiciones. Para un conjunto $B\subseteq V$, la familia es la inclusión $b\mapsto b$.

Una **base** de $V$ es un conjunto independiente $B\subseteq V$ tal que $\operatorname{span}(B)=V$. Una lista base es una lista independiente y generadora. El conjunto vacío es independiente por la condición vacua y genera exactamente el espacio cero.

Para un conjunto $I$, definimos
$$
F^{(I)}=\{a:I\to F:\exists E\subseteq I,\ E\text{ finito},\
\forall i\notin E,\ a(i)=0_F\}.
$$
«Finito» significa que existe una biyección con un conjunto de índices de longitud natural. Este conjunto existe por Separación en [$F^I$](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-pro-00108). Para una familia $(v_i)$ y $a\in F^{(I)}$ se escribirá $\sum_{i\in I}a(i)v_i$ como suma sobre un testigo finito $E$; la independencia de ese testigo se comprobará en el [lema siguiente](#talg-lem-00009). No se confunde $F^{(I)}$ con el espacio de todas las funciones $F^I$.

## 34.2. Eliminación, adjunción y unicidad de coordenadas

### [Lema 34.2.1](#talg-lem-00009) — Eliminación, adjunción y unicidad de coordenadas {#talg-lem-00009}

Si una lista $(v_i)_{i<n}$ tiene una relación $\sum_i a_iv_i=0$ con $a_j\ne0$, $v_j$ pertenece al span de los demás y puede retirarse sin cambiar el span. Si $A$ es independiente y $v\notin\operatorname{span}(A)$, $A\cup\{v\}$ es independiente.

La suma $\sum_i a(i)v_i$ para $a\in F^{(I)}$ es independiente del testigo finito de soporte. Para $B\subseteq V$ existe la función de evaluación
$$
E_B:F^{(B)}\to V,\qquad E_B(a)=\sum_{b\in B}a(b)b.
$$
Es inyectiva exactamente cuando $B$ es independiente, y sobreyectiva exactamente cuando $B$ genera $V$. Por tanto, si $B$ es base, cada vector tiene una única función de coordenadas de soporte finito sobre $B$, sin elección de representaciones.

#### Demostración {#talg-prf-00174}

**Eliminación.** Reordenando la relación para separar el índice $j$, se obtiene $a_jv_j+\sum_{i\ne j}a_iv_i=0$. Sumando el opuesto de la segunda suma y aplicando $a_j^{-1}$,
$$
v_j=-a_j^{-1}\sum_{i\ne j}a_iv_i
=\sum_{i\ne j}(-a_j^{-1}a_i)v_i.
$$
Así $v_j$ está en el span de los demás. Ese span contiene toda la lista y por [minimalidad](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-pro-00110) contiene su span; la inclusión recíproca se sigue de monotonía. Retirar el término no cambia la generación.

**Adjunción.** Como $A$ está contenido en su span, $v\notin A$. En una relación finita de vectores distintos de $A\cup\{v\}$, si no aparece $v$ se aplica independencia de $A$. Si aparece, reordenamos para escribir $av+\sum_k a_ku_k=0$, con $u_k\in A$. Usamos explícitamente $a=0$ o $a\ne0$. La segunda alternativa daría por eliminación $v\in\operatorname{span}(A)$, contradicción. Por tanto $a=0$, y la independencia de $A$ obliga a que los demás coeficientes sean cero. La familia ampliada es independiente.

**Soportes.** Si $E,E'$ son dos testigos finitos para una función $a$, su unión es finita por el [lema de sumas](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008). Enumeremos localmente la unión y reordenémosla en los elementos de $E$ y los restantes. En los restantes $a(i)=0$, de modo que añadirlos no altera la suma. Esto muestra que la suma sobre $E$ coincide con la de la unión; el mismo argumento escrito para $E'$ añade sólo términos cero fuera de $E'$, por lo que también coincide con la de la unión. Las dos sumas son iguales. Las descomposiciones de la unión usan casos clásicos finitos de pertenencia. Para cada $a$, el valor es único; el grafo de $E_B$ existe por Separación en $F^{(B)}\times V$.

**Inyectividad desde independencia.** Si $E_B(a)=E_B(c)$, tomemos localmente soportes finitos y su unión $D$. La [distributividad finita](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) da $\sum_{b\in D}(a(b)-c(b))b=0$. Enumerando $D$ sin repeticiones, independencia implica $a(b)=c(b)$ para $b\in D$. Fuera de $D$ ambas funciones valen cero; Extensionalidad funcional da $a=c$.

**Independencia desde inyectividad.** Para una relación sobre vectores distintos $b_0,\ldots,b_{n-1}\in B$, construyamos $a:B\to F$ con esos coeficientes en los índices indicados y cero fuera. Es función de soporte finito, y la relación dice $E_B(a)=0=E_B(0)$. Inyectividad da $a=0$, luego cada coeficiente es cero.

**Sobreyectividad y generación.** Cada valor de $E_B$ es una combinación finita de $B$, por lo que su imagen está en el span. Recíprocamente, para $v=\sum_{i<n}a_ib_i$ con posibles repeticiones, el conjunto finito $D$ de valores $b_i$ se obtiene eliminando repeticiones. Para $b\in D$ definimos el coeficiente como la suma de los $a_i$ con $b_i=b$, y fuera de $D$ lo hacemos cero. [Reagrupamiento y distributividad](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md#talg-lem-00008) prueban que la evaluación de esta función es $v$. Por tanto $\operatorname{im}E_B=\operatorname{span}(B)$, y queda probado el criterio de sobreyectividad.

Cuando $B$ es base, existencia y unicidad dan, para cada $v$, una sola función $a_v\in F^{(B)}$. El grafo $\{(v,a):E_B(a)=v\}$ es una función inversa por Separación. Ningún principio de elección se necesita para invertir una biyección. No se afirma un algoritmo para encontrar sus valores. $\square$

## 34.3. Extracción y extensión finitas de bases

### Proposición 34.3.1 — Extracción y extensión finitas de bases {#talg-pro-00111}

Si una lista finita genera $V$, puede extraerse de ella una lista base. Más generalmente, cualquier lista independiente finita $(u_0,\ldots,u_{r-1})$ de $V$ puede extenderse a una lista base añadiendo algunos elementos de una lista generadora finita dada. Se conserva el orden de los vectores originales. El espacio cero tiene la base vacía.

#### Demostración {#talg-prf-00175}

Sea $(w_0,\ldots,w_{m-1})$ la lista generadora y comencemos con la lista independiente $U_0=(u_0,\ldots,u_{r-1})$. Construimos, por [inducción finita](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006) sobre $k\le m$, una lista independiente $U_k$ que comienza con la lista original y cuyo span contiene $w_0,\ldots,w_{k-1}$.

El caso $k=0$ es la lista dada. Supongamos construido $U_k$. Usamos explícitamente la disyunción clásica
$$
w_k\in\operatorname{span}(U_k)\quad\text{o}\quad
w_k\notin\operatorname{span}(U_k).
$$
En la primera rama, pongamos $U_{k+1}=U_k$. En la segunda, añadamos $w_k$ al final; la adjunción del [Lema 34.2.1](#talg-lem-00009) prueba independencia. En ambas ramas, el nuevo span contiene el anterior y contiene $w_k$. Esto cumple el paso inductivo. Se trata de una inducción finita de existencias locales; no se escoge un vector de cada miembro de una familia arbitraria y no se supone decidible pertenecer al span.

Al terminar, $\operatorname{span}(U_m)$ contiene toda la lista generadora; por minimalidad del span contiene $V$, y como sus vectores están en $V$, es exactamente $V$. La lista es independiente, luego es base y extiende la inicial.

Para extraer de la lista generadora, se comienza con la lista vacía, independiente por definición. Sólo se añaden elementos de la lista dada, de modo que el resultado es una sublista y es base. Si $V=\{0_V\}$, su span vacío ya es $V$ y ningún vector necesita añadirse. La base vacía satisface ambas condiciones. $\square$

## 34.4. Rama condicional de Zorn

### Convención fundacional 34.4.1 — Rama condicional de Zorn {#talg-cnv-00001}

Se establece una rama condicional con el siguiente principio adicional:

**Zorn.** Si $(P,\le)$ es un [conjunto parcialmente ordenado](tratado-de-algebra-capitulo-25-grupos-ordenados.md#talg-imp-00004) habitado y toda cadena $C\subseteq P$ posee una cota superior en $P$, entonces $P$ posee un elemento maximal. Una cadena es un subconjunto donde dos elementos cualesquiera son comparables. Una cota superior $u$ satisface $c\le u$ para todo $c\in C$. Un elemento $m$ es maximal si $m\le p$ implica $p=m$.

Este principio se asume únicamente en resultados cuyo enunciado declare «bajo Zorn». No se afirma que se deduzca de ZF. Esta convención fija una hipótesis adicional y su frontera de uso. En particular, los resultados finitos anteriores y los resultados sobre una base dada conservan su fundamento ZF.

## 34.5. Existencia y extensión de bases bajo Zorn

### Teorema 34.5.1 — Existencia y extensión de bases bajo Zorn {#talg-thm-00036}

**Bajo la hipótesis adicional de Zorn**, todo subconjunto independiente $I\subseteq V$ está contenido en una base de $V$. En particular, todo espacio vectorial posee una base bajo esa hipótesis. No se deduce aquí la afirmación incondicional en ZF ni se obtiene un método efectivo de construcción.

#### Demostración {#talg-prf-00176}

Sea
$$
\mathscr P=\{A\subseteq V:I\subseteq A,\ A\text{ independiente}\}
$$
ordenado por inclusión. Este conjunto existe por Potencia y Separación, y está habitado por $I$. La inclusión es un orden parcial por reflexividad, transitividad y Extensionalidad.

Sea $\mathscr C$ una cadena en $\mathscr P$. Si es vacía, $I$ es cota superior. Si está habitada, definamos $A=\bigcup\mathscr C$. Contiene $I$, pues cualquiera de los miembros de la cadena contiene $I$. Para verificar independencia, consideremos una relación sobre un número finito de elementos distintos de $A$. Cada uno pertenece a algún miembro de la cadena. Se demuestra por inducción finita que todos pertenecen a un solo miembro: para un primer elemento se utiliza un miembro local que lo contiene; si un miembro $D$ contiene los primeros $k$ y otro $E$ contiene el siguiente, la comparabilidad de la cadena da $D\subseteq E$ o $E\subseteq D$, y el mayor de esos dos contiene los $k+1$. La relación vacía no exige seleccionar miembro. En la relación no vacía resultante, la independencia de ese miembro obliga a que cada coeficiente sea cero. Así $A$ es independiente y pertenece a $\mathscr P$; por definición de unión es cota superior de la cadena.

Se satisfacen las hipótesis del [principio adicional de Zorn](#talg-cnv-00001). Por él existe un miembro maximal $B\in\mathscr P$. Para cada $v\in V$, usemos explícitamente $v\in\operatorname{span}(B)$ o $v\notin\operatorname{span}(B)$. En la segunda rama, el [Lema 34.2.1](#talg-lem-00009) certifica que $B\cup\{v\}$ es independiente. Contiene $I$ y estrictamente contiene $B$, porque $B\subseteq\operatorname{span}(B)$ implica $v\notin B$. Esto contradice maximalidad. Por tanto todos los vectores están en el span de $B$, y $B$ es base.

Tomando $I=\varnothing$, independiente por definición, se obtiene una base de cualquier $V$, incluido el espacio cero. El único uso adicional de elección es la aplicación declarada de Zorn. Los testigos para una relación finita en la cadena se utilizan mediante inducción finita de existencias locales, sin una selección global previa de miembros de cadenas. $\square$

---

## 34.99. Síntesis

Independencia convierte las representaciones finitas en coordenadas únicas. La existencia de bases finitas se obtuvo recorriendo una lista generadora; la existencia general queda expresamente condicionada a Zorn. La [dimensión natural del capítulo siguiente](tratado-de-algebra-capitulo-35-dimension-finita.md) se construirá desde intercambio finito y no dependerá de la rama de Zorn.

---

[← **Capítulo 33 — Subespacios y generación**](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md) · [**Capítulo 35 — Dimensión finita →**](tratado-de-algebra-capitulo-35-dimension-finita.md)
