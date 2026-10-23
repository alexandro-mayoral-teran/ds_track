"""Preparar, medir o verificar observaciones didacticas. Importar no lee ni escribe."""
import argparse
from datetime import date, datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import statistics
import subprocess
import sys
from time import get_clock_info, perf_counter_ns

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
MOTORES = ("pandas", "polars", "duckdb")
FASES = ("importar", "configurar", "entrada_o_plan", "ejecutar_recuperar", "adaptar", "exportar")
_spec = importlib.util.spec_from_file_location("referencia_1009",
    CARPETA.parent / "01_question_contract_reference/referencia.py")
referencia = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(referencia)


def huella(ruta):
    return hashlib.sha256(Path(ruta).read_bytes()).hexdigest()


def esquema():
    import pyarrow as pa
    return pa.schema([("id_credito", pa.string()), ("fecha_corte", pa.date32()), ("saldo_mxn", pa.int32())])


def preparar(destino, fuente=FUENTE):
    import pyarrow as pa
    import pyarrow.parquet as pq
    filas = referencia.cargar_filas(fuente)
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    archivo = destino / "entrada.parquet"
    pq.write_table(pa.Table.from_pylist(filas, schema=esquema()), archivo, compression="zstd")
    auditar(archivo, fuente)
    return archivo


def auditar(entrada, fuente=FUENTE):
    import pyarrow.parquet as pq
    filas = referencia.cargar_filas(fuente)
    tabla = pq.read_table(entrada)
    if not tabla.schema.equals(esquema(), check_metadata=False):
        raise ValueError("Entrada debe conservar string/date32/int32 en orden")
    clave = lambda f: (f["id_credito"], f["fecha_corte"], f["saldo_mxn"])
    if sorted(tabla.to_pylist(), key=clave) != sorted(filas, key=clave):
        raise ValueError("Parquet distinto de fuente externa por clave/valor")
    return len(filas)


def validar_registro(r, fuente, corte, minimo):
    if r["motor"] not in MOTORES or r["esquema"] not in (
            [["id_credito", "string"], ["saldo_mxn", "int32"]],
            [["id_credito", "large_string"], ["saldo_mxn", "int32"]]):
        raise ValueError("Motor/esquema de salida incompatibles")
    control = referencia.comprobar_seleccion(r["seleccion"], fuente, corte, minimo)
    tiempos = r["fases_ns"]
    if set(tiempos) != set(FASES) or any(type(v) is not int or v < 0 for v in tiempos.values()):
        raise ValueError("Fases invalidas")
    for n in ("intervalo_ns", "consulta_ns", "cpu_ns", "proceso_ns", "temporales_retenidos_bytes"):
        if type(r[n]) is not int or r[n] < 0:
            raise ValueError("Tiempo/contador invalido")
    if (sum(tiempos.values()) != r["intervalo_ns"] or
        sum(tiempos[n] for n in FASES[2:5]) != r["consulta_ns"] or r["proceso_ns"] < r["intervalo_ns"]):
        raise ValueError("Intervalos no concilian")
    memoria = r["memoria"]
    if memoria["metrica"] not in ("PeakWorkingSetSize", "ru_maxrss_linux", "no_disponible"):
        raise ValueError("Metrica de memoria desconocida")
    for n in ("pico_bytes", "residente_final_bytes"):
        if memoria[n] is not None and (type(memoria[n]) is not int or memoria[n] <= 0):
            raise ValueError("Memoria debe ser bytes positivos o no disponible")
    if (memoria["pico_bytes"] is None) != (memoria["metrica"] == "no_disponible"):
        raise ValueError("Ausencia de memoria incoherente")
    if memoria["metrica"] == "PeakWorkingSetSize":
        if memoria["residente_final_bytes"] is None or memoria["residente_final_bytes"] > memoria["pico_bytes"]:
            raise ValueError("Residente actual incompatible con pico")
    elif memoria["residente_final_bytes"] is not None:
        raise ValueError("Residente actual no disponible para esta metrica")
    if not r["hilos"] or any(type(v) is not int or v != 1 for v in r["hilos"].values()):
        raise ValueError("Pools configurados deben informar uno")
    if set(r["hilos"]) != {"arrow_cpu", "arrow_io"} | ({r["motor"]} if r["motor"] != "pandas" else set()):
        raise ValueError("Faltan pools efectivos")
    if any(type(r[n]) is not str or not r[n] for n in ("version", "pyarrow", "python")):
        raise ValueError("Faltan versiones")
    if type(r["pid"]) is not int or r["pid"] <= 0 or r["intervalo_ns"] <= 0:
        raise ValueError("Proceso/intervalo invalidos")
    if r["limites_env"] != {n: "1" for n in
            ("POLARS_MAX_THREADS", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")}:
        raise ValueError("Limites de entorno incoherentes")
    return control


def resumir(registros):
    if len({(r["pyarrow"], r["python"], r["memoria"]["metrica"]) for r in registros}) != 1:
        raise ValueError("No mezclar versiones comunes o metricas entre motores")
    salida = []
    for motor in MOTORES:
        grupo = [r for r in registros if r["motor"] == motor]
        if not grupo:
            raise ValueError("Falta un motor")
        if len({(r["version"], r["pyarrow"], r["python"], r["memoria"]["metrica"]) for r in grupo}) != 1:
            raise ValueError("Versiones o metricas distintas entre repeticiones")
        fila = dict(motor=motor, repeticiones=len(grupo))
        for n in ("consulta_ns", "intervalo_ns", "proceso_ns"):
            valores = [r[n] for r in grupo]
            fila[n] = dict(min=min(valores), mediana=statistics.median(valores), max=max(valores))
        picos = [r["memoria"]["pico_bytes"] for r in grupo]
        fila["pico_bytes"] = (dict(min=min(picos), mediana=statistics.median(picos), max=max(picos))
                              if all(v is not None for v in picos) else None)
        salida.append(fila)
    return salida


def medir(entrada, destino, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000, repeticiones=3, nota="sin anotaciones de disco/carga"):
    referencia.validar_parametros(corte, minimo)
    if type(repeticiones) is not int or not 3 <= repeticiones <= 30 or repeticiones % 3:
        raise ValueError("Repeticiones debe ser multiplo de tres entre 3 y 30")
    cantidad = auditar(entrada, fuente)
    entrada = Path(entrada).resolve()
    destino = Path(destino).resolve()
    destino.mkdir(parents=True, exist_ok=False)
    iniciales = dict(fuente_sha256=huella(fuente), entrada_sha256=huella(entrada))
    entorno = os.environ.copy()
    for n in ("POLARS_MAX_THREADS", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        entorno[n] = "1"  # Solo hijos; no modifica entorno global ni afinidad CPU.
    crudas = []
    for vuelta in range(repeticiones):
        orden = MOTORES[vuelta % 3:] + MOTORES[:vuelta % 3]
        for posicion, motor in enumerate(orden, 1):
            nombre = f"{vuelta+1:02d}_{posicion}_{motor}"
            temporal = destino / f"observacion_{nombre}" / "temporales"
            temporal.mkdir(parents=True)
            inicio = perf_counter_ns()
            p = subprocess.run([sys.executable, "-X", "utf8", str(CARPETA / "trabajador.py"),
                motor, str(entrada), str(temporal), "--corte", corte.isoformat(), "--minimo", str(minimo)],
                env=entorno, capture_output=True, text=True, encoding="utf-8")
            proceso_ns = perf_counter_ns()-inicio
            (destino / f"{nombre}.log").write_text(p.stderr, encoding="utf-8")
            if p.returncode:
                raise RuntimeError(f"Fallo {nombre}; revisar log y conservar carpeta parcial")
            r = json.loads(p.stdout)
            r.update(repeticion=vuelta+1, posicion=posicion, proceso_ns=proceso_ns)
            validar_registro(r, fuente, corte, minimo)  # Fuera del trabajador y sus relojes.
            if json.loads((temporal.parent / "seleccion.json").read_text(encoding="utf-8")) != r["seleccion"]:
                raise ValueError("Exportacion distinta de la salida recuperada")
            with (destino / f"{nombre}.json").open("x", encoding="utf-8") as f:
                json.dump(r, f, ensure_ascii=False, indent=2)
            crudas.append(r)
    if iniciales != dict(fuente_sha256=huella(fuente), entrada_sha256=huella(entrada)):
        raise ValueError("Fuentes cambiaron durante la corrida; conservar y revisar")
    reloj = get_clock_info("perf_counter")
    informe = dict(**iniciales, filas_fuente=cantidad, corte=corte.isoformat(), minimo=minimo,
        repeticiones=repeticiones, fin_utc=datetime.now(timezone.utc).isoformat(),
        equipo=dict(sistema=platform.platform(), cpu=platform.processor(), arquitectura=platform.machine(),
                    procesadores_logicos=os.cpu_count(), nota=nota),
        reloj=dict(implementacion=reloj.implementation, resolucion_segundos=reloj.resolution, monotono=reloj.monotonic),
        protocolo="procesos nuevos, orden rotado; entrada leida en auditoria previa, cache SO sin vaciar; auditoria fuera del trabajador",
        resumen=resumir(crudas))
    with (destino / "informe.json").open("x", encoding="utf-8") as f:
        json.dump(informe, f, ensure_ascii=False, indent=2)
    return informe


def verificar(destino, entrada, fuente=FUENTE):
    """Solo lectura: reconstruye pares e invariantes; no autentica tiempos pasados."""
    d = Path(destino)
    informe = json.loads((d / "informe.json").read_text(encoding="utf-8"))
    if (huella(fuente) != informe["fuente_sha256"] or huella(entrada) != informe["entrada_sha256"] or
        auditar(entrada, fuente) != informe["filas_fuente"]):
        raise ValueError("Fuente/entrada distintas")
    corte, minimo = date.fromisoformat(informe["corte"]), informe["minimo"]
    referencia.validar_parametros(corte, minimo)
    repeticiones = informe["repeticiones"]
    if type(repeticiones) is not int or not 3 <= repeticiones <= 30 or repeticiones % 3:
        raise ValueError("Repeticiones invalidas")
    esperados = []
    registros = []
    for vuelta in range(repeticiones):
        orden = MOTORES[vuelta % 3:] + MOTORES[:vuelta % 3]
        for posicion, motor in enumerate(orden, 1):
            nombre = f"{vuelta+1:02d}_{posicion}_{motor}.json"
            esperados.append(nombre)
            r = json.loads((d / nombre).read_text(encoding="utf-8"))
            if (r["motor"], r["repeticion"], r["posicion"]) != (motor, vuelta+1, posicion):
                raise ValueError("Orden/repeticion alterados")
            validar_registro(r, fuente, corte, minimo)
            exportada = d / f"observacion_{nombre[:-5]}" / "seleccion.json"
            if json.loads(exportada.read_text(encoding="utf-8")) != r["seleccion"]:
                raise ValueError("Exportacion distinta de crudas")
            registros.append(r)
    if {p.name for p in d.glob("*.json")} != set(esperados + ["informe.json"]):
        raise ValueError("Registros adicionales o ausentes")
    if resumir(registros) != informe["resumen"]:
        raise ValueError("Resumen no concilia con crudas")
    return informe["resumen"]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("accion", choices=["preparar", "medir", "verificar"])
    p.add_argument("destino", type=Path)
    p.add_argument("--entrada", type=Path)
    p.add_argument("--fuente", type=Path, default=FUENTE)
    p.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    p.add_argument("--minimo", type=int, default=2000)
    p.add_argument("--repeticiones", type=int, default=3)
    p.add_argument("--nota", default="sin anotaciones de disco/carga")
    a = p.parse_args()
    if a.accion == "preparar":
        print(preparar(a.destino, a.fuente))
    else:
        if a.entrada is None:
            p.error("medir/verificar requieren --entrada")
        x = (medir(a.entrada, a.destino, a.fuente, a.corte, a.minimo, a.repeticiones, a.nota)
             if a.accion == "medir" else verificar(a.destino, a.entrada, a.fuente))
        print(json.dumps(x, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
