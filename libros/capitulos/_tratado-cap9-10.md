## 9.10. Compatibilidad del orden con las operaciones {#sec-ta-9-10}

Ya disponemos por separado de las dos estructuras que deben convivir en un cuerpo ordenado:

$$
(\mathbb R_C,+_C,\cdot_C,0_C,1_C)
$$

es un cuerpo (Teorema 9.7.10 — $\mathbb R_C$ es un cuerpo), y

$$
(\mathbb R_C,\le_C)
$$

es un conjunto totalmente ordenado (Teorema 9.8.5 — $\le_C$ es un orden total). Falta verificar exactamente las dos compatibilidades exigidas por la definición abstracta de cuerpo ordenado Definición 4.1.1 — Cuerpo ordenado:

$$
x\le_C y
\Longrightarrow
x+z\le_C y+z,
$$

$$
0_C\le_C x,
\quad
0_C\le_C y
\Longrightarrow
0_C\le_C xy.
$$

La primera se transmitirá directamente desde la comparación asintótica de representantes. Para la segunda conviene aprovechar el criterio estricto ya obtenido: dos clases estrictamente positivas admiten representantes que, a partir de cierto índice, están separados de cero por márgenes racionales positivos; el producto de esos márgenes vuelve a ser positivo.

### Proposición 9.10.1 — Invariancia del orden de Cauchy por traslación

Para cualesquiera $x,y,z\in\mathbb R_C$,

$$
\boxed{
x\le_C y
\Longrightarrow
x+z\le_C y+z.
}
$$

**Demostración.**

Supongamos

$$
x\le_C y.
$$

Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, tomemos representantes locales

$$
x=[a]_C,
\qquad
y=[b]_C,
\qquad
z=[c]_C,
$$

con $a,b,c\in\mathcal C_{\mathbb Q}$.

El criterio de representantes de Definición 9.8.4 — Orden de Cauchy da

$$
a\preccurlyeq_C b.
$$

Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Por Definición 9.8.1 — Comparación asintótica de representantes, existe $N\in\mathbb N$ tal que, para todo $n\ge N$,

$$
a_n<b_n+\varepsilon.
$$

Como $\mathbb Q$ es un cuerpo ordenado (Proposición 4.1.4 — $\mathbb Q$ es un cuerpo ordenado), la invariancia estricta por traslación de Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado permite sumar $c_n$ a ambos miembros:

$$
a_n+c_n
<
(b_n+\varepsilon)+c_n.
$$

Por asociatividad y conmutatividad de la suma racional,

$$
(b_n+\varepsilon)+c_n
=
(b_n+c_n)+\varepsilon.
$$

Luego, para todo $n\ge N$,

$$
(a+c)_n<(b+c)_n+\varepsilon.
$$

Como $\varepsilon>0$ era arbitraria,

$$
a+c\preccurlyeq_C b+c.
$$

Las sucesiones $a+c$ y $b+c$ pertenecen a $\mathcal C_{\mathbb Q}$ por Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto, y la definición de la suma en el cociente (Definición 9.5.4 — Suma y producto en $\mathbb R_C$) da

$$
x+z=[a+c]_C,
\qquad
y+z=[b+c]_C.
$$

Aplicando nuevamente Definición 9.8.4 — Orden de Cauchy, concluimos

$$
x+z\le_C y+z.
$$

∎

### Proposición 9.10.2 — El producto de elementos no negativos es no negativo

Para cualesquiera $x,y\in\mathbb R_C$,

$$
\boxed{
0_C\le_C x,
\quad
0_C\le_C y
\Longrightarrow
0_C\le_C xy.
}
$$

**Demostración.**

Supongamos

$$
0_C\le_C x,
\qquad
0_C\le_C y.
$$

Tomemos representantes locales

$$
x=[a]_C,
\qquad
y=[b]_C,
$$

con $a,b\in\mathcal C_{\mathbb Q}$. Como
$0_C=[\underline{0_{\mathbb Q}}]_C$, la definición del orden da

$$
\underline{0_{\mathbb Q}}\preccurlyeq_C a,
\qquad
\underline{0_{\mathbb Q}}\preccurlyeq_C b.
$$

Por Teorema 8.6.3 — Toda sucesión racional de Cauchy es acotada, las dos sucesiones son acotadas. Existen racionales no negativos
$B_a,B_b$ tales que

$$
|a_n|\leq B_a,
\qquad
|b_n|\leq B_b
$$

para todo $n$. Pongamos

$$
B:=B_a+B_b+1_{\mathbb Q}.
$$

Entonces $0<B$ y, para todo $n$,

$$
|a_n|<B,
\qquad
|b_n|<B.
$$

Sea ahora $\varepsilon>0$. Definimos

$$
\eta:=\frac{\varepsilon}{B+1_{\mathbb Q}}>0.
$$

De $\underline0\preccurlyeq_C a$ y $\underline0\preccurlyeq_C b$ existen índices
$N_a,N_b$ tales que

$$
n\geq N_a\Longrightarrow -\eta<a_n,
\qquad
n\geq N_b\Longrightarrow -\eta<b_n.
$$

Por la comparación decidible de naturales tomamos un índice $N$ que domina a ambos. Fijemos
$n\geq N$. La tricotomía decidible racional permite separar los signos de $a_n,b_n$.

Si ambos son no negativos, $0\leq a_nb_n$. Si ambos son negativos, también
$0<a_nb_n$. En los casos de signos opuestos, por ejemplo $a_n<0\leq b_n$,

$$
-\eta<a_n<0,
\qquad
0\leq b_n<B,
$$

y por compatibilidad del orden con el producto,

$$
a_nb_n\geq-\eta b_n>-\eta B.
$$

El otro caso mixto es simétrico. Como

$$
\eta B
=
\varepsilon\frac{B}{B+1_{\mathbb Q}}
<
\varepsilon,
$$

en todos los casos obtenemos

$$
-\varepsilon<a_nb_n,
$$

equivalentemente,

$$
0_{\mathbb Q}<a_nb_n+\varepsilon.
$$

Esto vale para todo $n\geq N$, de modo que

$$
\underline{0_{\mathbb Q}}\preccurlyeq_C ab.
$$

Por la definición del producto en el cociente,

$$
xy=[ab]_C,
$$

y por tanto

$$
0_C\le_Cxy.
$$

∎

> apartness de los factores. Sólo usa el preorder asintótico, acotación racional y decisiones de signo
> para términos racionales individuales. Por ello no hereda la clasicidad de Lema 9.7.2 — Separación eventual respecto de cero ni de la
> totalidad de $\mathbb R_C$. Tampoco utiliza Choice.

### Teorema 9.10.3 — $\mathbb R_C$ es un cuerpo ordenado

Con las operaciones y el orden construidos en este capítulo,

$$
\boxed{
(\mathbb R_C,+_C,\cdot_C,0_C,1_C,\le_C)
\text{ es un cuerpo ordenado.}
}
$$

**Demostración.**

Teorema 9.7.10 — $\mathbb R_C$ es un cuerpo demuestra que

$$
(\mathbb R_C,+_C,\cdot_C,0_C,1_C)
$$

es un cuerpo, y Teorema 9.8.5 — $\le_C$ es un orden total demuestra que $\le_C$ es un orden total sobre $\mathbb R_C$.

La primera compatibilidad exigida por Definición 4.1.1 — Cuerpo ordenado,

$$
x\le_C y
\Longrightarrow
x+z\le_C y+z,
$$

es exactamente Proposición 9.10.1 — Invariancia del orden de Cauchy por traslación.

La segunda,

$$
0_C\le_C x,
\quad
0_C\le_C y
\Longrightarrow
0_C\le_C xy,
$$

es Proposición 9.10.2 — El producto de elementos no negativos es no negativo.

Se satisfacen, por tanto, todas las condiciones de Definición 4.1.1 — Cuerpo ordenado. ∎

### Corolario 9.10.4 — La aplicación racional es una incrustación de cuerpos ordenados

La función

$$
\iota_C:\mathbb Q\to\mathbb R_C,
\qquad
q\longmapsto[\underline q]_C,
$$

es una incrustación de cuerpos ordenados en el sentido de Definición 4.8.1 — Incrustación de cuerpos ordenados.

**Demostración.**

Por Proposición 4.1.4 — $\mathbb Q$ es un cuerpo ordenado, $\mathbb Q$ es un cuerpo ordenado, y por Teorema 9.10.3 — $\mathbb R_C$ es un cuerpo ordenado, $\mathbb R_C$ también lo es.

La función $\iota_C$ fue construida en Definición 9.9.1 — Aplicación canónica de $\mathbb Q$ en $\mathbb R_C$. Proposición 9.9.2 — Igualdad de imágenes e inyectividad de $\iota_C$ demuestra que es inyectiva. Proposición 9.9.3 — Preservación de la aritmética racional establece

$$
\iota_C(0_{\mathbb Q})=0_C,
\qquad
\iota_C(1_{\mathbb Q})=1_C,
$$

$$
\iota_C(q+r)=\iota_C(q)+\iota_C(r),
$$

$$
\iota_C(qr)=\iota_C(q)\iota_C(r).
$$

Finalmente, Proposición 9.9.5 — Preservación y reflexión del orden racional demuestra, para cualesquiera $q,r\in\mathbb Q$,

$$
q\le r
\iff
\iota_C(q)\le_C\iota_C(r).
$$

Éstas son exactamente las condiciones de Definición 4.8.1 — Incrustación de cuerpos ordenados. ∎

### Lo que hemos ganado

La construcción de Cauchy ya no consiste sólo en un cociente de sucesiones con operaciones y un orden definidos por separado. Las dos estructuras han quedado acopladas:

$$
\boxed{
(\mathbb R_C,+_C,\cdot_C,0_C,1_C,\le_C)
\text{ es un cuerpo ordenado.}
}
$$

Además,

$$
\boxed{
\iota_C:\mathbb Q\to\mathbb R_C
}
$$

es ahora formalmente una incrustación de cuerpos ordenados. En particular, la copia racional dentro de $\mathbb R_C$ no es una convención de escritura: es la imagen de una función inyectiva que preserva exactamente la aritmética y el orden.

Desde este punto, todos los resultados abstractos demostrados en el Capítulo 4 para cuerpos ordenados pueden aplicarse legítimamente a $\mathbb R_C$: reglas de signos, positividad de inversos, invariancia estricta por traslación y multiplicación por factores positivos, valor absoluto y demás infraestructura estructural correspondiente.

No hemos usado para ello ningún hecho de completitud de $\mathbb R_D$, ni hemos identificado los racionales con un subconjunto literal de $\mathbb R_C$, ni hemos recurrido a Choice.

Con esto termina la construcción algebraica y ordenada del cuerpo de Cauchy. Lo que todavía falta para convertirlo en una completación ordenada de $\mathbb Q$ en el sentido de Definición 4.8.2 — Completación ordenada de $\mathbb Q$ es demostrar su completitud. Ése será el objeto del capítulo siguiente.
