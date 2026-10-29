"""Revisa configuracion y calcula una consulta. No genera archivos de resultado."""
from pathlib import Path
import sys
import argparse
sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "codigo"))
from configuracion import leer_configuracion
from modelo import cargar_fuente, resolver

def revisar(archivo="config/consulta.csv"):
    config = leer_configuracion(RAIZ, archivo)
    datos = cargar_fuente(config["entrada_resuelta"])
    resultado = resolver(datos, config["corte"], config["segmentos"], config["minimo_texto"])
    for clave in ("version_reglas", "entrada", "corte", "segmentos", "minimo_texto", "app", "salida"):
        print(f"{clave}: {config[clave]}")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
    print("Solo revision: no inicia app/reporte ni crea/reserva el destino de salida.")
    return resultado

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="config/consulta.csv", help="Ruta relativa a la raiz del proyecto")
    revisar(parser.parse_args().config)
