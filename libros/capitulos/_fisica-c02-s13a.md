## §13 — Ejemplos de modelización dimensional {#fpm-i-02-s13}

### 13.1. Intuir: ahora importa tanto elegir variables como manipular dimensiones

Hasta §12 hemos construido un aparato poderoso:

- dimensión;
- homogeneidad;
- firmas dimensionales;
- inferencia de exponentes;
- escalamiento;
- semejanza;
- teorema $\Pi$ de Buckingham.

Pero una herramienta formal solo trabaja con las variables que el modelo le entrega.

Si seleccionamos mal esas variables, podemos hacer álgebra impecable sobre un modelo incompleto.

Por eso esta sección no introduce un nuevo teorema.

Introduce un modo de **usar** los teoremas.

La pregunta rectora será:

$$
\boxed{
\text{¿qué parte de la conclusión proviene de la dimensión
y qué parte proviene de la física?}
}
$$

Trabajaremos dos casos:

1. período de un péndulo;
2. fuerza de arrastre de una esfera en un medio.

Ambos aparecen en la tradición clásica del análisis dimensional y están tratados como aplicaciones por Zorich.[^s13-zorich-applications]

### 13.2. Caso I — El péndulo: empezar por la lista de variables

Consideremos un péndulo idealizado:

- masa puntual $m$;
- suspensión sin masa de longitud $\ell$;
- ángulo inicial $\varphi_0$;
- aceleración gravitatoria $g$;
- período $P$.

Queremos modelar:

$$
P.
$$

Una primera lista incompleta sería:

$$
P=f(\ell,m,\varphi_0).
$$

Pero esta lista no distingue, por ejemplo, un péndulo situado en campos gravitatorios de distinta intensidad.

Zorich utiliza precisamente esta observación para justificar que debe incluirse $g$.[^s13-zorich-pendulum]

La lista mínima considerada pasa entonces a:

$$
\boxed{
P=f(\ell,m,g,\varphi_0).
}
$$

::: {.ma-block .ma-metodo}
**Principio 25 — La selección de variables es una hipótesis de modelización**
Buckingham $\Pi$ puede reorganizar una lista de variables pertinente, pero no decide por sí solo si esa lista está físicamente completa. Incluir u omitir una variable es una decisión del modelo que debe justificarse por separado.
:::

### 13.3. Representar: matriz dimensional del péndulo

Usaremos el orden de dimensiones:

$$
(T,L,M).
$$

Las firmas son:

$$
\mathbf d(P)
=
\begin{pmatrix}
1\\
0\\
0
\end{pmatrix},
$$

$$
\mathbf d(\ell)
=
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix},
$$

$$
\mathbf d(m)
=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix},
$$

$$
\mathbf d(g)
=
\begin{pmatrix}
-2\\
1\\
0
\end{pmatrix},
$$

y, porque el ángulo tiene dimensión uno,

$$
\mathbf d(\varphi_0)
=
\begin{pmatrix}
0\\
0\\
0
\end{pmatrix}.
$$

Por tanto:

$$
A
=
\begin{pmatrix}
1 & 0 & 0 & -2 & 0\\
0 & 1 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0
\end{pmatrix}.
$$

Tenemos:

$$
n=5.
$$

Las tres primeras columnas son independientes, por lo que:

$$
r=3.
$$

Buckingham predice:

$$
\boxed{
n-r=2
}
$$

grupos adimensionales independientes.

### 13.4. Construir los dos grupos Π

Uno es inmediato:

$$
\boxed{
\Pi_2=\varphi_0.
}
$$

Para el otro buscamos:

$$
\Pi_1
=
P\ell^\alpha g^\beta.
$$

La dimensión es:

$$
[\Pi_1]
=
T
L^\alpha
(LT^{-2})^\beta.
$$

Entonces:

$$
[\Pi_1]
=
L^{\alpha+\beta}
T^{1-2\beta}.
$$

Exigimos dimensión uno:

$$
\alpha+\beta=0,
$$

$$
1-2\beta=0.
$$

De aquí:

$$
\beta=\frac12,
$$

$$
\alpha=-\frac12.
$$

Por tanto:

$$
\boxed{
\Pi_1
=
P\sqrt{\frac g\ell}.
}
$$

### 13.5. Buckingham aplicado al péndulo

El teorema permite escribir:

$$
\Phi(\Pi_1,\Pi_2)=0.
$$

Es decir:

$$
\Phi\left(
P\sqrt{\frac g\ell},
\varphi_0
\right)
=
0.
$$

Localmente, cuando la relación puede resolverse respecto del primer grupo, podemos escribir:

$$
P\sqrt{\frac g\ell}
=
\Psi(\varphi_0).
$$

Por tanto:

$$
\boxed{
P
=
\sqrt{\frac{\ell}{g}}\,
\Psi(\varphi_0).
}
$$

Ésta es una conclusión mucho más precisa que:

$$
P=C\sqrt{\frac{\ell}{g}}.
$$

La constante $C$ aparece solo si $\Psi$ puede tratarse como aproximadamente constante en el régimen físico considerado.

### 13.6. ¿Dónde quedó la masa?

La masa $m$ estaba incluida en la lista.

Sin embargo, no aparece en la forma reducida:

$$
P
=
\sqrt{\frac{\ell}{g}}\,
\Psi(\varphi_0).
$$

Esto no ocurrió porque decidiéramos de antemano «ignorar la masa».

Ocurrió porque, dentro de este conjunto de variables y dimensiones, no puede construirse una dependencia adimensional independiente en $m$ compatible con el período.

La dimensión impide que $m$ aparezca no trivialmente en la forma reducida.

Pero debemos leer la conclusión correctamente:

> dentro del modelo idealizado y de la lista de variables declarada, la masa no aparece como parámetro independiente del período.

No estamos afirmando que la masa sea irrelevante para toda propiedad física de un péndulo real.

### 13.7. Lo que la dimensión no determina en el péndulo

La expresión:

$$
P
=
\sqrt{\frac{\ell}{g}}\,
\Psi(\varphi_0)
$$

todavía contiene información desconocida:

$$
\Psi.
$$

El análisis dimensional no dice:

- cuál es la función exacta;
- si es constante;
- cómo depende de $\varphi_0$;
- para qué amplitudes puede aproximarse;
- cuál es el error de una aproximación.

Para oscilaciones de pequeña amplitud, la teoría dinámica permite obtener:

$$
\Psi(\varphi_0)
\approx
2\pi.
$$

Entonces:

$$
P
\approx
2\pi
\sqrt{\frac{\ell}{g}}.
$$

Pero el símbolo:

$$
\approx
$$

marca información física adicional: una aproximación de régimen pequeño, no una consecuencia del teorema $\Pi$.

### 13.8. Autoexplicación del primer caso

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Explica con tus propias palabras:

1. por qué fue necesario incluir $g$;
2. por qué $\varphi_0$ sobrevive como argumento de una función;
3. por qué la masa desaparece;
4. por qué Buckingham no produce $2\pi$;
5. qué afirmación depende del modelo idealizado y no solo del álgebra.
:::

### 13.9. Caso II — Arrastre en un medio: empezar por el modelo más austero

Consideremos una esfera de radio $r$ que se mueve con velocidad característica $v$ en un medio de densidad $\rho$.

Queremos estudiar una fuerza de arrastre $F$.

Comencemos con el modelo dimensional:

$$
\boxed{
F=f(\rho,v,r).
}
$$

Zorich utiliza precisamente este conjunto de variables para su ejemplo de una esfera en un medio no viscoso.[^s13-zorich-drag]

Las dimensiones son:

$$
[F]=MLT^{-2},
$$

$$
[\rho]=ML^{-3},
$$

$$
[v]=LT^{-1},
$$

$$
[r]=L.
$$

Tenemos cuatro variables:

$$
n=4.
$$

Y las dimensiones $M,L,T$ aparecen independientemente, de modo que:

$$
r_{\mathrm{dim}}=3.
$$

Por tanto:

$$
n-r_{\mathrm{dim}}=1.
$$

Solo existe un grupo adimensional independiente.

### 13.10. Construir el grupo de fuerza

Buscamos:

$$
\Pi_F
=
F\rho^\alpha v^\beta r^\gamma.
$$

Su dimensión es:

$$
MLT^{-2}
\cdot
(M L^{-3})^\alpha
\cdot
(LT^{-1})^\beta
\cdot
L^\gamma.
$$

Agrupando:

$$
M^{1+\alpha}
L^{1-3\alpha+\beta+\gamma}
T^{-2-\beta}.
$$

Exigimos exponente cero para cada dimensión.

Masa:

$$
1+\alpha=0,
$$

luego:

$$
\alpha=-1.
$$

Tiempo:

$$
-2-\beta=0,
$$

luego:

$$
\beta=-2.
$$

Longitud:

$$
1-3(-1)-2+\gamma=0.
$$

Por tanto:

$$
2+\gamma=0,
$$

y:

$$
\gamma=-2.
$$

Así:

$$
\boxed{
\Pi_F
=
\frac{F}{\rho v^2r^2}.
}
$$

### 13.11. Qué concluye Buckingham en el modelo de tres variables explicativas

Como solo existe un grupo adimensional independiente, la relación reducida tiene la forma:

$$
\Phi(\Pi_F)=0.
$$

En una rama física donde esta ecuación selecciona un valor constante:

$$
\Pi_F=C.
$$

Entonces:

$$
\boxed{
F
=
C\rho v^2r^2.
}
$$

Ésta es precisamente la estructura obtenida en el ejemplo dimensional de Zorich.[^s13-zorich-drag-form]

Pero:

$$
\boxed{
C
}
$$

no viene determinado por la dimensión.

La dimensión tampoco prueba que el modelo de variables:

$$
\rho,\ v,\ r
$$

sea suficiente para un fluido real.

### 13.12. Poner a prueba el modelo: introducir viscosidad

Supongamos ahora que el medio posee una viscosidad dinámica relevante:

$$
\mu.
$$

La lista se amplía:

$$
\boxed{
F=f(\rho,v,r,\mu).
}
$$

Tenemos ahora:

$$
n=5.
$$

El rango dimensional continúa siendo:

$$
r_{\mathrm{dim}}=3.
$$

Por tanto:

$$
\boxed{
n-r_{\mathrm{dim}}=2.
}
$$

Debemos esperar dos grupos adimensionales independientes.

Uno puede seguir siendo:

$$
\Pi_1
=
\frac{F}{\rho v^2r^2}.
$$

El segundo puede tomarse como:

$$
\Pi_2
=
\frac{\rho vr}{\mu}.
$$

Verifiquemos:

$$
[\rho vr]
=
ML^{-3}
\cdot
LT^{-1}
\cdot
L
=
ML^{-1}T^{-1}.
$$

Y:

$$
[\mu]
=
ML^{-1}T^{-1}.
$$

Por tanto:

$$
[\Pi_2]=1.
$$

### 13.13. La función reaparece

Buckingham produce ahora:

$$
\Phi(\Pi_1,\Pi_2)=0.
$$

Cuando podemos despejar $\Pi_1$:

$$
\Pi_1
=
\Psi(\Pi_2).
$$

Así:

$$
\boxed{
\frac{F}{\rho v^2r^2}
=
\Psi\left(
\frac{\rho vr}{\mu}
\right).
}
$$

O:

$$
\boxed{
F
=
\rho v^2r^2
\,
\Psi\left(
\frac{\rho vr}{\mu}
\right).
}
$$

La combinación:

$$
\frac{\rho vr}{\mu}
$$

es una forma del número de Reynolds basada en la escala $r$.

La sección no necesita todavía interpretar en detalle todos los regímenes de flujo.

Lo importante es observar qué ocurrió al añadir una variable físicamente relevante:

$$
\boxed{
\text{constante adimensional}
\longrightarrow
\text{función de un parámetro adimensional}.
}
$$

### 13.14. Qué enseña el segundo caso

Con el modelo:

$$
F=f(\rho,v,r),
$$

la dimensión obliga a una forma:

$$
F=C\rho v^2r^2.
$$

Con el modelo ampliado:

$$
F=f(\rho,v,r,\mu),
$$

la dimensión solo obliga a:

$$
F
=
\rho v^2r^2
\Psi(\rho vr/\mu).
$$

No hay contradicción.

Cambió el modelo.

La diferencia muestra por qué la elección de variables es una decisión física previa a Buckingham.

Si omitimos $\mu$, el teorema no puede advertir que la viscosidad era importante.

### 13.15. Semejanza en el problema de arrastre

Supongamos dos experimentos con:

$$
(\rho_1,v_1,r_1,\mu_1)
$$

y:

$$
(\rho_2,v_2,r_2,\mu_2).
$$

Si queremos que ambos ocupen el mismo punto en la descripción adimensional del modelo viscoso, debemos mantener:

$$
\boxed{
\frac{\rho_1v_1r_1}{\mu_1}
=
\frac{\rho_2v_2r_2}{\mu_2}.
}
$$

Entonces el mismo valor del argumento de $\Psi$ produce, dentro del modelo, el mismo valor del coeficiente adimensional:

$$
\frac{F}{\rho v^2r^2}.
$$

Ésta es la lógica de semejanza:

$$
\boxed{
\text{igualar parámetros adimensionales relevantes}
\longrightarrow
\text{comparar sistemas a escalas distintas}.
}
$$

### 13.16. Ejemplo de escalamiento de un modelo

Supongamos:

- mismo fluido, de modo que $\rho$ y $\mu$ son iguales;
- radios relacionados por:

$$
r_2=\lambda r_1.
$$

Para conservar:

$$
\frac{\rho vr}{\mu},
$$

necesitamos:

$$
v_2r_2=v_1r_1.
$$

Entonces:

$$
v_2
=
\lambda^{-1}v_1.
$$

Así, si el modelo es diez veces más pequeño:

$$
\lambda=\frac1{10},
$$

la velocidad necesaria para conservar este parámetro sería:

$$
v_2=10v_1.
$$

La semejanza física no sigue automáticamente la escala geométrica.

Puede exigir reescalar otras variables en sentido contrario.

### 13.17. Diagnóstico comparado de los dos casos

El péndulo y el arrastre muestran dos mecanismos distintos.

#### Péndulo

Una variable ya adimensional:

$$
\varphi_0
$$

sobrevive directamente como argumento funcional:

$$
P
=
\sqrt{\frac{\ell}{g}}
\Psi(\varphi_0).
$$

#### Arrastre viscoso

La variable adicional $\mu$ no es adimensional.

Pero, al combinarse con:

$$
\rho,\ v,\ r,
$$

genera:

$$
\frac{\rho vr}{\mu}.
$$

Entonces:

$$
F
=
\rho v^2r^2
\Psi(\rho vr/\mu).
$$

En ambos casos, la función adimensional contiene física no resuelta por las dimensiones.

### 13.18. Qué puede decir la dimensión y qué no

Podemos ordenar los resultados.

#### La dimensión sí puede

- detectar variables incompatibles;
- construir grupos adimensionales;
- restringir exponentes;
- eliminar dependencias imposibles dentro de un modelo;
- identificar escalas naturales;
- reducir el número de variables;
- formular criterios de semejanza.

#### La dimensión no puede, por sí sola

- decidir qué variables son físicamente relevantes;
- demostrar que una idealización es válida;
- determinar funciones adimensionales generales;
- fijar todos los coeficientes numéricos;
- establecer regímenes de aproximación;
- reemplazar experimentos o ecuaciones dinámicas.

La herramienta es poderosa precisamente cuando mantenemos visible esta frontera.

### 13.19. Práctica guiada

::: {.ma-block .ma-enunciado}
**Ejercicio 27 — Modelización dimensional completa**

**Objetivo:** `Síntesis`

**Intenta primero: 3–5 min antes de leer la solución.**

Queremos estudiar una fuerza $F$ asociada al movimiento de un objeto de tamaño característico $L$ con velocidad $v$ en un medio de densidad $\rho$ y viscosidad dinámica $\mu$.

### A. Recuperación

Usa:

$$
[F]=MLT^{-2},
$$

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

Construye la matriz dimensional en el orden $(T,L,M)$ y determina su rango.

### B. Consolidación

Usa Buckingham para justificar que deben existir dos grupos adimensionales independientes.

Encuentra un conjunto posible.

### C. Diagnóstico

Un estudiante omite $\mu$ y obtiene:

$$
F=C\rho v^2L^2.
$$

Explica:

1. por qué la deducción dimensional es correcta para la lista reducida;
2. por qué eso no demuestra que la viscosidad sea físicamente irrelevante.

### D. Síntesis

Para dos modelos en el mismo fluido, con tamaños:

$$
L_2=\frac14L_1,
$$

determina cómo debe cambiar la velocidad para conservar:

$$
\frac{\rho vL}{\mu}.
$$

Luego explica qué cantidad adimensional de fuerza debería coincidir entre ambos modelos si la semejanza es válida.

### E. Autoexplicación

Señala en tu solución:

- qué vino de las dimensiones;
- qué vino de la selección de variables;
- qué sigue dependiendo de una función o de datos físicos.
:::

::: {.ma-block .ma-comprobacion}
**Solución**
