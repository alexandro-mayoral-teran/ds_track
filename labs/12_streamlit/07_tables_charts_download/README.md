# Lab 12.07 — Conciliar pantalla y archivos

[Inicio](../../../README.md) / [Labs](../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.07**

## Propósito

Comprobar que tabla, gráfico, indicadores y archivos representan la misma selección
aplicada, conservando el contexto para revisarla después.

## Entradas y preparación

- [Lección 12.07](../../../curriculum/12_streamlit/07_tables_charts_download/README.md)
  y [recorridos por shell](../../../curriculum/12_streamlit/07_tables_charts_download/recorridos.md).
- Mismo entorno local de 12.01, con Altair ya declarado; sin dependencias nuevas.
- Prepara una carpeta nueva, por ejemplo `output/practica_1207`. No necesitas
  salidas de otros labs. Trabaja sobre esa copia y respalda su cartera.csv antes de variarla.
- Elige una carpeta personal para conservar los CSV y JSON descargados. El
  navegador puede ofrecer otra ubicación o cambiar el nombre si ya existe.

## Predicción

1. Septiembre/ambos/2000: ¿qué dos barras y registros deben aparecer?
2. ¿Qué archivo debe obtenerse al editar octubre sin confirmar el formulario?
3. ¿Qué debe contener el CSV de una selección vacía con universo válido?
4. ¿Por qué guardar también el JSON si el CSV ya contiene los importes?

## Actividad

1. Ejecuta el mínimo. Recupera sus dos filas, dos barras y CSV con suma 4500 MXN.
   Revisa el archivo como texto para comprobar IDs `002` y `003`.
2. En la app completa, aplica septiembre/ambos/2000. Contrasta tabla, etiquetas,
   tooltip y métricas. Descarga CSV y contexto. Relee los cuatro campos por fila:
   002/servicios/septiembre/2000 y 003/comercio/septiembre/2500.
3. Comprueba en el contexto filtros, universo 3/4500, seleccionados 2/4500 y
   porcentaje 66.666... (la pantalla redondea a 66.67%). Verifica su huella del CSV
   según el apoyo de los recorridos. Ocultar detalle no debe cambiar los archivos.
4. Prepara octubre con mínimo 2000, sin enviar. Descarga otra vez: debe seguir
   correspondiendo a septiembre. Confirma los filtros y descarga de nuevo:
   ahora 003/octubre/2600, universo 3/4600 y 33.33% de créditos.
5. Envía `2000.5`. Se identifica el intento rechazado y los botones quedan
   deshabilitados. Corrige a `2000` y confirma: deben volver a habilitarse.
6. Aplica octubre/servicios/2000: selección vacía, universo válido. Descarga CSV
   y contexto: encabezado sin filas, cantidad/saldo seleccionados 0 y universo
   3/4600. No debe aparecer una barra con un crédito inventado.
7. Aplica noviembre: no hay universo del corte; sin métricas ni botones de
   descarga. Vuelve a octubre/ambos/2000 y comprueba recuperación.
8. En el CSV de tu copia cambia solo 003/octubre de 2600 a 2800. Pulsa «Reintentar
   lectura» antes de descargar. Contrasta gráfico, fila, CSV y contexto: 2800
   seleccionado, universo 4800 y uno de tres. Los archivos previos siguen siendo
   copias de su vista anterior; conserva ambos casos con nombres que permitan distinguirlos.
9. Introduce una clave repetida de septiembre en tu copia y reintenta. Deben
   desaparecer indicadores, gráfico y botones de esa vista. Restaura el respaldo
   y recupera el caso original 003/2600, universo 4600.

## Resultado y comprobación

| Caso | Filas y barras | Archivo y contexto |
| --- | --- | --- |
| Septiembre ≥ 2000, ambos | 002/2000 y 003/2500 | Dos filas, suma 4500; universo 3/4500 |
| Octubre ≥ 2000, ambos | 003/2600 | Una fila, 2600; universo 3/4600 |
| Borrador sin enviar | Sigue el caso aplicado | Sigue el archivo de esa vista |
| Filtro rechazado | Últimos filtros válidos identificados | Descarga deshabilitada hasta corregir |
| Selección vacía válida | Ninguna barra ni fila | Encabezado CSV, cero seleccionados y universo conservado |
| Corte ausente o fuente inválida | Sin resultados actuales | No ofrece descargas de esa vista |
| Variante releída | 003/2800 | Una fila, 2800; universo 3/4800 y huella correspondiente |

<details>
<summary><strong>Ver solución razonada</strong></summary>

El resultado del análisis es único: su selección alimenta tabla, gráfico y CSV.
El contexto añade filtros, universo e indicadores, además de una huella de los
bytes del CSV. Comparar solo sumas podría ocultar un intercambio de importes;
por eso se revisa ID, segmento, corte y saldo de cada registro.

El formulario pendiente no reemplaza los filtros aplicados. El botón descarga
bytes ya preparados y no vuelve a leer al hacer clic. Tras cambiar datos se
requiere otra pasada para obtener una vista nueva. Un filtro vacío con universo
válido sí puede exportarse; la falta de fuente o de corte observado no se
presenta como una selección de cartera válida.

La variante aumenta saldo seleccionado y universo en 200 MXN, pero sigue un
crédito de tres. El porcentaje permanece en 33.33%. La huella relaciona los dos
archivos descargados; no demuestra autoría ni autenticidad de una entrega.

</details>

## Evidencia y reflexión

Conserva CSV y JSON de dos casos, predicción y comprobación por clave. Una captura
de las barras puede ayudar, pero no reemplaza los valores recuperables.

- ¿Qué condición evitaría exportar un conjunto distinto del mostrado?
- ¿Por qué CSV no garantiza que una hoja de cálculo conserve los ceros del ID?
- ¿Qué significa `on_click="ignore"` para la actualidad de la descarga?
- ¿Qué información del universo falta si guardas solamente el CSV seleccionado?
- ¿Cómo detectarías mezclar un CSV viejo con el contexto de otra pasada?

Revisa con tu compañero y registra ayudas y dudas en tu bitácora personal.
PROGRESS.md registra desarrollo, no aprendizaje; proyecto/checkpoints pendientes.

## Siguiente paso

Revisa el [criterio de salida](../../../curriculum/12_streamlit/07_tables_charts_download/README.md#evidencia-y-criterio-de-salida).
Retoma después [12.08 — Pruebas de la aplicación](../../../curriculum/12_streamlit/README.md#08-pruebas-de-la-aplicacion),
todavía planificado. El [punto de reanudación](../../../docs/streamlit-closure.md) distingue material disponible de trabajo pendiente.
