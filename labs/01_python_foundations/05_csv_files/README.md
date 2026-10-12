# Lab 01.05 — Del archivo de entrada a una salida comprobable

## Relación y entrada

- Lección: [Archivos CSV](../../../curriculum/01_python_foundations/05_csv_files/README.md).
- Entrada: ventas_entrada.csv y csv_pipeline.py de esa lección.
- Proyecto: todavía no aplica.

Reserva 40 a 60 minutos; puedes dividir lectura y escritura en dos sesiones.
Consulta las soluciones después de predecir e intentar. No necesitas instalar paquetes.

## Parte A — Interpretar y ejecutar

1. Abre la entrada como texto e identifica encabezado y tres registros.
2. Explica por qué lápiz, azul es un solo campo.
3. Predice importes y total; ejecuta el script.
4. Revisa la salida y comprueba que se conserva el producto completo.

<details>
<summary>Ver solución de la parte A</summary>

Las comillas delimitan un campo que contiene una coma. Los importes son 80,
50 y 35, total 165 MXN. Entrada y salida tienen tres registros; la salida agrega
importe_mxn. DictReader interpreta los campos numéricos como texto antes de
que preparar_ventas los convierta.

</details>

## Parte B — Utilizar otra entrada conservando la original

1. Haz una copia local de ventas_entrada.csv dentro de output, llamada ventas_practica.csv.
2. Agrega rotulador, 3 unidades, precio 30 a esa copia.
3. En main, cambia ruta_entrada para leer la copia y ruta_salida para escribir
   output/ventas_practica_con_importe.csv. Mantén rutas distintas.
4. Predice y comprueba cuatro registros y su total. Revisa que la entrada original no cambió.

<details>
<summary>Ver una solución de la parte B</summary>

En main, mantén carpeta_leccion y sustituye las dos rutas:

```python
ruta_entrada = carpeta_leccion / "output" / "ventas_practica.csv"
ruta_salida = carpeta_leccion / "output" / "ventas_practica_con_importe.csv"
```

Agrega a la copia:

```csv
rotulador,3,30
```

El registro nuevo vale 90 y el total es 255 MXN. Copia y agrega con el editor,
sin duplicar el encabezado. Crea la copia después de ejecutar la parte A, que
genera la carpeta output. Los mensajes de cantidad y total deben reflejar el
nuevo contenido; adapta también el mensaje de presentación si lo necesitas.

</details>

## Parte C — Comprobar una repetición

1. Ejecuta otra vez con las mismas entradas.
2. Comprueba que hay un solo encabezado y cuatro registros, no ocho.
3. Explica qué hizo el modo w y qué habría ocurrido si la salida fuera la entrada.

<details>
<summary>Ver respuesta orientativa de la parte C</summary>

w reemplaza el contenido de la salida. No agrega ventas de una ejecución anterior.
Si hubieras escrito sobre la entrada, perderías su contenido original. El ejemplo
evita esa situación usando nombres distintos para entrada y salida.

</details>

## Parte D — Reconocer una entrada que no se puede convertir

1. En la copia de práctica cambia una cantidad por `tres`.
2. Predice, ejecuta y localiza el error.
3. Comprueba que no se anunció una ejecución correcta y que la salida previa
   no debe confundirse con un resultado de los datos modificados.
4. Corrige a un entero válido y vuelve a ejecutar.

<details>
<summary>Ver respuesta orientativa de la parte D</summary>

int no convierte tres y produce ValueError. La transformación termina antes de
abrir la salida, que conserva la ejecución anterior si ya existía. Su existencia
no acredita que los datos nuevos se procesaron correctamente. Al corregir y
ejecutar, vuelve a comprobar cantidades y total.

</details>

## Extensión opcional — Otra forma de delimitar

En otra copia, utiliza punto y coma entre campos y ajusta el delimiter del lector.
La coma del nombre lápiz, azul pertenece al producto. Predice por qué leer esa
copia con separador coma produciría un encabezado diferente.

## Evidencia y reflexión

- Conserva código y una nota con entrada, salida, cantidad de registros y total.
- ¿Qué hace with al salir del bloque, incluso con un error?
- ¿Por qué int es necesario después de leer los campos?
- ¿Qué informa fieldnames al lector y al escritor?
- ¿Por qué contar líneas no siempre cuenta registros CSV?
- Si usas Git, revisa el script y registra la modificación; output está ignorado.
  Las entradas originales versionadas no deben modificarse para esta práctica.

## Siguiente paso

06 — Validación y resumen está por desarrollar. Consulta el
[índice de Python fundamental](../../../curriculum/01_python_foundations/README.md).
