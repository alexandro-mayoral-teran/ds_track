# Desde la raiz del proyecto de practica, en una sesion nueva del IDE.
# source() define el recorrido; la llamada explicita crea la entrega.
ejecutar_practica_parquet <- function(destino = "output/09_04_r") {
  e <- new.env(parent = globalenv())
  sys.source("R/contrato_0902.R", envir = e)
  sys.source("R/intercambio_parquet.R", envir = e)
  resultado <- e$crear_entrega_r(destino)
  stopifnot(identical(resultado$registros, c(14L, 14L)),
    identical(resultado$saldo_mxn, c(29000, 31800)))
  print(resultado)
  invisible(resultado)
}
