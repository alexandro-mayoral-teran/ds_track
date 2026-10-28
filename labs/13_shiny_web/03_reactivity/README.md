# Lab 13.03 — Modelo de reactividad

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.03**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Predecir invalidación y demanda a partir de las lecturas del código |
| **Entrada** | Copia nueva de 13.03, mínimo número/doble y cuatro ventas de 300/240/0/120 MXN |
| **Evidencia** | Grafos, predicciones, resultados y una variante explicada |

[Lección 13.03](../../../curriculum/13_shiny_web/03_reactivity/README.md) · [Actividad](#actividad) · [Comprobación](#resultado-y-comprobación)

## Relación y preparación

Este lab refuerza [13.03 — Modelo de reactividad](../../../curriculum/13_shiny_web/03_reactivity/README.md).
No hay proyecto ni checkpoint asociado implementado. No exige entregar labs previos.
Sigue [los recorridos](../../../curriculum/13_shiny_web/03_reactivity/recorridos.md)
para preparar una carpeta nueva, restaurar localmente y abrir shiny_1303.Rproj
en tu IDE. Trabaja sobre esa copia; conserva las fuentes del curso.

Necesitas distinguir entrada, render, función corriente y expresión reactiva.
Antes de ejecutar, abre minimo.R y app.R en el editor. Los mensajes de consola
son marcas didácticas, no un orden de ejecución garantizado ni un benchmark.
No hace falta instalar reactlog ni usar las pruebas opcionales para completar el lab.

## Actividad

### 1. Dibujar antes de ejecutar

Dibuja el mínimo con la casilla marcada y después desmarcada. Usa flechas
productor → consumidor. Señala qué lectura de código justifica cada flecha.
Incluye la nota/eco; no conectes objetos solo por aparecer cerca en el archivo.

Inicia minimo.R desde la consola R de tu copia con iniciar_app. Predice y
contrasta en este orden; espera cada salida antes del siguiente cambio:

| Paso | Acción | Salida esperada | ¿Debe ejecutarse el cuerpo de doble? |
| --- | --- | --- | --- |
| 1 | Inicio con número 2, casilla marcada | Completar | Completar |
| 2 | Número 3 | Completar | Completar |
| 3 | Cambiar solo la nota | Completar | Completar |
| 4 | Desmarcar y esperar | Completar | Completar |
| 5 | Número 7, aún desmarcada | Completar | Completar |
| 6 | Volver a marcar | Completar | Completar |
| 7 | Desmarcar/marcar sin cambiar número | Completar | Completar |

Registra marcas nuevas de consola, no todo su historial acumulado. Explica por
qué un resultado invalidado puede esperar sin calcularse hasta el paso 6.
No presupongas un número exacto de mensajes durante la conexión inicial.

### 2. Un texto igual con dependencias distintas

Detén tu servidor. En la copia de minimo.R mueve `valor <- doble()` antes de
la condición que retorna `Consulta desactivada.`. Mantén el resto del código.
Predice qué cambia al desmarcar y modificar número; guarda, reinicia R, carga
iniciar.R y vuelve a iniciar el mínimo.

Comprueba que con número 7 el texto desactivado sigue igual y, sin embargo,
aparece [doble] al cambiar número. Explica la lectura que agrega la conexión.
Restaura el orden original y repite desde una sesión R nueva. Guarda el cambio
o una nota suficiente para reconstruirlo, sin necesitar capturas de cada paso.

### 3. Contrastar la consulta compartida

Detén el mínimo e inicia app.R. Dibuja su grafo con detalle marcado/desmarcado.
Las cuatro ventas son V001: 4×75=300; V002: 2×120=240; V003: 0×50=0;
V004: 3×40=120. Todas suman 660 MXN. Una fila representa una venta.

1. Comprueba el inicio: cuatro filas y resumen 4/660 MXN.
2. Recorre V001, V002, V003 y V004. Contrasta cada campo de la tabla y el resumen.
3. Deja V003 y cambia la nota. ¿Por qué no hace falta otra [consulta]?
4. Desmarca detalle; conserva V003/0 en el resumen. Cambia a V004: ¿por qué aquí
   sí aparece [consulta], aunque la tabla no esté mostrando filas?
5. Recupera detalle y comprueba V004/3/40/120. Explica la reutilización del resultado.
6. Abre otra pestaña y comprueba que inicia con todas/660. La primera conserva
   su elección. Recargar la primera vuelve al inicio definido en UI; no se
   persisten elecciones ni se comparte una cache de consulta entre sesiones.

### 4. Distinguir un efecto de un resultado

Localiza observe en app.R. Predice qué pasa al quitarlo de tu copia, detén el
servidor, comenta solo ese bloque y vuelve a iniciar desde una sesión nueva.
Prueba selección y casilla: las cifras deben conservarse y desaparecen las
marcas [observador]. Restaura el bloque original.

Explica por qué asignar observe a consulta no proporcionaría una tabla que
las salidas pudieran pedir con consulta(). No hace falta introducir ese error
en la app ni manipular archivos desde un observador.

<details>
<summary>Ver una pista sobre las marcas de consola</summary>

Una marca dentro de reactive observa su ejecución, no cada invalidación.
Para justificar la ausencia de [doble], revisa si algún consumidor sigue
leyendo doble(). Para ventas, revisa también el resumen, no solo la tabla.

</details>

## Resultado y comprobación

La app conserva las cuatro ventas y sus importes. Puedes explicar la lectura
que crea cada conexión, invalidación sin demanda, reutilización y la diferencia
entre una salida y un efecto. No basta entregar un grafo que coincida en forma:
justifica al menos un cambio observado y otro que no se propaga.

<details>
<summary>Ver solución razonada</summary>

En el mínimo: 2→4 al inicio, 3→6 al cambiar; la nota solo cambia eco. Al
desmarcar, resultado devuelve el texto sin leer doble. Cambiar a 7 invalida
el doble previo, sin demanda para recalcular. Marcar pide el valor actualizado
y muestra 14. Desmarcar/marcar sin cambiar número reutiliza 14. Con la lectura
antes del if, resultado vuelve a depender de doble incluso en la rama desactivada.

En ventas: todas da 4/660; V001 da 1/300, V002 1/240, V003 1/0 y V004 1/120.
Nota no llega a consulta. La casilla cambia detalle y el observador, no la fuente.
Cambiar venta con tabla desactivada sí recalcula consulta porque el resumen
continúa leyéndola. Recuperar tabla reutiliza la consulta válida. observe solo
escribe un diagnóstico y su retorno no es un valor de datos para las salidas.

El orden entre resumen y detalle no prueba el grafo. Los valores y las lecturas
del código sí permiten explicar las conexiones; las marcas las complementan.

</details>

## Evidencia y reflexión

Conserva en tu copia personal los dos grafos por app, la tabla de predicciones,
al menos tres contrastes de ventas y las variantes justificadas. Anota ayudas,
dudas y el siguiente paso; no registres aprendizaje en PROGRESS.md del curso.
Quien acompaña elige un cambio y pide explicarlo antes de probarlo.

- ¿Por qué cambiar número y cambiar nota tienen efectos distintos?
- ¿Qué diferencia hay entre resultado viejo, resultado invalidado y resultado recalculado?
- ¿Por qué un texto igual en pantalla no garantiza que se hizo el mismo trabajo?
- ¿Qué conserva esta cache y qué ocurre al abrir una sesión nueva?

## Siguiente paso

Haz una pausa. Al retomar, consulta
[13.04 — Filtros e indicadores compartidos](../../../curriculum/13_shiny_web/README.md#04-filtros-e-indicadores-compartidos),
todavía planificado. Esta práctica no completa el proyecto del módulo.

[← Lección 13.03](../../../curriculum/13_shiny_web/03_reactivity/README.md) · [Módulo 13](../../../curriculum/13_shiny_web/README.md)
