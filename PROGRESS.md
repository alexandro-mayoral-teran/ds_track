# Estado del material y bitácora editorial

<a id="progreso-de-aprendizaje"></a>

Este archivo registra desarrollo del material, comprobaciones de autoría y
siguiente trabajo. El plan vive en [ROADMAP.md](ROADMAP.md); la evidencia de
quien estudia pertenece a su copia personal, no a esta bitácora compartida.

## En este momento

- **Material disponible:** base de módulos 00–14 con lecciones y labs; consultar el
  [curriculum](curriculum/README.md) para orden, alcance y ampliaciones opcionales.
  Proyectos/checkpoints y práctica del estudiante
  siguen pendientes; material desarrollado no acredita aprendizaje.
- **Siguiente trabajo educativo:** práctica de cierre y [depuración transversal acordada](docs/reproducible-projects-closure.md#trabajo-posterior-depurar-y-observar). No hay módulo 15 definido.
- **Cierres de aplicación disponibles:** [12.09 — Streamlit](curriculum/12_streamlit/09_local_delivery/README.md)
  y [13.10 — Shiny](curriculum/13_shiny_web/10_local_delivery/README.md).
  Elegir una ruta y retomar su práctica de reconstrucción/demostración antes
  del [cierre integrado de 14](docs/reproducible-projects-closure.md).
  [Estado de Streamlit](docs/streamlit-closure.md) y [cierre de Shiny](docs/shiny-closure.md).
- **Último desarrollo educativo:** 2026-10-29, 14.09 — Revisión final y defensa: reconstrucción, revisión por casos, decisiones y acta; base de lecciones/labs disponible.
- **Última revisión documental:** 2026-10-29, cierre de ajustes de preparación y
  reanudación; revisión visual de 14.08 completada y entorno local reconstruido.
- **Presentación:** índices 00–14 y lecciones 00–11 adaptados; la
  [cobertura vigente](docs/README.md#cobertura-de-las-plantillas-y-del-portal)
  distingue lecciones, labs y portal.
- **Portal local:** módulo 00 y sesión 02.01 integrados, sin despliegue en Internet.
  [Uso y comprobaciones](portal/README.md).
- **Último trabajo:** 2026-10-27, adaptación de las nueve lecciones de
  Reportes con Quarto, con apoyos y cierre común; cobertura visual 00–11.
- **Siguiente paso:** revisar el contenido y observar una sesión real de pareja
  con el portal local:
  orientación, apertura, reconstrucción de práctica, revisión y reanudación.
- **Criterios de integración:** [tidyverse](docs/tidyverse-closure.md),
  [almacenamiento](docs/storage-closure.md) y [reportes](docs/reporting-closure.md).

### Para retomar el desarrollo

**Depuración 00.03 — 2026-10-29, áreas de Git como secuencia:**
Diagrama por columnas/líneas de vida inspirado en la referencia del usuario,
con SVG legible y fuente Mermaid editable. Separa copia/preparación/historial
y referencias del remoto en local frente al repositorio en GitHub.
Add/commit/push y anticipación fetch/pull --ff-only, sin adelantar merge/rebase.
Referencias como origin/main no se presentan como otro repositorio ni estado
en vivo. Lectura textual y acceso a tamaño completo; comandos de práctica
previos intactos. Fuentes oficiales Git contrastadas. Portal y privados fuera.
Verificación: Mermaid renderizado, SVG válido sin scripts y con título/descripción;
carga en HTML a 1280/390 comprobada con imagen ajustada al ancho y enlace al
tamaño completo. Diagrama completo y vista de escritorio revisados visualmente;
5735 enlaces locales sin incidencias. No se amplía la integración del portal.

**Depuración 00.03 — 2026-10-29, diagrama de las áreas de Git:**
Diagrama Mermaid junto al área de preparación: copia de trabajo, selección e
historial dentro del equipo; remoto separado y flechas add/commit/push.
Lectura textual equivalente, archivo conservado en la copia de trabajo y
comparaciones diff/diff --staged explicadas, incluido archivo nuevo/primer
commit. Sustituye el esquema lineal previo sin modificar comandos de práctica.
Portal y cambios locales previos ajenos fuera del alcance.
Verificación: 5731 enlaces locales sin incidencias; Mermaid renderizado con el
motor incluido en Quarto a 1280/390 sin desbordes y móvil revisado visualmente.
Formato comprobado. No se cambian las secuencias de comandos ya verificadas.

**Depuración 00.03 — 2026-10-29, bases de Git y dos recorridos:**
Problema de versiones, usos en scripts/SQL/documentación y límite de comparación
de Excel. Preparación orientada a fuentes oficiales; descargar DS Track como
ZIP separado de la disponibilidad de Git/GitHub. Perfil por clone y alternativa
local en carpeta nueva con init, identidad local y dos commits sin remoto.
Ejemplo de frase/diff y estados al guardar, preparar y registrar; cambio después
de add explicado en desplegable. Glosario contextual y lab alineados por ruta.
Evidencia personal dirigida a bitácora propia, no al PROGRESS editorial.
Fuentes Git consultadas; sin cambiar entornos ni instalar Git para la revisión.
Portal y cambios locales previos ajenos fuera del alcance.
Índice del módulo alineado con ambas rutas. Verificación: recorrido local real
en carpeta aislada de output, dos commits sin remoto y estados/diffs contrastados,
incluido cambio posterior a add; configuración global conservada. 5731 enlaces
locales sin incidencias; HTML de lección/lab a 1280/390 sin desbordes ni IDs
repetidos, variante local móvil revisada visualmente. No se instala Git ni se
publica un perfil durante las pruebas; autenticación real del alumno pendiente.

**Depuración 00.02 — 2026-10-29, ejecutar una macro desde un script:**
Ejemplo conceptual de Excel de escritorio: abrir .xlsm, llamar macro existente
con fecha/ruta como argumentos, revisar/guardar y cerrar recursos incluso ante
errores. Workbooks.Open/Application.Run documentados con fuentes oficiales;
se distingue script coordinador de VBA y ejecución interactiva de Office
desatendido. No se crean scripts, libros ni tareas; no se afirma ejecución real.
Enlaces y formato comprobados. Portal y cambios locales previos conservados.

**Depuración 00.02 — 2026-10-29, macros y patrones cercanos al trabajo:**
Puente entre macros VBA, scripts .vbs/Windows Script Host y Programador de
tareas, sin confundir lenguajes ni crear tareas. VBScript en desuso documentado;
PowerShell/Python como alternativas a valorar para nuevas automatizaciones.
Regex con casos RFC/CURP/folios: formato separado de registro, reglas e identidad.
Folio ficticio con dos casos y límites de rendimiento/lectura CSV explícitos.
Fuentes primarias Microsoft, SAT y SEGOB consultadas. Glosario de macro/tarea
programada; notebook, muestras y prácticas obligatorias conservados.
Portal y cambios locales previos fuera del alcance educativo.
Verificación: 5726 enlaces locales sin incidencias y formato correcto; patrón
de folio contrastado con un caso aceptado y tres rechazados. HTML a 1280/390
sin desbordes ni IDs repetidos, lectura móvil revisada. No se ejecutaron macros,
archivos .vbs, tareas programadas ni consultas de identificadores reales.

**Depuración 00.02 — 2026-10-29, aplicaciones y curiosidad por regex:**
Sección breve después del diagnóstico de errores: scripts y ejemplos de
genómica (SeqKit/SAMtools), logs y datos climáticos (NCO), con fuentes primarias.
Regex como patrón de texto con dos líneas ficticias y ejemplo ^ERROR;
distinción de comodines y comprobación de forma frente a validez del dato.
Glosario amplía script/log/regex. Sin instalar herramientas, ampliar prácticas
obligatorias ni afirmar memoria acotada por usar terminal. Código y notebook
previos conservados; portal y cambios locales ajenos fuera del alcance.
Verificación: fuentes consultadas, ejemplo ^ERROR contrastado en PowerShell,
5726 enlaces locales sin incidencias y formato correcto. HTML a 1280/390
sin desbordes ni IDs repetidos; sección móvil revisada visualmente.
No se ejecutaron herramientas científicas ni se midió rendimiento.

**Depuración 00.02 — 2026-10-29, retos equivalentes con resultado oculto:**
Se conserva el ajuste del usuario «Extensión opcional» en PowerShell y se
mantiene un ancla para el título anterior. Ambos recorridos incluyen el reto
de ventas con al menos dos unidades, con resultado y explicación en details
cerrado por defecto. Dos registros: cuaderno (2) y lapiz (5), con límite
inclusivo y distinción entre contar ventas y sumar unidades.
Portal y cambios locales previos ajenos al ajuste permanecen fuera del alcance.
Verificación: ambos comandos contrastados con el CSV (dos ventas); 5726 enlaces
locales sin incidencias. Resultados cerrados por defecto y apertura comprobada
en HTML a 1280/390 sin desbordes. Formato y publicación selectiva revisados.

**Depuración 00.02 — 2026-10-29, arranque y recorrido esencial:**
PowerShell y Bash/Zsh incluyen apertura de terminal, ubicación en la copia
extraída, ruta real entre comillas y confirmación; VS Code como alternativa
si ya se usa. Núcleo visible: ubicación, listado, navegación, rutas y CSV;
consulta de herramientas separada del verificador condicional y de la extensión.
Objetivos, evidencia y lab alineados: Python ausente implica pendiente explícito
para 00.05; herramientas faltantes no impiden avanzar ni exigen instalar.
Fuentes oficiales Microsoft/VS Code contrastadas. Numeración, anclas, código,
CSV y notebook conservados. Portal y cambios locales previos fuera del alcance.
Verificación: 5726 enlaces locales sin incidencias; HTML de lección/lab a
1280/390 sin desbordes ni IDs repetidos, apertura PowerShell revisada visualmente.
Comprobación de formato correcta. Instrucciones de interfaz contrastadas con
documentación oficial; apertura manual de aplicaciones no acreditada.

**Depuración 00.02 — 2026-10-29, alcance del cuaderno guiado:**
Nota visible en lección y notebook: apoyo opcional para terminal; el aprendizaje
formal de notebooks, kernel y ejecución desde cero corresponde a 00.06.
Instrucciones de 00.02 simplificadas sin cambiar celdas ejecutables ni resultados.
00.06 recupera el uso previo de forma condicional, sin exigir ese ensayo.
Portal y cambios locales previos permanecen fuera del alcance.
Verificación: 5724 enlaces locales sin incidencias; código del notebook
idéntico al ya ejecutado. HTML de lección/cuaderno a 1280/390 sin desbordes
ni IDs repetidos. Ajuste editorial, sin repetir pruebas de código sin cambios.

**Depuración 00.02 — 2026-10-29, glosario y notebook para Colab:**
Lección con glosario contextual y notebook opcional `.ipynb` autocontenido:
preparación temporal, comandos Bash reales, rutas, CSV de tres ventas,
herramientas y ampliación de filtros/suma. Explicaciones, predicciones y
evidencia; no instala paquetes ni exige acceso al repositorio desde Colab.
Uso remoto separado de comprobación personal; cada celda Bash recupera su
ubicación y la preparación permite reconstruir tras reiniciar. Lab alineado
con ensayo opcional y pendientes explícitos. Verificador con Python existente;
se retira uv run de ese paso para no adelantar preparación del entorno.
Fuentes oficiales de Colab/IPython consultadas. Portal y privados previos fuera.
Verificación: notebook válido y ocho celdas ejecutadas en dos kernels nuevos
con Python/IPython y Git Bash existentes en Windows. Muestra CSV idéntica,
rutas y resultados contrastados; salidas de prueba solo en output. Archivo
publicado sin salidas ni contadores. Interfaz y ejecución alojada de Colab
pendientes de observación; no se modifican entornos ni lockfiles.
5722 enlaces locales sin incidencias; HTML de lección y notebook a 1280/390
sin desbordes ni IDs repetidos, con lectura móvil revisada visualmente.

**Depuración 00.01 — 2026-10-29, glosario y caso de IA:**
Plantilla de lección y guías de autoría incorporan un glosario breve antes de
referencias, con términos explicados también al aparecer. Primera aplicación
en 00.01: once términos, incluido repositorio, y acceso desde la cabecera.
El ejemplo de IA se titula «Caso de uso: organizar contexto e instrucciones
para IA»; conserva el ancla anterior. Aplicación a otras lecciones pendiente
de su revisión gradual. Portal y cambios locales previos fuera del alcance.
Verificación: 5716 enlaces locales sin incidencias; render 1280/390 sin
desbordes ni IDs repetidos, ancla antigua de IA conservada y glosario móvil
revisado visualmente. Comprobación de formato y publicación selectiva.

**Depuración 00.01 — 2026-10-29, propósito y casos de Markdown:**
La parte de Markdown inicia con definición, utilidad y problemas que ayuda a
resolver; después conserva la prueba de cinco líneas y fuente/resultado.
Casos de uso reunidos dentro de Markdown: apuntes, README, diccionario,
decisiones, notebooks, sitios de documentación, colaboración e IA.
Prompts y skills introducidos brevemente como formas de organizar contexto e
instrucciones reutilizables, sin práctica de instalación o creación de skills.
Fuentes primarias de Markdown, Jupyter, MkDocs, GitHub y OpenAI consultadas.
Lab alineado: elegir otro caso, con IA como una opción. Anclas previas preservadas;
Git/GitHub permanece después de Markdown. Portal y privados previos fuera.
Verificación: enlaces locales sin incidencias y render 1280/390 sin desbordes
ni IDs repetidos; fuente/resultado, sintaxis de código y anclas conservados.
Definición móvil revisada visualmente. Fuentes primarias contrastadas; skills
como concepto, sin instalar ni crear una skill como actividad del curso.


**Depuración 00.01 — 2026-10-29, primera prueba de Markdown:**
Markdown precede a Git/GitHub dentro de la lección. Prueba inicial de cinco
líneas, fuente y resultado visible; el ejemplo de perfil también muestra su
versión presentada. Sintaxis literal del código en línea aclarada. Vista previa
de VS Code enlazada como apoyo; archivo .md suficiente, sin Python/kernel.
Se conservan los contenidos posteriores, el lab y la numeración del módulo.
Anclas anteriores de los apartados preservadas para mantener enlaces existentes.
Edición acotada a los puntos 1/2 acordados; portal y privados previos fuera.
Verificados fuente de cinco líneas, dos resultados presentados, sintaxis literal
de código en línea y anclas anteriores/nuevas. Render 1280/390 sin desbordes ni
IDs repetidos; primera prueba móvil revisada visualmente. Enlaces locales sin
incidencias. Instrucción de vista previa contrastada con documentación oficial
de VS Code; no se acredita operación de la interfaz del editor por este render.


**Cierre de la ronda de revisión — 2026-10-29:**
Preparación de 05 aclarada en índice, lección y lab: conceptos previos necesarios,
pero la ejecución inicial usa CSV incluidos; una entrega personal de 04.09 sirve
para comparar y no bloquea empezar. Resultados esperados explícitos y bloques
de trabajo sin duración inventada. Pauta de pausa/reanudación en el flujo de
aprendizaje y aplicación concreta en 09–14: preparación, caso y revisión separados.
La .venv raíz no arrancaba por un intérprete local inexistente; se conservó en
una carpeta de respaldo excluida y se reconstruyó desde uv.lock con Python
3.12.12 existente, sin descargas ni cambios de pyproject/lockfile o bibliotecas
globales. Dependencias esenciales restauradas; grupos opcionales conservan sus
instrucciones por lección. Las 115 pruebas de 05 pasan desde la .venv reconstruida.
Revisión pendiente de 14.08 completada en las copias reconstruidas: dos apps,
seis HTML y muestras conciliados en doce comparaciones DOM a 1280/390.
Borrador, vacío, rechazo y sesiones independientes comprobados; HTML offline.
Doce vistas de material y dos diagramas revisados sin desbordes, IDs duplicados
ni soluciones abiertas. El control espera el fin del render de Streamlit antes
de comparar, sin filtrar elementos. Apps y cálculos sin cambios.
Registro de cierre actualizado; observación con estudiantes, IDE completo,
otras plataformas y proyectos/checkpoints mantienen su alcance posterior.
No se afirma reejecución de las 135 prácticas ni certificación del aprendizaje.
Portal y reorganización privada previos conservados fuera de esta publicación.
Verificación final: 15 módulos y 135 parejas lección/lab con navegación coherente;
5710 enlaces de 392 Markdown locales y 5714 de 394 en la copia publicable sin
incidencias. Once páginas finales a 1280/390, 22 vistas sin desbordes, IDs
duplicados ni soluciones abiertas. Corregida una ruta larga del lab 05.01 que
desbordaba en móvil. Preparación de 05 y pauta de reanudación revisadas en formato
renderizado. Los cambios publicados son documentales; entorno y respaldo quedan
locales y excluidos de Git.

**Revisión documental — 2026-10-29, base 00–14:**
Revisión de índices, guías, cierres y plantillas. Inventarios repetidos de 14
sustituidos por enlaces al módulo responsable; cierre integrado incorporado a
la tabla de consulta de docs/. Corregidos el plan obsoleto de 14 en Streamlit,
la elección futura de requisitos en Quarto y referencias futuras en pandas/Python.
Arquitectura sin duplicar el inventario por sección ni el párrafo de cierre.
Guías de módulo/lección alineadas con el patrón aplicado, con anclas anteriores
conservadas. Labs enfocados y cierres de varias sesiones diferenciados de
proyectos/checkpoints; plantilla de lab con evidencia, criterio de salida y
continuidad a la siguiente lección. Retirada referencia obsoleta a muestras
00/02.01 de bitácora desde almacenamiento; flujo vigente enlazado sin cambiar portal.
Sin cambios de código, datos, entornos, lockfiles ni evidencias de práctica.
Reorganización local previa y cambios del portal conservados fuera del commit.
La revisión de explicaciones/ejemplos y la observación de sesiones continúan;
no acredita auditoría teórica completa ni práctica del estudiante.
Comprobaciones: 15 módulos y 135 parejas lección/lab con enlaces recíprocos e
índices coherentes. 5702 enlaces de 392 Markdown locales y 5706 de 394 Markdown
en la copia exacta publicable sin incidencias; se distingue del estado local
del portal, cuyos cambios previos no se publican. 29 páginas renderizadas con
Pandoc y 58 vistas Chrome 1280/390 sin desbordes, IDs duplicados ni soluciones
abiertas. Índice documental móvil y arquitectura de escritorio revisados visualmente.
Solo documentación: no se repitieron pruebas de cálculo o apps sin cambios.

**Desarrollo — 2026-10-29, revisión final y defensa 14.09:**
Lección/lab, recorridos completos R/IDE, PowerShell y Bash, tres plantillas
personales pendientes por defecto: revisión, decisiones y acta. Ruta esencial
desde las 53 fuentes de 14.07; 14.08 conserva su carácter opcional. Sin modelos,
dependencias, lockfiles ni entornos globales nuevos. Predicción/observación y
explicación diferenciadas; comparación manual de las seis filas con CSV externo.
Siete grupos heredados, tres consultas trazadas/reportes y una app elegida.
Ensayo de reporte separado con 2600→2700, rechazo específico y original intacto.
Decisiones con alternativas/evidencia/consecuencias, límites y siguiente acción.
Acta humana, sin calificación ni certificación automática del aprendizaje.
Comprobación de autoría en copias nuevas Python 3.12.12/R 4.6.1 con renv 1.3.1:
siete grupos y tres consultas/HTML/verificaciones por ruta, ensayo de importe
rechazado específicamente y reporte original intacto; CSV externo conciliado.
Restauración local sin modificar bibliotecas globales ni metadatos raíz.
5699 enlaces locales de 392 Markdown sin incidencias; ocho páginas renderizadas
con Pandoc y dieciséis vistas Chrome 1280/390 sin desbordes ni IDs duplicados.
Lección móvil y acta de escritorio revisadas visualmente. Las apps se conservan
de 14.07, con sus comprobaciones previas; no se repitió su revisión UI en 14.09.
Rscript/Windows comprobados; operación completa del IDE y Bash/Linux pendientes.
Las nueve secciones de 14 completan la base de lecciones/labs 00–14; práctica,
proyectos/checkpoints, depuración transversal y cobertura del portal siguen aparte.
Estado y próximos criterios en docs/reproducible-projects-closure.md.

**Desarrollo — 2026-10-29, entrega y automatización opcional 14.08:**
Lección/lab opcionales, recorridos R/IDE, PowerShell y Bash, preparadores de
60 fuentes y paquete de 90 archivos. Catálogo explícito, 27 archivos de muestra,
descriptor, manual y manifiesto con 89 huellas. Tres casos conocidos: octubre
003/2600 sobre 3/4600; septiembre 002/2000 y 003/2500 sobre 3/4500;
selección vacía 0/3 válida. Revisor fuera del paquete, CSV externo completo
comparado por clave y campo, filtros fijos y productos conciliados. Verificación
de solo lectura con funciones propias del revisor: no ejecuta código recibido,
no abre .Rprofile. MD5 y fechas no autentican ni aprueban código para ejecutar.
Copia exclusiva de fuentes y reconstrucción explícita tras revisión/restauración:
siete grupos heredados, tres consultas trazadas y tres reportes por ruta.
Bibliotecas de cálculo e interfaces restauradas en copias nuevas Python/R,
sin cambios de dependencias, lockfiles raíz ni bibliotecas globales.
Catorce controles por lenguaje: lectura sin cambios, inventario/marca/ruta,
referencia externa, orden por clave, filtros, duplicados fuera del corte,
compensaciones con huellas renovadas, HTML, rutas inyectadas y sentinelas que
prueban ausencia de ejecución del modelo recibido. Junction R rechazada.
CI_EJEMPLO.yml queda inactivo: Windows/Python 3.12.12, ejecución manual,
permisos de lectura, acciones fijadas a SHA oficiales y pruebas estándar.
Comando local con venv sin pip comprobado; ejecución hospedada no acreditada.
Preparadores R/Python: 60 fuentes idénticas byte a byte. Destinos ocupados
rechazados, reconstrucción repetida sin reemplazar resultados y YAML validado.
5630 enlaces locales de 385 Markdown sin incidencias; seis páginas renderizadas
con Pandoc existente. Interfaces reconstruidas arrancan en localhost, pero la
nueva revisión visual/DOM de 14.08 quedó pendiente: la revisión automática de
permisos de Chrome expiró en dos intentos; no atribuirlo a un fallo del producto.
Sin despliegue, envío a terceros ni activación real de automatizaciones.
Rscript/Windows comprobados; operación completa del IDE y Bash/Linux pendientes.
14.01–14.08 disponibles; 14.08 es opcional. 14.09, proyectos/checkpoints y
práctica del estudiante siguen pendientes. Portal y privados previos fuera.

**Desarrollo — 2026-10-29, integración de reporte y app 14.07:**
Lección/lab y recorridos completos Python/Streamlit y R/Shiny, con IDE como
ruta principal R. Preparadores equivalentes de 53 fuentes; cálculo del pipeline
factorizado solo en la copia nueva, sin duplicar reglas ni alterar modelos/fuentes
de secciones previas. Lector de solo lectura comprueba fuente/configuración y
entrega antes de presentar. Raíz de cálculo mínima e interfaces con entornos
locales separados: lockfile Streamlit derivado de la resolución existente y
comprobado/restaurado con uv; Shiny reutiliza los 31 registros de 13.01.
Sin cambios de metadatos raíz ni bibliotecas globales. Bibliotecas R restauradas
desde tarball/archivos de paquetes existentes, sin copiar bibliotecas instaladas.
El activador elimina su tarball de arranque: se conserva otro archivo de origen.
Tres reportes Quarto por ruta, preparados sin Jupyter/knitr: selección/contexto,
producto.csv y .qmd, render HTML y verificador de lectura. Fotografía estática
distinguida de comprobación actual; identidad, hora UTC y filtros visibles.
Octubre 003/2600 y universo 3/4600; septiembre 002/2000 y 003/2500 sobre 3/4500;
vacío válido 0/3 y sin barras; sin universo rechazado, sin entrega.
Siete grupos heredados y once comprobaciones de integración por motor aprobados:
mezcla de cortes, destinos ocupados, app distinta, entrega ausente/incompleta,
HTML/.qmd/tablas alterados, fuente cambiada, duplicado fuera del corte,
compensaciones con huellas renovadas y restauración. Preparadores: 53 fuentes
idénticas con app explícita igual. Apps/reportes: doce comparaciones DOM a
1280/390, valores/tablas/barras conciliados, borrador sin aplicar, rechazo que
retira cifras y sesiones independientes. HTML offline comprobado en navegador.
MD5 no autentica; verificador no certifica el HTML completo ni accesibilidad.
No hay caché de cálculo/monitor de disco ni publicación atómica de productos.
Rscript/Windows comprobados; operación completa del IDE y Bash/Linux pendientes.
Revisión adicional: hora UTC canónica/calendario y versiones de interfaz explícitas.
Cuatro casos de fecha inválida por lenguaje rechazados aun sincronizando metadatos,
.qmd y HTML para aislar ese control. Fuente cambiada en navegador: ambas apps
retiran cifras; HTML histórico intacto y vista recuperada al restaurar. Botón con
teclado comprobado. 5585 enlaces locales de 380 Markdown sin incidencias; diez
vistas de documentación y diagrama a 1280/390 revisados; git diff --check limpio.
La integración local está disponible; 14.08/14.09, proyectos/checkpoints y
práctica del estudiante siguen pendientes. Portal y cambios privados previos fuera.

**Desarrollo — 2026-10-29, trazabilidad y recuperación 14.06:**
Lección/lab y recorridos R/IDE, PowerShell y Bash; preparadores equivalentes
de 33 fuentes. Nuevos trazadores alrededor del pipeline 14.04, sin cambiar
modelos, datos, suites 14.05 ni lockfiles. Eventos CSV por intento exclusivo,
consulta, huellas y diagnóstico; fallos antes/después de publicar y recálculo
con reutilización comprobada. Parciales y registros anteriores conservados;
sin reanudación de temporales ni recuperación automática.
Python 3.12.12/uv y R 4.6.1/renv 1.3.1 locales: secuencia principal y siete
grupos heredados aprobados en ambos motores. Diez comprobaciones adicionales
por ruta: cierre fallido y reutilización sin escritura, intento ocupado intacto,
septiembre por clave, vacío válido, sin universo, duplicado fuera del corte,
configuración inválida/ausente, compensación con huellas actualizadas y corte
abrupto sin evento terminal seguido de nuevo intento. Octubre 003/2600 y
universo 3/4600; septiembre 002/2000 y 003/2500 sobre 3/4500.
R restaurado desde tarball local existente; inconsistencia inicial de paquetes
base en ejecutor restringido resuelta comprobando con permisos de lectura
adecuados, sin desactivar sandbox ni controles. Rscript/Windows comprobados;
interfaz completa del IDE y Bash/Linux no acreditados. Los logs/MD5 no autentican
sesiones ni recuperan fuentes; la ausencia de cierre deja estado indeterminado.
Preparadores Python/R: 33 fuentes idénticas. Seis tablas selección/contexto
conciliadas; ejemplos mínimos ejecutados y conexiones R restauradas tras error.
5536 enlaces locales de 376 Markdown sin incidencias; diez vistas a 1280/390
y diagrama renderizado revisados, sin desbordamiento ni IDs duplicados.
git diff --check sin errores; dependencias y lockfiles anteriores intactos.
Retomar 14.07 — Integración de reporte y app, todavía planificada. No hay
proyecto/checkpoints ni aprendizaje acreditado. Portal y reorganización privada
previa conservan su alcance y cambios locales.

**Cierre documental — 2026-10-29 (antes de desarrollar 14.06):**
Revisados portada, roadmap, índices, guías y continuidades entre módulos.
Corregidas referencias antiguas que aún presentaban 14.04/14.05 como planes:
14.01–14.05 tienen lecciones/labs; 14.06–14.09 siguen pendientes. La siguiente
sesión de desarrollo comienza con 14.06 — Trazabilidad y recuperación de fallas,
sobre el pipeline comprobado de 14.04 y las suites de 14.05, sin exigir entregas
personales previas. Modelos, datos, paquetes y pruebas no se modifican en este
cierre; se conservan las comprobaciones de autoría registradas para 14.05.
Proyectos/checkpoints, práctica del estudiante e integración final siguen pendientes.
Verificados 5497 enlaces locales de 372 archivos Markdown sin incidencias y
git diff --check sin errores. Los cambios locales del portal y los archivos
privados se conservan por separado.

**Desarrollo — 2026-10-28, pruebas y calidad de datos 14.05:**
Lección/lab, recorridos R/IDE, PowerShell y Bash, preparadores de 31 fuentes.
Sin paquetes nuevos: modelos/pipeline/datos/metadatos 14.04 reutilizados,
unittest en Python y ejecutor R base con errores acumulados por grupo.
Siete grupos por ruta: nueve criterios literales, catorce fuentes inválidas,
orden/cero, integración/repetición de dos cortes, vacío/sin universo,
duplicado fuera del corte y alteración compensada con huellas actualizadas.
Comparaciones por ID/saldo, contexto, denominador y tolerancia explícita para
porcentajes; las suites no certifican cobertura completa ni datos futuros.
Fixtures nuevas conservadas en cada tanda; fuente/configuración originales
intactas, sin borrar ensayos ni reemplazar entregas anteriores. La entrega
alterada de prueba queda deliberadamente inválida. R 4.6.1/renv 1.3.1 local y
Python 3.12.12/uv, siete grupos aprobados en ambas rutas. Dos defectos controlados
por motor (>= a > y unicidad desactivada) producen fallas/código no cero;
restaurar recupera aprobación. Práctica del estudiante, proyecto/checkpoints,
CI y producto final integrado pendientes. Solo 14.01–14.05 disponibles;
Preparadores R/Python: 31 fuentes idénticas y rechazo de destino ocupado.
Ejemplos mínimos ejecutados; seis tablas selección/contexto conciliadas entre
motores. Fuentes conservadas tras los ensayos; activador renv solo cambia
espacios finales. Doce vistas Markdown a 1280/390 comprobadas y revisión visual
de muestra, sin desbordamiento/IDs duplicados, solución cerrada. Bash/Linux y
operación completa del IDE no acreditados. 5495 enlaces locales sin incidencias;
retomar 14.06. Portal y archivos privados fuera de esta entrega.

**Desarrollo — 2026-10-28, pipeline y reprocesamiento 14.04:**
Lección/lab, recorridos R/IDE, PowerShell y Bash; preparadores de 28 fuentes en
carpeta nueva. Python/R conservan modelos, datos y metadatos 14.03 sin paquetes
nuevos. Entrega de cuatro CSV: selección, contexto, insumos y COMPLETO; temporal
hermano, relectura por valor y publicación mediante renombrado a destino libre.
Repetir comprueba de nuevo y no escribe; cambios de fuente/configuración/código
registrados requieren otro destino. Sin append, reemplazo, escritores simultáneos
ni garantía de transacción/durabilidad completas. Fuente completa antes del filtro.
Octubre 003/2600, universo 3/4600; septiembre 002/2000 y 003/2500, universo 3/4500.
Siete consultas válidas y dos inválidas del contrato, 21 comprobaciones por ruta,
conciliación Python/R por campo; bytes/mtime al repetir, vacío, sin universo,
fuente vacía, duplicado fuera del corte, cambios de entrada/configuración,
entregas alteradas con suma/huellas conservadas, inventario/marca y fallo/reintento
comprobados en procesos nuevos. R 4.6.1/renv 1.3.1 local y Python 3.12.12/uv;
restauración real en copias con espacios. Bash/Linux y operación completa del
IDE no acreditados. Reporte/app, proyecto/checkpoints y práctica siguen pendientes.
Preparadores R/Python: 28 fuentes idénticas; destino ocupado rechazado. Guías
PowerShell/uv y helper R ejecutados. Doce vistas Markdown a 1280/390 sin
desbordamiento/IDs duplicados, solución cerrada y revisión visual de muestra;
5457 enlaces locales comprobados sin incidencias.
Solo 14.01–14.04 disponibles; retomar 14.05. Portal y privados fuera de esta entrega.

**Desarrollo — 2026-10-28, entornos y ejecución reconstruible 14.03:**
Lección/lab, preparadores equivalentes de 26 fuentes, metadatos mínimos reales
y ejecutores con registro nuevo de entorno/parámetros/resultado. Conserva las
fuentes de 14.02; entorno.csv declara Python 3.12.12/R 4.6.1. uv.lock generado
con uv contiene solo el proyecto sin dependencias externas; renv.lock generado
con renv 1.3.1 contiene solo renv, herramienta de biblioteca local. Sin paquetes
de análisis añadidos ni cambios de metadatos/entornos globales o previos.

Dos copias desde fuentes, con .venv y biblioteca R inicialmente vacíos, fueron
construidas/restauradas y ejecutadas en procesos nuevos, con rutas con espacios.
Doce registros: octubre en ambas copias, septiembre desde otra carpeta,
Quarto presente en PATH, vacío/sin universo; parámetros, resultados por crédito,
porcentajes y huellas de entrada/configuración conciliados con Python estándar.
Quarto 1.9.38 existente se detectó sin render/instalación; su ausencia en PATH
también se registra. No acredita preparación de reporte/app integrados.

Entorno base/sin activar, evidencia existente, metadatos uv/renv desalineados y
versión declarada distinta rechazados sin generar evidencia válida ni modificar
la previa. Lockfiles originales restaurados tras alteraciones; preparadores
rechazan destino ocupado. renv regenera espacios del activador; contenido
funcional contrastado y fuentes de modelo/configuración conservadas.

Recorridos IDE, PowerShell y Bash completos; operación completa del IDE y
Bash/Linux no acreditadas con Rscript Windows. Registros contienen rutas locales,
no autentican ejecuciones históricas y no garantizan escritura transaccional.
Seis páginas revisadas en doce vistas 1280/390, sin desbordamiento de página
ni IDs duplicados y soluciones cerradas; 363 Markdown y 5423 enlaces locales
sin incidencias. No hay pipeline, productos renderizados ni checkpoints implementados. Portal
y especificaciones privadas fuera de esta entrega; retomar 14.04.

**Desarrollo — 2026-10-28, estructura y configuración 14.02:**
Lección/lab, preparadores Python/R y copia organizada de trece archivos:
contrato/plantilla, entrada preservada, criterios de referencia, modelos,
configuración, revisores y guía de salidas. Modelo derivado de las referencias
14.01 conserva contrato/indicadores; configuración CSV con siete claves exactas,
valores textuales validados, raíz explícita y destinos nuevos previstos.
Los revisores leen e imprimen, sin crear/reservar salida, iniciar app/reporte,
instalar paquetes o simular un pipeline. App elegida no altera los indicadores.

Python 3.12.12/R 4.6.1: nueve casos del contrato (entrada inválida rechazada
antes del cálculo), dos elecciones de app y 22 configuraciones inválidas más
fuente duplicada contrastados. Claves ausentes/repetidas/extra, versión, calendario,
segmentos, mínimo, rutas y destinos ocupados comprobados. Ejecución desde otra
carpeta y copia movida con espacios; hash/fechas/archivos intactos al revisar.
Ambos preparadores producen trece archivos equivalentes y rechazan destinos
existentes. Fuente original intacta, sin paquetes/entornos/lockfiles nuevos.
Recorrido principal IDE/consola R y alternativas PowerShell/Bash separadas;
operación completa del IDE y Bash/Linux no acreditadas por Rscript Windows.

Seis páginas renderizadas en doce vistas 1280/390, sin desbordamiento de página
ni IDs duplicados y soluciones cerradas; 359 Markdown y 5382 enlaces locales
sin incidencias. Solo 14.01–14.02 disponibles; retomar 14.03. Integración final, pipeline,
entornos reconstruibles y checkpoints siguen pendientes. Portal y documentos
privados fuera de esta entrega.

**Desarrollo — 2026-10-28, pregunta y contrato del producto 14.01:**
Lección/lab, especificación resuelta, plantilla personal y nueve criterios de
aceptación con IDs/saldos por crédito, universo, medidas y estados. Seis filas
sintéticas de 12.03 copiadas sin alterar la fuente. Pregunta/público, contrato
de datos/cálculo/producto, denominadores y cero/vacío/sin universo/rechazo;
aceptación futura separada de comprobación aritmética actual. Un reporte HTML
y una app elegida; sin implementar pipeline, integración o checkpoints.

Referencias Python estándar/R base de solo lectura: nueve casos literales y
360 combinaciones conciliados. Seis alteraciones rechazadas en ambas rutas:
porcentaje, saldos compensados, duplicado fuera del corte, fecha inválida,
saldo ausente y fila vacía. Frontera adicional del lab comprobada; copia en ruta
con espacios y originales conservados. Python 3.12.12/R 4.6.1 de revisión;
sin paquetes nuevos, restauraciones, cambios de entornos o lockfiles.

Índices, roadmap y continuidades de cierres actualizados: solo 14.01 disponible;
14.02–14.09 conservan su plan. Portal y documentación privada fuera de la entrega.
Retomar 14.02; la integración final, proyectos/checkpoints y práctica personal
requieren implementación y evidencia propias.

**Revisión documental — 2026-10-28, continuidad después del cierre de Shiny:**
Inventario contrastado: 126 parejas lección/lab en 00–13; 14 sin lecciones/labs
implementados y projects/ sin proyectos ejecutables. Corregidas referencias
desfasadas de Quarto 11.09 y del plan 14 que aún trataban las apps como planes.
Ambas rutas de aplicación tienen cierre local, sin acreditar práctica personal
ni activar proyectos/checkpoints. Criterios de almacenamiento/tidyverse/reportes,
catálogo de proyectos, índice documental y arquitectura enlazan las dos alternativas.

Arquitectura distingue el proyecto R de análisis del proyecto independiente de
Shiny. Guía de autoría distingue disponibilidad de recorridos y comprobación
real del IDE, y no exige checkpoints inexistentes. Instrucciones locales
depuradas en sus referencias de estado/reanudación; se conservan privadas.
Solo documentación educativa: sin cambios de código, dependencias o portal,
sin ejecutar de nuevo las suites de apps por cambios de texto. Las modificaciones
locales anteriores del portal y su reorganización documental se mantienen aparte.
Comprobación: 349 Markdown y 5307 enlaces locales sin incidencias, diff sin
errores de espacios y cinco documentos renderizados a 1280/390, sin
desbordamiento de página ni IDs duplicados. Se mantiene 14 como plan.

**Desarrollo — 2026-10-28, cierre y entrega local Shiny 13.10:**
Lección/lab, contrato, seis preguntas, instrucciones autocontenidas, preparador
de 24 fuentes y constructor/verificador R. Entrega base de 41 archivos:
fuentes, resumen/nota/huellas, cinco selecciones y cinco contextos CSV y cuatro
PNG 960 × 600. Cero/frontera conservan 2500 MXN con distinta cantidad; vacío
exporta encabezado y contexto, sin universo conserva indicadores ausentes y no
genera exportaciones de vista. Lote y descargas HTTP diferenciados.

App/módulo de 13.08, pruebas de 13.09, funciones/CSV/metadatos previos intactos
por copia. Mismo lockfile de 42 registros: R 4.6.1/Shiny 1.14.0/ggplot2 4.0.3/
renv 1.3.1, sin dependencias nuevas ni cambios globales. Dos bibliotecas locales
restauradas desde vacías; reconstrucción solo desde fuentes recibidas, en ruta
con espacios, pruebas completas y seis casos recalculados. Tablas de ambas
entregas conciliadas independientemente con Python estándar por clave/campo;
cuatro figuras reconstruidas revisadas visualmente.

Verificador de solo lectura con CSV externo y cálculo R base independiente;
fuente, preguntas, tablas, ausencias, inventario/huellas y cabecera/dimensiones
PNG. Ocho alteraciones rechazadas aun con huellas renovadas: valores compensados
en selección/fuente, porcentaje, ausencia cambiada por cero, casos reducidos,
PNG, código ausente y exportación no prevista. Archivos/fechas de modificación
intactos al verificar; código/app/perfil deliberadamente alterados no se ejecutan.
Por tanto, verificar no certifica toda la lógica recibida ni la sesión histórica.
Destinos existentes/internos y referencias internas rechazados; fuentes vacía
y de un crédito con cero comprobadas, originales conservados.

Chrome headless 1280/390 sobre la reconstrucción: estado por panel/sesión,
borrador/aplicada, tabla oculta, rechazo, cero/vacío/sin universo, bloqueo y
recuperación; cuarenta descargas actuales releídas contra CSV independiente.
IDE/consola R principal, terminales separadas; operación completa de la interfaz
del IDE y Bash/Linux no acreditadas con Rscript Windows. Huellas sin autenticidad,
nota generada sin certificar demostración humana y lockfile sin garantía de
disponibilidad futura. Portal y especificaciones privadas fuera de esta entrega.

Ocho páginas renderizadas en dieciséis vistas 1280/390, soluciones cerradas,
sin desbordamiento de página y con IDs únicos; 349 Markdown y 5292 enlaces
locales sin incidencias. Las diez secciones de Shiny tienen material. Criterios y reanudación en
docs/shiny-closure.md; práctica personal, proyecto/checkpoints y módulo 14 siguen
pendientes. Retomar revisión de práctica/cierre y diseño de 14, sin darlo por implementado.

**Desarrollo — 2026-10-28, pruebas y observación del flujo Shiny 13.09:**
Lección/lab, mínimo autónomo número/doble/nota y pruebas con R base y testServer.
Expectativas literales, identical frente a all.equal, inicialización de entradas/
botón antes del primer evento, rondas reactivas y límites de la simulación.
Funciones: seis observaciones completas, siete consultas por crédito, frontera
inclusiva, cero/vacío/sin universo, rechazo y fuente completa antes del filtro;
catorce CSV temporales escritos/releídos, contexto y capas ggplot comprobados.
Servidor: borrador/aplicada, rechazo, bloqueo por duplicado fuera del corte,
ausencia y recuperación; sesión nueva, dos instancias, API del padre y namespaces.

App/módulo de 13.08 y funciones/fuente/metadatos anteriores conservados por copia.
Preparador exclusivo de veinte archivos; biblioteca local restaurada desde vacía,
R 4.6.1/Shiny 1.14.0/ggplot2 4.0.3/renv 1.3.1 y mismos 42 registros del lockfile
13.07. Sin dependencias nuevas ni cambios de Conda o bibliotecas globales.
IDE/consola R es recorrido principal; PowerShell y Bash separados. La operación
completa de la interfaz del IDE sigue pendiente, sin acreditarla con Rscript.

Chrome headless a 1280/390: mínimo y mensajes por número, nota sin recálculo;
app con aplicada/borrador, tabla oculta, cero/vacío, rechazo, bloqueo/recuperación,
sesión nueva/recarga y cuarenta descargas reales releídas por Python por clave/
campo/contexto. Se distinguen de los catorce CSV temporales de las pruebas R.
Seis regresiones deliberadas detectadas con fallo concreto: texto aislado,
frontera exclusiva, denominador de selección, resumen fijo, índice CSV y saldos
erróneos compensados. Frontera adicional del lab comprobada; originales
restaurados y conjunto esencial final correcto en proceso nuevo.

Lección/lab, índice, recorridos y cobertura renderizados en diez vistas a dos
anchos: sin desbordamiento de página, IDs únicos y soluciones cerradas.
343 Markdown y 5237 enlaces locales sin incidencias; diff sin errores de espacios.
Trazas de consola esenciales; reactlog opcional, sin instalarlo ni acreditar
su visor. No se infiere rendimiento ni ausencia de todos los errores. Portal
y especificaciones privadas fuera de esta entrega. Retomar 13.10; entrega,
proyecto/checkpoints y práctica personal siguen pendientes.

**Desarrollo — 2026-10-28, organización y módulos Shiny 13.08:**
Lección/lab, mínimo autónomo y módulo de consulta reutilizado dos veces. NS
separa controles/salidas estáticos; session$ns identifica botones dinámicos.
moduleServer conserva estado dentro de cada instancia y devuelve una API
reactiva de lectura que el padre utiliza para comparar consultas. Ruta de fuente
explícita; funciones de datos, validación y presentación anteriores conservadas.
Se distinguen instancia, sesión y archivo compartido, sin confundir aislamiento
del estado con una copia privada de la fuente.

Preparador de diecisiete archivos, recorrido IDE y alternativas PowerShell/Bash.
DESCRIPTION y lockfile de 13.07 idénticos: 42 registros, sin paquetes nuevos.
Restauración local desde biblioteca vacía con R 4.6.1, Shiny 1.14.0 y renv 1.3.1;
sin modificar Conda ni bibliotecas globales. Operación completa de la interfaz
del IDE pendiente; Rscript y navegador real no la acreditan.

Controles testServer del mínimo, módulo y app padre: siete consultas, API,
rechazo, duplicado fuera del filtro, ausencia de fuente y recuperación independiente.
Chrome headless a 1280/390 comprueba controles, namespaces dinámicos, borrador,
tabla oculta, cero/vacío/sin universo, sesiones nuevas y recarga. Cuarenta CSV
base y cuatro de la variante principal descargados realmente y releídos contra
referencia independiente; cambiar el ID exige solo las dos llamadas del padre.
Seis regresiones deliberadas detectadas: namespaces estático/dinámico, prefijo
incorrecto en servidor, estado compartido, ID disparejo y API no reactiva.

Lección/lab y apoyos revisados a dos anchos, diagrama Mermaid comprobado;
340 Markdown y 5197 enlaces locales sin incidencias. Captura propia de ambas
consultas incorporada. Portal y especificaciones privadas fuera de esta entrega.
Retomar 13.09; proyectos/checkpoints y práctica personal siguen pendientes.

**Desarrollo — 2026-10-28, gráficos, tablas y descargas Shiny 13.07:**
lección/lab, mínimo tabla/CSV y app con barras ggplot2, tabla y CSV de selección/
contexto desde la misma consulta aplicada. geom_col conserva saldos por crédito,
etiquetas, base cero, unidades y subtítulo del corte; alt reactivo incluye IDs/
saldos. Sin filtros nuevos de presentación ni datos recalculados desde borrador.
CSV selección conserva cuatro columnas, sin índice; contexto registra filtros,
universo, medidas y porcentaje sin redondeo de presentación. Dos solicitudes
independientes: descargar ambas antes de aplicar otra consulta; no constituyen
una entrega reconstruible completa ni autentican ejecuciones anteriores.

Vacío sobre universo exporta encabezado de selección y una fila de contexto,
sin barras inventadas. Inicio/sin universo/bloqueo no ofrece descargas, y cada
handler vuelve a exigir consulta utilizable al ejecutarse. Rechazo con consulta
anterior válida y borrador pendiente exportan esa instantánea identificada.
Ocultar tabla no cambia gráfica ni descargas; cambiar fuente sin aplicar no
actualiza la instantánea. Archivo temporal de Shiny y destino del navegador
diferenciados, relectura con IDs textuales y precisión/unidades explicadas.

DESCRIPTION directo shiny/ggplot2 y lockfile real propio: ggplot2 4.0.3, 42
registros con los 31 anteriores idénticos. Once paquetes añadidos; dos bibliotecas
locales comprobadas, la segunda restaurada desde vacía, con R 4.6.1, Shiny 1.14.0 y renv 1.3.1.
Preparador exclusivo de dieciséis archivos. cartera.R/consulta.R/validacion.R,
CSV, iniciador/restaurador y contenido Rproj anteriores intactos; proyecto
shiny_1307.Rproj. Sin cambios de Conda, bibliotecas globales, metadatos Python
o lockfiles previos. Recorrido principal IDE, PowerShell/Bash opcionales;
operación completa de la interfaz del IDE pendiente, sin acreditarla con Rscript.

Siete consultas por clave/campo: ggplot_build contrasta datos, alturas, categorías
y etiquetas; alt, fila cero única y vacío. CSV temporales releídos con encabezado
estricto para no inferir un índice como row.names; contexto y bloqueo de falta
de universo comprobados. Mismos controles en ambas bibliotecas. Seis regresiones
detectadas en copias: conteo en vez de saldo, exportar universo, índice extra,
contexto con mínimo falso, vacío con fila inventada y exportación sin universo.
Original restaurado, fronteras del preparador y fuentes/metadatos comprobados.

Chrome headless a 1280/390: descargas reales del mínimo, selección/contexto,
borrador pendiente, tabla oculta, octubre, cero, vacío, rechazo y dos sesiones.
Treinta y seis archivos releídos con csv de Python y referencia externa: columnas,
IDs/cortes/saldos, filtros, indicadores, porcentaje y nombres conciliados. Figura/
alt, recuperación de fuente ausente/inválida, sin universo, recarga y URL antigua
de descarga sin servir datos bloqueados comprobados. Capturas de figura/cero y
consulta seleccionadas revisadas; captura propia incorporada como apoyo.
Diez vistas GFM a dos anchos, imagen cargada, IDs únicos, sin desbordamiento y
soluciones cerradas; grafo Mermaid parseado/renderizado y enlaces/diff --check
comprobados. Servidores propios detenidos. Portal/reorganización privada fuera.
Retomar 13.08 — Organización y módulos; cierre/proyecto y práctica pendientes.

**Desarrollo — 2026-10-28, validación y mensajes Shiny 13.06:**
lección/lab, mínimo req/validate/need y app de cartera con saldo mínimo textual.
Contrato léxico explícito antes de convertir, sin truncar ni imputar: vacío,
signos, espacios, decimales, notación científica, ceros iniciales y exceso de
rango rechazados. Cero conocido y ningún segmento siguen siendo válidos.
Espera, rechazo, selección vacía, corte sin universo, fuente fallida y error
inesperado diferenciados. req silencioso, propagación de validate/need y
cancelOutput frente a estado explícito explicados con referencias primarias.

Cada Aplicar relee/valida toda la fuente antes del borrador. Rechazo conserva
consulta anterior identificada; fuente ausente/inválida o fallo inesperado
retira consulta disponible y cifras. Selección vacía sobre tres créditos conserva
0/0/0%; sin universo no hay indicadores. Noviembre es opción sin filas nuevas.
Aviso general independiente de casilla; validación silenciosa en consumidores
evita repetir el mismo bloqueo. El mínimo sí demuestra propagación visible.
No hay monitor de archivos ni invalidación global de otras sesiones: cada una
comprueba al aplicar. Corrección de fuente requiere aplicar, no reiniciar.

Preparador exclusivo de quince archivos, validacion.R nuevo; cartera.R de 13.04,
consulta.R de 13.05 y CSV de seis observaciones de 12.03 intactos byte por byte.
Metadatos/iniciador/restaurador de 13.01 conservados y proyecto shiny_1306.Rproj.
Restauración real en biblioteca local nueva: mismos 31 registros, R 4.6.1,
Shiny 1.14.0 y renv 1.3.1. Sin paquetes nuevos ni cambios globales, Conda o
metadatos Python. Recorrido principal IDE y terminal PowerShell/Bash opcional;
revisión completa de la interfaz del IDE pendiente, sin acreditarla con Rscript.

Funciones/testServer: entradas, condiciones de salida, rechazo, cero/vacío,
noviembre, fuente ausente/inválida/solo encabezado, recuperación y fallo de cálculo
inyectado. CSV temporal con limpieza, sin escribir la fuente de práctica. Seis
regresiones detectadas en copias: fuente fallida conserva cifras, rechazo borra
consulta, falta de universo publica indicadores, léxico admite 01, ninguno pasa
a todos y umbral exclusivo. Original restaurado, fronteras y metadatos comprobados.

Chrome headless a 1280/390: mínimo y propagación de mensajes, entradas rechazadas,
contexto/celdas/medidas, cero/vacío/sin universo, avisos con tabla oculta, ausencia
de fuente desde apertura y tras consulta válida, duplicado de octubre consultando
septiembre, encabezado solo y recuperación completa. Dos sesiones conservan
instantáneas hasta nueva aplicación; recarga y teclado comprobados. Mejora visual
de aviso único verificada de nuevo en navegador. Diez vistas GFM, IDs únicos,
sin desbordamiento y soluciones cerradas; capturas seleccionadas revisadas.
Diagrama de decisiones Mermaid parseado/renderizado con biblioteca de Quarto y
revisado visualmente. Enlaces/diff --check comprobados. Servidores propios
detenidos; portal y reorganización privada fuera del alcance. Retomar 13.07 —
Gráficos, tablas y descargas, todavía planificado; proyecto y práctica pendientes.

**Desarrollo — 2026-10-28, eventos y estado de sesión Shiny 13.05:**
lección/lab, mínimo número editado/guardado y app de cartera con borrador y
consulta aplicada. actionButton, bindEvent con observe, ignoreNULL/ignoreInit,
reactiveVal por sesión y diferencias respecto de reactive/reactiveValues.
Estado inicial NULL sin consulta; aplicar construye filtros/universo/selección/
indicadores antes de escribir una lista completa. Contexto y resultados leen
solo consulta aplicada; pendientes compara borrador, casilla no envía. tryCatch
rechaza intento sin reemplazar consulta anterior; el primer rechazo sigue sin
consulta. Cero y ningún segmento conservan las reglas previas. No hay archivos
de estado, autenticación, operaciones externas ni persistencia tras recarga.

Preparador exclusivo de catorce archivos, nuevo consulta.R y cartera.R de 13.04
reutilizado byte por byte, mismo CSV de seis observaciones de 12.03. Metadatos/
iniciador/restaurador de 13.01 intactos; proyecto shiny_1305.Rproj con contenido
anterior y nombre nuevo. Restauración real en biblioteca local nueva, mismos
31 registros: R 4.6.1, Shiny 1.14.0 y renv 1.3.1, sin paquetes nuevos ni cambios
globales, Conda o metadatos Python. Recorrido IDE y PowerShell/Bash opcionales;
operación completa de la interfaz del IDE sigue pendiente y no se acredita con Rscript.

Funciones/testServer: siete consultas por clave y cada campo, contexto aplicado,
cantidad/saldo/porcentaje, edición sin envío, rechazo sin reemplazo, repetición,
nueva sesión y mínimo. Seis regresiones detectadas en copias: aplicación al
editar, aplicación al inicio, estado global, contexto del borrador, rechazo que
borra consulta y ningún segmento convertido a todos. Original restaurado y
comprobado; fronteras del preparador y fuentes/metadatos previos intactos.

Chrome headless a 1280/390: inicio sin consulta, mínimo, siete consultas,
pendientes y regreso al borrador aplicado, contexto/celdas/medidas, rechazo
primero y posterior, recuperación explícita, cero/vacío, repetición, ocultación,
Enter en campo sin envío y Space en botón con envío. Dos sesiones simultáneas
con consultas/borradores distintos; recargar A pierde su estado y conserva B.
Diez vistas GFM a dos anchos, IDs únicos, sin desbordamiento y soluciones
cerradas; capturas seleccionadas revisadas. Esquema de acción/estado Mermaid
parseado/renderizado y revisado con biblioteca incluida en Quarto. Enlaces
locales/diff --check comprobados. Servidores propios detenidos. Portal y
reorganización privada fuera del alcance. Retomar 13.06 — Validación y mensajes,
todavía planificado; proyecto/checkpoints y práctica del estudiante pendientes.

**Desarrollo — 2026-10-28, filtros e indicadores compartidos Shiny 13.04:**
lección/lab, mínimo autónomo de tres créditos y app de cartera con corte,
segmentos, saldo mínimo inclusivo y casilla de tabla. Fuente completa, universo
del corte, selección e indicadores separados; tabla y medidas comparten la
selección. Cantidad/saldo y porcentaje de créditos sobre el universo anterior
a segmento/mínimo, con contexto vigente. Seis observaciones del CSV de 12.03
conservadas: tres créditos por corte, septiembre 4500/octubre 4600 MXN; mínimo
2000 selecciona 002/003 y 4500 en septiembre, 003 y 2600 en octubre. Cero
conocido, vacío y ausencia de universo diferenciados; ningún segmento selecciona
cero filas, no todos. Umbral/redondeo/denominador y conciliación por clave
explicados con grafo Mermaid y lectura textual; referencias primarias consultadas.

cartera.R contiene lectura/contrato/filtros/resumen sin Shiny ni lectura al
hacer source; valida toda la fuente antes del filtro. ID/corte único, categorías,
fechas reales, saldo entero conocido 0–1000000 y límite didáctico de 10000
observaciones. Preparador exclusivo de trece archivos con CSV copiado sin
cambios y proyecto shiny_1304.Rproj. DESCRIPTION/lockfile/iniciador/restaurador
de 13.01 conservados byte por byte. Restauración real en biblioteca local nueva:
R 4.6.1, Shiny 1.14.0, renv 1.3.1 y mismos 31 registros; sin dependencias nuevas,
cambios globales, Conda o metadatos Python. IDE como recorrido principal,
PowerShell/Bash opcionales. Operación completa de la interfaz del IDE sigue
pendiente; las ejecuciones Rscript/navegador no se atribuyen a esa revisión.

Doce escenarios explícitos de funciones/testServer por ID y campo; controles
de vacío, cero, 1900/1901 y 2500/2501, caché y ocultación. Cruce independiente
de 96 combinaciones con el modelo Python existente: IDs, cantidad, saldo y
porcentaje conciliados. Orden inverso, fuente vacía, fechas/valores inválidos,
límite de registros y suma de 1000 créditos a 1000000 comprobados. Seis
regresiones detectadas en copias: frontera exclusiva, denominador seis, tabla
sin filtro, vacío convertido a todos, cero eliminado y saldos compensados.
Siete CSV inválidos rechazados, incluso incidentes fuera del corte solicitado;
control original restaurado y comprobado. No es un lector general de limpieza.

Chrome headless a 1280/390: mínimo, diez escenarios, contexto, celdas completas,
cantidad/saldo/cobertura, tabla oculta con cambio de filtros, reutilización,
dos sesiones, recarga y teclado. Variante exclusiva con etiquetas/contexto
coherentes comprobada en procesos nuevos; copia restaurada y servidores propios
detenidos. Diez vistas GFM, soluciones cerradas, IDs únicos y sin desbordamiento;
capturas seleccionadas revisadas. Grafo parseado/renderizado con Mermaid de
Quarto y revisado visualmente, sin instalar. Enlaces locales y diff --check
comprobados. Portal y reorganización privada conservados fuera del alcance.
Retomar 13.05 — Eventos y estado de sesión, todavía planificado; proyecto,
checkpoints y práctica del estudiante siguen pendientes.

**Desarrollo — 2026-10-28, modelo de reactividad Shiny 13.03:**
lección/lab, mínimo número/doble con nota independiente y rama de demanda;
app de ventas con consulta reactive compartida entre resumen y tabla, y observe
solo de diagnóstico. Productores/consumidores, grafo por lecturas, invalidación
frente a ejecución, caché por expresión/sesión y conexiones condicionales. Dos
diagramas Mermaid y alternativa textual; diferencias reactive/render/observe,
contexto reactivo y errores habituales. Fuentes primarias Posit y Mastering Shiny
consultadas; ejemplos propios. No promete orden de mensajes ni ejecutar todo
app.R ante un cambio. No adelanta cartera/filtros de 13.04, eventos o persistencia.

Preparador exclusivo de doce archivos; funciones ventas.R de 13.02 copiadas sin
cambios, proyecto shiny_1303.Rproj y metadatos/iniciador/restaurador de 13.01
conservados byte por byte. Restauración real en biblioteca local nueva: R 4.6.1,
Shiny 1.14.0, renv 1.3.1 y mismo lockfile de 31 registros, sin nuevas dependencias
ni cambios globales, Conda o metadatos Python. Recorrido principal en IDE y
alternativas completas PowerShell/Bash. La operación completa de la interfaz
del IDE sigue pendiente; no se atribuyen las ejecuciones Rscript a esa revisión.

testServer contrasta cada campo de cinco consultas y las cifras 4/660, 1/300,
1/240, 1/0 y 1/120 MXN; nota/casilla, reutilización y sesión nueva. Sonda sin
outputs comprueba invalidación sin demanda y ramas; isolate/contadores son
instrumentación de autoría. Chrome real headless a 1280/390 contrasta UI inicial,
celdas, marcas de ejecución, mínimo 2/4, 3/6, pausa y 7/14, cero, nota, casilla,
consulta con tabla desactivada, dos sesiones, recarga y teclado. Variante de
lectura antes del if y retirada de observe comprobadas en procesos nuevos;
las cifras permanecen y cambian las trazas previstas. Servidores propios detenidos.

Fronteras del preparador y cinco regresiones detectadas en copias: eliminar
caché, dependencia accidental de nota, doble incorrecto, precios compensados
con total 660 y eliminación del cero. Control original restaurado y comprobado.
Diez vistas GFM a dos anchos, soluciones cerradas, IDs únicos y sin desbordamiento;
capturas seleccionadas revisadas. Dos grafos parseados/renderizados con Mermaid
incluido en Quarto y revisados visualmente, sin instalar. Enlaces locales y
git diff --check comprobados. Portal/reorganización privada fuera del alcance.
Pausa solicitada: retomar 13.04 — Filtros e indicadores compartidos, todavía
planificado; proyecto/checkpoints y práctica del estudiante siguen pendientes.

**Desarrollo — 2026-10-28, entradas y salidas Shiny 13.02:**
lección/lab, mínimo textInput/eco y app con selector nativo de venta/todas y
casilla de detalle. ID/etiqueta/valor, entradas character/logical, parejas
textOutput/renderText y tableOutput/renderTable, guarda de inicio NULL y
texto escapado. Misma muestra de cuatro ventas/660 MXN; V003 conserva una
fila/0. Ocultar el detalle no cambia consulta; recuperación y cambio mientras
está oculto muestran la consulta vigente. Sin reactive() compartido, eventos
propios, persistencia, descarga ni validación general de fuentes.

ventas.R contiene funciones R corrientes sin Shiny. Preparador exclusivo de
doce fuentes, proyecto de copia shiny_1302.Rproj y configuración local reutilizada.
DESCRIPTION/renv.lock, contenido Rproj, restaurador e iniciador de 13.01 idénticos;
31 registros, R 4.6.1/Shiny 1.14.0/renv 1.3.1. Restauración local desde biblioteca
vacía comprobada, sin dependencias nuevas ni cambios en fuentes/entornos previos,
Conda, metadatos Python o bibliotecas globales. No exige entregas anteriores.

Controles de funciones, cinco consultas por campos completos, ocultar/recuperar,
NULL inicial y texto/vacío/HTML pasaron. testServer fija entradas y no monta UI;
no acredita opciones iniciales/etiquetas. Siete ejecuciones adicionales:
control con UI variante, fronteras del preparador y cinco regresiones detectadas
(ID de entrada, ID de salida, casilla invertida, importes compensados con total
660 y cero eliminado). Fuentes de revisión restauradas tras cada experimento.

Chrome headless Windows a 1280/390: cinco consultas, todos los campos, texto
vacío y HTML literal, ocultar/cambiar/recuperar, sesiones nuevas, recarga y teclado
comprobados. Variantes del lab desde procesos R nuevos: etiqueta Conjunto
completo conserva valor todas/660; selected V004 inicia una fila/120 y recarga
reinicia selección/casilla. Captura propia con alternativa textual. No acredita
revisión completa del IDE; el recorrido principal del estudiante mantiene
proyecto/sesión nueva en RStudio o IDE elegido y terminal como apoyo opcional.

Diez vistas GFM de lección/lab/índice/recorridos/cobertura a 1280/390: imagen
cargada, IDs únicos, sin desbordamiento y soluciones cerradas; capturas revisadas.
4917 enlaces locales/fragmentos sin incidencias y git diff --check correcto.
13.01–13.02 disponibles; retomar 13.03 — Modelo de reactividad. 13.03–13.10 y 14
mantienen planes; proyectos/checkpoints y aprendizaje requieren evidencia propia.
Portal y reorganización privada conservados fuera de este alcance educativo.

**Desarrollo — 2026-10-28, web básica y primera app Shiny 13.01:**
lección/lab, mínimo y app de cuatro ventas sintéticas. Navegador/UI/proceso R,
HTML/CSS/JavaScript de contexto, objeto app y runApp, preparación/sesión/salida,
inicio/detención y reconstrucción. Ejemplos completos, diagrama con alternativa
textual y captura propia. Sin controles todavía: 13.02 y modelo reactivo 13.03
siguen planificados; no se implementan filtros, estado propio o descargas.

Preparador exclusivo de once fuentes, proyecto renv independiente sin entregas
anteriores, perfil/activador/ajustes de 06.08 reutilizados y biblioteca local.
Shiny 1.14.0/renv 1.3.1/R 4.6.1: lockfile real de 31 registros, dos restauraciones
desde bibliotecas vacías y estado sincronizado comprobados. No se inicializa renv
en raíz ni se alteran proyectos R previos, bibliotecas globales, Conda o metadatos
Python. Preparar solo copia; restaurar instala localmente; iniciar escucha 127.0.0.1.

Controles de objetos app, resumen y 16 celdas contra expectativas explícitas;
base 300/240/0/120, total 660. Variante V004/150, total 690 desde proceso nuevo.
Siete ejecuciones adicionales: fronteras/destinos ocupados, base restaurada,
regresión de total, compensación con total conservado, ID de salida incorrecto,
variante y rechazo de esperado base en variante. Fallos detectados, fuentes y
metadatos conservados. El control usa testServer como apoyo opcional de autoría,
sin presentar pruebas reactivas como lección ya desarrollada.

Chrome headless Windows: mínimo, cuatro filas/660 a 1280/390, idioma y ancho;
recarga y tres sesiones con una preparación observadas. Variante 690 con todos
los campos conciliados. Al detener el servidor propio, texto retenido/conexión
cerrada y recarga rechazada sin servidor comprobados; servidores temporales detenidos.
RStudio abrió con R 4.6.1; no se acredita la revisión completa del IDE: el control
de escritorio no permitió verificar foco fiable para ejecutar en consola. No se
escribieron comandos allí; restauración y reinicios se comprobaron en Rscript.
El recorrido principal del estudiante permanece en su IDE con sesión nueva.

Diez vistas GFM de lección/lab/índice/recorridos/cobertura a 1280/390: imagen
cargada, IDs únicos, sin desbordamiento y soluciones cerradas; capturas revisadas.
4867 enlaces locales/fragmentos sin incidencias; git diff --check correcto.
13.01 disponible; retomar 13.02 — Entradas y salidas. 13.02–13.10 y 14 mantienen
planes; proyectos/checkpoints y aprendizaje requieren evidencia propia. Portal,
especificaciones privadas y cambios locales previos conservan su alcance.

**Desarrollo — 2026-10-28, cierre y entrega local Streamlit 12.09:**
lección/lab, preparador, instrucciones autocontenidas y entrega.py con acciones
exclusivas crear/verificar. Reutiliza las fuentes de 12.03/05/06/07/08 sin cambiar
algoritmos ni exigir entregas previas. Entrega de 36 archivos: código/pruebas,
fuente/contrato, metadatos bloqueados, seis análisis y cinco pares CSV/JSON de
terminal, con manifiesto SHA-256. Noviembre sin universo no ofrece CSV/contexto;
vacío válido conserva encabezado y universo. Destinos nuevos fuera de la fuente.

Verificador de solo lectura sin importar código de la carpeta revisada: inventario,
huellas, fuente completa por ID/corte y todos los campos de filtros/resultados/
CSV/contexto contra referencia externa. Rechaza referencia interna; no autentica
origen ni historial. Contrato de cierre requiere septiembre/octubre presentes y
noviembre ausente. Prueba de archivos no sustituye comportamiento ni demostración.

Comprobación: doce métodos de autoría aprobados en ambos entornos existentes;
reconstrucción desde carpeta distinta sin acceder a fuentes del repositorio,
dos entornos .venv nuevos restaurados con uv --locked --offline desde caché local
y 19 métodos de referencia de 12.08 aprobados en cada copia. Python 3.12.12,
Streamlit 1.66.1/Altair 6.3.0; metadatos idénticos a raíz y programas previos intactos.
Seis casos conciliados y verificación sin cambios de bytes. Fuente invertida,
variante 2800/4800, fuentes inválidas/vacías, duplicados fuera del filtro, archivos
extra/faltantes, CLI exclusiva y destinos ocupados comprobados. Alteraciones
compensadas de fuente/análisis/CSV rechazadas aun con huellas/contexto actualizados;
solución literal del lab comprobada en dos fases: huella y luego valores.

Chrome headless sobre la app reconstruida a 1440/390: nueve pares descargados
realmente, columnas por clave/contexto/huellas conciliados y revisor estándar
ejecutado sobre esos archivos. Borrador/Enter, tabla oculta, servicios/1900–1901,
rechazo, vacío, corte ausente, cambio/fallo/recuperación de fuente, recarga y
teclado hasta envío/descargas comprobados. Doce vistas GFM de lección/lab/índice/
recorridos/README entregable/guía a 1280/390, sin desbordamiento, IDs únicos y
soluciones cerradas; capturas revisadas. Enlaces locales/fragmentos y diff --check
sin incidencias. No certifica accesibilidad completa ni otros navegadores.

Las nueve secciones de 12 tienen material; retomar práctica/demostración de cierre.
13 es alternativa y 14 conserva su plan. Proyecto/checkpoints y aprendizaje del
estudiante siguen pendientes. Portal y reorganización privada no se integran ni
publican por este trabajo; no hay despliegue ni cambios de dependencias globales.

**Desarrollo — 2026-10-28, pruebas de la aplicación Streamlit 12.08:**
lección/lab, mínimo autónomo de dos ventas, preparador a destino nuevo y
recorridos PowerShell/Bash-Zsh/CMD. Reutiliza app/modelo/caché/entradas/gráfico/
salidas de 12.07 sin cambiar algoritmos ni exigir entregas previas. Expectativas
explícitas por clave, frontera, vacío/cero/corte ausente, errores tratados,
relectura, recuperación y sesión nueva. CSV temporal por caso, patch de ruta
restaurado y limpieza de caché incluso al fallar; ejecución secuencial.

Comprobación: 19 métodos originales (1 mínimo, 7 modelo, 11 AppTest) aprobados
en ambos entornos locales existentes Python 3.12.12/Streamlit 1.66.1/Altair 6.3.0.
Soluciones del lab extraídas del texto y ejecutadas: servicios/1900–1901,
8 métodos de modelo y 12 AppTest aprobados en ambos entornos. Regresión 4600
frente a 2600 detectada y corregida; intercambio compensado de saldos de
septiembre rechazado por función e interfaz pese a mantener 4500 MXN.
Destinos ocupados rechazados; programas anteriores y pyproject/uv.lock intactos.
El ejecutor restringido impidió temporales/AppTest; comprobado con permisos
adecuados, sin desactivar controles ni cambiar dependencias.

Chrome headless Windows a 1440/390: nueve pares CSV/JSON descargados realmente,
campos por clave/contexto/huellas conciliados y esos archivos releídos con el
revisor de Python estándar. Incluye servicios/1900 y vacío/1901, borrador/Enter
sin envío, tabla oculta, rechazo/recuperación, corte ausente, fuente cambiada/
inválida y recarga. Teclado hasta envío y descargas comprobado en ambos anchos;
barras de septiembre separadas y etiquetas recuperables. Inspección Arrow/proto
en AppTest es ampliación dependiente de versión y no acredita descarga real.
Diez vistas GFM de lección/lab/índice/recorridos/guía a 1280/390 sin desbordamiento,
IDs únicos y soluciones cerradas; revisión visual de capturas de autoría.
Enlaces locales y fragmentos comprobados sin incidencias; git diff --check correcto.

Índices, continuidad, cobertura y reanudación actualizados: 12.01–12.08 disponibles;
retomar 12.09 — Cierre y entrega local. Proyecto/checkpoints y aprendizaje
siguen pendientes. Portal y reorganización privada conservan su alcance y
cambios locales; no se integra Streamlit ni se despliega el sitio por esta sección.

**Revisión documental — 2026-10-27, antes de cerrar:** arquitectura, roadmap y
criterios de almacenamiento/tidyverse distinguen 12.01–12.07 disponibles de
12.08–12.09/13–14 pendientes. Guías de autoría/presentación actualizadas sin
confundir plantilla con revisión teórica; índice de labs reunido en una tabla
continua, con navegación fuera de ella. Módulo 12 describe evidencias existentes,
incluidos CSV/contexto, sin presentar la app como futura. Notas locales de
agentes consolidadas en decisiones vigentes y reanudación 12.08; siguen excluidas.
Sin cambios de programas, dependencias ni integración del portal. Comprobación:
4691 enlaces locales sin incidencias y seis vistas GFM 1280/390, con IDs únicos,
sin desbordamiento; las 114 filas del catálogo se conservan en el mismo orden.
El historial anterior permanece como registro de autoría, no como estado vigente.

**Desarrollo — 2026-10-27, tabla/gráfico/descarga Streamlit 12.07 y cierre de sesión:**
lección/lab, mínimo completo, Altair y exportación CSV/JSON desde el mismo
resultado. IDs nominales, pesos enteros, barras/etiquetas, eje desde cero y
alternativa textual. Altura explícita 320: navegador confirmó barras separadas,
no comprimidas por el contenedor. Tabla opcional no cambia filas descargadas.
CSV UTF-8 sin índice; contexto con filtros/universo/indicadores/versión y SHA-256
del CSV. Nombres con corte/mínimo/segmentos; bytes en memoria, on_click ignore.
Descarga representa la vista calculada, no una relectura al hacer clic.

Vacío válido exporta encabezado y contexto; intento rechazado deshabilita botones
hasta confirmar filtros válidos. Fuente inválida/sin registros y corte ausente
no ofrecen archivos actuales. Revisor de solo lectura para par CSV/JSON: huella,
filas y suma, sin autenticar ni sustituir revisión por clave frente a referencia.
Preparador exclusivo con once archivos reutiliza modelo 03/caché 05/entradas 06
sin cambios y sin exigir salidas previas. No hay paquetes ni lockfiles nuevos.

Comprobación: nueve pruebas de funciones/AppTest en ambos entornos existentes
Python 3.12.12/Streamlit 1.66.1/Altair 6.3.0. Datos Arrow enviados al gráfico
conciliados con tabla; CSV/contexto releídos, casos manuales, vacío, cero, rechazo,
fuente cambiada/inválida, recuperación y preservación comprobados. Navegador
Windows/Chrome 1440/390: siete pares descargados realmente (base, borrador,
septiembre, tabla oculta, vacío, variante y móvil), campos/filas/sumas y huellas
conciliados; revisor estándar comprobó esos mismos archivos. Borrador sin enviar
conserva descarga aplicada, otra pasada actualiza variante 2800/4800, fallo de
fuente retira controles. Gráfico SVG con dos barras visibles separadas y etiquetas.

Documentación de cierre en docs/streamlit-closure.md: material 12.01–12.07,
preparación/reanudación, decisiones de estado/caché/descarga y límites de evidencia.
Retomar 12.08 — Pruebas de la aplicación; después 12.09 — Cierre y entrega local.
Ambas siguen planificadas; controles de autoría no acreditan lección impartida,
práctica del estudiante ni proyecto/checkpoints. Índices y continuidad actualizados.
Diez vistas GFM 1280/390 de lección/lab/índice/recorridos/guía de reanudación,
sin desbordamiento, imagen cargada, IDs únicos y soluciones cerradas; 4685 enlaces
locales sin incidencias.
Portal y documentos privados pendientes conservados fuera del commit educativo;
no se integran estas apps al portal ni se despliega en Internet.

**Desarrollo — 2026-10-27, mensajes y vacíos Streamlit 12.06:** lección/lab,
mínimo de cuatro situaciones y app con mensajes de situación/efecto/acción.
Campo de mínimo textual validado antes de aplicar: enteros 0–1000000, espacios
exteriores permitidos solo en interfaz; vacío, signos, decimales y comas se
rechazan sin truncar ni imputar. El intento inválido conserva últimos filtros
válidos claramente identificados y no cuenta otro envío. Error de intento persiste
hasta confirmar corrección; se recalcula con la fuente actual, no una foto pasada.

Lectura/validación antes de caché, spinner breve sin espera artificial, excepciones
esperadas, diagnóstico desplegable y stop. Controles disponibles para reintentar.
Fuente inválida/ausente no presenta cifras guardadas; encabezado sin filas y corte
noviembre sin registros muestran avisos sin métricas. Selección vacía con universo
válido conserva ceros de selección; un crédito con saldo conocido cero se distingue.
Avisos independientes de ocultar detalle. Preparador exclusivo reutiliza fuentes
03 y capa de caché 05 sin cambios; no exige entregas ni añade dependencias.

Comprobación: nueve pruebas en ambos entornos locales Python 3.12.12/Streamlit
1.66.1: forma/rango, fronteras, intentos rechazados, corrección, sesión independiente,
cero observado, fuente ausente, encabezado/UTF-8/duplicados/saldo faltante y
recuperación aun tras caché. Permisos/OSError comprobados mediante lector inyectado,
sin alterar permisos del sistema. Navegador real 1440/390: rechazo con filtros
identificados, corte ausente, segmentos vacíos, aviso sin tabla, fuente inválida,
encabezado solo y recuperación. Captura propia con alternativa textual. Ocho vistas
GFM sin desbordamiento, imagen cargada, IDs únicos y soluciones cerradas; 4622
enlaces locales sin incidencias.
Originales, pyproject/uv.lock y entornos globales intactos; portal y documentos
privados pendientes se conservan fuera del trabajo educativo. Material disponible
no acredita práctica ni proyecto/checkpoint. Retomar 12.07 — Tablas, gráficos y
descarga; 12.07–12.09 siguen planificadas.

**Desarrollo — 2026-10-27, caché Streamlit 12.05:** lección/lab con mínimo de
cache_data frente a cache_resource y app sobre filtros aplicados de 12.04.
Preparador nuevo reutiliza modelo/CSV/configuración/ejecutor de 12.03 sin cambios.
La fuente completa se lee y valida antes de caché; el análisis se identifica por
registros completos, filtros y versión de reglas. TTL 60 segundos, ocho entradas,
limpieza por función y memoria sin persistencia en disco. UUID observa ejecución,
no corrección ni velocidad. Conserva 003/2600 y universo 4600; variante 2800/4800
sin nuevo envío. Fuente inválida fuera del filtro detiene cifras aun con una
entrada guardada. Mínimo con copias independientes y catálogo simulado de lectura:
misma identidad de recurso, sin conexión/modelo pesado ni mutaciones compartidas.

Comprobación: ocho pruebas en ambos entornos locales existentes Python 3.12.12/
Streamlit 1.66.1, incluyendo aciertos, cambio de corte/segmentos/mínimo/versión,
contenido compensado con iguales indicadores, no mutación, fuente ausente,
rechazo y recuperación. Límite de ocho entradas y TTL breve en proceso nuevo
comprobados. Navegador real 1440/390: formulario, reutilización, limpieza, sesiones
con caché global/filtros independientes, CSV actualizado, rechazo y recuperación.
Mínimo y limpiezas independientes revisados en servidor temporal propio; variante
TTL de cinco segundos comprobada en navegador, sin actualizar antes de otra pasada.
Ocho vistas GFM de lección/lab/índice/recorridos sin desbordamiento, imagen cargada,
IDs únicos y soluciones cerradas; 4576 enlaces locales sin incidencias.
Sin paquetes ni lockfiles nuevos, sin cambios en entornos globales ni fuentes
anteriores. No acredita evitar lectura, rendimiento general ni RAM acotada.
Retomar 12.06 — Mensajes y casos sin datos; 12.06–12.09 siguen planificadas.
Proyecto/checkpoints y práctica del estudiante pendientes; portal y documentación
privada se conservan fuera de este trabajo.

**Desarrollo — 2026-10-27, estado y formularios Streamlit 12.04:** lección/lab,
contador mínimo y app con formulario. Claves explícitas, inicialización solo si
faltan, filtros aplicados separados de los widgets, copia de segmentos y contador
de envíos. Editar prepara un lote; confirmar cambia la selección. Otra pasada
conserva parámetros; otra pestaña/recarga/reinicio vuelve al inicio. Enter no envía
en esta app y el formulario conserva sus campos tras confirmar. No se promete
conservar borradores sin enviar después de otras interacciones.

Preparador crea una carpeta nueva con interfaces de 12.04 y funciones/CSV/
configuración/ejecutor de 12.03, idénticos a sus fuentes; no exige salidas previas,
no duplica algoritmos ni sobrescribe prácticas. Octubre 003/2600 y universo 4600;
septiembre >= 2001, 003/2500 y universo 4500, ambos uno de tres. Variante del CSV
2800/4800 se relee en la siguiente pasada sin contar otro envío: conserva filtros,
no resultados ni una fuente congelada. Sin caché, persistencia de elecciones en
disco, paquetes ni lockfiles nuevos. Recorridos completos PowerShell/Bash-Zsh/CMD.

Comprobación: ocho pruebas AppTest en los dos entornos locales existentes,
Python 3.12.12/Streamlit 1.66.1. Contador, inicialización, envíos, frontera, vacío,
recuperación, copia de segmentos, sesiones independientes, relectura, error de
fuente fuera del filtro y preparación exclusiva. Navegador real 1440/390: borrador
sin aplicar, Enter, envío conjunto, detalle recuperable, dos pestañas, recarga y
vacío. Servidor temporal propio detenido/reiniciado realmente: memoria reiniciada,
variante en disco conservada; lectura del CSV sin nuevo envío comprobada también
en navegador. Captura propia con alternativa textual, ocho vistas GFM de lección,
lab, índice y recorridos, enlaces locales revisados. Originales y entornos globales
intactos; portal y documentación privada pendientes fuera de este trabajo.
No acredita aprendizaje ni proyecto/checkpoint. Retomar 12.05 — Caché de datos y
recursos; 12.05–12.09 siguen planificadas.

**Desarrollo — 2026-10-27, separar datos e interfaz Streamlit 12.03:** lección,
lab, recorridos y CSV autónomo con los seis valores de 12.02. Lectura/validación/
análisis en cartera.py sin Streamlit, configuración con ruta propia y consumidores
app/JSON. Sin lectura ni salida al importar; cálculo con entradas explícitas y
salida sin modificar registros. Contrato completo antes de filtrar, IDs/cortes
únicos, enteros conocidos, selección ordenada y mismo denominador del corte.
Octubre ≥ 2000 conserva 003/2600, universo 3/4600 y 33.33%; variante 2800/4800
mantiene uno de tres. Ningún segmento es ninguno; sin universo el porcentaje es
None/null/N/D. Ruta predeterminada anclada al módulo; --fuente relativa pertenece
a la terminal. Importación de módulos no equivale a caché de datos.

Comprobación: ocho pruebas de modelo/CLI y tres de AppTest en los dos entornos
locales existentes de 12.01, Python 3.12.12/Streamlit 1.66.1. Referencias manuales,
fronteras, vacío, recuperación, copias independientes, variante de saldo, fuente
ausente, duplicado fuera del filtro, no mutación, nuevo proceso y otra carpeta.
Navegador real 1280/390: corte, mínimo, segmentos vacíos, sesiones independientes
y sidebar móvil, sin desbordamiento; captura propia revisada con alternativa
textual. Ocho vistas GFM de lección/lab/índice/recorridos sin desbordamiento,
IDs únicos, imagen cargada y soluciones cerradas; 4484 enlaces locales sin
incidencias. Índices y continuidad actualizados. Sin paquetes ni lockfiles nuevos;
fuentes anteriores, entornos globales y portal conservados. No acredita práctica
del estudiante ni proyecto/checkpoint. Retomar 12.04 — Estado de sesión y
formularios; 12.04–12.09 siguen planificadas.

**Desarrollo — 2026-10-27, entradas y filtros Streamlit 12.02:** lección, app,
recorridos y lab con plantilla. Muestra autónoma de seis observaciones de tres
créditos/dos cortes, segmentos comercio/servicios e importes conocidos: 4500/4600
MXN por fecha. Selectbox, multiselect y mínimo entero en sidebar; fecha → universo,
segmento/mínimo → selección. Tabla y métricas desde la misma selección; proporción
de créditos sobre los tres del corte, no proporción de saldo. Octubre ≥ 2000:
003/2600 y 33.33%; septiembre: 002/2000, 003/2500 y 66.67%. Frontera 2000/2001,
ningún segmento (selecciona ninguno), vacío válido y recuperación explicados.
Los controles muestran opciones/valores iniciales y filtros efectivos; no hay
estado/caché propios, CSV arbitrario, descarga ni funciones importables como tema
implementado. 12.03–12.09 siguen planificadas. Continuidad de 12.01 y catálogos
actualizados; retomar 12.03 — Separar datos e interfaz.

Comprobación: doce combinaciones manuales por ID/segmento/fecha/importe y tres
indicadores; recuperación tras vacío y arranque nuevo. AppTest pasó en los dos
entornos uv existentes de 12.01 con Python 3.12.12/Streamlit 1.66.1. Variante de
lab estricta > 2000 comprobada: septiembre 003/2500, 33.33%, texto corregido.
Navegador real: cambio de corte/mínimo, lista de segmentos vacía, dos sesiones
independientes y sidebar móvil; vistas 1280/390 revisadas con detalle recuperable
y sin desbordamiento de página. Captura local y alternativa textual en la lección.
Revisión documental: 4435 enlaces locales sin incidencias y ocho vistas GFM
(1280/390) de lección/lab/índice/recorridos, imagen cargada, IDs únicos y
soluciones cerradas, sin desbordamiento de página.
Programas y muestras previos, pyproject/uv.lock y entornos sin cambios; no se
instalaron paquetes ni se cambiaron globales. No acredita aprendizaje ni proyecto/
checkpoint implementado. Los cambios simultáneos del portal se conservan aparte;
no se integra esta app a su catálogo ni se despliega.

**Desarrollo — 2026-10-27, primera app Streamlit 12.01:** lección con la plantilla,
recorridos por gestor/shell, mínimo de 300 MXN, app autónoma y lab. Cuatro ventas
sintéticas: importes 300/240/0/120 y total 660; casilla de visibilidad, botón,
marca de ejecución y variable local reinicializada. Variante con precio 50 para
V004: 150 y total 690. Navegador/servidor/script, pasada completa, widget frente
a variable, nuevo arranque y sesiones explicados antes de exigirlos. No añade
filtros de negocio, estado propio, caché, lectura CSV, exportaciones o despliegue.
12.02–12.09 siguen planificadas, sin carpetas vacías ni enlaces ficticios. Índices,
roadmap y continuidad de 11.09 actualizados; guía de lección documenta la prueba
de la plantilla con material nuevo. Retomar 12.02 — Entradas, filtros y presentación.

Entorno: grupo opcional streamlit con 1.66.1; los 87 registros previos del lockfile
permanecen idénticos salvo metadatos del proyecto; once paquetes nuevos (98 registros de paquetes). Dos entornos uv locales Python 3.12.12 comprobados;
el segundo se reconstruyó desde caché con --locked y comprobación de dependencias.
Sin modificar Conda, venv raíz, bibliotecas globales ni entornos previos. La prueba
AppTest del mínimo y de interacciones pasó en ambos entornos; variante 690 y cuatro
importes contrastados desde sesiones nuevas con original intacto. AppTest se ofrece
como apoyo de autoría opcional; se enseñará en 12.08. Navegador real: casilla/botón,
marca, total 660, variable 1 y dos pestañas independientes; vistas a 1280/390 px
sin desbordamiento de página. Captura local y alternativa textual en la lección.
Conda/Bash son recorridos documentados, no instalaciones/plataformas acreditadas.
Revisión documental: 4390 enlaces locales sin incidencias y ocho vistas GFM
(1280/390) de lección, lab, índice y recorridos: sin desbordamiento, IDs únicos,
imagen cargada y soluciones cerradas.
No acredita aprendizaje ni checkpoints. Los cambios simultáneos del portal quedan
fuera de esta implementación; no se amplía su catálogo con Streamlit.

**Desarrollo — 2026-10-27, plantilla en Reportes con Quarto:** adaptadas
11.01–11.09 con ubicación, ficha, preparación, objetivos, apoyos, práctica,
evidencia/criterio, referencias y continuidad. CSV, preparadores, .qmd, análisis,
parámetros, configuración, bibliografía, CSS, verificadores y guías existentes
enlazados sin duplicación. Desarrollo, ejemplos de documentos completos,
recorridos Python/R, reglas y cifras conservados. Un motor y HTML bastan para
el recorrido esencial; 11.01 conserva preparación editorial sin Quarto, 11.02
separa preparar cifras/renderizar texto y 11.03 ejecuta dentro del render.
11.06 conserva los experimentos de caché/freeze; 11.07 mantiene revisión humana
y PDF opcional. 11.07 permite pasar directamente a 11.09, ya disponible;
11.08 muestra ampliación opcional y distribución local sin despliegue. El cierre
conserva reconstrucción desde fuentes y referencia externa. Siete labs solo
corrigieron evidencia personal fuera de PROGRESS. Cobertura central 00–11:
las lecciones disponibles usan la plantilla; 12–14 conservan sus planes.
Labs sin migración visual adicional; proyectos/checkpoints y práctica del
estudiante siguen pendientes. Retomar revisión de contenido y sesión real.

Comprobación: 4338 enlaces locales de Markdown sin incidencias; anclas anteriores,
desarrollo, referencias y 109 bloques conservados, incluidos documentos .qmd con
cercas anidadas. Nueve páginas GFM locales a 1280/390 px (18 vistas), con apoyos/
cierre presentes, IDs únicos, sin desbordamiento de página y desplegables cerrados;
salto esencial 11.07/11.08 → 11.09 comprobado y muestra visual revisada. Programas,
fuentes Quarto, datos, configuración, metadatos y dependencias sin cambios.
No se ejecutaron reportes, programas del curso, motores ni instalaciones por
este ajuste documental. El render revisado es el Markdown de las lecciones,
no una nueva comprobación de los reportes ni del GitHub remoto. El portal sigue
limitado a 00 y sesión 02.01; no hay publicación ni acreditación de aprendizaje.

**Desarrollo — 2026-10-27, plantilla en Polars y DuckDB:** adaptadas 10.01–10.10
con ubicación, ficha, preparación, objetivos, apoyos, práctica, evidencia/criterio,
referencias y continuidad. Tablas previas de entorno/archivos integradas al índice
de apoyo; muestras, SQL, funciones, ejecutores, recorridos, métricas y metadatos
existentes enlazados sin duplicación. Datos/contexto conservados en las páginas,
con ejemplos autónomos y recorridos Python/R. 10.04 permite pasar a 10.06;
10.05 muestra opcionalidad en la apertura y mantiene la observación adicional
de memoria como exploración. 10.07 conserva controles entre clientes, recursos
y límites de versiones. 10.09 mantiene fases, crudas, orden/caché e interpretación
limitada de métricas; 10.10 exige revisión humana de la decisión y enlaza 11.01.
Cuatro labs corrigieron solo evidencia personal fuera de PROGRESS; también se
corrigió esa indicación dentro del cierre 10.10. Sin migración visual de labs.
Cobertura central 00–10; siguiente módulo visual: 11. Proyecto/checkpoints y
práctica del estudiante siguen pendientes.

Comprobación: 4189 enlaces locales de Markdown sin incidencias; anclas anteriores,
referencias, ejemplos y 82 bloques de código/comandos/diagramas conservados.
Diez páginas GFM locales a 1280/390 px (20 vistas), con apoyos/cierre presentes,
IDs únicos, sin desbordamiento de página y desplegables cerrados; salto esencial
10.04/10.05 → 10.06 comprobado y muestra visual revisada. Programas, SQL, muestras,
metadatos y dependencias sin cambios. No se ejecutaron motores, programas del
curso, mediciones ni restauraciones/instalaciones por este ajuste documental.
El render local no acredita el de GitHub remoto ni aprendizaje del estudiante;
el portal sigue limitado a 00 y sesión 02.01.

**Desarrollo — 2026-10-27, plantilla en Arrow y Parquet:** adaptadas 09.01–09.09
con ubicación, ficha, preparación, objetivos, apoyos, práctica, evidencia/criterio,
referencias y continuidad. Inspectores, evaluadores, CSV/Parquet/inventario,
recorridos, módulos Python/R, preparadores y lockfiles existentes enlazados sin
duplicación. Se conservaron desarrollo, contratos, cifras, ejemplos autónomos,
recorridos por lenguaje/IDE, sesiones nuevas y límites de memoria/medición.
09.01 distingue inspección esencial y decodificación opcional; 09.03 mantiene
su alcance Python. Notas antiguas de estado en esas aperturas se actualizaron
hacia 09.04/09.05 disponibles. 09.07 permite pasar directamente al cierre 09.09;
09.08 muestra opcionalidad antes del desarrollo. El cierre conserva las cuatro
combinaciones escritor/lector y la verificación contra fuente externa, sin
exigir particiones ni entregas previas. Labs conservados sin cambios. Cobertura
central 00–09; siguiente módulo visual: 10. Proyecto/checkpoints y práctica del
estudiante siguen pendientes.

Comprobación: 4073 enlaces locales de Markdown sin incidencias; anclas anteriores,
desarrollo, referencias y 75 bloques de código/comandos/diagramas conservados.
Nueve páginas GFM locales a 1280/390 px (18 vistas), con apoyos/cierre presentes,
IDs únicos, sin desbordamiento de página y desplegables cerrados; acceso al cierre
desde 09.07/09.08 comprobado y muestra visual revisada. Programas, muestras,
metadatos, dependencias y labs sin cambios. No se ejecutaron programas del curso,
mediciones ni restauraciones/instalaciones por este ajuste documental. El render
local no acredita el de GitHub remoto ni aprendizaje del estudiante; el portal
sigue limitado a 00 y sesión 02.01.

**Desarrollo — 2026-10-27, plantilla en Visualización con R:** adaptadas
08.01–08.09 con ubicación, ficha, preparación, objetivos, apoyos, práctica,
evidencia/criterio, referencias y continuidad. Scripts, figuras de referencia,
preparador/lockfile de patchwork y base/reglas compartidas de 07.10 enlazados
sin duplicación. Desarrollo, muestras, cifras, pausas y recorridos IDE/sesión
nueva conservados. Exploración sin exportación obligatoria en 08.01–08.07;
08.07 mantiene la ampliación anidada opcional. 08.08 conserva PNG esencial y
SVG/PDF/doble resolución como ampliaciones; separa diagnóstico de práctica.
08.09 conserva reconstrucción independiente y seis conciliaciones R/Python.
Siete labs corrigieron solo el destino de evidencia personal fuera de PROGRESS;
el lab 08.09 y su lección actualizaron la nota antigua de continuidad: las nueve
secciones de 09 ya tienen material. Sin migración visual de labs ni cambios de
actividades/soluciones. Cobertura central 00–08; siguiente módulo visual: 09.
Proyecto/checkpoints y práctica del estudiante siguen pendientes.

Comprobación: 3923 enlaces locales de Markdown sin incidencias; anclas anteriores,
desarrollo, referencias, 83 bloques de código/comandos/diagramas y 20 imágenes
conservados. Nueve páginas GFM locales a 1280/390 px (18 vistas), con imágenes
cargadas, apoyos/cierre presentes, IDs únicos, sin desbordamiento de página y
desplegables cerrados; muestra visual revisada. Programas, muestras, figuras,
metadatos y dependencias sin cambios. No se ejecutaron programas del curso ni
restauraciones/instalaciones por este ajuste documental. El render local no
acredita el de GitHub remoto ni aprendizaje del estudiante; el portal sigue
limitado a 00 y sesión 02.01.

**Desarrollo — 2026-10-27, plantilla en tidyverse:** adaptadas 07.01–07.10
con ubicación, ficha, preparación, objetivos, apoyos, práctica, evidencia/criterio,
referencias y continuidad. Preparadores, funciones, ejecutores, CSV compartidos,
metadatos/lockfiles y verificador existentes enlazados sin duplicación. Se
conservaron el desarrollo conceptual, reglas, muestras, cifras, pausas y límites,
así como los recorridos IDE/sesión nueva del mismo proyecto renv y sus respaldos.
07.01 mantiene la comprobación opcional desde terminal cerrada; 07.08/07.09
separan la comprobación del recorrido antes de la práctica. 07.10 conserva la
relectura, revisión visual del PNG y límites del verificador. Diez labs corrigieron
solo el destino de evidencia personal fuera de PROGRESS, sin migración visual ni
cambios de actividades/soluciones. Cobertura central 00–07; siguiente módulo de
presentación: 08. Proyecto/checkpoints y práctica del estudiante siguen pendientes.

Comprobación: 3816 enlaces locales de Markdown sin incidencias; anclas anteriores,
desarrollo, referencias y 122 bloques de código/comandos/diagramas conservados.
Diez páginas GFM locales a 1280/390 px (20 vistas), con apoyos/cierre presentes,
IDs únicos, sin desbordamiento de página y desplegables cerrados; muestra visual
revisada. Scripts, muestras, metadatos y dependencias sin cambios. No se ejecutaron
programas del curso ni restauraciones/instalaciones por este ajuste documental.
El render local no acredita el de GitHub remoto ni aprendizaje del estudiante;
el portal sigue limitado a 00 y sesión 02.01.

**Desarrollo — 2026-10-27, plantilla en R fundamental:** adaptadas 06.01–06.09
con ubicación, ficha, preparación, objetivos, material de apoyo, práctica,
evidencia/criterio, referencias y continuidad. Scripts, CSV, preparadores,
plantilla/lockfile y comparadores existentes enlazados sin duplicación. Se
conservó el desarrollo conceptual y se añadió orientación desde el IDE en
06.02–06.09: inspección por bloques y comprobación completa tras reiniciar R.
06.01 ya tenía ese recorrido. Consola R y terminal diferenciadas; recorridos
PowerShell/Bash/CMD conservados. Copias preparadas para renv y cierre, con
rutas locales y destinos nuevos para repetir sin sobrescribir entregas.
Ocho labs corrigieron solo el destino de evidencia personal fuera de PROGRESS,
sin migración visual ni cambios de actividades/soluciones. Cobertura central
00–06; siguiente módulo de presentación: 07. Proyectos/checkpoints y práctica
del estudiante siguen pendientes.

Comprobación: 3688 enlaces locales de Markdown sin incidencias; anclas anteriores,
desarrollo y 118 bloques de código/comandos/diagramas conservados. Nueve páginas
GFM locales a 1280/390 px (18 vistas), con apoyos/cierre presentes, IDs únicos,
sin desbordamiento de página y desplegables cerrados; muestra visual revisada.
Scripts, muestras, lockfiles y dependencias sin cambios. No se ejecutaron
programas del curso ni restauraciones/instalaciones por este ajuste documental.
La vista GFM local no acredita el renderizado remoto ni aprendizaje del estudiante;
el portal sigue limitado a 00 y sesión 02.01.

**Desarrollo — 2026-10-27, plantilla en Python aplicado:** adaptadas 05.01–05.11
con ficha, preparación, objetivos, apoyos, práctica, evidencia/criterio,
referencias y navegación. Paquete compartido, ejecutores, notebook, pruebas y
JSON existentes enlazados sin duplicar programas. Ruta esencial 05.01–05.05 →
05.11; 05.06–05.10 muestran opcionalidad en la apertura y acceso directo al cierre,
con continuidad alternativa entre ampliaciones. Se conservaron ejemplos, contratos,
pausas, límites de memoria/medición, simulación local de API y responsabilidades
de archivos y entregas. Once labs corrigieron solo el destino de evidencia
personal fuera de PROGRESS, sin migración visual. Cobertura central 00–05.
**Para retomar después del descanso:** empezar la adaptación visual del módulo 06;
su contenido ya existe. Proyectos/checkpoints y sesión real siguen pendientes.

Comprobación: 3582 enlaces locales de Markdown sin incidencias; anclas anteriores,
desarrollo y 112 bloques de código/comandos/diagramas conservados. Once páginas
GFM locales a 1280/390 px (22 vistas), con apoyos/cierre presentes, desplegables
cerrados, rutas opcionales disponibles e IDs sin duplicación. Paquete, notebook,
scripts, pruebas, muestras, JSON y dependencias sin cambios. No se ejecutaron
programas, mediciones, servicios ni instalaciones por este ajuste documental.
La revisión local no acredita GitHub remoto ni aprendizaje; no se amplió el portal.

**Desarrollo — 2026-10-27, plantilla en Visualización Python:** adaptadas
04.01–04.09 con ubicación, ficha, preparación, objetivos, apoyos,
práctica/evidencia, referencias y continuidad. Conservados contratos, tablas,
figuras, código, pausas y versiones de referencia; los datos y su contexto siguen
en la propia lección. 04.01 conserva cierre con ficha/boceto y regeneración
opcional. 04.08 muestra su opcionalidad antes del desarrollo; 04.07 permite
saltar a 04.09 sin interacción. PNG/SVG de referencia y scripts existentes
enlazados sin duplicar fuentes. Nueve labs corrigieron solo el destino de
evidencia personal fuera de PROGRESS, sin migrar su presentación ni alterar
ejercicios o soluciones. Cobertura central 00–04; próximo módulo visual: 05.

Comprobación: 3446 enlaces locales de Markdown sin incidencias; anclas anteriores,
desarrollo, 65 bloques de código/comandos/diagramas y 27 imágenes conservados.
Nueve páginas GFM locales a 1280/390 px (18 vistas), con apoyos/cierre presentes,
figuras cargadas, desplegables cerrados y saltos opcionales disponibles. Recursos,
programas, CSV, PNG/SVG y dependencias sin cambios. No se ejecutaron scripts ni
instalaciones ni se certificó accesibilidad o interacción por revisar el Markdown.
La revisión local no acredita GitHub remoto ni aprendizaje; no se amplió el portal.

**Desarrollo — 2026-10-27, plantilla en SQL:** adaptadas 03.01–03.09 con
ubicación NN.LL, ficha, preparación, objetivos, recursos, práctica,
evidencia/criterio, referencias y navegación final. Scripts, esquemas, consultas
SQL y CSV compartidos enlazados sin duplicarlos. Conservadas pausas por sesión,
extensiones opcionales, lectura de las fuentes y escrituras sobre copias nuevas.
Corregido el destino de evidencia personal en cinco labs (03.04/06/07/08/09),
sin cambiar ejercicios, soluciones ni su presentación general. Cobertura vigente
actualizada solo en el índice de documentación. Próximo módulo visual: 04;
proyectos/checkpoints y observación de una sesión real siguen pendientes.

Comprobación: 3336 enlaces locales de Markdown sin incidencias; anclas previas,
desarrollo principal y 100 bloques de código/comandos/diagramas conservados.
Nueve páginas GFM locales a 1280/390 px (18 vistas), con apoyos/cierre presentes,
desplegables cerrados e imágenes disponibles. Scripts, SQL guardado, CSV y figura
sin cambios; ejercicios y soluciones de labs intactos. No se ejecutaron consultas,
escrituras ni instalaciones por este ajuste de presentación. No acredita revisión
del GitHub remoto ni aprendizaje; SQL no se integró como lecciones del portal.

**Desarrollo — 2026-10-27, depuración documental:** revisadas referencias Markdown,
rutas en preparadores y catálogos. Retirados los esqueletos sin contenido activo
docs/decisions/README.md, datasets/data_dictionary/README.md y
datasets/generators/README.md; sus reglas útiles quedaron en arquitectura y
política de datos. Conservados README de entregas y plantillas consumidos por
código. Arquitectura y cierres condensados, sin repetir inventarios por sección;
criterios y anclas vigentes conservados. Índice de documentación como acceso y
fuente de cobertura de plantillas; resumen actual de esta bitácora simplificado,
historial anterior conservado. Corregida separación entre evidencia personal y
estado editorial y referencias antiguas al piloto/Quarto. Recursos educativos,
programas y especificaciones privadas conservados. Próximo módulo visual: 03.

Comprobación: 288 Markdown presentes y 3224 enlaces locales sin incidencias;
anclas anteriores de arquitectura, cierres y guía de lección conservadas.
Siete pruebas existentes del portal correctas. Seis documentos principales
renderizados y comprobados a 1280/390 px (12 vistas locales). Sin cambios en
curriculum, labs, código, notebooks, dependencias o muestras. El historial
editorial anterior y la reorganización privada pendiente permanecen conservados.

**Desarrollo — 2026-10-27, plantilla en pandas:** adaptadas 02.01–02.10 con
ficha, preparación, objetivos, recursos, práctica, evidencia/criterio, referencias
y continuidad. Diez scripts, CSV propios/compartidos y notebooks existentes
enlazados sin duplicarlos: notebook opcional de lab 02.01 y cierre 02.10.
Diagnósticos separados de la práctica en 02.04/06/07/09; ejemplos, comandos,
datos y reglas conservados. Corregido el estado antiguo de SQL en el cierre;
sus nueve lecciones/labs están disponibles. Labs sin migración visual; guías
actualizadas con cobertura 00/01/02. Resto de módulos y sesión real pendientes.

Comprobación: 3254 enlaces locales de Markdown y 1477 enlaces en las 27 páginas
del portal sin incidencias. Diez lecciones GFM local y sesión 02.01 del portal
a 1280/390 px (22 vistas); apoyos/cierre presentes y desplegables cerrados.
Anclas anteriores, desarrollo principal y 110 bloques de código/comandos/diagramas
contrastados con las fuentes previas. Scripts, CSV, notebooks, figura y labs
sin cambios; no se ejecutaron ejemplos ni instalaciones. No acredita revisión
del GitHub remoto ni aprendizaje completado; 02.02–02.10 no se integraron al portal.

**Desarrollo — 2026-10-27, plantilla en Entorno de aprendizaje:** completada la
adaptación de 00.02–00.06, conservando 00.01 ya adaptada. Cabecera, preparación,
objetivos, apoyos, práctica, evidencia/criterio, referencias y continuidad; 00.05
mantiene entrada, lecturas A/B y recorridos Conda/venv/uv con orientación y cierre.
Solo un camino obligatorio. Recursos existentes enlazados y bitácora personal;
comandos y ejemplos conservados, sin instalaciones ni cambios de scripts/datos.
Corregida continuidad de 00.06 hacia las seis lecciones disponibles de Python.
Labs conservados y guías actualizadas con cobertura 00/01. Otros módulos y
la sesión real de estudio siguen pendientes.

Comprobación: 3139 enlaces locales de Markdown y 1459 enlaces de las 27 páginas
HTML del portal sin incidencias. Once páginas de lección/apoyo comprobadas en
GFM local y portal a 1280/390 px (44 vistas), con apoyos y cierre presentes y
desplegables cerrados. Anclas previas y 79 bloques de código/comandos contrastados
con las fuentes anteriores. Scripts, notebook, datos y labs sin cambios; no se
ejecutaron instalaciones ni ejemplos. La revisión local no acredita inspección
del GitHub remoto ni una sesión de aprendizaje.

**Desarrollo — 2026-10-27, plantilla en Python fundamental:** las seis lecciones
01.01–01.06 aplican cabecera NN.LL, preparación, objetivos, apoyo, práctica,
evidencia/criterio, referencias y continuidad. Recursos existentes enlazados en
tabla y contexto: seis scripts y dos CSV; sin copias ni dependencias nuevas.
Ejemplos y comandos conservados; preparación y cierre específicos de cada tema,
con evidencia personal y revisión en pareja. Corregida la continuidad antigua de
01.06: pandas ya tiene diez lecciones/labs. Labs conservados, con enlaces de
ida/vuelta y siguiente lección revisados. Guías actualizadas con cobertura real;
otros módulos y una sesión real de estudio siguen pendientes.

Comprobación: 2967 enlaces locales de Markdown sin incidencias; anclas previas,
desarrollo didáctico y bloques de código/comandos contrastados con las fuentes
anteriores (solo se añadió un enlace conceptual a 00.06 en el desarrollo de
01.01). Render GFM local de las seis páginas a 1280/390 px, apoyos enlazados y
desplegables cerrados. Scripts, datos y labs sin cambios; no se volvieron a
ejecutar ejemplos ni se amplió su integración en el portal. La revisión local
no acredita inspección del GitHub remoto ni aprendizaje completado.

**Desarrollo — 2026-10-27, apoyo y primera lección de prueba:** criterio de
recursos documentado en guía y plantilla de lección: índice después de objetivos
con finalidad/uso y enlaces en el lugar donde se utilizan. Primera aplicación
en [00.01](curriculum/00_getting_started/01_github_profile/README.md), con plantilla
de perfil, guía y bitácora existentes; sin añadir notebooks ni código innecesarios.
Cabecera 00.01, preparación, objetivos observables, práctica, evidencia/criterio
y continuidad ajustados; anclas anteriores conservadas. El resto de lecciones
no se migró. Pendiente observar uso real con pareja; 00.02 sigue como siguiente
caso propuesto para revisar varios recorridos.

Comprobación de esta prueba: enlaces del Markdown sin incidencias, portal local
generado sin ejecutar ejemplos y 1236 enlaces locales en 27 páginas HTML
verificados. Lectura en Chrome aislado a 1280/390 px para GFM local y portal;
anclas de continuidad conservadas y pista cerrada. No acredita revisión visual
del GitHub remoto ni una sesión de aprendizaje.

**Desarrollo — 2026-10-27, propuesta de estructura de lección:** revisión
estructural de nueve páginas (cuatro iniciales y una de Python, pandas, SQL, R
y Quarto), con consulta de las dos partes de 00.05. Evaluación, elementos
comunes y variantes en [la guía de lección](docs/lesson-page-guide.md), con
[plantilla reutilizable](templates/lesson/README.md). Apertura y cierre estables;
desarrollo adaptable al tema. Se identificaron continuidades antiguas y ajustes
de evidencia personal/recorrido R, sin migrar ni ejecutar las lecciones.
Siguiente prueba propuesta: adaptar 00.02 y revisarla antes de extender el patrón.


**Desarrollo — 2026-10-27, alcance común de módulos:** desplegable «Ver el alcance
de las secciones» unificado en los índices 00–14, cerrado por defecto después
de la tabla. Se añadió alcance propio a 00/01 y se plegó el previsto de 12–14,
con estado de planificación visible y anclas anteriores conservadas. La tabla,
preparación, evidencia y cierre siguen accesibles fuera del desplegable.
Regla documentada en guía de módulo, presentación Markdown y plantilla.
Quince desplegables a dos anchos, apertura/cierre y revelado del plan por
fragmentos comprobados en GFM local; anclas y enlaces del corpus conservados.


**Desarrollo — 2026-10-27, estructura aplicada a todos los módulos:** los índices
00–14 comparten cabecera y ocho secciones, con objetivos, tabla lección/lab,
evidencia, criterio y continuidad propios de cada módulo. Se conservaron anclas,
alcances y referencias; 12–14 siguen como planes y sus labs no se crearon.
Opciones de Python aplicado, exportación/particiones/streaming y Quarto visibles;
Streamlit/Shiny siguen como alternativas. Estados antiguos de 01 y 10 corregidos.
La adaptación es de índices, no de toda la teoría o las pantallas del portal.
Quince índices con ocho secciones y anclas conservadas; enlaces del corpus
comprobados. Treinta vistas GFM locales a 1280/390 px, cierre, apoyos y planes
navegables revisados, sin ejecutar lecciones o modificar entornos.


**Desarrollo — 2026-10-27, estructura de página de módulo:** acuerdo educativo
con cabecera y ocho secciones, documentado en
[guía de módulo](docs/module-page-guide.md), plantilla y autoría. Referencia
aplicada al índice 00 con preparación, objetivos, ruta, evidencia, criterio y
continuidad. No se han uniformado otros módulos ni la composición del portal.
Hallazgo para revisar al adaptar 01: su índice aún describe Python aplicado
como planificado, pese al material disponible de 05.


**Desarrollo — 2026-10-27, índice visual del curriculum:** entrada breve con
ruta inicial y módulos 00–14 agrupados en tres etapas. Enlaces a cada índice,
separación de material disponible/planes, alternativa Streamlit/Shiny y guía
para avanzar. El inventario editorial deja de ocupar la introducción; se conserva
en sus fuentes de referencia. Patrón añadido a la guía Markdown y reglas locales.


**Desarrollo — 2026-10-27, muestra de estudio visual en Markdown:** portada
con accesos y mapa temprano, índice 00 con lección/lab/resultado y muestra
00.01 con ubicación, ficha inicial, pistas y tabla de comprobación. Evidencia
personal distinguida del estado editorial. Patrón documentado en
[guía de presentación](docs/markdown-study-guide.md) y enlazado desde autoría;
resto del track pendiente de adaptación gradual. La navegación a portada/índice
se declara en el catálogo del portal, conservando las fuentes compartidas.
Se revisó la muestra GFM local a dos anchos, con pistas y navegación entre
portada/lección/lab. No equivale a inspección visual del GitHub remoto.

**Desarrollo — 2026-10-26, estructura del portal:** portada general, contenido
00–14 y página del primer módulo 00, conservando la prueba adicional 02.01.
Catálogo del curso, seis lecciones/labs originales y seis páginas de apoyo de
00; 00.05 conserva A/B y Conda/venv/uv. Registro Markdown personal para 00,
sin mezclarlo con el borrador de pandas ni exportar PROGRESS.md completo.
Los índices restantes se ofrecen como descarga: 01–11 con material en el repo,
12–14 planificados; no se presentan como módulos integrados en el portal.
La [propuesta de publicación](docs/portal-publication.md) registra alternativas,
audiencia pendiente, revisión de archivos y publicación explícita de versiones.
No se contrató alojamiento ni se desplegó servicio. Render de lectura sin ejecutar
programas o instalar entornos; fuentes educativas y lockfiles conservados.
El arranque comprueba fuentes y conserva las copias anteriores al actualizar.
Veintisiete páginas y 1616 enlaces/recursos locales comprobados; siete pruebas
estándar y 81 vistas a 1440/768/390 px, junto con pregunta/descarga/borrador de
02.01. Las referencias numeradas y enlaces a directorios se adaptan a Quarto.
Revisión del contenido y observación de una pareja siguen pendientes.

**Desarrollo — 2026-10-26, primer piloto local 02.01:** disponible
[portal/README.md](portal/README.md), catálogo explícito, seis páginas Quarto,
adaptador de enlaces y descargas. Reutiliza lección/lab sin duplicar su fuente
editorial; las consultas fuera del piloto conservan ubicación y fuente descargable.
Notebook junto al lab, script auxiliar, instrucciones y bitácora en paquete ZIP;
preparación rechaza destinos ocupados. Render de lectura sin ejecución ni paquetes
nuevos; Python 3.12.12/Quarto 1.9.38 existentes. Notebook limpio ejecutado desde
kernel nuevo, muestra 3 × 3/ocho unidades, variante 4 × 3/once y vacío 0 × 3.
Cuatro pruebas estándar del adaptador/copias; originales y lockfiles conservados.
Seis páginas a 1440/768/390 px, navegación, soluciones cerradas, pregunta con
feedback, ZIP y bitácora guardada/recuperada/exportada comprobados en navegador
aislado sin solicitudes externas. El registro guarda un solo borrador por sesión
y navegador, sin sincronización. Código del portal versionado; sitio generado,
prácticas y registros personales excluidos. No se desplegó servicio en Internet.
El material está comprobado técnicamente; la sesión real en pareja y la mejora
de experiencia a partir de ella siguen pendientes antes de extender a 02.02/02.03.

**Desarrollo — 2026-10-26, 11.09:** disponibles la
[lección](curriculum/11_reporting_quarto/09_reproducible_report_closure/README.md) y el
[lab](labs/11_reporting_quarto/09_reproducible_report_closure/README.md). CSV propio
de siete filas, parámetros JSON estrictos, documentos/preparadores/construcción
Python/R y copia de solo fuentes. Entrega HTML, detalle/resumen/barras/PNG,
versiones, comando, diagnóstico y huellas; verificador Python estándar de solo
lectura con referencia externa y parámetros esperados. Septiembre 3/6000 y
selección 2/5000 MXN; octubre 4/7000 y 1/3300. Sin dependencias ni lockfiles nuevos.
Seis escenarios por motor, reconstrucciones desde fuentes, 24 entradas/parámetros
inválidos y doce alteraciones con huellas actualizadas comprobados. Verificación
sin mutaciones, entornos Python reconstruidos y dos bibliotecas R locales;
HTML offline a 1280/640/390 px, navegación y teclado revisados.
El entorno R se restauró localmente: los binarios conservados de arrow/duckdb
permitieron evitar compilación desde fuentes, manteniendo versiones bloqueadas.
Las nueve secciones de Quarto tienen material; práctica personal, proyecto
integrador y checkpoints siguen pendientes. Próximo trabajo: piloto de experiencia
con alcance pequeño sobre el contenido existente; 12–14 conservan sus planes.


**Desarrollo — 2026-10-26, 11.08:** disponibles la
[lección](curriculum/11_reporting_quarto/08_dashboard_distribution/README.md) y el
[lab](labs/11_reporting_quarto/08_dashboard_distribution/README.md) opcionales,
CSV propio de seis filas, mínimo, dashboards/preparadores Python/R, CSS,
verificador estándar de solo lectura y distribuidores por lenguaje. Reutiliza
funciones de 11.03 sin entregas previas. Tres tarjetas, tabla de tres créditos
y figura conservan 6000/6300 MXN, diferencia 300 y 5.00%; misma población.

**Comprobación:** ocho escenarios por motor (base, cambio a 6600/10%,
compensación, base cero, todos cero, baja, máximos y fuente invertida), tarjetas,
tasa y detalle por valor; alturas/etiquetas de barras contrastadas con CSV.
Duplicados, fuentes incompletas y negativos rechazados; alternativas ausentes,
enlaces rotos, tarjetas falsas, recursos no incorporados y HTML antiguo con
datos compensados rechazados por el verificador. Comprobación sin modificar
entradas/HTML. Mínimo estático renderizado; preparadores/distribuidores protegen
destinos ocupados. Segundo entorno Python y segunda biblioteca R existentes
con render real; metadatos R, pyproject y uv.lock conservados.

**Entrega y revisión:** HTML y LEEME en carpetas nuevas; copia idéntica por
bytes/MD5, sin atribuir autenticidad ni validación de datos a esa igualdad.
Copias finales abiertas offline en Chrome headless aislado a 1280/640/390:
figura cargada, tarjetas coherentes al cambiar vistas, pestañas con flechas,
Tab hasta región nombrada y desplazamiento real hasta última columna con foco
visible; sin solicitudes HTTP. Capturas de ambos motores inspeccionadas.
Se corrigieron duplicación de tabla, títulos de tarjeta R, filas excesivamente
altas y salidas auxiliares de Matplotlib. Python usa celdas calculadas porque
refresco de Jupyter Cache no admite las expresiones en línea de esta variante.
No certifica accesibilidad completa, zoom manual, IDE u otros sistemas.

Quarto 1.9.38, Python 3.12.12/Matplotlib 3.10.7 y R 4.6.1/knitr 1.52/ggplot2
4.0.3, sin nuevas dependencias. Distribuir la lectura no incluye todos los
fuentes de reconstrucción ni implementa alojamiento, portal o app con servidor.
Práctica del estudiante y proyectos/checkpoints pendientes. Retomar 11.09.

**Cierre documental 11.08:** 2888 enlaces locales en 278 Markdown, fragmentos
y bloques comprobados; `git diff --check` sin errores de espacios. Fuentes,
entornos y entregas previas conservados. La publicación se consulta en Git.


**Desarrollo — 2026-10-26, 11.07:** disponibles la
[lección](curriculum/11_reporting_quarto/07_formats_visual_review/README.md) y el
[lab](labs/11_reporting_quarto/07_formats_visual_review/README.md), muestra propia
de seis filas, mínimo estático, reportes/preparadores Python/R, CSS y verificador
de solo lectura. Reutiliza funciones de 11.03, sin entregas personales previas.
Conserva tres créditos y 6000/6300 MXN, +300/5.00%; resumen, detalle y figura
desde el mismo resultado. Sin nuevas dependencias ni cambios de lockfiles.

**Comprobación:** ocho escenarios por motor (base, cambio a 6600/10%,
compensación, base cero, todos cero, baja, máximos y fuente invertida), texto y
celdas por valor; alturas/etiquetas de barras contrastadas con referencia CSV.
Duplicados, fuentes incompletas y negativos rechazados; HTML sin alternativa
textual, enlaces rotos y saldos desactualizados/compensados rechazados por el
verificador, sin modificar entradas o HTML al comprobar. Segundo entorno Python
y segunda biblioteca R existentes con render real; destinos ocupados protegidos
y metadatos R intactos. Mínimo HTML y cambio estático 3500 → 4000 comprobados.

**Revisión visual:** Chrome headless aislado en Windows, sin conexión, a
1280/640/390 píxeles: capturas de ambos motores inspeccionadas, imagen cargada,
cuerpo sin desbordamiento horizontal, índice y referencias funcionales.
Tab alcanza el recuadro, contorno visible y flechas hasta la última columna y
vuelta al ID. Se corrigió el overflow de la celda interior de Quarto y el índice
oculto por el tema a ancho estrecho. No certifica zoom manual, lector de pantalla,
otros navegadores/sistemas, IDE ni accesibilidad completa. Quarto 1.9.38,
Python 3.12.12/Matplotlib 3.10.7, R 4.6.1/knitr 1.52/ggplot2 4.0.3.

**PDF opcional:** intento con LuaLaTeX/MiKTeX existente e instalación automática
deshabilitada. Falló el acceso del ejecutor a su configuración de usuario;
no se generó un PDF comprobado ni se instalaron paquetes. No bloquea el cierre
HTML. Las copias, capturas y salidas de revisión quedan fuera de Git; práctica
del estudiante, portal y proyectos/checkpoints siguen pendientes. Retomar 11.08.

**Cierre documental 11.07:** 2863 enlaces locales en 275 Markdown, fragmentos
y bloques comprobados; `git diff --check` sin errores de espacios. Fuentes y
lockfiles anteriores conservados. Implementación completa; la publicación se
consulta en el historial Git.


**Avance parcial — 2026-10-26, 11.07:** se conservan los
[fuentes del borrador](curriculum/11_reporting_quarto/07_formats_visual_review/BORRADOR.md):
CSV propio, CSS, mínimo estático, preparadores y reportes Python/R. Ambos
reportes renderizaron a HTML con los entornos locales existentes, sin nuevas
dependencias. Falta redactar la lección y el lab, completar el contraste de
datos y las comprobaciones visuales, y actualizar la navegación al cerrarlos.
La revisión en navegador se interrumpió por una limitación de la herramienta
para verificar la URL de Chrome; no se acredita revisión visual del HTML.
PDF opcional todavía no comprobado. Este avance no cuenta como sección
terminada ni como evidencia de aprendizaje. Retomar aquí antes de 11.08.

**Desarrollo — 2026-10-26, 11.06:** disponibles la
[lección](curriculum/11_reporting_quarto/06_projects_cache_freeze/README.md) y el
[lab](labs/11_reporting_quarto/06_projects_cache_freeze/README.md), CSV propio de
siete filas, configuración de proyecto, reportes/preparadores Python/R y
verificador de solo lectura. Funciones de 11.05 reutilizadas sin entregas previas.
Rutas desde proyecto, render global frente a individual, freeze auto/true y
caché por motor. Septiembre 6000/5000 MXN; cambio de 003 a 3600 produce 6600/5600;
octubre conserva 7000/3300. Identificadores/bitácora permiten observar recálculo,
sin autenticar sesiones históricas. Un refresco global no evita freeze; documento
explícito más refresco y contraste por fila recuperan resultados actuales.

**Verificación principal:** veinte renders por motor en Quarto 1.9.38,
Python 3.12.12/jupyter-cache 1.0.1 y R 4.6.1/knitr 1.52. Datos, código del
documento, funciones externas y parámetros; reutilización y recuperación reales.
Volver a una versión conocida del código puede recuperar una entrada Jupyter
anterior con dependencias externas antiguas: por eso se separan los experimentos
y se exige refresco explícito. Jupyter-cache declarado en notebooks; 81 registros
uv previos completos conservados y cinco añadidos. Segundo entorno local
reconstruido desde caché. R sin paquetes ni metadatos nuevos; ejecutor restringido
no resuelve enlaces base de renv, comprobación realizada con permisos de lectura
adecuados, sin desactivar validaciones. No modifica entornos globales ni
implementa el portal o proyectos/checkpoints. Retomar con 11.07.

**Cierre de revisión 11.06:** diez escenarios adicionales por motor: base,
frontera inclusiva, selección vacía, ceros, máximos, fuente invertida, duplicado
y saldo inválido fuera del corte, corte ausente y recuperación. Dos cambios
compensados rechazados por el verificador, uno con total/selección iguales y
detalle distinto; archivos conservados al verificar. Mínimos 3500 → 4000
ejecutados en ambos motores. Tabla R con enteros formateados explícitamente
para no presentar 1000000 como notación científica. Preparadores protegen destinos
ocupados; metadatos R conservados. Revisados 2833 enlaces locales en 272 Markdown,
fragmentos y bloques, y diff sin errores de espacios. No se acredita revisión
visual completa del HTML, IDE ni otros sistemas. La publicación se consulta
en el historial Git.


**Cierre de sesión — 2026-10-24:** material hasta 11.05 publicado en `main`
mediante `2c25d22`; árbol de trabajo limpio al cerrar. No se inició 11.06.
Retomar con **11.06 — Proyectos, caché y freeze**, revisando esta bitácora y
[los pendientes de cierre](docs/storage-closure.md). Mantener ejemplos autónomos,
recorridos Python/R separados y comprobación del recálculo ante cambios de datos,
código o parámetros. Práctica del estudiante y proyecto/checkpoints pendientes.

**Desarrollo — 2026-10-23, 11.05:** disponibles la
[lección](curriculum/11_reporting_quarto/05_parameters_cutoffs/README.md),
mínimos completos Python/R, CSV propio de siete filas, funciones, documentos,
dos YAML, preparadores y [lab](labs/11_reporting_quarto/05_parameters_cutoffs/README.md).
Parámetro, filtro y nombre de salida distinguidos; Jupyter sustituye valores
después de la celda parameters y los cálculos derivados van después; knitr usa
params. Fuente completa validada antes del filtro. Septiembre: universo 3/6000
MXN, selección 2/5000/66.67%; octubre: 4/7000 y 1/3300/25%, mínimo 2000.
Umbral inclusivo, denominador por corte, observación adicional en octubre y
selección vacía frente a corte ausente; las barras de universo/selección se
solapan y no se suman. Recorridos independientes sin entregas personales previas.

**Verificación:** Quarto 1.9.38/Pandoc 3.8.3, Python 3.12.12 y R 4.6.1/knitr 1.52.
Papermill 2.7.0 declarado en notebooks y uv.lock real: 64 registros previos
completos conservados y 17 añadidos; dos entornos uv locales reconstruidos.
R conserva DESCRIPTION/renv.lock y biblioteca previa; sin cambios globales.
31 casos de parámetros conciliados Python/R; seis fuentes inválidas (incluidos
duplicado y saldo inválido fuera del corte), no finitos y destinos ocupados
rechazados. Saldos cero y máximos con mínimo cero conservan los cuatro créditos
de octubre en ambos motores. Ambos renderizan septiembre, octubre, octubre vacío y
frontera septiembre/2001; cada celda, parámetro visible, cifra y altura/etiqueta
real de barras conciliados con referencia independiente. PNG incorporados de
Python/septiembre y R/octubre revisados visualmente. CLI -P, corte/tipo inválidos
y clave no declarada comprobados: Jupyter puede ignorar una variable extra y
usar el valor predeterminado; knitr rechaza la clave. Mínimos ejecutados en ambos
motores. Un entorno anterior sin Papermill renderiza defaults pero falla al
sustituir; se documenta el requisito real. En Quarto 1.9.38 se observó fallo de
recursos con salida desde otra carpeta: los recorridos entran en la del documento.
Fuentes y metadatos R intactos. No se acredita revisión visual completa del HTML,
IDE, otros sistemas ni accesibilidad completa. Proyecto/checkpoints y práctica
del estudiante pendientes. Revisados 2812 enlaces locales en 270 Markdown,
fragmentos, bloques y soluciones; sin incidencias. Retomar con 11.06.

**Desarrollo — 2026-10-23, 11.04:** disponibles la
[lección](curriculum/11_reporting_quarto/04_tables_figures_references/README.md),
mínimo completo de referencia estática, CSV propio, reportes Python/R con
cifras en línea, tabla por crédito y barras del agregado, bibliografía local,
preparadores y [lab](labs/11_reporting_quarto/04_tables_figures_references/README.md).
Funciones de 11.03 reutilizadas sin exigir entregas previas. Identificador,
caption, texto alternativo, referencia interna, procedencia y cita bibliográfica
distinguidos con ejemplos. El texto, la tabla y las barras se alimentan del mismo
resultado: 6000/6300 MXN, diferencia 300 y 5% sobre septiembre.

**Verificación:** Quarto 1.9.38/Pandoc 3.8.3, Python 3.12.12/Matplotlib 3.10.7 y
R 4.6.1/knitr 1.52/ggplot2 4.0.3 existentes. Sin nuevas dependencias, instalaciones
ni cambios en pyproject/uv.lock, DESCRIPTION/renv.lock o bibliotecas globales.
Seis escenarios renderizados en ambos motores: base, cambio 6600/+600/10%,
modificación compensada con total idéntico, base cero, todos cero y baja.
HTML inspeccionado: cifras del párrafo, cada celda por clave, vínculos/captions,
cita resuelta, imagen incorporada y texto alternativo. Alturas y etiquetas
reales de las barras (artistas Matplotlib/capas ggplot2) conciliadas contra
entrada independiente; ambas figuras base revisadas visualmente desde el PNG
incorporado al HTML. Duplicados detienen ejecución en ambos motores.
Tabla adicional renumera la referencia correcta; referencia y cita inexistentes
generan advertencia aun con salida exitosa del comando. Mínimo, bibliografía,
recuperación y metadatos intactos comprobados. No se acredita revisión visual
completa del HTML, interfaz del IDE, Linux/macOS ni accesibilidad completa.
Proyecto/checkpoints y práctica del estudiante pendientes. Retomar con 11.05.

**Desarrollo — 2026-10-23, 11.03:** disponibles la
[lección](curriculum/11_reporting_quarto/03_execution_python_r/README.md),
CSV propio, funciones Python/R, documentos ejecutables, preparadores y
[lab](labs/11_reporting_quarto/03_execution_python_r/README.md). Teoría común,
recorridos separados, mínimo con tres saldos y comparación completa de seis
filas. Render lee CSV/funciones desde cero: 6000/6300 MXN, +300 y 5% sobre
septiembre; cambio a 6600/+600/10% sin regenerar texto con el preparador.
Se comprueba el intérprete dentro del kernel y proyecto/biblioteca R activos.
Sin caché ni daemon Python; `error: false` detiene errores de ejecución.

Grupo notebooks: nbclient 0.10.2, nbformat 5.10.4 y PyYAML 6.0.3 añadidos,
ipykernel 6.30.1 conservado. Los 58 registros Python previos (sin el registro
del proyecto) permanecen idénticos. Dos entornos uv nuevos Python 3.12.12
sin modificar la venv raíz ni Conda. R 4.6.1/renv 1.3.1: knitr 1.52 y
rmarkdown 2.32; lockfile real conserva 50 registros y añade 21, sin cambios
de versiones previas. Una copia del proyecto anterior y una restauración
completa desde biblioteca vacía, con estado sincronizado. Preparador extiende
metadatos con respaldo_10_07 o crea entorno autónomo reutilizando configuración
local; no necesita entregas personales ni inicializa renv en la raíz.

**Verificación:** 18 casos Python/R con pares, sumas y tasas conciliados:
base/cambio/orden inverso/baja/sin cambio/base cero/todos cero/máximo y rechazo
de vacío/incompleto/duplicado/ID/fecha/ausencia/negativo/decimal/exceso/espacio.
Quarto 1.9.38/Pandoc 3.8.3 existentes: renders reales de ambos lenguajes desde
entornos reconstruidos para base, cambio y base cero; fallos por duplicado,
entrada ausente y función ausente, y recuperación a base. Mínimos ejecutados
y dependencia Python ausente comprobada con fallo explícito. Recursos incluidos
en reportes completos, salida de celdas/cifras inspeccionadas por parser;
los mínimos mantienen su carpeta de recursos. Preparadores protegen destinos
y metadatos, respaldos coinciden y archivos anteriores se conservan.
Jupyter requirió comunicación local entre procesos y renv lectura de enlaces
base fuera del ejecutor restringido; no se desactivaron controles. No se probó
la interfaz del IDE, Linux/macOS ni revisión visual/accesibilidad completa.
No cambian bibliotecas globales, fuentes o entregas anteriores. Proyecto,
checkpoints y práctica del estudiante pendientes. Retomar con 11.04.

**Desarrollo — 2026-10-23, 11.02:** disponibles la
[lección](curriculum/11_reporting_quarto/02_first_document/README.md),
primer `hola.qmd`, encabezado reutilizable, CSV propio, preparadores Python/R y
[lab](labs/11_reporting_quarto/02_first_document/README.md). YAML, Markdown,
archivo fuente/extensión, CLI frente a extensión, código mostrado frente a
ejecutable, render/preview y recursos HTML. Se reutilizan las reglas/narrativa
de 11.01 sin exigir sus entregas. Dos fases explícitas: Python/R calcula y
escribe `reporte.qmd`; Quarto renderiza texto ya guardado, sin ejecutar Jupyter
o knitr. Tres créditos, 6000/6300 MXN, diferencia 300 y 5% sobre septiembre.

**Verificación:** Quarto 1.9.38 y Pandoc 3.8.3 incluidos en RStudio, sin instalar
ni actualizar herramientas. Python 3.12.12/R 4.6.1 con UTF-8 de autoría; ambas
preparaciones y renders comprobados para base, cambio 6600/+600/10% y base cero
con tasa no definida. Pares/grupos, copia y texto coinciden; vacío, duplicado y
destinos existentes se rechazan conservando archivos. `hola.qmd` renderiza y
su bloque sin llaves muestra código sin salida ejecutada. Render aislado conserva
cifras previas tras cambiar CSV, como corresponde al flujo documentado; YAML
inválido falla y puede dejar HTML previo. HTML separado inspeccionado por parser:
idioma, título, secciones, cifras y recursos de presentación incluidos.
Preview respondió HTTP y actualizó al guardar desde una comprobación fuera del
ejecutor restringido, que no permite conectarse al puerto local. No se automatizó
el botón Render del IDE. El navegador integrado no permitió revisar el archivo
local; no se acredita revisión visual, offline en navegador ni accesibilidad completa.
Los pasos de lectura/ventana estrecha quedan explícitos en el lab.
No cambian dependencias, lockfiles, Conda, renv ni bibliotecas globales.
Proyecto/checkpoints y práctica del estudiante pendientes. Cierre de la sesión
de desarrollo solicitado; siguiente sección por implementar: 11.03.

**Desarrollo — 2026-10-23, 11.01:** disponibles la
[lección](curriculum/11_reporting_quarto/01_report_source_render/README.md),
CSV autónomo, preparadores Python estándar/R base y
[lab](labs/11_reporting_quarto/01_report_source_render/README.md).
Pregunta/público, entrada frente a documento fuente, cálculo frente a renderizado,
notebook exploratorio y narrativa con evidencia/límites. Seis filas de tres
créditos en dos cortes: 6000/6300 MXN, diferencia 300 y 5% sobre septiembre.
Cada preparador genera fuente copiada, pares, resumen y borrador Markdown con
cifras insertadas desde los cálculos, en un destino nuevo. El lab cambia una
copia a 6600 MXN, +600 y 10%, conservando la preparación anterior.

**Verificación:** Python 3.12.12/R 4.6.1 (locale UTF-8 en procesos de autoría),
procesos nuevos y 18 casos en ambos
lenguajes: base, cambio, orden invertido, baja, sin cambio, base cero, todos
cero, máximo y rechazos de vacío, cobertura incompleta, duplicados, ID/fecha
incorrectos, ausencia, negativo, decimal, exceso y espacio. Pares, grupos,
texto y copia conciliados; originales y destinos existentes protegidos.
No se añaden dependencias ni cambian lockfiles, Conda, renv o bibliotecas
globales. No se genera `.qmd`/HTML ni se ejecuta Quarto en esta preparación;
las APIs de documentos y motores se contrastaron con fuentes oficiales.
La revisión de autoría no prueba la interfaz del IDE ni acredita práctica del
estudiante. Proyecto `05_monthly_report` y checkpoints siguen pendientes.
Retomar con 11.02, después de comprobar los requisitos del primer render.

**Revisión — 2026-10-23, cierre 10.10:** se reprodujeron y corrigieron dos
omisiones: la comparación por clave aceptaba Parquet de salida desordenados
aunque la entrega promete selección por ID/resumen por fecha; la CLI aceptaba
opciones de otra acción y las ignoraba (generar --exigir-decision devolvía
borrador sin avisar). Ahora se exige el orden final y cada acción declara solo
sus opciones, con rechazo antes de crear archivos. La fuente puede seguir
llegando en otro orden. Cuatro grupos de regresión comprueban ambos rechazos,
CLI documentada, decisión pendiente y entregas anteriores válidas con medidas,
vacío, suma amplia, fuente invertida y máximo 1998. Navegación del módulo y
260 Markdown/2666 enlaces locales revisados sin incidencias; git diff --check
sin errores. Sin cambios de dependencias, datos o mediciones previas.
Retoma vigente: 11.01, aún planificada.

**Desarrollo — 2026-10-23, 10.10 y cierre del material de 10:** disponibles la
[lección](curriculum/10_polars_duckdb/10_closure_tool_choice/README.md),
CSV propio de cuarenta filas, generador/verificador de entrega, referencia R
base, recorridos y [lab](labs/10_polars_duckdb/10_closure_tool_choice/README.md).
Contexto/diccionario/reglas completos, mini muestra de seis filas independiente
y todos los valores de veinte créditos/dos cortes. Las diez secciones de 10
tienen lección/lab (10.05 opcional); esto no acredita práctica ni implementa
04_large_credit_dataset o sus checkpoints.

Python 3.12.12, pandas 2.3.3/PyArrow 21.0.0/Polars 2.0.0/DuckDB 2.0.0 y R
base 4.6.1 conservados. No hay instalaciones ni cambios de dependencias,
pyproject/uv.lock, renv o entornos globales. Misma selección y resumen en tres
motores; seis IDs 015–020, 14061 MXN; veinte/26030 y veinte/27690 por corte.
Int64 antes de agregar; cota didáctica <=1998 saldos Int32 justifica BIGINT y
la referencia R double por debajo de 2^53, sin generalizar a cualquier base.

Entrega fuente/contrato, entrada, seis Parquet de resultados, comparación,
manifiesto, mediciones nuevas y decisión inicialmente en borrador. Escritura/
relectura y comparación por clave contra referencia externa Python estándar;
R calcula pares/grupos independientemente. Nueve procesos nuevos con protocolo
10.09 sobre esta entrada/pregunta: solo selección/JSON, no resumen o entrega
completa. La decisión usa contexto/claridad/entorno/costos/límites y condición
para revisarla; verificador de solo lectura exige evidencia/estructura, no
certifica calidad del argumento o autenticidad de tiempos. La revisión humana
pertenece al cierre de práctica, no al estado de autoría.

**Verificación:** seis grupos con subcasos y bloques completos Python de
lección/lab ejecutados; dos entregas con mediciones reales de nueve procesos
para octubre. Segunda biblioteca Python genera/verifica otra entrega con nueve
procesos para noviembre vacío. Septiembre >=2000, octubre >=2002/todos y
noviembre conciliados; vacío completo tipado, suma 4294967294, fechas 1900/2100,
orden físico invertido y máximo 1998 aceptados; 1999, duplicados, ausencias y
negativos rechazados antes de crear entrega. Selección/resumen/entrada con
errores compensados y huellas actualizadas, esquema float, contrato/comparación
alterados rechazados. Borrador, motor/alcance inválido o decisión sin costos no
pasan revisión exigida. Fallo parcial conserva resultados sin manifiesto final;
destinos existentes y fuentes anteriores protegidos, verificación no modifica archivos.
Referencia R base y fronteras comprobadas en procesos nuevos; no se probó la
interfaz del IDE ni Linux/macOS u otras instalaciones. No se acreditan grandes
volúmenes, I/O físico o RAM acotada. Enlaces/fragmentos, navegación y git diff
--check revisados; roadmap y referencias de cierre previas actualizados.

**Siguiente:** [11.01 — Reporte, fuente y renderizado](curriculum/11_reporting_quarto/README.md#01-reporte-fuente-y-renderizado),
después de [storage-closure.md](docs/storage-closure.md). Teoría común de reporte/
fuente/renderizado, contexto/datos completos y recorridos Python/Jupyter y R/knitr
separados al implementar; verificar APIs/herramientas sin instalar solo por
planificar. 11–14, proyectos/checkpoints y práctica del estudiante siguen
pendientes. Este es el punto de retoma vigente; las entradas siguientes son historial.

**Desarrollo — 2026-10-23, 10.09:** disponibles la
[lección](curriculum/10_polars_duckdb/09_time_memory/README.md),
CSV propio, preparador/coordinador/verificador, trabajador aislado, métricas SO,
recorridos y [lab](labs/10_polars_duckdb/09_time_memory/README.md).
Contexto/datos/contrato completos y ejemplos iniciales autónomos. Python 3.12.12,
pandas 2.3.3/PyArrow 21.0.0/Polars 2.0.0/DuckDB 2.0.0 conservados; no se
instalan paquetes ni cambian pyproject/uv.lock o metadatos R. R opcional usa
4.6.1/DuckDB 1.5.6/DBI 1.3.0 del proyecto existente, sin modificarlo.

Mismo Parquet, filtro/orden/pares y JSON UTF-8 en tres variantes: tres
observaciones por motor/nueve procesos nuevos, orden rotado y pools a uno.
Seis fases (importar/configurar/entrada_o_plan/ejecutar_recuperar/adaptar/exportar),
consulta/intervalo/proceso y CPU con límites explícitos. PeakWorkingSetSize y
WorkingSetSize Windows en bytes después de exportar, antes de cerrar conexión/
emitir crudas. Pico absoluto del proceso, no RAM exclusiva de una consulta;
temporales retenidos al final no acreditan I/O ni pico de disco. Entrada leída
en auditoría previa y caché SO sin vaciar: proceso nuevo no se llama disco frío.

Preparación/auditoría y conciliación fuera del trabajador. Seis filas,
003/2600 conservados; cada exportación y esquema se comprueban por clave con
CSV externo/Python estándar. Crudas y medianas/mínimos/máximos conservados,
con hardware conocido/notas, versiones, hilos efectivos y resolución del reloj.
Verificador de solo lectura revisa huellas, pares/exportaciones, fases y orden;
no autentica duraciones históricas. R system.time mide otro intervalo sobre
tabla en memoria/DBI, con tres conexiones en una sesión, sin mezclar protocolos.

**Verificación:** siete grupos de pruebas con subcasos, bloques completos
Python de lección/lab ejecutados y dos corridas reales de nueve procesos para
octubre; segunda biblioteca Python ejecuta nueve procesos para noviembre vacío
y verifica desde otro proceso. Fases suman sus intervalos, exportaciones concilian
y contadores/hilos se registran. Fronteras del trabajador: fuente vacía, umbral
2001, todos los pares, fechas 1900/2100, saldos individuales Int32/suma 4294967294,
escalas 40/400/1998 y base común 28 filas (nueve/24100). Fuente duplicada fuera
del filtro, compensaciones y esquema float rechazados. Pares, exportaciones,
orden, tiempos incoherentes, resumen, columnas/tipos y contadores alterados
rechazados; duraciones ficticias aritméticamente coherentes ilustran el límite
de autenticidad. Verificar no modifica archivos; destinos existentes protegidos.
R ejecutado desde procesos nuevos en ambas bibliotecas existentes, sin probar
la interfaz del IDE. Linux/macOS y otras instalaciones no probados; rama Linux
marcada sin verificar, otras plataformas con contador no disponible. No se
acreditan grandes volúmenes, I/O físico ni RAM acotada. Fuentes, lockfiles y
entregas anteriores conservados; enlaces/fragmentos y git diff --check revisados.

**Siguiente:** [10.10 — Cierre y elección de herramienta](curriculum/10_polars_duckdb/README.md#10-cierre-y-eleccion-de-herramienta),
después de [storage-closure.md](docs/storage-closure.md): pregunta propia,
alternativas con respuesta equivalente y decisión por claridad/entorno/costos
medidos, sin exigir entregas previas ni generalizar desde muestras pequeñas.
10.10 y 11–14 conservan planes; proyectos/checkpoints y práctica del estudiante
siguen pendientes. Este es el punto de retoma vigente; las entradas siguientes
son historial.

**Desarrollo — 2026-10-23, 10.08:** disponibles la
[lección](curriculum/10_polars_duckdb/08_engine_interchange/README.md),
CSV propio, módulo/ejecutor Python, ampliación R/ejecutor/preparador,
recorridos por shell y [lab](labs/10_polars_duckdb/08_engine_interchange/README.md).
Contexto/datos/reglas completos, ejemplos iniciales autónomos en memoria;
no exige Parquet ni entregas personales anteriores. Python 3.12.12,
pandas 2.3.3/PyArrow 21.0.0/Polars 2.0.0/DuckDB 2.0.0; R 4.6.1,
Arrow 25.0.1/DuckDB 1.5.6/DBI 1.3.0. Sin instalaciones, dependencias nuevas
ni cambios en pyproject/uv.lock o DESCRIPTION/renv.lock; conserva entornos globales.

Ocho etapas: pandas → Arrow → Polars → Arrow, registros directos pandas/Polars
y Arrow en DuckDB, salida Arrow/Polars y vuelta completa a pandas/Arrow.
Tipos inspeccionados antes de adaptar y cada valor conciliado por clave con
CSV externo/Python estándar. Seis filas, 003/2600 y resumen tres/4500,
tres/4600 MXN conservados. Equivalencia acotada string/large_string, índice
omitido explícitamente y marcas de ausencia; no acredita igualdad de metadatos
o disposición física. Contrato anulable independiente: 0/ausencia/10 y
vacío/ausencia/café, suma observada 10 y cobertura 2/3. Entero mayor que 2^53
muestra pérdida al pasar a float; no pertenece al contrato Int32 de cartera.

Registro/relación frente a materialización/lector; DuckDB 2.0 usa salida Arrow
desde con.sql para evitar la copia adicional advertida en la ruta DB-API.
Ejemplo separado de lector con lotes 2/2/1 y cierre dentro de la conexión;
no garantiza RAM acotada. R registra Arrow, recupera por DBI, compara clases/
valores y reconstruye Arrow; no instala Polars en R ni implementa esa alternativa.

**Verificación:** ocho grupos Python con fronteras/subcasos en dos entornos
existentes, advertencias tratadas como errores. Bloques completos de lección/lab
ejecutados; fuente y selección vacías tipadas, umbral inclusivo/2001, fechas
1900/2100 y suma 4294967294. Duplicados fuera del filtro, ausencias, negativos,
esquemas float/int64/timestamp, columnas extra y saldos compensados rechazados.
Orden físico invertido aceptado; escalas 40/400 y base común 28 filas (nueve/24100)
conciliadas. Vida de relación frente a Table y agotamiento del lector comprobados.
R ejecutado en ambas bibliotecas existentes y procesos nuevos, con vacío/suma
amplia/fronteras. Error simulado después del registro comprueba retirada y
desconexión. Preparador protege ocupados/personalizaciones y conserva metadatos;
fuentes/lockfiles anteriores intactos. No se probó interfaz del IDE ni otros
sistemas operativos o instalaciones Conda. No se midió rendimiento, I/O o RAM.
Navegación, enlaces/fragmentos, bloques/soluciones y git diff --check revisados.

**Siguiente:** [10.09 — Comparar tiempo y memoria](curriculum/10_polars_duckdb/README.md#09-comparar-tiempo-y-memoria),
después de [storage-closure.md](docs/storage-closure.md): resultados equivalentes,
fases de costo, repeticiones crudas y métricas cuyo alcance sea explícito.
10.09–10.10 y 11–14 conservan planes; proyectos/checkpoints y práctica del
estudiante siguen pendientes. Este es el punto de retoma vigente; las entradas
siguientes son historial.

**Desarrollo — 2026-10-23, 10.07:** disponibles la
[lección](curriculum/10_polars_duckdb/07_duckdb_python_r/README.md),
CSV propio, SQL compartido, funciones/ejecutores Python/R, preparador R,
recorridos y [lab](labs/10_polars_duckdb/07_duckdb_python_r/README.md).
Datos/reglas completos y ejemplos iniciales autónomos; misma consulta con
parámetros y resultado por clave, tipos SQL/clases nativas y limpieza de recursos.
Python 3.12.12/DuckDB 2.0.0 conserva pyproject/uv.lock; R 4.6.1 incorpora
DuckDB 1.5.6/DBI 1.3.0 al mismo proyecto renv, con respaldo_09_09.
renv infiere dbplyr 2.6.0/blob 1.3.0 por el dplyr/backend DBI presentes;
se registran para consistencia sin usarlos como interfaz. Los 46 registros
previos permanecen idénticos. Segunda restauración desde biblioteca vacía y
consulta real comprobadas, sin cambiar Conda, venv raíz ni bibliotecas globales.

Seis filas, 003/2600 y resumen tres/4500, tres/4600 MXN. COUNT/SUM se adaptan
en SQL a texto decimal exacto; muestra independiente demuestra la pérdida
de un HUGEINT mayor que 2^53 al convertirlo a numeric R. Páginas acumuladas
son didácticas: no se acredita RAM acotada ni rendimiento. No se comparte
una base DuckDB persistente entre motores de versiones distintas.

**Verificación:** bloques completos de lección/lab ejecutados; tipos y pares
de octubre, septiembre, frontera 2001 y noviembre vacío. CSV/Parquet vacíos y
suma 4294967294 comprobados en ambos lectores/escritores; lectura cruzada real
en ambas direcciones y procesos nuevos, incluido segundo entorno Python.
Alteraciones compensadas, duplicados fuera del filtro, esquema incompatible
y parámetros inválidos rechazados. Error simulado durante dbFetch comprueba
dbClearResult y dbDisconnect. Preparador comprueba respaldo exacto, SQL idéntico,
repetición/personalizaciones/destinos ocupados protegidos. Se conservan fuentes,
lockfiles y entregas anteriores. No se probó la interfaz del IDE, instalaciones
Conda ni otros sistemas operativos. Enlaces/fragmentos, bloques/soluciones y
git diff --check revisados.

**Siguiente:** [10.08 — Intercambio entre motores](curriculum/10_polars_duckdb/README.md#08-intercambio-entre-motores),
después de [storage-closure.md](docs/storage-closure.md): conversiones entre
pandas/Arrow/Polars/DuckDB, valores/tipos tras adaptar y materialización explícita.
10.08–10.10 y 11–14 conservan planes; proyectos/checkpoints y práctica del
estudiante siguen pendientes. Este es el punto de retoma vigente; las entradas
siguientes son historial.

**Desarrollo — 2026-10-23, 10.06:** disponibles la
[lección](curriculum/10_polars_duckdb/06_duckdb_parquet/README.md),
CSV autónomo, consultas SQL, preparador/verificador, recorridos por shell y
[lab](labs/10_polars_duckdb/06_duckdb_parquet/README.md). DuckDB 2.0.0 se añade
a pyproject/uv.lock; todos los registros anteriores permanecen idénticos salvo
la dependencia del proyecto. Instalación en entorno uv nuevo y segunda
reconstrucción local desde caché comprobadas con Python 3.12.12; no cambia
Conda, renv, venv raíz ni bibliotecas globales. No se incorporan paquetes R.

Ejemplos completos sin entregas previas: tabla pequeña, escritura Parquet en
carpeta nueva y conexión en memoria distinta que consulta el archivo. SELECT,
WHERE, GROUP BY, ORDER BY, parámetros y recuperación con tipos; unión pequeña
como ampliación. Seis filas y tres créditos/dos cortes; selección 003/2600,
resumen tres/4500 y tres/4600 MXN, COUNT BIGINT y SUM INTEGER a HUGEINT.
Archivo Parquet frente a base persistente; COPY puede sobrescribir un archivo
único y la práctica evita destinos existentes mediante carpeta exclusiva.

EXPLAIN muestra plan/estimaciones, EXPLAIN ANALYZE ejecuta solo nuestro SELECT
y se recuperan después sus valores en otra ejecución. Archivos y grupos/Data
Read son métricas del motor, no acreditan I/O físico, RAM acotada o benchmark.
Fuente completa y partes se consultan por separado; auditoría de cada esquema
y todas las filas contra CSV externo con Python estándar, incluida clave global.
La auditoría materializa registros y no se confunde con la consulta selectiva.

**Verificación:** ocho grupos con escenarios/subcasos en los dos entornos uv.
Bloques Python de lección/lab ejecutados en orden, cambiando solo destinos
temporales. Completo/partes, vacío tipado, frontera inclusiva/2001, fechas
extremas y suma 4294967294. Esquemas incompatibles, partes omitidas, duplicados
fuera del filtro, null/negativos y saldos compensados rechazados; orden físico
invertido aceptado. Escalas 40/400/1998 y base común de 28 filas (nueve/24100)
conciliadas. Procesos nuevos, verificación de solo lectura y conservación de
fuentes/lockfiles comprobados. No se probaron instalaciones Conda, otros
sistemas o la interfaz del IDE; no se midió rendimiento ni RAM.
Navegación, bloques/soluciones y git diff --check revisados; 248 Markdown y
2514 enlaces locales sin incidencias, incluidos sus fragmentos.

**Siguiente:** [10.07 — DuckDB desde Python y R](curriculum/10_polars_duckdb/README.md#07-duckdb-desde-python-y-r),
después de [storage-closure.md](docs/storage-closure.md): contexto/datos propios,
misma consulta parametrizada en recorridos separados, tipos y cierre de
conexiones. Revisar clientes R/DBI y compatibilidad antes de ampliar renv,
con respaldo y restauración local. 10.07–10.10 y 11–14 conservan planes;
proyectos/checkpoints y práctica del estudiante siguen pendientes. Este
desarrollo sustituye el punto de retoma anterior; las entradas siguientes son historial.

**Desarrollo — 2026-10-23, 10.05 (extensión opcional):** disponibles la
[lección](curriculum/10_polars_duckdb/05_streaming_memory/README.md),
CSV propio, funciones/preparador/verificador, observador, recorridos completos y
[lab](labs/10_polars_duckdb/05_streaming_memory/README.md). Contexto/datos/reglas
autónomos; ejemplos directos de collect streaming, lotes sin lista y sink
Parquet exclusivo. Plan lógico y físico DOT sin instalar Graphviz; estado de
operaciones, buffers, concurrencia y materialización explicados. APIs oficiales
consultadas y ejecutadas con Polars 2.0.0; collect_batches es inestable.

Seis observaciones y tres créditos/dos cortes, fuente sin ausencias ni claves
repetidas. Octubre ≥ 2000: 003/2600; octubre ≥ 0: tres pares/4600 MXN;
septiembre ≥ 2000: dos/4500; noviembre vacío con String/Int32. Auditoría
completa contra CSV externo separada de la consulta y de los trabajadores;
relectura del sink por cada par. La auditoría materializa datos y no tiene
garantía de memoria acotada. Fuentes conservadas; no exige entregas previas.

**Verificación:** nueve grupos con escenarios/subcasos en dos entornos uv
locales existentes, Python 3.12.12/Polars 2.0.0. Bloques Python de lección/lab
ejecutados en orden, cambiando solo destinos temporales. Consumidores streaming/
in-memory y sink conciliados; tamaños de entrega 1/2/7, vacío, fronteras,
fechas extremas y suma 4294967294. Esquemas alterados, duplicados/null/negativos
fuera del filtro, saldos compensados y destinos existentes rechazados; orden
físico invertido aceptado. Escalas 40/400/1998 y base común de 28 filas
(selección nueve/24100) conciliadas. Procesos nuevos y verificación de solo
lectura comprobados; fuentes y lockfiles conservados.

Observador probado en Windows: procesos collect+escritura/sink separados,
trazas POLARS_VERBOSE limitadas a hijos y PeakWorkingSetSize en bytes tras
consulta/escritura. Pico incluye vida del proceso hasta leer el contador,
importaciones e instrumentación; auditoría/conciliación en el padre. Ambos
archivos releídos y conciliados. No es RAM exclusiva de consulta ni benchmark:
una observación por modo, sin control de caché o afirmación de ahorro general.
Rama Linux/ru_maxrss documentada, no ejecutada; otras plataformas informan
no disponible. No acredita I/O físico, disco temporal ni RAM acotada.

Sin nuevas dependencias, instalaciones o cambios de Conda, renv, venv raíz
o configuración global. Controles, trazas y salidas auxiliares ignorados bajo
output/. No se probaron instalaciones Conda, otros sistemas o la interfaz del IDE.
Navegación, bloques/soluciones y git diff --check revisados; 245 Markdown y
2474 enlaces locales sin incidencias, incluidos sus fragmentos.

**Siguiente:** [10.06 — DuckDB: SQL sobre Parquet](curriculum/10_polars_duckdb/README.md#06-duckdb-sql-sobre-parquet),
después de [storage-closure.md](docs/storage-closure.md). Pregunta/contrato,
archivos frente a base persistente, SQL, EXPLAIN/EXPLAIN ANALYZE y ejecución
conciliada; revisar API/versión antes de incorporar DuckDB localmente. No
instalar por planificar. 10.06–10.10 y 11–14 conservan planes; proyectos/
checkpoints y práctica del estudiante siguen pendientes. El punto de retoma
anterior en 10.05 queda sustituido; las entradas siguientes son historial.

**Desarrollo — 2026-10-23, 10.04:** disponibles la
[lección](curriculum/10_polars_duckdb/04_types_missing_joins/README.md),
CSV propios de saldos/catálogo, funciones/verificador, recorridos completos y
[lab](labs/10_polars_duckdb/04_types_missing_joins/README.md). Ejemplos autónomos
de conversión con originales, pérdida de fracciones/ceros, null/NaN/filtros,
agregaciones con cobertura y uniones por igualdad. Fuentes oficiales consultadas
y APIs ejecutadas con Polars 2.0.0; no exige entregas anteriores.

Seis observaciones, tres créditos y dos cortes; catálogo de tres claves con
002 sin etiqueta y 004 sin uso. Left m:1 conserva seis filas y 4500/4600 MXN;
cuatro coincidencias y dos etiquetas conocidas sobre seis observaciones.
Por corte: tres registros, dos coincidencias, un producto conocido, una etiqueta
pendiente y un registro sin catálogo. Inner/semi/anti y full opcional; duplicar
002 sin control produce ocho filas y 6500/6500 MXN. Se rechazan también claves
duplicadas sin uso, sin deduplicar ni imputar saldos/productos. Las muestras de
saldos opcionales y mediciones flotantes tienen contratos independientes.

**Verificación:** diez grupos con escenarios/subcasos en dos entornos uv
locales existentes, Python 3.12.12/Polars 2.0.0/pandas 2.3.3/SQLite 3.51.1.
Bloques de lección/lab ejecutados en orden, cambiando solo destinos temporales.
Conversión fallida frente a ausencia de origen, truncamiento estricto, NaN,
filtros con desconocidos, grupos sin valores y suma comunicada con cobertura.
Fuente/catálogo vacíos por separado y juntos; esquema conservado, fechas
extremas y suma 4294967294. Claves repetidas/incompletas, columnas/tipos,
valores compensados y banderas/etiquetas alteradas rechazados; orden invertido
aceptado. Los seis campos por fila se concilian con Python estándar y contraste
pandas/SQLite. Unión lazy con motor in-memory comprobada; políticas de claves
null y SUM sin valores contrastadas. Procesos nuevos y solo lectura comprobados.

Sin nuevas dependencias, instalaciones ni cambios de lockfiles, Conda, renv,
venv raíz o configuración global. Fuentes previas conservadas; controles y
salidas auxiliares ignorados bajo output/. No se probaron instalaciones Conda,
otros sistemas o la interfaz del IDE; no se midió rendimiento ni RAM.
Navegación, bloques/soluciones y git diff --check revisados; 242 Markdown y
2435 enlaces locales sin incidencias, incluidos sus fragmentos.

**Siguiente:** [10.05 — Streaming y límites de memoria](curriculum/10_polars_duckdb/README.md#05-streaming-y-limites-de-memoria),
extensión opcional, después de [storage-closure.md](docs/storage-closure.md).
Contexto autónomo, lotes, estado de operaciones y salida/materialización;
verificar soporte real sin prometer memoria acotada. No bloquea el siguiente
esencial previsto, 10.06. 10.05–10.10 y 11–14 conservan planes; proyectos/
checkpoints y evidencia del estudiante siguen pendientes. Este desarrollo
sustituye el punto de retoma anterior en 10.04. Las entradas siguientes son historial.

**Desarrollo — 2026-10-23, 10.03:** disponibles la
[lección](curriculum/10_polars_duckdb/03_polars_lazy_plans/README.md),
CSV autónomo, funciones, preparador/verificador, recorridos de shell y
[lab](labs/10_polars_duckdb/03_polars_lazy_plans/README.md). Ejemplos completos
sin entregas previas: tabla en memoria, escritura Parquet nueva, scan y esquema,
planes lógicos sin optimizar/optimizado y collect real. Las expresiones y
dependencias se explican antes de utilizarlas. Fuentes oficiales consultadas
y APIs comprobadas con Polars 2.0.0.

Seis filas propias y tres créditos/dos cortes; selección octubre 003/2600,
resumen por corte tres/4500 y tres/4600 MXN. El filtro necesita tres columnas
aunque devuelva dos; el resumen proyecta dos de tres. Auditoría completa
separada de consulta nativa: referencia CSV externa con Python estándar,
esquemas/valores por clave y rechazo de incidentes fuera del filtro. No se
infiere I/O físico, rendimiento ni memoria acotada a partir del plan. Se
explica que resolver esquema puede leer metadatos y que collect materializa
la salida; engine auto no identifica lazy con un límite de memoria.

**Verificación:** diez grupos de comprobaciones con escenarios/subcasos en
dos entornos uv locales ya existentes, Python 3.12.12/Polars 2.0.0. Bloques
Python de lección/lab ejecutados en orden, cambiando solo destinos temporales;
frontera inclusiva/2001, vacío con tipos, fechas extremas, suma 4294967294,
parámetros inválidos, null/duplicados/negativos fuera del filtro, esquemas
alterados y valores compensados. Orden físico invertido aceptado; selección
y resumen conciliados en escalas 40/400 y base común de 28 (29000/31800,
nueve/24100). Procesos nuevos y verificación de solo lectura comprobados;
destinos existentes rechazados y fuentes/lockfiles conservados.

Sin instalaciones, dependencias nuevas ni cambios de entornos globales,
Conda, renv o venv raíz. Controles y salidas auxiliares ignorados bajo output/.
No se probaron instalaciones Conda, otros sistemas o la interfaz del IDE.
Navegación, bloques/soluciones y git diff --check revisados; 239 Markdown y
2395 enlaces locales sin incidencias, incluidos sus fragmentos.

**Siguiente:** [10.04 — Tipos, faltantes y uniones](curriculum/10_polars_duckdb/README.md#04-tipos-faltantes-y-uniones),
después de [storage-closure.md](docs/storage-closure.md): contexto autónomo,
null/NaN, conversión, agregaciones y cardinalidad con referencia independiente.
10.04–10.10 y 11–14 conservan planes; proyectos/checkpoints, revisión retroactiva
y evidencia del estudiante siguen pendientes. Este desarrollo sustituye el
punto de retoma anterior en 10.03. Las entradas siguientes son historial.

**Cierre de sesión — 2026-10-23 (hasta 10.02):** disponibles la
[lección 10.02](curriculum/10_polars_duckdb/02_polars_tables_expressions/README.md),
CSV autónomo, funciones, recorridos PowerShell/Bash/Zsh/CMD y
[lab](labs/10_polars_duckdb/02_polars_tables_expressions/README.md).
El usuario corrigió el punto de cierre: 10.02 sustituye el cierre documental
anterior en 10.01 (`6886052`). Navegación, índices, arquitectura y pendientes
reflejan este estado; proyectos/checkpoints y evidencia del estudiante pendientes.

**Qué se desarrolló:** DataFrame/Series/expresiones, select, with_columns,
filter y group_by/agg; contexto, forma de salida, literales/alias y dependencias.
Seis filas completas, IDs textuales, fechas Date y saldos Int32; derivada en
miles Float64 solo para presentación y suma ampliada a Int64 antes de reducir.
Octubre ≥ 2000: 003/2600; resumen septiembre tres/4500, octubre tres/4600 MXN.
Entrada completa auditada antes del filtro, esquema y pares conciliados con
Python estándar; controles didácticos separados de la consulta nativa.
No desarrolla lazy, DuckDB ni mediciones de tiempo/RAM.

**Verificación:** Python 3.12.12/Polars 2.0.0; once grupos de comprobaciones
funcionales con escenarios/subcasos, ejecutados en dos entornos uv locales.
Bloques exactos de lección/lab, esquema vacío, frontera inclusiva/2001,
parámetros inválidos, incidentes fuera del filtro, duplicados, null y tipos
alterados; errores compensados y suma 4294967294 MXN comprobados.
Escalas 40/400 conciliadas; para 40 filas, 26030/27690 MXN y selección seis/14061;
base común de 28, 29000/31800 y selección nueve/24100 también conservados.
Polars y su runtime estándar son los únicos paquetes añadidos al lockfile;
registros anteriores idénticos salvo la dependencia del proyecto. Instalación y
segunda reconstrucción desde entorno vacío (offline con caché local), sin
modificar el venv raíz, Conda, renv ni bibliotecas globales. Rutas/entornos de
autoría y controles auxiliares quedan ignorados bajo output/. No se probaron
instalaciones Conda, otros sistemas ni la interfaz del IDE.
Revisión documental final: 236 Markdown, 2359 enlaces locales sin errores,
fragmentos/bloques/soluciones revisados y git diff --check correcto.

**Próxima sesión:** leer este registro y [storage-closure.md](docs/storage-closure.md),
después desarrollar [10.03 — Polars lazy y planes de consulta](curriculum/10_polars_duckdb/README.md#03-polars-lazy-y-planes-de-consulta).
Presentar datos, reglas y resultados completos sin exigir entregas anteriores;
explicar scan/collect/explain, comparar esquemas/valores tras ejecutar y
distinguir plan de ejecución efectiva. Lazy no implica memoria acotada.
10.03–10.10 y 11–14 conservan planes. La revisión retroactiva de ejemplos/IDE,
proyectos/checkpoints e integración mantienen sus pendientes. Desarrollar el
material no acredita aprendizaje. Las entradas siguientes conservan el historial.

**Cierre anterior — 2026-10-22:** publicada la ampliación de 09.06 (`61a082b`),
09.07 (`d911179`), 09.08 (`c553bbd`), 09.09 (`eb85ac4`) y 10.01 (`03ee6d6`),
con cierre documental `6886052`. Ese punto de retoma queda sustituido por 10.03.

**Desarrollo — 2026-10-22, 10.01:** disponibles la
[lección](curriculum/10_polars_duckdb/01_question_contract_reference/README.md) y el
[lab](labs/10_polars_duckdb/01_question_contract_reference/README.md), con muestra
CSV nueva de seis filas y tres créditos, referencia Python estándar y contraste
opcional R base. Cada ejemplo inicial define sus datos completos; no necesita
entregas personales ni recordar resultados de capítulos anteriores. Reutiliza
reglas verificadas como código y vuelve a presentar fuente, contrato y pregunta.

Octubre ≥ 2000: `003/2600`, una fila y 2600 MXN. Septiembre ≥ 2000:
`002/2000`, `003/2500`, dos filas/4500; frontera 2001, cero y selección vacía
explicados. Contrato de entrada frente a esquema/adaptación de salida, suma
amplia, ausencia frente a vacío y pares frente a conteos/totales. Preparación,
lectura, validación, transformación, materialización y exportación diferenciadas
sin cronometrar. Se investiga documentación primaria Polars/DuckDB, pero no se
instalan ni ejecutan motores ni se fijan sus versiones por anticipado.

Generador opcional determinista, IDs nuevos y dos cortes: ejemplos de 40/400
filas, máximo 1998 por el contrato de tres dígitos. Parámetros inválidos y
destinos ocupados rechazados; no usa azar ni cambia semilla global. Referencia
común opcional de 28 filas presentada de nuevo y conservada (nueve/24100 MXN).

Python 3.12.12 y R 4.6.1, biblioteca estándar/base: bloques exactos de lección/
lab y procesos nuevos comprobados, Python también con -I -S. Ochenta y un
controles Python y cincuenta R: pares/fronteras, orden, selección vacía, tipos,
errores compensados, errores fuera del filtro, duplicados, ausencias, calendario,
desborde y suma de 4294967294. Escalas de 1/20/200/999 créditos conciliadas
entre Python/R en cada ID/importe; determinismo y fuentes intactas comprobados.
Sin cambios de requisitos, lockfiles, renv, bibliotecas globales o muestras
anteriores. Locale C solo en procesos R de revisión; no se probó la interfaz
del IDE. Enlaces/fragmentos, bloques/soluciones y git diff --check revisados.

Siguiente: [10.02](curriculum/10_polars_duckdb/README.md#02-polars-tablas-y-expresiones)
después de [storage-closure.md](docs/storage-closure.md). Presentar de nuevo
contexto/datos/reglas, comprobar la API y el entorno local al incorporar Polars.
No adelantar lazy como requisito de 10.02. Proyecto/checkpoints y práctica del
estudiante siguen pendientes; 10.02–10.10 y 11–14 conservan sus planes.
Las entradas siguientes se conservan como historial.

**Desarrollo — 2026-10-22, 09.09:** disponibles la
[lección](curriculum/09_arrow_parquet/09_shared_contract_closure/README.md) y el
[lab](labs/09_arrow_parquet/09_shared_contract_closure/README.md), con funciones
Python/R y preparador. Ejemplo autónomo de cuatro filas y entrega completa
desde el CSV incluido: fuente/contrato, Parquet completo/partes planas,
resumen/selección, notas/huellas. No requiere entregas previas ni particiones.
Las nueve secciones de 09 tienen material; no queda autoría pendiente del módulo.

La entrega conserva 28 registros, 14 IDs y 29000/31800 MXN; octubre ≥ 2000:
nueve ID/importe y 24100 MXN. Ambos lectores revisan estructura, fuente externa,
esquemas/valores por clave, partes, inventario, resumen, selección, notas y
huellas MD5. Las huellas detectan cambios accidentales, no autentican sesiones
ni sustituyen la relectura; se rechazan saldos compensados aun registrando
las huellas nuevas. Reordenar el Parquet se acepta tras registrar sus nuevos
bytes porque la comparación lógica es por clave.

Bloques completos de lección/lab ejecutados con Python 3.12.12/PyArrow 21.0.0/
pandas 2.3.3 y R 4.6.1/arrow 25.0.1/dplyr 1.2.1/renv 1.3.1. Reconstrucciones
independientes y cuatro combinaciones escritor/lector desde procesos nuevos.
Sesenta y cuatro controles Python, cincuenta y seis R y trece rechazos del
preparador: vacío, fechas/extremos enteros, duplicados, ausencias/fracciones,
desborde/calendario, archivos ausentes/adicionales, esquemas, notas/huellas,
fuente copiada, CSV exportados, alteraciones compensadas y solo lectura.
Entregas vacías/de frontera escritas y verificadas también en el otro lenguaje.

Sin dependencias nuevas ni cambios de lockfiles, fuentes, entornos o entregas
previas. El preparador añade script, consultas compartidas y ruta local; R
se comprobó con lectura de biblioteca renv fuera del ejecutor restringido y
locale C solo en procesos de revisión. Enlaces/fragmentos, bloques/soluciones
y git diff --check revisados. No se midieron I/O, rendimiento o RAM ni se probó
la interfaz del IDE. Proyecto `04_large_credit_dataset`, checkpoints y práctica
del estudiante siguen pendientes; desarrollar contenido no acredita aprendizaje.

**Retomar:** [10.01](curriculum/10_polars_duckdb/README.md#01-pregunta-contrato-y-referencia),
después de [storage-closure.md](docs/storage-closure.md): pregunta, contrato y
referencia antes de cambiar motores. 10–14 siguen planificados. No instalar
paquetes por anticipado. Las entradas siguientes se conservan como historial.

**Desarrollo — 2026-10-22, 09.08:** disponibles la
[lección](curriculum/09_arrow_parquet/08_justified_partitioning/README.md) y el
[lab](labs/09_arrow_parquet/08_justified_partitioning/README.md), como ampliación
opcional, con funciones Python/R y preparador. Ejemplos autónomos de cuatro
filas; carpetas Hive, columnas físicas/virtuales, candidatos, cardinalidad y
políticas de escritura explicadas. Etiqueta textual auxiliar derivada de la
fecha; tres columnas físicas no anulables conservadas en cada archivo.

Base común reconstruida desde CSV, sin entregas previas: 28 filas, 14 IDs,
29000/31800 MXN. Comparación plana/por corte y selección de octubre ≥ 2000:
nueve IDs/24100 MXN, contrastados por clave con CSV en ambos lenguajes.
Dos particiones por corte frente a 28 por clave ID/fecha. Destinos nuevos y
existing_data_behavior error, sin borrar ni sobrescribir; duplicar septiembre
en una copia no altera la consulta de octubre, pero la auditoría lo rechaza.

Bloques completos de lección/lab y fronteras ejecutados con Python 3.12.12/
PyArrow 21.0.0/pandas 2.3.3 y R 4.6.1/arrow 25.0.1/dplyr 1.2.1. Setenta y dos
controles Python, cincuenta y uno R y trece rechazos del preparador: lectura
cruzada, umbrales, vacío con esquema, fechas/extremos enteros, duplicados,
faltantes, notas/subcarpetas intrusas, etiqueta física incorrecta, calendario,
esquemas distintos y alteraciones compensadas. Fuentes, metadatos, lockfiles,
entornos y entregas anteriores conservados. El preparador solo añade script,
módulo de consultas incluido y ruta local. Lectura renv autorizada fuera del
ejecutor restringido; locale C solo en procesos de revisión, sin paquetes nuevos.

Relecturas desde procesos nuevos, verificadores de solo lectura y revisión de
enlaces/fragmentos, bloques/soluciones y git diff --check. Inventarios y
candidatos no miden I/O físico, tiempo ni RAM; no se probó la interfaz del IDE.
No hay proyecto/checkpoint activo ni se acredita práctica del estudiante.
Siguiente: [09.09](curriculum/09_arrow_parquet/README.md#09-cierre-del-contrato-compartido)
y [storage-closure.md](docs/storage-closure.md), con entrega integrada sin exigir
particiones ni resultados personales previos. Las entradas siguientes son historial.

**Desarrollo — 2026-10-22, 09.07:** disponibles la
[lección](curriculum/09_arrow_parquet/07_metadata_compression/README.md) y el
[lab](labs/09_arrow_parquet/07_metadata_compression/README.md), con funciones
Python/R y preparador. Teoría común de archivo/grupo/bloque/página, esquema y
estadísticas, codificación frente a compresión y límites de las mediciones.
Ejemplos de cuatro filas definidos completos, sin archivos ni funciones previas;
dos grupos frente a uno y estadísticas ausentes con valores conservados.

Base común reconstruida desde CSV: 28 registros, 14 IDs y 29000/31800 MXN.
Cuatro variantes (base sin compresión, Snappy, diccionario, grupos de siete),
una modificación respecto de la base por comparación y tres repeticiones con
orden rotado. Escritura/lectura completas separadas de preparación, validación
e inspección; notas crudas locales y verificadores de solo lectura. Los
archivos son variantes completas, no partes que se deban abrir como un dataset.
PyArrow observa estadísticas/códecs/codificaciones reales, también de archivos R;
arrow R 25.0.1 expone esquema/conteos y lectura de grupos, sin ese detalle.

Bloques de lección/lab ejecutados con Python 3.12.12/PyArrow 21.0.0 y
R 4.6.1/arrow 25.0.1, sin paquetes nuevos ni cambios de lockfiles. Setenta y
cinco controles Python, cuarenta y cinco R y trece rechazos del preparador:
vacíos, fechas/extremos enteros, duplicados, ausencias, fracciones, desborde,
archivos ausentes/adicionales, esquema, alteraciones compensadas y notas
inválidas. Intercambio de los doce archivos de cada lenguaje contrastado por
clave con CSV y metadatos; escrituras solo en carpetas nuevas. R se comprobó
con lectura de la biblioteca local fuera del ejecutor restringido y locale C
solo en procesos de revisión. Fuentes, metadatos del proyecto y entregas
anteriores conservados. Relecturas desde procesos nuevos y comprobación de
enlaces/fragmentos, bloques/soluciones y git diff --check.

No se midió RAM ni I/O físico; caché no controlada y sin fsync. Los tiempos R
pueden ser cero por resolución; no comparan velocidad entre lenguajes ni
generalizan rendimiento a partir de 28 filas. No se probó la interfaz del IDE.
Siguiente: [09.08](curriculum/09_arrow_parquet/README.md#08-particionamiento-justificado),
ampliación opcional; [09.09](curriculum/09_arrow_parquet/README.md#09-cierre-del-contrato-compartido)
y proyectos/checkpoints siguen pendientes. Consultar
[storage-closure.md](docs/storage-closure.md). Material disponible no acredita
práctica del estudiante. Las entradas siguientes conservan su carácter histórico.

**Revisión — 2026-10-22, 09.06:** ampliadas la
[lección](curriculum/09_arrow_parquet/06_selective_datasets/README.md) y su
[lab](labs/09_arrow_parquet/06_selective_datasets/README.md). La muestra completa
de cuatro filas aparece antes del código; los ejemplos iniciales declaran el
esquema y escriben/consultan sus archivos directamente con Arrow. No necesitan
CSV, TXT, preparador, funciones ni entregas de capítulos anteriores; sí las
bibliotecas del lenguaje elegido. La base común conserva su recorrido separado.

Se explican unidad y clave, objetos antes/después de materializar, columnas de
filtro frente a proyección, sintaxis Python/R, consulta frente a auditoría y
vacío/cero/ausencia. El lab añade cuatro consultas pequeñas con comparación de
cada ID/importe; la integración R crea su propia copia alterada y puede
ejecutarse sin la ruta Python. Los dos recorridos integrados siguen comprobando
cuatro/12400, ocho/20500 y selección vacía, más rechazo de duplicados fuera del
filtro. Base común de 28 registros y 29000/31800 MXN conservada.

Ejemplos pequeños, fronteras y relectura desde procesos nuevos ejecutados con
Python 3.12.12/PyArrow 21.0.0 y R 4.6.1/arrow 25.0.1/dplyr 1.2.1; lab integrado
ejecutado en ambos lenguajes con carpetas nuevas. En R se permitió la lectura
de la biblioteca renv local fuera del ejecutor restringido; locale C solo en
esos procesos. No se instalaron paquetes ni cambiaron funciones, fuentes,
lockfiles o entregas anteriores. Referencias oficiales revisadas; enlaces,
fragmentos, bloques/soluciones y git diff --check comprobados. No se probó la
interfaz del IDE ni se midieron I/O, rendimiento o RAM.

El siguiente desarrollo sigue siendo **09.07 — Metadatos, row groups y
compresión**, después de [storage-closure.md](docs/storage-closure.md).
Proyectos/checkpoints y evidencia del estudiante mantienen su estado pendiente.

**Cierre de sesión — 2026-10-21 (09.04–09.06):** completado el desarrollo de
[lectura/escritura desde R](curriculum/09_arrow_parquet/04_r_read_write/README.md),
[intercambio Python/R](curriculum/09_arrow_parquet/05_python_r_exchange/README.md)
y [lectura selectiva y datasets](curriculum/09_arrow_parquet/06_selective_datasets/README.md),
con sus labs, funciones, preparadores y navegación. Publicados en `main` los
commits `3ec6d33`, `c4d3b37` y `2badcc3`. Se incorporó a autoría el criterio de
presentar ejemplos con contexto, datos y resultados completos por sección;
la revisión retroactiva del material existente queda pendiente con el usuario.

Se conservan fuentes y entregas anteriores: base de 28 registros, 14 IDs y
29000/31800 MXN. R dispone de arrow 25.0.1 en renv local con respaldo y
restauración comprobada; 09.05–09.06 no añaden dependencias ni cambian lockfiles.
Cruces reales en ambos sentidos y consultas por clave contrastados con CSV;
09.06 distingue auditoría completa, plan de consulta y materialización.
La selección de octubre ≥ 2000 conserva nueve IDs y 24100 MXN, sin atribuir
al ejemplo pruebas de rendimiento, I/O físico o RAM acotada.

Las verificaciones funcionales de cada sección, incluidas sesiones nuevas,
fronteras y conservación de originales, están registradas en las entradas
siguientes. Este cierre es documental: no modifica código, muestras, entornos
ni resultados y no vuelve a ejecutar esas pruebas. Se revisan enlaces,
fragmentos (2193 enlaces locales en 225 Markdown), bloques/soluciones y
git diff --check del estado final, sin errores.

**Para la próxima sesión:** empezar por este registro y
[storage-closure.md](docs/storage-closure.md), después desarrollar
[09.07 — Metadatos, row groups y compresión](curriculum/09_arrow_parquet/README.md#07-metadatos-row-groups-y-compresion).
Investigar las APIs oficiales al implementarla; presentar un ejemplo pequeño
completo, comparar archivos con registros/esquema equivalentes, separar
codificación de compresión y conservar mediciones crudas. No instalar paquetes
solo por planificar ni inferir rendimiento general a partir de 28 filas.
09.07 no se inició; 09.08 sigue opcional y 09.09 pendiente. Proyectos/checkpoints,
práctica del estudiante y módulos 10–14 mantienen su estado pendiente.


**Desarrollo — 2026-10-21, 09.06:** disponible
[Lectura selectiva y datasets](curriculum/09_arrow_parquet/06_selective_datasets/README.md)
y su [lab](labs/09_arrow_parquet/06_selective_datasets/README.md), con funciones
Python/R y preparador. Ejemplo completo de cuatro observaciones en cada lenguaje;
base común presentada con contexto/reglas/resultados, sin exigir entregas previas.
Conserva 28 filas, 14 IDs y 29000/31800 MXN, distribuidas en dos partes planas.

Dataset/Scanner en Python y open_dataset/dplyr en R; proyección y filtro antes
de to_table/collect. Esquemas reales de todos los archivos antes de abrir;
auditoría completa deliberadamente en memoria separada de consulta selectiva.
Referencia CSV con recorrido Python/indexación R base, sin reutilizar el filtro
Arrow para lo esperado. Octubre ≥ 2000: nueve IDs, dos columnas y 24100 MXN.
Lab: octubre ≥ 2800 cuatro/12400, septiembre ≥ 2000 ocho/20500 y selección
vacía de noviembre cero filas, sin afirmar saldo cero del corte completo.

Duplicar septiembre deja correcta la consulta de octubre, pero ambos auditores
rechazan las claves repetidas. Se diferencia validación del conjunto y de su
selección; se conservan claves/valores y originales. Lotes Python como ampliación,
sin acreditar RAM total acotada. No se mide I/O, rendimiento ni bytes omitidos;
no se implementan particiones o validación escalable de grandes volúmenes.

Sin dependencias nuevas ni cambios de lockfiles: Python 3.12.12/pandas 2.3.3/
PyArrow 21.0.0 y R 4.6.1/arrow 25.0.1/dplyr 1.2.1/renv 1.3.1. Mismo proyecto
renv, metadatos, funciones y datos anteriores intactos; preparador solo añade
script/ruta local. No cambia Conda ni bibliotecas globales. Lección/lab ejecutados
con rutas de revisión en procesos nuevos, también ampliación por lotes; no se
probó la interfaz del IDE ni instalación en otros sistemas.

Cincuenta y ocho controles Python, cincuenta y cuatro R y cuatro consultas
adicionales de frontera escritas en R/releídas en Python. Vacío con esquema,
carpeta sin archivos, partes ausentes/extrañas, esquemas distintos incluso en
la última parte, nulabilidad, filas negativas fuera del filtro, alteraciones
compensadas, parámetros/tamaños inválidos y umbrales inclusivos. Todos los
pares Python/R conciliados con CSV estándar; huellas de originales conservadas.
Preparador: fuentes intactas, ruta absoluta y trece rechazos comprobados.
Revisados 2188 enlaces locales/fragmentos en 225 Markdown, bloques/soluciones
equilibrados y git diff --check limpio.

Retomar con [09.07](curriculum/09_arrow_parquet/README.md#07-metadatos-row-groups-y-compresion)
y [storage-closure.md](docs/storage-closure.md). Proyectos/checkpoints y práctica
del estudiante siguen pendientes. Las entradas siguientes describen cierres
anteriores y se conservan como historial.


**Desarrollo — 2026-10-21, 09.05:** disponible
[Intercambio Python y R](curriculum/09_arrow_parquet/05_python_r_exchange/README.md)
y su [lab](labs/09_arrow_parquet/05_python_r_exchange/README.md). Funciones Python/R
y preparador; cada sección presenta datos, contratos y resultados completos,
sin necesitar entregas de capítulos anteriores. Reutiliza los escritores y
validadores de 09.03/09.04, sin cambiar algoritmos, muestras o lockfiles.

Python escribe/R lee y R escribe/Python lee: esquema real antes de convertir,
presencia, dominio, claves y cada valor. Conserva 28 registros, 14 IDs y
29000/31800 MXN. Muestra propia de tres filas con fecha bisiesta, texto
acentuado, vacío/ausencia y cero; esquema independiente con etiqueta/importe
anulables, suma observada 10 y cobertura 2/3, sin inventar el total completo.
Distingue equivalencia lógica, clases y bytes; notas de sesión no acreditan
el cruce. No implementa contratos nuevos para decimales o factores.

Sin dependencias nuevas: Python 3.12.12/pandas 2.3.3/PyArrow 21.0.0 y
R 4.6.1/arrow 25.0.1/renv 1.3.1. Mismo proyecto y biblioteca renv; preparador
solo añade script/ruta local y conserva metadatos, funciones y datos. No
modifica Conda ni bibliotecas globales. Recorridos de lección/lab comprobados
con procesos nuevos, reinicios y permisos de lectura de enlaces R base;
no se probó la interfaz del IDE ni instalación en otros sistemas.

Veintiséis controles Python, veintidós R y cuatro relecturas adicionales:
tipos/nulabilidad, filas repetidas/faltantes, acentos/fechas, ausencia frente
a vacío/cero, muestras incompletas y archivo falso. Cruces con fuente vacía
y cinco fronteras válidas de 09.02; orden invertido y metadatos auxiliares
aceptados por clave. Saldos intercambiados conservan sumas pero fallan en ambos
lectores; reemplazar vacío por ausencia también falla. Huellas de originales
conservadas. Preparador: ruta absoluta/fuentes intactas y trece rechazos
conservadores comprobados; ninguna salida personal se incorpora al material.
Revisados 2158 enlaces locales/fragmentos en 223 Markdown, bloques/soluciones
equilibrados y git diff --check limpio.

Al cerrar 09.05 se dejó previsto [09.06](curriculum/09_arrow_parquet/06_selective_datasets/README.md)
y [storage-closure.md](docs/storage-closure.md). Proyectos/checkpoints y práctica
del estudiante siguen pendientes. Las entradas siguientes describen cierres
anteriores y se conservan como historial.


**Desarrollo — 2026-10-21, 09.04:** disponible
[Leer y escribir desde R](curriculum/09_arrow_parquet/04_r_read_write/README.md)
y su [lab](labs/09_arrow_parquet/04_r_read_write/README.md), con funciones,
ejecutor, preparador, DESCRIPTION y lockfile real. Ejemplo de tres créditos
definido completo en la lección y muestra propia de dos en el lab; la base común
se presenta de nuevo con contexto, reglas y resultados. No requiere entregas
personales Python ni reconstruir los ejercicios de cartera de 07–08. Criterio
incorporado a autoría; revisión retroactiva de ejemplos existentes pendiente.

Arrow 25.0.1/assertthat 0.2.1 añadidos al mismo proyecto renv con respaldo
08.09 y 44 registros previos idénticos; segunda restauración local desde
biblioteca vacía comprobada. R 4.6.1/renv 1.3.1, sin cambiar Conda ni bibliotecas
globales. El ejecutor necesita lectura de los enlaces renv a paquetes base;
se comprobó con esos permisos sin desactivar verificaciones.

Esquema string/date32/int32 no anulable; lectura del esquema real antes de
convertir, validación de presencia/dominio/clave y comparación completa por
ID/fecha. Entrega nueva con Parquet/resumen/sesión y verificador de solo lectura;
28 registros, 14 IDs y 29000/31800 MXN. Los ejemplos de ausencia/cero usan
otra tabla y otro permiso, sin modificar la cartera. Fuentes y entregas previas
conservadas; no se exige identidad binaria entre escritores.

Siete bloques de lección después de preparar y tres de lab comprobados desde
procesos nuevos, también con la segunda biblioteca restaurada. Cuarenta y siete
controles adicionales: vacío en disco, límites/suma, NA, fracciones, Date con
fracciones/infinitos, calendario/rango, tipos/nulabilidad, claves, metadatos,
orden inverso, archivo falso, alteración compensada y destinos ocupados.
Python 3.12.12/PyArrow 21.0.0 concilia esquema y todos los valores de cuatro
entregas R. Se comprueba lectura en R de la referencia escrita por Python;
09.05 sigue pendiente como práctica completa de intercambio en ambas direcciones.
Preparador: copia/respaldo y nueve rechazos conservadores comprobados.
Revisados 2130 enlaces locales/fragmentos en 221 Markdown, bloques/soluciones
equilibrados y git diff --check limpio. No se probó la interfaz del IDE ni
instalación en otros sistemas.

Al cerrar 09.04 se dejó previsto [09.05](curriculum/09_arrow_parquet/05_python_r_exchange/README.md)
y [storage-closure.md](docs/storage-closure.md). Proyectos/checkpoints y práctica
del estudiante siguen pendientes. Las notas anteriores se conservan como
historial del estado al cierre de cada sesión.

**Cierre de sesión — 2026-10-21:** revisada la teoría de 09.01 y ampliadas las
explicaciones de filas/columnas, selección lógica frente a lectura física,
codificación de texto/valores y compresión, serialización y condiciones del
intercambio Arrow. Ejemplos conceptuales con registros ya conocidos; lab,
solución y procedencia actualizados. Corregidas referencias al estado de 09.03:
PyArrow ya está declarado desde esa sección, aunque no se requiere para el
esencial de 09.01. Fuentes oficiales revisadas; no se modifican scripts, muestras,
entornos, dependencias ni resultados. No se inició 09.04; sigue siendo el punto
para retomar después de este cierre. Los proyectos/checkpoints y la evidencia
del estudiante permanecen pendientes.
Comprobados esencial Python (también con -S), decodificación PyArrow y los dos
bloques R de lección/lab desde procesos nuevos; ejemplos conceptuales contrastados
con el CSV. Revisados 2097 enlaces locales/fragmentos en 219 Markdown, bloques
y soluciones equilibrados y git diff --check limpio.

**Criterio de autoría acordado:** en R, priorizar RStudio o el IDE elegido,
scripts y ejecución por bloques; terminal/Rscript solo cuando aporten al objetivo
o como alternativa opcional. Distinguir consola R de terminal. Aplicar desde el
material nuevo. 07.01 y su lab ya se ajustaron; 07.02–07.10 nacen con ese recorrido. Revisar las demás lecciones
implementadas posteriormente con el usuario.

**Cierre anterior — 09.03:**
[09.03 — Leer y escribir desde Python](curriculum/09_arrow_parquet/03_python_read_write/README.md),
con [recorridos por shell/gestor](curriculum/09_arrow_parquet/03_python_read_write/recorridos.md),
[funciones/ejecutor/verificador](curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py)
y [lab](labs/09_arrow_parquet/03_python_read_write/README.md).
PyArrow 21.0.0 queda declarado en pyproject.toml/uv.lock; todos los registros
previos, salvo la dependencia del proyecto, permanecen idénticos, con pandas
2.3.3 conservado. Python 3.12.12; entorno uv local nuevo y segunda reconstrucción
desde caché, sin modificar Conda ni bibliotecas globales. El venv anterior de la
raíz no se reutilizó porque apuntaba a un intérprete inexistente; se conservó.

CSV de 09.01 validado bajo 09.02, DataFrame con string/date/Int32, esquema Arrow
string/date32/int32 no anulable, índice omitido y metadatos pandas auxiliares
retirados. Escritura en carpeta nueva, cierre y relectura real por clave;
Parquet y sesion.json sin rutas personales. Verificador de solo lectura
reconstruye el CSV; misma base de 28 registros/14 IDs y 29000/31800 MXN.
Nueve bloques de lección/lab comprobados en proceso nuevo y treinta controles
adicionales: vacío tipado en disco, límites/cero, ausencias, tipos/nulabilidad,
claves, orden, alteración compensada, firma falsa, destinos ocupados, columna
extra, archivo bajo carpeta con nombre de partición y fallo de escritura.
Muestra 09.01, reglas/casos 09.02 y lockfiles R conservados; lectura R y cruce
siguen pendientes. La nota JSON no sustituye volver a verificar el archivo.
No se probaron instalaciones Conda/Bash en otros equipos ni interfaces IDE.
Los lectores previos 09.01 (incluida decodificación Parquet) y 09.02 pasan
en el entorno nuevo; uv pip check confirma compatibilidad de sus 25 paquetes.
Revisados 2092 enlaces locales/fragmentos fuera de bloques en 219 Markdown,
bloques y soluciones equilibrados y git diff --check limpio.

[09.02 — Esquemas y tipos entre lenguajes](curriculum/09_arrow_parquet/02_schemas_types/README.md)
dispone de [evaluador Python](curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.py),
[evaluador R](curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.R),
[casos separados](curriculum/09_arrow_parquet/02_schemas_types/casos_contrato.csv)
y [lab](labs/09_arrow_parquet/02_schemas_types/README.md).
Contrato de la base conocida sin cambiar sus 28 registros: nombres, clave,
tipos y nulabilidad; ausencia/vacío/cero, calendario, rango y precisión.
Veintitrés casos separados: cinco aceptados/dieciocho rechazados, con textos y
todos los motivos conservados, incluidas ambas apariciones de claves repetidas.
Centavos/decimal, Date/timestamp y categorías se explican sin dependencias nuevas;
no se acredita conversión ni lectura Parquet en R.

Comprobados los cinco bloques Python/R de lección y lab desde procesos nuevos,
con Python 3.12.12/R 4.6.1 y sin paquetes externos. Los 23 casos oficiales y
39 fronteras adicionales concilian textos, fechas, saldos y motivos entre ambos
lenguajes; vacío, orden invertido, claves con saldo inválido y tres CSV malformados
comprobados. Año cero se rechaza explícitamente también en R para conservar
el calendario compartido. Se conservan muestra e inventario 09.01, requisitos
y lockfiles; sus dos inspectores esenciales siguen pasando. Locale UTF-8 solo
en los procesos de revisión; no se probó la interfaz del IDE.
Revisados 2051 enlaces locales/fragmentos fuera de bloques en 216 Markdown,
bloques y soluciones equilibrados y git diff --check limpio.

En el cierre de 09.03 se dejó previsto [09.04 — Leer y escribir desde R](curriculum/09_arrow_parquet/README.md#04-leer-y-escribir-desde-r):
incorporar arrow al mismo proyecto renv con respaldo/lockfile y restauración
local real, sin cambiar dependencias previas. IDE como recorrido principal;
leer el esquema real y comparar todos los valores por clave, con casos separados
de ausencia/rango/calendario. Consultar los [pendientes de almacenamiento](docs/storage-closure.md).

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

En ese cierre, 09.04–09.09 seguían pendientes (09.08 opcional); la lectura Parquet
en R todavía no estaba implementada. Las nueve secciones de 08 tienen material, pero falta evidencia
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
