## 14.4. Series de términos no negativos {#sec-ta-14-4}

Para una serie arbitraria, una suma parcial puede aumentar o disminuir: el signo de $a_{n+1}$ decide la variación entre $s_n$ y $s_{n+1}$. La situación se simplifica si **todos los términos son no negativos**. En ese caso, sumar un término nuevo nunca reduce el total. La existencia de un límite deja entonces de depender de oscilaciones y se convierte en un problema de acotación.

Aquí «serie de términos no negativos» significa exactamente que $a:\mathbb N\to\mathbb R$ satisface $a_n\ge0$ para todo $n\in\mathbb N$. No creamos una nueva clase de objetos ni suponemos que la serie converja.

### Proposición 14.4.1 — Monotonía de las sumas parciales de una serie no negativa

Sea $a=(a_n)_{n\in\mathbb N}$ una sucesión real tal que $a_n\ge0$ para todo $n$. Entonces su sucesión de sumas parciales $s=\operatorname{PS}(a)$ es creciente en el sentido no estricto fijado en §13.7. Más precisamente,

$$
\boxed{0\le s_0\le s_n\le s_m\qquad(n\le m).}
$$

**Demostración.**

La definición recursiva Definición 14.1.1 — Sucesión de sumas parciales y serie numérica da $s_0=a_0\ge0$ y, para cada $j\in\mathbb N$,

$$
s_{j+1}=s_j+a_{j+1}\ge s_j,
$$

pues $a_{j+1}\ge0$ y la suma del cuerpo ordenado respeta el orden. No basta, sin embargo, con escribir esta desigualdad entre índices consecutivos: la definición de sucesión creciente exige comparar *cualquier par* $n\le m$.

Fijemos $n\in\mathbb N$ y probemos por inducción en $d\in\mathbb N$ que $s_n\le s_{n+d}$. Para $d=0$ tenemos $s_{n+0}=s_n$. Si $s_n\le s_{n+d}$, la asociatividad de la suma natural y la desigualdad anterior permiten concluir

$$
s_n\le s_{n+d}\le s_{(n+d)+1}=s_{n+(d+1)}.
$$

La inducción prueba la afirmación para todo $d$. Dados $n\le m$, por la definición del orden natural existe $d\in\mathbb N$ tal que $m=n+d$; por tanto, $s_n\le s_m$. En particular, como $0\le n$, se obtiene $0\le s_0\le s_n$ para cada índice. Es exactamente la monotonía requerida. ∎

> **Clave de lectura.** El signo de los términos controla la dirección de las sumas parciales, pero no garantiza por sí solo un límite: una sucesión creciente todavía puede carecer de cota superior.

---

### Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos

Sea $a=(a_n)_{n\in\mathbb N}$ una sucesión real con $a_n\ge0$ para todo $n$, y pongamos

$$
s=\operatorname{PS}(a),\qquad
S:=s[\mathbb N]=\left\{\sum_{k=0}^{n}a_k:n\in\mathbb N\right\}.
$$

El conjunto de valores $S\subseteq\mathbb R$ es no vacío, pues contiene $s_0$. Entonces las condiciones siguientes son equivalentes:

1. la serie $\sum_{k=0}^{\infty}a_k$ converge en $\mathbb R$;
2. $S$ está acotado superiormente, es decir, existe $M\in\mathbb R$ tal que $s_n\le M$ para todo $n\in\mathbb N$.

Cuando se cumplen, su suma es exactamente el supremo de las sumas parciales:

$$
\boxed{\sum_{k=0}^{\infty}a_k
=\lim_{n\to\infty}s_n
=\sup S.}
$$

**Demostración.**

La imagen $S=s[\mathbb N]$ existe por la teoría de imágenes de funciones ya desarrollada (Definición 0.6.9 — Imagen y preimagen); es un subconjunto de $\mathbb R$ y contiene $s_0$. Por Proposición 14.4.1 — Monotonía de las sumas parciales de una serie no negativa, $s$ es creciente.

**(1) implica (2).** Si la serie converge, la definición Definición 14.1.4 — Convergencia, divergencia y suma de una serie afirma que $s$ converge a un real. Toda sucesión real convergente es acotada por Teorema 13.4.5 — Toda sucesión real convergente es acotada; en particular, existe una cota superior $M$ para todos los $s_n$. Como todo elemento de $S$ es algún $s_n$, ese mismo $M$ acota superiormente $S$.

**(2) implica (1).** Si $S$ está acotado superiormente, la sucesión creciente $s$ está acotada superiormente. Aplicamos el teorema de convergencia monótona Teorema 13.7.3 — Teorema de convergencia monótona (1), que, usando la completitud real, garantiza tanto la existencia de $\sup S\in\mathbb R$ como

$$
s_n\longrightarrow\sup S.
$$

Por la definición de convergencia de una serie, ésta converge; la unicidad del límite y la convención de suma infinita identifican su valor con $\sup S$. ∎

> **Interpretación.** Una cota superior para *todas* las sumas parciales es suficiente; no hace falta adivinar la suma. Si no existe tal cota, la serie no puede converger a un real, pero **no** introducimos aquí $+\infty$ como supuesto valor de la serie. El ejemplo armónico de §14.2 muestra, además, que $a_n\to0$ puede coexistir con sumas parciales no acotadas.

> **Dependencias y fundamento.** La monotonía se deduce de la recursión y del orden, sin completitud. La implicación de convergencia a acotación usa sólo la acotación de sucesiones convergentes. La recíproca y la identificación con el supremo importan exactamente la completitud y la lógica clásica documentadas en Teorema 13.7.3 — Teorema de convergencia monótona. No se seleccionan elementos, cotas o índices mediante Choice ni se afirma computabilidad del supremo.

La convergencia queda así reducida, para términos no negativos, a una pregunta de orden. En §14.5 estudiaremos cómo usar cotas entre términos de **dos series distintas** para trasladar conclusiones de convergencia o divergencia: será el punto de partida de los criterios de comparación.

---
