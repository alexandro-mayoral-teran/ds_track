# Lab 09.03 — Escribir y comprobar Parquet desde Python

## Objetivo y entradas

Aplica la [lección 09.03](../../../curriculum/09_arrow_parquet/03_python_read_write/README.md).
Recibes el CSV conservado de 09.01, el contrato de 09.02 y las funciones de
[intercambio_python.py](../../../curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py).
Usa Python/pandas/PyArrow en el entorno elegido; no necesitas paquetes de R.
No hay proyecto ni checkpoint implementado asociado a esta práctica.

## Actividad

1. Antes de ejecutar, escribe qué papel tienen CSV, DataFrame, tabla Arrow y
   Parquet. Copia el contrato de tres columnas con tipos, nulabilidad, unidad
   y clave. Predice qué ocurriría si se infiriera el ID como número.
2. Completa [un recorrido de entorno y ejecución](../../../curriculum/09_arrow_parquet/03_python_read_write/recorridos.md).
   Registra intérprete y versiones. Si ya están disponibles, no reinstales.
   Usa `output/09_03_python` solo si no existe; conserva el Parquet y el JSON.
3. Crea tu script propio con los bloques de la lección y ejecútalo desde la raíz.
   Usa una carpeta nueva para el ejemplo por bloques. Inspecciona tipos pandas,
   esquema Arrow, valores `001`, índice y resultado de la relectura.
4. Explica por qué `preserve_index=False` es correcto aquí y sería peligroso si
   el ID solo viviera en el índice. Comprueba el ejemplo con `posicion_local`.
5. En el mismo script, tras los imports y la creación de `tabla`, prueba estas
   copias **en memoria**. No edites fuentes ni reemplaces tu entrega:

```python
# Cambiar el orden fisico no cambia la tabla bajo la clave acordada.
invertida = tabla.take(pa.array(list(reversed(range(tabla.num_rows))), type=pa.int64()))
comparar_tablas(tabla, invertida)

# Compensar dos saldos conserva la suma; debe fallar la comparacion por clave.
filas = tabla.to_pylist()
assert filas[0]["fecha_corte"] == filas[1]["fecha_corte"]
filas[0]["saldo_mxn"] += 1
filas[1]["saldo_mxn"] -= 1
compensada = pa.Table.from_pylist(filas, schema=ESQUEMA)
assert resumir(compensada) == resumir(tabla)
try:
    comparar_tablas(tabla, compensada)
except ValueError as error:
    print("Alteracion detectada:", error)
else:
    raise AssertionError("No se detecto el cambio por clave")
```

6. Prueba un esquema de `int64` con los mismos importes. Explica por qué puede
   representar esos valores y aun así incumplir el contrato `int32` exacto:

```python
esquema_ancho = pa.schema([
    pa.field("id_credito", pa.string(), nullable=False),
    pa.field("fecha_corte", pa.date32(), nullable=False),
    pa.field("saldo_mxn", pa.int64(), nullable=False),
])
ancha = pa.Table.from_pylist(tabla.to_pylist(), schema=esquema_ancho)
try:
    comparar_tablas(tabla, ancha)
except ValueError as error:
    print("Tipo distinto detectado:", error)
else:
    raise AssertionError("Se acepto int64 sin cambiar el contrato")

vacia = crear_tabla(df.iloc[:0].copy())
assert vacia.schema.equals(ESQUEMA, check_metadata=False)
assert resumir(vacia) == {"registros": 0, "ids": 0, "cortes": []}
```

7. Comprueba con una copia que la API de referencia rechaza una columna extra
   antes de convertir, y que no modifica el DataFrame original:

```python
copia_original = df.copy(deep=True)
try:
    crear_tabla(df.assign(columna_sobrante="no pertenece al contrato"))
except ValueError as error:
    print("Columna extra detectada:", error)
else:
    raise AssertionError("Se perdio una columna silenciosamente")
pd.testing.assert_frame_equal(df, copia_original)
```

8. **Ampliación opcional:** ejecuta la tabla independiente `[0, ausente, 10]`
   de la lección. Explica dtype, cobertura 2/3, suma observada y total desconocido.
   No la mezcles con la cartera ni cambies su contrato para aprobarla.
9. Cierra el proceso de exploración. Ejecuta `--verificar` desde otro proceso
   contra el Parquet entregado y vuelve a ejecutar tu script completo en una
   sesión nueva con otro destino. No vuelvas a escribir sobre la primera carpeta.
10. Redacta una nota que explique qué conservaste, qué cambió en la representación,
    por qué la igualdad de sumas no bastaba y qué falta para acreditar lectura R.

## Resultado, comprobación y evidencia

| Control | Resultado esperado |
| --- | --- |
| Entorno | pandas 2.3.3/PyArrow 21.0.0 de referencia; intérprete local identificado |
| Base | 28 observaciones, 14 IDs, 14 registros por corte |
| Saldos | Septiembre 29000; octubre 31800 MXN; diferencia 2800 |
| Esquema releído | string/date32/int32 no anulables; cero null; tres columnas |
| Índice | Omitido; clave ID/corte sigue en columnas; nuevo índice posicional en pandas |
| Orden invertido | Comparación por clave aprobada |
| Saldos compensados | Mismo resumen, comparación rechazada |
| Tipo más ancho/columna extra | Rechazo explícito bajo el contrato actual |
| Vacío | Mismo esquema, cero registros, sin cortes inventados |
| Sesión nueva | Verificación de solo lectura contra CSV, sin objetos previos |

Conserva contrato, script, versiones, salidas, explicación y mensajes esperados
de rechazo. No publiques el entorno, rutas personales ni archivos de práctica.
Mantén intactos CSV/Parquet de 09.01 y funciones/casos de 09.02. Un JSON de
ejecución pasada no demuestra que el Parquet siga intacto: vuelve a verificar.

<details>
<summary>Solución razonada</summary>

La clave es una pareja de columnas, no la posición del registro. Un índice local
puede omitirse porque el ID y el corte permanecen explícitos. Con otro diseño,
descartar el índice podría eliminar el identificador y habría que recuperarlo
como columna antes. La API no puede decidir esa intención por nosotros.

La escritura principal usa esquema explícito no anulable y controles de valores.
La lectura observa el esquema real antes de compararlo; no convierte int64 a
int32 para ocultar la diferencia. `validate(full=True)` no demuestra la unicidad
de la clave ni la no negatividad del saldo: esas reglas se comprueban aparte.

Invertir filas conserva la correspondencia ID/corte/valor. Sumar uno a un saldo
y restarlo a otro del mismo corte conserva los totales, pero cambia dos valores
asociados a claves distintas. Por eso se comparan todos los registros, además
del resumen. La columna extra se rechaza antes de que una selección de esquema
pueda omitirla; el original no se modifica.

El vacío tipado es una tabla válida bajo el contrato general; no reproduce los
resultados de la muestra de 28 registros. En la ampliación, un cero observado
y una ausencia siguen siendo distintos. La suma de conocidos no se convierte
en total completo. El retorno a pandas usa tipos respaldados por Arrow sin
exigir que el dtype se llame igual que el del DataFrame de entrada.

</details>

## Reflexión, criterio de salida y siguiente paso

¿Qué comprobarías si el archivo abre, pero una fecha vuelve con hora? ¿Una
versión más ancha del entero debe aceptarse sin cambiar el contrato? ¿Por qué
usar `safe=False` o rellenar null con cero impediría reconocer algunas pérdidas?

Cierra cuando puedas reconstruir la entrega, justificar esquema/índice y
detectar la alteración compensada con evidencia propia. Regresa a la
[lección 09.03](../../../curriculum/09_arrow_parquet/03_python_read_write/README.md).
Continúa con [09.04 — Leer y escribir desde R](../../../curriculum/09_arrow_parquet/README.md#04-leer-y-escribir-desde-r),
todavía planificada. Los [pendientes de almacenamiento](../../../docs/storage-closure.md)
separan material disponible, práctica del estudiante e integración futura.
