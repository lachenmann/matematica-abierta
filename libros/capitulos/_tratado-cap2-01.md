## 2.1. Diferencias formales {#sec-ta-2-1}

Llamaremos **[diferencia formal](../otros/tratado-de-analisis-glosario.md#gl-diferencia-formal)** a un elemento de $\mathbb N\times\mathbb N$. Esta expresión es interpretativa: no introduce aún una operación de resta.

Si $(a,b)$ es una diferencia formal, pensaremos heurísticamente en ella como «$a-b$». Dos pares $(a,b)$ y $(c,d)$ deben representar el mismo valor cuando la igualdad

$$
a-b=c-d
$$

sería válida en una aritmética donde la resta ya existiera. Trasladando todos los términos a sumas, la condición se convierte en

$$
a+d=b+c.
$$

Ésta sí es una igualdad legítima en $\mathbb N$.

### Definición 2.1.1 — Relación de equivalencia entera {#ta-relacion-equivalencia-entera}

Sobre $\mathbb N\times\mathbb N$ definimos la **[relación de equivalencia entera](../otros/tratado-de-analisis-glosario.md#gl-relacion-equivalencia-entera)** $\sim_{\mathbb Z}$ por

$$
\boxed{
(a,b)\sim_{\mathbb Z}(c,d)
\iff
a+d=b+c.
}
$$

La notación $(a,b)$ es aquí una abreviatura tipográfica del par ordenado fijado en el capítulo fundacional.

La definición anterior produce la noción correcta de igualdad entre diferencias formales sólo si realmente es una relación de equivalencia. Esto debe demostrarse antes de formar el cociente.

### Proposición 2.1.2 — $\sim_{\mathbb Z}$ es una relación de equivalencia {#ta-equivalencia-entera}

La relación $\sim_{\mathbb Z}$ es reflexiva, simétrica y transitiva sobre $\mathbb N\times\mathbb N$.

**Demostración.**  
**Reflexividad.** Para $a,b\in\mathbb N$,

$$
a+b=b+a
$$

por conmutatividad de la suma natural. Luego

$$
(a,b)\sim_{\mathbb Z}(a,b).
$$

**Simetría.** Si

$$
(a,b)\sim_{\mathbb Z}(c,d),
$$

entonces

$$
a+d=b+c.
$$

Por simetría de la igualdad,

$$
c+b=d+a,
$$

después de reordenar las sumas mediante conmutatividad. Por tanto

$$
(c,d)\sim_{\mathbb Z}(a,b).
$$

**Transitividad.** Supongamos

$$
(a,b)\sim_{\mathbb Z}(c,d)
\qquad\text{y}\qquad
(c,d)\sim_{\mathbb Z}(e,f).
$$

Entonces

$$
a+d=b+c
$$

y

$$
c+f=d+e.
$$

Sumando ambas igualdades y reordenando por asociatividad y conmutatividad,

$$
(a+f)+(c+d)=(b+e)+(c+d).
$$

La cancelación aditiva en $\mathbb N$ da

$$
a+f=b+e.
$$

Por definición,

$$
(a,b)\sim_{\mathbb Z}(e,f).
$$

Así $\sim_{\mathbb Z}$ es una relación de equivalencia. ∎

La prueba merece una observación. En la transitividad no hemos escrito

$$
a-b=c-d=e-f,
$$

porque esas restas todavía no existen en el nivel objeto. Todo el argumento se realiza con las operaciones ya construidas en $\mathbb N$.

---

::: {.callout-note title="Publicación progresiva"}
Con §2.1 queda construida y verificada la relación que identifica pares de naturales que representan la misma diferencia formal. La siguiente entrega será **§2.2 — Construcción del conjunto $\mathbb Z$**, donde formaremos el cociente $(\mathbb N\times\mathbb N)/{\sim_{\mathbb Z}}$.
:::
