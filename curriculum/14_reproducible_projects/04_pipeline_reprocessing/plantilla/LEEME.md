# Producto local — 14.04

Esta copia contiene 28 fuentes. Lee docs/ESPECIFICACION.md y config/consulta.csv.
Datos sintéticos: seis filas, tres créditos y dos cortes. Octubre con ambos
segmentos y mínimo 2000 selecciona 003/2600 MXN; universo 3/4600 MXN.

## R, ruta principal

Abre producto_1404.Rproj en tu IDE, reinicia R sin workspace y confirma getwd().
Se requiere R 4.6.1. El perfil usa renv local, sin caché compartida.

```r
source("restaurar.R")
source("pipeline.R")
pipeline_proyecto(".")
pipeline_proyecto(".") # comprueba y reutiliza; no agrega filas
```

## Python, alternativa

Desde esta carpeta, con uv y Python 3.12.12 disponibles:

```text
uv sync --locked --no-python-downloads --cache-dir .uv-cache
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py
```

Detente si falla un comando. La biblioteca estándar hace el cálculo; R solo
restaura renv 1.3.1. Los metadatos 1403-v1 se conservan porque el entorno no cambia.
No copies .venv, renv/library ni cachés al entregar fuentes. No instales paquetes globales.

## Otro corte o intento

Copia config/consulta.csv como config/septiembre.csv sin sobrescribir; cambia
corte a 2026-09-30 y salida a salidas/septiembre. R:
`pipeline_proyecto(".", "config/septiembre.csv")`; Python:
`python pipeline.py --config config/septiembre.csv` desde el entorno local.
Resultado: 002/2000 y 003/2500, universo 3/4500 y selección 2/4500 MXN.

Para ensayar un fallo, usa otro archivo de configuración y salida nuevos:
R `simular_fallo = TRUE`; Python `--simular-fallo`. Conserva el temporal .pendiente-*;
no habrá destino final. Repite sin esa opción: crea una entrega nueva sin incorporar
el temporal anterior. La opción solo se dispara al construir un destino nuevo.

Cada entrega contiene cuatro CSV. Repetir exige mismo motor, fuente, configuración
y código registrados; si algo difiere, elige otro destino. No se reemplazan salidas.
MD5 detecta cambios accidentales, no autentica al autor. Solo estados ok/vacio
se publican; sin_universo/rechazo detienen la ejecución antes de crear temporales.
No ejecutar escritores simultáneos. El renombrado final dentro de salidas reduce
la exposición de carpetas parciales, sin garantizar una transacción completa ni
recuperación frente a todas las fallas del sistema. No genera reporte ni app.
