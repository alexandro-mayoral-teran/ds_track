# Equivalencias básicas: PowerShell y Unix

Esta tabla compara intenciones, no garantiza que ambos comandos tengan todas las
mismas opciones o produzcan exactamente el mismo tipo de resultado.

| Intención | PowerShell | Bash/Zsh |
| --- | --- | --- |
| Mostrar ubicación | `Get-Location` | `pwd` |
| Listar contenido | `Get-ChildItem` | `ls` |
| Incluir elementos ocultos | `Get-ChildItem -Force` | `ls -la` |
| Cambiar de carpeta | `Set-Location ruta` o `cd ruta` | `cd ruta` |
| Ir a la carpeta padre | `Set-Location ..` o `cd ..` | `cd ..` |
| Comprobar una ruta | `Test-Path ruta` | `test -e ruta` |
| Localizar un comando | `Get-Command python` | `command -v python` |
| Mostrar un archivo | `Get-Content archivo` | `cat archivo` |
| Mostrar tres líneas iniciales | `Get-Content archivo -TotalCount 3` | `head -n 3 archivo` |
| Listar archivos CSV | `Get-ChildItem -Filter *.csv` | `ls *.csv` |
| Crear una carpeta | `New-Item -ItemType Directory nombre` | `mkdir nombre` |
| Limpiar la pantalla | `Clear-Host` | `clear` |

## Separadores de ruta

```text
Windows: curriculum\00_getting_started\README.md
Unix:   curriculum/00_getting_started/README.md
```

En documentación compartida y comandos de Git suele preferirse `/` cuando la
herramienta lo admite.

## Variables de entorno

La sintaxis sí depende del shell:

```powershell
# PowerShell
$env:VARIABLE
$env:VARIABLE = "valor"
```

```bash
# Bash/Zsh
echo "$VARIABLE"
export VARIABLE="valor"
```

## Pipes

Ambos utilizan `|`, pero no transportan lo mismo por defecto:

```powershell
Get-ChildItem | Where-Object Length -gt 1KB
```

PowerShell pasa objetos con propiedades. En Unix, los programas normalmente
pasan texto o bytes:

```bash
ls -la | grep README
```

Estudiaremos composición de comandos después. Por ahora basta con reconocer que
copiar literalmente un pipeline entre shells puede producir resultados
distintos.

## Comandos portables de las herramientas

Estos comandos pertenecen a sus programas y normalmente no cambian de shell:

```text
git status
git log
python --version
uv --version
uv run python script.py
```

