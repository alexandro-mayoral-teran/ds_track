# Lab 04.08 — Interacción con Altair

## Propósito, entradas y preparación

Este lab es **extensión opcional**. Lee la
[lección 04.08](../../../curriculum/04_visualization_python/08_altair_interaction/README.md)
y completa 04.07 con sus prerrequisitos. Explorarás figuras conservando una
explicación comprobable de sus estados y bases. Omitir este lab no bloquea
el cierre visual ni Python aplicado.

**Entradas:** interaction.py y las fuentes sintéticas de SQL 03.01.
**Resultado:** HTML/JSON de filtro, resaltado e intervalo, tablas, una variación
propia y evidencia de estados contrastados con datos. Mantén las fuentes,
scripts originales, SQLite y entregas anteriores intactos.

Tiempo orientativo: dos sesiones de 60–90 minutos para A–C y E. D profundiza
en intervalos y puede hacerse en otra sesión. Usa un solo gestor y el recorrido
completo de tu shell indicado en la lección. Desde la raíz, ejecuta interaction.py
con `--cut 2026-10-31` y una carpeta nueva
`curriculum/04_visualization_python/08_altair_interaction/output/lab_08`.
Abre los HTML en un navegador compatible con conexión. Si eliges `--bundle`,
usa el convertidor de 04.07 y otra carpeta; la prueba sin red es ampliación.
No necesitas instalar paquetes nuevos si el entorno de 04.07 ya es adecuado.

## A. Filtro y ficha sobre bases diferentes

Abre filtro.html, pares.csv y resumen_segmentos.csv.

1. Antes de tocar el menú, registra opción inicial, número de puntos,
   registros del corte, saldos conocidos y mediana global.
2. Elige consumo. Comprueba IDs y coordenadas de sus puntos con pares.csv.
   Cuenta también los registros y saldos de consumo en corte.csv.
3. Explica por qué la ficha informa diez registros aunque haya nueve puntos.
   Calcula la mediana sobre los diez saldos conocidos del segmento.
4. Elige educación. Escribe el mensaje y distingue registros, saldos y pares.
5. Vuelve a Todos. Comprueba que regresan los 19 puntos y la base global.
6. Revisa si los límites de los ejes cambiaron. ¿Qué confusión evitaron?

**Resultado:** ficha de tres estados y tablas conciliadas. **Comprobación:**
Todos = 24 registros, 21 saldos, 19 pares, mediana 2300; consumo = 10, 10,
9 y 1750; educación = 3, 0, 0 y mediana ausente.

<details>
<summary>Ver solución razonada de A</summary>

Todos incluye los segmentos completos. La mediana global 2300 se calcula
sobre 21 saldos originales, no sobre cuatro medianas de grupo. En consumo,
falta el atraso del crédito 006: su saldo participa en la mediana pero no
forma un punto. Por eso son diez saldos y nueve pares. El crédito 004 tiene
saldo cero válido y atraso 40: se conserva en (0, 40).

Educación tiene tres registros sin saldo, por lo que no tiene pares ni
mediana. La figura indica Sin pares conocidos y la ficha conserva 0/3.
Volver a Todos restablece la base sin reescribir archivos. Los dominios
se fijan desde el corte completo y permanecen iguales; una reducción de
escala no hace parecer mayor un saldo del segmento seleccionado.

</details>

## B. Condición y selección vacía

Abre resaltado.html. Identifica los cuatro cuadrados superiores.

1. Registra el estado inicial: puntos presentes, opacidad y ficha.
2. Haz clic en consumo. Cuenta puntos resaltados y atenuados.
3. Compara ese resultado con elegir consumo en filtro.html. ¿Cuáles
   permanecen en cada dispersión? ¿Qué vista sí se filtra en resaltado.html?
4. Haz clic en comercio y comprueba que reemplaza consumo.
5. Haz clic en educación. ¿Por qué el control puede seleccionarse aunque
   no haya pares de ese segmento? Revisa su ficha.
6. Haz doble clic sobre un cuadrado para limpiar. Explica empty=False
   y qué cambiaría si una selección vacía actuara como cumplimiento de todos.

**Resultado:** explicación de condición, filtro y limpieza. **Comprobación:**
consumo resalta nueve puntos y atenúa diez; la dispersión conserva 19.
Comercio resalta cinco y atenúa 14. Educación no resalta ninguno.

<details>
<summary>Ver solución razonada de B</summary>

Inicialmente no se elige segmento, todos los puntos están atenuados y
la ficha está vacía. La condición modifica opacidad/borde sin quitar filas.
El filtro de A deja solo nueve puntos de consumo; el resaltado de B conserva
19. En B se filtra la ficha para mostrar únicamente el segmento seleccionado.

toggle=False hace que el nuevo clic reemplace la selección anterior.
Los controles vienen del resumen completo, no de pares.csv, por lo que
educación puede elegirse y mostrar tres registros sin mediana. Elegirla
deja todos los puntos atenuados y no elimina los registros de la fuente.

empty=False establece que ninguna fila cumple una selección vacía. En la
condición todos pasan a la alternativa atenuada; en la ficha filtrada no
queda fila. Con empty=True, el predicado vacío cumpliría para todas las
filas: esa decisión exige explicar un estado inicial diferente.

</details>

## C. Construir una variación y explorar un corte vacío

Copia interaction.py como `interaction_lab.py` **en la misma carpeta** para
conservar la reutilización de 04.07. En la copia:

1. Cambia el valor inicial del menú de Todos a consumo. No cambies datos,
   opciones, reglas, ejes ni preparación de medianas.
2. Ejecuta con octubre en una carpeta nueva y comprueba el estado inicial.
3. Cambia a educación y a Todos. Verifica que la mediana no dependa del
   número de puntos visibles ni del orden en que usaste el menú.
4. Ejecuta otra entrega con `--cut 2026-11-30`. Prueba Todos y consumo.
5. Explica por qué Sin registros y cobertura no definida difieren de
   Sin pares conocidos y cobertura 0 % de educación en octubre.
6. Intenta repetir una carpeta de salida: el script debe rechazarla y
   conservar sus archivos.

**Resultado:** copia propia, dos entregas y registro de estados.

<details>
<summary>Ver solución razonada de C</summary>

Cambiar value a consumo en el parámetro segmento_elegido modifica solo
el estado inicial de filtro.html. Octubre comienza con nueve puntos, mediana
1750, diez saldos y diez registros. Todos muestra otra vez 19 pares y mediana
global 2300. Los CSV siguen conteniendo la base preparada completa.

Noviembre no existe en la muestra. Las fichas muestran Sin registros;
no hay mediana ni cobertura definida, porque el denominador es cero.
Educación en octubre sí tiene registros y su cobertura es 0/3 = 0 %,
aunque no tenga saldo conocido. Ambos gráficos pueden carecer de puntos,
pero significan cosas distintas.

La carpeta existente se rechaza por exist_ok=False. No se borra para
volver a ejecutar: usa otra carpeta. Comprueba archivos y fuentes después
de cualquier error; una salida parcial no equivale a una entrega completa.

</details>

## D. Intervalo vinculado — profundización opcional

Abre intervalo.html y conserva pares.csv como referencia.

1. Antes de arrastrar, cuenta A y B; explica el contador cero y su base.
2. Dibuja un rectángulo pequeño alrededor de (1300 MXN, 10 días), crédito
   001. Comprueba que no incluye otros puntos y compara A con B.
3. Amplía o mueve el rectángulo y registra IDs/coordenadas de los pares
   que entran. Concilia el conteo con la tabla usando los mismos límites.
4. Dibuja en una zona sin puntos. Limpia con doble clic en A.
5. Explica por qué 1/19 y 1/24 describen bases distintas y por qué el
   rectángulo no produce una tasa de atraso de cartera.
6. Describe qué sucede con créditos cuyo saldo o atraso es ausente.

**Resultado:** captura de un intervalo, IDs y conteo conciliado.
**Comprobación:** el rectángulo de un par deja 19 puntos en A, uno en B
y contador 1/19; al limpiar, B y el contador vuelven a cero.

<details>
<summary>Ver solución razonada de D</summary>

A conserva la población de 19 pares conocidos. B contiene el subconjunto
del rectángulo. El crédito 001 aporta (1300, 10) de una sola fila; si el
rectángulo es pequeño y no toca otro punto, B tiene uno. Un intervalo sin
puntos también tiene conteo cero; esto difiere de no haber registros fuente.

1/19 se refiere a pares conocidos seleccionados; 1/24 usa la base original
de registros. El contador explicita ambas bases, pero no convierte la
selección visual en una medida crediticia. Las cinco exclusiones carecen
de al menos una coordenada y no pueden recuperarse mediante arrastre.
Sus motivos siguen en excluidos_pares.csv. El rectángulo es una elección
visual, no una muestra aleatoria ni evidencia causal.

</details>

## E. Compartir y explicar un estado

1. Elige consumo en el menú y guarda una captura con su ficha visible.
   Conserva corte, opción, conteos, mediana, fuente y limitaciones en texto.
2. Recarga filtro.html. ¿Conserva el estado anterior o el valor inicial
   de su especificación? Distingue la entrega original de tu copia de C.
3. Comprueba que pares.csv no cambió con tus clics. ¿Qué recibiría alguien
   que interpreta ese CSV como descarga del segmento seleccionado?
4. Si eliges --bundle, abre los tres HTML sin red y prueba menú, clic y
   arrastre. Compara una captura del estado elegido con _inicial.png/svg.
5. Explica qué puede comprobar alguien que recibe la captura, el JSON,
   el HTML o las tablas. Adjunta texto y tablas para lectura sin cursor.

<details>
<summary>Ver solución razonada de E</summary>

La captura guarda la apariencia de consumo en ese momento. La evidencia
debe indicar nueve pares entre diez registros, diez saldos conocidos y
mediana 1750, además de fecha y fuente sintética. El HTML original vuelve
a Todos al recargar; tu copia de C vuelve a consumo por su value inicial.

Los CSV son tablas preparadas, no descargas del estado de la interfaz.
El HTML incorporado conserva interacción sin red con estos datos; el básico
necesita bibliotecas de CDN. PNG/SVG se exportan desde la especificación
inicial y no cambian al usar el HTML. Una captura prueba un aspecto del
estado; tabla y código permiten comprobar sus valores y reconstrucción.

</details>

## Evidencia, reflexión y siguiente paso

Conserva código propio, HTML/JSON, tablas, captura y comentario de al menos
un filtro y un resaltado. Si realizas D, añade intervalo e IDs; si eliges
exportación incorporada, registra la prueba sin conexión. Anota versiones,
visor, estado inicial y forma de restablecer. Registra evidencias y dudas
en tu bitácora personal junto a la práctica sin atribuir aprendizaje por la disponibilidad del material.

Reflexiona: ¿cuándo conviene conservar puntos atenuados? ¿Qué significa
una selección vacía? ¿Por qué contar solo puntos no describe todos los
registros? ¿Qué necesitas guardar para que otra persona interprete tu captura?

No hay checkpoint de proyecto implementado. Continúa con el
[04.09 — Cierre visual del análisis](../../../curriculum/04_visualization_python/09_visual_closure/README.md),
disponible. Las referencias primarias están en la lección.
