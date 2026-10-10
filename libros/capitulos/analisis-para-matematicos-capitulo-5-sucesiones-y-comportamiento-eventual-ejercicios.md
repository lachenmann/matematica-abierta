---
title: "Ejercicios — Capítulo 5"
content-id: MA-BCH-0180
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-005-EJERCICIOS
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-10-07
date-modified: 2026-10-07
areas: [analisis]
level: universitario
topics: [analisis-real, sucesiones, eventualidad]
prerequisites: [MA-BCH-0083]
related: [MA-BOK-0010]
provenance:
  type: original
  sources:
    - "ANM-C05_EJERCICIOS.md, fuente canónica ANM; paquete C05 cerrado."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 5](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.md) · [Ejercicios](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-microcontroles.md)

## §5.1. Una sucesión es una función: índice y término

[]{#MA-EX-ANM-01-005-001}

[]{#MA-SEC-ANM-01-005-001}

[]{#MA-SOL-ANM-01-005-001}

### 1. Entrada, salida y repetición

Sea la sucesión real

$$
a:\mathbb N\to\mathbb R,
\qquad
a_n=(n-2)^2-1.
$$

a) Calcula $a_0$, $a_1$, $a_2$, $a_3$ y $a_5$.

b) Para cada una de las expresiones siguientes, indica qué tipo de objeto designa:

$$
a,
\qquad
5,
\qquad
a_5,
\qquad
a(5).
$$

No basta con dar su valor numérico: debes decir si se trata de la función completa, de un índice o de un término.

c) Observa que dos índices distintos producen el mismo valor. Encuentra esos dos índices entre $0,1,2,3$ y escribe las dos igualdades correspondientes.

d) Explica por qué esa repetición no contradice que $a$ sea una función.

[]{#MA-EX-ANM-01-005-002}

[]{#MA-SOL-ANM-01-005-002}

### 2. La misma regla no determina la misma función

Considera

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=2x+1,
$$

$$
a:\mathbb N\to\mathbb R,
\qquad
a_n=2n+1,
$$

y

$$
c:\mathbb Z\to\mathbb R,
\qquad
c(k)=2k+1.
$$

a) Calcula $f(3)$, $a_3$ y $c(3)$.

b) ¿Son iguales como funciones $f$, $a$ y $c$? Justifica tu respuesta usando el dominio como parte del objeto matemático.

c) Decide cuáles de las expresiones siguientes están definidas y, cuando lo estén, calcula su valor:

$$
a_{-1},
\qquad
c(-1),
\qquad
f\!\left(\frac12\right),
\qquad
a_{1/2}.
$$

d) Formula con precisión la relación que sí existe entre $f$ y $a$: ¿qué ocurre cuando ambos se evalúan en un mismo $n\in\mathbb N$?

[]{#MA-EX-ANM-01-005-003}

[]{#MA-SOL-ANM-01-005-003}

### 3. Tres registros para una misma sucesión

Sea $b:\mathbb N\to\mathbb R$ definida por

$$
b_n=
\begin{cases}
4, & \text{si }n\equiv0\pmod 3,\\
-1, & \text{si }n\equiv1\pmod 3,\\
0, & \text{si }n\equiv2\pmod 3.
\end{cases}
$$

a) Construye una tabla con dos columnas, $n$ y $b_n$, para $0\le n\le8$.

b) Escribe esos nueve términos como una lista ordenada

$$
(b_0,b_1,\ldots,b_8).
$$

c) Escribe explícitamente las nueve asignaciones

$$
n\longmapsto b_n
$$

para $0\le n\le8$.

d) Señala qué información permanece visible en las tres representaciones y explica por qué la aparición repetida de $4$, $-1$ y $0$ es compatible con la definición de función.

[]{#MA-EX-ANM-01-005-004}

[]{#MA-SOL-ANM-01-005-004}

### 4. Una fórmula, tres errores de tipo

Sea

$$
c:\mathbb N\to\mathbb R,
\qquad
c_n=2n-3.
$$

Un estudiante escribe:

> Como $c_3=3$, el índice $3$ y el término $c_3$ son el mismo objeto. Además, la función $g:\mathbb R\to\mathbb R$ dada por $g(x)=2x-3$ es igual a $c$, porque ambas usan la misma fórmula. Por tanto $c$ también tiene un término de índice $3.5$, y ese término vale $4$.

Analiza el argumento completo.

a) Localiza tres errores distintos.

b) Para cada error, identifica qué distinción de tipos o de dominios se ha perdido.

c) Reescribe el razonamiento de forma correcta, conservando todas las afirmaciones verdaderas que puedan rescatarse.

d) Indica qué habría que comprobar para poder afirmar que dos sucesiones $u,v:\mathbb N\to\mathbb R$ son iguales.

## §5.2. El orden de las visitas importa

[]{#MA-EX-ANM-01-005-005}

[]{#MA-SEC-ANM-01-005-002}

[]{#MA-SOL-ANM-01-005-005}

### 5. Los valores y los índices que los visitan

Sea la sucesión $a:\mathbb N\to\mathbb R$ definida por

$$
a_n=
\begin{cases}
0, & \text{si }n\equiv0\pmod 4,\\
2, & \text{si }n\equiv1\text{ o }2\pmod 4,\\
-1, & \text{si }n\equiv3\pmod 4.
\end{cases}
$$

Para cada $x\in\mathbb R$, define el conjunto de índices de aparición de $x$ por

$$
I_a(x)=\{n\in\mathbb N:a_n=x\}.
$$

a) Determina el conjunto de valores $a(\mathbb N)$.

b) Describe exactamente $I_a(0)$, $I_a(2)$ e $I_a(-1)$.

c) Indica el tipo matemático de cada objeto:

$$
a,
\qquad
a(\mathbb N),
\qquad
I_a(2),
\qquad
a_6.
$$

d) Explica qué información conservan los conjuntos $I_a(x)$ que desaparece si sólo conocemos $a(\mathbb N)$.

[]{#MA-EX-ANM-01-005-006}

[]{#MA-SOL-ANM-01-005-006}

### 6. Recuperar la sucesión a partir de sus índices de aparición

Sean $a,b:\mathbb N\to\mathbb R$. Para cada $x\in\mathbb R$, define

$$
I_a(x)=\{n\in\mathbb N:a_n=x\},
\qquad
I_b(x)=\{n\in\mathbb N:b_n=x\}.
$$

Demuestra la equivalencia

$$
\boxed{
a=b
\iff
\forall x\in\mathbb R,\ I_a(x)=I_b(x).
}
$$

Después demuestra que

$$
a(\mathbb N)
=
\{x\in\mathbb R:I_a(x)\ne\varnothing\}.
$$

Concluye explicando por qué conocer todos los conjuntos $I_a(x)$ contiene estrictamente más información que conocer sólo el conjunto de valores $a(\mathbb N)$.

[]{#MA-EX-ANM-01-005-007}

[]{#MA-SOL-ANM-01-005-007}

### 7. Dos existencias no alinean los índices

Un estudiante escribe:

> Si dos sucesiones $a,b:\mathbb N\to\mathbb R$ tienen el mismo conjunto de valores, entonces cada término $a_n$ aparece en algún lugar de $b$ y cada término $b_m$ aparece en algún lugar de $a$. Por tanto, para todo $n$ se tiene $a_n=b_n$, y las sucesiones son iguales.

Audita el argumento.

a) Traduce la igualdad de conjuntos de valores en dos afirmaciones cuantificadas que expresen «cada término aparece en algún lugar de la otra sucesión».

b) Escribe la afirmación cuantificada que sería necesaria para concluir $a=b$.

c) Localiza el paso ilegítimo: explica por qué un índice $m$ cuya existencia depende de $n$ no puede reemplazarse sin más por ese mismo $n$.

d) Usa

$$
a=(0,1,0,1,\ldots),
\qquad
b=(1,0,1,0,\ldots)
$$

para mostrar concretamente que las dos afirmaciones existenciales pueden ser verdaderas mientras $a\ne b$.

e) Reescribe la conclusión correcta del argumento del estudiante.

[]{#MA-EX-ANM-01-005-008}

[]{#MA-SOL-ANM-01-005-008}

### 8. Ningún prefijo finito fija el orden completo

Sea $M\in\mathbb N$ arbitrario.

Construye dos sucesiones $a,b:\mathbb N\to\mathbb R$ que satisfagan simultáneamente:

1. $a_n=b_n$ para todo $0\le n\le M$;
2. $a(\mathbb N)=b(\mathbb N)=\mathbb N$;
3. cada valor natural aparece exactamente una vez en cada sucesión;
4. $a\ne b$.

Tu construcción debe funcionar para **todo** $M$.

Después identifica un índice concreto que demuestre $a\ne b$ y explica qué refuta el ejemplo acerca de la posibilidad de reconstruir una sucesión conociendo su conjunto de valores y una cantidad finita, aunque arbitrariamente grande, de términos iniciales.

[]{#MA-EX-ANM-01-005-009}

[]{#MA-SOL-ANM-01-005-009}

### 9. El mismo conjunto de valores, muchos ritmos de repetición

Para cada entero $r\ge1$, define una sucesión $b^{(r)}:\mathbb N\to\mathbb R$ por bloques. Para $q\in\mathbb N$ y $j\in\{0,1,\ldots,r-1\}$, fija

$$
b^{(r)}_{3rq+j}=0,
$$

$$
b^{(r)}_{3rq+r+j}=1,
$$

y

$$
b^{(r)}_{3rq+2r+j}=2.
$$

Así, cada ciclo contiene $r$ ceros, luego $r$ unos y luego $r$ doses.

a) Escribe los primeros doce términos de $b^{(1)}$, $b^{(2)}$ y $b^{(3)}$.

b) Demuestra que, para todo $r\ge1$,

$$
b^{(r)}(\mathbb N)=\{0,1,2\}.
$$

c) Demuestra que si $1\le r<s$, entonces

$$
b^{(r)}_r=1
\qquad\text{y}\qquad
b^{(s)}_r=0.
$$

Concluye que las sucesiones $b^{(r)}$ son dos a dos distintas.

d) Describe el conjunto de índices en los que $b^{(r)}$ toma el valor $0$.

e) Explica qué aspecto de la sucesión cambia con $r$ y por qué ese cambio es completamente invisible en el conjunto de valores $\{0,1,2\}$.

## §5.3. Ver una sucesión sin perder el índice

[]{#MA-EX-ANM-01-005-010}

[]{#MA-SEC-ANM-01-005-003}

[]{#MA-SOL-ANM-01-005-010}

### 10. Del conjunto de puntos a tres registros coordinados

Los primeros ocho términos de una sucesión $a:\mathbb N\to\mathbb R$ están representados por el conjunto de puntos

$$
G_7=
\{(0,3),(1,1),(2,3),(3,-1),(4,1),(5,3),(6,-1),(7,1)\}.
$$

Este conjunto registra sólo los índices $0$ a $7$; no se afirma nada todavía sobre los términos posteriores.

a) Reconstruye una tabla con columnas $n$ y $a_n$ para $0\le n\le7$.

b) Escribe el mismo bloque como lista ordenada

$$
(a_0,a_1,\ldots,a_7).
$$

c) Representa esos ocho términos sobre la recta real usando únicamente las posiciones $-1$, $1$ y $3$, pero añade junto a cada posición **todos** los índices que llegan a ella.

d) Localiza la afirmación

$$
a_5=3
$$

en los tres registros: conjunto de puntos, tabla y recta real etiquetada.

e) Borra ahora las etiquetas de índice de la representación sobre la recta real. ¿Qué información queda y qué información deja de poder recuperarse acerca de los primeros ocho términos?

[]{#MA-EX-ANM-01-005-011}

[]{#MA-SOL-ANM-01-005-011}

### 11. Una codificación fiel que no es la gráfica estándar

Sea

$$
a_n=(-1)^n(n+1),
\qquad n\in\mathbb N.
$$

Considera dos conjuntos de puntos:

$$
G=\{(n,a_n):n\in\mathbb N\}
$$

y

$$
H=\{(2n+1,a_n):n\in\mathbb N\}.
$$

a) Escribe los primeros cinco puntos de $G$ y los primeros cinco puntos de $H$.

b) Explica por qué $G$ es la gráfica de la sucesión en el sentido estándar de §5.3.

c) El conjunto $H$ no usa el índice original como coordenada horizontal. Demuestra, sin embargo, que conserva toda la información de la sucesión si se declara la regla de decodificación

$$
n=\frac{x-1}{2}.
$$

En particular, muestra cómo recuperar $a_3$ a partir del punto correspondiente de $H$.

d) Explica por qué $H$ es una representación codificada fiel, pero no es literalmente la gráfica

$$
\{(n,a_n):n\in\mathbb N\}.
$$

e) Si de $G$ o de $H$ conservamos únicamente las alturas y borramos por completo la coordenada horizontal, ¿qué estructura de la sucesión se pierde?

[]{#MA-EX-ANM-01-005-012}

[]{#MA-SOL-ANM-01-005-012}

### 12. Dos curvas distintas, una sola sucesión

Considera las funciones reales

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=x,
$$

y

$$
g:\mathbb R\to\mathbb R,
\qquad
g(x)=x+\sin(\pi x).
$$

A partir de ellas se definen dos sucesiones

$$
a_n=f(n),
\qquad
b_n=g(n),
\qquad n\in\mathbb N.
$$

Un estudiante afirma:

> Las gráficas de $f$ y $g$ son distintas como curvas del plano. Por tanto, las sucesiones $a$ y $b$ también son distintas.

a) Demuestra que para todo $n\in\mathbb N$ se cumple

$$
a_n=b_n=n.
$$

b) Concluye, usando la igualdad de sucesiones índice por índice, que $a=b$.

c) Exhibe un número real $x\notin\mathbb N$ para el cual $f(x)\ne g(x)$ y verifica numéricamente la desigualdad.

d) Localiza con precisión el error del estudiante: ¿qué dos objetos está identificando indebidamente?

e) Escribe la gráfica discreta común de $a$ y $b$ y explica por qué los valores de $f$ y $g$ entre dos índices naturales consecutivos no pertenecen a ninguna de las dos sucesiones.

[]{#MA-EX-ANM-01-005-013}

[]{#MA-SOL-ANM-01-005-013}

### 13. Cuánto puede cambiar una representación sin perder la sucesión

Sea $a:\mathbb N\to\mathbb R$ la sucesión periódica

$$
a_n=
\begin{cases}
2, & n\equiv0\pmod 3,\\
0, & n\equiv1\pmod 3,\\
1, & n\equiv2\pmod 3.
\end{cases}
$$

Considera los siguientes registros de información:

1. la gráfica estándar
   $$
   G=\{(n,a_n):n\in\mathbb N\};
   $$
2. una tabla que contiene todos los pares $(n,a_n)$, pero cuyas filas han sido reordenadas arbitrariamente;
3. el conjunto codificado
   $$
   H=\{(n+10,a_n):n\in\mathbb N\},
   $$
   acompañado de la regla «el índice original es $x-10$»;
4. el conjunto de valores
   $$
   V=\{a_n:n\in\mathbb N\}.
   $$

a) Decide para cada registro si permite reconstruir exactamente la sucesión $a$. Justifica cada respuesta.

b) Para el registro 2, explica por qué el orden físico de las filas es irrelevante mientras cada fila conserve su etiqueta $n$.

c) Para el registro 3, da una fórmula explícita que permita recuperar $a_n$ a partir del punto cuya coordenada horizontal es $n+10$.

d) Calcula $V$ y construye una sucesión $b:\mathbb N\to\mathbb R$ distinta de $a$ que tenga exactamente ese mismo conjunto de valores.

e) Formula un criterio general, en una sola frase matemática, para decidir cuándo un cambio de representación conserva la sucesión y cuándo la ha colapsado a un objeto más pobre.

## §5.4. Colas: olvidar un comienzo finito

[]{#MA-EX-ANM-01-005-014}

[]{#MA-SEC-ANM-01-005-004}

[]{#MA-SOL-ANM-01-005-014}

### 14. Tres objetos después del mismo corte

Sea $a:\mathbb N\to\mathbb R$ la sucesión periódica

$$
a_n=
\begin{cases}
5, & n\equiv0\pmod 3,\\
-1, & n\equiv1\pmod 3,\\
2, & n\equiv2\pmod 3.
\end{cases}
$$

Fija $N=4$ y define

$$
R=a|_{\mathbb N_{\ge4}},
\qquad
T=a^{\langle4\rangle},
\qquad
V_4=\{a_n:n\ge4\}.
$$

a) Escribe el dominio y el codominio de $R$ y de $T$.

b) Escribe las primeras seis asignaciones de $R$ y los primeros seis términos de $T$.

c) Determina $V_4$.

d) Calcula $R(6)$ y $T_2$ y explica por qué ambos valores coinciden aunque $R$ y $T$ no sean la misma función.

e) Clasifica tipológicamente $R$, $T$ y $V_4$: ¿cuáles son funciones y cuál es sólo un subconjunto de $\mathbb R$?

[]{#MA-EX-ANM-01-005-015}

[]{#MA-SOL-ANM-01-005-015}

### 15. Reparar una igualdad mal tipada

Sea $a:\mathbb N\to\mathbb R$ y fija $N\in\mathbb N$. Un estudiante escribe

$$
a|_{\mathbb N_{\ge N}}
=
a^{\langle N\rangle}
=
\{a_n:n\ge N\}.
$$

Audita la cadena.

a) Escribe el tipo exacto de cada uno de los tres objetos.

b) Explica por qué las dos igualdades escritas no son igualdades de funciones o conjuntos bien tipadas.

c) Sea

$$
\tau_N:\mathbb N\to\mathbb N_{\ge N},
\qquad
\tau_N(k)=N+k.
$$

Demuestra la relación correcta

$$
\boxed{
a^{\langle N\rangle}
=
\left(a|_{\mathbb N_{\ge N}}\right)\circ\tau_N.
}
$$

d) Demuestra además que las imágenes de las dos funciones coinciden y son precisamente el conjunto de valores tardíos:

$$
\boxed{
\left(a|_{\mathbb N_{\ge N}}\right)(\mathbb N_{\ge N})
=
a^{\langle N\rangle}(\mathbb N)
=
\{a_n:n\ge N\}.
}
$$

[]{#MA-EX-ANM-01-005-016}

[]{#MA-SOL-ANM-01-005-016}

### 16. Una misma cola en cuatro registros

Sea $a:\mathbb N\to\mathbb R$ dada por

$$
a_n=
\begin{cases}
3, & n\equiv0\pmod 4,\\
-1, & n\equiv1\pmod 4,\\
2, & n\equiv2\pmod 4,\\
-1, & n\equiv3\pmod 4.
\end{cases}
$$

Fija $N=5$.

a) Construye una tabla con los pares $(n,a_n)$ para $5\le n\le10$.

b) Escribe ese mismo bloque como parte inicial de la cola restringida $a|_{\mathbb N_{\ge5}}$, conservando los índices originales.

c) Reescríbelo como los primeros seis términos de la cola reindexada $a^{\langle5\rangle}$, usando índices $k=0,\ldots,5$.

d) Escribe los seis puntos correspondientes de la gráfica discreta de la cola reindexada,

$$
(k,a^{\langle5\rangle}_k).
$$

e) Determina el conjunto completo de valores tardíos $\{a_n:n\ge5\}$ y explica qué información presente en los tres registros anteriores desaparece al pasar a este conjunto.

[]{#MA-EX-ANM-01-005-017}

[]{#MA-SOL-ANM-01-005-017}

### 17. Reconstruir el corte desde las nuevas posiciones

Sea $a:\mathbb N\to\mathbb R$ una sucesión y supón que queremos reindexar una de sus colas. No estamos comparando valores numéricos por coincidencia accidental: cuando escribimos

$$
r\longleftrightarrow p,
$$

queremos decir que el término original $a_p$ debe ocupar exactamente el nuevo índice $r$ de la cola reindexada.

a) Decide si existe un corte $N$ que satisfaga simultáneamente

$$
3\longleftrightarrow14,
\qquad
9\longleftrightarrow20.
$$

Si existe, encuéntralo y verifica ambas correspondencias.

b) Manteniendo esas dos exigencias, ¿puede añadirse también

$$
4\longleftrightarrow16?
$$

Justifica.

c) Sean en general $r,s,p,q\in\mathbb N$. Demuestra que existe un mismo corte $N$ para el cual

$$
r\longleftrightarrow p,
\qquad
s\longleftrightarrow q
$$

en la cola $a^{\langle N\rangle}$ si y sólo si

$$
\boxed{p-r=q-s\ge0.}
$$

Cuando existe, identifica el único valor posible de $N$.

[]{#MA-EX-ANM-01-005-018}

[]{#MA-SOL-ANM-01-005-018}

### 18. Componer reindexaciones

Sea $a:\mathbb N\to\mathbb R$ y sean $N,K\in\mathbb N$.

a) Demuestra, como igualdad de funciones $\mathbb N\to\mathbb R$, que

$$
\boxed{
\left(a^{\langle N\rangle}\right)^{\langle K\rangle}
=
a^{\langle N+K\rangle}.
}
$$

Tu prueba debe comenzar con un índice arbitrario $j\in\mathbb N$ y seguir explícitamente qué índice original de $a$ representa cada término.

b) Explica la cadena de índices

$$
j
\longmapsto
K+j
\longmapsto
N+K+j.
$$

c) Deduce como caso particular que, si $M\ge N$, entonces

$$
\boxed{
a^{\langle M\rangle}
=
\left(a^{\langle N\rangle}\right)^{\langle M-N\rangle}.
}
$$

d) Explica por qué esta identidad habla de reindexar dos veces y no de eliminar dos bloques independientes de términos.

[]{#MA-EX-ANM-01-005-019}

[]{#MA-SOL-ANM-01-005-019}

### 19. Cuándo deja de encogerse el conjunto de valores tardíos

Para una sucesión $a:\mathbb N\to\mathbb R$ define

$$
V_N(a)=\{a_n:n\ge N\}.
$$

Sean $M,N\in\mathbb N$ con $M\ge N$.

a) Demuestra que

$$
V_M(a)\subseteq V_N(a).
$$

b) Demuestra la equivalencia

$$
\boxed{
V_N(a)=V_M(a)
\iff
\forall n\in\{N,N+1,\ldots,M-1\}\;\exists m\ge M:\ a_n=a_m.
}
$$

Interpreta verbalmente la condición de la derecha.

c) Explica qué ocurre en el caso $M=N$.

d) Da un ejemplo en el que la inclusión de a) sea estricta y otro en el que haya igualdad aunque $M>N$.

e) Explica por qué la igualdad de conjuntos $V_N(a)=V_M(a)$ no implica que las colas restringidas desde $N$ y desde $M$ sean la misma función.

## §5.5. «A partir de cierto momento»: propiedades eventuales

[]{#MA-EX-ANM-01-005-020}

[]{#MA-SEC-ANM-01-005-005}

[]{#MA-SOL-ANM-01-005-020}

### 20. Todos los testigos de una desigualdad eventual

Sea

$$
a_n=4n-13,
\qquad n\in\mathbb N,
$$

y considera la propiedad

$$
P(n):\quad a_n\ge7.
$$

a) Encuentra un testigo $N$ de que $P(n)$ ocurre eventualmente y verifica tu elección para un índice arbitrario $n\ge N$.

b) Determina **todos** los valores de $N\in\mathbb N$ que sirven como testigos de eventualidad.

c) Explica por qué no es necesario elegir el menor testigo para demostrar que $P$ es eventual, aunque en este ejemplo pueda identificarse.

[]{#MA-EX-ANM-01-005-021}

[]{#MA-SOL-ANM-01-005-021}

### 21. Un intervalo fijo y el conjunto exacto de testigos

Sea

$$
b_n=\frac{2n+1}{n+2},
\qquad n\in\mathbb N,
$$

y fija, **antes de elegir cualquier umbral**, el intervalo

$$
I=\left(\frac32,2\right).
$$

a) Demuestra que $b_n<2$ para todo $n\in\mathbb N$.

b) Encuentra un testigo $N$ de que $b_n\in I$ eventualmente.

c) Caracteriza exactamente el conjunto de todos los testigos para esta propiedad.

d) Identifica en tu prueba qué dato estaba fijado antes de elegir $N$ y qué variable quedó arbitraria después de fijar el umbral.

[]{#MA-EX-ANM-01-005-022}

[]{#MA-SOL-ANM-01-005-022}

### 22. El conjunto de testigos y la cola reindexada

Sea $P(n)$ una propiedad definida para cada $n\in\mathbb N$ y define

$$
W_P
=
\{N\in\mathbb N:\forall n\ge N,\ P(n)\}.
$$

Demuestra las tres afirmaciones siguientes.

a) $P(n)$ ocurre eventualmente si y sólo si $W_P\ne\varnothing$.

b) Si $N\in W_P$ y $M\ge N$, entonces $M\in W_P$.

c) Para cada $N\in\mathbb N$,

$$
\boxed{
N\in W_P
\iff
\forall k\in\mathbb N:\ P(N+k).
}
$$

Concluye explicando por qué el conjunto de testigos, cuando no es vacío, está cerrado hacia índices posteriores y cómo la parte c) traduce la eventualidad al lenguaje de una cola reindexada.

[]{#MA-EX-ANM-01-005-023}

[]{#MA-SOL-ANM-01-005-023}

### 23. Un millón de verificaciones no produce un cuantificador universal

Un estudiante quiere demostrar que una propiedad $P(n)$ ocurre eventualmente y escribe:

> He comprobado $P(n)$ para todos los índices desde $1000$ hasta $10^6$. Por tanto puedo tomar $N=1000$ y concluir que $P(n)$ es verdadera para todo $n\ge1000$.

a) Escribe la afirmación cuantificada que el estudiante necesita demostrar para que $N=1000$ sea un testigo.

b) Localiza el salto lógico entre lo que verificó y lo que concluyó.

c) Construye una propiedad explícita $P(n)$ que sea verdadera para **todos** los índices $1000\le n\le10^6$ y, sin embargo, no sea eventual.

d) Demuestra desde la definición que tu propiedad no es eventual.

e) Indica qué tipo de argumento adicional, más allá de una lista finita de comprobaciones, repararía la prueba original.

[]{#MA-EX-ANM-01-005-024}

[]{#MA-SOL-ANM-01-005-024}

### 24. Mover una única excepción mueve el umbral

Para cada $r\in\mathbb N$, fija primero el parámetro $r$ y define la sucesión

$$
d^{(r)}_n=
\begin{cases}
0, & n=r,\\
1, & n\ne r.
\end{cases}
$$

Considera la propiedad

$$
P_r(n):\quad d^{(r)}_n=1.
$$

a) Demuestra que, para cada $r$ fijo, $P_r(n)$ ocurre eventualmente.

b) Determina exactamente todos los testigos $N$ para $P_r$.

c) Explica por qué ningún $N\le r$ puede ser testigo.

d) ¿Es $P_r(n)$ verdadera para todo $n\in\mathbb N$? Justifica.

e) Compara los casos $r$ y $r+10$: ¿qué cambia en el conjunto de testigos y qué estructura lógica de la definición permanece idéntica?

[]{#MA-EX-ANM-01-005-025}

[]{#MA-SOL-ANM-01-005-025}

### 25. Tres lenguajes para la misma eventualidad

Sea $a:\mathbb N\to\mathbb R$ y sea $I\subseteq\mathbb R$ un intervalo **fijo**. Demuestra que son equivalentes las afirmaciones siguientes:

1. $a_n\in I$ eventualmente;
2. existe $N\in\mathbb N$ tal que
   $$
   a(\mathbb N_{\ge N})\subseteq I;
   $$
3. existe $N\in\mathbb N$ tal que
   $$
   \forall k\in\mathbb N:\ a^{\langle N\rangle}_k\in I.
   $$

Después responde:

a) Si $a_n\in I$ para todo $n\in\mathbb N$, ¿qué testigo puede elegirse inmediatamente?

b) Da un ejemplo explícito en el que $a_n\in I$ sea eventual pero no global.

c) Explica por qué el intervalo $I$ debe considerarse fijado antes de buscar el testigo $N$.

d) Resume en una sola cadena conceptual cómo intervienen en esta equivalencia el segmento final, la cola reindexada y el patrón $\exists N\,\forall n\ge N$.

## §5.6. Eventualmente no significa infinitas veces

[]{#MA-EX-ANM-01-005-026}

[]{#MA-SEC-ANM-01-005-006}

[]{#MA-SOL-ANM-01-005-026}

### 26. El conjunto de ocurrencias visto desde cada cola

Sea $P(n)$ una propiedad definida para cada $n\in\mathbb N$ y define su conjunto de ocurrencias por

$$
A_P=\{n\in\mathbb N:P(n)\}.
$$

Para $N\in\mathbb N$, recuerda que

$$
\mathbb N_{\ge N}=\{n\in\mathbb N:n\ge N\}.
$$

Demuestra las equivalencias

$$
\boxed{
P\text{ ocurre infinitas veces}
\iff
\forall N\in\mathbb N:\ A_P\cap\mathbb N_{\ge N}\ne\varnothing,
}
$$

y

$$
\boxed{
P\text{ ocurre eventualmente}
\iff
\exists N\in\mathbb N:\ \mathbb N_{\ge N}\subseteq A_P.
}
$$

Después:

a) usa únicamente estas dos caracterizaciones para demostrar que toda propiedad eventual ocurre infinitas veces;

b) explica, en lenguaje de conjuntos, la diferencia entre «una cola completa queda dentro de $A_P$» y «cada cola corta a $A_P$ en al menos un punto»;

c) indica cuál de las dos caracterizaciones permite que haya fallos de $P$ arbitrariamente tardíos.

[]{#MA-EX-ANM-01-005-027}

[]{#MA-SOL-ANM-01-005-027}

### 27. Apariciones arbitrariamente tardías no llenan una cola

Define la propiedad

$$
P(n):\quad n=2^k\text{ para algún }k\in\mathbb N.
$$

Un estudiante razona:

> Para cualquier umbral $N$ puedo encontrar una potencia de $2$ situada después de $N$. Por tanto, llega un momento a partir del cual todos los índices son potencias de $2$, así que $P$ es eventual.

Audita el argumento.

a) Escribe la afirmación cuantificada que expresa correctamente que $P$ ocurre infinitas veces.

b) Demuestra esa afirmación construyendo, para un $N$ arbitrario, un índice testigo $n\ge N$ que sea potencia de $2$.

c) Localiza con precisión el cambio ilegítimo de orden o alcance de cuantificadores en el razonamiento del estudiante.

d) Demuestra que $P$ **no** es eventual: dado un umbral arbitrario $N$, construye un índice $m\ge N$ que no sea potencia de $2$.

e) Reescribe la conclusión correcta sin cambiar ninguna premisa verdadera del argumento original.

[]{#MA-EX-ANM-01-005-028}

[]{#MA-SOL-ANM-01-005-028}

### 28. Bloques cada vez más largos sin estabilización

Define una propiedad $P(n)$ de los naturales de la siguiente manera. Para cada entero $k\ge1$, declara verdadera a $P$ en el bloque

$$
k^2\le n<k^2+k
$$

y falsa en el bloque siguiente

$$
k^2+k\le n<(k+1)^2.
$$

Además, fija $P(0)$ como falsa.

a) Escribe el patrón de verdad de $P(n)$ para $0\le n\le20$, agrupando los índices en bloques consecutivos de verdad y falsedad.

b) Demuestra directamente desde la definición que $P$ ocurre infinitas veces.

c) Demuestra directamente que $\neg P$ ocurre infinitas veces.

d) Concluye que ni $P$ ni $\neg P$ son eventuales.

e) Demuestra algo más fuerte: para cada $L\ge1$ existe un bloque de al menos $L$ índices consecutivos en los que $P$ es verdadera y también un bloque de al menos $L$ índices consecutivos en los que $P$ es falsa.

f) Explica qué falsa inferencia destruye este ejemplo acerca de observar bloques finitos cada vez más largos.

[]{#MA-EX-ANM-01-005-029}

[]{#MA-SOL-ANM-01-005-029}

### 29. Tricotomía del comportamiento tardío de una propiedad

Sea $P(n)$ una propiedad cualquiera sobre $\mathbb N$. Demuestra que **exactamente una** de las tres situaciones siguientes ocurre:

1. $P$ ocurre eventualmente;
2. $\neg P$ ocurre eventualmente;
3. tanto $P$ como $\neg P$ ocurren infinitas veces.

Tu demostración debe cumplir estas condiciones:

a) prueba primero que las tres situaciones son mutuamente excluyentes usando sólo los resultados de §5.6;

b) prueba después que siempre ocurre al menos una de ellas, separando los casos según si $P$ es eventual o no y, cuando corresponda, según si $\neg P$ es eventual o no;

c) deduce como corolario que, para cualquier propiedad $P$, al menos una de $P$ o $\neg P$ ocurre infinitas veces;

d) explica por qué esta tricotomía es más precisa que dividir simplemente entre «eventual» y «no eventual».

No utilices el lema de sincronización de §5.7.

[]{#MA-EX-ANM-01-005-030}

[]{#MA-SOL-ANM-01-005-030}

### 30. Cuando el testigo depende de otro parámetro

Para cada entero $r\ge1$, define la propiedad

$$
P_r(n):\quad r\mid n.
$$

Analiza con cuidado el orden de los cuantificadores.

a) Demuestra que, para cada $r\ge1$ fijo, $P_r(n)$ ocurre infinitas veces. Tu prueba debe construir explícitamente un índice $n=n(r,N)\ge N$ para un umbral arbitrario $N$.

b) Concluye que es verdadera la afirmación

$$
\forall r\ge1\;\forall N\in\mathbb N\;\exists n\ge N:\ r\mid n.
$$

c) Demuestra, en cambio, que es falsa la afirmación

$$
\forall N\in\mathbb N\;\exists n\ge N\;\forall r\ge1:\ r\mid n.
$$

Basta analizar cuidadosamente el caso $N=1$.

d) Explica por qué los testigos obtenidos en a), que pueden depender de $r$ y de $N$, no autorizan a producir un único $n$ que funcione simultáneamente para todos los enteros positivos $r$.

e) Fija ahora un entero $m\ge1$ y reemplaza la familia infinita $r\ge1$ por la familia finita $1\le r\le m$. Demuestra que

$$
\forall N\in\mathbb N\;\exists n\ge N\;\forall r\in\{1,\ldots,m\}:\ r\mid n.
$$

Construye un testigo explícito y explica qué cambió al pasar de una familia infinita a una familia finita de divisores.

## §5.7. Sincronizar colas y olvidar perturbaciones finitas

[]{#MA-EX-ANM-01-005-031}

[]{#MA-SEC-ANM-01-005-007}

[]{#MA-SOL-ANM-01-005-031}

### 31. Un solo corte para tres obligaciones

Sean $P(n)$, $Q(n)$ y $R(n)$ tres propiedades sobre $\mathbb N$. Se sabe que

$$
\forall n\ge4:\ P(n),
$$

$$
\forall n\ge9:\ Q(n),
$$

y

$$
\forall n\ge6:\ R(n).
$$

No se afirma que $4$, $9$ y $6$ sean los menores testigos posibles.

a) Construye un único umbral $N$ que garantice simultáneamente $P(n)$, $Q(n)$ y $R(n)$ para todo $n\ge N$.

b) Verifica tu elección tomando un índice arbitrario $n\ge N$ y siguiendo explícitamente las tres comparaciones de índices.

c) Determina todos los valores $M$ que, **sólo a partir de la información dada**, están garantizados como testigos comunes.

d) Explica por qué los datos no permiten concluir que tu umbral sea el menor testigo posible de $P\land Q\land R$.

e) Identifica qué función lógica cumple el máximo de los tres umbrales: ¿mejora alguna estimación o sincroniza tres colas?

[]{#MA-EX-ANM-01-005-032}

[]{#MA-SOL-ANM-01-005-032}

### 32. Intersecar conjuntos de testigos

Sea $P(n)$ una propiedad sobre $\mathbb N$ y define

$$
W_P=\{N\in\mathbb N:\forall n\ge N,\ P(n)\}.
$$

Sean ahora $P_1,\ldots,P_k$ propiedades, con $k\ge1$ finito.

a) Demuestra que

$$
\boxed{
W_{P_1\land\cdots\land P_k}
=
W_{P_1}\cap\cdots\cap W_{P_k}.
}
$$

b) Supón que cada $P_i$ es eventual. Elige un testigo $N_i\in W_{P_i}$ para cada $i$ y demuestra que

$$
N=\max\{N_1,\ldots,N_k\}
$$

pertenece a la intersección de a).

c) Concluye que una conjunción finita de propiedades eventuales es eventual.

d) Explica con precisión dónde se usa la finitud de la familia en esta demostración. No concluyas nada sobre familias infinitas.

[]{#MA-EX-ANM-01-005-033}

[]{#MA-SOL-ANM-01-005-033}

### 33. Encadenar coincidencias eventuales

Sean

$$
a,b,c:\mathbb N\to\mathbb R.
$$

Supón que $a$ y $b$ coinciden desde $N_{ab}$, mientras que $b$ y $c$ coinciden desde $N_{bc}$:

$$
\forall n\ge N_{ab}:\ a_n=b_n,
$$

y

$$
\forall n\ge N_{bc}:\ b_n=c_n.
$$

a) Define

$$
M=\max\{N_{ab},N_{bc}\}
$$

y demuestra que $a$ y $c$ coinciden desde $M$.

b) Demuestra algo más fuerte: desde ese mismo $M$, las tres sucesiones coinciden término a término,

$$
\forall n\ge M:\ a_n=b_n=c_n.
$$

c) Traduce b) al lenguaje de colas reindexadas y demuestra

$$
\boxed{
a^{\langle M\rangle}
=
b^{\langle M\rangle}
=
c^{\langle M\rangle}.
}
$$

d) Explica por qué a), b) y c) no autorizan a concluir $a=b=c$ como funciones sobre todo $\mathbb N$.

[]{#MA-EX-ANM-01-005-034}

[]{#MA-SOL-ANM-01-005-034}

### 34. «Cambiar finitos términos no cambia nada»

Considera

$$
a=(0,1,1,1,1,\ldots)
$$

y

$$
b=(9,1,1,1,1,\ldots).
$$

Un estudiante escribe:

> Las dos sucesiones sólo difieren en un término. Por tanto son la misma sucesión a partir de una modificación irrelevante, y cualquier propiedad verdadera de $a$ también es verdadera de $b$.

Audita la afirmación.

a) Decide si $a=b$ como funciones y justifica tu respuesta.

b) Determina un umbral desde el cual $a$ y $b$ coinciden eventualmente.

c) Da una propiedad del prefijo que sea verdadera para $a$ y falsa para $b$.

d) Da una propiedad término a término que ocurra eventualmente para ambas y exhibe un umbral común.

e) Reescribe la afirmación del estudiante en una forma correcta que delimite exactamente qué clase de propiedades se conservan bajo una modificación finita.

f) Explica por qué la frase «los primeros términos son irrelevantes» es matemáticamente demasiado fuerte si no se especifica **para qué tipo de afirmación** son irrelevantes.

[]{#MA-EX-ANM-01-005-035}

[]{#MA-SOL-ANM-01-005-035}

### 35. Mismos valores tardíos en cada corte, pero sin cola común

Construye dos sucesiones $a,b:\mathbb N\to\mathbb R$ que satisfagan simultáneamente:

$$
\forall N\in\mathbb N:
\{a_n:n\ge N\}
=
\{b_n:n\ge N\},
$$

pero que **no** coincidan eventualmente.

Tu contraejemplo debe cumplir además:

a) los conjuntos de valores tardíos anteriores deben tener exactamente dos elementos para todo $N$;

b) debes demostrar la igualdad de esos conjuntos para un $N$ arbitrario, no sólo para algunos cortes;

c) debes demostrar que para todo $M\in\mathbb N$ existe $n\ge M$ con $a_n\ne b_n$;

d) concluye explicando por qué la igualdad de todos los conjuntos de valores tardíos no recupera la información indexada necesaria para una cola común.

[]{#MA-EX-ANM-01-005-036}

[]{#MA-SOL-ANM-01-005-036}

### 36. Sincronizar primero o transferir primero

Sean $a,b:\mathbb N\to\mathbb R$ dos sucesiones que coinciden desde un umbral $N_E$:

$$
\forall n\ge N_E:\ a_n=b_n.
$$

Sean además $P(x)$ y $Q(x)$ dos predicados fijos sobre números reales. Supón que

$$
\forall n\ge N_P:\ P(a_n)
$$

y

$$
\forall n\ge N_Q:\ Q(a_n).
$$

Demuestra que $P(b_n)\land Q(b_n)$ ocurre eventualmente siguiendo **dos rutas distintas**.

**Ruta A.** Sincroniza primero $P(a_n)$ y $Q(a_n)$ sobre la sucesión $a$ y después transfiere la conjunción a $b$ usando la coincidencia eventual.

**Ruta B.** Transfiere primero $P$ y $Q$ por separado desde $a$ hacia $b$ y después sincroniza las dos propiedades ya transferidas.

En ambos casos:

a) escribe todos los umbrales intermedios;

b) demuestra que puede elegirse finalmente

$$
\boxed{M=\max\{N_E,N_P,N_Q\};}
$$

c) explica por qué las dos rutas producen el mismo corte efectivo aunque agrupen los máximos de manera distinta;

d) generaliza el argumento a una familia finita $P_1,\ldots,P_k$ de predicados eventuales sobre $a$, con testigos $N_1,\ldots,N_k$;

e) indica por qué el mismo argumento no transfiere una propiedad como «$a_0=0$».

## §5.8. Captura eventual: la puerta a $\varepsilon$–$N$

[]{#MA-EX-ANM-01-005-037}

[]{#MA-SEC-ANM-01-005-008}

[]{#MA-SOL-ANM-01-005-037}

### 37. El último escape determina todos los testigos

Sea $U\subsetneq\mathbb R$ un conjunto no vacío. Fija dos números

$$
u\in U,
\qquad
v\notin U,
$$

y sea $F\subseteq\mathbb N$ un conjunto finito no vacío. Define una sucesión $a:\mathbb N\to\mathbb R$ por

$$
a_n=
\begin{cases}
v, & n\in F,\\
u, & n\notin F.
\end{cases}
$$

Sea

$$
m=\max F.
$$

a) Demuestra que $a$ está eventualmente en $U$.

b) Determina **exactamente** el conjunto de todos los testigos de captura

$$
W_U(a)=\{N\in\mathbb N:\forall n\ge N,\ a_n\in U\}.
$$

c) Reescribe el resultado de b) mediante la inclusión de valores tardíos

$$
\{a_n:n\ge N\}\subseteq U.
$$

d) Explica por qué el número decisivo es el último índice modificado, $m$, y no la cantidad de elementos de $F$.

e) ¿Qué cambia si $F=\varnothing$? Formula el conjunto de testigos en ese caso.

[]{#MA-EX-ANM-01-005-038}

[]{#MA-SOL-ANM-01-005-038}

### 38. Cálculo con conjuntos de testigos de captura

Sea $a:\mathbb N\to\mathbb R$. Para cada conjunto fijo $U\subseteq\mathbb R$, define

$$
W_U(a)=\{N\in\mathbb N:\forall n\ge N,\ a_n\in U\}.
$$

Demuestra las afirmaciones siguientes.

a) Si $U\subseteq V$, entonces

$$
W_U(a)\subseteq W_V(a).
$$

b) Para cualesquiera conjuntos fijos $U,V\subseteq\mathbb R$,

$$
\boxed{
W_{U\cap V}(a)=W_U(a)\cap W_V(a).
}
$$

c) Generaliza b) a una familia finita $U_1,\ldots,U_k$:

$$
\boxed{
W_{\bigcap_{j=1}^k U_j}(a)
=
\bigcap_{j=1}^k W_{U_j}(a).
}
$$

d) Supón que cada $W_{U_j}(a)$ es no vacío y elige $N_j\in W_{U_j}(a)$. Demuestra directamente que

$$
N=\max\{N_1,\ldots,N_k\}
$$

es un testigo de captura en $\bigcap_{j=1}^k U_j$.

e) Deduce que, si $U\cap V=\varnothing$, ninguna sucesión puede estar eventualmente en ambos conjuntos a la vez.

Tu prueba debe distinguir en todo momento entre los conjuntos geométricos $U,V\subseteq\mathbb R$ y los conjuntos de índices $W_U(a),W_V(a)\subseteq\mathbb N$.

[]{#MA-EX-ANM-01-005-039}

[]{#MA-SOL-ANM-01-005-039}

### 39. Una cola común atrapada por dos regiones

Sean

$$
a,b:\mathbb N\to\mathbb R
$$

dos sucesiones que coinciden eventualmente. Supón que existen umbrales $N_E,N_U,N_V\in\mathbb N$ tales que

$$
\forall n\ge N_E:\ a_n=b_n,
$$

$$
\forall n\ge N_U:\ a_n\in U,
$$

y

$$
\forall n\ge N_V:\ b_n\in V,
$$

donde $U,V\subseteq\mathbb R$ son conjuntos fijos.

a) Define un único umbral $M$ que permita usar simultáneamente las tres hipótesis.

b) Demuestra que para todo $n\ge M$ el valor común $a_n=b_n$ pertenece a $U\cap V$.

c) Concluye que **ambas** sucesiones están eventualmente en $U\cap V$.

d) Deduce que, si $U\cap V=\varnothing$, las tres hipótesis anteriores no pueden cumplirse simultáneamente.

e) Explica por qué la conclusión de d) depende esencialmente de la coincidencia eventual. Construye dos sucesiones que estén respectivamente siempre en dos conjuntos disjuntos $U$ y $V$, pero que no coincidan eventualmente.

[]{#MA-EX-ANM-01-005-040}

[]{#MA-SOL-ANM-01-005-040}

### 40. Una batería finita de bolas sigue siendo una exigencia fija

Fija un entero $k\ge1$ y radios positivos

$$
r_1,\ldots,r_k>0.
$$

Sea

$$
r_*=\min\{r_1,\ldots,r_k\}.
$$

Trabajamos con bolas centradas en $0$,

$$
B(0,r)=\{x\in\mathbb R:|x|<r\}.
$$

a) Demuestra que

$$
\bigcap_{j=1}^k B(0,r_j)=B(0,r_*).
$$

b) Considera la sucesión constante

$$
c_n=\frac{r_*}{2}.
$$

Demuestra que $c$ está en **cada una** de las bolas $B(0,r_j)$ para todo índice $n$.

c) Demuestra, sin embargo, que ningún término de $c$ pertenece a la bola más pequeña

$$
B\!\left(0,\frac{r_*}{4}\right).
$$

d) Concluye que verificar captura eventual en cualquier lista **finita** prefijada de bolas no equivale a disponer de una respuesta para exigencias de tamaño cada vez menor.

e) Explica, sólo con palabras y sin escribir todavía la definición formal de convergencia, qué cambia en C06 en el orden conceptual

$$
\text{tolerancia}
\longrightarrow
\text{umbral}
\longrightarrow
\text{todos los índices posteriores}.
$$

f) Explica por qué este ejercicio no autoriza todavía ninguna notación de límite: todo lo demostrado en a)–d) pertenece al lenguaje de capturas por una **familia finita de conjuntos ya fijados**.

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 5](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.md) · [Ejercicios](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-microcontroles.md)
