# Producto de práctica 14.07

Elige una ruta: Python/Streamlit o R/Shiny. No necesitas entregas previas.
Los preparadores reúnen las fuentes; no instalan. La raíz conserva el entorno
de cálculo mínimo de 14.03–14.06. Cada interfaz tiene su propio entorno local
bajo interfaz/python o interfaz/r; solo restaura la elegida. .renvignore evita
atribuir las dependencias de esas interfaces al proyecto R de cálculo.

En raíz, produce las entregas de config/octubre.csv, septiembre.csv y vacio.csv
mediante trazar.py / trazar.R. Cada configuración declara la app elegida.
Sin universo no produce entrega. El lector integracion.py / integracion.R
reconstruye las tablas esperadas con el mismo modelo y comprueba los cuatro
archivos finales sin escribir ni crear salidas ausentes. La copia 14.07 factoriza
ese cálculo dentro de pipeline.py/R; no modifica fuentes de 14.04–14.06.

Genera un reporte con nombre nuevo mediante integracion.py generar / generar_reporte,
y renderízalo con integracion.py renderizar / renderizar_reporte. Se usa Quarto
existente; no se instala. El .qmd contiene una fotografía HTML preparada con
datos verificados: renderizar no vuelve a consultar ni ejecuta Jupyter/knitr.
No hay caché ni freeze que actualizar. Cambiar datos/configuración requiere
otra entrega y otro reporte. El renderizador rechaza un HTML existente y conserva
carpetas parciales si Quarto falla. El verificador revisa tablas, fuente .qmd y
la sección calculada del HTML; no certifica todo el documento ni autenticidad.

Inicia una app solo en 127.0.0.1. El botón Comprobar entrega relee y compara
fuente completa, configuración y salida. El borrador no cambia la vista aplicada;
un rechazo retira la vista anterior. No hay monitor de disco, caché de cálculo,
persistencia ni sincronización entre sesiones. La hora UTC indica comprobación;
no es fecha de corte ni certifica una sesión histórica. MD5 identifica bytes,
no autentica. Comparar también los valores por crédito y los denominadores.

La interfaz Python tiene un lockfile separado derivado de las versiones ya
declaradas en el curso y comprobado con uv; incluye Streamlit 1.66.1. La interfaz
R reutiliza DESCRIPTION/renv.lock de 13.01, con Shiny 1.14.0 y renv 1.3.1.
No se modifica ningún entorno global ni los metadatos raíz del curso.
R 4.6.1/Python 3.12.12 siguen siendo las versiones de esta práctica.

Conserva fuentes, intentos, entregas y reportes. Un solo escritor; sin cambios
de archivos durante una operación, bloqueo ni transacción de todo el producto.
Pruebas 14.05 heredadas siguen disponibles. No hay paquete final distribuible,
CI, despliegue, autenticación ni checkpoints de proyecto; 14.08 aporta entrega opcional y 14.09 revisión final en el recorrido.
