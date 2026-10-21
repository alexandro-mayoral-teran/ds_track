# Mismo proyecto renv de 07.10; ejecutar desde su raiz en el IDE.
# Guardar una copia propia como output/mi_escalas.R; no instala ni exporta.
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
resumen <- cierre$datos_figura |> dplyr::mutate(
  corte = factor(format(fecha_corte, "%Y-%m-%d"),
                 levels = c("2026-09-30", "2026-10-31"))
)
pares <- cierre$comunes
septiembre <- pares |> dplyr::select(id_credito, saldo_mxn = saldo_sep)
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          nrow(pares) == 14L, nrow(cierre$sin_pareja) == 8L,
          identical(resumen$saldo_mxn, c(29000, 31800)),
          sum(as.double(pares$saldo_sep)) == 29000,
          sum(as.double(pares$saldo_oct)) == 31800,
          !anyNA(septiembre))
print(resumen)

formato_mxn <- function(x) {
  format(x, big.mark = " ", scientific = FALSE, trim = TRUE)
}
base_barras <- ggplot2::ggplot(resumen, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_col(fill = "#246A86", width = 0.6) +
  ggplot2::labs(title = "Saldo de los mismos 14 créditos",
    x = "Fecha de corte", y = "Saldo observado (MXN)",
    caption = "Datos sintéticos. Base común: 14/18 aceptados por corte.") +
  ggplot2::theme_minimal(base_size = 12)
barras <- base_barras + ggplot2::scale_y_continuous(
  limits = c(0, NA), breaks = seq(0, 40000, by = 10000),
  labels = formato_mxn, expand = ggplot2::expansion(mult = c(0, 0.08))
)
print(barras)

etiquetas_miles <- base_barras + ggplot2::scale_y_continuous(
  limits = c(0, NA), breaks = c(0, 10000, 20000, 30000),
  labels = function(x) formato_mxn(x / 1000)
) + ggplot2::labs(y = "Saldo observado (miles de MXN)")
tabla_miles <- resumen |> dplyr::mutate(saldo_miles_mxn = saldo_mxn / 1000)
valores_miles <- ggplot2::ggplot(tabla_miles,
    ggplot2::aes(corte, saldo_miles_mxn)) +
  ggplot2::geom_col(fill = "#246A86", width = 0.6) +
  ggplot2::labs(x = "Fecha de corte", y = "Saldo observado (miles de MXN)")
print(etiquetas_miles)
print(valores_miles)
stopifnot(identical(ggplot2::layer_data(etiquetas_miles, 1)$y, c(29000, 31800)),
          identical(ggplot2::layer_data(valores_miles, 1)$y, c(29, 31.8)))

barras_rotuladas <- barras + ggplot2::scale_x_discrete(
  breaks = levels(resumen$corte),
  labels = c("2026-09-30" = "Septiembre 2026", "2026-10-31" = "Octubre 2026")
)
print(barras_rotuladas)

base_caja <- ggplot2::ggplot(septiembre, ggplot2::aes(x = "Septiembre", y = saldo_mxn)) +
  ggplot2::geom_boxplot(quantile.type = 7, coef = 1.5, width = 0.4,
    fill = "#D9EBF2", colour = "#183C4A") +
  ggplot2::labs(x = NULL, y = "Saldo por crédito (MXN)") +
  ggplot2::theme_minimal(base_size = 12)
caja_completa <- base_caja + ggplot2::labs(title = "Caja de los 14 saldos de septiembre")
caja_limite <- base_caja +
  ggplot2::scale_y_continuous(limits = c(1000, 2500)) +
  ggplot2::labs(title = "Límite de escala: cambia el cálculo",
    subtitle = "La estadística recibe 10 saldos; cuatro quedan fuera",
    caption = "Demostración de censura; no es la distribución completa de los 14 IDs.")
caja_zoom <- base_caja +
  ggplot2::coord_cartesian(ylim = c(1000, 2500),
    expand = c(bottom = FALSE, top = FALSE)) +
  ggplot2::labs(title = "Zoom: conserva el cálculo de 14 saldos",
    subtitle = "Vista parcial: Q3 y bigote superior quedan fuera del panel",
    caption = "Datos sintéticos. La vista no muestra toda la caja; no implica ausencia de saldos mayores.")
print(caja_completa)
print(caja_limite)
print(caja_zoom)

dentro <- septiembre$saldo_mxn >= 1000 & septiembre$saldo_mxn <= 2500
cuartiles <- function(x) {
  stats::quantile(x, c(0.25, 0.5, 0.75), type = 7, names = FALSE)
}
q_completos <- cuartiles(septiembre$saldo_mxn)
q_limitados <- cuartiles(septiembre$saldo_mxn[dentro])
completa <- ggplot2::layer_data(caja_completa, 1)
limitada <- ggplot2::layer_data(caja_limite, 1)
zoom <- ggplot2::layer_data(caja_zoom, 1)
columnas_caja <- c("ymin", "lower", "middle", "upper", "ymax")
stopifnot(sum(dentro) == 10L, sum(!dentro) == 4L,
          identical(q_completos, c(1475, 2050, 2575)),
          identical(q_limitados, c(1325, 1750, 2075)),
          identical(unname(unlist(completa[c("lower", "middle", "upper")])), q_completos),
          identical(unname(unlist(limitada[c("lower", "middle", "upper")])), q_limitados),
          identical(completa[columnas_caja], zoom[columnas_caja]))
print(rbind(completa = q_completos, con_limite = q_limitados))

temporal <- ggplot2::ggplot(resumen,
    ggplot2::aes(fecha_corte, saldo_mxn, group = 1)) +
  ggplot2::geom_line(colour = "#246A86", linewidth = 0.8) +
  ggplot2::geom_point(colour = "#246A86", size = 3) +
  ggplot2::scale_x_date(breaks = resumen$fecha_corte, date_labels = "%d/%m/%Y") +
  ggplot2::labs(title = "Dos cortes observados de los mismos 14 IDs",
    x = "Fecha de corte", y = "Saldo observado (MXN)",
    caption = "Datos sintéticos. El segmento conecta dos fechas; no son mediciones diarias.") +
  ggplot2::theme_minimal(base_size = 12)
print(temporal)
stopifnot(inherits(resumen$fecha_corte, "Date"),
          identical(ggplot2::layer_data(temporal, 1)$x, as.numeric(resumen$fecha_corte)))

calendario <- data.frame(
  fecha = as.Date(c("2026-09-30", "2026-10-01", "2026-10-31")),
  valor = c(100, 200, 150)
)
calendario$categoria <- factor(format(calendario$fecha, "%Y-%m-%d"),
                               levels = format(calendario$fecha, "%Y-%m-%d"))
espacio_fecha <- ggplot2::ggplot(calendario, ggplot2::aes(fecha, valor)) +
  ggplot2::geom_point() + ggplot2::scale_x_date(date_labels = "%d/%m")
espacio_categoria <- ggplot2::ggplot(calendario, ggplot2::aes(categoria, valor)) +
  ggplot2::geom_point()
print(espacio_fecha)
print(espacio_categoria)
stopifnot(identical(diff(ggplot2::layer_data(espacio_fecha, 1)$x), c(1, 30)),
          all(diff(as.numeric(ggplot2::layer_data(espacio_categoria, 1)$x)) == 1))

stopifnot(all(septiembre$saldo_mxn > 0))
puntos_lineales <- ggplot2::ggplot(septiembre,
    ggplot2::aes(x = "Septiembre", y = saldo_mxn)) +
  ggplot2::geom_point(colour = "#246A86", size = 2.5) +
  ggplot2::labs(x = NULL, y = "Saldo por crédito (MXN)")
puntos_log <- puntos_lineales +
  ggplot2::scale_y_log10(breaks = c(1000, 1500, 2000, 3000), labels = formato_mxn) +
  ggplot2::labs(title = "Saldos positivos: eje logarítmico base 10",
    subtitle = "Marcas rotuladas en MXN; las distancias representan razones",
    y = "Saldo por crédito (MXN; escala log10)")
print(puntos_lineales)
print(puntos_log)
stopifnot(isTRUE(all.equal(ggplot2::layer_data(puntos_log, 1)$y,
                          log10(septiembre$saldo_mxn))))

comparacion <- ggplot2::ggplot(pares, ggplot2::aes(saldo_sep, saldo_oct)) +
  ggplot2::geom_abline(intercept = 0, slope = 1, linetype = "dashed", colour = "#68747A") +
  ggplot2::geom_point(colour = "#246A86", size = 3) +
  ggplot2::scale_x_continuous(breaks = seq(0, 3600, by = 600)) +
  ggplot2::scale_y_continuous(breaks = seq(0, 3600, by = 600)) +
  ggplot2::coord_fixed(ratio = 1, xlim = c(0, 3600), ylim = c(0, 3600), expand = FALSE) +
  ggplot2::labs(title = "Comparar los saldos del mismo crédito",
    subtitle = "14 pares; referencia discontinua: octubre igual a septiembre",
    x = "Saldo septiembre (MXN)", y = "Saldo octubre (MXN)",
    caption = "Datos sintéticos. Base común: 14/18 por corte.\nCada par aumenta 200 MXN; la alineación construida no demuestra causas.") +
  ggplot2::theme_minimal(base_size = 12)
print(comparacion)
stopifnot(nrow(ggplot2::layer_data(comparacion, 2)) == 14L,
          all(pares$saldo_oct - pares$saldo_sep == 200L),
          identical(huella, tools::md5sum(ruta)))

cat("Escalas y coordenadas comprobadas; fuente intacta.\n")
