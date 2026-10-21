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
PyArrow es una ampliación de autoría. No se implementó el lector arrow de R.

[09.02 — Esquemas y tipos entre lenguajes](../curriculum/09_arrow_parquet/02_schemas_types/README.md)
y su [lab](../labs/09_arrow_parquet/02_schemas_types/README.md) también están
disponibles: contrato de la base conocida, evaluadores Python estándar/R base
y 23 casos separados, sin nuevas dependencias. Se conservan originales y motivos;
se explican rango/precisión, dinero, fechas/instantes y categorías. No se ha
implementado todavía lectura cruzada Parquet en ambos lenguajes.

[09.03 — Leer y escribir desde Python](../curriculum/09_arrow_parquet/03_python_read_write/README.md)
dispone de lección, recorridos completos de entorno, funciones/ejecutor/verificador
y [lab](../labs/09_arrow_parquet/03_python_read_write/README.md). PyArrow 21.0.0
declarado con lockfile real; pandas 2.3.3 y registros previos conservados.
Esquema no anulable, índice omitido, entrega nueva y relectura completa por clave
contra el CSV reconstruido, sin cambiar la muestra de 09.01 ni el entorno R.

El siguiente trabajo concreto es
[09.04 — Leer y escribir desde R](../curriculum/09_arrow_parquet/README.md#04-leer-y-escribir-desde-r).
El estado y verificaciones de la sesión se registran en [PROGRESS.md](../PROGRESS.md),
sin duplicar aquí una bitácora. **09.01–09.03 no completan el módulo ni acreditan práctica
del estudiante.**

## Qué falta desarrollar para cerrar el módulo

| Sección pendiente | Producto y condición de cierre |
| --- | --- |
| 09.04 — R | Incorporar arrow al mismo proyecto renv con respaldo/lockfile y restauración local real; IDE como recorrido principal. No cambiar Conda ni bibliotecas globales. Comprobar tipos y NA, sin asumir compatibilidad por coincidir nombres de versiones. |
| 09.05 — Lectura cruzada | Python escribe/R lee y R escribe/Python lee; comparar claves, tipos, faltantes e indicadores por ambas rutas. No basta releer con el mismo escritor ni comparar dos sumas. |
| 09.06 — Consulta selectiva | Selección de columnas/filtros y varios archivos; explicar cuándo se prepara una consulta y cuándo se materializa. Comprobar equivalencia con el análisis de referencia y límites de memoria. |
| 09.07 — Metadatos y compresión | Leer grupos/columnas/estadísticas; comparar configuraciones con datos equivalentes, tamaño y mediciones separadas. Evitar conclusiones de rendimiento a partir de 28 filas o solo bytes. |
| 09.08 — Particiones, extensión | Implementar solo como ampliación: consulta justificada, archivos repetidos y particiones excesivas. No bloquear el cierre esencial por particionar. |
| 09.09 — Entrega integrada | Reconstrucción desde una sesión nueva en ambos lenguajes; archivos/contrato y verificadores de solo lectura, con interpretación y límites. Mantener entradas y rechazar sobrescrituras accidentales. |

Para 09.04 partir del contrato de 09.02 y del Parquet Python de 09.03, sin
modificarlos. Incorporar arrow al mismo proyecto renv con respaldo, lockfile
y restauración local comprobada. Leer tipos reales antes de convertir, conservar
ID/date32/int32 y nulabilidad, comprobar todos los valores por clave. Reutilizar
casos separados de ausencia/calendario/rango y no imponer el tamaño de la muestra
como regla universal. Mantener IDE como recorrido principal y conservar entregas.

PyArrow 21.0.0 se utilizó en un entorno de autoría ya existente para producir y
releer el ejemplo 09.01; no se añadió como dependencia durante esa introducción.
Desde 09.03 sí es dependencia declarada y comprobada del track, con instalación
y segunda reconstrucción uv local. No instalar por adelantado arrow de R,
Polars o DuckDB solo para planificar el recorrido.

## Qué falta para cerrar las prácticas y la integración

- Reunir evidencia propia del estudiante de 09.01–09.03 y, más adelante, de
  conversión R, intercambio y consulta. Material disponible no acredita aprendizaje.
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
