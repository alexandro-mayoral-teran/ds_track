# Definiciones sin ejecucion; requiere suma_observada de 07.04.
cortes_formas <- c("2026-09-30", "2026-10-31")
columnas_ancho <- c("id_credito", paste0("saldo_", cortes_formas))

validar_claves_formas <- function(claves) {
  if (!is.data.frame(claves) || !identical(names(claves), c("id_credito", "corte")) ||
      !all(vapply(claves, is.character, logical(1))) || anyNA(claves) ||
      any(!nzchar(claves$id_credito)) || any(!claves$corte %in% cortes_formas) ||
      anyDuplicated(claves)) {
    stop("Se requieren claves ID/corte completas y unicas, con los dos cortes admitidos.")
  }
  invisible(TRUE)
}

validar_proyeccion <- function(largo) {
  if (!is.data.frame(largo) ||
      !identical(names(largo), c("id_credito", "corte", "saldo_mxn"))) {
    stop("La proyeccion requiere exactamente ID, corte y saldo_mxn, en ese orden.")
  }
  validar_claves_formas(largo[c("id_credito", "corte")])
  x <- largo$saldo_mxn
  if (!is.integer(x) || is.object(x) || any(x < 0L, na.rm = TRUE)) {
    stop("El saldo debe ser integer no negativo o NA; no convertir truncando.")
  }
  invisible(TRUE)
}

leer_fuente_formas <- function(ruta) {
  fuente <- readr::read_csv(ruta, col_types = readr::cols(
    id_credito = readr::col_character(), segmento = readr::col_character(),
    fecha_corte = readr::col_character(), saldo_mxn = readr::col_integer(),
    dias_atraso = readr::col_integer()), na = "", trim_ws = FALSE,
    locale = readr::locale(encoding = "UTF-8"), name_repair = "check_unique",
    skip_empty_rows = FALSE, lazy = FALSE, show_col_types = FALSE, progress = FALSE)
  readr::stop_for_problems(fuente)
  if (!identical(names(fuente), c("id_credito", "segmento", "fecha_corte", "saldo_mxn", "dias_atraso")) ||
      any(fuente$dias_atraso < 0L, na.rm = TRUE)) { stop("Revisa esquema y atraso de la fuente.") }
  proyeccion <- fuente |> dplyr::select(id_credito, corte = fecha_corte, saldo_mxn)
  validar_proyeccion(proyeccion)
  fuente
}

largo_a_ancho <- function(largo) {
  validar_proyeccion(largo)
  ancho <- largo |>
    dplyr::ungroup() |>
    tidyr::pivot_wider(id_cols = id_credito, names_from = corte,
                       values_from = saldo_mxn, names_prefix = "saldo_", names_sort = TRUE)
  # Esquema estable incluso si un corte no tiene registros o el detalle esta vacio.
  for (nombre in columnas_ancho[-1]) {
    if (!nombre %in% names(ancho)) { ancho[[nombre]] <- rep(NA_integer_, nrow(ancho)) }
  }
  ancho |> dplyr::select(dplyr::all_of(columnas_ancho)) |> dplyr::arrange(id_credito)
}

ancho_a_rejilla <- function(ancho) {
  if (!is.data.frame(ancho) || !identical(names(ancho), columnas_ancho) ||
      !is.character(ancho$id_credito) || anyNA(ancho$id_credito) ||
      any(!nzchar(ancho$id_credito)) || anyDuplicated(ancho$id_credito)) {
    stop("El ancho requiere ID unico y las dos columnas de saldo acordadas.")
  }
  rejilla <- ancho |>
    dplyr::ungroup() |>
    tidyr::pivot_longer(cols = dplyr::all_of(columnas_ancho[-1]),
                        names_to = "corte", names_prefix = "saldo_", values_to = "saldo_mxn",
                        values_ptypes = list(saldo_mxn = integer()), values_drop_na = FALSE) |>
    dplyr::arrange(id_credito, corte)
  # Comprobar tambien los tipos originales; no admitir una conversion double -> integer.
  if (!all(vapply(ancho[-1], function(x) is.integer(x) && !is.object(x), logical(1)))) {
    stop("Las celdas deben conservar integer ordinario.")
  }
  validar_proyeccion(rejilla)
  rejilla
}

recuperar_saldos <- function(ancho, claves_presentes) {
  validar_claves_formas(claves_presentes)
  rejilla <- ancho_a_rejilla(ancho)
  if (nrow(dplyr::anti_join(claves_presentes, rejilla,
                            by = c("id_credito", "corte"), na_matches = "never")) > 0L) {
    stop("El inventario contiene claves que no existen en la rejilla.")
  }
  dplyr::semi_join(rejilla, claves_presentes, by = c("id_credito", "corte"),
                   na_matches = "never")
}

control_por_corte <- function(largo) {
  validar_proyeccion(largo)
  largo |> dplyr::ungroup() |> dplyr::group_by(corte) |>
    dplyr::summarise(registros = dplyr::n(), conocidos = sum(!is.na(saldo_mxn)),
                     saldo_observado_mxn = suma_observada(saldo_mxn), .groups = "drop") |>
    dplyr::arrange(corte)
}

comprobar_formas <- function(largo, ancho, claves_presentes, recuperado) {
  validar_proyeccion(largo)
  validar_proyeccion(recuperado)
  esperado <- largo |> dplyr::ungroup() |> dplyr::arrange(id_credito, corte)
  claves_esperadas <- esperado |> dplyr::select(id_credito, corte)
  validar_claves_formas(claves_presentes)
  claves_ordenadas <- claves_presentes |> dplyr::ungroup() |> dplyr::arrange(id_credito, corte)
  stopifnot(identical(as.list(claves_ordenadas), as.list(claves_esperadas)),
            identical(as.list(ancho), as.list(largo_a_ancho(largo))),
            identical(as.list(recuperado), as.list(esperado)),
            identical(as.list(recuperado), as.list(recuperar_saldos(ancho, claves_presentes))),
            identical(as.list(control_por_corte(largo)), as.list(control_por_corte(recuperado))))
  invisible(TRUE)
}
