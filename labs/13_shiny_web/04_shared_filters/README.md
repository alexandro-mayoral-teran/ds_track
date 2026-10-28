# Lab 13.04 — Filtros e indicadores compartidos

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.04**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Conciliar tabla y medidas desde una selección común |
| **Entrada** | Copia independiente con seis observaciones, tres créditos y dos cortes |
| **Evidencia** | Predicciones por clave, cifras, grafo y una regla modificada con justificación |

[Lección 13.04](../../../curriculum/13_shiny_web/04_shared_filters/README.md) · [Actividad](#actividad) · [Comprobación](#resultado-y-comprobación)

## Relación y preparación

Practica [13.04 — Filtros e indicadores compartidos](../../../curriculum/13_shiny_web/04_shared_filters/README.md).
No hay proyecto/checkpoint implementado ni entregas previas obligatorias. Sigue
[preparación y arranque](../../../curriculum/13_shiny_web/04_shared_filters/recorridos.md)
desde tu IDE, en una carpeta nueva. Usa la copia y conserva las fuentes del curso.

cartera.csv contiene 001/comercio/0, 002/servicios/2000 y 003/comercio/2500 en
septiembre; en octubre los mismos IDs/segmentos con saldos 100/1900/2600 MXN.
La clave es ID/corte, cada saldo corresponde a una fecha y todos son conocidos.
El denominador de cobertura es siempre la cantidad de créditos del corte antes
de segmento/mínimo. No se suman ambos cortes para llamar al resultado saldo de cartera.

## Actividad

### 1. Predecir con el mínimo

Abre minimo.R en la copia. Antes de ejecutarlo, anota qué IDs, conteo y suma
esperas con mínimos 2000, 2001, 0 y 2501. Inícialo con iniciar_app desde la
consola R, comprueba tabla/texto y explica por qué 2000 se incluye.

Detén tu servidor. No necesitas capturas de cada paso; conserva una tabla breve
con predicción, resultado y explicación de una diferencia si la hubo.

### 2. Conciliar la app completa

Inicia app.R. Para cada caso predice primero los IDs, cantidad, saldo y
porcentaje. Luego compara las cuatro columnas de las filas con el CSV y completa:

| Corte | Segmentos | Mínimo MXN | IDs | Cantidad | Saldo MXN | Cobertura sobre el corte |
| --- | --- | --- | --- | --- | --- | --- |
| Septiembre | Ambos | 2000 | Completar | Completar | Completar | Completar |
| Octubre | Ambos | 2000 | Completar | Completar | Completar | Completar |
| Septiembre | Comercio | 0 | Completar | Completar | Completar | Completar |
| Septiembre | Comercio | 1 | Completar | Completar | Completar | Completar |
| Octubre | Servicios | 1900 | Completar | Completar | Completar | Completar |
| Octubre | Servicios | 1901 | Completar | Completar | Completar | Completar |
| Septiembre | Ninguno | 0 | Completar | Completar | Completar | Completar |

Deja que cada cambio termine antes del siguiente. Revisa que el texto de
contexto refleje lo que consultaste. Recupera ambos segmentos después del caso
sin casillas: la selección debe recuperarse, sin reiniciar R ni recargar el CSV.

### 3. Revisar dependencias

Dibuja corte → universo → selección → tabla/indicadores, añade segmentos,
mínimo y denominador. Para cada flecha identifica la lectura en app.R.

Con octubre/ambos/2000, desmarca Mostrar tabla. Cambia mínimo a 0: el resumen
debe pasar a 3/4600 y la cobertura a 100%, aunque la tabla siga sin mostrarse.
Vuelve a marcar y comprueba 001/100, 002/1900 y 003/2600, todos del mismo corte.
Explica por qué ocultar la tabla no altera los indicadores ni el denominador.

Abre otra pestaña: inicia con septiembre/ambos/2000, mientras la primera conserva
su consulta. Recargar la primera recupera los valores iniciales de UI; aquí no
se persisten filtros ni se sincronizan elecciones entre sesiones.

### 4. Una variante que modifica la regla completa

En tu copia, detén el servidor y cambia en cartera.R la comparación de selección
`>= minimo_mxn` por `> minimo_mxn`. Actualiza también la etiqueta y el texto de
contexto de app.R para indicar mínimo exclusivo (`>`): la regla visible debe
coincidir con el cálculo. No cambies el CSV ni introduzcas filtros en cada render.
Guarda, reinicia R y vuelve a iniciar la app.

Predice y comprueba septiembre/ambos/2000 y octubre/servicios/1900. Revisa que
tabla, cantidad, saldo y cobertura cambien juntos y conserva una explicación
del efecto de frontera. Restaura la regla inclusiva y sus etiquetas, guarda y
repite el inicio desde una sesión R nueva.

**Ampliación opcional:** explica por qué usar nrow(seleccion()) como denominador
daría 100% para cualquier selección no vacía y 0/0 al vaciar. No hace falta
romper la app para demostrarlo: usa el caso inicial en una cuenta escrita.

<details>
<summary>Ver una pista para el porcentaje</summary>

El numerador son filas de la selección. El denominador de esta pregunta son
los tres créditos del corte, incluso si has elegido solo un segmento. No son
las seis observaciones ni la cantidad seleccionada. El saldo no es el numerador
del porcentaje de créditos.

</details>

## Resultado y comprobación

Puedes reconstruir filas y medidas desde el CSV, explicar el cero y el vacío,
y señalar dónde se comparte la selección. El umbral y contexto visible deben
coincidir. La prueba opcional de autoría no sustituye esa explicación ni la
revisión de controles en navegador.

<details>
<summary>Ver solución razonada</summary>

El mínimo da 002/003, 2/4500 con 2000; solo 003, 1/2500 con 2001;
001/002/003, 3/4500 con 0; vacío, 0/0 con 2501.

En la app completa: septiembre/ambos/2000 da 002/003, 2/4500/66.67%;
octubre/ambos/2000 da 003, 1/2600/33.33%. Septiembre/comercio con mínimo 0
da 001/003, 2/2500/66.67%, y con 1 da 003, 1/2500/33.33%: el saldo coincide,
las filas no. Octubre/servicios con 1900 da 002, 1/1900/33.33%; con 1901 queda
vacío, 0/0/0%. Ningún segmento también da vacío y 0%, sobre un universo de tres.

En la variante exclusiva, septiembre/ambos/2000 da solo 003, 1/2500/33.33%;
octubre/servicios/1900 queda vacío, 0/0/0%. Cambiar el helper común afecta
todas las salidas. Usar una selección como su propio denominador deformaría
la pregunta y ocultaría su cobertura real.

</details>

## Evidencia y reflexión

Conserva en tu copia personal las predicciones/filas, el grafo y la variante
con su regla visible. Anota ayudas, dudas y siguiente paso fuera de PROGRESS.md.
Quien acompaña propone un umbral distinto y revisa la explicación antes de probarlo.

- ¿Por qué 4500 MXN de 4500 no implica que seleccionaste todos los créditos?
- ¿Qué comprobación detecta una fila cero perdida cuando la suma no cambia?
- ¿En qué se distinguen cero seleccionados y una fecha sin universo?
- ¿Qué ocurriría si la tabla leyera el corte y el indicador sumara toda la fuente?

## Siguiente paso

Continúa con [13.05 — Eventos y estado de sesión](../../../curriculum/13_shiny_web/05_events_session/README.md),
ya disponible. No hay formulario, botón de aplicar ni proyecto completado por este lab.

[← Lección 13.04](../../../curriculum/13_shiny_web/04_shared_filters/README.md) · [Módulo 13](../../../curriculum/13_shiny_web/README.md)
