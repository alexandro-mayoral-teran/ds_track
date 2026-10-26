# Entrega de cierre 11.09

Esta carpeta reúne fuentes, parámetros y configuración para generar un reporte
HTML por corte. Cada fila de cartera.csv es un crédito ficticio en una fecha
exacta. Se requieren siete observaciones: 001/002/003 en septiembre y octubre
de 2026, y 004 solo en octubre. Saldos enteros de 0 a 1000000 MXN, sin ausencias.
La selección aplica saldo mayor o igual al mínimo y la proporción cuenta créditos
del corte. Las barras universo/selección se superponen y no se suman.

1. Inspecciona cartera.csv, parametros.json y las funciones. No cambies un
   resultado manualmente para que concuerde con otra fuente.
2. Prepara el entorno del motor de esta copia y comprueba Quarto. No se incluyen
   intérpretes, bibliotecas, credenciales ni una configuración global.
3. Construye desde esta raíz. Python: `python construir.py --quarto quarto`.
   R: abre cierre.Rproj, reinicia y restaura si hace falta con
   `source("restaurar.R")`; después `source("construir.R")` y
   `construir_reporte(quarto = "quarto")` en la consola R.
4. La construcción crea reporte.html, salida/, registro del comando y huellas.
   Rechaza resultados existentes. Si falla, conserva esa copia y su registro;
   corrige los fuentes en una copia nueva para volver a construir.
5. Comprueba contra un CSV de referencia conservado fuera de esta carpeta:
   `python verificar.py . RUTA_REFERENCIA --fecha 2026-09-30 --minimo 2000`.
   Ajusta los argumentos al corte/mínimo esperado. No basta usar la fuente de
   esta carpeta como su propia referencia externa.
6. Abre el HTML final y revisa texto, ambas tablas, figura y navegación.

Para Python, pyproject.toml y uv.lock son la instantánea de configuración del
curso, no un entorno mínimo. Puedes reconstruirla con `uv sync --locked --group
notebooks --python 3.12.12`, usando un UV_PROJECT_ENVIRONMENT local nuevo.
Ejecuta construir.py con ese Python. No mezcles gestores sobre el mismo entorno.
En R se conservan DESCRIPTION y renv.lock de 11.03 con estado/biblioteca locales.
La restauración puede necesitar Internet; construir no instala paquetes.

Para repetir sin resultados anteriores, copia únicamente los fuentes listados
por `fuentes(motor)` en verificar.py a una carpeta nueva. El comando
`python copiar_fuentes.py . ../reconstruccion --motor python` (o `--motor r`)
conserva también las subcarpetas renv en R. No copies salida/, reporte.html, huellas, logs, .quarto, _freeze,
cachés, .venv ni .renv-local. R requerirá restaurar su biblioteca en la copia.
Python puede reutilizar un entorno adecuado o reconstruirlo desde el lockfile.

Un HTML legible no demuestra recálculo. Huellas MD5, logs y versiones declaradas
ayudan a revisar coherencia, pero no autentican ejecuciones históricas ni al
autor. El verificador contrasta archivos y valores; no certifica significado
editorial, accesibilidad completa o los píxeles de la figura. Hay que revisar.
