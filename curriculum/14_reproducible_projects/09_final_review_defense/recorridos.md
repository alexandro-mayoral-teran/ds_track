# 14.09 — Reconstrucción para la revisión final

[Volver a la lección](README.md). Elige Python/Streamlit o R/Shiny; no necesitas
las dos rutas. Todos los nombres propuestos suponen carpetas nuevas. Si existen,
conserva los archivos y cambia los nombres en todos los pasos. Se reutilizan los preparadores
de 14.07: copian 53 fuentes; restaurar los entornos es una operación separada.
El proyecto conserva el nombre producto_1407.Rproj y la interfaz interfaz_1407.Rproj.
14.08 no es requisito. No se modifican modelos, fuentes ni lockfiles previos.

Antes de ejecutar, predice los casos de la [lección](README.md). Copia las tres
[plantillas personales](README.md#material-de-apoyo) a una carpeta de notas
separada de las fuentes. Completa el registro, tres decisiones y el acta al final;
las plantillas no cuentan entre las 53 fuentes. Compara manualmente las seis
filas con el [CSV original externo](../01_product_question_contract/cartera.csv).
Las rutas de resultados son nuevas; no copies salidas del autor.

La revisión de autoría registra versiones concretas; R 4.6.1, renv 1.3.1,
Python 3.12.12 y Quarto 1.9.38 son referencias comprobadas, no instaladores
incluidos. Cambiar versiones requiere revisar compatibilidad y documentarlo.

## R e IDE, recorrido principal de la ruta Shiny

Desde la raíz de DS Track, en consola R:

```r
source("curriculum/14_reproducible_projects/07_report_app_integration/preparar.R", encoding = "UTF-8")
preparar_integracion("output/cierre_1409", app = "shiny")
```

Abre producto_1407.Rproj de esa copia y reinicia R sin workspace. Lee LEEME.md,
entorno.csv, DESCRIPTION, renv.lock y .Rprofile. Confirma getwd(). Se conservan
R 4.6.1 y renv 1.3.1 locales; usa UTF-8 al guardar y cargar tus scripts.

En consola R de la **raíz de la copia**:

```r
getwd()
source("restaurar.R", encoding = "UTF-8")
source("pruebas.R", encoding = "UTF-8")
probar_proyecto(".")
source("trazar.R", encoding = "UTF-8")
trazar_proyecto(".", "oct01", "config/octubre.csv")
trazar_proyecto(".", "sep01", "config/septiembre.csv")
trazar_proyecto(".", "vacio01", "config/vacio.csv")
source("integracion.R", encoding = "UTF-8")
generar_reporte(".", "octubre", "config/octubre.csv")
renderizar_reporte(".", "octubre", "config/octubre.csv")
generar_reporte(".", "septiembre", "config/septiembre.csv")
renderizar_reporte(".", "septiembre", "config/septiembre.csv")
generar_reporte(".", "vacio", "config/vacio.csv")
renderizar_reporte(".", "vacio", "config/vacio.csv")
```

Se esperan siete grupos aprobados, tres entregas creadas y tres HTML conciliados.
Quarto 1.9.38 existente se detecta en PATH o, en Windows, en la ruta habitual de
RStudio. Si está en otra ubicación, pasa `quarto = "ruta/al/ejecutable"` a
renderizar_reporte. No se instala automáticamente. El render no ejecuta código
R: transforma el .qmd preparado. Si falla, conserva la carpeta; no ocultes el
error ni sobrescribas un HTML previo para repetir.

Abre en el navegador reportes/octubre/reporte.html, septiembre/reporte.html y
vacio/reporte.html. Revisa tabla, contexto, barras y hora de comprobación.
Para comprobar de nuevo desde una sesión nueva de la raíz:

```r
source("integracion.R", encoding = "UTF-8")
verificar_reporte(".", "octubre", "config/octubre.csv")
verificar_reporte(".", "septiembre", "config/septiembre.csv")
verificar_reporte(".", "vacio", "config/vacio.csv")
```

Estas verificaciones son de lectura; no restauran el entorno ni corrigen un
reporte. Rscript permite comprobar una sesión nueva desde terminal. Desde esa
raíz, en PowerShell con Rscript 4.6.1 disponible:

```powershell
Rscript --vanilla -e 'source(".Rprofile"); source("integracion.R", encoding="UTF-8"); verificar_reporte(".", "octubre")'
if ($LASTEXITCODE -ne 0) { throw "Revisar reporte." }
```

En Bash, alternativa completa de esa comprobación:

```bash
Rscript --vanilla -e 'source(".Rprofile"); source("integracion.R", encoding="UTF-8"); verificar_reporte(".", "octubre")' || exit 1
```

### Demostrar una falla sin cambiar el reporte válido

En el explorador del IDE o de archivos, copia la carpeta reportes/octubre a
**reportes/ensayo_saldo**, que debe ser nueva. No muevas ni reemplaces octubre.
En el editor cambia solo el saldo de 003 de 2600 a 2700 dentro de
ensayo_saldo/seleccion.csv; conserva encabezado, ID y resto de campos.
Desde la raíz de cálculo, en consola R:

```r
fallo <- tryCatch(
  verificar_reporte(".", "ensayo_saldo", "config/octubre.csv"),
  error = function(e) e
)
stopifnot(inherits(fallo, "error"))
stopifnot(grepl("Tabla del reporte distinta", conditionMessage(fallo)))
cat(conditionMessage(fallo), "\n")
verificar_reporte(".", "octubre", "config/octubre.csv")
```

Debe rechazarse la tabla alterada y aprobarse el original. Si falla por otro
motivo, registra ese problema y corrígelo antes de afirmar que el control
detectó el importe. Conserva ensayo_saldo como evidencia rechazada.

### Abrir la interfaz Shiny

Abre **interfaz/r/interfaz_1407.Rproj** en otro proyecto/sesión del IDE y reinicia
sin workspace. La biblioteca de la raíz de cálculo y la de la interfaz son
distintas. Confirma que getwd() termina en interfaz/r. Lee DESCRIPTION y
renv.lock de esta interfaz: se reutilizan los de 13.01, con Shiny 1.14.0 y
renv 1.3.1; restaurar puede descargar esos paquetes a su biblioteca local.

```r
getwd()
source("restaurar.R", encoding = "UTF-8")
source("iniciar.R", encoding = "UTF-8")
iniciar_app(puerto = 8861, abrir = TRUE)
```

Abre http://127.0.0.1:8861 si no se abre automáticamente. La consola queda ocupada
mientras sirve la app. Pulsa Detener/Esc en el IDE cuando termines. En terminal,
Ctrl+C detiene el proceso. Si el puerto está ocupado, elige otro disponible.

En el navegador:

1. Confirma que no hay cifras al abrir una sesión nueva.
2. Elige Octubre, pulsa Comprobar entrega y contrasta con su reporte.
3. Elige Septiembre sin pulsar: la vista anterior debe seguir identificada como
   octubre y aparecer un aviso de borrador distinto. Pulsa para aplicar septiembre.
4. Aplica Selección vacía: contexto válido, cero seleccionados, tabla sin filas
   y sin barras. Compara su reporte.
5. Aplica Sin universo: debe aparecer rechazo y retirarse la vista anterior.
6. Abre otra sesión/recarga: empieza sin consulta aplicada.

Repite desde una sesión nueva del IDE cargando el script completo. La revisión
de autoría con Rscript y navegador en Windows no acredita operar toda la interfaz
del IDE ni ejecutar Bash/Linux. Si renv informa paquetes base inconsistentes en
un ejecutor restringido, revisa permisos de lectura de su sandbox sin desactivar
los controles para ocultar el problema. Continúa con el [lab](../../../labs/14_reproducible_projects/09_final_review_defense/README.md).

## PowerShell y Python/Streamlit, alternativa completa

Desde DS Track, con uv/Python 3.12.12 disponibles:

```powershell
python curriculum/14_reproducible_projects/07_report_app_integration/preparar.py output/cierre_1409 --app streamlit
if ($LASTEXITCODE -ne 0) { throw "Revisar copia." }
Set-Location output/cierre_1409
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno de calculo." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py
if ($LASTEXITCODE -ne 0) { throw "Revisar pruebas." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py oct01 --config config/octubre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega de octubre." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py sep01 --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega de septiembre." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py vacio01 --config config/vacio.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega vacia." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar octubre
if ($LASTEXITCODE -ne 0) { throw "Revisar preparacion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar octubre
if ($LASTEXITCODE -ne 0) { throw "Revisar render." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar septiembre --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar preparacion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar septiembre --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar render." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar vacio --config config/vacio.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar preparacion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar vacio --config config/vacio.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar render." }
```

Abre los tres reporte.html en sus carpetas bajo reportes/. Se esperan 003/2600,
002/2000 + 003/2500 y selección vacía con universo. Para verificar el HTML de
octubre, en esta misma raíz:

```powershell
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar octubre
if ($LASTEXITCODE -ne 0) { throw "Revisar conciliacion." }
```

El render detecta Quarto existente; si hace falta, añade `--quarto` con la ruta
completa. Solo esa acción acepta la opción. No borra reportes ni instala Quarto.

### Ensayo separado, con un rechazo esperado

Copia desde el explorador reportes/octubre a **reportes/ensayo_saldo**, una
carpeta nueva. En el editor cambia solo 2600 a 2700 en la fila 003 de su
seleccion.csv. Conserva el original y el resto de archivos. Desde la raíz:

```powershell
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar ensayo_saldo
if ($LASTEXITCODE -eq 0) { throw "La alteracion debia rechazarse." }
```

Comprueba que el diagnóstico diga **Tabla del reporte distinta de la entrega**;
otro error no demuestra detección del importe. Después:

```powershell
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar octubre
if ($LASTEXITCODE -ne 0) { throw "Revisar el reporte original." }
```

Conserva el ensayo fallido y registra qué control actuó.

### Abrir Streamlit

Desde la raíz de la copia cambia al proyecto de interfaz, que tiene su propio
pyproject.toml/uv.lock. Se conservan versiones ya usadas en el curso; el lockfile
separado incluye Streamlit 1.66.1. La raíz de cálculo sigue sin paquetes externos.

```powershell
Set-Location interfaz/python
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno de interfaz." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860. Revisa inicio sin cifras; octubre; borrador de
septiembre sin aplicar; septiembre aplicado; vacío; rechazo sin universo y
sesión nueva, como en la lista del recorrido R. Compara los tres reportes.
La terminal permanece ocupada; Ctrl+C detiene la app. No se inicia un servicio
público ni se guarda la consulta en disco. Continúa con el [lab](../../../labs/14_reproducible_projects/09_final_review_defense/README.md).

## Bash y Python/Streamlit, alternativa completa

Desde DS Track, con uv/Python 3.12.12 disponibles. Este recorrido no acredita
una ejecución en Linux o macOS; las comprobaciones de autoría se hicieron en Windows.

```bash
python curriculum/14_reproducible_projects/07_report_app_integration/preparar.py output/cierre_1409 --app streamlit || exit 1
cd output/cierre_1409 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py oct01 --config config/octubre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py sep01 --config config/septiembre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py vacio01 --config config/vacio.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar octubre || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar octubre || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar septiembre --config config/septiembre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar septiembre --config config/septiembre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar vacio --config config/vacio.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar vacio --config config/vacio.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar octubre || exit 1
```

Abre los HTML de reportes/octubre, septiembre y vacio y compara con los valores
de referencia. Si Quarto está fuera de PATH, indica --quarto en renderizar.
Antes de abrir la app, copia desde el explorador reportes/octubre a
**reportes/ensayo_saldo**, destino nuevo. Cambia solo 2600 a 2700 en la fila
003 de ensayo_saldo/seleccion.csv y conserva los demás archivos.

```bash
if uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar ensayo_saldo; then
  printf '%s\n' 'La alteracion debia rechazarse.'
  exit 1
fi
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar octubre || exit 1
```

Lee el diagnóstico: debe indicar Tabla del reporte distinta de la entrega.
Un error de entorno o de ruta no cuenta como detección del saldo. Conserva
ensayo_saldo como evidencia rechazada y el original aprobado.

Después restaura e inicia solo la interfaz elegida:

```bash
cd interfaz/python || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860. Comprueba los mismos estados del recorrido R: inicio,
borrador sin aplicar, casos habitual/vacío, rechazo y sesión nueva. Ctrl+C detiene
la app. Conserva carpetas y registros; realiza el [lab](../../../labs/14_reproducible_projects/09_final_review_defense/README.md).


## Cerrar la revisión

Una vez detenida la app, completa [REVISION](plantillas/REVISION.md),
[DECISIONES](plantillas/DECISIONES.md) y [ACTA_CIERRE](plantillas/ACTA_CIERRE.md)
en tus copias personales. La persona que acompaña elige un caso y sigue contigo
el dato desde fuente y filtros hasta tabla, HTML y app. Identifiquen ayudas,
diferencias y límites. No marquen una observación como realizada por haber
copiado un comando de este documento. Continúen con el
[lab 14.09](../../../labs/14_reproducible_projects/09_final_review_defense/README.md)
y el [cierre del módulo](../../../docs/reproducible-projects-closure.md).
