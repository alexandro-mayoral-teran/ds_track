# source() solo define funciones. Requiere suma_observada de 07.04.
columnas_texto <- c("id_credito", "segmento", "fecha_corte", "fecha_alta", "saldo_mxn")
niveles_segmento <- c("consumo", "servicios", "comercio", "educacion")

validar_fuente_texto <- function(fuente) {
  if (!is.data.frame(fuente) || !identical(names(fuente), columnas_texto) ||
      !all(vapply(fuente[columnas_texto[-5]], is.character, logical(1))) ||
      !is.integer(fuente$saldo_mxn) || is.object(fuente$saldo_mxn) ||
      anyNA(fuente$saldo_mxn) || any(fuente$saldo_mxn < 0L)) {
    stop("Se requieren cuatro textos y saldo integer presente no negativo, con el esquema declarado.")
  }
  invisible(TRUE)
}

leer_texto_segmentos <- function(ruta) {
  fuente <- readr::read_csv(ruta, col_types = readr::cols(
    id_credito = readr::col_character(), segmento = readr::col_character(),
    fecha_corte = readr::col_character(), fecha_alta = readr::col_character(),
    saldo_mxn = readr::col_integer()), na = "", trim_ws = FALSE,
    locale = readr::locale(encoding = "UTF-8"), name_repair = "check_unique",
    skip_empty_rows = FALSE, lazy = FALSE, show_col_types = FALSE, progress = FALSE)
  readr::stop_for_problems(fuente)
  validar_fuente_texto(fuente)
  fuente
}

normalizar_segmento <- function(texto) {
  if (!is.character(texto) || is.object(texto)) { stop("Conserva el segmento como texto ordinario.") }
  limpio <- stringr::str_trim(texto)
  limpio <- dplyr::na_if(limpio, "")
  normalizado <- stringr::str_to_lower(limpio, locale = "es")
  # Equivalencia de valor completo; no quitar acentos ni espacios indiscriminadamente.
  normalizado <- dplyr::if_else(normalizado == "educación", "educacion", normalizado)
  list(limpio = limpio, normalizado = normalizado)
}

preparar_segmentos <- function(fuente) {
  validar_fuente_texto(fuente)
  conversion <- normalizar_segmento(fuente$segmento)
  trabajo <- fuente |>
    dplyr::ungroup() |>
    dplyr::mutate(
      numero_registro = seq_len(nrow(fuente)),
      segmento_limpio = conversion$limpio,
      segmento_normalizado = conversion$normalizado,
      estado_segmento = dplyr::case_when(
        is.na(segmento_normalizado) ~ "ausente",
        segmento_normalizado %in% niveles_segmento ~ "reconocido",
        .default = "fuera_catalogo"
      ),
      texto_modificado = (is.na(segmento) != is.na(segmento_normalizado)) |
        (!is.na(segmento) & !is.na(segmento_normalizado) & segmento != segmento_normalizado)
    )
  reconocidos <- trabajo |>
    dplyr::filter(estado_segmento == "reconocido") |>
    dplyr::mutate(segmento_factor = forcats::fct(segmento_normalizado, levels = niveles_segmento))
  pendientes <- trabajo |> dplyr::filter(estado_segmento != "reconocido")
  resumen <- reconocidos |>
    dplyr::group_by(segmento_factor, .drop = FALSE) |>
    dplyr::summarise(registros = dplyr::n(),
                     saldo_observado_mxn = suma_observada(saldo_mxn), .groups = "drop")
  partes <- list(trabajo, reconocidos, pendientes)
  controles <- tibble::tibble(
    parte = c("entrada", "reconocidos", "pendientes"),
    registros = vapply(partes, nrow, integer(1)),
    saldo_observado_mxn = vapply(partes, function(x) suma_observada(x$saldo_mxn), double(1))
  )
  list(trabajo = trabajo, reconocidos = reconocidos, pendientes = pendientes,
       resumen = resumen, controles = controles)
}

comprobar_segmentos <- function(fuente, resultado) {
  esperado <- preparar_segmentos(fuente)
  stopifnot(is.list(resultado), identical(names(resultado), names(esperado)))
  for (nombre in names(esperado)) {
    stopifnot(is.data.frame(resultado[[nombre]]),
              !dplyr::is_grouped_df(resultado[[nombre]]),
              identical(as.list(resultado[[nombre]]), as.list(esperado[[nombre]])))
  }
  trabajo <- resultado$trabajo
  reconocidos <- resultado$reconocidos
  # Comparar las columnas, sin equiparar metadatos internos del lector y tibble.
  stopifnot(all(vapply(columnas_texto, function(n) identical(trabajo[[n]], fuente[[n]]), logical(1))),
            !anyNA(trabajo$texto_modificado),
            identical(levels(reconocidos$segmento_factor), niveles_segmento),
            !is.ordered(reconocidos$segmento_factor),
            identical(as.character(reconocidos$segmento_factor), reconocidos$segmento_normalizado))
  juntos <- dplyr::bind_rows(dplyr::select(reconocidos, -segmento_factor), resultado$pendientes) |>
    dplyr::arrange(numero_registro)
  stopifnot(identical(as.list(juntos), as.list(trabajo)))
  invisible(TRUE)
}
