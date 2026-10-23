# Estado y pendientes de almacenamiento — módulo 09

## Punto de reanudación

[09.01 — CSV, Parquet y Arrow](../curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md)
y su [lab](../labs/09_arrow_parquet/01_csv_parquet_arrow/README.md) están disponibles.
Incluyen la muestra CSV/Parquet de 28 observaciones, inventario, evidencia de
lectura real y recorridos esenciales de solo lectura sin dependencias nuevas.
La introducción explica filas/columnas, selección lógica frente a lectura física,
codificación/compresión y condiciones del intercambio en memoria, con decisiones
de uso sin anticipar la práctica de datasets ni la medición de rendimiento.
El esencial distingue inspección de firma de decodificación Parquet; la opción
PyArrow es una ampliación de autoría. Esta introducción no implementa el lector arrow de R.

[09.02 — Esquemas y tipos entre lenguajes](../curriculum/09_arrow_parquet/02_schemas_types/README.md)
y su [lab](../labs/09_arrow_parquet/02_schemas_types/README.md) también están
disponibles: contrato de la base conocida, evaluadores Python estándar/R base
y 23 casos separados, sin nuevas dependencias. Se conservan originales y motivos;
se explican rango/precisión, dinero, fechas/instantes y categorías. Esta sección no realiza
lectura cruzada Parquet en ambos lenguajes.

[09.03 — Leer y escribir desde Python](../curriculum/09_arrow_parquet/03_python_read_write/README.md)
dispone de lección, recorridos completos de entorno, funciones/ejecutor/verificador
y [lab](../labs/09_arrow_parquet/03_python_read_write/README.md). PyArrow 21.0.0
declarado con lockfile real; pandas 2.3.3 y registros previos conservados.
Esquema no anulable, índice omitido, entrega nueva y relectura completa por clave
contra el CSV reconstruido, sin cambiar la muestra de 09.01 ni el entorno R.

[09.04 — Leer y escribir desde R](../curriculum/09_arrow_parquet/04_r_read_write/README.md)
y su [lab](../labs/09_arrow_parquet/04_r_read_write/README.md) están disponibles.
Ejemplo pequeño completo y base común; no se necesitan entregas personales Python
ni objetos de 07–08. Arrow 25.0.1/assertthat 0.2.1 se incorporan al mismo proyecto
renv con respaldo 08.09, 44 registros previos idénticos y segunda restauración
local desde biblioteca vacía. Lectura del esquema real antes de convertir,
valores por clave y entrega R verificada desde sesión nueva, conservando
28 registros y 29000/31800 MXN. Se lee la referencia escrita por Python;
la práctica completa del intercambio en ambas direcciones se desarrolla en 09.05.

[09.05 — Intercambio Python y R](../curriculum/09_arrow_parquet/05_python_r_exchange/README.md)
y su [lab](../labs/09_arrow_parquet/05_python_r_exchange/README.md) están disponibles.
Python escribe/R lee y R escribe/Python lee, sin depender de entregas anteriores
ni añadir paquetes. Conserva la base común y concilia esquema y valores por
clave; muestra independiente de tres filas con acentos, vacío/ausencia/cero y
otro contrato. Verificaciones desde procesos nuevos, fuentes/lockfiles intactos.

[09.06 — Lectura selectiva y datasets](../curriculum/09_arrow_parquet/06_selective_datasets/README.md)
y su [lab](../labs/09_arrow_parquet/06_selective_datasets/README.md) están disponibles.
Partes Parquet, Dataset/Scanner y dplyr, filtros/proyección y materialización;
auditoría completa separada de la selección. Mantiene la base común y concilia
nueve IDs/24100 MXN para octubre ≥ 2000, contra CSV independiente en cada lenguaje.
Ejemplo pequeño completo, sesiones nuevas y fuentes/lockfiles intactos; no
acredita bytes omitidos, rendimiento ni RAM acotada.
La ampliación didáctica presenta la tabla pequeña antes del código y ejemplos
iniciales con APIs Arrow directas, sin funciones ni archivos de capítulos
anteriores. El lab separa esa práctica de la integración con CSV; Python y R
crean sus propias copias alteradas y pueden ejecutarse por separado.

El siguiente trabajo concreto es
[09.07 — Metadatos, row groups y compresión](../curriculum/09_arrow_parquet/README.md#07-metadatos-row-groups-y-compresion).
El estado y verificaciones de la sesión se registran en [PROGRESS.md](../PROGRESS.md),
sin duplicar aquí una bitácora. **09.01–09.06 no completan el módulo ni acreditan práctica
del estudiante.**

## Qué falta desarrollar para cerrar el módulo

| Sección pendiente | Producto y condición de cierre |
| --- | --- |
| 09.07 — Metadatos y compresión | Leer grupos/columnas/estadísticas; comparar configuraciones con datos equivalentes, tamaño y mediciones separadas. Evitar conclusiones de rendimiento a partir de 28 filas o solo bytes. |
| 09.08 — Particiones, extensión | Implementar solo como ampliación: consulta justificada, archivos repetidos y particiones excesivas. No bloquear el cierre esencial por particionar. |
| 09.09 — Entrega integrada | Reconstrucción desde una sesión nueva en ambos lenguajes; archivos/contrato y verificadores de solo lectura, con interpretación y límites. Mantener entradas y rechazar sobrescrituras accidentales. |

Para 09.07 conservar los contratos, escritores y verificadores existentes.
Presentar metadatos, grupos de filas y compresión con ejemplos completos;
comparar archivos que representen los mismos registros y esquema. Separar
codificación de compresión y verificar códecs disponibles antes de usarlos.
Medir tamaño y tiempo por separado, conservar observaciones crudas y distinguir
caché/entorno de diferencias de formato. Estos 28 registros no justifican
conclusiones generales de rendimiento. No inferir bytes físicamente omitidos
por una consulta solo de su plan o del número de filas resultantes.

PyArrow 21.0.0 se utilizó en un entorno de autoría ya existente para producir y
releer el ejemplo 09.01; no se añadió como dependencia durante esa introducción.
Desde 09.03 sí es dependencia declarada y comprobada del track, con instalación
y segunda reconstrucción uv local. Arrow de R ya está incorporado desde 09.04. No instalar por adelantado
Polars o DuckDB solo para planificar el recorrido.

## Qué falta para cerrar las prácticas y la integración

- Reunir evidencia propia del estudiante de 09.01–09.06 y, más adelante, de
  metadatos, compresión e integración. Material disponible no acredita aprendizaje.
- Revisar el cierre de [08](../curriculum/08_visualization_r/README.md): geometrías,
  escalas, población, exportación desde sesión nueva y conciliación con Python.
  Sus nueve secciones tienen material; no faltan lecciones de ese módulo.
- Los criterios y pendientes del cierre de 07 siguen en
  [tidyverse-closure.md](tidyverse-closure.md). El proyecto previsto
  `03_portfolio_analysis_r` continúa sin carpeta ni checkpoints activos.
- El proyecto previsto `04_large_credit_dataset` tampoco está implementado:
  definir producto, fuentes, contrato, rúbrica y checkpoints antes de crear su
  estructura o dar por cerrada la integración de 09/10. Consultar
  [proyectos](../projects/README.md).
- R aplicado, terminal avanzada y separación entre progreso del material y
  bitácoras personales siguen como decisiones de diseño. No renumerar 00–14
  ni presentar esas integraciones como realizadas.

## Comprobaciones requeridas al desarrollar lo siguiente

Conservar fuente y resultados anteriores; probar vacío, claves duplicadas,
faltantes, límites de enteros/decimales y fechas. Comparar por clave, sin depender
del orden accidental. Si se usa punto flotante, justificar tolerancias; no
imputar ni truncar para conseguir igualdad. Distinguir equivalencia de valores,
tipos lógicos, representación en cada lenguaje e igualdad binaria del archivo.

Revisar enlaces y navegación lección → lab → comprobación → evidencia → siguiente
lección; actualizar índices, arquitectura y progreso. Cuando se incorporen
dependencias, comprobar restauración desde otra biblioteca/entorno local sin
modificar los globales. Datos personales, bibliotecas y salidas de práctica
quedan fuera de Git. El módulo 10 y 11–14 conservan sus planes.
