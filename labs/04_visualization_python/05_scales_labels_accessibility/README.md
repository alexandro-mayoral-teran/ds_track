# Lab 04.05 — Escalas, etiquetas y accesibilidad

## Propósito, entradas y preparación

Lee la [lección 04.05](../../../curriculum/04_visualization_python/05_scales_labels_accessibility/README.md)
y completa los prerrequisitos de 04.04. Recibes scales.py, los CSV sintéticos
originales de SQL y cuatro figuras. Tu tarea es revisar una representación,
corregir decisiones y explicar sus límites conservando los datos.

Tiempo orientativo: dos sesiones de 60–90 minutos para A–D; E es ampliación.
Puedes resolver una parte y registrar dudas antes de continuar. Usa el entorno
elegido y el recorrido completo de tu shell en la lección. Ejecuta con una carpeta
nueva `output/lab_05` dentro de la sección y corte 2026-10-31.

**Entradas:** corte.csv, medianas.csv, positivos_log.csv, excluidos_log.csv,
medianas_por_corte.csv y los PNG generados. **Entrega:** tablas comprobadas,
figura corregida desde código, descripción textual y nota de decisiones.
Conserva fuentes y SQLite. No necesitas un notebook ni una aplicación.

## A. Revisar barras y justificar su origen

Abre origen.png y medianas.csv. Antes de consultar la solución:

1. Identifica población, medida, corte y unidad. ¿Es saldo total o mediana?
2. Confirma los valores de comercio y consumo ordenando sus saldos en corte.csv.
3. Calcula diferencia y razón entre medianas. Después calcula las longitudes
   visibles cuando el eje comienza en 1600 MXN.
4. Explica por qué «comercio tiene diez veces la mediana de consumo» sería falso.
5. En una copia de scales.py, conserva la vista desde cero y escribe un título
   propio que nombre medida y corte. Usa otra carpeta nueva para su resultado.

**Comprobación:** el cambio de presentación debe mantener 3100 y 1750 MXN,
el orden de categorías y sus coberturas. No modificar CSV para reducir la diferencia.

<details>
<summary>Ver solución razonada de A</summary>

La diferencia es 1350 MXN y la razón 3100/1750 ≈ 1,77. Al recortar desde
1600, las longitudes visibles son 1500 y 150, cuya razón es 10. Es una
propiedad del dibujo recortado, no de los saldos. La corrección incluye cero
y etiqueta «Mediana del saldo conocido (MXN)», corte 2026-10-31 y datos sintéticos.
Comercio tiene 5/5 conocidos y consumo 10/10; mediana no significa suma.
Puedes editar baseline_figure en una copia situada en la misma carpeta para
mantener la reutilización de 04.04. Conservar solo el panel corregido es opcional.

</details>

## B. Decidir si una escala log responde la pregunta

Abre lineal_log.png y coteja los cuatro CSV del corte.

1. Concilia 24 registros con positivos y exclusiones; cuenta cada motivo.
2. Identifica el crédito con saldo cero y comprueba que permanece en corte.csv.
3. Explica la diferencia entre distancias 100 → 1000 y 1000 → 10000 en log.
   ¿Representan el mismo incremento en MXN?
4. Elige una escala para describir **todos los saldos conocidos** de octubre.
   Justifica si excluir el cero ayuda a responder esa pregunta.
5. Explica qué harías con un saldo negativo en otro conjunto de datos, sin
   dibujarlo en log ordinario ni cambiarlo a positivo.

**Resultado:** conciliación, elección razonada y protocolo para valores fuera
del dominio de la escala. No sumar 1 ni eliminar exclusiones de la evidencia.

<details>
<summary>Ver solución razonada de B</summary>

24 = 20 positivos + 4 excluidos: 1 cero (crédito 004), 3 ausentes y 0 negativos.
Hay 21 conocidos en lineal. En log, ambos saltos multiplican por diez, pero
sus incrementos son 900 y 9000 MXN. Para todos los conocidos elegimos lineal:
los positivos abarcan 1300–3300 MXN y perder cero no aporta una ventaja clara.
En otro conjunto, un negativo debe conservarse y revisarse con la regla del
dominio; si es válido, elegir una representación que lo admita. El contrato
sintético actual rechaza negativos en la lectura: no introducirlos en la fuente.

</details>

## C. Corregir etiquetas y explicar ausencia

Usa etiquetas.png como referencia. Revisa esta propuesta problemática:
«Saldo total; educación = 0; comercio es el más riesgoso». Escribe qué cambiarías
y por qué. Redacta un título, unidad del eje, descripción breve de la imagen
y un párrafo que permita entender los valores sin verla.

Incluye cobertura de cada segmento, fecha y fuente sintética. Explica qué cambia
si expresas los importes en miles de MXN; distingue convertir la unidad de cambiar
el formato de marcas. No agregues intervalos de confianza sin método.

**Comprobación:** coteja descripción y figura con medianas.csv. Ninguna frase
debe convertir una mediana en suma, una ausencia en cero o un saldo en medida de riesgo.

<details>
<summary>Ver solución razonada de C</summary>

Título posible: «Mediana del saldo conocido por segmento · octubre de 2026».
Unidad: MXN. Descripción breve: «Comercio tiene la mayor mediana conocida;
educación no tiene saldos conocidos». Párrafo: comercio 3100 MXN (5/5), consumo
1750 (10/10), servicios 2550 (6/6); educación sin mediana (0/3). Son datos
sintéticos de SQL 03.01 al 2026-10-31, no evidencia de riesgo real.
En miles de MXN, comercio sería 3,1; hay que dividir una vez y nombrar la unidad.
Escribir «3 100» con espacios solo formatea 3100. Cobertura no es intervalo
de confianza y los bigotes de 04.04 tampoco lo son.

</details>

## D. Leer sin depender del color

Abre senales.png y medianas_por_corte.csv. Identifica los dos cortes por forma
y leyenda. Revisa la figura al tamaño que usarías al compartirla y, si tu visor
lo permite, en escala de grises. Anota si hay texto difícil de leer o superpuesto.

En tu copia del código cambia los dos colores por un gris oscuro y vuelve a
generar en otra carpeta nueva. Mantén círculo y cuadrado, fechas y valores.
¿Puedes identificar las series sin color? ¿Qué falta si entregas solo el PNG?

**Comprobación:** las medianas y coberturas no cambian. Educación conserva el
punto de septiembre y la ausencia de octubre. Escribe por qué comparar estos
resúmenes no acredita un cambio de los mismos créditos.

<details>
<summary>Ver solución razonada de D</summary>

En signals_figure puedes usar [("#333333", "o"), ("#333333", "s")]. El círculo
identifica septiembre y el cuadrado octubre mediante la leyenda. No se unen
categorías. Falta una descripción textual y acceso a valores/cobertura si solo
se comparte el PNG. Una revisión en gris detecta dependencia del color, pero
no verifica toda la accesibilidad. La base conocida puede cambiar por fecha;
usar los pares de 04.03 si la pregunta trata de cambios de los mismos créditos.

</details>

## E. Ampliación: una selección vacía

Ejecuta el script con `--cut 2026-11-30` y otra carpeta nueva. Esta fecha no está
en las fuentes. Compara las vistas del corte con el grupo educación de octubre.
¿«Sin registros» y «registros sin saldo conocido» significan lo mismo?
Recuerda que senales.png sigue comparando las dos fechas originales.

<details>
<summary>Ver solución razonada de E</summary>

El corte de noviembre contiene cero registros: no conocemos una población
observada para esa fecha. Educación en octubre tiene tres registros, pero
ningún saldo conocido. En ninguno de los casos se imputa cero ni se inventa
una mediana. La comparación senales se construye con las fechas de la fuente,
no con el argumento --cut, como declara la lección.

</details>

## Evidencia, reflexión y siguiente paso

Conserva código propio, tabla de conciliación, figura corregida, texto alternativo
y párrafo de lectura con límites. Registra evidencia y dudas en tu bitácora personal junto a la práctica;
desarrollar el material no acredita haber realizado esta práctica.

Reflexiona: ¿qué conclusión cambiaba solo por el eje? ¿Qué pregunta justifica
log? ¿Cómo sabe alguien qué significan los datos sin ver sus colores? ¿Qué
información seguiría faltando aunque la figura fuera legible?

No hay checkpoint de proyecto implementado. Continúa con el
[04.06 — Composición y exportación](../../../curriculum/04_visualization_python/06_composition_export/README.md).
