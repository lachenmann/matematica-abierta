## 1.5. Producto de números naturales {#sec-ta-1-5}

La multiplicación se construye con el mismo principio, pero ahora la etapa sucesora no aplica $S$ directamente: añade una copia más del primer factor. Así, para $m$ fijo, el producto por $n$ se obtiene acumulando $m$ mediante la suma ya construida.

De nuevo la definición recursiva distingue los dos argumentos. Las leyes de unidad, distributividad, asociatividad y conmutatividad deberán surgir después como consecuencias.

### Definición 1.5.1 — Multiplicación {#ta-multiplicacion-naturales}

*Glosario: [multiplicación natural](../otros/tratado-de-analisis-glosario.md#gl-multiplicacion-natural)*

Por recursión con parámetros existe una única función

$$
\cdot:\mathbb N\times\mathbb N\to\mathbb N.
$$

Escribimos $m\cdot n$ o, cuando no haya ambigüedad, $mn$, y fijamos

$$
\boxed{m\cdot0=0}
$$

y

$$
\boxed{m\cdot S(n)=m\cdot n+m.}
$$

La recursión se realiza en el segundo argumento.

### Proposición 1.5.2 — El cero absorbe por la izquierda {#ta-cero-absorbe-izquierda-producto}

Para todo $n\in\mathbb N$,

$$
0\cdot n=0.
$$

**Demostración.**  
Inducción: $0\cdot0=0$; si $0\cdot n=0$, entonces $0\cdot S(n)=0\cdot n+0=0$. ∎

### Lema 1.5.3 — Sucesor en el primer argumento del producto {#ta-sucesor-primer-argumento-producto}

Para $m,n\in\mathbb N$,

$$
S(m)\cdot n=m\cdot n+n.
$$

**Demostración.**  
Inducimos sobre $n$. Para $0$ ambos lados son $0$. Supongamos la igualdad para $n$. Entonces

$$
S(m)\cdot S(n)=(m\cdot n+n)+S(m).
$$

Por asociatividad y conmutatividad de la suma,

$$
(m\cdot n+n)+S(m)=m\cdot n+(n+S(m)).
$$

Además

$$
n+S(m)=S(n+m)=S(m+n)=m+S(n).
$$

Luego

$$
S(m)\cdot S(n)=m\cdot n+(m+S(n))=(m\cdot n+m)+S(n)=m\cdot S(n)+S(n).
$$

∎

### Proposición 1.5.4 — Leyes de la unidad {#ta-unidad-producto}

*Glosario: [unidad multiplicativa](../otros/tratado-de-analisis-glosario.md#gl-unidad-multiplicativa)*

Para todo $m\in\mathbb N$,

$$
m\cdot1=m,
\qquad
1\cdot m=m.
$$

**Demostración.**  
Como $1=S(0)$,

$$
m\cdot1=m\cdot0+m=0+m=m.
$$

Y, por el Lema 1.5.3,

$$
1\cdot m=S(0)\cdot m=0\cdot m+m=0+m=m.
$$

∎

### Teorema 1.5.5 — Distributividad en el segundo factor {#ta-distributividad-producto-segundo-factor}

*Glosario: [distributividad](../otros/tratado-de-analisis-glosario.md#gl-distributividad-producto)*

Para $m,n,p\in\mathbb N$,

$$
m(n+p)=mn+mp.
$$

**Demostración.**  
Inducimos sobre $p$. Para $p=0$, $m(n+0)=mn=mn+0$. Si vale para $p$,

$$
\begin{aligned}
m(n+S(p))
&=mS(n+p)\\
&=m(n+p)+m\\
&=(mn+mp)+m\\
&=mn+(mp+m)\\
&=mn+mS(p).
\end{aligned}
$$

∎

### Teorema 1.5.6 — Asociatividad del producto {#ta-asociatividad-producto}

*Glosario: [asociatividad del producto](../otros/tratado-de-analisis-glosario.md#gl-asociatividad-producto)*

Para $a,b,c\in\mathbb N$,

$$
(ab)c=a(bc).
$$

**Demostración.**  
Inducción sobre $c$. Para $0$ ambos lados son $0$. Si vale para $c$,

$$
(ab)S(c)=(ab)c+ab=a(bc)+ab=a(bc+b)=a(bS(c)),
$$

usando el Teorema 1.5.5. ∎

### Teorema 1.5.7 — Conmutatividad del producto {#ta-conmutatividad-producto}

*Glosario: [conmutatividad del producto](../otros/tratado-de-analisis-glosario.md#gl-conmutatividad-producto)*

Para $a,b\in\mathbb N$,

$$
ab=ba.
$$

**Demostración.**  
Inducimos sobre $b$. Para $0$, $a0=0=0a$. Si $ab=ba$,

$$
aS(b)=ab+a=ba+a=S(b)a,
$$

por el Lema 1.5.3. ∎

### Corolario 1.5.8 — Distributividad en ambos lados {#ta-distributividad-ambos-lados}

Para $a,b,c\in\mathbb N$,

$$
a(b+c)=ab+ac,
\qquad
(a+b)c=ac+bc.
$$

**Demostración.**  
La primera es el Teorema 1.5.5; para la segunda,

$$
(a+b)c=c(a+b)=ca+cb=ac+bc.
$$

∎

### Proposición 1.5.9 — Producto nulo {#ta-producto-nulo}

*Glosario: [producto nulo](../otros/tratado-de-analisis-glosario.md#gl-producto-nulo)*

Para $a,b\in\mathbb N$,

$$
ab=0\iff a=0\text{ o }b=0.
$$

**Demostración.**  
Supongamos $ab=0$. Si $b=0$, terminamos. Si $b=S(k)$, entonces

$$
0=ab=ak+a,
$$

por lo que la Proposición 1.4.7 — Suma nula da $a=0$. La recíproca se sigue de las dos leyes absorbentes del cero. ∎

---
