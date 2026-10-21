# Lab 08.09 — Un análisis, dos implementaciones

## Objetivo y entradas

Practicar el [cierre visual y comparación con Python](../../../curriculum/08_visualization_r/09_visual_comparison/README.md).
Recibes la fuente conservada `datos/cartera_texto.csv`, las funciones R de 07.10,
el [script R](../../../curriculum/08_visualization_r/09_visual_comparison/cerrar_visual.R)
y la [referencia Python](../../../curriculum/08_visualization_r/09_visual_comparison/comparar_python.py).
Usa los entornos existentes; no cambia ningún lockfile. 08.08 sigue pendiente.

Trabaja en el proyecto renv desde RStudio o tu IDE. Para Python usa la terminal
y uno de los recorridos completos de la lección, desde la raíz de DS Track.
Puedes repartir la práctica en reconstrucción, diagnóstico e interpretación.
No hay proyecto/checkpoint integrador implementado que acreditar con este lab.

## Actividad y resultados esperados

1. Antes de ejecutar, escribe la pregunta, unidad original, población de la
   figura, dos cortes y unidad monetaria. Predice por qué 18 registros por
   corte no implican 18 pares.
2. Guarda una copia propia del script R. Reinicia R y genera una entrega con
   nombre nuevo. Comprueba los siete CSV y el RDS desde otra sesión, siguiendo
   el bloque final de la lección. Conserva las advertencias y explica los rechazos.
3. Ejecuta Python sobre la fuente original y esa entrega R, usando otro destino
   nuevo. Revisa el JSON y abre las dos figuras. Explica qué calcula Python
   por su cuenta y qué lee de R solo para contrastar.
4. Comprueba la relectura de las dos tablas Python. Desde un archivo Python en
   tu IDE, con la raíz de DS Track como directorio, adapta la primera ruta:

```python
from pathlib import Path
from runpy import run_path

practica = Path("curriculum/06_r_foundations/09_known_result/output/cierre_ventas")
api = run_path("curriculum/08_visualization_r/09_visual_comparison/comparar_python.py")
esperado = api["reconstruir"](practica / "datos/cartera_texto.csv")
salida = practica / "output/entrega_visual_python"
api["conciliar"](salida / "base_comun.csv", esperado["base_comun"],
                 ["id_credito", "saldo_sep", "saldo_oct", "diferencia_mxn"], "id_credito")
api["conciliar"](salida / "datos_figura.csv", esperado["datos_figura"],
                 ["fecha_corte", "creditos", "saldo_mxn", "aceptados_corte"], "fecha_corte")
print("Tablas Python releidas y conciliadas")
```

`run_path` devuelve las funciones definidas sin activar el bloque de terminal
`if __name__ == "__main__"`. No exporta al cargar. `conciliar` exige igualdad
de campos por clave y lanza `ValueError` si no coincide. No exige el orden de filas.

5. Diseña un error que conserve las sumas: añade 100 MXN al saldo de septiembre
   de un ID y réstalos del de otro. Predice si bastaría comparar dos totales.
   Haz el experimento en memoria con el bloque de la solución; no edites entregas
   ni la fuente. Debe fallar la conciliación por pares.
6. Calcula diferencia y cambio relativo de la base común, cobertura por corte
   y diferencia de todos los aceptados. Identifica la pregunta de cada medida.
7. Redacta entre 100 y 180 palabras con hallazgo, base, cortes, cobertura,
   fuente sintética y límites. Explica una diferencia visual entre las figuras
   que no cambie el análisis, y una que sí podría engañar.

## Comprobación y evidencia

| Elemento | Esperado |
| --- | --- |
| Partición de entrada | 48 = 36 aceptados + 12 rechazados |
| Base común | 14 IDs; dos registros por ID |
| Conservados sin pareja | Ocho registros, cuatro por corte |
| Fuera de los dos cortes | Cero en esta muestra; tabla con cabecera conservada |
| Saldos de la base común | 29000/31800 MXN; diferencia 2800 MXN |
| Cambio relativo | Aproximadamente 9.66%, denominador 29000 MXN |
| Cobertura | 14/18 por fecha, aproximadamente 77.78% |
| Todos los aceptados | 39900/41500 MXN; diferencia 1600 MXN |
| Alteración compensada | Suma igual; conciliación de pares falla |

Conserva tu script R, el archivo Python de comprobaciones, las dos entregas,
la salida de la comprobación desde sesión nueva y el comentario. Las capturas
de figuras pueden acompañar la evidencia; no reemplazan tablas y código.
No registres esta práctica como terminada solo por ejecutar la solución.

<details>
<summary>Solución razonada: alteración compensada e interpretación</summary>

Continúa el archivo Python anterior; `esperado`, `api` y `practica` ya están
definidos. `deepcopy` permite alterar una copia sin modificar lo reconstruido:

```python
from copy import deepcopy

alterados = deepcopy(esperado["base_comun"])
for indice, cambio in ((0, 100), (1, -100)):
    fila = alterados[indice]
    fila["saldo_sep"] = str(int(fila["saldo_sep"]) + cambio)
    fila["diferencia_mxn"] = str(int(fila["saldo_oct"]) - int(fila["saldo_sep"]))
assert sum(int(f["saldo_sep"]) for f in alterados) == 29000
try:
    api["conciliar"](practica / "output/entrega_visual_r/base_comun.csv", alterados,
                     ["id_credito", "saldo_sep", "saldo_oct", "diferencia_mxn"], "id_credito")
except ValueError:
    print("Error compensado detectado por ID; los totales no bastan")
else:
    raise AssertionError("La comprobacion debio fallar")
```

La suma de septiembre y la suma de diferencias se conservan, pero dos saldos
y sus diferencias individuales cambian. Por eso el control usa ID y ambos
importes; no certifica equivalencia a partir de un agregado.

Un comentario posible:

> En la muestra sintética de DS Track, el saldo observado de los mismos 14
> créditos pasa de 29000 MXN el 30 de septiembre de 2026 a 31800 MXN el 31 de
> octubre. La diferencia es 2800 MXN, aproximadamente 9.66% del saldo inicial.
> Esta base representa 14 de los 18 aceptados de cada fecha; quedan cuatro sin
> pareja por corte y los rechazos se conservan aparte. R y Python coinciden
> en registros, motivos, pares y resumen. Las barras resumen dos fechas, sin
> describir la evolución diaria ni explicar causas. El resultado no representa
> todos los aceptados ni permite generalizar a una cartera real. La tabla de
> pares muestra que cada ID aumenta 200 MXN, dato que las barras solas no prueban.

Cambiar el margen o la tipografía no altera los saldos. Truncar el eje vertical
de barras sin explicarlo puede exagerar visualmente el cambio. Aun con tablas
conciliadas hay que revisar el archivo final y su lectura.

</details>

## Reflexión, criterio de salida y siguiente paso

Explica por qué R y Python pueden dibujar figuras distintas y representar el
mismo análisis; después da un ejemplo de figuras parecidas con poblaciones
distintas. Identifica lo que no comprueba el JSON ni una inspección visual.

Puedes cerrar el lab cuando reconstruyas sin estado previo, concilies la
relectura, detectes el error compensado y expliques las medidas con sus bases.
Registra evidencia y dudas; 08.08 continúa pendiente. Regresa a la
[lección 08.09](../../../curriculum/08_visualization_r/09_visual_comparison/README.md)
y revisa como siguiente sección
[08.08 — Exportación reproducible](../../../curriculum/08_visualization_r/README.md#08-exportacion-reproducible).
Todavía es un plan, no un enlace a una lección disponible. El proyecto y los
checkpoints integradores siguen pendientes.
