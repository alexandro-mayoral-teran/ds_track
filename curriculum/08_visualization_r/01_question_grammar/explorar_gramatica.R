# Abrir el mismo proyecto renv de 07.10; directorio de trabajo: su raiz.
# Puede guardarse como output/mi_gramatica.R y ejecutarse por bloques en el IDE.
# No instala, exporta ni modifica los archivos de la practica.
if (!file.exists("R/funciones_cierre.R") || !file.exists(".Rprofile")) {
  stop("Abre el proyecto preparado para 07.10 y manten su raiz como directorio.")
}
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
cierre <- construir_cierre(fuente)
comprobar_cierre(fuente, cierre)
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          nrow(cierre$comunes) == 14L, nrow(cierre$sin_pareja) == 8L,
          nrow(cierre$fuera_cortes) == 0L,
          identical(cierre$datos_figura$saldo_mxn, c(29000, 31800)),
          identical(cierre$datos_figura$aceptados_corte, c(18L, 18L)))

# 1. Dos filas agregadas: una por fecha, cada una resume los mismos 14 IDs.
datos <- cierre$datos_figura |> dplyr::mutate(
  corte = factor(format(fecha_corte, "%Y-%m-%d"),
                 levels = c("2026-09-30", "2026-10-31")),
  etiqueta = format(saldo_mxn, big.mark = " ", scientific = FALSE, trim = TRUE)
)
print(datos, width = Inf)

# 2. Datos y mapeos comunes. Todavia no hay marcas que representen los saldos.
p0 <- ggplot2::ggplot(datos, ggplot2::aes(x = corte, y = saldo_mxn))
print(p0)

# 3. Las alturas ya estan calculadas: geom_col no cuenta registros.
p1 <- p0 + ggplot2::geom_col(fill = "#246A86", width = 0.6)
print(p1)

# 4. Texto que hereda x/y y agrega su mapeo local de label.
p2 <- p1 + ggplot2::geom_text(
  ggplot2::aes(label = etiqueta), vjust = -0.5, size = 4.5
)
print(p2)

# 5. Escala y contexto: son componentes, no nuevas capas de datos.
p3 <- p2 + ggplot2::scale_y_continuous(
  limits = c(0, NA), expand = ggplot2::expansion(mult = c(0, 0.12)),
  labels = function(x) format(x, big.mark = " ", scientific = FALSE, trim = TRUE)
) + ggplot2::labs(
  title = "Saldo de los mismos créditos en dos cortes",
  subtitle = "Base común: 14 IDs aceptados en ambas fechas",
  x = "Fecha de corte", y = "Saldo observado (MXN)",
  caption = paste(
    "Datos sintéticos DS Track. Base común: 14/18 aceptados por corte.",
    "Comparación descriptiva; no explica las causas del cambio.", sep = "\n"
  )
)
print(p3)

# 6. Tema: cambia elementos de presentacion, conserva tabla y mapeos.
figura <- p3 + ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(panel.grid.major.x = ggplot2::element_blank(),
                 plot.caption = ggplot2::element_text(hjust = 0))
print(figura)

# Contraste: una fila por fecha en esta tabla -> conteos 1 y 1.
conteo <- ggplot2::ggplot(datos, ggplot2::aes(x = corte)) +
  ggplot2::geom_bar() +
  ggplot2::labs(title = "Filas de la tabla resumida por corte", y = "Filas (no MXN)")
print(conteo)

# La suma de componentes crea otro objeto; no modifica p0 ni el CSV.
stopifnot(length(p0$layers) == 0L, length(p1$layers) == 1L,
          length(p2$layers) == 2L, length(figura$layers) == 2L,
          identical(datos$saldo_mxn, cierre$datos_figura$saldo_mxn),
          identical(huella, tools::md5sum(ruta)))
print(utils::packageVersion("ggplot2"))
cat("Dos barras: 29000/31800 MXN; dos etiquetas; base comun de 14 IDs.\n")
cat("Cambio: +2800 MXN; 9.66% sobre septiembre. Cobertura: 14/18 por corte.\n")
# Volver a la figura de saldo al terminar el recorrido.
print(figura)
