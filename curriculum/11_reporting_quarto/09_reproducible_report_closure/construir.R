# Cargar en consola R dentro del proyecto; no construye al hacer source().
construir_reporte <- function(quarto = "quarto") {
  if (!all(file.exists(c("reporte.qmd", "parametros.json", "cartera.csv", "renv.lock")))) stop("Falta la copia preparada")
  if (any(file.exists(c("salida", "reporte.html", "huellas.json", "render.log", "comando.txt")))) {
    stop("Entrega iniciada u ocupada: conservar y preparar otra copia")
  }
  p <- jsonlite::fromJSON("parametros.json", simplifyVector = FALSE)
  if (!is.list(p) || anyDuplicated(names(p)) || !setequal(names(p), c("fecha_corte", "minimo_mxn")) || length(p) != 2L) {
    stop("Exactamente fecha_corte y minimo_mxn requeridos")
  }
  source("analisis.R", local = TRUE, encoding = "UTF-8")
  analizar("cartera.csv", p$fecha_corte, p$minimo_mxn)
  version <- system2(quarto, "--version", stdout = TRUE)
  args <- c("render", "reporte.qmd", "--to", "html", "--execute-params", "parametros.json", "--cache-refresh")
  writeLines(c(paste("Quarto", version), paste(c("quarto", args), collapse = " ")), "comando.txt", useBytes = TRUE)
  Sys.setenv(QUARTO_R = R.home("bin"))
  status <- system2(quarto, args, stdout = "render.log", stderr = "render.log")
  if (status != 0L) stop("Fallo el render; conservar render.log y la copia parcial")
  nombres <- c("_quarto.yml", "cartera.csv", "parametros.json", "reporte.qmd", "estilos.css", "README.md", "verificar.py", "copiar_fuentes.py",
               "analisis.R", "construir.R", ".Rprofile", "renv/activate.R", "renv/settings.json", "restaurar.R",
               "DESCRIPTION", "renv.lock", "cierre.Rproj", "reporte.html", "salida/detalle.csv", "salida/resumen.csv",
               "salida/barras.csv", "salida/figura.png", "salida/metadatos.json", "render.log", "comando.txt")
  if (!all(file.exists(nombres))) stop("Faltan archivos; conservar e investigar")
  jsonlite::write_json(as.list(tools::md5sum(nombres)), "huellas.json", pretty = TRUE, auto_unbox = TRUE)
  cat("Entrega construida. Contrastar con la referencia externa y revisar el HTML.\n")
  invisible(normalizePath("."))
}
