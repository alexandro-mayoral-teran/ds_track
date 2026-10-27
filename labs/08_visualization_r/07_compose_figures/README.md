# Lab 08.07 — Componer figuras

## Propósito y entradas

Reunir resumen y detalle en un conjunto verificable y explicar qué comparte
cada vista. Lee la [lección 08.07](../../../curriculum/08_visualization_r/07_compose_figures/README.md)
y prepara el mismo proyecto renv mediante su preparador/restauración. Conserva
`respaldo_08_06/`, fuentes, funciones anteriores y entregas. La dependencia
añadida es patchwork 1.3.2; no necesitas otro paquete ni otra biblioteca por lab.

En RStudio o tu IDE crea `output/mi_composicion_lab.R`, sin sobrescribir trabajo.
Usa tu script `output/mi_composicion.R` de la lección y la raíz del proyecto
como directorio. Ejecuta en Console de R; no dependas del workspace anterior.

## Actividad esencial

1. Antes de ejecutar, explica por qué A y B son gráficos distintos y no una
   faceta. Identifica tabla, unidad de fila, marca, medida y población de cada
   uno. Predice cantidades de puntos y grupos de línea.
2. Reconstruye la lección y concilia el detalle con las sumas de A: 14 IDs,
   28 observaciones, 29000/31800 MXN. Explica por qué no puedes sumar ambas
   fechas como saldo en una fecha única.
3. Crea una disposición vertical con **A arriba y B abajo**, dando más altura
   al detalle. Conserva títulos, ejes, rótulos A/B, una nota común y el orden
   temporal. Justifica por qué los rangos verticales permanecen distintos.
4. Contrasta `guides = "keep"` y `guides = "collect"`. Inspecciona las leyendas
   al dibujar y comprueba que sus colores, formas y etiquetas significan lo
   mismo. No interpretes la recolección como una conciliación de datos.
5. En una copia de B, invierte la correspondencia de **colores por fecha**, sin
   alterar los saldos ni las formas. Reúne A y esa copia con `collect` y
   diagnostica la incoherencia. Después recupera las correspondencias comunes;
   no la ocultes eliminando leyendas o renombrando fechas.
6. Comprueba los hijos del conjunto correcto: dos puntos de suma, 28 puntos de
   detalle y 14 grupos por ID. Conserva una tabla y una descripción de ambas
   vistas, indicando agregación, cobertura y alcance descriptivo.
7. Inspecciona la disposición al tamaño previsto. Revisa títulos, notas, guía,
   rangos y recortes. Si no cabe, cambia disposición o redacción antes de
   reducir textos hasta hacerlos ilegibles.
8. Guarda, reinicia R y ejecuta el script completo. Conserva una predicción
   corregida o decisión comprobada y explica por qué una composición que se
   dibuja sin error todavía puede comparar poblaciones diferentes.

## Resultados y comprobación

| Evidencia | Resultado esperado |
| --- | --- |
| Dependencias | Proyecto sincronizado; patchwork 1.3.2 y metadatos anteriores respaldados |
| A | Dos sumas, 29000/31800 MXN, una serie de dos puntos |
| B | 28 puntos, 14 grupos por ID y dos fechas por grupo |
| Conciliación | 14 saldos por fecha suman lo que representa A; diferencia 2800 MXN |
| Disposición vertical | A arriba, B abajo; orden y descripción coherentes con rótulos |
| Guías | Mismas correspondencias de fecha; recogidas cuando son compatibles |
| Caso incorrecto | Importes intactos, colores por fecha incompatibles entre A y B |
| Conservación | Fuentes/funciones/entregas anteriores intactas; lockfile solo añade patchwork |

Una sola leyenda no prueba equivalencia de poblaciones; dos leyendas tampoco
deben eliminarse automáticamente. Primero revisa las correspondencias y si
realmente describen lo mismo. Los títulos de los ejes deben distinguir total
de saldo individual, aunque ambos se expresen en MXN.

## Pistas

<details>
<summary>Ver pistas después de formular tus predicciones</summary>

`wrap_plots(..., ncol = 1, heights = ...)` permite cambiar la disposición sin
recalcular datos. `plot_annotation` controla título y nota del conjunto; `&`
puede aplicar la posición de leyenda a todos sus gráficos. Usa paréntesis.

`conjunto[[1]]` y `conjunto[[2]]` permiten inspeccionar los hijos. En ambos,
la capa 1 contiene líneas y la 2 puntos. Revisa grupo por ID en B, no un grupo
único sobre las 28 filas. La escala de color correcta usa nombres de fechas,
no un vector cuyo significado dependa del orden de filas.

</details>

## Solución razonada

<details>
<summary>Ver una solución después de intentar la actividad</summary>

Empieza tu script reconstruyendo la lección:

```r
source("output/mi_composicion.R", encoding = "UTF-8")
diseno_lab <- patchwork::wrap_plots(p_resumen, p_detalle,
  ncol = 1, heights = c(1, 1.6), guides = "collect", axes = "keep", axis_titles = "keep")
conjunto_lab <- (diseno_lab + anotacion) & ggplot2::theme(legend.position = "bottom")
con_guias_locales <- (patchwork::wrap_plots(p_resumen, p_detalle,
  ncol = 1, heights = c(1, 1.6), guides = "keep") + anotacion) &
  ggplot2::theme(legend.position = "bottom")
print(con_guias_locales)
print(conjunto_lab)
```

Los dos objetos mantienen medidas y datos. Con `keep`, cada gráfico conserva
su guía; con `collect` se reúnen y se eliminan duplicados compatibles. La
posición se aplica al conjunto. Los tamaños relativos organizan espacio; no
representan proporciones de créditos ni cambian escalas de datos.

Ahora crea la incoherencia de correspondencias en una copia:

```r
paleta_incoherente <- c("2026-09-30" = "#A34E12", "2026-10-31" = "#246A86")
p_incoherente <- p_detalle + ggplot2::scale_colour_manual(
  name = "Fecha de corte", values = paleta_incoherente, labels = rotulos_fecha)
caso_incorrecto <- patchwork::wrap_plots(p_resumen, p_incoherente,
  ncol = 2, guides = "collect") & ggplot2::theme(legend.position = "bottom")
print(caso_incorrecto)
colores_correctos <- unname(paleta[as.character(detalle$corte)])
stopifnot(!identical(ggplot2::layer_data(p_incoherente, 2)$colour, colores_correctos),
          identical(ggplot2::layer_data(p_incoherente, 2)$y,
                    ggplot2::layer_data(p_detalle, 2)$y),
          identical(ggplot2::layer_data(p_detalle, 2)$colour, colores_correctos))
```

Se espera un aviso de sustitución de la escala de color al crear la copia:
añadimos otra escala para esa estética. El error de significado consiste en
que una fecha tiene colores diferentes entre vistas; los saldos siguen siendo
los mismos. La solución utiliza `p_detalle`, que conserva la paleta común,
como ya hace `conjunto_lab`. No es necesario borrar o modificar el objeto original.

```r
a <- ggplot2::layer_data(conjunto_lab[[1]], 2)
b <- ggplot2::layer_data(conjunto_lab[[2]], 2)
lineas_b <- ggplot2::layer_data(conjunto_lab[[2]], 1)
grupos_b <- split(lineas_b, lineas_b$group)
control_lab <- detalle |> dplyr::group_by(fecha_corte) |>
  dplyr::summarise(creditos = dplyr::n(), saldo_mxn = sum(as.double(saldo_mxn)), .groups = "drop")
stopifnot(length(conjunto_lab) == 2L, nrow(a) == 2L, nrow(b) == 28L,
          identical(a$y, c(29000, 31800)), length(grupos_b) == 14L,
          all(vapply(grupos_b, nrow, integer(1)) == 2L),
          all(vapply(grupos_b, function(g) length(unique(g$x)), integer(1)) == 2L),
          identical(control_lab$creditos, c(14L, 14L)),
          identical(control_lab$saldo_mxn, a$y),
          identical(huella, tools::md5sum(ruta)))
descripcion_lab <- paste("Disposición vertical, A arriba y B abajo.", descripcion_conjunto)
cat(descripcion_lab, "\n")
print(resumen |> dplyr::select(fecha_corte, creditos, saldo_mxn, aceptados_corte))
print(conjunto_lab)
```

A describe sumas de los mismos IDs; B muestra sus saldos individuales. Una
interpretación adecuada es: «El saldo común aumenta 2800 MXN entre dos cortes.
Las 28 observaciones de B corresponden a los mismos 14 IDs que alimentan A;
cada par sintético aumenta 200 MXN. Los ejes verticales tienen diferente
agregación. La base común cubre 14/18 aceptados por fecha; la figura no describe
todos los aceptados ni identifica causas». Los tramos no son observaciones diarias.

Guarda, reinicia R mediante Session > Restart R y ejecuta en Console desde la
raíz del proyecto:

```r
source("output/mi_composicion_lab.R", encoding = "UTF-8")
```

Adapta los nombres si elegiste otros. El
[script de referencia](../../../curriculum/08_visualization_r/07_compose_figures/componer_figuras.R)
puede ayudar a contrastar el recorrido. La evidencia incluye tu interpretación
y revisión visual, además de las aserciones.

</details>

## Extensión opcional — Una tercera vista o un orden diferente

Revisa la composición anidada de la lección: resumen arriba, detalle y pares
abajo. Explica la función de los paréntesis, la proporción fija de C y por qué
su diagonal es una referencia. Si decides usarla, escribe una descripción
que incluya las tres vistas; no reutilices sin cambios la descripción A/B.

Si inviertes el orden de los gráficos, revisa rótulos A/B, nota y descripción.
Una etiqueta automática sigue el orden de composición, no el significado que
le diste en un párrafo anterior. No es requisito añadir otra vista para cerrar.

## Evidencia, reflexión y salida

Conserva script, tablas conciliadas, descripción del conjunto y notas de
revisión visual. Registra evidencia real y dudas en tu bitácora personal junto a la práctica.
No hay proyecto integrador ni checkpoint activo; ejecutar la referencia no
demuestra aprendizaje por sí solo.

- ¿Por qué una faceta no resuelve automáticamente esta comparación de medidas?
- ¿Qué comparten A y B y qué debe conservar su propia escala?
- ¿Qué compruebas antes de recoger una leyenda?
- ¿Cómo detectarías que A usa 18 IDs y B solo 14, aunque la figura se dibuje?
- ¿Por qué una nota general puede perderse si se coloca solo en un conjunto anidado?
- ¿Qué cambia en la explicación si reordenas o agregas una vista?

Cierra cuando puedas reconstruir y justificar esas decisiones. Siguiente:
[08.08 — Exportación reproducible](../../../curriculum/08_visualization_r/08_reproducible_export/README.md). Volver a la [lección 08.07](../../../curriculum/08_visualization_r/07_compose_figures/README.md).
