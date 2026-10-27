# Plantilla de lección

Base para crear o adaptar una lección de DS Track. Consulta la
[estructura propuesta y su evaluación](../../docs/lesson-page-guide.md) y la
[guía de autoría](../../docs/authoring-guide.md). La
[lección 00.01](../../curriculum/00_getting_started/01_github_profile/README.md)
es la primera prueba aplicada, con material de apoyo enlazado también donde se usa.

Copia el bloque y sustituye todos los campos CAMPO/RUTA. Sus rutas son
marcadores, no archivos existentes. Ajusta el desarrollo al tema, elimina las
notas de autoría y comprueba enlaces antes de publicar. Conserva los apartados
comunes; si uno es breve, basta una frase concreta. Para páginas que organizan
varias partes, aplica la variante descrita en la guía.

````markdown
# NN.LL — CAMPO_NOMBRE_DE_LA_LECCION

[Inicio](RUTA_INICIO) / [Módulo NN](RUTA_MODULO) / **Lección NN.LL**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | CAMPO_CAPACIDAD_EN_UNA_FRASE |
| **Necesitas** | CAMPO_PREPARACION_BREVE |
| **Evidencia** | CAMPO_PRODUCTO_Y_EXPLICACION |

[Empezar](#antes-de-empezar) · [Ir al lab](RUTA_LAB) · [Comprobar](#evidencia-y-criterio-de-salida)

<!-- Si corresponde: alcance opcional y enlace para continuar sin esta ampliación. -->

## Propósito

CAMPO_PROBLEMA_QUE_RESUELVE_Y_CONEXION_CON_EL_RECORRIDO

## Antes de empezar

- CAMPO_CONCEPTO_PREVIO_CON_ENLACE
- CAMPO_HERRAMIENTAS_Y_PREPARACION_O_INDICAR_QUE_NO_HAY_INSTALACION
- CAMPO_ARCHIVOS_NECESARIOS_Y_DONDE_TRABAJAR

<!-- Separar preparación de entorno y entregas previas realmente necesarias.
Indicar qué recorrido elegir si hay alternativas. No exigirlos todos. -->

## Qué vas a aprender

- CAMPO_ACCION_OBSERVABLE_1
- CAMPO_ACCION_OBSERVABLE_2
- CAMPO_ACCION_OBSERVABLE_3_SI_APLICA

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [CAMPO_ARCHIVO_EXISTENTE](RUTA_RECURSO) | CAMPO_PROPOSITO_CONCRETO | CAMPO_NECESARIO_PARA_ACTIVIDAD_O_CONSULTA_OPCIONAL |

<!-- Incluir solo recursos útiles y existentes: notebook, script, datos,
diccionario, plantilla o guía. No exigir todos los formatos. Enlazar de nuevo
justo antes de usarlos, explicando qué abrir y qué observar. Si no hay apoyos
adicionales, omitir este apartado. Referencias conserva las fuentes teóricas. -->

## 1. CAMPO_PRIMER_CONCEPTO_O_PROBLEMA

CAMPO_CONTEXTO_Y_EXPLICACION_ANTES_DE_LA_SINTAXIS

<!-- Cuando se use un archivo: "Abre [NOMBRE](RUTA_RECURSO) para OBJETIVO;
CAMPO_PREPARACION_Y_QUE_OBSERVAR". No dejar este comentario en la lección final. -->

CAMPO_EJEMPLO_PEQUENO_COMPLETO_TEXTO_CODIGO_TABLA_O_CARPETAS

**Qué deberías observar:** CAMPO_RESULTADO_ESPERADO_Y_SU_INTERPRETACION.

**Compruébalo:** CAMPO_COMPROBACION_SENCILLA_Y_QUE_DETECTA.

## 2. CAMPO_SIGUIENTE_CONCEPTO_O_RECORRIDO

CAMPO_EXPLICACION_EJEMPLO_RESULTADO_Y_COMPROBACION

<!-- Repetir o reorganizar bloques según la actividad. Cuando haya datos,
explicar origen, unidad, campos y reglas antes de operar. En varios shells o
motores dar recorridos completos separados. En R priorizar el IDE y sesión
nueva; en notebooks comprobar kernel, reinicio y ejecución completa. -->

**Prueba un cambio:** CAMPO_VARIACION_PEQUENA_Y_PREGUNTA_DE_PREDICCION.

<!-- Si ayuda, incluir una pista opcional; eliminarla si no hace falta. -->
<details>
<summary>Ver una pista</summary>

CAMPO_PISTA_RAZONADA

</details>

<!-- Añadir errores habituales cerca del concepto si son útiles. Las
ampliaciones se marcan al empezar; no esconden pasos esenciales. -->

## Práctica

Realiza el [lab NN.LL — CAMPO_NOMBRE](RUTA_LAB) para
CAMPO_TAREA_CENTRAL_SIN_REPETIR_TODA_LA_CONSIGNA.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| CAMPO_PRODUCTO_O_NOTA | CAMPO_RESULTADO_O_COMPORTAMIENTO | CAMPO_DECISION_Y_RAZON |
| CAMPO_EVIDENCIA_ADICIONAL_SI_APLICA | CAMPO_VARIACION_O_CASO_LIMITE | CAMPO_QUE_DEMUESTRA_Y_QUE_NO |

CAMPO_CRITERIO_CONCRETO_PARA_CONTINUAR_VINCULADO_A_LOS_OBJETIVOS

Quien aprende realiza la práctica y explica el resultado; su compañero revisa
una comprobación y plantea una pregunta o variación. Guarda evidencia y dudas
en tu copia o bitácora personal.

CAMPO_PROYECTO_CHECKPOINT_EXISTENTE_O_INDICAR_QUE_NO_HAY_ASOCIADO

## Referencias

- [CAMPO_FUENTE_PRIMARIA_O_LIBRO_ABIERTO](RUTA_FUENTE)

CAMPO_ATRIBUCIONES_VERSIONES_Y_LIMITES_PERTINENTES

## Siguiente paso

Después del lab y su comprobación, continúa con
[CAMPO_SIGUIENTE_LECCION_DISPONIBLE](RUTA_SIGUIENTE).

[Volver al módulo NN](RUTA_MODULO) · [Lab NN.LL](RUTA_LAB) · [Siguiente →](RUTA_SIGUIENTE)
````

No rellenes apartados con instalaciones, diagramas, datos o proyectos inventados.
En una lección opcional, identifica la continuación esencial. Al cerrar un
módulo puedes enlazar el índice siguiente si necesita elegirse una ruta; no
presentes planes como lecciones disponibles. Conserva anclas anteriores al
adaptar material existente y verifica también los enlaces desde el lab.
