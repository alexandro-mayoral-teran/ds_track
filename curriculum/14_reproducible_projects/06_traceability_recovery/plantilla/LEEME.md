# Producto de práctica 14.06

33 fuentes; elige Python/uv o R/renv. Los preparadores reúnen datos, contrato,
configuración, pipeline y pruebas sin exigir entregas anteriores. Lee entorno.csv
y los metadatos del gestor antes de restaurar. Se conservan Python 3.12.12,
R 4.6.1 y renv 1.3.1, sin paquetes nuevos.

- Python: `uv sync --locked --no-python-downloads --cache-dir .uv-cache`.
  Ejecutar `uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py a01 --simular-fallo`.
- R: abre producto_1406.Rproj, reinicia sin workspace, `source("restaurar.R")`,
  `source("trazar.R")` y `trazar_proyecto(".", "a01", simular_fallo = TRUE)`.

El error anterior es deliberado: inspecciona intentos/a01/eventos.csv, el diagnóstico
y consola.txt. Conserva el temporal .pendiente-* de salidas/.
Repite sin simular y con intento a02: se crea una entrega nueva y el temporal
anterior permanece. Otro intento a03 comprueba y reutiliza la entrega existente.
Nunca repitas un identificador. El fallo final opcional ocurre después del pipeline:
una entrega puede existir aunque el intento termine con FALLO.

Cada intento crea eventos.csv y, si llega a esas etapas, consulta.csv, huellas.csv,
consola.txt y diagnóstico. No hay archivo de éxito separado: el último evento
TERMINADO registra el cierre del intento. Sin evento terminal, el estado es
indeterminado; no inventes FALLO ni éxito. Un log puede quedar incompleto si el
proceso es terminado, se corta la energía o falla el disco. No hay fsync ni
garantía de persistencia ante esos fallos. Si falla el registro del diagnóstico,
puede aparecer ese segundo error: conserva todo y revisa la consola.

Registro e intento no certifican validez actual ni autenticidad. MD5 compara
bytes, no firma archivos. Las huellas no copian ni permiten recuperar los insumos.
El pipeline compara valores actuales, contexto y huellas antes de reutilizar.
Un solo escritor por proyecto; no modificar archivos durante una ejecución.
Las redirecciones de consola son para ejecución secuencial, no para hilos o
sesiones concurrentes. No capturan toda salida nativa ni procesos externos.

No borrar ensayos, regenerar marcas a mano ni promover temporales. Para cambios
de fuente/configuración/código registrado usa una nueva salida; conserva las
anteriores. Las pruebas 14.05 siguen en pruebas.py / pruebas.R y generan sus
propios ensayos. Un resultado de prueba alterado no es una entrega válida.

Esta carpeta no integra reporte/app, servidor, CI ni recuperación automática.
Los registros contienen rutas locales y diagnósticos: revisarlos antes de compartir.
