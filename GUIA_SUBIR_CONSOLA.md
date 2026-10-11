# 🚀 Guía: Cómo subir y actualizar tu perfil de GitHub desde la Consola

Esta guía te muestra los comandos exactos de Git para subir tu perfil a GitHub desde tu terminal y cómo actualizarlo cuando hagas modificaciones en el futuro.

### 📋 Requisitos Previos
1. Tener [Git instalado](https://git-scm.com/downloads).
2. Haber creado el repositorio con tu nombre de usuario (`alexandro-mayoral-teran`) en GitHub.

---

## 🟢 Escenario 1: Traer el perfil a tu computadora

Si creaste el repositorio en GitHub con un README, clónalo para conservar su historial.
Abre la terminal en `C:\bluepill5\Devs`, fuera de `ds_track`, y ejecuta:

```text
git clone https://github.com/alexandro-mayoral-teran/alexandro-mayoral-teran.git
cd alexandro-mayoral-teran
git status
```

Edita el README dentro de esa carpeta. Luego sigue el escenario 2 para guardar
la actualización y publicarla. No necesitas ejecutar `git init` ni configurar
el remoto: el clon ya incluye ambos.

Consulta la [lección de Git y perfil](curriculum/00_getting_started/02_github_profile/README.md)
para comprender cada paso.

---
## 🔄 Escenario 2: Ya lo subiste antes y solo quieres ACTUALIZAR cambios

Si ya enlazaste tu carpeta (hiciste el Escenario 1 en el pasado), y hoy decidiste modificar algo en tu `README.md` (por ejemplo, agregaste una nueva herramienta, cambiaste un texto o agregaste un proyecto) y quieres que se refleje en GitHub, **ya no necesitas hacer todos los pasos de nuevo**. 

Solo abre tu terminal en la carpeta clonada de tu perfil y ejecuta la "trinidad" de comandos de Git:

```bash
# 1. Prepara el archivo modificado para subirlo.
# De nuevo, usamos solo el nombre del archivo para no subir basura por accidente.
git add README.md

# 2. Guarda los cambios con un mensaje corto que describa qué modificaste
git commit -m "Actualizando iconos y estilo del perfil"

# 3. Empuja (sube) los cambios a GitHub
git push
```

¡Eso es todo! Ve a la página principal de tu GitHub, presiona F5 para refrescar y verás tus nuevos cambios aplicados inmediatamente.
