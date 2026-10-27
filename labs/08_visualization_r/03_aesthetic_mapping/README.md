# Lab 08.03 — Mapear y fijar estéticas

## Propósito y entradas

Explicar y corregir mapeos, estilos y agrupación. Lee primero la
[lección 08.03](../../../curriculum/08_visualization_r/03_aesthetic_mapping/README.md).
Reutiliza el proyecto renv de 07.10 y tu script `output/mi_esteticas.R` de la
lección. No necesitas instalaciones, nuevas fuentes ni exportación de figuras.

Abre el proyecto en RStudio o tu IDE. Crea `output/mi_esteticas_lab.R`, sin
sobrescribir trabajo anterior. Ejecuta bloques en Console de R con la raíz del
proyecto como directorio. Conserva fuente, funciones, lockfile y entregas.

## Actividad esencial

1. Sin ejecutar, explica `fill = "red"`, `aes(fill = "red")`,
   `aes(fill = corte)` y `aes(fill = "corte")`. Predice rellenos y categorías
   de leyenda; identifica qué casos representan realmente una columna.
2. Reconstruye la lección desde el CSV. Mantén 14 IDs comunes, 28 observaciones
   y sumas 29000/31800 MXN. Corrige `accidental` para obtener barras de relleno
   fijo `#246A86` sin categoría de relleno accidental. Comprueba sus alturas.
3. Conserva la variante que sí representa fecha con relleno. Usa `paleta` con
   nombres, invierte las filas de `resumen` y comprueba la correspondencia
   fecha/relleno por x, además de la altura. Explica por qué no basta comparar
   un vector de colores sin considerar su fecha.
4. Dibuja 28 puntos con forma 21, relleno por fecha, borde fijo y tamaño fijo.
   Después representa fecha con color y forma. Explica dónde se usa cada
   propiedad y cómo detectar superposición sin eliminar registros.
5. Diagnostica el siguiente gráfico. Anticipa cuántos grupos de línea habrá y
   qué fechas reunirá cada grupo. Después compruébalo con `layer_data`.
6. Corrígelo para tener una trayectoria por ID con trazo gris discontinuo,
   `linewidth = 0.8`, y puntos con color y forma por fecha. Conserva 14 grupos
   de dos filas, sus pares originales y 28 puntos. Explica qué mapeos son
   globales, cuáles locales y qué propiedades son constantes.
7. Guarda, reinicia R y ejecuta el script completo. Inspecciona figuras y
   documenta una predicción corregida, las comprobaciones y los límites de
   interpretación. No basta entregar la imagen de referencia.

Este es el caso a diagnosticar; ejecútalo después de reconstruir la lección:

```r
mal_agrupado <- ggplot2::ggplot(detalle,
    ggplot2::aes(fecha_corte, saldo_mxn, colour = corte)) +
  ggplot2::geom_line() + ggplot2::geom_point()
print(mal_agrupado)
```

Que se dibuje sin error no demuestra que cada línea corresponda a un crédito.
No cambies las claves, no filtres créditos y no sustituyas la tabla por dos
totales para hacer desaparecer el problema.

## Resultado y comprobación

| Evidencia | Resultado esperado |
| --- | --- |
| Reconstrucción | 48 = 36 aceptados + 12 rechazados; 14 IDs comunes |
| Barras fijas y mapeadas | Dos alturas 29000/31800 MXN; distinta intención del relleno |
| Paleta con filas invertidas | Misma fecha, relleno y altura; categorías no dependen del orden de filas |
| Caso incorrecto | Dos grupos de 14 filas; cada grupo contiene una sola fecha |
| Caso corregido | 14 grupos de dos filas; cada uno tiene ambas fechas y el par de un ID |
| Puntos | 28 registros preparados para dibujar; dos colores y dos formas por fecha |
| Conservación | CSV intacto, mismos saldos y población; reconstrucción desde sesión nueva |

Los grupos numéricos de la capa no son IDs de negocio. Compara conjuntos de
pares con sus repeticiones y revisa la clave original. Las sumas por fecha
pueden ser correctas aunque las conexiones entre créditos sean incorrectas.

## Pistas

<details>
<summary>Ver pistas después de formular tus predicciones</summary>

Para un estilo fijo, mueve la propiedad fuera de `aes`. Para fecha, usa la
columna sin comillas. `shape = 21` permite controlar borde e interior.
`group = id_credito` puede ser local a `geom_line`; el color por fecha puede
ser local a `geom_point`. Evita heredar color por fecha en la línea cuando no
quieres que determine sus grupos. `linetype = "dashed"` fija el trazo discontinuo.

En la capa incorrecta, `table(capa$group)` revela tamaños; `split` permite
comprobar fechas dentro de cada grupo. En el caso correcto deben aparecer dos
fechas distintas por grupo. `group = 1` conservaría una sola serie en el detalle.

</details>

## Solución razonada

<details>
<summary>Ver una solución después de intentar la actividad</summary>

La cadena dentro de `aes` crea una categoría literal; fuera fija el relleno.
`aes(fill = corte)` representa las dos fechas; `aes(fill = "corte")` representa
una sola cadena repetida. Para reconstruir sin workspace, empieza tu script con:

```r
source("output/mi_esteticas.R", encoding = "UTF-8")
corregidas <- base_barras + ggplot2::geom_col(fill = "#246A86", width = 0.6)
invertido <- resumen[nrow(resumen):1, ]
por_fecha <- ggplot2::ggplot(invertido, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_col(ggplot2::aes(fill = corte), width = 0.6) +
  ggplot2::scale_fill_manual(values = paleta)
capa <- ggplot2::layer_data(por_fecha, 1)
capa <- capa[order(capa$x), ]
stopifnot(identical(ggplot2::layer_data(corregidas, 1)$y, c(29000, 31800)),
          all(ggplot2::layer_data(corregidas, 1)$fill == "#246A86"),
          identical(capa$y, c(29000, 31800)),
          identical(capa$fill, unname(paleta[levels(resumen$corte)])))
print(corregidas)
print(por_fecha)
print(puntos)
print(doble_senal)
```

Ordenar por x en la tabla preparada permite comparar septiembre primero. El
factor conserva el orden de categorías aunque invertimos las filas. En una
práctica con fechas diferentes, adapta el control a sus claves; no compares
colores por la posición accidental de los registros.

Agrega ahora el bloque del caso incorrecto de la actividad a tu script y luego:

```r
incorrecta <- ggplot2::layer_data(mal_agrupado, 1)
grupos_incorrectos <- split(incorrecta, incorrecta$group)
stopifnot(length(grupos_incorrectos) == 2L,
          all(vapply(grupos_incorrectos, nrow, integer(1)) == 14L),
          all(vapply(grupos_incorrectos,
            function(g) length(unique(g$x)), integer(1)) == 1L))

reparado <- ggplot2::ggplot(detalle, ggplot2::aes(fecha_corte, saldo_mxn)) +
  ggplot2::geom_line(ggplot2::aes(group = id_credito),
    colour = "#68747A", linewidth = 0.8, linetype = "dashed") +
  ggplot2::geom_point(ggplot2::aes(colour = corte, shape = corte), size = 3) +
  ggplot2::scale_colour_manual(values = paleta) +
  ggplot2::scale_x_date(breaks = resumen$fecha_corte, date_labels = "%Y-%m-%d") +
  ggplot2::labs(title = "Una trayectoria por crédito",
    subtitle = "14 IDs comunes; puntos por fecha y líneas discontinuas por ID",
    x = "Fecha de corte", y = "Saldo por crédito (MXN)",
    colour = "Fecha de corte", shape = "Fecha de corte",
    caption = "Datos sintéticos. Base común: 14/18 por corte.\nDos observaciones por ID; los tramos no describen mediciones diarias.") +
  ggplot2::theme_minimal(base_size = 12)
g <- split(ggplot2::layer_data(reparado, 1),
           ggplot2::layer_data(reparado, 1)$group)
firmas <- vapply(g, function(z) {
  z <- z[order(z$x), ]
  stopifnot(nrow(z) == 2L, identical(z$x, as.numeric(resumen$fecha_corte)))
  firma(z$y[1], z$y[2])
}, character(1))
stopifnot(length(g) == 14L,
          identical(sort(unname(firmas)), sort(firma(pares$saldo_sep, pares$saldo_oct))),
          nrow(ggplot2::layer_data(reparado, 2)) == 28L,
          identical(huella, tools::md5sum(ruta)))
print(reparado)
```

Las líneas heredan solo x/y; agrupan por ID con estilo fijo. Los puntos heredan
x/y y agregan color/forma por fecha. El trazo discontinuo no crea otra categoría
ni una leyenda propia. La agrupación por fecha del caso incorrecto preservaba
las posiciones y sumas, pero conectaba créditos distintos en la misma fecha.

Guarda, reinicia R mediante Session > Restart R y ejecuta en Console:

```r
source("output/mi_esteticas_lab.R", encoding = "UTF-8")
```

Si elegiste otros nombres, ajusta los `source`. El
[script de referencia](../../../curriculum/08_visualization_r/03_aesthetic_mapping/explorar_esteticas.R)
puede ayudar a contrastar la lección. El script del lab debe incluir el caso
incorrecto antes de inspeccionarlo; no dependas de haberlo ejecutado a mano.

</details>

## Extensión opcional — Una capa con otra unidad

Añade los dos totales como puntos negros de otra forma sobre un gráfico
independiente. Si el gráfico tuviera `group = id_credito` global, la tabla de
dos sumas no tendría esa columna para heredarla. Define datos y mapeos de esa
capa explícitamente con `inherit.aes = FALSE`, como en 08.01. Justifica antes
si mezclar totales e individuales en un mismo eje sirve a una pregunta: aquí
los totales comprimirían mucho los saldos individuales. No es requisito crear
esa figura ni sustituir el gráfico corregido por ella.

## Evidencia, reflexión y salida

Conserva script propio, predicciones, comprobaciones y notas de inspección visual.
Registra evidencia y dudas reales en tu bitácora personal junto a la práctica.
No hay proyecto integrador ni checkpoint activo; ejecutar la solución no
acredita por sí solo aprendizaje.

- ¿Por qué una cadena en `aes` puede producir un color diferente del que nombra?
- ¿Qué cambia al pasar de relleno fijo a escala manual por fecha?
- ¿Qué determina el interior y el borde de un punto con forma 21?
- ¿Por qué `group = 1` tenía sentido sobre dos sumas y falla para los 14 IDs?
- ¿Puede haber sumas correctas y líneas incorrectas? Muestra tu comprobación.
- ¿Qué información aporta la forma además del color y qué no puede mostrar la figura?

Cierra cuando puedas reconstruir, corregir y justificar esas decisiones.
Siguiente: [08.04 — Escalas y coordenadas](../../../curriculum/08_visualization_r/04_scales_coordinates/README.md),
ya disponible. Volver a la [lección 08.03](../../../curriculum/08_visualization_r/03_aesthetic_mapping/README.md).
