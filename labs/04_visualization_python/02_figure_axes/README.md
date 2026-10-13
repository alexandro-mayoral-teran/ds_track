# Lab 04.02 — Matplotlib: Figure y Axes

## Entrada, actividad y resultado

Lee la [lección 04.02](../../../curriculum/04_visualization_python/02_figure_axes/README.md)
y completa 04.01 con sus prerrequisitos. Recibes resumen_octubre.csv y
[figure_axes.py](../../../curriculum/04_visualization_python/02_figure_axes/figure_axes.py).
Produce una figura PNG, tu script y una nota que identifique objetos, valores,
ausencias y cómo guardaste/cerraste. Mantén entradas y ejemplos originales.
Una sesión puede cubrir A–B; C–D completan el criterio esencial. E es extensión.

Puedes guardar mi_figura.py en la carpeta de la lección para importar helpers
desde figure_axes; el archivo original se conserva. Ejecuta con tu entorno
elegido y sigue los recorridos de la lección. Cada entrega usa carpeta nueva
en output; no sobrescribas revisiones anteriores.

## A — Leer y ubicar responsabilidades

1. Ejecuta figure_axes.py sin --output y verifica las cantidades del resumen.
2. Explica Figure, Axes y Axis con palabras propias.
3. Ubica qué objeto dibuja barras, cuál pone etiquetas y cuál guarda el archivo.
4. Explica por qué educacion debe permanecer aunque no tenga barra numérica.

<details>
<summary>Ver solución razonada de A</summary>

El resumen tiene cuatro segmentos, 24 registros y 21 saldos conocidos;
la suma conocida es 46 700 MXN. Figure reúne el contenido y guarda mediante
fig.savefig; Axes dibuja con ax.barh y configura sus etiquetas; Axis gestiona
un eje y sus marcas. Un Axes normalmente tiene eje x e y.

educacion tiene tres registros y cero saldos conocidos; su suma es ausente,
no cero. La categoría y el mensaje evitan presentar una población incompleta
como si todos sus saldos estuvieran observados.

</details>

## B — Crear, configurar y guardar una figura explícita

1. Lee read_summary y crea la figura con create_single.
2. Cambia el título del Axes conservando pregunta, fecha y unidades.
3. Guarda el PNG en una carpeta nueva y cierra en finally.
4. Abre el archivo; comprueba barras, etiquetas, fuente y ausencia.

<details>
<summary>Ver solución razonada de B</summary>

Un mi_figura.py completo en la misma carpeta:

```python
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_axes import read_summary, create_single

carpeta = Path(__file__).resolve().parent
resumen = read_summary(carpeta / "resumen_octubre.csv")
salida = carpeta / "output" / "mi_revision"
salida.mkdir(parents=True, exist_ok=False)
fig, ax = create_single(resumen)
try:
    ax.set_title("Saldo conocido por segmento · revisión de octubre", loc="left")
    fig.savefig(salida / "figura.png", dpi=150)
finally:
    plt.close(fig)
```

La figura se guarda mediante la referencia fig, no con el estado actual de
pyplot. Esperas barras 15 500, 15 900 y 15 300; educacion recibe un mensaje
sin saldo conocido. La fecha general permanece en el título de Figure.
Si la carpeta existe, el programa se detiene para conservar tu revisión.

Si llevas el script a otra ubicación, adapta importaciones y rutas. La prueba
no consiste solo en que exista un archivo: revisa que la imagen muestre los
datos, unidades y cobertura correctos y que el texto no quede cortado.

</details>

## C — Estado y cierre de figuras

1. Crea dos figuras distintas con create_single y cambia sus títulos por separado.
2. Guarda cada una usando su propia variable fig_a o fig_b.
3. Cierra solo fig_a y explica qué ocurre con fig_b.
4. Cierra fig_b al terminar. Explica por qué no usamos close('all') dentro de un helper.

<details>
<summary>Ver solución razonada de C</summary>

Cada llamada crea una Figure diferente con su propio Axes. ax_a.set_title
cambia solo el primer panel, aunque fig_b se haya creado después. Cada
fig.savefig guarda su contenido. plt.close(fig_a) no cierra fig_b ni elimina
los archivos guardados; la segunda sigue disponible para configurar y guardar.

close('all') podría cerrar otras figuras del notebook o de una sesión compartida.
El helper de dibujo recibe un Axes y no administra recursos ajenos. Quien crea
la Figure controla su guardado y cierre. Usa try/finally para no dejar figuras
abiertas si una ruta o escritura falla.

</details>

## D — Vacío, desconocido y cero

1. Crea una tabla vacía con las mismas columnas y tipos usando resumen.iloc[0:0].copy().
2. Genera una figura y comprueba el mensaje de entrada vacía, sin barras inventadas.
3. En otra copia conserva solo educacion; distingue grupo presente de tabla vacía.
4. En un ejemplo propio en memoria declara un registro, un conocido y suma cero;
   explica qué etiqueta corresponde. No modifiques el CSV original.

<details>
<summary>Ver solución razonada de D</summary>

La tabla sin filas muestra «Sin observaciones en la tabla de entrada». No hay
fecha observable para asignar; el título general indica sin registros.
educacion sí es una fila de grupo: tres registros, cero conocidos y suma NA;
se conserva con su mensaje, no como tabla vacía.

Una fila con registros = 1, conocidos = 1 y suma = 0 es un cero conocido:
la barra tiene longitud cero, pero la etiqueta indica 0 MXN y 1/1 conocidos.
Una fila con conocidos = 0 y suma = 0 viola el contrato; read_summary la rechaza.
Igualmente rechaza conocidos mayores que registros, categorías duplicadas
o fechas mezcladas. Esos casos se estudian en memoria o archivos nuevos.

</details>

## E — Extensión: dos Axes en la misma Figure

1. Ejecuta --two-panels en una carpeta nueva y revisa los dos PNG.
2. Usa create_pair y cambia únicamente el título de axes[1].
3. Explica qué operaciones corresponden a Figure y cuáles a cada Axes.
4. Comprueba las categorías alineadas y por qué no comparten el eje horizontal.

<details>
<summary>Ver solución razonada de la extensión</summary>

create_pair devuelve una Figure y una colección de dos Axes. axes[0] dibuja
saldo y axes[1] cobertura; fig.suptitle afecta el título general y fig.savefig
guarda ambos paneles. axes[1].set_title cambia solo la segunda vista.

La cobertura es 100 % para comercio, consumo y servicios, y 0 % para educacion,
porque hay cero conocidos entre tres observaciones. El primer panel mide MXN;
el segundo porcentaje. No compartiríamos límites horizontales de esas medidas.
El mensaje de ausencia de saldo y el punto de cobertura cero son compatibles.

</details>

## Evidencia, reflexión y siguiente paso

Conserva script, PNG, resumen usado y una nota sobre Figure/Axes/Axis, valores,
ausencias y cierre. Registra evidencia y dudas en PROGRESS.md. Explica:
¿qué cambia guardar frente a mostrar? ¿Por qué un layout automático necesita
revisión visual? ¿Cómo puedes dibujar sin depender del panel actual?
¿Qué representa la barra de longitud cero frente a una suma ausente?

No hay checkpoint de proyecto implementado. Continúa con el
[plan de 04.03 — Comparaciones y evolución](../../../curriculum/04_visualization_python/README.md#03-comparaciones-y-evolucion),
pendiente de desarrollo; todavía no hay siguiente lab disponible.
