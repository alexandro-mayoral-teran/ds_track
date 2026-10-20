# source() define funciones; cargar primero calidad, texto y fechas de 07.04/08/09.
construir_cierre <- function(fuente) {
  validar_fuente_texto(fuente)
  # Retener valores/tipos, sin atributos internos del lector (punteros no serializables).
  fuente <- tibble::as_tibble(lapply(fuente, identity))
  resultado <- preparar_fechas(fuente)
  comprobar_fechas(fuente, resultado)
  aceptados <- resultado$aceptados
  cortes <- as.Date(c("2026-09-30", "2026-10-31"))
  septiembre <- aceptados |> dplyr::filter(fecha_corte == cortes[1])
  octubre <- aceptados |> dplyr::filter(fecha_corte == cortes[2])
  comunes <- dplyr::inner_join(
    septiembre |> dplyr::select(id_credito, saldo_sep = saldo_mxn),
    octubre |> dplyr::select(id_credito, saldo_oct = saldo_mxn),
    by = "id_credito", relationship = "one-to-one", na_matches = "never"
  ) |> dplyr::mutate(diferencia_mxn = as.double(saldo_oct) - saldo_sep) |>
    dplyr::arrange(id_credito)
  sin_pareja <- dplyr::bind_rows(
    dplyr::anti_join(septiembre, comunes, by = "id_credito", na_matches = "never"),
    dplyr::anti_join(octubre, comunes, by = "id_credito", na_matches = "never")
  ) |> dplyr::arrange(fecha_corte, id_credito)
  # Observaciones aceptadas fuera de los dos cortes se conservan, no se grafican.
  fuera_cortes <- aceptados |> dplyr::filter(!fecha_corte %in% cortes)
  datos_figura <- tibble::tibble(
    fecha_corte = cortes,
    creditos = rep(nrow(comunes), 2L),
    saldo_mxn = c(suma_observada(comunes$saldo_sep), suma_observada(comunes$saldo_oct)),
    aceptados_corte = c(nrow(septiembre), nrow(octubre))
  )
  stopifnot(nrow(aceptados) == 2L * nrow(comunes) + nrow(sin_pareja) + nrow(fuera_cortes))
  if (nrow(comunes) > 0L) {
    stopifnot(sum(comunes$diferencia_mxn) == diff(datos_figura$saldo_mxn))
  }
  list(fuente = fuente, resultado = resultado,
       resumen_cortes = resumir_cortes_fechas(aceptados), comunes = comunes,
       sin_pareja = sin_pareja, fuera_cortes = fuera_cortes, datos_figura = datos_figura)
}

comprobar_cierre <- function(fuente, cierre) {
  # Reconstruir todas las columnas detecta cambios compensados que conservan sumas.
  esperado <- construir_cierre(fuente)
  stopifnot(identical(cierre, esperado))
  invisible(TRUE)
}

crear_figura_cierre <- function(cierre) {
  comprobar_cierre(cierre$fuente, cierre)
  datos <- cierre$datos_figura
  if (any(datos$creditos == 0L)) {
    stop("No hay IDs comunes: conserva las tablas y explica la ausencia; no dibujes ceros.")
  }
  datos <- datos |> dplyr::mutate(
    corte = factor(format(fecha_corte, "%Y-%m-%d"), levels = c("2026-09-30", "2026-10-31")),
    etiqueta = format(saldo_mxn, big.mark = " ", scientific = FALSE, trim = TRUE)
  )
  ggplot2::ggplot(datos, ggplot2::aes(x = corte, y = saldo_mxn)) +
    ggplot2::geom_col(fill = "#246A86", width = 0.6) +
    ggplot2::geom_text(ggplot2::aes(label = etiqueta), vjust = -0.5, size = 4.5) +
    ggplot2::scale_y_continuous(
      limits = c(0, NA), expand = ggplot2::expansion(mult = c(0, 0.12)),
      labels = function(x) format(x, big.mark = " ", scientific = FALSE, trim = TRUE)
    ) +
    ggplot2::labs(
      title = "Saldo de los mismos créditos en dos cortes",
      subtitle = sprintf("Base común: %d IDs aceptados en ambas fechas", datos$creditos[1]),
      x = "Fecha de corte", y = "Saldo observado (MXN)",
      caption = sprintf("Datos sintéticos DS Track. Base común: %d/%d y %d/%d aceptados.\nComparación descriptiva; no explica las causas del cambio.",
                        datos$creditos[1], datos$aceptados_corte[1],
                        datos$creditos[2], datos$aceptados_corte[2])
    ) +
    ggplot2::theme_minimal(base_size = 12) +
    ggplot2::theme(panel.grid.major.x = ggplot2::element_blank(),
                   plot.caption = ggplot2::element_text(hjust = 0))
}

tablas_entrega <- function(cierre) {
  list(aceptados = cierre$resultado$aceptados, rechazados = cierre$resultado$rechazados,
       resumen_cortes = cierre$resumen_cortes, base_comun = cierre$comunes,
       sin_pareja = cierre$sin_pareja, fuera_cortes = cierre$fuera_cortes,
       datos_figura = cierre$datos_figura)
}

validar_ruta_cierre <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una ruta de carpeta como texto.")
  }
  invisible(TRUE)
}

exportar_cierre <- function(cierre, destino) {
  validar_ruta_cierre(destino)
  comprobar_cierre(cierre$fuente, cierre)
  figura <- crear_figura_cierre(cierre) # Validar antes de crear carpetas.
  if (file.exists(destino) || !dir.exists(dirname(destino))) {
    stop("El destino debe ser nuevo y su carpeta madre debe existir; conserva entregas anteriores.")
  }
  if (!dir.create(destino)) { stop("No se pudo crear el destino.") }
  # Si falla una escritura, queda una entrega parcial: revisar, no sobrescribir.
  saveRDS(cierre, file.path(destino, "analisis.rds"), version = 3)
  tablas <- tablas_entrega(cierre)
  for (nombre in names(tablas)) {
    readr::write_csv(tablas[[nombre]], file.path(destino, paste0(nombre, ".csv")), na = "")
  }
  ggplot2::ggsave(file.path(destino, "saldo_comun.png"), plot = figura,
                  device = grDevices::png, width = 9, height = 6, units = "in", dpi = 144, bg = "white")
  writeLines(capture.output(utils::sessionInfo()), file.path(destino, "sesion.txt"))
  invisible(destino)
}

comprobar_entrega <- function(fuente, destino) {
  validar_ruta_cierre(destino)
  cierre <- readRDS(file.path(destino, "analisis.rds"))
  comprobar_cierre(fuente, cierre)
  tablas <- tablas_entrega(cierre)
  for (nombre in names(tablas)) {
    leida <- readr::read_csv(file.path(destino, paste0(nombre, ".csv")),
      col_types = readr::cols(.default = readr::col_character()), na = character(),
      trim_ws = FALSE, show_col_types = FALSE, progress = FALSE, lazy = FALSE)
    readr::stop_for_problems(leida)
    stopifnot(identical(names(leida), names(tablas[[nombre]])),
              nrow(leida) == nrow(tablas[[nombre]]))
    for (columna in names(leida)) {
      x <- tablas[[nombre]][[columna]]
      if (is.numeric(x) && !inherits(x, "Date")) {
        numero <- readr::parse_double(leida[[columna]], na = "")
        readr::stop_for_problems(numero)
        stopifnot(identical(numero, as.double(x)))
      } else {
        texto <- if (inherits(x, "Date")) format(x, "%Y-%m-%d") else as.character(x)
        texto[is.na(texto)] <- ""
        stopifnot(identical(leida[[columna]], texto))
      }
    }
  }
  ruta_png <- file.path(destino, "saldo_comun.png")
  cabecera <- readBin(ruta_png, what = "raw", n = 24L)
  stopifnot(length(cabecera) == 24L,
            identical(cabecera[1:8], as.raw(c(137,80,78,71,13,10,26,10))),
            file.info(ruta_png)$size > 24,
            file.exists(file.path(destino, "sesion.txt")))
  cat("Tablas reconstruidas y CSV conciliados; PNG presente. Revisa su aspecto visual.\n")
  invisible(TRUE)
}
