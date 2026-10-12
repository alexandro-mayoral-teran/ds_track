# Lab 02.10 — Reconstruir un análisis y explicar la figura

## Relación, entrada y resultado

- Lección: [Análisis y primera gráfica](../../../curriculum/02_pandas/10_analysis_plot/README.md).
- Entrada: muestra de 02.06, analysis.py y first_analysis.ipynb de 02.10.
- Resultado: notebook ejecutable, resumen comprobado, figura y explicación propia.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 80 a 120 minutos o dos sesiones. Usa el entorno con pandas, Matplotlib
y un kernel preparado. Conserva la fuente; trabaja sobre copias al proponer cambios.

## Parte A — Ejecutar desde cero

1. Ejecuta el script con el corte inicial y registra versiones.
2. Abre el notebook, selecciona el mismo entorno, reinicia kernel y ejecuta todo.
3. Comprueba partición, créditos del corte y saldo total.
4. Compara las tablas y la figura de ambas ejecuciones.

<details>
<summary>Ver comprobaciones de la parte A</summary>

La entrada tiene 48 registros, 36 aceptados y 12 rechazados entre los dos cortes.
Octubre tiene 18 créditos aceptados y saldo 41500. El resumen: servicios 12600,
consumo 11700, educacion 8800 y comercio 8400; conteos 5, 5, 4 y 4.
Script y notebook comparten funciones y producen el mismo resumen. La partición
conserva todos los registros; los rechazos no se eliminan del material de revisión.

</details>

## Parte B — Explicar la gráfica

1. Escribe una pregunta que la figura realmente responda.
2. Identifica la barra mayor, su importe, su conteo y participación.
3. Escribe dos afirmaciones que no puedas concluir con esta figura.
4. Comprueba que todas las longitudes y etiquetas coincidan con resumen.

<details>
<summary>Ver una explicación posible</summary>

“Entre los registros aceptados del corte de octubre, servicios concentra el mayor
saldo: 12600 MXN en cinco créditos, equivalente al 30.36 % de los 41500 MXN aceptados.
La gráfica excluye los rechazos y no explica por qué ese importe es mayor.”
No demuestra mayor riesgo ni crecimiento del segmento. Tampoco representa saldo
promedio: muestra un total, con su propia unidad y denominador.

</details>

## Parte C — Cambiar el corte y repetir

1. Cambia corte a 2026-09-30 en el notebook.
2. Reinicia y ejecuta todas las celdas.
3. Predice y comprueba créditos, saldo y segmento mayor.
4. Explica por qué no atribuyes el cambio entre cortes a una causa sin revisar poblaciones.

<details>
<summary>Ver comprobaciones de la parte C</summary>

Septiembre tiene 18 créditos aceptados y saldo **39900 MXN**. Educación es el
máximo con **12200 MXN** en cinco créditos (30.58 %). Los demás son comercio
10500, consumo 9200 y servicios 8000. Comprueba el detalle; no reutilices el
título ni la nota de octubre. La igualdad de conteos no demuestra igualdad de IDs:
las reglas apartaron registros diferentes. Primero se necesitaría una comparación
por ID, como en 02.08, antes de interpretar el cambio de los mismos créditos.

</details>

## Parte D — Una corrección cambia la base aceptada

1. Desde la fuente original, en una copia corrige fecha_corte del registro 14
   a 2026-09-30, como en el lab 02.06.
2. Usa limpiar_y_separar y resumir_corte sobre esa copia para septiembre.
3. Comprueba conteos y saldo antes/después; genera otra figura en output/practica.
4. Explica la diferencia entre corregir con evidencia y cambiar datos para obtener un resultado.

<details>
<summary>Ver solución de la parte D</summary>

```python
otra = fuente.copy()
otra.loc[otra.index[13], "fecha_corte"] = "2026-09-30"
aceptados2, rechazados2 = limpiar_y_separar(otra)
seleccion2, resumen2 = resumir_corte(aceptados2, "2026-09-30")
```

Hay 37 aceptados/11 rechazados entre ambos cortes y 19 créditos aceptados en
septiembre. Su saldo pasa de 39900 a **42300** por el registro de 2400 MXN.
La fuente versionada conserva la fecha imposible. En datos reales se necesitaría
evidencia para afirmar cuál era la fecha correcta.

</details>

## Parte E — Un corte sin observaciones

1. Cambia corte a 2026-12-31 y ejecuta desde cero.
2. Comprueba resumen, figura y texto del hallazgo.
3. Vuelve al corte inicial, reinicia y repite para no entregar resultados de diciembre
   con una explicación de octubre.

<details>
<summary>Ver solución de la parte E</summary>

No hay registros aceptados de diciembre. El resumen conserva columnas y cero
filas. La figura muestra ausencia de observaciones; el hallazgo no inventa un
segmento mayor ni un saldo cero observado. Los CSV tienen encabezados y el proceso
conserva los aceptados y rechazos de la entrada completa.

</details>

## Evidencia de cierre

- Conserva el notebook con tu pregunta e interpretación; debe ejecutarse desde un
  kernel limpio. Limpia salidas que contengan rutas personales antes de compartir.
- Registra origen, corte, reglas, versiones y conteos de entrada/aceptados/rechazos.
- Comprueba resumen y figura; explica qué queda fuera y qué preguntas siguen abiertas.
- Revisa Git antes de registrar código/notas. output está ignorado; publicar tus
  resultados no es requisito para completar este cierre.

El módulo dispone de diez lecciones y labs. Marca el aprendizaje como completado
solo cuando tengas esta evidencia y hayas cubierto los criterios de las prácticas
previas; desarrollar el material no acredita tus ejercicios.

Continúa con [03 — SQL y bases de datos](../../../curriculum/03_sql_databases/README.md),
con plan definido y lecciones pendientes de implementación.
