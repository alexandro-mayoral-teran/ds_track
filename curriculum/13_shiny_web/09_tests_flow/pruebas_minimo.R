# Requiere library(shiny). No inicia navegador ni servidor HTTP.
entorno_minimo <- new.env(parent = globalenv())
source("minimo.R", local = entorno_minimo, encoding = "UTF-8")
testServer(entorno_minimo$dobleServer, {
  session$setInputs(numero = 3, nota = "inicio")
  stopifnot("3 debe dar 6" = identical(doble(), 6),
    "Salida inicial" = identical(output$resultado, "Doble: 6."))
  session$setInputs(numero = 7)
  stopifnot("7 debe actualizar a 14" = identical(doble(), 14),
    "Texto actualizado" = identical(output$resultado, "Doble: 14."))
  session$setInputs(nota = "cambio independiente")
  stopifnot("Nota no cambia el doble" = identical(doble(), 14),
    "Eco independiente" = identical(output$eco, "Nota: cambio independiente"))
  session$setInputs(numero = 0)
  stopifnot("Cero conocido" = identical(doble(), 0),
    "Texto de cero" = identical(output$resultado, "Doble: 0."))
})
cat("OK minimo: 3 -> 7 -> nota -> 0.\n")
