# Lab 00.03 — Actualizar el perfil con Git

## Relación

- Módulo: `00_getting_started`.
- Lección: [03 — Git: historial y actualización](../../../curriculum/00_getting_started/03_git_workflow/README.md).
- Prerrequisitos: labs [00.01](../01_github_profile/README.md) y [00.02](../02_terminal_paths/README.md).
- Proyecto: no aplica; la evidencia es el historial del perfil o de la práctica local.

## Objetivo y tiempo orientativo

Conservar una actualización verificable del README y explicar su recorrido.
Tiempo orientativo: 30 a 45 minutos, ajustable según preparación y dudas.
Publicar forma parte de la ruta del perfil; la variante local no requiere GitHub.

## Entrada

Necesitas Git disponible (`git --version`). Elige una ruta:

- **Perfil:** repositorio con el README publicado en 00.01 y acceso para enviar cambios.
- **Local:** carpeta nueva y vacía fuera de otros repositorios, sin cuenta de GitHub.

Consulta la [preparación y elección del recorrido](../../../curriculum/00_getting_started/03_git_workflow/README.md#antes-de-empezar).
Descargar DS Track como ZIP no impide realizar ninguna de las dos rutas.

## Actividad

### Ruta del perfil

1. Clona el repositorio del perfil fuera de la carpeta de DS Track.
2. Comprueba el remoto y la identidad de autor; configura esta última si hace falta.
3. Agrega una frase sobre una habilidad que quieras desarrollar y guarda el README.
4. Revisa `git status` y `git diff`; explica qué cambió antes de prepararlo.
5. Prepara únicamente `README.md` y comprueba `git diff --staged`.
6. Crea un commit descriptivo y consulta `git log --oneline -1` antes de publicar.
7. Haz push, comprueba la frase y el commit en GitHub y revisa el estado local.

<details>
<summary>Ver una solución — Preparar la copia local</summary>

Desde tu carpeta de proyectos, sustituye los marcadores por tus datos:

```text
# Clona solo si todavía no tienes una copia local
git clone https://github.com/TU_USUARIO/TU_USUARIO.git
cd TU_USUARIO
# Comprueba el estado, la dirección remota y la identidad
git status
git remote -v
git config user.name
git config user.email
```

El remoto debe apuntar a tu perfil. Si falta la identidad, configúrala como
explica la lección. Esto es diferente de autenticarte para publicar.

</details>

<details>
<summary>Ver una solución — Revisar, registrar y publicar</summary>

Después de editar y guardar el README:

```text
# Revisa lo modificado antes de seleccionarlo
git status
git diff
# Prepara el README y comprueba lo que incluirá el commit
git add README.md
git diff --staged
git status
# Conserva el cambio en el historial local
git commit -m "Agrega mi siguiente objetivo de aprendizaje"
git log --oneline -1
# Publica y comprueba el estado
git push
git status
```

El cambio pasa de modificado a preparado y después forma parte de un commit.
El commit existe localmente antes del push. Comprueba su identificador y mensaje
en GitHub, además de la frase publicada. El mensaje de ejemplo puede adaptarse
para describir tu modificación real.

</details>

### Variante local sin GitHub

Realiza esta variante en lugar de la ruta del perfil:

1. Prepara una carpeta vacía fuera de otros repositorios e inicializa Git.
2. Configura la identidad solo en ese repositorio.
3. Crea el README de tres líneas del
   [ejemplo local](../../../curriculum/00_getting_started/03_git_workflow/README.md#alternativa-local-sin-github),
   comprueba que aparece como no seguido y registra la primera versión.
4. Cambia el objetivo, guarda y explica el diff antes de prepararlo.
5. Prepara solo README.md, revisa el diff preparado y crea un segundo commit.
6. Comprueba los dos commits, el estado limpio y que no hay remoto configurado.
   No ejecutes push ni pull.

<details>
<summary>Ver resultado y explicación — Variante local</summary>

El historial muestra «Agrega presentación inicial» y «Concreta mi objetivo de
SQL» si utilizaste los mensajes del ejemplo. Los identificadores serán propios
de tu ejecución. El segundo diff cambia «Quiero aprender SQL.» por
«Quiero consultar ventas con SQL y comprobar los totales.».

`git status` queda limpio si no hay otros cambios o archivos nuevos y
`git remote -v` no imprime direcciones. Ambos commits son locales: no se publicó
el README en GitHub. Un archivo nuevo no seguido aparece en status, pero su
contenido no se muestra en diff antes de prepararlo.

</details>

## Resultado y evidencia

En la ruta del perfil, el README publicado contiene tu frase y el historial
muestra el commit. Conserva su enlace e identificador en tu nota personal.

En la ruta local, conserva los dos identificadores, el README y una explicación
de por qué no hubo publicación. Puedes guardar tu nota fuera del repositorio
de práctica para que no aparezca como archivo nuevo pendiente.

En ambos casos, registra evidencia y dudas en tu copia de la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o en una nota propia. PROGRESS.md del curso es la bitácora editorial, no la
evidencia de quien estudia.

## Reflexión

- ¿Qué diferencia hay entre guardar el archivo, hacer commit y hacer push?
- En el perfil, ¿por qué clonaste el repositorio que ya tenía un README? En la ruta local, ¿por qué usaste init en una carpeta nueva?
- ¿Qué te permite comprobar `git diff --staged` antes del commit?
- ¿Configurar el correo del autor inicia sesión en GitHub?
- ¿Qué comprobarías antes de retomar el trabajo? ¿Qué paso adicional corresponde solo si tienes un remoto configurado?

<details>
<summary>Ver respuestas orientativas de reflexión</summary>

- Guardar escribe el archivo; commit registra cambios preparados en el historial
  local; push envía commits al remoto.
- Clonar conserva el historial existente y configura el remoto.
  Inicializar permite comenzar uno nuevo; no descarga el perfil ni configura GitHub.
- `git diff --staged` muestra la selección que registrará el próximo commit.
- El correo identifica al autor; la autenticación permite acceder y publicar.
- Primero consultarías `git status`. Con el árbol limpio, `git pull --ff-only`
  puede traer novedades sin combinar historiales divergentes; si falla, revisa
  el mensaje antes de seguir. En la práctica local, sin remoto, revisas el estado
  y el historial sin ejecutar pull ni push.

</details>

## Siguiente paso

Continúa con la [lección 04 — Primer script Python](../../../curriculum/00_getting_started/04_first_script/README.md).
Lee el material antes de realizar su lab y registra tus dudas antes de continuar.
