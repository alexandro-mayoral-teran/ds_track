# 06 — R fundamental

## Propósito y prerrequisitos

Aprender el modelo de R sobre preguntas ya resueltas con Python. Completa el
cierre esencial de [05 — Python aplicado](../05_python_applied/README.md):
datos conocidos, indicadores conciliados, figura y ejecución reconstruible.
No se exige completar todas las ampliaciones de Python.

**Estado:** [06.01 — R, editor, scripts y paquetes](01_r_session/README.md)
dispone de lección, script ejecutable y lab.
[06.02 — Objetos, vectores y tipos](02_objects_vectors/README.md) añade ventas
vectorizadas, coerción y reciclaje con scripts y lab.
[06.03 — Seleccionar elementos](03_subsetting/README.md) incorpora posiciones,
nombres, máscaras y operadores, con script y lab.
[06.04 — Lógica y valores faltantes](04_logic_missing/README.md) añade condiciones,
grupos pendientes y resúmenes con cobertura, con script y lab.
[06.05 — Listas y data frames](05_lists_data_frames/README.md) incorpora listas,
tablas, selección por filas/columnas y modificación de copia con recálculo.
[06.06 — Funciones y control de flujo](06_functions_control/README.md) añade
validación, cálculo y resumen reutilizables, decisiones y ciclos con scripts y lab.
[06.07 — Archivos y validación básica](07_files_validation/README.md) añade
CSV textual, reglas por registro, rechazos conservados y relectura de la exportación.
06.08–06.09 siguen planificadas;
sus enlaces de la tabla describen el alcance pendiente dentro de este documento.

Empezaremos con ventas pequeñas y luego reutilizaremos la cartera sintética.
R no se aprenderá traduciendo mecánicamente líneas de pandas: compararemos
estructuras, reglas y resultados. RStudio será un editor opcional; el intérprete
R es necesario. 06.01–06.07 se comprobaron con R 4.6.1 y paquetes incluidos; la versión
efectiva se registra por sesión. Las dependencias posteriores se fijarán al implementarlas.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [R, editor, scripts y paquetes](01_r_session/README.md) | Esencial | Ejecutar un script e identificar su sesión |
| 2 | [Objetos, vectores y tipos](02_objects_vectors/README.md) | Esencial | Representar datos y explicar coerciones |
| 3 | [Seleccionar elementos](03_subsetting/README.md) | Esencial | Distinguir posiciones, nombres y estructuras |
| 4 | [Lógica y valores faltantes](04_logic_missing/README.md) | Esencial | Aplicar condiciones con tratamiento explícito de NA |
| 5 | [Listas y data frames](05_lists_data_frames/README.md) | Esencial | Construir y consultar registros tabulares |
| 6 | [Funciones y control de flujo](06_functions_control/README.md) | Esencial | Separar una transformación de su presentación |
| 7 | [Archivos y validación básica](07_files_validation/README.md) | Esencial | Leer, validar y escribir sin alterar la fuente |
| 8 | [Proyectos y dependencias con renv](#08-proyectos-y-dependencias-con-renv) | Práctica | Conservar y restaurar paquetes del proyecto |
| 9 | [Reproducir un resultado conocido](#09-reproducir-un-resultado-conocido) | Práctica de cierre | Conciliar conteos e indicadores con Python |

## Alcance de cada sección

<a id="01-r-editor-scripts-y-paquetes"></a>

### 01 — R, editor, scripts y paquetes

- Distinguir intérprete, consola, script .R y editor; ejecutar desde consola y
  Rscript. Help, sessionInfo, instalación frente a library y uso de paquete::función.
- [Lección disponible](01_r_session/README.md) y
  [lab 06.01](../../labs/06_r_foundations/01_r_session/README.md): ejecutar una venta,
  identificar versión/instalación/directorio/bibliotecas y repetir en una sesión
  nueva sin .RData. RStudio opcional, ayuda y paquetes incluidos, sin instalaciones.

<a id="02-objetos-vectores-y-tipos"></a>

### 02 — Objetos, vectores y tipos

- Asignación con <-, c, length, typeof y class; vectores numéricos, enteros,
  lógicos y de texto. Operaciones vectorizadas, coerción y reciclaje de longitudes.
- [Lección disponible](02_objects_vectors/README.md) y
  [lab 06.02](../../labs/06_r_foundations/02_objects_vectors/README.md): calcular
  cuatro ventas, comprobar tipos/longitudes y detectar coerción, truncamiento,
  reciclaje silencioso y parcial. Separar cálculo correcto de demostraciones
  incorrectas; no asumir semántica de listas de Python ni unión por claves.

<a id="03-seleccionar-elementos"></a>

### 03 — Seleccionar elementos

- Posiciones desde 1, nombres, selección lógica y diferencia entre [, [[ y $.
  Preservar dimensiones cuando corresponda; columnas y filas se explican en 05.
- [Lección disponible](03_subsetting/README.md) y
  [lab 06.03](../../labs/06_r_foundations/03_subsetting/README.md): seleccionar
  ventas conservando correspondencia, nombres y tipo/longitud. Vista mínima de
  lista para contrastar contenedor/contenido; matrices y drop opcionales.
  Vacío/faltante/error y modificación de copia; no equiparar operadores con Python.

<a id="04-logica-y-valores-faltantes"></a>

### 04 — Lógica y valores faltantes

- Comparaciones, vectores lógicos, & frente a &&, | frente a ||; NA, is.na y
  propagación de faltantes. Diferenciar NA, NULL, NaN y cero en casos pequeños.
- [Lección disponible](04_logic_missing/README.md) y
  [lab 06.04](../../labs/06_r_foundations/04_logic_missing/README.md): ampliar las
  cuatro ventas con dos casos incompletos, separar cumplen/no cumplen/pendientes
  y conciliar conteos. any/all, cortocircuito escalar, cobertura y na.rm explícitos;
  distinguir cero observado de suma vacía y conservar fuentes al confirmar un dato.

<a id="05-listas-y-data-frames"></a>

### 05 — Listas y data frames

- Listas con elementos de tipos distintos; data.frame, nombres, dimensiones y str.
  Seleccionar una columna como vector frente a mantener una tabla.
- [Lección disponible](05_lists_data_frames/README.md) y
  [lab 06.05](../../labs/06_r_foundations/05_lists_data_frames/README.md): reconstruir
  seis ventas, distinguir columna vector y tabla, conservar pendientes y modificar
  una copia con recálculo. Reciclaje, nombres exactos y vacío comprobados; matrices
  como comparación opcional, sin paquetes externos.

<a id="06-funciones-y-control-de-flujo"></a>

### 06 — Funciones y control de flujo

- function, argumentos, retorno explícito o último valor y alcance local básico.
  if requiere una condición escalar; for y alternativas vectorizadas cuando procedan.
- [Lección disponible](06_functions_control/README.md) y
  [lab 06.06](../../labs/06_r_foundations/06_functions_control/README.md): funciones
  sin datos globales, validación con stop, resumen con cobertura y casos sin base.
  Separa definiciones, ejecución y presentación; for con secuencia segura y
  multiplicación vectorizada. tryCatch para una falla esperada como extensión.

<a id="07-archivos-y-validacion-basica"></a>

### 07 — Archivos y validación básica

- Rutas relativas al proyecto, read.csv/write.csv, codificación y separadores.
  Registrar tipos esperados y evitar exportar nombres de fila como columna accidental.
- [Lección disponible](07_files_validation/README.md) y
  [lab 06.07](../../labs/06_r_foundations/07_files_validation/README.md): leer texto,
  comprobar estructura y reglas, conservar motivos y conciliar aceptados/rechazos.
  Exportar sin sobrescribir y releer identidad, notas e importes con cobertura.
  R base; imports con readr siguen en 07, sin instalaciones anticipadas.

<a id="08-proyectos-y-dependencias-con-renv"></a>

### 08 — Proyectos y dependencias con renv

- Carpeta de proyecto, archivos .R, librería de paquetes, renv.lock, snapshot y
  restore. Distinguir conservar paquetes de instalar R o guardar el estado de una sesión.
- Práctica prevista: restaurar el entorno de un proyecto pequeño y ejecutarlo desde
  cero; registrar también la versión de R. Reutilizar ese proyecto en tidyverse.

<a id="09-reproducir-un-resultado-conocido"></a>

### 09 — Reproducir un resultado conocido

- Integrar lectura, funciones, reglas, rechazos y resumen sobre la misma muestra
  y corte que Python; definir cómo comparar tipos, faltantes e importes.
- Práctica prevista: conciliar un conteo y un indicador, explicar diferencias y
  conservar instrucciones. Una gráfica inicial en ggplot2 llegará en el módulo 07.

## Prácticas y criterio de salida

Los labs 06.01–06.07 están disponibles con soluciones desplegables; 06.08–06.09 siguen previstos.
El cierre reutilizará el resultado Python como referencia y preparará el proyecto
03_portfolio_analysis_r, previsto en [proyectos](../../projects/README.md), sin
carpeta implementada todavía. No hay checkpoint activo asociado.

Podrás avanzar al ejecutar un análisis pequeño en una sesión nueva, explicar
vectores y tablas, tratar faltantes explícitamente y conciliar un resultado con
Python. Evaluación no estándar, entornos avanzados, S3/S4/R6 y metaprogramación
no bloquean tidyverse; se contemplan en el futuro R aplicado.

## Continuidad y lecturas

Comienza por [06.01](01_r_session/README.md). Después del cierre, continúa con
[07 — tidyverse](../07_tidyverse/README.md).

Fuentes: [manual introductorio de R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html),
[selección de estructuras en Advanced R](https://adv-r.hadley.nz/subsetting.html) y
[renv](https://rstudio.github.io/renv/articles/renv.html).
Consulta la [guía de libros abiertos de R](../../docs/r-reading-guide.md) para
ubicar estas referencias y las ampliaciones de Hadley Wickham.
