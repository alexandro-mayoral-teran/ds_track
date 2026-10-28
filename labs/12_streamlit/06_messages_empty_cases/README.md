# Lab 12.06 — Explicar el vacío y recuperar la lectura

[Inicio](../../../README.md) / [Labs](../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.06**

## Propósito

Distinguir qué se sabe en cada situación, conservar filtros válidos sin ocultar
un intento rechazado y recuperar la app después de corregir su fuente.

## Entradas y preparación

- [Lección 12.06](../../../curriculum/12_streamlit/06_messages_empty_cases/README.md)
  y [recorridos por shell](../../../curriculum/12_streamlit/06_messages_empty_cases/recorridos.md).
- Mismo entorno local de 12.01; no hay nuevas dependencias ni entregas previas obligatorias.
- Prepara una carpeta nueva, por ejemplo `output/practica_1206`, desde el repositorio.
  Ejecuta sus archivos, no el app.py fuente de la sección.
- Guarda una copia del CSV preparado como `cartera_respaldo.csv` en esa carpeta.
  Todas las variantes de este lab se hacen en tu copia, conservando las fuentes originales.

## Predicción

1. ¿Cómo distingues un crédito con saldo cero de ningún crédito seleccionado?
2. Si envías un mínimo decimal, ¿qué filtros y cifras deben permanecer?
3. ¿Noviembre sin registros significa que su cartera vale cero?
4. ¿Un CSV de cero bytes equivale a un CSV con solo encabezado?
5. ¿Mostrar un mensaje de error evita por sí mismo que continúe el cálculo?

## Actividad

1. Ejecuta el mínimo y elige sus cuatro escenarios. Registra mensaje, cantidad
   seleccionada y si presenta un saldo. Después detén ese servidor y abre la app completa.
2. En la muestra completa aplica septiembre/ambos/2001: 003/2500, universo 4500.
   Prepara octubre con `2000.5` y confirma. El intento debe rechazarse y conservar
   los filtros anteriores bajo una etiqueta clara, sin contar un envío válido.
   Oculta y muestra detalle: el aviso sigue visible. Corrige a `2000` y aplica.
3. Aplica noviembre. Debes obtener un aviso de corte ausente, sin métricas.
   Recupera octubre mediante otro envío válido.
4. Aplica octubre, solo servicios, mínimo 2000. Verifica selección vacía, universo
   3/4600 y métricas 0/0/0%. Oculta detalle: el mensaje debe permanecer. Vacía
   segmentos y aplica: ahora el mensaje debe explicar «ninguno».
5. Con una selección conocida ya calculada, renombra **el CSV de tu copia** a
   `cartera_guardada.csv`. Pulsa «Reintentar lectura». Revisa el mensaje principal,
   la acción y el diagnóstico; no deben quedar indicadores anteriores visibles.
   Restaura el nombre cartera.csv y reintenta. No limpies caché para fingir reparación.
6. En cartera.csv deja solo el encabezado correcto y reintenta. Debe advertir que
   no hay registros, sin métricas. Después deja el archivo de cero bytes y
   reintenta: debe rechazar el contrato por falta de encabezado.
7. Restaura el respaldo y agrega otra vez la fila de 001/septiembre. Pregunta
   por octubre: la clave duplicada fuera del filtro debe bloquear indicadores.
   Vuelve al respaldo y comprueba recuperación.
8. En una última variante deja encabezado y la fila 001/septiembre/saldo 0.
   Aplica septiembre, ambos segmentos, mínimo 0: un crédito, saldo conocido 0,
   100% del universo de esa variante. No es el filtro vacío del paso 4.
9. Restaura la muestra completa desde tu respaldo y reintenta. Aplica octubre/
   ambos/2000 y comprueba 003/2600, universo 3/4600 y 33.33%. Conserva tu nota.

## Resultado y comprobación

| Situación | Qué debe ocurrir |
| --- | --- |
| Mínimo `2000.5` después de septiembre/2001 | Rechazo; últimos filtros válidos y 003/2500 claramente identificados |
| Noviembre | Sin registros para el corte, proporción indefinida, sin métricas |
| Octubre servicios ≥ 2000 | Cero seleccionados, 0 MXN de selección, 0%; universo 3/4600 |
| Ningún segmento | Selección vacía válida, con indicación de elegir segmentos |
| Archivo ausente o contrato inválido | Error y acción; ninguna cifra de fuente presentada como válida |
| Encabezado sin filas | Advertencia de fuente sin registros, sin métricas |
| Variante de un crédito con saldo cero | Un seleccionado, 0 MXN y 100% de esa variante |
| Respaldo restaurado y filtros iniciales | 003/2600, universo 3/4600, 33.33% |

<details>
<summary><strong>Ver solución razonada</strong></summary>

El mínimo decimal nunca se convierte en entero para truncarlo. El validador
rechaza el intento y no reemplaza los parámetros aplicados. La pantalla explica
que sigue utilizando los últimos filtros válidos sobre la fuente actual.

Con universo de tres y selección vacía, 0/3 es 0% y la suma de selección es cero.
Sin registros de noviembre no hay denominador; mostrar saldo cero como observado
sería engañoso. Un crédito registrado con saldo cero sí permite un resultado
observado: cantidad uno y saldo cero.

El encabezado sin filas cumple la forma del CSV; el archivo de cero bytes no
tiene ese encabezado. Un fallo de lectura o contrato se explica y detiene la
pasada antes de caché. Restaurar la fuente y reintentar corrige la entrada;
borrar caché sin arreglar el archivo no lo vuelve válido.

</details>

## Evidencia y reflexión

Conserva copia y respaldo, más una tabla de situación, mensaje, acción, filtros
efectivos y cifras permitidas. Una captura del intento rechazado y otra del corte
vacío pueden ayudar; no es obligatorio capturar cada combinación.

- ¿Por qué el mensaje de vacío debe quedar fuera de «Mostrar detalle»?
- ¿Qué explica el diagnóstico y qué debe resolver el mensaje principal?
- ¿Qué pasaría si un error de lectura devolviera `[]` para continuar?
- ¿Qué diferencia hay entre conservar parámetros válidos y congelar datos?
- ¿Qué pasos te permitirán retomar mañana con la muestra completa?

Revisa con tu compañero y guarda ayudas, dudas y siguiente paso en tu bitácora
personal. PROGRESS.md registra autoría del material, no aprendizaje. No hay
proyecto ni checkpoint asociado todavía.

## Siguiente paso

Vuelve al [criterio de salida](../../../curriculum/12_streamlit/06_messages_empty_cases/README.md#evidencia-y-criterio-de-salida)
y después consulta [12.07 — Tablas, gráficos y descarga](../../../curriculum/12_streamlit/07_tables_charts_download/README.md).
