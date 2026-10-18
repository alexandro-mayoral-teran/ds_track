# Desde la raiz de DS Track. Solo copia fuentes; no activa ni instala renv.
argumentos <- commandArgs(trailingOnly = TRUE)
if (length(argumentos) > 1L) { stop("Indica como maximo una carpeta nueva.") }
destino <- "curriculum/06_r_foundations/08_projects_renv/output/ventas_renv"
if (length(argumentos) == 1L) { destino <- argumentos[1] }
if (file.exists(destino) || dir.exists(destino)) {
  stop("El destino ya existe; elige otra carpeta para conservarlo.")
}
base <- "curriculum/06_r_foundations"
plantilla <- file.path(base, "08_projects_renv", "plantilla")
origenes <- c(
  file.path(plantilla, c(".Rprofile", ".gitignore", "DESCRIPTION", "renv.lock",
                         "analisis.R", "ejecutar.R", "restaurar.R", "README.md")),
  file.path(plantilla, "renv", c("activate.R", "settings.json")),
  file.path(base, "06_functions_control", "funciones_ventas.R"),
  file.path(base, "07_files_validation", c("funciones_archivos.R", "ventas_entrada.csv"))
)
relativas <- c(".Rprofile", ".gitignore", "DESCRIPTION", "renv.lock",
               "analisis.R", "ejecutar.R", "restaurar.R", "README.md",
               "renv/activate.R", "renv/settings.json", "R/funciones_ventas.R",
               "R/funciones_archivos.R", "datos/ventas_entrada.csv")
if (!all(file.exists(origenes))) { stop("Faltan fuentes; ejecuta desde la raiz de DS Track.") }
if (!dir.create(destino, recursive = TRUE)) { stop("No se pudo crear el destino.") }
for (subcarpeta in c("R", "datos", "renv")) {
  if (!dir.create(file.path(destino, subcarpeta))) { stop("No se pudo crear una subcarpeta.") }
}
for (i in seq_along(origenes)) {
  if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) {
    stop("La copia quedo parcial; revisa el mensaje y conserva esa carpeta.")
  }
}
cat("Proyecto copiado sin instalar paquetes. Entra en esa carpeta para restaurar.\n")
print(destino)
