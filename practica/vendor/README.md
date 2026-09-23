# Dependencia local de MathJax

MA-Práctica sirve **MathJax 4.0.0** desde el mismo origen que la aplicación para evitar conexiones a un CDN durante el uso.

Los archivos generados viven en `vendor/mathjax/` y **no se versionan**. Se obtienen del paquete oficial `mathjax@4.0.0` mediante:

```powershell
npm install --prefix practica --ignore-scripts --no-audit --no-fund --no-package-lock
npm run --prefix practica vendor:mathjax
```

El script `scripts/vendor-mathjax.mjs` comprueba el nombre, la versión y la licencia declarada antes de copiar la distribución completa, incluida su licencia.

MathJax es software de terceros bajo **Apache License 2.0**. La GPL-3.0-or-later de MA-Práctica no relicencia MathJax.

No editar manualmente `vendor/mathjax/`: es un artefacto reproducible de preparación. El flujo de publicación deberá ejecutar este paso antes de copiar MA-Práctica al sitio final.
