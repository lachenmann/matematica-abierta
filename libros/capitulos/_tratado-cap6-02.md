## 6.2. El cero de Dedekind {#sec-ta-6-2}

### Definición 6.2.1 — Cero de Dedekind

Definimos

$$
\boxed{
0_D:=\iota_D(0_{\mathbb Q})=\delta_{0_{\mathbb Q}}
=\{q\in\mathbb Q:q<0_{\mathbb Q}\}.
}
$$

El racional $0_{\mathbb Q}$ y la cortadura $0_D$ siguen siendo objetos distintos; la igualdad relevante es $\iota_D(0_{\mathbb Q})=0_D$.

### Proposición 6.2.2 — El cero de Dedekind es neutro para la suma

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{
\alpha+_D0_D=\alpha=0_D+_D\alpha.
}
$$

**Demostración.**

Demostremos primero $\alpha+_D0_D=\alpha$.

Si $x\in\alpha+_D0_D$, existen $a\in\alpha$ y $b<0$ tales que $x=a+b$. Entonces $x<a$, de modo que la clausura inferior de $\alpha$ da $x\in\alpha$. Así $\alpha+_D0_D\subseteq\alpha$.

Recíprocamente, sea $x\in\alpha$. Como $\alpha$ no tiene máximo, existe $a\in\alpha$ con $x<a$. Pongamos $b:=x-a$. Entonces $b<0$, por lo que $b\in0_D$, y $x=a+b$. Así $x\in\alpha+_D0_D$.

La igualdad $0_D+_D\alpha=\alpha$ se prueba del mismo modo, pero sin invocar conmutatividad: si $x=b+a$ con $b<0$ y $a\in\alpha$, entonces $x<a$; para la inclusión inversa, dado $x\in\alpha$ elegimos $a\in\alpha$ con $x<a$ y escribimos $x=(x-a)+a$ con $x-a\in0_D$.

Por doble inclusión obtenemos ambas identidades. ∎

### Corolario 6.2.3 — Compatibilidad del cero con la copia racional

Se tiene

$$
\boxed{\iota_D(0_{\mathbb Q})=0_D.}
$$

**Demostración.**

Es exactamente la definición de $0_D$. ∎
