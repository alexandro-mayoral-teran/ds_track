# Revisar las fuentes antes de ejecutar; restaurar la raiz en otra carpeta.
reconstruir_producto <- function(raiz = ".", quarto = Sys.which("quarto")) {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  e <- new.env(parent = globalenv())
  for (p in c("ejecutar.R", "trazar.R", "integracion.R", "pruebas.R")) source(file.path(raiz, p), local = e, encoding = "UTF-8")
  e$verificar_entorno(raiz)
  if (!nzchar(quarto)) quarto <- "C:/Program Files/RStudio/resources/app/bin/quarto/bin/quarto.exe"
  if (!file.exists(quarto)) stop("Quarto existente requerido; indicar su ruta.")
  casos <- c("octubre", "septiembre", "vacio")
  for (caso in casos) {
    for (ruta in c(file.path(raiz, "salidas", paste0(caso, "_integrado")), file.path(raiz, "reportes", caso), file.path(raiz, "intentos", paste0("recon_", caso)))) {
      enlace <- Sys.readlink(ruta)
      if (file.exists(ruta) || dir.exists(ruta) || (!is.na(enlace) && nzchar(enlace))) stop("Reconstruccion ocupada o parcial; conservar y usar otra copia nueva.")
    }
  }
  e$probar_proyecto(raiz)
  for (caso in casos) {
    archivo <- paste0("config/", caso, ".csv")
    cfg <- utils::read.csv(file.path(raiz, archivo), colClasses = "character")
    app <- cfg$valor[cfg$clave == "app"]
    if (!identical(app, "shiny")) stop("Esta ruta reconstruye R/Shiny; elige Python para Streamlit.")
    e$trazar_proyecto(raiz, paste0("recon_", caso), archivo)
    e$generar_reporte(raiz, caso, archivo, app)
    e$renderizar_reporte(raiz, caso, archivo, app, quarto)
  }
  cat("Tres consultas y tres HTML reconstruidos. La app se inicia por separado.\n")
  invisible(raiz)
}
