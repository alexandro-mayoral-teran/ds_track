# En la raiz del proyecto de practica: bloques en el IDE o source() completo.
if (!file.exists("R/funciones_transformacion.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.03.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Comprueba el entorno de 07.02.") }
source("R/funciones_transformacion.R", encoding = "UTF-8")
ruta <- "datos/cartera_conversion.csv"
huella <- tools::md5sum(ruta)
entrada <- leer_texto_conversion(ruta)
original <- entrada
resultado <- transformar_columnas(entrada)

# Auditar conversiones sin eliminar filas ni perder los textos de origen.
for (nombre in c("saldo_mxn", "pago_mxn", "dias_atraso")) {
  cat(nombre, ": ausentes =", sum(is.na(entrada[[nombre]])),
      "; incompatibles =", sum(resultado[[paste0(nombre, "_incompatible")]]), "\n")
}
base_resta <- resultado |> dplyr::filter(!is.na(saldo_despues_pago_mxn))
stopifnot(
  identical(dim(resultado), c(40L, 15L)),
  identical(resultado$id_credito, sprintf("%03d", 1:40)),
  identical(resultado$id_credito[resultado$saldo_mxn_incompatible], "014"),
  identical(resultado$id_credito[resultado$pago_mxn_incompatible], "009"),
  identical(resultado$id_credito[resultado$dias_atraso_incompatible], c("023", "038")),
  nrow(base_resta) == 36L,
  sum(base_resta$saldo_mxn) == 217750,
  sum(base_resta$pago_mxn) == 6600,
  sum(base_resta$saldo_despues_pago_mxn) == 211150,
  sum(base_resta$saldo_mxn) - sum(base_resta$pago_mxn) ==
    sum(base_resta$saldo_despues_pago_mxn),
  sum(!is.na(resultado$porcentaje_pago)) == 35L,
  all(is.finite(resultado$porcentaje_pago[!is.na(resultado$porcentaje_pago)])),
  sum(resultado$estado_atraso == "30 dias o mas") == 21L,
  sum(resultado$estado_atraso == "menos de 30 dias") == 16L,
  sum(resultado$estado_atraso == "sin dato evaluable") == 3L,
  identical(entrada, original), identical(huella, tools::md5sum(ruta))
)
print(resultado |>
        dplyr::select(id_credito, saldo_despues_pago_mxn, porcentaje_pago, estado_atraso) |>
        head(3), width = Inf)
print(resultado |>
        dplyr::filter(id_credito %in% c("005", "009", "014", "018", "023", "028", "033", "038")),
      n = 8, width = Inf)
cat("40 filas conservadas; 36 restas evaluables, 35 porcentajes evaluables.\n")
cat("En las mismas 36 filas: 217750 - 6600 = 211150 MXN.\n")
print(R.version.string)
print(utils::packageVersion("dplyr"))
# Las advertencias por error/pendiente/no_dato son esperadas y no se ocultan.
# No exporta, no imputa cero y no decide aceptacion/rechazo de registros.
