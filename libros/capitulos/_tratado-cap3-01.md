## 3.1. Lemas enteros preparatorios {#sec-ta-3-1}

La construcción racional exige cancelar factores enteros no nulos y comparar desigualdades después de multiplicar por enteros positivos. Estas propiedades se siguen de la estructura obtenida en el capítulo anterior, pero todavía no han sido aisladas como resultados formales. Lo hacemos ahora.

### Lema 3.1.1 — Cancelación multiplicativa en $\mathbb Z$ {#ta-cancelacion-multiplicativa-enteros}

*Glosario: [cancelación multiplicativa](../otros/tratado-de-analisis-glosario.md#gl-cancelacion-multiplicativa)*

Sean $r,x,y\in\mathbb Z$. Si $r\neq0_{\mathbb Z}$ y

$$
rx=ry,
$$

entonces $x=y$.

**Demostración.**  
De $rx=ry$ obtenemos, sumando $-(ry)$,

$$
rx-ry=0_{\mathbb Z}.
$$

Por distributividad,

$$
r(x-y)=0_{\mathbb Z}.
$$

Como $\mathbb Z$ carece de divisores de cero por la [Proposición 2.8.3](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-ausencia-divisores-cero-enteros) y $r\neq0_{\mathbb Z}$, se sigue

$$
x-y=0_{\mathbb Z}.
$$

Sumando $y$ a ambos lados, $x=y$. ∎

### Lema 3.1.2 — Invariancia del orden entero por traslación {#ta-invariancia-orden-traslacion-enteros}

Para $x,y,z\in\mathbb Z$,

$$
\boxed{
x\leq_{\mathbb Z}y
\iff
x+z\leq_{\mathbb Z}y+z.
}
$$

**Demostración.**  
La implicación directa es la compatibilidad del orden con la suma demostrada en la [Proposición 2.9.4](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-orden-entero-compatible). Recíprocamente, si

$$
x+z\leq_{\mathbb Z}y+z,
$$

sumamos $-z$ a ambos miembros mediante la misma compatibilidad:

$$
(x+z)+(-z)\leq_{\mathbb Z}(y+z)+(-z).
$$

Las leyes del grupo aditivo reducen esta desigualdad a $x\leq_{\mathbb Z}y$. ∎

### Lema 3.1.3 — Escalamiento por un entero positivo {#ta-escalamiento-entero-positivo}

Sean $x,y,r\in\mathbb Z$ con

$$
0_{\mathbb Z}<_{\mathbb Z}r.
$$

Entonces

$$
\boxed{
x\leq_{\mathbb Z}y
\iff
xr\leq_{\mathbb Z}yr.
}
$$

**Demostración.**  
Como $0_{\mathbb Z}<r$, tenemos $0_{\mathbb Z}\leq r$. La implicación directa es la compatibilidad multiplicativa del orden establecida en la [Proposición 2.9.4](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-orden-entero-compatible).

Supongamos ahora $xr\leq yr$. Por totalidad del orden entero, demostrada en el [Teorema 2.9.3](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-orden-entero-total), $x\leq y$ o $y\leq x$. Si $x\leq y$, terminamos. Si $y\leq x$, la compatibilidad multiplicativa da

$$
yr\leq xr.
$$

La antisimetría implica $xr=yr$. Por conmutatividad del producto entero, esta igualdad equivale a $rx=ry$. Como $r\neq0_{\mathbb Z}$, el Lema 3.1.1 permite cancelar el factor izquierdo $r$ y da $x=y$; en particular $x\leq y$. ∎

### Lema 3.1.4 — Producto de enteros positivos {#ta-producto-enteros-positivos}

Si

$$
0_{\mathbb Z}<x
\qquad\text{y}\qquad
0_{\mathbb Z}<y,
$$

entonces

$$
0_{\mathbb Z}<xy.
$$

**Demostración.**  
Primero verificamos la absorción del cero que utilizaremos en la comparación. Por distributividad,

$$
(0_{\mathbb Z}+0_{\mathbb Z})y
=
0_{\mathbb Z}y+0_{\mathbb Z}y.
$$

Como $0_{\mathbb Z}+0_{\mathbb Z}=0_{\mathbb Z}$, la cancelación aditiva en el grupo entero da

$$
0_{\mathbb Z}y=0_{\mathbb Z}.
$$

De $0\leq x$ y $0\leq y$, la compatibilidad multiplicativa del orden aplicada a $0\leq x$ y al factor no negativo $y$ produce

$$
0_{\mathbb Z}y\leq xy,
$$

y por la identidad recién demostrada obtenemos $0_{\mathbb Z}\leq xy$. Además $x\neq0$ y $y\neq0$, por lo que la [ausencia de divisores de cero](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-ausencia-divisores-cero-enteros) implica $xy\neq0$. Por la definición del orden estricto asociado, $0<xy$. ∎

### Notación 3.1.5 — Enteros no nulos {#ta-enteros-no-nulos}

*Glosario: [enteros no nulos](../otros/tratado-de-analisis-glosario.md#gl-enteros-no-nulos)*

Definimos

$$
\mathbb Z_{\neq0}
:=
\{b\in\mathbb Z:b\neq0_{\mathbb Z}\}.
$$

Este conjunto existe por separación.

### Definición 3.1.6 — Conjunto de representantes racionales {#ta-conjunto-representantes-racionales}

*Glosario: [conjunto de representantes racionales](../otros/tratado-de-analisis-glosario.md#gl-conjunto-representantes-racionales), [representante fraccionario](../otros/tratado-de-analisis-glosario.md#gl-representante-fraccionario)*

Definimos

$$
\boxed{
D_{\mathbb Q}
:=
\mathbb Z\times\mathbb Z_{\neq0}.
}
$$

Un elemento $(a,b)\in D_{\mathbb Q}$ se llamará representante fraccionario. El segundo componente es, por definición, no nulo.

### Notación 3.1.7 — Cuadrado {#ta-notacion-cuadrado}

Siempre que $x$ pertenezca a un sistema numérico en el que la multiplicación ya haya sido construida, escribiremos

$$
\boxed{x^2:=x\cdot x.}
$$

Esta convención introduce únicamente el cuadrado. Las potencias naturales generales se definirán más adelante, cuando su construcción sea necesaria; no se las presupone aquí.

---
