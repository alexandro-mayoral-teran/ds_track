# Lab 11.02 — Crear, renderizar y revisar el primer HTML

Módulo: 11 — Reportes con Quarto. Tiempo orientativo: 45–75 minutos;
puedes separar creación, comparación y revisión en sesiones distintas.

## Entrada y objetivo

Lee la [lección 11.02](../../../curriculum/11_reporting_quarto/02_first_document/README.md).
Necesitas Quarto comprobado con `--version`, editor y navegador. Para preparar
las cifras elige Python estándar o R base. No necesitas instalar Jupyter/knitr,
producir PDF ni tener una entrega anterior.

Utiliza [hola.qmd](../../../curriculum/11_reporting_quarto/02_first_document/hola.qmd)
como primer documento y la
[muestra propia de seis filas](../../../curriculum/11_reporting_quarto/02_first_document/cartera.csv)
para la comparación. Son tres créditos 001/002/003 en septiembre y octubre de
2026: saldos 1000/2000/3000 y 1200/1800/3300 MXN. Deben existir las seis claves
ID/fecha sin ausencias ni duplicados y saldos enteros entre 0 y 1000000.

## Actividad

1. Crea una carpeta de práctica nueva dentro de `output`. Escribe tu `hola.qmd`
   con el ejemplo completo de la lección y cambia el título por uno propio.
   Comprueba la extensión real, guarda y renderiza HTML siguiendo el recorrido
   de tu shell. Abre el HTML desde el explorador de archivos.
2. Añade una sección con una frase en énfasis y un bloque **no ejecutable** que
   contenga `print(12345)`, marcado como `python`. Predice si aparecerá una salida
   calculada. Renderiza y explica lo que se muestra. No añadas llaves.
3. En otra carpeta nueva, ejecuta el preparador Python o R de 11.02 con la
   entrada incluida. Renderiza el `.qmd` resultante y comprueba pares, resumen,
   tabla y párrafo. Anota versión de Quarto y lenguaje de preparación.
4. Copia **solo** `reporte.html` a una carpeta vacía distinta y ábrelo. Revisa
   título, acentos, índice, tablas y lectura en una ventana más estrecha. Explica
   qué resolvió `embed-resources` y qué archivos faltan para reconstruir cálculos.
5. Prueba `preview` con tu `.qmd` usando el recorrido de la lección. Guarda un
   cambio en una frase y observa la vista previa; termina con Ctrl+C. No dejes
   ese proceso como requisito para abrir el HTML final.
6. Haz una copia del CSV en `output/1102_cambio.csv` y cambia solo 003/octubre de
   3300 a 3600. Antes de ejecutar el preparador, vuelve a renderizar el `.qmd`
   anterior: explica por qué conserva las cifras anteriores. Después genera
   otra preparación con la copia y renderiza su fuente; revisa qué cambió.
   No modifiques la entrada del curriculum ni el HTML a mano.

Los comandos siguientes presuponen que la copia modificada ya existe y que el
destino nuevo no existe. Sustituye `quarto` por la ruta completa comprobada si
tu terminal la necesita. Los recorridos completos de preparación/render originales
y de `preview` están en la lección.

### Cambio de entrada con Python — PowerShell

Desde la raíz del repositorio y con tu entorno activado:

```powershell
$quarto1102 = "quarto"
python curriculum/11_reporting_quarto/02_first_document/preparar.py output/1102_cambio_python --fuente output/1102_cambio.csv
& $quarto1102 render output/1102_cambio_python/reporte.qmd --to html
```

### Cambio de entrada con Python — Bash/Zsh

Desde la raíz y con tu entorno activado:

```bash
quarto1102="quarto"
python curriculum/11_reporting_quarto/02_first_document/preparar.py output/1102_cambio_python --fuente output/1102_cambio.csv
"$quarto1102" render output/1102_cambio_python/reporte.qmd --to html
```

### Cambio de entrada con R

En RStudio o tu IDE, reinicia R y ejecuta un script completo con la raíz de
DS Track como directorio de trabajo:

```r
source("curriculum/11_reporting_quarto/02_first_document/preparar.R", encoding = "UTF-8")
r <- preparar_documento("output/1102_cambio.csv", "output/1102_cambio_r")
print(r$resumen)
stopifnot(identical(as.numeric(r$resumen$saldo_mxn), c(6000, 6600)),
          identical(r$porcentaje, "10.00%"))
```

Abre el nuevo `.qmd` y pulsa Render en RStudio, o usa la terminal del sistema:

**PowerShell:**

```powershell
$quarto1102 = "quarto"
& $quarto1102 render output/1102_cambio_r/reporte.qmd --to html
```

**Bash/Zsh:**

```bash
quarto1102="quarto"
"$quarto1102" render output/1102_cambio_r/reporte.qmd --to html
```

## Resultado, comprobación y evidencia

Conserva fuente/HTML de tu primer documento, las dos preparaciones completas,
la copia modificada del CSV y el HTML separado. En tus notas identifica las
dos fases, la versión usada y las comprobaciones de lectura/cifras realizadas.
Una captura puede apoyar la revisión visual, pero no sustituye los archivos.

<details>
<summary>Solución razonada y resultados esperados</summary>

El primer HTML muestra el título del YAML, las secciones del cuerpo, el énfasis
y el código literal. `print(12345)` se presenta como ejemplo; no aparece una
salida ejecutada porque el bloque no tiene llaves y no se eligió un motor.

La primera comparación conserva tres créditos en ambos cortes: 6000/6300 MXN,
diferencia +300 y 5.00% sobre septiembre. Los pares cambian +200/-200/+300.
Modificar otro CSV y renderizar el `.qmd` anterior conserva esos números porque
ya son texto guardado. Eso no es un error de caché: el documento no contiene
instrucciones para volver a calcularlos.

Tras preparar con la copia, octubre suma 6600, diferencia +600 y tasa 10.00%;
el cambio de 003 es +600. Septiembre y los otros dos pares permanecen iguales.
El preparador inserta los valores y Quarto transforma su presentación.

El HTML con recursos incluidos de esta muestra permite lectura separado de la
carpeta original y sin un proceso preview activo. Para reconstruir hacen falta
entrada, scripts, funciones reutilizadas, `.qmd` y herramientas. No basta con
que una página abra, ni se necesita publicar un sitio para entregar HTML local.

</details>

## Ampliaciones opcionales

- En una copia del primer `.qmd`, retira `embed-resources: true`, renderiza y
  observa los recursos que genera esa versión de Quarto. Prueba mover la salida
  con y sin su carpeta asociada; conserva la entrega esencial con recursos incluidos.
- En otra copia introduce un YAML inválido y comprueba el mensaje de fallo.
  Si queda un HTML de una ejecución previa, explica por qué no prueba éxito nuevo.
  Corrige el fuente y vuelve a renderizar; no ocultes el fallo editando la salida.

## Criterio de salida y siguiente paso

Puedes reconstruir una comparación y su HTML desde archivos guardados, explicar
qué se calculó y qué se renderizó, y revisar el resultado fuera de preview.
Registra evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md).
`05_monthly_report` y checkpoints siguen pendientes en
[proyectos](../../../projects/README.md); el material disponible no acredita tu práctica.

Siguiente: [11.03 — Ejecución con Python o R](../../../curriculum/11_reporting_quarto/03_execution_python_r/README.md),
ya disponible. No es necesario comenzarla para cerrar esta sesión de trabajo.
