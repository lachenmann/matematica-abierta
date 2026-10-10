## 12.8. Teorema de caracterización {#sec-ta-12-8}

La construcción abstracta está terminada. Ya no queda por fabricar ninguna operación, ningún orden ni ningún transporte nuevo. Lo que resta es reunir en una sola afirmación las dos partes lógicamente distintas del problema:

1. **existencia:** hay al menos una completación ordenada de $\mathbb Q$;
2. **unicidad estructural:** cualesquiera dos completaciones están unidas por un único isomorfismo de cuerpos ordenados compatible con sus copias racionales.

La primera parte fue obtenida concretamente mediante el modelo de Dedekind. La segunda es exactamente el contenido de §12.7. Su combinación permite formular por fin la caracterización que estaba detrás de toda la Parte I.

### Teorema 12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$

Existe una completación ordenada de $\mathbb Q$. Más precisamente,

$$
\boxed{
(\mathbb R_D,\iota_D)
\text{ es una completación ordenada de }\mathbb Q.
}
$$

Además, si $(E,\iota_E)$ es cualquier completación ordenada de $\mathbb Q$, existe un único isomorfismo de cuerpos ordenados

$$
\Theta_E:E\longrightarrow\mathbb R_D
$$

que satisface

$$
\boxed{
\Theta_E\circ\iota_E=\iota_D.
}
$$

Ese único isomorfismo es el transporte canónico construido a partir de las trazas racionales:

$$
\boxed{
\Theta_E=\Psi_{E,\mathbb R_D}.
}
$$

Equivalentemente: la clase de las completaciones ordenadas de $\mathbb Q$ es no vacía y cualesquiera dos de sus miembros son isomorfos mediante un único isomorfismo de cuerpos ordenados que hace conmutar las correspondientes incrustaciones de $\mathbb Q$.

**Demostración.**

La existencia ya fue demostrada en Proposición 7.5.3 — El modelo de Dedekind es una completación ordenada de $\mathbb Q$, que establece que

$$
(\mathbb R_D,\iota_D)
$$

es una completación ordenada de $\mathbb Q$ en el sentido de Definición 4.8.2 — Completación ordenada de $\mathbb Q$.

Sea ahora $(E,\iota_E)$ una completación ordenada arbitraria. Podemos aplicar Teorema 12.7.2 — Unicidad del isomorfismo entre completaciones ordenadas a las dos completaciones

$$
(E,\iota_E)
\qquad\text{y}\qquad
(\mathbb R_D,\iota_D).
$$

El teorema produce un único isomorfismo de cuerpos ordenados

$$
\Theta_E:E\longrightarrow\mathbb R_D
$$

tal que

$$
\Theta_E\circ\iota_E=\iota_D,
$$

y afirma además que ese isomorfismo coincide con el transporte canónico:

$$
\Theta_E=\Psi_{E,\mathbb R_D}.
$$

Como $E$ era arbitrario, toda completación ordenada es estructuralmente idéntica al modelo de Dedekind en el sentido preciso de un único isomorfismo compatible con $\mathbb Q$.

La formulación equivalente para dos completaciones arbitrarias es precisamente Teorema 12.7.2 — Unicidad del isomorfismo entre completaciones ordenadas. ∎

El teorema anterior caracteriza primero una completación de $\mathbb Q$. Pero la arquitectura inicial del tratado formulaba la meta de manera ligeramente distinta, hablando de un cuerpo ordenado completo arquimediano. A esta altura podemos eliminar esa redundancia.

### Corolario 12.8.2 — Todo cuerpo ordenado completo realiza la completación única

Sea $E$ un cuerpo ordenado completo. Entonces su copia racional canónica

$$
\jmath_{\mathbb Q}^{E}:\mathbb Q\longrightarrow E
$$

convierte a

$$
\boxed{
(E,\jmath_{\mathbb Q}^{E})
}
$$

en una completación ordenada de $\mathbb Q$. En consecuencia, existe un único isomorfismo de cuerpos ordenados

$$
\boxed{
\Theta_E:E\longrightarrow\mathbb R_D
}
$$

que satisface

$$
\boxed{
\Theta_E\circ\jmath_{\mathbb Q}^{E}=\iota_D.
}
$$

Además, $E$ es arquimediano. Por tanto, la arquimedianidad no necesita imponerse como hipótesis independiente en el teorema de caracterización: se sigue de la completitud.

**Demostración.**

Como $E$ es un cuerpo ordenado, Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados garantiza que

$$
\jmath_{\mathbb Q}^{E}:\mathbb Q\to E
$$

es una incrustación de cuerpos ordenados. Por hipótesis, $E$ es completo. En virtud de Definición 4.8.2 — Completación ordenada de $\mathbb Q$, el par

$$
(E,\jmath_{\mathbb Q}^{E})
$$

es entonces una completación ordenada de $\mathbb Q$.

Aplicando Teorema 12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$, existe un único isomorfismo de cuerpos ordenados

$$
\Theta_E:E\to\mathbb R_D
$$

con

$$
\Theta_E\circ\jmath_{\mathbb Q}^{E}=\iota_D.
$$

Finalmente, Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano afirma que todo cuerpo ordenado completo es arquimediano. No es, pues, necesario añadir la arquimedianidad como una tercera hipótesis independiente. ∎

Este corolario da la forma intrínseca de la caracterización: una vez fijadas las operaciones, el orden total compatible y la propiedad del supremo, no queda libertad estructural. La copia de $\mathbb Q$ tampoco es un dato adicional arbitrario, pues §12.2 demostró que es canónica.

### Corolario 12.8.3 — El isomorfismo concreto de Cauchy–Dedekind es el transporte canónico

El isomorfismo

$$
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
$$

construido explícitamente en el Capítulo 11 coincide con el transporte abstracto determinado por trazas racionales:

$$
\boxed{
\Phi=\Psi_{\mathbb R_C,\mathbb R_D}.
}
$$

**Demostración.**

Proposición 10.6.1 — $(\mathbb R_C,\iota_C)$ es una completación ordenada de $\mathbb Q$ y Proposición 7.5.3 — El modelo de Dedekind es una completación ordenada de $\mathbb Q$ muestran respectivamente que

$$
(\mathbb R_C,\iota_C)
\qquad\text{y}\qquad
(\mathbb R_D,\iota_D)
$$

son completaciones ordenadas de $\mathbb Q$.

Por Teorema 11.9.4 — Isomorfismo canónico entre las completaciones de Cauchy y Dedekind, la función $\Phi$ es un isomorfismo de cuerpos ordenados y satisface

$$
\Phi\circ\iota_C=\iota_D.
$$

Pero Teorema 12.7.2 — Unicidad del isomorfismo entre completaciones ordenadas afirma que entre esas dos completaciones existe exactamente un isomorfismo con esa propiedad, y que dicho isomorfismo es

$$
\Psi_{\mathbb R_C,\mathbb R_D}.
$$

Por unicidad,

$$
\Phi=\Psi_{\mathbb R_C,\mathbb R_D}.
$$

∎

El corolario cierra el círculo entre los dos niveles del tratado. El Capítulo 11 produjo un isomorfismo mediante las codificaciones concretas de Cauchy y Dedekind; el Capítulo 12 demuestra que, una vez olvidadas esas codificaciones, ese isomorfismo no podía ser otro.

El problema de existencia y unicidad está, por tanto, resuelto. Podemos fijar ahora la convención estructural que cerrará la Parte I.
