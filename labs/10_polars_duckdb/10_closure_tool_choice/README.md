# Lab 10.10 — Una elección defendible

## Propósito y entradas

Resolver una pregunta con tres motores y justificar uno para un contexto definido.
La [lección](../../../curriculum/10_polars_duckdb/10_closure_tool_choice/README.md)
presenta todos los valores de la muestra y conceptos; no necesitas entregas previas.

La financiera ficticia tiene veinte créditos y dos cortes: cuarenta filas en
el CSV incluido. ID textual 001–020; para j=0..19, saldos `137*j` en septiembre
y `137*j+83` en octubre de 2026. Unidad crédito/corte; clave ID/fecha única,
Date 1900–2100, saldo entero 0–2147483647 MXN sin ausencias. El cierre admite
hasta 1998 filas; no imputa ni elimina duplicados. Son datos sintéticos pequeños.

Pregunta: **créditos con saldo ≥ 2000 MXN al 31 de octubre de 2026**, más resumen
de todos los registros por fecha. Se espera:

| ID seleccionado | Saldo MXN |
| --- | ---: |
| 015 | 2001 |
| 016 | 2138 |
| 017 | 2275 |
| 018 | 2412 |
| 019 | 2549 |
| 020 | 2686 |

Seis/14061 seleccionados. Resumen completo: veinte/26030 en septiembre y
veinte/27690 en octubre. No sumes cortes para presentar saldo a una fecha única.

## Actividad

1. Escribe pregunta, unidad, reglas y resultados esperados antes de ejecutar.
2. Genera una entrega en carpeta nueva. Comprueba selección y resumen de cada
   motor después de escribir/releer, no solo conteo/suma del objeto en memoria.
3. Revisa el protocolo y las mediciones nuevas: qué incluye consulta, intervalo,
   proceso y pico residente; qué queda fuera y qué caché no se controló.
4. Define un contexto real o explícitamente ficticio de quien revisará/mantendrá
   el análisis. Elige motor por claridad, entorno y costos de alcance conocido.
5. Completa decision.json y verifica desde otra sesión con exigir_decision=True.
   Discute tu argumento con quien te acompaña; el verificador no lo califica.
6. En una copia, demuestra que un error compensado se detecta aun actualizando
   huellas. Conserva la entrega original y la evidencia del rechazo.

## Resultado y evidencia

Entrega fuente/contrato, entrada Parquet, seis Parquet de resultados, comparación,
crudas/mediciones, manifiesto y decisión. Conserva versiones, notas del equipo,
parámetros y evidencia de ejecución desde sesión nueva. No requiere notebook,
figura, aplicación, publicación web ni instalar Quarto para cerrar este módulo.

## Solución razonada

<details>
<summary>Generación y decisión con cifras de la corrida propia</summary>

Ejemplo con contexto **ficticio** de una persona que revisa pandas y entrega
tablas locales pequeñas. Sustituye las razones por las de tu práctica. Desde
la raíz en una sesión Python con el entorno elegido:

```python
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/10_closure_tool_choice").resolve()))
import cierre

entrega = Path("output/lab_1010")
x = cierre.generar(entrega, nota="Anotar condiciones conocidas del equipo")
assert x["control"]["saldo_mxn"] == 14061
costos = json.loads((entrega / "mediciones/informe.json").read_text(encoding="utf-8"))
pandas_costos = next(r for r in costos["resumen"] if r["motor"] == "pandas")
consulta = pandas_costos["consulta_ns"]
decision = json.loads((entrega / "decision.json").read_text(encoding="utf-8"))
decision.update(
    estado="documentada", motor_elegido="pandas",
    contexto="Caso ficticio: persona que revisa pandas, 40 filas y tablas para reporte local.",
    claridad="El equipo puede revisar filtro y groupby; no necesita introducir SQL para esta tarea.",
    entorno="pandas y PyArrow ya estan declarados; conservar versiones del manifiesto y entorno elegido.",
    costos=(f"Mediana de consulta {consulta['mediana']/1e6:.4f} ms, rango "
            f"{consulta['min']/1e6:.4f}-{consulta['max']/1e6:.4f} ms. "
            "Acepto este costo local por continuidad; no afirmo que sea la menor mediana."),
    limites="La medicion adjunta solo cubre seleccion/JSON, no resumen ni entrega completa; cache SO sin vaciar.",
    cuando_cambiaria="Si cambia volumen, equipo revisor o necesidad de SQL, conciliaria y mediria de nuevo."
)
# Editar la decision de esta entrega propia; no modifica fuente ni resultados.
(entrega / "decision.json").write_text(json.dumps(decision, ensure_ascii=False, indent=2), encoding="utf-8")
revision = cierre.verificar(entrega, exigir_decision=True)
assert revision["decision"] == "documentada"
print(revision)
```

La decisión cita una medición nueva y acepta su costo para el contexto descrito;
no necesita declarar un ganador en velocidad. La lectura de costos no prueba
calidad del argumento: discutirlo sigue siendo parte de la actividad.

En otra sesión repite imports, asigna entrega a la carpeta conservada y llama
solo a verificar. El verificador reconstruye contra el CSV externo incluido,
revisa ambos resultados por motor y no modifica archivos de la entrega.

</details>

<details>
<summary>Alteración compensada incluso con huella actualizada</summary>

Después de la solución anterior, en la raíz, con la carpeta original conservada:

```python
from pathlib import Path
import json
import shutil
import sys
import pyarrow as pa
import pyarrow.parquet as pq
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/10_closure_tool_choice").resolve()))
import cierre

copia = Path("output/lab_1010_alterada")
shutil.copytree("output/lab_1010", copia)  # Falla si el destino ya existe.
archivo = copia / "pandas/seleccion.parquet"
tabla = pq.read_table(archivo)
filas = tabla.to_pylist()
filas[0]["saldo_mxn"] += 1
filas[1]["saldo_mxn"] -= 1
assert sum(f["saldo_mxn"] for f in filas) == 14061
pq.write_table(pa.Table.from_pylist(filas, schema=tabla.schema), archivo)
manifiesto = json.loads((copia / "manifiesto.json").read_text(encoding="utf-8"))
manifiesto["archivos"]["pandas/seleccion.parquet"] = cierre.mediciones.huella(archivo)
(copia / "manifiesto.json").write_text(json.dumps(manifiesto), encoding="utf-8")
try:
    cierre.verificar(copia)
except ValueError as error:
    print("Cambio detectado:", error)
else:
    raise AssertionError("Actualizar una huella no debe sustituir la referencia externa")
```

La fuente externa sigue diciendo 015/2001 y 016/2138. El total no basta para
certificar esos pares; la huella describe contenido pero no su corrección.

</details>

## Ampliaciones y fronteras

- Genera otra entrega para septiembre ≥ 2000: cinco/11645. Octubre ≥ 2002:
  cinco/12060. Noviembre: selección vacía, dos grupos del resumen conservados.
  No mezcles mediciones de preguntas distintas en el mismo informe.
- Comprueba la referencia R base desde una sesión nueva: debe coincidir en
  cada par y grupo. No necesitas instalar otro paquete ni producir una entrega R previa.
- Usa --sin-mediciones solo al depurar. Debe impedir que exigir-decision pase
  aunque llenes todos los textos: todavía faltaría evidencia de costos.

## Criterio de salida y siguiente paso

Puedes reconstruir la respuesta desde fuente externa, explicar claves/tipos,
justificar sumas enteras, revisar la decisión y decir cuándo habría que cambiarla.
El material de 10 queda desarrollado; tu práctica se cierra con evidencia y
explicación revisada, no solo con una salida exitosa del programa.

`04_large_credit_dataset` y sus checkpoints siguen previstos en
[proyectos](../../../projects/README.md). Este lab no los implementa.
Siguiente: [11 — Reportes con Quarto](../../../curriculum/11_reporting_quarto/README.md),
comenzando por [11.01 — Reporte, fuente y renderizado](../../../curriculum/11_reporting_quarto/README.md#01-reporte-fuente-y-renderizado),
todavía planificada. Conserva pregunta, tablas, método y límites como entradas
para un reporte posterior; no instales herramientas solo por planificarlo.
