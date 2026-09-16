### D. Diagnóstico

La fórmula propuesta:

$$
\tau
=
\frac Lv
\left[
1+
\frac{\rho vL}{\mu}
\right]
$$

corresponde a elegir:

$$
\Psi(x)=1+x.
$$

Buckingham no determina esa función.

Por tanto:

$$
\boxed{
\text{la fórmula pasa el control dimensional,
pero no queda demostrada por él}.
}
$$

### E. Variación

Si dos sistemas con el mismo:

$$
\frac{\rho vL}{\mu}
$$

producen distinto:

$$
\frac{\tau v}{L},
$$

antes de culpar al teorema debemos revisar, por ejemplo:

1. **variables omitidas**: rugosidad, geometría adicional, temperatura u otro parámetro relevante;
2. **diferentes condiciones de frontera o iniciales**;
3. **regímenes físicos distintos** no capturados por el modelo;
4. errores experimentales o definición no equivalente de $\tau$;
5. hipótesis constitutivas distintas para el medio.

Buckingham trabaja sobre el modelo declarado.

Una discrepancia puede indicar que el modelo no contiene toda la física pertinente.

### F. Síntesis epistemológica

**1.**

$$
\frac{\tau v}{L}
$$

tiene dimensión uno:

**consecuencia dimensional**.

**2.**

$$
\frac{\rho vL}{\mu}
$$

tiene dimensión uno:

**consecuencia dimensional**.

**3.**

Solo $L,v,\rho,\mu$ son relevantes:

**hipótesis de modelización**.

**4.**

$$
\frac{\tau v}{L}
=
\Psi\left(
\frac{\rho vL}{\mu}
\right)
$$

es la reducción dimensional derivada de Buckingham **condicionada a esa lista de variables y a sus hipótesis de invariancia**.

**5.**

$$
\Psi(x)=1+x
$$

es **información física adicional** o una hipótesis funcional que requiere justificación.

**6.**

Comparar sistemas con el mismo argumento adimensional es una consecuencia del marco de semejanza **dentro del mismo modelo**.

La distinción final queda:

$$
\boxed{
\text{álgebra dimensional}
\quad|\quad
\text{premisas del modelo}
\quad|\quad
\text{contenido físico adicional}.
}
$$
:::

### 14.20. Mapa final del capítulo

El capítulo comenzó con una advertencia sencilla:

$$
\boxed{
\text{un número no es todavía una magnitud física}.
}
$$

Desde allí construimos:

$$
\text{número}
\to
\text{valor}
\to
\text{unidad}
\to
\text{tipo de magnitud}
\to
\text{SI}
\to
\text{unidad derivada}
\to
\text{dimensión}
\to
\text{homogeneidad}
\to
\text{auditoría}
\to
\text{dimensión uno}
\to
\text{escala característica}
\to
\text{adimensionalización}
\to
\text{inferencia}
\to
\text{semejanza}
\to
\text{Buckingham }\Pi
\to
\text{modelización}.
$$

La cadena no termina en una fórmula.

Termina en una disciplina de lectura:

$$
\boxed{
\text{¿qué sabemos?}
\quad
\text{¿qué suponemos?}
\quad
\text{¿qué demostramos?}
\quad
\text{¿qué sigue siendo físico?}
}
$$

### 14.21. Cierre

El análisis dimensional es una herramienta extraordinaria porque detecta estructura sin exigir conocer todos los detalles de una teoría.

Puede decir mucho con poca información.

Pero no puede decir más de lo que esa información contiene.

Por eso su uso riguroso exige dos movimientos simultáneos:

$$
\boxed{
\text{explotar al máximo las consecuencias dimensionales}
}
$$

y

$$
\boxed{
\text{no atribuirles contenido físico que no poseen}.
}
$$

Con esto queda cerrado el capítulo:

$$
\boxed{
\text{Magnitudes, unidades y análisis dimensional}.
}
$$

El siguiente capítulo del tratado será:

$$
\boxed{
\text{el capítulo 3 — Medición, incertidumbre, estimación y órdenes de magnitud}.
}
$$

Allí cambiaremos de pregunta.

Hasta ahora estudiamos principalmente cómo **representar y estructurar magnitudes**, elegir escalas y construir variables de dimensión uno.

A continuación cambiaremos desde la estructura del modelo hacia la **obtención experimental de valores**: mediciones finitas, incertidumbre, cifras significativas y estimaciones cuantitativas. El desarrollo detallado de estimaciones tipo Fermi y de precisión experimental queda deliberadamente allí, para no duplicar el alcance de este capítulo.

---

### Notas y fuentes

[^s14-zorich-closing]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §2.8, «Concluding remarks», pp. 18–21.
