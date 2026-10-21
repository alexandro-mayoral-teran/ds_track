# Procedencia de la muestra 09.01

Los dos archivos contienen las mismas **28 observaciones** de la base común:
14 IDs aceptados el 2026-09-30 y el 2026-10-31. Proceden del
[CSV de 48 registros](../../../02_pandas/06_text_dates/cartera_texto_fechas.csv)
y las reglas de [07.09](../../../07_tidyverse/09_dates_cutoffs/README.md)
y [07.10](../../../07_tidyverse/10_first_plot_closure/README.md).
La [referencia independiente 08.09](../../../08_visualization_r/09_visual_comparison/comparar_python.py)
reconstruyó aceptados/rechazos y los 14 pares; cada par se proyectó a una fila
por corte, ordenadas por fecha e ID. No se generaron otros créditos ni importes.

- Campos: ID textual, fecha ISO de calendario y saldo en MXN enteros.
- Clave: ID/corte, única. Sin ausencias en esta muestra.
- Totales: 29000/31800 MXN, 14 registros por fecha; cobertura de origen 14/18.
- No contiene rechazos ni los ocho aceptados sin pareja, que se conservan en
  las entregas anteriores; tampoco es toda la información del análisis original.

El CSV usa UTF-8 sin BOM, coma y LF. El Parquet se produjo durante la autoría
con PyArrow 21.0.0 existente, esquema explícito con `string`, `date32[day]` e
`int32`, campos no anulables, `row_group_size=14`, `compression="snappy"`,
`version="2.6"` y `store_schema=True`. Su lectura se comparó valor por valor,
conservando fechas e IDs; no basta comprobar solo totales. No se instaló ni
registró PyArrow en los requisitos raíz. El lector R de Parquet queda para 09.04.

[inventario.csv](inventario.csv) conserva tamaño y MD5 de las dos representaciones.
Las reglas locales de atributos Git fijan LF para estas muestras CSV y tratan
Parquet como binario; así sus huellas no dependen de conversión de saltos de línea
al clonar. Las huellas son controles de integridad de esta muestra, no pruebas de
calidad o seguridad. No editar el inventario para ocultar una alteración.

[lectura_parquet.txt](lectura_parquet.txt) resume los metadatos observados. Para
repetir la lectura con un lector compatible ya disponible, utiliza la opción
`--verificar-parquet` de [inspeccionar_formatos.py](../inspeccionar_formatos.py).
Esa función es de solo lectura y permite comparar esquema y valores por clave;
el recorrido esencial no importa PyArrow. Vuelve a la [lección](../README.md).
