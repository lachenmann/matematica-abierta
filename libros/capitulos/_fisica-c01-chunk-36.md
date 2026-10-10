#### 18. Ficha formal

Podemos escribir esquemáticamente:

$$
\mathcal M
=
(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R),
$$

con:

- $\mathcal S$: estados discretos $(n,x)$;
- $X$: posición $x$ y observable asociado;
- $\theta$: $d=2$;
- $\mathcal L$: regla $x_{n+1}=x_n+d$;
- $I$: $x_0=0$;
- $B$: no intervienen condiciones de frontera relevantes en este modelo mínimo;
- $\mathcal R$: serie de observaciones bajo condiciones comparables.

El diccionario:

$$
\mathfrak I_{\mathcal M}
$$

declara que:

- $n$ representa el índice de una imagen tomada a intervalos iguales;
- $x$ representa una posición sobre la pista;
- $d$ representa el incremento de posición entre registros;
- `[OBS]` conecta píxeles o marcas de la imagen con la coordenada física.

La unidad mínima de lectura es entonces:

$$
\boxed{
(\mathcal M,\mathfrak I_{\mathcal M}).
}
$$

El ejercicio ha recorrido prácticamente todo el protocolo del capítulo.
### 14.7. Cierre

Empezamos con una pregunta:

> **¿Qué convierte una pregunta sobre el mundo en un problema físico matemáticamente tratable?**

La respuesta no fue «una ecuación».

Fue una arquitectura.

$$
\boxed{
\text{fenómeno}
\to
\text{pregunta}
\to
\text{sistema}
\to
\text{modelo}
\to
\text{matemática}
\to
\text{predicción}
\to
\text{observación}
\to
\text{revisión}.
}
$$

Aprendimos que:

$$
\boxed{
\text{objeto físico}
\neq
\text{objeto matemático que lo representa};
}
$$

que:

$$
\boxed{
\text{ley}
\neq
\text{modelo}
\neq
\text{teoría};
}
$$

que:

$$
\boxed{
\text{ajuste}
\neq
\text{predicción}
\neq
\text{explicación};
}
$$

que:

$$
\boxed{
\text{datos finitos}
\not\Rightarrow
\text{ley única};
}
$$

que:

$$
\boxed{
\text{fallo predictivo}
\not\Rightarrow
\text{culpable único};
}
$$

y, finalmente:

$$
\boxed{
\text{exactitud matemática}
\neq
\text{adecuación física}.
}
$$

Estas distinciones no pertenecen únicamente al capítulo inicial.

Constituyen la gramática del resto del tratado.

A partir del próximo capítulo comenzaremos a construir las primeras herramientas cuantitativas de esa gramática:

$$
\boxed{
\text{magnitudes, unidades y análisis dimensional}.
}
$$

Las ecuaciones podrán ser cada vez más sofisticadas.

La pregunta seguirá siendo la misma:

> **¿Qué relación existe entre el fenómeno, el modelo y la estructura matemática que estamos usando para comprenderlo?**
