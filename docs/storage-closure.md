# Estado y pendientes de almacenamiento — módulo 09

## Punto de reanudación

[09.01 — CSV, Parquet y Arrow](../curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md)
y su [lab](../labs/09_arrow_parquet/01_csv_parquet_arrow/README.md) están disponibles.
Incluyen la muestra CSV/Parquet de 28 observaciones, inventario, evidencia de
lectura real y recorridos esenciales de solo lectura sin dependencias nuevas.
El esencial distingue inspección de firma de decodificación Parquet; la opción
PyArrow es una ampliación de autoría. No se implementó el lector arrow de R.

El siguiente trabajo concreto es
[09.02 — Esquemas y tipos entre lenguajes](../curriculum/09_arrow_parquet/README.md#02-esquemas-y-tipos-entre-lenguajes).
El estado y verificaciones de la sesión se registran en [PROGRESS.md](../PROGRESS.md),
sin duplicar aquí una bitácora. **09.01 no completa el módulo ni acredita práctica
del estudiante.**

## Qué falta desarrollar para cerrar el módulo

| Sección pendiente | Producto y condición de cierre |
| --- | --- |
| 09.02 — Contrato | Lección/lab con nombres, unidad, clave ID/corte, tipos y nulabilidad. Distinguir ausente, texto vacío y cero; ID con ceros, fechas de calendario frente a instantes, dinero/unidad/rango y precisión. Separar esquema y reglas de negocio. |
| 09.03 — Python | Recorrido completo de instalación solo en el entorno elegido, versiones registradas, conversión y relectura. Definir índice pandas explícitamente; comparar claves, tipos y valores. Mantener los requisitos existentes y comprobar lockfile. |
| 09.04 — R | Incorporar arrow al mismo proyecto renv con respaldo/lockfile y restauración local real; IDE como recorrido principal. No cambiar Conda ni bibliotecas globales. Comprobar tipos y NA, sin asumir compatibilidad por coincidir nombres de versiones. |
| 09.05 — Lectura cruzada | Python escribe/R lee y R escribe/Python lee; comparar claves, tipos, faltantes e indicadores por ambas rutas. No basta releer con el mismo escritor ni comparar dos sumas. |
| 09.06 — Consulta selectiva | Selección de columnas/filtros y varios archivos; explicar cuándo se prepara una consulta y cuándo se materializa. Comprobar equivalencia con el análisis de referencia y límites de memoria. |
| 09.07 — Metadatos y compresión | Leer grupos/columnas/estadísticas; comparar configuraciones con datos equivalentes, tamaño y mediciones separadas. Evitar conclusiones de rendimiento a partir de 28 filas o solo bytes. |
| 09.08 — Particiones, extensión | Implementar solo como ampliación: consulta justificada, archivos repetidos y particiones excesivas. No bloquear el cierre esencial por particionar. |
| 09.09 — Entrega integrada | Reconstrucción desde una sesión nueva en ambos lenguajes; archivos/contrato y verificadores de solo lectura, con interpretación y límites. Mantener entradas y rechazar sobrescrituras accidentales. |

Para 09.02 empezar por la muestra actual y explicar qué **no** cubre: está
completa y sin ausencias. Diseñar casos pequeños separados con NA/null, campos
vacíos, ID textual, fechas inválidas y fronteras de precisión/rango; conservar
la muestra y sus resultados. Un caso rechazado se documenta, no se corrige
silenciosamente. El esquema no comprueba unicidad, cobertura o saldo válido.

PyArrow 21.0.0 se utilizó en un entorno de autoría ya existente para producir y
releer el ejemplo 09.01; **no es una dependencia nueva fijada del track**. Elegir,
verificar y registrar versiones forma parte de 09.03. No instalar por adelantado
PyArrow, arrow de R, Polars o DuckDB solo para planificar el recorrido.

## Qué falta para cerrar las prácticas y la integración

- Reunir evidencia propia del estudiante de 09.01 y, más adelante, del contrato,
  conversiones, intercambio y consulta. Material disponible no acredita aprendizaje.
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
