# Lab 06.09 — Conciliar Python y R y explicar el cierre

**Tiempo orientativo:** 90–150 minutos, repartibles entre sesiones.

## Propósito, entradas y preparación

Aplica la [lección 06.09](../../../curriculum/06_r_foundations/09_known_result/README.md).
Necesitas 06.06–06.08 y el método de validación Python estudiado antes. La
entrada es la muestra de 14 ventas de 06.07 y el contrato común de esta lección.
No hay proyecto/checkpoint integrador implementado asociado.

Completa un recorrido de terminal de la lección: prepara la copia de cierre,
genera primero la referencia Python, restaura el entorno R, ejecuta y verifica.
Conserva fuentes y salidas anteriores. Trabaja en sesiones nuevas desde la
raíz de la **copia preparada**, no desde la raíz de DS Track salvo al prepararla.

## 1. Explicar qué significa «el mismo resultado»

Escribe la pregunta, población, unidad de fila, identificador, reglas de
faltantes y umbral. Contrasta con Python 01.06: ¿por qué no servirían sus
salidas originales como referencia directa? Distingue dos representaciones
equivalentes de una diferencia que obligaría a detener el cierre.

<details>
<summary>Solución razonada: acordar semántica antes de comparar archivos</summary>

La población son las 14 entradas, sin filtro temporal. Una fila representa
un registro; la clave válida es V y tres dígitos y debe ser única. Se aceptan
decimales no negativos y faltantes numéricos explícitos; se rechazan todas las
apariciones de claves válidas repetidas. El umbral es importe conocido >= 200.

Python 01.06 utiliza otro esquema y exige unidades enteras positivas; aquí
el cero observado es válido. La referencia de 06.09 adapta el método al nuevo
contrato, sin modificar ese ejercicio anterior. `4` y `4.0` pueden representar
el mismo número; NA frente a cero, una clave movida o un motivo distinto son
diferencias de significado que no se resuelven con formato de impresión.

</details>

## 2. Contrastar los resultados con cuentas manuales

Desde una consola R nueva en la copia preparada, carga las definiciones y
reproduce la lectura, validación y resumen sin depender de objetos que hayan
quedado en otra sesión. Explica los dos denominadores e identifica los seis
rechazos. Compara las tablas calculadas con la referencia Python.

<details>
<summary>Solución razonada: cálculo explícito e independiente de la presentación</summary>

```r
# Estas funciones de diagnostico usan R incluido, sin activar paquetes externos.
source("R/funciones_ventas.R", encoding = "UTF-8")
source("R/funciones_archivos.R", encoding = "UTF-8")
source("R/comparar_resultados.R", encoding = "UTF-8")
crudos_lab <- leer_ventas("datos/ventas_entrada.csv")
revision_lab <- validar_registros(crudos_lab)
resumen_lab <- resumir_importes(revision_lab$aceptados$importe_mxn)
print(revision_lab$controles) # 14 = 8 + 6
print(revision_lab$rechazos$fila_origen) # 8 9 10 11 12 13
print(resumen_lab) # 8/6/2; cobertura 75; suma 765.5; media 765.5/6; total NA.
pruebas_lab <- comparar_con_python(tablas_revision(revision_lab, resumen_lab),
                                  "output/referencia_python", "datos/ventas_entrada.csv")
print(nrow(pruebas_lab)) # 36 controles sobre memoria.
```

Se aceptan 8/14 registros. Entre los aceptados se conocen 6/8 importes, con
cobertura 75%. Los conocidos 300, 240, 0, 120, 80 y 25.5 suman 765.5 MXN;
la media es aproximadamente 127.5833333, incluyendo el cero. Los seis
rechazos no participan y el total completo de aceptados sigue desconocido.
Con umbral 200 los grupos son 2/4/2, no 2/6 tras ocultar pendientes.

</details>

## 3. Leer el informe y comprobar lo guardado

Inspecciona `conciliacion.csv`. Distingue sus dos etapas del número de ventas.
Vuelve a comprobar la entrega con el verificador del recorrido de terminal;
explica por qué un informe antiguo no acredita que los archivos actuales
sigan correctos. Comprueba las notas UTF-8 y los textos rechazados.

<details>
<summary>Solución razonada: memoria y archivos son dos fronteras</summary>

```r
informe_lab <- read.csv("output/cierre_r/conciliacion.csv", fileEncoding = "UTF-8")
print(nrow(informe_lab)) # 72 controles, no 72 ventas.
print(sum(informe_lab$etapa == "memoria")) # 36
print(sum(informe_lab$etapa == "csv_guardado")) # 36
print(all(informe_lab$correcto)) # TRUE
guardadas_lab <- leer_entrega_cierre("output/cierre_r")
print(guardadas_lab$aceptados$nota[guardadas_lab$aceptados$id_venta == "V007"])
# "México, mostrador"
print(guardadas_lab$rechazos$unidades[guardadas_lab$rechazos$id_venta == "V008"]) # "dos"
print(nrow(comparar_con_python(guardadas_lab, "output/referencia_python", "datos/ventas_entrada.csv"))) # 36
```

El informe registra controles aprobados en su ejecución. El verificador
recalcula desde la fuente y relee los CSV ahora, sin confiar en ese informe
ni reparar una entrega. Las notas son texto; los importes se comparan como
números con faltantes explícitos y tolerancia absoluta de 1e-9.

</details>

## 4. Confirmar un dato en otra muestra y conciliarla

Construye un archivo nuevo confirmando precio 60 para V006. Conserva la fuente
original; genera **otra** referencia Python y **otra** entrega R. Predice el
resultado: mismo 14/8/6, siete importes conocidos, cobertura 87.5%, suma 885.5,
media 126.5 y total desconocido. Mantén umbral 200: grupos 2/5/1.

<details>
<summary>Preparación razonada de una variante textual</summary>

```r
confirmadas_lab <- crudos_lab
confirmadas_lab$precio_mxn[confirmadas_lab$id_venta == "V006"] <- "60"
ruta_confirmada_lab <- "datos/ventas_confirmadas.csv"
if (file.exists(ruta_confirmada_lab)) { stop("Conserva la variante existente y elige otro nombre.") }
write.csv(confirmadas_lab, ruta_confirmada_lab, row.names = FALSE, fileEncoding = "UTF-8")
revision_confirmada_lab <- validar_registros(leer_ventas(ruta_confirmada_lab))
resumen_confirmado_lab <- resumir_importes(revision_confirmada_lab$aceptados$importe_mxn)
print(resumen_confirmado_lab) # 8/7/1; 87.5%; 885.5; 126.5; total NA; grupos 2/5/1.
print(identical(leer_ventas("datos/ventas_entrada.csv"), crudos_lab)) # TRUE
```

El CSV nuevo conserva texto y declara la confirmación ficticia. No sobrescribe
la entrada original ni reutiliza la referencia de otra fuente.

</details>

Ejecuta uno de estos recorridos completos **desde la copia de cierre**:

### PowerShell

```powershell
python referencia_python.py datos/ventas_confirmadas.csv output/python_confirmadas
$LASTEXITCODE
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar_cierre.R datos/ventas_confirmadas.csv output/python_confirmadas output/r_confirmadas
$LASTEXITCODE
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla verificar_cierre.R datos/ventas_confirmadas.csv output/python_confirmadas output/r_confirmadas
$LASTEXITCODE
```

### Bash/Zsh

```bash
python3 referencia_python.py datos/ventas_confirmadas.csv output/python_confirmadas
echo $?
Rscript --vanilla ejecutar_cierre.R datos/ventas_confirmadas.csv output/python_confirmadas output/r_confirmadas
echo $?
Rscript --vanilla verificar_cierre.R datos/ventas_confirmadas.csv output/python_confirmadas output/r_confirmadas
echo $?
```

### CMD / Anaconda Prompt

```bat
python referencia_python.py datos/ventas_confirmadas.csv output/python_confirmadas
echo %ERRORLEVEL%
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla ejecutar_cierre.R datos/ventas_confirmadas.csv output/python_confirmadas output/r_confirmadas
echo %ERRORLEVEL%
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla verificar_cierre.R datos/ventas_confirmadas.csv output/python_confirmadas output/r_confirmadas
echo %ERRORLEVEL%
```

Se esperan códigos 0. Si algo falla, revisa el mensaje antes de continuar y
conserva las carpetas previas. Elige destinos nuevos para repetir la práctica.

## 5. Detectar una referencia antigua

Predice qué ocurre al comparar la variante confirmada con la referencia de
la fuente original. Ejecuta este bloque **por separado** del script correcto.
¿Sería suficiente cambiar la huella del contexto a mano? Explica qué debes
reconstruir para conservar evidencia válida de un cambio legítimo.

<details>
<summary>Solución razonada: la referencia pertenece a una entrada concreta</summary>

```r
# Error deliberado: referencia anterior para una muestra modificada.
comparar_con_python(tablas_revision(revision_confirmada_lab, resumen_confirmado_lab),
                    "output/referencia_python", ruta_confirmada_lab)
```

Debe fallar por la fuente distinta, sin escribir resultados. Cambiar el
contexto no recalcula los importes Python. Hay que regenerar una referencia
en carpeta nueva para la nueva fuente, comprobarla y luego conciliar R.
La huella detecta cambios de bytes, no decide si la confirmación era correcta.

</details>

## 6. Alterar una copia de la entrega y verificar sin repararla

Conserva `output/cierre_r`. Copia sus archivos a `output/cierre_alterado`,
cambia **solo** el primer importe guardado de 300 a 301 y ejecuta el
verificador sobre esa copia. Debe fallar aunque conserve el informe antiguo.
Comprueba que el verificador no reescriba ni el importe alterado ni la entrega
original.

<details>
<summary>Preparación razonada: una alteración aislada y reversible</summary>

```r
alterada_lab <- "output/cierre_alterado"
if (file.exists(alterada_lab)) { stop("Conserva la copia existente y elige otro destino.") }
if (!dir.create(alterada_lab)) { stop("No se pudo crear la copia.") }
archivos_lab <- c("aceptados.csv", "rechazos.csv", "controles.csv", "resumen.csv",
                  "conciliacion.csv", "sesion_r.txt")
if (!all(file.copy(file.path("output/cierre_r", archivos_lab), alterada_lab, overwrite = FALSE))) {
  stop("La copia quedo parcial: conserva la carpeta y revisa el error.")
}
detalle_alterado_lab <- leer_tabla_cierre(file.path(alterada_lab, "aceptados.csv"))
detalle_alterado_lab$importe_mxn[1] <- "301"
write.csv(detalle_alterado_lab, file.path(alterada_lab, "aceptados.csv"),
            row.names = FALSE, fileEncoding = "UTF-8")
huellas_antes_lab <- tools::md5sum(file.path(alterada_lab, archivos_lab))
```

Se altera una copia identificada de práctica; no la fuente ni la entrega buena.
La lectura textual conserva también los marcadores NA y las notas.

</details>

### PowerShell desde la copia de cierre

```powershell
& "C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla verificar_cierre.R datos/ventas_entrada.csv output/referencia_python output/cierre_alterado
$LASTEXITCODE
```

### Bash/Zsh desde la copia de cierre

```bash
Rscript --vanilla verificar_cierre.R datos/ventas_entrada.csv output/referencia_python output/cierre_alterado
echo $?
```

### CMD / Anaconda Prompt desde la copia de cierre

```bat
"C:\Program Files\R\R-4.6.1\bin\Rscript.exe" --vanilla verificar_cierre.R datos/ventas_entrada.csv output/referencia_python output/cierre_alterado
echo %ERRORLEVEL%
```

Se espera código distinto de cero y un diagnóstico sobre aceptados/importe.
Después, desde la misma consola R del ejercicio:

```r
print(identical(tools::md5sum(file.path(alterada_lab, archivos_lab)), huellas_antes_lab)) # TRUE
print(leer_tabla_cierre("output/cierre_r/aceptados.csv")$importe_mxn[1]) # "300"
```

Un resultado incorrecto no se vuelve correcto al conservar un informe con
72 controles históricos. La comprobación actual debe fallar y conservar el
estado observado para diagnosticarlo.

## Evidencia, reflexión y criterio de salida del módulo

Conserva código, fuente original, variante, contexto Python, tablas, versiones,
informe y resultados de verificación. Explica 14 = 8 + 6, cobertura 6/8 y suma
765.5; después 885.5/126.5 con siete conocidos para la variante. Añade los
rechazos de referencia antigua y archivo alterado, con fuente/entrega buena
intactas. La evidencia local queda bajo output/ y no se agrega con fuerza a Git.

Responde con tus palabras:

1. ¿Qué cambió al aprender el modelo de R en lugar de traducir Python línea por línea?
2. ¿Por qué comparar solo suma o media habría sido insuficiente?
3. ¿Qué se compara exactamente y qué admite tolerancia? ¿Por qué NA no equivale a cero?
4. ¿Qué información aporta renv y qué aporta la conciliación de datos?
5. ¿Qué significa cerrar el aprendizaje si ya existen todas las lecciones?

Puedes continuar cuando reconstruyas desde una sesión nueva y justifiques
vectores/tablas, faltantes, reglas, conteos e indicadores con evidencia.
Registra lo realizado y las dudas en [PROGRESS.md](../../../PROGRESS.md), sin
confundir el cierre del material con finalización automática del estudiante.
No hay proyecto/checkpoint integrador implementado asociado.

Siguiente: [plan 07.01 — Tibbles, importación y pipes](../../../curriculum/07_tidyverse/README.md#01-tibbles-importacion-y-pipes),
todavía sin lección ni lab. Volver a la [lección 06.09](../../../curriculum/06_r_foundations/09_known_result/README.md).
