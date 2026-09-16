### 5.20. Ejercicios

::: {.ma-block .ma-enunciado #fpm-i-02-e11}
**Ejercicio 11 — Reconstruir dimensiones**

**Tipo:** análisis dimensional · **Nivel:** básico

Calcula las dimensiones de:

1. área;
2. volumen;
3. velocidad;
4. aceleración;
5. densidad de masa;
6. fuerza, usando $F=ma$;
7. energía, usando $E=F\ell$;
8. potencia, usando $P=E/t$;
9. presión, usando $p=F/A$.

No uses una tabla memorizada: deriva cada resultado.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

1. Para área:

$$
[A]=L\cdot L=L^2.
$$

2. Para volumen:

$$
[V]=L^3.
$$

3. Para velocidad:

$$
[v]=\frac{L}{T}=LT^{-1}.
$$

4. Para aceleración:

$$
[a]
=
\frac{LT^{-1}}{T}
=
LT^{-2}.
$$

5. Para densidad:

$$
[\rho]
=
\frac{M}{L^3}
=
ML^{-3}.
$$

6. Para fuerza:

$$
[F]
=
[m][a]
=
MLT^{-2}.
$$

7. Para energía:

$$
[E]
=
[F]L
=
ML^2T^{-2}.
$$

8. Para potencia:

$$
[P]
=
\frac{[E]}{T}
=
ML^2T^{-3}.
$$

9. Para presión:

$$
[p]
=
\frac{[F]}{[A]}
=
\frac{MLT^{-2}}{L^2}
=
ML^{-1}T^{-2}.
$$

El procedimiento es siempre el mismo:

$$
\boxed{
\text{relación entre magnitudes}
\longrightarrow
\text{relación entre dimensiones}.
}
$$
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e12}
**Ejercicio 12 — Cambiar unidades sin cambiar dimensión**

**Familia:** `E-DIM / E-PROOF / CORE`

Una rapidez vale

$$
v=90\,\mathrm{km\,h^{-1}}.
$$

1. Exprésala en $\mathrm{m\,s^{-1}}$.
2. Escribe su dimensión antes y después de la conversión.
3. Explica por qué el cambio de valor numérico no modifica los exponentes dimensionales.
4. Repite el argumento de manera simbólica si

$$
u_L'=\lambda_Lu_L,
\qquad
u_T'=\lambda_Tu_T.
$$
:::

::: {.ma-block .ma-comprobacion}
**Solución**

Como

$$
1\,\mathrm{km}=10^3\,\mathrm m
$$

y

$$
1\,\mathrm h=3600\,\mathrm s,
$$

tenemos

$$
90\,\mathrm{km\,h^{-1}}
=
90\frac{10^3\,\mathrm m}{3600\,\mathrm s}.
$$

Por tanto,

$$
v=25\,\mathrm{m\,s^{-1}}.
$$

El valor numérico cambió:

$$
90\longrightarrow25.
$$

La unidad cambió:

$$
\mathrm{km\,h^{-1}}
\longrightarrow
\mathrm{m\,s^{-1}}.
$$

Pero en ambos casos

$$
[v]=LT^{-1}.
$$

En forma simbólica, si

$$
u_L'=\lambda_Lu_L
$$

y

$$
u_T'=\lambda_Tu_T,
$$

entonces los valores numéricos de longitud y tiempo adquieren factores inversos:

$$
\ell'\sim\lambda_L^{-1}\ell,
$$

$$
t'\sim\lambda_T^{-1}t.
$$

Por ello la rapidez numérica adquiere el factor

$$
\lambda_L^{-1}\lambda_T,
$$

pero la estructura de dependencia continúa siendo

$$
L^1T^{-1}.
$$

Los factores de conversión afectan números; los exponentes dimensionales registran la estructura y permanecen iguales.
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e13}
**Ejercicio 13 — Misma dimensión, distinto significado**

**Familia:** `E-CON / E-DIM / CORE`

Considera los pares:

1. frecuencia y actividad radionúclida;
2. presión y densidad de energía;
3. longitud de una barra y longitud de onda;
4. masa y tiempo.

Para cada par:

a. determina si las dimensiones son iguales;
b. decide si la igualdad dimensional basta para afirmar que son magnitudes del mismo tipo;
c. explica qué conclusión es legítima.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

**1. Frecuencia y actividad radionúclida**

Ambas tienen

$$
T^{-1}.
$$

Sin embargo, no son del mismo tipo de magnitud.

La conclusión legítima es:

$$
\boxed{
\text{misma dimensión, distinto significado físico}.
}
$$

**2. Presión y densidad de energía**

Para presión:

$$
[p]=ML^{-1}T^{-2}.
$$

Para densidad de energía:

$$
\left[\frac{E}{V}\right]
=
\frac{ML^2T^{-2}}{L^3}
=
ML^{-1}T^{-2}.
$$

Las dimensiones coinciden.

Esto no demuestra que ambas magnitudes sean del mismo tipo.

**3. Longitud de una barra y longitud de onda**

Ambas pertenecen al tipo longitud y tienen

$$
L.
$$

Aquí la igualdad dimensional es compatible con que sean del mismo tipo.

Pero no es la igualdad dimensional por sí sola la que establece esa clasificación: necesitamos además la interpretación física.

**4. Masa y tiempo**

Tenemos

$$
[m]=M,
$$

$$
[t]=T.
$$

Como las dimensiones son diferentes, necesariamente se trata de tipos de magnitud distintos.

En conjunto:

$$
\boxed{
\text{dimensiones diferentes}
\Longrightarrow
\text{tipos diferentes},
}
$$

pero

$$
\boxed{
\text{dimensiones iguales}
\not\Longrightarrow
\text{mismo tipo}.
}
$$
:::

### 5.21. Síntesis

La sección introduce la abstracción decisiva:

$$
\boxed{
\text{unidad concreta}
\longrightarrow
\text{dimensión}
}
$$

La dimensión de una magnitud se expresa, respecto de la base dimensional del SI, como

$$
\boxed{
[Q]
=
T^\alpha
L^\beta
M^\gamma
I^\delta
\Theta^\varepsilon
N^\zeta
J^\eta.
}
$$

Los exponentes describen la estructura dimensional y no dependen del tamaño de las unidades concretas elegidas.

Por eso:

$$
\boxed{
\text{cambiar unidad}
\not\Rightarrow
\text{cambiar dimensión}.
}
$$

Y debemos conservar otra cautela:

$$
\boxed{
\text{misma dimensión}
\not\Rightarrow
\text{mismo tipo de magnitud}.
}
$$

Con este lenguaje ya podemos formular la siguiente pregunta.

Si una ecuación física debe seguir teniendo sentido cuando cambiamos las unidades base, ¿qué restricciones impone eso a los términos que sumamos o igualamos?

Ése será el objeto de:

$$
\boxed{
\text{§6 — Homogeneidad dimensional}.
}
$$

---

### Notas y fuentes

[^s5-bipm-dimensions]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.3, pp. 132–133.
[^s5-vim-dimension]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.7, «quantity dimension».
[^s5-zorich-dimensions]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §§1.1–1.2, pp. 5–8, DOI 10.1007/978-3-642-14813-2.
