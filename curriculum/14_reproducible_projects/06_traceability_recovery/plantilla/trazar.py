"""14.06: un registro nuevo por intento; no reanuda temporales ni oculta errores."""
from pathlib import Path
import argparse
import csv
from contextlib import redirect_stdout
from datetime import datetime, timezone
import platform
import re
import sys
import traceback

sys.dont_write_bytecode = True
from ejecutar import RAIZ, verificar_entorno
from configuracion import leer_configuracion
from modelo import cargar_fuente, resolver
from pipeline import pipeline, md5


def tabla(ruta, filas):
    with ruta.open("x", encoding="utf-8", newline="") as salida:
        csv.writer(salida, lineterminator="\n").writerows(filas)


def trazar(intento, archivo="config/consulta.csv", simular_fallo=False, simular_fallo_final=False):
    if not re.fullmatch(r"[a-z][a-z0-9_-]{0,39}", intento):
        raise ValueError("Intento: letra inicial y hasta 40 caracteres a-z, 0-9, _ o -")
    if simular_fallo and simular_fallo_final:
        raise ValueError("Elige una sola falla didactica")
    padre = RAIZ / "intentos"
    if padre.is_symlink() or (padre.exists() and padre.resolve() != padre):
        raise ValueError("Carpeta intentos enlazada")
    padre.mkdir(exist_ok=True)
    carpeta = padre / intento
    carpeta.mkdir(exist_ok=False)  # No se mezcla un intento con otro.
    eventos = carpeta / "eventos.csv"
    tabla(eventos, [["secuencia", "fecha_utc", "intento", "etapa", "evento", "detalle"]])
    secuencia = 0
    etapa = "entorno"

    def evento(tipo, detalle):
        nonlocal secuencia
        secuencia += 1
        # Abrir/cerrar por evento deja el prefijo legible ante un error ordinario.
        with eventos.open("a", encoding="utf-8", newline="") as salida:
            csv.writer(salida, lineterminator="\n").writerow([
                secuencia, datetime.now(timezone.utc).isoformat(), intento, etapa, tipo, detalle])

    evento("INICIO", "1406-v1; python " + platform.python_version())
    try:
        verificar_entorno()
        evento("OK", "Entorno local comprobado")
        etapa = "configuracion"
        cfg = leer_configuracion(RAIZ, archivo, permitir_existente=True)
        contexto = {k: cfg[k] for k in ("version_reglas", "entrada", "corte", "segmentos", "minimo_texto", "app", "salida")}
        contexto.update(config=archivo, raiz=str(RAIZ), ejecutable=sys.executable,
                        simular_fallo=str(simular_fallo), simular_fallo_final=str(simular_fallo_final))
        tabla(carpeta / "consulta.csv", [["clave", "valor"], *contexto.items()])
        evento("OK", cfg["salida"])
        etapa = "huellas"
        rutas = [archivo, cfg["entrada"], "entorno.csv", "uv.lock", "pyproject.toml",
                 "ejecutar.py", "revisar.py", "codigo/modelo.py", "codigo/configuracion.py", "pipeline.py", "trazar.py"]
        antes = [(r, md5(RAIZ / r)) for r in rutas]
        tabla(carpeta / "huellas.csv", [["archivo", "md5"], *antes])
        evento("OK", "Huellas de fuente, configuracion, codigo y metadatos")
        etapa = "fuente"
        datos = cargar_fuente(cfg["entrada_resuelta"])
        resultado = resolver(datos, cfg["corte"], cfg["segmentos"], cfg["minimo_texto"])
        evento("OK", "estado_consulta=" + resultado["estado"])
        etapa = "pipeline"
        evento("ENTRADA", "Ver consola.txt; la etapa agrupa escritura y comprobacion")
        with (carpeta / "consola.txt").open("x", encoding="utf-8") as consola:
            with redirect_stdout(consola):
                accion = pipeline(archivo, simular_fallo)
        evento("OK", accion)
        etapa = "cierre"
        if simular_fallo_final:
            raise RuntimeError("Fallo didactico despues de publicar/comprobar; revisar la entrega")
        if antes != [(r, md5(RAIZ / r)) for r in rutas]:
            raise ValueError("Insumos cambiaron durante el intento; revisar entrega en otro intento")
        evento("TERMINADO", accion)
        print("Intento terminado:", carpeta, "; entrega", accion)
        return accion
    except Exception as error:
        with (carpeta / "error.txt").open("x", encoding="utf-8") as diagnostico:
            traceback.print_exc(file=diagnostico)
        evento("FALLO", type(error).__name__ + ": " + str(error))
        raise  # Registrar no convierte el error en exito.


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("intento")
    p.add_argument("--config", default="config/consulta.csv")
    grupo = p.add_mutually_exclusive_group()
    grupo.add_argument("--simular-fallo", action="store_true")
    grupo.add_argument("--simular-fallo-final", action="store_true")
    a = p.parse_args()
    trazar(a.intento, a.config, a.simular_fallo, a.simular_fallo_final)
