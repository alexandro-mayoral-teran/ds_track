# Producto de práctica 14.08 — Entrega local

Esta sección es opcional. Elige Python/Streamlit o R/Shiny; las dos rutas tienen
material y basta una. Los preparadores reúnen 60 fuentes sin instalar paquetes.
Se conservan los metadatos de cálculo e interfaces de 14.07. No hay cambios en
dependencias raíz de DS Track ni bibliotecas globales.

1. Revisa fuentes, catalogo.csv y metadatos. Restaura solo el entorno de cálculo
   elegido y ejecuta reconstruir.py / reconstruir_producto de reconstruir.R.
   Se ejecutan siete grupos de pruebas, tres consultas trazadas y tres reportes
   Quarto. Requiere Quarto existente y una copia nueva, sin salidas previas.
2. Crea un paquete hermano, fuera de este proyecto, con entrega.py crear o
   crear_entrega. Indica un CSV de referencia externo al paquete. Copia solo
   las 60 fuentes enumeradas y la muestra de tres entregas/reportes comprobados.
   No copia .venv, renv/library, caches, ensayos ni intentos con rutas locales.
3. Verifica con la herramienta local revisada: entrega.py verificar o
   verificar_entrega. Solo lee; usa el modelo/vista del revisor y el CSV externo.
   No ejecuta codigo del paquete. Cada revisor comprueba su ruta, no la contraria.
4. Copia solo fuentes a otro destino nuevo con entrega.py copiar / copiar_fuentes.
   Revisa ese codigo antes de restaurar y ejecutarlo. No copies bibliotecas ni
   resultados de muestra para simular una reconstruccion.

El paquete contiene fuentes/, muestra/, LEEME.md, ENTREGA.csv y MANIFIESTO.csv.
Son 90 archivos. El manifiesto compara bytes y no se incluye a si mismo. MD5
no autentica; tampoco aprueba el codigo ni la calidad editorial de toda la salida.
Se comprueban datos por clave/campo, configuraciones, insumos, tablas y seccion
calculada de los HTML. Horas UTC validas no autentican ejecuciones pasadas.
Una verificacion numerica no sustituye revisar codigo, instrucciones y navegador.

Los destinos deben ser nuevos. Un fallo conserva la carpeta parcial; no hay
limpieza automatica, reemplazo, reanudacion ni publicacion atomica del conjunto.
Un manifiesto presente no certifica que el constructor termino correctamente.
Un solo escritor y sin cambiar archivos mientras se copian o verifican.
Una lista permitida de archivos delimita el alcance; no limpia informacion
privada que alguien haya escrito dentro de un archivo permitido.

CI_EJEMPLO.yml es una ampliacion sin activar. Se puede estudiar sin cuenta ni
servicio remoto. Su comando ejecuta solo las pruebas Python en un venv nuevo,
no la reconstruccion completa ni la interfaz. No ponerlo en .github/workflows
de DS Track. Su activacion en otro repositorio y una ejecucion hospedada son
acciones separadas; este material no acredita haberlas realizado.

El cierre de revision y defensa se desarrolla en 14.09. Proyectos/checkpoints
y practica personal siguen pendientes; material disponible no acredita aprendizaje.
