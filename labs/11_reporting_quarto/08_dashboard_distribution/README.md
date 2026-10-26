# Lab 11.08 — Entregar un dashboard local revisado

## Relación, entrada y resultado

- Lección: [11.08 — Dashboard y distribución](../../../curriculum/11_reporting_quarto/08_dashboard_distribution/README.md).
- Entrada: muestra de seis filas, dashboard y entorno de uno de los dos motores.
- Resultado: dashboard conciliado, carpeta de lectura nueva y nota de revisión.
- Alcance: ampliación opcional; no bloquea el cierre esencial 11.09.
- Proyecto/checkpoint: todavía no aplica; `05_monthly_report` sigue previsto.

Reserva 50–80 minutos o dos sesiones. Usa copias personales y conserva originales.
No exige entregas previas, una cuenta ni publicación en un servicio.

## A. Distinguir disposición y cálculo

1. Renderiza el mínimo estático, revisa 001/1000 y 002/2500 y su total 3500.
2. Alterna las vistas y explica qué contenido ya estaba incluido.
3. En el dashboard ejecutable identifica filas, tarjetas de valores y pestañas.
4. Predice el universo, cada tarjeta, la tasa y los tres pares antes de renderizar.

<details>
<summary>Comprobación razonada de A</summary>

El mínimo solo contiene texto/tabla: no ejecuta sumas. El dashboard ejecutable
compara tres créditos observados en ambos cortes. Las tarjetas deben mostrar
6000, 6300 y 300 MXN; tasa 5.00% sobre septiembre. Las diferencias por crédito
son 200, -200 y 300. Cambiar de pestaña no recalcula esos valores.

</details>

## B. Verificar vistas y uso

1. Sigue el recorrido completo de tu motor. Comprueba una tabla, tres tarjetas
   y una figura de dos barras, sin duplicados ni salidas auxiliares de código.
2. Contrasta todos los saldos/IDs y la tasa; usa el verificador si tienes Python
   o deja una comprobación manual completa en el recorrido R.
3. Alterna Figura y Detalle: comprueba que las tarjetas no cambian de universo.
4. En una ventana estrecha, prueba pestañas con teclado y después Tab hasta el
   recuadro de tabla. Revisa ambos extremos con flechas y el contorno de foco.
5. Comprueba que imagen, etiquetas, fuente y límites se pueden leer. Anota qué
   anchos, zoom y controles probaste realmente.

<details>
<summary>Pista de B</summary>

Compara cada dato aunque el agregado sea correcto. Para teclado, observa qué
elemento tiene el foco y cuál recibe el desplazamiento. Un atributo presente
no demuestra que un control funcione en tu navegador.

</details>

<details>
<summary>Solución razonada de B</summary>

Los pares son 001:1000/1200, 002:2000/1800 y 003:3000/3300. La figura conserva
6000/6300, eje desde cero y etiquetas por corte. La tabla permite recuperar
valores exactos sin interpretar solo colores. La tasa es diferencia/6000,
no diferencia/6300. Las pestañas muestran resultados ya incluidos; no aplican
un filtro ni ejecutan otra consulta. Las observaciones de accesibilidad se
limitan a las pruebas realizadas.

</details>

## C. Distribuir y abrir la copia final

1. Tras revisar el HTML, usa el distribuidor de tu motor para crear una carpeta
   nueva con `dashboard.html` y `LEEME.md`.
2. Repite sobre el mismo destino y conserva el mensaje de protección.
3. Abre el HTML del destino sin conexión y repite ambas vistas, tabla y figura.
4. Explica qué faltaría para reconstruir el análisis desde esa carpeta de lectura.

<details>
<summary>Solución razonada de C</summary>

El destino ocupado debe rechazarse. La igualdad de bytes/MD5 comprueba la
copia, no las cifras ni su autenticidad. En esta muestra se incorporan recursos
de lectura al HTML; la copia debe abrir sin necesitar CSV ni bibliotecas de
autoría, aunque sus pestañas requieren JavaScript. Para reconstruir faltan
fuentes, datos y configuración del entorno que deben conservarse aparte.

</details>

## D. Cambio de datos sin confundir entregas

1. Conserva la entrega original. En el CSV de práctica cambia 003/octubre a 3600.
2. Abre la entrega anterior y cambia de pestaña. Explica por qué no se actualiza.
3. Renderiza el documento explícito, verifica y crea otra carpeta de entrega.
4. Comprueba ambas entregas y registra cuál corresponde a cada fuente.
5. Como variante, restaura el CSV y sube 001/octubre a 1300 mientras bajas
   002/octubre a 1700. Predice qué vistas cambian y cuáles conservan sus cifras.

<details>
<summary>Solución razonada de D</summary>

El primer cambio produce 6000/6600 MXN, diferencia 600 y 10.00%. El HTML
anterior conserva 6000/6300 porque no vuelve a leer el CSV. En la variante
compensada, tarjetas y agregado vuelven a 6000/6300, diferencia 300 y 5.00%,
pero los pares 001/002 cambian. El detalle debe reflejarlo. No basta revisar
las tarjetas para afirmar que el archivo contiene los datos nuevos.

</details>

## Evidencia, pareja y reflexión individual

Una persona verifica datos; la otra revisa la interfaz y abre la copia de
entrega. Cambien papeles antes de D. Cada persona explica:

- ¿Qué interacción ocurre en el navegador y cuándo se ejecuta Python/R?
- ¿Qué conserva la carpeta de lectura y qué falta para reproducir?
- ¿Qué comprobación detectaría una tabla con saldos compensados?
- ¿Qué probaste en la copia final y qué no puedes certificar?

Conserva la nota, las fuentes y las entregas en tus carpetas personales, fuera
de Git. La nota identifica motor/versiones, comandos, datos, HTML revisado,
pruebas, resultados y límites. Un historial o un render exitoso no acredita
aprendizaje por sí solo.

## Criterio de salida y siguiente paso

Puedes cerrar la ampliación al conservar valores coherentes entre vistas,
explicar su funcionamiento y entregar una copia local revisada sin conexión.
No se exige desplegar ni construir una app. Registra evidencia en
[PROGRESS.md](../../../PROGRESS.md).

Continúa con la [lección 11.09 — Cierre del reporte reproducible](../../../curriculum/11_reporting_quarto/09_reproducible_report_closure/README.md).
