## 2.0. Por qué necesitamos los enteros {#sec-ta-2-0}

Los números naturales nos permiten contar y sumar cantidades, y su multiplicación y su orden han sido construidos sin apelar a ningún sistema numérico anterior. Sin embargo, la aritmética obtenida en el capítulo precedente posee una limitación esencial: la sustracción no está siempre disponible.

Si $a,b\in\mathbb N$, una ecuación

$$
a+x=b
$$

tiene solución natural precisamente cuando $a\leq b$. En particular, no existe $x\in\mathbb N$ que satisfaga

$$
1+x=0.
$$

No queremos remediar esta deficiencia introduciendo símbolos nuevos de manera puramente formal y declarando después, por decreto, cómo deben operar. Queremos construir un nuevo conjunto cuyos elementos contengan a la aritmética natural mediante una incrustación canónica y en el cual toda ecuación aditiva

$$
x+y=z
$$

admita una solución única para $y$.

La idea heurística es familiar. Una diferencia como $a-b$ puede ser representada por el par $(a,b)$. Pero en este punto del tratado la expresión $a-b$ no tiene todavía significado general en $\mathbb N$. Por ello no la utilizaremos en ninguna definición. El par

$$
(a,b)\in\mathbb N\times\mathbb N
$$

será solamente un candidato a representar una diferencia formal.

Hay, sin embargo, un problema inmediato: distintos pares deben representar la misma diferencia. Intuitivamente,

$$
(5,2),\qquad(4,1),\qquad(3,0)
$$

deberían describir el mismo entero. La igualdad adecuada entre pares no puede expresarse recurriendo a la resta que precisamente estamos tratando de construir. Debe formularse únicamente con la suma natural ya disponible.

La construcción seguirá, por tanto, la cadena

$$
\mathbb N
\longrightarrow
\mathbb N\times\mathbb N
\longrightarrow
\text{diferencias formales}
\longrightarrow
\text{relación de equivalencia}
\longrightarrow
\mathbb Z
\longrightarrow
+,-,\cdot,\leq_{\mathbb Z}.
$$

En ningún momento utilizaremos el axioma de elección.

---
