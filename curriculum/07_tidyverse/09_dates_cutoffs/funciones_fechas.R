# source() define funciones; requiere funciones_texto.R y funciones_calidad.R.
limpiar_texto_fecha <- function(texto) {
  if (!is.character(texto) || is.object(texto)) { stop("Se requiere texto ordinario, no fechas ni factores.") }
  dplyr::na_if(stringr::str_trim(texto), "")
}

interpretar_fecha_iso <- function(texto) {
  limpio <- limpiar_texto_fecha(texto)
  forma <- !is.na(limpio) & stringr::str_detect(limpio, "^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
  # Contrato didactico acotado: anos 1900 a 2100, ambos incluidos.
  anio_texto <- substr(limpio, 1L, 4L)
  en_rango <- forma & anio_texto >= "1900" & anio_texto <= "2100"
  fecha <- as.Date(rep(NA_character_, length(limpio)))
  if (any(en_rango)) {
    # No ocultar advertencias de calendario invalido. ymd solo recibe forma/rango aptos.
    fecha[en_rango] <- lubridate::ymd(limpio[en_rango], locale = "C", quiet = FALSE)
  }
  coincide <- !is.na(fecha) & format(fecha, "%Y-%m-%d") == limpio
  fecha[!coincide] <- as.Date(NA_character_)
  list(texto = limpio, fecha = fecha, ausente = is.na(limpio),
       invalida = !is.na(limpio) & is.na(fecha))
}

preparar_fechas <- function(fuente) {
  validar_fuente_texto(fuente)
  corte <- interpretar_fecha_iso(fuente$fecha_corte)
  alta <- interpretar_fecha_iso(fuente$fecha_alta)
  trabajo <- fuente |>
    dplyr::ungroup() |>
    dplyr::mutate(numero_registro = seq_len(nrow(fuente)),
                   id_credito_original = id_credito, segmento_original = segmento,
                   fecha_corte_original = fecha_corte, fecha_alta_original = fecha_alta) |>
    dplyr::select(numero_registro, dplyr::all_of(columnas_texto),
                   id_credito_original, segmento_original, fecha_corte_original, fecha_alta_original) |>
    dplyr::mutate(id_credito = limpiar_texto_fecha(id_credito),
                   segmento = normalizar_segmento(segmento)$normalizado,
                   fecha_corte = corte$fecha, fecha_alta = alta$fecha)
  clave <- trabajo[c("id_credito", "fecha_corte")]
  completa <- !is.na(trabajo$id_credito) & !is.na(trabajo$fecha_corte)
  reglas <- list(
    id_ausente = is.na(trabajo$id_credito),
    id_formato = !is.na(trabajo$id_credito) & !stringr::str_detect(trabajo$id_credito, "^[0-9]{3}$"),
    segmento_ausente = is.na(trabajo$segmento),
    segmento_fuera_catalogo = !is.na(trabajo$segmento) & !trabajo$segmento %in% niveles_segmento,
    fecha_corte_ausente = corte$ausente,
    fecha_corte_invalida = corte$invalida,
    fecha_alta_ausente = alta$ausente,
    fecha_alta_invalida = alta$invalida,
    alta_posterior_corte = trabajo$fecha_alta > trabajo$fecha_corte,
    clave_repetida = completa & (duplicated(clave) | duplicated(clave, fromLast = TRUE))
  )
  for (nombre in names(reglas)) { reglas[[nombre]] <- dplyr::coalesce(reglas[[nombre]], FALSE) }
  banderas <- tibble::as_tibble(reglas)
  trabajo$motivos <- motivos_de_banderas(banderas)
  trabajo <- trabajo |>
    dplyr::mutate(
      dias_desde_alta = as.integer(difftime(fecha_corte, fecha_alta, units = "days")),
      mes_corte = as.integer(lubridate::month(fecha_corte)),
      anio_corte = as.integer(lubridate::year(fecha_corte)),
      inicio_mes = as.Date(lubridate::floor_date(fecha_corte, unit = "month"))
    )
  aceptados <- trabajo |> dplyr::filter(motivos == "")
  rechazados <- trabajo |> dplyr::filter(motivos != "")
  partes <- list(trabajo, aceptados, rechazados)
  controles <- tibble::tibble(
    parte = c("entrada", "aceptados", "rechazados"),
    registros = vapply(partes, nrow, integer(1)),
    saldo_observado_mxn = vapply(partes, function(x) suma_observada(x$saldo_mxn), double(1))
  )
  list(trabajo = trabajo, aceptados = aceptados, rechazados = rechazados,
       banderas = banderas, controles = controles)
}

validar_fecha_limite <- function(x) {
  if (!identical(class(x), "Date") || length(x) != 1L || is.na(x) ||
      !is.finite(unclass(x)) || unclass(x) %% 1 != 0) {
    stop("Cada limite debe ser una fecha Date escalar y valida, no texto ni un instante.")
  }
  invisible(TRUE)
}

seleccionar_periodo <- function(aceptados, inicio, fin) {
  validar_fecha_limite(inicio)
  validar_fecha_limite(fin)
  if (inicio >= fin) { stop("Inicio debe ser anterior al fin exclusivo.") }
  if (!is.data.frame(aceptados) || !identical(class(aceptados$fecha_corte), "Date") ||
      anyNA(aceptados$fecha_corte)) {
    stop("Selecciona sobre una tabla con fechas interpretadas presentes; conserva pendientes aparte.")
  }
  aceptados |> dplyr::ungroup() |> dplyr::filter(fecha_corte >= inicio, fecha_corte < fin)
}

resumir_cortes_fechas <- function(aceptados) {
  if (!is.data.frame(aceptados) ||
      !all(c("fecha_corte", "saldo_mxn", "dias_desde_alta") %in% names(aceptados)) ||
      !identical(class(aceptados$fecha_corte), "Date") || anyNA(aceptados$fecha_corte)) {
    stop("Usa los aceptados con fechas interpretadas y diferencia en dias.")
  }
  aceptados |> dplyr::ungroup() |> dplyr::group_by(fecha_corte) |>
    dplyr::summarise(registros = dplyr::n(),
                     saldo_observado_mxn = suma_observada(saldo_mxn),
                     dias_conocidos = sum(!is.na(dias_desde_alta)),
                     dias_promedio = if (any(!is.na(dias_desde_alta))) mean(dias_desde_alta, na.rm = TRUE) else NA_real_,
                     .groups = "drop") |>
    dplyr::arrange(fecha_corte)
}

comprobar_fechas <- function(fuente, resultado) {
  esperado <- preparar_fechas(fuente)
  stopifnot(is.list(resultado), identical(names(resultado), names(esperado)))
  for (nombre in names(esperado)) {
    stopifnot(is.data.frame(resultado[[nombre]]),
              !dplyr::is_grouped_df(resultado[[nombre]]),
              identical(as.list(resultado[[nombre]]), as.list(esperado[[nombre]])))
  }
  w <- resultado$trabajo
  for (nombre in columnas_texto[-5]) {
    stopifnot(identical(w[[paste0(nombre, "_original")]], fuente[[nombre]]))
  }
  stopifnot(identical(w$saldo_mxn, fuente$saldo_mxn),
            identical(class(w$fecha_corte), "Date"), identical(class(w$fecha_alta), "Date"),
            !anyNA(resultado$banderas),
            !anyNA(resultado$aceptados[c("id_credito", "fecha_corte")]),
            !anyDuplicated(resultado$aceptados[c("id_credito", "fecha_corte")]))
  juntos <- dplyr::bind_rows(resultado$aceptados, resultado$rechazados) |> dplyr::arrange(numero_registro)
  stopifnot(identical(as.list(juntos), as.list(w)))
  invisible(TRUE)
}
