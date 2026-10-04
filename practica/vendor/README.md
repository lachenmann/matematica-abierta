# Dependencias locales de MathJax

MA-Práctica sirve **MathJax 4.0.0** y la fuente **@mathjax/mathjax-newcm-font 4.0.0** desde el mismo origen que la aplicación para evitar conexiones a un CDN durante el uso.

Los archivos generados viven en:

- `vendor/mathjax/`
- `vendor/mathjax-newcm-font/`

y **no se versionan**. Se obtienen de los paquetes npm oficiales, fijados exactamente a 4.0.0, mediante:

```powershell
npm install --prefix practica --ignore-scripts --no-audit --no-fund --no-package-lock
npm run --prefix practica vendor:mathjax
```

El script `scripts/vendor-mathjax.mjs` comprueba nombre, versión y licencia declarada antes de copiar las distribuciones. El paquete npm de NewCM 4.0.0 declara Apache-2.0 pero no incorpora un archivo `LICENSE`; durante la preparación se añade al artefacto una copia íntegra del texto Apache-2.0 incluido por MathJax 4.0.0.

MathJax y NewCM son componentes de terceros bajo **Apache License 2.0**. La GPL-3.0-or-later de MA-Práctica no los relicencia.

No editar manualmente los directorios generados: son artefactos reproducibles. El flujo de publicación deberá ejecutar este paso antes de copiar MA-Práctica al sitio final y después repetir la prueba de tráfico del navegador.
