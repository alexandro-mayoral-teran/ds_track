# Lab 08.04 — Escalas y coordenadas

## Propósito y entradas

Justificar unidades, límites y ventanas mediante resultados comprobables. Lee
primero la [lección 08.04](../../../curriculum/08_visualization_r/04_scales_coordinates/README.md).
Usa el mismo proyecto renv de 07.10 y tu script `output/mi_escalas.R`. Se conserva
el CSV, las reglas de aceptación, las funciones anteriores y el lockfile.
No necesitas instalaciones ni una nueva entrega exportada.

En RStudio o tu IDE crea `output/mi_escalas_lab.R`, sin sobrescribir trabajo
anterior. Trabaja por bloques en Console de R, con la raíz del proyecto como
directorio. No dependas de los objetos que dejó otra sesión.

## Actividad esencial

1. Antes de ejecutar, explica qué cambia con `labels`, `breaks`, `limits`,
   `expand` y `coord_cartesian`. Identifica qué argumento puede afectar la
   estadística de una caja y cuál define solo marcas del eje.
2. Reconstruye la lección desde el CSV. Comprueba 14 pares, 29000/31800 MXN y
   los cuartiles de las cajas completa, limitada y con zoom. Explica por qué
   tener el CSV intacto no basta para afirmar que el cálculo del gráfico es igual.
3. Presenta las sumas como miles de MXN **solo mediante etiquetas**. Conserva
   posiciones de capa 29000/31800 y muestra marcas 0, 10, 20 y 30. Contrasta
   con la columna en miles de la lección. Explica cómo detectar una doble división.
4. Cambia el límite superior del experimento de septiembre a **2000 MXN**,
   conservando 1000 como inferior. Antes de ejecutar, predice si 2000 está dentro
   del intervalo, cuántos saldos quedan y qué mediana esperas. Dibuja límite de
   escala y zoom. Comprueba sus cuartiles y el conteo mediante la tabla original.
5. Si la pregunta pidiera realmente «saldos entre 1000 y 2000», crea dos copias:
   dentro/fuera del intervalo. Conserva todos los IDs, concilia conteos y sumas,
   e informa la cobertura. No cambies las reglas de aceptación de la cartera.
6. Revisa la muestra independiente de tres fechas. Explica sus distancias de
   1/30 días frente a las separaciones iguales del factor. Después muestra los
   dos cortes principales con Date y formato `%d/%m/%Y`; no inventes fechas observadas.
7. Comprueba las posiciones log10 de los saldos positivos. Ante la muestra
   independiente `c(0, 100, 1000)`, elige una escala que conserve el cero sin
   alterar datos. Justifica por qué no basta añadir 1 para evitar el problema.
8. Inspecciona la dispersión con proporción 1:1. Explica qué significa la
   diagonal y por qué no es una regresión ni prueba causas. Guarda, reinicia R
   y ejecuta el script completo. Conserva predicciones, resultados y una corrección propia.

## Resultado y comprobación

| Evidencia | Resultado esperado |
| --- | --- |
| Base comparable | 14 IDs, dos sumas 29000/31800 MXN; cobertura 14/18 por corte |
| Formato en miles | Rótulos 0/10/20/30; posiciones siguen en MXN |
| Límite 1000–2000, extremos incluidos | Siete dentro, siete fuera; 2000 incluido |
| Caja con ese límite de escala | Q1 1250, mediana 1400, Q3 1750 |
| Caja con zoom a esa ventana | Conserva Q1 1475, mediana 2050, Q3 2575; mediana fuera de la vista |
| Subpoblación explícita | Dentro 10500 MXN; fuera 18500 MXN; suma 29000 y 14 IDs conservados |
| Calendario independiente | Date: separaciones 1/30 días; factor: 1/1 posiciones |
| Cero independiente | Conservado con escala lineal; sin sumar constantes ni borrarlo |
| Dispersión | 14 pares, mismos MXN en ambos ejes y referencia de igualdad |

Una ventana puede ocultar incluso la mediana sin cambiar su valor. Una caja
parcial no basta para describir toda la distribución: compara el cálculo y
declara la vista recortada. En el límite de escala se esperan avisos de siete
valores retirados; no los silencies para afirmar cobertura completa.

## Pistas

<details>
<summary>Ver pistas después de escribir tus predicciones</summary>

Usa `>=` y `<=` para declarar los extremos incluidos de la subpoblación. La
igualdad con 2000 conserva ese saldo. Obtén los cuartiles tipo 7 con la función
`cuartiles` de la lección. Compara `lower`, `middle`, `upper` y los bigotes en
`layer_data`; no deduzcas los cuartiles solo del fragmento visible de la caja.

Para rotular miles divide `x` dentro de la función de etiquetas, no el saldo de
la tabla. Para el cero, dibuja la muestra aparte con escala lineal. En la
dispersión, la capa 1 es la referencia y la capa 2 contiene los pares.

</details>

## Solución razonada

<details>
<summary>Ver una solución después de intentar la actividad</summary>

Empieza `output/mi_escalas_lab.R` con la reconstrucción completa de la lección:

```r
source("output/mi_escalas.R", encoding = "UTF-8")
miles_lab <- base_barras + ggplot2::scale_y_continuous(
  limits = c(0, NA), breaks = c(0, 10000, 20000, 30000),
  labels = function(x) formato_mxn(x / 1000)
) + ggplot2::labs(y = "Saldo observado (miles de MXN)")
stopifnot(identical(ggplot2::layer_data(miles_lab, 1)$y, c(29000, 31800)))
print(miles_lab)
```

Las posiciones siguen en MXN; el eje declara la unidad de sus etiquetas. Si
decidieras trabajar con una columna en miles, los límites y las marcas también
tendrían que expresarse en miles. La etiqueta por sí sola no convierte valores.

```r
limite_lab <- base_caja +
  ggplot2::scale_y_continuous(limits = c(1000, 2000)) +
  ggplot2::labs(title = "Límite de escala: caja calculada con siete saldos",
    caption = "Demostración de censura; no es la caja de los 14 IDs.")
zoom_lab <- base_caja +
  ggplot2::coord_cartesian(ylim = c(1000, 2000),
    expand = c(bottom = FALSE, top = FALSE)) +
  ggplot2::labs(title = "Vista parcial de la caja de los 14 saldos",
    subtitle = "La mediana 2050 y el cuartil superior quedan fuera del panel",
    caption = "Datos sintéticos. Ventana 1000–2000 MXN; los valores superiores se conservan.")
dentro_lab <- septiembre$saldo_mxn >= 1000 & septiembre$saldo_mxn <= 2000
seleccion <- septiembre[dentro_lab, ]
exteriores <- septiembre[!dentro_lab, ]
q_lab <- cuartiles(seleccion$saldo_mxn)
l_lab <- ggplot2::layer_data(limite_lab, 1)
z_lab <- ggplot2::layer_data(zoom_lab, 1)
stopifnot(nrow(seleccion) == 7L, nrow(exteriores) == 7L,
          any(seleccion$saldo_mxn == 2000),
          identical(q_lab, c(1250, 1400, 1750)),
          identical(unname(unlist(l_lab[c("lower", "middle", "upper")])), q_lab),
          identical(z_lab[columnas_caja], completa[columnas_caja]),
          sum(as.double(seleccion$saldo_mxn)) == 10500,
          sum(as.double(exteriores$saldo_mxn)) == 18500,
          nrow(seleccion) + nrow(exteriores) == nrow(septiembre),
          sum(as.double(seleccion$saldo_mxn)) + sum(as.double(exteriores$saldo_mxn)) == 29000,
          identical(sort(c(seleccion$id_credito, exteriores$id_credito)),
                    sort(septiembre$id_credito)))
print(limite_lab)
print(zoom_lab)
```

El límite de escala recibe siete saldos para calcular; el zoom conserva los
catorce. La subpoblación seleccionada contiene 7/14 IDs comunes (50%) y 10500
MXN; los siete exteriores conservan 18500 MXN. La cobertura se refiere a la
base común de septiembre, no a todos los aceptados ni al archivo original.
Conservar los IDs comprueba la partición además de sumar cantidades.

```r
print(temporal)
print(espacio_fecha)
print(espacio_categoria)
stopifnot(identical(diff(ggplot2::layer_data(espacio_fecha, 1)$x), c(1, 30)),
          isTRUE(all.equal(ggplot2::layer_data(puntos_log, 1)$y,
                            log10(septiembre$saldo_mxn))))
cero_didactico <- data.frame(caso = c("A", "B", "C"), saldo_mxn = c(0, 100, 1000))
con_cero <- ggplot2::ggplot(cero_didactico, ggplot2::aes(caso, saldo_mxn)) +
  ggplot2::geom_point(size = 3, colour = "#246A86") +
  ggplot2::labs(title = "Muestra independiente: cero observado conservado",
    x = "Caso didáctico", y = "Saldo (MXN; escala lineal)")
print(con_cero)
print(comparacion)
stopifnot(identical(ggplot2::layer_data(con_cero, 1)$y, c(0, 100, 1000)),
          nrow(ggplot2::layer_data(comparacion, 2)) == 14L,
          identical(huella, tools::md5sum(ruta)))
```

La muestra de cero es independiente; no agrega registros a la cartera ni
modifica su validación. Una escala log10 no admite ese cero como posición
finita. Mantener una escala lineal resuelve la lectura sin cambiar los datos.
La diagonal de la dispersión representa igualdad de saldos; todos estos pares
sintéticos están 200 MXN por encima, sin justificar una causa.

Guarda y reinicia R mediante Session > Restart R. Desde la raíz del proyecto,
ejecuta en Console:

```r
source("output/mi_escalas_lab.R", encoding = "UTF-8")
```

Adapta los nombres de archivos si elegiste otros. Puedes contrastar la lección
con el [script de referencia](../../../curriculum/08_visualization_r/04_scales_coordinates/explorar_escalas.R).
Una solución válida incluye también la interpretación; las aserciones no la sustituyen.

</details>

## Extensión opcional — Transformar antes o después del cálculo

Sin modificar fuentes, calcula `cuartiles(log10(septiembre$saldo_mxn))` y
`log10(cuartiles(septiembre$saldo_mxn))`. Comprueba que no son idénticos y
explica la interpolación. Después contrasta las bisagras de una caja con
`scale_y_log10` con el primer cálculo. Esta extensión no cambia el criterio
de salida; no hace falta usar `coord_transform` ni ajustar modelos.

## Evidencia, reflexión y salida

Conserva script propio, tabla de predicciones, controles de unidades/cuartiles/
partición y notas de inspección visual. Registra evidencia real y dudas según
tu bitácora personal junto a la práctica. No hay proyecto integrador ni checkpoint
activo; consultar la solución no demuestra aprendizaje.

- ¿Cómo puede cambiar la mediana de una caja sin cambiar el CSV?
- ¿Qué información conserva un zoom que no deja ver toda la caja?
- ¿Qué unidades tienen tus posiciones, tus límites y tus etiquetas?
- ¿Por qué una marca del eje no demuestra que hubo una observación en esa fecha?
- ¿Qué perderías si borrases un cero para usar un logaritmo?
- ¿Cuándo tiene sentido igualar la longitud de una unidad en ambos ejes?

Cierra cuando puedas reconstruir y justificar esas decisiones. Siguiente:
[08.05 — Facetas y comparación entre grupos](../../../curriculum/08_visualization_r/05_facets_groups/README.md),
ya disponible. Volver a la [lección 08.04](../../../curriculum/08_visualization_r/04_scales_coordinates/README.md).
