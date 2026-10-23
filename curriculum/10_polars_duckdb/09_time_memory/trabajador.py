"""Una observacion aislada; solo importa el motor solicitado mas PyArrow comun."""
import argparse
from datetime import date
import json
import os
from pathlib import Path
import platform
from time import perf_counter_ns, process_time_ns

from metricas import memoria_residente


def trabajar(motor, entrada, temporal, corte, minimo):
    cpu0 = process_time_ns()
    t0 = perf_counter_ns()
    import pyarrow as pa
    if motor == "pandas":
        import pandas as pd
        version = pd.__version__
    elif motor == "polars":
        import polars as pl
        version = pl.__version__
    elif motor == "duckdb":
        import duckdb
        version = duckdb.__version__
    else:
        raise ValueError("Motor desconocido")
    t1 = perf_counter_ns()
    pa.set_cpu_count(1)
    pa.set_io_thread_count(1)
    con = None
    limite_duckdb = None
    hilos = dict(arrow_cpu=pa.cpu_count(), arrow_io=pa.io_thread_count())
    try:
        if motor == "duckdb":
            con = duckdb.connect(":memory:", config={"threads": 1, "memory_limit": "128MiB",
                                                     "temp_directory": str(temporal)})
            hilos["duckdb"], limite_duckdb = con.execute(
                "SELECT current_setting('threads'), current_setting('memory_limit')").fetchall()[0]
        if motor == "polars":
            hilos["polars"] = pl.thread_pool_size()
        t2 = perf_counter_ns()
        if motor == "pandas":
            base = pd.read_parquet(entrada, engine="pyarrow", dtype_backend="pyarrow",
                                   columns=["id_credito", "fecha_corte", "saldo_mxn"])
        elif motor == "polars":
            base = (pl.scan_parquet(entrada, hive_partitioning=False)
                .filter((pl.col("fecha_corte") == corte) & (pl.col("saldo_mxn") >= minimo))
                .select("id_credito", "saldo_mxn").sort("id_credito"))
        else:
            base = con.sql("""SELECT id_credito,saldo_mxn FROM read_parquet(?)
                WHERE fecha_corte=CAST(? AS DATE) AND saldo_mxn>=? ORDER BY id_credito""",
                params=[str(entrada), corte, minimo])
        t3 = perf_counter_ns()
        if motor == "pandas":
            resultado = base.loc[(base.fecha_corte == corte) & (base.saldo_mxn >= minimo),
                                 ["id_credito", "saldo_mxn"]].sort_values("id_credito").reset_index(drop=True)
        elif motor == "polars":
            resultado = base.collect(engine="auto")
        else:
            resultado = base.to_arrow_table()
        t4 = perf_counter_ns()
        if motor == "pandas":
            tabla = pa.Table.from_pandas(resultado, preserve_index=False)
        elif motor == "polars":
            tabla = resultado.to_arrow()
        else:
            tabla = resultado
        filas = tabla.to_pylist()
        t5 = perf_counter_ns()
        # Misma salida UTF-8 JSON en los tres motores; cierre incluido, sin fsync.
        with (temporal.parent / "seleccion.json").open("x", encoding="utf-8") as f:
            json.dump(filas, f, ensure_ascii=False, indent=2)
        t6 = perf_counter_ns()
        cpu_ns = process_time_ns()-cpu0
        memoria = memoria_residente()  # Antes de validar en el padre, emitir crudas o cerrar conexion.
        retenidos = sum(p.stat().st_size for p in temporal.rglob("*") if p.is_file())
        return dict(motor=motor, pid=os.getpid(), version=version, pyarrow=pa.__version__, python=platform.python_version(),
            hilos=hilos, limites_env={n: os.environ.get(n) for n in
                ("POLARS_MAX_THREADS", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")},
            seleccion=filas, esquema=[(f.name, str(f.type)) for f in tabla.schema],
            fases_ns=dict(importar=t1-t0, configurar=t2-t1, entrada_o_plan=t3-t2,
                          ejecutar_recuperar=t4-t3, adaptar=t5-t4, exportar=t6-t5),
            intervalo_ns=t6-t0, consulta_ns=t5-t2, cpu_ns=cpu_ns,
            memoria=memoria, limite_duckdb=limite_duckdb, temporales_retenidos_bytes=retenidos)
    finally:
        if con is not None:
            con.close()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("motor", choices=["pandas", "polars", "duckdb"])
    p.add_argument("entrada", type=Path)
    p.add_argument("temporal", type=Path)
    p.add_argument("--corte", type=date.fromisoformat, required=True)
    p.add_argument("--minimo", type=int, required=True)
    a = p.parse_args()
    print(json.dumps(trabajar(a.motor, a.entrada, a.temporal, a.corte, a.minimo)))


if __name__ == "__main__":
    main()
