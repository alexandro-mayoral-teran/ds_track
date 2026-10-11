# Terminal y rutas — Recorrido en Bash/Zsh

Lee primero los conceptos de la [lección 02](README.md). Este recorrido reúne
los comandos de Unix para que puedas practicar sin alternar con PowerShell.
Parte de la raíz de `ds_track`. Las líneas con `#` explican cada paso.

## 1. Identificar tu ubicación

```bash
# Muestra el directorio actual
pwd
```

La raíz contiene `README.md`, `ROADMAP.md` y `pyproject.toml`. Su ruta absoluta
depende de dónde descargaste el proyecto, por ejemplo `/home/usuario/ds_track`.

## 2. Listar contenido

```bash
# Muestra archivos y carpetas visibles
ls

# Incluye archivos ocultos (-a) y detalles (-l)
ls -la
```

## 3. Comprobar rutas

Una ruta absoluta empieza en `/`; una relativa parte del directorio actual.
Pon entre comillas las rutas con espacios.

```bash
# Comprueba la existencia y muestra un mensaje si la ruta existe
test -e README.md && echo "existe"

# Comprueba un archivo dentro del módulo
test -e curriculum/00_getting_started/README.md && echo "existe"
```

`test -e` comprueba la existencia. `&&` ejecuta el comando siguiente solo si
esa comprobación tuvo éxito. Si la ruta no existe, estos ejemplos no imprimen
el mensaje; no devuelven `True` o `False` como `Test-Path` en PowerShell.

## 4. Cambiar de carpeta

```bash
# Entra al módulo desde la raíz
cd curriculum/00_getting_started

# Confirma la nueva ubicación
pwd

# Lista el contenido de esa carpeta
ls

# Sube dos niveles y vuelve a la raíz
cd ../..

# Comprueba que regresaste a ds_track
pwd
```

`.` representa la carpeta actual y `..` la carpeta padre.

## 5. Comprobar herramientas

```bash
# Muestra las versiones instaladas
python --version
uv --version
git --version

# Localiza el comando que el shell utilizará
command -v python
command -v uv
command -v git
```

Si tu sistema tiene Python como `python3`, usa `python3` en lugar de `python`
en los comandos directos. Anota cualquier herramienta faltante para preparar el entorno.

## 6. Ejecutar el verificador

```bash
# Ejecuta el script desde la raíz del proyecto
python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

Si usas el entorno del proyecto con `uv`, esta es la alternativa:

```bash
# Ejecuta Python mediante el entorno administrado por uv
uv run python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

El verificador actual busca los comandos `python`, `uv` y `git`. Si solo existe
`python3`, puede informar que falta `python` aunque hayas podido ejecutar el script.

## 7. Inspeccionar el CSV

```bash
# Lista los archivos con extensión CSV dentro de la lección
ls curriculum/00_getting_started/02_terminal_paths/*.csv

# Comprueba que existe la muestra
test -e curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv && echo "existe"

# Muestra el encabezado y los primeros dos registros
head -n 3 curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv
```

El archivo tiene tres registros y un encabezado. Leer las líneas no valida los datos.

## 8. Extensión opcional: filtrar y resumir

En un shell Unix puedes combinar herramientas de texto. Desde la raíz:

```bash
ventas_path="curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv"
# Cuenta saltos de línea, incluido el encabezado: 4
wc -l < "$ventas_path"
# Busca la línea de la venta de lápices
grep ',lapiz,' "$ventas_path"
# Omite el encabezado y muestra producto e importe para ventas de al menos 50
awk -F',' 'NR > 1 && $4 >= 50 { print $2, $4 }' "$ventas_path"
# Suma los importes de los registros: 165
awk -F',' 'NR > 1 { total += $4 } END { print total }' "$ventas_path"
```

- `wc -l` cuenta los saltos de línea: `4` en el archivo incluido.
- `grep` encuentra la línea que contiene `,lapiz,`.
- `awk -F','` separa por comas; `NR > 1` omite el encabezado, `$2` es producto
  y `$4` es importe. Los últimos comandos muestran las dos ventas de al menos
  50 MXN y el total `165`.

Estos comandos de texto funcionan para esta muestra sencilla. `grep` busca
texto, no interpreta columnas, y separar por comas con `awk` no es un lector
general de CSV: campos entre comillas pueden contener comas o saltos de línea.
Para esos casos necesitas un lector de CSV, como los que estudiarás en Python.
Además, `wc -l` puede dar un resultado distinto si falta el salto de línea final.

## Práctica

Continúa con el [lab 00.02](../../../labs/00_getting_started/02_terminal_paths/README.md).

