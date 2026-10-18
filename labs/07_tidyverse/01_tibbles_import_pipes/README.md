# Lab 07.01 — Cargar y explicar una tibble

## Propósito y entradas

Practica la [lección 07.01](../../../curriculum/07_tidyverse/01_tibbles_import_pipes/README.md)
antes de aplicar verbos de dplyr. Recibes el CSV ficticio de seis créditos,
su diccionario y el lector con controles. Usa la misma carpeta renv de 06.09
extendida según el recorrido en RStudio/IDE de la lección; no crees otro
entorno ni vuelvas a ejecutar el preparador si ya lo hiciste.

**Resultado:** un script propio que inspeccione la tabla y una explicación
breve sobre sus tipos, faltantes y secuencia de pasos. No se pide limpiar,
exportar, graficar ni implementar el proyecto integrador, todavía pendiente.
Puedes dividir el lab en dos sesiones: carga/forma y problemas/explicación.

## 1. Anticipar el contrato

Sin ejecutar R, abre datos/cartera_demo.csv como texto en tu práctica.
Anota la unidad de cada fila, el corte y los cinco campos. Predice:

1. ¿Por qué 001 es texto aunque solo contenga dígitos?
2. ¿Cuántos registros y columnas hay? ¿Por qué la coma de comercio, local no añade una columna?
3. ¿Qué campo de 005 está vacío? ¿Qué significa el cero de 004?
4. ¿Qué tipos necesitas para saldo y atraso? ¿Por qué dejamos la fecha como texto?

<details>
<summary>Comprobar el razonamiento</summary>

Una fila es un crédito ficticio en 2026-09-30. Son seis filas y cinco columnas;
la cabecera no cuenta como registro. El identificador no es una cantidad:
interpretarlo como número perdería los ceros. Las comillas contienen la coma.
En 005 falta atraso, no saldo; 004 tiene saldo y atraso cero conocidos.
Usamos double para saldo e integer para atraso, que admite NA_integer_. La
fecha se conserva como character hasta aprender su interpretación en 07.09.

</details>

## 2. Cargar desde el editor de RStudio o tu IDE

Abre el proyecto **de tu práctica**, donde están .Rprofile, renv.lock y datos/.
Comprueba getwd() en **Console**; no abras Terminal para esta actividad.
Desde **File > New File > R Script**, crea output/importar_mi_cartera.R
(crea output/ desde Files si falta), sin editar el ejecutor ni la fuente.
Aunque guardes el script en output/, conserva la raíz de la práctica como
directorio de trabajo. Empieza con:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_importacion.R", encoding = "UTF-8")
cartera <- leer_cartera("datos/cartera_demo.csv")
```

Selecciona el bloque completo y usa **Run** o Ctrl+Enter (Cmd+Enter en macOS).
Observa cartera en **Environment**; puedes abrirla en el visor para inspeccionarla,
sin sustituir los controles del script por una revisión visual.
Añade llamadas que muestren clase, dimensión, nombres y tipo de cada columna.
Muestra las seis filas completas y ejecuta comprobar_muestra(cartera).
La función de comprobación devuelve TRUE invisiblemente: si no hay error,
pasaron los controles de esta muestra. No exige una captura idéntica a otra
sesión: el ancho y el formato impreso pueden variar. Usa print() para las
salidas que quieras ver también al ejecutar el script completo con source().

<details>
<summary>Una solución posible</summary>

```r
print(class(cartera))
print(dim(cartera))
print(names(cartera))
print(vapply(cartera, typeof, character(1)))
print(cartera, n = 6, width = Inf)
comprobar_muestra(cartera)
stopifnot(sum(cartera[["saldo_mxn"]]) == 6000,
          sum(!is.na(cartera[["saldo_mxn"]])) == 6,
          sum(is.na(cartera[["dias_atraso"]])) == 1)
```

La clase incluye data.frame junto con tbl_df/tbl. Tres columnas son character,
saldo es double y atraso integer. Los seis saldos son conocidos y suman 6000 MXN;
solo cinco de seis atrasos se conocen. No convertir el faltante a cero.

</details>

## 3. Distinguir contenedor y contenido

Compara cartera["saldo_mxn"], cartera[, "saldo_mxn"] y
cartera[["saldo_mxn"]] mediante class, dim y length. Construye una tibble de
dos filas con identificadores de texto y saldos; explica por qué sus columnas
pueden tener tipos diferentes.

<details>
<summary>Comprobación</summary>

```r
columna_tabla <- cartera[, "saldo_mxn"]
columna_vector <- cartera[["saldo_mxn"]]
stopifnot(inherits(columna_tabla, "tbl_df"),
          identical(dim(columna_tabla), c(6L, 1L)),
          length(columna_tabla) == 1L,
          is.double(columna_vector), length(columna_vector) == 6L,
          is.null(dim(columna_vector)))
mini <- tibble::tibble(id_credito = c("001", "002"), saldo_mxn = c(1000, 1500))
stopifnot(identical(mini[["saldo_mxn"]], c(1000, 1500)))
```

length de una tabla cuenta columnas; length del vector cuenta elementos. Los
tipos se conservan por columna porque la tabla es una lista, no un vector
atómico común a todas las celdas. La extracción con un solo corchete conserva
la tibble; doble corchete obtiene su columna. Relaciónalo con 06.05.

</details>

## 4. Explicar un pipe

Obtén las primeras tres filas y cuenta cuántas quedaron con un pipe de dos
pasos. Escribe su equivalente sin pipe y comprueba que cartera conserva seis
filas. Explica el tipo de entrada/salida de head y nrow. Después cambia 3 por 0:
una vista vacía debe conservar las cinco columnas.

<details>
<summary>Una solución posible</summary>

```r
cantidad <- cartera |> head(3) |> nrow()
stopifnot(identical(cantidad, nrow(head(cartera, 3))), cantidad == 3L,
          nrow(cartera) == 6L)
vacia <- cartera |> head(0)
stopifnot(identical(dim(vacia), c(0L, 5L)),
          identical(names(vacia), names(cartera)))
```

head recibe la tabla y devuelve otra tabla. nrow recibe esa tabla y devuelve
un entero. Ni el pipe ni head reemplazan cartera: guardamos el resultado en
otro nombre. Una vista vacía no prueba que el archivo original estuviera vacío.

</details>

## 5. Detectar una interpretación fallida

Construye un CSV literal de dos filas usando I(): identificadores 001/002 y
saldos 100/mil. Declara texto/double. No uses suppressWarnings: observa la
advertencia y después problems(). ¿Qué saldo queda como NA? Ejecuta
stop_for_problems en una llamada separada: debe detener el flujo.

<details>
<summary>Solución y explicación</summary>

```r
problematica <- readr::read_csv(
  I("id_credito,saldo_mxn\n001,100\n002,mil\n"),
  col_types = readr::cols(id_credito = readr::col_character(),
                          saldo_mxn = readr::col_double()),
  show_col_types = FALSE, lazy = FALSE
)
problemas <- readr::problems(problematica)
print(problemas)
stopifnot(nrow(problemas) == 1L,
          identical(problematica[["id_credito"]], c("001", "002")),
          is.na(problematica[["saldo_mxn"]][2]))
```

Ejecuta **aparte**, como error esperado:

```r
readr::stop_for_problems(problematica)
```

La segunda fila de datos no se pudo interpretar como double. El problema
conserva el valor mil; el NA no es una ausencia permitida del archivo. No
reemplazarlo por cero ni seguir calculando. En cambio, -10 sí es un double:
decidir si se permite un saldo negativo es una regla de dominio posterior.
problems vacía no certifica claves, rangos o fechas.

</details>

## 6. Reconstruir y guardar evidencia

Guarda output/importar_mi_cartera.R. Deja el ejemplo de error esperado en otro
archivo o ejecútalo aparte; no debe impedir reconstruir la carga correcta.
Mantén el bloque de inicio de la actividad 2 en tu script.

1. Guarda los archivos y usa **Session > Restart R** (o reinicia la sesión R
   en tu IDE). Comprueba que no se recuperó cartera desde un workspace guardado;
   la evidencia debe reconstruirse con código. Limpiar Console no reinicia R.
2. Conserva abierto el mismo proyecto: el directorio sigue siendo la raíz de
   la práctica. Ejecuta en Console el bloque siguiente. source() lee tu archivo
   y ejecuta todas sus expresiones; no cambia el directorio a output/.
3. Comprueba que vuelven a aparecer cartera, los controles y los resultados
   esperados. Si falta un objeto, añade a tu script el paso que lo construye.

```r
source("output/importar_mi_cartera.R", encoding = "UTF-8")
source("importar_cartera.R", encoding = "UTF-8")
```

También puedes usar **Source** para ejecutar el archivo abierto completo,
manteniendo el directorio de la práctica. La ejecución por bloques ayuda a
explorar; el reinicio seguido de la ejecución completa comprueba las dependencias
entre pasos. No necesitas salir del IDE para esta comprobación.

Conserva el script, versiones, resultado de los controles y una explicación de
la interpretación fallida. Comprueba que la fuente conserva su contenido; el
ejecutor compara su huella antes/después. output/ está ignorado: no agregues con
fuerza bibliotecas, resultados de práctica o cachés a Git.

Si necesitas ejecutar fuera del IDE, la lección conserva una
[alternativa opcional con Rscript](../../../curriculum/07_tidyverse/01_tibbles_import_pipes/README.md#comprobacion-opcional-desde-terminal).
No es un requisito adicional del lab.

Responde con tus palabras: ¿qué conserva una tibble?, ¿qué garantiza leer sin
problemas?, ¿qué queda por validar?, ¿por qué la vista y la tabla tienen tamaños
distintos?, ¿qué aporta renv y qué comprobaste sobre los datos?

Puedes avanzar cuando ejecutes desde una sesión nueva, justifiques los cinco
tipos, conserves 001 y el faltante, compruebes 6 × 5 y 6000 MXN y expliques un
pipe sin depender de objetos previos. Registra evidencia y dudas en
[PROGRESS.md](../../../PROGRESS.md); no se acredita aprendizaje por existir la lección.

Siguiente: [07.02 — Seleccionar, filtrar y ordenar](../../../curriculum/07_tidyverse/README.md#02-seleccionar-filtrar-y-ordenar),
todavía planificada. Volver a la [lección 07.01](../../../curriculum/07_tidyverse/01_tibbles_import_pipes/README.md).
