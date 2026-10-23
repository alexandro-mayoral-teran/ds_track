# 10.10 — Generar y reconstruir la entrega

Vuelve a la [lección](README.md) para contexto, datos, cotas y decisiones.
Parte de la raíz de DS Track. El entorno Python local necesita pandas 2.3.3,
PyArrow 21.0.0, Polars 2.0.0 y DuckDB 2.0.0; referencia Python 3.12.12.
Ya están declarados en la configuración raíz; no hay paquetes nuevos.

Usa un gestor elegido según [00.05](../../00_getting_started/05_environment/README.md).
Si falta el entorno, sigue [10.08](../08_engine_interchange/recorridos.md);
si ya es adecuado, no reinstales. No instales en Anaconda base ni mezcles gestores.
No necesitas Parquet ni mediciones de prácticas anteriores.

Generar crea una carpeta nueva con datos/outputs, nueve observaciones de costos
y decision.json en borrador. No se sobrescribe un destino existente. Verificar
solo lee y reconstruye contra el CSV externo propio de esta sección.

## PowerShell

Con Conda o venv/pip adecuado y activado:

```powershell
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py generar output/cierre_1010_ps --nota "Anotar equipo, disco y carga conocidos"
python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py verificar output/cierre_1010_ps
```

Alternativa uv, fuera de otro entorno activo:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py generar output/cierre_1010_ps_uv
uv run --locked python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py verificar output/cierre_1010_ps_uv
```

## Bash/Zsh

Con Conda o venv/pip adecuado y activado:

```bash
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py generar output/cierre_1010_bash --nota "Anotar equipo, disco y carga conocidos"
python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py verificar output/cierre_1010_bash
```

Alternativa uv, fuera de otro entorno activo:

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py generar output/cierre_1010_bash_uv
uv run --locked python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py verificar output/cierre_1010_bash_uv
```

Los comandos son completos, pero Linux/macOS no se probaron por autoría;
la medición residente está comprobada en Windows. Una métrica no disponible
no se interpreta como cero.

## CMD / Anaconda Prompt

```bat
conda activate ds-track
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py generar output/cierre_1010_cmd
python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py verificar output/cierre_1010_cmd
```

## Completar la decisión y retomar

Abre decision.json de **tu entrega** y completa los campos según la lección/lab.
Al documentar la explicación cambia estado a documentada. Con el entorno adecuado,
desde una sesión nueva, ajustando la ruta a la que creaste:

```text
python -X utf8 curriculum/10_polars_duckdb/10_closure_tool_choice/cierre.py verificar output/cierre_1010_ps --exigir-decision
```

Antes de completar el archivo, exigir-decision debe fallar; el borrador no
acredita cierre de práctica. El verificador revisa evidencia y estructura,
no sustituye conversar con quien te acompaña sobre la calidad del argumento.

Para otra pregunta, generar admite --corte/--minimo con otro destino. Septiembre
≥ 2000 debe dejar cinco/11645; noviembre exporta selección vacía y conserva
los dos grupos del resumen. Verificar lee esos parámetros del manifiesto.
Con un CSV diferente pasa --fuente tanto al generar como al verificar.
--sin-mediciones sirve para depurar; no completa la evidencia de costos.

R opcional: el bloque de la lección se ejecuta en la consola R del IDE, con
la raíz del repositorio como carpeta de trabajo; no necesita bibliotecas externas.
Reinicia R y ejecuta todo para comprobar independencia de la sesión anterior.

Continúa con el [lab 10.10](../../../labs/10_polars_duckdb/10_closure_tool_choice/README.md).
