# Mi contrato de producto

Estado: borrador de diseño. Completar y revisar; no equivale a producto ejecutable.

## Público y necesidad

¿Quién utiliza el resultado y para qué decisión o revisión concreta?

## Pregunta verificable y límites

Escribe una pregunta con población, corte, unidad y filtros. Indica qué no se
puede concluir y qué queda fuera del producto esencial.

## Entrada y diccionario

Procedencia sintética, unidad de fila, claves, campos/tipos/unidades, ausencias,
rangos, categorías y volumen cubierto. ¿Se valida toda la fuente antes del filtro?

## Parámetros y reglas

Nombres, valores admitidos, frontera inclusiva/exclusiva, segmentos vacíos,
numeradores/denominadores, orden y precisión de presentación.

## Estados

Define resultado válido, cero, selección vacía, corte ausente, rechazo y bloqueo.
Aclara qué puede mostrarse como resultado nuevo y qué ocurre con resultados previos.

## Productos y alternativa elegida

Reporte HTML y una app local: ¿Streamlit o Shiny? Explica por qué basta esa ruta.
¿Qué datos/contexto deben coincidir entre tabla, figura y descarga?

## Aceptación y evidencia

| Caso / entrada | Resultado esperado por clave y medidas | Cómo se revisará | Estado real |
| --- | --- | --- | --- |
| Caso habitual | Completar antes de calcular | Referencia independiente y futura integración | Pendiente |
| Frontera / cero | Completar | Completar | Pendiente |
| Vacío / ausencia | Completar por separado | Completar | Pendiente |
| Entrada/fuente inválida | Completar | Completar | Pendiente |

## Revisión y cambios

Versión de reglas, dudas abiertas y cambios que obligarían a revisar el contrato.
Separa comprobaciones aritméticas actuales de integración/reconstrucción futura.
