# Lab 00.05 — Un entorno, tres caminos posibles

## Relación y entrada

- Lección: [05 — Teoría de entornos y dependencias](../../../curriculum/00_getting_started/05_environment/README.md).
- Recorridos: [Conda](../../../curriculum/00_getting_started/05_environment/conda.md),
  [venv + pip](../../../curriculum/00_getting_started/05_environment/venv-pip.md) o
  [uv](../../../curriculum/00_getting_started/05_environment/uv.md).
- Proyecto: no aplica todavía; practicamos con datos ficticios.

Reserva dos sesiones de 20 a 30 minutos, además de las descargas. Elige un solo
camino para ambas: sesión A después de [05A](../../../curriculum/00_getting_started/05_environment/environment.md)
y sesión B después de [05B](../../../curriculum/00_getting_started/05_environment/dependencies.md).

## Sesión A — Preparar y usar un entorno

1. Explica qué es un entorno, qué aísla y qué no protege.
2. Identifica tu shell y elige un gestor según tu instalación y necesidades.
3. Explica quién crea el entorno y quién instala sus paquetes en tu recorrido.
4. Realiza la parte A de tu recorrido y comprueba la ruta de Python.
5. Ejecuta el script de la lección 04 sin instalar tabulate todavía.
6. Si usas VS Code, selecciona ese intérprete y comprueba una terminal nueva.

<details>
<summary>Ver respuesta orientativa de la parte A</summary>

Conda administra entorno, Python y paquetes; venv crea el entorno y pip instala;
uv integra entorno y gestión del proyecto. El entorno separa paquetes de otros
proyectos, pero no es una barrera de seguridad. Si ya usas Anaconda, Conda es
un comienzo natural. El shell y el gestor son herramientas distintas.

Conda: prepara y activa ds-track. pip: crea .venv-practice y usa su Python.
uv: crea el mini proyecto y ejecuta con uv run. El primer script no necesita
bibliotecas externas. La evidencia es la ruta del intérprete y su resultado.

</details>

## Sesión B — Instalar y conservar dependencias

Lee 05B y continúa con la parte B de tu recorrido, sin crear otro entorno.

1. Selecciona el entorno de la sesión A y consulta el ejecutable de Python.
2. Instala tabulate 0.9.0 en el entorno, no en base ni en el Python global.
3. Comprueba que el intérprete importa el paquete y muestra su versión.
4. Ejecuta library_demo.py con ese entorno y revisa la tabla.

<details>
<summary>Ver comprobación — Conda</summary>

Con ds-track activado, desde la raíz:

```text
conda install -c conda-forge tabulate=0.9.0
python -c "import sys, tabulate; print(sys.executable); print(tabulate.__version__)"
python curriculum/00_getting_started/05_environment/library_demo.py
```

La ruta pertenece a ds-track. Revisa el plan de Conda antes de confirmar.

</details>

<details>
<summary>Ver comprobación — venv + pip</summary>

En PowerShell, desde la raíz:

```powershell
.\.venv-practice\Scripts\python.exe -m pip install "tabulate==0.9.0"
.\.venv-practice\Scripts\python.exe -c "import sys, tabulate; print(sys.executable); print(tabulate.__version__)"
.\.venv-practice\Scripts\python.exe curriculum\00_getting_started\05_environment\library_demo.py
```

En Bash/Zsh sustituye el ejecutable por `./.venv-practice/bin/python` y usa
barras `/` en la ruta del script. La ruta pertenece al entorno de práctica.

</details>

<details>
<summary>Ver comprobación — uv</summary>

Desde el mini proyecto .environment-practice/uv-demo creado según la guía:

```text
uv add "tabulate==0.9.0"
uv run --locked python -c "import sys, tabulate; print(sys.executable); print(tabulate.__version__)"
uv run --locked python ../../curriculum/00_getting_started/05_environment/library_demo.py
```

La ruta pertenece a .venv dentro del mini proyecto. No instales la dependencia
en el proyecto compartido de la raíz para resolver esta práctica.

</details>

La tabla debe contener tres productos e importes: cuaderno 80, lapiz 50 y
carpeta 35. No hace falta dominar el código del ejemplo todavía.

### Registrar y retomar al terminar la sesión B

1. Consulta los paquetes instalados usando tu gestor.
2. Conserva una configuración revisada: YAML de Conda, requirements.txt de pip
   o pyproject.toml y uv.lock de uv. Documenta también la versión de Python.
3. Explica qué información fija y qué limitaciones tiene tu documento.
4. En una sesión nueva, selecciona el mismo entorno y vuelve a ejecutar.

<details>
<summary>Ver respuesta orientativa de la parte C</summary>

Conda: conda list y export desde historial; el YAML recoge elecciones Conda,
no todas las versiones transitivas ni lo instalado con pip.
venv/pip: pip list, pip check y pip freeze; la lista registra lo instalado,
no un lockfile universal ni la versión del intérprete.
uv: uv tree y los archivos del mini proyecto; sync --locked permite preparar
la resolución declarada. No se comparte la carpeta del entorno.

</details>

## Evidencia y reflexión

Conserva tu elección y su motivo, la ruta de Python, la versión importada,
el resultado y una copia revisada de la configuración. No subas carpetas de
entornos ni rutas privadas. Las prácticas locales están excluidas de Git.

- ¿Qué pasaría si instalaras en un intérprete y ejecutaras con otro?
- ¿Activar cambia el código o la elección de comandos del shell?
- ¿Por qué pip por sí solo no constituye todo el recorrido de un entorno?
- ¿Qué necesitaría otra persona para reconstruir tu práctica?

## Siguiente paso

06 — Primer notebook está por desarrollar. Consulta el
[índice del nivel 0](../../../curriculum/00_getting_started/README.md).
