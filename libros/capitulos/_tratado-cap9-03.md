## 9.3. Relación de equivalencia {#sec-ta-9-3}

Dos sucesiones de Cauchy no deben representar números distintos si su diferencia se hace asintóticamente despreciable. La noción de sucesión nula construida en §9.2 permite expresar esta idea sin invocar ningún número real previamente existente.

### Definición 9.3.1 — Equivalencia de Cauchy

Definimos una relación sobre $\mathcal C_{\mathbb Q}$ por

$$
\boxed{
a\sim_C b
\iff
a-b\in\mathcal N_{\mathbb Q}.
}
$$

Conjuntistamente,

$$
\boxed{
\sim_C
:=
\left\{
\langle a,b\rangle
\in
\mathcal C_{\mathbb Q}\times\mathcal C_{\mathbb Q}:
a-b\in\mathcal N_{\mathbb Q}
\right\}.
}
$$

El producto cartesiano $\mathcal C_{\mathbb Q}\times\mathcal C_{\mathbb Q}$ existe por Proposición 0.3.7 — Existencia del producto cartesiano, y el subconjunto indicado existe por separación. Como $a,b\in\mathcal C_{\mathbb Q}\subseteq\mathbb Q^{\mathbb N}$, la diferencia puntual $a-b$ está definida por Definición 8.1.3 — Operaciones puntuales sobre sucesiones racionales. Por tanto $\sim_C$ es una relación binaria bien formada sobre $\mathcal C_{\mathbb Q}$.

Desplegando las definiciones, para $a,b\in\mathcal C_{\mathbb Q}$ tenemos

$$
a\sim_C b
$$

si y sólo si

$$
\forall\varepsilon\in\mathbb Q\;
\Bigl(
0<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\in\mathbb N\;
\bigl(
N\le n
\Longrightarrow
|a_n-b_n|<\varepsilon
\bigr)
\Bigr).
$$

Equivalentemente, mediante la distancia racional,

$$
\forall\varepsilon>0\;
\exists N\in\mathbb N\;
\forall n\ge N,
\qquad
d_{\mathbb Q}(a_n,b_n)<\varepsilon.
$$

Así, $a\sim_C b$ significa exactamente que ambas sucesiones se hacen mutuamente arbitrariamente próximas en sentido racional.

---

### Proposición 9.3.2 — $\sim_C$ es una relación de equivalencia

La relación $\sim_C$ es reflexiva, simétrica y transitiva sobre $\mathcal C_{\mathbb Q}$. En consecuencia, es una relación de equivalencia.

**Demostración.**

**Reflexividad.** Sea $a\in\mathcal C_{\mathbb Q}$. Para todo $n\in\mathbb N$,

$$
(a-a)_n
=
a_n-a_n
=
0_{\mathbb Q}
=
\underline{0_{\mathbb Q}}{}_n.
$$

Por el criterio término a término Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones,

$$
a-a=\underline{0_{\mathbb Q}}.
$$

La proposición Proposición 9.2.3 — Estabilidad aditiva de las sucesiones nulas (1) da

$$
\underline{0_{\mathbb Q}}\in\mathcal N_{\mathbb Q}.
$$

Por tanto

$$
a-a\in\mathcal N_{\mathbb Q},
$$

y, por definición,

$$
a\sim_C a.
$$

**Simetría.** Sean $a,b\in\mathcal C_{\mathbb Q}$ y supongamos

$$
a\sim_C b.
$$

Entonces

$$
a-b\in\mathcal N_{\mathbb Q}.
$$

Por la estabilidad bajo opuestos de Proposición 9.2.3 — Estabilidad aditiva de las sucesiones nulas,

$$
-(a-b)\in\mathcal N_{\mathbb Q}.
$$

Para cada $n\in\mathbb N$, las leyes del grupo aditivo racional dan

$$
\bigl(-(a-b)\bigr)_n
=
-(a_n-b_n)
=
b_n-a_n
=
(b-a)_n.
$$

Por Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones,

$$
b-a=-(a-b).
$$

Así

$$
b-a\in\mathcal N_{\mathbb Q},
$$

y por tanto

$$
b\sim_C a.
$$

**Transitividad.** Sean $a,b,c\in\mathcal C_{\mathbb Q}$ y supongamos

$$
a\sim_C b
\qquad\text{y}\qquad
b\sim_C c.
$$

Entonces

$$
a-b\in\mathcal N_{\mathbb Q},
\qquad
b-c\in\mathcal N_{\mathbb Q}.
$$

Por la estabilidad bajo suma de Proposición 9.2.3 — Estabilidad aditiva de las sucesiones nulas,

$$
(a-b)+(b-c)\in\mathcal N_{\mathbb Q}.
$$

Para todo $n\in\mathbb N$,

$$
\begin{aligned}
\bigl((a-b)+(b-c)\bigr)_n
&=(a_n-b_n)+(b_n-c_n)\\
&=a_n-c_n\\
&=(a-c)_n,
\end{aligned}
$$

por las leyes del grupo aditivo racional. El criterio término a término produce

$$
a-c=(a-b)+(b-c).
$$

Por consiguiente,

$$
a-c\in\mathcal N_{\mathbb Q},
$$

y entonces

$$
a\sim_C c.
$$

Hemos verificado reflexividad, simetría y transitividad. Por Definición 0.4.7 — Relación de equivalencia, $\sim_C$ es una relación de equivalencia sobre $\mathcal C_{\mathbb Q}$. ∎

> **Auditoría fundacional.** La prueba no selecciona representantes ni índices dependientes de infinitas precisiones. Utiliza únicamente identidades algebraicas término a término y la estabilidad de $\mathcal N_{\mathbb Q}$ ya demostrada. `choice-use: none`.

---

### Lo que hemos ganado

Ya no tenemos solamente una colección de sucesiones de Cauchy, sino una noción rigurosa de cuándo dos de ellas describen la misma posición asintótica:

$$
\boxed{
a\sim_C b
\iff
a-b\in\mathcal N_{\mathbb Q}.
}
$$

La relación está definida como un conjunto y ha sido demostrada equivalente en el sentido formal de Definición 0.4.7 — Relación de equivalencia. Por tanto, el siguiente objeto está ahora legitimado conjuntistamente:

$$
\mathcal C_{\mathbb Q}/{\sim_C}.
$$

Sólo en §9.4 daremos a ese cociente el nombre $\mathbb R_C$; hasta entonces no identificamos ninguna sucesión con su futura clase de equivalencia.

---
