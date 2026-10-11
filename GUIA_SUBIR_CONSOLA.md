# 🚀 Guía: Cómo subir y actualizar tu perfil de GitHub desde la Consola

Esta guía te muestra los comandos exactos de Git para subir tu perfil a GitHub desde tu terminal y cómo actualizarlo cuando hagas modificaciones en el futuro.

### 📋 Requisitos Previos
1. Tener [Git instalado](https://git-scm.com/downloads).
2. Haber creado el repositorio con tu nombre de usuario (`alexandro-mayoral-teran`) en GitHub.

---

## 🟢 Escenario 1: Es la PRIMERA vez que subes los archivos

Si es la primera vez que vas a enlazar esta carpeta de tu computadora con GitHub, abre tu terminal en esta carpeta (`C:\bluepill5\Devs\git_profile`) y ejecuta estos comandos uno por uno:

```bash
# 1. Inicializa el repositorio local (le dice a Git que empiece a rastrear la carpeta)
git init

# 2. Agrega los archivos que quieres subir. 
# NOTA: Si usas "git add ." subirás TODOS los archivos de la carpeta. 
# Si tienes apuntes u otros archivos en esta carpeta que NO quieres subir,
# especifica mejor los archivos o carpetas exactas así:
git add README.md .github/workflows/snake.yml assets/

# 3. Guarda los cambios localmente (hace una "captura")
git commit -m "Primera subida de mi perfil"

# 4. Conecta tu carpeta con el repositorio de GitHub
git remote add origin https://github.com/alexandro-mayoral-teran/alexandro-mayoral-teran.git

# 5. Sube los archivos a la rama principal (main)
git branch -M main
git push -u origin main --force
```

---

## 🔄 Escenario 2: Ya lo subiste antes y solo quieres ACTUALIZAR cambios

Si ya enlazaste tu carpeta (hiciste el Escenario 1 en el pasado), y hoy decidiste modificar algo en tu `README.md` (por ejemplo, agregaste una nueva herramienta, cambiaste un texto o agregaste un proyecto) y quieres que se refleje en GitHub, **ya no necesitas hacer todos los pasos de nuevo**. 

Solo abre tu terminal en la misma carpeta y ejecuta la "trinidad" de comandos de Git:

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
