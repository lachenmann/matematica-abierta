## 22.4. Integración por partes {#sec-ta-22-4}

La regla de derivación de un producto, ya demostrada en §19.4, afirma que la derivada interior de $uv$ se descompone en $u'v+uv'$. Para convertir esa igualdad en una identidad de integrales necesitamos algo más: las expresiones que vamos a integrar han de ser funciones **definidas sobre todo el intervalo cerrado e integrables**. No confundiremos la existencia de las derivadas en $(a,b)$ con su prolongación automática a los extremos, ni deduciremos de la mera derivabilidad que una derivada es Riemann-integrable.

Formularemos primero la regla con dos funciones auxiliares $p,q:[a,b]\to\mathbb R$ cuyos valores interiores son las derivadas respectivas; sus valores extremos quedan especificados como parte de las funciones dadas. Después obtendremos la versión usual cuando tales prolongaciones son continuas y, finalmente, una fórmula para subintervalos y un cálculo elemental.

### Teorema 22.4.1 — Integración por partes bajo hipótesis exactas de integrabilidad
Sean $a<b$ y sean $u,v,p,q:[a,b]\to\mathbb R$ funciones tipadas. Supongamos que:

1. $u$ y $v$ son continuas en todo $[a,b]$ y derivables en todo $(a,b)$;
2. $u'(x)=p(x)$ y $v'(x)=q(x)$ para cada $x\in(a,b)$;
3. las funciones $A,B:[a,b]\to\mathbb R$, definidas por $A(t)=u(t)q(t)$ y $B(t)=p(t)v(t)$, son Riemann-integrables en $[a,b]$.

Entonces el producto $H:=uv:[a,b]\to\mathbb R$ es continuo en el cerrado, derivable en el interior, y la integración por partes toma la forma

$$
\boxed{\int_a^b A(t)\,dt
=u(b)v(b)-u(a)v(a)-\int_a^b B(t)\,dt.}
\tag{22.4.1}
$$

Es decir, con las abreviaturas puntuales ya justificadas,

$$
\boxed{\int_a^b u(t)q(t)\,dt
=[uv]_a^b-\int_a^b p(t)v(t)\,dt,\qquad
[uv]_a^b:=u(b)v(b)-u(a)v(a).}
\tag{22.4.2}
$$

La expresión $[uv]_a^b$ es una abreviatura **local** para la diferencia explícita de los valores extremos de una función; no es una definición de integral ni autoriza invertir extremos. Se permite que $p$ y $q$ no sean continuas. La integrabilidad se exige a los *productos* $uq$ y $pv$, no necesariamente a cada factor por separado.

**Demostración.**
Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales garantiza que los productos puntuales $H=uv$, $A=uq$ y $B=pv$, así como la suma $G:=A+B$, son funciones reales con **el mismo dominio** $[a,b]$. Por estabilidad algebraica de la continuidad Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto, $H$ es continua en cada punto del cerrado, incluidos los extremos. Si $x\in(a,b)$, la regla del producto Teorema §19.4.3 — Regla de derivación del producto da

$$
H'(x)=u'(x)v(x)+u(x)v'(x)
=p(x)v(x)+u(x)q(x)=B(x)+A(x)=G(x).
\tag{22.4.3}
$$

La hipótesis tercera afirma la integrabilidad de $A$ y $B$. La clausura aditiva Teorema §21.5.4 — La suma de funciones integrables es integrable y su integral es aditiva prueba, **antes de escribir su integral**, que $G=A+B$ también es integrable y que

$$
\int_a^b G=\int_a^b A+\int_a^b B.
\tag{22.4.4}
$$

Por (22.4.3) y la continuidad de $H$ en el cerrado, $H$ es una primitiva de $G$ según Definición §22.3.1 — Primitiva sobre un intervalo cerrado. La regla de Newton–Leibniz Teorema §22.3.3 — Regla de Newton–Leibniz para integrandas integrables que admiten primitiva, aplicable porque $G$ es integrable, proporciona

$$
\int_a^b G=H(b)-H(a)=u(b)v(b)-u(a)v(a).
\tag{22.4.5}
$$

Igualando (22.4.4) y (22.4.5), y restando en el cuerpo real el término $\int_a^b B$, obtenemos (22.4.1). La fórmula (22.4.2) es solamente su reescritura. Todas las integrales tienen extremos ordenados y funciones tipadas ya demostradas integrables. No se han presupuesto derivadas en $a$ ni en $b$, ni seleccionado puntos o aproximaciones mediante elección. $\square$

**Lectura deductiva.** La prueba tiene tres eslabones distintos: *regla del producto* $\Rightarrow$ *primitiva del sumando* $\Rightarrow$ *Newton–Leibniz y linealidad*. Si se suprime la integrabilidad de las expresiones $uq$ y $pv$, el segundo eslabón puede escribirse formalmente como una derivada, pero el tercero carece de justificación.

### Corolario 22.4.2 — Versión para derivadas con prolongaciones continuas
Sean $u,v:[a,b]\to\mathbb R$ continuas en el cerrado y derivables en $(a,b)$. Supongamos que existen funciones **continuas en el cerrado** $p,q:[a,b]\to\mathbb R$ tales que

$$
p(x)=u'(x),\qquad q(x)=v'(x)
\quad\text{para todo }x\in(a,b).
\tag{22.4.6}
$$

Entonces los productos $uq$ y $pv$ son integrables, y se cumple (22.4.1). Ésta es la formulación habitual de integración por partes para funciones continuamente derivables, entendiendo rigurosamente la derivada en los extremos por sus prolongaciones continuas, sin atribuirle allí una derivada bilateral.

**Demostración.**
Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales construye las funciones $A:=uq$ y $B:=pv$ sobre $[a,b]$. Cada factor es continuo en el cerrado, por lo que $A$ y $B$ son continuas allí por Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto. El corolario Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable demuestra su integrabilidad. Quedan verificadas todas las hipótesis de Teorema §22.4.1 — Integración por partes bajo hipótesis exactas de integrabilidad; su conclusión es precisamente (22.4.1). No hemos tomado límites laterales para fabricar nuevos valores de las derivadas: $p(a),p(b),q(a),q(b)$ forman parte de las funciones suministradas por la hipótesis. $\square$

### Corolario 22.4.3 — Integración por partes en subintervalos ordenados
Con las hipótesis del teorema Teorema §22.4.1 — Integración por partes bajo hipótesis exactas de integrabilidad, para todos los reales $r,s$ con $a\le r\le s\le b$ se cumple

$$
\boxed{\int_r^s(A\upharpoonright[r,s])
=u(s)v(s)-u(r)v(r)
-\int_r^s(B\upharpoonright[r,s]).}
\tag{22.4.7}
$$

**Demostración.**
Si $r=s$, ambas integrales son cero por la convención tipada Definición §21.6.5 — Integración en un intervalo degenerado y la diferencia de productos extremos también es cero. Si $r<s$, Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado proporciona la integrabilidad de las restricciones de $A$ y $B$ a $[r,s]$. Las restricciones de $u,v$ son continuas en el nuevo cerrado por Corolario §17.4.6 — Clausura global, restricciones y cocientes; son derivables en $(r,s)$ con derivadas dadas por las restricciones de $p,q$, respectivamente, según Proposición §19.5.2 — Restricción de una función derivable. La igualdad de funciones tipadas asegura que los productos puntuales de las restricciones coinciden con $A\upharpoonright[r,s]$ y $B\upharpoonright[r,s]$. Aplicar Teorema §22.4.1 — Integración por partes bajo hipótesis exactas de integrabilidad a estas cuatro funciones restringidas produce (22.4.7). No aparece en ningún paso una integral con extremo superior menor que el inferior. $\square$

### Proposición 22.4.4 — Primer cálculo por integración por partes: la función identidad
Para todo intervalo no degenerado $[a,b]$ y la función identidad tipada $\iota:[a,b]\to\mathbb R$, $\iota(t)=t$, se tiene

$$
\boxed{\int_a^b\iota(t)\,dt=\frac{b^2-a^2}{2}.}
\tag{22.4.8}
$$

**Demostración.**
Por Teorema §17.5.3 — Todo polinomio real es continuo en la recta, la identidad y las constantes son continuas en la recta; sus restricciones tipadas a $[a,b]$ son continuas por Corolario §17.4.6 — Clausura global, restricciones y cocientes. Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática prueba que la derivada de la identidad en cada punto interior vale $1_{\mathbb R}$; la función constante uno en el cerrado sirve de prolongación continua. En el corolario Corolario §22.4.2 — Versión para derivadas con prolongaciones continuas tomemos $u=v=\iota$ y $p=q=1$, donde $1$ significa aquí la **función constante** de valor $1_{\mathbb R}$. Los productos $A=u q$ y $B=pv$ coinciden, como funciones tipadas, con $\iota$. El corolario prueba su integrabilidad, también obtenible por Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable, y (22.4.1) queda

$$
I=b^2-a^2-I,\qquad I:=\int_a^b\iota.
$$

Sumando $I$ a ambos miembros y dividiendo por el real no nulo $2_{\mathbb R}$ resulta $I=(b^2-a^2)/2$, según (22.4.8). Si $a=b$, la convención de §21.6 da también ambos miembros iguales a cero, pero ese caso no requiere invocar un teorema formulado para $a<b$. $\square$

**Nota de fuentes.** Jacob y Evans, *A Course in Analysis*, vol. I (2015), cap. 26, proposición 26.5, p. 371, enuncian la regla para dos funciones continuamente derivables. Nuestra prueba usa esa formulación como contraste y explicita, antes de presentar el corolario clásico, la hipótesis más débil de integrabilidad de los dos productos; los argumentos deductivos proceden de resultados ya demostrados en §§19.4, 21.5 y 22.3.

**Transición.** Una integración por partes transforma la derivada de un producto en una identidad entre dos integrales. La siguiente unidad estudiará otra transformación: el cambio de variable. Allí habrá que controlar el dominio de la composición, el signo de la derivada de la función de cambio y, de manera especial, el orden de sus imágenes extremas antes de escribir una integral transformada.
