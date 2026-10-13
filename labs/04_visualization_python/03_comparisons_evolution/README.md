# Lab 04.03 — Comparaciones y evolución

## Propósito, entradas y preparación

Lee la [lección 04.03](../../../curriculum/04_visualization_python/03_comparisons_evolution/README.md)
y completa 04.02 con sus prerrequisitos. Recibes los CSV sintéticos de créditos
y cortes, comparisons.py y una serie mensual didáctica independiente. No edites
las fuentes ni la base SQLite. Puedes dividir este lab en varias sesiones.

Tiempo orientativo: dos sesiones de 60–90 minutos para A–D; E puede realizarse
en otra sesión. Ajusta el ritmo y conserva las dudas para la revisión acompañada.

La meta es justificar una comparación por categorías y otra temporal con sus
unidades, denominadores y ausencias. Las actividades A–D son esenciales; E es
una ampliación que no bloquea avanzar.

## A. Decidir qué se compara

Antes de ejecutar, redacta dos preguntas: una sobre segmentos en octubre y otra
sobre cambio entre cortes. Para cada una escribe unidad de registro, medida,
base, unidad del eje, regla para ausencias y representación elegida.

Calcula a mano la suma y el promedio conocido de consumo y comercio en octubre.
Después calcula sus tasas de atraso ≥ 30 días. ¿Se conserva el orden entre
segmentos cuando cambia la medida? ¿Qué información falta para decir «mayor riesgo»?

**Comprobación:** explica por qué los diez saldos de consumo no implican diez
atrasos conocidos y por qué educacion puede tener una tasa conocida sin saldo
conocido. Conserva las fracciones, además de porcentajes redondeados.

<details>
<summary>Ver solución razonada de A</summary>

Consumo suma 15 900 MXN y promedia 1 590 MXN entre diez saldos; comercio suma
15 500 y promedia 3 100 entre cinco. Cambia el orden porque la suma incluye
tamaño del grupo. Las tasas son 4/9 ≈ 44,44 % y 2/5 = 40 %. Consumo tiene un
atraso ausente aunque sus saldos están completos. Educacion tiene 0/3 saldos
conocidos y 2/3 atrasos conocidos: las coberturas corresponden a variables
distintas. Su tasa 1/2 describe dos casos evaluables; no permite inferir una
probabilidad para toda una población ni explicar causas.

</details>

## B. Reconstruir y auditar barras agrupadas

Ejecuta el script siguiendo el recorrido completo de tu shell en la lección,
con carpeta nueva `output/lab_b`. Abre comparaciones.csv y segmentos.png.

1. Comprueba ocho filas: cuatro segmentos en dos fechas, sin claves repetidas.
2. Localiza las dos barras de consumo. Comprueba 12 100 y 15 900 MXN y sus
   coberturas 8/10 y 10/10. Describe por qué no bastan para medir el cambio
   de saldo de los mismos créditos conocidos.
3. Localiza las dos ausencias de educacion: saldo en octubre y tasa en septiembre.
4. En una copia del script dentro de la misma carpeta, cambia `GROUPS` para
   ordenar consumo, comercio, servicios, educacion. Ejecuta en `output/lab_b_orden`.
   Conserva la versión original. El orden nuevo debe aplicarse a ambos cortes
   y paneles sin alterar valores ni asociar etiquetas a otro segmento.

**Resultado:** dos PNG con orden distinto y la misma información, más una nota
que justifique uno de los órdenes. Revisa leyenda, tramas, cero del eje y unidades.
Si cambias el script de carpeta, su ruta relativa a las fuentes cambia; esta
actividad mantiene la copia junto al original.

<details>
<summary>Ver solución razonada de B</summary>

GROUPS controla las posiciones pedidas por reindex, y los ticks usan ese mismo
orden. Cambiar solo los ticks reasignaría nombres sin mover datos y sería
incorrecto. Las fuentes no cambian, tampoco las fracciones ni longitudes.
La suma de consumo aumenta 3 800 MXN, pero pasan de ocho a diez saldos conocidos.
No podemos atribuir todo ese aumento al cambio de importes de un conjunto fijo.
Las ausencias se identifican con texto, no con barras de longitud cero.

</details>

## C. Comprobar bases temporales

Abre pares.csv y totales.csv. Cuenta los 19 créditos que tienen saldo conocido
en ambos cortes. Comprueba sumas por columna. Contrasta con las sumas de todos
los saldos conocidos de cada fecha.

Escribe dos interpretaciones de bases.png: una por panel. Incluye fechas,
importe inicial/final, cambio y población considerada. Corrige esta frase:
«La cartera cayó 500 MXN y por tanto los créditos redujeron sus saldos».
Explica también por qué dos puntos no demuestran una tendencia sostenida.

**Comprobación:** identifica los cinco créditos excluidos de los pares y explica
por qué «21 conocidos en ambos cortes» no significa «los mismos 21».

<details>
<summary>Ver solución razonada de C</summary>

Se excluyen 005, 009, 022, 023 y 024. Los primeros dos tienen saldo ausente en
septiembre; 022 y 023 en octubre; 024 en ambos. La suma disponible pasa de
47 200 a 46 700 MXN, −500 MXN, con conjuntos diferentes de 21 saldos.
Los mismos 19 pares pasan de 40 700 a 42 900, +2 200 MXN. Corregiríamos:
«La suma de saldos conocidos disminuyó 500 MXN entre los cortes; entre los
19 créditos conocidos en ambos aumentó 2 200 MXN. Falta información para
afirmar el cambio del saldo real total». Los dos puntos describen un intervalo;
no permiten reconocer persistencia, ciclos ni causas.

</details>

## D. Representar un hueco sin inventar un saldo

Revisa serie_mensual.csv, calendario.csv y huecos.png. Identifica octubre,
noviembre y diciembre con una frase por mes: presencia de fila, conocimiento
del importe y marca dibujada.

En un archivo nuevo junto a comparisons.py, ejecuta este ejemplo de contraste
desde esa carpeta con el entorno elegido:

```python
import matplotlib.pyplot as plt
from comparisons import calendar, HERE

serie = calendar(HERE / "serie_mensual.csv")
fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained", sharey=True)
axes[0].plot(serie.index, serie["saldo_mxn"].to_numpy(dtype=float, na_value=float("nan")), marker="o")
solo_conocidos = serie.dropna(subset=["saldo_mxn"])
axes[1].plot(solo_conocidos.index, solo_conocidos["saldo_mxn"].astype(float), marker="o")
axes[0].set_title("Calendario con ausencias")
axes[1].set_title("Contraste: eliminar ausencias conecta puntos")
for ax in axes:
    ax.set_xticks(serie.index, serie.index.strftime("%Y-%m"))
    ax.set_ylabel("Saldo (MXN)")
fig.savefig("contraste_huecos.png", dpi=160)  # Usa un nombre nuevo.
plt.close(fig)
```

Este contraste intencional permite ver el efecto de quitar filas. No uses el
segundo panel como evidencia de un saldo observado en octubre o noviembre.
Conserva una nota que explique la diferencia. No completar la serie con cero.

**Comprobación:** calendario tiene cinco filas, cuatro presentes, tres importes
conocidos; su único cero está en diciembre. El CSV fuente sigue con cuatro filas.

<details>
<summary>Ver solución razonada de D</summary>

Octubre tiene fila pero no importe; noviembre carece de fila; ambos interrumpen
la línea. Diciembre tiene un saldo observado de cero. El panel filtrado une
septiembre y diciembre y oculta los huecos. Una conexión guía la lectura entre
observaciones; no prueba valores intermedios. La reindexación conserva el
importe desconocido y marca por separado si existía una fila.

</details>

## E. Ampliación: cambios relativos

Calcula el cambio relativo de los pares y el índice de octubre con septiembre
como base 100. Calcula la diferencia de tasas de consumo en puntos porcentuales
y como porcentaje relativo. Escribe unidades correctas y límites de comparación.
¿Qué harías si el valor inicial fuera cero o estuviera ausente?

<details>
<summary>Ver solución razonada de E</summary>

2 200 / 40 700 × 100 ≈ 5,41 %; índice 105,41. La tasa pasa de 25 % a 44,44 %:
+19,44 puntos porcentuales o +77,78 % relativo. Su denominador cambia de ocho
a nueve atrasos conocidos; no es una comparación de todos los mismos casos.
Con una base cero o ausente, el cambio relativo y el índice no se calculan;
la diferencia absoluta aún puede calcularse si ambos importes son conocidos.

</details>

## Evidencia, reflexión y siguiente paso

Conserva código, tablas exportadas, figuras y una interpretación por pregunta.
Debes poder explicar orden, unidad, cobertura, base temporal y huecos sin leer
la solución. Reflexiona: ¿qué afirmación dejó de ser válida al cambiar la base?
¿Qué información pedirías antes de interpretar un cambio como tendencia?
Registra evidencia y dudas en PROGRESS.md; producir contenido no acredita aprendizaje.

No hay checkpoint de proyecto implementado. Continúa con el
[04.04 — Distribuciones y relaciones](../../../curriculum/04_visualization_python/04_distributions_relationships/README.md).
