# Copia de práctica — ventas con renv

Esta carpeta se completa con `preparar_proyecto.R` de DS Track. En la plantilla
no están las carpetas R/ y datos/: no la ejecutes directamente.

Desde la raíz de la copia preparada:

1. Ejecuta `Rscript --vanilla restaurar.R`: activa renv y restaura los paquetes
   del lockfile. Puede acceder a CRAN e instalar dentro de esta copia.
2. Comprueba el estado y las versiones impresas.
3. Ejecuta `Rscript --vanilla ejecutar.R`: escribe en output/primera_revision.
   Para conservar esa salida, repite con otra carpeta:
   `Rscript --vanilla ejecutar.R output/segunda_revision`.

En Windows puedes usar la ruta explícita de Rscript de tu instalación.
Las rutas se interpretan desde esta carpeta, no desde la raíz de DS Track.
Consulta la lección y el lab 06.08 de DS Track para los recorridos completos,
snapshot, reconstrucción y diagnóstico. Copiada fuera del repositorio, esta
carpeta preparada tiene las fuentes y datos que necesita el análisis.

Se esperan 14 entradas, 8 aceptados y 6 rechazos; cobertura 6/8 y suma observada
765.5 MXN. El total completo permanece desconocido. La presentación de la media
con cuatro cifras significativas no cambia el dato guardado en resumen.csv.

El perfil local dirige estado y descargas de renv a .renv-local/ y desactiva
su caché compartida para esta práctica. Los paquetes se instalan en renv/library/;
no se instalan en Conda ni en la biblioteca del sistema. --vanilla no carga
automáticamente .Rprofile: restaurar.R y ejecutar.R lo hacen explícitamente.

La versión de R está registrada en renv.lock; renv no instala el intérprete ni
configura el locale. El análisis reutiliza el contrato UTF-8 de 06.07. Conserva
los avisos y revisa LC_CTYPE si la sesión no admite los acentos de la muestra.

Para transferir el proyecto conserva fuentes, datos sintéticos, DESCRIPTION,
renv.lock, .Rprofile, renv/activate.R y renv/settings.json. No copies las
bibliotecas, .renv-local/, output/, .RData ni .Rhistory. Una nueva copia debe
restaurar y ejecutar; un lockfile por sí solo no contiene los datos ni el código.
