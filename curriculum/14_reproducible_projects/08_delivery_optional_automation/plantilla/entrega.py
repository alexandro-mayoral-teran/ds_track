"""14.08: crear, verificar o copiar fuentes. Verificar nunca ejecuta código recibido."""
from pathlib import Path
import argparse
import csv
from datetime import datetime
import re
import shutil
from ejecutar import RAIZ, verificar_entorno
from modelo import leer, cargar_fuente
from pipeline import tablas_esperadas, comprobar, md5
from integracion import verificar as verificar_reporte, vista, documento, normalizar_html

CASOS = ("octubre", "septiembre", "vacio")


def catalogo():
    columnas, filas = leer(RAIZ / "catalogo.csv")
    nombres = [f["archivo"] for f in filas]
    if columnas != ["archivo"] or len(nombres) != 60 or len(set(nombres)) != 60 or nombres != sorted(nombres):
        raise ValueError("Catalogo local incompatible")
    for n in nombres:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*", n) or any(p in (".", "..") for p in n.split("/")):
            raise ValueError("Ruta no admitida en catalogo local")
    return nombres


def inventario(raiz):
    raiz = Path(raiz)
    if raiz.is_symlink() or raiz.is_junction() or not raiz.is_dir():
        raise ValueError("Carpeta ausente o enlazada")
    archivos = []
    def visitar(carpeta):
        for p in carpeta.iterdir():
            if p.is_symlink() or p.is_junction():
                raise ValueError("Enlace no admitido: " + str(p))
            if p.is_dir(): visitar(p)
            elif p.is_file(): archivos.append(p.relative_to(raiz).as_posix())
            else: raise ValueError("Archivo no regular")
    visitar(raiz)
    return sorted(archivos)


def nombres_paquete():
    nombres = ["LEEME.md", "ENTREGA.csv", "MANIFIESTO.csv"]
    nombres += ["fuentes/" + n for n in catalogo()]
    for caso in CASOS:
        nombres += [f"muestra/salidas/{caso}_integrado/" + n for n in ("seleccion.csv", "contexto.csv", "insumos.csv", "COMPLETO.csv")]
        nombres += [f"muestra/reportes/{caso}/" + n for n in ("seleccion.csv", "contexto.csv", "producto.csv", "reporte.qmd", "reporte.html")]
    return sorted(nombres)


def escribir(ruta, filas):
    with ruta.open("x", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(filas)


def referencia_externa(entrega, referencia):
    externa = Path(referencia).resolve(strict=True)
    if externa.is_relative_to(entrega):
        raise ValueError("La referencia debe estar fuera de la entrega")
    datos = cargar_fuente(externa)
    empaquetados = cargar_fuente(entrega / "fuentes/datos/entrada/cartera.csv")
    ordenar = lambda filas: sorted(filas, key=lambda f: (f["id_credito"], f["fecha_corte"]))
    if ordenar(datos) != ordenar(empaquetados):
        raise ValueError("Fuente distinta de la referencia externa por clave/campo")


def verificar(entrega, referencia):
    entrega = Path(entrega).absolute()
    actuales = inventario(entrega)
    entrega = entrega.resolve(strict=True)
    if RAIZ.is_relative_to(entrega):
        raise ValueError("Usar herramientas revisadas fuera de la entrega")
    if actuales != nombres_paquete():
        raise ValueError("Inventario incompatible: faltan archivos o hay extras")
    if leer(entrega / "ENTREGA.csv") != (["clave", "valor"], [{"clave": "esquema", "valor": "1408-v1"}, {"clave": "app", "valor": "streamlit"}]):
        raise ValueError("Esquema o ruta distinta; usar revisor Python para Streamlit")
    columnas, manifiesto = leer(entrega / "MANIFIESTO.csv")
    esperados = [n for n in actuales if n != "MANIFIESTO.csv"]
    if columnas != ["archivo", "md5"] or manifiesto != [{"archivo": n, "md5": md5(entrega / n)} for n in esperados]:
        raise ValueError("Manifiesto incompatible o huellas distintas")
    if leer(entrega / "fuentes/catalogo.csv") != leer(RAIZ / "catalogo.csv"):
        raise ValueError("Catalogo recibido distinto del catalogo local revisado")
    referencia_externa(entrega, referencia)
    fuente = entrega / "fuentes"
    for caso in CASOS:
        archivo = "config/" + caso + ".csv"
        cfg, tablas = tablas_esperadas(archivo, raiz=fuente)  # Código del revisor, datos recibidos.
        esperado = {"version_reglas": "1401-v1", "entrada": "datos/entrada/cartera.csv", "corte": "2026-09-30" if caso == "septiembre" else "2026-10-31",
                    "segmentos": "servicios" if caso == "vacio" else "comercio|servicios", "minimo_texto": "1901" if caso == "vacio" else "2000",
                    "app": "streamlit", "salida": "salidas/" + caso + "_integrado"}
        if any(cfg[k] != v for k, v in esperado.items()):
            raise ValueError("Configuracion distinta del plan de entrega")
        salida = entrega / "muestra" / cfg["salida"]
        comprobar(salida, tablas)
        reporte = entrega / "muestra/reportes" / caso
        for n in ("seleccion.csv", "contexto.csv"):
            columnas, filas = leer(reporte / n)
            if [columnas] + [[f[c] for c in columnas] for f in filas] != tablas[n]:
                raise ValueError("Tabla del reporte distinta del calculo revisado")
        columnas, filas = leer(reporte / "producto.csv")
        claves = ["config", "entrega", "revision", "comprobado_utc"]
        if columnas != ["clave", "valor"] or [f["clave"] for f in filas] != claves:
            raise ValueError("Metadatos del reporte incompatibles")
        meta = {f["clave"]: f["valor"] for f in filas}
        if any(meta[k] != v for k, v in {"config": archivo, "entrega": cfg["salida"], "revision": md5(salida / "COMPLETO.csv")}.items()):
            raise ValueError("Reporte de otra entrega/configuracion")
        instante = datetime.strptime(meta["comprobado_utc"], "%Y-%m-%dT%H:%M:%SZ")
        if instante.strftime("%Y-%m-%dT%H:%M:%SZ") != meta["comprobado_utc"]:
            raise ValueError("Hora UTC no canonica")
        columnas, *filas = tablas["seleccion.csv"]
        p = dict(meta, contexto=dict(zip(*tablas["contexto.csv"])), seleccion=[dict(zip(columnas, f)) for f in filas])
        if (reporte / "reporte.qmd").read_text(encoding="utf-8") != documento(p):
            raise ValueError("Fuente del reporte distinta")
        html = (reporte / "reporte.html").read_text(encoding="utf-8")
        fragmentos = re.findall(r"<!-- inicio-vista-1407 -->.*?<!-- fin-vista-1407 -->", html, re.S)
        if len(fragmentos) != 1 or normalizar_html(fragmentos[0]) != normalizar_html(vista(p)):
            raise ValueError("HTML sin la vista conciliada")
    print("Entrega conciliada con referencia externa. No autentica ni aprueba el codigo recibido.")
    return entrega


def destino_nuevo(destino, origen):
    ruta = Path(destino).absolute()
    if ruta.exists() or ruta.is_symlink() or ruta.is_junction():
        raise ValueError("Destino ocupado; conservar y elegir otro")
    ruta = ruta.resolve()
    if ruta.is_relative_to(origen.resolve()):
        raise ValueError("El destino debe estar fuera del origen")
    return ruta


def crear(destino, referencia):
    verificar_entorno()
    destino = destino_nuevo(destino, RAIZ)
    for caso in CASOS: verificar_reporte(caso, "config/" + caso + ".csv", "streamlit")
    # Validar todos los orígenes antes de abrir la carpeta de entrega.
    pares = [(RAIZ / n, "fuentes/" + n) for n in catalogo()]
    for caso in CASOS:
        for relativa in nombres_paquete():
            if relativa.startswith(f"muestra/salidas/{caso}_integrado/") or relativa.startswith(f"muestra/reportes/{caso}/"):
                pares.append((RAIZ / relativa.removeprefix("muestra/"), relativa))
    for p, _ in pares:
        if p.is_symlink() or p.is_junction() or not p.is_file() or not p.resolve().is_relative_to(RAIZ):
            raise ValueError("Origen ausente, enlazado o fuera del proyecto")
    destino.mkdir(parents=True, exist_ok=False)
    for origen, relativa in pares:
        final = destino / relativa; final.parent.mkdir(parents=True, exist_ok=True)
        with origen.open("rb") as entrada, final.open("xb") as salida: shutil.copyfileobj(entrada, salida)
    shutil.copyfile(RAIZ / "LEEME_ENTREGA.md", destino / "LEEME.md")
    escribir(destino / "ENTREGA.csv", [["clave", "valor"], ["esquema", "1408-v1"], ["app", "streamlit"]])
    escribir(destino / "MANIFIESTO.csv", [["archivo", "md5"]] + [[n, md5(destino / n)] for n in inventario(destino)])
    verificar(destino, referencia)
    print("Entrega nueva creada y verificada:", destino)
    return destino


def copiar(entrega, destino, referencia):
    entrega = verificar(entrega, referencia)
    destino = destino_nuevo(destino, entrega)
    destino.mkdir(parents=True, exist_ok=False)
    for n in catalogo():
        final = destino / n; final.parent.mkdir(parents=True, exist_ok=True)
        with (entrega / "fuentes" / n).open("rb") as entrada, final.open("xb") as salida: shutil.copyfileobj(entrada, salida)
    print("Solo fuentes copiadas. Revisarlas antes de restaurar y ejecutar:", destino)
    return destino


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="accion", required=True)
    for accion in ("crear", "verificar", "copiar"):
        q = sub.add_parser(accion)
        if accion != "crear": q.add_argument("entrega")
        if accion != "verificar": q.add_argument("destino")
        q.add_argument("--referencia", required=True)
    a = p.parse_args()
    if a.accion == "crear": crear(a.destino, a.referencia)
    elif a.accion == "verificar": verificar(a.entrega, a.referencia)
    else: copiar(a.entrega, a.destino, a.referencia)
