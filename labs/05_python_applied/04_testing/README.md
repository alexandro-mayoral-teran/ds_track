# Lab 05.04 — Pruebas de código y datos

## Entrada, propósito y resultado

Completa la [lección 05.04](../../../curriculum/05_python_applied/04_testing/README.md).
Usa el entorno elegido y el paquete compartido de 05.01–05.03. Recibirás
[muestras pequeñas y pruebas](../../../curriculum/05_python_applied/01_notebook_to_modules/pruebas_0504/);
no necesitas instalaciones, notebook, datos privados ni entregas nuevas permanentes.

**Resultado:** colección ejecutada, interpretación de una falla controlada,
un caso nuevo y una explicación que conecte regla, entrada y esperado.
El lab puede dividirse en varias sesiones. No hay proyecto/checkpoint implementado asociado.

## A. Predecir antes de ejecutar — esencial

1. Lee las seis observaciones de muestras.py y la tabla de resultados de la lección.
2. Calcula a mano para octubre: mediana/cobertura de comercio, educación,
   servicios y Todos. Explica por qué el saldo 900 de septiembre no interviene.
3. Escribe qué resultado incorrecto aparecería al excluir cero, rellenar ausencias
   con cero o dividir conocidos entre conocidos.
4. Explica por qué [0, 1] permite comprobar medio peso, pero no distingue media y mediana.

**Comprobación:** cada esperado tiene una cuenta y una base explícita.
**Evidencia:** tabla manual con desconocidos separados de ceros.

<details>
<summary>Ver solución razonada de A</summary>

Comercio: conocidos [0, 1], mediana 0,5, cobertura 2/3 × 100.
Educación: una fila desconocida, mediana no definida y cobertura 0 %.
Servicios: ninguna fila, mediana y cobertura no definidas. Todos: [0, 1, 10],
mediana 1 y cobertura 3/5 × 100 = 60 %. El filtro excluye septiembre.
Si se elimina cero, comercio queda con mediana 1 y pierde un conocido.
Si se imputa cero a su ausencia, la mediana de [0, 1, 0] es 0 y la cobertura
aparenta 100 %. Cambiar el denominador a conocidos también oculta ausencias;
con cero conocidos podría generar división inválida, según cómo se implemente.
Media y mediana de [0, 1] coinciden en 0,5: hace falta otro caso para distinguirlas.

</details>

## B. Ejecutar y leer — esencial

1. Sigue el recorrido completo de tu shell en la lección: comprueba intérprete,
   entra en 01_notebook_to_modules, ejecuta un método y después discover.
2. Registra cantidad de métodos, resultado y código de salida inmediatamente.
3. Busca en los archivos un ejemplo de assertEqual, assertAlmostEqual,
   assertRaises, assert_frame_equal y subTest. Explica qué comprueba cada uno.
4. Relaciona un test_ de cada archivo con la regla que protege.

**Comprobación:** original: 1 prueba individual y 21 en la colección, OK y código 0.
**Evidencia:** comando, directorio de ejecución, intérprete y resumen de resultados.

<details>
<summary>Ver solución razonada de B</summary>

El test de mediana compara 0,5 exactamente y cobertura aproximadamente;
el de fecha imposible exige ValueError. El de entrada conservada compara
valores/tipos/índices con assert_frame_equal; el de fechas usa subTest para
identificar cada variante. El total de veinte conciliaciones pertenece a una
ejecución del análisis, no al número de métodos unittest. Cero tests descubiertos
no satisface la actividad. Los tiempos dependen del equipo.

</details>

## C. Una falla controlada y su corrección — esencial

1. Antes de editar, conserva cualquier trabajo propio de test_transformacion.py.
2. Cambia únicamente el esperado `0.5` por `1.0` en
   test_mediana_con_cero_y_medio_peso. No cambies el cálculo del paquete.
3. Predice el resultado. Ejecuta solo ese método con el comando de la lección.
4. Lee nombre de prueba, archivo/línea y observado/esperado. Registra el código.
5. Restaura tu esperado 0.5; vuelve a ejecutar el método y la colección.
   No uses restauración global de Git: conserva otras ediciones personales.

**Comprobación:** FAIL y código distinto de 0 con esperado incorrecto;
OK y 0 tras restaurar. Las muestras y el paquete no cambian.
**Evidencia:** fragmento de falla, explicación de su causa y corrección.

<details>
<summary>Ver solución razonada de C</summary>

assertEqual compara observado 0.5 con esperado 1.0 y lanza AssertionError;
unittest informa FAIL. El defecto está en la expectativa que acabamos de editar.
La regla manual obliga a restaurar 0.5. Que una prueba falle demuestra que
ejecutamos esa comprobación, pero esta actividad por sí sola no demuestra
que detecte todos los cambios incorrectos de la implementación.

</details>

## D. Agregar un caso que distinga mediana de promedio — práctica

1. En la clase PruebasResumen de test_transformacion.py agrega
   un método test_mediana_no_es_promedio con la misma indentación que los demás.
2. Prepara una copia de las primeras tres filas de self.detail; conserva fecha
   y segmento comercio, y asigna saldos [0, 0, 100].
3. Calcula a mano mediana, conocidos y cobertura. Ejecuta summarize y compruébalos.
4. Ejecuta el método nuevo y después la colección. Debe descubrir 22 métodos.
5. Explica qué error detecta este caso y por qué no bastaba [0, 1].

**Comprobación:** mediana 0, tres conocidos, cobertura 100 %, sin cambiar self.detail.
**Evidencia:** método propio, salida y justificación; no basta copiar la solución sin explicarla.

<details>
<summary>Ver una solución razonada de D</summary>

Agregar dentro de la clase existente:

```python
    def test_mediana_no_es_promedio(self):
        detail = self.detail.iloc[:3].copy(deep=True)
        detail["saldo_mxn"] = pd.Series([0, 0, 100], index=detail.index, dtype="Int64")
        _, summary = summarize(detail, CUT)
        row = summary.set_index("segmento").loc["comercio"]
        self.assertEqual(row["mediana_mxn"], 0)
        self.assertEqual(row["conocidos"], 3)
        self.assertEqual(row["cobertura_pct"], 100)
```

pd, summarize y CUT ya están importados en ese archivo. La lista ordenada
[0, 0, 100] tiene centro 0 y promedio 100/3; sustituir mediana por promedio
rompería esta prueba. El caso original de dos conocidos tenía ambos valores iguales.
No se agrega este ejercicio resuelto a la colección inicial: el método es tu evidencia.

</details>

## E. Datos nuevos y conservación ante fallas — práctica

1. Lee test_credito_repetido_no_multiplica_union. Identifica qué CSV se modifica
   en el temporal y qué excepción se espera. ¿Por qué no aceptar filas multiplicadas?
2. Lee test_falla_antes_de_replace_conserva_bytes_y_causa. Explica qué protege
   comparar bytes, comprobar la causa y revisar los archivos restantes.
3. Lee test_fallas_por_etapa_no_publican_cierre y completa una tabla con
   entrega.json, ejecucion.json y cierre.json para cada etapa.
4. Explica por qué una suite verde hoy no autoriza quitar las validaciones
   del lector cuando mañana se procese otro CSV.

**Comprobación:** puedes identificar entrada, llamada real, esperado y limpieza
sin depender del orden de los métodos ni de archivos personales.
**Evidencia:** tabla de etapas y una explicación de los límites de la suite.

<details>
<summary>Ver solución razonada de E</summary>

Crédito repetido viola unicidad y se rechaza antes de que multiplique la unión.
El JSON anterior debe seguir idéntico: no basta con que exista algún archivo.
La causa conserva información del error original; la carpeta no debe retener
temporales en la falla simulada.

| Simulación | entrega.json | ejecucion.json | cierre.json |
| --- | --- | --- | --- |
| after-export | Sí | No | No |
| record | Sí | No | No |
| before-close | Sí | Sí | No |

Los temporales se eliminan después de cada caso: conserva la evidencia escrita,
no dependas de inspeccionarlos más tarde. read_detail valida los CSV realmente
recibidos en cada ejecución. La suite cubre ejemplos elegidos; revisión visual,
validez de otras entradas e interpretación siguen teniendo responsables.

</details>

## Extensión opcional

Desde 01_notebook_to_modules, ejecuta los módulos de recursos y transformación
en el orden inverso usando `python -m unittest -v pruebas_0504.test_recursos pruebas_0504.test_transformacion`.
Usa el mecanismo de código de salida de tu shell ya explicado. Deben pasar
independientemente. Propón otro caso para una clave textual con ceros iniciales
o un corte válido vacío; explica qué regresión descubriría antes de programarlo.

## Reflexión, evidencia y continuidad

- ¿Cómo elegiste el esperado y quién podría equivocarse al calcularlo?
- ¿Qué diferencia hay entre FAIL y ERROR? ¿Puede estar equivocada la prueba?
- ¿Por qué desconocido y sin registros exigen expectativas distintas?
- ¿Qué comprueba una reconstrucción y qué sigue requiriendo revisión visual?
- ¿Por qué no debe depender la aceptación de datos de una sentencia assert?

Registra cuentas manuales, comandos, falla/corrección, método nuevo y dudas
en PROGRESS.md sin cambiar el estado de aprendizaje por la mera disponibilidad
del material. Avanza cuando puedas explicar esas evidencias con tus palabras.

Continúa con el [plan 05.05 — Tipos y contratos](../../../curriculum/05_python_applied/README.md#05-tipos-y-contratos-de-funciones),
todavía pendiente. Volver a la [lección 05.04](../../../curriculum/05_python_applied/04_testing/README.md).
