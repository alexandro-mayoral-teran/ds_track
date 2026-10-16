# Lab 05.05 — Tipos y contratos de funciones

## Entrada, propósito y resultado

Completa la [lección 05.05](../../../curriculum/05_python_applied/05_types_contracts/README.md).
Usa el paquete compartido, el entorno elegido y las muestras conservadas.
No requiere notebook, instalaciones ni un checker estático.

**Resultado:** contrato explicado con tus palabras, ejemplos ejecutados y un
caso de contrato propio comprobado. No hay proyecto/checkpoint implementado
asociado. Puedes dividir el lab en sesiones de lectura, ejecución y revisión.

## A. Leer una firma y descubrir lo que falta — esencial

1. Abre revision.py y lee únicamente la firma de review_summary.
2. Explica el tipo y obligatoriedad de cada parámetro, el significado de `*`
   y el retorno. ¿Qué llamada permite omitir cut? ¿Qué llamada admite None?
3. Sin leer el cuerpo, anota las preguntas que el tipo DataFrame no responde.
4. Lee su docstring y completa: columnas, unidad, orden, ausencias, errores,
   efectos sobre fuentes/lista de selección y significado de [].

**Comprobación:** distingues hechos de la firma y reglas documentadas.
**Evidencia:** una ficha de contrato de una página o menos.

<details>
<summary>Ver solución razonada de A</summary>

source es obligatorio y admite str/Path; cut puede omitirse y admite str/None.
segments solo se pasa por nombre, puede omitirse y admite list[str]/None.
El resultado es una tabla; esa anotación no fija sus columnas, moneda o claves.
El docstring declara ocho columnas, mediana en MXN, cobertura 0–100,
orden de la selección, ausencia preservada y ninguna escritura. None selecciona
todos los grupos, [] ninguno; ambos siguen leyendo y conciliando las fuentes.
Una lista duplicada es inválida aunque todos sus elementos sean str.

</details>

## B. Predecir tipos, resultados y errores — esencial

Antes de ejecutar, completa esta tabla con resultado o tipo de excepción y razón:

| Llamada | Predicción | Regla |
| --- | --- | --- |
| double_annotated("3") | | |
| coverage_pct(0, 4) | | |
| coverage_pct(0, 0) | | |
| coverage_pct(5, 4) | | |
| coverage_pct(True, 4) | | |
| normalize_cut() | | |
| normalize_cut("") | | |
| normalize_cut("2024-02-29") | | |

Sigue el recorrido de tu shell en la lección para ejecutar el script y las dos
colecciones. Registra intérprete, comandos, cantidad de métodos y códigos de salida.
Para comprobar los casos individuales, desde 01_notebook_to_modules inicia
`python` e importa las funciones antes de llamarlas:

```python
from ejecutar_contratos import double_annotated
from analisis_cartera.contratos import coverage_pct, normalize_cut
```

Ejecuta las llamadas una por una: una excepción en el intérprete permite seguir
probando en la siguiente entrada. No pegues todas como un script que se detenga
en el primer rechazo. Sal con `exit()` al terminar.

**Comprobación:** predicciones comparadas con ejecución; doce pruebas nuevas
y veintiuna previas (o veintidós con tu ejercicio anterior), OK y código 0.
**Evidencia:** tabla corregida con explicación de las diferencias encontradas.

<details>
<summary>Ver solución razonada de B</summary>

Resultados en orden: texto "33"; 0.0; None; ValueError; TypeError;
"2026-10-31"; ValueError; "2024-02-29". El último es un día válido de año bisiesto.
La anotación de double_annotated no rechaza ni convierte texto. El bool se
excluye mediante código; la relación 5 > 4 viola una regla de conteos.
Omitir cut activa el predeterminado, pero texto vacío no significa None.

</details>

## C. None, lista vacía y orden — práctica

Desde el mismo directorio inicia una nueva sesión `python` y prepara:

```python
from pathlib import Path
from pandas.testing import assert_frame_equal
from analisis_cartera.revision import review_summary

source = Path("../../03_sql_databases/01_relational_sqlite/data")
all_groups = review_summary(source)
chosen = review_summary(source, segments=["educacion", "comercio"])
empty = review_summary(source, segments=[])
print(chosen[["segmento", "registros", "conocidos", "mediana_mxn", "cobertura_pct"]])
print(empty.shape)
assert_frame_equal(empty, all_groups.iloc[:0], check_exact=True)
```

1. Explica las dos poblaciones mostradas y el orden de chosen.
2. Confirma qué columnas/dtypes conserva empty; distingue cero filas de cero columnas.
3. Prueba `segments="comercio"` y una lista duplicada; identifica los errores.
4. Prueba un corte válido sin filas, "2027-01-31", sin selección de segmentos.
   Explica por qué devuelve cuatro filas sin mediana, mientras [] devuelve cero filas.
5. Lee test_lista_vacia_no_omite_validacion_de_datos sin modificar fuentes.
   ¿Qué error seguiría detectándose aunque no se pidieran grupos?

**Comprobación:** comercio original 5/5, mediana 3100; educación 3/0 sin
mediana. Empty tiene forma (0, 8); corte sin registros conserva cuatro grupos.
**Evidencia:** tabla de los cuatro significados: None, [], corte sin filas y fuente inválida.

<details>
<summary>Ver solución razonada de C</summary>

None conserva todos los grupos; la lista explícita define orden educación/comercio.
[] pide no devolver grupos y conserva el esquema del resumen calculado.
Un corte válido sin registros no elimina las filas de los cuatro grupos:
registros/conocidos son cero y las dos medidas están ausentes. Una fuente
con créditos duplicados se rechaza aun con segments=[]: no se devuelve una
tabla vacía como si el análisis hubiera sido válido.

Los números anteriores corresponden a los CSV originales, no a la fixture pequeña
de 05.04/05.05. En esta última comercio tiene 3/2 y mediana 0,5.

</details>

## D. Escribir un contrato y comprobarlo — práctica

1. En pruebas_0505/test_revision.py agrega a PruebasRevision un método
   test_segmento_sin_registros_conserva_fila. Conserva tus cambios anteriores.
2. Antes de programar, escribe el contrato para pedir ["servicios"] sobre
   self.source (la fixture pequeña, no los CSV originales).
3. Comprueba orden, una fila, registros/conocidos cero y ambas medidas ausentes.
4. Ejecuta de nuevo la colección de 05.05: debe descubrir trece métodos.
5. Explica qué cambio incorrecto detectaría este caso y qué no demostraría.

**Comprobación:** servicios se conserva sin convertir sus ausencias en ceros.
**Evidencia:** ficha breve, método propio, ejecución y razón de cada esperado.

<details>
<summary>Ver una solución razonada de D</summary>

Dentro de la clase existente, con la misma indentación que los otros métodos:

```python
    def test_segmento_sin_registros_conserva_fila(self):
        actual = review_summary(self.source, segments=["servicios"])
        self.assertEqual(actual["segmento"].tolist(), ["servicios"])
        row = actual.iloc[0]
        self.assertEqual(row["registros"], 0)
        self.assertEqual(row["conocidos"], 0)
        self.assertTrue(pd.isna(row["mediana_mxn"]))
        self.assertTrue(pd.isna(row["cobertura_pct"]))
```

pd y review_summary ya están importados. La lista de segmentos comprueba una
única fila además de su nombre. Detecta eliminar grupos sin registros o inventar
cero para medidas no definidas. No demuestra por sí sola que todas las fuentes
sean válidas ni que las figuras se interpreten correctamente.

</details>

## Extensión opcional — análisis sin ejecutar

Si ya dispones de un checker en el entorno elegido, analiza un archivo pequeño
con double_annotated y la llamada textual. Anota herramienta/versión y distingue
el diagnóstico del resultado al ejecutar. No instales ni reconfigures el entorno
para cerrar este lab. Si no tienes checker, basta explicar qué diferencia se
esperaría y qué reglas seguirían necesitando if/raise.

## Reflexión, evidencia y continuidad

- ¿Qué aporta int que no aporta un nombre, y qué regla sigue faltando?
- ¿Qué diferencia hay entre un argumento omitido y un valor None permitido?
- ¿Quién debe validar una tabla antes de llamar summarize directamente?
- ¿Por qué list[str] no garantiza nombres únicos del catálogo?
- ¿Qué sucedería con 0.0 si usaras if not coverage para detectar ausencia?

Registra evidencia y dudas en PROGRESS.md. Puedes avanzar cuando expliques la
firma, el contrato y las comprobaciones con tus palabras, sin confundir pasar
ejemplos con validación de cualquier archivo futuro.

Continúa con [05.06 — Clases, composición y dataclasses](../../../curriculum/05_python_applied/06_classes_composition/README.md),
disponible como práctica opcional. El cierre 05.11 sigue planificado; las ampliaciones
no bloquean el núcleo. Volver a la [lección 05.05](../../../curriculum/05_python_applied/05_types_contracts/README.md).
