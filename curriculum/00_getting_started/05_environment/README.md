# 00.05 — Entornos y dependencias

<a id="05--entornos-y-dependencias"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / **Lección 00.05**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Elegir un entorno, comprobar su Python y conservar sus dependencias |
| **Necesitas** | Tu editor y shell de 00.02–00.04; elegirás una herramienta después de comprender la base común |
| **Evidencia** | Ruta del intérprete, demostración y configuración revisada del camino elegido |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Glosario](#glosario) · [Ir al lab](../../../labs/00_getting_started/05_environment/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Separar las dependencias de tu práctica de otros proyectos y conservar una
configuración que permita reconstruirlas. Estudia esta lección en dos partes:
primero el motivo, los conceptos comunes y la preparación del entorno;
después la instalación y el registro de una biblioteca. Cada parte puede
ocupar más de una sesión.

## Antes de empezar

Retoma [00.02 — Terminal y rutas](../02_terminal_paths/README.md) y
[00.04 — Primer script](../04_first_script/README.md). Necesitas el editor y el
shell de tu práctica. Los recorridos explican qué preparar si falta Python o
el gestor; no instales las tres alternativas. Las descargas requieren Internet.

**Empieza por 05A sin elegir todavía un gestor.** Primero comprenderás qué
necesita un programa para ejecutarse, qué separa un entorno y por qué conservar
sus requisitos. Al final elegirás **un solo camino** para ambas partes.
Trabaja en los espacios de práctica que indica ese camino y conserva la
configuración del repositorio.

## Qué vas a aprender

- Distinguir intérprete, entorno, biblioteca y gestor de dependencias.
- Elegir un camino y comprobar qué Python ejecuta la práctica.
- Instalar e importar una biblioteca en ese mismo entorno.
- Conservar la configuración pertinente y explicar cómo reconstruirla y sus límites.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Primer script](../04_first_script/first_summary.py) | Comprobar el entorno sin bibliotecas externas en la sesión A | Sesión A |
| [Demostración con biblioteca](library_demo.py) | Revisar la tabla de ventas con tabulate en la sesión B | Sesión B |

Abre cada recurso cuando aparezca en el recorrido. Conserva los originales y
trabaja las modificaciones en tu copia personal.

## Lecturas y recorridos

| Sesión | Material | Resultado |
| --- | --- | --- |
| 05A | [Preparar y usar un entorno](environment.md) | Comprender el motivo y las piezas comunes; después elegir un camino, comprobar el intérprete y ejecutar el primer script |
| 05B | [Instalar y conservar dependencias](dependencies.md) | Importar una biblioteca y explicar cómo reconstruir sus requisitos |

## Cómo continuar

1. Lee los conceptos comunes de 05A; explica el problema que resuelve un entorno.
2. Al final de 05A, elige un recorrido y realiza su parte A y la del lab.
3. Lee 05B y completa la parte B de ese mismo recorrido y del lab.
4. Comprueba que puedes explicar tanto el entorno como los archivos que compartirías.

Estos son los recorridos que encontrarás después de la explicación común de
05A. Cada uno tiene instrucciones por shell:

- [Conda](conda.md), recomendado si ya utilizas Anaconda.
- [venv + pip](venv-pip.md), herramientas estándar de Python.
- [uv](uv.md), gestión integrada de proyectos y lockfiles.

## Práctica

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md) para completar las sesiones A y B del camino elegido.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Nota de la sesión A con ruta de Python | El intérprete pertenece al entorno elegido y ejecuta el primer script | Qué separa el entorno y qué no garantiza |
| Configuración revisada y resultado de la sesión B | Importación de tabulate 0.9.0 y tabla con importes 80, 50 y 35 MXN | Qué archivos compartirías para reconstruir y por qué no compartir el entorno completo |

Puedes continuar cuando completes las dos sesiones con el mismo camino,
identifiques su intérprete, ejecutes ambos ejemplos y expliques qué conserva
su configuración. No necesitas practicar también los otros gestores.

Quien aprende realiza la práctica y explica el resultado. Tu compañero pregunta qué Python importó la biblioteca y qué archivos necesitaría otra persona para reconstruirlo.
Guarda evidencia y dudas en tu copia de la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o en una nota propia. PROGRESS.md registra el desarrollo editorial del curso.
Todavía no hay proyecto de datos ni checkpoint asociado a esta lección.

## Glosario

Consulta estos términos cuando aparezcan en las lecturas o en tu recorrido.
Las explicaciones y ejemplos se desarrollan en [05A](environment.md) y
[05B](dependencies.md); no necesitas memorizar la tabla antes de comenzar.

| Término | Significado en 00.05 |
| --- | --- |
| Intérprete | Programa que ejecuta las instrucciones Python; su ruta permite identificar cuál utilizas |
| Biblioteca | Funcionalidad reutilizable; puede estar incluida con Python o instalarse aparte, como tabulate |
| Paquete distribuido | Software que solicitas al gestor para instalarlo; aquí se llama tabulate |
| Dependencia | Software que tu proyecto necesita para funcionar |
| Versión | Edición concreta de Python o de un paquete; tabulate 0.9.0 es la usada en esta práctica |
| Entorno | Intérprete y espacio de paquetes que utilizas para ejecutar un trabajo |
| Gestor | Herramienta que prepara o administra entornos, intérpretes o paquetes |
| Activar | Preparar la sesión del shell para utilizar los comandos del entorno |
| Instalar | Añadir un paquete al entorno elegido mediante su gestor |
| Importar | Solicitar desde el código una funcionalidad disponible para ese Python; no la descarga |
| Requisito | Declaración del software necesario y, cuando corresponde, de su versión |
| Configuración | Archivos de texto con información que las herramientas leen para preparar el proyecto o entorno |
| Resolución | Selección de versiones compatibles con los requisitos y sus dependencias |
| Lockfile | Archivo que conserva una resolución de dependencias, como uv.lock; no contiene una copia del entorno |
| Reconstruir | Preparar de nuevo el entorno desde la configuración y comprobar la ejecución |

Para recuperar más detalle, consulta los glosarios de
[entornos y herramientas — 05A](environment.md#glosario) y de
[instalación y requisitos — 05B](dependencies.md#glosario).

## Referencias

Las fuentes oficiales se incluyen en [05A](environment.md#referencias) y
[05B](dependencies.md#referencias), junto a los conceptos que respaldan.

<a id="siguiente-lección"></a>

## Siguiente paso

Después del lab y su comprobación, continúa con [00.06 — Tu primer notebook](../06_first_notebook/README.md).

[← Módulo 00](../README.md) · [Lab 00.05](../../../labs/00_getting_started/05_environment/README.md) · [Siguiente →](../06_first_notebook/README.md)
