# Guía de apoyo — Visual Studio Code

VS Code reúne un editor, un explorador de archivos y una terminal. Puedes usarlo
para Markdown, Python y otros lenguajes. Esta guía prepara la práctica de la
[lección 04 — Primer script](../curriculum/00_getting_started/04_first_script/README.md);
no cambia el orden de las lecciones ni exige usar este editor.

## 1. Preparar y abrir el proyecto

Si aún no lo tienes en tu equipo personal, descarga VS Code desde su
[sitio oficial](https://code.visualstudio.com/). En un equipo de trabajo utiliza
las herramientas e instalaciones permitidas por tu organización.

1. Abre VS Code.
2. Selecciona **Archivo → Abrir carpeta** (`File → Open Folder`).
3. Elige la carpeta `ds_track`, la que contiene README.md y ROADMAP.md.
4. Si aparece el diálogo de confianza, revisa la procedencia del material antes
   de decidir. El modo restringido permite examinar archivos desconocidos.

Abrir la carpeta completa permite encontrar los archivos relacionados y trabajar
desde un mismo proyecto. Si el comando `code` está disponible en tu terminal,
`code .` abre la carpeta actual; el menú es suficiente si no lo está.

## 2. Reconocer los espacios de trabajo

| Zona | Qué haces allí |
| --- | --- |
| Explorador lateral | Encuentras carpetas y archivos del proyecto |
| Editor central | Lees y modificas archivos abiertos en pestañas |
| Terminal integrada | Ejecutas los comandos del shell |
| Barra de estado inferior | Consultas información del archivo y herramientas activas |
| Paleta de comandos | Buscas acciones del editor por su nombre |

Una pestaña abierta representa un archivo. La carpeta del explorador es el
proyecto; el directorio actual de la terminal es otra ubicación que debes
comprobar. Abrir un archivo no cambia automáticamente ese directorio.

## 3. Editar y guardar

### Captura de referencia: reconocer la interfaz

![Interfaz de VS Code con sus principales zonas señaladas](https://code.visualstudio.com/assets/docs/editing/userinterface/hero.png)

Captura de la [documentación oficial de VS Code](https://code.visualstudio.com/docs/editing/getting-started/userinterface).
Localiza el explorador, el editor, el panel inferior y la barra de estado.
El idioma, el tema y algunos paneles pueden diferir de tu instalación.

1. Localiza `curriculum/00_getting_started/04_first_script/first_summary.py`.
2. Ábrelo y modifica un valor como indica la lección.
3. Guarda con **Ctrl+S** antes de ejecutarlo.

Para crear un archivo, usa **Nuevo archivo** en el explorador y escribe su nombre
con extensión, por ejemplo `mis_notas.md`. `Ctrl+N` abre un archivo sin nombre;
al guardarlo, elige la carpeta y el nombre completo. La extensión ayuda al editor
a reconocer el lenguaje, pero no transforma por sí sola el contenido.

## 4. Leer Markdown con vista previa

Abre `README.md` y ejecuta **Markdown: Open Preview to the Side** desde la paleta
de comandos. También puedes usar **Ctrl+K, luego V**. Compara el texto fuente
con la vista renderizada y observa cómo cambian títulos, listas y enlaces.

**Ctrl+Shift+V** abre la vista previa de Markdown cuando el editor Markdown tiene
el foco. Los atajos pueden tener otra acción cuando estás dentro de la terminal.
GitHub y la vista previa local pueden presentar diferencias; comprueba también
el documento en GitHub cuando publiques.

## 5. Ejecutar desde la terminal integrada

### Captura de referencia: dos archivos lado a lado

![Dos editores abiertos lado a lado en VS Code](https://code.visualstudio.com/assets/docs/editing/userinterface/sidebyside.png)

Captura de la [documentación oficial](https://code.visualstudio.com/docs/editing/getting-started/userinterface#side-by-side-editing).
Esta distribución permite comparar notas y código, o mantener instrucciones
visibles mientras editas. Usa el botón para dividir el editor o arrastra una
pestaña hacia un lado. La vista previa de Markdown utiliza una disposición similar.

Selecciona **Terminal → Nueva terminal** (`Terminal → New Terminal`). En Windows
comprueba que el perfil sea PowerShell si vas a seguir ese recorrido de la lección.
El menú junto al botón de nueva terminal permite elegir entre shells instalados.

Desde PowerShell:

```powershell
# Comprueba que estás en la raíz de ds_track
Get-Location
# Ejecuta el primer script si Python está instalado
python curriculum\00_getting_started\04_first_script\first_summary.py
```

Desde Bash/Zsh:

```bash
# Comprueba la ubicación
pwd
# Ejecuta con el nombre disponible en tu instalación
python3 curriculum/00_getting_started/04_first_script/first_summary.py
```

La terminal integrada utiliza los mismos comandos que una terminal externa.
VS Code no instala Python por abrir un `.py`. Si falta el intérprete, sigue la
orientación de la lección; entornos y dependencias se desarrollarán en la 05.

## 6. Atajos iniciales para Windows

Practica primero guardar, buscar archivos, abrir la paleta y previsualizar Markdown.
Los demás son referencias para cuando los necesites.

| Acción | Atajo predeterminado |
| --- | --- |
| Guardar archivo | Ctrl+S |
| Buscar y abrir un archivo por nombre | Ctrl+P |
| Abrir paleta de comandos | Ctrl+Shift+P |
| Buscar en el archivo actual | Ctrl+F |
| Buscar en el proyecto | Ctrl+Shift+F |
| Ir a una línea | Ctrl+G |
| Mostrar u ocultar la barra lateral | Ctrl+B |
| Vista previa de Markdown | Ctrl+Shift+V |
| Vista previa al lado | Ctrl+K, luego V |
| Mostrar u ocultar terminal | Ctrl+` (acento grave) |
| Consultar y editar atajos | Ctrl+K, luego Ctrl+S |

Los atajos con «luego» son secuencias: pulsa la primera combinación, suéltala y
pulsa la segunda. Pueden variar por teclado, sistema operativo o personalización.
Si alguno no funciona, busca la acción en el menú o la paleta; no necesitas
memorizar toda la tabla. Consulta las referencias oficiales para Linux y macOS.

## 7. Edición práctica: varias líneas y cursores

Estos atajos de Windows se usan **con el foco en el editor**, no en la terminal.
Pruébalos en un archivo de notas y usa Ctrl+Z para deshacer si hace falta.

| Acción | Atajo predeterminado | Ejemplo de uso |
| --- | --- | --- |
| Mover una línea o un bloque seleccionado | Alt+↑ / Alt+↓ | Reordenar pasos sin copiar y pegar |
| Duplicar una línea o un bloque | Shift+Alt+↑ / Shift+Alt+↓ | Crear una línea parecida a la anterior |
| Añadir un cursor arriba o abajo | Ctrl+Alt+↑ / Ctrl+Alt+↓ | Escribir lo mismo en varias líneas |
| Añadir cursores con el ratón | Alt+clic | Editar posiciones concretas a la vez |
| Seleccionar la siguiente aparición de una palabra | Ctrl+D | Cambiar varias apariciones del mismo texto |
| Seleccionar todas las apariciones de la selección | Ctrl+Shift+L | Modificar un texto repetido en todo el archivo |
| Borrar la línea actual | Ctrl+Shift+K | Quitar una línea sin seleccionarla completa |
| Insertar una línea debajo | Ctrl+Enter | Continuar sin mover el cursor al final |
| Insertar una línea arriba | Ctrl+Shift+Enter | Añadir una explicación antes del paso actual |
| Aumentar o reducir sangría | Tab / Shift+Tab | Ajustar un bloque de líneas seleccionadas |

Al seleccionar un bloque, mover o duplicar opera sobre ese bloque. En Python,
la sangría forma parte de la estructura del programa; revisa el resultado al
cambiarla. Algunos atajos pueden ser interceptados por el sistema, por ejemplo
Ctrl+Alt+flechas; consulta los atajos del editor si no funcionan.

### Mini práctica: escribir en tres líneas a la vez

En un archivo de notas, escribe:

```text
Leer la lección
Realizar el lab
Explicar el resultado
```

1. Coloca el cursor al principio de la primera línea.
2. Pulsa Ctrl+Alt+↓ dos veces: verás un cursor en cada línea.
3. Escribe `- ` para convertir las tres líneas en una lista de Markdown.
4. Pulsa Escape para volver a un solo cursor.
5. Mueve una línea con Alt+↑ o Alt+↓ y duplícala con Shift+Alt+↓.
6. Usa Ctrl+Z para observar qué operación deshaces.

Los cursores múltiples repiten tu escritura en cada posición. Con Ctrl+D puedes
seleccionar apariciones una a una y comprobar cuáles modificarás; con
Ctrl+Shift+L debes revisar todas las selecciones antes de escribir.

## 8. Extensiones: introducirlas cuando hagan falta

Markdown y la terminal ya forman parte del editor. Para esta primera práctica
basta con editar el script y ejecutarlo con Python desde la terminal.

Más adelante usaremos la extensión **Python**, publicada por Microsoft, para
seleccionar un intérprete, completar código y depurar. Cuando esté instalada,
la paleta ofrece **Python: Select Interpreter**. La extensión no sustituye la
instalación de Python. Jupyter se introducirá con la lección de notebooks;
las funciones de IA son opcionales.

## Práctica breve

1. Abre `ds_track` como carpeta y encuentra el README usando Ctrl+P.
2. Abre su vista previa y compara el título con el texto fuente.
3. Abre el primer script, cambia una entrada y guarda.
4. Abre la terminal, comprueba la ubicación y ejecuta el archivo.
5. Explica qué ocurrió en el editor y qué ocurrió en la terminal.

Continúa con el [lab 00.04](../labs/00_getting_started/04_first_script/README.md).

## Referencias oficiales

- [Primeros pasos](https://code.visualstudio.com/docs/getstarted/overview).
- [Terminal integrada](https://code.visualstudio.com/docs/terminal/getting-started).
- [Referencia de atajos](https://code.visualstudio.com/docs/reference/default-keybindings).
- [Atajos de Windows en PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf).
- [Consejos y vista previa de Markdown](https://code.visualstudio.com/docs/editing/getting-started/tips-and-tricks).
