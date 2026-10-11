# Lab 00.05 — Preparar y comprobar un entorno

## Relación

- Módulo: `00_getting_started`.
- Lección: [05 — Entorno y dependencias](../../../curriculum/00_getting_started/05_environment/README.md).
- Proyecto: no aplica todavía; se prepara el entorno para las próximas prácticas.

## Objetivo y tiempo orientativo

Preparar **un** entorno, identificar su intérprete y ejecutar el primer script.
Reserva 30 a 45 minutos, además de las descargas necesarias.
Si ya usas Anaconda, elige Conda; uv es una alternativa. No necesitas hacer ambos
ni crear el entorno opcional venv. Intenta antes de abrir las soluciones.

## Entrada

El proyecto y el script del lab 04. La herramienta del recorrido elegido,
instalada como explica la lección; acceso a Internet para preparar el entorno.

## Parte A — Reconocer tus herramientas

1. Identifica si usas PowerShell, CMD o Bash/Zsh.
2. Consulta la versión de Conda o uv, según tu elección.
3. Explica qué diferencia hay entre tu shell, tu editor y el intérprete Python.

<details>
<summary>Ver respuesta orientativa de la parte A</summary>

Anaconda Prompt suele usar CMD y Anaconda PowerShell Prompt usa PowerShell.
Comprueba `conda --version` o `uv --version`. El shell interpreta comandos,
VS Code edita archivos y Python ejecuta el código. Que la ventana sea de
Anaconda no significa que todos los comandos sean de Conda.

</details>

## Parte B — Preparar el entorno elegido

1. Sigue el recorrido de tu herramienta y shell en la lección.
2. Identifica el ejecutable de Python y comprueba que es 3.11 o posterior.
3. Ejecuta el script y compara la salida con las entradas que guardaste en el lab 04.
4. Explica por qué los paquetes de otro entorno pueden no estar disponibles aquí.

<details>
<summary>Ver solución orientativa — Conda</summary>

```text
# Consulta antes de crear para no repetir un entorno existente
conda env list
# Si no existe ds-track, créalo y confirma la instalación
conda create --name ds-track python=3.12 pip
# Activa y comprueba
conda activate ds-track
python -c "import sys; print(sys.executable)"
python -m pip --version
conda list
```

Entra en la raíz del proyecto con el comando de navegación de tu shell.
Después ejecuta:

```text
python curriculum/00_getting_started/04_first_script/first_summary.py
```

El Python pertenece a ds-track. La salida depende de tus valores del lab 04.
No necesitas instalar pandas ni modificar base.

</details>

<details>
<summary>Ver solución orientativa — uv</summary>

Sal de cualquier entorno Conda o venv activado y entra en la raíz del proyecto:

```text
uv sync --locked
uv run --locked python -c "import sys; print(sys.executable)"
uv run --locked python curriculum/00_getting_started/04_first_script/first_summary.py
```

El Python pertenece a `.venv`. La salida coincide con el cálculo de tu script;
no se requieren paquetes externos. No necesitas activar `.venv` para usar uv run.

</details>

## Parte C — Retomar y compartir

1. Explica cómo volverías a ejecutar el script en una sesión nueva.
2. Identifica los archivos que describen tu entorno y qué no debes subir a Git.
3. Si usas VS Code, selecciona el intérprete de tu recorrido.

<details>
<summary>Ver respuesta orientativa de la parte C</summary>

Con Conda activas ds-track, entras al proyecto y ejecutas con `python`.
Puedes exportar los requisitos elegidos con Conda a un environment.yml revisado;
no compartas rutas personales ni supongas que ese export registra paquetes de pip.

Con uv entras al proyecto y usas `uv run --locked`; pyproject.toml y uv.lock
permiten reconstruir su entorno. No subes `.venv` ni `.venv-practice`.
En VS Code seleccionas el ejecutable correspondiente; confirma la ruta cuando
cambies de herramienta.

</details>

## Evidencia y reflexión

- Anota tu recorrido, shell, versión y ruta de Python, y resultado del script.
- ¿Por qué no agregar los paquetes de tus ejercicios a base?
- ¿Configurar el intérprete en VS Code cambia todas las terminales abiertas?
- ¿Dónde instalaría un paquete `python -m pip` en tu sesión?
- ¿Qué distingue el archivo de entorno de Conda de un lockfile de uv?
- Si usas Git, comprueba que no preparaste carpetas de entornos.

## Siguiente paso

La lección 06 — Primer notebook está por desarrollar. Consulta el
[índice del nivel 0](../../../curriculum/00_getting_started/README.md).
