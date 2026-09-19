## 10.5. De la completitud secuencial a la propiedad del supremo {#sec-ta-10-5}

La completitud secuencial obtenida en §10.4 todavía no es, por sí sola, la completitud de orden definida en Definición 4.6.1 — Propiedad del supremo y cuerpo ordenado completo. Debemos demostrar que todo subconjunto no vacío y acotado superiormente de $\mathbb R_C$ posee una menor cota superior.

El paso no será una apelación abstracta a una equivalencia conocida. En el tratado todavía no hemos demostrado que, en cualquier cuerpo ordenado, la completitud secuencial implique la propiedad del supremo; además, esa afirmación necesita una hipótesis arquimediana o una condición equivalente. Construiremos aquí el argumento necesario para el cuerpo concreto $\mathbb R_C$.

La estrategia tiene cuatro etapas:

1. demostrar que la copia racional hace a $\mathbb R_C$ **arquimediano**;
2. encerrar cualquier conjunto no vacío y acotado entre un extremo que no sea cota superior y otro que sí lo sea;
3. bisecar ese intervalo de manera **determinista en sentido extensional**, manteniendo ambos invariantes y haciendo tender su anchura a cero;
4. usar la completitud secuencial para obtener un límite común y demostrar que ese límite es exactamente el supremo.

La construcción es deliberadamente funcional. En cada etapa de bisección la pregunta «¿es el punto medio una cota superior?» tiene una respuesta lógica determinada; no escogeremos un elemento de $A$ en cada paso ni construiremos una familia de elecciones.

### Lema 10.5.1 — Compatibilidad de los numerales naturales con $\iota_C$

Sea

$$
\nu_{\mathbb R_C}:\mathbb N\longrightarrow\mathbb R_C
$$

la aplicación canónica de numerales naturales de Definición 4.1.5 — Aplicación de numerales naturales en un cuerpo ordenado, especializada al cuerpo ordenado $\mathbb R_C$. Entonces, para todo $n\in\mathbb N$,

$$
\boxed{
\nu_{\mathbb R_C}(n)
=
\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(n)\right).
}
$$

**Demostración.**

Por Proposición 4.4.3 — La formulación abstracta coincide con la arquimedianidad ya probada en $\mathbb Q$, la aplicación de numerales de $\mathbb Q$ coincide con $\nu_{\mathbb N}^{\mathbb Q}$. Demostraremos la igualdad por inducción sobre $n$.

Para $n=0$,

$$
\nu_{\mathbb R_C}(0)
=0_C
=
\iota_C(0_{\mathbb Q})
=
\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(0)\right),
$$

usando la preservación del cero de Proposición 9.9.3 — Preservación de la aritmética racional.

Supongamos

$$
\nu_{\mathbb R_C}(n)
=
\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(n)\right).
$$

Por la recursión que define los numerales y por la preservación de suma y unidad de $\iota_C$,

$$
\begin{aligned}
\nu_{\mathbb R_C}(S(n))
&=\nu_{\mathbb R_C}(n)+1_C\\
&=\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(n)\right)
  +\iota_C(1_{\mathbb Q})\\
&=\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}\right)\\
&=\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(S(n))\right).
\end{aligned}
$$

La inducción concluye la afirmación. ∎

> **Consecuencia tipológica.** Esta igualdad no identifica $\mathbb N$, $\mathbb Q$ y $\mathbb R_C$. Expresa la compatibilidad de las dos aplicaciones canónicas que conectan esos sistemas.

### Proposición 10.5.2 — El cuerpo de Cauchy es arquimediano

El cuerpo ordenado $\mathbb R_C$ es arquimediano.

**Demostración.**

Usaremos la caracterización por recíprocos pequeños de Proposición 4.4.2 — Caracterización por recíprocos pequeños. Sea

$$
\varepsilon\in\mathbb R_C,
\qquad
0_C<_C\varepsilon.
$$

Por Lema 10.1.2 — Escalas racionales positivas dentro de toda escala positiva de $\mathbb R_C$ existe $q\in\mathbb Q$ tal que

$$
0<q
\qquad\text{y}\qquad
0_C<_C\iota_C(q)<_C\varepsilon.
$$

El cuerpo racional es arquimediano por Proposición 4.4.3 — La formulación abstracta coincide con la arquimedianidad ya probada en $\mathbb Q$. Aplicando Proposición 4.4.2 — Caracterización por recíprocos pequeños dentro de $\mathbb Q$ a la tolerancia $q$, existe $n\in\mathbb N$, $n\neq0$, tal que

$$
0_{\mathbb Q}
<
\nu_{\mathbb N}^{\mathbb Q}(n)^{-1}
<q.
$$

La preservación del orden estricto por Proposición 9.9.5 — Preservación y reflexión del orden racional produce

$$
0_C
<_C
\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(n)^{-1}\right)
<_C
\iota_C(q).
$$

Como $n\neq0$, Proposición 4.1.6 — Aritmética y orden de los numerales naturales aplicado a $\mathbb Q$ muestra que $\nu_{\mathbb N}^{\mathbb Q}(n)\neq0_{\mathbb Q}$. La compatibilidad de $\iota_C$ con recíprocos (Corolario 9.9.4 — Compatibilidad con los recíprocos racionales) y Lema 10.5.1 — Compatibilidad de los numerales naturales con $\iota_C$ dan

$$
\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(n)^{-1}\right)
=
\iota_C\!\left(\nu_{\mathbb N}^{\mathbb Q}(n)\right)^{-1}
=
\nu_{\mathbb R_C}(n)^{-1}.
$$

Por tanto

$$
0_C
<_C
\nu_{\mathbb R_C}(n)^{-1}
<_C
\iota_C(q)
<_C
\varepsilon.
$$

Hemos verificado la condición de recíprocos positivos arbitrariamente pequeños. Por la implicación recíproca de Proposición 4.4.2 — Caracterización por recíprocos pequeños, $\mathbb R_C$ es arquimediano. ∎

La arquimedianidad es la pieza que permite hacer cuantitativamente pequeña una bisección. Ahora fijaremos el mecanismo de bisección sin seleccionar puntos del conjunto en cada etapa.

### Definición 10.5.3 — Operador de bisección respecto de las cotas superiores

Fijemos un subconjunto

$$
A\subseteq\mathbb R_C.
$$

Pongamos

$$
s_C:=1_C+1_C.
$$

Como $0_C<_C1_C$, se tiene $0_C<_Cs_C$, de modo que $s_C^{-1}$ existe y es positivo. Para $\ell,r\in\mathbb R_C$ definimos su punto medio por

$$
m(\ell,r)
:=(\ell+r)s_C^{-1}.
$$

Definimos entonces

$$
\boxed{
\beta_A:\mathbb R_C\times\mathbb R_C
\longrightarrow
\mathbb R_C\times\mathbb R_C
}
$$

mediante

$$
\boxed{
\beta_A(\ell,r)
=
\begin{cases}
(\ell,m(\ell,r)),
&\text{si }m(\ell,r)\text{ es cota superior de }A,\\[1mm]
(m(\ell,r),r),
&\text{si }m(\ell,r)\text{ no es cota superior de }A.
\end{cases}
}
$$

La condición «$m$ es cota superior de $A$» abrevia, conforme a Definición 0.7.4 — Cotas superiores e inferiores,

$$
\forall x\in A,\qquad x\le_C m.
$$

El grafo de $\beta_A$ existe por separación dentro de

$$
(\mathbb R_C\times\mathbb R_C)
\times
(\mathbb R_C\times\mathbb R_C).
$$

La lógica clásica garantiza que exactamente una de las dos ramas se aplica y cada rama determina un único par. Por tanto $\beta_A$ es una función total.

> **Nota fundacional.** No se escoge un elemento de $A$ cuando el punto medio deja de ser cota superior. La función es **determinista en sentido extensional**: LEM fija cuál de las dos proposiciones vale y cada rama tiene salida única. Pero el predicado
> $$
> \forall x\in A,\quad x\le_Cm
> $$
> no es decidible para un subconjunto arbitrario $A$. Por tanto,
> $$
> \boxed{
> \text{determinista extensionalmente}
> \neq
> \text{computable}.
> }
> $$

### Proposición 10.5.4 — Sucesiones de encajamiento asociadas a $A$

Sean $A\subseteq\mathbb R_C$, $a\in A$ y $u\in\mathbb R_C$ una cota superior de $A$. Existen sucesiones únicas

$$
(\ell_n)_{n\in\mathbb N},
\qquad
(r_n)_{n\in\mathbb N}
$$

de elementos de $\mathbb R_C$ tales que

$$
\boxed{
\ell_0=a-1_C,
\qquad
r_0=u,
}
$$

y

$$
\boxed{
(\ell_{S(n)},r_{S(n)})
=
\beta_A(\ell_n,r_n)
\qquad(n\in\mathbb N).
}
$$

**Demostración.**

Consideremos el conjunto de estados

$$
X:=\mathbb R_C\times\mathbb R_C
$$

y el estado inicial

$$
p_0:=(a-1_C,u)\in X.
$$

La definición anterior proporciona una función

$$
\beta_A:X\longrightarrow X.
$$

El teorema de recursión sobre $\mathbb N$, Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$, produce una única función

$$
p:\mathbb N\longrightarrow X
$$

tal que

$$
p(0)=p_0,
\qquad
p(S(n))=\beta_A(p(n)).
$$

Para cada $n$, el valor $p(n)$ es un único par de elementos de $\mathbb R_C$. Definimos $\ell_n$ y $r_n$ como su primera y segunda coordenada, respectivamente. Los grafos de ambas sucesiones se obtienen por separación y la unicidad de $p$ implica la unicidad de las dos coordenadas en cada índice.

Las condiciones inicial y recursiva son exactamente las anunciadas. ∎

### Lema 10.5.5 — Invariantes del encajamiento

En la situación de Proposición 10.5.4 — Sucesiones de encajamiento asociadas a $A$, para todo $n\in\mathbb N$ se cumplen:

1. $\ell_n$ **no** es cota superior de $A$;
2. $r_n$ es cota superior de $A$;
3. $\ell_n<_Cr_n$;
4. el paso es encajado:
   $$
   \ell_n\le_C\ell_{S(n)}<_Cr_{S(n)}\le_Cr_n;
   $$
5. si
   $$
   \delta_n:=r_n-\ell_n,
   $$
   entonces
   $$
   0_C<_C\delta_n
   $$
   y
   $$
   \boxed{
   \delta_{S(n)}=\delta_n s_C^{-1}.
   }
   $$

Además, si $m\le n$, entonces

$$
\boxed{
\ell_m\le_C\ell_n<_Cr_n\le_Cr_m.
}
$$

**Demostración.**

Comenzamos por el índice $0$. Como $0_C<_C1_C$, la invariancia estricta por traslación da

$$
a-1_C<_Ca.
$$

Si $\ell_0=a-1_C$ fuera cota superior de $A$, de $a\in A$ obtendríamos $a\le_Ca-1_C$, contradicción. Por tanto $\ell_0$ no es cota superior. El elemento

$$
r_0=u
$$

sí lo es por hipótesis. Además

$$
\ell_0<_Ca\le_Cu=r_0,
$$

de modo que $\ell_0<_Cr_0$.

Supongamos ahora que para un índice $n$ tenemos

$$
\ell_n<_Cr_n,
$$

con $\ell_n$ no cota superior y $r_n$ cota superior. El teorema del punto medio Teorema 4.1.11 — Todo cuerpo ordenado es densamente ordenado aplicado al cuerpo ordenado $\mathbb R_C$ afirma que

$$
\ell_n<_Cm_n<_Cr_n,
\qquad
m_n:=m(\ell_n,r_n).
$$

Hay dos casos.

Si $m_n$ es cota superior de $A$, la definición de $\beta_A$ da

$$
\ell_{S(n)}=\ell_n,
\qquad
r_{S(n)}=m_n.
$$

Así el extremo izquierdo sigue sin ser cota superior, el derecho sigue siendo cota superior y

$$
\ell_n
=
\ell_{S(n)}
<_C
r_{S(n)}
<_C
r_n.
$$

Si $m_n$ no es cota superior, entonces

$$
\ell_{S(n)}=m_n,
\qquad
r_{S(n)}=r_n,
$$

y obtenemos

$$
\ell_n
<_C
\ell_{S(n)}
<_C
r_{S(n)}
=
r_n.
$$

En ambos casos se preservan los tres primeros invariantes y se obtiene el encajamiento de un paso. Por inducción valen para todo $n$.

Para la anchura, en cualquiera de las dos ramas uno de los extremos es el punto medio. Usando

$$
m_n=(\ell_n+r_n)s_C^{-1}
$$

y

$$
s_C=1_C+1_C,
$$

las leyes del cuerpo dan, tanto si conservamos la mitad izquierda como si conservamos la derecha,

$$
\delta_{S(n)}
=
(r_n-\ell_n)s_C^{-1}
=
\delta_n s_C^{-1}.
$$

Como $\ell_n<_Cr_n$, tenemos $0_C<_C\delta_n$.

Falta justificar la forma global del encajamiento. Fijemos $m$. Por inducción sobre $k\in\mathbb N$, el encajamiento de un paso implica

$$
\ell_m\le_C\ell_{m+k}
\qquad\text{y}\qquad
r_{m+k}\le_Cr_m.
$$

El caso $k=0$ es inmediato. Si vale para $k$, entonces

$$
\ell_{m+k}\le_C\ell_{S(m+k)},
\qquad
r_{S(m+k)}\le_Cr_{m+k},
$$

y, como $m+S(k)=S(m+k)$, la transitividad cierra el paso inductivo.

Si $m\le n$, la definición del orden natural proporciona $k\in\mathbb N$ tal que $n=m+k$. Por tanto

$$
\ell_m\le_C\ell_n,
\qquad
r_n\le_Cr_m.
$$

Junto con $\ell_n<_Cr_n$ obtenemos la última fórmula. ∎

### Lema 10.5.6 — Las anchuras se hacen arbitrariamente pequeñas

Con la notación

$$
\delta_n:=r_n-\ell_n
$$

de Lema 10.5.5 — Invariantes del encajamiento, para todo $\varepsilon\in\mathbb R_C$ con $0_C<_C\varepsilon$, existe $N\in\mathbb N$ tal que, para todo $n\ge N$,

$$
\boxed{
0_C<_C\delta_n<_C\varepsilon.
}
$$

**Demostración.**

La prueba generaliza el argumento utilizado para las anchuras racionales en Lema 8.7.5 — Las anchuras se hacen arbitrariamente pequeñas, pero ahora se realiza enteramente en $\mathbb R_C$.

Primero probaremos

$$
\boxed{
n\neq0
\Longrightarrow
\nu_{\mathbb R_C}(n)\delta_n\le_C\delta_0.
}
$$

Es suficiente demostrar por inducción que

$$
\nu_{\mathbb R_C}(S(k))\delta_{S(k)}
\le_C
\delta_0
\qquad(k\in\mathbb N).
$$

Para $k=0$, Proposición 4.1.6 — Aritmética y orden de los numerales naturales da $\nu_{\mathbb R_C}(1)=1_C$, y Lema 10.5.5 — Invariantes del encajamiento da

$$
\delta_1=\delta_0s_C^{-1}.
$$

Como

$$
1_C<_Cs_C=1_C+1_C,
$$

la inversión del orden entre positivos produce

$$
0_C<_Cs_C^{-1}<_C1_C.
$$

Multiplicando por $\delta_0>_C0_C$,

$$
\nu_{\mathbb R_C}(1)\delta_1
=
\delta_0s_C^{-1}
<_C
\delta_0.
$$

Supongamos ahora

$$
\nu_{\mathbb R_C}(r)\delta_r\le_C\delta_0
$$

para $r=S(k)$. Por Proposición 1.4.2 — Cero neutro por la izquierda, $0+k=k$; usando Definición 1.6.1 — Orden aritmético con testigo $k$ obtenemos

$$
0\le k.
$$

Como Proposición 4.1.6 — Aritmética y orden de los numerales naturales preserva el orden natural,

$$
0_C
\le_C
\nu_{\mathbb R_C}(k).
$$

Sumando $1_C$ y usando la recursión de los numerales,

$$
1_C
\le_C
\nu_{\mathbb R_C}(k)+1_C
=
\nu_{\mathbb R_C}(S(k))
=
\nu_{\mathbb R_C}(r).
$$

Por tanto

$$
\begin{aligned}
\nu_{\mathbb R_C}(S(r))
&=\nu_{\mathbb R_C}(r)+1_C\\
&\le_C\nu_{\mathbb R_C}(r)+\nu_{\mathbb R_C}(r).
\end{aligned}
$$

La cantidad $\delta_{S(r)}=\delta_rs_C^{-1}$ es positiva. Multiplicando la desigualdad anterior por ella,

$$
\begin{aligned}
\nu_{\mathbb R_C}(S(r))\delta_{S(r)}
&\le_C
\bigl(\nu_{\mathbb R_C}(r)+\nu_{\mathbb R_C}(r)\bigr)
\delta_rs_C^{-1}\\
&=
\nu_{\mathbb R_C}(r)\delta_r\\
&\le_C
\delta_0.
\end{aligned}
$$

La inducción queda cerrada, y Teorema 1.2.7 — Predecesor de todo natural no nulo extiende la estimación a todo natural no nulo.

Sea ahora $\varepsilon>_C0_C$. Como $\delta_0>_C0_C$ y $\varepsilon^{-1}>_C0_C$,

$$
0_C<_C\delta_0\varepsilon^{-1}.
$$

La arquimedianidad de $\mathbb R_C$, Proposición 10.5.2 — El cuerpo de Cauchy es arquimediano, proporciona $N\in\mathbb N$ tal que

$$
\delta_0\varepsilon^{-1}
<_C
\nu_{\mathbb R_C}(N).
$$

El miembro izquierdo es positivo, luego $N\neq0$. Por la estimación anterior,

$$
\nu_{\mathbb R_C}(N)\delta_N
\le_C
\delta_0.
$$

Multiplicando la desigualdad arquimediana por $\varepsilon>_C0_C$,

$$
\delta_0
<_C
\varepsilon\nu_{\mathbb R_C}(N).
$$

Así

$$
\nu_{\mathbb R_C}(N)\delta_N
<_C
\varepsilon\nu_{\mathbb R_C}(N).
$$

Como $N\neq0$, Proposición 4.1.6 — Aritmética y orden de los numerales naturales da

$$
0_C<_C\nu_{\mathbb R_C}(N),
$$

y el escalamiento estricto por un factor positivo permite cancelarlo:

$$
\delta_N<_C\varepsilon.
$$

Finalmente, si $N\le n$, el encajamiento global de Lema 10.5.5 — Invariantes del encajamiento da

$$
\ell_N\le_C\ell_n<_Cr_n\le_Cr_N.
$$

Restando extremos,

$$
0_C<_C\delta_n
\le_C
\delta_N
<_C
\varepsilon.
$$

Esto prueba la afirmación. ∎

### Teorema 10.5.7 — Los extremos encajados convergen a una frontera común

En la situación de Proposición 10.5.4 — Sucesiones de encajamiento asociadas a $A$, manteniendo $\delta_n:=r_n-\ell_n$, existe un elemento $L\in\mathbb R_C$ tal que

$$
\boxed{
\ell_n\to_C L
\qquad\text{y}\qquad
r_n\to_C L.
}
$$

**Demostración.**

Demostraremos primero que $(\ell_n)$ es una sucesión de Cauchy en $\mathbb R_C$. Sea $\varepsilon>_C0_C$. Por Lema 10.5.6 — Las anchuras se hacen arbitrariamente pequeñas existe $N$ tal que

$$
\delta_N<_C\varepsilon.
$$

Sean $m,n\ge N$. El orden natural es total; supongamos, sin pérdida de generalidad, $m\le n$. El encajamiento global da

$$
\ell_N
\le_C
\ell_m
\le_C
\ell_n
<_C
r_N.
$$

Por tanto

$$
0_C
\le_C
\ell_n-\ell_m
\le_C
r_N-\ell_N
=
\delta_N.
$$

Como $\ell_m\le_C\ell_n$, la definición del valor absoluto da

$$
|\ell_m-\ell_n|
=
\ell_n-\ell_m
\le_C
\delta_N
<_C
\varepsilon.
$$

El caso $n\le m$ es simétrico. Así $(\ell_n)$ es de Cauchy.

Por la completitud secuencial Corolario 10.4.8 — $\mathbb R_C$ es secuencialmente completo, existe $L\in\mathbb R_C$ tal que

$$
\ell_n\to_C L.
$$

Mostremos que el extremo derecho converge al mismo $L$. Sea $\varepsilon>_C0_C$ y definamos

$$
\theta:=\varepsilon s_C^{-1}.
$$

Como $s_C>_C0_C$,

$$
0_C<_C\theta
$$

y

$$
\theta+\theta=\varepsilon.
$$

Por Lema 10.5.6 — Las anchuras se hacen arbitrariamente pequeñas, existe $N_0$ tal que

$$
n\ge N_0
\Longrightarrow
\delta_n<_C\theta.
$$

Como $\ell_n\to_C L$, existe $N_1$ tal que

$$
n\ge N_1
\Longrightarrow
|\ell_n-L|<_C\theta.
$$

Tomemos como $N$ el mayor de $N_0$ y $N_1$, obtenido por una comparación finita en $\mathbb N$. Para $n\ge N$, la desigualdad triangular da

$$
\begin{aligned}
|r_n-L|
&\le_C
|r_n-\ell_n|+|\ell_n-L|\\
&=
\delta_n+|\ell_n-L|\\
&<_C
\theta+\theta\\
&=
\varepsilon.
\end{aligned}
$$

Por Definición 10.4.1 — Convergencia en $\mathbb R_C$,

$$
r_n\to_C L.
$$

Ambas sucesiones convergen, por tanto, a la misma frontera. ∎

### Teorema 10.5.8 — Propiedad del supremo de $\mathbb R_C$

Sea

$$
A\subseteq\mathbb R_C
$$

no vacío y acotado superiormente. Entonces existe $L\in\mathbb R_C$ tal que

$$
\boxed{L=\sup A.}
$$

En consecuencia, $\mathbb R_C$ tiene la propiedad del supremo.

**Demostración.**

Como $A$ es no vacío, fijemos un único elemento

$$
a\in A.
$$

Como $A$ está acotado superiormente, fijemos una única cota superior

$$
u\in\mathbb R_C.
$$

> **Nota lógica.** En la interfaz clásica vigente, «$A$ no vacío» y «$A$ acotado superiormente» permiten instanciar localmente los testigos $a$ y $u$. Esto no es una elección de una familia, pero debe distinguirse de recibir esos testigos positivamente como parte de los datos de entrada.

Aplicamos Proposición 10.5.4 — Sucesiones de encajamiento asociadas a $A$ a $A,a,u$. Obtenemos las sucesiones $(\ell_n)$ y $(r_n)$, y Lema 10.5.5 — Invariantes del encajamiento asegura para todo $n$ que

$$
\ell_n\text{ no es cota superior de }A,
$$

mientras que

$$
r_n\text{ sí es cota superior de }A.
$$

Por Teorema 10.5.7 — Los extremos encajados convergen a una frontera común existe $L\in\mathbb R_C$ con

$$
\ell_n\to_C L,
\qquad
r_n\to_C L.
$$

Demostraremos que $L$ es la menor cota superior de $A$.

**Primero, $L$ es cota superior.** Sea $x\in A$. Supongamos, por contradicción,

$$
L<_Cx.
$$

Entonces

$$
\varepsilon:=x-L
$$

es positivo. Como $r_n\to_C L$, existe $N$ tal que

$$
|r_N-L|<_Cx-L.
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto,

$$
r_N-L
\le_C
|r_N-L|
<_C
x-L.
$$

La invariancia del orden por traslación da

$$
r_N<_Cx.
$$

Pero $r_N$ es cota superior de $A$ y $x\in A$, luego

$$
x\le_Cr_N,
$$

contradicción. Por totalidad del orden, necesariamente

$$
x\le_CL.
$$

Como $x\in A$ era arbitrario, $L$ es cota superior de $A$.

**Segundo, $L$ es menor o igual que toda cota superior.** Sea $c$ una cota superior cualquiera de $A$. Supongamos, por contradicción,

$$
c<_CL.
$$

Entonces

$$
\varepsilon:=L-c>_C0_C.
$$

Como $\ell_n\to_C L$, existe $N$ tal que

$$
|\ell_N-L|<_CL-c.
$$

Por simetría del valor absoluto y Proposición 4.2.2 — Propiedades elementales del valor absoluto,

$$
L-\ell_N
\le_C
|L-\ell_N|
=
|\ell_N-L|
<_C
L-c.
$$

Trasladando la desigualdad obtenemos

$$
c<_C\ell_N.
$$

Ahora bien, $\ell_N$ no es cota superior de $A$. Por definición de cota superior,

$$
\neg\forall y\in A\;(y\le_C\ell_N).
$$

Por lógica clásica existe $y\in A$ tal que

$$
\neg(y\le_C\ell_N).
$$

Como el orden es total,

$$
\ell_N<_Cy.
$$

Pero $c$ es cota superior y $y\in A$, por lo que

$$
y\le_Cc.
$$

Hemos obtenido

$$
c<_C\ell_N<_Cy\le_Cc,
$$

contradicción. Por tanto

$$
L\le_Cc
$$

para toda cota superior $c$ de $A$.

Hemos demostrado exactamente las dos condiciones de Definición 0.7.7 — Supremo e ínfimo: $L$ es cota superior de $A$ y no excede a ninguna otra cota superior. Luego

$$
L=\sup A.
$$

∎

> **Nota fundacional.** El teorema establece existencia y unicidad extensional del supremo para cada conjunto que satisface las hipótesis. No construye un operador computable uniforme
> $$
> A\longmapsto\sup A.
> $$
> En particular,
> $$
> \boxed{
> \text{propiedad del supremo}
> \neq
> \text{algoritmo de supremo}.
> }
> $$

### Corolario 10.5.9 — $\mathbb R_C$ es un cuerpo ordenado completo

Se tiene

$$
\boxed{
(\mathbb R_C,+_C,\cdot_C,\le_C)
\text{ es un cuerpo ordenado completo}.
}
$$

**Demostración.**

Teorema 9.10.3 — $\mathbb R_C$ es un cuerpo ordenado demuestra que $\mathbb R_C$ es un cuerpo ordenado. Teorema 10.5.8 — Propiedad del supremo de $\mathbb R_C$ demuestra que todo subconjunto no vacío y acotado superiormente de $\mathbb R_C$ posee supremo. Ésta es exactamente la propiedad exigida por Definición 4.6.1 — Propiedad del supremo y cuerpo ordenado completo para ser un cuerpo ordenado completo. ∎

> **Conclusión de la sección.** La construcción por Cauchy ha alcanzado ahora la misma propiedad estructural que se exigió abstractamente en el capítulo 4: $\mathbb R_C$ no sólo absorbe todas sus sucesiones de Cauchy, sino que tampoco contiene huecos de orden. La prueba se obtuvo desde su propia completitud secuencial y su propia estructura ordenada, sin utilizar cortaduras de Dedekind.
