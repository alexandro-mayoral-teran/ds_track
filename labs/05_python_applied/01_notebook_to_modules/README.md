# Lab 05.01 — Del notebook a módulos

## Propósito, entradas y preparación

Lee la [lección 05.01](../../../curriculum/05_python_applied/01_notebook_to_modules/README.md)
y completa el cierre 04.09 con sus prerrequisitos. Vas a explicar y comprobar
una reorganización que conserva la pregunta, los valores y las ausencias.

**Entradas:** medidas_demo.py, paquete analisis_cartera, ejecutar.py,
exploracion.ipynb y los CSV sintéticos de SQL 03.01. Si conservas tu entrega
de 04.09, compara sus tablas sobre las mismas fuentes. **Resultado:** mapa de
responsabilidades, entrega modular, notebook ejecutado y explicación propia.
No hay proyecto/checkpoint implementado asociado todavía.

Tres sesiones orientativas de 45–75 minutos: A/B, C y D/E. Usa el shell y
entorno elegidos según los recorridos completos de la lección. Trabaja desde
curriculum/05_python_applied/01_notebook_to_modules; conserva todos los
ejemplos, fuentes y entregas anteriores. Guarda notas y variantes en una carpeta
nueva dentro de output, que está ignorada. No copies rutas personales al notebook.

## A. Ejecutar e importar un módulo

1. Lee medidas_demo.py. Señala qué instrucciones están al nivel superior,
   cuáles en resumir_saldos y cuáles en main.
2. Ejecuta `python -c "import medidas_demo"`. Después `python medidas_demo.py`.
   Registra qué imprime cada uno y explica la diferencia.
3. En Python o una celda importa el módulo y llama a la función con
   `[0, 100, None, 300]`, `[]`, `[None, None]` y `[0, 1]`.
4. Prueba `from medidas_demo import resumir_saldos`; explica qué nombre
   puedes usar directamente y cuál no fue incorporado por esa instrucción.
5. Muestra `medidas_demo.__name__` y `medidas_demo.__file__` después de
   `import medidas_demo`. Explica para qué sirve cada dato.

**Comprobación:** importar no imprime la demostración. Ejecutar sí imprime
el diccionario: 4 registros, 3 conocidos, mediana 100, cobertura 75 %.
**Evidencia:** resultados y explicación de la protección de entrada.

<details>
<summary>Ver solución razonada de A</summary>

El import de statistics y las definiciones están al nivel superior. Definir
main no ejecuta su cuerpo; la condición final llama main solo cuando el archivo
es la entrada principal. Importar medidas_demo establece su nombre como
medidas_demo, por lo que no cumple la condición.

| Entrada | Registros | Conocidos | Mediana | Cobertura |
| --- | ---: | ---: | ---: | ---: |
| `[0, 100, None, 300]` | 4 | 3 | 100 | 75 % |
| `[]` | 0 | 0 | None | None |
| `[None, None]` | 2 | 0 | None | 0 % |
| `[0, 1]` | 2 | 2 | 0.5 | 100 % |

`from medidas_demo import resumir_saldos` permite usar ese nombre sin prefijo;
no incorpora el nombre medidas_demo a una sesión nueva. Si ya hiciste el otro
import, ese nombre puede seguir en tu sesión: comprueba en una sesión limpia.
__name__ muestra la identidad del módulo; __file__ su archivo de procedencia.

</details>

## B. Explicar las responsabilidades del paquete

1. Dibuja la relación de ejecutar.py, __main__.py, flujo, entrada,
   transformación, comprobación y presentación. Indica qué llama a qué.
2. Escribe entradas y resultados de read_detail, summarize, build_analysis y export.
3. Busca una importación relativa y otra absoluta; explica su punto de partida.
4. Señala dónde decidirías otro color, otro corte y otra carpeta de fuentes.
5. Explica por qué comprobacion.py no llama a summarize para su referencia.

**Resultado:** mapa con responsabilidades y dependencias. **Comprobación:**
el cálculo no importa al consumidor; cambiar color no requiere cambiar mediana.

<details>
<summary>Ver solución razonada de B</summary>

ejecutar.py llama main del paquete; main elige rutas y llama export. El flujo
lee mediante entrada, calcula con transformación, concilia con comprobación
y construye figuras/informe con presentación. Las reglas compartidas viven
en reglas.py. __init__.py no dispara ninguna de esas acciones.

read_detail recibe carpeta y devuelve detalle validado. summarize recibe
detalle/fecha y devuelve detalle del corte/resumen. build_analysis recibe
carpeta/fecha y devuelve cinco tablas conciliadas. export recibe además
destino/resolución, escribe una carpeta nueva y devuelve las tablas.

`from .entrada import read_detail` parte del paquete actual;
`from analisis_cartera.flujo import build_analysis` nombra el paquete completo.
Los colores pertenecen a presentación. Fecha/fuentes se pasan al flujo;
la entrada principal conserva valores iniciales por ahora. La referencia CSV
calcula por un camino independiente, reduciendo el riesgo de repetir un mismo
error de transformación en ambos resultados.

</details>

## C. Construir y cotejar la entrega modular

1. Importa analisis_cartera.flujo sin llamar ninguna función. Comprueba que
   no se crea output/entrega_modular ni aparecen figuras o resultados.
   Si esa carpeta ya existe, registra su estado antes/después del import.
2. Ejecuta `python -m analisis_cartera` una vez. Si ya existe la entrega,
   usa export desde Python con un destino nuevo como en la solución.
3. Revisa indicadores.csv, referencia_csv.csv y las 20 filas de conciliacion.csv.
   Contrasta con tu 04.09 sobre las mismas fuentes y fecha.
4. Abre Matplotlib PNG/SVG y Altair HTML con conexión; coteja valores,
   etiquetas, ausencias y unidades con resumen.csv.
5. Repite la llamada con el mismo destino y explica FileExistsError.
   Comprueba que las fuentes y la entrega anterior siguen intactas.
6. Reconstruye usando fuentes/ de la nueva entrega y otro destino.

**Comprobación:** 24 registros, 21 conocidos, mediana global 2300 MXN y
cobertura global 87,5 %. Educación: 3 registros, 0 conocidos, mediana ausente
y cobertura 0 %. El saldo cero sigue siendo conocido. **Evidencia:** tablas
comparadas, explicación de ausencias y revisión visual con un hallazgo y un límite.

<details>
<summary>Ver solución razonada de C</summary>

Desde Python en la carpeta de la lección, una alternativa con destinos nuevos:

```python
from pathlib import Path
from analisis_cartera.flujo import export

lesson = Path.cwd()
source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"
tables = export(source, "output/lab_modular")
rebuilt = export("output/lab_modular/fuentes", "output/lab_reconstruccion")
```

Comercio: mediana 3100 sobre 5/5; consumo: 1750 sobre 10/10;
servicios: 2550 sobre 6/6. Las tres coberturas son 100 %. Educación conserva
su categoría con ausencia de mediana. La mediana global proviene de los 21
saldos del detalle; no es una agregación de medianas.

La importación no llama export. Ambas entradas explícitas llaman el mismo
main y usan la misma carpeta inicial. Si existe, mkdir con exist_ok=False
detiene la escritura: conserva la entrega, pero exige elegir otro destino
para una ejecución posterior. entrega.json se escribe al final; una interrupción
puede dejar archivos parciales, que deben identificarse al revisar.

Las imágenes pueden variar en bytes; deben conservar valores, bases y
mensajes. La revisión visual no se acredita automáticamente por la conciliación.

</details>

## D. Usar las mismas funciones en un notebook limpio

1. Abre exploracion.ipynb con el kernel adecuado y comprueba intérprete/carpeta.
2. Reinicia el kernel y ejecuta todas las celdas en orden.
3. Identifica dónde se importa build_analysis y dónde se llama. Comprueba
   que el notebook no contiene otra definición de summarize.
4. Selecciona un corte inexistente como `2026-11-30` en una celda de exploración.
   Describe la diferencia entre no tener registros y tener saldos ausentes.
5. Recupera octubre, reinicia y ejecuta todo antes de conservar tu copia.
   Limpiar resultados visibles es otra operación y no reinicia el kernel.

**Resultado:** notebook ejecutable desde el comienzo, reutilizando el paquete.
**Evidencia:** tabla, figura y explicación propia sobre caché y orden de ejecución.

<details>
<summary>Ver solución razonada de D</summary>

El notebook importa build_analysis de flujo.py y delivery_figure de
presentacion.py. La misma transformación interviene en ambos consumidores;
el notebook muestra el resultado y no escribe otra entrega por defecto.

En un corte vacío cada segmento tiene 0 registros/0 conocidos, con mediana
y cobertura no definidas. En octubre educación tiene registros y cobertura
0 %, pero sigue sin mediana. Cero conocidos no equivale a saldo cero.

Una sesión puede conservar la primera versión de un módulo importado. Reiniciar
el kernel y ejecutar todo carga el archivo actual y descubre variables que
antes solo existían por celdas ejecutadas fuera de orden.

</details>

## E. Extraer una función por tu cuenta

En una carpeta nueva dentro de output, crea tu variante de un módulo y un
consumidor. Extrae una función pequeña que calcule conocidos/registros desde
una lista; pasa la entrada como argumento, retorna el resultado y protege la
demostración con `if __name__ == "__main__"`. No modifiques el ejemplo curado.

Comprueba lista vacía, todo ausente, cero y una mediana de medio MXN. Importa
desde tu consumidor y desde una sesión iniciada en esa carpeta. Explica qué
acción querías evitar al importar y por qué creaste ese archivo.

<details>
<summary>Ver orientación razonada de E</summary>

Una función puede reutilizar las reglas del pequeño medidas_demo, pero debe
expresar entradas/salidas y conservar el cero. La demostración llama la función
solo bajo la condición de entrada. Basta un módulo para este ejercicio;
crear una jerarquía de paquetes no aporta claridad por sí mismo.

</details>

## Reflexión y criterio de salida

- ¿Qué ejecuta Python al importar y qué protege la condición de entrada?
- ¿Qué cambió en la organización y qué evidencia muestra resultados conservados?
- ¿Por qué abrir otra carpeta y activar otro entorno resuelven problemas distintos?
- ¿Qué podría seguir equivocado aunque las 20 conciliaciones coincidan?

Registra resultados, revisión visual, dudas y siguiente paso en tu bitácora personal junto a la práctica.
Puedes avanzar cuando expliques esas decisiones y uses el mismo cálculo desde
script/notebook sin editar sys.path ni depender de variables ocultas.

Continúa con la [siguiente lección, 05.02 — Configuración y registro](../../../curriculum/05_python_applied/02_configuration_logging/README.md).
Volver a la [lección 05.01](../../../curriculum/05_python_applied/01_notebook_to_modules/README.md).
