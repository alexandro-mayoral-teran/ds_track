# Lab 02.03 — Explicar qué se selecciona y en qué orden

## Relación, entrada y resultado

- Lección: [Seleccionar, filtrar y ordenar](../../../curriculum/02_pandas/03_select_filter_sort/README.md).
- Entrada: cartera_demo.csv de la lección 02 y select_filter_sort.py de la 03.
- Resultado: selecciones verificadas y una nota con condiciones, IDs, orden y subtotales.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 50 a 70 minutos o dos sesiones. Utiliza el entorno con pandas preparado.
Predice antes de ejecutar y consultar soluciones; no modifiques la fuente original.

## Parte A — La pregunta inicial

1. Revisa las seis filas e identifica cuáles cumplen saldo ≥ 500 y atraso conocido ≥ 5.
2. Predice los IDs, índices originales, orden por saldo y subtotal.
3. Ejecuta el script y compara con la salida y la tabla de desconocidos.
4. Explica por qué 006 entra, 001 no entra y 005 no se evalúa como atraso cero.

<details>
<summary>Ver solución de la parte A</summary>

Entrarán 002, 003 y 006, con índices originales 1, 2 y 5. Ordenados por saldo
descendente: 1500, 750 y 500 MXN, subtotal 2750. 006 está justo en los límites
500/5 y >= lo incluye. 001 tiene atraso 0 y no cumple ambas condiciones.
005 tiene atraso desconocido: su máscara queda desconocida y no se incluye en
esta pregunta. Permanece visible aparte para revisión, sin sustituir el dato.

</details>

## Parte B — Otra selección por segmentos

Con la muestra original, dentro de main sustituye la asignación de seleccion:

1. Selecciona consumo o servicios, con saldo de al menos 500.
2. Conserva las cuatro columnas de salida, ordena y predice IDs y subtotal.
3. Ejecuta y verifica que la entrada conserva las seis filas.

<details>
<summary>Ver una solución de la parte B</summary>

```python
mascara = tabla["segmento"].isin(["consumo", "servicios"]) & (tabla["saldo_mxn"] >= 500)
seleccion = tabla.loc[mascara.fillna(False), COLUMNAS_SALIDA].copy()
```

Mantén ordenar_creditos y la exportación del programa. Se obtienen 001, 003 y
006, ordenados con saldos 1000, 750 y 500: subtotal 2250 MXN. Son tres filas y
cuatro columnas. No se exige atraso en esta pregunta; cambiarla cambia el universo.

</details>

## Parte C — OR y negación con valores desconocidos

Vuelve a la muestra original. Puedes añadir estas comprobaciones dentro de main:

1. Selecciona saldo ≥ 1000 **o** atraso ≥ 30. Predice qué ocurre con 005.
2. Para el filtro inicial de la parte A, compara negar la máscara original con
   negar la máscara después de fillna(False).
3. Explica cuál permite reunir todas las filas no incluidas y por qué eso no
   equivale a declararlas inválidas.

<details>
<summary>Ver solución de la parte C</summary>

```python
mascara_or = (tabla["saldo_mxn"] >= 1000) | (tabla["dias_atraso"] >= 30)
seleccion_or = tabla.loc[mascara_or.fillna(False), COLUMNAS_SALIDA].copy()
print(list(seleccion_or["id_credito"]))  # 001, 002, 003, 005, en orden de origen
print(seleccion_or["saldo_mxn"].sum(min_count=1))  # 5500

bruta = (tabla["saldo_mxn"] >= 500) & (tabla["dias_atraso"] >= 5)
print(list(tabla.loc[~bruta, "id_credito"]))  # 001, 004
confirmadas = bruta.fillna(False)
print(list(tabla.loc[~confirmadas, "id_credito"]))  # 001, 004, 005
```

005 sí entra en la pregunta OR: su saldo basta para confirmar una de las
condiciones. En el filtro inicial, ~bruta conserva NA para 005, que no se
selecciona al aplicar loc. Tras decidir que solo se incluyen condiciones confirmadas,
la negación reúne las tres filas no incluidas. No cumplen o no se pueden evaluar;
eso no demuestra que los registros sean incorrectos.

</details>

## Parte D — Un empate en el saldo

1. Después de la parte A, copia el CSV original como output/cartera_practica.csv.
2. Inserta después del encabezado, antes de las filas existentes, el registro
   007, servicios, corte 2026-09-30, saldo 1500 y atraso 10.
3. En main lee esa copia y escribe output/seleccion_practica.csv.
4. Recupera el filtro inicial de seleccionar_creditos y comprueba su orden.
5. Explica qué lo determina cuando dos saldos son iguales.

<details>
<summary>Ver una solución de la parte D</summary>

```csv
007,servicios,2026-09-30,1500,10
```

En main:

```python
entrada = carpeta / "output" / "cartera_practica.csv"
salida = carpeta / "output" / "seleccion_practica.csv"
seleccion = seleccionar_creditos(tabla, saldo_minimo=500, atraso_minimo=5)
```

Hay siete entradas y cuatro seleccionados. El orden es 002, 007, 003 y 006,
subtotal 4250 MXN. Aunque 007 aparece antes que 002 en la copia de origen, el
desempate por ID ascendente coloca 002 primero. Las etiquetas originales se
conservan durante la selección; sus posiciones cambian al ordenar.

</details>

## Parte E — Un filtro vacío

1. Utiliza saldo_minimo=10000 y atraso_minimo=5.
2. Predice forma, columnas y contenido del CSV generado.
3. Ejecuta sin consultar una primera fila inexistente.
4. Vuelve a los umbrales iniciales y repite: comprueba que no se acumulan filas.

<details>
<summary>Ver solución de la parte E</summary>

La selección tiene forma (0, 4), mantiene COLUMNAS_SALIDA y la exportación
contiene solo el encabezado. empty es True; el script evita iloc[0]. El subtotal
con min_count=1 se muestra como ausencia de observaciones, no como una cifra medida.
La tabla de entrada permanece intacta y los atrasos desconocidos se siguen
mostrando aparte. Al restaurar el filtro, se reemplaza la salida con el nuevo
resultado: tres filas para la muestra original o cuatro para la copia de la parte D.

</details>

## Evidencia y reflexión

- Conserva código y una nota con pregunta, umbrales, política de NA, IDs, orden
  y subtotal; identifica si utilizaste la fuente original o la copia ampliada.
- ¿En qué cambia la respuesta al pasar de >= a >, o de & a |?
- ¿Por qué el índice no empieza necesariamente en cero después de filtrar?
- ¿Por qué cambiar una máscara no equivale a limpiar la columna de origen?
- ¿Qué controla reset_index(drop=True) al comparar la salida recargada?
- Si usas Git, revisa y registra cambios de código y nota. output está ignorado;
  publicar en el repositorio compartido no es requisito para completar el lab.

## Siguiente paso

04 — Tipos y columnas calculadas está por desarrollar. Consulta el
[plan de la siguiente lección](../../../curriculum/02_pandas/README.md#04-tipos-y-columnas-calculadas)
antes de su futuro lab.
