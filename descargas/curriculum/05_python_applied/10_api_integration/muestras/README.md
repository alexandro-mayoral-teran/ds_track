# Muestras locales de 05.10

Estas respuestas son simulaciones propias, no descargas de un servicio real.
Se derivan de [creditos.csv](../../../03_sql_databases/01_relational_sqlite/data/creditos.csv)
y [cortes.csv](../../../03_sql_databases/01_relational_sqlite/data/cortes.csv),
uniendo segmento por id_credito y ordenando por fecha/id. Se conservan las 48
observaciones, ceros iniciales, valores y ausencias. No reemplazan esos CSV.

- pagina_01.json, pagina_02.json y pagina_03.json: 16 registros cada una,
  total 48 y next_page 2, 3, null respectivamente. Los campos son los descritos
  en la [lección](../README.md).
- correcto.json: tres pasos con estado 200 y referencia body_file a esas páginas.
- recuperable.json: 503, éxito de página 1, timeout, éxito de página 2 y página 3.
- error_tardio.json: página 1 válida y 401 en página 2; el cuerpo de ese error
  no se usa como una página aceptada, aunque apunte a un archivo con JSON válido.
- json_invalido.json: 200 con invalido.txt, deliberadamente incompleto.

Cada paso representa una respuesta o falla de transporte, no otro dato económico.
content_type y retry_after simulan cabeceras; error=timeout lanza TimeoutError.
body_file permanece dentro de esta carpeta. La simulación consume pasos: preparar
un transporte nuevo para repetir. Los archivos se leen y no se modifican.
