# Lab 13.07 — Gráficos, tablas y descargas

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.07**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Conciliar gráfica, tabla e indicadores con dos archivos descargados |
| **Entrada** | Copia nueva con cartera de seis filas y ggplot2 local |
| **Evidencia** | Descargas releídas, predicciones por clave y casos vacío/bloqueado |

[Lección 13.07](../../../curriculum/13_shiny_web/07_outputs_downloads/README.md) · [Actividad](#actividad) · [Comprobación](#resultado-y-comprobación)

## Relación y preparación

Refuerza [13.07](../../../curriculum/13_shiny_web/07_outputs_downloads/README.md).
Sigue [los recorridos](../../../curriculum/13_shiny_web/07_outputs_downloads/recorridos.md)
en el IDE, sobre una carpeta nueva. Revisa DESCRIPTION/renv.lock y restaura la
biblioteca local: esta sección incorpora ggplot2. No instala globalmente ni
exige entregas anteriores. No hay proyecto/checkpoint implementado por este lab.

La fuente conserva 001/002/003: septiembre 0/2000/2500 y octubre 100/1900/2600
MXN. Una fila es un crédito en un corte. Saldo >= mínimo, cobertura sobre los
tres créditos del corte y ningún segmento significa ninguna fila.

## Actividad

### 1. La primera descarga real

Inicia minimo.R y descarga creditos_minimo.csv. Ábrelo en el editor: encabezado
credito/saldo_mxn y tres filas, IDs con ceros y sin índice extra. Detén el
servidor para usar la consola R del mismo IDE si vas a importar el archivo.
Léelo con colClasses que conserve credito como character y saldo como numeric.
Comprueba tres filas y 4500 MXN. Explica filename, content(file) y row.names = FALSE.

### 2. Una consulta y varias representaciones

Detén el mínimo, inicia app.R y aplica septiembre/ambos/2000. Predice y comprueba:

- Tabla: 002/servicios/2026-09-30/2000 y 003/comercio/2026-09-30/2500.
- Gráfica: categorías 002/003, alturas y etiquetas 2000/2500, eje MXN, corte septiembre.
- Indicadores: dos créditos, 4500 MXN y 66.67% de tres.

Descarga selección y contexto antes de aplicar otra consulta. Guárdalos juntos
en una carpeta de esta consulta, conservando los nombres que eligió el navegador.
Relee ambos: cuatro columnas/dos filas en selección y una fila de contexto con
ambos segmentos, mínimo 2000, regla inclusiva, universo tres/4500 y selección
dos/4500. Comprueba que el porcentaje almacenado no se limitó a 66.67 por formato.

### 3. Borrador pendiente y presentación

Edita octubre y mínimo 0 **sin aplicar**. Descarga ambos archivos otra vez a
otra carpeta: todavía deben describir septiembre/ambos/2000. Comprueba también
subtítulo y texto alternativo de la imagen; no deben usar el borrador.

Oculta la tabla, descarga y vuelve a mostrarla. La consulta no cambia. Después
aplica octubre/ambos/0: tres filas, barras 100/1900/2600, tres créditos y 4600 MXN.
Descarga ambos y relee. No mezcles el contexto de una consulta con filas de otra.

En el navegador, el texto alternativo se puede consultar con las herramientas
de inspección de la imagen; el código también muestra cómo se construye. Quien
acompaña puede ayudar a localizarlo. No basta la existencia del atributo: revisa
que corte, IDs y saldos correspondan a la consulta aplicada.

### 4. Cero observado y vacío exportable

Aplica septiembre/comercio/0. Debe conservar 001/0 y 003/2500: dos filas y dos
categorías, una barra sin altura con etiqueta 0, total 2500 y cobertura 66.67%.
Descarga y comprueba que 001 no desaparece del CSV.

Aplica mínimo 1 en esa consulta: solo 003/2500, cobertura 33.33%. La suma coincide;
explica por qué una revisión de totales no detectaría perder el crédito cero.

Desmarca ambos segmentos y aplica. Espera cero seleccionados/0 MXN/0%; la tabla
y la gráfica deben explicar que no hay filas/barras. Descarga selección: solo
encabezado con cuatro columnas, no una fila de ceros. El contexto sigue teniendo
una fila con universo tres y selección cero. Recupera ambos segmentos y aplica
para comprobar recuperación de gráfica y descargas.

### 5. No ofrecer archivos de una consulta bloqueada

Aplica noviembre: no hay universo, indicadores ni botones de descarga. No debe
presentarse como un CSV vacío válido de selección sobre tres créditos.

Vuelve a septiembre/ambos/2000 y aplica. En el explorador, renombra cartera.csv
de **tu copia** como cartera_ausente.csv, conservando su contenido. Mantén el
servidor y pulsa Aplicar: debe retirar cifras, gráfica y botones. Recupera el
nombre y aplica: se recuperan consulta y descargas. No modifiques la fuente del curso.

Un rechazo de mínimo decimal con una consulta anterior válida es otro caso:
se conserva la consulta identificada y se pueden descargar sus archivos. El
rechazo no publica un archivo del borrador inválido. Comprueba esa distinción.

### 6. Justificar el flujo

Localiza disponible() en app.R y qué leen gráfica, alt y los dos handlers.
Explica por qué ocultar botones no sustituye validar al ejecutar la descarga.
Señala qué escribe cada función de presentacion.R y por qué no modifica filtros.

**Ampliación opcional:** en una copia de revisión, cambia geom_col por geom_bar
sin cambiar su estadística. El mapeo y no corresponde al conteo predeterminado;
puede producir un diagnóstico en lugar de la figura esperada. Explica la
diferencia sin instalar nada, y restaura geom_col. No necesitas romper la app
para demostrarlo: una predicción razonada con la documentación también sirve.

<details>
<summary>Ver una pista para releer</summary>

CSV no conserva esquema. Usa ID/segmento/corte como texto y saldo como numeric.
Lee contexto como character y convierte solo los campos numéricos para comparar.
Con filas vacías, verifica encabezado y cero registros, no un valor imputado.
El nombre del archivo ayuda a identificar el corte, pero no prueba sus filtros.

</details>

## Resultado y comprobación

Debes poder explicar qué representa cada barra y cada archivo, conciliar las
filas completas y demostrar pendiente/vacío/bloqueo. El éxito del clic no prueba
equivalencia; la relectura y comparación con la fuente y contexto sí la contrastan.

<details>
<summary>Ver solución razonada</summary>

El mínimo exporta 001/0, 002/2000 y 003/2500. Septiembre/ambos/2000 exporta
002/2000 y 003/2500, suma 4500 y cobertura 2/3; preparar octubre sin aplicar
no cambia archivo, gráfica ni contexto. Octubre/ambos/0 da tres créditos/4600.

Septiembre/comercio/0 conserva cero y 2500; con mínimo 1 conserva solo 2500.
Ningún segmento da selección CSV con encabezado y cero filas, contexto una fila
y cobertura 0% sobre tres. Noviembre no tiene universo y no ofrece descargas.
Fuente ausente detectada al aplicar retira la consulta; restaurar y aplicar la
reconstruye. Un borrador inválido conserva únicamente la consulta aplicada anterior.

</details>

## Evidencia y reflexión

Conserva pares de CSV por consulta, notas de relectura y una explicación de
alturas/etiquetas. Guarda ayudas y dudas en tu copia personal, fuera de PROGRESS.md.
Quien acompaña elige un archivo y pide reconstruir sus filtros y valores.

- ¿Qué diferencia hay entre el nombre sugerido y la ruta temporal file?
- ¿Cómo detectarías contexto de octubre junto a filas de septiembre?
- ¿Qué ocurre si la fuente cambia sin aplicar antes de descargar?
- ¿Por qué estos dos archivos no son todavía una entrega reconstruible completa?

## Siguiente paso

Continúa con [13.08 — Organización y módulos](../../../curriculum/13_shiny_web/08_organization_modules/README.md), ya disponible.

[← Lección 13.07](../../../curriculum/13_shiny_web/07_outputs_downloads/README.md) · [Módulo 13](../../../curriculum/13_shiny_web/README.md)
