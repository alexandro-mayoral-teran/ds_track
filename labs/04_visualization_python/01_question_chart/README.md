# Lab 04.01 — Pregunta y elección de gráfico

## Entrada, actividad y resultado

Lee la [lección 04.01](../../../curriculum/04_visualization_python/01_question_chart/README.md)
y completa sus prerrequisitos. Recibes las cuatro vistas de esa lección y los
resultados comprobados del cierre SQL. Produce una ficha de elección, un boceto
y una nota de interpretación. Puedes resolver este lab con Markdown y papel:
regenerar el ejemplo en Python es opcional y no bloquea avanzar.

Conserva datos y ejemplos originales. No necesitas volver a limpiar la cartera
ni escribir funciones de una biblioteca que se enseñará después. Una sesión
puede cubrir A–B; C–E completan el criterio esencial.

## A — Convertir una idea en una pregunta

1. Reescribe «quiero ver cómo va la cartera» como una pregunta comprobable.
2. Completa público, fecha, población, unidad del detalle, unidad de figura,
   medida y cobertura usando el ejemplo de octubre.
3. Indica qué registro representa una marca y qué dato no puedes recuperar.

<details>
<summary>Ver una solución razonada de A</summary>

Pregunta posible: ¿qué suma de saldo conocido tiene cada segmento en octubre?
Público: quien revisa el corte sin conocer el código. Población: 24 observaciones
crédito/fecha de octubre; detalle: una observación; figura: un segmento por barra.
Medida: SUM de saldo conocido en MXN. Base: 21 saldos conocidos de 24;
educacion tiene cero saldos conocidos de tres observaciones.

La barra resume varias filas, no un cliente. No sabemos el importe de los tres
saldos ausentes; no los representamos como cero. Otra pregunta puede ser válida
si declara de forma coherente su medida, unidad y cobertura.

</details>

## B — Misma fuente, cuatro preguntas

1. Relaciona cada panel de la figura con comparación, tiempo, distribución o relación.
2. Declara la base de cada vista y explica por qué no sirve el mismo resumen para todas.
3. Identifica un gráfico alternativo justificable y qué lectura facilitaría.

<details>
<summary>Ver solución razonada de B</summary>

| Vista | Pregunta | Base |
| --- | --- | --- |
| A | Suma conocida por segmento | 24 observaciones, 21 saldos conocidos; cuatro grupos |
| B | Cambio en los mismos pares temporales | 19 créditos conocidos en septiembre y octubre |
| C | Distribución del saldo individual | 21 saldos conocidos de octubre |
| D | Asociación saldo/atraso por observación | 19 pares con ambas medidas conocidas en octubre |

El resumen por segmento sirve para A, pero pierde valores individuales que
requieren C y D. B necesita IDs y dos fechas para comprobar una base común.
Una tabla pequeña puede facilitar valores exactos y cobertura; puntos por
segmento también podrían comparar magnitudes conocidas. No hay una única
respuesta válida si la alternativa conserva el contrato y se entiende su lectura.

</details>

## C — Cambiar la medida cambia la respuesta

1. Compara consumo y comercio por suma conocida y por promedio conocido.
2. Explica cuál responde a «mayor volumen conocido» y cuál a «saldo promedio».
3. Compara los dos cortes con totales conocidos y con pares comparables.
4. Explica por qué las dos bases de 19 de los paneles B y D no son iguales.

<details>
<summary>Ver solución razonada de C</summary>

Consumo suma 15 900 con diez conocidos, promedio 1 590; comercio suma 15 500
con cinco, promedio 3 100 MXN. Mayor suma conocida es consumo; mayor promedio
conocido es comercio. Ninguna afirmación se transfiere automáticamente a educacion.

Totales conocidos por corte: 47 200 y 46 700, diferencia −500. Los mismos 19
pares temporales: 40 700 y 42 900, diferencia +2 200. Cambian los IDs conocidos
al usar totales independientes; decide qué pregunta quieres responder antes
de conectar puntos y titular la figura.

B excluye 005/009/022/023/024; D excluye 006/012/022/023/024. La cantidad 19
coincide, pero la población no. En D se requieren dos medidas del mismo corte;
en B se requiere el mismo saldo en dos cortes del mismo crédito.

</details>

## D — Corregir propuestas ambiguas

Para cada propuesta explica el problema y ofrece una formulación comprobable:

1. Una línea conecta consumo, comercio y servicios para mostrar «evolución».
2. Una barra cero representa educacion porque su SUM está ausente.
3. La dispersión se titula «el saldo alto causa atraso».
4. Un círculo del 100 % presenta las tasas de atraso por segmento como composición.
5. Se eliminan los extremos del histograma solo para que se vea equilibrado.

<details>
<summary>Ver solución razonada de D</summary>

1. Segmentos sin orden temporal no constituyen evolución; usa categorías para
   comparar una medida o fechas para comparar en el tiempo.
2. Ausencia de importes no es cero; conserva la categoría con cobertura 0/3 y
   un mensaje, como en A.
3. Dos medidas observadas permiten explorar asociación, no atribuir una causa;
   titula por variables y base, y plantea qué evidencia adicional haría falta.
4. Tasas con denominadores diferentes no son partes de un mismo todo. Una tabla
   o puntos por segmento pueden mostrar tasas con sus numeradores y bases.
5. Un extremo conocido pertenece a la muestra salvo una regla de validación
   documentada. Inspecciónalo y explica su efecto; no lo borres por estética.

</details>

## E — Proponer una vista y explicar sus límites

1. Elige una pregunta diferente o una alternativa a A; completa la ficha.
2. Dibuja un boceto con título, ejes/unidades, categorías o fechas y nota de cobertura.
3. Escribe observación, alcance y pregunta pendiente en tres frases.
4. Revisa con quien te acompaña si la conclusión está respaldada por esa base.

<details>
<summary>Ver una propuesta razonada de E</summary>

Pregunta: ¿qué tasa de atraso confirmado entre conocidos tiene cada segmento
en octubre? Vista: puntos por segmento y tabla de numerador/denominador/cobertura.
Medida: ≥30 días / atrasos conocidos, en %. Tabla: comercio 2/5, consumo 4/9,
educacion 1/2 y servicios 2/5, con observaciones 5/10/3/6 respectivamente.

Observación: educacion tiene 50 % entre los dos atrasos conocidos. Alcance:
es una muestra ficticia de tres observaciones y una tiene atraso desconocido;
no es la tasa sobre tres clasificaciones completas. Pregunta pendiente:
¿qué información falta para clasificar esa observación y evaluar otros cortes?

Otra propuesta puede ser válida. El criterio no es copiar este gráfico, sino
justificar población, unidad, medida, base y límites sin inventar información.

</details>

## Extensión — Regenerar y comprobar

Ejecuta choice_examples.py según la lección con una carpeta nueva. Compara las
tablas exportadas con las bases de B. Prueba septiembre y una fecha inexistente:
no se inventa una fecha previa ni se rellenan vistas con cero. Explica qué
mensajes usarías para alguien que solo ve la figura, sin el script.
Esta extensión no requiere entender toda la sintaxis gráfica para avanzar.

## Evidencia, reflexión y siguiente paso

Conserva ficha, boceto y tres frases de interpretación, junto con una alternativa
y su justificación. Registra evidencia y dudas en PROGRESS.md; una imagen
atractiva no demuestra por sí sola que la elección responde la pregunta.

Explica: ¿qué dato perdiste al agrupar? ¿Por qué igualar conteos no garantiza
igualar bases? ¿Cuándo elegirías una tabla? ¿Qué afirmación causal no puedes
defender con estas variables? No hay checkpoint de proyecto implementado.

Continúa con el [plan de 04.02 — Matplotlib: Figure y Axes](../../../curriculum/04_visualization_python/README.md#02-matplotlib-figure-y-axes),
pendiente de desarrollo; todavía no hay siguiente lab disponible.
