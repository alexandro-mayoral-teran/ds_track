# 03 — Git: historial y actualización del perfil

## Propósito

Conservar y publicar una actualización del README comprendiendo cada paso:
archivo modificado → cambios preparados → commit local → publicación remota.

## Prerrequisitos

Completa [Markdown y perfil](../01_github_profile/README.md) y
[terminal y rutas](../02_terminal_paths/README.md). Necesitas Git instalado y,
para publicar, acceso al repositorio del perfil creado en la primera lección.
Esta práctica es opcional para quien estudie desde un ZIP.

## Conceptos

El repositorio local contiene los archivos y su historial en tu computadora.
El remoto es la copia alojada en GitHub; `origin` es el nombre habitual de ese
remoto. `clone` obtiene los archivos y el historial y configura la conexión.

El área de preparación selecciona los cambios que incluirá el próximo commit.
Un commit registra esos cambios localmente; `push` envía los commits al remoto.
Guardar un archivo en el editor no ejecuta ninguna de esas acciones.

## Actualizar desde la terminal

Después de la práctica de terminal, clona el repositorio del perfil en una carpeta
separada de DS Track. Como ya lo creaste con un README, clonar conserva su historial.
Sustituye `TU_USUARIO` por tu usuario real:

```text
git clone https://github.com/TU_USUARIO/TU_USUARIO.git
cd TU_USUARIO
git status
```

Edita el README y luego ejecuta:

```text
git diff
git add README.md
git diff --staged
git commit -m "Describe mis objetivos de aprendizaje"
git push
git status
```

`diff` permite revisar antes de guardar. `add` prepara los cambios; `commit`
los registra localmente; `push` los envía al remoto. La autenticación puede
solicitarse al clonar o publicar. Si Git pide tu identidad de autor, configura
tu nombre y un correo verificado o el correo privado de GitHub antes del commit.

Si `push` indica que hay cambios remotos pendientes, consulta `git status` y
el historial antes de continuar. No uses `--force` como solución inicial.

## Práctica y criterio de salida

Realiza el [lab 00.03](../../../labs/00_getting_started/03_git_workflow/README.md).
Puedes avanzar cuando identifiques qué cambios están preparados, expliques la
diferencia entre commit y push y compruebes una actualización en GitHub.
No hay proyecto de datos asociado todavía: la evidencia es el commit del perfil.

## Siguiente lección

Primer script Python (por desarrollar). Usarás la terminal que ya conoces para
pasar de editar documentación a ejecutar un programa.

## Referencia

- [Fundamentos de Git](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Obteniendo-un-repositorio-Git).
