# Definiciones: source() no lee ni escribe datos.
columnas_cartera <- c("id_credito", "segmento", "fecha_corte", "saldo_mxn", "dias_atraso")

tipos_cartera <- function() {
  readr::cols(
    id_credito = readr::col_character(),
    segmento = readr::col_character(),
    fecha_corte = readr::col_character(),
    saldo_mxn = readr::col_double(),
    dias_atraso = readr::col_integer()
  )
}

leer_cartera <- function(ruta) {
  # Declarar tipos no valida el dominio; solo controla la interpretacion.
  tabla <- readr::read_csv(
    ruta, col_types = tipos_cartera(),
    locale = readr::locale(encoding = "UTF-8", decimal_mark = "."),
    na = c("", "NA"), trim_ws = FALSE, name_repair = "check_unique",
    skip_empty_rows = FALSE, lazy = FALSE, show_col_types = FALSE,
    progress = FALSE
  )
  # No devolver una tabla parcialmente interpretada para analizarla por accidente.
  readr::stop_for_problems(tabla)
  if (!identical(names(tabla), columnas_cartera)) {
    stop("Esquema distinto: comprueba nombres y orden de las cinco columnas.")
  }
  tabla
}

comprobar_muestra <- function(tabla) {
  # Estos controles pertenecen a esta muestra conocida, no a cualquier cartera.
  stopifnot(
    inherits(tabla, "tbl_df"), inherits(tabla, "data.frame"),
    identical(dim(tabla), c(6L, 5L)),
    identical(names(tabla), columnas_cartera),
    identical(vapply(tabla, typeof, character(1)),
              c(id_credito = "character", segmento = "character",
                fecha_corte = "character", saldo_mxn = "double", dias_atraso = "integer")),
    identical(tabla[["id_credito"]], sprintf("%03d", 1:6)),
    identical(tabla[["segmento"]],
              c("consumo", "comercio, local", "servicios", "consumo", "educación", "servicios")),
    identical(tabla[["fecha_corte"]], rep("2026-09-30", 6)),
    identical(tabla[["saldo_mxn"]], c(1000, 1500, 750, 0, 2250, 500)),
    identical(tabla[["dias_atraso"]], c(0L, 10L, 45L, 0L, NA_integer_, 5L)),
    sum(tabla[["saldo_mxn"]]) == 6000,
    sum(!is.na(tabla[["saldo_mxn"]])) == 6L,
    sum(is.na(tabla[["dias_atraso"]])) == 1L
  )
  invisible(TRUE)
}
