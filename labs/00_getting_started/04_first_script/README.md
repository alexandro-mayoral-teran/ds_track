# Lab 00.04 — Ejecutar y modificar tu primer script

## Relación

- Módulo: `00_getting_started`.
- Lección: [04 — Primer script](../../../curriculum/00_getting_started/04_first_script/README.md).
- Proyecto: todavía no aplica; la evidencia es el script modificado.

## Objetivo y tiempo orientativo

Ejecutar un cálculo, modificar sus entradas y comprobar el resultado.
Reserva de 20 a 30 minutos; intenta cada parte antes de abrir la solución.

## Entrada

[first_summary.py](../../../curriculum/00_getting_started/04_first_script/first_summary.py),
un editor y Python 3 disponible. No necesitas instalar paquetes.

## Parte A — Ejecutar y explicar

1. Lee el script y predice el total sin ejecutarlo.
2. Desde la raíz del proyecto, ejecútalo con el comando de tu shell.
3. Compara la salida con tu predicción e identifica entradas y transformación.

<details>
<summary>Ver solución de la parte A</summary>

El total inicial es `3 * 40 = 120` MXN. En PowerShell:

```powershell
python curriculum\00_getting_started\04_first_script\first_summary.py
```

En Bash/Zsh con Python disponible como `python3`:

```bash
python3 curriculum/00_getting_started/04_first_script/first_summary.py
```

Las entradas son producto, unidades y precio. La transformación multiplica
unidades por precio y la salida muestra esos valores y el importe calculado.

</details>

## Parte B — Cambiar las entradas

1. Cambia producto a `carpeta`, unidades a `4` y precio a `25`.
2. Predice el resultado, guarda y ejecuta de nuevo.
3. Comprueba que todas las líneas de la salida corresponden a tus nuevas entradas.

<details>
<summary>Ver solución de la parte B</summary>

```python
producto = "carpeta"
unidades = 4
precio_unitario_mxn = 25
```

Conserva el cálculo y los `print` del archivo. El total debe ser `100` MXN.
No escribas el resultado fijo en el código: debe calcularse desde las entradas.

</details>

## Parte C — Detectar y corregir

1. Escribe `unidadess` en lugar de `unidades` solo en la línea del cálculo.
2. Ejecuta y lee el nombre y la línea que indica el error.
3. Corrige, guarda y ejecuta nuevamente. Explica por qué falló.

<details>
<summary>Ver solución de la parte C</summary>

Python informa `NameError` porque `unidadess` no fue definido. La corrección es:

```python
importe_mxn = unidades * precio_unitario_mxn
```

El resultado vuelve a ser 100 MXN con las entradas de la parte B.

</details>

## Evidencia y reflexión

- Conserva el script modificado y anota tus entradas y resultado.
- Explica por qué guardar, ejecutar y hacer commit son acciones diferentes.
- ¿Por qué `producto` usa comillas y `unidades` no?
- ¿Qué cambiaría si el precio pasara de 25 a 30? Predice y comprueba.

## Refuerzo opcional — Conservar tu cambio con Git

Si trabajas en una copia con Git, aplica el flujo de la
[lección 03](../../../curriculum/00_getting_started/03_git_workflow/README.md).
No necesitas publicar en el repositorio compartido para completar el lab.

1. Consulta `git status` para identificar el script modificado.
2. Revisa su diferencia: ¿qué entradas cambiaste?, ¿conservaste el cálculo?
3. Prepara únicamente el script y comprueba la selección antes de registrarla.
4. Crea un commit con un mensaje que describa tu modificación.
5. Consulta el último commit y explica qué evidencia conserva de tu práctica.

<details>
<summary>Ver comandos de apoyo para el refuerzo de Git</summary>

Desde la raíz de tu copia de `ds_track`:

```text
# Comprueba qué archivos cambiaron
git status
# Revisa solo el script de esta práctica
git diff -- curriculum/00_getting_started/04_first_script/first_summary.py
# Selecciona únicamente ese archivo
git add curriculum/00_getting_started/04_first_script/first_summary.py
# Comprueba todo lo preparado antes del commit
git diff --staged
git status
# Registra cuando la selección incluya solo lo que quieres conservar
git commit -m "Practica cálculo de venta con nuevas entradas"
# Comprueba el último registro del historial
git log --oneline -1
```

Si ya había otros cambios preparados, detente y revísalos antes del commit:
este registra toda la selección, no únicamente el último archivo agregado.
Adapta el mensaje al cambio que realmente hiciste.

</details>

### Para reflexionar sobre Git

- ¿Qué te permite comprobar el diff antes de crear el commit?
- ¿El commit guarda la salida de la terminal o el cambio del archivo que preparaste?
- ¿Por qué ejecutar correctamente el script no significa que ya esté registrado en Git?
- ¿Tu commit ya aparece en GitHub si no hiciste push?

## Siguiente paso

La lección 05 — Entorno y dependencias está por desarrollar. Consulta el
[índice del nivel 0](../../../curriculum/00_getting_started/README.md).
