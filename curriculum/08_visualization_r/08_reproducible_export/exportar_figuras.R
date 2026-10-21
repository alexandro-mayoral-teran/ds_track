# Desde la raiz del proyecto renv de 07.10/08.07. source() no exporta.
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")

preparar_visual <- function() {
  fuente <- leer_texto_segmentos("datos/cartera_texto.csv")
  cierre <- construir_cierre(fuente)
  comprobar_cierre(fuente, cierre)
  stopifnot(nrow(cierre$comunes) == 14L,
            identical(cierre$datos_figura$saldo_mxn, c(29000, 31800)),
            identical(cierre$datos_figura$aceptados_corte, c(18L, 18L)))
  figura <- crear_figura_cierre(cierre)
  descripcion <- paste(
    "Datos sintéticos DS Track. Saldo observado de los mismos 14 IDs aceptados.",
    "30 sep 2026: 29 000 MXN; 31 oct 2026: 31 800 MXN. Diferencia: +2 800 MXN.",
    "Cobertura: 14/18 aceptados por fecha; cuatro sin pareja por corte.",
    "Dos barras desde cero. Comparación descriptiva, sin identificación de causas."
  )
  list(cierre = cierre, figura = figura, descripcion = descripcion)
}

validar_configuracion_visual <- function(configuracion) {
  columnas <- c("ancho_in", "alto_in", "dpi", "vectoriales", "fuente_md5")
  stopifnot(is.data.frame(configuracion), identical(names(configuracion), columnas),
            nrow(configuracion) == 1L, !anyNA(configuracion),
            is.logical(configuracion$vectoriales), is.character(configuracion$fuente_md5))
  for (n in c("ancho_in", "alto_in", "dpi")) {
    stopifnot(is.numeric(configuracion[[n]]), is.finite(configuracion[[n]]), configuracion[[n]] > 0)
  }
  # Mantener limitsize de ggsave y un limite didactico de resolucion.
  stopifnot(configuracion$ancho_in < 50, configuracion$alto_in < 50,
            configuracion$dpi <= 600, configuracion$dpi %% 1 == 0,
            configuracion$ancho_in * configuracion$dpi >= 1,
            configuracion$alto_in * configuracion$dpi >= 1)
  invisible(TRUE)
}

archivos_visuales <- function(vectoriales) {
  c("datos_figura.csv", "base_comun.csv", "configuracion.csv", "descripcion.txt",
    "sesion.txt", "saldo_comun.png", if (vectoriales) c("saldo_comun.svg", "saldo_comun.pdf"))
}

guardar_png_visual <- function(figura, ruta, ancho = 9, alto = 6, dpi = 144) {
  if (file.exists(ruta)) { stop("El archivo ya existe; elige otro nombre.") }
  ggplot2::ggsave(ruta, plot = figura, device = grDevices::png,
    width = ancho, height = alto, units = "in", dpi = dpi,
    bg = "white", limitsize = TRUE)
}

exportar_visual <- function(destino, ancho = 9, alto = 6, dpi = 144, vectoriales = FALSE) {
  validar_ruta_cierre(destino)
  ruta <- "datos/cartera_texto.csv"
  huella <- unname(tools::md5sum(ruta))
  configuracion <- tibble::tibble(ancho_in = ancho, alto_in = alto, dpi = dpi,
                                 vectoriales = vectoriales, fuente_md5 = huella)
  validar_configuracion_visual(configuracion)
  if (vectoriales && !isTRUE(capabilities("cairo"))) {
    stop("SVG/PDF de esta ampliacion requieren Cairo; el PNG esencial puede hacerse sin ellos.")
  }
  if (file.exists(destino) || !dir.exists(dirname(destino))) {
    stop("El destino debe ser una carpeta nueva y su carpeta madre debe existir.")
  }
  preparado <- preparar_visual() # Reconstruir antes de crear la carpeta.
  figura <- preparado$figura
  if (!dir.create(destino)) { stop("No se pudo crear el destino.") }
  # Si una escritura falla queda una entrega parcial: revisarla, no reemplazarla.
  readr::write_csv(preparado$cierre$datos_figura, file.path(destino, "datos_figura.csv"))
  readr::write_csv(preparado$cierre$comunes, file.path(destino, "base_comun.csv"))
  readr::write_csv(configuracion, file.path(destino, "configuracion.csv"))
  writeLines(preparado$descripcion, file.path(destino, "descripcion.txt"), useBytes = TRUE)
  writeLines(capture.output(utils::sessionInfo()), file.path(destino, "sesion.txt"))
  guardar_png_visual(figura, file.path(destino, "saldo_comun.png"), ancho, alto, dpi)
  if (vectoriales) {
    # Dispositivos incluidos en R: no depende de svglite ni de paquetes nuevos.
    ggplot2::ggsave(file.path(destino, "saldo_comun.svg"), plot = figura,
      device = grDevices::svg, width = ancho, height = alto, units = "in", bg = "white")
    ggplot2::ggsave(file.path(destino, "saldo_comun.pdf"), plot = figura,
      device = grDevices::cairo_pdf, width = ancho, height = alto, units = "in", bg = "white")
  }
  archivos <- archivos_visuales(vectoriales)
  manifiesto <- tibble::tibble(archivo = archivos,
    md5 = unname(tools::md5sum(file.path(destino, archivos))))
  readr::write_csv(manifiesto, file.path(destino, "manifiesto.csv"))
  stopifnot(identical(huella, unname(tools::md5sum(ruta))))
  verificar_exportacion(destino)
  invisible(destino)
}

leer_csv_visual <- function(ruta) {
  x <- readr::read_csv(ruta, col_types = readr::cols(.default = readr::col_character()),
    na = character(), trim_ws = FALSE, name_repair = "check_unique", lazy = FALSE,
    show_col_types = FALSE, progress = FALSE)
  readr::stop_for_problems(x)
  x
}

dimensiones_png <- function(ruta) {
  conexion <- file(ruta, "rb")
  on.exit(close(conexion))
  cabecera <- readBin(conexion, "raw", n = 16L)
  stopifnot(length(cabecera) == 16L,
    identical(cabecera[1:8], as.raw(c(137, 80, 78, 71, 13, 10, 26, 10))),
    identical(rawToChar(cabecera[13:16]), "IHDR"))
  dimensiones <- readBin(conexion, integer(), n = 2L, size = 4L, endian = "big")
  stopifnot(length(dimensiones) == 2L, all(dimensiones > 0L))
  setNames(dimensiones, c("ancho_px", "alto_px"))
}

verificar_exportacion <- function(destino) {
  validar_ruta_cierre(destino)
  configuracion <- readr::read_csv(file.path(destino, "configuracion.csv"),
    col_types = readr::cols(ancho_in = readr::col_double(), alto_in = readr::col_double(),
      dpi = readr::col_double(), vectoriales = readr::col_logical(), fuente_md5 = readr::col_character()),
    name_repair = "check_unique", lazy = FALSE, show_col_types = FALSE, progress = FALSE)
  readr::stop_for_problems(configuracion)
  validar_configuracion_visual(configuracion)
  stopifnot(identical(configuracion$fuente_md5, unname(tools::md5sum("datos/cartera_texto.csv"))))
  archivos <- archivos_visuales(configuracion$vectoriales)
  manifiesto <- leer_csv_visual(file.path(destino, "manifiesto.csv"))
  stopifnot(identical(names(manifiesto), c("archivo", "md5")),
    identical(manifiesto$archivo, archivos),
    identical(manifiesto$md5, unname(tools::md5sum(file.path(destino, archivos)))))
  preparado <- preparar_visual()
  for (nombre in c("datos_figura", "base_comun")) {
    esperado <- if (nombre == "datos_figura") preparado$cierre$datos_figura else preparado$cierre$comunes
    esperado <- lapply(esperado, as.character)
    # Comparar columnas; no punteros/metadatos internos del lector readr.
    observado <- lapply(leer_csv_visual(file.path(destino, paste0(nombre, ".csv"))), identity)
    stopifnot(identical(observado, esperado))
  }
  stopifnot(identical(readLines(file.path(destino, "descripcion.txt"), encoding = "UTF-8"),
                      preparado$descripcion))
  medidas <- dimensiones_png(file.path(destino, "saldo_comun.png"))
  esperado_px <- floor(c(configuracion$ancho_in, configuracion$alto_in) * configuracion$dpi)
  stopifnot(identical(unname(medidas), as.integer(esperado_px)))
  if (configuracion$vectoriales) {
    stopifnot(any(grepl("<svg", readLines(file.path(destino, "saldo_comun.svg"), warn = FALSE))),
      identical(rawToChar(readBin(file.path(destino, "saldo_comun.pdf"), "raw", n = 5L)), "%PDF-"))
  }
  print(medidas)
  cat("Fuente, tablas, configuracion, huellas y dimensiones comprobadas. Revisa la legibilidad final.\n")
  invisible(medidas)
}
