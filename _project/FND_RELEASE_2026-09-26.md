# Primera entrega de Fundamentos para matemáticos

Propuesta de publicación progresiva de la Parte I: C01 v02, C02 v05, C03 v08 y C04 v11. El libro mantiene once capítulos y cuatro apéndices previstos; esta entrega comprende cuatro capítulos completos y 51 ejercicios finales con soluciones.

## Exportación

La fuente editorial es el manuscrito Markdown de la bóveda FND. El manifiesto `FND_EXPORT_2026-09-26.json` conserva nombres, versiones, hashes SHA-256 de las copias utilizadas y correspondencia entre IDs editoriales y públicos. La transformación sustituye los metadatos administrativos, elimina el H1 que duplica el título de Quarto y añade navegación; conserva el cuerpo matemático. Las erratas se corrigen primero en la fuente y después se actualizan el derivado y su hash.

IDs: libro `MA-BOK-FND-01` → `MA-BOK-0008`; C01–C04 `MA-BCH-FND-01-001`–`004` → `MA-BCH-0078`–`0081`. Verificar que los alias siguen libres en main antes de integrar si otra entrega editorial se ha adelantado.

## Validación

- Quarto 1.10.18: render completo de 203 páginas con salida 0; render dirigido de las ocho páginas de contenido y navegación, sin advertencias. El render completo informa advertencias en contenidos anteriores de Física y Álgebra, fuera de esta entrega.
- Cuerpos de los cuatro capítulos comparados con la fuente; enlaces locales y anclas de las cinco páginas nuevas comprobados.
- Catálogo: cinco entradas FND presentes, identificadores únicos; siete tests del generador aprobados.
- Controles existentes del flujo Quarto Check: seis pruebas del laboratorio triangular, comprobaciones JavaScript y QA estático de Cauchy–Schwarz aprobados.
- QA matemático de C04: revisión de diez secciones y quince pares ejercicio–solución; controles finitos auxiliares sobre 499 funciones, 193106 comparaciones y 31 relaciones. No sustituyen las demostraciones.
- Fuentes de contraste y coincidencias de motivos estándar declaradas en el expediente editorial; nota bibliográfica accesible desde cada capítulo.
- Chrome/MathJax: 3477 expresiones compuestas sin errores en C01–C04; página sin desbordamiento horizontal en escritorio (1440 px) y móvil (390 px). La tabla de §4.7 utiliza un contenedor desplazable accesible por teclado. Capturas de aperturas, portada y muestra interior revisadas; no se inspeccionó visualmente cada línea.

## Integración

Esta propuesta no confirma despliegue en producción. Después de integrar y completar el flujo de publicación, verificar portada, capítulo 4, navegación, fórmulas y catálogo en el dominio público; registrar entonces la URL y la versión publicadas en el estado editorial de FND.
