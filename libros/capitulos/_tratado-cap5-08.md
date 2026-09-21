## 5.8. Hacia la aritmética de las cortaduras {#sec-ta-5-8}

Hemos construido un conjunto totalmente ordenado que contiene una copia ordenada propia de $\mathbb Q$. Pero un sistema numérico requiere más que orden.

El problema del próximo capítulo será dotar a las cortaduras de operaciones algebraicas.

No diremos simplemente que debemos “transportar” la suma y el producto racionales. Los elementos de

$$
\mathbb R_D\setminus\iota_D[\mathbb Q]
$$

no proceden de racionales. Debemos construir operaciones directamente sobre las cortaduras y demostrar después que, cuando se restringen a la copia racional, coinciden con las operaciones ya conocidas.

Para la suma, la intuición procede de los racionales

$$
a+b,
\qquad
a\in\alpha,
\quad
b\in\beta.
$$

Pero una fórmula sugerente no será suficiente. Habrá que demostrar que el conjunto obtenido es nuevamente una cortadura: no vacío, propio, cerrado hacia abajo y sin máximo.

Después habrá que identificar el elemento que desempeña el papel de cero y construir, para cada cortadura $\alpha$, una cortadura opuesta. Este último paso requerirá especial cuidado: invertir simplemente el signo de todos los elementos de una cortadura no produce automáticamente un lado inferior sin máximo.

Una vez construida la estructura aditiva, abordaremos la multiplicación. También allí será necesario controlar los signos y probar que la operación permanece dentro de $\mathbb R_D$. Posteriormente construiremos los inversos multiplicativos de las cortaduras no nulas.

El objetivo no será solamente obtener las leyes abstractas de cuerpo. Deberemos comprobar que las nuevas operaciones prolongan exactamente las racionales:

$$
\boxed{
\iota_D(p+q)
=
\iota_D(p)+_D\iota_D(q),
}
$$

$$
\boxed{
\iota_D(pq)
=
\iota_D(p)\cdot_D\iota_D(q),
}
$$

así como

$$
\iota_D(0_{\mathbb Q})=0_D,
\qquad
\iota_D(1_{\mathbb Q})=1_D.
$$

Sólo entonces podremos promover $\iota_D$ desde una incrustación de órdenes a una incrustación de cuerpos ordenados.

La siguiente etapa será, por tanto,

$$
\boxed{
\text{Capítulo 6 — Aritmética de las cortaduras}.
}
$$

Su programa será

$$
\mathbb R_D
\longrightarrow
\text{suma}
\longrightarrow
\text{opuestos}
\longrightarrow
\text{grupo aditivo}
\longrightarrow
\text{producto}
\longrightarrow
\text{inversos}
\longrightarrow
\text{cuerpo ordenado}.
$$

Sólo después de completar esa estructura volveremos al problema que originó toda la construcción:

$$
\boxed{
\text{¿posee }\mathbb R_D\text{ la propiedad del supremo?}
}
$$

Esa pregunta será la prueba definitiva de que la construcción de Dedekind ha reparado la deficiencia que encontramos en $\mathbb Q$.
