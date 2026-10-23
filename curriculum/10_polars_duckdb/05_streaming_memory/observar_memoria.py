"""Observacion exploratoria de pico residente en procesos nuevos, sin instalar.

No es un benchmark: el pico incluye arranque/importaciones, consulta y escritura.
La auditoria y conciliacion se ejecutan en el padre, fuera de esos procesos.
"""

import argparse
from datetime import date
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

import polars as pl
import streaming_polars as curso


def pico_residente():
    """Bytes del maximo residente del proceso hasta esta lectura; no solo Polars."""
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes

        class Contadores(ctypes.Structure):
            _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
                (nombre, ctypes.c_size_t) for nombre in (
                    "PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
                    "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage",
                    "QuotaNonPagedPoolUsage", "PagefileUsage", "PeakPagefileUsage")
            ]

        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        psapi = ctypes.WinDLL("psapi", use_last_error=True)
        kernel.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(Contadores), wintypes.DWORD]
        psapi.GetProcessMemoryInfo.restype = wintypes.BOOL
        valores = Contadores()
        valores.cb = ctypes.sizeof(valores)
        if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(valores), valores.cb):
            raise ctypes.WinError(ctypes.get_last_error())
        return dict(metrica="PeakWorkingSetSize", bytes=int(valores.PeakWorkingSetSize))
    if sys.platform.startswith("linux"):
        import resource
        valor = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Linux informa KiB. Esta rama no se probo en la revision Windows.
        return dict(metrica="ru_maxrss", bytes=int(valor * 1024))
    return dict(metrica="no_disponible", bytes=None)


def trabajar(modo, entrada, salida, corte, minimo):
    consulta = curso.consultar(entrada, corte, minimo)
    with Path(salida).open("xb") as archivo:
        if modo == "collect":
            tabla = consulta.collect(engine="streaming")
            tabla.write_parquet(archivo, compression="zstd")
        elif modo == "sink":
            consulta.sink_parquet(archivo, compression="zstd", engine="streaming")
        else:
            raise ValueError("Modo desconocido")
    # Se lee antes de imprimir/serializar y antes de la conciliacion del padre.
    memoria = pico_residente()
    return dict(modo=modo, pico_residente=memoria, python=platform.python_version(),
                polars=pl.__version__, sistema=platform.system(), hilos=pl.thread_pool_size(),
                alcance="vida del proceso hasta leer el pico tras consulta/escritura, sin auditoria")


def observar(entrada, destino, fuente=curso.FUENTE, corte=date(2026, 10, 31), minimo=2000):
    curso.referencia.validar_parametros(corte, minimo)
    curso.base.auditar(entrada, fuente)
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    entorno = os.environ.copy()
    entorno["POLARS_VERBOSE"] = "1"  # Solo los hijos; no cambia el entorno global.
    registros = []
    for modo in ("collect", "sink"):
        salida = destino / f"{modo}.parquet"
        proceso = subprocess.run([
            sys.executable, "-X", "utf8", str(Path(__file__).resolve()), "--trabajador", modo,
            str(Path(entrada).resolve()), str(salida.resolve()),
            "--corte", corte.isoformat(), "--minimo", str(minimo),
        ], env=entorno, capture_output=True, text=True, encoding="utf-8")
        (destino / f"{modo}.log").write_text(proceso.stderr, encoding="utf-8")
        if proceso.returncode != 0:
            raise RuntimeError(f"Fallo el trabajador {modo}; revisar {destino / (modo + '.log')}")
        registro = json.loads(proceso.stdout)
        registro["control"] = curso.verificar(salida, entrada, fuente, corte, minimo)
        with (destino / f"{modo}.json").open("x", encoding="utf-8") as archivo:
            json.dump(registro, archivo, ensure_ascii=False, indent=2)
        registros.append(registro)
    return registros


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trabajador", choices=["collect", "sink"], help=argparse.SUPPRESS)
    parser.add_argument("entrada", type=Path)
    parser.add_argument("destino", type=Path)
    parser.add_argument("--fuente", type=Path, default=curso.FUENTE)
    parser.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    parser.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    if args.trabajador:
        print(json.dumps(trabajar(args.trabajador, args.entrada, args.destino, args.corte, args.minimo)))
    else:
        print(json.dumps(observar(args.entrada, args.destino, args.fuente, args.corte, args.minimo),
                         ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
