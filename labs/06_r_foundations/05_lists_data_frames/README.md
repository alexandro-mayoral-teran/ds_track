# Lab 06.05 — Consultar ventas conservando su estructura

**Tiempo orientativo:** 60–90 minutos, repartibles entre sesiones.

## Propósito, entradas y preparación

Aplica la [lección 06.05](../../../curriculum/06_r_foundations/05_lists_data_frames/README.md).
Necesitas vectores, selección y faltantes de 06.02–06.04. La entrada es la
muestra de seis ventas del [script](../../../curriculum/06_r_foundations/05_lists_data_frames/listas_tablas.R).
No hay archivos que importar, paquetes que instalar ni proyecto/checkpoint
implementado asociado. Ejecuta el script en una sesión nueva con uno de los
recorridos de la lección; luego, desde la raíz en consola R, carga sus objetos:

```r
source("curriculum/06_r_foundations/05_lists_data_frames/listas_tablas.R", encoding = "UTF-8")
```

Conserva el script y las muestras anteriores. Guarda tu trabajo en una copia
personal bajo `output/` de este lab, ignorado por Git. Predice antes de ejecutar;
las soluciones son una alternativa razonada, no una entrega para copiar.

## 1. Explicar una lista antes de construir una tabla

Construye `ficha_lab` con identificador V002, unidades 2L, precio 120 y dos
notas de texto. Inspecciona nombres, longitud, tipo y estructura. Extrae las
unidades conservando la lista y después como contenido. ¿Cuántas ventas
describe? ¿Por qué `length` no responde esa pregunta por sí solo?

<details>
<summary>Solución razonada: componentes y contenido</summary>

```r
ficha_lab <- list(id_venta = "V002", unidades = 2L, precio_mxn = 120,
                  notas = c("Venta ficticia", "Revisada en el lab"))
print(names(ficha_lab))
print(length(ficha_lab)) # 4 componentes; describe una venta.
print(typeof(ficha_lab)) # "list"
str(ficha_lab)
str(ficha_lab["unidades"]) # Lista de un componente.
str(ficha_lab[["unidades"]]) # int 2.
print(length(ficha_lab$notas)) # 2 notas, no dos ventas.
```

La interpretación depende de qué representa cada componente. Una lista no
impone que los componentes sean filas de una tabla.

</details>

## 2. Reconstruir e inspeccionar las ventas

Construye `ventas_lab` desde los tres vectores fuente del script y calcula el
importe usando sus columnas. Antes comprueba las tres longitudes. Explica
la unidad de fila y muestra nombres, dimensiones, `length` y `str`.
No uses `mal_reciclada` como entrada. ¿Qué control falta aunque las longitudes
sean iguales?

<details>
<summary>Solución razonada: rectangular y con correspondencia</summary>

```r
print(c(length(id_venta), length(unidades), length(precio_mxn))) # 6 6 6
ventas_lab <- data.frame(id_venta = id_venta, unidades = unidades,
                         precio_mxn = precio_mxn, stringsAsFactors = FALSE)
ventas_lab$importe_mxn <- ventas_lab$unidades * ventas_lab$precio_mxn
print(names(ventas_lab))
print(dim(ventas_lab)) # 6 4
print(length(ventas_lab)) # 4 columnas.
str(ventas_lab) # character, integer, double y double.
print(ventas_lab) # Importes 300 240 0 120 NA NA.
```

Una fila es una venta. Revisa los pares identificador/unidades/precio contra
la muestra de la lección: igual longitud no demuestra que los vectores estén
en el mismo orden. Las etiquetas de fila impresas no sustituyen `id_venta`.

</details>

## 3. Elegir la forma y el orden del resultado

Obtén importes como vector y como tabla 6 × 1. Recupera V004 y V001 en ese
orden, con identificador e importe; después V003 como tabla 1 × 4.
Muestra dimensiones y tipos para justificar la forma, sin confiar solo en
cómo se imprime. Explica dónde van filas y columnas en los corchetes.

<details>
<summary>Solución razonada: extraer y conservar dimensiones</summary>

```r
vector_lab <- ventas_lab[["importe_mxn"]]
tabla_lab <- ventas_lab[, "importe_mxn", drop = FALSE]
print(typeof(vector_lab)) # "double"
print(length(vector_lab)) # 6
print(dim(vector_lab)) # NULL
print(class(tabla_lab)) # "data.frame"
print(dim(tabla_lab)) # 6 1
seleccion_lab <- ventas_lab[c(4, 1), c("id_venta", "importe_mxn"), drop = FALSE]
print(seleccion_lab) # V004 120; V001 300.
print(dim(seleccion_lab)) # 2 2
cero_lab <- ventas_lab[ventas_lab$id_venta == "V003", , drop = FALSE]
print(cero_lab) # V003 0 50 0.
print(dim(cero_lab)) # 1 4
```

La coma separa filas de columnas. La tabla de una columna no se puede tratar
como si fuera sin más un vector numérico: extrae su columna para calcular.

</details>

## 4. Consultar sin perder pendientes ni confundir el vacío

Usa el umbral **100**, distinto del ejemplo principal. Separa cumplen, no
cumplen conocidos y pendientes; conserva todas las columnas y concilia con
seis filas. Consulta también V999. Explica por qué las dos tablas, de
pendientes y de búsqueda sin coincidencias, no representan lo mismo.

<details>
<summary>Solución razonada: tres grupos y una tabla vacía</summary>

```r
condicion_lab <- ventas_lab$importe_mxn >= 100
conocida_lab <- !is.na(condicion_lab)
cumplen_lab <- ventas_lab[conocida_lab & condicion_lab, , drop = FALSE]
no_cumplen_lab <- ventas_lab[conocida_lab & !condicion_lab, , drop = FALSE]
pendientes_lab <- ventas_lab[is.na(condicion_lab), , drop = FALSE]
print(cumplen_lab$id_venta) # V001 V002 V004
print(no_cumplen_lab$id_venta) # V003
print(pendientes_lab$id_venta) # V005 V006
print(c(nrow(cumplen_lab), nrow(no_cumplen_lab), nrow(pendientes_lab))) # 3 1 2
print(nrow(cumplen_lab) + nrow(no_cumplen_lab) + nrow(pendientes_lab)) # 6
vacia_lab <- ventas_lab[ventas_lab$id_venta == "V999", , drop = FALSE]
print(dim(vacia_lab)) # 0 4
print(dim(pendientes_lab)) # 2 4
print(typeof(vacia_lab$unidades)) # "integer"
```

V005 conserva su precio y V006 sus unidades. Hay dos registros con información
incompleta; en la búsqueda V999 no hay registros. V003 sí tiene cero observado.
El umbral nuevo no cambia los importes ni su cobertura.

</details>

## 5. Confirmar otro dato en una copia

Una revisión ficticia confirma que el precio de V006 era **60 MXN**.
Trabaja desde `ventas_lab`, no desde `ventas_confirmadas` del script.
Comprueba cuántas filas seleccionas, cambia solo ese precio y recalcula el
importe. Informa conocidos, faltantes, cobertura, suma y media observadas;
contrasta con el original. ¿Qué pasaría si olvidaras recalcular?

<details>
<summary>Solución razonada: original 660 y variante 780</summary>

```r
confirmadas_lab <- ventas_lab
fila_v006_lab <- confirmadas_lab$id_venta == "V006"
print(sum(fila_v006_lab)) # 1
confirmadas_lab$precio_mxn[fila_v006_lab] <- 60
confirmadas_lab$importe_mxn <- confirmadas_lab$unidades * confirmadas_lab$precio_mxn
print(confirmadas_lab[fila_v006_lab, , drop = FALSE]) # V006 2 60 120
print(sum(!is.na(confirmadas_lab$importe_mxn))) # 5
print(sum(is.na(confirmadas_lab$importe_mxn))) # 1
print(100 * sum(!is.na(confirmadas_lab$importe_mxn)) / nrow(confirmadas_lab)) # 83.33333 aprox.
print(sum(confirmadas_lab$importe_mxn, na.rm = TRUE)) # 780
print(mean(confirmadas_lab$importe_mxn, na.rm = TRUE)) # 156
print(ventas_lab[ventas_lab$id_venta == "V006", , drop = FALSE]) # V006 2 NA NA
print(sum(ventas_lab$importe_mxn, na.rm = TRUE)) # 660
```

La variante tiene cinco importes conocidos de seis y uno pendiente: suma
observada 780 MXN y media 156 MXN. El total completo sigue desconocido.
Sin recalcular, V006 mantendría un importe desactualizado `NA` a pesar del
precio confirmado. El original conserva dos importes faltantes.

</details>

## 6. Diagnosticar una tabla plausible pero incorrecta

Inspecciona `mal_reciclada` del script. Compara sus seis precios con la fuente
y justifica por qué no sirve para resumirla. Explica también por qué
`ventas_lab$importe` podría funcionar mientras `ventas_lab[["importe"]]`
devuelve `NULL`. No uses nombres parciales en tu entrega.

<details>
<summary>Solución razonada: revisar valores y nombres exactos</summary>

```r
print(mal_reciclada$precio_mxn) # 75 120 75 120 75 120
print(ventas_lab$precio_mxn) # 75 120 50 40 100 NA
print(names(ventas_lab))
print(ventas_lab[["importe"]]) # NULL: nombre exacto inexistente.
print(ventas_lab[["importe_mxn"]]) # Vector correcto, con dos NA.
```

El reciclaje cambió cuatro precios y ocultó un faltante. Tener seis filas no
lo vuelve correcto. `$` puede buscar parcialmente; `[[` usa coincidencia
exacta por defecto. Revisa nombres antes de interpretar un `NULL` como dato.

</details>

## Evidencia, comprobación y reflexión

Conserva tu script y una nota con versión/sesión, estructura 6 × 4, vector y
tabla 6 × 1, selección V004/V001, grupos 3/1/2, vacío 0 × 4, original 660 y
variante 780 con sus coberturas. Reinicia la sesión y ejecuta tu archivo desde
cero; no basta con que funcione después de otras ejecuciones en consola.

Explica con tus palabras:

1. ¿Qué cuenta `length` en una lista, en una columna y en un data.frame?
2. ¿Cómo conservaste la identidad y los datos conocidos de los pendientes?
3. ¿Qué comprobación detectaría una columna movida aunque sus longitudes coincidan?
4. ¿Por qué un importe calculado exige recalcular después de confirmar un dato?

Cierra cuando puedas justificar formas, correspondencias y resultados sin
depender de la solución. Registra evidencia real y dudas en
[PROGRESS.md](../../../PROGRESS.md). Después continúa con el
[06.06 — Funciones y control de flujo](../../../curriculum/06_r_foundations/06_functions_control/README.md). Volver a la [lección 06.05](../../../curriculum/06_r_foundations/05_lists_data_frames/README.md).
