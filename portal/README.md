# Portal local — portada, contenido y módulo inicial

Una capa de lectura y orientación sobre el material existente. La portada presenta
el curso, Contenido muestra 00–14 y el módulo 00 integra sus seis lecciones/labs
y apoyos. La sesión acompañada 02.01 conserva notebook y bitácora descargables. El código fuente
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
Si ya existe una salida completa y sus fuentes coinciden, se sirve esa copia.
Si las fuentes cambiaron, se conserva la anterior y se genera otra carpeta
con fecha/hora en el nombre. No se sobrescriben ni borran archivos.
Una copia incompleta debe revisarse, no borrarse para ocultar el fallo.

### Después de cambiar las fuentes

El arranque detecta cambios en las fuentes registradas y prepara una copia nueva.
También puedes elegir explícitamente otra salida. Comando igual en ambos shells:

```text
python portal/servir.py --destino output/portal-revision-2 --abrir
```

El preparador rechaza destinos existentes. Las salidas, cachés y prácticas
personales van dentro de `output/`, que ya está excluido de Git. No se versiona
el sitio generado ni la evidencia de estudiantes.

## Entrada al curso y primera sesión

Empieza por Portada → Contenido → 00 — Entorno de aprendizaje. El módulo 00
reúne las seis lecciones y labs originales, conserva 00.05 A/B y los recorridos
Conda/venv/uv. Sus comandos usan una copia local de DS Track, como explica cada
lección; los archivos de apoyo descargables no equivalen a un clon completo.
Su registro usa una plantilla Markdown personal, no el formulario de pandas.

Para la prueba adicional de pandas, después de sus prerrequisitos:

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

- `curso.json` enumera 00–14 y las páginas/archivos del módulo 00. Solo 00 está
  integrado como módulo completo; los demás índices se descargan como fuente,
  con 12–14 marcados como planes. `sesiones.json` conserva la prueba 02.01.
- `herramientas/preparar_portal.py` adapta enlaces de la lección/lab originales
  a páginas locales; el contenido educativo no se duplica como fuente editorial.
  Las tarjetas de lecciones se generan desde el catálogo.
- Las fuentes de consulta fuera del piloto tienen una página con su ubicación
  en el clon y descarga. No se convierten en sesiones adicionales del portal.
- El adaptador admite los enlaces inline y bloques cercados presentes en estas
  fuentes; conserva anclas explícitas, adapta índices numerados a Quarto y
  conserva detalles desplegables. Los enlaces a directorios resuelven su README.
  Rechaza enlaces locales no enumerados. No es un conversor universal de Markdown.
- `procedencia.json` registra SHA-256 de las fuentes incluidas y versión Quarto;
  ayuda a comprobar coherencia, sin autenticar autoría ni ejecución histórica.
- La construcción de lectura desactiva ejecución y no instala entornos. La
  comprobación del notebook es una fase separada con el entorno elegido.
- No hay cuentas, persistencia compartida, tutor de IA ni coedición. El alcance
  útil de esta prueba es una sesión acompañada, con copias personales.

PROGRESS.md conserva el estado editorial del curso; el portal ofrece una bitácora
personal para 00 y conserva la de 02.01, sin migrar los registros anteriores.
Los enlaces de 00 a PROGRESS se orientan a una guía de registro personal; el
archivo completo de progreso no se incluye en las descargas del sitio. Una visita,
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

La [propuesta de publicación](../docs/portal-publication.md) documenta alojamiento,
audiencia y etapas futuras; no se ha desplegado el sitio.

Siguiente paso: revisar el contenido y observar una sesión del módulo inicial
antes de ampliar otros módulos o 02.02/02.03. El resto del recorrido numerado permanece intacto.

Referencias primarias: [sitios Quarto](https://quarto.org/docs/websites/),
[navegación](https://quarto.org/docs/websites/website-navigation) y
[opciones de proyecto](https://quarto.org/docs/reference/projects/websites.html).
