---
title: "Tratado de anÃ¡lisis â€” CapÃ­tulo 0: Fundamento lÃ³gico y conjuntista"
description: "Fundamento lÃ³gico y conjuntista del Tratado de anÃ¡lisis: conjuntos, relaciones, cocientes, funciones y Ã³rdenes construidos antes de los sistemas numÃ©ricos."
author: "Gustav A. Tachek"
content-id: MA-BCH-0005
content-type: book-chapter
book-id: MA-BOK-0003
status: published
date-created: 2026-09-09
date-modified: 2026-09-09
areas:
  - fundamentos
  - analisis
level: avanzado
topics:
  - logica-matematica
  - teoria-de-conjuntos
  - relaciones
  - relaciones-de-equivalencia
  - conjuntos-cociente
  - funciones
  - ordenes
prerequisites: []
related:
  - MA-BOK-0003
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# CapÃ­tulo 0 â€” Fundamento lÃ³gico y conjuntista

[**â† Volver al Tratado de anÃ¡lisis**](../otros/tratado-de-analisis.md)

*Parte I â€” Fundamentos y construcciÃ³n de los nÃºmeros reales*


---

## 0.0. PropÃ³sito y posiciÃ³n deductiva

Este capÃ­tulo fija el lenguaje conjuntista que se utilizarÃ¡ en todo el tratado. No pretende desarrollar metamatemÃ¡tica ni teorÃ­a axiomÃ¡tica de conjuntos por sÃ­ mismas; su funciÃ³n es construir, a partir del contrato fundacional de la obra, el aparato mÃ­nimo con el cual podrÃ¡ comenzar en el capÃ­tulo siguiente la construcciÃ³n de los nÃºmeros naturales.

La regla de lectura serÃ¡ estricta:

> **Todo sÃ­mbolo matemÃ¡tico interno del tratado aparece por primera vez en una definiciÃ³n, convenciÃ³n o notaciÃ³n identificable; toda afirmaciÃ³n matemÃ¡tica que no pertenezca al fundamento lÃ³gico-conjuntista admitido se demuestra antes de utilizarse.**

La cadena principal de este capÃ­tulo es:

$$
\text{conjuntos}
\longrightarrow
\text{inclusiÃ³n y operaciones}
\longrightarrow
\text{pares ordenados}
\longrightarrow
\text{productos cartesianos}
\longrightarrow
\text{relaciones}
\longrightarrow
\text{equivalencias y cocientes}
\longrightarrow
\text{funciones}
\longrightarrow
\text{Ã³rdenes}.
$$

NingÃºn resultado de anÃ¡lisis es utilizado en este capÃ­tulo.

---

## 0.1. Lenguaje lÃ³gico y axiomas conjuntistas disponibles

Antes de construir objetos matemÃ¡ticos conviene precisar quÃ© parte de la maquinaria se **admite** y quÃ© parte deberÃ¡ **demostrarse**. La distinciÃ³n es esencial en un tratado que pretende construir los sistemas numÃ©ricos desde fundamentos explÃ­citos: si una propiedad se apoya en un axioma de ZF, queremos poder decir cuÃ¡l; si se obtiene de definiciones anteriores, queremos verla aparecer como resultado interno.

Esta secciÃ³n no pretende convertir el tratado en un curso de lÃ³gica o teorÃ­a de conjuntos. Su funciÃ³n es mÃ¡s austera: fijar el suelo sobre el que caminaremos. A partir de ese suelo, las construcciones posteriores deberÃ¡n justificarse dentro del propio desarrollo.

### ConvenciÃ³n 0.1.1 â€” Metanivel y nivel objeto {#ta-metanivel-nivel-objeto}

*Glosario: [metanivel](../otros/tratado-de-analisis-glosario.md#gl-metanivel) Â· [nivel objeto](../otros/tratado-de-analisis-glosario.md#gl-nivel-objeto)*

Distinguiremos permanentemente:

1. el **metanivel**, en el que hablamos de fÃ³rmulas, demostraciones, variables, definiciones y dependencias;
2. el **nivel objeto**, en el que las variables recorren conjuntos.

Los numerales usados para numerar capÃ­tulos, secciones o resultados pertenecen al metanivel editorial hasta que los nÃºmeros naturales hayan sido construidos.

---

### ConvenciÃ³n 0.1.2 â€” LÃ³gica ambiente {#ta-logica-ambiente}

*Glosario: [lÃ³gica clÃ¡sica](../otros/tratado-de-analisis-glosario.md#gl-logica-clasica)*

Se trabaja en lÃ³gica clÃ¡sica de primer orden con igualdad. Se permiten, entre otros, modus ponens, introducciÃ³n y eliminaciÃ³n usual de cuantificadores, sustituciÃ³n de iguales, contrapositiva, reducciÃ³n al absurdo y tercero excluido.

La igualdad `=` es lÃ³gica y primitiva. La pertenencia $\in$ es el Ãºnico sÃ­mbolo no lÃ³gico primitivo del lenguaje conjuntista.

No registraremos como resultados del tratado las tautologÃ­as puramente lÃ³gicas.

---

### 0.1.1. Inventario axiomÃ¡tico {#ta-zf}

*Glosario: [ZF](../otros/tratado-de-analisis-glosario.md#gl-zf)*

Los axiomas siguientes son **fundamento admitido**, no teoremas del tratado. Se los reproduce aquÃ­ para que las dependencias de las construcciones posteriores sean visibles.

#### Extensionalidad {#ta-axioma-extensionalidad}

*Glosario: [extensionalidad](../otros/tratado-de-analisis-glosario.md#gl-extensionalidad)*

$$
\forall A\,\forall B\,
\Bigl[
\forall x\,(x\in A\leftrightarrow x\in B)
\;\Longrightarrow\;
A=B
\Bigr].
$$

#### Par

Para cualesquiera conjuntos $a,b$ existe un conjunto $P$ cuyos elementos son exactamente $a$ y $b$:

$$
\forall a\,\forall b\,\exists P\,\forall x
\bigl(x\in P\leftrightarrow(x=a\lor x=b)\bigr).
$$

#### UniÃ³n

Para todo conjunto $A$ existe un conjunto $U$ tal que

$$
x\in U
\iff
\exists B\,(B\in A\land x\in B).
$$

#### Conjunto potencia

Para todo conjunto $A$ existe un conjunto $P$ tal que

$$
X\in P
\iff
\forall x\,(x\in X\rightarrow x\in A).
$$

#### Esquema de separaciÃ³n

Dado un conjunto $A$ y una fÃ³rmula $\varphi(x)$, existe un conjunto $B$ tal que

$$
x\in B
\iff
(x\in A\land\varphi(x)).
$$

#### Esquema de reemplazo

Si una fÃ³rmula $\varphi(x,y)$ determina para cada $x\in A$ un Ãºnico $y$, entonces la colecciÃ³n de esos valores $y$ es un conjunto.

#### Infinito

Usaremos en el capÃ­tulo 1 el axioma de infinito. Para evitar utilizar anticipadamente el sÃ­mbolo $\varnothing$, puede expresarse en una forma equivalente adecuada a este tratado:

$$
\exists I\Bigl[
\exists e\bigl(e\in I\land\forall z\,(z\notin e)\bigr)
\land
\forall x\Bigl(
x\in I\rightarrow
\exists y\bigl(
y\in I\land
\forall z\,(z\in y\leftrightarrow(z\in x\lor z=x))
\bigr)
\Bigr)
\Bigr].
$$

En este capÃ­tulo utilizaremos de este axioma Ãºnicamente su consecuencia inmediata de que **existe al menos un conjunto**.

#### FundaciÃ³n

El axioma de fundaciÃ³n estÃ¡ disponible por pertenecer a ZF, pero ningÃºn resultado de este capÃ­tulo dependerÃ¡ de Ã©l.

---

### NotaciÃ³n 0.1.3 â€” SeparaciÃ³n restringida {#ta-separacion-restringida}

*Glosario: [separaciÃ³n restringida](../otros/tratado-de-analisis-glosario.md#gl-separacion-restringida)*

Cuando $A$ es un conjunto y $P(x)$ una propiedad, escribiremos

$$
\{x\in A:P(x)\}
$$

para el subconjunto de $A$ cuya existencia garantiza separaciÃ³n.

Esta notaciÃ³n **no** autoriza expresiones irrestrictas de la forma $\{x:P(x)\}$ sin un conjunto ambiente previamente disponible.

---

## 0.2. Conjuntos, inclusiÃ³n y operaciones

El lenguaje primitivo sÃ³lo nos da pertenencia e igualdad. Para trabajar matemÃ¡ticamente necesitamos derivar de Ã©l formas estables de comparar y combinar conjuntos. La primera es la inclusiÃ³n: en vez de preguntar por un elemento aislado, preguntamos si **todo** elemento de un conjunto pertenece a otro. De esa relaciÃ³n surgirÃ¡n luego las operaciones usuales â€”uniÃ³n, intersecciÃ³n, diferencia y conjunto potenciaâ€” y, con ellas, los conjuntos ambientes en los que podremos construir productos, relaciones y funciones.

### DefiniciÃ³n 0.2.1 â€” Subconjunto {#ta-subconjunto}

*Glosario: [subconjunto](../otros/tratado-de-analisis-glosario.md#gl-subconjunto)*

Sean $A$ y $B$ conjuntos. Definimos

$$
A\subseteq B
\quad\Longleftrightarrow\quad
\forall x\,(x\in A\rightarrow x\in B).
$$

Si $A\subseteq B$ y $A\neq B$, escribiremos $A\subsetneq B$.

---

### ProposiciÃ³n 0.2.2 â€” Reflexividad de la inclusiÃ³n
Para todo conjunto $A$,

$$
A\subseteq A.
$$

**DemostraciÃ³n.**  
Sea $x\in A$. Entonces $x\in A$. Por la DefiniciÃ³n 0.2.1, $A\subseteq A$. âˆ

---

### ProposiciÃ³n 0.2.3 â€” Transitividad de la inclusiÃ³n
Si $A\subseteq B$ y $B\subseteq C$, entonces $A\subseteq C$.

**DemostraciÃ³n.**  
Sea $x\in A$. Como $A\subseteq B$, tenemos $x\in B$; como $B\subseteq C$, tenemos $x\in C$. Por la DefiniciÃ³n 0.2.1, $A\subseteq C$. âˆ

---

### Teorema 0.2.4 â€” Criterio extensional por doble inclusiÃ³n
Para cualesquiera conjuntos $A$ y $B$,

$$
A=B
\quad\Longleftrightarrow\quad
(A\subseteq B\ \text{y}\ B\subseteq A).
$$

**DemostraciÃ³n.**  
Si $A=B$, la reflexividad de la inclusiÃ³n (ProposiciÃ³n 0.2.2) da $A\subseteq B$ y $B\subseteq A$.

RecÃ­procamente, supongamos $A\subseteq B$ y $B\subseteq A$. Entonces, para todo $x$,

$$
x\in A\iff x\in B.
$$

Por extensionalidad, $A=B$. âˆ

---

### ProposiciÃ³n 0.2.5 â€” Existencia y unicidad del conjunto vacÃ­o {#ta-existencia-vacio}

Existe un Ãºnico conjunto que no tiene elementos.

**DemostraciÃ³n.**  
**Existencia.** Del axioma de infinito se sigue que existe al menos un conjunto $A$. Por separaciÃ³n existe

$$
E:=\{x\in A:xneq x\}.
$$

No existe $x\in E$, pues $x\neq x$ es falso por reflexividad de la igualdad.

%'‰ÈiÔjq2Ê'éí¢Ë"é^™éí¢ÃÚ­«hvŒqŠq"}übœZnzÆ¦m«)®Šh²'"¢w¬²‰ßj[°ú+{^È¨©bu§DÚ-iÈ§Ón‚¢xîÚ/iÊ-iÊ'éí¢öœŠ¥¢Æ«Š‡(;§¶‹Úrè¶º,şÚÚµ§huæ§jX¬ŠÈ%¢Æ«Š‰‚W(;§¶‹Úr*zz-j·¦¢Êh®ö«‹aŠx–xœ¡Ê'éí¢È§zW¦z{h±Ë²iìb²×§r&²ºxœ‰Ö~ç«¢w^š‹-­§Z±éåhúè¦‹"r)ôÛ“ë¢š,‰È§ÓnÄ–öœ¡ë-r‰ízx¡éí¡Ú¢xîÚj¶­¡Ú¢xîÚ ½ªç¢Øb.nÇ­z zj,¶¶œŠsh{¬µìbö«‹aŠx¢»ZÚ%j)©–'r)ñŠ{Ú®z-†)àF(!µªë£bœ¬½êİi×«j–«jÚ£)–'Ú%h7ŸŠxœŠ}6Öö«‹aŠx,¹»µê€6‹Zr)ôÛÃÚ­ë'¢Šİzv¢Ì¬Šx%zÚ'²Ö©j¹è¢·^§h²)à•ëhœih±ªâ¢–«Š+uéÚvè¶º,şÚÚµ§huæ§jX¬ŠÈ%¢Æ«Š‰‚ZZ®z(­×§iÚ,Šx%zÚ'ş‹k¢Ïí­«Zv‡^jv¥ŠÈ¬‚Z,j¸¨™Ø%²)à•ëhœú+zV±Š‰šuéijºZ­§(;§¶‹mìb²×®xœ¡Ê'éí¡Ë²¢Ç¥zg§¶‹,¢w±iËZ™éíy¬›.‡^‹Z­é¨±¦Ãyø§Šj,z["	^¶‰İyªh­