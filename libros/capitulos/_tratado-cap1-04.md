## 1.4. Suma de números naturales {#sec-ta-1-4}

Estamos finalmente en condiciones de definir una operación aritmética. Para un natural fijo $m$, queremos comenzar en $m$ y aplicar el sucesor tantas veces como indique el segundo argumento. La recursión produce exactamente esa función.

La definición será deliberadamente **asimétrica**: recursaremos sobre el segundo argumento. Nada nos autoriza todavía a intercambiar los dos argumentos. La futura conmutatividad será un teorema y no una propiedad introducida de contrabando en la definición.

### Definición 1.4.1 — Adición {#ta-adicion-naturales}

*Glosario: [adición natural](../otros/tratado-de-analisis-glosario.md#gl-adicion-natural)*

Por recursión con parámetros existe una única función

$$
+:\mathbb N\times\mathbb N\to\mathbb N.
$$

Escribimos su valor como $m+n$ y la caracterizamos por

$$
\boxed{m+0=m}
$$

y

$$
\boxed{m+S(n)=S(m+n).}
$$

La recursión se realiza en el segundo argumento.

### Proposición 1.4.2 — Cero neutro por la izquierda {#ta-cero-neutro-izquierda-suma}

Para todo $n\in\mathbb N$,

$$
0+n=n.
$$

**Demostración.**  
Inducción: $0+0=0$; si $0+n=n$, entonces $0+S(n)=S(0+n)=S(n)$. ∎

### Lema 1.4.3 — Sucesor en el primer argumento {#ta-sucesor-primer-argumento-suma}

Para $m,n\in\mathbb N$,

$$
S(m)+n=S(m+n).
$$

**Demostración.**  
Inducimos sobre $n$. Para $n=0$, $S(m)+0=S(m)=S(m+0)$. Si $S(m)+n=S(m+n)$, entonces

$$
S(m)+S(n)=S(S(m)+n)=S(S(m+n))=S(m+S(n)).
$$

∎

### Teorema 1.4.4 — Asociatividad de la suma {#ta-asociatividad-suma}

*Glosario: [asociatividad de la suma](../otros/tratado-de-analisis-glosario.md#gl-asociatividad-suma)*

Para $a,b,c\in\mathbb N$,

$$
(a+b)+c=a+(b+c).
$$

**Demostración.**  
Inducción sobre $c$. El caso $0$ es la ecuación inicial. Si vale para $c$,

$$
(a+b)+S(c)=S((a+b)+c)=S(a+(b+c))=a+S(b+c)=a+(b+S(c)).
$$

∎

### Teorema 1.4.5 — Conmutatividad de la suma {#ta-conmutatividad-suma}

*Glosario: [conmutatividad de la suma](../otros/tratado-de-analisis-glosario.md#gl-conmutatividad-suma)*

Para $a,b\in\mathbb N$,

$$
a+b=b+a.
$$

**Demostración.**  
Fijamos $a$ e inducimos sobre $b$. Para $b=0$, $a+0=a=0+a$. Si $a+b=b+a$,

$$
a+S(b)=S(a+b)=S(b+a)=S(b)+a,
$$

por el Lema 1.4.3. ∎

### Proposición 1.4.6 — Cancelación aditiva {#ta-cancelacion-aditiva}

*Glosario: [cancelación aditiva](../otros/tratado-de-analisis-glosario.md#gl-cancelacion-aditiva)*

Si

$$
a+c=b+c,
$$

entonces $a=b$.

**Demostración.**  
Inducción sobre $c$. Para $c=0$, $a+0=b+0$ es exactamente $a=b$. Para $S(c)$, la igualdad se convierte en $S(a+c)=S(b+c)$; la inyectividad del sucesor reduce al caso inductivo. ∎

### Proposición 1.4.7 — Suma nula {#ta-suma-nula}

*Glosario: [suma nula](../otros/tratado-de-analisis-glosario.md#gl-suma-nula)*

Para $a,b\in\mathbb N$,

$$
a+b=0\iff a=0\text{ y }b=0.
$$

**Demostración.**  
Si $b=S(k)$, entonces $a+b=S(a+k)\neq0$. Luego $b=0$; entonces $a=a+b=0$. La recíproca es inmediata. ∎
