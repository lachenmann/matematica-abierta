# MA-ART-0020 — publicación web

La solicitud expresa del autor autoriza publicar el artículo y su documento histórico de acompañamiento como páginas HTML de Quarto, derivadas de los maestros Markdown de la bóveda. Se conserva la licencia editorial del repositorio (GFDL-1.3-or-later).

| Documento | Maestro canónico | Página Quarto |
|---|---|---|
| MA-ART-0020 | `Obsidian/Vault/Matemática/Matemática Abierta/Artículos/MA-ART-0020 - Euler y el problema de Basilea.md`, v0.2.0 | `blog/euler-problema-de-basilea.qmd` |
| MA-ART-0020-HIST | `Obsidian/Vault/Matemática/Matemática Abierta/Artículos/MA-ART-0020-HIST - La prueba histórica de Euler.md`, v0.2.0 | `blog/euler-basilea-prueba-historica.qmd` |

Las huellas SHA-256 de cada instantánea Markdown constan en el front matter de su derivado. Los 75 bloques matemáticos del artículo y los 18 del acompañamiento coinciden exactamente con los maestros. La conversión añade metadatos web, enlaces recíprocos y figuras responsive; convierte el enlace Obsidian final en un enlace web y evita el título duplicado del acompañamiento. La lectura de E41 se presenta como comentario histórico, sin atribuirle carácter de traducción literal ni de edición crítica.

Las figuras de elaboración propia conservan los datos y las funciones del maestro. Incorporan variantes móviles y convierten las etiquetas tipográficas del SVG a trazados para que los símbolos se lean sin fuentes locales. El generador web y los SVG se conservan en `MA-ART-0020-assets/web/` de la bóveda. Los manifiestos MA-FIG registran su procedencia, huellas y destinos.

Validación: render con Quarto 1.10.18 de las dos páginas y del índice; comparación exacta de los bloques matemáticos; 91 pruebas MA-FIG y 43 pruebas de catálogo, manifiestos offline y smart render; preflight MA-FIG y C9 de las dos figuras. Revisión de MathJax, figuras y navegación a 1440 y 390 px. No se incrustan documentos PDF: ambos textos son HTML con navegación por secciones.
