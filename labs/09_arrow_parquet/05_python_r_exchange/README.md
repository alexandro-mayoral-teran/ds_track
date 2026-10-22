# Lab 09.05 — Comprobar el archivo del otro lenguaje

## Propósito y entradas

Practicar [09.05 — Intercambio Python y R](../../../curriculum/09_arrow_parquet/05_python_r_exchange/README.md)
con sus herramientas preparadas, sin instalar paquetes ni usar entregas de otras
secciones. Trabaja con Python en la raíz de DS Track y R en el proyecto renv
existente. Usa la misma carpeta compartida que indica tu TXT local.

La base común tiene 28 filas, 14 IDs en dos fechas y esquema no anulable
`string/date32/int32`; clave ID/fecha, saldo en pesos enteros no negativos.
Son 14 registros y 29 000/31 800 MXN por corte, septiembre/octubre de 2026.
La muestra independiente tiene tres IDs A/B/C, fechas de calendario,
etiquetas `"Crédito ágil"`/vacío/ausente e importes 0/ausente/10. Solo etiqueta
e importe admiten ausencias; suma observada 10 con cobertura 2/3.

## Actividad

1. Python: crea una entrega nueva en `python_lab/` con ambas tablas.
2. R: lee esa carpeta, compara todas las claves/valores y escribe otra en `r_lab/`.
3. Python: reinicia y verifica la carpeta R sin usar objetos previos.
4. Haz una copia de `r_lab/` en `compensada/`; intercambia los dos primeros
   saldos de septiembre, sin cambiar sus IDs. Conserva las sumas, pero exige
   que **ambos lectores rechacen** la copia. Nunca modifiques `r_lab/`.
5. En otra copia, `texto_ausente/`, reemplaza solo la etiqueta vacía de B por
   ausencia. El esquema permite ambas cosas: ¿eso hace equivalentes los valores?
   Comprueba el rechazo en ambos lectores.

Extensión opcional: escribe una tercera copia con filas invertidas y exige
que se acepte por clave. No hace falta que coincidan los bytes de dos escritores.

## Resultado y comprobación

- Dos cruces satisfactorios con ambos archivos y procesos nuevos.
- Tipos/nulabilidad, claves y valores contrastados antes del resumen.
- Dos copias alteradas rechazadas por ambos lenguajes, con explicación del motivo.
- Entradas y entregas originales conservadas. El total completo de la muestra
  con importe ausente sigue desconocido, aunque su suma observada sea 10.

<details>
<summary>Una solución razonada</summary>

**Primero Python**, desde la raíz de DS Track. Las funciones reconstruyen los
datos, por lo que no necesitas ejecutar otra sección para obtener una entrega:

```python
from pathlib import Path
import sys

sys.path.insert(0, str(Path("curriculum/09_arrow_parquet/05_python_r_exchange").resolve()))
import intercambio_cruzado as cruce

compartida = Path("output/09_05_cruce").resolve()
print(cruce.escribir_desde_python(compartida / "python_lab"))
```

**Ahora R**, desde la raíz del proyecto de práctica, tras reiniciar:

```r
source("intercambio_cruzado.R", encoding = "UTF-8")
compartida <- readLines("ruta_cruce_0905.txt", encoding = "UTF-8")
resultado_python <- leer_desde_python(file.path(compartida, "python_lab"))
stopifnot(identical(resultado_python$cartera$saldo_mxn, c(29000, 31800)),
  resultado_python$muestra$importes_conocidos == 2L)
print(resultado_python)
print(escribir_desde_r(file.path(compartida, "r_lab")))
```

**Vuelve a Python en una sesión nueva.** Copiar conserva la entrega original;
`copytree()` rechaza destinos ocupados. Solo se reescriben los Parquet de las
copias que acabamos de crear:

```python
from pathlib import Path
import shutil
import sys
import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, str(Path("curriculum/09_arrow_parquet/05_python_r_exchange").resolve()))
import intercambio_cruzado as cruce

compartida = Path("output/09_05_cruce").resolve()
resultado_r = cruce.leer_desde_r(compartida / "r_lab")
assert resultado_r["cartera"]["registros"] == 28
assert resultado_r["muestra"]["suma_observada"] == 10

compensada = compartida / "compensada"
shutil.copytree(compartida / "r_lab", compensada)
original = pq.ParquetFile(compensada / "base_comun.parquet").read()
filas = original.to_pylist()
assert filas[0]["fecha_corte"] == filas[1]["fecha_corte"]
assert filas[0]["saldo_mxn"] != filas[1]["saldo_mxn"]
filas[0]["saldo_mxn"], filas[1]["saldo_mxn"] = filas[1]["saldo_mxn"], filas[0]["saldo_mxn"]
alterada = pa.Table.from_pylist(filas, schema=original.schema)
assert cruce.cartera.resumir(original) == cruce.cartera.resumir(alterada)
pq.write_table(alterada, compensada / "base_comun.parquet")

texto_ausente = compartida / "texto_ausente"
shutil.copytree(compartida / "r_lab", texto_ausente)
original_muestra = pq.ParquetFile(texto_ausente / "muestra.parquet").read()
filas_muestra = original_muestra.to_pylist()
assert filas_muestra[1]["id_prueba"] == "B" and filas_muestra[1]["etiqueta"] == ""
filas_muestra[1]["etiqueta"] = None
pq.write_table(pa.Table.from_pylist(filas_muestra, schema=original_muestra.schema),
               texto_ausente / "muestra.parquet")

for carpeta in (compensada, texto_ausente):
    try:
        cruce.leer_desde_r(carpeta)
    except ValueError as error:
        print(carpeta.name, error)
    else:
        raise AssertionError("Se aceptó una copia alterada")
```

El esquema de ambas copias sigue siendo compatible. En una se conserva el
resumen de cartera y en la otra ni siquiera cambian los importes. Lo que falla
es la correspondencia de los valores con la referencia, no la decodificación.
Las notas de sesión copiadas no se actualizan ni se usan como prueba de validez.

**Finalmente R en otra sesión nueva**. El mismo verificador puede inspeccionar
cualquier carpeta que siga el contrato: su nombre no prueba quién escribió
el archivo. Aquí le entregamos copias de origen R alteradas con Python:

```r
source("intercambio_cruzado.R", encoding = "UTF-8")
compartida <- readLines("ruta_cruce_0905.txt", encoding = "UTF-8")
for (nombre in c("compensada", "texto_ausente")) {
  error <- tryCatch({
    leer_desde_python(file.path(compartida, nombre))
    NULL
  }, error = function(e) e)
  stopifnot(inherits(error, "error"))
  cat(nombre, ": ", conditionMessage(error), "\n", sep = "")
}
print(leer_desde_python(file.path(compartida, "python_lab")))
print(leer_desde_python(file.path(compartida, "r_lab")))
```

`tryCatch()` y `try/except` se usan para inspeccionar un rechazo esperado y
fallar si no ocurre. No convierten un archivo alterado en válido ni ocultan
errores del recorrido normal. La última comprobación vuelve a leer las
entregas originales para contrastar que siguen siendo válidas.

</details>

## Evidencia y reflexión

Conserva scripts, versiones, rutas locales de entrada/salida y resultados de
ambos lectores. Registra los dos cruces y los rechazos esperados, explicando
qué cambió y qué se mantuvo. La configuración con rutas personales permanece
en tu copia local; no publiques esos datos como parte del material del curso.

- ¿Qué comprueba leer con el otro lenguaje que no prueba la relectura propia?
- ¿Por qué admitir ausencias no autoriza cambiar un texto vacío por ausencia?
- ¿Por qué las sumas y las notas de sesión no detectan por sí solas estas copias?
- ¿Qué acuerdo haría falta antes de intercambiar decimales o factores?

No hay proyecto/checkpoint implementado asociado. Después de comprobar y
explicar, continúa con [09.06 — Lectura selectiva y datasets](../../../curriculum/09_arrow_parquet/README.md#06-lectura-selectiva-y-datasets),
todavía planificada. Consulta los [pendientes de cierre](../../../docs/storage-closure.md).
