## 13.0. De la construcción de los reales al análisis sobre los reales {#sec-ta-13-0}

La Parte I respondió una pregunta fundacional:

$$
\boxed{\text{¿qué son los números reales y por qué podemos trabajar con ellos?}}
$$

Construimos dos realizaciones distintas de la completación de $\mathbb Q$, demostramos su equivalencia mediante un isomorfismo explícito y probamos finalmente que toda completación ordenada de $\mathbb Q$ es única hasta único isomorfismo de cuerpos ordenados compatible con la copia racional.

El problema cambia ahora de naturaleza. Ya no necesitamos fabricar nuevos números. Disponemos de un cuerpo ordenado completo y queremos estudiar **procesos que evolucionan dentro de él**.

El primero de esos procesos será una sucesión.

En el Capítulo 8 las sucesiones aparecieron con una finalidad constructiva: una sucesión racional servía como nombre aproximativo a partir del cual podía construirse el modelo de Cauchy. Aquí la dirección se invierte. Los reales ya están construidos; una sucesión real será un objeto del análisis realizado **sobre** ellos.

La transición es, por tanto,

$$
\boxed{
\text{sucesiones para construir }\mathbb R
\quad\longrightarrow\quad
\text{sucesiones dentro de }\mathbb R.
}
$$

Esta diferencia impide simplemente declarar que el Capítulo 13 es una repetición del Capítulo 8. Una sucesión racional tiene codominio $\mathbb Q$; una sucesión real tendrá codominio $\mathbb R$. Además, la completitud que faltaba en el Capítulo 8 está ahora disponible y se convertirá en una herramienta matemática central: permitirá transformar ciertas formas de control —monotonía y acotación, o la condición de Cauchy— en existencia de límites reales.

Conforme a §12.9, durante la Parte II fijamos una realización de trabajo de la completación ordenada de $\mathbb Q$ y la denotamos por

$$
\mathbb R.
$$

Podemos tomar explícitamente como realización el modelo de Dedekind ya construido; ningún argumento de este capítulo utilizará, sin embargo, la codificación de sus elementos como cortaduras. Todo resultado formulado exclusivamente en términos de la estructura de cuerpo ordenado completo se transporta a cualquier otra realización por el único isomorfismo compatible con la copia racional.

Esta fijación no introduce una nueva identificación conjuntista:

$$
\mathbb R_D\neq\mathbb R_C
$$

como conjuntos en las realizaciones construidas. La letra $\mathbb R$ designa desde aquí una realización de la estructura cuya unicidad fue demostrada en Teorema 12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$.

El objetivo del capítulo es construir gradualmente la cadena

$$
\boxed{
\text{sucesión}
\longrightarrow
\text{convergencia}
\longrightarrow
\text{monotonía y completitud}
\longrightarrow
\text{Cauchy}
\longrightarrow
\text{subsucesiones}
\longrightarrow
\text{Bolzano--Weierstrass}.
}
$$

Comenzamos por el objeto más elemental, antes de atribuirle cualquier comportamiento asintótico.
