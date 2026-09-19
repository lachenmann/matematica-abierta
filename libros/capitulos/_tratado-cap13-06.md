## 13.6. Orden de los límites y teorema del sándwich {#sec-ta-13-6}

Las operaciones algebraicas de la sección anterior permiten combinar límites. El orden plantea una cuestión distinta: si dos sucesiones están ordenadas término a término —al menos desde algún índice—, ¿qué relación puede sobrevivir entre sus límites?

Conviene separar dos direcciones lógicas que a primera vista parecen equivalentes, pero no lo son con la misma fuerza fundacional.

La dirección **estricta** es positiva: si dos límites satisfacen $\alpha<\beta$, entonces las sucesiones quedan finalmente separadas en ese mismo orden. La dirección **no estricta** parte, en cambio, de una desigualdad eventual $x_n\le y_n$ y concluye $\alpha\le\beta$; en nuestra interfaz abstracta de orden real, el núcleo negativo de esa prueba es constructivo, pero su conversión final a una desigualdad no estricta utiliza la lógica clásica ambiente.

Esta distinción será visible en las demostraciones.

---

### Proposición 13.6.1 — Límites estrictamente ordenados separan eventualmente las sucesiones

Sean $x=(x_n)$ e $y=(y_n)$ sucesiones reales tales que

$$
x_n\to\alpha,
\qquad
y_n\to\beta.
$$

Si

$$
\alpha<\beta,
$$

entonces

$$
\boxed{
x_n<y_n
\quad\text{eventualmente}.
}
$$

**Demostración.**

La desigualdad estricta $\alpha<\beta$ implica, por invariancia del orden estricto bajo traslación,

$$
0<\beta-\alpha.
$$

Definamos

$$
\delta:=\beta-\alpha.
$$

Entonces

$$
0<\delta.
$$

Como en la prueba de unicidad del límite, pongamos

$$
s:=1+1.
$$

De $0<1$ y la invariancia estricta por traslación obtenemos

$$
0<s.
$$

Por tanto $s^{-1}>0$. Definimos

$$
\eta:=\delta s^{-1}.
$$

La positividad del producto da

$$
0<\eta,
$$

y las leyes del cuerpo producen

$$
\eta+\eta=\delta.
$$

Aplicando la formulación por ventanas de Proposición 13.3.3 — Formulaciones equivalentes de la convergencia a la convergencia de $x$ y de $y$, valen eventualmente

$$
\alpha-\eta<x_n<\alpha+\eta
$$

y

$$
\beta-\eta<y_n<\beta+\eta.
$$

Por Proposición 13.2.5 — Reglas elementales de eventualidad (3) ambas propiedades valen simultáneamente en un mismo tramo final. Para todo índice de ese tramo,

$$
x_n<\alpha+\eta
$$

y

$$
\beta-\eta<y_n.
$$

Además,

$$
\begin{aligned}
\beta-\eta
&=\alpha+\delta-\eta\\
&=\alpha+(\eta+\eta)-\eta\\
&=\alpha+\eta.
\end{aligned}
$$

Por consiguiente,

$$
x_n<\alpha+\eta
=\beta-\eta<y_n.
$$

Por transitividad,

$$
x_n<y_n
$$

para todo índice suficientemente grande. ∎

> **Lectura geométrica.** Dos límites distintos poseen una separación positiva. Tomando como radio la mitad de esa separación, las ventanas centradas en $\alpha$ y $\beta$ dejan de solaparse. La eventualidad convierte esa separación geométrica en una desigualdad entre términos tardíos.

> **Nota fundacional.** No intervienen completitud, Choice ni lógica clásica sustantiva. El inverso $s^{-1}$ es el inverso ordinario de un real no nulo ya disponible en la estructura de cuerpo; no se está introduciendo todavía el recíproco de una sucesión.

---

### Teorema 13.6.2 — Preservación del orden en el paso al límite

Sean $x=(x_n)$ e $y=(y_n)$ sucesiones reales tales que

$$
x_n\to\alpha,
\qquad
y_n\to\beta.
$$

Si

$$
x_n\le y_n
\quad\text{eventualmente},
$$

entonces

$$
\boxed{
\alpha\le\beta.
}
$$

**Demostración.**

Comencemos por la parte que no necesita lógica clásica. Si se tuviera

$$
\beta<\alpha,
$$

la proposición Proposición 13.6.1 — Límites estrictamente ordenados separan eventualmente las sucesiones, aplicada a $y_n\to\beta$ y $x_n\to\alpha$, daría

$$
y_n<x_n
\quad\text{eventualmente}.
$$

Por hipótesis también vale eventualmente

$$
x_n\le y_n.
$$

Proposición 13.2.5 — Reglas elementales de eventualidad (3) permite pasar a un tramo final común en el que ambas desigualdades son verdaderas. Allí tendríamos

$$
y_n<x_n\le y_n,
$$

lo que contradice la irreflexividad del orden estricto. Hemos demostrado, por tanto, la afirmación constructivamente robusta

$$
\boxed{
\neg(\beta<\alpha).
}
$$

Falta convertir esta información negativa en la desigualdad no estricta deseada.

Supongamos

$$
\neg(\alpha\le\beta).
$$

Como el orden de $\mathbb R$ es total, debe cumplirse

$$
\beta\le\alpha.
$$

Además, $\beta=\alpha$ implicaría $\alpha\le\beta$, contradiciendo la suposición anterior. Luego

$$
\beta\ne\alpha,
$$

y por la definición del orden estricto,

$$
\beta<\alpha.
$$

Esto contradice la conclusión negativa ya obtenida. Así hemos probado

$$
\neg\neg(\alpha\le\beta).
$$

La lógica clásica ambiente permite eliminar la doble negación y concluir

$$
\alpha\le\beta.
$$

∎

> **Auditoría lógica.** El contenido cuantitativo de la prueba establece sin lógica clásica sustantiva que el orden eventual impide la desigualdad opuesta entre los límites: $\neg(\beta<\alpha)$. En la interfaz abstracta de cuerpo ordenado adoptada por el tratado no hemos identificado esa negación con $\alpha\le\beta$ por definición. El último paso usa, por tanto, eliminación clásica de doble negación. No se está suponiendo que el orden de $\mathbb R$ sea decidible.

Como casos particulares, si $x_n\to\alpha$ y $x_n\le c$ eventualmente, entonces

$$
\alpha\le c;
$$

y si $c\le x_n$ eventualmente, entonces

$$
c\le\alpha,
$$

pues la sucesión constante $\underline c$ converge a $c$.

La hipótesis no estricta sólo permite una conclusión no estricta: incluso cuando todos los términos satisfacen una cota, el límite puede situarse exactamente sobre ella.

---

### Proposición 13.6.3 — Estabilidad eventual del signo estricto

Sea $x=(x_n)$ una sucesión real con

$$
x_n\to\alpha.
$$

Entonces:

1. si $0<\alpha$, se tiene
   $$
   \boxed{
   0<x_n
   \quad\text{eventualmente};
   }
   $$
2. si $\alpha<0$, se tiene
   $$
   \boxed{
   x_n<0
   \quad\text{eventualmente}.
   }
   $$

**Demostración.**

La sucesión constante $\underline 0$ converge a $0$ por Proposición 13.3.4 — Las sucesiones constantes convergen a su valor.

Si $0<\alpha$, aplicamos Proposición 13.6.1 — Límites estrictamente ordenados separan eventualmente las sucesiones a

$$
\underline 0_n\to0
\qquad\text{y}\qquad
x_n\to\alpha.
$$

Como $0<\alpha$, obtenemos

$$
\underline 0_n<x_n
$$

eventualmente, es decir,

$$
0<x_n
$$

eventualmente.

Si $\alpha<0$, aplicamos la misma proposición en el orden inverso a

$$
x_n\to\alpha
\qquad\text{y}\qquad
\underline 0_n\to0.
$$

Resulta

$$
x_n<\underline 0_n=0
$$

eventualmente. ∎

> **Interpretación.** Un límite estrictamente positivo no permite que la sucesión siga visitando valores no positivos arbitrariamente lejos; un límite estrictamente negativo impone el comportamiento simétrico. El signo estricto del límite acaba dominando el signo de la cola.

---

### Corolario 13.6.4 — Un límite no nulo fuerza no anulación eventual

Sea $x=(x_n)$ una sucesión real. Si

$$
x_n\to\alpha
$$

y

$$
\alpha\ne0,
$$

entonces

$$
\boxed{
x_n\ne0
\quad\text{eventualmente}.
}
$$

**Demostración.**

Por totalidad del orden real,

$$
\alpha\le0
\qquad\text{o}\qquad
0\le\alpha.
$$

En el primer caso, $\alpha\ne0$ implica

$$
\alpha<0.
$$

Por Proposición 13.6.3 — Estabilidad eventual del signo estricto, la desigualdad

$$
x_n<0
$$

vale eventualmente. Todo término estrictamente negativo es distinto de cero; por estabilidad de la eventualidad bajo implicación, Proposición 13.2.5 — Reglas elementales de eventualidad (5), se sigue que

$$
x_n\ne0
$$

eventualmente.

En el segundo caso, de $\alpha\ne0$ obtenemos también $0\ne\alpha$, y por tanto

$$
0<\alpha.
$$

Proposición 13.6.3 — Estabilidad eventual del signo estricto da ahora

$$
0<x_n
$$

eventualmente, lo que nuevamente implica $x_n\ne0$ eventualmente. ∎

> **Puente hacia los cocientes.** Esta es exactamente la pieza que faltaba al final de §13.5: si el límite del denominador es no nulo, entonces el denominador es no nulo desde algún índice. Todavía no definimos aquí el recíproco de una sucesión; sólo hemos demostrado que, bajo la hipótesis correcta, la cola necesaria para hacerlo existe sin ninguna elección.

---

### Teorema 13.6.5 — Teorema del sándwich

Sean $x=(x_n)$, $y=(y_n)$ y $z=(z_n)$ sucesiones reales. Supongamos que

$$
x_n\to\ell,
\qquad
z_n\to\ell,
$$

y que

$$
x_n\le y_n
$$

y

$$
y_n\le z_n
$$

valen eventualmente. Entonces

$$
\boxed{
y_n\to\ell.
}
$$

**Demostración.**

Sea $\varepsilon>0$.

De $x_n\to\ell$ y Proposición 13.3.3 — Formulaciones equivalentes de la convergencia obtenemos que

$$
\ell-\varepsilon<x_n
$$

vale eventualmente. De $z_n\to\ell$ obtenemos que

$$
z_n<\ell+\varepsilon
$$

vale eventualmente.

Por hipótesis también son eventuales

$$
x_n\le y_n
$$

y

$$
y_n\le z_n.
$$

Aplicando repetidamente Proposición 13.2.5 — Reglas elementales de eventualidad (3), existe un único tramo final en el que las cuatro desigualdades valen simultáneamente. En todo índice de ese tramo,

$$
\ell-\varepsilon
< x_n
\le y_n
\le z_n
<\ell+\varepsilon.
$$

La transitividad del orden, junto con la definición del orden estricto asociado, da

$$
\ell-\varepsilon<y_n<\ell+\varepsilon.
$$

Por tanto esa ventana alrededor de $\ell$ contiene eventualmente a $y_n$. Como $\varepsilon>0$ era arbitrario, la equivalencia Proposición 13.3.3 — Formulaciones equivalentes de la convergencia concluye

$$
y_n\to\ell.
$$

∎

> **Arquitectura de la prueba.** El teorema no calcula el error de $y_n$ directamente. Transfiere dos controles unilaterales desde las sucesiones exteriores:
>
> $$
> \boxed{
> \ell-\varepsilon<x_n\le y_n\le z_n<\ell+\varepsilon.
> }
> $$
>
> El límite común de las fronteras comprime así a la sucesión intermedia dentro de toda ventana prescrita.

> **Nota fundacional.** No se usa completitud, Choice ni lógica clásica sustantiva. El teorema del sándwich es una consecuencia directa del significado cuantificado de convergencia y de la transitividad del orden.

---

### Corolario 13.6.6 — Criterio absoluto de sándwich

Sean $x=(x_n)$ e $y=(y_n)$ sucesiones reales. Si

$$
x_n\to0
$$

y

$$
|y_n|\le x_n
\quad\text{eventualmente},
$$

entonces

$$
\boxed{
y_n\to0.
}
$$

**Demostración.**

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto (4), para todo $n$,

$$
-|y_n|\le y_n\le|y_n|.
$$

En todo índice en que

$$
|y_n|\le x_n,
$$

la inversión del orden al tomar opuestos da

$$
-x_n\le-|y_n|.
$$

Por transitividad,

$$
-x_n\le y_n\le x_n.
$$

La propiedad anterior vale eventualmente por Proposición 13.2.5 — Reglas elementales de eventualidad (5).

De $x_n\to0$, la proposición Proposición 13.5.2 — Límite del opuesto y de una diferencia da

$$
-x_n\to-0=0.
$$

Así, $y_n$ queda eventualmente comprimida entre dos sucesiones que convergen a $0$:

$$
-x_n\le y_n\le x_n.
$$

Aplicando Teorema 13.6.5 — Teorema del sándwich,

$$
y_n\to0.
$$

∎

Este corolario será una forma de uso muy frecuente del sándwich: para demostrar que una sucesión tiende a cero basta a menudo dominar su valor absoluto por otra sucesión que ya sabemos que tiende a cero.

---

La sección ha separado cuatro fenómenos que suelen comprimirse bajo la frase «el límite respeta el orden»:

$$
\boxed{
\begin{array}{c}
\alpha<\beta
\Longrightarrow
x_n<y_n\ \text{eventualmente},\\[4pt]
x_n\le y_n\ \text{eventualmente}
\Longrightarrow
\alpha\le\beta,\\[4pt]
\alpha\ne0
\Longrightarrow
x_n\ne0\ \text{eventualmente},\\[4pt]
x_n\le y_n\le z_n,
\quad x_n,z_n\to\ell
\Longrightarrow
y_n\to\ell.
\end{array}
}
$$

Ninguno de estos resultados utiliza todavía la completitud de $\mathbb R$. Hasta aquí hemos estudiado qué propiedades **debe** tener un límite, suponiendo que ya existe.

La situación cambia en la sección siguiente. Introduciremos sucesiones monótonas y preguntaremos cuándo el orden y la acotación bastan para **producir** un límite. Allí aparecerá por primera vez de manera esencial la completitud de $\mathbb R$ mediante supremos e ínfimos.
---
