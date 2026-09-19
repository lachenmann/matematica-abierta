## 9.6. Cero, unidad, opuesto y estructura de anillo {#sec-ta-9-6}

Las operaciones binarias ya han descendido al cociente. El siguiente paso consiste en comprobar que la aritmética racional término a término transmite a las clases la estructura algebraica esperada.

Hay, sin embargo, una precaución que conviene mantener visible. Los símbolos $0_{\mathbb Q}$ y $1_{\mathbb Q}$ designan racionales; sus sucesiones constantes $\underline{0_{\mathbb Q}}$ y $\underline{1_{\mathbb Q}}$ son elementos de $\mathcal C_{\mathbb Q}$; y sólo sus **clases** serán los elementos distinguidos de $\mathbb R_C$. No identificaremos ninguno de estos tres niveles.

### Definición 9.6.1 — Cero y unidad de Cauchy

Por Proposición 8.4.4 — Las sucesiones constantes son de Cauchy, las sucesiones constantes

$$
\underline{0_{\mathbb Q}},
\qquad
\underline{1_{\mathbb Q}}
$$

pertenecen a $\mathcal C_{\mathbb Q}$. Por tanto sus clases pertenecen a $\mathbb R_C$.

Definimos

$$
\boxed{
0_C
:=
[\underline{0_{\mathbb Q}}]_C
}
$$

y

$$
\boxed{
1_C
:=
[\underline{1_{\mathbb Q}}]_C.
}
$$

Así,

$$
0_C,1_C\in\mathbb R_C.
$$

Estas definiciones no identifican $0_{\mathbb Q}$ con $0_C$, ni $1_{\mathbb Q}$ con $1_C$. Los primeros son racionales; los segundos son clases de equivalencia de sucesiones racionales de Cauchy.

### Proposición 9.6.2 — Leyes del cero y de la unidad

Para todo $x\in\mathbb R_C$,

$$
\boxed{
x+0_C=0_C+x=x,
}
$$

$$
\boxed{
x1_C=1_Cx=x,
}
$$

y

$$
\boxed{
x0_C=0_Cx=0_C.
}
$$

**Demostración.**

Sea $x\in\mathbb R_C$. Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existe una sucesión

$$
a\in\mathcal C_{\mathbb Q}
$$

tal que

$$
x=[a]_C.
$$

Para cada $n\in\mathbb N$, las leyes del grupo aditivo racional (Proposición 3.3.8 — Leyes del grupo aditivo racional) dan

$$
(a+\underline{0_{\mathbb Q}})_n
=
a_n+0_{\mathbb Q}
=
a_n.
$$

Por igualdad término a término (Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones),

$$
a+\underline{0_{\mathbb Q}}=a.
$$

Usando Definición 9.5.4 — Suma y producto en $\mathbb R_C$ y Definición 9.6.1 — Cero y unidad de Cauchy,

$$
\begin{aligned}
x+0_C
&=[a]_C+[\underline{0_{\mathbb Q}}]_C\\
&=[a+\underline{0_{\mathbb Q}}]_C\\
&=[a]_C\\
&=x.
\end{aligned}
$$

La identidad $0_C+x=x$ se demuestra del mismo modo, o bien usando la conmutatividad racional término a término.

Para la unidad, Proposición 3.4.5 — Leyes multiplicativas y distributivas da para todo $n$,

$$
(a\,\underline{1_{\mathbb Q}})_n
=
a_n1_{\mathbb Q}
=
a_n,
$$

por lo que

$$
a\,\underline{1_{\mathbb Q}}=a.
$$

Así,

$$
x1_C
=[a\,\underline{1_{\mathbb Q}}]_C
=[a]_C
=x,
$$

y análogamente $1_Cx=x$.

Finalmente, derivamos la absorción racional del cero de las leyes ya disponibles. Para cada $n$, la distributividad de Proposición 3.4.5 — Leyes multiplicativas y distributivas da

$$
a_n0_{\mathbb Q}
=
a_n(0_{\mathbb Q}+0_{\mathbb Q})
=
a_n0_{\mathbb Q}+a_n0_{\mathbb Q}.
$$

Cancelando aditivamente $a_n0_{\mathbb Q}$ mediante las leyes de grupo de Proposición 3.3.8 — Leyes del grupo aditivo racional, obtenemos

$$
a_n0_{\mathbb Q}=0_{\mathbb Q}.
$$

Por tanto

$$
(a\,\underline{0_{\mathbb Q}})_n
=
0_{\mathbb Q}
=
\underline{0_{\mathbb Q}}{}_n.
$$

Luego

$$
a\,\underline{0_{\mathbb Q}}
=
\underline{0_{\mathbb Q}},
$$

y por tanto

$$
x0_C=0_C.
$$

El caso $0_Cx=0_C$ es análogo. ∎

### Proposición 9.6.3 — El opuesto término a término preserva Cauchy y respeta $\sim_C$

Se cumplen las dos afirmaciones siguientes:

1. si $a\in\mathcal C_{\mathbb Q}$, entonces $-a\in\mathcal C_{\mathbb Q}$;
2. si $a,b\in\mathcal C_{\mathbb Q}$ y $a\sim_C b$, entonces
   $$
   -a\sim_C-b.
   $$

**Demostración.**

**(1)** Sea $a\in\mathcal C_{\mathbb Q}$ y sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Como $a$ es de Cauchy, existe $N\in\mathbb N$ tal que, para cualesquiera $m,n\ge N$,

$$
|a_m-a_n|<\varepsilon.
$$

Para esos mismos $m,n$, usando las leyes aditivas racionales y la invariancia del valor absoluto frente al opuesto (Proposición 4.2.2 — Propiedades elementales del valor absoluto),

$$
\begin{aligned}
|(-a)_m-(-a)_n|
&=|-a_m-(-a_n)|\\
&=|-a_m+a_n|\\
&=|-(a_m-a_n)|\\
&=|a_m-a_n|\\
&<\varepsilon.
\end{aligned}
$$

Por Definición 8.4.1 — Sucesión racional de Cauchy, $-a$ es de Cauchy; por tanto

$$
-a\in\mathcal C_{\mathbb Q}.
$$

**(2)** Supongamos ahora

$$
a\sim_C b.
$$

Por Definición 9.3.1 — Equivalencia de Cauchy,

$$
a-b\in\mathcal N_{\mathbb Q}.
$$

La estabilidad de las sucesiones nulas bajo opuesto (Proposición 9.2.3 — Estabilidad aditiva de las sucesiones nulas) da

$$
-(a-b)\in\mathcal N_{\mathbb Q}.
$$

Por otro lado, para todo $n\in\mathbb N$,

$$
\begin{aligned}
\bigl((-a)-(-b)\bigr)_n
&=(-a_n)-(-b_n)\\
&=-(a_n-b_n)\\
&=\bigl(-(a-b)\bigr)_n.
\end{aligned}
$$

De Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones se sigue

$$
(-a)-(-b)=-(a-b).
$$

Por consiguiente,

$$
(-a)-(-b)\in\mathcal N_{\mathbb Q},
$$

y entonces, por definición de $\sim_C$,

$$
-a\sim_C-b.
$$

∎

### Proposición 9.6.4 — Existencia y unicidad de la operación de opuesto

Existe una única función

$$
\boxed{
\nu_C:\mathbb R_C\to\mathbb R_C
}
$$

tal que, para todo $a\in\mathcal C_{\mathbb Q}$,

$$
\boxed{
\nu_C([a]_C)=[-a]_C.
}
$$

**Demostración.**

Definimos por separación

$$
G_{\nu}
:=
\left\{
\langle x,y\rangle
\in
\mathbb R_C\times\mathbb R_C:
\exists a\in\mathcal C_{\mathbb Q}
\bigl(
 x=[a]_C
 \land
 y=[-a]_C
\bigr)
\right\}.
$$

Sea $x\in\mathbb R_C$. Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existe $a\in\mathcal C_{\mathbb Q}$ con $x=[a]_C$. Por Proposición 9.6.3 — El opuesto término a término preserva Cauchy y respeta $\sim_C$, $-a\in\mathcal C_{\mathbb Q}$, de modo que

$$
[-a]_C\in\mathbb R_C.
$$

Así, $G_{\nu}$ es total sobre $\mathbb R_C$.

Para la unicidad del valor, supongamos que también

$$
x=[b]_C
$$

con $b\in\mathcal C_{\mathbb Q}$. Entonces

$$
[a]_C=[b]_C,
$$

por lo que Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy implica

$$
a\sim_C b.
$$

La compatibilidad demostrada en Proposición 9.6.3 — El opuesto término a término preserva Cauchy y respeta $\sim_C$ da

$$
-a\sim_C-b,
$$

y nuevamente por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy,

$$
[-a]_C=[-b]_C.
$$

Por tanto $G_{\nu}$ es univaluado y constituye el grafo de una función

$$
\nu_C:\mathbb R_C\to\mathbb R_C.
$$

La unicidad de la función sigue de Proposición 0.6.3 — Criterio de igualdad de funciones, pues su valor queda forzado en toda clase $[a]_C$. ∎

### Definición 9.6.5 — Opuesto y sustracción en $\mathbb R_C$

Para $x\in\mathbb R_C$ definimos su **opuesto aditivo** por

$$
\boxed{
-x:=\nu_C(x).
}
$$

En particular, si $a\in\mathcal C_{\mathbb Q}$,

$$
\boxed{
-[a]_C=[-a]_C.
}
$$

Para $x,y\in\mathbb R_C$ definimos además la sustracción por

$$
\boxed{
x-y:=x+(-y).
}
$$

Por las definiciones de las operaciones inducidas, para cualesquiera $a,b\in\mathcal C_{\mathbb Q}$ se obtiene

$$
\boxed{
[a]_C-[b]_C=[a-b]_C.
}
$$

No se introduce una nueva operación primitiva: la sustracción queda definida a partir de la suma y del opuesto, exactamente como en los sistemas numéricos anteriores.

### Teorema 9.6.6 — $\mathbb R_C$ es un anillo conmutativo con identidad

Con las operaciones y elementos distinguidos ya definidos,

$$
\boxed{
(\mathbb R_C,+_C,\cdot_C,0_C,1_C)
}
$$

es un **anillo conmutativo con identidad**.

**Demostración.**

Sean

$$
x,y,z\in\mathbb R_C.
$$

Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existen representantes locales

$$
a,b,c\in\mathcal C_{\mathbb Q}
$$

tales que

$$
x=[a]_C,
\qquad
y=[b]_C,
\qquad
z=[c]_C.
$$

No necesitamos fijar representantes de ninguna otra clase.

**Asociatividad de la suma.** Para todo $n\in\mathbb N$, la asociatividad racional da

$$
((a+b)+c)_n
=(a_n+b_n)+c_n
=a_n+(b_n+c_n)
=(a+(b+c))_n.
$$

Por Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones,

$$
(a+b)+c=a+(b+c).
$$

Por tanto

$$
\begin{aligned}
(x+y)+z
&=[(a+b)+c]_C\\
&=[a+(b+c)]_C\\
&=x+(y+z).
\end{aligned}
$$

**Conmutatividad de la suma.** Del mismo modo,

$$
(a+b)_n=a_n+b_n=b_n+a_n=(b+a)_n,
$$

luego

$$
x+y=y+x.
$$

**Neutro e inversos aditivos.** Las leyes del cero ya fueron probadas en Proposición 9.6.2 — Leyes del cero y de la unidad. Además,

$$
\begin{aligned}
x+(-x)
&=[a]_C+[-a]_C\\
&=[a+(-a)]_C.
\end{aligned}
$$

Para todo $n$,

$$
(a+(-a))_n
=a_n+(-a_n)
=0_{\mathbb Q}
=
\underline{0_{\mathbb Q}}{}_n.
$$

Así

$$
a+(-a)=\underline{0_{\mathbb Q}},
$$

y en consecuencia

$$
x+(-x)=0_C.
$$

Por la conmutatividad ya demostrada,

$$
(-x)+x=0_C.
$$

Por tanto $(\mathbb R_C,+_C,0_C)$ es un grupo abeliano.

**Asociatividad y conmutatividad del producto.** Las identidades racionales de Proposición 3.4.5 — Leyes multiplicativas y distributivas dan término a término

$$
(ab)c=a(bc)
$$

y

$$
ab=ba.
$$

Luego

$$
(xy)z=x(yz)
$$

y

$$
xy=yx.
$$

La ley de la unidad fue establecida en Proposición 9.6.2 — Leyes del cero y de la unidad.

**Distributividad.** Para cada $n\in\mathbb N$,

$$
\begin{aligned}
(a(b+c))_n
&=a_n(b_n+c_n)\\
&=a_nb_n+a_nc_n\\
&=(ab+ac)_n.
\end{aligned}
$$

Por tanto

$$
\begin{aligned}
x(y+z)
&=[a(b+c)]_C\\
&=[ab+ac]_C\\
&=xy+xz.
\end{aligned}
$$

La distributividad por la derecha se obtiene análogamente —o a partir de la conmutatividad del producto—:

$$
(x+y)z=xz+yz.
$$

Hemos probado las leyes de grupo abeliano para la suma, de monoide conmutativo para el producto y las dos leyes distributivas. Según la convención algebraica Convención 2.6.2 — Terminología algebraica, esto demuestra que $\mathbb R_C$ es un anillo conmutativo con identidad. ∎

> **Nota estructural.** La prueba no «transfiere» informalmente las leyes desde $\mathbb Q$. Cada igualdad en el cociente se reduce primero a una identidad entre sucesiones representantes y ésta, a su vez, se verifica término a término en $\mathbb Q$.

### Proposición 9.6.7 — Distinción entre cero y unidad

En $\mathbb R_C$,

$$
\boxed{
0_C\ne1_C.
}
$$

**Demostración.**

Supongamos, para obtener una contradicción, que

$$
0_C=1_C.
$$

Por Definición 9.6.1 — Cero y unidad de Cauchy, esto significa

$$
[\underline{0_{\mathbb Q}}]_C
=
[\underline{1_{\mathbb Q}}]_C.
$$

El criterio de igualdad de clases Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy implica entonces

$$
\underline{0_{\mathbb Q}}
-
\underline{1_{\mathbb Q}}
\in
\mathcal N_{\mathbb Q}.
$$

Por la compatibilidad de las sucesiones constantes con la sustracción (Proposición 8.1.5 — Compatibilidad de las sucesiones constantes con las operaciones puntuales),

$$
\underline{0_{\mathbb Q}}
-
\underline{1_{\mathbb Q}}
=
\underline{0_{\mathbb Q}-1_{\mathbb Q}}.
$$

Pongamos

$$
r:=0_{\mathbb Q}-1_{\mathbb Q}.
$$

La pertenencia anterior a $\mathcal N_{\mathbb Q}$ y Definición 9.2.1 — Sucesión racional nula y conjunto $\mathcal N_{\mathbb Q}$ muestran que

$$
\underline r_n\to_{\mathbb Q}0_{\mathbb Q}.
$$

Pero Proposición 8.3.4 — Las sucesiones constantes convergen a su valor, aplicado a la sucesión constante $\underline r$, da también

$$
\underline r_n\to_{\mathbb Q}r.
$$

Por unicidad del límite racional (Teorema 8.3.5 — Unicidad del límite racional),

$$
r=0_{\mathbb Q}.
$$

Así,

$$
0_{\mathbb Q}-1_{\mathbb Q}=0_{\mathbb Q}.
$$

Las leyes del grupo aditivo racional (Proposición 3.3.8 — Leyes del grupo aditivo racional) permiten sumar $1_{\mathbb Q}$ a ambos miembros y concluir

$$
0_{\mathbb Q}=1_{\mathbb Q},
$$

contradiciendo Proposición 3.4.6 — Distinción entre cero y uno. Por tanto

$$
0_C\ne1_C.
$$

∎

### Lo que hemos ganado

La construcción de Cauchy ha alcanzado ahora una estructura algebraica completa hasta el nivel de anillo:

$$
\boxed{
(\mathbb R_C,+_C,\cdot_C,0_C,1_C)
\text{ es un anillo conmutativo no trivial con identidad.}
}
$$

Además, el opuesto y la sustracción están definidos intrínsecamente en el cociente y satisfacen

$$
-[a]_C=[-a]_C,
\qquad
[a]_C-[b]_C=[a-b]_C.
$$

El único axioma algebraico de cuerpo que todavía falta es la existencia de inverso multiplicativo para todo elemento no nulo. Éste es el primer punto de la construcción de Cauchy en que no basta una operación término a término ingenua: un representante de una clase no nula puede contener ceros en posiciones finitas, y antes de tomar recíprocos debemos demostrar que toda clase no nula admite un control **eventual** que la separa de cero.

Ese será el siguiente frente. Todavía no definiremos el inverso hasta haber demostrado esa separación eventual y construido, sin Choice, un representante recíproco legítimo.
