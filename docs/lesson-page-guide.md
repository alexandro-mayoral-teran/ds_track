# Estructura común de una lección

Patrón acordado a partir de una revisión de muestra, 2026-10-27. Define lo que
el estudiante debe poder encontrar en cada lección, con un inicio y un cierre
reconocibles. El desarrollo cambia según la actividad: explicar Markdown,
preparar un entorno, consultar datos o construir un reporte.

Usa la [plantilla de lección](../templates/lesson/README.md), junto con la
[guía de autoría](authoring-guide.md) y la
[guía de presentación Markdown](markdown-study-guide.md). La cobertura aplicada
está en el [índice de documentación](README.md#cobertura-de-las-plantillas-y-del-portal);
la estructura de una página no acredita que sus ejemplos se hayan ejecutado.

## Qué se revisó y qué encontramos

El patrón se definió contrastando lecciones iniciales y de Python, pandas, SQL,
R y Quarto. La base didáctica compartía propósito, ejemplos y comprobación;
variaban la ubicación de preparación, objetivos, evidencia y continuidad.
La estructura hace esos elementos localizables sin fijar la cantidad de conceptos,
formatos ni sesiones. La [cobertura vigente](README.md#cobertura-de-las-plantillas-y-del-portal)
indica dónde se aplicó; el historial de adaptación pertenece a PROGRESS.md.

<a id="estructura-propuesta"></a>

## Estructura común

Cabecera breve → propósito → preparación → objetivos → material de apoyo cuando
exista → desarrollo adaptable → lab → evidencia y comprobación → referencias →
continuidad.

| Parte | Elementos comunes | Qué puede cambiar |
| --- | --- | --- |
| Cabecera | Identificador completo NN.LL, nombre, enlace al módulo; ficha Meta / Necesitas / Evidencia; acceso al lab y al cierre | Índice de recorridos si hace falta; alcance esencial u opcional cuando corresponda |
| Propósito | Para qué sirve y qué problema ayuda a resolver | Contexto de trabajo y conexión con el recorrido |
| Antes de empezar | Conceptos previos enlazados, herramientas y archivos necesarios; dónde trabajar | IDE, entorno, shell o preparación específica; decir si no hay instalación ni archivo de entrada |
| Qué vas a aprender | Pocos objetivos observables que se recuperan en la comprobación | Acciones y número de objetivos según el alcance |
| Material de apoyo | Índice breve con enlaces, finalidad y uso necesario u opcional; enlaces también donde se utilizan | Notebooks, scripts, datos, diccionarios, plantillas o guías que realmente ayuden; omitir si no existen recursos adicionales |
| Desarrollo | Explicación gradual, ejemplo comprensible, resultado esperado y forma de comprobarlo | Títulos, cantidad de secciones, formatos y recorridos |
| Práctica | Enlace al lab y tarea central en una frase | Variantes esenciales u opcionales; no repetir la consigna completa |
| Evidencia y criterio de salida | Qué conservar, qué comprobar y qué explicar; siguiente duda o límite | Archivo, nota, consulta, notebook o resultado de otra naturaleza |
| Referencias | Fuentes primarias o libros abiertos pertinentes, atribuciones | Versiones y límites de lo contrastado cuando sean relevantes |
| Siguiente paso | Navegación al módulo, lab y siguiente lección disponible | Anterior opcional; al cerrar módulo puede llevar al índice siguiente para elegir ruta |

Mantener esos nombres para los apartados comunes al crear o adaptar una lección.
Los apartados del desarrollo usan nombres descriptivos del tema. No obligar a
encerrar toda la explicación bajo un único encabezado «Desarrollo».

### Cabecera que permita ubicarse

- Usar `# NN.LL — Nombre de la lección` sin renumerar carpetas ni el track.
- La ruta de ubicación enlaza inicio y módulo; el identificador evita confundir
  00.05 con 01.05.
- La ficha es un resumen de tres filas. «Necesitas» orienta; la preparación
  detallada vive en «Antes de empezar». «Evidencia» anticipa el producto; el
  cierre explica cómo revisarlo. No copiar párrafos completos en ambas partes.
- Mostrar alcance opcional antes de comenzar. Una ampliación no bloquea avanzar.
- Añadir accesos a los recorridos solo si ayudan a elegir. No fijar tiempos ni
  progreso sin evidencia, ni usar casillas compartidas como registro de dominio.

### Material de apoyo localizable y explicado

Combinar dos accesos: una sección «Material de apoyo» después de los objetivos
y un enlace en el punto concreto del recorrido donde se usa cada recurso.
El índice permite encontrarlo de nuevo; el enlace contextual explica qué abrir,
para qué, qué preparación requiere y qué observar o comprobar.

Usar la tabla «Recurso / Para qué sirve / Uso». Distinguir lo necesario para
una actividad de la consulta opcional; publicar un enlace no convierte el recurso
en requisito. En notebooks indicar kernel/entorno y reinicio cuando corresponda;
en código, dónde ejecutarlo y qué resultado revisar. No añadir esas instrucciones
si el recurso solo se lee. El lab conserva su apartado propio.

Enlazar archivos existentes junto a la lección o en su ubicación compartida, sin
duplicarlos para llenar la tabla. No exigir un notebook, script o dataset por
lección ni crear carpetas vacías. Si el ejemplo completo está en la propia
página y no necesita archivos adicionales, se puede omitir este apartado.
Las fuentes teóricas y documentación primaria permanecen en «Referencias»;
una guía usada durante la actividad puede aparecer también como apoyo.

Primera prueba aplicada en [00.01 — Markdown y perfil](../curriculum/00_getting_started/01_github_profile/README.md):
plantilla de perfil, guía de adaptación y bitácora personal. La plantilla se
enlaza al crear el perfil; la bitácora, al conservar evidencia. Esta actividad
trabaja con Markdown y no necesita notebooks ni scripts.

### Prueba con material nuevo: 12.01

[12.01 — Primera app y modelo de ejecución](../curriculum/12_streamlit/01_first_app_execution/README.md)
aplica la plantilla desde el inicio: mínimo completo, datos propios, predicciones,
observación de interacciones, variante y reconstrucción. La preparación extensa
por gestor/shell vive en un apoyo enlazado; la lección mantiene el arranque y su
explicación. El lab practica sin duplicar la teoría y cierra con una solución
razonada oculta. El índice distingue el material disponible de los alcances previstos.

No fue necesario añadir apartados obligatorios a la plantilla. El desarrollo se
amplió para explicar servidor/navegador/script y ejecución de arriba abajo antes
de exigir interacciones. Una imagen y un diagrama acompañan alternativas textuales.
Las comprobaciones de autoría no sustituyen la evidencia de quien estudia ni
obligan a incluir AppTest en todas las lecciones; ese tema tiene su sección posterior.

### Desarrollo que se adapte al tema

Cada bloque importante debe permitir responder: ¿qué problema resuelve?,
¿qué recibo?, ¿qué hago?, ¿qué debería observar? y ¿cómo lo compruebo?
Estas preguntas orientan la explicación; no requieren cinco subtítulos repetidos.

Cuando haya datos, presentar su procedencia sintética, unidad de fila, campos,
claves, reglas, ausencias y unidades pertinentes antes de operar. Empezar, cuando
sea posible, con una muestra pequeña completa. Después conectar con archivos o
funciones compartidos mediante enlaces y explicación suficiente; preparar el
entorno no implica exigir entregas personales de lecciones anteriores.

Para Markdown o terminal, la entrada puede ser un texto, una estructura de
carpetas o un comando; no inventar una tabla de datos ni un contrato numérico.
Los resultados esperados pueden ser visuales o una explicación comprobable.

Alternar explicación, ejemplo y lectura del resultado. Añadir una pregunta de
predicción o un cambio pequeño cuando ayude a practicar antes del lab. Presentar
sintaxis nueva antes de exigirla. Los errores habituales van junto al concepto o
en una tabla breve de diagnóstico; no llenar apartados sin un caso útil.

Las ampliaciones se marcan donde comienzan. Pistas y soluciones pueden usar
`details` cerrado; requisitos, pasos esenciales y criterio de salida permanecen
visibles. Tablas, imágenes y Mermaid se usan cuando aclaran algo, con explicación
que también funcione sin renderizador. No se exige un diagrama por lección.

### Cierre que permita revisar con otra persona

La evidencia es lo que se conserva; el criterio es lo que permite evaluar esa
evidencia. Un archivo guardado o una captura de éxito no basta por sí solo.
Usar una tabla breve «Conserva / Comprueba / Explica» vinculada a los objetivos.
Por ejemplo, en una unión: consulta y claves elegidas / filas e importes
conciliados / por qué la cardinalidad evita multiplicaciones.

Quien aprende realiza la práctica y explica decisiones. Su compañero revisa
una comprobación y plantea una variación o pregunta. No convertir esa revisión
en una segunda solución que el estudiante solo copie.

La evidencia y las dudas se guardan en la copia o bitácora personal; PROGRESS.md
del repositorio registra desarrollo editorial. No inventar proyectos ni
checkpoints: enlazarlos solo cuando existan e indicar su ausencia cuando aplique.
Material desarrollado no significa aprendizaje completado.

## Variantes que conserva la estructura

| Caso | Cómo aplicar el patrón |
| --- | --- |
| Entrada con varias partes, como 00.05 | Cabecera y cierre comunes en la entrada; tabla parte / resultado / enlace. Cada parte indica dónde empezar, qué necesita y cómo regresar o continuar. Evitar duplicar toda la teoría y el lab en la entrada |
| Varios shells | Recorridos completos separados: PowerShell y después Bash/Zsh; CMD cuando corresponda a Anaconda Prompt. Elegir uno sin alternarlos paso a paso |
| Varios motores, como Python/R | Explicar lo compartido una vez; dar recorridos completos con entradas y resultados identificados. Decir si basta elegir uno o si comparar ambos es parte del objetivo |
| R | Abrir proyecto, editar y ejecutar bloques en RStudio o IDE elegido, inspeccionar objetos y repetir el script tras reiniciar sesión. Diferenciar consola R y terminal; Rscript cuando sea necesario o como apoyo |
| Notebook | Identificar kernel, observar resultados y comprobar reinicio y ejecución completa; no exigir un script adicional sin motivo |
| Lección de cierre | Recuperar capacidades y controles pertinentes, conservar evidencia integrada y declarar proyectos pendientes; no repetir toda la teoría |
| Lección opcional | Mostrarlo en la apertura y permitir saltar al siguiente paso esencial disponible |

Una página corta puede resolver un apartado en una frase. Si una lección ocupa
varias sesiones, señalar puntos de pausa y cómo retomar. No fijar una extensión
en líneas ni exigir notebooks, scripts, gráficos y CSV en todos los temas.

## Aplicación gradual y revisión

1. Usar la plantilla para material nuevo y adaptar una lección completa como
   prueba antes de migrar el resto. 00.01 aporta la referencia visual; 00.02
   permite probar un caso largo y con varios recorridos.
2. Conservar ejemplos, reglas, datos, numeración y anclas enlazadas al cambiar
   títulos. Corregir afirmaciones antiguas sobre material pendiente tras revisar
   los destinos, sin dar por hecha una revisión retroactiva completa.
3. Comprobar enlaces lección ↔ lab, regreso al módulo y lab → siguiente lección.
   Referencias antes de la navegación final para que continuar sea fácil.
4. Revisar objetivos contra evidencia, comprobación y explicación. Separar
   instrucciones para el estudiante de la bitácora de pruebas del autor.
5. Verificar Markdown renderizado y lectura estrecha. Si la lección está
   integrada en el portal, comprobar también catálogo, generación y anclas;
   una plantilla no modifica automáticamente su composición.

La [lección 00.01](../curriculum/00_getting_started/01_github_profile/README.md)
es la referencia inicial. La cobertura por módulo y la integración real en el
portal se mantienen en el [índice de documentación](README.md#cobertura-de-las-plantillas-y-del-portal).
No dar por migradas otras páginas ni por acreditado aprendizaje al aplicar la
plantilla. Registrar la revisión concreta y el siguiente paso en PROGRESS.md.
