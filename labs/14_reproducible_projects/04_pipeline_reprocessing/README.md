# Lab 14.04 — Repetir un corte sin mezclar resultados

[Volver a la lección 14.04](../../../curriculum/14_reproducible_projects/04_pipeline_reprocessing/README.md) · [Módulo 14](../../../curriculum/14_reproducible_projects/README.md)

## Propósito y preparación

Demostrar con archivos que el pipeline conserva una entrega y separa consultas.
Lee la lección y sigue un [recorrido completo](../../../curriculum/14_reproducible_projects/04_pipeline_reprocessing/recorridos.md)
en una copia nueva. Elige R o Python; no necesitas entregas previas ni paquetes nuevos.
Trabaja sobre datos sintéticos. No edites fuentes del curso para hacer los ensayos.

Tiempo orientativo: 60–90 minutos, divisible en dos sesiones. La simulación y
el ensayo de alteración pueden revisarse al retomar si hoy completas los cortes.

## 1. Crear y repetir octubre

Ejecuta la configuración inicial dos veces. Debe decir creada y luego reutilizada.
Registra nombres, tamaños, fechas de modificación y huellas de los cuatro CSV
antes/después; no deben cambiar. Lee las filas: 003/2600 MXN, universo 3/4600,
selección 1 y porcentaje 33.333… . Explica por qué no se agregó otra fila de 003.

## 2. Septiembre en otro destino

Crea config/septiembre.csv como indica el recorrido, con corte 2026-09-30 y
salida salidas/septiembre. Mantén ambos segmentos y mínimo 2000. Comprueba
002/2000 y 003/2500, universo 3/4500 y selección 2/4500; porcentaje 66.666… .
Repite septiembre y verifica que octubre continúa igual. Explica qué columnas
permiten identificar el corte aunque recibas solamente los archivos de resultado.

## 3. Cambiar la pregunta sin reemplazar la respuesta anterior

Crea otra configuración con mínimo 0 pero salida salidas/octubre. Debe fallar:
conserva los cuatro archivos anteriores. Después cambia la salida a un nombre
nuevo y ejecuta: octubre selecciona 001/100, 002/1900 y 003/2600; 3/4600 y 100%.
Explica por qué tener el mismo corte no basta para reutilizar una entrega.

## 4. Vacío y ausencia de universo

Crea dos configuraciones/destinos nuevos. Para octubre, segmento servicios y
mínimo 1901: estado vacio, cero seleccionados y saldo cero, universo 3/4600,
porcentaje 0. seleccion.csv conserva sus cuatro encabezados sin filas.
Para corte 2026-11-30: se rechaza la publicación por sin_universo, sin carpeta final.
Explica por qué ese caso no merece un porcentaje cero.

## 5. Fallo y reintento

Sigue la simulación del recorrido con un destino nuevo. Conserva el mensaje y
el inventario del temporal: seleccion.csv, sin COMPLETO.csv y sin destino final.
Repite sin simulación. Debe crear una entrega final completa y conservar el
intento parcial anterior. Explica por qué un temporal no se toma como entrega.

## 6. Comprobar una alteración

Usa **otra copia de práctica o una entrega nueva reservada para el ensayo**.
Altera un saldo seleccionado; repetir debe fallar sin corregir automáticamente
el archivo. Ampliación: en septiembre cambia 2000/2500 por 1999/2501 y actualiza
las huellas del manifiesto usando la herramienta de tu lenguaje. Debe fallar
por valores distintos aunque la suma siga siendo 4500 y las huellas coincidan.
No presentes esa carpeta alterada como evidencia de una entrega válida.

<details>
<summary>Ver una explicación para revisar después del ensayo</summary>

La repetición vuelve a calcular y compara cada tabla: no añade filas ni confía
solo en el manifiesto. El universo se decide por corte antes de filtrar segmentos
y saldo. Por eso servicios con mínimo 1901 tiene selección cero y universo tres,
pero noviembre carece de denominador. El temporal fallido no es la entrega final;
el reintento genera otra carpeta y solo anuncia éxito después de comprobarla.
Una suma de 4500 no distingue 2000/2500 de 1999/2501: comparar cada valor sí.

</details>

## Evidencia y criterio de salida

Guarda una nota con configuraciones usadas, comandos/llamadas, cifras por corte,
inventarios antes/después y explicación de cada error esperado. Incluye las
versiones reales del entorno y distingue tus ensayos de la revisión de autoría.

La revisión acompañada debe poder contestar:

- ¿Qué se comprueba antes de escribir? ¿Qué depende de la fuente completa?
- ¿Qué permanece idéntico al repetir? ¿Qué requiere un destino nuevo?
- ¿Por qué una suma o una huella correctas no prueban todos los registros?
- ¿Qué riesgo queda si dos procesos escriben a la vez o el sistema se apaga?

No hay proyecto asociado ni checkpoint implementado. Puedes cerrar la sesión
tras revisar este lab. Siguiente lección: [14.05 — Pruebas y calidad de datos](../../../curriculum/14_reproducible_projects/05_tests_data_quality/README.md),
ya disponible. Para repasar vuelve a la [lección](../../../curriculum/14_reproducible_projects/04_pipeline_reprocessing/README.md).
