# Lab 06.08 — Restaurar y reconstruir un proyecto R

**Tiempo orientativo:** 75–120 minutos, más descargas; repartible entre sesiones.

## Propósito, entradas y preparación

Aplica la [lección 06.08](../../../curriculum/06_r_foundations/08_projects_renv/README.md).
Necesitas haber practicado 06.06/06.07. La entrada son fuentes, datos sintéticos,
`DESCRIPTION`, activador y lockfile de la plantilla. No requiere RStudio ni
construir el proyecto integrador previsto; no hay checkpoint implementado asociado.

Completa primero uno de los recorridos de terminal de la lección: prepara
`ventas_renv`, restaura y ejecuta. Ese paso puede descargar e instalar **renv
y withr en la copia**, sin instalar en Conda o la biblioteca del sistema.
Conserva el registro de la restauración y el resultado bajo `output/`.
Si tu copia ya funciona, comprueba su estado sin reinstalar innecesariamente.

## 1. Identificar qué se conserva

Explora la copia preparada. Localiza código, datos, declaración de dependencias,
lockfile, perfil, biblioteca instalada y salida. Explica cuál de estas piezas
permite seleccionar versiones y cuál contiene los paquetes ya instalados.
Indica qué seguiría faltando si solo te entregaran `renv.lock`.

<details>
<summary>Solución razonada: archivos portables frente a instalación local</summary>

`R/` y los scripts contienen código; `datos/` contiene el CSV de práctica;
`DESCRIPTION` declara withr; `renv.lock` registra R 4.6.1 y las versiones renv
1.3.1/withr 3.0.3. `renv/activate.R` y `.Rprofile` permiten activar la biblioteca.
Los paquetes instalados están en `renv/library/...`; el estado auxiliar queda
en `.renv-local/`. Los resultados están bajo `output/`.

El lockfile no contiene código propio, datos ni el intérprete. Tampoco contiene
los archivos instalados de cada paquete: permite obtenerlos de las fuentes
registradas, si siguen disponibles y son compatibles con la computadora.

</details>

## 2. Comprobar la sesión que realmente ejecuta

En una consola R nueva, situada en la raíz de `ventas_renv`, activa su perfil.
Muestra estado, rutas de bibliotecas, ruta de withr y versiones. Demuestra
que la opción `digits` vuelve a su valor anterior tras una impresión temporal.
¿Por qué `--vanilla` por sí solo no activa renv?

<details>
<summary>Solución razonada: activar expresamente y mirar rutas</summary>

```r
source(".Rprofile")
estado_lab <- renv::status()
print(estado_lab$synchronized) # TRUE
print(.libPaths())
print(find.package("withr"))
print(utils::packageVersion("renv")) # 1.3.1
print(utils::packageVersion("withr")) # 3.0.3
print(R.version.string)
digitos_lab <- getOption("digits")
withr::with_options(list(digits = 4), print(765.5 / 6)) # 127.6
print(identical(getOption("digits"), digitos_lab)) # TRUE
```

La primera biblioteca y withr deben quedar dentro de la copia. El sandbox
también debe estar bajo `.renv-local/`. `--vanilla` omite el perfil automático;
los scripts del curso lo cargan de forma explícita. Las rutas pueden variar
con plataforma y versión R: comprueba su pertenencia al proyecto, no copies
una ruta personal como si fuera parte del contrato.

</details>

## 3. Conservar el entorno comprobado con snapshot

Inspecciona `DESCRIPTION` y `renv.lock` como texto. Después del análisis correcto,
ejecuta snapshot y revisa su propuesta. Explica por qué usas modo `explicit`
y qué tendrías que declarar si, en el futuro, el código necesitara otro paquete.
No instales un paquete adicional solo para generar cambios en el lockfile.

<details>
<summary>Solución razonada: registrar el estado que ya se comprobó</summary>

```r
renv::status()
renv::snapshot()
renv::status()
```

Con el mismo R y los mismos paquetes no se esperan cambios relevantes. En modo
`explicit`, `DESCRIPTION` expresa las dependencias deseadas. Una nueva dependencia
se declara allí, se instala en la biblioteca activa y se comprueba antes de
registrarla. `snapshot` no guarda objetos, datos o resultados y no instala un
paquete que falte. No aceptes un cambio de versión de R sin explicar qué R
ejecutaste y qué referencia deseas conservar.

</details>

## 4. Reconstruir sin transferir bibliotecas

Prepara otra copia llamada `ventas_reconstruidas`, sin copiar `renv/library`,
`.renv-local`, salidas ni `.RData`. Restáurala y ejecútala desde procesos nuevos.
Estos recorridos parten otra vez de la raíz de DS Track; elige uno completo.

### PowerShell

```powershell
Set-Location C:\bluepill5\Devs\ds_track
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla curriculum/06_r_foundations/08_projects_renv/preparar_proyecto.R curriculum/06_r_foundations/08_projects_renv/output/ventas_reconstruidas
Set-Location curriculum/06_r_foundations/08_projects_renv/output/ventas_reconstruidas
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla restaurar.R
$LASTEXITCODE
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar.R
$LASTEXITCODE
```

### Bash/Zsh

```bash
cd /ruta/a/ds_track
Rscript --vanilla curriculum/06_r_foundations/08_projects_renv/preparar_proyecto.R curriculum/06_r_foundations/08_projects_renv/output/ventas_reconstruidas
cd curriculum/06_r_foundations/08_projects_renv/output/ventas_reconstruidas
Rscript --vanilla restaurar.R
echo $?
Rscript --vanilla ejecutar.R
echo $?
```

### CMD / Anaconda Prompt

```bat
cd /d C:\bluepill5\Devs\ds_track
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla curriculum/06_r_foundations/08_projects_renv/preparar_proyecto.R curriculum/06_r_foundations/08_projects_renv/output/ventas_reconstruidas
cd curriculum\06_r_foundations\08_projects_renv\output\ventas_reconstruidas
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla restaurar.R
echo %ERRORLEVEL%
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar.R
echo %ERRORLEVEL%
```

Conserva los destinos anteriores. Si el de reconstrucción ya existe, elige
otro y ajusta tanto el argumento del preparador como el cambio de carpeta.
Se esperan códigos 0 y los mismos conteos/indicadores, aunque las rutas sean otras.

<details>
<summary>Comprobación razonada desde una consola R en la raíz de DS Track</summary>

```r
base_lab <- file.path("curriculum", "06_r_foundations", "08_projects_renv", "output")
original_lab <- file.path(base_lab, "ventas_renv", "output", "primera_revision")
reconstruida_lab <- file.path(base_lab, "ventas_reconstruidas", "output", "primera_revision")
for (archivo_lab in c("aceptados.csv", "rechazos.csv", "controles.csv", "resumen.csv")) {
  a_lab <- read.csv(file.path(original_lab, archivo_lab), fileEncoding = "UTF-8")
  b_lab <- read.csv(file.path(reconstruida_lab, archivo_lab), fileEncoding = "UTF-8")
  print(archivo_lab)
  print(isTRUE(all.equal(a_lab, b_lab, tolerance = 1e-12))) # TRUE en las cuatro.
}
controles_lab <- read.csv(file.path(reconstruida_lab, "controles.csv"))
resumen_lab <- read.csv(file.path(reconstruida_lab, "resumen.csv"))
print(controles_lab) # 14 8 6
print(resumen_lab) # 8/6/2; cobertura 75; suma 765.5; media 765.5/6; total NA.
```

Esta comparación usa la muestra conocida: no es un lector contractual genérico
para CSV arbitrarios. Son cuatro tablas equivalentes; no es necesario que
`sesion.txt` tenga los mismos bytes. Revisa también la nota UTF-8 y los motivos
de rechazo, como hiciste en 06.07. La reconstrucción local no acredita que se
haya comprobado otro sistema operativo.

</details>

## 5. Extensión opcional: diagnosticar un paquete que falta

Usa solo la copia `ventas_reconstruidas`, sin tocar la primera. En una sesión
nueva allí, sin ejecutar antes el análisis, retira withr de **esa biblioteca**
con renv. Conserva el lockfile y observa el desajuste:

```r
source(".Rprofile")
renv::remove("withr")
estado_incompleto_lab <- renv::status()
print(estado_incompleto_lab$synchronized) # FALSE
```

`remove` desinstala un paquete de la biblioteca del proyecto activo. Es una
alteración deliberada y reversible de esta copia de práctica; verifica el
proyecto antes de usarla. No cambies `DESCRIPTION` ni hagas snapshot para
ocultar que falta una dependencia que el análisis necesita.

Cierra esa sesión sin guardar objetos. En un proceso nuevo, `ejecutar.R`
debe detenerse por entorno incompleto antes de generar otra entrega. Después
ejecuta `restaurar.R` con el recorrido de terminal anterior. Para repetir el
análisis usa un destino nuevo, como `output/tras_restaurar`:

### PowerShell desde la copia reconstruida

```powershell
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar.R output/no_debe_crearse
$LASTEXITCODE
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla restaurar.R
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar.R output/tras_restaurar
$LASTEXITCODE
```

### Bash/Zsh desde la copia reconstruida

```bash
Rscript --vanilla ejecutar.R output/no_debe_crearse
echo $?
Rscript --vanilla restaurar.R
Rscript --vanilla ejecutar.R output/tras_restaurar
echo $?
```

### CMD / Anaconda Prompt desde la copia reconstruida

```bat
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar.R output/no_debe_crearse
echo %ERRORLEVEL%
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla restaurar.R
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar.R output/tras_restaurar
echo %ERRORLEVEL%
```

El primer comando debe fallar; el último debe terminar con código 0 tras
restaurar. Si la restauración falla, detente a revisar su mensaje antes de
intentar el análisis. No necesitas completar esta extensión para cerrar
la práctica principal de reconstrucción.

## Evidencia, criterio de salida y reflexión

Conserva las versiones/rutas comprobadas, el resultado de `status`, el lockfile,
las cuatro tablas y `sesion.txt` de ambas copias, y las comparaciones. Explica
14 = 8 + 6, cobertura 6/8 y suma observada 765.5; no conviertas un total
desconocido en cero. Para la extensión añade el estado incompleto, el rechazo
de ejecución y la recuperación sin cambiar el lockfile.

Responde con tus palabras:

1. ¿Qué diferencia hay entre activar renv, restaurar y ejecutar el análisis?
2. ¿Qué dirección tiene snapshot y qué dirección tiene restore?
3. ¿Por qué una biblioteca ya instalada no es lo que transferimos a otra copia?
4. ¿Qué archivos faltan si solo recibes el lockfile?
5. ¿Qué cosas pueden impedir reproducir aunque las versiones estén registradas?

Cierra cuando puedas reconstruir y justificar los resultados en una sesión
nueva. Registra evidencia real y dudas en [PROGRESS.md](../../../PROGRESS.md).
No hay proyecto/checkpoint integrador implementado asociado. Continúa con el
[06.09 — Reproducir un resultado conocido](../../../curriculum/06_r_foundations/09_known_result/README.md). Volver a la [lección 06.08](../../../curriculum/06_r_foundations/08_projects_renv/README.md).
