# 03 — Git: historial y actualización del perfil

## Propósito

Conservar y publicar una actualización del README comprendiendo cada paso.
Esta base servirá después para guardar tus scripts, consultas y documentación
junto con una explicación de sus cambios.

## Prerrequisitos

Completa [Markdown y perfil](../01_github_profile/README.md) y
[terminal y rutas](../02_terminal_paths/README.md). Necesitas Git instalado y
acceso al repositorio de tu perfil. Esta práctica es opcional si estudias desde ZIP.
No necesitas Python, pip ni uv para realizarla.

## Objetivos

- Distinguir guardar un archivo, preparar cambios, hacer commit y publicar.
- Clonar el perfil y registrar una modificación de su README.
- Revisar los cambios antes de confirmarlos y comprobar el resultado en GitHub.
- Retomar una sesión reconociendo el estado del repositorio.

## 1. Entender el recorrido de un cambio

Git conserva el historial de los archivos que registras. Si modificas una
explicación o corriges un script, puedes consultar qué cambió y por qué.
El repositorio local está en tu computadora; el remoto está alojado en GitHub.

```text
Editar y guardar → Preparar → Registrar en el historial → Publicar en GitHub
     editor         git add          git commit               git push
```

| Momento | Qué ocurre | Cómo lo compruebas |
| --- | --- | --- |
| Archivo guardado | Tu editor escribe la modificación en el archivo local | `git diff` muestra cambios sin preparar en archivos ya registrados |
| Cambio preparado | Seleccionas lo que incluirá el próximo commit | `git diff --staged` muestra esa selección |
| Commit creado | Git registra los cambios preparados en el historial local | `git log --oneline -1` muestra el último commit |
| Publicación completada | Los commits se envían al remoto | Compruebas el archivo y el historial en GitHub |

El **área de preparación** es la selección de cambios para el próximo commit.
No es una publicación. Un commit tiene un identificador y un mensaje; el mensaje
explica la intención, por ejemplo «Agrega mis objetivos de aprendizaje».

> **Para conversar:** si guardas el README y cierras el editor, ¿ya existe un
> commit? ¿La copia de GitHub cambió?

## 2. Clonar el perfil una sola vez

Abre la terminal en la carpeta donde guardas tus proyectos, fuera de `ds_track`.
Sustituye `TU_USUARIO` por tu usuario real en ambos lugares de la URL y en `cd`.
Estos comandos de Git funcionan en PowerShell y Bash/Zsh; `cd` también está
disponible en ambos.

```text
# Comprueba que Git está disponible
git --version

# Descarga los archivos y el historial del perfil en una carpeta nueva
git clone https://github.com/TU_USUARIO/TU_USUARIO.git

# Entra en la carpeta creada por clone
cd TU_USUARIO

# Consulta el estado de esa copia local
git status

# Comprueba la dirección del remoto
git remote -v
```

`clone` configura normalmente el remoto con el nombre `origin`. Sus direcciones
para lectura (fetch) y publicación (push) deben corresponder a tu perfil.
Como el repositorio ya contiene un README, no necesitas ejecutar `git init`.
Si ya lo clonaste, entra en esa carpeta; no vuelvas a clonarlo en cada sesión.

Antes de editar, `git status` debería indicar que no hay cambios pendientes
(`working tree clean`). La descarga de un repositorio público puede funcionar
sin iniciar sesión; publicar requiere autenticarte con una cuenta con permiso.
Si te pide autenticación, sigue el método de inicio de sesión de tu instalación.
La contraseña de tu cuenta no se usa como contraseña de Git por HTTPS.

## 3. Configurar la identidad del autor

Dentro del repositorio, consulta la configuración:

```text
git config user.name
git config user.email
```

Si no hay un valor o quieres utilizar otro en este repositorio, sustituye los
marcadores antes de ejecutar:

```text
# Configura la identidad solo para este repositorio
git config user.name "TU_NOMBRE"
git config user.email "TU_CORREO_DE_AUTOR"
```

Usa un correo verificado de tu cuenta o el correo privado `noreply` que GitHub
muestra en sus ajustes de correo. La identidad queda en los commits; configurar
nombre y correo no inicia sesión ni concede permisos para publicar.

## 4. Editar y revisar antes de preparar

Abre el `README.md` de la carpeta clonada en tu editor, agrega un objetivo real
y guarda el archivo. Vuelve a la terminal de esa misma carpeta:

```text
# Identifica los archivos modificados
git status

# Revisa la diferencia respecto a lo que está preparado
git diff
```

El README aparecerá como modificado, todavía sin preparar. En el diff,
las líneas con `+` muestran adiciones y las que tienen `-` muestran eliminaciones.
Esos signos describen la diferencia; no forman parte del archivo.
Si aparece un visor con `(END)`, pulsa `q` para volver a la terminal.

## 5. Seleccionar y registrar el cambio

```text
# Prepara únicamente el README
git add README.md

# Comprueba la selección que incluirá el commit
git diff --staged
git status

# Registra esa selección con un mensaje que explique el cambio
git commit -m "Agrega mis objetivos de aprendizaje"

# Comprueba el último commit y el estado local
git log --oneline -1
git status
```

Después de `add`, el archivo aparece entre los cambios preparados
(`Changes to be committed`). Después del commit, ya no queda modificado si no
hiciste nuevas ediciones. Puede aparecer que tu rama está por delante de
`origin`: el commit existe localmente y todavía falta publicarlo.

`git add README.md` selecciona un archivo concreto. No necesitas preparar toda
la carpeta con `git add .`. Si editas el README después de prepararlo, vuelve a
revisar y preparar la nueva edición antes del commit.

## 6. Publicar y comprobar

```text
# Envía los commits pendientes al remoto configurado
git push

# Consulta el estado después de publicar
git status
```

Abre tu repositorio en GitHub y comprueba la frase en el README y el mensaje en
su historial de commits. Después visita tu perfil. El commit publicado debe
coincidir con el que consultaste localmente.

> **Para comprobar:** ¿qué comando conserva el cambio localmente y cuál lo
> publica? ¿Cómo demostrarías que ocurrió cada acción?

## 7. Retomar el trabajo otro día

Entra en la carpeta que ya clonaste y consulta `git status`. Si no hay cambios
locales pendientes, trae las novedades que pudieron hacerse desde la web:

```text
# Revisa el estado antes de traer cambios
git status

# Actualiza la copia local si puede avanzar sin combinar historiales divergentes
git pull --ff-only
```

Si no hubo cambios remotos, puede indicar `Already up to date`.
Después repite editar → revisar → preparar → commit → push.
Si hay ediciones sin guardar en un commit o el comando indica que no puede
avanzar, revisa lo pendiente con quien te acompaña antes de continuar.

## Cuando algo no funciona

| Situación | Qué revisar |
| --- | --- |
| `not a git repository` | Estás fuera de la carpeta clonada; comprueba tu ubicación |
| Git no conoce tu identidad | Configura nombre y correo dentro del repositorio |
| `nothing to commit` | Comprueba si guardaste el archivo correcto y preparaste su cambio |
| `git diff` está vacío después de add | Revisa `git diff --staged`: el cambio ya puede estar preparado |
| `push` pide autenticación o rechaza permisos | Confirma tu cuenta y la URL con `git remote -v` |
| `push` rechaza cambios por novedades remotas | Consulta el estado; con el árbol limpio prueba `git pull --ff-only` y vuelve a publicar si tuvo éxito |

Si la actualización no puede avanzar, revisa el mensaje con quien te acompaña.
No uses `--force` para resolverlo. Ramas de trabajo, conflictos y pull requests
se estudiarán después; esta lección se centra en una actualización sencilla.

## Práctica y criterio de salida

Realiza el [lab 00.03](../../../labs/00_getting_started/03_git_workflow/README.md).
Puedes avanzar cuando registres y publiques una modificación, expliques guardar
frente a commit y push, y compruebes la selección preparada y el último commit.
La evidencia es el commit del perfil; todavía no hay proyecto de datos asociado.

## Siguiente lección

[04 — Primer script Python](../04_first_script/README.md). Usarás la terminal para ejecutar un
programa y Git para conservar sus cambios conforme avances.

## Referencias

- [Fundamentos de Git](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Obteniendo-un-repositorio-Git).
- [Configuración inicial de Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configuraci%C3%B3n-inicial-de-Git).
- [Autenticación con GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github).
