# Suplemento terminológico 3D · candidato a glosario v0.11

**Estado:** `PROVISIONAL`, revisión comunitaria abierta. Complementa [GLOSARIO.md](GLOSARIO.md) v0.10; no sustituye ni elimina entradas de capítulos anteriores.

| Inglés | Español de trabajo | Criterio |
|---|---|---|
| invertible linear map | aplicación lineal invertible | $T\in\mathcal L(V,W)$ con inversa bilateral. |
| inverse | inversa | $T^{-1}$ invierte dominio y llegada. |
| one-sided inverse | inversa unilateral | Distinguir izquierda/derecha cuando sólo se conoce $ST=I$ o $TS=I$. |
| identity operator | operador identidad | $I_V$ e $I_W$ cuando haga falta desambiguar. |
| isomorphism | isomorfismo | Aplicación lineal invertible. |
| isomorphic vector spaces | espacios vectoriales isomorfos | No confundir isomorfía con igualdad conjuntista. |
| inverse linear map | aplicación lineal inversa | Teorema 3.63: la inversa de una biyección lineal también es lineal. |
| matrix of a vector | matriz de un vector | Columna de coordenadas $\mathcal M(v)$, dependiente de la base. |
| coordinate map | aplicación de coordenadas | Isomorfismo $v\mapsto\mathcal M(v)$ para una base fijada. |
| identity matrix | matriz identidad | $I_n$; Axler 3.79 la define para $n\ge1$. |
| invertible matrix | matriz invertible | Inversa multiplicativa bilateral $A^{-1}$. |
| singular matrix | matriz singular | Matriz cuadrada no invertible. |
| nonsingular matrix | matriz no singular | Sinónimo de invertible. |
| change of basis | cambio de base | Traducción entre columnas de coordenadas. |
| change-of-basis matrix | matriz de cambio de base | Especificar SIEMPRE orientación: $C=\mathcal M(I,\mathcal U,\mathcal V)$ transforma coordenadas de $\mathcal U$ a $\mathcal V$. |
| change-of-basis formula | fórmula de cambio de base | $A=C^{-1}BC$ con las bases definidas en 3.84. |
| similar matrices | matrices semejantes | Relación $A=C^{-1}BC$; precisar que $C$ es invertible. |
| left multiplication | multiplicación por la izquierda | Aplicación $\mathcal A(T)=ST$, ejercicio 17. |
| evaluation | evaluación | $p(3)$ es valor del polinomio en $3$, no derivada. |

**QA pendiente / caso frontera:** en 3.79 Axler define matrices identidad para $n\ge1$, pero 3.70 admite espacios de dimensión $0$. Para generalizar el Ejercicio 22 a $V=\{0\}$, debe fijarse explícitamente si la edición incorpora la matriz vacía $0\times0$ con identidad única; sin esa convención, interpretar el ejercicio para $n\ge1$. No alterar la definición de Axler silenciosamente.

**Control de fuente:** la errata oficial p. 85 enuncia el intercambio $V\leftrightarrow W$ en la última línea de 3.68, corregido en el PDF canónico fechado 16-08-2026. Se registra como errata del original, no como innovación de Matemática Abierta.
