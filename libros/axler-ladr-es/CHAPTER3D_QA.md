# QA de 3D — Invertibilidad e isomorfismos

**Fecha:** 2026-09-16. **Estado:** control del caso límite completado; revisión independiente de las 24 soluciones y cierre editorial de 3D aún pendientes.

## Testimonio y alcance

Fuente: PDF oficial de Axler, 4.ª ed., 16-08-2026, pp. 82–95. La definición **3.79** de matriz identidad supone explícitamente que `n` es un entero positivo; el ejercicio **22** supone que `v_1,…,v_n` es una base sin declarar `n≥1`. En la definición de matrices 3.29 los tamaños pueden ser no negativos. Estas tres afirmaciones no se deben fusionar silenciosamente.

## Decisión editorial MA-3D-22 (no atribuida a Axler)

1. **Interpretación estrictamente interna:** para `n≥1`, la afirmación del ejercicio 22 está bien formulada con la identidad e inversa de matrices definidas en 3.79–3.80. La equivalencia `M(T,B) invertible ⇔ T invertible` se demuestra mediante el isomorfismo de coordenadas y la compatibilidad entre composición y producto de matrices.
2. **Si `dim V=0`:** `V={0}`, su única base es la lista vacía y su único operador es simultáneamente cero e identidad, por lo que es invertible. Su matriz, de tamaño `0×0`, existe conforme a 3.29. Sin embargo, la expresión «matriz invertible» aún no está definida para `0×0` por 3.79–3.80. Por tanto, **la equivalencia del ejercicio 22 requiere una convención adicional para abarcar este caso**.
3. **Extensión opcional, claramente nuestra [NOTA]:** llamar `I_0` a la única matriz `0×0` y definirla como unidad para el producto compatible. Entonces `I_0 I_0=I_0` (igualdad vacía de entradas); la única matriz `0×0` es invertible, y la equivalencia del ejercicio 22 sigue siendo verdadera en dimensión cero. Esta extensión NO forma parte explícita de la definición 3.79 de Axler y no debe insertarse en su texto traducido como si lo fuera.

**Corrección requerida en la lectura de la solución [SOL] 22:** las identidades matriciales con `I` prueban directamente el caso `n≥1`. La frase final sobre matrices vacías debe leerse sólo bajo la nota adicional precedente; no constituye una aplicación de 3.79 al caso cero.

## Otros controles

- Se conserva la errata oficial p. 85 / 3.68, intercambio `V ↔ W` en la última línea.
- En la prueba del ejercicio 20, `p(3)` es evaluación en 3, no derivada tercera.
- Separación editorial: `TRAD` (original), `SOL` (soluciones propias), `NOTA` (convención opcional).
- No se declara `CERRADO` ni se transforma el acumulado de 165 soluciones verificadas en 189 sin segundo control independiente de las 24 nuevas.

**Checkpoint:** `3D_DIMENSION_ZERO_SCOPE_RESOLVED`; `3D_INDEPENDENT_SOLUTION_QA_PENDING`.
