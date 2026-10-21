# Mismo proyecto renv de 07.10; ejecutar desde su raiz en el IDE.
# Guardar una copia propia como output/mi_facetas.R; no instala ni exporta.
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
fechas <- cierre$datos_figura$fecha_corte
niveles_segmento <- c("comercio", "consumo", "educacion", "servicios")
detalle <- cierre$resultado$aceptados |>
  dplyr::filter(fecha_corte %in% fechas) |>
  dplyr::semi_join(cierre$comunes, by = "id_credito", na_matches = "never") |>
  dplyr::select(id_credito, fecha_corte, segmento, saldo_mxn) |>
  dplyr::mutate(
    segmento = factor(segmento, levels = niveles_segmento),
    corte = factor(format(fecha_corte, "%Y-%m-%d"), levels = format(fechas, "%Y-%m-%d"))
  )
por_id <- detalle |> dplyr::distinct(id_credito, segmento)
control <- detalle |> dplyr::group_by(fecha_corte) |>
  dplyr::summarise(creditos = dplyr::n(),
    saldo_mxn = sum(as.double(saldo_mxn)), .groups = "drop")
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          nrow(detalle) == 28L, nrow(cierre$comunes) == 14L,
          !anyNA(detalle), anyDuplicated(detalle[c("id_credito", "fecha_corte")]) == 0L,
          nrow(por_id) == 14L,
          identical(control$creditos, c(14L, 14L)),
          identical(control$saldo_mxn, c(29000, 31800)))
print(control)

resumen_segmentos <- detalle |> dplyr::group_by(segmento, corte) |>
  dplyr::summarise(creditos = dplyr::n(),
    saldo_mxn = sum(as.double(saldo_mxn)), .groups = "drop") |>
  dplyr::group_by(corte) |>
  dplyr::mutate(total_creditos = sum(creditos),
    proporcion_creditos = creditos / total_creditos) |>
  dplyr::ungroup() |>
  dplyr::arrange(segmento, corte)
stopifnot(nrow(resumen_segmentos) == 8L,
          !dplyr::is_grouped_df(resumen_segmentos),
          all(resumen_segmentos$total_creditos == 14L))
print(resumen_segmentos, width = Inf)

base_segmentos <- ggplot2::ggplot(resumen_segmentos, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_col(fill = "#246A86", width = 0.6) +
  ggplot2::scale_y_continuous(limits = c(0, NA),
    expand = ggplot2::expansion(mult = c(0, 0.18))) +
  ggplot2::scale_x_discrete(labels = c("2026-09-30" = "Sep", "2026-10-31" = "Oct")) +
  ggplot2::labs(x = "Corte de 2026", y = "Saldo observado (MXN)") +
  ggplot2::theme_minimal(base_size = 12)
por_segmento <- base_segmentos +
  ggplot2::geom_text(ggplot2::aes(label = paste0("n = ", creditos)), vjust = -0.5, size = 3.5) +
  ggplot2::facet_wrap(ggplot2::vars(segmento), ncol = 2, scales = "fixed") +
  ggplot2::labs(title = "Saldo por segmento de los mismos 14 créditos",
    subtitle = "Escala compartida; n indica créditos del segmento en ese corte",
    caption = "Datos sintéticos. Cada ID conserva su segmento.\nBase común: 14/18 aceptados por corte; las sumas no son promedios.")
print(por_segmento)

segmentos_libres <- base_segmentos +
  ggplot2::geom_text(ggplot2::aes(label = paste0("n = ", creditos)), vjust = -0.5, size = 3.5) +
  ggplot2::facet_wrap(ggplot2::vars(segmento), ncol = 2, scales = "free_y") +
  ggplot2::labs(title = "Mismos saldos, rango vertical propio por segmento",
    subtitle = "Escalas verticales libres: compara valores leyendo los ejes de cada panel",
    caption = "Datos sintéticos. Cada barra conserva su base cero.\nAlturas parecidas entre paneles pueden representar importes diferentes.")
print(segmentos_libres)

cuadricula <- ggplot2::ggplot(detalle, ggplot2::aes(x = "Saldos", y = saldo_mxn)) +
  ggplot2::geom_boxplot(quantile.type = 7, coef = 1.5,
    outlier.shape = NA, width = 0.35, fill = "#D9EBF2") +
  ggplot2::geom_point(position = ggplot2::position_jitter(width = 0.07, height = 0, seed = 805),
    colour = "#246A86", size = 2) +
  ggplot2::facet_grid(rows = ggplot2::vars(segmento), cols = ggplot2::vars(corte),
    scales = "fixed") +
  ggplot2::labs(title = "Distribución de saldos por segmento y corte",
    subtitle = "Tres o cuatro créditos en cada celda; puntos conservados",
    x = NULL, y = "Saldo por crédito (MXN)",
    caption = "Datos sintéticos. Base común: 14/18 por fecha.\nJitter solo horizontal; las cajas no muestran el emparejamiento por ID.") +
  ggplot2::theme_minimal(base_size = 11)
print(cuadricula)

construccion <- ggplot2::ggplot_build(por_segmento)
paneles <- construccion$layout$layout
capa_barras <- ggplot2::layer_data(por_segmento, 1) |> tibble::as_tibble()
observado <- capa_barras |> dplyr::select(PANEL, x, y) |>
  dplyr::left_join(paneles |> dplyr::select(PANEL, segmento),
    by = "PANEL", relationship = "many-to-one") |>
  dplyr::transmute(segmento = as.character(segmento),
    corte = levels(detalle$corte)[as.integer(x)], saldo_mxn = y) |>
  dplyr::arrange(segmento, corte)
esperado <- resumen_segmentos |>
  dplyr::transmute(segmento = as.character(segmento), corte = as.character(corte), saldo_mxn) |>
  dplyr::arrange(segmento, corte)
stopifnot(nrow(paneles) == 4L, identical(observado, esperado),
          nrow(ggplot2::layer_data(segmentos_libres, 1)) == 8L,
          nrow(ggplot2::layer_data(cuadricula, 1)) == 8L,
          nrow(ggplot2::layer_data(cuadricula, 2)) == 28L)
print(paneles[c("PANEL", "segmento", "SCALE_X", "SCALE_Y")])

demo <- data.frame(
  segmento = factor(c("A", "A", "B"), levels = c("A", "B", "C")),
  corte = factor(c("Sep", "Oct", "Sep"), levels = c("Sep", "Oct")),
  saldo_mxn = c(0, 100, NA_real_), observado = TRUE
)
inventario <- expand.grid(segmento = levels(demo$segmento), corte = levels(demo$corte),
                          stringsAsFactors = FALSE) |>
  dplyr::left_join(demo, by = c("segmento", "corte"), relationship = "one-to-one") |>
  dplyr::mutate(
    segmento = factor(segmento, levels = levels(demo$segmento)),
    corte = factor(corte, levels = levels(demo$corte)),
    estado = dplyr::case_when(
      is.na(observado) ~ "Sin registro",
      is.na(saldo_mxn) ~ "Saldo NA",
      saldo_mxn == 0 ~ "Cero observado",
      .default = "Saldo observado"
    )
  )
sin_registros <- ggplot2::ggplot(demo, ggplot2::aes(x = 1, y = saldo_mxn)) +
  ggplot2::geom_point(size = 3, colour = "#246A86") +
  ggplot2::geom_text(data = inventario, ggplot2::aes(x = 1, y = 160, label = estado),
    inherit.aes = FALSE, size = 3.2) +
  ggplot2::facet_grid(rows = ggplot2::vars(segmento), cols = ggplot2::vars(corte), drop = FALSE) +
  ggplot2::scale_x_continuous(breaks = NULL) +
  ggplot2::scale_y_continuous(limits = c(0, 200)) +
  ggplot2::labs(title = "Muestra independiente: ausencias y cero",
    subtitle = "Los textos describen el inventario; solo dos saldos son conocidos",
    x = NULL, y = "Saldo didáctico (MXN)",
    caption = "Sin registro no equivale a cero. Saldo NA conserva una fila de origen.") +
  ggplot2::theme_minimal(base_size = 11)
print(inventario)
print(sin_registros)
stopifnot(nrow(demo) == 3L, nrow(inventario) == 6L,
          sum(!is.na(demo$saldo_mxn)) == 2L,
          sum(inventario$estado == "Sin registro") == 3L,
          sum(inventario$estado == "Saldo NA") == 1L,
          nrow(ggplot2::ggplot_build(sin_registros)$layout$layout) == 6L,
          identical(huella, tools::md5sum(ruta)))

cat("Facetas comprobadas; fuente intacta.\n")
