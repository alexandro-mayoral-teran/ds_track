# Lab 08.06 — Etiquetas, temas y accesibilidad

## Propósito y entradas

Mejorar la comunicación de una figura conservando los datos y justificando sus
decisiones. Lee la [lección 08.06](../../../curriculum/08_visualization_r/06_labels_themes_accessibility/README.md)
y conserva tu script `output/mi_comunicacion.R`. Usa el proyecto renv de 07.10,
con sus funciones, CSV, reglas y lockfile. No necesitas instalar paquetes ni
exportar otra entrega.

En RStudio o tu IDE crea `output/mi_comunicacion_lab.R`, sin sobrescribir
trabajo. Ejecuta por bloques en Console de R desde la raíz del proyecto.
Guarda y comprueba la reconstrucción tras reiniciar, además de trabajar por partes.

## Actividad esencial

1. Antes de ejecutar, revisa estas frases: «Resultados», «La cartera mejoró
   9.66%» y «La estrategia causó el aumento». Explica qué falta o qué afirman
   sin evidencia. Escribe un título y subtítulo propios que comuniquen saldo,
   población comparable y fechas, sin afirmar causas ni representar toda la cartera.
2. Reconstruye la lección. Comprueba 29000/31800 MXN, +2800 y aproximadamente
   +9.66% sobre septiembre. Distingue ese porcentaje de la cobertura 14/18.
3. Crea una variante con dos barras y **una sola etiqueta de importe, en octubre**,
   usando `geom_label` y una tabla local. Conserva las dos filas para las barras;
   no filtres el gráfico completo. Deja disponibles los dos importes en la tabla
   y en la descripción, aunque no estén ambos escritos sobre las barras.
4. Aplica `theme_bw` y después tus ajustes locales. Mantén texto legible,
   unidades, base cero y fuente/cobertura. Explica qué argumentos modifican
   textos del tema y cuáles modifican la etiqueta de la capa. Justifica el orden.
5. Compara `con_senales` y `sin_color`. Comprueba los mismos valores y formas
   por fecha, pero dos colores en la primera y uno en la segunda. Explica cómo
   identificar fechas sin depender del color. No basta decir que una paleta
   «es accesible» porque te resulta agradable.
6. Redacta una alternativa textual para tu variante y recupera el texto con
   `get_alt_text`. Reúne la tabla de lectura. Explica qué harías con ese texto
   si insertaras la imagen en otro documento y por qué un PNG no basta para
   asegurar que un lector de pantalla lo reciba.
7. Inspecciona título, tamaños, leyenda, recortes y contraste al tamaño previsto.
   Si hay texto que no cabe, ajusta distribución o redacción antes de reducirlo
   hasta volverlo ilegible. Registra una corrección concreta o una decisión
   comprobada; no inventes haber probado un dispositivo que no utilizaste.
8. Guarda, reinicia R y ejecuta el script completo. Conserva controles y escribe
   un párrafo con hallazgo, población, fechas, cobertura y límite interpretativo.

## Resultados y comprobación

| Evidencia | Resultado esperado |
| --- | --- |
| Base | Dos sumas 29000/31800 MXN; mismos 14 IDs, cobertura 14/18 por corte |
| Cambio | +2800 MXN; 100 × 2800 / 29000 ≈ 9.66% |
| Variante | Dos barras y un recuadro de importe en octubre; alturas intactas |
| Tema | Tema completo antes de ajustes locales; unidades y fuente legibles |
| Señales | Misma fecha/forma/posición; dos colores frente a uno |
| Alternativa | Población, medida, fechas, valores y límites coherentes con la figura |
| Conservación | CSV intacto, reglas/lockfile sin cambios y ejecución desde sesión nueva |

Una figura que cambia solo de tema debe conservar los valores representados.
La alternativa textual también debe seguir siendo fiel si cambias la selección
de etiquetas. Revisar el texto no equivale a comprobar su integración con un
lector de pantalla: esa comprobación corresponde al destino donde se utilice.

## Pistas

<details>
<summary>Ver pistas después de formular tu propuesta</summary>

La tabla local de `geom_label` puede seleccionar octubre sin tocar `datos`.
Con `inherit.aes = FALSE`, declara x/y/label. Mantén espacio superior para el
recuadro mediante expansión del eje, sin aumentar el saldo. `vjust` desplaza
el dibujo del texto respecto de su anclaje; no es una nueva observación.

Aplica primero `theme_bw(...)` y después `tema_lectura` o tus ajustes propios.
El tamaño de la etiqueta se establece en su geometría, con unidad explícita;
`axis.text` solo cambia textos del eje. Las formas deben corresponder a las
mismas fechas con y sin color. Mantén descripción y tabla junto a la imagen.

</details>

## Solución razonada

<details>
<summary>Ver una solución después de intentar la actividad</summary>

Empieza `output/mi_comunicacion_lab.R` con la reconstrucción de la lección:

```r
source("output/mi_comunicacion.R", encoding = "UTF-8")
solo_octubre <- datos |> dplyr::filter(fecha_corte == max(fecha_corte))
descripcion_variante <- paste(
  "La etiqueta directa de importe aparece solo en octubre; ambos saldos están en la tabla.",
  descripcion
)
variante <- base +
  ggplot2::geom_label(data = solo_octubre,
    ggplot2::aes(x = corte, y = saldo_mxn, label = etiqueta), inherit.aes = FALSE,
    vjust = -0.3, colour = "#222222", fill = "white", size = 11, size.unit = "pt") +
  ggplot2::scale_x_discrete(labels = etiquetas_fecha) +
  ggplot2::scale_y_continuous(limits = c(0, NA), labels = formato_mxn,
    expand = ggplot2::expansion(mult = c(0, 0.25))) +
  ggplot2::labs(title = "El saldo común pasa de 29 000 a 31 800 MXN",
    subtitle = "Los mismos 14 IDs; 30 de septiembre y 31 de octubre de 2026",
    x = "Fecha de corte", y = "Saldo observado (MXN)",
    caption = nota_fuente, alt = descripcion_variante) +
  ggplot2::theme_bw(base_size = 12, base_family = "sans") + tema_lectura
print(variante)
```

El título de ejemplo incluye ambos importes y se ha contrastado con esta
muestra. Si adaptas los datos, actualiza esa redacción explícita y compruébala
contra la tabla. La descripción añade que solo octubre tiene etiqueta directa,
pero conserva los valores de ambos cortes y su alcance.

```r
barras_variante <- ggplot2::layer_data(variante, 1)
recuadro <- ggplot2::layer_data(variante, 2)
stopifnot(nrow(barras_variante) == 2L, nrow(recuadro) == 1L,
          identical(barras_variante$y, c(29000, 31800)),
          all(barras_variante$ymin == 0),
          as.integer(recuadro$x) == 2L, recuadro$y == 31800,
          identical(recuadro$label, solo_octubre$etiqueta),
          nrow(datos) == 2L, diferencia == 2800,
          abs(variacion_pct - 100 * 2800 / 29000) < 1e-12,
          identical(ggplot2::get_alt_text(variante), descripcion_variante))
color <- ggplot2::layer_data(con_senales, 2)
un_color <- ggplot2::layer_data(sin_color, 2)
stopifnot(identical(color[c("x", "y", "shape")], un_color[c("x", "y", "shape")]),
          length(unique(color$colour)) == 2L,
          length(unique(un_color$colour)) == 1L,
          length(unique(un_color$shape)) == 2L,
          identical(huella, tools::md5sum(ruta)))
cat(ggplot2::get_alt_text(variante), "\n")
print(tabla_lectura)
print(con_senales)
print(sin_color)
```

El círculo y el triángulo mantienen fechas distintas con el mismo color; las
posiciones y los rótulos refuerzan su lectura. No evaluamos todas las formas
de visión ni certificamos un documento completo. La leyenda, el tamaño real,
las tablas y la alternativa también forman parte de la revisión.

Un párrafo válido sería: «En los mismos 14 IDs aceptados en ambas fechas, el
saldo observado pasa de 29000 a 31800 MXN entre el 30 de septiembre y el 31 de
octubre de 2026: +2800 MXN, aproximadamente +9.66% respecto a septiembre. La
base común cubre 14 de los 18 aceptados por corte. Son datos sintéticos y una
comparación descriptiva; no permite identificar causas ni describir todos los
aceptados». El 9.66% no es una tasa de mejora ni el porcentaje de cobertura.

Guarda y reinicia R mediante Session > Restart R. Ejecuta en Console desde la
raíz del proyecto:

```r
source("output/mi_comunicacion_lab.R", encoding = "UTF-8")
```

Adapta los nombres si usaste otros archivos. Puedes contrastar la lección con
el [script de referencia](../../../curriculum/08_visualization_r/06_labels_themes_accessibility/comunicar_resultados.R).
La evidencia incluye tu explicación y revisión visual, además de las aserciones.

</details>

## Extensión opcional — Orden del tema y anotaciones

Compara `rotulado + tema_lectura + theme_bw()` con
`rotulado + theme_bw() + tema_lectura`. Explica qué ajustes del tema completo
reemplazan los anteriores y comprueba que los saldos siguen iguales.

En otra copia, añade una anotación en una posición exterior al rango y observa
si el eje se amplía. Conserva el gráfico principal: no presentes la posición
de una nota como una medición nueva ni uses recortes para ocultar datos.
Para facetas, aplica la regla de claves de 08.05 antes de anotar un panel específico.

## Evidencia, reflexión y salida

Conserva script, tabla, alternativa textual, interpretación y notas de revisión
visual. Registra evidencia real y dudas según [PROGRESS.md](../../../PROGRESS.md).
No hay proyecto integrador ni checkpoint activo; desarrollar o ejecutar el
material no acredita aprendizaje por sí solo.

- ¿Qué diferencia hay entre cambiar `labs(y = ...)` y convertir una unidad?
- ¿Por qué `element_text` no modifica el texto de una geometría?
- ¿Cómo justificas que la anotación no es un tercer dato de saldo?
- ¿Qué sigue permitiendo interpretar la figura cuando quitas la diferencia de color?
- ¿Qué información necesita alguien que no puede ver la imagen?
- ¿Qué revisarías al trasladar esa imagen y su descripción a otro documento?

Cierra cuando puedas reconstruir y justificar esas decisiones. Siguiente:
[08.07 — Componer figuras](../../../curriculum/08_visualization_r/07_compose_figures/README.md),
ya disponible. Volver a la [lección 08.06](../../../curriculum/08_visualization_r/06_labels_themes_accessibility/README.md).
