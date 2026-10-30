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

Prepara la [copia personal indicada en la lección](../../../curriculum/00_getting_started/04_first_script/README.md#preparar-la-copia-que-vas-a-ejecutar):
carpeta propia fuera de DS Track, con `first_summary.py`. Abre ese archivo en el
editor y la terminal en esa misma carpeta. Ejecutarás y modificarás la copia;
el archivo del curso queda como referencia. Si falta Python, registra la
ejecución pendiente y retómala después de preparar el entorno en 00.05.

## Parte A — Ejecutar y explicar

1. Lee el script y predice el total sin ejecutarlo.
2. Desde tu carpeta personal, ejecútalo con el comando de tu shell.
3. Compara la salida con tu predicción e identifica entradas y transformación.

<details>
<summary>Ver solución de la parte A</summary>

El total inicial es `3 * 40 = 120` MXN. En PowerShell:

```powershell
python first_summary.py
```

En Bash/Zsh con Python disponible como `python3`:

```bash
python3 first_summary.py
```

Las entradas son producto, unidades y precio. La transformación multiplica
unidades por precio y la salida muestra esos valores y el importe calculado.

</details>

## Parte B — Cambiar las entradas

1. En tu copia personal, cambia producto a `carpeta`, unidades a `4` y precio a `25`.
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
2. Ejecuta e identifica el tipo de error, el nombre desconocido y el archivo
   y línea que señala. Usa la [guía para leerlo](../../../curriculum/00_getting_started/04_first_script/README.md#cómo-leer-ese-error)
   si lo necesitas. Distingue este intento de cualquier salida anterior.
3. Corrige, guarda y ejecuta nuevamente. Explica por qué falló.

<details>
<summary>Ver solución de la parte C</summary>

Python informa `NameError` porque `unidadess` no fue definido. La corrección es:

```python
importe_mxn = unidades * precio_unitario_mxn
```

El resultado vuelve a ser 100 MXN con las entradas de la parte B.
El nombre desconocido es `unidadess`; la ruta y la línea indican dónde revisarlo
en tu copia. El intento fallido no llega a mostrar un resumen nuevo, porque
el error ocurre antes de los `print`.

</details>

## Evidencia y reflexión

- Conserva el script modificado y anota tus entradas y resultado.
- Anota qué archivo ejecutaste y cómo comprobaste que era la copia que editabas.
- Explica por qué guardar, ejecutar y hacer commit son acciones diferentes.
- ¿Por qué `producto` usa comillas y `unidades` no?
- ¿Qué cambiaría si el precio pasara de 25 a 30? Predice y comprueba.

## Refuerzo opcional — Conservar tu cambio con Git

Si tu carpeta personal ya es un repositorio Git, aplica el flujo de la
[lección 03](../../../curriculum/00_getting_started/03_git_workflow/README.md).
Si no lo es, puedes omitir este refuerzo o prepararla con quien te acompaña,
siguiendo la [alternativa local](../../../curriculum/00_getting_started/03_git_workflow/README.md#alternativa-local-sin-github).
Trabaja en tu carpeta de práctica, fuera de repositorios ajenos. No necesitas
publicar en el repositorio compartido para completar el lab.

1. Consulta `git status` para identificar el script modificado.
2. Revisa su diferencia: ¿qué entradas cambiaste?, ¿conservaste el cálculo?
3. Prepara únicamente el script y comprueba la selección antes de registrarla.
4. Crea un commit con un mensaje que describa tu modificación.
5. Consulta el último commit y explica qué evidencia conserva de tu práctica.

<details>
<summary>Ver comandos de apoyo para el refuerzo de Git</summary>

Desde tu carpeta personal, si ya está preparada como repositorio Git:

```text
# Comprueba qué archivos cambiaron
git status
# Revisa solo el script de esta práctica
git diff -- first_summary.py
# Selecciona únicamente ese archivo
git add first_summary.py
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
Si el script es nuevo para Git, aparece como no seguido en `status`: su
contenido se revisa en el editor y, después de add, en `git diff --staged`.
Un `git diff` vacío antes de add no significa que ya esté registrado.

</details>

### Para reflexionar sobre Git

- ¿Qué te permite comprobar el diff antes de crear el commit?
- ¿El commit guarda la salida de la terminal o el cambio del archivo que preparaste?
- ¿Por qué ejecutar correctamente el script no significa que ya esté registrado en Git?
- ¿Tu commit ya aparece en GitHub si no hiciste push?

## Siguiente paso

Continúa con la [lección 05 — Entorno y dependencias](../../../curriculum/00_getting_started/05_environment/README.md)
antes de realizar su lab.
