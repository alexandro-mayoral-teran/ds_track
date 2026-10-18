# Ejecutar desde la raiz del repositorio en una sesion nueva.
source("curriculum/06_r_foundations/06_functions_control/funciones_ventas.R",
       encoding = "UTF-8")

# Datos propios de esta seccion: preservan la muestra de 06.04 y 06.05.
ventas <- data.frame(
  id_venta = c("V001", "V002", "V003", "V004", "V005", "V006"),
  unidades = c(4L, 2L, 0L, 3L, NA, 2L),
  precio_mxn = c(75, 120, 50, 40, 100, NA),
  stringsAsFactors = FALSE
)
ventas$importe_mxn <- calcular_importes(ventas$unidades, ventas$precio_mxn)
resultado <- resumir_importes(ventas$importe_mxn)
cat("Tabla y resumen original; total completo desconocido:\n")
print(ventas)
print(resultado)

# La repeticion recorre umbrales; el calculo por venta sigue vectorizado.
umbrales <- c(100, 200, 300)
conteos <- integer(length(umbrales))
for (i in seq_along(umbrales)) {
  resumen_i <- resumir_importes(ventas$importe_mxn, umbral = umbrales[i])
  conteos[i] <- resumen_i$n_cumplen
}
cat("Cumplimientos confirmados por umbral; siempre dos pendientes:\n")
print(data.frame(umbral = umbrales, n_cumplen = conteos)) # 3 2 1

cat("Tabla vacia, todos faltantes y cero observado:\n")
print(resumir_importes(numeric(0)))
print(resumir_importes(c(NA_real_, NA_real_)))
print(resumir_importes(0))

# Variante: una unidad confirmada de V005, sin alterar el original.
confirmadas <- ventas
fila <- confirmadas$id_venta == "V005"
confirmadas$unidades[fila] <- 1L
confirmadas$importe_mxn <- calcular_importes(confirmadas$unidades, confirmadas$precio_mxn)
cat("Variante con cinco importes conocidos y suma observada 760:\n")
print(resumir_importes(confirmadas$importe_mxn))

# Extension explicada: una falla esperada genera estado explicito, nunca cero.
intento <- tryCatch(
  {
    valor <- calcular_importes(c(2, 3), 100)
    list(ok = TRUE, valor = valor, mensaje = NULL)
  },
  error = function(e) {
    list(ok = FALSE, valor = NULL, mensaje = conditionMessage(e))
  }
)
cat("Intento con longitudes incompatibles, rechazado sin resultado de exito:\n")
print(intento)
cat("Version y sesion:\n")
print(R.version.string)
print(utils::sessionInfo())
