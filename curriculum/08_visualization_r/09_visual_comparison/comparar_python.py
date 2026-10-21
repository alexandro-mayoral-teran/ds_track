"""Referencia independiente de la muestra 07.09/07.10 y cierre visual 08.09.

Lee el CSV original, reconstruye reglas y concilia tablas R antes de dibujar.
Biblioteca estandar para datos; Matplotlib para la figura. Importar no exporta.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

COLUMNAS = ["id_credito", "segmento", "fecha_corte", "fecha_alta", "saldo_mxn"]
CORTES = ("2026-09-30", "2026-10-31")
SEGMENTOS = {"consumo", "servicios", "comercio", "educacion"}
AUDITORIA = ["numero_registro", *COLUMNAS, "motivos"]


def leer_csv(ruta):
    with Path(ruta).open(encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        nombres = lector.fieldnames
        if not nombres or len(set(nombres)) != len(nombres):
            raise ValueError("Cabecera ausente o repetida")
        filas = list(lector)
        if any(None in fila or None in fila.values() for fila in filas):
            raise ValueError("Registro con distinta cantidad de campos")
    return nombres, filas


def fecha_iso(texto):
    limpio = texto.strip()
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", limpio):
        return None
    if not 1900 <= int(limpio[:4]) <= 2100:
        return None
    try:
        return date.fromisoformat(limpio)
    except ValueError:
        return None


def reconstruir(ruta):
    nombres, fuente = leer_csv(ruta)
    if nombres != COLUMNAS:
        raise ValueError("Esquema original distinto del contrato")
    trabajo = []
    for numero, original in enumerate(fuente, start=1):
        # El contrato R exige saldo integer presente y no negativo.
        saldo = original["saldo_mxn"].strip()
        if not re.fullmatch(r"-?[0-9]+", saldo) or not 0 <= int(saldo) <= 2147483647:
            raise ValueError(f"Saldo fuera del contrato en registro {numero}")
        segmento = original["segmento"].strip().lower()
        if segmento == "educación":
            segmento = "educacion"
        fila = dict(numero_registro=str(numero), id_credito=original["id_credito"].strip(),
                    segmento=segmento, saldo_mxn=str(int(saldo)))
        for campo in ("fecha_corte", "fecha_alta"):
            fecha = fecha_iso(original[campo])
            fila[campo] = fecha.isoformat() if fecha else ""
        trabajo.append(fila)
    claves = Counter((f["id_credito"], f["fecha_corte"]) for f in trabajo
                     if f["id_credito"] and f["fecha_corte"])
    aceptados, rechazados = [], []
    for original, fila in zip(fuente, trabajo):
        identificador, segmento = fila["id_credito"], fila["segmento"]
        corte, alta = fila["fecha_corte"], fila["fecha_alta"]
        # Mismo orden de motivos que en R; todas las repeticiones se apartan.
        reglas = {
            "id_ausente": not identificador,
            "id_formato": bool(identificador) and not re.fullmatch(r"[0-9]{3}", identificador),
            "segmento_ausente": not segmento,
            "segmento_fuera_catalogo": bool(segmento) and segmento not in SEGMENTOS,
            "fecha_corte_ausente": not original["fecha_corte"].strip(),
            "fecha_corte_invalida": bool(original["fecha_corte"].strip()) and not corte,
            "fecha_alta_ausente": not original["fecha_alta"].strip(),
            "fecha_alta_invalida": bool(original["fecha_alta"].strip()) and not alta,
            "alta_posterior_corte": bool(alta and corte) and alta > corte,
            "clave_repetida": bool(identificador and corte) and claves[identificador, corte] > 1,
        }
        fila["motivos"] = "; ".join(nombre for nombre, incumple in reglas.items() if incumple)
        (rechazados if fila["motivos"] else aceptados).append(fila)
    por_corte = [{f["id_credito"]: f for f in aceptados if f["fecha_corte"] == corte}
                 for corte in CORTES]
    ids = sorted(por_corte[0].keys() & por_corte[1].keys())
    pares = []
    for identificador in ids:
        sep, octu = (int(grupo[identificador]["saldo_mxn"]) for grupo in por_corte)
        pares.append(dict(id_credito=identificador, saldo_sep=str(sep), saldo_oct=str(octu),
                          diferencia_mxn=str(octu - sep)))
    resumen = [dict(fecha_corte=corte, creditos=str(len(ids)),
                    # Sin pares no hay saldo observado: R exporta NA como campo vacio.
                    saldo_mxn=str(sum(int(p[campo]) for p in pares)) if pares else "",
                    aceptados_corte=str(len(grupo)))
               for corte, campo, grupo in zip(CORTES, ("saldo_sep", "saldo_oct"), por_corte)]
    sin_pareja = [f for f in aceptados if f["fecha_corte"] in CORTES and f["id_credito"] not in ids]
    fuera = [f for f in aceptados if f["fecha_corte"] not in CORTES]
    return dict(aceptados=aceptados, rechazados=rechazados, base_comun=pares,
                datos_figura=resumen, sin_pareja=sin_pareja, fuera_cortes=fuera)


def conciliar(ruta, esperadas, columnas, clave):
    nombres, observadas = leer_csv(ruta)
    if not set(columnas) <= set(nombres):
        raise ValueError(f"Faltan columnas en {Path(ruta).name}")

    def indice(filas):
        resultado = {}
        for fila in filas:
            valor = fila[clave]
            if valor in resultado:
                raise ValueError(f"Clave repetida en {Path(ruta).name}: {valor}")
            resultado[valor] = tuple(fila[c] for c in columnas)
        return resultado

    if indice(observadas) != indice(esperadas):
        raise ValueError(f"No concilia {Path(ruta).name}; revisa claves, campos y motivos")


def comparar(fuente, entrega_r, destino):
    fuente, entrega_r, destino = map(Path, (fuente, entrega_r, destino))
    huella = hashlib.sha256(fuente.read_bytes()).hexdigest()
    datos = reconstruir(fuente)  # No usa los valores de la entrega R para calcular.
    for nombre in ("aceptados", "rechazados", "sin_pareja", "fuera_cortes"):
        conciliar(entrega_r / f"{nombre}.csv", datos[nombre], AUDITORIA, "numero_registro")
    conciliar(entrega_r / "base_comun.csv", datos["base_comun"],
              ["id_credito", "saldo_sep", "saldo_oct", "diferencia_mxn"], "id_credito")
    conciliar(entrega_r / "datos_figura.csv", datos["datos_figura"],
              ["fecha_corte", "creditos", "saldo_mxn", "aceptados_corte"], "fecha_corte")
    # Referencia de esta muestra, adicional a la conciliacion entre lenguajes.
    resumen = datos["datos_figura"]
    if not datos["base_comun"]:
        raise ValueError("No hay IDs comunes: conserva las tablas; no dibujes ceros")
    saldos = [int(f["saldo_mxn"]) for f in resumen]
    if (len(datos["aceptados"]), len(datos["rechazados"]), len(datos["base_comun"]), saldos) != (
            36, 12, 14, [29000, 31800]):
        raise ValueError("La fuente no reproduce los valores conocidos de esta practica")
    if destino.exists() or not destino.parent.is_dir():
        raise ValueError("Usa una carpeta nueva con carpeta madre existente")
    if hashlib.sha256(fuente.read_bytes()).hexdigest() != huella:
        raise ValueError("La fuente cambio durante la comprobacion")

    import matplotlib
    matplotlib.use("Agg")  # Exportar sin depender de una ventana interactiva.
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter

    diferencia = saldos[1] - saldos[0]
    porcentaje = 100 * diferencia / saldos[0] if saldos[0] else None
    fig, ax = plt.subplots(figsize=(9, 6), layout="constrained")
    ax.bar(CORTES, saldos, color="#246A86", width=0.6)
    ax.set(ylim=(0, 36000), xlabel="Fecha de corte", ylabel="Saldo observado (MXN)",
           title="Saldo de los mismos 14 créditos en dos cortes")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda valor, _: f"{valor:,.0f}".replace(",", " ")))
    for corte, saldo in zip(CORTES, saldos):
        ax.text(corte, saldo + 500, f"{saldo:,}".replace(",", " "), ha="center")
    fig.suptitle("Octubre aumenta 2 800 MXN respecto de septiembre", fontsize=14)
    fig.supxlabel("Datos sintéticos DS Track. Base común: 14/18 aceptados por fecha.\n"
                  "Cambio: 9.66% del saldo inicial. Comparación descriptiva; no identifica causas.",
                  fontsize=10)
    destino.mkdir()  # Una escritura fallida deja salida parcial; no se sobreescribe.
    try:
        for nombre in ("base_comun", "datos_figura"):
            filas = datos[nombre]
            with (destino / f"{nombre}.csv").open("w", encoding="utf-8", newline="") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=list(filas[0]))
                escritor.writeheader()
                escritor.writerows(filas)
        fig.savefig(destino / "saldo_comun_python.png", dpi=144, facecolor="white")
        informe = dict(fuente_sha256=huella, python=sys.version.split()[0],
                       matplotlib=matplotlib.__version__, aceptados=36, rechazados=12,
                       ids_comunes=14, diferencia_mxn=diferencia, cambio_porcentaje=porcentaje,
                       tablas_conciliadas=["aceptados", "rechazados", "sin_pareja", "fuera_cortes",
                                           "base_comun", "datos_figura"],
                       alcance="Campos de auditoria, pares y resumen; no compara pixeles ni RDS")
        (destino / "comparacion.json").write_text(
            json.dumps(informe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    finally:
        plt.close(fig)
    print(f"6 tablas conciliadas; 14 IDs, 29000/31800 MXN; cambio {porcentaje:.2f}%.")
    return datos


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fuente", help="CSV original de la practica R")
    parser.add_argument("entrega_r", help="Carpeta nueva generada por cerrar_visual")
    parser.add_argument("destino", help="Carpeta inexistente para la salida Python")
    argumentos = parser.parse_args()
    comparar(argumentos.fuente, argumentos.entrega_r, argumentos.destino)
