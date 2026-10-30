# Lab 00.05 — Un entorno, tres caminos posibles

## Relación y entrada

- Lección: [05 — Teoría de entornos y dependencias](../../../curriculum/00_getting_started/05_environment/README.md).
- Recorridos: [Conda](../../../curriculum/00_getting_started/05_environment/conda.md),
  [venv + pip](../../../curriculum/00_getting_started/05_environment/venv-pip.md) o
  [uv](../../../curriculum/00_getting_started/05_environment/uv.md).
- Proyecto: no aplica todavía; practicamos con datos ficticios.

Trabaja en dos partes, con las pausas que necesites. Antes de elegir una
herramienta, estudia los conceptos comunes de
[05A](../../../curriculum/00_getting_started/05_environment/environment.md).
Después elige un solo camino para ambas partes: sesión A al finalizar 05A y
sesión B después de [05B](../../../curriculum/00_getting_started/05_environment/dependencies.md).

## Antes de elegir — Explicar el motivo

Imagina dos proyectos que necesitan versiones diferentes de una biblioteca.
Sin ejecutar comandos todavía:

1. Explica qué problema podría causar instalarlas para el mismo Python.
2. Distingue el archivo de código, el intérprete que lo ejecuta y la biblioteca
   que necesita. Explica qué aporta un entorno separado.
3. Predice si compartir solo el `.py` basta para reconstruir el trabajo.

<details>
<summary>Ver explicación orientativa</summary>

Cambiar una biblioteca en la instalación compartida puede afectar al otro
proyecto aunque su código no cambie. El archivo contiene instrucciones; un
intérprete las ejecuta con los paquetes disponibles en su entorno. Separar
entornos permite mantener conjuntos de paquetes distintos. Para reconstruir,
se necesitan también los requisitos, la versión de Python y los datos utilizados.

</details>

## Sesión A — Preparar y usar un entorno

1. Explica qué es un entorno, qué aísla y qué no protege.
2. Identifica tu shell y elige un gestor según tu instalación y necesidades.
3. Explica quién crea el entorno y quién instala sus paquetes en tu recorrido.
4. Identifica la carpeta de trabajo. Antes de ejecutar la parte A, predice dónde
   estará su Python; realiza esa parte y compara con la ruta consultada.
5. Ejecuta el script de la lección 04 sin instalar tabulate todavía.
6. Si usas VS Code, puedes utilizar el apoyo opcional de 05A para seleccionar
   ese intérprete y comprobar una terminal nueva.
7. Explica si cerrar la terminal elimina el entorno y qué tendrás que hacer
   para ejecutar el mismo script al retomar. Compruébalo en otra sesión.

<details>
<summary>Ver respuesta orientativa de la parte A</summary>

Conda administra entorno, Python y paquetes; venv crea el entorno y pip instala;
uv integra entorno y gestión del proyecto. El entorno separa paquetes de otros
proyectos, pero no es una barrera de seguridad. Si ya usas Anaconda, Conda es
un comienzo natural. El shell y el gestor son herramientas distintas.

Conda: prepara y activa ds-track. pip: crea .venv-practice y usa su Python.
uv: crea el mini proyecto y ejecuta con uv run. El primer script no necesita
bibliotecas externas. La evidencia es la ruta del intérprete y su resultado.
Cerrar la terminal conserva el entorno. Al retomar, vuelve a tu carpeta de
trabajo y activa Conda, utiliza la ruta del Python de venv o entra al mini
proyecto y usa uv run, según tu elección. Vuelve a consultar el ejecutable.

</details>

## Sesión B — Instalar y conservar dependencias

Lee 05B y continúa con la parte B de tu recorrido, sin crear otro entorno.

1. Selecciona el entorno de la sesión A y consulta el ejecutable de Python.
   Antes de instalar, explica si `import` descargaría la biblioteca por sí solo.
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
<summary>Ver respuesta orientativa del registro y la reanudación</summary>

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

### Caso para diagnosticar

Una persona instala tabulate sin errores, pero al ejecutar el script recibe
`ModuleNotFoundError: No module named 'tabulate'`. Explica qué comprobarías
primero y con qué consulta de tu recorrido. No necesitas provocar el fallo
ni instalar paquetes en otros entornos para resolver este caso.

<details>
<summary>Ver diagnóstico orientativo</summary>

Primero identificaría el Python que ejecutó el script y comprobaría si es el
mismo entorno que recibió la instalación. Consultaría `sys.executable` con
la forma de ejecución de mi recorrido y revisaría allí el paquete. El éxito
de la instalación no prueba que otro intérprete pueda importarlo.

</details>

Puedes continuar cuando el mismo entorno ejecute ambos scripts, importes
tabulate 0.9.0, obtengas la tabla esperada y expliques cómo retomar y qué
configuración conservar. Guarda dudas y el siguiente paso si falta comprobar algo.

## Siguiente paso

Continúa con la [lección 06 — Primer notebook](../../../curriculum/00_getting_started/06_first_notebook/README.md)
antes de realizar su lab.
