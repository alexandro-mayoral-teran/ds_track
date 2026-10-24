# Lab 11.04 — Relacionar narrativa y evidencia

Módulo: 11 — Reportes con Quarto. Tiempo orientativo: 60–90 minutos;
la preparación inicial del entorno puede hacerse en otra sesión.

## Entrada y objetivo

Lee la [lección 11.04](../../../curriculum/11_reporting_quarto/04_tables_figures_references/README.md).
Elige Python/Jupyter o R/knitr y utiliza sus preparadores. No necesitas tus
entregas previas: la lección incluye datos completos y enlaces para preparar
el entorno si todavía falta. No hay dependencias nuevas en esta sección.

La [fuente propia](../../../curriculum/11_reporting_quarto/04_tables_figures_references/cartera.csv)
tiene IDs 001/002/003 en septiembre y octubre de 2026, con saldos
1000/2000/3000 y 1200/1800/3300 MXN respectivamente. Son seis claves únicas,
una por ID/fecha; saldo entero entre 0 y 1000000, sin ausencias. El resultado
conserva tres créditos en ambos cortes.

## Actividad esencial

1. Crea una copia del [mínimo](../../../curriculum/11_reporting_quarto/04_tables_figures_references/minimo.qmd)
   en una carpeta nueva y renderízala. Localiza identificador, caption, referencia
   y nota de fuente. Explica por qué sus cifras son texto fijo y no un cálculo.
2. Prepara una práctica nueva y renderiza el reporte completo del lenguaje
   elegido, siguiendo el recorrido de la lección. Revisa el registro de render,
   párrafo, tabla, figura, notas de fuente y bibliografía.
3. Comprueba cada valor por ID y reconstruye ambos totales. Utiliza los enlaces
   de tabla y figura: deben llegar al objeto correcto y mostrar la numeración
   que corresponda. Identifica qué parte de la pregunta explica mejor cada objeto.
4. Conserva el primer CSV y HTML como evidencia. En la copia de tu práctica,
   cambia solo 003/octubre de 3300 a 3600. Renderiza el mismo `.qmd` sin editar
   totales ni regenerar texto con el preparador. Comprueba simultáneamente
   párrafo, fila de 003, altura y etiqueta de la segunda barra.
5. En una copia del `.qmd`, cambia el caption para aclarar población/unidad,
   manteniendo su identificador. Renderiza y comprueba que los enlaces funcionan.
   Luego prueba una referencia mal escrita, por ejemplo `@tbl-ausente`: guarda
   el aviso y localiza la referencia sin resolver. Corrígela y vuelve a renderizar.
6. Cambia `echo: false` a `echo: true` en una copia y explica qué aparece.
   Los datos y las cifras deben conservarse. Distingue ocultar código de evitar
   su ejecución y de ocultar también resultados con `include: false`.

No modifiques los archivos del curriculum ni edites el HTML para corregir cifras.
Trabaja con copias y conserva la entrada que corresponde a cada salida.

## Repetir el render

La preparación completa y la selección del entorno están en la lección. Estos
bloques presuponen que ya preparaste la práctica. Si Quarto no está en PATH,
asigna su ruta comprobada a la variable.

### Python — PowerShell

Desde la raíz de DS Track, con el entorno local del recorrido 11.03:

```powershell
$quarto1104 = "quarto"
$env:QUARTO_PYTHON = (Resolve-Path "output/1103_entorno/Scripts/python.exe").Path
& $quarto1104 render output/1104_python/reporte_python.qmd --to html
```

### Python — Bash/Zsh

Desde la raíz:

```bash
quarto1104="quarto"
export QUARTO_PYTHON="$PWD/output/1103_entorno/bin/python"
"$quarto1104" render output/1104_python/reporte_python.qmd --to html
```

### R — IDE y comprobación por terminal

Abre el proyecto R preparado, reinicia la sesión y renderiza `reporte_1104.qmd`
desde RStudio o tu IDE. El documento carga sus datos/funciones; no depende de
haber creado variables en la consola. La biblioteca renv debe estar sincronizada.

Como alternativa, en la terminal del sistema situada en la carpeta del proyecto R:

**PowerShell:**

```powershell
$quarto1104 = "quarto"
$env:QUARTO_R = "C:/Program Files/R/R-4.6.1/bin"
& $quarto1104 render reporte_1104.qmd --to html
```

**Bash/Zsh:**

```bash
quarto1104="quarto"
export QUARTO_R="$(dirname "$(command -v Rscript)")"
"$quarto1104" render reporte_1104.qmd --to html
```

Usa la ubicación real de tu R; comprueba que `Rscript` sea el elegido en Bash.
La terminal del sistema no es la consola R. No necesitas el otro motor para avanzar.

## Resultado, comprobación y evidencia

Conserva ambas entradas y HTML, fuentes `.qmd`/funciones/`.bib` y una nota
breve que relacione afirmación, tabla y figura. Indica qué comprobaste en el
registro y qué revisaste visualmente en el navegador. No incluyas entornos,
bibliotecas ni cachés en Git. Una captura puede apoyar la revisión, pero no
sustituye los archivos para reconstruir.

<details>
<summary>Solución razonada</summary>

En el mínimo, `tbl-ejemplo` identifica la tabla, `@tbl-ejemplo` la referencia y
el texto que comienza con `:` es el caption. La nota explica procedencia y unidad
de observación. Los números no se recalculan porque no hay bloques ejecutables.

En el reporte completo inicial, los pares son +200/-200/+300. Total septiembre
6000 MXN, octubre 6300, diferencia 300 y tasa 5.00% sobre septiembre. La tabla
permite localizar el crédito 002 que disminuyó; las barras comparan el agregado.
No es correcto afirmar que todos aumentaron ni atribuir el cambio a cobranza.

Al cambiar 003/octubre a 3600, párrafo y segunda barra deben indicar 6600 MXN;
diferencia 600 y tasa 10.00%. La fila de 003 cambia a +600; las demás y septiembre
se conservan. Si cambia solo una representación, revisa si contiene cifras
manuales o utiliza otros objetos de datos.

Cambiar el caption no rompe una referencia mientras el identificador permanezca.
Una referencia inexistente puede producir HTML con advertencia: el éxito del
comando no basta. `echo: true` muestra código sin alterar su cálculo;
`include: false` oculta código y resultados del bloque, pero lo ejecuta.

`@tbl-pares` y `@fig-saldo` apuntan a evidencia interna. La cita
`[@quarto-referencias]` remite a documentación del procedimiento, no a una fuente
de saldos. La procedencia de estos datos es la muestra sintética propia, indicada
junto a cada objeto. Debe conservarse el `.bib` para reconstruir la bibliografía.

</details>

## Ampliaciones opcionales

- Añade una tabla estática antes de la calculada, con otro ID `tbl-...`.
  Comprueba que la referencia a `tbl-pares` se renumera sin editar el párrafo.
- Cambia dos saldos de octubre, uno +100 y otro -100. La suma y las barras no
  cambian, pero sí los pares. Explica por qué revisar solo el total no es suficiente.
- Deja todos los saldos de septiembre en cero en otra copia: la tasa debe ser
  no definida; tabla y figura conservan esos ceros, sin inventar una base.
- Prueba una clave bibliográfica inexistente en una copia, identifica el aviso
  y corrígela. No inventes una fuente para hacer desaparecer el aviso.

## Reflexión, criterio de salida y siguiente paso

Registra evidencia en [PROGRESS.md](../../../PROGRESS.md). Explica: ¿qué responde
la tabla y qué responde la figura?, ¿cuál es el denominador de la tasa?, ¿qué
demuestra la cita técnica y qué no?, ¿por qué una referencia puede quedar mal
aunque el render termine?

Puedes avanzar cuando cada afirmación tiene evidencia localizable, las tres
representaciones concuerdan y distingues referencia interna, procedencia y cita.
`05_monthly_report` y checkpoints siguen pendientes en
[proyectos](../../../projects/README.md); el material no acredita aprendizaje.
Siguiente: [11.05 — Parámetros y cortes](../../../curriculum/11_reporting_quarto/05_parameters_cutoffs/README.md).
