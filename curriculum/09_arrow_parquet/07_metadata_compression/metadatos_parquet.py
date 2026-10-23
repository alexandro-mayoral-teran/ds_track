"""Experimento pequeno: equivalencia primero, tiempos y metadatos separados.

Importar no escribe. Reutiliza el contrato de la fuente incluida, no entregas.
"""

import argparse
import csv
import importlib.util
import json
import math
from pathlib import Path
import platform
from time import perf_counter

import pyarrow as pa
import pyarrow.parquet as pq

CARPETA = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "cartera_0907", CARPETA.parent / "03_python_read_write/intercambio_python.py")
cartera = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cartera)
FUENTE = cartera.FUENTE

# Una diferencia por comparacion con base; no se busca una configuracion ganadora.
CONFIGURACIONES = {
    "base": dict(compression="NONE", use_dictionary=False, row_group_size=14),
    "snappy": dict(compression="snappy", use_dictionary=False, row_group_size=14),
    "diccionario": dict(compression="NONE", use_dictionary=True, row_group_size=14),
    "grupos7": dict(compression="NONE", use_dictionary=False, row_group_size=7),
}


def inspeccionar(ruta):
    """Solo metadatos: no decodifica columnas ni certifica claves/valores."""
    ruta = Path(ruta)
    with pq.ParquetFile(ruta) as lector:
        m = lector.metadata
        columnas = []
        for i in range(m.num_row_groups):
            grupo = m.row_group(i)
            for j in range(grupo.num_columns):
                c = grupo.column(j)
                s = c.statistics
                columnas.append(dict(
                    archivo=ruta.name, grupo=i, filas_grupo=grupo.num_rows,
                    columna=c.path_in_schema, tipo_fisico=c.physical_type,
                    codec=c.compression, codificaciones="|".join(c.encodings),
                    bytes_comprimidos=c.total_compressed_size,
                    bytes_sin_comprimir=c.total_uncompressed_size,
                    estadisticas=c.is_stats_set,
                    nulos=s.null_count if s is not None and s.has_null_count else None,
                    minimo=str(s.min) if s is not None and s.has_min_max else None,
                    maximo=str(s.max) if s is not None and s.has_min_max else None))
        return dict(archivo=ruta.name, bytes_archivo=ruta.stat().st_size,
                    filas=m.num_rows, grupos=m.num_row_groups,
                    esquema=str(lector.schema_arrow), creado_por=m.created_by,
                    columnas=columnas)


def escribir_csv(ruta, filas):
    with Path(ruta).open("x", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0]))
        escritor.writeheader()
        escritor.writerows(filas)


def crear_experimento(destino, ruta_csv=FUENTE, repeticiones=3):
    """Escribe archivos nuevos; no mide preparacion, validacion ni inspeccion."""
    if type(repeticiones) is not int or repeticiones < 1:
        raise ValueError("repeticiones debe ser entero positivo")
    if not pa.Codec.is_available("snappy"):
        raise ValueError("Snappy no disponible; conserva el mensaje, no sustituyas el codec")
    tabla = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    medidas, columnas = [], []
    nombres = list(CONFIGURACIONES)
    for repeticion in range(1, repeticiones + 1):
        # Rotacion explicita: evita dejar siempre la misma configuracion al inicio.
        desplazamiento = (repeticion - 1) % len(nombres)
        orden = nombres[desplazamiento:] + nombres[:desplazamiento]
        for posicion, nombre in enumerate(orden, 1):
            config = CONFIGURACIONES[nombre]
            ruta = destino / f"{nombre}_{repeticion:02d}.parquet"
            inicio = perf_counter()
            with ruta.open("xb") as archivo:
                pq.write_table(tabla, archivo, version="2.6", write_statistics=True, **config)
            escritura = perf_counter() - inicio
            inicio = perf_counter()
            with pq.ParquetFile(ruta) as lector:
                observada = lector.read(use_threads=False)
            lectura = perf_counter() - inicio
            # Fuera de ambos intervalos: la igualdad es condicion del experimento.
            cartera.comparar_tablas(tabla, observada)
            detalle = inspeccionar(ruta)
            columnas.extend(detalle["columnas"])
            medidas.append(dict(configuracion=nombre, repeticion=repeticion, orden=posicion,
                archivo=ruta.name, codec=config["compression"],
                diccionario=config["use_dictionary"], filas_por_grupo=config["row_group_size"],
                filas=tabla.num_rows, grupos=detalle["grupos"],
                bytes_archivo=detalle["bytes_archivo"], escritura_s=escritura, lectura_s=lectura))
    escribir_csv(destino / "mediciones.csv", medidas)
    escribir_csv(destino / "metadatos.csv", columnas)
    with (destino / "sesion.json").open("x", encoding="utf-8") as archivo:
        json.dump(dict(python=platform.python_version(), pyarrow=pa.__version__,
            plataforma=platform.platform(), repeticiones=repeticiones,
            lectura="completa, use_threads=False, mmap=False; despues de escribir",
            reloj="perf_counter; segundos transcurridos", cache="no controlada",
            persistencia="cierre de API; sin fsync ni medida de persistencia fisica",
            version_parquet="2.6", estadisticas=True,
            fuente="CSV reconstruido fuera del intervalo", **cartera.resumir(tabla)),
            archivo, ensure_ascii=False, indent=2)
    return medidas


def verificar_experimento(destino, ruta_csv=FUENTE, repeticiones=3):
    """Solo lectura: archivos esperados, esquema/valores y notas de tamano/grupos.

    Los tiempos son observaciones historicas: no se pueden autenticar releyendo.
    """
    if type(repeticiones) is not int or repeticiones < 1:
        raise ValueError("repeticiones debe ser entero positivo")
    destino = Path(destino)
    esperados = {f"{n}_{r:02d}.parquet" for n in CONFIGURACIONES
                 for r in range(1, repeticiones + 1)}
    entradas = list(destino.iterdir())
    if {p.name for p in entradas} != esperados | {"mediciones.csv", "metadatos.csv", "sesion.json"}:
        raise ValueError("Archivos ausentes o adicionales en el experimento")
    if any(not p.is_file() for p in entradas):
        raise ValueError("El experimento debe contener solo archivos")
    tabla = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    columnas_releidas = []
    with (destino / "mediciones.csv").open(encoding="utf-8", newline="") as archivo:
        medidas = list(csv.DictReader(archivo))
    if len(medidas) != len(esperados) or {f["archivo"] for f in medidas} != esperados:
        raise ValueError("Inventario de mediciones distinto")
    for f in medidas:
        config = CONFIGURACIONES[f["configuracion"]]
        repeticion = int(f["repeticion"])
        if f["archivo"] != f'{f["configuracion"]}_{repeticion:02d}.parquet':
            raise ValueError("Archivo/configuracion distintos")
        ruta = destino / f["archivo"]
        with pq.ParquetFile(ruta) as lector:
            cartera.comparar_tablas(tabla, lector.read(use_threads=False))
        detalle = inspeccionar(ruta)
        columnas_releidas.extend(detalle["columnas"])
        tamano_grupo = config["row_group_size"]
        # PyArrow escribe un grupo de cero filas para la tabla vacia.
        grupos = max(1, math.ceil(tabla.num_rows / tamano_grupo))
        codec = "UNCOMPRESSED" if config["compression"] == "NONE" else "SNAPPY"
        if (int(f["bytes_archivo"]) != detalle["bytes_archivo"] or
                int(f["filas"]) != tabla.num_rows or int(f["grupos"]) != detalle["grupos"] or
                detalle["grupos"] != grupos or f["codec"] != config["compression"] or
                f["diccionario"] != str(config["use_dictionary"]) or
                int(f["filas_por_grupo"]) != tamano_grupo or
                any(c["filas_grupo"] > tamano_grupo for c in detalle["columnas"]) or
                any(not c["estadisticas"] for c in detalle["columnas"] if c["filas_grupo"]) or
                (not config["use_dictionary"] and any(
                    "RLE_DICTIONARY" in c["codificaciones"] for c in detalle["columnas"])) or
                any(c["codec"] != codec for c in detalle["columnas"])):
            raise ValueError("Metadatos o configuracion distintos del registro")
        for campo in ("escritura_s", "lectura_s"):
            if not math.isfinite(float(f[campo])) or float(f[campo]) < 0:
                raise ValueError("Tiempo invalido en el registro")
    with (destino / "metadatos.csv").open(encoding="utf-8", newline="") as archivo:
        anotadas = list(csv.DictReader(archivo))
    actuales = [{k: "" if v is None else str(v) for k, v in c.items()}
                for c in columnas_releidas]
    clave = lambda c: (c["archivo"], int(c["grupo"]), c["columna"])
    if sorted(anotadas, key=clave) != sorted(actuales, key=clave):
        raise ValueError("Notas de metadatos distintas de los archivos reales")
    return cartera.resumir(tabla)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    accion = parser.add_mutually_exclusive_group(required=True)
    accion.add_argument("--crear", type=Path)
    accion.add_argument("--verificar", type=Path)
    accion.add_argument("--inspeccionar", type=Path)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    parser.add_argument("--repeticiones", type=int, default=3)
    args = parser.parse_args()
    if args.crear is not None:
        resultado = crear_experimento(args.crear, args.fuente, args.repeticiones)
    elif args.verificar is not None:
        resultado = verificar_experimento(args.verificar, args.fuente, args.repeticiones)
    else:
        resultado = inspeccionar(args.inspeccionar)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
