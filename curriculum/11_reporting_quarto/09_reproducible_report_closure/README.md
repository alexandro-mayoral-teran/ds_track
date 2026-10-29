# 11.09 — Cierre del reporte reproducible

[Inicio](../../../README.md) / [Módulo 11](../README.md) / **Lección 11.09**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Entregar lectura y reconstrucción con parámetros y evidencia comprobables |
| **Necesitas** | 11.03/05/06/07; un motor y HTML, sin entregas previas |
| **Evidencia** | Fuentes reconstruidas por otra persona y reporte contrastado con referencia externa |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Lab 11.09](../../../labs/11_reporting_quarto/09_reproducible_report_closure/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-prerrequisitos-y-objetivos"></a>

## Propósito

Entregar un HTML legible es una parte del trabajo. Aquí entregarás también lo
necesario para volver a calcularlo en una carpeta nueva y contrastarlo con una
referencia independiente. Otra persona debe saber qué ejecutar, qué esperar y
qué revisar si algo falla.

## Antes de empezar

Requiere [ejecución](../03_execution_python_r/README.md),
[parámetros](../05_parameters_cutoffs/README.md),
[proyectos y ejecución](../06_projects_cache_freeze/README.md) y
[revisión visual](../07_formats_visual_review/README.md).
[Dashboards](../08_dashboard_distribution/README.md) es opcional.
No necesitas entregas anteriores: el preparador copia datos, funciones y
metadatos desde el curso. Basta **un motor y HTML**; comparar motores es ampliación.

## Qué vas a aprender

- Distinguir entrega para leer y fuentes para reconstruir.
- Declarar parámetros y sus denominadores.
- Conciliar texto, tablas y figura con una referencia independiente.
- Explicar alcance y límites de huellas y registros.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [CSV de la práctica](cartera.csv) | Consultar la entrada completa y conservar el original | Para el recorrido |
| [Preparador py](preparar.py) / [Preparador R](preparar.R) | Crear una copia nueva con las fuentes necesarias | Elige el lenguaje de tu recorrido |
| [Reporte python.qmd](reporte_python.qmd) / [Reporte r.qmd](reporte_r.qmd) | Consultar texto, tablas y figura del motor elegido | Elige el lenguaje de tu recorrido |
| [Construcción py](construir.py) / [Construcción R](construir.R) | Ejecutar la reconstrucción completa | Elige el lenguaje de tu recorrido |
| [Configuración](_quarto.yml) | Consultar proyecto y ejecución | Para el recorrido |
| [Parámetros](parametros.json) | Declarar corte y mínimo de la entrega | Para el recorrido |
| [Verificador](verificar.py) | Contrastar salida y referencia externa sin reparar | Para el recorrido |
| [Copiador de fuentes](copiar_fuentes.py) | Preparar una reconstrucción sin resultados previos | Para el recorrido |
| [Guía de fuentes](LEEME_fuentes.md) | Consultar archivos y pasos que recibe otra persona | Para el recorrido |

Consulta las fuentes aquí y trabaja en la copia nueva que prepara el recorrido.
Elige el lenguaje indicado para tu práctica; preparar el entorno y renderizar
son pasos distintos. Conserva datos, fuentes y salidas anteriores.

## Una entrega mínima, antes de ejecutar

Imagina esta entrada completa:

```csv
credito_id,fecha_corte,saldo_mxn
001,2026-09-30,1000
002,2026-09-30,2000
```

Pregunta: ¿cuántos créditos tienen saldo de al menos 2000 MXN en septiembre?
Universo: dos créditos y 3000 MXN. Selección: uno y 2000 MXN; proporción de
créditos 50%. Una entrega que solo conserva «50%» no permite averiguar si se
contaron créditos o se sumaron pesos. Conserva entrada, regla, código y unidad.
Esta mini muestra explica la idea; **no la sustituyas por el CSV de la práctica**,
cuyo contrato exige las siete observaciones siguientes.

## Datos, contrato y resultados de la práctica

[cartera.csv](cartera.csv) contiene datos ficticios propios:

| Crédito | Septiembre, MXN | Octubre, MXN |
| --- | ---: | ---: |
| 001 | 1000 | 1200 |
| 002 | 2000 | 1800 |
| 003 | 3000 | 3300 |
| 004 | Sin registro | 700 |

Cada fila representa un ID textual en una fecha exacta: `2026-09-30` o
`2026-10-31`. Se requieren exactamente estas siete claves únicas. Saldo entero
entre cero y 1000000 MXN, sin ausencias. Se valida la fuente completa antes de
seleccionar. «Sin registro» en la tabla explicativa no es un cero ni una fila
con saldo vacío.

La selección usa `saldo >= minimo_mxn`. El denominador de la proporción es el
número de créditos del corte, no todos los registros del archivo.

| Parámetros | Universo | Selección | Proporción de créditos |
| --- | --- | --- | --- |
| Septiembre, mínimo 2000 | 3 / 6000 MXN | 2 / 5000 MXN | 66.67% |
| Octubre, mínimo 2000 | 4 / 7000 MXN | 1 / 3300 MXN | 25.00% |
| Octubre, mínimo 4000 | 4 / 7000 MXN | 0 / 0 MXN | 0.00% |

Las barras universo/selección **se superponen conceptualmente**: la selección
está contenida en el universo. No sumes sus alturas como categorías excluyentes.
El gráfico comienza en cero y conserva las cantidades en una tabla.

## Qué conserva la carpeta

| Archivos | Responsabilidad |
| --- | --- |
| `cartera.csv`, `parametros.json` | Entrada y solicitud explícita |
| `reporte.qmd`, `analisis.py` o `analisis.R`, `estilos.css` | Documento, cálculo y presentación |
| `_quarto.yml`, metadatos del entorno | Ejecución y dependencias declaradas |
| `construir.py` o `construir.R` | Construcción protegida en una copia nueva |
| `reporte.html`, `salida/` | Lectura, detalle, resumen, datos de barras, PNG y versiones efectivas |
| `comando.txt`, `render.log`, `huellas.json` | Comando portable, diagnóstico y coherencia de archivos |
| `verificar.py`, `copiar_fuentes.py`, `README.md` | Comprobación, copia de fuentes e instrucciones |

La referencia para comprobar se conserva **fuera** de la entrega. Si alguien
intercambia dos saldos manteniendo el total, un resumen puede coincidir. Por eso
el verificador reconstruye valores por clave desde ese CSV externo, además de
contrastar tablas, narrativa y datos de las barras. Sus argumentos de fecha y
mínimo expresan lo que la persona revisora esperaba, independientemente del JSON.

El verificador usa solo Python estándar y no renderiza ni instala paquetes.
También sirve para la entrega R. Quien elija exclusivamente R puede realizar la
conciliación manual descrita en el lab; Python estándar facilita automatizarla.

### Parámetros y recálculo

```json
{"fecha_corte": "2026-09-30", "minimo_mxn": 2000}
```

Se permiten exactamente esas dos claves, sin repeticiones. La fecha debe ser
uno de los cortes y el mínimo numérico entero de 0 a 1000000; `true`, `"2000"`
y una clave desconocida son errores. JSON es compatible con YAML 1.2; por eso
Quarto puede recibir este archivo con `--execute-params parametros.json`.
Python usa la celda `parameters`; R usa `params`. Revisa los parámetros efectivos
en el HTML, no solo el archivo que crees haber pasado.

El proyecto desactiva caché, freeze y daemon, y la construcción pide
`--cache-refresh`. Ejecuta el documento explícito. No copia resultados viejos.
Ni esa configuración ni un log demuestran por sí solos que un HTML histórico
se calculó correctamente: la prueba es una construcción nueva y su conciliación.

## Recorrido Python — PowerShell

Desde la raíz del repositorio, con Python y uv disponibles como en
[11.03](../03_execution_python_r/README.md). Si Quarto no está en PATH, reemplaza
el valor `quarto` por su ruta completa. Comprueba primero `quarto --version`.

```powershell
python curriculum/11_reporting_quarto/09_reproducible_report_closure/preparar.py output/cierre_1109_python
$referencia = (Resolve-Path curriculum/11_reporting_quarto/09_reproducible_report_closure/cartera.csv).Path
Set-Location output/cierre_1109_python
$env:UV_PROJECT_ENVIRONMENT = "$PWD/.venv"
uv sync --locked --group notebooks --python 3.12.12
& ./.venv/Scripts/python.exe construir.py --quarto quarto
& ./.venv/Scripts/python.exe verificar.py . $referencia --fecha 2026-09-30 --minimo 2000
& ./.venv/Scripts/python.exe copiar_fuentes.py . ../cierre_1109_reconstruido --motor python
Set-Location ../cierre_1109_reconstruido
$env:UV_PROJECT_ENVIRONMENT = "$PWD/.venv"
uv sync --locked --group notebooks --python 3.12.12
& ./.venv/Scripts/python.exe construir.py --quarto quarto
& ./.venv/Scripts/python.exe verificar.py . $referencia --fecha 2026-09-30 --minimo 2000
```

Abre el segundo `reporte.html` en tu navegador. Las dos carpetas deben dar los
mismos valores; no se exige que HTML/PNG sean idénticos byte por byte entre
plataformas. El entorno se crea localmente, sin activar ni modificar Conda.
Los lockfiles son la instantánea completa del curso, no una selección mínima.

## Recorrido Python — Bash/Zsh

Desde la raíz del repositorio:

```bash
python curriculum/11_reporting_quarto/09_reproducible_report_closure/preparar.py output/cierre_1109_python
referencia="$PWD/curriculum/11_reporting_quarto/09_reproducible_report_closure/cartera.csv"
cd output/cierre_1109_python
export UV_PROJECT_ENVIRONMENT="$PWD/.venv"
uv sync --locked --group notebooks --python 3.12.12
.venv/bin/python construir.py --quarto quarto
.venv/bin/python verificar.py . "$referencia" --fecha 2026-09-30 --minimo 2000
.venv/bin/python copiar_fuentes.py . ../cierre_1109_reconstruido --motor python
cd ../cierre_1109_reconstruido
export UV_PROJECT_ENVIRONMENT="$PWD/.venv"
uv sync --locked --group notebooks --python 3.12.12
.venv/bin/python construir.py --quarto quarto
.venv/bin/python verificar.py . "$referencia" --fecha 2026-09-30 --minimo 2000
```

## Recorrido R — proyecto y consola R

Abre DS Track en el IDE. Desde la **consola R**, situada en la raíz del curso:

```r
source("curriculum/11_reporting_quarto/09_reproducible_report_closure/preparar.R")
preparar_cierre("output/cierre_1109_r")
```

Abre `output/cierre_1109_r/cierre.Rproj` y reinicia la sesión. Restaura la
biblioteca local y construye desde esa copia:

```r
source("restaurar.R")
source("construir.R", encoding = "UTF-8")
construir_reporte(quarto = "quarto")
```

La restauración puede requerir Internet y binarios de las versiones fijadas.
No inicialices renv en la raíz del curso. Si un paquete antiguo ya no dispone de
binario, revisa la disponibilidad y los diagnósticos antes de intentar compilar;
no cambies el lockfile solo para lograr que el comando termine. En la revisión
de autoría se reutilizaron archivos binarios locales previamente conservados
para arrow/duckdb; no se instalaron paquetes globales. El reporte no utiliza esos
motores, aunque la instantánea del curso los conserva.

Abre el HTML y verifica la tabla anterior. Para automatizar, en la **terminal
del sistema**, situada en esta copia (comando válido en PowerShell y Bash):

```text
python verificar.py . ../../../curriculum/11_reporting_quarto/09_reproducible_report_closure/cartera.csv --fecha 2026-09-30 --minimo 2000
python copiar_fuentes.py . ../cierre_1109_r_reconstruido --motor r
```

Abre el nuevo `.Rproj`, reinicia y repite restauración/construcción/comprobación.
No copies la biblioteca instalada como sustituto de restaurar. Si no tienes
Python, copia manualmente la lista R que devuelve `fuentes("r")` en
[verificar.py](verificar.py), conservando las subcarpetas `renv`, y concilia cada
clave, tabla, cifra y barra. Conserva evidencia de esa revisión manual.

## Un cambio deliberado y un error deliberado

Haz otra copia de fuentes y edita `parametros.json`: octubre y mínimo 4000.
Antes de construir escribe tu predicción: universo 4/7000, selección 0/0.
Construye y verifica con los argumentos correspondientes. La tabla conserva
cuatro créditos aunque no haya seleccionados; la barra seleccionada vale cero.

Para comprobar recálculo de datos, conserva una referencia nueva fuera de la
entrega, cambia allí el saldo de 003 en septiembre a 3600 y copia esa entrada
a otra carpeta nueva. Espera universo 6600 y selección 5600. Nunca alteres el
CSV original del curso. Para un error, duplica una clave de octubre aunque
solicites septiembre: debe fallar antes de producir resultados.

Las construcciones rechazan destinos iniciados. Si fallan, conserva la carpeta
y su `render.log`; corrige las fuentes y elige otro destino. No borres toda tu
carpeta de trabajo para «arreglar» un render. El preparador y copiador también
rechazan destinos existentes.

## Revisión y límites

Comprueba el HTML final sin conexión, con ventana amplia y estrecha: título,
parámetros, dos tablas, figura, referencias internas, índice y alternativas
textuales. Usa Tab y flechas en el detalle si se desborda. La tabla desplazable
no debe ensanchar toda la página. Contrasta también las etiquetas y alturas
observadas con `salida/barras.csv` y la referencia.

MD5 detecta cambios accidentales al comparar archivos; no autentica autoría.
Alguien puede alterar un archivo y recalcular su huella. El verificador detecta
varias contradicciones incluso así, pero no prueba que el código entregado sea
el que se ejecutó históricamente, ni interpreta todos los píxeles o el argumento.
La reconstrucción y la revisión humana siguen siendo necesarias. Tampoco se
certifica accesibilidad completa por superar estas comprobaciones.

<a id="práctica-criterio-de-salida-y-continuidad"></a>

## Práctica

Realiza el [lab 11.09](../../../labs/11_reporting_quarto/09_reproducible_report_closure/README.md) para
entregar fuentes, reconstruir en otra carpeta y detectar una discrepancia.

Como apoyo para preparar la actividad, consulta [preparar.py](preparar.py) o
[preparar.R](preparar.R) según el lenguaje elegido; sigue las rutas y los pasos
del recorrido completo antes de renderizar o reconstruir.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Fuentes, parámetros, HTML y resultados | Septiembre: 3/6000 y selección 2/5000; octubre: 4/7000 y 1/3300 con mínimo 2000 | Denominador de créditos del corte frente al de todo el archivo |
| Reconstrucción y nota de revisión | Otra carpeta sin resultados previos; texto, tablas y barras contra referencia externa | Huellas y registros frente a recálculo real y revisión humana |

Puedes cerrar cuando tu compañero reconstruya un reporte sin resultados
previos, explique el denominador y detecte una discrepancia sin corregir cifras
a mano. Basta un motor y HTML; comparar motores y dashboard son ampliaciones.

Quien aprende realiza la práctica y explica las decisiones; su compañero revisa.
Tu compañero cambia una cifra y su huella en una copia y pide comprobar qué contradicción aún detecta el verificador.
Guarda evidencia, ayudas y dudas en una nota personal junto a tu práctica.
PROGRESS.md registra desarrollo editorial, no tu expediente de aprendizaje.
El proyecto `05_monthly_report` y sus checkpoints siguen planificados;
las comprobaciones técnicas del material no acreditan haber completado la práctica.

<a id="referencias-primarias"></a>

## Referencias

[Ejecución de proyectos Quarto](https://quarto.org/docs/projects/code-execution.html),
[parámetros por motor](https://quarto.org/docs/computations/parameters.html),
[recursos HTML](https://quarto.org/docs/output-formats/html-basics.html) y
[compatibilidad JSON/YAML 1.2](https://yaml.org/spec/1.2.2/).
Ejemplos propios; comprobación de autoría en Windows con Quarto 1.9.38,
Python 3.12.12 y R 4.6.1. No se añaden dependencias ni se modifican lockfiles.

## Siguiente paso

Las nueve secciones de Quarto tienen material. Después del cierre, revisa los
[criterios de integración](../../../docs/reporting-closure.md). En el recorrido
numerado siguen [12 — Streamlit](../../12_streamlit/README.md) o
[13 — Shiny](../../13_shiny_web/README.md). Ambas rutas tienen sus lecciones,
labs y entrega local disponibles; basta elegir una. Revisa su cierre de
[Streamlit](../../../docs/streamlit-closure.md) o [Shiny](../../../docs/shiny-closure.md).
14.01–14.09 tienen material de diseño, estructura, entornos, reprocesamiento, pruebas, trazabilidad, integración local, entrega opcional y revisión final; la integración del portal es un trabajo separado.

[← Módulo 11](../README.md) · [Lab 11.09](../../../labs/11_reporting_quarto/09_reproducible_report_closure/README.md) · [Revisar el cierre del módulo →](../README.md#criterio-de-salida)
