# Lab 08.08 — Guardar, reconstruir y revisar una figura

## Objetivo y entradas

Aplicar la [exportación reproducible](../../../curriculum/08_visualization_r/08_reproducible_export/README.md)
con una entrega nueva y una justificación de tamaño y formato. Recibes el
CSV conservado `datos/cartera_texto.csv`, las funciones del mismo proyecto
renv y el [script de referencia](../../../curriculum/08_visualization_r/08_reproducible_export/exportar_figuras.R).
No se modifican paquetes, metadatos ni entregas anteriores.

Trabaja en RStudio o tu IDE, desde la raíz de la práctica. Guarda una copia
del script como `output/mi_exportacion_lab.R`, usando otro nombre si existe.
Ejecuta bloques en Console de R. El recorrido esencial no necesita terminal,
SVG, PDF ni publicar archivos. No hay checkpoint integrador implementado.

## Actividad

1. Define el destino de lectura: documento o pantalla, espacio disponible y
   formato elegido. Justifica PNG para esta práctica sin afirmar que siempre
   sea el mejor formato. Predice los píxeles para 9 × 6 pulgadas a 144 dpi.
2. Reinicia R, carga tu script y exporta a una carpeta nueva:

```r
source("output/mi_exportacion_lab.R", encoding = "UTF-8")
exportar_visual("output/exportacion_0808_lab")
```

3. Desde Files o el explorador abre la imagen, el resumen y la configuración.
   Explica qué representa cada barra, qué población cubre y por qué no muestra
   todos los aceptados. Comprueba título, acentos, fechas, MXN y nota al tamaño
   de uso. La descripción textual debe acompañar el hallazgo.
4. Comprueba la entrega sin reescribirla y comprueba que no admite reemplazarla:

```r
verificar_exportacion("output/exportacion_0808_lab")
intento <- try(exportar_visual("output/exportacion_0808_lab"), silent = TRUE)
stopifnot(inherits(intento, "try-error"))
```

`try` permite observar un error esperado sin interrumpir toda la práctica.
Aquí se usa para comprobar la protección del destino, no para ocultar fallos
imprevistos. La carpeta anterior debe permanecer intacta.

5. Guarda tu archivo, reinicia R y ejecuta el siguiente bloque completo:

```r
source("output/mi_exportacion_lab.R", encoding = "UTF-8")
verificar_exportacion("output/exportacion_0808_lab")
exportar_visual("output/exportacion_0808_lab_reconstruida")
a <- leer_csv_visual("output/exportacion_0808_lab/datos_figura.csv")
b <- leer_csv_visual("output/exportacion_0808_lab_reconstruida/datos_figura.csv")
stopifnot(identical(lapply(a, identity), lapply(b, identity)))
```

Se comparan columnas, sin equiparar punteros internos del lector CSV. Repite
la comparación para `base_comun.csv` y explica por qué el código debe poder
reconstruir sin depender del objeto `preparado` de otra sesión.

6. Describe qué detectaría una modificación del PNG y qué detectaría un cambio
   compensado entre dos saldos que mantuviera el total. Explica por qué ni las
   huellas ni las dimensiones certifican legibilidad. No alteres la fuente
   ni la entrega para hacer el experimento; puedes usar la copia en memoria
   de la solución.

## Ampliaciones opcionales

- Exporta a otro destino con `dpi = 288`. Predice 2592 × 1728 píxeles. Compara
  datos y pulgadas, y mira ambos PNG al mismo tamaño de uso. Explica por qué
  no se arreglaría un título recortado aumentando solo dpi.
- Si `capabilities("cairo")` es verdadero, exporta a otra carpeta con
  `vectoriales = TRUE`. Abre SVG/PDF y revisa sus notas y tamaños. Si no está
  disponible, registra la limitación y conserva la entrega PNG esencial.
- Diseña cómo exportarías una composición de 08.07: objeto explícito,
  dimensiones y disposición. Justifica el espacio de las notas; no basta
  usar las mismas pulgadas de una figura simple sin revisarlas.

## Resultado, comprobación y evidencia

| Resultado | Comprobación esperada |
| --- | --- |
| PNG de referencia | 1296 × 864 píxeles, fondo blanco, etiquetas completas |
| Dos filas resumidas | 14 IDs; 29000/31800 MXN; 18 aceptados por corte |
| Tabla de pares | 14 IDs, dos saldos y diferencia; mismos integrantes |
| Configuración | 9 × 6 pulgadas, 144 dpi, sin vectoriales en el esencial |
| Verificador | Reconstrucción, huellas y dimensiones sin errores |
| Sesión nueva | Mismos datos y configuración; otro destino conservado |

Entrega el script propio, las dos carpetas, una nota de revisión visual y
entre cinco y ocho frases que justifiquen formato, tamaño, población y límites.
Registra la ejecución desde sesión nueva. No basta una captura de Plots ni
el mensaje «archivo creado». No compares los diagnósticos de sesión como si
fueran tablas de indicadores que debieran ser idénticas.

<details>
<summary>Solución razonada: píxeles y límites de los controles</summary>

El PNG inicial tiene 9 × 144 = 1296 píxeles de ancho y 6 × 144 = 864 de alto.
Duplicar dpi conserva 9 × 6 pulgadas y duplica ambas dimensiones en píxeles.
El lienzo físico sigue siendo el mismo; no hay espacio adicional para una nota.

Para comparar pares de las dos entregas, sin modificar archivos:

```r
pares_a <- leer_csv_visual("output/exportacion_0808_lab/base_comun.csv")
pares_b <- leer_csv_visual("output/exportacion_0808_lab_reconstruida/base_comun.csv")
stopifnot(identical(lapply(pares_a, identity), lapply(pares_b, identity)))
alterados <- pares_b
alterados$saldo_sep <- as.numeric(alterados$saldo_sep)
alterados$saldo_sep[1:2] <- alterados$saldo_sep[1:2] + c(100, -100)
stopifnot(sum(alterados$saldo_sep) == sum(as.numeric(pares_a$saldo_sep)),
          !identical(as.numeric(pares_a$saldo_sep), alterados$saldo_sep))
```

La suma sigue siendo 29000, pero cambian dos saldos individuales. El verificador
compara columnas completas de los pares contra la reconstrucción de la fuente;
la igualdad del total no bastaría. Si cambia un archivo de la entrega, también
debe fallar la huella que se conservó al exportar.

Eso no detecta por sí solo un título demasiado pequeño, un texto recortado
o una mala decisión de escalas. El manifiesto registra lo que se escribió;
no juzga la calidad visual ni prueba que nadie haya editado el manifiesto.
La revisión del archivo al tamaño de uso sigue siendo parte del trabajo.

Una justificación posible: «Elijo PNG para insertar esta figura en un documento.
La genero a 9 × 6 pulgadas y 144 dpi; revisaré sus 1296 × 864 píxeles al tamaño
de uso. Representa los mismos 14 IDs, con saldos de 29000 y 31800 MXN. La base
cubre 14/18 aceptados por corte, con datos sintéticos y alcance descriptivo.
Conservo tabla, pares, configuración y descripción para revisar el resultado.
Reconstruyo desde otra sesión en una carpeta nueva y compruebo la lectura final».

</details>

## Reflexión y criterio de salida

Explica qué ocurriría si el último gráfico mostrado fuera otro, por qué `plot`
lo evita y qué tendrías que cambiar si las notas no caben al tamaño previsto.
Distingue «misma tabla», «mismas dimensiones» y «mismos bytes».

Cierra cuando puedas reconstruir, justificar las decisiones y revisar tanto
valores como archivo final. Conserva dudas y evidencia de tu práctica: las
nueve secciones tienen material, pero eso no acredita aprendizaje.
Siguiente lección: [08.09 — Cierre visual y comparación con Python](../../../curriculum/08_visualization_r/09_visual_comparison/README.md).
Volver a la [lección 08.08](../../../curriculum/08_visualization_r/08_reproducible_export/README.md).
