# Lab 14.03 — Reconstruir el entorno y repetir la consulta

[Inicio](../../../README.md) / [Módulo 14](../../../curriculum/14_reproducible_projects/README.md) / **Lab 14.03**

[Volver a la lección](../../../curriculum/14_reproducible_projects/03_reconstructible_environments/README.md)

## Objetivo y entrada

Preparar un entorno local desde sus metadatos, repetir en otra copia nueva y
conciliar lo obtenido. Sigue los [recorridos](../../../curriculum/14_reproducible_projects/03_reconstructible_environments/recorridos.md).
Recibes 26 fuentes y eliges Python/uv o R/renv. No se exigen entregas anteriores,
ni practicar ambas rutas, ni instalar las futuras dependencias de reporte/app.

## 1. Revisar qué está declarado

Antes de preparar el entorno, localiza:

- Versión del intérprete en entorno.csv y en los metadatos de tu ruta.
- Paquetes solicitados y qué contiene realmente el lockfile.
- Dónde se instalará la biblioteca/venv y dónde quedará la evidencia.
- Qué herramienta externa falta por revisar para un futuro reporte Quarto.

Explica por qué dependencies=[] en Python es válido para esta consulta y por qué
el lockfile R contiene renv, aunque el cálculo no necesita paquetes de análisis.
No añadas paquetes para que el archivo parezca más completo.

## 2. Preparar y ejecutar en la primera copia

Sigue una ruta completa de recorridos. Conserva el comando real y su resultado.
Antes de ejecutar predice octubre/ambos/2000: 003=2600 MXN, universo tres/4600,
cobertura 100/3. Ejecuta creando evidencia/python_1.csv o evidencia/r_1.csv.

Abre el registro como CSV con columnas clave/valor. Comprueba versión, intérprete,
raíz y entorno local, parámetros y resultados por crédito. ¿Dónde indica que
Quarto se encontró o no en PATH? ¿Eso demuestra que ya existe un reporte renderizado?

## 3. Reconstruir desde las fuentes

Crea otra carpeta nueva, preferiblemente con espacios, usando la lista de 26
fuentes del recorrido. No copies .venv, bibliotecas/cache de renv, caché uv ni
evidencia anterior. No necesitas volver a leer las fuentes del repositorio original.

Reconstruye el entorno de la segunda ubicación, en una sesión/proceso nuevo.
Ejecuta la misma consulta y crea evidencia/python_2.csv o evidencia/r_2.csv.
Compara:

| Debe coincidir | Puede diferir sin cambiar la consulta |
| --- | --- |
| Reglas, corte, segmentos, mínimo y app elegida | Rutas de proyecto/intérprete/biblioteca |
| IDs y saldos por crédito, universo e indicadores | Fecha/hora y algunos datos del sistema |
| Huellas de entrada y configuración si conservaste los bytes | Bytes completos del registro de evidencia |

Si una huella cambia, revisa también finales de línea y contenido; una coincidencia
numérica aislada no demuestra que recibiste la misma fuente. No uses MD5 como firma.
renv puede regenerar el activador con diferencias de espacios: revisa su contenido
sin atribuirlo a cambios del contrato.

## 4. Demostrar que los controles detectan diferencias

Elige al menos dos casos en una copia de práctica, conservando el estado original:

1. Intenta ejecutar desde Python base o R sin la biblioteca local activada.
   El ejecutor debe rechazarlo, aunque revisar.py/R de 14.02 pudiera calcular.
2. Repite el mismo nombre de evidencia: debe rechazarlo y conservar el archivo
   previo. Repite después con un nombre nuevo, sin borrar evidencia para ocultar el intento.
3. En una copia de los metadatos Python, cambia version del proyecto 0.1.0 a
   0.1.1 en pyproject.toml, sin modificar uv.lock. Ejecuta con --locked: debe
   rechazar la desalineación. Restaura el archivo original después de observarlo.
4. En una copia de entorno.csv, declara otra versión del intérprete de tu ruta.
   El ejecutor debe rechazar la diferencia; no la presentes como reconstrucción equivalente.

Conserva el diagnóstico real. Cambiar un lockfile para ocultar un fallo no es
la solución; revisa la intención y las versiones efectivamente requeridas.

## 5. Cambiar una consulta sin cambiar el entorno

Crea config/septiembre.csv a partir de la configuración original, sin sobrescribirla.
Cambia corte a 2026-09-30 y salida a salidas/septiembre. Ejecuta con esa configuración
y un nombre nuevo de evidencia. Debes obtener 002=2000 y 003=2500, saldo 4500
y cobertura 2/3. Mantén el mismo entorno y conserva ambas consultas identificadas.

Explica por qué fecha/raíz de ejecución no son filtros de negocio, y por qué
el registro no demuestra una exportación pasada de una app. Esta sección no
inicia apps, genera HTML ni implementa reprocesamiento de resultados completos.

## Ayudas y solución razonada

<details>
<summary>Ver cómo distinguir las capas</summary>

pyproject/DESCRIPTION declaran; uv.lock/renv.lock conservan la resolución;
.venv o renv/library contienen lo instalado. El ejecutor revisa su entorno real
y calcula la consulta. El registro conserva observaciones, sin autenticar la
historia. Quarto es una herramienta externa: registrar su versión no renderiza.

</details>

<details>
<summary>Ver qué demuestra reconstruir en otra carpeta</summary>

Se parte de fuentes/metadatos, se crea otra biblioteca/venv y se repite desde
una sesión nueva. No se conserva el entorno anterior como si fuera portable.
Cambian las rutas y fechas; deben coincidir pregunta efectiva, valores por crédito
y medidas. El lockfile no garantiza sistema, permisos o disponibilidad futura.

</details>

## Evidencia y criterio de salida

Conserva fuentes, comandos, dos registros comparados, la variante de septiembre
y un rechazo explicado, además de dudas/ayudas/siguiente paso en tu nota personal.
No publiques rutas o registros sin revisarlos. Distingue entorno reconstruido,
consulta correcta y producto integrado aún pendiente.

## Siguiente paso

Consulta [14.04 — Pipeline y reprocesamiento](../../../curriculum/14_reproducible_projects/04_pipeline_reprocessing/README.md),
ya disponible. Los proyectos y checkpoints requieren implementación propia.
