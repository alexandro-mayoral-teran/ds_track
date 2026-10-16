# Lab 06.03 — Seleccionar sin perder correspondencia

## Propósito, entradas y resultado

Este lab acompaña [06.03 — Seleccionar elementos](../../../curriculum/06_r_foundations/03_subsetting/README.md).
Recibes las mismas cuatro ventas de 06.02 y
[seleccionar_ventas.R](../../../curriculum/06_r_foundations/03_subsetting/seleccionar_ventas.R).
Usa el recorrido completo de tu shell en la lección con el R ya elegido; no
necesitas instalar paquetes ni construir tablas. Las listas aparecen solo como
vista mínima para comparar operadores; su desarrollo sigue en 06.05.

Conserva una nota personal con predicciones, valores, tipos/longitudes, identidades
seleccionadas y una variante. Guarda tu práctica en output con nombres nuevos y
mantén intactas las muestras anteriores. No hay proyecto/checkpoint implementado
asociado. Una sesión puede cubrir solo parte del lab.

## A. Predecir posiciones, orden y duplicados

Antes de ejecutar, predice importe_mxn[1], importe_mxn[c(4, 1)],
importe_mxn[c(1, 1)], importe_mxn[-c(2, 4)] e importe_mxn[0].
Ejecuta el archivo completo desde una sesión nueva y registra código/versión.
Después comprueba las expresiones en la consola.

Explica qué cambia al repetir una posición y por qué 0 no significa primer
elemento. ¿Qué diferencia hay entre [] y [0]? No confundas [1] en la salida de
print con una selección que debas copiar como parte del dato.

<details>
<summary>Resultados y explicación</summary>

Se esperan 300; 120/300; 300/300; 300/0; y numeric(0), respectivamente.
La selección respeta el orden del índice. Repetir 1 repite la primera observación;
no produce otra venta original. [] conserva todos los elementos, [0] ninguno.
La longitud del vacío es cero; el importe cero de la tercera venta sí es observado.
El archivo correcto debe terminar con código 0 y sin avisos de selección.

</details>

## B. Seleccionar nombres y conservar etiquetas

Utiliza importes_por_venta del script. Predice y comprueba valores, names,
typeof y length de importes_por_venta["V004"] y
importes_por_venta[["V004"]]. Explica por qué imprimir 120 no basta para afirmar
que ambos objetos son idénticos en todas sus propiedades.

Después pide V004 y V001 por nombre y compara el orden con una máscara que
seleccione primera y cuarta. Explica por qué asignar names no hace una unión
con otro archivo y por qué nombres duplicados requieren revisar la entrada.

<details>
<summary>Comprobación razonada</summary>

Ambas extracciones atómicas tienen valor 120, tipo double y longitud 1.
Con [ se conserva el nombre V004; con [[ se elimina esa etiqueta. La selección
por c("V004", "V001") produce 120/300 en ese orden. La máscara
c(TRUE, FALSE, FALSE, TRUE) produce 300/120 en el orden original.
Los nombres etiquetan posiciones ya existentes: no emparejan por sí mismos las
cantidades de una fuente con los precios de otra ni garantizan unicidad.

</details>

## C. Una máscara para todas las entradas relacionadas

Selecciona segunda y cuarta venta mediante una máscara completa de longitud 4.
Usa la misma máscara en id_venta, unidades, precio_mxn e importe_mxn.
Comprueba que el producto de las cantidades/precios elegidos coincide con los
importes seleccionados y calcula el total. Conserva los cuatro vectores originales.

Predice qué ocurriría con una máscara de solo dos valores TRUE/FALSE. Después
explica por qué el caso unidades > 0 deja total 660, pero no describe las mismas
cuatro observaciones de la fuente.

<details>
<summary>Una solución y la información que debe acompañarla</summary>

Con los vectores definidos por el archivo de la lección:

```r
elegidas_lab <- c(FALSE, TRUE, FALSE, TRUE)
ids_lab <- id_venta[elegidas_lab]
unidades_lab <- unidades[elegidas_lab]
precios_lab <- precio_mxn[elegidas_lab]
importes_lab <- importe_mxn[elegidas_lab]
print(ids_lab)                       # V002 V004
print(unidades_lab * precios_lab)    # 240 120
print(importes_lab)                  # 240 120
print(sum(importes_lab))             # 360
```

El total elegido es 360 MXN para dos ventas. Aplicar la misma máscara mantiene
la correspondencia por posición en esta muestra. Una máscara c(TRUE, FALSE)
se recicla y elegiría primera y tercera sin aviso: no cumple la selección pedida.
El caso de unidades positivas elimina solo de esa selección la venta de importe
cero; por eso su total sigue 660 aunque el conteo sea 3. Deben revisarse también
identificadores y conteos, no solo la suma.

</details>

## D. Diferenciar contenedor y contenido

En la lista mínima paquete_ventas, consulta typeof y length de
paquete_ventas["importes"], paquete_ventas[["importes"]] y paquete_ventas$importes.
Explica qué mide length en cada caso. Si campo contiene "importes", decide si
debes usar paquete_ventas$campo o paquete_ventas[[campo]].

<details>
<summary>Interpretación</summary>

La primera selección es una lista de longitud 1; conserva un componente que
contiene el vector de importes. Las otras extraen ese contenido: double de
longitud 4, con sus etiquetas de venta. Un componente extraído no tiene por
qué ser un solo número. [[campo]] utiliza el texto guardado en la variable;
$campo buscaría literalmente un componente llamado campo, inexistente aquí.
No utilices $ para un vector atómico aunque tenga nombres.

</details>

## E. Observar fronteras sin ocultar errores

En una consola de R, prueba por separado importe_mxn[5], importe_mxn[[5]],
importes_por_venta["V999"], importe_mxn[c(-1, 2)] e importe_mxn$V001.
Registra cuáles producen un faltante y cuáles un error. No añadas esos errores
al archivo correcto ni interpretes un NA como una venta con importe cero.

Explica cómo cambia la conclusión si el objeto es una lista en lugar del vector
atómico de esta actividad. No se exige aún tratar NA con condiciones ni imputarlo.

<details>
<summary>Qué comprobar</summary>

La selección con [5] y el nombre inexistente mediante [ devuelven NA en este
vector. [[5]], mezclar índices positivos/negativos y aplicar $ al vector atómico
producen errores. El texto exacto puede variar por idioma. Una lista puede
devolver NULL al extraer un nombre inexistente con [[, de modo que no debes
generalizar «todo nombre inexistente da error» a cualquier objeto de R.

</details>

## F. Modificar una copia y volver a comprobar

En una copia personal del script, crea precios_lab_variante desde precio_mxn y
reemplaza solo su segunda posición por 100. Predice el nuevo total y conserva
el precio original. Comprueba longitud y tipo después de reemplazar; no cambies
una cifra del resultado para forzarlo.

<details>
<summary>Una solución</summary>

```r
precios_lab_variante <- precio_mxn
precios_lab_variante[2] <- 100
print(precios_lab_variante)           # 75 100 50 40
print(precio_mxn)                     # 75 120 50 40
print(length(precios_lab_variante))   # 4
print(typeof(precios_lab_variante))   # double
print(sum(unidades * precios_lab_variante)) # 620
```

La segunda venta pasa de 240 a 200; el total baja 40 MXN de 660 a 620.
La copia conserva cuatro precios double y el original sigue igual. Si se
escribiera "100" como texto, podría cambiar el tipo de todo el vector y no
sería la misma modificación numérica.

</details>

## Ampliación opcional y reflexión

Si seguiste la matriz de una columna en la lección, explica dim del resultado
con y sin drop = FALSE. No es requisito dominar matrices ni adelantar data frames.

Conserva predicciones, selecciones de 420/360, conteos/identificadores, errores
observados, contraste de operadores y variante de 620. Anota versión y dudas.

- ¿Cuándo importan tanto las etiquetas como el valor impreso?
- ¿Por qué una máscara corta o un índice repetido puede alterar la pregunta?
- ¿Qué demuestra y qué no demuestra que dos selecciones sumen 660?
- ¿Por qué extraer un componente puede devolver un vector de longitud 4?

Registra evidencia real y dudas en PROGRESS.md. Puedes cerrar la práctica cuando
predigas valores/estructuras y mantengas la correspondencia al seleccionar.
Desarrollar el material no acredita aprendizaje ni completa un proyecto.

Continúa con [06.04 — Lógica y valores faltantes](../../../curriculum/06_r_foundations/04_logic_missing/README.md).
Volver a la [lección 06.03](../../../curriculum/06_r_foundations/03_subsetting/README.md).
