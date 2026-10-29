# Estructura de la página de un módulo

Acuerdo de presentación educativa: 2026-10-27. Se aplica al índice README de un
módulo y orienta su futura representación en el portal. La referencia aplicada
es [00 — Entorno de aprendizaje](../curriculum/00_getting_started/README.md).
La estructura está aplicada a los índices 00–14. El módulo 12 dispone de sus nueve secciones; 13 dispone de sus diez secciones
con cierre local; 14.01–14.02 tienen material de diseño y estructura; 14.03–14.09 conservan su plan. La tabla distingue
cada estado: aplicar la estructura no desarrolla una lección ni revisa toda la teoría.

## Qué debe resolver esta página

La página de módulo es el punto de orientación entre el curriculum y las
lecciones. Debe permitir decidir dónde empezar, qué preparar, en qué orden
practicar y cómo reconocer que se puede continuar. La teoría y las soluciones
pertenecen a las lecciones/labs; el historial editorial pertenece a PROGRESS.md.

## Cabecera común

- **Identidad:** número y nombre; conservar los identificadores del recorrido.
- **Ubicación:** regreso a Inicio y Curriculum, más el módulo actual.
- **Resumen:** una frase concreta sobre la capacidad que se trabajará.
- **Acciones:** primera lección, lecciones/labs y criterio de salida.

La cabecera ofrece orientación rápida. No necesita repetir todos los requisitos,
objetivos y resultados de las secciones siguientes. No inventar duración total,
porcentaje de progreso o nivel adquirido para llenar una ficha.

## Las ocho secciones, en orden

| Sección | Pregunta que responde | Contenido esperado |
| --- | --- | --- |
| **1 · Propósito** | ¿Para qué me sirve este módulo? | Capacidad y relación con el recorrido, en un párrafo breve |
| **2 · Antes de empezar** | ¿Qué debo saber o tener ahora? | Prerrequisitos con enlaces cuando existan; preparación inicial y opciones claramente separadas |
| **3 · Qué vas a aprender** | ¿Qué podré hacer y explicar? | Tres a cinco acciones observables, sin afirmar que ya se adquirieron |
| **4 · Lecciones y labs** | ¿En qué orden trabajo? | Tabla de lección, lab y resultado comprobable, con enlaces válidos |
| **5 · Cómo trabajar este módulo** | ¿Cómo realizo la práctica? | Leer/predicción, práctica, comprobación y explicación; acompañamiento y decisiones de recorrido específicas |
| **6 · Qué conservar** | ¿Qué evidencia necesito guardar? | Archivos/notas concretos y qué permiten revisar; ubicación personal cuando corresponda |
| **7 · Criterio de salida** | ¿Cómo sé si puedo continuar? | Comprobación de la capacidad global y explicación; estado del proyecto/checkpoint si aplica |
| **8 · Siguiente paso** | ¿Qué abro ahora o después? | Primera lección para empezar; módulo siguiente al cerrar; navegación de regreso |

Los nombres pueden adaptarse si resulta necesario para un módulo, manteniendo
su función y orden. No multiplicar encabezados o tablas si una sección breve
resuelve la pregunta. La estructura es común; el contenido depende del módulo.

## Módulos que todavía son planes

Conservar las mismas ocho preguntas, marcando objetivos, evidencia y criterio
como previstos. La tabla enlaza solo los apartados reales del plan y muestra
los labs como pendientes; la acción inicial invita a consultar el alcance, no
a ejecutar una lección inexistente. No crear carpetas, instalar dependencias o
acreditar aprendizaje para completar la presentación.

## Cómo escribir cada parte

### Propósito frente a objetivos

El propósito explica para qué sirve. Los objetivos describen acciones que se
practicarán. Ejemplo: «Preparar un entorno para estudiar datos» es propósito;
«elegir el kernel y ejecutar un notebook desde cero» es una acción observable.
Evitar objetivos como «dominar Python» o «comprender todo».

### Preparación inicial frente a instalación completa

Indicar qué hace falta al entrar y qué se introducirá después. No exigir que la
persona instale por adelantado todas las herramientas del módulo. Distinguir
necesario, recomendado y opcional; enlazar la preparación específica sin repetirla.

### Tabla de lecciones

Usar pocas columnas para que sea legible en móvil:

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| Número y título enlazado | Lab enlazado | Una acción o resultado concreto |

Esta fila explica el formato; la página real debe contener solo archivos existentes.
Si un material está planificado, marcarlo como tal sin enlace a una lección o lab
inexistente. Señalar partes, prerrequisitos internos y ampliaciones opcionales sin
convertirlas en condiciones obligatorias de avance.

### Desplegable común de alcance

Todos los índices 00–14 incluyen **Ver el alcance de las secciones**, una sola
vez dentro de «Lecciones y labs», después de la tabla y las notas de orden,
y antes de «Cómo trabajar este módulo». Se presenta cerrado por defecto.
Su ancla común es `alcance-de-las-secciones`; conservar además las anclas
anteriores de alcance y de sus apartados.

La tabla permite elegir y navegar; el desplegable aclara qué incluye y qué deja
fuera cada sección. Para contenidos breves, usar dos notas concretas por lección;
para alcances más amplios, conservar sus apartados y referencias sin copiar la
teoría completa ni el historial de desarrollo.

En módulos planificados, la etiqueta del desplegable se conserva para que sea
reconocible. La advertencia de planificación y los labs pendientes permanecen
visibles fuera; dentro se repite que el alcance es previsto. Comprobar que los
enlaces a apartados del plan revelen el contenido cerrado al navegar por ancla.
Si un visor no lo revela, se puede abrir mediante el resumen; no trasladar allí
preparación, actividad obligatoria, evidencia o criterio de salida.

Esta regla se aplicó a los quince índices; la composición específica del portal
no cambia automáticamente por incluir el bloque en los Markdown originales.

### Evidencia frente a criterio de salida

La evidencia es un archivo, salida o explicación conservada. El criterio de
salida establece qué debe demostrar. Tener un notebook guardado no prueba que
pueda ejecutarse desde una sesión limpia ni que la persona explique el resultado.

Mostrar si existe un proyecto/checkpoint implementado. En caso contrario,
indicarlo expresamente; no crear enlaces o porcentajes para simular su existencia.

### Navegación y accesibilidad

Conservar lección ↔ lab y lab → siguiente lección. La página de módulo debe
permitir volver a Curriculum y entrar a la primera lección sin buscar entre
muchos enlaces. No esconder preparación, actividad, evidencia o cierre dentro
de desplegables. Reservarlos para apoyos y ampliaciones voluntarias.

Mantener enlaces relativos, texto descriptivo y anclas estables. Una imagen
puede aclarar una relación, pero no es un requisito decorativo del índice.

## Qué queda fuera de la página

- Bitácora detallada de desarrollo, versiones de paquetes y conteos de pruebas.
- Toda la teoría de las lecciones o las soluciones de los labs.
- Instalaciones copiadas de todos los gestores como si fueran obligatorias.
- Promesas de aprendizaje completado por visitar páginas o descargar archivos.
- Arquitectura interna o especificaciones privadas del sitio.

## Aplicación y revisión

Usar la [plantilla de módulo](../templates/module/README.md) y contrastarla con
la referencia 00. Revisar fuentes y estado real antes de adaptar otro índice.
Comprobar enlaces, fragmentos, orden, opciones, evidencias y criterio de salida;
después revisar la presentación renderizada en escritorio y ventana estrecha.

El portal puede reutilizar este contrato educativo. Cada integración requiere
revisar fuentes, composición, catálogo y enlaces; definir esta estructura no la
implementa automáticamente. El estado operativo del sitio vive en su
[documentación de uso](../portal/README.md), separado de este contrato de contenido.

La [guía Markdown](markdown-study-guide.md) define el estilo general; la
[guía de autoría](authoring-guide.md) mantiene los criterios educativos del track.
