## 7.3. Verificación de que la unión es una cortadura {#sec-ta-7-3}

### Proposición 7.3.1 — Unión de una familia no vacía y acotada

Sea $\mathcal A\subseteq\mathbb R_D$ una familia no vacía y acotada superiormente. Entonces

$$
\boxed{U_D(\mathcal A)=\bigcup\mathcal A\in\mathbb R_D.}
$$

**Demostración.**

Verificamos las cuatro condiciones de una cortadura.

**No vaciedad.** Como $\mathcal A\neq\varnothing$, existe $\alpha_0\in\mathcal A$. Como $\alpha_0$ es una cortadura, existe $q\in\alpha_0$. Por definición de unión,

$$
q\in\bigcup\mathcal A.
$$

Así, $\bigcup\mathcal A\neq\varnothing$. Las dos instanciaciones existenciales son locales y finitas; no interviene Choice.

**Propiedad.** Como $\mathcal A$ está acotada superiormente, existe una cota superior $\beta\in\mathbb R_D$. Por Proposición 7.1.1 — Caracterización conjuntista de las cotas superiores,

$$
\alpha\subseteq\beta
\qquad(\alpha\in\mathcal A).
$$

Si $q\in\bigcup\mathcal A$, existe $\alpha\in\mathcal A$ con $q\in\alpha$, y por tanto $q\in\beta$. Luego

$$
\bigcup\mathcal A\subseteq\beta.
$$

Como $\beta$ es una cortadura, $\beta\neq\mathbb Q$. Si $\bigcup\mathcal A=\mathbb Q$, tendríamos $\mathbb Q\subseteq\beta$ y, como $\beta\subseteq\mathbb Q$, la extensionalidad daría $\beta=\mathbb Q$, contradicción. Por tanto,

$$
\bigcup\mathcal A\neq\mathbb Q.
$$

Éste es el único punto en el que se utiliza la hipótesis de acotación superior.

**Clausura inferior.** Sea $q\in\bigcup\mathcal A$ y $r<q$. Existe $\alpha\in\mathcal A$ tal que $q\in\alpha$. Como $\alpha$ es cerrada hacia abajo, $r\in\alpha$; luego $r\in\bigcup\mathcal A$.

**Ausencia de máximo.** Sea $q\in\bigcup\mathcal A$. Existe $\alpha\in\mathcal A$ con $q\in\alpha$. Como $\alpha$ no posee máximo, existe $r\in\alpha$ tal que $q<r$. Entonces $r\in\bigcup\mathcal A$.

Se cumplen las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind; por tanto,

$$
\boxed{\bigcup\mathcal A\in\mathbb R_D.}
$$

∎

Tres propiedades —no vaciedad, clausura inferior y ausencia de máximo— pasan localmente de las cortaduras a su unión. Sólo la propiedad $\bigcup\mathcal A\neq\mathbb Q$ exige información global, y esa información es exactamente la existencia de una cota superior.

> **Nota fundacional.** El primer paso de la prueba convierte clásicamente $\mathcal A\neq\varnothing$ en un testigo $\alpha_0\in\mathcal A$ y luego $\alpha_0\neq\varnothing$ en $q\in\alpha_0$. Con una familia **habitada** y cortaduras acompañadas de habitabilidad interior, el núcleo de la prueba es constructivamente robusto y sigue sin requerir Choice.
>
> La situación cambia si fortalecemos las cortaduras con **locatedness**. Aunque cada $\alpha\in\mathcal A$ sea localizada, una unión arbitraria $\bigcup\mathcal A$ no hereda automáticamente locatedness: para decidir positivamente, dados $p<q$, entre $p\in\bigcup\mathcal A$ y $q\notin\bigcup\mathcal A$ hace falta información uniforme adicional sobre la familia. Este hecho no afecta la completitud clásica demostrada aquí.
