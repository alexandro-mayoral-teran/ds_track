# Producto local — 14.05

31 fuentes, sin biblioteca ni resultados de otras prácticas. Datos sintéticos:
tres créditos/dos cortes. Modelos, pipeline, metadatos y lockfiles de 14.04
conservados; no hay paquetes nuevos. Lee docs/ESPECIFICACION.md.

## R, ruta principal

Abre producto_1405.Rproj, reinicia R sin workspace y confirma getwd().
Lee .Rprofile, entorno.csv, DESCRIPTION y renv.lock antes de restaurar.
R 4.6.1, renv 1.3.1 local:

```r
source("restaurar.R")
source("pruebas.R")
probar_proyecto(".")
```

## Python, alternativa

Desde esta copia, con uv y Python 3.12.12 disponibles; detente si falla un comando:

```text
uv sync --locked --no-python-downloads --cache-dir .uv-cache
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py
```

La suite contiene siete grupos: nueve criterios literales, catorce fuentes
inválidas, orden/cero, integración/repetición de dos cortes, vacío/sin universo,
duplicado fuera del corte y alteración compensada con huellas actualizadas.
Python usa unittest con subTest; R base acumula fallas por grupo y termina con
error si alguno falla. Un rechazo esperado cuenta como prueba aprobada solo si
la expectativa se cumple. Cero fallas no certifica todos los datos futuros.

## Archivos de ensayo y evidencia

Cada ejecución crea carpetas nuevas pruebas-* dentro de ensayos/, config/ y
datos/entrada/. Los resultados propios van a salidas/pruebas-*. No elimina
archivos ni modifica la fuente o configuración inicial. La prueba de alteración
cambia únicamente su propia entrega de ensayo y la deja inválida deliberadamente.
No entregues todos los ensayos como resultados válidos. Repetir la suite crea
otra tanda, sin reutilizar los casos previos. Ejecuta una suite por copia a la vez.

Para probar el producto con tu fuente real, ejecuta pipeline.py o
pipeline_proyecto(".") según 14.04: las fixtures de integración no sustituyen
validar la configuración que realmente vas a entregar. Esta muestra no acredita
exactitud financiera, cobertura completa, accesibilidad ni integración reporte/app.
No copies bibliotecas/cachés/ensayos al reconstruir. Los metadatos 1403-v1 siguen
vigentes porque el entorno no cambia. No se instalan pytest ni testthat.
