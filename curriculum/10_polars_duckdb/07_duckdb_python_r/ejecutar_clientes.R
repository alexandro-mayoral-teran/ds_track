# Desde la copia renv en RStudio/IDE, despues de restaurar y reiniciar la sesion.
source("R/clientes_1007.R", encoding = "UTF-8")
carpeta <- "output/clientes_1007_r"
archivo <- preparar_1007(carpeta)
entrega <- ejecutar_1007(archivo)
print(entrega)
stopifnot(identical(entrega$seleccion$id_credito, "003"),
          identical(entrega$seleccion$saldo_mxn, 2600L))
