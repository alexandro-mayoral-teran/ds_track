# Shiny: cierre y reanudación

Las diez secciones de [13 — Shiny](../curriculum/13_shiny_web/README.md) tienen
lecciones y labs. [13.10 — Cierre y entrega local](../curriculum/13_shiny_web/10_local_delivery/README.md)
añade una entrega reconstruible y verificación con referencia externa. Esto no
acredita práctica del estudiante ni completa proyectos/checkpoints.

## Decisiones del cierre

- App y módulo de 13.08 conservados, con pruebas de 13.09; dos instancias
  independientes dentro de cada sesión y fuente compartida validada al aplicar.
- Muestra sintética de seis observaciones, clave crédito/corte; tres créditos
  por fecha y 4500/4600 MXN. Reglas y seis preguntas autocontenidas en la entrega.
- Preparador de 24 fuentes, constructor de destino nuevo y verificador R base
  de solo lectura. Entrega base de 41 archivos, sin biblioteca instalada ni caché.
- Seis casos incluyen cero, frontera, vacío y corte sin universo; cinco selecciones
  y cinco contextos CSV, cuatro PNG, resumen y nota de generación. Los archivos
  generados en lote no son descargas de una sesión web anterior.
- Contraste por clave/campo contra CSV externo, inventario y huellas MD5.
  Huellas sin autenticidad; revisión del gráfico y demostración siguen necesarias.
- Lockfile de 13.07 conservado: 42 registros, Shiny 1.14.0, ggplot2 4.0.3 y
  renv 1.3.1; R 4.6.1 de referencia. Sin paquetes nuevos o cambios globales.
- IDE/consola R como recorrido principal; terminal opcional. No atribuir las
  comprobaciones con Rscript/navegador a una operación completa del IDE.

## Práctica y evidencia pendientes

Revisar la entrega con otra persona, restaurar en otra carpeta, repetir pruebas,
recalcular resultados y demostrar UI/descargas reales. Registrar predicción,
comprobación, explicación, ayudas, dudas y siguiente paso en la copia personal.
PROGRESS.md es bitácora del material; no un porcentaje de aprendizaje.

La verificación no ejecuta el código recibido, por lo que no certifica toda su
lógica. La referencia y el verificador deben ser revisados e independientes de
una copia alterada. La nota de generación no autentica ejecuciones pasadas.
El lockfile tampoco incluye R, sistema, navegador o disponibilidad futura de paquetes.

## Qué sigue

[14 — Proyectos reproducibles](../curriculum/14_reproducible_projects/README.md)
dispone de [14.01 — Pregunta y contrato](../curriculum/14_reproducible_projects/01_product_question_contract/README.md);
[14.02 — Estructura y configuración](../curriculum/14_reproducible_projects/02_structure_configuration/README.md), [14.03 — Entornos](../curriculum/14_reproducible_projects/03_reconstructible_environments/README.md), [14.04 — Pipeline](../curriculum/14_reproducible_projects/04_pipeline_reprocessing/README.md), [14.05 — Pruebas](../curriculum/14_reproducible_projects/05_tests_data_quality/README.md), [14.06 — Trazabilidad](../curriculum/14_reproducible_projects/06_traceability_recovery/README.md) y [14.07 — Integración](../curriculum/14_reproducible_projects/07_report_app_integration/README.md) están disponibles; 14.08–14.09 siguen planificadas. 06_shiny_portfolio_app y sus checkpoints figuran en
[proyectos](../projects/README.md), sin implementación asociada. Elegir una app
(Shiny o Streamlit) es suficiente; no se exige completar ambas alternativas.

El portal mantiene su cobertura propia: disponer de material en el repositorio
no implica que esté integrado o publicado como sitio. No se amplía esa cobertura
con este cierre. Despliegue, autenticación y persistencia son extensiones.
