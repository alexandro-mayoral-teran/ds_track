# 06 — R fundamental

[Inicio](../../README.md) / [Módulos](../README.md) / **06 — R fundamental**

**Aprende el modelo de R comparando estructuras y resultados conocidos.**

[**Empezar por 06.01 →**](01_r_session/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 9 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Trabajar con objetos, vectores, tablas, funciones y archivos en R sobre preguntas conocidas. La comparación con Python se hace por contratos y resultados, no traduciendo cada línea.

## Antes de empezar

Completa el cierre esencial de [05 — Python aplicado](../05_python_applied/README.md); sus ampliaciones no son obligatorias. R es el intérprete necesario; RStudio o el IDE elegido facilitan editar, ejecutar bloques e inspeccionar objetos. La primera lección orienta la preparación.

## Qué vas a aprender

- Distinguir tipos, vectores, listas y tablas.
- Seleccionar elementos y tratar NA explícitamente.
- Separar validación y cálculo en funciones.
- Leer y exportar archivos conservando rechazos y cobertura.
- Reconstruir una práctica local y conciliar un resultado con Python.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **06.01** · [R, editor, scripts y paquetes](01_r_session/README.md) | [Lab 06.01](../../labs/06_r_foundations/01_r_session/README.md) | Ejecutar un script e identificar su sesión |
| **06.02** · [Objetos, vectores y tipos](02_objects_vectors/README.md) | [Lab 06.02](../../labs/06_r_foundations/02_objects_vectors/README.md) | Representar datos y explicar coerciones |
| **06.03** · [Seleccionar elementos](03_subsetting/README.md) | [Lab 06.03](../../labs/06_r_foundations/03_subsetting/README.md) | Distinguir posiciones, nombres y estructuras |
| **06.04** · [Lógica y valores faltantes](04_logic_missing/README.md) | [Lab 06.04](../../labs/06_r_foundations/04_logic_missing/README.md) | Aplicar condiciones con tratamiento explícito de NA |
| **06.05** · [Listas y data frames](05_lists_data_frames/README.md) | [Lab 06.05](../../labs/06_r_foundations/05_lists_data_frames/README.md) | Construir y consultar registros tabulares |
| **06.06** · [Funciones y control de flujo](06_functions_control/README.md) | [Lab 06.06](../../labs/06_r_foundations/06_functions_control/README.md) | Separar una transformación de su presentación |
| **06.07** · [Archivos y validación básica](07_files_validation/README.md) | [Lab 06.07](../../labs/06_r_foundations/07_files_validation/README.md) | Leer, validar y escribir sin alterar la fuente |
| **06.08** · [Proyectos y dependencias con renv](08_projects_renv/README.md) | [Lab 06.08](../../labs/06_r_foundations/08_projects_renv/README.md) | Conservar y restaurar paquetes del proyecto |
| **06.09** · [Reproducir un resultado conocido](09_known_result/README.md) | [Lab 06.09](../../labs/06_r_foundations/09_known_result/README.md) | Conciliar conteos e indicadores con Python |

<a id="alcance-de-cada-sección"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

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
- [Lección disponible](08_projects_renv/README.md) y
  [lab 06.08](../../labs/06_r_foundations/08_projects_renv/README.md): preparar copias
  con fuentes, datos y lockfile, restaurar paquetes locales y comparar resultados.
  Distinguir activación, snapshot/restore y ejecución; withr para presentación
  temporal. Organización reutilizable en tidyverse, sin instalarlo por anticipado.

<a id="09-reproducir-un-resultado-conocido"></a>

### 09 — Reproducir un resultado conocido

- Integrar lectura, funciones, reglas, rechazos y resumen sobre la misma muestra
  y reglas que Python; definir cómo comparar tipos, faltantes e importes.
- [Lección disponible](09_known_result/README.md) y
  [lab 06.09](../../labs/06_r_foundations/09_known_result/README.md): referencia Python
  independiente, tablas/indicadores conciliados, exportación releída y verificador
  de solo lectura. Copia autocontenida, tolerancia explícita y entradas conservadas.
  Una gráfica inicial en ggplot2 llegará en el módulo 07.

</details>

## Cómo trabajar este módulo

Trabaja principalmente en el proyecto y la consola R de tu IDE. Ejecuta bloques para explorar y después reinicia la sesión para comprobar el script completo. 06.08 introduce renv en copias locales; no lo inicialices en la raíz del curso ni cambies bibliotecas globales. Objetos avanzados S3/S4/R6 y metaprogramación no bloquean tidyverse.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Scripts y funciones R | Tipos, selección, reglas y resultados |
| Archivos aceptados y rechazados | Reconstrucción y cobertura de la entrada |
| Proyecto y nota Python/R | Entorno local y comparación del mismo contrato |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-y-criterio-de-salida"></a>

## Criterio de salida

Puedes ejecutar un análisis pequeño en una sesión nueva, explicar vectores/tablas y valores faltantes, y conciliar el resultado con Python. Conserva instrucciones de entorno y distingue consola R de terminal del sistema.

03_portfolio_analysis_r sigue previsto en [proyectos](../../projects/README.md), sin carpeta implementada ni checkpoint activo.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Podrás avanzar al ejecutar un análisis pequeño en una sesión nueva, explicar
vectores y tablas, tratar faltantes explícitamente y conciliar un resultado con
Python. Evaluación no estándar, entornos avanzados, S3/S4/R6 y metaprogramación
no bloquean tidyverse; se contemplan en el futuro R aplicado.

</details>

<a id="continuidad-y-lecturas"></a>

## Siguiente paso

**Para empezar:** [lee 06.01](01_r_session/README.md) y realiza su lab.

**Al cerrar:** continúa con [07 — tidyverse](../07_tidyverse/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Fuentes: [manual introductorio de R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html),
[selección de estructuras en Advanced R](https://adv-r.hadley.nz/subsetting.html) y
[renv](https://rstudio.github.io/renv/articles/renv.html).
Consulta la [guía de libros abiertos de R](../../docs/r-reading-guide.md) para
ubicar estas referencias y las ampliaciones de Hadley Wickham.

### Apoyos relacionados

- [07.01 — Tibbles, importación y pipes](../07_tidyverse/01_tibbles_import_pipes/README.md)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_r_session/README.md)
