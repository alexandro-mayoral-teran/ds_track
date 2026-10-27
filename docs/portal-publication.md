# Publicación del portal — propuesta y decisiones pendientes

Fecha de revisión: 2026-10-26. Este documento describe cómo pasar del prototipo
local a una versión en línea. **No acredita un despliegue ni el alta de cuentas.**
El código sigue versionado en DS Track; las salidas de generación y las evidencias
personales permanecen fuera de Git. La arquitectura privada de trabajo no forma
parte de los archivos distribuidos.

## Punto de partida

El [portal](../portal/README.md) se construye con Python estándar y Quarto.
El resultado es HTML, CSS, JavaScript y descargas. El servidor local es una
herramienta de revisión: al publicar el resultado estático no hace falta
mantenerlo encendido ni ejecutar Python para cada visitante.

El notebook de pandas se abre en el equipo del estudiante. La bitácora web usa
almacenamiento de ese navegador y exportación Markdown. Alojar los archivos
no agrega cuentas, progreso sincronizado, coedición ni ejecución remota.

## Propuesta para la primera publicación

1. Revisar el contenido, instrucciones, rutas de práctica y archivos descargables.
2. Elegir audiencia: pública o restringida a participantes autorizados.
3. Generar una copia nueva y comprobar navegación, fragmentos, recursos, descargas,
   notebook y formularios. Publicar únicamente su `_site/`, no la raíz del repo.
4. Revisar una vista previa de la versión candidata antes de promoverla.
5. Registrar el commit publicado y conservar posibilidad de volver a la versión
   anterior. Un push al repo no debe publicar automáticamente al principio.
6. Probar una sesión real y corregir fricción antes de ampliar funcionalidades.

El control de versiones del código y la visibilidad del sitio son decisiones
separadas. Mantener el repositorio privado no restringe por sí solo el acceso
al HTML que se publique. La revisión del paquete incluye documentos auxiliares:
no distribuir bitácoras personales, credenciales ni registros de trabajo.

## Alojamiento a evaluar

| Alternativa | Utilidad para el piloto | Decisión pendiente |
| --- | --- | --- |
| Netlify | Primera candidata: admite resultado estático y flujos desde Git; Quarto documenta su publicación | Cuenta, audiencia y plan adecuado; protección de acceso depende de las condiciones del plan |
| Cloudflare Pages | Alternativa para archivos estáticos y vistas previas | Configuración de publicación y, si se requiere, protección de todas las rutas de acceso |
| GitHub Pages | Adecuada si el contenido será público y se quiere integrar con GitHub | Comprobar elegibilidad del repo/plan; publicación privada exige condiciones de Enterprise Cloud |

No se eligió proveedor ni presupuesto. Revisar precios, límites y opciones de
acceso en la cuenta concreta antes de contratar. Un dominio propio es opcional:
puede empezarse con la dirección del proveedor y conectarlo después.

## Qué se necesita para cada etapa

| Etapa | Producto | Requisitos adicionales |
| --- | --- | --- |
| Portal de lectura y práctica local | Páginas, preguntas en JavaScript y descargas | Alojamiento estático, revisión y procedimiento de publicación |
| Cuentas y progreso entre dispositivos | Registros asociados a participantes | Autenticación, permisos, almacenamiento y reglas de privacidad/recuperación |
| Revisión entre compañeros | Evidencias y comentarios compartidos | Modelo de acceso, archivos compartidos y revisión del flujo |
| Python en el navegador o remoto | Práctica ejecutable en línea | Evaluar compatibilidad de paquetes, aislamiento, archivos, persistencia y costos |
| Tutor de IA | Ayuda contextual conectada al contenido | Diseño pedagógico, evaluación de respuestas, servicio/API y control de costos/datos |

Estas etapas no son requisitos automáticos del portal estático. La necesidad
de cada una debe surgir de sesiones reales y decisiones explícitas.

## Organización de la interfaz

La entrada se divide en **portada → contenido → módulo → lección → lab →
comprobación y evidencia**. La portada presenta propósito, público y método.
Contenido muestra 00–14 con diferencias claras entre material del repo,
integración en el portal y módulos aún planificados. El primer módulo es
**00 — Entorno de aprendizaje**, sin renumerar el track.

Su página de módulo reúne propósito, seis lecciones, prácticas y criterio de
salida. En 00.05 conserva las partes A/B y la elección de un único gestor.
Las páginas educativas se generan desde curriculum/labs, sin crear una segunda
versión editorial de la teoría. La prueba acompañada 02.01 sigue accesible
después de sus prerrequisitos. Integrar páginas no acredita práctica completada.

## Referencias primarias

- [Sitios Quarto](https://quarto.org/docs/websites/).
- [Publicación HTML con Quarto](https://quarto.org/docs/output-formats/html-publishing).
- [Despliegues Netlify](https://docs.netlify.com/deploy/create-deploys/).
- [Protección de acceso Netlify](https://docs.netlify.com/manage/security/secure-access-to-sites/password-protection/).
- [Archivos estáticos en Cloudflare Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/).
- [Vistas previas en Cloudflare Pages](https://developers.cloudflare.com/pages/configuration/preview-deployments/).
- [Visibilidad de GitHub Pages](https://docs.github.com/en/enterprise-cloud%40latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site).
