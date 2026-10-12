"""Preparar e inspeccionar una base didáctica sin modificar una base existente."""

from contextlib import closing
from datetime import date
from pathlib import Path
import argparse
import csv
import sqlite3


TABLAS = {
    "clientes": ["id_cliente", "alias", "region"],
    "creditos": ["id_credito", "id_cliente", "segmento"],
    "cortes": ["id_credito", "fecha_corte", "saldo_mxn", "dias_atraso"],
}


def cargar_fuentes(carpeta):
    fuentes = {}
    for nombre, columnas in TABLAS.items():
        with (carpeta / "data" / (nombre + ".csv")).open(encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            if lector.fieldnames != columnas:
                raise ValueError(f"Columnas inesperadas en {nombre}")
            filas = []
            for registro in lector:
                if nombre == "cortes":
                    texto = registro["fecha_corte"]
                    if date.fromisoformat(texto).isoformat() != texto:
                        raise ValueError("El corte requiere YYYY-MM-DD")
                    for columna in ["saldo_mxn", "dias_atraso"]:
                        registro[columna] = None if registro[columna] == "" else int(registro[columna])
                filas.append(tuple(registro[c] for c in columnas))
            fuentes[nombre] = filas
    return fuentes


def abrir_consulta(ruta):
    if not ruta.is_file():
        raise FileNotFoundError("Primero genera la base de la leccion")
    conexion = sqlite3.connect(ruta.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        conexion.execute("PRAGMA foreign_keys = ON")
        if conexion.execute("PRAGMA foreign_keys").fetchone()[0] != 1:
            raise RuntimeError("Este motor no tiene claves foraneas habilitadas")
    except Exception:
        conexion.close()
        raise
    return conexion


def comprobar(conexion, esperado):
    claves = {"clientes": ["id_cliente"], "creditos": ["id_credito"], "cortes": ["id_credito", "fecha_corte"]}
    referencias = {"clientes": [], "creditos": [("clientes", "id_cliente", "id_cliente")],
                   "cortes": [("creditos", "id_credito", "id_credito")]}
    for tabla, columnas in TABLAS.items():
        campos = conexion.execute(f"PRAGMA table_info({tabla})").fetchall()
        pk = [r[1] for r in sorted(campos, key=lambda r: r[5]) if r[5]]
        fk = [(r[2], r[3], r[4]) for r in conexion.execute(f"PRAGMA foreign_key_list({tabla})")]
        if [r[1] for r in campos] != columnas or pk != claves[tabla] or fk != referencias[tabla]:
            raise ValueError("El esquema de la base no coincide con el modelo de practica")
        if any(not r[3] for r in campos if r[1] in claves[tabla]):
            raise ValueError("La base no declara obligatoriedad para sus claves")
        # Nombres fijos del programa; los datos se cargan con parámetros, no SQL construido.
        resultado = conexion.execute(f"SELECT {', '.join(columnas)} FROM {tabla}").fetchall()
        if sorted(resultado) != sorted(esperado[tabla]):
            raise ValueError("La base no coincide con las fuentes; usa otra ruta de practica")
    if conexion.execute("PRAGMA foreign_key_check").fetchall():
        raise ValueError("Hay relaciones sin referencia valida")
    if conexion.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        raise ValueError("La base no pasa la comprobacion de integridad")


def preparar_base(ruta, carpeta):
    esperado = cargar_fuentes(carpeta)
    if ruta.exists():
        # No reiniciar ni borrar una base existente. Verificarla en modo de lectura.
        with closing(abrir_consulta(ruta)) as conexion:
            comprobar(conexion, esperado)
        return False
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(ruta)) as conexion:
        conexion.execute("PRAGMA foreign_keys = ON")
        if conexion.execute("PRAGMA foreign_keys").fetchone()[0] != 1:
            raise RuntimeError("No se pudieron habilitar las claves foraneas")
        try:
            conexion.executescript((carpeta / "schema.sql").read_text(encoding="utf-8"))
            for tabla, columnas in TABLAS.items():
                parametros = ", ".join("?" for _ in columnas)
                conexion.executemany(f"INSERT INTO {tabla} VALUES ({parametros})", esperado[tabla])
            comprobar(conexion, esperado)
            conexion.commit()
        except Exception:
            conexion.rollback()
            raise
    # Volver a abrir comprueba que los datos quedaron persistidos.
    with closing(abrir_consulta(ruta)) as conexion:
        comprobar(conexion, esperado)
    return True


def inspeccionar(ruta):
    with closing(abrir_consulta(ruta)) as conexion:
        print(f"SQLite: {sqlite3.sqlite_version}; base: {ruta.name}; modo: solo lectura")
        for tabla in TABLAS:
            cantidad = conexion.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]
            print(f"{tabla}: {cantidad} filas")
            print("  Campos y posiciones de clave primaria:",
                  [(r[1], r[2], r[5]) for r in conexion.execute(f"PRAGMA table_info({tabla})")])
        print("Ejemplo: observaciones de 001, ordenadas por corte")
        consulta = "SELECT id_credito, fecha_corte, saldo_mxn, dias_atraso FROM cortes WHERE id_credito = ? ORDER BY fecha_corte"
        for fila in conexion.execute(consulta, ("001",)):
            print(fila)
        print("Relaciones e integridad comprobadas al preparar; conexiones cerradas explicitamente")


def main():
    carpeta = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=carpeta / "output" / "cartera_demo.sqlite")
    argumentos = parser.parse_args()
    creada = preparar_base(argumentos.database, carpeta)
    print("Base creada y comprobada" if creada else "Base existente comprobada; sin modificaciones")
    inspeccionar(argumentos.database)


if __name__ == "__main__":
    main()
