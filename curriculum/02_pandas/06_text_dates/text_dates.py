"""Normalizar texto e interpretar fechas sin ocultar las entradas originales."""

from pathlib import Path

import pandas as pd


COLUMNAS = ["id_credito", "segmento", "fecha_corte", "fecha_alta", "saldo_mxn"]
TEXTOS = COLUMNAS[:-1]
SEGMENTOS = ["consumo", "servicios", "comercio", "educacion"]
FECHAS = ["fecha_corte", "fecha_alta"]
CLAVE = ["id_credito", "fecha_corte"]


def leer_fuente(ruta):
    tipos = {c: "string" for c in TEXTOS}
    tipos["saldo_mxn"] = "Int64"
    tabla = pd.read_csv(ruta, dtype=tipos, encoding="utf-8-sig",
                        keep_default_na=False, na_values=[""])
    if list(tabla.columns) != COLUMNAS:
        raise ValueError("Las columnas no coinciden con el diccionario")
    if tabla["saldo_mxn"].isna().any() or (tabla["saldo_mxn"] < 0).any():
        raise ValueError("Esta muestra requiere saldos enteros presentes y no negativos")
    return tabla


def limpiar_texto(serie):
    # Un campo formado solo por espacios pasa a ausencia; no sustituir por cero.
    return serie.str.strip().replace("", pd.NA)


def interpretar_fecha(texto):
    # Verificar también la forma literal: to_datetime puede admitir partes sin ceros.
    forma = texto.str.fullmatch(r"\d{4}-\d{2}-\d{2}").fillna(False)
    fecha = pd.to_datetime(texto.where(forma), format="%Y-%m-%d", errors="coerce")
    invalida = texto.notna() & fecha.isna()
    return fecha, invalida


def preparar(tabla):
    trabajo = tabla.reset_index(drop=True).copy()
    trabajo.insert(0, "numero_registro", pd.Series(range(1, len(tabla) + 1), dtype="Int64"))
    for columna in TEXTOS:
        trabajo[columna + "_original"] = trabajo[columna]
        trabajo[columna] = limpiar_texto(trabajo[columna])
    trabajo["segmento"] = trabajo["segmento"].str.lower().replace({"educación": "educacion"})
    reglas = {
        "id_ausente": trabajo["id_credito"].isna(),
        "id_formato": trabajo["id_credito"].notna() & ~trabajo["id_credito"].str.fullmatch(r"\d{3}"),
        "segmento_ausente": trabajo["segmento"].isna(),
        "segmento_fuera_catalogo": trabajo["segmento"].notna() & ~trabajo["segmento"].isin(SEGMENTOS),
    }
    for columna in FECHAS:
        texto = trabajo[columna].copy()
        fecha, invalida = interpretar_fecha(texto)
        trabajo[columna] = fecha
        reglas[columna + "_ausente"] = texto.isna()
        reglas[columna + "_invalida"] = invalida
    reglas["alta_posterior_corte"] = trabajo["fecha_alta"] > trabajo["fecha_corte"]
    clave_completa = trabajo[CLAVE].notna().all(axis=1)
    reglas["clave_repetida"] = clave_completa & trabajo.duplicated(subset=CLAVE, keep=False)
    banderas = pd.DataFrame(reglas, index=trabajo.index).fillna(False).astype("boolean")
    motivos = pd.Series("", index=trabajo.index, dtype="string")
    for nombre in banderas:
        mascara = banderas[nombre]
        separador = pd.Series("", index=trabajo.index, dtype="string")
        separador.loc[motivos != ""] = "; "
        motivos.loc[mascara] = motivos.loc[mascara] + separador.loc[mascara] + nombre
    trabajo["motivos"] = motivos
    trabajo["dias_desde_alta"] = (trabajo["fecha_corte"] - trabajo["fecha_alta"]).dt.days.astype("Int64")
    trabajo["mes_corte"] = trabajo["fecha_corte"].dt.month.astype("Int64")
    invalido = banderas.any(axis=1)
    aceptados, rechazados = trabajo.loc[~invalido].copy(), trabajo.loc[invalido].copy()
    juntos = pd.concat([aceptados, rechazados]).sort_values("numero_registro").reset_index(drop=True)
    pd.testing.assert_frame_equal(trabajo, juntos)
    if aceptados.duplicated(subset=CLAVE).any():
        raise ValueError("La clave normalizada aceptada no es unica")
    if len(aceptados) + len(rechazados) != len(tabla):
        raise ValueError("No concilian los registros")
    if trabajo["saldo_mxn"].sum() != aceptados["saldo_mxn"].sum() + rechazados["saldo_mxn"].sum():
        raise ValueError("No concilian los saldos de la particion")
    return trabajo, aceptados, rechazados, banderas


def seleccionar_periodo(tabla, inicio, fin):
    # Intervalo cerrado por la izquierda y abierto por la derecha.
    mascara = (tabla["fecha_corte"] >= pd.Timestamp(inicio)) & (tabla["fecha_corte"] < pd.Timestamp(fin))
    return tabla.loc[mascara].copy()


def exportar(tablas, entrada, carpeta):
    rutas = {nombre: carpeta / nombre for nombre in tablas}
    if any(r.resolve() == entrada.resolve() for r in rutas.values()):
        raise ValueError("Una salida reemplazaria la fuente")
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre, tabla in tablas.items():
        ruta = rutas[nombre]
        tabla.to_csv(ruta, index=False, encoding="utf-8", date_format="%Y-%m-%d", lineterminator="\n")
        tipos = {c: str(t) for c, t in tabla.dtypes.items() if c not in FECHAS}
        tipos.update({c: "string" for c in FECHAS})
        recargada = pd.read_csv(ruta, dtype=tipos, keep_default_na=False, na_values=[""])
        for c in FECHAS:
            recargada[c] = pd.to_datetime(recargada[c], format="%Y-%m-%d", errors="raise")
        recargada["motivos"] = recargada["motivos"].fillna("")
        pd.testing.assert_frame_equal(tabla.reset_index(drop=True), recargada, check_exact=True)


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta / "cartera_texto_fechas.csv"
    fuente = leer_fuente(entrada)
    original = fuente.copy()
    trabajo, aceptados, rechazados, banderas = preparar(fuente)
    pd.testing.assert_frame_equal(fuente, original)
    exportar({"normalizados.csv": trabajo, "aceptados.csv": aceptados, "rechazados.csv": rechazados},
             entrada, carpeta / "output")
    print(f"Entrada={len(fuente)}; aceptados={len(aceptados)}; rechazados={len(rechazados)}")
    for inicio, fin in [("2026-09-01", "2026-10-01"), ("2026-10-01", "2026-11-01")]:
        corte = seleccionar_periodo(aceptados, inicio, fin)
        print(f"Desde {inicio} hasta antes de {fin}: {len(corte)} filas; saldo={corte['saldo_mxn'].sum(min_count=1)}")
    print(banderas.sum().to_string())
    print("Tres exportaciones comprobadas; fuente intacta")


if __name__ == "__main__":
    main()
