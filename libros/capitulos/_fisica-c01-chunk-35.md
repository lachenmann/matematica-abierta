#### 5. Variable, parámetro y observable

Una variable de estado es:

$$
x.
$$

El parámetro del modelo es:

$$
d=2.
$$

El observable es la posición registrada por la cámara:

$$
O(n,x)=x.
$$

En una realización experimental, esa cantidad necesita una regla de calibración espacial.
#### 6. Estatus de la regla

La relación:

$$
x_{n+1}=x_n+d
$$

se ha propuesto para representar exactamente, dentro del modelo, la regularidad observada.

Por tanto, en este contexto su estatus principal es:

$$
[\mathrm{MOD}].
$$

Podría haber sido motivada por datos `[EMP]`, pero no la hemos derivado de una teoría mecánica.
#### 7. Condición inicial

Podemos tomar:

$$
[\mathrm{IC}]
\qquad
x_0=0.
$$

Esto selecciona una realización concreta de la regla.
#### 8. Predicción

Como:

$$
x_3=6
$$

y:

$$
d=2,
$$

la regla da:

$$
x_4=x_3+d.
$$

Entonces:

$$
x_4=6+2=8.
$$

Por tanto:

$$
\boxed{x_4=8}.
$$
#### 9. Parte matemática

Una vez aceptados:

$$
x_3=6,
$$

$$
d=2
$$

y:

$$
x_{n+1}=x_n+d,
$$

la inferencia:

$$
x_4=8
$$

es:

$$
[\mathrm{MATH}].
$$

La aritmética es exacta dentro del modelo.
#### 10. Regla observacional

Necesitamos una conexión:

$$
[\mathrm{OBS}]
\qquad
x
\longleftrightarrow
\text{posición inferida de la imagen de la cámara mediante una escala calibrada}.
$$

Debemos saber:

- qué punto del carro representa su posición;
- dónde está el origen;
- qué unidad se utiliza;
- cómo la imagen se convierte en una coordenada.

Sin esa mediación, el número $8$ sigue siendo solo parte del formalismo.
#### 11. Idealizaciones o simplificaciones

Entre otras:

1. representamos el carro mediante una única coordenada;
2. ignoramos su orientación y dimensiones;
3. tratamos los instantes como igualmente espaciados;
4. suponemos que el mismo incremento $d$ continúa siendo adecuado;
5. ignoramos explícitamente causas físicas del movimiento.

Estas omisiones son aceptables solo respecto de la pregunta propuesta.
#### 12. Régimen cualitativo

Podemos declarar provisionalmente:

> la regla se utiliza para los próximos registros mientras la pista, la preparación, el intervalo entre imágenes y el comportamiento observado permanezcan comparables con los de la serie inicial.

No es todavía un régimen cuantitativo sofisticado.

Pero hace visible que no estamos autorizados a extrapolar indefinidamente.
#### 13. Si observamos $x_4=8$

El nuevo dato es compatible con la predicción.

Podemos afirmar:

> el modelo ha superado esta prueba adicional.

No podemos afirmar:

> la regla ha sido demostrada como ley única del movimiento.

`P01` ya nos enseñó que datos finitos no determinan una única ley funcional.
#### 14. Si observamos $x_4=7.1$

Tenemos una discrepancia.

Debemos auditar, por ejemplo:

1. **regla del modelo:** quizá el incremento dejó de ser constante;
2. **condición o dato anterior:** quizá $x_3$ fue mal determinado;
3. **parámetro:** quizá $d$ no era realmente $2$;
4. **mediación observacional:** quizá la cámara o calibración introdujo un error;
5. **régimen:** quizá cambió alguna condición de la pista o preparación;
6. **idealización:** quizá un efecto omitido se volvió relevante.

La observación no identifica automáticamente cuál de estas alternativas es responsable.
#### 15. Por qué no es todavía una teoría mecánica

El modelo:

$$
x_{n+1}=x_n+2
$$

describe una regularidad de posiciones.

No proporciona todavía:

- principios generales de movimiento;
- una estructura aplicable a muchas clases de sistemas;
- mecanismos;
- una teoría de interacciones;
- reglas generales para construir otros modelos.

Por tanto:

$$
\boxed{
\text{modelo empírico}
\neq
\text{teoría mecánica}.
}
$$
#### 16. Nueva prueba

Podemos observar:

$$
x_5.
$$

El modelo predice:

$$
x_5=10.
$$

Pero una prueba más informativa podría también cambiar deliberadamente una condición del experimento y preguntar si $d$ permanece constante.

La elección depende de qué aspecto del modelo queramos poner a prueba.
#### 17. Exactitud y adecuación

**Exactitud matemática:**

dentro de:

$$
x_{n+1}=x_n+2,
$$

la predicción:

$$
x_4=8
$$

se obtiene exactamente.

**Adecuación física:**

solo puede evaluarse comparando la regla con nuevas observaciones dentro del régimen pertinente.

Por tanto:

$$
\boxed{
\text{predicción algebraicamente exacta}
\neq
\text{garantía de adecuación física}.
}
$$
