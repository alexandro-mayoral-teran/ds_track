"""Entrega local de 12.09. Crear escribe un destino nuevo; verificar solo lee.

La referencia de verificación es independiente del análisis de la aplicación.
Las huellas comprueban integridad declarada, no autenticidad ni ejecuciones pasadas.
"""

import argparse
import csv
from datetime import date
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import re
import shutil

BASE = Path(__file__).resolve().parent
COLUMNAS = ["id_credito", "segmento", "fecha_corte", "saldo_mxn"]
ARCHIVOS = (
    "app.py", "cartera.py", "cartera.csv", "configuracion.py", "ejecutar.py",
    "cache_analisis.py", "entradas.py", "graficos.py", "salidas.py",
    "revisar_descarga.py", "minimo.py", "minimo_pruebas.py", "pruebas_modelo.py",
    "pruebas_app.py", "entrega.py", "README.md", "pyproject.toml", "uv.lock",
)
CASOS = {
    "octubre": {"corte": "2026-10-31", "segmentos": ["comercio", "servicios"], "minimo_mxn": 2000},
    "septiembre": {"corte": "2026-09-30", "segmentos": ["comercio", "servicios"], "minimo_mxn": 2000},
    "frontera": {"corte": "2026-09-30", "segmentos": ["comercio", "servicios"], "minimo_mxn": 2001},
    "servicios": {"corte": "2026-10-31", "segmentos": ["servicios"], "minimo_mxn": 1900},
    "vacio": {"corte": "2026-10-31", "segmentos": [], "minimo_mxn": 0},
    "sin_corte": {"corte": "2026-11-30", "segmentos": ["comercio", "servicios"], "minimo_mxn": 0},
}
VERSION_REGLAS = "1205-v1"
CONTRATO = {
    "version_entrega": 1, "unidad_fila": "credito/corte", "clave": ["id_credito", "fecha_corte"],
    "columnas": COLUMNAS, "unidad_saldo": "MXN", "saldo_entero": [0, 1_000_000],
    "ausencias": "no admitidas", "validacion": "fuente completa antes de filtrar",
    "version_reglas": VERSION_REGLAS, "casos": CASOS,
}


def leer_json(ruta):
    def pares_unicos(pares):
        resultado = {}
        for clave, valor in pares:
            if clave in resultado:
                raise ValueError(f"Clave JSON repetida: {clave}")
            resultado[clave] = valor
        return resultado

    def constante_invalida(valor):
        raise ValueError(f"Constante JSON no válida: {valor}")

    return json.loads(Path(ruta).read_text(encoding="utf-8"),
                      object_pairs_hook=pares_unicos, parse_constant=constante_invalida)


def escribir_json(ruta, valor):
    Path(ruta).write_text(json.dumps(valor, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def exigir_igual(obtenido, esperado, mensaje):
    # Comparación JSON que distingue bool/int y 1/1.0, además de claves y valores.
    serializar = lambda v: json.dumps(v, sort_keys=True, ensure_ascii=False, allow_nan=False)
    if serializar(obtenido) != serializar(esperado):
        raise ValueError(mensaje)


def leer_referencia(ruta):
    """Contrato independiente con Python estándar; no importa cartera ni Streamlit."""
    contenido = Path(ruta).read_bytes()
    lector = csv.DictReader(StringIO(contenido.decode("utf-8")), strict=True)
    if lector.fieldnames != COLUMNAS:
        raise ValueError("Referencia CSV: encabezado incorrecto.")
    filas, claves = [], set()
    for fila in lector:
        if set(fila) != set(COLUMNAS) or any(v is None for v in fila.values()):
            raise ValueError("Referencia CSV: número de campos incorrecto.")
        if not re.fullmatch(r"[0-9]{3}", fila["id_credito"]):
            raise ValueError("Referencia: ID debe conservar tres dígitos.")
        corte = fila["fecha_corte"]
        if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", corte):
            raise ValueError("Referencia: fecha ISO requerida.")
        fecha = date.fromisoformat(corte)
        if not 1900 <= fecha.year <= 2100 or fila["segmento"] not in ("comercio", "servicios"):
            raise ValueError("Referencia: fecha o segmento fuera del contrato.")
        if not re.fullmatch(r"0|[1-9][0-9]*", fila["saldo_mxn"]):
            raise ValueError("Referencia: saldo entero sin signos ni decimales.")
        fila["saldo_mxn"] = int(fila["saldo_mxn"])
        if fila["saldo_mxn"] > 1_000_000:
            raise ValueError("Referencia: saldo fuera del rango.")
        clave = (fila["id_credito"], corte)
        if clave in claves:
            raise ValueError("Referencia: clave repetida, incluso fuera del filtro.")
        claves.add(clave)
        filas.append(fila)
    return sorted(filas, key=lambda f: (f["id_credito"], f["fecha_corte"]))


def referencia_caso(filas, filtros):
    universo, seleccion = [], []
    for fila in filas:
        if fila["fecha_corte"] == filtros["corte"]:
            universo.append(fila)
            if fila["segmento"] in filtros["segmentos"] and fila["saldo_mxn"] >= filtros["minimo_mxn"]:
                seleccion.append(dict(fila))
    seleccion.sort(key=lambda f: f["id_credito"])
    return {
        **filtros,
        "universo": {"cantidad": len(universo), "saldo_mxn": sum(f["saldo_mxn"] for f in universo)},
        "seleccion": seleccion,
        "indicadores": {"cantidad": len(seleccion), "saldo_mxn": sum(f["saldo_mxn"] for f in seleccion),
                        "porcentaje_creditos": len(seleccion) / len(universo) * 100 if universo else None},
    }


def inventario():
    archivos = set(ARCHIVOS) | {"contrato.json"}
    for nombre in CASOS:
        archivos.add(f"resultados/{nombre}/analisis.json")
        if nombre != "sin_corte":
            archivos |= {f"resultados/{nombre}/seleccion.csv", f"resultados/{nombre}/contexto.json"}
    return archivos


def comprobar_archivos(carpeta):
    """Rechaza enlaces y archivos extra; no inspecciona entornos ni bytecode."""
    encontrados = set()
    for ruta in carpeta.rglob("*"):
        relativo = ruta.relative_to(carpeta)
        if any(p in (".venv", "__pycache__") for p in relativo.parts):
            continue
        if ruta.is_symlink():
            raise ValueError(f"No se permiten enlaces en la entrega: {relativo}")
        if ruta.is_file():
            encontrados.add(relativo.as_posix())
    if encontrados != inventario() | {"manifiesto.json"}:
        raise ValueError("Inventario incompleto o archivos extra en la entrega.")


def verificar(carpeta, referencia):
    """Solo lee: no importa ni ejecuta código de la entrega que está revisando."""
    carpeta, referencia = Path(carpeta).resolve(), Path(referencia).resolve()
    if referencia.is_relative_to(carpeta):
        raise ValueError("La referencia debe estar FUERA de la entrega revisada.")
    esperadas = leer_referencia(referencia)
    comprobar_archivos(carpeta)
    exigir_igual(leer_json(carpeta / "contrato.json"), CONTRATO, "Contrato/casos alterados.")
    manifiesto = leer_json(carpeta / "manifiesto.json")
    if set(manifiesto) != {"version", "sha256"} or type(manifiesto["version"]) is not int or manifiesto["version"] != 1:
        raise ValueError("Manifiesto: formato inesperado.")
    if not isinstance(manifiesto["sha256"], dict) or set(manifiesto["sha256"]) != inventario():
        raise ValueError("Manifiesto: inventario incorrecto.")
    # Solo rutas conocidas: nunca seguir rutas arbitrarias del manifiesto.
    for nombre in sorted(inventario()):
        if sha256((carpeta / nombre).read_bytes()).hexdigest() != manifiesto["sha256"][nombre]:
            raise ValueError(f"Huella diferente: {nombre}")
    exigir_igual(leer_referencia(carpeta / "cartera.csv"), esperadas, "Fuente distinta de la referencia externa por ID/corte.")
    for nombre, filtros in CASOS.items():
        esperado = referencia_caso(esperadas, filtros)
        caso = carpeta / "resultados" / nombre
        exigir_igual(leer_json(caso / "analisis.json"), esperado, f"Análisis distinto por valores o filtros: {nombre}")
        if nombre == "sin_corte":
            # En este contrato noviembre no es una opción con registros.
            if esperado["universo"]["cantidad"]:
                raise ValueError("La referencia de cierre no admite registros de noviembre.")
            continue
        if not esperado["universo"]["cantidad"]:
            raise ValueError("La referencia de cierre requiere registros en septiembre y octubre.")
        contenido = (caso / "seleccion.csv").read_bytes()
        lector = csv.DictReader(StringIO(contenido.decode("utf-8")), strict=True)
        filas_csv = list(lector)
        esperado_csv = [{k: str(v) for k, v in f.items()} for f in esperado["seleccion"]]
        if lector.fieldnames != COLUMNAS or filas_csv != esperado_csv:
            raise ValueError(f"CSV distinto por campos, orden o valores: {nombre}")
        contexto = {
            "version_formato": 1, "version_reglas": VERSION_REGLAS, "unidad_saldo": "MXN",
            "filtros": filtros, "universo": esperado["universo"], "indicadores": esperado["indicadores"],
            "columnas_csv": COLUMNAS, "filas_csv": len(esperado_csv), "sha256_csv": sha256(contenido).hexdigest(),
        }
        exigir_igual(leer_json(caso / "contexto.json"), contexto, f"Contexto distinto: {nombre}")
    return {"casos": len(CASOS), "filas_fuente": len(esperadas), "archivos": len(inventario()) + 1}


def crear(destino):
    """Genera evidencia de terminal en una copia nueva; no simula una descarga real."""
    from cartera import analizar, leer_cartera
    from salidas import preparar_descargas

    destino = Path(destino).resolve()
    if destino.is_relative_to(BASE):
        raise ValueError("El destino debe estar fuera de la carpeta fuente.")
    for nombre in ARCHIVOS:
        if not (BASE / nombre).is_file():
            raise FileNotFoundError(f"Falta una fuente preparada: {nombre}")
    filas = leer_cartera(BASE / "cartera.csv")
    # Validar el alcance antes de crear la carpeta: cierre con dos cortes presentes.
    cortes = {f["fecha_corte"] for f in filas}
    if not {"2026-09-30", "2026-10-31"} <= cortes or "2026-11-30" in cortes:
        raise ValueError("El cierre requiere septiembre/octubre y noviembre sin registros.")
    resultados = {nombre: analizar(filas, f["corte"], f["segmentos"], f["minimo_mxn"]) for nombre, f in CASOS.items()}
    destino.mkdir(parents=True, exist_ok=False)
    for nombre in ARCHIVOS:
        shutil.copyfile(BASE / nombre, destino / nombre)
    escribir_json(destino / "contrato.json", CONTRATO)
    for nombre, resultado in resultados.items():
        carpeta = destino / "resultados" / nombre
        carpeta.mkdir(parents=True)
        escribir_json(carpeta / "analisis.json", resultado)
        if resultado["universo"]["cantidad"]:
            salida = preparar_descargas(resultado, VERSION_REGLAS)
            (carpeta / "seleccion.csv").write_bytes(salida["csv"])
            (carpeta / "contexto.json").write_bytes(salida["contexto"])
    huellas = {nombre: sha256((destino / nombre).read_bytes()).hexdigest() for nombre in sorted(inventario())}
    escribir_json(destino / "manifiesto.json", {"version": 1, "sha256": huellas})
    verificar(destino, BASE / "cartera.csv")
    return destino


def main():
    parser = argparse.ArgumentParser(description="12.09: crear una entrega nueva o verificarla sin modificarla.")
    acciones = parser.add_subparsers(dest="accion", required=True)
    nuevo = acciones.add_parser("crear")
    nuevo.add_argument("destino", type=Path)
    revisar = acciones.add_parser("verificar")
    revisar.add_argument("carpeta", type=Path)
    revisar.add_argument("--referencia", type=Path, required=True, help="CSV externo a la entrega, conservado por quien revisa.")
    args = parser.parse_args()
    try:
        if args.accion == "crear":
            print("Entrega creada:", crear(args.destino))
        else:
            print("Entrega conciliada:", verificar(args.carpeta, args.referencia))
            print("No se ejecutó la app ni se autenticaron archivos o sesiones históricas.")
    except (OSError, UnicodeError, ValueError, csv.Error, KeyError, TypeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
