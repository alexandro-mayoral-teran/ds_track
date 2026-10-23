"""Entrega de cierre independiente; importar solo define funciones y constantes.

La auditoria materializa valores pequenos. No es un ejecutor de RAM acotada.
"""
import argparse
from datetime import date
import importlib.util
import json
from pathlib import Path
import platform

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
_spec = importlib.util.spec_from_file_location("mediciones_1010", CARPETA.parent / "09_time_memory/comparar.py")
mediciones = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mediciones)
MOTORES = mediciones.MOTORES
ALCANCE = "seleccion ordenada y exportacion JSON del protocolo 10.09; no resumen ni entrega completa"
DECISION = dict(estado="borrador", motor_elegido="", contexto="", claridad="", entorno="",
                costos="", limites="", cuando_cambiaria="", alcance_costos=ALCANCE)


def contrato():
    return dict(version=1, unidad="credito/corte", clave=["id_credito", "fecha_corte"],
        id_credito="texto de tres digitos", fecha_corte="Date entre 1900 y 2100",
        saldo_mxn="entero de 0 a 2147483647 MXN, sin ausencias", max_filas=1998,
        regla="rechazar fuente completa ante incidencias; no imputar ni deduplicar")


def cargar(fuente=FUENTE):
    filas = mediciones.referencia.cargar_filas(fuente)
    if len(filas) > contrato()["max_filas"]:
        raise ValueError("Cierre didactico limitado a 1998 filas")
    return filas


def referencia(fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    filas = cargar(fuente)
    r = mediciones.referencia.construir_referencia(fuente, corte, minimo)
    grupos = {}
    for f in filas:
        n, s = grupos.get(f["fecha_corte"], (0, 0))
        grupos[f["fecha_corte"]] = n+1, s+f["saldo_mxn"]
    r["resumen"] = [dict(fecha_corte=c.isoformat(), registros=grupos[c][0], saldo_mxn=grupos[c][1])
                    for c in sorted(grupos)]
    return r


def consultar(motor, entrada, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    """Cada motor resuelve seleccion y resumen; las mediciones se hacen aparte."""
    import pyarrow as pa
    mediciones.referencia.validar_parametros(corte, minimo)
    cargar(fuente)
    mediciones.auditar(entrada, fuente)
    if motor == "pandas":
        import pandas as pd
        tabla = pd.read_parquet(entrada, engine="pyarrow", dtype_backend="pyarrow")
        seleccion = tabla.loc[(tabla.fecha_corte == corte) & (tabla.saldo_mxn >= minimo),
                              ["id_credito", "saldo_mxn"]].sort_values("id_credito")
        # Ampliar ANTES de sumar; no convertir una suma que ya se desbordo.
        amplia = tabla.assign(saldo_mxn=tabla.saldo_mxn.astype("int64[pyarrow]"))
        resumen = amplia.groupby("fecha_corte", as_index=False).agg(
            registros=("id_credito", "size"), saldo_mxn=("saldo_mxn", "sum")).sort_values("fecha_corte")
        return (pa.Table.from_pandas(seleccion, preserve_index=False),
                pa.Table.from_pandas(resumen, preserve_index=False))
    if motor == "polars":
        import polars as pl
        tabla = pl.scan_parquet(entrada, hive_partitioning=False)
        seleccion = (tabla.filter((pl.col("fecha_corte") == corte) & (pl.col("saldo_mxn") >= minimo))
            .select("id_credito", "saldo_mxn").sort("id_credito").collect())
        resumen = (tabla.group_by("fecha_corte").agg(pl.len().cast(pl.Int64).alias("registros"),
            pl.col("saldo_mxn").cast(pl.Int64).sum()).sort("fecha_corte").collect())
        return seleccion.to_arrow(), resumen.to_arrow()
    if motor == "duckdb":
        import duckdb
        with duckdb.connect(":memory:", config={"threads": 1}) as con:
            seleccion = con.sql("""SELECT id_credito,saldo_mxn FROM read_parquet(?)
                WHERE fecha_corte=CAST(? AS DATE) AND saldo_mxn>=? ORDER BY id_credito""",
                params=[str(entrada), corte, minimo]).to_arrow_table()
            # El maximo de 1998 saldos Int32 cabe sobradamente en BIGINT.
            resumen = con.sql("""SELECT fecha_corte, CAST(COUNT(*) AS BIGINT) AS registros,
                CAST(SUM(saldo_mxn) AS BIGINT) AS saldo_mxn FROM read_parquet(?)
                GROUP BY fecha_corte ORDER BY fecha_corte""", params=[str(entrada)]).to_arrow_table()
        return seleccion, resumen
    raise ValueError("Motor desconocido")


def comprobar(seleccion, resumen, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    import pyarrow as pa
    r = referencia(fuente, corte, minimo)
    if not isinstance(seleccion, pa.Table) or seleccion.column_names != ["id_credito", "saldo_mxn"]:
        raise ValueError("Columnas de seleccion distintas")
    if not (pa.types.is_string(seleccion[0].type) or pa.types.is_large_string(seleccion[0].type)) or seleccion[1].type != pa.int32():
        raise ValueError("Seleccion exige texto/int32 antes de adaptar")
    pares = seleccion.to_pylist()
    control = mediciones.referencia.comprobar_seleccion(pares, fuente, corte, minimo)
    if pares != sorted(pares, key=lambda f: f["id_credito"]):
        raise ValueError("Seleccion debe estar ordenada por ID")
    esperado = pa.schema([("fecha_corte", pa.date32()), ("registros", pa.int64()), ("saldo_mxn", pa.int64())])
    if not isinstance(resumen, pa.Table) or resumen.column_names != esperado.names or list(resumen.schema.types) != list(esperado.types):
        raise ValueError("Resumen exige date32/int64/int64 antes de adaptar")
    filas = resumen.to_pylist()
    if any(type(f["fecha_corte"]) is not date or type(f["registros"]) is not int or
           type(f["saldo_mxn"]) is not int for f in filas):
        raise ValueError("Ausencias/tipos nativos del resumen incompatibles")
    observadas = [dict(f, fecha_corte=f["fecha_corte"].isoformat()) for f in filas]
    if observadas != sorted(observadas, key=lambda f: f["fecha_corte"]):
        raise ValueError("Resumen debe estar ordenado por fecha")
    if observadas != r["resumen"]:
        raise ValueError("Resumen distinto por fecha/valor")
    return dict(control=control, seleccion=pares,
                resumen=r["resumen"])


def escribir_json(ruta, valor):
    with Path(ruta).open("x", encoding="utf-8") as f:
        json.dump(valor, f, ensure_ascii=False, indent=2)


def generar(destino, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000,
            con_mediciones=True, nota="sin anotaciones de disco/carga"):
    import pyarrow.parquet as pq
    filas = cargar(fuente)
    mediciones.referencia.validar_parametros(corte, minimo)
    if type(con_mediciones) is not bool:
        raise ValueError("con_mediciones debe ser booleano")
    destino = Path(destino).resolve()
    destino.mkdir(parents=True, exist_ok=False)
    (destino / "fuente.csv").write_bytes(Path(fuente).read_bytes())
    escribir_json(destino / "contrato.json", contrato())
    entrada = mediciones.preparar(destino / "datos", fuente)
    comparacion = {}
    archivos = ["fuente.csv", "contrato.json", "datos/entrada.parquet", "comparacion.json"]
    for motor in MOTORES:
        (destino / motor).mkdir()
        seleccion, resumen = consultar(motor, entrada, fuente, corte, minimo)
        comprobar(seleccion, resumen, fuente, corte, minimo)
        for nombre, tabla in (("seleccion", seleccion), ("resumen", resumen)):
            relativo = f"{motor}/{nombre}.parquet"
            pq.write_table(tabla, destino / relativo, compression="zstd")
            archivos.append(relativo)
        # Certificar lo releido, no solo los objetos anteriores a la escritura.
        comparacion[motor] = comprobar(pq.read_table(destino / motor / "seleccion.parquet"),
            pq.read_table(destino / motor / "resumen.parquet"), fuente, corte, minimo)
    escribir_json(destino / "comparacion.json", comparacion)
    if con_mediciones:
        mediciones.medir(entrada, destino / "mediciones", fuente, corte, minimo, nota=nota)
    escribir_json(destino / "decision.json", DECISION)
    import pandas as pd
    import pyarrow as pa
    import polars as pl
    import duckdb
    escribir_json(destino / "manifiesto.json", dict(fuente_sha256=mediciones.huella(fuente),
        archivos={n: mediciones.huella(destino / n) for n in archivos}, filas=len(filas),
        corte=corte.isoformat(), minimo=minimo, con_mediciones=con_mediciones, alcance_costos=ALCANCE,
        versiones=dict(python=platform.python_version(), pandas=pd.__version__, pyarrow=pa.__version__,
                       polars=pl.__version__, duckdb=duckdb.__version__)))
    return verificar(destino, fuente)


def verificar(destino, fuente=FUENTE, exigir_decision=False):
    """Solo lectura: reconstruye evidencia; valida estructura, no calidad del argumento."""
    import pyarrow.parquet as pq
    d = Path(destino)
    if type(exigir_decision) is not bool:
        raise ValueError("exigir_decision debe ser booleano")
    leer = lambda n: json.loads((d / n).read_text(encoding="utf-8"))
    m = leer("manifiesto.json")
    corte, minimo = date.fromisoformat(m["corte"]), m["minimo"]
    r = referencia(fuente, corte, minimo)
    esperados = {"fuente.csv", "contrato.json", "datos/entrada.parquet", "comparacion.json"} | {
        f"{motor}/{nombre}.parquet" for motor in MOTORES for nombre in ("seleccion", "resumen")}
    if (set(m["archivos"]) != esperados or m["fuente_sha256"] != mediciones.huella(fuente) or
        type(m["filas"]) is not int or m["filas"] != len(cargar(fuente)) or m["alcance_costos"] != ALCANCE):
        raise ValueError("Manifiesto/fuente incompatibles")
    if set(m["versiones"]) != {"python", "pandas", "pyarrow", "polars", "duckdb"} or any(
            type(v) is not str or not v for v in m["versiones"].values()):
        raise ValueError("Versiones ausentes/incompletas")
    if any(mediciones.huella(d / n) != h for n, h in m["archivos"].items()):
        raise ValueError("Archivo distinto de su huella")
    if leer("contrato.json") != contrato() or mediciones.huella(d / "fuente.csv") != mediciones.huella(fuente):
        raise ValueError("Contrato/copia distintos de referencia externa")
    mediciones.auditar(d / "datos/entrada.parquet", fuente)
    comparacion = {motor: comprobar(pq.read_table(d / motor / "seleccion.parquet"),
        pq.read_table(d / motor / "resumen.parquet"), fuente, corte, minimo) for motor in MOTORES}
    if comparacion != leer("comparacion.json"):
        raise ValueError("Comparacion guardada distinta de reconstruccion")
    if type(m["con_mediciones"]) is not bool:
        raise ValueError("Estado de mediciones invalido")
    if m["con_mediciones"]:
        mediciones.verificar(d / "mediciones", d / "datos/entrada.parquet", fuente)
        datos = leer("mediciones/informe.json")
        if (datos["corte"], datos["minimo"]) != (m["corte"], minimo):
            raise ValueError("Mediciones de otra pregunta")
    elif (d / "mediciones").exists():
        raise ValueError("Mediciones presentes pero no declaradas")
    decision = leer("decision.json")
    if set(decision) != set(DECISION) or any(type(v) is not str for v in decision.values()) or decision["alcance_costos"] != ALCANCE:
        raise ValueError("Estructura de decision incompatible")
    if decision["estado"] not in ("borrador", "documentada") or decision["motor_elegido"] not in ("", *MOTORES):
        raise ValueError("Estado/motor de decision invalido")
    if exigir_decision or decision["estado"] == "documentada":
        if not m["con_mediciones"] or decision["estado"] != "documentada" or any(not v.strip() for v in decision.values()):
            raise ValueError("Faltan mediciones o campos de decision documentada")
    return dict(control=r["control"], resumen=r["resumen"], mediciones=m["con_mediciones"],
                decision=decision["estado"], argumento="requiere revision humana")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    comandos = p.add_subparsers(dest="accion", required=True)
    generar_p = comandos.add_parser("generar", help="crear una entrega nueva")
    verificar_p = comandos.add_parser("verificar", help="reconstruir una entrega existente")
    for comando in (generar_p, verificar_p):
        comando.add_argument("destino", type=Path)
        comando.add_argument("--fuente", type=Path, default=FUENTE)
    generar_p.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    generar_p.add_argument("--minimo", type=int, default=2000)
    generar_p.add_argument("--sin-mediciones", action="store_true", help="solo depuracion; no completa evidencia de costos")
    generar_p.add_argument("--nota", default="sin anotaciones de disco/carga")
    verificar_p.add_argument("--exigir-decision", action="store_true")
    a = p.parse_args()
    x = (generar(a.destino, a.fuente, a.corte, a.minimo, not a.sin_mediciones, a.nota)
         if a.accion == "generar" else verificar(a.destino, a.fuente, a.exigir_decision))
    print(json.dumps(x, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
