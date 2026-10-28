# Contrato de la entrega Shiny 13.10

Fuente sintética, sin datos personales. Una fila representa un crédito en un
corte; la clave es id_credito/fecha_corte. Columnas en orden:

| Columna | Regla |
| --- | --- |
| id_credito | Texto de tres dígitos; conservar ceros iniciales |
| segmento | comercio o servicios |
| fecha_corte | Texto YYYY-MM-DD, calendario válido, años 1900–2100 |
| saldo_mxn | Pesos enteros de 0 a 1000000; 0 conocido es válido |

No se admiten ausencias, claves repetidas ni más de 10000 observaciones.
El lector CSV exige saldo textual canónico, sin signos, espacios, decimales
o ceros iniciales salvo 0. Se valida toda la fuente antes de filtrar.

La muestra conocida contiene tres créditos por corte:

| Crédito / segmento | 2026-09-30 | 2026-10-31 |
| --- | ---: | ---: |
| 001 / comercio | 0 | 100 |
| 002 / servicios | 2000 | 1900 |
| 003 / comercio | 2500 | 2600 |

Universos: 4500/4600 MXN y tres créditos en cada fecha. Selección:
segmento elegido y saldo_mxn >= minimo_mxn. Ningún segmento significa cero
filas. La cobertura es créditos seleccionados / todos los créditos del corte,
por 100; no es una proporción de saldo. El mínimo de la UI es texto canónico
0..1000000. No se limpia ni se imputa para aceptar una entrada.

casos.csv fija seis preguntas. resumen.csv conserva el caso/tipo y medidas:
sin universo tiene creditos_universo=0 y medidas de selección/porcentaje ausentes
(campos vacíos), sin ofrecer CSV de vista ni figura. Vacío sobre universo
conserva cantidad/saldo/porcentaje 0, un CSV selección con encabezado y una
fila de contexto; no inventa barras. Los PNG con filas miden 960 × 600 píxeles.

Cada panel de la app mantiene borrador y consulta aplicada por sesión. Editar
no aplica; ocultar tabla solo cambia presentación. Entrada rechazada conserva
la consulta anterior identificada; fuente ausente/inválida la retira al aplicar.
Recargar pierde estado. La fuente física es compartida, no existe monitor de
archivos ni persistencia de consultas. Aplicar relee y valida la fuente completa.

La app y los resultados de cierre se recalculan por rutas distintas de uso:
la app al aplicar; el constructor en lote a partir de casos.csv. Los CSV del
lote no son descargas HTTP pasadas. Descargar selección/contexto en navegador
son dos solicitudes: completar ambas antes de aplicar otra consulta.

Huellas MD5: integridad declarada frente a los bytes recibidos, sin firma ni
autenticidad. Verificar con referencia externa reconstruye valores por clave;
no demuestra ejecución histórica, autoría ni ausencia de otros errores. Los
PNG requieren revisión visual; el verificador solo comprueba firma/dimensiones
y huella. INFORME.md describe generación y deja la revisión humana pendiente.
