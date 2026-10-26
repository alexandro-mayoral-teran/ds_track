# Portal local — primera prueba 02.01

Una capa de lectura y orientación sobre el material existente. Incluye inicio,
sesión, lección, lab, notebook descargable y bitácora personal. El código fuente
se versiona en este repositorio; esta prueba no despliega un servicio en Internet.

## Abrir la prueba

Desde la raíz de DS Track, en la terminal del sistema. Necesitas Python 3.11 o
posterior y Quarto; no necesitas instalar paquetes Python para construir el portal.
Comprobado con Python 3.12.12 y Quarto 1.9.38 existentes.

### PowerShell

```powershell
python portal/servir.py --abrir
```

### Bash/Zsh

```bash
python portal/servir.py --abrir
```

El comando construye una copia en `output/portal-local/` si no existe, abre
`http://127.0.0.1:8871/` y sirve únicamente el HTML generado y sus recursos.
En Windows detecta también el Quarto incluido en RStudio en su ruta habitual.
Si está en otra ubicación, pasa `--quarto` con la ruta del ejecutable.
La terminal debe permanecer abierta. **Ctrl+C** detiene el servidor; las copias
y el borrador guardado del navegador se conservan. Se enlaza solo a 127.0.0.1.

Si el puerto está ocupado, añade `--puerto 8872`; el borrador del navegador
pertenece al origen anterior y no se traslada automáticamente a otro puerto.
Si ya existe la salida se sirve esa copia, sin reconstruirla ni borrar archivos.
Una copia incompleta debe revisarse, no borrarse para ocultar el fallo.

### Después de cambiar las fuentes

Elige una salida nueva para revisar los cambios. Comando igual en ambos shells:

```text
python portal/servir.py --destino output/portal-revision-2 --abrir
```

El preparador rechaza destinos existentes. Las salidas, cachés y prácticas
personales van dentro de `output/`, que ya está excluido de Git. No se versiona
el sitio generado ni la evidencia de estudiantes.

## Primera sesión con tu compañero

1. Entren a «Tu recorrido» y contrasten la pregunta inicial. Cada persona explica
   su predicción antes de ejecutar.
2. Descarguen el ZIP, extraigan la carpeta completa y lean ABRIR.md. Cada persona
   abre su notebook en el editor que ya usa, con el kernel del entorno de estudio
   y pandas 2.3.3. El portal no ejecuta Python en el navegador.
3. Lean la lección y trabajen el lab. Una persona escribe, la otra pregunta;
   cambien de papel al agregar la venta. Las soluciones permanecen cerradas.
4. Guarden el notebook y su bitácora. El formulario web guarda un único borrador
   local por sesión/navegador, solo al pulsar Guardar, y permite descargar Markdown.
   No sincroniza con bitacora.md, otra persona ni el repositorio.
5. Reinicien el kernel, ejecuten todas las celdas y expliquen una variante.
   Anoten especialmente dónde les costó orientarse, abrir o retomar.

También puedes preparar una copia sin usar las descargas (desde la raíz):

```text
python portal/herramientas/preparar_practica.py output/mis-practicas/02.01
```

Si existe, se rechaza para conservar tu trabajo. Para retomar abre esa misma
carpeta; no ejecutes la preparación encima.

## Responsabilidades y límites

- `sesiones.json` enumera una sola sesión y todas las fuentes permitidas.
- `herramientas/preparar_portal.py` adapta enlaces de la lección/lab originales
  a páginas locales; el contenido educativo no se duplica como fuente editorial.
- Las fuentes de consulta fuera del piloto tienen una página con su ubicación
  en el clon y descarga. No se convierten en sesiones adicionales del portal.
- El adaptador admite los enlaces inline y bloques cercados presentes en estas
  fuentes; conserva fragmentos de páginas incluidas y detalles desplegables.
  Rechaza enlaces locales no enumerados. No es un conversor universal de Markdown.
- `procedencia.json` registra SHA-256 de las fuentes incluidas y versión Quarto;
  ayuda a comprobar coherencia, sin autenticar autoría ni ejecución histórica.
- La construcción de lectura desactiva ejecución y no instala entornos. La
  comprobación del notebook es una fase separada con el entorno elegido.
- No hay cuentas, persistencia compartida, tutor de IA ni coedición. El alcance
  útil de esta prueba es una sesión acompañada, con copias personales.

PROGRESS.md conserva el estado editorial del curso; el piloto añade una bitácora
personal en la copia de trabajo, sin migrar los registros anteriores. Una visita,
una respuesta correcta o ejecutar el ejemplo no acredita aprendizaje. Proyecto
integrador y checkpoints siguen pendientes. Una sesión real de pareja todavía
debe observarse; la revisión técnica no la sustituye.

## Comprobación de autoría

```text
python -m unittest discover -s portal/tests -v
```

Además se comprueba render completo, enlaces/fragmentos/recursos locales, descarga
del paquete, notebook desde kernel limpio con ejemplo/variante/vacío, destinos
ocupados y originales intactos. En navegador se revisan ventanas amplias/estrechas,
soluciones cerradas, pregunta inicial, bitácora guardada/recuperada/exportada y
teclado. No se certifica accesibilidad completa por esas comprobaciones.

Siguiente ampliación: observar una sesión y corregir fricción antes de añadir
02.02/02.03. El resto del recorrido numerado permanece intacto.

Referencias primarias: [sitios Quarto](https://quarto.org/docs/websites/),
[navegación](https://quarto.org/docs/websites/website-navigation) y
[opciones de proyecto](https://quarto.org/docs/reference/projects/websites.html).
