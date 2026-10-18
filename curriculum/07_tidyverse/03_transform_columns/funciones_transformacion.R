# Definiciones: cargar con source() no lee datos ni modifica la biblioteca.
columnas_conversion <- c("id_credito", "segmento", "fecha_corte",
                         "saldo_mxn", "pago_mxn", "dias_atraso")

leer_texto_conversion <- function(ruta) {
  tabla <- readr::read_csv(
    ruta, col_types = readr::cols(.default = readr::col_character()),
    na = "", locale = readr::locale(encoding = "UTF-8"), trim_ws = FALSE,
    name_repair = "check_unique", skip_empty_rows = FALSE, lazy = FALSE,
    show_col_types = FALSE, progress = FALSE
  )
  readr::stop_for_problems(tabla)
  if (!identical(names(tabla), columnas_conversion)) {
    stop("Se esperan las seis columnas del diccionario, en su orden.")
  }
  tabla
}

convertir_entero <- function(texto) {
  if (!is.character(texto)) { stop("La conversion recibe una columna de texto.") }
  numero <- readr::parse_double(texto, na = "", trim_ws = FALSE,
                                locale = readr::locale(decimal_mark = "."))
  # Las advertencias de parseo se conservan; tambien devolvemos su detalle.
  problemas <- readr::problems(numero)
  ausente <- is.na(texto) | texto == ""
  apto <- is.finite(numero) & numero %% 1 == 0 &
    numero >= -.Machine$integer.max & numero <= .Machine$integer.max
  valor <- rep(NA_integer_, length(texto))
  valor[apto] <- as.integer(numero[apto])
  list(valor = valor, incompatible = !ausente & !apto, problemas = problemas)
}

transformar_columnas <- function(tabla) {
  if (!is.data.frame(tabla) || !identical(names(tabla), columnas_conversion) ||
      !all(vapply(tabla, is.character, logical(1)))) {
    stop("Se requiere la tabla de seis columnas leida como texto.")
  }
  resultado <- tabla
  # Tres nombres de columnas; no se recorre cada fila.
  for (nombre in c("saldo_mxn", "pago_mxn", "dias_atraso")) {
    resultado[[paste0(nombre, "_texto")]] <- tabla[[nombre]]
    conversion <- convertir_entero(tabla[[nombre]])
    resultado[[nombre]] <- conversion$valor
    resultado[[paste0(nombre, "_incompatible")]] <- conversion$incompatible
  }
  resultado |>
    dplyr::mutate(
      # double para la resta: evita desbordar el tipo integer al operar.
      saldo_despues_pago_mxn = as.double(saldo_mxn) - pago_mxn,
      porcentaje_pago = pago_mxn /
        dplyr::if_else(saldo_mxn > 0, as.double(saldo_mxn), NA_real_) * 100,
      estado_atraso = dplyr::case_when(
        is.na(dias_atraso) ~ "sin dato evaluable",
        dias_atraso >= 30L ~ "30 dias o mas",
        .default = "menos de 30 dias"
      )
    )
}
