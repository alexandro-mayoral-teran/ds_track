# Estado y pendientes de almacenamiento — módulos 09 y 10

## Punto de reanudación

[09 — Arrow/Parquet](../curriculum/09_arrow_parquet/README.md) y
[10 — Polars/DuckDB](../curriculum/10_polars_duckdb/README.md) tienen todas sus
lecciones y labs. 09.08 y 10.05 son opcionales. El inventario por sección vive
en esos índices; la bitácora de autoría está en [PROGRESS.md](../PROGRESS.md).
Este documento reúne criterios de integración y límites de las comprobaciones.

El [cierre 09.09](../curriculum/09_arrow_parquet/09_shared_contract_closure/README.md)
reconstruye una referencia externa y compara entregas completas/partes desde
Python y R. El [cierre 10.10](../curriculum/10_polars_duckdb/10_closure_tool_choice/README.md)
compara pandas, Polars y DuckDB con la misma fuente, selección y resumen,
mediciones acotadas y una decisión que requiere revisión humana.

## Desarrollo del material y siguiente módulo

Los contratos se introducen antes de elegir formato o motor. Leer un esquema
antes de adaptar tipos; comparar valores por clave después de releer. Separar
fuente, auditoría completa, consulta y entrega. Preparar una carpeta nueva sin
exigir entregas personales de capítulos anteriores ni alterar los originales.

La introducción 09.01 permite inspección esencial sin decodificar Parquet;
PyArrow pasa a dependencia declarada en 09.03 y Arrow R se incorpora en 09.04.
Los requisitos efectivos viven en pyproject/uv.lock y los proyectos renv de
práctica, con preparación específica en cada lección. No instalar motores por
leer un plan ni modificar bibliotecas globales.

[11 — Quarto](../curriculum/11_reporting_quarto/README.md) también tiene material;
Streamlit dispone de 12.01–12.09; 13.01–13.09 de Shiny están disponibles; 13.10 y 14 siguen planificados.
La reanudación de la app está en [criterios de Streamlit](streamlit-closure.md).
Los criterios de reporte están en
[cierre de reportes](reporting-closure.md). Desarrollar una lección no completa
las prácticas ni activa proyectos o checkpoints.

## Qué falta para cerrar las prácticas y la integración

| Evidencia por reunir | Comprobación |
| --- | --- |
| Contrato y fuente explicados | Unidad de fila, clave, tipos, unidades, ausencias y reglas antes de operar |
| Intercambio y entrega propios | Valores por clave, esquema y relectura; originales y motivos conservados |
| Selección y resumen | Mismo universo, cobertura y referencia externa independiente del motor |
| Medición con alcance explícito | Respuesta equivalente, protocolo, fases, repeticiones y métricas realmente observadas |
| Elección argumentada | Relación entre necesidad, costos medidos, límites y reconstrucción |
| Reconstrucción por otra persona | Copia nueva, entornos locales y explicación del resultado y sus límites |

Reunir evidencia de las secciones esenciales de 09 y 10 y de las ampliaciones
que se elijan. Los criterios de los módulos previos están en
[cierre de tidyverse](tidyverse-closure.md) y el
[índice de visualización R](../curriculum/08_visualization_r/README.md).

Los proyectos `03_portfolio_analysis_r` y `04_large_credit_dataset` siguen en
[planificación](../projects/README.md), sin carpetas ni checkpoints activos.
Definir producto, entradas, contrato, rúbrica y enlaces antes de implementarlos.
R aplicado y terminal avanzada siguen pendientes de diseño; no renumerar 00–14.
Las bitácoras personales ya están separadas del estado editorial en las muestras
00/02.01; no afirmar que se migraron todos los registros anteriores.

## Comprobaciones requeridas al desarrollar lo siguiente

- Conservar entradas y resultados previos; probar vacío, claves repetidas,
  faltantes, límites de enteros/decimales y fechas.
- Comparar detalle por clave y justificar tolerancias cuando haya punto flotante.
  Una suma coincidente o una huella no validan cada registro ni autentican sesiones.
- Distinguir tipos lógicos, representación de cada lenguaje e igualdad binaria.
  No imputar ni truncar para conseguir equivalencia.
- Separar auditoría de proyección/filtro y medición de validación/escritura.
  Seguir el [protocolo 10.09](../curriculum/10_polars_duckdb/09_time_memory/README.md)
  para interpretar sus fases y métricas: caché del SO sin vaciar, pico residente
  absoluto y límites de plataforma; no atribuir esos tiempos a otra operación.
- Lazy, streaming, planes o pocos registros no acreditan RAM acotada, I/O físico,
  disco frío, ausencia de copias ni rendimiento general. Arrow R y PyArrow no
  exponen necesariamente los mismos metadatos; declarar qué se observó.
- Comprobar restauración local cuando cambien dependencias, sin modificar entornos
  globales. Datos personales, bibliotecas y salidas de práctica quedan fuera de Git.
- Revisar navegación y evidencia con el [flujo de aprendizaje](learning-workflow.md)
  y registrar comprobaciones de autoría en PROGRESS.md.
