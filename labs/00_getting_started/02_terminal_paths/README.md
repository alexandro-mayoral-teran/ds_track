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

## Parte A — Ubicación

1. Ve a la raíz de `ds_track`.
2. Muestra el directorio actual.
3. Lista los elementos visibles y ocultos.
4. Comprueba que existen `README.md`, `ROADMAP.md` y `pyproject.toml`.

Preguntas:

- ¿Qué diferencia observaste al incluir los elementos ocultos?
- ¿Qué devuelve la comprobación de existencia cuando cambias una letra del
  nombre?

## Parte B — Navegación

1. Entra a `curriculum/00_getting_started` usando una ruta relativa y el
   separador apropiado para tu shell.
2. Lista su contenido.
3. Regresa a la raíz sin escribir la ruta absoluta completa.
4. Confirma nuevamente tu ubicación.

Pregunta:

- Si estás en `curriculum/00_getting_started`, ¿qué representa subir dos veces
  a la carpeta padre (`../..` o `..\..`)?

## Parte C — Herramientas

Obtén la versión y ubicación de:

- Python;
- `uv`;
- Git.

No es necesario que tus versiones coincidan exactamente con las de otra
persona.

## Parte D — Verificación

En PowerShell ejecuta:

```powershell
uv run python curriculum\00_getting_started\02_terminal_paths\check_environment.py
```

Resultado esperado al final:

```text
Resultado: entorno minimo disponible.
```

En Bash o Zsh, el comando equivalente es:

```bash
uv run python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

## Parte E — Inspección de datos

1. Desde la raíz, localiza `ventas_demo.csv` dentro de la carpeta de la lección.
2. Comprueba que existe y muestra sus primeras tres líneas.
3. Identifica las columnas y explica cuántos registros viste, sin contar el encabezado.
4. Explica una tarea de datos que podrías repetir mediante un comando y qué
   necesitaría otra persona para ejecutarlo en su computadora.

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

## Evidencia

Da por terminado el lab cuando puedas responder sin probar al azar:

- ¿Cuál es la raíz del proyecto?
- ¿Desde dónde se interpreta una ruta relativa?
- ¿Cómo compruebas si un archivo existe?
- ¿Cómo sabes qué ejecutable corresponde al comando `python`?
- ¿Qué comandos anteriores pertenecen al shell y cuáles son programas externos?
- ¿Qué cambiaría si realizaras el lab en Bash o Zsh?
- ¿Qué aporta la terminal al repetir un análisis?
- ¿Por qué leer las primeras líneas de un CSV no equivale a validar sus datos?

No es necesario guardar capturas ni salidas de la terminal en Git.

## Siguiente paso

Continúa con la [lección 03 — Git: historial y actualización del perfil](../../../curriculum/00_getting_started/03_git_workflow/README.md).
Lee los conceptos y ejemplos antes de realizar su lab asociado.
