# Lab 00.02 — Terminal y rutas

## Relación

- **Módulo:** `00_getting_started`.
- **Lección:**
  [`02_terminal_paths`](../../../curriculum/00_getting_started/02_terminal_paths/).
- **Proyecto:** no aplica; prepara el entorno común del recorrido.

## Tiempo orientativo

30 a 45 minutos. No es una carrera: el objetivo es poder explicar cada
resultado.

Realiza el lab en el shell que estés usando. Las instrucciones principales
están expresadas por intención; consulta la
[tabla de equivalencias](../../../curriculum/00_getting_started/02_terminal_paths/shell-cheatsheet.md)
para PowerShell y Bash/Zsh.

Si aún no tienes un entorno local, puedes hacer primero el ensayo del
[notebook para Colab](../../../curriculum/00_getting_started/02_terminal_paths/practica_terminal_colab.ipynb).
Incluye sus propias instrucciones, carpeta temporal y CSV. Allí practicas los
conceptos de ubicación, navegación e inspección de las partes A, B y E con una
muestra distinta de la copia del repositorio. No busques `ROADMAP.md` ni
`pyproject.toml` en esa muestra. Las partes C y D del entorno personal quedan
pendientes: las herramientas de Colab corresponden a la máquina remota.
Conserva tu cuaderno con respuestas y retoma la copia real en tu equipo después.

Intenta cada parte antes de abrir su solución. Los apartados desplegables muestran
una forma de resolverla y explican el resultado; otras respuestas pueden ser válidas.

## Recorrido esencial y diagnóstico

Para comenzar, sigue **A → B → E**: ubicación, navegación y lectura del CSV.
Después vuelve a **C** para registrar herramientas disponibles o faltantes y
a **D** si Python ya está disponible. Dejar el verificador pendiente con una
nota para retomarlo en 00.05 es un resultado válido. La extensión de filtros
y sumas es opcional y no bloquea avanzar.

Si no sabes abrir la terminal en la carpeta del proyecto, sigue primero el
inicio del [recorrido PowerShell](../../../curriculum/00_getting_started/02_terminal_paths/README.md#abrir-powershell-y-situarte-en-el-proyecto)
o del [recorrido Bash/Zsh](../../../curriculum/00_getting_started/02_terminal_paths/README.md#abrir-la-terminal-y-situarte-en-el-proyecto).

## Parte A — Ubicación

1. Ve a la raíz de `ds_track`.
2. Muestra el directorio actual.
3. Lista los elementos visibles y ocultos.
4. Comprueba que existen `README.md`, `ROADMAP.md` y `pyproject.toml`.

Preguntas:

- ¿Qué diferencia observaste al incluir los elementos ocultos?
- ¿Qué devuelve la comprobación de existencia cuando cambias una letra del
  nombre?

<details>
<summary>Ver solución de la parte A — PowerShell</summary>

Abre la terminal en la carpeta donde descargaste `ds_track`. Si estás en otra
ubicación, usa `Set-Location "RUTA_REAL_DEL_PROYECTO"`, sustituyendo el marcador.

```powershell
# Comprueba la ubicación
Get-Location
# Lista el contenido visible y después incluye los elementos ocultos
Get-ChildItem
Get-ChildItem -Force
# Comprueba los archivos que identifican la raíz
Test-Path README.md
Test-Path ROADMAP.md
Test-Path pyproject.toml
```

Las tres comprobaciones devuelven `True`. `-Force` incluye elementos marcados como
ocultos; la diferencia visible depende del sistema y los atributos de los archivos.
Un nombre inexistente devuelve `False`; cambiar solo mayúsculas puede seguir
encontrando el archivo en un sistema que no distingue mayúsculas y minúsculas.

</details>

<details>
<summary>Ver solución de la parte A — Bash/Zsh</summary>

Sitúate en tu carpeta del proyecto con `cd "RUTA_REAL_DEL_PROYECTO"`.

```bash
# Comprueba la ubicación y lista los archivos
pwd
ls
# Incluye nombres que empiezan por punto y muestra detalles
ls -la
# Imprime un mensaje si cada archivo existe
test -e README.md && echo "existe"
test -e ROADMAP.md && echo "existe"
test -e pyproject.toml && echo "existe"
```

Los archivos ocultos suelen comenzar por punto. Si la ruta no existe,
`test -e` falla y no se imprime el mensaje; no muestra `False`.

</details>

## Parte B — Navegación

1. Entra a `curriculum/00_getting_started` usando una ruta relativa y el
   separador apropiado para tu shell.
2. Lista su contenido.
3. Regresa a la raíz sin escribir la ruta absoluta completa.
4. Confirma nuevamente tu ubicación.

Pregunta:

- Si estás en `curriculum/00_getting_started`, ¿qué representa subir dos veces
  a la carpeta padre (`../..` o `..\..`)?

<details>
<summary>Ver solución de la parte B — PowerShell</summary>

Desde la raíz:

```powershell
# Entra al módulo
Set-Location curriculum\00_getting_started
# Lista su contenido
Get-ChildItem
# Sube al directorio curriculum y después a ds_track
Set-Location ..\..
# Confirma que regresaste a la raíz
Get-Location
```

Cada `..` representa una carpeta padre. Subir dos veces desde el módulo te lleva
a la raíz de `ds_track`; no significa ir siempre a la raíz de la unidad.

</details>

<details>
<summary>Ver solución de la parte B — Bash/Zsh</summary>

```bash
# Desde la raíz, entra al módulo y lista su contenido
cd curriculum/00_getting_started
ls
# Sube dos carpetas y confirma la ubicación
cd ../..
pwd
```

La primera subida llega a `curriculum` y la segunda a `ds_track`.

</details>

## Parte C — Herramientas

Consulta la versión y ubicación de las herramientas disponibles. Anota cuáles
no se encuentran en tu sesión, sin instalarlas como parte de este lab:

- Python;
- `uv`;
- Git.

No es necesario que tus versiones coincidan exactamente con las de otra
persona.

<details>
<summary>Ver solución de la parte C — PowerShell</summary>

```powershell
# Consulta las versiones
python --version
uv --version
git --version
# Consulta qué comandos resolverá el shell
Get-Command python
Get-Command uv
Get-Command git
```

Las rutas y versiones dependen de tu instalación. Un comando no reconocido
indica que la herramienta no está disponible en esa sesión. Anota cuál falta;
la preparación de Python y uv se estudiará más adelante.

</details>

<details>
<summary>Ver solución de la parte C — Bash/Zsh</summary>

```bash
# Consulta las versiones
python --version
uv --version
git --version
# Localiza los comandos
command -v python
command -v uv
command -v git
```

Si Python está instalado como `python3`, comprueba `python3 --version` y
`command -v python3`. Anota la diferencia para la configuración del entorno.

</details>

## Parte D — Verificación

Python, pip y uv se explicarán más adelante. Ejecuta esta parte si Python ya
está disponible; las demás herramientas pueden faltar y el script lo informará.
Si no tienes Python, anota «verificador pendiente; retomar en 00.05» y continúa
con las rutas y el CSV. No necesitas una salida positiva para avanzar.

En PowerShell ejecuta:

```powershell
python curriculum\00_getting_started\02_terminal_paths\check_environment.py
```

Si las herramientas y la ubicación están preparadas, el resultado final será:

```text
Resultado: entorno minimo disponible.
```

En Bash o Zsh, el comando equivalente es:

```bash
python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

<details>
<summary>Ver solución y explicación de la parte D</summary>

Desde la raíz, el comando dado ejecuta el script con el Python disponible.
El script comprueba la ubicación y si están disponibles `python`, `uv` y `git`.
Si todo está preparado, termina con `Resultado: entorno minimo disponible.`

Si no aparece ese resultado, lee qué herramienta falta o si la raíz no fue
encontrada. Si tu comando es `python3`, úsalo en lugar de `python`, como indica
la lección. Eso no elimina las comprobaciones internas del script.
Que falte una herramienta es una observación del entorno, no una respuesta
incorrecta al ejercicio. Registra el pendiente y retómalo en la lección de entorno.
No instales herramientas para forzar una salida positiva en este paso.

</details>

## Parte E — Inspección de datos

1. Desde la raíz, localiza `ventas_demo.csv` dentro de la carpeta de la lección.
2. Comprueba que existe y muestra sus primeras tres líneas.
3. Identifica las columnas y explica cuántos registros viste, sin contar el encabezado.
4. Explica una tarea de datos que podrías repetir mediante un comando y qué
   necesitaría otra persona para ejecutarlo en su computadora.

<details>
<summary>Ver solución de la parte E — PowerShell</summary>

```powershell
# Lista CSV de la lección
Get-ChildItem curriculum\00_getting_started\02_terminal_paths -Filter *.csv
# Guarda la ruta de la muestra
$ventasPath = "curriculum\00_getting_started\02_terminal_paths\ventas_demo.csv"
# Confirma la existencia y muestra tres líneas
Test-Path $ventasPath
Get-Content $ventasPath -TotalCount 3
```

Las columnas son `fecha`, `producto`, `unidades` e `importe_mxn`.
Ves el encabezado y dos registros; el archivo completo contiene tres registros.
Una tarea repetible sería generar un resumen mensual. Otra persona necesitaría
el programa, los datos, las dependencias y saber desde dónde ejecutarlo.

</details>

<details>
<summary>Ver solución de la parte E — Bash/Zsh</summary>

```bash
# Lista CSV y guarda la ruta
ls curriculum/00_getting_started/02_terminal_paths/*.csv
ventas_path="curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv"
# Comprueba el archivo y muestra tres líneas
test -e "$ventas_path" && echo "existe"
head -n 3 "$ventas_path"
```

La primera línea contiene los cuatro nombres de columnas y las siguientes
dos son registros. El encabezado no es una venta. Para repetir un análisis,
comparte también sus entradas e instrucciones de ejecución.

</details>

## Extensión opcional — Explorar el CSV

Después de leer la sección 8 de la lección:

1. Cuenta las líneas y compara el resultado con la cantidad de registros.
2. Filtra las ventas de `lapiz` y comprueba el resultado en el archivo.
3. Filtra los importes de al menos 50 MXN y explica qué registros permanecen.
4. Calcula el importe total y compruébalo sumando los tres valores manualmente.
5. Prueba el reto de unidades y explica qué aporta combinar comandos.

Esta extensión no bloquea el avance. En PowerShell, compara los números
convirtiendo los campos de texto; en Bash/Zsh, aplica los ejemplos solo a la
muestra sencilla y explica su limitación para CSV más complejos.

<details>
<summary>Ver solución de la extensión — PowerShell</summary>

Desde la raíz:

```powershell
# Lee líneas de texto y cuenta: 4
$ventasPath = "curriculum\00_getting_started\02_terminal_paths\ventas_demo.csv"
Get-Content $ventasPath | Measure-Object -Line
# Importa registros y cuenta sin encabezado: 3
$ventas = @(Import-Csv $ventasPath)
$ventas.Count
# Filtra el producto: una venta, 5 unidades, 50 MXN
$ventas | Where-Object { $_.producto -eq "lapiz" }
# Filtra importes: cuaderno (80) y lapiz (50)
$ventas | Where-Object { [decimal]$_.importe_mxn -ge 50 }
# Suma importes: 165
($ventas | ForEach-Object { [decimal]$_.importe_mxn } | Measure-Object -Sum).Sum
# Reto: al menos dos unidades; quedan cuaderno y lapiz
$ventas | Where-Object { [int]$_.unidades -ge 2 }
```

La comprobación manual es `80 + 50 + 35 = 165`. Los campos del CSV son texto,
por eso se convierten antes de comparar números o sumar. Cada comando cumple
una tarea y los pipes permiten combinar lectura, filtro y resumen.

</details>

<details>
<summary>Ver solución de la extensión — Bash/Zsh</summary>

```bash
ventas_path="curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv"
# Cuenta saltos de línea: 4
wc -l < "$ventas_path"
# Cuenta registros de esta muestra sencilla: 3
awk 'NR > 1 { cantidad++ } END { print cantidad }' "$ventas_path"
# Busca la venta de lapiz
grep ',lapiz,' "$ventas_path"
# Muestra cuaderno 80 y lapiz 50
awk -F',' 'NR > 1 && $4 >= 50 { print $2, $4 }' "$ventas_path"
# Suma importes: 165
awk -F',' 'NR > 1 { total += $4 } END { print total }' "$ventas_path"
# Reto de unidades: cuaderno y lapiz
awk -F',' 'NR > 1 && $3 >= 2 { print $2, $3 }' "$ventas_path"
```

La suma manual es `80 + 50 + 35 = 165`. Estas herramientas procesan texto:
separar por comas funciona aquí, pero no interpreta CSV con comas dentro de
campos entre comillas o registros de varias líneas.

</details>

## Evidencia

Para el núcleo, conserva una nota con tu ubicación, una ruta absoluta, una
relativa y los nombres de columnas y registros que viste al leer tres líneas.
Para el diagnóstico, registra versiones/rutas encontradas y herramientas
faltantes. Si no ejecutaste el verificador, indica el motivo y retómalo en 00.05.
Los filtros y sumas no son requisitos de cierre.

Da por terminado el lab cuando puedas responder sobre lo que comprobaste,
distinguiendo los pendientes, sin probar al azar:

- ¿Cuál es la raíz del proyecto?
- ¿Desde dónde se interpreta una ruta relativa?
- ¿Cómo compruebas si un archivo existe?
- Si Python está disponible, ¿cómo sabes qué ejecutable corresponde al comando `python`? Si falta, ¿qué registraste para retomarlo?
- ¿Qué comandos anteriores pertenecen al shell y cuáles son programas externos?
- ¿Qué cambiaría si realizaras el lab en Bash o Zsh?
- ¿Qué aporta la terminal al repetir un análisis?
- ¿Por qué leer las primeras líneas de un CSV no equivale a validar sus datos?

No es necesario guardar capturas ni salidas de la terminal en Git.

## Siguiente paso

Continúa con la [lección 03 — Git: historial y actualización del perfil](../../../curriculum/00_getting_started/03_git_workflow/README.md).
Lee los conceptos y ejemplos antes de realizar su lab asociado.
