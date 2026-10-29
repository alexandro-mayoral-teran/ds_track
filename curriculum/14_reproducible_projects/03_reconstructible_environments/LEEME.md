# Copia reconstruible de consulta — 14.03

26 fuentes, sin entorno instalado. Elige Python/uv o R/renv; no necesitas practicar
las dos alternativas. Rutas, modelo y configuración de 14.02 se conservan.
La consulta sigue usando distribución estándar, no motores de datos ni una app.
El registro de evidencia es nuevo; salidas/ sigue sin productos de reporte/app.

## Python

Revisa pyproject.toml, uv.lock, .python-version y entorno.csv. La versión de
referencia es Python 3.12.12. El proyecto no declara dependencias externas;
uv.lock contiene el proyecto, sin paquetes de análisis inventados.

Desde esta copia, en terminal:

```text
uv sync --locked --no-python-downloads --cache-dir .uv-cache
uv run --locked --no-python-downloads --cache-dir .uv-cache python ejecutar.py evidencia/python_1.csv
```

uv debe estar disponible y encontrar Python 3.12.12 instalado. Puede usarse
--python con la ruta al intérprete elegido, conservando esa decisión en la nota
personal. No se descarga Python automáticamente. No mezcles pip/Conda sobre
.venv. El ejecutor exige el .venv local, versión declarada y sitios de usuario/
sistema desactivados; no acepta ejecutar desde base aunque el cálculo pudiera correr.

--locked rechaza metadatos desactualizados; no actualices el lockfile para ocultar
una diferencia. Si falta uv/Python, revisa la preparación ya aprendida en 00.05,
sin instalar gestores o modificar base automáticamente. Esta copia está comprobada
con uv; las alternativas Conda/venv requieren sus propios metadatos y evidencia.

## R

Revisa DESCRIPTION/renv.lock/.Rprofile/renv/settings.json. Abre producto_1403.Rproj,
reinicia R sin workspace guardado y desde la consola R de la copia:

```r
source("restaurar.R")
source("ejecutar.R")
ejecutar_reconstruible(".", "evidencia/r_1.csv")
```

R 4.6.1 y renv 1.3.1 son las versiones declaradas. El lockfile solo conserva
renv, usado para crear/activar la biblioteca local; el cálculo usa paquetes
incluidos en R. No instala Shiny, ggplot2, knitr ni otros por anticipado.
La restauración puede descargar renv y usa renv/library y .renv-local de la copia,
sin caché compartida ni bibliotecas globales. No inicialices renv en la raíz del curso.
renv puede regenerar renv/activate.R con espacios/finales de línea distintos;
revisa esa diferencia sin confundirla con un cambio de las reglas del cálculo.

En un proceso nuevo de terminal, desde esta copia:

```text
Rscript --vanilla -e 'source(".Rprofile"); source("ejecutar.R"); ejecutar_reconstruible(".", "evidencia/r_2.csv")'
```

Primero debe haberse restaurado; el ejecutor verifica proyecto/biblioteca/
lockfile sincronizados y no llama a restore. .Rprofile activa el entorno; en
una copia sin preparar su activador podría necesitar obtener renv. --vanilla
evita perfiles/workspace de arranque; cargar .Rprofile aquí es una decisión
explícita después de revisarlo, no prueba de aislamiento absoluto del sistema.

## Qué comprobar

Octubre/ambos/2000: 003=2600 MXN, universo tres/4600, cobertura 100/3. Ambos
ejecutores guardan claves/valores de entorno, parámetros y resultado nuevo,
huellas de entrada/configuración/declaración/lockfile. No reemplazan un archivo
de evidencia existente; usa otro nombre después de leerlo.

Solo se admite evidencia/nombre.csv, minúsculas y nombre simple. El registro
incluye rutas locales del equipo: queda en tu copia personal, no se publica.
Quarto se consulta con --version si está en PATH; si no, se registra ausencia
sin instalar. Esta consulta no renderiza: no acredita preparación de un reporte.
Para el producto futuro, Quarto y el motor elegido serán requisitos explícitos.

La evidencia generada no autentica sesiones pasadas ni garantiza por sí sola
corrección. Las huellas detectan cambios respecto a esos bytes, sin firma.
Un registro de otra persona puede contener rutas/datos de su entorno: revisa
antes de compartir. No se garantiza escritura transaccional ni uso concurrente.

## Reconstrucción

Crea otra copia usando únicamente los 26 archivos fuente, conservando archivos
ocultos y configuración. No copies .venv, .uv-cache, renv/library, .renv-local
ni evidencia previa. Reconstruye el entorno local y repite la consulta con un
registro nuevo. Compara parámetros/resultados/huellas de entrada y configuración,
no rutas, fechas o bytes de toda la evidencia, que deben describir cada ejecución.

Un lockfile conserva paquetes/metadatos; no incluye el sistema, el intérprete
completo, permisos, fuentes del sistema o disponibilidad futura de repositorios.
Si cambia una versión, registra la diferencia y revisa el contrato antes de
afirmar reconstrucción equivalente. Pipeline e integración siguen pendientes.
