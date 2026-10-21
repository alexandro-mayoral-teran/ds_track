# Lab 09.02 — Acordar y comprobar un contrato

## Objetivo y entradas

Aplica la [lección 09.02](../../../curriculum/09_arrow_parquet/02_schemas_types/README.md).
Recibes la base de 28 observaciones de 09.01, el contrato de tres columnas,
[23 casos separados](../../../curriculum/09_arrow_parquet/02_schemas_types/casos_contrato.csv)
y evaluadores de solo lectura en Python estándar/R base. Conserva las entradas;
trabaja en un script o nota propios. No instales paquetes ni inicialices renv
en la raíz. No existe proyecto ni checkpoint implementado para este lab.

## Actividad

1. Antes de ejecutar, escribe una tabla de contrato: nombre, significado, unidad,
   tipo lógico, nulabilidad y regla. Añade unidad de observación, clave compuesta,
   rango de fechas y política de rechazos. Separa esquema y reglas de negocio.
2. Predice los motivos para cero, marcador `\N`, campo vacío, texto `NA`,
   fracción, negativo, entero fuera de rango y fecha imposible. Explica por
   qué no todos los rechazos son errores de tipo. Revisa las dos filas de
   clave repetida: ¿qué debe pasar si una tiene saldo inválido?
3. Ejecuta el recorrido Python completo de la lección desde el IDE o la terminal
   indicada. Contrasta cada motivo con tu predicción y cuenta aceptados/rechazos.
   Ejecuta también sus ejemplos de ausencia, Decimal, precisión e instante.
4. En RStudio o tu IDE, desde la raíz y en **Console de R**, ejecuta:

```r
source("curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.R", encoding = "UTF-8")
r <- comprobar_contrato()
d <- r$evaluados$diagnostico
stopifnot(nrow(d) == 23L, sum(d$aceptado) == 5L, sum(!d$aceptado) == 18L,
          identical(d$motivos, r$casos$motivos_esperados))
print(d[!d$aceptado, , drop = FALSE])
str(r$base$aceptados)
```

5. Con una copia **en memoria**, cambia el saldo de `duplicado_b` a `"-1"`.
   Comprueba que ambas filas siguen apartadas por clave, y la segunda conserva
   además `saldo_negativo`. No edites el CSV ni sus motivos esperados.
6. Prueba vacío y orden distinto con estas copias:

```r
entradas <- r$casos[columnas_contrato]
copia <- entradas
copia$saldo_mxn[r$casos$caso == "duplicado_b"] <- "-1"
alterado <- evaluar_contrato(copia)$diagnostico
stopifnot(alterado$motivos[r$casos$caso == "duplicado_a"] == "clave_repetida",
          alterado$motivos[r$casos$caso == "duplicado_b"] == "saldo_negativo|clave_repetida",
          identical(entradas, r$casos[columnas_contrato]))
vacio <- evaluar_contrato(entradas[FALSE, , drop = FALSE])
stopifnot(nrow(vacio$aceptados) == 0L,
          identical(names(vacio$aceptados), columnas_contrato),
          inherits(vacio$aceptados$fecha_corte, "Date"),
          is.integer(vacio$aceptados$saldo_mxn))
invertido <- evaluar_contrato(entradas[rev(seq_len(nrow(entradas))), , drop = FALSE])
stopifnot(identical(rev(invertido$diagnostico$motivos), d$motivos))
```

7. Ejecuta los ejemplos R de la lección. Explica por qué convertir `12.50` a
   integer, convertir un ID a número o comparar códigos de factor puede perder
   información aunque el programa continúe sin errores.
8. Diseña **por escrito** un contrato separado para dinero con dos decimales.
   Elige centavos enteros o decimal fijo, especifica rango, nulabilidad y qué
   harías con `12.345`. No conviertas la muestra de pesos a centavos ni cambies
   nombres/unidades sin dejarlo explícito. Explica por qué no usarías una
   tolerancia para aceptar dos claves diferentes o una diferencia de un centavo.
9. Para `[0, ausente, 10]`, comunica suma observada, cobertura y estado del total
   completo. Para un timestamp, indica unidad y zona que tendrías que acordar;
   explica por qué la fecha de corte no es un instante por sí sola.
10. Guarda tu script, reinicia R y ejecútalo entero; repite Python desde un proceso
    nuevo. Registra evidencia y dudas propias, sin atribuirte lectura Parquet.

## Resultado, comprobación y evidencia

| Control | Resultado esperado |
| --- | --- |
| Base original | 28 registros, 14 IDs, 14 por corte, 29000/31800 MXN |
| Casos separados | 23 registros = 5 aceptados + 18 rechazados |
| Aceptados de los casos | cero, maximo, bisiesto, limite_inferior, limite_superior |
| Clave repetida | Ambas apariciones apartadas; los otros motivos se conservan |
| Tipos R de aceptados | character / Date / integer, también con cero filas |
| Orden de filas invertido | Mismos motivos al recuperar el orden por caso |
| Ausencia analítica independiente | Suma observada 10, cobertura 2/3, total desconocido |
| Conservación | Originales intactos; sin paquetes, escrituras ni cambios de lockfile |

Conserva tu contrato, predicciones corregidas con explicación, script y salidas,
decisión sobre centavos y nota de límites. El saldo máximo de un caso no forma
parte de la población de la cartera y no se suma a sus cortes. Puedes dividir
la práctica en varias sesiones.

<details>
<summary>Solución razonada y decisiones posibles</summary>

El esquema exige texto, fecha y entero no anulables. Tres dígitos, años
1900–2100, saldo no negativo y unicidad ID/corte son reglas adicionales.
La sintaxis textual estricta también forma parte del contrato de entrada.

`0` es una observación válida; `\N` declara ausencia prohibida. Vacío y `NA`
son textos que no cumplen la forma numérica. `12.50` no se trunca para aprobar.
`-1` es un entero interpretable que viola dominio. `2147483648` no cabe en el
rango elegido aunque Python pueda almacenarlo. `2026-02-30` tiene forma ISO,
pero no corresponde al calendario. 2000 es bisiesto, 1900 no lo es.

El caso con varios fallos conserva `id_forma|fecha_calendario|saldo_negativo`.
La unicidad se evalúa sobre todas las claves completas antes de elegir aceptados:
si una repetición tiene saldo negativo, la otra sigue siendo una repetición.
Filtrar primero por saldo haría desaparecer evidencia de esa clave duplicada.

Una elección posible para centavos es columna `saldo_centavos`, entero no
anulable, rango 0–2147483647 centavos y escala 100. Se rechazan importes con más
de dos decimales y se conserva su texto; no hay redondeo implícito. Otra elección
es decimal de precisión y escala declaradas, con lector y cálculo compatibles.
Ambas requieren nuevo contrato, no reinterpretar silenciosamente `saldo_mxn`.

Para la muestra analítica, suma observada 10 y cobertura 2/3 no implican total
10: falta un saldo. En el ejemplo temporal, un mismo instante cae en fechas
distintas al cambiar de UTC a −06:00. La fecha de corte se conserva como Date.
Las categorías se comparan por etiquetas y metadatos acordados, no por códigos.

</details>

## Reflexión, criterio de salida y siguiente paso

Explica una pérdida que un esquema puede detectar y otra que requiere reglas
de negocio. Propón un cambio de valores que conserve la suma y aun así deba
fallar una comparación por clave. ¿Qué información adicional necesitarías
para comprobar una fila inexistente en vez de una celda ausente?

Cierra cuando justifiques el contrato, los resultados y sus límites, con
evidencia propia. Regresa a la [lección 09.02](../../../curriculum/09_arrow_parquet/02_schemas_types/README.md).
Continúa con [09.03 — Leer y escribir desde Python](../../../curriculum/09_arrow_parquet/03_python_read_write/README.md).
Consulta los [pendientes de almacenamiento](../../../docs/storage-closure.md).
