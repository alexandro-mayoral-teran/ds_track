# 11.05 — Parámetros y cortes

## Propósito, prerrequisitos y objetivos

Un reporte parametrizado conserva las reglas de cálculo y permite elegir valores
de entrada al ejecutarlo. En lugar de mantener una copia del análisis para cada
mes, usarás **el mismo documento fuente** para producir dos HTML con cortes
distintos. Cada reporte mostrará los parámetros efectivamente utilizados, su
universo, su selección y las limitaciones de compararlos.

Lee [11.03](../03_execution_python_r/README.md) y
[11.04](../04_tables_figures_references/README.md) como prerrequisitos conceptuales:
ejecución desde archivos, entornos y evidencia enlazada. Elige Python/Jupyter o
R/knitr; un motor basta. Esta sección incluye datos, reglas, parámetros y
preparadores completos; no necesita tus entregas anteriores.

Al terminar podrás distinguir parámetro, filtro y salida; definir parámetros con
la sintaxis de cada motor; generar dos reportes; comprobar tipos y fronteras;
y explicar cuándo cambia la población comparada. No se activa caché/freeze ni
se publica un sitio. El HTML es suficiente para esta práctica.

## 1. Qué cambia y qué permanece

| Elemento | En esta práctica |
| --- | --- |
| Pregunta | Qué créditos tienen saldo mayor o igual al mínimo en una fecha exacta |
| Parámetros | `fecha_corte` y `minimo_mxn` |
| Reglas constantes | Validar el archivo completo; seleccionar una fecha; aplicar `>=` |
| Universo | Todos los créditos observados en la fecha elegida |
| Selección | Subconjunto del universo que cumple el mínimo |
| Resultado | Conteos, saldos, proporción, tabla y figura |
| Nombre de salida | Identifica el archivo; no decide qué se calculó |

Un parámetro **es un dato de entrada**, no un resultado: no escribimos como
parámetro «saldo total 5000», sino el criterio con el que se debe calcular ese
total. Un filtro utiliza el valor del parámetro para elegir observaciones. El
motor sigue necesitando código que aplique esa regla: declarar una fecha no
filtra automáticamente un CSV.

Aquí `fecha_corte` significa **igualdad exacta de fecha**, no «todos los registros
hasta esa fecha». El saldo es una observación a un corte, no pagos o actividad
de todo el mes. Usar octubre en el nombre de salida tampoco cambia los datos.

La [documentación oficial de parámetros](https://quarto.org/docs/computations/parameters.html)
describe las definiciones por motor y las dos formas de pasarlos al render.

## 2. Primer ejemplo completo y pequeño

Con saldos ficticios de 1000 y 2500 MXN, un mínimo de 2000 selecciona uno;
un mínimo de 3000 selecciona ninguno. Guarda **una** versión según el motor
que preparaste. Los datos están completos dentro del documento.

Python, `minimo_python.qmd`:

````markdown
---
title: "Un umbral parametrizado"
jupyter: python3
format: html
execute:
  daemon: false
  cache: false
  error: false
---

```{python}
#| tags: [parameters]
minimo_mxn = 2000
```

```{python}
saldos = [1000, 2500]
seleccionados = [saldo for saldo in saldos if saldo >= minimo_mxn]
print(len(seleccionados))
```
````

R, `minimo_r.qmd`, dentro del proyecto renv preparado:

````markdown
---
title: "Un umbral parametrizado"
engine: knitr
params:
  minimo_mxn: 2000
format: html
execute:
  cache: false
  error: false
---

```{r}
saldos <- c(1000L, 2500L)
seleccionados <- saldos[saldos >= params$minimo_mxn]
print(length(seleccionados))
```
````

El render sin argumentos de parámetros usa el valor predeterminado y muestra
**1**. Desde la carpeta del documento, `quarto render minimo_python.qmd -P
minimo_mxn:3000 --output minimo_3000.html` (o el archivo R) debe mostrar **0**.
Es un único comando de terminal; las asignaciones de intérprete y ejecutable
se detallan en los recorridos de abajo. Conserva la carpeta `*_files` del mínimo
si mueves su HTML, porque este ejemplo no incorpora recursos.

### Por qué la sintaxis cambia entre motores

En **Python/Jupyter**, la celda con `tags: [parameters]` declara variables y sus
valores predeterminados. Quarto utiliza Papermill para insertar después una celda
que sustituye los valores solicitados. Los cálculos derivados deben ir **en una
celda posterior**, no junto a los valores predeterminados. De otro modo, una
variable derivada puede conservar un cálculo anterior a la sustitución. Esta
conducta está explicada en [Parameterize, de Papermill](https://papermill.readthedocs.io/en/latest/usage-parameterize.html).

Por ejemplo, si escribes `minimo_mxn = 2000` y `doble = minimo_mxn * 2` en la
celda de parámetros, cambiar el mínimo a 3000 no garantiza que `doble` se vuelva
6000. Calcula `doble` después de la sustitución. No reasignes luego un parámetro
al valor predeterminado, porque anularías la variante solicitada.

En **R/knitr**, los valores predeterminados se declaran en el YAML `params:` y
se leen desde la lista `params`, por ejemplo `params$minimo_mxn`. No se necesita
una celda Python etiquetada ni instalar Papermill para este recorrido. Los dos
documentos implementan la misma pregunta, cada uno con su mecanismo de ejecución.

## 3. Datos completos: el universo cambia con el corte

Una persona revisa créditos con saldo de al menos 2000 MXN en dos fechas.
Esta es toda la muestra propia [cartera.csv](cartera.csv):

```csv
credito_id,fecha_corte,saldo_mxn
001,2026-09-30,1000
002,2026-09-30,2000
003,2026-09-30,3000
001,2026-10-31,1200
002,2026-10-31,1800
003,2026-10-31,3300
004,2026-10-31,700
```

| Campo | Regla |
| --- | --- |
| `credito_id` | Texto con ceros iniciales: 001/002/003 en septiembre y 001/002/003/004 en octubre |
| `fecha_corte` | Texto ISO; exactamente los cortes 2026-09-30 y 2026-10-31 de la muestra |
| `saldo_mxn` | Pesos enteros entre 0 y 1000000, sin ausencias |

Una fila es un crédito en una fecha. La clave ID/fecha es única. El contrato
exige esas siete observaciones; **004 no tiene una observación en septiembre**.
No se crea una fila con saldo cero para aparentar una base rectangular. No se
conoce la causa de su aparición en octubre ni se deducen altas o desembolsos.

Se valida **todo el archivo antes del filtro**: un duplicado, ausencia o saldo
inválido en octubre también impide producir el reporte de septiembre. Es una
regla de esta entrega completa, no una afirmación de que cualquier consulta deba
leer todos los datos de un sistema grande. La muestra es pequeña y sintética.

### Referencia independiente para los dos reportes

Con `minimo_mxn: 2000`:

| Corte | Universo: créditos / saldo MXN | IDs seleccionados | Selección: créditos / saldo MXN | Proporción de créditos |
| --- | --- | --- | --- | --- |
| 2026-09-30 | 3 / 6000 | 002, 003 | 2 / 5000 | 2/3 = 66.67% |
| 2026-10-31 | 4 / 7000 | 003 | 1 / 3300 | 1/4 = 25.00% |

El crédito 002 con saldo **exactamente 2000** entra en septiembre porque la
regla es `>=`, no `>`. En octubre tiene 1800 y ya no cumple. El 004 pertenece al
universo de octubre, aunque no a la selección. El denominador de la proporción
es el **número de créditos de ese corte**, no siete, no el saldo y no el número
de créditos seleccionados.

Esta proporción expresa cumplimiento del criterio, no una medida de calidad o
completitud de datos. Tampoco es la proporción del saldo seleccionado: en
septiembre esa otra pregunta sería `5000/6000`, no `2/3`.

La selección pasa de 5000 a 3300 MXN, pero no son exactamente los mismos créditos.
El universo pasa de tres a cuatro y cambia la pertenencia al subconjunto. No
interpretes la diferencia como caída del saldo de una población fija ni como
efecto causal del tiempo. Para comparar los mismos IDs habría que definir y
comprobar otra pregunta con base común.

## 4. Contrato de parámetros y casos límite

| Parámetro | Valores aceptados en las funciones de esta práctica |
| --- | --- |
| `fecha_corte` | Un texto con forma YYYY-MM-DD, calendario válido y año 1900–2100; además debe ser un corte disponible en la fuente |
| `minimo_mxn` | Un número sin parte fraccionaria entre 0 y 1000000; no acepta texto, booleanos, ausencias o valores infinitos |

Un `2000.0` numérico representa un entero y se normaliza a 2000; el texto
`"2000"` se rechaza. Esto evita interpretar automáticamente entradas ambiguas.
R y Python conservan la misma regla aunque representen los números de modo distinto.

Los archivos [septiembre.yml](septiembre.yml) y [octubre.yml](octubre.yml)
usan **comillas para fechas** y un número para el mínimo:

```yaml
fecha_corte: "2026-10-31"
minimo_mxn: 2000
```

YAML no es solo texto con etiquetas: sus valores tienen tipos. Las comillas
evitan que un lector trate la fecha como otro tipo. No escribas `params:` en
estos archivos externos: contienen directamente las claves y valores que
Quarto pasará al motor. `params:` pertenece al encabezado del documento R.

Una **selección vacía** y un **corte ausente** son situaciones distintas:

- Octubre con mínimo 4000: universo 4/7000 MXN; selección 0/0; proporción 0.00%;
  IDs «ninguno». La tabla sigue mostrando los cuatro créditos, todos marcados «no».
- Noviembre: no es un corte disponible; el render debe fallar. No se declara
  que su cartera esté vacía ni que tenga saldo cero.
- Mínimo cero: incluye también saldos cero. Tener suma cero no demuestra ausencia
  de créditos ni selección vacía.

## 5. Preparación de herramientas y archivos

Python incorpora **Papermill 2.7.0** al grupo `notebooks` de
[pyproject.toml](../../../pyproject.toml) y [uv.lock](../../../uv.lock).
Quarto 1.9.38 utiliza su traductor al procesar parámetros Jupyter. Comprobar
solo que un `.qmd` renderiza sin sustituciones no demuestra que ese entorno
pueda procesar `--execute-params`.

Los requisitos anteriores de Python se conservan. R reutiliza knitr 1.52,
rmarkdown 2.32 y ggplot2 4.0.3 del proyecto renv de 11.03, **sin cambios de
DESCRIPTION/renv.lock** ni instalaciones R nuevas. Quarto/Pandoc siguen siendo
las herramientas existentes de 11.02. No se modifica Conda ni bibliotecas globales.

Los preparadores copian datos, funciones, documento y dos archivos de parámetros.
No calculan resultados ni renderizan. Las nuevas funciones [Python](analisis.py)
y [R](analisis.R) implementan el contrato de siete registros de esta sección;
las de 11.03 no servirían sin adaptar su contrato de seis registros.

## 6. Recorrido completo Python/Jupyter

El siguiente recorrido usa uv y un entorno local nuevo dentro de output. No lo
ejecutes sobre un entorno administrado por Conda/pip. Si utilizas otro gestor,
prepara los requisitos declarados con tu recorrido de
[00.05](../../00_getting_started/05_environment/README.md), dentro del entorno
del proyecto. Autoría comprobó uv, no la resolución de todos los gestores.
La sincronización puede descargar Python o paquetes si no están disponibles.

**PowerShell**, desde la raíz de DS Track:

```powershell
$quarto1105 = "quarto"
$env:UV_PROJECT_ENVIRONMENT = Join-Path $PWD "output/1105_entorno"
uv sync --locked --group notebooks --python 3.12.12
$env:QUARTO_PYTHON = Join-Path $env:UV_PROJECT_ENVIRONMENT "Scripts/python.exe"
& $env:QUARTO_PYTHON -c "import sys, papermill; print(sys.executable); print(papermill.__version__)"
& $env:QUARTO_PYTHON curriculum/11_reporting_quarto/05_parameters_cutoffs/preparar.py output/1105_python
Push-Location output/1105_python
& $quarto1105 render reporte_python.qmd --execute-params septiembre.yml --output reporte_septiembre.html
& $quarto1105 render reporte_python.qmd --execute-params octubre.yml --output reporte_octubre.html
Pop-Location
```

**Bash/Zsh**, desde la raíz:

```bash
quarto1105="quarto"
export UV_PROJECT_ENVIRONMENT="$PWD/output/1105_entorno"
uv sync --locked --group notebooks --python 3.12.12
export QUARTO_PYTHON="$UV_PROJECT_ENVIRONMENT/bin/python"
"$QUARTO_PYTHON" -c "import sys, papermill; print(sys.executable); print(papermill.__version__)"
"$QUARTO_PYTHON" curriculum/11_reporting_quarto/05_parameters_cutoffs/preparar.py output/1105_python
raiz1105="$PWD"
cd output/1105_python
"$quarto1105" render reporte_python.qmd --execute-params septiembre.yml --output reporte_septiembre.html
"$quarto1105" render reporte_python.qmd --execute-params octubre.yml --output reporte_octubre.html
cd "$raiz1105"
```

Si Quarto no está en PATH, asigna su ruta real a la variable; la de autoría es
`C:/Program Files/RStudio/resources/app/bin/quarto/bin/quarto.exe` en Windows.
No copies esa ruta a Linux/macOS. Las variables afectan la terminal actual y
sus procesos hijos, no una configuración global.

Entramos en la carpeta del documento **antes de renderizar**. Así los archivos
de parámetros, recursos y salidas quedan juntos. `Push-Location`/`Pop-Location`
entran y regresan en PowerShell; Bash conserva la ruta en `raiz1105`. Al usar
`--output` en Quarto 1.9.38 no conviene combinar un fuente en otra carpeta con
un destino relativo a la raíz: autoría encontró un fallo de recursos en esa
combinación. Los comandos comprobados evitan ese problema.

Los dos renders utilizan el mismo `.qmd` y el mismo CSV. Solo cambia el archivo
de parámetros y el nombre de salida. No vuelvas a ejecutar el preparador para
cambiar de corte: además de innecesario, rechaza el destino ya ocupado.

## 7. Recorrido completo R/knitr

Desde la raíz del repositorio, en la consola R, prepara los archivos en el
proyecto renv sincronizado de 11.03 (cambia la ruta si tiene otro nombre):

```r
source("curriculum/11_reporting_quarto/05_parameters_cutoffs/preparar.R")
preparar_parametros("output/1103_r")
```

Si no tienes ese entorno, puedes preparar uno sin entregas previas:

```r
source("curriculum/11_reporting_quarto/03_execution_python_r/preparar.R")
crear_entorno_ejecucion("output/1105_r")
source("curriculum/11_reporting_quarto/05_parameters_cutoffs/preparar.R")
preparar_parametros("output/1105_r")
```

Abre su `.Rproj` en RStudio o la carpeta en tu IDE. Reinicia R; si es un entorno
nuevo, ejecuta `source("restaurar.R")` en la consola R y comprueba
`renv::status()`. No reinicialices renv en la raíz ni reinstales paquetes si el
proyecto ya es adecuado. La preparación añade cinco archivos con nombres 11.05
y conserva los anteriores y sus metadatos; rechaza destinos ocupados.

Abre `reporte_1105.qmd` para inspeccionar parámetros y bloques. Un Render sin
argumentos utiliza los valores predeterminados del YAML: septiembre/2000.
Para producir las dos variantes explícitas, usa la **terminal del sistema** desde
la carpeta del proyecto R preparado, no la consola R:

**PowerShell:**

```powershell
$quarto1105 = "quarto"
$env:QUARTO_R = "C:/Program Files/R/R-4.6.1/bin"
& $quarto1105 render reporte_1105.qmd --execute-params septiembre_1105.yml --output reporte_1105_septiembre.html
& $quarto1105 render reporte_1105.qmd --execute-params octubre_1105.yml --output reporte_1105_octubre.html
```

**Bash/Zsh:**

```bash
quarto1105="quarto"
export QUARTO_R="$(dirname "$(command -v Rscript)")"
"$quarto1105" render reporte_1105.qmd --execute-params septiembre_1105.yml --output reporte_1105_septiembre.html
"$quarto1105" render reporte_1105.qmd --execute-params octubre_1105.yml --output reporte_1105_octubre.html
```

Usa el R real de tu equipo; comprueba antes que `Rscript` sea el elegido en Bash.
El render inicia su propia ejecución y lee `params$fecha_corte` y
`params$minimo_mxn`. No depende de haber modificado variables en la consola R.
Autoría verificó CLI en procesos nuevos, no el botón Render del IDE.

## 8. Valores predeterminados, variantes y conservación

El documento declara septiembre/2000 para que pueda ejecutarse sin argumentos.
Los archivos externos sustituyen esos valores en cada render. Una variante
que solo cambia el mínimo puede usar `-P minimo_mxn:4000`, pero conviene guardar
**ambos parámetros** en un YAML al conservar una ejecución: así no dependes de
recordar qué valor predeterminado estaba vigente. No mezcles `-P` y
`--execute-params` en esta práctica; utiliza una forma por ejecución.

Para dos o más parámetros, el YAML evita repetir reglas de comillas específicas
del shell. Un cambio en un archivo de parámetros afecta el próximo render;
abrir el HTML ya producido no recalcula nada ni cambia su fecha declarada.

**Render puede reemplazar un HTML existente.** Los nombres distintos conservan
septiembre y octubre de la primera serie; para otra serie usa una carpeta de
práctica nueva o nombres nuevos. No confundas que el preparador proteja la
carpeta con que el CLI proteja automáticamente todos los archivos de salida.
Revisa el estado del comando antes de ejecutar el siguiente paso si falla.

Conserva el CSV utilizado, funciones, `.qmd`, ambos YAML, HTML y versiones de
herramientas. El HTML incorpora la figura y recursos de lectura, no todos los
fuentes para reconstruir. Un nombre correcto ayuda a organizar; el contenido
con parámetros visibles permite comprobar lo que realmente se calculó.

## 9. Comprobaciones y errores que no conviene ocultar

Abre ambas salidas y contrasta los parámetros visibles, el universo, los IDs,
conteos, saldos, proporción, tabla y barras con la referencia de la sección 3.
La tabla muestra **todos los créditos del corte** y marca la condición; no
presenta los no seleccionados como si hubieran desaparecido del universo.
Las barras comparan saldo del universo y de la selección: no son categorías
disjuntas y no deben sumarse.

La validación de tipos se aplica a los valores que recibe el cálculo. No
supongas que un nombre de parámetro mal escrito siempre se rechaza igual en
ambos motores. Una variable adicional en Jupyter puede quedar sin utilizar,
mientras el valor predeterminado de la variable correcta sigue vigente;
knitr puede rechazar una clave que no está declarada en `params`. Comprueba los
valores visibles y el registro de render, además de la salida del comando.

| Síntoma | Revisión |
| --- | --- |
| Sigue apareciendo septiembre | Revisar archivo de parámetros, nombre de clave y uso real en el código |
| Error de Papermill | Comprobar el entorno Python que ejecuta Quarto y sincronizar el grupo notebooks actual |
| Fecha rechazada | Texto ISO entre comillas, calendario/rango y disponibilidad en la fuente |
| Mínimo rechazado | Número entero no negativo, no texto/booleano; unidad MXN, sin separadores de miles |
| Cero seleccionados | Distinguir selección vacía válida de corte ausente o entrada inválida |
| Cambia el universo inesperadamente | Revisar igualdad de fecha, IDs y denominador; no usar todas las filas del archivo |
| Error de recursos al cambiar salida | Entrar en la carpeta del documento y utilizar el nombre de salida allí |
| Un HTML previo sigue abriendo después de fallar | No atribuirlo a un render nuevo exitoso |

## Práctica, criterio de salida y siguiente paso

Realiza el [lab 11.05](../../../labs/11_reporting_quarto/05_parameters_cutoffs/README.md).
Puedes generar las dos variantes sin editar el cálculo, comprobar sus universos,
explicar la frontera inclusiva y conservar evidencia suficiente para repetirlas.
Registra resultados y dudas en [PROGRESS.md](../../../PROGRESS.md).
`05_monthly_report` y sus checkpoints siguen pendientes en
[proyectos](../../../projects/README.md); el material no acredita aprendizaje.
Siguiente: [11.06 — Proyectos, caché y freeze](../README.md#06-proyectos-cache-y-freeze),
todavía planificada.

## Referencias primarias y alcance

Consultadas el 2026-10-23: [Quarto Parameters](https://quarto.org/docs/computations/parameters.html),
[Papermill Parameterize](https://papermill.readthedocs.io/en/latest/usage-parameterize.html),
[Using Python](https://quarto.org/docs/computations/python.html),
[Using R](https://quarto.org/docs/computations/r.html).
Datos y ejemplos propios. Autoría: Quarto 1.9.38/Pandoc 3.8.3, Python 3.12.12,
Papermill 2.7.0 y R 4.6.1/knitr 1.52. Son versiones comprobadas, no una afirmación
de actualidad universal. Bash/Zsh son recorridos de apoyo; no se certifican otros
sistemas, la interfaz del IDE ni accesibilidad completa del HTML.
