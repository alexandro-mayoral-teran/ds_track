"""Preparación editorial 11.01 con biblioteca estándar; no ejecuta Quarto."""

import argparse
import csv
import re
import shutil
from pathlib import Path


def preparar(origen: Path, destino: Path) -> None:
    """Comprueba esta muestra de seis claves y crea un borrador en carpeta nueva."""
    columnas = ["credito_id", "fecha_corte", "saldo_mxn"]
    fechas = ["2026-09-30", "2026-10-31"]
    ids = ["001", "002", "003"]
    with origen.open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != columnas:
            raise ValueError("Se requieren las tres columnas del contrato, en orden")
        filas = list(lector)
    esperadas = {(i, f) for i in ids for f in fechas}
    valores = {}
    for fila in filas:
        clave = (fila["credito_id"], fila["fecha_corte"])
        texto = fila["saldo_mxn"]
        if (None in fila or clave not in esperadas or clave in valores
                or texto is None or re.fullmatch(r"0|[1-9][0-9]{0,6}", texto) is None):
            raise ValueError("Clave inválida/repetida o saldo fuera del contrato")
        saldo = int(texto)
        if saldo > 1_000_000:
            raise ValueError("El saldo excede 1000000 MXN")
        valores[clave] = saldo
    if set(valores) != esperadas:
        raise ValueError("Se necesitan los tres créditos en ambos cortes: seis filas")
    totales = [sum(valores[i, f] for i in ids) for f in fechas]
    diferencia = totales[1] - totales[0]
    # El porcentaje solo tiene sentido si existe una base distinta de cero.
    porcentaje = (f"{100 * diferencia / totales[0]:.2f}%"
                  if totales[0] != 0 else "no definido (base inicial cero)")
    direccion = "aumentó" if diferencia > 0 else "disminuyó" if diferencia < 0 else "no cambió"
    borrador = f"""# Saldo observado de tres créditos ficticios

Documento de preparación editorial generado con Python; todavía no es un reporte Quarto.

## Pregunta y público

Para una persona que revisa la cartera: ¿cómo cambió el saldo observado de los
mismos tres créditos entre 2026-09-30 y 2026-10-31?

## Hallazgo

El saldo total {direccion}: pasó de {totales[0]} a {totales[1]} MXN.
La diferencia octubre menos septiembre es {diferencia} MXN; la variación sobre
septiembre es {porcentaje}. La base común contiene {len(ids)} créditos.

## Evidencia y método

| Corte | Créditos | Saldo (MXN) |
| --- | --- | --- |
| {fechas[0]} | {len(ids)} | {totales[0]} |
| {fechas[1]} | {len(ids)} | {totales[1]} |

Fuente: fuente.csv, copia de la entrada sintética de esta preparación.
Una fila representa un crédito en un corte. Se comprobaron las seis claves
esperadas, sin ausencias ni duplicados, y saldos enteros entre 0 y 1000000 MXN.
Se sumó por fecha sobre los mismos IDs. pares.csv permite revisar cada cambio;
resumen.csv conserva los totales. La tasa se presenta con dos decimales.

## Límites y revisión

Son saldos observados de una muestra ficticia, no desembolsos ni pagos del mes.
No se conoce la causa del cambio ni se describe una cartera real completa.
Revisar las tablas y la claridad del texto antes de preparar el documento Quarto.
"""
    # Se valida antes de crear la carpeta; mkdir rechaza destinos existentes.
    destino.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(origen, destino / "fuente.csv")
    with (destino / "resumen.csv").open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["fecha_corte", "creditos", "saldo_mxn"])
        escritor.writerows((f, len(ids), t) for f, t in zip(fechas, totales))
    with (destino / "pares.csv").open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["credito_id", "septiembre_mxn", "octubre_mxn", "diferencia_mxn"])
        for i in ids:
            a, b = (valores[i, f] for f in fechas)
            escritor.writerow([i, a, b, b - a])
    (destino / "borrador.md").write_text(borrador, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path, help="Carpeta nueva para la preparación")
    parser.add_argument("--fuente", type=Path, default=Path(__file__).with_name("cartera.csv"))
    args = parser.parse_args()
    preparar(args.fuente, args.destino)
    print(f"Preparación creada: {args.destino}")
