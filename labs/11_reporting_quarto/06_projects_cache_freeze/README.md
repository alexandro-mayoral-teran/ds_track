# Lab 11.06 — Demostrar cuándo se recalculó un reporte

## Relación, entrada y resultado

- Lección: [11.06 — Proyectos, caché y freeze](../../../curriculum/11_reporting_quarto/06_projects_cache_freeze/README.md).
- Entrada: muestra de siete filas, funciones de 11.05 y proyecto preparado en la lección.
- Resultado: dos experimentos separados, HTML conservados y una explicación del recálculo.
- Proyecto/checkpoint: no aplica todavía; `05_monthly_report` sigue previsto.

Reserva dos sesiones de 40–60 minutos si lo necesitas. Un motor basta; comparar
Python/R es ampliación. Usa copias nuevas y conserva fuentes y trabajos anteriores.
No se exige una entrega personal de 11.05.

## A. Preparar y predecir

1. Sigue el recorrido de tu motor y abre `_quarto.yml` y el reporte.
2. Explica desde dónde se resuelven las rutas de `datos/` y qué hace `output-dir`.
3. Con caché/freeze desactivados, predice universo y selección de septiembre.
4. Renderiza dos veces y anota cifras, identificadores y líneas de la bitácora.
5. Conserva el primer HTML fuera de la carpeta que puede reemplazar el render.

<details>
<summary>Comprobación razonada de A</summary>

Septiembre contiene tres créditos por 6000 MXN. Con mínimo inclusivo 2000,
002/003 suman 5000; son dos de tres (66.67%). `execute-dir: project` hace que
las rutas del código partan de la raíz, aunque el reporte esté en `informes/`.
`output-dir` ubica el HTML, no las entradas. Cada ejecución nueva tiene otro
identificador y añade una línea; igualdad de cifras no significa reutilización.

</details>

## B. Un CSV nuevo con un resultado antiguo

1. Activa `freeze: auto`, conserva `cache: false` y realiza un render global.
2. Repite sin cambios. Predice si se ejecutará el cálculo.
3. Cambia solo el saldo de 003 en septiembre a 3600 dentro de tu copia.
4. Predice la suma actual antes de renderizar. Ejecuta `quarto render`.
5. Contrasta HTML y CSV; ejecuta el verificador de la lección si tienes Python.
6. Ejecuta el documento explícito con `--cache-refresh` y vuelve a comprobar.

<details>
<summary>Pista de B</summary>

Pregunta qué archivo cambió: el CSV o el documento `.qmd`. Después comprueba
si tu comando selecciona el proyecto entero o el documento concreto.

</details>

<details>
<summary>Solución razonada de B</summary>

La fuente actual contiene 6600 MXN en septiembre y selecciona 5600. Con freeze
auto, el render global puede conservar 6000/5000, el identificador y las líneas
anteriores. El verificador debe rechazar esa salida. Desde la raíz del proyecto:

```text
quarto render informes/reporte_1106.qmd --cache-refresh
```

El reporte vuelve a leer los datos y muestra 6600/5600 con nueva ejecución.
`--cache-refresh` en un render global no sustituye la selección del documento
para evitar freeze. No edites manualmente las cifras del HTML.

</details>

## C. Código y parámetros

1. Con freeze auto y caché desactivada, cambia solo la revisión del bloque de
   cálculo de 1 a 2, como se explica en la lección. Renderiza globalmente.
2. Explica por qué cambió la evidencia aunque los saldos sigan iguales.
3. Renderiza explícitamente octubre con su YAML y `--cache-refresh`.
4. Contrasta el universo, la selección, los IDs y la tabla completa de octubre.
5. Como ampliación, cambia freeze a true y compara render global e individual
   tras cambiar otra vez la revisión. No cambies las reglas de selección.

<details>
<summary>Solución razonada de C</summary>

El cambio de revisión está dentro del `.qmd`, por lo que auto puede observarlo;
no es una modificación de saldos. Octubre conserva cuatro créditos/7000 MXN,
selecciona 003/3300 (25.00%) aunque hayas alterado septiembre. Pasa el YAML de
tu motor siguiendo la sección 9; para verificar octubre indica su fecha.
Freeze true conserva resultados en el render global incluso tras editar el
documento; el render individual permite actualizarlos.

</details>

## D. Caché en una copia independiente

1. Prepara otra copia completa del proyecto con la muestra original.
2. Configura `freeze: false` y `cache: true`.
3. Renderiza el documento con refresco y repite sin refresco.
4. Cambia 003/septiembre a 3600 y repite sin refresco. Explica lo observado.
5. Refresca y comprueba los valores por fila, además de las sumas.
6. Cambia el mínimo a 4000 mediante parámetros siguiendo 11.05. Ejecuta con
   refresco y comprueba que selección vacía no significa universo vacío.

<details>
<summary>Solución razonada de D</summary>

La primera serie parte de 6000/5000. La caché puede conservar esos resultados
después del cambio de CSV; con refresco aparecen 6600/5600. Con mínimo 4000
en septiembre cambiado, el universo sigue siendo tres/6600 y la selección
cero/0 MXN (0.00%). La tabla conserva las tres filas marcadas como no cumplidas.
Jupyter y knitr no tienen idéntica invalidación: por eso se utiliza refresco
explícito al cambiar entradas o parámetros. No mezcles las carpetas de caché
de los dos experimentos.

</details>

## E. Trabajar en pareja y cerrar individualmente

Una persona escribe y explica lo que espera; la otra contrasta el CSV y anota
el comando exacto. Cambien papeles entre B y D. Cada persona responde después:

- ¿Qué evidencia distingue una ejecución nueva de unas cifras idénticas?
- ¿Qué cambio externo podría quedar sin observar?
- ¿Por qué ejecutar correctamente y entregar datos vigentes son comprobaciones distintas?
- Si la entrada tuviera un duplicado fuera del corte, ¿cuándo se detectaría?

La validación completa se ejecuta al recalcular; un HTML reutilizado puede
ocultar incluso una fuente ahora inválida. El verificador vuelve a leerla sin
depender del motor del reporte. No atribuyas a un resultado histórico una
validación de la fuente actual.

## Evidencia y criterio de salida

Conserva una tabla con escenario, configuración, comando, dato cambiado,
valores esperados/observados, identificador y comprobación. Adjunta las copias
de HTML relevantes, fuentes, YAML y una explicación de recuperación.
La bitácora no autentica sesiones históricas y no sustituye la explicación.

Puedes avanzar al demostrar un resultado antiguo, recuperarlo y explicar
por qué funcionó. Registrar la evidencia no exige publicar el trabajo personal.
Continúa con [11.07 — Formatos y revisión visual](../../../curriculum/11_reporting_quarto/07_formats_visual_review/README.md),
ya disponible; no con otro lab.
