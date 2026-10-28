# Lab 13.06 — Validación y mensajes

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.06**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Mostrar una causa y una acción sin convertir fallos en indicadores |
| **Entrada** | Copia nueva de 13.06, seis observaciones y respaldo local de su CSV |
| **Evidencia** | Matriz causa/mensaje/cifras y una recuperación desde fuente corregida |

[Lección 13.06](../../../curriculum/13_shiny_web/06_validation_messages/README.md) · [Actividad](#actividad) · [Comprobación](#resultado-y-comprobación)

## Relación y preparación

Refuerza [13.06](../../../curriculum/13_shiny_web/06_validation_messages/README.md).
Sigue [preparación y arranque](../../../curriculum/13_shiny_web/06_validation_messages/recorridos.md)
desde el IDE, en carpeta nueva. No exige entregas ni tiene proyecto/checkpoint
implementado. Trabaja solo con tu copia, conservando el CSV del curso.

Antes de iniciar la app, duplica cartera.csv de la copia como
cartera_respaldo.csv. Usa el explorador/administrador de archivos y el editor
del IDE para renombrar y editar mientras el servidor ocupa la consola R; no
intentes ejecutar código en esa consola ocupada. Conserva siempre el respaldo
íntegro y restaura cartera.csv al terminar. No uses Excel para esta actividad:
el editor de texto permite conservar IDs, fechas y estructura sin conversiones.

## Actividad

### 1. Requerir y explicar

Inicia minimo.R. Escribe 2000, vacío, 1.5, 2501 y 0; espera cada resultado.
Registra qué salidas muestran mensaje y cuáles siguen disponibles. Explica:

- Qué evita la guarda req durante el inicio sin valor recibido.
- Por qué validate/need de la expresión se propaga a texto y tabla.
- Por qué 2501 es un mínimo válido aunque no seleccione filas.
- Por qué saldo cero no se debe eliminar por «veracidad».

Localiza `nrow(seleccion) > 0L`: no lo reemplaces por req(nrow(seleccion)).
Detén el mínimo y arranca app.R.

### 2. Rechazar un borrador y conservar una consulta identificada

Aplica septiembre/ambos/2000: 002/003, dos créditos, 4500 MXN, cobertura 66.67%.
Edita mínimo vacío y aplica. Después prueba 1900.5, -1, 1e3 y 1000001, aplicando
cada uno. Anota la causa y la acción que pide el mensaje. El contexto y las
cifras deben seguir describiendo la última consulta aplicada, no el borrador.

Corrige a 2000 sin aplicar: eso no envía filtros. Aplica para recuperar el aviso
de éxito. Explica por qué as.integer("1900.5") no sería una corrección legítima.

### 3. Cero, vacío y fecha sin universo

Predice antes de aplicar y contrasta con las seis filas conocidas:

| Caso | Qué registrar |
| --- | --- |
| Septiembre/comercio/0 | 001/0 y 003/2500, cantidad y porcentaje |
| Septiembre/comercio/1 | Cambio de filas/conteo aunque la suma sea igual |
| Septiembre/ninguno/0 | Universo existente, indicadores cero y mensaje de tabla |
| Octubre/servicios/1901 | Filtro sin coincidencias, recuperación bajando a 1900 |
| Noviembre/ambos/2000 | Corte aplicado sin registros; indicadores ausentes |

Desmarca Mostrar tabla en el caso vacío y después en noviembre: el aviso general
debe seguir visible. Ocultar la tabla no aplica otros filtros ni resuelve la causa.
Vuelve a septiembre/ambos/2000 y aplica antes del siguiente bloque.

### 4. Fuente ausente, inválida y vacía

Con el servidor funcionando, actúa sobre archivos **de tu copia** mediante el
explorador y el editor. No reinicies entre estos pasos: queremos comprobar la
relectura al aplicar.

1. Renombra cartera.csv como cartera_ausente.csv. La página conserva la instantánea
   hasta que pulses Aplicar. Al aplicar debe indicar archivo ausente y retirar
   las cifras anteriores, no mostrar 0 MXN. Comprueba también con tabla oculta.
2. Recupera el nombre cartera.csv y aplica: regresan 2/4500 y 66.67%.
3. Con septiembre elegido, duplica al final la fila de octubre
   `003,comercio,2026-10-31,2600`. Guarda y aplica: debe bloquear por fuente
   inválida aunque esa fila esté fuera del corte solicitado. Revisa el diagnóstico
   de clave repetida en consola; el mensaje de UI indica qué revisar sin publicar cifras.
4. Restaura desde el respaldo íntegro y aplica para recuperar.
5. En cartera.csv conserva solo la línea de encabezado, guarda y aplica. Esa
   tabla no tiene registros de septiembre: no debe publicar porcentaje 0%.
6. Restaura otra vez el contenido íntegro y aplica. Contrasta todas las celdas,
   no solo la suma. Conserva los archivos de respaldo para explicar la recuperación.

**Ampliación opcional:** prueba fuente ausente y mínimo inválido a la vez. La
prioridad es fuente: retira cifras y pide recuperar el archivo. No diagnostiques
el conjunto como una selección vacía ni sigas ajustando mínimos para arreglarlo.

### 5. Sesiones e instantáneas

Abre una pestaña B, aplica octubre y conserva A en septiembre. Editar A no
cambia B. Si cambias el archivo, B no se actualiza automáticamente: comprueba
que solo detecta el estado de la fuente al volver a aplicar. Restaura el CSV
antes de terminar; esto no es un monitor de archivos ni una invalidación global.

<details>
<summary>Ver una pista sobre mensajes y cifras</summary>

Pregunta primero si la fuente es utilizable, después si el borrador es válido,
y luego si existe universo/selección. El rechazo conserva la consulta anterior
identificada. El bloqueo de fuente no debe conservar cifras disponibles. Una
selección vacía sí puede sumar 0; una falla no se convierte en esa selección.

</details>

## Resultado y comprobación

Entrega una matriz breve: situación, mensaje observado, contexto/cifras que
permanecen o se retiran y acción que recupera la consulta. Incluye una fila cero,
un vacío, noviembre, una fuente inválida fuera del filtro y la recuperación.

<details>
<summary>Ver solución razonada</summary>

Septiembre/comercio/0 da 001/003, 2/2500/66.67%; con 1 da 003, 1/2500/33.33%.
Ningún segmento o servicios/octubre/1901 da cero seleccionados sobre tres,
suma 0 y cobertura 0%. Noviembre no tiene universo y no ofrece indicadores.
El mínimo inválido mantiene la consulta anterior con aviso de rechazo.

Fuente ausente o con clave repetida retira las cifras al aplicar. El CSV solo
con encabezado conserva estructura, pero no hay universo del corte. Recuperar
el archivo íntegro y aplicar reconstruye septiembre 002/003, 2/4500/66.67%.
Tabla oculta no elimina avisos generales; cada sesión comprueba al aplicar.

</details>

## Evidencia y reflexión

Guarda matriz, archivos de respaldo y dudas en tu copia personal, fuera de
PROGRESS.md. Quien acompaña revisa una predicción y una recuperación completa.

- ¿Qué puede ocultar un tryCatch que convierte cualquier error en tabla vacía?
- ¿Por qué conservar solo una salida con cancelOutput no asegura coherencia?
- ¿Qué distingue archivo vacío sin encabezado de CSV válido solo con encabezado?
- ¿Qué garantiza la comprobación por aplicación y qué no garantiza entre aplicaciones?

## Siguiente paso

Continúa con [13.07 — Gráficos, tablas y descargas](../../../curriculum/13_shiny_web/07_outputs_downloads/README.md),
ya disponible.

[← Lección 13.06](../../../curriculum/13_shiny_web/06_validation_messages/README.md) · [Módulo 13](../../../curriculum/13_shiny_web/README.md)
