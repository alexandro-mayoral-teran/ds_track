# Portal local — portada, contenido y módulo inicial

Una capa de lectura y orientación sobre el material existente. La portada presenta
el curso, Contenido muestra 00–14 y los módulos 00 a 05 integran sus lecciones,
labs y apoyos. La interfaz usa una paleta monocromática de alto contraste y el símbolo
del recorrido aparece como icono del sitio. Material de consulta ofrece apoyos
opcionales de los módulos integrados.
El código fuente
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
La terminal debe permanecer abierta. **Ctrl+C** detiene el servidor y las copias
se conservan. Se enlaza solo a 127.0.0.1.

Si el puerto está ocupado, añade `--puerto 8872`.
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

Las páginas de lección y lab se preparan desde sus fuentes actuales en
`curriculum/` y `labs/`; no edites su copia generada en `_site/`. La presentación
curada del módulo 00, los resúmenes de tarjetas y las etiquetas del menú se
mantienen en `portal/paginas/modulo-00.qmd`, `portal/curso.json` y
`portal/_quarto.yml`. Cuando cambie el material de un módulo integrado, contrasta
esas piezas con las fuentes, actualiza solo lo que el portal presenta por
separado y genera una salida nueva para comprobarlo. Las reglas de esta revisión
recurrente están en las especificaciones locales del sitio; no se distribuyen
con el portal.

## Entrada al curso

Empieza por Portada → Contenido → 00 — Entorno de aprendizaje. El módulo 00
reúne las seis lecciones y labs originales, conserva 00.05 A/B y los recorridos
Conda/venv/uv. Después, 01 — Python fundamental presenta seis lecciones/labs
con sus scripts y CSV de apoyo; trabaja en una copia propia. Los archivos
descargables de 00 a 05 no equivalen a un clon completo. El registro de 00 usa
una plantilla Markdown personal. El módulo 02 (pandas) integra sus diez lecciones y labs, con scripts, CSV de entrada,
notebooks y el entorno de referencia; las salidas generadas no se publican.

## Tema de noche

El icono pequeño del interruptor es el nativo de Quarto (`theme: light/dark` en `_quarto.yml`): sigue el tema del sistema al inicio y recuerda la elección en el navegador, sin servidor. Los ajustes de la paleta oscura están al final de `estilos.css` bajo `body.quarto-dark`; al añadir componentes con colores fijos, agregar también su variante allí. Pendiente: revisión visual en navegador a 1440/768/390 px.

## Alcance de la copia

El portal integra los módulos 00 a 05. Material de consulta reúne apoyos
opcionales enlazados desde sus lecciones. Contenido
indica qué otros módulos ofrecen material en el repo y cuáles son planes.
Los archivos de consulta se descargan con su ubicación en el clon.

La lectura no ejecuta programas ni instala entornos. Las prácticas se ejecutan
por separado en la copia personal. El registro de procedencia ayuda a contrastar
archivos de una copia, sin autenticar autoría o ejecuciones históricas.

PROGRESS.md conserva el estado editorial del curso; el portal ofrece una bitácora
personal para 00.
Los enlaces de 00 a PROGRESS se orientan a una guía de registro personal; el
archivo completo de progreso no se incluye en las descargas del sitio. Una visita,
una respuesta correcta o ejecutar el ejemplo no acredita aprendizaje. Proyecto
integrador y checkpoints siguen pendientes. Una sesión real de pareja todavía
debe observarse; la revisión técnica no la sustituye.

## Comprobación de autoría

```text
python -m unittest discover -s portal/tests -v
```

Además se comprueba el render completo, los enlaces/fragmentos/recursos locales
y los apoyos descargables. En navegador se revisan navegación, teclado, soluciones
cerradas y ventanas estrechas. No se certifica accesibilidad completa por esas
comprobaciones.

La copia descrita aquí funciona localmente. La publicación en línea requiere
definir audiencia, alojamiento y una versión revisada; no se ha desplegado el sitio.

Siguiente paso: revisar el contenido y observar una sesión real de los módulos
00–05 antes de ampliar otros módulos. La prueba aislada 02.01 se retiró del portal;
sus fuentes educativas permanecen en curriculum/ y labs/.

Referencias primarias: [sitios Quarto](https://quarto.org/docs/websites/),
[navegación](https://quarto.org/docs/websites/website-navigation) y
[opciones de proyecto](https://quarto.org/docs/reference/projects/websites.html).
