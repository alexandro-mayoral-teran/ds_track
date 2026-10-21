# Lab 09.01 — Distinguir archivo, tabla y biblioteca

## Objetivo y entradas

Aplica la [lección 09.01](../../../curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md)
sin cambiar datos ni instalar paquetes. Recibes dos representaciones de las
mismas 28 observaciones y su inventario, una lectura Parquet documentada y
scripts esenciales de solo lectura en Python estándar/R base.

Elige tu IDE y los intérpretes existentes. Mantén la raíz de DS Track como
directorio para el recorrido R. Para Python, sigue uno de los recorridos completos
de terminal de la lección o ejecuta el archivo en el IDE. No inicialices renv
en la raíz. No hay proyecto ni checkpoint implementado asociado a este lab.

## Actividad

1. Antes de ejecutar, clasifica `base_comun.csv`, Parquet, una tabla Arrow,
   PyArrow, arrow de R, un data.frame y una carpeta con varios cortes. Indica
   cuáles son archivo, formato, representación, biblioteca o posible dataset.
2. Abre el CSV en el editor. Explica por qué `001` debe conservarse como texto,
   por qué el ID aparece dos veces y qué identifica ID/corte. Compara los
   campos del CSV con el esquema de la lectura documentada.
3. Ejecuta el script Python esencial y guarda su resultado como evidencia propia,
   o registra los valores en una nota. Explica la frase de alcance final. No
   presentes una comprobación de firma como si hubieras decodificado el Parquet.
4. En RStudio o tu IDE ejecuta desde la raíz, en Console de R:

```r
source("curriculum/09_arrow_parquet/01_csv_parquet_arrow/inspeccionar_formatos.R", encoding = "UTF-8")
r <- inspeccionar_formatos()
stopifnot(nrow(r$observaciones) == 28L,
          identical(r$resumen$registros, c(14L, 14L)),
          identical(r$resumen$saldo_mxn, c(29000, 31800)))
print(r$inventario)
print(r$alcance)
```

5. Guarda tu script propio en una carpeta de trabajo, reinicia R y ejecútalo
   completo. Repite Python desde otro proceso. Verifica que no se hayan creado
   nuevas muestras ni modificado las entradas.
6. Compara 593 bytes de CSV, 1668 bytes de Parquet y 420 bytes de buffers lógicos
   Arrow de la evidencia. Escribe qué mide cada cantidad y por qué no son tres
   mediciones de RAM. Explica por qué el Parquet pequeño puede ser más grande.
7. Responde: ¿se puede usar el Parquet sin que la aplicación se llame Arrow?
   ¿una tabla Arrow es necesariamente un archivo? ¿un esquema demuestra clave
   única? ¿podrías sumar CSV y Parquet como dos lotes distintos?
8. Redacta entre 100 y 180 palabras para alguien que conoce CSV y quiere saber
   qué aportan Parquet y Arrow. Incluye sus diferencias y una afirmación de
   rendimiento que todavía no puedes sostener con esta muestra.
9. Dibuja los dos primeros registros por filas y por columnas. Para sumar saldo
   por fecha, identifica los campos del cálculo y los que además necesitas para
   validar la clave. Explica por qué seleccionar dos columnas no demuestra haber
   leído menos bytes. Después resuelve tres decisiones: revisar unas filas en
   texto, guardar una tabla tipada para análisis e intercambiar representaciones
   en memoria. Justifica el papel de CSV, Parquet o Arrow en cada caso.

## Comprobación y evidencia

| Elemento | Esperado |
| --- | --- |
| Unidad y clave | Crédito/corte; ID textual más fecha |
| Población | Mismos 14 IDs, 28 observaciones en dos fechas |
| Saldos | 29000 y 31800 MXN; diferencia 2800 MXN |
| Inventario | CSV 593 bytes; Parquet 1668 bytes; huellas coincidentes |
| Inspector esencial | Interpreta CSV; no decodifica Parquet |
| Evidencia de autoría | Lectura Parquet real con PyArrow, esquema y valores conciliados |
| Organización y lectura | Misma información por filas/columnas; selección lógica no demuestra ahorro físico |
| Codificación y compresión | UTF-8, diccionario y Snappy tienen funciones distintas; no corrigen pérdidas previas |
| Sesión nueva | Mismos controles; entradas conservadas |

Conserva la clasificación, tu script/nota, resultados de ambos recorridos y la
explicación. Una sesión puede cubrir solo una parte. La ampliación con PyArrow
ya instalado es opcional; sin ella, atribuye correctamente la lectura documentada
a la autoría. No necesitas instalar una biblioteca para cumplir este lab.

<details>
<summary>Solución razonada y ejemplo de explicación</summary>

CSV y Parquet son formatos; un nombre concreto con ruta identifica un archivo.
PyArrow y arrow de R son bibliotecas; una tabla Arrow o un data.frame son
representaciones en memoria. Una carpeta puede contener archivos de un dataset,
pero necesitamos decidir qué archivos lo forman y con qué esquema se consultan.

En la muestra, 593 y 1668 miden bytes de archivos. Los 420 bytes se refieren a
buffers lógicos de la tabla Arrow leída durante la autoría, no al intérprete
ni a temporales o al pico del proceso. Parquet incluye metadatos: en pocas filas
pueden pesar más que el ahorro de compresión. No se midió velocidad.

Cambiar la extensión no convierte el contenido. Leer `PAR1` no demuestra que
se puedan reconstruir datos y tipos. El inspector esencial contrasta la muestra
contra un inventario conocido; la opción PyArrow sí decodifica y concilia.
Un archivo renombrado o una firma copiada no bastan como formato válido.

Una explicación posible:

> CSV guarda texto y requiere acordar cómo leer identificadores, fechas y
> ausencias. Parquet guarda datos columnares con esquema y metadatos; se necesita
> un lector compatible para reconstruirlos. Arrow aporta una representación
> columnar en memoria y bibliotecas como PyArrow, además de mecanismos de
> intercambio. Leer Parquet puede devolver una tabla Arrow, pero ambos conceptos
> tienen funciones distintas. En esta muestra hay 28 observaciones de los mismos
> 14 créditos, con saldos de 29000 y 31800 MXN. El Parquet ocupa más que el CSV
> pequeño; no puedo deducir por eso cuál será más rápido con millones de filas.
> Compararé claves, tipos e indicadores antes de evaluar tamaños y rendimiento.

El ID individual puede repetirse en fechas distintas; la combinación ID/corte
debe ser única. Un esquema con saldo entero no impide por sí solo un saldo
negativo ni una clave duplicada. Concatenar ambas representaciones duplicaría
la misma población, no añadiría otro corte.

Para sumar saldo por fecha bastan esos dos campos del cálculo; para validar la
identidad de observaciones también se necesita el ID. Parquet permite localizar
bloques por columna, pero el trabajo físico depende del lector y la consulta.
Un CSV pequeño con contrato puede bastar para revisar texto; Parquet conserva
una representación tipada para análisis, y Arrow facilita representaciones e
interfaces de intercambio en memoria. Pueden usarse juntos en un mismo flujo.

UTF-8 codifica caracteres; un diccionario Parquet codifica valores y referencias;
Snappy comprime bloques. Comprimir no convierte texto a tipos, no cifra los datos
ni recupera ceros del ID que se perdieron antes de escribir. Ninguna de estas
decisiones demuestra por sí sola que una consulta sea más rápida.

</details>

## Reflexión, criterio de salida y continuidad

Explica qué significa «conservar los datos» cuando cambian los bytes y los tipos
internos de los objetos. Identifica dos decisiones que deberán formar parte del
contrato en 09.02 y una afirmación que requiere una medición posterior.

Cierra el lab cuando puedas justificar la clasificación, filas/columnas, los controles y los
límites de lo observado. Registra dudas y evidencia real; no se acredita por
consultar la solución. Regresa a la [lección 09.01](../../../curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md).
Siguiente: [09.02 — Esquemas y tipos entre lenguajes](../../../curriculum/09_arrow_parquet/02_schemas_types/README.md).
Los [pendientes de cierre](../../../docs/storage-closure.md)
distinguen esta introducción del módulo completo y del proyecto aún previsto.
