## 17.1. Definición puntual y relación exacta con el límite {#sec-ta-17-1}

### Definición 17.1.1 — Continuidad relativa al dominio en un punto
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$. Diremos que **$f$ es continua en $a$ (relativamente a $D$)** si

$$
\boxed{\forall\varepsilon\in\mathbb R\ \bigl(\varepsilon>0\Rightarrow
\exists\delta\in\mathbb R\,[\delta>0\ \land
\forall x\in D\,(|x-a|<\delta\Rightarrow
|f(x)-f(a)|<\varepsilon)]\bigr).}
$$

Cuando se conoce el dominio escribiremos simplemente «$f$ es continua en $a$». En esta definición **no** se exige $a\in\operatorname{Acc}(D)$: sí se exige $a\in D$ para que $f(a)$ tenga sentido. Además, no aparece $0<|x-a|$: el punto central forma parte del cuantificador universal. Para $x=a$, la desigualdad requerida es $|f(a)-f(a)|=0<\varepsilon$, que se cumple automáticamente; los restantes puntos del dominio son los que permiten detectar una eventual falta de continuidad.

No basta hallar un $\delta$ adecuado para un solo argumento. El orden de los cuantificadores exige que, dada cada tolerancia $\varepsilon>0$, un mismo $\delta>0$ funcione para **todos** los $x\in D$ suficientemente próximos a $a$. No se ha impuesto que $D$ sea abierto ni que $a$ sea interior: un extremo de un intervalo puede ser un punto de continuidad relativo a ese intervalo.


### Proposición 17.1.2 — Caracterización mediante imágenes de bolas
Bajo las hipótesis de la definición anterior, $f$ es continua en $a$ si y sólo si

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0:\quad
f[D\cap B_\delta(a)]\subseteq B_\varepsilon(f(a)).}
$$

**Demostración.**
Supongamos continua la función en $a$ y fijemos $\varepsilon>0$. Sea $\delta>0$ el radio de la definición. Si $y\in f[D\cap B_\delta(a)]$, la definición de imagen proporciona un $x\in D\cap B_\delta(a)$ con $y=f(x)$. Por la definición de bola, $|x-a|<\delta$; la continuidad da $|y-f(a)|<\varepsilon$, esto es, $y\in B_\varepsilon(f(a))$. Se obtiene la inclusión.

Recíprocamente, fijemos $\varepsilon>0$ y tomemos el $\delta>0$ suministrado por la inclusión. Para cualquier $x\in D$ con $|x-a|<\delta$, tenemos $x\in D\cap B_\delta(a)$ y por tanto $f(x)\in B_\varepsilon(f(a))$, es decir, $|f(x)-f(a)|<\varepsilon$. Es exactamente la continuidad definida en §17.1.1. Las dos implicaciones utilizan puntos arbitrarios y un solo radio por tolerancia; no construyen una sucesión de elecciones. ∎

> **Comparación con §16.1.3.** Para el límite se utiliza la bola **perforada** $B_\delta(a)\setminus\{a\}$ y un valor candidato $L$. Para la continuidad se utiliza la bola completa intersectada con $D$, y la bola de llegada está centrada en el valor efectivo $f(a)$.


### Proposición 17.1.3 — Continuidad automática en un punto aislado
Sean $f:D\to\mathbb R$ y $a\in D$. Si $a\notin\operatorname{Acc}(D)$, entonces $f$ es continua en $a$, **cualquiera que sea el valor $f(a)$**.

**Demostración.**
La negación clásica del criterio de acumulación Lema §16.1.1 — Acumulación y aproximación perforada afirma que existe $r>0$ para el cual no hay $x\in D$ con $0<|x-a|<r$. Fijemos un $\varepsilon>0$ cualquiera y pongamos $\delta:=r$. Si $x\in D$ y $|x-a|<\delta$, entonces necesariamente $x=a$: si fuese distinto, la definitud del valor absoluto produciría $0<|x-a|<r$, contradicción. En consecuencia,

$$
|f(x)-f(a)|=|f(a)-f(a)|=0<\varepsilon.
$$

El mismo radio sirve para toda tolerancia positiva. No se afirma que la función posea un límite en $a$: el Capítulo 16 reserva esa relación para puntos de acumulación. ∎

**Ejemplo.** Sea $D=\{0,1\}$, subconjunto de $\mathbb R$, y $f:D\to\mathbb R$ una función cualquiera. El punto $0$ es aislado: basta $r=1/2$, pues el único otro elemento del dominio está a distancia $1$. Por la proposición, $f$ es continua en $0$ aunque se asignen valores arbitrarios a $f(0)$ y $f(1)$. Lo mismo vale en $1$. Este ejemplo muestra por qué no conviene introducir un límite vacuo en los puntos aislados para definir la continuidad.


### Teorema 17.1.4 — Continuidad y límite en un punto de acumulación
Sean $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Entonces

$$
\boxed{f\text{ es continua en }a
\iff \lim_{\substack{x\to a\\x\in D}}f(x)=f(a).}
$$

La condición $a\in D$ hace legítimo escribir $f(a)$; la acumulación hace legítima y no vacua la relación de límite. No basta que el límite finito exista: debe coincidir con el valor efectivo de la función.

**Demostración.**
**Continuidad $\Rightarrow$ límite.** Fijemos $\varepsilon>0$. Por continuidad existe $\delta>0$ tal que $x\in D$ y $|x-a|<\delta$ implican $|f(x)-f(a)|<\varepsilon$. En particular la desigualdad se cumple para los $x\in D$ que satisfacen la condición más restrictiva $0<|x-a|<\delta$. Junto con $a\in\operatorname{Acc}(D)$, esto prueba la relación definitoria de límite con candidato $f(a)$.

**Límite $\Rightarrow$ continuidad.** Supongamos $\lim_{\substack{x\to a\\x\in D}}f(x)=f(a)$ y fijemos $\varepsilon>0$. Por la definición del límite existe $\delta>0$ tal que, para todo $x\in D$ con $0<|x-a|<\delta$, se cumple $|f(x)-f(a)|<\varepsilon$. Consideremos ahora cualquier $x\in D$ con $|x-a|<\delta$. Si $x\ne a$, la desigualdad anterior se aplica. Si $x=a$, obtenemos directamente $|f(a)-f(a)|=0<\varepsilon$. Se han cubierto todos los elementos del dominio comprendidos en la bola completa; la misma $\delta$ acredita continuidad en $a$. ∎

**Contraejemplo: existencia del límite sin continuidad.** Sea $D=\mathbb R$ y definamos

$$
f(x)=\begin{cases}1,&x=0,\\0,&x\ne0.\end{cases}
$$

El origen es punto de acumulación de $D$, y $\lim_{x\to0}f(x)=0$: para todo $\varepsilon>0$ basta $\delta=1$, ya que en la bola perforada se tiene $|f(x)-0|=0<\varepsilon$. Sin embargo $f(0)=1$, y el teorema demuestra que $f$ no es continua en $0$. Directamente, para $\varepsilon=1/2$ y cualquier $\delta>0$, el punto $x=\delta/2\ne0$ satisface $|x|<\delta$ pero $|f(x)-f(0)|=1\not<1/2$. Sólo se necesita un testigo explícito por radio, no una sucesión de selecciones.


### Corolario 17.1.5 — Caracterización completa sobre dominios arbitrarios
Para una función $f:D\to\mathbb R$ y un punto $a\in D$, la continuidad en $a$ se caracteriza por los siguientes casos exhaustivos:

- Si $a\notin\operatorname{Acc}(D)$, $f$ es continua en $a$ sin ninguna condición adicional sobre los valores de $f$.
- Si $a\in\operatorname{Acc}(D)$, $f$ es continua en $a$ si y sólo si $\lim_{\substack{x\to a\\x\in D}}f(x)=f(a)$.

**Demostración.**
Por la lógica clásica del contrato fundacional, $a$ pertenece a $\operatorname{Acc}(D)$ o no pertenece. En el primer caso aplicamos las dos implicaciones del Teorema 17.1.4; en el segundo, la Proposición 17.1.3. No se escribe ningún límite fuera de la rama en que la acumulación lo hace legítimo. ∎

**Síntesis.** Continuidad no significa simplemente «existencia de límite» para cualquier dominio. Exige siempre que el valor $f(a)$ esté definido; en un punto de acumulación, exige además que coincida con el límite perforado. En un punto aislado, en cambio, la propia definición $\varepsilon$–$\delta$ resulta satisfecha sin imponer un supuesto valor límite. La próxima sección estudiará cómo se comporta esta propiedad sobre sucesiones que **sí pueden alcanzar $a$**, distinguiendo la dirección incondicional del criterio y la necesidad eventual de hipótesis fundacionales para la recíproca en dominios arbitrarios.
