# Entrega local reconstruible — DS Track 14.08

Consulta ENTREGA.csv para elegir Python/Streamlit o R/Shiny; basta una ruta.
fuentes/ contiene 60 archivos de datos sintéticos, contrato, configuraciones,
código, pruebas, metadatos e instrucciones. muestra/ conserva tres consultas y
tres reportes ya preparados para comparar: no acredita ejecución en tu equipo.
El paquete tiene 90 archivos; MANIFIESTO.csv registra los otros 89, sin firmarlos.

La clave es ID/corte y el saldo se expresa en MXN enteros. Octubre selecciona
003/2600 sobre universo 3/4600; septiembre 002/2000 y 003/2500 sobre 3/4500;
vacío conserva universo válido y cero seleccionados. Coberturas: 1/3, 2/3 y 0%.
El contrato está en fuentes/docs/ESPECIFICACION.md.

## Antes de ejecutar

Usa herramientas del revisor obtenidas de una copia revisada de DS Track 14.08,
fuera del paquete, y un CSV original de referencia conservado por separado.
El revisor comprueba inventario, fuente por clave/campo, filtros y resultados
sin ejecutar código recibido. Cada revisor comprueba su ruta, no la contraria.
No autentica procedencia ni aprueba todo el código, HTML o accesibilidad.

Copiar fuentes solo lee y copia; no instala ni ejecuta. Revisa código y metadatos
copiados antes de restaurar o abrir un proyecto que ejecute .Rprofile. No copies
un entorno instalado ni muestra/ para simular una reconstrucción.
Python 3.12.12, R 4.6.1 y Quarto 1.9.38 son las versiones comprobadas.

Los nombres siguientes son ejemplos: adapta las rutas y elige destinos nuevos.
Si una operación falla, conserva la evidencia; no renueves huellas para forzar
aprobación. La presencia del manifiesto no demuestra que el constructor terminó.

## Ruta R/Shiny en el IDE

Desde las herramientas revisadas, en consola R:

```r
source("entrega.R", encoding = "UTF-8")
verificar_entrega("../paquete_shiny", "datos/entrada/cartera.csv")
copiar_fuentes("../paquete_shiny", "../reconstruida", "datos/entrada/cartera.csv")
```

Revisa las fuentes copiadas. Después abre producto_1408.Rproj de la copia nueva,
reinicia sin workspace, confirma getwd() y ejecuta desde su raíz:

```r
source("restaurar.R", encoding = "UTF-8")
source("reconstruir.R", encoding = "UTF-8")
reconstruir_producto(".")
```

Se esperan siete grupos aprobados, tres consultas y tres reportes HTML nuevos.
Compara reportes/ con muestra/ del paquete. Si Quarto no se detecta, indica
quarto= con su ruta. No se instala automáticamente.

Abre después interfaz/r/interfaz_1407.Rproj, cuyo nombre se conserva de 14.07.
Reinicia y ejecuta desde interfaz/r:

```r
source("restaurar.R", encoding = "UTF-8")
source("iniciar.R", encoding = "UTF-8")
iniciar_app(puerto = 8861, abrir = TRUE)
```

Aplica octubre, septiembre y vacío y compara con los reportes. Sin universo
debe rechazar y retirar cifras. Detener/Esc en el IDE o Ctrl+C terminan el servidor.

## Ruta Python/Streamlit en PowerShell

Desde las herramientas revisadas:

```powershell
python entrega.py verificar ../paquete_streamlit --referencia datos/entrada/cartera.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega." }
python entrega.py copiar ../paquete_streamlit ../reconstruida --referencia datos/entrada/cartera.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar copia." }
```

Revisa las fuentes copiadas antes de ejecutar. Después:

```powershell
Set-Location ../reconstruida
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python reconstruir.py
if ($LASTEXITCODE -ne 0) { throw "Revisar reconstruccion." }
```

Compara los tres HTML de reportes/ con muestra/ del paquete. Indica --quarto
con la ruta si no se detecta. Después restaura e inicia la interfaz:

```powershell
Set-Location interfaz/python
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar interfaz." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860, aplica los casos y compara contexto y valores.
El borrador no cambia la consulta aplicada; un rechazo retira cifras. Ctrl+C
detiene el servidor.

## Ruta Python/Streamlit en Bash

Desde las herramientas revisadas:

```bash
python entrega.py verificar ../paquete_streamlit --referencia datos/entrada/cartera.csv || exit 1
python entrega.py copiar ../paquete_streamlit ../reconstruida --referencia datos/entrada/cartera.csv || exit 1
```

Revisa las fuentes copiadas antes de ejecutar. Después:

```bash
cd ../reconstruida || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python reconstruir.py || exit 1
```

Compara los tres HTML de reportes/ con muestra/ del paquete. Indica --quarto
con la ruta si no se detecta. Después restaura e inicia la interfaz:

```bash
cd interfaz/python || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860 y compara los casos y transiciones. Ctrl+C detiene
la app. Estos comandos no acreditan una ejecución en Linux/macOS.

## Qué comparar y qué queda pendiente

Revisa IDs/saldos, corte, segmentos, mínimo, reglas, universo y cobertura.
Las horas de comprobación pueden cambiar; si cambian bytes, las huellas pueden
diferir. Los valores por crédito deben conciliar. Sin universo no hay entrega.

El lockfile no contiene instaladores: restaurar puede necesitar red o cachés
adecuados. No hay garantía offline, firma, despliegue ni transacción completa.
Se conserva cualquier carpeta parcial y se exige otra copia nueva para repetir.
La lista de archivos no limpia contenido privado insertado en un archivo permitido.

fuentes/CI_EJEMPLO.yml no está activo y no se copia automáticamente a workflows.
La reconstrucción independiente y defensa de decisiones se revisan en 14.09;
recibir esta carpeta no acredita aprendizaje ni un cierre del módulo.
