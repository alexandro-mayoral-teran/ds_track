# Progreso de aprendizaje

Este archivo registra dónde estamos y qué sigue. El plan completo vive en
[`ROADMAP.md`](ROADMAP.md); aquí solo se actualiza el avance real.

## En este momento

- **Módulos con desarrollo de sus secciones cerrado:** `06_r_foundations`, `07_tidyverse` y `08_visualization_r`; proyecto/checkpoints pendientes.
- **Módulo en desarrollo:** `09_arrow_parquet`: 09.01 disponible; 09.02–09.09 todavía planificadas.
- **Estado de desarrollo:** 06.01–06.09, 07.01–07.10, 08.01–08.09 y 09.01 implementadas; 09.02–09.09 y 10–14 conservan sus planes.
- **Sesión de desarrollo:** 2026-10-21, desarrollo y comprobación de 09.01; cierre de sesión documentado.
- **Foco actual:** CSV/Parquet, representación Arrow, bibliotecas y medidas de disco/memoria.
  Próximo paso: desarrollar
  [09.02 — Esquemas y tipos entre lenguajes](curriculum/09_arrow_parquet/README.md#02-esquemas-y-tipos-entre-lenguajes), todavía planificada.
  Los [pendientes de cierre](docs/storage-closure.md) separan material, práctica e integración.
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
  28 secciones y lecturas abiertas; 06.01–06.09 disponen de lecciones, scripts y labs,
  también 07.01–07.10 y 08.01–08.09. Los módulos 09–10 tienen
  19 secciones: 09.01 disponible y las otras 18 planificadas; 11–14 añaden 37 previstas. La planificación de 02–14 está
  detallada; 02.01–02.10 ya disponen de lección y lab dentro de esos módulos.
- **Referencia de estudio, pendiente de evidencia:** leer la
  [lección de modelo relacional y SQLite](curriculum/03_sql_databases/01_relational_sqlite/README.md) y realizar
  el [lab 03.01](labs/03_sql_databases/01_relational_sqlite/README.md), después de
  completar las prácticas previas.

### Para retomar el desarrollo

**Criterio de autoría acordado:** en R, priorizar RStudio o el IDE elegido,
scripts y ejecución por bloques; terminal/Rscript solo cuando aporten al objetivo
o como alternativa opcional. Distinguir consola R de terminal. Aplicar desde el
material nuevo. 07.01 y su lab ya se ajustaron; 07.02–07.10 nacen con ese recorrido. Revisar las demás lecciones
implementadas posteriormente con el usuario.

La última sección desarrollada es
[09.01 — CSV, Parquet y Arrow](curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md),
con [script Python](curriculum/09_arrow_parquet/01_csv_parquet_arrow/inspeccionar_formatos.py),
[script R](curriculum/09_arrow_parquet/01_csv_parquet_arrow/inspeccionar_formatos.R),
[muestra e inventario](curriculum/09_arrow_parquet/01_csv_parquet_arrow/datos/README.md)
y [lab](labs/09_arrow_parquet/01_csv_parquet_arrow/README.md).
La sesión queda cerrada con el estado real y los
[pendientes para cerrar almacenamiento](docs/storage-closure.md). Retomar con
[09.02 — Esquemas y tipos entre lenguajes](curriculum/09_arrow_parquet/README.md#02-esquemas-y-tipos-entre-lenguajes):
contrato de tipos/nulabilidad, casos separados de NA/null/vacío/cero, fechas,
ID textual, unidades, rango y precisión. No instalar paquetes todavía.

09.01 contiene CSV/Parquet reales de los mismos 14 IDs: 28 × 3, dos cortes de
14 registros y 29000/31800 MXN. Generados desde las reglas y fuente anteriores;
original R y referencia Python conciliados observación por observación. CSV de
593 bytes y Parquet de 1668; 420 bytes lógicos de buffers de tabla Arrow no se
presentan como RAM del proceso. Esquema string/date32/int32 no anulable, dos
grupos de filas y Snappy; evidencia de autoría con PyArrow 21.0.0 ya existente,
sin incorporarlo a pyproject/uv.lock ni al renv. Esencial comprobado sin paquetes
externos (Python -S y R base); opcional sí decodifica Parquet y compara por clave.
Python 3.12.12/R 4.6.1; bloques de lección/lab desde procesos nuevos. Vacío,
ceros, fronteras, fechas inválidas, repeticiones, faltantes y enteros fuera de
rango comprobados en ambos lectores. Una firma PAR1 falsa pasa el control
parcial con inventario alterado, pero falla el lector real; tipo incorrecto se
rechaza y orden distinto se acepta por clave. Son límites explícitos del
inspector, no una afirmación de validación completa. Huellas/atributos LF y
binario conservan la muestra al clonar; fuentes, entornos y entregas previos intactos.

09.02–09.09 siguen pendientes (09.08 opcional); lectura cruzada de Parquet en R
no implementada. Las nueve secciones de 08 tienen material, pero falta evidencia
del estudiante para acreditar su práctica. Los proyectos/checkpoints previstos
03_portfolio_analysis_r y 04_large_credit_dataset siguen sin implementar. R
aplicado, terminal avanzada y separación de bitácoras mantienen su consideración
de diseño, sin renumerar el track. Consultar también [cierre de 07](docs/tidyverse-closure.md).

08.08 conserva la fuente, funciones y metadatos del proyecto renv, sin paquetes
nuevos. PNG esencial con objeto explícito, 9 × 6 pulgadas/144 dpi (1296 × 864),
tablas de resumen/pares, configuración, descripción, sesión y manifiesto de
huellas. Verificador de solo lectura: fuente, tablas reconstruidas, huellas y
cabecera PNG; revisión visual complementaria, sin certificar los píxeles.
Ampliaciones: 288 dpi (2592 × 1728) y SVG/PDF con dispositivos Cairo incluidos
en R. Lección/lab ejecutados en procesos nuevos con R 4.6.1/ggplot2 4.0.3;
entrada vacía, valores/tamaño inválidos, destinos ocupados, archivos ausentes o alterados,
pares compensados y configuración incoherente comprobados. Python independiente
concilia pares y resumen, densidad/dimensiones PNG y tamaño SVG; PDF de una página
648 × 432 puntos comprobado. PNG y renderizados SVG/PDF inspeccionados.
Fuentes, funciones, metadatos y entregas 07.10/08.09 conservados mediante huellas.
No se probó la interfaz del IDE ni se exige identidad binaria entre plataformas.

08.09 reutiliza la entrega de 07.10 y el proyecto renv existente, sin nuevas
dependencias ni cambios de lockfile. Python relee la fuente y reconstruye reglas,
particiones, pares y resumen antes de contrastar seis tablas R. Concilia campos
de auditoría y motivos por registro, 14 pares y 29000/31800 MXN; explica 2800 MXN,
9.66% del saldo inicial y cobertura 14/18 por fecha. Incluye dos figuras, relectura
Python, error compensado y explicación razonada. R 4.6.1/ggplot2 4.0.3 y Python
3.12.12/Matplotlib 3.10.7 comprobados en procesos nuevos; cuatro muestras de
frontera (fechas/rango/claves, vacío, sin pares y ceros), alteraciones, destinos
ocupados y ejemplos completos del lab comprobados. Sin pares se conserva
saldo ausente, sin dibujar ceros ficticios; los ceros observados son distintos.
Se conservaron fuentes, funciones, metadatos y entrega 07.10 mediante huellas.
Las figuras se inspeccionaron; no se certifica equivalencia de píxeles ni se
probó la interfaz del IDE. La biblioteca local renv se usó sin cambios globales.

08.07 añade lección/script/lab, preparador, metadatos y tres figuras. Patchwork
1.3.2 se añade al mismo proyecto renv con respaldo exacto en respaldo_08_06/;
los 43 registros anteriores del lockfile siguen idénticos. El preparador no
instala: copia solo DESCRIPTION, renv.lock y componer_figuras.R, rechaza
repeticiones, destinos ocupados y metadatos personalizados sin sobrescribirlos.
Restauración local y segunda restauración real desde biblioteca vacía comprobadas;
sin cambiar Conda ni bibliotecas globales. Fuentes, funciones y entregas intactas.

Composición A/B de dos sumas 29000/31800 MXN y 28 observaciones de los mismos
14 IDs; cobertura 14/18, 14 grupos de dos cortes y +2800 conciliados. Disposición
horizontal/vertical, tamaños relativos, ejes/títulos propios y guía común;
facetas frente a gráficos distintos, anotación superior y descripción del conjunto.
Ampliación anidada con dispersión de 14 pares y proporción fija; ruta esencial
comprobada sin exigir esa ampliación. Guías correctas recogidas: una; locales:
dos; correspondencias de color incoherentes: dos y diferencia detectada.

Nueve bloques de lección, incluidas preparación/restauración y reinicio,
y cuatro de lab comprobados; scripts por source desde procesos nuevos con
R 4.6.1/ggplot2 4.0.3/patchwork 1.3.2. Composición completa construida como
gtable, hijos, rangos, pares, guía, proporción y tema global intacto revisados;
vacío sin puntos inventados, ceros con un ID y orden de hijos comprobados.
Preparador sin biblioteca, respaldo, repetición, metadatos alterados, ruta
ocupada, raíz incorrecta y siete argumentos inválidos comprobados. Los scripts
de referencia 08.01–08.06 pasan con el nuevo lockfile. Python estándar concilia
los 14 pares, 28 observaciones, sumas, conexiones y registros del lockfile;
respaldo conserva huellas previas y cierre idéntico al RDS verificado de 07.10.
Figuras revisadas: horizontal 1728 × 1008, vertical 1296 × 1296 y anidada
1728 × 1440; variantes del lab también inspeccionadas. Ejecución con lectura de
enlaces base renv, sin probar la interfaz del IDE. Índices, navegación y pendientes
actualizados; proyecto/checkpoints y aprendizaje del estudiante siguen separados.
Revisados 1,909 enlaces locales/fragmentos en 206 Markdown, bloques y soluciones
equilibrados y git diff --check limpio.

08.06 añade lección/script/lab y tres figuras, sin nuevas dependencias ni
cambios de fuente, funciones previas o lockfile. Mensaje, títulos, unidades,
texto/etiquetas y annotate, tema completo seguido de ajustes locales, tamaños
en puntos explícitos y señales adicionales al color. Conserva los mismos 14
IDs y 29000/31800 MXN, +2800 y aproximadamente +9.66% sobre septiembre;
cobertura 14/18 por corte y alcance descriptivo. Puntos con color/forma y
variante de color único; descripción alternativa recuperable y tabla de lectura.
Se distingue guardar alt en el objeto de integrarlo en el documento de destino.

Comprobados ocho bloques R de lección y tres de lab, incluidos source tras
reinicio, más el script de referencia en procesos nuevos; R 4.6.1/ggplot2 4.0.3.
Temas locales y orden de aplicación, tema global intacto, posiciones/importes,
nota local de una fila y annotate sin medición nueva, etiqueta vacía, filas
invertidas y categoría exterior que amplía escala comprobados. Correspondencia
de fecha/forma con dos colores y uno, alternativa recuperada y rama matemática
de base cero/cambio negativo/sin cambio revisadas. Datos y cambio conciliados
con Python estándar frente a 07.10; contraste de texto/colores seleccionados
contra blanco calculado independientemente, sin certificar accesibilidad completa.
Cierre idéntico al RDS de 07.10; fuentes, funciones, metadatos, lockfile y entrega
previa conservan huellas. Tres figuras inspeccionadas a 1296 × 864; versión
reducida 1008 × 720, variante de lab y anotación también revisadas. Sin instalar
ni cambiar entornos: ejecución con lectura de enlaces base renv, sin probar la
interfaz del IDE. Índices, navegación y pendientes actualizados; proyecto y
checkpoints siguen pendientes y no se acredita aprendizaje del estudiante.
Revisados 1,874 enlaces locales/fragmentos en 204 Markdown, bloques y soluciones
equilibrados y git diff --check limpio.

08.05 añade lección/script/lab y cuatro figuras, sin nuevas dependencias ni
cambios de fuente, funciones previas o lockfile. Recupera segmento desde los
aceptados para los mismos 14 IDs; comprueba segmento estable por ID. Ocho sumas
por segmento/corte: comercio 7600/8400, consumo 9200/10000, educacion 5800/6400
y servicios 6400/7000 MXN; cuatro/cuatro/tres/tres créditos por fecha y
fracciones con denominador común 14. Wrap fijo/libre y grid con ocho cajas,
28 puntos y escalas compartidas por fila cuando y es libre. Muestra independiente
A/B/C: tres filas, dos saldos conocidos, un saldo NA y tres combinaciones sin
registro en inventario de seis celdas; cero conservado, sin imputación.

Comprobados ocho bloques R de lección y cuatro de lab, incluidos source tras
reinicio, más el script de referencia en procesos nuevos; R 4.6.1/ggplot2 4.0.3.
Paneles, rangos, sumas/etiquetas por clave y cuartiles por celda comprobados;
capas globales sin segmento repetidas y corregidas. Drop con/sin inventario,
wrap frente a grid, vacío con/sin niveles, un segmento, cero, saldo NA, categoría
NA, niveles/filas reordenados y tabla sin variable de faceta comprobados.
Cambio de segmento con totales globales conservados y alteración compensada
detectados. Los 28 registros coinciden exactamente con el detalle de la entrega
07.10; integrantes, ocho sumas/fracciones, cuartiles/bigotes y estados conciliados
con Python estándar independiente. Cierre idéntico al RDS de 07.10 y huellas de
fuentes, funciones, metadatos, lockfile y entrega previa intactas. Cuatro figuras
inspeccionadas a 1296 × 864 (grid 1296 × 1152), con encabezados y notas legibles;
variantes de lab también revisadas. Sin instalar ni modificar entornos: R con
lectura de enlaces base renv existentes; no se prueba la interfaz del IDE.
Índices, navegación y pendientes actualizados. Proyecto/checkpoints y aprendizaje
del estudiante no se acreditan por el desarrollo del material.
Revisados 1,842 enlaces locales/fragmentos en 202 Markdown, bloques y soluciones
equilibrados y git diff --check limpio.

08.04 añade lección/script/lab y tres figuras, sin nuevas dependencias ni
cambios de fuente, funciones previas o lockfile. Escalas continuas/discretas/Date,
marcas/etiquetas, unidades y miles de MXN; límites de escala frente a zoom con
márgenes verticales explícitos, log10 sobre positivos y proporción fija.
Conserva 14 pares y 29000/31800 MXN. Caja septiembre: 14 saldos, cuartiles
1475/2050/2575; límite 1000–2500 deja diez y 1325/1750/2075, mientras el zoom
conserva la estadística completa. Lab 1000–2000: siete/siete, 10500/18500 MXN,
cuartiles 1250/1400/1750; muestra independiente de fechas con distancias 1/30
frente a categorías equidistantes, y cero conservado en escala lineal.

Comprobados once bloques R de lección y cuatro de lab, incluidos source tras
reinicio, más el script de referencia desde procesos nuevos; R 4.6.1/ggplot2 4.0.3.
Fronteras incluidas, valores justo fuera, NA, vacío, un valor, ceros, empates y
orden invertido comprobados. Avisos esperados de censura revisados; log10 de
cero/negativo, Date incompatible, categorías excluidas y barras sin base cero.
Posiciones, etiquetas/unidades, rangos de panel y proporción 1:1 comprobados;
transformación antes de cuartiles contrastada en la extensión opcional. Cuartiles,
bigotes, partición y calendario conciliados con Python estándar independiente.
Cierre idéntico al RDS verificado de 07.10; fuentes, funciones, metadatos,
lockfile y entrega anterior conservan huellas. Figuras de referencia y variantes
inspeccionadas a 1296 × 864, con textos legibles y recortes declarados. Sin
instalar ni cambiar entornos: ejecución con lectura de enlaces base renv, sin
probar la interfaz del IDE. Índices, navegación y pendientes actualizados;
proyecto/checkpoints y estado del estudiante siguen pendientes de evidencia.
Revisados 1,804 enlaces locales/fragmentos en 200 Markdown, bloques y soluciones
equilibrados y git diff --check limpio.

08.03 añade lección/script/lab y figura sobre el mismo proyecto de 07.10,
sin dependencias nuevas ni cambios de fuente, funciones previas o lockfile.
Estéticas mapeadas frente a propiedades constantes, leyenda accidental, escalas
manuales con nombres, relleno/borde de puntos, formas/tamaño y mapeos locales.
Base común conservada: 14 IDs, 28 observaciones y 29000/31800 MXN. Agrupación
por ID independiente del color/forma por fecha; caso incorrecto de dos grupos
de 14 filas corregido a 14 grupos de dos fechas y pares originales.

Comprobados diez bloques R de lección y cuatro de lab, incluidas reconstrucciones,
además del script de referencia mediante source desde procesos nuevos, con
R 4.6.1/ggplot2 4.0.3. Propiedades, escalas/leyendas, posiciones y grupos revisados;
orden invertido, agrupación previa, vacío, un ID, ceros, empates y claves numéricas.
Errores esperados de forma continua y herencia incompatible comprobados; paleta
incompleta y agrupaciones incorrectas detectadas. Pares, fechas y sumas conciliados
con Python estándar independiente. Cierre idéntico al RDS verificado de 07.10;
huellas de fuentes, funciones, metadatos, lockfile y entrega anterior intactas.
Figura de trayectorias revisada visualmente a 1296 × 864, con textos legibles;
variantes de relleno y puntos también inspeccionadas. Sin instalar ni modificar
entornos: R ejecutado con lectura de enlaces base renv existentes; no se prueba
la interfaz del IDE. Índices, navegación y pendientes actualizados. El proyecto
integrador y el estado de aprendizaje del estudiante continúan sin cambios.
Revisados 1,768 enlaces locales/fragmentos en 198 Markdown, bloques y soluciones
equilibrados y git diff --check limpio.

08.02 añade lección/script/lab y figuras sobre el cierre de 07.10, sin modificar
fuente, funciones anteriores ni metadatos renv. Misma población: dos sumas
29000/31800 MXN, 14 pares y 28 observaciones. Identidad/conteo (1/1 en resumen,
14/14 en detalle), líneas con dos fechas y dispersión de pares; histograma de
septiembre con bordes 1000–3500 cada 500 MXN, cierre derecho y frecuencias
4/3/3/2/2. Cajas tipo 7: Q1/mediana/Q3 1475/2050/2575 y 1675/2250/2775;
bigotes 1100/3200 y 1300/3400. Jitter solo horizontal reproducible y puntos
conservados. Lab con intervalos de 1000 (7/5/2), exterior independiente de
1000 MXN conservado y ampliaciones de proporciones/huecos temporales.
No instala paquetes ni exige nueva exportación; suavizados no son requisito.

Comprobados nueve bloques R de lección y cinco de lab, incluidas reconstrucción
y ampliaciones, con R 4.6.1/ggplot2 4.0.3. Script de referencia y scripts propios
de lección/lab ejecutados mediante source desde procesos nuevos, sin workspace.
Inspección por capa: sumas/conteos, fechas, pares, intervalos, cuartiles, bigotes
y exteriores. Fronteras de todos los bordes incluidos, octubre con los mismos
intervalos (3/3/3/3/2), orden invertido, empates/cero, un valor, vacío, apilado
de 28 rectángulos y NA interior frente a fila ausente comprobados. Frecuencias,
cuartiles tipo 7 y bigotes conciliados con Python estándar independiente.
El cierre coincide con el RDS verificado de 07.10; huellas de fuentes, funciones,
metadatos, lockfile y entrega anterior intactas. Figuras principales y variantes
revisadas a 1296 × 864, con textos legibles; histogramas y cajas incorporados
como referencias. Ejecución con lectura de enlaces base renv, sin instalar ni
modificar entornos. Las comprobaciones ejecutan R, no la interfaz del IDE.
Revisados 1,733 enlaces locales/fragmentos en 196 Markdown, bloques y soluciones
equilibrados y git diff --check limpio.

08.01 amplía pregunta, población y unidades; gramática, objeto ggplot, mapeos,
capas/herencia, componentes y presentación explícita. Reconstruye 07.10 sin
cambiar su fuente ni sus reglas: 14 IDs comunes, 29000/31800 MXN, +2800 y
9.66% sobre septiembre; cobertura 14/18 por corte. Script por etapas y lab con
dos barras/una etiqueta de octubre; conteo separado 1/1 sobre las filas resumidas.
Sin dependencias nuevas, cambios de lockfile ni nueva exportación obligatoria.
Referencias oficiales y R4DS segunda edición consultadas; el borrador de capas
del libro ggplot2 se identifica como consulta, no lectura obligatoria.

Comprobados los diez bloques R de lección y tres de lab, incluidas las llamadas
de reconstrucción, además del script de referencia con source desde procesos
nuevos. R 4.6.1/ggplot2 4.0.3: alturas/etiquetas, fechas/posiciones, conteo 1/1,
herencia con una sola etiqueta, orden de filas invertido y capa de texto vacía
comprobados; tabla de capa sin columnas heredadas rechazada. El cierre completo
es idéntico al RDS previamente verificado en 07.10; fuentes, funciones anteriores,
metadatos, lockfile y entrega previa conservan sus huellas. Figura de referencia
y variantes revisadas visualmente a 1296 × 864, con textos legibles y base cero.
El ejecutor restringido no resolvió enlaces base renv; ejecución con permisos de
lectura comprobada, sin desactivar controles ni instalar paquetes. Las revisiones
ejecutan R, no la interfaz del IDE. Revisados 1,702 enlaces locales/fragmentos en
194 Markdown, bloques y soluciones equilibrados, y git diff --check limpio.

07.10 añade lección/lab, funciones, ejecutor, verificador de entrega y preparador
con respaldo de metadatos 07.09. Reutiliza el CSV original y reglas de 07.09:
48 = 36 aceptados + 12 rechazos; 14 IDs comunes y cuatro aceptados sin pareja
por corte. Dos filas alimentan geom_col: 29000/31800 MXN, cambio +2800 y 9.66%
sobre septiembre de la base común; cobertura 14/18 por fecha. Contraste explícito
con geom_bar, que cuenta una fila por corte en esa tabla resumida.

Entrega en carpeta nueva: siete CSV, RDS con tipos/originales/banderas, PNG y
sessionInfo local. Relectura y reconstrucción desde la fuente comparan todas las
tablas; la firma/presencia PNG no certifica píxeles y requiere revisión visual.
Figura de 1296 × 864 revisada, con base cero, etiquetas, MXN, fechas y población,
sin textos cortados. Restauración real en segunda copia sin ggplot2 previo;
R 4.6.1/ggplot2 4.0.3 y ocho dependencias nuevas, registros previos del lockfile
idénticos y respaldo exacto. No se cambia Conda ni bibliotecas globales.

Ejemplos y soluciones R ejecutados por bloques; errores esperados aislados,
source tras reinicio y verificador en proceso nuevo sin alterar la entrega.
Fronteras: fuente vacía, todos rechazados, sin pares, un par con saldos cero,
base inicial cero y otro corte conservado aparte; orden invertido y agrupación
previa. Alteraciones de tablas, motivos y saldos compensados detectadas;
RDS/CSV modificados y PNG ausente rechazados. Exportación a ruta ocupada,
carpeta madre ausente y seis tipos/rutas inválidos controlados sin sobrescribir.
Preparación sin biblioteca, respaldo exacto, repetición y seis argumentos
inválidos comprobados. Aceptados/rechazos, pares, no coincidentes, resumen y
figura conciliados con pandas 2.3.3/SQLite; medias con tolerancia absoluta 1e-10.
Fuentes y archivos previos intactos, 07.01–07.09 pasan con el nuevo lockfile.
Las revisiones ejecutan R, no la interfaz del IDE. Revisados 1,671 enlaces
locales/fragmentos en 192 Markdown, bloques y soluciones equilibrados,
y git diff --check limpio.

07.09 añade lección/lab, funciones, ejecutor y preparador desde R. Reutiliza
el CSV conservado de 07.08 sin copiar otra fuente. Forma YYYY-MM-DD, calendario
y rango 1900–2100 antes de aceptar Date; ID/segmento normalizados, textos
originales y diez banderas con motivos conservados. Alta ≤ corte y clave
ID/corte única tras interpretar; ambas apariciones repetidas se apartan.
Trabajo 48 × 15: 36 aceptados/12 rechazados, 12 motivos en esta muestra.
Suma de registros 112800 = 81400 + 31400 MXN, no saldo a una fecha única.
Diferencia en días desde alta (no atraso), componentes e inicio_mes Date;
42 diferencias evaluables en trabajo, 36/36 entre aceptados.

Selección con límites Date y fin exclusivo; septiembre/octubre contienen
18 aceptados cada uno y 39900/41500 MXN. La base común tiene 14 IDs, con
29000/31800 MXN y diferencia 2800; cuatro no coincidentes por lado conservados.
Igual cantidad de filas no acredita igual población ni permite inferir altas/bajas.
Lubridate 1.9.5/timechange 0.4.0 incorporados con registros previos idénticos;
respaldo 07.08 y restauración real en segunda copia que no tenía lubridate.
Preparador actualiza metadatos y añade dos archivos, sin instalar por preparar.

Comprobados doce bloques R de lección y seis de lab, errores esperados aislados
y reconstrucción por source desde procesos nuevos. R 4.6.1/lubridate 1.9.5 y
pandas 2.3.3: quince columnas, banderas/motivos, partes, períodos, componentes,
resúmenes e IDs comunes conciliados; medias con tolerancia absoluta 1e-10.
Calendario/rango contrastados con datetime.date independiente. Fronteras:
vacío/todos ausentes/incompatibles, 1900/2000/2100 bisiestos, años límite,
formatos no acordados, relación igual/invertida, motivos múltiples, clave
normalizada repetida y claves incompletas; orden invertido/agrupación previa.
Límites texto/NA/Inf/fraccionarios/instantes/múltiples/invertidos rechazados,
fin exclusivo y selección vacía comprobados. Ocho resultados alterados detectados,
incluidos saldos/conteos compensados. Preparación sin biblioteca, respaldo exacto,
repetición y seis argumentos inválidos comprobados. Fuentes y archivos previos
intactos; 07.01–07.08 pasan con el nuevo lockfile, sin cambiar Conda ni bibliotecas
globales. Advertencias de fechas imposibles visibles y justificadas; no se
desactivan comprobaciones. Las revisiones ejecutan R, no la interfaz del IDE.
Revisados 1,628 enlaces locales/fragmentos, bloques/soluciones equilibrados
y git diff --check limpio.

07.08 añade lección/lab, funciones, ejecutor y preparador desde R con respaldo
07.07. Reutiliza 48 entradas de pandas 02.06, distintas de la fuente de 07.07:
trabajo 48 × 10 con cinco columnas originales conservadas, segmento recortado,
normalizado, estado y marca de cambio. Reglas explícitas: trim exterior,
vacío a NA, minúsculas en locale es y equivalencia exacta educación/educacion.
45 segmentos reconocidos y tres pendientes (registros 5/9/48): dos ausencias
y microcredito fuera de catálogo. 46 textos modificados; suma de registros
112800 = 105800 + 7000 MXN, sin presentarla como saldo a una fecha única.
Fechas e IDs siguen sin interpretar/normalizar: reconocimiento no acredita
aceptación completa. Los pendientes conservan texto e importes.

Forcats 1.0.1 añadido y stringr 1.6.0 declarado directamente; todos los registros
previos del lockfile permanecen idénticos. Preparador sin instalación respalda
DESCRIPTION/renv.lock en respaldo_07_07/, actualiza ambos y añade tres archivos.
Restauración real en segunda copia que no tenía forcats, con ejecución completa.
Factores estrictos solo para reconocidos; etiquetas/códigos/niveles y orden
nominal, fct_relevel/reorder/drop, grupos vacíos y patrones sencillos explicados.
No grafica, no absorbe desconocidos en NA ni recodifica categorías sin regla.

Comprobados catorce bloques R de lección y siete de lab, errores esperados
separados y reconstrucción por source desde procesos nuevos. R 4.6.1/stringr
1.6.0/forcats 1.0.1 y pandas 2.3.3: todas las columnas de texto, estados,
marcas, partes, niveles y resumen conciliados independientemente. Fronteras:
vacío, todos pendientes/reconocidos, cero, rango integer, espacios/tabulación/
NBSP, acentos y representación Unicode descompuesta conservada, textos NA/no_dato,
grupos previos y orden invertido. Tipos/esquemas incompatibles, saldo ausente/
negativo/fraccionario y campos extra rechazados por el lector o contrato.
Ocho alteraciones detectadas, incluidas sumas/conteos compensados y cambios
de niveles. Preparación sin biblioteca, respaldo exacto, repetición y seis
argumentos inválidos comprobados; fuentes y archivos previos intactos.
07.01–07.07 pasan con el nuevo lockfile; sin cambiar Conda ni bibliotecas globales.
Revisión automatizada ejecuta R, no la interfaz del IDE. Revisados 1,607 enlaces
locales/fragmentos, bloques y soluciones equilibrados y git diff --check limpio.

07.07 añade lección/lab, lector/funciones, ejecutor y preparador desde R.
Muestra analítica de pandas 02.07: 48 observaciones de 24 IDs en dos cortes,
distinta de los 29 aceptados previos. Proyección ID/corte/saldo 48 × 3 →
ancho 24 × 3 → 48 × 3 recuperado, con seis NA y tipos conservados. Saldos
observados 47200/46700 MXN; cobertura 21/24 en cada corte, sin afirmar totales
completos. Inventario de claves presentes distingue NA explícito de combinación
ausente en una muestra mínima independiente. Validación de celda única antes
del pivot, esquema vacío estable, values_drop_na/values_fill y values_fn
explicados sin borrar ausencias, imputar cero ni agregar duplicados.

Lockfile generado con R 4.6.1/renv 1.3.1: incorpora tidyr 1.3.2, purrr 1.2.2,
stringr 1.6.0 y stringi 1.8.9; todos los registros previos permanecen idénticos.
Preparador respalda DESCRIPTION/lockfile en respaldo_07_06/, actualiza ambos
y añade funciones, ejecutor y CSV; sin instalar por preparar. Comprobada una
restauración real desde biblioteca nueva y ejecución completa en esa copia.
Sin modificar Conda, bibliotecas globales ni las semillas renv anteriores.

Comprobados doce bloques R de lección y nueve de lab, con errores esperados
separados; reconstrucción por source desde procesos nuevos. Conciliación
campo a campo con pandas 2.3.3 de proyección, ancho, vuelta y muestra con huecos.
Fronteras: vacío, un corte, cero, todos NA, rango integer, orden invertido,
agrupación previa, clave repetida/incompleta y corte ajeno. Tipos incompatibles
y factores rechazados; lector probado con cabecera sola, esquema incorrecto,
fracciones, negativos, campos extra y duplicados. Ocho alteraciones detectadas,
incluidos saldos compensados, sustitución de NA por cero y cambios de claves.
Preparación sin biblioteca, respaldo exacto, repetición y seis argumentos
inválidos comprobados. Fuentes y archivos previos intactos; 07.01–07.06 pasan
con el nuevo lockfile. Revisión automatizada ejecuta R, no la interfaz del IDE.
Revisados 1,585 enlaces locales/fragmentos; bloques y soluciones equilibrados,
git diff --check limpio y lockfile de la copia restaurada idéntico al entregado.

07.06 añade lección/lab, funciones, ejecutor y catálogo estático sintético;
preparador desde R añade exactamente tres archivos sin alterar los anteriores.
left_join/inner_join y semi_join/anti_join, claves completas, relationship y
na_matches. Unión de 29 aceptados de 07.04: 29 × 14, 177250 MXN conservados,
19 coincidencias/10 sin catálogo, con partición 120250/57000 MXN. Seis registros
coinciden pero tienen etiqueta desconocida; salud queda sin uso. Catálogo
completo y único validado antes de unir, incluso claves sin uso. Estado de
coincidencia distinto de presencia de etiqueta; cobertura y cardinalidad son
contratos independientes. Demostración incorrecta: duplicar comercio genera
37 filas y 224250 MXN; la relación muchos a uno detiene la multiplicación.

Comprobados doce bloques R de lección y nueve de lab, con errores esperados
separados; reconstrucción por source desde procesos nuevos. R 4.6.1/dplyr 1.2.1,
pandas 2.3.3 y SQLite: conciliación de todas las columnas del detalle/ampliado,
partes con/sin coincidencia, catálogo sin uso y políticas NA/NULL. Fronteras:
detalle/catálogo vacíos, coincidencia total/nula, cantidades NA/cero, orden
invertido, agrupaciones previas y varios cortes. Rechazados duplicados usados
y sin uso, claves incompletas, rastros repetidos/inválidos y columnas en conflicto.
Probados uno a muchos sin advertencia predeterminada, clave compuesta, límites
de relationship y unmatched; ocho resultados alterados detectados, incluso saldos
y conteos compensados. Preparación sin biblioteca, repetición y seis argumentos
inválidos comprobados. Archivos previos, fuentes, metadatos y lockfile intactos;
07.01–07.05 siguen funcionando. Sin instalaciones ni cambios globales; revisión
R con permisos de lectura de enlaces base renv existentes, sin desactivar controles.
Las pruebas ejecutan R, no la interfaz del IDE. Revisados 1,562 enlaces locales
y fragmentos, bloques/soluciones equilibrados y git diff --check limpio.

07.05 añade lección/lab, funciones, ejecutor y preparador desde R; incorpora
exactamente dos archivos al proyecto sin nuevos datos ni dependencias. Resume
los 29 aceptados de 07.04: cuatro grupos corte/segmento, 177250 MXN y 18 atrasos
≥ 30 entre 29 conocidos. group_by/summarise/n, estado de agrupación/ungroup,
suma observada/total completo, promedio y tasas con denominadores explícitos.
Muestra analítica mínima independiente para ausencias sin cambiar aceptación;
NA en clave, cero, todos faltantes, vacío y factores como ampliación opcional.

Comprobados once bloques R de lección y ocho de lab, con error deliberado
separado; reconstrucción desde procesos nuevos. R 4.6.1/dplyr 1.2.1 y pandas
2.3.3: doce columnas conciliadas en resumen principal y muestra mínima; base
principal aceptada independientemente con las reglas pandas de 02.05.
Fronteras: 29/30/31 días, rango integer, suma double, NA/cero/vacío, varios
cortes, orden invertido y agrupación previa; duplicados/claves incompletas y
cantidades fuera de contrato rechazados. Ocho resúmenes alterados detectados,
incluso sumas/conteos compensados. Preparación sin biblioteca, repetición y
seis argumentos inválidos comprobados; archivos previos y lockfile intactos.
El ejecutor restringido no resolvió enlaces base renv; la ejecución con permisos
de lectura pasó, sin desactivar comprobaciones, instalar ni cambiar entornos.
Las revisiones ejecutan R; no afirman una prueba de la interfaz gráfica del IDE.
Ejecutor final y compatibilidad con 07.01–07.04 comprobados; 1,537 enlaces
locales/fragmentos revisados, bloques y soluciones equilibrados y diff limpio.

07.04 añade lección/lab, funciones y ejecutor sobre 44 registros de pandas 02.05,
sin dependencias nuevas. Preparador desde R añade exactamente tres archivos al
mismo proyecto; conserva CSV, funciones, scripts, resultados y metadatos previos.
Reutiliza lectura/conversión de 07.03. Reglas de presencia, entero, rango, catálogo,
pago ≤ saldo y clave compuesta completa. Todas las apariciones repetidas se
apartan; distinct solo ilustra reducción y dependencia del orden, no una reparación.
Trabajo 44 × 12, banderas 44 × 15: 29 aceptados/15 rechazados, 19 incidencias.
Conserva numero_registro, tres textos originales y todos los motivos, en orden fijo.
Saldo interpretable 234900 = 177250 + 57650 MXN, cobertura 42/44; dos saldos
siguen sin interpretar. No se presenta como total limpio de créditos únicos.

Revisados los once bloques R de lección y ocho del lab, con un error esperado
de partición aislado; reconstrucción por source desde sesiones nuevas. R 4.6.1,
dplyr 1.2.1/readr 2.2.0 existentes. Comparación exacta con pandas 2.3.3 de trabajo,
aceptados, rechazados y quince banderas: claves, textos, faltantes, cantidades
y todos los motivos. Fronteras: cero válido, vacío, todos ausentes, claves
completas/incompletas, mismo ID en cortes distintos, repeticiones exactas y
conflictivas/no adyacentes, catálogo, negativos, sobrepago y conversiones fuera
de contrato. Diez alteraciones de partes/banderas detectadas, incluso conteos
o sumas compensadas. Segunda preparación y cinco argumentos inválidos rechazados;
fuente/archivos previos/lockfile intactos, sin instalar ni inicializar biblioteca.
La revisión automatizada ejecuta R; no afirma una prueba de la interfaz del IDE.
Revisados 1,513 enlaces locales/fragmentos y bloques/soluciones equilibrados;
git diff --check limpio. La documentación conserva el contrato y sus límites.

07.03 añade lección ampliada, lab, funciones y ejecutor sin dependencias nuevas
ni modificar metadatos. Preparador desde R copia exactamente tres archivos al
mismo proyecto: funciones, script y CSV de 40 filas de pandas 02.04. Ejemplos
pequeños con las seis filas previas antes de convertir/calcular la muestra mayor.
mutate, if_else/case_when, tipos y prioridad; texto de origen y marcas conservados.
parse_double más requisito de entero finito/en rango: no trunca 3.5, no imputa
ausentes. Denominador positivo antes de dividir; resta double para evitar overflow.
40 × 15, 36 restas/35 porcentajes evaluables; en la misma base,
217750 − 6600 = 211150 MXN y etiquetas 21/16/3. Clasificar no acredita validez.

Comprobados diez bloques R de la lección y diez del lab (uno con error de tipos
aislado), reconstrucción desde sesión nueva y compatibilidad con scripts previos.
Conciliados 600 campos con pandas 2.3.3: claves, textos, máscaras y marcas exactos,
restas/etiquetas exactas, porcentajes con tolerancia absoluta 1e-10. R 4.6.1,
dplyr 1.2.1/readr 2.2.0 existentes. Fronteras integer, fracciones/Inf/NaN/texto NA,
cero/negativo/sobrepago, datos ausentes, prioridad, vacío tipado y todos faltantes.
Segunda preparación y cinco argumentos inválidos rechazados; lectura con esquema
incorrecto y mutate con tamaño incorrecto fallan. Fuente, muestras anteriores,
funciones y lockfile intactos. Advertencias esperadas visibles, sin instalaciones
ni cambios globales; las pruebas ejecutan R, no la interfaz gráfica del IDE.
Preparación sin biblioteca añade exactamente tres archivos y conserva todos
los anteriores, sin inicializar ni instalar. 1,486 enlaces locales/fragmentos
revisados, bloques/soluciones equilibrados y git diff --check limpio.

07.02 añade dplyr 1.2.1/generics 0.1.4 al lockfile del mismo proyecto, con
respaldo exacto de DESCRIPTION/lock de 07.01. Preparador como función cargada
por source; restaura desde R y trabaja en scripts del IDE. Mismo CSV de seis
filas, selección saldo ≥ 500/atraso ≥ 5: claves 002/003/006 y 2750 MXN con saldo
conocido 3/3. Condición completa separada en 3 confirmados, 2 no cumplen y 1
pendiente. select/rename/filter/arrange, empates explícitos y vacío tipado.

Comprobados los ocho bloques R de la lección y ocho del lab, con un error
deliberado por separado; restauración real y reconstrucción por source desde
sesiones nuevas. R 4.6.1/pandas 2.3.3/SQLite concilian registros completos y orden
de la selección, pendiente 005 y caso sin coincidencias sobre el mismo CSV.
Nueve combinaciones de lógica de tres valores, fronteras incluidas, todos
faltantes/todos falsos/vacío, empate con entrada invertida, NA al final y
duplicados conservados al filtrar. Segunda preparación y cinco argumentos
inválidos rechazados sin cambios. Fuente, lector, metadatos, versiones previas
y respaldo comprobados; sin instalación global ni cambios en dependencias Python.
Revisados 1,455 enlaces locales y fragmentos, bloques y soluciones equilibrados;
git diff --check limpio. Los menús del IDE se reutilizan de 07.01; las pruebas
automatizadas ejecutan llamadas R, sin afirmar una prueba de la interfaz gráfica.

07.01 reutiliza el CSV/diccionario de pandas 02.02: seis créditos, cinco columnas,
6000 MXN con cobertura 6/6 y atraso desconocido 1/6. Lector con tipos explícitos,
problems/stop_for_problems, comprobación del esquema y controles de muestra.
Pipe nativo y extracción tabla/vector sin verbos de dplyr adelantados.
Preparador extiende la práctica 06.09 con respaldo exacto de DESCRIPTION/lockfile;
conserva perfil, funciones, datos y salidas anteriores. Lockfile generado y
restaurado en biblioteca local: R 4.6.1, readr 2.2.0, tibble 3.3.1, withr 3.0.3,
renv 1.3.1; 23 paquetes nuevos incluyendo dependencias transitivas.
Sin instalación global ni cambio en las semillas 06 o dependencias Python.

En la primera versión se comprobaron seis bloques R de la lección y seis del lab
(uno con error deliberado), ejecutor en sesión nueva y fronteras: solo cabecera, NA permitido,
cero, UTF-8/coma/decimal, texto numérico inválido, atraso fraccionario, campos
de más/de menos, esquema extra/duplicado/reordenado, fila vacía y longitudes
incompatibles. Un negativo/fecha inválida ilustra los límites del parseo sin
confundirlo con calidad. Segunda preparación rechazada sin cambios; respaldo
de metadatos exacto y fuentes intactas. Advertencias esperadas observadas sin
silenciarlas; locale UTF-8 solo por proceso. Una entrega previa de 06.09 se
conservó byte a byte tras extender el proyecto; verificador y nuevo cálculo
06.09 pasan con el lockfile ampliado (72 controles). Revisados 1,427 enlaces
locales y fragmentos; bloques/soluciones equilibrados y git diff --check limpio.
En la adaptación al IDE se comprobaron los ocho bloques R de lección y siete
del lab: preparación por función, restauración con source y reconstrucción del
script propio y del ejecutor desde otro proceso sin objetos previos. Cargar el
preparador no copia archivos; llamada por R y CLI producen archivos idénticos.
Segunda preparación y cinco argumentos inválidos rechazados; entrada, lockfile
y respaldo intactos. Menús/atajos contrastados con documentación oficial Posit;
la revisión automatizada ejecutó las llamadas R, no la interfaz de RStudio.

06.09 añade copia autocontenida con referencia Python independiente, cálculo R,
comparador y verificador de solo lectura. Usa las mismas 14 ventas y reglas
06.07, distintas de 01.06; ese ejercicio anterior se conserva. Concilia 14/8/6,
cobertura 6/8, suma observada 765.5 y total desconocido. Posiciones, claves,
textos, motivos y faltantes exactos; valores numéricos con tolerancia absoluta
1e-9. Contexto Python con contrato, umbral y huella de fuente. Se comparan
36 controles en memoria y 36 sobre CSV guardados; informe final y sesión.

Comprobado con R 4.6.1/Python 3.12.12 y el lockfile renv 1.3.1/withr 3.0.3 de
06.08, sin dependencias nuevas. Recorrido predeterminado y seis bloques R del
lab ejecutados, uno con error deliberado por separado. Ocho fronteras conciliadas:
solo cabecera, todos rechazados, todos faltantes, cero, frontera de umbral,
decimales, motivos múltiples y notas con comillas/acentos/NA. Variante confirmada
V006: suma 885.5, media 126.5, cobertura 87.5% y grupos 2/5/1.
Diez alteraciones de tablas detectadas sin reparar: importe, NA por cero, clave,
orden, conteo, conteo fraccionario, motivo, texto rechazado, total falso y media
redondeada. Referencia antigua o discrepancia previa no crea salida; corrupción
durante escritura deja parcial sin informe, y entrega sin informe se rechaza.
Entradas y salidas anteriores intactas; verificador sin escrituras comprobado.
Locale UTF-8 solo en procesos de revisión; sin cambios globales de configuración.
No se reejecutó la colección Python 05: la referencia de cierre se probó aparte.

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

### 2026-10-21

- Se desarrolló [09.01](curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md)
  con lección/lab, scripts de inspección, CSV/Parquet reales y evidencia de lectura.
  Controles R/Python y lectores desde sesiones nuevas comprobados; sin dependencias
  nuevas ni cambios de entornos. El esencial distingue firma de decodificación.
- Se documentaron [pendientes de cierre](docs/storage-closure.md) y el punto de
  reanudación 09.02. No se da por terminado el módulo 09 ni se acredita práctica
  del estudiante o proyectos/checkpoints previstos.

- Se implementó [08.08 — Exportación reproducible](curriculum/08_visualization_r/08_reproducible_export/README.md)
  con script, figura y lab: PNG esencial, dimensiones/dpi, configuración y
  verificación; SVG/PDF opcionales. Ejemplos, sesiones nuevas, alteraciones y
  conservación de archivos anteriores comprobados. Navegación 08.07 → 08.08 →
  08.09 restablecida; las nueve secciones tienen material, sin acreditar prácticas.

- Se desarrolló 08.09 con lección/lab, scripts R/Python y dos figuras. Reconstrucción
  independiente, seis tablas conciliadas, denominadores y error compensado; sesiones
  nuevas, fronteras y archivos previos conservados comprobados. Sin dependencias nuevas.
- 08.08 conserva su plan y es el siguiente trabajo de autoría; no se da el módulo
  por terminado ni se acredita al estudiante o al proyecto integrador.

### 2026-10-20

- Se desarrolló [08.07 — Componer figuras](curriculum/08_visualization_r/07_compose_figures/README.md)
  con script, tres figuras y [lab](labs/08_visualization_r/07_compose_figures/README.md).
  Resumen/detalle conciliados, disposición, guías y contexto; patchwork 1.3.2
  registrado con respaldo y restauración local real, conservando dependencias
  previas. Ejemplos y 08.01–08.06 comprobados; fuentes/funciones/entregas intactas.
  Siguiente: **08.08 — Exportación reproducible**, todavía planificada.

- Se desarrolló [08.06 — Etiquetas, temas y accesibilidad](curriculum/08_visualization_r/06_labels_themes_accessibility/README.md)
  con script, tres figuras y [lab](labs/08_visualization_r/06_labels_themes_accessibility/README.md).
  Mensaje, etiquetas/anotaciones, temas locales, señales además del color,
  descripción alternativa y tabla; ejemplos R, variantes y contraste comprobados.
  Datos/cambio conciliados con Python, fuentes/lockfile/entregas intactos.
  Siguiente: **08.07 — Componer figuras**, todavía planificada.

- Se desarrolló [08.05 — Facetas y comparación entre grupos](curriculum/08_visualization_r/05_facets_groups/README.md)
  con script, cuatro figuras y [lab](labs/08_visualization_r/05_facets_groups/README.md).
  Paneles, escalas compartidas/libres, integrantes, denominadores y capas con
  claves; muestra independiente de cero/NA/sin registro. Ejemplos R comprobados,
  detalle y cálculos conciliados con Python; fuentes/lockfile/entregas intactos.
  Siguiente: **08.06 — Etiquetas, temas y accesibilidad**, todavía planificada.

- Se desarrolló [08.04 — Escalas y coordenadas](curriculum/08_visualization_r/04_scales_coordinates/README.md)
  con script, tres figuras y [lab](labs/08_visualization_r/04_scales_coordinates/README.md).
  Unidades, límites frente a zoom, fechas, log10 y proporción 1:1; ejemplos R
  comprobados y cuartiles/bigotes/partición conciliados con Python. Fuentes,
  lockfile y entregas previas intactos. Siguiente: **08.05 — Facetas y comparación
  entre grupos**, todavía planificada; no se modifica el estado del estudiante.

- Se desarrolló [08.03 — Mapear y fijar estéticas](curriculum/08_visualization_r/03_aesthetic_mapping/README.md)
  con script, figura y [lab](labs/08_visualization_r/03_aesthetic_mapping/README.md).
  Mapeos/constantes, leyendas, relleno/borde, formas/tamaño y líneas por ID;
  ejemplos y reconstrucciones R comprobados y pares conciliados con Python.
  Fuentes, lockfile y entregas previas intactos. Siguiente: **08.04 — Escalas y
  coordenadas**, todavía planificada; los proyectos/checkpoints siguen pendientes.

- Se desarrollaron [08.01](curriculum/08_visualization_r/01_question_grammar/README.md)
  y [08.02](curriculum/08_visualization_r/02_geometries_stats/README.md), con
  lecciones, scripts, labs y figuras de referencia. Reconstrucciones desde
  procesos R nuevos y comprobaciones de datos/capas/figuras completadas;
  sin dependencias nuevas ni cambios de fuente, lockfile o entregas anteriores.
- Cierre de la mañana: índices, navegación, arquitectura, lecturas y pendientes
  revisados; referencias antiguas a lecciones planificadas corregidas y mapa
  general separado del progreso. Retomar con **08.03 — Mapear y fijar estéticas**;
  las otras siete secciones de 08 y los proyectos/checkpoints siguen pendientes.
  El estado de aprendizaje del estudiante no se modifica sin evidencia.
  Comprobados 1,735 enlaces locales/fragmentos en 196 Markdown, bloques y
  soluciones equilibrados, SVG válido con textos dentro del espacio disponible
  y git diff --check limpio. Esta revisión documental no reejecuta los ejemplos
  de código ya comprobados durante el desarrollo de 08.01–08.02.

- Se cerró el material de 07 con lección/lab 07.10, figura ggplot2 y entrega
  reconstruible. Conserva las reglas y población de 07.09, con base común
  explícita, tablas auditables y límites de interpretación.
- Lockfile/restauración local, fuentes, fronteras, datos alterados, relectura y
  comparación pandas/SQLite comprobados; scripts previos conservados. PNG
  inspeccionado y 1,671 enlaces revisados. Índices, arquitectura y lecturas
  actualizados; criterios y pendientes en docs/tidyverse-closure.md.
- En ese cierre de 07 quedaban pendientes la evidencia del estudiante,
  el proyecto/checkpoints y 08.01–08.09; el siguiente desarrollo era 08.01.
  Su implementación posterior se registra arriba, sin acreditar aprendizaje por autoría.

### 2026-10-19

- Se desarrolló 07.09 con lección/lab, funciones, ejecutor y preparador: fechas
  bajo formato/calendario, relaciones y claves, 36 aceptados/12 rechazados con
  todos sus motivos; diferencias en días y selección con fin exclusivo.
- Comparación por corte y base común de 14 IDs conciliadas con pandas; calendario
  con datetime, fronteras y alteraciones comprobados. Lubridate/timechange
  incorporados con respaldo, restauración local y versiones previas conservadas.
  Navegación y 1,628 enlaces revisados. Sigue 07.10, todavía planificada; no se
  acredita aprendizaje ni se crean checkpoints integradores pendientes.

- Se desarrolló 07.08 con lección/lab, funciones, ejecutor y preparador: texto
  original conservado, equivalencias exactas, 45 segmentos reconocidos y tres
  pendientes sobre 48 entradas. Factores nominales y orden sin alterar indicadores.
- Forcats añadido y stringr declarado directamente, con respaldo y restauración
  local comprobada; registros previos del lockfile conservados. Ejemplos,
  fronteras, alteraciones y conciliación pandas verificados; 1,607 enlaces y
  navegación revisados. Sigue 07.09, todavía planificada, sin acreditar aprendizaje
  ni crear checkpoints integradores pendientes.

- Se desarrolló 07.07 con lección/lab, funciones, ejecutor y preparador.
  Cambio largo/ancho/largo de la proyección de 48 observaciones; claves,
  tipos, NA y cobertura conservados. Inventario explícito para huecos.
- Tidyr y tres dependencias incorporados al mismo proyecto renv con respaldo;
  registros previos intactos y restauración desde biblioteca nueva comprobada.
  Ejemplos, fronteras, alteraciones y conciliación pandas verificados; navegación,
  referencias y estado actualizados. Sigue 07.08, todavía planificada, sin
  acreditar aprendizaje ni crear checkpoints integradores pendientes.

- Se desarrolló 07.06 con lección/lab, catálogo, funciones, ejecutor y preparador.
  Unión muchos a uno sobre 29 aceptados; coincidencias, etiquetas ausentes y
  claves sin uso distinguidas, sin inflar el saldo ni descartar no coincidencias.
- Ejemplos, fronteras, reconstrucción, alteraciones y compatibilidad previa
  comprobados; todas las columnas conciliadas con pandas/SQLite. Índices,
  navegación, referencias y estado actualizados; 1,562 enlaces revisados.
  Sigue 07.07, todavía planificada; sin acreditar aprendizaje ni crear checkpoints.

- Se desarrolló 07.05 con lección/lab, funciones, ejecutor y preparador desde R.
  Agrupación, estado persistente, cobertura y denominadores; resumen de los
  29 aceptados de 07.04 conciliado con pandas, sin mezclar otras muestras.
- Comprobados bloques, reconstrucción, fronteras y resúmenes alterados;
  fuentes y dependencias conservadas. Índices, continuidad y referencias
  actualizados. Continúa 07.06, todavía planificada; no se acredita aprendizaje
  ni se crean checkpoints integradores pendientes.

### 2026-10-18

- Se completó y revisó 07.04: lección/lab, funciones, preparador y ejecutor en
  RStudio/IDE; 44 = 29 + 15, 19 incidencias y todos los motivos conservados.
  Conciliación con pandas, fronteras y diez particiones alteradas comprobadas.
- Índices, continuidad desde 07.03, roadmap, arquitectura, lecturas y estado
  de desarrollo actualizados; 1,513 enlaces locales revisados. Continúa 07.05,
  todavía planificada. La revisión
  no modifica el avance del estudiante ni crea checkpoints integradores pendientes.

### 2026-10-17

- Se desarrolló 07.03 con lección ampliada, lab, funciones y script, sin paquetes
  nuevos. mutate/if_else/case_when, conversión con origen/marcas y denominadores
  explícitos; muestra de 40 filas de pandas conservada y 600 campos conciliados.
  Ejemplos, fronteras, vacío, fuente intacta y ejecución completa desde R
  comprobados; 1,486 enlaces locales revisados. Sigue 07.04, todavía planificada;
  sin acreditar aprendizaje.

- Se desarrolló 07.02 con lección/lab, preparador desde R, lockfile dplyr 1.2.1
  y script de selección comprobable. Recorrido IDE, lógica de tres valores,
  partición 3/2/1, empates, vacío y conservación. pandas/SQLite concilian la
  misma selección y orden; 1,455 enlaces locales revisados. Continúa 07.03, todavía planificada; sin acreditar
  aprendizaje ni crear checkpoints integradores pendientes.

- Se adaptaron 07.01 y su lab al recorrido RStudio/IDE: preparación con función
  cargada por source, apertura de la carpeta existente como proyecto, restauración
  desde R, script por bloques y reinicio seguido de ejecución completa. Console
  y Terminal diferenciados; Rscript queda como alternativa opcional desplegable.
  Recorrido R, compatibilidad CLI, controles de preparación y reconstrucción
  comprobados; archivos de entrada y lockfile conservados, 1,427 enlaces válidos.

- Se acordó priorizar el trabajo en RStudio/IDE en el material R nuevo y reservar
  la terminal para necesidades concretas. Criterio registrado en la guía de
  autoría; adaptación de lecciones existentes pendiente de revisión posterior.

- Se desarrolló 07.01 con lección, lab, lector/ejecutor y extensión del proyecto
  renv con respaldo de metadatos. Retoma cartera de pandas 02.02; controles de
  tipos, forma, faltantes y saldo, pipe nativo y problemas de lectura.
- Lockfile generado/restaurado con readr 2.2.0 y tibble 3.3.1; ejemplos y fronteras
  ejecutados. Entrega 06.09 intacta y recalculada con el lock ampliado; 1,427
  enlaces locales revisados. Índices, continuidad y fuentes actualizados. Sigue 07.02,
  todavía planificada; sin acreditar aprendizaje ni crear checkpoints ficticios.

- Se desarrolló 06.09 con lección/lab, referencia Python de biblioteca estándar,
  preparador, comparación de tablas y verificador sin escrituras. Cierre material
  de las nueve secciones de R fundamental, sin acreditar aprendizaje del estudiante.
- Recorrido, fronteras, variante, referencia antigua, alteraciones y conservación
  comprobados. Índices, navegación, roadmap, arquitectura y lecturas actualizados.
  1,370 enlaces locales y sus fragmentos revisados; bloques y soluciones equilibrados.
  Sigue 07.01, todavía planificada; no se inicia tidyverse en este cierre.
  Proyectos/checkpoints integradores siguen pendientes.

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
