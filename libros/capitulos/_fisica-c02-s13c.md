### 13.20. Variar: volver al péndulo con una variable omitida

Supongamos que alguien comienza con:

$$
P=f(\ell,m,\varphi_0)
$$

y aplica Buckingham correctamente.

El resultado será matemáticamente consistente con esa lista.

Pero no contendrá:

$$
g.
$$

El problema no está en la reducción dimensional.

Está **antes** de ella.

La pregunta física fue incompleta.

Esta variación muestra una regla general:

$$
\boxed{
\text{una inferencia formal no puede recuperar una variable
que el modelo nunca declaró}.
}
$$

### 13.21. Conectar con el cierre del capítulo

Después de trece secciones podemos ver el análisis dimensional como una cadena completa:

$$
\boxed{
\text{magnitudes}
\to
\text{unidades}
\to
\text{dimensiones}
\to
\text{homogeneidad}
\to
\text{auditoría}
\to
\text{escalamiento}
\to
\text{grupos }\Pi
\to
\text{modelización}.
}
$$

El valor del método no está únicamente en encontrar potencias correctas.

Está en hacer visibles las preguntas:

- ¿qué variables elegimos?;
- ¿qué supuestos estamos introduciendo?;
- ¿qué información es dimensional?;
- ¿qué información sigue siendo física?;
- ¿qué debe decidir un experimento o una teoría más completa?

### 13.22. Síntesis

#### Péndulo

Buckingham produce:

$$
\boxed{
P
=
\sqrt{\frac{\ell}{g}}
\Psi(\varphi_0).
}
$$

La dimensión explica:

- la escala temporal $\sqrt{\ell/g}$;
- la ausencia de una dependencia independiente en $m$;
- la supervivencia de $\varphi_0$ como parámetro adimensional.

No produce:

- la función $\Psi$;
- el valor $2\pi$;
- el régimen de pequeña amplitud.

#### Arrastre viscoso

Buckingham produce:

$$
\boxed{
F
=
\rho v^2r^2
\Psi\left(
\frac{\rho vr}{\mu}
\right).
}
$$

La dimensión explica:

- la escala de fuerza;
- el grupo adimensional de flujo;
- la estructura de semejanza.

No produce:

- la función $\Psi$;
- qué regímenes físicos existen;
- la validez del modelo para un medio concreto.

La lección común es:

$$
\boxed{
\text{análisis dimensional}
=
\text{estructura rigurosa dentro de un modelo},
}
$$

no:

$$
\boxed{
\text{análisis dimensional}
=
\text{física completa}.
}
$$

Solo queda cerrar el capítulo mediante:

$$
\boxed{
\text{§14 — Qué puede y qué no puede decir el análisis dimensional}.
}
$$

---

### Notas y fuentes

[^s13-zorich-applications]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, cap. 2, «Examples of applications», pp. 11–21.
[^s13-zorich-pendulum]: Zorich, op. cit., §2.3, «Period of oscillation of a heavy pendulum (inclusion of g)», pp. 13–14.
[^s13-zorich-drag]: Zorich, op. cit., §2.5, «Drag force for the motion of a ball in a non-viscous medium», pp. 14–15, y §2.6, «…in a viscous medium», pp. 15–16.
[^s13-zorich-drag-form]: Zorich, op. cit., §2.5, pp. 14–15, ecuación (2.1).
