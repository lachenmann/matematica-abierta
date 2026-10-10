---
{
  "title": "Congruencias y aritmética modular",
  "description": "Capítulo 17 del Tomo I de Álgebra para matemáticos, con 96 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0192",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C17",
  "editorial-id": "MA-BCH-APM-01-017",
  "status": "published",
  "date-created": "2026-10-09",
  "date-modified": "2026-10-09",
  "areas": [
    "algebra",
    "fundamentos"
  ],
  "level": "fundamental",
  "topics": [
    "numeros-complejos-y-el-horizonte-de-las-ecuaciones"
  ],
  "prerequisites": [
    "MA-BCH-0191"
  ],
  "related": [
    "MA-BOK-0006"
  ],
  "provenance": {
    "type": "original",
    "sources": []
  },
  "license": "GFDL-1.3-or-later"
}
---

En los capítulos anteriores aprendimos a mirar los enteros mediante divisibilidad, máximo común divisor, factorización y combinaciones lineales. Ahora introduciremos una manera distinta de comparar enteros: en lugar de preguntar si son iguales, preguntaremos si **dejan el mismo resto al dividir por un entero fijo**.

Por ejemplo, al dividir por $5$ los números

$$
2,
\,7,
\,12,
\,17,
\,22
$$

dejan todos resto $2$. Desde el punto de vista de los restos módulo $5$, esos enteros se comportan como una sola clase.

La afirmación

$$
17\equiv2\pmod5
$$

no significa que $17=2$. Significa que su diferencia es múltiplo de $5$:

$$
5\mid(17-2).
$$

Esta pequeña modificación del concepto de igualdad produce una estructura sorprendentemente rica. La congruencia será una relación de equivalencia sobre $\mathbb Z$; sus clases podrán sumarse y multiplicarse; aparecerán inversos cuando exista coprimalidad; las ecuaciones lineales se convertirán en congruencias lineales; y, finalmente, el Teorema Chino del Resto permitirá reconstruir un entero a partir de varios restos compatibles.

La idea central del capítulo será:

> **La congruencia transforma una condición de divisibilidad en una relación de equivalencia compatible con suma y producto. Al pasar de enteros a clases residuales obtenemos una aritmética finita en la que la posibilidad de cancelar o invertir está gobernada exactamente por la coprimalidad.**

Trabajaremos siempre con un módulo $n\ge2$, salvo indicación expresa.

***
## 17.1. Cuando los enteros se observan a través de un módulo {#apm-c17-s01}

En la aritmética usual, dos enteros distintos permanecen distintos. Sin embargo, muchos problemas no dependen del valor exacto de un entero, sino únicamente de su resto al dividir por cierto número fijo.

Si dividimos cualquier entero $a$ por $5$, el algoritmo de división de C15 produce enteros únicos $q$ y $r$ tales que

$$
a=5q+r,
\qquad
0\le r<5.
$$

Por tanto, sólo existen cinco restos posibles:

$$
0,1,2,3,4.
$$

Todo entero pertenece exactamente a una de las cinco familias

$$
\ldots,-10,-5,0,5,10,\ldots,
$$

$$
\ldots,-9,-4,1,6,11,\ldots,
$$

$$
\ldots,-8,-3,2,7,12,\ldots,
$$

$$
\ldots,-7,-2,3,8,13,\ldots,
$$

$$
\ldots,-6,-1,4,9,14,\ldots.
$$

Los miembros de cada fila difieren entre sí en múltiplos de $5$.

Esta observación sugiere una relación. Diremos que dos enteros son equivalentes respecto del módulo $5$ cuando su diferencia es divisible por $5$. Así, por ejemplo,

$$
23-8=15,
$$

de modo que $23$ y $8$ serán equivalentes módulo $5$.

La misma idea funciona para cualquier módulo $n\ge2$. No estamos “cambiando” los enteros. Estamos eligiendo deliberadamente ignorar toda información excepto aquella que permanece visible al dividir por $n$.

Esta perspectiva es útil porque muchas propiedades aritméticas son periódicas. Por ejemplo, si un entero es par depende sólo de su resto módulo $2$; si un entero es múltiplo de $3$ depende sólo de su resto módulo $3$; y el último dígito de un entero depende sólo de su resto módulo $10$.

El paso importante será convertir esta intuición en una definición precisa y, después, demostrar que esa definición es compatible con las operaciones aritméticas.

***
## 17.2. Definición de congruencia y equivalencias básicas {#apm-c17-s02}

Sea $n\ge2$. Para $a,b\in\mathbb Z$ definimos

$$
\boxed{
a\equiv b\pmod n
\iff
n\mid(a-b).
}
$$

Leemos $a\equiv b\pmod n$ como “$a$ es congruente con $b$ módulo $n$”.

Por ejemplo,

$$
37\equiv7\pmod{10}
$$

porque

$$
10\mid(37-7)=30.
$$

También

$$
-8\equiv4\pmod6
$$

porque

$$
6\mid(-8-4)=-12.
$$

La definición puede escribirse de una segunda manera. Por divisibilidad,

$$
n\mid(a-b)
$$

si y sólo si existe $k\in\mathbb Z$ tal que

$$
a-b=kn.
$$

Equivalentemente,

$$
\boxed{
a\equiv b\pmod n
\iff
\exists k\in\mathbb Z:\ a=b+kn.
}
$$

Esta forma permite ver que dos enteros congruentes difieren exactamente en un número entero de módulos.

Congruencia y resto canónico
-

La tercera caracterización conecta la congruencia con el algoritmo de división.

**Teorema.** Sean $a,b\in\mathbb Z$ y $n\ge2$. Entonces

$$
a\equiv b\pmod n
$$

si y sólo si $a$ y $b$ dejan el mismo resto al dividir por $n$.

**Demostración.** Por el algoritmo de división existen enteros $q_1,q_2$ y restos $r_1,r_2$ con

$$
a=nq_1+r_1,
\qquad
b=nq_2+r_2,
$$

$$
0\le r_1,r_2<n.
$$

Si $a\equiv b\pmod n$, entonces $n\mid(a-b)$. Pero

$$
a-b=n(q_1-q_2)+(r_1-r_2).
$$

Por tanto $n\mid(r_1-r_2)$. Como

$$
-(n-1)\le r_1-r_2\le n-1,
$$

el único múltiplo de $n$ posible es $0$. Luego $r_1=r_2$.

Recíprocamente, si $r_1=r_2$, entonces

$$
a-b=n(q_1-q_2),
$$

y por tanto $n\mid(a-b)$. Así,

$$
a\equiv b\pmod n.
$$

Esto demuestra la equivalencia. $\square$

Por ejemplo,

$$
-17=5(-4)+3,
$$

así que el resto canónico de $-17$ módulo $5$ es $3$. En consecuencia,

$$
-17\equiv3\pmod5.
$$

Conviene distinguir cuidadosamente dos usos del lenguaje:

- $a\equiv b\pmod n$ es una **relación** entre dos enteros;
- “el resto de $a$ módulo $n$” es el único entero $r\in\{0,1,\ldots,n-1\}$ que representa la clase de $a$.

***
## 17.3. Congruencia como relación de equivalencia {#apm-c17-s03}

En C8 estudiamos relaciones reflexivas, simétricas y transitivas. La congruencia módulo $n$ proporciona ahora un ejemplo aritmético fundamental.

**Teorema.** Para todo $n\ge2$, la relación

$$
a\sim b
\iff
a\equiv b\pmod n
$$

es una relación de equivalencia sobre $\mathbb Z$.

**Demostración.** Verificamos las tres propiedades.

**Reflexividad.** Para todo $a\in\mathbb Z$,

$$
a-a=0,
$$

y $n\mid0$. Por tanto

$$
a\equiv a\pmod n.
$$

**Simetría.** Si $a\equiv b\pmod n$, entonces

$$
n\mid(a-b).
$$

Como $b-a=-(a-b)$, también

$$
n\mid(b-a).
$$

Luego

$$
b\equiv a\pmod n.
$$

**Transitividad.** Si

$$
a\equiv b\pmod n
$$

y

$$
b\equiv c\pmod n,
$$

entonces

$$
n\mid(a-b)
$$

y

$$
n\mid(b-c).
$$

Por cierre de los múltiplos bajo suma,

$$
n\mid[(a-b)+(b-c)]=a-c.
$$

Por tanto

$$
a\equiv c\pmod n.
$$

La congruencia módulo $n$ es, pues, una relación de equivalencia. $\square$

Este resultado no es sólo terminológico. Toda relación de equivalencia particiona el conjunto sobre el que está definida. Por tanto, $\mathbb Z$ queda dividido en clases disjuntas de enteros congruentes entre sí.

Para módulo $4$, por ejemplo, aparecen cuatro clases:

$$
\ldots,-8,-4,0,4,8,\ldots,
$$

$$
\ldots,-7,-3,1,5,9,\ldots,
$$

$$
\ldots,-6,-2,2,6,10,\ldots,
$$

$$
\ldots,-5,-1,3,7,11,\ldots.
$$

Desde este punto de vista, la aritmética modular no comienza con reglas de cálculo. Comienza con una **partición de $\mathbb Z$ producida por una relación de equivalencia**.

***
## 17.4. Clases residuales y representantes canónicos {#apm-c17-s04}

Para $a\in\mathbb Z$ y $n\ge2$, definimos la **clase residual de $a$ módulo $n$** por

$$
[a]_n
=
\{b\in\mathbb Z:b\equiv a\pmod n\}.
$$

Por ejemplo,

$$
[2]_5
=
\{\ldots,-8,-3,2,7,12,17,\ldots\}.
$$

La notación no privilegia realmente al número $2$. Como $7\equiv2\pmod5$,

$$
[7]_5=[2]_5.
$$

Esto es un caso particular de una propiedad general.

**Teorema.** Para $a,b\in\mathbb Z$,

$$
\boxed{
[a]_n=[b]_n
\iff
a\equiv b\pmod n.
}
$$

**Demostración.** Si $a\equiv b\pmod n$, sea $x\in[a]_n$. Entonces

$$
x\equiv a\pmod n.
$$

Como $a\equiv b\pmod n$, por transitividad

$$
x\equiv b\pmod n,
$$

de modo que $x\in[b]_n$. Así $[a]_n\subseteq[b]_n$. El argumento simétrico da la inclusión contraria.

Recíprocamente, si $[a]_n=[b]_n$, como $a\in[a]_n$, se tiene $a\in[b]_n$. Por definición,

$$
a\equiv b\pmod n.
$$

$\square$

Representantes canónicos
-

Cada clase tiene infinitos representantes, pero el algoritmo de división selecciona uno de manera canónica.

Para todo $a\in\mathbb Z$ existe un único $r$ con

$$
0\le r<n
$$

tal que

$$
a\equiv r\pmod n.
$$

Ese $r$ es precisamente el resto de dividir $a$ por $n$.

Por ejemplo, módulo $7$:

$$
-23=7(-4)+5,
$$

luego

$$
[-23]_7=[5]_7.
$$

Por tanto, las clases distintas módulo $n$ son exactamente

$$
[0]_n,[1]_n,\ldots,[n-1]_n.
$$

Además son distintas dos a dos. En efecto, si

$$
[r]_n=[s]_n
$$

con $0\le r,s<n$, entonces $r\equiv s\pmod n$, de modo que $n\mid(r-s)$. Pero $|r-s|<n$, por lo que necesariamente $r=s$.

Así, aunque cada clase contiene infinitos enteros, el conjunto de clases tiene exactamente $n$ elementos.

***
## 17.5. El cociente elemental $\mathbb Z/n\mathbb Z$ {#apm-c17-s05}

Definimos

$$
\boxed{
\mathbb Z/n\mathbb Z
=
\{[0]_n,[1]_n,\ldots,[n-1]_n\}.
}
$$

Este conjunto no debe confundirse con $\{0,1,\ldots,n-1\}$. Sus elementos son **clases de equivalencia**, cada una de las cuales contiene infinitos enteros. Los números $0,1,\ldots,n-1$ sirven únicamente como representantes canónicos de esas clases.

Por ejemplo,

$$
\mathbb Z/4\mathbb Z
=
\{[0]_4,[1]_4,[2]_4,[3]_4\}.
$$

El paso de $\mathbb Z$ a $\mathbb Z/n\mathbb Z$ puede interpretarse como un proceso de identificación: enteros distintos se consideran iguales cuando su diferencia es múltiplo de $n$.

Sistemas completos de residuos
-

Un conjunto de $n$ enteros

$$
\{r_0,r_1,\ldots,r_{n-1}\}
$$

se llama **sistema completo de residuos módulo $n$** si contiene exactamente un representante de cada clase módulo $n$.

El sistema canónico es

$$
\{0,1,\ldots,n-1\}.
$$

Pero no es el único. Por ejemplo,

$$
\{-2,-1,0,1,2\}
$$

es un sistema completo de residuos módulo $5$.

Para verificarlo basta observar que sus restos canónicos son

$$
3,4,0,1,2,
$$

que recorren todas las clases exactamente una vez.

La idea de sistema completo de residuos será útil más adelante: multiplicar todos los representantes por un número coprimo con $n$ volverá a producir un sistema completo de residuos. Esa afirmación será otra cara de la invertibilidad modular.

### Nota pedagógica — Tres objetos que la notación no debe confundir

Un entero $a$, su clase $[a]_n$ y el resto canónico $r$ son objetos diferentes. El entero pertenece a su clase; el resto también pertenece a ella. La igualdad $[a]_n=[r]_n$ identifica dos conjuntos, mientras $a\equiv r\pmod n$ compara dos enteros. Ninguna de esas afirmaciones exige $a=r$.

**Control resuelto.** Con módulo seis, $-19=6(-4)+5$. El resto es cinco y $[-19]_6=[5]_6=[11]_6$, aunque esos tres representantes no son iguales. La clase es el conjunto $\{5+6t:t\in\mathbb Z\}$; el conjunto cociente tiene seis clases, no seis enteros. La elección de un representante por clase permite hacer tablas finitas, pero no cambia los elementos del cociente en números ordinarios.

Un sistema completo de residuos sólo exige una elección por cada clase. Por ejemplo, $\{-3,-2,-1,0,1,2\}$ es completo módulo seis porque sus restos son $3,4,5,0,1,2$. En cambio, seis enteros distintos pueden representar una sola clase: $\{5,11,17,23,29,35\}$. Antes de contar clases, reduce los representantes y comprueba cuáles se identifican.

***
## 17.6. Compatibilidad con suma, resta, producto y potencias {#apm-c17-s06}

La congruencia sería poco útil si no respetara las operaciones aritméticas. El siguiente resultado es la base del cálculo modular.

**Teorema.** Si

$$
a\equiv a'\pmod n
$$

y

$$
b\equiv b'\pmod n,
$$

entonces

$$
a+b\equiv a'+b'\pmod n,
$$

$$
a-b\equiv a'-b'\pmod n,
$$

y

$$
ab\equiv a'b'\pmod n.
$$

**Demostración.** Existen $r,s\in\mathbb Z$ tales que

$$
a-a'=rn,
\qquad
b-b'=sn.
$$

Para la suma,

$$
(a+b)-(a'+b')
=(a-a')+(b-b')
=(r+s)n.
$$

Por tanto

$$
a+b\equiv a'+b'\pmod n.
$$

La resta se trata de manera análoga.

Para el producto,

$$
ab-a'b'
=a(b-b')+b'(a-a').
$$

Sustituyendo,

$$
ab-a'b'
=a(sn)+b'(rn)
=n(as+b'r),
$$

por lo que

$$
ab\equiv a'b'\pmod n.
$$

$\square$

Potencias
-

Si

$$
a\equiv b\pmod n,
$$

entonces para todo entero $k\ge1$,

$$
\boxed{
a^k\equiv b^k\pmod n.
}
$$

La afirmación se obtiene aplicando repetidamente la compatibilidad con el producto, o por inducción.

Reducir antes de calcular
-

Supongamos que queremos hallar el resto de

$$
38^4+27^3
$$

módulo $5$. Como

$$
38\equiv3\pmod5,
\qquad
27\equiv2\pmod5,
$$

se sigue que

$$
38^4+27^3
\equiv
3^4+2^3
=81+8
=89
\equiv4\pmod5.
$$

No fue necesario calcular las potencias originales. Podemos reducir **antes**, **durante** y **después** de las operaciones porque la congruencia es compatible con suma y producto.

Este principio convierte muchos cálculos enormes en operaciones con representantes pequeños.

***
## 17.7. Operaciones sobre clases y el problema de la buena definición {#apm-c17-s07}

Queremos ahora sumar y multiplicar directamente clases residuales. La definición natural es

$$
[a]_n+[b]_n=[a+b]_n,
$$

$$
[a]_n[b]_n=[ab]_n.
$$

Sin embargo, hay una dificultad lógica. Una misma clase tiene muchos representantes. Por ejemplo,

$$
[2]_5=[7]_5.
$$

Si usamos $2$ o $7$ para calcular, ¿obtenemos realmente la misma clase final?

Ésta es la cuestión de la **buena definición**.

**Teorema.** Las operaciones anteriores no dependen de los representantes elegidos.

**Demostración.** Supongamos

$$
[a]_n=[a']_n,
\qquad
[b]_n=[b']_n.
$$

Por el criterio de igualdad de clases,

$$
a\equiv a'\pmod n,
\qquad
b\equiv b'\pmod n.
$$

Por compatibilidad,

$$
a+b\equiv a'+b'\pmod n,
$$

y

$$
ab\equiv a'b'\pmod n.
$$

Luego

$$
[a+b]_n=[a'+b']_n
$$

y

$$
[ab]_n=[a'b']_n.
$$

Por tanto las operaciones están bien definidas. $\square$

Un pequeño laboratorio: $\mathbb Z/4\mathbb Z$
-

En $\mathbb Z/4\mathbb Z$ tenemos, por ejemplo,

$$
[3]_4+[3]_4=[6]_4=[2]_4,
$$

$$
[3]_4[3]_4=[9]_4=[1]_4.
$$

También

$$
[2]_4[2]_4=[4]_4=[0]_4.
$$

Esta última igualdad anuncia una diferencia importante respecto de la aritmética de enteros: en el mundo de las clases módulo $4$ pueden aparecer productos de clases no nulas que dan la clase cero.

No desarrollaremos todavía la teoría general de anillos. Pero sí registraremos el fenómeno, porque explica por qué la cancelación puede fallar.

### Nota pedagógica — Una regla debe sobrevivir al cambio de representante

Para una regla $[a]_n\mapsto[f(a)]_n$, la obligación es universal: si $a'=a+nt$, se debe demostrar que $n\mid f(a')-f(a)$ para todo entero $t$. Una sola pareja favorable no prueba buena definición. En cambio, una pareja de representantes de la misma clase que produzca clases distintas refuta la regla.

**Control resuelto sobre las mismas entradas.** Módulo cinco, $[2]_5=[7]_5$. La regla $[a]_5\mapsto[a^2]_5$ produce $[4]_5$ usando dos y $[49]_5=[4]_5$ usando siete. Para representantes arbitrarios, $(a+5t)^2-a^2=5(2at+5t^2)$; la regla está bien definida.

La regla propuesta $[a]_5\mapsto[|a|]_5$ falla: $[2]_5=[-3]_5$, pero $[|2|]_5=[2]_5$ y $[|-3|]_5=[3]_5$ son distintas. No es una función sobre clases si se permite cualquier representante. Podemos definir otra regla eligiendo primero el resto canónico; ésa sí tiene un valor determinado porque el resto es único, pero la elección debe formar parte de la definición y no se puede reemplazar por un representante arbitrario.

El criterio también se aplica a propiedades: «este representante es positivo» no depende sólo de la clase, pues una misma clase tiene representantes de ambos signos. Ser una expresión familiar en los enteros no basta para que descienda al cociente.

***
## 17.8. Cancelación: por qué puede fallar y cuándo se recupera {#apm-c17-s08}

En los enteros, si $c\ne0$ y

$$
ca=cb,
$$

podemos cancelar $c$ y concluir $a=b$.

Para congruencias, la afirmación análoga no es siempre verdadera.

Por ejemplo,

$$
2\cdot1\equiv2\cdot3\pmod4
$$

porque

$$
2\equiv6\pmod4.
$$

Sin embargo,

$$
1\not\equiv3\pmod4.
$$

Por tanto no podemos cancelar el factor $2$ módulo $4$.

La razón es aritmética: $2$ y $4$ no son coprimos.

**Teorema de cancelación modular.** Si

$$
\gcd(c,n)=1
$$

y

$$
ca\equiv cb\pmod n,
$$

entonces

$$
\boxed{
a\equiv b\pmod n.
}
$$

**Demostración.** De

$$
ca\equiv cb\pmod n
$$

obtenemos

$$
n\mid c(a-b).
$$

Como

$$
\gcd(c,n)=1,
$$

la cancelación coprima demostrada en C15 implica

$$
n\mid(a-b).
$$

Por tanto

$$
a\equiv b\pmod n.
$$

$\square$

La hipótesis no es decorativa. Si $c$ comparte un factor con el módulo, puede colapsar clases distintas.

Por ejemplo, módulo $6$,

$$
2[1]_6=[2]_6,
\qquad
2[4]_6=[8]_6=[2]_6,
$$

pero

$$
[1]_6\ne[4]_6.
$$

Así, antes de cancelar un factor en una congruencia debemos verificar su coprimalidad con el módulo.

***
## 17.9. Inversos modulares y coprimalidad {#apm-c17-s09}

Sea $a\in\mathbb Z$. Decimos que $a$ posee un **inverso módulo $n$** si existe $u\in\mathbb Z$ tal que

$$
au\equiv1\pmod n.
$$

En términos de clases,

$$
[a]_n[u]_n=[1]_n.
$$

El criterio de existencia es exactamente la coprimalidad.

**Teorema.** Para $n\ge2$,

$$
\boxed{
a\text{ es invertible módulo }n
\iff
\gcd(a,n)=1.
}
$$

**Demostración.** Supongamos primero que

$$
\gcd(a,n)=1.
$$

Por Bézout existen $u,v\in\mathbb Z$ tales que

$$
au+nv=1.
$$

Entonces

$$
au-1=-nv,
$$

por lo que

$$
n\mid(au-1).
$$

Así,

$$
au\equiv1\pmod n.
$$

Por tanto $u$ es un inverso de $a$ módulo $n$.

Recíprocamente, supongamos que existe $u$ con

$$
au\equiv1\pmod n.
$$

Entonces existe $k\in\mathbb Z$ tal que

$$
au-1=kn,
$$

o equivalentemente,

$$
au-kn=1.
$$

Hemos escrito $1$ como combinación lineal de $a$ y $n$. Por el criterio de Bézout de C15,

$$
\gcd(a,n)=1.
$$

$\square$

Unicidad del inverso como clase
-

Si $u$ y $v$ son ambos inversos de $a$ módulo $n$, entonces

$$
au\equiv1\pmod n,
\qquad
av\equiv1\pmod n.
$$

Por tanto

$$
au\equiv av\pmod n.
$$

Como la existencia de inverso implica $\gcd(a,n)=1$, podemos cancelar $a$ y obtener

$$
u\equiv v\pmod n.
$$

El inverso es, pues, único **como clase módulo $n$**.

***
## 17.10. Cómo calcular un inverso: Bézout vuelve a aparecer {#apm-c17-s10}

El teorema anterior es constructivo. Para calcular un inverso de $a$ módulo $n$ basta encontrar coeficientes de Bézout para $a$ y $n$.

Consideremos el inverso de $17$ módulo $43$.

Aplicamos Euclides:

$$
43=2\cdot17+9,
$$

$$
17=1\cdot9+8,
$$

$$
9=1\cdot8+1.
$$

Sustituyendo hacia atrás,

$$
1=9-8,
$$

$$
1=9-(17-9)=2\cdot9-17,
$$

$$
1=2(43-2\cdot17)-17,
$$

por tanto

$$
1=2\cdot43-5\cdot17.
$$

Reduciendo módulo $43$,

$$
-5\cdot17\equiv1\pmod{43}.
$$

Así, un inverso de $17$ módulo $43$ es $-5$, o equivalentemente su representante canónico $38$:

$$
17^{-1}\equiv38\pmod{43}.
$$

La notación $17^{-1}$ en este contexto no significa el racional $1/17$. Significa **la clase multiplicativa inversa de $[17]_{43}$**.

Protocolo de cálculo
-

Para hallar el inverso de $a$ módulo $n$:

1. calcular $d=\gcd(a,n)$;
2. si $d\ne1$, concluir que el inverso no existe;
3. si $d=1$, usar Euclides extendido para hallar
   $$
   au+nv=1;
   $$
4. reducir $u$ módulo $n$.

Por ejemplo, $14$ no posee inverso módulo $35$ porque

$$
\gcd(14,35)=7\ne1.
$$

No hace falta buscar candidatos.

***
## 17.11. Congruencias lineales como ecuaciones diofánticas disfrazadas {#apm-c17-s11}

Consideremos una congruencia lineal

$$
ax\equiv b\pmod n.
$$

Por definición,

$$
n\mid(ax-b).
$$

Por tanto existe $y\in\mathbb Z$ tal que

$$
ax-b=ny.
$$

Equivalentemente,

$$
\boxed{
ax-ny=b.
}
$$

Así, resolver una congruencia lineal es resolver una ecuación diofántica lineal en dos variables y después leer sólo la coordenada $x$ módulo $n$.

Esta traducción permite importar directamente el criterio de C15.

Sea

$$
d=\gcd(a,n).
$$

La ecuación

$$
ax-ny=b
$$

tiene solución entera si y sólo si

$$
d\mid b.
$$

Por tanto obtenemos:

**Teorema de solvencia.**

$$
\boxed{
ax\equiv b\pmod n
\text{ tiene solución}
\iff
\gcd(a,n)\mid b.
}
$$

Necesidad
-

Si $x$ es solución, entonces existe $y$ con

$$
ax-ny=b.
$$

Todo divisor común de $a$ y $n$ divide el lado izquierdo, y en particular

$$
\gcd(a,n)\mid b.
$$

Suficiencia
-

Si

$$
d=\gcd(a,n)
$$

y $d\mid b$, el teorema de C15 garantiza que

$$
ax-ny=b
$$

tiene solución entera. La coordenada $x$ satisface entonces

$$
ax\equiv b\pmod n.
$$

Por ejemplo,

$$
18x\equiv12\pmod{30}
$$

es soluble porque

$$
\gcd(18,30)=6
$$

y

$$
6\mid12.
$$

En cambio,

$$
18x\equiv7\pmod{30}
$$

no tiene solución porque $6\nmid7$.

***
## 17.12. Clasificación y número de soluciones de $ax\equiv b\pmod n$ {#apm-c17-s12}

El criterio anterior decide si existen soluciones. Ahora queremos describirlas todas.

Sea

$$
d=\gcd(a,n)
$$

y supongamos

$$
d\mid b.
$$

Escribimos

$$
a=da_1,
\qquad
b=db_1,
\qquad
n=dn_1.
$$

Entonces

$$
\gcd(a_1,n_1)=1.
$$

La congruencia original

$$
d a_1x\equiv d b_1\pmod{d n_1}
$$

si $d<n$, es equivalente a

$$
\boxed{
a_1x\equiv b_1\pmod{n_1}.
}
$$

Si $d=n$, entonces $n\mid a$. En ese caso la congruencia original es equivalente a

$$
0\equiv b\pmod n.
$$

Por tanto, si es soluble, necesariamente $n\mid b$ y **todas** las $n$ clases módulo $n$ son soluciones. Esto coincide con la afirmación general de que hay exactamente $d=n$ soluciones.

Supongamos ahora $d<n$. Entonces $n_1=n/d\ge2$. Como $a_1$ es coprimo con $n_1$, posee inverso. Por tanto existe una única clase solución módulo $n_1$:

$$
x\equiv x_0\pmod{n_1}.
$$

Al volver a mirar soluciones módulo $n=dn_1$, esa única clase módulo $n_1$ se descompone en exactamente $d$ clases módulo $n$:

$$
\boxed{
x\equiv x_0+k\frac nd\pmod n,
\qquad
k=0,1,\ldots,d-1.
}
$$

Por qué son soluciones
-

Como

$$
x=x_0+kn_1,
$$

se tiene

$$
a_1x
\equiv
 a_1x_0
\equiv
b_1
\pmod{n_1}.
$$

Luego cada una satisface la congruencia reducida y, por tanto, la original.

Por qué son distintas módulo $n$
-

Si para $0\le k<\ell\le d-1$ tuviéramos

$$
x_0+kn_1\equiv x_0+\ell n_1\pmod{dn_1},
$$

entonces

$$
dn_1\mid(\ell-k)n_1,
$$

por lo que

$$
d\mid(\ell-k).
$$

Pero

$$
0<\ell-k<d,
$$

imposible.

Por qué no hay otras
-

Toda solución de la congruencia original satisface la reducida, luego es congruente con $x_0$ módulo $n_1$. Por tanto tiene la forma

$$
x=x_0+tn_1.
$$

El valor de $t$ módulo $d$ determina exactamente una de las $d$ clases anteriores.

Concluimos:

**Teorema completo de la congruencia lineal.** Si

$$
d=\gcd(a,n),
$$

entonces:

- si $d\nmid b$, no hay soluciones;
- si $d\mid b$, hay exactamente $d$ clases solución módulo $n$.

Ejemplo
-

Resolvamos

$$
18x\equiv12\pmod{30}.
$$

Tenemos $d=6$. Dividimos por $6$:

$$
3x\equiv2\pmod5.
$$

Como

$$
3^{-1}\equiv2\pmod5,
$$

obtenemos

$$
x\equiv4\pmod5.
$$

Al levantar a módulo $30$ aparecen seis clases:

$$
x\equiv4,9,14,19,24,29\pmod{30}.
$$

### Nota pedagógica — Existencia, clases y representantes se cuentan por separado

El certificado $d=\gcd(a,n)\mid b$ decide existencia. Una solución particular permite construir la familia, pero la exhaustividad exige partir de una solución arbitraria. Finalmente, contar clases módulo $n$ no equivale a contar los representantes enteros de esas clases, que son infinitos.

**Control resuelto.** Para $8x\equiv12\pmod{20}$, el MCD es cuatro y divide a doce. La condición de divisibilidad $20\mid8x-12$ equivale a $5\mid2x-3$, y multiplicar por el inverso tres de dos módulo cinco da $x\equiv4\pmod5$. Todas las soluciones enteras son $x=4+5t$, $t\in\mathbb Z$. Módulo veinte, reducir $t$ módulo cuatro da exactamente $[4],[9],[14],[19]$. Son distintas porque una diferencia $5(j-k)$ es divisible por veinte sólo si cuatro divide a $j-k$.

Cambiar doce por diez hace imposible la congruencia: cuatro no divide a diez. Si el coeficiente es múltiplo del módulo, se vuelve necesario tratar el caso directamente. Por ejemplo, $40x\equiv20\pmod{20}$ lo cumple todo entero, y hay veinte clases solución; $40x\equiv1\pmod{20}$ no tiene ninguna. No hace falta introducir un módulo reducido igual a uno.

Para imponer después un intervalo o una segunda condición, trabaja con la familia completa y demuestra que cada restricción equivale a una condición sobre su parámetro. La lista de clases y la lista finita de representantes permitidos responden preguntas diferentes.

***
## 17.13. Sistemas de congruencias y el problema de compatibilidad {#apm-c17-s13}

Una congruencia individual prescribe un resto. Un sistema de congruencias prescribe varios restos simultáneamente.

Por ejemplo,

$$
x\equiv2\pmod3,
$$

$$
x\equiv3\pmod5.
$$

Buscamos un entero que deje resto $2$ al dividir por $3$ y resto $3$ al dividir por $5$.

Una manera elemental de explorar el problema consiste en listar números congruentes con $2$ módulo $3$:

$$
2,5,8,11,14,17,\ldots
$$

y observar que

$$
8\equiv3\pmod5.
$$

Por tanto $x=8$ es una solución.

Pero la pregunta estructural es más profunda:

1. ¿cuándo existe una solución?
2. si existe, ¿es única en algún sentido modular?
3. ¿cómo construirla sin tanteo?

Para módulos coprimos, el Teorema Chino del Resto responde completamente estas preguntas.

Antes de demostrarlo, conviene observar la cuestión de compatibilidad cuando los módulos comparten factores. Por ejemplo,

$$
x\equiv0\pmod2,
\qquad
x\equiv1\pmod4
$$

no puede tener solución: la segunda congruencia obliga a que $x$ sea impar, mientras la primera obliga a que sea par.

En cambio,

$$
x\equiv1\pmod2,
\qquad
x\equiv3\pmod4
$$

sí es compatible.

La coprimalidad elimina automáticamente este tipo de conflicto, y por eso será la hipótesis principal del teorema que sigue.

***
## 17.14. Teorema Chino del Resto para dos módulos coprimos {#apm-c17-s14}

**Teorema Chino del Resto.** Sean $m,n\ge2$ con

$$
\gcd(m,n)=1.
$$

Entonces para cualesquiera $a,b\in\mathbb Z$, el sistema

$$
x\equiv a\pmod m,
$$

$$
x\equiv b\pmod n
$$

tiene solución. Además, cualesquiera dos soluciones son congruentes módulo $mn$.

Existencia constructiva
-

Como

$$
\gcd(m,n)=1,
$$

por Bézout existen $r,s\in\mathbb Z$ tales que

$$
rm+sn=1.
$$

Queremos construir un término que sea $1$ módulo $m$ y $0$ módulo $n$, y otro que sea $0$ módulo $m$ y $1$ módulo $n$.

De

$$
rm+sn=1
$$

se sigue:

$$
sn\equiv1\pmod m,
\qquad
sn\equiv0\pmod n,
$$

mientras

$$
rm\equiv0\pmod m,
\qquad
rm\equiv1\pmod n.
$$

Por tanto la construcción correcta es

$$
\boxed{
x_0=a(sn)+b(rm).
}
$$

Entonces

$$
x_0\equiv a\pmod m
$$

y

$$
x_0\equiv b\pmod n.
$$

Así existe una solución.

Unicidad módulo $mn$
-

Sean $x$ e $y$ dos soluciones. Entonces

$$
x\equiv y\pmod m
$$

y

$$
x\equiv y\pmod n.
$$

Por tanto

$$
m\mid(x-y)
$$

y

$$
n\mid(x-y).
$$

Como $m$ y $n$ son coprimos,

$$
mn\mid(x-y).
$$

Luego

$$
x\equiv y\pmod{mn}.
$$

La solución es única como clase módulo $mn$. $\square$

Ejemplo
-

Resolvamos

$$
x\equiv2\pmod3,
\qquad
x\equiv3\pmod5.
$$

Una identidad de Bézout es

$$
2\cdot3-1\cdot5=1.
$$

Así podemos tomar

$$
r=2,
\qquad
s=-1,
$$

con

$$
rm+sn=2\cdot3+(-1)\cdot5=1.
$$

La construcción da

$$
x_0=2(-1)(5)+3(2)(3)=8.
$$

Por tanto

$$
\boxed{x\equiv8\pmod{15}.}
$$

### Nota pedagógica — Construir una solución y cerrar la unicidad

La fórmula de Bézout produce un testigo para el sistema. La unicidad empieza después, comparando dos soluciones arbitrarias. Con módulos coprimos $m,n$, su diferencia es múltiplo de ambos; escribirla como $mk$ y usar cancelación coprima obliga a $n\mid k$, de modo que es múltiplo de $mn$.

**Control resuelto.** Para $x\equiv1\pmod4$, $x\equiv2\pmod5$, usamos $5-4=1$. Los términos selectores son cinco, que vale uno módulo cuatro y cero módulo cinco, y menos cuatro, que vale cero módulo cuatro y uno módulo cinco. El testigo es $x_0=1\cdot5+2(-4)=-3$. Cumple ambos residuos. Si $x$ es otra solución, $x+3$ es múltiplo de cuatro y de cinco; por coprimalidad, es múltiplo de veinte. Por tanto todas las soluciones son $-3+20t$, $t\in\mathbb Z$, o la clase $[17]_{20}$.

Diecisiete y menos tres son enteros distintos que representan la misma solución modular. La construcción no privilegia un entero único; cualquier múltiplo del producto puede añadirse.

Cuando los módulos no son coprimos, no se conserva automáticamente el producto como módulo de unicidad. El sistema $x\equiv1\pmod4$, $x\equiv3\pmod6$ tiene todas sus soluciones $9+12t$. Nueve y veintiuno son soluciones, pero no son congruentes módulo veinticuatro. El MCM doce es el período correcto. Antes de reconstruir, revisa compatibilidad; después, prueba el módulo exacto de la familia.

***
## 17.15. CRT finito, reconstrucción y diagnóstico de errores {#apm-c17-s15}

El Teorema Chino del Resto se extiende a cualquier familia finita de módulos dos a dos coprimos.

Sean

$$
n_1,n_2,\ldots,n_r\ge2
$$

dos a dos coprimos y sea

$$
N=n_1n_2\cdots n_r.
$$

Para residuos $a_1,\ldots,a_r$, el sistema

$$
x\equiv a_i\pmod{n_i},
\qquad
1\le i\le r,
$$

tiene una solución única módulo $N$.

Construcción directa
-

Definimos

$$
N_i=\frac{N}{n_i}.
$$

Como los módulos son dos a dos coprimos,

$$
\gcd(N_i,n_i)=1.
$$

Para justificarlo, si ese MCD fuera mayor que uno tendría un divisor primo $p$. El lema de Euclides para el producto $N_i$ obligaría a que $p$ dividiera algún $n_j$, $j\ne i$, además de $n_i$, contradiciendo la coprimalidad de ese par. Si la familia tiene un solo módulo, $N_i=1$ y el MCD vale uno directamente.

Por tanto existe $u_i$ tal que

$$
N_i u_i\equiv1\pmod{n_i}.
$$

Entonces

$$
\boxed{
x_0=\sum_{i=1}^r a_iN_i u_i
}
$$

satisface todas las congruencias. En efecto, módulo $n_j$, todos los términos con $i\ne j$ son divisibles por $n_j$, mientras

$$
N_j u_j\equiv1\pmod{n_j}.
$$

Por tanto

$$
x_0\equiv a_j\pmod{n_j}.
$$

La unicidad se demuestra inductivamente como en el caso de dos módulos. El argumento primo anterior también prueba que $n_k$ es coprimo con $n_1\cdots n_{k-1}$. Si ese producto divide a $x-y$, escribimos $x-y=(n_1\cdots n_{k-1})t$; como $n_k$ divide a la diferencia, la cancelación coprima obliga a $n_k\mid t$. Por tanto $n_1\cdots n_k$ divide a $x-y$. Empezando con $n_1\mid x-y$, la inducción da

$$
N\mid(x-y).
$$

Ejemplo de reconstrucción
-

Consideremos

$$
x\equiv1\pmod3,
$$

$$
x\equiv2\pmod5,
$$

$$
x\equiv3\pmod7.
$$

Aquí

$$
N=105.
$$

Tenemos

$$
N_1=35,
\qquad
N_2=21,
\qquad
N_3=15.
$$

Elegimos inversos:

$$
35\equiv2\pmod3,
\qquad
2^{-1}\equiv2\pmod3,
$$

así $u_1=2$;

$$
21\equiv1\pmod5,
$$

así $u_2=1$;

$$
15\equiv1\pmod7,
$$

así $u_3=1$.

Entonces

$$
x_0
=1\cdot35\cdot2
+2\cdot21\cdot1
+3\cdot15\cdot1
=157.
$$

Reduciendo módulo $105$,

$$
\boxed{x\equiv52\pmod{105}.}
$$

Diagnóstico de errores frecuentes
-

La aritmética modular exige distinguir cuidadosamente varias afirmaciones.

**Error 1: cancelar sin coprimalidad.** De

$$
ca\equiv cb\pmod n
$$

no puede concluirse en general que $a\equiv b\pmod n$.

**Error 2: suponer que todo número no nulo tiene inverso.** Una clase $[a]_n$ es invertible exactamente cuando

$$
\gcd(a,n)=1.
$$

**Error 3: confundir existencia con unicidad.** Una congruencia lineal puede tener varias clases solución módulo $n$; cuando $d=\gcd(a,n)$ divide a $b$, hay exactamente $d$.

**Error 4: interpretar la unicidad del CRT como igualdad de enteros.** La solución es única **módulo el producto**, no como entero ordinario.

**Error 5: multiplicar módulos no coprimos sin analizar compatibilidad.** La forma principal del CRT de este capítulo exige coprimalidad. La versión general requiere una condición adicional y queda principalmente para el bloque avanzado.

***
## 17.16. Cierre del Bloque D — del resto al cociente {#apm-c17-s16}

Los cuatro capítulos del Bloque D han construido una primera teoría algebraica coherente dentro de $\mathbb Z$.

En C14 partimos de la relación

$$
a\mid b.
$$

En C15 descubrimos que el máximo común divisor puede recuperarse como combinación lineal y que Bézout controla la coprimalidad y las ecuaciones diofánticas lineales.

En C16 vimos que los primos son los bloques multiplicativos elementales de los enteros y que la factorización es esencialmente única.

C17 ha agregado una nueva operación conceptual: **identificar enteros distintos cuando su diferencia es múltiplo de un módulo fijo**.

La cadena completa puede resumirse así:

```text
DIVISIBILIDAD
     ↓
MCD / EUCLIDES / BÉZOUT
     ↓
PRIMOS / FACTORIZACIÓN
     ↓
CONGRUENCIA
     ↓
CLASES RESIDUALES
     ↓
OPERACIONES BIEN DEFINIDAS
     ↓
COPRIMALIDAD ↔ INVERSIBILIDAD
     ↓
CONGRUENCIAS LINEALES
     ↓
CRT
```

### Protocolo para problemas modulares

Ante un problema de congruencias conviene preguntar, en este orden:

1. **¿Cuál es el módulo?** Fijar con claridad $n\ge2$.
2. **¿Qué significa la congruencia?** Traducir a divisibilidad cuando sea necesario.
3. **¿Puedo reducir los números?** Reemplazar representantes por otros más simples.
4. **¿Estoy intentando cancelar?** Verificar coprimalidad antes de hacerlo.
5. **¿Necesito un inverso?** Calcular $\gcd(a,n)$ y usar Bézout si vale $1$.
6. **¿Es una congruencia lineal?** Calcular $d=\gcd(a,n)$ y comprobar si $d\mid b$.
7. **¿Cuántas soluciones debe haber?** Si es soluble, exactamente $d$ clases módulo $n$.
8. **¿Es un sistema de congruencias?** Verificar coprimalidad o compatibilidad antes de aplicar CRT.
9. **¿Qué significa unicidad?** Precisar siempre el módulo respecto del cual la solución es única.

El objeto

$$
\mathbb Z/n\mathbb Z
$$

es el primer ejemplo sustancial de este libro en el que una relación de equivalencia produce un nuevo universo matemático sobre el cual las operaciones descienden correctamente. En capítulos y tomos posteriores esta idea reaparecerá de forma mucho más general: clases laterales, cocientes, ideales, anillos cociente y homomorfismos.

Por ahora basta conservar la intuición esencial:

> **pasar al cociente significa decidir qué diferencias dejan de importar y demostrar que las operaciones que queremos realizar respetan esa decisión.**

Con ello queda cerrado el Bloque D y estamos preparados para continuar el desarrollo algebraico con ecuaciones, orden, polinomios y nuevas estructuras.
***
# Ejercicios

Los ejercicios están organizados para pasar de la lectura elemental de restos a la comprensión estructural de las clases residuales, la inversibilidad, las congruencias lineales y el Teorema Chino del Resto. Salvo indicación expresa, todos los módulos satisfacen $n\ge2$. “Resolver módulo $n$” significa determinar clases de soluciones módulo $n$, no enumerar infinitamente todos sus representantes enteros.

## A. Definición, restos y congruencias básicas


**1.** **Nivel A.** Decide cuáles de las siguientes congruencias son verdaderas y justifica cada respuesta directamente mediante divisibilidad de la diferencia:
$$
37\equiv7\pmod{10},
\qquad
-11\equiv4\pmod5,
\qquad
26\equiv5\pmod7,
\qquad
41\equiv-1\pmod6.
$$


**2.** **Nivel A.** Encuentra el representante canónico de cada entero en el módulo indicado:
$$
-23\pmod7,\qquad
58\pmod9,\qquad
-101\pmod{12},\qquad
250\pmod{17}.
$$
En cada caso escribe también la división con resto correspondiente.


**3.** **Nivel B.** Sea $n\ge2$. Demuestra que
$$
a\equiv b\pmod n
$$
si y sólo si existe $k\in\mathbb Z$ tal que
$$
a=b+kn.
$$
Explica por qué esta formulación y la definición $n\mid(a-b)$ expresan exactamente la misma información.


**4.** **Nivel B.** Demuestra que dos enteros $a$ y $b$ son congruentes módulo $n$ si y sólo si dejan el mismo resto al dividir por $n$. Debes usar la unicidad del resto del algoritmo de división.


**5.** **Nivel B.** Determina todos los enteros $r\in\{0,1,\ldots,11\}$ tales que
$$
r\equiv 137\pmod{12}.
$$
Después explica por qué existe exactamente uno.


**6.** **Nivel C.** Decide si cada afirmación es verdadera o falsa. Demuestra las verdaderas y da un contraejemplo para las falsas.

a) Si $a\equiv b\pmod n$, entonces $a-b$ es múltiplo de $n$.

b) Si $a-b<n$, entonces $a\not\equiv b\pmod n$.

c) Si $a\equiv b\pmod n$, entonces $a\equiv b\pmod d$ para todo divisor positivo $d$ de $n$ con $d\ge2$.

d) Si $a\equiv b\pmod d$ y $d\mid n$, entonces $a\equiv b\pmod n$.


**7.** **Nivel C.** Sea $a\in\mathbb Z$. Demuestra que existe un único $r\in\{0,\ldots,n-1\}$ tal que
$$
a\equiv r\pmod n.
$$
Distingue claramente la existencia de la unicidad.


**8.** **Nivel C.** Un estudiante escribe:
$$
-17\equiv-2\pmod5
$$
y concluye que “el resto de $-17$ al dividir por $5$ es $-2$”. Diagnostica el error. Explica la diferencia entre un representante cualquiera de una clase y su representante canónico.

## B. Relación de equivalencia y clases residuales


**9.** **Nivel B.** Para un módulo fijo $n\ge2$, demuestra directamente desde la definición que la congruencia módulo $n$ es reflexiva.


**10.** **Nivel B.** Demuestra directamente que la congruencia módulo $n$ es simétrica y señala qué propiedad de la divisibilidad se usa al pasar de $a-b$ a $b-a$.


**11.** **Nivel B.** Demuestra directamente que la congruencia módulo $n$ es transitiva. Tu prueba debe escribir explícitamente
$$
a-c=(a-b)+(b-c).
$$


**12.** **Nivel C.** Describe por extensión las clases
$$
[0]_4,\quad[1]_4,\quad[2]_4,\quad[3]_4
$$
mostrando al menos cinco representantes positivos y cinco negativos de cada una. Explica por qué no existe una quinta clase distinta módulo $4$.


**13.** **Nivel C.** Demuestra que
$$
[a]_n=[b]_n
\iff
a\equiv b\pmod n.
$$
En la implicación de izquierda a derecha usa el hecho de que $a\in[a]_n$.


**14.** **Nivel C.** Decide cuáles de las siguientes igualdades de clases son verdaderas:
$$
[17]_6=[5]_6,\qquad
[-8]_6=[4]_6,\qquad
[21]_8=[5]_8,\qquad
[-15]_7=[6]_7.
$$
Justifica cada respuesta sin listar todos los elementos de las clases.


**15.** **Nivel D.** Demuestra que las clases
$$
[0]_n,[1]_n,\ldots,[n-1]_n
$$
son distintas dos a dos y que su unión es $\mathbb Z$. Concluye que forman una partición de $\mathbb Z$.


**16.** **Nivel D.** Sea $R=\{2,7,12,17,22\}$. Decide si $R$ es un sistema completo de residuos módulo $5$. Si no lo es, explica exactamente qué condición falla. Construye después dos sistemas completos de residuos módulo $5$ que no sean $\{0,1,2,3,4\}$.

## C. Operaciones compatibles y potencias


**17.** **Nivel B.** Supón
$$
a\equiv b\pmod n,
\qquad
c\equiv d\pmod n.
$$
Demuestra
$$
a+c\equiv b+d\pmod n.
$$


**18.** **Nivel B.** Bajo las mismas hipótesis del ejercicio anterior, demuestra
$$
a-c\equiv b-d\pmod n.
$$


**19.** **Nivel C.** Supón
$$
a\equiv b\pmod n,
\qquad
c\equiv d\pmod n.
$$
Demuestra
$$
ac\equiv bd\pmod n.
$$
Hazlo escribiendo $a=b+rn$ y $c=d+sn$.


**20.** **Nivel C.** Demuestra por inducción que
$$
a\equiv b\pmod n
\Longrightarrow
a^m\equiv b^m\pmod n
$$
para todo entero $m\ge1$.


**21.** **Nivel B.** Calcula reduciendo antes de operar:

a) $47+89$ módulo $11$;

b) $123\cdot77$ módulo $13$;

c) $(-38)^2$ módulo $9$;

d) $17^4+8^3$ módulo $5$.

En cada caso muestra al menos una reducción intermedia.


**22.** **Nivel C.** Demuestra que si
$$
a\equiv b\pmod n,
$$
entonces para todo polinomio
$$
P(x)=c_0+c_1x+\cdots+c_rx^r
$$
con coeficientes enteros se cumple
$$
P(a)\equiv P(b)\pmod n.
$$
No uses teoría de anillos.


**23.** **Nivel C.** Usa congruencias para determinar el último dígito de
$$
7^{2026}.
$$
Debes justificar la periodicidad que utilices mediante cálculos de potencias módulo $10$, sin invocar teoremas posteriores.


**24.** **Nivel D.** Demuestra que para todo entero $m$,
$$
m(m+1)
$$
es congruente con $0$ módulo $2$. Después demuestra que
$$
m(m+1)(m+2)
$$
es congruente con $0$ módulo $3$. Formula ambas pruebas usando clases residuales posibles, no factorización prima.

## D. Buena definición, aritmética de clases y cancelación


**25.** **Nivel C.** Sean
$$
[a]_n=[a']_n,
\qquad
[b]_n=[b']_n.
$$
Demuestra que
$$
[a+b]_n=[a'+b']_n.
$$
Explica por qué esto prueba que la suma de clases
$$
[a]_n+[b]_n=[a+b]_n
$$
está bien definida.


**26.** **Nivel C.** Demuestra análogamente que
$$
[ab]_n=[a'b']_n
$$
y concluye que el producto de clases no depende de los representantes elegidos.


**27.** **Nivel B.** Construye las tablas de suma y multiplicación de $\mathbb Z/4\mathbb Z$. Identifica en la tabla de multiplicación dos clases no nulas cuyo producto sea $[0]_4$.


**28.** **Nivel C.** En $\mathbb Z/6\mathbb Z$, calcula
$$
[4]_6+[5]_6,\qquad
[4]_6[5]_6,\qquad
[5]_6^2,\qquad
([2]_6+[5]_6)[4]_6.
$$
Reduce cada resultado a representante canónico.


**29.** **Nivel C.** Da un contraejemplo explícito a la regla de cancelación ingenua
$$
ac\equiv bc\pmod n
\Longrightarrow
a\equiv b\pmod n.
$$
Tu ejemplo debe tener $a\not\equiv b\pmod n$ y $c\not\equiv0\pmod n$.


**30.** **Nivel D.** Demuestra que si
$$
\gcd(c,n)=1
$$
y
$$
ac\equiv bc\pmod n,
$$
entonces
$$
a\equiv b\pmod n.
$$
La prueba debe traducir primero la congruencia a
$$
n\mid c(a-b)
$$
y usar la cancelación coprima de C15.


**31.** **Nivel D.** Supón que $d=\gcd(c,n)>1$. Demuestra que la multiplicación por $[c]_n$ no puede ser inyectiva en $\mathbb Z/n\mathbb Z$ exhibiendo dos clases distintas que tengan la misma imagen. Sugerencia: compara $[0]_n$ y $[n/d]_n$.


**32.** **Nivel D.** Audita la siguiente “prueba”:
$$
18x\equiv18y\pmod{30}
\Longrightarrow
x\equiv y\pmod{30}.
$$
Localiza la operación inválida. Determina la conclusión más fuerte que sí puede deducirse de la congruencia original y justifícala.

## E. Inversos modulares y Bézout


**33.** **Nivel B.** Decide cuáles de las clases
$$
[2]_7,\quad[3]_8,\quad[4]_9,\quad[6]_{15},\quad[11]_{12}
$$
son invertibles en sus respectivos módulos. Justifica cada respuesta mediante el MCD.


**34.** **Nivel C.** Demuestra que si $\gcd(a,n)=1$, entonces $a$ posee inverso módulo $n$. Parte de una identidad de Bézout
$$
au+nv=1.
$$


**35.** **Nivel C.** Demuestra la recíproca: si existe $u$ tal que
$$
au\equiv1\pmod n,
$$
entonces
$$
\gcd(a,n)=1.
$$
Traduce la congruencia a una combinación lineal entera igual a $1$.


**36.** **Nivel C.** Usa Euclides extendido para calcular el inverso de:

a) $17$ módulo $43$;

b) $23$ módulo $64$;

c) $37$ módulo $101$.

Verifica cada inverso por multiplicación.


**37.** **Nivel C.** Demuestra que un inverso modular, si existe, es único como clase módulo $n$. Es decir, si
$$
au\equiv1\pmod n
$$
y
$$
av\equiv1\pmod n,
$$
entonces
$$
u\equiv v\pmod n.
$$


**38.** **Nivel D.** Sea $a$ invertible módulo $n$. Demuestra que la congruencia
$$
ax\equiv b\pmod n
$$
tiene una única solución módulo $n$, y exprésala en términos de un inverso $a^{-1}$.


**39.** **Nivel D.** Determina todos los enteros $a\in\{0,1,\ldots,19\}$ que poseen inverso módulo $20$. Para cada uno calcula un inverso y explica por qué no necesitas probar los enteros restantes por búsqueda exhaustiva de productos.


**40.** **Nivel D.** Un estudiante afirma: “si $a\not\equiv0\pmod n$, entonces $a$ tiene inverso módulo $n$”. Refuta la afirmación con el menor módulo compuesto que te resulte conveniente y formula el criterio correcto.

## F. Congruencias lineales: existencia


**41.** **Nivel C.** Traduce cada congruencia a una ecuación diofántica lineal equivalente:

a) $7x\equiv3\pmod{12}$;

b) $18x\equiv6\pmod{30}$;

c) $14x\equiv5\pmod{21}$.

No resuelvas todavía las ecuaciones.


**42.** **Nivel D.** Sea $d=\gcd(a,n)$. Demuestra la necesidad del criterio de solvencia:
$$
ax\equiv b\pmod n
\Longrightarrow
d\mid b.
$$


**43.** **Nivel D.** Demuestra la suficiencia:
$$
d=\gcd(a,n),\qquad d\mid b
\Longrightarrow
ax\equiv b\pmod n
$$
tiene solución. Usa el criterio diofántico de C15.


**44.** **Nivel C.** Sin hallar las soluciones, decide cuáles de las siguientes congruencias son solubles:

a) $12x\equiv8\pmod{20}$;

b) $12x\equiv7\pmod{20}$;

c) $21x\equiv14\pmod{35}$;

d) $18x\equiv15\pmod{42}$.

En cada caso exhibe $d=\gcd(a,n)$ y prueba o refuta $d\mid b$.


**45.** **Nivel C.** Resuelve
$$
7x\equiv5\pmod{12}
$$
usando un inverso modular. Verifica la solución sustituyendo un representante.


**46.** **Nivel D.** Reduce correctamente
$$
18x\equiv12\pmod{30}
$$
dividiendo por el MCD pertinente. Explica por qué no es correcto simplemente “dividir ambos lados por $6$” y conservar el módulo $30$.


**47.** **Nivel D.** Sea
$$
d=\gcd(a,n),
\qquad
a=da_1,
\qquad
n=dn_1.
$$
Demuestra que
$$
\gcd(a_1,n_1)=1.
$$
Si $d<n$, explica por qué este hecho convierte la congruencia reducida en un problema con coeficiente invertible módulo $n_1$. Señala qué ocurre en el caso extremo $d=n$.


**48.** **Nivel D.** Encuentra todos los enteros $b$ con $0\le b<36$ para los cuales
$$
24x\equiv b\pmod{36}
$$
tiene solución. Describe el conjunto de valores obtenidos mediante una condición de divisibilidad y comprueba tu respuesta contando cuántos hay.

## G. Clasificación y conteo de soluciones


**49.** **Nivel D.** Resuelve completamente
$$
12x\equiv8\pmod{20}.
$$
Determina todas las clases solución módulo $20$ y verifica que su número coincide con $\gcd(12,20)$.


**50.** **Nivel D.** Resuelve completamente
$$
18x\equiv6\pmod{30}.
$$
Debes mostrar: MCD, reducción, solución del problema reducido y levantamiento a todas las clases módulo $30$.


**51.** **Nivel D.** Resuelve completamente
$$
21x\equiv14\pmod{35}
$$
y explica por qué aparecen exactamente siete clases solución módulo $35$.


**52.** **Nivel D.** Determina todas las soluciones de
$$
15x\equiv0\pmod{45}.
$$
Interpreta la respuesta como un caso del teorema general y no como una búsqueda por prueba y error.


**53.** **Nivel E.** Sea $d=\gcd(a,n)$, supón $d\mid b$ y además $d<n$. Si $x_0$ es una solución del problema reducido módulo $n/d$, demuestra que
$$
x_k=x_0+k\frac nd,
\qquad
k=0,\ldots,d-1,
$$
produce $d$ soluciones módulo $n$.


**54.** **Nivel E.** Bajo las hipótesis del ejercicio anterior, demuestra que las $d$ clases
$$
[x_0+k(n/d)]_n
$$
son distintas dos a dos.


**55.** **Nivel E.** Completa la prueba de exhaustividad: demuestra que toda solución de
$$
ax\equiv b\pmod n
$$
es congruente módulo $n$ con una de las $d$ clases del ejercicio 53.


**56.** **Nivel E.** Analiza separadamente los casos extremos de
$$
ax\equiv b\pmod n:
$$

a) $\gcd(a,n)=1$;

b) $n\mid a$.

Determina, según $b$, cuántas soluciones módulo $n$ puede haber en cada caso y relaciona la respuesta con el teorema general.

## H. Sistemas y Teorema Chino del Resto


**57.** **Nivel C.** Resuelve el sistema
$$
x\equiv2\pmod3,
\qquad
x\equiv3\pmod5,
$$
y expresa la respuesta como una única clase módulo $15$. Verifica el resultado en ambas congruencias.


**58.** **Nivel D.** Resuelve
$$
x\equiv4\pmod7,
\qquad
x\equiv5\pmod9,
$$
construyendo una solución mediante un inverso modular. Expresa la solución final módulo $63$.


**59.** **Nivel D.** Sean $\gcd(m,n)=1$ y
$$
rm+sn=1.
$$
Demuestra que
$$
x=a(sn)+b(rm)
$$
satisface
$$
x\equiv a\pmod m,
\qquad
x\equiv b\pmod n.
$$


**60.** **Nivel D.** Demuestra la unicidad en el CRT para dos módulos coprimos: si $x$ e $y$ satisfacen el mismo sistema módulo $m$ y módulo $n$, demuestra
$$
x\equiv y\pmod{mn}.
$$
Señala dónde usas $\gcd(m,n)=1$.


**61.** **Nivel D.** Resuelve
$$
x\equiv1\pmod4,
\qquad
x\equiv2\pmod9,
\qquad
x\equiv3\pmod5.
$$
Expresa la respuesta como una clase módulo $180$ y verifica los tres residuos.


**62.** **Nivel E.** Explica por qué el sistema
$$
x\equiv1\pmod6,
\qquad
x\equiv2\pmod9
$$
no puede resolverse aplicando directamente el CRT coprimo. Decide, sin usar todavía el teorema general del ejercicio 79, si el sistema tiene solución y justifica tu decisión a partir de los residuos módulo $\gcd(6,9)$.


**63.** **Nivel E.** Encuentra el menor entero positivo $x$ que satisface
$$
x\equiv2\pmod5,
\qquad
x\equiv4\pmod7,
\qquad
x\equiv6\pmod{11}.
$$
Después describe todos los enteros que satisfacen el sistema.


**64.** **Nivel E.** Sean $n_1,n_2,n_3$ dos a dos coprimos. Demuestra el caso de tres módulos del CRT aplicando dos veces el caso de dos módulos. Justifica que
$$
\gcd(n_1n_2,n_3)=1.
$$

## I. Síntesis estructural y diagnóstico


**65.** **Nivel D.** Decide si cada afirmación es verdadera o falsa. Demuestra las verdaderas y refuta las falsas.

a) Toda clase no nula módulo $n$ es invertible.

b) Si $a\equiv b\pmod n$, entonces $a^2\equiv b^2\pmod n$.

c) Si $ac\equiv bc\pmod n$ y $c\not\equiv0\pmod n$, entonces $a\equiv b\pmod n$.

d) Si $\gcd(a,n)=1$, entonces $ax\equiv b\pmod n$ tiene exactamente una solución módulo $n$.


**66.** **Nivel D.** Un estudiante resuelve
$$
6x\equiv9\pmod{15}
$$
“dividiendo por $3$” y obtiene
$$
2x\equiv3\pmod{15}.
$$
Explica por qué la reducción es incorrecta, realiza la reducción correcta y determina todas las soluciones módulo $15$.


**67.** **Nivel E.** Demuestra que si $a$ es invertible módulo $n$, entonces las clases
$$
[0]_n,[a]_n,[2a]_n,\ldots,[(n-1)a]_n
$$
son todas distintas. Concluye que los enteros
$$
0,a,2a,\ldots,(n-1)a
$$
forman un sistema completo de residuos módulo $n$.


**68.** **Nivel E.** Demuestra la recíproca del ejercicio anterior: si
$$
[0]_n,[a]_n,\ldots,[(n-1)a]_n
$$
son todas distintas, entonces $\gcd(a,n)=1$.


**69.** **Nivel E.** Sea $n\ge2$. Describe exactamente cuáles clases $[a]_n$ satisfacen
$$
[a]_n^2=[a]_n
$$
para $n=6$. Después explica por qué hallar esas clases es un problema distinto de hallar inversos.


**70.** **Nivel E.** Compara los sistemas
$$
x\equiv1\pmod4,\quad x\equiv3\pmod6
$$
y
$$
x\equiv1\pmod4,\quad x\equiv2\pmod6.
$$
Decide cuál es soluble, determina su solución módulo el MCM de los módulos y explica la compatibilidad o incompatibilidad a través del MCD.


**71.** **Nivel E.** Explica rigurosamente por qué las expresiones
$$
[a]_n+[b]_n
$$
y
$$
[a]_n[b]_n
$$
requieren una prueba de buena definición, mientras que las expresiones
$$
a+b,\qquad ab
$$
en $\mathbb Z$ no plantean ese problema de representantes.


**72.** **Nivel E.** Construye un diagrama de dependencias lógico, acompañado de una explicación escrita, que conecte:
$$
n\mid(a-b),
\quad
a\equiv b\pmod n,
\quad
[a]_n,
\quad
\gcd(a,n)=1,
\quad
a^{-1}\pmod n,
\quad
ax\equiv b\pmod n,
\quad
CRT.
$$
Tu explicación debe indicar qué resultados proceden de C8, C14 y C15.

## M. Problemas avanzados tipo prueba


**73.** **Nivel F.** Sea $n\ge2$. Demuestra desde la definición que $\equiv\pmod n$ es una relación de equivalencia sobre $\mathbb Z$ y prueba rigurosamente que
$$
[a]_n=[b]_n
\iff
a\equiv b\pmod n.
$$
Deduce que las $n$ clases
$$
[0]_n,\ldots,[n-1]_n
$$
forman una partición de $\mathbb Z$. Debes justificar tanto que cubren todo $\mathbb Z$ como que dos clases distintas son disjuntas.


**74.** **Nivel F.** Supón
$$
a\equiv a'\pmod n,
\qquad
b\equiv b'\pmod n.
$$
Demuestra
$$
a+b\equiv a'+b'\pmod n,
\qquad
ab\equiv a'b'\pmod n,
$$
y usa estas implicaciones para justificar completamente que
$$
[a]_n+[b]_n=[a+b]_n,
\qquad
[a]_n[b]_n=[ab]_n
$$
definen operaciones independientes de los representantes elegidos.


**75.** **Nivel G.** Sea $c\in\mathbb Z$ y $n\ge2$. Demuestra la equivalencia entre las siguientes afirmaciones:

1. $\gcd(c,n)=1$;
2. $c$ posee inverso módulo $n$;
3. para todos $a,b\in\mathbb Z$, si
   $$
   ca\equiv cb\pmod n,
   $$
   entonces
   $$
   a\equiv b\pmod n;
   $$
4. las clases
   $$
   [0]_n,[c]_n,[2c]_n,\ldots,[(n-1)c]_n
   $$
   son todas distintas.

Tu prueba debe cerrar el ciclo completo de implicaciones sin usar teoría de grupos.


**76.** **Nivel G.** Sea
$$
d=\gcd(a,n).
$$
Demuestra que
$$
ax\equiv b\pmod n
$$
tiene solución si y sólo si
$$
d\mid b.
$$
En el caso soluble, demuestra además que existen exactamente $d$ clases solución módulo $n$. Si $d<n$, descríbelas a partir de una solución $x_0$ del problema reducido módulo $n/d$; si $d=n$, trata el caso separadamente. La prueba debe establecer existencia, distinción y exhaustividad.


**77.** **Nivel G.** Resuelve completamente
$$
84x\equiv30\pmod{138}
$$
usando Euclides extendido como algoritmo modular. Tu solución deberá incluir:

1. cálculo de $d=\gcd(84,138)$;
2. certificado de solvencia;
3. reducción de la congruencia;
4. construcción de un inverso mediante Bézout;
5. obtención de una clase base de soluciones;
6. levantamiento a las $d$ soluciones módulo $138$;
7. demostración de que no existen otras.


**78.** **Nivel G.** Sean $m,n\ge2$ con
$$
\gcd(m,n)=1.
$$
Demuestra que para cualesquiera $a,b\in\mathbb Z$ el sistema
$$
x\equiv a\pmod m,
\qquad
x\equiv b\pmod n
$$
tiene solución y que ésta es única módulo $mn$. La prueba debe producir explícitamente una solución usando una identidad de Bézout o inversos modulares y tratar existencia y unicidad por separado.


**79.** **Nivel G.** Sean $m,n\ge2$ y
$$
d=\gcd(m,n).
$$
Demuestra que el sistema
$$
x\equiv a\pmod m,
\qquad
x\equiv b\pmod n
$$
tiene solución si y sólo si
$$
d\mid(a-b).
$$
Cuando existe solución, demuestra que es única módulo
$$
\operatorname{lcm}(m,n).
$$
Cuando $d\ge2$, la condición equivale a $a\equiv b\pmod d$; si $d=1$, es automática y no se usa aritmética módulo uno. No invoques una versión general del CRT sin demostrar la parte necesaria.


**80.** **Nivel G.** Sean $n_1,\ldots,n_r\ge2$ dos a dos coprimos y
$$
N=n_1\cdots n_r.
$$
Demuestra que cada clase módulo $N$ determina exactamente una $r$-tupla
$$
([x]_{n_1},\ldots,[x]_{n_r}),
$$
y que toda $r$-tupla posible de clases residuales procede de una única clase módulo $N$. Explica por qué este resultado puede interpretarse como una descomposición de información residual, sin utilizar todavía lenguaje de isomorfismos de anillos.
***
## N. Reglas sobre clases, reconstrucción y compatibilidad

Todos los parámetros son enteros y se respetan los módulos al menos dos. Las condiciones reducidas con divisor uno se expresan directamente por divisibilidad.


**81.** **Nivel E.** Para $n,m\ge2$ y $k,c\in\mathbb Z$, determina cuándo la regla $[a]_n\mapsto[ka+c]_m$ está bien definida. Aplica tu criterio a $[a]_6\mapsto[2a+1]_4$ y $[a]_6\mapsto[a]_4$, y proporciona un contraejemplo para la regla que falle.


**82.** **Nivel E.** Clasifica los módulos $n\ge2$ para los cuales $[a]_n\mapsto[|a|]_n$ está bien definida. Compara con la regla $[a]_n\mapsto[a^2]_n$ en esos mismos módulos.


**83.** **Nivel D.** Módulo seis, se proponen las reglas $F([a]_6)=[\lfloor a/6\rfloor]_2$ y $G([a]_6)=[r(a)]_2$, donde $r(a)$ es el resto canónico al dividir por seis. Decide cuáles definen funciones sobre clases, incluyendo representantes negativos. Si una falla, explica por qué imponer un representante canónico cambia la definición.


**84.** **Nivel E.** Sean $d,n\ge2$. Determina cuándo la frase «$d$ divide al representante $a$» define una propiedad de la clase $[a]_n$. Prueba el criterio en ambos sentidos y contrasta $d=3,n=12$ con $d=8,n=12$.


**85.** **Nivel E.** Para $c\in\mathbb Z$, $n\ge2$ y $d=\gcd(c,n)$, demuestra la equivalencia $ca\equiv cb\pmod n\iff(n/d)\mid(a-b)$. Incluye $c=0$ y explica cuándo puedes expresar el resultado como congruencia con módulo al menos dos. Exhibe todas las clases que colapsan con $[0]_n$.


**86.** **Nivel D.** En los enteros, $a^2=b^2$ obliga a $a=b$ o $a=-b$. Módulo ocho, determina todas las clases $[a]_8$ con $a^2\equiv1\pmod8$ y decide si todas son $[1]_8$ o $[-1]_8$. Relaciona el diagnóstico con $(a-1)(a+1)\equiv0\pmod8$.


**87.** **Nivel D.** Compara las conclusiones de $6x=6y$, $6x\equiv6y\pmod{35}$ y $6x\equiv6y\pmod{42}$. En cada caso determina exactamente la información sobre $x-y$ y muestra por qué no puedes transferir la conclusión del primer caso a los otros.


**88.** **Nivel E.** Sea $H([x]_n)=[cx+t]_n$ con $n\ge2$. Demuestra que es una permutación de las clases exactamente cuando $\gcd(c,n)=1$. Si $d=\gcd(c,n)>1$, clasifica las imágenes posibles y cuenta sus preimágenes. Aplica el resultado a $H([x]_{18})=[6x+5]_{18}$.


**89.** **Nivel D.** Usa el certificado $(-14)\cdot2+35\cdot1=7$ para reconstruir todas las soluciones de $-14x\equiv21\pmod{35}$, tanto como enteros como clases. Determina además los representantes con $-7\le x\le7$ y justifica exhaustividad.


**90.** **Nivel D.** Para resolver $11x\equiv-3\pmod{25}$ se dispone de $1=-9\cdot11+4\cdot25$ y de $1=16\cdot11-7\cdot25$. Reconstruye desde ambos certificados la familia completa de soluciones de $11x-25y=-3$. Explica cómo dos soluciones particulares distintas producen la misma familia.


**91.** **Nivel E.** Para cada $m\in\mathbb Z$, usa $1=3\cdot2-1\cdot5$ para resolver completamente $20x\equiv10m\pmod{50}$. Describe todos los enteros y todas las clases módulo cincuenta, y demuestra que el número de clases no depende de $m$.


**92.** **Nivel E.** Reconstruye todos los enteros que cumplen $12x\equiv6\pmod{18}$ y $7x\equiv4\pmod{10}$. Cuenta después las clases solución módulo noventa. Justifica por qué el menor período positivo de la familia no es noventa.


**93.** **Nivel D.** Determina todos los enteros $x$ con $x\equiv-3\pmod8$ y $x\equiv4\pmod9$. Obtén un testigo mediante $9-8=1$, prueba la unicidad con el módulo pertinente y encuentra todas las soluciones en $[-100,100]$.


**94.** **Nivel E.** Clasifica los $b\in\{0,\ldots,17\}$ para los cuales existe $x$ con $x\equiv5\pmod{12}$ y $x\equiv b\pmod{18}$. Para cada valor permitido, reconstruye todas las soluciones y determina su menor período positivo, sin aplicar el CRT coprimo a doce y dieciocho.


**95.** **Nivel E.** Sean $n=km$ con $m,k\ge2$. Clasifica cuándo $x\equiv a\pmod m$, $x\equiv b\pmod n$ es soluble y reconstruye todas las soluciones sin introducir congruencias módulo uno. Aplica el resultado a $m=8,n=24,a=3$ y todos los restos $0\le b<24$.


**96.** **Nivel E.** Determina los $b\in\{0,\ldots,14\}$ para los cuales es soluble el sistema $x\equiv1\pmod6$, $x\equiv3\pmod{10}$, $x\equiv b\pmod{15}$. Reconstruye todas las soluciones. Explica por qué $b=8$ supera un control de compatibilidad pero falla otro, y por qué no se aplica directamente el CRT dos a dos coprimo.

***
# Soluciones razonadas

## A. Definición, restos y congruencias básicas


### 1

Las cuatro congruencias son verdaderas. En efecto,

$$
37-7=30=3\cdot10,
$$

$$
-11-4=-15=(-3)\cdot5,
$$

$$
26-5=21=3\cdot7,
$$

y

$$
41-(-1)=42=7\cdot6.
$$

En cada caso el módulo divide la diferencia, que es exactamente la definición de congruencia.


### 2

Aplicamos el algoritmo de división con resto no negativo.

$$
-23=7(-4)+5,
$$

por lo que el representante canónico es $5$ módulo $7$.

$$
58=9\cdot6+4,
$$

así que el representante canónico es $4$ módulo $9$.

$$
-101=12(-9)+7,
$$

por lo que el representante canónico es $7$ módulo $12$.

Finalmente,

$$
250=17\cdot14+12,
$$

así que el representante canónico es $12$ módulo $17$.


### 3

Por definición,

$$
a\equiv b\pmod n
\iff
n\mid(a-b).
$$

La divisibilidad $n\mid(a-b)$ significa que existe $k\in\mathbb Z$ tal que

$$
a-b=kn.
$$

Sumando $b$ a ambos lados,

$$
a=b+kn.
$$

Recíprocamente, si $a=b+kn$, entonces $a-b=kn$, de modo que $n\mid(a-b)$ y por tanto $a\equiv b\pmod n$. Las dos formulaciones expresan la misma condición: la diferencia entre $a$ y $b$ es un múltiplo entero del módulo.


### 4

Por el algoritmo de división existen únicos $q_1,q_2\in\mathbb Z$ y $r_1,r_2\in\{0,\ldots,n-1\}$ tales que

$$
a=nq_1+r_1,
\qquad
b=nq_2+r_2.
$$

Si $a\equiv b\pmod n$, entonces $n\mid(a-b)$. Pero

$$
a-b=n(q_1-q_2)+(r_1-r_2),
$$

de donde $n\mid(r_1-r_2)$. Como $|r_1-r_2|<n$, el único múltiplo de $n$ posible es $0$. Luego $r_1=r_2$.

Recíprocamente, si $r_1=r_2$, entonces

$$
a-b=n(q_1-q_2),
$$

así que $n\mid(a-b)$ y $a\equiv b\pmod n$. Por la unicidad del resto, compartir resto y ser congruentes módulo $n$ son condiciones equivalentes.


### 5

Dividimos $137$ por $12$:

$$
137=12\cdot11+5.
$$

Por tanto,

$$
137\equiv5\pmod{12}.
$$

El único $r\in\{0,1,\ldots,11\}$ buscado es

$$
\boxed{r=5}.
$$

La unicidad se debe al algoritmo de división: cada entero posee exactamente un resto en ese intervalo.


### 6

**a) Verdadera.** Es la definición:

$$
a\equiv b\pmod n
\Longrightarrow
n\mid(a-b).
$$

**b) Falsa.** Basta tomar $a=b$. Entonces $a-b=0<n$, pero

$$
a\equiv b\pmod n.
$$

**c) Verdadera.** Si $a\equiv b\pmod n$, entonces $n\mid(a-b)$. Si además $d\mid n$, por transitividad de la divisibilidad se tiene $d\mid(a-b)$, y por tanto

$$
a\equiv b\pmod d.
$$

**d) Falsa.** Tomemos $d=2$, $n=4$, $a=2$ y $b=0$. Entonces

$$
2\equiv0\pmod2,
$$

pero

$$
2\not\equiv0\pmod4.
$$

La congruencia respecto de un divisor del módulo es, en general, una condición más débil.


### 7

**Existencia.** Por el algoritmo de división existen $q\in\mathbb Z$ y $r$ con $0\le r<n$ tales que

$$
a=nq+r.
$$

Así,

$$
a-r=nq,
$$

de modo que $a\equiv r\pmod n$.

**Unicidad.** Supongamos que $r,s\in\{0,\ldots,n-1\}$ satisfacen

$$
a\equiv r\pmod n,
\qquad
a\equiv s\pmod n.
$$

Por simetría y transitividad,

$$
r\equiv s\pmod n,
$$

por lo que $n\mid(r-s)$. Pero $|r-s|<n$. Luego $r-s=0$ y $r=s$.


### 8

La congruencia escrita por el estudiante es correcta:

$$
-17-(-2)=-15,
$$

y $5\mid-15$. Por tanto,

$$
-17\equiv-2\pmod5.
$$

El error está en llamar a $-2$ **el resto**. El resto canónico debe pertenecer a $\{0,1,2,3,4\}$. Como

$$
-17=5(-4)+3,
$$

el resto canónico es $3$. Además,

$$
-2\equiv3\pmod5.
$$

Así, $-2$ es un representante de la misma clase, pero $3$ es su representante canónico.

## B. Relación de equivalencia y clases residuales


### 9

Para todo $a\in\mathbb Z$,

$$
a-a=0.
$$

Como $n\mid0$, por definición

$$
a\equiv a\pmod n.
$$

Por tanto, la congruencia módulo $n$ es reflexiva.


### 10

Si

$$
a\equiv b\pmod n,
$$

entonces $n\mid(a-b)$. Existe $k\in\mathbb Z$ con

$$
a-b=kn.
$$

Multiplicando por $-1$,

$$
b-a=(-k)n,
$$

de modo que $n\mid(b-a)$. Por tanto,

$$
b\equiv a\pmod n.
$$

La propiedad usada es que si un entero divide a otro, también divide a su opuesto.


### 11

Supongamos

$$
a\equiv b\pmod n,
\qquad
b\equiv c\pmod n.
$$

Entonces

$$
n\mid(a-b)
\qquad\text{y}\qquad
n\mid(b-c).
$$

Como los múltiplos de $n$ son cerrados bajo suma,

$$
n\mid[(a-b)+(b-c)].
$$

Pero

$$
a-c=(a-b)+(b-c).
$$

Por tanto $n\mid(a-c)$ y

$$
a\equiv c\pmod n.
$$


### 12

Podemos escribir, por ejemplo,

$$
[0]_4=\{\ldots,-20,-16,-12,-8,-4,0,4,8,12,16,20,\ldots\},
$$

$$
[1]_4=\{\ldots,-19,-15,-11,-7,-3,1,5,9,13,17,21,\ldots\},
$$

$$
[2]_4=\{\ldots,-18,-14,-10,-6,-2,2,6,10,14,18,22,\ldots\},
$$

$$
[3]_4=\{\ldots,-17,-13,-9,-5,-1,3,7,11,15,19,23,\ldots\}.
$$

No existe una quinta clase distinta porque todo entero, al dividirse por $4$, tiene exactamente uno de los restos $0,1,2,3$. Por tanto pertenece a exactamente una de esas cuatro clases.


### 13

Supongamos primero que

$$
[a]_n=[b]_n.
$$

Como $a\in[a]_n$, también $a\in[b]_n$. Por definición de clase,

$$
a\equiv b\pmod n.
$$

Recíprocamente, supongamos $a\equiv b\pmod n$. Si $x\in[a]_n$, entonces $x\equiv a\pmod n$. Por transitividad,

$$
x\equiv b\pmod n,
$$

de modo que $x\in[b]_n$. Así $[a]_n\subseteq[b]_n$. Por simetría del argumento, $[b]_n\subseteq[a]_n$. Luego

$$
[a]_n=[b]_n.
$$


### 14

Todas las igualdades son verdaderas:

$$
17-5=12=2\cdot6,
$$

por lo que $[17]_6=[5]_6$;

$$
-8-4=-12=(-2)\cdot6,
$$

así que $[-8]_6=[4]_6$;

$$
21-5=16=2\cdot8,
$$

por lo que $[21]_8=[5]_8$;

y

$$
-15-6=-21=(-3)\cdot7,
$$

así que $[-15]_7=[6]_7$.


### 15

Primero probamos que las clases son distintas dos a dos. Si

$$
[r]_n=[s]_n,
\qquad
0\le r,s<n,
$$

entonces $r\equiv s\pmod n$, así que $n\mid(r-s)$. Como $|r-s|<n$, necesariamente $r=s$.

Ahora sea $a\in\mathbb Z$. Por el algoritmo de división existe un único $r\in\{0,\ldots,n-1\}$ con

$$
a\equiv r\pmod n.
$$

Por tanto $a\in[r]_n$, y la unión de las $n$ clases es todo $\mathbb Z$.

Finalmente, si dos clases tuvieran un elemento común $x$, tendríamos

$$
x\equiv r\pmod n,
\qquad
x\equiv s\pmod n,
$$

y por simetría y transitividad $r\equiv s\pmod n$. Entonces $r=s$. Por tanto dos clases distintas son disjuntas. Las clases forman, pues, una partición de $\mathbb Z$.


### 16

Todos los elementos de

$$
R=\{2,7,12,17,22\}
$$

son congruentes con $2$ módulo $5$. Por tanto $R$ representa cinco veces la misma clase y no contiene representantes de las otras cuatro. No es un sistema completo de residuos.

Dos ejemplos válidos son

$$
\{-2,-1,0,1,2\}
$$

y

$$
\{5,6,7,8,9\}.
$$

En el primer conjunto los restos canónicos son $3,4,0,1,2$; en el segundo son $0,1,2,3,4$. En ambos casos aparece exactamente una vez cada clase módulo $5$.

## C. Operaciones compatibles y potencias


### 17

De

$$
a\equiv b\pmod n
\qquad\text{y}\qquad
c\equiv d\pmod n
$$

se sigue que $n\mid(a-b)$ y $n\mid(c-d)$. Entonces

$$
(a+c)-(b+d)=(a-b)+(c-d)
$$

es múltiplo de $n$. Por tanto

$$
a+c\equiv b+d\pmod n.
$$


### 18

Bajo las mismas hipótesis,

$$
(a-c)-(b-d)=(a-b)-(c-d).
$$

Como $n$ divide tanto $a-b$ como $c-d$, divide también su diferencia. Luego

$$
a-c\equiv b-d\pmod n.
$$


### 19

Escribamos

$$
a=b+rn,
\qquad
c=d+sn
$$

para ciertos $r,s\in\mathbb Z$. Entonces

$$
ac=(b+rn)(d+sn)
=bd+bsn+drn+rsn^2.
$$

Por tanto

$$
ac-bd=n(bs+dr+rsn),
$$

de modo que $n\mid(ac-bd)$. Así,

$$
ac\equiv bd\pmod n.
$$


### 20

Procedemos por inducción sobre $m\ge1$.

Para $m=1$, la afirmación es exactamente la hipótesis

$$
a\equiv b\pmod n.
$$

Supongamos ahora que

$$
a^m\equiv b^m\pmod n.
$$

Como también $a\equiv b\pmod n$, la compatibilidad con el producto da

$$
a^{m+1}=a^m a\equiv b^m b=b^{m+1}\pmod n.
$$

Por inducción, la afirmación vale para todo $m\ge1$.


### 21

**a)** Módulo $11$,

$$
47\equiv3,
\qquad
89\equiv1.
$$

Luego

$$
47+89\equiv3+1\equiv\boxed4\pmod{11}.
$$

**b)** Módulo $13$,

$$
123\equiv6,
\qquad
77\equiv12\equiv-1.
$$

Por tanto

$$
123\cdot77\equiv6(-1)=-6\equiv\boxed7\pmod{13}.
$$

**c)** Módulo $9$,

$$
-38\equiv7,
$$

así que

$$
(-38)^2\equiv7^2=49\equiv\boxed4\pmod9.
$$

**d)** Módulo $5$,

$$
17\equiv2,
\qquad
8\equiv3.
$$

Entonces

$$
17^4+8^3\equiv2^4+3^3=16+27=43\equiv\boxed3\pmod5.
$$


### 22

Si $a\equiv b\pmod n$, por el ejercicio 20,

$$
a^j\equiv b^j\pmod n
$$

para todo $j\ge1$. Multiplicar una congruencia por el entero $c_j$ conserva la congruencia, de modo que

$$
c_j a^j\equiv c_j b^j\pmod n
$$

para $j\ge1$. El término constante $c_0$ es idéntico en ambos polinomios. Sumando obtenemos

$$
c_0+c_1a+\cdots+c_ra^r
\equiv
c_0+c_1b+\cdots+c_rb^r
\pmod n.
$$

Es decir,

$$
P(a)\equiv P(b)\pmod n.
$$

Sólo se usaron las reglas elementales de congruencia para suma y producto.


### 23

Calculamos las primeras potencias módulo $10$:

$$
7^1\equiv7,
$$

$$
7^2=49\equiv9,
$$

$$
7^3\equiv9\cdot7=63\equiv3,
$$

$$
7^4\equiv3\cdot7=21\equiv1\pmod{10}.
$$

Al multiplicar otra vez por $7$, la sucesión de residuos vuelve a comenzar, por lo que el ciclo tiene longitud $4$:

$$
7,9,3,1,7,9,3,1,\ldots
$$

Como

$$
2026=4\cdot506+2,
$$

tenemos

$$
7^{2026}\equiv7^2\equiv9\pmod{10}.
$$

Por tanto, el último dígito es

$$
\boxed9.
$$


### 24

Módulo $2$, todo entero es congruente con $0$ o con $1$.

- Si $m\equiv0\pmod2$, entonces $m(m+1)\equiv0$.
- Si $m\equiv1\pmod2$, entonces $m+1\equiv0\pmod2$, y de nuevo $m(m+1)\equiv0$.

Así,

$$
m(m+1)\equiv0\pmod2.
$$

Módulo $3$, todo entero es congruente con $0$, $1$ o $2$.

- Si $m\equiv0$, el primer factor es $0$.
- Si $m\equiv1$, entonces $m+2\equiv0$.
- Si $m\equiv2$, entonces $m+1\equiv0$.

En todos los casos uno de los tres factores es congruente con $0$ módulo $3$. Por tanto

$$
m(m+1)(m+2)\equiv0\pmod3.
$$

## D. Buena definición, aritmética de clases y cancelación


### 25

De

$$
[a]_n=[a']_n,
\qquad
[b]_n=[b']_n
$$

se obtiene

$$
a\equiv a'\pmod n,
\qquad
b\equiv b'\pmod n.
$$

Por compatibilidad con la suma,

$$
a+b\equiv a'+b'\pmod n.
$$

Luego

$$
[a+b]_n=[a'+b']_n.
$$

Esto demuestra que, si sustituimos cualquiera de las clases iniciales por otro representante, la clase final no cambia. Por tanto la definición

$$
[a]_n+[b]_n=[a+b]_n
$$

está bien definida.


### 26

De nuevo,

$$
a\equiv a'\pmod n,
\qquad
b\equiv b'\pmod n.
$$

La compatibilidad con el producto da

$$
ab\equiv a'b'\pmod n,
$$

y por tanto

$$
[ab]_n=[a'b']_n.
$$

Así, el producto de clases

$$
[a]_n[b]_n=[ab]_n
$$

no depende de los representantes elegidos.


### 27

La tabla de suma en $\mathbb Z/4\mathbb Z$ es

| $+$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
|---|---|---|---|---|
| $[0]$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
| $[1]$ | $[1]$ | $[2]$ | $[3]$ | $[0]$ |
| $[2]$ | $[2]$ | $[3]$ | $[0]$ | $[1]$ |
| $[3]$ | $[3]$ | $[0]$ | $[1]$ | $[2]$ |

La tabla de multiplicación es

| $\cdot$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
|---|---|---|---|---|
| $[0]$ | $[0]$ | $[0]$ | $[0]$ | $[0]$ |
| $[1]$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
| $[2]$ | $[0]$ | $[2]$ | $[0]$ | $[2]$ |
| $[3]$ | $[0]$ | $[3]$ | $[2]$ | $[1]$ |

En particular,

$$
[2]_4[2]_4=[0]_4,
$$

aunque $[2]_4\ne[0]_4$. Esto muestra que pueden existir clases no nulas cuyo producto sea cero.


### 28

Reducimos siempre módulo $6$:

$$
[4]_6+[5]_6=[9]_6=[3]_6,
$$

$$
[4]_6[5]_6=[20]_6=[2]_6,
$$

$$
[5]_6^2=[25]_6=[1]_6.
$$

Además,

$$
([2]_6+[5]_6)[4]_6
=[7]_6[4]_6
=[1]_6[4]_6
=[4]_6.
$$


### 29

Tomemos módulo $6$:

$$
a=1,
\qquad
b=4,
\qquad
c=2.
$$

Entonces $c\not\equiv0\pmod6$ y

$$
ac=2,
\qquad
bc=8\equiv2\pmod6.
$$

Por tanto

$$
ac\equiv bc\pmod6,
$$

pero

$$
1\not\equiv4\pmod6.
$$

Así, la cancelación puede fallar incluso cuando el factor cancelado no es la clase cero.


### 30

De

$$
ac\equiv bc\pmod n
$$

obtenemos

$$
n\mid(ac-bc)=c(a-b).
$$

Como

$$
\gcd(c,n)=1,
$$

la cancelación coprima de C15 implica

$$
n\mid(a-b).
$$

Por tanto

$$
a\equiv b\pmod n.
$$

La hipótesis de coprimalidad es exactamente la que permite cancelar el factor $c$ dentro de una afirmación de divisibilidad.


### 31

Sea

$$
d=\gcd(c,n)>1.
$$

Las clases

$$
[0]_n
\qquad\text{y}\qquad
\left[\frac nd\right]_n
$$

son distintas, porque

$$
0<\frac nd<n.
$$

Sin embargo,

$$
c\frac nd
=\frac cd\,n,
$$

que es múltiplo de $n$ ya que $d\mid c$. Por tanto

$$
[c]_n[0]_n=[0]_n
$$

y

$$
[c]_n\left[\frac nd\right]_n=[0]_n.
$$

Dos clases distintas tienen la misma imagen; la multiplicación por $[c]_n$ no es inyectiva.


### 32

La inferencia inválida consiste en cancelar $18$ sin comprobar que sea coprimo con $30$. En efecto,

$$
\gcd(18,30)=6\ne1.
$$

La congruencia original equivale a

$$
30\mid18(x-y).
$$

Dividiendo la relación de divisibilidad por $6$ obtenemos

$$
5\mid3(x-y).
$$

Como $\gcd(3,5)=1$, ahora sí podemos cancelar $3$ y concluir

$$
5\mid(x-y).
$$

Por tanto, la conclusión correcta es

$$
\boxed{x\equiv y\pmod5}.
$$

No puede concluirse congruencia módulo $30$: por ejemplo, $x=0$ y $y=5$ satisfacen $18x\equiv18y\pmod{30}$, pero no son congruentes módulo $30$.

## E. Inversos modulares y Bézout


### 33

Una clase $[a]_n$ es invertible exactamente cuando $\gcd(a,n)=1$.

$$
\gcd(2,7)=1,
$$

por lo que $[2]_7$ es invertible.

$$
\gcd(3,8)=1,
$$

por lo que $[3]_8$ es invertible.

$$
\gcd(4,9)=1,
$$

por lo que $[4]_9$ es invertible.

$$
\gcd(6,15)=3,
$$

por lo que $[6]_{15}$ no es invertible.

Finalmente,

$$
\gcd(11,12)=1,
$$

así que $[11]_{12}$ sí es invertible.


### 34

Si

$$
\gcd(a,n)=1,
$$

Bézout garantiza la existencia de $u,v\in\mathbb Z$ tales que

$$
au+nv=1.
$$

Reduciendo módulo $n$ desaparece el término $nv$ y queda

$$
au\equiv1\pmod n.
$$

Por tanto $[u]_n$ es un inverso de $[a]_n$.


### 35

Si

$$
au\equiv1\pmod n,
$$

entonces $n\mid(au-1)$. Existe $k\in\mathbb Z$ tal que

$$
au-1=kn,
$$

o equivalentemente

$$
au-kn=1.
$$

Todo divisor común de $a$ y $n$ divide el miembro izquierdo y, por tanto, divide a $1$. Luego el único divisor común positivo es $1$:

$$
\gcd(a,n)=1.
$$


### 36

**a) Inverso de $17$ módulo $43$.**

El algoritmo de Euclides da

$$
43=2\cdot17+9,
$$

$$
17=9+8,
$$

$$
9=8+1.
$$

Sustituyendo hacia atrás,

$$
1=9-8=2\cdot9-17=2\cdot43-5\cdot17.
$$

Por tanto

$$
17^{-1}\equiv-5\equiv\boxed{38}\pmod{43}.
$$

Verificación: $17\cdot38=646=43\cdot15+1$.

**b) Inverso de $23$ módulo $64$.**

$$
64=2\cdot23+18,
$$

$$
23=18+5,
$$

$$
18=3\cdot5+3,
$$

$$
5=3+2,
$$

$$
3=2+1.
$$

La sustitución hacia atrás produce

$$
1=9\cdot64-25\cdot23.
$$

Así,

$$
23^{-1}\equiv-25\equiv\boxed{39}\pmod{64}.
$$

Verificación: $23\cdot39=897=64\cdot14+1$.

**c) Inverso de $37$ módulo $101$.**

$$
101=2\cdot37+27,
$$

$$
37=27+10,
$$

$$
27=2\cdot10+7,
$$

$$
10=7+3,
$$

$$
7=2\cdot3+1.
$$

Sustituyendo,

$$
1=11\cdot101-30\cdot37.
$$

Luego

$$
37^{-1}\equiv-30\equiv\boxed{71}\pmod{101}.
$$

Verificación: $37\cdot71=2627=101\cdot26+1$.


### 37

Si $au\equiv1\pmod n$ y $av\equiv1\pmod n$, al restar obtenemos

$$
a(u-v)\equiv0\pmod n.
$$

La existencia de un inverso implica $\gcd(a,n)=1$. Por cancelación coprima,

$$
u-v\equiv0\pmod n.
$$

Por tanto

$$
\boxed{u\equiv v\pmod n}.
$$

El inverso puede tener muchos representantes enteros, pero determina una única clase módulo $n$.


### 38

Sea $a^{-1}$ un inverso de $a$ módulo $n$. Multiplicando

$$
ax\equiv b\pmod n
$$

por $a^{-1}$ obtenemos

$$
x\equiv a^{-1}b\pmod n.
$$

Por tanto existe la solución

$$
\boxed{x\equiv a^{-1}b\pmod n}.
$$

Si $x$ e $y$ fueran dos soluciones, entonces $ax\equiv ay\pmod n$. Como $\gcd(a,n)=1$, podemos cancelar $a$ y obtener $x\equiv y\pmod n$. La solución es única como clase.


### 39

Los residuos invertibles módulo $20$ son exactamente los coprimos con $20$:

$$
1,3,7,9,11,13,17,19.
$$

Un inverso para cada uno es:

$$
1^{-1}\equiv1,
\qquad
3^{-1}\equiv7,
\qquad
7^{-1}\equiv3,
\qquad
9^{-1}\equiv9,
$$

$$
11^{-1}\equiv11,
\qquad
13^{-1}\equiv17,
\qquad
17^{-1}\equiv13,
\qquad
19^{-1}\equiv19
\pmod{20}.
$$

Por ejemplo, $3\cdot7=21\equiv1\pmod{20}$ y $13\cdot17=221\equiv1\pmod{20}$.

No es necesario ensayar productos para los demás residuos: el criterio

$$
[a]_{20}\text{ invertible}\iff\gcd(a,20)=1
$$

decide el problema completamente.


### 40

Módulo $4$, la clase $[2]_4$ es no nula, pero no tiene inverso. En efecto,

$$
\gcd(2,4)=2\ne1.
$$

También puede verse directamente: los productos de $2$ por residuos módulo $4$ son sólo $0$ o $2$, nunca $1$.

Por tanto, la condición $a\not\equiv0\pmod n$ no basta. El criterio correcto es

$$
\boxed{a\text{ es invertible módulo }n\iff\gcd(a,n)=1.}
$$

## F. Congruencias lineales: existencia


### 41

Usamos

$$
ax\equiv b\pmod n
\iff
n\mid(ax-b).
$$

Por tanto existe $y\in\mathbb Z$ tal que $ax-b=ny$, es decir,

$$
ax-ny=b.
$$

Así, las tres congruencias son equivalentes a:

**a)**

$$
7x-12y=3.
$$

**b)**

$$
18x-30y=6.
$$

**c)**

$$
14x-21y=5.
$$

En cada caso la variable auxiliar $y$ registra cuántos módulos separan $ax$ de $b$.


### 42

Supongamos

$$
ax\equiv b\pmod n.
$$

Entonces existe $k\in\mathbb Z$ tal que

$$
ax-b=kn,
$$

o bien

$$
b=ax-kn.
$$

Sea

$$
d=\gcd(a,n).
$$

Como $d\mid a$ y $d\mid n$, se tiene $d\mid ax$ y $d\mid kn$. Por tanto $d$ divide su diferencia:

$$
d\mid b.
$$

Esto prueba la necesidad.


### 43

Supongamos

$$
d=\gcd(a,n)
\qquad\text{y}\qquad
d\mid b.
$$

La congruencia

$$
ax\equiv b\pmod n
$$

es equivalente a pedir enteros $x,y$ tales que

$$
ax-ny=b.
$$

Los coeficientes son $a$ y $-n$, cuyo MCD es también $d$. Por el criterio de ecuaciones diofánticas lineales de C15, la ecuación

$$
ax+(-n)y=b
$$

tiene solución entera precisamente porque $d\mid b$.

Por tanto existe $x$ con

$$
ax\equiv b\pmod n.
$$


### 44

Aplicamos el criterio

$$
ax\equiv b\pmod n
\text{ soluble}
\iff
\gcd(a,n)\mid b.
$$

**a)**

$$
\gcd(12,20)=4,
$$

y $4\mid8$. Es soluble.

**b)**

$$
\gcd(12,20)=4,
$$

pero $4\nmid7$. No es soluble.

**c)**

$$
\gcd(21,35)=7,
$$

y $7\mid14$. Es soluble.

**d)**

$$
\gcd(18,42)=6,
$$

pero $6\nmid15$. No es soluble.


### 45

Queremos resolver

$$
7x\equiv5\pmod{12}.
$$

Como

$$
7\cdot7=49\equiv1\pmod{12},
$$

el inverso de $7$ módulo $12$ es $7$. Multiplicamos por él:

$$
x\equiv7\cdot5=35\equiv11\pmod{12}.
$$

Por tanto,

$$
\boxed{x\equiv11\pmod{12}}.
$$

Verificación:

$$
7\cdot11=77\equiv5\pmod{12}.
$$


### 46

Tenemos

$$
\gcd(18,30)=6,
$$

y $6\mid12$. Partimos de

$$
18x\equiv12\pmod{30},
$$

que significa

$$
30\mid18x-12=6(3x-2).
$$

Esto es equivalente a

$$
5\mid3x-2,
$$

o sea,

$$
3x\equiv2\pmod5.
$$

El inverso de $3$ módulo $5$ es $2$, así que

$$
x\equiv4\pmod5.
$$

Como clases módulo $30$, esto produce

$$
\boxed{x\equiv4,9,14,19,24,29\pmod{30}}.
$$

No es correcto dividir por $6$ y conservar el módulo $30$, porque al factorizar

$$
30\mid6(3x-2)
$$

la condición equivalente es $5\mid(3x-2)$: el módulo también se reduce por el mismo factor.


### 47

Sea

$$
d=\gcd(a,n),
\qquad
a=da_1,
\qquad
n=dn_1.
$$

Por Bézout existen $u,v\in\mathbb Z$ tales que

$$
au+nv=d.
$$

Sustituyendo $a=da_1$ y $n=dn_1$,

$$
da_1u+dn_1v=d.
$$

Dividiendo por $d>0$,

$$
a_1u+n_1v=1.
$$

Por el criterio de Bézout,

$$
\gcd(a_1,n_1)=1.
$$

Si $d<n$, entonces $n_1=n/d\ge2$, y en la congruencia reducida el coeficiente $a_1$ es invertible módulo $n_1$. Si $d=n$, entonces $n_1=1$; bajo la convención de este capítulo no hablamos de aritmética módulo $1$, y ese caso se trata separadamente: la congruencia original es soluble exactamente cuando $n\mid b$, y entonces todas las clases módulo $n$ son soluciones.


### 48

Calculamos

$$
\gcd(24,36)=12.
$$

Por el criterio de solvencia,

$$
24x\equiv b\pmod{36}
$$

tiene solución si y sólo si

$$
12\mid b.
$$

Entre $0$ y $35$ los múltiplos de $12$ son

$$
\boxed{0,12,24}.
$$

Hay exactamente tres. Esto coincide con que en un intervalo completo de $36$ enteros aparecen $36/12=3$ múltiplos de $12$.

## G. Clasificación y conteo de soluciones


### 49

Tenemos

$$
d=\gcd(12,20)=4.
$$

Como $4\mid8$, la congruencia es soluble. Dividimos coeficiente, término independiente y módulo por $4$:

$$
3x\equiv2\pmod5.
$$

El inverso de $3$ módulo $5$ es $2$, de modo que

$$
x\equiv4\pmod5.
$$

Al levantar esta clase al módulo $20$, obtenemos

$$
x=4+5k,
\qquad
k=0,1,2,3.
$$

Por tanto las soluciones módulo $20$ son

$$
\boxed{[4]_{20},[9]_{20},[14]_{20},[19]_{20}}.
$$

Hay exactamente $4=d$ soluciones.


### 50

Calculamos

$$
\gcd(18,30)=6.
$$

Como $6\mid6$, dividimos por $6$:

$$
3x\equiv1\pmod5.
$$

El inverso de $3$ módulo $5$ es $2$, así que

$$
x\equiv2\pmod5.
$$

Al levantar al módulo $30$ aparecen las seis clases

$$
x=2+5k,
\qquad
k=0,1,2,3,4,5.
$$

Es decir,

$$
\boxed{x\equiv2,7,12,17,22,27\pmod{30}}.
$$

Hay exactamente $6=\gcd(18,30)$ soluciones.


### 51

Tenemos

$$
\gcd(21,35)=7.
$$

Como $7\mid14$, reducimos:

$$
3x\equiv2\pmod5.
$$

El inverso de $3$ módulo $5$ es $2$, por lo que

$$
x\equiv4\pmod5.
$$

Al levantar al módulo $35$:

$$
x=4+5k,
\qquad
k=0,1,\ldots,6.
$$

Las siete soluciones son

$$
\boxed{x\equiv4,9,14,19,24,29,34\pmod{35}}.
$$

Aparecen exactamente siete porque $d=\gcd(21,35)=7$.


### 52

Aquí

$$
d=\gcd(15,45)=15.
$$

Como $15\mid0$, el teorema general garantiza exactamente $15$ soluciones módulo $45$.

Dividimos por $15$:

$$
x\equiv0\pmod3.
$$

Por tanto, las soluciones son exactamente las clases representadas por los múltiplos de $3$:

$$
\boxed{0,3,6,9,12,15,18,21,24,27,30,33,36,39,42}
$$

módulo $45$.


### 53

Escribamos

$$
a=da_1,
\qquad
b=db_1,
\qquad
n=dn_1,
$$

con $n_1=n/d$. La congruencia reducida es

$$
a_1x\equiv b_1\pmod{n_1}.
$$

Supongamos que $x_0$ es una solución. Para

$$
x_k=x_0+kn_1,
\qquad
k=0,\ldots,d-1,
$$

tenemos

$$
x_k\equiv x_0\pmod{n_1}.
$$

Por tanto

$$
a_1x_k\equiv a_1x_0\equiv b_1\pmod{n_1}.
$$

Esto significa que $n_1\mid(a_1x_k-b_1)$. Multiplicando por $d$,

$$
n\mid(ax_k-b),
$$

y así

$$
ax_k\equiv b\pmod n.
$$

Los $d$ valores propuestos producen, por tanto, soluciones del problema original.


### 54

Supongamos que para $0\le j,k\le d-1$,

$$
x_0+j\frac nd
\equiv
x_0+k\frac nd
\pmod n.
$$

Restando,

$$
n\mid(j-k)\frac nd.
$$

Como $n=d(n/d)$, esto equivale a

$$
d\mid(j-k).
$$

Pero

$$
|j-k|\le d-1.
$$

El único múltiplo de $d$ en ese intervalo es $0$, así que $j=k$. Las $d$ clases son distintas dos a dos.


### 55

Sea $x$ cualquier solución de

$$
ax\equiv b\pmod n.
$$

Con la notación

$$
a=da_1,
\qquad
b=db_1,
\qquad
n=dn_1,
$$

la congruencia se reduce a

$$
a_1x\equiv b_1\pmod{n_1}.
$$

Como

$$
\gcd(a_1,n_1)=1,
$$

esta congruencia reducida tiene una única solución módulo $n_1$. Si $x_0$ es una de ellas, entonces

$$
x\equiv x_0\pmod{n_1}.
$$

Así,

$$
x=x_0+tn_1
$$

para algún $t\in\mathbb Z$. Por división entera por $d>0$, existen únicos $q\in\mathbb Z$ y $k\in\{0,\ldots,d-1\}$ tales que $t=dq+k$. Si $d=1$, esto da directamente $k=0$, sin introducir congruencias módulo uno. Entonces

$$
x\equiv x_0+kn_1\pmod n.
$$

Por tanto toda solución pertenece a una de las $d$ clases construidas en el ejercicio 53. Esto prueba la exhaustividad.


### 56

**a) Caso $\gcd(a,n)=1$.**

Aquí $d=1$. Como $1\mid b$ para todo entero $b$, la congruencia

$$
ax\equiv b\pmod n
$$

siempre es soluble. El teorema general dice que hay exactamente una clase solución módulo $n$. Equivalentemente, $a$ es invertible y

$$
x\equiv a^{-1}b\pmod n.
$$

**b) Caso $n\mid a$.**

Entonces

$$
\gcd(a,n)=n.
$$

El criterio de solvencia exige

$$
n\mid b.
$$

Si $n\nmid b$, no hay soluciones. Si $n\mid b$, entonces

$$
a\equiv0\pmod n,
\qquad
b\equiv0\pmod n,
$$

y la congruencia se convierte en

$$
0\cdot x\equiv0\pmod n,
$$

que satisface toda clase $[x]_n$. Hay exactamente $n$ soluciones módulo $n$, de acuerdo con $d=n$.

## H. Sistemas y Teorema Chino del Resto


### 57

Los enteros congruentes con $2$ módulo $3$ son, entre otros,

$$
2,5,8,11,14,\ldots
$$

De ellos, $8\equiv3\pmod5$. Por tanto

$$
\boxed{x\equiv8\pmod{15}}.
$$

Verificación:

$$
8\equiv2\pmod3,
\qquad
8\equiv3\pmod5.
$$

Como $\gcd(3,5)=1$, el CRT garantiza unicidad módulo $15$.


### 58

Escribimos

$$
x=4+7t.
$$

La segunda congruencia exige

$$
4+7t\equiv5\pmod9,
$$

o sea,

$$
7t\equiv1\pmod9.
$$

Como

$$
7\cdot4=28\equiv1\pmod9,
$$

tenemos

$$
t\equiv4\pmod9.
$$

Entonces

$$
x=4+7\cdot4=32
$$

es una solución. Como $7$ y $9$ son coprimos,

$$
\boxed{x\equiv32\pmod{63}}.
$$

Verificación:

$$
32\equiv4\pmod7,
\qquad
32\equiv5\pmod9.
$$


### 59

Sea

$$
rm+sn=1
$$

y definamos

$$
x=a(sn)+b(rm).
$$

Módulo $m$ tenemos

$$
rm\equiv0\pmod m
$$

y, de la identidad de Bézout,

$$
sn\equiv1\pmod m.
$$

Por tanto

$$
x\equiv a\cdot1+b\cdot0\equiv a\pmod m.
$$

Análogamente, módulo $n$,

$$
sn\equiv0\pmod n,
\qquad
rm\equiv1\pmod n,
$$

por lo que

$$
x\equiv b\pmod n.
$$

La fórmula construye explícitamente una solución del sistema.


### 60

Supongamos que $x$ e $y$ satisfacen el mismo sistema. Entonces

$$
x\equiv y\pmod m
$$

y

$$
x\equiv y\pmod n.
$$

Así,

$$
m\mid(x-y)
\qquad\text{y}\qquad
n\mid(x-y).
$$

Escribamos

$$
x-y=mk.
$$

Como $n\mid mk$ y $\gcd(m,n)=1$, la cancelación coprima de C15 da

$$
n\mid k.
$$

Luego $k=nq$ para algún $q$, y

$$
x-y=mnq.
$$

Por tanto

$$
\boxed{x\equiv y\pmod{mn}}.
$$

La coprimalidad se usa exactamente al pasar de $n\mid mk$ a $n\mid k$.


### 61

Primero resolvemos

$$
x\equiv1\pmod4,
\qquad
x\equiv2\pmod9.
$$

Escribimos $x=1+4t$. Entonces

$$
1+4t\equiv2\pmod9,
$$

de modo que

$$
4t\equiv1\pmod9.
$$

Como $4^{-1}\equiv7\pmod9$,

$$
t\equiv7\pmod9.
$$

Así,

$$
x\equiv29\pmod{36}.
$$

Ahora escribimos $x=29+36s$ y exigimos

$$
29+36s\equiv3\pmod5.
$$

Reduciendo,

$$
4+s\equiv3\pmod5,
$$

por lo que

$$
s\equiv4\pmod5.
$$

Tomando $s=4$ obtenemos

$$
x=29+144=173.
$$

Como $4,9,5$ son dos a dos coprimos,

$$
\boxed{x\equiv173\pmod{180}}.
$$

Verificación:

$$
173\equiv1\pmod4,
\qquad
173\equiv2\pmod9,
\qquad
173\equiv3\pmod5.
$$


### 62

No podemos aplicar directamente el CRT coprimo porque

$$
\gcd(6,9)=3\ne1.
$$

Si existiera una solución, de

$$
x\equiv1\pmod6
$$

se seguiría

$$
x\equiv1\pmod3,
$$

mientras que de

$$
x\equiv2\pmod9
$$

se seguiría

$$
x\equiv2\pmod3.
$$

Eso es imposible. Por tanto el sistema no tiene solución.

La incompatibilidad ya se detecta al comparar los residuos módulo el MCD $3$.


### 63

Partimos de

$$
x\equiv2\pmod5,
$$

así que escribimos

$$
x=2+5a.
$$

Imponemos la segunda congruencia:

$$
2+5a\equiv4\pmod7,
$$

de donde

$$
5a\equiv2\pmod7.
$$

Como $5^{-1}\equiv3\pmod7$,

$$
a\equiv6\pmod7.
$$

Así,

$$
x\equiv32\pmod{35}.
$$

Escribimos ahora

$$
x=32+35b.
$$

Módulo $11$:

$$
32+35b\equiv6,
$$

es decir,

$$
10+2b\equiv6\pmod{11}.
$$

Luego

$$
2b\equiv7\pmod{11}.
$$

Como $2^{-1}\equiv6\pmod{11}$,

$$
b\equiv42\equiv9\pmod{11}.
$$

Tomando $b=9$,

$$
x=32+35\cdot9=347.
$$

El producto de los módulos es

$$
5\cdot7\cdot11=385,
$$

por lo que

$$
\boxed{x\equiv347\pmod{385}}.
$$

El menor entero positivo es $347$, y todos los enteros solución son

$$
\boxed{x=347+385k,
\qquad k\in\mathbb Z.}
$$


### 64

Como

$$
\gcd(n_1,n_2)=1,
$$

el CRT para dos módulos permite combinar las dos primeras congruencias en una única congruencia

$$
x\equiv a\pmod{n_1n_2}.
$$

Necesitamos ahora comprobar

$$
\gcd(n_1n_2,n_3)=1.
$$

Si un primo $p$ dividiera a $n_1n_2$ y a $n_3$, por el lema de Euclides dividiría a $n_1$ o a $n_2$. Eso contradice que $n_3$ sea coprimo con ambos. Por tanto el MCD es $1$.

Aplicamos de nuevo el CRT, ahora a los módulos $n_1n_2$ y $n_3$. Obtenemos una solución, única módulo

$$
(n_1n_2)n_3=n_1n_2n_3.
$$

Esto demuestra el caso de tres módulos.

## I. Síntesis estructural y diagnóstico


### 65

**a) Falsa.** Módulo $6$, la clase $[2]_6$ es no nula pero

$$
\gcd(2,6)=2,
$$

así que no es invertible.

**b) Verdadera.** La compatibilidad con potencias da directamente

$$
a\equiv b\pmod n
\Longrightarrow
a^2\equiv b^2\pmod n.
$$

**c) Falsa.** Módulo $6$,

$$
1\cdot2\equiv4\cdot2\pmod6,
$$

pues $2\equiv8\pmod6$, y $2\not\equiv0\pmod6$. Sin embargo,

$$
1\not\equiv4\pmod6.
$$

**d) Verdadera.** Si $\gcd(a,n)=1$, entonces $a$ es invertible módulo $n$, y

$$
ax\equiv b\pmod n
$$

tiene la única solución

$$
x\equiv a^{-1}b\pmod n.
$$


### 66

La congruencia es

$$
6x\equiv9\pmod{15}.
$$

Como

$$
\gcd(6,15)=3,
$$

y $3\mid9$, dividimos correctamente coeficiente, término independiente y módulo por $3$:

$$
2x\equiv3\pmod5.
$$

No es equivalente mantener el módulo $15$ después de dividir, porque

$$
15\mid3(2x-3)
$$

es equivalente a

$$
5\mid(2x-3),
$$

no a $15\mid(2x-3)$.

El inverso de $2$ módulo $5$ es $3$, de modo que

$$
x\equiv9\equiv4\pmod5.
$$

Levantando al módulo $15$ obtenemos las tres soluciones

$$
\boxed{x\equiv4,9,14\pmod{15}}.
$$


### 67

Supongamos que $a$ es invertible módulo $n$. Consideremos dos índices

$$
0\le i,j<n
$$

y supongamos

$$
[ia]_n=[ja]_n.
$$

Entonces

$$
ia\equiv ja\pmod n.
$$

Como $a$ es invertible, $\gcd(a,n)=1$, y podemos cancelar $a$:

$$
i\equiv j\pmod n.
$$

Pero $i$ y $j$ son representantes canónicos entre $0$ y $n-1$, así que $i=j$.

Por tanto las $n$ clases

$$
[0]_n,[a]_n,\ldots,[(n-1)a]_n
$$

son distintas. Como $\mathbb Z/n\mathbb Z$ contiene exactamente $n$ clases, los enteros

$$
0,a,2a,\ldots,(n-1)a
$$

representan cada clase exactamente una vez y forman un sistema completo de residuos módulo $n$.


### 68

Supongamos que

$$
[0]_n,[a]_n,\ldots,[(n-1)a]_n
$$

son todas distintas. Queremos probar

$$
\gcd(a,n)=1.
$$

Procedemos por contradicción. Si

$$
d=\gcd(a,n)>1,
$$

entonces

$$
1\le\frac nd<n.
$$

Además,

$$
a\frac nd=\frac ad\,n,
$$

que es múltiplo de $n$. Por tanto

$$
\left[\frac nd a\right]_n=[0]_n.
$$

Esto identifica dos términos de la lista correspondientes a índices distintos, contradiciendo la hipótesis. Luego

$$
\boxed{\gcd(a,n)=1}.
$$


### 69

Buscamos las clases $[a]_6$ tales que

$$
a^2\equiv a\pmod6.
$$

Probamos los seis representantes canónicos:

$$
0^2\equiv0,
\qquad
1^2\equiv1,
$$

$$
2^2=4\not\equiv2,
$$

$$
3^2=9\equiv3,
$$

$$
4^2=16\equiv4,
$$

$$
5^2=25\equiv1\not\equiv5
\pmod6.
$$

Por tanto las clases buscadas son

$$
\boxed{[0]_6,[1]_6,[3]_6,[4]_6}.
$$

Éste es un problema distinto de la invertibilidad. Una clase idempotente satisface $e^2=e$; una clase invertible debe admitir $u$ con $eu=1$. Por ejemplo, $[3]_6$ y $[4]_6$ son idempotentes, pero no son invertibles porque

$$
\gcd(3,6)=3,
\qquad
\gcd(4,6)=2.
$$


### 70

Para el primer sistema,

$$
x\equiv1\pmod4,
\qquad
x\equiv3\pmod6,
$$

los módulos tienen

$$
\gcd(4,6)=2.
$$

Los residuos son compatibles módulo $2$ porque

$$
1\equiv3\pmod2.
$$

Resolvemos: escribimos $x=1+4t$ y exigimos

$$
1+4t\equiv3\pmod6.
$$

Entonces

$$
4t\equiv2\pmod6.
$$

Dividiendo por $2$ correctamente,

$$
2t\equiv1\pmod3,
$$

de donde $t\equiv2\pmod3$. Tomando $t=2$ obtenemos $x=9$. Como

$$
\operatorname{lcm}(4,6)=12,
$$

la solución es

$$
\boxed{x\equiv9\pmod{12}}.
$$

Para el segundo sistema,

$$
x\equiv1\pmod4,
\qquad
x\equiv2\pmod6,
$$

los residuos no son compatibles módulo $2$:

$$
1\not\equiv2\pmod2.
$$

Por tanto no hay solución.


### 71

En $\mathbb Z$, los símbolos $a$ y $b$ designan enteros concretos. Una vez fijados esos enteros, $a+b$ y $ab$ tienen valores unívocamente determinados.

En cambio, $[a]_n$ no es un entero concreto, sino una clase con infinitos representantes. Si

$$
[a]_n=[a']_n
\qquad\text{y}\qquad
[b]_n=[b']_n,
$$

podemos intentar calcular usando $a,b$ o usando $a',b'$. Para que

$$
[a]_n+[b]_n=[a+b]_n
$$

y

$$
[a]_n[b]_n=[ab]_n
$$

sean verdaderas **definiciones de operaciones sobre clases**, hay que probar que ambos caminos producen la misma clase final:

$$
[a+b]_n=[a'+b']_n,
$$

$$
[ab]_n=[a'b']_n.
$$

Esa independencia del representante es precisamente la buena definición.


### 72

Una cadena lógica posible es

```text
C14: divisibilidad
n | (a-b)
      ↓ definición
C17: a ≡ b (mod n)
      ↓ C8: relación de equivalencia
[a]_n y partición de Z
      ↓ compatibilidad con + y ·
Z/nZ con operaciones bien definidas
      ↓ C15: MCD + Bézout
 gcd(a,n)=1 ⇔ a posee inverso módulo n
      ↓
 cancelación e inversos
      ↓
 ax ≡ b (mod n)
      ↓ traducción diofántica de C15
 criterio gcd(a,n) | b y clasificación
      ↓
 sistemas de congruencias
      ↓ Bézout + coprimalidad
 CRT
```

La primera flecha usa la divisibilidad desarrollada en C14. El paso de congruencia a clases usa la teoría de relaciones de equivalencia de C8. La caracterización de inversos y la cancelación dependen del MCD y de Bézout de C15. Finalmente, la congruencia lineal se convierte en una ecuación diofántica lineal de C15, y el CRT vuelve a usar Bézout para construir soluciones cuando los módulos son coprimos.

## M. Problemas avanzados tipo prueba


### 73

Fijemos $n\ge2$ y definamos

$$
a\sim b
\iff
a\equiv b\pmod n
\iff
n\mid(a-b).
$$

**Reflexividad.** Como $a-a=0$ y $n\mid0$,

$$
a\sim a.
$$

**Simetría.** Si $n\mid(a-b)$, entonces también

$$
n\mid-(a-b)=b-a,
$$

por lo que $b\sim a$.

**Transitividad.** Si $n\mid(a-b)$ y $n\mid(b-c)$, entonces

$$
n\mid[(a-b)+(b-c)]=a-c,
$$

así que $a\sim c$.

Por tanto la congruencia módulo $n$ es una relación de equivalencia.

Ahora probamos

$$
[a]_n=[b]_n
\iff
a\equiv b\pmod n.
$$

Si las clases son iguales, $a\in[a]_n=[b]_n$, de modo que $a\equiv b\pmod n$.

Recíprocamente, si $a\equiv b\pmod n$ y $x\in[a]_n$, entonces $x\equiv a\pmod n$. Por transitividad,

$$
x\equiv b\pmod n,
$$

así que $x\in[b]_n$. Esto da $[a]_n\subseteq[b]_n$; por simetría se obtiene la inclusión contraria.

Para la partición, el algoritmo de división garantiza que todo $x\in\mathbb Z$ posee un único resto

$$
r\in\{0,\ldots,n-1\}
$$

tal que $x\equiv r\pmod n$. Por tanto cada entero pertenece a alguna de las clases

$$
[0]_n,\ldots,[n-1]_n.
$$

Si dos de ellas, $[r]_n$ y $[s]_n$, tuvieran un elemento común $x$, entonces

$$
x\equiv r\pmod n,
\qquad
x\equiv s\pmod n,
$$

y por simetría y transitividad $r\equiv s\pmod n$. Como $0\le r,s<n$, se sigue $r=s$. Luego dos clases distintas son disjuntas.

Así, las $n$ clases cubren $\mathbb Z$ y son disjuntas dos a dos: forman una partición.


### 74

De

$$
a\equiv a'\pmod n,
\qquad
b\equiv b'\pmod n
$$

se sigue

$$
n\mid(a-a'),
\qquad
n\mid(b-b').
$$

Para la suma,

$$
(a+b)-(a'+b')=(a-a')+(b-b'),
$$

por lo que

$$
a+b\equiv a'+b'\pmod n.
$$

Para el producto usamos

$$
ab-a'b'=a(b-b')+b'(a-a').
$$

Ambos sumandos del lado derecho son múltiplos de $n$, así que

$$
ab\equiv a'b'\pmod n.
$$

Ahora supongamos que elegimos representantes distintos de las mismas clases:

$$
[a]_n=[a']_n,
\qquad
[b]_n=[b']_n.
$$

Entonces las congruencias anteriores implican

$$
[a+b]_n=[a'+b']_n
$$

y

$$
[ab]_n=[a'b']_n.
$$

Por tanto las reglas

$$
[a]_n+[b]_n=[a+b]_n,
$$

$$
[a]_n[b]_n=[ab]_n
$$

son independientes de los representantes y definen operaciones genuinas sobre las clases residuales.


### 75

Probaremos el ciclo

$$
(1)\Longrightarrow(2)\Longrightarrow(3)\Longrightarrow(4)\Longrightarrow(1).
$$

**$(1)\Rightarrow(2)$.** Si

$$
\gcd(c,n)=1,
$$

Bézout da enteros $u,v$ tales que

$$
cu+nv=1.
$$

Reduciendo módulo $n$,

$$
cu\equiv1\pmod n,
$$

así que $c$ posee inverso módulo $n$.

**$(2)\Rightarrow(3)$.** Supongamos que $u$ es un inverso de $c$ y que

$$
ca\equiv cb\pmod n.
$$

Multiplicando por $u$,

$$
uca\equiv ucb\pmod n.
$$

Como $uc\equiv1\pmod n$,

$$
a\equiv b\pmod n.
$$

**$(3)\Rightarrow(4)$.** Supongamos

$$
[ic]_n=[jc]_n
$$

para $0\le i,j<n$. Entonces

$$
ic\equiv jc\pmod n.
$$

Por $3$,

$$
i\equiv j\pmod n.
$$

Como ambos son representantes canónicos, $i=j$. Por tanto las $n$ clases de la lista son distintas.

**$(4)\Rightarrow(1)$.** Supongamos, por contradicción, que

$$
d=\gcd(c,n)>1.
$$

Entonces $k=n/d$ satisface $1\le k<n$, pero

$$
k c=\frac nd c=\frac cd n,
$$

que es múltiplo de $n$. Así,

$$
[kc]_n=[0]_n,
$$

contradiciendo que las clases de la lista sean todas distintas. Por tanto $d=1$.

Las cuatro afirmaciones son equivalentes, sin haber usado teoría de grupos.


### 76

Sea

$$
d=\gcd(a,n).
$$

Probaremos primero el criterio de existencia.

Si

$$
ax\equiv b\pmod n,
$$

entonces existe $k\in\mathbb Z$ tal que

$$
b=ax-kn.
$$

Como $d\mid a$ y $d\mid n$, se sigue $d\mid b$.

Recíprocamente, si $d\mid b$, la ecuación diofántica

$$
ax-ny=b
$$

tiene solución porque el MCD de $a$ y $n$ divide a $b$. Por tanto la congruencia tiene solución. Así,

$$
ax\equiv b\pmod n
\text{ es soluble}
\iff
d\mid b.
$$

Supongamos ahora que $d\mid b$.

Si $d=n$, entonces $n\mid a$ y $n\mid b$, de modo que

$$
ax\equiv b\pmod n
$$

se reduce a $0\equiv0\pmod n$. Por tanto las $n=d$ clases módulo $n$ son soluciones, y no hay nada más que clasificar.

Supongamos desde ahora $d<n$ y escribamos

$$
a=da_1,
\qquad
b=db_1,
\qquad
n=dn_1.
$$

Entonces $n_1=n/d\ge2$ y

$$
\gcd(a_1,n_1)=1.
$$

El problema se reduce a

$$
a_1x\equiv b_1\pmod{n_1}.
$$

Como $a_1$ es invertible módulo $n_1$, existe una única clase solución $x_0$ módulo $n_1$.

Definimos

$$
x_k=x_0+kn_1,
\qquad
k=0,\ldots,d-1.
$$

**Existencia.** Como $x_k\equiv x_0\pmod{n_1}$,

$$
a_1x_k\equiv b_1\pmod{n_1}.
$$

Multiplicando la correspondiente divisibilidad por $d$ obtenemos

$$
ax_k\equiv b\pmod n.
$$

**Distinción.** Si $x_j\equiv x_k\pmod n$, entonces

$$
n\mid(j-k)n_1.
$$

Como $n=dn_1$, resulta $d\mid(j-k)$. Pero $|j-k|<d$, luego $j=k$.

**Exhaustividad.** Si $x$ es cualquier solución original, al dividir por $d$ satisface la congruencia reducida, por lo que

$$
x\equiv x_0\pmod{n_1}.
$$

Así $x=x_0+tn_1$ para algún $t$. Dividiendo $t$ por el entero positivo $d$, escribimos $t=dq+k$, con $0\le k<d$. Entonces $x=x_0+kn_1+qn$, y por tanto su clase es $[x_k]_n$. El resto $k$ es único; si $d=1$, es cero y no se introduce congruencia módulo uno.

En conclusión, cuando $d\mid b$ existen exactamente $d$ soluciones módulo $n$:

$$
\boxed{
x\equiv x_0+k\frac nd\pmod n,
\qquad
k=0,\ldots,d-1.
}
$$


### 77

Queremos resolver

$$
84x\equiv30\pmod{138}.
$$

**1. Cálculo del MCD.**

El algoritmo de Euclides da

$$
138=84+54,
$$

$$
84=54+30,
$$

$$
54=30+24,
$$

$$
30=24+6,
$$

$$
24=4\cdot6.
$$

Por tanto

$$
\boxed{d=\gcd(84,138)=6}.
$$

**2. Certificado de solvencia.**

Como

$$
6\mid30,
$$

la congruencia es soluble.

**3. Reducción.**

Dividimos por $6$:

$$
14x\equiv5\pmod{23}.
$$

**4. Inverso mediante Bézout.**

Tenemos

$$
23=14+9,
$$

$$
14=9+5,
$$

$$
9=5+4,
$$

$$
5=4+1.
$$

Sustituyendo hacia atrás,

$$
1=5-4
=2\cdot5-9
=2\cdot14-3\cdot9
=5\cdot14-3\cdot23.
$$

Luego

$$
14^{-1}\equiv5\pmod{23}.
$$

**5. Clase base.**

Multiplicamos por $5$:

$$
x\equiv25\equiv2\pmod{23}.
$$

**6. Levantamiento a módulo $138$.**

Como $d=6$ y $138/6=23$, las soluciones son

$$
x=2+23k,
\qquad
k=0,1,2,3,4,5.
$$

Por tanto

$$
\boxed{x\equiv2,25,48,71,94,117\pmod{138}}.
$$

**7. Exhaustividad.**

Toda solución del problema original reduce a una solución de

$$
14x\equiv5\pmod{23}.
$$

Esta congruencia reducida tiene una única clase solución módulo $23$, porque $14$ es invertible. Por tanto toda solución original satisface $x\equiv2\pmod{23}$, y al pasar a módulo $138$ sólo aparecen las seis clases anteriores. No existen otras.


### 78

Supongamos

$$
\gcd(m,n)=1.
$$

Por Bézout existen $r,s\in\mathbb Z$ tales que

$$
rm+sn=1.
$$

Definamos

$$
x_0=a(sn)+b(rm).
$$

**Existencia.** Módulo $m$,

$$
rm\equiv0,
\qquad
sn\equiv1,
$$

por lo que

$$
x_0\equiv a\pmod m.
$$

Módulo $n$,

$$
sn\equiv0,
\qquad
rm\equiv1,
$$

de modo que

$$
x_0\equiv b\pmod n.
$$

Así existe una solución explícita.

**Unicidad.** Si $x$ e $y$ satisfacen el sistema, entonces

$$
m\mid(x-y)
\qquad\text{y}\qquad
n\mid(x-y).
$$

Escribamos $x-y=mk$. Como $n\mid mk$ y $\gcd(m,n)=1$, la cancelación coprima da $n\mid k$. Por tanto $k=nq$ y

$$
x-y=mnq.
$$

Luego

$$
x\equiv y\pmod{mn}.
$$

El sistema tiene, por tanto, una solución única módulo $mn$.


### 79

Sea

$$
d=\gcd(m,n).
$$

**Necesidad.** Supongamos que $x$ satisface

$$
x\equiv a\pmod m,
\qquad
x\equiv b\pmod n.
$$

Entonces existen $u,v\in\mathbb Z$ tales que

$$
x-a=mu,
\qquad
x-b=nv.
$$

Restando,

$$
b-a=mu-nv.
$$

Como $d\mid m$ y $d\mid n$,

$$
d\mid(b-a),
$$

por lo que

$$
d\mid(a-b).
$$

Si $d=1$, la divisibilidad se cumple siempre; para $d\ge2$ puede expresarse como congruencia módulo $d$.

**Suficiencia.** Supongamos ahora

$$
d\mid(a-b).
$$

Entonces $d\mid(b-a)$. Escribamos

$$
m=dm_1,
\qquad
n=dn_1,
$$

con

$$
\gcd(m_1,n_1)=1.
$$

Buscamos una solución de la forma

$$
x=a+mt.
$$

La segunda congruencia exige

$$
a+mt\equiv b\pmod n,
$$

o sea,

$$
mt\equiv b-a\pmod n.
$$

Dividiendo por $d$, la condición equivale a la ecuación diofántica

$$
m_1t-n_1s=\frac{b-a}{d}
$$

para algún $s\in\mathbb Z$. Como

$$
\gcd(m_1,n_1)=1,
$$

el criterio de C15 garantiza una solución entera $(t,s)$, incluso en el caso extremo $n_1=1$. Por tanto existe $x=a+mt$ que satisface ambas congruencias.

Hemos probado

$$
\boxed{
\text{el sistema es soluble}
\iff
d\mid(a-b).
}
$$

**Unicidad.** Si $x$ e $y$ son dos soluciones, entonces

$$
m\mid(x-y),
\qquad
n\mid(x-y).
$$

Escribimos $x-y=mq=dm_1q$. Como $n=dn_1$ divide a $dm_1q$, se tiene

$$
n_1\mid m_1q.
$$

La coprimalidad $\gcd(m_1,n_1)=1$ implica

$$
n_1\mid q.
$$

Por tanto $q=n_1s$ y

$$
x-y=mn_1s
=\frac{mn}{d}s.
$$

Pero

$$
\operatorname{lcm}(m,n)=\frac{mn}{d}.
$$

Así,

$$
\boxed{x\equiv y\pmod{\operatorname{lcm}(m,n)}}.
$$

Además, sumar un múltiplo del MCM conserva ambas congruencias, de modo que ése es exactamente el módulo natural de unicidad.


### 80

Sea

$$
N=n_1\cdots n_r,
$$

donde los módulos son dos a dos coprimos. Consideremos la regla que a una clase $[x]_N$ asigna la tupla

$$
([x]_{n_1},\ldots,[x]_{n_r}).
$$

**Buena definición.** Si

$$
[x]_N=[y]_N,
$$

entonces $N\mid(x-y)$. Como cada $n_i$ divide a $N$,

$$
n_i\mid(x-y)
$$

para todo $i$. Luego

$$
[x]_{n_i}=[y]_{n_i}
$$

para cada componente. La tupla no depende del representante de $[x]_N$.

**Unicidad de la clase que produce una tupla.** Supongamos que $x$ e $y$ producen la misma tupla. Entonces

$$
n_i\mid(x-y)
$$

para todo $i$. Como los $n_i$ son dos a dos coprimos, su producto divide a $x-y$. Esto puede demostrarse inductivamente usando la cancelación coprima: si $n_1\cdots n_{k-1}\mid(x-y)$ y $n_k\mid(x-y)$, la coprimalidad de $n_k$ con el producto anterior implica

$$
n_1\cdots n_k\mid(x-y).
$$

Al final,

$$
N\mid(x-y),
$$

por lo que

$$
[x]_N=[y]_N.
$$

**Existencia para toda tupla.** Sea dada una tupla arbitraria

$$
([a_1]_{n_1},\ldots,[a_r]_{n_r}).
$$

Para cada $i$ definimos

$$
N_i=\frac N{n_i}.
$$

La coprimalidad dos a dos implica

$$
\gcd(N_i,n_i)=1,
$$

por lo que existe $u_i$ tal que

$$
N_i u_i\equiv1\pmod{n_i}.
$$

Definimos

$$
x=\sum_{i=1}^r a_iN_i u_i.
$$

Fijemos $j$. Si $i\ne j$, entonces $n_j\mid N_i$, de modo que el término $a_iN_i u_i$ es $0$ módulo $n_j$. El término con $i=j$ satisface

$$
a_jN_j u_j\equiv a_j\pmod{n_j}.
$$

Por tanto

$$
x\equiv a_j\pmod{n_j}
$$

para todo $j$. La tupla dada procede de la clase $[x]_N$.

Así, cada clase módulo $N$ determina exactamente una tupla de clases residuales y toda tupla posible procede de exactamente una clase módulo $N$.

Conceptualmente, el resultado dice que la información de un entero módulo el producto $N$ puede separarse completamente en sus residuos respecto de los factores coprimos y reconstruirse sin pérdida a partir de ellos. Ésta es una descomposición de información residual; no necesitamos todavía formularla en lenguaje de isomorfismos de anillos.

## N. Reglas sobre clases, reconstrucción y compatibilidad


### 81

Si $a'=a+nt$, la diferencia de salidas es $k(a'-a)=knt$. Por tanto $m\mid kn$ garantiza que las salidas representan la misma clase para todos $t$, y la regla queda bien definida. Recíprocamente, cero y $n$ representan la misma clase de entrada; sus salidas difieren en $kn$, así que la buena definición exige $m\mid kn$. Éste es el criterio necesario y suficiente; el término $c$ desaparece en la diferencia.

En la primera regla, $4\mid2\cdot6=12$, luego funciona. Por ejemplo, cero y seis producen uno y trece, congruentes módulo cuatro. En la segunda, cuatro no divide a seis: $[0]_6=[6]_6$, pero $[0]_4\ne[6]_4=[2]_4$. La buena definición entre módulos distintos no exige necesariamente que el módulo de salida divida al de entrada; el coeficiente puede compensar la diferencia.


### 82

Los enteros uno y $1-n$ son congruentes módulo $n$. Sus valores absolutos son uno y $n-1$, cuya diferencia es $n-2$. Si la regla es válida, $n\mid(n-2)$ y, por diferencia, $n\mid2$. Con $n\ge2$, necesariamente $n=2$. Si $n>2$, esos mismos representantes proporcionan un contraejemplo.

Para $n=2$, $|a|-a$ es cero si $a\ge0$ y es $-2a$ si $a<0$; siempre es múltiplo de dos. Así $|a|\equiv a\pmod2$. Si $a\equiv b\pmod2$, entonces $|a|\equiv|b|\pmod2$, de modo que la regla es válida. La clasificación es exhaustiva.

La regla del cuadrado funciona para todo $n\ge2$: si $a'=a+nt$, $(a')^2-a^2=nt(2a+nt)$ es múltiplo de $n$. No se puede trasladar sin prueba al valor absoluto la independencia que sí tiene el cuadrado.


### 83

En la división $a=6q+r$, $0\le r<6$, el cociente es $q=\lfloor a/6\rfloor$. Cero y seis representan la misma clase módulo seis, pero sus cocientes son cero y uno, que representan clases distintas módulo dos. Por tanto $F$ no está bien definida. También $-1=6(-1)+5$ y $5=6\cdot0+5$ dan cocientes menos uno y cero, otra falla con representante negativo.

La regla $G$ sí funciona: representantes congruentes módulo seis tienen el mismo resto canónico, luego el mismo resto módulo dos. En particular, menos uno y cinco dan ambos $[5]_2=[1]_2$. Esto es un argumento universal apoyado en la unicidad del resto.

Si primero se elige el representante canónico $r\in\{0,\ldots,5\}$ y después se aplica $F$, su cociente por seis es siempre cero. Esa nueva regla es la función constante $[0]_2$. No coincide con la propuesta original para representantes arbitrarios: al usar seis, la propuesta devolvía $[1]_2$. La selección canónica debe aparecer expresamente.


### 84

Si $d\mid n$ y $a'=a+nt$, de $d\mid a$ se deduce $d\mid a'$. El argumento inverso usa $a=a'-nt$. Por tanto la verdad de $d\mid a$ no cambia de representante y define una propiedad de la clase.

Recíprocamente, si es una propiedad de clases, cero y $n$ deben recibir el mismo valor de verdad. Como $d\mid0$, debe cumplirse $d\mid n$. Éste es el criterio completo.

Con $d=3,n=12$, funciona: sumar un múltiplo de doce conserva la divisibilidad por tres. Con $d=8,n=12$, falla: cero y doce pertenecen a la misma clase módulo doce, pero ocho divide a cero y no divide a doce. Tener un MCD no trivial entre $d$ y $n$ no basta; se necesita la divisibilidad completa del módulo por $d$.


### 85

Escribimos $c=dc_1$, $n=dn_1$, con $n_1=n/d>0$ y $\gcd(c_1,n_1)=1$. La congruencia equivale a $dn_1\mid dc_1(a-b)$, es decir, $n_1\mid c_1(a-b)$. Por cancelación coprima, esto equivale a $n_1\mid(a-b)$. El converso también se verifica directamente multiplicando el testigo por $c_1$.

Si $d<n$, $n_1\ge2$ y escribimos $a\equiv b\pmod{n_1}$. Si $d=n$, $n_1=1$ y la divisibilidad se cumple para todos los enteros; no introducimos congruencias módulo uno. En particular, $c=0$ da $d=n$ y todas las clases tienen la misma imagen cero.

Tomando $b=0$, las clases que van a cero son exactamente $[jn_1]_n$, $j=0,\ldots,d-1$. Son distintas porque $n\mid(j-k)n_1$ equivale a $d\mid j-k$. Toda solución entera $a=n_1t$ pertenece a una de ellas al escribir $t=dq+j$, $0\le j<d$, por división entera. Para $d=1$ el único resto es cero, sin congruencia módulo uno. Por tanto son todas y hay exactamente $d$.


### 86

En los enteros, $(a-b)(a+b)=0$ fuerza que uno de los factores sea cero, porque un producto de dos enteros no nulos no puede valer cero. Módulo ocho, esa propiedad no está disponible.

Examinamos los ocho restos canónicos. Los cuadrados de $0,1,2,3,4,5,6,7$ tienen restos $0,1,4,1,0,1,4,1$, respectivamente. Por tanto las soluciones son $[1]_8,[3]_8,[5]_8,[7]_8$, y todas las soluciones enteras son los enteros impares. La lista es exhaustiva porque cada entero tiene uno de esos ocho restos y el cuadrado respeta la congruencia.

Las clases $[3]_8$ y $[5]_8$ son distintas de $[1]_8$ y $[-1]_8=[7]_8$. Para $a=3$, el producto $(a-1)(a+1)=2\cdot4=8$ es congruente con cero, aunque ninguno de los factores lo sea. No se puede concluir que un factor es cero ni cancelar dos módulo ocho, pues $\gcd(2,8)=2$. La factorización algebraica sigue siendo válida; falla la inferencia adicional sobre el producto.


### 87

En la igualdad entera, seis es no nulo y se cancela: $x-y=0$, luego $x=y$. En módulo 35, $\gcd(6,35)=1$, y la cancelación modular da $35\mid x-y$. El converso es inmediato; por tanto la información exacta es $x\equiv y\pmod{35}$. No fuerza igualdad: $x=0,y=35$ es un ejemplo.

En módulo 42, $42\mid6(x-y)$ equivale a $7\mid x-y$. Por tanto la conclusión exacta es $x\equiv y\pmod7$. El converso se verifica escribiendo $x-y=7t$, que da $6(x-y)=42t$. No implica congruencia módulo 42: cero y siete satisfacen la hipótesis y pertenecen a clases distintas módulo 42.

En términos de clases, multiplicar por $[6]_{35}$ es inyectivo, mientras que módulo 42 identifica las seis clases $[y+7j]_{42}$, $j=0,\ldots,5$, con la misma imagen. Igualdad de enteros, igualdad de clases y divisibilidad por el módulo reducido tienen conclusiones distintas.


### 88

La regla está bien definida porque cambiar $x$ en un múltiplo de $n$ cambia $cx+t$ en otro múltiplo de $n$. La clase $[b]_n$ tiene preimagen exactamente cuando $cx\equiv b-t\pmod n$ es soluble. El criterio lineal dice que esto sucede si y sólo si $d\mid b-t$, y en tal caso hay exactamente $d$ clases preimagen.

Las imágenes son las $n/d$ clases representadas por $t+dj$, $j=0,\ldots,n/d-1$. Son distintas: si $n\mid d(j-k)$, entonces $n/d\mid j-k$, y el intervalo obliga a $j=k$. Si $d=1$, todo destino tiene una única preimagen, así que la regla es una permutación. Si $d>1$, hay menos de $n$ imágenes y cada una tiene $d$ preimágenes, por lo que no es una permutación. Esto incluye $d=n$, que produce una función constante.

En el ejemplo, $d=6$ y las imágenes son $[5],[11],[17]$ módulo 18. Para cinco, la condición es $x\equiv0\pmod3$, con restos $0,3,6,9,12,15$; para once, $x\equiv1\pmod3$, con $1,4,7,10,13,16$; para diecisiete, $x\equiv2\pmod3$, con $2,5,8,11,14,17$. Las tres listas cubren todas las dieciocho entradas.


### 89

El certificado es cierto: menos veintiocho más treinta y cinco es siete. Como siete divide a ambas entradas, el MCD es siete. Multiplicar la identidad por tres da $(-14)\cdot6+35\cdot3=21$, de donde $x_0=6$ es solución.

La condición $35\mid-14x-21$ equivale a $5\mid-2x-3$, y ésta a $x\equiv1\pmod5$, pues el inverso de menos dos módulo cinco es dos. Todas las soluciones enteras son $x=1+5t$, $t\in\mathbb Z$. La equivalencia prueba exhaustividad y la sustitución verifica $-14(1+5t)-21=-35-70t$.

Módulo 35 hay siete clases: $[1],[6],[11],[16],[21],[26],[31]$. Reducir $t$ módulo siete las obtiene todas y sus diferencias muestran que son distintas. En el intervalo dado, $-7\le1+5t\le7$ equivale a $-8\le5t\le6$, y los únicos enteros son $t=-1,0,1$. Los representantes permitidos son menos cuatro, uno y seis. No son una lista completa de clases módulo 35; responden a la restricción adicional.


### 90

Ambas identidades valen uno: $-99+100=1$ y $176-175=1$. Al multiplicar la primera por menos tres, $-3=27\cdot11-12\cdot25$, obtenemos $(x_0,y_0)=(27,12)$. La segunda entrega $-3=-48\cdot11+21\cdot25$, luego $(x_1,y_1)=(-48,-21)$.

Las familias son $(27+25t,12+11t)$ y $(-48+25s,-21+11s)$, con parámetros enteros. Sustituir cualquiera verifica la ecuación. Si $(x,y)$ es una solución arbitraria, restar la primera da $11(x-27)=25(y-12)$. Como el certificado prueba coprimalidad, $25\mid x-27$ y luego $y-12=11t$. Esto prueba exhaustividad.

Las dos familias coinciden mediante $s=t+3$: sus coordenadas se vuelven iguales. También se puede usar la pareja $(2,1)$, obtenida en la primera familia con $t=-1$, y escribir $(2+25u,1+11u)$. La congruencia tiene una sola clase $[2]_{25}$, pero la ecuación diofántica tiene infinitas parejas enteras. La libertad de Bézout cambia el punto de partida, no el conjunto de soluciones.


### 91

El MCD de veinte y cincuenta es diez, que divide a $10m$ para cualquier entero $m$. La congruencia equivale a $5\mid2x-m$, es decir, $2x\equiv m\pmod5$. El certificado muestra que tres es inverso de dos módulo cinco, luego todas las soluciones enteras son $x=3m+5t$, $t\in\mathbb Z$.

Para cualquier solución, multiplicar la congruencia reducida por tres obliga a $x\equiv3m\pmod5$, así que la familia es exhaustiva. Recíprocamente, $20(3m+5t)-10m=50m+100t$ es múltiplo de cincuenta.

Las clases son $[3m+5j]_{50}$, $j=0,\ldots,9$. Si dos coinciden, cincuenta divide a $5(j-k)$, luego diez divide a $j-k$ y el intervalo obliga a $j=k$. Toda solución entera pertenece a una de ellas al dividir su parámetro por diez. Hay exactamente diez clases para cada $m$, aunque sus representantes cambien. El certificado reducido funciona también cuando $m$ es cero o negativo.


### 92

La primera congruencia se reduce por el MCD seis a $2x\equiv1\pmod3$, luego $x\equiv2\pmod3$. La segunda tiene coeficiente invertible: $7\cdot3=21\equiv1\pmod{10}$, y da $x\equiv12\equiv2\pmod{10}$. Por tanto $x-2$ es múltiplo de tres y diez. Como son coprimos, es múltiplo de treinta. Todas las soluciones son $x=2+30t$, $t\in\mathbb Z$.

La construcción verifica ambas congruencias: $12(2+30t)-6=18+360t$ es múltiplo de dieciocho y $7(2+30t)-4=10+210t$ es múltiplo de diez. La deducción desde una solución arbitraria prueba exhaustividad.

Módulo noventa, reducir $t$ módulo tres entrega exactamente $[2],[32],[62]$. Son distintas. Treinta es el menor período positivo de la familia: si un desplazamiento $T>0$ conserva todas sus soluciones, en particular convierte dos en otra solución, de modo que $T=30t$ con $t\ge1$. Noventa también es un período, pero no el menor. El período correcto procede de los módulos reducidos, no del producto de los módulos originales.


### 93

La identidad proporciona los selectores nueve y menos ocho. El testigo es $x_0=(-3)\cdot9+4(-8)=-59$. Éste satisface $-59+3=-56=8(-7)$ y $-59-4=-63=9(-7)$.

Si $x$ es otra solución, $x+59$ es divisible por ocho y nueve. Escribimos $x+59=8k$; de $9\mid8k$ y coprimalidad se sigue $9\mid k$, luego $x+59$ es múltiplo de 72. Recíprocamente, sumar $72t$ conserva ambas congruencias. Así todas las soluciones son $-59+72t$, $t\in\mathbb Z$, o $13+72u$ con $u\in\mathbb Z$.

En el intervalo, $-100\le13+72u\le100$ equivale a $-113\le72u\le87$, cuyos parámetros enteros son $u=-1,0,1$. Las soluciones son menos cincuenta y nueve, trece y ochenta y cinco. La unicidad es de la clase módulo 72; la existencia de tres enteros en el intervalo no la contradice.


### 94

Escribimos $x=5+12t$. La segunda condición equivale a $18\mid5+12t-b$. Como seis divide a doce y dieciocho, se necesita $6\mid b-5$. En el intervalo dado, los valores son $b=5,11,17$, que escribimos $b=5+6s$ con $s=0,1,2$.

Para esos valores, la condición se reduce a $3\mid2t-s$, de donde $t\equiv2s\pmod3$. Por tanto todas las soluciones son $x=5+24s+36u$, $u\in\mathbb Z$. La sustitución verifica ambos residuos y las equivalencias anteriores prueban exhaustividad. Los restos canónicos módulo 36 son cinco, veintinueve y diecisiete, respectivamente.

El menor período positivo es 36. Una diferencia entre dos soluciones es múltiplo de doce y dieciocho; escribirla como $12k$ obliga a $3\mid2k$, luego $3\mid k$, así que es múltiplo de 36. Treinta y seis sí conserva ambas condiciones. El producto 216 también conserva los residuos, pero no expresa la única clase natural: cada familia contiene seis clases módulo 216. La compatibilidad se decidió antes de construir.


### 95

Si $x\equiv b\pmod n$, entonces $x=b+nt=b+kmt$ y, por tanto, $x\equiv b\pmod m$. La primera condición requiere $m\mid b-a$. Esta condición es necesaria y también suficiente: si se cumple, todo entero $b+nt$ satisface ambas congruencias. Ésa es la familia completa, porque la segunda condición ya obliga a esa forma.

El menor período positivo es $n$: cualquier desplazamiento entre soluciones es múltiplo de $n$, y $n$ conserva ambas condiciones. No se divide un módulo hasta uno ni se busca un inverso en ese módulo; la inclusión de divisibilidades resuelve directamente el caso.

En el ejemplo, $8\mid b-3$ y $0\le b<24$ permiten exactamente $b=3,11,19$. Para cada valor, todas las soluciones son $b+24t$, $t\in\mathbb Z$. Los otros restos son incompatibles. Compartir factores no implica imposibilidad; aquí el módulo mayor determina el conjunto completo si sus datos respetan el módulo menor.


### 96

De la primera condición, $x=1+6t$. La segunda exige $6t\equiv2\pmod{10}$, equivalente a $3t\equiv1\pmod5$. Como tres tiene inverso dos, $t=2+5u$ y $x=13+30u$, $u\in\mathbb Z$. Toda pareja de las dos primeras condiciones queda descrita así, y la sustitución confirma ambas.

Estos enteros tienen resto trece módulo quince. Por tanto, en el intervalo indicado, sólo $b=13$ permite la tercera condición. Para ese valor, todas las soluciones siguen siendo $13+30u$. Treinta es el menor período positivo, porque las diferencias entre soluciones ya son exactamente múltiplos de treinta; sumar treinta conserva los tres residuos.

El valor ocho es congruente con tres módulo cinco, de modo que supera el control entre módulos diez y quince. Pero ocho no es congruente con uno módulo tres, así que falla el control entre seis y quince. Los módulos tienen MCD dos, tres y cinco por pares; no son dos a dos coprimos y el CRT de producto no se puede aplicar sin analizar los datos. La reconstrucción directa establece suficiencia para trece y descarta exhaustivamente los otros catorce valores.

***

[← Capítulo 16](algebra-para-matematicos-capitulo-16-numeros-primos-y-factorizacion.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 18 →](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md)
