# 02.05 — Faltantes, duplicados y reglas

<a id="05--faltantes-duplicados-y-reglas"></a>

[Inicio](../../../README.md) / [Módulo 02](../README.md) / **Lección 02.05**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Aplicar reglas y conservar aceptados, rechazos y motivos conciliados |
| **Necesitas** | Entorno de estudio con pandas; entrada incluida o compartida según la lección |
| **Evidencia** | Aceptados, rechazos y nota de reglas y motivos |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/02_pandas/05_missing_duplicates_rules/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-prerrequisitos-y-objetivos"></a>

## Propósito

Separar registros utilizables de registros que requieren revisión, sin perder
la fuente ni el motivo de cada decisión.

## Antes de empezar

Completa [02.04 — Tipos y columnas calculadas](../04_types_calculated_columns/README.md) y su lab.
Usa el mismo entorno con pandas 2.3.3 como referencia. Trabaja desde la raíz
de DS Track, con tu editor y el shell elegido. La entrada se enlaza más abajo;
no necesitas producir archivos de lecciones anteriores para leer esta muestra.

Retoma las [reglas y rechazos de Python fundamental](../../01_python_foundations/06_validation_summary/README.md).
La normalización de texto y la interpretación de fechas llegan en 02.06.

## Qué vas a aprender

- Definir la clave y distinguir repeticiones exactas de conflictos por clave.
- Detectar ausencias y aplicar reglas explícitas sin imputar ni borrar automáticamente.
- Conservar todos los motivos y los valores de origen de cada rechazo.
- Conciliar la partición y distinguir los saldos conocidos de los pendientes.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Script de ejemplo](quality_rules.py) | Evaluar reglas, apartar registros y comprobar la reconstrucción de la partición | Para el ejemplo |
| [CSV de entrada](cartera_calidad.csv) | Explorar 44 registros con conflictos deliberados y fuente conservada | Entrada incluida |

Abre los recursos cuando aparezcan en el recorrido. Lee el código antes de
ejecutarlo y contrasta sus resultados esperados. Conserva los originales y
trabaja las variantes en tu copia. Los datos compartidos se reutilizan desde
su ubicación actual, sin duplicarlos.

## 1. Antes de limpiar: acordar qué significa una fila válida

[cartera_calidad.csv](cartera_calidad.csv) contiene **44 registros sintéticos**.
Parte de las 40 filas de la lección anterior, incorpora dos modificaciones y cuatro
registros adicionales. Las fuentes anteriores permanecen intactas. Cada registro
pretende describir un crédito ficticio en un corte, con el
[diccionario de seis campos de 02.04](../04_types_calculated_columns/README.md#1-una-muestra-más-amplia-para-explorar).

La clave de esta tabla es **id_credito + fecha_corte**. Un crédito en dos cortes
distintos puede aparecer dos veces sin violar esa clave. El índice de pandas no
sustituye la clave ni prueba que el negocio tenga registros únicos.

| Regla de la práctica | Qué se exige | Decisión ante incumplimiento |
| --- | --- | --- |
| Campos obligatorios | Los seis campos presentes | Apartar para revisión |
| Tipo numérico | Saldo, pago y días como enteros pequeños | Conservar texto y motivo |
| Rango | Saldo, pago y días no negativos | Rechazar, sin cambiar el signo |
| Catálogo | consumo, servicios, comercio o educacion | Apartar categoría desconocida |
| Relación entre campos | pago_mxn ≤ saldo_mxn | Rechazar, sin recortar el pago |
| Clave | ID y corte presentes, sin repetición | Apartar todas las filas de la clave repetida |

Son reglas didácticas de esta muestra, no reglas universales de crédito. Un pago
superior al saldo podría tener otra interpretación en otro sistema. Aquí se rechaza
porque así se declaró el contrato. "Aceptado" significa que pasó **estas reglas**;
no que se verificó toda la información posible. No comprobamos todavía la validez
calendárica de fecha_corte ni normalizamos espacios, mayúsculas o acentos.

## 2. Ausente, cero e incompatible son situaciones distintas

El [script](quality_rules.py) lee las seis columnas como string. Solo el campo
vacío se interpreta como ausente, con keep_default_na=False y na_values=[""].
Conserva "error", "pendiente" y "no_dato" como textos que deben interpretarse.

```python
print(tabla.isna().sum())       # Ausencias por columna de origen
print(tabla["pago_mxn"].isna()) # Máscara, no los registros mismos
```

isna detecta ausencia; notna detecta presencia. No compares con `== pd.NA` para
detectar faltantes: esa comparación puede devolver un resultado desconocido.

| Caso | Ejemplo | Qué podemos afirmar |
| --- | --- | --- |
| Cero conocido | 028: saldo 0 y pago 0 | Ambos valores existen; cumplen rango y relación |
| Ausencia en origen | 005: saldo vacío | No tenemos una cantidad que evaluar |
| Conversión fallida | 014: saldo "error" | Había texto que no representa el entero requerido |
| Tipo incompatible | 023: días "3.5" | Es número, pero no conteo entero de días |

La conversión sigue los pasos de 02.04: to_numeric, comprobación de parte fraccionaria
y astype("Int64"). Cada cantidad conserva su columna _texto. Las ausencias se
detectan **antes** de convertir: después, tanto "error" como el vacío pueden quedar NA.

## 3. fillna y dropna requieren una decisión

```python
# Ejemplos para discutir políticas; no forman parte de nuestra limpieza
pago_supuesto = tabla["pago_mxn"].fillna("0")
con_pago = tabla.dropna(subset=["pago_mxn"])
```

fillna devuelve valores con ausencias sustituidas. En este ejemplo reemplaza
texto ausente por "0"; no comprueba que realmente no hubo pago. Solo sería adecuado
si la definición de la fuente garantizara ese significado y se registrara la imputación.

dropna selecciona según ausencias; subset delimita qué campos revisar. Sin subset,
podrías perder filas por un campo que ni siquiera es necesario para tu pregunta.
Además, un texto incompatible como "pendiente" está presente: dropna no lo valida.
Ninguna de estas operaciones conserva por sí sola una explicación de lo descartado.

En esta práctica **no imputamos cantidades ni borramos registros**. Separamos las
filas con motivos. Más adelante una corrección debe provenir de evidencia y quedar
documentada, conservando los valores originales.

## 4. Duplicado exacto y clave repetida

```python
exactos = tabla.duplicated(keep=False)
repetidos = tabla.duplicated(subset=["id_credito", "fecha_corte"], keep=False)
print(tabla.loc[repetidos])
```

Sin subset se comparan los valores de todas las columnas de entrada. Con subset
se comparan únicamente los campos de la clave. El índice no participa en esa
comparación. Haz la revisión sobre la entrada, antes de agregar un número de registro
distinto a cada fila: ese nuevo campo haría que las filas completas ya no fueran iguales.

| keep | Filas marcadas dentro de una repetición |
| --- | --- |
| "first" | Todas salvo la primera en el orden actual |
| "last" | Todas salvo la última |
| False | Todas las involucradas |

La primera fila no es automáticamente la más reciente o correcta. Ordenar antes
de eliminar puede cambiar cuál se conserva; se necesita una regla y evidencia.
drop_duplicates elimina según los campos y keep indicados, pero no decide si los
valores son correctos ni genera un registro de resolución.

Aquí los registros 1 y 41 son idénticos: ID 001. Los registros 2 y 42 comparten
ID 002 y corte, pero sus pagos son 200 y 250. Hay **dos filas involucradas en una
repetición exacta** y **cuatro en claves repetidas**, repartidas entre dos claves.
No confundir cantidad de filas marcadas con cantidad de claves o copias adicionales.

Nuestra política es apartar las cuatro filas. No acumulamos ambos pagos ni elegimos
una versión sin evidencia. Para evitar tratar dos claves incompletas como una clave
identificada, el script evalúa repeticiones solo cuando ID y corte están presentes:

```python
clave_presente = trabajo[["id_credito", "fecha_corte"]].notna().all(axis=1)
clave_repetida = clave_presente & trabajo.duplicated(
    subset=["id_credito", "fecha_corte"], keep=False
)
```

all(axis=1) pide que todos los campos de **cada fila** estén presentes.
Una clave incompleta se rechaza por sus campos ausentes, sin asignarle una identidad.

## 5. Construir reglas con máscaras

Después de convertir, trabajo contiene cantidades Int64 y columnas de texto de origen:

```python
reglas = {
    "saldo_mxn_negativo": trabajo["saldo_mxn"] < 0,
    "pago_supera_saldo": trabajo["pago_mxn"] > trabajo["saldo_mxn"],
    "clave_repetida": clave_repetida,
}
banderas = pd.DataFrame(reglas, index=trabajo.index).fillna(False).astype("boolean")
invalido = banderas.any(axis=1)
```

Cada columna de banderas representa una regla; True significa incumplimiento
confirmado. any(axis=1) pregunta si **alguna regla de esa fila** se incumple.
axis=0 operaría por columnas y respondería otra pregunta.

En el script completo también hay banderas de ausencia, incompatibilidad, catálogo
y rango para cada campo requerido. Si un operando falta, una comparación de rango
puede ser NA. fillna(False) se aplica **solo a las banderas de incumplimiento**:
esa comparación no confirmó la falla, pero otra bandera registra la ausencia o
incompatibilidad y rechaza la fila. Nunca rellenamos los importes con cero.

Usar fillna(False) sin esas reglas de obligatoriedad podría aceptar datos que no
se pudieron evaluar. La política funciona porque el conjunto de reglas cubre ambos casos.

## 6. Registrar todos los motivos y separar

El script recorre nombres de reglas y añade su nombre a motivos con loc. Un
separador `; ` aparece entre motivos sucesivos. El ciclo trabaja por regla sobre
Series, sin recorrer filas individualmente.

```python
aceptados = trabajo.loc[~invalido].copy()
rechazados = trabajo.loc[invalido].copy()
```

La tabla de trabajo incluye numero_registro, posición 1 a 44 en la entrada. Es
una referencia de esta carga, no una clave de negocio ni necesariamente una línea
física del CSV: un campo entre comillas podría contener saltos de línea.
El script normaliza el índice de trabajo antes de crear las máscaras y conserva
el número de registro durante la separación.

041, en el registro 43, tiene saldo −100, pago −50 y días −1. Incumple cuatro
reglas: tres rangos y pago_supera_saldo, pues −50 > −100. Conservamos **todos** sus
motivos; no solo el primero. Así una corrección parcial no oculta los demás problemas.

## 7. Comprobar el resultado y sus límites

Resultados conocidos de la muestra sin modificaciones:

| Comprobación | Resultado |
| --- | --- |
| Registros de entrada | 44 |
| Aceptados / rechazados | 29 / 15 |
| Incumplimientos registrados | 19; una fila puede tener varios |
| Saldo interpretable de entrada | 234900 MXN |
| Saldo interpretable aceptado / rechazado | 177250 / 57650 MXN |
| Saldo sin interpretar | 2 registros: 005 y 014 |

44 = 29 + 15 y 234900 = 177250 + 57650. Este último es un **total de valores
interpretables de registros de entrada**, incluyendo repeticiones y negativos;
no es un saldo depurado de créditos únicos. Los dos saldos sin interpretar se
cuentan aparte. Conciliar lo conocido no recupera las cantidades desconocidas.

El programa también reúne aceptados y rechazados con concat, los ordena por
numero_registro y compara con trabajo. concat apila aquí tablas con las mismas
columnas; los detalles de combinar tablas se estudiarán en 08. Esta comprobación
demuestra que no se perdieron ni duplicaron registros durante la partición.

Cada rechazado debe tener motivos, cada aceptado ninguno, y las claves aceptadas
deben ser completas y únicas. Una suma no basta para verificar eso: una pérdida y
una duplicación podrían compensarse. Para una tabla sin saldos interpretables se
usa sum(min_count=1), que devuelve NA en lugar de un cero observado.

Se exportan tres archivos dentro de output:

- aceptados.csv: registros que pasan todas las reglas.
- rechazados.csv: registros apartados, textos originales y motivos.
- reglas_por_registro.csv: número de registro y todas las banderas lógicas.

Cada CSV se relee con sus tipos y se compara exactamente. Solo el campo textual
motivos vacío se restaura a "", porque significa aceptación; no se imputan cantidades.
Las salidas se reemplazan en cada ejecución y no constituyen una escritura atómica
del conjunto: si el programa falla, podrían quedar archivos anteriores o parciales.
Usa las salidas después de ver la confirmación de comprobaciones completas.

## 8. Ejecutar el ejemplo completo

Desde la raíz, con el entorno ya preparado:

### PowerShell

```powershell
# Evaluar reglas, separar y comprobar las tres exportaciones
python curriculum\02_pandas\05_missing_duplicates_rules\quality_rules.py
# Revisar todos los motivos conservados
Get-Content curriculum\02_pandas\05_missing_duplicates_rules\output\rechazados.csv -Encoding utf8
```

### Bash/Zsh

```bash
python curriculum/02_pandas/05_missing_duplicates_rules/quality_rules.py
cat curriculum/02_pandas/05_missing_duplicates_rules/output/rechazados.csv
```

### uv

Con la configuración raíz del proyecto:

```text
uv run --locked python curriculum/02_pandas/05_missing_duplicates_rules/quality_rules.py
```

No hay nuevas dependencias. output permanece ignorado por Git; el CSV de entrada
es fijo y versionado. La función evaluar conserva la tabla fuente sin modificarla.

## Errores frecuentes

| Situación | Qué revisar |
| --- | --- |
| Una ausencia pasa las reglas | Obligatorios registrados antes de rellenar máscaras |
| No aparecen duplicados exactos | Si se agregó un número de registro distinto antes de comparar |
| Cambia la fila conservada al ordenar | Política keep y evidencia para elegir una versión |
| Más motivos que rechazados | Varias reglas pueden afectar al mismo registro |
| Totales que parecen completos | Conteo de saldos sin interpretar y presencia de repeticiones |

<a id="práctica-criterio-de-salida-y-siguiente-paso"></a>

## Práctica

Realiza el [lab 02.05](../../../labs/02_pandas/05_missing_duplicates_rules/README.md) para
justificar reglas y rastrear decisiones, motivos y conteos.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Código, reglas y nota de decisiones | Clave, política de duplicados y motivos por registro | Qué evidencia haría falta para resolver un conflicto |
| Partición aceptados/rechazos y controles | Conteos conciliados y valores originales conservados | Por qué puede haber más motivos que rechazos y qué cantidades siguen desconocidas |

Puedes avanzar cuando expliques la clave y la política de duplicados, rastrees
varios motivos, concilies la partición y distingas lo conocido de lo ausente.

Quien aprende modifica y ejecuta su copia y explica lo que comprobó.
Tu compañero selecciona un registro con varios motivos y pide reconstruir su decisión.
Guarda evidencia, ayudas y dudas en una nota personal junto a tu práctica;
PROGRESS.md registra el desarrollo editorial del curso. El material disponible
no acredita por sí solo aprendizaje completado.

El proyecto de limpieza y sus checkpoints siguen previstos, sin proyecto
asociado implementado ni práctica adicional de proyecto obligatoria.

<a id="referencias-oficiales"></a>

## Referencias

- [Faltantes, detección y tratamiento](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/missing_data.html).
- [duplicated](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.duplicated.html) y
  [drop_duplicates](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.drop_duplicates.html).
- [dropna](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.dropna.html).

## Siguiente paso

Después del lab y su comprobación, continúa con [02.06 — Texto y fechas](../06_text_dates/README.md)
antes de realizar su lab.

[← Módulo 02](../README.md) · [Lab 02.05](../../../labs/02_pandas/05_missing_duplicates_rules/README.md) · [Siguiente →](../06_text_dates/README.md)
