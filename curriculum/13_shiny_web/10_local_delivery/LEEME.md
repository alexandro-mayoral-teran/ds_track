# Explorador Shiny — entrega local 13.10

Esta carpeta contiene fuentes, datos sintéticos, reglas, entorno bloqueado,
pruebas y resultados de seis casos. Lee CONTRATO.md antes de ejecutarla.
No depende del repositorio DS Track ni de una entrega anterior. Necesitas
R y un navegador; el lockfile registra paquetes, no instala R ni el sistema.

Referencias comprobadas: R 4.6.1, Shiny 1.14.0, ggplot2 4.0.3 y renv 1.3.1.
DESCRIPTION/renv.lock contienen los mismos 42 registros de la práctica previa.
No se incluyen paquetes instalados, cachés, workspace, descargas personales
ni credenciales. La restauración puede necesitar red y disponibilidad de los
paquetes registrados. No se ha comprobado otra plataforma distinta de Windows.

## 1. Revisar y restaurar en una carpeta de trabajo

Conserva la entrega recibida y trabaja en otra carpeta. Para reconstruir copia
solo las rutas de archivos_cierre() en entrega.R: son los 24 archivos fuente,
incluyendo .Rprofile y los dos archivos de renv, sin biblioteca ni resultados.
No copies a ciegas todo un proyecto ya ejecutado.

Abre shiny_1310.Rproj o su carpeta en tu IDE y reinicia R sin cargar workspace.
Desde la **consola R** de esa copia, después de revisar los scripts:

```r
getwd()
source("restaurar.R")
source("ejecutar_pruebas.R")
```

restaurar.R activa la configuración local y ejecuta renv::restore; instala en
renv/library, con estado .renv-local y caché compartida desactivada. No inicialices
renv en la raíz de otro proyecto ni modifiques Conda/globales. Si no se pueden
restaurar las versiones, conserva el diagnóstico; no cambies lockfile para
presentar una reconstrucción distinta como equivalente.

En Windows, un ejecutor restringido puede no leer los enlaces del sandbox a
paquetes base: revisa sus permisos sin desactivar comprobaciones. El conjunto
de pruebas debe terminar con OK conjunto esencial. Los mensajes [fuente] de
duplicado/ausencia son provocados sobre un CSV temporal propio.

## 2. Iniciar y demostrar la app

En la consola R de la copia:

```r
source("iniciar.R")
iniciar_app("app.R", puerto = 8532)
```

Escucha solo en 127.0.0.1. La URL de consola sirve en ese equipo mientras el
proceso R siga activo. Si el puerto está ocupado elige otro; no cierres procesos
ajenos. No es un sitio publicado en Internet. Detén tu servidor con Stop/Esc;
cerrar una pestaña no detiene R. Para repasar, minimo.R es el número/doble/nota.

Demostración mínima: A septiembre/ambos/2000 → 002/003, 4500 MXN y 66.67%;
B octubre/ambos/2000 → 003, 2600 MXN y 33.33%. Edita A sin aplicar: conserva
su consulta; B sigue independiente. Descarga selección y contexto de A antes
de otra aplicación y relee sus valores por crédito. Prueba cero, vacío,
rechazo 1.5, noviembre sin universo y recarga. Las pruebas de servidor no
sustituyen esta revisión de controles, figura y descarga real.

## 3. Reconstruir resultados en otro destino nuevo

Detén el servidor. Desde la copia reconstruida con entorno restaurado:

```r
source("entrega.R")
crear_entrega("../recalculada_1310")
verificar_entrega("../recalculada_1310", referencia = "../entrega_recibida/cartera.csv")
```

Sustituye entrega_recibida por la ruta real a una referencia externa revisada.
No uses como referencia el CSV de la misma carpeta que verificas. crear_entrega
solo admite destinos nuevos fuera de origen, copia una lista explícita, recalcula
seis casos y comprueba lo generado. Si falla dejando carpeta parcial, consérvala
y revisa; no se trata como destino nuevo ni se sobrescribe.

La entrega base tiene 41 archivos: 24 fuentes, resumen/INFORME/huellas y 14
resultados (cinco selecciones CSV, cinco contextos CSV y cuatro PNG). Se esperan:

| Caso | IDs | Saldo seleccionado | Créditos / universo |
| --- | --- | ---: | ---: |
| septiembre | 002, 003 | 4500 | 2/3 |
| octubre | 003 | 2600 | 1/3 |
| cero | 001, 003 | 2500 | 2/3 |
| frontera | 003 | 2500 | 1/3 |
| vacio | Ninguno | 0 | 0/3 |
| sin_universo | Sin corte | Ausente | Sin denominador |

Los resultados son evidencia generada en lote, no exportaciones antiguas de una
sesión web. Revisa PNG con sus tablas; las escalas de cada figura/panel pueden
diferir. Compara importes y etiquetas, no alturas entre gráficos independientes.

## 4. Verificar sin ejecutar la app

Desde un R base nuevo puedes cargar una copia revisada de entrega.R y llamar
verificar_entrega(entrega, referencia). Solo lee: no carga .Rprofile, instala
paquetes, ejecuta el código recibido ni escribe dentro de la entrega. Compara
fuente por clave/campo, seis preguntas, tablas completas y ausencias; comprueba
inventario, huellas y cabecera/dimensiones PNG. No exige que no existan carpetas
de entorno local después de reconstruir, ni certifica que no añadiste datos
privados: revisa manualmente lo que vas a compartir.

Usa un verificador revisado fuera de una copia deliberadamente alterada. Las
huellas no autentican y pueden actualizarse junto con un error. El contraste
externo permite detectar valores equivocados aunque sus sumas coincidan;
no prueba que todo código recibido sea correcto. Repetir pruebas, recalcular
y demostrar en navegador sigue siendo necesario.

## 5. Evidencia y límites

Guarda tu nota humana fuera de la carpeta entregable: fecha/entorno, casos
ejecutados, resultados, dudas y siguiente paso. INFORME.md es texto generado;
no lo uses como certificado de una sesión pasada. El lockfile tampoco garantiza
disponibilidad futura de paquetes, binarios o componentes del sistema.

Terminal opcional, desde la copia, en PowerShell:

```powershell
$rscript = "C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
& $rscript --vanilla -e 'source("restaurar.R"); source("ejecutar_pruebas.R")'
if ($LASTEXITCODE -ne 0) { throw "Revisa la restauracion o pruebas." }
& $rscript --vanilla -e 'source("iniciar.R"); iniciar_app("app.R", puerto=8532, abrir=FALSE)'
```

Abre la URL y detén con Ctrl+C. Alternativa completa Bash/Zsh desde la copia:

```bash
Rscript --vanilla -e 'source("restaurar.R"); source("ejecutar_pruebas.R")' || exit 1
Rscript --vanilla -e 'source("iniciar.R"); iniciar_app("app.R", puerto=8532, abrir=FALSE)'
```

Detén con Ctrl+C. Despliegue, autenticación y empaquetado binario son ampliaciones.
Entregar material y pasar pruebas no certifica aprendizaje ni completa un
proyecto/checkpoint de otro recorrido.
