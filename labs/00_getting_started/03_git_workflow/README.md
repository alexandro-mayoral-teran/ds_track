# Lab 00.03 — Actualizar el perfil con Git

## Relación

- Módulo: `00_getting_started`.
- Lección: [03 — Git: historial y actualización](../../../curriculum/00_getting_started/03_git_workflow/README.md).
- Prerrequisitos: labs [00.01](../01_github_profile/README.md) y [00.02](../02_terminal_paths/README.md).
- Proyecto: no aplica; la evidencia es un commit del perfil.

## Objetivo y tiempo orientativo

Conservar y publicar una actualización verificable del README, en 30 a 45 minutos.
Esta práctica es opcional si estudias sin GitHub.

## Entrada

El repositorio de tu perfil con el README publicado en el lab 00.01.

## Actividad

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

## Resultado y evidencia

El README publicado contiene tu frase y el historial muestra el commit.
Registra el enlace al commit y las dudas en [PROGRESS.md](../../../PROGRESS.md).

## Reflexión

- ¿Qué diferencia hay entre guardar el archivo, hacer commit y hacer push?
- ¿Por qué clonaste el repositorio que ya tenía un README?
- ¿Qué te permite comprobar `git diff --staged` antes del commit?
- ¿Configurar el correo del autor inicia sesión en GitHub?
- ¿Qué comprobarías antes de retomar el trabajo y traer cambios remotos?

<details>
<summary>Ver respuestas orientativas de reflexión</summary>

- Guardar escribe el archivo; commit registra cambios preparados en el historial
  local; push envía commits al remoto.
- Clonar conserva el historial existente y configura el remoto.
- `git diff --staged` muestra la selección que registrará el próximo commit.
- El correo identifica al autor; la autenticación permite acceder y publicar.
- Primero consultarías `git status`. Con el árbol limpio, `git pull --ff-only`
  puede traer novedades sin combinar historiales divergentes; si falla, revisa
  el mensaje antes de seguir.

</details>

## Siguiente paso

Continúa con la [lección 04 — Primer script Python](../../../curriculum/00_getting_started/04_first_script/README.md).
Lee el material antes de realizar su lab y registra tus dudas antes de continuar.
