# QA · Sección 3E — Productos y cocientes de espacios vectoriales

**Fecha:** 2026-09-16. **Estado:** primera pasada documental y matemática terminada; segunda lectura independiente y cierre editorial pendientes.

## Fuente y estructura

- Fuente canónica: Sheldon Axler, 4.ª ed., PDF oficial de 16-08-2026, pp. 96–104.
- Numeración cotejada: 3.87–3.107, con 3.95–3.107 dedicados a cocientes.
- Banco cotejado: ejercicios **1–19**, pp. 103–104; 19 enunciados y 19 soluciones en archivos distintos.
- Errata oficial consultada el 16-09-2026: ninguna entrada específica para pp. 96–104.
- El diagrama de 3.96 se ha descrito mediante equivalente textual accesible; falta maquetación gráfica propia si se desea conservar una figura visual.

## Dependencias y casos límite

- 3.89: el producto tiene las operaciones por componentes; los ceros pertenecen a sus factores respectivos.
- 3.90: $\mathbf R^2\times\mathbf R^3$ es isomorfo, **no literalmente igual**, a $\mathbf R^5$.
- 3.93: $\Gamma$ es sobreyectiva; es inyectiva exactamente cuando la suma es directa. 3.94 requiere finitud para su argumento dimensional.
- 3.101: igualdad de clases equivale a diferencia de representantes en $U$; fundamenta que las operaciones 3.102 estén bien definidas.
- 3.103: la verificación de independencia del representante precede a los axiomas del cociente.
- 3.105: fórmula de dimensión del cociente solo bajo $\dim V<\infty$.
- 3.107(d): isomorfismo cociente–imagen **sin** hipótesis de dimensión finita.
- Ejercicios 3–5: fórmulas de isomorfía válidas sin finitud; construcción explícita de inversas.
- Ejercicio 9: prueba mediante medias y escalamiento usa $1/2\in\mathbf F$; Axler fija $\mathbf F=\mathbf R$ o $\mathbf C$. No extender la prueba a un cuerpo arbitrario de característica dos.
- Ejercicio 11(b): las clases elegidas tienen soportes infinitos y mutuamente disjuntos; cualquier combinación no trivial conserva soporte infinito, de modo que se prueba independencia **en el cociente**, no meramente en $\mathbf F^\infty$.
- Ejercicios 13, 16–19: no introducir finitud de $V$; usar bases finitas del cociente, rango de funcional no nula y factorización bien definida.
- Ejercicio 18(b): el caso $\dim(V/U)=0$ da $W=\{0\}$ y $U=V$.

## Estados de evidencia

- `TRAD`: sección y 19 enunciados incorporados en primera pasada, cotejo de numeración y formulaciones principales con fuente.
- `SOL`: **19 soluciones redactadas** y revisadas en primera lectura. No equivale aún a verificación matemática/editorial independiente.
- `NOTA`: equivalente textual de la figura 3.96 y advertencias editoriales, claramente separados del texto del autor.
- `VERIFICADO`: **no asignado todavía a 3E**.
- `CERRADO`: **no asignado**; requiere segunda lectura, fórmulas/render, control cruzado enunciado-solución y revisión comunitaria.

**Checkpoint:** `3E_FIRST_PASS_19_OF_19_DRAFTED`; `3E_SECOND_PASS_QA_PENDING`. Para 3D, el caso $0\times0$ se resuelve separadamente en `CHAPTER3D_QA.md`; esto no implica promoción automática de sus 24 soluciones.