# Desde la raiz del proyecto; define una comprobacion sin exportar ni abrir graficos.
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el lockfile de 07.10 desde R.") }
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")
verificar_entrega_cierre <- function(destino) {
  fuente <- leer_texto_segmentos("datos/cartera_texto.csv")
  comprobar_entrega(fuente, destino)
}
