# En el proyecto R preparado: abrir, reiniciar R y ejecutar el script completo.
source("R/intercambio_1008.R", encoding = "UTF-8")
x <- ejecutar_1008_r()
print(x)
stopifnot(identical(x$seleccion$id_credito, "003"),
          identical(x$seleccion$saldo_mxn, 2600L),
          identical(x$resumen$saldo_mxn, c(4500, 4600)))
