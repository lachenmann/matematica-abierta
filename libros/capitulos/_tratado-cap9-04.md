## 9.4. Construcción del cociente {#sec-ta-9-4}

La relación de equivalencia ya está construida. Podemos efectuar ahora el paso que convierte los procesos racionales en nuevos objetos: **cada nuevo número será una clase completa de sucesiones de Cauchy mutuamente equivalentes**, no una sucesión privilegiada.

Esta distinción es estructural. Si $a\in\mathcal C_{\mathbb Q}$, entonces $a$ seguirá siendo una función $\mathbb N\to\mathbb Q$. El nuevo objeto asociado a $a$ será su clase de equivalencia. No identificaremos ambos niveles.

### Proposición 9.4.1 — Existencia del cociente de Cauchy

Existe el conjunto cociente

$$
\boxed{
\mathcal C_{\mathbb Q}/{\sim_C}.
}
$$

**Demostración.**

Por Proposición 9.3.2 — $\sim_C$ es una relación de equivalencia, $\sim_C$ es una relación de equivalencia sobre $\mathcal C_{\mathbb Q}$. El resultado general Proposición 0.5.8 — Existencia del cociente garantiza entonces la existencia del conjunto cociente asociado a una relación de equivalencia. Aplicándolo a

$$
A=\mathcal C_{\mathbb Q}
$$

y a la relación $\sim_C$, obtenemos la existencia de

$$
\mathcal C_{\mathbb Q}/{\sim_C}.
$$

No se selecciona un representante de cada clase: el cociente es el conjunto de las clases mismas. ∎

> **Auditoría fundacional.** La construcción heredada de Proposición 0.5.8 — Existencia del cociente utiliza conjunto potencia y separación. No requiere una función de elección ni una familia escogida de representantes.

---

### Definición 9.4.2 — El conjunto de los reales de Cauchy

Definimos el **conjunto de los reales de Cauchy** por

$$
\boxed{
\mathbb R_C
:=
\mathcal C_{\mathbb Q}/{\sim_C}.
}
$$

En este punto $\mathbb R_C$ es únicamente un conjunto. Todavía no hemos definido en él suma, producto, cero, unidad, opuestos, inversos ni orden, y por tanto **no** hemos demostrado aún que sea un cuerpo ordenado ni que sea completo.

El subíndice $C$ se conservará hasta comparar esta construcción con el modelo de Dedekind $\mathbb R_D$.

---

### Notación 9.4.3 — Clases de Cauchy

Para cada

$$
a\in\mathcal C_{\mathbb Q},
$$

denotaremos su clase de equivalencia respecto de $\sim_C$ por

$$
\boxed{
[a]_C.
}
$$

Es decir,

$$
[a]_C:=[a]_{\sim_C}.
$$

Por definición del cociente,

$$
[a]_C\in\mathbb R_C.
$$

Debe mantenerse permanentemente la distinción de tipos

$$
\boxed{
a\in\mathcal C_{\mathbb Q},
\qquad
[a]_C\in\mathbb R_C.
}
$$

Una sucesión es un representante; una clase es el nuevo objeto numérico. No se escribirá $a=[a]_C$.

---

### Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy

Se cumplen las siguientes propiedades:

1. para todo $a\in\mathcal C_{\mathbb Q}$,
   $$
   [a]_C\in\mathbb R_C;
   $$
2. para todo $x\in\mathbb R_C$, existe $a\in\mathcal C_{\mathbb Q}$ tal que
   $$
   x=[a]_C;
   $$
3. para cualesquiera $a,b\in\mathcal C_{\mathbb Q}$,
   $$
   \boxed{
   [a]_C=[b]_C
   \iff
   a\sim_C b
   \iff
   a-b\in\mathcal N_{\mathbb Q}.
   }
   $$

**Demostración.**

Las dos primeras afirmaciones son consecuencias directas de la definición general de cociente Definición 0.5.7 — Conjunto cociente, aplicada a

$$
\mathbb R_C
=
\mathcal C_{\mathbb Q}/{\sim_C}.
$$

En efecto, los elementos del cociente son precisamente las clases $[a]_C$ con $a\in\mathcal C_{\mathbb Q}$.

Para la tercera afirmación, sean $a,b\in\mathcal C_{\mathbb Q}$. El lema general de igualdad de clases Lema 0.5.3 — Igualdad de clases da

$$
[a]_C=[b]_C
\iff
a\sim_C b.
$$

Por la definición de la equivalencia de Cauchy Definición 9.3.1 — Equivalencia de Cauchy,

$$
a\sim_C b
\iff
a-b\in\mathcal N_{\mathbb Q}.
$$

Encadenando ambas equivalencias obtenemos

$$
[a]_C=[b]_C
\iff
a\sim_C b
\iff
a-b\in\mathcal N_{\mathbb Q}.
$$

Esto prueba las tres afirmaciones. ∎

> **Nota conceptual.** La igualdad en $\mathbb R_C$ no exige que dos representantes coincidan término a término. Exige exactamente que su diferencia sea asintóticamente nula. Ésta es la identificación que permitirá que procesos racionales distintos representen el mismo número.
>
> **Nota fundacional.** El criterio
> $$ [a]_C=[b]_C\iff a-b\in\mathcal N_{\mathbb Q} $$
> caracteriza exactamente la igualdad, pero no la vuelve decidible para representantes arbitrarios:
> $$ \boxed{\text{igualdad caracterizada}\neq\text{igualdad decidible en }\mathbb R_C.} $$

> **Auditoría de elección.** La afirmación de que cada clase posee un representante no requiere escoger simultáneamente uno para cada clase. Para un elemento fijo $x\in\mathbb R_C$, la propia definición del cociente proporciona un testigo local $a$ con $x=[a]_C$. No se construye ninguna sección global del cociente.

---

### Lo que hemos ganado

Por primera vez en la construcción de Cauchy disponemos de un conjunto que contiene los futuros números reales:

$$
\boxed{
\mathbb R_C
=
\mathcal C_{\mathbb Q}/{\sim_C}.
}
$$

Pero todavía no es legítimo tratarlo como cuerpo. Las operaciones término a término viven en $\mathcal C_{\mathbb Q}$; para trasladarlas a $\mathbb R_C$ debemos demostrar que el resultado **no depende del representante escogido**.

El criterio

$$
[a]_C=[b]_C
\iff
a-b\in\mathcal N_{\mathbb Q}
$$

será precisamente la herramienta de control. El siguiente problema es §9.5: demostrar que suma y producto término a término son compatibles con $\sim_C$ y, sólo después, hacerlas descender al cociente.

---
