# Copia de estructura y configuración 14.02

Esta carpeta es una práctica de organización: reúne 13 archivos útiles, una
fuente sintética y el contrato 1401-v1. No contiene aún reporte/app integrados,
pipeline, entorno bloqueado o checkpoints de proyecto. Python estándar o R base
bastan para revisar la consulta. No necesitas practicar ambas alternativas.

## Responsabilidades

| Ruta | Responsabilidad |
| --- | --- |
| docs/ | Pregunta, contrato y plantilla personal de 14.01 |
| datos/entrada/cartera.csv | Entrada preservada: seis filas, clave ID/corte |
| referencia/criterios.csv | Expectativas conocidas, no entrada de producción |
| config/consulta.csv | Parámetros explícitos y rutas relativas a esta raíz |
| codigo/modelo.py y modelo.R | Contrato de fuente y cálculo reutilizable |
| codigo/configuracion.py y configuracion.R | Leer claves, tipos y rutas; rechazar configuraciones ambiguas |
| revisar.py y revisar.R | Coordinar lectura/configuración y mostrar una consulta |
| salidas/ | Destinos regenerables previstos; lee su LEEME |

## Revisar

Python, desde cualquier carpeta, usando la ruta real al script:

```text
python ruta/a/esta/carpeta/revisar.py
```

En consola R del IDE, desde la raíz de esta copia:

```r
source("revisar.R")
revisar_proyecto(".")
```

Si el directorio actual es otro, carga revisar.R por su ruta real y pasa la raíz
explícita a revisar_proyecto. No modifica getwd ni depende de objetos anteriores.
Referencia comprobada: Python 3.12.12 y R 4.6.1, sin paquetes externos.

El caso inicial octubre/ambos/2000 debe mostrar 003=2600 MXN, universo 3/4600
y cobertura 100/3. App=shiny registra una elección; no inicia ni instala Shiny.
Cambiarla a streamlit tampoco cambia los indicadores o crea otra aplicación.

## Formato de configuración

CSV UTF-8 con encabezado clave,valor. Siete claves obligatorias, únicas y sin
extras. No se completan valores ausentes con defaults ocultos. Cada valor se
lee como texto antes de validar; minimo_texto=2000 no es lo mismo que 2000.0.

version_reglas solo admite 1401-v1; corte debe ser fecha válida 1900–2100;
segmentos admite comercio, servicios, ambos separados por | o ninguno;
minimo_texto es entero canónico 0..1000000; app es shiny o streamlit.
La regla >= y el denominador pertenecen al código/contrato, no son filtros
editables para alterar silenciosamente el significado de una medida.

entrada debe identificar un CSV existente bajo datos/entrada/. salida usa
salidas/nombre_simple, con nombre minúsculo que empiece por letra y contenga
letras, dígitos, _ o -, hasta 40 caracteres. Debe estar libre. Rutas relativas
a esta raíz, con /, sin .., puntos aislados, unidades Windows o rutas personales.
No son relativas a config/ ni a la terminal. Se comprueban rutas existentes
resueltas dentro de la raíz; son reglas de esta práctica, no un aislamiento
del sistema frente a código no confiable o cambios concurrentes.

## Variantes sin modificar código

Copia config/consulta.csv como config/septiembre.csv, cambia corte a 2026-09-30
y salida a salidas/septiembre. Conserva otras claves. Después:

```text
python revisar.py --config config/septiembre.csv
```

O en R:

```r
revisar_proyecto(".", "config/septiembre.csv")
```

Resultado: 002=2000 y 003=2500, 4500 MXN y 2/3. Ninguno produce selección
vacía sobre universo; noviembre no publica medidas; parámetros inválidos
detienen la revisión de configuración con diagnóstico. Es un rechazo antes
del cálculo, no una simulación de mensajes/estado de una app anterior.

Los revisores solo leen e imprimen; Python desactiva escritura de bytecode en
su punto de entrada. No crean/reservan el destino, instalan paquetes ni generan
productos. Preserva fuente y contrato. Conservar configuración explícita ayuda
a revisar qué se pidió, pero aún no es un registro histórico de ejecución.
