## 6.1. Suma de cortaduras {#sec-ta-6-1}

### Lema 6.1.1 — Todo punto exterior domina una cortadura

Sean $\alpha\in\mathbb R_D$ y $u\in\mathbb Q$ tales que $u\notin\alpha$. Entonces, para todo $a\in\alpha$,

$$
\boxed{a<u.}
$$

**Demostración.**

Sea $a\in\alpha$. La tricotomía **decidible** de los racionales (Proposición 3.7.6 — Tricotomía decidible de los racionales) separa los casos $a<u$, $a=u$ y $u<a$.

La igualdad $a=u$ implicaría $u\in\alpha$. Si $u<a$, la clausura inferior de $\alpha$ aplicada a $a\in\alpha$ daría igualmente $u\in\alpha$. Ambos casos contradicen la hipótesis. Luego necesariamente

$$
a<u.
$$

∎

La fuerza constructiva del lema procede de que la comparación se realiza en $\mathbb Q$. La dificultad posterior no será comparar $a$ y $u$, sino obtener un testigo exterior $u\notin\alpha$ a partir de la condición negativa $\alpha\neq\mathbb Q$.

### Definición 6.1.2 — Conjunto suma de dos cortaduras

Para $\alpha,\beta\in\mathbb R_D$ definimos

$$
\boxed{
\Sigma_D(\alpha,\beta)
:=
\{q\in\mathbb Q:\exists a\in\alpha\;\exists b\in\beta\;(q=a+b)\}.
}
$$

Equivalentemente escribiremos $\Sigma_D(\alpha,\beta)=\{a+b:a\in\alpha,\ b\in\beta\}$, entendiendo esta notación como abreviatura de la fórmula acotada anterior. El conjunto existe por Separación sobre $\mathbb Q$.

### Proposición 6.1.3 — La suma de dos cortaduras es una cortadura

Para cualesquiera $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{\Sigma_D(\alpha,\beta)\in\mathbb R_D.}
$$

**Demostración.**

Verificamos las cuatro condiciones de una cortadura.

**No vaciedad.** Como $\alpha$ y $\beta$ son no vacías, existen $a\in\alpha$ y $b\in\beta$. Entonces $a+b\in\Sigma_D(\alpha,\beta)$.

**Propiedad.** Como $\alpha\neq\mathbb Q$ y $\beta\neq\mathbb Q$, existen $u\notin\alpha$ y $v\notin\beta$. Por Lema 6.1.1 — Todo punto exterior domina una cortadura, todo $a\in\alpha$ satisface $a<u$ y todo $b\in\beta$ satisface $b<v$. La compatibilidad del orden racional con la suma da

$$
a+b<u+b<u+v.
$$

Por tanto $u+v$ no puede ser de la forma $a+b$ con $a\in\alpha$ y $b\in\beta$. Así $u+v\notin\Sigma_D(\alpha,\beta)$ y el conjunto es propio.

**Clausura inferior.** Sea $x=a+b\in\Sigma_D(\alpha,\beta)$ y sea $r<x$. Trasladando por $-b$ obtenemos

$$
r-b<a.
$$

Como $a\in\alpha$, la clausura inferior da $r-b\in\alpha$. Además $b\in\beta$ y

$$
r=(r-b)+b.
$$

Luego $r\in\Sigma_D(\alpha,\beta)$.

**Ausencia de máximo.** Sea $x=a+b\in\Sigma_D(\alpha,\beta)$. Como $\alpha$ no tiene máximo, existe $a'\in\alpha$ tal que $a<a'$. Por compatibilidad con la suma,

$$
x=a+b<a'+b,
$$

y $a'+b\in\Sigma_D(\alpha,\beta)$. Así el conjunto no posee máximo.

Por Definición 5.1.1 — Cortadura de Dedekind y Definición 5.1.3 — Conjunto subyacente del modelo de Dedekind, $\Sigma_D(\alpha,\beta)\in\mathbb R_D$. Las elecciones efectuadas son finitas y locales; no interviene Choice. ∎

### Definición 6.1.4 — Adición de Dedekind

Sea

$$
G_{+_D}
:=
\{\langle\langle\alpha,\beta\rangle,\gamma\rangle\in(\mathbb R_D\times\mathbb R_D)\times\mathbb R_D:
\gamma=\Sigma_D(\alpha,\beta)\}.
$$

Por Separación existe $G_{+_D}$, y Proposición 6.1.3 — La suma de dos cortaduras es una cortadura garantiza para cada par $(\alpha,\beta)$ un único valor en $\mathbb R_D$. Definimos así

$$
\boxed{
+_D:\mathbb R_D\times\mathbb R_D\longrightarrow\mathbb R_D,
\qquad
\alpha+_D\beta:=\Sigma_D(\alpha,\beta).
}
$$

### Proposición 6.1.5 — La adición de Dedekind prolonga la suma racional

Para $p,q\in\mathbb Q$,

$$
\boxed{
\iota_D(p+q)=\iota_D(p)+_D\iota_D(q).
}
$$

Equivalentemente,

$$
\delta_{p+q}=\delta_p+_D\delta_q.
$$

**Demostración.**

Si $x\in\delta_p+_D\delta_q$, existen $a<p$ y $b<q$ tales que $x=a+b$. Entonces

$$
x=a+b<p+b<p+q,
$$

de modo que $x\in\delta_{p+q}$. Así

$$
\delta_p+_D\delta_q\subseteq\delta_{p+q}.
$$

Recíprocamente, sea $x<p+q$. Entonces $x-q<p$. Por densidad de $\mathbb Q$ existe $a$ con

$$
x-q<a<p.
$$

Pongamos $b:=x-a$. De $x-q<a$ se sigue $b<q$, y por construcción $x=a+b$. Por tanto $a\in\delta_p$, $b\in\delta_q$ y $x\in\delta_p+_D\delta_q$. Así

$$
\delta_{p+q}\subseteq\delta_p+_D\delta_q.
$$

La extensionalidad proporciona la igualdad. ∎
