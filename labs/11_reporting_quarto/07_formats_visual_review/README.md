# Lab 11.07 — Revisar el HTML que vas a entregar

## Relación, entrada y resultado

- Lección: [11.07 — Formatos y revisión visual](../../../curriculum/11_reporting_quarto/07_formats_visual_review/README.md).
- Entrada: seis filas propias, documentos y CSS preparados según el motor elegido.
- Resultado: HTML revisado, corrección de presentación y nota de evidencias/límites.
- Proyecto/checkpoint: todavía no aplica; `05_monthly_report` sigue previsto.

Reserva 45–75 minutos o dos sesiones. Un motor basta. No requiere entregas
anteriores ni PDF. Usa copias de práctica; conserva los archivos originales.

## A. Un mínimo estático y un reporte calculado

1. Renderiza el mínimo a HTML y sigue la referencia a su tabla.
2. En una copia cambia 2500 por 3000. Predice qué pasa con el texto «3500».
3. Corrige el texto estático a 4000 y conserva la explicación.
4. Renderiza el reporte ejecutable. Identifica la fuente común de cifras,
   resumen, detalle y barras; predice los resultados antes de leerlos.

<details>
<summary>Comprobación razonada de A</summary>

El mínimo no ejecuta cálculos: el texto 3500 no cambia al editar una celda de
la tabla. En el reporte ejecutable, septiembre suma 6000, octubre 6300 y la
diferencia es 300 (5.00% sobre septiembre). Los tres pares son 1000/1200,
2000/1800 y 3000/3300. El agregado positivo no implica que cada crédito aumente.

</details>

## B. Revisar navegación, tabla y figura

1. Abre el HTML generado, recorre el índice y las referencias a tablas/figura.
2. Comprueba cada ID, fecha, saldo y diferencia contra el CSV.
3. Estrecha la ventana. Comprueba que el cuerpo cabe y que puedes llegar a la
   última columna de la tabla sin perder registros.
4. Con Tab alcanza el recuadro; comprueba su contorno y usa las flechas para
   desplazarte. Prueba también el control con ratón o panel táctil.
5. Amplía al 200% y anota qué observaste; no marques esa prueba si no la hiciste.
6. Explica caption, fuente y texto alternativo. Contrasta alturas/etiquetas de
   barras con la tabla; no dependas solo del color.

<details>
<summary>Pista de B</summary>

La página completa y el recuadro de la tabla son superficies distintas.
Comprueba qué elemento recibe el foco y cuál se desplaza. El verificador puede
encontrar los atributos correctos sin demostrar que el CSS funcione.

</details>

<details>
<summary>Solución razonada de B</summary>

La tabla conserva seis columnas y tres créditos. El desplazamiento pertenece
al recuadro, el foco tiene contorno visible y el índice permite llegar a cada
sección. Las barras son 6000/6300 y parten de cero. La tabla de resumen y el
párrafo conservan cifras exactas cuando la figura se vea pequeña. Caption,
procedencia y alternativa textual tienen propósitos distintos; ninguno
certifica accesibilidad completa por sí solo.

</details>

## C. Corregir un problema de presentación en una copia

1. Conserva el CSS que funciona y un HTML revisado.
2. En el CSS de tu práctica comenta temporalmente la regla
   `.tabla-ancha .cell-output-display { overflow: visible; }` usando `/* ... */`.
3. Renderiza y repite la prueba de teclado en una ventana estrecha.
4. Describe si el contenedor interior captura el desplazamiento en tu versión
   de Quarto. Si no reproduce el problema, registra eso sin inventar un fallo.
5. Restaura la regla, renderiza y vuelve a comprobar foco y desplazamiento.

<details>
<summary>Solución razonada de C</summary>

En Quarto 1.9.38 el resultado de la celda puede tener su propio overflow auto.
La región exterior recibe Tab, pero el desbordamiento queda dentro: las flechas
no desplazan el recuadro enfocado. Dejar visible el overflow de esa celda permite
que el recuadro exterior sea quien se desplace. El CSV y los cálculos no cambian.
Una comprobación estructural puede pasar en las dos versiones; la prueba de
uso permite distinguirlas. No arregles el problema ocultando columnas.

</details>

## D. Actualización y cambio compensado

1. En tu CSV cambia solo 003/octubre de 3300 a 3600. Predice las cifras.
2. Abre primero el HTML anterior y explica por qué no cambió.
3. Renderiza el documento explícito con refresco, revisa texto, tablas y barras.
4. Restaura la muestra. Después aumenta 001/octubre a 1300 y baja 002/octubre
   a 1700. Predice el total y el detalle antes de renderizar.
5. Comprueba por valor, no solo por suma. Puedes usar el verificador estándar
   de la lección o documentar la revisión manual en el recorrido R.
6. Restaura la muestra al cerrar o conserva claramente identificada tu variante.

<details>
<summary>Solución razonada de D</summary>

Con 003/octubre = 3600 aparecen 6000/6600, diferencia 600 y 10.00%. Abrir el
HTML previo no ejecuta código. En el cambio compensado el agregado vuelve a
6000/6300, diferencia 300 y 5.00%, pero los pares 001/002 y sus diferencias
cambian. El detalle debe reflejarlo; las sumas y barras iguales no prueban
que cada crédito esté actualizado. El verificador rechaza el HTML anterior
contra ese CSV aunque sus totales coincidan.

</details>

## E. Pareja, evidencia y reflexión individual

Una persona predice y maneja el teclado; la otra contrasta la fuente y registra
incidencias. Cambien papeles entre B y D. Cada persona explica después:

- ¿Qué puede pasar aunque el render termine sin errores?
- ¿Qué comprobación detectó el problema de tabla que los atributos no detectaban?
- ¿Por qué una tabla de cifras ayuda aunque exista texto alternativo?
- ¿Qué parte comprobaste visualmente, cuál automáticamente y cuál no probaste?

Conserva una nota con HTML, motor/versiones, fuente, anchos/zoom, prueba,
resultado, corrección y límites. Adjunta la evidencia necesaria sin publicar
carpetas personales ni instalar herramientas globales. El verificador no
autentica la fecha histórica de una ejecución.

## Ampliación opcional: PDF

Solo si ya tienes TeX adecuado, genera el mínimo PDF siguiendo la lección.
Revisa todas sus páginas y contrasta la tabla, acentos y referencia. No cambies
la extensión del HTML para simular una conversión. Si falta motor/configuración,
registra el límite y conserva el HTML; no bloquea avanzar. No se exige convertir
el reporte ejecutable completo ni instalar paquetes para terminar este lab.

## Criterio de salida y siguiente paso

Puedes avanzar al entregar un HTML legible con valores conciliados, navegación
funcional y tabla de detalle alcanzable, explicando lo que quedó fuera.
Registra la evidencia en [PROGRESS.md](../../../PROGRESS.md).

Continúa con [11.08 — Dashboard y distribución](../../../curriculum/11_reporting_quarto/08_dashboard_distribution/README.md),
ampliación disponible. El cierre esencial 11.09 sigue previsto;
no hay otro lab disponible que sustituya la siguiente lección.
