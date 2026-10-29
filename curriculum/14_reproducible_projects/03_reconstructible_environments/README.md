# 14.03 — Entornos y ejecución reconstruible

[Inicio](../../../README.md) / [Módulo 14](../README.md) / **Lección 14.03**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Reconstruir el entorno local y repetir una consulta desde fuentes explícitas |
| **Necesitas** | Contrato/configuración de 14.01–14.02; Python/uv o R/renv |
| **Evidencia** | Dos copias reconstruidas, registros nuevos y resultados conciliados |

[Empezar](#antes-de-empezar) · [Ir al lab](../../../labs/14_reproducible_projects/03_reconstructible_environments/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Una carpeta ordenada todavía puede depender de paquetes instalados en otro
proyecto o de objetos de una sesión anterior. Para reconstruir necesitamos
fuentes, configuración, herramientas declaradas y una forma explícita de
preparar el entorno y ejecutar. Copiar una carpeta de paquetes no equivale
a reconstruirla.

Ejemplo pequeño: dos ventas de 100 y 200 MXN suman 300. Obtener 300 en otro
equipo comprueba una cifra; no demuestra qué entrada, intérprete o regla se
utilizaron. Una lista de versiones tampoco demuestra que se obtuvo 300.
Aquí conservaremos ambas evidencias: entorno observado y resultado por crédito.

## Antes de empezar

- Revisa [14.01 — Contrato](../01_product_question_contract/README.md) y
  [14.02 — Configuración](../02_structure_configuration/README.md).
- Sigue [recorridos.md](recorridos.md) para una copia nueva: no requiere
  entregas personales anteriores y conserva modelo/configuración de 14.02.
- Elige una ruta: **Python 3.12.12 con uv** o **R 4.6.1 con renv 1.3.1**.
  No necesitas practicar ambas ni instalar paquetes de análisis para esta consulta.
  Preparación de gestores en [00.05](../../00_getting_started/05_environment/README.md)
  y proyecto R en [06.08](../../06_r_foundations/08_projects_renv/README.md).
- Conserva el entorno raíz, Conda/base y bibliotecas globales. Las nuevas
  bibliotecas/entornos quedan solo en copias de práctica.

## Qué vas a aprender

- Distinguir declaración de dependencias, resolución bloqueada y entorno instalado.
- Preparar un entorno nuevo desde metadatos sin copiar bibliotecas anteriores.
- Ejecutar en un proceso nuevo y comprobar el entorno realmente utilizado.
- Registrar parámetros, resultado, versiones y límites de la evidencia.
- Reconocer qué conserva un lockfile y qué herramientas externas faltan por revisar.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [preparar.py](preparar.py), [preparar.R](preparar.R), [recorridos.md](recorridos.md) | Copia explícita de 26 fuentes | Elige una ruta |
| [LEEME.md](LEEME.md) | Instrucciones autocontenidas de la copia | Esencial |
| [entorno.csv](entorno.csv) | Versiones declaradas y alcance de dependencias | Esencial |
| [pyproject.toml](entorno_python/pyproject.toml), [uv.lock](entorno_python/uv.lock), [.python-version](entorno_python/.python-version) | Proyecto Python mínimo, sin dependencias externas | Ruta Python |
| [DESCRIPTION](entorno_r/DESCRIPTION), [renv.lock](entorno_r/renv.lock), [restaurar.R](entorno_r/restaurar.R) | Proyecto R mínimo, biblioteca local con renv | Ruta R |
| [ejecutar.py](ejecutar.py), [ejecutar.R](ejecutar.R) | Consulta y registro nuevo de evidencia | Elige un lenguaje |
| [Modelo/configuración](../02_structure_configuration/README.md) y [contrato/criterios](../01_product_question_contract/README.md) | Misma fuente y reglas, sin exigir entregas previas | Se copian sin cambiar |

## 1. Tres cosas que no conviene confundir

| Capa | Qué declara o contiene | Qué no demuestra por sí sola |
| --- | --- | --- |
| Declaración | Paquetes/versiones solicitados, intérprete de referencia | Que estén instalados |
| Lockfile | Resolución de dependencias para ese proyecto | Sistema completo o ejecución correcta |
| Entorno instalado | Intérprete/biblioteca que utilizará el proceso | Que coincida con la declaración o produzca el resultado esperado |

La evidencia de ejecución debe revisar esas relaciones. La consulta actual
solo usa Python estándar o paquetes incluidos en R. Por eso el proyecto Python
declara dependencies=[]; uv.lock registra el proyecto y no añade paquetes
ficticios. El proyecto R registra solo renv como herramienta de biblioteca local;
no añade Shiny, knitr o ggplot2 por tenerlos previstos para un producto futuro.

## 2. Fuentes que viajan y entornos que se reconstruyen

El preparador reúne 26 fuentes: las trece de 14.02, con LEEME actualizado,
dos ejecutores, entorno.csv, metadatos Python/R, activador/configuración de
renv y proyecto R. No instala al copiar.

Comparte/preserva esas fuentes. No copies `.venv`, `.uv-cache`, `renv/library`,
`.renv-local` o registros anteriores para presentar una nueva reconstrucción.
Un venv suele contener referencias al intérprete y a su ubicación; recrearlo
en el destino evita asumir que moverlo es portable.

Las entradas sintéticas siguen teniendo seis filas, clave crédito/corte y saldos
enteros. Octubre/ambos/2000 selecciona 003=2600 MXN, universo tres/4600 y 100/3.
La reconstrucción no autoriza a cambiar denominadores, fuente o filtros para
forzar coincidencias.

## 3. Python: sincronizar y ejecutar con una resolución comprobada

Desde la copia preparada, en terminal:

```text
uv sync --locked --no-python-downloads --cache-dir .uv-cache
uv run --locked --no-python-downloads --cache-dir .uv-cache python ejecutar.py evidencia/python_1.csv
```

`.python-version` solicita 3.12.12 y pyproject la exige en este ejemplo.
El intérprete debe estar instalado; --no-python-downloads evita obtener otro
sin explicitarlo. --locked rechaza un proyecto que requiera actualizar el
lockfile, en vez de resolverlo silenciosamente. No edites uv.lock a mano.

Son dos controles: uv revisa los metadatos al ejecutar y el programa comprueba
versión, `.venv` de la copia y exclusión de sitios de usuario/sistema. Invocar
un Python de base puede calcular lo mismo, pero no pasa este control de entorno.
El programa no autentica que se haya invocado uv: conserva también el comando
y su resultado en tu nota personal.

uv no sustituye tu elección de gestor para el resto del curso. Si tu ruta usa
Conda/venv, conserva sus instrucciones/versiones y comprueba su reconstrucción
por separado; no mezcles gestores dentro de este .venv ni atribuyas a esas
alternativas las comprobaciones realizadas aquí con uv.

## 4. R: biblioteca local y sesión nueva

Abre producto_1403.Rproj de la copia en tu IDE, reinicia R sin workspace y
ejecuta desde su consola R:

```r
source("restaurar.R")
source("ejecutar.R")
ejecutar_reconstruible(".", "evidencia/r_1.csv")
```

El perfil/activador de renv se reutiliza de 06.08, con biblioteca y estado
locales, sin caché compartida. El lockfile real registra R 4.6.1 y renv 1.3.1.
restore reconstruye la biblioteca; status comprueba su sincronización. No
reconstruye el intérprete R ni garantiza disponibilidad futura de repositorios.

Para repetir en un proceso nuevo, después de restaurar y desde la misma copia:

```text
Rscript --vanilla -e 'source(".Rprofile"); source("ejecutar.R"); ejecutar_reconstruible(".", "evidencia/r_2.csv")'
```

--vanilla omite perfiles/workspace de arranque. Cargar después el perfil local
revisado es explícito y necesario para activar esta biblioteca. No transforma
el proceso en un contenedor ni elimina todas las variables de entorno heredadas.
El ejecutor exige versión, proyecto y biblioteca local sincronizados; no llama
a restore. Un R base sin activar puede correr el cálculo anterior, pero no pasa
este control de entorno.

## 5. Registrar lo observado sin confundirlo con autenticidad

Cada ejecutor crea un CSV nuevo bajo evidencia/, con columnas clave/valor:
versión/intérprete, raíz/biblioteca, sistema, parámetros, resultados y huellas
MD5 de entrada, configuración, declaración y lockfile de la ruta elegida.
Rechaza evidencia existente; usa otro nombre para otra ejecución.

Fechas, rutas y bibliotecas pueden diferir entre copias. Compara los mismos
parámetros, IDs/saldos, universo, medidas y huellas de entrada/configuración;
no exijas igualdad de todos los bytes del registro. Una huella sin firma no
autentica autoría, procedencia o sesiones pasadas. También pueden alterarse el
programa y el registro: conserva referencias revisadas y revisión humana.

Los registros incluyen rutas locales. Permanecen en tu copia personal y deben
revisarse antes de compartirlos. Esta escritura didáctica no garantiza una
transacción completa ni ejecución concurrente del producto.

## 6. Intérprete, paquete y herramienta externa

Quarto es una herramienta aparte de los paquetes R/Python. Si está en PATH,
el ejecutor consulta --version; si no, registra que no está disponible sin
instalarlo. Esta consulta todavía no renderiza un reporte, por eso no falla por
su ausencia. Para el reporte futuro habrá que exigir Quarto y un motor elegido,
no convertir ausencia en una preparación supuestamente comprobada.

Un lockfile no conserva sistema operativo, permisos, navegador, tipografías,
hardware ni datos fuente. La disponibilidad de paquetes/binarios también importa.
Si una versión no coincide, registra y resuelve la diferencia antes de declarar
equivalencia; no actualices archivos solo para ocultar el fallo.

## Práctica

Continúa con el [lab 14.03](../../../labs/14_reproducible_projects/03_reconstructible_environments/README.md):
preparar dos copias nuevas, reconstruir su entorno y conciliar las consultas.

## Evidencia y criterio de salida

Conserva las fuentes declaradas, comandos reales, dos registros nuevos y tu
comparación de parámetros/resultados. Explica qué proviene del lockfile y qué
debe instalarse/comprobarse fuera de él. Distingue reconstrucción de entorno,
consulta ejecutada y producto final todavía sin integrar.

## Siguiente paso

Consulta [14.04 — Pipeline y reprocesamiento](../04_pipeline_reprocessing/README.md),
ya disponible. Los registros de esta sección no implementan el pipeline,
el reporte/app ni sus checkpoints de aceptación final.

## Referencias primarias

- [uv: sincronización y bloqueo](https://docs.astral.sh/uv/concepts/projects/sync/) y [versiones de Python](https://docs.astral.sh/uv/concepts/python-versions/).
- [Python: venv](https://docs.python.org/3.12/library/venv.html): recrear entornos en su destino.
- [renv: restore](https://rstudio.github.io/renv/reference/restore.html): restauración de paquetes desde lockfile.
- [R: arranque de sesión](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Startup.html): perfiles, workspace y --vanilla.
- [Quarto: preparación](https://quarto.org/docs/get-started/): herramienta externa y editor elegido.
