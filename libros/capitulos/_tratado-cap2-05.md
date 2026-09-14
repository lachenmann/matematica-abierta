## 2.5. Multiplicación de enteros {#sec-ta-2-5}

La multiplicación debe ser compatible con la interpretación heurística de los pares como diferencias. Formalmente, la identidad

$$
(a-b)(c-d)
=
(ac+bd)-(ad+bc)
$$

sugiere la regla

$$
(a,b)(c,d):=(ac+bd,ad+bc).
$$

La fórmula utiliza sólo suma y producto de naturales, por lo que es legítima en nuestro nivel actual.

### Definición 2.5.1 — Producto de diferencias formales {#ta-producto-diferencias-formales}

Definimos

$$
\mu_{\mathbb Z}:
(\mathbb N\times\mathbb N)\times(\mathbb N\times\mathbb N)
\to
\mathbb N\times\mathbb N
$$

por

$$
\boxed{
\mu_{\mathbb Z}\bigl((a,b),(c,d)\bigr)
=
(ac+bd,\;ad+bc).
}
$$

### Proposición 2.5.2 — Compatibilidad del producto con $\sim_{\mathbb Z}$ {#ta-compatibilidad-producto-enteros}

Si

$$
(a,b)\sim_{\mathbb Z}(a',b')
$$

y

$$
(c,d)\sim_{\mathbb Z}(c',d'),
$$

entonces

$$
(ac+bd,ad+bc)
\sim_{\mathbb Z}
(a'c'+b'd',a'd'+b'c').
$$

**Demostración.**  
Demostraremos primero compatibilidad al modificar solamente el primer factor.

Supongamos

$$
(a,b)\sim_{\mathbb Z}(a',b'),
$$

de modo que

$$
a+b'=b+a'.
$$

Fijemos $(c,d)$. Debemos probar

$$
(ac+bd,ad+bc)
\sim_{\mathbb Z}
(a'c+b'd,a'd+b'c).
$$

Por definición de $\sim_{\mathbb Z}$ esto equivale a

$$
(ac+bd)+(a'd+b'c)
=
(ad+bc)+(a'c+b'd).
$$

El miembro izquierdo puede reagruparse como

$$
c(a+b')+d(b+a'),
$$

mientras que el derecho se reagrupa como

$$
d(a+b')+c(b+a').
$$

Como $a+b'=b+a'$, ambos miembros son iguales a

$$
c(a+b')+d(a+b')
$$

salvo el orden de los sumandos. Por conmutatividad de la suma, son iguales. Así el producto es compatible con cambio de representante en el primer factor.

La regla $\mu_{\mathbb Z}$ es simétrica en sus dos argumentos:

$$
\mu_{\mathbb Z}((a,b),(c,d))
=
\mu_{\mathbb Z}((c,d),(a,b)),
$$

pues el producto y la suma naturales son conmutativos. Por tanto la compatibilidad en el segundo factor se reduce al caso recién demostrado.

Partiendo ahora de

$$
(a,b)\sim_{\mathbb Z}(a',b')
$$

y

$$
(c,d)\sim_{\mathbb Z}(c',d'),
$$

obtenemos sucesivamente

$$
\mu_{\mathbb Z}((a,b),(c,d))
\sim_{\mathbb Z}
\mu_{\mathbb Z}((a',b'),(c,d))
$$

y

$$
\mu_{\mathbb Z}((a',b'),(c,d))
\sim_{\mathbb Z}
\mu_{\mathbb Z}((a',b'),(c',d')).
$$

La transitividad de $\sim_{\mathbb Z}$ concluye la prueba. ∎

### Definición 2.5.3 — Multiplicación en $\mathbb Z$ {#ta-multiplicacion-enteros}

*Glosario: [multiplicación entera](../otros/tratado-de-analisis-glosario.md#gl-multiplicacion-entera)*

Por el principio binario de definición sobre clases existe una única función

$$
\cdot_{\mathbb Z}:\mathbb Z\times\mathbb Z\to\mathbb Z
$$

tal que

$$
\boxed{
[(a,b)]\cdot_{\mathbb Z}[(c,d)]
=
[(ac+bd,\;ad+bc)].
}
$$

Cuando el contexto determine el sistema numérico, escribiremos $xy$ o $x\cdot y$.

### Notación 2.5.4 — Unidad entera {#ta-unidad-entera}

*Glosario: [unidad entera](../otros/tratado-de-analisis-glosario.md#gl-unidad-entera)*

Definimos

$$
\boxed{
1_{\mathbb Z}:=[(1,0)].
}
$$

De nuevo, $1_{\mathbb Z}$ y el natural $1$ no han sido identificados.

---

::: {.callout-note title="Publicación progresiva"}
Con §2.5 queda construida la multiplicación de enteros como una operación bien definida sobre clases, junto con su unidad $1_{\mathbb Z}$. La siguiente entrega será **§2.6 — Estructura algebraica**.
:::
