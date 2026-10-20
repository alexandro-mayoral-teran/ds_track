# Definiciones sin ejecucion. Cargar despues de funciones_resumen.R (07.05).
validar_catalogo <- function(catalogo) {
  if (!is.data.frame(catalogo) ||
      !identical(names(catalogo), c("segmento", "etiqueta_segmento")) ||
      !all(vapply(catalogo, is.character, logical(1)))) {
    stop("El catalogo requiere segmento y etiqueta_segmento como texto, en ese orden.")
  }
  if (anyNA(catalogo$segmento) || any(!nzchar(catalogo$segmento)) ||
      anyDuplicated(catalogo$segmento)) {
    stop("La clave del catalogo debe ser completa y unica, incluso si no se usa.")
  }
  invisible(TRUE)
}

leer_catalogo <- function(ruta) {
  catalogo <- readr::read_csv(
    ruta, col_types = readr::cols(.default = readr::col_character()),
    na = "", locale = readr::locale(encoding = "UTF-8"), trim_ws = FALSE,
    name_repair = "check_unique", skip_empty_rows = FALSE, lazy = FALSE,
    show_col_types = FALSE, progress = FALSE
  )
  readr::stop_for_problems(catalogo)
  validar_catalogo(catalogo)
  catalogo
}

unir_catalogo <- function(detalle, catalogo) {
  validar_detalle_resumen(detalle)
  validar_catalogo(catalogo)
  if (!"numero_registro" %in% names(detalle) ||
      !is.integer(detalle$numero_registro) || anyNA(detalle$numero_registro) ||
      any(detalle$numero_registro < 1L) || anyDuplicated(detalle$numero_registro)) {
    stop("Conserva numero_registro entero, positivo y unico para rastrear cada fila.")
  }
  if (any(c("etiqueta_segmento", "en_catalogo") %in% names(detalle))) {
    stop("El detalle ya tiene columnas reservadas para esta union.")
  }
  # Declarar el estado de entrada evita heredar agrupaciones de otro analisis.
  detalle <- dplyr::ungroup(detalle)
  catalogo <- dplyr::ungroup(catalogo)
  marcado <- catalogo |> dplyr::mutate(en_catalogo = TRUE)
  ampliado <- detalle |>
    dplyr::left_join(marcado, by = "segmento", na_matches = "never",
                     relationship = "many-to-one") |>
    # Solo la marca de existencia se convierte a FALSE; la etiqueta queda NA.
    dplyr::mutate(en_catalogo = dplyr::coalesce(en_catalogo, FALSE))
  con_catalogo <- dplyr::semi_join(detalle, catalogo, by = "segmento", na_matches = "never")
  sin_catalogo <- dplyr::anti_join(detalle, catalogo, by = "segmento", na_matches = "never")
  catalogo_sin_uso <- dplyr::anti_join(catalogo, detalle, by = "segmento", na_matches = "never")
  partes <- list(detalle, con_catalogo, sin_catalogo)
  controles <- tibble::tibble(
    parte = c("detalle", "con_catalogo", "sin_catalogo"),
    registros = vapply(partes, nrow, integer(1)),
    saldos_conocidos = vapply(partes, function(x) sum(!is.na(x$saldo_mxn)), integer(1)),
    saldo_observado_mxn = vapply(partes, function(x) suma_observada(x$saldo_mxn), double(1))
  )
  list(ampliado = ampliado, con_catalogo = con_catalogo, sin_catalogo = sin_catalogo,
       catalogo_sin_uso = catalogo_sin_uso, controles = controles)
}

comprobar_union <- function(detalle, catalogo, resultado) {
  esperado <- unir_catalogo(detalle, catalogo)
  stopifnot(is.list(resultado), identical(names(resultado), names(esperado)))
  for (nombre in names(esperado)) {
    stopifnot(is.data.frame(resultado[[nombre]]),
              !dplyr::is_grouped_df(resultado[[nombre]]),
              identical(as.list(resultado[[nombre]]), as.list(esperado[[nombre]])))
  }
  ampliado <- resultado$ampliado
  stopifnot(nrow(ampliado) == nrow(detalle),
            identical(as.list(ampliado[names(detalle)]), as.list(dplyr::ungroup(detalle))),
            !anyNA(ampliado$en_catalogo))
  juntos <- dplyr::bind_rows(resultado$con_catalogo, resultado$sin_catalogo)
  juntos <- juntos[match(detalle$numero_registro, juntos$numero_registro), ]
  stopifnot(identical(as.list(juntos), as.list(dplyr::ungroup(detalle))))
  invisible(TRUE)
}
