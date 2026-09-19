# Suplemento terminológico 3E · Productos y cocientes

**Estado:** propuestas `PROVISIONAL` para integración en el glosario general después de QA y revisión comunitaria; no se cambia todavía el número de versión v0.10 del glosario principal. Fuente: Axler 4.ª ed., §3E, pp. 96–104.

| Inglés | Español de trabajo | Precisión |
|---|---|---|
| product of vector spaces | producto de espacios vectoriales | Producto cartesiano con estructura componente a componente, $V_1\times\cdots\times V_m$. |
| Cartesian product | producto cartesiano | Estructura subyacente como conjuntos; no equiparar a suma interna. |
| factor | factor | Cada $V_k$ del producto. |
| slot | componente / posición | Para la posición $k$ de una tupla del producto; seleccionar según contexto. |
| projection onto a factor | proyección sobre un factor | Aplicación $(v_1,\dots,v_m)\mapsto v_k$; no confundir con proyección de 3B como operador idempotente. |
| direct sum | suma directa | La suma de subespacios internos $V_1\oplus\cdots\oplus V_m$, no literalmente igual al producto externo en general. |
| translate | trasladado | El conjunto $v+U$; se evita llamar «traslación» al conjunto, reservando esa palabra para la operación geométrica. |
| quotient space | espacio cociente | $V/U$: conjunto de todos los trasladados de un subespacio $U$, provisto de operaciones bien definidas. |
| coset | clase lateral / clase | Término de comparación; Axler desarrolla el concepto mediante *translate*, no hay que añadirlo a la voz del autor si no aparece. |
| representative | representante | Un vector $v$ que determina la clase $v+U$; no es único. |
| well defined | bien definida | La operación debe ser independiente del representante. |
| quotient map | aplicación cociente | $\pi(v)=v+U$; en prosa puede emplearse «proyección cociente» con cuidado. |
| induced linear map | aplicación lineal inducida | $\widetilde T:V/\operatorname{null}T\to W$; no es por definición una aplicación de llegada $\operatorname{range}T$, aunque se convierte en isomorfismo al restringir la llegada a esa imagen. |
| graph of a function | gráfica de una función | Subconjunto $\{(v,Tv):v\in V\}$ de $V\times W$. |
| affine combination | combinación afín | [SOL/NOTA] Combinación cuyos coeficientes suman uno; herramienta explícita en el ejercicio 12. |
| affine subspace | subespacio afín | [SOL/NOTA] Trasladado de un subespacio lineal; no interpolar esta nomenclatura como parte literal del texto de Axler. |
| finitely supported sequence | sucesión de soporte finito | Sucesión con solo un número finito de entradas no nulas, Ej. 11. |

**Decisiones de continuidad:** en fórmulas conservar $\operatorname{null}T$ y $\operatorname{range}T$; en prosa «espacio nulo» e «imagen». El rango (*rank*) de una matriz no debe confundirse con *range*. El isomorfismo de 3.107 no debe presentarse como igualdad literal de $V/\operatorname{null}T$ y $\operatorname{range}T$. No añadir hipótesis de finitud al ejercicio 13 ni al teorema 3.107.