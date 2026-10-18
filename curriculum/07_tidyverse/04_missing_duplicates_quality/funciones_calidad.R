# Cargar despues de funciones_transformacion.R. source() solo define funciones.
clave_calidad <- c("id_credito", "fecha_corte")
segmentos_calidad <- c("consumo", "servicios", "comercio", "educacion")
nombres_reglas_calidad <- c(
  paste0(c("id_credito", "segmento", "fecha_corte", "saldo_mxn", "pago_mxn", "dias_atraso"), "_ausente"),
  "saldo_mxn_incompatible", "saldo_mxn_negativo",
  "pago_mxn_incompatible", "pago_mxn_negativo",
  "dias_atraso_incompatible", "dias_atraso_negativo",
  "segmento_fuera_catalogo", "pago_supera_saldo", "clave_repetida"
)

motivos_de_banderas <- function(banderas) {
  motivos <- rep("", nrow(banderas))
  for (nombre in names(banderas)) {
    mascara <- banderas[[nombre]]
    separador <- dplyr::if_else(motivos[mascara] == "", "", "; ")
    motivos[mascara] <- paste0(motivos[mascara], separador, nombre)
  }
  motivos
}

suma_observada <- function(x) {
  if (!is.numeric(x)) { stop("La suma requiere cantidades interpretadas.") }
  if (!any(!is.na(x))) { return(NA_real_) }
  sum(as.double(x), na.rm = TRUE)
}

comprobar_particion <- function(trabajo, aceptados, rechazados, banderas) {
  stopifnot(
    identical(trabajo$numero_registro, seq_len(nrow(trabajo))),
    identical(names(aceptados), names(trabajo)),
    identical(names(rechazados), names(trabajo)),
    identical(names(banderas), nombres_reglas_calidad),
    nrow(banderas) == nrow(trabajo),
    all(vapply(banderas, is.logical, logical(1))), !anyNA(banderas),
    identical(trabajo$motivos, motivos_de_banderas(banderas)),
    nrow(aceptados) + nrow(rechazados) == nrow(trabajo),
    identical(aceptados$numero_registro, trabajo$numero_registro[trabajo$motivos == ""]),
    identical(rechazados$numero_registro, trabajo$numero_registro[trabajo$motivos != ""])
  )
  juntos <- dplyr::bind_rows(aceptados, rechazados) |>
    dplyr::arrange(numero_registro)
  # Comparar todas las columnas, sin depender de atributos internos del lector CSV.
  stopifnot(identical(as.list(juntos), as.list(trabajo)),
            !anyNA(aceptados[clave_calidad]),
            !any(duplicated(aceptados[clave_calidad])))
  conocidos <- sum(!is.na(trabajo$saldo_mxn))
  stopifnot(conocidos == sum(!is.na(aceptados$saldo_mxn)) + sum(!is.na(rechazados$saldo_mxn)))
  if (conocidos > 0L) {
    # Identidad entre partes sobre una base conocida; no imputacion de importes.
    stopifnot(suma_observada(trabajo$saldo_mxn) ==
                sum(c(suma_observada(aceptados$saldo_mxn),
                      suma_observada(rechazados$saldo_mxn)), na.rm = TRUE))
  }
  invisible(TRUE)
}

evaluar_calidad <- function(fuente) {
  if (!is.data.frame(fuente) || !identical(names(fuente), columnas_conversion) ||
      !all(vapply(fuente, is.character, logical(1)))) {
    stop("Usa la fuente de seis columnas leida como texto, antes de transformar.")
  }
  trabajo <- fuente |>
    dplyr::mutate(numero_registro = seq_len(nrow(fuente))) |>
    dplyr::select(numero_registro, id_credito, segmento, fecha_corte,
                  saldo_mxn, pago_mxn, dias_atraso)
  reglas <- list()
  # Registrar ausencia en origen ANTES de convertir textos.
  for (nombre in columnas_conversion) {
    reglas[[paste0(nombre, "_ausente")]] <- is.na(fuente[[nombre]])
  }
  for (nombre in c("saldo_mxn", "pago_mxn", "dias_atraso")) {
    trabajo[[paste0(nombre, "_texto")]] <- fuente[[nombre]]
    conversion <- convertir_entero(fuente[[nombre]])
    trabajo[[nombre]] <- conversion$valor
    reglas[[paste0(nombre, "_incompatible")]] <- conversion$incompatible
    reglas[[paste0(nombre, "_negativo")]] <- trabajo[[nombre]] < 0
  }
  reglas$segmento_fuera_catalogo <- !is.na(trabajo$segmento) &
    !(trabajo$segmento %in% segmentos_calidad)
  reglas$pago_supera_saldo <- trabajo$pago_mxn > trabajo$saldo_mxn
  claves <- fuente[clave_calidad]
  clave_presente <- !is.na(fuente$id_credito) & !is.na(fuente$fecha_corte)
  reglas$clave_repetida <- clave_presente &
    (duplicated(claves) | duplicated(claves, fromLast = TRUE))
  # Solo las banderas convierten lo no confirmado en FALSE. Los datos quedan NA.
  for (nombre in names(reglas)) {
    reglas[[nombre]] <- !is.na(reglas[[nombre]]) & reglas[[nombre]]
  }
  banderas <- tibble::as_tibble(reglas)
  trabajo$motivos <- motivos_de_banderas(banderas)
  trabajo <- trabajo |>
    dplyr::mutate(saldo_despues_pago_mxn = as.double(saldo_mxn) - pago_mxn)
  aceptados <- trabajo |> dplyr::filter(motivos == "")
  rechazados <- trabajo |> dplyr::filter(motivos != "")
  comprobar_particion(trabajo, aceptados, rechazados, banderas)
  controles <- tibble::tibble(
    parte = c("entrada", "aceptados", "rechazados"),
    registros = c(nrow(trabajo), nrow(aceptados), nrow(rechazados)),
    saldos_conocidos = c(sum(!is.na(trabajo$saldo_mxn)),
                         sum(!is.na(aceptados$saldo_mxn)), sum(!is.na(rechazados$saldo_mxn))),
    saldos_sin_interpretar = registros - saldos_conocidos,
    saldo_observado_mxn = c(suma_observada(trabajo$saldo_mxn),
                            suma_observada(aceptados$saldo_mxn), suma_observada(rechazados$saldo_mxn))
  )
  list(trabajo = trabajo, aceptados = aceptados, rechazados = rechazados,
       banderas = banderas, controles = controles)
}
