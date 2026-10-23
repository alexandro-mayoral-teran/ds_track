# Lab 10.01 — Definir y comprobar la misma pregunta

## Propósito y entradas

Practicar [10.01 — Pregunta, contrato y referencia](../../../curriculum/10_polars_duckdb/01_question_contract_reference/README.md).
Solo necesita Python estándar; R base es una comprobación opcional. No requiere
Polars, DuckDB, entregas anteriores ni objetos de otra sesión.

Entrada nueva incluida en el capítulo:

| id_credito | fecha_corte | saldo_mxn |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Cada fila es un saldo en pesos de un crédito en un corte. Clave ID/fecha;
ID textual de tres dígitos, fecha válida 1900–2100, saldo entero no negativo
dentro de int32 y sin ausencias. No modifiques la muestra original.

## Actividad 1 — Escribir la especificación

Antes del código, guarda un documento propio con estas decisiones:

1. Pregunta de negocio, unidad de fila y población.
2. Fuente, columnas, tipos, unidades, clave y política de errores.
3. Corte/umbral, predicado y columnas de salida.
4. Pares ID/importe esperados, conteo y suma.
5. Tratamiento de orden y selección vacía.
6. Qué fase tendría que ejecutar una comparación de rendimiento posterior.

Resuelve manualmente estas consultas y después comprueba cada par:

| Corte | Mínimo MXN | Pares esperados | Conteo | Suma MXN |
| --- | ---: | --- | ---: | ---: |
| 2026-10-31 | 2000 | 003/2600 | 1 | 2600 |
| 2026-09-30 | 2000 | 002/2000, 003/2500 | 2 | 4500 |
| 2026-09-30 | 2001 | 003/2500 | 1 | 2500 |
| 2026-10-31 | 0 | 001/100, 002/1900, 003/2600 | 3 | 4600 |
| 2026-11-30 | 0 | Sin filas | 0 | 0 en la selección |

## Actividad 2 — Ejecutar la referencia

Desde la raíz de DS Track en tu IDE, con el intérprete Python elegido:

1. Carga `referencia.py` como indica la lección y ejecuta las cinco consultas.
2. Verifica pares, conteos, sumas y parámetros; la frontera 2000/2001 importa.
3. Reinicia la sesión y ejecuta el script completo sin datos en memoria previa.
4. Si quieres otro contraste, repite con R base desde la raíz del repositorio.

<details>
<summary>Una solución razonada: referencia y fronteras</summary>

**Python**:

```python
from pathlib import Path
from datetime import date
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/01_question_contract_reference").resolve()))
import referencia as curso

casos = [
    (date(2026, 10, 31), 2000, [("003", 2600)]),
    (date(2026, 9, 30), 2000, [("002", 2000), ("003", 2500)]),
    (date(2026, 9, 30), 2001, [("003", 2500)]),
    (date(2026, 10, 31), 0, [("001", 100), ("002", 1900), ("003", 2600)]),
    (date(2026, 11, 30), 0, []),
]
for corte, minimo, pares in casos:
    resultado = curso.construir_referencia(corte=corte, minimo=minimo)
    esperada = [{"id_credito": id_, "saldo_mxn": saldo} for id_, saldo in pares]
    assert resultado["seleccion"] == esperada
    control = curso.comprobar_seleccion(esperada, corte=corte, minimo=minimo)
    assert control == {"corte": corte.isoformat(), "minimo_mxn": minimo,
        "registros": len(pares), "saldo_mxn": sum(saldo for _, saldo in pares)}
    print(resultado)
```

**R base, opcional**, desde la raíz de DS Track, en Console del IDE:

```r
source("curriculum/10_polars_duckdb/01_question_contract_reference/referencia.R", encoding = "UTF-8")
cortes <- as.Date(c("2026-10-31", "2026-09-30", "2026-09-30", "2026-10-31", "2026-11-30"))
minimos <- c(2000L, 2000L, 2001L, 0L, 0L)
ids <- list("003", c("002", "003"), "003", c("001", "002", "003"), character())
saldos <- list(2600L, c(2000L, 2500L), 2500L, c(100L, 1900L, 2600L), integer())
for (i in seq_along(cortes)) {
  resultado <- construir_referencia_r(corte = cortes[i], minimo = minimos[i])
  esperada <- data.frame(id_credito = ids[[i]], saldo_mxn = saldos[[i]])
  stopifnot(identical(resultado$seleccion, esperada))
  control <- comprobar_seleccion_r(esperada, corte = cortes[i], minimo = minimos[i])
  stopifnot(control$registros == length(ids[[i]]),
    control$saldo_mxn == sum(as.double(saldos[[i]])))
  print(control)
}
```

En septiembre, `2000` entra con `>= 2000`, pero sale con `>= 2001`.
La consulta vacía de noviembre no afirma saldo real cero del corte completo.
La lista vacía Python no demuestra esquema; al usar un motor después también
habrá que inspeccionar las columnas de su resultado vacío.

</details>

## Actividad 3 — Un resultado que engaña al total

Para septiembre ≥ 2000, compara estas dos salidas con la referencia:

- `002/2000` y `003/2500`, en orden inverso: debe aceptarse.
- `002/2100` y `003/2400`: debe rechazarse, aunque haya dos filas y 4500 MXN.

Añade un caso con el mismo ID/importe repetido y otro con un ID cambiado.
No deduzcas equivalencia solo de una suma, ni arregles los datos para pasar.

<details>
<summary>Una solución razonada: aceptar reordenación y rechazar cambios</summary>

**Python**, con el módulo ya importado:

```python
corte = date(2026, 9, 30)
correcta_invertida = [
    {"id_credito": "003", "saldo_mxn": 2500},
    {"id_credito": "002", "saldo_mxn": 2000},
]
print(curso.comprobar_seleccion(correcta_invertida, corte=corte))
incorrectas = [
    [{"id_credito": "002", "saldo_mxn": 2100}, {"id_credito": "003", "saldo_mxn": 2400}],
    [{"id_credito": "002", "saldo_mxn": 2000}, {"id_credito": "002", "saldo_mxn": 2000}],
    [{"id_credito": "001", "saldo_mxn": 2000}, {"id_credito": "003", "saldo_mxn": 2500}],
]
for observada in incorrectas:
    try:
        curso.comprobar_seleccion(observada, corte=corte)
    except ValueError as error:
        print(error)
    else:
        raise AssertionError("Se acepto una seleccion incorrecta")
```

**R base, opcional**:

```r
corte <- as.Date("2026-09-30")
correcta <- data.frame(id_credito = c("003", "002"), saldo_mxn = c(2500L, 2000L))
print(comprobar_seleccion_r(correcta, corte = corte))
incorrectas <- list(
  data.frame(id_credito = c("002", "003"), saldo_mxn = c(2100L, 2400L)),
  data.frame(id_credito = c("002", "002"), saldo_mxn = c(2000L, 2000L)),
  data.frame(id_credito = c("001", "003"), saldo_mxn = c(2000L, 2500L)))
for (observada in incorrectas) {
  error <- tryCatch({comprobar_seleccion_r(observada, corte = corte); NULL}, error = function(e) e)
  stopifnot(inherits(error, "error"))
  print(conditionMessage(error))
}
```

El error compensado tiene conteo y suma correctos, pero cambia el importe
de cada crédito. La comparación ordena por clave para emparejar; no elimina
duplicados. La corrección se basa en las reglas y en la referencia independiente.

</details>

## Ampliaciones opcionales

- Ejecuta la referencia sobre el CSV de 28 filas presentado de nuevo en la
  sección 7 de la lección: nueve seleccionadas/24 100 MXN en octubre ≥ 2000.
- Genera 40 y 400 filas con el código completo de la sección 8, siempre en
  archivos nuevos. Construye su referencia y conserva parámetros/fórmula.
  Cada motor futuro deberá usar el mismo archivo en cada escala.
- Desde R puedes leer esos CSV recién generados con `construir_referencia_r(ruta)`;
  no necesitan Parquet ni bibliotecas externas. No midas velocidad entre
  lenguajes a partir de estos resultados: aquí se comprueba la respuesta.

## Evidencia y reflexión

Conserva especificación, script ejecutable, resultados comprobados y rechazos
esperados; anota dudas y qué repetiste tras reiniciar. No publiques tus salidas
de práctica en el repositorio del curso. Explica:

- ¿Qué diferencia hay entre una fila, un crédito y un crédito en un corte?
- ¿Por qué `001` debe conservarse como texto?
- ¿Qué valida la fuente completa y qué comprueba solo la selección?
- ¿Por qué el conjunto vacío no es un saldo ausente imputado a cero?
- ¿Por qué cambia el contrato si repites filas para «hacer más grande» la muestra?
- ¿Qué faltaría ejecutar antes de comparar el tiempo de un plan diferido?

Criterio de salida: especificación precisa, respuesta manual justificada,
referencia repetible y detección del error compensado. R y escalas no bloquean
avanzar. No hay proyecto/checkpoint activo asociado; `04_large_credit_dataset`
sigue planificado. El material no acredita aprendizaje sin evidencia propia.

Siguiente: [10.02 — Polars: tablas y expresiones](../../../curriculum/10_polars_duckdb/README.md#02-polars-tablas-y-expresiones),
todavía planificada. Consulta los [pendientes del recorrido](../../../docs/storage-closure.md).
