# Arquitectura de aprendizaje — {{NOMBRE_DEL_PROYECTO}}

Copiar como docs/architecture.md y completar {{...}} para el nuevo tema. Este
documento explica cómo diseñar el recorrido y registra su estructura resultante;
no es una lista de herramientas ni una copia de la bitácora de desarrollo.

## 1. Definir la intención antes de las carpetas

- Tema y problema: {{TEMA_Y_PREGUNTA_CENTRAL}}.
- Público y conocimientos previos: {{PUNTO_DE_PARTIDA_REAL}}.
- Modalidad: {{COMO_SE_ESTUDIARA_Y_QUIEN_ACOMPANA}}.
- Capacidad final: {{QUE_PODRA_HACER_LA_PERSONA}}.
- Evidencia final: {{COMO_SE_PODRA_COMPROBAR}}.
- Alcance excluido: {{QUE_NO_SE_EXIGIRA_EN_ESTA_RUTA}}.

Describir resultados con acciones y condiciones observables. Evitar un objetivo
como «conocer varias herramientas» sin una práctica que permita comprobarlo.

## 2. Investigar y construir el orden

1. Reunir referencias oficiales, libros o fuentes reconocidas del tema; registrar
   autoría, edición y enlace. Distinguir contenidos estables de APIs o reglas cambiantes.
2. Descomponer el resultado final en capacidades y determinar sus prerrequisitos.
3. Ordenar lo básico antes de la aplicación que lo necesita; justificar transiciones.
4. Introducir calidad, explicación y documentación desde prácticas iniciales.
5. Separar alternativas y profundizaciones que no bloquean lo esencial.
6. Proponer prácticas y criterios de salida antes de implementar toda la ruta.

Orden resultante: {{SECUENCIA_DE_CAPACIDADES_Y_RAZON_DEL_ORDEN}}.
Alternativas: {{CAMINOS_EQUIVALENTES_Y_COMO_SE_ELIGE}}.
Pendientes: {{DECISIONES_QUE_AUN_NO_SE_HAN_CERRADO}}.

Cuando varios lenguajes o herramientas resuelvan el mismo problema, explicar
la teoría una vez y presentar recorridos completos por separado. Reutilizar
ejemplos y evidencias comparables en lugar de repetir el curso desde cero.

## 3. Responsabilidades de la documentación

| Área | Responsabilidad | Evitar |
| --- | --- | --- |
| README.md | Orientar, explicar cómo empezar y cómo estudiar | Un diagrama sin instrucciones |
| ROADMAP.md | Capacidades, prerrequisitos y criterios del plan | Copiar la bitácora diaria |
| docs/architecture.md | Estructura, transiciones y decisiones | Duplicar toda la teoría de lecciones |
| curriculum/ | Enseñar conceptos en secuencia | Ejercicios con teoría no explicada |
| labs/ | Practicar una habilidad y comprobarla | Repetir la lección completa |
| projects/ | Integrar habilidades mediante checkpoints | Proyectos vacíos por anticipación |
| resources/ o datasets/ | Materiales o muestras con origen claro | Archivos privados o voluminosos sin necesidad |
| templates/ | Reducir decisiones repetidas | Ejemplos sin adaptar presentados como definitivos |
| showcase/ | Productos terminados apropiados para compartir | Salidas temporales o incompletas |
| Registro de estado elegido | Avance, evidencias y siguiente paso | Confundir material desarrollado con aprendizaje |
| AGENTS.md | Reglas de trabajo y decisiones vigentes | Historial de todas las conversaciones |

Adaptar nombres al tema. No crear todas estas carpetas desde el inicio; cada una
aparece cuando contiene material útil. Esta tabla es una propuesta de responsabilidades,
no un requisito de infraestructura.

## 4. Flujo de una sesión

```text
comprender → practicar → comprobar → explicar → registrar → continuar

lección → lab asociado → siguiente lección → siguiente lab
cuando existe: lab → checkpoint de proyecto → evidencia integrada
producto terminado apropiado → showcase
```

Una sesión puede cubrir parte de una lección. El cierre del lab enlaza la siguiente
lección, no exige resolver otro lab sin haber estudiado su material.
Enlazar lección y práctica en ambos sentidos. Un checkpoint no es obligatorio
cuando todavía no hay un proyecto asociado.

## 5. Mapa de módulos

Definir la numeración después de revisar prerrequisitos. Cada módulo enseña una
capacidad principal; explicar su resultado y por qué prepara el siguiente.

| Orden | Módulo | Requisito de entrada | Capacidad de salida | Alcance |
| --- | --- | --- | --- | --- |
| {{ORDEN}} | {{NOMBRE_DEL_MODULO}} | {{PRERREQUISITO}} | {{RESULTADO_COMPROBABLE}} | {{ESENCIAL_PRACTICA_EXTENSION_AVANZADO}} |

No fijar la cantidad de módulos por imitar otro proyecto. Si dos rutas son
alternativas, hacer explícito que basta una y señalar dónde se reúnen de nuevo.
Temas avanzados pendientes no se presentan como módulos implementados.

## 6. Plan interno de cada módulo

| Orden | Sección | Conceptos necesarios | Práctica prevista | Evidencia y comprobación |
| --- | --- | --- | --- | --- |
| {{ORDEN}} | {{SECCION}} | {{CONCEPTOS}} | {{ACTIVIDAD}} | {{RESULTADO_Y_COMO_VALIDARLO}} |

En cada README de módulo incluir propósito, prerrequisitos, orden, alcance por
sección, prácticas, criterio de salida, siguiente módulo y referencias.
Mientras sea planificación, los enlaces pueden llevar a apartados del propio
README; indicar claramente que aún no hay lecciones ni labs ejecutables.

Al implementar una sección, crear su contenido, ejemplo si corresponde y lab;
actualizar índices y enlaces. No anunciar una lección disponible antes de comprobarla.

## 7. Formatos, ejemplos y herramientas

Formato principal: {{FORMATO_APROPIADO_PARA_LA_EXPLICACION}}.
Formatos de práctica: {{FORMATOS_QUE_APORTAN_A_LA_ACTIVIDAD}}.
Ejemplo compartido: {{CASO_SIMPLE_QUE_CRECE_CON_EL_RECORRIDO}}.

Seleccionar herramientas por el problema que resuelven, sus requisitos y una
alternativa más sencilla. Introducir dependencias cuando se implementa su uso;
registrar versiones o condiciones necesarias cuando corresponda.

Si el recorrido transforma datos o archivos, definir entrada preservada,
salidas regenerables, unidades, reglas y comprobaciones. Si no trata programación,
adaptar estas nociones a los materiales y resultados de la disciplina.

## 8. Integración y criterios de cierre

Proyecto o actividad integradora: {{PRODUCTO_Y_PREGUNTA}}.
Prácticas reutilizadas: {{LECCIONES_QUE_PREPARAN_LA_INTEGRACION}}.

| Checkpoint propuesto | Capacidades integradas | Resultado | Comprobación |
| --- | --- | --- | --- |
| {{CP_ID}} | {{CAPACIDADES}} | {{PRODUCTO_PARCIAL}} | {{EVIDENCIA}} |

Los checkpoints se concretan cuando existe el proyecto. Reutilizar resultados
anteriores y evitar imponer un problema nuevo al enseñar una herramienta adicional.
Definir un cierre esencial alcanzable; servicios de pago, publicación y otras
ampliaciones solo se exigen si forman parte del objetivo declarado.

## 9. Estado, evidencias y diagrama

Registro elegido: {{ARCHIVO_O_ESTRUCTURA_DE_SEGUIMIENTO}}.
Distinguir estado del material (planificado, en desarrollo, disponible) y estado
del aprendizaje (pendiente, en práctica, demostrado). Se pueden usar secciones
separadas o archivos diferentes; decidirlo explícitamente y mantener una fuente
de verdad para cada tipo de estado.

El diagrama muestra etapas, transiciones y rutas alternativas. Mantener títulos
legibles, colores consistentes y poco texto; no usarlo para atribuir habilidades
que todavía no se han demostrado. Al cambiar el orden, actualizar referencias.

## 10. Revisión antes de desarrollar

- El público puede comenzar sin requisitos ocultos.
- El orden respeta dependencias y explica cada cambio de herramienta o tema.
- Cada sección tiene una práctica y una evidencia que permiten comprobarla.
- Lo opcional no bloquea el cierre esencial.
- Las referencias sustentan el contenido y las fuentes cambiantes se comprobarán.
- Roles de archivos, navegación y estados están claros.
- Las decisiones pendientes están nombradas y no se presentan como resueltas.
- El siguiente paso es una lección concreta que puede implementarse y revisarse.

Próxima lección por desarrollar: {{MODULO_Y_SECCION_INICIAL}}.
Referencias iniciales: {{FUENTES_CON_AUTORIA_EDICION_Y_ENLACES}}.
