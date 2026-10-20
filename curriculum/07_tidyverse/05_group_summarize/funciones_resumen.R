# Definiciones sin lecturas ni escrituras. Requiere suma_observada de 07.04.
validar_detalle_resumen <- function(detalle) {
  requeridas <- c("id_credito", "fecha_corte", "segmento", "saldo_mxn", "dias_atraso")
  if (!is.data.frame(detalle) || anyDuplicated(names(detalle)) ||
      !all(requeridas %in% names(detalle))) {
    stop("Se requiere detalle con ID, corte, segmento, saldo y atraso.")
  }
  for (nombre in c("id_credito", "fecha_corte", "segmento")) {
    if (!is.character(detalle[[nombre]])) { stop("Las claves se reciben como texto.") }
  }
  claves <- detalle[c("id_credito", "fecha_corte")]
  if (anyNA(claves) || any(!nzchar(detalle$id_credito)) ||
      any(!nzchar(detalle$fecha_corte)) || anyDuplicated(claves)) {
    stop("La clave ID/corte debe estar presente y ser unica antes de resumir.")
  }
  for (nombre in c("saldo_mxn", "dias_atraso")) {
    x <- detalle[[nombre]]
    if (!is.numeric(x) || is.object(x)) { stop("Se requieren cantidades numericas ordinarias.") }
    conocidos <- x[!is.na(x)]
    if (any(is.nan(x)) || any(!is.finite(conocidos)) ||
        any(conocidos < 0 | conocidos %% 1 != 0 | conocidos > .Machine$integer.max)) {
      stop("Las cantidades conocidas deben ser enteros finitos no negativos en rango.")
    }
  }
  invisible(TRUE)
}

resumir_grupos <- function(detalle) {
  validar_detalle_resumen(detalle)
  # El contrato analitico admite NA en segmento/cantidades; no acepta duplicados.
  # El recorrido principal pasa SOLO aceptados de 07.04, sin relajar sus reglas.
  detalle |>
    dplyr::ungroup() |>
    dplyr::group_by(fecha_corte, segmento) |>
    dplyr::summarise(
      registros = dplyr::n(),
      saldos_conocidos = sum(!is.na(saldo_mxn)),
      saldo_observado_mxn = suma_observada(saldo_mxn),
      atrasos_conocidos = sum(!is.na(dias_atraso)),
      atrasos_30_confirmados = sum(dias_atraso >= 30L, na.rm = TRUE),
      .groups = "drop"
    ) |>
    dplyr::mutate(
      cobertura_saldo_pct = saldos_conocidos / registros * 100,
      saldo_promedio_conocido_mxn = saldo_observado_mxn /
        dplyr::if_else(saldos_conocidos > 0L, as.double(saldos_conocidos), NA_real_),
      saldo_total_mxn = dplyr::if_else(saldos_conocidos == registros,
                                      saldo_observado_mxn, NA_real_),
      cobertura_atraso_pct = atrasos_conocidos / registros * 100,
      atraso_30_pct_conocidos = atrasos_30_confirmados /
        dplyr::if_else(atrasos_conocidos > 0L, as.double(atrasos_conocidos), NA_real_) * 100
    ) |>
    dplyr::arrange(fecha_corte, segmento)
}

comprobar_resumen <- function(detalle, resumen) {
  esperado <- resumir_grupos(detalle)
  # Comparar claves, columnas y tipos: compensar dos sumas no oculta un error.
  stopifnot(is.data.frame(resumen), !dplyr::is_grouped_df(resumen),
            identical(as.list(resumen), as.list(esperado)),
            sum(resumen$registros) == nrow(detalle),
            sum(resumen$saldos_conocidos) == sum(!is.na(detalle$saldo_mxn)),
            sum(resumen$atrasos_conocidos) == sum(!is.na(detalle$dias_atraso)),
            identical(suma_observada(resumen$saldo_observado_mxn),
                      suma_observada(detalle$saldo_mxn)))
  invisible(TRUE)
}
