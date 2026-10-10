## 20.4. Teorema del valor medio de Cauchy {#sec-ta-20-4}

Lagrange relaciona el incremento de una función con el incremento del argumento. Ahora compararemos dos funciones que comparten intervalo de definición. El resultado no debe introducir un cociente de derivadas antes de saber que su denominador es distinto de cero. Por eso comenzaremos con una igualdad de productos cruzados, válida incluso cuando alguna función es constante.

La estrategia es formar una combinación lineal de las dos funciones cuyos valores en los extremos coincidan. Los coeficientes serán sus incrementos sobre el intervalo; éstos son números reales determinados por los datos y no requieren ninguna división. Rolle proporcionará entonces la identidad buscada.

### Lema 20.4.1 — Combinación auxiliar con incrementos cruzados
Sean $a,b\in\mathbb R$, $a<b$, $I:=[a,b]$ y $f,g:I\to\mathbb R$ dos funciones. Denotemos, sólo dentro de esta construcción,

$$
\Delta_f:=f(b)-f(a),\qquad \Delta_g:=g(b)-g(a),
$$

y formemos la función $H:I\to\mathbb R$ mediante operaciones puntuales:

$$
\boxed{H(x):=\Delta_g f(x)-\Delta_f g(x)\qquad(x\in I).}
$$

Entonces:

1. $H(a)=H(b)$, sin suponer que $\Delta_f$ o $\Delta_g$ sean no nulos.
2. Si $f$ y $g$ son continuas en todo $I$, también lo es $H$.
3. Si $c\in(a,b)$ y ambas funciones son derivables en $c$ relativamente a $I$, entonces $H$ es derivable allí y

$$
\boxed{H'(c)=\Delta_g f'(c)-\Delta_f g'(c).}
$$

**Demostración.**
Los valores extremos están definidos porque $a,b\in I$ y las dos funciones tienen codominio $\mathbb R$. Sus diferencias $\Delta_f,\Delta_g$ son reales, incluidos los casos en que valen cero. Por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales existen las funciones tipadas $\Delta_g f:I\to\mathbb R$ y $\Delta_f g:I\to\mathbb R$, así como su diferencia $H:I\to\mathbb R$. Concretamente, el grafo de $H$ es el subconjunto de $I\times\mathbb R$ determinado por la igualdad funcional del enunciado; existe por Separación y asigna un único valor real a cada $x\in I$. No ampliamos ni cambiamos el dominio de ninguna función.

Por distributividad y conmutatividad del cuerpo real,

$$
\begin{aligned}
H(b)-H(a)
&=\Delta_g\,[f(b)-f(a)]-\Delta_f\,[g(b)-g(a)]\\
&=\Delta_g\Delta_f-\Delta_f\Delta_g=0.
\end{aligned}
$$

Por cancelación aditiva, $H(a)=H(b)$. No hemos afirmado que cada uno de esos dos valores sea cero: sólo necesitamos su igualdad para Rolle.

Si $f$ y $g$ son continuas en todos los puntos de $I$, Corolario §17.4.6 — Clausura global, restricciones y cocientes conserva la continuidad bajo multiplicación por escalares reales fijos y bajo diferencia de funciones con igual dominio y codominio. Aplicándolo dos veces a los coeficientes $\Delta_g$ y $\Delta_f$, obtenemos continuidad de $H$ en todo $I$, incluidos ambos extremos.

Sea finalmente $c\in(a,b)$ un punto donde ambas funciones sean derivables. El corolario Corolario §19.8.5 — Extremos e interior de un intervalo cerrado no degenerado garantiza $c\in\operatorname{Acc}(I)$ y legitima las derivadas relativas. La regla Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias, aplicada primero a cada múltiplo escalar y después a la diferencia, da

$$
H'(c)=(\Delta_g f)'(c)-(\Delta_f g)'(c)
=\Delta_g f'(c)-\Delta_f g'(c).
$$

Los coeficientes se fijaron antes de derivar: dependen de los valores de borde, no del argumento variable $x$. Se han definido objetos mediante fórmulas unívocas, sin escoger testigos de una familia. $\square$

**Lectura de la construcción.** Los dos incrementos cumplen el papel de coeficientes cruzados: al evaluar la diferencia de los valores de $H$ en los extremos, los productos se cancelan exactamente. Esta es la reducción a Rolle que se necesita, sin dividir por un incremento ni por una derivada.

### Teorema 20.4.2 — Teorema del valor medio de Cauchy, forma sin cocientes
Sean $a,b\in\mathbb R$ con $a<b$ y dos funciones $f,g:[a,b]\to\mathbb R$. Supongamos que ambas son continuas en cada punto de $[a,b]$ y derivables en cada punto de $(a,b)$, siempre relativamente a su dominio $[a,b]$. Entonces existe al menos un $c\in(a,b)$ tal que

$$
\boxed{[f(b)-f(a)]\,g'(c)=[g(b)-g(a)]\,f'(c).}
\tag{20.4.1}
$$

No se exige $g(b)\ne g(a)$ ni $g'(x)\ne0$. Si esos números se anulan, la expresión (20.4.1) sigue estando definida y el enunciado continúa siendo verdadero.

**Demostración.**
Pongamos $I=[a,b]$ y tomemos los dos incrementos $\Delta_f,\Delta_g$ y la función tipada $H:I\to\mathbb R$ del lema Lema §20.4.1 — Combinación auxiliar con incrementos cruzados. La primera conclusión de ese lema da $H(a)=H(b)$. Por continuidad de $f$ y $g$ en todo $I$, la segunda prueba que $H$ también es continua allí. Para cada $x\in(a,b)$, la derivabilidad de ambas funciones y la tercera conclusión del lema garantizan que $H$ es derivable en $x$ relativamente a $I$.

Quedan verificadas las tres hipótesis de Rolle Teorema §20.2.2 — Teorema de Rolle para la función $H:I\to\mathbb R$, no para $f$ ni para $g$ por separado. Existe entonces un $c\in(a,b)$ con $H'(c)=0$. La fórmula de derivación ya demostrada proporciona

$$
0=H'(c)=\Delta_g f'(c)-\Delta_f g'(c).
$$

Tras sumar $\Delta_f g'(c)$ a ambos miembros,

$$
\Delta_g f'(c)=\Delta_f g'(c),
$$

que es precisamente (20.4.1), por simetría de la igualdad. En ningún paso se ha dividido por alguno de los incrementos o de las derivadas. Se ha instanciado una única existencia de Rolle para una función explícitamente determinada; no se define una selección de puntos $c$ dependiente de todos los pares de funciones. $\square$

**Interpretación y recuperación de Lagrange.** Cauchy compara dos variaciones sobre un mismo intervalo. Si tomamos $g:[a,b]\to\mathbb R$ como la restricción de la identidad real, entonces $g(b)-g(a)=b-a$ y $g'(c)=1$ por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática y la regla de restricción Proposición §19.5.2 — Restricción de una función derivable. La igualdad (20.4.1) se convierte exactamente en $f(b)-f(a)=(b-a)f'(c)$, forma ya demostrada de Lagrange. Esta observación no se utiliza para probar Cauchy y no reabre aquel resultado.

### Corolario 20.4.3 — Forma de cocientes bajo denominadores demostrablemente no nulos
Bajo las hipótesis de Teorema §20.4.2 — Teorema del valor medio de Cauchy, forma sin cocientes, supongamos además que

$$
\forall x\in(a,b),\qquad g'(x)\ne0.
\tag{20.4.2}
$$

Entonces $g(b)\ne g(a)$ y existe un $c\in(a,b)$ con $g'(c)\ne0$ para el cual todos los cocientes siguientes están definidos y

$$
\boxed{\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}.}
\tag{20.4.3}
$$

**Demostración.**
**Primero verificamos el incremento del denominador.** Supongamos, buscando contradicción, que $g(b)=g(a)$. Como $g:[a,b]\to\mathbb R$ es continua en todo el intervalo y derivable en su interior, Rolle Teorema §20.2.2 — Teorema de Rolle daría un punto $d\in(a,b)$ con $g'(d)=0$. Pero (20.4.2) aplicado a ese $d$ afirma $g'(d)\ne0$. La contradicción demuestra

$$
\Delta_g:=g(b)-g(a)\ne0.
$$

**Ahora obtenemos el punto común.** El teorema de Cauchy Teorema §20.4.2 — Teorema del valor medio de Cauchy, forma sin cocientes proporciona un $c\in(a,b)$ tal que, escribiendo $\Delta_f:=f(b)-f(a)$,

$$
\Delta_f g'(c)=\Delta_g f'(c).
$$

La hipótesis (20.4.2) implica $g'(c)\ne0$. Así, ambos denominadores de (20.4.3) son no nulos. Podemos dividir la igualdad anterior por el producto real no nulo $\Delta_g g'(c)$ y obtenemos exactamente

$$
\frac{\Delta_f}{\Delta_g}=\frac{f'(c)}{g'(c)}.
$$

La prueba emplea una instancia de Rolle para excluir un incremento nulo y una instancia de Cauchy para obtener el punto requerido. Son dos testigos existenciales para un par de funciones ya fijado; no aparece Choice ni se atribuye al teorema principal una condición adicional que no necesita. $\square$

**Por qué no debe confundirse el corolario con el teorema.** Si $g$ es constante, entonces $g(b)-g(a)=0$ y $g'(x)=0$ en los puntos interiores. La igualdad (20.4.1) conserva sentido y se cumple, pero ambos cocientes de (20.4.3) quedan sin definir. El requisito de no anulación de $g'$ pertenece únicamente a esta forma dividida.

**Transición.** El teorema de Cauchy ha quedado demostrado en su forma general y en su forma de cocientes bajo hipótesis explícitas. En §20.5 comenzarán las consecuencias de signo: aplicaremos el valor medio de Lagrange a subintervalos para relacionar el signo de la derivada con la monotonía. Ni esos criterios ni las futuras estimaciones Lipschitz se han utilizado para justificar las demostraciones anteriores. La sección §20.4 queda estabilizada como unidad humana; el capítulo continúa abierto y no se abre un nuevo checkpoint Lean.
