## §14 — Qué puede y qué no puede decir el análisis dimensional {#fpm-i-02-s14}

### 14.1. Intuir: una herramienta poderosa puede ser peligrosa si olvidamos qué información contiene

A lo largo del capítulo hemos obtenido resultados sorprendentemente fuertes a partir de información aparentemente modesta.

Con dimensiones pudimos:

- detectar ecuaciones imposibles;
- inferir exponentes;
- construir escalas;
- comparar sistemas semejantes;
- reducir problemas con muchas variables;
- aislar parámetros adimensionales.

Esto puede producir una ilusión:

> si el análisis dimensional funciona tan bien, quizá pueda reemplazar la física detallada.

No puede.

La razón es estructural.

Las dimensiones conservan cierta información sobre las magnitudes, pero descartan otra.

Por eso el análisis dimensional es potente **porque comprime información**, y limitado **por la misma compresión**.

La pregunta final del capítulo será:

$$
\boxed{
\text{¿qué información conserva la dimensión y qué información pierde?}
}
$$

### 14.2. Lo que conserva

Una firma dimensional como

$$
\mathbf d(Q)
=
(\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta)
$$

conserva cómo una magnitud depende de las dimensiones base.

Esto permite reconstruir:

- cómo cambia su valor numérico al cambiar unidades base;
- qué productos y cocientes son dimensionalmente admisibles;
- qué términos pueden aparecer en una suma homogénea;
- qué combinaciones monomiales tienen dimensión uno;
- qué exponentes puede tener un ansatz monomial;
- qué parámetros pueden actuar como grupos de semejanza.

En este sentido, la dimensión conserva **estructura de escala**.

### 14.3. Lo que pierde

La misma firma no registra, por sí sola:

- el significado físico completo;
- el tipo de magnitud;
- si un objeto es escalar, vector o tensor;
- el signo;
- la dirección;
- coeficientes numéricos;
- condiciones iniciales;
- condiciones de frontera;
- geometría detallada;
- régimen de aproximación;
- causalidad;
- estabilidad;
- mecanismo dinámico;
- dependencia funcional entre parámetros adimensionales.

Dos cantidades pueden compartir dimensión y diferir en muchas de estas propiedades.

Por tanto:

$$
\boxed{
\text{misma dimensión}
\neq
\text{misma física}.
}
$$

### 14.4. Primera capacidad — detectar incompatibilidades

Si una ecuación propone:

$$
x=x_0+at,
$$

entonces:

$$
[x]=L,
$$

mientras:

$$
[at]=LT^{-1}.
$$

La ecuación falla.

Ésta es una conclusión fuerte:

$$
\boxed{
\text{una inhomogeneidad dimensional real invalida la expresión tal como está escrita}.
}
$$

No necesitamos medir el sistema.

No necesitamos resolver una ecuación diferencial.

No necesitamos conocer el valor de $a$.

La contradicción está en la estructura.

### 14.5. Primera limitación — pasar la auditoría no prueba la ley

Consideremos:

$$
E=Cmv^2.
$$

Para cualquier número puro $C$:

$$
[E]=ML^2T^{-2}.
$$

Por tanto, todas estas expresiones son dimensionalmente admisibles:

$$
E=\frac12mv^2,
$$

$$
E=mv^2,
$$

$$
E=17mv^2,
$$

$$
E=-3mv^2.
$$

Las dimensiones no distinguen entre ellas.

Así:

$$
\boxed{
\text{homogeneidad}
\text{ es necesaria en muchos modelos, pero no suficiente para la verdad física}.
}
$$

Esta fue la lección de el Principio 12.

### 14.6. Segunda capacidad — inferir escalas y exponentes

Si aceptamos un ansatz:

$$
Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},
$$

La Proposición 3 convierte la homogeneidad en un sistema lineal.

Por ejemplo, para el péndulo:

$$
P=C\ell^\alpha g^\beta,
$$

obtenemos:

$$
\alpha=\frac12,
$$

$$
\beta=-\frac12,
$$

y por tanto:

$$
P=C\sqrt{\frac{\ell}{g}}.
$$

La inferencia es rigurosa **dentro del ansatz declarado**.

### 14.7. Segunda limitación — la clase funcional fue una hipótesis

El análisis dimensional no demostró que el período fuera monomial.

Nosotros propusimos esa clase funcional.

Al incorporar el ángulo inicial:

$$
\varphi_0,
$$

Buckingham mostró que la forma más general es:

$$
P=
\sqrt{\frac{\ell}{g}}
\Psi(\varphi_0).
$$

La función:

$$
\Psi
$$

no es determinada por las dimensiones.

Por tanto:

$$
\boxed{
\text{restricción dimensional}
\neq
\text{determinación funcional completa}.
}
$$

### 14.8. Tercera capacidad — descubrir grupos adimensionales

Con $n$ variables y matriz dimensional de rango $r$, la Proposición 5 permite encontrar:

$$
n-r
$$

grupos independientes:

$$
\Pi_1,\ldots,\Pi_{n-r}.
$$

La relación física puede reorganizarse como:

$$
\Phi(\Pi_1,\ldots,\Pi_{n-r})=0.
$$

Esto puede reducir drásticamente un problema experimental o numérico.

En lugar de explorar cada variable dimensional por separado, podemos explorar el espacio reducido de parámetros adimensionales.

### 14.9. Tercera limitación — Buckingham no determina Φ

El teorema produce:

$$
\Phi(\Pi_1,\ldots,\Pi_k)=0,
$$

pero no suele producir:

$$
\Phi.
$$

La función restante puede contener casi toda la física interesante del problema.

En el arrastre viscoso obtuvimos:

$$
F
=
\rho v^2L^2
\Psi\left(
\frac{\rho vL}{\mu}
\right).
$$

El análisis dimensional identifica:

- la escala de fuerza;
- el parámetro adimensional;
- la reducción de variables.

No determina la función:

$$
\Psi.
$$

### 14.10. Cuarta capacidad — construir semejanza

Si dos sistemas preservan los mismos grupos adimensionales relevantes, pueden compararse dentro de una misma descripción reducida.

Por ejemplo, en un modelo viscoso:

$$
\frac{\rho_1v_1L_1}{\mu_1}
=
\frac{\rho_2v_2L_2}{\mu_2}.
$$

Esto permite diseñar:

- modelos a escala;
- comparaciones experimentales;
- familias de sistemas dinámicamente semejantes.

La semejanza es una de las aplicaciones más profundas del método.

### 14.11. Cuarta limitación — semejanza dimensional no significa identidad física

Dos sistemas pueden compartir ciertos grupos $\Pi$ y, sin embargo, diferir en:

- geometría no incluida en el modelo;
- condiciones de frontera;
- rugosidad;
- propiedades constitutivas;
- campos externos;
- mecanismos adicionales;
- transiciones de régimen;
- variables omitidas.

Por eso la afirmación correcta siempre tiene la forma:

$$
\boxed{
\text{semejanza respecto de un modelo declarado}.
}
$$

No:

$$
\boxed{
\text{identidad física absoluta}.
}
$$

### 14.12. Quinta capacidad — revelar variables omitidas indirectamente

El análisis dimensional no puede inventar una variable que no incluimos.

Pero puede producir señales de que el modelo es insuficiente.

Por ejemplo, si experimentos realizados con la misma combinación dimensional predicha muestran comportamientos sistemáticamente diferentes, debemos preguntar si falta un parámetro.

La discrepancia puede sugerir:

- una viscosidad omitida;
- una longitud característica adicional;
- temperatura;
- elasticidad;
- una condición geométrica;
- otro mecanismo físico.

Así, el fracaso de una reducción dimensional puede funcionar como herramienta diagnóstica.

### 14.13. Quinta limitación — ninguna inferencia formal recupera una premisa ausente

Este punto merece quedar como principio final del capítulo.

::: {.ma-block .ma-metodo #fpm-i-02-mp26}
**Principio 26 — Ninguna conclusión dimensional puede exceder las premisas del modelo**
El análisis dimensional puede deducir consecuencias rigurosas de una lista de magnitudes, dimensiones e hipótesis de invariancia, pero no puede establecer por sí solo la corrección física de esas premisas ni recuperar variables, mecanismos o regímenes que el modelo haya omitido.
:::

Podemos escribir:

$$
\boxed{
\text{premisas incompletas}
+
\text{álgebra correcta}
=
\text{conclusión correctamente deducida de un modelo incompleto}.
}
$$

Éste es uno de los riesgos más importantes del método.

### 14.14. La advertencia de Zorich

Zorich cierra sus ejemplos dimensionales señalando que la eficacia del método depende principalmente de comprender correctamente la naturaleza del fenómeno al que se aplica.[^s14-zorich-closing]

Esta observación resume nuestra arquitectura.

El análisis dimensional es especialmente valioso cuando aún no conocemos toda la ley física, porque puede revelar conexiones generales y orientar la investigación.

Pero precisamente en esos casos debemos ser más cuidadosos con:

- la selección de variables;
- las idealizaciones;
- las escalas;
- el dominio físico.

No basta con «hacer cuadrar las dimensiones».

### 14.15. Tabla de decisión del análisis dimensional

Ante un problema nuevo, usaremos esta secuencia.

| Pregunta | Si la respuesta es sí | Si la respuesta es no |
|---|---|---|
| ¿Están definidas las magnitudes? | seguir | precisar significado |
| ¿Las unidades y referencias son coherentes? | seguir | corregir representación |
| ¿La ecuación es homogénea? | seguir | localizar error |
| ¿Los argumentos de funciones son de dimensión uno? | seguir | normalizar/corregir |
| ¿La lista de variables es físicamente plausible? | aplicar inferencia | revisar modelo |
| ¿Hay grupos $\Pi$? | reducir variables | revisar rango/lista |
| ¿Se preservan los $\Pi$ relevantes entre sistemas? | comparar por semejanza | no afirmar semejanza |
| ¿La función adimensional está determinada? | usarla | teoría/datos necesarios |
| ¿El resultado está dentro del régimen del modelo? | interpretar | no extrapolar |

Esta tabla no es un algoritmo que reemplace el juicio físico.

Es una lista de control para organizarlo.

### 14.16. Qué distingue una demostración dimensional de una afirmación física

A lo largo de FPM mantendremos dos capas.

#### Capa matemática

Ejemplos:

$$
A\alpha=0,
$$

$$
\operatorname{rank}A=r,
$$

$$
n-r,
$$

$$
s_Q=\sum_i\alpha_is_i.
$$

Estas conclusiones pueden demostrarse exactamente bajo hipótesis formales.

#### Capa física

Ejemplos:

- estas son las variables relevantes;
- esta aproximación es adecuada;
- esta constante puede ignorarse;
- estos dos sistemas son comparables;
- este régimen experimental corresponde al modelo.

Estas afirmaciones deben justificarse físicamente.

La separación no debilita el rigor.

Lo aumenta.

### 14.17. Exactitud matemática y adecuación física

Volvemos así a una idea de `el capítulo 1`.

Podemos resolver exactamente un modelo inadecuado.

También podemos trabajar con una aproximación controlada de un modelo mucho más adecuado.

El análisis dimensional participa de esta misma distinción.

Una matriz dimensional puede ser impecable.

Un sistema de exponentes puede estar perfectamente resuelto.

Los grupos $\Pi$ pueden ser correctos.

Y, sin embargo, la representación física inicial puede ser insuficiente.

Por eso:

$$
\boxed{
\text{exactitud matemática relativa al modelo}
\neq
\text{adecuación física del modelo}.
}
$$

### 14.18. Autoexplicación final

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Sin consultar las secciones anteriores, explica:

1. una cosa que una incompatibilidad dimensional puede demostrar de manera concluyente;
2. una cosa que la homogeneidad nunca demuestra por sí sola;
3. qué información aporta Buckingham $\Pi$;
4. qué información deja sin determinar;
5. por qué la selección de variables pertenece a la física y no solamente al álgebra;
6. qué significa decir que dos sistemas son semejantes «respecto de un modelo».
:::

### 14.19. Práctica final

::: {.ma-block .ma-enunciado #fpm-i-02-e28}
**Ejercicio 28 — Auditoría integral de un modelo dimensional**

**Objetivo:** `Síntesis final`

**Intenta primero: 5–10 min antes de leer la solución.**

Un investigador propone que el tiempo característico $\tau$ de cierto fenómeno depende de:

$$
L,\qquad v,\qquad \rho,\qquad \mu,
$$

donde:

$$
[L]=L,
$$

$$
[v]=LT^{-1},
$$

$$
[\rho]=ML^{-3},
$$

$$
[\mu]=ML^{-1}T^{-1}.
$$

Propone además:

$$
\tau
=
\frac Lv
\left[
1+
\frac{\rho vL}{\mu}
\right].
$$

### A. Recuperación

Audita dimensionalmente la fórmula.

### B. Consolidación

Construye la matriz dimensional de:

$$
\tau,\ L,\ v,\ \rho,\ \mu.
$$

Determina $n$, $r$ y $n-r$.

### C. Buckingham

Construye dos grupos adimensionales independientes y escribe la forma general que Buckingham permite para $\tau$.

### D. Diagnóstico

Decide si la fórmula propuesta por el investigador queda demostrada por el análisis dimensional.

### E. Variación

Supón que nuevos experimentos muestran que dos sistemas con el mismo valor de:

$$
\frac{\rho vL}{\mu}
$$

tienen valores distintos de:

$$
\frac{\tau v}{L}.
$$

Da al menos tres explicaciones físicamente plausibles que deberían investigarse antes de concluir que Buckingham falla.

### F. Síntesis epistemológica

Clasifica cada afirmación como:

- consecuencia dimensional;
- hipótesis de modelización;
- información física adicional.

1. $\tau v/L$ tiene dimensión uno.
2. $\rho vL/\mu$ tiene dimensión uno.
3. solo las variables $L,v,\rho,\mu$ son relevantes.
4. existe una función $\Psi$ tal que

$$
\frac{\tau v}{L}
=
\Psi\left(
\frac{\rho vL}{\mu}
\right).
$$

5. $\Psi(x)=1+x$.
6. dos sistemas con igual argumento de $\Psi$ deben compararse dentro del mismo modelo.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

### A. Recuperación

Primero:

$$
\left[\frac Lv\right]
=
\frac{L}{LT^{-1}}
=
T.
$$

Además:

$$
\left[
\frac{\rho vL}{\mu}
\right]
=
1.
$$

Por tanto:

$$
\left[
1+\frac{\rho vL}{\mu}
\right]
=
1.
$$

Entonces:

$$
[\tau]=T.
$$

La expresión es dimensionalmente homogénea.

### B. Consolidación

En el orden $(T,L,M)$:

$$
\tau:
\begin{pmatrix}
1\\
0\\
0
\end{pmatrix},
\qquad
L:
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix},
$$

$$
v:
\begin{pmatrix}
-1\\
1\\
0
\end{pmatrix},
\qquad
\rho:
\begin{pmatrix}
0\\
-3\\
1
\end{pmatrix},
$$

$$
\mu:
\begin{pmatrix}
-1\\
-1\\
1
\end{pmatrix}.
$$

Así:

$$
n=5.
$$

Hay tres columnas dimensionalmente independientes, de modo que:

$$
r=3.
$$

Por tanto:

$$
\boxed{
n-r=2.
}
$$

### C. Buckingham

Dos grupos posibles son:

$$
\boxed{
\Pi_1
=
\frac{\tau v}{L}
}
$$

y:

$$
\boxed{
\Pi_2
=
\frac{\rho vL}{\mu}.
}
$$

Buckingham permite:

$$
\Phi(\Pi_1,\Pi_2)=0.
$$

Si podemos resolver para $\Pi_1$:

$$
\boxed{
\frac{\tau v}{L}
=
\Psi\left(
\frac{\rho vL}{\mu}
\right).
}
$$

Equivalentemente:

$$
\boxed{
\tau
=
\frac Lv
\Psi\left(
\frac{\rho vL}{\mu}
\right).
}
$$
