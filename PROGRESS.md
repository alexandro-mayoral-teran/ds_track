# Progreso de aprendizaje

Este archivo registra dónde estamos y qué sigue. El plan completo vive en
[`ROADMAP.md`](ROADMAP.md); aquí solo se actualiza el avance real.

## En este momento

- **Módulo activo de desarrollo:** `06_r_foundations`
- **Estado de desarrollo:** 06.01–06.08 implementadas; 06.09 conserva su plan.
- **Sesión de desarrollo:** 2026-10-17, desarrollo y revisión de 06.08.
- **Foco de desarrollo del material:** proyectos autocontenidos, bibliotecas locales y reconstrucción con renv.
  Próxima sección por implementar:
  [06.09 — Reproducir un resultado conocido](curriculum/06_r_foundations/README.md#09-reproducir-un-resultado-conocido), todavía planificada.
- **Estado del contenido:** nivel 0 disponible y las seis lecciones de Python
  fundamental con sus labs. Esto no acredita finalización del estudiante.
  Los módulos 02–05 tienen un plan de 39 secciones. Las diez de pandas y sus
  labs están disponibles; también SQL 03.01–03.09 con base local y labs.
  04.01–04.09 tienen lecciones y labs (04.08 opcional); 05.01 tiene lección,
  paquete local, script, notebook y lab. 05.02 añade argumentos, configuración
  JSON, logging y lab; 05.03 añade errores, recursos, JSON atómico y lab.
  05.04 añade lección, 21 pruebas unittest y lab; 05.05 añade tipos, contratos,
  revisión sin exportar, doce pruebas y lab. 05.06 añade clases/composición,
  dataclasses, trece pruebas y lab opcionales. 05.07 añade generadores, lotes
  conciliados, quince pruebas y lab de extensión. 05.08 añade funciones como
  valores, decoradores, trece pruebas y lab de extensión. 05.09 añade mediciones
  repetidas, memoria trazada, perfiles, trece pruebas y lab de extensión.
  05.10 añade páginas simuladas, normalización conciliada, dieciocho pruebas
  y lab de extensión. 05.11 integra ejecución y figura, verificación/reconstrucción,
  diez pruebas nuevas y lab de cierre. Las once secciones tienen material.
  Los módulos 06–08 tienen
  28 secciones y lecturas abiertas; 06.01–06.08 disponen de lecciones, scripts y labs,
  y las otras 20 siguen planificadas. Los módulos 09–10 tienen
  19 secciones planificadas y 11–14 añaden 37. La planificación de 02–14 está
  detallada; 02.01–02.10 ya disponen de lección y lab dentro de esos módulos.
- **Referencia de estudio, pendiente de evidencia:** leer la
  [lección de modelo relacional y SQLite](curriculum/03_sql_databases/01_relational_sqlite/README.md) y realizar
  el [lab 03.01](labs/03_sql_databases/01_relational_sqlite/README.md), después de
  completar las prácticas previas.

### Para retomar el desarrollo

El último material disponible es
[06.08 — Proyectos y dependencias con renv](curriculum/06_r_foundations/08_projects_renv/README.md)
con su [lab](labs/06_r_foundations/08_projects_renv/README.md).
Retomar con 06.09: integrar lectura, funciones, reglas, rechazos y resumen sobre
la misma muestra que Python; conciliar conteos e indicadores con contrato explícito
de tipos, faltantes e importes. Reutilizar las copias de práctica, sin traducir
Python línea por línea ni anticipar la primera figura de ggplot2 del módulo 07.
Mantener separados cierre del material y evidencia de aprendizaje del estudiante.

06.08 añade preparar_proyecto.R y plantilla con DESCRIPTION, renv.lock y activador
generado por renv. Copia funciones/CSV de 06.06/06.07 en R/ y datos/ de una carpeta
nueva. La biblioteca y el estado de la práctica quedan locales; --vanilla se
combina con activación explícita del perfil. withr presenta cuatro cifras
significativas temporalmente, sin redondear los CSV. Se conserva 14 = 8 + 6,
cobertura 6/8, suma observada 765.5 y total NA. Snapshot explícito conserva el
lockfile; restore prepara bibliotecas a partir de él. No se inicializó renv en
la raíz del repositorio ni se implementó el proyecto integrador pendiente.

Comprobado con R 4.6.1, renv 1.3.1 y withr 3.0.3 instalados localmente para
esta práctica. Restauraciones reales en copias independientes y sesiones nuevas;
cuatro CSV equivalentes. Retirar withr de una copia bloquea la ejecución antes
de exportar; restore recupera sin cambiar el lockfile ni los resultados. Opciones
de presentación restauradas también tras error. Activación incorrecta, destino
existente y ejecución desde otra carpeta rechazados. Snapshot y bloques de
lección/lab comprobados; fuentes anteriores y biblioteca del sistema conservadas.
Locale UTF-8 solo en procesos de revisión; sin modificar Conda, PATH o configuración
global de R. Los enlaces locales del sandbox renv de Windows requieren que la
revisión pueda leer los paquetes base de R; restricciones del ejecutor no se
corrigen desactivando las comprobaciones de renv. Python no se reejecutó.

Los proyectos y checkpoints asociados siguen pendientes. No se cambió el
estado del estudiante sin evidencia de las prácticas.

## Estados

- `No iniciado`: todavía no se trabaja el módulo.
- `En curso`: existe trabajo activo, aunque falten actividades.
- `En pausa`: se conserva el avance, pero no es el foco actual.
- `Completado`: se alcanzó el criterio de salida definido en el roadmap.

## Avance por módulo

Esta tabla registra el aprendizaje del estudiante según sus evidencias;
la disponibilidad del material se resume arriba y no modifica estos estados.

| Nivel | Módulo | Estado | Evidencia de finalización |
| --- | --- | --- | --- |
| 00 | Entorno de aprendizaje | En curso | Pendiente |
| 01 | Python fundamental | No iniciado | — |
| 02 | pandas | No iniciado | — |
| 03 | SQL y bases de datos | No iniciado | — |
| 04 | Visualización en Python | No iniciado | — |
| 05 | Python aplicado | No iniciado | — |
| 06 | R fundamental | No iniciado | — |
| 07 | tidyverse | No iniciado | — |
| 08 | Visualización en R | No iniciado | — |
| 09 | Arrow y Parquet | No iniciado | — |
| 10 | Polars y DuckDB | No iniciado | — |
| 11 | Reportes con Quarto | No iniciado | — |
| 12 | Streamlit | No iniciado | — |
| 13 | Shiny y fundamentos web | No iniciado | — |
| 14 | Proyecto reproducible | No iniciado | — |

## Bitácora

### 2026-10-17

- Se desarrolló 06.08 con lección, preparador, plantilla con lockfile real y lab:
  bibliotecas locales, activación explícita, snapshot/restore y reconstrucción.
  Documentación renv/withr y R4DS contrastada con las versiones usadas.
- Dos copias restauradas producen cuatro tablas equivalentes; paquete retirado
  recuperado sin alterar lockfile, entradas ni entregas previas. Índices,
  continuidad, arquitectura y lecturas actualizados. Sigue 06.09, todavía planificada.
  Recorrido predeterminado comprobado y 1,340 enlaces locales con sus fragmentos
  revisados; bloques y soluciones equilibrados.
  Sin cambios globales de configuración; estado del estudiante conservado y
  proyectos/checkpoints integradores pendientes.

- Se desarrolló 06.07 con lección, CSV propio, funciones, script y lab:
  lectura textual, reglas explícitas, aceptados/rechazos conciliados y exportación
  con relectura. R4DS y documentación de R contrastados con R 4.6.1 local.
- Ejemplos, fronteras, errores estructurales, no sobrescritura y cuatro variantes
  incorrectas comprobados. Índices, continuidad, arquitectura y lecturas actualizados;
  1,315 enlaces locales y sus fragmentos comprobados; bloques y soluciones equilibrados.
  Una falla de escritura simulada conserva carpeta parcial y propaga el error.
  Sigue 06.08, todavía planificada. Sin instalaciones ni cambios globales.
  Estado del estudiante conservado; proyectos/checkpoints siguen pendientes.

- Se desarrolló 06.06 con lección, funciones reutilizables, script de ejecución
  y lab con soluciones: argumentos/retorno/alcance, if, stop, for y tryCatch opcional.
  R4DS y Advanced R contrastados con documentación oficial y R 4.6.1 local.
- Ejemplos, errores separados, fronteras y cuatro variantes incorrectas comprobados;
  fuentes previas intactas. Índices, continuidad, arquitectura y lecturas actualizados.
  Se comprobaron 1,289 enlaces locales y sus fragmentos, bloques y soluciones cerradas.
  Sigue 06.07, todavía planificada; sin instalaciones ni cambios de entornos.
  Estado del estudiante conservado y proyectos/checkpoints aún pendientes.

- Se desarrolló 06.05 con lección, script y lab de soluciones desplegables:
  listas, data.frame, tipos/forma, selección, pendientes y copia con recálculo.
  Referencias de Wickham y documentación oficial contrastadas con R 4.6.1;
  sin paquetes externos ni cambios de entornos. Conservadas las muestras previas.
- Bloques de lección/lab ejecutados, dos errores intencionales por separado,
  resultados y fronteras comprobados. Cuatro variantes incorrectas detectadas
  por controles independientes; script repetido en procesos nuevos. Índices,
  continuidad, arquitectura y lecturas actualizados; enlaces/fragmentos y bloques
  revisados. Sigue 06.06, todavía planificada.
- Estado del estudiante conservado; proyectos/checkpoints siguen pendientes.

### 2026-10-16

- Se desarrolló 06.04 con lección, script y lab de soluciones desplegables:
  condiciones, lógica con NA, grupos conciliados y resúmenes con cobertura.
  Ejemplos, variantes, cortocircuito y fronteras comprobados con R 4.6.1;
  fuentes previas intactas, sin paquetes externos. Índices y continuidad actualizados.
- Material R disponible hasta 06.04; 06.05 sigue planificada. No se modificó el
  estado del estudiante ni se implementaron proyectos/checkpoints pendientes.
- Cierre de sesión: material 06.04 publicado en main, commit `cf65948`.
  Se ejecutaron los 18 bloques R de lección/lab y se comprobaron 1,258 enlaces
  locales sin problemas. Revisión final de índices, lecturas, arquitectura y
  continuidad; corregida la tabla del índice de labs y añadido el tiempo
  orientativo del lab 06.04. Retomar con 06.05, sin iniciar otra sección hoy.

### 2026-10-15

- Se desarrolló 06.03 con lección, script y lab: índices desde 1, orden/repetición,
  exclusión, nombres exactos y máscaras alineadas. Contrasta [, [[ y $ según
  objeto, tipo y contenido con una lista mínima explicada; matrices/drop opcionales.
  Incluye modificación de copia, vacíos/faltantes/errores, diagrama con lectura
  textual y soluciones razonadas. Advanced R y documentación oficial contrastados.
- Script ejecutado en dos procesos nuevos R 4.6.1 sin avisos. Se comprobaron valores,
  nombres/tipos/longitudes, selección 420, tres ventas positivas con total 660,
  variante 720 y soluciones del lab 360/620. Cinco errores deliberados devuelven
  código 1; también se verificaron índice decimal, máscara corta, nombres inexistentes,
  búsqueda parcial de $ y dimensiones opcionales. Bloques Markdown y soluciones
  ejecutados. Índice repetido y máscara corta se detectan contra selecciones
  manuales; el cambio de contenedor/contenido se observa en la salida. Scripts
  previos intactos, sin paquetes externos ni modificaciones de entornos.
- Índices, roadmap, arquitectura, lecturas y continuidad actualizados; enlaces,
  fragmentos, bloques y diff revisados. Sigue 06.04. Estado del estudiante sin
  nuevas evidencias ni proyectos acreditados; la colección Python conserva 115 métodos.

- Se desarrolló 06.02 con lección, dos scripts y lab: nombres/asignación,
  vectores atómicos, length/typeof/class, tipos comunes, operaciones por posición,
  suma, coerción y truncamiento. Distingue un factor único deliberado de precios
  incompletos y separa resultados correctos de demostraciones incorrectas.
  Incluye vacío frente a cero observado, límites de precisión, diagrama textual
  y soluciones razonadas. Advanced R como consulta puntual, con documentación
  oficial y sin exigir sus temas avanzados.
- Dos procesos nuevos del cálculo correcto conservan importes 300/240/0/120,
  total 660 y descuento 594. Se comprobaron tipos/clases/longitudes, ceros,
  vacío, coerción y conversión conservando entradas. Reciclaje 4/2 produce 900
  sin aviso; 4/3 produce 300/240/0/225 con aviso y código 0. Texto en aritmética
  falla con código 1. Bloques R de lección y soluciones ejecutados; variante
  del lab da 720/648 y precios desordenados 485. Copias con precio alterado o
  reciclaje silencioso fallan contra valores manuales. Scripts y muestra 06.01
  intactos, R 4.6.1 existente y ninguna instalación.
- Índices, roadmap, arquitectura, guía de lecturas y continuidad actualizados;
  enlaces locales/fragmentos/bloques y diff revisados. Sigue 06.03. La colección
  Python conserva sus 115 métodos, sin mezclarlos con evidencia de R. Estado del
  estudiante conservado sin evidencias nuevas ni proyectos acreditados.

- Se desarrolló 06.01: intérprete/editor/terminal, asignación y cálculo pequeño,
  archivo .R, print, source, Rscript, sesión nueva y paquetes incluidos. Lecturas
  selectivas de R4DS segunda edición con coautoría reconocida, contrastadas con
  documentación de R y Posit. Lección/lab, diagrama con lectura textual y ejemplos
  propios; renv/tidyverse siguen en sus secciones sin instalaciones anticipadas.
- Script ejecutado en dos procesos Rscript --vanilla con total 300 y sesión
  identificada. Variante y solución del lab producen 450. Caso de objeto oculto
  funciona tras source previo y falla en proceso nuevo; corrección comprobada.
  Muestras temporales .RData/.Rprofile/.Renviron no se cargan con --vanilla;
  error de sintaxis devuelve código no cero. Ayuda instalada consultable y bloques
  R válidos; archivo original intacto. R 4.6.1 existente, sin nuevas instalaciones.
- Índices, roadmap, arquitectura, guía de lecturas y continuidad de 05.11
  actualizados; enlaces locales/fragmentos/bloques y diff revisados. Sigue 06.02.
  Estado del estudiante conservado sin evidencias nuevas; material disponible
  no acredita aprendizaje ni completa los proyectos todavía pendientes.

- Se desarrolló 05.11 como cierre: recorrido completo de ejecución, verificación,
  reconstrucción desde copias y falla antes del cierre. Reutiliza la entrada de
  05.03; añade auditoría de solo lectura de tablas/Altair y propiedades de figuras.
  Incluye diagrama, referencias primarias, lab con soluciones y prueba de estructura.
  Las once lecciones/labs del módulo tienen material, sin acreditar aprendizaje.
- Pasaron 115 métodos combinados, diez con Python -O y once con la solución del
  lab en copia. Entrega original y reconstruida equivalentes; cinco tablas y
  20 controles, PNG 1920×880 revisado visualmente. Destino existente conserva
  sus archivos; falla before-close conserva carpeta parcial sin marcador, y
  verificación falla sin repararla. Fuentes originales intactas. Copias aisladas
  detectaron omisión de tablas, uso de ruta original en vez de copia y omisión
  de especificación. También se comprobaron corte vacío, registros incoherentes,
  tabla/fuente alterada, figura truncada y SVG inválido.
- Índices, navegación, roadmap y arquitectura actualizados; continuidad desde
  lecciones/labs anteriores al cierre disponible y siguiente desarrollo 06.01.
  Enlaces, fragmentos, bloques y diff revisados. Entorno existente, sin instalaciones
  ni cambios al lockfile. Proyectos/checkpoints siguen pendientes y el estado del
  estudiante se conserva sin agregar evidencias personales.

- Se desarrolló 05.10 como extensión: solicitud HTTP/GET, estados, cabeceras,
  JSON frente a contrato de datos, paginación, límites y política explícita de
  reintentos. Muestras propias de las 48 observaciones anteriores en tres páginas,
  cuatro escenarios, configuración local, tabla tipada y conciliación con CSV.
  Incluye diagrama con lectura textual, referencias primarias y lab con soluciones.
- Pasaron 105 métodos combinados, dieciocho con Python -O y diecinueve con la
  solución del lab en copia. Ejemplos Markdown y cuatro escenarios comprobados;
  errores tardíos/JSON inválido no crean carpetas de resultados. Dos escenarios
  exitosos conservan 48 filas, cinco indicadores y 20 controles. Se comprobaron
  no sobrescritura, max_pages=1 sin segunda solicitud, fuentes intactas y ausencia
  de rutas personales en evidencia. No hubo consultas de red ni esperas reales.
- Pruebas de HTTP sustituyen urlopen y verifican solicitud GET, timeout, bytes,
  UTF-8 y cierre de respuesta/HTTPError incluso ante lectura interrumpida. Cubren
  duplicados globales, segmento cambiante, esquema, JSON no estándar, vacío,
  cero/ausencia, precisión Int64, errores y agotamiento. Copias aisladas detectaron
  claves olvidadas entre páginas, reintento indebido de 401 y respuesta sin cerrar.
  Importaciones sin salida ni configuración del logging raíz; entorno existente,
  sin instalaciones ni cambios al lockfile. Índices, navegación, roadmap,
  arquitectura, enlaces, bloques y diff revisados. Sigue 05.11, aún planificada;
  estado del estudiante conservado sin nuevas evidencias personales.

- Se desarrolló 05.09 como extensión: frontera, tiempo transcurrido, repeticiones,
  calentamiento/orden alterno, memoria trazada frente a RSS, perfiles de llamadas
  y crecimiento según tamaño/diversidad. Compara alternativas de validación con
  resultados/errores conservados, separa instrumentos y registra límites.
  Incluye diagrama con lectura textual, referencias primarias y lab con soluciones.
- Pasaron 87 métodos combinados, trece nuevos con Python -O y catorce con la
  solución del lab en copia. Ejemplos Markdown ejecutados; dos recorridos del
  script con cinco/dos repeticiones y evidencia comprobada. Fuentes intactas,
  rechazo de salida existente sin sobrescribir, parámetros inválidos sin crear
  carpeta e importaciones sin salida/instrumentación. Copias aisladas detectaron
  conteo incorrecto de repetidas, calentamiento omitido, trazado sin cerrar e
  iterador agotado en la preparación del lab. Se comprobó el perfil ajeno real de
  CPython 3.12 además de sys.setprofile, sin cambiar sesiones ajenas.
- Índices, navegación, roadmap y arquitectura actualizados. Enlaces locales,
  fragmentos, bloques Markdown y git diff --check revisados; se reutilizó
  .venv-altair-review sin instalaciones ni cambios al lockfile. Sigue 05.10
  como extensión y 05.11 permanece planificado. Estado del estudiante conservado
  sin nuevas evidencias personales; desarrollar material no acredita aprendizaje.

- Se desarrolló 05.08 como extensión: funciones como valores, callbacks,
  funciones anidadas/cierre, reenvío de argumentos, @, wraps y metadatos.
  Registro de inicio/fin/falla alrededor del análisis conocido, con errores
  conservados y límites de generadores/caché. Incluye diagrama y lectura textual,
  ejemplos propios y lab con soluciones razonadas y prueba de efecto único.
- Pasaron los 74 métodos combinados (61 previos y 13 nuevos), catorce con la
  solución del lab en copia y trece con Python -O. Ejemplos Markdown ejecutados;
  nueve combinaciones de corte/tamaño equivalentes a lectura completa. Fuentes
  intactas e importaciones sin ejecución/mensajes ni cambios al logging raíz.
  Copias temporales detectaron pérdida de retorno, ocultación de error y falta
  de metadatos. Se comprobaron causa, identidad, retorno None, interrupciones,
  rechazo de funciones generadoras/async y no consumo de iteradores retornados.
  Se reutilizó .venv-altair-review sin instalaciones ni cambios al lockfile.
- Índices, roadmap, arquitectura y continuidad actualizados; enlaces locales,
  fragmentos y bloques Markdown comprobados. Sigue 05.09 como extensión;
  05.11 permanece planificado. Estado del estudiante conservado sin añadir
  evidencias personales; desarrollar el material no acredita aprendizaje.

- Se desarrolló 05.07 como extensión: iterables/iteradores, consumo compartido,
  agotamiento, yield, expresiones generadoras, errores diferidos, islice y lotes.
  Incluye CSV con cierre explícito, indicadores por lotes conciliados, diagrama
  con lectura textual e inventario de memoria, sin prometer memoria constante.
  Lab con soluciones razonadas y prueba propia del último lote.
- Pasaron los 61 métodos combinados (21/12/13 previos y 15 nuevos), dieciséis
  con la solución del lab en copia y quince con Python -O. Se ejecutaron los
  ejemplos Markdown; nueve combinaciones de corte/tamaño de fuentes originales
  coinciden con la lectura completa. Fuentes intactas y archivos cerrados en
  éxito/falla. Copias temporales detectaron pérdida del último lote, olvido de
  claves entre lotes y exclusión de cero. Se comprobaron errores tardíos fuera
  del corte, campos faltantes/adicionales, comillas sin cierre, vacíos y rangos.
  Se reutilizó .venv-altair-review, sin instalaciones ni cambios al lockfile.
- Índices, navegación, roadmap y arquitectura actualizados; enlaces locales,
  fragmentos y bloques Markdown revisados. Sigue 05.08 como extensión;
  05.11 permanece planificado y el estado del estudiante se conserva sin
  evidencias nuevas. El desarrollo del material no acredita aprendizaje.

- Se desarrolló 05.06 como ampliación opcional: función/diccionario/clase,
  instancias, __init__, self, métodos, alias, atributos compartidos y propios;
  dataclasses, __post_init__, frozen, fábricas y replace. Incluye diagrama de
  composición y lectura textual, ejemplos propios y lab con soluciones razonadas.
- Pasaron los 46 métodos combinados (21 de 05.04, 12 de 05.05 y 13 nuevos),
  los 14 de la solución del lab en copia y los 13 nuevos con Python -O.
  Se comprobaron ejemplos Markdown de listas compartidas/propias, igualdad y
  frozen superficial. Nueve combinaciones de cortes/selecciones de la fuente
  original produjeron tablas idénticas a la función; fuentes intactas. Copias
  temporales detectaron tupla vacía tratada como todos, corte ignorado y fecha
  no validada. Se reutilizó .venv-altair-review, sin instalaciones ni cambios
  al lockfile. La revisión de código no acredita aprendizaje del estudiante.
- Se actualizaron índices, continuidad, roadmap y arquitectura; enlaces locales,
  fragmentos y bloques Markdown comprobados. Sigue 05.07 como extensión;
  el cierre esencial 05.11 todavía está planificado. Se conserva el estado del
  estudiante sin añadir evidencias personales.

- Se desarrolló 05.05 con explicación gradual de firmas, uniones, retorno None,
  argumentos predeterminados/por nombre, docstrings, pre/postcondiciones y
  estructura de tablas. Distingue documentación, análisis estático, validación
  y pruebas. Añade revisión de segmentos sin exportar y lab con soluciones.
- Se comprobaron doce métodos nuevos y los veintiuno de 05.04; la solución del
  lab pasó con trece y los doce pasan también con Python -O. Copias temporales
  detectaron [] tratado como None, texto vacío como fecha omitida y bool como
  conteo. Comparadas con la versión anterior: tablas y especificaciones Altair
  idénticas para dos cortes y uno vacío; consumidores 05.01/05.02/05.03 ejecutados
  en destinos temporales, con fuentes anteriores intactas. Se reutilizó el
  entorno .venv-altair-review sin instalaciones ni cambios al lockfile.
- Se actualizaron índices, roadmap, arquitectura y continuidad. Enlaces locales,
  fragmentos y bloques Markdown revisados. Sigue 05.06 opcional; 05.11 continúa
  planificado. El estado del estudiante se conserva sin nuevas evidencias.

- Se desarrolló 05.04: explicación gradual de resultados esperados, unittest,
  clases mínimas de TestCase, fixtures, comparación de tablas y límites de las
  pruebas frente a la validación de cada ejecución. Incluye 21 métodos sobre el
  paquete compartido, entradas temporales y lab con soluciones razonadas; su
  ejercicio añade el método 22 sin entregarlo ya integrado en la suite inicial.
- Se comprobaron ceros, medio MXN, mediana impar, ausencias, vacíos, tipos,
  claves, fechas, negativos, conservación de entradas/archivos, JSON anterior,
  causa del error, reconstrucción y tres fallas sin cierre. En copias temporales,
  mediana sustituida por promedio, denominador incorrecto y exclusión de cero
  provocan fallas. La solución del lab pasó con 22 métodos; fuentes originales
  conservaron sus bytes e indicadores 24/21/2300/87,5. La revisión reutiliza
  Python 3.12.12 y .venv-altair-review, sin instalaciones. Los temporales de
  revisión se ubicaron en output local por los permisos del sandbox.
- Se actualizaron índices, enlaces de continuidad, roadmap y arquitectura;
  se comprobaron enlaces/fragmentos y bloques Markdown. Retomar con 05.05,
  todavía planificada. No se modificó la evidencia de aprendizaje del estudiante.

### 2026-10-14

- Cierre final del día: material 05.01–05.03 publicado en main mediante
  los commits 8a3c4ea, 8428187 y 54db292. Retorno acordado: 05.04,
  todavía planificada. AGENTS.md permanece local e ignorado; entorno y
  salidas de revisión se conservan localmente, fuera de Git. No se modificó
  la evidencia de aprendizaje del estudiante.

- Se cerró la sesión con 05.03: explicación gradual de excepciones, causa,
  propagación, with/finally, conexión/transacción y reemplazo atómico de JSON.
  Añade consumidor con cierre final después del registro y tres fallas didácticas,
  conserva parciales y consumidores anteriores. Lab con soluciones razonadas,
  recursos cerrados, archivo anterior preservado y reconstrucción comprobada.
  Se verificaron fallas de serialización/escritura/limpieza, interrupción y
  errores inesperados; tablas, ausencias y figuras conservadas. Se actualizaron
  índices, arquitectura, continuidad y retorno a 05.04. No se acreditó aprendizaje.

- Se desarrolló 05.02 con argumentos, configuración JSON, precedencia,
  bases de rutas y logging. Añade una entrada configurable al paquete de 05.01,
  conservando el consumidor original. Cada entrega registra valores efectivos,
  procedencia, reglas y versiones; lab con comparación de dos cortes y soluciones.
  Se verificaron parámetros, niveles, rutas, errores antes de exportar,
  reconstrucción y falla del registro final; tablas equivalentes al análisis
  previo y fuentes/entregas intactas. Figuras revisadas y navegación actualizada.
  Sigue 05.03; no se acreditó aprendizaje ni se instalaron dependencias nuevas.

- Se desarrolló 05.01: módulo pequeño, explicación de importaciones/nombres,
  main/__main__, paquetes regulares, búsqueda de código frente a rutas de datos
  y caché del kernel. El análisis de 04.09 se organiza en un paquete local
  con entrada, transformación, comprobación, presentación y flujo; script y
  notebook reutilizan las mismas funciones. Lab gradual con soluciones razonadas.
  Se verificaron equivalencia con el cierre, fronteras, conservación de entradas
  y entregas, reconstrucción, importaciones y entradas completas. Notebook
  ejecutado desde kernel nuevo; figuras revisadas. Índices, continuidad,
  roadmap y arquitectura actualizados. Sigue 05.02, todavía planificada;
  el estado del estudiante se conserva sin nuevas evidencias.

### 2026-10-13

- Se desarrolló 04.09: entrega de medianas/cobertura con figuras Matplotlib
  y Altair, referencia independiente CSV, veinte conciliaciones, fuentes
  conservadas, informe e instrucciones de reconstrucción. Lab con soluciones
  y revisión acompañada; interacción y HTML sin conexión siguen opcionales.
  Se comprobaron fuentes/carpeta intactas, reconstrucción, vacíos, ausencias,
  ceros y fallas. Se corrigieron etiquetas monetarias compartidas para conservar
  medianas de medio MXN sin redondearlas a cero. Figuras y HTML revisados;
  navegación y arquitectura actualizadas. El módulo 04 tiene nueve secciones
  disponibles; sigue 05.01 planificada. No se acreditó aprendizaje sin evidencia.

- Se desarrolló 04.08 como extensión opcional: parámetro variable con menú,
  selección de segmento, condiciones de opacidad/borde y filtro por intervalo.
  Incluye tres HTML, tablas de bases, capturas curadas y lab con soluciones.
  Se verificaron medianas, pares y exclusiones desde CSV, ausencia/cero/vacío,
  exportaciones y fuentes conservadas; controles, limpieza, contador e HTML
  sin red en Edge. No agrega dependencias; referencias de 04.07 reutilizadas.
  Se actualizaron navegación, arquitectura e índices. Sigue 04.09;
  la disponibilidad del material no acredita aprendizaje del estudiante.

- Se completó 04.07 desde el borrador conservado: explicación de Chart,
  marcas, canales N/O/Q/T, composición, agregación y exportación; lab con
  soluciones razonadas y cuatro figuras curadas. Se conciliaron medianas,
  pares y tramos contra CSV originales; se comprobaron fronteras, vacíos,
  ausencias, cero, esquema, agregación renderizada y entregas conservadas.
  HTML sin conexión comprobado en Edge; referencias Altair 6.3.0, pandas
  2.3.3, Matplotlib 3.10.7 y vl-convert-python 1.9.0.post1 ejecutadas.
  Se actualizaron índices, arquitectura y navegación. Sigue 04.08 opcional;
  el avance del material no acredita aprendizaje del estudiante.

- Antes de retomar, se pausó la sesión a petición del usuario durante 04.07.
  Se conservaron investigación, dependencias, script y lección en borrador
  sin commit ni push. El lab y la verificación final se completaron al retomar.

- Se desarrolló 04.06 con explicación ampliada: composición por pregunta, ejes
  comunes o unidades distintas, anotaciones, espacio, pulgadas/píxeles/dpi,
  PNG/SVG y guardado/cierre explícitos. Incluye dos composiciones, exportaciones
  a dos resoluciones, tablas, registro de formatos, lectura textual y lab razonado.
  Se comprobaron medianas/cobertura contra los CSV originales, coordenadas,
  casos vacíos/cero/ausencia, dimensiones PNG, SVG renderizado, conservación de
  fuentes/entregas y cierre sin afectar otras figuras. Runtime local: pandas
  2.3.3 y Matplotlib 3.10.6; referencia 3.10.7 conservada. Sigue 04.07;
  la disponibilidad del material no acredita aprendizaje del estudiante.

- Se desarrolló 04.05: límites y origen de barras, escala lineal/logarítmica,
  exclusiones trazables, unidades, cobertura, formas/tramas y descripción textual.
  Incluye cuatro figuras, cinco CSV reconstruibles y lab con soluciones razonadas.
  Se verificaron medianas contra los CSV originales, coordenadas, ceros, ausencias,
  vacíos, partición log y conservación de fuentes/salidas. Runtime local: pandas
  2.3.3 y Matplotlib 3.10.6; referencia 3.10.7 conservada. Sigue 04.06;
  la disponibilidad del material no acredita aprendizaje del estudiante.

- Se cerró la sesión con revisión documental: índices generales, navegación de
  visualización y punto de retorno a 04.05. Se completó el índice de labs SQL
  03.03–03.09 y se distinguieron material disponible, planes y evidencias del
  estudiante. Se comprobaron enlaces locales y fragmentos de los 109 documentos
  Markdown versionados fuera de las plantillas, junto con git diff --check.
  AGENTS.md permanece local e ignorado; no se versionan salidas de práctica.

- Se desarrolló 04.04: histogramas e intervalos, cuartiles/cajas/bigotes, valores
  exteriores y dispersión con pares conocidos, sin atribución causal. Incluye
  cuatro figuras, script con siete tablas de comprobación y lab con soluciones.
  Se verificaron frecuencias, cuartiles, coordenadas, exclusiones, fronteras,
  vacíos, ausencias/cero, exportaciones y fuentes intactas. Runtime local:
  pandas 2.3.3 y Matplotlib 3.10.6; referencia 3.10.7 conservada. Sigue 04.05;
  el material disponible no acredita aprendizaje.

### 2026-10-12

- Se desarrolló 04.03: barras agrupadas, medidas y denominadores, fechas, pares
  comparables y huecos sin imputación, con tres figuras y lab razonado. Se
  comprobaron sumas, tasas, pares, cero/ausencia, calendario, exportaciones y
  entradas intactas con pandas 2.3.3 y Matplotlib 3.10.6 locales; referencia
  Matplotlib 3.10.7 conservada. Sigue 04.04; el estudiante requiere evidencia.

- Se desarrolló 04.02: Figure/Axes/Axis, interfaz explícita, dibujo reutilizable,
  guardado y cierre, con resumen derivado de SQL, figuras y lab. Se verificaron
  ausencia/cero/vacío, aislamiento de figuras y conservación de entradas/salidas
  con pandas 2.3.3 y Matplotlib 3.10.6 locales, manteniendo referencia 3.10.7.
  El siguiente desarrollo es 04.03; el aprendizaje requiere evidencia.

- Se desarrolló 04.01: pregunta, público, población, unidad y medida; elección
  entre categorías, tiempo, distribución y relación. Se añadieron vistas propias
  con bases comprobadas, ficha y lab; la regeneración es opcional. Se revisaron
  figuras, ausencias, vacíos y conservación de entradas, con las bibliotecas locales
  disponibles. El siguiente desarrollo es 04.02; el aprendizaje requiere evidencia.

- Se desarrolló SQL 03.09: base reconstruible, read_sql_query parametrizado,
  referencia independiente desde CSV/pandas, tipos y conciliación de detalle/grupos;
  exportaciones recargadas y figura con cobertura. SQL tiene nueve lecciones y labs;
  el estudiante aún requiere evidencias. El siguiente desarrollo es 04.01.
  Se verificó con pandas 2.3.3 y Matplotlib 3.10.6 disponibles, contrastando la API
  de referencia 3.10.7; no se modificó el entorno local incompleto ni las dependencias.

- Se desarrolló SQL 03.08: copia separada, UPDATE/DELETE con selección previa,
  control explícito, commit/rollback, carga repetible y conflictos; lección amplia
  y lab con SAVEPOINT opcional. Se comprobó persistencia, reversión de lotes,
  relaciones, archivos existentes y conservación de fuentes. El siguiente
  desarrollo es 03.09; la disponibilidad del material no acredita aprendizaje.

- Se desarrolló SQL 03.07: OVER, particiones, ROW_NUMBER, LAG y marcos, con
  explicación gradual, diagramas y lab. Se comprobó la comparación de 19 pares
  conocidos, selección con empates, vacíos, huecos temporales y base cero;
  también se conciliaron acumulados y cobertura conservando las fuentes.
  El siguiente desarrollo es 03.08; el aprendizaje requiere evidencia.

- Se desarrolló SQL 03.06 con explicación gradual de subconsultas escalares, IN,
  EXISTS/NOT EXISTS, correlación, tablas derivadas y CTE por etapas; lab amplio
  con equivalencia y referencias globales/por grupo. Se contrastaron resultados
  con los CSV y se comprobaron NULL, vacíos y conservación de fuentes.
  El siguiente desarrollo es 03.07; el aprendizaje requiere evidencia.

- Se completó SQL 03.05: INNER/LEFT JOIN, cardinalidad, ON/WHERE, antiunión y
  claves compuestas, con diagramas, resumen regional y lab. Se conciliaron
  claves y valores contra los CSV y se verificaron casos sin correspondencia,
  multiplicación y vacíos conservando las entradas. El siguiente desarrollo
  es 03.06; la disponibilidad del material no acredita aprendizaje.

- Se desarrolló SQL 03.04: COUNT/SUM/AVG, grupos, HAVING, CASE, tasas y cobertura,
  con script de solo lectura y detalle temporal por segmento. Se conciliaron
  ocho grupos contra cálculos Python sobre los CSV y se comprobaron vacíos,
  desconocidos, cero y frontera 30. El siguiente desarrollo es 03.05;
  el borrador local de joins aún no está publicado ni cuenta como material disponible.

- Se desarrolló SQL 03.03: esquema, tipos y restricciones, INSERT con parámetros,
  carga desde los CSV existentes y lab con soluciones. Se comprobaron rechazos,
  persistencia, repetición sin cambios y conservación de entradas. El siguiente
  desarrollo es 03.04; el aprendizaje sigue pendiente de evidencia.

- Se desarrolló SQL 03.02: SELECT, filtros, alias, orden y desempates, LIMIT,
  DISTINCT, NULL y parámetros; script de solo lectura y lab con resultados conocidos.
  Se comprobó conservación de la base, fronteras y selecciones vacías. El siguiente
  desarrollo es 03.03; el avance del estudiante sigue pendiente de evidencia.

### 2026-10-11

- Se desarrolló SQL 03.01: modelo relacional, claves y relaciones con diagramas;
  base local de 16 clientes, 24 créditos y 48 cortes ficticios. Se verificaron
  restricciones, persistencia, repetición sin cambios y exploración de solo lectura.

- Se desarrolló pandas 02.10: análisis integrado, rechazos trazables, resumen
  conciliado, primera figura Matplotlib y notebook con funciones compartidas.
  Se completó el material de diez lecciones/labs; el aprendizaje requiere evidencia.

- Se desarrolló pandas 02.09: pivot, melt y pivot_table, con diagramas y
  conservación de presencia para distinguir celdas ausentes de importes desconocidos.
  Se verificó la vuelta exacta y el resumen por corte; se agregó lab y navegación.

- Se desarrolló pandas 02.08: concat, tipos de merge, validate, indicator y
  comparación por ID sobre una base común. Tres diagramas Mermaid explican las
  operaciones y la multiplicación de filas; se agregó lab con comprobaciones.

- Se desarrolló pandas 02.07 con 48 observaciones: groupby/agg, size/count/nunique,
  grupos con NA, cobertura y tasas con bases explícitas. Los 10 grupos se verificaron
  contra cálculos independientes; se agregó lab y transform como ampliación.

- Se desarrolló pandas 02.06 con 48 registros de dos cortes: normalización
  trazable, formatos temporales explícitos, NaT, relaciones de fechas y claves
  posteriores a la limpieza. Se agregó lab y comparación de períodos comprobada.

- Se desarrolló pandas 02.05: 44 registros sintéticos, reglas explícitas, claves
  repetidas apartadas para revisión y múltiples motivos por registro. El script
  concilia la partición y comprueba exportaciones; se agregó lab y navegación.

- Se desarrolló pandas 02.04 con 40 filas sintéticas: conversión trazable, tipos
  nullable, operaciones entre columnas, asignación con loc y conciliación sobre
  la misma base. Se agregó el lab con soluciones desplegables y navegación.

- Se desarrolló pandas 02.03: loc/iloc, máscaras, condiciones combinadas, NA,
  orden y desempates, con selección vacía y exportación comprobada. Se agregó
  el lab y se conservó la fuente de la lección anterior.

- Se desarrolló pandas 02.02 con muestra crediticia ficticia y diccionario: lectura
  tipada, head/info/describe, exportación y comparación de la tabla recargada.
  Se agregó su lab y se enlazó desde la primera lección.

- Se depuraron las instrucciones locales de agentes, separando reglas vigentes
  de historial. Se crearon plantillas generales de agentes y arquitectura, con
  instrucciones para copiarlas y adaptarlas a proyectos de otros temas.
- Se revisaron las instrucciones locales y el roadmap: estado real de pandas,
  alcances opcionales, proyectos aún por implementar y pendientes de R aplicado
  y terminal avanzada. Se alineó el flujo de estudio con checkpoints opcionales.

- Se investigaron y definieron Quarto (9 secciones), Streamlit (9), Shiny (10)
  y proyecto reproducible (9). El recorrido numerado completo tiene planes
  detallados; se retoma la implementación por pandas 02.02 en la siguiente sesión.

- Se investigaron fuentes oficiales y se organizaron Arrow/Parquet (9 secciones)
  y Polars/DuckDB (10), con intercambio Python/R, consultas verificables y mediciones.
  Se mantuvo la numeración y se separaron particiones y streaming como ampliaciones.

- Se investigaron libros abiertos de Hadley Wickham y documentación oficial para
  definir R fundamental (9 secciones), tidyverse (10) y visualización R (9).
  Se agregó una guía de lecturas y se mantuvo pendiente la numeración de R aplicado.

- Se desarrolló 02.01 — Series y DataFrame, con script y lab; pandas 2.3.3 se
  declaró en pyproject.toml y se resolvió en uv.lock. Se verificó el ejemplo
  en un entorno aislado y se actualizaron navegación y arquitectura.

- Se investigó documentación oficial y se organizaron las secciones de pandas (10),
  SQL (9), visualización Python (9) y Python aplicado (11), con prácticas y cierres
  propuestos. Se distinguió el recorrido esencial de las ampliaciones opcionales.
- Se desarrolló la lección 06 de Python fundamental y su lab: reglas, excepciones,
  rechazos trazables y resumen conciliado. El módulo dispone de seis lecciones;
  la finalización del aprendizaje sigue pendiente de evidencias.

- Se desarrolló la lección 05 de Python fundamental y su lab: lectura CSV,
  conversión, escritura y comprobación de registros e importes, conservando la entrada.
- Se revisaron las instrucciones locales, la arquitectura y los diagramas:
  flujo lección/lab, avances de contenido y diferencia entre muestras iniciales
  de ventas y dominio crediticio posterior.
- Se desarrolló la lección 04 de Python fundamental y su lab: parámetros,
  retorno, alcance y reutilización de filtros y resúmenes.
- Se desarrolló la lección 03 de Python fundamental: condiciones, recorrido,
  acumuladores y selección de registros, con script y lab verificables.
- Se desarrolló la lección 02 de Python fundamental y su lab: listas,
  diccionarios, registros, mutabilidad y copias.
- Se inició Python fundamental con la lección y lab de variables, tipos y
  operaciones. Se registró R aplicado como consideración para la próxima revisión.
- Se integraron las rutas en un flujo numerado 00–14; visualización y Python aplicado
  ahora tienen ubicación y prerrequisitos, con Streamlit/Shiny como elección de aplicación.

- Se revisó el track completo: comunicación y calidad tempranas, cierre integrado
  antes de R y separación de contenidos esenciales y avanzados sin renumerar niveles.
- Se creó la lección 06, el notebook de ejemplo y su lab: selección de kernel,
  celdas, estado en memoria y ejecución desde cero.
- Se dividió la lección 05 en dos sesiones: preparación del entorno y gestión
  de dependencias, con teoría específica de requirements.txt y archivos de configuración.
- Se separó la teoría de entornos de tres recorridos prácticos: Conda, venv + pip
  y uv, con una demostración común de instalación e importación de una biblioteca.
- Se adaptó la lección 05 a Anaconda/Conda como recorrido principal, con uv como
  alternativa y un solo entorno requerido en el lab.
- Se creó la lección 05 y su lab: intérpretes, venv, pip y entorno del proyecto
  con uv, conservando recorridos por shell y soluciones desplegables.
- Se desarrollaron las primeras tres lecciones y sus labs, con explicaciones
  por pasos y soluciones desplegables.
- Se preparó la lección 04 y un primer script sin paquetes externos; la
  preparación del entorno queda para la lección 05.
- Se creó el repositorio privado de DS Track y se publicó el material inicial.
- Se incorporó el perfil de GitHub como práctica inicial del nivel 0, con
  Markdown y actualización desde Git. La práctica de terminal se conserva.
- Se alineó la numeración con el orden de estudio y se agregó una plantilla
  editable para el README del perfil.
- Se separaron las lecciones 01 y 03: creación desde la web y actualización con
  Git, cada una con su propio documento y lab.

### 2026-10-08

- Se definió la arquitectura del repositorio.
- Se creó el roadmap por niveles.
- Se prepararon plantillas para módulos y proyectos.
- Se estableció la política de datos sintéticos.
- Se inició el módulo `00_getting_started`.
- Se creó la primera lección y su lab sobre terminal, rutas y entorno.
- Se agregaron equivalencias PowerShell–Unix para preparar el uso de Git,
  servidores y entornos de nube.

## Cómo actualizar este archivo

Al terminar una sesión:

1. Actualiza el siguiente paso con una acción pequeña y concreta.
2. Registra uno o dos resultados en la bitácora, no cada comando ejecutado.
3. Cambia un módulo a `Completado` solo cuando exista evidencia de su criterio
   de salida.
4. Enlaza la evidencia: ejercicio, script, notebook, reporte o proyecto.
