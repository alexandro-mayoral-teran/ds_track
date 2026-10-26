# Ejecutar desde la raiz de DS Track; no renderiza ni comprueba cifras.
distribuir_dashboard <- function(html, destino) {
  nota <- "curriculum/11_reporting_quarto/08_dashboard_distribution/LEEME_entrega.md"
  if (!file.exists(html) || dir.exists(html) || !grepl("\\.html$", html, ignore.case = TRUE) || !file.exists(nota)) {
    stop("Se requiere HTML existente y ejecutar desde la raiz de DS Track")
  }
  if (file.exists(destino)) stop("Destino ocupado: conservar y elegir otro")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear destino")
  copia <- file.path(destino, "dashboard.html")
  if (!file.copy(html, copia) || !file.copy(nota, file.path(destino, "LEEME.md"))) {
    stop("Copia parcial: conservar carpeta e investigar")
  }
  if (!identical(unname(tools::md5sum(html)), unname(tools::md5sum(copia)))) stop("Copia distinta")
  cat("Copia preparada. Abrir dashboard.html en el destino y revisar.\n")
  cat("La comparacion MD5 no verifica datos ni acredita autenticidad.\n")
  invisible(destino)
}
