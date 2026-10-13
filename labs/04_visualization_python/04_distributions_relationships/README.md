# Lab 04.04 — Distribuciones y relaciones

## Propósito, entradas y preparación

Lee la [lección 04.04](../../../curriculum/04_visualization_python/04_distributions_relationships/README.md)
y completa 04.03 con sus prerrequisitos. Recibes los CSV originales de SQL,
distributions.py y cuatro figuras reconstruibles. Conserva las fuentes y la
base SQLite; no elimines registros por su apariencia.

Tiempo orientativo: dos sesiones de 60–90 minutos para A–D, con revisión
acompañada; E es una ampliación. Puedes detenerte entre actividades y conservar
tus dudas. La meta es explicar variabilidad y una relación usando tablas y
figuras, con bases y unidades explícitas.

## A. Formular preguntas y distinguir centro de variabilidad

Escribe una pregunta para cada vista: histograma, caja por segmento y dispersión.
Para cada una declara registro, variable(s), unidad de ejes y base conocida.

Calcula media, mediana y rango de A = [1900, 2000, 2100] y B = [0, 2000, 4000].
Redacta una frase que sería incompleta si solo comunicaras el promedio.
Después explica qué cambiaría si uno de los valores de B estuviera ausente:
¿podrías seguir afirmando su media original? ¿Lo reemplazarías por cero?

**Resultado:** ficha de preguntas y cálculos, sin atribuir significado real
a esta muestra independiente de seis valores.

<details>
<summary>Ver solución razonada de A</summary>

Ambas medias y medianas son 2000 MXN, pero A tiene rango 200 y B, 4000 MXN.
«Ambos promedian 2000» no comunica su distinta separación. Un valor ausente
cambia la base conocida: no podemos conservar el promedio de tres valores
como si lo hubiéramos observado. Reemplazarlo por cero inventaría un importe.
El histograma estudia saldo de cada crédito en octubre; las cajas comparan
esa distribución por segmento; la dispersión estudia saldo y atraso conocidos
del mismo crédito y fecha. Sus bases son 21, 5/10/0/6 por segmento y 19 pares.

</details>

## B. Reconstruir y conciliar histogramas

Ejecuta el recorrido de tu shell indicado en la lección. Usa una carpeta nueva
`output/lab_b` y corte 2026-10-31. Abre saldos.csv, intervalos_500.csv,
intervalos_1000.csv y histogramas.png.

1. Comprueba 24 filas en corte.csv y 21 en saldos.csv. Localiza el saldo cero.
2. Suma las frecuencias de ambas tablas de intervalos. Deben conciliar con
   los saldos conocidos, aunque el número de barras difiera.
3. Ubica manualmente 0, 1500, 2000 y 3300 en intervalos de 500 MXN.
4. Explica qué cambia al usar 1000 MXN y qué permanece intacto.
5. Describe una concentración, un hueco y una limitación sin afirmar una
   forma poblacional ni inventar ubicación para los ausentes.

**Comprobación:** cuenta filas, además de mirar alturas. ¿Por qué no deben sumar
24? ¿Qué pasaría si usaras bordes solo hasta 3000? El script rechaza esa
exclusión; un histograma sin comprobación podría ocultar los valores mayores.

<details>
<summary>Ver solución razonada de B</summary>

Los conteos de 500 son [1, 0, 2, 4, 5, 5, 4] y los de 1000, [1, 6, 10, 4].
Ambos suman 21. El crédito 004 tiene saldo cero. 1500 pertenece a [1500, 2000)
y 2000 a [2000, 2500); 3300 a [3000, 3500]. Tres saldos ausentes no se
ubican en intervalos. Bordes hasta 3000 incluirían el valor 3000 en el último
intervalo, pero dejarían fuera 3100, 3200 y 3300. El aspecto cambia al
agrupar más valores, no la muestra. No hay conocidos entre 500 y 1000;
veinte se ubican entre 1300 y 3300. Desconocemos la posición de los tres ausentes.

</details>

## C. Leer una caja y revisar un valor exterior

Abre cajas.png y resumen_cajas.csv. En consumo ordena los diez saldos conocidos
y calcula mediana, Q1, Q3, IQR y límites de referencia usando interpolación
lineal, como se explicó en la lección. Identifica los bigotes observados.

Localiza el crédito fuera de los bigotes y coteja su saldo y atraso en corte.csv.
Escribe qué se puede afirmar y qué evidencia pedirías para decidir si es un
error. No borres la fila. Explica por qué educacion no tiene caja.

Contrasta mediana e IQR de comercio y servicios. ¿Una mediana mayor implica
también mayor variabilidad? ¿La longitud de la caja indica tamaño del grupo?

**Resultado:** figura anotada en una nota de lectura, cálculos y protocolo
de revisión del valor exterior. No necesitas editar la imagen.

<details>
<summary>Ver solución razonada de C</summary>

Consumo: Q1 1425, mediana 1750, Q3 1975, IQR 550 MXN. Límites 600 y 2800;
bigotes en 1300 y 2200. El saldo cero del crédito 004 queda fuera. Su atraso
conocido es 40 días; la combinación merece consultar definiciones y registros
de origen, pero la figura no prueba un error ni explica el evento.
Educacion tiene tres observaciones y ningún saldo conocido: no inventar
mediana cero. Comercio tiene mediana 3100 e IQR 200; servicios 2550 e IQR 250.
Un centro más alto no implica mayor separación. La longitud muestra IQR,
no cantidad; las bases son cinco y seis conocidos respectivamente.

</details>

## D. Comprobar pares e interpretar dispersión

Abre pares.csv, excluidos.csv y dispersion.png. Comprueba:

- Pares y excluidos tienen claves sin repetición, no se solapan y reúnen
  los 24 créditos del corte.
- Cada par tiene ambas variables conocidas; un excluido tiene al menos una
  ausente. Localiza los cinco créditos y sus motivos.
- El punto del crédito 004 está en (0 MXN, 40 días). Localiza otro de comercio
  y coteja las coordenadas con su fila, sin confundir ejes.

Explica por qué la siguiente idea dañaría el emparejamiento:
«Elimino ausencias de saldo y atraso por separado, ordeno ambas listas y las
dibujo juntas». Aunque las listas tengan igual longitud, no garantiza que
los valores correspondan al mismo crédito.

Redacta tres frases: patrón observado, base/ausencias y límite de interpretación.
Corrige «El gráfico demuestra que saldos mayores causan más atraso».
Describe qué ocurriría si dos créditos compartieran las mismas coordenadas.

**Comprobación:** los 19 pares aquí no son necesariamente los mismos 19 pares
temporales de 04.03. Escribe las dos reglas de selección y un crédito que
demuestre la diferencia.

<details>
<summary>Ver solución razonada de D</summary>

Los excluidos son 006 y 012 por atraso ausente, 022 y 023 por saldo ausente,
y 024 por ambos. 19 + 5 = 24; tres saldos y tres atrasos ausentes no son
seis créditos distintos. El crédito 017 de comercio está en (2900, 20).
Los pares de esta vista exigen saldo y atraso en octubre; los de 04.03 exigen
saldo en septiembre y octubre. 006 entra en los pares temporales pero no aquí;
005 tiene ambas variables en octubre y sí entra aquí, pero no en los pares
temporales por saldo ausente en septiembre.

Podemos decir que los atrasos observados forman bandas y que saldos próximos
presentan atrasos diferentes. La vista incluye 19 de 24 créditos; la selección
y el origen sintético limitan su alcance. La nube no demuestra causalidad.
Ordenar columnas independientemente emparejaría personas o créditos distintos.
Dos puntos coincidentes podrían verse como uno; la tabla y los conteos
declarados conservan la cantidad real, aunque haya transparencia.

</details>

## E. Ampliación: proporciones y otro corte

Calcula la frecuencia relativa del intervalo [2000, 2500) de octubre y su
altura si fuera densidad con anchura 500 MXN. Explica unidad y área.

Ejecuta otra vez con `--cut 2026-09-30` y una carpeta nueva `output/lab_e_sep`.
Compara saldos conocidos, intervalos y cajas usando los mismos bordes y medidas.
En septiembre educacion tiene dos saldos conocidos; comenta qué se puede
describir con tan pocos casos. No interpretes diferencias de distribución
como cambios de los mismos créditos sin comprobar una base comparable.

<details>
<summary>Ver solución razonada de E</summary>

La proporción es 5/21 ≈ 23,81 %. La densidad es 5/(21 × 500) ≈ 0,000476
por MXN; su área es 5/21. No es un porcentaje de saldo total ni un valor
para cada crédito. Septiembre también tiene 21 saldos conocidos, con conteos
de 500 [0, 0, 4, 3, 5, 5, 4]. Educacion tiene 3200 y 3300 MXN: mediana 3250
e IQR 50 con interpolación lineal, una descripción de dos casos, con uno
ausente. En octubre carece de saldos conocidos. Igual cantidad global conocida
no garantiza el mismo conjunto de créditos; la cobertura por grupo importa.

</details>

## Evidencia, reflexión y siguiente paso

Conserva código, tablas, figuras y una nota de interpretación para histograma,
caja y dispersión. Explica base, unidad, variabilidad, exclusiones y límites;
registra evidencia y dudas en PROGRESS.md sin confundir material disponible
con aprendizaje acreditado.

Reflexiona: ¿qué perdía el promedio? ¿Qué parte de la figura depende de una
decisión de agrupación? ¿Qué dato exterior conservarías y por qué? ¿Cómo
comprobarías un par si solo vieras una nube sin identificadores?

No hay checkpoint de proyecto implementado. Continúa con el
[04.05 — Escalas, etiquetas y accesibilidad](../../../curriculum/04_visualization_python/05_scales_labels_accessibility/README.md).
